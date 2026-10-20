# Research conversation: Search the web for recent papers (2025-2026) that might be concurrent or competing work with the idea of "bilateral cont

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a6e82473bf7a9063b.jsonl`
- **Structured JSON:** [`ee76586ed26132ce9718.json`](../../sessions/ee/ee76586ed26132ce9718.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

58 recorded events

### User

_source line 1 · 2026-05-10T22:11:34.463Z_

Search the web for recent papers (2025-2026) that might be concurrent or competing work with the idea of "bilateral contrastive training for multi-agent LLM communication." I need to find papers the proposal might have missed. Search for:

1. "bilateral communication training LLM agents 2026" 
2. "contrastive learning multi-agent communication LLM 2026"
3. "sender receiver alignment multi-agent 2026"
4. "intent grounding multi-agent reinforcement learning 2026"
5. "communication quality training multi-agent LLM GRPO"
6. Search arxiv for any papers from March-May 2026 about multi-agent LLM communication training

Also specifically search for:
- Any paper that does end-to-end bilateral contrastive training of sender AND receiver in multi-agent LLM systems
- Any paper applying CLIPO-style contrastive loss to multi-agent communication

Report all relevant papers found with titles, venues, and brief descriptions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "e8563164-5dfe-4c51-83e9-8b961df031fd",
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

_source line 2 · 2026-05-10T22:11:34.466Z_

```json
{
  "parentUuid": "e8563164-5dfe-4c51-83e9-8b961df031fd",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
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
  "uuid": "2fdd4bf9-5d03-476b-ae19-8af2e9170a68",
  "timestamp": "2026-05-10T22:11:34.466Z",
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

_source line 3 · 2026-05-10T22:11:37.479Z_



I'll search for all these topics in parallel. Let me first load the WebSearch tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fdd4bf9-5d03-476b-ae19-8af2e9170a68",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauewe7TNJstGpZyhVUqE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7cc0737-6212-4ca1-821f-119e1682df7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4dS7dGRoxtabDMc8opE7a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 777,
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

_source line 4 · 2026-05-10T22:11:37.727Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013yiAoLUriT4b2h27LPR36X`</summary>

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
  "parentUuid": "a7cc0737-6212-4ca1-821f-119e1682df7c",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauewe7TNJstGpZyhVUqE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ba3c21a-d350-4ca8-8adb-5c9b458bbcce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4dS7dGRoxtabDMc8opE7a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 8223,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 777
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 777,
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

_source line 5 · 2026-05-10T22:11:37.730Z_

<details><summary>↩ Tool result · `toolu_013yiAoLUriT4b2h27LPR36X`</summary>

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
  "parentUuid": "6ba3c21a-d350-4ca8-8adb-5c9b458bbcce",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "d3df2813-cc4a-4071-b694-d1714da4b0d6",
  "sourceToolAssistantUUID": "6ba3c21a-d350-4ca8-8adb-5c9b458bbcce",
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

_source line 6 · 2026-05-10T22:11:40.614Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3df2813-cc4a-4071-b694-d1714da4b0d6",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011CauewtUPzeFJWiwZHgHXr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7fb122d4-621c-4bd1-a593-bdaff50ed1ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYGQ1WY93nKzV1nTpq6NrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 7 · 2026-05-10T22:11:41.235Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TKcbv3ak6ZfXhmQLQKShbL`</summary>

```json
{
  "query": "bilateral communication training LLM agents 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fb122d4-621c-4bd1-a593-bdaff50ed1ee",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011CauewtUPzeFJWiwZHgHXr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9252ebd8-eb7a-4a6f-97bd-f6174de050ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYGQ1WY93nKzV1nTpq6NrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 8 · 2026-05-10T22:11:41.571Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LK8MfpbVf9oK6mp3FsGarZ`</summary>

```json
{
  "query": "contrastive learning multi-agent communication LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9252ebd8-eb7a-4a6f-97bd-f6174de050ae",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011CauewtUPzeFJWiwZHgHXr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a58b9b7f-8a71-4ec0-830d-4137642047f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYGQ1WY93nKzV1nTpq6NrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 9 · 2026-05-10T22:11:42.049Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TMyuqxwHNRa9G6jfae16Bm`</summary>

```json
{
  "query": "sender receiver alignment multi-agent 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a58b9b7f-8a71-4ec0-830d-4137642047f5",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011CauewtUPzeFJWiwZHgHXr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a70d5eb5-33d8-47a8-a46f-481bdce0ecc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYGQ1WY93nKzV1nTpq6NrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 10 · 2026-05-10T22:11:42.526Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01831X4iXU27afk5737vFmEa`</summary>

```json
{
  "query": "intent grounding multi-agent reinforcement learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a70d5eb5-33d8-47a8-a46f-481bdce0ecc2",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011CauewtUPzeFJWiwZHgHXr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cdabe06-5df5-4bd1-a9f4-b1fbc51289ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYGQ1WY93nKzV1nTpq6NrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 11 · 2026-05-10T22:11:43.515Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016mc7xfAckD5uqgYQEgHyBj`</summary>

```json
{
  "query": "communication quality training multi-agent LLM GRPO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cdabe06-5df5-4bd1-a9f4-b1fbc51289ef",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011CauewtUPzeFJWiwZHgHXr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "190139d9-9a37-4489-9cee-b4dcf4240c25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYGQ1WY93nKzV1nTpq6NrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 12 · 2026-05-10T22:11:43.919Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JHCMNF3vwgprQVA81phiX2`</summary>

```json
{
  "query": "arxiv multi-agent LLM communication training 2026 March April May"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "190139d9-9a37-4489-9cee-b4dcf4240c25",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011CauewtUPzeFJWiwZHgHXr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e480689-88fa-4713-b8bb-9f7c2e10e6fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FYGQ1WY93nKzV1nTpq6NrA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

### Tool result

_source line 13 · 2026-05-10T22:11:48.683Z_

<details><summary>↩ Tool result · `toolu_01TKcbv3ak6ZfXhmQLQKShbL`</summary>

```text
Web search results for query: "bilateral communication training LLM agents 2026"

Links: [{"title":"July 2026 1 LLM-enabled Social Agents","url":"https://arxiv.org/pdf/2605.02335"},{"title":"GitHub - HenryPengZou/Awesome-Human-Agent-Collaboration-Interaction-Systems: [ACL 2026] LLM-Based Human-Agent Collaboration and Interaction Systems: A Survey | Awesome Human-Agent Collaboration | Human-AI Collaboration · GitHub","url":"https://github.com/HenryPengZou/Awesome-Human-Agent-Collaboration-Interaction-Systems"},{"title":"LLM Collaboration with Multi-Agent Reinforcement Learning","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40487/44448"},{"title":"LLM Agents","url":"https://llmagents.github.io/"},{"title":"Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces","url":"https://arxiv.org/html/2605.02801v1"},{"title":"GitHub - AGI-Edgerunners/LLM-Agents-Papers: A repo lists papers related to LLM based agent · GitHub","url":"https://github.com/AGI-Edgerunners/LLM-Agents-Papers"},{"title":"Exploring Communication Strategies for Collaborative LLM Agents in Mathematical Problem-SolvingThe manuscript has been accepted for presentation at the 26th International Conference on Artificial Intelligence in Education (AIED 2025), to be held from July 22–26, 2025, in Palermo, Italy.","url":"https://arxiv.org/html/2507.17753v1"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"LLM News Today (May 2026) – AI Model Releases","url":"https://llm-stats.com/ai-news"},{"title":"Chain of Agents: Large language models collaborating on long-context tasks","url":"https://research.google/blog/chain-of-agents-large-language-models-collaborating-on-long-context-tasks/"}]

Based on the search results, here are findings about bilateral communication training for LLM agents in 2026:

## Recent Research and Developments

Large Language Models (LLMs) have transformed agent–agent and human–agent interaction by enabling software, physical, and simulation agents to communicate and deliberate through natural language.

### Communication Training Approaches

Effective communication strategies among LLM agents improve collaborative problem-solving efficiency and facilitate cost-effective adoption in education. Research in this area has explored various communication strategies for dual-agent systems, with LLM agents leveraging complementary reasoning processes to cross-validate ideas, refine their understanding, and ultimately produce more robust solutions than single-agent approaches.

### Multi-Agent Communication Mechanisms

In collaborative agent systems, workers read and process sequentially, each receiving the message from the previous worker and transferring the useful updated information to the next, with a manager agent receiving the complete evidence and generating the final response.

Classical MARL has a long tradition of communication-level credit, with recent work including message-level debate outcomes as reward signals and counterfactual message-level credit estimation.

### Current Research Gaps

As of May 2026, agent-, role-, and turn-level credit credit mechanisms are denser, but published work still lacks composition of explicit credit mechanisms across all these levels. This indicates that bilateral communication training remains an active area of research with opportunities for further development.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9252ebd8-eb7a-4a6f-97bd-f6174de050ae",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "58b1205d-1be2-4a73-b49a-30a33f9a7ce3",
  "sourceToolAssistantUUID": "9252ebd8-eb7a-4a6f-97bd-f6174de050ae",
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

_source line 14 · 2026-05-10T22:11:48.715Z_

<details><summary>↩ Tool result · `toolu_01LK8MfpbVf9oK6mp3FsGarZ`</summary>

```text
Web search results for query: "contrastive learning multi-agent communication LLM 2026"

Links: [{"title":"CLEAR: Context Augmentation from Contrastive Learning of Experience via Agentic Reflection","url":"https://arxiv.org/html/2604.07487"},{"title":"Learning To Ground Decentralized Multi-Agent Communication with Contrastive Learning | OpenReview","url":"https://openreview.net/forum?id=rLceWXWCmZc"},{"title":"Downloads 2025","url":"https://iclr.cc/Downloads/2025"},{"title":"Aligning Backchannel and Dialogue Context Representations via Contrastive LLM Fine-Tuning | OpenReview","url":"https://openreview.net/forum?id=wBajQcrGEv"},{"title":"(PDF) Learning to Ground Decentralized Multi-Agent Communication with Contrastive Learning","url":"https://www.researchgate.net/publication/359079677_Learning_to_Ground_Decentralized_Multi-Agent_Communication_with_Contrastive_Learning"},{"title":"Towards Communication Efficient Multi-Agent Cooperations: Reinforcement Learning and LLM","url":"https://www.techrxiv.org/users/878096/articles/1259644-towards-communication-efficient-multi-agent-cooperations-reinforcement-learning-and-llm"},{"title":"LLM Collaboration With Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2508.04652v1"},{"title":"GitHub - taichengguo/LLM_MultiAgents_Survey_Papers: Large Language Model based Multi-Agents: A Survey of Progress and Challenges (In IJCAI 2024) · GitHub","url":"https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers"},{"title":"ICLR 2026 Workshop on Multi-Agent Learning and Generative ...","url":"https://iclr26-mal-gai.github.io/"},{"title":"LLMs for Multi-Agent Cooperation | Xueguang Lyu","url":"https://xue-guang.com/post/llm-marl/"}]

I've completed the web search for "contrastive learning multi-agent communication LLM 2026". Here are the key findings:

## Recent Research Areas

Contrastive signals are widely used to learn robust representations by explicitly comparing informative alternatives, and in LLM-agent settings, a closely related idea appears in reflection-based methods that learn from behavioral differences across trials, especially between successful and failed executions.

## Multi-Agent Communication with Contrastive Learning

Researchers propose a method to ground decentralized multi-agent communication based on contrastive learning to maximize the mutual information between messages within a trajectory, considering messages as incomplete views of environment states.

## LLM-Based Multi-Agent Systems

CAMEL explored role-playing-based cooperative communication, while MetaGPT and ChatDev organized agents into software-engineering teams following structured workflows, and AutoGen provided a general-purpose multi-agent conversation framework with human-in-the-loop support.

LLM-based Multi-Agent Systems refer to computational systems comprising multiple intelligent agents powered by large language models that can perceive, learn, reason, and act collaboratively, encompassing five essential components: profile, perception, self-action, mutual interaction, and evolution.

## Recent Work (2025-2026)

An LLM-based Bandwidth-Adaptive Dual-Policy framework leverages LLM-based multi-agents to adapt to varying bandwidth constraints by simply modifying the input prompt, thereby eliminating the need for retraining.

The search results show active development in combining contrastive learning approaches with multi-agent LLM systems, with emphasis on communication efficiency, coordination mechanisms, and emergent behavior in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a58b9b7f-8a71-4ec0-830d-4137642047f5",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "d5d0a854-7701-4172-b982-2f09a0fb9468",
  "sourceToolAssistantUUID": "a58b9b7f-8a71-4ec0-830d-4137642047f5",
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

_source line 15 · 2026-05-10T22:11:49.100Z_

<details><summary>↩ Tool result · `toolu_01TMyuqxwHNRa9G6jfae16Bm`</summary>

```text
Web search results for query: "sender receiver alignment multi-agent 2026"

Links: [{"title":"GitHub - xz-liu/heterogeneous-latent-mas: The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems · GitHub","url":"https://github.com/xz-liu/heterogeneous-latent-mas"},{"title":"Best Multi-Agent Frameworks in 2026: LangGraph, CrewAI ...","url":"https://gurusup.com/blog/best-multi-agent-frameworks-2026"},{"title":"Multi-agent routing - OpenClaw","url":"https://docs.openclaw.ai/concepts/multi-agent"},{"title":"WMAC 2026 - Overview | WMAC 2026: AAAI 2026 Bridge Program on Advancing LLM-Based Multi-Agent Collaboration","url":"https://multiagents.org/2026/"},{"title":"How to Orchestrate Multi-Agent AI Systems at Scale in 2026","url":"https://atlan.com/know/multi-agent-system-orchestration/"},{"title":"Multi-Agent Systems & AI Orchestration Guide 2026 | Codebridge","url":"https://www.codebridge.tech/articles/mastering-multi-agent-orchestration-coordination-is-the-new-scale-frontier"},{"title":"How to Design a Production-Grade Multi-Agent Communication System Using LangGraph Structured Message Bus, ACP Logging, and Persistent Shared State Architecture - MarkTechPost","url":"https://www.marktechpost.com/2026/03/01/how-to-design-a-production-grade-multi-agent-communication-system-using-langgraph-structured-message-bus-acp-logging-and-persistent-shared-state-architecture/"},{"title":"Multi-Agent System Architecture Guide for 2026","url":"https://www.clickittech.com/ai/multi-agent-system-architecture/"},{"title":"How to Build Multi-Agent Systems: Complete 2026 Guide - DEV Community","url":"https://dev.to/eira-wexford/how-to-build-multi-agent-systems-complete-2026-guide-1io6"},{"title":"Multi-Agent Architectures, Clearly Explained","url":"https://newsletter.systemdesign.one/p/multi-agent-system"}]

Based on the search results, here's what I found regarding sender-receiver alignment in multi-agent systems for 2026:

## Key Research and Development

One notable 2026 project is "The Vision Wormhole," which introduces a Universal Visual Codec to map heterogeneous reasoning traces into a shared continuous latent space and inject them into the receiver's visual pathway. The framework adopts a hub-and-spoke topology to reduce pairwise alignment complexity from O(N^2) to O(N) and uses label-free, teacher-student distillation to align the high-speed visual channel with the robust reasoning patterns of the text pathway.

## Alignment Challenges in Multi-Agent Systems

A critical alignment problem in 2026 multi-agent systems is context inconsistency. When a supervisor agent routes a query to multiple specialist agents in parallel, the supervisor expects aligned answers it can synthesize. However, what it receives are answers derived from different definitions held in isolated memory stores, and the supervisor has no mechanism to resolve the conflict on principled grounds.

## Governance and Alignment Standards

Social norms and governance practices involve embedding multi-agent systems insights on incentives, trust, and governance into LLM-driven agents to ensure alignment across a large number of agents.

## Communication Protocols

Agent-to-Agent (A2A) by Google enables peer-to-peer collaboration, allowing agents to negotiate, share findings, and coordinate without central oversight.

The field in 2026 is actively addressing sender-receiver alignment through structured communication protocols, shared context architectures, and governance frameworks to ensure heterogeneous agents can communicate and coordinate effectively.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a70d5eb5-33d8-47a8-a46f-481bdce0ecc2",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "1830f903-6d22-4b83-96e1-dacad09f054b",
  "sourceToolAssistantUUID": "a70d5eb5-33d8-47a8-a46f-481bdce0ecc2",
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

_source line 16 · 2026-05-10T22:11:49.550Z_

<details><summary>↩ Tool result · `toolu_01831X4iXU27afk5737vFmEa`</summary>

```text
Web search results for query: "intent grounding multi-agent reinforcement learning 2026"

Links: [{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"Language Grounded Multi-agent Reinforcement Learning with Human-interpretable Communication","url":"https://arxiv.org/html/2409.17348v2"},{"title":"Language Grounded Multi-agent Reinforcement Learning with Human-interpretable Communication | OpenReview","url":"https://openreview.net/forum?id=DUHX779C5q"},{"title":"[2409.17348] Language Grounded Multi-agent Reinforcement Learning with Human-interpretable Communication","url":"https://arxiv.org/abs/2409.17348"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"Language Grounded Multi-agent Reinforcement Learning ...","url":"https://arxiv.org/pdf/2409.17348"},{"title":"Ontology-Grounded Multi-Agent Graph Reinforcement Learning (MAGRL) | by Akash Goyal | Medium","url":"https://medium.com/@aiwithakashgoyal/ontology-grounded-multi-agent-graph-reinforcement-learning-magrl-for-healthcare-7f565da526f9"},{"title":"The Rise of Reinforcement Learning Gyms and the Future of Agentic AI - Norwest","url":"https://www.norwest.com/blog/the-rise-of-reinforcement-learning-gyms-and-the-future-of-agentic-ai/"},{"title":"Language Grounded Multi-agent Reinforcement Learning with Human-interpretable Communication","url":"https://romanlee6.github.io/langground_web/"},{"title":"[2302.02662] Grounding Large Language Models in Interactive Environments with Online Reinforcement Learning","url":"https://arxiv.org/abs/2302.02662"}]

Based on the search results, here are the key findings on intent grounding in multi-agent reinforcement learning from recent research:

## Recent Research on Intent Grounding in MARL

A notable approach aligns the communication space between MARL agents with human natural language by grounding agent communications on synthetic data generated by embodied Large Language Models (LLMs), with results showing that language grounding maintains task performance while accelerating the emergence of communication.

Research indicates that through LLM integration, it's possible to capture complex information exchanged among team members in addition to individual observations, such as beliefs, intents, and requests.

## Key Applications

Multi-Agent Graph Reinforcement Learning (MAGRL) represents a change in how we represent and reason about interacting decision-makers, modeling agents as nodes in a graph and their interactions as edges. This approach has been applied to healthcare systems with ontology grounding.

In comparison to prior approaches like CICERO, newer methods involve both action and communication generated by individual RL agents that are trained end-to-end with a combination of RL loss and supervised learning loss.

## Generalization and Teamwork

Learned communication protocols exhibit zero-shot generalization capabilities in ad-hoc teamwork scenarios with unseen teammates and novel task states.

The research landscape shows active work on grounding agent intentions through language and communication protocols, particularly in collaborative multi-agent scenarios with human-agent teamwork as a key focus.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cdabe06-5df5-4bd1-a9f4-b1fbc51289ef",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "8ab79e32-bbe5-4dd0-9081-a0a76f52a197",
  "sourceToolAssistantUUID": "1cdabe06-5df5-4bd1-a9f4-b1fbc51289ef",
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

_source line 17 · 2026-05-10T22:11:51.074Z_

<details><summary>↩ Tool result · `toolu_016mc7xfAckD5uqgYQEgHyBj`</summary>

```text
Web search results for query: "communication quality training multi-agent LLM GRPO"

Links: [{"title":"LLM Collaboration with Multi-Agent Reinforcement Learning","url":"https://arxiv.org/pdf/2508.04652"},{"title":"GitHub - TsinghuaC3I/MARTI: A Framework for LLM-based Multi-Agent Reinforced Training and Inference · GitHub","url":"https://github.com/TsinghuaC3I/MARTI"},{"title":"Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces","url":"https://arxiv.org/html/2605.02801"},{"title":"Improved Multi-Agent Collaboration with Multi-Turn Reinforcement Learning","url":"https://openreview.net/pdf?id=WYfzRJgWbO"},{"title":"How to Train a Leader: Hierarchical Reasoning in Multi-Agent LLMs","url":"https://arxiv.org/pdf/2507.08960"},{"title":"LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision, and the Road Ahead | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3712003"},{"title":"Towards Communication Efficient Multi-Agent Cooperations: Reinforcement Learning and LLM","url":"https://www.techrxiv.org/users/878096/articles/1259644-towards-communication-efficient-multi-agent-cooperations-reinforcement-learning-and-llm"},{"title":"Multi-Agent Deep Research: Training Multi-Agent Systems with M-GRPO | alphaXiv","url":"https://www.alphaxiv.org/overview/2511.13288"},{"title":"Hierarchical Reasoning in Multi-Agent LLMs","url":"https://www.emergentmind.com/papers/2507.08960"},{"title":"Adapting LLM Agents Through Communication | OpenReview","url":"https://openreview.net/forum?id=wOelVq8fwL"}]

Based on the web search results, here's what I found about communication quality training in multi-agent LLM systems with GRPO:

## Overview

The search reveals several key research directions in multi-agent LLM training with GRPO-based methods:

### MAGRPO (Multi-Agent Group Relative Policy Optimization)

MAGRPO is an algorithm that optimizes agent cooperation through shared rewards, enabling agents to efficiently generate high-quality responses via effective collaboration. In multi-turn training, MAGRPO achieves higher overall returns and lower variances when trained on datasets with well-defined cooperative structures, and agents can learn to incorporate feedback effectively and improve the quality of their responses.

### Communication Quality in Multi-Agent Systems

In LLM-based multi-agent systems, every message is a natural-language utterance, which widens the communication channel (agents can transmit plans, critiques, counterfactuals) and creates a new signal/credit-assignment unit at the message level.

### M-GRPO for Hierarchical Systems

M-GRPO extends Group Relative Policy Optimization to handle training of vertical multi-agent systems with distinct LLMs, addressing variable sub-agent invocations, hierarchical credit assignment, and decoupled deployment requirements. Communication follows a structured call-return protocol, with agents having access to specialized tools.

### Communication-Efficient Approaches

LLM-based multi-agents can adapt to varying bandwidth constraints by simply modifying the input prompt, thereby eliminating the need for retraining.

These approaches represent ongoing research to improve how multi-agent LLM systems coordinate and communicate effectively through reinforcement learning training methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "190139d9-9a37-4489-9cee-b4dcf4240c25",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "810e531b-c3f4-418a-98c1-7ae75bc63767",
  "sourceToolAssistantUUID": "190139d9-9a37-4489-9cee-b4dcf4240c25",
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

_source line 18 · 2026-05-10T22:11:53.206Z_

<details><summary>↩ Tool result · `toolu_01JHCMNF3vwgprQVA81phiX2`</summary>

```text
Web search results for query: "arxiv multi-agent LLM communication training 2026 March April May"

Links: [{"title":"Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces","url":"https://arxiv.org/html/2605.02801v1"},{"title":"LLM Collaboration With Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2508.04652v1"},{"title":"[2605.02801] Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces","url":"https://arxiv.org/abs/2605.02801"},{"title":"Multiagent Systems","url":"https://arxiv.org/list/cs.MA/recent"},{"title":"July 2026 1 LLM-enabled Social Agents","url":"https://arxiv.org/pdf/2605.02335"},{"title":"Latent Collaboration in Multi-Agent Systems","url":"https://arxiv.org/html/2511.20639v1"},{"title":"Large Language Models Miss the Multi-Agent Mark Emanuele La Malfa1∗","url":"https://arxiv.org/pdf/2505.21298"},{"title":"Large Language Models Miss the Multi-Agent Mark","url":"https://arxiv.org/html/2505.21298v4"},{"title":"[2604.08567] Multi-User Large Language Model Agents","url":"https://arxiv.org/abs/2604.08567"},{"title":"Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems An Information-Controlled Empirical Study on Prediction Markets","url":"https://arxiv.org/html/2605.03310v1"}]

Based on the web search results, here are some recent arXiv papers on multi-agent LLM communication and training from March-May 2026:

## Key Recent Papers

**1. Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces**
As of May 4, 2026, this paper found no explicit RL training method for the stopping decision in orchestration learning. The paper uses orchestration traces as a working abstraction—a temporal interaction graph in which an orchestrator decides when to spawn sub-agents, whom to delegate to, how they should communicate, which tools they may call, and how their partial outputs are aggregated. Between 2025-Q2 through May 2026, the literature produced a systematic multi-agent RFT paradigm, a hierarchical GRPO decomposition for LLM teams, a single-LLM dual-role policy optimization with tool integration, a stability analysis of multi-agent GRPO, and credit-assignment methods targeting message-level counterfactuals and Shapley-based agent-level credit.

**2. Active Learning for Communication Structure Optimization**
A May 2026 paper titled "Active Learning for Communication Structure Optimization in LLM-Based Multi-Agent Systems" by Huchen Yang and colleagues was posted to arXiv.

**3. Multi-User Large Language Model Agents**
This work presents the first systematic study of multi-user LLM agents, posted in March 2026. The results reveal systematic gaps: frontier LLMs frequently fail to maintain stable prioritization under conflicting user objectives, exhibit increasing privacy violations over multi-turn interactions, and suffer from efficiency bottlenecks when coordination requires iterative information gathering.

**4. Coordination as an Architectural Layer**
A recent paper argues that coordination in LLM-based multi-agent systems should be treated as a configurable architectural layer, separable from agent logic and from information access.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e480689-88fa-4713-b8bb-9f7c2e10e6fe",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "bf98cf32-d9da-48bd-87e6-478d026e1961",
  "sourceToolAssistantUUID": "9e480689-88fa-4713-b8bb-9f7c2e10e6fe",
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

_source line 19 · 2026-05-10T22:11:55.787Z_

Now let me run the more specific searches for bilateral contrastive training and CLIP-style losses.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf98cf32-d9da-48bd-87e6-478d026e1961",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauey2DGMYnQCUpnLYFCa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34c24bbc-5cf7-4e31-bb51-c021ce26f069",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NxyhrAgCKEQ1owynRR7FS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5853,
      "cache_read_input_tokens": 10413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5853,
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

_source line 20 · 2026-05-10T22:11:56.749Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H4V55XEmNzQ4pzE6dK9ELe`</summary>

```json
{
  "query": "end-to-end bilateral contrastive training sender receiver multi-agent LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34c24bbc-5cf7-4e31-bb51-c021ce26f069",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauey2DGMYnQCUpnLYFCa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f42abd4-85f8-4ecf-963b-45cc948b56d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NxyhrAgCKEQ1owynRR7FS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5853,
      "cache_read_input_tokens": 10413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5853,
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

_source line 21 · 2026-05-10T22:11:57.231Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011EEyQXvEw55PFg9EN891yu`</summary>

```json
{
  "query": "CLIP contrastive loss multi-agent communication emergent language"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f42abd4-85f8-4ecf-963b-45cc948b56d0",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauey2DGMYnQCUpnLYFCa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7ebd78f-b501-4221-8263-ad6517b3deec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NxyhrAgCKEQ1owynRR7FS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5853,
      "cache_read_input_tokens": 10413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5853,
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

_source line 22 · 2026-05-10T22:11:58.217Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HoEZ5kzGarDeBeUEDEbyTx`</summary>

```json
{
  "query": "\"contrastive learning\" \"multi-agent communication\" grounding mutual information 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7ebd78f-b501-4221-8263-ad6517b3deec",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauey2DGMYnQCUpnLYFCa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4611384-61aa-4c68-b48f-073d21ad39f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NxyhrAgCKEQ1owynRR7FS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5853,
      "cache_read_input_tokens": 10413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5853,
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

_source line 23 · 2026-05-10T22:11:58.551Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ToMNCyXCLygqoScrf5Ff7K`</summary>

```json
{
  "query": "M-GRPO multi-agent deep research training arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4611384-61aa-4c68-b48f-073d21ad39f8",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauey2DGMYnQCUpnLYFCa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ddf535f-58da-4e78-9e78-e359509d7c4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NxyhrAgCKEQ1owynRR7FS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5853,
      "cache_read_input_tokens": 10413,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5853
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 10413,
          "cache_creation_input_tokens": 5853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5853,
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

_source line 24 · 2026-05-10T22:12:02.516Z_

<details><summary>↩ Tool result · `toolu_011EEyQXvEw55PFg9EN891yu`</summary>

```text
Web search results for query: "CLIP contrastive loss multi-agent communication emergent language"

Links: [{"title":"Learning Multi-Agent Communication with Contrastive Learning","url":"https://arxiv.org/html/2307.01403"},{"title":"CLIP: Contrastive Language–Image Pretraining","url":"https://www.emergentmind.com/topics/clip"},{"title":"(PDF) Learning to Ground Decentralized Multi-Agent Communication with Contrastive Learning","url":"https://www.researchgate.net/publication/359079677_Learning_to_Ground_Decentralized_Multi-Agent_Communication_with_Contrastive_Learning"},{"title":"CLSP: High-Fidelity Contrastive Language-State Pre-training for Agent State Representation","url":"https://arxiv.org/html/2409.15806v1"},{"title":"Understanding CLIP: the Contrastive Language-Image Pre-train | by Anna L | Medium","url":"https://medium.com/@anna.ml4fun/understanding-clip-the-contrastive-language-image-pre-train-2994ae6e9b18"},{"title":"LEARNING MULTI-AGENT COMMUNICATION WITH ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/de2ad3ed44ee4e675b3be42aa0b615d0-Paper-Conference.pdf"},{"title":"LEARNING TO GROUND DECENTRALIZED MULTI","url":"https://richielo.github.io/files/MARL_COMM_CACL_ICLR_WS_22.pdf"},{"title":"Biases for Emergent Communication in Multi-agent Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/340397814_Biases_for_Emergent_Communication_in_Multi-agent_Reinforcement_Learning"},{"title":"Language Grounded Multi-agent Communication for Ad-hoc Teamwork","url":"https://arxiv.org/html/2409.17348v1"},{"title":"[2307.01403] Learning Multi-Agent Communication with Contrastive Learning","url":"https://arxiv.org/abs/2307.01403"}]

Based on the search results, here's what I found about CLIP contrastive loss in the context of multi-agent communication and emergent language:

## Multi-Agent Communication with Contrastive Learning

In CACL (Communication Alignment Contrastive Learning), different agents' views of the same environment state are considered positive samples and messages are contrastively learned as encodings of that state. This approach treats messages within a trajectory as different incomplete views of the same environment state.

## Key Application: Emergent Language

Messages sent between agents are considered as different incomplete views of the environment state, and by examining the relationship between messages sent and received, contrastive learning is used to maximize the mutual information between messages of a given trajectory. This method outperforms previous work in both performance and learning speed, induces more symmetric communication and captures global state information from the environment, demonstrating the power of contrastive learning and the importance of leveraging messages as encodings for effective communication.

## Challenge Being Addressed

Communication is a powerful tool for coordination in multi-agent RL, but inducing an effective, common language is a difficult challenge, particularly in the decentralized setting.

## Related Approaches

Representation learning methods such as autoencoder and contrastive learning are used to ground an agent's communication on individual observations.

The research demonstrates that contrastive loss provides an effective framework for facilitating the emergence of shared communication protocols among multiple agents without requiring centralized supervision.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7ebd78f-b501-4221-8263-ad6517b3deec",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "58a65001-ca6e-4a8b-95a5-9ad340e3502a",
  "sourceToolAssistantUUID": "f7ebd78f-b501-4221-8263-ad6517b3deec",
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

_source line 25 · 2026-05-10T22:12:04.134Z_

<details><summary>↩ Tool result · `toolu_01H4V55XEmNzQ4pzE6dK9ELe`</summary>

```text
Web search results for query: "end-to-end bilateral contrastive training sender receiver multi-agent LLM"

Links: [{"title":"GitHub - TsinghuaC3I/MARTI: A Framework for LLM-based Multi-Agent Reinforced Training and Inference · GitHub","url":"https://github.com/TsinghuaC3I/MARTI"},{"title":"CLlight: Enhancing representation of multi-agent reinforcement learning with contrastive learning for cooperative traffic signal control - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S095741742402445X"},{"title":"Multi-Agent Transfer Learning Based on Contrastive Role Relationship Representation","url":"https://www.mdpi.com/2673-2688/7/1/13"},{"title":"Attention-Guided Contrastive Role Representations for Multi-agent Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=LWmuPfEYhH"},{"title":"State-Aware Routing Framework for Efficient Multi-Agent ...","url":"https://arxiv.org/pdf/2511.02200"},{"title":"Towards Communication Efficient Multi-Agent Cooperations: Reinforcement Learning and LLM","url":"https://www.techrxiv.org/users/878096/articles/1259644-towards-communication-efficient-multi-agent-cooperations-reinforcement-learning-and-llm"},{"title":"GitHub - taichengguo/LLM_MultiAgents_Survey_Papers: Large Language Model based Multi-Agents: A Survey of Progress and Challenges (In IJCAI 2024) · GitHub","url":"https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers"},{"title":"LLM Collaboration With Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2508.04652v1"},{"title":"Learning Multi-Agent Communication with Contrastive Learning","url":"https://arxiv.org/html/2307.01403"},{"title":"GitHub - LantaoYu/MARL-Papers: Paper list of multi-agent reinforcement learning (MARL) · GitHub","url":"https://github.com/LantaoYu/MARL-Papers"}]

Based on the search results, here's what I found about end-to-end bilateral contrastive training with sender-receiver multi-agent LLM systems:

## Key Research Areas

Communication Alignment Contrastive Learning (CACL) is an approach where each agent separately uses contrastive learning between their own sent and received messages to learn a communication encoding. This directly addresses bilateral (two-way) communication between agents.

In this framework, communicative messages sent between agents are considered as different incomplete views of the environment state, with different agents' messages being encodings of different incomplete "views" of the same underlying state.

## Multi-Agent LLM Systems

Recent work has focused on integrating LLMs with multi-agent reinforcement learning. MARTI is an open-source framework for training LLM-based Multi-Agent Systems (MAS) with Reinforcement Learning (RL) that enables powerful, scalable, and adaptive workflows by combining centralized multi-agent interactions with distributed policy training.

Additionally, RouterDC refines routing through contrastive learning, distinguishing fine-grained model capabilities and enabling efficient, generalizable, end-to-end allocation among multiple LLMs.

## Contrastive Learning in Multi-Agent Settings

The Multi-agent Transfer Learning Based on Contrastive Role Relationship Representation (MCRR) framework employs contrastive learning-driven role representation modeling to capture differences and commonalities of agent behavior patterns among multiple tasks, generating generalizable role representations for transfer policy networks.

These approaches combine contrastive learning objectives with multi-agent architectures to improve communication, coordination, and capability allocation in LLM-based systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f42abd4-85f8-4ecf-963b-45cc948b56d0",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "5603888e-b768-46be-b6c6-0f7080805109",
  "sourceToolAssistantUUID": "6f42abd4-85f8-4ecf-963b-45cc948b56d0",
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

_source line 26 · 2026-05-10T22:12:04.403Z_

<details><summary>↩ Tool result · `toolu_01HoEZ5kzGarDeBeUEDEbyTx`</summary>

```text
Web search results for query: ""contrastive learning" "multi-agent communication" grounding mutual information 2025 2026"

Links: [{"title":"Learning To Ground Decentralized Multi-Agent Communication with Contrastive Learning | OpenReview","url":"https://openreview.net/forum?id=rLceWXWCmZc"},{"title":"(PDF) Learning to Ground Decentralized Multi-Agent Communication with Contrastive Learning","url":"https://www.researchgate.net/publication/359079677_Learning_to_Ground_Decentralized_Multi-Agent_Communication_with_Contrastive_Learning"},{"title":"LEARNING MULTI-AGENT COMMUNICATION WITH ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/de2ad3ed44ee4e675b3be42aa0b615d0-Paper-Conference.pdf"},{"title":"Multi-Agent Communication with Information Preserving ...","url":"https://www.ijcai.org/proceedings/2025/0008.pdf"},{"title":"Learning Multi-Agent Communication with Contrastive Learning | OpenReview","url":"https://openreview.net/forum?id=vZZ4hhniJU"},{"title":"[2307.01403] Learning Multi-Agent Communication with Contrastive Learning","url":"https://arxiv.org/abs/2307.01403"},{"title":"Learning Multi-Agent Communication with Contrastive Learning","url":"https://arxiv.org/html/2307.01403"},{"title":"Language Grounded Multi-agent Communication for Ad-hoc Teamwork","url":"https://arxiv.org/html/2409.17348v1"},{"title":"Intent-Grounded Compositional Communication through ...","url":"https://dcslgatech.github.io/iros22-multi-agent-workshop/contributed_papers/IROS22-DMMAS_paper_5730.pdf"},{"title":"Learning multi-agent communication via graph contrastive learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538"}]

Based on the search results, here's what I found on contrastive learning in multi-agent communication with grounding and mutual information:

## Key Research Work

A notable approach proposes grounding decentralized multi-agent communication based on contrastive learning to maximize mutual information between messages within a trajectory by considering messages as incomplete views of environment states.

## Core Methodology

The research introduces an alternative perspective where communicative messages sent between agents are considered as different incomplete views of the environment state, and proposes learning to communicate using contrastive learning to maximize mutual information between messages of a given trajectory.

The approach involves maximizing mutual information using contrastive learning which aligns the message space by pushing messages from similar states closer together and messages of different states further apart.

## Recent Developments (2025)

A 2025 paper proposes a multi-agent communication protocol via graph contrastive learning (MAGE), which utilizes contrast objectives to learn optimal message representations, considering feature and topological levels.

## Performance

In communication-essential environments, these methods outperform previous work in both performance and learning speed. Qualitative metrics and representation probing show that the method induces more symmetric communication and captures global state information from the environment.

The search results show active research in this area, with both foundational work from 2023-2024 and more recent developments in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4611384-61aa-4c68-b48f-073d21ad39f8",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "14cbd99b-7910-4d9e-8e08-37cdf11026c5",
  "sourceToolAssistantUUID": "b4611384-61aa-4c68-b48f-073d21ad39f8",
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

_source line 27 · 2026-05-10T22:12:06.787Z_

<details><summary>↩ Tool result · `toolu_01ToMNCyXCLygqoScrf5Ff7K`</summary>

```text
Web search results for query: "M-GRPO multi-agent deep research training arxiv 2025 2026"

Links: [{"title":"[2511.13288] Multi-Agent Deep Research: Training Multi-Agent Systems with M-GRPO","url":"https://arxiv.org/abs/2511.13288"},{"title":"[2511.13288v2] Multi-Agent Deep Research: Training Multi-Agent Systems with M-GRPO","url":"https://arxiv.org/abs/2511.13288v2"},{"title":"Multi-Agent Deep Research: Training Multi-Agent Systems with M-GRPO","url":"https://arxiv.org/pdf/2511.13288v2"},{"title":"[Quick Review] Multi-Agent Deep Research: Training Multi-Agent Systems with M-GRPO","url":"https://liner.com/review/multiagent-deep-research-training-multiagent-systems-with-mgrpo"},{"title":"LLM Collaboration With Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2508.04652v1"},{"title":"Paper page - Multi-Agent Deep Research: Training Multi-Agent Systems with M-GRPO","url":"https://huggingface.co/papers/2511.13288"},{"title":"Multi-Agent Deep Research: Training Multi-Agent Systems with M-GRPO | alphaXiv","url":"https://www.alphaxiv.org/overview/2511.13288"},{"title":"How to Train Your Deep Research Agent? Prompt, Reward, and Policy Optimization in Search-R1","url":"https://arxiv.org/html/2602.19526"},{"title":"Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration","url":"https://arxiv.org/html/2604.02869v1"},{"title":"[2510.04935] MARS: Co-evolving Dual-System Deep Research via Multi-Agent Reinforcement Learning","url":"https://arxiv.org/abs/2510.04935"}]

Based on the web search results, here's what I found about M-GRPO multi-agent deep research training:

## Overview

M-GRPO is a hierarchical extension of Group Relative Policy Optimization designed for vertical Multi-agent systems. The paper was published on arXiv in November 2025 (arXiv:2511.13288) by Haoyang Hong and 16 other authors.

## Key Features

M-GRPO computes group-relative advantages for both main and sub-agents, maintaining hierarchical credit assignment, and introduces a trajectory-alignment scheme that generates fixed-size batches despite variable sub-agent invocations.

## Problem Being Addressed

Multi-agent systems perform well on general reasoning tasks, but the lack of training in specialized areas hinders their accuracy. Current training methods train a unified large language model (LLM) for all agents in the system, which may limit performance due to different distributions underlying for different agents.

Agents operate at different frequencies, rollouts involve varying sub-agent invocations, and agents are often deployed across separate servers, disrupting end-to-end gradient flow.

## Technical Approach

A decoupled training pipeline is deployed in which agents run on separate servers and exchange minimal statistics via a shared store, enabling scalable training without cross-server backpropagation.

## Performance

In experiments on real-world benchmarks (e.g., GAIA, XBench-DeepSearch, and WebWalkerQA), M-GRPO consistently outperforms both single-agent GRPO and multi-agent GRPO with frozen sub-agents, demonstrating improved stability and sample efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ddf535f-58da-4e78-9e78-e359509d7c4f",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "00016806-c10a-4e35-9810-424867f399e5",
  "sourceToolAssistantUUID": "3ddf535f-58da-4e78-9e78-e359509d7c4f",
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

_source line 28 · 2026-05-10T22:12:09.803Z_

Let me do a few more targeted searches to find additional relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00016806-c10a-4e35-9810-424867f399e5",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauez2JzgpbpL8UxTEn75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eda59b5c-6e33-44f2-8769-13113e0b954d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWLTTmh9a72xA1tuK7gesy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3976,
      "cache_read_input_tokens": 16266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3976,
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

_source line 29 · 2026-05-10T22:12:10.949Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PMcGuFVJXvHSsP7jTMvm9Y`</summary>

```json
{
  "query": "MARTI framework multi-agent reinforcement training LLM Tsinghua 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eda59b5c-6e33-44f2-8769-13113e0b954d",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauez2JzgpbpL8UxTEn75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a980cb2-391b-4587-80f7-f9311c18d7e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWLTTmh9a72xA1tuK7gesy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3976,
      "cache_read_input_tokens": 16266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3976,
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

_source line 30 · 2026-05-10T22:12:11.294Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Syj63eaFEBggxpQ8VdqE2G`</summary>

```json
{
  "query": "\"vision wormhole\" latent communication heterogeneous multi-agent arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a980cb2-391b-4587-80f7-f9311c18d7e0",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauez2JzgpbpL8UxTEn75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9dd9bfac-61b6-4809-ad23-205c4b8618ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWLTTmh9a72xA1tuK7gesy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3976,
      "cache_read_input_tokens": 16266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3976,
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

_source line 31 · 2026-05-10T22:12:11.824Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WTnxa1XLrvREEZGLWj5cpp`</summary>

```json
{
  "query": "MAGRPO multi-agent group relative policy optimization LLM collaboration 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dd9bfac-61b6-4809-ad23-205c4b8618ee",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauez2JzgpbpL8UxTEn75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "497ebaf3-f742-41bf-ab37-a15b9532d8d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWLTTmh9a72xA1tuK7gesy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3976,
      "cache_read_input_tokens": 16266,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3976,
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

_source line 32 · 2026-05-10T22:12:12.621Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QKgyW8jzFNycjCJiANkipa`</summary>

```json
{
  "query": "\"adapting LLM agents through communication\" openreview 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "497ebaf3-f742-41bf-ab37-a15b9532d8d9",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauez2JzgpbpL8UxTEn75",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c8d08ef7-faa8-4cae-9748-4fe731cf37ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWLTTmh9a72xA1tuK7gesy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3976,
      "cache_read_input_tokens": 16266,
      "output_tokens": 248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3976
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 248,
          "cache_read_input_tokens": 16266,
          "cache_creation_input_tokens": 3976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3976,
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

_source line 33 · 2026-05-10T22:12:17.739Z_

<details><summary>↩ Tool result · `toolu_01PMcGuFVJXvHSsP7jTMvm9Y`</summary>

```text
Web search results for query: "MARTI framework multi-agent reinforcement training LLM Tsinghua 2025 2026"

Links: [{"title":"GitHub - TsinghuaC3I/MARTI: A Framework for LLM-based Multi-Agent Reinforced Training and Inference · GitHub","url":"https://github.com/TsinghuaC3I/MARTI"},{"title":"MARTI: A Framework for Multi-Agent LLM Systems Reinforced Training and Inference | OpenReview","url":"https://openreview.net/forum?id=E7jZqo0A50"},{"title":"MARTI: A FRAMEWORK FOR MULTI-AGENT LLM ...","url":"https://openreview.net/pdf?id=E7jZqo0A50"},{"title":"MARTI: A FRAMEWORK FOR MULTI-AGENT LLM SYSTEMS ...","url":"https://openreview.net/pdf/be61bdf63f6dcb786a5f70bfbc5c9f8cc8bc209d.pdf"},{"title":"ICLR Poster MARTI: A Framework for Multi-Agent LLM Systems Reinforced Training and Inference","url":"https://iclr.cc/virtual/2026/poster/10010710"},{"title":"Kaiyan Zhang on X: \"🧠 Again! Introducing: MARTI — Multi-Agent Reinforced Training and Inference A unified framework for LLM-based Multi-Agent Systems with centralized interaction &amp; distributed policy training. Supports structured workflows (debate, MoA, chain), custom rewards, and 3rd-party MAS https://t.co/XGyTf02o68\" / X","url":"https://x.com/OkhayIea/status/1927739357383086438"},{"title":"Introducing MARTI —— A Framework based on OpenRLHF for Multi-Agents Reinforced Training and Inference · Issue #1042 · OpenRLHF/OpenRLHF","url":"https://github.com/OpenRLHF/OpenRLHF/issues/1042"},{"title":"A Practitioner's Guide to Multi-turn Agentic Reinforcement ...","url":"https://www.facebook.com/groups/DeepNetGroup/posts/2613713835688149/"},{"title":"LLM Collaboration with Multi-Agent Reinforcement Learning","url":"https://arxiv.org/pdf/2508.04652"},{"title":"MARFT: Multi-Agent Reinforcement Fine-Tuning","url":"https://arxiv.org/html/2504.16129v2"}]

Based on the search results, here's what I found about the MARTI framework:

## Overview

MARTI (Multi-Agent Reinforced Training and Inference) is an open-source framework designed to facilitate scalable and efficient learning of multi-agent LLM systems.

## Key Features

MARTI supports centralized multi-agent interactions and distributed policy training, with the added capability of multi-turn asynchronous rollouts to enhance training efficiency. The framework includes dynamic workflows for multi-agent interactions, which integrate both rule-based verifiable rewards and LLM-based generative rewards.

## Development and Adoption

The MARTI codebase was released on May 27, 2025. MARTI was accepted by ICLR 2026. Additionally, ReviewRL (EMNLP 2025) and CoMAS are being built on MARTI.

## Advanced Capabilities

MARTI-v2 extends the framework with tree search-augmented reinforcement learning for complex reasoning tasks like code generation, integrating multi-agent tree search with advanced RL techniques to enable efficient multi-step exploration.

## Research Institution

The framework is developed by Tsinghua University's C3I (as indicated by the GitHub repository TsinghuaC3I/MARTI).

## Validation Results

The effectiveness of MARTI has been validated through comprehensive experiments on diverse mathematical tasks, demonstrating that multi-agent LLM-based systems outperform single-agent systems within the same inference budget after convergence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a980cb2-391b-4587-80f7-f9311c18d7e0",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "fa3f7cd8-1c80-43b0-bf3a-4fc0a449f346",
  "sourceToolAssistantUUID": "1a980cb2-391b-4587-80f7-f9311c18d7e0",
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

_source line 34 · 2026-05-10T22:12:18.074Z_

<details><summary>↩ Tool result · `toolu_01WTnxa1XLrvREEZGLWj5cpp`</summary>

```text
Web search results for query: "MAGRPO multi-agent group relative policy optimization LLM collaboration 2025"

Links: [{"title":"LLM Collaboration with Multi-Agent Reinforcement Learning","url":"https://arxiv.org/pdf/2508.04652"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Multi-Turn+Group+Relative+Policy+Optimization"},{"title":"LLM Collaboration With Multi-Agent Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2508.04652v1"},{"title":"M-GRPO: Multi-Agent Group Relative Policy Optimization","url":"https://www.emergentmind.com/topics/multi-agent-group-relative-policy-optimization-m-grpo"},{"title":"MAGRPO Explained: 3x Faster LLM Collaboration","url":"https://www.bohrium.com/en/blog/research-notes/aaai-2026-llm-collaboration-multi-agent-reinforcement-learning/"},{"title":"NeurIPS Improved Multi-Agent Collaboration with Multi-Turn Reinforcement Learning","url":"https://neurips.cc/virtual/2025/128017"},{"title":"Improved Multi-Agent Collaboration with Multi-Turn Reinforcement Learning","url":"https://openreview.net/pdf?id=WYfzRJgWbO"},{"title":"[2508.04652] LLM Collaboration With Multi-Agent Reinforcement Learning","url":"https://arxiv.org/abs/2508.04652"},{"title":"LLM Collaboration with Multi-Agent Reinforcement Learning | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40487"},{"title":"Improved Multi-Agent Collaboration with Multi-Turn Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=WYfzRJgWbO"}]

Based on the search results, here's what I found about MAGRPO:

## Overview

MAGRPO (Multi-Agent Group Relative Policy Optimization) is a multi-agent, multi-turn algorithm developed to solve LLM collaboration problems, building on current RL approaches for LLMs as well as MARL techniques.

## Key Characteristics

MAGRPO leverages centralized group-relative advantages for joint optimization, while preserving decentralized execution for each agent. Rather than relying on brittle text prompts to coordinate Large Language Models, MAGRPO treats collaboration as a mathematical problem—specifically, a cooperative Multi-Agent Reinforcement Learning task that trains agents to generate responses maximizing a shared group reward rather than just their individual success.

## Problem It Addresses

By formalizing LLM dialogue as a Decentralized Partially Observable Markov Decision Process (Dec-POMDP), MAGRPO moves beyond fragile prompt engineering or isolated fine-tuning, creating a framework where agents optimize for a shared team objective while acting on their own local observations.

## Applications and Results

Experiments on LLM writing and coding collaboration demonstrate that fine-tuning multiple LLMs with MAGRPO enables agents to generate high-quality responses efficiently through effective cooperation. The authors have released CoMLRL, an open-source library for training multiple LLMs using MARL, which includes the environments and benchmarks used in the paper.

The research has been presented at major AI venues including NeurIPS 2025 and AAAI 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "497ebaf3-f742-41bf-ab37-a15b9532d8d9",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "c96e4b76-d3ae-4b4a-ba85-842fd43e2226",
  "sourceToolAssistantUUID": "497ebaf3-f742-41bf-ab37-a15b9532d8d9",
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

_source line 35 · 2026-05-10T22:12:18.643Z_

<details><summary>↩ Tool result · `toolu_01Syj63eaFEBggxpQ8VdqE2G`</summary>

```text
Web search results for query: ""vision wormhole" latent communication heterogeneous multi-agent arxiv 2026"

Links: [{"title":"The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems","url":"https://arxiv.org/html/2602.15382v1"},{"title":"GitHub - xz-liu/heterogeneous-latent-mas: The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems · GitHub","url":"https://github.com/xz-liu/heterogeneous-latent-mas"},{"title":"Preprint. Work in progress. The Vision Wormhole: Latent-Space Communication in","url":"https://arxiv.org/pdf/2602.15382"},{"title":"[2602.15382] The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems","url":"https://arxiv.org/abs/2602.15382"},{"title":"Preprint. Work in progress. The Vision Wormhole: Latent-Space Communication in","url":"https://openreview.net/pdf?id=xTh4AwVKdw"},{"title":"GitHub - kyegomez/awesome-multi-agent-papers: A compilation of the best multi-agent papers · GitHub","url":"https://github.com/kyegomez/awesome-multi-agent-papers"},{"title":"[2511.09149] Enabling Agents to Communicate Entirely in Latent Space","url":"https://arxiv.org/abs/2511.09149"},{"title":"Latent Collaboration in Multi-Agent Systems","url":"https://arxiv.org/html/2511.20639v1"},{"title":"GitHub - Gen-Verse/LatentMAS: [ICML 2026 Spotlight] Latent Collaboration in Multi-Agent Systems · GitHub","url":"https://github.com/Gen-Verse/LatentMAS"},{"title":"Enabling Agents to Communicate Entirely in Latent Space","url":"https://arxiv.org/html/2511.09149v4"}]

I found the research paper you're looking for. Here are the key findings:

## The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems

The Vision Wormhole is a novel framework that repurposes the visual interface of Vision-Language Models (VLMs) to enable model-agnostic, text-free communication.

**Core Innovation:**
By introducing a Universal Visual Codec, the framework maps heterogeneous reasoning traces into a shared continuous latent space and injects them directly into the receiver's visual pathway, effectively treating the vision encoder as a universal port for inter-agent telepathy.

**Problem it Solves:**
Multi-Agent Systems powered by Large Language Models have unlocked advanced collaborative reasoning, yet they remain shackled by the inefficiency of discrete text communication. While latent state transfer offers a high-bandwidth alternative, existing approaches either assume homogeneous sender-receiver architectures or rely on pair-specific learned translators, limiting scalability and modularity across diverse model families with disjoint manifolds.

**Training Approach:**
The framework develops a self-supervised distillation training objective that requires no human annotation, treating the slow-but-accurate text-based communication as the "Teacher" and forcing the high-speed vision wormhole (the "Student") to mimic the teacher's internal representations and output distributions.

**Results:**
Results demonstrate that the method reduces overall MAS wall-clock time compared to text-based baselines while maintaining reasoning performance comparable to the original text-based MAS, validating the efficacy of the Vision Wormhole as a practical acceleration layer.

The paper was published in February 2026 on arXiv (2602.15382).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9dd9bfac-61b6-4809-ad23-205c4b8618ee",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "e02186c7-ee0f-4f9a-ae4a-55d4deb6686e",
  "sourceToolAssistantUUID": "9dd9bfac-61b6-4809-ad23-205c4b8618ee",
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

_source line 36 · 2026-05-10T22:12:22.538Z_

<details><summary>↩ Tool result · `toolu_01QKgyW8jzFNycjCJiANkipa`</summary>

```text
Web search results for query: ""adapting LLM agents through communication" openreview 2025 2026"

Links: [{"title":"Adapting LLM Agents Through Communication | OpenReview","url":"https://openreview.net/forum?id=wOelVq8fwL&noteId=yCjsgUZtGy"},{"title":"Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems | OpenReview","url":"https://openreview.net/forum?id=LkzuPorQ5L"},{"title":"Which LLM Multi-Agent Protocol to Choose? | OpenReview","url":"https://openreview.net/forum?id=lqNqKUG2dn"},{"title":"Multi-Agent Collaboration via Evolving Orchestration | OpenReview","url":"https://openreview.net/forum?id=L0xZPXT3le"},{"title":"Adapting LLM Agents with Universal Feedback in Communication | OpenReview","url":"https://openreview.net/forum?id=LqlzI69nJA"},{"title":"Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration | OpenReview","url":"https://openreview.net/forum?id=34cANdsHKV"},{"title":"Toward Self-Evolving Systems of LLM Agents through Exploration and Iterative Feedback | OpenReview","url":"https://openreview.net/forum?id=uO3gGxzu8k"},{"title":"Chain of Agents: Large Language Models Collaborating on Long-Context Tasks | OpenReview","url":"https://openreview.net/forum?id=LuCLf4BJsr"},{"title":"Enhancing Language Model Agents using Diversity of Thoughts | OpenReview","url":"https://openreview.net/forum?id=ZsP3YbYeE9"},{"title":"Learning Efficient and Interpretable Multi-Agent Communication | OpenReview","url":"https://openreview.net/forum?id=a3CUE06G5Y"}]

I found several research papers on OpenReview related to adapting LLM agents through communication. Here are the most relevant results:

## Primary Match

The paper "Adapting LLM Agents Through Communication" proposes the Learning through Communication (LTC) paradigm, a novel training approach enabling LLM agents to improve continuously through interactions with their environments and other agents.

## Related Recent Research (2025-2026)

Several other papers on OpenReview explore LLM agent communication and adaptation:

1. **Adapting LLM Agents with Universal Feedback in Communication** - This work introduces Learning through Communication (LTC) to facilitate agent training with both linguistic feedback and non-linguistic reward signals, using a universal buffer to store feedback and an iterative pipeline to enable agents to explore and update their policy, with diverse communication patterns tailored for single-agent and multi-agent environments.

2. **Which LLM Multi-Agent Protocol to Choose?** - This paper addresses how the communication protocol layer has become a critical component affecting system performance and reliability, introducing ProtocolBench, a benchmark designed to evaluate agent communication protocols across task utility, communication overhead, system performance, and resilience under failure.

3. **Multi-Agent Collaboration via Evolving Orchestration** - This work proposes a puppeteer-style paradigm for LLM-based multi-agent collaboration, where a centralized orchestrator dynamically directs agents in response to evolving task states, trained via reinforcement learning to adaptively sequence and prioritize agents.

4. **Graph-of-Agents** - This paper proposes Graph-of-Agents (GoA), a new graph-based framework for modeling multi-agent LLM communication.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8d08ef7-faa8-4cae-9748-4fe731cf37ff",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "e6dfd3f0-1602-47bf-976b-157ee39ededa",
  "sourceToolAssistantUUID": "c8d08ef7-faa8-4cae-9748-4fe731cf37ff",
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

_source line 37 · 2026-05-10T22:12:25.288Z_

Let me do a few more targeted searches to find any remaining relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6dfd3f0-1602-47bf-976b-157ee39ededa",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauf1BjoZtyHqjGtNHdzX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99636718-69e7-4eba-a353-86eef0d28ae9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKHKvigeCErNrCJrtyzG8m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4025,
      "cache_read_input_tokens": 20242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4025,
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

_source line 38 · 2026-05-10T22:12:26.550Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BpUMrb3fr1MQg7yQeCXt87`</summary>

```json
{
  "query": "\"latent collaboration\" multi-agent ICML 2026 spotlight LatentMAS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99636718-69e7-4eba-a353-86eef0d28ae9",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauf1BjoZtyHqjGtNHdzX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0510e2fb-d498-4acd-bbb2-f2f62ec2f16c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKHKvigeCErNrCJrtyzG8m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4025,
      "cache_read_input_tokens": 20242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4025,
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

_source line 39 · 2026-05-10T22:12:26.709Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PUAEbbgwQh1dpdK4Mfm2QF`</summary>

```json
{
  "query": "MARFT multi-agent reinforcement fine-tuning arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0510e2fb-d498-4acd-bbb2-f2f62ec2f16c",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauf1BjoZtyHqjGtNHdzX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4659c4f0-b1f1-4966-b007-9828aa3b4c11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKHKvigeCErNrCJrtyzG8m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4025,
      "cache_read_input_tokens": 20242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4025,
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

_source line 40 · 2026-05-10T22:12:27.979Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rvdu4sZvCX62EWGLxw7XSt`</summary>

```json
{
  "query": "\"active learning communication structure\" multi-agent LLM 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4659c4f0-b1f1-4966-b007-9828aa3b4c11",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauf1BjoZtyHqjGtNHdzX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5cc811b4-3012-4026-b2c6-908cf011d7c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKHKvigeCErNrCJrtyzG8m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4025,
      "cache_read_input_tokens": 20242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4025,
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

_source line 41 · 2026-05-10T22:12:28.059Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016sgtZBn56JCYHt9GQdRfvU`</summary>

```json
{
  "query": "MAGE graph contrastive learning multi-agent communication 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cc811b4-3012-4026-b2c6-908cf011d7c2",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauf1BjoZtyHqjGtNHdzX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e5f1afc-102a-4822-b6d8-d6412d7d97e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKHKvigeCErNrCJrtyzG8m",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4025,
      "cache_read_input_tokens": 20242,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4025
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 240,
          "cache_read_input_tokens": 20242,
          "cache_creation_input_tokens": 4025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4025,
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

_source line 42 · 2026-05-10T22:12:33.141Z_

<details><summary>↩ Tool result · `toolu_01Rvdu4sZvCX62EWGLxw7XSt`</summary>

```text
Web search results for query: ""active learning communication structure" multi-agent LLM 2026 arxiv"

Links: [{"title":"Multiagent Systems","url":"https://arxiv.org/list/cs.MA/recent"},{"title":"Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces","url":"https://arxiv.org/html/2605.02801"},{"title":"Multi-Agent Collaboration Mechanisms: A Survey of LLMs","url":"https://arxiv.org/html/2501.06322v1"},{"title":"Agent Q-Mix: Selecting the Right Action for LLM Multi-Agent Systems through Reinforcement Learning","url":"https://arxiv.org/html/2604.00344"},{"title":"[2605.02801] Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces","url":"https://arxiv.org/abs/2605.02801"},{"title":"LLM-based Multi-Agent Reinforcement Learning: Current and Future Directions","url":"https://arxiv.org/pdf/2405.11106"},{"title":"[2502.14321] Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems","url":"https://arxiv.org/abs/2502.14321"},{"title":"Multiagent Systems Apr 2026","url":"https://arxiv.org/list/cs.MA/current"},{"title":"LLM Collaboration With Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2508.04652v1"},{"title":"July 2026 1 LLM-enabled Social Agents","url":"https://arxiv.org/pdf/2605.02335"}]

Based on the search results, I found a highly relevant paper that directly matches your query:

**"Active Learning for Communication Structure Optimization in LLM-Based Multi-Agent Systems"** by Huchen Yang, Xinghao Dong, Dan Negrut, and Jin-Long Wu (arXiv:2605.05703)

This paper appears in the recent arXiv listings for Multiagent Systems and directly addresses the intersection of active learning, communication structure, and multi-agent LLM systems that you're searching for.

The search results also reveal a broader research landscape in this area. For context, communication topology—the graph specifying which agents exchange information—is a key determinant of overall system behavior in LLM-based multi-agent systems, affecting task performance, token efficiency, and robustness.

If you'd like more specific information about the content of the Active Learning paper or other related works in this research area, I can search for additional details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cc811b4-3012-4026-b2c6-908cf011d7c2",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "ea60078d-285e-4ac0-89f9-eb70e9cdcde6",
  "sourceToolAssistantUUID": "5cc811b4-3012-4026-b2c6-908cf011d7c2",
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

_source line 43 · 2026-05-10T22:12:33.591Z_

<details><summary>↩ Tool result · `toolu_01PUAEbbgwQh1dpdK4Mfm2QF`</summary>

```text
Web search results for query: "MARFT multi-agent reinforcement fine-tuning arxiv 2025"

Links: [{"title":"[2504.16129] MARFT: Multi-Agent Reinforcement Fine-Tuning","url":"https://arxiv.org/abs/2504.16129"},{"title":"MARFT: Multi-Agent Reinforcement Fine-Tuning","url":"https://arxiv.org/html/2504.16129v4"},{"title":"MARFT: Multi-Agent Reinforcement Fine-Tuning - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2504.16129"},{"title":"[2504.16129v2] MARFT: Multi-Agent Reinforcement Fine-Tuning","url":"http://arxiv.org/abs/2504.16129v2"},{"title":"[PDF] MARFT: Multi-Agent Reinforcement Fine-Tuning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MARFT:-Multi-Agent-Reinforcement-Fine-Tuning-Liao-Wen/a9a6f3178221ee4bacbdddd7b8fc0d6861e39b25"},{"title":"MARFT: Multi-Agent Reinforcement Fine-Tuning - Paper Detail","url":"https://deeplearn.org/arxiv/598961/marft:-multi-agent-reinforcement-fine-tuning"},{"title":"MARFT: Multi-Agent Reinforcement Fine-Tuning | OpenReview","url":"https://openreview.net/forum?id=Yu1ZsRlqeK"},{"title":"ToMPO: Training LLM Strategic Decision Making from a Multi-Agent Perspective","url":"https://arxiv.org/html/2509.21134v1"},{"title":"MARFT: Multi-Agent Reinforcement Fine-Tuning","url":"https://alphaxiv.org/overview/2504.16129v1"},{"title":"SWIRL: A Staged Workflow for Interleaved Reinforcement Learning in Mobile GUI Control","url":"https://arxiv.org/html/2508.20018v1"}]

Based on the search results, here's what I found about MARFT:

## MARFT: Multi-Agent Reinforcement Fine-Tuning

MARFT is a novel paradigm proposed to address challenges in LLM-based MARL, presented as a comprehensive study of LLM-based MARL.

### Paper Details

The paper was authored by Junwei Liao, Muning Wen, Jun Wang, and Weinan Zhang, and was submitted on April 21, 2025. The latest version (v4) was updated on November 3, 2025.

### Key Motivation

LLM-based Multi-Agent Systems have demonstrated remarkable capabilities in addressing complex, agentic tasks, from generating high-quality presentation slides to conducting sophisticated scientific research. However, limited research has investigated the fine-tuning of LaMAS (LLM-based Multi-Agent Systems) using foundational RL techniques.

### Main Contributions

The paper introduces a brand-new mechanism called Flex-MG, which aligns with the LaMAS optimization in real-world applications, and a universal algorithmic framework tailored specifically for LaMAS.

### Framework Availability

The implementation of the proposed framework is publicly available at: https://github.com/jwliao-ai/MARFT.

The paper addresses fundamental challenges that arise from applying traditional Multi-Agent Reinforcement Learning directly to LLM-based systems, proposing MARFT as a specialized paradigm designed for this unique setting.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4659c4f0-b1f1-4966-b007-9828aa3b4c11",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "b379adde-6d04-45e5-b20b-02214bed3528",
  "sourceToolAssistantUUID": "4659c4f0-b1f1-4966-b007-9828aa3b4c11",
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

_source line 44 · 2026-05-10T22:12:33.743Z_

<details><summary>↩ Tool result · `toolu_01BpUMrb3fr1MQg7yQeCXt87`</summary>

```text
Web search results for query: ""latent collaboration" multi-agent ICML 2026 spotlight LatentMAS"

Links: [{"title":"GitHub - Gen-Verse/LatentMAS: [ICML 2026 Spotlight] Latent Collaboration in Multi-Agent Systems · GitHub","url":"https://github.com/Gen-Verse/LatentMAS"},{"title":"[2511.20639] Latent Collaboration in Multi-Agent Systems","url":"https://arxiv.org/abs/2511.20639"},{"title":"Latent Collaboration in Multi-Agent Systems","url":"https://arxiv.org/html/2511.20639v1"},{"title":"Paper page - Latent Collaboration in Multi-Agent Systems","url":"https://huggingface.co/papers/2511.20639"},{"title":"Enabling Agents to Communicate Entirely in Latent Space | OpenReview","url":"https://openreview.net/forum?id=rmYbgsehTd"},{"title":"The Invisible AI Threat: Latent Collaboration's Efficiency Breakthrough and Dangerous Security Risks","url":"https://kenhuangus.substack.com/p/latentmas-ai-agents-collaborate-at"},{"title":"Latent Collaboration in Multi-Agent Systems","url":"https://www.emergentmind.com/papers/2511.20639"},{"title":"(PDF) Latent Collaboration in Multi-Agent Systems","url":"https://www.researchgate.net/publication/397983060_Latent_Collaboration_in_Multi-Agent_Systems"},{"title":"[2604.13349] When Less Latent Leads to Better Relay: Information-Preserving Compression for Latent Multi-Agent LLM Collaboration","url":"https://arxiv.org/abs/2604.13349"},{"title":"Agent Primitives: Reusable Latent Building Blocks for Multi-Agent Systems","url":"https://arxiv.org/html/2602.03695"}]

Based on the search results, here's what I found about LatentMAS:

## Overview

LatentMAS has been accepted into ICML 2026 as a spotlight. LatentMAS is a multi-agent reasoning framework that moves agent collaboration from token space into the model's latent space, with agents communicating by passing latent thoughts through their own working memory instead of producing long textual reasoning traces.

## How It Works

Each agent performs auto-regressive latent thoughts generation through last-layer hidden embeddings, and a shared latent working memory preserves and transfers each agent's internal representations, ensuring lossless information exchange.

## Key Features

LatentMAS has efficient multi-step reasoning with drastically fewer tokens, training-free latent-space alignment for stable generation, and is a general technique compatible with any HF model and optionally vLLM backends.

## Performance Results

Across both sequential and hierarchical MAS settings and three backbone scales (4B, 8B, and 14B), LatentMAS consistently outperforms strong single-model and text-based MAS baselines by improving accuracy by up to 14.6%, reducing output token usage by 70.8%-83.7%, and delivering 4x faster end-to-end inference.

Comprehensive evaluations are conducted on nine benchmarks spanning math and science reasoning, commonsense understanding, and code generation.

## Availability

Code and data are fully open-sourced at https://github.com/Gen-Verse/LatentMAS.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0510e2fb-d498-4acd-bbb2-f2f62ec2f16c",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "80ddcf2d-bad2-46a1-a7f9-b9be71843d45",
  "sourceToolAssistantUUID": "0510e2fb-d498-4acd-bbb2-f2f62ec2f16c",
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

_source line 45 · 2026-05-10T22:12:35.251Z_

<details><summary>↩ Tool result · `toolu_016sgtZBn56JCYHt9GQdRfvU`</summary>

```text
Web search results for query: "MAGE graph contrastive learning multi-agent communication 2025"

Links: [{"title":"Learning multi-agent communication via graph contrastive learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538"},{"title":"Multi-Agent Communication with Information Preserving ...","url":"https://www.ijcai.org/proceedings/2025/0008.pdf"},{"title":"Learning To Ground Decentralized Multi-Agent Communication with Contrastive Learning | OpenReview","url":"https://openreview.net/forum?id=rLceWXWCmZc"},{"title":"A unified multimodal GenAI platform integrating GraphRAG multi-agent systems and custom language models for intelligent document processing and knowledge synthesis | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-47145-x"},{"title":"Learning Multi-Agent Communication from Graph Modeling Perspective | OpenReview","url":"https://openreview.net/forum?id=Qox9rO0kN0"},{"title":"(PDF) Learning to Ground Decentralized Multi-Agent Communication with Contrastive Learning","url":"https://www.researchgate.net/publication/359079677_Learning_to_Ground_Decentralized_Multi-Agent_Communication_with_Contrastive_Learning"},{"title":"[2307.01403] Learning Multi-Agent Communication with Contrastive Learning","url":"https://arxiv.org/abs/2307.01403"},{"title":"Learning Communication Skills in Multi-task Multi-agent Deep Reinforcement Learning","url":"https://arxiv.org/html/2511.03348v2"},{"title":"Graph-Based Multimodal Contrastive Learning for Chart ...","url":"https://arxiv.org/pdf/2501.04303"},{"title":"graph-based-deep-learning-literature/conference-publications/README.md at master · naganandy/graph-based-deep-learning-literature","url":"https://github.com/naganandy/graph-based-deep-learning-literature/blob/master/conference-publications/README.md"}]

Based on the search results, I found relevant information about MAGE and multi-agent communication with graph contrastive learning in 2025:

## MAGE: Multi-Agent Communication via Graph Contrastive Learning

MAGE is a multi-agent communication protocol via graph contrastive learning that utilizes contrast objectives to learn optimal message representations, considering feature and topological level.

**Background and Motivation:**

Communication learning has emerged as a successful tool for tackling complex tasks in multi-agent reinforcement learning (MARL), with many MARL methods using graph neural networks (GNNs) to build a communication learning framework where agents and communication channels are represented as nodes and edges in a graph. However, most GNN-based MARL methods simply aggregate features of neighboring agents to obtain message representations, which may not extract enough useful information.

**Key Technical Approach:**

In MAGE, two correlated graph views are generated by applying stochastic corruption to the constructed graph, and MAGE is trained using a contrastive loss function to enhance the consistency of agent features across these two views. The scheme improves data augmentation by modifying both the topology structure and agent features to boost the optimization of the contrastive objective, specifically through edge removal and feature masking.

**Advantages:**

MAGE learns high-quality feature representations that extract important information at the topological and feature levels through graph contrastive learning, thus facilitating action selection and coordination. This work is the first to extend graph contrastive learning to MARL, which enables efficient multi-agent communication learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e5f1afc-102a-4822-b6d8-d6412d7d97e6",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "b91094b4-53dd-439c-864f-f9611c014495",
  "sourceToolAssistantUUID": "9e5f1afc-102a-4822-b6d8-d6412d7d97e6",
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

_source line 46 · 2026-05-10T22:12:38.528Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ykNZbEHsB4bPpDhjaJRot`</summary>

```json
{
  "query": "\"beyond self-talk\" communication-centric survey LLM multi-agent 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b91094b4-53dd-439c-864f-f9611c014495",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauf282b6Y5J1oghxS536",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e2e0a07-3003-430f-85e9-c89a7a8afcb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015U83rD1LYFwoP2H7WYnazK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3717,
      "cache_read_input_tokens": 24267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3717,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-10T22:12:38.962Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014KkRPtSphgFHJgQhukJ8pW`</summary>

```json
{
  "query": "\"cut the crap\" economical communication multi-agent LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e2e0a07-3003-430f-85e9-c89a7a8afcb6",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauf282b6Y5J1oghxS536",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e94da99f-e2e2-4edf-8fc2-3465e97344b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015U83rD1LYFwoP2H7WYnazK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3717,
      "cache_read_input_tokens": 24267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3717,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-10T22:12:39.954Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Td69SePZTpHtquvKqd5gzX`</summary>

```json
{
  "query": "MARS co-evolving dual-system deep research multi-agent reinforcement learning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e94da99f-e2e2-4edf-8fc2-3465e97344b9",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauf282b6Y5J1oghxS536",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "37fbcd4f-aa3f-49b4-b598-1f97125fc976",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015U83rD1LYFwoP2H7WYnazK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3717,
      "cache_read_input_tokens": 24267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3717,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-10T22:12:40.488Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xy5hBfd1zooknSDBTRwVnr`</summary>

```json
{
  "query": "CACL communication alignment contrastive learning ICLR 2024 multi-agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37fbcd4f-aa3f-49b4-b598-1f97125fc976",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauf282b6Y5J1oghxS536",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa8f4428-c9f3-4713-909d-cdc874815099",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015U83rD1LYFwoP2H7WYnazK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3717,
      "cache_read_input_tokens": 24267,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3717
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 234,
          "cache_read_input_tokens": 24267,
          "cache_creation_input_tokens": 3717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3717,
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

_source line 50 · 2026-05-10T22:12:43.505Z_

<details><summary>↩ Tool result · `toolu_014KkRPtSphgFHJgQhukJ8pW`</summary>

```text
Web search results for query: ""cut the crap" economical communication multi-agent LLM 2025 2026"

Links: [{"title":"[2410.02506] Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems","url":"https://arxiv.org/abs/2410.02506"},{"title":"Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems | OpenReview","url":"https://openreview.net/forum?id=LkzuPorQ5L"},{"title":"[2410.02506v1] Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems","url":"https://arxiv.org/abs/2410.02506v1"},{"title":"Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems | alphaXiv","url":"https://www.alphaxiv.org/abs/2410.02506"},{"title":"Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems | PromptLayer","url":"https://www.promptlayer.com/research-papers/cut-the-crap-an-economical-communication-pipeline-for-llm-based-multi-agent-systems"},{"title":"(PDF) Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems","url":"https://www.researchgate.net/publication/384630697_Cut_the_Crap_An_Economical_Communication_Pipeline_for_LLM-based_Multi-Agent_Systems"},{"title":"GitHub - yanweiyue/AgentPrune · GitHub","url":"https://github.com/yanweiyue/AgentPrune"},{"title":"[Literature Review] Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems","url":"https://www.themoonlight.io/en/review/cut-the-crap-an-economical-communication-pipeline-for-llm-based-multi-agent-systems"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Cut+the+Crap:+An+Economical+Communication+Pipeline+for+LLM-based+Multi-Agent+Systems."},{"title":"Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/bbc461518c59a2a8d64e70e2c38c4a0e-Abstract-Conference.html"}]

Based on the search results, here's what I found about "Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems":

## Overview

"Cut the Crap" addresses a challenge in LLM-based multi-agent systems where collective intelligence can significantly outperform individual capabilities, but existing multi-agent pipelines inherently introduce substantial token overhead and increased economic costs.

## The AgentPrune Framework

The paper proposes an economical, simple, and robust multi-agent communication framework called AgentPrune, which can seamlessly integrate into mainstream multi-agent systems and prunes redundant or even malicious communication messages.

AgentPrune is the first to identify and formally define the communication redundancy issue present in current LLM-based multi-agent pipelines, and efficiently performs one-shot pruning on the spatial-temporal message-passing graph, yielding a token-economic and high-performing communication topology.

## Key Results

Extensive experiments across six benchmarks demonstrate that AgentPrune achieves comparable results as state-of-the-art topologies at merely $5.6 cost compared to their $43.7, integrates seamlessly into existing multi-agent frameworks with 28.1%-72.8% token reduction, and successfully defends against two types of agent-based adversarial attacks with 3.5%-10.8% performance boost.

## Publication Timeline

The paper was initially submitted in October 2024 and is scheduled to be published in the Thirteenth International Conference on Learning Representations in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e94da99f-e2e2-4edf-8fc2-3465e97344b9",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "ec79ae6d-d697-4aa0-a683-71f6672f5866",
  "sourceToolAssistantUUID": "e94da99f-e2e2-4edf-8fc2-3465e97344b9",
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

_source line 51 · 2026-05-10T22:12:44.227Z_

<details><summary>↩ Tool result · `toolu_015ykNZbEHsB4bPpDhjaJRot`</summary>

```text
Web search results for query: ""beyond self-talk" communication-centric survey LLM multi-agent 2025"

Links: [{"title":"[2502.14321] Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems","url":"https://arxiv.org/abs/2502.14321"},{"title":"Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems","url":"https://arxiv.org/html/2502.14321v1"},{"title":"Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250214321Y/abstract"},{"title":"[PDF] Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Beyond-Self-Talk:-A-Communication-Centric-Survey-of-Yan-Zhang/77137fc47a569d66952cdf656ed6e99f3b027c26"},{"title":"Paper page - Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems","url":"https://huggingface.co/papers/2502.14321"},{"title":"A Communication-Centric Survey of LLM-Based Multi- ...","url":"https://arxiv.org/pdf/2502.14321"},{"title":"Beyond Self-Talk: A Communication-Centric Survey of LLM ...","url":"https://www.alphaxiv.org/overview/2502.14321v1"},{"title":"Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems | OpenReview","url":"https://openreview.net/forum?id=09UsnNdVar"},{"title":"[2502.14321v1] Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems","url":"http://arxiv.org/abs/2502.14321v1"},{"title":"Beyond Self-Talk - A Communication-Centric Survey of LLM-Based Multi-Agent Systems | PDF | Communication | Information","url":"https://www.scribd.com/document/835435758/Beyond-Self-Talk-A-Communication-Centric-Survey-of-LLM-Based-Multi-Agent-Systems"}]

I found the paper! Here are the key results for your search:

## "Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems"

This comprehensive survey addresses large language model-based multi-agent systems from a communication-centric perspective, recognizing that existing surveys typically overlook the central role of communication in coordinating agent behaviors and interactions.

**Key Framework:**
The paper proposes a structured framework that integrates system-level communication (architecture, goals, and protocols) with system internal communication (strategies, paradigms, objects, and content), enabling a detailed exploration of how agents interact, negotiate, and achieve collective intelligence.

**Focus Areas:**
The survey highlights current challenges, including communication efficiency, security vulnerabilities, inadequate benchmarking, and scalability issues, and outlines promising future research directions.

**Publication Details:**
- **Authors:** Bingyu Yan and 8 co-authors
- **Repository:** ArXiv (arXiv:2502.14321)
- **Latest Version:** June 19, 2025
- **Available Formats:** PDF, HTML (experimental)

The paper is available on multiple platforms including arXiv, Semantic Scholar, Hugging Face Papers, and OpenReview.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e2e0a07-3003-430f-85e9-c89a7a8afcb6",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "056a68c0-a642-4023-b046-e56c2917ce54",
  "sourceToolAssistantUUID": "5e2e0a07-3003-430f-85e9-c89a7a8afcb6",
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

_source line 52 · 2026-05-10T22:12:47.164Z_

<details><summary>↩ Tool result · `toolu_01Td69SePZTpHtquvKqd5gzX`</summary>

```text
Web search results for query: "MARS co-evolving dual-system deep research multi-agent reinforcement learning 2025"

Links: [{"title":"[2510.04935] MARS: Co-evolving Dual-System Deep Research via Multi-Agent Reinforcement Learning","url":"https://arxiv.org/abs/2510.04935"},{"title":"MARS: Co-evolving Dual-System Deep Research via Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2510.04935"},{"title":"MARS: Optimizing Dual-System Deep Research via Multi-Agent Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=abxVxyXNhW"},{"title":"MARS: Optimizing Dual-System Deep Research via Multi-Agent Reinforcement Learning","url":"https://arxiv.org/html/2510.04935v1"},{"title":"[2510.04935v1] MARS: Optimizing Dual-System Deep Research via Multi-Agent Reinforcement Learning","url":"https://arxiv.org/abs/2510.04935v1"},{"title":"(PDF) MARS: Optimizing Dual-System Deep Research via Multi-Agent Reinforcement Learning","url":"https://www.researchgate.net/publication/396250113_MARS_Optimizing_Dual-System_Deep_Research_via_Multi-Agent_Reinforcement_Learning"},{"title":"[Literature Review] MARS: Optimizing Dual-System Deep Research via Multi-Agent Reinforcement Learning","url":"https://www.themoonlight.io/en/review/mars-optimizing-dual-system-deep-research-via-multi-agent-reinforcement-learning"},{"title":"MARS: Optimizing Dual-System Deep Research via Multi- ...","url":"https://arxiv.org/pdf/2510.04935"},{"title":"MARS-DA: A Hierarchical Reinforcement Learning Framework for Risk-Aware Multi-Agent Bidding in Power Grids","url":"https://arxiv.org/html/2605.03142"},{"title":"MARS: A Meta-Adaptive Reinforcement Learning Framework for Risk-Aware Multi-Agent Portfolio Management","url":"https://arxiv.org/html/2508.01173"}]

Based on the search results, I found comprehensive information about MARS (Multi-Agent System for Deep ReSearch):

## Overview

MARS is a novel co-evolution framework that jointly optimizes dual cognitive systems through multi-agent reinforcement learning. The framework addresses two fundamental limitations of Large Reasoning Models (LRMs): excessive token consumption when overanalyzing simple information processing tasks, and inability to access up-to-date knowledge beyond their training data.

## Key Architecture

MARS enables System 1 (fast, intuitive processing) and System 2 (deliberate reasoning) to co-adapt through shared trajectory rewards, developing complementary strategies where System 1 learns to distill information specifically useful for System 2's reasoning.

MARS strategically integrates multiple external tools—such as Google Search, Google Scholar, and Python Interpreter—to access up-to-date information and execute complex computations, while creating a specialized division of labor where System 1 efficiently processes and summarizes high-volume external information, providing distilled insights that expand System 2's reasoning context without overwhelming its capacity.

## Technical Approach

The framework extends Group Relative Policy Optimization to simultaneously optimize both systems with multi-turn tool interactions, bin-packing optimization, and sample balancing strategies that enhance collaborative efficiency.

## Performance

Despite using smaller models (7B/8B vs. 32B/72B) and no SFT warmup, MARS achieves superior performance, validating the effectiveness of their multi-agent RL framework rather than relying on model scale or supervised data.

The paper was published in October 2025, with an updated version in February 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37fbcd4f-aa3f-49b4-b598-1f97125fc976",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "44a1eefe-bb64-4800-8a65-0e6f041c7a7c",
  "sourceToolAssistantUUID": "37fbcd4f-aa3f-49b4-b598-1f97125fc976",
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

_source line 53 · 2026-05-10T22:12:47.275Z_

<details><summary>↩ Tool result · `toolu_01Xy5hBfd1zooknSDBTRwVnr`</summary>

```text
Web search results for query: "CACL communication alignment contrastive learning ICLR 2024 multi-agent"

Links: [{"title":"LEARNING MULTI-AGENT COMMUNICATION WITH ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/de2ad3ed44ee4e675b3be42aa0b615d0-Paper-Conference.pdf"},{"title":"Published as a workshop paper at EmeCom at ICLR 2022 LEARNING TO GROUND","url":"https://richielo.github.io/files/MARL_COMM_CACL_ICLR_WS_22.pdf"},{"title":"aligning visual contrastive learning models","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/affda8306b5501c58fca59fe52f05fda-Paper-Conference.pdf"},{"title":"LEARNING MULTI-AGENT COMMUNICATION FROM ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/37c6d0bc4d2917dcbea693b18504bd87-Paper-Conference.pdf"},{"title":"To appear at the ICLR 2024 Workshop on Representational Alignment (Re-Align)","url":"https://kushinm.com/assets/pdf/mukherjee_iclr_2024.pdf"},{"title":"Downloads 2024","url":"https://iclr.cc/Downloads/2024"},{"title":"ICLR 2024 Papers","url":"https://iclr.cc/virtual/2024/papers.html"},{"title":"ICML 2024 Papers","url":"https://icml.cc/virtual/2024/papers.html"},{"title":"Published as a conference paper at ICLR 2025 WHAT TO ALIGN IN MULTIMODAL","url":"https://proceedings.iclr.cc/paper/2025/file/108030643e640ac050e0ed5e6aace48f-Paper-Conference.pdf"},{"title":"ICLR2024 Statistics - Guoqiang Wei","url":"https://guoqiangwei.xyz/iclr2024_stats/iclr2024_submissions.html"}]

Based on the search results, I found information related to CACL (Communication Alignment Contrastive Learning) and multi-agent communication:

## Key Findings

Communication Alignment Contrastive Learning (CACL) is a method that uses a contrastive learning method to align the message space for communication, which pulls messages within a trajectory to be closer to each other and pushes messages of different trajectories to be further apart.

In this approach, messages within a trajectory are considered to be different views of the same data sample with the same label. Practically, each agent has a replay buffer that maintains a batch of trajectory data containing messages received during training to compute the CACL loss.

The results show that CACL induces a more common protocol with the agents compared to baseline methods like AE COMM, which grounds communication without considering messages of other agents.

It's worth noting that the search returned a workshop paper from ICLR 2022 on CACL, along with other multi-agent communication papers from ICLR 2024. While there are multiple papers on multi-agent communication and contrastive learning at ICLR 2024, the specific CACL conference paper appears to have originally been published as a workshop paper in 2022.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa8f4428-c9f3-4713-909d-cdc874815099",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "f1097093-f536-477c-b9b5-ead862305684",
  "sourceToolAssistantUUID": "fa8f4428-c9f3-4713-909d-cdc874815099",
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

_source line 54 · 2026-05-10T22:12:49.730Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UoKyhijky5conzoAbwkkyx`</summary>

```json
{
  "query": "\"information preserving\" multi-agent communication IJCAI 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1097093-f536-477c-b9b5-ead862305684",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauf31Q1neLbeREk6oqzc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c6deed3-2085-42bf-89ff-5643a211c2e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fU7ARE9Y7NPwAc4UZemcU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4012,
      "cache_read_input_tokens": 27984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4012,
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

_source line 55 · 2026-05-10T22:12:50.797Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CzEkAmKQxr6Ap6aSEtxJxa`</summary>

```json
{
  "query": "LTC \"learning through communication\" LLM agents reinforcement learning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c6deed3-2085-42bf-89ff-5643a211c2e7",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauf31Q1neLbeREk6oqzc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9abd2e8e-d498-4f2b-aaa1-b9bfbd4fc88d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015fU7ARE9Y7NPwAc4UZemcU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4012,
      "cache_read_input_tokens": 27984,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4012
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 27984,
          "cache_creation_input_tokens": 4012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4012,
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

_source line 56 · 2026-05-10T22:12:55.298Z_

<details><summary>↩ Tool result · `toolu_01UoKyhijky5conzoAbwkkyx`</summary>

```text
Web search results for query: ""information preserving" multi-agent communication IJCAI 2025"

Links: [{"title":"Multi-Agent Communication with Information Preserving ...","url":"https://www.ijcai.org/proceedings/2025/0008.pdf"},{"title":"dblp: IJCAI 2025","url":"https://dblp.org/db/conf/ijcai/ijcai2025.html"}]

I found relevant results for your search! The paper "Multi-Agent Communication with Information Preserving Graph Contrastive Learning" by Wei Du, Shifei Ding, Wei Guo, Yuqing Sun, Guoxian Yu, and Lizhen Cui was accepted at IJCAI 2025.

The paper is part of the proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence (IJCAI-25). The approach, called MAIL, uses contrastive learning to minimize feature contrastive loss, cross-module loss, and topological contrastive loss to learn expressive message representations.

The paper appears to be available as a PDF in the official IJCAI proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c6deed3-2085-42bf-89ff-5643a211c2e7",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "58f68f17-9a5b-492f-9b7e-abcf7f2c2dac",
  "sourceToolAssistantUUID": "8c6deed3-2085-42bf-89ff-5643a211c2e7",
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

_source line 57 · 2026-05-10T22:12:58.223Z_

<details><summary>↩ Tool result · `toolu_01CzEkAmKQxr6Ap6aSEtxJxa`</summary>

```text
Web search results for query: "LTC "learning through communication" LLM agents reinforcement learning 2025 2026"

Links: [{"title":"Adapting LLM Agents with Universal Feedback in Communication","url":"https://arxiv.org/html/2310.01444v3"},{"title":"Adapting LLM Agents Through Communication | OpenReview","url":"https://openreview.net/forum?id=wOelVq8fwL"},{"title":"[2605.02801] Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces","url":"https://arxiv.org/abs/2605.02801"},{"title":"Towards Communication Efficient Multi-Agent Cooperations: Reinforcement Learning and LLM | TechRxiv","url":"https://www.techrxiv.org/doi/full/10.36227/techrxiv.173739115.54193062/v2"},{"title":"[2310.01444] Adapting LLM Agents with Universal Feedback in Communication","url":"https://arxiv.org/abs/2310.01444"},{"title":"Towards Communication Efficient Multi-Agent Cooperations: Reinforcement Learning and LLM","url":"https://www.techrxiv.org/users/878096/articles/1259644-towards-communication-efficient-multi-agent-cooperations-reinforcement-learning-and-llm"},{"title":"Adapting LLM Agents Through Communication","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231001444W/abstract"},{"title":"Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces","url":"https://arxiv.org/html/2605.02801"},{"title":"(PDF) ADAPTING LLM AGENTS THROUGH COMMUNICATION","url":"https://www.researchgate.net/publication/400069878_ADAPTING_LLM_AGENTS_THROUGH_COMMUNICATION"},{"title":"Paper page - Adapting LLM Agents Through Communication","url":"https://huggingface.co/papers/2310.01444"}]

Based on the search results, I found relevant research on "Learning through Communication" (LTC) and related work on LLM agents with reinforcement learning:

## Learning Through Communication (LTC)

Learning through Communication (LTC) is a framework designed to facilitate the training of LLM agents with both linguistic feedback and non-linguistic reward signals. The approach uses a universal buffer to store all feedback and an iterative pipeline to enable an LLM agent to explore and update its policy in a given environment.

The LTC paradigm includes three specific communication patterns: Single-agent Monologue, Multi-agent Dialogue, and Teacher-student Dialogue, which can be combined to generate diverse structured interactions and feedback signals for agent training.

## Research Findings

LTC was evaluated on four diverse datasets: ALFWorld (single-agent), HotpotQA (multi-agent collaboration), Chameleon (multi-agent competition), and GSM8k (multi-agent teacher-student), and outperformed supervised instruction fine-tuning baselines by 3.6% to 12%.

## Recent Related Work (2026)

More recent work published in May 2026 extends this direction. A new paper studies reinforcement learning for LLM-based multi-agent systems through orchestration traces: temporal interaction graphs whose events include sub-agent spawning, delegation, communication, tool use, return, aggregation, and stopping decisions.

The search results show active research in 2025-2026 on combining communication mechanisms with reinforcement learning for LLM-based multi-agent systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9abd2e8e-d498-4f2b-aaa1-b9bfbd4fc88d",
  "isSidechain": true,
  "promptId": "c4053383-51a2-4c53-bef4-50bbbd8ab467",
  "agentId": "a6e82473bf7a9063b",
  "type": "user",
  "uuid": "1dac36b0-49ec-4fbd-b4d4-660bf44de71d",
  "sourceToolAssistantUUID": "9abd2e8e-d498-4f2b-aaa1-b9bfbd4fc88d",
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

_source line 58 · 2026-05-10T22:14:04.803Z_

Here is the comprehensive report of all relevant papers found that could be concurrent or competing work with "bilateral contrastive training for multi-agent LLM communication."

---

## HIGHLY RELEVANT PAPERS (Directly Overlapping Ideas)

### 1. CACL: Learning Multi-Agent Communication with Contrastive Learning
- **Venue:** ICLR 2024 (conference paper, building on ICLR 2022 workshop paper)
- **arXiv:** 2307.01403
- **Description:** Proposes Communication Alignment Contrastive Learning (CACL), which treats messages sent between agents as different incomplete views of the same environment state and uses contrastive learning to maximize mutual information between messages within a trajectory. Messages from the same trajectory are pulled closer; messages from different trajectories are pushed apart. This is the closest existing work to bilateral contrastive training -- it applies a CLIP-style contrastive objective directly to inter-agent messages. However, it operates in the traditional MARL (small-model) setting, not with LLMs.
- [Paper PDF](https://proceedings.iclr.cc/paper_files/paper/2024/file/de2ad3ed44ee4e675b3be42aa0b615d0-Paper-Conference.pdf)

### 2. Learning to Ground Decentralized Multi-Agent Communication with Contrastive Learning
- **Venue:** ICLR 2022 Workshop (EmeCom)
- **Description:** The precursor workshop paper introducing CACL, grounding decentralized multi-agent communication via contrastive learning to maximize mutual information between agent messages. Demonstrates that contrastive grounding induces more symmetric communication and captures global state information.
- [OpenReview](https://openreview.net/forum?id=rLceWXWCmZc)

### 3. MAIL: Multi-Agent Communication with Information Preserving Graph Contrastive Learning
- **Venue:** IJCAI 2025
- **Description:** Proposes a graph contrastive learning approach for multi-agent communication that minimizes feature contrastive loss, cross-module loss, and topological contrastive loss to learn expressive message representations. Extends contrastive communication to graph-structured agent topologies.
- [IJCAI 2025 Proceedings PDF](https://www.ijcai.org/proceedings/2025/0008.pdf)

### 4. MAGE: Learning Multi-Agent Communication via Graph Contrastive Learning
- **Venue:** Pattern Recognition (2025)
- **Description:** Uses graph contrastive learning for multi-agent communication by generating correlated graph views through stochastic corruption, then training with contrastive loss to enhance consistency of agent features. First work to extend graph contrastive learning to MARL communication.
- [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0031320325007538)

---

## STRONGLY RELEVANT PAPERS (Multi-Agent LLM Training / GRPO Extensions)

### 5. M-GRPO: Multi-Agent Deep Research -- Training Multi-Agent Systems with M-GRPO
- **arXiv:** 2511.13288 (November 2025)
- **Description:** Extends GRPO to vertical (hierarchical) multi-agent LLM systems. Computes group-relative advantages for both main and sub-agents, introduces trajectory-alignment for variable sub-agent invocations, and uses a decoupled training pipeline where agents on separate servers exchange minimal statistics. Directly relevant as it applies GRPO to multi-agent LLM training.
- [arXiv](https://arxiv.org/abs/2511.13288)

### 6. MAGRPO: LLM Collaboration with Multi-Agent Reinforcement Learning
- **Venue:** AAAI 2026
- **Description:** Formalizes LLM dialogue as a Dec-POMDP and introduces Multi-Agent Group Relative Policy Optimization. Uses centralized group-relative advantages for joint optimization while preserving decentralized execution. Directly trains multiple LLMs to collaborate via shared reward signals. Open-source library CoMLRL released.
- [arXiv](https://arxiv.org/abs/2508.04652) | [AAAI 2026 Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40487)

### 7. MARFT: Multi-Agent Reinforcement Fine-Tuning
- **arXiv:** 2504.16129 (April 2025, updated November 2025)
- **Description:** Introduces the MARFT paradigm for fine-tuning LLM-based multi-agent systems with RL. Proposes Flex-MG mechanism and a universal algorithmic framework specifically tailored for LLM-based MAS. Addresses the gap between traditional MARL and LLM-based multi-agent systems.
- [arXiv](https://arxiv.org/abs/2504.16129)

### 8. MARTI: A Framework for Multi-Agent LLM Systems Reinforced Training and Inference
- **Venue:** ICLR 2026
- **Institution:** Tsinghua University
- **Description:** Open-source framework for training LLM-based multi-agent systems with RL. Supports centralized multi-agent interactions with distributed policy training, multi-turn asynchronous rollouts, dynamic workflows, and both verifiable and generative rewards. MARTI-v2 adds tree search-augmented RL.
- [OpenReview](https://openreview.net/forum?id=E7jZqo0A50) | [GitHub](https://github.com/TsinghuaC3I/MARTI)

### 9. MARS: Co-evolving Dual-System Deep Research via Multi-Agent Reinforcement Learning
- **arXiv:** 2510.04935 (October 2025, updated February 2026)
- **Description:** Co-evolution framework jointly optimizing dual cognitive systems (System 1 fast processing + System 2 deliberate reasoning) through multi-agent RL. Extends GRPO to simultaneously optimize both systems with multi-turn tool interactions. Relevant as it trains bilateral agent roles with shared trajectory rewards.
- [arXiv](https://arxiv.org/abs/2510.04935)

---

## RELEVANT PAPERS (Communication Optimization / Latent Communication)

### 10. LatentMAS: Latent Collaboration in Multi-Agent Systems
- **Venue:** ICML 2026 Spotlight
- **arXiv:** 2511.20639 (November 2025)
- **Description:** Moves agent collaboration from token space into latent space. Agents communicate by passing latent thoughts (last-layer hidden embeddings) through shared working memory. Achieves up to 14.6% accuracy improvement with 70-84% token reduction and 4x faster inference. Training-free latent-space alignment.
- [arXiv](https://arxiv.org/abs/2511.20639) | [GitHub](https://github.com/Gen-Verse/LatentMAS)

### 11. The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems
- **arXiv:** 2602.15382 (February 2026)
- **Description:** Maps heterogeneous reasoning traces into a shared continuous latent space via a Universal Visual Codec and injects them into the receiver's visual pathway. Uses self-supervised distillation (teacher-student) to align high-speed visual channel with text-based reasoning. Reduces sender-receiver alignment complexity from O(N^2) to O(N) with hub-and-spoke topology.
- [arXiv](https://arxiv.org/abs/2602.15382)

### 12. Adapting LLM Agents Through Communication (LTC)
- **Venue:** Under review / OpenReview
- **arXiv:** 2310.01444
- **Description:** Proposes Learning Through Communication (LTC), enabling LLM agents to improve through interactions with environments and other agents. Defines three communication patterns: single-agent monologue, multi-agent dialogue, and teacher-student dialogue. Uses universal buffer for linguistic and reward feedback with iterative policy updates.
- [OpenReview](https://openreview.net/forum?id=wOelVq8fwL)

### 13. Cut the Crap: An Economical Communication Pipeline for LLM-based Multi-Agent Systems (AgentPrune)
- **Venue:** ICLR 2025
- **arXiv:** 2410.02506
- **Description:** Identifies and formalizes communication redundancy in LLM-based multi-agent pipelines. Proposes AgentPrune for one-shot pruning of the spatial-temporal message-passing graph. Achieves comparable results with ~87% cost reduction.
- [arXiv](https://arxiv.org/abs/2410.02506)

### 14. Language Grounded Multi-Agent Reinforcement Learning with Human-Interpretable Communication
- **arXiv:** 2409.17348 (September 2024, updated 2025)
- **Description:** Grounds MARL agent communication in natural language using synthetic data from embodied LLMs. Demonstrates zero-shot generalization in ad-hoc teamwork with unseen teammates. Combines RL loss with supervised learning loss for end-to-end training.
- [arXiv](https://arxiv.org/abs/2409.17348)

---

## CONTEXTUAL / SURVEY PAPERS

### 15. Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems
- **arXiv:** 2502.14321 (February 2025, updated June 2025)
- **Description:** Comprehensive survey examining LLM-based MAS from a communication perspective. Proposes a framework integrating system-level communication (architecture, goals, protocols) with internal communication (strategies, paradigms, content). Highlights challenges in communication efficiency, security, and scalability.
- [arXiv](https://arxiv.org/abs/2502.14321)

### 16. Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces
- **arXiv:** 2605.02801 (May 2026)
- **Description:** Surveys and systematizes RL methods for LLM-based MAS through orchestration traces. Documents the recent emergence of hierarchical GRPO decompositions, message-level counterfactual credit assignment, and Shapley-based agent-level credit methods from 2025-Q2 through May 2026.
- [arXiv](https://arxiv.org/abs/2605.02801)

### 17. Active Learning for Communication Structure Optimization in LLM-Based Multi-Agent Systems
- **arXiv:** 2605.05703 (May 2026)
- **Authors:** Huchen Yang, Xinghao Dong, Dan Negrut, Jin-Long Wu
- **Description:** Optimizes communication topology in LLM-based MAS using active learning. Directly relevant to the structural aspects of multi-agent communication design.

---

## KEY GAP ANALYSIS

Based on this extensive search, the specific niche of **bilateral contrastive training applied to sender AND receiver in multi-agent LLM systems** does not appear to have been published. The closest works are:

- **CACL (ICLR 2024)** does bilateral contrastive alignment of agent messages, but in small MARL models, not LLMs.
- **MAGRPO / M-GRPO / MARFT** apply GRPO-based RL to multi-agent LLM training, but do not use contrastive objectives on the communication channel itself.
- **LatentMAS and Vision Wormhole** address sender-receiver alignment in LLM agents, but through latent-space distillation rather than contrastive losses.
- **No paper found** applies a CLIP/CLIPO-style contrastive loss specifically to bilateral sender-receiver LLM communication in multi-agent systems.

The proposal's combination of (a) contrastive loss on the communication channel + (b) applied to LLM-scale agents + (c) bilateral training of both sender and receiver appears to be a novel intersection as of May 2026. The most threatening concurrent work would be CACL's potential extension to LLMs, and the GRPO-family papers (MAGRPO, M-GRPO, MARTI, MARFT) which could be combined with contrastive communication objectives.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dac36b0-49ec-4fbd-b4d4-660bf44de71d",
  "isSidechain": true,
  "agentId": "a6e82473bf7a9063b",
  "requestId": "req_011Cauf3pDadpeZmvfcNbi9M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8add12fb-fb28-4a5f-9596-23a65178f804",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0c886791-a9d9-487c-99a0-b2a7b1d3d99e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019a5SKQGPwJjRZZMoHwSiMT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1348,
      "cache_read_input_tokens": 31996,
      "output_tokens": 2990,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1348
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2990,
          "cache_read_input_tokens": 31996,
          "cache_creation_input_tokens": 1348,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1348,
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
