# Research conversation: I need to find recent (2025-2026) work on document-level relation extraction, especially any work that: 1. Uses LLMs for

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 103
- **Recorded user turns:** 1
- **Tool calls:** 46
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a5ef95c84eda75a4a.jsonl`
- **Structured JSON:** [`3c4fd75024c2b974c6f6.json`](../../sessions/3c/3c4fd75024c2b974c6f6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

103 recorded events

### User

_source line 1 · 2026-05-10T19:28:54.406Z_

I need to find recent (2025-2026) work on document-level relation extraction, especially any work that:
1. Uses LLMs for document-level RE on DocRED
2. Combines evidence generation with relation extraction
3. Uses reinforcement learning (GRPO, PPO, DPO) for document-level IE

Search for:
- "document-level relation extraction" 2025 2026 site:arxiv.org
- "DocRED" LLM GRPO 2025 2026
- "evidence generation" "relation extraction" 2025 2026
- "document relation extraction" reinforcement learning 2026
- "joint extraction evidence" document-level 2025 2026
- Check CDER (arXiv 2504.06529) - what does it do exactly?
- Check Ru-LLM (2026) - what does it achieve on DocRED?
- Any new LLM-based DocRE methods from late 2025 or 2026

Also check: has anyone applied GRPO specifically to document-level RE (not sentence-level)?

Use WebSearch and WebFetch. Report all relevant findings with paper titles, venues, and key results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "7d2bd687-d552-4e16-9cdd-a7295ae8f83e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:28:54.410Z_

```json
{
  "parentUuid": "7d2bd687-d552-4e16-9cdd-a7295ae8f83e",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
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
  "uuid": "8ca26cb4-40e2-4ec9-ab38-a65a982abfb9",
  "timestamp": "2026-05-10T19:28:54.410Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:28:56.752Z_



I'll conduct a comprehensive search on document-level relation extraction research from 2025-2026. Let me start with multiple parallel searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ca26cb4-40e2-4ec9-ab38-a65a982abfb9",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSYBnssgofcdWeDYuPe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bea1c3a-f53f-459b-8669-e958ac1922f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018UeQwoEvygbb42ciHqBCSG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 832,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 832,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T19:28:56.912Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011Gy5ughu1VYfbYtqVuQuZZ`</summary>

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
  "parentUuid": "4bea1c3a-f53f-459b-8669-e958ac1922f0",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSYBnssgofcdWeDYuPe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07352aa6-284f-4d6e-9bd8-dab815027972",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018UeQwoEvygbb42ciHqBCSG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 832,
      "cache_read_input_tokens": 8223,
      "output_tokens": 110,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 832
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 110,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 832,
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

_source line 5 · 2026-05-10T19:28:56.916Z_

<details><summary>↩ Tool result · `toolu_011Gy5ughu1VYfbYtqVuQuZZ`</summary>

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
  "parentUuid": "07352aa6-284f-4d6e-9bd8-dab815027972",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "3f0fa78b-b28f-426e-8bb0-14097bdd5818",
  "sourceToolAssistantUUID": "07352aa6-284f-4d6e-9bd8-dab815027972",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:28:59.815Z_



Now let me launch all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f0fa78b-b28f-426e-8bb0-14097bdd5818",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSYNdVqXRQVnAx1i89c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74d605ad-18f9-4cbb-b490-7280b5881e90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDThaywygX87Gyg2nut1SQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 7 · 2026-05-10T19:29:00.403Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KEmCXrkD1z7TJnf6bBQxwQ`</summary>

```json
{
  "query": "\"document-level relation extraction\" 2025 2026 site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74d605ad-18f9-4cbb-b490-7280b5881e90",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSYNdVqXRQVnAx1i89c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8efbea32-26ff-46f9-8da8-cea059e79d4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDThaywygX87Gyg2nut1SQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 8 · 2026-05-10T19:29:01.385Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X71Czkqhmbup1GPYeTZoKJ`</summary>

```json
{
  "query": "\"DocRED\" LLM GRPO 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8efbea32-26ff-46f9-8da8-cea059e79d4e",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSYNdVqXRQVnAx1i89c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65988f26-ff12-4ef6-ae29-cd526d00c59b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDThaywygX87Gyg2nut1SQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 9 · 2026-05-10T19:29:01.793Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LmZRkPrtVGQryRU6zEzdQM`</summary>

```json
{
  "query": "\"evidence generation\" \"relation extraction\" 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65988f26-ff12-4ef6-ae29-cd526d00c59b",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSYNdVqXRQVnAx1i89c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be56e1c9-9e9c-45ce-aff2-22e527ed2df3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDThaywygX87Gyg2nut1SQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 10 · 2026-05-10T19:29:02.244Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BZ15GdmUw4XjturALUB5sG`</summary>

```json
{
  "query": "\"document relation extraction\" reinforcement learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be56e1c9-9e9c-45ce-aff2-22e527ed2df3",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSYNdVqXRQVnAx1i89c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2baed75-6f8e-4674-bf21-4d0c4fe7a3ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDThaywygX87Gyg2nut1SQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 11 · 2026-05-10T19:29:03.481Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WbSHJb9NrXVHy7fxXmio7U`</summary>

```json
{
  "query": "arXiv 2504.06529 CDER document relation extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2baed75-6f8e-4674-bf21-4d0c4fe7a3ee",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSYNdVqXRQVnAx1i89c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e41f633-e171-4529-bf20-00644a910644",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDThaywygX87Gyg2nut1SQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1919,
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

_source line 12 · 2026-05-10T19:29:03.652Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X3JbQfGBT28e8Z5X84X77a`</summary>

```json
{
  "query": "GRPO \"document-level relation extraction\" 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e41f633-e171-4529-bf20-00644a910644",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSYNdVqXRQVnAx1i89c",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92c438c0-d8b6-4c0e-8296-b53f188808ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDThaywygX87Gyg2nut1SQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1919,
      "cache_read_input_tokens": 9055,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1919
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 327,
          "cache_read_input_tokens": 9055,
          "cache_creation_input_tokens": 1919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1919,
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

_source line 13 · 2026-05-10T19:29:08.317Z_

<details><summary>↩ Tool result · `toolu_01X71Czkqhmbup1GPYeTZoKJ`</summary>

```text
Web search results for query: ""DocRED" LLM GRPO 2025 2026"

Links: [{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"Reinforcement Learning (RL) Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide"},{"title":"The State Of LLMs 2025: Progress, Problems, and Predictions | Sebastian Raschka, PhD","url":"https://sebastianraschka.com/blog/2025/state-of-llms-2025.html"},{"title":"State of LLMs 2026: RLVR, GRPO, Inference Scaling — Sebastian Raschka - YouTube","url":"https://www.youtube.com/watch?v=K5WPr5dtne0"},{"title":"Use large language model to enhance reasoning of another large language model through reward updated GRPO | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-39296-8"},{"title":"GRPO-$\\lambda$: Credit Assignment improves LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=iRWqcnBlLQ"},{"title":"Turn-Level Advantage Estimation with PPO for Improved ...","url":"https://aclanthology.org/2026.findings-eacl.328.pdf"},{"title":"How Top AI Labs Are Building RL Agents in 2026","url":"https://blog.dailydoseofds.com/p/how-top-ai-labs-are-building-rl-agents"},{"title":"GRPO++: Tricks for Making RL Actually Work","url":"https://cameronrwolfe.substack.com/p/grpo-tricks"}]

Based on the search results, here's what I found regarding your query about DocRED, LLM, GRPO in 2025-2026:

The search results primarily focus on GRPO (Group Relative Policy Optimization) and related LLM training techniques in 2025-2026, but I didn't find specific results directly mentioning DocRED in connection with these topics.

## What I Found:

**GRPO Overview:**
GRPO (Group Relative Policy Optimization) is an RL algorithm that samples multiple responses per prompt and computes advantages by comparing them within the group. It was introduced by DeepSeek and is now used in models like Nemotron 3 Super.

**GRPO in 2025-2026:**
RLVR with GRPO became the dominant approach for training reasoning models through 2025, with every major lab releasing a reasoning variant following this recipe.

**Recent Research:**
A novel update to GRPO's objective function with a novel reward component was proposed to improve training efficiency and model performance. Additionally, GRPO-λ, a novel extension to GRPO, enhances credit assignment in RL finetuning of LLMs for complex reasoning tasks.

However, the search results don't contain specific information about DocRED in the context of GRPO or LLM training. If you're looking for information about DocRED specifically, you may want to clarify whether you're referring to a dataset, benchmark, or particular research paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65988f26-ff12-4ef6-ae29-cd526d00c59b",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "67f57c8e-34e4-48a9-b5ef-c0706ff4d180",
  "sourceToolAssistantUUID": "65988f26-ff12-4ef6-ae29-cd526d00c59b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T19:29:08.374Z_

<details><summary>↩ Tool result · `toolu_01KEmCXrkD1z7TJnf6bBQxwQ`</summary>

```text
Web search results for query: ""document-level relation extraction" 2025 2026 site:arxiv.org"

Links: [{"title":"[2309.16396] A Comprehensive Survey of Document-level Relation Extraction (2016-2023)","url":"https://arxiv.org/abs/2309.16396"},{"title":"[2508.00757] GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/abs/2508.00757"},{"title":"KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction with Comprehensive Reasoning Abilities","url":"https://arxiv.org/html/2501.00571"},{"title":"[2310.13000] Document-Level Relation Extraction with Relation Correlation Enhancement","url":"https://arxiv.org/abs/2310.13000"},{"title":"[1906.06127] DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://arxiv.org/abs/1906.06127"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/pdf/2508.00757"},{"title":"[2602.04320] A Domain-Specific Curated Benchmark for Entity and Document-Level Relation Extraction","url":"https://arxiv.org/abs/2602.04320"},{"title":"[2503.13885] COMM:Concentrated Margin Maximization for Robust Document-Level Relation Extraction","url":"https://arxiv.org/abs/2503.13885"},{"title":"CLEF HIPE-2026: Evaluating Accurate and Efficient Person–Place Relation Extraction from Multilingual Historical Texts","url":"https://arxiv.org/html/2602.17663"},{"title":"[2511.08143] Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction","url":"https://arxiv.org/abs/2511.08143"}]

The search returned several relevant papers on document-level relation extraction from arXiv. Here are the results from 2025-2026:

## Recent Papers (2025-2026)

1. **GLiDRE: Generalist Lightweight model for Document-level Relation Extraction** (October 2025)
   - Introduces GLiDRE, a compact model for document-level relation extraction designed to work efficiently in both supervised and few-shot settings

2. **KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction** (August 2025)
   - Constructs a document graph for semantic encoding, integrates co-reference resolution, expands it into a document knowledge graph through external knowledge retrieval, and proposes an axis attention mechanism for cross-sentence logical reasoning

3. **COMM: Concentrated Margin Maximization for Robust Document-Level Relation Extraction** (March 2025)
   - Uses instance-aware reasoning to dynamically capture pertinent information of entity pairs and employs Concentrated Margin Maximization to adjust margins between prediction logits and decision threshold, enhancing relational feature extraction

4. **Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction** (November 2025)
   - Proposes RelPrior paradigm using binary relation as a prior to filter irrelevant entity pairs and match entities for triple extraction instead of directly predicting relations

5. **A Domain-Specific Curated Benchmark for Entity and Document-Level Relation Extraction** (February 2026)
   - Introduces GutBrainIE, a benchmark based on more than 1,600 PubMed abstracts manually annotated with fine-grained entities, concept-level links, and relations

6. **CLEF HIPE-2026: Evaluating Accurate and Efficient Person–Place Relation Extraction** (February 2026)
   - HIPE-2026 is a CLEF Evaluation Lab dedicated to the extraction of person–place relations in multilingual historical documents


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8efbea32-26ff-46f9-8da8-cea059e79d4e",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "e2ff8564-70e8-4d1f-bcef-d504ef1a62e0",
  "sourceToolAssistantUUID": "8efbea32-26ff-46f9-8da8-cea059e79d4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T19:29:08.610Z_

<details><summary>↩ Tool result · `toolu_01BZ15GdmUw4XjturALUB5sG`</summary>

```text
Web search results for query: ""document relation extraction" reinforcement learning 2026"

Links: [{"title":"A New Hierarchical Reinforcement Learning Framework for Relation Extraction | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9540098/"},{"title":"Incorporating Human Knowledge in Neural Relation Extraction with Reinforcement Learning | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/8852431/"},{"title":"A Two-Level Noise-Tolerant Model for Relation Extraction with Reinforcement Learning | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9194528/"},{"title":"A Reinforcement Learning Framework for N-Ary Document-Level Relation Extraction | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10549760/"},{"title":"Joint Entity and Relation Extraction Based on Reinforcement Learning | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/8822686/"},{"title":"Reinforcement Learning for Distantly Supervised Relation Extraction | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/abstract/document/8768386/"},{"title":"Reducing Wrong Labels for Distantly Supervised Relation Extraction With Reinforcement Learning | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9079540/"},{"title":"Reinforcement Learning with Dual Attention Guided Graph Convolution for Relation Extraction | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9412654/"},{"title":"URRel: Joint Entity and Relation Extraction in Chinese Medical Texts via Unified Representation and Reinforcement Learning With Overlapping Relations - Xu - 2026 - Expert Systems - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1111/exsy.70214"},{"title":"Deep mining the textual gold in relation extraction | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-024-11042-4"}]

Based on the web search results, I found several research works on document-level relation extraction using reinforcement learning approaches:

## Recent Research (2026)

A recent 2026 study introduced URRel, a model combining unified coding and reinforcement learning techniques for entity and relationship extraction. URRel uses a semantic fusion approach to merge sentences and relational descriptions into a single representation, allowing simultaneous capture of entities and their relationships.

## Document-Level Approaches

A reinforcement learning-based relation classifier training framework has been proposed for N-ary Document-Level relation extraction, which can handle relations that include an arbitrary number of entities and span multiple sentences within a document.

## Key Research Areas

Hierarchical reinforcement learning (HRL-RL) has been proposed to deal with relationship extraction by adopting joint extraction paradigms. Another approach uses sentence-level label denoising based on reinforcement learning and Deep Q Network (DQN), a value-based RL algorithm, to select the most reliable labels from multiple relations.

More recent work addresses relationship extraction by capturing contextual dependencies using attention mechanisms and distributional reinforcement learning, creating a Dual Attention Graph Convolutional Network (DAGCN).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2baed75-6f8e-4674-bf21-4d0c4fe7a3ee",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "bed52b63-a5f8-4976-b981-76ad29840b87",
  "sourceToolAssistantUUID": "a2baed75-6f8e-4674-bf21-4d0c4fe7a3ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T19:29:09.416Z_

<details><summary>↩ Tool result · `toolu_01LmZRkPrtVGQryRU6zEzdQM`</summary>

```text
Web search results for query: ""evidence generation" "relation extraction" 2025 2026"

Links: [{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"The construction and refined extraction techniques of knowledge graph based on large language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-38066-w"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers | ACM Computing Surveys","url":"https://dl.acm.org/doi/abs/10.1145/3674501"},{"title":"Evidence selection via multi-aspect query diversification for cross-document relation extraction | Journal of Intelligent Information Systems","url":"https://link.springer.com/article/10.1007/s10844-025-00952-6"},{"title":"Clinical entity augmented retrieval for clinical information extraction | npj Digital Medicine","url":"https://www.nature.com/articles/s41746-024-01377-1"},{"title":"Event Extraction in Large Language Model: A Holistic Survey of Method, Modality, and Future","url":"https://arxiv.org/html/2512.19537v1"},{"title":"EMERGE: A Benchmark for Updating Knowledge Graphs with","url":"https://arxiv.org/pdf/2507.03617"},{"title":"2025 in Review: Evidence Synthesis at a Turning Point - PICO Portal","url":"https://picoportal.org/2025/12/22/2025-year-end-recap/"},{"title":"Agricultural Meteorological Disaster Relation Extraction ...","url":"https://www.preprints.org/manuscript/202601.2029/v1/download"}]

Here are the search results for "evidence generation" "relation extraction" 2025 2026:

## Key Findings:

**Relation Extraction with Evidence Integration:**

E2GRE tackles the challenge of handling relations spanning multiple sentences by jointly extracting relations and their supporting evidence sentences using BERT as an input encoder.

One notable approach uses evidence information to guide attention modules to emphasize important evidence, with the model self-trained to learn relationships between entities using automatically generated evidence from large amounts of data without requiring explicit evidence annotations.

**Knowledge Graph Construction and Relation Extraction:**

Fine-tuned language models achieve substantial gains in relationship extraction accuracy, while the resulting knowledge graphs show strong performance in semantic coherence and operational reasoning assessments.

**Cross-Document Evidence Selection:**

MAQD is a novel cross-document relation extraction approach that enhances evidence selection through multi-aspect query diversification, constructing a knowledge-aware entity graph from the original text and leveraging large language models for multi-faceted query augmentation.

**Challenges in Generation-Based Approaches:**

Large language models and multimodal LLMs are changing event extraction through prompting and generation in zero-shot or few-shot settings, yet LLM-based pipelines face deployment gaps, including hallucinations under weak constraints and fragile temporal and causal linking over long contexts and across documents.

The research shows an active focus on integrating evidence generation with relation extraction tasks, particularly using LLMs and attention mechanisms to identify and verify supporting evidence for extracted relationships.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be56e1c9-9e9c-45ce-aff2-22e527ed2df3",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "5ed7addd-5f34-49d8-a2fb-acce781a15fa",
  "sourceToolAssistantUUID": "be56e1c9-9e9c-45ce-aff2-22e527ed2df3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T19:29:10.177Z_

<details><summary>↩ Tool result · `toolu_01X3JbQfGBT28e8Z5X84X77a`</summary>

```text
Web search results for query: "GRPO "document-level relation extraction" 2025 2026"

Links: [{"title":"Document-Level Relation Extraction with Global ...","url":"https://aclanthology.org/2025.findings-acl.1002.pdf"},{"title":"Toward Better Document-Level Relation Extraction: De-sampling and Mixture of Experts in Action | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-04549-2_12"},{"title":"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning | OpenReview","url":"https://openreview.net/forum?id=SVl9tIADWV"},{"title":"ICML Poster DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning","url":"https://icml.cc/virtual/2025/poster/45220"},{"title":"Document-Level Relation Extraction with Global Relations and Entity Pair Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1002/"},{"title":"Dual reasoning enhanced document-level relation extraction | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-026-12099-8"},{"title":"Enhancing cross-evidence reasoning graph for document-level relation extraction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/"},{"title":"Document-Level Relation Extraction","url":"https://www.emergentmind.com/topics/document-level-relation-extraction"},{"title":"[2201.04826] Document-level Relation Extraction with Context Guided Mention Integration and Inter-pair Reasoning","url":"https://arxiv.org/abs/2201.04826"},{"title":"Document-level relation extraction via commonsense knowledge enhanced graph representation learning | Applied Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10489-024-05985-y"}]

Based on the search results, here are the findings related to GRPO and document-level relation extraction from 2025-2026:

## Recent Research on Document-Level Relation Extraction (2025-2026)

Several recent papers have addressed document-level relation extraction in this timeframe:

**GREP Model (2025)**: A paper titled "Document-Level Relation Extraction with Global Relations and Entity Pair Reasoning" was published in Findings of the Association for Computational Linguistics: ACL 2025. GREP leverages the global interdependencies between entity pairs to capture fine-grained interactions and perform multi reasoning at the entity pair level, and proposes an auxiliary task that predicts all possible relations in advance that exist in a document.

**Other Notable Work (2025-2026)**:
- A paper on "Toward Better Document-Level Relation Extraction: De-sampling and Mixture of Experts in Action" appeared in ICANN 2025
- A model called "Gega: Graph convolutional networks and evidence retrieval guided attention for enhanced document-level relation extraction" was presented at ICASSP 2025
- "DocKS-RAG" aims to extract comprehensive correlations between entities and relations from documents, using transfer learning on pre-trained language models for richer contextual representation

**Note**: The search results show extensive research on document-level relation extraction but do not specifically mention "GRPO" as an acronym or methodology in these 2025-2026 papers. If you're looking for information about GRPO specifically, it may be a technique within one of these papers or a different research direction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92c438c0-d8b6-4c0e-8296-b53f188808ba",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "2eebf7d6-f16a-4406-baf5-8242c87c06d1",
  "sourceToolAssistantUUID": "92c438c0-d8b6-4c0e-8296-b53f188808ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T19:29:10.746Z_

<details><summary>↩ Tool result · `toolu_01WbSHJb9NrXVHy7fxXmio7U`</summary>

```text
Web search results for query: "arXiv 2504.06529 CDER document relation extraction"

Links: [{"title":"[2504.06529] CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/abs/2504.06529"},{"title":"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://arxiv.org/html/2504.06529"},{"title":"(PDF) CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction","url":"https://www.researchgate.net/publication/390638674_CDER_Collaborative_Evidence_Retrieval_for_Document-level_Relation_Extraction"},{"title":"[PDF] CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CDER:-Collaborative-Evidence-Retrieval-for-Relation-Tran-Li/07f36e6f29c07f0edce7465f4d005bd34ac659ce"},{"title":"CDER: Collaborative Evidence Retrieval for Document-Level Relation Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-97-4982-9_3"},{"title":"open source AI","url":"https://bytez.com/docs/arxiv/2504.06529/paper"},{"title":"arXiv:2504.06529v1 [cs.CL] 9 Apr 2025","url":"https://arxiv.org/pdf/2504.06529"},{"title":"Document-Level In-Context Few-Shot Relation Extraction via Pre-Trained Language Models","url":"https://arxiv.org/html/2310.11085v4"},{"title":"Towards Better Graph-based Cross-document Relation Extraction via Non-bridge Entity Enhancement and Prediction Debiasing","url":"https://arxiv.org/html/2406.16529v1"},{"title":"Document-Level Relation Extraction with Reconstruction | Request PDF","url":"https://www.researchgate.net/publication/363410025_Document-Level_Relation_Extraction_with_Reconstruction"}]

Based on the search results, here's information about the paper arXiv 2504.06529:

## CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction

Document-level Relation Extraction (DocRE) involves identifying relations between entities across multiple sentences in a document. Evidence sentences, crucial for precise entity pair relationships identification, enhance focus on essential text segments, improving DocRE performance.

### The Problem

Existing evidence retrieval systems often overlook the collaborative nature among semantically similar entity pairs in the same document, hindering the effectiveness of the evidence retrieval task.

### The Solution

The authors propose a novel evidence retrieval framework, namely CDER, which employs an attentional graph-based architecture to capture collaborative patterns and incorporates a dynamic sub-structure for additional robustness in evidence retrieval.

### Technical Approach

CDER transforms the document into a bipartite graph with entity pair and sentence nodes, partitioning it into three sub-graphs: (i) Entity Pair sub-graph models collaboration, (ii) Entity Pair-Sentence sub-graph captures semantic relationships, and (iii) Sentence sub-graph aids co-reference reasoning.

### Results

Experimental results on the benchmark DocRE dataset show that CDER not only excels in the evidence retrieval task but also enhances overall performance of existing DocRE system.

The paper was submitted on April 9, 2025, and the authors' code is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e41f633-e171-4529-bf20-00644a910644",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "d63c4b7e-decc-4493-9a78-e7b80dc1cdf1",
  "sourceToolAssistantUUID": "2e41f633-e171-4529-bf20-00644a910644",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-10T19:29:13.379Z_

Good, I have initial results. Let me now do deeper dives on the most promising leads.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d63c4b7e-decc-4493-9a78-e7b80dc1cdf1",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSZPZLaDfjne1uLq6VC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51ab34da-fde2-4f42-b950-9757000b292c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWoYFDveynvdsSkLnsoFxG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 4943,
      "cache_read_input_tokens": 10974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4943,
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

_source line 20 · 2026-05-10T19:29:15.326Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KxfhWymajnkvXGQAu9GRwB`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.06529",
  "prompt": "Extract the full paper details: title, authors, date, abstract, key methods, datasets used, main results/numbers on DocRED, and any evidence retrieval results. What exactly does CDER do and how well does it perform?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51ab34da-fde2-4f42-b950-9757000b292c",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSZPZLaDfjne1uLq6VC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec0ae898-c936-40e6-9e87-6c40b5a4d3b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWoYFDveynvdsSkLnsoFxG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 4943,
      "cache_read_input_tokens": 10974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4943,
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

_source line 21 · 2026-05-10T19:29:17.209Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011dLze7iQkDQcxBgp1a7GAs`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.08143",
  "prompt": "Extract full details: title, authors, date, abstract, key method, datasets, results on DocRED. What is the RelPrior paradigm and how does it use LLMs for document-level relation extraction?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec0ae898-c936-40e6-9e87-6c40b5a4d3b2",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSZPZLaDfjne1uLq6VC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af7869f5-0e4b-4b92-adfc-eefddbb8baa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWoYFDveynvdsSkLnsoFxG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 4943,
      "cache_read_input_tokens": 10974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4943,
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

_source line 22 · 2026-05-10T19:29:18.161Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013YbZnajvCx21GUH2WWKQDg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.00757",
  "prompt": "Extract full details: title, authors, date, abstract, key method, datasets, results on DocRED. What is GLiDRE and how does it perform compared to other methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af7869f5-0e4b-4b92-adfc-eefddbb8baa0",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSZPZLaDfjne1uLq6VC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22a79384-6340-4d39-af90-34c4e3300ebf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWoYFDveynvdsSkLnsoFxG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 4943,
      "cache_read_input_tokens": 10974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4943,
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

_source line 23 · 2026-05-10T19:29:19.092Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CA2oW54eePnoxoHMi2LpLD`</summary>

```json
{
  "query": "Ru-LLM DocRED 2026 document-level relation extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22a79384-6340-4d39-af90-34c4e3300ebf",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSZPZLaDfjne1uLq6VC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c94ed5f0-f52c-4331-95fe-69545a0bc4a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWoYFDveynvdsSkLnsoFxG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 4943,
      "cache_read_input_tokens": 10974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4943,
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

_source line 24 · 2026-05-10T19:29:19.589Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DDF3yBnPsTqiUUzw7mS8Qr`</summary>

```json
{
  "query": "LLM document-level relation extraction DocRED 2025 2026 new method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c94ed5f0-f52c-4331-95fe-69545a0bc4a4",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSZPZLaDfjne1uLq6VC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "943678c1-80a0-4766-8235-2e05f99bf6cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWoYFDveynvdsSkLnsoFxG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 4943,
      "cache_read_input_tokens": 10974,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4943,
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

_source line 25 · 2026-05-10T19:29:19.912Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VAptM5vhanpM9jH8ShF73w`</summary>

```json
{
  "query": "DocKS-RAG document-level relation extraction LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "943678c1-80a0-4766-8235-2e05f99bf6cd",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSZPZLaDfjne1uLq6VC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e2dbb39-5ba2-447c-9528-ee888442adf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWoYFDveynvdsSkLnsoFxG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 946,
      "cache_creation_input_tokens": 4943,
      "cache_read_input_tokens": 10974,
      "output_tokens": 527,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4943
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 946,
          "output_tokens": 527,
          "cache_read_input_tokens": 10974,
          "cache_creation_input_tokens": 4943,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4943,
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

_source line 26 · 2026-05-10T19:29:20.287Z_

<details><summary>↩ Tool result · `toolu_01KxfhWymajnkvXGQAu9GRwB`</summary>

```text
# Paper Analysis: CDER

## Full Details

**Title:** CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction

**Authors:** Khai Phan Tran, Xue Li

**Submission Date:** April 9, 2025

**Publication:** ACIIDS 2024

## Abstract Summary

The paper addresses document-level relation extraction (DocRE) by focusing on identifying entity relationships across multiple sentences. The authors note that "Evidence sentences, crucial for precise entity pair relationships identification, enhance focus on essential text segments" in improving DocRE performance.

## Key Methods

CDER employs an "attentional graph-based architecture to capture collaborative patterns" and incorporates dynamic sub-structures for robustness. The innovation centers on recognizing that semantically similar entity pairs within the same document should inform evidence retrieval collaboratively—a factor prior systems overlooked.

## Datasets & Results

The abstract references testing on "the benchmark DocRE dataset" but does not provide specific numerical performance metrics, F1 scores, or comparative results against baseline systems in the available text. The paper claims CDER "not only excels in the evidence retrieval task but also enhances overall performance of existing DocRE system," yet quantitative results are not disclosed in this preview.

## What CDER Does

CDER is an evidence retrieval framework designed to identify which sentences in a document support relation extraction between entity pairs by modeling their interdependencies through graph-based attention mechanisms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec0ae898-c936-40e6-9e87-6c40b5a4d3b2",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "5436ccde-0e7e-4a07-aeb5-908d75df69ce",
  "sourceToolAssistantUUID": "ec0ae898-c936-40e6-9e87-6c40b5a4d3b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T19:29:22.440Z_

<details><summary>↩ Tool result · `toolu_011dLze7iQkDQcxBgp1a7GAs`</summary>

```text
# Research Summary: RelPrior for Document-Level Relation Extraction

**Title:** Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction

**Authors:** Qiankun Pi, Yepeng Sun, Jicang Lu, Qinlong Fan, Ningbo Huang, Shiyu Wang

**Submission Date:** November 11, 2025

**arXiv ID:** 2511.08143

## Abstract Summary
The paper addresses performance gaps in Large Language Models when extracting relations from documents. The authors note that "LLMs still exhibit performance gaps in Document-level Relation Extraction (DocRE) as requiring fine-grained comprehension."

## The RelPrior Paradigm

RelPrior introduces a novel approach that departs from conventional "extract entities then predict relations" methodology. The framework tackles two specific challenges:

1. **Noise Reduction:** It employs "binary relation as a prior to extract and determine whether two entities are correlated," filtering irrelevant entity pairs that create interference during relation prediction.

2. **Label Matching:** Rather than directly predicting relations, it uses "predefined relation as a prior to match entities for triples extraction," circumventing errors from rigid predefined labeling constraints.

## Key Results
The research demonstrates state-of-the-art performance on two benchmarks, surpassing existing LLM-based methods. However, specific DocRED benchmark results are not detailed in the provided abstract content.

**Paper Length:** 17 pages | **License:** CC BY 4.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af7869f5-0e4b-4b92-adfc-eefddbb8baa0",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "c5685124-9345-40ab-bb18-0a0db334b03a",
  "sourceToolAssistantUUID": "af7869f5-0e4b-4b92-adfc-eefddbb8baa0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T19:29:22.489Z_

<details><summary>↩ Tool result · `toolu_013YbZnajvCx21GUH2WWKQDg`</summary>

```text
# GLiDRE: Document-Level Relation Extraction Model

## Key Details

**Title:** GLiDRE: Generalist Lightweight model for Document-level Relation Extraction

**Authors:** Robin Armingaud, Romaric Besançon

**Date:** Submitted August 1, 2025; revised October 7, 2025

**arXiv ID:** 2508.00757

## Abstract Summary

The paper addresses document-level relation extraction with a focus on scenarios where training data is limited. The abstract states: "Relation Extraction (RE) is a fundamental task in Natural Language Processing, and its document-level variant poses significant challenges, due to complex interactions between entities across sentences."

## What is GLiDRE?

GLiDRE is a compact neural model designed for document-level relation extraction that operates effectively in both supervised and few-shot learning contexts. The model targets data-constrained scenarios where traditional fully-supervised approaches may struggle.

## Performance Claims

According to the abstract, GLiDRE "outperforms existing methods in data-constrained scenarios, establishing a new state-of-the-art in few-shot document-level relation extraction."

## Note

The provided webpage does not include detailed methodology descriptions, specific dataset results, or comparative performance metrics on DocRED or other benchmarks. These details would be available in the full paper PDF or HTML versions linked on the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22a79384-6340-4d39-af90-34c4e3300ebf",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "3d433aa8-7895-4ce1-b055-1aafd1d2d99d",
  "sourceToolAssistantUUID": "22a79384-6340-4d39-af90-34c4e3300ebf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T19:29:25.749Z_

<details><summary>↩ Tool result · `toolu_01CA2oW54eePnoxoHMi2LpLD`</summary>

```text
Web search results for query: "Ru-LLM DocRED 2026 document-level relation extraction"

Links: [{"title":"Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11"},{"title":"[PDF] DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DocRED:-A-Large-Scale-Document-Level-Relation-Yao-Ye/2745fc72e1dd53d1c30f17cf05841b163c2f63c9"},{"title":"Document-level Relation Extraction with Relation Correlations - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608023006883"},{"title":"Toward Better Document-Level Relation Extraction: De-sampling and Mixture of Experts in Action | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-04549-2_12"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889"},{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/html/2403.14888v1"},{"title":"Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction","url":"https://arxiv.org/html/2511.08143"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset - ACL Anthology","url":"https://aclanthology.org/P19-1074/"},{"title":"GitHub - kracr/document-level-relation-extraction: A NeuroSymbolic AI technique for extracting relations from documents.","url":"https://github.com/kracr/document-level-relation-extraction"},{"title":"[2408.13889] LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/abs/2408.13889"}]

Based on the web search results, I found relevant information about Ru-LLM and document-level relation extraction using DocRED:

## Ru-LLM Framework

Ru-LLM is a novel framework that learns logical rules to enhance the performance of Large Language Models in Document-Level Relation Extraction (DocRE).

### Key Characteristics

Ru-LLM transforms logical rules into concise prompts to guide initial result generation, which is then subjected to a Chain-of-Thought verification process that retains only those triples satisfying all rules.

### Methodology

Ru-LLM leverages frequent pattern mining and LLM-assisted completion to obtain the candidate predicate pool, and incorporates the Monte Carlo Tree Search algorithm to efficiently search for and generate logical rules through a four-stage process: selection, expansion, simulation, and backpropagation.

### Performance

Experimental results on the three datasets DWIE, DocRED, and Re-DocRED demonstrate that Ru-LLM outperforms existing implicit reasoning models, LLM-based models, and rule-based frameworks.

### Context: DocRED Dataset

Document-level Relation Extraction (DocRE) aims to identify the relation types between entity pairs within a document. DocRED is a large-scale dataset constructed from Wikipedia and Wikidata that requires reading multiple sentences in a document to extract entities and infer their relations by synthesizing all information of the document.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c94ed5f0-f52c-4331-95fe-69545a0bc4a4",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "8cc8d2d4-4a79-44df-ab9b-210cc2cb1bd2",
  "sourceToolAssistantUUID": "c94ed5f0-f52c-4331-95fe-69545a0bc4a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T19:29:26.338Z_

<details><summary>↩ Tool result · `toolu_01VAptM5vhanpM9jH8ShF73w`</summary>

```text
Web search results for query: "DocKS-RAG document-level relation extraction LLM 2025"

Links: [{"title":"ICML Poster DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning","url":"https://icml.cc/virtual/2025/poster/45220"},{"title":"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning | OpenReview","url":"https://openreview.net/forum?id=SVl9tIADWV"},{"title":"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning","url":"https://proceedings.mlr.press/v267/xu25am.html"},{"title":"DocKS-RAG: Optimizing Document-Level Relation Extraction through","url":"https://openreview.net/pdf/96d59841526745109ad60229721708a19c60aa01.pdf"},{"title":"GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.","url":"https://github.com/liunian-Jay/Awesome-RAG"},{"title":"GitHub - HKUDS/LightRAG: [EMNLP2025] \"LightRAG: Simple and Fast Retrieval-Augmented Generation\" · GitHub","url":"https://github.com/hkuds/lightrag"},{"title":"Unified Ranking for Multiple Retrieval-Augmented Large ...","url":"https://dl.acm.org/doi/pdf/10.1145/3626772.3657733"},{"title":"AutoRE: Document-Level Relation Extraction with Large ...","url":"https://aclanthology.org/2024.acl-demos.20.pdf"},{"title":"Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11"},{"title":"Efficient Knowledge Graph Construction and Retrieval from Unstructured Text for Large-Scale RAG Systems","url":"https://arxiv.org/html/2507.03226v2"}]

Based on the search results, here's what I found about DocKS-RAG:

## Overview

DocKS-RAG is a framework for document-level relation extraction that enhances structural and semantic understanding by integrating a Document-level Knowledge Graph and a Sentence-level Semantic Retrieval-Augmented Generation mechanism.

## Problem It Addresses

Existing PLMs-based methods suffer from incorporating structural knowledge, such as entity-entity interactions, and current works struggle to infer implicit relations between entities across different sentences, which results in poor prediction.

## Key Components

The framework includes three main components:

1. **Document-level Knowledge Graph**: The framework constructs a Document-level Knowledge Graph from the observable documentation data to better capture the structural information between entities and relations.

2. **Sentence-level Semantic Retrieval-Augmented Generation**: A Sentence-level Semantic Retrieval-Augmented Generation mechanism is designed to consider the similarity in different sentences by retrieving the relevant contextual semantic information.

3. **Hybrid-Prompt Tuning**: The framework presents a hybrid-prompt tuning method on large language models (LLMs) for specific document-level RE tasks.

## Publication and Results

The paper was published in the Proceedings of the 42nd International Conference on Machine Learning, PMLR 267:69936-69949, 2025. Extensive experiments conducted on two benchmark datasets demonstrate that the proposed framework enhances all the metrics compared with state-of-the-art methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e2dbb39-5ba2-447c-9528-ee888442adf3",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "f521a3fa-3266-46cc-91b0-1af4a7a79415",
  "sourceToolAssistantUUID": "0e2dbb39-5ba2-447c-9528-ee888442adf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T19:29:27.220Z_

<details><summary>↩ Tool result · `toolu_01DDF3yBnPsTqiUUzw7mS8Qr`</summary>

```text
Web search results for query: "LLM document-level relation extraction DocRED 2025 2026 new method"

Links: [{"title":"[PDF] DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DocRED:-A-Large-Scale-Document-Level-Relation-Yao-Ye/2745fc72e1dd53d1c30f17cf05841b163c2f63c9"},{"title":"Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11"},{"title":"Leveraging Large Language Models for Document-Level Complex Relation Extraction Through Self-Verification and Tool-Assisted Relational Reasoning | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-96-9812-7_32"},{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/html/2403.14888v1"},{"title":"Dual reasoning enhanced document-level relation extraction | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-026-12099-8"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889v1"},{"title":"Toward Better Document-Level Relation Extraction: De-sampling and Mixture of Experts in Action | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-04549-2_12"},{"title":"Document-level Relation Extraction with Relation Correlations - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608023006883"},{"title":"Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction","url":"https://arxiv.org/html/2511.08143"},{"title":"(PDF) LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://www.researchgate.net/publication/383428854_LLM_with_Relation_Classifier_for_Document-Level_Relation_Extraction"}]

Based on the search results, here are recent and new methods in LLM-based document-level relation extraction on DocRED:

## Recent 2025-2026 Methods

**1. RelPrior - "Relation as a Prior" Paradigm**
A novel "Relation as a Prior" (RelPrior) paradigm for LLM-based DocRE has been proposed, which utilizes binary relation as a prior to extract and determine whether two entities are correlated, thereby filtering out irrelevant entity pairs and reducing prediction noise.

**2. Ru-LLM - Logical Rule-Constrained LLMs**
Logical Rule-constrained LLMs (Ru-LLM) is a novel framework that learns logical rules to enhance the performance of LLMs in DocRE. Ru-LLM leverages frequent pattern mining and LLM-assisted completion to obtain candidate predicates, and incorporates the Monte Carlo Tree Search algorithm to efficiently search for and generate logical rules.

**3. ToolRE - Tool-Assisted Relational Reasoning**
ToolRE is a novel framework that leverages LLMs for DocRE through self-verification and tool-assisted relational reasoning, designing three tools for entity extraction, explicit relation extraction, and complex relation extraction, with progressive refinement of extraction results.

**4. Dual Reasoning Enhanced Method**
A dual-reasoning enhanced method for DocRE integrates a two-stage graph convolutional network (GCN) and a Transformer-based module, with a graph-based reasoning module leveraging multi-head attention and entity co-occurrence guidance, while the Transformer-based reasoning module enhances interaction between entity pairs.

**5. Data Augmentation with VaeDiff-DocRE**
VaeDiff-DocRE is an end-to-end data augmentation framework for document-level relation extraction introduced in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "943678c1-80a0-4766-8235-2e05f99bf6cd",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "ee08e2a7-5334-4d5b-9faf-9981e4df1c03",
  "sourceToolAssistantUUID": "943678c1-80a0-4766-8235-2e05f99bf6cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-10T19:29:33.775Z_

Excellent. Let me now fetch more details on the most relevant papers and search for additional leads.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee08e2a7-5334-4d5b-9faf-9981e4df1c03",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSabyUqNFQWU4nvbUau",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf88f054-c654-4215-99a6-469dfa90107b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AZe1tqFqyPzXgsq4S8dGw2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 971,
      "cache_creation_input_tokens": 4660,
      "cache_read_input_tokens": 15917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4660,
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

_source line 33 · 2026-05-10T19:29:36.882Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015LKeCENByqjkS7dcPGnADK`</summary>

```json
{
  "url": "https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11",
  "prompt": "Extract full details about Ru-LLM: authors, venue/year, method details, datasets, specific numerical results on DocRED and Re-DocRED (F1 scores), comparison with baselines. What exactly are the logical rules and how does MCTS work here?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf88f054-c654-4215-99a6-469dfa90107b",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSabyUqNFQWU4nvbUau",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab5b1d4c-ab1b-4c9a-bf84-17b17e6bc34a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AZe1tqFqyPzXgsq4S8dGw2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 971,
      "cache_creation_input_tokens": 4660,
      "cache_read_input_tokens": 15917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4660,
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

### Tool result

_source line 34 · 2026-05-10T19:29:37.413Z_

<details><summary>↩ Tool result · reported error · `toolu_015LKeCENByqjkS7dcPGnADK`</summary>

```text
Request failed with status code 303
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab5b1d4c-ab1b-4c9a-bf84-17b17e6bc34a",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "a2fc816f-778c-4efe-a8ff-a4f904ca7ffc",
  "toolUseResult": "Error: Request failed with status code 303",
  "sourceToolAssistantUUID": "ab5b1d4c-ab1b-4c9a-bf84-17b17e6bc34a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-10T19:29:37.710Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XresNmtoMopw5PE6knDAnJ`</summary>

```json
{
  "url": "https://openreview.net/forum?id=SVl9tIADWV",
  "prompt": "Extract full details about DocKS-RAG: authors, venue/year, method details, specific numerical results on DocRED (F1 scores), comparison with baselines. What LLM do they use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2fc816f-778c-4efe-a8ff-a4f904ca7ffc",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSabyUqNFQWU4nvbUau",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f93ae419-2a06-4ed1-a599-2805b4fac3f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AZe1tqFqyPzXgsq4S8dGw2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 971,
      "cache_creation_input_tokens": 4660,
      "cache_read_input_tokens": 15917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4660,
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

_source line 36 · 2026-05-10T19:29:39.161Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EaWGX6ww1XLzWFwoZf4pz2`</summary>

```json
{
  "query": "ToolRE \"tool-assisted relational reasoning\" document-level relation extraction LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f93ae419-2a06-4ed1-a599-2805b4fac3f5",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSabyUqNFQWU4nvbUau",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c73edd25-6c8d-44fd-8dff-ccb041173d87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AZe1tqFqyPzXgsq4S8dGw2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 971,
      "cache_creation_input_tokens": 4660,
      "cache_read_input_tokens": 15917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4660,
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

_source line 37 · 2026-05-10T19:29:39.663Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TRKTZUV14WS9etswFs2qtQ`</summary>

```json
{
  "query": "\"joint evidence extraction\" \"relation extraction\" document-level LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c73edd25-6c8d-44fd-8dff-ccb041173d87",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSabyUqNFQWU4nvbUau",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "574377b5-7ea6-413a-9e1f-cba295a25b3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AZe1tqFqyPzXgsq4S8dGw2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 971,
      "cache_creation_input_tokens": 4660,
      "cache_read_input_tokens": 15917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4660,
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

_source line 38 · 2026-05-10T19:29:40.251Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HvcKactBRbkg5x5Na7z9G3`</summary>

```json
{
  "query": "reinforcement learning GRPO PPO DPO \"information extraction\" \"relation extraction\" document 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "574377b5-7ea6-413a-9e1f-cba295a25b3f",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSabyUqNFQWU4nvbUau",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b063f09-34d5-455a-a1f3-0883c7cf05be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AZe1tqFqyPzXgsq4S8dGw2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 971,
      "cache_creation_input_tokens": 4660,
      "cache_read_input_tokens": 15917,
      "output_tokens": 470,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4660
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 971,
          "output_tokens": 470,
          "cache_read_input_tokens": 15917,
          "cache_creation_input_tokens": 4660,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4660,
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

_source line 39 · 2026-05-10T19:29:41.563Z_

<details><summary>↩ Tool result · `toolu_01XresNmtoMopw5PE6knDAnJ`</summary>

```text
# DocKS-RAG Paper Details

**Authors:** Xiaolong Xu, Yibo Zhou, Haolong Xiang, Xiaoyong Li, Xuyun Zhang, Lianyong Qi, Wanchun Dou

**Venue & Year:** ICML 2025 (published May 1, 2025)

**Submission Number:** 9793

## Method Overview

The framework incorporates three main components:

1. **Document-level Knowledge Graph** - Constructed from source documents to capture structural relationships between entities and relations

2. **Sentence-level Semantic Retrieval-Augmented Generation** - Designed to handle cross-sentence implicit relations by retrieving relevant contextual information based on semantic similarity

3. **Hybrid-Prompt Tuning on LLMs** - Applied to large language models for the specific task

## Results & Baselines

The abstract states the framework "enhances all the metrics compared with state-of-the-art methods" on two benchmark datasets, but **the webpage provided does not include specific numerical results, F1 scores on DocRED, or details about which LLM is used**.

To obtain those specifics, you would need to access the full PDF or paper, which is available for download on the OpenReview page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f93ae419-2a06-4ed1-a599-2805b4fac3f5",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "36390013-e577-4ee1-8d3d-032e27eb8a91",
  "sourceToolAssistantUUID": "f93ae419-2a06-4ed1-a599-2805b4fac3f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T19:29:44.799Z_

<details><summary>↩ Tool result · `toolu_01EaWGX6ww1XLzWFwoZf4pz2`</summary>

```text
Web search results for query: "ToolRE "tool-assisted relational reasoning" document-level relation extraction LLM 2025 2026"

Links: [{"title":"Leveraging Large Language Models for Document-Level Complex Relation Extraction Through Self-Verification and Tool-Assisted Relational Reasoning | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-96-9812-7_32"},{"title":"Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11"},{"title":"Document-level Relation Extraction with Relation Correlations - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608023006883"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889v2"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction | OpenReview","url":"https://openreview.net/forum?id=SOWcC2cCMT"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://openreview.net/pdf?id=SOWcC2cCMT"},{"title":"(PDF) LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://www.researchgate.net/publication/383428854_LLM_with_Relation_Classifier_for_Document-Level_Relation_Extraction"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/html/2403.14888v1"},{"title":"a Refiner with Task Distribution and Probability Fusion","url":"https://aclanthology.org/2025.naacl-long.319.pdf"}]

Based on the search results, I found relevant information about ToolRE:

ToolRE is a novel framework that leverages LLMs for DocRE through self-verification and tool-assisted relational reasoning. 

The framework designs three tools for entity extraction, explicit relation extraction, and complex relation extraction, and progressively refines the extraction results by allowing the agentic user to select tools.

The approach adopts a tuning-free strategy that utilizes LLMs to reason over trigger words and relation through reasoning. Additionally, the method implements backward verification to obtain interpretable relation verification scores, thereby enhancing the performance of relation extraction.

Experimental results on the DocRE benchmark demonstrate that the method significantly outperforms baseline LLM-based DocRE models.

The paper was published in 2025 in the ICIC 2025 conference proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c73edd25-6c8d-44fd-8dff-ccb041173d87",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "cf00ef52-e954-415b-b0dd-d4070080b7ab",
  "sourceToolAssistantUUID": "c73edd25-6c8d-44fd-8dff-ccb041173d87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T19:29:47.181Z_

<details><summary>↩ Tool result · `toolu_01TRKTZUV14WS9etswFs2qtQ`</summary>

```text
Web search results for query: ""joint evidence extraction" "relation extraction" document-level LLM 2025 2026"

Links: [{"title":"Leveraging Large Language Models for Document-Level Complex Relation Extraction Through Self-Verification and Tool-Assisted Relational Reasoning | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-96-9812-7_32"},{"title":"Structured information extraction from scientific text with large language models | Nature Communications","url":"https://www.nature.com/articles/s41467-024-45563-x"},{"title":"Information Extraction from Visually Rich Documents using ...","url":"https://aclanthology.org/2025.acl-long.844.pdf"},{"title":"Large language model augmented joint learning framework for entity-relation extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1568494625014073"},{"title":"Few-Shot Relation Extraction via Two-Stage Knowledge- ...","url":"https://www.ijcai.org/proceedings/2025/0897.pdf"},{"title":"A case study for automated attribute extraction from legal documents using large language models | Artificial Intelligence and Law | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10506-024-09425-7"},{"title":"Document-level Relation Extraction with Relation Correlations - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608023006883"},{"title":"ICML Poster DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning","url":"https://icml.cc/virtual/2025/poster/45220"},{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/html/2403.14888v1"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"}]

Based on the web search results, here are the key findings related to joint evidence extraction, relation extraction, and document-level LLM approaches in 2025-2026:

## Recent Work on Document-Level Relation Extraction with LLMs

Large language models (LLMs) create a new paradigm for Document-level Relation Extraction (DocRE). ToolRE is a novel framework that leverages LLMs for DocRE through self-verification and tool-assisted relational reasoning, designing three tools for entity extraction, explicit relation extraction, and complex relation extraction.

## Joint Extraction Approaches

A simple approach to joint named entity recognition and relation extraction demonstrates how pretrained large language models (GPT-3, Llama-2) can be fine-tuned to extract useful records of complex scientific knowledge. Additionally, Reamend is a novel LLM augmented joint learning framework for entity-relation extraction that is capable of simultaneously recognizing potential entities and the corresponding relations from the text content, with entity-relation amendment introduced to eliminate redundant triplets.

## Challenges and Solutions

Existing LLM-based methods still face challenges, including inadequate utilization of reasoning capabilities and potential omission of intricate implicit relation due to manually designed joint extraction processes. Document-level relation extraction aims to extract comprehensive correlations between entities and relations from documents, but current works struggle to infer implicit relations between entities across different sentences; DocKS-RAG introduces extra structural knowledge and semantic information to further enhance performance.

The search results show significant recent research activity in this area, with multiple approaches being developed in 2025-2026 to improve document-level information extraction using LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "574377b5-7ea6-413a-9e1f-cba295a25b3f",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "644688af-5bd2-4664-95c5-b5aea304d7c9",
  "sourceToolAssistantUUID": "574377b5-7ea6-413a-9e1f-cba295a25b3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-10T19:29:47.626Z_

<details><summary>↩ Tool result · `toolu_01HvcKactBRbkg5x5Na7z9G3`</summary>

```text
Web search results for query: "reinforcement learning GRPO PPO DPO "information extraction" "relation extraction" document 2025 2026"

Links: [{"title":"A Guide to Reinforcement Learning Post-Training for LLMs: PPO, DPO, GRPO, and Beyond","url":"https://huggingface.co/blog/karina-zadorozhny/guide-to-llm-post-training-algorithms"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"Reinforcement Learning (RL) Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide"},{"title":"A vision researcher’s guide to some RL stuff: PPO & GRPO - Yuge (Jimmy) Shi","url":"https://yugeten.github.io/posts/2025/01/ppogrpo/"},{"title":"PPO, DPO & GRPO: Reinforcement Learning Techniques for Training LLMs | by Mandeep Singh | Medium","url":"https://medium.com/@mandeep0405/ppo-dpo-grpo-reinforcement-learning-techniques-for-training-llms-193459ffc14e"},{"title":"It Takes Two: Your GRPO Is Secretly DPO","url":"https://arxiv.org/pdf/2510.00977"},{"title":"The State of Reinforcement Learning for LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"Published as a conference paper at ICLR 2026 GROUP-RELATIVE REINFORCE","url":"https://arxiv.org/pdf/2509.24203"},{"title":"Self-Guided Plan Extraction for Instruction-Following Tasks with Goal-Conditional Reinforcement Learning","url":"https://arxiv.org/html/2604.20601"}]

I've performed the web search on reinforcement learning methods (GRPO, PPO, DPO) in relation to information/relation extraction and document processing from 2025-2026. Here's what I found:

## Key Findings:

**Reinforcement Learning Algorithms Overview:**

GRPO (Group Relative Policy Optimization) is an RL algorithm that samples multiple responses per prompt and computes advantages by comparing them within the group. It eliminates the need for a separate critic model, reducing memory and compute costs while matching or exceeding PPO performance.

DPO (Rafailov et al., 2023) doesn't use a separate Reward Model neural network. Instead, it extracts the optimal reward directly from the preference data.

**Recent Post-Training Framework (2025-2026):**

Post-training now has three distinct stages after pretraining, each solving a different problem. The order matters. Post-training (SFT, Preference Optimization, RL) now accounts for the majority of a model's usable capability.

**Notable Extensions:**

Recent work, A Comedy of Estimators (Shah et al., 2026) and On a few pitfalls in KL divergence gradient estimation (Tang & Munos, 2025), has shown how the most popular methods, including those used in popular open-sourced libraries, often calculate the wrong gradients.

However, the search results primarily focus on these algorithms for general LLM post-training and reasoning tasks rather than specifically for information extraction or relation extraction on documents. The results don't contain specific applications of these methods to document-based IE/RE tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b063f09-34d5-455a-a1f3-0883c7cf05be",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "95bb73b3-98b9-470a-b5ca-84d5193099aa",
  "sourceToolAssistantUUID": "4b063f09-34d5-455a-a1f3-0883c7cf05be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-10T19:29:51.154Z_

Let me dig deeper into a few more specific areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95bb73b3-98b9-470a-b5ca-84d5193099aa",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSc7CfsRMym5rUR8xMo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3221572a-2436-4b70-9a01-696eebde2fb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGrBGEchn5UpeBZGY3e9o1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4486,
      "cache_read_input_tokens": 20577,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4486,
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

_source line 44 · 2026-05-10T19:29:54.214Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KpFhZw5YEzjt7vsJWaTFM9`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.06529",
  "prompt": "Extract the detailed experimental results from CDER: specific F1 scores on DocRED (dev and test), evidence retrieval F1 scores, comparison with baselines like ATLOP, DocuNet, KD-DocRE, DREEAM, etc. Also extract information about which backbone encoder they use."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3221572a-2436-4b70-9a01-696eebde2fb4",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSc7CfsRMym5rUR8xMo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d95a465c-61ee-4b64-a525-b3940928ba56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGrBGEchn5UpeBZGY3e9o1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4486,
      "cache_read_input_tokens": 20577,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4486,
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

_source line 45 · 2026-05-10T19:29:56.636Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FhCYRKqFK8BLJY5X1qFvqM`</summary>

```json
{
  "url": "https://arxiv.org/html/2511.08143",
  "prompt": "Extract the detailed experimental results: specific F1 scores on DocRED and Re-DocRED, comparison with other LLM-based methods, which base LLM they use, and the complete methodology of the RelPrior paradigm. Include any numbers and tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d95a465c-61ee-4b64-a525-b3940928ba56",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSc7CfsRMym5rUR8xMo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0eb7b1f7-e67b-4c06-86d9-853b5b49727f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGrBGEchn5UpeBZGY3e9o1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4486,
      "cache_read_input_tokens": 20577,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4486,
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

_source line 46 · 2026-05-10T19:29:57.321Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ktd1wDKEGLXaNkGrApwvFr`</summary>

```json
{
  "query": "RLVR reinforcement learning \"relation extraction\" OR \"information extraction\" document-level 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0eb7b1f7-e67b-4c06-86d9-853b5b49727f",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSc7CfsRMym5rUR8xMo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7268b35d-25d6-460e-8caa-6f4b4d1c6592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGrBGEchn5UpeBZGY3e9o1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4486,
      "cache_read_input_tokens": 20577,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4486,
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

_source line 47 · 2026-05-10T19:29:58.337Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G2mAU5H4g75d2kG82DgegD`</summary>

```json
{
  "query": "\"KnowRA\" document-level relation extraction 2025 arxiv knowledge retrieval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7268b35d-25d6-460e-8caa-6f4b4d1c6592",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSc7CfsRMym5rUR8xMo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd08ed24-3cb6-499e-bed0-bfcc2f8a8ca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGrBGEchn5UpeBZGY3e9o1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4486,
      "cache_read_input_tokens": 20577,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4486,
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

_source line 48 · 2026-05-10T19:29:58.497Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CPtwU74kcGTB7z6LfpYSrt`</summary>

```json
{
  "query": "COMM \"concentrated margin maximization\" DocRED 2025 results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd08ed24-3cb6-499e-bed0-bfcc2f8a8ca1",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSc7CfsRMym5rUR8xMo",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe132539-1e3b-4909-b8ee-3e9bc14ffa9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGrBGEchn5UpeBZGY3e9o1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4486,
      "cache_read_input_tokens": 20577,
      "output_tokens": 449,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4486
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 449,
          "cache_read_input_tokens": 20577,
          "cache_creation_input_tokens": 4486,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4486,
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

_source line 49 · 2026-05-10T19:30:00.077Z_

<details><summary>↩ Tool result · `toolu_01KpFhZw5YEzjt7vsJWaTFM9`</summary>

```text
# CDER Experimental Results Summary

## Backbone Encoder
CDER utilizes "cased BERTbasebase{}\_{\\textnormal{base}}" as its document encoder for all experiments.

## DocRED Development Set Results
On the development set, CDER achieved:
- **F1 Score**: 62.32±0.07 (with EIDER baseline)
- **Ign F1**: 60.31±0.10
- **Evidence F1**: 52.92±0.11

When integrated with DREEAM baseline:
- **F1**: 62.42±0.02
- **Ign F1**: 60.42±0.03
- **Evidence F1**: 52.86±0.10

## DocRED Test Set Results
Test performance showed:
- **F1**: 62.33 (EIDER+CDER) / 62.45 (DREEAM+CDER)
- **Ign F1**: 59.98 / 60.22
- **Evidence F1**: 52.89 / 53.03

## Evidence Retrieval Performance
For positive entity pairs on development data:
- **Precision**: 86.84±0.31
- **Recall**: 82.75±0.35
- **Pos Evidence F1**: 84.75±0.05

This represents improvements of 6.6 points over EIDER and 0.11 points over DREEAM.

## Baseline Comparisons
CDER outperformed established methods like ATLOP (61.09 F1), DocuNet (61.83 F1), and prior evidence retrieval systems (EIDER: 49.92 Evi F1, DREEAM: 52.78 Evi F1).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d95a465c-61ee-4b64-a525-b3940928ba56",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "5d88b20a-6b61-46db-afbc-38f95e84a89b",
  "sourceToolAssistantUUID": "d95a465c-61ee-4b64-a525-b3940928ba56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-10T19:30:03.265Z_

<details><summary>↩ Tool result · `toolu_01FhCYRKqFK8BLJY5X1qFvqM`</summary>

```text
# RelPrior: Document-Level Relation Extraction Results

## Experimental Performance

**DocRED Dataset Results (Table 2):**
- RelPrior with LLaMA3-8B achieved 47.82 F1 and 47.70 Ign F1 on dev set
- Test set performance: 48.34 F1 and 46.41 Ign F1
- Improvements over AutoRE (prior LLM-based SOTA): +2.06% F1 (dev), +2.38% F1 (test)

**RE-DocRED Dataset Results:**
- Dev set: 55.94 F1 and 55.50 Ign F1
- Test set: 54.80 F1 and 54.53 Ign F1

## LLM Base Models Tested

The research evaluated RelPrior across five open-source models:
- DeepSeek-R1-Distill-LLaMA3-8B
- Qwen2.5-7B
- LLaMA2-13B-Chat
- LLaMA3.1-8B
- LLaMA3-8B (best performer)

## RelPrior Methodology: Two-Module Architecture

**Module 1 - Entity Pairs Filtering (EPF):**
Converts relation extraction into binary classification. The system determines whether relationships exist between entity pairs using fine-tuned LLMs trained on both positive and negative samples. This reduces noise from unrelated entity pairs and formalized as: "determine whether there is a relationship between them and output the set of entity pairs that have a relationship."

**Module 2 - Relation Matching (RM):**
Uses identified relations as constraints to discover head and tail entities. The process involves two sub-tasks: inferring possible head entities and inferring tail entities for each predicted relation, then merging candidates sharing identical relations to form new triples.

## Ablation Study Results

Removing EPF caused performance drops of 18-21% F1, while removing RM reduced performance by approximately 4-5% F1, demonstrating both components' necessity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0eb7b1f7-e67b-4c06-86d9-853b5b49727f",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "a9915eeb-63c4-43fa-8ee7-07ca1335529f",
  "sourceToolAssistantUUID": "0eb7b1f7-e67b-4c06-86d9-853b5b49727f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-10T19:30:04.933Z_

<details><summary>↩ Tool result · `toolu_01CPtwU74kcGTB7z6LfpYSrt`</summary>

```text
Web search results for query: "COMM "concentrated margin maximization" DocRED 2025 results"

Links: [{"title":"COMM: Concentrated Margin Maximization for Robust Document-Level Relation Extraction","url":"https://arxiv.org/html/2503.13885"},{"title":"COMM: Concentrated Margin Maximization for Robust Document-Level Relation Extraction | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34556"},{"title":"COMM: Concentrated Margin Maximization for Robust Document-Level","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34556/36711"},{"title":"[2503.13885] COMM:Concentrated Margin Maximization for Robust Document-Level Relation Extraction","url":"https://arxiv.org/abs/2503.13885"},{"title":"© 2024 CME Group. All rights reserved. CME GROUP PUBLIC","url":"https://www.cftc.gov/media/10226/AAC121423presentation_SuzanneSprague/download"},{"title":"Performance Bond Requirements - Metal Margin - Effective December 29, 2025 - CME Group","url":"https://www.cmegroup.com/notices/clearing/2025/25-393.html"},{"title":"CME updates its margining methodology for precious Metals","url":"https://energynews.oedigital.com/mineral-resources/2026/01/13/cme-updates-its-margining-methodology-for-precious-metals"},{"title":"CMOC 2025 Annual Report: Record Performance and ...","url":"https://www.linkedin.com/posts/cmocinternational_cmoc-annualresults-responsiblemining-activity-7443287550305275904-d6FG"},{"title":"© 2025 CME Group. All rights reserved. CME GROUP PUBLIC","url":"https://www.cmegroup.com/trading/interest-rates/cleared-otc/files/portfolio-margining-capital-efficiencies.pdf"},{"title":"Are Operating Margin, Markup and Unit Margin Good for Profit? An Approach Based on Microeconomic Theory - Mesnard - 2025 - Managerial and Decision Economics - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/mde.4535?af=R"}]

Based on the search results, I found information about COMM (Concentrated Margin Maximization) for Document-Level Relation Extraction:

## Overview

COMM is a robust framework for document relation extraction (DocRE). COMM consists of two main components: instance-aware reasoning augmentation (IARA) and margin-centered optimization.

## Key Components

The instance-aware reasoning augmentation stage utilizes an existing relational encoding model to capture and encode complex interactions between mentions, entities, sentences, and the document, deriving contextualized relational feature representations.

The Concentrated Margin Maximization (CMM) strategy adaptively adjusts the margins between relation logits and the decision boundary to reduce the influence of abundant negative samples.

## 2025 Results

The experimental results underscore the robustness of COMM, showcasing substantial performance improvements, particularly in handling low-quality data, with enhancements exceeding 10%. The versatility and effectiveness of COMM demonstrate its robustness when trained on low-quality data, achieving over 10% performance gains.

The research appears to have been published as part of the AAAI Conference on Artificial Intelligence in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe132539-1e3b-4909-b8ee-3e9bc14ffa9d",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "5e7d7533-ce95-44f3-9a12-75fef5ef6e20",
  "sourceToolAssistantUUID": "fe132539-1e3b-4909-b8ee-3e9bc14ffa9d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-10T19:30:04.948Z_

<details><summary>↩ Tool result · `toolu_01Ktd1wDKEGLXaNkGrApwvFr`</summary>

```text
Web search results for query: "RLVR reinforcement learning "relation extraction" OR "information extraction" document-level 2025 2026"

Links: [{"title":"longrlvr: long-context reinforcement learning re-","url":"https://openreview.net/pdf?id=omVhYvyTPJ"},{"title":"GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-RLVR"},{"title":"The Power of RLVR: Training a Leading SQL Reasoning Model on Databricks | Databricks Blog","url":"https://www.databricks.com/blog/power-rlvr-training-leading-sql-reasoning-model-databricks"},{"title":"Chart-RL: Generalized Chart Comprehension via Reinforcement Learning with Verifiable Rewards","url":"https://arxiv.org/html/2603.06958"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2601.18533"},{"title":"GitHub - real-absolute-AI/LongRLVR: [ICLR 2026] LongRLVR: Long-Context Reinforcement Learning Requires Verifiable Context Rewards. · GitHub","url":"https://github.com/real-absolute-AI/LongRLVR"},{"title":"RLVR Beyond Math and Code: The Verifier Problem Nobody Has Solved | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/rlvr-beyond-math-code/"},{"title":"RLVR-World: Training World Models with Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=jpiSagi8aV"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"}]

Based on the web search results, I found several relevant papers and resources about RLVR (Reinforcement Learning with Verifiable Rewards), though I did not find papers specifically focusing on relation extraction or information extraction at the document level in 2025-2026. Here's what I found:

## Key RLVR Resources and Applications:

**General RLVR Framework:**
RLVR is a rapidly emerging paradigm that aligns both LLMs and other agents through objective, externally verifiable signals.

**Document-Level Information Extraction:**
The closest match to your query is that RLVR is being applied to information extraction (IE) from documents, with information extraction tasks having verifiable rewards since correctness can be checked directly, enabling reinforcement learning without a learned reward model.

**Recent RLVR Extensions (2025-2026):**

1. **LongRLVR**: RLVR has advanced LLM reasoning capabilities, but falters in long-context scenarios; LongRLVR addresses this by augmenting sparse answer rewards with dense, verifiable context rewards that incentivize correct evidence selection.

2. **RLVRR**: RLVRR extends RLVR to open-ended generation by extracting an ordered sequence of verifiable linguistic signals from high-quality references, transforming single verification into a reward chain.

3. **Chart Understanding**: Chart-RL leverages group relative policy optimization with chart-aligned accuracy and format rewards to train VLMs with robust reasoning capabilities.

**Future Directions:**
RLVR is expected to more widely expand into other domains beyond math and coding.

I did not find papers specifically titled with the exact combination of "RLVR," "relation extraction," and "document-level" for 2025-2026 in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7268b35d-25d6-460e-8caa-6f4b4d1c6592",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "714e0a41-902c-4fa5-b858-727169740f1b",
  "sourceToolAssistantUUID": "7268b35d-25d6-460e-8caa-6f4b4d1c6592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-10T19:30:05.453Z_

<details><summary>↩ Tool result · `toolu_01G2mAU5H4g75d2kG82DgegD`</summary>

```text
Web search results for query: ""KnowRA" document-level relation extraction 2025 arxiv knowledge retrieval"

Links: [{"title":"[2501.00571] KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction with Comprehensive Reasoning Abilities","url":"https://arxiv.org/abs/2501.00571"},{"title":"KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction with Comprehensive Reasoning Abilities","url":"https://arxiv.org/html/2501.00571v3"},{"title":"KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction with Comprehensive Reasoning Abilities - Paper Detail","url":"https://deeplearn.org/arxiv/600676/knowra:-knowledge-retrieval-augmented-method-for-document-level-relation-extraction-with-comprehensive-reasoning-abilities"},{"title":"KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction with Comprehensive Reasoning Abilities | Article Information | J-GLOBAL","url":"https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202502219727728986"},{"title":"(PDF) KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction with Comprehensive Reasoning Abilities","url":"https://www.researchgate.net/publication/387670823_KnowRA_Knowledge_Retrieval_Augmented_Method_for_Document-level_Relation_Extraction_with_Comprehensive_Reasoning_Abilities"},{"title":"dblp: KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction with Comprehensive Reasoning Abilities.","url":"https://dblp.org/rec/conf/ijcai/MaiWGW025.html"},{"title":"KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction with Comprehensive Reasoning Abilities | IJCAI","url":"https://www.ijcai.org/proceedings/2025/910"},{"title":"[2211.14470] Towards Better Document-level Relation Extraction via Iterative Inference","url":"https://arxiv.org/abs/2211.14470"},{"title":"Augmenting Document-level Relation Extraction with Efficient Multi-Supervision","url":"https://arxiv.org/html/2407.01026"},{"title":"[2203.10900] Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation","url":"https://arxiv.org/abs/2203.10900"}]

Based on the search results, I found detailed information about KnowRA:

## KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction

Document-level relation extraction (Doc-RE) aims to extract relations between entities across multiple sentences. Doc-RE requires more comprehensive reasoning abilities like humans, involving complex cross-sentence interactions between entities, contexts, and external general knowledge, compared to the sentence-level RE.

### The Problem

Most existing Doc-RE methods focus on optimizing single reasoning ability, but lack the ability to utilize external knowledge for comprehensive reasoning on long documents.

### The Solution

KnowRA, a knowledge retrieval augmented method, was proposed with comprehensive reasoning to autonomously determine whether to accept external knowledge to assist DocRE. The approach includes several key components:

1. A document graph was constructed for semantic encoding and a co-reference resolution model was integrated to augment the co-reference reasoning ability.

2. The document graph was expanded into a document knowledge graph by retrieving the external knowledge base for common-sense reasoning and a novel knowledge filtration method was presented to filter out irrelevant knowledge.

3. An axis attention mechanism was proposed to build direct and indirect associations with intermediary entities for achieving cross-sentence logical reasoning.

### Results

On datasets Re-DocRED and DWIE, KnowRA surpassed the existing SOTA model, JMRL-DREEAM, by 0.28 and 1.13 in F1 score, respectively.

The paper was published on arXiv (2501.00571) and has been accepted to IJCAI 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd08ed24-3cb6-499e-bed0-bfcc2f8a8ca1",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "a363187f-7df0-4897-b021-977250c8254f",
  "sourceToolAssistantUUID": "cd08ed24-3cb6-499e-bed0-bfcc2f8a8ca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-10T19:30:09.431Z_

Good progress. Let me fetch more detailed results and search for the remaining areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a363187f-7df0-4897-b021-977250c8254f",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSdRSZALcab4P3T68ee",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2dd3aec0-7bf8-449d-88a8-e06cac0f218a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwCZcEssQduA1iyW3NRPf7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 919,
      "cache_creation_input_tokens": 3594,
      "cache_read_input_tokens": 25063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3594,
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

_source line 55 · 2026-05-10T19:30:12.619Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015r9yyfBq9WZtxckWXzdjwf`</summary>

```json
{
  "url": "https://arxiv.org/html/2503.13885",
  "prompt": "Extract detailed experimental results from COMM: specific F1 scores on DocRED dev and test set, comparison with baselines (ATLOP, DocuNet, DREEAM, etc.), results on Re-DocRED if available. Also extract information about BERT-base and RoBERTa-large results separately."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dd3aec0-7bf8-449d-88a8-e06cac0f218a",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSdRSZALcab4P3T68ee",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d564646a-05dd-41ad-a624-30921a97765b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwCZcEssQduA1iyW3NRPf7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 919,
      "cache_creation_input_tokens": 3594,
      "cache_read_input_tokens": 25063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3594,
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

_source line 56 · 2026-05-10T19:30:14.744Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VCttnhFqvbjBksAz67C1gW`</summary>

```json
{
  "url": "https://arxiv.org/abs/2501.00571",
  "prompt": "Extract specific experimental results: F1 scores on DocRED, Re-DocRED, and DWIE. What encoders are used? Comparison numbers vs DREEAM, JMRL, and other baselines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d564646a-05dd-41ad-a624-30921a97765b",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSdRSZALcab4P3T68ee",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00698f09-8487-4ad0-a923-c8b27e8013ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwCZcEssQduA1iyW3NRPf7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 919,
      "cache_creation_input_tokens": 3594,
      "cache_read_input_tokens": 25063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3594,
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

_source line 57 · 2026-05-10T19:30:15.739Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rp8wcvxrXhGHbHDJZBK4CD`</summary>

```json
{
  "query": "DPO RLHF \"entity extraction\" OR \"relation extraction\" OR \"information extraction\" fine-tuning LLM 2025 2026 document"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00698f09-8487-4ad0-a923-c8b27e8013ba",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSdRSZALcab4P3T68ee",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99b5ee48-5ed5-465d-b186-b79d96d44c2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwCZcEssQduA1iyW3NRPf7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 919,
      "cache_creation_input_tokens": 3594,
      "cache_read_input_tokens": 25063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3594,
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

_source line 58 · 2026-05-10T19:30:16.605Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BitoX3ioRZPTtgYEzCimnF`</summary>

```json
{
  "query": "\"GREP\" \"global relations entity pair\" document-level relation extraction ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99b5ee48-5ed5-465d-b186-b79d96d44c2e",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSdRSZALcab4P3T68ee",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f26f9989-d1d1-4442-aa30-934635bf0d1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwCZcEssQduA1iyW3NRPf7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 919,
      "cache_creation_input_tokens": 3594,
      "cache_read_input_tokens": 25063,
      "output_tokens": 408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3594
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 919,
          "output_tokens": 408,
          "cache_read_input_tokens": 25063,
          "cache_creation_input_tokens": 3594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3594,
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

_source line 59 · 2026-05-10T19:30:17.168Z_

<details><summary>↩ Tool result · `toolu_015r9yyfBq9WZtxckWXzdjwf`</summary>

```text
# COMM Experimental Results Summary

## DocRED-Mixed Results (Low-Quality Data)

The framework demonstrates substantial improvements when trained on the lower-quality DocRED dataset:

**BERT-ATLOP:**
- Baseline dev F1: 50.5% → COMM: 61.8% (+11.3)
- Test F1: 50.1% → 62.3% (+12.2)

**RoBERTa-ATLOP:**
- Baseline dev F1: 51.8% → COMM: 63.9% (+12.1)
- Test F1: 50.6% → 63.5% (+12.9)

**BERT-DocuNet:**
- Test F1: 46.9% → 60.6% (+13.7)

**RoBERTa-DocuNet:**
- Test F1: 48.7% → 62.1% (+13.4)

## Re-DocRED Results (High-Quality Data)

Performance gains are more modest with cleaner annotations:

**BERT-ATLOP:**
- Test F1: 72.9% → 76.1% (+3.2)

**RoBERTa-ATLOP:**
- Test F1: 77.5% → 80.8% (+3.3)

## Key Finding

The paper states: "achieving >10% performance gains" specifically when trained on low-quality data, highlighting COMM's robustness advantage for challenging datasets with annotation errors and class imbalance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d564646a-05dd-41ad-a624-30921a97765b",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "c9bcb04e-6feb-4ed5-9631-17738fe68bca",
  "sourceToolAssistantUUID": "d564646a-05dd-41ad-a624-30921a97765b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-10T19:30:18.980Z_

<details><summary>↩ Tool result · `toolu_01VCttnhFqvbjBksAz67C1gW`</summary>

```text
# Experimental Results Not Available in Provided Content

I cannot extract the specific experimental results you requested because the web page content provided contains only the abstract and metadata from the arXiv paper, not the full paper with results sections.

The abstract mentions that "Extensive experiments conducted on two datasets verified the effectiveness of our method," but does not provide:

- F1 scores for DocRED, Re-DocRED, or DWIE
- Specific encoder details
- Numerical comparisons with DREEAM, JMRL, or other baselines

**To obtain this information**, you would need to:
1. Access the full PDF via the "[View PDF](/pdf/2501.00571)" link
2. Check the HTML version at the provided experimental link
3. Review the TeX source materials

The abstract does note that the work uses "a document graph for semantic encoding and integrated the co-reference resolution model," but complete technical specifications and comparative benchmark results are not included in this metadata page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00698f09-8487-4ad0-a923-c8b27e8013ba",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "8f9835dd-4029-444b-b962-60e603d5f776",
  "sourceToolAssistantUUID": "00698f09-8487-4ad0-a923-c8b27e8013ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-10T19:30:22.070Z_

<details><summary>↩ Tool result · `toolu_01BitoX3ioRZPTtgYEzCimnF`</summary>

```text
Web search results for query: ""GREP" "global relations entity pair" document-level relation extraction ACL 2025"

Links: [{"title":"Document-Level Relation Extraction with Global ...","url":"https://aclanthology.org/2025.findings-acl.1002.pdf"},{"title":"Document-Level Relation Extraction with Global Relations and Entity Pair Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1002/"},{"title":"Document-level relation extraction with global and path dependencies - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950705124001801"},{"title":"Entity Pair-guided Relation Summarization and Retrieval in LLMs for Document-level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.224/"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"Taxonomy-Driven Knowledge Graph Construction for ...","url":"https://aclanthology.org/2025.findings-acl.223.pdf"},{"title":"[2201.04826] Document-level Relation Extraction with Context Guided Mention Integration and Inter-pair Reasoning","url":"https://arxiv.org/abs/2201.04826"},{"title":"Multi-Relation Extraction in Entity Pairs using Global Context","url":"https://arxiv.org/html/2507.22926"},{"title":"Document-level relation extraction via dual attention fusion and dynamic asymmetric loss | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-024-01632-8"},{"title":"Joint Entity and Relation Extraction Based on Bidirectional Update and","url":"https://aclanthology.org/2024.ccl-1.85.pdf"}]

Based on the search results, I found detailed information about GREP:

## GREP: Document-Level Relation Extraction Framework

GREP is a framework with the acronym standing for "global relations and entity pair reasoning" designed for document-level relation extraction (DocRE) tasks.

### Key Features

GREP leverages the global interdependencies between entity pairs to capture fine-grained interactions and perform multi reasoning at the entity pair level. Additionally, GREP for the first time proposes an auxiliary task that predicts all possible relations in advance that exist in a document, which enables the model to filter out the most unlikely relations.

### Performance

Experimental results on widely-used datasets demonstrate that the model achieves state-of-the-art performance.

### Publication Details

The paper was published in Findings of the Association for Computational Linguistics: ACL 2025, pages 19556–19567, Vienna, Austria. The authors are Fu Zhang, Yi Yan, and Jingwei Cheng, and code is available at https://github.com/yanyi74/GREP.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f26f9989-d1d1-4442-aa30-934635bf0d1c",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "f9bc1580-d1de-400a-9757-838fa30225d5",
  "sourceToolAssistantUUID": "f26f9989-d1d1-4442-aa30-934635bf0d1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-10T19:30:25.007Z_

<details><summary>↩ Tool result · `toolu_01Rp8wcvxrXhGHbHDJZBK4CD`</summary>

```text
Web search results for query: "DPO RLHF "entity extraction" OR "relation extraction" OR "information extraction" fine-tuning LLM 2025 2026 document"

Links: [{"title":"[2305.18290] Direct Preference Optimization: Your Language Model is Secretly a Reward Model","url":"https://arxiv.org/abs/2305.18290"},{"title":"RLHF vs DPO in LLM fine-tuning: 60+ patent analysis | PatSnap","url":"https://www.patsnap.com/resources/blog/articles/rlhf-vs-dpo-in-llm-fine-tuning-60-patent-analysis-2/"},{"title":"Direct Preference Optimization (DPO) - Deep (Learning) Focus","url":"https://cameronrwolfe.substack.com/p/direct-preference-optimization"},{"title":"Direct Preference Optimization: Your Language Model is Secretly a Reward Model | OpenReview","url":"https://openreview.net/forum?id=HPuSIXJaa9"},{"title":"The Shift from RLHF to DPO for LLM Alignment: Fine-Tuning Large Language Models | by Nishtha kukreti | Medium","url":"https://medium.com/@nishthakukreti.01/the-shift-from-rlhf-to-dpo-for-llm-alignment-fine-tuning-large-language-models-631f854de301"},{"title":"Relation Extraction with Fine-Tuned Large Language Models in Retrieval Augmented Generation Frameworks","url":"https://arxiv.org/html/2406.14745v2"},{"title":"How to align open LLMs in 2025 with DPO & and synthetic data","url":"https://www.philschmid.de/rl-with-llms-in-2025-dpo"},{"title":"Data Annotation for LLM Fine-Tuning: RLHF and Instruction Tuning Guide | Second Talent","url":"https://www.secondtalent.com/resources/data-annotation-for-llm-fine-tuning-rlhf-and-instruction-tuning-guide/"},{"title":"GitHub - raghavc/LLM-RLHF-Tuning-with-PPO-and-DPO: Comprehensive toolkit for Reinforcement Learning from Human Feedback (RLHF) training, featuring instruction fine-tuning, reward model training, and support for PPO and DPO algorithms with various configurations for the Alpaca, LLaMA, and LLaMA2 models. · GitHub","url":"https://github.com/raghavc/LLM-RLHF-Tuning-with-PPO-and-DPO"},{"title":"Direct Preference Optimization: Your Language Model is Secretly a Reward Model","url":"https://arxiv.org/pdf/2305.18290"}]

I've completed the web search for your query about DPO RLHF and information extraction tasks. Here's a summary of what I found:

## Key Results:

**DPO and RLHF Fundamentals:**
DPO introduces a new parameterization of the reward model in RLHF that enables extraction of the optimal policy in closed form, allowing the standard RLHF problem to be solved with only a simple classification loss, resulting in an algorithm that is stable, performant, and computationally lightweight.

**Recent 2025-2026 Developments:**
A 2025 patent from CloudWalk Technology confirms that RLHF training consumes large computational resources, is prone to convergence difficulties due to RL's inherent instability, and is extremely sensitive to hyperparameters. Baidu's 2024 patent proposes combining DPO and PPO algorithms for SFT training into a unified alignment learning framework, noting that methods merging DPO and PPO represent the next generation of alignment training.

**Information/Relation Extraction:**
In the current era dominated by Large Language Models, fine-tuning these models can overcome limitations associated with zero-shot LLM prompting-based relation extraction methods, and fine-tuned LLMs can be integrated into Retrieval Augmented-based approaches to address challenges of identifying implicit relations at the sentence level.

**Performance Comparisons:**
DPO reduces compute costs by 40-75% compared to RLHF and offers substantially more stable training, though DPO may lag in structured reasoning tasks and show weaker out-of-distribution generalization.

The search results show DPO and RLHF are active areas of research for LLM alignment through 2025-2026, with applications to information extraction tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99b5ee48-5ed5-465d-b186-b79d96d44c2e",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "62b6379d-064a-4e74-b6ff-304aac1b4de6",
  "sourceToolAssistantUUID": "99b5ee48-5ed5-465d-b186-b79d96d44c2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-10T19:30:28.151Z_

Let me now search for a few more specific areas and fetch detailed results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62b6379d-064a-4e74-b6ff-304aac1b4de6",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSes4woVXLQKGHSjjQQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82c30f20-d66c-4b0c-a768-8a1ace564843",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3s41nNMYr6EtmFJV65jya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 790,
      "cache_creation_input_tokens": 3122,
      "cache_read_input_tokens": 28657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3122,
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

_source line 64 · 2026-05-10T19:30:30.097Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011Tdy22gaSFL2BsgSttQzSz`</summary>

```json
{
  "url": "https://aclanthology.org/2025.findings-acl.1002/",
  "prompt": "Extract the specific F1 scores on DocRED and Re-DocRED for GREP, comparison with baselines, and method details. What are the exact numbers?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82c30f20-d66c-4b0c-a768-8a1ace564843",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSes4woVXLQKGHSjjQQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d7903286-de48-4384-92e7-366d5939e058",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3s41nNMYr6EtmFJV65jya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 790,
      "cache_creation_input_tokens": 3122,
      "cache_read_input_tokens": 28657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3122,
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

_source line 65 · 2026-05-10T19:30:30.587Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ls2qqyUQ8J2pBuvuGHwhCD`</summary>

```json
{
  "query": "\"entity pair\" \"relation summarization\" \"retrieval\" LLM document-level relation extraction NAACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7903286-de48-4384-92e7-366d5939e058",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSes4woVXLQKGHSjjQQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "531acb9b-fcb1-499e-8e9f-b6600ebcaf5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3s41nNMYr6EtmFJV65jya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 790,
      "cache_creation_input_tokens": 3122,
      "cache_read_input_tokens": 28657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3122,
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

_source line 66 · 2026-05-10T19:30:32.640Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RKySsefm9NiyGcuNBz6Yhi`</summary>

```json
{
  "query": "GRPO \"knowledge extraction\" OR \"named entity\" OR \"relation extraction\" reinforcement learning 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "531acb9b-fcb1-499e-8e9f-b6600ebcaf5b",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSes4woVXLQKGHSjjQQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48c490d0-9c1e-4ff9-adc7-0d1fa7a11299",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3s41nNMYr6EtmFJV65jya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 790,
      "cache_creation_input_tokens": 3122,
      "cache_read_input_tokens": 28657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3122,
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

_source line 67 · 2026-05-10T19:30:32.715Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dwv155qewqno9ho6hfXpXz`</summary>

```json
{
  "query": "\"dual reasoning enhanced\" document-level relation extraction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48c490d0-9c1e-4ff9-adc7-0d1fa7a11299",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSes4woVXLQKGHSjjQQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a5f1432-837b-4325-a203-58b6744a4338",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3s41nNMYr6EtmFJV65jya",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 790,
      "cache_creation_input_tokens": 3122,
      "cache_read_input_tokens": 28657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3122,
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

### Tool result

_source line 68 · 2026-05-10T19:30:33.498Z_

<details><summary>↩ Tool result · `toolu_011Tdy22gaSFL2BsgSttQzSz`</summary>

```text
# F1 Score Information

I cannot provide the specific F1 scores you're requesting. The webpage content provided is an ACL Anthology entry page that contains metadata, citation information, and an abstract, but **does not include the experimental results section** with the actual numerical F1 scores on DocRED and Re-DocRED datasets.

The abstract states that "Experimental results on widely-used datasets demonstrate that our model achieves state-of-the-art performance," but the precise benchmark numbers are located in the full PDF paper itself, which is not included in the provided content.

**To obtain these metrics**, you would need to access the complete paper at: https://aclanthology.org/2025.findings-acl.1002.pdf or check the code repository: https://github.com/yanyi74/GREP
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7903286-de48-4384-92e7-366d5939e058",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "e16bff54-1d8e-41ef-b7a7-7e54ddc2e77a",
  "sourceToolAssistantUUID": "d7903286-de48-4384-92e7-366d5939e058",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-10T19:30:38.304Z_

<details><summary>↩ Tool result · `toolu_01Dwv155qewqno9ho6hfXpXz`</summary>

```text
Web search results for query: ""dual reasoning enhanced" document-level relation extraction 2026"

Links: [{"title":"Dual reasoning enhanced document-level relation extraction | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-026-12099-8"},{"title":"Document-level relation extraction via dual attention fusion and dynamic asymmetric loss | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-024-01632-8"},{"title":"Dual Reasoning Based Pairwise Representation Network for Document Level Relation Extraction | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9859653/"},{"title":"Advancing document-level relation extraction with a syntax-enhanced multi-hop reasoning network - Yu Zhong, Bo Shen, Tao Wang, 2024","url":"https://journals.sagepub.com/doi/abs/10.3233/JIFS-237167"},{"title":"Document-level Relation Extraction via Separate Relation Representation and Logical Reasoning | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3597610"},{"title":"[2201.04826] Document-level Relation Extraction with Context Guided Mention Integration and Inter-pair Reasoning","url":"https://arxiv.org/abs/2201.04826"},{"title":"Document-level relation extraction based on sememe knowledge-enhanced abstract meaning representation and reasoning | Complex & Intelligent Systems","url":"https://link.springer.com/article/10.1007/s40747-023-01084-6"},{"title":"Document-Level Relation Extraction with Path Reasoning | ACM Transactions on Asian and Low-Resource Language Information Processing","url":"https://dl.acm.org/doi/10.1145/3572898"},{"title":"EIDER: Evidence-enhanced Document-level Relation Extraction | OpenReview","url":"https://openreview.net/forum?id=Z9arKXstUo5"},{"title":"Attention Based Document-level Relation Extraction with ...","url":"https://www.ijcai.org/proceedings/2024/0726.pdf"}]

I found a highly relevant result! The search returned the exact paper you're looking for:

"Dual reasoning enhanced document-level relation extraction" was published in Neural Computing and Applications in 2026.

The paper addresses document-level relation extraction (DocRE), which involves identifying relations between entities distributed across multiple sentences within a document, noting that traditional methods often struggle to consider the comprehensive context of the entire document.

The authors propose a dual-reasoning enhanced method that integrates a two-stage graph convolutional network (GCN) and a Transformer-based module. The graph-based reasoning module leverages a two-stage GCN with multi-head attention to learn weighted entity representations and entity co-occurrence guidance, while the Transformer-based reasoning module enhances interaction between entity pairs through contextual fusion.

The paper is authored by Zhang, F., Wu, Y., Xu, H. and others, and is available through Springer Nature Link.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a5f1432-837b-4325-a203-58b6744a4338",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "1f3a8c42-3c24-49a1-a09b-5bdc8991a6e5",
  "sourceToolAssistantUUID": "4a5f1432-837b-4325-a203-58b6744a4338",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-10T19:30:40.102Z_

<details><summary>↩ Tool result · `toolu_01Ls2qqyUQ8J2pBuvuGHwhCD`</summary>

```text
Web search results for query: ""entity pair" "relation summarization" "retrieval" LLM document-level relation extraction NAACL 2025"

Links: [{"title":"Entity Pair-guided Relation Summarization and Retrieval in LLMs for Document-level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.224/"},{"title":"Entity Pair-guided Relation Summarization and Retrieval in ...","url":"https://aclanthology.org/anthology-files/pdf/findings/2025.findings-naacl.224.pdf"},{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"a Refiner with Task Distribution and Probability Fusion","url":"https://aclanthology.org/2025.naacl-long.319.pdf"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889v2"},{"title":"[2408.13889] LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/abs/2408.13889"},{"title":"Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11"},{"title":"Knowledge-Aware Query Expansion with Large Language ...","url":"https://aclanthology.org/2025.naacl-long.216.pdf"}]

I found the paper you were searching for! Here are the key details:

## "Entity Pair-guided Relation Summarization and Retrieval in LLMs for Document-level Relation Extraction"

The paper is authored by Fu Zhang, Hongsen Yu, Jingwei Cheng, and Huangming Xu and was published in 2025 in Findings of the Association for Computational Linguistics: NAACL 2025, pages 4022–4037, in Albuquerque, New Mexico.

### Overview
The paper addresses document-level relation extraction (DocRE), which aims to extract relations between entities in a document. While previous research primarily focused on traditional small models, recent studies have extended the scope to large language models (LLMs). Current LLM-based methods typically focus on filtering all potential relations (candidate relations) within a document at one time and then performing triplet fact extraction.

### Proposed Approach
The authors propose an entity pair-guided relation summarization and retrieval model (EP-RSR) for DocRE, which introduces an innovative LLM-based document-level relation extraction paradigm, EPRF (Entity Pair-Relation-Fact), along with an entity pair-level candidate relation filtering method. The approach first selects entity pairs that potentially contain relations and uses them to guide relation summarization and retrieval for extracting relation facts, which enhances the relevance between candidate relations and entity pairs while alleviating the issue of imbalanced NA data.

### Results
Benchmark testing on three datasets demonstrates that the approach achieves state-of-the-art (SOTA) performance for LLM-based models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "531acb9b-fcb1-499e-8e9f-b6600ebcaf5b",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "8322ecf9-35fe-4226-9957-ccf965f35de6",
  "sourceToolAssistantUUID": "531acb9b-fcb1-499e-8e9f-b6600ebcaf5b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-10T19:30:40.958Z_

<details><summary>↩ Tool result · `toolu_01RKySsefm9NiyGcuNBz6Yhi`</summary>

```text
Web search results for query: "GRPO "knowledge extraction" OR "named entity" OR "relation extraction" reinforcement learning 2025 2026 arxiv"

Links: [{"title":"[2411.15195] Graph Neural Network-Based Entity Extraction and Relationship Reasoning in Complex Knowledge Graphs","url":"https://arxiv.org/abs/2411.15195"},{"title":"KARL: Knowledge Agents via Reinforcement Learning","url":"https://arxiv.org/html/2603.05218v1"},{"title":"(PDF) Joint Extraction of Entities and Relations Using Reinforcement Learning and Deep Learning","url":"https://www.researchgate.net/publication/319117698_Joint_Extraction_of_Entities_and_Relations_Using_Reinforcement_Learning_and_Deep_Learning"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/html/2503.06639v4"},{"title":"Knowledge Graph Construction: Extraction, Learning, and Evaluation","url":"https://www.mdpi.com/2076-3417/15/7/3727"},{"title":"The construction and refined extraction techniques of knowledge graph based on large language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-38066-w"},{"title":"Recent Advances in Named Entity Recognition: A Comprehensive Survey and Comparative Study","url":"https://arxiv.org/html/2401.10825v3"},{"title":"LLMs for Knowledge Graph Construction and Reasoning: Recent Capabilities and Future Opportunities","url":"https://arxiv.org/html/2305.13168v4"},{"title":"Multimodal deep learning for entity relation extraction and spatiotemporal decision knowledge graph construction in earthquake emergency rescue | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-24135-z"},{"title":"Knowledge enhanced graph inference network based entity-relation extraction and knowledge graph construction for industrial domain | ENGINEERING Management | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s42524-023-0273-1"}]

Based on the web search results, here are the most relevant findings related to GRPO (Group Relative Policy Optimization) combined with knowledge extraction, named entity recognition, and relation extraction tasks in the context of reinforcement learning for 2025-2026:

## Key Findings:

**GRPO and Reinforcement Learning Applications:**

GRPO has been employed in the DeepSeek model series, including DeepSeek-v3 and DeepSeek-R1. DeepSeek-R1 unlocked reasoning capabilities in open-source models through the use of verifiable binary rewards with GRPO to fine-tune models on reasoning and math tasks.

A new post-training paradigm based on iterative large-batch off-policy RL has been developed, and the approach is robust to discrepancies between the trainer and inference engine without requiring heuristics such as clipped importance weighting or data deletion that were thought necessary for stabilizing online GRPO training for large-scale MoE models.

**Knowledge Extraction and Named Entity Recognition with RL:**

Recent work has shown that Reinforcement Learning can help address challenges in Named Entity Recognition (NER). Yang et al. (2023) proposed a Gaussian Prior Reinforcement Learning framework (GPRL) to learn the order of recognition of entities and use boundary positions of nested entities.

**Knowledge Graph Construction Trends:**

A dramatic increase in 2024 in supervised plus reinforcement learning hybrid approaches for knowledge graph tasks could stem from breakthroughs in reinforcement learning frameworks. Researchers have been motivated by the promise of achieving more robust and adaptive link prediction or reasoning tasks by combining supervised signals with reinforcement-based explorations.

The search results show active research at the intersection of GRPO/RL methodologies and knowledge extraction tasks, particularly for entity recognition and relation extraction applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48c490d0-9c1e-4ff9-adc7-0d1fa7a11299",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "eb9c95ef-18c0-473f-8135-ae1928a514b8",
  "sourceToolAssistantUUID": "48c490d0-9c1e-4ff9-adc7-0d1fa7a11299",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-10T19:30:44.914Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NLyM4TNDYHD7jV11j5ZeX2`</summary>

```json
{
  "url": "https://aclanthology.org/2025.findings-naacl.224/",
  "prompt": "Extract the specific F1 scores on DocRED and Re-DocRED for EP-RSR, which LLM they use, comparison with other LLM-based methods (AutoRE, etc.), and detailed method information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb9c95ef-18c0-473f-8135-ae1928a514b8",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSg3J8byGT28Hksq2Li",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e6658ac-ca89-4ef6-a56c-9603081751e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HBWg9d2okCLkiNvZsoGfvj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 803,
      "cache_creation_input_tokens": 3295,
      "cache_read_input_tokens": 31779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3295,
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

_source line 73 · 2026-05-10T19:30:45.918Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RrRzDqqj89axdyL9vTCs5L`</summary>

```json
{
  "query": "\"LLM with relation classifier\" document-level relation extraction DocRED 2024 2025 results F1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e6658ac-ca89-4ef6-a56c-9603081751e5",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSg3J8byGT28Hksq2Li",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "faa66e89-d2ef-442f-a125-f42084c48962",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HBWg9d2okCLkiNvZsoGfvj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 803,
      "cache_creation_input_tokens": 3295,
      "cache_read_input_tokens": 31779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3295,
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

_source line 74 · 2026-05-10T19:30:47.025Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017hkEDc16fcYn1jDvMN7cf3`</summary>

```json
{
  "query": "GRPO PPO \"document understanding\" OR \"document-level\" \"information extraction\" OR \"relation\" reinforcement learning LLM fine-tuning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faa66e89-d2ef-442f-a125-f42084c48962",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSg3J8byGT28Hksq2Li",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcd37ef6-49b0-45a8-9e7f-58504131934d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HBWg9d2okCLkiNvZsoGfvj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 803,
      "cache_creation_input_tokens": 3295,
      "cache_read_input_tokens": 31779,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3295
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 803,
          "output_tokens": 271,
          "cache_read_input_tokens": 31779,
          "cache_creation_input_tokens": 3295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3295,
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

_source line 75 · 2026-05-10T19:30:49.138Z_

<details><summary>↩ Tool result · `toolu_01NLyM4TNDYHD7jV11j5ZeX2`</summary>

```text
# Summary of EP-RSR Paper Content

Based on the provided web page, I can only extract limited information:

## Available Information

**Model & Approach:**
The paper proposes "an entity pair-guided relation summarization and retrieval model (EP-RSR)" that introduces the EPRF paradigm for document-level relation extraction with entity pair-level candidate relation filtering.

**Key Innovation:**
The method "first selects entity pairs that potentially contain relations and uses them to guide relation summarization and retrieval for extracting relation facts."

## Information Not Available

Unfortunately, the webpage content does not include:
- Specific F1 scores on DocRED or Re-DocRED datasets
- The particular LLM used in the model
- Quantitative comparisons with AutoRE or other LLM-based baselines
- Detailed technical method specifications beyond the paradigm description

**Note:** These critical evaluation metrics and comparative results would be found in the full PDF paper (linked as https://aclanthology.org/2025.findings-naacl.224.pdf), which is not included in the provided content. The webpage serves primarily as a metadata and citation resource rather than a detailed technical summary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e6658ac-ca89-4ef6-a56c-9603081751e5",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "ee9945dc-653c-43dc-88ad-450e790c16ef",
  "sourceToolAssistantUUID": "7e6658ac-ca89-4ef6-a56c-9603081751e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-10T19:30:52.635Z_

<details><summary>↩ Tool result · `toolu_01RrRzDqqj89axdyL9vTCs5L`</summary>

```text
Web search results for query: ""LLM with relation classifier" document-level relation extraction DocRED 2024 2025 results F1"

Links: [{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889v2"},{"title":"[2408.13889] LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/abs/2408.13889"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://openreview.net/pdf?id=SOWcC2cCMT"},{"title":"[Literature Review] LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://www.themoonlight.io/en/review/llm-with-relation-classifier-for-document-level-relation-extraction"},{"title":"(PDF) LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://www.researchgate.net/publication/383428854_LLM_with_Relation_Classifier_for_Document-Level_Relation_Extraction"},{"title":"[PDF] DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DocRED:-A-Large-Scale-Document-Level-Relation-Yao-Ye/2745fc72e1dd53d1c30f17cf05841b163c2f63c9"},{"title":"Document-level Relation Extraction with Relation Correlations - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608023006883"},{"title":"Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction | OpenReview","url":"https://openreview.net/forum?id=SOWcC2cCMT"},{"title":"[2408.13889v1] LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/abs/2408.13889v1"}]

Based on the search results, here's what I found about "LLM with Relation Classifier for Document-Level Relation Extraction":

## Overview

The paper presents a novel approach to document-level relation extraction (DocRE) by utilizing large language models (LLMs) structured around a composite method that integrates a relation classifier. The method introduces a novel classifier-LLM approach to DocRE, where the proposed approach begins with a classifier designed to select entity pair candidates that exhibit potential relations and then feed them to LLM for final relation classification.

## Key Problem Being Addressed

LLM-based methods still lag behind traditional methods in document-level relation extraction (DocRE), with the dispersion of attention by LLMs due to entity pairs without relations identified as a primary factor.

## Methodology

The methodology consists of two main stages: Relation Candidate Proposal (RCP) and Relation Classification (RC). To prevent LLMs from prioritizing NA entity pairs, the proposed LMRC methodology initially uses traditional neural networks for Relation Candidate Proposal to identify relation-expressing entity pairs.

## Performance Results

Through systematic evaluations focusing on metrics like F1 scores and Ignoring F1, LMRC outperformed competing methods, demonstrating practical advantages over traditional and recently proposed LLM-based methods. Experiments on DocRE benchmarks reveal that the method significantly outperforms recent LLM-based DocRE models and narrows the performance gap with state-of-the-art BERT-based models.

## Datasets

The paper reports on several experiments using the DocRED and Re-DocRED datasets, which are extensively used benchmarks for evaluating document-level relation extraction tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "faa66e89-d2ef-442f-a125-f42084c48962",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "6fdd7794-6782-48cf-b859-35183174a7e0",
  "sourceToolAssistantUUID": "faa66e89-d2ef-442f-a125-f42084c48962",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-10T19:30:55.798Z_

<details><summary>↩ Tool result · `toolu_017hkEDc16fcYn1jDvMN7cf3`</summary>

```text
Web search results for query: "GRPO PPO "document understanding" OR "document-level" "information extraction" OR "relation" reinforcement learning LLM fine-tuning 2025 2026"

Links: [{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"Reinforcement Learning (RL) Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide"},{"title":"A Guide to Reinforcement Learning Post-Training for LLMs: PPO, DPO, GRPO, and Beyond","url":"https://huggingface.co/blog/karina-zadorozhny/guide-to-llm-post-training-algorithms"},{"title":"The State of Reinforcement Learning for LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"},{"title":"A vision researcher’s guide to some RL stuff: PPO & GRPO - Yuge (Jimmy) Shi","url":"https://yugeten.github.io/posts/2025/01/ppogrpo/"},{"title":"PPO for LLMs: A Guide for Normal People","url":"https://cameronrwolfe.substack.com/p/ppo-llm"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"Published as a conference paper at ICLR 2026 GROUP-RELATIVE REINFORCE","url":"https://openreview.net/pdf?id=7CFlXvCoN6"},{"title":"GRPO++: Tricks for Making RL Actually Work","url":"https://cameronrwolfe.substack.com/p/grpo-tricks"},{"title":"DeepSeekMath: Pushing the Limits of Mathematical","url":"https://arxiv.org/pdf/2402.03300"}]

I've found comprehensive information about GRPO, PPO, and reinforcement learning for LLMs. Here's a summary of the key findings:

## GRPO vs PPO for LLM Training

Most early work on RL for LLMs used Proximal Policy Optimization (PPO) as the default RL optimizer, but recent reasoning research relies upon Group Relative Policy Optimization (GRPO).

## GRPO Overview

DeepSeek developed GRPO (Group Relative Policy Optimization) to train their R1 reasoning models. GRPO is an RL algorithm that samples multiple responses per prompt and computes advantages by comparing them within the group. It eliminates the need for a separate critic model, reducing memory and compute.

## Key Differences from PPO

GRPO is a variant of Proximal Policy Optimization (PPO) that enhances mathematical reasoning abilities while concurrently optimizing the memory usage of PPO. The efficiency improvements are achieved by dropping the "critic" (value model), i.e., the LLM that computes the value function.

## Applications to Reinforcement Learning with Verifiable Rewards (RLVR)

RLVR trains models on tasks where correctness can be automatically checked, like math problems and code execution. Instead of human preference labels, the reward signal comes from programmatic verification.

## Recent Developments (2025-2026)

GRPO was introduced by DeepSeek and is now used in models like Nemotron 3 Super. The most consequential shift in 2025 was the move from human preference labels to verifiable rewards for reasoning tasks. DeepSeek-R1 demonstrated that pure RL with verifiable rewards (RLVR) can produce emergent reasoning capabilities, including self-reflection and dynamic strategy adaptation, without any human-labeled reasoning traces.

The search results do not contain specific information about GRPO/PPO applied to document understanding, document-level information extraction, or relation extraction tasks. The focus is primarily on reasoning and mathematical problem-solving applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcd37ef6-49b0-45a8-9e7f-58504131934d",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "fbde0d0e-36a8-4687-ad26-431ad503df7d",
  "sourceToolAssistantUUID": "fcd37ef6-49b0-45a8-9e7f-58504131934d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-10T19:31:00.266Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U3nTfqQVykovSjLHX16Qpx`</summary>

```json
{
  "url": "https://arxiv.org/html/2408.13889v2",
  "prompt": "Extract the specific F1 scores of LMRC on DocRED and Re-DocRED (dev and test), which LLM is used, comparison with AutoRE and other methods. List exact numbers from tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbde0d0e-36a8-4687-ad26-431ad503df7d",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSh8h6deVej9VWzdDYb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf0853ea-5304-46f6-b261-435e9d78471a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFv7Q1ixhw3bPEQNHnECSR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3401,
      "cache_read_input_tokens": 35074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3401,
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

_source line 79 · 2026-05-10T19:31:01.281Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0126fMrkg2iFSyH6yom86k5J`</summary>

```json
{
  "query": "\"VaeDiff-DocRE\" data augmentation document-level relation extraction 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf0853ea-5304-46f6-b261-435e9d78471a",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSh8h6deVej9VWzdDYb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c76e26f-f286-42e8-ba9a-90799ad4dede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFv7Q1ixhw3bPEQNHnECSR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3401,
      "cache_read_input_tokens": 35074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3401,
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

_source line 80 · 2026-05-10T19:31:02.167Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SpVp5x3AkvD7xif56uP4sW`</summary>

```json
{
  "query": "reinforcement learning reward model \"relation extraction\" OR \"triple extraction\" OR \"knowledge graph\" LLM GRPO 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c76e26f-f286-42e8-ba9a-90799ad4dede",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSh8h6deVej9VWzdDYb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82ad3553-bf67-4bb1-9eac-cf8cda757687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFv7Q1ixhw3bPEQNHnECSR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3401,
      "cache_read_input_tokens": 35074,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3401
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 252,
          "cache_read_input_tokens": 35074,
          "cache_creation_input_tokens": 3401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3401,
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

_source line 81 · 2026-05-10T19:31:07.540Z_

<details><summary>↩ Tool result · `toolu_01U3nTfqQVykovSjLHX16Qpx`</summary>

```text
# LMRC Performance Results

## DocRED Results

**LMRC with LLaMA2-13B-Chat:**
- Dev: F1 = 59.97, Ign F1 = 58.16
- Test: F1 = 60.52, Ign F1 = 58.49

**LMRC with LLaMA3-8B-Instruct:**
- Dev: F1 = 61.01, Ign F1 = 59.13
- Test: F1 = 60.84, Ign F1 = 58.77

## Re-DocRED Results

**LMRC with LLaMA2-13B-Chat:**
- Test: F1 = 74.63, Ign F1 = 74.08

**LMRC with LLaMA3-8B-Instruct:**
- Test: F1 = 72.80, Ign F1 = 72.21

## Comparative Performance

The proposed LMRC substantially outperforms baseline LLM approaches. For context, the direct fine-tuning baseline (LLaMA2-13B-Chat alone) achieved only 39.25 F1 on DocRED dev. LMRC improves this to approximately 60 F1, narrowing the gap with BERT-based SOTA (DREEAM: 67.41 F1).

On Re-DocRED, LMRC with LLaMA2-13B-Chat (74.63 F1) outperforms the AutoRE baseline mentioned in the paper, which scored 53.84 F1.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf0853ea-5304-46f6-b261-435e9d78471a",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "2bccc8e5-4b77-4156-85e8-ab4d490b9cf1",
  "sourceToolAssistantUUID": "cf0853ea-5304-46f6-b261-435e9d78471a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-10T19:31:07.709Z_

<details><summary>↩ Tool result · `toolu_0126fMrkg2iFSyH6yom86k5J`</summary>

```text
Web search results for query: ""VaeDiff-DocRE" data augmentation document-level relation extraction 2025"

Links: [{"title":"[2412.13503] VaeDiff-DocRE: End-to-end Data Augmentation Framework for Document-level Relation Extraction","url":"https://arxiv.org/abs/2412.13503"},{"title":"VaeDiff-DocRE: End-to-end Data Augmentation Framework for Document-level Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.488/"},{"title":"GitHub - khaitran22/VaeDiff-DocRE: [COLING 2025] VaeDiff-DocRE: End-to-end Data Augmentation for Document-level Relation Extraction via Variational Autoencoder and Diffusion Prior","url":"https://github.com/khaitran22/VaeDiff-DocRE"},{"title":"Dual reasoning enhanced document-level relation extraction | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-026-12099-8"},{"title":"VaeDiff-DocRE: End-to-end Data Augmentation Framework for Document-level Relation Extraction","url":"https://arxiv.org/html/2412.13503v1"},{"title":"(PDF) VaeDiff-DocRE: End-to-end Data Augmentation Framework for Document-level Relation Extraction","url":"https://www.researchgate.net/publication/387183827_VaeDiff-DocRE_End-to-end_Data_Augmentation_Framework_for_Document-level_Relation_Extraction"},{"title":"VaeDiff-DocRE: End-to-end Data Augmentation ...","url":"https://aclanthology.org/2025.coling-main.488.pdf"},{"title":"VaeDiff-DocRE: End-to-end Data Augmentation Framework for Document-level Relation Extraction | alphaXiv","url":"https://www.alphaxiv.org/abs/2412.13503"},{"title":"[Literature Review] VaeDiff-DocRE: End-to-end Data Augmentation Framework for Document-level Relation Extraction","url":"https://www.themoonlight.io/en/review/vaediff-docre-end-to-end-data-augmentation-framework-for-document-level-relation-extraction"},{"title":"[PDF] VaeDiff-DocRE: End-to-end Data Augmentation Framework for Document-level Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/VaeDiff-DocRE:-End-to-end-Data-Augmentation-for-Tran-Hua/c86039e10308b16b0e6073ce53d222411ce1eb2f"}]

I've found comprehensive information about VaeDiff-DocRE. Here's what the search results reveal:

## Overview

VaeDiff-DocRE is an end-to-end data augmentation framework for document-level relation extraction that was accepted at the 31st International Conference on Computational Linguistics (COLING 2025).

## Problem & Motivation

Document-level Relation Extraction (DocRE) aims to identify relationships between entity pairs within a document. However, most existing methods assume a uniform label distribution, resulting in suboptimal performance on real-world, imbalanced datasets.

## Technical Approach

The method leverages the Variational Autoencoder (VAE) architecture to capture all relation-wise distributions formed by entity pair representations and augment data for underrepresented relations. To better capture the multi-label nature of DocRE, the VAE's latent space is parameterized with a Diffusion Model.

The approach introduces a hierarchical training framework to integrate the proposed VAE-based augmentation module into DocRE systems.

## Results

Experiments on two benchmark datasets demonstrate that the method outperforms state-of-the-art models, effectively addressing the long-tail distribution problem in DocRE.

## Authors & Source Code

The paper is by Khai Phan Tran, Wen Hua, and Xue Li, with code released at https://github.com/khaitran22/VaeDiff-DocRE.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c76e26f-f286-42e8-ba9a-90799ad4dede",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "47e0ada1-05d4-43ac-be6c-b221e2467317",
  "sourceToolAssistantUUID": "3c76e26f-f286-42e8-ba9a-90799ad4dede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-10T19:31:10.489Z_

<details><summary>↩ Tool result · `toolu_01SpVp5x3AkvD7xif56uP4sW`</summary>

```text
Web search results for query: "reinforcement learning reward model "relation extraction" OR "triple extraction" OR "knowledge graph" LLM GRPO 2025 2026"

Links: [{"title":"GraphRAG-R1: Graph Retrieval-Augmented Generation with Process-Constrained Reinforcement Learning","url":"https://arxiv.org/html/2507.23581"},{"title":"RLKGF: Reinforcement Learning from Knowledge Graph Feedback Without Human Annotations - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.344/"},{"title":"Frontiers | Practices, opportunities and challenges in the fusion of knowledge graphs and large language models","url":"https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1590632/full"},{"title":"Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle","url":"https://arxiv.org/html/2509.16679v1"},{"title":"Ultimate Guide - The Best Open Source LLMs For Knowledge Graph Construction In 2026","url":"https://www.siliconflow.com/articles/en/best-open-source-LLM-for-Knowledge-Graph-Construction"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/html/2510.20345v1"},{"title":"GitHub - DavidZWZ/Awesome-RAG-Reasoning: [EMNLP 2025] Awesome RAG Reasoning Resources · GitHub","url":"https://github.com/DavidZWZ/Awesome-RAG-Reasoning"},{"title":"Reinforcement Learning (RL) Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"}]

I've completed the web search for your query. Here are the most relevant results:

## Key Findings

**1. GraphRAG-R1 with GRPO (2026)**
GraphRAG-R1 uses a modified version of GRPO that supports the roll-out-with-thinking capability and employs Group Relative Policy Optimization to leverage external retrieval tools on demand. The framework combines structured graph triplets (capturing precise entity relationships) with unstructured text snippets to provide more comprehensive knowledge for the LLM's reasoning tasks.

**2. RLKGF: Reinforcement Learning from Knowledge Graph Feedback (2025)**
RLKGF proposes a novel method that leverages KG semantics and structure to derive RL rewards in the absence of manual annotations. Unlike RLAIF, RLKGF directly integrates human priors encoded in KGs as the reward model, structuring context-relevant facts into knowledge subgraphs and defining rewards by simulating information flow across semantic and logical connections.

**3. Scene Graph Structures with GRPO (2025)**
Research combined SFT with GRPO and introduced a rule-based reward tailored to scene graph structures, improving structural validity and relationship recall.

**4. Knowledge Graph Construction Survey (2025)**
SF-GPT uses three modules for knowledge triple extraction: Entity Extraction Filter, Entity Alignment Generator, and Self-Fusion Subgraph strategy to reduce noise.

**5. GRPO Framework Overview**
DeepSeek developed GRPO to train their R1 reasoning models, with key differences to PPO being the removal of the value model and reward model, replaced with statistics from calling the reward function and custom reward functions using RLVR.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82ad3553-bf67-4bb1-9eac-cf8cda757687",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "db2e8962-7647-4601-944d-ab127aad5f9a",
  "sourceToolAssistantUUID": "82ad3553-bf67-4bb1-9eac-cf8cda757687",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 84 · 2026-05-10T19:31:13.012Z_

Let me do a few final targeted searches for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db2e8962-7647-4601-944d-ab127aad5f9a",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSiDVc3vzKfhYHyawZx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "397fc3cf-5fa6-4d3c-971e-8b7c146f7bbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6q6aLtmPydXbMsC4fBV9P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2752,
      "cache_read_input_tokens": 38475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2752,
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

_source line 85 · 2026-05-10T19:31:14.272Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017j9LxV6Xko6oAbQ8VzDkZk`</summary>

```json
{
  "url": "https://aclanthology.org/2025.findings-acl.344/",
  "prompt": "Extract details about RLKGF: what does it do, how does it use RL for knowledge graph tasks, does it apply to relation extraction, what results does it achieve?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "397fc3cf-5fa6-4d3c-971e-8b7c146f7bbc",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSiDVc3vzKfhYHyawZx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15d7bef0-159c-4bbd-a650-66f8fd0d3fd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6q6aLtmPydXbMsC4fBV9P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2752,
      "cache_read_input_tokens": 38475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2752,
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

_source line 86 · 2026-05-10T19:31:15.329Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019igDGiWvYsqzfonCWF4UCL`</summary>

```json
{
  "query": "\"de-sampling\" \"mixture of experts\" document-level relation extraction DocRED ICANN 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15d7bef0-159c-4bbd-a650-66f8fd0d3fd9",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSiDVc3vzKfhYHyawZx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb39397c-b99c-43ad-9ce0-37ed534f775d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6q6aLtmPydXbMsC4fBV9P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2752,
      "cache_read_input_tokens": 38475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2752,
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

_source line 87 · 2026-05-10T19:31:15.888Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0135i5Pj94Zk8NjeLFBDehNW`</summary>

```json
{
  "query": "DocRED state-of-the-art F1 2025 2026 leaderboard results best"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb39397c-b99c-43ad-9ce0-37ed534f775d",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSiDVc3vzKfhYHyawZx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a932729-9ba8-4152-bd59-26f460ccfe1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6q6aLtmPydXbMsC4fBV9P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2752,
      "cache_read_input_tokens": 38475,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2752
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 255,
          "cache_read_input_tokens": 38475,
          "cache_creation_input_tokens": 2752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2752,
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

_source line 88 · 2026-05-10T19:31:18.851Z_

<details><summary>↩ Tool result · `toolu_017j9LxV6Xko6oAbQ8VzDkZk`</summary>

```text
# RLKGF Overview

## What It Does

RLKGF (Reinforcement Learning from Knowledge Graph Feedback) is a method that "leverages KG semantics and structure to derive RL rewards in the absence of manual annotations." Rather than requiring human preference labels, it uses knowledge graphs to train language models.

## How It Uses RL for Knowledge Graphs

The approach differs from traditional RLHF by eliminating human annotation. Instead, it "structures context-relevant facts into knowledge subgraphs and defines rewards by simulating information flow across semantic and logical connections between question and candidate response entities."

## Application Domain

RLKGF does **not** focus on relation extraction. Rather, it targets medical dialogue—the research evaluated the method on "three public and one private medical dialogue dataset," showing improvements in LLM diagnostic accuracy.

## Key Results

The paper demonstrates that "RLKGF significantly outperforms the competitive RLAIF in improving LLM diagnostic accuracy" across the tested medical datasets. The method avoids the need for additional preference labeling or reward model training compared to existing approaches.

## Code Availability

Implementation is available at: https://github.com/YanPioneer/RLKGF
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15d7bef0-159c-4bbd-a650-66f8fd0d3fd9",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "9fe61231-718b-4b82-9fc2-e31e760240d5",
  "sourceToolAssistantUUID": "15d7bef0-159c-4bbd-a650-66f8fd0d3fd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-10T19:31:25.901Z_

<details><summary>↩ Tool result · `toolu_019igDGiWvYsqzfonCWF4UCL`</summary>

```text
Web search results for query: ""de-sampling" "mixture of experts" document-level relation extraction DocRED ICANN 2025"

Links: [{"title":"Toward Better Document-Level Relation Extraction: De-sampling and Mixture of Experts in Action | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-04549-2_12"},{"title":"Document-level Relation Extraction via Separate Relation Representation and Logical Reasoning | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3597610"},{"title":"Multidisciplinary End-to-End Document-Level Relation Extraction from Scientific Literature | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-04627-7_15"},{"title":"Document-Level Relation Extraction with Global ...","url":"https://aclanthology.org/2025.findings-acl.1002.pdf"},{"title":"GitHub - kracr/document-level-relation-extraction: A NeuroSymbolic AI technique for extracting relations from documents.","url":"https://github.com/kracr/document-level-relation-extraction"},{"title":"Document-Level Relation Extraction with Path Reasoning | ACM Transactions on Asian and Low-Resource Language Information Processing","url":"https://dl.acm.org/doi/10.1145/3572898"},{"title":"Document-Level Relation Extraction Based on Machine Reading Comprehension and Hybrid Pointer-sequence Labeling | ACM Transactions on Asian and Low-Resource Language Information Processing","url":"https://dl.acm.org/doi/10.1145/3666042"},{"title":"(PDF) DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://www.researchgate.net/publication/333815327_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"Document-level Relation Extraction with Progressive Self-distillation | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3656168"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Request PDF","url":"https://www.researchgate.net/publication/335780641_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"}]

Based on the search results, I found relevant information about your query:

The paper "Toward Better Document-Level Relation Extraction: De-sampling and Mixture of Experts in Action" was published in ICANN 2025. The model introduces two core components: De-Sampling to balance the relation category distribution and alleviate the long-tail problem, and a Mixture of Experts system to focus on evidence.

The paper appears to address challenges in document-level relation extraction using the DocRED dataset. DocRED is described as a large-scale document-level relation extraction dataset from the Association for Computational Linguistics.

The key innovation is the combination of de-sampling techniques with a mixture of experts architecture to improve relation extraction performance on document-level tasks, particularly by handling class imbalance issues common in relation extraction datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb39397c-b99c-43ad-9ce0-37ed534f775d",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "038d71d8-ac33-4b66-b4c1-96925a97540b",
  "sourceToolAssistantUUID": "fb39397c-b99c-43ad-9ce0-37ed534f775d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-10T19:31:29.977Z_

<details><summary>↩ Tool result · `toolu_0135i5Pj94Zk8NjeLFBDehNW`</summary>

```text
Web search results for query: "DocRED state-of-the-art F1 2025 2026 leaderboard results best"

Links: [{"title":"F1 - The Official Home of Formula 1® Racing","url":"https://www.formula1.com/en/results/2025/drivers"},{"title":"F1 standings 2026 - Formula 1 points","url":"https://www.formula1points.com/season"},{"title":"F1 driver standings 2026 | RacingNews365","url":"https://racingnews365.com/f1/standings/2026/drivers"},{"title":"F1 Leaderboard: Updated Rankings Following Each Race of 2026 Season | NESN","url":"https://nesn.com/motorsport/news/f1-leaderboard-updated-rankings-each-race-2026-season/03fe56106954e97b5fa1e8ba"},{"title":"best f1 stats website for F1 Standings 2025 | Racing Statistics","url":"https://www.racingstatisticsf1.com/f1-standings-2025"},{"title":"Formula 1 2026 results and standings for top drivers and teams","url":"https://www.motorsport.com/f1/standings/2026/"},{"title":"2026 F1 Drivers Standings - ESPN","url":"https://www.espn.com/f1/standings"},{"title":"2026 • STATS F1","url":"https://www.statsf1.com/en/2026.aspx"},{"title":"F1 Drivers 2026 - Verstappen, Hamilton, Leclerc and more","url":"https://www.formula1.com/en/drivers"},{"title":"F1 driver standings 2025 | RacingNews365","url":"https://racingnews365.com/f1/standings/2025/drivers"}]

I notice the search results are returning information about Formula 1 racing standings, not about "DocRED," which is a machine learning benchmark dataset for document-level relation extraction. Let me search more specifically for DocRED:

Links: [{"title":"thunlp/docred · Datasets at Hugging Face","url":"https://huggingface.co/datasets/thunlp/docred"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset - ACL Anthology","url":"https://aclanthology.org/P19-1074/"},{"title":"GitHub - thunlp/DocRED: Dataset and codes for ACL 2019 DocRED: A Large-Scale Document-Level Relation Extraction Dataset. · GitHub","url":"https://github.com/thunlp/DocRED"},{"title":"GitHub - tonytan48/KD-DocRE: Implementation of Document-level Relation Extraction with Knowledge Distillation and Adaptive Focal Loss · GitHub","url":"https://github.com/tonytan48/KD-DocRE"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Request PDF","url":"https://www.researchgate.net/publication/335780641_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"DocRED Benchmark (Relation Extraction)","url":"https://paperswithcode.com/sota/relation-extraction-on-docred"},{"title":"Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation - ACL Anthology","url":"https://aclanthology.org/2022.findings-acl.132/"},{"title":"(PDF) DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://www.researchgate.net/publication/333815327_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"[1906.06127] DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://arxiv.org/abs/1906.06127"},{"title":"Revisiting DocRED – Addressing the False Negative Problem in Relation Extraction","url":"https://arxiv.org/html/2205.12696"}]

Good! Now let me search specifically for the current DocRED leaderboard results with the latest state-of-the-art F1 scores:

Links: [{"title":"F1 standings 2026 - Formula 1 points","url":"https://www.formula1points.com/season"},{"title":"best f1 stats website for F1 Standings 2025 | Racing Statistics","url":"https://www.racingstatisticsf1.com/f1-standings-2025"},{"title":"F1 - The Official Home of Formula 1® Racing","url":"https://www.formula1.com/en/results/2026/drivers"},{"title":"F1 Leaderboard: Updated Rankings Following Each Race of 2026 Season | NESN","url":"https://nesn.com/motorsport/news/f1-leaderboard-updated-rankings-each-race-2026-season/03fe56106954e97b5fa1e8ba"},{"title":"POWER RANKINGS final scores for 2025: Where do the drivers rank on the final leaderboard after an exhilarating 2025 season?","url":"https://www.formula1.com/en/latest/article/power-rankings-where-do-the-drivers-rank-on-the-final-leaderboard-after-an.RBWmq73lkM5CKZ0hgztOI"},{"title":"F1 standings teams 2025 - Formula 1 points","url":"https://www.formula1points.com/season/season-teams/2025"},{"title":"2026 • STATS F1","url":"https://www.statsf1.com/en/2026.aspx"},{"title":"F1 standings 2024 - Formula 1 points","url":"https://www.formula1points.com/season/2024"},{"title":"F1 standings 2025 - Formula 1 points","url":"https://www.formula1points.com/season/2025"},{"title":"2025 • STATS F1","url":"https://www.statsf1.com/en/2025.aspx"}]

Let me search more specifically for Papers with Code DocRED leaderboard results:

Links: [{"title":"DocRED Benchmark (Relation Extraction)","url":"https://paperswithcode.com/sota/relation-extraction-on-docred"},{"title":"GitHub - tonytan48/KD-DocRE: Implementation of Document-level Relation Extraction with Knowledge Distillation and Adaptive Focal Loss · GitHub","url":"https://github.com/tonytan48/KD-DocRE"},{"title":"Papers with Code - Paper tables with annotated results for DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://paperswithcode.com/paper/docred-a-large-scale-document-level-relation/review/"},{"title":"Papers with Code - DocRED Dataset","url":"https://paperswithcode.com/dataset/docred"},{"title":"Relation Extraction | Papers With Code","url":"https://paperswithcode.com/task/relation-extraction/latest"},{"title":"Papers with Code - Paper tables with annotated results for Revisiting DocRED -- Addressing the False Negative Problem in Relation Extraction","url":"https://paperswithcode.com/paper/revisiting-docred-addressing-the-overlooked/review/"},{"title":"Machine Learning Datasets - Relation Extraction","url":"https://paperswithcode.com/datasets?v=lst&o=newest&task=relation-extraction&page=1"},{"title":"Relation Extraction","url":"https://paperswithcode.com/task/relation-extraction"},{"title":"Papers with Code - DocRED-IE Benchmark (Document-level Relation Extraction)","url":"https://paperswithcode.com/sota/document-level-relation-extraction-on-docred-3"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset - ACL Anthology","url":"https://aclanthology.org/P19-1074/"}]

Let me search for more recent DocRED SOTA results with specific F1 scores:

Links: [{"title":"GLiM: Integrating Graph Transformer and LLM for ...","url":"https://aclanthology.org/2025.findings-acl.727.pdf"}]

Based on my search results, I found information about DocRED, which is a machine learning benchmark dataset, though I wasn't able to retrieve complete specific F1 scores for the 2025-2026 leaderboard rankings. However, I can provide you with what I found:

## DocRED Overview

DocRED is a dataset constructed from Wikipedia and Wikidata that annotates both named entities and relations, and is the largest human-annotated dataset for document-level relation extraction (RE) from plain text. DocRED requires reading multiple sentences in a document to extract entities and infer their relations by synthesizing all information of the document.

## Recent SOTA Progress

Document-level relation extraction models have been showing performance improvements, with some models exceeding previous state-of-the-art by 1.36 F1 and 1.46 Ign_F1 score on the DocRED leaderboard. 

There's also a revised version of the dataset: Models trained and evaluated on Re-DocRED (a revised version addressing annotation issues) gain around 13 F1 compared to DocRED.

Unfortunately, the search results did not contain the most current detailed leaderboard with specific F1 scores for 2025-2026. For the most up-to-date ranking results, I recommend checking the Papers with Code DocRED leaderboard directly at https://paperswithcode.com/sota/relation-extraction-on-docred or https://paperswithcode.com/sota/relation-extraction-on-redocred for the revised dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a932729-9ba8-4152-bd59-26f460ccfe1b",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "f065ab65-ddac-4d56-83bb-ddcd7d1ec366",
  "sourceToolAssistantUUID": "4a932729-9ba8-4152-bd59-26f460ccfe1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-10T19:31:33.428Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011sxR1HPfV3hgBg5hTuzyb7`</summary>

```json
{
  "url": "https://paperswithcode.com/sota/relation-extraction-on-docred",
  "prompt": "List the top-ranked methods on the DocRED leaderboard with their F1 and Ign F1 scores, model names, and dates. Focus on the most recent entries from 2024-2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f065ab65-ddac-4d56-83bb-ddcd7d1ec366",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSjeqdKUEwihvB3MTHh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f1ea8c4-0889-4e01-aa98-d521bb09d716",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvxKg6vKnD6RZ1KPy8LoTk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3936,
      "cache_read_input_tokens": 41227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3936,
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

### Tool result

_source line 92 · 2026-05-10T19:31:33.671Z_

<details><summary>↩ Tool result · `toolu_011sxR1HPfV3hgBg5hTuzyb7`</summary>

```text
REDIRECT DETECTED: The URL redirects to a different host.

Original URL: https://paperswithcode.com/sota/relation-extraction-on-docred
Redirect URL: https://huggingface.co/papers/trending
Status: 302 Found

To complete your request, I need to fetch content from the redirected URL. Please use WebFetch again with these parameters:
- url: "https://huggingface.co/papers/trending"
- prompt: "List the top-ranked methods on the DocRED leaderboard with their F1 and Ign F1 scores, model names, and dates. Focus on the most recent entries from 2024-2026."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f1ea8c4-0889-4e01-aa98-d521bb09d716",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "8abc2790-e1b7-4ad9-badb-1779f4039f38",
  "sourceToolAssistantUUID": "8f1ea8c4-0889-4e01-aa98-d521bb09d716",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-10T19:31:33.891Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012XcYKtM37VmXnhDPvKeT57`</summary>

```json
{
  "query": "\"evidence-aware\" OR \"evidence-enhanced\" LLM \"document-level relation extraction\" 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8abc2790-e1b7-4ad9-badb-1779f4039f38",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSjeqdKUEwihvB3MTHh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e2e43dae-117c-4470-aa3d-93b914ecf0b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HvxKg6vKnD6RZ1KPy8LoTk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3936,
      "cache_read_input_tokens": 41227,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3936
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 41227,
          "cache_creation_input_tokens": 3936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3936,
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

_source line 94 · 2026-05-10T19:31:39.162Z_

<details><summary>↩ Tool result · `toolu_012XcYKtM37VmXnhDPvKeT57`</summary>

```text
Web search results for query: ""evidence-aware" OR "evidence-enhanced" LLM "document-level relation extraction" 2025 2026"

Links: [{"title":"Evidence-aware Document-level Relation Extraction | OpenReview","url":"https://openreview.net/forum?id=JMyPmI06JN"},{"title":"Evidence-aware Document-level Relation Extraction | Proceedings of the 31st ACM International Conference on Information & Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3511808.3557313"},{"title":"Document-level relation extraction using evidence reasoning on RST-GRAPH - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950705121005360"},{"title":"Enhancing cross-evidence reasoning graph for document-level relation extraction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/"}]

Based on the web search results, I found relevant research on evidence-aware document-level relation extraction:

Document-level Relation Extraction (RE) is a task aiming at identifying relations of multiple entity pairs in a document. In most cases, a relational fact can be expressed via a small subset of sentences from the document, namely evidence sentences.

Recent work in this area includes evidence-aware document-level relation extraction research published in the Proceedings of the 31st ACM International Conference on Information & Knowledge Management in 2022. Additionally, a 2025 publication titled "Evidence and Axial Attention Guided Document-level Relation Extraction" was published in Computer Speech and Language in March 2025.

Other related approaches include a discourse-aware neural RE model (DISCO-RE) built upon BERT that uses evidence-aware attention methods to capture fine-grained evidence and avoid manual annotation of evidence in the dataset.

The search results show active research in evidence-aware approaches to document-level relation extraction, with publications appearing in 2025 as well as earlier years.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2e43dae-117c-4470-aa3d-93b914ecf0b8",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "f949bdd9-92b9-449f-ab17-7f3cab9b29a2",
  "sourceToolAssistantUUID": "e2e43dae-117c-4470-aa3d-93b914ecf0b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-10T19:31:42.666Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F7z9PKmiMkH7wbWCuwBtse`</summary>

```json
{
  "query": "site:paperswithcode.com \"relation-extraction-on-docred\" leaderboard F1 score 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f949bdd9-92b9-449f-ab17-7f3cab9b29a2",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSkL5YTuNfJdJmGLdrQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de2f21b0-f1c3-4454-8729-1c5e7ec02e63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FQM4FhZAeiC7nJpbKKkYVH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 909,
      "cache_read_input_tokens": 45163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 909,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-10T19:31:43.580Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D3qQNChFJiQdMQRa6eRYcc`</summary>

```json
{
  "query": "\"DREEAM\" OR \"JMRL\" OR \"COMM\" Re-DocRED F1 score state-of-the-art 2025 best result"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de2f21b0-f1c3-4454-8729-1c5e7ec02e63",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSkL5YTuNfJdJmGLdrQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b685aeb8-080f-41ee-92f0-862f7fef61c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FQM4FhZAeiC7nJpbKKkYVH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 909,
      "cache_read_input_tokens": 45163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 909,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-10T19:31:48.430Z_

<details><summary>↩ Tool result · `toolu_01F7z9PKmiMkH7wbWCuwBtse`</summary>

```text
Web search results for query: "site:paperswithcode.com "relation-extraction-on-docred" leaderboard F1 score 2025"

Links: [{"title":"GitHub - tonytan48/KD-DocRE: Implementation of Document-level Relation Extraction with Knowledge Distillation and Adaptive Focal Loss · GitHub","url":"https://github.com/tonytan48/KD-DocRE"},{"title":"[2203.10900] Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation","url":"https://arxiv.org/abs/2203.10900"},{"title":"Document-Level Zero-Shot Relation Extraction with Entity Side Information","url":"https://arxiv.org/html/2601.07271"},{"title":"Rethinking Document-Level Relation Extraction: A Reality Check","url":"https://arxiv.org/html/2306.08953"},{"title":"Document-Level Relation Extraction with Adaptive Focal Loss and Knowledge Distillation - ACL Anthology","url":"https://aclanthology.org/2022.findings-acl.132/"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Request PDF","url":"https://www.researchgate.net/publication/335780641_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"GLiM: Integrating Graph Transformer and LLM for ...","url":"https://aclanthology.org/2025.findings-acl.727.pdf"},{"title":"None Class Ranking Loss for Document-Level Relation Extraction","url":"https://www.ijcai.org/proceedings/2022/0630.pdf"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://openreview.net/pdf?id=SOWcC2cCMT"},{"title":"(PDF) Entity and Evidence Guided Relation Extraction for DocRED","url":"https://www.academia.edu/103732963/Entity_and_Evidence_Guided_Relation_Extraction_for_DocRED"}]

I've performed the web search, though I should note that my search removed the "site:" operator as per my search guidelines. The results provide information about document-level relation extraction on the DocRED dataset, but they don't contain specific 2025 leaderboard data from Papers with Code for the "relation-extraction-on-docred" task.

The search results include:

1. References to the DocRED leaderboard where models have achieved SOTA performance with scores exceeding previous best by 1.36 F1 and 1.46 Ign_F1

2. Information about Re-DocRED models that gain around 13 F1 compared to DocRED

3. Recent results showing Flair achieving F1 scores of 63.47% on DocRED

4. A 2025 research paper on GLiM model tested on BioRED, and DocRED datasets

However, the search results don't provide the specific current 2025 leaderboard rankings you requested from Papers with Code. To get the most up-to-date leaderboard data, I recommend visiting the Papers with Code website directly at their relation extraction leaderboards section.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de2f21b0-f1c3-4454-8729-1c5e7ec02e63",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "4c0b6cd9-df26-4c69-a8fe-33eecf58cf06",
  "sourceToolAssistantUUID": "de2f21b0-f1c3-4454-8729-1c5e7ec02e63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-10T19:31:49.580Z_

<details><summary>↩ Tool result · `toolu_01D3qQNChFJiQdMQRa6eRYcc`</summary>

```text
Web search results for query: ""DREEAM" OR "JMRL" OR "COMM" Re-DocRED F1 score state-of-the-art 2025 best result"

Links: [{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/html/2508.00757"},{"title":"[2302.08675] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://ar5iv.labs.arxiv.org/html/2302.08675"},{"title":"Document-Level Relation Extraction with Global ...","url":"https://aclanthology.org/2025.findings-acl.1002.pdf"},{"title":"DREEAM: Guiding Attention with Evidence for Improving ...","url":"https://aclanthology.org/2023.eacl-main.145.pdf"},{"title":"SAIS: Supervising and Augmenting Intermediate Steps for ...","url":"https://www.cs.emory.edu/~jyang71/files/sais.pdf"},{"title":"(PDF) GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://www.researchgate.net/publication/394262622_GLiDRE_Generalist_Lightweight_model_for_Document-level_Relation_Extraction"},{"title":"F1 points system: How can drivers score points in F1 2025?","url":"https://www.planetf1.com/features/f1-points-scoring-system-explained"},{"title":"2025 • STATS F1","url":"https://www.statsf1.com/en/2025.aspx"},{"title":"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction","url":"https://www.researchgate.net/publication/373811777_DREEAM_Guiding_Attention_with_Evidence_for_Improving_Document-Level_Relation_Extraction"},{"title":"SAIS: Supervising and Augmenting Intermediate Steps for ...","url":"https://aclanthology.org/2022.naacl-main.171.pdf"}]

Based on the search results, I found relevant information about state-of-the-art models on the Re-DocRED dataset in 2025:

DREEAM is mentioned as one of the current state-of-the-art methods, though the search results don't provide the specific F1 score for DREEAM on Re-DocRED. 

Regarding other models on Re-DocRED: TTM-RE is noted as a current state-of-the-art method alongside DREEAM, with TTM-RE incorporating a Turing Token Machine designed to scale better than other approaches with large datasets. GLiDRE achieves a test F1 score of 77.83 on Re-DocRED, though it does not surpass DREEAM and TTM-RE.

Unfortunately, the search results did not contain specific information about JMRL or COMM, nor the exact F1 scores for DREEAM or TTM-RE on Re-DocRED in 2025. The results suggest that DREEAM and TTM-RE are among the leading approaches, but the precise state-of-the-art scores are not clearly stated in the retrieved documents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b685aeb8-080f-41ee-92f0-862f7fef61c8",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "e337bc24-ba52-40d7-8eca-a4f7b4f26e06",
  "sourceToolAssistantUUID": "b685aeb8-080f-41ee-92f0-862f7fef61c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-10T19:31:57.068Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HgqLEz6Mkec1mRqo5ZqZE3`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.00757",
  "prompt": "Extract the detailed experimental results from GLiDRE: specific F1 scores on DocRED and Re-DocRED (dev and test), comparison table with baselines including DREEAM, TTM-RE, JMRL, KD-DocRE, ATLOP. List exact numbers from the results tables. What are the current SOTA numbers that GLiDRE compares against?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e337bc24-ba52-40d7-8eca-a4f7b4f26e06",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSm6cCPmTkzEqQ55d9y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb0e7450-dc40-42ee-8f30-4bd29ef086e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJXzRfmYDxehUrUKn6qfiv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1848,
      "cache_read_input_tokens": 46072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1848,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-10T19:31:57.364Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0179PHKYx2moww5kzHKQK3BJ`</summary>

```json
{
  "query": "\"GLiM\" graph transformer LLM document-level relation extraction ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb0e7450-dc40-42ee-8f30-4bd29ef086e5",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSm6cCPmTkzEqQ55d9y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5f8b19b-d31f-4d1e-8c10-ad2bcb575e23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJXzRfmYDxehUrUKn6qfiv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1848,
      "cache_read_input_tokens": 46072,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1848
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 225,
          "cache_read_input_tokens": 46072,
          "cache_creation_input_tokens": 1848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1848,
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

_source line 101 · 2026-05-10T19:32:02.056Z_

<details><summary>↩ Tool result · `toolu_01HgqLEz6Mkec1mRqo5ZqZE3`</summary>

```text
# GLiDRE Experimental Results Summary

## Re-DocRED Fully Supervised Setting (Table 3)

**GLiDRE Performance:**
- Dev F1: 77.76±0.35
- Dev Ign F1: 76.70±0.37
- Test F1: 77.83±0.23
- Test Ign F1: 76.80±0.22

**Baseline Comparisons:**

| Model | Test F1 | Test Ign F1 |
|-------|---------|------------|
| DREEAM | 80.20±0.45 | 78.56±0.39 |
| TTM-RE | 79.95±0.13 | 78.20±0.34 |
| KD-DocRE | 78.28±0.72 | 77.60±0.25 |
| ATLOP | 77.81±0.71 | 76.13±0.28 |
| GLiDRE | **77.83±0.23** | **76.80±0.22** |

## Current SOTA Context

The document indicates that "DREEAM and TTM-RE" represent the strongest existing methods on Re-DocRED. GLiDRE achieves competitive performance but trails these specialized approaches by approximately 2-3 F1 points. However, the paper notes that these models employ specialized mechanisms—DREEAM uses evidence annotations, while TTM-RE integrates a memory-augmented architecture—designed specifically for larger datasets.

GLiDRE's primary advantage emerges in data-constrained and few-shot scenarios, where it substantially outperforms these baselines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb0e7450-dc40-42ee-8f30-4bd29ef086e5",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "ee183c38-6338-4f3f-9307-140dfd6b0fd9",
  "sourceToolAssistantUUID": "fb0e7450-dc40-42ee-8f30-4bd29ef086e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-10T19:32:05.921Z_

<details><summary>↩ Tool result · `toolu_0179PHKYx2moww5kzHKQK3BJ`</summary>

```text
Web search results for query: ""GLiM" graph transformer LLM document-level relation extraction ACL 2025"

Links: [{"title":"GLiM: Integrating Graph Transformer and LLM for Document-Level Biomedical Relation Extraction with Incomplete Labeling - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.727/"},{"title":"GLiM: Integrating Graph Transformer and LLM for ...","url":"https://aclanthology.org/2025.findings-acl.727.pdf"},{"title":"GLiM: Integrating Graph Transformer and LLM for Document-Level Biomedical Relation Extraction with Incomplete Labeling | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.findings-acl.727@ACL"},{"title":"GitHub - HaoFang10/GLiM","url":"https://github.com/HaoFang10/GLiM"},{"title":"GLiM: Integrating Graph Transformer and LLM for Document-Level Biomedical Relation Extraction with Incomplete Labeling | Request PDF","url":"https://www.researchgate.net/publication/394273241_GLiM_Integrating_Graph_Transformer_and_LLM_for_Document-Level_Biomedical_Relation_Extraction_with_Incomplete_Labeling"},{"title":"RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints","url":"https://arxiv.org/html/2509.19057v1"},{"title":"GraphCheck: Breaking Long-Term Text Barriers with Extracted Knowledge Graph-Powered Fact-Checking - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12360635/"},{"title":"Information Extraction from Visually Rich Documents using ...","url":"https://aclanthology.org/2025.acl-long.844.pdf"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/html/2510.20345v1"},{"title":"GLiM: Integrating Graph Transformer and LLM for ...","url":"https://chatpaper.com/paper/178080"}]

I found comprehensive information about GLiM. Here's what the search revealed:

## GLiM: Overview

GLiM is a paper titled "Integrating Graph Transformer and LLM for Document-Level Biomedical Relation Extraction with Incomplete Labeling" published in the Findings of the Association for Computational Linguistics: ACL 2025.

## Key Innovation

GLiM is a novel framework that reduces the problem space using a graph-enhanced Transformer-based model and leverages large language models (LLMs) for reasoning. 

The framework employs a cascaded approach: first, a graph-enhanced Transformer processes entity-pair relations with finer granularity by dynamically adjusting the graph size based on the number of entities; then, LLM inference handles challenging cases.

## Problem Addressed

Document-level relation extraction faces challenges as the number and complexity of entities and entity-pair relations grow, causing incomplete annotations and frequent false negatives, especially in biomedical datasets due to high construction costs.

## Results

Experiments show that GLiM boosts average recall and F1 scores by +6.34 and +4.41, respectively, outperforming state-of-the-art models on biomedical benchmarks.

## Code Availability

Code will be released at https://github.com/HaoFang10/GLiM.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5f8b19b-d31f-4d1e-8c10-ad2bcb575e23",
  "isSidechain": true,
  "promptId": "e3a9a54e-9385-4828-a365-880213e09c46",
  "agentId": "a5ef95c84eda75a4a",
  "type": "user",
  "uuid": "34cf8545-9d6d-4c1d-888e-97bfba6eea1d",
  "sourceToolAssistantUUID": "d5f8b19b-d31f-4d1e-8c10-ad2bcb575e23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 103 · 2026-05-10T19:33:37.064Z_

Now I have comprehensive information. Let me compile the final report.

Here is a comprehensive report on recent (2025-2026) work on document-level relation extraction, organized by your specific questions.

---

## 1. LLMs for Document-Level RE on DocRED

### RelPrior (arXiv 2511.08143, November 2025)
**"Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction"**
- Authors: Qiankun Pi, Yepeng Sun, Jicang Lu, Qinlong Fan, Ningbo Huang, Shiyu Wang
- Two-module architecture: (1) Entity Pairs Filtering (EPF) -- binary classification of whether entity pairs are related, and (2) Relation Matching (RM) -- uses predefined relations as priors to match head/tail entities
- Tested on LLaMA3-8B, LLaMA2-13B-Chat, Qwen2.5-7B, DeepSeek-R1-Distill-LLaMA3-8B
- **DocRED results (LLaMA3-8B):** Dev F1=47.82, Test F1=48.34 (surpasses AutoRE by +2.06/+2.38 F1)
- **Re-DocRED results:** Dev F1=55.94, Test F1=54.80
- Ablation shows removing EPF causes 18-21% F1 drop
- [Paper](https://arxiv.org/abs/2511.08143)

### LMRC (arXiv 2408.13889, 2024-2025)
**"LLM with Relation Classifier for Document-Level Relation Extraction"**
- Two-stage: Relation Candidate Proposal (traditional NN) then Relation Classification (LLM)
- **DocRED results (LLaMA3-8B-Instruct):** Dev F1=61.01, Test F1=60.84
- **Re-DocRED results (LLaMA2-13B-Chat):** Test F1=74.63
- Massive improvement over naive LLM fine-tuning (39.25 F1 -> 61.01 F1)
- Still trails BERT-based SOTA (DREEAM: ~67 F1 on DocRED) but significantly narrows the gap
- [Paper](https://arxiv.org/abs/2408.13889)

### EP-RSR (Findings of NAACL 2025)
**"Entity Pair-guided Relation Summarization and Retrieval in LLMs for Document-level Relation Extraction"**
- Authors: Fu Zhang, Hongsen Yu, Jingwei Cheng, Huangming Xu
- Introduces the EPRF (Entity Pair-Relation-Fact) paradigm: first select entity pairs with potential relations, then use them to guide relation summarization and retrieval
- Claims SOTA for LLM-based DocRE models on three datasets
- [Paper](https://aclanthology.org/2025.findings-naacl.224/)

### DocKS-RAG (ICML 2025)
**"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning"**
- Authors: Xiaolong Xu, Yibo Zhou, Haolong Xiang, Xiaoyong Li, Xuyun Zhang, Lianyong Qi, Wanchun Dou
- Three components: Document-level Knowledge Graph construction, Sentence-level Semantic RAG, and Hybrid-Prompt Tuning on LLMs
- Claims improvements over SOTA on two benchmark datasets
- Published in PMLR 267:69936-69949
- [Paper](https://openreview.net/forum?id=SVl9tIADWV)

### Ru-LLM (Springer, 2026)
**"Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction"**
- Learns logical rules via frequent pattern mining + LLM-assisted completion, then uses Monte Carlo Tree Search (MCTS) with four stages (selection, expansion, simulation, backpropagation) to search for rules
- Rules are converted into prompts for LLM + Chain-of-Thought verification retains only rule-satisfying triples
- Tested on DWIE, DocRED, and Re-DocRED
- Claims to outperform existing implicit reasoning models, LLM-based models, and rule-based frameworks
- [Paper](https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11)

### ToolRE (ICIC 2025)
**"Leveraging Large Language Models for Document-Level Complex Relation Extraction Through Self-Verification and Tool-Assisted Relational Reasoning"**
- Designs three agentic tools: entity extraction, explicit relation extraction, complex relation extraction
- Tuning-free strategy with backward verification for interpretable relation verification scores
- Claims significant outperformance over baseline LLM-based DocRE models
- [Paper](https://link.springer.com/chapter/10.1007/978-981-96-9812-7_32)

### GLiM (Findings of ACL 2025)
**"Integrating Graph Transformer and LLM for Document-Level Biomedical Relation Extraction with Incomplete Labeling"**
- Cascaded approach: graph-enhanced Transformer for entity-pair classification, then LLM for hard cases
- Focused on biomedical RE (not DocRED specifically)
- Average recall +6.34, F1 +4.41 over SOTA on biomedical benchmarks
- [Paper](https://aclanthology.org/2025.findings-acl.727/)

---

## 2. Combining Evidence Generation with Relation Extraction

### CDER (arXiv 2504.06529, April 2025)
**"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction"**
- Authors: Khai Phan Tran, Xue Li (published at ACIIDS 2024)
- Builds bipartite graph (entity pair nodes + sentence nodes) with three sub-graphs: Entity Pair sub-graph (collaboration modeling), Entity Pair-Sentence sub-graph (semantic relationships), Sentence sub-graph (co-reference reasoning)
- Uses BERT-base encoder
- **DocRED results (DREEAM+CDER):** Test F1=62.45, Ign F1=60.22, Evidence F1=53.03
- Evidence retrieval: Precision=86.84, Recall=82.75, Pos Evidence F1=84.75
- Improves evidence F1 by +6.6 over EIDER and +0.11 over DREEAM
- [Paper](https://arxiv.org/abs/2504.06529)

### VaeDiff-DocRE (COLING 2025)
**"VaeDiff-DocRE: End-to-end Data Augmentation Framework for Document-level Relation Extraction"**
- Authors: Khai Phan Tran, Wen Hua, Xue Li
- Uses VAE + Diffusion Model to augment data for underrepresented relations
- Addresses long-tail distribution problem in DocRE
- Outperforms SOTA on two benchmarks
- [Paper](https://arxiv.org/abs/2412.13503) | [Code](https://github.com/khaitran22/VaeDiff-DocRE)

### MAQD (2025, Springer JIIS)
**"Evidence selection via multi-aspect query diversification for cross-document relation extraction"**
- Constructs knowledge-aware entity graph from text, leverages LLMs for multi-faceted query augmentation
- Cross-document (not single-document) evidence selection
- [Paper](https://link.springer.com/article/10.1007/s10844-025-00952-6)

---

## 3. Reinforcement Learning (GRPO/PPO/DPO) for Document-Level IE

### Key Finding: No published work applies GRPO specifically to document-level RE

After extensive searching, **no paper was found that applies GRPO, PPO, or DPO specifically to document-level relation extraction on DocRED or similar benchmarks**. The RL-for-IE landscape in 2025-2026 is as follows:

- **GRPO** remains focused on mathematical reasoning, coding, and general LLM alignment (DeepSeek-R1, Nemotron 3 Super). It has been applied to scene graph structures (combining SFT with GRPO and rule-based rewards), but not to document-level RE.
- **RLKGF** (Findings of ACL 2025) uses RL with Knowledge Graph feedback for medical dialogue, not RE.
- **GraphRAG-R1** uses a modified GRPO for graph-based retrieval-augmented generation but focuses on QA, not RE.
- **URRel** (Expert Systems, 2026) combines unified representation with RL for joint entity and relation extraction in Chinese medical texts, but at sentence level.
- Older work uses RL for distantly supervised RE (noise reduction) and N-ary document-level RE, but these predate the GRPO/DPO era and use DQN or policy gradient methods.

The **LongRLVR** (ICLR 2026) framework is potentially relevant -- it augments sparse answer rewards with dense, verifiable context rewards that incentivize correct evidence selection in long contexts. This concept could theoretically be adapted for evidence-based document-level RE, but no one has published such work yet.

---

## 4. Non-LLM SOTA Methods on DocRED (2025-2026)

### COMM (AAAI 2025)
**"Concentrated Margin Maximization for Robust Document-Level Relation Extraction"**
- Instance-aware reasoning augmentation + margin-centered optimization
- Dramatically improves performance on noisy data: +12.9 F1 on DocRED-Mixed (RoBERTa-ATLOP)
- **Re-DocRED (RoBERTa-ATLOP+COMM):** Test F1=80.8 (+3.3 over baseline)
- [Paper](https://arxiv.org/abs/2503.13885)

### GREP (Findings of ACL 2025)
**"Document-Level Relation Extraction with Global Relations and Entity Pair Reasoning"**
- Auxiliary task predicts all possible relations in a document first, then entity pair-level reasoning
- Claims SOTA on widely-used datasets
- [Paper](https://aclanthology.org/2025.findings-acl.1002/)

### KnowRA (IJCAI 2025)
**"Knowledge Retrieval Augmented Method for Document-level Relation Extraction with Comprehensive Reasoning Abilities"**
- Document graph + co-reference resolution + external knowledge retrieval + axis attention for cross-sentence reasoning
- **Re-DocRED:** Surpasses JMRL-DREEAM by +0.28 F1
- **DWIE:** +1.13 F1 over previous SOTA
- [Paper](https://arxiv.org/abs/2501.00571)

### GLiDRE (arXiv 2508.00757, August 2025)
**"Generalist Lightweight model for Document-level Relation Extraction"**
- Compact model for supervised and few-shot settings
- **Re-DocRED:** Test F1=77.83 (competitive but trails DREEAM at 80.20 and TTM-RE at 79.95)
- New SOTA in few-shot DocRE
- [Paper](https://arxiv.org/abs/2508.00757)

### De-Sampling + MoE (ICANN 2025)
**"Toward Better Document-Level Relation Extraction: De-sampling and Mixture of Experts in Action"**
- De-Sampling to balance relation category distribution + Mixture of Experts for evidence focus
- [Paper](https://link.springer.com/chapter/10.1007/978-3-032-04549-2_12)

### Dual Reasoning Enhanced (Neural Computing and Applications, 2026)
- Two-stage GCN + Transformer-based module with multi-head attention and entity co-occurrence guidance
- [Paper](https://link.springer.com/article/10.1007/s00521-026-12099-8)

---

## 5. Current SOTA Numbers Summary (Re-DocRED, best known)

| Method | Type | Re-DocRED Test F1 |
|--------|------|-------------------|
| DREEAM | BERT-based | 80.20 |
| COMM (RoBERTa-ATLOP) | BERT-based | 80.8 |
| TTM-RE | BERT-based | 79.95 |
| KD-DocRE | BERT-based | 78.28 |
| GLiDRE | Compact | 77.83 |
| LMRC (LLaMA2-13B) | LLM-based | 74.63 |
| RelPrior (LLaMA3-8B) | LLM-based | 54.80 |

**Key gap:** LLM-based methods still lag behind specialized BERT-based methods by 5-25+ F1 points on DocRED/Re-DocRED, though the gap is narrowing (LMRC reaches 74.63 vs DREEAM's 80.20 on Re-DocRED).

---

## 6. Answer to Your Specific Question: Has anyone applied GRPO to document-level RE?

**No.** Based on exhaustive searching, no published work (through May 2026) applies GRPO, DAPO, or any group-relative RL method specifically to document-level relation extraction. GRPO remains concentrated in mathematical reasoning and code generation. The closest adjacent work is LongRLVR (ICLR 2026), which rewards evidence selection in long contexts but targets QA rather than RE. This represents a clear research gap -- document-level RE with verifiable rewards (relation correctness is checkable against gold annotations) seems well-suited for RLVR/GRPO approaches, but no one has published on it yet.

---

Sources:
- [CDER: Collaborative Evidence Retrieval](https://arxiv.org/abs/2504.06529)
- [RelPrior: Relation as a Prior](https://arxiv.org/abs/2511.08143)
- [GLiDRE: Generalist Lightweight DocRE](https://arxiv.org/abs/2508.00757)
- [LMRC: LLM with Relation Classifier](https://arxiv.org/abs/2408.13889)
- [COMM: Concentrated Margin Maximization (AAAI 2025)](https://arxiv.org/abs/2503.13885)
- [KnowRA: Knowledge Retrieval Augmented (IJCAI 2025)](https://arxiv.org/abs/2501.00571)
- [DocKS-RAG (ICML 2025)](https://openreview.net/forum?id=SVl9tIADWV)
- [GREP: Global Relations Entity Pair Reasoning (ACL 2025)](https://aclanthology.org/2025.findings-acl.1002/)
- [EP-RSR: Entity Pair-guided Relation Summarization (NAACL 2025)](https://aclanthology.org/2025.findings-naacl.224/)
- [VaeDiff-DocRE (COLING 2025)](https://arxiv.org/abs/2412.13503)
- [Ru-LLM: Logical Rule-Constrained LLMs](https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11)
- [ToolRE: Tool-Assisted Relational Reasoning (ICIC 2025)](https://link.springer.com/chapter/10.1007/978-981-96-9812-7_32)
- [GLiM: Graph Transformer + LLM for Biomedical RE (ACL 2025)](https://aclanthology.org/2025.findings-acl.727/)
- [De-Sampling + MoE (ICANN 2025)](https://link.springer.com/chapter/10.1007/978-3-032-04549-2_12)
- [Dual Reasoning Enhanced DocRE (2026)](https://link.springer.com/article/10.1007/s00521-026-12099-8)
- [MAQD: Cross-Document Evidence Selection](https://link.springer.com/article/10.1007/s10844-025-00952-6)
- [RLKGF: RL from Knowledge Graph Feedback (ACL 2025)](https://aclanthology.org/2025.findings-acl.344/)
- [LongRLVR (ICLR 2026)](https://github.com/real-absolute-AI/LongRLVR)
- [GutBrainIE Benchmark (2026)](https://arxiv.org/abs/2602.04320)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34cf8545-9d6d-4c1d-888e-97bfba6eea1d",
  "isSidechain": true,
  "agentId": "a5ef95c84eda75a4a",
  "requestId": "req_011CauSnJX5ydAA1ANjEShgW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "afcc3c8f-f03f-472b-a848-455a231769c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6fba8c4d-9839-4d27-a45c-283e521efb16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WaPMZXKhaL3aQsakyTyG5Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1568,
      "cache_read_input_tokens": 47920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1568,
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
