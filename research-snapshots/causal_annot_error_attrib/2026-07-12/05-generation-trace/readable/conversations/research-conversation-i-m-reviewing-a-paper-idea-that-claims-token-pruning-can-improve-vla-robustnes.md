# Research conversation: I'm reviewing a paper idea that claims token pruning can IMPROVE VLA robustness. However, existing papers (arXiv 2601.21

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a12cdb144c85a9795.jsonl`
- **Structured JSON:** [`cba2e1fc2fbf205b94e0.json`](../../sessions/cb/cba2e1fc2fbf205b94e0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-14T05:35:51.264Z_

I'm reviewing a paper idea that claims token pruning can IMPROVE VLA robustness. However, existing papers (arXiv 2601.21531 "On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression" and arXiv 2601.12042 "Less Is More Until It Breaks") suggest that token compression generally HURTS robustness.

I need to understand the nuance here. Please:

1. Fetch and read the abstract + key findings of arXiv 2601.21531 (use WebFetch on https://arxiv.org/abs/2601.21531). What exactly do they find? Do they distinguish between adversarial perturbations vs. natural perturbations (lighting, viewpoint, etc.)?

2. The proposed idea uses "action-conditioned" pruning trained with an information bottleneck objective — this is fundamentally different from the post-hoc compression studied in those papers. Is there evidence that TRAINED/adaptive pruning behaves differently from fixed/post-hoc compression regarding robustness?

3. Search for "information bottleneck robustness 2025 2026" — are there recent papers showing IB-based methods improve robustness in vision or RL?

4. Search for "DTP distracting token pruning VLA" (arXiv 2601.16065) — this paper prunes "distracting" tokens which is closest to pruning-for-robustness. What exactly does it do and how does it differ from the proposed ACIBS?

5. Search for "OBEYED-VLA" (arXiv 2512.22519) — does this object-centric approach for clutter-robust VLAs overlap with the proposed idea?

Report with URLs and key distinctions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a12cdb144c85a9795",
  "type": "user",
  "uuid": "96ca4b4e-9bfe-4789-b4df-8b126ab25d76",
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

_source line 2 · 2026-05-14T05:35:51.268Z_

```json
{
  "parentUuid": "96ca4b4e-9bfe-4789-b4df-8b126ab25d76",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
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
  "uuid": "622932c6-449b-47ae-82ed-867e8dff8b5c",
  "timestamp": "2026-05-14T05:35:51.268Z",
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

_source line 3 · 2026-05-14T05:35:54.299Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01P2u63rQMdpGE9aHQ9a44BL`</summary>

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
  "parentUuid": "622932c6-449b-47ae-82ed-867e8dff8b5c",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vFNmjgWubnBKuzpbNk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98535e46-5288-4013-b312-829f4b49f980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011QRbwpn2jVbJj9NjkxAGCL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 957,
      "cache_read_input_tokens": 8223,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 957
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 957,
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

_source line 4 · 2026-05-14T05:35:54.303Z_

<details><summary>↩ Tool result · `toolu_01P2u63rQMdpGE9aHQ9a44BL`</summary>

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
  "parentUuid": "98535e46-5288-4013-b312-829f4b49f980",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a12cdb144c85a9795",
  "type": "user",
  "uuid": "01fe488a-e65a-4a22-abe9-8b433a656f99",
  "sourceToolAssistantUUID": "98535e46-5288-4013-b312-829f4b49f980",
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

_source line 5 · 2026-05-14T05:36:00.392Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LJjLD5oxC8M1WfGo1W19Qy`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.21531",
  "prompt": "Extract the full abstract, key findings, and main conclusions of this paper. Specifically: 1) What do they find about how visual token compression affects adversarial robustness of large vision-language models? 2) Do they distinguish between adversarial perturbations and natural perturbations (lighting, viewpoint changes, etc.)? 3) What types of compression methods do they study (post-hoc, fixed, trained)? 4) What are their main conclusions about whether compression helps or hurts robustness?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01fe488a-e65a-4a22-abe9-8b433a656f99",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vFbyjaw9gQBoKbgyXz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd246f84-e502-408f-b564-efb73988cc49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UA1Lcnjr6eYvmBjwhDtUuH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 6 · 2026-05-14T05:36:00.759Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013wtuaW17fJHEzNwVTBt7f5`</summary>

```json
{
  "query": "information bottleneck robustness 2025 2026 vision reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd246f84-e502-408f-b564-efb73988cc49",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vFbyjaw9gQBoKbgyXz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bc2e6de-aee4-425d-928d-822343cb9e93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UA1Lcnjr6eYvmBjwhDtUuH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 7 · 2026-05-14T05:36:01.233Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NTGYqZx4NDTdt6eQzevVtr`</summary>

```json
{
  "query": "DTP distracting token pruning VLA arXiv 2601.16065"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bc2e6de-aee4-425d-928d-822343cb9e93",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vFbyjaw9gQBoKbgyXz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b69d6a83-f627-49bb-bd84-fa5e32a08985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UA1Lcnjr6eYvmBjwhDtUuH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9180,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1888,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
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

_source line 8 · 2026-05-14T05:36:01.478Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DzpDPR7fugf96DgDSf7nMt`</summary>

```json
{
  "query": "OBEYED-VLA arXiv 2512.22519 object-centric clutter robust"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b69d6a83-f627-49bb-bd84-fa5e32a08985",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vFbyjaw9gQBoKbgyXz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56390783-1cad-45eb-941b-9aaa505f6324",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UA1Lcnjr6eYvmBjwhDtUuH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 9180,
      "output_tokens": 359,
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
          "output_tokens": 359,
          "cache_read_input_tokens": 9180,
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

_source line 9 · 2026-05-14T05:36:04.838Z_

<details><summary>↩ Tool result · `toolu_01LJjLD5oxC8M1WfGo1W19Qy`</summary>

```text
# Analysis of Paper 2601.21531

## 1) Visual Token Compression and Adversarial Robustness

The paper reveals a critical vulnerability: "existing encoder-based attacks can substantially overestimate the robustness of compressed LVLMs" due to a mismatch between how perturbations are optimized (on full tokens) versus how inference operates (through compression).

## 2) Adversarial vs. Natural Perturbations

The webpage content does not distinguish between adversarial perturbations and natural perturbations like lighting or viewpoint changes. The focus remains exclusively on adversarial robustness.

## 3) Compression Methods Studied

The paper examines "diverse representative plug-and-play compression mechanisms," indicating they test multiple compression approaches without specifying whether they're post-hoc, fixed, or trained methods in the available abstract.

## 4) Main Conclusions on Compression and Robustness

The findings indicate compression substantially **hurts** robustness. The researchers conclude that "robustness assessments ignoring compression can be overly optimistic," and they emphasize the need for "compression-aware security evaluation and defenses for efficient LVLMs."

Their proposed CAGE attack achieves lower robust accuracy than baseline approaches across tested mechanisms, demonstrating that compression creates exploitable vulnerabilities.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd246f84-e502-408f-b564-efb73988cc49",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a12cdb144c85a9795",
  "type": "user",
  "uuid": "6346b693-642c-4b0b-8369-b43ce4ae665a",
  "sourceToolAssistantUUID": "cd246f84-e502-408f-b564-efb73988cc49",
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

_source line 10 · 2026-05-14T05:36:07.726Z_

<details><summary>↩ Tool result · `toolu_01NTGYqZx4NDTdt6eQzevVtr`</summary>

```text
Web search results for query: "DTP distracting token pruning VLA arXiv 2601.16065"

Links: [{"title":"[2601.16065] DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models","url":"https://arxiv.org/abs/2601.16065"},{"title":"DTP:A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models","url":"https://arxiv.org/html/2601.16065"},{"title":"DTP: A Simple yet Effective Distracting Token Pruning Framework for Vision-Language Action Models | OpenReview","url":"https://openreview.net/forum?id=5yYQDuXzZh"},{"title":"DTP:A SIMPLE YET EFFECTIVE DISTRACTING TOKEN ...","url":"https://openreview.net/pdf/81a879f3502bf537aca1b6c9bab050f3b90967e4.pdf"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"Efficient Token Pruning for LLaDA-V","url":"https://arxiv.org/html/2601.20168"},{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"[2601.07667] Adaptive Layer Selection for Layer-Wise Token Pruning in LLM Inference","url":"https://arxiv.org/abs/2601.07667"},{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"}]

Based on the search results, here's what I found about the paper DTP (arXiv 2601.16065):

## Overview

DTP is a simple yet effective plug-and-play Distracting Token Pruning framework that dynamically detects and prunes distracting image tokens, aiming to improve task success rate by correcting the model's visual attention patterns without altering its original architecture or adding additional inputs.

## Problem Addressed

Vision-Language Action (VLA) models have shown remarkable progress in robotic manipulation by leveraging the powerful perception abilities of Vision-Language Models (VLMs) to understand environments and directly output actions. However, VLA models may overly attend to image tokens in the task-irrelevant region, which are described as 'distracting tokens', and this behavior can disturb the model from the generation of the desired action tokens in each step, affecting the success rate of tasks.

## Key Findings

Experiments on the SIMPLER Benchmark show that the method consistently achieves relative improvements in task success rates across different types of novel VLA models, demonstrating generalizability to transformer-based VLAs. Additionally, further analysis reveals a negative correlation between the task success rate and the amount of attentions in the task-irrelevant region for all models tested.

The paper was published on January 22, 2026, and the authors provide code publicly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b69d6a83-f627-49bb-bd84-fa5e32a08985",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a12cdb144c85a9795",
  "type": "user",
  "uuid": "8acce07f-ae4b-432a-ad85-3ffdc1ca6a8f",
  "sourceToolAssistantUUID": "b69d6a83-f627-49bb-bd84-fa5e32a08985",
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

_source line 11 · 2026-05-14T05:36:08.775Z_

<details><summary>↩ Tool result · `toolu_013wtuaW17fJHEzNwVTBt7f5`</summary>

```text
Web search results for query: "information bottleneck robustness 2025 2026 vision reinforcement learning"

Links: [{"title":"Revisiting the Variational Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=w10KdRwcMk"},{"title":"Learning Robust Representations with Long-Term Information for Generalization in Visual Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=PDtMrogheZ"},{"title":"Publications | Chenjia Bai","url":"http://baichenjia.cn/publication/"},{"title":"GitHub - yingchengyang/Reinforcement-Learning-Papers: Related papers for reinforcement learning, including classic papers and latest papers in top conferences · GitHub","url":"https://github.com/yingchengyang/Reinforcement-Learning-Papers"},{"title":"Information Bottleneck-Enhanced Reinforcement Learning for Solving Operation Research Problems - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12737287/"},{"title":"[2208.10481] BARReL: Bottleneck Attention for Adversarial Robustness in Vision-Based Reinforcement Learning","url":"https://ar5iv.labs.arxiv.org/html/2208.10481"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/e92381dba235a8309f08ce46376189a9-Paper-Conference.pdf"},{"title":"DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://proceedings.mlr.press/v162/fan22b/fan22b.pdf"},{"title":"Information Bottleneck-Enhanced Reinforcement Learning for Solving Operation Research Problems","url":"https://www.mdpi.com/1424-8220/25/24/7572"},{"title":"Multimodal information bottleneck for deep reinforcement learning with multiple sensors - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608024002715"}]

Based on the search results, here's what I found on information bottleneck robustness in vision and reinforcement learning from 2025-2026:

## Recent Developments (2025-2026)

### Visual Reinforcement Learning with Information Bottleneck

A novel approach called ROUSER (robust action-value representation learning) has been proposed for visual reinforcement learning under the information bottleneck framework, designed to simultaneously capture long-term information and discard irrelevant features while facilitating sequential decision-making under unseen visual distractions. ROUSER introduces the information bottleneck to learn robust representations that capture long-term information from the sequential decision-making objective (i.e., action values).

### Information Bottleneck-Enhanced Framework

A new framework called Information Bottleneck-Enhanced Reinforcement Learning (IBE) integrates information-theoretic regularization into attention-based RL architectures to enhance both representation learning and exploration efficiency. IBE introduces two complementary objectives: a state representation bottleneck for extracting compact and task-relevant representations, and a policy bottleneck for regularizing policy optimization, together promoting more robust representations, smoother policy updates, and more effective exploration.

### Information Bottleneck for Variational Approaches

Recent efforts have optimized supervised deep neural networks using a variational upper bound on the information bottleneck objective, leading to enhanced robustness to adversarial attacks.

These approaches demonstrate a growing trend of applying information bottleneck principles to achieve robustness in vision-based reinforcement learning systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bc2e6de-aee4-425d-928d-822343cb9e93",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a12cdb144c85a9795",
  "type": "user",
  "uuid": "e25b5672-e4e1-4909-8310-8ed11cf5c9bd",
  "sourceToolAssistantUUID": "3bc2e6de-aee4-425d-928d-822343cb9e93",
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

_source line 12 · 2026-05-14T05:36:08.955Z_

<details><summary>↩ Tool result · `toolu_01DzpDPR7fugf96DgDSf7nMt`</summary>

```text
Web search results for query: "OBEYED-VLA arXiv 2512.22519 object-centric clutter robust"

Links: [{"title":"Clutter-Robust Vision–Language–Action Models through Object-Centric and Geometry Grounding","url":"https://arxiv.org/html/2512.22519"},{"title":"LiLo-VLA: Compositional Long-Horizon Manipulation via Linked Object-Centric Policies","url":"https://arxiv.org/html/2602.21531v1"},{"title":"HSC-VLA: Hierarchical Scene-Clearing for Robust Bimanual Manipulation in Dense Clutter","url":"https://arxiv.org/html/2603.07484"},{"title":"Learning Object-Centric Spatial Reasoning for Sequential Manipulation in Cluttered Environments","url":"https://arxiv.org/html/2603.02511"},{"title":"PosA-VLA: Enhancing Action Generation via Pose-Conditioned Anchor Attention","url":"https://arxiv.org/html/2512.03724"},{"title":"Robust Vision-Language-Action Models via Object-Centric Learning and Distance-Based Chunk Alignment","url":"https://www.mdpi.com/2076-3417/16/7/3376"},{"title":"Run-time Observation Interventions Make Vision-Language-Action Models More Visually Robust","url":"https://arxiv.org/html/2410.01971v1"},{"title":"Goal-VLA: Image-Generative VLMs as Object-Centric World Models Empowering Zero-shot Robot Manipulation","url":"https://arxiv.org/html/2506.23919v3"},{"title":"[2210.05519] Robust and Controllable Object-Centric Learning through Energy-based Models","url":"https://arxiv.org/abs/2210.05519"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"}]

Based on the search results, I found information about the paper you're asking about:

## OBEYED-VLA: Clutter-Robust Vision-Language-Action Models

OBEYED-VLA (OBject-centric and gEometrY groundED VLA) demonstrates superior robustness to cluttered scenes with various distraction settings and environmental clutter challenges compared to strong VLA baselines, despite fine-tuning only on clean single-object demonstrations.

### Key Approach

The framework explicitly disentangles perceptual grounding from action reasoning. Instead of operating directly on raw RGB, OBEYED-VLA augments VLAs with a perception module that grounds multi-view inputs into task-conditioned, object-centric, and geometry-aware observations. This module comprises a VLM-based object-centric grounding stage that selects task-relevant object regions across camera views, and a complementary geometric grounding stage that emphasizes the 3D structure of these objects over their appearance.

### How It Works

The system uses off-the-shelf VLM grounding and explicit cross-view reasoning to transform cluttered multi-view observations into task-conditioned inputs for the VLA that preserve the target object and its relevant geometry while suppressing distractors. Unlike BYOVLA, the method simply masks out distractor regions directly in the VLA inputs rather than removing them through expensive multiple forward passes and diffusion-based inpainting, making inference substantially lighter.

The arXiv paper number 2512.22519 was published in April 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56390783-1cad-45eb-941b-9aaa505f6324",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a12cdb144c85a9795",
  "type": "user",
  "uuid": "e41387ac-10a0-4b0b-978b-dbd350fecefc",
  "sourceToolAssistantUUID": "56390783-1cad-45eb-941b-9aaa505f6324",
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

_source line 13 · 2026-05-14T05:36:15.654Z_

Now let me get more details on the arXiv 2601.21531 paper and the specific IB robustness papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e41387ac-10a0-4b0b-978b-dbd350fecefc",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vGgMwEKBMoj3BW2Sx2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7458dda-e388-419b-b2c1-08c4e116c82a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4KPQQ7tbhXPfx6TYNAHkd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3414,
      "cache_read_input_tokens": 11068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3414,
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

_source line 14 · 2026-05-14T05:36:18.648Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MUp7pNFyyoHuvQPkMxmbhD`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.21531",
  "prompt": "Extract the full title, authors, abstract text, and any details about: what specific compression methods are tested (FastV, ToMe, LLaVolta, etc.), whether they test post-hoc/plug-and-play compression vs. trained compression, whether they find ANY scenario where compression helps robustness, and whether they discuss natural distribution shifts vs adversarial attacks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7458dda-e388-419b-b2c1-08c4e116c82a",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vGgMwEKBMoj3BW2Sx2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7b89702-45af-4cfc-aaa2-ae4a9378557e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4KPQQ7tbhXPfx6TYNAHkd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3414,
      "cache_read_input_tokens": 11068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3414,
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

_source line 15 · 2026-05-14T05:36:21.890Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SAr2etEMfWjFCNMcPqkvbg`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.16065",
  "prompt": "Extract the full methodology of DTP (Distracting Token Pruning): 1) How exactly does it identify \"distracting\" tokens? What criterion is used? 2) Is it training-free or does it require training? 3) Does it use attention patterns, gradients, or some other signal? 4) Does it improve robustness to visual distractors or just improve task success on clean tasks? 5) What is the pruning mechanism at inference time? 6) Does it relate to information bottleneck theory at all?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7b89702-45af-4cfc-aaa2-ae4a9378557e",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vGgMwEKBMoj3BW2Sx2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d1e85de-fac7-4fc2-82d7-02cef6eecf0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4KPQQ7tbhXPfx6TYNAHkd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3414,
      "cache_read_input_tokens": 11068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3414,
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

_source line 16 · 2026-05-14T05:36:23.466Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LPLk3ED1v2CV8VyU9XXj3f`</summary>

```json
{
  "url": "https://openreview.net/forum?id=PDtMrogheZ",
  "prompt": "Extract the title, abstract, and key findings of this paper about information bottleneck for robust visual reinforcement learning. What is the method called? How does it use information bottleneck to achieve robustness? Does it show that IB-trained representations are more robust to visual distractions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d1e85de-fac7-4fc2-82d7-02cef6eecf0d",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vGgMwEKBMoj3BW2Sx2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a21f012d-c3d1-47e0-919a-d89da93e5b23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4KPQQ7tbhXPfx6TYNAHkd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3414,
      "cache_read_input_tokens": 11068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3414,
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

_source line 17 · 2026-05-14T05:36:24.042Z_

<details><summary>↩ Tool result · `toolu_01MUp7pNFyyoHuvQPkMxmbhD`</summary>

```text
# Paper Summary: Adversarial Robustness of LVLMs under Visual Token Compression

**Full Title:** "On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression"

**Authors:** Xinwei Zhang, Hangcheng Liu, Li Bai, Hao Wang, Qingqing Ye, Tianwei Zhang, Haibo Hu

## Abstract
The researchers demonstrate that existing attacks overestimate robustness in compressed vision-language models due to an "optimization-inference mismatch." They propose CAGE (Compression-AliGnEd attack) to address this gap, using expected feature disruption and rank distortion alignment techniques.

## Specific Compression Methods Tested
The abstract states the evaluation covers "diverse representative plug-and-play compression mechanisms" but **does not name specific methods** (like FastV, ToMe, or LLaVolta) in the provided content.

## Compression Type
The paper explicitly focuses on **plug-and-play, encoder-based compression** that works without assuming "access to the deployed compression mechanism or its token budget."

## Robustness Improvements Found
**No scenarios identified where compression improves robustness.** Results consistently show CAGE "achieves lower robust accuracy than the baseline," indicating compression consistently reduces adversarial robustness.

## Distribution Shifts vs. Adversarial Attacks
The provided content addresses **adversarial attacks only**—no discussion of natural distribution shifts appears in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7b89702-45af-4cfc-aaa2-ae4a9378557e",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a12cdb144c85a9795",
  "type": "user",
  "uuid": "a9c8a465-59aa-4fad-8f39-23c0974c4bd7",
  "sourceToolAssistantUUID": "c7b89702-45af-4cfc-aaa2-ae4a9378557e",
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

_source line 18 · 2026-05-14T05:36:24.631Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XrAc4X9AtVToS6cToYP47E`</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/2208.10481",
  "prompt": "Extract the title, abstract, and key findings of BARReL (Bottleneck Attention for Adversarial Robustness in Vision-Based Reinforcement Learning). How does it use information bottleneck for adversarial robustness in visual RL? What are the key results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9c8a465-59aa-4fad-8f39-23c0974c4bd7",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vGgMwEKBMoj3BW2Sx2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a3faf95-146e-483d-8621-642342e1e606",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4KPQQ7tbhXPfx6TYNAHkd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3414,
      "cache_read_input_tokens": 11068,
      "output_tokens": 642,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3414
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 642,
          "cache_read_input_tokens": 11068,
          "cache_creation_input_tokens": 3414,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3414,
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

_source line 19 · 2026-05-14T05:36:26.685Z_

<details><summary>↩ Tool result · `toolu_01LPLk3ED1v2CV8VyU9XXj3f`</summary>

```text
# Visual RL Robustness Paper Summary

**Title:** Learning Robust Representations with Long-Term Information for Generalization in Visual Reinforcement Learning

**Method Name:** ROUSER (Robust Action-Value Representation Learning)

**How Information Bottleneck Achieves Robustness:**

ROUSER applies the IB framework by "maximizing their mutual information with action values for long-term information, while minimizing mutual information with state-action pairs to discard irrelevant features." This dual optimization preserves decision-critical information while filtering out distracting visual elements.

**Key Innovation:**

Since action values are unavailable during training, the method decomposes them into "one-step rewards and robust representations of subsequent pairs," enabling practical implementation using known rewards.

**Empirical Results:**

The paper demonstrates strong generalization performance, with ROUSER "outperforms several state-of-the-art methods in eleven out of twelve tasks, across both unseen background and color distractions."

**Key Finding:**

Yes—the results confirm that IB-trained representations effectively improve robustness to visual distractions while maintaining the long-term decision-making capability essential for reinforcement learning tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a21f012d-c3d1-47e0-919a-d89da93e5b23",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a12cdb144c85a9795",
  "type": "user",
  "uuid": "97dc91ef-0f11-4909-9100-62272ca0fc29",
  "sourceToolAssistantUUID": "a21f012d-c3d1-47e0-919a-d89da93e5b23",
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

_source line 20 · 2026-05-14T05:36:29.561Z_

<details><summary>↩ Tool result · `toolu_01SAr2etEMfWjFCNMcPqkvbg`</summary>

```text
# DTP Methodology: Complete Analysis

## 1. Distracting Token Identification Criterion

DTP identifies distracting tokens through a two-stage comparison process:

**Important Region Construction**: The method computes relevance scores between prompt tokens and visual tokens using cross-attention weights (Equation 1) or embedding similarity (Equation 2). The top-k highest-relevance tokens form the "important region."

**Distraction Detection**: A visual token in the unimportant region qualifies as distracting if: "its attention value exceeds the thresholded maximum" (Equation 5). Specifically, if attention in the unimportant region exceeds τ times the maximum attention in the important region, the token gets pruned.

## 2. Training Requirements

**Completely training-free.** The authors emphasize it's a "plug-and-play framework" operating "during inference with negligible overhead." No model retraining, weight modification, or architectural changes occur.

## 3. Signal Type

The method relies exclusively on **attention patterns**, not gradients. It:
- Extracts attention weights from transformer layers
- Constructs relevance heatmaps from prompt-to-visual token attention
- Analyzes action generation attention across layers using weighted aggregation

## 4. Robustness vs. Clean Task Performance

The paper addresses **clean task performance improvement**, not explicit robustness to visual distractors. However, the analysis reveals that "failure episodes consistently exhibit higher unimportant attention than success episodes" across models, suggesting the method indirectly improves robustness by reducing attention leakage to irrelevant regions.

## 5. Inference-Time Pruning Mechanism

At inference, DTP:
1. Generates an initial action token to analyze attention patterns
2. Constructs a binary pruning mask based on the distraction criterion
3. Re-generates the refined action token with masked visual tokens (preventing attention to pruned regions)

For efficiency, "SpatialVLA analyzes only the first action token, applying one mask across all subsequent tokens."

## 6. Information Bottleneck Relation

**No explicit connection to information bottleneck theory.** However, the framework uses an entropy-based formulation (Section 4.2) measuring "conditional uncertainty" of correct actions under different attention patterns. This resembles information-theoretic concepts but remains distinct from formal IB frameworks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d1e85de-fac7-4fc2-82d7-02cef6eecf0d",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a12cdb144c85a9795",
  "type": "user",
  "uuid": "9df0e592-5701-4e79-a3e0-9406f248c109",
  "sourceToolAssistantUUID": "0d1e85de-fac7-4fc2-82d7-02cef6eecf0d",
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

_source line 21 · 2026-05-14T05:36:31.006Z_

<details><summary>↩ Tool result · `toolu_01XrAc4X9AtVToS6cToYP47E`</summary>

```text
# BARReL: Bottleneck Attention for Adversarial Robustness

## Title and Abstract

**Title:** BARReL: Bottleneck Attention for Adversarial Robustness in Vision-Based Reinforcement Learning

**Abstract Summary:** The paper investigates how vision-based RL agents respond to gradient-based adversarial attacks and proposes Bottleneck Attention Modules (BAM) as a defense mechanism. The authors demonstrate that "learned attention maps can be used to recover activations of a convolutional layer by restricting" spatial activations to salient regions, improving robustness during inference.

## How It Uses Information Bottleneck

Rather than implementing classical information bottleneck theory, BARReL leverages **selective spatial attention** as a practical defense. The key mechanism works by:

1. Training BAM-CNN architectures with adversarial training (applying PGD attacks every 10th frame)
2. Using learned attention maps to identify decision-relevant image regions
3. Applying element-wise multiplication to "prune" non-salient areas affected by perturbations

The approach assumes that adversarial perturbations corrupt both relevant and irrelevant image regions, but masking non-salient areas reduces overall perturbation impact.

## Key Results

**Performance improvements across Atari environments:**
- Breakout-v4: 4.2× improvement in reward performance
- MsPacman-v4: 1.36× improvement
- SpaceInvaders-v4: 1.02× improvement

**Attack recovery metrics** (at ε=0.05):
- Breakout: 35.51% full action recovery (Reversed-TOP-1)
- Partial recovery rates (Reversed-TOP-2): 66-76% across environments

The method shows promise but remains insufficient for full robustness, with agents still performing worse under attack than clean conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a3faf95-146e-483d-8621-642342e1e606",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a12cdb144c85a9795",
  "type": "user",
  "uuid": "59cc72e5-cc36-441f-8219-0654148b2597",
  "sourceToolAssistantUUID": "0a3faf95-146e-483d-8621-642342e1e606",
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

_source line 22 · 2026-05-14T05:36:35.092Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WzLb2m9VbsyroPVspxjcnY`</summary>

```json
{
  "query": "\"Less Is More Until It Breaks\" arXiv 2601.12042 token compression VLM robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59cc72e5-cc36-441f-8219-0654148b2597",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vJJdnYy7yUcTM2v8Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eedebe6a-2ea7-410d-8bfd-beb86d141b51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aavc2C55nePm6CAGssHaME",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2327,
      "cache_read_input_tokens": 14482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2327,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 23 · 2026-05-14T05:36:35.529Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016JJdxUF5C6HzrVYaLB8nU7`</summary>

```json
{
  "query": "trained adaptive token pruning improves robustness vs post-hoc compression 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eedebe6a-2ea7-410d-8bfd-beb86d141b51",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vJJdnYy7yUcTM2v8Nh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3505c464-3fd6-475e-98ad-b34f4e2d45f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aavc2C55nePm6CAGssHaME",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2327,
      "cache_read_input_tokens": 14482,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2327
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 14482,
          "cache_creation_input_tokens": 2327,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2327,
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

_source line 24 · 2026-05-14T05:36:38.849Z_

<details><summary>↩ Tool result · `toolu_01WzLb2m9VbsyroPVspxjcnY`</summary>

```text
Web search results for query: ""Less Is More Until It Breaks" arXiv 2601.12042 token compression VLM robustness"

No links found.

I was unable to find search results for that specific query. The search didn't return any matching results for the arXiv paper with ID 2601.12042 or the exact title "Less Is More Until It Breaks" combined with those specific parameters.

This could be because:
1. The paper might be very recent and not yet indexed by search engines
2. The arXiv ID or title might have a slight variation
3. The paper may not be publicly available yet or widely indexed online

If you're looking for this paper, I'd recommend:
- Visiting arXiv.org directly and searching for paper 2601.12042
- Searching for the paper title alone on arXiv
- Checking if the arXiv ID is correct (the format is typically YYMM.XXXXX)

Would you like me to try a different search query with adjusted terms?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eedebe6a-2ea7-410d-8bfd-beb86d141b51",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a12cdb144c85a9795",
  "type": "user",
  "uuid": "fdd0b7cc-c31e-407b-9a05-3ebcd0dcc8de",
  "sourceToolAssistantUUID": "eedebe6a-2ea7-410d-8bfd-beb86d141b51",
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

_source line 25 · 2026-05-14T05:36:45.462Z_

<details><summary>↩ Tool result · `toolu_016JJdxUF5C6HzrVYaLB8nU7`</summary>

```text
Web search results for query: "trained adaptive token pruning improves robustness vs post-hoc compression 2025 2026"

Links: [{"title":"GitHub - ZLKong/Awesome-Collection-Token-Reduction: A collection of token reduction (token pruning, merging, clustering, etc.) techniques for ML/AI · GitHub","url":"https://github.com/ZLKong/Awesome-Collection-Token-Reduction"},{"title":"Token Reduction Should Go Beyond Efficiency in ...","url":"https://arxiv.org/pdf/2505.18227"},{"title":"Token Pruning","url":"https://www.aussieai.com/research/token-pruning"},{"title":"Token Pruning for Efficient NLP, Vision, and Speech Models[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202502.2098"},{"title":"Does Visual Token Pruning Improve Calibration? An Empirical Study on Confidence in MLLMs","url":"https://arxiv.org/html/2604.12035"},{"title":"Compact: Common-token Optimized Model Pruning Across Channels and Tokens","url":"https://arxiv.org/html/2509.06836v1"},{"title":"Token Reduction Should Go Beyond Efficiency in Generative Models – From Vision, Language to Multimodality","url":"https://arxiv.org/html/2505.18227v1"},{"title":"Adaptive Pruning with Module Robustness Sensitivity: Balancing Compression and Robustness","url":"https://arxiv.org/html/2410.15176v2"},{"title":"AI Model Compression: Pruning and Quantization Strategies for Real-Time Devices","url":"https://promwad.com/news/ai-model-compression-real-time-devices-2025"},{"title":"ATP-LLaVA: Adaptive Token Pruning for Large Vision Language Models","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Ye_ATP-LLaVA_Adaptive_Token_Pruning_for_Large_Vision_Language_Models_CVPR_2025_paper.pdf"}]

Based on the search results, here's what I found regarding trained adaptive token pruning versus post-hoc compression:

## Key Distinction Between Adaptive Training vs. Post-hoc Compression

Token reduction is commonly treated as a post hoc optimization, rather than being integrated into the core design and training of the model, according to a 2025 position paper on token reduction. This highlights a fundamental issue in current approaches.

## Robustness Advantages of Trained Adaptive Approaches

The research suggests that integrated training approaches offer robustness benefits over post-hoc methods:

By learning to intelligently select, merge, or compress tokens based on their contribution to generation objectives—rather than solely on raw redundancy—models can simultaneously reduce computational load, improve robustness, and enhance interpretability and alignment.

Naive pruning methods may discard informative tokens, thereby degrading model understanding and performance, which is a risk with post-hoc approaches.

## Research Direction

A new paradigm may emerge: models trained from the ground up for compressed deployment, eliminating post-hoc adaptations.

Recent work from 2025-2026 includes papers like "ATP-LLaVA" (Adaptive Token Pruning for Large Vision Language Models) at CVPR 2025, which exemplifies the shift toward integrating adaptive pruning during model design rather than as an afterthought.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3505c464-3fd6-475e-98ad-b34f4e2d45f2",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a12cdb144c85a9795",
  "type": "user",
  "uuid": "4adb8dac-dcfc-4c4a-b27d-e1f064e3b853",
  "sourceToolAssistantUUID": "3505c464-3fd6-475e-98ad-b34f4e2d45f2",
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

_source line 26 · 2026-05-14T05:36:50.555Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012mhpadd6Ge6Ado3s8hpChP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.12042",
  "prompt": "Extract the full title, abstract, and key findings of this paper. What do they find about token compression and robustness? Do they study VLMs or VLAs? What compression methods are studied? What breaks when you compress too much?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4adb8dac-dcfc-4c4a-b27d-e1f064e3b853",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vKNRmWN2bTZhizWUjU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a62afea-7d04-4c6c-9d08-a804733d6f16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THk9LnnZmw7NGviiHeVFvX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1305,
      "cache_read_input_tokens": 16809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1305,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 27 · 2026-05-14T05:36:52.416Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AaPEZGtmkmKP1nhet6aWgg`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.18227v1",
  "prompt": "Extract the key arguments about trained/adaptive token reduction vs post-hoc compression. Do they discuss robustness? Do they argue that training-aware token reduction can improve model properties beyond just efficiency? What is their key thesis about why integrated token reduction during training is superior to post-hoc methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a62afea-7d04-4c6c-9d08-a804733d6f16",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vKNRmWN2bTZhizWUjU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db4dea8a-5b70-4bcf-b421-5194643ffd82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THk9LnnZmw7NGviiHeVFvX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1305,
      "cache_read_input_tokens": 16809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1305,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
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

_source line 28 · 2026-05-14T05:36:54.774Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GWAPJLRqM4s3DKJjYYxge5`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.22519",
  "prompt": "Extract the full methodology of OBEYED-VLA: 1) How does the object-centric grounding work? 2) How does it handle clutter/distractors? 3) Does it prune tokens or mask image regions? 4) Is it training-free or does it require fine-tuning? 5) How does it differ from simple attention-based token pruning? 6) What are the key results on clutter robustness?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db4dea8a-5b70-4bcf-b421-5194643ffd82",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vKNRmWN2bTZhizWUjU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51c95ce0-c058-4698-820a-8427a3c94e16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THk9LnnZmw7NGviiHeVFvX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1305,
      "cache_read_input_tokens": 16809,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1305
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 429,
          "cache_read_input_tokens": 16809,
          "cache_creation_input_tokens": 1305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1305,
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

_source line 29 · 2026-05-14T05:36:56.047Z_

<details><summary>↩ Tool result · `toolu_012mhpadd6Ge6Ado3s8hpChP`</summary>

```text
# Paper Analysis: Vision Token Compression Security

## Full Title
"Less Is More -- Until It Breaks: Security Pitfalls of Vision Token Compression in Large Vision-Language Models"

## Abstract Summary
The researchers reveal that visual token compression—a technique to improve inference efficiency—creates significant security vulnerabilities in Large Vision-Language Models (LVLMs). They discover that models robust under normal conditions become vulnerable when compression is enabled, with failures appearing only in compressed settings.

## Key Findings

**Core Discovery:** The team identifies "instability in token importance ranking as the primary cause" of robustness degradation. Small perturbations can alter which tokens get discarded, causing the model to lose critical information.

**Model Type:** This research focuses on **LVLMs** (Large Vision-Language Models), not VLAs.

**Compression Methods Studied:** The abstract indicates "extensive experiments across models, datasets, and compression methods," though specific compression techniques aren't detailed in this excerpt.

**What Breaks:** The primary failure occurs in the token selection mechanism. According to their findings, "small and imperceptible perturbations can significantly alter token rankings, leading the compression mechanism to mistakenly discard task-critical information and ultimately causing model failure."

The authors propose "Compression-Aware Attack" methods to exploit these vulnerabilities and note that "defenses provide only limited protection," revealing a previously overlooked efficiency-security trade-off.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a62afea-7d04-4c6c-9d08-a804733d6f16",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a12cdb144c85a9795",
  "type": "user",
  "uuid": "8f68de14-3cd3-47e7-b972-8efbb605000c",
  "sourceToolAssistantUUID": "5a62afea-7d04-4c6c-9d08-a804733d6f16",
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

_source line 30 · 2026-05-14T05:36:57.223Z_

<details><summary>↩ Tool result · `toolu_01AaPEZGtmkmKP1nhet6aWgg`</summary>

```text
# Key Arguments on Training-Integrated vs Post-Hoc Token Reduction

## Core Thesis

The paper positions token reduction as fundamentally superior when integrated during training rather than applied post-hoc. They argue that current approaches treat token reduction as "a post hoc optimization, rather than being integrated into the core design and training of the model."

## Training-Aware Superiority

The authors contend that principled integration during training enables models to "learn to intelligently select, merge, or compress tokens based on their contribution to generation objectives." This contrasts with post-hoc methods that merely respond to redundancy patterns already baked into trained weights.

## Beyond Efficiency Claims

Yes, they extensively argue for benefits transcending computational gains:

- **Robustness & Stability**: Methods like Rho-1 demonstrate that selective token focus during pre-training "filters out noisy or less informative tokens, leading to faster convergence and improved performance."

- **Model Properties**: They claim token reduction can simultaneously "reduce computational load, improve robustness, and enhance interpretability and alignment."

- **Semantic Integrity**: Training-aware approaches preserve "semantic integrity" across modalities and long contexts, addressing alignment issues that post-hoc pruning often degrades.

## Key Distinction

The fundamental difference: training-integrated methods optimize tokens *for the task*, while post-hoc compression optimizes for *efficiency alone*, often sacrificing performance quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db4dea8a-5b70-4bcf-b421-5194643ffd82",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a12cdb144c85a9795",
  "type": "user",
  "uuid": "c755491d-6b49-4341-b90b-a8ecf9d6c5f0",
  "sourceToolAssistantUUID": "db4dea8a-5b70-4bcf-b421-5194643ffd82",
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

_source line 31 · 2026-05-14T05:37:03.724Z_

<details><summary>↩ Tool result · `toolu_01GWAPJLRqM4s3DKJjYYxge5`</summary>

```text
# OBEYED-VLA Methodology Extraction

## 1) Object-Centric Grounding Process

OBEYED-VLA employs a two-stage approach:

**Stage 1 - Task-Aware Base-View Grounding:** A VLM parses the instruction to identify relevant objects, then uses "set-of-mark visual prompting" by overlaying numeric markers on segmentation masks. The VLM identifies which marked regions correspond to task-relevant objects.

**Stage 2 - Cross-View Region Matching:** Rather than grounding the wrist view directly, the system transfers base-view localization by using "object-centric reference crops" as canonical anchors. The VLM matches these base-view crops to corresponding regions in wrist-view images using set-of-mark prompting again.

## 2) Handling Clutter and Distractors

The framework suppresses irrelevant content through explicit masking. After identifying task-relevant objects, the system "applies binary masks within cropped windows to suppress background," effectively removing distractor visibility before policy inference.

## 3) Token Pruning vs. Image Masking

OBEYED-VLA uses **image region masking**, not token pruning. It converts selected regions into masked depth representations. The approach "applies depth-based observations as masks to filter only the depth measurements associated with relevant objects," preserving geometry while eliminating distractors.

## 4) Training Requirements

The framework is **partially training-free**:
- Perception modules remain **frozen** (VLM, segmentation, depth estimation)
- Only the downstream VLA policy requires fine-tuning on clean single-object demonstrations
- No synthetic clutter data or auxiliary training objectives needed

## 5) Distinction from Attention-Based Token Pruning

Unlike attention mechanisms, OBEYED-VLA:
- Operates on explicit image-space masks rather than learned attention weights
- Produces interpretable, structured representations (masked depth)
- Doesn't rely on the policy learning to ignore distractors; instead, distractors are removed pre-input
- Enables "plug-and-play integration with different VLAs"

## 6) Key Clutter Robustness Results

- **With 4 distractors:** OBEYED-VLA achieves ~85% success vs. <10% for baselines
- **With 7 distractors:** Maintains ~80% success while baselines drop to near-zero
- **Absent-target rejection:** Reaches ~95% success (correctly abstaining) vs. 10-40% for baselines
- **Background shifts:** Remains >80% stable across appearance changes where baselines degrade 10-50 percentage points
- **Unseen objects:** Achieves ~75% success in cluttered scenes with novel objects
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51c95ce0-c058-4698-820a-8427a3c94e16",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a12cdb144c85a9795",
  "type": "user",
  "uuid": "3fe465e0-c5ac-4a52-8ffa-f1e5aa1eb996",
  "sourceToolAssistantUUID": "51c95ce0-c058-4698-820a-8427a3c94e16",
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

_source line 32 · 2026-05-14T05:37:07.692Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LJQZuw23gHMBpG4bLbqtKt`</summary>

```json
{
  "query": "DRIBO \"deep reinforcement learning\" \"multi-view information bottleneck\" robustness visual distractions results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fe465e0-c5ac-4a52-8ffa-f1e5aa1eb996",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vLiYGUTkfKnzUS9EFA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b094f65-9be6-4679-ac95-bdedaef127c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEMiehh4n8YjAp38vbuJXK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1776,
      "cache_read_input_tokens": 18114,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1776
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 18114,
          "cache_creation_input_tokens": 1776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1776,
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

_source line 33 · 2026-05-14T05:37:15.591Z_

<details><summary>↩ Tool result · `toolu_01LJQZuw23gHMBpG4bLbqtKt`</summary>

```text
Web search results for query: "DRIBO "deep reinforcement learning" "multi-view information bottleneck" robustness visual distractions results"

Links: [{"title":"[2102.13268] DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://arxiv.org/abs/2102.13268"},{"title":"DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://proceedings.mlr.press/v162/fan22b/fan22b.pdf"},{"title":"DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck | OpenReview","url":"https://openreview.net/forum?id=Py8WbvKH_wv"},{"title":"[2102.13268] DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://ar5iv.labs.arxiv.org/html/2102.13268"},{"title":"GitHub - JmfanBU/DRIBO: DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://github.com/JmfanBU/DRIBO"},{"title":"(PDF) Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://www.researchgate.net/publication/349682874_Robust_Deep_Reinforcement_Learning_via_Multi-View_Information_Bottleneck"},{"title":"ICML Poster DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck","url":"https://icml.cc/virtual/2022/poster/16441"},{"title":"Robust Deep Reinforcement Learning via MultiView Infomration BOttleneck... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Robust-Deep-Reinforcement-Learning-via-MultiView-Infomration-BOttleneck-DRIBO_fig1_349682874"},{"title":"[PDF] Robust Deep Reinforcement Learning via Multi-View Information Bottleneck | Semantic Scholar","url":"https://www.semanticscholar.org/paper/09f36087d9dae1ca5ccc1d75bb326954ec30239a"},{"title":"GitHub - BU-DEPEND-Lab/DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck · GitHub","url":"https://github.com/BU-DEPEND-Lab/DRIBO"}]

Based on the search results, I found comprehensive information about DRIBO and its results. Here's a summary:

## DRIBO: Robust Deep Reinforcement Learning via Multi-View Information Bottleneck

DRIBO addresses the problem that deep reinforcement learning agents are often sensitive to visual changes unseen in training environments by leveraging the sequential nature of RL to learn robust representations that encode only task-relevant information based on an unsupervised multi-view setting.

### Methodology

The approach introduces a novel contrastive version of the Multi-View Information Bottleneck (MIB) objective for temporal data, training RL agents from pixels with this auxiliary objective to learn robust representations that can compress away task-irrelevant information and are predictive of task-relevant dynamics.

### Results on Visual Distractions

The approach achieves state-of-the-art performance on a diverse set of visual control tasks in the DeepMind Control Suite when the background is replaced with natural videos. 

Experimental results show that DRIBO learns representations that are robust against task-irrelevant distractions and boosts the RL agent's performance even when complex visual distractors are introduced, while also improving generalization performance compared to well-established baselines on the large-scale Procgen benchmarks.

### Key Advantage

DRIBO substantially outperforms its variant without the information bottleneck term (DRIBO-no-skl) in the natural video setting, demonstrating better robustness of the learned policy against unseen visual distractors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b094f65-9be6-4679-ac95-bdedaef127c0",
  "isSidechain": true,
  "promptId": "7eed4653-b9f3-4dd3-bb68-b431a54098c8",
  "agentId": "a12cdb144c85a9795",
  "type": "user",
  "uuid": "4eb7cbbb-38d2-4ad4-b862-9c935d6c53e3",
  "sourceToolAssistantUUID": "2b094f65-9be6-4679-ac95-bdedaef127c0",
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

_source line 34 · 2026-05-14T05:38:16.799Z_

Now I have comprehensive information to provide a detailed report. Let me compile the findings.

---

## Report: Token Pruning and VLA Robustness — Key Distinctions

### 1. arXiv 2601.21531: "On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression"

**URL:** https://arxiv.org/abs/2601.21531

**Key findings:**
- Studies **plug-and-play, post-hoc** visual token compression on LVLMs (not VLAs).
- Discovers that existing encoder-based adversarial attacks **overestimate** robustness of compressed models due to an "optimization-inference mismatch" — attacks are optimized on full tokens but inference operates through compression.
- Proposes CAGE (Compression-AliGnEd attack) that properly accounts for compression, revealing that compression **consistently hurts adversarial robustness**.
- **Critical limitation:** The paper is exclusively about **adversarial perturbations**. It does NOT study natural perturbations (lighting, viewpoint, clutter, backgrounds). This is the key nuance — their negative finding applies only to adversarial attacks, not to natural distribution shifts.

### arXiv 2601.12042: "Less Is More — Until It Breaks"

**URL:** https://arxiv.org/abs/2601.12042

**Key findings:**
- Identifies "instability in token importance ranking" as the primary cause of robustness degradation — small perturbations can **alter which tokens get discarded**, causing loss of critical information.
- Again focuses on **adversarial/security** attacks, not natural perturbations.
- The vulnerability is inherent to **post-hoc compression**: the token selection mechanism was never trained to be robust; adversaries can manipulate rankings cheaply.

### 2. Trained/Adaptive Pruning vs. Post-hoc Compression: Why They Behave Differently

**The fundamental distinction:** Both negative papers (2601.21531 and 2601.12042) study **post-hoc, plug-and-play compression** where the pruning criterion was never optimized for the downstream task or for robustness. The vulnerability they expose — ranking instability under perturbation — is precisely what a **trained, task-aware** pruning mechanism can address.

Evidence from the position paper "Token Reduction Should Go Beyond Efficiency" (arXiv 2505.18227, https://arxiv.org/html/2505.18227v1):
- Argues that post-hoc methods optimize for **efficiency alone** while training-integrated methods optimize tokens **for the task**.
- Claims training-aware reduction can simultaneously "reduce computational load, improve robustness, and enhance interpretability."
- Cites Rho-1 showing that selective token focus during pre-training "filters out noisy or less informative tokens, leading to faster convergence and improved performance."

**Bottom line:** An action-conditioned IB objective that LEARNS which tokens to discard (optimizing for task-relevant information preservation) is categorically different from post-hoc methods that discard tokens based on heuristic redundancy metrics. The negative findings in those papers do not transfer to trained-compression approaches.

### 3. Information Bottleneck + Robustness: Strong Recent Evidence

Multiple papers demonstrate IB-based methods improving robustness in vision/RL:

**DRIBO (ICML 2022, still state-of-art baseline):** https://arxiv.org/abs/2102.13268
- Multi-View Information Bottleneck for deep RL.
- Learns representations that compress away task-irrelevant information while being predictive of task-relevant dynamics.
- Substantially outperforms its ablation without the IB term, demonstrating that the bottleneck specifically contributes to robustness against visual distractors.

**BARReL (2022):** https://ar5iv.labs.arxiv.org/html/2208.10481
- Bottleneck Attention for Adversarial Robustness in vision-based RL.
- Uses learned attention maps to spatially mask non-salient regions, functioning as a practical bottleneck.
- Achieves 4.2x improvement in Breakout under adversarial attack.
- Directly demonstrates that **pruning non-salient spatial regions improves adversarial robustness** because perturbations in irrelevant regions are discarded.

**ROUSER (ICLR 2025):** https://openreview.net/forum?id=PDtMrogheZ
- Applies IB by maximizing mutual information with action values (long-term information) while minimizing MI with state-action pairs (irrelevant features).
- Outperforms SOTA in 11/12 tasks across unseen background and color distractions.
- **Most directly relevant:** Shows IB-trained representations in visual RL achieve robustness to natural visual distractions (not just adversarial).

**IBE (2025):** Information Bottleneck-Enhanced RL introducing both state representation bottleneck and policy bottleneck for "more robust representations, smoother policy updates, and more effective exploration."

### 4. DTP: Distracting Token Pruning (arXiv 2601.16065)

**URL:** https://arxiv.org/abs/2601.16065

**What it does:**
- **Training-free, plug-and-play** framework for VLAs.
- Identifies "distracting" tokens via cross-attention relevance: constructs an "important region" from prompt-visual attention, then flags tokens in the unimportant region that nonetheless receive high action-generation attention (exceeding threshold tau times max attention in the important region).
- At inference: generates initial action token, analyzes attention patterns, builds pruning mask, re-generates with masked tokens.

**Key distinction from proposed ACIBS:**
| | DTP | ACIBS (proposed) |
|---|---|---|
| Training | None (post-hoc) | End-to-end with IB objective |
| Pruning signal | Attention heuristics | Learned action-conditioned relevance |
| Theoretical basis | Empirical observation | Information bottleneck theory |
| Adaptation | Fixed threshold tau | Learned, task-adaptive |
| Robustness claim | Indirect (removes attention leakage) | Explicit (IB removes task-irrelevant info) |
| Overhead | 2x forward pass per step | Single forward pass (amortized) |

DTP is the closest existing work, but it relies on heuristic attention thresholds without theoretical guarantees. The key weakness: its pruning criterion is itself **not robust** — under visual perturbations, the attention patterns it relies on may shift, leading to incorrect pruning decisions (exactly the vulnerability identified in 2601.12042). A trained IB objective should learn stable, task-grounded pruning that is robust to input perturbations by construction.

### 5. OBEYED-VLA (arXiv 2512.22519)

**URL:** https://arxiv.org/html/2512.22519

**What it does:**
- Object-centric + geometry grounding for clutter-robust VLAs.
- Two-stage perception: (1) VLM-based grounding identifies task-relevant objects via set-of-mark prompting, (2) cross-view region matching transfers localization across camera views.
- Applies **binary image-space masks** (not token pruning) to suppress distractors before policy input.
- Converts to masked depth representations, preserving geometry while eliminating clutter.
- Fine-tuned on clean single-object demos only; perception modules frozen.

**Results:** ~85% success with 4 distractors vs. <10% baselines; ~80% with 7 distractors.

**Key distinctions from proposed ACIBS:**
| | OBEYED-VLA | ACIBS (proposed) |
|---|---|---|
| Operates on | Image-space masks (pre-tokenization) | Token-level pruning (post-tokenization) |
| Requires | External VLM + segmentation + depth | Self-contained (single model) |
| Mechanism | Explicit object detection + masking | Learned information bottleneck |
| Efficiency | Heavier (multiple external modules) | Lighter (learned pruning within backbone) |
| Generalization | Limited by VLM grounding accuracy | Limited by IB training distribution |
| Theory | None (engineering pipeline) | Information-theoretic (IB) |

OBEYED-VLA achieves strong clutter robustness but through an expensive external perception pipeline. It validates the core insight that **removing task-irrelevant visual information improves robustness** — the proposed ACIBS would internalize this same principle within the model via learned token pruning.

---

## Summary of Key Distinctions for Your Review

1. **The negative papers (2601.21531, 2601.12042) study post-hoc compression under adversarial attack** — they do NOT study trained/adaptive compression, and they do NOT study natural perturbations. Their findings do not contradict the proposed idea.

2. **Strong theoretical and empirical precedent exists** for IB-trained representations improving robustness (DRIBO, BARReL, ROUSER), specifically in visual RL with natural distractions.

3. **DTP is the closest competitor** but is training-free and heuristic-based, making it vulnerable to the same ranking instability that plagues post-hoc methods. The proposed ACIBS with a learned IB objective addresses this by making the pruning criterion itself robust and task-grounded.

4. **OBEYED-VLA validates the pruning-for-robustness hypothesis** at the image level but requires heavy external modules. ACIBS would be an internalized, efficient version operating at the token level.

**The core argument for ACIBS is sound:** the key insight is that *why* and *how* you prune matters enormously. Post-hoc pruning introduces fragile token selection that adversaries can exploit. Trained IB pruning explicitly optimizes for task-relevant information retention, which is fundamentally aligned with robustness to both natural and adversarial perturbations.

Sources:
- [On the Adversarial Robustness of LVLMs under Visual Token Compression](https://arxiv.org/abs/2601.21531)
- [Less Is More — Until It Breaks](https://arxiv.org/abs/2601.12042)
- [DTP: Distracting Token Pruning for VLAs](https://arxiv.org/abs/2601.16065)
- [OBEYED-VLA: Clutter-Robust VLAs through Object-Centric Grounding](https://arxiv.org/html/2512.22519)
- [ROUSER: Learning Robust Representations with Long-Term Information (ICLR 2025)](https://openreview.net/forum?id=PDtMrogheZ)
- [BARReL: Bottleneck Attention for Adversarial Robustness in Visual RL](https://ar5iv.labs.arxiv.org/html/2208.10481)
- [DRIBO: Robust Deep RL via Multi-View Information Bottleneck](https://arxiv.org/abs/2102.13268)
- [Token Reduction Should Go Beyond Efficiency (2025)](https://arxiv.org/html/2505.18227v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4eb7cbbb-38d2-4ad4-b862-9c935d6c53e3",
  "isSidechain": true,
  "agentId": "a12cdb144c85a9795",
  "requestId": "req_011Cb1vMbD22jnHQboDsU4xc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1e55282-7707-438c-a304-5f529de50393",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff6d9a32-54b2-458b-be61-7a2497b3e836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JRXBCVDsBRKtgbZrhRLAKz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 19890,
      "output_tokens": 2712,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1063
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2712,
          "cache_read_input_tokens": 19890,
          "cache_creation_input_tokens": 1063,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1063,
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
