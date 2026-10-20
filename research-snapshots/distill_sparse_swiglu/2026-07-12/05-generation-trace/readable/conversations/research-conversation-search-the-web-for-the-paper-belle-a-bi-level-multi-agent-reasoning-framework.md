# Research conversation: Search the web for the paper "BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering" (arxiv

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a7605e06f39e9a077.jsonl`
- **Structured JSON:** [`4a721ea094fc94c729be.json`](../../sessions/4a/4a721ea094fc94c729be.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

33 recorded events

### User

_source line 1 · 2026-05-14T16:58:25.613Z_

Search the web for the paper "BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering" (arxiv 2505.11811, claimed ACL 2025). I need to verify:
1. Does this paper exist? What venue was it actually published at?
2. What exactly does it do? Does it classify question types and assign reasoning operators per type?
3. What datasets does it evaluate on?
4. What are its key results (specific F1 numbers)?
5. Does it use BM25 retrieval as claimed?

Use WebSearch and WebFetch to find and read the paper. Report specific details, not vague summaries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "a7605e06f39e9a077",
  "type": "user",
  "uuid": "2257bff3-28f8-4c5c-96df-ea4fde70e510",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T16:58:25.617Z_

```json
{
  "parentUuid": "2257bff3-28f8-4c5c-96df-ea4fde70e510",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
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
  "uuid": "f476bf22-ab51-4243-857f-11ee81661d75",
  "timestamp": "2026-05-14T16:58:25.617Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T16:58:28.160Z_



I'll search for this paper and verify the claims. Let me start by loading the necessary tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f476bf22-ab51-4243-857f-11ee81661d75",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pJJ95NrMXMeezya6wD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3815db22-0989-41a8-b320-f780d2dc0d8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYezAaKtsU6MXhMdd1kt8p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 697,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 4 · 2026-05-14T16:58:28.563Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UpGmJNXWCm9NJRzh4m2Ms2`</summary>

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
  "parentUuid": "3815db22-0989-41a8-b320-f780d2dc0d8d",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pJJ95NrMXMeezya6wD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cddf7209-67f9-4fa8-9428-9330a1b8d31d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYezAaKtsU6MXhMdd1kt8p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 8223,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 697
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 697,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 697,
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

_source line 5 · 2026-05-14T16:58:28.567Z_

<details><summary>↩ Tool result · `toolu_01UpGmJNXWCm9NJRzh4m2Ms2`</summary>

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
  "parentUuid": "cddf7209-67f9-4fa8-9428-9330a1b8d31d",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "a7605e06f39e9a077",
  "type": "user",
  "uuid": "2ea792ed-1baf-409c-a275-876ee53d5599",
  "sourceToolAssistantUUID": "cddf7209-67f9-4fa8-9428-9330a1b8d31d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T16:58:30.910Z_



Now let me search for this paper from multiple angles.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ea792ed-1baf-409c-a275-876ee53d5599",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pJX4TSUCzsvdDcAfbU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bbbbb31-4d4f-437a-982c-62b0a954c94e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1uYwPxBamtwdg4HeRSYD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 7 · 2026-05-14T16:58:31.397Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HumDErDRqpXdK1wqssdrFM`</summary>

```json
{
  "query": "BELLE Bi-Level Multi-Agent Reasoning Framework Multi-Hop Question Answering arxiv 2505.11811"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3bbbbb31-4d4f-437a-982c-62b0a954c94e",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pJX4TSUCzsvdDcAfbU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de631dd8-e120-48d2-8052-e30cfd847cf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1uYwPxBamtwdg4HeRSYD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 8 · 2026-05-14T16:58:32.273Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011crB9B2dBD4vadEynjGnQi`</summary>

```json
{
  "query": "\"BELLE\" \"multi-hop question answering\" \"bi-level\" ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de631dd8-e120-48d2-8052-e30cfd847cf0",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pJX4TSUCzsvdDcAfbU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15481789-f641-43ac-8c77-9b41803d2152",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1uYwPxBamtwdg4HeRSYD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 9 · 2026-05-14T16:58:32.278Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PCJX1AtXevwJ4bC4njBWr6`</summary>

```json
{
  "query": "arxiv 2505.11811"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15481789-f641-43ac-8c77-9b41803d2152",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pJX4TSUCzsvdDcAfbU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "515f87e8-0fcf-47f3-8752-bf269b8dd412",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1uYwPxBamtwdg4HeRSYD7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 10 · 2026-05-14T16:58:37.694Z_

<details><summary>↩ Tool result · `toolu_01PCJX1AtXevwJ4bC4njBWr6`</summary>

```text
Web search results for query: "arxiv 2505.11811"

Links: [{"title":"[2505.11811] BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering","url":"https://arxiv.org/abs/2505.11811"},{"title":"BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering","url":"https://arxiv.org/html/2505.11811"},{"title":"[2511.11811] Lessons Learned from Developing a Privacy-Preserving Multimodal Wearable for Local Voice-and-Vision Inference","url":"https://arxiv.org/abs/2511.11811"},{"title":"[2502.11811] Less is More: Compact Clue Selection for Efficient Retrieval-Augmented Generation Reasoning","url":"https://arxiv.org/abs/2502.11811"},{"title":"Artificial Intelligence May 2025","url":"https://www.arxiv.org/list/cs.AI/2025-05?skip=2975&show=50"},{"title":"Computer Science May 2025","url":"https://www.arxiv.org/list/cs/2025-05?skip=4075&show=500"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2408.11811"},{"title":"RepLiQA: A Question-Answering Dataset for Benchmarking LLMs on Unseen Reference Content","url":"https://arxiv.org/html/2406.11811"},{"title":"[2507.11811] Observation and Interpretation of Field Emission Saturation Induced by an Ultra-fast Intense Terahertz Field","url":"https://arxiv.org/abs/2507.11811"},{"title":"Prepared for submission to JHEP YITP-25-42, KUNS-3051","url":"https://arxiv.org/pdf/2505.16546"}]

Based on the search results, I found the paper you're looking for:

**BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering**

Multi-hop question answering (QA) involves finding multiple relevant passages and performing step-by-step reasoning to answer complex questions. The paper conducts an in-depth analysis of public multi-hop QA benchmarks, dividing the questions into four types and evaluating five types of cutting-edge methods for multi-hop QA: Chain-of-Thought (CoT), Single-step, Iterative-step, Sub-step, and Adaptive-step. 

The researchers find that different types of multi-hop questions have varying degrees of sensitivity to different types of methods. They propose the BELLE framework to address multi-hop QA by specifically focusing on the correspondence between question types and methods, where each type of method is regarded as an "operator" by prompting LLMs differently.

The paper was submitted on May 17, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "515f87e8-0fcf-47f3-8752-bf269b8dd412",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "a7605e06f39e9a077",
  "type": "user",
  "uuid": "e09b2c2f-548a-4e59-b64d-1690ea32f691",
  "sourceToolAssistantUUID": "515f87e8-0fcf-47f3-8752-bf269b8dd412",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T16:58:38.609Z_

<details><summary>↩ Tool result · `toolu_011crB9B2dBD4vadEynjGnQi`</summary>

```text
Web search results for query: ""BELLE" "multi-hop question answering" "bi-level" ACL 2025"

Links: [{"title":"BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.211/"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"[논문리뷰]BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering(ACL, 2025) - Meaningful AI","url":"https://meaningful96.github.io/nr/belle/"},{"title":"[2505.11811] BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering","url":"https://arxiv.org/abs/2505.11811"},{"title":"BELLE: A Bi-Level Multi-Agent Reasoning Framework for ...","url":"https://aclanthology.org/2025.acl-long.211.pdf"},{"title":"BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering - East China Normal University","url":"https://pure.ecnu.edu.cn/en/publications/belle-a-bi-level-multi-agent-reasoning-framework-for-multi-hop-qu/"},{"title":"Dongyang Li - ACL Anthology","url":"https://aclanthology.org/people/dongyang-li/"},{"title":"(PDF) BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering","url":"https://www.researchgate.net/publication/391878416_BELLE_A_Bi-Level_Multi-Agent_Reasoning_Framework_for_Multi-Hop_Question_Answering"},{"title":"Qizhou Chen - ACL Anthology","url":"https://aclanthology.org/people/qizhou-chen/"},{"title":"[PDF] BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BELLE:-A-Bi-Level-Multi-Agent-Reasoning-Framework-Zhang-Li/4e826915ce02cb2f523dc0b08e5badac6f48ed84"}]

I found the paper! Here are the search results for BELLE:

## BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering

BELLE is a paper titled "A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering" published in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) in Vienna, Austria.

**Authors:** Taolin Zhang, Dongyang Li, Qizhou Chen, Chengyu Wang, and Xiaofeng He

**Core Contribution:**

The BELLE framework addresses multi-hop QA by specifically focusing on the correspondence between question types and methods, where each type of method is regarded as an "operator" by prompting LLMs differently.

**Framework Structure:**

The first level of BELLE includes multiple agents that debate to obtain an executive plan of combined "operators" to address the multi-hop QA task comprehensively. During the debate, in addition to the basic roles of affirmative debater, negative debater, and judge, at the second level, the framework further leverages fast and slow debaters to monitor whether changes in viewpoints are reasonable.

**Results:**

Extensive experiments demonstrate that BELLE significantly outperforms strong baselines in various datasets. Additionally, the model consumption of BELLE is higher cost-effectiveness than that of single models in more complex multi-hop QA scenarios.

You can access the full paper at the ACL Anthology: https://aclanthology.org/2025.acl-long.211/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15481789-f641-43ac-8c77-9b41803d2152",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "a7605e06f39e9a077",
  "type": "user",
  "uuid": "02dfc221-f549-4750-b516-2a57e6ebf429",
  "sourceToolAssistantUUID": "15481789-f641-43ac-8c77-9b41803d2152",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T16:58:39.270Z_

<details><summary>↩ Tool result · `toolu_01HumDErDRqpXdK1wqssdrFM`</summary>

```text
Web search results for query: "BELLE Bi-Level Multi-Agent Reasoning Framework Multi-Hop Question Answering arxiv 2505.11811"

Links: [{"title":"[2505.11811] BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering","url":"https://arxiv.org/abs/2505.11811"},{"title":"BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering","url":"https://arxiv.org/html/2505.11811"},{"title":"[PDF] BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BELLE:-A-Bi-Level-Multi-Agent-Reasoning-Framework-Zhang-Li/4e826915ce02cb2f523dc0b08e5badac6f48ed84"},{"title":"(PDF) BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering","url":"https://www.researchgate.net/publication/391878416_BELLE_A_Bi-Level_Multi-Agent_Reasoning_Framework_for_Multi-Hop_Question_Answering"},{"title":"BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering - East China Normal University","url":"https://pure.ecnu.edu.cn/en/publications/belle-a-bi-level-multi-agent-reasoning-framework-for-multi-hop-qu/"},{"title":"BELLE: A Bi-Level Multi-Agent Reasoning Framework for ...","url":"https://aclanthology.org/2025.acl-long.211.pdf"},{"title":"BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.211/"},{"title":"[논문리뷰]BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering(ACL, 2025) - Meaningful AI","url":"https://meaningful96.github.io/nr/belle/"},{"title":"BELLE: A Bi-Level Multi-Agent Reasoning Framework ...","url":"https://eurekamag.com/research/100/126/100126422.php"},{"title":"Computation and Language May 2025","url":"https://www.arxiv.org/list/cs.CL/2025-05?skip=525&show=25"}]

I found the paper! Here's information about BELLE (arxiv 2505.11811):

## Paper Overview

Multi-hop question answering (QA) involves finding multiple relevant passages and performing step-by-step reasoning to answer complex questions.

## The BELLE Framework

The BELLE framework addresses multi-hop QA by specifically focusing on the correspondence between question types and methods, where each type of method is regarded as an 'operator' by prompting LLMs differently.

## Key Research Findings

The authors conduct an in-depth analysis of public multi-hop QA benchmarks, dividing the questions into four types and evaluating five types of cutting-edge methods for multi-hop QA: Chain-of-Thought (CoT), Single-step, Iterative-step, Sub-step, and Adaptive-step. They find that different types of multi-hop questions have varying degrees of sensitivity to different types of methods.

## Framework Architecture

The first level of BELLE includes multiple agents that debate to obtain an executive plan of combined 'operators' to address the multi-hop QA task comprehensively. During the debate, in addition to the basic roles of affirmative debater, negative debater, and judge, at the second level, the framework further leverages fast and slow debaters to monitor whether changes in viewpoints are reasonable.

## Results

Extensive experiments demonstrate that BELLE significantly outperforms strong baselines in various datasets, and the model consumption of BELLE is higher cost-effectiveness than that of single models in more complex multi-hop QA scenarios.

## Publication

The paper was accepted by ACL 2025 main track.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de631dd8-e120-48d2-8052-e30cfd847cf0",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "a7605e06f39e9a077",
  "type": "user",
  "uuid": "9e0e74c2-2db9-4033-8ead-363680649059",
  "sourceToolAssistantUUID": "de631dd8-e120-48d2-8052-e30cfd847cf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-14T16:58:43.171Z_

The paper exists. Now let me fetch the actual paper content from arxiv and the ACL Anthology to get specific details about datasets, results, and methods.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e0e74c2-2db9-4033-8ead-363680649059",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pKJZQBYXNj155rqvKq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72425b74-0139-4381-917f-9cdd5b063575",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZRhhiirfbi2TnqS4P8ALN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1763,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 10830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1237,
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

_source line 14 · 2026-05-14T16:58:44.999Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019ma3UpWTttZrReuv4bd1JQ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.11811",
  "prompt": "Extract the full abstract, list of authors, submission/publication dates, and any venue information (ACL 2025, etc.). Also extract any mentions of datasets, methods (especially BM25 retrieval), question types, and specific F1 scores or numerical results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72425b74-0139-4381-917f-9cdd5b063575",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pKJZQBYXNj155rqvKq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4761c3c9-7539-4162-b7a0-3d34d16e609d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZRhhiirfbi2TnqS4P8ALN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1763,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 10830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1237,
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

_source line 15 · 2026-05-14T16:58:45.930Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BeRQahApWhdBAVH6jiLhwn`</summary>

```json
{
  "url": "https://aclanthology.org/2025.acl-long.211/",
  "prompt": "Extract all details: authors, venue, abstract, and any available information about the paper's content, datasets, results, and methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4761c3c9-7539-4162-b7a0-3d34d16e609d",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pKJZQBYXNj155rqvKq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bdf11b0-4871-438c-9d40-1ae36ca2b5a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZRhhiirfbi2TnqS4P8ALN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1763,
      "cache_creation_input_tokens": 1237,
      "cache_read_input_tokens": 10830,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1237
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1763,
          "output_tokens": 268,
          "cache_read_input_tokens": 10830,
          "cache_creation_input_tokens": 1237,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1237,
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

_source line 16 · 2026-05-14T16:58:50.708Z_

<details><summary>↩ Tool result · `toolu_01BeRQahApWhdBAVH6jiLhwn`</summary>

```text
# BELLE: Multi-Hop Question Answering Framework

## Authors
Taolin Zhang, Dongyang Li, Qizhou Chen, Chengyu Wang, Xiaofeng He

## Venue
ACL 2025 (63rd Annual Meeting of the Association for Computational Linguistics)
- **Location:** Vienna, Austria
- **Volume:** Proceedings Volume 1: Long Papers
- **Pages:** 4184–4202
- **Month:** July 2025

## Core Research Problem
The paper addresses multi-hop question answering, which involves "finding multiple relevant passages and performing step-by-step reasoning to answer complex questions."

## Key Innovation
BELLE is a bi-level multi-agent reasoning framework that matches different question types with appropriate reasoning methods. The authors identify that "different types of multi-hop questions have varying degrees of sensitivity to different types of methods."

## Methods Evaluated
The research examines five reasoning approaches:
- Chain-of-Thought (CoT)
- Single-step
- Iterative-step
- Sub-step
- Adaptive-step

## Framework Design
The framework operates on two levels:
1. **First level:** Multiple agents debate to determine an optimal combination of "operators" (different reasoning methods)
2. **Second level:** Fast and slow debaters monitor whether viewpoint changes remain reasonable

## Results
The framework demonstrates significant improvements over baselines across multiple datasets, with favorable cost-effectiveness compared to single-model approaches in complex scenarios.

## Citation
DOI: 10.18653/v1/2025.acl-long.211
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bdf11b0-4871-438c-9d40-1ae36ca2b5a4",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "a7605e06f39e9a077",
  "type": "user",
  "uuid": "ccfa7c62-d8b6-4e34-8598-88db04006e13",
  "sourceToolAssistantUUID": "2bdf11b0-4871-438c-9d40-1ae36ca2b5a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T16:58:52.777Z_

<details><summary>↩ Tool result · `toolu_019ma3UpWTttZrReuv4bd1JQ`</summary>

```text
# BELLE Paper Summary

## Full Abstract
"Multi-hop question answering (QA) involves finding multiple relevant passages and performing step-by-step reasoning to answer complex questions. Previous works on multi-hop QA employ specific methods from different modeling perspectives based on large language models (LLMs), regardless of the question types. In this paper, we first conduct an in-depth analysis of public multi-hop QA benchmarks, dividing the questions into four types and evaluating five types of cutting-edge methods for multi-hop QA: Chain-of-Thought (CoT), Single-step, Iterative-step, Sub-step, and Adaptive-step. We find that different types of multi-hop questions have varying degrees of sensitivity to different types of methods. Thus, we propose a Bi-levEL muLti-agEnt reasoning (BELLE) framework to address multi-hop QA by specifically focusing on the correspondence between question types and methods, where each type of method is regarded as an ''operator'' by prompting LLMs differently. The first level of BELLE includes multiple agents that debate to obtain an executive plan of combined ''operators'' to address the multi-hop QA task comprehensively. During the debate, in addition to the basic roles of affirmative debater, negative debater, and judge, at the second level, we further leverage fast and slow debaters to monitor whether changes in viewpoints are reasonable. Extensive experiments demonstrate that BELLE significantly outperforms strong baselines in various datasets. Additionally, the model consumption of BELLE is higher cost-effectiveness than that of single models in more complex multi-hop QA scenarios."

## Authors
Taolin Zhang, Dongyang Li, Qizhou Chen, Chengyu Wang, Xiaofeng He

## Dates
- **Submitted:** May 17, 2025
- **Venue:** Accepted by ACL 2025 main track

## Key Technical Details
- **Framework:** BELLE uses bi-level multi-agent reasoning with debate mechanisms
- **Methods Evaluated:** Chain-of-Thought, Single-step, Iterative-step, Sub-step, Adaptive-step
- **Agents:** Affirmative debater, negative debater, judge, fast debater, slow debater

**Note:** The provided content does not include specific datasets, F1 scores, or other numerical results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4761c3c9-7539-4162-b7a0-3d34d16e609d",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "a7605e06f39e9a077",
  "type": "user",
  "uuid": "317c0aee-c3f0-4a74-8e9d-4b9a69f271dd",
  "sourceToolAssistantUUID": "4761c3c9-7539-4162-b7a0-3d34d16e609d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-14T16:58:56.159Z_

Good, I have the abstract-level details confirmed. Now let me fetch the full HTML version of the paper to get specific datasets, F1 numbers, question types, and whether BM25 is used.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "317c0aee-c3f0-4a74-8e9d-4b9a69f271dd",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pLJGKViXWmwZeEi34g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ee7a621-9f37-48c4-85b7-9fc820c54d91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013knDQY2pqYhM9ZqZDmrRFU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 387,
      "cache_creation_input_tokens": 2586,
      "cache_read_input_tokens": 12067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2586,
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

_source line 19 · 2026-05-14T16:59:01.443Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Jv5FaBsLwuHEHasiVYUm6J`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.11811",
  "prompt": "I need very specific details from this paper. Extract:\n\n1. The FOUR question types they identify - what are they called?\n2. The FIVE operator/method types - exact names and what each does\n3. ALL datasets used for evaluation - exact names (HotpotQA, MuSiQue, 2WikiMultiHopQA, etc.)\n4. ALL specific F1 scores and EM (exact match) numbers from the results tables - include the baseline numbers and BELLE's numbers\n5. Any mention of BM25 retrieval - do they use BM25 for passage retrieval? How?\n6. The retrieval setup - what retriever do they use, how many passages, what corpus?\n7. The LLM backbone - what model(s) do they use (GPT-4, GPT-3.5, etc.)?\n\nBe as specific and numerical as possible. Copy exact numbers from tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ee7a621-9f37-48c4-85b7-9fc820c54d91",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pLJGKViXWmwZeEi34g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0024bfc2-6d4f-4e5d-a571-508e7e678959",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013knDQY2pqYhM9ZqZDmrRFU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 387,
      "cache_creation_input_tokens": 2586,
      "cache_read_input_tokens": 12067,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2586
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 387,
          "output_tokens": 336,
          "cache_read_input_tokens": 12067,
          "cache_creation_input_tokens": 2586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2586,
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

_source line 20 · 2026-05-14T16:59:13.255Z_

<details><summary>↩ Tool result · `toolu_01Jv5FaBsLwuHEHasiVYUm6J`</summary>

```text
# BELLE Framework: Specific Details Extraction

## 1. Four Question Types
The paper identifies these multi-hop question categories:
- **Inference**: Requires logical connections through intermediate entities
- **Comparison**: Compares similarities/differences between entities
- **Temporal**: Based on event sequences at different time points
- **Null**: Questions unanswerable from retrieved documents or free-form queries

## 2. Five Operator/Method Types
- **CoT** (Chain-of-Thought): "generates logic reasoning steps before the final answer"
- **Single-step**: One-time retrieval using the full question as query
- **Iterative-step**: Multi-round retrieval concatenating previous outputs with sub-questions
- **Sub-step**: Decomposes complex questions into sub-questions progressively
- **Adaptive-step**: Uses classifiers for different question types with fixed approach

## 3. Datasets Used
- MultiHop-RAG
- HotPotQA
- 2WikiMultiHopQA
- MuSiQue

## 4. F1 and EM Scores

**Main Results (Table 1, GPT-3.5-turbo):**

| Dataset | BELLE EM | BELLE F1 | BeamAggR EM | BeamAggR F1 |
|---------|----------|----------|-------------|------------|
| Multi-hop RAG | 64.7 | 70.4 | 61.9 | 67.2 |
| HotpotQA | 59.2 | 66.5 | 55.6 | 62.9 |
| 2WikiQA | 69.7 | 75.7 | 66.1 | 71.6 |
| MuSiQue 2-hop | 50.5 | 42.1 | 45.9 | 36.8 |
| MuSiQue 3-hop | — | 29.2 | — | 21.6 |
| MuSiQue 4-hop | — | 7.6 | — | 1.6 |

## 5. BM25 Retrieval Usage
Yes, they employ BM25: "we use the sparse model BM25...to replace the complex models." This provides "cost-effective retrieval" for passage selection.

## 6. Retrieval Setup
- **Corpus**: October 2017 Wikipedia dumps
- **Retriever**: BM25 sparse model (can be replaced with neural alternatives)
- **Passages per query**: 3-10 candidate documents per dataset
- **Replacement note**: "The retriever can be replaced by other high-precision neural models"

## 7. LLM Backbone Models
- Primary: GPT-3.5-turbo (Azure OpenAI 2024-01-25 version)
- Secondary: GPT-4 (Azure OpenAI 2024-06-13, used for annotation)
- Open-source alternatives tested: Qwen2.5-7B, Mistral-7B
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0024bfc2-6d4f-4e5d-a571-508e7e678959",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "a7605e06f39e9a077",
  "type": "user",
  "uuid": "034f73f7-db35-4d62-9a23-7c37dc560b76",
  "sourceToolAssistantUUID": "0024bfc2-6d4f-4e5d-a571-508e7e678959",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-14T16:59:16.152Z_

Excellent, very detailed. Let me get even more specifics on the results and baselines by fetching the PDF directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "034f73f7-db35-4d62-9a23-7c37dc560b76",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pMos5QQShgH9WVpMp4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af6df279-1b50-43fc-b4b5-436f521f3ae0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QEwMSfmfrrYDTDNqbjByx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1468,
      "cache_read_input_tokens": 14653,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1468,
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

_source line 22 · 2026-05-14T16:59:21.752Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VXGQTMfbKBeDQTCp1aMcki`</summary>

```json
{
  "url": "https://aclanthology.org/2025.acl-long.211.pdf",
  "prompt": "Extract ALL numerical results from the experimental tables. I need:\n\n1. Complete Table 1 or main results table: ALL rows (all baselines and BELLE), ALL columns (EM, F1 for each dataset). Include baselines like IRCoT, Self-Ask, ReAct, BeamAggR, DSP, etc.\n2. Any ablation study results\n3. Any results with GPT-4 vs GPT-3.5\n4. Any results comparing open-source models (Qwen, Mistral)\n5. The exact question type classification details - how many types, how they classify\n6. Whether BM25 is the default retriever or if they also test with dense retrievers like Contriever or ColBERT\n7. Any cost analysis numbers (token usage, API costs)\n\nCopy the exact numbers. Do not approximate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af6df279-1b50-43fc-b4b5-436f521f3ae0",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pMos5QQShgH9WVpMp4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e143599-8a08-417c-aa0b-186609dc93d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018QEwMSfmfrrYDTDNqbjByx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1468,
      "cache_read_input_tokens": 14653,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1468
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 307,
          "cache_read_input_tokens": 14653,
          "cache_creation_input_tokens": 1468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1468,
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

_source line 23 · 2026-05-14T16:59:28.364Z_

<details><summary>↩ Tool result · `toolu_01VXGQTMfbKBeDQTCp1aMcki`</summary>

```text
I apologize, but I cannot extract the numerical results you're requesting from the provided content. The text appears to be a PDF document encoded in binary/compressed format (with markers like `%PDF-1.5`, `FlateDecode`, etc.), which renders as unreadable encoded streams rather than displayable text.

To help you effectively, I would need:

1. **Plain text or properly formatted content** - The current format is a PDF binary stream that cannot be parsed for specific data tables
2. **Direct access to the paper's tables** - Either as extracted text, a CSV file, or clearer image descriptions

**What I can suggest:**

- Try converting the PDF to text using tools like `pdftotext` or online PDF converters
- Check if the paper is available on arXiv or the publisher's website in a more accessible format
- If you can copy-paste the actual table content from the PDF, I can extract the exact numbers you need

Once you provide the data in readable format, I can deliver:
- Complete Table 1 with all baseline comparisons
- Ablation study results
- GPT-4 vs GPT-3.5 comparisons
- Open-source model results
- Question classification details
- Retriever specifications (BM25 vs dense retrievers)
- Cost analysis metrics

Please reformat the source material and resubmit.

[Binary content (application/pdf, 2.4MB) also saved to /home/ubuntu/.claude-account-2/projects/-/dc0000b1-7eb7-408f-93e5-2e48a2af8809/tool-results/webfetch-1778777963722-l86iev.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e143599-8a08-417c-aa0b-186609dc93d2",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "a7605e06f39e9a077",
  "type": "user",
  "uuid": "d07e24a8-4fe5-4746-9abd-b57a1be2165c",
  "sourceToolAssistantUUID": "3e143599-8a08-417c-aa0b-186609dc93d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-14T16:59:31.114Z_

The PDF is binary. Let me try the HTML version more carefully and also check for a Semantic Scholar page that might have extracted results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d07e24a8-4fe5-4746-9abd-b57a1be2165c",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pNvQW8BXNW2VhkoApZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aeb484ec-f2d3-41a0-a8ba-786ab6dcfcbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185KEhY1PgkgkLfNBCfhLrW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 16121,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 701,
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

_source line 25 · 2026-05-14T16:59:35.161Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NF4rXMua5J5VNXPo8smqv6`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.11811",
  "prompt": "Focus ONLY on the experimental results section and tables. I need every single number from the results tables. Look for:\n\n1. Table 1 or the main comparison table - list EVERY baseline method name and their EM/F1 scores on each dataset\n2. Baselines should include methods like: IO prompting, CoT, Self-Ask, IRCoT, ReAct, DSP, BeamAggR, ITER-RETGEN, etc.\n3. For each dataset (MultiHop-RAG, HotpotQA, 2WikiMultiHopQA, MuSiQue), give me ALL numbers\n4. Any table about ablation studies\n5. Any table about different LLM backbones\n\nCopy numbers EXACTLY as they appear. Format as tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aeb484ec-f2d3-41a0-a8ba-786ab6dcfcbb",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pNvQW8BXNW2VhkoApZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d56118be-e277-4b06-80b5-4fd1a4bb1468",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0185KEhY1PgkgkLfNBCfhLrW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 701,
      "cache_read_input_tokens": 16121,
      "output_tokens": 290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 701
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 290,
          "cache_read_input_tokens": 16121,
          "cache_creation_input_tokens": 701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 701,
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

_source line 26 · 2026-05-14T16:59:50.738Z_

<details><summary>↩ Tool result · `toolu_01NF4rXMua5J5VNXPo8smqv6`</summary>

```text
# Experimental Results from BELLE Paper

## Table 1: Main Results Across All Datasets

| Model | Multi-hop RAG |  | HotpotQA |  | 2WikiQA |  | MuSiQue |  |  |
|-------|---|---|---|---|---|---|---|---|---|
| | EM | F1 | EM | F1 | EM | F1 | 2hop | 3hop | 4hop |
| **Closed-book** |
| SP | 39.4 | 47.5 | 32.1 | 38.9 | 27.8 | 33.9 | 16.4 | 16.2 | 12.6 |
| CoT | 43.6 | 50.5 | 40.5 | 46.5 | 36.2 | 42.3 | 30.2 | 22.5 | 13.2 |
| **Retrieval-augmented** |
| Single-step | 47.2 | 52.3 | 48.7 | 55.3 | 38.1 | 42.9 | 22.1 | 10.6 | 10.4 |
| Self-Ask | 49.8 | 54.6 | 44.5 | 49.4 | 40.5 | 46.9 | 24.4 | 8.8 | 7.5 |
| IRCoT | 55.1 | 59.2 | 51.2 | 56.2 | 50.7 | 56.8 | 31.4 | 19.2 | 16.4 |
| FLARE | 54.9 | 58.7 | 50.8 | 56.1 | 58.2 | 60.1 | 40.9 | 27.1 | 15.0 |
| ProbTree | 56.5 | 62.5 | 56.3 | 60.4 | 64.3 | 67.9 | 41.2 | 30.9 | 14.4 |
| EfficientRAG | 49.2 | 55.3 | 52.9 | 57.9 | 47.7 | 51.6 | 32.7 | 23.6 | 12.5 |
| BeamAggR | 61.9 | 67.2 | 55.6 | 62.9 | 66.1 | 71.6 | 45.9 | 36.8 | 21.6 |
| **Agent-based** |
| LONGAGENT | 53.6 | 56.8 | 52.4 | 59.3 | 60.1 | 65.6 | 40.5 | 25.8 | 16.4 |
| GEAR | 50.7 | 52.5 | 50.4 | 54.6 | 47.4 | 52.3 | 35.1 | 20.9 | 15.3 |
| RopMura | 52.6 | 53.7 | 49.2 | 53.1 | 58.8 | 63.2 | 41.1 | 24.6 | 16.2 |
| **BELLE** | **64.7** | **70.4** | **59.2** | **66.5** | **69.7** | **75.7** | **50.5** | **42.1** | **29.2** |

## Table 2: Ablation Study (F1 Scores)

| Component Removed | Multi-hop RAG | HotpotQA | 2WikiQA | MuSiQue | Avg |
|---|---|---|---|---|---|
| **Qwen2.5-7B** |
| Full BELLE | 64.1 | 59.4 | 68.5 | 32.8 | 56.2 |
| w/o Type Classifier | 59.6 | 54.1 | 63.5 | 25.9 | 50.8 |
| w/o First Level Debate | 61.2 | 55.4 | 64.6 | 28.9 | 52.5 |
| w/o Second Level Debate | 58.8 | 53.5 | 62.1 | 25.4 | 50.0 |
| **GPT-3.5-turbo** |
| Full BELLE | 70.4 | 66.5 | 75.7 | 40.6 | 63.3 |
| w/o Type Classifier | 67.9 | 63.4 | 73.2 | 37.6 | 60.5 |
| w/o First Level Debate | 68.2 | 63.7 | 73.5 | 38.1 | 60.9 |
| w/o Second Level Debate | 66.8 | 62.8 | 72.3 | 36.5 | 59.6 |
| w/o Affir.&Neg. Debater | 68.4 | 64.1 | 73.9 | 38.5 | 61.2 |
| w/o Fast Debater | 67.3 | 63.2 | 72.9 | 37.4 | 60.2 |
| w/o Slow Debater | 67.0 | 63.1 | 72.7 | 36.9 | 59.9 |

## Table 6: Different LLM Backbones (F1 Scores)

| Model | Multi-hop RAG | HotpotQA | 2WikiQA | MuSiQue Avg | Overall Avg |
|---|---|---|---|---|---|
| **Qwen2.5-7B** |
| CoT | 24.9 | 22.5 | 19.9 | 11.8 | 19.8 |
| ProbTree | 50.7 | 47.1 | 55.6 | 17.3 | 42.7 |
| BeamAggR | 55.8 | 51.8 | 62.4 | 23.2 | 48.3 |
| BELLE | 64.1 | 59.4 | 68.5 | 32.8 | 56.2 |
| **Mistral-7B** |
| CoT | 26.3 | 25.1 | 19.2 | 10.6 | 20.3 |
| ProbTree | 51.4 | 48.7 | 53.8 | 16.9 | 42.7 |
| BeamAggR | 56.6 | 54.3 | 59.9 | 22.7 | 48.4 |
| BELLE | 65.8 | 61.3 | 64.4 | 29.7 | 55.3 |
| **GPT-4** |
| CoT | 51.8 | 47.2 | 44.9 | 24.6 | 42.1 |
| ProbTree | 62.8 | 61.5 | 68.3 | 30.5 | 55.8 |
| BeamAggR | 67.6 | 63.4 | 72.7 | 36.2 | 60.0 |
| BELLE | 71.3 | 66.9 | 75.3 | 41.3 | 63.7 |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d56118be-e277-4b06-80b5-4fd1a4bb1468",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "a7605e06f39e9a077",
  "type": "user",
  "uuid": "28213bae-3798-437d-b7a8-74d968022225",
  "sourceToolAssistantUUID": "d56118be-e277-4b06-80b5-4fd1a4bb1468",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-14T16:59:54.154Z_

This is very detailed. Let me also get the specifics on the question type classification and BM25 retrieval setup.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28213bae-3798-437d-b7a8-74d968022225",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pQa5C9CAuLZzXuWZuu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be4639e1-173b-43fc-a4df-6d388e9fcbda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjjeTeDbZ18yPr8neXsZko",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2279,
      "cache_read_input_tokens": 16822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2279,
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

_source line 28 · 2026-05-14T16:59:59.022Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DKssh7CogJgd8eACjHdiKc`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.11811",
  "prompt": "Focus on these specific sections:\n\n1. QUESTION TYPE CLASSIFICATION: How exactly do they classify questions into the 4 types (Inference, Comparison, Temporal, Null)? Is it rule-based, LLM-based, or trained classifier? What percentage of questions fall into each type?\n\n2. BM25 RETRIEVAL: Find every mention of BM25. How is it used? Is it the default retriever? What parameters? Do they compare against dense retrievers? What retrieval results do they report?\n\n3. OPERATOR ASSIGNMENT: How does the framework decide which operator(s) to use for a given question? Is it the debate that decides, or is there a classifier?\n\n4. COST ANALYSIS: Any token usage or cost numbers comparing BELLE to baselines.\n\n5. The DEBATE MECHANISM: How exactly does the bi-level debate work? What are the fast and slow debaters?\n\nBe very specific and quote from the paper where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be4639e1-173b-43fc-a4df-6d388e9fcbda",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pQa5C9CAuLZzXuWZuu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5cdeee6-4d40-4a0f-af3e-990c1ea355b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjjeTeDbZ18yPr8neXsZko",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2279,
      "cache_read_input_tokens": 16822,
      "output_tokens": 323,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2279
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 323,
          "cache_read_input_tokens": 16822,
          "cache_creation_input_tokens": 2279,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2279,
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

_source line 29 · 2026-05-14T17:00:12.001Z_

<details><summary>↩ Tool result · `toolu_01DKssh7CogJgd8eACjHdiKc`</summary>

```text
# BELLE Framework Analysis

## 1. QUESTION TYPE CLASSIFICATION

**Method**: LLM-based with in-context learning (ICL).

The framework uses GPT-4 to annotate unlabeled datasets, then performs manual verification. They state: "we use GPT-4 to annotate half of the datasets and perform cross-validation." Two independent reviewers validated 100 samples per type, achieving "an accuracy of 95%."

For inference, they use in-context examples formatted as QA pairs: "We concatenate several QA examples as demonstrations to perform the ICL mechanism, ensuring output of the correct question type labels."

**Distribution** (Table 4):
- Inference: 816-4,758 questions across datasets
- Comparison: 856-3,819
- Temporal: 414-2,691
- Null: 251-1,719

Ablation study (Table 7) compares strategies:
- In-context learning (ICL): 63.3% F1
- Supervised fine-tuning (SFT): 62.6% F1
- Zero-shot: 59.9% F1

## 2. BM25 RETRIEVAL

**Usage**: BM25 is the default sparse retriever, explicitly chosen for cost efficiency.

"Considering the computational cost of retrievers, we use the sparse model BM25 to replace the complex models." They note it "can be replaced by other high-precision neural models...as long as the candidate documents are prepared in advance."

**Parameters**: 
"We set a range of 3 to 10 candidate documents in each dataset for the multi-hop questions corresponding to these methods."

**Comparison**: The paper doesn't directly compare BM25 against dense retrievers, but frames it as a practical choice rather than optimal retrieval.

## 3. OPERATOR ASSIGNMENT

**Decision mechanism**: The bi-level debate determines operator selection, not a separate classifier.

The framework strategically assigns operators based on question type analysis:
- **Inference types**: Require "breaking down the question and using iterative-step retrieval to obtain more external knowledge"
- **Comparison/Temporal types**: Benefit from "sub-questions combined with single-step retrieval"

The opposing debaters propose operators, then "the judge J operates in two modes: (a) Hard Mode...if a correct combination of operators can be determined...the debate concludes; otherwise, it continues."

## 4. COST ANALYSIS

**Token consumption** (Table 3, comparing agent settings):
- BELLE: 20,742 average tokens
- LONGAGENT: 48,493 tokens  
- GEAR: 41,931 tokens
- RopMura: 56,859 tokens

**Performance vs. cost** (Figure 6):
BELLE achieves "higher performance while reducing reasoning overhead in terms of required tokens" compared to BeamAggR baseline.

Table 5 shows specific examples: on MultiHop-RAG, BELLE uses 18,324 tokens for 56.4% F1, while BeamAggR requires 26,940 tokens for 52.3% F1.

## 5. BI-LEVEL DEBATE MECHANISM

**Structure**: Two levels with five agent roles.

**First Level** (opposing):
- Affirmative debater (f_ad^t): "take turns presenting arguments based on their own previous debate history"
- Negative debater (f_nd^t): symmetric opposing role

Each receives "debate history from all t-1 rounds" plus outputs from second-level agents.

**Second Level** (monitoring):
- **Fast debater** (f_fast^t): "assess whether the operators selected in the current discussion between both sides are reasonable" using only current-round information
- **Slow debater** (f_slow^t): "integrates all historical information to judge the rationality of operator selection"—prevents "debaters from losing confidence in correct viewpoints"

The slow debater formula is: f_slow^t = M(f_ad^t, f_nd^t, f_fast^t, H_slow^(t-1)), incorporating full history.

**Judge**: "decides if a correct combination of operators can be determined after all debaters present their viewpoints."

**Efficiency**: Results show "typically requires only 2 rounds to determine operators."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5cdeee6-4d40-4a0f-af3e-990c1ea355b9",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "a7605e06f39e9a077",
  "type": "user",
  "uuid": "e5ac16f3-9593-4099-9841-8fcf42e3fa67",
  "sourceToolAssistantUUID": "d5cdeee6-4d40-4a0f-af3e-990c1ea355b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-14T17:00:15.437Z_

Now I have comprehensive details. Let me also do a quick check on the Semantic Scholar page for any additional citation or verification details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5ac16f3-9593-4099-9841-8fcf42e3fa67",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pS936zHEMqcXEMfHF7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37cd0fbd-d6ec-4347-8593-3c9f1c819c3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JGsuWrLGk7ncT74DooPdLj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1333,
      "cache_read_input_tokens": 19101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1333,
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

_source line 31 · 2026-05-14T17:00:18.161Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DrkS7nDshqnRpfcNFis9bR`</summary>

```json
{
  "url": "https://www.semanticscholar.org/paper/BELLE:-A-Bi-Level-Multi-Agent-Reasoning-Framework-Zhang-Li/4e826915ce02cb2f523dc0b08e5badac6f48ed84",
  "prompt": "Extract: number of citations, publication venue confirmation, author affiliations, and any other metadata about this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37cd0fbd-d6ec-4347-8593-3c9f1c819c3d",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pS936zHEMqcXEMfHF7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b44aea99-187c-4728-a56b-9740ff571de1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JGsuWrLGk7ncT74DooPdLj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1333,
      "cache_read_input_tokens": 19101,
      "output_tokens": 176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1333
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 176,
          "cache_read_input_tokens": 19101,
          "cache_creation_input_tokens": 1333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1333,
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

_source line 32 · 2026-05-14T17:00:20.479Z_

<details><summary>↩ Tool result · `toolu_01DrkS7nDshqnRpfcNFis9bR`</summary>

```text
I appreciate your detailed instructions, but I notice the web page content section appears to be empty (only dashes are shown). Without actual article content, I cannot extract:

- Citation count
- Publication venue
- Author affiliations
- Other metadata

**To assist you, please provide:**
1. The actual webpage content or article text
2. A direct link to the paper if available
3. Or the paper's title/DOI for reference

Once you share the source material, I'll extract the requested information while adhering to your guidelines about character limits and proper attribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b44aea99-187c-4728-a56b-9740ff571de1",
  "isSidechain": true,
  "promptId": "fc9aef79-ed3e-436e-abbf-266022d190cc",
  "agentId": "a7605e06f39e9a077",
  "type": "user",
  "uuid": "00f31a6d-7fc2-4ed3-8b06-6a179f7680c8",
  "sourceToolAssistantUUID": "b44aea99-187c-4728-a56b-9740ff571de1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-14T17:00:53.047Z_

That page didn't render. I have enough information now to provide a comprehensive answer. Here is my detailed report:

---

## Verification Report: BELLE (arxiv 2505.11811)

### 1. Does this paper exist? What venue?

**Yes, the paper exists.** Full title: "BELLE: A Bi-Level Multi-Agent Reasoning Framework for Multi-Hop Question Answering" by Taolin Zhang, Dongyang Li, Qizhou Chen, Chengyu Wang, and Xiaofeng He.

- **ArXiv**: 2505.11811, submitted May 17, 2025
- **Venue**: ACL 2025 main conference (long paper), confirmed via ACL Anthology at `https://aclanthology.org/2025.acl-long.211/`. Published in Proceedings of the 63rd Annual Meeting of the ACL, Volume 1: Long Papers, pages 4184-4202, Vienna, Austria, July 2025.
- DOI: `10.18653/v1/2025.acl-long.211`

**The ACL 2025 claim is verified.**

### 2. What does it do? Question type classification and operator assignment?

**Yes, this is accurate.** The framework has two key ideas:

**Question Type Classification**: They divide multi-hop questions into **4 types**:
- **Inference** -- requires logical connections through intermediate entities
- **Comparison** -- compares similarities/differences between entities
- **Temporal** -- based on event sequences at different time points
- **Null** -- unanswerable from retrieved documents or free-form queries

Classification uses **LLM-based in-context learning** (GPT-4 for annotation, then ICL at inference). They validated with human reviewers at 95% accuracy on 100 samples per type.

**Operator Assignment**: They define **5 reasoning operators** (methods for prompting LLMs):
- **CoT** (Chain-of-Thought) -- generates reasoning steps before the final answer
- **Single-step** -- one-time retrieval using the full question
- **Iterative-step** -- multi-round retrieval concatenating previous outputs
- **Sub-step** -- decomposes complex questions into sub-questions progressively
- **Adaptive-step** -- uses classifiers for different question types with a fixed approach

The key finding is that different question types respond differently to different operators (e.g., Inference benefits from iterative-step retrieval; Comparison/Temporal benefit from sub-questions with single-step retrieval). The **bi-level debate mechanism** decides which combination of operators to apply -- it is NOT a simple classifier but a multi-agent debate with 5 roles:

- **Level 1**: Affirmative debater, Negative debater (propose competing operator combinations)
- **Level 2**: Fast debater (assesses current-round reasonableness), Slow debater (integrates full history to prevent flip-flopping)
- **Judge**: Decides when consensus is reached (typically ~2 rounds)

### 3. Evaluation Datasets

Four datasets:
- **MultiHop-RAG**
- **HotpotQA**
- **2WikiMultiHopQA**
- **MuSiQue** (evaluated separately for 2-hop, 3-hop, and 4-hop subsets)

### 4. Key Results (F1 scores, GPT-3.5-turbo backbone)

**BELLE vs. strongest baseline (BeamAggR):**

| Dataset | BeamAggR F1 | BELLE F1 | Improvement |
|---------|------------|----------|-------------|
| MultiHop-RAG | 67.2 | **70.4** | +3.2 |
| HotpotQA | 62.9 | **66.5** | +3.6 |
| 2WikiMultiHopQA | 71.6 | **75.7** | +4.1 |
| MuSiQue 2-hop | 45.9 (EM) | **50.5** (EM) | +4.6 |
| MuSiQue 3-hop | 36.8 (F1) | **42.1** (F1) | +5.3 |
| MuSiQue 4-hop | 21.6 (F1) | **29.2** (F1) | +7.6 |

Other baselines it beats: IRCoT (59.2 F1 on MultiHop-RAG), FLARE (58.7), ProbTree (62.5), EfficientRAG (55.3), LONGAGENT (56.8), GEAR (52.5), RopMura (53.7).

**With GPT-4 backbone**: BELLE reaches 71.3 F1 on MultiHop-RAG, 66.9 on HotpotQA, 75.3 on 2WikiQA.

**With open-source models**: Qwen2.5-7B achieves 56.2 avg F1; Mistral-7B achieves 55.3 avg F1 -- both still beating BeamAggR with GPT-3.5.

**Ablation highlights** (GPT-3.5, avg F1 across datasets):
- Full BELLE: 63.3
- w/o Type Classifier: 60.5 (-2.8)
- w/o Second Level Debate: 59.6 (-3.7)
- w/o Slow Debater: 59.9 (-3.4)

**Cost efficiency**: BELLE uses ~20,742 tokens on average vs. LONGAGENT (48,493), GEAR (41,931), RopMura (56,859) -- roughly 2-3x fewer tokens than other agent-based methods.

### 5. Does it use BM25 retrieval?

**Yes, confirmed.** The paper states: "Considering the computational cost of retrievers, we use the sparse model BM25 to replace the complex models." BM25 is the **default retriever** used across all experiments. The corpus is October 2017 Wikipedia dumps. They retrieve 3-10 candidate documents per question depending on the dataset.

They explicitly note BM25 is a practical/cost choice and "can be replaced by other high-precision neural models...as long as the candidate documents are prepared in advance." They do NOT directly compare BM25 against dense retrievers like Contriever or ColBERT in their experiments.

---

Sources:
- [ArXiv Abstract](https://arxiv.org/abs/2505.11811)
- [ArXiv HTML Full Paper](https://arxiv.org/html/2505.11811)
- [ACL Anthology Entry](https://aclanthology.org/2025.acl-long.211/)
- [Semantic Scholar](https://www.semanticscholar.org/paper/BELLE:-A-Bi-Level-Multi-Agent-Reasoning-Framework-Zhang-Li/4e826915ce02cb2f523dc0b08e5badac6f48ed84)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00f31a6d-7fc2-4ed3-8b06-6a179f7680c8",
  "isSidechain": true,
  "agentId": "a7605e06f39e9a077",
  "requestId": "req_011Cb2pSmGCLv2Yf8WbaBifk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db1659e9-e456-48e8-9987-781dd6ad60d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dc0000b1-7eb7-408f-93e5-2e48a2af8809",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGZQb8dE3pdBNEJPA54KpU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 308,
      "cache_read_input_tokens": 20434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 308,
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
