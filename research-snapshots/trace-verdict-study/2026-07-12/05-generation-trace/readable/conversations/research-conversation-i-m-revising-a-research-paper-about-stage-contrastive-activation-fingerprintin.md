# Research conversation: I'm revising a research paper about "Stage-Contrastive Activation Fingerprinting" for benchmark contamination detection.

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 83
- **Recorded user turns:** 1
- **Tool calls:** 37
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a2fba1c8859d87ffe.jsonl`
- **Structured JSON:** [`040f8d348b666fe03446.json`](../../sessions/04/040f8d348b666fe03446.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

83 recorded events

### User

_source line 1 · 2026-05-09T20:56:42.389Z_

I'm revising a research paper about "Stage-Contrastive Activation Fingerprinting" for benchmark contamination detection. The paper claims that SFT (supervised fine-tuning) and RL probe directions are "nearly orthogonal in activation space (cosine ≈ −0.07)" citing "unpublished mechanistic work (pending arXiv)." A reviewer flagged this as an unverifiable citation.

I need you to:
1. Search for published or arXiv papers (2024-2026) that study how different training stages (SFT vs RL/RLHF/DPO) affect activation spaces in language models. Search queries like: "SFT RL activation space orthogonal probe directions", "fine-tuning stages activation geometry LLM", "SFT RLHF activation difference representation space"
2. Search for work on probing different fine-tuning stages of LLMs: "probing SFT vs RLHF representation differences", "activation probing training stages LLM"
3. Use WebFetch to read the abstract and relevant sections of any promising papers found.

Report: (a) What published work, if any, supports or contradicts the claim that SFT and RL produce orthogonal probe directions? (b) Are there any papers that characterize how different post-training stages change activation geometry? (c) What would be a reasonable empirical finding to add as an analysis section in this paper to replace the unverifiable citation?

Be specific about paper titles, arXiv IDs, and relevant findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f665e9e5-0a3b-430d-856f-f79521590172",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "c4d25b11-b067-4aa7-a2e4-d7f2940819ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-09T20:56:42.398Z_

```json
{
  "parentUuid": "c4d25b11-b067-4aa7-a2e4-d7f2940819ca",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "565bc938-474d-4fdf-bff2-a35b85029643",
  "timestamp": "2026-05-09T20:56:42.398Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-09T20:56:44.267Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ReDbE3XZUNaAWYA8HazAaP`</summary>

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
  "parentUuid": "565bc938-474d-4fdf-bff2-a35b85029643",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfRbVxuE6ma3uBY4s9X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df9ae6ce-13ac-4e34-bf26-8fae1cc223ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01X66hbtQ4WR5tZ3LfrG8Hby",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8106,
      "cache_read_input_tokens": 0,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8106
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 8106,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8106,
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

_source line 4 · 2026-05-09T20:56:44.270Z_

<details><summary>↩ Tool result · `toolu_01ReDbE3XZUNaAWYA8HazAaP`</summary>

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
  "parentUuid": "df9ae6ce-13ac-4e34-bf26-8fae1cc223ea",
  "isSidechain": true,
  "promptId": "f665e9e5-0a3b-430d-856f-f79521590172",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "d9446401-6f30-4fad-aa4c-0807204ca07f",
  "sourceToolAssistantUUID": "df9ae6ce-13ac-4e34-bf26-8fae1cc223ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-09T20:56:47.515Z_

I'll run multiple searches in parallel to cover the different angles of this question.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9446401-6f30-4fad-aa4c-0807204ca07f",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfRjj4sWdSpMshXvVWt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9df880eb-a3b0-4857-b89f-b598d5705066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AqPpX5jdKKf4g9hY7ps2zm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8106,
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

_source line 6 · 2026-05-09T20:56:48.464Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XubZrLUajJPRKtQnK2hB1N`</summary>

```json
{
  "query": "SFT RL activation space orthogonal probe directions LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9df880eb-a3b0-4857-b89f-b598d5705066",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfRjj4sWdSpMshXvVWt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30c05e99-b73e-4110-ac62-25d498462404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AqPpX5jdKKf4g9hY7ps2zm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8106,
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

_source line 7 · 2026-05-09T20:56:49.985Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UYkrSYeso61VzzZavZEzEK`</summary>

```json
{
  "query": "fine-tuning stages activation geometry language model SFT RLHF representation space 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30c05e99-b73e-4110-ac62-25d498462404",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfRjj4sWdSpMshXvVWt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32da085a-b0ef-4296-a8c2-a98b8c469438",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AqPpX5jdKKf4g9hY7ps2zm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8106,
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

_source line 8 · 2026-05-09T20:56:50.046Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qt3ncu2SKQAr3rijp1qMXr`</summary>

```json
{
  "query": "probing SFT vs RLHF representation differences activation space arXiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32da085a-b0ef-4296-a8c2-a98b8c469438",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfRjj4sWdSpMshXvVWt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5153d09-e867-4250-ad19-5077342d94b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AqPpX5jdKKf4g9hY7ps2zm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1888,
      "cache_read_input_tokens": 8106,
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

### Tool result

_source line 9 · 2026-05-09T20:56:55.621Z_

<details><summary>↩ Tool result · `toolu_01XubZrLUajJPRKtQnK2hB1N`</summary>

```text
Web search results for query: "SFT RL activation space orthogonal probe directions LLM 2024 2025"

Links: [{"title":"Beyond Two-Stage Training: Cooperative SFT and RL for LLM Reasoning","url":"https://arxiv.org/pdf/2509.06948"},{"title":"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs","url":"https://arxiv.org/html/2508.16546v1"},{"title":"RL Squeezes, SFT Expands: A Comparative Study of Reasoning LLMs","url":"https://arxiv.org/html/2509.21128v1"},{"title":"On the Generalization of SFT: A Reinforcement Learning ...","url":"https://arxiv.org/pdf/2508.05629"},{"title":"SFT or RL? An Early Investigation into Training R1-Like Reasoning Large Vision-Language Models","url":"https://arxiv.org/html/2504.11468v1"},{"title":"SFT or RL? An Early Investigation into Training R1-Like Reasoning Large Vision-Language Models | OpenReview","url":"https://openreview.net/forum?id=wZI5qkQeDF"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=SFT"},{"title":"RL Fine-Tuning Heals OOD Forgetting in SFT","url":"https://arxiv.org/html/2509.12235v2"},{"title":"Seeking arXiv cs.LG endorsement for paper on probe transfer failure in reward hacking detection - Research - Hugging Face Forums","url":"https://discuss.huggingface.co/t/seeking-arxiv-cs-lg-endorsement-for-paper-on-probe-transfer-failure-in-reward-hacking-detection/174565"},{"title":"RL Is Neither a Panacea Nor a Mirage:","url":"https://arxiv.org/pdf/2508.16546"}]

I found several highly relevant papers on this topic. Here are the key findings:

## Key Research Results

Recent research tracks geometric shifts in parameter space across SFT and RL phases, finding that OOD performance degradation and recovery correlate almost entirely with rotations of singular vectors at the spectrum's extremes, with directional shifts in the extremal components, rather than magnitude shifts, governing model performance.

A particularly relevant finding relates directly to your query: The SFT and RL probe directions are nearly orthogonal, with a cosine similarity of -0.07. This suggests that the activation space directions learned during SFT and RL phases are nearly perpendicular to each other.

The model's intrinsic capacity, reflected in the bulk of spectral density, remains essentially constant throughout training, while OOD performance changes correlate almost entirely with rotations of singular vectors at the spectrum's extremes.

## Main Themes in Recent Research (2024-2025)

Several papers examine the comparative effects of SFT and RL on LLM training:

- RL substantially mitigates OOD performance decay from SFT, restoring up to 99% of lost OOD performance while maintaining strong in-distribution competence, suggesting that RL plays a restoration role rather than endowing fundamentally new capabilities.

- Research suggests that the empirical finding SFT memorizes and RL generalizes may be related to RL's aggregation and SFT's distribution of reasoning functionalities.

The papers indicate active research into understanding how probe directions and activation spaces differ between SFT and RL phases, with evidence of orthogonality in these directions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30c05e99-b73e-4110-ac62-25d498462404",
  "isSidechain": true,
  "promptId": "f665e9e5-0a3b-430d-856f-f79521590172",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "9b0c91ee-bd28-4681-be5e-d30aee9d647c",
  "sourceToolAssistantUUID": "30c05e99-b73e-4110-ac62-25d498462404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-09T20:56:57.476Z_

<details><summary>↩ Tool result · `toolu_01Qt3ncu2SKQAr3rijp1qMXr`</summary>

```text
Web search results for query: "probing SFT vs RLHF representation differences activation space arXiv 2024 2025"

Links: [{"title":"Continual SFT Matches Multimodal RLHF with Negative Supervision","url":"https://arxiv.org/html/2411.14797v1"},{"title":"[2502.11026] RLHF in an SFT Way: From Optimal Solution to Reward-Weighted Alignment","url":"https://arxiv.org/abs/2502.11026"},{"title":"RLSR: Reinforcement Learning with Supervised Reward Outperforms SFT in Instruction Following","url":"https://arxiv.org/html/2510.14200v1"},{"title":"Intuitive Fine-Tuning: Towards Unifying SFT and RLHF into a Single Process","url":"https://arxiv.org/html/2405.11870v1"},{"title":"[2411.14797] Continual SFT Matches Multimodal RLHF with Negative Supervision","url":"https://arxiv.org/abs/2411.14797"},{"title":"On the Generalization of SFT: A Reinforcement Learning ...","url":"https://arxiv.org/pdf/2508.05629"},{"title":"Quagmires in SFT-RL Post-Training: When High SFT Scores Mislead and What to Use Instead","url":"https://arxiv.org/html/2510.01624v1"},{"title":"On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification","url":"https://arxiv.org/html/2508.05629v2"},{"title":"SFT or RL? An Early Investigation into Training R1-Like Reasoning Large Vision-Language Models","url":"https://arxiv.org/html/2504.11468v1"},{"title":"RLHF in an SFT Way: From Optimal Solution to Reward-Weighted Alignment","url":"https://arxiv.org/html/2502.11026v3"}]

I've completed the web search for your query about probing SFT vs RLHF representation differences in activation space from arXiv 2024-2025. Here's a summary of the most relevant results:

## Key Findings:

The search returned several recent arXiv papers comparing SFT (Supervised Fine-Tuning) and RLHF (Reinforcement Learning from Human Feedback), though most focus on performance comparisons rather than specifically probing activation space differences:

1. **Theoretical Connections Between SFT and RLHF**: Recent work reinterprets RLHF as a reward-weighted variant of SFT, while other research shows that SFT can be cast as RL with an implicit reward.

2. **SFT vs RL Generalization**: SFT often shows limited generalization compared to reinforcement learning, while RL leverages explicit reward or verification signals to explore diverse strategies and thus generalizes better.

3. **Representation and Behavioral Differences**: One study found that self-reflection thinking from the SFT process becomes overloaded with excessive and irrelevant reasoning, creating "pseudo aha moments" that hurt performance.

4. **Negative Supervision in Multimodal Settings**: Research observed that the inherent value of multimodal RLHF lies in its negative supervision, proposing a negative supervised finetuning approach that excavates this information and aligns models with a simple SFT loss.

The papers suggest fundamental differences in how these methods shape model representations and behavior, though a paper specifically focused on detailed activation space probing may not have appeared in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5153d09-e867-4250-ad19-5077342d94b4",
  "isSidechain": true,
  "promptId": "f665e9e5-0a3b-430d-856f-f79521590172",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "cfc55e58-8754-4465-b1c5-6a5b5dc731d0",
  "sourceToolAssistantUUID": "e5153d09-e867-4250-ad19-5077342d94b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-09T20:56:58.267Z_

<details><summary>↩ Tool result · `toolu_01UYkrSYeso61VzzZavZEzEK`</summary>

```text
Web search results for query: "fine-tuning stages activation geometry language model SFT RLHF representation space 2024 2025"

Links: [{"title":"Understanding and Using Supervised Fine-Tuning (SFT) for Language Models","url":"https://cameronrwolfe.substack.com/p/understanding-and-using-supervised"},{"title":"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs","url":"https://arxiv.org/html/2508.16546v1"},{"title":"On the Generalization of SFT: A Reinforcement Learning ...","url":"https://arxiv.org/pdf/2508.05629"},{"title":"preserving diversity in supervised fine-tuning","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf"},{"title":"Systems Opportunities for LLM Fine-Tuning using ...","url":"https://dl.acm.org/doi/pdf/10.1145/3721146.3721944"},{"title":"Intuitive Fine-Tuning: Towards Unifying SFT and RLHF into a Single Process","url":"https://arxiv.org/html/2405.11870v1"},{"title":"Getting More Juice Out of the SFT Data: Reward Learning ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/e0c9b65fb3e41aaa86576df3ec33ad2e-Paper-Conference.pdf"},{"title":"Fine-Tuning Language Models with Reward Learning on ...","url":"https://aclanthology.org/2024.naacl-long.75.pdf"},{"title":"Preventing Safety Drift in Large Language Models via Coupled Weight and Activation Constraints","url":"https://arxiv.org/html/2604.12384v1"},{"title":"RL Fine-Tuning of Language Models CS 224R Default Project Specification","url":"https://cs224r.stanford.edu/material/CS224R_Default_Project_Guidelines.pdf"}]

Based on the web search results, here are findings related to fine-tuning stages, activation geometry, and representation space in language models from 2024-2025:

## Key Research Findings

**SFT and RLHF in Two-Stage Post-Training:**

Recent research tracks geometric shifts in parameter space across the SFT phase and the subsequent RL phase. The model's intrinsic capacity, reflected in the bulk of the spectral density, remains essentially constant throughout training, while OOD performance degradation and its later recovery correlate almost entirely with rotations of the singular vectors at the spectrum's extremes, with the corresponding singular values changing little.

**Directional Shifts Over Magnitude Changes:**

Directional shifts in the extremal components, rather than magnitude shifts, govern model's performance. This finding contrasts with earlier work emphasizing the absolute size of singular values.

**RL as Memory Restoration:**

The subsequent RL stage substantially mitigates OOD decay, restoring up to 99% of the OOD performance lost during SFT for Qwen-2.5-7B and up to 85% for Llama-3.2-11B. RL does not endow fundamentally new capabilities; instead, it plays a restoration role that recovers general competencies compromised by aggressive SFT.

**Diversity Preservation in SFT:**

Standard SFT practices—particularly the use of CE loss—often reduces diversity, leading to knowledge forgetting and aligning with the "alignment tax" phenomenon.

**Safety Alignment and Fine-Tuning:**

Fine-tuning-stage defenses typically constrain weight-level updates or regularize activation-level critical pathways, highlighting the importance of representation-level considerations during fine-tuning stages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32da085a-b0ef-4296-a8c2-a98b8c469438",
  "isSidechain": true,
  "promptId": "f665e9e5-0a3b-430d-856f-f79521590172",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "f9f412e8-b4b6-4068-a0d8-67fcf9e34f4d",
  "sourceToolAssistantUUID": "32da085a-b0ef-4296-a8c2-a98b8c469438",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-09T20:57:00.177Z_

Good. Now let me fetch the most relevant papers directly to get concrete findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9f412e8-b4b6-4068-a0d8-67fcf9e34f4d",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfSmM5F9JxDSskR7YWb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d129d2b0-444d-45c5-8957-e2fe084f9990",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CMsYuGAuNCrkEvi9aTYsxW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 2108,
      "cache_read_input_tokens": 9994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2108,
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

_source line 13 · 2026-05-09T20:57:01.933Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NYQLSY8i897VnK6W4WHYuf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.16546",
  "prompt": "Extract the abstract, key findings about activation space geometry, singular vectors, probe directions, and any quantitative claims about SFT vs RL representation differences. Note the paper title, authors, and arXiv ID."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d129d2b0-444d-45c5-8957-e2fe084f9990",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfSmM5F9JxDSskR7YWb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58dc089a-11d9-42af-bd7d-96c6f86c5d0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CMsYuGAuNCrkEvi9aTYsxW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 2108,
      "cache_read_input_tokens": 9994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2108,
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

_source line 14 · 2026-05-09T20:57:02.907Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013vC8tqeV7y4KnPTFcDBWAo`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.21128",
  "prompt": "Extract the abstract, key findings about activation space geometry, representation differences between SFT and RL, and any quantitative claims. Note the paper title, authors, and arXiv ID."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58dc089a-11d9-42af-bd7d-96c6f86c5d0e",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfSmM5F9JxDSskR7YWb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47b55b61-514a-4cab-9cd5-f6ea3f6d46b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CMsYuGAuNCrkEvi9aTYsxW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 2108,
      "cache_read_input_tokens": 9994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2108,
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

_source line 15 · 2026-05-09T20:57:03.452Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MxePNEpoXvPhAdqQ6QDT6P`</summary>

```json
{
  "query": "activation space probe direction cosine similarity SFT RLHF DPO post-training LLM arXiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47b55b61-514a-4cab-9cd5-f6ea3f6d46b4",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfSmM5F9JxDSskR7YWb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "341907f0-cfc6-40c9-a0dd-75fd6fa108b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CMsYuGAuNCrkEvi9aTYsxW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 929,
      "cache_creation_input_tokens": 2108,
      "cache_read_input_tokens": 9994,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2108
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 929,
          "output_tokens": 314,
          "cache_read_input_tokens": 9994,
          "cache_creation_input_tokens": 2108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2108,
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

_source line 16 · 2026-05-09T20:57:07.526Z_

<details><summary>↩ Tool result · `toolu_01NYQLSY8i897VnK6W4WHYuf`</summary>

```text
# Paper Summary

**Title:** RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs

**ArXiv ID:** 2508.16546

**Authors:** Hangzhan Jin, Sicheng Lv, Sifan Wu, Mohammad Hamdaqa

**Submission Date:** August 22, 2025

## Abstract

The authors investigate how supervised fine-tuning (SFT) and reinforcement learning fine-tuning (RL-FT) reshape LLM representations using an out-of-distribution card game task and spectrum-based diagnostics.

## Key Findings on Activation Space Geometry

**Singular Vectors & Directional Shifts:**
The research reveals that "direction shifts of singular vectors matter more than singular value magnitudes." These directional changes concentrate specifically on dimensions linked to the largest and smallest singular values, while the broader spectrum remains relatively stable.

**Low-Rank Recovery:**
A notable efficiency finding indicates that "restoring singular vector directions for the top 20% of values or first 25% of layers recovers 70-80% of OOD performance."

**RL's Mechanism:**
Rather than discovering novel solutions, "RL primarily counteracts SFT-induced directional drift" in the representation space.

## Quantitative Claims

- Llama-11B: OOD performance improves from 8.97% to 15.38% through RL
- Qwen-7B: Recovery from 17.09% to 19.66% via RL-FT
- RL cannot fully recover performance when severe overfitting occurs with clear distribution shifts
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58dc089a-11d9-42af-bd7d-96c6f86c5d0e",
  "isSidechain": true,
  "promptId": "f665e9e5-0a3b-430d-856f-f79521590172",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "3c72fa3c-82e4-4de0-88bb-7b51077a36c9",
  "sourceToolAssistantUUID": "58dc089a-11d9-42af-bd7d-96c6f86c5d0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-09T20:57:08.634Z_

<details><summary>↩ Tool result · `toolu_013vC8tqeV7y4KnPTFcDBWAo`</summary>

```text
# Paper Summary: RL Squeezes, SFT Expands

**Title:** RL Squeezes, SFT Expands: A Comparative Study of Reasoning LLMs

**arXiv ID:** 2509.21128

**Authors:** Kohsei Matsutani, Shota Takashiro, Gouki Minegishi, Takeshi Kojima, Yusuke Iwasawa, Yutaka Matsuo

**Submission Date:** September 25, 2025

---

## Abstract

The paper investigates how reinforcement learning with verifiable rewards (RLVR) and supervised fine-tuning (SFT) differently shape reasoning in language models (1.5B-14B parameters) on mathematical tasks through a novel analysis framework examining reasoning paths.

---

## Key Findings

**Trajectory-Level Effects:**
- "RL compresses incorrect trajectories, whereas SFT expands correct ones"—demonstrating complementary mechanisms between the two training approaches

**Step-Level Analysis:**
- RL increases decay rates approximately 2.5-fold in node visitation frequency, degree, and betweenness centrality distributions
- SFT reduces these decay rates to roughly one-third, creating flatter distributions
- This indicates RL concentrates reasoning into fewer critical steps, while SFT distributes functionality across many steps

**Practical Implications:**
The analysis explains why sequential SFT-then-RL training succeeds and provides insights for data construction and more efficient learning strategies.

---

## Note on Activation Space Geometry

The provided content does not contain specific information about activation space geometry or representation differences between methods. The analysis focuses on reasoning graph topology and trajectory clustering rather than neural representation analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47b55b61-514a-4cab-9cd5-f6ea3f6d46b4",
  "isSidechain": true,
  "promptId": "f665e9e5-0a3b-430d-856f-f79521590172",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "a730275a-cb77-454a-b7dd-7a9d5154c198",
  "sourceToolAssistantUUID": "47b55b61-514a-4cab-9cd5-f6ea3f6d46b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-09T20:57:11.126Z_

<details><summary>↩ Tool result · `toolu_01MxePNEpoXvPhAdqQ6QDT6P`</summary>

```text
Web search results for query: "activation space probe direction cosine similarity SFT RLHF DPO post-training LLM arXiv 2024 2025"

Links: [{"title":"Probe-Based Data Attribution: Discovering and Mitigating Undesirable","url":"https://arxiv.org/pdf/2602.11079"},{"title":"Probe-Based Data Attribution: Discovering and Mitigating Undesirable Behaviors in LLM Post-Training","url":"https://arxiv.org/html/2602.11079"},{"title":"Quagmires in SFT-RL Post-Training: When High SFT Scores Mislead and What to Use Instead","url":"https://arxiv.org/html/2510.01624v1"},{"title":"Published as a conference paper at ICLR 2025 ASYNCHRONOUS RLHF: FASTER AND MORE","url":"https://openreview.net/pdf?id=FhTAG591Ve"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=WjKea8bGFF"},{"title":"[2503.10460] Light-R1: Curriculum SFT, DPO and RL for Long COT from Scratch and Beyond","url":"https://arxiv.org/abs/2503.10460"},{"title":"LLMOrbit: A Circular Taxonomy of Large Language Models","url":"https://arxiv.org/pdf/2601.14053"},{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2504.02904"},{"title":"A First-Order Logic–Based Alternative to Reward Models in RLHF","url":"https://arxiv.org/html/2512.14100v1"},{"title":"On the Generalization of SFT: A Reinforcement Learning ...","url":"https://arxiv.org/pdf/2508.05629"}]

I've found several highly relevant papers on arXiv from 2024-2025 related to your search query. Here are the most relevant results:

## Primary Results:

**1. Probe-Based Data Attribution (2025)** - This paper projects behavior changes and training datapoints into a common space for comparison through vector similarity, using cosine similarities between behavior change vectors and datapoint vectors. The work directly addresses activation-space probing in the context of LLM post-training methods (SFT, DPO, RLHF).

**2. Mechanistic Study of Post-Training (COLM 2025)** - This paper studies direction-based interventions in model activations, using truthfulness directions from one model to intervene in another, by adding these representations at specific layers. It compares BASE, SFT, and INSTRUCT models across multiple perspectives.

## Other Relevant Papers:

**3. Light-R1: Curriculum SFT, DPO and RL (March 2025)** - This paper introduces an open-source suite for training long reasoning models using curriculum training that progressively increases data difficulty, combined with multi-staged post-training.

**4. Quagmires in SFT-RL Post-Training (October 2024)** - Discusses the dynamics and interactions between SFT and RL stages in reasoning model post-training.

**5. LLMOrbit: A Circular Taxonomy (2025)** - Provides insight into key post-training techniques including RLHF, PPO, DPO, GRPO, and ORPO.

The first two papers appear most directly aligned with your query about activation space, probes, direction, and cosine similarity in the context of post-training methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "341907f0-cfc6-40c9-a0dd-75fd6fa108b8",
  "isSidechain": true,
  "promptId": "f665e9e5-0a3b-430d-856f-f79521590172",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "6fbca475-7bc9-4c23-be4f-fb53817ba800",
  "sourceToolAssistantUUID": "341907f0-cfc6-40c9-a0dd-75fd6fa108b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-09T20:57:14.242Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011DNS9HapUPLvfSUcv6fjfR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.11079",
  "prompt": "Extract the abstract, methods, and key findings about activation space probing, probe directions, cosine similarity between probes for different training stages (SFT, RLHF, DPO), and any quantitative claims about representation geometry differences between training stages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fbca475-7bc9-4c23-be4f-fb53817ba800",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfTiM2WFpaacFpCRmzU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3764828d-2d31-4984-85a8-df6004a3f240",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Y9KyNKfd9keS2UxnkadMxX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3006,
      "cache_read_input_tokens": 12102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3006,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-09T20:57:15.534Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X8gkJLBqTo2CwihEWwHTkH`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.02904",
  "prompt": "Extract the abstract, methods, and key findings about activation space probing, probe directions, cosine similarity, differences between SFT/RLHF/DPO representations. Note the paper title, authors, and arXiv ID."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3764828d-2d31-4984-85a8-df6004a3f240",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfTiM2WFpaacFpCRmzU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1106bdd3-ba01-49c6-9dfc-e81d60d521f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Y9KyNKfd9keS2UxnkadMxX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3006,
      "cache_read_input_tokens": 12102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3006,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 60,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-09T20:57:16.429Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fzf2vmiZ2SUsVWHCXQxUAF`</summary>

```json
{
  "query": "\"linear probe\" \"training stage\" LLM activation representation \"SFT\" \"RLHF\" orthogonal cosine arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1106bdd3-ba01-49c6-9dfc-e81d60d521f9",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfTiM2WFpaacFpCRmzU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61a844bd-341e-4514-9a87-fded79a2113d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Y9KyNKfd9keS2UxnkadMxX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3006,
      "cache_read_input_tokens": 12102,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3006
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 320,
          "cache_read_input_tokens": 12102,
          "cache_creation_input_tokens": 3006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3006,
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

_source line 22 · 2026-05-09T20:57:19.580Z_

<details><summary>↩ Tool result · `toolu_011DNS9HapUPLvfSUcv6fjfR`</summary>

```text
# Paper Analysis: Probe-Based Data Attribution

## Abstract Summary
The researchers introduced a technique for identifying which training datapoints cause specific behaviors in language models. Their approach compares "activation-difference vectors for both test prompts and preference pairs and ranking by cosine similarity" to pinpoint responsible data.

## Methods Overview
The methodology involves:
- Computing activation differences between model states
- Ranking datapoints using cosine similarity measurements
- Validating findings through controlled retraining experiments
- Using clustering on behavior-datapoint similarity matrices for unsupervised discovery

## Key Findings

**Discovered Behavior:** The team surfaced "distractor-triggered compliance: a harmful behavior where the model complies with dangerous requests when benign formatting instructions are appended."

**Mitigation Results:** 
- Filtering problematic datapoints reduced harmful behavior by **63%**
- Switching labels on top-ranked datapoints achieved **78%** reduction

**Performance Claims:** The method "outperforms gradient-based attribution and LLM-judge baselines while being over 10 times cheaper than both."

## Representation Geometry Insights
The paper does not explicitly present quantitative claims comparing representation geometry across SFT, RLHF, and DPO training stages in the available abstract. The focus centers on identifying and mitigating specific behaviors through datapoint attribution rather than analyzing cross-stage geometric differences.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3764828d-2d31-4984-85a8-df6004a3f240",
  "isSidechain": true,
  "promptId": "f665e9e5-0a3b-430d-856f-f79521590172",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "0cff6198-0818-4482-9453-c18ac6083a2f",
  "sourceToolAssistantUUID": "3764828d-2d31-4984-85a8-df6004a3f240",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-09T20:57:20.474Z_

<details><summary>↩ Tool result · `toolu_01X8gkJLBqTo2CwihEWwHTkH`</summary>

```text
# Paper Summary

**Title:** How Post-Training Reshapes LLMs: A Mechanistic View on Knowledge, Truthfulness, Refusal, and Confidence

**ArXiv ID:** 2504.02904

**Authors:** Hongzhe Du, Weikai Li, Min Cai, Karim Saraipour, Zimin Zhang, Himabindu Lakkaraju, Yizhou Sun, Shichang Zhang

## Abstract

The research examines how post-training internally transforms language models by comparing base and post-trained versions mechanistically across four dimensions.

## Key Findings

**Knowledge Representation:** Post-training preserves the original storage locations for factual knowledge while simultaneously adapting existing representations and generating novel ones.

**Truthfulness & Refusal Directions:** Both behaviors "can be represented by vectors in the hidden representation space." Truthfulness directions remain remarkably consistent between base and post-trained models with strong transferability for interventions. By contrast, refusal directions diverge significantly and demonstrate limited forward transferability across model versions.

**Confidence Mechanisms:** Changes in model confidence between base and post-trained variants cannot be explained by entropy neuron activity.

## Methodology Note

The abstract indicates mechanistic analysis comparing model families and datasets, though specific technical details about activation space probing, probe directions, or cosine similarity measurements aren't elaborated in the provided content excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1106bdd3-ba01-49c6-9dfc-e81d60d521f9",
  "isSidechain": true,
  "promptId": "f665e9e5-0a3b-430d-856f-f79521590172",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "badf0045-f2ef-4213-bd5f-b13d1393263e",
  "sourceToolAssistantUUID": "1106bdd3-ba01-49c6-9dfc-e81d60d521f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-09T20:57:22.648Z_

<details><summary>↩ Tool result · `toolu_01Fzf2vmiZ2SUsVWHCXQxUAF`</summary>

```text
Web search results for query: ""linear probe" "training stage" LLM activation representation "SFT" "RLHF" orthogonal cosine arXiv"

Links: [{"title":"Exploring the LLM Journey from Cognition to Expression with Linear Representations","url":"https://arxiv.org/html/2405.16964"},{"title":"Revisiting Pre-training Period of Large Language Models","url":"https://aclanthology.org/2024.findings-acl.290.pdf"},{"title":"The 3 Stages of LLM Training: A Deep Dive into Reinforcement Learning from Human Feedback (RLHF) - DataSci Ocean","url":"https://datasciocean.com/en/ai-concept/llm-fine-tuning-rlhf/"},{"title":"LLM Training: RLHF and Its Alternatives - Ahead of AI","url":"https://magazine.sebastianraschka.com/p/llm-training-rlhf-and-its-alternatives"},{"title":"Building an RLHF Pipeline for LLMs: A Beginner-Friendly Tutorial | by Vi Q. Ha | Medium","url":"https://medium.com/@vi.ha.engr/building-an-rlhf-pipeline-for-llms-a-beginner-friendly-tutorial-21112bfcff9b"},{"title":"GitHub - michaelnny/InstructLLaMA: Implements pre-training, supervised fine-tuning (SFT), and reinforcement learning from human feedback (RLHF), to train and fine-tune the LLaMA2 model to follow human instructions, similar to InstructGPT or ChatGPT, but on a much smaller scale. · GitHub","url":"https://github.com/michaelnny/InstructLLaMA"},{"title":"SFT vs. RLHF: Choose the Right Approach to Train Your LLM","url":"https://invisibletech.ai/blog/supervised-fine-tuning-vs-rlhf-how-to-choose-the-right-approach-to-train-your-llm"},{"title":"RLHF Pipeline for Clinical LLMs: An Implementation Guide | IntuitionLabs","url":"https://intuitionlabs.ai/articles/rlhf-pipeline-clinical-llms"},{"title":"GitHub - Mattral/LLM-Improving-Trained-Models-with-RLHF: Experimented with the three essential Reinforcement Learning with Human Feedback (RLHF) process stages. It starts by revisiting the Supervised Fine-Tuning (SFT) process, then proceeds with the training of a reward model, and finally concludes with the reinforcement learning phase. We explored and applied methods such as 4-bit quantization and LoRA · GitHub","url":"https://github.com/Mattral/LLM-Improving-Trained-Models-with-RLHF"},{"title":"Reinforcement Learning From Human Feedback (RLHF) | by Naren Suri | Medium","url":"https://medium.com/@SuriNaren/reinforcement-learning-from-human-feedback-rlhf-8ab957750ac8"}]

I found relevant search results. The first result is particularly pertinent to your query - it's an arXiv paper from November 2024 titled "Exploring the LLM Journey from Cognition to Expression with Linear Representations" that directly addresses your interests.

This paper presents an in-depth examination of the evolution of cognitive and expressive capabilities in large language models, exploring the model's cognitive and expressive capabilities through linear representations across three critical phases: Pretraining, Supervised Fine-Tuning (SFT), and Reinforcement Learning from Human Feedback (RLHF).

The research specifically examines how the discrepancy between capabilities may stem from differences in linear separability between the embedding space of neuron output and the token-level semantic space. From the standpoint of the LLM's architecture, the diminution of this gap during the SFT/RLHF stage could be attributed to enhancements in the vocabulary linear layer at this phase.

The paper also reveals: Cognitive capability is primarily established during the Pretraining stage, whereas expressive capability is developed during the SFT and RLHF stages, with SFT playing a more significant role.

The full paper is available at: https://arxiv.org/html/2405.16964

The second result also mentions linear probing approaches for analyzing LLMs across different trustworthiness dimensions during pre-training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61a844bd-341e-4514-9a87-fded79a2113d",
  "isSidechain": true,
  "promptId": "f665e9e5-0a3b-430d-856f-f79521590172",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "9e82624f-5101-487e-bedc-54d7027f6d65",
  "sourceToolAssistantUUID": "61a844bd-341e-4514-9a87-fded79a2113d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-09T20:57:26.160Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0165tY94Hb4AHDUM7hUHaasQ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2405.16964",
  "prompt": "Extract the abstract, methodology, and key findings about how SFT and RLHF affect activation space geometry, linear probe directions, and any quantitative measurements of cosine similarity or orthogonality between probes from different training stages. Note paper title, authors, arXiv ID."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e82624f-5101-487e-bedc-54d7027f6d65",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfUZZxajmFDLjTg6udo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "624792f6-2f7b-4553-9918-8dd34b7d3e92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RGj4R2MU1YMxHho6QkxLMY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2228,
      "cache_read_input_tokens": 15108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2228,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-09T20:57:27.013Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UKePCWAuq6Tqqx379vfsc3`</summary>

```json
{
  "query": "benchmark contamination detection activation fingerprinting probe training stage LLM 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "624792f6-2f7b-4553-9918-8dd34b7d3e92",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfUZZxajmFDLjTg6udo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80041860-4fdd-439a-ad5a-f6a0d667bb22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RGj4R2MU1YMxHho6QkxLMY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2228,
      "cache_read_input_tokens": 15108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2228,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-09T20:57:27.701Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016WZjevuXvhFumAumE2rhvN`</summary>

```json
{
  "query": "\"representation geometry\" \"post-training\" LLM \"cosine similarity\" probes SFT RL directions hidden states 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80041860-4fdd-439a-ad5a-f6a0d667bb22",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfUZZxajmFDLjTg6udo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1617c49-ec44-4e7f-b953-8dc958a4fb1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RGj4R2MU1YMxHho6QkxLMY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2228,
      "cache_read_input_tokens": 15108,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2228
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 268,
          "cache_read_input_tokens": 15108,
          "cache_creation_input_tokens": 2228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2228,
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

_source line 28 · 2026-05-09T20:57:31.099Z_

<details><summary>↩ Tool result · `toolu_0165tY94Hb4AHDUM7hUHaasQ`</summary>

```text
# Paper Summary

**Title:** Exploring the LLM Journey from Cognition to Expression with Linear Representations

**Authors:** Yuzi Yan, Jialian Li, Yipin Zhang, Dong Yan

**arXiv ID:** 2405.16964

## Abstract
The research examines how cognitive and expressive capabilities develop across training phases in large language models, specifically Baichuan-7B and Baichuan-33B. The authors define "cognitive capability" as information conveyed through neuron output vectors and "expressive capability" as word-level output production.

## Key Findings

**Developmental Pattern:** The study reveals that "cognitive abilities are largely established during Pretraining, whereas expressive abilities predominantly advance during SFT and RLHF."

**Correlation:** Statistical analyses demonstrate significant correlation between cognitive and expressive capabilities, suggesting cognitive capacity may constrain expressive potential.

**Training Phase Effects:**
- **Pretraining:** Establishes foundational cognitive abilities
- **SFT and RLHF:** Drive advancement in expressive capabilities

**Bridging Strategies:** The research evaluates optimization-independent approaches including few-shot learning and repeated sampling as methods to reduce gaps between cognitive and expressive capabilities.

## Note
The abstract provided does not include specific quantitative measurements of cosine similarity, orthogonality metrics, or detailed activation space geometry analysis. These details would require access to the full paper text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "624792f6-2f7b-4553-9918-8dd34b7d3e92",
  "isSidechain": true,
  "promptId": "f665e9e5-0a3b-430d-856f-f79521590172",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "0d8a7783-3873-49ad-83b0-451122e13000",
  "sourceToolAssistantUUID": "624792f6-2f7b-4553-9918-8dd34b7d3e92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-09T20:57:33.908Z_

<details><summary>↩ Tool result · `toolu_01UKePCWAuq6Tqqx379vfsc3`</summary>

```text
Web search results for query: "benchmark contamination detection activation fingerprinting probe training stage LLM 2024 2025 arXiv"

Links: [{"title":"arXiv:2502.14425v2 [cs.CL] 5 Jun 2025","url":"https://arxiv.org/pdf/2502.14425"},{"title":"A Comprehensive Survey of Contamination Detection Methods in Large Language Models","url":"https://arxiv.org/html/2404.00699v4"},{"title":"Detecting Benchmark Contamination Through Watermarking","url":"https://arxiv.org/html/2502.17259"},{"title":"livebench:achallenging, contamination-limited llm benchmark","url":"https://arxiv.org/pdf/2406.19314"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/html/2601.19334v1"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/html/2510.09259"},{"title":"A Comprehensive Survey of Contamination Detection Meth","url":"https://arxiv.org/pdf/2404.00699"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/html/2502.14425v2"},{"title":"[2404.00699] A Comprehensive Survey of Contamination Detection Methods in Large Language Models","url":"https://arxiv.org/abs/2404.00699"}]

I found several relevant arXiv papers on benchmark contamination detection in large language models from 2024-2025. Here are the key findings:

## Main Research Areas:

**1. Activation-Based Fingerprinting and Probe Training:**

Liu et al. (2024) developed a method that fine-tunes an LLM to classify membership between members and non-members, then uses activations of intermediate layers of the fine-tuned LLM on both members and non-members as input of a probe classifier assessing membership. The best layer to extract activation from is determined on a validation set, with results showing greater ROC-AUC on WikiMIA and ArxivMIA, indicating that this probing system works better with larger models.

**2. Training Stage Impact:**

Kocyigit et al. (2025) found that the training stage at which contamination occurs plays a crucial role in its impact, with early contamination leading to a sharp initial performance increase, but this effect gradually diminishing as training progresses.

**3. In-Distribution Contamination Detection:**

Tu et al. (2024) proposed DICE to detect in-distribution contamination during fine-tuning by analyzing layer-specific activation patterns.

**4. Watermarking Approaches:**

Contamination detection remains strong and reliable when different tokenizers are used by the suspect model, with performance metrics and contamination detection capabilities tested on models pre-trained with various tokenizers both with and without contamination on MMLU.

The search results reveal a comprehensive research landscape focused on detecting benchmark contamination through various technical approaches including activation analysis, membership inference attacks, and watermarking methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80041860-4fdd-439a-ad5a-f6a0d667bb22",
  "isSidechain": true,
  "promptId": "f665e9e5-0a3b-430d-856f-f79521590172",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "c5d82d30-3791-4ca9-a617-34a20421b128",
  "sourceToolAssistantUUID": "80041860-4fdd-439a-ad5a-f6a0d667bb22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-09T20:57:36.622Z_

<details><summary>↩ Tool result · `toolu_016WZjevuXvhFumAumE2rhvN`</summary>

```text
Web search results for query: ""representation geometry" "post-training" LLM "cosine similarity" probes SFT RL directions hidden states 2024 2025"

Links: [{"title":"The Linear Representation Hypothesis and the Geometry of Large Language Models","url":"https://arxiv.org/html/2311.03658v2"},{"title":"Tracing the Representation Geometry of Language Models from Pretraining to Post-training","url":"https://arxiv.org/html/2509.23024"},{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2504.02904"},{"title":"Tracing the Representation Geometry of Language Models from Pretraining to Post-training - Li et al. | Academic Research","url":"https://melodylizx.github.io/llm-geometry-project/"},{"title":"Hidden-State Signals in Iterative LLM Repair: What Cosine Similarity at Layer 27 Actually Tells You - Research - Hugging Face Forums","url":"https://discuss.huggingface.co/t/hidden-state-signals-in-iterative-llm-repair-what-cosine-similarity-at-layer-27-actually-tells-you/174143"},{"title":"Modulating LLM's Behavior via Simple Parameter Editing","url":"https://aclanthology.org/2025.naacl-long.321.pdf"},{"title":"Do LLM Outputs Mirror Their Internal Semantic Maps? A Large-Scale Behavioral Probing Study | One trivial observation at a time","url":"https://www.pokutta.com/blog/research/2026/03/06/neural-semantic-geometry.html"},{"title":"arXiv:2502.19649v3 [cs.LG] 12 Mar 2025 - Jan Wehner","url":"https://janwehner.com/files/representation_engineering.pdf"},{"title":"Pretrained LLMs Learn Multiple Types of Uncertainty","url":"https://arxiv.org/html/2505.21218"},{"title":"Preprint. Under review DOES MATH REASONING IMPROVE GENERAL LLM","url":"https://arxiv.org/pdf/2507.00432"}]

I found several highly relevant papers on representation geometry in LLMs during post-training. Here's a summary of the key findings:

## Primary Research: Tracing Representation Geometry Through Post-training

The most directly relevant work investigates geometric changes during post-training stages, analyzing the Tülu-3.1 models which utilize a three-stage post-training recipe—Supervised Fine-tuning (SFT), Direct Preference Optimization (DPO), and Reinforcement Learning with Verifiable Rewards (RLVR) applied to LLaMA-3.1-8B.

## Key Findings on SFT vs. RL

SFT drives an "entropy-seeking" dynamic, expanding the representational manifold for specific instruction-response examples, which improves in-distribution performance but risks overfitting due to higher representational capacity. In contrast, RLVR promotes a "compression-seeking" dynamic, refining representations towards reward-aligned directions.

Research on math reasoning finds that SFT induces significant drift in both latent and output spaces, especially for non-reasoning inputs, whereas RL better preserves the geometry of internal features and the stability of token distributions.

## Representation Geometry Framework

Recent work addresses how to make sense of geometric notions (e.g., cosine similarity and projection) in representation space, proving that these connect to linear probing and model steering, and using a non-Euclidean inner product that respects language structure to unify notions of linear representation and construct probes and steering vectors using counterfactual pairs.

## Linear Probes and Hidden States

To identify truthfulness directions in models, researchers compute difference-in-mean on hidden representations, getting this direction on one dataset and transferring it to other datasets. Linear uncertainty vectors—directions in the model's hidden space—correlate with generation correctness across multiple models and datasets, suggesting that uncertainty is a learnable and linearly separable concept within LLMs' latent spaces.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1617c49-ec44-4e7f-b953-8dc958a4fb1d",
  "isSidechain": true,
  "promptId": "f665e9e5-0a3b-430d-856f-f79521590172",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "0e7c2908-3b99-4a1d-ba94-2294d521c69d",
  "sourceToolAssistantUUID": "c1617c49-ec44-4e7f-b953-8dc958a4fb1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-09T20:57:38.738Z_

Excellent — the "Tracing the Representation Geometry" paper looks highly relevant. Let me fetch it and also the RL contamination detection paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e7c2908-3b99-4a1d-ba94-2294d521c69d",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfVbL9tdw1CfkK83Sjo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1351f04-7f52-4933-84a0-f8679ef83152",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01N1GngkYf6X9wFJJv22Lypf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2485,
      "cache_read_input_tokens": 17336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2485,
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

_source line 32 · 2026-05-09T20:57:41.215Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018UeB9YWtxhPuWDdsJrp48d`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.23024",
  "prompt": "Extract the full abstract, methodology, and all key findings about how SFT, DPO, and RL/RLVR stages affect representation geometry. Include any quantitative claims about cosine similarity between probe directions across training stages, orthogonality, entropy-seeking vs compression-seeking dynamics, and specific numbers. Note the paper title, authors, arXiv ID."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1351f04-7f52-4933-84a0-f8679ef83152",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfVbL9tdw1CfkK83Sjo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7eddfa32-30df-4c3f-9795-29b3bf07be68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01N1GngkYf6X9wFJJv22Lypf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2485,
      "cache_read_input_tokens": 17336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2485,
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

_source line 33 · 2026-05-09T20:57:42.145Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KkSTEpRsmNbNcuB1G1SHsT`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.09259",
  "prompt": "Extract the abstract, methodology, and key findings about how different training stages (SFT vs RL) leave different activation fingerprints that can be used for contamination detection. Include any quantitative findings. Note paper title, authors, arXiv ID."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7eddfa32-30df-4c3f-9795-29b3bf07be68",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfVbL9tdw1CfkK83Sjo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff7ac744-b524-433c-94f2-5377f9bf71ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01N1GngkYf6X9wFJJv22Lypf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2485,
      "cache_read_input_tokens": 17336,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2485
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 314,
          "cache_read_input_tokens": 17336,
          "cache_creation_input_tokens": 2485,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2485,
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

_source line 34 · 2026-05-09T20:57:47.325Z_

<details><summary>↩ Tool result · `toolu_018UeB9YWtxhPuWDdsJrp48d`</summary>

```text
# Paper Summary: Representation Geometry in Language Models

**Title:** "Tracing the Representation Geometry of Language Models from Pretraining to Post-training"

**ArXiv ID:** 2509.23024

**Authors:** Melody Zixuan Li, Kumar Krishna Agrawal, Arna Ghosh, Komal Kumar Teru, Adam Santoro, Guillaume Lajoie, Blake A. Richards

---

## Abstract

The research investigates how learned representations evolve through training stages by analyzing spectral properties. The authors examine "the geometry of learned representations across pretraining and post-training, measuring effective rank (RankMe) and eigenspectrum decay."

---

## Key Findings

**Pretraining Phases:**
Three distinct geometric phases emerge during autoregressive pretraining:

1. **Warmup Phase:** "rapid representational collapse"
2. **Entropy-Seeking Phase:** manifold dimensionality expands substantially, correlating with peak n-gram memorization
3. **Compression-Seeking Phase:** "anisotropic consolidation, selectively preserving variance along dominant eigendirections while contracting others"

**Post-Training Dynamics:**

- **SFT and DPO:** Drive "entropy-seeking" dynamics, improving in-distribution performance but degrading out-of-distribution robustness
- **RLVR:** Induces "compression-seeking," enhancing reward alignment while reducing generation diversity

---

## Methodology

Models tested: OLMo (1B-7B) and Pythia (160M-12B)

The paper analyzes how "cross-entropy optimization under skewed token frequencies and representational bottlenecks" produces these geometric transitions.

---

## Note

The abstract provided does not include specific quantitative claims about cosine similarity or orthogonality metrics between probe directions across stages.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7eddfa32-30df-4c3f-9795-29b3bf07be68",
  "isSidechain": true,
  "promptId": "f665e9e5-0a3b-430d-856f-f79521590172",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "db030ccb-966a-4c7e-b626-6888670245ec",
  "sourceToolAssistantUUID": "7eddfa32-30df-4c3f-9795-29b3bf07be68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-09T20:57:48.086Z_

<details><summary>↩ Tool result · `toolu_01KkSTEpRsmNbNcuB1G1SHsT`</summary>

```text
# Data Contamination Detection in RL Post-training for LLMs

**Paper Details:**
- **Title:** Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models
- **arXiv ID:** 2510.09259
- **Authors:** Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Xiaolong Hu, Ge Li

## Abstract

The research addresses a critical gap in contamination detection across LLM training phases. While methods exist for pre-training and supervised fine-tuning stages, "a critical research gap exists for the increasingly significant phase of Reinforcement Learning (RL) post-training."

## Key Methodology

The authors propose **Self-Critique**, motivated by a crucial observation: RL post-training causes "output entropy distribution of LLMs tends to collapse into highly specific and sparse modes." The method probes for policy collapse—when models converge to narrow reasoning paths—which distinguishes RL-contaminated models from clean ones.

The research introduces **RL-MIA**, a benchmark designed to simulate this contamination scenario in RL contexts.

## Quantitative Findings

Self-Critique demonstrates substantial performance improvements, achieving "an AUC improvement of up to 30%" compared to baseline methods. Notably, "existing methods are close to a random guess for RL-phase contamination," while Self-Critique successfully enables reliable detection across multiple models and contamination tasks.

The work was accepted to ICLR 2026, with code available publicly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff7ac744-b524-433c-94f2-5377f9bf71ee",
  "isSidechain": true,
  "promptId": "f665e9e5-0a3b-430d-856f-f79521590172",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "e547519c-2252-456b-97b6-ee40adbecc44",
  "sourceToolAssistantUUID": "ff7ac744-b524-433c-94f2-5377f9bf71ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-09T20:57:52.793Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01B4SuBF9rRKxKWXkoW7yuaM`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.23024",
  "prompt": "Look for any specific quantitative findings about cosine similarity between probe directions from different training stages (SFT, DPO, RLVR), orthogonality of probe directions, specific numerical values comparing representations across stages, and methods involving linear probes. Also look for any discussion of how SFT vs RL probe directions relate geometrically in activation space."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e547519c-2252-456b-97b6-ee40adbecc44",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfWSSPgEEH8SzowZ1j7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8293fe8a-2b52-46d4-9731-2446a90ab613",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Jd4oiSp1qj3omW8NTLnxeZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1154,
      "cache_read_input_tokens": 19821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1154,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-09T20:57:52.933Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017V5g44GAPTzvsJ4XNteEuT`</summary>

```json
{
  "query": "\"stage-contrastive\" OR \"contrastive activation\" benchmark contamination fingerprinting SFT RL probe 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8293fe8a-2b52-46d4-9731-2446a90ab613",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfWSSPgEEH8SzowZ1j7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d69ffceb-9437-4951-839d-340106834c8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Jd4oiSp1qj3omW8NTLnxeZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1154,
      "cache_read_input_tokens": 19821,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1154
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 19821,
          "cache_creation_input_tokens": 1154,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1154,
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

_source line 38 · 2026-05-09T20:57:59.182Z_

<details><summary>↩ Tool result · `toolu_01B4SuBF9rRKxKWXkoW7yuaM`</summary>

```text
# Analysis: Geometric Relationships Between Post-Training Stages

Based on my review of this research paper, **I found no specific quantitative findings regarding cosine similarity between probe directions across post-training stages (SFT, DPO, RLVR), orthogonality measurements, or linear probe methods comparing representation geometry across these stages.**

## What the Paper Does Contain

The research focuses on **spectral metrics** (RankMe and αReQ) to characterize representation geometry rather than probe-based approaches. For post-training stages, the analysis tracks:

- **RankMe changes**: SFT and DPO show increases (entropy-seeking), while RLVR shows decreases (compression-seeking)
- **Behavioral correlations**: Different training methods produce distinct geometric transformations linked to specific model behaviors
- **Pass@k performance**: RLVR constrains exploratory behavior, indicated by declining pass@256 performance despite improving pass@16

## Key Limitation

The paper states that "our findings are primarily correlational; establishing causal connections between geometric dynamics and emergent capabilities requires additional investigation." The authors do not employ linear probe techniques or measure angular relationships between representation directions across post-training phases.

The geometric analysis remains at the level of **covariance matrix spectral properties** rather than directional/orthogonality comparisons between specific learned representations at different training stages.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8293fe8a-2b52-46d4-9731-2446a90ab613",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "a1bfaee5-9248-4f93-9e5f-928b315902a1",
  "sourceToolAssistantUUID": "8293fe8a-2b52-46d4-9731-2446a90ab613",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-09T20:57:59.785Z_

<details><summary>↩ Tool result · `toolu_017V5g44GAPTzvsJ4XNteEuT`</summary>

```text
Web search results for query: ""stage-contrastive" OR "contrastive activation" benchmark contamination fingerprinting SFT RL probe 2024 2025 arXiv"

Links: [{"title":"Mutli-Stage Contrastive Training For Fine-grained Cross- ...","url":"https://arxiv.org/pdf/2506.01806"},{"title":"A Practical Two-Stage Recipe for Mathematical LLMs:","url":"https://arxiv.org/pdf/2507.08267"},{"title":"Published in Transactions on Machine Learning Research (07/2025)","url":"https://arxiv.org/pdf/2404.00699"},{"title":"From Construction to Injection: Edit-Based Fingerprints for Large Language Models","url":"https://arxiv.org/html/2509.03122v3"},{"title":"Machine Learning Jun 2024","url":"https://web3.arxiv.org/list/cs.LG/2024-06?skip=1900&show=2000"},{"title":"Reinforcement Learning from Human Feedback","url":"https://arxiv.org/html/2504.12501v3"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/affda8306b5501c58fca59fe52f05fda-Paper-Conference.pdf"},{"title":"LLM Fingerprinting via Semantically Conditioned Watermarks","url":"https://arxiv.org/html/2505.16723v2"},{"title":"Computer Vision and Pattern Recognition Sep 2024","url":"https://www.arxiv.org/list/cs.CV/2024-09?skip=1550&show=2000"},{"title":"Brain-Cognition Fingerprinting via Graph-GCCA with Contrastive Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/brain-cognition-fingerprinting-via-graph-gcca-contrastive"}]

Based on the search results, I found several relevant papers from 2024-2025 on arXiv related to your query terms:

## Key Findings:

**Contamination Detection & Benchmarks:**
A recent survey by Deng et al. (2024) covers contamination in language models, including detection methods, impact, and remediation, with a focus specifically on detecting contamination techniques.

**Fingerprinting & LLM Protection:**
Recent work on fingerprint injection for SFT involves selecting regularization samples to mix with fingerprint datasets. Both Instructional Fingerprinting (IF) by Xu et al. (2024) and Scalable Fingerprinting (SF) by Nasery et al. (2025) use supervised finetuning (SFT) to learn fingerprints.

**Contrastive Learning & Alignment:**
Preference optimization has been extended to contrastive learning models, with approaches that build on contrastive learning frameworks while preserving pretrained knowledge through continual learning.

**RL & Post-Training:**
Contrastive loss functions are commonly used in RLHF-based training approaches, and recent methods for post-training models use supervised learning and/or reinforcement learning, with growing reports of improvements from post-training models in the open-source community.

The search results show active research in 2024-2025 combining these concepts, though the specific term "stage-contrastive" didn't appear prominently in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d69ffceb-9437-4951-839d-340106834c8a",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "33f855b6-22b0-45a8-b0c8-e2938f1de18f",
  "sourceToolAssistantUUID": "d69ffceb-9437-4951-839d-340106834c8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-09T20:58:02.594Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018GvFv71QLan8xTHc7q6jo3`</summary>

```json
{
  "query": "mechanistic interpretability \"SFT\" \"RLHF\" OR \"DPO\" probe direction hidden state cosine similarity orthogonal 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33f855b6-22b0-45a8-b0c8-e2938f1de18f",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfXJMzxz42wzggf8b18",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b3e1b07-bb0f-480a-acfa-c665ccac99c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WXknyyNShN2gpx3WpZaE1g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 20975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-09T20:58:03.472Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TdG1aNpUjSk2sKFE66Fi9H`</summary>

```json
{
  "query": "representation engineering SFT RLHF activation difference vector alignment training stage LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b3e1b07-bb0f-480a-acfa-c665ccac99c0",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfXJMzxz42wzggf8b18",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c06d09ac-9c43-40ea-a855-857db2cb9cd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WXknyyNShN2gpx3WpZaE1g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 20975,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1439
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 20975,
          "cache_creation_input_tokens": 1439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1439,
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

_source line 42 · 2026-05-09T20:58:10.741Z_

<details><summary>↩ Tool result · `toolu_018GvFv71QLan8xTHc7q6jo3`</summary>

```text
Web search results for query: "mechanistic interpretability "SFT" "RLHF" OR "DPO" probe direction hidden state cosine similarity orthogonal 2024 arXiv"

Links: [{"title":"The Geometry of Persona: Disentangling Personality from Reasoning in Large Language Models","url":"https://arxiv.org/html/2512.07092"},{"title":"A Mechanistic Perspective from Safety Neurons","url":"https://arxiv.org/pdf/2406.14144"},{"title":"A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity","url":"https://arxiv.org/html/2401.01967"},{"title":"A First-Order Logic–Based Alternative to Reward Models in RLHF","url":"https://arxiv.org/html/2512.14100v1"},{"title":"Provably Mitigating Overoptimization in RLHF: Your SFT Loss is Implicitly an Adversarial Regularizer","url":"https://arxiv.org/html/2405.16436v3"},{"title":"[2411.14797] Continual SFT Matches Multimodal RLHF with Negative Supervision","url":"https://arxiv.org/abs/2411.14797"},{"title":"Mechanistic Interpretability for Large Language Model Alignment: Progress, Challenges, and Future Directions","url":"https://arxiv.org/html/2602.11180"},{"title":"[2602.11180] Mechanistic Interpretability for Large Language Model Alignment: Progress, Challenges, and Future Directions","url":"https://arxiv.org/abs/2602.11180"},{"title":"[2405.16436] Provably Mitigating Overoptimization in RLHF: Your SFT Loss is Implicitly an Adversarial Regularizer","url":"https://arxiv.org/abs/2405.16436"},{"title":"[2502.11026] RLHF in an SFT Way: From Optimal Solution to Reward-Weighted Alignment","url":"https://arxiv.org/abs/2502.11026"}]

I found several relevant papers on arXiv that combine mechanistic interpretability with alignment techniques (SFT, RLHF, DPO) and analysis of hidden state properties. Here are the key results:

## Primary Results

**1. "The Geometry of Persona: Disentangling Personality from Reasoning in Large Language Models"** (January 2026)

This work explores the Linear Representation Hypothesis, suggesting that high-level semantic concepts are encoded as linear, orthogonal directions within the high-dimensional latent space of the Transformer. Through layer-wise probing on frozen models, the authors demonstrate that personality representations emerge in upper transformer blocks and are largely orthogonal to reasoning vectors. Their findings challenge the prevailing assumption in Supervised Fine-Tuning (SFT) that personality is a holistic behavioral pattern requiring global weight updates.

**2. "A Mechanistic Perspective from Safety Neurons"** (June 2024)

This work conducts SFT on ShareGPT and then performs safety alignment using DPO on HH-RLHF-Harmless. The paper identifies interpretable neurons as a key goal in mechanistic interpretability for Transformers.

**3. "A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity"** (January 2024)

This work characterizes the representations of language models from a geometric perspective, demonstrating geometric characterization that can extract feature representations for toxicity detection.

**4. "Mechanistic Interpretability for Large Language Model Alignment: Progress, Challenges, and Future Directions"** (January 2026)

This survey examines mechanistic interpretability techniques applied to LLM alignment, including circuit discovery, feature visualization, activation steering, and causal intervention, analyzing how these insights inform alignment strategies including RLHF, constitutional AI, and scalable oversight.

These papers directly address the intersection of mechanistic interpretability, alignment methods, and analysis of learned representations in hidden states.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b3e1b07-bb0f-480a-acfa-c665ccac99c0",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "0d7facb8-be41-4b44-be97-dc36b0bffe80",
  "sourceToolAssistantUUID": "1b3e1b07-bb0f-480a-acfa-c665ccac99c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-09T20:58:14.520Z_

<details><summary>↩ Tool result · `toolu_01TdG1aNpUjSk2sKFE66Fi9H`</summary>

```text
Web search results for query: "representation engineering SFT RLHF activation difference vector alignment training stage LLM 2024 2025"

Links: [{"title":"RLHF in an SFT Way: From Optimal Solution to Reward-Weighted Alignment","url":"https://arxiv.org/html/2502.11026v3"},{"title":"The 3 Stages of LLM Training: A Deep Dive into Reinforcement Learning from Human Feedback (RLHF) - DataSci Ocean","url":"https://datasciocean.com/en/ai-concept/llm-fine-tuning-rlhf/"},{"title":"On the Generalization of SFT: A Reinforcement Learning ...","url":"https://arxiv.org/pdf/2508.05629"},{"title":"An Introduction to Representation Engineering","url":"https://www.alignmentforum.org/posts/3ghj8EuKzwD3MQR5G/an-introduction-to-representation-engineering-an-activation"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.12299"},{"title":"Post-training methods for language models | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/11/04/post-training-methods-language-models"},{"title":"Preference Alignment vs Supervised Fine-Tuning in LLM Training","url":"https://www.rohan-paul.com/p/preference-alignment-vs-supervised"},{"title":"Aligning Large Language Models with Representation ...","url":"https://par.nsf.gov/servlets/purl/10620886"},{"title":"Published as a conference paper at ICLR 2024 THE UNLOCKING SPELL ON BASE LLMS:","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6bcbb4a501dbad0eba1b660c1a55318c-Paper-Conference.pdf"},{"title":"RLHF vs. RLAIF: Fine-Tuning LLMs for Better Alignment (OTS, SFT, PPO, Jailbreak) | by Riley Learning | Medium","url":"https://rileylearning.medium.com/rlhf-vs-rlaif-fine-tuning-llms-for-better-alignment-ots-sft-ppo-jailbreak-37532653f195"}]

I've successfully performed the web search for your query. Here's a summary of the relevant findings:

## Key Research Areas Found

**Representation Engineering & Activation Differences:**
Activation engineering has been proposed as a cost-effective method to modify an LLM's activations during decoding, with these methods identifying specific directions to adjust LLM behaviors by analyzing activation differences between contrastive pairs. The process involves extracting activation differences between positive and negative examples across all layers of the model, which are aggregated to compute the mean difference used to identify critical elements influencing the model's behavior.

**SFT and RLHF Training Stages:**
The alignment tuning process typically comprises two stages: supervised fine-tuning (SFT) on instruction data and reinforcement learning from human feedback (RLHF), during which the base LLM is fine-tuned using instruction-answer pairs.

**Recent Theoretical Developments (2024-2025):**
Recent research reinterprets RLHF as a reward-weighted variant of SFT, preserving reliance on an explicit reward. Other work shows that SFT can be cast as RL with an implicit reward, proposing adjustments such as smaller learning rates to manage the vanishing KL constraint.

**Representation Engineering vs. RLHF:**
RLHF compares two different texts which might differ on many things aside from the desired alignment property, whereas representation engineering measures the difference in activations taken from the same prompt that only differs with respect to the alignment property, reducing noise in the alignment signal.

The search results include recent papers from 2024-2025 covering theoretical unification of SFT and RL, activation-based steering methods, and analysis of LLM alignment training stages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c06d09ac-9c43-40ea-a855-857db2cb9cd8",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "3a894a3b-7da0-4ea6-9223-fdd4438b5046",
  "sourceToolAssistantUUID": "c06d09ac-9c43-40ea-a855-857db2cb9cd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-09T20:58:18.758Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015nL7Wd5EqZGzmNaQFxqUdq`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.07092",
  "prompt": "Extract the abstract, methodology, and all key quantitative findings about orthogonality of probe directions in LLMs (personality vs reasoning, SFT effects, etc.). Note paper title, authors, arXiv ID, and any specific cosine similarity values reported."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a894a3b-7da0-4ea6-9223-fdd4438b5046",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfYPiVavjqCCAcbbZWh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8c5d68b-6db4-4d66-934b-65b2de45a80d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KVgveEF84Q5CAdb6PeXrq3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2316,
      "cache_read_input_tokens": 22414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2316,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-09T20:58:19.988Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TnCYEt1Lujrq8hz37MMS8y`</summary>

```json
{
  "url": "https://arxiv.org/abs/2401.01967",
  "prompt": "Extract the abstract, methodology, and all key findings about how DPO/RLHF training affects the geometry of activation space, representation directions, cosine similarity of features, and orthogonality of probe directions. Note paper title, authors, arXiv ID."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8c5d68b-6db4-4d66-934b-65b2de45a80d",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfYPiVavjqCCAcbbZWh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "75c19eb9-877a-4f19-af9e-cd6b94b16475",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KVgveEF84Q5CAdb6PeXrq3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2316,
      "cache_read_input_tokens": 22414,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2316
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 259,
          "cache_read_input_tokens": 22414,
          "cache_creation_input_tokens": 2316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2316,
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

_source line 46 · 2026-05-09T20:58:23.205Z_

<details><summary>↩ Tool result · `toolu_015nL7Wd5EqZGzmNaQFxqUdq`</summary>

```text
# Paper Summary

**Title:** "The Geometry of Persona: Disentangling Personality from Reasoning in Large Language Models"

**Author:** Zhixiang Wang

**arXiv ID:** 2512.07092

## Abstract
The paper addresses the stability-plasticity dilemma in personalized LLMs, proposing that "personality traits exist as orthogonal linear subspaces." The framework avoids degrading reasoning capabilities during alignment.

## Methodology
The Soul Engine framework employs:
- Linear Representation Hypothesis as theoretical foundation
- SoulBench dataset via dynamic contextual sampling
- Dual-head architecture on frozen Qwen-2.5 base
- Extraction of disentangled personality vectors without backbone modification

## Key Quantitative Findings

**Precision:** Mean Squared Error of 0.011 against psychological ground truth

**Orthogonality:** "T-SNE visualization confirms that personality manifolds are distinct and continuous," enabling zero-shot personality injection while preserving model intelligence

**Control:** Achieved "robust control over behavior via vector arithmetic, validated through extensive ablation studies"

**Note:** The page content provided does not include specific cosine similarity values for personality-reasoning orthogonality or SFT effects. Code and dataset are available on Hugging Face.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8c5d68b-6db4-4d66-934b-65b2de45a80d",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "e69f7a4a-444e-48ad-873c-37542603130d",
  "sourceToolAssistantUUID": "d8c5d68b-6db4-4d66-934b-65b2de45a80d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-09T20:58:24.478Z_

<details><summary>↩ Tool result · `toolu_01TnCYEt1Lujrq8hz37MMS8y`</summary>

```text
# Paper Summary

**Title:** A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity

**arXiv ID:** 2401.01967

**Authors:** Andrew Lee, Xiaoyan Bai, Itamar Pres, Martin Wattenberg, Jonathan K. Kummerfeld, Rada Mihalcea

## Abstract

The researchers investigate how Direct Preference Optimization (DPO) reduces toxicity in language models. They state: "capabilities learned from pre-training are not removed, but rather bypassed."

## Key Findings

Based on the abstract provided, the paper makes three critical discoveries:

1. **Toxicity Representation:** The team first examined how toxic outputs emerge in GPT2-medium before alignment.

2. **Alignment Mechanism:** Rather than erasing problematic capabilities, DPO causes models to circumvent or sidestep these behaviors through learned avoidance strategies.

3. **Vulnerability to Un-alignment:** The researchers demonstrate "a simple method to un-align the model, reverting it back to its toxic behavior," indicating alignment changes are not permanent deletions but reversible redirections.

## Note

The provided webpage excerpt contains only the abstract and metadata. Specific technical details about activation space geometry, representation directions, cosine similarity metrics, or orthogonality analyses are not present in this source material. Access to the full PDF would be required for those mechanistic details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75c19eb9-877a-4f19-af9e-cd6b94b16475",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "38a9584a-d09f-444c-a62b-356b598a88d3",
  "sourceToolAssistantUUID": "75c19eb9-877a-4f19-af9e-cd6b94b16475",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-09T20:58:26.723Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C771tJZbidqEto7Th1ge2c`</summary>

```json
{
  "query": "DICE activation pattern contamination detection fine-tuning layer-specific arXiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38a9584a-d09f-444c-a62b-356b598a88d3",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfZ7wF76XgcPD7BqANG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5da1284d-53e3-4ff4-a029-82019f69006d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NVgxGs8ECKWSzvXUzjq6HL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 931,
      "cache_read_input_tokens": 24730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 931,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-09T20:58:27.521Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VRqk2ArWDzWofovc424Xkh`</summary>

```json
{
  "query": "\"linear representation hypothesis\" SFT RLHF DPO \"probe\" \"direction\" orthogonal cosine geometry 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5da1284d-53e3-4ff4-a029-82019f69006d",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfZ7wF76XgcPD7BqANG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "875c66e9-00fa-4453-bba8-f0508f26bf19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NVgxGs8ECKWSzvXUzjq6HL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 931,
      "cache_read_input_tokens": 24730,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 931
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 143,
          "cache_read_input_tokens": 24730,
          "cache_creation_input_tokens": 931,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 931,
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

_source line 50 · 2026-05-09T20:58:33.404Z_

<details><summary>↩ Tool result · `toolu_01C771tJZbidqEto7Th1ge2c`</summary>

```text
Web search results for query: "DICE activation pattern contamination detection fine-tuning layer-specific arXiv 2024"

Links: [{"title":"DICE: Detecting In-distribution Contamination in LLM’s Fine-tuning Phase for Math Reasoning","url":"https://arxiv.org/html/2406.04197v2"},{"title":"DICE: Detecting In-distribution Contamination","url":"https://arxiv.org/pdf/2406.04197"},{"title":"[2406.04197] DICE: Detecting In-distribution Contamination in LLM's Fine-tuning Phase for Math Reasoning","url":"https://arxiv.org/abs/2406.04197"},{"title":"A Comprehensive Survey of Contamination Detection Meth","url":"https://arxiv.org/pdf/2404.00699"},{"title":"DICE: Detecting In-distribution Contamination in LLM's Fine-tuning Phase for Math Reasoning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/dice-detecting-distribution-contamination-llms-fine-tuning"},{"title":"DICE: Detecting In-distribution Contamination in LLM's Fine-tuning Phase for Math Reasoning | PromptLayer","url":"https://www.promptlayer.com/research-papers/dice-detecting-in-distribution-contamination-in-llm-s-fine-tuning-phase-for-math-reasoning"},{"title":"DICE: Detecting In-distribution Contamination in LLM's Fine- ...","url":"https://web3.arxiv.org/pdf/2406.04197v1"},{"title":"DICE: Detecting In-distribution Contamination in LLM's Fine-tuning Phase for Math Reasoning | Request PDF","url":"https://www.researchgate.net/publication/381227046_DICE_Detecting_In-distribution_Contamination_in_LLM's_Fine-tuning_Phase_for_Math_Reasoning"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"Computer Science Jun 2024","url":"http://arxiv.org/list/cs/2024-06?skip=4400&show=2000"}]

Based on the search results, I found comprehensive information about DICE, a paper from 2024 on detecting in-distribution contamination in LLMs:

## Summary

DICE is a novel method that leverages the internal states of LLMs to locate-then-detect contamination. DICE first identifies the most sensitive layer to contamination, then trains a classifier based on the internal states of that layer.

The paper specifically addresses in-distribution contamination, which occurs when training on data similar to benchmark data inflates performance. This is distinct from exact contamination, where the model has seen identical data during training.

### Key Features

The method uses a Locate-then-Detect paradigm, which first locates the contaminated layer and then detects the contamination via the internal states. The method specifically identifies 'contamination layers' where the model shows unusual patterns of activity when processing potentially contaminated data.

### Results

Experiments reveal DICE's high accuracy in detecting in-distribution contamination across various LLMs and math reasoning datasets. Additionally, DICE's predictions correlate with the performance of LLMs fine-tuned by either users or other organizations, achieving a coefficient of determination between 0.61 and 0.75.

The paper (arXiv 2406.04197) was published in June 2024, with the most recent version appearing in September 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5da1284d-53e3-4ff4-a029-82019f69006d",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "32076b00-9bd7-4bee-9dd9-e3538b2b2529",
  "sourceToolAssistantUUID": "5da1284d-53e3-4ff4-a029-82019f69006d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-09T20:58:34.978Z_

<details><summary>↩ Tool result · `toolu_01VRqk2ArWDzWofovc424Xkh`</summary>

```text
Web search results for query: ""linear representation hypothesis" SFT RLHF DPO "probe" "direction" orthogonal cosine geometry 2024 2025 arXiv"

Links: [{"title":"The Linear Representation Hypothesis and the Geometry of Large Language Models","url":"https://arxiv.org/html/2311.03658v2"},{"title":"[2311.03658] The Linear Representation Hypothesis and the Geometry of Large Language Models","url":"https://arxiv.org/abs/2311.03658"},{"title":"The Geometry of Persona: Disentangling Personality from Reasoning in Large Language Models","url":"https://arxiv.org/html/2512.07092"},{"title":"Linear Representation Hypothesis","url":"https://www.emergentmind.com/topics/linear-representation-hypothesis-lrh"},{"title":"The Linear Representation Hypothesis and the Geometry of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=T0PoOJg8cK"},{"title":"The Linear Representation Hypothesis and the Geometry of Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/linear-representation-hypothesis-geometry-large-language-models"},{"title":"[PDF] The Linear Representation Hypothesis and the Geometry of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Linear-Representation-Hypothesis-and-the-of-Park-Choe/eb44ce1f7e1f4deac10f6e7009e2073f1eb0b3e4"},{"title":"The Linear Representation Hypothesis and the Geometry of Large Language Models","url":"https://proceedings.mlr.press/v235/park24c.html"},{"title":"The linear representation hypothesis and the geometry of large language models | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3693675"},{"title":"The Origins of Representation Manifolds in Large Language Models","url":"https://arxiv.org/html/2505.18235v1"}]

I found several highly relevant papers on the linear representation hypothesis. Here are the key results:

## Primary Research

The "linear representation hypothesis" is the idea that high-level concepts are represented linearly as directions in some representation space. The most prominent work is "The Linear Representation Hypothesis and the Geometry of Large Language Models" (Park et al., arXiv:2311.03658, ICML 2024), which addresses questions about what linear representation means and how to interpret geometric notions like cosine similarity in representation space, proving connections to linear probing and model steering.

## Key Technical Contributions

The paper uses counterfactual language to formalize linear representation in both output and input spaces, identifies a particular non-Euclidean inner product that respects language structure, and uses this causal inner product to unify all notions of linear representation.

The concept of a causal inner product is introduced with the property that concepts that can vary freely of each other are represented as orthogonal vectors.

## Recent Applications (2025-2026)

Recent work on "The Geometry of Persona" (arXiv:2512.07092, January 2026) applies the Linear Representation Hypothesis, suggesting that high-level semantic concepts like sentiment, truthfulness, and personality traits are encoded as linear, orthogonal directions within transformer latent spaces.

Research demonstrates through layer-wise probing that personality representations emerge in upper transformer blocks and are largely orthogonal to reasoning vectors.

The linear representation hypothesis posits that neural representations are sparse linear combinations of 'almost-orthogonal' direction vectors, reflecting the presence or absence of different features.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "875c66e9-00fa-4453-bba8-f0508f26bf19",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "ec5e04ab-60df-4ccf-b9c1-8debee1ae294",
  "sourceToolAssistantUUID": "875c66e9-00fa-4453-bba8-f0508f26bf19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-09T20:58:38.860Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CySwf8udBKkgRLxARU86BN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.04197",
  "prompt": "Extract the abstract, methodology, and key findings about how fine-tuning stages leave distinct activation signatures, how DICE uses internal layer states to detect contamination, and any quantitative findings. Note paper title, authors, arXiv ID."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec5e04ab-60df-4ccf-b9c1-8debee1ae294",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfZtoFEtRYff9M8jXTC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7bfd0975-5c6f-49f1-9590-6a18de884457",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XU4QWJFSBp3WPYLwi8HjKp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2002,
      "cache_read_input_tokens": 25661,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2002,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-09T20:58:39.862Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019yxF3hnNiUGoczVbMffpYS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2311.03658",
  "prompt": "Extract the abstract, key theorems, and main findings about the geometry of representation space, cosine similarity interpretations, orthogonality of concept directions, and how this framework applies to understanding different training stages or fine-tuning. Note paper title, authors, arXiv ID."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bfd0975-5c6f-49f1-9590-6a18de884457",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfZtoFEtRYff9M8jXTC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91a1a056-a3cd-4a96-b8e0-1617db38dd96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XU4QWJFSBp3WPYLwi8HjKp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2002,
      "cache_read_input_tokens": 25661,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2002
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 254,
          "cache_read_input_tokens": 25661,
          "cache_creation_input_tokens": 2002,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2002,
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

_source line 54 · 2026-05-09T20:58:43.684Z_

<details><summary>↩ Tool result · `toolu_01CySwf8udBKkgRLxARU86BN`</summary>

```text
# DICE: Detecting In-distribution Contamination in LLM Fine-tuning

**Paper Details:**
- **Title:** DICE: Detecting In-distribution Contamination in LLM's Fine-tuning Phase for Math Reasoning
- **Authors:** Shangqing Tu, Kejian Zhu, Yushi Bai, Zijun Yao, Lei Hou, Juanzi Li
- **arXiv ID:** 2406.04197
- **Submission:** June 6, 2024 (v1); September 22, 2024 (v2)

## Abstract Summary

The research addresses data contamination in LLM evaluation, specifically targeting "in-distribution contamination"—where training on data similar to benchmark datasets inflates performance metrics. The authors propose that this type of contamination causes performance degradation on out-of-distribution benchmarks.

## Methodology

DICE employs a two-stage detection approach leveraging internal LLM states:

1. **Layer Identification:** The method identifies the layer most sensitive to contamination
2. **Classification:** A classifier is trained using internal activation states from the sensitive layer to detect contamination presence

## Key Quantitative Findings

- **Detection Accuracy:** High accuracy across multiple LLMs and math reasoning datasets
- **Generalization:** The trained detector generalizes across benchmarks with similar distributions
- **Performance Correlation:** DICE predictions correlate with fine-tuned LLM performance, achieving "a coefficient of determination ($R^2$) between 0.61 and 0.75"

**Resources:** Code and data are available via the GitHub repository referenced in the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bfd0975-5c6f-49f1-9590-6a18de884457",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "8b416ec8-9857-4dec-8595-4960c976643a",
  "sourceToolAssistantUUID": "7bfd0975-5c6f-49f1-9590-6a18de884457",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-09T20:58:45.528Z_

<details><summary>↩ Tool result · `toolu_019yxF3hnNiUGoczVbMffpYS`</summary>

```text
# The Linear Representation Hypothesis and the Geometry of Large Language Models

**Paper Details:**
- **Title:** The Linear Representation Hypothesis and the Geometry of Large Language Models
- **Authors:** Kiho Park, Yo Joong Choe, Victor Veitch
- **arXiv ID:** 2311.03658
- **Submission:** November 7, 2023 (v2: July 17, 2024)
- **Venue:** ICML 2024; NeurIPS 2023 Workshop on Causal Representation Learning

---

## Abstract Summary

The paper investigates how "high-level concepts are represented linearly as directions in representation space." The authors provide two formalizations of linear representation—one for output and one for input spaces—connecting these to linear probing and model steering respectively.

---

## Key Contributions

**Geometric Framework:**
The authors identify "a particular (non-Euclidean) inner product that respects language structure" to interpret geometric notions like cosine similarity and projection in representation spaces.

**Causal Inner Product:**
They introduce a causal inner product enabling unified treatment of linear representations and "construction of probes and steering vectors using counterfactual pairs."

**Empirical Validation:**
Experiments with LLaMA-2 demonstrate linear concept representations exist and support both interpretation and control mechanisms.

---

## Limitations

The provided webpage content lacks specific details about orthogonality of concept directions or applications across different training stages or fine-tuning scenarios. Such technical details would appear in the full paper PDF.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91a1a056-a3cd-4a96-b8e0-1617db38dd96",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "11366d08-626d-4417-959b-7dc7a881926c",
  "sourceToolAssistantUUID": "91a1a056-a3cd-4a96-b8e0-1617db38dd96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-09T20:58:49.047Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CWq5JRZpJKCzVyKn651BJh`</summary>

```json
{
  "query": "SFT RL probe direction \"weight matrix\" OR \"activation\" \"singular vector\" rotation geometry orthogonal 2024 2025 LLM mechanistic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11366d08-626d-4417-959b-7dc7a881926c",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfaftdgTX35YYZy2BP4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e62db868-0555-40af-a3b8-28b6a8d92e37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WRpXieC5nqgd4rtGHzFTKM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1045,
      "cache_read_input_tokens": 27663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1045,
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

### Tool call

_source line 57 · 2026-05-09T20:58:49.763Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RZtQ1qk6r7QuXUf6FkEmsB`</summary>

```json
{
  "query": "\"post-training\" LLM \"orthogonal\" probe direction \"cosine\" SFT DPO RLHF 2025 arXiv hidden representation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e62db868-0555-40af-a3b8-28b6a8d92e37",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfaftdgTX35YYZy2BP4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4134317a-f264-4c7c-8d28-9c92b000af7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WRpXieC5nqgd4rtGHzFTKM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1045,
      "cache_read_input_tokens": 27663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1045,
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

_source line 58 · 2026-05-09T20:58:56.848Z_

<details><summary>↩ Tool result · `toolu_01CWq5JRZpJKCzVyKn651BJh`</summary>

```text
Web search results for query: "SFT RL probe direction "weight matrix" OR "activation" "singular vector" rotation geometry orthogonal 2024 2025 LLM mechanistic"

Links: [{"title":"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs","url":"https://arxiv.org/html/2508.16546v1"},{"title":"RL Is Neither a Panacea Nor a Mirage:","url":"https://arxiv.org/pdf/2508.16546"},{"title":"La RoSA: Enhancing LLM Efficiency via Layerwise Rotated Sparse Activation","url":"https://arxiv.org/pdf/2507.01299"},{"title":"SFT or RL? An Early Investigation into Training R1-Like Reasoning Large Vision-Language Models","url":"https://arxiv.org/html/2504.11468v1"},{"title":"Beyond Two-Stage Training: Cooperative SFT and RL for LLM Reasoning","url":"https://arxiv.org/pdf/2509.06948"},{"title":"The Geometry of Refusal: Exploring LLM Activation Space Before and After Abliteration | Cracken","url":"https://cracken.ai/blog/the-geometry-of-refusal-exploring-llm-activation-space-before-and-after-abliteration"},{"title":"On the Generalization of SFT: A Reinforcement Learning ...","url":"https://arxiv.org/pdf/2508.05629"},{"title":"[2405.16406] SpinQuant: LLM quantization with learned rotations","url":"https://arxiv.org/abs/2405.16406"},{"title":"RLHF in an SFT Way: From Optimal Solution to Reward-Weighted Alignment","url":"https://arxiv.org/html/2502.11026v3"},{"title":"SpinQuant: LLM Quantization with Learned Rotations | OpenReview","url":"https://openreview.net/forum?id=ogO6DGE6FZ"}]

The search results contain several highly relevant papers on mechanistic understanding of LLM fine-tuning. Here's what I found:

## Key Findings

**Most Directly Relevant: "RL Is Neither a Panacea Nor a Mirage" (December 2025)**

This paper tracks geometric shifts in parameter space across the SFT and RL phases by analyzing model weight matrices through spectral analysis, specifically singular-value decomposition (SVD). 

The core mechanistic insight is striking: OOD performance degradation and its later recovery correlate almost entirely with rotations of the singular vectors at the spectrum's extremes, while the corresponding singular values change little. This directly addresses your query about probe direction and singular vector geometry.

Importantly, the findings indicate that directional shifts in the extremal components, rather than magnitude shifts, govern model's performance—emphasizing rotation and direction geometry over absolute values.

## Other Related Work

The search also returned several complementary papers:

1. **LaRoSA (2025)** - Studies orthogonal rotations of input activations for LLM inference, where the rotation is orthogonal and can be reversed after pruning.

2. **Mechanistic Interpretability of Refusal (2025)** - Discusses how refusal isn't a decision but a geometric pattern—a region of activation space that the model has learned to associate with refusing.

3. **SpinQuant (2024-2025)** - Covers how rotating activation or weight matrices helps remove outliers, with rotation parameterizations that lead to identical outputs in full-precision Transformer architectures.

The first paper appears most aligned with your search focus on SFT/RL probe direction geometry and singular vector rotations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e62db868-0555-40af-a3b8-28b6a8d92e37",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "81fbab8d-033b-4d92-9cbe-c0904c3d2d7a",
  "sourceToolAssistantUUID": "e62db868-0555-40af-a3b8-28b6a8d92e37",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-09T20:58:57.207Z_

<details><summary>↩ Tool result · `toolu_01RZtQ1qk6r7QuXUf6FkEmsB`</summary>

```text
Web search results for query: ""post-training" LLM "orthogonal" probe direction "cosine" SFT DPO RLHF 2025 arXiv hidden representation"

Links: [{"title":"Probe-Based Data Attribution: Discovering and Mitigating Undesirable","url":"https://arxiv.org/pdf/2602.11079"},{"title":"Table Of Contents ↑ RL for LLM Post-training survey","url":"https://arxiv.org/pdf/2407.16216"},{"title":"[2407.16216] Reinforcement Learning for LLM Post-Training: A Survey","url":"https://arxiv.org/abs/2407.16216"},{"title":"Quagmires in SFT-RL Post-Training: When High SFT Scores Mislead and What to Use Instead","url":"https://arxiv.org/html/2510.01624v1"},{"title":"Improving LLM Safety and Helpfulness using SFT and DPO: A Study on OPT-350M","url":"https://arxiv.org/pdf/2509.09055"},{"title":"Direct Preference Optimization (DPO) - Deep (Learning) Focus","url":"https://cameronrwolfe.substack.com/p/direct-preference-optimization"},{"title":"1 Reasoning Beyond Limits: Advances and Open Problems for LLMs","url":"https://arxiv.org/pdf/2503.22732"},{"title":"(PDF) A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More","url":"https://www.researchgate.net/publication/382492528_A_Comprehensive_Survey_of_LLM_Alignment_Techniques_RLHF_RLAIF_PPO_DPO_and_More"},{"title":"How to align open LLMs in 2025 with DPO & and synthetic data","url":"https://www.philschmid.de/rl-with-llms-in-2025-dpo"},{"title":"[2503.10460] Light-R1: Curriculum SFT, DPO and RL for Long COT from Scratch and Beyond","url":"https://arxiv.org/abs/2503.10460"}]

Based on the search results, I found several relevant papers about LLM post-training, though the specific combination of all your query terms appears to target specialized technical work. Here's what I found:

## Key Research Found

Recent work on probing LLM hidden representations includes analysis of cosine similarities between behavior change vectors and datapoint vectors, which relates to your interest in probe directions and cosine similarity metrics.

Research addresses how SFT models before DPO training maintain specific behavioral properties, responding to critiques from 2025 work about activation-space artifacts in narrowly finetuned models.

## Post-Training Methods

Major post-training approaches for LLMs include RLHF, RLVR, and DPO methods built on PPO and GRPO optimization frameworks.

Recent work incorporates Supervised Fine-tuning (SFT), Direct Preference Optimization (DPO), and Reinforcement Learning with Verifiable Rewards (RLVR) in comprehensive post-training pipelines.

## 2025 Research on Post-Training Dynamics

Current 2025 research shows inconsistent views on SFT-RL sequencing, with some work asserting initial SFT is necessary for subsequent RL, others warning that over-SFT may constrain RL, and additional work claiming SFT generalizes poorly.

The search results do not contain papers that specifically focus on orthogonal probe directions or detailed hidden representation analysis during post-training with the exact combination of terms you specified. You may want to search directly on arXiv for more specialized papers on mechanistic interpretability and representation probing in post-trained models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4134317a-f264-4c7c-8d28-9c92b000af7b",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "8d368c60-dbba-4c09-b86d-83396f265ec3",
  "sourceToolAssistantUUID": "4134317a-f264-4c7c-8d28-9c92b000af7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-09T20:59:04.974Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MepitRCaUgeSKQd227Ekhw`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.16546v1",
  "prompt": "Find all specific quantitative findings about: (1) how SFT and RL affect weight matrix singular vectors and their directions, (2) any cosine similarity measurements between SFT and RL representation directions, (3) orthogonality of any vectors, (4) the specific mechanism by which RL \"counteracts SFT-induced directional drift.\" Report section titles and exact numbers if present."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d368c60-dbba-4c09-b86d-83396f265ec3",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfbXxRVaGSHVqQkq9Nx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a922643b-d332-4bfe-91d6-5d0cf2409599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012r6TxSuq2KappnC5uKfUNa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2094,
      "cache_read_input_tokens": 28708,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2094,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-09T20:59:05.140Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GeJzV3BDGttdbhK35uuq4p`</summary>

```json
{
  "query": "LLM training stages activation fingerprint \"refusal direction\" OR \"honesty direction\" \"orthogonal\" SFT DPO RLHF cosine 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a922643b-d332-4bfe-91d6-5d0cf2409599",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfbXxRVaGSHVqQkq9Nx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f5f53b6-477c-4b81-8b63-72ec58578b54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012r6TxSuq2KappnC5uKfUNa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2094,
      "cache_read_input_tokens": 28708,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2094,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-09T20:59:14.542Z_

<details><summary>↩ Tool result · `toolu_01MepitRCaUgeSKQd227Ekhw`</summary>

```text
# Quantitative Findings on Weight Matrix Dynamics in SFT vs. RL Fine-Tuning

## 1. Singular Vector Directional Changes

**Principal Angles Between Subspaces (PABS):**
The paper measures directional shifts using principal angles θᵢ ∈ [0, π/2]. Key findings from Figure 4 show that "angles start around 25-30 for the leading singular vectors and rise smoothly toward 90 in the tail." This indicates substantial rotation, with 90° representing orthogonal directions.

The authors note: "the curves for supervised SFT and RL lie on top of each other," meaning both training stages produce similar rotation patterns across the spectrum.

## 2. Singular Value Stability

**Minimal Magnitude Changes:**
Figure 3 demonstrates that singular value changes (Δσᵢ) remain extremely small: "fluctuates from 0 to 0.005, as a low-magnitude, zero-centered noisy signal." The Frobenius norm of transformation energy (‖W‖²ₓ) is "largely preserved from the pre-trained model."

## 3. Recovery Through Vector Restoration

**Layer-wise Recovery:**
- Restoring top-25% of layers recovers "70 to 80 % of a model's OOD performance"
- Rank-wise restoration shows Qwen "peaks after restoring approximately 512 directions"

**Causal Evidence:**
When RL-tuned models were forced to adopt SFT's geometric orientation, OOD accuracy "plummets from 16.2% down to 10.6%" (Llama) and drops from "19.8% to 19.0%" (Qwen), confirming directional alignment's criticality.

## 4. The Orthogonal-Rotation Mechanism

**Mathematical Foundation (Appendix A.1):**
The proof demonstrates that orthogonal rotations incur O(η²) parameter cost versus O(η) for singular value changes, making rotation energetically favorable. The update rule produces strictly orthogonal matrices where "W₁'=W₁Rη" with Rη ∈ O(d_mid).

**Key Result:** "Right-multiplying by orthogonal R leaves Σ invariant but rotates the right singular vectors," explaining why SFT and RL both preferentially rotate rather than alter magnitudes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a922643b-d332-4bfe-91d6-5d0cf2409599",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "f4f81432-7b4a-41b2-a3e8-c1c3c093a5bf",
  "sourceToolAssistantUUID": "a922643b-d332-4bfe-91d6-5d0cf2409599",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-09T20:59:15.794Z_

<details><summary>↩ Tool result · `toolu_01GeJzV3BDGttdbhK35uuq4p`</summary>

```text
Web search results for query: "LLM training stages activation fingerprint "refusal direction" OR "honesty direction" "orthogonal" SFT DPO RLHF cosine 2024 2025"

Links: [{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2504.02904"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"RLHF vs DPO in LLM fine-tuning: 60+ patent analysis | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/rlhf-vs-dpo-in-llm-fine-tuning-60-patent-analysis-2/"},{"title":"A Technical Survey of Reinforcement Learning Techniques for Large Language Models","url":"https://arxiv.org/html/2507.04136v1"},{"title":"The 3 Stages of LLM Training: A Deep Dive into Reinforcement Learning from Human Feedback (RLHF) - DataSci Ocean","url":"https://datasciocean.com/en/ai-concept/llm-fine-tuning-rlhf/"},{"title":"Quagmires in SFT-RL Post-Training: When High SFT Scores Mislead and What to Use Instead","url":"https://arxiv.org/html/2510.01624v1"},{"title":"Published as a conference paper at ICLR 2025 ASYNCHRONOUS RLHF: FASTER AND MORE","url":"https://openreview.net/pdf?id=FhTAG591Ve"},{"title":"Modulating LLM's Behavior via Simple Parameter Editing","url":"https://aclanthology.org/2025.naacl-long.321.pdf"},{"title":"What Is LLM Post-Training? Best Techniques in 2025 | by Suneth Kawasaki | Medium","url":"https://medium.com/@sunethkawasaki750/what-is-llm-post-training-best-techniques-in-2025-db482d585579"},{"title":"How Post-Training Reshapes LLMs: A Mechanistic View ...","url":"https://openreview.net/pdf?id=w5DSwn9wTC"}]

Based on the web search results, I found several highly relevant papers and resources related to your query about LLM training stages, activation fingerprints, and refusal/honesty directions:

## Key Findings:

### 1. **Post-Training Mechanistic Analysis (2025)**
Recent work systematically and mechanistically studies post-trained models compared to pre-trained base models from four perspectives: knowledge storage and representation, internal belief of truthfulness, refusal behavior, and confidence. 

Researchers induce refusal behavior on harmless inputs by adding a learned direction vector to the model's representations at specific layers. They compare using truthfulness directions extracted from one model to intervene in another model, showing that transfer interventions exhibit small differences compared to same-model interventions.

### 2. **Training Pipeline Structure**
Post-training for reasoning LLMs typically consists of three stages: Supervised Fine-Tuning (SFT), an optional Direct Preference Optimization (DPO) stage, and Reinforcement Learning with Verifiable Rewards (RLVR).

The RLHF pipeline typically consists of three main stages: supervised fine-tuning where a pre-trained LLM is trained on human-written demonstrations, followed by a second stage where a reward model is trained to predict human preferences between different model outputs.

### 3. **Conflicting Results on SFT's Role**
Different prominent works show inconsistent viewpoints: some claim initial SFT is necessary for subsequent RL, while others suggest over-SFT may constrain subsequent RL, and others argue SFT generalizes poorly with RL doing better without it.

The search results contain a COLM 2025 paper and an OpenReview paper published at ICLR 2025 that appear directly relevant to mechanistic study of how training stages reshape LLMs and affect behavioral properties like refusal and truthfulness. These would be worth examining for detailed information on activation fingerprints and directional analysis across SFT, DPO, and RLHF stages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f5f53b6-477c-4b81-8b63-72ec58578b54",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "26d193c5-f22b-4eb5-876c-408fb1e24d07",
  "sourceToolAssistantUUID": "8f5f53b6-477c-4b81-8b63-72ec58578b54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-09T20:59:19.453Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JNgxhigFF1myZMatexQwwF`</summary>

```json
{
  "url": "https://openreview.net/pdf?id=w5DSwn9wTC",
  "prompt": "Extract the abstract, methodology, and all quantitative findings about how SFT, DPO, and RLHF training stages affect activation space geometry, probe directions, cosine similarity of directions, refusal directions, truthfulness directions, and any orthogonality findings. Note paper title, authors, venue."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26d193c5-f22b-4eb5-876c-408fb1e24d07",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfcuMKFvcKWQWdFmVer",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "44f82a19-2b6e-4265-86fd-5e4626cfdf03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FUWPnuwZd1zTeG8bcoq3EF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2036,
      "cache_read_input_tokens": 30802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2036,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-09T20:59:20.246Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BQUHEsWSK5eMgbnHT5Ac8U`</summary>

```json
{
  "query": "arxiv 2024 2025 \"activation space\" \"training stage\" \"SFT\" \"RLHF\" OR \"DPO\" OR \"PPO\" different direction fingerprint representation mechanistic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44f82a19-2b6e-4265-86fd-5e4626cfdf03",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfcuMKFvcKWQWdFmVer",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1aa2bfbf-0b49-4b35-a49b-56757b9cde82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FUWPnuwZd1zTeG8bcoq3EF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2036,
      "cache_read_input_tokens": 30802,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2036
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 30802,
          "cache_creation_input_tokens": 2036,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2036,
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

_source line 66 · 2026-05-09T20:59:26.438Z_

<details><summary>↩ Tool result · `toolu_01JNgxhigFF1myZMatexQwwF`</summary>

```text
I appreciate your request, but I need to be transparent: the content provided is a PDF file in binary/compressed format that I cannot meaningfully parse or extract information from.

The "web page content" consists of PDF object streams with FlateDecode compression - this is not readable text. To properly assist you, I would need:

1. **The actual paper text** - either the PDF rendered to text, or the paper's HTML/markdown version
2. **A direct link** to the paper (e.g., arXiv, conference proceedings)
3. **The paper title and authors** to help identify which research you're referencing

Once you provide readable content, I can extract:
- Abstract, methodology, and quantitative findings regarding SFT/DPO/RLHF effects on:
  - Activation space geometry
  - Probe directions and cosine similarity
  - Refusal/truthfulness directions
  - Orthogonality findings
- Proper citations (title, authors, venue)

**Would you like to share the paper in a readable format?**

[Binary content (application/pdf, 3.4MB) also saved to /home/ubuntu/.claude-account-2/projects/-/906a5f13-3f9b-4a39-87d3-524ad7b8f4e0/tool-results/webfetch-1778360360547-10k2yc.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44f82a19-2b6e-4265-86fd-5e4626cfdf03",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "4c3d90eb-5382-4a1a-9c82-81ceec0b3b1a",
  "sourceToolAssistantUUID": "44f82a19-2b6e-4265-86fd-5e4626cfdf03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-09T20:59:28.385Z_

<details><summary>↩ Tool result · `toolu_01BQUHEsWSK5eMgbnHT5Ac8U`</summary>

```text
Web search results for query: "arxiv 2024 2025 "activation space" "training stage" "SFT" "RLHF" OR "DPO" OR "PPO" different direction fingerprint representation mechanistic"

Links: [{"title":"DPO Meets PPO: Reinforced Token Optimization for RLHF","url":"https://arxiv.org/html/2404.18922v4"},{"title":"LLMOrbit: A Circular Taxonomy of Large Language Models","url":"https://arxiv.org/pdf/2601.14053"},{"title":"rlhf, rlaif, ppo, dpo and more","url":"https://arxiv.org/pdf/2407.16216"},{"title":"Reinforcement Learning from Human Feedback","url":"https://arxiv.org/html/2504.12501v3"},{"title":"Reinforcement Learning Meets Large Language Models: A Survey of","url":"https://arxiv.org/pdf/2509.16679"},{"title":"DPO Meets PPO: Reinforced Token Optimization for RLHF Han Zhong∗† Zikang Shan†","url":"https://arxiv.org/pdf/2404.18922"},{"title":"A Mechanistic Perspective from Safety Neurons","url":"https://arxiv.org/pdf/2406.14144"},{"title":"Quagmires in SFT-RL Post-Training: When High SFT Scores Mislead and What to Use Instead","url":"https://arxiv.org/html/2510.01624v1"},{"title":"On the Generalization of SFT: A Reinforcement Learning ...","url":"https://arxiv.org/pdf/2508.05629"},{"title":"Published as a conference paper at ICLR 2025 ASYNCHRONOUS RLHF: FASTER AND MORE","url":"https://openreview.net/pdf?id=FhTAG591Ve"}]

Based on the search results, I found several relevant papers from 2024-2025 that discuss activation spaces, training stages, and preference optimization methods (SFT, RLHF, DPO, PPO). Here are the key findings:

## Key Papers Found:

1. **"A Mechanistic Perspective from Safety Neurons"** (2024-2025)
   - Discusses how SN-Tune identifies safety neurons based on their contribution to residual stream on safety-related data, and how SFT can recover over 90% of DPO's safety performance
   - Examines mechanistic interpretability in the context of different training stages (SFT vs DPO)

2. **"DPO Meets PPO: Reinforced Token Optimization for RLHF"** (2024)
   - Introduces Reinforced Token Optimization (RTO), which extracts token-wise reward signals from offline preference data, using a novel token-wise reward extraction approach from direct preference optimization (DPO), and optimizes with PPO

3. **"Quagmires in SFT-RL Post-Training: When High SFT Scores Mislead and What to Use Instead"** (2025)
   - Post-training for reasoning LLMs consists of SFT, an optional DPO stage, and RLVR, where SFT serves as a "cold-start" phase, and DPO fixes/strengthens targeted behaviors

4. **"On the Generalization of SFT: A Reinforcement Learning Perspective"** (2025)
   - Recent work shows that SFT can be cast as RL with an implicit reward, with adjustments such as smaller learning rates to manage the vanishing KL constraint

These papers explore how activation spaces and model representations change across different training stages (SFT → DPO/RLHF → PPO), with mechanistic interpretability perspectives on how neurons contribute differently to model behavior in each stage.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1aa2bfbf-0b49-4b35-a49b-56757b9cde82",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "6ddae512-987c-4c91-88a3-f8a461353bb0",
  "sourceToolAssistantUUID": "1aa2bfbf-0b49-4b35-a49b-56757b9cde82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-09T20:59:32.861Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014fsKWF4bsSGQ7GvpZ2crSb`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.02904",
  "prompt": "Fetch this paper's full HTML version if available. Extract: (1) the abstract, (2) any quantitative measurements about how SFT, DPO, and RLHF change probe directions, (3) any cosine similarity values reported between directions from different training stages, (4) any claims about orthogonality, (5) findings about refusal or truthfulness directions. Note if truthfulness directions transfer well across training stages vs refusal directions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ddae512-987c-4c91-88a3-f8a461353bb0",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfdqFY3jYGmczzdzG5X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f62bfca-3649-4bbb-b351-d41e1bdf4e3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RBnpgpjcPbcLjyBoXaFnXg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 32838,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1565,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-09T20:59:34.407Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HghFGmWppyMWmDRc4ixV8r`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.02904",
  "prompt": "Find all quantitative results about cosine similarity between probe directions across training stages (base model, SFT, DPO, RLHF, RLVR). Find any specific numbers comparing how truthfulness directions vs refusal directions change across training stages. Look for tables or figures with cosine similarity values."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f62bfca-3649-4bbb-b351-d41e1bdf4e3a",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfdqFY3jYGmczzdzG5X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3abc26a-05cb-4fe3-84a4-5edf824d6777",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RBnpgpjcPbcLjyBoXaFnXg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1565,
      "cache_read_input_tokens": 32838,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1565
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 313,
          "cache_read_input_tokens": 32838,
          "cache_creation_input_tokens": 1565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1565,
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

_source line 70 · 2026-05-09T20:59:36.879Z_

<details><summary>↩ Tool result · `toolu_014fsKWF4bsSGQ7GvpZ2crSb`</summary>

```text
# Analysis of arXiv:2504.02904

## Abstract
The paper examines how post-training mechanistically reshapes LLMs across four dimensions: knowledge, truthfulness, refusal, and confidence. Key finding: "Post-training does not change the factual knowledge storage locations" while adapting representations.

## Quantitative Measurements on Direction Changes
The webpage content provided does not include specific numerical measurements about how SFT, DPO, and RLHF change probe directions. The full paper would be needed to access detailed quantitative results.

## Cosine Similarity Values
No specific cosine similarity values between directions from different training stages are reported in the available content.

## Orthogonality Claims
The document does not discuss orthogonality between directions.

## Truthfulness vs. Refusal Transferability
The study identifies a critical distinction:

**Truthfulness directions**: "The truthfulness direction is highly similar between the base and post-trained model, and it is effectively transferable for interventions."

**Refusal directions**: "The refusal direction is different between the base and post-trained models, and it shows limited forward transferability."

This contrast suggests truthfulness mechanisms remain stable across training stages while refusal mechanisms are substantially restructured during post-training.

---
*Note: Full quantitative details require accessing the complete PDF or HTML paper version.*
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f62bfca-3649-4bbb-b351-d41e1bdf4e3a",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "7bd6280f-2807-4186-bc30-4e3b1709a4bf",
  "sourceToolAssistantUUID": "3f62bfca-3649-4bbb-b351-d41e1bdf4e3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-09T20:59:39.363Z_

<details><summary>↩ Tool result · `toolu_01HghFGmWppyMWmDRc4ixV8r`</summary>

```text
# Cosine Similarity Analysis: Truthfulness vs. Refusal Directions

## Truthfulness Direction Similarity

The paper reports **high cosine similarity** for truthfulness directions across training stages:

**Figure 3(a-b)** displays heatmaps showing "high cosine similarity" between base, SFT, and instruct models' truthfulness directions on the inventors and animal_class datasets.

**Table 2** demonstrates probe transfer accuracy with minimal performance degradation:
- Base-to-SFT transfer: differences range from -0.37% to +2.15%
- Base-to-instruct transfer: differences range from -2.29% to +3.76%

These negligible variations indicate preserved internal representations.

## Refusal Direction Similarity

The paper reports **low cosine similarity** for refusal directions:

**Figure 3(c)** shows that the refusal direction from base models has "very low cosine similarity" with SFT and instruct variants.

**Table 4** quantifies this divergence through intervention effectiveness:
- Base refusal direction applied to instruct for harmful inputs: 0.95 vs. 0.36 baseline
- Harmless inputs show dramatic failure: 0.08 vs. 0.98 expected performance

## Key Distinction

The paper explicitly contrasts mechanisms: truthfulness direction demonstrates effective forward transferability while refusal direction does not, indicating post-training fundamentally restructures safety mechanisms but preserves factual-knowledge representations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3abc26a-05cb-4fe3-84a4-5edf824d6777",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "4c9cdc61-14b7-4ebc-87c2-c74d4167a579",
  "sourceToolAssistantUUID": "a3abc26a-05cb-4fe3-84a4-5edf824d6777",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-09T20:59:41.718Z_

This is a significant finding. Let me get one more targeted search to look for any work that specifically quantifies SFT vs RL probe direction geometry with cosine values close to -0.07.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c9cdc61-14b7-4ebc-87c2-c74d4167a579",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011Casfee6ba2qJj5iwz1ZZN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b00564e1-1a19-4efa-9d8f-81d03e85091b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C6wbovDZfqZuWLUTZ5baTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1012,
      "cache_read_input_tokens": 34403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1012,
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

_source line 73 · 2026-05-09T20:59:42.603Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QCLUdYmKzFSHymbxGbxqjQ`</summary>

```json
{
  "query": "\"cosine similarity\" \"-0.07\" OR \"near zero\" SFT RL RLHF probe direction activation 2024 2025 LLM arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b00564e1-1a19-4efa-9d8f-81d03e85091b",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011Casfee6ba2qJj5iwz1ZZN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "727734a1-e26a-4fb3-84b5-4e41601e1712",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C6wbovDZfqZuWLUTZ5baTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1012,
      "cache_read_input_tokens": 34403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1012,
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

_source line 74 · 2026-05-09T20:59:43.283Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ETw3A8BNx8Cu6WgTyNh7Bu`</summary>

```json
{
  "query": "probe transfer SFT RLHF reward hacking detection activation directions 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "727734a1-e26a-4fb3-84b5-4e41601e1712",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011Casfee6ba2qJj5iwz1ZZN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ebfe713-b7ab-43c9-80fd-5a743cf9e17e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01C6wbovDZfqZuWLUTZ5baTo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1012,
      "cache_read_input_tokens": 34403,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1012
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 34403,
          "cache_creation_input_tokens": 1012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1012,
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

_source line 75 · 2026-05-09T20:59:49.626Z_

<details><summary>↩ Tool result · `toolu_01QCLUdYmKzFSHymbxGbxqjQ`</summary>

```text
Web search results for query: ""cosine similarity" "-0.07" OR "near zero" SFT RL RLHF probe direction activation 2024 2025 LLM arXiv"

Links: [{"title":"Probe-Based Data Attribution: Discovering and Mitigating Undesirable","url":"https://arxiv.org/pdf/2602.11079"},{"title":"Solving the Inverse Alignment Problem for Efficient RLHF","url":"https://arxiv.org/html/2412.10529v1"},{"title":"arXiv:2412.10529v1 [cs.LG] 13 Dec 2024","url":"https://arxiv.org/pdf/2412.10529"},{"title":"A Systematic Evaluation of Preference Aggregation in ...","url":"https://arxiv.org/pdf/2512.08786"},{"title":"Demystifying Long Chain-of-Thought Reasoning in LLMs","url":"https://arxiv.org/pdf/2502.03373"},{"title":"A First-Order Logic–Based Alternative to Reward Models in RLHF","url":"https://arxiv.org/html/2512.14100v1"},{"title":"Is Cosine-Similarity of Embeddings Really About Similarity? Harald Steck","url":"https://arxiv.org/pdf/2403.05440"},{"title":"Published as a conference paper at ICLR 2025 ASYNCHRONOUS RLHF: FASTER AND MORE","url":"https://openreview.net/pdf?id=FhTAG591Ve"},{"title":"Reinforcement Learning from Human Feedback","url":"https://arxiv.org/html/2504.12501v3"},{"title":"arXiv:2505.17769v2 [cs.LG] 12 Jun 2025","url":"https://arxiv.org/pdf/2505.17769"}]

I found several relevant research papers from arXiv related to your search query. Here are the most relevant results:

## Key Findings

The search returned papers from 2024-2025 discussing LLMs, probing, activation analysis, and RLHF/SFT techniques:

1. **Probe-Based Data Attribution** - Research has shown that specific behaviors in LLMs can be localized to directions in activation space, and activation addition demonstrates that adding vectors to activations can steer model behavior. This paper (arXiv:2602.11079) uses cosine similarities between behavior change vectors and datapoint vectors, clustered using Ward's method, which directly relates to your search terms about cosine similarity and probe directions.

2. **RLHF and Efficient Training** - Several papers discuss cosine similarity measures for comparing embeddings as part of RLHF frameworks, with supervised fine-tuning (SFT) as the first step, followed by RLHF involving optimizing a policy based on scores from a reward model.

3. **Long Chain-of-Thought in LLMs** - Recent work explores cosine length-scaling rewards with repetition penalties to stabilize CoT growth while encouraging emergent reasoning behaviors.

The papers discuss activation space analysis, probe vectors, and their relationships to model behavior changes - which appears to match your interest in understanding how probe directions relate to cosine similarity values near zero in SFT vs RLHF models.

Would you like me to search for more specific information about any particular aspect of these results?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "727734a1-e26a-4fb3-84b5-4e41601e1712",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "e164f61f-2ffd-48cc-aefb-32ddb05a04f0",
  "sourceToolAssistantUUID": "727734a1-e26a-4fb3-84b5-4e41601e1712",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-09T20:59:51.439Z_

<details><summary>↩ Tool result · `toolu_01ETw3A8BNx8Cu6WgTyNh7Bu`</summary>

```text
Web search results for query: "probe transfer SFT RLHF reward hacking detection activation directions 2024 2025 arXiv"

Links: [{"title":"Seeking arXiv cs.LG endorsement for paper on probe transfer failure in reward hacking detection - Research - Hugging Face Forums","url":"https://discuss.huggingface.co/t/seeking-arxiv-cs-lg-endorsement-for-paper-on-probe-transfer-failure-in-reward-hacking-detection/174565"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/html/2502.18770v3"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/html/2604.02986"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/html/2602.10623"},{"title":"[2510.13694] Information-Theoretic Reward Modeling for Stable RLHF: Detecting and Mitigating Reward Hacking","url":"https://arxiv.org/abs/2510.13694"},{"title":"NATURAL EMERGENT MISALIGNMENT FROM REWARD HACKING IN PRODUCTION RL","url":"https://assets.anthropic.com/m/74342f2c96095771/original/Natural-emergent-misalignment-from-reward-hacking-paper.pdf"},{"title":"[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://ar5iv.labs.arxiv.org/html/2502.18770"},{"title":"Reward Hacking Mitigation using Verifiable Composite Rewards","url":"https://arxiv.org/html/2509.15557"},{"title":"InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling","url":"https://arxiv.org/html/2402.09345v5"}]

Based on the search results, I found several relevant papers and research on probe transfer, activation directions, and reward hacking detection in SFT and RLHF contexts from 2024-2025 on arXiv:

## Key Findings

**Probe Transfer Failure in Reward Hacking Detection:**
A recent paper discusses activation probe transfer failure for reward hacking detection, testing whether probes trained on the School of Reward Hacks dataset transfer to GRPO-induced reward seeking. The research shows that the SFT and RL probe directions are nearly orthogonal (cosine = -0.07), indicating that probes trained on one setting do not effectively transfer to another.

**Detection and Mitigation Approaches:**

Several papers address reward hacking detection using activation-based approaches:

1. InfoRM proposes an information-theoretic reward modeling framework based on the Information Bottleneck principle, which filters out preference-irrelevant information to alleviate reward misgeneralization. The work presents Mahalanobis Outlier Probability (MOP), a statistical metric for quantifying reward hacking severity, enabling principled hyperparameter tuning and online mitigation such as early stopping.

2. Outliers in the Information Bottleneck latent space of InfoRM usually signify overoptimized samples, and using InfoRM significantly reduces the emergence of overoptimized samples.

**Other Mitigation Strategies:**

Penalizing reward hacking during training either with an HHH preference model reward (with sufficiently high weight) or a dedicated reward-hacking classifier is effective in preventing RL from incentivizing reward hacking.

The research landscape shows active work on detection mechanisms using activation directions and latent space representations, though the challenge of probe transfer across different training regimes remains significant.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ebfe713-b7ab-43c9-80fd-5a743cf9e17e",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "9cb9bd76-157e-458f-90ca-147a4ae5127e",
  "sourceToolAssistantUUID": "4ebfe713-b7ab-43c9-80fd-5a743cf9e17e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-09T20:59:54.475Z_

Critical finding. The Hugging Face forum post mentions the exact cosine = -0.07 figure. Let me fetch that immediately.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cb9bd76-157e-458f-90ca-147a4ae5127e",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasffXjt7XMWjPJWRYdhk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ae815a4f-041e-47db-ba5c-45099a819f3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01R57Wgxr8xxP2zzNW6rJpLN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2080,
      "cache_read_input_tokens": 35415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2080,
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

_source line 78 · 2026-05-09T20:59:56.559Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PPeezTEYPJ5rp4PQQhpqCr`</summary>

```json
{
  "url": "https://discuss.huggingface.co/t/seeking-arxiv-cs-lg-endorsement-for-paper-on-probe-transfer-failure-in-reward-hacking-detection/174565",
  "prompt": "Extract all details from this forum post: the paper title, authors, abstract or summary, methodology, key findings (especially the claim about SFT and RL probe directions being nearly orthogonal with cosine = -0.07), what datasets were used, what models were used, and the current status of this work (is it on arXiv? Is it submitted somewhere?). Get all details available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae815a4f-041e-47db-ba5c-45099a819f3c",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasffXjt7XMWjPJWRYdhk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "180fc070-ecb5-4ed2-bb51-ee330da27aec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01R57Wgxr8xxP2zzNW6rJpLN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2080,
      "cache_read_input_tokens": 35415,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2080
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 35415,
          "cache_creation_input_tokens": 2080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2080,
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

_source line 79 · 2026-05-09T21:00:00.716Z_

<details><summary>↩ Tool result · `toolu_01PPeezTEYPJ5rp4PQQhpqCr`</summary>

```text
# Forum Post Analysis: arXiv Endorsement Request

## Available Information

**Paper Title:** Not explicitly stated in the post

**Authors:** Amanhij (poster); builds on work by Wilhelm et al. 2026, Taufeeque et al. 2026, and Gupta & Jenner 2025

**Abstract/Summary:** The research examines whether activation probes trained on one dataset transfer to different reward-seeking scenarios. The author states: "I test whether probes trained on the School of Reward Hacks dataset (Taylor et al. 2025) transfer to GRPO-induced reward seeking. They don't."

**Key Finding:** The critical discovery involves directional alignment—"The SFT and RL probe directions are nearly orthogonal (cosine = -0.07)," indicating minimal correlation between probe directions across these training paradigms.

**Datasets Used:**
- School of Reward Hacks (Taylor et al. 2025)
- GRPO-induced reward seeking scenarios

**Models Used:** Not specified in the post

**Methodology:** Activation probe transfer testing and cosine similarity analysis

**Current Status:** Not yet on arXiv. The author notes: "Paper will be visible on arXiv once endorsed and submitted," indicating the endorsement request precedes publication.

**Additional Context:** Work builds on mechanistic interpretability research presented at NeurIPS MechInterp Workshop.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "180fc070-ecb5-4ed2-bb51-ee330da27aec",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "847bcdd4-6354-425c-9ebd-bf7d9994b386",
  "sourceToolAssistantUUID": "180fc070-ecb5-4ed2-bb51-ee330da27aec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 80 · 2026-05-09T21:00:03.337Z_

This is the smoking gun. Now I have everything needed for a complete report. Let me do one final search to look for any additional empirical work on activation geometry across training stages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "847bcdd4-6354-425c-9ebd-bf7d9994b386",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfgDRLqyzpWw89yuges",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52dc4199-bf7a-4ec9-9cdf-62c6162e6c46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0143YbtmrYP3cckFScSUp7Ei",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 37495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 556,
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

_source line 81 · 2026-05-09T21:00:04.392Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q63jZV44DgfcjEvABeofbo`</summary>

```json
{
  "query": "LLM \"effective rank\" OR \"intrinsic dimensionality\" SFT RLHF DPO activation representation geometry empirical 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52dc4199-bf7a-4ec9-9cdf-62c6162e6c46",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfgDRLqyzpWw89yuges",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "782805a8-c72f-4909-b86c-5583292f6cbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0143YbtmrYP3cckFScSUp7Ei",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 37495,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 556
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 37495,
          "cache_creation_input_tokens": 556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 556,
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

_source line 82 · 2026-05-09T21:00:09.798Z_

<details><summary>↩ Tool result · `toolu_01Q63jZV44DgfcjEvABeofbo`</summary>

```text
Web search results for query: "LLM "effective rank" OR "intrinsic dimensionality" SFT RLHF DPO activation representation geometry empirical 2024 2025 arXiv"

Links: [{"title":"arXiv:2506.08446v1 [cs.AI] 10 Jun 2025 A SURVEY ON LARGE LANGUAGE MODELS FOR","url":"https://arxiv.org/pdf/2506.08446"},{"title":"Language Models as Continuous Self-Evolving Data Engineers","url":"https://arxiv.org/html/2412.15151v2"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=WjKea8bGFF"},{"title":"InSPO: Unlocking Intrinsic Self-Reflection for LLM Preference Optimization","url":"https://arxiv.org/html/2512.23126"},{"title":"A Comprehensive Survey of Direct Preference Optimization: Datasets, Theories, Variants, and Applications","url":"https://arxiv.org/html/2410.15595v3"},{"title":"A Comprehensive Survey of Datasets, Theories, Variants, and Applications in Direct Preference Optimization","url":"https://arxiv.org/html/2410.15595v1"},{"title":"Published as a conference paper at ICLR 2025 ASYNCHRONOUS RLHF: FASTER AND MORE","url":"https://openreview.net/pdf?id=FhTAG591Ve"},{"title":"arXiv:2503.19201v1 [cs.LG] 24 Mar 2025","url":"https://arxiv.org/pdf/2503.19201"},{"title":"On the Evolution of Federated Post-Training Large Language Models: A Model Accessibility View","url":"https://arxiv.org/html/2508.16261"},{"title":"1 Reasoning Beyond Limits: Advances and Open Problems for LLMs","url":"https://arxiv.org/pdf/2503.22732"}]

I've performed a web search for your query about LLM "effective rank" or "intrinsic dimensionality" in relation to SFT, RLHF, DPO, and activation representation geometry. 

The search results primarily returned recent surveys and papers (2024-2025) on DPO, RLHF, and related preference optimization methods from arXiv. However, the results don't contain specific papers focused on "effective rank" or "intrinsic dimensionality" of neural network activations during different fine-tuning stages (SFT, RLHF, DPO).

The results do cover:
- Empirical and theoretical analyses of DPO, including its limitations compared to RLHF, such as asymmetric optimization dynamics
- Comparative empirical studies showing DPO's stability compared to RLHF
- Studies using dimensionality reduction techniques (t-SNE) to visualize distribution shifts in synthetic data for SFT and DPO training

If you're looking for papers specifically analyzing the representational geometry and intrinsic dimensionality of activations across different fine-tuning methods, you may need to search with more specific terms or check specialized venues focused on mechanistic interpretability, neural network analysis, or representational learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "782805a8-c72f-4909-b86c-5583292f6cbf",
  "isSidechain": true,
  "promptId": "904d16f5-e68c-48e6-acc6-4627332f7901",
  "agentId": "a2fba1c8859d87ffe",
  "type": "user",
  "uuid": "c0e97a60-a637-459b-bdee-57383bf2f981",
  "sourceToolAssistantUUID": "782805a8-c72f-4909-b86c-5583292f6cbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 83 · 2026-05-09T21:01:15.618Z_

I now have enough to write a thorough, well-sourced report. Here is the complete analysis:

---

## Research Report: SFT vs. RL Activation Space Geometry and the "cosine = -0.07" Claim

---

### (a) What published work supports or contradicts the claim that SFT and RL produce orthogonal probe directions?

**The origin of the exact claim has been traced.** The specific number "cosine = -0.07" appears in an unpublished Hugging Face forum post in which a researcher (username "Amanhij") sought arXiv cs.LG endorsement for a paper titled something like "Probe Transfer Failure in Reward Hacking Detection." The post describes testing whether probes trained on the School of Reward Hacks dataset (Taylor et al. 2025) transfer to GRPO-induced reward seeking, finding they do not, and reporting: "The SFT and RL probe directions are nearly orthogonal (cosine = −0.07)." The work builds on mechanistic interpretability presented at NeurIPS MechInterp Workshop and cites Wilhelm et al. 2026, Taufeeque et al. 2026, and Gupta & Jenner 2025. As of the search date, **this paper was not yet on arXiv** — it was awaiting endorsement before submission. This is almost certainly the "unpublished mechanistic work (pending arXiv)" your paper cites.

**Assessment:** The citation is circular — your paper appears to be citing the same grey-literature forum post that your reviewer cannot verify. The claim itself may be empirically real, but it has not been peer-reviewed or even formally preprinted.

**No other published work directly reports a cosine similarity of approximately −0.07 between SFT and RL probe directions.** However, several published papers provide related and partially corroborating findings:

1. **"RL Is Neither a Panacea Nor a Mirage" (arXiv:2508.16546, Jin et al., Aug 2025)** — This is the closest published support. The paper uses SVD-based spectral analysis to track geometric shifts across SFT and then RL fine-tuning. It finds that: (i) both SFT and RL preferentially *rotate* singular vectors rather than change their magnitudes; (ii) the principal angles between pre-training and post-SFT subspaces reach toward 90 degrees in the tail; (iii) RL's mechanism is to counteract SFT-induced directional drift rather than find new solutions. Critically, the paper reports that "angles start around 25–30° for the leading singular vectors and rise smoothly toward 90° in the tail," and that forcing RL-tuned models to adopt SFT's geometric orientation collapses OOD performance. This paper does not report probe-level cosine similarity, but the mathematical proof in Appendix A.1 shows that orthogonal rotations (O(η²) cost) are energetically preferred over singular value changes, providing a mechanistic basis for why SFT and RL probe directions could diverge substantially.

2. **"How Post-Training Reshapes LLMs: A Mechanistic View" (arXiv:2504.02904, Du et al., COLM 2025)** — This paper directly measures direction transfer across training stages using linear probes. It finds a stark asymmetry: **truthfulness directions are highly similar (high cosine similarity) across base, SFT, and instruct models** (probe transfer accuracy differs by only −0.37% to +3.76%), while **refusal directions show very low cosine similarity between base and SFT/instruct models** with catastrophic transfer failure. This is the best published quantitative evidence that different training stages can produce probe directions that are geometrically very different — directly supporting the general principle your paper invokes, though not with the specific −0.07 value.

3. **"Tracing the Representation Geometry of Language Models from Pretraining to Post-training" (arXiv:2509.23024, Li et al., Sep 2025)** — Analyzes the Tülu-3.1 pipeline (LLaMA-3.1-8B → SFT → DPO → RLVR) using spectral metrics (RankMe and αReQ). It finds that SFT and DPO induce entropy-seeking dynamics (expanding the representational manifold) while RLVR induces compression-seeking dynamics (contracting toward reward-aligned directions). This is consistent with SFT and RL directions being geometrically distinct, but the paper operates at the level of covariance eigenspectrum, not individual probe cosine similarity.

**Summary:** No published paper directly reports a cosine of approximately −0.07 between SFT and RL probe directions. The claim originates from an unendorsed, unsubmitted paper. However, published work does establish that SFT and RL produce different directional effects in activation/parameter space, and that probes from one stage can fail to transfer to another — making the general claim plausible, but the specific number unverifiable.

---

### (b) Published work characterizing how different post-training stages change activation geometry

Here is the landscape of relevant published/peer-reviewed work:

| Paper | arXiv ID | Key Geometry Finding |
|---|---|---|
| "RL Is Neither a Panacea Nor a Mirage" (Jin et al.) | 2508.16546 | SFT and RL both rotate weight matrix singular vectors; RL counteracts SFT-induced rotational drift; principal angles approach 90° in spectral tail |
| "Tracing Representation Geometry" (Li et al.) | 2509.23024 | SFT/DPO are entropy-seeking (expand manifold); RLVR is compression-seeking; measured via RankMe and αReQ on OLMo and Pythia |
| "How Post-Training Reshapes LLMs" (Du et al.) | 2504.02904 | Truthfulness probe directions preserved across SFT/instruct (high cosine); refusal probe directions restructured (low cosine, probe transfer fails) |
| "RL Squeezes, SFT Expands" (Matsutani et al.) | 2509.21128 | RL compresses reasoning trajectories (~2.5× decay rate increase), SFT expands them (decay rate reduced to ~1/3); analyzed via reasoning graph topology |
| "Detecting Contamination from RL Post-training" (Tao et al.) | 2510.09259 | RL post-training collapses output entropy into sparse modes; existing contamination probes (trained on SFT-phase signals) near-random for RL; ICLR 2026 |
| "DICE" (Tu et al.) | 2406.04197 | Layer-specific activation classifiers can detect fine-tuning contamination; contamination layer identification; R² 0.61–0.75 |
| "Linear Representation Hypothesis" (Park et al.) | 2311.03658 | Foundational: concepts that vary freely of each other are represented as orthogonal vectors under the causal inner product; ICML 2024 |

The most empirically precise characterization of how stages differ in activation geometry comes from arXiv:2504.02904, which actually measures probe direction cosine similarities across stages (high for truthfulness, low/failing for refusal), and arXiv:2508.16546, which measures principal angles between singular vector subspaces before and after each training stage.

---

### (c) Recommended empirical analysis to replace the unverifiable citation

Rather than citing an unpublished forum post, the paper can add a credible and verifiable analysis section. Here are three concrete options, ordered by cost/feasibility:

**Option 1 (Recommended — Low cost, fully verifiable):** Compute the cosine similarity between mean-difference probe directions extracted at multiple layers from an openly available model pair such as Llama-3-8B-SFT and Llama-3-8B-RLVR from the Tülu-3.1 release (already public). Train a binary linear probe on residual stream activations for SFT-phase contaminated vs. clean inputs, then train a second probe for RL-phase contaminated vs. clean inputs, and report the cosine similarity between these two probe vectors layer-by-layer. This is directly reproducible and directly motivated by arXiv:2504.02904's methodology. Expected result: low cosine similarity for stages that induce qualitatively different behaviors, consistent with the refusal-direction finding in that paper. Report the layer-wise profile rather than a single scalar.

**Option 2 (Medium cost):** Use the DICE framework (arXiv:2406.04197) but apply it separately to SFT-contaminated and RL-contaminated models. Report the layer sensitivity profiles and show that the "most contamination-sensitive layer" differs between SFT-contaminated and RL-contaminated models. This both motivates your fingerprinting approach and provides a citable, reproducible empirical baseline.

**Option 3 (Reframing with published results):** Instead of claiming a specific cosine of −0.07 from an unverifiable source, cite arXiv:2504.02904 for the principle that post-training stages produce substantially different probe directions (demonstrated for refusal, with near-zero transfer accuracy), and cite arXiv:2509.23024 for the opposing entropy-seeking (SFT) vs. compression-seeking (RLVR) directional dynamics. Frame the stage-specific probe orthogonality as a natural prediction of both frameworks, which your method is designed to exploit, rather than an observed empirical fact from unpublished work.

For the citation text, a revised version might read: "Activation probes trained on SFT-stage behavior have been shown to transfer poorly to RL-stage behavior — and vice versa — consistent with the geometric divergence between training stages characterized in recent work on post-training representation dynamics (Du et al., arXiv:2504.02904; Li et al., arXiv:2509.23024; Jin et al., arXiv:2508.16546). We replicate and extend this finding in Section X by measuring inter-stage probe cosine similarities directly on [model]."

---

**Bottom line for the reviewer response:** The specific "cosine ≈ −0.07" figure traces to an unendorsed, unsubmitted manuscript circulated via a Hugging Face forum post — it is not peer-reviewed and does not meet the bar for citation. The reviewer's concern is fully warranted. The general claim (SFT and RL probes are geometrically distinct) is supported by published work, especially arXiv:2504.02904 (COLM 2025), 2508.16546, and 2509.23024, but no published paper reports that specific cosine value. The paper should either replace the citation with one of the above published sources (Option 3) or run the analysis itself (Options 1–2) and convert the claim into a primary contribution.

---

Sources:
- [RL Is Neither a Panacea Nor a Mirage (arXiv:2508.16546)](https://arxiv.org/html/2508.16546v1)
- [How Post-Training Reshapes LLMs: A Mechanistic View (arXiv:2504.02904)](https://arxiv.org/html/2504.02904)
- [Tracing the Representation Geometry from Pretraining to Post-training (arXiv:2509.23024)](https://arxiv.org/html/2509.23024)
- [RL Squeezes, SFT Expands (arXiv:2509.21128)](https://arxiv.org/html/2509.21128v1)
- [Detecting Data Contamination from RL Post-training (arXiv:2510.09259)](https://arxiv.org/html/2510.09259)
- [DICE: Detecting In-distribution Contamination (arXiv:2406.04197)](https://arxiv.org/abs/2406.04197)
- [The Linear Representation Hypothesis and the Geometry of LLMs (arXiv:2311.03658)](https://arxiv.org/abs/2311.03658)
- [Probe-Based Data Attribution (arXiv:2602.11079)](https://arxiv.org/html/2602.11079)
- [Exploring the LLM Journey from Cognition to Expression (arXiv:2405.16964)](https://arxiv.org/html/2405.16964)
- [Hugging Face Forum: Probe transfer failure in reward hacking detection](https://discuss.huggingface.co/t/seeking-arxiv-cs-lg-endorsement-for-paper-on-probe-transfer-failure-in-reward-hacking-detection/174565)
- [A Mechanistic Understanding of Alignment Algorithms: DPO and Toxicity (arXiv:2401.01967)](https://arxiv.org/abs/2401.01967)
- [The Geometry of Persona (arXiv:2512.07092)](https://arxiv.org/html/2512.07092)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0e97a60-a637-459b-bdee-57383bf2f981",
  "isSidechain": true,
  "agentId": "a2fba1c8859d87ffe",
  "requestId": "req_011CasfgtGgsY3vnnK5KaJ7p",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "253bb722-2d45-4205-808a-c4d6715f397c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "906a5f13-3f9b-4a39-87d3-524ad7b8f4e0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GvKX9Fk1Qjn62hou55nyGB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1056,
      "cache_read_input_tokens": 38051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1056,
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
