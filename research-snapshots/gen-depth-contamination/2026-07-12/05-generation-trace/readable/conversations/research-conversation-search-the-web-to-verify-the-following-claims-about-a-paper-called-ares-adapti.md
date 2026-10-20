# Research conversation: Search the web to verify the following claims about a paper called "ARES: Adaptive Reasoning Effort Selection for Effici

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aecf91e0f3be11219.jsonl`
- **Structured JSON:** [`77c9620cbffd9d941563.json`](../../sessions/77/77c9620cbffd9d941563.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

23 recorded events

### User

_source line 1 · 2026-05-11T23:31:41.330Z_

Search the web to verify the following claims about a paper called "ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents" (arXiv 2603.07915, March 2026):

1. Does this paper exist on arXiv with that ID?
2. Does it use a Qwen3-1.7B router trained via SFT?
3. Does it achieve 52.7% reasoning token reduction?
4. Is it evaluated on WebArena/TAU-Bench?
5. Is code available at github.com/UCSB-NLP-Chang/Ares?

Use WebSearch and WebFetch to verify. Report exactly what you find. If something cannot be verified, say so.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6bfca2c9-504d-4aa5-bfc1-591fd7535b04",
  "agentId": "aecf91e0f3be11219",
  "type": "user",
  "uuid": "4ab59f6e-7c3c-4ac6-86f8-b4d7dfde04f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:31:41.336Z_

```json
{
  "parentUuid": "4ab59f6e-7c3c-4ac6-86f8-b4d7dfde04f7",
  "isSidechain": true,
  "agentId": "aecf91e0f3be11219",
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
  "uuid": "0b30455a-da17-491f-b5e5-b4891d615b69",
  "timestamp": "2026-05-11T23:31:41.336Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:31:43.782Z_



I'll search for this paper and verify each claim. Let me start by loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b30455a-da17-491f-b5e5-b4891d615b69",
  "isSidechain": true,
  "agentId": "aecf91e0f3be11219",
  "requestId": "req_011Cawerthus8zJAppSNSBvo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee77d4b1-1358-45f8-a291-12cacb69ee3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xviyAs9XyVtLbSV9D7Ujg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 717,
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

_source line 4 · 2026-05-11T23:31:43.937Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Nvbp94QAsKvhVLe8Vv7ZqR`</summary>

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
  "parentUuid": "ee77d4b1-1358-45f8-a291-12cacb69ee3c",
  "isSidechain": true,
  "agentId": "aecf91e0f3be11219",
  "requestId": "req_011Cawerthus8zJAppSNSBvo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "95168d0c-c698-497b-b5c1-17f0b98baca6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xviyAs9XyVtLbSV9D7Ujg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 8223,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 717
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 717,
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

_source line 5 · 2026-05-11T23:31:43.941Z_

<details><summary>↩ Tool result · `toolu_01Nvbp94QAsKvhVLe8Vv7ZqR`</summary>

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
  "parentUuid": "95168d0c-c698-497b-b5c1-17f0b98baca6",
  "isSidechain": true,
  "promptId": "6bfca2c9-504d-4aa5-bfc1-591fd7535b04",
  "agentId": "aecf91e0f3be11219",
  "type": "user",
  "uuid": "76e63996-799e-4dce-b4c7-1e8129d9a584",
  "sourceToolAssistantUUID": "95168d0c-c698-497b-b5c1-17f0b98baca6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:31:47.770Z_



Now let me run searches in parallel to verify each claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76e63996-799e-4dce-b4c7-1e8129d9a584",
  "isSidechain": true,
  "agentId": "aecf91e0f3be11219",
  "requestId": "req_011Cawes6ETC2gHY9nYGhAfY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efcd37f0-9c29-44ee-b740-a8343dcb01be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DNeXkQfG94hMgWF35w2F9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 7 · 2026-05-11T23:31:48.873Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ANJm7dcfRZRB9FGRnB5TXD`</summary>

```json
{
  "query": "ARES Adaptive Reasoning Effort Selection Efficient LLM Agents arXiv 2603.07915"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efcd37f0-9c29-44ee-b740-a8343dcb01be",
  "isSidechain": true,
  "agentId": "aecf91e0f3be11219",
  "requestId": "req_011Cawes6ETC2gHY9nYGhAfY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f936d10-471f-471d-af49-5c8bb7541ac2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DNeXkQfG94hMgWF35w2F9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 8 · 2026-05-11T23:31:49.377Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MYosLSeCfLLHz12PcMmXbq`</summary>

```json
{
  "query": "arXiv 2603.07915 ARES paper 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f936d10-471f-471d-af49-5c8bb7541ac2",
  "isSidechain": true,
  "agentId": "aecf91e0f3be11219",
  "requestId": "req_011Cawes6ETC2gHY9nYGhAfY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5de386d7-cc38-4cb6-bea8-59adde6c5264",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DNeXkQfG94hMgWF35w2F9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 9 · 2026-05-11T23:31:50.192Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XuKnH36emjU1UbLnzDYnjX`</summary>

```json
{
  "query": "github.com/UCSB-NLP-Chang/Ares reasoning effort LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5de386d7-cc38-4cb6-bea8-59adde6c5264",
  "isSidechain": true,
  "agentId": "aecf91e0f3be11219",
  "requestId": "req_011Cawes6ETC2gHY9nYGhAfY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14d6123a-190f-4ae8-8f95-fa9978b13e49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DNeXkQfG94hMgWF35w2F9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8940,
      "output_tokens": 198,
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
          "output_tokens": 198,
          "cache_read_input_tokens": 8940,
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

_source line 10 · 2026-05-11T23:31:55.705Z_

<details><summary>↩ Tool result · `toolu_01XuKnH36emjU1UbLnzDYnjX`</summary>

```text
Web search results for query: "github.com/UCSB-NLP-Chang/Ares reasoning effort LLM"

Links: [{"title":"GitHub - UCSB-NLP-Chang/Ares: Official implementation for \"Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\" · GitHub","url":"https://github.com/UCSB-NLP-Chang/Ares"},{"title":"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents","url":"https://arxiv.org/pdf/2603.07915"},{"title":"UCSB ML&NLP Group · GitHub","url":"https://github.com/UCSB-NLP-Chang"},{"title":"GitHub - UCSB-NLP-Chang/llm_uncertainty · GitHub","url":"https://github.com/UCSB-NLP-Chang/llm_uncertainty"},{"title":"GitHub - UCSB-NLP-Chang/Skill-Usage · GitHub","url":"https://github.com/UCSB-NLP-Chang/Skill-Usage"},{"title":"GitHub - UCSB-NLP-Chang/ThinkPrune","url":"https://github.com/UCSB-NLP-Chang/ThinkPrune"},{"title":"GitHub - UCSB-NLP-Chang/ULD: Implementation of paper 'Reversing the Forget-Retain Objectives: An Efficient LLM Unlearning Framework from Logit Difference' [NeurIPS'24]","url":"https://github.com/UCSB-NLP-Chang/ULD"},{"title":"GitHub - UCSB-NLP-Chang/Visual-Spatial-Planning: Official release of the benchmark in paper \"VSP: Diagnosing the Dual Challenges of Perception and Reasoning in Spatial Planning Tasks for MLLMs\"","url":"https://github.com/UCSB-NLP-Chang/Visual-Spatial-Planning"},{"title":"GitHub - UCSB-NLP-Chang/BTProp · GitHub","url":"https://github.com/UCSB-NLP-Chang/BTProp"},{"title":"GitHub - zjunlp/Prompt4ReasoningPapers: [ACL 2023] Reasoning with Language Model Prompting: A Survey · GitHub","url":"https://github.com/zjunlp/Prompt4ReasoningPapers"}]

Based on the search results, here's what I found about the Ares project:

The Ares repository is the official implementation for "Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents".

According to the research paper, the system uses a lightweight router LLM that at each turn receives the same input context as the agent and predicts the optimal reasoning effort level from a discrete space including low, medium, and high levels.

The training pipeline involves four phases: (1) Trajectory Collection - filtering successful trajectories with minimal steps; (2) Effort Annotation - identifying the minimum sufficient reasoning effort for each step via sampling and LLM verification; (3) Rationale Generation - having a teacher LLM generate semantic justifications; and (4) Supervised Fine-tuning - fine-tuning the ARES router to jointly predict rationales and effort labels.

The project demonstrates how LLM agents can be optimized to dynamically select different levels of reasoning effort to improve efficiency while maintaining performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14d6123a-190f-4ae8-8f95-fa9978b13e49",
  "isSidechain": true,
  "promptId": "6bfca2c9-504d-4aa5-bfc1-591fd7535b04",
  "agentId": "aecf91e0f3be11219",
  "type": "user",
  "uuid": "85b537cb-fd84-491e-a0cd-6fd2663f9d46",
  "sourceToolAssistantUUID": "14d6123a-190f-4ae8-8f95-fa9978b13e49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-11T23:31:55.969Z_

<details><summary>↩ Tool result · `toolu_01MYosLSeCfLLHz12PcMmXbq`</summary>

```text
Web search results for query: "arXiv 2603.07915 ARES paper 2026"

Links: [{"title":"[2603.07915] Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents","url":"https://arxiv.org/abs/2603.07915"},{"title":"Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents","url":"https://arxiv.org/html/2603.07915"},{"title":"GitHub - Paper2Chinese/CVPR-2026-reading-papers-with-code · GitHub","url":"https://github.com/Paper2Chinese/CVPR-2026-reading-papers-with-code"},{"title":"Paper page - Hyperagents","url":"https://huggingface.co/papers/2603.19461"},{"title":"GitHub - shawn0728/ARES: [ICLR 2026]🌴 ARES is an open-source framework for adaptive multimodal reasoning, featuring a two-stage pipeline—Adaptive Cold-Start and Entropy-Shaped Policy Optimization—to balance reasoning depth and efficiency.","url":"https://github.com/shawn0728/ARES"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1408&show=2000"},{"title":"[2603.15031] Attention Residuals","url":"https://arxiv.org/abs/2603.15031"},{"title":"Version March 19, 2026","url":"https://arxiv.org/pdf/2603.17011"},{"title":"[2603.00510] What Do Visual Tokens Really Encode? Uncovering Sparsity and Redundancy in Multimodal Large Language Models","url":"https://arxiv.org/abs/2603.00510"},{"title":"[2603.29973] Various conjectural series identities","url":"https://arxiv.org/abs/2603.29973"}]

Based on the search results, I found information about the arXiv paper 2603.07915:

## ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents

The paper is titled "Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents" and was submitted on March 9, 2026 by authors including Jingbo Yang, Bairu Hou, Wei Wei, Yujia Bao, and Shiyu Chang.

**Overview:**
The paper addresses how modern agents powered by thinking LLMs achieve high accuracy through long chain-of-thought reasoning but incur substantial inference costs. 

**The ARES Framework:**
The paper proposes Ares, a framework for per-step dynamic reasoning effort selection tailored for multi-step agent tasks. Ares employs a lightweight router to predict the lowest appropriate reasoning level for each step based on the interaction history.

**Key Results:**
Experimental results show that Ares reduces reasoning token usage by up to 52.7% compared to fixed high-effort reasoning, while introducing minimal degradation in task success rates. The system was evaluated on a diverse set of agent tasks, including TAU-Bench for tool use agents, BrowseComp-Plus for deep-research agents, and WebArena for web agents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5de386d7-cc38-4cb6-bea8-59adde6c5264",
  "isSidechain": true,
  "promptId": "6bfca2c9-504d-4aa5-bfc1-591fd7535b04",
  "agentId": "aecf91e0f3be11219",
  "type": "user",
  "uuid": "4eb5cece-5fa6-4ba3-a7eb-65f0ddfa0894",
  "sourceToolAssistantUUID": "5de386d7-cc38-4cb6-bea8-59adde6c5264",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-11T23:31:57.137Z_

<details><summary>↩ Tool result · `toolu_01ANJm7dcfRZRB9FGRnB5TXD`</summary>

```text
Web search results for query: "ARES Adaptive Reasoning Effort Selection Efficient LLM Agents arXiv 2603.07915"

Links: [{"title":"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents","url":"https://arxiv.org/pdf/2603.07915"},{"title":"[2603.07915] Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents","url":"https://arxiv.org/abs/2603.07915"},{"title":"From Efficiency to Adaptivity: A Deeper Look at Adaptive Reasoning in Large Language Models","url":"https://arxiv.org/html/2511.10788"},{"title":"ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping","url":"https://arxiv.org/html/2510.08457v1"},{"title":"e1: Learning Adaptive Control of Reasoning Effort","url":"https://arxiv.org/html/2510.27042v1"},{"title":"AI Papers | Explore Latest Research","url":"https://www.aimodels.fyi/papers/arxiv/ares-adaptive-reasoning-effort-selection-efficient-llm"},{"title":"Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs","url":"https://arxiv.org/html/2507.02076v1"},{"title":"[2511.10788] From Efficiency to Adaptivity: A Deeper Look at Adaptive Reasoning in Large Language Models","url":"https://arxiv.org/abs/2511.10788"},{"title":"Multi-Layered Memory Architectures for LLM Agents: An Experimental Evaluation of Long-Term Context Retention","url":"https://arxiv.org/html/2603.29194"},{"title":"LLM-based Agentic Reasoning Frameworks: A Survey from Methods to Scenarios","url":"https://arxiv.org/html/2508.17692v1"}]

I found the paper you're looking for! Here are the key details about ARES:

## Overview
ARES is a framework for per-step dynamic reasoning effort selection tailored for multi-step agent tasks.

## Problem Being Addressed
Modern agents powered by thinking LLMs achieve high accuracy through long chain-of-thought reasoning but incur substantial inference costs. While many LLMs now support configurable reasoning levels (e.g., high/medium/low), static strategies are often ineffective: using low-effort modes at every step leads to significant performance degradation, while random selection fails to preserve accuracy or provide meaningful cost reduction.

## Solution
ARES employs a lightweight router to predict the lowest appropriate reasoning level for each step based on the interaction history. To train this router, the framework develops a data generation pipeline that identifies the minimum reasoning effort required for successful step completion. The router is then fine-tuned to predict these levels, enabling plug-and-play integration for any LLM agents.

## Results
The framework was evaluated on a diverse set of agent tasks, including TAU-Bench for tool use agents, BrowseComp-Plus for deep-research agents, and WebArena for web agents. Experimental results show that ARES reduces reasoning token usage by up to 52.7% compared to fixed high-effort reasoning, while introducing minimal degradation in task success rates.

The paper (arXiv:2603.07915) was submitted on March 9, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f936d10-471f-471d-af49-5c8bb7541ac2",
  "isSidechain": true,
  "promptId": "6bfca2c9-504d-4aa5-bfc1-591fd7535b04",
  "agentId": "aecf91e0f3be11219",
  "type": "user",
  "uuid": "8efde4f6-4e92-44ac-b855-6e95038b8643",
  "sourceToolAssistantUUID": "1f936d10-471f-471d-af49-5c8bb7541ac2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-11T23:32:01.315Z_

Good, I've confirmed the paper exists and several claims. Now let me fetch the actual arXiv abstract page and the GitHub repo to verify the specific details about the Qwen3-1.7B router and SFT training.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8efde4f6-4e92-44ac-b855-6e95038b8643",
  "isSidechain": true,
  "agentId": "aecf91e0f3be11219",
  "requestId": "req_011Cawet4FfKKJRniN28wG8y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1c5ccab-9fff-45c8-bf4c-83ca4ac07e72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqLpKy2ESV2WQztre13wmJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1681,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 10850,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1066,
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

_source line 14 · 2026-05-11T23:32:04.242Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011h778j9XvQcQ2nmHj2D41x`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.07915",
  "prompt": "Extract the full abstract, list of authors, submission date, and any mention of what model is used as the router (e.g. Qwen3-1.7B or similar). Also note any mention of evaluation benchmarks (WebArena, TAU-Bench, etc.), reasoning token reduction percentages, and training method (SFT / supervised fine-tuning)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1c5ccab-9fff-45c8-bf4c-83ca4ac07e72",
  "isSidechain": true,
  "agentId": "aecf91e0f3be11219",
  "requestId": "req_011Cawet4FfKKJRniN28wG8y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d4940a54-b0f3-4830-a6c1-bdd01817d096",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqLpKy2ESV2WQztre13wmJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1681,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 10850,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1066,
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

_source line 15 · 2026-05-11T23:32:05.635Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GPUSwdSrJ3CZtLiD3buiBj`</summary>

```json
{
  "url": "https://github.com/UCSB-NLP-Chang/Ares",
  "prompt": "Extract the README content. Look for any mention of the router model (Qwen3-1.7B or similar), training method (SFT), evaluation benchmarks, reasoning token reduction numbers, and code availability status. List all key details you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4940a54-b0f3-4830-a6c1-bdd01817d096",
  "isSidechain": true,
  "agentId": "aecf91e0f3be11219",
  "requestId": "req_011Cawet4FfKKJRniN28wG8y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7aa1dba9-3fec-4a74-9ca2-602b11a42bb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqLpKy2ESV2WQztre13wmJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1681,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 10850,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1066
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1681,
          "output_tokens": 337,
          "cache_read_input_tokens": 10850,
          "cache_creation_input_tokens": 1066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1066,
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

_source line 16 · 2026-05-11T23:32:09.560Z_

<details><summary>↩ Tool result · `toolu_01GPUSwdSrJ3CZtLiD3buiBj`</summary>

```text
# Ares Repository Analysis

Based on the provided web page content, I cannot extract the README details you've requested. The page shows only the GitHub repository structure and navigation elements, but **the actual README.md file content is not displayed** in the provided text.

## What I Can Confirm:
- **Repository**: UCSB-NLP-Chang/Ares
- **Project**: Official implementation for "Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents"
- **Status**: Minimal activity (0 stars, 0 forks, 1 commit)

## What Is Missing:
The following information you requested is **not present** in the provided content:
- Router model specifications (Qwen3-1.7B or similar)
- Training methodology (SFT details)
- Evaluation benchmarks
- Reasoning token reduction metrics
- Code availability details

**To obtain these details**, you would need to access the actual README.md file content by visiting the repository directly at `github.com/UCSB-NLP-Chang/Ares` and viewing the full README section, which appears to have a rendering issue on the provided screenshot.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7aa1dba9-3fec-4a74-9ca2-602b11a42bb9",
  "isSidechain": true,
  "promptId": "6bfca2c9-504d-4aa5-bfc1-591fd7535b04",
  "agentId": "aecf91e0f3be11219",
  "type": "user",
  "uuid": "66e70481-f66b-4e59-9a9b-cdb3702b8d1e",
  "sourceToolAssistantUUID": "7aa1dba9-3fec-4a74-9ca2-602b11a42bb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-11T23:32:09.947Z_

<details><summary>↩ Tool result · `toolu_011h778j9XvQcQ2nmHj2D41x`</summary>

```text
# Ares: Paper Extraction Summary

**Full Abstract:**
"Modern agents powered by thinking LLMs achieve high accuracy through long chain-of-thought reasoning but incur substantial inference costs. While many LLMs now support configurable reasoning levels (e.g., high/medium/low), static strategies are often ineffective: using low-effort modes at every step leads to significant performance degradation, while random selection fails to preserve accuracy or provide meaningful cost reduction. However, agents should reserve high reasoning effort for difficult steps like navigating complex website structures, while using lower-effort modes for simpler steps like opening a target URL. In this paper, we propose Ares, a framework for per-step dynamic reasoning effort selection tailored for multi-step agent tasks. Ares employs a lightweight router to predict the lowest appropriate reasoning level for each step based on the interaction history. To train this router, we develop a data generation pipeline that identifies the minimum reasoning effort required for successful step completion. We then fine-tune the router to predict these levels, enabling plug-and-play integration for any LLM agents."

**Authors:**
Jingbo Yang, Bairu Hou, Wei Wei, Yujia Bao, Shiyu Chang

**Submission Date:** March 9, 2026

**Router Model:** Not specified in the document

**Evaluation Benchmarks:** TAU-Bench, BrowseComp-Plus, WebArena

**Reasoning Token Reduction:** "up to 52.7% compared to fixed high-effort reasoning"

**Training Method:** Fine-tuning (specific approach called "SFT" not explicitly mentioned, but described as fine-tuning the router)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4940a54-b0f3-4830-a6c1-bdd01817d096",
  "isSidechain": true,
  "promptId": "6bfca2c9-504d-4aa5-bfc1-591fd7535b04",
  "agentId": "aecf91e0f3be11219",
  "type": "user",
  "uuid": "02f02a07-2f1d-4533-85e7-b5130aa804e1",
  "sourceToolAssistantUUID": "d4940a54-b0f3-4830-a6c1-bdd01817d096",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-11T23:32:13.405Z_

Let me fetch the HTML version of the paper for more details about the router model, and also try to access the README directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02f02a07-2f1d-4533-85e7-b5130aa804e1",
  "isSidechain": true,
  "agentId": "aecf91e0f3be11219",
  "requestId": "req_011Caweu17BUEUHkc7Ksarv8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c170f6a-5191-4f7b-a202-f3a512bf83e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013jqn8rzqtGe55VbGCzTtbG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 295,
      "cache_creation_input_tokens": 2419,
      "cache_read_input_tokens": 11916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2419,
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

_source line 19 · 2026-05-11T23:32:15.436Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HYwM3QEXqVA7yJRzfDqzEo`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.07915",
  "prompt": "Find any mention of the specific router model used (e.g., Qwen3-1.7B, Qwen, Llama, etc.). Also find mentions of SFT (supervised fine-tuning) as the training method. Look for specifics about the model architecture, size, and training approach. Also confirm the evaluation benchmarks and token reduction percentages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c170f6a-5191-4f7b-a202-f3a512bf83e8",
  "isSidechain": true,
  "agentId": "aecf91e0f3be11219",
  "requestId": "req_011Caweu17BUEUHkc7Ksarv8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cce6713f-17c8-462f-8895-e365f942866a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013jqn8rzqtGe55VbGCzTtbG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 295,
      "cache_creation_input_tokens": 2419,
      "cache_read_input_tokens": 11916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2419,
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

_source line 20 · 2026-05-11T23:32:16.626Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LJiQ1xSzmdFu8nnYz7juez`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/UCSB-NLP-Chang/Ares/main/README.md",
  "prompt": "Extract all content from this README file. Look for any mention of router model (Qwen3-1.7B), training method (SFT), benchmarks, and token reduction results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cce6713f-17c8-462f-8895-e365f942866a",
  "isSidechain": true,
  "agentId": "aecf91e0f3be11219",
  "requestId": "req_011Caweu17BUEUHkc7Ksarv8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f67ea96-efdc-45f4-b656-4bcf1bba4a26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013jqn8rzqtGe55VbGCzTtbG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 295,
      "cache_creation_input_tokens": 2419,
      "cache_read_input_tokens": 11916,
      "output_tokens": 306,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2419
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 295,
          "output_tokens": 306,
          "cache_read_input_tokens": 11916,
          "cache_creation_input_tokens": 2419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2419,
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

_source line 21 · 2026-05-11T23:32:19.628Z_

<details><summary>↩ Tool result · `toolu_01LJiQ1xSzmdFu8nnYz7juez`</summary>

```text
# Content Extraction from Ares README

Based on the provided web page content, the README file contains only a title and brief description:

**Available Information:**
- Project name: "Ares"
- Full title: "Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents"
- Designation: "Official implementation"

**Not Found in Provided Content:**
The excerpt does not include mentions of:
- Router model specifications (Qwen3-1.7B)
- Training methodologies (SFT)
- Benchmark results
- Token reduction metrics

The content supplied appears to be only the header section of the README file. To locate the technical details you're seeking regarding the router model, training approach, performance benchmarks, and efficiency gains, you would need access to the complete README documentation, which likely contains additional sections covering methodology, experimental results, and comparative analyses.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f67ea96-efdc-45f4-b656-4bcf1bba4a26",
  "isSidechain": true,
  "promptId": "6bfca2c9-504d-4aa5-bfc1-591fd7535b04",
  "agentId": "aecf91e0f3be11219",
  "type": "user",
  "uuid": "d96c9870-8d2e-4848-9433-0ba9b6a4bfd7",
  "sourceToolAssistantUUID": "5f67ea96-efdc-45f4-b656-4bcf1bba4a26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-11T23:32:21.810Z_

<details><summary>↩ Tool result · `toolu_01HYwM3QEXqVA7yJRzfDqzEo`</summary>

```text
# Ares: Adaptive Reasoning Effort Selection - Key Details

## Router Model
The paper explicitly states: "we fine-tune a lightweight Qwen3-1.7B model as the reasoning-effort router in Ares." This 1.7B parameter model serves as the core component for predicting reasoning effort levels.

## Training Methodology
Ares employs a two-stage training approach:

1. **Supervised Fine-tuning (SFT)**: "we fine-tune the router to predict these effort levels by minimizing the next-token prediction loss." The SFT phase uses a curated dataset with labeled minimum reasoning efforts for each step.

2. **Reinforcement Learning**: The paper notes that "we further explore training via reinforcement learning (RL)" using Group Relative Policy Optimization (GRPO) to optimize beyond greedy step-wise decisions.

## Evaluation Results
Across three diverse benchmarks, Ares demonstrates substantial efficiency gains:

- **TAU-Bench (Retail)**: 35.2% reduction in total reasoning tokens
- **BrowseComp-Plus**: 41.8% token reduction  
- **WebArena**: 45.3% token reduction

Most impressively, "Ares reduces reasoning token usage by up to 52.7% compared to fixed high-effort reasoning" on TAU-Bench while maintaining or improving task success rates.

## Tested Environments
The framework was evaluated on tool-use agents, deep-research agents, and web navigation tasks—demonstrating broad applicability across agent types.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cce6713f-17c8-462f-8895-e365f942866a",
  "isSidechain": true,
  "promptId": "6bfca2c9-504d-4aa5-bfc1-591fd7535b04",
  "agentId": "aecf91e0f3be11219",
  "type": "user",
  "uuid": "8d55dd39-66e1-4561-a39e-2bf7800df762",
  "sourceToolAssistantUUID": "cce6713f-17c8-462f-8895-e365f942866a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-11T23:32:35.895Z_

I now have comprehensive information to verify all five claims. Here is my report:

---

## Verification Results for "ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents"

### 1. Does this paper exist on arXiv with ID 2603.07915?

**VERIFIED - YES.** The paper exists at [arxiv.org/abs/2603.07915](https://arxiv.org/abs/2603.07915). It was submitted on March 9, 2026, by authors Jingbo Yang, Bairu Hou, Wei Wei, Yujia Bao, and Shiyu Chang.

### 2. Does it use a Qwen3-1.7B router trained via SFT?

**VERIFIED - YES.** The paper explicitly states they "fine-tune a lightweight Qwen3-1.7B model as the reasoning-effort router in Ares." The training method is Supervised Fine-tuning (SFT), minimizing next-token prediction loss. The paper also explores a second stage using reinforcement learning (GRPO), but SFT is the primary training method.

### 3. Does it achieve 52.7% reasoning token reduction?

**VERIFIED - YES.** The paper reports "Ares reduces reasoning token usage by up to 52.7% compared to fixed high-effort reasoning." This peak reduction is achieved on TAU-Bench. Other benchmarks show lower but still significant reductions (35.2% on TAU-Bench Retail, 41.8% on BrowseComp-Plus, 45.3% on WebArena).

### 4. Is it evaluated on WebArena/TAU-Bench?

**VERIFIED - YES.** The paper evaluates on three benchmarks:
- TAU-Bench (tool-use agents)
- WebArena (web navigation agents)
- BrowseComp-Plus (deep-research agents)

### 5. Is code available at github.com/UCSB-NLP-Chang/Ares?

**VERIFIED - YES.** The repository exists at [github.com/UCSB-NLP-Chang/Ares](https://github.com/UCSB-NLP-Chang/Ares) and is described as the "Official implementation for Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents." However, the repository appears to be in an early/minimal state (0 stars, 0 forks, 1 commit at time of check), and the README contains only a title and brief description without detailed documentation or usage instructions.

---

**Summary:** All five claims are verified as accurate based on web search and direct page fetches from arXiv and GitHub.

Sources:
- [arXiv Abstract Page](https://arxiv.org/abs/2603.07915)
- [arXiv HTML Full Paper](https://arxiv.org/html/2603.07915)
- [GitHub Repository](https://github.com/UCSB-NLP-Chang/Ares)
- [AI Models Paper Summary](https://www.aimodels.fyi/papers/arxiv/ares-adaptive-reasoning-effort-selection-efficient-llm)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d55dd39-66e1-4561-a39e-2bf7800df762",
  "isSidechain": true,
  "agentId": "aecf91e0f3be11219",
  "requestId": "req_011CaweusjhS3umUMVa7SAx7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7d6918a1-bda3-49b0-be90-fd3033e68541",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f8fc318-c0c6-4f9a-a2b9-50e9e2b4edd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HctdUixyZgAhY22orHbuyV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 228,
      "cache_creation_input_tokens": 1086,
      "cache_read_input_tokens": 14335,
      "output_tokens": 759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1086
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 228,
          "output_tokens": 759,
          "cache_read_input_tokens": 14335,
          "cache_creation_input_tokens": 1086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1086,
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
