# Research conversation: I'm reviewing a paper proposal about using reconstruction-based auxiliary losses for training text-based communication i

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-adc656e1cd45fd18f.jsonl`
- **Structured JSON:** [`7981d95af623f65a58d6.json`](../../sessions/79/7981d95af623f65a58d6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

59 recorded events

### User

_source line 1 · 2026-05-10T20:19:53.099Z_

I'm reviewing a paper proposal about using reconstruction-based auxiliary losses for training text-based communication in multi-agent LLM systems. The method is called "Stop-Gradient Intent Reconstruction (SGIR)" — it reconstructs the sender's hidden-state intent embedding from text messages using an MLP decoder, with EMA target stabilization and stop-gradient detachment, as an auxiliary loss during multi-agent GRPO training.

Your job: find competing or closely related work the proposal might have missed. Search for:

1. "auxiliary loss communication multi-agent LLM 2025 2026" — any auxiliary losses for training agent communication
2. "reconstruction loss multi-agent communication language model" — reconstruction-based approaches 
3. "intent reconstruction agent communication" — similar framing
4. "dense supervision agent communication reinforcement learning" — dense signal approaches
5. "stop gradient multi-agent communication" — stop-gradient in MARL communication
6. "EMA target reinforcement learning auxiliary loss" — EMA stabilization in RL
7. "text communication training multi-agent reinforcement learning LLM 2026" — general area
8. "ThoughtComm NeurIPS 2025" — verify this paper and check how it relates
9. "Social Deduction LLM AAMAS 2025 multi-agent RL" — verify and check relevance

For each paper found, note: title, venue, year, and how it relates to SGIR. Focus especially on papers from 2025-2026 that might be concurrent work.

Use WebSearch. Report concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "02fe5d5d-5e67-46e7-a10a-f0b13b18116c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T20:19:53.119Z_

```json
{
  "parentUuid": "02fe5d5d-5e67-46e7-a10a-f0b13b18116c",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
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
  "uuid": "e02e9756-4f24-4ee5-a0cf-e548549b1577",
  "timestamp": "2026-05-10T20:19:53.119Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T20:19:55.608Z_



I'll search for competing and related work across all these queries. Let me start by loading the WebSearch tool schema.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e02e9756-4f24-4ee5-a0cf-e548549b1577",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWRf11pR9WEVdywy5g1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "235f2960-ca9d-4941-96d1-baa302b89f56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SbsjSWVrLtRkhZpUuUpKgo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 904,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 904,
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

_source line 4 · 2026-05-10T20:19:55.879Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01B2cyC3jp1Ke2aB8T2k2tVM`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "235f2960-ca9d-4941-96d1-baa302b89f56",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWRf11pR9WEVdywy5g1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e178efde-67d1-437a-b3a6-70e331853685",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SbsjSWVrLtRkhZpUuUpKgo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 904,
      "cache_read_input_tokens": 8223,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 904
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 101,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 904,
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

_source line 5 · 2026-05-10T20:19:55.885Z_

<details><summary>↩ Tool result · `toolu_01B2cyC3jp1Ke2aB8T2k2tVM`</summary>

````text
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
  "parentUuid": "e178efde-67d1-437a-b3a6-70e331853685",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "4e06b90b-9dfc-473d-80eb-5a9adcf18b2f",
  "sourceToolAssistantUUID": "e178efde-67d1-437a-b3a6-70e331853685",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T20:19:58.342Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e06b90b-9dfc-473d-80eb-5a9adcf18b2f",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWRsBzLSgb6345aXED3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "caf77a85-2dc0-4194-9eb7-a1a7c44f2400",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERrpJZspGa9HRJPbg9sWP6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 7 · 2026-05-10T20:19:58.888Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YZ1WwoAcq5oxjkuyb7xi29`</summary>

```json
{
  "query": "auxiliary loss communication multi-agent LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caf77a85-2dc0-4194-9eb7-a1a7c44f2400",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWRsBzLSgb6345aXED3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52e78b80-4f1e-4cc3-8e02-6d54b2bf0722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERrpJZspGa9HRJPbg9sWP6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 8 · 2026-05-10T20:19:59.417Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MAB8h9wH8kkV2YhUYPEmPJ`</summary>

```json
{
  "query": "reconstruction loss multi-agent communication language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52e78b80-4f1e-4cc3-8e02-6d54b2bf0722",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWRsBzLSgb6345aXED3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "811df0bc-5b02-443e-950f-271d72b719e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERrpJZspGa9HRJPbg9sWP6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 9 · 2026-05-10T20:19:59.891Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KkwrpFGzuhQCdco1hZadMN`</summary>

```json
{
  "query": "intent reconstruction agent communication reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "811df0bc-5b02-443e-950f-271d72b719e0",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWRsBzLSgb6345aXED3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d445e1d8-3c4f-4d95-8e20-dd693214f048",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERrpJZspGa9HRJPbg9sWP6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 10 · 2026-05-10T20:20:00.362Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BBVDHv649GA9SRu2vVzCv5`</summary>

```json
{
  "query": "dense supervision agent communication reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d445e1d8-3c4f-4d95-8e20-dd693214f048",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWRsBzLSgb6345aXED3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a518b8c5-8b33-4669-a659-ee07cc819d85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERrpJZspGa9HRJPbg9sWP6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1418,
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

_source line 11 · 2026-05-10T20:20:00.822Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011uDup8jX5VnWhJHME9YTN6`</summary>

```json
{
  "query": "stop gradient multi-agent communication reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a518b8c5-8b33-4669-a659-ee07cc819d85",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWRsBzLSgb6345aXED3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "961564c2-6c98-4d79-b060-f905ac202386",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERrpJZspGa9HRJPbg9sWP6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 9127,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1418
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 245,
          "cache_read_input_tokens": 9127,
          "cache_creation_input_tokens": 1418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1418,
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

_source line 12 · 2026-05-10T20:20:06.091Z_

<details><summary>↩ Tool result · `toolu_01YZ1WwoAcq5oxjkuyb7xi29`</summary>

```text
Web search results for query: "auxiliary loss communication multi-agent LLM 2025 2026"

Links: [{"title":"Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems | OpenReview","url":"https://openreview.net/forum?id=LkzuPorQ5L"},{"title":"Frontiers | Auto-scaling LLM-based multi-agent systems through dynamic integration of agents","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1638227/full"},{"title":"WMAC 2026: AAAI 2026 Bridge Program on Advancing LLM-Based Multi-Agent Collaboration","url":"https://multiagents.org/workshop/"},{"title":"On the Resilience of LLM-Based Multi-Agent Collaboration with Faulty Agents | OpenReview","url":"https://openreview.net/forum?id=bkiM54QftZ"},{"title":"Multi-agent LLMs in 2026 [+frameworks] | SuperAnnotate","url":"https://www.superannotate.com/blog/multi-agent-llms"},{"title":"Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering","url":"https://arxiv.org/html/2604.08224v1"},{"title":"LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision, and the Road Ahead | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3712003"},{"title":"Multi-Agent AI Systems: Why They Fail and How to Fix Coordination Issues (2026) | Augment Code","url":"https://www.augmentcode.com/guides/why-multi-agent-llm-systems-fail-and-how-to-fix-them"},{"title":"LLMs and Multi-Agent Systems: The Future of AI in 2025","url":"https://www.classicinformatics.com/blog/how-llms-and-multi-agent-systems-work-together-2025"},{"title":"Multi-Agent Multi-LLM Systems: The Future of AI Architecture (Complete Guide 2026) · Technical news about AI, coding and all","url":"https://dasroot.net/posts/2026/02/multi-agent-multi-llm-systems-future-ai-architecture-guide-2026/"}]

Based on the search results, here's what I found about auxiliary loss communication in multi-agent LLM systems for 2025-2026:

## Key Findings

**Communication Efficiency & Optimization:**
Recent advancements in LLM-powered agents show that collective intelligence can significantly outperform individual capabilities, though existing multi-agent pipelines introduce substantial token overhead and economic costs. To address this, researchers propose frameworks that can prune redundant or even malicious communication messages.

**Coordination and Communication Challenges:**
The MAST Failure Taxonomy identifies coordination failures accounting for 36.94% of failures, involving communication breakdowns, state synchronization issues, and conflicting objectives across 1,600+ execution traces. Multi-agent LLM systems fail at rates between 41-86.7% in production because specification ambiguity and unstructured coordination protocols cause agents to misinterpret roles, duplicate work, and skip verification.

**Protocol Standards:**
The Model Context Protocol (MCP) provides a structured way for agents to access external tools and data sources, with MCP highlighted as a must-have for enterprise-level AI agent deployment in 2026, and the latest MCP version 2.1 introducing enhanced permission verification, real-time data access, and secure API integration.

**Communication Infrastructure:**
New approaches could refine communication with LLM-based agents, reducing misinterpretation and significantly enhancing overall performance, with explicit definition of agent behaviors and communication patterns reducing ambiguity and improving task execution.

The research suggests that while auxiliary losses for communication optimization aren't explicitly highlighted in these results, the focus has shifted toward standardized communication protocols and structured coordination mechanisms to reduce failures in multi-agent systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52e78b80-4f1e-4cc3-8e02-6d54b2bf0722",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "6232d7c9-9b96-492a-9788-37d41d08225a",
  "sourceToolAssistantUUID": "52e78b80-4f1e-4cc3-8e02-6d54b2bf0722",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T20:20:06.519Z_

<details><summary>↩ Tool result · `toolu_01MAB8h9wH8kkV2YhUYPEmPJ`</summary>

```text
Web search results for query: "reconstruction loss multi-agent communication language model"

Links: [{"title":"A Framework for Studying Communication Pathways in Machine","url":"https://www.scitepress.org/Papers/2024/124235/124235.pdf"},{"title":"Full article: Generative emergent communication: large language model is a collective world model","url":"https://www.tandfonline.com/doi/full/10.1080/01691864.2026.2661958?af=R"},{"title":"Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems","url":"https://arxiv.org/html/2604.21794"},{"title":"1 A Joint Learning and Communication Framework for Multi-Agent Reinforcement","url":"https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/ipc-lab/A-Joint-Learning-and-Communication.pdf"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges | Vicinagearth | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44336-024-00009-2"},{"title":"[2505.21298] Large Language Models Miss the Multi-Agent Mark","url":"https://arxiv.org/abs/2505.21298"},{"title":"Multi-Agent Reinforcement Learning with Communication-Constrained Priors","url":"https://arxiv.org/pdf/2512.03528"},{"title":"Large Language Models Miss the Multi-Agent Mark Emanuele La Malfa1∗","url":"https://arxiv.org/pdf/2505.21298"},{"title":"Large Language Models for Message Mediation in Multi-agent Networks Environments | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-97119-8_12"}]

Based on the web search results, I found several relevant sources discussing reconstruction loss, multi-agent communication, and language models:

## Key Findings

**Reconstruction Loss in Multi-Agent Communication:**

Reconstruction loss is used to measure the binary cross entropy loss between one agent's perceived image and another agent's reconstructed image using symbols. In language emergence studies, when sender and receiver agents learn to reconstruct images using each other's symbols, they develop a shared language.

**Framework Applications:**

A framework models language emergence as decentralized Bayesian inference, effectively creating an encoder-decoder structure at a societal scale: human society collectively encodes its grounded representations into language, and an LLM decodes these symbols to reconstruct a latent space mirroring the original structure.

**Visual Information Processing:**

In the context of LLM-based multi-agent systems, reconstruction loss is employed to ensure that images generated by a generator from input visual vectors closely resemble the original images, thereby aiming to deceive the discriminator.

**Multi-Agent Communication Architecture:**

In one approach, the backbone language model remains frozen while lightweight LoRA adapters are optimized. Intermediate agents perform latent reasoning steps and produce continuous KV representations that encode their internal computation, which are accumulated sequentially across agents and passed to downstream agents as a shared latent context.

These approaches highlight how reconstruction loss functions are integral to enabling effective communication and language emergence among multiple agents in machine learning systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "811df0bc-5b02-443e-950f-271d72b719e0",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "f95bfbbb-d5e6-4721-83b0-693c0c4c61f6",
  "sourceToolAssistantUUID": "811df0bc-5b02-443e-950f-271d72b719e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T20:20:06.553Z_

<details><summary>↩ Tool result · `toolu_01KkwrpFGzuhQCdco1hZadMN`</summary>

```text
Web search results for query: "intent reconstruction agent communication reinforcement learning"

Links: [{"title":"Communication in Multi-Agent Reinforcement Learning: Intention Sharing | OpenReview","url":"https://openreview.net/forum?id=qpsl2dR9twy"},{"title":"Agentic AI-Enhanced Semantic Communications: Foundations, Architecture, and Applications","url":"https://arxiv.org/html/2512.23294"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"Learning to Communicate with Intent: An Introduction","url":"https://arxiv.org/pdf/2211.09613"},{"title":"Intent-Grounded Compositional Communication through ...","url":"https://dcslgatech.github.io/iros22-multi-agent-workshop/contributed_papers/IROS22-DMMAS_paper_5730.pdf"},{"title":"The Power in Communication: Power Regularization of Communication for Autonomy in Cooperative Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2404.06387v1"},{"title":"A survey of multi-agent deep reinforcement learning with communication | Autonomous Agents and Multi-Agent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10458-023-09633-6"},{"title":"[2211.09613] Learning to Communicate with Intent: An Introduction","url":"https://arxiv.org/abs/2211.09613"},{"title":"Towards Collaborative Intelligence: Propagating Intentions and Reasoning for Multi-Agent Coordination with Large Language Models","url":"https://arxiv.org/html/2407.12532v1"},{"title":"Designing Intent Communication for Agent-Human Collaboration","url":"https://arxiv.org/html/2510.20409"}]

Based on the search results, here's what I found about intent reconstruction, agent communication, and reinforcement learning:

## Key Research Areas

**Communication in Multi-Agent Reinforcement Learning:**

Communication is a core component for learning coordinated behavior in multi-agent systems, with approaches like Intention Sharing (IS) designed to enhance coordination among agents. In the IS scheme, each agent generates an imagined trajectory representing its future action plan based on the learned model of environment dynamics and other agents.

**Intent-Based Communication:**

A key framework involves learning how to communicate with intent—transmitting messages over a channel based on the end-goal of the communication, which differs from classical communication systems that focus on exact message reconstruction.

**Intention Sharing in MARL:**

Agents learn when to communicate intentions and which teammates require task details, resulting in emergent coordinated behaviors, demonstrating the efficacy of intention sharing for cooperative multi-agent RL.

**Intent-Grounded Communication:**

Research aims to ground communication to more accurately represent intent through goal-grounded contrastive learning, which builds on maximum-entropy reinforcement learning objectives.

These approaches address fundamental challenges in multi-agent systems, particularly partial observability where agents have access only to local observations, non-stationarity from other agents' changing policies, and how communication can help tackle these problems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d445e1d8-3c4f-4d95-8e20-dd693214f048",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "b3adedf5-aa2e-45df-a5b5-d9ca34aca9ae",
  "sourceToolAssistantUUID": "d445e1d8-3c4f-4d95-8e20-dd693214f048",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T20:20:08.426Z_

<details><summary>↩ Tool result · `toolu_01BBVDHv649GA9SRu2vVzCv5`</summary>

```text
Web search results for query: "dense supervision agent communication reinforcement learning"

Links: [{"title":"Effects of Supervision, Population Size, and Self-Play on Multi-Agent Reinforcement Learning to Communicate | Artificial Life Conference Proceedings | MIT Press","url":"https://direct.mit.edu/isal/article/doi/10.1162/isal_a_00328/98420/Effects-of-Supervision-Population-Size-and-Self"},{"title":"A survey of multi-agent deep reinforcement learning with communication | Autonomous Agents and Multi-Agent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10458-023-09633-6"},{"title":"Explainable multi agent reinforcement learning framework for secure and adaptive communication in UAV swarm based fanets | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-39366-x"},{"title":"Learning to Communicate with Deep Multi-Agent Reinforcement Learning","url":"https://dl.acm.org/doi/pdf/10.5555/3157096.3157336"},{"title":"A Multi-Agent Deep Reinforcement Learning System for Governmental Interoperability","url":"https://www.mdpi.com/2076-3417/15/6/3146"},{"title":"Effects of Supervision, Population Size, and Self-Play on Multi-Agent Reinforcement Learning to Communicate | Request PDF","url":"https://www.researchgate.net/publication/342930910_Effects_of_Supervision_Population_Size_and_Self-Play_on_Multi-Agent_Reinforcement_Learning_to_Communicate"},{"title":"(PDF) Learning to Communicate with Deep Multi-Agent Reinforcement Learning","url":"https://www.researchgate.net/publication/303448501_Learning_to_Communicate_with_Deep_Multi-Agent_Reinforcement_Learning"},{"title":"Learning to Schedule Communication in Multi-agent Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=SJxu5iR9KQ"},{"title":"Agent Learning via Early Experience","url":"https://arxiv.org/pdf/2510.08558"},{"title":"Reviews: Learning to Communicate with Deep Multi-Agent Reinforcement Learning","url":"https://proceedings.neurips.cc/paper/2016/file/c7635bfd99248a2cdef8249ef7bfbef4-Reviews.html"}]

I've completed the web search for "dense supervision agent communication reinforcement learning". Here are the key findings:

## Overview of Results

The search revealed several important research areas related to agent communication and reinforcement learning:

### Dense Supervision in Multi-Agent Communication

Research has examined the effects of bottom-driven supervision on multi-agent reinforcement learning systems, finding that supervising feedback augments the learning results of all groups and helps agents coordinate on maximally homogeneous and symmetric communication systems.

### Communication Protocols in Multi-Agent RL

Communication is an effective mechanism for coordinating the behaviors of multiple agents, broadening their views of the environment, and supporting their collaborations. In the field of multi-agent deep reinforcement learning (MADRL), agents can improve the overall learning performance and achieve their objectives by communication.

### Key Approaches

Two main approaches for learning communication in these domains are Reinforced Inter-Agent Learning (RIAL) and Differentiable Inter-Agent Learning (DIAL). The former uses deep Q-learning, while the latter exploits the fact that, during learning, agents can propagate error derivatives through (noisy) communication channels, using centralised learning but decentralised execution.

### Communication Scheduling

Recent work addresses practical constraints: A multi-agent deep reinforcement learning framework called SchedNet enables agents to learn how to schedule themselves, how to encode the messages, and how to select actions based on received messages.

The search results show that dense supervision can improve convergence and communication protocol symmetry in multi-agent systems, while various deep reinforcement learning approaches enable agents to learn effective communication protocols for coordination.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a518b8c5-8b33-4669-a659-ee07cc819d85",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "ca58c795-ea83-40ba-adc5-c6e35db7b927",
  "sourceToolAssistantUUID": "a518b8c5-8b33-4669-a659-ee07cc819d85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T20:20:12.565Z_

<details><summary>↩ Tool result · `toolu_011uDup8jX5VnWhJHME9YTN6`</summary>

```text
Web search results for query: "stop gradient multi-agent communication reinforcement learning"

Links: [{"title":"Decentralized Policy Gradient Descent Ascent for Safe Multi-Agent Reinforcement Learning | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/17062"},{"title":"Communication with factorized policy gradients in multi-agent deep reinforcement learning | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-025-11272-9"},{"title":"GitHub - LantaoYu/MARL-Papers: Paper list of multi-agent reinforcement learning (MARL) · GitHub","url":"https://github.com/LantaoYu/MARL-Papers"},{"title":"A survey of multi-agent deep reinforcement learning with communication | Autonomous Agents and Multi-Agent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10458-023-09633-6"},{"title":"MADDPG: When Your Agents Need to Stop Fighting Each Other | by Alper Ersin Balcı | Medium","url":"https://alperersinbalci.medium.com/multi-agent-deep-deterministic-policy-gradient-advancing-collaborative-learning-in-reinforcement-ba5a46bdcae7"},{"title":"Counterfactual Multi-Agent Policy Gradients Jakob N. Foerster1,†","url":"https://www.cs.ox.ac.uk/people/shimon.whiteson/pubs/foersteraaai18.pdf"},{"title":"A New Framework for Multi-Agent Reinforcement Learning –","url":"https://arxiv.org/pdf/1910.09152"},{"title":"𝐾-Level Policy Gradients for Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2509.12117v1"},{"title":"Deep multiagent reinforcement learning: challenges and directions | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-022-10299-x"},{"title":"Explainable multi agent reinforcement learning framework for secure and adaptive communication in UAV swarm based fanets | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-39366-x"}]

I've completed the web search for "stop gradient multi-agent communication reinforcement learning". Here are the key findings:

## Overview of Results

The search returned research on multi-agent reinforcement learning (MARL) with communication, though no specific results directly mentioned "stop gradient" as a technique. However, the results do cover several important related topics:

### Key Research Areas Found:

1. **Communication with Factorized Policy Gradients**: Recent work uses deterministic policies and message encoders for end-to-end training that efficiently backpropagates gradients from factorized value functions to communicating agents.

2. **Centralized Training with Decentralized Execution**: The core principle of centralized training with decentralized execution has become a standard framework in multi-agent RL. Agents are connected by peer-to-peer communication networks to share information with their neighbors.

3. **Multi-Agent Frameworks**: Five key research areas address challenges in multi-agent RL: centralised training and decentralised execution, opponent modelling, communication, efficient coordination, and reward shaping.

4. **Recent Advances**: K-Level Policy Gradient (KPG) is a method that recursively updates each agent against the updated policies of other agents, and theoretically achieves monotonic convergence to a local Nash equilibrium under certain conditions.

The search results focus on gradient-based approaches to multi-agent communication, though they don't specifically address "stop gradient" techniques. This term is typically used in deep learning to prevent gradient flow through certain operations—a technique that may be used in multi-agent systems but wasn't directly highlighted in these particular research papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "961564c2-6c98-4d79-b060-f905ac202386",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "db6ffdc8-1311-44e5-9ae8-f7fcec01a5b9",
  "sourceToolAssistantUUID": "961564c2-6c98-4d79-b060-f905ac202386",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-10T20:20:15.462Z_

Now let me run the remaining searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db6ffdc8-1311-44e5-9ae8-f7fcec01a5b9",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWT689SkaBhnB95SccD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32a55922-e360-48b0-8d14-39ed66dcc7f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSsBYzgvMcpxVhwcBDesT9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4905,
      "cache_read_input_tokens": 10545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4905,
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

_source line 18 · 2026-05-10T20:20:16.971Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KFQkFBoenewAKo4jBiXMrk`</summary>

```json
{
  "query": "EMA target reinforcement learning auxiliary loss stabilization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32a55922-e360-48b0-8d14-39ed66dcc7f8",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWT689SkaBhnB95SccD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac73167b-3f5b-48c6-adb4-9190727c4b48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSsBYzgvMcpxVhwcBDesT9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4905,
      "cache_read_input_tokens": 10545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4905,
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

_source line 19 · 2026-05-10T20:20:18.157Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FWqzR9wY6hYGP9XjEDTnpS`</summary>

```json
{
  "query": "text communication training multi-agent reinforcement learning LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac73167b-3f5b-48c6-adb4-9190727c4b48",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWT689SkaBhnB95SccD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0982675-5289-4bb2-86c9-92ac07b748fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSsBYzgvMcpxVhwcBDesT9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4905,
      "cache_read_input_tokens": 10545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4905,
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

_source line 20 · 2026-05-10T20:20:19.034Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K2KuKJrkjmmHxFkGAwAi12`</summary>

```json
{
  "query": "ThoughtComm NeurIPS 2025 multi-agent communication"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0982675-5289-4bb2-86c9-92ac07b748fb",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWT689SkaBhnB95SccD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c52a733f-c243-420f-9915-74e528eb8791",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSsBYzgvMcpxVhwcBDesT9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4905,
      "cache_read_input_tokens": 10545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4905,
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

_source line 21 · 2026-05-10T20:20:19.752Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0192JqLoRYp46YZFCQA3miGN`</summary>

```json
{
  "query": "Social Deduction LLM AAMAS 2025 multi-agent RL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c52a733f-c243-420f-9915-74e528eb8791",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWT689SkaBhnB95SccD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2f40601-7673-4c65-8c3b-7182e11c5997",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSsBYzgvMcpxVhwcBDesT9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4905,
      "cache_read_input_tokens": 10545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4905,
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

_source line 22 · 2026-05-10T20:20:25.006Z_

<details><summary>↩ Tool result · `toolu_01FWqzR9wY6hYGP9XjEDTnpS`</summary>

```text
Web search results for query: "text communication training multi-agent reinforcement learning LLM 2026"

Links: [{"title":"GitHub - TsinghuaC3I/MARTI: A Framework for LLM-based Multi-Agent Reinforced Training and Inference · GitHub","url":"https://github.com/TsinghuaC3I/MARTI"},{"title":"Towards Communication Efficient Multi-Agent Cooperations: Reinforcement Learning and LLM","url":"https://www.techrxiv.org/users/878096/articles/1259644-towards-communication-efficient-multi-agent-cooperations-reinforcement-learning-and-llm"},{"title":"A Brief Overview: Agentic Reinforcement Learning In Large Language Models","url":"https://arxiv.org/html/2604.27859"},{"title":"[2605.02801] Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces","url":"https://arxiv.org/abs/2605.02801"},{"title":"[2405.11106] LLM-based Multi-Agent Reinforcement Learning: Current and Future Directions","url":"https://arxiv.org/abs/2405.11106"},{"title":"NeurIPS A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning","url":"https://neurips.cc/virtual/2025/127960"},{"title":"Full article: Generative emergent communication: large language model is a collective world model","url":"https://www.tandfonline.com/doi/full/10.1080/01691864.2026.2661958?af=R"},{"title":"Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces","url":"https://arxiv.org/html/2605.02801"},{"title":"A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=K6T0o875zF"},{"title":"LLM Collaboration With Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2508.04652v1"}]

Here are the search results for "text communication training multi-agent reinforcement learning LLM 2026":

## Key Findings

**Recent Frameworks and Research:**

MARTI is an open-source framework for training LLM-based Multi-Agent Systems (MAS) with Reinforcement Learning (RL). MARTI-v2 was released on February 10, 2026 with scaling multi-agent tree search via reinforcement learning for code generation, and MARTI was accepted by ICLR 2026.

**Communication-Focused Research:**

Multi-agent systems have gained popularity due to their effectiveness in diverse applications, with decentralized approaches relying on inter-agent communication emerging as a promising alternative to centralized coordination methods. An LLM-based Bandwidth-Adaptive Dual-Policy (LLM-BDP) framework has been proposed that can adapt to varying bandwidth constraints by simply modifying the input prompt, thereby eliminating the need for retraining.

**Multi-Agent Orchestration:**

As LLM agents evolve from isolated tool users into coordinated teams, reinforcement learning must optimize not only individual actions but also how work is spawned, delegated, communicated, aggregated, and stopped through orchestration traces.

**Collaboration and Training:**

LLM collaboration has been modeled as a cooperative Multi-Agent Reinforcement Learning problem with the development of Multi-Agent Group Relative Policy Optimization (MAGRPO).

These recent developments show significant progress in combining text-based communication, multi-agent systems, and reinforcement learning with LLMs in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0982675-5289-4bb2-86c9-92ac07b748fb",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "70232840-fd02-44ef-9a50-8b12a891a474",
  "sourceToolAssistantUUID": "f0982675-5289-4bb2-86c9-92ac07b748fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T20:20:25.017Z_

<details><summary>↩ Tool result · `toolu_01KFQkFBoenewAKo4jBiXMrk`</summary>

```text
Web search results for query: "EMA target reinforcement learning auxiliary loss stabilization"

Links: [{"title":"How to Scale Your EMA - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/scale-em"},{"title":"Taming Reinforcement Learning for LLMs with EMA ...","url":"https://arxiv.org/pdf/2602.04417"},{"title":"Exponential Moving Average of Weights in Deep Learning: Dynamics and Benefits","url":"https://arxiv.org/html/2411.18704v1"},{"title":"How to Scale Your EMA Dan Busbridge∗ Jason Ramapuram∗ Pierre Ablin∗","url":"https://arxiv.org/pdf/2307.13813"},{"title":"EMA Without the Lag: Bias-Corrected Iterate Averaging Schemes","url":"https://arxiv.org/html/2508.00180"},{"title":"Reinforcement Learning with Automated Auxiliary Loss Search","url":"https://seqml.github.io/a2ls/"},{"title":"(PDF) EMA Policy Gradient: Taming Reinforcement Learning for LLMs with EMA Anchor and Top-k KL","url":"https://www.researchgate.net/publication/400459520_EMA_Policy_Gradient_Taming_Reinforcement_Learning_for_LLMs_with_EMA_Anchor_and_Top-k_KL"},{"title":"[2602.04417] EMA Policy Gradient: Taming Reinforcement Learning for LLMs with EMA Anchor and Top-k KL","url":"https://arxiv.org/abs/2602.04417"},{"title":"Model EMA (Exponential Moving Average) | timmdocs","url":"https://timm.fast.ai/training_modelEMA"},{"title":"[2210.06041] Reinforcement Learning with Automated Auxiliary Loss Search","url":"https://arxiv.org/abs/2210.06041"}]

Based on the search results, here are the key findings related to EMA (Exponential Moving Average) target networks, reinforcement learning, and auxiliary loss stabilization:

## EMA Target Networks in Reinforcement Learning

The use of a target network has been the common practice since the dawn of deep Q-learning, with a target network using an Exponential Moving Average (EMA) to update its knowledge while producing stable supervision targets.

## Recent Advances in EMA-based RL

A recent paper titled "EMA Policy Gradient: Taming Reinforcement Learning for LLMs with EMA Anchor and Top-k KL" proposes improvements to policy gradient algorithms. The work proposes two simple techniques to improve policy gradient algorithms for LLMs, first replacing the fixed anchor policy during RL with an Exponential Moving Average (EMA), similar to a target network in deep Q-learning. The authors derive the stability conditions for using EMA anchor and show that their Top-k KL estimator yields both unbiased KL values and unbiased gradients at any k, while bringing the benefits of exact KL.

## Stabilization Benefits of EMA

EMA methods attribute the effectiveness of EMA to smoother changes in target representations, maintaining consistency and stability, rather than the quality of the representations. Compared to the target model, the model EMA moves slowly, making it useful as a stabilizer for networks governing Bellman updates in reinforcement learning.

## Auxiliary Loss Search

Separately, many recent works focus on designing auxiliary losses for learning informative representations, but these handcrafted objectives rely heavily on expert knowledge and may be sub-optimal, prompting the development of Automated Auxiliary Loss Search (A2LS), which automatically searches for top-performing auxiliary loss functions for RL.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac73167b-3f5b-48c6-adb4-9190727c4b48",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "5c748063-710c-4879-9487-d6706ddaa027",
  "sourceToolAssistantUUID": "ac73167b-3f5b-48c6-adb4-9190727c4b48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T20:20:26.738Z_

<details><summary>↩ Tool result · `toolu_01K2KuKJrkjmmHxFkGAwAi12`</summary>

```text
Web search results for query: "ThoughtComm NeurIPS 2025 multi-agent communication"

Links: [{"title":"NeurIPS Poster Thought Communication in Multiagent Collaboration","url":"https://neurips.cc/virtual/2025/poster/115550"},{"title":"NeurIPS Thought Communication in Multiagent Collaboration","url":"https://neurips.cc/virtual/2025/133198"},{"title":"Mind meld: agentic communication through thoughts instead of words - MBZUAI","url":"https://mbzuai.ac.ae/news/mind-meld-agentic-communication-through-thoughts-instead-of-words/"},{"title":"Thought Communication in Multiagent Collaboration | OpenReview","url":"https://openreview.net/forum?id=tq9lyV9Cml"},{"title":"NeurIPS Utilizing MCP and Shared Introspection for Targeted Agent-to-Agent Communication in Hierarchical Clinical Multi-Agent Systems","url":"https://neurips.cc/virtual/2025/loc/mexico-city/129950"},{"title":"NeurIPS Poster COGNAC: Cooperative Graph-based Networked Agent Challenges for Multi-Agent Reinforcement Learning","url":"https://neurips.cc/virtual/2025/poster/121486"},{"title":"NeurIPS Improved Multi-Agent Collaboration with Multi-Turn Reinforcement Learning","url":"https://neurips.cc/virtual/2025/128017"},{"title":"NeurIPS Poster Pragmatic Heterogeneous Collaborative Perception via Generative Communication Mechanism","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/119282"},{"title":"NeurIPS Poster Multi-Agent Collaboration via Evolving Orchestration","url":"https://neurips.cc/virtual/2025/poster/118584"},{"title":"NeurIPS Poster MetaMind: Modeling Human Social Thoughts with Metacognitive Multi-Agent Systems","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/115802"}]

Based on the search results, here's what I found about ThoughtComm at NeurIPS 2025:

## Overview

ThoughtComm is a framework that works by extracting latent thoughts from agents' internal states before communication happens. It introduces a new paradigm of thought communication, which enables agents to interact directly mind-to-mind, akin to telepathy.

## Key Motivation

Natural language has long enabled human cooperation, but its lossy, ambiguous, and indirect nature limits the potential of collective intelligence. While machines are not subject to these constraints, most LLM-based multi-agent systems still rely solely on natural language, exchanging tokens or their embeddings.

## Technical Approach

To uncover these latent thoughts in a principled way, the process is formalized as a general latent variable model, where agent states are generated by an unknown function of underlying thoughts. The researchers prove that, in a nonparametric setting without auxiliary information, both shared and private latent thoughts between any pair of agents can be identified.

## Performance Results

Across the models, ThoughtComm achieved a relative improvement of 67.23% over single answer and 19.06% over multiagent finetuning, the current state-of-the-art. With Qwen 3-1.7B, ThoughtComm achieved an accuracy of 93% on MATH, an absolute gain of 17.2% over multiagent finetuning.

## Research Team

The research was presented at NeurIPS 2025 by a team from MBZUAI, Carnegie Mellon University, and Meta AI.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c52a733f-c243-420f-9915-74e528eb8791",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "90d525d3-0011-499b-9cd0-93a69ec17194",
  "sourceToolAssistantUUID": "c52a733f-c243-420f-9915-74e528eb8791",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T20:20:29.893Z_

<details><summary>↩ Tool result · `toolu_0192JqLoRYp46YZFCQA3miGN`</summary>

```text
Web search results for query: "Social Deduction LLM AAMAS 2025 multi-agent RL"

Links: [{"title":"Training Language Models for Social Deduction with Multi-Agent","url":"https://www.ifaamas.org/Proceedings/aamas2025/pdfs/p1830.pdf"},{"title":"Accepted Papers (with video links) – AAMAS 2025 Detroit","url":"https://aamas2025.org/index.php/conference/program/accepted-papers/"},{"title":"GitHub - git-disl/awesome-LLM-game-agent-papers: A Survey on Large Language Model-Based Game Agents (ACM CSUR) · GitHub","url":"https://github.com/git-disl/awesome-LLM-game-agent-papers"},{"title":"New Paper at AAMAS 2025: Scaling LLM-Guided Agent Simulations to Millions — MIT Media Lab","url":"https://www.media.mit.edu/posts/new-paper-on-limits-of-agency-at-aamas-2025/"},{"title":"Multi-Agent Systems in the Era of Foundation Models: Opportunities, Challenges and Futures","url":"https://icml.cc/virtual/2025/workshop/39955"},{"title":"GitHub - LantaoYu/MARL-Papers: Paper list of multi-agent reinforcement learning (MARL) · GitHub","url":"https://github.com/LantaoYu/MARL-Papers"},{"title":"Accepted Extended Abstracts (with video links) – AAMAS 2025 Detroit","url":"https://aamas2025.org/index.php/conference/program/accepted-extended-abstracts/"},{"title":"Language Agents with Reinforcement Learning for Strategic Play in the Werewolf Game | OpenReview","url":"https://openreview.net/forum?id=N1gmpVd4iE"},{"title":"[2508.04652] LLM Collaboration With Multi-Agent Reinforcement Learning","url":"https://arxiv.org/abs/2508.04652"},{"title":"MAPoRL2: Multi-Agent Post-Co-Training for Collaborative ...","url":"https://aclanthology.org/2025.acl-long.1459.pdf"}]

Based on the web search results, here are the key findings related to "Social Deduction LLM AAMAS 2025 multi-agent RL":

## Main Paper: Training Language Models for Social Deduction

There is a research paper on improving the ability of an LLM in social deduction games, showing how it enables agents to communicate effectively in the game of Among Us. 

Despite having weak base models, the agents learn to speak effectively and extract information from discussion messages through a framework that encourages listening and speaking with auxiliary dense rewards for helping other crewmates vote out the correct imposter.

## Key Results and Findings

The framework was evaluated by analyzing the success rate of crewmates against both pretrained and adaptive imposters, finding that crewmates form a robust communication strategy.

The technique results in emergent behavior commonly found in real games of Among Us between humans, such as directly accusing players and providing evidence to help other crewmates. The augmentation to discussions results in two times higher success rates relative to standard RL, doubling the win rates compared to standard RL.

## Publication and Availability

This work is part of the 24th International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2025), held May 19 – 23, 2025, in Detroit, Michigan. The authors released their code and models at https://socialdeductionllm.github.io/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2f40601-7673-4c65-8c3b-7182e11c5997",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "fca0807c-b24d-4d31-919b-5fa4b058cb83",
  "sourceToolAssistantUUID": "b2f40601-7673-4c65-8c3b-7182e11c5997",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-10T20:20:32.798Z_

Let me do a few more targeted searches to find additional closely related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fca0807c-b24d-4d31-919b-5fa4b058cb83",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWUNCJbpnpKUU7qUGPz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e542c2a-688d-480d-9590-0149922e869d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbfCVYpHudkdazEtsoP2sa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3975,
      "cache_read_input_tokens": 15450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3975,
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

_source line 27 · 2026-05-10T20:20:33.273Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018ALCnPazjeSDekcMwNM3Dn`</summary>

```json
{
  "query": "MARTI ICLR 2026 multi-agent reinforcement learning LLM training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e542c2a-688d-480d-9590-0149922e869d",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWUNCJbpnpKUU7qUGPz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "556a441e-f37c-4de8-ad82-083e5902da47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbfCVYpHudkdazEtsoP2sa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3975,
      "cache_read_input_tokens": 15450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3975,
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

_source line 28 · 2026-05-10T20:20:34.273Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UpQWtXGECQYmWupzDW6ne1`</summary>

```json
{
  "query": "MAGRPO multi-agent group relative policy optimization LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "556a441e-f37c-4de8-ad82-083e5902da47",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWUNCJbpnpKUU7qUGPz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "421d278d-a8fc-4aee-bdb6-43c28aff1bae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbfCVYpHudkdazEtsoP2sa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3975,
      "cache_read_input_tokens": 15450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3975,
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

_source line 29 · 2026-05-10T20:20:34.754Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0167EG7gF17ra3o4C9fvqf1H`</summary>

```json
{
  "query": "\"Learning to Communicate\" end-to-end multi-agent language 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "421d278d-a8fc-4aee-bdb6-43c28aff1bae",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWUNCJbpnpKUU7qUGPz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00441228-667e-40df-9b17-8608030b14e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbfCVYpHudkdazEtsoP2sa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3975,
      "cache_read_input_tokens": 15450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3975,
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

_source line 30 · 2026-05-10T20:20:35.395Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013YPqwuyVb1DMBKDpHkkE2X`</summary>

```json
{
  "query": "DIAL differentiable inter-agent learning stop gradient communication"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00441228-667e-40df-9b17-8608030b14e9",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWUNCJbpnpKUU7qUGPz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "649def96-373e-4cda-bfea-296f765b8968",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbfCVYpHudkdazEtsoP2sa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3975,
      "cache_read_input_tokens": 15450,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3975
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 240,
          "cache_read_input_tokens": 15450,
          "cache_creation_input_tokens": 3975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3975,
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

_source line 31 · 2026-05-10T20:20:39.772Z_

<details><summary>↩ Tool result · `toolu_018ALCnPazjeSDekcMwNM3Dn`</summary>

```text
Web search results for query: "MARTI ICLR 2026 multi-agent reinforcement learning LLM training"

Links: [{"title":"GitHub - TsinghuaC3I/MARTI: A Framework for LLM-based Multi-Agent Reinforced Training and Inference · GitHub","url":"https://github.com/TsinghuaC3I/MARTI"},{"title":"MARTI: A FRAMEWORK FOR MULTI-AGENT LLM SYSTEMS ...","url":"https://openreview.net/pdf/be61bdf63f6dcb786a5f70bfbc5c9f8cc8bc209d.pdf"},{"title":"ICLR Poster MARTI: A Framework for Multi-Agent LLM Systems Reinforced Training and Inference","url":"https://iclr.cc/virtual/2026/poster/10010710"},{"title":"MARTI: A FRAMEWORK FOR MULTI-AGENT LLM ...","url":"https://openreview.net/pdf?id=E7jZqo0A50"},{"title":"MARTI: A Framework for Multi-Agent LLM Systems Reinforced Training and Inference | OpenReview","url":"https://openreview.net/forum?id=E7jZqo0A50"},{"title":"ICLR 2026 Workshop on Multi-Agent Learning and Generative ...","url":"https://iclr26-mal-gai.github.io/"},{"title":"Paper published at the Lifelong Agent Workshop @ ICLR 2026 MAGE:","url":"https://openreview.net/pdf/d80ccf0395e94992b8cb63a1961d4b4612df0a4e.pdf"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"},{"title":"ICLR 2026 Workshop Proposal MemAgents: Memory for LLM-Based Agentic Systems","url":"https://openreview.net/pdf?id=U51WxL382H"},{"title":"Kaiyan Zhang on X: \"🧠 Again! Introducing: MARTI — Multi-Agent Reinforced Training and Inference A unified framework for LLM-based Multi-Agent Systems with centralized interaction &amp; distributed policy training. Supports structured workflows (debate, MoA, chain), custom rewards, and 3rd-party MAS https://t.co/XGyTf02o68\" / X","url":"https://x.com/OkhayIea/status/1927739357383086438"}]

Based on the search results, here's what I found about MARTI at ICLR 2026:

## MARTI at ICLR 2026

MARTI was accepted by ICLR 2026, and the framework addresses an important gap in existing research.

### Overview

MARTI is an open-source framework designed to facilitate scalable and efficient learning of multi-agent LLM systems. More specifically, MARTI supports centralized multi-agent interactions and distributed policy training, with the added capability of multi-turn asynchronous rollouts to enhance training efficiency, and includes dynamic workflows for multi-agent interactions that integrate both rule-based verifiable rewards and LLM-based generative rewards.

### Key Features

MARTI employs a centralized interaction design for its built-in workflows (e.g., Multi-Agent Debate, Chain-of-Agents, and Mixture-of-Agents) and customizable workflows, while utilizing distributed policy training for individual agents.

### Performance Results

The framework demonstrates effectiveness through comprehensive experiments on diverse mathematical tasks, showing that multi-agent LLM-based systems outperform single-agent systems within the same inference budget after convergence.

### Additional Developments

The framework has evolved beyond the ICLR paper submission. MARTI-v2 introduces tree search-augmented reinforcement learning training (MARS²) for complex reasoning tasks like code generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "556a441e-f37c-4de8-ad82-083e5902da47",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "a3b8791c-3ffd-4918-a408-548430907f13",
  "sourceToolAssistantUUID": "556a441e-f37c-4de8-ad82-083e5902da47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T20:20:39.966Z_

<details><summary>↩ Tool result · `toolu_01UpQWtXGECQYmWupzDW6ne1`</summary>

```text
Web search results for query: "MAGRPO multi-agent group relative policy optimization LLM"

Links: [{"title":"LLM Collaboration with Multi-Agent Reinforcement Learning","url":"https://arxiv.org/pdf/2508.04652"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Multi-Turn+Group+Relative+Policy+Optimization"},{"title":"LLM Collaboration With Multi-Agent Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2508.04652v1"},{"title":"M-GRPO: Multi-Agent Group Relative Policy Optimization","url":"https://www.emergentmind.com/topics/multi-agent-group-relative-policy-optimization-m-grpo"},{"title":"MAGRPO Explained: 3x Faster LLM Collaboration","url":"https://www.bohrium.com/en/blog/research-notes/aaai-2026-llm-collaboration-multi-agent-reinforcement-learning/"},{"title":"NeurIPS Improved Multi-Agent Collaboration with Multi-Turn Reinforcement Learning","url":"https://neurips.cc/virtual/2025/128017"},{"title":"Improved Multi-Agent Collaboration with Multi-Turn Reinforcement Learning","url":"https://openreview.net/pdf?id=WYfzRJgWbO"},{"title":"[2508.04652] LLM Collaboration With Multi-Agent Reinforcement Learning","url":"https://arxiv.org/abs/2508.04652"},{"title":"LLM Collaboration with Multi-Agent Reinforcement Learning | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40487"},{"title":"Improved Multi-Agent Collaboration with Multi-Turn Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=WYfzRJgWbO"}]

Based on the search results, here's what I found about MAGRPO:

## Overview

MAGRPO (Multi-Agent Group Relative Policy Optimization) is a multi-agent, multi-turn algorithm developed to solve LLM collaboration, building on current RL approaches for LLMs as well as MARL techniques.

## Key Characteristics

MAGRPO leverages centralized group-relative advantages for joint optimization, while preserving decentralized execution for each agent. Instead of relying on brittle text prompts to coordinate Large Language Models, MAGRPO treats collaboration as a mathematical problem—specifically, a cooperative Multi-Agent Reinforcement Learning task that trains agents to generate responses maximizing a shared group reward rather than just their individual success.

## Technical Foundation

By formalizing LLM dialogue as a Decentralized Partially Observable Markov Decision Process (Dec-POMDP), MAGRPO creates a framework where agents optimize for a shared team objective while acting on their own local observations, effectively bridging the gap between independent learning and true cooperative AI.

## Applications and Results

Experiments on LLM writing and coding collaboration demonstrate that fine-tuning multiple LLMs with MAGRPO enables agents to generate high-quality responses efficiently through effective cooperation. The authors have released CoMLRL, an open-source library for training multiple LLMs using MARL that includes the environments and benchmarks used in the paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "421d278d-a8fc-4aee-bdb6-43c28aff1bae",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "288e469e-3a75-44b4-bbb5-153f5453a7ac",
  "sourceToolAssistantUUID": "421d278d-a8fc-4aee-bdb6-43c28aff1bae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-10T20:20:40.992Z_

<details><summary>↩ Tool result · `toolu_0167EG7gF17ra3o4C9fvqf1H`</summary>

```text
Web search results for query: ""Learning to Communicate" end-to-end multi-agent language 2025 2026 arxiv"

Links: [{"title":"[2604.21794] Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems","url":"https://arxiv.org/abs/2604.21794"},{"title":"Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems","url":"https://arxiv.org/html/2604.21794"},{"title":"End-to-End Optimization of LLM-Driven Multi-Agent Search Systems via Heterogeneous-Group-Based Reinforcement Learning","url":"https://arxiv.org/html/2506.02718v2"},{"title":"Towards Language-Augmented Multi-Agent Deep Reinforcement Learning","url":"https://arxiv.org/html/2506.05236v1"},{"title":"Latent Collaboration in Multi-Agent Systems","url":"https://arxiv.org/html/2511.20639v1"},{"title":"Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces","url":"https://arxiv.org/html/2605.02801v1"},{"title":"[2511.20639] Latent Collaboration in Multi-Agent Systems","url":"https://arxiv.org/abs/2511.20639"},{"title":"Large Language Models Miss the Multi-Agent Mark","url":"https://arxiv.org/html/2505.21298v3"},{"title":"[1605.06676] Learning to Communicate with Deep Multi-Agent Reinforcement Learning","url":"https://arxiv.org/abs/1605.06676"},{"title":"[2506.09331] Multi-Agent Language Models: Advancing Cooperation, Coordination, and Adaptation","url":"https://arxiv.org/abs/2506.09331"}]

Based on the web search results, I found the paper you're looking for:

**Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems** (arXiv:2604.21794)

## Key Details:

The paper proposes DiffMAS, a training framework that treats latent communication as a learnable component of multi-agent systems. DiffMAS performs parameter-efficient supervised training over multi-agent latent trajectories, enabling agents to jointly learn how information should be encoded and interpreted across interactions.

Multi-agent systems built on large language models have shown strong performance on complex reasoning tasks, yet most work focuses on agent roles and orchestration while treating inter-agent communication as a fixed interface. Latent communication through internal representations such as key-value caches offers a promising alternative to text-based protocols, but existing approaches do not jointly optimize communication with multi-agent reasoning.

Experiments on mathematical reasoning, scientific QA, code generation, and commonsense benchmarks show that DiffMAS consistently improves reasoning accuracy and decoding stability over single-agent inference and text-based approaches.

The paper was submitted on April 23, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00441228-667e-40df-9b17-8608030b14e9",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "b1697460-498b-4ba4-8b70-c518ed9b6fc2",
  "sourceToolAssistantUUID": "00441228-667e-40df-9b17-8608030b14e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-10T20:20:42.063Z_

<details><summary>↩ Tool result · `toolu_013YPqwuyVb1DMBKDpHkkE2X`</summary>

```text
Web search results for query: "DIAL differentiable inter-agent learning stop gradient communication"

Links: [{"title":"Learning to Communicate with Deep Multi-Agent Reinforcement Learning","url":"https://arxiv.org/pdf/1605.06676"},{"title":"[1605.06676] Learning to Communicate with Deep Multi-Agent Reinforcement Learning","url":"https://arxiv.org/abs/1605.06676"},{"title":"DIAL and RIAL - CommRL","url":"https://commrl-docs.readthedocs.io/en/latest/Literature_Reviews/DIAL_RIAL/"},{"title":"(PDF) Learning to Communicate with Deep Multi-Agent Reinforcement Learning","url":"https://www.researchgate.net/publication/303448501_Learning_to_Communicate_with_Deep_Multi-Agent_Reinforcement_Learning"},{"title":"COMMUNICATION IN MULTI-AGENT REINFORCEMENT ...","url":"https://openreview.net/pdf?id=qpsl2dR9twy"},{"title":"Differentiable Inter-Agent Learning (DIAL)","url":"https://www.emergentmind.com/topics/differentiable-inter-agent-learning-dial"},{"title":"Learning to Communicate with Deep Multi-Agent Reinforcement Learning","url":"https://www.cs.ox.ac.uk/people/shimon.whiteson/pubs/foersternips16.pdf"},{"title":"Coordinated Multi-Agent Learning Mohit Sharma mohits1@andrew.cmu.edu","url":"https://mohitsharma0690.github.io/files/multi-agent-communication/report.pdf"},{"title":"Reviews: Learning to Communicate with Deep Multi-Agent Reinforcement Learning","url":"https://proceedings.neurips.cc/paper/2016/file/c7635bfd99248a2cdef8249ef7bfbef4-Reviews.html"},{"title":"Learning to communicate with Deep multi-agent reinforcement learning | Proceedings of the 30th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3157096.3157336"}]

Based on the search results, here's information about DIAL (Differentiable Inter-Agent Learning) and stop gradient communication:

## DIAL Overview

DIAL (Differentiable Inter-Agent Learning) is based on the insight that centralised learning affords more opportunities to improve learning than just parameter sharing. It allows real-valued messages to pass between agents during centralised learning, treating communication actions as bottleneck connections between agents, through which gradients can be pushed, yielding a system that is end-to-end trainable even across agents.

## How DIAL Works

During centralised learning, communication actions are replaced with direct connections between the output of one agent's network and the input of another's. During decentralised execution, real-valued messages are discretised and mapped to the discrete set of communication actions allowed by the task.

## Stop Gradient / No Gradient Flow

The key contrast is between DIAL and RIAL (Reinforced Inter-Agent Learning). While RIAL is end-to-end trainable within an agent, it is not end-to-end trainable across agents, i.e., no gradients are passed between agents. DIAL improves upon this by enabling gradient flow through the communication channel.

## Training Signal Advantage

In DIAL the gradient term for the message is the backpropagated error from the recipient of the message to the sender. Using this inter-agent gradient for training provides a richer training signal than the DQN loss for message selection in RIAL.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "649def96-373e-4cda-bfea-296f765b8968",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "3a7ac650-2407-4ec6-a5d2-6b763c00ba7a",
  "sourceToolAssistantUUID": "649def96-373e-4cda-bfea-296f765b8968",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-10T20:20:46.571Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W4GEXSvSpVg9PDWNBXtYFX`</summary>

```json
{
  "query": "\"Latent Collaboration in Multi-Agent Systems\" latent communication KV cache 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a7ac650-2407-4ec6-a5d2-6b763c00ba7a",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWVGGPfp3X1dydHQj6r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "010bbc05-3c3c-4249-acf0-33e87337bbac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xCombbUAza9wA8ZYaRUmt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3722,
      "cache_read_input_tokens": 19425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3722,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-10T20:20:47.181Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VdXxn8N5RGLjEykmkjodoT`</summary>

```json
{
  "query": "EMA policy gradient LLM reinforcement learning anchor 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "010bbc05-3c3c-4249-acf0-33e87337bbac",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWVGGPfp3X1dydHQj6r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db3871bc-0ba0-4071-9ac7-eb5139e2b535",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xCombbUAza9wA8ZYaRUmt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3722,
      "cache_read_input_tokens": 19425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3722,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-10T20:20:48.052Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013G5khjrQMBcEPkhpBcWzT2`</summary>

```json
{
  "query": "Automated Auxiliary Loss Search reinforcement learning A2LS NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db3871bc-0ba0-4071-9ac7-eb5139e2b535",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWVGGPfp3X1dydHQj6r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1f9181f-0950-4253-ba01-7664f8723d67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xCombbUAza9wA8ZYaRUmt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3722,
      "cache_read_input_tokens": 19425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3722,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-10T20:20:48.746Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A4VkRU9mMPc98RTWgRL4Bq`</summary>

```json
{
  "query": "intention sharing multi-agent reinforcement learning ICLR 2023 IS-MARL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1f9181f-0950-4253-ba01-7664f8723d67",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWVGGPfp3X1dydHQj6r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6ff9f63-dd81-49cf-8c44-9b34a162f468",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xCombbUAza9wA8ZYaRUmt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3722,
      "cache_read_input_tokens": 19425,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3722
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 226,
          "cache_read_input_tokens": 19425,
          "cache_creation_input_tokens": 3722,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3722,
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

_source line 39 · 2026-05-10T20:20:53.958Z_

<details><summary>↩ Tool result · `toolu_01W4GEXSvSpVg9PDWNBXtYFX`</summary>

```text
Web search results for query: ""Latent Collaboration in Multi-Agent Systems" latent communication KV cache 2025"

Links: [{"title":"Latent Collaboration in Multi-Agent Systems","url":"https://arxiv.org/pdf/2511.20639"},{"title":"GitHub - Gen-Verse/LatentMAS: [ICML 2026 Spotlight] Latent Collaboration in Multi-Agent Systems · GitHub","url":"https://github.com/Gen-Verse/LatentMAS"},{"title":"[2511.20639] Latent Collaboration in Multi-Agent Systems","url":"https://arxiv.org/abs/2511.20639"},{"title":"Latent Collaboration in Multi-Agent Systems","url":"https://www.emergentmind.com/papers/2511.20639"},{"title":"Ramp Labs on X: \"Latent Briefing: Efficient Memory Sharing for Multi-Agent Systems via KV Cache Compaction\" / X","url":"https://x.com/RampLabs/status/2042660310851449223"},{"title":"Paper page - Latent Collaboration in Multi-Agent Systems","url":"https://huggingface.co/papers/2511.20639"},{"title":"Learning to Communicate: Toward End-to-End Optimization of Multi-Agent Language Systems","url":"https://arxiv.org/html/2604.21794"},{"title":"The Invisible AI Threat: Latent Collaboration's Efficiency Breakthrough and Dangerous Security Risks","url":"https://kenhuangus.substack.com/p/latentmas-ai-agents-collaborate-at"},{"title":"Agent Primitives: Reusable Latent Building Blocks for Multi-Agent Systems","url":"https://arxiv.org/html/2602.03695v1"},{"title":"Latent Collaboration in Multi-Agent Systems | alphaXiv","url":"https://www.alphaxiv.org/resources/2511.20639"}]

I found comprehensive information about "Latent Collaboration in Multi-Agent Systems" from the recent research. Here's what the search reveals:

## Overview

LatentMAS is an end-to-end training-free framework that enables pure latent collaboration among LLM agents. It enables models to collaborate directly within the continuous latent space rather than relying on text-based communication.

## Core Components

The framework operates through two main mechanisms:

1. **Latent Thoughts Generation**: Each agent performs auto-regressive latent thoughts generation through last-layer hidden embeddings.

2. **Latent Working Memory Transfer**: A shared latent working memory preserves and transfers each agent's internal representations, ensuring lossless information exchange. Specifically, in decoder-only Transformers, the Key-Value (KV) cache functions as a dynamic working memory during auto-regressive generation, storing intermediate representations from previous decoding steps to avoid redundant computation.

## Performance Results

The approach shows substantial improvements: LatentMAS consistently outperforms strong single-model and text-based MAS baselines, achieving up to 14.6% higher accuracy, reducing output token usage by 70.8%-83.7%, and providing 4x-4.3x faster end-to-end inference.

## Theoretical Advantages

LatentMAS attains higher expressiveness and lossless information preservation with substantially lower complexity than vanilla text-based MAS. Each latent step carries far more information than a token, drastically reducing the number of required communication steps.

The framework was accepted to ICML 2026 as a Spotlight paper and has generated significant community interest with multiple extensions and improvements already being developed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "010bbc05-3c3c-4249-acf0-33e87337bbac",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "1cfcfd39-016d-46e5-a91c-bdca0842f3de",
  "sourceToolAssistantUUID": "010bbc05-3c3c-4249-acf0-33e87337bbac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T20:20:54.362Z_

<details><summary>↩ Tool result · `toolu_013G5khjrQMBcEPkhpBcWzT2`</summary>

```text
Web search results for query: "Automated Auxiliary Loss Search reinforcement learning A2LS NeurIPS"

Links: [{"title":"Reinforcement Learning with Automated Auxiliary Loss Search","url":"https://proceedings.neurips.cc/paper_files/paper/2022/hash/0be44cc1d459731928501cae5699f57a-Abstract-Conference.html"},{"title":"autorl-research/a2ls at main · microsoft/autorl-research","url":"https://github.com/microsoft/autorl-research/tree/main/a2ls"},{"title":"Reinforcement Learning with Automated Auxiliary Loss Search","url":"https://seqml.github.io/a2ls/"},{"title":"[2210.06041] Reinforcement Learning with Automated Auxiliary Loss Search","url":"https://arxiv.org/abs/2210.06041"},{"title":"Reinforcement learning with automated auxiliary loss search | Proceedings of the 36th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3600270.3600403"},{"title":"Reinforcement Learning with Automated Auxiliary Loss Search | OpenReview","url":"https://openreview.net/forum?id=_3XVbh6L2c"},{"title":"[PDF] Reinforcement Learning with Automated Auxiliary Loss Search | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Reinforcement-Learning-with-Automated-Auxiliary-He-Zhang/551633338103610cb8a60e6df004ef6fd3841d17"},{"title":"Reinforcement Learning with Automated Auxiliary Loss ...","url":"https://papers.neurips.cc/paper_files/paper/2022/file/0be44cc1d459731928501cae5699f57a-Paper-Conference.pdf"},{"title":"Reinforcement Learning with Automated Auxiliary Loss Search | Request PDF","url":"https://www.researchgate.net/publication/364517538_Reinforcement_Learning_with_Automated_Auxiliary_Loss_Search"},{"title":"AARL: Automated Auxiliary Loss for Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=v-27phh2c8O"}]

Based on the search results, here's what I found about Automated Auxiliary Loss Search (A2LS):

## Overview

A2LS is a principled and universal method for learning better representations with auxiliary loss functions that automatically searches for top-performing auxiliary loss functions for RL.

## Problem it Addresses

Good state representation is crucial to solving complicated reinforcement learning challenges. Many recent works focus on designing auxiliary losses for learning informative representations. Unfortunately, these handcrafted objectives rely heavily on expert knowledge and may be sub-optimal.

## Methodology

Based on the collected trajectory data, A2LS defines a general auxiliary loss space of size 7.5 × 10^20 and explores the space with an efficient evolutionary search strategy. A2LS contains an inner loop and an outer loop. The inner loop performs an RL training procedure with searched auxiliary loss functions. The outer loop searches auxiliary loss functions using an evolutionary algorithm to select the better auxiliary losses.

## Results

The discovered auxiliary loss (namely, A2-winner) significantly improves the performance on both high-dimensional (image) and low-dimensional (vector) unseen tasks with much higher efficiency, showing promising generalization.

## Publication

This is a NeurIPS 2022 paper. The code is available on GitHub through the Microsoft Research repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1f9181f-0950-4253-ba01-7664f8723d67",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "bc43abf7-5e33-4d8d-a7af-80a9217c9429",
  "sourceToolAssistantUUID": "d1f9181f-0950-4253-ba01-7664f8723d67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T20:20:55.143Z_

<details><summary>↩ Tool result · `toolu_01VdXxn8N5RGLjEykmkjodoT`</summary>

```text
Web search results for query: "EMA policy gradient LLM reinforcement learning anchor 2025"

Links: [{"title":"Taming Reinforcement Learning for LLMs with EMA ...","url":"https://arxiv.org/pdf/2602.04417"},{"title":"[2602.04417] EMA Policy Gradient: Taming Reinforcement Learning for LLMs with EMA Anchor and Top-k KL","url":"https://arxiv.org/abs/2602.04417"},{"title":"(PDF) EMA Policy Gradient: Taming Reinforcement Learning for LLMs with EMA Anchor and Top-k KL","url":"https://www.researchgate.net/publication/400459520_EMA_Policy_Gradient_Taming_Reinforcement_Learning_for_LLMs_with_EMA_Anchor_and_Top-k_KL"},{"title":"GitHub - LunjunZhang/ema-pg: Code for \"EMA Policy Gradient: Taming Reinforcement Learning for LLMs with EMA Anchor and Top-k KL\" (arxiv.org/abs/2602.04417) · GitHub","url":"https://github.com/LunjunZhang/ema-pg"},{"title":"[2504.18587] Training Large Language Models to Reason via EM Policy Gradient","url":"https://arxiv.org/abs/2504.18587"},{"title":"The State of Reinforcement Learning for LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"},{"title":"Reinforcement Learning via Self-Distillation","url":"https://arxiv.org/pdf/2601.20802"},{"title":"Reinforcement Learning | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/06-policy-gradients"},{"title":"Reinforcement Learning Meets Large Language Models: A Survey of","url":"https://arxiv.org/pdf/2509.16679"},{"title":"Training Large Language Models to Reason via EM Policy Gradient","url":"https://arxiv.org/html/2504.18587v1"}]

Based on the search results, I found relevant information about EMA policy gradient and reinforcement learning for LLMs in 2025:

## EMA Policy Gradient for LLM Reinforcement Learning

The research proposes two simple techniques to improve policy gradient algorithms for LLMs. First, it replaces the fixed anchor policy during RL with an Exponential Moving Average (EMA), similar to a target network in deep Q-learning. Second, it introduces a Top-k KL estimator, which allows for flexible interpolation between exact KL and sampled KL.

### Key Contributions

The work derives the stability conditions for using EMA anchor; moreover, it shows that the Top-k KL estimator yields both unbiased KL values and unbiased gradients at any k, while bringing the benefits of exact KL.

### Performance Improvements

In math reasoning, using an EMA anchor (η < 1) improves GRPO across all evaluated datasets. For instance, using the EMA anchor gives a boost of 50.8% → 53.9% on OlympiadBench. Using an EMA anchor improves not just Pass@1 but Pass@16 as well, suggesting that target networks can effectively mitigate Pass@N collapse that is common in reasoning RL.

### Memory Efficiency

Using EMA does not require storing an additional set of weights during training, since the anchor (reference) policy weights already need to be stored for standard KL-regularized policy gradients.

The paper (arXiv:2602.04417) was published in February 2026 and demonstrates practical improvements for training reasoning models like DeepSeek-R1 on mathematical and agentic tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db3871bc-0ba0-4071-9ac7-eb5139e2b535",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "21404aa2-30ed-472c-a7c1-96f6daf4f8d3",
  "sourceToolAssistantUUID": "db3871bc-0ba0-4071-9ac7-eb5139e2b535",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-10T20:20:55.330Z_

<details><summary>↩ Tool result · `toolu_01A4VkRU9mMPc98RTWgRL4Bq`</summary>

```text
Web search results for query: "intention sharing multi-agent reinforcement learning ICLR 2023 IS-MARL"

Links: [{"title":"LEARNING HIERARCHICAL MULTI-AGENT COOPERA","url":"https://openreview.net/pdf?id=rWW2WAGjfOi"},{"title":"COMMUNICATION IN MULTI-AGENT REINFORCEMENT ...","url":"https://openreview.net/pdf?id=qpsl2dR9twy"},{"title":"GitHub - chrisyrniu/Recent-Advances-in-Multi-Agent-Reinforcement-Learning: A collection of recent MARL papers · GitHub","url":"https://github.com/chrisyrniu/Recent-Advances-in-Multi-Agent-Reinforcement-Learning"},{"title":"GitHub - LantaoYu/MARL-Papers: Paper list of multi-agent reinforcement learning (MARL) · GitHub","url":"https://github.com/LantaoYu/MARL-Papers"},{"title":"Communication in Multi-Agent Reinforcement Learning: Intention Sharing | OpenReview","url":"https://openreview.net/forum?id=qpsl2dR9twy"},{"title":"ICLR Learning to Share in Multi-Agent Reinforcement Learning","url":"https://iclr.cc/virtual/2022/7786"},{"title":"RACE: Improve Multi-Agent Reinforcement Learning with Representation","url":"https://proceedings.mlr.press/v202/li23i/li23i.pdf"},{"title":"ICLR Learning to Communicate and Collaborate in a Competitive Multi-Agent Setup to Clean the Ocean from Macroplastics","url":"https://iclr.cc/virtual/2023/13476"},{"title":"LEARNING MULTI-AGENT COMMUNICATION FROM ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5623c35f3ab5e2c72aeb3abce27dc28f-Paper-Conference.pdf"}]

Based on the search results, I found relevant information about Intention Sharing (IS) in Multi-Agent Reinforcement Learning:

## Intention Sharing (IS) in MARL

Intention Sharing (IS) is a communication scheme for MARL designed to go beyond existing observation-sharing schemes. 

### How It Works

The proposed IS scheme allows each agent to share its intention with other agents in the form of encoded imagined trajectory, where each agent generates an imagined trajectory by modeling the environment dynamics and other agents' actions. Each agent learns the relative importance of the components in the imagined trajectory based on received messages from other agents using an attention model, with the output serving as an encoded imagined trajectory capturing the agent's intention and used as the communication message.

### Motivation

The approach addresses the question of how to harness the benefit of communication beyond sharing partial observation by proposing that each agent shares its intention as the content of the message.

Note: The search results indicate that the original IS paper by Kim et al. was published at ICLR 2020, not ICLR 2023. The specific "IS-MARL" designation from your query does not appear as a distinct work in the search results, though IS-based approaches continue to be cited in more recent MARL research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6ff9f63-dd81-49cf-8c44-9b34a162f468",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "530ef4f3-3e40-4d0f-ae2d-dbb86bf6c8fb",
  "sourceToolAssistantUUID": "e6ff9f63-dd81-49cf-8c44-9b34a162f468",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-10T20:20:58.465Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PecyhkNZtQ1NwU5wTxp5zJ`</summary>

```json
{
  "query": "auxiliary dense reward LLM agent communication Among Us social deduction 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "530ef4f3-3e40-4d0f-ae2d-dbb86bf6c8fb",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWWEvoaoxdUScVne1BM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8bd8917-41b1-42a0-b456-a8bc423f3ca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrGFuq4vsvZyV1hMTBGxLo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3831,
      "cache_read_input_tokens": 23147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3831,
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

_source line 44 · 2026-05-10T20:20:58.947Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015WbyemafKb26nZZNqCitY1`</summary>

```json
{
  "query": "\"generative emergent communication\" LLM collective world model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8bd8917-41b1-42a0-b456-a8bc423f3ca8",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWWEvoaoxdUScVne1BM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "528f391b-0a86-4135-8967-4ac190d3f15c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrGFuq4vsvZyV1hMTBGxLo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3831,
      "cache_read_input_tokens": 23147,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3831,
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

_source line 45 · 2026-05-10T20:20:59.472Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KjoWGqSb7gziz3wCao5QbT`</summary>

```json
{
  "query": "GRPO multi-agent text communication hidden state reconstruction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "528f391b-0a86-4135-8967-4ac190d3f15c",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWWEvoaoxdUScVne1BM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3521162b-fc9d-433b-969e-a405c9bb73f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrGFuq4vsvZyV1hMTBGxLo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3831,
      "cache_read_input_tokens": 23147,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3831
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 23147,
          "cache_creation_input_tokens": 3831,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3831,
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

_source line 46 · 2026-05-10T20:21:06.839Z_

<details><summary>↩ Tool result · `toolu_015WbyemafKb26nZZNqCitY1`</summary>

```text
Web search results for query: ""generative emergent communication" LLM collective world model 2026"

Links: [{"title":"Full article: Generative emergent communication: large language model is a collective world model","url":"https://www.tandfonline.com/doi/full/10.1080/01691864.2026.2661958?af=R"},{"title":"[2501.00226] Generative Emergent Communication: Large Language Model is a Collective World Model","url":"https://arxiv.org/abs/2501.00226"},{"title":"Generative Emergent Communication: Large Language Model is a Collective World Model","url":"https://arxiv.org/html/2501.00226"},{"title":"[Literature Review] Generative Emergent Communication: Large Language Model is a Collective World Model","url":"https://www.themoonlight.io/en/review/generative-emergent-communication-large-language-model-is-a-collective-world-model"},{"title":"[2501.00226v1] Generative Emergent Communication: Large Language Model is a Collective World Model","url":"https://arxiv.org/abs/2501.00226v1"},{"title":"Emergent social conventions and collective bias in LLM populations | Science Advances","url":"https://www.science.org/doi/10.1126/sciadv.adu9368"},{"title":"Generative AI collective behavior needs an interactionist paradigm","url":"https://arxiv.org/html/2601.10567v1"},{"title":"Multi-Agent LLM Systems: From Emergent Collaboration to Structured Collective Intelligence[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202511.1370"},{"title":"Generative Emergent Communication - CLaE","url":"https://bsky.app/profile/claeneuro.bsky.social/post/3lhyfbaneqs27"},{"title":"Unraveling the emergence of collective behavior in networks of cognitive agents | npj Artificial Intelligence","url":"https://www.nature.com/articles/s44387-026-00091-5"}]

Here are the key findings from the search results:

## Overview

The Collective World Model hypothesis argues that an LLM does not learn a world model from scratch but instead learns a statistical approximation of a collective world model already implicitly encoded in human language through a society-wide process of embodied, interactive sense-making.

## Generative Emergent Communication Framework

The generative emergent communication (Generative EmCom) framework, built upon Collective Predictive Coding (CPC), models language emergence as decentralized Bayesian inference, effectively creating an encoder-decoder structure at a societal scale: human society collectively encodes its grounded representations into language, and an LLM decodes these symbols to reconstruct a latent space mirroring the original structure.

## Key Contributions

The framework connects generative emergent communication to world models and multi-agent reinforcement learning, applying it to interpret LLMs and explaining phenomena like distributional semantics as a natural consequence of representation reconstruction.

## Recent Research Context (2026)

Beyond the primary Taniguchi et al. paper, recent 2026 research explores related areas: Studies demonstrate the spontaneous emergence of universally adopted social conventions in decentralized populations of LLM agents, and show how strong collective biases can emerge during this process, even when agents exhibit no bias individually.

Additionally, Recent perspectives argue that the next scaling frontier for LLMs is societies of models designed as structured collective intelligences, introducing frameworks based on interaction regimes—competition, collaboration, and coordination—and proposing "multi-agent pretraining" where agents jointly learn language and world models along with norms of discourse and self-correction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "528f391b-0a86-4135-8967-4ac190d3f15c",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "8e32527f-fd3b-4eb4-abcd-dbb988f66593",
  "sourceToolAssistantUUID": "528f391b-0a86-4135-8967-4ac190d3f15c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-10T20:21:08.363Z_

<details><summary>↩ Tool result · `toolu_01KjoWGqSb7gziz3wCao5QbT`</summary>

```text
Web search results for query: "GRPO multi-agent text communication hidden state reconstruction 2025 2026"

Links: [{"title":"Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization","url":"https://arxiv.org/html/2603.02701"},{"title":"GitHub - Gen-Verse/LatentMAS: [ICML 2026 Spotlight] Latent Collaboration in Multi-Agent Systems · GitHub","url":"https://github.com/Gen-Verse/LatentMAS"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group...","url":"https://arxiv.org/abs/2603.02701v1"},{"title":"[2511.13288] Multi-Agent Deep Research: Training Multi-Agent Systems with M-GRPO","url":"https://arxiv.org/abs/2511.13288"},{"title":"Multi-Agent Deep Research: Training Multi-Agent Systems with M-GRPO | alphaXiv","url":"https://www.alphaxiv.org/overview/2511.13288"},{"title":"Multiagent Systems Apr 2026","url":"https://arxiv.org/list/cs.MA/current"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"A Multi-Objective GRPO Approach","url":"https://arxiv.org/pdf/2503.21819"},{"title":"UNIFYING THE GRPO FRAMEWORKS WITH LEARNABLE ...","url":"https://openreview.net/pdf?id=0czAcXMBNO"}]

I found several relevant research papers and projects related to your query. Here are the key findings:

## GRPO and Multi-Agent Systems (2025-2026)

The paradigm of utilizing multiple Large Language Models (LLMs) to tackle complex tasks has garnered significant attention in 2025, with GRPO (Group Relative Policy Optimization) emerging as a key optimization method.

### Graph-GRPO
Graph-GRPO is a topology optimization framework that integrates Group Relative Policy Optimization to optimize communication in LLM-based Multi-Agent Systems, sampling a group of diverse communication graphs for each query and computing the advantage of specific edges based on their relative performance within the group.

### M-GRPO for Multi-Agent Training
M-GRPO is a hierarchical extension of Group Relative Policy Optimization designed for vertical Multi-agent systems with a main agent (planner) and multiple sub-agents (multi-turn tool executors), addressing optimization challenges when training distinct LLMs for different agents.

### Latent Collaboration (LatentMAS)
Recent frameworks introduce Binary RL via GRPO and On-Policy Distillation as learning paradigms for multi-agent systems, with extensions like Science-LatentMAS designed for specific downstream applications.

### GRPO Extensions
Group Relative Policy Optimization removes the need for separate value and reward models, instead relying on rule-based verifiers as training signals, proving effective in mathematical problem solving, code programming, and multimodal reasoning.

The search results indicate active research in 2025-2026 on optimizing multi-agent communication and coordination, though I didn't find specific papers explicitly focused on "hidden state reconstruction" in the context you may be seeking.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3521162b-fc9d-433b-969e-a405c9bb73f2",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "fadac9f7-11dc-4f90-96f9-70b41a819c9b",
  "sourceToolAssistantUUID": "3521162b-fc9d-433b-969e-a405c9bb73f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-10T20:21:09.249Z_

<details><summary>↩ Tool result · `toolu_01PecyhkNZtQ1NwU5wTxp5zJ`</summary>

```text
Web search results for query: "auxiliary dense reward LLM agent communication Among Us social deduction 2025"

Links: [{"title":"Training Language Models for Social Deduction with Multi-Agent","url":"https://www.ifaamas.org/Proceedings/aamas2025/pdfs/p1830.pdf"},{"title":"Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2502.06060"},{"title":"LLM Training for Social Deduction with MARL","url":"https://www.emergentmind.com/papers/2502.06060"},{"title":"Paper page - Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning","url":"https://huggingface.co/papers/2502.06060"},{"title":"Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning","url":"https://socialdeductionllm.github.io/"},{"title":"[2502.06060] Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning","url":"https://arxiv.org/abs/2502.06060"},{"title":"GitHub - FudanDISC/SocialAgent: A collection of resources that investigate social agents. · GitHub","url":"https://github.com/FudanDISC/SocialAgent"},{"title":"GitHub - AGI-Edgerunners/LLM-Agents-Papers: A repo lists papers related to LLM based agent · GitHub","url":"https://github.com/AGI-Edgerunners/LLM-Agents-Papers"},{"title":"Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems","url":"https://arxiv.org/html/2502.14321v1"},{"title":"AmongAgents: Evaluating Large Language Models in the Interactive Text-Based Social Deduction Game","url":"https://arxiv.org/html/2407.16521v2"}]

I found relevant research on your query. Here's what the search returned:

## Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning

A research framework trains LLMs by encouraging listening and speaking with auxiliary dense rewards for helping other crewmates vote out the correct imposter, enabling the self-improvement of these models over time.

### Key Approach

The framework decomposes the communication problem into listening and speaking, leveraging the agent's goal to predict useful information about the world as a dense reward signal that guides communication. More specifically, they improve a model's listening skills by training them to predict information about the environment based on discussions, and simultaneously improve a model's speaking skills with multi-agent reinforcement learning by rewarding messages based on their influence on other agents.

### Results and Emergent Behaviors

The full model achieves twice the win rate of the RL-only baseline in the base environment. The technique results in emergent behavior commonly found in real games of Among Us between humans, such as directly accusing players and providing evidence to help other crewmates.

### Game Environment

The research studies an embodied social deduction game based on Among Us, where the key question to answer is the identity of an adversarial imposter. During discussion phases, agents leverage large language models to generate free-form messages guided by the framework encouraging effective speaking and listening within the crewmates and finally vote out a suspected imposter.

This paper appears to be from AAMAS 2025 (published February 9, 2025).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8bd8917-41b1-42a0-b456-a8bc423f3ca8",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "ce36cc16-3352-4514-a797-32221263ca2e",
  "sourceToolAssistantUUID": "b8bd8917-41b1-42a0-b456-a8bc423f3ca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-10T20:21:12.970Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LAzxuG453cwLMfNUEeBRRM`</summary>

```json
{
  "query": "message reconstruction auxiliary loss emergent communication referential game deep learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce36cc16-3352-4514-a797-32221263ca2e",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWXGWqJWKGFkbbhFv39",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e20edef-fdc5-4953-b6fe-223f51cca0a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbSzEhRzGQLCHo3qZyY5yR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1813,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 26978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 50 · 2026-05-10T20:21:13.482Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016BTUd7R1GMQ9ce6PBzGzKo`</summary>

```json
{
  "query": "\"Cut the Crap\" LLM multi-agent communication pruning token efficiency 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e20edef-fdc5-4953-b6fe-223f51cca0a6",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWXGWqJWKGFkbbhFv39",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "227416fa-3689-4b3e-9316-c6b33aa6484e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbSzEhRzGQLCHo3qZyY5yR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1813,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 26978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1125,
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

_source line 51 · 2026-05-10T20:21:14.115Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QsPnySzViYousok1QjgTo1`</summary>

```json
{
  "query": "Werewolf language agent reinforcement learning strategic communication NeurIPS ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "227416fa-3689-4b3e-9316-c6b33aa6484e",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWXGWqJWKGFkbbhFv39",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53a19bf1-d817-45b6-a07d-ed8fc03b712a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbSzEhRzGQLCHo3qZyY5yR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1813,
      "cache_creation_input_tokens": 1125,
      "cache_read_input_tokens": 26978,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1125
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1813,
          "output_tokens": 174,
          "cache_read_input_tokens": 26978,
          "cache_creation_input_tokens": 1125,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1125,
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

_source line 52 · 2026-05-10T20:21:19.786Z_

<details><summary>↩ Tool result · `toolu_01QsPnySzViYousok1QjgTo1`</summary>

```text
Web search results for query: "Werewolf language agent reinforcement learning strategic communication NeurIPS ICLR 2025"

Links: [{"title":"ICML Poster Learning Strategic Language Agents in the Werewolf Game with Iterative Latent Space Policy Optimization","url":"https://icml.cc/virtual/2025/poster/45520"},{"title":"Language agents with reinforcement learning for strategic play in the Werewolf game | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3694355"},{"title":"Language Agents with Reinforcement Learning for Strategic Play in the Werewolf Game | OpenReview","url":"https://openreview.net/forum?id=N1gmpVd4iE"},{"title":"Learning Strategic Language Agents in the Werewolf Game with...","url":"https://arxiv.org/abs/2502.04686"},{"title":"[2310.18940] Language Agents with Reinforcement Learning for Strategic Play in the Werewolf Game","url":"https://arxiv.org/abs/2310.18940"},{"title":"ICML Poster Language Agents with Reinforcement Learning for Strategic Play in the Werewolf Game","url":"https://icml.cc/virtual/2024/poster/32805"},{"title":"Learning Strategic Language Agents in the Werewolf Game with Iterative Latent Space Policy Optimization","url":"https://arxiv.org/html/2502.04686v3"},{"title":"(PDF) Learning Strategic Language Agents in the Werewolf Game with Iterative Latent Space Policy Optimization","url":"https://www.researchgate.net/publication/388847830_Learning_Strategic_Language_Agents_in_the_Werewolf_Game_with_Iterative_Latent_Space_Policy_Optimization"},{"title":"NeurIPS Poster Multi-agent KTO: Enhancing Strategic Interactions of Large Language Model in Language Game","url":"https://neurips.cc/virtual/2025/poster/117599"},{"title":"Paper page - Learning Strategic Language Agents in the Werewolf Game with Iterative Latent Space Policy Optimization","url":"https://huggingface.co/papers/2502.04686"}]

Based on the search results, I found several recent research papers on language agents, reinforcement learning, and strategic communication in the Werewolf game:

## Key Research Papers Found:

**1. Latent Space Policy Optimization (LSPO) for Werewolf**

Researchers have proposed Latent Space Policy Optimization (LSPO), an iterative framework that combines game-theoretic methods with LLM fine-tuning to build strategic language agents, leveraging the observation that while the language space is combinatorially large, the underlying strategy space is relatively compact. The work addresses the challenge that strategic language games like Werewolf demand both strategic decision-making and free-form language interactions, while existing LLM agents often suffer from intrinsic bias and limited exploration.

This paper was presented at ICML 2025.

**2. Multi-agent KTO at NeurIPS 2025**

Using Werewolf as a test bed, researchers developed Multi-agent Kahneman-Tversky's Optimization (MaKTO) which engages diverse models in extensive gameplay to generate unpaired desirable and unacceptable responses, then employs KTO to refine the model's decision-making process, achieving a 61% average win rate across various models.

This paper was presented at NeurIPS 2025.

**3. Earlier RL-based Strategic Language Agents**

Earlier work proposed a framework that powers LLM-based agents with reinforcement learning, where agents use an LLM to perform deductive reasoning and generate a diverse set of action candidates, then an RL policy trained to optimize decision-making ability chooses an action from the candidates.

Both papers represent cutting-edge research combining reinforcement learning with large language models for strategic communication in the Werewolf game.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53a19bf1-d817-45b6-a07d-ed8fc03b712a",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "14740b67-40bd-4961-9367-dbfac879b545",
  "sourceToolAssistantUUID": "53a19bf1-d817-45b6-a07d-ed8fc03b712a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-10T20:21:20.357Z_

<details><summary>↩ Tool result · `toolu_016BTUd7R1GMQ9ce6PBzGzKo`</summary>

```text
Web search results for query: ""Cut the Crap" LLM multi-agent communication pruning token efficiency 2025"

Links: [{"title":"[2410.02506] Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems","url":"https://arxiv.org/abs/2410.02506"},{"title":"[Literature Review] Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems","url":"https://www.themoonlight.io/en/review/cut-the-crap-an-economical-communication-pipeline-for-llm-based-multi-agent-systems"},{"title":"Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems | OpenReview","url":"https://openreview.net/forum?id=LkzuPorQ5L"},{"title":"[2410.02506v1] Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems","url":"https://arxiv.org/abs/2410.02506v1"},{"title":"(PDF) Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems","url":"https://www.researchgate.net/publication/384630697_Cut_the_Crap_An_Economical_Communication_Pipeline_for_LLM-based_Multi-Agent_Systems"},{"title":"GitHub - yanweiyue/AgentPrune · GitHub","url":"https://github.com/yanweiyue/AgentPrune"},{"title":"Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems | PromptLayer","url":"https://www.promptlayer.com/research-papers/cut-the-crap-an-economical-communication-pipeline-for-llm-based-multi-agent-systems"},{"title":"Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems | alphaXiv","url":"https://www.alphaxiv.org/abs/2410.02506"},{"title":"Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/cut-crap-economical-communication-pipeline-llm-based"},{"title":"AgentDropout: Dynamic Agent Elimination for Token-Efficient and High-Performance LLM-Based Multi-Agent Collaboration","url":"https://arxiv.org/html/2503.18891"}]

Based on the search results, here's what I found about "Cut the Crap":

## Overview

"Cut the Crap" is an economical, simple, and robust multi-agent communication framework called AgentPrune, which can seamlessly integrate into mainstream multi-agent systems and prunes redundant or even malicious communication messages.

## Problem Addressed

Existing multi-agent pipelines inherently introduce substantial token overhead, as well as increased economic costs, which pose challenges for their large-scale deployments. AgentPrune is the first to identify and formally define the communication redundancy issue present in current LLM-based multi-agent pipelines, and efficiently performs one-shot pruning on the spatial-temporal message-passing graph.

## Technical Approach

By leveraging a trainable communication graph mask, AgentPrune identifies key message exchanges and prunes non-essential components in a one-shot manner, resulting in a sparse, token-economical, and highly informative communication graph.

## Key Results

AgentPrune integrates seamlessly into existing multi-agent frameworks, reducing token usage by 28.1% to 72.8% and achieves comparable results to state-of-the-art topologies, but at only 5.6% of their cost. It successfully defends against two types of agent-based adversarial attacks, with a 3.5% to 10.8% performance boost.

## Publication

The paper was accepted at The Thirteenth International Conference on Learning Representations (ICLR) 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "227416fa-3689-4b3e-9316-c6b33aa6484e",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "eff36bcc-a27b-4f01-b4b1-1066ae74a4f2",
  "sourceToolAssistantUUID": "227416fa-3689-4b3e-9316-c6b33aa6484e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-10T20:21:22.332Z_

<details><summary>↩ Tool result · `toolu_01LAzxuG453cwLMfNUEeBRRM`</summary>

```text
Web search results for query: "message reconstruction auxiliary loss emergent communication referential game deep learning"

Links: [{"title":"Emergence of Linguistic Communication from Referential Games with Symbolic and Pixel Input | Request PDF","url":"https://www.researchgate.net/publication/324472390_Emergence_of_Linguistic_Communication_from_Referential_Games_with_Symbolic_and_Pixel_Input"},{"title":"Emergence of Language with Multi-agent Games: Learning ...","url":"https://arxiv.org/pdf/1705.11192"},{"title":"[2006.02419] Emergent Multi-Agent Communication in the Deep Learning Era","url":"https://ar5iv.labs.arxiv.org/html/2006.02419"},{"title":"Emergent Communication Models in AI","url":"https://www.emergentmind.com/topics/emergent-communication-models"},{"title":"Deep Learning-Based Emergent Communication","url":"https://www.emergentmind.com/topics/deep-learning-based-emergent-communication"},{"title":"Frontiers | Emergent communication of multimodal deep generative models based on Metropolis-Hastings naming game","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2023.1290604/full"},{"title":"[2410.18806] A Combinatorial Approach to Neural Emergent Communication","url":"https://arxiv.org/abs/2410.18806"},{"title":"[PDF] Emergent Communication of Generalizations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Emergent-Communication-of-Generalizations-Mu-Goodman/c524002fb88ce10a5ca0bfb92f055ca52252ca90"},{"title":"Emergent communication and learning pressures in language models: a language evolution perspective","url":"https://arxiv.org/html/2403.14427v1"},{"title":"Emergent Communication: Generalization and Overfitting in Lewis Games","url":"https://proceedings.neurips.cc/paper_files/paper/2022/file/093b08a7ad6e6dd8d34b9cc86bb5f07c-Paper-Conference.pdf"}]

I've found relevant research on your query about message reconstruction auxiliary loss in emergent communication and referential games. Here are the key findings:

## Overview of the Research Area

Deep learning-based emergent communication is an approach where neural agents spontaneously develop structured protocols through goal-oriented referential games and reinforcement learning, with multi-agent systems—typically instantiated as neural networks—spontaneously developing discrete or structured communication protocols through interactive, goal-oriented tasks.

## Referential Games Framework

A classic template is the referential game: a sender observes an object and, without explicit linguistic grounding, generates a message intended to help a receiver identify the object or perform a goal. The referential game serves as the canonical experimental testbed for inducing language emergence in deep agents, where the speaker is given a target (symbolic vector or image) and generates a message. The receiver views the message and a candidate set (target + distractors) and selects the most likely target. Reward is only granted for communicative success.

## Message Reconstruction in Learning

The receiver is trained to infer the sender's input based on the message, by selecting the correct object among distractors or by fully reconstructing it. A Reassembly game is a reconstruction task-based Lewis signaling game in which communicating agents have different pre-trained VAE, and experimental results show that the emergent language learned in the Reassembly game showed high compositionality on several metrics than the emergent language learned in other reconstruction task-based Lewis signaling game settings.

## Auxiliary Tasks and Loss Functions

The ETHER agent addresses limitations by means of (i) a discriminative visual referential game, commonly studied in the subfield of Emergent Communication (EC), used here as an unsupervised auxiliary task and (ii) a semantic grounding scheme to align the emergent language with natural language. The final loss is a weighted sum of losses for the two tasks L = Lcaption + λLgame.

The research shows how auxiliary loss functions combining reconstruction tasks and game-based objectives help agents develop more structured and compositional emergent communication protocols.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e20edef-fdc5-4953-b6fe-223f51cca0a6",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "e4397af7-b790-4b09-8f16-e6f632b42b56",
  "sourceToolAssistantUUID": "9e20edef-fdc5-4953-b6fe-223f51cca0a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-10T20:21:25.967Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015AS5gtGmm9L7GNqxS7C5o1`</summary>

```json
{
  "query": "MAPoRL multi-agent post-training collaborative reinforcement learning ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4397af7-b790-4b09-8f16-e6f632b42b56",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWYERbdbSZKotq76S4s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2720a25a-1d72-4502-ad6b-a184979a75ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196xVYxQXEEPW5UqxERmQG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2016,
      "cache_creation_input_tokens": 3039,
      "cache_read_input_tokens": 28103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3039,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-10T20:21:26.650Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VfWQThHWMttoQtxhPTip4w`</summary>

```json
{
  "query": "Graph-GRPO multi-agent topology optimization communication graph 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2720a25a-1d72-4502-ad6b-a184979a75ee",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWYERbdbSZKotq76S4s",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08cd838f-af47-45a5-bd98-1831cbf12162",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196xVYxQXEEPW5UqxERmQG4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2016,
      "cache_creation_input_tokens": 3039,
      "cache_read_input_tokens": 28103,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3039
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2016,
          "output_tokens": 118,
          "cache_read_input_tokens": 28103,
          "cache_creation_input_tokens": 3039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3039,
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

_source line 57 · 2026-05-10T20:21:30.569Z_

<details><summary>↩ Tool result · `toolu_015AS5gtGmm9L7GNqxS7C5o1`</summary>

```text
Web search results for query: "MAPoRL multi-agent post-training collaborative reinforcement learning ACL 2025"

Links: [{"title":"MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1459/"},{"title":"[2502.18439] MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning","url":"https://arxiv.org/abs/2502.18439"},{"title":"Publication","url":"https://chanwoo-park-official.github.io/publication/"},{"title":"MAPoRL2: Multi-Agent Post-Co-Training for Collaborative ...","url":"https://aclanthology.org/2025.acl-long.1459.pdf"},{"title":"MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=f85TQ7hyzh"},{"title":"[PDF] MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MAPoRL:-Multi-Agent-Post-Co-Training-for-Large-with-Park-Han/aa89c6bf86486e180833037333555e3492b15c8e"},{"title":"MAPoRL: Multi-Agent Post-Co-Training for Collaborative ...","url":"https://arxiv.org/pdf/2502.18439"},{"title":"[2502.18439v1] MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning","url":"http://arxiv.org/abs/2502.18439v1"},{"title":"Stronger-MAS: Multi-Agent Reinforcement Learning for Collaborative LLMs","url":"https://arxiv.org/html/2510.11062"},{"title":"ICML MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning","url":"https://icml.cc/virtual/2025/49316"}]

I've successfully found comprehensive information about MAPoRL. Here's what the search results reveal:

## Overview

MAPoRL: Multi-Agent Post-Co-Training for Collaborative Large Language Models with Reinforcement Learning was presented at the 63rd Annual Meeting of the Association for Computational Linguistics (ACL) in Vienna, Austria. The paper was authored by Chanwoo Park, Seungju Han, Xingzhi Guo, Asuman E. Ozdaglar, Kaiqing Zhang, and Joo-Kyung Kim.

## Key Innovation

Unlike existing LLM post-training paradigms, MAPoRL advocates the co-training of multiple LLMs together using RL for better generalization.

## How It Works

In MAPoRL, multiple LLMs first generate their own responses independently and engage in a multi-turn discussion to collaboratively improve the final answer. A MAPoRL verifier evaluates both the answer and the discussion, by assigning a score that verifies the correctness of the answer, while adding incentives to encourage corrective and persuasive discussions. The score serves as the co-training reward, and is then maximized through multi-agent RL.

## Results

Training individual LLMs alone is insufficient to induce effective collaboration, while multi-agent co-training can boost the collaboration performance across benchmarks, with generalization to unseen domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2720a25a-1d72-4502-ad6b-a184979a75ee",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "fb806f0e-4436-4cd6-a917-30583dac8fae",
  "sourceToolAssistantUUID": "2720a25a-1d72-4502-ad6b-a184979a75ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-10T20:21:33.711Z_

<details><summary>↩ Tool result · `toolu_01VfWQThHWMttoQtxhPTip4w`</summary>

```text
Web search results for query: "Graph-GRPO multi-agent topology optimization communication graph 2026"

Links: [{"title":"Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group...","url":"https://arxiv.org/abs/2603.02701"},{"title":"Graph-GRPO: Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization","url":"https://arxiv.org/html/2603.02701v1"},{"title":"Learning Multi-Agent Communication from Graph Modeling Perspective | OpenReview","url":"https://openreview.net/forum?id=Qox9rO0kN0"},{"title":"ResMAS: Resilience Optimization in LLM-based Multi-agent Systems","url":"https://arxiv.org/html/2601.04694"},{"title":"Assemble Your Crew: Automatic Multi-agent Communication Topology Design","url":"https://arxiv.org/pdf/2507.18224"},{"title":"[2604.09703] Cayley Graph Optimization for Scalable Multi-Agent Communication Topologies","url":"https://arxiv.org/abs/2604.09703"},{"title":"G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks","url":"https://arxiv.org/html/2410.11782v1"},{"title":"Cayley Graph Optimization for Scalable Multi-Agent Communication Topologies","url":"https://arxiv.org/html/2604.09703"},{"title":"Dynamic Generation of Multi LLM Agents Communication Topologies with Graph Diffusion Models","url":"https://arxiv.org/html/2510.07799v1"},{"title":"GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems","url":"https://arxiv.org/html/2603.19677v1"}]

I've found relevant research on your query. Here are the key findings:

## Graph-GRPO: Stabilizing Multi-Agent Topology Learning

Graph-GRPO is a novel topology optimization framework that integrates Group Relative Policy Optimization. Optimizing communication topology is fundamental to the efficiency and effectiveness of Large Language Model (LLM)-based Multi-Agent Systems (MAS).

### Key Approach

Instead of evaluating a single topology in isolation, Graph-GRPO samples a group of diverse communication graphs for each query and computes the advantage of specific edges based on their relative performance within the group. By normalizing rewards across the sampled group, the method effectively mitigates the noise derived from task difficulty variance and enables fine-grained credit assignment.

### Problem It Addresses

Recent approaches utilize reinforcement learning to dynamically construct task-specific graphs, but typically rely on single-sample policy gradients with absolute rewards. This paradigm suffers from severe gradient variance and the credit assignment problem: simple queries yield non-informative positive rewards for suboptimal structures, while difficult queries often result in failures that provide no learning signal.

### Results

Extensive experiments on reasoning and code generation benchmarks demonstrate that Graph-GRPO significantly outperforms state-of-the-art baselines, achieving superior training stability and identifying critical communication pathways previously obscured by reward noise.

The paper was published in March 2026 from researchers at Tsinghua University and Donghua University.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08cd838f-af47-45a5-bd98-1831cbf12162",
  "isSidechain": true,
  "promptId": "e428cf44-342c-4bc5-88b8-72420713d432",
  "agentId": "adc656e1cd45fd18f",
  "type": "user",
  "uuid": "c5841a7b-59ec-4f3e-88b0-0da5c19c8a6a",
  "sourceToolAssistantUUID": "08cd838f-af47-45a5-bd98-1831cbf12162",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-10T20:22:51.506Z_

Here is my consolidated report on competing and closely related work to SGIR.

---

## Closely Related and Competing Work for SGIR

### TIER 1: MOST DIRECTLY RELEVANT (same problem space -- training text-based communication in multi-agent LLM systems with auxiliary/dense signals)

**1. "Training Language Models for Social Deduction with Multi-Agent Reinforcement Learning"**
- Venue: AAMAS 2025 | Authors: (Among Us team) | [Paper](https://www.ifaamas.org/Proceedings/aamas2025/pdfs/p1830.pdf)
- Uses **auxiliary dense rewards** to train LLM agents to communicate in free-form text. Decomposes communication into "listening" (predicting environment info from messages) and "speaking" (rewarding messages based on influence on others). Achieves 2x win rate over standard RL.
- **Relevance to SGIR**: This is the closest competitor. Both use auxiliary losses to provide dense signal for text communication training. The listening reward (predicting environment state from messages) is conceptually similar to SGIR's reconstruction objective, but operates on environment facts rather than hidden-state intent embeddings. SGIR should cite and differentiate from this work explicitly.

**2. "ThoughtComm: Thought Communication in Multiagent Collaboration"**
- Venue: NeurIPS 2025 | Authors: MBZUAI, CMU, Meta AI | [OpenReview](https://openreview.net/forum?id=tq9lyV9Cml)
- Extracts **latent thoughts from agents' internal states** and enables direct "mind-to-mind" communication, bypassing natural language. Formalizes thought extraction as a latent variable model and proves identifiability of shared/private thoughts. 67% relative improvement over single-agent, 19% over multi-agent finetuning SOTA.
- **Relevance to SGIR**: Both extract hidden-state representations for communication. ThoughtComm bypasses text entirely (latent-to-latent), while SGIR keeps text as the communication medium but reconstructs hidden states as an auxiliary loss. The proposal should discuss how SGIR differs by preserving text interpretability.

**3. "LatentMAS: Latent Collaboration in Multi-Agent Systems"**
- Venue: ICML 2026 (Spotlight) | [arXiv:2511.20639](https://arxiv.org/abs/2511.20639)
- Enables **latent collaboration via KV-cache transfer** -- agents share last-layer hidden embeddings as "latent working memory" instead of text. Training-free. Up to 14.6% higher accuracy, 70-84% token reduction, 4x faster inference.
- **Relevance to SGIR**: Another latent-space communication approach. LatentMAS is training-free and replaces text entirely. SGIR trains with text messages but uses hidden-state reconstruction as auxiliary supervision. The proposal should position SGIR as complementary for settings where text communication is required (e.g., interpretability, human-in-the-loop).

**4. "DiffMAS: Learning to Communicate -- Toward End-to-End Optimization of Multi-Agent Language Systems"**
- arXiv: 2604.21794 (April 2026) | [Paper](https://arxiv.org/abs/2604.21794)
- Treats **latent communication as a learnable component** via parameter-efficient supervised training over multi-agent latent trajectories. Jointly optimizes how information is encoded and interpreted across interactions. Backbone LLM stays frozen; lightweight LoRA adapters optimized.
- **Relevance to SGIR**: Concurrent work (April 2026). Both aim to optimize inter-agent communication jointly. DiffMAS operates in latent space with LoRA; SGIR uses text with MLP reconstruction. Strong concurrent competitor.

**5. MAPoRL: "Multi-Agent Post-Co-Training for Collaborative LLMs with RL"**
- Venue: ACL 2025 / ICML 2025 | [ACL Anthology](https://aclanthology.org/2025.acl-long.1459/) | [arXiv:2502.18439](https://arxiv.org/abs/2502.18439)
- Co-trains multiple LLMs via RL with a **verifier that scores both the answer and the multi-turn discussion quality**, incentivizing corrective/persuasive communication. Uses multi-agent RL with a discussion-aware reward.
- **Relevance to SGIR**: Both train LLM communication via RL. MAPoRL uses a verifier-based reward for discussion quality (sparse), while SGIR uses reconstruction-based dense auxiliary loss. Complementary approaches.

---

### TIER 2: STRONGLY RELATED (multi-agent LLM training with RL, communication optimization)

**6. MARTI: "A Framework for Multi-Agent LLM Systems Reinforced Training and Inference"**
- Venue: ICLR 2026 | [OpenReview](https://openreview.net/forum?id=E7jZqo0A50)
- Open-source framework for training multi-agent LLM systems with RL. Supports debate, chain-of-agents, mixture-of-agents workflows. Centralized interaction, distributed policy training.
- **Relevance**: General framework for multi-agent LLM RL training. SGIR could potentially be integrated as an auxiliary loss module within MARTI.

**7. MAGRPO: "LLM Collaboration With Multi-Agent Reinforcement Learning"**
- Venue: AAAI 2026 | [arXiv:2508.04652](https://arxiv.org/abs/2508.04652)
- Extends GRPO to multi-agent settings (Dec-POMDP formulation). Centralized group-relative advantages, decentralized execution.
- **Relevance**: Since SGIR builds on GRPO for multi-agent training, MAGRPO is directly relevant as the multi-agent GRPO baseline. SGIR adds the reconstruction auxiliary loss on top of this kind of approach.

**8. Graph-GRPO: "Stabilizing Multi-Agent Topology Learning via Group Relative Policy Optimization"**
- arXiv: 2603.02701 (March 2026)
- Optimizes **communication topology** (who talks to whom) via GRPO with group-sampled graphs.
- **Relevance**: Optimizes communication structure rather than content. Orthogonal to SGIR (which optimizes message content via reconstruction loss). Could be combined.

**9. M-GRPO: "Multi-Agent Deep Research: Training Multi-Agent Systems with M-GRPO"**
- arXiv: 2511.13288 | [Paper](https://arxiv.org/abs/2511.13288)
- Hierarchical GRPO for vertical multi-agent systems (planner + sub-agents).
- **Relevance**: Another GRPO extension for multi-agent training. SGIR's auxiliary loss could supplement M-GRPO's training signal.

---

### TIER 3: RELATED TECHNIQUES AND FOUNDATIONS

**10. "EMA Policy Gradient: Taming RL for LLMs with EMA Anchor and Top-k KL"**
- arXiv: 2602.04417 (February 2026) | [Paper](https://arxiv.org/abs/2602.04417)
- Replaces fixed anchor/reference policy in GRPO-style training with an **EMA-updated anchor**. Derives stability conditions. Improves Pass@1 and prevents Pass@N collapse.
- **Relevance to SGIR**: Directly relevant to SGIR's EMA target stabilization component. If SGIR uses EMA for stabilizing reconstruction targets, this paper's stability analysis and conditions should be cited. They may provide theoretical grounding for SGIR's EMA design choices.

**11. "Intention Sharing in Multi-Agent RL" (IS)**
- Venue: ICLR 2021 | [OpenReview](https://openreview.net/forum?id=qpsl2dR9twy)
- Agents share **imagined future trajectories** as intentions. Uses attention to encode trajectory components into messages.
- **Relevance**: Classic precursor. SGIR reconstructs sender intent from messages; IS explicitly shares intent as message content. Different direction (reconstruct vs. transmit) but same motivation.

**12. DIAL: "Learning to Communicate with Deep Multi-Agent RL" (Foerster et al.)**
- Venue: NeurIPS 2016 | [Paper](https://arxiv.org/abs/1605.06676)
- Foundational work. DIAL allows **gradient flow through communication channels** during centralized training; discretizes at execution. RIAL uses stop-gradient (no inter-agent gradients).
- **Relevance**: SGIR's stop-gradient detachment on the reconstruction target echoes RIAL's design philosophy of blocking certain gradient paths. The proposal should discuss how SGIR's stop-gradient differs from DIAL/RIAL's design.

**13. A2LS: "Reinforcement Learning with Automated Auxiliary Loss Search"**
- Venue: NeurIPS 2022 | [Paper](https://arxiv.org/abs/2210.06041) | Microsoft Research
- Automatically searches for optimal auxiliary loss functions in RL from a space of 7.5x10^20 candidates.
- **Relevance**: Methodological comparison -- SGIR hand-designs the auxiliary loss (reconstruction), while A2LS would search for it. The proposal could discuss whether SGIR's reconstruction loss could be discovered automatically.

**14. LSPO: "Learning Strategic Language Agents in the Werewolf Game with Iterative Latent Space Policy Optimization"**
- Venue: ICML 2025 | [arXiv:2502.04686](https://arxiv.org/abs/2502.04686)
- Optimizes in a **compact latent strategy space** rather than the combinatorial language space. Combines game theory with LLM fine-tuning.
- **Relevance**: Uses latent representations for strategic communication training. Different approach (latent policy vs. reconstruction loss) but related motivation of using latent spaces to improve text communication.

**15. Multi-agent KTO (MaKTO): "Enhancing Strategic Interactions of LLMs in Language Games"**
- Venue: NeurIPS 2025
- Uses **Kahneman-Tversky Optimization** with unpaired desirable/unacceptable responses from multi-agent gameplay.
- **Relevance**: Alternative RL objective for multi-agent text communication. Different from GRPO+auxiliary loss but same goal.

**16. "Cut the Crap" / AgentPrune**
- Venue: ICLR 2025 | [arXiv:2410.02506](https://arxiv.org/abs/2410.02506)
- Prunes redundant communication messages via trainable graph masks. Reduces tokens 28-73%.
- **Relevance**: Focuses on communication efficiency (what to prune) rather than content quality (what to say). Complementary to SGIR.

**17. "Generative Emergent Communication: LLM is a Collective World Model" (Taniguchi et al.)**
- Published: Advanced Robotics, 2026 | [arXiv:2501.00226](https://arxiv.org/abs/2501.00226)
- Models language emergence as **decentralized Bayesian inference** with encoder-decoder structure at societal scale. LLM decodes symbols to reconstruct latent space.
- **Relevance**: Theoretical framing. The reconstruction perspective (decode messages to reconstruct latent representations) is philosophically aligned with SGIR's approach.

---

### KEY GAPS THE PROPOSAL SHOULD ADDRESS

1. **The Among Us / Social Deduction paper (AAMAS 2025)** is the most dangerous omission -- it uses auxiliary dense rewards for LLM communication training in a very similar spirit.
2. **ThoughtComm (NeurIPS 2025)** and **LatentMAS (ICML 2026 Spotlight)** are the main latent-space communication competitors. SGIR needs to clearly position itself as preserving text interpretability while using reconstruction only as training signal.
3. **EMA Policy Gradient (arXiv 2602.04417)** provides theoretical stability analysis for EMA in GRPO-like settings that SGIR should cite for its EMA target component.
4. **DiffMAS (arXiv April 2026)** is concurrent work optimizing inter-agent communication end-to-end.
5. **MAGRPO (AAAI 2026)** is the multi-agent GRPO baseline that SGIR likely builds on or competes with.

Sources:
- [Training Language Models for Social Deduction with MARL (AAMAS 2025)](https://www.ifaamas.org/Proceedings/aamas2025/pdfs/p1830.pdf)
- [ThoughtComm (NeurIPS 2025)](https://openreview.net/forum?id=tq9lyV9Cml)
- [LatentMAS (ICML 2026 Spotlight)](https://arxiv.org/abs/2511.20639)
- [DiffMAS (arXiv April 2026)](https://arxiv.org/abs/2604.21794)
- [MAPoRL (ACL 2025)](https://aclanthology.org/2025.acl-long.1459/)
- [MARTI (ICLR 2026)](https://openreview.net/forum?id=E7jZqo0A50)
- [MAGRPO (AAAI 2026)](https://arxiv.org/abs/2508.04652)
- [Graph-GRPO (arXiv March 2026)](https://arxiv.org/abs/2603.02701)
- [M-GRPO (arXiv 2511)](https://arxiv.org/abs/2511.13288)
- [EMA Policy Gradient (arXiv Feb 2026)](https://arxiv.org/abs/2602.04417)
- [Intention Sharing (ICLR 2021)](https://openreview.net/forum?id=qpsl2dR9twy)
- [DIAL (NeurIPS 2016)](https://arxiv.org/abs/1605.06676)
- [A2LS (NeurIPS 2022)](https://arxiv.org/abs/2210.06041)
- [LSPO Werewolf (ICML 2025)](https://arxiv.org/abs/2502.04686)
- [Multi-agent KTO (NeurIPS 2025)](https://neurips.cc/virtual/2025/poster/117599)
- [AgentPrune / Cut the Crap (ICLR 2025)](https://arxiv.org/abs/2410.02506)
- [Generative Emergent Communication (2026)](https://arxiv.org/abs/2501.00226)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5841a7b-59ec-4f3e-88b0-0da5c19c8a6a",
  "isSidechain": true,
  "agentId": "adc656e1cd45fd18f",
  "requestId": "req_011CauWZ563qM7CNp3HxgBNk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8fe2b3d6-8c07-4d35-be9f-16075f104d04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f2d7a3bf-a23d-4efa-9357-fb35b1845602",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGBCoQdydtwCxUQ2NZjDXv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3845,
      "cache_read_input_tokens": 31142,
      "output_tokens": 3666,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3845
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3666,
          "cache_read_input_tokens": 31142,
          "cache_creation_input_tokens": 3845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3845,
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
