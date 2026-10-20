# Research conversation: Search the web for theoretical work on how LoRA fine-tuning affects learned representations and feature stability. Speci

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 62
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad487675142d937dd.jsonl`
- **Structured JSON:** [`68054dd4f56ed2561c28.json`](../../sessions/68/68054dd4f56ed2561c28.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

62 recorded events

### User

_source line 1 · 2026-05-13T19:43:48.838Z_

Search the web for theoretical work on how LoRA fine-tuning affects learned representations and feature stability. Specifically:

1. "LoRA representation drift" or "LoRA feature stability"
2. "LoRA Lipschitz bound" or "LoRA perturbation bound representation"
3. "LoRA Subtraction drift-resistant" arXiv 2503.18985 - verify this paper exists
4. "density ratio estimation high dimensional latent space"
5. "CKA similarity LoRA fine-tuning"

I need to assess whether the proposed "LoRA stability theorem" (bounding |Δβ| under low-rank perturbations) is novel and feasible. Is there existing work that already bounds representation changes under LoRA? Would such a theorem be a genuine contribution?

Report findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "ff5b8cdf-5104-4d75-9a3b-ed686d071b76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T19:43:48.840Z_

```json
{
  "parentUuid": "ff5b8cdf-5104-4d75-9a3b-ed686d071b76",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
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
  "uuid": "682e54c7-08dc-46dc-8f16-9c9bee6a8bae",
  "timestamp": "2026-05-13T19:43:48.840Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T19:43:52.660Z_



I'll search for each of these topics systematically. Let me start by loading the WebSearch tool and then conducting the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "682e54c7-08dc-46dc-8f16-9c9bee6a8bae",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb196s8a194we9FPSrLgp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3432e481-8429-4062-85d3-4a30850eb5bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TkDnrWDUSNfExxepzaoa3T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 732,
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

_source line 4 · 2026-05-13T19:43:53.199Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ChrVES6UaTEWdWGVjF8Ax4`</summary>

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
  "parentUuid": "3432e481-8429-4062-85d3-4a30850eb5bc",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb196s8a194we9FPSrLgp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60c4ba82-616f-4ea6-b4d5-65e5e6a38e17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TkDnrWDUSNfExxepzaoa3T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 8223,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 732
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 107,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 732,
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

_source line 5 · 2026-05-13T19:43:53.201Z_

<details><summary>↩ Tool result · `toolu_01ChrVES6UaTEWdWGVjF8Ax4`</summary>

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
  "parentUuid": "60c4ba82-616f-4ea6-b4d5-65e5e6a38e17",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "81cbaba3-f12e-417d-861f-ef22813ce3ec",
  "sourceToolAssistantUUID": "60c4ba82-616f-4ea6-b4d5-65e5e6a38e17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T19:43:55.708Z_



Now let me run all five searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81cbaba3-f12e-417d-861f-ef22813ce3ec",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb197CCXxA28YdTBTDSv7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2393cf23-f90b-4423-bec1-3d657842df8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cx7GPHgeksP2UwboomUMmG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 8955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 7 · 2026-05-13T19:43:56.267Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EEcaSd3dBe1kPwuUFCc2Db`</summary>

```json
{
  "query": "LoRA representation drift feature stability fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2393cf23-f90b-4423-bec1-3d657842df8d",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb197CCXxA28YdTBTDSv7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a199285e-e32c-42ef-80ec-986bb75cc1c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cx7GPHgeksP2UwboomUMmG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 8955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 8 · 2026-05-13T19:43:57.200Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P1rVGiUBPYKPibRJ92BuEf`</summary>

```json
{
  "query": "LoRA Lipschitz bound perturbation bound representation low-rank adaptation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a199285e-e32c-42ef-80ec-986bb75cc1c6",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb197CCXxA28YdTBTDSv7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49fc0a85-152d-44fe-bcfa-702db1f9fb40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cx7GPHgeksP2UwboomUMmG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 8955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 9 · 2026-05-13T19:43:57.664Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HgwMHm3CMpr1XQM3KEPvGu`</summary>

```json
{
  "query": "arXiv 2503.18985 LoRA subtraction drift-resistant"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49fc0a85-152d-44fe-bcfa-702db1f9fb40",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb197CCXxA28YdTBTDSv7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b370fc34-d506-4364-9e40-7402a86f981f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cx7GPHgeksP2UwboomUMmG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 8955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 10 · 2026-05-13T19:43:58.608Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GFUVvmSZG5ocB5mWafeq4Z`</summary>

```json
{
  "query": "density ratio estimation high dimensional latent space neural network"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b370fc34-d506-4364-9e40-7402a86f981f",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb197CCXxA28YdTBTDSv7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77a4bb5f-7e4d-4277-aaa1-5cf4f2ca9590",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cx7GPHgeksP2UwboomUMmG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 8955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1916,
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

_source line 11 · 2026-05-13T19:43:58.847Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QHhmEjMNc5yXvR8WRZ7Q8D`</summary>

```json
{
  "query": "CKA similarity LoRA fine-tuning representation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77a4bb5f-7e4d-4277-aaa1-5cf4f2ca9590",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb197CCXxA28YdTBTDSv7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df11f57c-79ea-4c79-a5e5-e93ca97013dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cx7GPHgeksP2UwboomUMmG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1916,
      "cache_read_input_tokens": 8955,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1916
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 267,
          "cache_read_input_tokens": 8955,
          "cache_creation_input_tokens": 1916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1916,
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

_source line 12 · 2026-05-13T19:44:03.095Z_

<details><summary>↩ Tool result · `toolu_01HgwMHm3CMpr1XQM3KEPvGu`</summary>

```text
Web search results for query: "arXiv 2503.18985 LoRA subtraction drift-resistant"

Links: [{"title":"[2503.18985] LoRA Subtraction for Drift-Resistant Space in Exemplar-Free Continual Learning","url":"https://arxiv.org/abs/2503.18985"},{"title":"[2503.18985] LoRA Subtraction for Drift-Resistant Space in Exemplar-Free Continual Learning","url":"https://ar5iv.labs.arxiv.org/html/2503.18985"},{"title":"LoRA Subtraction for Drift-Resistant Space in Exemplar-Free Continual Learning","url":"https://arxiv.org/html/2503.18985"},{"title":"LoRA Subtraction for Drift-Resistant Space in Exemplar-Free Continual Learning | alphaXiv","url":"https://www.alphaxiv.org/abs/2503.18985"},{"title":"Computer Science Mar 2025","url":"https://arxiv.org/list/cs/2025-03?skip=9375&show=500"},{"title":"Machine Learning Mar 2025","url":"https://arxiv.org/list/cs.LG/2025-03?skip=1575&show=50"},{"title":"LoRA Subtraction for Drift-Resistant Space in Exemplar ...","url":"https://bytez.com/docs/arxiv/2503.18985/paper"},{"title":"LoRA Subtraction for Drift-Resistant Space in Exemplar-Free Continual Learning","url":"https://www.researchgate.net/publication/390177163_LoRA_Subtraction_for_Drift-Resistant_Space_in_Exemplar-Free_Continual_Learning"},{"title":"LoRA Subtraction for Drift-Resistant Space in Exemplar ...","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2503.18985"},{"title":"LoRA Subtraction for Drift-Resistant Space in Exemplar-Free Continual Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/lora-subtraction-drift-resistant-space-exemplar-free"}]

I found the paper! Here's what I found about arXiv 2503.18985:

**Title:** LoRA Subtraction for Drift-Resistant Space in Exemplar-Free Continual Learning

**Authors:** Xuan Liu and Xiaobin Chang

**Status:** Accepted to CVPR 2025

**Key Contribution:**
The paper addresses catastrophic forgetting in continual learning, which is particularly prominent in exemplar-free continual learning where samples from previous tasks cannot be retained. The authors introduce the Drift-Resistant Space (DRS), which effectively handles feature drifts without requiring explicit feature modeling or storage of previous tasks, using a novel parameter-efficient fine-tuning approach called Low-Rank Adaptation Subtraction (LoRA-).

**Technical Approach:**
The method subtracts the layer-wise LoRA weights associated with previous tasks from the initial pre-trained weights, with the modified model then processing data from new tasks to obtain the projection matrix for the DRS.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b370fc34-d506-4364-9e40-7402a86f981f",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "3495a37a-b6e4-4faf-b5ea-87e5d31ac577",
  "sourceToolAssistantUUID": "b370fc34-d506-4364-9e40-7402a86f981f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T19:44:04.616Z_

<details><summary>↩ Tool result · `toolu_01EEcaSd3dBe1kPwuUFCc2Db`</summary>

```text
Web search results for query: "LoRA representation drift feature stability fine-tuning"

Links: [{"title":"LoRA Subtraction for Drift-Resistant Space in Exemplar-Free Continual Learning","url":"https://arxiv.org/html/2503.18985"},{"title":"LoRA-TCN: A pre-trained/fine-tuning learning paradigm for drift adaptation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925400525014200"},{"title":"Using LoRA for Efficient Stable Diffusion Fine-Tuning","url":"https://huggingface.co/blog/lora"},{"title":"[2503.18985] LoRA Subtraction for Drift-Resistant Space in Exemplar-Free Continual Learning","url":"https://arxiv.org/abs/2503.18985"},{"title":"GitHub - cloneofsimo/lora: Using Low-rank adaptation to quickly fine-tune diffusion models. · GitHub","url":"https://github.com/cloneofsimo/lora"},{"title":"[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685"},{"title":"LoRA · Hugging Face","url":"https://huggingface.co/docs/peft/main/en/conceptual_guides/lora"},{"title":"LoRA fine-tuning Hyperparameters Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/lora-hyperparameters-guide"},{"title":"AdaptiveFedLoRA: Drift-Aware Adaptive LoRA Rank 1","url":"https://www.medrxiv.org/content/10.64898/2026.01.18.26344237v1.full.pdf"},{"title":"Efficient Fine-Tuning with LoRA: A Guide to Optimal Parameter Selection for Large Language Models","url":"https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms"}]

I found several relevant research papers and resources on LoRA representation drift, feature stability, and fine-tuning. Here are the key findings:

## LoRA Subtraction for Drift-Resistant Space

In continual learning, catastrophic forgetting often arises due to feature drift, which is particularly prominent in exemplar-free continual learning where samples from previous tasks cannot be retained. A novel approach called Drift-Resistant Space (DRS) effectively handles feature drifts without requiring explicit feature modeling or the storage of previous tasks, using a parameter-efficient fine-tuning approach called Low-Rank Adaptation Subtraction (LoRA-).

This method subtracts the LoRA weights of old tasks from the initial pre-trained weight before processing new task data to establish the DRS for model training. LoRA- enhances stability, improves efficiency, and simplifies implementation.

## Feature Stability in LoRA Fine-Tuning

The LoRA architecture scales each adapter during every forward pass by a fixed scalar, which is set at initialization and depends on the rank r. The research Rank-Stabilized LoRA proves that using lora_alpha/math.sqrt(r) stabilizes the adapters and unlocks increased performance potential from higher ranks.

## Adaptive LoRA with Drift Awareness

Recent research on AdaptiveFedLoRA achieves substantially reduced drift (0.000010 average) compared to baselines (0.0004–0.0012), representing a 40–120× reduction. Adaptive rank scheduling acts as a safety mechanism during transient drift episodes, with stability constraints preventing instability where sudden large rank jumps caused loss spikes.

These approaches address the important problem of maintaining feature representation stability when fine-tuning large models using parameter-efficient methods like LoRA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a199285e-e32c-42ef-80ec-986bb75cc1c6",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "30d77ec3-5042-4af2-a9d9-df5ea28a440d",
  "sourceToolAssistantUUID": "a199285e-e32c-42ef-80ec-986bb75cc1c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T19:44:05.092Z_

<details><summary>↩ Tool result · `toolu_01QHhmEjMNc5yXvR8WRZ7Q8D`</summary>

```text
Web search results for query: "CKA similarity LoRA fine-tuning representation"

Links: [{"title":"Layer-wise LoRA fine-tuning: a similarity metric approach","url":"https://arxiv.org/pdf/2602.05988"},{"title":"GitHub - c2d-usp/Layer-wise-LoRA-with-CKA · GitHub","url":"https://github.com/c2d-usp/Layer-wise-LoRA-with-CKA"},{"title":"LoRASuite: Efficient LoRA Adaptation Across Large ...","url":"https://arxiv.org/pdf/2505.13515"},{"title":"Dynamic Cross-Modal Prompt Generation for Multimodal Continual Instruction Tuning","url":"https://arxiv.org/html/2605.10765"},{"title":"LoRA vs Full Fine-tuning: An Illusion of Equivalence","url":"https://arxiv.org/html/2410.21228v1"},{"title":"LoRA vs. Full Fine-Tuning: An Illusion of Equivalence | Hacker News","url":"https://news.ycombinator.com/item?id=42085665"},{"title":"[2410.20777] KD-LoRA: A Hybrid Approach to Efficient Fine-Tuning with LoRA and Knowledge Distillation","url":"https://arxiv.org/abs/2410.20777"},{"title":"LoRA vs Full Fine-tuning: An Illusion of Equivalence | OpenReview","url":"https://openreview.net/forum?id=PGNdDfsI6C"},{"title":"Efficient Fine-Tuning with LoRA: A Guide to Optimal Parameter Selection for Large Language Models","url":"https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms"},{"title":"[2410.21228] LoRA vs Full Fine-tuning: An Illusion of Equivalence","url":"https://arxiv.org/abs/2410.21228"}]

Based on the search results, here's what I found about CKA similarity and LoRA fine-tuning representation:

## CKA Similarity for LoRA Layer Selection

Centered Kernel Alignment (CKA) is a representation similarity metric used to identify the most important layers to fine-tune in LoRA. The method measures the similarity between the input and output representations of each transformer layer.

### How It Works

High similarity indicates a low impact to changes on internal representations, and therefore low task-specific importance. The selection process involves choosing the top N layers with the lowest similarity, as lower similarity is associated with a higher impact on internal representations.

### Application and Results

This approach successfully fine-tunes only a small subset of layers while matching or even surpassing the predictive performance of fine-tuning all layers. The method selects a subset of transformer layers for fine-tuning based on the similarity metric.

The approach has been evaluated across multiple model architectures including encoder-only models (RoBERTa, DeBERTa), decoder-only models (LLaMA, Mistral, Gemma), and multimodal models (LLaVA).

### Related Applications

CKA is also used in other contexts, such as employing centered kernel alignment to quantify the similarity between corresponding layers of two LLMs for layer mapping with dynamic programming-based algorithms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df11f57c-79ea-4c79-a5e5-e93ca97013dd",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "acc71928-b605-42db-af6c-da08bb52ba6a",
  "sourceToolAssistantUUID": "df11f57c-79ea-4c79-a5e5-e93ca97013dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-13T19:44:05.301Z_

<details><summary>↩ Tool result · `toolu_01GFUVvmSZG5ocB5mWafeq4Z`</summary>

```text
Web search results for query: "density ratio estimation high dimensional latent space neural network"

Links: [{"title":"Density estimation using deep generative neural networks | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2101344118"},{"title":"Density estimation using deep generative neural networks - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC8054014/"},{"title":"Density Ratio Estimation in Machine Learning | Request PDF","url":"https://www.researchgate.net/publication/215705204_Density_Ratio_Estimation_in_Machine_Learning"},{"title":"Telescoping Density-Ratio Estimation Benjamin Rhodes School of Informatics","url":"https://proceedings.neurips.cc/paper/2020/file/33d3b157ddc0896addfb22fa2a519097-Paper.pdf"},{"title":"Density estimation using deep generative neural networks","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC8054014/figure/fig01/"},{"title":"Density Ratio Estimation via Inﬁnitesimal Classiﬁcation Kristy Choi˚","url":"https://proceedings.mlr.press/v151/choi22a/choi22a.pdf"},{"title":"Density estimation using deep generative neural networks | TransferLab — appliedAI Institute","url":"https://transferlab.ai/pills/2023/density-estimation-using-gans/"},{"title":"Adaptive Multi-stage Density Ratio Estimation for Learning Latent Space Energy-based Model","url":"https://proceedings.neurips.cc/paper_files/paper/2022/hash/874a4d89f2d04b4bcf9a2c19545cf040-Abstract-Conference.html"},{"title":"Featurized Density Ratio Estimation Kristy Choi1 Madeline Liao1 Stefano Ermon1","url":"https://proceedings.mlr.press/v161/choi21a/choi21a.pdf"},{"title":"Adaptive Multi-stage Density Ratio Estimation for Learning Latent Space Energy-based Model | OpenReview","url":"https://openreview.net/forum?id=kS5KG3mpSY"}]

Here are the search results for "density ratio estimation high dimensional latent space neural network":

## Key Research Findings

**High-Dimensional Density Estimation Challenges:**
It is notoriously difficult to estimate the density of high-dimensional data due to the "curse of dimensionality." Additionally, direct estimation of density ratios in high-dimensional task spaces is challenging and often unstable.

**Deep Generative Network Approaches:**

By modeling data normally distributed around a manifold of reduced dimension, researchers show how the power of bidirectional generative neural networks (e.g., cycleGAN) can be exploited for explicit evaluation of the data density. The Roundtrip framework specifically addresses limitations in latent space dimensionality: It can efficiently model data densities that are concentrated near learned manifolds, which is difficult to achieve by previous approaches as they require the latent space to have the same dimension as the data space.

**Advanced Density Ratio Methods:**

Telescoping density-ratio estimation (TRE) can accurately estimate density-ratios using deep neural networks on high-dimensional problems, significantly outperforming existing single-ratio methods.

**Neural Network-Based Estimation:**

Recent approaches also use noise contrastive estimation (NCE) to discriminatively learn through density ratio estimation between the latent prior density and latent posterior density.

The search results reveal a rich literature on combining neural networks with density ratio estimation in latent spaces, particularly for handling the challenges posed by high-dimensional data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77a4bb5f-7e4d-4277-aaa1-5cf4f2ca9590",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "6715ceb3-4d43-4d0f-8fe3-06a3a1a23d0d",
  "sourceToolAssistantUUID": "77a4bb5f-7e4d-4277-aaa1-5cf4f2ca9590",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T19:44:05.915Z_

<details><summary>↩ Tool result · `toolu_01P1rVGiUBPYKPibRJ92BuEf`</summary>

```text
Web search results for query: "LoRA Lipschitz bound perturbation bound representation low-rank adaptation"

Links: [{"title":"On the Convergence Rate of LoRA Gradient Descent Siqiao Mu Diego Klabjan","url":"https://arxiv.org/pdf/2512.18248"},{"title":"[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685"},{"title":"Bridging The Gap between Low-rank and Orthogonal ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/cdd0640218a27e9e2c0e52e324e25db0-Paper-Conference.pdf"},{"title":"Flexible Low-Rank Adaptation for Large Language Models","url":"https://aclanthology.org/2025.acl-long.713.pdf"},{"title":"ARD-LoRA: Dynamic Rank Allocation for Parameter- ...","url":"https://arxiv.org/pdf/2506.18267"},{"title":"THE EXPRESSIVE POWER OF LOW-RANK ADAPTATION","url":"https://openreview.net/pdf?id=likXVjmh3E"},{"title":"Robust and Efficient Fine-tuning of LLMs with Bayesian ...","url":"https://www.arxiv.org/pdf/2411.04358"},{"title":"LORA: LOW-RANK ADAPTATION OF LARGE LAN","url":"https://openreview.net/pdf?id=nZeVKeeFYf9"},{"title":"Low-Rank Adaptation for Foundation Models: A Comprehensive Review","url":"https://arxiv.org/html/2501.00365v1"},{"title":"L2R: Low-Rank and Lipschitz-Controlled Routing for Mixture-of-Experts","url":"https://arxiv.org/html/2601.21349"}]

Based on the search results, here are the key findings related to your query about LoRA, Lipschitz bounds, perturbation bounds, and representation in low-rank adaptation:

## Lipschitz Smoothness Challenges in LoRA

Even if the original loss function is Lipschitz smooth, the new loss function reparametrized in terms of the LoRA matrices A and B is not. This nonsmoothness is a major obstacle to applying classic convergence proof techniques of gradient methods to LoRA.

## Theoretical Analysis and Perturbation Bounds

Recent theoretical work addresses this challenge. A modified descent lemma for the "Lipschitz-like" reparametrized function is used to handle the convergence analysis. Additionally, the first non-asymptotic convergence analysis of the original LoRA gradient descent algorithm has been provided without restrictive assumptions.

## Representation and Robustness

In the context of orthogonal constraints related to Lipschitz properties, by constraining the orthogonality of weight matrices, models can be ensured to be 1-Lipschitz in theory and thus achieve provable robustness against adversarial perturbations.

## Related Framework

Low-rank & Lipschitz-controlled Routing (L2R) features a low-rank routing space for representation decoupling and a Lipschitz-controlled scoring function for stable expert selection, showing how these concepts are being integrated in modern architectures.

The search results indicate active research into bridging the gap between low-rank representations and Lipschitz constraints to improve stability and robustness in adaptation methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49fc0a85-152d-44fe-bcfa-702db1f9fb40",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "ad3c0654-5329-436e-9ab4-55fe6ec6c5e8",
  "sourceToolAssistantUUID": "49fc0a85-152d-44fe-bcfa-702db1f9fb40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-13T19:44:10.190Z_

Good, I have initial results. Let me now do deeper dives on the most critical papers -- particularly the "LoRA vs Full Fine-tuning: Illusion of Equivalence" paper (which directly addresses representation changes under LoRA), the convergence/Lipschitz paper, and the expressive power of LoRA paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad3c0654-5329-436e-9ab4-55fe6ec6c5e8",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb1988DhKnL8GSLYVoJyv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf00c1cb-ae11-460b-adc2-32615c3c4586",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMChgHei64nv8V8m7niR2X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2610,
      "cache_creation_input_tokens": 2123,
      "cache_read_input_tokens": 10871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2123,
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

_source line 18 · 2026-05-13T19:44:12.160Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016GhkC1ivZKFsTiUXswrQN7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.21228",
  "prompt": "Extract the full abstract and key claims about how LoRA vs full fine-tuning affects internal representations. What do they find about representation similarity or divergence? Do they provide any formal bounds on representation change?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf00c1cb-ae11-460b-adc2-32615c3c4586",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb1988DhKnL8GSLYVoJyv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "03a7218a-3cdf-42e0-a438-eaf5f521f16c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMChgHei64nv8V8m7niR2X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2610,
      "cache_creation_input_tokens": 2123,
      "cache_read_input_tokens": 10871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2123,
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

### Tool result

_source line 19 · 2026-05-13T19:44:16.460Z_

<details><summary>↩ Tool result · `toolu_016GhkC1ivZKFsTiUXswrQN7`</summary>

```text
# LoRA vs Full Fine-tuning: Key Findings

## Full Abstract

The researchers examine whether LoRA and full fine-tuning produce equivalent solutions. Their key finding: "weight matrices trained with LoRA have new, high-ranking singular vectors, which we call intruder dimensions, while those trained with full fine-tuning do not."

## Main Claims About Representation Changes

**Spectral Structure Divergence:** The two methods yield weight matrices with fundamentally different singular value decomposition patterns. LoRA introduces novel high-rank singular vectors absent in full fine-tuning approaches.

**Catastrophic Forgetting Localization:** The researchers discovered that LoRA exhibits less forgetting overall, but when it does forget, the forgetting concentrates specifically in these intruder dimensions. Through causal intervention on singular values post-fine-tuning, they demonstrated these dimensions "cause forgetting."

**Continual Learning Performance:** The paper finds that LoRA models accumulating intruder dimensions across sequential fine-tuning tasks "tend to perform worse" in continual learning scenarios.

## Formal Bounds

The document provided does not include formal mathematical bounds on representation change. The analysis relies on empirical spectral analysis and causal interventions rather than theoretical bounds on representation divergence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03a7218a-3cdf-42e0-a438-eaf5f521f16c",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "626b28c4-d615-4807-b012-15ce3437c0d4",
  "sourceToolAssistantUUID": "03a7218a-3cdf-42e0-a438-eaf5f521f16c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-13T19:44:16.686Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RTP1f51ZkhAbAXTUd834XW`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.18985",
  "prompt": "Extract the full abstract and key theoretical claims. Do they provide formal bounds on feature drift or representation stability under LoRA? What is their \"LoRA Subtraction\" method exactly?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "626b28c4-d615-4807-b012-15ce3437c0d4",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb1988DhKnL8GSLYVoJyv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19f78b98-cf48-4867-a6db-2f4ce141b343",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMChgHei64nv8V8m7niR2X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2610,
      "cache_creation_input_tokens": 2123,
      "cache_read_input_tokens": 10871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2123,
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

_source line 21 · 2026-05-13T19:44:16.865Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016cBQb6SAXTQFPQKVdkmjJV`</summary>

```json
{
  "url": "https://openreview.net/pdf?id=likXVjmh3E",
  "prompt": "Extract the key theoretical results about the expressive power of low-rank adaptation. Do they provide bounds on how much LoRA can change representations? Any Lipschitz-type bounds or perturbation analysis?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19f78b98-cf48-4867-a6db-2f4ce141b343",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb1988DhKnL8GSLYVoJyv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b3f953a-2831-4b1f-a861-473cb13972dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMChgHei64nv8V8m7niR2X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2610,
      "cache_creation_input_tokens": 2123,
      "cache_read_input_tokens": 10871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2123,
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

_source line 22 · 2026-05-13T19:44:17.143Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01L76QkMURUPG4tnskT1jURE`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2512.18248",
  "prompt": "Extract the key theoretical results about LoRA convergence. Do they analyze Lipschitz smoothness of LoRA? What bounds do they provide? Do they discuss representation stability or perturbation bounds?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b3f953a-2831-4b1f-a861-473cb13972dd",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb1988DhKnL8GSLYVoJyv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c775f3b-c67c-444a-a722-ec7774fd9d52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NMChgHei64nv8V8m7niR2X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2610,
      "cache_creation_input_tokens": 2123,
      "cache_read_input_tokens": 10871,
      "output_tokens": 527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2123
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2610,
          "output_tokens": 527,
          "cache_read_input_tokens": 10871,
          "cache_creation_input_tokens": 2123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2123,
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

_source line 23 · 2026-05-13T19:44:21.171Z_

<details><summary>↩ Tool result · `toolu_01RTP1f51ZkhAbAXTUd834XW`</summary>

```text
# Abstract and Key Claims Analysis

## Full Abstract
The paper addresses catastrophic forgetting in exemplar-free continual learning by introducing a Drift-Resistant Space (DRS) through "Low-Rank Adaptation Subtraction" (LoRA-). The method subtracts LoRA weights from previous tasks before processing new data, enhancing stability without storing old task samples. The authors claim "state-of-the-art results, especially for long task sequences."

## LoRA Subtraction Method
The core mechanism involves: "subtract the LoRA weights of old tasks from the initial pre-trained weight" before training on new tasks. This establishes the DRS for subsequent model training, claimed to enhance stability while remaining parameter-efficient.

## Formal Bounds and Theoretical Analysis
**The abstract does not mention formal bounds.** There are no explicit references to theoretical guarantees on feature drift or representation stability. The paper claims the method "effectively handles feature drifts" and "stabilizing feature drifts allows for better plasticity," but these appear to be empirical claims rather than formally proven bounds.

## Key Limitation
The abstract relies on empirical validation across datasets rather than providing mathematical proofs or theoretical bounds on drift resistance. The stability claims are functional descriptions of the approach's behavior rather than formally quantified guarantees.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19f78b98-cf48-4867-a6db-2f4ce141b343",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "00b7b422-3bf3-46ec-96c6-8d90aa01d11a",
  "sourceToolAssistantUUID": "19f78b98-cf48-4867-a6db-2f4ce141b343",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T19:44:22.510Z_

<details><summary>↩ Tool result · `toolu_016cBQb6SAXTQFPQKVdkmjJV`</summary>

```text
I appreciate your question, but I need to be direct: the content you've provided appears to be a PDF file in binary/compressed format rather than readable text. The garbled characters and stream objects suggest this is the underlying PDF structure rather than extractable text.

From what I can observe in the structure, there are multiple compressed streams (objects 197, 292, 342, etc.) and figure references, but I cannot reliably extract and analyze the actual theoretical content about LoRA's expressive power without proper PDF rendering.

**To help you effectively, I would need:**

1. The plain text version of the paper, or
2. The paper title/authors so I can reference publicly available versions, or
3. Specific page numbers where theoretical results appear

**What I can tell you:** If this is research on LoRA's theoretical properties, typical bounds in this area often address:
- How rank constraints limit the subspace of weight modifications
- Perturbation analysis showing LoRA as a low-rank approximation to full fine-tuning
- Lipschitz continuity properties between base and adapted models

Once you provide readable source material, I can extract and summarize the specific theoretical results you're asking about while respecting all your stated constraints.

[Binary content (application/pdf, 1.7MB) also saved to /home/ubuntu/.claude-account-2/projects/-/d420c8fc-73ad-49e5-a076-6b52b56c836b/tool-results/webfetch-1778701457680-67ok91.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b3f953a-2831-4b1f-a861-473cb13972dd",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "4edad8af-1657-47b5-b93e-32b461ee5122",
  "sourceToolAssistantUUID": "3b3f953a-2831-4b1f-a861-473cb13972dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-13T19:44:22.827Z_

<details><summary>↩ Tool result · `toolu_01L76QkMURUPG4tnskT1jURE`</summary>

```text
# Key Theoretical Results on LoRA Convergence

Based on the PDF metadata and document structure, this paper by Mu and Klabjan analyzes convergence rates for Low-Rank Adaptation (LoRA) gradient descent. While I cannot access the full mathematical content due to the compressed PDF stream format, the document organization reveals several key areas of investigation:

## Theoretical Framework

The paper establishes convergence analysis for LoRA optimization, examining how the low-rank parameterization affects training dynamics. The document contains multiple theorems (Theorem 3.1 through 3.6) and appendix sections dedicated to theoretical proofs, suggesting rigorous convergence rate analysis.

## Likely Analytical Components

Based on the theorem structure and section headings visible in the metadata:

- **Convergence characterization** for gradient descent under the LoRA constraint
- **Subsection analysis** of different convergence regimes (subsections 3.1-3.3 and appendix sections A.1-A.5)
- **Empirical validation** through experiments on standard datasets (CIFAR, ImageNet)

## Scope Limitations

The PDF structure indicates this work builds on prior LoRA analyses while providing novel convergence bounds, but specific details about Lipschitz smoothness analysis, perturbation bounds, or representation stability results require access to the decompressed content streams.

The paper cites contemporary work on LoRA theory (Hayou 2024, Zeng 2024, Kim 2025) suggesting positioning within an active research area on formal LoRA properties.

[Binary content (application/pdf, 1.1MB) also saved to /home/ubuntu/.claude-account-2/projects/-/d420c8fc-73ad-49e5-a076-6b52b56c836b/tool-results/webfetch-1778701457166-917rwq.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c775f3b-c67c-444a-a722-ec7774fd9d52",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "741fc9f4-1aa8-4471-9bcf-10a215dafc6d",
  "sourceToolAssistantUUID": "3c775f3b-c67c-444a-a722-ec7774fd9d52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-13T19:44:29.195Z_

Let me search for more specific theoretical work on bounding representation changes under LoRA, and also look at the expressive power paper through the HTML version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "741fc9f4-1aa8-4471-9bcf-10a215dafc6d",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb199NQWUWh9bLPVgPDsh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1197a6da-e1c7-41db-bdd1-eba9e0fb56ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARHk3VQt7Fa5Zrek6bpTTJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4586,
      "cache_read_input_tokens": 12994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4586,
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

_source line 27 · 2026-05-13T19:44:29.843Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H7DNx571rb5XV3mcJ2vEUp`</summary>

```json
{
  "query": "\"expressive power of low-rank adaptation\" LoRA theoretical bounds representation change ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1197a6da-e1c7-41db-bdd1-eba9e0fb56ba",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb199NQWUWh9bLPVgPDsh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0dd740e2-e93c-4bec-a346-96bae29b3f5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARHk3VQt7Fa5Zrek6bpTTJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4586,
      "cache_read_input_tokens": 12994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4586,
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

_source line 28 · 2026-05-13T19:44:30.827Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017zz72fq4UkRHC3im7smnwa`</summary>

```json
{
  "query": "LoRA fine-tuning representation change bound theorem \"low rank\" perturbation theory neural network"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dd740e2-e93c-4bec-a346-96bae29b3f5b",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb199NQWUWh9bLPVgPDsh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0fdaca3a-e26f-46b3-9fa0-dea12075d7a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARHk3VQt7Fa5Zrek6bpTTJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4586,
      "cache_read_input_tokens": 12994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4586,
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

_source line 29 · 2026-05-13T19:44:31.386Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XdQVPUSJN1LoUGMUsWL3cK`</summary>

```json
{
  "query": "\"LoRA stability\" theorem bound representation shift formal proof 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fdaca3a-e26f-46b3-9fa0-dea12075d7a1",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb199NQWUWh9bLPVgPDsh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc473b59-d7bd-416d-a239-51ec75b9a03e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARHk3VQt7Fa5Zrek6bpTTJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4586,
      "cache_read_input_tokens": 12994,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4586
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 12994,
          "cache_creation_input_tokens": 4586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4586,
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

_source line 30 · 2026-05-13T19:44:35.910Z_

<details><summary>↩ Tool result · `toolu_01H7DNx571rb5XV3mcJ2vEUp`</summary>

```text
Web search results for query: ""expressive power of low-rank adaptation" LoRA theoretical bounds representation change ICLR"

Links: [{"title":"THE EXPRESSIVE POWER OF LOW-RANK ADAPTATION","url":"https://openreview.net/pdf?id=likXVjmh3E"},{"title":"The Expressive Power of Low-Rank Adaptation | OpenReview","url":"https://openreview.net/forum?id=likXVjmh3E"},{"title":"The Expressive Power of Low-Rank Adaptation","url":"https://arxiv.org/html/2310.17513v3"},{"title":"ICLR Poster The Expressive Power of Low-Rank Adaptation","url":"https://iclr.cc/virtual/2024/poster/17923"},{"title":"[2310.17513] The Expressive Power of Low-Rank Adaptation","url":"https://ar5iv.labs.arxiv.org/html/2310.17513"},{"title":"LORA: LOW-RANK ADAPTATION OF LARGE LAN","url":"https://openreview.net/pdf?id=nZeVKeeFYf9"},{"title":"ICLR Poster LoRA: Low-Rank Adaptation of Large Language Models","url":"https://iclr.cc/virtual/2022/poster/6319"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=nZeVKeeFYf9"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf"},{"title":"[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685"}]

I found relevant research on the expressive power of Low-Rank Adaptation (LoRA). Here are the key findings:

## Main Results

This paper takes the first step to theoretically analyzing the expressive power of Low-Rank Adaptation (LoRA).

### For Fully Connected Neural Networks (FCNNs):

LoRA can adapt any model to accurately represent any smaller target model if LoRA-rank ≥ (width of f) × (depth of target / depth of f), under a mild assumption. Additionally, the approximation error is quantified when the LoRA-rank is lower than the threshold.

### For Transformer Networks:

Any model can be adapted to a target model of the same size with rank-(embedding size/2) LoRA adapters.

## Theoretical Contributions

Even though the learnable parameters under LoRA finetuning appear to be highly constrained, the effective expressive power of LoRA is nearly optimal up to a constant factor of 2. This discovery provides the first theoretical insights into the practical success of LoRA.

The research formally characterizes necessary LoRA ranks for adaptation tasks and establishes approximation error bounds, particularly characterizing the approximation error between the finetuned model and the target model as a function of the LoRA-rank.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0dd740e2-e93c-4bec-a346-96bae29b3f5b",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "a42e0f40-452c-4015-850e-da4eaa9b7ab3",
  "sourceToolAssistantUUID": "0dd740e2-e93c-4bec-a346-96bae29b3f5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-13T19:44:38.519Z_

<details><summary>↩ Tool result · `toolu_017zz72fq4UkRHC3im7smnwa`</summary>

```text
Web search results for query: "LoRA fine-tuning representation change bound theorem "low rank" perturbation theory neural network"

Links: [{"title":"Rethinking the Rank Threshold for LoRA Fine-Tuning","url":"https://arxiv.org/html/2605.03724"},{"title":"LoRA+: Efficient Low Rank Adaptation of Large Models","url":"https://arxiv.org/pdf/2402.12354"},{"title":"Why LoRA Resists Label Noise: A Theoretical Framework for Noise-Robust Parameter-Efficient Fine-Tuning","url":"https://arxiv.org/html/2602.00084"},{"title":"LORA: LOW-RANK ADAPTATION OF LARGE LAN- GUAGE MODELS Edward Hu∗ Yelong Shen∗","url":"https://arxiv.org/pdf/2106.09685"},{"title":"[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685"},{"title":"LORA: LOW-RANK ADAPTATION OF LARGE LAN","url":"https://openreview.net/pdf?id=nZeVKeeFYf9"},{"title":"Low-Rank Adaptation for Foundation Models: A Comprehensive Review","url":"https://arxiv.org/html/2501.00365v1"},{"title":"LoRA Training Provably Converges to a Low-Rank Global Minimum or It Fails Loudly (But it Probably Won’t Fail)","url":"https://arxiv.org/html/2502.09376v3"},{"title":"Understanding LoRA - Low Rank Adaptation For Finetuning Large Models | Towards Data Science","url":"https://towardsdatascience.com/understanding-lora-low-rank-adaptation-for-finetuning-large-models-936bce1a07c6/"},{"title":"Low Rank Adaptation (Lora) | Continuum Labs","url":"https://training.continuumlabs.ai/training/the-fine-tuning-process/parameter-efficient-fine-tuning/low-rank-adaptation-lora"}]

Based on the search results, I found several relevant theoretical works on LoRA fine-tuning with bounds and perturbation analysis:

## Key Theoretical Results

Recent landscape analysis of LoRA fine-tuning in the neural tangent kernel regime by Jang et al. (2024) establishes theoretical bounds on LoRA behavior, building on kernel-based views of pretrained-model fine-tuning.

One theoretical framework characterizes: (1) the memorization capacity bound that limits fitting of noisy samples, (2) the optimal rank balancing approximation and noise-induced errors, and (3) the temporal separation of clean pattern learning from noise memorization.

## Representation Change and Low-Rank Structure

A key result identifies a phase transition where tokens bifurcate into new clusters after a critical time governed by eigenvalue gaps in the Value matrix, showing how LoRA fine-tunes models without catastrophic forgetting while preserving token structure early in training and allowing controlled divergence.

One line of theoretical work focuses on analyzing LoRA's training dynamics, exploring why optimizers like SGD or Adam successfully find effective low-rank updates despite the non-convexity introduced by the factorization and inherent non-convexity of neural networks by utilizing linearization.

## Generalization Bounds

Recent work derives generalization bounds for different LoRA variants using an information-theoretic framework, and analysis shows the absence of any rank threshold for cross-entropy under the Polyak–Łojasiewicz inequality.

The search results reveal active theoretical development connecting LoRA to perturbation theory, low-rank optimization, and neural network representation dynamics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fdaca3a-e26f-46b3-9fa0-dea12075d7a1",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "5ae1398e-c327-4163-bca8-2091e79ba2a6",
  "sourceToolAssistantUUID": "0fdaca3a-e26f-46b3-9fa0-dea12075d7a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T19:44:39.965Z_

<details><summary>↩ Tool result · `toolu_01XdQVPUSJN1LoUGMUsWL3cK`</summary>

```text
Web search results for query: ""LoRA stability" theorem bound representation shift formal proof 2024 2025"

Links: [{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/4e243e95c913b367775d71d7182b99d9-Paper-Conference.pdf"},{"title":"Stable-LoRA: Stabilizing Feature Learning of Low-Rank ...","url":"https://arxiv.org/pdf/2603.05204"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.20625"},{"title":"FLoRG: Federated Fine-tuning with Low-rank Gram ...","url":"https://arxiv.org/pdf/2602.17095"},{"title":"Stable-LoRA: Stabilizing Feature Learning of Low-Rank Adaptation","url":"https://arxiv.org/html/2603.05204v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=VpWki1v2P8"},{"title":"On the Convergence Rate of LoRA Gradient Descent Siqiao Mu Diego Klabjan","url":"https://arxiv.org/pdf/2512.18248"},{"title":"CE-LoRA: Computation-Efficient LoRA Fine-Tuning for Language Models","url":"https://arxiv.org/html/2502.01378v1"},{"title":"LoRA Training Provably Converges to a Low-Rank Global Minimum or It Fails Loudly (But it Probably Won’t Fail)","url":"https://arxiv.org/html/2502.09376v3"},{"title":"Computational Limits of Low-Rank Adaptation (LoRA) Fine-Tuning for Transformer Models | OpenReview","url":"https://openreview.net/forum?id=Lf5znhZmFu"}]

I've completed a web search for "LoRA stability theorem bound representation shift formal proof 2024 2025" and found several highly relevant recent papers. Here's a summary of the key findings:

## Recent LoRA Stability Research (2024-2025)

**Stable-LoRA (2025):**
Stable-LoRA proposes a weight-shrinkage strategy for LoRA optimization that dynamically enhances the stability of feature learning. The paper provides formal definitions: LoRA feature learning is stable if the final output update ∆Yt = Θ(1) for all iterations, which only constrains the final output update rather than requiring intermediate representations to individually scale as Θ(1). The authors demonstrate both theoretically and empirically that non-zero initialization of matrix A compromises stable feature learning.

**Convergence and Gradient Descent Analysis:**
LoRA gradient descent converges to a stationary point at O(1/√T), which matches the standard convergence rate of gradient descent on Lipschitz smooth functions when the parameter norm is uniformly bounded.

**Transformation-Invariant LoRA Optimization (ICLR 2025):**
Research has shown that applying standard optimizers to LoRA leads to updates that are not transformation invariant, and in practice one LoRA factor often dominates the optimization process, receiving substantial updates while the other remains nearly fixed.

**Loss Landscape Analysis:**
Recent work concludes that any second-order stationary point is a global minimum under certain conditions, using proof techniques inspired by low-rank optimization literature that extend results from matrix sensing to cover both special and generic regimes.

These papers collectively provide formal theorems and proofs regarding LoRA's stability properties and representation shift dynamics during training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc473b59-d7bd-416d-a239-51ec75b9a03e",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "aeecfd7f-883e-459b-9c04-acc4e5d695a0",
  "sourceToolAssistantUUID": "cc473b59-d7bd-416d-a239-51ec75b9a03e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-13T19:44:43.519Z_

This is very important -- let me fetch the Stable-LoRA paper, the noise-robust LoRA paper, and the expressive power paper's HTML version for more detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aeecfd7f-883e-459b-9c04-acc4e5d695a0",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19Adg3mXDgK6uG1gc4P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bb22d51-cd9b-40f6-a6a8-bc7937d3a777",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1EVsBgRKWAkdvLRj2vyDs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2913,
      "cache_read_input_tokens": 17580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2913,
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

_source line 34 · 2026-05-13T19:44:45.888Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0143LDcFnuFaWcEjDDR3qzt7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.05204",
  "prompt": "Extract the full abstract, key theorems, and formal definitions. Specifically: how do they define \"stable feature learning\" for LoRA? Do they provide bounds on representation change (Delta beta or similar)? What is their main theoretical contribution regarding bounding representation shifts under low-rank perturbations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bb22d51-cd9b-40f6-a6a8-bc7937d3a777",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19Adg3mXDgK6uG1gc4P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d53f107-e892-4696-80d5-f1bf2098ae37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1EVsBgRKWAkdvLRj2vyDs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2913,
      "cache_read_input_tokens": 17580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2913,
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

_source line 35 · 2026-05-13T19:44:48.225Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AxA8UaESEQ8QRi5qypacd1`</summary>

```json
{
  "url": "https://arxiv.org/html/2310.17513v3",
  "prompt": "Extract the main theorems about LoRA's expressive power. Do they bound the approximation error as a function of rank? Do they analyze how much the internal representations can change under LoRA? List specific theorem statements if visible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d53f107-e892-4696-80d5-f1bf2098ae37",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19Adg3mXDgK6uG1gc4P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b9dcc42-eeae-4367-8754-65f646836693",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1EVsBgRKWAkdvLRj2vyDs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2913,
      "cache_read_input_tokens": 17580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2913,
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

### Tool result

_source line 36 · 2026-05-13T19:44:50.191Z_

<details><summary>↩ Tool result · `toolu_0143LDcFnuFaWcEjDDR3qzt7`</summary>

```text
# Analysis of Stable-LoRA Paper

## Full Abstract

The paper establishes that LoRA can achieve stable feature learning under appropriate hyperparameters and initializations. However, the non-zero initialization of matrix A compromises this self-stability. Their solution, Stable-LoRA, uses weight-shrinkage optimization during early training to enhance stability while preserving benefits of non-zero initialization.

## Formal Definitions

Unfortunately, the webpage content provided does not include the detailed mathematical sections. The abstract mentions the update formula: **W = W₀ + sBA**, where W₀ is the frozen weight, s is a scaling factor, and A, B are trainable low-rank matrices.

## Key Limitations

The extracted content does not provide:
- Explicit mathematical definition of "stable feature learning"
- Formal bounds on representation change (Δβ or similar metrics)
- Detailed theoretical contribution statements with specific inequalities

## What We Know

The paper claims to offer "theoretical and empirical validation" of their method's effectiveness, but the abstract lacks the formal theorems and bounded perturbation analysis necessary to answer your question completely.

**To obtain this information, you would need to access the full PDF** at the arXiv link provided, which would contain the rigorous mathematical definitions and theorems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d53f107-e892-4696-80d5-f1bf2098ae37",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "dceb9a8c-afe0-44f9-af1d-ecebecc06db2",
  "sourceToolAssistantUUID": "8d53f107-e892-4696-80d5-f1bf2098ae37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-13T19:44:52.567Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PPjTD4AFPCC23MQgyHQGk9`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.00084",
  "prompt": "Extract the key theoretical framework. How do they bound LoRA's behavior? Do they provide bounds on representation changes? What is the memorization capacity bound? List any formal theorems about perturbation or representation stability."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dceb9a8c-afe0-44f9-af1d-ecebecc06db2",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19Adg3mXDgK6uG1gc4P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd754fd2-5429-42e8-a608-1c011afecdb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R1EVsBgRKWAkdvLRj2vyDs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2913,
      "cache_read_input_tokens": 17580,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2913,
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

### Tool result

_source line 38 · 2026-05-13T19:44:55.201Z_

<details><summary>↩ Tool result · `toolu_01AxA8UaESEQ8QRi5qypacd1`</summary>

```text
# Main Theorems on LoRA's Expressive Power

## Key Theoretical Results

The paper establishes two primary informal theorems:

**Theorem 1 (FNNs):** For fully connected neural networks, low-rank adapters can match a target model when the LoRA-rank satisfies: "rank ≥ (width of f) × depth of target / depth of frozen model" under mild conditions.

**Theorem 2 (Transformers):** For transformer networks, any model can adapt to a same-sized target using "rank-(embedding size/2)" LoRA adapters on attention matrices.

## Approximation Error Bounds

Yes, the paper rigorously bounds approximation error as a function of rank:

**Lemma 2** provides an expected squared error bound: "𝔼‖f(x) - target_f(x)‖²₂ ≤ ‖Σ‖_F σ²_{RL+1}(E)" where σ_{RL+1} denotes the (RL+1)-th singular value of the error matrix.

The analysis shows that when rank is below the threshold, approximation degrades gracefully based on singular value decay rather than catastrophically failing.

## Internal Representation Analysis

The paper does **not** directly analyze how internal activations change under LoRA. Instead, it focuses on:

1. **Weight matrix approximation** - matching frozen model weights to target weights through low-rank updates
2. **Linearization technique** - eliminating ReLU nonlinearity in intermediate layers to enable analysis
3. **Rank requirements** - characterizing when LoRA adapters can achieve exact or approximate matching

The theoretical approach treats internal representations implicitly through the model partition strategy rather than explicitly analyzing hidden activation changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b9dcc42-eeae-4367-8754-65f646836693",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "6df49a71-f5a9-4864-8d9b-8ee0d18ca393",
  "sourceToolAssistantUUID": "3b9dcc42-eeae-4367-8754-65f646836693",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-13T19:44:58.746Z_

<details><summary>↩ Tool result · `toolu_01PPjTD4AFPCC23MQgyHQGk9`</summary>

```text
# Key Theoretical Framework in LoRA Noise Robustness Paper

## Core Theorems

**Theorem 3.3 (Memorization Capacity Bound):**
The paper establishes that rank-r LoRA cannot memorize all possible label assignments once sample size exceeds O(r(d+k−r)). This provides an existential bound showing "some label assignments are unachievable" when data volume surpasses the degrees of freedom available to the low-rank parameterization.

**Theorem 3.7 (Rank-Robustness Tradeoff):**
The authors derive an optimal rank formula balancing three error sources:

- Bias (approximation): O(r^−2α)
- Variance (estimation): O(rd/n)  
- Noise-induced: O(ηrd/n)

The optimal rank scales as r* = O((n/d(1+η))^(1/(2α+1))), demonstrating that "optimal rank decreases with noise rate."

**Theorem 3.10 (Temporal Separation):**
This establishes that gradient descent exhibits temporal separation: clean patterns are learned in early epochs while noise memorization occurs later. The noise-learning threshold is t* = O((1/γσ_r)log(1/η)), where the logarithmic factor depends on corruption rate η.

## Representation Stability

The framework does not explicitly bound representation changes. Instead, it focuses on how the low-rank constraint itself limits fitting capacity—providing implicit regularization through parametric restrictions rather than direct perturbation bounds on learned features.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd754fd2-5429-42e8-a608-1c011afecdb3",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "f7284dec-16b6-4dcf-a908-dbd49c6e126f",
  "sourceToolAssistantUUID": "fd754fd2-5429-42e8-a608-1c011afecdb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-13T19:45:03.451Z_

Now let me get the Stable-LoRA full HTML version for the actual theorem statements, and search for any work specifically on bounding |Delta beta| or coefficient changes under LoRA.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7284dec-16b6-4dcf-a908-dbd49c6e126f",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19C21FdRrbsXvtWdgAK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8adcba13-89c5-48e5-a62c-d74498534b04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2P3xpxcxGZihDmdts9JGK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1554,
      "cache_read_input_tokens": 20493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1554,
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

_source line 41 · 2026-05-13T19:45:06.438Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0182Crx4Ud7DgUTwHb4tpbVC`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.05204v1",
  "prompt": "Extract all formal definitions and theorems. Specifically look for: (1) the formal definition of \"stable feature learning\" for LoRA, (2) any bounds on representation changes like Delta Y or activation changes, (3) the main theoretical results about how low-rank perturbations affect learned features. Include exact theorem statements if possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8adcba13-89c5-48e5-a62c-d74498534b04",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19C21FdRrbsXvtWdgAK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e339d38-4894-4634-9757-2a479cb05fe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2P3xpxcxGZihDmdts9JGK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1554,
      "cache_read_input_tokens": 20493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1554,
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

_source line 42 · 2026-05-13T19:45:07.233Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KRbXPqwRgL3qjFsiC1HZaB`</summary>

```json
{
  "query": "bound representation change low-rank weight perturbation neural network \"beta\" coefficient feature learning theory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e339d38-4894-4634-9757-2a479cb05fe1",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19C21FdRrbsXvtWdgAK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43d247dd-74c2-4748-983e-3a3edcd59ad5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2P3xpxcxGZihDmdts9JGK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1554,
      "cache_read_input_tokens": 20493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1554,
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

_source line 43 · 2026-05-13T19:45:08.026Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X5dvjDt56cWiNJvAe9K27C`</summary>

```json
{
  "query": "LoRA rank regularization implicit bias low rank perturbation representation geometry 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43d247dd-74c2-4748-983e-3a3edcd59ad5",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19C21FdRrbsXvtWdgAK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "384d7169-0145-4349-ab24-7cacca37b30b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A2P3xpxcxGZihDmdts9JGK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1554,
      "cache_read_input_tokens": 20493,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1554
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 20493,
          "cache_creation_input_tokens": 1554,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1554,
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

_source line 44 · 2026-05-13T19:45:13.226Z_

<details><summary>↩ Tool result · `toolu_0182Crx4Ud7DgUTwHb4tpbVC`</summary>

```text
# Formal Definitions and Theorems from Stable-LoRA

## Definition 1: LoRA Stable Feature Learning

"LoRA feature learning is stable, if ΔY_t = Θ(1) for all training steps t."

This definition requires output updates to remain bounded with respect to model width n, neither exploding nor vanishing as width increases.

## Theorem 3.1: Self-Stability of LoRA

"LoRA can naturally achieve and sustain stable feature learning, if the hyper-parameters s and η are tuned such that γ[s] + 2γ[η] + 1 = 0, and the initializations A₀ and B₀ satisfy γ[A₀Z] ≤ γ[η] + 1 and γ[B₀] ≤ γ[η]."

This establishes conditions under which LoRA automatically achieves feature stability without additional mechanisms.

## Key Technical Tools

**γ-function**: For variable v, γ[v] represents the power of n in v = Θ(n^γ[v]). For tensors, γ captures dominant scaling behavior among components.

**Main Constraint (Equation 3)**: Stability requires three components of ΔY_t to satisfy specific scaling relationships with learning rate η and scaling factor s.

## Central Finding

The paper demonstrates that non-zero initialization A₀ violates the stability condition γ[A₀Z] ≤ γ[η] + 1 in practice, causing persistent feature learning instability. Stable-LoRA addresses this through progressive weight shrinkage until norm balance: ||A||_F/n ≤ ||B||_F/m.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e339d38-4894-4634-9757-2a479cb05fe1",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "d845ac09-61a7-4d3e-8267-5017e7cdc25a",
  "sourceToolAssistantUUID": "0e339d38-4894-4634-9757-2a479cb05fe1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-13T19:45:15.292Z_

<details><summary>↩ Tool result · `toolu_01X5dvjDt56cWiNJvAe9K27C`</summary>

```text
Web search results for query: "LoRA rank regularization implicit bias low rank perturbation representation geometry 2024 2025 arXiv"

Links: [{"title":"[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685"},{"title":"Flat-LoRA: Low-Rank Adaptation over a Flat Loss Landscape","url":"https://arxiv.org/html/2409.14396v2"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models Edward Hu∗ Yelong Shen∗","url":"https://arxiv.org/pdf/2106.09685v1/1000"},{"title":"Mirror, Mirror of the Flow: How Does Regularization Shape Implicit Bias?","url":"https://arxiv.org/html/2504.12883"},{"title":"LoRA Training Provably Converges to a Low-Rank Global Minimum or It Fails Loudly (But it Probably Won’t Fail)","url":"https://arxiv.org/html/2502.09376v3"},{"title":"Why LoRA Fails to Forget: Regularized Low-Rank Adaptation Against","url":"https://arxiv.org/pdf/2601.06305"},{"title":"Post-Optimization Adaptive Rank Allocation for LoRA","url":"https://arxiv.org/html/2604.27796"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/html/2106.09685v2"},{"title":"LORA: LOW-RANK ADAPTATION OF LARGE LAN- GUAGE MODELS Edward Hu∗ Yelong Shen∗","url":"https://arxiv.org/pdf/2106.09685"},{"title":"Paper page - LoRA: Low-Rank Adaptation of Large Language Models","url":"https://huggingface.co/papers/2106.09685"}]

Based on the search results, I found several recent papers from 2024-2025 on arXiv that relate to your query about LoRA, rank regularization, implicit bias, and low-rank perturbations:

## Key Recent Papers

**1. LoRA Training Provably Converges to a Low-Rank Global Minimum (2025)**

The zero-initialization and weight decay in LoRA training induce an implicit bias toward the low-rank, small-magnitude region of the parameter space, where global minima lie, shedding light on why practical LoRA training effectively converges to global minima. This paper addresses the theoretical aspects of implicit bias in LoRA optimization.

**2. Mirror, Mirror of the Flow: How Does Regularization Shape Implicit Bias? (2025)**

This work explores applications including sparse coding, matrix sensing, attention mechanisms in transformers, and Low-Rank Adaptation (LoRA) through experiments while analyzing how explicit regularization shapes implicit bias through mirror flow frameworks.

**3. Flat-LoRA: Low-Rank Adaptation over a Flat Loss Landscape (2025)**

This paper improves LoRA by optimizing the sharpness of the loss landscape in the full parameter space, describing a random perturbation generation strategy for effectively improving generalization.

**4. Post-Optimization Adaptive Rank Allocation for LoRA (2025)**

This work introduces Post-Optimization Adaptive Rank Allocation (PARA), a post-optimization compression framework that efficiently identifies and prunes redundant spectral components, serving as a data-free proxy for parameter importance.

These papers collectively address implicit bias, rank regularization, low-rank perturbation strategies, and representation geometry in the context of LoRA and modern fine-tuning methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "384d7169-0145-4349-ab24-7cacca37b30b",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "7264e588-dd9a-4f13-a493-1235ba996146",
  "sourceToolAssistantUUID": "384d7169-0145-4349-ab24-7cacca37b30b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-13T19:45:16.091Z_

<details><summary>↩ Tool result · `toolu_01KRbXPqwRgL3qjFsiC1HZaB`</summary>

```text
Web search results for query: "bound representation change low-rank weight perturbation neural network "beta" coefficient feature learning theory"

Links: [{"title":"Theory of Minimal Weight Perturbations in Deep Networks and its Applications for Low-Rank Activated Backdoor Attacks","url":"https://arxiv.org/html/2601.16880"},{"title":"Low-rank bias, weight decay, and model merging in neural networks","url":"https://arxiv.org/pdf/2502.17340"},{"title":"Theory of Minimal Weight Perturbations in Deep Networks ...","url":"https://www.arxiv.org/pdf/2601.16880"},{"title":"Rank Diminishing in Deep Neural Networks","url":"https://proceedings.neurips.cc/paper_files/paper/2022/file/d5cd70b708f726737e2ebace18c3f71b-Paper-Conference.pdf"},{"title":"On Generalization Bounds for Neural Networks with Low Rank Layers","url":"https://arxiv.org/html/2411.13733v1"},{"title":"Neural Network Perturbation Theory (NNPT): Learning Residual Corrections from","url":"https://arxiv.org/pdf/2512.01558"},{"title":"Perturbation-based Learning for Recurrent Neural Networks","url":"https://arxiv.org/html/2405.08967v1"},{"title":"Generalization Bounds for Rank-sparse Neural Networks Antoine Ledent","url":"https://arxiv.org/pdf/2510.21945"},{"title":"Theoretical Properties for Neural Networks with Weight Matrices of Low","url":"http://proceedings.mlr.press/v70/zhao17b/zhao17b.pdf"},{"title":"Theory of Deep Learning - cs.Princeton","url":"https://www.cs.princeton.edu/~arora/TheoryDL.pdf"}]

I've completed the web search with your query about bound representation change, low-rank weight perturbation, neural networks, beta coefficient, and feature learning theory. Here's a summary of the most relevant results:

## Key Findings:

The search retrieved several highly relevant papers on neural network theory:

1. **"Theory of Minimal Weight Perturbations in Deep Networks"** (arxiv.org/html/2601.16880) - This work derives minimal norm weight perturbations of DNNs required to achieve specified output changes and contrasts single-layer exact formulae with more generic multi-layer Lipschitz constant based robustness guarantees.

2. **Low-rank Bias and Weight Decay** (arxiv.org/pdf/2502.17340) - Provides bounds on gaps with exponentially decaying terms arising from weight decay and epsilon-dependent terms capturing similarity of inputs in different tasks.

3. **Rank Diminishing in Deep Neural Networks** (NeurIPS 2022) - Discusses how the assumption of low-rank feature representations leads to algorithmic developments, while noting that the intrinsic mechanism yielding low-rank structures remains unclear, and conducts rigorous study on the behavior of network rank.

4. **"On Generalization Bounds for Neural Networks with Low Rank Layers"** (arxiv.org/html/2411.13733v1) - Demonstrates how low-rank layers can prevent the multiplication of rank and dimension-dependent quantities across layers, leveraging this to establish Gaussian complexity bounds for low-rank deep networks.

5. **"Generalization Bounds for Rank-sparse Neural Networks"** - Notes that depth induces low-rank representations, and the training dynamics of DNNs through gradient-based methods naturally encourages low-rank representations converging to a bottleneck intrinsic dimension.

These papers directly address theoretical bounds on representation changes under weight perturbations and the role of low-rank structures in neural network learning theory.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43d247dd-74c2-4748-983e-3a3edcd59ad5",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "7bf5beca-1830-4d17-9bf0-6ea8cff07ac8",
  "sourceToolAssistantUUID": "43d247dd-74c2-4748-983e-3a3edcd59ad5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-13T19:45:19.948Z_

Let me get one more critical piece -- the "Layer-wise LoRA fine-tuning with CKA" paper and check for any work specifically on bounding downstream coefficient changes under LoRA.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bf5beca-1830-4d17-9bf0-6ea8cff07ac8",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19DJ9t57LcG2EZC3q6E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6fb4ff9-a80a-46aa-bfec-bc3d6988be2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WbijTanosp3a1Ep1rTMhs7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 1667,
      "cache_read_input_tokens": 22047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1667,
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

_source line 48 · 2026-05-13T19:45:22.022Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01J4Wn2rGfmVBEHkx9tvkKvJ`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2602.05988",
  "prompt": "Extract the abstract and method. How do they use CKA to guide LoRA fine-tuning? Do they measure representation similarity between base and LoRA-adapted models? What metrics do they report?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6fb4ff9-a80a-46aa-bfec-bc3d6988be2e",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19DJ9t57LcG2EZC3q6E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a99c748e-8dff-4cff-9feb-690ec5f8ccbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WbijTanosp3a1Ep1rTMhs7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 1667,
      "cache_read_input_tokens": 22047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1667,
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

_source line 49 · 2026-05-13T19:45:22.687Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XQ1ww1unjBiQh3TkshtjAY`</summary>

```json
{
  "query": "\"LoRA\" \"downstream\" \"coefficient\" \"representation\" bound perturbation \"linear probe\" regression theory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a99c748e-8dff-4cff-9feb-690ec5f8ccbc",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19DJ9t57LcG2EZC3q6E",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae7b61e3-78ce-4fcf-8c29-279214efc6ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WbijTanosp3a1Ep1rTMhs7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 936,
      "cache_creation_input_tokens": 1667,
      "cache_read_input_tokens": 22047,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1667
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 936,
          "output_tokens": 228,
          "cache_read_input_tokens": 22047,
          "cache_creation_input_tokens": 1667,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1667,
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

_source line 50 · 2026-05-13T19:45:26.534Z_

<details><summary>↩ Tool result · `toolu_01J4Wn2rGfmVBEHkx9tvkKvJ`</summary>

```text
# Layer-wise LoRA Fine-tuning with CKA: Summary

## Abstract
The paper proposes a method for fine-tuning large language models using LoRA (Low-Rank Adaptation) that leverages Centered Kernel Alignment (CKA) to guide layer-wise adaptation decisions.

## Method Overview
The researchers use CKA—a similarity metric comparing representations between models—to identify which layers require LoRA adaptation. Rather than uniformly applying LoRA across all layers, they measure representational divergence between the base pretrained model and intermediate fine-tuning states using CKA, then selectively apply LoRA only to layers exhibiting significant representation changes.

## Key Approach
The technique involves:
- Computing CKA scores between base model representations and adapted model representations across layers
- Using these similarity measurements to determine which layers need trainable LoRA modules
- Applying efficient layer-wise adaptation based on representation divergence rather than applying LoRA uniformly

## Metrics Reported
The authors evaluate their approach using standard benchmarks including:
- GLUE (text classification tasks)
- Mathematical reasoning datasets (GSM8K, MATH)
- Code generation (HumanEval, MBPP)
- Multimodal tasks (LLaVA, ScienceQA)

Results demonstrate that selective LoRA application guided by CKA achieves comparable performance to full LoRA while reducing trainable parameters and computational overhead.

[Binary content (application/pdf, 911.7KB) also saved to /home/ubuntu/.claude-account-2/projects/-/d420c8fc-73ad-49e5-a076-6b52b56c836b/tool-results/webfetch-1778701522040-9en1ls.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a99c748e-8dff-4cff-9feb-690ec5f8ccbc",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "f419f534-9b1a-4901-85f5-c97a1750db3f",
  "sourceToolAssistantUUID": "a99c748e-8dff-4cff-9feb-690ec5f8ccbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-13T19:45:30.008Z_

<details><summary>↩ Tool result · `toolu_01XQ1ww1unjBiQh3TkshtjAY`</summary>

```text
Web search results for query: ""LoRA" "downstream" "coefficient" "representation" bound perturbation "linear probe" regression theory"

Links: [{"title":"Formalising the Logit Shift Induced by LoRA: A Technical Note","url":"https://arxiv.org/html/2604.20313"},{"title":"Linearization Explains Fine-Tuning in Large Language Models","url":"https://openreview.net/pdf?id=tdwRIP6NG2"},{"title":"[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685"},{"title":"Bernoulli-LoRA: A Theoretical Framework for Randomized Low-Rank Adaptation","url":"https://arxiv.org/html/2508.03820v1"},{"title":"LoRA+: Efficient Low Rank Adaptation of Large Models","url":"https://arxiv.org/pdf/2402.12354"},{"title":"Understanding Linear Probing then Fine-tuning Language ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/fcc22e5b7d5d2155d994da22d045f0a6-Paper-Conference.pdf"},{"title":"LORA: LOW-RANK ADAPTATION OF LARGE LAN","url":"https://openreview.net/pdf?id=nZeVKeeFYf9"},{"title":"LoRA Training Provably Converges to a Low-Rank Global Minimum or It Fails Loudly (But it Probably Won’t Fail)","url":"https://arxiv.org/html/2502.09376v3"},{"title":"LoRA Training in the NTK Regime has No Spurious Local Minima","url":"https://arxiv.org/pdf/2402.11867"},{"title":"Preprint. Under review LORA-DA: DATA-AWARE INITIALIZATION FOR LOW-","url":"https://arxiv.org/pdf/2510.24561"}]

I've found several highly relevant research papers that discuss LoRA with connections to the specific topics you mentioned. Here are the key findings:

## Top Results

A recent technical note formalizes the logit shift induced by LoRA by developing a principled approximation that connects a layerwise LoRA perturbation to its downstream effect on the model output. The work provides a local first-order analysis of the logit shift induced by LoRA.

Research also bounds the difference between the kernel of full fine-tuning and the kernel of LoRA. One approach uses tangent kernel regression and the eigenvalue decomposition of the neural tangent kernel to derive bounds on the empirical risk of fine-tuning, with bounds on the spectral perturbation on the NTK when a set of trainable parameters is added to fine-tuning.

## Linear Probe and Regression Theory

Analysis based on the NTK has been extended to the training process of LoRA by following a linear model setting and analyzing the training dynamics of LoRA in the NTK regime.

## LoRA Theory and Representation

While prior analyses of LoRA's training dynamics either rely on linearization arguments or consider highly simplified setups, recent work analyzes the LoRA loss landscape without such restrictive assumptions.

The search results reveal an active area of theoretical research on LoRA focusing on perturbation bounds, downstream effects, and neural tangent kernel theory applied to understand LoRA's behavior during fine-tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae7b61e3-78ce-4fcf-8c29-279214efc6ee",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "f3fc57b6-a75c-4c1c-8a04-6b7bce605aa8",
  "sourceToolAssistantUUID": "ae7b61e3-78ce-4fcf-8c29-279214efc6ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-13T19:45:34.921Z_

This is a critical find -- let me fetch that "Formalising the Logit Shift Induced by LoRA" paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3fc57b6-a75c-4c1c-8a04-6b7bce605aa8",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19EKehoj4PptvhgEP64",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "000025a5-7730-4801-82e2-1c82c21835df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XoNgfCugaaDS4Fz8zk6Rwe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2470,
      "cache_read_input_tokens": 23714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2470,
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

_source line 53 · 2026-05-13T19:45:37.420Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Un2Kq1Gk9V7Jzu5rQRmddn`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.20313",
  "prompt": "Extract the full abstract, main theorems, and key results. This paper formalizes the logit shift induced by LoRA. What bounds do they derive? How do they connect layerwise LoRA perturbation to downstream effects on model output? Do they bound representation changes? List all theorem or proposition statements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "000025a5-7730-4801-82e2-1c82c21835df",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19EKehoj4PptvhgEP64",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60607f2f-c9ff-4179-a422-69ef2e6c3ca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XoNgfCugaaDS4Fz8zk6Rwe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2470,
      "cache_read_input_tokens": 23714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2470,
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

_source line 54 · 2026-05-13T19:45:38.305Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BXzNSTyhqciYHixgwnYNws`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.09376v3",
  "prompt": "Extract the main theoretical results. Do they provide bounds on how LoRA changes representations? What are the key theorems about convergence and loss landscape?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60607f2f-c9ff-4179-a422-69ef2e6c3ca1",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19EKehoj4PptvhgEP64",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a5e24e1-b496-46d7-a779-f0558bb15084",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XoNgfCugaaDS4Fz8zk6Rwe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2470,
      "cache_read_input_tokens": 23714,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2470
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 277,
          "cache_read_input_tokens": 23714,
          "cache_creation_input_tokens": 2470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2470,
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

_source line 55 · 2026-05-13T19:45:43.444Z_

<details><summary>↩ Tool result · `toolu_01Un2Kq1Gk9V7Jzu5rQRmddn`</summary>

```text
# Summary: Formalising the Logit Shift Induced by LoRA

## Abstract
This technical note provides a first-order mathematical formalization of how Low-Rank Adaptation (LoRA) changes model logits. Using Fréchet approximation around the base model's trajectory, the authors demonstrate that multi-layer LoRA effects decompose into layerwise contributions plus higher-order coupling terms.

## Key Propositions

**Proposition 1 (Single-Layer First-Order Logit Shift):**
For LoRA applied at layer *l*, the logit change satisfies:
> "δℓ_y(x) = (α/r)u_y^T J_{l+1→L}(x)B_l A_l z_l + o(‖ΔW_l z_l‖)"

This identifies three components determining LoRA's effect: the intermediate representation, the LoRA injection direction, and downstream network sensitivity.

## Multi-Layer Result

For multiple LoRA layers in set *S*:
> "ℓ̃(y;x) - ℓ(y;x) = (α/r)∑_{l∈S} u_y^T J_{l+1→L}(x)B_l A_l z_l + R_y(Δ)"

The remainder satisfies R_y(Δ) = o(‖Δ‖), capturing inter-layer coupling effects.

## Bounds and Scope

**No explicit magnitude bounds are derived.** Instead, the analysis provides:
- A **linear decomposition** of first-order effects across layers
- A **characterization of remainder terms** as higher-order
- A **criterion for fact-margin reversal**: the first-order correction must overcome the base model's preference margin

The framework explicitly acknowledges limitations: validity requires small perturbations where higher-order terms remain negligible.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60607f2f-c9ff-4179-a422-69ef2e6c3ca1",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "09b810dc-0a92-4bac-b934-232083a670b3",
  "sourceToolAssistantUUID": "60607f2f-c9ff-4179-a422-69ef2e6c3ca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-13T19:45:45.179Z_

<details><summary>↩ Tool result · `toolu_01BXzNSTyhqciYHixgwnYNws`</summary>

```text
# Main Theoretical Results from LoRA Training Paper

## Key Theorems

**Theorem 1 (Primary Result):** Characterizes the loss landscape for LoRA fine-tuning. It establishes two regimes:

1. **Special Regime** (2α > β): Every second-order stationary point is a global minimum
2. **Generic Regime** (2α ≤ β): Each stationary point is either a global minimum with low rank/magnitude, or a spurious solution with "high rank and large magnitude"

The paper notes: "LoRA training converges to a global minimizer or fails loudly (But it Probably Won't Fail)" - capturing the intuition that bad solutions are detectable through their high-rank, large-magnitude characteristics.

**Theorem 2:** Extends the analysis to multiple weight matrices, preserving the qualitative conclusions about the tradeoff between rank and solution quality.

## Bounds and Characterizations

Rather than direct representation change bounds, the results provide **structural characterizations**:

- Spurious solutions must satisfy: σᵣ(X□) ≥ (2α/β)·σᵣ₊(X□)
- Distance from global minimum for spurious solutions: ‖X□ - X⋆‖²ₓ ≥ ‖projection error‖²/(1 - 2α·σᵣ₊/(β·σᵣ))

## Key Assumptions

The analysis assumes:
- Existence of low-rank global minimizer for full fine-tuning
- Restricted strong convexity (RSC) and restricted smoothness (RSM) near the solution
- Nuclear norm regularization (equivalent to weight decay)

The results do **not** provide bounds on absolute representation changes, but rather establish qualitative guarantees about convergence behavior and the relationship between rank, magnitude, and optimality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a5e24e1-b496-46d7-a779-f0558bb15084",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "48637ca4-89de-4d0d-bce6-0853a8cb4652",
  "sourceToolAssistantUUID": "4a5e24e1-b496-46d7-a779-f0558bb15084",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-13T19:45:49.202Z_

Now I have a comprehensive picture. Let me do one final search to make sure I haven't missed any paper that directly proves a "LoRA stability theorem" bounding representation changes (|Delta beta|).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48637ca4-89de-4d0d-bce6-0853a8cb4652",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19FSefMU449QPBbtucn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec3da2cb-5787-4b48-b775-67a2af524da9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANZTzmjUMF7k9b3WvphnB9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 26184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1218,
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

_source line 58 · 2026-05-13T19:45:50.215Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BkzMuD9Eb4wvyvvUgetQeR`</summary>

```json
{
  "query": "\"LoRA\" \"representation change\" \"upper bound\" theorem proof arxiv 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec3da2cb-5787-4b48-b775-67a2af524da9",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19FSefMU449QPBbtucn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e992394-f335-454b-b029-e5fe47b78559",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANZTzmjUMF7k9b3WvphnB9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 26184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1218,
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

_source line 59 · 2026-05-13T19:45:50.623Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N8TwSe6N7cw1KNmXXuu3GW`</summary>

```json
{
  "query": "density ratio estimation latent space distribution shift LoRA fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e992394-f335-454b-b029-e5fe47b78559",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19FSefMU449QPBbtucn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30792764-c421-48d2-b171-64f73cdaba35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANZTzmjUMF7k9b3WvphnB9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 26184,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1218
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 26184,
          "cache_creation_input_tokens": 1218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1218,
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

_source line 60 · 2026-05-13T19:45:56.896Z_

<details><summary>↩ Tool result · `toolu_01N8TwSe6N7cw1KNmXXuu3GW`</summary>

```text
Web search results for query: "density ratio estimation latent space distribution shift LoRA fine-tuning"

Links: [{"title":"Latent Space Factorization in LoRA | OpenReview","url":"https://openreview.net/forum?id=Bqui2s3xFi"},{"title":"Latent Space Factorization in LoRA","url":"https://arxiv.org/html/2510.19640v1"},{"title":"[2510.19640] Latent Space Factorization in LoRA","url":"https://arxiv.org/abs/2510.19640"},{"title":"[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685"},{"title":"LoRAGen: Structure-Aware Weight Space Learning for LoRA Generation | OpenReview","url":"https://openreview.net/forum?id=mrafO7aTYj"},{"title":"Efficient Fine-Tuning with LoRA: A Guide to Optimal Parameter Selection for Large Language Models","url":"https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms"},{"title":"LoRA-TCN: A pre-trained/fine-tuning learning paradigm for drift adaptation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925400525014200"},{"title":"LAD: LoRA-Adapted Diffusion","url":"https://aclanthology.org/2025.emnlp-demos.8.pdf"},{"title":"LoRA Fine-tuning & Hyperparameters Explained (in Plain English) | Entry Point AI","url":"https://www.entrypointai.com/blog/lora-fine-tuning/"},{"title":"LoRA vs Full Fine-tuning: An Illusion of Equivalence","url":"https://arxiv.org/html/2410.21228v1"}]

Based on the web search results, I found several relevant papers and resources related to your query about density ratio estimation, latent space, distribution shift, and LoRA fine-tuning. Here are the key findings:

## Related Research

**Latent Space Factorization in LoRA (FVAE-LoRA)**: A recent approach proposes Factorized Variational Autoencoder LoRA (FVAE-LoRA), which leverages a VAE to learn two distinct latent spaces with a novel Evidence Lower Bound formulation that explicitly promotes factorization between the latent spaces, dedicating one latent space to task-salient features and the other to residual information. This method better isolates task-relevant signals, leading to improved robustness under distribution shifts.

**LoRA for Distribution Shift Adaptation**: A novel LoRA-TCN model integrates Low-Rank Adaptation with Temporal Convolutional Networks, where the low-rank matrices preserve general knowledge from different but related source domain, enabling knowledge transfer to drift-affected target domain with only a small amount of target domain data.

**Spectral Analysis of LoRA vs Full Fine-tuning**: LoRA and full fine-tuning have structural differences: while full fine-tuning makes small changes to existing singular vectors and singular values, LoRA introduces new singular vectors that have a large contribution to the norm of the updated parameter matrix.

The research suggests that combining latent space learning (like VAEs) with LoRA architectures can effectively address distribution shift challenges in fine-tuning, though the specific intersection of density ratio estimation with these techniques appears to be an emerging research direction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30792764-c421-48d2-b171-64f73cdaba35",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "e5631c16-8cf3-47e0-b445-ee080060245d",
  "sourceToolAssistantUUID": "30792764-c421-48d2-b171-64f73cdaba35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-13T19:45:57.310Z_

<details><summary>↩ Tool result · `toolu_01BkzMuD9Eb4wvyvvUgetQeR`</summary>

```text
Web search results for query: ""LoRA" "representation change" "upper bound" theorem proof arxiv 2024 2025 2026"

Links: [{"title":"[2406.03136] Computational Limits of Low-Rank Adaptation (LoRA) Fine-Tuning for Transformer Models","url":"https://arxiv.org/abs/2406.03136"},{"title":"The Scaling Law for LoRA Base on Mutual Information Upper Bound","url":"https://arxiv.org/html/2501.03152v1"},{"title":"[2501.03152] The Scaling Law for LoRA Base on Mutual Information Upper Bound","url":"https://arxiv.org/abs/2501.03152"},{"title":"Rethinking LoRA for Data Heterogeneous Federated Learning:","url":"https://www.arxiv.org/pdf/2602.01746"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.20625"},{"title":"On the Convergence Rate of LoRA Gradient Descent Siqiao Mu Diego Klabjan","url":"https://arxiv.org/pdf/2512.18248"},{"title":"1 Illustration of (a) vanilla LoRA; (b) LoRA variants utilizing an adaptive rank masking strategy; (c) LoRA variants employing a nonzero initialization strategy; and (d) GoRA, which introduces the key innovation of adaptively leveraging 𝑊’s gradients to allocate adapter ranks and initialize the weights of 𝐵. 𝐴₀ and 𝐵₀ denote the initialized value of matrix 𝐴 and matrix 𝐵","url":"https://arxiv.org/html/2502.12171v1"},{"title":"LoRA Training Provably Converges to a Low-Rank Global Minimum or It Fails Loudly (But it Probably Won’t Fail)","url":"https://arxiv.org/html/2502.09376v3"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf"},{"title":"CE-LoRA: Computation-Efficient LoRA Fine-Tuning for Language Models","url":"https://arxiv.org/html/2502.01378v1"}]

I found several relevant papers on LoRA with upper bound theorems and theoretical analysis. Here are the key results from recent arxiv papers (2024-2026):

## Key Papers Found

**1. Computational Limits of LoRA (arxiv 2406.03136, June 2024/2025)**

This paper derives a shared upper bound threshold for norms, showing that efficient (sub-quadratic) approximation algorithms of LoRA exist only below this threshold. The work identifies a sharp transition in the efficiency of all possible rank-r LoRA update algorithms for transformers, based on specific norms resulting from the multiplications of the input sequence X, pretrained weights W*, and adapter matrices αBA/r.

**2. The Scaling Law for LoRA Based on Mutual Information Upper Bound (arxiv 2501.03152, January 2025)**

This paper examines LoRA through an information-theoretic lens with mutual information upper bounds to establish scaling laws for fine-tuning.

**3. LoRA Training Convergence Analysis (arxiv 2502.09376, February 2025)**

Recent work identifies the training dynamics in a 2-layer setup, proving LoRA will align to a singular subspace of one-step gradient of full fine-tuning.

**4. Convergence Rate of LoRA Gradient Descent (arxiv 2512.18248, December 2025)**

This paper provides convergence rate analysis and theoretical bounds for LoRA optimization.

These papers represent the latest theoretical developments regarding LoRA with upper bound proofs and representation change analysis from 2024-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e992394-f335-454b-b029-e5fe47b78559",
  "isSidechain": true,
  "promptId": "5b46ad89-389b-47f2-a018-96735126287a",
  "agentId": "ad487675142d937dd",
  "type": "user",
  "uuid": "3e613d75-7db5-421d-b472-045a919a9624",
  "sourceToolAssistantUUID": "3e992394-f335-454b-b029-e5fe47b78559",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-13T19:47:03.518Z_

I now have a comprehensive picture. Here is my analysis:

---

## Report: Novelty and Feasibility of a "LoRA Stability Theorem" Bounding |Delta beta| Under Low-Rank Perturbations

### 1. Verification of arXiv 2503.18985

**Confirmed.** The paper "LoRA Subtraction for Drift-Resistant Space in Exemplar-Free Continual Learning" by Xuan Liu and Xiaobin Chang exists and was accepted to CVPR 2025. However, it is an **empirical/algorithmic** contribution, not a theoretical one. It introduces a method (LoRA-) that subtracts old-task LoRA weights from the pretrained weights before learning new tasks, creating a "Drift-Resistant Space." It does **not** provide formal bounds on representation drift -- its stability claims are empirical.

### 2. Existing Theoretical Work on LoRA and Representation Changes

I identified a rich and rapidly growing body of theoretical LoRA work. Here are the most relevant papers, organized by what they bound:

**A. Bounds on output/logit changes (closest to bounding |Delta beta|):**

- **"Formalising the Logit Shift Induced by LoRA" (arXiv 2604.20313, April 2025):** This is the most directly relevant paper. It provides a first-order Frechet approximation decomposing the logit shift as: `delta_y(x) = (alpha/r) * sum_{l in S} u_y^T J_{l+1->L}(x) B_l A_l z_l + R_y(Delta)`, where the remainder is `o(||Delta||)`. However, it derives a **decomposition**, not an explicit **upper bound** on the magnitude. No closed-form bound on |Delta beta| is given.

**B. Bounds on feature learning stability (scaling behavior):**

- **"Stable-LoRA: Stabilizing Feature Learning of Low-Rank Adaptation" (arXiv 2603.05204, March 2025):** Defines LoRA feature learning as "stable" if `Delta Y_t = Theta(1)` for all training steps t (i.e., output updates neither explode nor vanish with width n). Theorem 3.1 gives conditions on hyperparameters (s, eta) and initializations (A_0, B_0) under which LoRA is self-stable. This bounds scaling behavior with respect to width, not the absolute magnitude of representation change under a given rank-r perturbation.

**C. Bounds on expressive power and approximation error:**

- **"The Expressive Power of Low-Rank Adaptation" (ICLR 2024, arXiv 2310.17513):** Bounds the approximation error `E||f(x) - target(x)||^2` as a function of LoRA rank via singular value decay. Shows LoRA is nearly optimally expressive up to a constant factor of 2. Does not bound intermediate representation changes.

**D. Convergence and optimization landscape bounds:**

- **"On the Convergence Rate of LoRA Gradient Descent" (arXiv 2512.18248):** Shows O(1/sqrt(T)) convergence. Notes the Lipschitz non-smoothness of the LoRA reparameterization and develops a modified descent lemma.
- **"LoRA Training Provably Converges to a Low-Rank Global Minimum" (arXiv 2502.09376):** Shows that spurious stationary points must have high rank and large magnitude, so they are detectable. Does not bound representation changes.

**E. Noise robustness through rank constraints:**

- **"Why LoRA Resists Label Noise" (arXiv 2602.00084):** Provides a memorization capacity bound (Theorem 3.3) showing rank-r LoRA cannot memorize all label assignments beyond O(r(d+k-r)) samples. Bounds are on fitting capacity, not on representation geometry.

**F. Representation similarity (empirical, CKA-based):**

- **"Layer-wise LoRA Fine-tuning: A Similarity Metric Approach" (arXiv 2602.05988):** Uses CKA to measure representational similarity between base and LoRA-adapted models to guide layer selection. Purely empirical -- no formal bounds on CKA change under LoRA.

- **"LoRA vs Full Fine-tuning: An Illusion of Equivalence" (arXiv 2410.21228):** Shows LoRA introduces "intruder dimensions" -- new high-ranking singular vectors absent in full fine-tuning. These cause localized forgetting. Empirical spectral analysis, no formal bounds.

### 3. On Density Ratio Estimation in High-Dimensional Latent Spaces

This is an established field with mature methods (telescoping DRE, noise contrastive estimation, featurized DRE). The challenge of density ratio estimation in high-dimensional spaces is well-documented, with solutions involving latent-space projections and generative models. Combining density ratio estimation with LoRA-induced latent space changes appears to be an **unexplored intersection**.

### 4. Assessment: Is the "LoRA Stability Theorem" (Bounding |Delta beta| Under Low-Rank Perturbations) Novel?

**Yes, it would be novel.** Here is why:

**What exists:**
- Logit shift decomposition (first-order, no magnitude bound) -- arXiv 2604.20313
- Width-scaling stability conditions (Theta(1) output updates) -- arXiv 2603.05204
- Approximation error bounds as function of rank (model-to-model, not representation-level) -- ICLR 2024
- Convergence rate bounds -- arXiv 2512.18248
- Memorization capacity bounds -- arXiv 2602.00084

**What does NOT exist (gap your theorem would fill):**
- An explicit upper bound of the form `|Delta beta| <= f(r, sigma_i, ...)` that bounds the change in downstream regression/classification coefficients (or equivalently, representation-level feature changes) as a function of LoRA rank, singular values of the perturbation matrices, and properties of the pre-trained network (e.g., Lipschitz constants of downstream layers).
- A Lipschitz-type bound connecting `||BA||` to `||phi_LoRA(x) - phi_base(x)||` across the representation space.

### 5. Feasibility Assessment

**Feasible, with caveats:**

**In favor:**
- The Frechet decomposition from arXiv 2604.20313 provides the scaffolding: `delta(x) = (alpha/r) * J * BA * z + o(||Delta||)`. Converting this to a bound requires bounding `||J||` (Jacobian of downstream layers) and `||z||` (intermediate activations), both of which are standard in perturbation theory.
- Stable-LoRA's analysis (arXiv 2603.05204) shows that LoRA updates can be controlled via hyperparameter/initialization conditions, suggesting the perturbation is structurally well-behaved.
- Standard matrix perturbation results (Weyl's inequality, Davis-Kahan) apply to `W + (alpha/r)BA` and give spectral bounds.

**Challenges:**
- The Lipschitz non-smoothness of the LoRA reparameterization (noted in arXiv 2512.18248) means naive application of standard smooth perturbation theory will not work. You need the modified Lipschitz-like condition they develop.
- Bounding the Jacobian `J_{l+1->L}` for deep networks is nontrivial -- it involves products of weight matrices and activation derivatives. Without assumptions (e.g., bounded activations, spectral norm constraints), bounds can be vacuous.
- Moving from logit-level bounds to feature-level bounds (|Delta beta| for a linear probe on representations) requires additional structure -- specifically, how the linear probe interacts with the perturbation subspace.

### 6. Would It Be a Genuine Contribution?

**Yes.** A clean theorem of the form:

> If the pre-trained model has layer Jacobians bounded in spectral norm by L, and LoRA adapters satisfy `||B_l A_l||_2 <= epsilon`, then for any linear functional beta of the representation, `|Delta beta| <= C * (alpha/r) * L * epsilon * ||z||`

...would be the first result to directly bound downstream coefficient changes under LoRA perturbations. It would unify and extend:
- The decomposition from the logit shift paper (adding magnitude bounds)
- The stability conditions from Stable-LoRA (making them quantitative at the representation level)
- The expressive power results (complementing "what LoRA can do" with "how much LoRA changes things")

The practical value would be in providing theoretically grounded guidance for rank selection, scaling factor choice, and continual learning stability guarantees.

### Sources

- [LoRA Subtraction for Drift-Resistant Space (arXiv 2503.18985)](https://arxiv.org/abs/2503.18985)
- [Formalising the Logit Shift Induced by LoRA (arXiv 2604.20313)](https://arxiv.org/html/2604.20313)
- [Stable-LoRA: Stabilizing Feature Learning (arXiv 2603.05204)](https://arxiv.org/abs/2603.05204)
- [The Expressive Power of Low-Rank Adaptation (ICLR 2024)](https://arxiv.org/html/2310.17513v3)
- [On the Convergence Rate of LoRA Gradient Descent (arXiv 2512.18248)](https://arxiv.org/pdf/2512.18248)
- [Why LoRA Resists Label Noise (arXiv 2602.00084)](https://arxiv.org/html/2602.00084)
- [LoRA vs Full Fine-tuning: An Illusion of Equivalence (arXiv 2410.21228)](https://arxiv.org/abs/2410.21228)
- [LoRA Training Provably Converges (arXiv 2502.09376)](https://arxiv.org/html/2502.09376v3)
- [Layer-wise LoRA with CKA (arXiv 2602.05988)](https://arxiv.org/pdf/2602.05988)
- [Latent Space Factorization in LoRA (arXiv 2510.19640)](https://arxiv.org/abs/2510.19640)
- [Density Estimation Using Deep Generative Neural Networks (PNAS)](https://www.pnas.org/doi/10.1073/pnas.2101344118)
- [Telescoping Density-Ratio Estimation (NeurIPS 2020)](https://proceedings.neurips.cc/paper/2020/file/33d3b157ddc0896addfb22fa2a519097-Paper.pdf)
- [Computational Limits of LoRA (arXiv 2406.03136)](https://arxiv.org/abs/2406.03136)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e613d75-7db5-421d-b472-045a919a9624",
  "isSidechain": true,
  "agentId": "ad487675142d937dd",
  "requestId": "req_011Cb19GLNAuTz6NwkTKX9Jd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27d7d882-9bab-4fc9-8f18-e780ada8da1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d420c8fc-73ad-49e5-a076-6b52b56c836b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LbPjMoUMJfvNVdWtpe5Cx6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 912,
      "cache_creation_input_tokens": 1197,
      "cache_read_input_tokens": 27402,
      "output_tokens": 2726,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1197
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 912,
          "output_tokens": 2726,
          "cache_read_input_tokens": 27402,
          "cache_creation_input_tokens": 1197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1197,
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
