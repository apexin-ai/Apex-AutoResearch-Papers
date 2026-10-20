# Research conversation: Search for and verify these two papers: 1. "Self-Guide: Co-Evolution of Policy and Internal Reward for Language Agents" 

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a41b6c49438027517.jsonl`
- **Structured JSON:** [`f8e7b9af391869434841.json`](../../sessions/f8/f8e7b9af391869434841.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-11T23:55:30.559Z_

Search for and verify these two papers:

1. "Self-Guide: Co-Evolution of Policy and Internal Reward for Language Agents" (arXiv:2604.03098, April 2026)
   - Does it exist? Does it explicitly acknowledge the non-PBRS bias problem and cite Ng et al. 1999?
   - Does it use a trapezoid annealing schedule to withdraw internal rewards?
   - What results does it achieve?

2. "TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs" (ICLR 2026)
   - Does it exist? Is it actually at ICLR 2026?
   - Does it use formal PBRS with teacher-model log-likelihood over gold answers?
   - Is it designed for QA/search tasks rather than interactive environments?

Use WebSearch and WebFetch. Try multiple queries for each paper. Report everything you find.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "a41b6c49438027517",
  "type": "user",
  "uuid": "a2f448d6-d1fa-42a3-99f4-c2ace34a7bc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:55:30.565Z_

```json
{
  "parentUuid": "a2f448d6-d1fa-42a3-99f4-c2ace34a7bc0",
  "isSidechain": true,
  "agentId": "a41b6c49438027517",
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
  "uuid": "c9f09109-ef94-4f10-af8f-88e1d26afc3d",
  "timestamp": "2026-05-11T23:55:30.565Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:55:32.801Z_



I'll search for both papers using multiple queries. Let me start by loading the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9f09109-ef94-4f10-af8f-88e1d26afc3d",
  "isSidechain": true,
  "agentId": "a41b6c49438027517",
  "requestId": "req_011CawggFFMeXiXArwup2qtx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e26b813a-4bf9-4f82-91fa-8cc482d7afcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HjLLVSLZJWWBAEguPLqegT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 767,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 767,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-11T23:55:32.918Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01J2sotK7tAgG8JqGpYUfDjt`</summary>

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
  "parentUuid": "e26b813a-4bf9-4f82-91fa-8cc482d7afcf",
  "isSidechain": true,
  "agentId": "a41b6c49438027517",
  "requestId": "req_011CawggFFMeXiXArwup2qtx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69dac260-c8ee-4742-b94d-c5e86533fad6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HjLLVSLZJWWBAEguPLqegT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 767,
      "cache_read_input_tokens": 8223,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 767
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 105,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 767,
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

_source line 5 · 2026-05-11T23:55:32.922Z_

<details><summary>↩ Tool result · `toolu_01J2sotK7tAgG8JqGpYUfDjt`</summary>

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
  "parentUuid": "69dac260-c8ee-4742-b94d-c5e86533fad6",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "a41b6c49438027517",
  "type": "user",
  "uuid": "746e3057-2d5a-4a09-9cb9-cb534aa384aa",
  "sourceToolAssistantUUID": "69dac260-c8ee-4742-b94d-c5e86533fad6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:55:35.271Z_



Now let me search for both papers with multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "746e3057-2d5a-4a09-9cb9-cb534aa384aa",
  "isSidechain": true,
  "agentId": "a41b6c49438027517",
  "requestId": "req_011CawggRi9jbnDYxHMz7t9K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4133660b-8e7f-4292-814b-c7250dfe6fa1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPEbFYqucDfecQySoHE8ib",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8990,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 7 · 2026-05-11T23:55:36.847Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lnw8UJTskFcaFKsm6fo5m4`</summary>

```json
{
  "query": "Self-Guide Co-Evolution Policy Internal Reward Language Agents arXiv 2604.03098"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4133660b-8e7f-4292-814b-c7250dfe6fa1",
  "isSidechain": true,
  "agentId": "a41b6c49438027517",
  "requestId": "req_011CawggRi9jbnDYxHMz7t9K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "862ac8ee-ac3b-4aa8-98a6-8b6a9a68eb89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPEbFYqucDfecQySoHE8ib",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8990,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 8 · 2026-05-11T23:55:37.226Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012HaKM34CpCoLN4Yvg7R17G`</summary>

```json
{
  "query": "\"Self-Guide\" \"Co-Evolution of Policy and Internal Reward\" language agents 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "862ac8ee-ac3b-4aa8-98a6-8b6a9a68eb89",
  "isSidechain": true,
  "agentId": "a41b6c49438027517",
  "requestId": "req_011CawggRi9jbnDYxHMz7t9K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49acb0ed-169a-4bf0-b638-72140ad76902",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPEbFYqucDfecQySoHE8ib",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8990,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 9 · 2026-05-11T23:55:38.180Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XvDay21AiabhuRSbtuJrF5`</summary>

```json
{
  "query": "TIPS Turn-Level Information-Potential Reward Shaping Search-Augmented LLMs ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49acb0ed-169a-4bf0-b638-72140ad76902",
  "isSidechain": true,
  "agentId": "a41b6c49438027517",
  "requestId": "req_011CawggRi9jbnDYxHMz7t9K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b51b46ce-8950-4ab3-8b90-07169fe568bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPEbFYqucDfecQySoHE8ib",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8990,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 10 · 2026-05-11T23:55:38.674Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NNgS8EwC3pnEBhscNYjmA7`</summary>

```json
{
  "query": "\"TIPS\" \"reward shaping\" \"search-augmented\" LLM ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b51b46ce-8950-4ab3-8b90-07169fe568bb",
  "isSidechain": true,
  "agentId": "a41b6c49438027517",
  "requestId": "req_011CawggRi9jbnDYxHMz7t9K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38335070-a563-4a41-975b-76a3ccdc3b77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UPEbFYqucDfecQySoHE8ib",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1914,
      "cache_read_input_tokens": 8990,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1914,
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

_source line 11 · 2026-05-11T23:55:43.472Z_

<details><summary>↩ Tool result · `toolu_01Lnw8UJTskFcaFKsm6fo5m4`</summary>

```text
Web search results for query: "Self-Guide Co-Evolution Policy Internal Reward Language Agents arXiv 2604.03098"

Links: [{"title":"[2604.03098] Co-Evolution of Policy and Internal Reward for Language Agents","url":"https://arxiv.org/abs/2604.03098"},{"title":"Co-Evolution of Policy and Internal Reward for Language Agents","url":"https://arxiv.org/html/2604.03098"},{"title":"Co-Evolution of Policy and Internal Reward for Language Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2604.03098v1"},{"title":"Co-Evolution of Policy and Internal Reward for Language ...","url":"https://arxiv.org/pdf/2604.03098"},{"title":"[2412.13492] Efficient Language-instructed Skill Acquisition via Reward-Policy Co-Evolution","url":"https://arxiv.org/abs/2412.13492"},{"title":"Multi-Agent Evolve: LLM Self-Improve through Co-evolution","url":"https://arxiv.org/html/2510.23595v3"},{"title":"Agentic Policy Optimization via Instruction-Policy Co-Evolution","url":"https://arxiv.org/html/2512.01945"},{"title":"Efficient Language-instructed Skill Acquisition via Reward-Policy Co-Evolution","url":"https://arxiv.org/html/2412.13492v1"},{"title":"Multi-Agent Evolve: LLM Self-Improve through Multi-Agent Co-evolution | OpenReview","url":"https://openreview.net/forum?id=sknMpr8NWU"},{"title":"Sager: Self-Evolving User Policy Skills for Recommendation Agent","url":"https://arxiv.org/html/2604.14972"}]

I found the paper you're looking for! Here are the key details:

**Title:** Co-Evolution of Policy and Internal Reward for Language Agents

**arXiv ID:** 2604.03098

**Key Contribution:**
Self-Guide is a self-generated internal reward for language agents that supports both inference-time guidance and training-time supervision. The agent uses Self-Guide as a short self-guidance signal to steer the next action during inference, and converts the same signal into step-level internal reward for denser policy optimization during training.

**Core Innovation:**
This creates a co-evolving loop: better policy produces better guidance, and better guidance further improves policy as internal reward.

**Results:**
Across three agent benchmarks, inference-time self-guidance already yields clear gains, while jointly evolving policy and internal reward with GRPO brings further improvements (8%) over baselines trained solely with environment reward.

**Authors:** Xinyu Wang, Hanwei Wu, Jingwei Song, Shuyuan Zhang, Jiayi Zhang, Fanqi Kong, Tung Sum Thomas Kwok, Xiao-Wen Chang, Yuyu Luo, Chenglin Wu, Bang Liu

**Submission Date:** April 3, 2026


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "862ac8ee-ac3b-4aa8-98a6-8b6a9a68eb89",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "a41b6c49438027517",
  "type": "user",
  "uuid": "b72dba93-1cd2-456a-bf07-32355feed5e8",
  "sourceToolAssistantUUID": "862ac8ee-ac3b-4aa8-98a6-8b6a9a68eb89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-11T23:55:45.713Z_

<details><summary>↩ Tool result · `toolu_012HaKM34CpCoLN4Yvg7R17G`</summary>

```text
Web search results for query: ""Self-Guide" "Co-Evolution of Policy and Internal Reward" language agents 2026"

Links: [{"title":"[2604.03098] Co-Evolution of Policy and Internal Reward for Language Agents","url":"https://arxiv.org/abs/2604.03098"},{"title":"Co-Evolution of Policy and Internal Reward for Language Agents","url":"https://arxiv.org/html/2604.03098"},{"title":"Co-Evolution of Policy and Internal Reward for Language Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2604.03098v1"},{"title":"Co-Evolution of Policy and Internal Reward for Language ...","url":"https://arxiv.org/pdf/2604.03098"}]

I found the research paper you were looking for! Here are the key findings:

## Self-Guide: Co-Evolution of Policy and Internal Reward for Language Agents

Self-Guide is a self-generated internal reward for language agents that supports both inference-time guidance and training-time supervision.

### How It Works

The agent uses Self-Guide as a short self-guidance signal to steer the next action during inference, and converts the same signal into step-level internal reward for denser policy optimization during training. This creates a co-evolving loop: better policy produces better guidance, and better guidance further improves policy as internal reward.

### Performance Results

Across three agent benchmarks, inference-time self-guidance already yields clear gains, while jointly evolving policy and internal reward with GRPO brings further improvements (8%) over baselines trained solely with environment reward.

### Key Insight

Language agents can improve not only by collecting more experience, but also by learning to generate and refine their own internal reward during acting and learning.

The paper was published on April 3, 2026, and is available on arXiv at 2604.03098.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49acb0ed-169a-4bf0-b638-72140ad76902",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "a41b6c49438027517",
  "type": "user",
  "uuid": "9482a1a3-3256-457c-9dfc-cd36a648827b",
  "sourceToolAssistantUUID": "49acb0ed-169a-4bf0-b638-72140ad76902",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-11T23:55:45.733Z_

<details><summary>↩ Tool result · `toolu_01NNgS8EwC3pnEBhscNYjmA7`</summary>

```text
Web search results for query: ""TIPS" "reward shaping" "search-augmented" LLM ICLR 2026"

Links: [{"title":"TIPS: Turn-level Information-Potential Reward Shaping for Search-Augmented LLMs | OpenReview","url":"https://openreview.net/forum?id=eBMOr6a84z"},{"title":"GitHub - ucsd-wang-lab-lm/tips: TIPS: Turn-level Information-Potential Reward Shaping for Search-Augmented LLMs · GitHub","url":"https://github.com/ucsd-wang-lab-lm/tips"},{"title":"[2603.22293] TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs","url":"https://arxiv.org/abs/2603.22293"},{"title":"TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260322293X/abstract"},{"title":"$\\nabla$-Reasoner: LLM Reasoning via Test-Time Gradient Descent in Latent Space | OpenReview","url":"https://openreview.net/forum?id=pEJAja73dk"},{"title":"Empowering LLM Tool Invocation with Tool-call Reward Model | OpenReview","url":"https://openreview.net/forum?id=LnBEASInVr"},{"title":"Learn to Reason Efficiently with Adaptive Length-based Reward Shaping | OpenReview","url":"https://openreview.net/forum?id=hj9eKpqxQl"},{"title":"Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains | OpenReview","url":"https://openreview.net/forum?id=c1bTcrDmt4"},{"title":"FlowRL: Matching Reward Distributions for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=lObnTKbm9U"},{"title":"Published as a conference paper at ICLR 2026 MIRA: MEMORY-INTEGRATED","url":"https://openreview.net/pdf/d51989c024fa1f46307cb91fcded600d3ae233f0.pdf"}]

I found the paper you're looking for! Here are the search results:

## TIPS: Turn-level Information-Potential Reward Shaping for Search-Augmented LLMs

TIPS is a framework that assigns dense, turn-level rewards to each reasoning + tool-call segment based on the increased likelihood of the correct answer under a teacher model.

**Problem it addresses:** Search-augmented large language models trained with reinforcement learning have achieved strong results on open-domain question answering, but training remains a significant challenge due to unstable optimization caused by sparse rewards and difficult credit assignments across reasoning and tool calls.

**Key approach:** By leveraging potential-based reward shaping, TIPS offers fine-grained and policy-invariant guidance that overcomes the limitations of outcome-only optimization.

**Results:** Evaluated on seven QA benchmarks, TIPS consistently outperforms GRPO/PPO baselines and substantially improves training stability. For instance, with a Qwen-2.5 7B Instruct model, TIPS improves the average Exact Match score by 11.8% and F1 by 13.6% relative to PPO.

The paper is presented as an ICLR 2026 poster with code available on GitHub at ucsd-wang-lab-lm/tips, and the preprint is available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38335070-a563-4a41-975b-76a3ccdc3b77",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "a41b6c49438027517",
  "type": "user",
  "uuid": "46004cba-5225-414b-9f78-1697c407a188",
  "sourceToolAssistantUUID": "38335070-a563-4a41-975b-76a3ccdc3b77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-11T23:55:46.152Z_

<details><summary>↩ Tool result · `toolu_01XvDay21AiabhuRSbtuJrF5`</summary>

```text
Web search results for query: "TIPS Turn-Level Information-Potential Reward Shaping Search-Augmented LLMs ICLR 2026"

Links: [{"title":"TIPS: Turn-level Information-Potential Reward Shaping for Search-Augmented LLMs | OpenReview","url":"https://openreview.net/forum?id=eBMOr6a84z"},{"title":"GitHub - ucsd-wang-lab-lm/tips: TIPS: Turn-level Information-Potential Reward Shaping for Search-Augmented LLMs · GitHub","url":"https://github.com/ucsd-wang-lab-lm/tips"},{"title":"TIPS: TURN-LEVEL INFORMATION-POTENTIAL REWARD ...","url":"https://openreview.net/pdf?id=eBMOr6a84z"},{"title":"[2603.22293] TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs","url":"https://arxiv.org/abs/2603.22293"},{"title":"TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260322293X/abstract"},{"title":"TIPS: Turn-level Information-Potential Reward Shaping for Search-Augmented LLMs","url":"https://arxiv.org/html/2603.22293v1"},{"title":"TURN-LEVEL INFORMATION-POTENTIAL REWARD SHAPING ...","url":"https://openreview.net/pdf/13085d9acfed8b19aee5efc0de2bc905f3022ef4.pdf"},{"title":"TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.22293v1"},{"title":"Natural Language Processing Papers on X: \"TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs Yutao Xie, Nathaniel Thomas, Nicklas Hansen, Yang Fu, Li Erran Li, Xiaolong Wang https://t.co/GE55vp2dx3 [𝚌𝚜.𝙲𝙻 𝚌𝚜.𝙰𝙸 𝚌𝚜.𝙻𝙶] https://t.co/IlsQ0EAGQ4\" / X","url":"https://x.com/HEI/status/2036829806247940255"},{"title":"(PDF) TIPS: Turn-Level Information-Potential Reward Shaping ...","url":"https://www.researchgate.net/publication/403111589_TIPS_Turn-Level_Information-Potential_Reward_Shaping_for_Search-Augmented_LLMs"}]

Here are the search results for TIPS (Turn-Level Information-Potential Reward Shaping):

## Overview

TIPS is an RL framework that assigns dense rewards to each reasoning-tool-call segment based on how much it increases a teacher model's log-likelihood of the correct answer. The paper was published at ICLR 2026.

## Problem Addressed

Search-augmented LLMs trained with RL have achieved strong results on open-domain question answering, but training remains a significant challenge due to sparse rewards and difficult credit assignments across reasoning and tool calls.

## Key Features

TIPS assigns dense, turn-level rewards to each reasoning + tool-call segment based on the increased likelihood of the correct answer under a teacher model. The potential is computed by a frozen or periodically refreshed copy of the policy, so TIPS only requires checkpoints of the model being trained—no separate reward model, verifier, or human process labels.

## Results

On a search-augmented QA setting spanning seven in-domain and out-of-domain benchmarks, TIPS consistently outperforms PPO/GRPO baselines and substantially improves training stability; for example, on Qwen-2.5-7B Instruct it improves average Exact Match by 11.8% and F1 by 13.6% over PPO.

## Authors and Resources

The paper is authored by Yutao Xie, Nathaniel Thomas, Nicklas Hansen, Yang Fu, Li Erran Li, and Xiaolong Wang. The code base for TIPS is available at https://github.com/ucsd-wang-lab-lm/tips.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b51b46ce-8950-4ab3-8b90-07169fe568bb",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "a41b6c49438027517",
  "type": "user",
  "uuid": "7ae4623b-09d8-41f2-9ace-54ff4805f85f",
  "sourceToolAssistantUUID": "b51b46ce-8950-4ab3-8b90-07169fe568bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-11T23:55:48.243Z_

Both papers exist. Now let me fetch the detailed content of both papers to answer the specific questions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ae4623b-09d8-41f2-9ace-54ff4805f85f",
  "isSidechain": true,
  "agentId": "a41b6c49438027517",
  "requestId": "req_011CawghPvGv1ccaYKAaKeQw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "149053d1-2120-4dfb-b9f7-858681ac2636",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABdfoemNQgrDrjKmJumHy2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 938,
      "cache_creation_input_tokens": 2668,
      "cache_read_input_tokens": 10904,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2668,
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

_source line 16 · 2026-05-11T23:55:52.609Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VSv7MkgWF2cjE15iFRmi2o`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.03098",
  "prompt": "Extract all details about: 1) Does the paper mention \"Self-Guide\" as its name? 2) Does it acknowledge a non-PBRS bias problem? 3) Does it cite Ng et al. 1999 (the classic potential-based reward shaping paper)? 4) Does it use a \"trapezoid annealing schedule\" to withdraw internal rewards? 5) What are the exact numerical results and benchmarks? 6) What method does it use for training (GRPO, PPO, etc.)? Please extract all relevant details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "149053d1-2120-4dfb-b9f7-858681ac2636",
  "isSidechain": true,
  "agentId": "a41b6c49438027517",
  "requestId": "req_011CawghPvGv1ccaYKAaKeQw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6e9c528-bb69-4a12-8af6-75608406b761",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABdfoemNQgrDrjKmJumHy2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 938,
      "cache_creation_input_tokens": 2668,
      "cache_read_input_tokens": 10904,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2668,
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

_source line 17 · 2026-05-11T23:55:56.214Z_

<details><summary>↩ Tool result · `toolu_01VSv7MkgWF2cjE15iFRmi2o`</summary>

```text
Based on the arXiv page content provided:

1) **Self-Guide name**: Yes, explicitly mentioned. The abstract states the method is called "Self-Guide, a self-generated internal reward for language agents."

2) **Non-PBRS bias problem**: No acknowledgment of this issue is visible in the provided content.

3) **Ng et al. 1999 citation**: Cannot confirm from this page. The excerpt doesn't include the full references section.

4) **Trapezoid annealing schedule**: Not mentioned in the available content.

5) **Exact numerical results**: The abstract reports "8%" improvement over baselines, stating the method brings "further improvements (8\\%) over baselines trained solely with environment reward." No detailed benchmark scores are provided in this excerpt.

6) **Training method**: Yes, the abstract mentions "GRPO" as the optimization approach, stating results come from "jointly evolving policy and internal reward with GRPO."

The page content is limited to the abstract and metadata. Comprehensive technical details, references, and full experimental results would require accessing the complete PDF or HTML version of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6e9c528-bb69-4a12-8af6-75608406b761",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "a41b6c49438027517",
  "type": "user",
  "uuid": "6c330f18-4009-4997-b9fe-87cf48516893",
  "sourceToolAssistantUUID": "b6e9c528-bb69-4a12-8af6-75608406b761",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-11T23:55:56.690Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LRrGaMN2SKXYjdEcyQiqp8`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.03098",
  "prompt": "Look for ALL of the following: 1) Any mention of \"non-PBRS bias\" or bias from non-potential-based reward shaping. 2) Any citation of \"Ng et al. 1999\" or \"Ng, Harada, Russell\" or the classic potential-based reward shaping paper. 3) Any mention of \"trapezoid annealing\" or \"trapezoid schedule\" or annealing schedule for withdrawing/removing internal rewards. 4) How does it handle the fact that internal rewards might change the optimal policy? 5) What are the specific benchmark results? Report everything you find on these topics, including if they are NOT mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c330f18-4009-4997-b9fe-87cf48516893",
  "isSidechain": true,
  "agentId": "a41b6c49438027517",
  "requestId": "req_011CawghPvGv1ccaYKAaKeQw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45ca2266-65de-4efa-be6a-c1b6f2de2653",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABdfoemNQgrDrjKmJumHy2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 938,
      "cache_creation_input_tokens": 2668,
      "cache_read_input_tokens": 10904,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2668,
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

_source line 19 · 2026-05-11T23:55:59.398Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015sJKhocD4R5XZUTXJGSQNZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.22293",
  "prompt": "Extract all details about: 1) Is this paper at ICLR 2026? 2) Does it use formal PBRS (potential-based reward shaping)? 3) Does it use teacher-model log-likelihood over gold answers as potential? 4) Is it designed for QA/search tasks or interactive environments? 5) What are the exact numerical results? 6) What is the formal reward shaping formulation? Please report all details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45ca2266-65de-4efa-be6a-c1b6f2de2653",
  "isSidechain": true,
  "agentId": "a41b6c49438027517",
  "requestId": "req_011CawghPvGv1ccaYKAaKeQw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c6180c6-a2f2-4966-b933-d0b69127dd6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABdfoemNQgrDrjKmJumHy2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 938,
      "cache_creation_input_tokens": 2668,
      "cache_read_input_tokens": 10904,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2668,
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

_source line 20 · 2026-05-11T23:56:01.039Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01MaeRdLQdLSUJ4tdCPyHbhx`</summary>

```json
{
  "url": "https://openreview.net/forum?id=eBMOr6a84z",
  "prompt": "Is this paper accepted at ICLR 2026? What venue and year is it published at? What is the paper's status (accepted, rejected, poster, spotlight, oral)? Report all venue/acceptance details you can find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c6180c6-a2f2-4966-b933-d0b69127dd6f",
  "isSidechain": true,
  "agentId": "a41b6c49438027517",
  "requestId": "req_011CawghPvGv1ccaYKAaKeQw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "547c8510-b91d-4c45-975b-eb751d96e69b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABdfoemNQgrDrjKmJumHy2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 938,
      "cache_creation_input_tokens": 2668,
      "cache_read_input_tokens": 10904,
      "output_tokens": 724,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2668
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 938,
          "output_tokens": 724,
          "cache_read_input_tokens": 10904,
          "cache_creation_input_tokens": 2668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2668,
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

_source line 21 · 2026-05-11T23:56:03.342Z_

<details><summary>↩ Tool result · `toolu_01MaeRdLQdLSUJ4tdCPyHbhx`</summary>

```text
Based on the content provided:

**Venue & Year:** ICLR 2026 Conference

**Status:** The paper is accepted as a **Poster** presentation. The page explicitly states "ICLR 2026 Poster" in the submission details.

**Publication Date:** Published January 26, 2026; last modified April 11, 2026

**Submission Number:** 3519

The paper titled "TIPS: Turn-level Information-Potential Reward Shaping for Search-Augmented LLMs" demonstrates acceptance at a top-tier venue with a poster presentation slot at ICLR 2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "547c8510-b91d-4c45-975b-eb751d96e69b",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "a41b6c49438027517",
  "type": "user",
  "uuid": "5ad52c14-0e28-449b-bc2f-7be88439b151",
  "sourceToolAssistantUUID": "547c8510-b91d-4c45-975b-eb751d96e69b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-11T23:56:04.525Z_

<details><summary>↩ Tool result · `toolu_015sJKhocD4R5XZUTXJGSQNZ`</summary>

```text
# Paper Analysis: TIPS (arXiv:2603.22293)

**1) ICLR 2026 Submission Status:**
Not indicated in the provided content. The paper is submitted to arXiv on March 11, 2026, but no conference venue is mentioned.

**2) Formal PBRS (Potential-Based Reward Shaping):**
Yes. The abstract explicitly states the approach "leverages the potential-based reward shaping" to provide guidance.

**3) Teacher-Model Log-Likelihood as Potential:**
The abstract indicates the method assigns rewards based on "increased likelihood of the correct answer under a teacher model," suggesting teacher-model probability functions are core to the potential function, though the exact mathematical formulation isn't detailed in this excerpt.

