# Research conversation: I need to verify the exact performance numbers for the paper "Imagine-then-Plan: Agent Learning from Adaptive Lookahead 

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aeb9052a04aec7401.jsonl`
- **Structured JSON:** [`2fcc8245ac7a5dc5ac49.json`](../../sessions/2f/2fcc8245ac7a5dc5ac49.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-12T00:50:22.443Z_

I need to verify the exact performance numbers for the paper "Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models" (ITP/ITP-R, arXiv 2601.08955, Jan 2026).

Specifically, I need to know:
1. What is ITP-R's OVERALL success rate on ALFWorld with Qwen2.5-7B backbone? There is a dispute: one claim says 94.29% (overall), another says 94.29% is only the PICK subtask and the overall is 85.07%.
2. What are the per-subtask scores (PICK, CLEAN, HEAT, COOL, LOOK, PICK2)?
3. What is ITP-R's performance on ScienceWorld with Qwen2.5-7B?

Please search for this paper using WebSearch and try to fetch the actual paper or its results table using WebFetch. Try multiple sources:
- arxiv.org/abs/2601.08955
- The HTML version at arxiv.org/html/2601.08955
- Any blog posts or reviews discussing ITP-R results

Report the exact numbers you find, specifying which table/figure they come from. This is critical for a research review - I need the ground truth.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "540c002c-9999-471e-b32d-70c2ebec2c01",
  "agentId": "aeb9052a04aec7401",
  "type": "user",
  "uuid": "41403670-1058-4771-9eda-3e0129acea2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:50:22.447Z_

```json
{
  "parentUuid": "41403670-1058-4771-9eda-3e0129acea2f",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
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
  "uuid": "02091cbf-c1e2-4e36-9adc-f41bc5acf854",
  "timestamp": "2026-05-12T00:50:22.447Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:50:24.969Z_



I'll help you verify the exact performance numbers from this paper. Let me start by loading the WebSearch and WebFetch tools, then search for the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02091cbf-c1e2-4e36-9adc-f41bc5acf854",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011CawkruTWFbmEG2W5hFcQ2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f48a798c-aadd-4307-9874-6995ece8bd7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DctAhEQvthbXXtHpn8f8uM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 845,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 845,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T00:50:25.336Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014msYejadNSBQS2ci59KcmW`</summary>

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
  "parentUuid": "f48a798c-aadd-4307-9874-6995ece8bd7d",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011CawkruTWFbmEG2W5hFcQ2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98080160-a8aa-4678-9981-eb10169a7ad5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DctAhEQvthbXXtHpn8f8uM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 845,
      "cache_read_input_tokens": 8223,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 845
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 114,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 845,
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

_source line 5 · 2026-05-12T00:50:25.341Z_

<details><summary>↩ Tool result · `toolu_014msYejadNSBQS2ci59KcmW`</summary>

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
  "parentUuid": "98080160-a8aa-4678-9981-eb10169a7ad5",
  "isSidechain": true,
  "promptId": "540c002c-9999-471e-b32d-70c2ebec2c01",
  "agentId": "aeb9052a04aec7401",
  "type": "user",
  "uuid": "bb5e9907-314d-4c6f-93a1-202d50306846",
  "sourceToolAssistantUUID": "98080160-a8aa-4678-9981-eb10169a7ad5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T00:50:27.780Z_



Now let me search for the paper and fetch its content from multiple sources in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb5e9907-314d-4c6f-93a1-202d50306846",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011Cawks8Gw4xajTFCnHnuWr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d81047e9-f3bd-49fe-a13a-7d78c846f760",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PHYwmTBAzbNLPpMGzFDjSP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 9068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1923,
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

_source line 7 · 2026-05-12T00:50:29.706Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012nyPnz2GnAvPYtSrP28k8u`</summary>

```json
{
  "query": "Imagine-then-Plan Agent Learning Adaptive Lookahead World Models ITP-R arXiv 2601.08955 ALFWorld results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d81047e9-f3bd-49fe-a13a-7d78c846f760",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011Cawks8Gw4xajTFCnHnuWr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09df206d-fdc0-4544-b591-822d3f0d59d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PHYwmTBAzbNLPpMGzFDjSP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 9068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1923,
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

_source line 8 · 2026-05-12T00:50:31.091Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01B7QnjdJx3JmdhgZwXdHwTG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.08955",
  "prompt": "Extract the full abstract and any information about results, tables, or performance numbers mentioned on this page for the paper \"Imagine-then-Plan\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09df206d-fdc0-4544-b591-822d3f0d59d3",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011Cawks8Gw4xajTFCnHnuWr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b796858-7329-4ef7-80dd-c311dfa2c76f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PHYwmTBAzbNLPpMGzFDjSP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 9068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1923,
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

_source line 9 · 2026-05-12T00:50:33.899Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NcUR8WAdYaiQWQERntCTdz`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.08955",
  "prompt": "Extract ALL performance tables from this paper. I need: 1) The ALFWorld results table with ITP-R using Qwen2.5-7B backbone - specifically the OVERALL success rate and all per-subtask scores (PICK, CLEAN, HEAT, COOL, LOOK, PICK2). 2) The ScienceWorld results table with ITP-R using Qwen2.5-7B. Report exact numbers, table numbers, and table captions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b796858-7329-4ef7-80dd-c311dfa2c76f",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011Cawks8Gw4xajTFCnHnuWr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d30c619e-476b-4719-a1bd-be74938d22f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PHYwmTBAzbNLPpMGzFDjSP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 9068,
      "output_tokens": 371,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1923
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 371,
          "cache_read_input_tokens": 9068,
          "cache_creation_input_tokens": 1923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1923,
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

_source line 10 · 2026-05-12T00:50:35.723Z_

<details><summary>↩ Tool result · `toolu_01B7QnjdJx3JmdhgZwXdHwTG`</summary>

```text
# Imagine-then-Plan: Paper Summary

**Full Abstract:**

"Recent advances in world models have shown promise for modeling future dynamics of environmental states, enabling agents to reason and act without accessing real environments." The paper introduces ITP, a unified framework where agents interact with learned world models to generate multi-step imagined trajectories. A key innovation is an adaptive lookahead mechanism that adjusts the imagination horizon based on task requirements. The imagined trajectories provide signals about future progress and potential conflicts, which combine with current observations to guide policy learning through a partially observable and imaginable Markov decision process. The authors present both training-free and reinforcement-trained variants.

**Results and Performance:**

The page does not contain specific numerical results, performance benchmarks, or tables. It only states that "Extensive experiments across representative agent benchmarks demonstrate that ITP significantly outperforms competitive baselines" and that "further analyses validate that our adaptive lookahead largely enhances agents' reasoning capability."

**Additional Information:**

The code and data are promised to be "publicly available" through a GitHub repository (URL referenced but not fully displayed on the page).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b796858-7329-4ef7-80dd-c311dfa2c76f",
  "isSidechain": true,
  "promptId": "540c002c-9999-471e-b32d-70c2ebec2c01",
  "agentId": "aeb9052a04aec7401",
  "type": "user",
  "uuid": "7c9bcb32-e4c7-489f-8645-ba2013ebd99b",
  "sourceToolAssistantUUID": "3b796858-7329-4ef7-80dd-c311dfa2c76f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-12T00:50:37.172Z_

<details><summary>↩ Tool result · `toolu_012nyPnz2GnAvPYtSrP28k8u`</summary>

```text
Web search results for query: "Imagine-then-Plan Agent Learning Adaptive Lookahead World Models ITP-R arXiv 2601.08955 ALFWorld results"

Links: [{"title":"[2601.08955] Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models","url":"https://arxiv.org/abs/2601.08955"},{"title":"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models","url":"https://arxiv.org/html/2601.08955v1"},{"title":"Paper page - Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models","url":"https://huggingface.co/papers/2601.08955"},{"title":"GitHub - loyiv/ITP: Code of Paper: Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models · GitHub","url":"https://github.com/loyiv/ITP"},{"title":"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models | Takara TLDR","url":"https://tldr.takara.ai/p/2601.08955"},{"title":"Agent Learning from Adaptive Lookahead with World Models","url":"https://www.semanticscholar.org/paper/Imagine-then-Plan:-Agent-Learning-from-Adaptive-Liu-Wang/f53634fdcc0a42d6e7e7ff7581494347d8cce6a8"},{"title":"(PDF) Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models","url":"https://www.researchgate.net/publication/399777126_Imagine-then-Plan_Agent_Learning_from_Adaptive_Lookahead_with_World_Models"},{"title":"Top arXiv papers","url":"https://scirate.com/?date=2026-01-15&page=18&range=3"},{"title":"Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2601.08955"},{"title":"ai-agent-papers/capability-papers/environment.md at main · masamasa59/ai-agent-papers","url":"https://github.com/masamasa59/ai-agent-papers/blob/main/capability-papers/environment.md"}]

Based on the search results, here's what I found about the paper "Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models":

## Overview

The paper proposes Imagine-then-Plan (ITP), a unified framework for agent learning via lookahead imagination, where an agent's policy model interacts with the learned world model, yielding multi-step "imagined" trajectories.

## Key Innovation

Since the imagination horizon may vary by tasks and stages, the paper introduces a novel adaptive lookahead mechanism by trading off the ultimate goal and task progress. The resulting imagined trajectories provide rich signals about future consequences, such as achieved progress and potential conflicts, which are fused with current observations, formulating a partially observable and imaginable Markov decision process to guide policy learning.

## Implementation and Results

The authors instantiate ITP with both training-free and reinforcement-trained variants. Extensive experiments across representative agent benchmarks demonstrate that ITP significantly outperforms competitive baselines. Further analyses validate that the adaptive lookahead largely enhances agents' reasoning capability, providing valuable insights into addressing broader, complex tasks.

## Paper Details

- **Authors**: Youwei Liu, Jian Wang, Hanlin Wang, Beichen Guo, and Wenjie Li
- **Affiliation**: The Hong Kong Polytechnic University and Central South University
- **arXiv ID**: 2601.08955
- **Posted**: January 13, 2026
- **Code**: Available at https://github.com/loyiv/ITP


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09df206d-fdc0-4544-b591-822d3f0d59d3",
  "isSidechain": true,
  "promptId": "540c002c-9999-471e-b32d-70c2ebec2c01",
  "agentId": "aeb9052a04aec7401",
  "type": "user",
  "uuid": "028cd716-d85c-4310-92f1-0a86aff9a593",
  "sourceToolAssistantUUID": "09df206d-fdc0-4544-b591-822d3f0d59d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T00:50:37.676Z_

<details><summary>↩ Tool result · `toolu_01NcUR8WAdYaiQWQERntCTdz`</summary>

```text
# Performance Results Extraction

## Table 1: ALFWorld Results (Qwen2.5-7B Backbone)

**Table Caption:** "Evaluation of task success rates (%) across ALFWorld, ScienceWorld, and WebShop benchmarks."

**ITP_R (ITPR) Performance with Qwen2.5-7B:**
- PICK: 94.29%
- CLEAN: 88.89%
- HEAT: 87.50%
- COOL: 53.84%
- LOOK: 76.00%
- PICK2: 91.67%
- **Overall: 85.07%**

## Table 1: ScienceWorld Results (Qwen2.5-7B Backbone)

**Same table provides ScienceWorld metrics:**

**ITP_R Performance with Qwen2.5-7B:**
- Seen: 62.58%
- Unseen: 58.94%
- **Total: 60.20%**

Both results appear in **Table 1** of the main paper under the "Training" section comparing multiple baseline methods across three backbone models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d30c619e-476b-4719-a1bd-be74938d22f7",
  "isSidechain": true,
  "promptId": "540c002c-9999-471e-b32d-70c2ebec2c01",
  "agentId": "aeb9052a04aec7401",
  "type": "user",
  "uuid": "5aaec82f-d170-4650-846c-4e146dce2e19",
  "sourceToolAssistantUUID": "d30c619e-476b-4719-a1bd-be74938d22f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-12T00:50:41.588Z_

The HTML version of the paper gave me the exact numbers from Table 1. Let me now cross-verify by fetching additional sources to confirm these numbers are accurate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5aaec82f-d170-4650-846c-4e146dce2e19",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011Cawkt2b9aSuPWJEAUhKvi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a55465f9-521a-4af4-9b89-d3bf46674f4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHXVTjzk5BqWZeq5Uiej4t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 10991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 14 · 2026-05-12T00:50:45.615Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RNUfuWhm7kUBRVcKBYFZfJ`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.08955v1",
  "prompt": "Find and extract the COMPLETE Table 1 from this paper. I need every row and column. Specifically I need: 1) All ALFWorld subtask columns (PICK, CLEAN, HEAT, COOL, LOOK, PICK2) and the Overall column for ITP-R with Qwen2.5-7B. 2) ScienceWorld results for ITP-R with Qwen2.5-7B. 3) Also extract the results for ITP (training-free variant) with Qwen2.5-7B for comparison. Report the exact table caption and all numbers precisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a55465f9-521a-4af4-9b89-d3bf46674f4a",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011Cawkt2b9aSuPWJEAUhKvi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8b1c1d0-bab6-4fad-8ba1-d7105b696f29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHXVTjzk5BqWZeq5Uiej4t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 10991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 15 · 2026-05-12T00:50:47.525Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LySyuWcK7MD1pKhAJnNyA3`</summary>

```json
{
  "url": "https://huggingface.co/papers/2601.08955",
  "prompt": "Extract any performance numbers, results tables, or discussion of ITP-R results on ALFWorld or ScienceWorld from this page. Specifically looking for success rates with Qwen2.5-7B backbone."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8b1c1d0-bab6-4fad-8ba1-d7105b696f29",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011Cawkt2b9aSuPWJEAUhKvi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "498eeed0-22b5-4c83-8449-31598ac67534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHXVTjzk5BqWZeq5Uiej4t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 10991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 16 · 2026-05-12T00:50:48.159Z_

<details><summary>↩ Tool result · `toolu_01LySyuWcK7MD1pKhAJnNyA3`</summary>

```text
&lt;persisted-output>
Output too large (78KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-/be982e2d-eefc-43fb-9f0c-35005d8376ef/tool-results/toolu_01LySyuWcK7MD1pKhAJnNyA3.txt

Preview (first 2KB):
Title: Agent Learning from Adaptive Lookahead with World Models

URL Source: https://arxiv.org/html/2601.08955

Published Time: Thu, 15 Jan 2026 01:04:11 GMT

Markdown Content:
Youwei Liu 2,1, Jian Wang 1†, Hanlin Wang 1, Beichen Guo 1, Wenjie Li 1

1 The Hong Kong Polytechnic University 

2 Central South University 

loyiv5477@gmail.com  jian51.wang@polyu.edu.hk

{hanlin-henry.wang,beichen.guo}@connect.polyu.hk 

 cswjli@comp.polyu.edu.hk This work was conducted while Youwei Liu was a remote research assistant at the Hong Kong Polytechnic University.

###### Abstract

Recent advances in world models have shown promise for modeling future dynamics of environmental states, enabling agents to reason and act without accessing real environments. Current methods mainly perform single-step or fixed-horizon rollouts, leaving their potential for complex task planning under-exploited. We propose Imagine-then-Plan (ITP), a unified framework for agent learning via lookahead imagination, where an agent’s policy model interacts with the learned world model, yielding multi-step “imagined” trajectories. Since the imagination horizon may vary by tasks and stages, we introduce a novel adaptive lookahead mechanism by trading off the ultimate goal and task progress. The resulting imagined trajectories provide rich signals about future consequences, such as achieved progress and potential conflicts, which are fused with current observations, formulating a partially observable and imaginable Markov decision process to guide policy learning. We instantiate ITP with both training-free and reinforcement-trained variants. Extensive experiments across representative agent benchmarks demonstrate that ITP significantly outperforms competitive baselines. Further analyses validate that our adaptive lookahead largely enhances agents’ reasoning capability, providing valuable insights into addressing broader, complex tasks. Our code and data will be released.

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "498eeed0-22b5-4c83-8449-31598ac67534",
  "isSidechain": true,
  "promptId": "540c002c-9999-471e-b32d-70c2ebec2c01",
  "agentId": "aeb9052a04aec7401",
  "type": "user",
  "uuid": "a230b06f-a21a-44e2-80b0-06791cf458b3",
  "sourceToolAssistantUUID": "498eeed0-22b5-4c83-8449-31598ac67534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-12T00:50:48.386Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MrEAfykhhxTSPBnR3yWUEL`</summary>

```json
{
  "url": "https://github.com/loyiv/ITP",
  "prompt": "Extract any performance numbers, results tables, or benchmarks mentioned in the README. Specifically looking for ITP-R results on ALFWorld (overall and per-subtask) and ScienceWorld with Qwen2.5-7B backbone."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a230b06f-a21a-44e2-80b0-06791cf458b3",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011Cawkt2b9aSuPWJEAUhKvi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "abbc1ec0-0fca-49da-9d42-3386e2714c63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHXVTjzk5BqWZeq5Uiej4t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 10991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 18 · 2026-05-12T00:50:49.764Z_

<details><summary>↩ Tool result · `toolu_01RNUfuWhm7kUBRVcKBYFZfJ`</summary>

```text
# Table 1 Extraction: ITP Results with Qwen2.5-7B

**Table Caption:** "Evaluation of task success rates (%) across ALFWorld and ScienceWorld benchmarks."

## Qwen2.5-7B Results

### ITP_I (Training-Free Variant)
| Task | PICK | CLEAN | HEAT | COOL | LOOK | PICK2 | Overall |
|------|------|-------|------|------|------|-------|---------|
| Success Rate | 65.71 | 25.93 | 25.00 | 24.00 | 30.77 | 25.00 | 35.71 |

**ScienceWorld (ITP_I):** Seen: 16.49% | Unseen: 17.88%

### ITP_R (Reinforcement-Trained Variant)
| Task | PICK | CLEAN | HEAT | COOL | LOOK | PICK2 | Overall |
|------|------|-------|------|------|------|-------|---------|
| Success Rate | 94.29 | 88.89 | 87.50 | 53.84 | 76.00 | 91.67 | 85.07 |

**ScienceWorld (ITP_R):** Seen: 62.58% | Unseen: 58.94%

The table demonstrates substantial performance improvements with reinforcement training, achieving notably higher success rates across both benchmarks compared to the training-free approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8b1c1d0-bab6-4fad-8ba1-d7105b696f29",
  "isSidechain": true,
  "promptId": "540c002c-9999-471e-b32d-70c2ebec2c01",
  "agentId": "aeb9052a04aec7401",
  "type": "user",
  "uuid": "2068e0f3-8e1c-408a-bc57-545ed889c567",
  "sourceToolAssistantUUID": "e8b1c1d0-bab6-4fad-8ba1-d7105b696f29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T00:50:53.449Z_

<details><summary>↩ Tool result · `toolu_01MrEAfykhhxTSPBnR3yWUEL`</summary>

```text
# Performance Results from ITP GitHub Repository

Based on my review of the provided README content, **no specific numerical performance results are included**. 

The README contains a reference to a results table:

> "[![](/loyiv/ITP/raw/main/figures/main_table.png)](/loyiv/ITP/blob/main/figures/main_table.png)"

However, this is only an image placeholder without accompanying numerical data in the text. The document mentions that experimental results exist but does not display the actual benchmarks, success rates, or performance metrics for:

- ITP-R on ALFWorld (overall or per-subtask breakdowns)
- ITP-R on ScienceWorld with Qwen2.5-7B
- Comparative performance against baselines

To obtain these specific performance numbers, you would need to either view the actual image file referenced in the repository or consult the full paper available on arXiv (2601.08955).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "abbc1ec0-0fca-49da-9d42-3386e2714c63",
  "isSidechain": true,
  "promptId": "540c002c-9999-471e-b32d-70c2ebec2c01",
  "agentId": "aeb9052a04aec7401",
  "type": "user",
  "uuid": "02fa6991-cb44-432b-bf2f-41f9843c3191",
  "sourceToolAssistantUUID": "abbc1ec0-0fca-49da-9d42-3386e2714c63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-12T00:51:08.374Z_

Good. Let me also try to access the full HTML paper content that was saved, and try to fetch the GitHub image of the main table for additional cross-verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02fa6991-cb44-432b-bf2f-41f9843c3191",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011CawkuC2xQhPTG46Wqt7YK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4503ea4e-3071-4a29-a261-35d3a769c880",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uqt13Kh7MpznfCmZGzfEHp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1813,
      "cache_read_input_tokens": 12903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1813,
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

_source line 21 · 2026-05-12T00:51:09.519Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JBKXbQLW8LPs8BZktKgAX3`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-/be982e2d-eefc-43fb-9f0c-35005d8376ef/tool-results/toolu_01LySyuWcK7MD1pKhAJnNyA3.txt",
  "offset": 0,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4503ea4e-3071-4a29-a261-35d3a769c880",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011CawkuC2xQhPTG46Wqt7YK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "212a61a1-d2fe-4ac1-ad19-b18412fc37eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uqt13Kh7MpznfCmZGzfEHp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1813,
      "cache_read_input_tokens": 12903,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1813,
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

_source line 22 · 2026-05-12T00:51:09.849Z_

<details><summary>↩ Tool result · `toolu_01JBKXbQLW8LPs8BZktKgAX3`</summary>

```text
0	Title: Agent Learning from Adaptive Lookahead with World Models
1	
2	URL Source: https://arxiv.org/html/2601.08955
3	
4	Published Time: Thu, 15 Jan 2026 01:04:11 GMT
5	
6	Markdown Content:
7	Youwei Liu 2,1, Jian Wang 1†, Hanlin Wang 1, Beichen Guo 1, Wenjie Li 1
8	
9	1 The Hong Kong Polytechnic University 
10	
11	2 Central South University 
12	
13	loyiv5477@gmail.com  jian51.wang@polyu.edu.hk
14	
15	{hanlin-henry.wang,beichen.guo}@connect.polyu.hk 
16	
17	 cswjli@comp.polyu.edu.hk This work was conducted while Youwei Liu was a remote research assistant at the Hong Kong Polytechnic University.
18	
19	###### Abstract
20	
21	Recent advances in world models have shown promise for modeling future dynamics of environmental states, enabling agents to reason and act without accessing real environments. Current methods mainly perform single-step or fixed-horizon rollouts, leaving their potential for complex task planning under-exploited. We propose Imagine-then-Plan (ITP), a unified framework for agent learning via lookahead imagination, where an agent’s policy model interacts with the learned world model, yielding multi-step “imagined” trajectories. Since the imagination horizon may vary by tasks and stages, we introduce a novel adaptive lookahead mechanism by trading off the ultimate goal and task progress. The resulting imagined trajectories provide rich signals about future consequences, such as achieved progress and potential conflicts, which are fused with current observations, formulating a partially observable and imaginable Markov decision process to guide policy learning. We instantiate ITP with both training-free and reinforcement-trained variants. Extensive experiments across representative agent benchmarks demonstrate that ITP significantly outperforms competitive baselines. Further analyses validate that our adaptive lookahead largely enhances agents’ reasoning capability, providing valuable insights into addressing broader, complex tasks. Our code and data will be released.
22	
23	Imagine-then-Plan: Agent Learning from Adaptive 
24	
25	Lookahead with World Models
26	
27	Youwei Liu 2,1††thanks: This work was conducted while Youwei Liu was a remote research assistant at the Hong Kong Polytechnic University., Jian Wang 1†, Hanlin Wang 1, Beichen Guo 1, Wenjie Li 1 1 The Hong Kong Polytechnic University 2 Central South University loyiv5477@gmail.com  jian51.wang@polyu.edu.hk{hanlin-henry.wang,beichen.guo}@connect.polyu.hk cswjli@comp.polyu.edu.hk
28	
29	1 1 footnotetext: Corresponding author.
30	1 Introduction
31	--------------
32	
33	The emergence of Large Language Models (LLMs) has sparked a paradigm shift in autonomous agents, enabling them to reason and interact across a wide range of digital and physical environments(Li et al., [2023](https://arxiv.org/html/2601.08955v1#bib.bib15 "Camel: communicative agents for\" mind\" exploration of large language model society"); Wang et al., [2024a](https://arxiv.org/html/2601.08955v1#bib.bib16 "Voyager: an open-ended embodied agent with large language models"); Fung et al., [2025](https://arxiv.org/html/2601.08955v1#bib.bib23 "Embodied ai agents: modeling the world")). LLM-based agents primarily leverage immediate observations and historical interaction traces to facilitate decision-making(Yao et al., [2023](https://arxiv.org/html/2601.08955v1#bib.bib9 "ReAct: synergizing reasoning and acting in language models"); Shinn et al., [2023](https://arxiv.org/html/2601.08955v1#bib.bib17 "Reflexion: language agents with verbal reinforcement learning")). Despite the impressive performance achieved, most agents remain constrained by shallow grounding, a state where they perceive the environment but lack a deep, causal understanding of how their current actions will ultimately reshape the environment. Without the ability to project into the future, agents are prone to catastrophic failures, discovering erroneous actions or state conflicts only after they have been irreversibly executed.
34	
35	![Image 1: Refer to caption](https://arxiv.org/html/2601.08955v1/x1.png)
36	
37	Figure 1: Comparison between our ITP framework and conventional agent learning frameworks.
38	
39	To bridge this grounding gap, world models(LeCun, [2022](https://arxiv.org/html/2601.08955v1#bib.bib22 "A path towards autonomous machine intelligence version 0.9. 2, 2022-06-27"); Hafner et al., [2023](https://arxiv.org/html/2601.08955v1#bib.bib19 "Mastering diverse domains through world models")) that focus on future state modeling have emerged as a promising solution, enabling agents to simulate environmental dynamics and “rehearse” actions in a mental sandbox(Wang et al., [2025d](https://arxiv.org/html/2601.08955v1#bib.bib20 "World modeling makes a better planner: dual preference optimization for embodied task planning")). Contemporary methods typically employ world models for single-step verification or with fixed-horizon rollouts Hao et al. ([2023](https://arxiv.org/html/2601.08955v1#bib.bib21 "Reasoning with language model is planning with world model")); Qiao et al. ([2024](https://arxiv.org/html/2601.08955v1#bib.bib26 "Agent planning with world knowledge model")); Zhang et al. ([2025](https://arxiv.org/html/2601.08955v1#bib.bib25 "Agent learning via early experience")). Such rigid strategies are often suboptimal, as they fail to capture long-term dependencies in complex tasks (e.g., household embodied tasks). Furthermore, they are prone to suffer from high computational costs with unnecessary deep rollouts for trivial actions. A truly intelligent agent should be deliberative, allocating deep foresight adaptively to resolve potential state conflicts and account for long-term dependencies in pivotal, high-stakes decisions.
40	
41	In this paper, we propose Imagine-then-Plan (ITP), a framework that empowers agents to perform task planning with world model-based foresight. The core of ITP is to move beyond passive observation and perform a proactive, deliberative “rehearsal” phase, where decisions are conditioned on both present observations and potential futures. This requires the agent to internally imagine multi-step future trajectories by looking ahead. Unlike previous rigid approaches, ITP introduces an adaptive lookahead mechanism that dynamically scales the imagination horizon by trading off the ultimate goal and estimated task progress. More importantly, this shift necessitates a new conceptualization of the agent’s decision-making process. We move beyond the Partially Observable Markov Decision Process (POMDP)(Åström, [1965](https://arxiv.org/html/2601.08955v1#bib.bib33 "Optimal control of markov processes with incomplete state information i"); Song et al., [2024](https://arxiv.org/html/2601.08955v1#bib.bib12 "Trial and error: exploration-based trajectory optimization of LLM agents"); Wang et al., [2025b](https://arxiv.org/html/2601.08955v1#bib.bib10 "STeCa: step-level trajectory calibration for LLM agent learning")) toward a Partially Observable and Imaginable MDP (POIMDP). As illustrated in Figure[1](https://arxiv.org/html/2601.08955v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), the agent’s action policy is optimized over a dual-stream representation: the concrete present (observable) and the foresighted future (imaginable). These imagined trajectories provide rich signals, such as anticipating goal progress or detecting potential bottlenecks, allowing the agent to close the loop between planning action sequences and estimating their possible consequences. This implicit feedback enables the agent to perform self-correction when necessary, significantly reducing the need for expensive interactions with the real environment.
42	
43	We instantiate ITP in two variants: a training-free (ITP I\texttt{ITP}_{\text{I}}) variant that uses reflection as the adaptive lookahead for plug-and-play enhancement of LLM agents, and a reinforcement-trained (ITP R\texttt{ITP}_{\text{R}}) variant that leverages imagined futures to optimize the agent policy more effectively and more efficiently. Extensive experiments demonstrate that both variants significantly improve task success rates. Further analyses validate the vital role of our adaptive lookahead mechanism.
44	
45	Our contributions are summarized as follows: 1) We conceptualize the partially observable and imaginable Markov decision process (POIMDP), laying a solid foundation for integrating imagined futures and historical interactions into agent decision-making. 2) We propose Imagine-then-Plan (ITP), a framework that incorporates world model-based imagination with an adaptive lookahead mechanism, which provides deliberative guidance for action policy planning. 3) We demonstrate through training-free and reinforcement-trained variants that ITP significantly improves the success rates of LLM-based agents, providing valuable insights into addressing complex, long-horizon tasks.
46	
47	2 Preliminaries
48	---------------
49	
50	##### Problem Formulation.
51	
52	The reasoning process of LLM agents is often formulated as a Partially Observable Markov Decision Process (POMDP), defined by (𝒮,𝒜,𝒪,𝒯,ℛ)(\mathcal{S},\mathcal{A},\mathcal{O},\mathcal{T},\mathcal{R}). Here, 𝒮\mathcal{S} denotes the environment state space, 𝒜\mathcal{A} the action space, and 𝒪\mathcal{O} the observation space. 𝒯:𝒮×𝒜→𝒮\mathcal{T}:\mathcal{S}\times\mathcal{A}\rightarrow\mathcal{S} represents the state transition function, and ℛ:𝒮×𝒜→[0,1]\mathcal{R}:\mathcal{S}\times\mathcal{A}\rightarrow[0,1] denotes the reward function that evaluates task performance. At each time step t t, the agent receives an observation o t∈𝒪 o_{t}\in\mathcal{O} and selects an action a t∼π θ(⋅|h t)a_{t}\sim\pi_{\theta}(\cdot|h_{t}), where h t=(o 1,a 1,…,o t)h_{t}=(o_{1},a_{1},\dots,o_{t}) denotes the interaction history. Executing a t a_{t} induces a transition to a new latent state s t+1∼𝒯​(s t,a t)s_{t+1}\sim\mathcal{T}(s_{t},a_{t}), from which the environment emits the next observation o t+1 o_{t+1}. The interaction terminates when the agent reaches a terminal state or exceeds a predefined maximum number of steps.
53	
54	##### LLMs as World Models.
55	
56	A world model is a predictive model of environment dynamics that estimates future states conditioned on actions LeCun ([2022](https://arxiv.org/html/2601.08955v1#bib.bib22 "A path towards autonomous machine intelligence version 0.9. 2, 2022-06-27")). In text-based environments, the environment state is typically represented as text and observable to the agent. We treat textual observations as state representations, denoted as s t s_{t} at time step t t. Under this formulation, LLMs can be interpreted as world models, as they capture transition regularities by predicting the next state given the current interaction context Zhang et al. ([2025](https://arxiv.org/html/2601.08955v1#bib.bib25 "Agent learning via early experience")); Li et al. ([2025](https://arxiv.org/html/2601.08955v1#bib.bib37 "From word to world: can large language models be implicit text-based world models?")). Concretely, a textual world model parameterized by an autoregressive LLM defines the conditional distribution p ϕ​(s t+1|s t,a t)p_{\phi}(s_{t+1}|s_{t},a_{t}). The distribution is factorized at the token level, and the model generates the next state sequentially. Such world models serve as powerful proxies for environment dynamics and enable planning in language-based agents.
57	
58	![Image 2: Refer to caption](https://arxiv.org/html/2601.08955v1/x2.png)
59	
60	Figure 2: Overview of the proposed Imageine-then-Plan (ITP) framework. It consists of two variants: (a) ITP I\texttt{ITP}_{\text{I}}, which is training-free and enables LLM agents to learn from the imagination at inference time. (b) ITP R\texttt{ITP}_{\text{R}}, which leverages imagined futures to optimize the action policy more effectively and more efficiently. 
61	
62	3 Method
63	--------
64	
65	We propose I magine-t hen-P lan (ITP), a framework that equips LLM-based agents with adaptive lookahead via learned world models. As illustrated in Figure[2](https://arxiv.org/html/2601.08955v1#S2.F2 "Figure 2 ‣ LLMs as World Models. ‣ 2 Preliminaries ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), ITP enables agents to condition decisions on both the observable present and imagined future trajectories.
66	
67	### 3.1 World Model Training
68	
69	As shown in Figure[2](https://arxiv.org/html/2601.08955v1#S2.F2 "Figure 2 ‣ LLMs as World Models. ‣ 2 Preliminaries ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), we first fine-tune a base LLM on expert demonstrations 𝒟 exp\mathcal{D}_{\mathrm{exp}} to obtain an initial agent policy π θ 0\pi_{\theta_{0}}. This warm-up establishes basic capability to produce executable actions, serving as the foundation for the agent’s exploration. We ask the agent to perform rollouts in the environment, obtaining the rollout trajectories 𝒟 roll\mathcal{D}_{\mathrm{roll}}. As introduced in §[2](https://arxiv.org/html/2601.08955v1#S2 "2 Preliminaries ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), we learn a LLM-based world model ℳ ϕ\mathcal{M}_{\phi} that approximates the environment dynamics p ϕ(s|′s,a)p_{\phi}(s{{}^{\prime}}|s,a), where s s and a a denote the current state and action, respectively. s′s{{}^{\prime}} represents the next-step state. To ensure the world model is grounded and robust to out-of-distribution actions, we train it on a joint dataset 𝒟 WM=𝒟 exp∪𝒟 roll\mathcal{D_{\mathrm{WM}}}=\mathcal{D}_{\mathrm{exp}}\cup\mathcal{D}_{\mathrm{roll}}. The world model ℳ ϕ\mathcal{M}_{\phi} is optimized by minimizing the negative log-likelihood as follows:
70	
71	ℒ WM(ϕ)=−𝔼(s,′s,a)∼𝒟 WM[log p ϕ(s|′s,a)].\mathcal{L}_{\text{WM}}(\phi)=-\mathbb{E}_{(s{{}^{\prime}},s,a)\sim\mathcal{D_{\mathrm{WM}}}}\bigl[\log p_{\phi}(s{{}^{\prime}}|s,a)\bigr].(1)
72	
73	### 3.2 Lookahead Imagination and POIMDP
74	
75	To integrate world-model foresight into decision making, we extend the standard POMDP (as introduced in §[2](https://arxiv.org/html/2601.08955v1#S2 "2 Preliminaries ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models")) to a P artially O bservable and I maginable M arkov D ecision P rocess (POIMDP). Under this formulation, the agent is endowed with a lookahead imagination operator induced by the learned world model.
76	
77	Formally, given the current observed state s t s_{t} and a lookahead horizon K t∈{0,1,…,K max}K_{t}\in\{0,1,\dots,K_{\max}\} at each time step t t, the agent policy π θ\pi_{\theta} and the world model ℳ ϕ\mathcal{M}_{\phi} interact for K t K_{t} steps within a “mental sandbox”. This imagination process is given by:
78	
79	→π θ a^t→ℳ ϕ s^t+1→π θ…→π θ a^t+K t−1→ℳ ϕ s^t+K t.\xrightarrow{\pi_{\theta}}\hat{a}_{t}\xrightarrow{\mathcal{M}_{\phi}}\hat{s}_{t+1}\xrightarrow{\pi_{\theta}}\dots\xrightarrow{\pi_{\theta}}\hat{a}_{t+K_{t}-1}\xrightarrow{\mathcal{M}_{\phi}}\hat{s}_{t+K_{t}}.(2)
80	
81	This yields an imagined future trajectory τ^t(K t)={(a^t+i,s^t+i+1)}i=0 K t−1\hat{\tau}^{(K_{t})}_{t}=\{(\hat{a}_{t+i},\hat{s}_{t+i+1})\}_{i=0}^{K_{t}-1}, where a^t+i∼π θ(⋅|s t,τ^t(i))\hat{a}_{t+i}\sim\pi_{\theta}(\cdot|s_{t},\hat{\tau}_{t}^{(i)}) and s^t+i+1∼ℳ ϕ(⋅|s^t+i,a^t+i)\hat{s}_{t+i+1}\sim\mathcal{M}_{\phi}(\cdot|\hat{s}_{t+i},\hat{a}_{t+i}). The objective of the agent policy is to yield an appropriate action a t a_{t} conditioned on both the observable state s t s_{t} and the imagined future τ^t(K t)\hat{\tau}^{(K_{t})}_{t}. As such, our POIMDP formulates the policy decision as follows:
82	
83	a t∼π θ(⋅∣s t,τ^t(K t)).a_{t}\sim\pi_{\theta}(\cdot\mid s_{t},\hat{\tau}^{(K_{t})}_{t}).(3)
84	
85	This allows the agent to anticipate goal progress or detect potential bottlenecks before generating the next action, enabling the agent to perform self-correction when necessary.
86	
87	### 3.3 Planning with Adaptive Lookahead
88	
89	To achieve effective task planning, a key challenge is determining how far the agent should imagine. Short-horizon imagination may miss long-term dependencies, while excessive rollouts can amplify model errors and incur unnecessary computation. To resolve this, we aim to adaptively select the imagination horizon K t K_{t} based on the estimated task progress against the ultimate goal. We instantiate ITP via two distinct variants to provide both flexibility and optimization: (i) ITP I\texttt{ITP}_{\text{I}}, which is an inference-time method that learns from the imagination, and (ii) ITP R\texttt{ITP}_{\text{R}}, which is a reinforcement-trained method that jointly optimizes the lookahead horizon selection and action policy.
90	
91	#### 3.3.1 In-Imagination Learning (ITP I\texttt{ITP}_{\text{I}})
92	
93	ITP I\texttt{ITP}_{\text{I}} is a training-free variant designed for improving LLM agents during inference time. In this mode, both the agent policy and the world model remain frozen, and the agent relies on its inherent capabilities to perform deliberative reasoning. At each step t t, the agent receives the current state s t s_{t} and executes a three-stage “Imagine-then-Plan” procedure: 1) Adaptive horizon selection: The agent first assesses the task instruction and the current state s t s_{t} to determine an appropriate imagination horizon K t∈{0,1,…,K max}K_{t}\in\{0,1,\dots,K_{\max}\}. This allows the agent to allocate deeper foresight to high-stakes decisions while maintaining computational efficiency for trivial actions. 2) World-model imagination: The agent invokes its world model to perform a “mental rehearsal”. By interacting with ℳ ϕ\mathcal{M}_{\phi} for K t K_{t} steps, the agent obtains a multi-step future trajectory τ^t(K t)\hat{\tau}_{t}^{(K_{t})}. 3) Reflective policy generation: Rather than directly taking the first action of the imagined sequence, the agent uses τ^t(K t)\hat{\tau}_{t}^{(K_{t})} as implicit feedback for reflective self-refinement.
94	
95	Specifically, the agent is prompted to self-reflect on the imagined trajectory to evaluate task progress, determine if the predicted states move closer to the ultimate task goal, and detect potential conflicts, bottlenecks, or catastrophic failures before they are irreversibly executed in the real environment. The agent is asked to perform self-refinement and then select the optimal next action a t a_{t}, given by:
96	
97	a t∼π θ(⋅∣s t,Reflect(τ^t(K t))).a_{t}\sim\pi_{\theta}(\cdot\mid s_{t},\text{Reflect}(\hat{\tau}_{t}^{(K_{t})})).(4)
98	
99	By grounding decisions in these imagined futures, ITP I\texttt{ITP}_{\text{I}} transforms passive observation into proactive deliberation, significantly improving task success rates without additional training.
100	
101	#### 3.3.2 Reinforced Training (ITP R\texttt{ITP}_{\text{R}})
102	
103	Compared to ITP I\texttt{ITP}_{\text{I}} that relies on inference-time reasoning, ITP R\texttt{ITP}_{\text{R}} aims to explicitly learn when and how long to imagine. We augment the agent with a lightweight K K-head predictor P θ​(K t|s t)P_{\theta}(K_{t}|s_{t}), which is a linear layer built on top of a backbone LLM that predicts distributions over imagination horizons. The action policy and predictor are optimized jointly with the following three stages.
104	
105	##### Stage 1: Pseudo-Labeling Lookahead Horizon.
106	
107	A key obstacle for learning adaptive lookahead is that expert trajectories provide only (s t,a t∗)(s_{t},a_{t}^{*}) pairs but do not specify the “right” lookahead horizon. We therefore construct pseudo labels using the world model ℳ ϕ\mathcal{M}_{\phi} and the initial agent policy π θ 0\pi_{\theta_{0}}. Specifically, we use teacher-forced expert actions to rollout on the frozen world model ℳ ϕ\mathcal{M}_{\phi} by looking ahead one step and obtain future states, from which we derive lookahead-conditioned trajectories {τ^t(k)}k=0 K max\{\hat{\tau}_{t}^{(k)}\}_{k=0}^{K_{\max}}. We then score each candidate step by the log-likelihood of expert actions under π θ 0\pi_{\theta_{0}}, and select the optimal lookahead step by:
108	
109	K~t=arg⁡max 0≤k≤K max⁡[log⁡p θ 0​(a t∗∣s t,τ^t(k))−λ K​k],\tilde{K}_{t}=\arg\max_{0\leq k\leq K_{\max}}\Big[\log p_{\theta_{0}}(a_{t}^{*}\mid s_{t},\hat{\tau}_{t}^{(k)})-\lambda_{K}\,k\Big],(5)
110	
111	where λ K\lambda_{K} is a hyperparameter controlling the lookahead penalty. Based on the selection criteria in Eq. ([5](https://arxiv.org/html/2601.08955v1#S3.E5 "In Stage 1: Pseudo-Labeling Lookahead Horizon. ‣ 3.3.2 Reinforced Training (\"ITP\"_\"R\") ‣ 3.3 Planning with Adaptive Lookahead ‣ 3 Method ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models")), we obtain a dataset 𝒟 K\mathcal{D}_{K} containing the pseudo-labels of the optimal lookahead step for each action in the expert trajectory.
112	
113	##### Stage 2: Warm-Up Training.
114	
115	Starting from the initial agent policy π θ 0\pi_{\theta_{0}}, we further fine-tune the agent to jointly (i) act under lookahead-conditioned pseudo-trajectories and (ii) predict the required lookahead step. Specifically, given labeled tuples {(s t,a t∗,K~t)}\{(s_{t},a_{t}^{*},\tilde{K}_{t})\}, we condition the agent policy on τ^t(K~t)\hat{\tau}_{t}^{(\tilde{K}_{t})} and train π θ​(a t|s t,τ^t(K~t))\pi_{\theta}(a_{t}|s_{t},\hat{\tau}_{t}^{(\tilde{K}_{t})}) to imitate the expert action a t∗a_{t}^{*}, with a standard negative log-likelihood loss ℒ π​(θ)\mathcal{L}_{\pi}(\theta). Meanwhile, we train the K K-head predictor to estimate the pseudo label K~t\tilde{K}_{t}, with a similar negative log-likelihood loss ℒ K​(θ)\mathcal{L}_{K}(\theta). Our warm-up training is given by:
116	
117	ℒ WT​(θ)=ℒ π​(θ)+η​ℒ K​(θ).\mathcal{L}_{\mathrm{WT}}(\theta)=\mathcal{L}_{\pi}(\theta)+\eta\,\mathcal{L}_{K}(\theta).(6)
118	
119	where η\eta is a weighted coefficient. This yields (i) a competent agent policy that can generate reliable actions and (ii) an adaptive lookahead horizon predictor that approximates lookahead steps, providing a stable initialization for the subsequent online reinforcement optimization.
120	
121	##### Stage 3: Online Optimization.
122	
123	To balance task performance and imagination cost, we further refine the agent policy through online reinforcement learning. At each step t t, the agent samples a lookahead step K t K_{t} from the K K-head predictor, invokes the frozen world model ℳ ϕ\mathcal{M}_{\phi} to generate a K t K_{t}-step imagined trajectory τ^t(K t)\hat{\tau}_{t}^{(K_{t})}, and subsequently samples an action a t∼π θ(⋅∣s t,τ^t(K t))a_{t}\sim\pi_{\theta}(\cdot\mid s_{t},\hat{\tau}_{t}^{(K_{t})}). As illustrated in Figure[2](https://arxiv.org/html/2601.08955v1#S2.F2 "Figure 2 ‣ LLMs as World Models. ‣ 2 Preliminaries ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), we employ a reward function that augments the environment reward r env r_{\mathrm{env}} with explicit penalties for computational and interaction overhead, given by:
124	
125	r t+1=r env−λ K​K t−λ step,r_{t+1}=r_{\mathrm{env}}-\lambda_{K}K_{t}-\lambda_{\mathrm{step}},(7)
126	
127	where λ K\lambda_{K} is the lookahead penalty coefficient, and λ step\lambda_{\text{step}} is a factor discouraging reasoning redundancy.
128	
129	Specifically, we utilize the Advantage Actor-Critic (A2C) algorithm Mnih et al. ([2016](https://arxiv.org/html/2601.08955v1#bib.bib40 "Asynchronous methods for deep reinforcement learning")) to jointly optimize the action policy and the K K-head parameters. The objective is decomposed into three components: (i) an actor term ℒ act​(θ)≜−𝔼​[A t​(log⁡p θ​(K t∣s t)+log⁡π θ​(a t∣s t,τ^t(K t)))]\mathcal{L}_{\mathrm{act}}(\theta)\triangleq-\mathbb{E}\!\left[A_{t}\left(\log p_{\theta}(K_{t}\mid s_{t})+\log\pi_{\theta}(a_{t}\mid s_{t},\hat{\tau}_{t}^{(K_{t})})\right)\right] that jointly updates the lookahead predictor and the agent policy; (ii) a Critic regression term ℒ value​(θ)≜𝔼​[(V θ​(s t)−V^t)2]\mathcal{L}_{\mathrm{value}}(\theta)\triangleq\mathbb{E}\!\left[(V_{\theta}(s_{t})-\hat{V}_{t})^{2}\right] that trains a Value-head to match the TD learning target; and (iii) an entropy regularizer ℒ ent​(θ)≜−𝔼​[ℋ​(p θ​(K t∣s t))]\mathcal{L}_{\mathrm{ent}}(\theta)\triangleq-\;\mathbb{E}\!\left[\mathcal{H}(p_{\theta}(K_{t}\mid s_{t}))\right] that encourages sufficient exploration over the lookahead steps to prevent premature convergence to sub-optimal horizons. The final training objective is:
130	
131	ℒ A2C​(θ)=ℒ act​(θ)+α​ℒ value​(θ)+β​ℒ ent​(θ),\mathcal{L}_{\mathrm{A2C}}(\theta)=\mathcal{L}_{\mathrm{act}}(\theta)+\alpha\mathcal{L}_{\mathrm{value}}(\theta)+\beta\mathcal{L}_{\mathrm{ent}}(\theta),(8)
132	
133	where α\alpha and β\beta are hyperparameters balancing value estimation and exploration. Algorithm[1](https://arxiv.org/html/2601.08955v1#alg1 "Algorithm 1 ‣ Stage 3: Online Optimization. ‣ 3.3.2 Reinforced Training (\"ITP\"_\"R\") ‣ 3.3 Planning with Adaptive Lookahead ‣ 3 Method ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models") shows the overview of ITP R\texttt{ITP}_{\text{R}}’s training process.
134	
135	At inference time, ITP R\texttt{ITP}_{\text{R}} utilizes the learned K K-head to perform adaptive lookahead, following a similar deliberative procedure as ITP I\texttt{ITP}_{\text{I}}.
136	
137	Algorithm 1 ITP R\texttt{ITP}_{\text{R}}: Reinforced Training with Adaptive Lookahead
138	
139	1:Dataset
140	
141	𝒟={(s t,a t∗)}\mathcal{D}=\{(s_{t},a_{t}^{*})\}
142	; Agent policy
143	
144	π θ 0\pi_{\theta_{0}}
145	; World model
146	
147	ℳ ϕ\mathcal{M}_{\phi}
148	; Parameters
149	
150	K max K_{\max}
151	,
152	
153	λ K\lambda_{K}
154	,
155	
156	η\eta
157	,
158	
159	α\alpha
160	,
161	
162	β\beta
163	.
164	
165	2:Agent policy
166	
167	π θ\pi_{\theta}
168	; Lookahead predictor
169	
170	P θ P_{\theta}
171	.
172	
173	3:// Stage 1: Pseudo-Labeling Lookahead Horizon
174	
175	4:for each episode in
176	
177	𝒟\mathcal{D}
178	do
179	
180	5: Cache
181	
182	{τ^t(k)}k=0 K max\{\hat{\tau}_{t}^{(k)}\}_{k=0}^{K_{\max}}
183	via
184	
185	ℳ ϕ\mathcal{M}_{\phi}
186	& teacher-forced
187	
188	a t∗a_{t}^{*}
189	.
190	
191	6:for each step
192	
193	t t
194	do
195	
196	7:
197	
198	S t​(k)≜log⁡p θ 0​(a t∗∣s t,τ^t(k))S_{t}(k)\triangleq\log p_{\theta_{0}}(a_{t}^{*}\mid s_{t},\hat{\tau}_{t}^{(k)})
199	.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "212a61a1-d2fe-4ac1-ad19-b18412fc37eb",
  "isSidechain": true,
  "promptId": "540c002c-9999-471e-b32d-70c2ebec2c01",
  "agentId": "aeb9052a04aec7401",
  "type": "user",
  "uuid": "79eaf940-2cd3-48b4-918c-2e2d5ad2bec4",
  "sourceToolAssistantUUID": "212a61a1-d2fe-4ac1-ad19-b18412fc37eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-12T00:51:11.683Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014Qu5Tu7tgW296xYTWVCsoW`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/loyiv/ITP/main/figures/main_table.png",
  "prompt": "Extract all numbers from this table image. I need every row and column, especially ITP-R with Qwen2.5-7B on ALFWorld (PICK, CLEAN, HEAT, COOL, LOOK, PICK2, Overall) and ScienceWorld."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79eaf940-2cd3-48b4-918c-2e2d5ad2bec4",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011CawkuC2xQhPTG46Wqt7YK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d92b7117-a24b-4d95-9d92-d11dc85dd9ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uqt13Kh7MpznfCmZGzfEHp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1813,
      "cache_read_input_tokens": 12903,
      "output_tokens": 325,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1813
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 325,
          "cache_read_input_tokens": 12903,
          "cache_creation_input_tokens": 1813,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1813,
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

_source line 24 · 2026-05-12T00:51:16.372Z_

<details><summary>↩ Tool result · `toolu_014Qu5Tu7tgW296xYTWVCsoW`</summary>

```text
I appreciate your request, but I'm unable to extract the specific numerical data you're looking for from the provided content. The text appears to be encoded PNG image data in binary/hex format rather than readable table information.

To help you effectively, I would need:

1. **A readable format** - The image data as an actual displayable image or as plain text table content
2. **Clear table structure** - The specific rows and columns you mentioned (ITP-R with Qwen2.5-7B metrics for ALFWorld tasks and ScienceWorld results)

**What I can tell you:** The content you've shared is the raw binary representation of a PNG file, which cannot be parsed as text to extract table values.

**Recommendation:** Please provide either:
- The image file itself (which I could attempt to read)
- A text-based export of the table
- A screenshot converted to readable format

Once you share the data in an accessible format, I'll be happy to extract all the numerical results you need for the ITP-R and Qwen2.5-7B comparisons across those specific benchmarks.

[Binary content (image/png, 240.2KB) also saved to /home/ubuntu/.claude-account-3/projects/-/be982e2d-eefc-43fb-9f0c-35005d8376ef/tool-results/webfetch-1778547072178-7zcdie.png]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d92b7117-a24b-4d95-9d92-d11dc85dd9ab",
  "isSidechain": true,
  "promptId": "540c002c-9999-471e-b32d-70c2ebec2c01",
  "agentId": "aeb9052a04aec7401",
  "type": "user",
  "uuid": "bb6ba7fa-78c5-4903-b604-701dcb1d1403",
  "sourceToolAssistantUUID": "d92b7117-a24b-4d95-9d92-d11dc85dd9ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-12T00:51:19.531Z_

Let me read the table image from GitHub and also continue reading the HTML paper to find the actual results table.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb6ba7fa-78c5-4903-b604-701dcb1d1403",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011Cawkvt4Gzq7yB8fWF1HJJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b40130d8-1664-4c92-93b7-17d0947018a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CGH8JWTcHmTgTm1H6Qiv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9722,
      "cache_read_input_tokens": 14716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9722,
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

_source line 26 · 2026-05-12T00:51:20.485Z_

<details open><summary>🔧 Tool call — Read · `toolu_011ZrU4FsymkgWByVUbX7PaT`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-/be982e2d-eefc-43fb-9f0c-35005d8376ef/tool-results/webfetch-1778547072178-7zcdie.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b40130d8-1664-4c92-93b7-17d0947018a1",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011Cawkvt4Gzq7yB8fWF1HJJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6abaf1ee-8272-412e-a38c-8575893156b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CGH8JWTcHmTgTm1H6Qiv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9722,
      "cache_read_input_tokens": 14716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9722,
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

_source line 27 · 2026-05-12T00:51:20.738Z_

<details><summary>↩ Tool result · `toolu_011ZrU4FsymkgWByVUbX7PaT`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6abaf1ee-8272-412e-a38c-8575893156b3",
  "isSidechain": true,
  "promptId": "540c002c-9999-471e-b32d-70c2ebec2c01",
  "agentId": "aeb9052a04aec7401",
  "type": "user",
  "uuid": "287ea97a-9bd8-40ac-ad94-93a7c35d98ec",
  "sourceToolAssistantUUID": "6abaf1ee-8272-412e-a38c-8575893156b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-12T00:51:22.446Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TYyZARGUeKWGrZTAHsZoux`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-/be982e2d-eefc-43fb-9f0c-35005d8376ef/tool-results/toolu_01LySyuWcK7MD1pKhAJnNyA3.txt",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "287ea97a-9bd8-40ac-ad94-93a7c35d98ec",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011Cawkvt4Gzq7yB8fWF1HJJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6c5e46d-63f9-4d32-9d62-09230fd808b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CGH8JWTcHmTgTm1H6Qiv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9722,
      "cache_read_input_tokens": 14716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9722,
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

_source line 29 · 2026-05-12T00:51:22.724Z_

<details><summary>↩ Tool result · `toolu_01TYyZARGUeKWGrZTAHsZoux`</summary>

```text
200	.
201	
202	8:
203	
204	K~t←arg⁡max⁡[S t​(k)−λ K​k]\tilde{K}_{t}\leftarrow\arg\max\big[S_{t}(k)-\lambda_{K}k\big]
205	.
206	
207	9: Store
208	
209	(s t,a t∗,K~t)(s_{t},a_{t}^{*},\tilde{K}_{t})
210	in
211	
212	𝒟 K\mathcal{D}_{K}
213	.
214	
215	10:end for
216	
217	11:end for
218	
219	12:// Stage 2: Warm-Up Training with Lookahead
220	
221	13:for each episode in
222	
223	𝒟 K\mathcal{D}_{K}
224	do
225	
226	14: Sample
227	
228	(s t,a t∗,K~t)∼𝒟 K(s_{t},a_{t}^{*},\tilde{K}_{t})\!\sim\!\mathcal{D}_{K}
229	.
230	
231	15: Update
232	
233	θ\theta
234	via Eq.([6](https://arxiv.org/html/2601.08955v1#S3.E6 "In Stage 2: Warm-Up Training. ‣ 3.3.2 Reinforced Training (\"ITP\"_\"R\") ‣ 3.3 Planning with Adaptive Lookahead ‣ 3 Method ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models")).
235	
236	16:end for
237	
238	17:// Stage 3: Online Actor–Critic Optimization
239	
240	18:for each episode in
241	
242	𝒟\mathcal{D}
243	do
244	
245	19: Sample
246	
247	K t∼P θ​(K∣s t)K_{t}\!\sim\!P_{\theta}(K\!\mid\!s_{t})
248	, query
249	
250	ℳ ϕ\mathcal{M}_{\phi}
251	for
252	
253	τ^t(K t)\hat{\tau}_{t}^{(K_{t})}
254	.
255	
256	20: Update
257	
258	θ\theta
259	via Eq.([8](https://arxiv.org/html/2601.08955v1#S3.E8 "In Stage 3: Online Optimization. ‣ 3.3.2 Reinforced Training (\"ITP\"_\"R\") ‣ 3.3 Planning with Adaptive Lookahead ‣ 3 Method ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models")).
260	
261	21:end for
262	
263	22:return
264	
265	π θ\pi_{\theta}
266	and
267	
268	P θ P_{\theta}
269	.
270	
271	4 Experiments
272	-------------
273	
274	### 4.1 Experimental Settings
275	
276	##### Benchmarks.
277	
278	We evaluate ITP on two representative agent benchmarks: ALFWorld(Shridhar et al., [2020](https://arxiv.org/html/2601.08955v1#bib.bib3 "ALFRED: A benchmark for interpreting grounded instructions for everyday tasks")) for embodied household tasks and ScienceWorld(Wang et al., [2022](https://arxiv.org/html/2601.08955v1#bib.bib4 "ScienceWorld: is your agent smarter than a 5th grader?")) for simulated science experiments. All tasks in these two environments can be formally described as POMDPs. Please refer to Appendix[A](https://arxiv.org/html/2601.08955v1#A1 "Appendix A Datasets and Preprocessing ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models") for more details of the two environments.
279	
280	##### Backbone Models.
281	
282	To ensure a fair comparison, all methods are instantiated using the same suite of backbone models: Qwen2.5-7B(Yang et al., [2024](https://arxiv.org/html/2601.08955v1#bib.bib6 "Qwen2.5 technical report")), Qwen3-8B(Yang et al., [2025](https://arxiv.org/html/2601.08955v1#bib.bib5 "Qwen3 technical report")), and Llama-3-8B-Instruct Dubey et al. ([2024](https://arxiv.org/html/2601.08955v1#bib.bib8 "The llama 3 herd of models")). For our main experiments, we employ Qwen3-8B as the backbone for training the world model. We further evaluate other backbone series as world models in §[4.4](https://arxiv.org/html/2601.08955v1#S4.SS4 "4.4 Impact of World Models ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). All models are prompted using their official chat templates to eliminate performance variances caused by formatting inconsistencies.
283	
284	Backbone Type Method ALFWorld ScienceWorld
285	PICK CLEAN HEAT COOL LOOK PICK2 Overall Seen Unseen
286	Qwen2.5-7B Prompting CoT 17.14 18.52 18.75 16.00 15.38 0.00 14.29 3.09 4.63
287	ReAct 20.00 22.22 18.75 20.00 23.08 0.00 17.14 8.24 9.93
288	RAP 40.00 33.33 6.25 32.00 15.38 20.83 27.86 10.30 16.55
289	\cellcolor gray!15 ITP I\texttt{ITP}_{\text{I}} (Ours)\cellcolor gray!15 65.71\cellcolor gray!15 25.93\cellcolor gray!15 25.00\cellcolor gray!15 24.00\cellcolor gray!15 30.77\cellcolor gray!15 25.00\cellcolor gray!15 35.71\cellcolor gray!15 16.49\cellcolor gray!15 17.88
290	Training SFT 85.71 66.67 56.25 68.00 38.46 66.67 67.86 55.67 49.00
291	WKM 77.14 77.78 75.00 76.00 76.92 75.00 76.43 54.12 56.29
292	IWM 90.60 85.20 88.20 84.20 42.90 76.90 82.80 60.82 57.61
293	\cellcolor blue!10 ITP R\texttt{ITP}_{\text{R}} (Ours)\cellcolor blue!10 94.29\cellcolor blue!10 88.89\cellcolor blue!10 87.50\cellcolor blue!1053.84\cellcolor blue!10 76.00\cellcolor blue!10 91.67\cellcolor blue!10 85.07\cellcolor blue!10 62.58\cellcolor blue!10 58.94
294	Qwen3-8B Prompting CoT 14.29 14.81 12.50 12.00 15.38 12.50 13.57 2.44 1.99
295	ReAct 25.71 22.22 12.50 12.00 7.69 25.00 19.29 9.79 8.61
296	RAP 42.86 37.04 37.50 16.00 15.38 4.17 28.57 15.46 27.14
297	\cellcolor gray!15 ITP I\texttt{ITP}_{\text{I}} (Ours)\cellcolor gray!15 82.86\cellcolor gray!15 25.93\cellcolor gray!15 12.50\cellcolor gray!15 16.00\cellcolor gray!15 23.08\cellcolor gray!15 54.17\cellcolor gray!15 41.43\cellcolor gray!15 20.61\cellcolor gray!15 19.86
298	Training SFT 71.43 70.37 68.75 72.00 69.23 70.83 70.71 56.70 49.67
299	WKM 80.00 77.78 81.25 80.00 76.92 79.17 79.29 60.31 47.68
300	IWM 85.71 85.19 87.50 84.00 46.15 87.50 82.14 59.27 54.30
301	\cellcolor blue!10 ITP R\texttt{ITP}_{\text{R}} (Ours)\cellcolor blue!10 97.14\cellcolor blue!10 88.88\cellcolor blue!10 93.75\cellcolor blue!10 88.00\cellcolor blue!10 76.92\cellcolor blue!10 79.17\cellcolor blue!10 88.57\cellcolor blue!10 61.85\cellcolor blue!10 56.95
302	Llama3.1-8B Prompting CoT 17.14 14.81 18.75 16.00 15.38 8.33 15.00 3.09 3.31
303	ReAct 22.86 22.22 6.25 24.00 23.08 25.00 21.43 9.27 13.24
304	RAP 25.71 25.93 6.25 32.00 7.69 25.00 22.86 11.34 17.21
305	\cellcolor gray!15 ITP I\texttt{ITP}_{\text{I}} (Ours)\cellcolor gray!15 57.14\cellcolor gray!15 37.04\cellcolor gray!15 31.25\cellcolor gray!15 28.00\cellcolor gray!15 23.08\cellcolor gray!15 33.33\cellcolor gray!15 37.86\cellcolor gray!15 19.58\cellcolor gray!15 19.20
306	Training SFT 85.71 85.20 82.40 89.50 85.70 53.80 79.28 57.21 50.33
307	WKM 85.71 85.19 75.00 80.00 38.46 79.17 77.86 61.34 54.96
308	IWM 87.50 88.90 82.40 94.70 85.90 84.60 85.90 57.56 56.29
309	\cellcolor blue!10 ITP R\texttt{ITP}_{\text{R}} (Ours)\cellcolor blue!10 88.57\cellcolor blue!10 92.59\cellcolor blue!10 93.75\cellcolor blue!10 92.00\cellcolor blue!1046.15\cellcolor blue!10 91.67\cellcolor blue!10 87.14\cellcolor blue!10 63.91\cellcolor blue!10 57.61
310	
311	Table 1: Evaluation of task success rates (%) across ALFWorld and ScienceWorld benchmarks. Bold and underlined values represent the best and second-best performance within each backbone model group, respectively.
312	
313	##### Baseline Methods.
314	
315	We compare ITP against two categories of baselines. (1) Prompting-based methods: CoT(Wei et al., [2022](https://arxiv.org/html/2601.08955v1#bib.bib2 "Chain-of-thought prompting elicits reasoning in large language models")) elicits reasoning capabilities by prompting the agent with step-by-step rationales. ReAct(Yao et al., [2023](https://arxiv.org/html/2601.08955v1#bib.bib9 "ReAct: synergizing reasoning and acting in language models")) interleaves reasoning and action to solve interactive tasks. RAP(Hao et al., [2023](https://arxiv.org/html/2601.08955v1#bib.bib21 "Reasoning with language model is planning with world model")) leverages the LLM as both a world model and a policy model, employing Monte Carlo Tree Search to perform planning. (2) Training-based methods: SFT(Chen et al., [2023](https://arxiv.org/html/2601.08955v1#bib.bib41 "Fireact: toward language agent fine-tuning")) conducts behavioral cloning on expert trajectories. WKM(Qiao et al., [2024](https://arxiv.org/html/2601.08955v1#bib.bib26 "Agent planning with world knowledge model")) trains a parametric world knowledge model that provides global task priors and local dynamic state knowledge to guide planning. IWM Zhang et al. ([2025](https://arxiv.org/html/2601.08955v1#bib.bib25 "Agent learning via early experience")) augments imitation learning with an implicit world-modeling objective to encourage the policy to internalize environment dynamics.
316	
317	##### Evaluation Metrics.
318	
319	We adopt success rate (SR) as the evaluation metric, defined as the percentage of episodes that successfully achieve the task goal(Feng et al., [2025](https://arxiv.org/html/2601.08955v1#bib.bib38 "Group-in-group policy optimization for llm agent training"); Wang et al., [2025a](https://arxiv.org/html/2601.08955v1#bib.bib39 "SPA-rl: reinforcing llm agents via stepwise progress attribution")). For ALFWorld, we report SR on each task, including Pick & Place (PICK), Examine in Light (LOOK), Clean & Place (CLEAN), Heat & Place (HEAT), Cool & Place (COOL), and Pick Two & Place (PICK2), as well as the overall SR. For ScienceWorld, we report SR on both the seen and unseen test splits.
320	
321	##### Implementation Details.
322	
323	To ensure a rigorous and fair comparison, we maintain a consistent training protocol across ITP and all baseline methods. We train distinct world models tailored to the two benchmarks. The maximum lookahead horizon is configured based on the typical complexity and average horizon of each environment, with K max=5 K_{\max}=5 for ALFWorld and K max=8 K_{\max}=8 for ScienceWorld. During inference, we employ a decoding temperature of 0.7 to balance generation diversity and stability. For hyperparameter settings and training procedures, please refer to Appendix[B](https://arxiv.org/html/2601.08955v1#A2 "Appendix B Additional Implementation Details ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models").
324	
325	![Image 3: Refer to caption](https://arxiv.org/html/2601.08955v1/x3.png)
326	
327	Figure 3: Ablation results of ITP R\texttt{ITP}_{\text{R}} on ALFWorld and ScienceWorld benchmarks.
328	
329	### 4.2 Main Results
330	
331	##### How does ITP perform across different benchmarks and backbone models?
332	
333	Table[1](https://arxiv.org/html/2601.08955v1#S4.T1 "Table 1 ‣ Backbone Models. ‣ 4.1 Experimental Settings ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models") demonstrates that ITP achieves consistent and significant improvements across all tested backbone models on both ALFWorld and ScienceWorld benchmarks. Specifically, without any additional training, ITP I\texttt{ITP}_{\text{I}} substantially enhances zero-shot planning performance compared to strong prompting baselines like ReAct and RAP. For instance, on the Qwen2.5-7B backbone, ITP I\texttt{ITP}_{\text{I}} achieves an overall success rate of 35.71%, nearly doubling the performance of ReAct (17.14%). Furthermore, our trained model ITP R\texttt{ITP}_{\text{R}} consistently outperforms all training-based baselines, reaching the highest success rates in every backbone group (e.g., 88.57% with Qwen3-8B on ALFWorld and 63.91% with Llama3.1-8B on ScienceWorld). These results underscore that ITP provides a robust advantage that scales effectively across different model architectures.
334	
335	##### Do ITP ’s performance gains stem from lookahead with world models?
336	
337	The effectiveness of our approach is twofold. First, ITP I\texttt{ITP}_{\text{I}} utilizes the same backbone LLM as the prompting baselines, meaning its performance gains stem solely from conditioning actions on world-model rollouts at inference time. This isolates the intrinsic value of explicit lookahead. Second, ITP R\texttt{ITP}_{\text{R}} significantly surpasses training-based alternatives such as IWM and WKM. Unlike IWM, which internalizes dynamics implicitly, or WKM, which relies on static task priors, ITP R\texttt{ITP}_{\text{R}} learns an adaptive lookahead to determine when to invoke the world model. The fact that ITP R\texttt{ITP}_{\text{R}} achieves the best results (e.g., 63.91% on ScienceWorld test-seen with Llama3.1-8B) suggests that combining policy learning with selective, adaptive lookahead provides complementary benefits that static or implicit methods lack. Moreover, as detailed in our ablation study, the reinforcement optimization of the lookahead horizon is also crucial to this final performance leap.
338	
339	##### Ablation Study.
340	
341	To identify the contribution of the reinforced training variant ITP R\texttt{ITP}_{\text{R}}, we ablate ITP R\texttt{ITP}_{\text{R}} by removing the online reinforcement optimization (w/o RT). In this setting, the model relies solely on initial warm-up training without the adaptive refinement of when to invoke the world model. We use Qwen-3-8B as the backbone for both the agent policy and the world model, evaluating performance across ALFWorld and ScienceWorld benchmarks. As shown in Figure[3](https://arxiv.org/html/2601.08955v1#S4.F3 "Figure 3 ‣ Implementation Details. ‣ 4.1 Experimental Settings ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), removing RT consistently and significantly degrades performance: The success rate on ALFWorld drops from 88.57% to 71.42%, while the performance on ScienceWorld decreases from 59.70% to 46.00%. These results confirm that the online reinforcement stage in ITP R\texttt{ITP}_{\text{R}} is a critical contributor rather than an incidental training detail. The substantial performance gap suggests that while supervised learning provides a baseline capability, the reinforced optimization is essential for the agent to master the strategic timing of “imagination,” allowing it to efficiently leverage the world model only when necessary to solve complex tasks.
342	
343	![Image 4: Refer to caption](https://arxiv.org/html/2601.08955v1/x4.png)
344	
345	Figure 4: Comparison between our adaptive lookahead mechanism and baselines with fixed lookahead steps, with success rate (_left_) and computational cost (_right_). 
346	
347	### 4.3 Benefits of Adaptive Lookahead
348	
349	##### Superior performance-efficiency trade-off over Fixed Lookahead.
350	
351	We first compare ITP against fixed-k k lookahead, where the agent always imagines a constant horizon k k at every step. We measure compute by the total tokens consumed over an episode, T=∑t(T(t)​(π θ)+T(t)​(ℳ ϕ))T=\sum_{t}\bigl(T^{(t)}(\pi_{\theta})+T^{(t)}(\mathcal{M}_{\phi})\bigr), and report a Normalized Budget (NB) defined by:
352	
353	NB​(k)=T¯​(k)−T¯​(0)T¯​(K max)−T¯​(0).\text{NB}(k)=\frac{\bar{T}(k)-\bar{T}(0)}{\bar{T}(K_{\max})-\bar{T}(0)}.
354	
355	This calculation of the computational budget transforms the average episode tokens T¯​(k)\bar{T}(k) to the [0,1][0,1] range. In subsequent experiments, we set K max=5 K_{\max}{=}5 on the ALFWorld and K max=8 K_{\max}{=}8 on the ScienceWorld benchmark, respectively (see Appendix[B](https://arxiv.org/html/2601.08955v1#A2 "Appendix B Additional Implementation Details ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models")).
356	
357	As shown in Figure[4](https://arxiv.org/html/2601.08955v1#S4.F4 "Figure 4 ‣ Ablation Study. ‣ 4.2 Main Results ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models") (left), fixed horizons are brittle: SR peaks at a moderate k k and then drops. In contrast, ITP’s adaptive lookahead preserves a significantly higher success rate, removing the need to tune a global horizon and avoiding the diminishing-returns regime of large k k. As shown in Figure[4](https://arxiv.org/html/2601.08955v1#S4.F4 "Figure 4 ‣ Ablation Study. ‣ 4.2 Main Results ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models") (right), the fixed-k k lookahead strategy remains cost-inefficient, where its normalized budget grows steeply as k k increases. In comparison, our adaptive lookahead attains a significantly lower budget, eliminating complex tuning and avoiding the high cost of large lookahead steps.
358	
359	![Image 5: Refer to caption](https://arxiv.org/html/2601.08955v1/x5.png)
360	
361	(a) Our ITP I\texttt{ITP}_{\text{I}} vs. ReAct + Random Lookahead
362	
363	![Image 6: Refer to caption](https://arxiv.org/html/2601.08955v1/x6.png)
364	
365	(b) Our ITP R\texttt{ITP}_{\text{R}} vs. SFT + Random Lookahead
366	
367	Figure 5: Comparison between our adaptive lookahead mechanism (both ITP I\texttt{ITP}_{\text{I}} and ITP R\texttt{ITP}_{\text{R}}) and baselines with a random lookahead strategy (ReAct and SFT).
368	
369	##### Higher success rates with reduced computational cost over Random Lookahead.
370	
371	While Figure[4](https://arxiv.org/html/2601.08955v1#S4.F4 "Figure 4 ‣ Ablation Study. ‣ 4.2 Main Results ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models") compares ITP to fixed-horizon lookahead, it may also vary the horizon over time. To disentangle the benefit of adaptive horizon selection from merely using a non-constant horizon, we additionally compare against random lookahead, which samples K t K_{t} independently at each step. We evaluate the SR vs. NB trade-off on ALFWorld using Qwen3-8B for both the policy and the world model. We run 140 tasks grouped into 14 folds and report fold-averaged SR and NB, where each point in Figure[5](https://arxiv.org/html/2601.08955v1#S4.F5 "Figure 5 ‣ Superior performance-efficiency trade-off over Fixed Lookahead. ‣ 4.3 Benefits of Adaptive Lookahead ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models") corresponds to one fold. We observe that our adaptive lookahead consistently dominates the random strategy, achieving higher SR under lower and more stable budgets. This confirms that the improvements stem from state-conditioned allocation of lookahead, rather than stochasticity or horizon variability per step.
372	
373	### 4.4 Impact of World Models
374	
375	In this section, we study how the choice of world-model backbones affects ultimate performance. We fix the agent policy to Qwen3-8B, and instantiate the world model with Qwen3-8B, Llama3.1-8B, and the large-scale DeepSeek-V3.2(DeepSeek-AI et al., [2025](https://arxiv.org/html/2601.08955v1#bib.bib36 "DeepSeek-v3.2: pushing the frontier of open large language models")). Here, DeepSeek-V3.2 is not trained with a world-modeling objective. We evaluate ITP I\texttt{ITP}_{\text{I}} and ITP R\texttt{ITP}_{\text{R}} on the ALFWorld benchmark.
376	
377	Figure[6](https://arxiv.org/html/2601.08955v1#S4.F6 "Figure 6 ‣ 4.4 Impact of World Models ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models") shows that world-model backbone choice matters most in the training-free setting. With ITP I\texttt{ITP}_{\text{I}}, using DeepSeek-V3.2 (without world-model training) yields markedly weaker performance, whereas Qwen and Llama world models maintain high success rates across task families. However, after training with ITP R\texttt{ITP}_{\text{R}}, DeepSeek-V3.2 becomes competitive, reaching success rates comparable to or outperforming other world models.
378	
379	![Image 7: Refer to caption](https://arxiv.org/html/2601.08955v1/x7.png)
380	
381	(a) ITP I\texttt{ITP}_{\text{I}} (Ours)
382	
383	![Image 8: Refer to caption](https://arxiv.org/html/2601.08955v1/x8.png)
384	
385	(b) ITP R\texttt{ITP}_{\text{R}} (Ours)
386	
387	Figure 6: Impact of different world-model backbones. We report success rates of (a) ITP I\texttt{ITP}_{\text{I}} and (b) ITP R\texttt{ITP}_{\text{R}} across six different tasks on ALFWorld.
388	
389	5 Related Work
390	--------------
391	
392	##### LLM-based Agents.
393	
394	LLM-based agents typically use language models as policies that map instructions and partial observations to executable actions. A significant line of work formulates agent learning as trajectory- or step-level optimization. For example, ETO(Song et al., [2024](https://arxiv.org/html/2601.08955v1#bib.bib12 "Trial and error: exploration-based trajectory optimization of LLM agents")) frames learning as exploration-based trajectory optimization, while IPR(Xiong et al., [2024](https://arxiv.org/html/2601.08955v1#bib.bib13 "Watch every step! LLM agent learning via iterative step-level process refinement")) and E 2 CL(Wang et al., [2024b](https://arxiv.org/html/2601.08955v1#bib.bib27 "E2CL: exploration-based error correction learning for embodied agents")) refine agent behavior via iterative revision and correction signals. More recent post-training methods further improve robustness and generalization through reflective updates, such as Agent-R(Yuan et al., [2025](https://arxiv.org/html/2601.08955v1#bib.bib34 "Agent-r: training language model agents to reflect via iterative self-training")), STeCa(Wang et al., [2025b](https://arxiv.org/html/2601.08955v1#bib.bib10 "STeCa: step-level trajectory calibration for LLM agent learning")), and AgentRefine(Fu et al., [2025](https://arxiv.org/html/2601.08955v1#bib.bib35 "AgentRefine: enhancing agent generalization through refinement tuning")). However, these methods primarily focus on learning from historical traces, often leaving the agent in a state of “shallow grounding” where it lacks the proactive foresight to anticipate future environmental shifts before execution.
395	
396	##### World Models for Planning.
397	
398	World models provide a “mental sandbox” for agents, enabling model-based decision-making by predicting environment dynamics(LeCun, [2022](https://arxiv.org/html/2601.08955v1#bib.bib22 "A path towards autonomous machine intelligence version 0.9. 2, 2022-06-27"); Xiang et al., [2024](https://arxiv.org/html/2601.08955v1#bib.bib1 "Language models meet world models: embodied experiences enhance language models"); Wang et al., [2025d](https://arxiv.org/html/2601.08955v1#bib.bib20 "World modeling makes a better planner: dual preference optimization for embodied task planning")). Recent research has increasingly positioned LLMs as either implicit or explicit world models for task planning. For instance, RAP(Hao et al., [2023](https://arxiv.org/html/2601.08955v1#bib.bib21 "Reasoning with language model is planning with world model")) treats LLM reasoning as a planning process over an implicit state space, while other works explicitly construct world models to simulate future states and verify plan feasibility(Guan et al., [2023](https://arxiv.org/html/2601.08955v1#bib.bib28 "Leveraging pre-trained large language models to construct and utilize world models for model-based task planning")). To improve simulation fidelity, methods like WKM(Qiao et al., [2024](https://arxiv.org/html/2601.08955v1#bib.bib26 "Agent planning with world knowledge model")) and IWM(Zhang et al., [2025](https://arxiv.org/html/2601.08955v1#bib.bib25 "Agent learning via early experience")) incorporate world knowledge or historical experience to guide rollouts, while D2PO(Wang et al., [2025d](https://arxiv.org/html/2601.08955v1#bib.bib20 "World modeling makes a better planner: dual preference optimization for embodied task planning")) and internalizing strategies(Chen et al., [2025](https://arxiv.org/html/2601.08955v1#bib.bib30 "Internalizing world models via self-play finetuning for agentic rl")) use preference signals or reinforcement learning to align planning behavior with environmental feedback. Further specialized architectures, such as WebEvolver(Fang et al., [2025](https://arxiv.org/html/2601.08955v1#bib.bib24 "WebEvolver: enhancing web agent self-improvement with co-evolving world model")) and DMWM(Wang et al., [2025c](https://arxiv.org/html/2601.08955v1#bib.bib32 "DMWM: dual-mind world model with long-term imagination")), explore world-model-driven agents in complex, high-stakes domains. Unlike existing methods that rely on rigid, fixed-horizon planning, our work formalizes the POIMDP to integrate imagined futures directly into the agent’s decision state. We propose an adaptive lookahead mechanism that dynamically scales the imagination horizon. This allows the agent to optimize the balance between foresight reliability and computational efficiency.
399	
400	6 Conclusion
401	------------
402	
403	In this paper, we propose Imagine-then-Plan (ITP), an agent learning framework that equips LLM-based agents with adaptive lookahead with world models. By extending the conventional Partially Observable MDP to a Partially Observable and Imaginable MDP, ITP enables agents to explicitly reason over both the observable present and imaginable future trajectories, addressing the shallow grounding limitation of reactive decision making. We instantiate ITP into both an inference-time variant and a reinforcement-trained variant. Extensive experiments demonstrate that our approach significantly improves task success and robustness across domains, and further analyses validate the critical role of the adaptive control of imagination horizon. We believe that ITP provides a principled advancement toward more deliberative utilization of world models for autonomous agent learning.
404	
405	Limitations
406	-----------
407	
408	While our approach demonstrates superior performance compared to baseline methods, it is important to acknowledge the limitations of our current work as follows: (1) Current evaluation primarily focuses on interactive text-based benchmarks. While these environments provide a rigorous test of long-horizon reasoning, they do not fully capture the challenges of multimodal environments, open-world tool-use, or real-world robotic control. The transition from linguistic state descriptions to visual or sensorimotor observations may introduce additional noise that could affect the stability of the adaptive lookahead mechanism. (2) Although our adaptive lookahead mechanism is designed to optimize efficiency by scaling the imagination horizon, the use of world models inherently introduces higher inference-time overhead compared to purely reactive agents. While higher success rates in high-stakes tasks often justify this trade-off, further optimization (e.g., via speculative decoding or distilled world models) is needed for real-time applications. We will leave these directions as our future work.
409	
410	Ethics Statement
411	----------------
412	
413	We strictly follow the protocols governing the academic use of all LLMs. Our study is conducted in simulated, text-based benchmarks and involves no human subjects or personally identifying information. We cite and comply with the licenses of all models, datasets, and software used. We acknowledge that world-model-based lookahead may introduce potential risks if transferred beyond our simulated evaluation settings: prediction errors and hallucinated rollouts could lead to unsafe or unintended actions in open-world tool-use systems or robots, and the generation of imagined trajectories increases inference-time computation and energy cost. Additionally, while AI assistants (e.g., Cursor and ChatGPT) were partially utilized for coding and linguistic refinement, we affirm that all core content and findings in this paper are the original work of the authors.
414	
415	References
416	----------
417	
418	*   Optimal control of markov processes with incomplete state information i. Journal of Mathematical Analysis and Applications 10,  pp.174–205. Cited by: [§1](https://arxiv.org/html/2601.08955v1#S1.p3.1 "1 Introduction ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
419	*   B. Chen, C. Shu, E. Shareghi, N. Collier, K. Narasimhan, and S. Yao (2023)Fireact: toward language agent fine-tuning. arXiv preprint arXiv:2310.05915. Cited by: [§4.1](https://arxiv.org/html/2601.08955v1#S4.SS1.SSS0.Px3.p1.1 "Baseline Methods. ‣ 4.1 Experimental Settings ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
420	*   S. Chen, T. Zhu, Z. Wang, J. Zhang, K. Wang, S. Gao, T. Xiao, Y. W. Teh, J. He, and M. Li (2025)Internalizing world models via self-play finetuning for agentic rl. arXiv preprint arXiv:2510.15047. Cited by: [§5](https://arxiv.org/html/2601.08955v1#S5.SS0.SSS0.Px2.p1.1 "World Models for Planning. ‣ 5 Related Work ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
421	*   DeepSeek-AI, A. Liu, A. Mei, B. Lin, B. Xue, B. Wang, B. Xu, B. Wu, B. Zhang, C. Lin, C. Dong, et al. (2025)DeepSeek-v3.2: pushing the frontier of open large language models. arXiv preprint arXiv:2512.02556. Cited by: [§4.4](https://arxiv.org/html/2601.08955v1#S4.SS4.p1.2 "4.4 Impact of World Models ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
422	*   A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten, A. Yang, A. Fan, et al. (2024)The llama 3 herd of models. arXiv preprint arXiv:2407.21783. Cited by: [Appendix B](https://arxiv.org/html/2601.08955v1#A2.p1.1 "Appendix B Additional Implementation Details ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§4.1](https://arxiv.org/html/2601.08955v1#S4.SS1.SSS0.Px2.p1.1 "Backbone Models. ‣ 4.1 Experimental Settings ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
423	*   T. Fang, H. Zhang, Z. Zhang, K. Ma, W. Yu, H. Mi, and D. Yu (2025)WebEvolver: enhancing web agent self-improvement with co-evolving world model. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, C. Christodoulopoulos, T. Chakraborty, C. Rose, and V. Peng (Eds.), Suzhou, China,  pp.8970–8986. External Links: [Link](https://aclanthology.org/2025.emnlp-main.454/), [Document](https://dx.doi.org/10.18653/v1/2025.emnlp-main.454)Cited by: [§5](https://arxiv.org/html/2601.08955v1#S5.SS0.SSS0.Px2.p1.1 "World Models for Planning. ‣ 5 Related Work ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
424	*   L. Feng, Z. Xue, T. Liu, and B. An (2025)Group-in-group policy optimization for llm agent training. arXiv preprint arXiv:2505.10978. Cited by: [§4.1](https://arxiv.org/html/2601.08955v1#S4.SS1.SSS0.Px4.p1.1 "Evaluation Metrics. ‣ 4.1 Experimental Settings ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
425	*   D. Fu, K. He, Y. Wang, W. Hong, Z. GongQue, W. Zeng, W. Wang, J. Wang, X. Cai, and W. Xu (2025)AgentRefine: enhancing agent generalization through refinement tuning. In The Thirteenth International Conference on Learning Representations (ICLR), Cited by: [§5](https://arxiv.org/html/2601.08955v1#S5.SS0.SSS0.Px1.p1.1 "LLM-based Agents. ‣ 5 Related Work ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
426	*   P. Fung, Y. Bachrach, A. Celikyilmaz, K. Chaudhuri, D. Chen, W. Chung, E. Dupoux, H. Gong, H. Jégou, A. Lazaric, et al. (2025)Embodied ai agents: modeling the world. arXiv preprint arXiv:2506.22355. Cited by: [§1](https://arxiv.org/html/2601.08955v1#S1.p1.1 "1 Introduction ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
427	*   L. Guan, K. Valmeekam, S. Sreedharan, and S. Kambhampati (2023)Leveraging pre-trained large language models to construct and utilize world models for model-based task planning. In Advances in Neural Information Processing Systems, Vol. 36,  pp.79081–79094. Cited by: [§5](https://arxiv.org/html/2601.08955v1#S5.SS0.SSS0.Px2.p1.1 "World Models for Planning. ‣ 5 Related Work ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
428	*   D. Hafner, J. Pasukonis, J. Ba, and T. Lillicrap (2023)Mastering diverse domains through world models. arXiv preprint arXiv:2301.04104. Cited by: [§1](https://arxiv.org/html/2601.08955v1#S1.p2.1 "1 Introduction ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
429	*   S. Hao, Y. Gu, H. Ma, J. Hong, Z. Wang, D. Wang, and Z. Hu (2023)Reasoning with language model is planning with world model. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, H. Bouamor, J. Pino, and K. Bali (Eds.), Singapore,  pp.8154–8173. External Links: [Link](https://aclanthology.org/2023.emnlp-main.507/), [Document](https://dx.doi.org/10.18653/v1/2023.emnlp-main.507)Cited by: [§1](https://arxiv.org/html/2601.08955v1#S1.p2.1 "1 Introduction ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§4.1](https://arxiv.org/html/2601.08955v1#S4.SS1.SSS0.Px3.p1.1 "Baseline Methods. ‣ 4.1 Experimental Settings ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§5](https://arxiv.org/html/2601.08955v1#S5.SS0.SSS0.Px2.p1.1 "World Models for Planning. ‣ 5 Related Work ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
430	*   Y. LeCun (2022)A path towards autonomous machine intelligence version 0.9. 2, 2022-06-27. Open Review 62 (1),  pp.1–62. Cited by: [§1](https://arxiv.org/html/2601.08955v1#S1.p2.1 "1 Introduction ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§2](https://arxiv.org/html/2601.08955v1#S2.SS0.SSS0.Px2.p1.3 "LLMs as World Models. ‣ 2 Preliminaries ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§5](https://arxiv.org/html/2601.08955v1#S5.SS0.SSS0.Px2.p1.1 "World Models for Planning. ‣ 5 Related Work ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
431	*   G. Li, H. Hammoud, H. Itani, D. Khizbullin, and B. Ghanem (2023)Camel: communicative agents for" mind" exploration of large language model society. In Advances in Neural Information Processing Systems, Vol. 36,  pp.51991–52008. Cited by: [§1](https://arxiv.org/html/2601.08955v1#S1.p1.1 "1 Introduction ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
432	*   Y. Li, H. Wang, J. Qiu, Z. Yin, D. Zhang, C. Qian, Z. Li, P. Ma, G. Chen, H. Ji, et al. (2025)From word to world: can large language models be implicit text-based world models?. arXiv preprint arXiv:2512.18832. Cited by: [§2](https://arxiv.org/html/2601.08955v1#S2.SS0.SSS0.Px2.p1.3 "LLMs as World Models. ‣ 2 Preliminaries ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
433	*   V. Mnih, A. P. Badia, M. Mirza, A. Graves, T. Lillicrap, T. Harley, D. Silver, and K. Kavukcuoglu (2016)Asynchronous methods for deep reinforcement learning. In International conference on machine learning,  pp.1928–1937. Cited by: [§3.3.2](https://arxiv.org/html/2601.08955v1#S3.SS3.SSS2.Px3.p2.4 "Stage 3: Online Optimization. ‣ 3.3.2 Reinforced Training (\"ITP\"_\"R\") ‣ 3.3 Planning with Adaptive Lookahead ‣ 3 Method ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
434	*   S. Qiao, R. Fang, N. Zhang, Y. Zhu, X. Chen, S. Deng, Y. Jiang, P. Xie, F. Huang, and H. Chen (2024)Agent planning with world knowledge model. In Advances in Neural Information Processing Systems, Vol. 37,  pp.114843–114871. Cited by: [§1](https://arxiv.org/html/2601.08955v1#S1.p2.1 "1 Introduction ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§4.1](https://arxiv.org/html/2601.08955v1#S4.SS1.SSS0.Px3.p1.1 "Baseline Methods. ‣ 4.1 Experimental Settings ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§5](https://arxiv.org/html/2601.08955v1#S5.SS0.SSS0.Px2.p1.1 "World Models for Planning. ‣ 5 Related Work ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
435	*   N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao (2023)Reflexion: language agents with verbal reinforcement learning. In Advances in Neural Information Processing Systems, Vol. 36,  pp.8634–8652. Cited by: [§1](https://arxiv.org/html/2601.08955v1#S1.p1.1 "1 Introduction ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
436	*   M. Shridhar, J. Thomason, D. Gordon, Y. Bisk, W. Han, R. Mottaghi, L. Zettlemoyer, and D. Fox (2020)ALFRED: A benchmark for interpreting grounded instructions for everyday tasks. In 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition, CVPR 2020, Seattle, WA, USA, June 13-19, 2020,  pp.10737–10746. External Links: [Document](https://dx.doi.org/10.1109/CVPR42600.2020.01075), [Link](https://doi.org/10.1109/CVPR42600.2020.01075)Cited by: [§A.1](https://arxiv.org/html/2601.08955v1#A1.SS1.p1.1 "A.1 Datasets ‣ Appendix A Datasets and Preprocessing ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§4.1](https://arxiv.org/html/2601.08955v1#S4.SS1.SSS0.Px1.p1.1 "Benchmarks. ‣ 4.1 Experimental Settings ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
437	*   Y. Song, D. Yin, X. Yue, J. Huang, S. Li, and B. Y. Lin (2024)Trial and error: exploration-based trajectory optimization of LLM agents. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), L. Ku, A. Martins, and V. Srikumar (Eds.), Bangkok, Thailand,  pp.7584–7600. External Links: [Link](https://aclanthology.org/2024.acl-long.409/), [Document](https://dx.doi.org/10.18653/v1/2024.acl-long.409)Cited by: [§1](https://arxiv.org/html/2601.08955v1#S1.p3.1 "1 Introduction ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§5](https://arxiv.org/html/2601.08955v1#S5.SS0.SSS0.Px1.p1.1 "LLM-based Agents. ‣ 5 Related Work ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
438	*   G. Wang, Y. Xie, Y. Jiang, A. Mandlekar, C. Xiao, Y. Zhu, L. Fan, and A. Anandkumar (2024a)Voyager: an open-ended embodied agent with large language models. Transactions on Machine Learning Research. Cited by: [§1](https://arxiv.org/html/2601.08955v1#S1.p1.1 "1 Introduction ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
439	*   H. Wang, C. T. Leong, J. Wang, and W. Li (2024b)E 2 CL: exploration-based error correction learning for embodied agents. In Findings of the Association for Computational Linguistics: EMNLP 2024, Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.), Miami, Florida, USA,  pp.7626–7639. External Links: [Link](https://aclanthology.org/2024.findings-emnlp.448/), [Document](https://dx.doi.org/10.18653/v1/2024.findings-emnlp.448)Cited by: [§5](https://arxiv.org/html/2601.08955v1#S5.SS0.SSS0.Px1.p1.1 "LLM-based Agents. ‣ 5 Related Work ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
440	*   H. Wang, C. T. Leong, J. Wang, J. Wang, and W. Li (2025a)SPA-rl: reinforcing llm agents via stepwise progress attribution. arXiv preprint arXiv:2505.20732. Cited by: [§4.1](https://arxiv.org/html/2601.08955v1#S4.SS1.SSS0.Px4.p1.1 "Evaluation Metrics. ‣ 4.1 Experimental Settings ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
441	*   H. Wang, J. Wang, C. T. Leong, and W. Li (2025b)STeCa: step-level trajectory calibration for LLM agent learning. In Findings of the Association for Computational Linguistics: ACL 2025, W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.), Vienna, Austria,  pp.11597–11614. External Links: [Link](https://aclanthology.org/2025.findings-acl.604/), [Document](https://dx.doi.org/10.18653/v1/2025.findings-acl.604)Cited by: [§1](https://arxiv.org/html/2601.08955v1#S1.p3.1 "1 Introduction ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§5](https://arxiv.org/html/2601.08955v1#S5.SS0.SSS0.Px1.p1.1 "LLM-based Agents. ‣ 5 Related Work ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
442	*   L. Wang, R. Shelim, W. Saad, and N. Ramakrishnan (2025c)DMWM: dual-mind world model with long-term imagination. In The Thirty-ninth Annual Conference on Neural Information Processing Systems, Cited by: [§5](https://arxiv.org/html/2601.08955v1#S5.SS0.SSS0.Px2.p1.1 "World Models for Planning. ‣ 5 Related Work ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
443	*   R. Wang, P. Jansen, M. Côté, and P. Ammanabrolu (2022)ScienceWorld: is your agent smarter than a 5th grader?. In EMNLP, Cited by: [§A.1](https://arxiv.org/html/2601.08955v1#A1.SS1.p1.1 "A.1 Datasets ‣ Appendix A Datasets and Preprocessing ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§4.1](https://arxiv.org/html/2601.08955v1#S4.SS1.SSS0.Px1.p1.1 "Benchmarks. ‣ 4.1 Experimental Settings ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
444	*   S. Wang, Z. Fei, Q. Cheng, S. Zhang, P. Cai, J. Fu, and X. Qiu (2025d)World modeling makes a better planner: dual preference optimization for embodied task planning. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.), Vienna, Austria,  pp.21518–21537. External Links: [Link](https://aclanthology.org/2025.acl-long.1044/), [Document](https://dx.doi.org/10.18653/v1/2025.acl-long.1044)Cited by: [§1](https://arxiv.org/html/2601.08955v1#S1.p2.1 "1 Introduction ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§5](https://arxiv.org/html/2601.08955v1#S5.SS0.SSS0.Px2.p1.1 "World Models for Planning. ‣ 5 Related Work ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
445	*   J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. H. Chi, Q. V. Le, and D. Zhou (2022)Chain-of-thought prompting elicits reasoning in large language models. In Advances in Neural Information Processing Systems, S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh (Eds.), Vol. 35,  pp.24824–24837. External Links: [Link](https://proceedings.neurips.cc/paper_files/paper/2022/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)Cited by: [§4.1](https://arxiv.org/html/2601.08955v1#S4.SS1.SSS0.Px3.p1.1 "Baseline Methods. ‣ 4.1 Experimental Settings ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
446	*   J. Xiang, T. Tao, Y. Gu, T. Shu, Z. Wang, Z. Yang, and Z. Hu (2024)Language models meet world models: embodied experiences enhance language models. Advances in neural information processing systems 36. Cited by: [§5](https://arxiv.org/html/2601.08955v1#S5.SS0.SSS0.Px2.p1.1 "World Models for Planning. ‣ 5 Related Work ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
447	*   W. Xiong, Y. Song, X. Zhao, W. Wu, X. Wang, K. Wang, C. Li, W. Peng, and S. Li (2024)Watch every step! LLM agent learning via iterative step-level process refinement. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.), Miami, Florida, USA,  pp.1556–1572. External Links: [Link](https://aclanthology.org/2024.emnlp-main.93/), [Document](https://dx.doi.org/10.18653/v1/2024.emnlp-main.93)Cited by: [§5](https://arxiv.org/html/2601.08955v1#S5.SS0.SSS0.Px1.p1.1 "LLM-based Agents. ‣ 5 Related Work ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
448	*   A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, C. Zheng, D. Liu, F. Zhou, F. Huang, F. Hu, H. Ge, H. Wei, H. Lin, J. Tang, J. Yang, J. Tu, J. Zhang, J. Yang, J. Yang, J. Zhou, J. Zhou, J. Lin, K. Dang, K. Bao, K. Yang, L. Yu, L. Deng, M. Li, M. Xue, M. Li, P. Zhang, P. Wang, Q. Zhu, R. Men, R. Gao, S. Liu, S. Luo, T. Li, T. Tang, W. Yin, X. Ren, X. Wang, X. Zhang, X. Ren, Y. Fan, Y. Su, Y. Zhang, Y. Zhang, Y. Wan, Y. Liu, Z. Wang, Z. Cui, Z. Zhang, Z. Zhou, and Z. Qiu (2025)Qwen3 technical report. arXiv preprint arXiv:2505.09388. Cited by: [Appendix B](https://arxiv.org/html/2601.08955v1#A2.p1.1 "Appendix B Additional Implementation Details ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§4.1](https://arxiv.org/html/2601.08955v1#S4.SS1.SSS0.Px2.p1.1 "Backbone Models. ‣ 4.1 Experimental Settings ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
449	*   A. Yang, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Li, D. Liu, F. Huang, H. Wei, H. Lin, J. Yang, J. Tu, J. Zhang, J. Yang, J. Yang, J. Zhou, J. Lin, K. Dang, K. Lu, K. Bao, K. Yang, L. Yu, M. Li, M. Xue, P. Zhang, Q. Zhu, R. Men, R. Lin, T. Li, T. Xia, X. Ren, X. Ren, Y. Fan, Y. Su, Y. Zhang, Y. Wan, Y. Liu, Z. Cui, Z. Zhang, and Z. Qiu (2024)Qwen2.5 technical report. arXiv preprint arXiv:2412.15115. Cited by: [Appendix B](https://arxiv.org/html/2601.08955v1#A2.p1.1 "Appendix B Additional Implementation Details ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§4.1](https://arxiv.org/html/2601.08955v1#S4.SS1.SSS0.Px2.p1.1 "Backbone Models. ‣ 4.1 Experimental Settings ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
450	*   S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao (2023)ReAct: synergizing reasoning and acting in language models. In International Conference on Learning Representations (ICLR), Cited by: [§1](https://arxiv.org/html/2601.08955v1#S1.p1.1 "1 Introduction ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§4.1](https://arxiv.org/html/2601.08955v1#S4.SS1.SSS0.Px3.p1.1 "Baseline Methods. ‣ 4.1 Experimental Settings ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
451	*   S. Yuan, Z. Chen, Z. Xi, J. Ye, Z. Du, and J. Chen (2025)Agent-r: training language model agents to reflect via iterative self-training. arXiv preprint arXiv:2501.11425. Cited by: [§5](https://arxiv.org/html/2601.08955v1#S5.SS0.SSS0.Px1.p1.1 "LLM-based Agents. ‣ 5 Related Work ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
452	*   K. Zhang, X. Chen, B. Liu, T. Xue, Z. Liao, Z. Liu, X. Wang, Y. Ning, Z. Chen, X. Fu, et al. (2025)Agent learning via early experience. arXiv preprint arXiv:2510.08558. Cited by: [§1](https://arxiv.org/html/2601.08955v1#S1.p2.1 "1 Introduction ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§2](https://arxiv.org/html/2601.08955v1#S2.SS0.SSS0.Px2.p1.3 "LLMs as World Models. ‣ 2 Preliminaries ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§4.1](https://arxiv.org/html/2601.08955v1#S4.SS1.SSS0.Px3.p1.1 "Baseline Methods. ‣ 4.1 Experimental Settings ‣ 4 Experiments ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), [§5](https://arxiv.org/html/2601.08955v1#S5.SS0.SSS0.Px2.p1.1 "World Models for Planning. ‣ 5 Related Work ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"). 
453	
454	Appendix A Datasets and Preprocessing
455	-------------------------------------
456	
457	### A.1 Datasets
458	
459	##### ALFWorld:
460	
461	ALFWorld is a text-based household embodied benchmark where an agent interacts with a simulated environment via natural-language observations and admissible text actions. Each episode specifies a goal instruction that can be instantiated from compositional templates, and success requires planning over multi-step action sequences under partial observability.
462	
463	*   •Pick: to find an object of the desired type, pick it up, navigate to the correct location/receptacle, and place it there. 
464	*   •Clean: to find the target object, pick it up, go to a sink/basin, wash it by turning on the faucet, then navigate to the target receptacle and place it. 
465	*   •Heat: to find the target object, pick it up, go to a microwave, heat it by turning on the microwave, then place it at the specified location. 
466	*   •Cool: to find the target object, pick it up, go to a fridge, cool it by placing it inside the fridge, then return and place it at the specified location. 
467	*   •Look: to find the target object, locate a light source, turn it on, and examine the object with the light while holding it. 
468	*   •Pick2: to find the first target object and place it at the destination, then find a second object of the same type, return to the destination, and place it together with the first one. 
469	
470	##### ScienceWorld:
471	
472	ScienceWorld is a text-based interactive science environment that evaluates an agent’s ability to solve procedural and reasoning-intensive tasks grounded in everyday scientific phenomena. Compared to household tasks, ScienceWorld typically involves longer horizons and requires the agent to combine information gathering, tool use, and multi-step experimentation.
473	
474	Domain Task Description Dataset Statistics
475	ALFWorld
476	Household, text-based embodied tasks Six compositional task families: Pick, Clean, Heat, Cool, Look, Pick2.Training: 3,119 Test: 140
477	ScienceWorld
478	Elementary science curriculum in an interactive text environment 30 subtasks with many variations (entities, initial conditions, distractors, room layouts), partitioned following the benchmark protocol.Training: 1,483 Test-Seen: 194 Test-Unseen: 151
479	
480	Table 2: Dataset statistics. We report dataset splits following the standard benchmark protocol.
481	
482	### A.2 Data Preprocessing
483	
484	We use the provided expert trajectories as supervision to warm-start the agent policy. For the world model, we repurpose the same expert rollouts into transition-level supervision for a text world model by emitting one record per environment step, containing: (i) a compact state string (goal + current observation + optional inventory), (ii) the executed expert action, and (iii) the next observation, optionally augmented with scalar signals such as reward and done. All records are stored in JSONL format and serialized as dialogue-style causal-LM input–output pairs, following standard SFT practice for text-based world models.
485	
486	To annotate the number of lookahead steps (i.e., K K) in ITP R\texttt{ITP}_{\text{R}}, we precompute imagined rollouts using the trained world model for a small discrete set of horizons (k_candidates) at each expert step. Each imagined rollout is summarized into a short lookahead text snippet (lookahead_summary). We then compute a per-horizon score that balances improved expert-action likelihood against deeper rollout cost, and store the resulting pseudo label (k_label) along with all scores.
487	
488	Benchmark Average K K Average Task Steps
489	ALFWorld 3 8
490	ScienceWorld 8 15
491	
492	Table 3: Average lookahead horizon step (K K) and episode length (steps) on different benchmarks.
493	
494	We conducted descriptive statistics on the average lookahead steps (Avg. K K) and average interaction steps (Avg. steps) during the adaptive planning process across different benchmark environments. As shown in the table[3](https://arxiv.org/html/2601.08955v1#A1.T3 "Table 3 ‣ A.2 Data Preprocessing ‣ Appendix A Datasets and Preprocessing ‣ Imagine-then-Plan: Agent Learning from Adaptive Lookahead with World Models"), models on ALFWorld tend to adopt shorter lookahead planning with an average K=3 K=3, while the average steps required to complete tasks is 8. This reflects relatively compact task chains and a decision space that is more easily covered within shorter lookaheads. In contrast, on ScienceWorld, the average K K increases to 8 and the average steps reach 15. This indicates that this environment typically requires longer-range reasoning and more complex state evolution modeling; the adaptive strategy more frequently selects larger lookahead depths to maintain planning stability and completion rates.
495	
496	Appendix B Additional Implementation Details
497	--------------------------------------------
498	
499	### B.1 Prompting Templates
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6c5e46d-63f9-4d32-9d62-09230fd808b9",
  "isSidechain": true,
  "promptId": "540c002c-9999-471e-b32d-70c2ebec2c01",
  "agentId": "aeb9052a04aec7401",
  "type": "user",
  "uuid": "1d2c4513-54de-47bb-9283-c242657ebce5",
  "sourceToolAssistantUUID": "b6c5e46d-63f9-4d32-9d62-09230fd808b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-12T00:51:44.059Z_

I now have the complete data from the paper. I was able to read both the HTML source text and visually verify the table image from the GitHub repository. Let me provide you with the definitive findings.

---

## Verified Results from "Imagine-then-Plan" (arXiv 2601.08955)

All numbers below come from **Table 1** of the paper, titled: *"Evaluation of task success rates (%) across ALFWorld and ScienceWorld benchmarks."* I verified them from three independent sources: (1) the arXiv HTML version at `arxiv.org/html/2601.08955v1`, (2) the raw HTML/LaTeX table data extracted from that page, and (3) the table image at `github.com/loyiv/ITP/blob/main/figures/main_table.png`.

### 1. ITP-R Overall Success Rate on ALFWorld with Qwen2.5-7B

**The overall success rate is 85.07%.** The value 94.29% is the PICK subtask score only, not the overall.

The dispute is resolved definitively: whoever claims 94.29% is the overall is incorrect -- they are confusing the PICK subtask column with the Overall column. The paper's Table 1 clearly shows these as separate columns.

### 2. Per-Subtask Scores (ALFWorld, ITP-R, Qwen2.5-7B)

| Subtask | Success Rate (%) |
|---------|-----------------|
| PICK    | 94.29           |
| CLEAN   | 88.89           |
| HEAT    | 87.50           |
| COOL    | 53.84           |
| LOOK    | 76.00           |
| PICK2   | 91.67           |
| **Overall** | **85.07**   |

Note: COOL (53.84%) is the weakest subtask by a large margin, which pulls the overall down significantly from the best subtask scores.

### 3. ITP-R Performance on ScienceWorld with Qwen2.5-7B

| Split   | Success Rate (%) |
|---------|-----------------|
| Seen    | 62.58           |
| Unseen  | 58.94           |

(The paper does not report a combined "Total" for ScienceWorld in Table 1 -- only Seen and Unseen splits are shown.)

### Additional Context for Comparison

For reference, the training-free variant **ITP-I** with Qwen2.5-7B achieves only 35.71% overall on ALFWorld and 16.49%/17.88% (Seen/Unseen) on ScienceWorld, showing the substantial impact of reinforcement training.

The best overall ALFWorld result across all backbones is ITP-R with **Qwen3-8B at 88.57%**.

Sources:
- [arXiv Abstract Page](https://arxiv.org/abs/2601.08955)
- [arXiv HTML Full Paper](https://arxiv.org/html/2601.08955v1)
- [GitHub Repository](https://github.com/loyiv/ITP)
- [HuggingFace Paper Page](https://huggingface.co/papers/2601.08955)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d2c4513-54de-47bb-9283-c242657ebce5",
  "isSidechain": true,
  "agentId": "aeb9052a04aec7401",
  "requestId": "req_011CawkwMEAGN1f2BQBPiZuT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "145afe73-2615-4a7e-95d7-124b09c1852d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "be982e2d-eefc-43fb-9f0c-35005d8376ef",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GDKsWiNyRiseqR61teSQ7x",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18863,
      "cache_read_input_tokens": 24438,
      "output_tokens": 785,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18863
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 785,
          "cache_read_input_tokens": 24438,
          "cache_creation_input_tokens": 18863,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18863,
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
