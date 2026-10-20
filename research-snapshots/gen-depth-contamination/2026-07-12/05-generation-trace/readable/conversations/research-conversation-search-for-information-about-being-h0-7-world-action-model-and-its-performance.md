# Research conversation: Search for information about "Being-H0.7" world action model and its performance on LIBERO-Plus benchmark. I need to ver

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a176c3d82875e8fc3.jsonl`
- **Structured JSON:** [`7e017ac8f83d28d9f153.json`](../../sessions/7e/7e017ac8f83d28d9f153.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

47 recorded events

### User

_source line 1 · 2026-05-10T19:51:37.805Z_

Search for information about "Being-H0.7" world action model and its performance on LIBERO-Plus benchmark. I need to verify:
1. The claimed 82.1% success rate on LIBERO-Plus under distributional shift
2. What specific perturbations LIBERO-Plus uses
3. Whether Being-H0.7 generates video at test time or uses latent queries only

Also search for any papers that combine FFDC-WAM with other methods, or any results showing verification stacks improving robustness under distributional shift.

Use WebSearch with queries like:
- "Being-H0.7 LIBERO-Plus performance"
- "arXiv 2605.00078 Being-H0.7"
- "FFDC-WAM composability verification stack"

Then use WebFetch to read the Being-H0.7 paper abstract and results section if you find the arXiv link.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "3a3281dc-ce4c-49c2-9efb-1a8b2eb90023",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:51:37.809Z_

```json
{
  "parentUuid": "3a3281dc-ce4c-49c2-9efb-1a8b2eb90023",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "ad0cf55d-5f9c-4446-958e-dc35b33c57ec",
  "timestamp": "2026-05-10T19:51:37.809Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:51:41.255Z_



I'll start by loading the WebSearch and WebFetch tool schemas, then conduct the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad0cf55d-5f9c-4446-958e-dc35b33c57ec",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUGhPtnK4AKS1o7bKbm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c406ea08-f2d5-413e-b908-17da01aa2cd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XqB8FHH2VgjyVBAjE81SY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8040,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8040,
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

_source line 4 · 2026-05-10T19:51:41.388Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012LE7ohAZovtiJpasYnECNS`</summary>

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
  "parentUuid": "c406ea08-f2d5-413e-b908-17da01aa2cd8",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUGhPtnK4AKS1o7bKbm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa58413d-c103-4a95-9441-8463fbce7941",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XqB8FHH2VgjyVBAjE81SY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8040,
      "cache_read_input_tokens": 0,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8040
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8040,
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

_source line 5 · 2026-05-10T19:51:41.393Z_

<details><summary>↩ Tool result · `toolu_012LE7ohAZovtiJpasYnECNS`</summary>

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
  "parentUuid": "fa58413d-c103-4a95-9441-8463fbce7941",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "e7beda30-d7cd-4811-a16a-783bc62c2a2f",
  "sourceToolAssistantUUID": "fa58413d-c103-4a95-9441-8463fbce7941",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:51:45.395Z_

Now let me conduct the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7beda30-d7cd-4811-a16a-783bc62c2a2f",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUGxkdCgVyxAhskH7vf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "afd0b351-a0fa-4efa-bcb3-f579ee28d59b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQEXhBmXjt1tyjLemgmURb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 7 · 2026-05-10T19:51:45.987Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016CvUudrXDpsYVgMnxgEg9S`</summary>

```json
{
  "query": "Being-H0.7 LIBERO-Plus performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afd0b351-a0fa-4efa-bcb3-f579ee28d59b",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUGxkdCgVyxAhskH7vf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e75cc75f-7bda-4a6d-ac03-49b55c922ea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQEXhBmXjt1tyjLemgmURb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 8 · 2026-05-10T19:51:46.393Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DVypFxarMRU2E8tAQs8T33`</summary>

```json
{
  "query": "arXiv 2605.00078 Being-H0.7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e75cc75f-7bda-4a6d-ac03-49b55c922ea3",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUGxkdCgVyxAhskH7vf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52fd8d03-fc4e-4394-86af-5b50074568db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQEXhBmXjt1tyjLemgmURb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8040,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 8040,
          "cache_creation_input_tokens": 1910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1910,
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

_source line 9 · 2026-05-10T19:51:46.400Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MrSkrJqoddF7bHpif897dH`</summary>

```json
{
  "query": "FFDC-WAM composability verification stack"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52fd8d03-fc4e-4394-86af-5b50074568db",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUGxkdCgVyxAhskH7vf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "463dd117-bfc3-4c4a-830c-7d4caef2f398",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQEXhBmXjt1tyjLemgmURb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8040,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 166,
          "cache_read_input_tokens": 8040,
          "cache_creation_input_tokens": 1910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1910,
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

_source line 10 · 2026-05-10T19:51:53.176Z_

<details><summary>↩ Tool result · `toolu_01DVypFxarMRU2E8tAQs8T33`</summary>

```text
Web search results for query: "arXiv 2605.00078 Being-H0.7"

Links: [{"title":"Being-H0.7: A Latent World-Action Model from Egocentric Videos","url":"https://arxiv.org/html/2605.00078v1"},{"title":"GitHub - BeingBeyond/Being-H: Being-H is BeingBeyond's family of human-centric embodied foundation models. · GitHub","url":"https://github.com/BeingBeyond/Being-H"},{"title":"Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos","url":"https://arxiv.org/html/2507.15597v1"},{"title":"Being-H0","url":"https://beingbeyond.github.io/Being-H0/"},{"title":"Being-H0.5: Scaling Human-Centric Robot Learning for Cross ...","url":"https://research.beingbeyond.com/being-h05"},{"title":"[2507.15597] Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos","url":"https://arxiv.org/abs/2507.15597"},{"title":"BeingBeyond/Being-H0 · Hugging Face","url":"https://huggingface.co/BeingBeyond/Being-H0"},{"title":"Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization","url":"https://arxiv.org/html/2601.12993v1"},{"title":"[2601.12993] Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization","url":"https://arxiv.org/abs/2601.12993"},{"title":"[2605.06591] BRICKS: Compositional Neural Markov Kernels for Zero-Shot Radiation-Matter Simulation","url":"https://arxiv.org/abs/2605.06591"}]

I found information about arXiv paper 2605.00078, which is titled "Being-H0.7: A Latent World-Action Model from Egocentric Videos."

Being-H0.7 is a latent world-action model that brings future-aware reasoning into VLA-style policies without generating future frames. It inserts learnable latent queries between perception and action as a compact reasoning interface, and trains them with a future-informed dual-branch design: a deployable prior branch infers latent states from the current context, while a training-only posterior branch replaces the queries with embeddings from future observations.

Jointly aligning the two branches at the latent reasoning space leads the prior branch to reason future-aware, action-useful structure from current observations alone. At inference, Being-H0.7 discards the posterior branch and performs no visual rollout.

Experiments across six simulation benchmarks and diverse real-world tasks show that Being-H0.7 achieves state-of-the-art or comparable performance, combining the predictive benefits of world models with the efficiency and deployability of direct VLA policies. Within the Being-H family, Being-H0.7 is the flagship WAM (world-action model).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52fd8d03-fc4e-4394-86af-5b50074568db",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "17c4e4c1-ba26-427b-8640-ac9a7ed74932",
  "sourceToolAssistantUUID": "52fd8d03-fc4e-4394-86af-5b50074568db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T19:51:53.323Z_

<details><summary>↩ Tool result · `toolu_01MrSkrJqoddF7bHpif897dH`</summary>

```text
Web search results for query: "FFDC-WAM composability verification stack"

Links: [{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"How to enable First Failure Data Capture (FFDC) for VCS agent entry point using AdvDbg attribute?","url":"https://www.veritas.com/support/en_US/article.100038026"},{"title":"First Failure Data Capture (FFDC) logs for support analysis","url":"https://sort.veritas.com/public/documents/sf/5.1/aix/html/vcs_notes/ch01s03s03s04.htm"},{"title":"PI19830: PROVIDE STACK TRACE IN FFDC WHEN RESPONSE ALREADY COMMITTED (SESN0066E) SCENARIO OCCURS.","url":"https://www.ibm.com/support/pages/apar/PI19830"},{"title":"Sunil's Notes: Understanding FFDC log files","url":"http://wpcertification.blogspot.com/2009/06/understanding-ffdc-tool.html"},{"title":"An Introduction To Full Stack Composability — Smashing Magazine","url":"https://www.smashingmagazine.com/2023/11/introduction-full-stack-composability/"},{"title":"First failure data capture (FFDC)","url":"https://egeria-project.org/guides/diagnostic/ffdc/"},{"title":"PM48513: FFDC EXCEPTION IS GENERATED WHEN RUNNIG IN CLIENT ENVIRONMENT","url":"https://www.ibm.com/support/pages/apar/PM48513"},{"title":"Introduction To Full Stack Composability - GeeksforGeeks","url":"https://www.geeksforgeeks.org/introduction-to-full-stack-composability-1/"},{"title":"Composable Software/Composable CDP Meaning - CDP.com - Leading CDP Industry Resource for Marketing & Sales","url":"https://cdp.com/glossary/composable-software-composable-cdp/"}]

Based on the search results, I found information about **FFDC-WAM** in the context of robotic manipulation research:

FFDC (Future Forward Dynamics Causal Attention) is a lightweight verifier that jointly reasons over predicted future actions, predicted visual dynamics, real observations, and language instructions to estimate whether the remaining action rollout can still be trusted.

The WAM predicts future visual dynamics and an action chunk, while FFDC verifies during execution whether the imagined future remains consistent with the real observation, planned actions, and language instruction. FFDC uses a structured attention mechanism to model the interaction between predicted vision and action, allowing it to detect task-critical mismatches and decide whether the remaining rollout can still be trusted.

Regarding the composability verification stack aspect, this design turns WAM execution from fixed open-loop rollout into adaptive future-aware control. The system enables FFDC to detect when the imagined future becomes unreliable and trigger replanning, improving robustness.

This appears to be a recent robotics research advancement published on arXiv, focusing on making World Action Models more reliable and adaptive during execution through intelligent verification of predicted futures against actual observations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "463dd117-bfc3-4c4a-830c-7d4caef2f398",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "94e86b1f-3987-4df8-8f38-cca4efc3d3d3",
  "sourceToolAssistantUUID": "463dd117-bfc3-4c4a-830c-7d4caef2f398",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T19:52:04.197Z_

<details><summary>↩ Tool result · `toolu_016CvUudrXDpsYVgMnxgEg9S`</summary>

```text
Web search results for query: "Being-H0.7 LIBERO-Plus performance"

Links: [{"title":"Being-H0","url":"https://beingbeyond.github.io/Being-H0/"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"},{"title":"Giordano Libero 1.6 | Road Bike, Cycling Forums","url":"https://www.roadbikereview.com/threads/giordano-libero-1-6.303914/"},{"title":"Libero Comfort 7 Diaper 16-26Kg x20 | Cosmetic2Go.com","url":"https://www.cosmetic2go.com/en/buy/libero-comfort-7-diaper-1626kg-x20"}]

Based on the search results, I found information about LIBERO-Plus and some information about Being-H0, though not specifically about "Being-H0.7" performance on LIBERO-Plus.

## LIBERO-Plus Overview

LIBERO-Plus is a generalized benchmark for in-depth robustness analysis of vision-language-action models. It systematically exposes the hidden vulnerabilities of contemporary VLA models through comprehensive robustness evaluation across seven perturbation dimensions.

## Key Findings on VLA Model Performance

Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. Additionally, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

## Regarding Being-H0

The search results mention Being-H0 as the first dexterous Vision-Language-Action model pretrained from large-scale human videos via explicit hand motion modeling, which by explicitly modeling hand motions, the resulting foundation model seamlessly transfers from human hand demonstrations to robotic manipulation.

However, the search results do not contain specific performance metrics for "Being-H0.7" on the LIBERO-Plus benchmark. To get detailed performance information about this specific model version, you may want to check the Being-H0 project page or recent research papers directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e75cc75f-7bda-4a6d-ac03-49b55c922ea3",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "29ca072f-463e-4f16-bfdd-d21c2288ec2b",
  "sourceToolAssistantUUID": "e75cc75f-7bda-4a6d-ac03-49b55c922ea3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T19:52:08.474Z_

I found the arXiv paper. Let me now fetch the Being-H0.7 paper and the FFDC-WAM paper for more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29ca072f-463e-4f16-bfdd-d21c2288ec2b",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUJddVK545TsV1K1ibr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e05d4a2a-11fa-4acf-b2c6-ee3bf6d023dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsQ2PMdKW4n4nPrrjaqSur",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1617,
      "cache_creation_input_tokens": 1033,
      "cache_read_input_tokens": 9950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1033,
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

_source line 14 · 2026-05-10T19:52:11.977Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ByUuXJqFeBS3EMSzk9NXSb`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.00078v1",
  "prompt": "Extract the following information: 1) The exact claimed success rate on LIBERO-Plus benchmark under distributional shift. 2) What specific perturbations LIBERO-Plus uses in their evaluation. 3) Whether Being-H0.7 generates video at test time or uses latent queries only at inference. 4) The architecture details about the prior and posterior branches. 5) Any results tables showing performance numbers on LIBERO-Plus or other benchmarks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e05d4a2a-11fa-4acf-b2c6-ee3bf6d023dd",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUJddVK545TsV1K1ibr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "674efea4-cfa3-4f61-a72d-0cacae361235",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsQ2PMdKW4n4nPrrjaqSur",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1617,
      "cache_creation_input_tokens": 1033,
      "cache_read_input_tokens": 9950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1033,
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

_source line 15 · 2026-05-10T19:52:13.425Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Nsgc5JNzHiUykLtAFNndfA`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06222",
  "prompt": "Extract information about: 1) FFDC-WAM and how it works. 2) Any combination with other methods or verification stacks. 3) Any results showing improved robustness under distributional shift. 4) Performance on LIBERO-Plus or similar benchmarks. 5) Whether Being-H0.7 is mentioned or used as a base model."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "674efea4-cfa3-4f61-a72d-0cacae361235",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUJddVK545TsV1K1ibr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af077901-de30-4c9c-9d93-2eea598b1148",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsQ2PMdKW4n4nPrrjaqSur",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1617,
      "cache_creation_input_tokens": 1033,
      "cache_read_input_tokens": 9950,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1033
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1617,
          "output_tokens": 364,
          "cache_read_input_tokens": 9950,
          "cache_creation_input_tokens": 1033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1033,
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

_source line 16 · 2026-05-10T19:52:17.606Z_

<details><summary>↩ Tool result · `toolu_01ByUuXJqFeBS3EMSzk9NXSb`</summary>

```text
# Being-H0.7 Key Information

**1) LIBERO-Plus Success Rate Under Distribution Shift:**
The model achieves "a 82.1% zero-shot success rate" on the standard LIBERO-Plus evaluation, which "further improves to 84.8% after fine-tuning on LIBERO-plus."

**2) LIBERO-Plus Perturbations:**
The benchmark "incorporates structured domain randomization along five axes: table-top clutter, varied lighting conditions, diverse background textures, tabletop height variations, and diverse language instructions."

**3) Test-Time Video Generation:**
Being-H0.7 does **not** generate video at inference. The authors explicitly state: "At inference, Being-H0.7 discards the posterior branch and performs no visual rollout." Instead, it uses only learnable latent queries for reasoning.

**4) Prior and Posterior Branch Architecture:**
- **Prior branch**: Uses learnable latent queries (K=16) to infer action-relevant state from current context alone
- **Posterior branch**: Replaces queries with future embeddings extracted via frozen ViT and Perceiver resampler, providing privileged supervision during training only
- Both branches share identical context and backbone, coupled through hidden-state alignment loss at the latent reasoning positions

**5) Performance Table:**
Table 1 shows Being-H0.7 (3B model) achieving 99.2% on LIBERO, 82.1% on LIBERO-plus (zero-shot), and 84.8% on LIBERO-plus after fine-tuning—outperforming comparable baselines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "674efea4-cfa3-4f61-a72d-0cacae361235",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "3c25e05d-970b-4f28-bd82-275f0f246e3c",
  "sourceToolAssistantUUID": "674efea4-cfa3-4f61-a72d-0cacae361235",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T19:52:20.297Z_

<details><summary>↩ Tool result · `toolu_01Nsgc5JNzHiUykLtAFNndfA`</summary>

```text
# Analysis of FFDC-WAM Research

## 1) FFDC-WAM Overview

**Future Forward Dynamics Causal Attention (FFDC-WAM)** operates as an adaptive execution framework for World Action Models. The system works by comparing WAM-predicted visual futures against real observations during task execution. As described: "the robot should execute longer when the WAM-predicted future remains reliable, and replan earlier when reality deviates from imagination."

The verifier uses structured attention mechanisms to analyze temporally-aligned interactions between predicted actions, predicted visual tokens, current observations, and language instructions. A confidence score determines whether to continue or trigger replanning.

## 2) Integration with Other Methods

The research builds exclusively on **Motus**, a unified latent action world model. No combinations with other verification approaches or stacks are discussed. The method represents a self-contained enhancement to Motus rather than complementary integration with competing systems.

## 3) Distributional Shift Results

The benchmark includes explicit robustness testing under distribution shift:

- **Random setting (with perturbations)**: "69.10% reduction in WAM forward passes" compared to baseline while achieving "2.54% success rate improvement"
- Hard task performance: Success rate increases from 54.20% to 76.40% under randomized conditions
- The system demonstrates "difficulty-aware behavior" by allocating computation adaptively

## 4) LIBERO-Plus or Similar Benchmarks

The evaluation uses **RoboTwin benchmark** exclusively (50 manipulation tasks with clean and random settings), plus limited real-world testing. No mention of LIBERO-Plus or comparable standardized benchmarks appears in the document.

## 5) Being-H0.7 Reference

Being-H0.7 is cited once in the related work bibliography as "a latent world-action model from egocentric videos" but is **not used** as a base model or integrated into the approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af077901-de30-4c9c-9d93-2eea598b1148",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "b29f5d37-367c-4425-a55c-147a8ea25c89",
  "sourceToolAssistantUUID": "af077901-de30-4c9c-9d93-2eea598b1148",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T19:52:24.215Z_

Now let me search for any additional information about combining FFDC-WAM with other methods or verification stacks improving distributional shift robustness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b29f5d37-367c-4425-a55c-147a8ea25c89",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUKpTdYQhostDTjPGB7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55eaebe4-d45e-4c3e-8957-dbfd66c0a481",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zxuqrV8j1FBKDnypjWfKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2848,
      "cache_read_input_tokens": 10983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2848,
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

_source line 19 · 2026-05-10T19:52:24.691Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QJ1Yz4uqzPeAjTxDeFKMR5`</summary>

```json
{
  "query": "\"FFDC-WAM\" \"Being-H0.7\" combined distributional shift robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55eaebe4-d45e-4c3e-8957-dbfd66c0a481",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUKpTdYQhostDTjPGB7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bcfdee24-5014-4aad-8ab1-ce4084d0d498",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zxuqrV8j1FBKDnypjWfKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2848,
      "cache_read_input_tokens": 10983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2848,
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

_source line 20 · 2026-05-10T19:52:25.268Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jo4NozKedwnaWezPDHnrni`</summary>

```json
{
  "query": "world action model verification stack robustness distributional shift LIBERO-Plus 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcfdee24-5014-4aad-8ab1-ce4084d0d498",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUKpTdYQhostDTjPGB7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd5311ca-030d-4d21-a1fd-f0f302a3b102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zxuqrV8j1FBKDnypjWfKB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2848,
      "cache_read_input_tokens": 10983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2848,
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

_source line 21 · 2026-05-10T19:52:32.546Z_

<details><summary>↩ Tool result · `toolu_01Jo4NozKedwnaWezPDHnrni`</summary>

```text
Web search results for query: "world action model verification stack robustness distributional shift LIBERO-Plus 2026"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry","url":"https://arxiv.org/html/2604.01985"},{"title":"[2603.22078] Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/abs/2603.22078"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"Paper page - Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://huggingface.co/papers/2603.22078"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"Reshaping Action Error Distributions for Reliable Vision-Language-Action Models","url":"https://arxiv.org/html/2602.04228"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study [Quick Review]","url":"https://liner.com/review/do-world-action-models-generalize-better-than-vlas-robustness-study"}]

Based on the web search results, here's what I found regarding your query about world action models, verification stacks, robustness, and distributional shift in relation to LIBERO-Plus and 2026:

## Key Findings:

### LIBERO-Plus Benchmark
LIBERO-Plus is a benchmark designed to rigorously evaluate generalization capabilities, constructed through two main steps: systematically expanding the original LIBERO benchmark by applying seven distinct perturbation factors, followed by evaluating tasks using four representative models and stratifying them into five difficulty levels. The resulting benchmark comprises 10,030 tasks spanning seven perturbation factors with twenty-one low-level components.

### Robustness Under Distributional Shift
The analysis introduces controlled perturbations across seven dimensions including objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise, with models exhibiting extreme sensitivity to perturbation factors and performance dropping from 95% to below 30% under modest perturbations.

### World Action Models vs. VLAs
World Action Models (WAMs) achieve strong robustness, with LingBot-VA reaching 74.2% success rate on RoboTwin 2.0-Plus and Cosmos-Policy achieving 82.2% on LIBERO-Plus. WAMs generally exhibit strong robustness to noise, lighting, and layout perturbations, attributed to spatiotemporal priors from world model backbones.

### World Action Verifier
Research validates whether inverse verification, especially with sparsity, is more robust and easier to learn than action-conditioned forward prediction under limited data and distribution shift.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd5311ca-030d-4d21-a1fd-f0f302a3b102",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "75612d1d-16b4-4ab0-82df-9d686c74b9ac",
  "sourceToolAssistantUUID": "fd5311ca-030d-4d21-a1fd-f0f302a3b102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T19:52:32.697Z_

<details><summary>↩ Tool result · `toolu_01QJ1Yz4uqzPeAjTxDeFKMR5`</summary>

```text
Web search results for query: ""FFDC-WAM" "Being-H0.7" combined distributional shift robustness 2025 2026"

Links: [{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"An Analysis of Model Robustness across Concurrent Distribution Shifts","url":"https://arxiv.org/html/2501.04288v1"},{"title":"Measuring Robustness to Natural Distribution Shifts in Image Classiﬁcation","url":"https://proceedings.neurips.cc/paper/2020/file/d8330f857a17c53d217014ee776bfd50-Paper.pdf"},{"title":"Evaluating Model Robustness and Stability to Dataset Shift","url":"http://proceedings.mlr.press/v130/subbaswamy21a/subbaswamy21a.pdf"},{"title":"Provable Robustness against Wasserstein Distribution Shifts via Input Randomization | OpenReview","url":"https://openreview.net/forum?id=HJFVrpCaGE"},{"title":"An Analysis of Model Robustness across Concurrent Distribution Shifts | OpenReview","url":"https://openreview.net/forum?id=nxQtoHHcj9"},{"title":"(PDF) Shifts: A Dataset of Real Distributional Shift Across Multiple Large-Scale Tasks","url":"https://www.researchgate.net/publication/353284527_Shifts_A_Dataset_of_Real_Distributional_Shift_Across_Multiple_Large-Scale_Tasks"},{"title":"Quantifying Distribution Shifts and Uncertainties for Enhanced Model Robustness in Machine Learning Applications | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/quantifying-distribution-shifts-uncertainties-enhanced-model-robustness"},{"title":"Quantifying Distribution Shifts and Uncertainties for Enhanced Model Robustness in Machine Learning Applications","url":"https://arxiv.org/html/2405.01978v1"},{"title":"The Many Faces of Robustness: A Critical Analysis of","url":"https://openaccess.thecvf.com/content/ICCV2021/papers/Hendrycks_The_Many_Faces_of_Robustness_A_Critical_Analysis_of_Out-of-Distribution_ICCV_2021_paper.pdf"}]

Based on my search results, I found information about "FFDC-WAM" in recent research. Here's what I discovered:

"FFDC" stands for Future Forward Dynamics Causal Attention, which is "a lightweight verifier that jointly reasons over predicted future actions, predicted visual dynamics, real observations, and language instructions to estimate whether the remaining action rollout can still be trusted." The "FFDC-WAM" system combines this verification mechanism with World Action Models (WAMs) to move "WAM execution beyond fixed-horizon chunking toward a more principled reliability-aware control strategy, improving both efficiency and robustness."

However, I did not find any search results specifically referencing "Being-H0.7" as a model or benchmark name in combination with "FFDC-WAM" and "combined distributional shift robustness" from 2025-2026. The FFDC-WAM paper I found (dated 3 days ago, from May 2025) focuses on robotic control and world model execution rather than explicitly addressing combined distributional shifts using that specific model designation.

The search results do contain extensive research on distributional shift robustness more broadly, but the specific combination of terms you're searching for doesn't appear in the available results. If you have additional context about where "Being-H0.7" comes from or what domain it relates to, I'd be happy to perform another search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcfdee24-5014-4aad-8ab1-ce4084d0d498",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "179e0a08-c575-4f9d-946b-4956619de4c7",
  "sourceToolAssistantUUID": "bcfdee24-5014-4aad-8ab1-ce4084d0d498",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T19:52:36.578Z_

Let me fetch the robustness study paper that directly compares WAMs on LIBERO-Plus, and look for more details on FFDC-WAM composability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "179e0a08-c575-4f9d-946b-4956619de4c7",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauULjSYLkX6MuLTGNbkm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9e56dd3-0121-4792-95c7-faafb3ea8bb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6EQwUHoCzDUdzys5fhUnT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 905,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 13831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-10T19:52:38.980Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01McvahcsDPoQ9iqruKtu8dT`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.22078",
  "prompt": "Extract key findings about: 1) Which World Action Models were tested on LIBERO-Plus. 2) Being-H0.7 performance specifically. 3) Any mention of FFDC-WAM or verification stacks. 4) The exact perturbation types used in LIBERO-Plus. 5) Any results showing WAMs improving robustness under distributional shift compared to VLAs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9e56dd3-0121-4792-95c7-faafb3ea8bb8",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauULjSYLkX6MuLTGNbkm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffcb9da7-f8fe-4c5d-b7b4-05d327e85b09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6EQwUHoCzDUdzys5fhUnT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 905,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 13831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1126,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-10T19:52:39.372Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014qaqSJAZhdcfEEszjCudtG`</summary>

```json
{
  "query": "\"Being-H0.7\" \"LIBERO-Plus\" 82.1 success rate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffcb9da7-f8fe-4c5d-b7b4-05d327e85b09",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauULjSYLkX6MuLTGNbkm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52175a5c-c752-4ad8-befb-21b782d31af9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6EQwUHoCzDUdzys5fhUnT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 905,
      "cache_creation_input_tokens": 1126,
      "cache_read_input_tokens": 13831,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 905,
          "output_tokens": 265,
          "cache_read_input_tokens": 13831,
          "cache_creation_input_tokens": 1126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1126,
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

_source line 26 · 2026-05-10T19:52:44.094Z_

<details><summary>↩ Tool result · `toolu_014qaqSJAZhdcfEEszjCudtG`</summary>

```text
Web search results for query: ""Being-H0.7" "LIBERO-Plus" 82.1 success rate"

Links: [{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"},{"title":"PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/711"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%? · Issue #734 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/734"},{"title":"LIBERO-Object: Lifelong Learning in Robotic Manipulation","url":"https://www.emergentmind.com/topics/libero-object"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"}]

Based on the search results, I found relevant information about LIBERO-Plus and success rates. Cosmos-Policy achieved 82.2% on LIBERO-Plus, which is very close to the 82.1% success rate you mentioned in your query.

However, I did not find specific information about "Being-H0.7" in the search results. The results show various VLA (Vision-Language-Action) models being evaluated on LIBERO-Plus benchmarks with different success rates, but this particular model designation doesn't appear in the retrieved sources.

The search results indicate that LIBERO-Plus is used to evaluate model performance under various visual and language perturbations, and that various world action models and VLA models achieve different success rates on this benchmark.

If you're looking for more specific information about "Being-H0.7," you may want to search with additional context or check if this might be a model variant with a different naming convention in the literature.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52175a5c-c752-4ad8-befb-21b782d31af9",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "ad6dd871-e7e1-4a95-8de7-6f1323d6b171",
  "sourceToolAssistantUUID": "52175a5c-c752-4ad8-befb-21b782d31af9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T19:52:44.168Z_

<details><summary>↩ Tool result · `toolu_01McvahcsDPoQ9iqruKtu8dT`</summary>

```text
# Analysis of arXiv Paper 2603.22078

Based on the webpage content provided, here's what I can extract:

## 1) World Action Models Tested on LIBERO-Plus
The abstract mentions **Cosmos-Policy** as achieving "82.2% on LIBERO-Plus," making it the explicitly named WAM tested on this benchmark.

## 2) Being-H0.7 Performance
**No information found.** The document does not reference a model with this designation.

## 3) FFDC-WAM or Verification Stacks
**No mention found.** Neither term appears in the available content.

## 4) Exact Perturbation Types for LIBERO-Plus
The abstract indicates evaluation occurred "under various visual and language perturbations" but does not specify the exact types of perturbations applied to this particular benchmark.

## 5) WAMs vs VLAs Under Distributional Shift
The key finding states: "WAMs achieve strong robustness" with specific success rates noted, while "VLAs such as π₀.₅ can achieve comparable robustness on certain tasks" but "typically require extensive training with diverse robotic datasets." This suggests WAMs show superior generalization, though the comparison is qualified as task-dependent.

---

**Note:** The full paper would likely contain detailed methodology and results tables with the specific information you're seeking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffcb9da7-f8fe-4c5d-b7b4-05d327e85b09",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "140a605e-c85c-43b7-b2d9-d20e50173d5b",
  "sourceToolAssistantUUID": "ffcb9da7-f8fe-4c5d-b7b4-05d327e85b09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T19:52:49.127Z_

Let me fetch the full HTML version of the Being-H0.7 paper to get details on the LIBERO-Plus results table and the robustness study paper for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "140a605e-c85c-43b7-b2d9-d20e50173d5b",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUMaWJAcYSfrX8Ysuyh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63f8e461-227e-4001-991b-48d5427c0178",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wyPXAJhSQxhxPuGUDfQbm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 777,
      "cache_creation_input_tokens": 1511,
      "cache_read_input_tokens": 14957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1511,
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

_source line 29 · 2026-05-10T19:52:51.469Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VczB3yCtgMVs3SdSmQ4yKE`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.22078v1",
  "prompt": "Extract: 1) The full results table showing Being-H0.7 or any WAMs on LIBERO-Plus. 2) Exact perturbation categories in LIBERO-Plus. 3) Any mention of FFDC-WAM or verification stacks combined with WAMs. 4) The 82.1% or 82.2% success rate - which model achieves it and under what conditions. 5) Any discussion of Being-H0.7 specifically."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63f8e461-227e-4001-991b-48d5427c0178",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUMaWJAcYSfrX8Ysuyh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df9497e4-3edc-4045-9810-771a86186bfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wyPXAJhSQxhxPuGUDfQbm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 777,
      "cache_creation_input_tokens": 1511,
      "cache_read_input_tokens": 14957,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1511
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 777,
          "output_tokens": 283,
          "cache_read_input_tokens": 14957,
          "cache_creation_input_tokens": 1511,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1511,
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

_source line 30 · 2026-05-10T19:52:51.695Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C23oDYWPtDnLLpS3z8bYRj`</summary>

```json
{
  "query": "\"Being-H0.7\" latent world action model results table benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df9497e4-3edc-4045-9810-771a86186bfa",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUMaWJAcYSfrX8Ysuyh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9f2887a-1b8c-4713-8e52-061bdfae875e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013wyPXAJhSQxhxPuGUDfQbm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 777,
      "cache_creation_input_tokens": 1511,
      "cache_read_input_tokens": 14957,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1511
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 777,
          "output_tokens": 283,
          "cache_read_input_tokens": 14957,
          "cache_creation_input_tokens": 1511,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1511,
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

_source line 31 · 2026-05-10T19:52:56.694Z_

<details><summary>↩ Tool result · `toolu_01VczB3yCtgMVs3SdSmQ4yKE`</summary>

```text
# Analysis of Requested Information from Paper

## 1) Full Results Table for LIBERO-Plus

Table 4 shows LIBERO-Plus results. The top WAM performers are:
- **Cosmos-Policy**: 98.5% original, 82.2% overall with perturbations
- **GE-Act**: 94.4% original, 80.3% overall

No model named "Being-H0.7" appears in the document.

## 2) Exact Perturbation Categories in LIBERO-Plus

The paper identifies seven perturbation dimensions:
- Camera (viewpoint changes)
- Robot (initial state variations)
- Language (instruction modifications)
- Light (illumination alterations)
- Background (texture changes)
- Noise (photometric distortions)
- Layout (distracting objects)

## 3) FFDC-WAM or Verification Stacks

No mention of "FFDC-WAM" or "verification stacks combined with WAMs" appears anywhere in the document.

## 4) The 82.2% Success Rate

"Cosmos-Policy achieving 82.2% on LIBERO-Plus" represents the model's overall success rate across all perturbation types evaluated on that benchmark.

## 5) Being-H0.7 Discussion

This model does not appear in the paper. The document evaluates models like π₀.₅, Cosmos-Policy, GE-Act, and LingBot-VA, but contains no reference to "Being-H0.7."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df9497e4-3edc-4045-9810-771a86186bfa",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "495ad476-b0c9-4fc6-a489-507a1521db52",
  "sourceToolAssistantUUID": "df9497e4-3edc-4045-9810-771a86186bfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T19:52:59.617Z_

<details><summary>↩ Tool result · `toolu_01C23oDYWPtDnLLpS3z8bYRj`</summary>

```text
Web search results for query: ""Being-H0.7" latent world action model results table benchmarks"

Links: [{"title":"Being-H0.7: A Latent World-Action Model from ... - BeingBeyond","url":"https://research.beingbeyond.com/being-h07"},{"title":"Being-H0.7: A Latent World-Action Model from Egocentric Videos","url":"https://arxiv.org/html/2605.00078v1"},{"title":"GitHub - BeingBeyond/Being-H: Being-H is BeingBeyond's family of human-centric embodied foundation models. · GitHub","url":"https://github.com/BeingBeyond/Being-H"},{"title":"BeingBeyond Unveils World's Most Powerful Model: Embodied Industry Enters the \"Brain Era\"","url":"https://eu.36kr.com/en/p/3766161393369609"},{"title":"Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization","url":"https://arxiv.org/html/2601.12993v1"},{"title":"Latent Action World Models for Control with Unlabeled Trajectories","url":"https://arxiv.org/html/2512.10016"},{"title":"Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos","url":"https://arxiv.org/html/2507.15597v1"},{"title":"Latent State Design for World Models under Sufficiency Constraints","url":"https://arxiv.org/html/2605.01694"},{"title":"A Survey of Embodied World Models Yu Shang1 Yinzhou Tang1∗ Xin Zhang1∗","url":"https://fi.ee.tsinghua.edu.cn/public/publications/0940dda4-af15-11f0-9d60-0242ac120002.pdf"},{"title":"[2601.05230] Learning Latent Action World Models In The Wild","url":"https://arxiv.org/abs/2601.05230"}]

I found information about Being-H0.7, a latent world-action model. Here are the key findings:

## Overview

Being-H0.7 is a latent world-action model that bridges direct action prediction and world modeling through a compact latent reasoning space, bringing future-aware reasoning into VLA-style policies without generating future frames.

## Benchmark Results

Across six widely used simulation benchmarks, Being-H0.7 reaches the strongest overall performance and the best average rank. More specifically:

Being-H0.7 sits on or near the frontier across almost every axis at once, including LIBERO, both LIBERO-plus settings, GR1, and both CALVIN splits, while remaining highly competitive on RoboCasa and Robotwin2.

In the experimental results, Being-H0.7 ranked first globally in 6 lists (topping 4 of them), becoming one of the most comprehensive embodied world models in terms of coverage.

## Key Performance Characteristics

The shape of that performance is that standard tabletop control, perturbation robustness, bimanual dexterity, long-horizon sequencing, and zero-shot environment shift all move together rather than trading off against one another.

The research paper and official documentation reference these benchmarks, but the web search results did not return a detailed numerical results table. For specific numerical scores on each benchmark, you may want to consult the full arxiv paper at https://arxiv.org/html/2605.00078v1 or the official research page at https://research.beingbeyond.com/being-h07.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9f2887a-1b8c-4713-8e52-061bdfae875e",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "75ec2568-9e7d-4fcb-85ca-8146f8d36bb5",
  "sourceToolAssistantUUID": "a9f2887a-1b8c-4713-8e52-061bdfae875e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-10T19:53:05.673Z_

Let me fetch the official Being-H0.7 research page for more detailed results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75ec2568-9e7d-4fcb-85ca-8146f8d36bb5",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUNiZWg1QA32jHpdSii",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "93133ca0-0274-43bf-9ae4-c30bc836f9b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VFgiBDoXuGhxLBxgMV244z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2363,
      "cache_read_input_tokens": 16468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2363,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-10T19:53:07.645Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PURa2tiQPQtk2Enb2RErGL`</summary>

```json
{
  "url": "https://research.beingbeyond.com/being-h07",
  "prompt": "Extract: 1) The exact LIBERO-Plus success rate numbers (is it 82.1%?). 2) Whether the model generates video at test time. 3) Specific benchmark results tables. 4) Any mention of distributional shift or perturbation robustness results. 5) Details about the latent query mechanism at inference time."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93133ca0-0274-43bf-9ae4-c30bc836f9b8",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUNiZWg1QA32jHpdSii",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbac2d23-45fa-429f-ac8e-cb2242557615",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VFgiBDoXuGhxLBxgMV244z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2363,
      "cache_read_input_tokens": 16468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2363,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-10T19:53:08.180Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HDjrwsYqJe3cDKi3zs74b6`</summary>

```json
{
  "query": "\"FFDC\" \"world action model\" adaptive execution replanning robustness improvement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbac2d23-45fa-429f-ac8e-cb2242557615",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUNiZWg1QA32jHpdSii",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9fd01b73-bfdd-4eb5-9810-2a6c0e740c35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VFgiBDoXuGhxLBxgMV244z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2363,
      "cache_read_input_tokens": 16468,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2363
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 16468,
          "cache_creation_input_tokens": 2363,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2363,
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

_source line 36 · 2026-05-10T19:53:12.174Z_

<details><summary>↩ Tool result · `toolu_01PURa2tiQPQtk2Enb2RErGL`</summary>

```text
Based on the web page content provided:

**1) LIBERO-Plus Success Rate Numbers:**
The page does not include specific numerical success rates for LIBERO-Plus. It only states that Being-H0.7 "sits on or near the frontier" across benchmarks including LIBERO-Plus.

**2) Video Generation at Test Time:**
No. The model explicitly does not generate video during deployment. The approach represents "a way to use future structure without turning deployment into a video-generation problem."

**3) Specific Benchmark Results Tables:**
The page contains no numerical tables. Results are presented through a radar chart visualization showing relative performance across benchmarks, but exact figures are not provided in tabular form.

**4) Distributional Shift and Perturbation Robustness:**
The page mentions these capabilities exist—the text references "perturbation robustness" and "zero-shot environment shift" as performance dimensions measured across benchmarks. However, specific numerical results are not disclosed.

**5) Latent Query Mechanism at Inference:**
During inference, the model "only uses the current instruction, observation history, state, and latent queries." These learnable latent queries serve as an "internal world-action workspace," but the document does not elaborate on their specific computational mechanism or dimensionality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbac2d23-45fa-429f-ac8e-cb2242557615",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "8e02adbc-efd1-42ea-a742-ce247bf76a16",
  "sourceToolAssistantUUID": "bbac2d23-45fa-429f-ac8e-cb2242557615",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-10T19:53:14.587Z_

<details><summary>↩ Tool result · `toolu_01HDjrwsYqJe3cDKi3zs74b6`</summary>

```text
Web search results for query: ""FFDC" "world action model" adaptive execution replanning robustness improvement"

Links: [{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"[2605.06222] When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/abs/2605.06222"},{"title":"Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection","url":"https://arxiv.org/html/2604.13942"},{"title":"Planner–Executor Framework","url":"https://www.emergentmind.com/topics/planner-executor-framework"},{"title":"RoboPilot: Generalizable Dynamic Robotic Manipulation with Dual-thinking Modes","url":"https://arxiv.org/html/2510.00154"},{"title":"A Hierarchical Error-Corrective Graph Framework for Autonomous Agents with LLM-Based Action Generation","url":"https://arxiv.org/html/2603.08388"},{"title":"Dynamic Adaptive Policy Pathways (DAPP)","url":"https://uncertainfutures.github.io/theory/DAPP/"},{"title":"Task and Motion Planning for Execution in the Real","url":"https://arxiv.org/html/2406.03641"},{"title":"Reconfiguration and Replanning for Robust Execution of ...","url":"https://dott-informatica.campusnet.unito.it/html/theses/scala.pdf"},{"title":"Leveraging Pre-trained Large Language Models with Refined Prompting for Online Task and Motion Planning","url":"https://arxiv.org/html/2504.21596"}]

Based on the search results, I found highly relevant information about FFDC and world action models:

## Summary of Findings

FFDC (Future Forward Dynamics Causal Attention) is a lightweight verifier that jointly reasons over predicted future actions, predicted visual dynamics, real observations, and language instructions to estimate whether the remaining action rollout can still be trusted.

### Adaptive Execution and Replanning

FFDC formulates adaptive WAM (World Action Model) execution as a future-reality verification problem: the robot should execute longer when the WAM-predicted future remains reliable, and replan earlier when reality deviates from imagination.

### Robustness Improvement

In difficult phases, FFDC detects when the imagined future becomes unreliable and triggers replanning, improving robustness. Additionally, FFDC enables adaptive action chunk sizes as an emergent consequence of prediction–observation consistency, preserving the efficiency of long-horizon execution while restoring responsiveness in contact-rich or difficult phases.

### Key Results

FFDC achieves the highest success rate while significantly reducing task completion time. The approach has been validated on both the RoboTwin benchmark and in real-world robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fd01b73-bfdd-4eb5-9810-2a6c0e740c35",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "f83cdf46-9a0b-4fdd-9168-d6038c459f4b",
  "sourceToolAssistantUUID": "9fd01b73-bfdd-4eb5-9810-2a6c0e740c35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-10T19:53:19.349Z_

Now let me get the precise numbers from the Being-H0.7 arXiv paper and check for any combined FFDC+Being-H0.7 work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f83cdf46-9a0b-4fdd-9168-d6038c459f4b",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUPpdAoqE8XoqMADGbp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d24ef6b9-3940-466d-9e6b-c08cb9e2dc56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wci9L8y67fzXyYRQcwVukD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 18831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1290,
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

_source line 39 · 2026-05-10T19:53:22.437Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ea2k1WARccTxZfkNbCiSS5`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.00078v1",
  "prompt": "Find and extract the exact numerical results from Table 1 or any results table. I need the specific numbers for Being-H0.7 on LIBERO-Plus (zero-shot and fine-tuned). Also list what other models are in the comparison table and their LIBERO-Plus scores. Look for any mention of 82.1% specifically."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d24ef6b9-3940-466d-9e6b-c08cb9e2dc56",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUPpdAoqE8XoqMADGbp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46c30147-6edc-45e2-a079-1aa4ccc043b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wci9L8y67fzXyYRQcwVukD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 18831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1290,
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

_source line 40 · 2026-05-10T19:53:22.570Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011RgzN4irpz9Kxy9y5w77XC`</summary>

```json
{
  "query": "\"FFDC-WAM\" \"Being-H0.7\" composability combined paper 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46c30147-6edc-45e2-a079-1aa4ccc043b3",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUPpdAoqE8XoqMADGbp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c838ebc-6751-4c8d-89c8-f00972bb4d24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wci9L8y67fzXyYRQcwVukD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1290,
      "cache_read_input_tokens": 18831,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1290
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 259,
          "cache_read_input_tokens": 18831,
          "cache_creation_input_tokens": 1290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1290,
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

_source line 41 · 2026-05-10T19:53:26.361Z_

<details><summary>↩ Tool result · `toolu_01Ea2k1WARccTxZfkNbCiSS5`</summary>

```text
# Being-H0.7 LIBERO-Plus Results

## Being-H0.7 Performance
According to Table 1, Being-H0.7 achieved:
- **Zero-shot (LIBERO-plus):** 82.1%
- **Fine-tuned (LIBERO-plus*):** 84.8%

## Comparative Models on LIBERO-Plus

The table includes these models with their LIBERO-plus scores:

| Model | Zero-shot | Fine-tuned |
|-------|-----------|-----------|
| π0 | 53.6 | — |
| π0.5 | 77.4 | — |
| Being-H0.5 | 78.5 | 83.1 |
| MINT-4B | 80.1 | 84.1 |
| ABot-M0 | 80.5 | — |
| JEPA-VLA | 25.6 | — |
| VLA-JEPA | 79.5 | — |
| **Being-H0.7** | **82.1** | **84.8** |

The paper notes that Being-H0.7 achieved "strong performance" on robustness benchmarks, maintaining "resilience against shifted viewpoints, novel textures, and sensor noise."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46c30147-6edc-45e2-a079-1aa4ccc043b3",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "0510d2e2-99e0-4e01-b743-d982a17d4632",
  "sourceToolAssistantUUID": "46c30147-6edc-45e2-a079-1aa4ccc043b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-10T19:53:27.626Z_

<details><summary>↩ Tool result · `toolu_011RgzN4irpz9Kxy9y5w77XC`</summary>

```text
Web search results for query: ""FFDC-WAM" "Being-H0.7" composability combined paper 2025 2026"

Links: [{"title":"Accepted Paper List 2025 – The 33rd IEEE International Symposium on Field-Programmable Custom Computing Machines","url":"https://www.fccm.org/accepted-paper-list-2025/"},{"title":"2026 MCM/ICM Problems","url":"https://www.immchallenge.org/mcm/index.html"},{"title":"Physics Official Question Paper 2025-2026 HSC Science (General) 12th Standard Board Exam Question Paper Solution | Shaalaa.com","url":"https://www.shaalaa.com/question-paper-solution/maharashtra-board-hsc-class-physics-12th-standard-board-exam-2025-2026-official-question-paper_20590"},{"title":"Atomic Composability & Shared State in Modular Blockchains: The 2026 Breakthrough","url":"https://cryptollia.com/articles/synchronicity-breakthrough-atomic-composability-shared-state-2026"},{"title":"HCDS 2025","url":"https://hcds-workshop.github.io/edition/2025/"},{"title":"Call for Papers 2025 – The 33rd IEEE International Symposium on Field-Programmable Custom Computing Machines","url":"https://www.fccm.org/call-for-papers-2025/"},{"title":"2025 Year in Review & the 2026 Year Ahead","url":"https://www.lds.com/insights/2025-year-in-review-the-2026-year-ahead"},{"title":"Combined Science · 0653 · Dynamic Papers","url":"https://papers.dynamicpapers.com/past-papers/cambridge-past-papers/o-level/subjects-a-e/combined-science/"},{"title":"Atomic Composability & The Synchronicity Problem in Modular Blockchains (2026 Outlook)","url":"https://cryptonium.cloud/articles/synchronicity-epoch-atomic-composability-modular-endgame"},{"title":"COMAP: Mathematics Instructional Resources for Innovative Educators","url":"https://www.contest.comap.com/undergraduate/contests/matrix/index.html"}]

The search results do not contain any information about "FFDC-WAM" or "Being-H0.7" papers or research. The results returned are about various other topics including blockchain composability, computer system composability, and academic conferences, but none specifically match the technical identifiers you're searching for.

These appear to be highly specialized technical terms or paper identifiers that may not be widely indexed on the public web. To find information about these specific research papers or systems, you might want to:

1. Check academic databases directly (arXiv, Google Scholar, IEEE Xplore, etc.)
2. Visit the websites of specific research institutions or labs working on these topics
3. Try more specific variants of the search terms if you have additional context about the field or authors

Would you like me to search with different query terms, or do you have additional information that might help locate these specific papers?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c838ebc-6751-4c8d-89c8-f00972bb4d24",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "5717d7e4-c135-40c1-8fb2-cb43353d7256",
  "sourceToolAssistantUUID": "6c838ebc-6751-4c8d-89c8-f00972bb4d24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-10T19:53:31.795Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LRVCB2JYToAH8aRapSBw6H`</summary>

```json
{
  "query": "FFDC \"verification stack\" WAM composability robotics manipulation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5717d7e4-c135-40c1-8fb2-cb43353d7256",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUQnKnbgVsvGUtTapXt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "677db777-537e-412c-8640-0d4f19539772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zgAn5jaPthQxApKkN1Lsx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1408,
      "cache_read_input_tokens": 20121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1408,
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

### Tool call

_source line 44 · 2026-05-10T19:53:32.247Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DPwASAr2hnMyGT7zJ4GRx9`</summary>

```json
{
  "query": "\"When to Trust Imagination\" FFDC results distributional shift perturbation improvement percentage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "677db777-537e-412c-8640-0d4f19539772",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauUQnKnbgVsvGUtTapXt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4f828319-b49d-4fff-9257-908c9ad3c3e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zgAn5jaPthQxApKkN1Lsx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1408,
      "cache_read_input_tokens": 20121,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1408
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 20121,
          "cache_creation_input_tokens": 1408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1408,
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

_source line 45 · 2026-05-10T19:53:35.600Z_

<details><summary>↩ Tool result · `toolu_01LRVCB2JYToAH8aRapSBw6H`</summary>

```text
Web search results for query: "FFDC "verification stack" WAM composability robotics manipulation 2025"

No links found.

The search did not return any results. It appears that the combination of these specific terms (FFDC, "verification stack", WAM, composability, robotics manipulation, and 2025) may not appear together in indexed web results, or they may refer to very specialized or recent research that hasn't yet been widely indexed by search engines.

To help you find what you're looking for, you might try:
- Searching for individual components separately (e.g., "FFDC verification stack" or "WAM robotics composability")
- Checking specialized databases like arXiv (for preprints), IEEE Xplore, or robotics conference proceedings
- Refining the search terms if some of these are acronyms that might have alternative names

Would you like me to search for any of these terms individually or in different combinations?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "677db777-537e-412c-8640-0d4f19539772",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "db788a23-9924-469b-b2bb-679cbdf9b3a1",
  "sourceToolAssistantUUID": "677db777-537e-412c-8640-0d4f19539772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-10T19:53:43.815Z_

<details><summary>↩ Tool result · `toolu_01DPwASAr2hnMyGT7zJ4GRx9`</summary>

```text
Web search results for query: ""When to Trust Imagination" FFDC results distributional shift perturbation improvement percentage"

Links: [{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"Offline Reinforcement Learning with Reverse Model-based Imagination | DeepAI","url":"https://deepai.org/publication/offline-reinforcement-learning-with-reverse-model-based-imagination"},{"title":"[2110.00188v1] Offline Reinforcement Learning with Reverse Model-based Imagination","url":"https://arxiv.org/abs/2110.00188v1"},{"title":"[2110.00188] Offline Reinforcement Learning with Reverse Model-based Imagination","url":"https://arxiv.org/abs/2110.00188"},{"title":"Distribution Shift","url":"https://parasdahal.com/notes/distribution-shift/"},{"title":"Offline Reinforcement Learning with Diffusion-Based Behavior Cloning Term | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-40292-0_22"},{"title":"The Stronger the Imagination, the Less Imaginary the Results | The Shift Network","url":"https://theshiftnetwork.com/Stronger-Imagination-Less-Imaginary-Results"},{"title":"Time Robust Trees: Using Temporal Invariance to Improve Generalization | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-21686-2_27"},{"title":"Distribution shift, generalization and OOD challenge in offline reinforcement learning: a comprehensive survey | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-026-11966-8"},{"title":"Signal Fidelity Index-aware calibration for addressing distributional shift in predictive modeling across heterogeneous real-world data | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-32656-w"}]

I found the "When to Trust Imagination" paper. Let me search for more specific information about the FFDC results, particularly the performance improvement percentages related to distributional shift and perturbation.

Links: [{"title":"When to Trust Imagination: Adaptive Action Execution for World Action Models","url":"https://arxiv.org/html/2605.06222"},{"title":"(PDF) RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://www.researchgate.net/publication/392941279_RoboTwin_20_A_Scalable_Data_Generator_and_Benchmark_with_Strong_Domain_Randomization_for_Robust_Bimanual_Robotic_Manipulation"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://arxiv.org/html/2506.18088v2"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong","url":"https://robogen-iros.github.io/accepted/9_RoboTwin_2_0_A_Scalable_Data.pdf"},{"title":"Paper page - RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://huggingface.co/papers/2506.18088"},{"title":"RoboTwin 2.0: Scalable Synthetic Data Generation and Benchmark Design for Dual-Arm Manipulation Robots | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media","url":"https://ai-scholar.tech/en/articles/llm-paper/robotwin-2.0"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=vAPIIscwc7"},{"title":"RoboTwin 2.0: Large-Scale Robot Simulation & Dataset","url":"https://www.emergentmind.com/topics/robotwin-2-0"},{"title":"[2506.18088] RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://arxiv.org/abs/2506.18088"}]

Based on the search results, I found the specific information about the FFDC results with distributional shift and perturbation improvements:

On hard tasks, FFDC-WAM substantially improves robustness over Base-Motus, raising success rate from 54.20% to 76.40% on Rand.hard and from 57.80% to 76.00% on Clean.hard. This represents improvements of approximately **40.6%** on the random/perturbation setting (Rand.hard) and **31.5%** on the clean setting (Clean.hard).

The improvements are particularly notable because the random setting further introduces background variation, table clutter, height perturbation, and lighting changes, making it a challenging benchmark for testing generalization under distribution shift.

In stable phases, FFDC allows the robot to trust the WAM's long-horizon imagination and execute more actions per inference, substantially reducing computation. In difficult phases, FFDC detects when the imagined future becomes unreliable and triggers replanning, improving robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f828319-b49d-4fff-9257-908c9ad3c3e9",
  "isSidechain": true,
  "promptId": "02b8aeca-f749-4c81-95f9-0a98f1c85a46",
  "agentId": "a176c3d82875e8fc3",
  "type": "user",
  "uuid": "0b70aaca-51b8-48b4-a2fb-71d0e5438671",
  "sourceToolAssistantUUID": "4f828319-b49d-4fff-9257-908c9ad3c3e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-10T19:54:22.098Z_

I now have comprehensive information to provide a thorough answer. Here is my findings report:

---

## Findings Summary

### 1. Being-H0.7 and the 82.1% Success Rate on LIBERO-Plus

**The claim is verified.** According to the Being-H0.7 paper (arXiv 2605.00078), the model achieves exactly **82.1% zero-shot success rate** on LIBERO-Plus under distributional shift, which further improves to **84.8% after fine-tuning** on LIBERO-Plus data.

This places Being-H0.7 at the top of the comparison table in Table 1 of the paper, outperforming:
- pi-0: 53.6%
- pi-0.5: 77.4%
- Being-H0.5: 78.5% (83.1% fine-tuned)
- MINT-4B: 80.1% (84.1% fine-tuned)
- ABot-M0: 80.5%
- JEPA-VLA: 25.6%
- VLA-JEPA: 79.5%

Note: A separate robustness study paper (arXiv 2603.22078) reports **Cosmos-Policy at 82.2%** on LIBERO-Plus -- very close to Being-H0.7's 82.1%. Being-H0.7 was not included in that comparison (likely because it was published later, in May 2026).

---

### 2. LIBERO-Plus Perturbations

LIBERO-Plus uses **seven perturbation dimensions** (five of which Being-H0.7's paper highlights):

1. **Camera** -- viewpoint changes
2. **Robot** -- initial state variations
3. **Language** -- instruction modifications
4. **Light** -- illumination/lighting condition alterations
5. **Background** -- texture/background changes
6. **Noise** -- photometric/sensor distortions
7. **Layout** -- distracting objects / table-top clutter

The Being-H0.7 paper specifically describes these as "table-top clutter, varied lighting conditions, diverse background textures, tabletop height variations, and diverse language instructions" (focusing on 5 axes). The paper notes the model shows "resilience against shifted viewpoints, novel textures, and sensor noise."

---

### 3. Being-H0.7 at Test Time: No Video Generation, Latent Queries Only

**Confirmed: Being-H0.7 does NOT generate video at test time.** The paper explicitly states:

> "At inference, Being-H0.7 discards the posterior branch and performs no visual rollout."

The architecture uses a dual-branch training design:
- **Prior branch** (used at inference): Uses K=16 learnable latent queries inserted between perception and action as a compact reasoning interface. It infers action-relevant state from the current context alone.
- **Posterior branch** (training only): Replaces queries with future embeddings extracted via a frozen ViT and Perceiver resampler, providing privileged future-informed supervision.

At deployment, only the prior branch runs -- using current instruction, observation history, state, and latent queries. The authors describe this as "a way to use future structure without turning deployment into a video-generation problem."

---

### 4. FFDC-WAM and Verification Stacks

**FFDC-WAM** ("When to Trust Imagination: Adaptive Action Execution for World Action Models," arXiv 2605.06222) is a separate work that adds a verification layer on top of World Action Models:

- **FFDC** = Future Forward Dynamics Causal Attention -- a lightweight verifier that jointly reasons over predicted future actions, predicted visual dynamics, real observations, and language instructions
- It determines whether remaining action rollouts can still be trusted, triggering replanning when reality deviates from the WAM's imagined future

**Results under distributional shift (RoboTwin benchmark, not LIBERO-Plus):**
- Hard tasks with perturbations (Rand.hard): success rate improved from 54.20% to 76.40% (~41% relative improvement)
- Hard tasks clean (Clean.hard): improved from 57.80% to 76.00% (~31% relative improvement)
- 69.10% reduction in WAM forward passes while achieving 2.54% overall success rate improvement

**Key limitations of this search:**
- FFDC-WAM builds exclusively on **Motus** (a unified latent action world model), NOT on Being-H0.7
- It was evaluated on **RoboTwin benchmark only**, not LIBERO-Plus
- **No paper was found combining FFDC-WAM with Being-H0.7** or any other method in a "composability verification stack"
- The term "FFDC-WAM composability verification stack" does not appear in any indexed research -- this specific combination may not exist in the literature as of May 2026

Being-H0.7 is only cited once in the FFDC-WAM related work section as background but is not integrated into the approach.

---

### Summary of Verification

| Claim | Status |
|-------|--------|
| Being-H0.7 achieves 82.1% on LIBERO-Plus under distributional shift | **Verified** (zero-shot) |
| LIBERO-Plus perturbations | **Verified** -- 7 axes (camera, robot, language, light, background, noise, layout) |
| Being-H0.7 generates video at test time | **False** -- uses latent queries only, no visual rollout at inference |
| FFDC-WAM combined with other methods / composability verification stack | **Not found** -- FFDC-WAM is standalone on Motus; no combined stack found |
| Verification stacks improving robustness under distributional shift | **Partially supported** -- FFDC-WAM shows robustness gains on RoboTwin (not LIBERO-Plus) |

---

Sources:
- [Being-H0.7: A Latent World-Action Model from Egocentric Videos (arXiv 2605.00078)](https://arxiv.org/html/2605.00078v1)
- [Being-H0.7 Official Research Page](https://research.beingbeyond.com/being-h07)
- [When to Trust Imagination: Adaptive Action Execution for World Action Models (arXiv 2605.06222)](https://arxiv.org/html/2605.06222)
- [Do World Action Models Generalize Better than VLAs? A Robustness Study (arXiv 2603.22078)](https://arxiv.org/html/2603.22078v1)
- [LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (arXiv 2510.13626)](https://arxiv.org/html/2510.13626v1)
- [Being-H GitHub Repository](https://github.com/BeingBeyond/Being-H)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b70aaca-51b8-48b4-a2fb-71d0e5438671",
  "isSidechain": true,
  "agentId": "a176c3d82875e8fc3",
  "requestId": "req_011CauURyYVh3Zn6rKXxJ5iE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44750434-4ea8-4c14-81b7-704cb6a62801",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "06cfb9be-b16e-4311-8f2f-d77e6ef015fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SnKxi1zFRZaeB6dSbV2Yv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1856,
      "cache_read_input_tokens": 21529,
      "output_tokens": 1680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1856
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1680,
          "cache_read_input_tokens": 21529,
          "cache_creation_input_tokens": 1856,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1856,
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
