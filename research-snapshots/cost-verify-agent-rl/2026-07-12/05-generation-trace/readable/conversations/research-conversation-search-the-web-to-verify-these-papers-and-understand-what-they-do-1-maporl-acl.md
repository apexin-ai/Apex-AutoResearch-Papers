# Research conversation: Search the web to verify these papers and understand what they do: 1. MAPoRL (ACL 2025) - "Multi-Agent Post-Co-Training 

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad679632efe395930.jsonl`
- **Structured JSON:** [`50233d5754acc6720a19.json`](../../sessions/50/50233d5754acc6720a19.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

61 recorded events

### User

_source line 1 · 2026-05-10T22:14:41.843Z_

Search the web to verify these papers and understand what they do:

1. MAPoRL (ACL 2025) - "Multi-Agent Post-Co-Training for Collaborative LLMs" 
   - Search for this paper on arxiv and Google Scholar
   - Does it co-train generation and comprehension?
   - Does it use contrastive objectives?

2. Social Deduction LLM (AAMAS 2025, arXiv 2502.06060) - "Training Language Models for Social Deduction with Multi-Agent RL"
   - Does it train receiver-side listening loss?
   - Is it task-specific (Among Us)?
   - Is it non-contrastive?

3. Also search for any paper that does "bilateral" or "bidirectional" contrastive training of both sender and receiver communication in LLM agents, specifically from 2025-2026.

4. Search for "MAGE contrastive multi-agent communication 2025" - there was a mention of MAGE (Pattern Recognition 2025) doing graph contrastive learning for multi-agent communication. Is this relevant as a missing citation?

Report exactly what you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "b1ff66d0-64ad-4114-aa20-0be008e119f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T22:14:41.846Z_

```json
{
  "parentUuid": "b1ff66d0-64ad-4114-aa20-0be008e119f7",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
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
  "uuid": "15de0956-a740-4d3e-879f-c41e25300270",
  "timestamp": "2026-05-10T22:14:41.846Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T22:14:44.774Z_



I'll search for all of these papers systematically. Let me start by loading the WebSearch and WebFetch tools, then conduct the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15de0956-a740-4d3e-879f-c41e25300270",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufBTEkDPM3FppRRCmfb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5f32e068-43df-4c4e-992d-1db052f7023b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4XQpKEx4rVqWb98pR1SHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 815,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 815,
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

_source line 4 · 2026-05-10T22:14:44.817Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Jx5CVAbteNP6PfLqCjTiL1`</summary>

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
  "parentUuid": "5f32e068-43df-4c4e-992d-1db052f7023b",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufBTEkDPM3FppRRCmfb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e16edfef-2799-432d-98d4-0772894aef14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4XQpKEx4rVqWb98pR1SHL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 815,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 815,
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

### Tool result

_source line 5 · 2026-05-10T22:14:44.820Z_

<details><summary>↩ Tool result · `toolu_01Jx5CVAbteNP6PfLqCjTiL1`</summary>

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
  "parentUuid": "e16edfef-2799-432d-98d4-0772894aef14",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "5303fd48-ff94-45b9-a28a-4b370ae0c8bf",
  "sourceToolAssistantUUID": "e16edfef-2799-432d-98d4-0772894aef14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T22:14:47.335Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5303fd48-ff94-45b9-a28a-4b370ae0c8bf",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufBggd8m9ecvg3n42qa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2a7ef7a-c73c-43db-9fd3-c51e05890733",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCY3u7pZqsZxHDRb8LcX3K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1922,
      "cache_read_input_tokens": 9038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1922,
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

_source line 7 · 2026-05-10T22:14:48.294Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013rF3Xd9Z6hVnfTKaQwVfdr`</summary>

```json
{
  "query": "MAPoRL \"Multi-Agent Post-Co-Training for Collaborative LLMs\" ACL 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2a7ef7a-c73c-43db-9fd3-c51e05890733",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufBggd8m9ecvg3n42qa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7df6d559-9a24-4250-8e99-32148032663c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCY3u7pZqsZxHDRb8LcX3K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1922,
      "cache_read_input_tokens": 9038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1922,
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

_source line 8 · 2026-05-10T22:14:49.818Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KZ8tjxfDjMdGauJZZVUE4V`</summary>

```json
{
  "query": "arXiv 2502.06060 \"Training Language Models for Social Deduction with Multi-Agent RL\" AAMAS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7df6d559-9a24-4250-8e99-32148032663c",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufBggd8m9ecvg3n42qa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "abc6bbf6-0080-435d-aa17-cb637fdcc40a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCY3u7pZqsZxHDRb8LcX3K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1922,
      "cache_read_input_tokens": 9038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1922,
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

_source line 9 · 2026-05-10T22:14:50.761Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CuRxrUcRpTgn2R3qLojAGi`</summary>

```json
{
  "query": "bilateral bidirectional contrastive training sender receiver communication LLM agents 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abc6bbf6-0080-435d-aa17-cb637fdcc40a",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufBggd8m9ecvg3n42qa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62ed3879-54d7-4e6d-af78-222b59b2c865",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCY3u7pZqsZxHDRb8LcX3K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1922,
      "cache_read_input_tokens": 9038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1922,
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

_source line 10 · 2026-05-10T22:14:51.107Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012mB6TbhDYaCRjuJxyFzWNi`</summary>

```json
{
  "query": "MAGE contrastive multi-agent communication 2025 Pattern Recognition graph"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62ed3879-54d7-4e6d-af78-222b59b2c865",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufBggd8m9ecvg3n42qa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a002022-88f1-4aa3-9c64-373413fbb441",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCY3u7pZqsZxHDRb8LcX3K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1922,
      "cache_read_input_tokens": 9038,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1922
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 262,
          "cache_read_input_tokens": 9038,
          "cache_creation_input_tokens": 1922,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1922,
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

_source line 11 · 2026-05-10T22:14:54.874Z_

<details><summary>↩ Tool result · `toolu_013rF3Xd9Z6hVnfTKaQwVfdr`</summary>

```text
Web search results for query: "MAPoRL "Multi-Agent Post-Co-Training for Collaborative LLMs" ACL 2025 arxiv"

Links: [{"title":"MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1459/"},{"title":"[2502.18439] MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning","url":"https://arxiv.org/abs/2502.18439"},{"title":"MAPoRL2: Multi-Agent Post-Co-Training for Collaborative ...","url":"https://aclanthology.org/2025.acl-long.1459.pdf"},{"title":"MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=f85TQ7hyzh"},{"title":"MAPoRL: Multi-Agent Post-Co-Training for Collaborative ...","url":"https://arxiv.org/pdf/2502.18439"},{"title":"[PDF] MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MAPoRL:-Multi-Agent-Post-Co-Training-for-Large-with-Park-Han/aa89c6bf86486e180833037333555e3492b15c8e"},{"title":"Publication","url":"https://chanwoo-park-official.github.io/publication/"},{"title":"[2502.18439v1] MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning","url":"http://arxiv.org/abs/2502.18439v1"},{"title":"[Quick Review] MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning","url":"https://liner.com/review/maporl-multiagent-postcotraining-for-collaborative-large-language-models-with-reinforcement"},{"title":"MAPoRL: Multi-agent post-co-training for collaborative large language models with reinforcement learning - Amazon Science","url":"https://www.amazon.science/publications/maporl-multi-agent-post-co-training-for-collaborative-large-language-models-with-reinforcement-learning"}]

I found the paper! Here are the results for your search:

## MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning

**Publication Details:**
- Published at ACL 2025 (63rd Annual Meeting of the Association for Computational Linguistics, pages 30215–30248, Vienna, Austria)
- Authors: Chanwoo Park, Seungju Han, Xingzhi Guo, Asuman E. Ozdaglar, Kaiqing Zhang, and Joo-Kyung Kim
- **arXiv:** 2502.18439

**Overview:**
MAPoRL introduces a new post-training paradigm to explicitly elicit collaborative behaviors and further unleash the power of multi-agentic LLM frameworks.

**Key Approach:**
In MAPoRL, multiple LLMs first generate their own responses independently and engage in a multi-turn discussion to collaboratively improve the final answer. In the end, a MAPoRL verifier evaluates both the answer and the discussion, by assigning a score that verifies the correctness of the answer, while adding incentives to encourage corrective and persuasive discussions.

**Key Innovation:**
A key novelty from most existing LLM post-training paradigms is the advocacy of co-training multiple LLMs together, and the use of RL for better generalization.

**Results:**
Experiments show that training single LLMs solely is insufficient for encouraging collaboration, while multi-agent co-training can significantly enhance the collaboration performance across multiple datasets, with generalization to unseen domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7df6d559-9a24-4250-8e99-32148032663c",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "62ff345e-6a34-49d6-bd86-5601baf4313b",
  "sourceToolAssistantUUID": "7df6d559-9a24-4250-8e99-32148032663c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T22:14:56.962Z_

<details><summary>↩ Tool result · `toolu_012mB6TbhDYaCRjuJxyFzWNi`</summary>

```text
Web search results for query: "MAGE contrastive multi-agent communication 2025 Pattern Recognition graph"

Links: [{"title":"Multi-Agent Communication with Information Preserving ...","url":"https://www.ijcai.org/proceedings/2025/0008.pdf"},{"title":"Exploring Communication in Multi-Agent Reinforcement Learning","url":"https://www.scitepress.org/Papers/2025/133834/133834.pdf"},{"title":"Learning To Ground Decentralized Multi-Agent Communication with Contrastive Learning | OpenReview","url":"https://openreview.net/forum?id=rLceWXWCmZc"},{"title":"Learning Multi-Agent Communication with Contrastive Learning | OpenReview","url":"https://openreview.net/forum?id=vZZ4hhniJU"},{"title":"Learning Multi-Agent Communication with Contrastive Learning","url":"https://arxiv.org/html/2307.01403v3"},{"title":"Accepted Papers (with video links) – AAMAS 2025 Detroit","url":"https://aamas2025.org/index.php/conference/program/accepted-papers/"},{"title":"AAMAS 2025: Proceedings of the 2025 International Conference on Autonomous Agents and Multiagent Systems","url":"https://www.ifaamas.org/Proceedings/aamas2025/forms/contents.htm"},{"title":"GitHub - LantaoYu/MARL-Papers: Paper list of multi-agent reinforcement learning (MARL) · GitHub","url":"https://github.com/LantaoYu/MARL-Papers"},{"title":"EUMAS 2025","url":"https://euramas.github.io/eumas2025/"},{"title":"A survey of multi-agent deep reinforcement learning with communication | Autonomous Agents and Multi-Agent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10458-023-09633-6"}]

Based on the search results, I found several relevant papers related to your query about multi-agent communication with contrastive learning and pattern recognition. Here's what I found:

## Key Research Works

**2025 Recent Publications:**

One paper combines node representations from original and agent feature views using contrastive learning, with MAIL effectively learning expressive message representations by minimizing feature contrastive loss, cross-module loss, and topological contrastive loss.

Another work was presented at the 14th International Conference on Pattern Recognition Applications and Methods (ICPRAM 2025), exploring communication in multi-agent reinforcement learning.

**Contrastive Learning for Multi-Agent Communication:**

Research proposes viewing communicative messages sent between agents as different incomplete views of the environment state, and uses contrastive learning to maximize the mutual information between messages of a given trajectory. In this approach, different agents' views of the same environment state are considered positive samples and messages are contrastively learned as encodings of that state.

**Graph-based Communication:**

Full communication is regarded as a fully connected graph, where works like DIAL, RIAL, CommNet, and BiCNet learn communication protocols that connect all agents together.

These papers collectively address the intersection of multi-agent communication, contrastive learning approaches, and graph-based communication patterns that align with your search topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a002022-88f1-4aa3-9c64-373413fbb441",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "77aa01c0-fe00-46a3-8096-22cc9a17fd11",
  "sourceToolAssistantUUID": "6a002022-88f1-4aa3-9c64-373413fbb441",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T22:14:57.465Z_

<details><summary>↩ Tool result · `toolu_01KZ8tjxfDjMdGauJZZVUE4V`</summary>

```text
Web search results for query: "arXiv 2502.06060 "Training Language Models for Social Deduction with Multi-Agent RL" AAMAS 2025"

Links: [{"title":"[2502.06060] Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning","url":"https://arxiv.org/abs/2502.06060"},{"title":"Training Language Models for Social Deduction with Multi-Agent","url":"https://arxiv.org/pdf/2502.06060"},{"title":"Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2502.06060"},{"title":"[2502.06060v1] Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning","url":"https://arxiv.org/abs/2502.06060v1"},{"title":"Paper page - Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning","url":"https://huggingface.co/papers/2502.06060"},{"title":"LLM Training for Social Deduction with MARL","url":"https://www.emergentmind.com/papers/2502.06060"},{"title":"(PDF) Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning","url":"https://www.researchgate.net/publication/388883243_Training_Language_Models_for_Social_Deduction_with_Multi-Agent_Reinforcement_Learning"},{"title":"Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/abs/2502.06060"},{"title":"LLM Collaboration with Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2508.04652v2"},{"title":"SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2506.24119v1"}]

I found the paper for you! Here are the key details about arXiv paper 2502.06060:

**Title:** Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning

**Publication Details:** The paper is being presented at AAMAS 2025 in Detroit, Michigan, USA, May 19–23, 2025

**Authors:** Bidipta Sarkar, Warren Xia, C. Karen Liu, and Dorsa Sadigh

**Main Contribution:** The work trains language models to have productive discussions about their environment in natural language without any human demonstrations.

**Key Approach:** The researchers improve a model's listening skills by training them to predict information about the environment based on discussions, and simultaneously improve a model's speaking skills with multi-agent reinforcement learning by rewarding messages based on their influence on other agents.

**Experimental Setting:** The study uses an embodied social deduction game based on Among Us, where the key question to answer is the identity of an adversarial imposter.

**Results:** The analysis found emergent behaviors such as accusing suspects and providing evidence, with the technique enabling strong discussions and doubling the win rates compared to standard RL.

The paper was first submitted on February 9, 2025, and the authors released their code and models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "abc6bbf6-0080-435d-aa17-cb637fdcc40a",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "48b24487-48e3-490e-b1ee-cea20861adaa",
  "sourceToolAssistantUUID": "abc6bbf6-0080-435d-aa17-cb637fdcc40a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T22:14:58.822Z_

<details><summary>↩ Tool result · `toolu_01CuRxrUcRpTgn2R3qLojAGi`</summary>

```text
Web search results for query: "bilateral bidirectional contrastive training sender receiver communication LLM agents 2025 2026"

Links: [{"title":"LLM2Vec Tutorial: Steps for transforming any decoder-only model into a text encoder - McGill NLP","url":"https://mcgill-nlp.github.io/llm2vec/tutorial/"},{"title":"Training LLMs to be Better Text Embedders through Bidirectional Reconstruction","url":"https://arxiv.org/html/2509.03020v1"},{"title":"Adapting LLM Agents Through Communication | OpenReview","url":"https://openreview.net/forum?id=wOelVq8fwL"},{"title":"MasRouter: Learning to Route LLMs for Multi-Agent System","url":"https://aclanthology.org/2025.acl-long.757.pdf"},{"title":"[2509.03020] Training LLMs to be Better Text Embedders through Bidirectional Reconstruction","url":"https://arxiv.org/abs/2509.03020"},{"title":"GitHub - AGI-Edgerunners/LLM-Agents-Papers: A repo lists papers related to LLM based agent · GitHub","url":"https://github.com/AGI-Edgerunners/LLM-Agents-Papers"},{"title":"Adapting LLM Agents with Universal Feedback in Communication","url":"https://arxiv.org/html/2310.01444v3"},{"title":"Towards Communication Efficient Multi-Agent Cooperations: Reinforcement Learning and LLM","url":"https://www.techrxiv.org/users/878096/articles/1259644-towards-communication-efficient-multi-agent-cooperations-reinforcement-learning-and-llm"},{"title":"Multi-Agent Transfer Learning Based on Contrastive Role Relationship Representation","url":"https://www.mdpi.com/2673-2688/7/1/13"},{"title":"Paper page - Adapting LLM Agents Through Communication","url":"https://huggingface.co/papers/2310.01444"}]

I found several relevant research papers related to bidirectional training, contrastive learning, and LLM agent communication. Here are the key findings:

## Bidirectional Reconstruction and Contrastive Training

A recent paper proposes adding a new training stage before contrastive learning using bidirectional generative reconstruction tasks, namely EBQ2D (Embedding-Based Query-to-Document) and EBD2Q (Embedding-Based Document-to-Query), which interleave to anchor the [EOS] embedding and reconstruct either side of Query-Document pairs. Following the bidirectional reconstruction, the second stage fine-tunes the model with contrastive learning to further improve the quality of the generated representations. This work was published in September 2025.

## LLM Agent Communication

A Learning through Communication (LTC) paradigm enables LLM agents to improve continuously through interactions with their environments and other agents, with three structured communication patterns: Monologue, Dialogue, and Analogue—tailored for common tasks such as decision-making, knowledge-intensive reasoning, and numerical reasoning.

## Multi-Agent Communication Protocols

Recent work proposes a goal-oriented human-interpretable feature communication protocol for multi-robot navigation, and an LLM-based Bandwidth-Adaptive Dual-Policy (LLM-BDP) framework that can adapt to varying bandwidth constraints by simply modifying the input prompt, thereby eliminating the need for retraining. This was published in April 2025.

## Contrastive Learning in Multi-Agent Systems

A Multi-agent Transfer Learning framework employs contrastive learning-driven role representation modeling to capture the differences and commonalities of agent behavior patterns among multiple tasks, generating generalizable role representations that enable agents to efficiently share role assignment knowledge and achieve policy transfer through precise role adaptation. This was published in January 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62ed3879-54d7-4e6d-af78-222b59b2c865",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "e92832f1-6281-43d9-98c4-1bf60f78e6c1",
  "sourceToolAssistantUUID": "62ed3879-54d7-4e6d-af78-222b59b2c865",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T22:15:02.600Z_

Good, I have initial results. Now let me dig deeper into each paper to answer the specific questions. Let me fetch the actual paper pages and do additional targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e92832f1-6281-43d9-98c4-1bf60f78e6c1",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufChqc3SSi3RTtxLMhU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6ea0774-501d-453f-a69e-0f18992ac00e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Z1RMQDLej3MhsePYcrBEt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 821,
      "cache_creation_input_tokens": 3053,
      "cache_read_input_tokens": 10960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3053,
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

_source line 16 · 2026-05-10T22:15:05.131Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UeRHKCY9pzrscYChS16qXr`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.18439",
  "prompt": "Extract the full abstract and methodology details. Specifically: 1) Does this paper co-train generation and comprehension? 2) Does it use any contrastive objectives or contrastive learning? 3) What training methodology does it use (RL, supervised, contrastive)? 4) What is the main training signal/reward?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6ea0774-501d-453f-a69e-0f18992ac00e",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufChqc3SSi3RTtxLMhU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63ca2be8-4b44-4ba2-8347-5962120e614b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Z1RMQDLej3MhsePYcrBEt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 821,
      "cache_creation_input_tokens": 3053,
      "cache_read_input_tokens": 10960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3053,
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

_source line 17 · 2026-05-10T22:15:07.467Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011NDaNUFs29S42aXGkdPiPy`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.06060",
  "prompt": "Extract the full abstract and methodology details. Specifically: 1) Does this paper train a receiver-side listening loss? 2) Is it task-specific to Among Us or general? 3) Does it use contrastive objectives or non-contrastive training? 4) How does it train speaking vs listening skills? 5) What is the training signal for the listening component?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63ca2be8-4b44-4ba2-8347-5962120e614b",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufChqc3SSi3RTtxLMhU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0295c5ec-9eaa-40d2-ae14-271db8465659",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Z1RMQDLej3MhsePYcrBEt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 821,
      "cache_creation_input_tokens": 3053,
      "cache_read_input_tokens": 10960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3053,
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

_source line 18 · 2026-05-10T22:15:09.333Z_

<details><summary>↩ Tool result · `toolu_01UeRHKCY9pzrscYChS16qXr`</summary>

```text
# MAPoRL Paper Analysis

Based on the abstract provided:

## 1) Co-training Generation and Comprehension?
**No.** The paper focuses on co-training multiple LLMs together for collaborative tasks. It describes "multiple LLMs first generate their own responses independently and engage in a multi-turn discussion," but this addresses collaborative generation rather than pairing generation with comprehension components.

## 2) Contrastive Learning?
**No indication present.** The abstract contains no mention of contrastive objectives or contrastive learning methodologies.

## 3) Training Methodology
**Reinforcement Learning (RL).** The abstract explicitly states the approach uses "multi-agent RL" and describes it as "Multi-Agent Post-co-training for collaborative LLMs with Reinforcement Learning."

## 4) Main Training Signal/Reward
The reward comes from **a specialized verifier component**. As described: "a MAPoRL verifier evaluates both the answer and the discussion, by assigning a score that verifies the correctness of the answer, while adding incentives to encourage corrective and persuasive discussions. The score serves as the co-training reward."

The key innovation is that unlike single-agent training approaches, this paradigm performs "co-training of multiple LLMs together using RL for better generalization."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63ca2be8-4b44-4ba2-8347-5962120e614b",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "74921fe0-c65c-4709-9235-25b23b6bbb8d",
  "sourceToolAssistantUUID": "63ca2be8-4b44-4ba2-8347-5962120e614b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-10T22:15:09.773Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FLQL2DuRENdapoxitGUyvs`</summary>

```json
{
  "url": "https://openreview.net/forum?id=wOelVq8fwL",
  "prompt": "What is this paper about? Does it do bilateral or bidirectional contrastive training of both sender and receiver in LLM multi-agent communication? Extract the title, authors, venue, and key methodology details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74921fe0-c65c-4709-9235-25b23b6bbb8d",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufChqc3SSi3RTtxLMhU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b3a4664-d2fd-49d3-b422-d06a51ffb3b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Z1RMQDLej3MhsePYcrBEt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 821,
      "cache_creation_input_tokens": 3053,
      "cache_read_input_tokens": 10960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3053,
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

_source line 20 · 2026-05-10T22:15:11.139Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01E9cEn2GyNRXoqybrbPsG5i`</summary>

```json
{
  "url": "https://openreview.net/forum?id=vZZ4hhniJU",
  "prompt": "Extract the full details of this paper. Title, authors, venue, year. Does it do contrastive learning for multi-agent communication? Is this the MAGE paper? What is the methodology?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b3a4664-d2fd-49d3-b422-d06a51ffb3b0",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufChqc3SSi3RTtxLMhU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b781e313-a893-4ae2-93a4-6f36b29c09a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Z1RMQDLej3MhsePYcrBEt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 821,
      "cache_creation_input_tokens": 3053,
      "cache_read_input_tokens": 10960,
      "output_tokens": 568,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3053
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 821,
          "output_tokens": 568,
          "cache_read_input_tokens": 10960,
          "cache_creation_input_tokens": 3053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3053,
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

_source line 21 · 2026-05-10T22:15:12.035Z_

<details><summary>↩ Tool result · `toolu_011NDaNUFs29S42aXGkdPiPy`</summary>

```text
# Analysis of Paper 2502.06060

Based on the abstract provided, here are the answers to your questions:

**1) Receiver-side listening loss:**
Yes. The paper explicitly states they "improve a model's listening skills by training them to predict information about the environment based on discussions," treating this as a dense reward signal.

