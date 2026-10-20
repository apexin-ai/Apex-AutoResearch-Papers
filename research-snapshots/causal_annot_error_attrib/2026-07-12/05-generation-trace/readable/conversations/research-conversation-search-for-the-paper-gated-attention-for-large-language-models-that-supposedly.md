# Research conversation: Search for the paper "Gated Attention for Large Language Models" that supposedly won NeurIPS 2025 Best Paper. The claime

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ac03be8f131e42260.jsonl`
- **Structured JSON:** [`c9bcfb75ac9ca947a05c.json`](../../sessions/c9/c9bcfb75ac9ca947a05c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-17T08:58:53.582Z_

Search for the paper "Gated Attention for Large Language Models" that supposedly won NeurIPS 2025 Best Paper. The claimed arXiv ID is 2505.06708 and OpenReview ID is 1b7whO4SfY. I need to verify:
1. Does this paper actually exist?
2. Did it win NeurIPS 2025 Best Paper?
3. Does it implement query-conditional per-head sigmoid gating as described?
4. Was it pre-trained from scratch on 3.5T tokens?
5. Is it deployed only in Qwen3-Next models?

Use WebSearch to find information about this paper. Try queries like:
- "Gated Attention Large Language Models NeurIPS 2025 Best Paper"
- "arXiv 2505.06708"
- "Qwen3-Next Gated Attention"
- site:openreview.net "Gated Attention"

Then use WebFetch to read the arXiv abstract if possible. Report all findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "ac03be8f131e42260",
  "type": "user",
  "uuid": "808f30de-fe75-4494-ac3d-5cb7a4791758",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-17T08:58:53.586Z_

```json
{
  "parentUuid": "808f30de-fe75-4494-ac3d-5cb7a4791758",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
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
  "uuid": "dc28e399-fa08-4c9c-b8b6-d092632d3bd8",
  "timestamp": "2026-05-17T08:58:53.586Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-17T08:58:56.166Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VFfWmBe2NKdBU1NdFFSNH4`</summary>

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
  "parentUuid": "dc28e399-fa08-4c9c-b8b6-d092632d3bd8",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sA8gwnNQw3sfWV95ee",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bc5cd5c-a9a9-4406-bec6-6de7ec866892",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdNUyHPhAzu6j1jxBmrKWg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 795,
      "cache_read_input_tokens": 8223,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 795
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 795,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 795,
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

_source line 4 · 2026-05-17T08:58:56.171Z_

<details><summary>↩ Tool result · `toolu_01VFfWmBe2NKdBU1NdFFSNH4`</summary>

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
  "parentUuid": "3bc5cd5c-a9a9-4406-bec6-6de7ec866892",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "ac03be8f131e42260",
  "type": "user",
  "uuid": "66201c58-8e97-4051-a8fc-a67e72240f81",
  "sourceToolAssistantUUID": "3bc5cd5c-a9a9-4406-bec6-6de7ec866892",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-17T08:58:59.244Z_

Now let me search for this paper using multiple queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66201c58-8e97-4051-a8fc-a67e72240f81",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sALGDCYbAwybMHqQzD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0481c417-5b7b-437f-aaff-35843df8b4e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZTmnyTVxmVDzD3qM657rf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 6 · 2026-05-17T08:58:59.267Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UapvL499nzufc2NtjC6djS`</summary>

```json
{
  "query": "Gated Attention Large Language Models NeurIPS 2025 Best Paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0481c417-5b7b-437f-aaff-35843df8b4e6",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sALGDCYbAwybMHqQzD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24a5722a-7536-4641-9cba-8026d54c4c0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZTmnyTVxmVDzD3qM657rf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 7 · 2026-05-17T08:58:59.690Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y7dwjDD3TjHnrZ8wuZUgQJ`</summary>

```json
{
  "query": "arXiv 2505.06708"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24a5722a-7536-4641-9cba-8026d54c4c0b",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sALGDCYbAwybMHqQzD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb1e6010-3124-452d-b6e2-324d850d0739",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZTmnyTVxmVDzD3qM657rf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 8 · 2026-05-17T08:59:00.228Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sn4Za7m8ioBwHqrgRoh4js`</summary>

```json
{
  "query": "Qwen3-Next Gated Attention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb1e6010-3124-452d-b6e2-324d850d0739",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sALGDCYbAwybMHqQzD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e91a17ac-0f37-40de-9f01-085d51e53655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZTmnyTVxmVDzD3qM657rf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
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

_source line 9 · 2026-05-17T08:59:00.474Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DUQPjZK719z1pxiZTwsKVu`</summary>

```json
{
  "query": "site:openreview.net \"Gated Attention\" NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e91a17ac-0f37-40de-9f01-085d51e53655",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sALGDCYbAwybMHqQzD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f17f1a9-7a8b-4845-8af0-7536c827b831",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZTmnyTVxmVDzD3qM657rf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9018,
      "output_tokens": 224,
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
          "output_tokens": 224,
          "cache_read_input_tokens": 9018,
          "cache_creation_input_tokens": 1888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1888,
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

_source line 10 · 2026-05-17T08:59:05.417Z_

<details><summary>↩ Tool result · `toolu_01UapvL499nzufc2NtjC6djS`</summary>

```text
Web search results for query: "Gated Attention Large Language Models NeurIPS 2025 Best Paper"

Links: [{"title":"Announcing the NeurIPS 2025 Best Paper Awards – NeurIPS Blog","url":"https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/"},{"title":"NeurIPS Poster Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://neurips.cc/virtual/2025/poster/120216"},{"title":"GitHub - qiuzh20/gated_attention: The official implementation for [NeurIPS2025 Oral] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free · GitHub","url":"https://github.com/qiuzh20/gated_attention"},{"title":"NeurIPS 2025 Best Paper Review: Qwen’s Systematic Exploration of Attention Gating | Towards Data Science","url":"https://towardsdatascience.com/neurips-2025-best-paper-review-qwens-systematic-exploration-of-attention-gating/"},{"title":"NeurIPS 2025 Best Papers TL;DR part 1: Gated Attention","url":"https://virtuslab.com/blog/ai/neur-ips-2025-papers-part-1"},{"title":"[NeurIPS 2025] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://arxiviq.substack.com/p/neurips-2025-gated-attention-for"},{"title":"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free | OpenReview","url":"https://openreview.net/forum?id=1b7whO4SfY"},{"title":"Alibaba Qwen Wins “NeurIPS 2025 Best Paper Award” for Breakthrough in Attention Mechanisms - Alibaba Cloud Community","url":"https://www.alibabacloud.com/blog/alibaba-qwen-wins-%E2%80%9Cneurips-2025-best-paper-award%E2%80%9D-for-breakthrough-in-attention-mechanisms_602708"},{"title":"Alibaba Qwen Wins “NeurIPS 2025 Best Paper Award” for Breakthrough in Attention Mechanisms | Alizila","url":"https://www.alizila.com/alibaba-qwen-wins-neurips-2025-best-paper-award-for-breakthrough-in-attention-mechanisms/"},{"title":"Gated Attention ~ NeurIPS 2025 Best Paper","url":"https://www.byhand.ai/p/gated-attention-neurips-2025-best"}]

Based on the search results, here's what I found about "Gated Attention for Large Language Models" as a NeurIPS 2025 Best Paper:

## Award Recognition

The paper "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free" has been awarded the NeurIPS 2025 Best Paper Award, recognizing only 4 papers out of 5,290 accepted submissions.

## Paper Overview

The paper is the first in the industry to systematically examine how attention gating affects the performance and training of large models. The central finding is that a simple modification—applying a head-specific sigmoid gate after the Scaled Dot-Product Attention (SDPA)—consistently improves performance, while also enhancing training stability, tolerating larger learning rates, and improving scaling properties.

## Key Findings

The findings are backed up by more than thirty experiments on different variants of gated softmax attention using 15B MoE and 1.7B dense models trained on large-scale datasets of 400B, 1T, or 3.5T tokens.

The introduction of gating improves the training stability of large language models, reduces the "attention sink" phenomenon that has been widely reported in attention models, and enhances the performance of context length extension.

## Practical Impact

These findings have already been incorporated into the Qwen3-Next model released in September 2025, which introduced architectural innovations by replacing standard attention with a combination of Gated DeltaNet and Gated Attention, improving in-context learning capabilities while increasing computational efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24a5722a-7536-4641-9cba-8026d54c4c0b",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "ac03be8f131e42260",
  "type": "user",
  "uuid": "5a675a3b-cb98-442f-ae30-fefd21002143",
  "sourceToolAssistantUUID": "24a5722a-7536-4641-9cba-8026d54c4c0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T08:59:06.743Z_

<details><summary>↩ Tool result · `toolu_01Y7dwjDD3TjHnrZ8wuZUgQJ`</summary>

```text
Web search results for query: "arXiv 2505.06708"

Links: [{"title":"[2505.06708] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://arxiv.org/abs/2505.06708"},{"title":"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2505.06708"},{"title":"[PDF] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free | Semantic Scholar","url":"https://www.semanticscholar.org/paper/a295e71055248f4145257ed88f25503a75a78406"},{"title":"[2505.06708] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://ar5iv.labs.arxiv.org/html/2505.06708"},{"title":"GitHub - qiuzh20/gated_attention: The official implementation for [NeurIPS2025 Oral] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free · GitHub","url":"https://github.com/qiuzh20/gated_attention"},{"title":"Kaiyue Wen","url":"https://scholar.google.com/citations?user=oTmQCFUAAAAJ&hl=en"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=2950&show=250"},{"title":"arXiv:2505.06708v1 [cs.CL] 10 May 2025 2025-06-11","url":"https://arxiv.org/pdf/2505.06708"},{"title":"Why do LLMs attend to the first token? | OpenReview","url":"https://openreview.net/forum?id=tu4dFUsW5z"},{"title":"Revisiting Long-context Modeling from Context Denoising Perspective","url":"https://arxiv.org/html/2510.05862v2"}]

Based on the search results, here's information about arXiv paper 2505.06708:

## Title
Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free

## Authors
Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin

## Publication Date
The paper was published on May 10, 2025

## Summary
While gating mechanisms have been widely utilized from early models like LSTMs and Highway Networks to recent state space models and softmax attention, existing literature rarely examines the specific effects of gating. The authors conduct comprehensive experiments to systematically investigate gating-augmented softmax attention variants.

## Key Findings
The researchers performed a comprehensive comparison over 30 variants of 15B Mixture-of-Experts (MoE) models and 1.7B dense models trained on a 3.5 trillion token dataset. Their central finding is that a simple modification—applying a head-specific sigmoid gate after the Scaled Dot-Product Attention (SDPA)—consistently improves performance.

This modification also enhances training stability, tolerates larger learning rates, and improves scaling properties.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb1e6010-3124-452d-b6e2-324d850d0739",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "ac03be8f131e42260",
  "type": "user",
  "uuid": "d5e665c5-aa4c-49fa-984b-349fddb4939d",
  "sourceToolAssistantUUID": "fb1e6010-3124-452d-b6e2-324d850d0739",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T08:59:06.985Z_

<details><summary>↩ Tool result · `toolu_01Sn4Za7m8ioBwHqrgRoh4js`</summary>

```text
Web search results for query: "Qwen3-Next Gated Attention"

Links: [{"title":"Qwen/Qwen3-Next-80B-A3B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct"},{"title":"Qwen3-Next: Next-Generation Ultra-Efficient AI Model Architecture","url":"https://qwen3-next.com/"},{"title":"Qwen3.5: Nobody Agrees on Attention Anymore","url":"https://huggingface.co/blog/mlabonne/qwen35"},{"title":"GitHub - qiuzh20/gated_attention: The official implementation for [NeurIPS2025 Oral] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free · GitHub","url":"https://github.com/qiuzh20/gated_attention"},{"title":"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free | OpenReview","url":"https://openreview.net/forum?id=1b7whO4SfY"},{"title":"Qwen/Qwen3-Next-80B-A3B-Thinking-FP8 · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Thinking-FP8"},{"title":"Qwen/Qwen3-Next-80B-A3B-Thinking · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Thinking"},{"title":"Gated DeltaNet for Linear Attention - rasbt/LLMs-from-scratch","url":"https://github.com/rasbt/LLMs-from-scratch/blob/main/ch04/08_deltanet/README.md"},{"title":"qwen3-next","url":"https://ollama.com/library/qwen3-next"},{"title":"unsloth/Qwen3-Next-80B-A3B-Thinking-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Qwen3-Next-80B-A3B-Thinking-GGUF"}]

Based on the search results, here's what I found about Qwen3-Next Gated Attention:

## Overview

Qwen3-Next uses a hybrid attention mechanism that combines Gated DeltaNet and Gated Attention, enabling efficient context modeling for ultra-long context length.

## Implementation Details

Qwen3-Next uses a 3:1 hybrid attention layout in which most layers use Gated DeltaNet (linear attention) and the remaining layers use Gated Attention (full/softmax-style attention).

Gated Attention is essentially regular full attention with an additional sigmoid gate.

## How It Works

A simple modification—applying a head-specific sigmoid gate after the Scaled Dot-Product Attention (SDPA)—consistently improves performance. The effectiveness comes from introducing non-linearity upon the low-rank mapping in the softmax attention, and applying query-dependent sparse gating scores to modulate the SDPA output.

## Benefits

This sparse gating mechanism mitigates "massive activation" and "attention sink" and enhances long-context extrapolation performance. Additionally, this modification enhances training stability, tolerates larger learning rates, and improves scaling properties.

## Research Recognition

The paper on Gated Attention for Large Language Models has been awarded the NeurIPS 2025 Best Paper Award. Gated Attention has been successfully integrated into the official Qwen3-Next architecture and deployed in the Qwen3-Next-80B-A3B-Instruct model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e91a17ac-0f37-40de-9f01-085d51e53655",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "ac03be8f131e42260",
  "type": "user",
  "uuid": "7a867f56-4010-428e-bfbc-1e8dbe302fb9",
  "sourceToolAssistantUUID": "e91a17ac-0f37-40de-9f01-085d51e53655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T08:59:11.087Z_

<details><summary>↩ Tool result · `toolu_01DUQPjZK719z1pxiZTwsKVu`</summary>

```text
Web search results for query: "site:openreview.net "Gated Attention" NeurIPS 2025"

Links: [{"title":"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free | OpenReview","url":"https://openreview.net/forum?id=1b7whO4SfY"},{"title":"Gated Attention for Large Language Models: Non-linearity, ...","url":"https://openreview.net/pdf?id=1b7whO4SfY"}]

I found the paper you're looking for on OpenReview! Here are the results:

**Paper Title:** "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free"

**Key Details:**
- **Status:** Published at NeurIPS 2025 as an oral presentation on September 18, 2025
- **OpenReview Links:** 
  - Forum: https://openreview.net/forum?id=1b7whO4SfY
  - PDF: https://openreview.net/pdf?id=1b7whO4SfY

**Main Contribution:** The paper proposes applying a query-dependent head-specific sigmoid gate after Scaled Dot-Product Attention, which consistently improves performance, improves scaling properties, and mitigates "massive activation" and "attention sink".

**Methodology:** The authors performed a comprehensive comparison over 30 variants of 15B Mixture-of-Experts (MoE) models and 1.7B dense models trained on a 3.5 trillion token dataset.

**Additional Resources:** The authors released related codes on GitHub and models on Hugging Face to facilitate future research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f17f1a9-7a8b-4845-8af0-7536c827b831",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "ac03be8f131e42260",
  "type": "user",
  "uuid": "6cf38eda-f60e-4947-a808-ddcd92389c45",
  "sourceToolAssistantUUID": "1f17f1a9-7a8b-4845-8af0-7536c827b831",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-17T08:59:15.866Z_

Now let me fetch the arXiv abstract for more details, and check the NeurIPS blog for the official best paper list.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cf38eda-f60e-4947-a808-ddcd92389c45",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sBRZjFg9XePzhJ6BLX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68f763ab-2317-43a6-b941-a4386833153f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RsRjbnVHMo42B4f1tz8hR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3743,
      "cache_read_input_tokens": 10906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3743,
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

_source line 15 · 2026-05-17T08:59:17.763Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MfqusHpzy377AaPBuPKCmp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.06708",
  "prompt": "Extract the full title, authors, abstract, and any other metadata about this paper. I need to verify if it mentions query-conditional per-head sigmoid gating, pre-training from scratch on 3.5T tokens, and any connection to Qwen3-Next models."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68f763ab-2317-43a6-b941-a4386833153f",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sBRZjFg9XePzhJ6BLX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8cc82749-5277-49d8-b0b8-3b0d1ff75cca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RsRjbnVHMo42B4f1tz8hR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3743,
      "cache_read_input_tokens": 10906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3743,
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

_source line 16 · 2026-05-17T08:59:18.866Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X5YXQs64aDvZffxYrdcyMZ`</summary>

```json
{
  "url": "https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/",
  "prompt": "List ALL best paper award winners at NeurIPS 2025. I need to verify if \"Gated Attention for Large Language Models\" won the Best Paper Award."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cc82749-5277-49d8-b0b8-3b0d1ff75cca",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sBRZjFg9XePzhJ6BLX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdd80f5d-361e-4998-82b6-e13108ac2053",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012RsRjbnVHMo42B4f1tz8hR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3743,
      "cache_read_input_tokens": 10906,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3743
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 10906,
          "cache_creation_input_tokens": 3743,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3743,
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

_source line 17 · 2026-05-17T08:59:22.971Z_

<details><summary>↩ Tool result · `toolu_01MfqusHpzy377AaPBuPKCmp`</summary>

```text
# Paper Metadata Extraction

**Full Title:**
"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free"

**Authors:**
Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin

**Key Abstract Points:**
The paper's central contribution involves "a simple modification-applying a head-specific sigmoid gate after the Scaled Dot-Product Attention (SDPA)." This directly confirms the query-conditional per-head sigmoid gating mechanism you asked about.

Regarding the 3.5 trillion token dataset, the abstract states the research involved models "trained on a 3.5 trillion token dataset," though it doesn't explicitly state whether this was pre-training from scratch versus continued training.

**Metadata:**
- Submitted: May 10, 2025
- arXiv ID: 2505.06708
- Category: Computation and Language (cs.CL)
- DOI: https://doi.org/10.48550/arXiv.2505.06708

**Notable Finding:**
No mention of "Qwen3-Next" or any specific model variant names appears in the provided excerpt. The paper references released codes and models on GitHub and Hugging Face but doesn't identify them by that designation in the abstract or metadata shown.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8cc82749-5277-49d8-b0b8-3b0d1ff75cca",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "ac03be8f131e42260",
  "type": "user",
  "uuid": "dc5531a9-dad3-43cb-a6cd-dba6919386ba",
  "sourceToolAssistantUUID": "8cc82749-5277-49d8-b0b8-3b0d1ff75cca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T08:59:23.930Z_

<details><summary>↩ Tool result · `toolu_01X5YXQs64aDvZffxYrdcyMZ`</summary>

```text
# NeurIPS 2025 Best Paper Award Winners

Based on the announcement, there are **four Best Papers** (one from Datasets & Benchmarks track):

1. **Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)** - Jiang et al.

2. **Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free** - Qiu et al.

3. **1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities** - Wang et al.

4. **Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training** - Bonnaire et al.

## Verification Result

**Yes, "Gated Attention for Large Language Models" won a Best Paper Award.** The document confirms it is among "four best papers" awarded at NeurIPS 2025. The committee noted that this work provides "substantial amount of work" demonstrating improvements in LLM performance through a simple architectural modification, with findings expected to be "widely adopted."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdd80f5d-361e-4998-82b6-e13108ac2053",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "ac03be8f131e42260",
  "type": "user",
  "uuid": "5bbcc224-4770-4ed8-9a6f-d556384f8481",
  "sourceToolAssistantUUID": "bdd80f5d-361e-4998-82b6-e13108ac2053",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-17T08:59:26.622Z_

Now let me get more detail on whether the models were pre-trained from scratch, and whether the deployment is exclusive to Qwen3-Next.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bbcc224-4770-4ed8-9a6f-d556384f8481",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sCNQkexBZGDgjjrfdu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "754a2702-4a19-473f-90c1-99a358e16dc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kf6ehPoEQgj84FffxDJqca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 974,
      "cache_read_input_tokens": 14649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 974,
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

_source line 20 · 2026-05-17T08:59:30.791Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RnYTZK5oaVKcAjHezdb9EF`</summary>

```json
{
  "url": "https://openreview.net/forum?id=1b7whO4SfY",
  "prompt": "Extract any information about: 1) Whether models were pre-trained from scratch on 3.5T tokens or if this was continued training. 2) Whether the gating is described as \"query-conditional per-head sigmoid gating\". 3) Any mention of Qwen3-Next or deployment details. 4) The paper's award status (Best Paper, Oral, etc). 5) Any reviewer scores or comments."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "754a2702-4a19-473f-90c1-99a358e16dc2",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sCNQkexBZGDgjjrfdu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07327400-5faa-4d27-b6ab-02b08b14a1fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kf6ehPoEQgj84FffxDJqca",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 974,
      "cache_read_input_tokens": 14649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 974,
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

_source line 21 · 2026-05-17T08:59:30.980Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Sqib8TMYJ85s53z9wA2s2y`</summary>

```json
{
  "url": "https://github.com/qiuzh20/gated_attention",
  "prompt": "Extract information about: 1) Whether models were pre-trained from scratch. 2) The training data size (3.5T tokens). 3) Any mention of Qwen3-Next deployment. 4) The exact gating mechanism described. 5) Any model checkpoints or references to specific deployed models."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07327400-5faa-4d27-b6ab-02b08b14a1fc",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sCNQkexBZGDgjjrfdu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb0411d1-491a-43b7-901c-0ea3422296d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kf6ehPoEQgj84FffxDJqca",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 974,
      "cache_read_input_tokens": 14649,
      "output_tokens": 347,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 974
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 347,
          "cache_read_input_tokens": 14649,
          "cache_creation_input_tokens": 974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 974,
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

_source line 22 · 2026-05-17T08:59:35.827Z_

<details><summary>↩ Tool result · `toolu_01RnYTZK5oaVKcAjHezdb9EF`</summary>

```text
# Information Extraction Summary

**1) Pre-training vs. Continued Training:**
Not specified in the content. The page mentions models were "trained on a 3.5 trillion token dataset" but does not clarify whether this was from-scratch pre-training or continued training.