**4) Application Domain:**
Designed specifically for QA and search tasks. The paper targets "open-domain question answering (QA)" with "search-augmented large language models" rather than interactive environments.

**5) Exact Numerical Results:**
For Qwen-2.5 7B Instruct model: "TIPS improves the average Exact Match score by 11.8% and F1 by 13.6% relative to PPO." Results evaluated across "seven QA benchmarks."

**6) Formal Reward Shaping Formulation:**
The specific mathematical formulation is not provided in this abstract. Only the conceptual approach of "turn-level rewards to each reasoning + tool-call segment" is described; detailed equations would require accessing the full paper PDF.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c6180c6-a2f2-4966-b933-d0b69127dd6f",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "a41b6c49438027517",
  "type": "user",
  "uuid": "f2f68a0d-817f-4262-9306-9f4b6730d815",
  "sourceToolAssistantUUID": "9c6180c6-a2f2-4966-b933-d0b69127dd6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-11T23:56:05.192Z_

<details><summary>↩ Tool result · `toolu_01LRrGaMN2SKXYjdEcyQiqp8`</summary>

```text
# Analysis of Self-Guide Paper on Reward Shaping and Policy Co-Evolution

## 1. Non-PBRS Bias and Potential-Based Reward Shaping

**Found:** The paper explicitly acknowledges non-potential-based reward shaping issues.

The authors state: "Because the self-guidance-derived reward is not potential-based, retaining it indefinitely would bias the converged policy away from the true environment objective."

This recognition motivates their Phase IV late annealing strategy, where internal reward contribution gradually reduces from 1 to 0 before convergence. The authors argue this ensures the terminal policy remains optimized primarily under environment rewards.

## 2. Citation of Ng et al. 1999

**Found:** Directly cited in Section 3.5.

The paper cites "Ng et al., [1999] Policy invariance under reward transformations: theory and application to reward shaping" when discussing why late annealing is necessary. This classic reference establishes the theoretical foundation for their concern about non-potential-based rewards.

## 3. Trapezoid Schedule and Annealing

**Found:** Comprehensive treatment provided.

The authors propose a four-phase trapezoid schedule (Equation 10):
- **Phase I:** Guidance-only (λ=0)
- **Phase II:** Linear ramp 0→1
- **Phase III:** Full strength (λ=1)
- **Phase IV:** Linear annealing 1→0

Ablation studies (Figure 5, Section 4.4) validate this structure, showing immediate full reward underperforms and no annealing degrades results.

## 4. Handling Policy Optimality Changes

**Found:** Addressed through staged activation and empirical validation.

The co-evolution chicken-and-egg problem is solved by: (1) warm-up before reward activation ensures self-guidance matures, (2) gradual Phase II ramp prevents optimization shock, and (3) Phase IV annealing ensures convergence toward true environment objectives. Figure 4 demonstrates this prevents the policy from becoming locked into suboptimal internal-reward-driven behavior.

## 5. Benchmark Results

**Found:** Comprehensive across three environments and three model scales.

On **ALFWorld** (Qwen3-4B): GRPO baseline 86.7% → GRPO w/ SG & GR 96.9% (+10.2%)

On **ScienceWorld** (Qwen3-4B): GRPO baseline 71.9% → 78.1% (+6.2%)

On **WebShop** (Qwen3-4B): GRPO baseline 84.3% → 87.8% (+3.5%)

Improvements consistent across smaller (1.7B) and larger (7B) models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45ca2266-65de-4efa-be6a-c1b6f2de2653",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "a41b6c49438027517",
  "type": "user",
  "uuid": "77443e1b-5c00-4b77-9a5e-62552ad262fa",
  "sourceToolAssistantUUID": "45ca2266-65de-4efa-be6a-c1b6f2de2653",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-11T23:56:08.135Z_

Excellent. Now let me fetch the full HTML of the TIPS paper to verify the specific claims about PBRS formulation and teacher-model log-likelihood.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77443e1b-5c00-4b77-9a5e-62552ad262fa",
  "isSidechain": true,
  "agentId": "a41b6c49438027517",
  "requestId": "req_011CawgioKyDbj6MrYYztjci",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45c2d4a0-a50a-408b-a747-b68c552c5405",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Et2GM3rD8ZTGQBujmaGXKs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 547,
      "cache_creation_input_tokens": 2602,
      "cache_read_input_tokens": 13572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2602,
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

_source line 25 · 2026-05-11T23:56:12.593Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TQcnsBNgSBBQNjhJbFePQF`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.22293v1",
  "prompt": "Find and report: 1) The exact mathematical formulation of the potential function - does it use teacher-model log-likelihood? What exactly is the potential function Phi? 2) Does it cite Ng et al. 1999 for PBRS? 3) Is the potential computed using log-likelihood of gold/correct answers under a teacher model? Or is it computed differently (e.g., using the policy model itself, or a frozen copy)? 4) Is it specifically for QA/search tasks or also for interactive environments like games or navigation? 5) The full list of benchmarks used. Report all mathematical and methodological details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45c2d4a0-a50a-408b-a747-b68c552c5405",
  "isSidechain": true,
  "agentId": "a41b6c49438027517",
  "requestId": "req_011CawgioKyDbj6MrYYztjci",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df307ba1-b3ef-41d9-94ad-68b1e969dfed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Et2GM3rD8ZTGQBujmaGXKs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 547,
      "cache_creation_input_tokens": 2602,
      "cache_read_input_tokens": 13572,
      "output_tokens": 258,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2602
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 547,
          "output_tokens": 258,
          "cache_read_input_tokens": 13572,
          "cache_creation_input_tokens": 2602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2602,
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