**2) Task-specificity:**
It appears task-specific to Among Us. The research "study[ies] an embodied social deduction game based on Among Us, where the key question to answer is the identity of an adversarial imposter."

**3) Training objectives:**
The abstract does not mention contrastive or non-contrastive approaches specifically. It describes decomposing communication into "listening and speaking" components with distinct training mechanisms.

**4) Speaking vs. listening training:**
The methodology decomposes distinctly: listening skills improve through prediction tasks about environmental information, while "speaking skills [improve] with multi-agent reinforcement learning by rewarding messages based on their influence on other agents."

**5) Listening training signal:**
The training signal appears to be predictive accuracy. The paper rewards models for "predict[ing] useful information about the world" from discussions, using this as "a dense reward signal that guides communication."

**Key result:** This approach "doubling the win rates compared to standard RL," suggesting substantial improvements over baseline methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0295c5ec-9eaa-40d2-ae14-271db8465659",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "047052bf-28fa-4efa-8ccc-e45446eb3f99",
  "sourceToolAssistantUUID": "0295c5ec-9eaa-40d2-ae14-271db8465659",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T22:15:13.870Z_

<details><summary>↩ Tool result · `toolu_01FLQL2DuRENdapoxitGUyvs`</summary>

```text
# Paper Summary

**Title:** "Adapting LLM Agents Through Communication"

**Authors:** Kuan Wang, Yadong Lu, Michael Santacroce, Yeyun Gong, Chao Zhang, yelong shen

**Venue:** ICLR 2024 Conference

**Key Focus:** The paper presents the Learning through Communication (LTC) paradigm, designed to help language model agents improve their task performance through structured interactions.

## Methodology Overview

The approach combines "iterative exploration and PPO training" to enable agents to convert short-term experiences into persistent knowledge. Rather than focusing on bilateral or bidirectional contrastive training between sender and receiver roles, the work emphasizes three communication patterns:

- **Monologue:** For decision-making tasks
- **Dialogue:** For knowledge-intensive reasoning
- **Analogue:** For numerical reasoning

## Key Results

The method demonstrates improvements across diverse benchmarks:
- ALFWorld: 12% improvement over instruction tuning baseline
- HotpotQA: 5.1% improvement over instruction-tuned LLaMA-7B
- GSM8k: 3.6% improvement over CoT-Tuning baseline

The paper does not appear to employ bilateral contrastive training methodology based on the abstract and submission details provided. Instead, it focuses on structured agent-environment and agent-agent interactions optimized for specific task categories.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b3a4664-d2fd-49d3-b422-d06a51ffb3b0",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "2bed35cb-03dd-48ca-bcde-7005694109d4",
  "sourceToolAssistantUUID": "6b3a4664-d2fd-49d3-b422-d06a51ffb3b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T22:15:14.975Z_

<details><summary>↩ Tool result · `toolu_01E9cEn2GyNRXoqybrbPsG5i`</summary>

```text
# Paper Details

