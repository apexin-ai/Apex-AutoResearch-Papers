# Research conversation: I need to read the abstracts and key details of two recent papers: 1. Fetch the page at https://arxiv.org/abs/2603.01063

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aa177f85c6e833a1e.jsonl`
- **Structured JSON:** [`5584be693c4e78134478.json`](../../sessions/55/5584be693c4e78134478.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-13T18:24:13.647Z_

I need to read the abstracts and key details of two recent papers:

1. Fetch the page at https://arxiv.org/abs/2603.01063 — read the abstract and any method details visible. ELF-VLA claims to learn from failures for VLA training data curation.

2. Fetch the page at https://arxiv.org/abs/2605.06175 — read the abstract. VLA-GSE is from May 2026.

3. Also search for "TLPO token level policy optimization VLA action chunk 2026" to check if TLPO has any VLA connection.

Report: for each paper, give me (a) exact title, (b) date, (c) core method in 2 sentences, (d) how it relates to adaptive data prioritization during VLA SFT. Under 250 words total.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ff73123e-d00a-48c0-ade6-4cf8c1f7e002",
  "agentId": "aa177f85c6e833a1e",
  "type": "user",
  "uuid": "1e69f156-4917-4cee-a84b-0cb19de28232",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T18:24:13.650Z_

```json
{
  "parentUuid": "1e69f156-4917-4cee-a84b-0cb19de28232",
  "isSidechain": true,
  "agentId": "aa177f85c6e833a1e",
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
  "uuid": "dfe28131-329d-4050-9629-6d3e51a01a41",
  "timestamp": "2026-05-13T18:24:13.650Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T18:24:16.440Z_



I'll fetch both papers and run the search in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfe28131-329d-4050-9629-6d3e51a01a41",
  "isSidechain": true,
  "agentId": "aa177f85c6e833a1e",
  "requestId": "req_011Cb132s91E7LMby8MJJvTs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89662bfa-6b06-44fc-af23-4e8de5676144",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MqvMGwuVgAsu12PF68gcmH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 739,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 739,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 4 · 2026-05-13T18:24:16.543Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QhyPY7NBvPqgRMPEdprKfm`</summary>

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
  "parentUuid": "89662bfa-6b06-44fc-af23-4e8de5676144",
  "isSidechain": true,
  "agentId": "aa177f85c6e833a1e",
  "requestId": "req_011Cb132s91E7LMby8MJJvTs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24a74fbc-7603-4140-bfa1-b55cab56c4ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MqvMGwuVgAsu12PF68gcmH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 739,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 739,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 5 · 2026-05-13T18:24:16.550Z_

<details><summary>↩ Tool result · `toolu_01QhyPY7NBvPqgRMPEdprKfm`</summary>

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
  "parentUuid": "24a74fbc-7603-4140-bfa1-b55cab56c4ea",
  "isSidechain": true,
  "promptId": "ff73123e-d00a-48c0-ade6-4cf8c1f7e002",
  "agentId": "aa177f85c6e833a1e",
  "type": "user",
  "uuid": "efea599b-054d-4e16-a8dd-a834de599c3e",
  "sourceToolAssistantUUID": "24a74fbc-7603-4140-bfa1-b55cab56c4ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T18:24:19.076Z_



Now I'll fetch both papers and run the search in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efea599b-054d-4e16-a8dd-a834de599c3e",
  "isSidechain": true,
  "agentId": "aa177f85c6e833a1e",
  "requestId": "req_011Cb1336FYPTZoGwthh3UdQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be695ac4-c821-42ac-b074-92aef0a1e2e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Adwm1N1vdWQHF5nc2Z2c6q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 8962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1902,
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

_source line 7 · 2026-05-13T18:24:20.556Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015Xo4TwPvKe4coauGbpW8MY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.01063",
  "prompt": "Extract the exact title, submission date, authors, and full abstract of this paper. Also extract any method details visible on the page about how ELF-VLA works — especially how it learns from failures and curates training data for VLA."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be695ac4-c821-42ac-b074-92aef0a1e2e8",
  "isSidechain": true,
  "agentId": "aa177f85c6e833a1e",
  "requestId": "req_011Cb1336FYPTZoGwthh3UdQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5376750-cbf7-4e4e-bc7a-8907e1b68fbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Adwm1N1vdWQHF5nc2Z2c6q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 8962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1902,
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

_source line 8 · 2026-05-13T18:24:21.413Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Axid291jQMFepzfrEGD3HJ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.06175",
  "prompt": "Extract the exact title, submission date, authors, and full abstract of this paper. Also extract any method details visible on the page about VLA-GSE and how it works."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5376750-cbf7-4e4e-bc7a-8907e1b68fbe",
  "isSidechain": true,
  "agentId": "aa177f85c6e833a1e",
  "requestId": "req_011Cb1336FYPTZoGwthh3UdQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e8928e8-4160-44b6-9f9b-72a47c03c5f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Adwm1N1vdWQHF5nc2Z2c6q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 8962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1902,
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

_source line 9 · 2026-05-13T18:24:21.508Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xc87nRXJ8a3xJ44kdtaoNq`</summary>

```json
{
  "query": "TLPO token level policy optimization VLA action chunk 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e8928e8-4160-44b6-9f9b-72a47c03c5f2",
  "isSidechain": true,
  "agentId": "aa177f85c6e833a1e",
  "requestId": "req_011Cb1336FYPTZoGwthh3UdQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a91b90ea-ed52-475d-974a-fdafe29c9d66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Adwm1N1vdWQHF5nc2Z2c6q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1902,
      "cache_read_input_tokens": 8962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1902,
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

_source line 10 · 2026-05-13T18:24:27.067Z_

<details><summary>↩ Tool result · `toolu_015Xo4TwPvKe4coauGbpW8MY`</summary>

```text
# Paper Extraction Summary

**Exact Title:**
"Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures"

**Submission Date:**
March 1, 2026

**Authors:**
Yuechen Luo, Qimao Chen, Fang Li, Shaoqing Xu, Jaxin Liu, Ziying Song, Zhi-xin Yang, Fuxi Wen

**Full Abstract:**
Vision-Language-Action models for autonomous driving encounter performance plateaus during RL optimization. The root cause stems from exploration limitations imposed by prior supervised fine-tuning, resulting in recurring failures in uncommon scenarios. When all tested actions produce zero-value driving scores, the reward signal indicates failure but cannot pinpoint whether planning, reasoning, or execution caused it. ELF-VLA addresses this by augmenting RL with structured diagnostic feedback. Rather than relying on scalar rewards, the system generates detailed, interpretable diagnostic reports identifying specific failure modes. The VLA policy then utilizes this explicit feedback to create feedback-guided refinements, reintroducing corrected, high-reward samples into RL training batches to supply targeted gradients. The approach achieves state-of-the-art results on the NAVSIM benchmark for overall PDMS, EPDMS scores, and high-level planning accuracy.

**Key Method Details Visible:**
The framework produces "detailed, interpretable reports that identify the specific failure mode" rather than vague scalar feedback, enabling the policy to address critical scenarios through targeted gradient updates from refined training samples.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5376750-cbf7-4e4e-bc7a-8907e1b68fbe",
  "isSidechain": true,
  "promptId": "ff73123e-d00a-48c0-ade6-4cf8c1f7e002",
  "agentId": "aa177f85c6e833a1e",
  "type": "user",
  "uuid": "b6670d1b-c5ac-4adc-868a-762f1b0dc139",
  "sourceToolAssistantUUID": "f5376750-cbf7-4e4e-bc7a-8907e1b68fbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T18:24:28.417Z_

<details><summary>↩ Tool result · `toolu_01Axid291jQMFepzfrEGD3HJ`</summary>

```text
# Paper Extraction: VLA-GSE

**Exact Title:**
"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts"

**Submission Date:**
Submitted May 7, 2026; revised May 8, 2026

**Authors:**
Yuhua Jiang, Junjie Lu, Xinyao Qin, Xiaoyu Chen, Kaixin Wang, Feifei Gao, Li Zhao

**Full Abstract:**
"Vision-language-action (VLA) models inherit rich visual-semantic priors from pre-trained vision-language backbones, but adapting them to robotic control remains challenging. Full fine-tuning (FFT) is prone to overfitting on downstream robotic data and catastrophic forgetting of pretrained vision-language capabilities. Parameter-efficient fine-tuning (PEFT) better preserves pre-trained knowledge, yet existing PEFT methods still struggle to adapt effectively to robot control tasks. To address this gap, we propose VLA-GSE, a parameter-efficient VLA fine-tuning framework that improves control adaptation while retaining PEFT's knowledge preservation advantage. Specifically, VLA-GSE (Generalized and Specialized Experts) is initialized by spectrally decomposing the frozen backbone, assigning leading singular components to generalized experts (shared experts) and disjoint residual components to specialized experts (routed experts). This decomposition improves adaptation capacity under a fixed trainable-parameter budget. Under a comparable parameter budget, VLA-GSE updates only 2.51% of the full model parameters and consistently outperforms strong FFT and PEFT baselines. It achieves 81.2% average zero-shot success on LIBERO-Plus, preserves pre-trained VLM capability comparably to LoRA on multimodal understanding benchmarks, and improves real-world manipulation success under multiple distribution shifts."

**VLA-GSE Method Details:**
The approach uses "spectral decomposition of the frozen backbone," routing "leading singular components to generalized experts (shared experts) and disjoint residual components to specialized experts (routed experts)," enabling efficient parameter updates while maintaining knowledge preservation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e8928e8-4160-44b6-9f9b-72a47c03c5f2",
  "isSidechain": true,
  "promptId": "ff73123e-d00a-48c0-ade6-4cf8c1f7e002",
  "agentId": "aa177f85c6e833a1e",
  "type": "user",
  "uuid": "a9b80b55-4672-4d7e-93fb-e0b800e0439d",
  "sourceToolAssistantUUID": "5e8928e8-4160-44b6-9f9b-72a47c03c5f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T18:24:28.727Z_

<details><summary>↩ Tool result · `toolu_01Xc87nRXJ8a3xJ44kdtaoNq`</summary>

```text
Web search results for query: "TLPO token level policy optimization VLA action chunk 2026"

Links: [{"title":"[2604.26553] TLPO: Token-Level Policy Optimization for Mitigating Language Confusion in Large Language Models","url":"https://arxiv.org/abs/2604.26553"},{"title":"TLPO: Token-Level Policy Optimization for Mitigating Language","url":"https://arxiv.org/pdf/2604.26553"},{"title":"TLPO: Token-Level Policy Optimization for Mitigating Language Confusion in Large Language Models","url":"https://arxiv.org/html/2604.26553"},{"title":"[2603.22847] Rethinking Token-Level Policy Optimization for Multimodal Chain-of-Thought","url":"https://arxiv.org/abs/2603.22847"},{"title":"GitHub - xzxxntxdy/PEPO: Official repo for ”Rethinking Token-Level Policy Optimization for Multimodal Chain-of-Thought“","url":"https://github.com/xzxxntxdy/PEPO"},{"title":"[2603.22847v1] Rethinking Token-Level Policy Optimization for Multimodal Chain-of-Thought","url":"https://arxiv.org/abs/2603.22847v1"},{"title":"Rethinking Token-Level Policy Optimization for Multimodal Chain-of-Thought","url":"https://arxiv.org/html/2603.22847v1"},{"title":"Unlocking robotics with action tokenization | by Dave Davies | Online Inference | Mar, 2026 | Medium","url":"https://medium.com/online-inference/unlocking-robotics-with-action-tokenization-15e4160c1aee"},{"title":"Paper page - Rethinking Token-Level Policy Optimization for Multimodal Chain-of-Thought","url":"https://huggingface.co/papers/2603.22847"},{"title":"FAST: Efficient Action Tokenization for Vision-Language-Action Models","url":"https://www.pi.website/download/fast.pdf"}]

Based on the search results, I found information related to your query about TLPO and token-level policy optimization:

## TLPO (Token-Level Policy Optimization)

Token-Level Policy Optimization (TLPO) is a fine-tuning framework designed to mitigate language confusion through localized, token-level updates. TLPO identifies error-prone positions, explores alternative candidate tokens, and updates the policy using a tailored objective to suppress error-inducing outputs at a granular level.

Prior mitigation approaches based on sequence-level fine-tuning, such as DPO, ORPO, and GRPO, operate at the level of entire responses and can lead to unintended degradation of general model capabilities, motivating the need for more fine-grained alternatives. Experiments on multiple multilingual LLMs across diverse languages demonstrate that TLPO significantly outperforms baselines in improving language consistency while preserving downstream task accuracy.

## VLA and Action Chunking

Regarding VLA (Vision-Language-Action) models and action chunks, the search results show that action tokenization is the mapping from continuous robot control trajectories to discrete token sequences that can be modeled alongside words and visual tokens, where a single autoregressive Transformer takes language prompts and visual tokens as input, then predicts action tokens, which are later detokenized back into low-level controls for the robot. Action "chunks" are commonly used for high-frequency control.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a91b90ea-ed52-475d-974a-fdafe29c9d66",
  "isSidechain": true,
  "promptId": "ff73123e-d00a-48c0-ade6-4cf8c1f7e002",
  "agentId": "aa177f85c6e833a1e",
  "type": "user",
  "uuid": "df3ecd6b-9b51-463b-9f66-365402d01b27",
  "sourceToolAssistantUUID": "a91b90ea-ed52-475d-974a-fdafe29c9d66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-13T18:24:43.196Z_

Here is the report:

---

**1. ELF-VLA**
- **Title:** "Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures"
- **Date:** March 1, 2026
- **Core method:** ELF-VLA augments RL-based VLA optimization with structured diagnostic feedback instead of scalar rewards, generating interpretable reports that identify specific failure modes (planning, reasoning, or execution). Corrected, high-reward samples are then reintroduced into RL training batches to supply targeted gradients.
- **Relation to adaptive data prioritization during VLA SFT:** Directly relevant -- it performs failure-aware data curation by diagnosing why episodes fail and re-weighting the training distribution toward corrected high-value samples, which is a form of adaptive prioritization (though applied at the RL stage rather than pure SFT).

**2. VLA-GSE**
- **Title:** "VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts"
- **Date:** May 7, 2026
- **Core method:** VLA-GSE spectrally decomposes the frozen VLA backbone, routing leading singular components to shared "generalized experts" and residual components to routed "specialized experts." This achieves strong adaptation (81.2% zero-shot on LIBERO-Plus) while updating only 2.51% of parameters.
- **Relation to adaptive data prioritization during VLA SFT:** Tangential -- it addresses *how* to fine-tune efficiently (parameter allocation), not *which data* to prioritize. It could complement a data-prioritization scheme by providing the parameter-efficient training substrate.

**3. TLPO**
- **TLPO** (arXiv [2604.26553](https://arxiv.org/abs/2604.26553)) targets token-level policy optimization for mitigating language confusion in multilingual LLMs. It has **no direct VLA or action-chunking connection**; it operates on text tokens in language models, not robot action tokens. A separate paper ([2603.22847](https://arxiv.org/abs/2603.22847)) rethinks token-level PO for multimodal chain-of-thought but also does not address VLA action chunks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df3ecd6b-9b51-463b-9f66-365402d01b27",
  "isSidechain": true,
  "agentId": "aa177f85c6e833a1e",
  "requestId": "req_011Cb133yfSK1j7C2EQNUieP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8297f6ee-5787-4b57-8d95-6173b5f69452",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e0f555a-917f-49a9-8533-db0d964d3272",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hnt4T9uW7vR6yZBiPgbXxj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2093,
      "cache_read_input_tokens": 10864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2093,
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