**2) Gating Description:**
The paper describes it as "a head-specific sigmoid gate" applied after SDPA. The exact wording is: "applying a query-dependent head-specific sigmoid gate after the Scaled Dot-Product Attention." This matches "query-conditional per-head sigmoid gating" conceptually, though the document uses "query-dependent" rather than "query-conditional."

**3) Qwen3-Next and Deployment:**
Yes, mentioned: "the most effective SDPA output gating is used in the Qwen3-Next models" with a link to the Hugging Face collection. Code and models are also released on GitHub and Hugging Face.

**4) Paper Award Status:**
Designated as "NeurIPS 2025 oral"—indicating oral presentation acceptance, but no "Best Paper" or similar distinction is mentioned.

**5) Reviewer Scores or Comments:**
No reviewer scores, comments, or detailed review information are included in this webpage content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07327400-5faa-4d27-b6ab-02b08b14a1fc",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "ac03be8f131e42260",
  "type": "user",
  "uuid": "a868c9fb-1ae5-4a2b-a6cb-0251a29f49c7",
  "sourceToolAssistantUUID": "07327400-5faa-4d27-b6ab-02b08b14a1fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-17T08:59:36.244Z_

<details><summary>↩ Tool result · `toolu_01Sqib8TMYJ85s53z9wA2s2y`</summary>