**Title:** Learning Multi-Agent Communication with Contrastive Learning

**Authors:** Yat Long Lo, Biswa Sengupta, Jakob Nicolaus Foerster, Michael Noukhovitch

**Venue:** ICLR 2024 Conference

**Year:** 2024 (Published January 16, 2024)

## Contrastive Learning for Multi-Agent Communication

Yes, this paper explicitly uses contrastive learning for multi-agent communication. The core contribution involves treating "communicative messages sent between agents are considered as different incomplete views of the environment state."

## Is This the MAGE Paper?

No indication in the provided content suggests this is the MAGE paper. The submission number is 2048.

## Methodology

The approach centers on a multi-view contrastive perspective:

- **Key insight:** Messages function as agent encodings of environmental state
- **Technique:** The method "learn[s] to communicate using contrastive learning to maximize the mutual information between messages of a given trajectory"
- **Setting:** Operates in decentralized multi-agent reinforcement learning environments
- **Results:** Shows improved performance, faster learning, more symmetric communication patterns, and better global state capture compared to prior approaches

The work is positioned as addressing the challenge of inducing effective shared communication in decentralized multi-agent settings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b781e313-a893-4ae2-93a4-6f36b29c09a6",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "a74226db-d622-4a9f-89dc-378593a26f4c",
  "sourceToolAssistantUUID": "b781e313-a893-4ae2-93a4-6f36b29c09a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T22:15:17.952Z_

Good, now let me search more specifically for the MAGE paper and for bilateral contrastive training of LLM agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a74226db-d622-4a9f-89dc-378593a26f4c",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufDtsfA4475yhMdHgkk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7f2a193-7aea-4a84-b89b-afba98f6506d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMr6GAajh1xj1yKN9TWzpv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2816,
      "cache_read_input_tokens": 14013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2816,
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