_source line 26 · 2026-05-11T23:56:20.863Z_

<details><summary>↩ Tool result · `toolu_01TQcnsBNgSBBQNjhJbFePQF`</summary>

```text
# TIPS: Turn-level Information-Potential Reward Shaping Analysis

## 1. Mathematical Formulation of the Potential Function

The potential function is explicitly defined as:

**Φ(S) := L(S;𝒜) = log ∑ₘ₌₁ᴹ p_teach(A⁽ᵐ⁾|S)**

This represents "the teacher's log-probability of generating _any_ correct answer." The turn-level reward is then:

**Δₖ = α[Φ(Sₖ) - Φ(Sₖ₋₁)]**

where Sₖ is "the context up to and including turn k" and α > 0 scales the reward magnitude.

## 2. Citation of Ng et al. 1999 for PBRS

Yes, the paper explicitly cites Ng et al. (1999) for potential-based reward shaping foundations. The authors state: "This signal can be viewed as a standard potential-based reward shaping term" and reference the classical PBRS framework multiple times throughout Section 3.2 and formal proofs in Appendix F.

## 3. Teacher Model for Potential Computation

The potential is computed using **a frozen copy of the policy model itself**, periodically refreshed. The paper states:

"We periodically refresh the teacher to prevent its beliefs from becoming stale and misaligned with the latest policy."

Ablation studies (Table 6) show that "the frozen policy is clearly best" compared to using different teacher models. This behavioral alignment is critical—using stronger but different models degraded performance.

## 4. Task Domain Specificity

This approach is specifically designed for **QA/search tasks with multi-turn tool use**, not general interactive environments. The framework targets "search-augmented large language models" for "open-domain question answering (QA)" where agents "interleave reasoning with retrieval."

## 5. Complete List of Benchmarks

**In-domain QA:**
- Natural Questions (NQ)
- HotpotQA

**Out-of-domain benchmarks:**
- TriviaQA
- PopQA
- 2WikiMultiHopQA
- MuSiQue
- Bamboogle

**Additional benchmark:**
- BrowseComp-Plus (Appendix B)

The paper evaluates across "seven in-domain and out-of-domain benchmarks" plus the deep-research benchmark for comprehensive assessment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df307ba1-b3ef-41d9-94ad-68b1e969dfed",
  "isSidechain": true,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "agentId": "a41b6c49438027517",
  "type": "user",
  "uuid": "184a14ee-acf8-40e3-aaa2-76f299812e0b",
  "sourceToolAssistantUUID": "df307ba1-b3ef-41d9-94ad-68b1e969dfed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-11T23:56:57.564Z_

Now I have all the information needed. Let me compile the full report.

---

## Paper 1: "Self-Guide: Co-Evolution of Policy and Internal Reward for Language Agents"

### Existence and Identity
**Confirmed to exist.** arXiv ID 2604.03098, submitted April 3, 2026. The method is explicitly called "Self-Guide" in the paper. Authors: Xinyu Wang, Hanwei Wu, Jingwei Song, Shuyuan Zhang, Jiayi Zhang, Fanqi Kong, Tung Sum Thomas Kwok, Xiao-Wen Chang, Yuyu Luo, Chenglin Wu, Bang Liu.

### Non-PBRS Bias Problem and Ng et al. 1999 Citation
**Yes to both.** The paper explicitly acknowledges the non-PBRS bias problem. It states: *"Because the self-guidance-derived reward is not potential-based, retaining it indefinitely would bias the converged policy away from the true environment objective."* It directly cites **Ng et al. (1999) "Policy invariance under reward transformations: theory and application to reward shaping"** in Section 3.5 as the theoretical foundation for why this bias matters.

### Trapezoid Annealing Schedule
**Yes, confirmed.** The paper proposes a four-phase "trapezoid schedule" (Equation 10) to withdraw internal rewards:
- **Phase I:** Guidance-only (lambda = 0)
- **Phase II:** Linear ramp from 0 to 1
- **Phase III:** Full strength (lambda = 1)
- **Phase IV:** Linear annealing from 1 to 0

Ablation studies (Figure 5, Section 4.4) validate this structure, showing that skipping annealing or using immediate full reward both degrade results.

### Results
Evaluated across three interactive agent benchmarks using GRPO, with Qwen3-4B:
- **ALFWorld:** 86.7% (GRPO baseline) -> 96.9% (+10.2%)
- **ScienceWorld:** 71.9% -> 78.1% (+6.2%)
- **WebShop:** 84.3% -> 87.8% (+3.5%)

Improvements are consistent across 1.7B, 4B, and 7B model scales. The overall improvement is approximately 8% over baselines trained solely with environment reward.

---

## Paper 2: "TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs"

### Existence and Venue
**Confirmed to exist and confirmed at ICLR 2026.** Accepted as an **ICLR 2026 Poster** (submission #3519). Published January 26, 2026 on OpenReview; arXiv preprint is 2603.22293. Authors: Yutao Xie, Nathaniel Thomas, Nicklas Hansen, Yang Fu, Li Erran Li, Xiaolong Wang (UCSD Wang Lab). Code available at `github.com/ucsd-wang-lab-lm/tips`.

### Formal PBRS with Teacher-Model Log-Likelihood
**Partially correct -- uses PBRS, but the "teacher model" is actually a frozen copy of the policy itself, not a separate teacher.** The potential function is formally defined as:

**Phi(S) := L(S; A) = log sum_{m=1}^{M} p_teach(A^(m) | S)**

This is the teacher's log-probability of generating any correct answer given context S. The turn-level reward is the difference in potential: **Delta_k = alpha * [Phi(S_k) - Phi(S_{k-1})]**.

The paper explicitly frames this as standard potential-based reward shaping and cites **Ng et al. (1999)** multiple times (Section 3.2 and Appendix F). However, the "teacher" is a **frozen copy of the policy model itself, periodically refreshed** -- not a separate, stronger teacher model. Ablation studies (Table 6) showed that using different/stronger teacher models actually degraded performance; the frozen policy copy worked best.

So: formal PBRS -- yes. Teacher-model log-likelihood over gold answers -- technically yes, but the "teacher" is a frozen self-copy, not an external teacher.

### Domain: QA/Search vs. Interactive Environments
**Confirmed: designed specifically for QA/search tasks, NOT interactive environments.** The framework targets "search-augmented large language models" for "open-domain question answering" where agents interleave reasoning with retrieval tool calls. This is fundamentally different from interactive environments like ALFWorld or WebShop (which Self-Guide targets).

### Results
Evaluated on seven QA benchmarks with Qwen-2.5-7B Instruct:
- **In-domain:** Natural Questions (NQ), HotpotQA
- **Out-of-domain:** TriviaQA, PopQA, 2WikiMultiHopQA, MuSiQue, Bamboogle
- **Additional:** BrowseComp-Plus

Performance: TIPS improves average Exact Match by **11.8%** and F1 by **13.6%** over PPO. It consistently outperforms both PPO and GRPO baselines and substantially improves training stability.

---

## Summary of Verification

| Claim | Verdict |
|-------|---------|
| Self-Guide exists at arXiv:2604.03098 (April 2026) | **TRUE** |
| Self-Guide acknowledges non-PBRS bias and cites Ng et al. 1999 | **TRUE** -- explicitly does both |
| Self-Guide uses trapezoid annealing schedule | **TRUE** -- four-phase trapezoid (Eq. 10) |
| TIPS exists at ICLR 2026 | **TRUE** -- accepted as poster |
| TIPS uses formal PBRS with teacher-model log-likelihood over gold answers | **MOSTLY TRUE** -- uses formal PBRS with log-likelihood of gold answers, but the "teacher" is a frozen self-copy, not a separate teacher model |
| TIPS is for QA/search rather than interactive environments | **TRUE** |

Sources:
- [Self-Guide on arXiv](https://arxiv.org/abs/2604.03098)
- [Self-Guide HTML version](https://arxiv.org/html/2604.03098)
- [TIPS on arXiv](https://arxiv.org/abs/2603.22293)
- [TIPS on OpenReview (ICLR 2026)](https://openreview.net/forum?id=eBMOr6a84z)
- [TIPS HTML version](https://arxiv.org/html/2603.22293v1)
- [TIPS GitHub repository](https://github.com/ucsd-wang-lab-lm/tips)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "184a14ee-acf8-40e3-aaa2-76f299812e0b",
  "isSidechain": true,
  "agentId": "a41b6c49438027517",
  "requestId": "req_011CawgjxLyJY7UDKUcSQLA1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7771bdfb-20ff-4736-8987-f4d69f956a10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eg6gmNHuNTEJq5ijnF6daC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1399,
      "cache_read_input_tokens": 16174,
      "output_tokens": 1661,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1399
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1661,
          "cache_read_input_tokens": 16174,
          "cache_creation_input_tokens": 1399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1399,
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