```text
# Gated Attention Repository Analysis

## 1) Pre-training from Scratch
The document does not specify whether models were pre-trained from scratch. It references using "Qwen3" model architecture as the foundation but provides no details about training initialization.

## 2) Training Data Size
No mention of training data size (3.5T tokens or otherwise) appears in this repository documentation.

## 3) Qwen3-Next Deployment
Yes, there is a specific mention: "Gated Attention has been successfully integrated into the official Qwen3-Next architecture" and is "deployed in the Qwen3-Next-80B-A3B-Instruct model" available on Hugging Face.

## 4) Exact Gating Mechanism
The mechanism is described as: "a query-dependent sparse gate after the SDPA output (G1), which modulates each attention head independently using a sigmoid function." Two variants are provided:
- **Headwise gating**: "Each attention head has its own gate scalar"
- **Elementwise gating**: "Each element of the attention output is modulated independently"

## 5) Model Checkpoints
Models are available at "huggingface repo" (QwQZh/gated_attention) with three variants: `baseline`, `gate_headwise`, and `gate_elementwise`. The Qwen3-Next-80B-A3B-Instruct model represents the primary deployed checkpoint.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb0411d1-491a-43b7-901c-0ea3422296d4",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "ac03be8f131e42260",
  "type": "user",
  "uuid": "425ac095-1ba7-4d9b-a215-21b49115f547",
  "sourceToolAssistantUUID": "bb0411d1-491a-43b7-901c-0ea3422296d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-17T08:59:57.706Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R36KbbNUGicob4hGFUM2fz`</summary>