_source line 25 · 2026-05-10T22:15:19.162Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DeGzZMXD1ARAJjmCBjZ9hL`</summary>

```json
{
  "query": "MAGE \"Pattern Recognition\" 2025 graph contrastive learning multi-agent communication reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7f2a193-7aea-4a84-b89b-afba98f6506d",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufDtsfA4475yhMdHgkk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb4e2287-46ce-4755-b28f-1cb2328fdd83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMr6GAajh1xj1yKN9TWzpv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2816,
      "cache_read_input_tokens": 14013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2816,
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

_source line 26 · 2026-05-10T22:15:19.923Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CKY9QUBFjaZ6d32oQGwUAw`</summary>

```json
{
  "query": "\"contrastive\" \"sender\" \"receiver\" \"LLM\" OR \"language model\" multi-agent communication training 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb4e2287-46ce-4755-b28f-1cb2328fdd83",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufDtsfA4475yhMdHgkk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "866b6c79-5eac-4590-9c0d-afbc5535a030",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMr6GAajh1xj1yKN9TWzpv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2816,
      "cache_read_input_tokens": 14013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2816,
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

_source line 27 · 2026-05-10T22:15:20.130Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W5BN86PYxodDYHMwYkLfKw`</summary>

```json
{
  "query": "MAGE multi-agent graph contrastive Pattern Recognition 2025 communication emergent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "866b6c79-5eac-4590-9c0d-afbc5535a030",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufDtsfA4475yhMdHgkk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39e04236-b03b-402a-9645-147e112f6817",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMr6GAajh1xj1yKN9TWzpv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2816,
      "cache_read_input_tokens": 14013,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2816
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 218,
          "cache_read_input_tokens": 14013,
          "cache_creation_input_tokens": 2816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2816,
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

_source line 28 · 2026-05-10T22:15:27.011Z_

<details><summary>↩ Tool result · `toolu_01W5BN86PYxodDYHMwYkLfKw`</summary>

```text
Web search results for query: "MAGE multi-agent graph contrastive Pattern Recognition 2025 communication emergent"

Links: [{"title":"Learning multi-agent communication via graph contrastive learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538"},{"title":"Multi-Agent Communication with Information Preserving ...","url":"https://www.ijcai.org/proceedings/2025/0008.pdf"},{"title":"MegaAgent: A Large-Scale Autonomous LLM-based Multi- ...","url":"https://aclanthology.org/2025.findings-acl.259.pdf"},{"title":"LEARNING MULTI-AGENT COMMUNICATION WITH ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/de2ad3ed44ee4e675b3be42aa0b615d0-Paper-Conference.pdf"},{"title":"A unified multimodal GenAI platform integrating GraphRAG multi-agent systems and custom language models for intelligent document processing and knowledge synthesis | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-47145-x"},{"title":"A Comprehensive Review of AI Agents: Transforming Possibilities in Technology and Beyond","url":"https://arxiv.org/html/2508.11957v1"},{"title":"Machine Learning Feb 2025","url":"https://www.arxiv.org/list/cs.LG/2025-02?skip=4125&show=1000"},{"title":"A survey of multi-agent deep reinforcement learning with communication | Autonomous Agents and Multi-Agent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10458-023-09633-6"},{"title":"Evaluating the Collaboration and Competition of LLM agents","url":"https://aclanthology.org/2025.acl-long.421.pdf"},{"title":"Learning Multi-Agent Communication from Graph Modeling Perspective | OpenReview","url":"https://openreview.net/forum?id=Qox9rO0kN0"}]

Based on the web search results, here's what I found about MAGE and related research:

## MAGE: Multi-Agent Graph Contrastive Learning

MAGE is a novel multi-agent communication method via graph contrastive learning to learn high-quality message representations. 

### Key Components

MAGE utilizes contrast objectives to learn optimal message representations, considering feature and topological levels. The approach works by:

1. **Graph View Generation**: In MAGE, two correlated graph views are generated by applying stochastic corruption to the constructed graph.

2. **Contrastive Training**: MAGE is trained using a contrastive loss function to enhance the consistency of agent features across these two views.

3. **Data Augmentation Strategy**: The scheme improves data augmentation by modifying both the topology structure and agent features to boost the optimization of the contrastive objective, specifically through edge removal and feature masking.

### Communication Learning Context

Communication learning has emerged as a successful tool for tackling complex tasks in multi-agent reinforcement learning (MARL). Many MARL methods use graph neural networks (GNNs) to build a communication learning framework where agents and communication channels can be represented as nodes and edges in a graph.

The research appears to be published in the Pattern Recognition journal in 2025, addressing how to extract expressive information from neighboring agents to obtain high-quality message representations in multi-agent systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39e04236-b03b-402a-9645-147e112f6817",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "55a5f81b-f86e-44dc-9989-7809c83ece77",
  "sourceToolAssistantUUID": "39e04236-b03b-402a-9645-147e112f6817",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T22:15:27.699Z_

<details><summary>↩ Tool result · `toolu_01CKY9QUBFjaZ6d32oQGwUAw`</summary>

```text
Web search results for query: ""contrastive" "sender" "receiver" "LLM" OR "language model" multi-agent communication training 2025"

Links: [{"title":"Multi-Agent Collaboration Mechanisms: A Survey of LLMs","url":"https://arxiv.org/html/2501.06322v1"},{"title":"MAPoRL2: Multi-Agent Post-Co-Training for Collaborative ...","url":"https://aclanthology.org/2025.acl-long.1459.pdf"},{"title":"LLM-Based Multi-Agent Systems (LLM-MAS)","url":"https://www.emergentmind.com/topics/large-language-model-based-multi-agent-systems-llm-mas"},{"title":"Learning Multi-Agent Communication with Contrastive Learning","url":"https://arxiv.org/html/2307.01403"},{"title":"GitHub - taichengguo/LLM_MultiAgents_Survey_Papers: Large Language Model based Multi-Agents: A Survey of Progress and Challenges (In IJCAI 2024) · GitHub","url":"https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers"},{"title":"LLM-Coordination: Evaluating and Analyzing Multi-agent ...","url":"https://aclanthology.org/2025.findings-naacl.448.pdf"},{"title":"LLMs for Multi-Agent Cooperation | Xueguang Lyu","url":"https://xue-guang.com/post/llm-marl/"},{"title":"Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems","url":"https://arxiv.org/html/2502.14321v1"},{"title":"Towards Communication Efficient Multi-Agent Cooperations: Reinforcement Learning and LLM","url":"https://www.techrxiv.org/users/878096/articles/1259644-towards-communication-efficient-multi-agent-cooperations-reinforcement-learning-and-llm"},{"title":"Large Language Model Enhanced Multi-Agent Systems for 6G Communications | IEEE Wireless Communications","url":"https://dl.acm.org/doi/abs/10.1109/MWC.016.2300600"}]

I've found several relevant results on contrastive learning and multi-agent communication training with LLMs. Here are the key findings:

## Contrastive Learning in Multi-Agent Communication

Communication Alignment Contrastive Learning (CACL) is a method where each agent separately uses contrastive learning between their own sent and received messages to learn a communication encoding. Different agents' messages are encodings of different incomplete "views" of the same underlying state, with messages from the same state generally being more similar to each other than to those from distant states or other trajectories.

## Recent 2025 Advances in LLM-Based Multi-Agent Training

Systematic frameworks like OMAC decompose the design and tuning process into functional and structural dimensions, optimizing prompts, agent construction, team selection, dynamic participation, and communication routing through iterative LLM-based contrastive reasoning.

Recent approaches like MAPoRL focus on training entire multi-agent systems using iterative SFT, while MAPoRL employs multi-agent RL to train the whole multi-LLM system.

## Communication Frameworks

Researchers have incorporated LLMs into multi-agent systems where agents collaborate or compete through natural language interactions, with a communication-centric perspective examining key system-level features such as architecture design, communication goals, strategies, paradigms, and content.

Communication paradigms within LLM-MAS include Message Passing (explicit natural language or structured data transmissions between agents), Speech Act mechanisms (where utterances act as commitments, commands, or queries), and Blackboard models (shared memory or context repositories).

These results show active research in 2025 on combining contrastive learning with sender-receiver agent communication frameworks for training collaborative LLM-based multi-agent systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "866b6c79-5eac-4590-9c0d-afbc5535a030",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "4ab5974e-681e-4e04-af7d-6e2a9d4e1ef7",
  "sourceToolAssistantUUID": "866b6c79-5eac-4590-9c0d-afbc5535a030",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T22:15:30.262Z_

<details><summary>↩ Tool result · `toolu_01DeGzZMXD1ARAJjmCBjZ9hL`</summary>

```text
Web search results for query: "MAGE "Pattern Recognition" 2025 graph contrastive learning multi-agent communication reinforcement learning"

Links: [{"title":"Learning multi-agent communication via graph contrastive learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538"},{"title":"Survey on Graph-Based Reinforcement Learning for Networked Coordination and Control","url":"https://www.mdpi.com/2673-4052/6/4/65"},{"title":"MAGE: Meta-Reinforcement Learning for Language Agents toward Strategic Exploration and Exploitation","url":"https://arxiv.org/html/2603.03680v1"},{"title":"Multi-Agent Deep Reinforcement Learning with Contrastive ...","url":"https://www.preprints.org/manuscript/202603.2495"},{"title":"A graph attention network-based multi-agent reinforcement learning framework for robust detection of smart contract vulnerabilities | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-14032-w"},{"title":"MAGE: META-REINFORCEMENT LEARNING FOR ...","url":"https://openreview.net/pdf/d80ccf0395e94992b8cb63a1961d4b4612df0a4e.pdf"},{"title":"Downloads 2024","url":"https://iclr.cc/Downloads/2024"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"GitHub - jwwthu/GNN-Communication-Networks: This is the repository for the collection of Graph-based Deep Learning for Communication Networks. · GitHub","url":"https://github.com/jwwthu/GNN-Communication-Networks"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"}]

Based on the search results, I found information about MAGE and related research in this area. Here are the key findings:

## MAGE: Multi-Agent Communication via Graph Contrastive Learning

MAGE is a multi-agent communication protocol via graph contrastive learning which utilizes contrast objectives to learn optimal message representations, considering feature and topological level.

### Key Characteristics:

**Problem It Addresses:**
Most GNN-based MARL methods simply aggregate features of neighboring agents to obtain message representations, which may not extract enough useful information. MAGE investigates how to extract expressive information from neighboring agents to obtain high-quality message representations.

**Technical Approach:**
In MAGE, two correlated graph views are generated by applying stochastic corruption to the constructed graph. Subsequently, MAGE is trained using a contrastive loss function to enhance the consistency of agent features across these two views.

At the topological level, edges are dynamically removed by assigning higher removal probabilities to less significant edges, thereby emphasizing crucial connectivity structures. At the agent feature level, additional noise is introduced to less critical dimensions of agent features, to prompt agents to discern essential information more effectively.

**Significance:**
MAGE is claimed to be the first to extend graph contrastive learning to MARL, which enables efficient multi-agent communication learning.

The research directly combines the concepts you mentioned: pattern recognition through feature learning, graph-based representations, contrastive learning methodology, multi-agent communication, and reinforcement learning frameworks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb4e2287-46ce-4755-b28f-1cb2328fdd83",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "9fabf789-e30a-4d58-80f2-e900d5a87199",
  "sourceToolAssistantUUID": "cb4e2287-46ce-4755-b28f-1cb2328fdd83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T22:15:35.154Z_

Let me now fetch the MAGE paper details and also check the Social Deduction paper more carefully for the contrastive question.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fabf789-e30a-4d58-80f2-e900d5a87199",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufF2HBA7x6XLfRHx5rh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24dbef55-6089-47df-abaf-73965fe930fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016vVBqVkWQk2AHjHVicmTJ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1857,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 16829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1071,
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

_source line 32 · 2026-05-10T22:15:37.419Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YBstcXb22HNrfUKaWiC2JZ`</summary>

```json
{
  "url": "https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538",
  "prompt": "Extract all details about this paper: title, authors, journal, volume, year, DOI. Is this called MAGE? What does MAGE stand for? Is it about LLM agents or traditional MARL agents? Does it work with language models or with lower-level RL policies? What kind of agents does it train?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24dbef55-6089-47df-abaf-73965fe930fa",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufF2HBA7x6XLfRHx5rh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "463e8d4d-3c18-4971-95dd-9221833ae271",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016vVBqVkWQk2AHjHVicmTJ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1857,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 16829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1071,
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

_source line 33 · 2026-05-10T22:15:37.709Z_

<details><summary>↩ Tool result · reported error · `toolu_01YBstcXb22HNrfUKaWiC2JZ`</summary>

```text
Request failed with status code 403
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "463e8d4d-3c18-4971-95dd-9221833ae271",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "23e4fc86-9388-403f-88c1-a18d59a88759",
  "toolUseResult": "Error: Request failed with status code 403",
  "sourceToolAssistantUUID": "463e8d4d-3c18-4971-95dd-9221833ae271",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-10T22:15:40.769Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011Rhp2w9iB2giKbNHMykrDY`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.06060",
  "prompt": "I need to understand the training methodology in detail. Specifically: 1) How is the listening/receiver component trained? Is it a prediction loss (cross-entropy)? Is it contrastive? 2) How is the speaking/sender component trained? 3) Are both trained jointly or separately? 4) Is there any contrastive objective anywhere in the paper? 5) What exactly is the listening loss function? Look for equations or loss descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23e4fc86-9388-403f-88c1-a18d59a88759",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufF2HBA7x6XLfRHx5rh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b54daae9-fb25-4788-a85c-02282f00a290",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016vVBqVkWQk2AHjHVicmTJ4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1857,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 16829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1071,
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

_source line 35 · 2026-05-10T22:15:41.981Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pg7N5yeukLx3jbQvSEfiyo`</summary>

```json
{
  "query": "\"bilateral contrastive\" OR \"bidirectional contrastive\" \"speaker\" OR \"sender\" \"listener\" OR \"receiver\" language model agent training 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b54daae9-fb25-4788-a85c-02282f00a290",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufF2HBA7x6XLfRHx5rh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e4ce137-0df8-42f7-a134-609c0bbf53ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016vVBqVkWQk2AHjHVicmTJ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1857,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 16829,
      "output_tokens": 433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1071
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1857,
          "output_tokens": 433,
          "cache_read_input_tokens": 16829,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1071,
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

_source line 36 · 2026-05-10T22:15:46.698Z_

<details><summary>↩ Tool result · `toolu_011Rhp2w9iB2giKbNHMykrDY`</summary>

```text
# Training Methodology Analysis

## 1) Listening Component Training

The listening component uses **prediction loss (cross-entropy)**, not contrastive learning. The paper states:

> "LL⁢(π,τti)=−log⁡π(q|τti)"

This is a standard negative log-likelihood loss where the agent predicts the correct imposter identity `q` given the action-observation history.

## 2) Speaking Component Training

Speaking uses **reinforcement learning with a custom reward signal**. The reward measures belief change:

> "rts=Bt−Bt′"

where `Bt` represents the sum of all living crewmates' confidence in voting out the true imposter. Messages that increase team certainty receive positive rewards.

## 3) Joint vs. Separate Training

Both are trained **jointly in a single loss function**:

> "LRL+L+S⁢(π)=LRL+L⁢(π)−𝔼τi∼Π⁢∑t[λS⁢γt⁢rts]"

The combined objective optimizes RL performance, listening accuracy, and speaking effectiveness simultaneously.

## 4) Contrastive Objectives

**No contrastive learning appears in this work.** The paper employs supervised prediction (listening) and reward-based RL (speaking), but no contrastive losses.

## 5) Listening Loss Function Summary

A straightforward supervised learning objective: agents minimize cross-entropy loss when predicting imposter identity from observations and messages, enabling them to extract meaning from communication.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b54daae9-fb25-4788-a85c-02282f00a290",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "9358d60a-b31f-4aaa-bb71-d20503a0cf0f",
  "sourceToolAssistantUUID": "b54daae9-fb25-4788-a85c-02282f00a290",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-10T22:15:49.336Z_

<details><summary>↩ Tool result · `toolu_01Pg7N5yeukLx3jbQvSEfiyo`</summary>

```text
Web search results for query: ""bilateral contrastive" OR "bidirectional contrastive" "speaker" OR "sender" "listener" OR "receiver" language model agent training 2025 2026 arxiv"

Links: [{"title":"arXiv:2503.08842v1 [cs.CL] 11 Mar 2025 Contrastive Speaker-Aware Learning for","url":"https://arxiv.org/pdf/2503.08842"},{"title":"[2503.08842] Contrastive Speaker-Aware Learning for Multi-party Dialogue Generation with LLMs","url":"https://arxiv.org/abs/2503.08842"},{"title":"Contrastive Speaker-Aware Learning for Multi-party Dialogue Generation with LLMs","url":"https://arxiv.org/html/2503.08842v1"},{"title":"Learning Multi-Agent Communication with Contrastive Learning","url":"https://arxiv.org/html/2307.01403"},{"title":"[2108.06209] W2v-BERT: Combining Contrastive Learning and Masked Language Modeling for Self-Supervised Speech Pre-Training","url":"https://arxiv.org/abs/2108.06209"},{"title":"Machine Learning Apr 2025","url":"https://arxiv.org/list/cs.LG/2025-04?show=500&skip=2500"},{"title":"Aligning Backchannel and Dialogue Context Representations via Contrastive LLM Fine-Tuning","url":"https://arxiv.org/html/2604.16622"},{"title":"Learning Speech Representation From Contrastive Token-Acoustic Pretraining","url":"https://arxiv.org/html/2309.00424v5"},{"title":"GitHub - ryanzhumich/Contrastive-Learning-NLP-Papers: Paper List for Contrastive Learning for Natural Language Processing · GitHub","url":"https://github.com/ryanzhumich/Contrastive-Learning-NLP-Papers"},{"title":"Language-Invariant Multilingual Speaker Verification for the TidyVoice 2026 Challenge","url":"https://arxiv.org/html/2603.08092v1"}]

Based on the search results, I found several relevant papers on arxiv from 2025-2026 involving contrastive learning with speaker/listener roles in language models and agents:

## Key Findings:

### 1. **Contrastive Speaker-Aware Learning (March 2025)**

SA-LLM incorporates a speaker-attributed input encoding and a contrastive learning objective to implicitly learn contextual coherence and speaker roles without explicit relation annotations. This paper (arXiv:2503.08842) focuses on multi-party dialogue generation. Extensive experiments on the Ubuntu IRC and Movie Dialogues datasets demonstrate that SA-LLM significantly outperforms state-of-the-art baselines in automatic and human evaluations, achieving superior performance in fluency, coherence, informativeness, and response diversity.

### 2. **Multi-Agent Communication with Contrastive Learning**

Another relevant work discusses multi-agent scenarios: Communication Alignment Contrastive Learning (CACL), where each agent separately uses contrastive learning between their own sent and received messages to learn a communication encoding. This approach frames different agents' views of the same environment state are considered positive samples and messages are contrastively learned as encodings of that state.

### 3. **Backchannel and Dialogue Context (2026)**

A recent paper (from 3 weeks ago, approximately April 2026) addresses "Aligning Backchannel and Dialogue Context Representations via Contrastive LLM Fine-Tuning" (arXiv:2604.16622), which involves speaker-listener interaction dynamics.

These papers align with your search for bilateral/bidirectional contrastive learning approaches involving speaker/sender and listener/receiver roles in language model training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e4ce137-0df8-42f7-a134-609c0bbf53ee",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "0184b057-7c62-48d9-949c-e9e6de8e6676",
  "sourceToolAssistantUUID": "7e4ce137-0df8-42f7-a134-609c0bbf53ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-10T22:15:51.912Z_

Let me do a few more targeted searches to be thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0184b057-7c62-48d9-949c-e9e6de8e6676",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufGRnKgAQcCEtsveLBP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac00b371-1590-4089-b612-b3a5054461ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CuD3qVm8qKBBdheyxvnxP9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3684,
      "cache_read_input_tokens": 17900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3684,
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

_source line 39 · 2026-05-10T22:15:52.862Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SJhRH8NYYuXjNCsHqFAbf2`</summary>

```json
{
  "query": "MAGE \"multi-agent\" \"graph\" \"contrastive\" arxiv paper reinforcement learning communication protocol"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac00b371-1590-4089-b612-b3a5054461ae",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufGRnKgAQcCEtsveLBP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02ece8c1-7aea-4cea-9909-f16a09a72334",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CuD3qVm8qKBBdheyxvnxP9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3684,
      "cache_read_input_tokens": 17900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3684,
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

_source line 40 · 2026-05-10T22:15:53.871Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SGutMSFjr79YUQzGjWg8AS`</summary>

```json
{
  "query": "\"contrastive communication\" LLM agents both sides speaker listener jointly train emergent language 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02ece8c1-7aea-4cea-9909-f16a09a72334",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufGRnKgAQcCEtsveLBP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c90a22a-9287-4d0c-84e8-0f5f09de14ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CuD3qVm8qKBBdheyxvnxP9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3684,
      "cache_read_input_tokens": 17900,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3684,
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

_source line 41 · 2026-05-10T22:16:00.272Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UXEenz531pvwCENYpCMYS4`</summary>

```json
{
  "url": "https://arxiv.org/html/2307.01403v3",
  "prompt": "Is this paper called MAGE? What is the full name? What venue was it published at? Does it operate on LLM agents or traditional MARL? Does it train both sender and receiver with contrastive objectives bilaterally?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c90a22a-9287-4d0c-84e8-0f5f09de14ea",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufGRnKgAQcCEtsveLBP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c7dd3a3d-006a-4bc9-8d8d-94a78e2a056c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CuD3qVm8qKBBdheyxvnxP9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3684,
      "cache_read_input_tokens": 17900,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3684
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 266,
          "cache_read_input_tokens": 17900,
          "cache_creation_input_tokens": 3684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3684,
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

_source line 42 · 2026-05-10T22:16:00.753Z_

<details><summary>↩ Tool result · `toolu_01SJhRH8NYYuXjNCsHqFAbf2`</summary>

```text
Web search results for query: "MAGE "multi-agent" "graph" "contrastive" arxiv paper reinforcement learning communication protocol"

Links: [{"title":"Learning multi-agent communication via graph contrastive learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538"},{"title":"Communication Learning in Multi-Agent Systems from Graph Modeling Perspective","url":"https://arxiv.org/html/2411.00382v1"},{"title":"Learning Multi-Agent Communication with Contrastive Learning","url":"https://arxiv.org/html/2307.01403"},{"title":"Graph Neural Network-based Multi-agent Reinforcement Learning for Resilient Distributed Coordination of Multi-Robot Systems","url":"https://arxiv.org/html/2403.13093v1"},{"title":"Graph Neural Network Meets Multi-Agent Reinforcement Learning: Fundamentals, Applications, and Future Directions","url":"https://arxiv.org/html/2404.04898v1"},{"title":"[2307.01403] Learning Multi-Agent Communication with Contrastive Learning","url":"https://arxiv.org/abs/2307.01403"},{"title":"Learning Communication Skills in Multi-task Multi-agent Deep Reinforcement Learning","url":"https://arxiv.org/html/2511.03348v2"},{"title":"[2302.04094] Learning Graph-Enhanced Commander-Executor for Multi-Agent Navigation","url":"https://arxiv.org/abs/2302.04094"},{"title":"Communication Methods in Multi-Agent Reinforcement Learning","url":"https://www.arxiv.org/pdf/2601.12886"},{"title":"Learning Multi-Agent Communication from Graph Modeling Perspective | OpenReview","url":"https://openreview.net/forum?id=Qox9rO0kN0"}]

Based on the search results, I found a highly relevant paper matching your query:

## MAGE: Multi-Agent Communication via Graph Contrastive Learning

MAGE is a multi-agent communication protocol via graph contrastive learning which utilizes contrast objectives to learn optimal message representations, considering feature and topological level.

### Key Contributions

This work is the first to extend graph contrastive learning to MARL, which enables efficient multi-agent communication learning.

### Methodology

Two correlated graph views are generated by applying stochastic corruption to the constructed graph, and MAGE is trained using a contrastive loss function to enhance the consistency of agent features across these two views.

At the topological level, edges are dynamically removed by assigning higher removal probabilities to less significant edges, thereby emphasizing crucial connectivity structures. At the agent feature level, additional noise is introduced to less critical dimensions of agent features, to prompt agents to discern essential information more effectively.

### Advantages

MAGE learns high-quality feature representations that extract important information at the topological and feature levels through graph contrastive learning, thus facilitating action selection and coordination.

The paper was published in July 2025 on ScienceDirect and addresses the problem of learning effective communication protocols in multi-agent reinforcement learning systems using graph neural networks and contrastive learning techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02ece8c1-7aea-4cea-9909-f16a09a72334",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "d6767f3a-3f51-477e-96d3-8a0f5bd316c0",
  "sourceToolAssistantUUID": "02ece8c1-7aea-4cea-9909-f16a09a72334",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-10T22:16:01.671Z_

<details><summary>↩ Tool result · `toolu_01SGutMSFjr79YUQzGjWg8AS`</summary>

```text
Web search results for query: ""contrastive communication" LLM agents both sides speaker listener jointly train emergent language 2025 2026"

Links: [{"title":"Multi-Agent LLM Systems: From Emergent Collaboration to Structured Collective Intelligence[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202511.1370"},{"title":"LLMs for Multi-Agent Cooperation | Xueguang Lyu","url":"https://xue-guang.com/post/llm-marl/"},{"title":"Multi-Agent Communication Protocols","url":"https://www.emergentmind.com/topics/multi-agent-communication-protocols-d367296e-d465-4280-a30e-43a332a05ba2"},{"title":"Strategic Communication and Language Bias in Multi-Agent LLM Coordination","url":"https://arxiv.org/html/2508.00032"},{"title":"Large Language Models Miss the Multi-Agent Mark","url":"https://arxiv.org/html/2505.21298"},{"title":"Large Language Model Agent: A Survey on Methodology, Applications and Challenges","url":"https://arxiv.org/html/2503.21460v1"},{"title":"Learning Multi-Agent Communication with Contrastive Learning","url":"https://arxiv.org/html/2307.01403"},{"title":"Why do AI agents communicate in human language?","url":"https://arxiv.org/html/2506.02739"},{"title":"[2510.05174] Emergent Coordination in Multi-Agent Language Models","url":"https://arxiv.org/abs/2510.05174"},{"title":"Emergent Coordination in Multi-Agent Language Models","url":"https://arxiv.org/html/2510.05174v1"}]

I've performed a web search for your query on "contrastive communication" with LLM agents, speaker-listener dynamics, and emergent language. Here are the key findings from recent research (2025-2026):

## Contrastive Learning for Multi-Agent Communication

In a method called CACL, different agents' views of the same environment state are considered positive samples and messages are contrastively learned as encodings of that state. To successfully communicate, a speaker and a listener must share a common language with a shared understanding of the symbols being used. Contrastive learning is shown to be a powerful direction for multi-agent communication with fundamental benefits over previous approaches.

## Joint Training and Emergent Language in Multi-Agent Systems

Recent research sketches a research agenda for "multi-agent pretraining", in which agents jointly learn not only language and world models, but also norms of discourse, peer review, and self-correction. LLM-based systems leverage natural language as a universal medium for coordination, enabling unprecedented flexibility and emergent behaviors.

## Emergent Coordination and Both-Sides Interaction

An information-theoretic framework tests whether multi-agent systems show signs of higher-order structure, measuring whether dynamical emergence is present in multi-agent LLM systems and distinguishing spurious temporal coupling from performance-relevant cross-agent synergy.

Communication substantially alters agent behavior: in the Prisoner's Dilemma, communication fosters cooperation and improves outcomes; by contrast, in the Battle of Sexes, a coordination game, communication unexpectedly reduces the level of alignment between agents.

These recent papers highlight active research into how LLM agents can jointly learn communication protocols through contrastive methods and how emergent language properties arise from multi-agent interaction dynamics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c90a22a-9287-4d0c-84e8-0f5f09de14ea",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "a83b6d35-8b2a-473d-b99b-42a6f1ce9fe8",
  "sourceToolAssistantUUID": "8c90a22a-9287-4d0c-84e8-0f5f09de14ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-10T22:16:04.057Z_

<details><summary>↩ Tool result · `toolu_01UXEenz531pvwCENYpCMYS4`</summary>

```text
# Paper Summary

**Not called MAGE.** The paper's full name is **"Learning Multi-Agent Communication with Contrastive Learning"** (arXiv:2307.01403v3).

**Publication venue:** Not explicitly stated in the provided content, though it appears to be an arXiv preprint from February 2024.

**Agent type:** This work focuses on **traditional multi-agent reinforcement learning (MARL)**, not LLM-based agents. The authors develop methods for embodied agents in grid-world environments learning to coordinate through continuous message vectors.

**Training approach:** The method uses a **unilateral contrastive objective on messages**. Each agent independently applies contrastive learning to its own sent and received messages within a trajectory window. The approach treats "messages from the same state as positive samples of each other" to align communication protocols, but this occurs through a single loss function optimized by each agent separately, not through bilateral symmetric training objectives between sender and receiver pairs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7dd3a3d-006a-4bc9-8d8d-94a78e2a056c",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "b074a34b-ce7f-4d42-8b0d-16dfbe448529",
  "sourceToolAssistantUUID": "c7dd3a3d-006a-4bc9-8d8d-94a78e2a056c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-10T22:16:09.643Z_

Now let me get the MAGE paper's arXiv link and confirm its details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b074a34b-ce7f-4d42-8b0d-16dfbe448529",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufHWjWSGFghfQGNcmZG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08044131-6b4e-4cc1-aadb-22bc9e4bdc22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXCgio3ipVqWmtWRL5UKfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2265,
      "cache_read_input_tokens": 21584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2265,
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

_source line 46 · 2026-05-10T22:16:10.645Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C88mzn9HkP5SYqxUH8RMLG`</summary>

```json
{
  "query": "arxiv \"Learning multi-agent communication via graph contrastive learning\" MAGE 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08044131-6b4e-4cc1-aadb-22bc9e4bdc22",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufHWjWSGFghfQGNcmZG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e134f6e-7704-4d02-bd0e-032994ad421b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXCgio3ipVqWmtWRL5UKfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2265,
      "cache_read_input_tokens": 21584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2265,
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

_source line 47 · 2026-05-10T22:16:12.220Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018pVmKT9YuG1NFmd1sHinka`</summary>

```json
{
  "url": "https://arxiv.org/html/2411.00382v1",
  "prompt": "Is this the MAGE paper about graph contrastive learning for multi-agent communication? Extract the title, authors, and whether this is about LLM agents or traditional MARL agents. Does MAGE stand for something specific?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e134f6e-7704-4d02-bd0e-032994ad421b",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufHWjWSGFghfQGNcmZG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7fb742b-40fa-45dc-b99d-d50151425fea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QXCgio3ipVqWmtWRL5UKfN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2265,
      "cache_read_input_tokens": 21584,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2265
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 21584,
          "cache_creation_input_tokens": 2265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2265,
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

_source line 48 · 2026-05-10T22:16:16.353Z_

<details><summary>↩ Tool result · `toolu_018pVmKT9YuG1NFmd1sHinka`</summary>

```text
# Paper Analysis

**This is NOT the MAGE paper you're asking about.**

## Document Details

**Title:** "Communication Learning in Multi-Agent Systems from Graph Modeling Perspective"

**Authors:** Shengchao Hu, Li Shen, Ya Zhang, and Dacheng Tao

**Agent Type:** Traditional MARL (Multi-Agent Reinforcement Learning) agents, not LLM-based agents. The paper focuses on cooperative control in environments like StarCraft II and Google Research Football.

**Method Name:** CommFormer (not MAGE)

## Key Distinction

This paper presents CommFormer, which "treats the communication architecture among agents as a learnable graph" through bi-level optimization. It uses Transformer-based architectures with attention mechanisms for coordination in partially observable environments with bandwidth constraints.

The work addresses *how agents learn communication patterns* rather than graph contrastive learning specifically. While it involves graph modeling, the emphasis is on architecture search for communication graphs during centralized training with distributed execution.

If you're seeking a paper about MAGE (which may stand for a different acronym in graph contrastive learning contexts), this document does not match that description.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7fb742b-40fa-45dc-b99d-d50151425fea",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "4a6f5014-fdd1-4199-9a6b-fb4689b9aba6",
  "sourceToolAssistantUUID": "d7fb742b-40fa-45dc-b99d-d50151425fea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-10T22:16:16.684Z_

<details><summary>↩ Tool result · `toolu_01C88mzn9HkP5SYqxUH8RMLG`</summary>

```text
Web search results for query: "arxiv "Learning multi-agent communication via graph contrastive learning" MAGE 2024 2025"

Links: [{"title":"[2307.01403] Learning Multi-Agent Communication with Contrastive Learning","url":"https://arxiv.org/abs/2307.01403"},{"title":"[2405.08550] Learning Multi-Agent Communication from Graph Modeling Perspective","url":"https://arxiv.org/abs/2405.08550"},{"title":"\\algo: Task-Agnostic Contrastive pre-Training for Inter-Agent Communication","url":"https://arxiv.org/html/2501.02174v1"},{"title":"Communication Learning in Multi-Agent Systems from Graph Modeling Perspective","url":"https://arxiv.org/html/2411.00382v1"},{"title":"Learning Multi-Agent Communication from Graph Modeling Perspective","url":"https://arxiv.org/html/2405.08550v1"},{"title":"Graph-Based Multimodal Contrastive Learning for Chart ...","url":"https://arxiv.org/pdf/2501.04303"},{"title":"[2411.00382] Communication Learning in Multi-Agent Systems from Graph Modeling Perspective","url":"https://arxiv.org/abs/2411.00382"},{"title":"Learning Communication Skills in Multi-task Multi-agent Deep Reinforcement Learning","url":"https://arxiv.org/html/2511.03348v2"},{"title":"G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks","url":"https://arxiv.org/html/2410.11782v1"},{"title":"Learning Multi-Agent Communication from Graph Modeling Perspective | OpenReview","url":"https://openreview.net/forum?id=Qox9rO0kN0"}]

Based on the web search results, I found several relevant papers on multi-agent communication and graph-based approaches. Here are the key findings:

## Related Research Findings

**Paper on Learning Multi-Agent Communication from Graph Modeling Perspective:**
Hu et al. (2024) authored "Learning multi-agent communication from graph modeling perspective," published as arXiv preprint arXiv:2405.08550 (2024). This work conceptualizes the communication structure among agents as a learnable graph and formulates the problem as determining the communication graph while enabling architecture parameters to update normally through a bi-level optimization process, relaxing the search space into a continuous domain for gradient descent optimization.

**Related Work on Contrastive Learning for Communication:**
One related approach proposes to learn to communicate using contrastive learning to maximize the mutual information between messages of a given trajectory.

**Recent Multi-Agent Communication Research:**
More recent work (2025) introduces TACTIC (Task-Agnostic Contrastive pre-Training for Inter-Agent Communication), which operates through offline contrastive pretraining where contrastive learning is applied to an offline dataset to pretrain communication modules, followed by online policy integration where pre-trained modules are frozen and incorporated into agents' online learning.

The search results show several papers addressing multi-agent communication, particularly combining graph modeling and contrastive learning approaches, though I didn't find a paper with the exact title "Learning multi-agent communication via graph contrastive learning" with the acronym MAGE in the 2024-2025 timeframe.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e134f6e-7704-4d02-bd0e-032994ad421b",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "32c4b01c-19be-4420-83d9-7e1072f31a9e",
  "sourceToolAssistantUUID": "5e134f6e-7704-4d02-bd0e-032994ad421b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-10T22:16:20.963Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N5vYaYxJpYb7qZxRv7VrrH`</summary>

```json
{
  "query": "MAGE \"multi-agent graph\" OR \"graph contrastive\" communication reinforcement learning Pattern Recognition journal 2025 ScienceDirect arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32c4b01c-19be-4420-83d9-7e1072f31a9e",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufJSjRuVDBiQtBwvRp9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08891dc6-f264-4fe2-b107-d0ccd1b53230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCGc6CZdKJWX6ongZZqcsk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 292,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 23849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1037,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-10T22:16:21.346Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01778o4sG4zbxgPmgam8rRSN`</summary>

```json
{
  "query": "site:arxiv.org \"MAGE\" multi-agent communication graph contrastive learning message representation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08891dc6-f264-4fe2-b107-d0ccd1b53230",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufJSjRuVDBiQtBwvRp9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f376739-40d0-44fb-a6ac-a041243eed6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DCGc6CZdKJWX6ongZZqcsk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 292,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 23849,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 292,
          "output_tokens": 141,
          "cache_read_input_tokens": 23849,
          "cache_creation_input_tokens": 1037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1037,
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

_source line 52 · 2026-05-10T22:16:27.911Z_

<details><summary>↩ Tool result · `toolu_01N5vYaYxJpYb7qZxRv7VrrH`</summary>

```text
Web search results for query: "MAGE "multi-agent graph" OR "graph contrastive" communication reinforcement learning Pattern Recognition journal 2025 ScienceDirect arxiv"

Links: [{"title":"Learning multi-agent communication via graph contrastive learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538"},{"title":"Multi-Agent Communication with Information Preserving ...","url":"https://www.ijcai.org/proceedings/2025/0008.pdf"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"Influence Enhanced Sparse Coordination Graphs for Multi-Agent Reinforcement Learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608025003338"},{"title":"Survey on Graph-Based Reinforcement Learning for Networked Coordination and Control","url":"https://www.mdpi.com/2673-4052/6/4/65"},{"title":"Learning Communication Skills in Multi-task Multi-agent Deep Reinforcement Learning","url":"https://arxiv.org/html/2511.03348v2"},{"title":"GitHub - LantaoYu/MARL-Papers: Paper list of multi-agent reinforcement learning (MARL) · GitHub","url":"https://github.com/LantaoYu/MARL-Papers"},{"title":"MAGE: Meta-Reinforcement Learning for Language Agents toward Strategic Exploration and Exploitation","url":"https://arxiv.org/html/2603.03680v1"},{"title":"MAGE: META-REINFORCEMENT LEARNING FOR ...","url":"https://openreview.net/pdf/d80ccf0395e94992b8cb63a1961d4b4612df0a4e.pdf"},{"title":"A survey of multi-agent deep reinforcement learning with communication | Autonomous Agents and Multi-Agent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10458-023-09633-6"}]

Based on the web search results, I found relevant information about your query. The primary result is from **ScienceDirect**:

## Key Finding

A paper titled "Learning multi-agent communication via graph contrastive learning (MAGE)" proposes a multi-agent communication protocol that utilizes contrast objectives to learn optimal message representations, considering feature and topological level.

## Details about MAGE

Communication learning has emerged as a successful tool for tackling complex tasks in multi-agent reinforcement learning (MARL), with many MARL methods using graph neural networks (GNNs) to build a communication learning framework where agents and communication channels can be represented as nodes and edges in a graph.

In MAGE, two correlated graph views are generated by applying stochastic corruption to the constructed graph, and the method is trained using a contrastive loss function to enhance the consistency of agent features across these two views.

At the topological level, edges are dynamically removed by assigning higher removal probabilities to less significant edges, and at the agent feature level, additional noise is introduced to less critical dimensions of agent features.

The paper was published on **ScienceDirect** in July 2025, matching your search criteria for Pattern Recognition journal publications on this topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08891dc6-f264-4fe2-b107-d0ccd1b53230",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "43fd8b14-882e-41cb-97c7-4ddb07e8ef67",
  "sourceToolAssistantUUID": "08891dc6-f264-4fe2-b107-d0ccd1b53230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-10T22:16:28.646Z_

<details><summary>↩ Tool result · `toolu_01778o4sG4zbxgPmgam8rRSN`</summary>

```text
Web search results for query: "site:arxiv.org "MAGE" multi-agent communication graph contrastive learning message representation"

Links: [{"title":"[2307.01403] Learning Multi-Agent Communication with Contrastive Learning","url":"https://arxiv.org/abs/2307.01403"},{"title":"\\algo: Task-Agnostic Contrastive pre-Training for Inter-Agent Communication","url":"https://arxiv.org/html/2501.02174"},{"title":"Learning Multi-Agent Communication with Contrastive Learning","url":"https://arxiv.org/html/2307.01403v3"},{"title":"Communication Learning in Multi-Agent Systems from Graph Modeling Perspective","url":"https://arxiv.org/html/2411.00382v1"},{"title":"[2405.08550] Learning Multi-Agent Communication from Graph Modeling Perspective","url":"https://arxiv.org/abs/2405.08550"},{"title":"Learning Multi-Agent Communication from Graph Modeling Perspective","url":"https://arxiv.org/html/2405.08550v1"},{"title":"[2411.00382] Communication Learning in Multi-Agent Systems from Graph Modeling Perspective","url":"https://arxiv.org/abs/2411.00382"},{"title":"Graph Neural Network Meets Multi-Agent Reinforcement Learning: Fundamentals, Applications, and Future Directions","url":"https://arxiv.org/html/2404.04898v1"},{"title":"Language Grounded Multi-agent Communication for Ad-hoc Teamwork","url":"https://arxiv.org/html/2409.17348v1"},{"title":"CLEAR: Context Augmentation from Contrastive Learning of Experience via Agentic Reflection","url":"https://arxiv.org/html/2604.07487"}]

Based on the search results, I found several relevant papers on arXiv related to multi-agent communication, graph-based approaches, and contrastive learning. Here are the key findings:

## Relevant Papers Found:

1. **Learning Multi-Agent Communication with Contrastive Learning** (2307.01403)
   - The work introduces an alternative perspective where communicative messages sent between agents are considered as different incomplete views of the environment state, and proposes to learn to communicate using contrastive learning to maximize the mutual information between messages of a given trajectory.
   - The method is called Communication Alignment Contrastive Learning (CACL), where each agent separately uses contrastive learning between their own sent and received messages to learn a communication encoding.

2. **Learning Multi-Agent Communication from Graph Modeling Perspective** (2405.08550 / 2411.00382)
   - The work conceptualizes the communication structure among agents as a learnable graph and formulates this problem as the task of determining the communication graph while enabling the architecture parameters to update normally, thus necessitating a bi-level optimization process.
   - The proposed approach, CommFormer, efficiently optimizes the communication graph and concurrently refines architectural parameters through gradient descent in an end-to-end manner.

3. **Task-Agnostic Contrastive pre-Training for Inter-Agent Communication** (2501.02174)
   - The communication mechanism encodes messages and integrates them with local observations, generating representations grounded in the global state using contrastive learning.

These papers address multi-agent communication, graph structures, and contrastive learning approaches for message representation, though I did not find a specific paper titled or abbreviated as "MAGE" in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f376739-40d0-44fb-a6ac-a041243eed6f",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "011c4060-c753-4792-a85b-4afb342b07b7",
  "sourceToolAssistantUUID": "6f376739-40d0-44fb-a6ac-a041243eed6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-10T22:16:31.184Z_

Let me get the exact publication details of the MAGE paper from Pattern Recognition.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "011c4060-c753-4792-a85b-4afb342b07b7",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufKKrxWfJ8KDEnpgzgK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35522f63-7412-4797-a54c-772c73fcdba8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W7amgnrwop6ALgwCbiTi9g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2165,
      "cache_read_input_tokens": 24886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2165,
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

_source line 55 · 2026-05-10T22:16:32.138Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FgiNmiu9iVJupyGVGL1nUj`</summary>

```json
{
  "query": "\"Learning multi-agent communication via graph contrastive learning\" MAGE authors Pattern Recognition 2025 DOI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35522f63-7412-4797-a54c-772c73fcdba8",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufKKrxWfJ8KDEnpgzgK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bea12a89-2959-489d-a279-d71bd14da8e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W7amgnrwop6ALgwCbiTi9g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2165,
      "cache_read_input_tokens": 24886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2165,
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

_source line 56 · 2026-05-10T22:16:32.925Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SwCqsCamRy5mVHYsUWapQy`</summary>

```json
{
  "query": "MAPoRL arxiv 2502.18439 contrastive loss generation comprehension co-training methodology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bea12a89-2959-489d-a279-d71bd14da8e1",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufKKrxWfJ8KDEnpgzgK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a57b554b-f446-4154-9a00-44ceb2f799be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W7amgnrwop6ALgwCbiTi9g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2165,
      "cache_read_input_tokens": 24886,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2165
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 24886,
          "cache_creation_input_tokens": 2165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2165,
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

_source line 57 · 2026-05-10T22:16:36.775Z_

<details><summary>↩ Tool result · `toolu_01FgiNmiu9iVJupyGVGL1nUj`</summary>

```text
Web search results for query: ""Learning multi-agent communication via graph contrastive learning" MAGE authors Pattern Recognition 2025 DOI"

Links: [{"title":"Learning multi-agent communication via graph contrastive learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538"},{"title":"Multi-Agent Communication with Information Preserving ...","url":"https://www.ijcai.org/proceedings/2025/0008.pdf"},{"title":"Learning Multi-Agent Communication from Graph Modeling Perspective | OpenReview","url":"https://openreview.net/forum?id=Qox9rO0kN0"},{"title":"[2405.08550] Learning Multi-Agent Communication from Graph Modeling Perspective","url":"https://arxiv.org/abs/2405.08550"},{"title":"Learning Multi-Agent Communication from Graph Modeling Perspective","url":"https://arxiv.org/html/2405.08550v1"},{"title":"Communication Learning in Multi-Agent Systems from Graph Modeling Perspective","url":"https://arxiv.org/html/2411.00382v1"},{"title":"[2411.00382] Communication Learning in Multi-Agent Systems from Graph Modeling Perspective","url":"https://arxiv.org/abs/2411.00382"},{"title":"Graph-Based Multimodal Contrastive Learning for Chart ...","url":"https://arxiv.org/pdf/2501.04303"},{"title":"A survey of multi-agent deep reinforcement learning with communication | Autonomous Agents and Multi-Agent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10458-023-09633-6"},{"title":"A unified multimodal GenAI platform integrating GraphRAG multi-agent systems and custom language models for intelligent document processing and knowledge synthesis | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-47145-x"}]

Based on the search results, I found information about the MAGE paper. The paper proposes a multi-agent communication protocol via graph contrastive learning (MAGE), which utilizes contrast objectives to learn optimal message representations, considering feature and topological level.

MAGE is trained using a contrastive loss function to enhance the consistency of agent features across different graph views.

The paper appears to be published in Pattern Recognition in 2025. Based on the ScienceDirect source URL, the DOI appears to be related to article pii/S0031320325007538, though the complete DOI in standard format is not explicitly shown in the search results. You may want to access the ScienceDirect link directly to confirm the full DOI and author information for proper citation purposes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bea12a89-2959-489d-a279-d71bd14da8e1",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "f0becb4e-dd35-4ff7-aace-a8fb32cb97f1",
  "sourceToolAssistantUUID": "bea12a89-2959-489d-a279-d71bd14da8e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-10T22:16:40.342Z_

<details><summary>↩ Tool result · `toolu_01SwCqsCamRy5mVHYsUWapQy`</summary>

```text
Web search results for query: "MAPoRL arxiv 2502.18439 contrastive loss generation comprehension co-training methodology"

Links: [{"title":"[2502.18439] MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning","url":"https://arxiv.org/abs/2502.18439"},{"title":"MAPoRL: Multi-Agent Post-Co-Training for Collaborative ...","url":"https://arxiv.org/pdf/2502.18439"},{"title":"[2502.18439v1] MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning","url":"http://arxiv.org/abs/2502.18439v1"},{"title":"MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/resources/2502.18439v1"},{"title":"[PDF] MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MAPoRL:-Multi-Agent-Post-Co-Training-for-Large-with-Park-Han/aa89c6bf86486e180833037333555e3492b15c8e"},{"title":"(PDF) MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning","url":"https://www.researchgate.net/publication/389351067_MAPoRL_Multi-Agent_Post-Co-Training_for_Collaborative_Large_Language_Models_with_Reinforcement_Learning"},{"title":"\\ours\\faIconcanadian-maple-leaf: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning","url":"https://arxiv.org/html/2502.18439"},{"title":"dblp: MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning.","url":"https://dblp.org/rec/journals/corr/abs-2502-18439.html"},{"title":"[2602.18439] Replication Study: Federated Text-Driven Prompt Generation for Vision-Language Models","url":"https://arxiv.org/abs/2602.18439"},{"title":"[2506.18439] Computational Complexity of Model-Checking Quantum Pushdown Systems","url":"https://arxiv.org/abs/2506.18439"}]

Based on the search results, I found detailed information about the paper MAPoRL (arxiv 2502.18439). Here's what the paper covers:

## Overview

MAPoRL (Multi-Agent Post-co-training for collaborative LLMs with Reinforcement Learning) is a new post-training paradigm to explicitly elicit the collaborative behaviors and further unleash the power of multi-agentic LLM frameworks.

## Core Methodology

In MAPoRL, multiple LLMs first generate their own responses independently and engage in a multi-turn discussion to collaboratively improve the final answer. A MAPoRL verifier evaluates both the answer and the discussion, by assigning a score that verifies the correctness of the answer, while adding incentives to encourage corrective and persuasive discussions.

## Co-training Approach

The score serves as the co-training reward, and is then maximized through multi-agent RL. Unlike existing LLM post-training paradigms, MAPoRL advocates the co-training of multiple LLMs together using RL for better generalization.

## Key Findings

Experiments demonstrate that training individual LLMs alone is insufficient to induce effective collaboration. In contrast, multi-agent co-training can boost the collaboration performance across benchmarks, with generalization to unseen domains.

The paper was submitted on February 25, 2025, and is authored by Chanwoo Park, Seungju Han, Xingzhi Guo, Asuman Ozdaglar, Kaiqing Zhang, and Joo-Kyung Kim.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a57b554b-f446-4154-9a00-44ceb2f799be",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "a5ce2296-f03c-4343-b49b-56ea2ef7097d",
  "sourceToolAssistantUUID": "a57b554b-f446-4154-9a00-44ceb2f799be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-10T22:16:45.553Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PT9Rp83Gm7ABsocUj6d6wR`</summary>

```json
{
  "url": "https://arxiv.org/html/2502.18439",
  "prompt": "I need to understand the training methodology in detail. Specifically: 1) Does this paper co-train generation and comprehension as separate skills, or does it co-train multiple agents? 2) Is there any contrastive loss or contrastive objective? 3) What losses/objectives are used? Look for the loss function equations. 4) Does it train agents to both speak and listen, or just to collaboratively discuss?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5ce2296-f03c-4343-b49b-56ea2ef7097d",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufLBsXR4zZHeKDZcDu2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4838313e-422a-47ca-96ac-cbc6e2b908db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PxSRRxwXMn4ssAtBeTFuHP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1860,
      "cache_read_input_tokens": 27051,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1860
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 174,
          "cache_read_input_tokens": 27051,
          "cache_creation_input_tokens": 1860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1860,
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

_source line 60 · 2026-05-10T22:16:52.279Z_

<details><summary>↩ Tool result · `toolu_01PT9Rp83Gm7ABsocUj6d6wR`</summary>

```text
# MAPoRL Training Methodology Analysis

## 1) Co-training Focus: Multiple Agents, Not Generation/Comprehension Skills

This paper co-trains **multiple LLM agents simultaneously** rather than separating generation and comprehension as distinct skills. The authors explicitly state: "Unlike existing LLM post-training paradigms, MAPoRL advocates the co-training of multiple LLMs together using RL for better generalization."

The framework trains agents to engage in collaborative debate across multiple turns, where each agent generates responses conditioned on previous discussion history from all participants.

## 2) No Contrastive Loss Present

The paper does **not employ contrastive objectives**. Instead, it relies on verifier-based reward signals and standard RL loss functions.

## 3) Loss Functions Used

The primary objective combines two components:

- **PPO Surrogate Loss**: "min(Rt^x A(it^x;θ_old,θ_old,vta), clip_ϵ(Rt^x)A(...))" for policy optimization
- **Value Loss**: "λ_value(V(it^x;θ_vta)−V^target_ta(it^x))²" for value function training
- **KL Regularization**: "−λ_KL KL(LLM_θref,ta||LLM_θta)" to prevent divergence from reference models

No contrastive or comparative losses between agents appear in the formulation.

## 4) Training Focus: Collaborative Discussion, Not Separate Skills

Agents train to "collaboratively improve the final answer" through multi-turn interactions. The framework emphasizes that agents must learn both to "speak persuasively" and "listen strategically" within the debate context, not as separated skill components but as integrated collaborative behaviors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4838313e-422a-47ca-96ac-cbc6e2b908db",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "ad679632efe395930",
  "type": "user",
  "uuid": "4f9cc14c-55c1-4053-ab0b-03ddef36dc8a",
  "sourceToolAssistantUUID": "4838313e-422a-47ca-96ac-cbc6e2b908db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-10T22:17:38.836Z_

Now I have comprehensive information on all four questions. Here is my complete report.

---

## 1. MAPoRL (ACL 2025) -- arXiv 2502.18439

**Title:** "Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning"
**Authors:** Chanwoo Park, Seungju Han, Xingzhi Guo, Asuman E. Ozdaglar, Kaiqing Zhang, Joo-Kyung Kim
**Venue:** ACL 2025, Vienna, Austria (pages 30215-30248)

**Does it co-train generation and comprehension?**
No. The "co-training" in MAPoRL refers to training **multiple LLM agents together simultaneously**, not co-training generation and comprehension as separate skills. Multiple LLMs generate their own responses independently, then engage in multi-turn discussion to collaboratively improve a final answer. The focus is on collaborative debate behavior, not on separating generation from comprehension.

**Does it use contrastive objectives?**
No. MAPoRL uses **no contrastive objectives whatsoever**. Its training signal comes from a verifier that assigns a score evaluating both the final answer's correctness and the quality of the discussion (rewarding corrective and persuasive exchanges). This score is maximized via multi-agent RL using PPO with a KL regularization term against reference models and a value function loss. There are no contrastive or comparative losses between agents.

---

## 2. Social Deduction LLM (AAMAS 2025) -- arXiv 2502.06060

**Title:** "Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning"
**Authors:** Bidipta Sarkar, Warren Xia, C. Karen Liu, Dorsa Sadigh
**Venue:** AAMAS 2025, Detroit, Michigan

**Does it train receiver-side listening loss?**
Yes. The paper explicitly decomposes communication into **listening** and **speaking** skills and trains both. The listening loss is a standard supervised **cross-entropy/negative log-likelihood loss**: `L_L(pi, tau) = -log pi(q | tau)`, where the agent predicts the identity of the imposter `q` given its action-observation history including discussion messages. This serves as a dense reward signal to guide communication learning.

**Is it task-specific (Among Us)?**
Yes. The paper studies an embodied social deduction game **based on Among Us**, where agents must identify an adversarial imposter through natural language discussion. It is task-specific to this Among Us-inspired setting.

**Is it non-contrastive?**
Yes, it is entirely **non-contrastive**. The listening component uses supervised prediction (cross-entropy), and the speaking component uses reinforcement learning with a reward based on belief change (`r_s = B_t - B_t'`, measuring how much a message increases crewmates' confidence in voting out the true imposter). Both are trained jointly in a single combined loss. No contrastive objectives appear anywhere in the paper.

---

## 3. Bilateral/Bidirectional Contrastive Training of Both Sender and Receiver in LLM Agents (2025-2026)

After extensive searching, **I did not find any paper from 2025-2026 that performs bilateral or bidirectional contrastive training of both sender and receiver communication specifically in LLM agents.** Here is what the closest related work looks like:

- **CACL (Communication Alignment Contrastive Learning)** from "Learning Multi-Agent Communication with Contrastive Learning" (Lo et al., ICLR 2024, arXiv 2307.01403): This uses contrastive learning for multi-agent communication, treating different agents' messages about the same state as positive pairs. However, it operates on **traditional MARL agents** (not LLMs), uses continuous message vectors (not natural language), and applies a **unilateral** contrastive objective -- each agent independently applies contrastive learning to its own messages, not a bilateral sender-receiver contrastive objective.

- **TACTIC** (arXiv 2501.02174, 2025): Task-Agnostic Contrastive pre-Training for Inter-Agent Communication. Uses offline contrastive pretraining for communication modules, but again operates on traditional MARL, not LLM agents.

- **SA-LLM** (arXiv 2503.08842, March 2025): "Contrastive Speaker-Aware Learning for Multi-party Dialogue Generation with LLMs" -- uses contrastive learning to learn speaker roles in multi-party dialogue, but this is about dialogue generation quality, not multi-agent communication protocol training between sender and receiver.

- The Social Deduction paper (2502.06060) trains both speaker and listener but is **non-contrastive**.

**Bottom line:** No paper was found that does bilateral contrastive training of both sender and receiver communication in LLM-based multi-agent systems from 2025-2026. This appears to be a gap in the literature.

---

## 4. MAGE (Pattern Recognition 2025) -- Graph Contrastive Learning for Multi-Agent Communication

**Title:** "Learning multi-agent communication via graph contrastive learning"
**Journal:** Pattern Recognition (Elsevier/ScienceDirect), published July 2025
**ScienceDirect:** [S0031320325007538](https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538)

**What MAGE does:** MAGE is a multi-agent communication protocol that uses graph contrastive learning to learn high-quality message representations. It generates two correlated graph views by applying stochastic corruption to a communication graph, then trains with a contrastive loss to enhance consistency of agent feature representations across these views. It operates at two levels:
- **Topological level:** Dynamically removes edges (higher removal probability for less significant edges)
- **Feature level:** Introduces noise to less critical dimensions of agent features

**Is it relevant as a missing citation?** This depends on what paper you are comparing it to, but here are the key limitations of its relevance:

1. **MAGE operates on traditional MARL agents, NOT LLM agents.** It works with continuous observation/action spaces and learned message vectors in cooperative control environments (e.g., StarCraft-style tasks), not with natural language communication between language models.

2. **MAGE's contrastive objective is about learning better message representations through graph augmentation**, not about bilateral sender-receiver contrastive training. It contrasts different augmented views of the same communication graph, not sender vs. receiver perspectives.

3. **It does not train both sender and receiver with contrastive objectives bilaterally.** The contrastive loss operates on graph-level representations.

If your paper concerns contrastive training of LLM agents' communication (both generation and comprehension of natural language messages), MAGE operates in a fundamentally different domain (traditional MARL with continuous messages, graph-based representation learning). It would be relevant primarily as a "contrastive learning has been used in multi-agent communication" background citation, but not as a directly comparable or competing approach for LLM-based bilateral contrastive communication training.

---

Sources:
- [MAPoRL -- ACL Anthology](https://aclanthology.org/2025.acl-long.1459/)
- [MAPoRL -- arXiv 2502.18439](https://arxiv.org/abs/2502.18439)
- [Social Deduction LLM -- arXiv 2502.06060](https://arxiv.org/abs/2502.06060)
- [MAGE -- ScienceDirect (Pattern Recognition 2025)](https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538)
- [CACL -- arXiv 2307.01403 (ICLR 2024)](https://arxiv.org/abs/2307.01403)
- [TACTIC -- arXiv 2501.02174](https://arxiv.org/html/2501.02174)
- [SA-LLM -- arXiv 2503.08842](https://arxiv.org/abs/2503.08842)
- [Adapting LLM Agents Through Communication -- ICLR 2024](https://openreview.net/forum?id=wOelVq8fwL)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f9cc14c-55c1-4053-ab0b-03ddef36dc8a",
  "isSidechain": true,
  "agentId": "ad679632efe395930",
  "requestId": "req_011CaufM4ypK9xPGa7hePVfC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45f44fcf-6dc5-4a52-8219-d5e1f733c30f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013DW2Cs2kTCuFnyh2bEPN9M",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 593,
      "cache_read_input_tokens": 28911,
      "output_tokens": 1990,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 593
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1990,
          "cache_read_input_tokens": 28911,
          "cache_creation_input_tokens": 593,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 593,
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