```json
{
  "query": "\"Gated Attention\" \"pre-trained from scratch\" OR \"trained from scratch\" \"3.5T\" OR \"3.5 trillion\" Qwen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "425ac095-1ba7-4d9b-a215-21b49115f547",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sDH9XBSMxSfY64JjEH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbee9e99-f0ed-4153-8ecd-1df0a9444bc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UM4x3fe8cRNWA433S6EGH6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1128,
      "cache_read_input_tokens": 15623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1128,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

_source line 25 · 2026-05-17T08:59:57.872Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y3urfKrK2eCZopijvV6aVo`</summary>

```json
{
  "query": "Qwen3-Next architecture \"gated attention\" deployed models list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbee9e99-f0ed-4153-8ecd-1df0a9444bc3",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sDH9XBSMxSfY64JjEH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7ceb72a-dbb3-4c59-b443-bd55c79596d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UM4x3fe8cRNWA433S6EGH6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1128,
      "cache_read_input_tokens": 15623,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1128
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 15623,
          "cache_creation_input_tokens": 1128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1128,
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

_source line 26 · 2026-05-17T09:00:04.254Z_

<details><summary>↩ Tool result · `toolu_01Y3urfKrK2eCZopijvV6aVo`</summary>

```text
Web search results for query: "Qwen3-Next architecture "gated attention" deployed models list"

Links: [{"title":"New Open Source Qwen3-Next Models Preview Hybrid MoE Architecture Delivering Improved Accuracy and Accelerated Parallel Processing across NVIDIA Platform | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/new-open-source-qwen3-next-models-preview-hybrid-moe-architecture-delivering-improved-accuracy-and-accelerated-parallel-processing-across-nvidia-platform/"},{"title":"Qwen/Qwen3-Next-80B-A3B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct"},{"title":"GitHub - qiuzh20/gated_attention: The official implementation for [NeurIPS2025 Oral] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free · GitHub","url":"https://github.com/qiuzh20/gated_attention"},{"title":"Qwen3-Next: Next-Generation Ultra-Efficient AI Model Architecture","url":"https://qwen3-next.com/"},{"title":"Qwen3-Next: Revolutionary 80B Model with Only 3B Active Parameters - Ultimate Efficiency Guide | Colin McNamara","url":"https://www.colinmcnamara.com/blog/qwen3-next-ultimate-training-inference-efficiency-guide"},{"title":"Qwen/Qwen3-Next-80B-A3B-Thinking · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Thinking"},{"title":"Qwen3-Next: A New Generation of Ultra-Efficient Model Architecture Unveiled - Alibaba Cloud Community","url":"https://www.alibabacloud.com/blog/qwen3-next-a-new-generation-of-ultra-efficient-model-architecture-unveiled_602536"},{"title":"Qwen3-Coder-Next: Architecture, Benchmarks, Capabilities, and Real-World Applications - Qubrid AI","url":"https://www.qubrid.com/blog/qwen3-coder-next-architecture-benchmarks-capabilities-and-real-world-applications"},{"title":"qwen3-next","url":"https://lmstudio.ai/models/qwen3-next"},{"title":"Qwen3 Next • LM Studio","url":"https://lmstudio.ai/models/qwen/qwen3-next-80b"}]

Based on the search results, here's what I found about Qwen3-Next architecture with gated attention and the deployed models list:

## Architecture Overview

Qwen3-Next-80B-A3B features hybrid attention that replaces standard attention with the combination of Gated DeltaNet and Gated Attention. The innovation marks a significant advancement including linear attention and attention gate, as well as increased sparsity in its MoE design.

More specifically, the model's 48 layers are arranged in a repeating pattern every four layers, three use Gated DeltaNet attention followed by one that uses standard Gated Attention, each paired with a MoE block.

## Deployed Models List

The primary deployed models featuring this architecture are:

1. Qwen3-Next 80B-A3B-Thinking and Qwen3-Next 80B-A3B-Instruct
2. **Qwen3-Coder-Next** - built on the same hybrid architecture that combines two types of attention mechanisms inside a Mixture-of-Experts transformer

## Deployment Options

The models can be deployed using NVIDIA NIM, SGLang, and vLLM, and are available for testing on build.NVIDIA.com and for download on Hugging Face. Additionally, enterprise developers can try Qwen3-Next-80B-A3B through NVIDIA-hosted NIM microservice endpoints in the NVIDIA API catalog.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7ceb72a-dbb3-4c59-b443-bd55c79596d1",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "ac03be8f131e42260",
  "type": "user",
  "uuid": "a6eb8cdf-f484-4b5d-91f8-f7f73f22a01c",
  "sourceToolAssistantUUID": "d7ceb72a-dbb3-4c59-b443-bd55c79596d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-17T09:00:05.548Z_

<details><summary>↩ Tool result · `toolu_01R36KbbNUGicob4hGFUM2fz`</summary>

```text
Web search results for query: ""Gated Attention" "pre-trained from scratch" OR "trained from scratch" "3.5T" OR "3.5 trillion" Qwen"

Links: [{"title":"[NeurIPS 2025] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://arxiviq.substack.com/p/neurips-2025-gated-attention-for"},{"title":"Qwen3.5: Nobody Agrees on Attention Anymore","url":"https://huggingface.co/blog/mlabonne/qwen35"},{"title":"Gated Attention: Solving the Hidden Bottlenecks in Transformer Attention | by Mandeep Singh | Medium","url":"https://medium.com/@mandeep0405/gated-attention-solving-the-hidden-bottlenecks-in-transformer-attention-685867a24779"},{"title":"Alibaba Qwen Wins “NeurIPS 2025 Best Paper Award” for Breakthrough in Attention Mechanisms - Alibaba Cloud Community","url":"https://www.alibabacloud.com/blog/alibaba-qwen-wins-%E2%80%9Cneurips-2025-best-paper-award%E2%80%9D-for-breakthrough-in-attention-mechanisms_602708"},{"title":"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free | OpenReview","url":"https://openreview.net/forum?id=1b7whO4SfY"},{"title":"Gated Attention for Large Language Models: Non-linearity, ...","url":"https://openreview.net/pdf?id=1b7whO4SfY"},{"title":"Alibaba's Qwen 3.5 397B-A17 beats its larger trillion-parameter model — at a fraction of the cost | VentureBeat","url":"https://venturebeat.com/technology/alibabas-qwen-3-5-397b-a17-beats-its-larger-trillion-parameter-model-at-a"},{"title":"GitHub - qiuzh20/gated_attention: The official implementation for [NeurIPS2025 Oral] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free · GitHub","url":"https://github.com/qiuzh20/gated_attention"},{"title":"NeurIPS 2025 Best Paper Review: Qwen’s Systematic Exploration of Attention Gating | Towards Data Science","url":"https://towardsdatascience.com/neurips-2025-best-paper-review-qwens-systematic-exploration-of-attention-gating/"},{"title":"Qwen3.5: Nobody Agrees on Attention Anymore | by Maxime Labonne | Medium","url":"https://medium.com/@mlabonne/qwen3-5-nobody-agrees-on-attention-anymore-4709e1bd014b"}]

Based on the web search results, I found relevant information about Gated Attention and its application with the 3.5 trillion token dataset in Qwen models.

## Key Findings

The paper "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free" is the first in the industry to systematically examine how attention gating affects the performance and training of large models.

The Qwen team conducted an extensive study, comparing over 30 variants of 15B Mixture-of-Experts (MoE) models and 1.7B dense models trained on a 3.5-trillion-token dataset.

A simple architectural modification – adding a head-specific sigmoid gate after Scaled Dot-Product Attention (SDPA) – consistently improves model performance.

Authors performed testing on LLMs trained on 3.5 trillion tokens to prove that Gated Attention is not just a stability fix. The gated models achieved a perplexity reduction of over 0.2 and downstream performance surged, with MMLU scores increasing by ~2.0 points and GSM8k math reasoning scores jumping by over 2.3 points compared to the baseline.

Gated Attention has been successfully integrated into the official Qwen3-Next architecture and deployed in the Qwen3-Next-80B-A3B-Instruct model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbee9e99-f0ed-4153-8ecd-1df0a9444bc3",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "ac03be8f131e42260",
  "type": "user",
  "uuid": "041d2795-94c8-4939-b5c8-c21af14ce426",
  "sourceToolAssistantUUID": "fbee9e99-f0ed-4153-8ecd-1df0a9444bc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-17T09:00:20.515Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ct4CnFKPrajq6a53JgtoRY`</summary>

```json
{
  "url": "https://www.alibabacloud.com/blog/alibaba-qwen-wins-%E2%80%9Cneurips-2025-best-paper-award%E2%80%9D-for-breakthrough-in-attention-mechanisms_602708",
  "prompt": "Extract all details about: 1) Whether models were pre-trained from scratch on 3.5T tokens. 2) The exact description of the gating mechanism. 3) Which models use Gated Attention - is it ONLY deployed in Qwen3-Next or also in other models? 4) Any details about the NeurIPS 2025 Best Paper award."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "041d2795-94c8-4939-b5c8-c21af14ce426",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sFSNiAz9ktPiXj5dVC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0ac2661-1a6c-4832-8dfb-194436f49026",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RNe7NvW1K8s7pyz2Jj5YZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1026,
      "cache_creation_input_tokens": 1259,
      "cache_read_input_tokens": 16751,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1259
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1026,
          "output_tokens": 213,
          "cache_read_input_tokens": 16751,
          "cache_creation_input_tokens": 1259,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1259,
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

_source line 29 · 2026-05-17T09:00:26.569Z_

<details><summary>↩ Tool result · `toolu_01Ct4CnFKPrajq6a53JgtoRY`</summary>

```text
# Key Details from Alibaba Qwen NeurIPS 2025 Article

## 1) Pre-training on 3.5T Tokens
The research involved comparing "over 30 variants of 15B Mixture-of-Experts (MoE) models and 1.7B dense models trained on a 3.5-trillion-token dataset." The models were trained on this extensive dataset, though the article doesn't explicitly state whether this was from-scratch pre-training versus continued training.

## 2) Gating Mechanism Description
The gating technique is described as functioning "like 'intelligent noise-canceling headphones' for a model," helping to filter irrelevant information. Specifically, the modification involves "adding a head-specific sigmoid gate after Scaled Dot-Product Attention (SDPA)."

## 3) Gated Attention Deployment
The paper identifies Gated Attention as incorporated into "Qwen3-Next" released in September 2025, which combined "Gated DeltaNet and Gated Attention." The document doesn't clarify whether this mechanism was deployed in other Qwen models beyond Qwen3-Next.

## 4) NeurIPS 2025 Best Paper Award Details
The winning paper is titled "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free." The NeurIPS Selection Committee noted: "The main recommendation of the paper is easily implemented" and praised the authors for sharing results that advance community understanding of attention mechanisms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0ac2661-1a6c-4832-8dfb-194436f49026",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "ac03be8f131e42260",
  "type": "user",
  "uuid": "96fecd70-fc44-4003-bfb5-92f24e5a730c",
  "sourceToolAssistantUUID": "e0ac2661-1a6c-4832-8dfb-194436f49026",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-17T09:00:29.065Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018LusqCrd4ookkcpXqJqbQe`</summary>

```json
{
  "query": "Qwen3.5 gated attention architecture OR \"Qwen 3.5\" gated attention"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96fecd70-fc44-4003-bfb5-92f24e5a730c",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sGzG8eDs9bUh17eVUi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78fa3f9f-29dc-4a17-88d6-6a0cce668592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013K6eCpwY7H4zDVePcGgnCA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1603,
      "cache_read_input_tokens": 18010,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1603
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 18010,
          "cache_creation_input_tokens": 1603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1603,
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

_source line 31 · 2026-05-17T09:00:36.633Z_

<details><summary>↩ Tool result · `toolu_018LusqCrd4ookkcpXqJqbQe`</summary>

```text
Web search results for query: "Qwen3.5 gated attention architecture OR "Qwen 3.5" gated attention"

Links: [{"title":"Qwen3.5: Nobody Agrees on Attention Anymore","url":"https://huggingface.co/blog/mlabonne/qwen35"},{"title":"Qwen3.5: Nobody Agrees on Attention Anymore | by Maxime Labonne | Medium","url":"https://medium.com/@mlabonne/qwen3-5-nobody-agrees-on-attention-anymore-4709e1bd014b"},{"title":"Gated Attention | Sebastian Raschka, PhD","url":"https://sebastianraschka.com/llm-architecture-gallery/gated-attention/"},{"title":"Qwen 3.5 Explained: Architecture, Upgrades Over Qwen 3, Benchmarks, and Real‑World Use Cases | by Sai Dheeraj Gummadi | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/qwen-3-5-explained-architecture-upgrades-over-qwen-3-benchmarks-and-real-world-use-cases-af38b01e9888"},{"title":"A Visual Guide to Attention Variants in Modern LLMs","url":"https://magazine.sebastianraschka.com/p/visual-attention-variants"},{"title":"[Deep Dive] Qwen 3.5 Brings Native Multimodality and Long Context to Small Open Models","url":"https://trilogyai.substack.com/p/deep-dive-qwen-35-brings-native-multimodality"},{"title":"Qwen 3.5: Complete Guide (2026)","url":"https://codersera.com/blog/qwen-3-5-complete-guide-2026/"},{"title":"Day 0 Support for Qwen 3.5 on AMD Instinct GPUs","url":"https://www.amd.com/en/developer/resources/technical-articles/2026/day-0-support-for-qwen-3-5-on-amd-instinct-gpus.html"},{"title":"qwen3.5-gated-deltanet-analysis · GitHub","url":"https://gist.github.com/justinchuby/0213aa253664fb72e9adb0089816de15"},{"title":"Running Qwen 3.5 Medium Models on Vast.ai","url":"https://vast.ai/article/running-qwen-3-5-medium-models-on-vast-ai"}]

Based on the search results, here's comprehensive information about Qwen3.5's gated attention architecture:

## Hybrid Attention Architecture

Qwen3.5 combines Gated Delta Networks (a linear attention variant) with sparse Mixture-of-Experts. Qwen 3.5 interleaves two layer types: full attention with grouped-query attention (GQA) and RoPE, and linear attention layers built on Gated DeltaNet. By default, every fourth layer is full attention.

## How Gated Attention Works

The gated attention block in Qwen-style hybrids is essentially standard scaled-dot-product attention with a few changes on top. The gated attention output gating helps eliminate attention sinks and massive activations, improving training stability at scale.

More specifically, the "gated" component adds two learned, input-dependent gates: a decay gate that controls how much of the previous state to retain, and an update gate that controls how aggressively to write corrections.

## Computational Efficiency

Qwen3-Next and Qwen3.5 architectures show that these recent hybrids do not replace attention everywhere. Instead, they replace most attention layers with a cheaper alternative and keep a smaller number of full-attention layers in the stack. Those remaining full-attention layers are where gated attention typically appears.

Full softmax attention is O(n²) in sequence length and requires a KV cache that grows linearly with context. Gated DeltaNet is O(n) and does not grow the KV cache at all - it maintains a fixed-size state vector that gets updated with a delta rule plus exponential gating.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78fa3f9f-29dc-4a17-88d6-6a0cce668592",
  "isSidechain": true,
  "promptId": "0968e2ee-949e-4503-8746-310af5436d58",
  "agentId": "ac03be8f131e42260",
  "type": "user",
  "uuid": "f671bdf7-3152-4bc7-8a38-e5bcaeb8195c",
  "sourceToolAssistantUUID": "78fa3f9f-29dc-4a17-88d6-6a0cce668592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-17T09:01:05.046Z_

I now have comprehensive information to provide a detailed verification report. Here are my findings:

---

## Verification Report: "Gated Attention for Large Language Models"

### 1. Does this paper actually exist?

**YES.** The paper is real and fully verified:
- **Full title:** "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free"
- **arXiv ID:** 2505.06708 (submitted May 10, 2025) -- CONFIRMED at https://arxiv.org/abs/2505.06708
- **OpenReview ID:** 1b7whO4SfY -- CONFIRMED at https://openreview.net/forum?id=1b7whO4SfY
- **Authors:** Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin (Alibaba/Qwen team)

### 2. Did it win NeurIPS 2025 Best Paper?

**YES.** Confirmed via the official NeurIPS blog post (https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/). It was one of four Best Papers selected from 5,290 accepted submissions at NeurIPS 2025. It was also designated as a NeurIPS 2025 Oral presentation. Alibaba Cloud publicized this win as well.

### 3. Does it implement query-conditional per-head sigmoid gating as described?

**YES, substantially correct.** The paper describes "applying a query-dependent head-specific sigmoid gate after the Scaled Dot-Product Attention (SDPA)." The terminology used in the paper is "query-dependent" rather than "query-conditional," but these are semantically equivalent. The gating is:
- **Per-head:** Each attention head has its own gate scalar
- **Sigmoid-based:** Uses a sigmoid activation function
- **Query-dependent:** The gate value is conditioned on the query

The paper also studies an "elementwise" variant where each element of the attention output is modulated independently. The GitHub repo (https://github.com/qiuzh20/gated_attention) provides both `gate_headwise` and `gate_elementwise` implementations.

### 4. Was it pre-trained from scratch on 3.5T tokens?

**PARTIALLY VERIFIED.** The paper states that models were "trained on a 3.5 trillion token dataset" in a comprehensive comparison of over 30 variants of 15B MoE models and 1.7B dense models. However, none of the sources I found explicitly state "pre-trained from scratch" versus continued pre-training. Given the nature of the study (comparing 30+ architectural variants systematically), it is highly likely these were trained from scratch for fair comparison, but the exact wording "pre-trained from scratch" does not appear verbatim in the accessible sources.

### 5. Is it deployed ONLY in Qwen3-Next models?

**NO -- this claim is too narrow.** While the paper and GitHub repo confirm that Gated Attention "has been successfully integrated into the official Qwen3-Next architecture" (specifically Qwen3-Next-80B-A3B-Instruct and Qwen3-Next-80B-A3B-Thinking), the technology has also propagated to:
- **Qwen3-Coder-Next** -- uses the same hybrid architecture
- **Qwen3.5** -- also uses gated attention in its hybrid architecture (interleaving Gated DeltaNet with full gated attention layers)

So the claim that it is deployed "only in Qwen3-Next models" is **incorrect** -- it is now used across multiple Qwen model families including Qwen3.5.

---

## Summary Table

| Claim | Verdict |
|-------|---------|
| Paper exists with arXiv ID 2505.06708 | CONFIRMED |
| OpenReview ID is 1b7whO4SfY | CONFIRMED |
| Won NeurIPS 2025 Best Paper | CONFIRMED |
| Implements query-conditional per-head sigmoid gating | CONFIRMED (paper uses "query-dependent" terminology) |
| Pre-trained from scratch on 3.5T tokens | LIKELY TRUE but not explicitly stated as "from scratch" |
| Deployed only in Qwen3-Next models | FALSE -- also in Qwen3-Coder-Next and Qwen3.5 |

Sources:
- [arXiv: 2505.06708](https://arxiv.org/abs/2505.06708)
- [OpenReview Forum](https://openreview.net/forum?id=1b7whO4SfY)
- [NeurIPS 2025 Best Paper Awards Blog Post](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)
- [GitHub: qiuzh20/gated_attention](https://github.com/qiuzh20/gated_attention)
- [Alibaba Cloud Blog: Qwen Wins NeurIPS 2025 Best Paper](https://www.alibabacloud.com/blog/alibaba-qwen-wins-%E2%80%9Cneurips-2025-best-paper-award%E2%80%9D-for-breakthrough-in-attention-mechanisms_602708)
- [Qwen3-Next on Hugging Face](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct)
- [Qwen3.5 Architecture Analysis](https://huggingface.co/blog/mlabonne/qwen35)
- [NVIDIA Blog on Qwen3-Next](https://developer.nvidia.com/blog/new-open-source-qwen3-next-models-preview-hybrid-moe-architecture-delivering-improved-accuracy-and-accelerated-parallel-processing-across-nvidia-platform/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f671bdf7-3152-4bc7-8a38-e5bcaeb8195c",
  "isSidechain": true,
  "agentId": "ac03be8f131e42260",
  "requestId": "req_011Cb7sHjGWZeWKg9fPTSMvf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b2cfddd-6b52-4b6d-a2f7-ab2cb80da671",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "809e0f3d-cfab-4e41-bee2-451342909dac",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fA7Xaev8owyaVDJCb3Etv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 19613,
      "output_tokens": 1491,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1111
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1491,
          "cache_read_input_tokens": 19613,
          "cache_creation_input_tokens": 1111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1111,
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
