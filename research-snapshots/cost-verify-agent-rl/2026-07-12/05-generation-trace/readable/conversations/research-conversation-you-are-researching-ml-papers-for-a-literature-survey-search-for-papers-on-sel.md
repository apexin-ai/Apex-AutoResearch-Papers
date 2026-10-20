# Research conversation: You are researching ML papers for a literature survey. Search for papers on "selective verification" or "adaptive comput

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a37b983625ac7a0da.jsonl`
- **Structured JSON:** [`fe4597386cb3bc85cff8.json`](../../sessions/fe/fe4597386cb3bc85cff8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

33 recorded events

### User

_source line 1 · 2026-05-14T04:34:10.527Z_

You are researching ML papers for a literature survey. Search for papers on "selective verification" or "adaptive computation allocation" in agent RL settings — specifically where an agent learns WHEN to do extra reasoning/verification steps during execution.

Use WebSearch to find 2-3 highly relevant papers (2023-2026). For each paper, record:
- Title, authors, year, venue
- Core method (1-2 sentences)
- arXiv link if available

Search queries to try:
1. "selective verification reinforcement learning agent"
2. "adaptive computation allocation LLM agent RL"
3. "learn when to verify agent reinforcement learning"
4. "adaptive inference budget language model agent"

Focus on papers where agents learn to allocate computation/verification adaptively, not just fixed-schedule verification. Return the findings in a structured format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "359c1439-b630-4437-9c0e-2b3bec18ea1d",
  "agentId": "a37b983625ac7a0da",
  "type": "user",
  "uuid": "8e260807-a09a-47b2-be3e-6d694f95d4d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T04:34:10.532Z_

```json
{
  "parentUuid": "8e260807-a09a-47b2-be3e-6d694f95d4d5",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
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
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "9a3d662b-94b6-4007-8b57-2ae836f86b2b",
  "timestamp": "2026-05-14T04:34:10.532Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T04:34:13.650Z_



I'll search for relevant papers using multiple queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a3d662b-94b6-4007-8b57-2ae836f86b2b",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qYaXpBFqQL7tKWhWHV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d5350d8-a263-4663-871b-3790a60afd4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwchLWvx4FmgpcVXqq9qqm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13305,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13305,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 4 · 2026-05-14T04:34:13.820Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Uy7RbPEU179Cy6MthPAmz5`</summary>

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
  "parentUuid": "0d5350d8-a263-4663-871b-3790a60afd4b",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qYaXpBFqQL7tKWhWHV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbbedf58-f1ea-4f05-9a97-4dee7f2264d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwchLWvx4FmgpcVXqq9qqm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13305,
      "cache_read_input_tokens": 0,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13305
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 87,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 13305,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13305,
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

_source line 5 · 2026-05-14T04:34:13.830Z_

<details><summary>↩ Tool result · `toolu_01Uy7RbPEU179Cy6MthPAmz5`</summary>

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
  "parentUuid": "bbbedf58-f1ea-4f05-9a97-4dee7f2264d5",
  "isSidechain": true,
  "promptId": "359c1439-b630-4437-9c0e-2b3bec18ea1d",
  "agentId": "a37b983625ac7a0da",
  "type": "user",
  "uuid": "889085cb-f38b-4b70-93b6-1d4c482cc420",
  "sourceToolAssistantUUID": "bbbedf58-f1ea-4f05-9a97-4dee7f2264d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T04:34:17.235Z_



Running all four search queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "889085cb-f38b-4b70-93b6-1d4c482cc420",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qYpiqUTKaz2hteQKgJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0ce80dc-26ff-4464-8edc-b25caad7c1a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAGWooCy6CqXxAudwJXi3q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 13305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 7 · 2026-05-14T04:34:17.719Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FM9kG5CchHYB7niATesdqn`</summary>

```json
{
  "query": "selective verification reinforcement learning agent LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0ce80dc-26ff-4464-8edc-b25caad7c1a4",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qYpiqUTKaz2hteQKgJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24177b89-c6ac-466d-aece-89a764e395d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAGWooCy6CqXxAudwJXi3q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 13305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 8 · 2026-05-14T04:34:18.847Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011tCk8WAgcB6NMqcTXSiRBP`</summary>

```json
{
  "query": "adaptive computation allocation LLM agent RL learn when to verify"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24177b89-c6ac-466d-aece-89a764e395d5",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qYpiqUTKaz2hteQKgJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "716450a2-9451-4382-90df-567929c2f3ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAGWooCy6CqXxAudwJXi3q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 13305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 9 · 2026-05-14T04:34:19.190Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014M7WEJU2vKzVBdWNjBGQiq`</summary>

```json
{
  "query": "adaptive inference budget language model agent reinforcement learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "716450a2-9451-4382-90df-567929c2f3ef",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qYpiqUTKaz2hteQKgJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "414e16a1-d630-4092-8d11-3f387b6235f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAGWooCy6CqXxAudwJXi3q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 13305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1451,
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

_source line 10 · 2026-05-14T04:34:19.938Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CevW7DeLq5V7B3ncG4uGbm`</summary>

```json
{
  "query": "learn when to think more LLM adaptive reasoning verification RL training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "414e16a1-d630-4092-8d11-3f387b6235f1",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qYpiqUTKaz2hteQKgJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4936daa5-98ce-422e-a6be-ee2f96b813c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAGWooCy6CqXxAudwJXi3q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1451,
      "cache_read_input_tokens": 13305,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1451
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 220,
          "cache_read_input_tokens": 13305,
          "cache_creation_input_tokens": 1451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1451,
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

_source line 11 · 2026-05-14T04:34:25.684Z_

<details><summary>↩ Tool result · `toolu_01FM9kG5CchHYB7niATesdqn`</summary>

```text
Web search results for query: "selective verification reinforcement learning agent LLM 2024 2025"

Links: [{"title":"GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-RLVR"},{"title":"Reinforcement Learning for LLM Agent Planning","url":"https://aclanthology.org/2025.emnlp-industry.116.pdf"},{"title":"GitHub - benjaminzwhite/reasoning-models: Experiments with reasoning models, training techniques, papers · GitHub","url":"https://github.com/benjaminzwhite/reasoning-models"},{"title":"Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning","url":"https://arxiv.org/html/2511.14460v1"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"Reinforcement Learning for Safe LLM Code Generation Roy Huang","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-123.pdf"},{"title":"Tree Search for LLM Agent Reinforcement Learning","url":"https://arxiv.org/pdf/2509.21240"},{"title":"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs | OpenReview","url":"https://openreview.net/forum?id=jGbRWwIidy"},{"title":"A Brief Overview: Agentic Reinforcement Learning In Large Language Models","url":"https://arxiv.org/html/2604.27859v2"},{"title":"How Top AI Labs Are Building RL Agents in 2026","url":"https://blog.dailydoseofds.com/p/how-top-ai-labs-are-building-rl-agents"}]

Based on the search results, here's what I found about selective verification and reinforcement learning with agents and LLMs in 2024-2025:

## Key Research Areas

**Reinforcement Learning with Verifiable Rewards (RLVR)**

RLVR with GRPO became the dominant approach for training reasoning models through 2025, with every major lab releasing a reasoning variant following this recipe. Research uses binary, verifiable reward functions to inject precise, unbiased learning signals into RL pipelines for math, code, and other accuracy-critical tasks.

Recent advancements in long chain-of-thought (CoT) reasoning, particularly through the Group Relative Policy Optimization algorithm used by DeepSeek-R1, have led to significant interest in RLVR for LLMs, while there remains debate over whether it truly enhances reasoning abilities or simply boosts sampling efficiency.

**Verification and Agent Planning**

DeepSeekMath-V2 investigates how to train an accurate and faithful LLM-based verifier for theorem proving, trains a proof generator using the verifier as the reward model, and scales verification compute to automatically label new hard-to-verify proofs.

**Agentic RL Frameworks**

Agent-R1 is a modular, flexible, and user-friendly training framework for RL-based LLM Agents, designed for straightforward adaptation across diverse task scenarios and interactive environments.

Recent work explores tree-based exploration with branching at high-uncertainty steps for lookahead tree-based rollouts for enhanced trajectory-level exploration in reinforcement learning with verifiable rewards.

These developments represent significant progress in making LLM agents more capable through selective verification mechanisms and sophisticated RL approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24177b89-c6ac-466d-aece-89a764e395d5",
  "isSidechain": true,
  "promptId": "359c1439-b630-4437-9c0e-2b3bec18ea1d",
  "agentId": "a37b983625ac7a0da",
  "type": "user",
  "uuid": "68bc71d7-197a-488c-9245-0501b1ae47b5",
  "sourceToolAssistantUUID": "24177b89-c6ac-466d-aece-89a764e395d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T04:34:26.755Z_

<details><summary>↩ Tool result · `toolu_011tCk8WAgcB6NMqcTXSiRBP`</summary>

```text
Web search results for query: "adaptive computation allocation LLM agent RL learn when to verify"

Links: [{"title":"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning","url":"https://arxiv.org/html/2505.11274v6"},{"title":"Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents","url":"https://arxiv.org/html/2509.03581v1"},{"title":"Agentic Reasoning and Tool Integration for LLMs via Reinforcement Learning","url":"https://arxiv.org/pdf/2505.01441"},{"title":"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints | OpenReview","url":"https://openreview.net/forum?id=JMDCMf7mlF"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"Learning How Hard to Think: Input-Adaptive Allocation of LM Computation | OpenReview","url":"https://openreview.net/forum?id=6qUUgw9bAZ"},{"title":"Multi-Agent Reinforcement Learning for Adaptive Resource ...","url":"https://dl.acm.org/doi/pdf/10.1145/3772726.3772833"},{"title":"e1: Learning Adaptive Control of Reasoning Effort","url":"https://arxiv.org/pdf/2510.27042"},{"title":"Learning How Hard to Think: Input-Adaptive Allocation of LM Computation","url":"https://arxiv.org/html/2410.04707v1"},{"title":"Tutorial on Large Language Model-Enhanced ...","url":"https://arxiv.org/pdf/2512.03722"}]

Based on the web search results, I found several highly relevant papers on adaptive computation allocation for LLM agents that involve learning when to verify:

## Key Research on Adaptive Computation Allocation

One paper introduces a conceptual framework for dynamic planning for LLM agents that enables them to flexibly decide when to allocate test-time compute for planning, using a two-stage training pipeline: supervised fine-tuning on diverse synthetic data to prime models for dynamic planning, and RL to refine this capability in long-horizon environments. This is claimed to be the first work to explore training LLM agents for dynamic test-time compute allocation in sequential decision-making tasks.

Another framework called Anytime Verified Agents (AVA) dynamically allocates compute across search, sampling, and verification within a user-specified budget, combining calibrated uncertainty estimation, value-of-information-guided search expansion, and selective verification cascades with early exits.

Additional research presents an approach that predicts the distribution of rewards given an input and computation budget, then allocates additional computation to inputs for which it is predicted to be most useful, applying this in adaptive best-of-k procedures and routing procedures that dynamically select between expensive but accurate or cheaper but less capable decoding procedures.

There's also work on SelfBudgeter, which uses RL training where the model learns to allocate token budgets dynamically based on question difficulty, with the model first estimating the required token budget before providing the answer.

These papers collectively address the problem of learning when to verify and allocate computational resources adaptively in LLM agents through reinforcement learning approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "716450a2-9451-4382-90df-567929c2f3ef",
  "isSidechain": true,
  "promptId": "359c1439-b630-4437-9c0e-2b3bec18ea1d",
  "agentId": "a37b983625ac7a0da",
  "type": "user",
  "uuid": "b9e47e10-7c0f-4236-9cbd-0568c36fce8b",
  "sourceToolAssistantUUID": "716450a2-9451-4382-90df-567929c2f3ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T04:34:26.954Z_

<details><summary>↩ Tool result · `toolu_014M7WEJU2vKzVBdWNjBGQiq`</summary>

```text
Web search results for query: "adaptive inference budget language model agent reinforcement learning 2024 2025"

Links: [{"title":"Controlling Performance and Budget of a Centralized Multi-agent LLM System with Reinforcement Learning","url":"https://arxiv.org/html/2511.02755v1"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"Reinforcement Learning for LLM Agent Planning","url":"https://aclanthology.org/2025.emnlp-industry.116.pdf"},{"title":"Language Model Guided Reinforcement Learning in Quantitative TradingPreprint under review for FLLM 2025.","url":"https://arxiv.org/html/2508.02366v1"},{"title":"Inference Budget","url":"https://www.aussieai.com/research/inference-budget"},{"title":"Reinforcement Learning Meets Large Language Models: A Survey of","url":"https://arxiv.org/pdf/2509.16679"},{"title":"L2M2: A Hierarchical Framework Integrating Large Language Model and","url":"https://www.ijcai.org/proceedings/2025/0012.pdf"},{"title":"Efficient Agents: Building Effective Agents While Reducing Cost","url":"https://arxiv.org/html/2508.02694v1"},{"title":"Published as a conference paper at ICLR 2026 TOWARD EFFICIENT EXPLORATION","url":"https://dilipa.github.io/papers/iclr26_psrl_llms.pdf"},{"title":"Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning","url":"https://arxiv.org/html/2511.14460v1"}]

I've successfully performed the web search on "adaptive inference budget language model agent reinforcement learning 2024 2025". Here are the key findings:

## Search Results Summary

The search returned highly relevant research spanning 2024-2025 that addresses multiple aspects of your query:

**Cost-Controllable Multi-LLM Systems:**
A reinforcement learning-based framework enables intelligent dispatch of queries to suitable expert models with dynamic control over inference behavior ranging from low-budget to high-budget modes.

**Adaptive Inference Budgets:**
An inference budget is a type of adaptive inference as an LLM inference optimization, whereby the processing of a query is given a "budget" that specifies how much processing can be used to compute the answer.

**RL for Language Model Agents:**
Reinforcement learning is considered key for training LLM agents, though the field still lacks in-depth exploration of RL approaches tailored for LLM agents; a modular framework called Agent-R1 was introduced for RL-based LLM agent training.

**Recent Developments in Agentic RL:**
Selective rollout strategies are used to optimize compute budget in reinforcement learning training, and starting around 2024, advanced LLMs like OpenAI's o1, Anthropic's Claude, DeepSeek R1, and Qwen 3 have demonstrated substantial improvements on complex reasoning tasks by employing test-time or post-training RL techniques.

**Tool-Use Optimization:**
Tool-use completeness rewards are computed for planners' action sequences, with the planner's tool use optimized through multi-turn reinforcement learning.

The research shows an active area of development in 2024-2025 combining budget-aware inference, multi-agent LLM systems, and reinforcement learning techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "414e16a1-d630-4092-8d11-3f387b6235f1",
  "isSidechain": true,
  "promptId": "359c1439-b630-4437-9c0e-2b3bec18ea1d",
  "agentId": "a37b983625ac7a0da",
  "type": "user",
  "uuid": "b5454e8f-38e4-4876-86fd-ee2869139cef",
  "sourceToolAssistantUUID": "414e16a1-d630-4092-8d11-3f387b6235f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T04:34:28.960Z_

<details><summary>↩ Tool result · `toolu_01CevW7DeLq5V7B3ncG4uGbm`</summary>

```text
Web search results for query: "learn when to think more LLM adaptive reasoning verification RL training"

Links: [{"title":"The State of Reinforcement Learning for LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"},{"title":"GitHub - Eclipsess/Awesome-Efficient-Reasoning-LLMs: [TMLR 2025] Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models · GitHub","url":"https://github.com/Eclipsess/Awesome-Efficient-Reasoning-LLMs"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning | Nature","url":"https://www.nature.com/articles/s41586-025-09422-z"},{"title":"Thinkless: LLM Learns When to Think","url":"https://arxiv.org/html/2505.13379v1"},{"title":"Demystifying Reasoning Models - by Cameron R. Wolfe, Ph.D.","url":"https://cameronrwolfe.substack.com/p/demystifying-reasoning-models"},{"title":"DeepSeek-R1: Advancing LLM Reasoning with Reinforcement Learning | by Shirley Li | Data Science Collective | Medium","url":"https://medium.com/data-science-collective/deepseek-r1-advancing-llm-reasoning-with-reinforcement-learning-3c09a4327778"},{"title":"Correct, Concise and Complete: Multi-stage Training For Adaptive Reasoning","url":"https://arxiv.org/html/2601.02972"},{"title":"Understanding Reasoning LLMs - by Sebastian Raschka, PhD","url":"https://magazine.sebastianraschka.com/p/understanding-reasoning-llms"},{"title":"Taming the Long-Tail: Efficient Reasoning RL Training with Adaptive Drafter","url":"https://arxiv.org/html/2511.16665v1"},{"title":"GitHub - benjaminzwhite/reasoning-models: Experiments with reasoning models, training techniques, papers · GitHub","url":"https://github.com/benjaminzwhite/reasoning-models"}]

Based on the search results, here are the key findings related to "learn when to think" for LLMs with adaptive reasoning, verification, and RL training:

## Key Research Areas

A learnable framework like Thinkless empowers an LLM to adaptively select between short-form and long-form reasoning, based on both task complexity and the model's ability. Thinkless is trained under a reinforcement learning paradigm and employs two control tokens, &lt;short> for concise responses and &lt;think> for detailed reasoning.

The core method uses a Decoupled Group Relative Policy Optimization (DeGRPO) algorithm, which decomposes the learning objective of hybrid reasoning into two components: (1) a control token loss that governs the selection of the reasoning mode, and (2) a response loss that improves the accuracy of the generated answers.

## Verification-Based RL Training

Reinforcement learning with verifiable rewards (RLVR) is an approach where instead of relying on human preferences and training a reward model, models use verifiable rewards. The model gets direct binary feedback (correct or wrong) from a deterministic tool, such as symbolic verifiers or rule-based tools.

## Addressing "Overthinking"

CoT often becomes unnecessarily long, increasing computation cost without actual accuracy gains or sometimes even degrading performance, a phenomenon known as "overthinking". Rather than using a manually fixed "thinking budget" shared across all inputs, models are trained to produce short yet complete reasoning traces while preserving accuracy by incentivizing the model to adaptively infer an input-dependent budget.

The research demonstrates that on the Minerva Algebra dataset, adaptive reasoning approaches activate the reasoning mode for only 25% of the samples, reducing token usage to one-third of the original, while maintaining performance within a 1% margin.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4936daa5-98ce-422e-a6be-ee2f96b813c5",
  "isSidechain": true,
  "promptId": "359c1439-b630-4437-9c0e-2b3bec18ea1d",
  "agentId": "a37b983625ac7a0da",
  "type": "user",
  "uuid": "53f11f20-1c80-41eb-a9e6-92721b2e3446",
  "sourceToolAssistantUUID": "4936daa5-98ce-422e-a6be-ee2f96b813c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-14T04:34:31.513Z_

Good results. Let me now get more details on the most relevant papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53f11f20-1c80-41eb-a9e6-92721b2e3446",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qZwJW1MfEXtMV7Nygg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31f67ac6-b61d-4205-84b9-b6afa65a7d6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZcSCe5w96sPJnqnVphjkH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3944,
      "cache_read_input_tokens": 14756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3944,
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

_source line 16 · 2026-05-14T04:34:32.617Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HtyoJqV3SkgwUJy3VUvP6R`</summary>

```json
{
  "query": "arxiv \"Learning When to Plan\" adaptive compute allocation LLM agents test-time 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31f67ac6-b61d-4205-84b9-b6afa65a7d6f",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qZwJW1MfEXtMV7Nygg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7de9299-51ab-4f55-930f-1a37b4dc18a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZcSCe5w96sPJnqnVphjkH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3944,
      "cache_read_input_tokens": 14756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3944,
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

_source line 17 · 2026-05-14T04:34:33.568Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013iyqJaHw1rkGDm9ASCWSpi`</summary>

```json
{
  "query": "arxiv \"Anytime Verified Agents\" adaptive compute verified reasoning budget constraints"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7de9299-51ab-4f55-930f-1a37b4dc18a6",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qZwJW1MfEXtMV7Nygg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f7e4679c-8ecf-4373-9658-f830d25c061f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZcSCe5w96sPJnqnVphjkH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3944,
      "cache_read_input_tokens": 14756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3944,
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

_source line 18 · 2026-05-14T04:34:33.872Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rnkm1fP8oW5QiuDTYYjqWa`</summary>

```json
{
  "query": "arxiv \"Thinkless LLM Learns When to Think\" 2025 adaptive reasoning mode"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7e4679c-8ecf-4373-9658-f830d25c061f",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qZwJW1MfEXtMV7Nygg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28663423-0563-4491-b623-e9be5485e256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZcSCe5w96sPJnqnVphjkH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3944,
      "cache_read_input_tokens": 14756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3944,
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

_source line 19 · 2026-05-14T04:34:34.334Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MLqRx9mp65uT2B4T5P5eeq`</summary>

```json
{
  "query": "arxiv \"Learning How Hard to Think\" input-adaptive allocation LM computation 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28663423-0563-4491-b623-e9be5485e256",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qZwJW1MfEXtMV7Nygg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4179cce9-0b3c-418c-8c39-1ff8b35646c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZcSCe5w96sPJnqnVphjkH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3944,
      "cache_read_input_tokens": 14756,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3944
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 14756,
          "cache_creation_input_tokens": 3944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3944,
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

_source line 20 · 2026-05-14T04:34:39.351Z_

<details><summary>↩ Tool result · `toolu_01HtyoJqV3SkgwUJy3VUvP6R`</summary>

```text
Web search results for query: "arxiv "Learning When to Plan" adaptive compute allocation LLM agents test-time 2025"

Links: [{"title":"[2509.03581] Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents","url":"https://arxiv.org/abs/2509.03581"},{"title":"Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents","url":"https://arxiv.org/html/2509.03581"},{"title":"What If We Allocate Test-Time Compute Adaptively?","url":"https://arxiv.org/html/2602.01070"},{"title":"Same Signal, Opposite Meaning: Direction-Informed Adaptive Learning for LLM Agents","url":"https://arxiv.org/html/2605.06908"},{"title":"GitHub - yxf203/Awesome-Efficient-Agents: Survey and paper list on efficiency-guided LLM agents (memory, tool learning, planning). · GitHub","url":"https://github.com/yxf203/Awesome-Efficient-Agents"},{"title":"(PDF) Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents","url":"https://www.researchgate.net/publication/395270414_Learning_When_to_Plan_Efficiently_Allocating_Test-Time_Compute_for_LLM_Agents"}]

I found the paper you're searching for! Here are the key details:

## "Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents"

This work is the first to explore training LLM agents for dynamic test-time compute allocation in sequential decision-making tasks, paving the way for more efficient, adaptive, and controllable agentic systems.

**Core Problem:**
Existing methods like ReAct prompt LLMs to explicitly plan before every action; however, always planning is computationally expensive and degrades performance on long-horizon tasks, while never planning further limits performance.

**Proposed Solution:**
The authors introduce a conceptual framework formalizing dynamic planning for LLM agents, enabling them to flexibly decide when to allocate test-time compute for planning. They propose a simple two-stage training pipeline: (1) supervised fine-tuning on diverse synthetic data to prime models for dynamic planning, and (2) RL to refine this capability in long-horizon environments.

**Results:**
Experiments on the Crafter environment show that dynamic planning agents trained with this approach are more sample-efficient and consistently achieve more complex objectives. Additionally, the authors demonstrate that these agents can be effectively steered by human-written plans, surpassing their independent capabilities.

**Paper Details:**
- ArXiv ID: 2509.03581
- First version: September 3, 2025
- Latest version: September 30, 2025


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7de9299-51ab-4f55-930f-1a37b4dc18a6",
  "isSidechain": true,
  "promptId": "359c1439-b630-4437-9c0e-2b3bec18ea1d",
  "agentId": "a37b983625ac7a0da",
  "type": "user",
  "uuid": "8c486d9a-bcef-45a7-a295-335bf44ab53b",
  "sourceToolAssistantUUID": "e7de9299-51ab-4f55-930f-1a37b4dc18a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T04:34:39.881Z_

<details><summary>↩ Tool result · `toolu_013iyqJaHw1rkGDm9ASCWSpi`</summary>

```text
Web search results for query: "arxiv "Anytime Verified Agents" adaptive compute verified reasoning budget constraints"

Links: [{"title":"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints | OpenReview","url":"https://openreview.net/forum?id=JMDCMf7mlF"},{"title":"Budget-Aware Anytime Reasoning with LLM-Synthesized Preference Data","url":"https://arxiv.org/html/2601.11038"},{"title":"Optimizing Anytime Reasoning via Budget Relative Policy Optimization","url":"https://arxiv.org/html/2505.13438"},{"title":"[2505.13438] Optimizing Anytime Reasoning via Budget Relative Policy Optimization","url":"https://arxiv.org/abs/2505.13438"},{"title":"[2505.13438v1] Optimizing Anytime Reasoning via Budget Relative Policy Optimization","url":"http://arxiv.org/abs/2505.13438v1"},{"title":"Budget-Aware Tool-Use Enables Effective Agent Scaling","url":"https://arxiv.org/html/2511.17006v1"},{"title":"What If We Allocate Test-Time Compute Adaptively?","url":"https://arxiv.org/html/2602.01070"},{"title":"Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs","url":"https://arxiv.org/html/2507.02076v1"},{"title":"Budget-aware Test-time Scaling via Discriminative Verification","url":"https://arxiv.org/html/2510.14913v1"},{"title":"Optimizing Anytime Reasoning via Budget Relative Policy Optimization - Paper Detail","url":"https://deeplearn.org/arxiv/606111/optimizing-anytime-reasoning-via-budget-relative-policy-optimization"}]

Based on the web search results, I found several papers related to anytime reasoning and verified agents with adaptive compute and budget constraints:

## Primary Result: Anytime Verified Agents (AVA)

Anytime Verified Agents (AVA) is a framework that dynamically allocates compute across search, sampling, and verification within a user-specified budget, with an extensible interface for tool use. Existing methods allocate computational resources using static strategies such as fixed search depths, constant self-consistency sampling, or uniform verification, so simple problems can consume as much compute as complex tasks.

AVA combines calibrated uncertainty estimation, value-of-information-guided search expansion, and selective verification cascades with early exits. The controller allocates compute based on uncertainty and estimated marginal reliability gains.

## Related Work

The search also returned several complementary papers on adaptive compute and budget-aware reasoning:

1. **AnytimeReasoner**: A novel framework for optimizing reasoning performance under varying thinking budget constraints.

2. **Budget-Aware Test-Time Scaling (BATS)**: An advanced framework that leverages budget awareness to dynamically adapt its planning and verification strategy, deciding whether to "dig deeper" on a promising lead or "pivot" to new paths based on remaining resources.

3. **Adaptive Allocation Framework**: A verifier-guided adaptive framework treating reasoning as iterative trajectory generation and selection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7e4679c-8ecf-4373-9658-f830d25c061f",
  "isSidechain": true,
  "promptId": "359c1439-b630-4437-9c0e-2b3bec18ea1d",
  "agentId": "a37b983625ac7a0da",
  "type": "user",
  "uuid": "0453f2c3-9682-4129-870d-e1b8a1e9fb40",
  "sourceToolAssistantUUID": "f7e4679c-8ecf-4373-9658-f830d25c061f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T04:34:40.681Z_

<details><summary>↩ Tool result · `toolu_01MLqRx9mp65uT2B4T5P5eeq`</summary>

```text
Web search results for query: "arxiv "Learning How Hard to Think" input-adaptive allocation LM computation 2024"

Links: [{"title":"[2410.04707] Learning How Hard to Think: Input-Adaptive Allocation of LM Computation","url":"https://arxiv.org/abs/2410.04707"},{"title":"Learning How Hard to Think: Input-Adaptive Allocation of LM Computation","url":"https://arxiv.org/html/2410.04707v1"},{"title":"Latency and Token-Aware Test-Time Compute","url":"https://arxiv.org/html/2509.09864v1"},{"title":"Learning How Hard to Think: Input-Adaptive Allocation of LM Computation | OpenReview","url":"https://openreview.net/forum?id=6qUUgw9bAZ"},{"title":"Trade-offs in Large Reasoning Models: An Empirical Analysis of Deliberative and Adaptive Reasoning over Foundational Capabilities","url":"https://arxiv.org/html/2503.17979v1"},{"title":"Make Every Penny Count: Difficulty-Adaptive Self-Consistency for Cost-Efficient Reasoning","url":"https://arxiv.org/html/2408.13457v3"},{"title":"Test-time Computing: from System-1 Thinking to System-2 Thinking","url":"https://arxiv.org/html/2501.02497v1"},{"title":"AdaBoN: Adaptive Best-of-𝑁 Alignment","url":"https://arxiv.org/html/2505.12050"},{"title":"Published as a conference paper at ICLR 2025 LEARNING HOW HARD TO THINK:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ff414825df833edb8b1839e3d5d495e9-Paper-Conference.pdf"},{"title":"Learning How Hard to Think: Input-Adaptive Allocation of LM Computation | Andi Peng","url":"https://andipeng.com/publication/2025-iclr-adaptivecompute/"}]

I found the paper you're looking for! Here are the key details:

## Paper Information

**Title:** "Learning How Hard to Think: Input-Adaptive Allocation of LM Computation"

**arXiv ID:** 2410.04707

**Authors:** Mehul Damani, Idan Shenfeld, Andi Peng, Andreea Bobu, Jacob Andreas

**Publication Date:** October 2024

## Main Contribution

The paper presents an approach that predicts the distribution of rewards given an input and computation budget, then allocates additional computation to inputs for which it is predicted to be most useful.

## Key Results

Across a suite of programming, mathematics, and dialog tasks, the paper shows that accurate computation-allocation procedures can be learned, and reduce computation by up to 50% at no cost to response quality, or improve quality by up to 10% at a fixed computational budget.

## Applications

The approach is applied in two decoding procedures: first, an adaptive best-of-k procedure that dynamically selects the number of samples to generate as input to a reranker; second, a routing procedure that dynamically responds to a query using a decoding procedure that is expensive but accurate, or one that is cheaper but less capable.

The paper has been published at ICLR 2025 and is available on arxiv.org.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4179cce9-0b3c-418c-8c39-1ff8b35646c9",
  "isSidechain": true,
  "promptId": "359c1439-b630-4437-9c0e-2b3bec18ea1d",
  "agentId": "a37b983625ac7a0da",
  "type": "user",
  "uuid": "1ff7447c-1a8b-4ad8-b37a-c9d9d4bce1b7",
  "sourceToolAssistantUUID": "4179cce9-0b3c-418c-8c39-1ff8b35646c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T04:34:41.394Z_

<details><summary>↩ Tool result · `toolu_01Rnkm1fP8oW5QiuDTYYjqWa`</summary>

```text
Web search results for query: "arxiv "Thinkless LLM Learns When to Think" 2025 adaptive reasoning mode"

No links found.

The search returned no results. Let me try a modified search:

Links: [{"title":"[2505.13379] Thinkless: LLM Learns When to Think","url":"https://arxiv.org/abs/2505.13379"},{"title":"arXiv:2505.13379v2 [cs.CL] 26 Jun 2025 Thinkless: LLM Learns When to Think","url":"https://arxiv.org/pdf/2505.13379"},{"title":"GitHub - VainF/Thinkless: [NeurIPS 2025] Thinkless: LLM Learns When to Think · GitHub","url":"https://github.com/VainF/Thinkless"},{"title":"Thinkless: LLM Learns When to Think","url":"https://arxiv.org/html/2505.13379v1"},{"title":"[2505.13379v2] Thinkless: LLM Learns When to Think","url":"https://arxiv.org/abs/2505.13379v2"},{"title":"[2505.13379v1] Thinkless: LLM Learns When to Think","url":"https://arxiv.org/abs/2505.13379v1"},{"title":"Thinkless: LLM Learns When to Think | OpenReview","url":"https://openreview.net/forum?id=ariVQf0KZx"},{"title":"Paper page - Thinkless: LLM Learns When to Think","url":"https://huggingface.co/papers/2505.13379"},{"title":"DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference","url":"https://arxiv.org/html/2510.19669"},{"title":"LLM Research Papers: The 2025 List (January to June)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-list-one"}]

I found the paper! Here's what I discovered about "Thinkless: LLM Learns When to Think":

## Overview

Thinkless is a learnable framework that empowers an LLM to adaptively select between short-form and long-form reasoning, based on both task complexity and the model's ability.

## Technical Approach

Thinkless is trained under a reinforcement learning paradigm and employs two control tokens, for concise responses and for detailed reasoning. At the core of the method is a Decoupled Group Relative Policy Optimization (DeGRPO) algorithm, which decomposes the learning objective of hybrid reasoning into two components: (1) a control token loss that governs the selection of the reasoning mode, and (2) a response loss that improves the accuracy of the generated answers.

## Performance

On several benchmarks such as Minerva Algebra, MATH-500, and GSM8K, Thinkless is able to reduce the usage of long-chain thinking by 50% - 90%, significantly improving the efficiency of Reasoning Language Models.

## Publication

The paper was published on arXiv (ID: 2505.13379) and was accepted to NeurIPS 2025 as a poster.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28663423-0563-4491-b623-e9be5485e256",
  "isSidechain": true,
  "promptId": "359c1439-b630-4437-9c0e-2b3bec18ea1d",
  "agentId": "a37b983625ac7a0da",
  "type": "user",
  "uuid": "ae2d786e-74da-42ce-8f2f-76802186655b",
  "sourceToolAssistantUUID": "28663423-0563-4491-b623-e9be5485e256",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-14T04:34:43.906Z_

Now let me get the exact author lists and venue information for the top papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae2d786e-74da-42ce-8f2f-76802186655b",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qarTKvHxRpQZSTBYyC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "47d14aa0-7928-44f7-bf8c-698417a05b57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRmZr6UYi6aB36rsUkVPTE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 866,
      "cache_creation_input_tokens": 2730,
      "cache_read_input_tokens": 18700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2730,
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

_source line 25 · 2026-05-14T04:34:44.862Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H5ByPBFvios2Ts24DY6Hpb`</summary>

```json
{
  "query": "arxiv 2509.03581 \"Learning When to Plan\" authors venue conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47d14aa0-7928-44f7-bf8c-698417a05b57",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qarTKvHxRpQZSTBYyC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f419822-7c28-4892-8470-040417a04b57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRmZr6UYi6aB36rsUkVPTE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 866,
      "cache_creation_input_tokens": 2730,
      "cache_read_input_tokens": 18700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2730,
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

_source line 26 · 2026-05-14T04:34:45.867Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012EtDUC9aC8GpTKuuNCehLH`</summary>

```json
{
  "query": "\"Anytime Verified Agents\" AVA authors arxiv 2025 2026 adaptive compute verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f419822-7c28-4892-8470-040417a04b57",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qarTKvHxRpQZSTBYyC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0ddfb744-93c6-493e-bccf-8f994429cb91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRmZr6UYi6aB36rsUkVPTE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 866,
      "cache_creation_input_tokens": 2730,
      "cache_read_input_tokens": 18700,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2730
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 866,
          "output_tokens": 144,
          "cache_read_input_tokens": 18700,
          "cache_creation_input_tokens": 2730,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2730,
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

_source line 27 · 2026-05-14T04:34:50.323Z_

<details><summary>↩ Tool result · `toolu_01H5ByPBFvios2Ts24DY6Hpb`</summary>

```text
Web search results for query: "arxiv 2509.03581 "Learning When to Plan" authors venue conference"

Links: [{"title":"[2509.03581] Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents","url":"https://arxiv.org/abs/2509.03581"},{"title":"Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents","url":"https://arxiv.org/html/2509.03581"},{"title":"(PDF) Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents","url":"https://www.researchgate.net/publication/395270414_Learning_When_to_Plan_Efficiently_Allocating_Test-Time_Compute_for_LLM_Agents"},{"title":"Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents","url":"https://arxiviq.substack.com/p/learning-when-to-plan-efficiently"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=3125&show=2000"},{"title":"Planning with a Learned Policy Basis to Optimally Solve Complex Tasks","url":"https://arxiv.org/html/2403.15301v1"},{"title":"1 Introduction","url":"https://arxiv.org/html/2406.14777v1"},{"title":"[2509.10303] Generalizing Beyond Suboptimality: Offline Reinforcement Learning Learns Effective Scheduling through Random Data","url":"https://arxiv.org/abs/2509.10303"},{"title":"Computer Science Jun 2023","url":"https://arxiv.org/list/cs/2023-06?skip=1650&show=25"},{"title":"Active Learning by Learning","url":"https://cdn.aaai.org/ojs/9597/9597-13-13125-1-2-20201228.pdf"}]

Based on the search results, here is the information about arxiv 2509.03581:

**Paper Title:** "Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents"

**Authors:** Davide Paglieri, Bartłomiej Cupiał, Jonathan Cook, Ulyana Piterbarg, Jens Tuyls, Edward Grefenstette, Jakob Nicolaus Foerster, Jack Parker-Holder, Tim Rocktäschel

**Submission Date:** Submitted on 3 Sep 2025 (v1), last revised 30 Sep 2025 (v2)

**Category/Venue:** arXiv:2509.03581v1 [cs.AI] (Computer Science - Artificial Intelligence)

**Note:** This is an arXiv preprint, so it has not yet been published at a peer-reviewed conference venue. The search results do not indicate acceptance to any specific conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f419822-7c28-4892-8470-040417a04b57",
  "isSidechain": true,
  "promptId": "359c1439-b630-4437-9c0e-2b3bec18ea1d",
  "agentId": "a37b983625ac7a0da",
  "type": "user",
  "uuid": "8de4964d-57ed-4b71-ac73-b3560bf6c5b4",
  "sourceToolAssistantUUID": "7f419822-7c28-4892-8470-040417a04b57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T04:34:53.186Z_

<details><summary>↩ Tool result · `toolu_012EtDUC9aC8GpTKuuNCehLH`</summary>

```text
Web search results for query: ""Anytime Verified Agents" AVA authors arxiv 2025 2026 adaptive compute verification"

Links: [{"title":"[2506.02539] VerificAgent: Domain-Specific Memory Verification for Scalable Oversight of Aligned Computer-Use Agents","url":"https://arxiv.org/abs/2506.02539"},{"title":"[2511.17330v2] Agentic Verification of Software Systems","url":"https://arxiv.org/abs/2511.17330v2"},{"title":"Agentic Program Verification","url":"https://arxiv.org/html/2511.17330v1"},{"title":"[2507.16203] SVAgent: AI Agent for Hardware Security Verification Assertion","url":"https://arxiv.org/abs/2507.16203"},{"title":"Verification-Aware Planning for Multi-Agent Systems","url":"https://arxiv.org/html/2510.17109v1"},{"title":"Artificial Intelligence Jul 2025","url":"https://arxiv.org/list/cs.AI/2025-07?skip=2050&show=1000"},{"title":"The 2025 AI Agent Index Documenting Technical and Safety Features of Deployed Agentic AI Systems","url":"https://arxiv.org/html/2602.17753v1"},{"title":"\\tool: Customizable Runtime Enforcement for Safe and Reliable LLM Agents","url":"https://arxiv.org/html/2503.18666v1"},{"title":"[2510.17109] Verification-Aware Planning for Multi-Agent Systems","url":"https://arxiv.org/abs/2510.17109"},{"title":"VerificAgent: Domain-Specific Memory Verification for Scalable Oversight of Aligned Computer-Use Agents","url":"https://arxiv.org/html/2506.02539v2"}]

Based on the search results, I found several papers related to agents and verification from 2025-2026, but I did not find a specific paper titled "Anytime Verified Agents" (AVA) in the results. However, here are some related papers on agent verification that were found:

1. **VerificAgent** - A paper by Thong Q. Nguyen and others, submitted in June 2025. VerificAgent is a scalable oversight framework that treats persistent memory as an explicit alignment surface, combining an expert-curated seed of domain knowledge, iterative trajectory-based memory growth during training, and a post-hoc human fact-checking pass.

2. **Agentic Verification of Software Systems** - A paper by Haoxin Tu and 5 other authors, with a first LLM agent called AutoRocq for conducting program verification that learns on-the-fly and improves proofs via iterative refinement through communication with the Rocq theorem prover.

3. **Verification-Aware Planning for Multi-Agent Systems (VeriMAP)** - A paper by Tianyang Xu and 3 other authors from October 2025. VeriMAP is a framework for multi-agent collaboration with verification-aware planning that decomposes tasks and encodes verification functions.

If you're looking for a specific paper called "Anytime Verified Agents" (AVA), it may use different terminology or may not yet be indexed in the search results. Would you like me to search with different keywords or provide more information about any of these papers?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ddfb744-93c6-493e-bccf-8f994429cb91",
  "isSidechain": true,
  "promptId": "359c1439-b630-4437-9c0e-2b3bec18ea1d",
  "agentId": "a37b983625ac7a0da",
  "type": "user",
  "uuid": "a3aa41e7-9da1-4b38-b49d-7f67c018ec96",
  "sourceToolAssistantUUID": "0ddfb744-93c6-493e-bccf-8f994429cb91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T04:34:56.584Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0197r4pAHr4n8KiktYAoJ6ur`</summary>

```json
{
  "query": "openreview \"Anytime Verified Agents\" JMDCMf7mlF authors adaptive compute"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3aa41e7-9da1-4b38-b49d-7f67c018ec96",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qbiswcaexAjU3TqxR3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "735b5486-d840-4ac4-bcbe-5bb47041f0c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXMV8bWbYzrwFTV2bPcUhb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2631,
      "cache_read_input_tokens": 21430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2631,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 30 · 2026-05-14T04:34:57.254Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018GLTysQmk7VftAL7U71ZdW`</summary>

```json
{
  "query": "arxiv 2505.13379 Thinkless authors NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "735b5486-d840-4ac4-bcbe-5bb47041f0c2",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qbiswcaexAjU3TqxR3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d92b9373-8103-4e1d-80f1-89ff74fd9d08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXMV8bWbYzrwFTV2bPcUhb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2631,
      "cache_read_input_tokens": 21430,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2631
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 21430,
          "cache_creation_input_tokens": 2631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2631,
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

_source line 31 · 2026-05-14T04:35:04.365Z_

<details><summary>↩ Tool result · `toolu_0197r4pAHr4n8KiktYAoJ6ur`</summary>

```text
Web search results for query: "openreview "Anytime Verified Agents" JMDCMf7mlF authors adaptive compute"

Links: [{"title":"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints | OpenReview","url":"https://openreview.net/forum?id=JMDCMf7mlF"},{"title":"ADAPTIVE IN-CONVERSATION TEAM BUILDING","url":"https://openreview.net/pdf/f2e46f1bd4fee7f26d2b8c4e4a85823358ed1208.pdf"},{"title":"Anytime Dense Prediction with Confidence Adaptivity | OpenReview","url":"https://openreview.net/forum?id=kNKFOXleuC"},{"title":"ALMC: Adaptive LLM-based Multi-Agent Collaboration Across Diverse Task Domains | OpenReview","url":"https://openreview.net/forum?id=jXZGgxTjiK"},{"title":"GitHub - vercel-labs/openreview: An open-source, self-hosted AI code review bot powered by Vercel. · GitHub","url":"https://github.com/vercel-labs/openreview"},{"title":"ADAM: A Systematic Data Extraction Attack on Agent Memory via Adaptive Querying | OpenReview","url":"https://openreview.net/forum?id=9H1nu8Z6Uy"},{"title":"Adaptive Social Learning via Mode Policy Optimization for Language Agents | OpenReview","url":"https://openreview.net/forum?id=GG7YQnsdhp"},{"title":"Learn to Memorize: Optimizing LLM-based Agents with Adaptive Memory Framework | OpenReview","url":"https://openreview.net/forum?id=EQ3TwO84Cs"},{"title":"WebArena Verified: Reliable Evaluation for Web Agents | OpenReview","url":"https://openreview.net/forum?id=94tlGxmqkN"},{"title":"Published as a conference paper at ICLR 2022 ANYTIME DENSE PREDICTION WITH","url":"https://openreview.net/pdf?id=kNKFOXleuC"}]

I found the paper you're looking for! Here's information about the OpenReview submission:

## Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints

The framework dynamically allocates compute across search, sampling, and verification within a user-specified budget, with an extensible interface for tool use.

**Key Contributions:**

AVA combines calibrated uncertainty estimation, value-of-information-guided search expansion, and selective verification cascades with early exits. The controller allocates compute based on uncertainty and estimated marginal reliability gains.

**Motivation:**

Existing methods allocate computational resources using static strategies such as fixed search depths, constant self-consistency sampling, or uniform verification, so simple problems can consume as much compute as complex tasks.

**Evaluation:**

AVA is evaluated on mathematical reasoning (GSM8K and MATH), multi-hop question answering (HotpotQA), and code generation (HumanEval), with two model back[ends mentioned but text was cut off in the source].

The paper appears to be a recent submission (from approximately 4 weeks ago based on the source metadata) and has undergone revisions addressing reviewer feedback, including evaluation on the MATH benchmark with GPT-4o for additional challenging test cases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "735b5486-d840-4ac4-bcbe-5bb47041f0c2",
  "isSidechain": true,
  "promptId": "359c1439-b630-4437-9c0e-2b3bec18ea1d",
  "agentId": "a37b983625ac7a0da",
  "type": "user",
  "uuid": "762f23ee-4207-483a-a25c-cc8ff59bf967",
  "sourceToolAssistantUUID": "735b5486-d840-4ac4-bcbe-5bb47041f0c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T04:35:04.623Z_

<details><summary>↩ Tool result · `toolu_018GLTysQmk7VftAL7U71ZdW`</summary>

```text
Web search results for query: "arxiv 2505.13379 Thinkless authors NeurIPS 2025"

Links: [{"title":"[2505.13379] Thinkless: LLM Learns When to Think","url":"https://arxiv.org/abs/2505.13379"},{"title":"Thinkless: LLM Learns When to Think","url":"https://arxiv.org/html/2505.13379"},{"title":"GitHub - VainF/Thinkless: [NeurIPS 2025] Thinkless: LLM Learns When to Think · GitHub","url":"https://github.com/VainF/Thinkless"},{"title":"[2505.13379v1] Thinkless: LLM Learns When to Think","url":"https://arxiv.org/abs/2505.13379v1"},{"title":"[2505.13379v2] Thinkless: LLM Learns When to Think","url":"https://arxiv.org/abs/2505.13379v2"},{"title":"arXiv:2505.13379v2 [cs.CL] 26 Jun 2025 Thinkless: LLM Learns When to Think","url":"https://arxiv.org/pdf/2505.13379"},{"title":"Paper page - Thinkless: LLM Learns When to Think","url":"https://huggingface.co/papers/2505.13379"},{"title":"NeurIPS Paper Checklist","url":"https://arxiv.org/html/2505.04037v1"},{"title":"NeurIPS 2025 FAQ for Authors","url":"https://neurips.cc/Conferences/2025/PaperInformation/NeurIPS-FAQ"},{"title":"NeurIPS 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/neurips-paper-list/neurips-2025-paper-list/"}]

Based on the search results, here's the information about arxiv paper 2505.13379:

## Paper Details

**Title:** Thinkless: LLM Learns When to Think

**Authors:** Gongfan Fang, Xinyin Ma, Xinchao Wang

**Affiliation:** xML Lab, National University of Singapore

**Venue:** NeurIPS 2025

## Summary

Thinkless is a learnable framework that empowers an LLM to adaptively select between short-form and long-form reasoning, based on both task complexity and the model's ability. Thinkless is trained under a reinforcement learning paradigm and employs two control tokens, for concise responses and for detailed reasoning.

At the core of the method is a Decoupled Group Relative Policy Optimization (DeGRPO) algorithm, which decomposes the learning objective of hybrid reasoning into two components: (1) a control token loss that governs the selection of the reasoning mode.

## Results

On several benchmarks such as Minerva Algebra, MATH-500, and GSM8K, Thinkless is able to reduce the usage of long-chain thinking by 50% - 90%, significantly improving the efficiency of Reasoning Language Models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d92b9373-8103-4e1d-80f1-89ff74fd9d08",
  "isSidechain": true,
  "promptId": "359c1439-b630-4437-9c0e-2b3bec18ea1d",
  "agentId": "a37b983625ac7a0da",
  "type": "user",
  "uuid": "a116ee68-36d0-461d-a2bb-5d23af29799c",
  "sourceToolAssistantUUID": "d92b9373-8103-4e1d-80f1-89ff74fd9d08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-14T04:35:42.057Z_

I now have enough information to compile the findings. Here are the results:

---

## Literature Survey: Selective Verification / Adaptive Computation Allocation in Agent RL

### Paper 1: Learning How Hard to Think: Input-Adaptive Allocation of LM Computation

- **Authors:** Mehul Damani, Idan Shenfeld, Andi Peng, Andreea Bobu, Jacob Andreas
- **Year:** 2024 (arXiv Oct 2024)
- **Venue:** ICLR 2025
- **Core method:** Trains a meta-predictor that estimates the reward distribution given an input and a computation budget, then allocates additional compute only to inputs where it is predicted to be most useful. Applied via (1) adaptive best-of-k sampling that dynamically varies the number of candidate generations per input, and (2) a routing procedure that selects between an expensive-accurate and a cheap-less-capable decoding path. Reduces computation by up to 50% with no quality loss, or improves quality by up to 10% at fixed budget.
- **arXiv:** https://arxiv.org/abs/2410.04707

### Paper 2: Thinkless: LLM Learns When to Think

- **Authors:** Gongfan Fang, Xinyin Ma, Xinchao Wang (National University of Singapore)
- **Year:** 2025 (arXiv May 2025)
- **Venue:** NeurIPS 2025
- **Core method:** Uses RL to train a reasoning LLM to adaptively choose between short-form (no chain-of-thought) and long-form (full CoT) reasoning per input, via two special control tokens (`&lt;short>` / `&lt;think>`). The key algorithm is Decoupled Group Relative Policy Optimization (DeGRPO), which separates the learning signal for mode selection from the learning signal for answer quality. Reduces long-chain thinking usage by 50-90% while maintaining accuracy within 1%.
- **arXiv:** https://arxiv.org/abs/2505.13379

### Paper 3: Learning When to Plan: Efficiently Allocating Test-Time Compute for LLM Agents

- **Authors:** Davide Paglieri, Bartlomiej Cupial, Jonathan Cook, Ulyana Piterbarg, Jens Tuyls, Edward Grefenstette, Jakob Nicolaus Foerster, Jack Parker-Holder, Tim Rocktaschel
- **Year:** 2025 (arXiv Sep 2025)
- **Venue:** arXiv preprint (2509.03581)
- **Core method:** Formalizes dynamic planning for LLM agents in sequential decision-making: the agent learns WHEN to invoke an expensive planning step (rather than planning before every action). Uses a two-stage pipeline -- SFT on synthetic data with diverse planning patterns, then RL in long-horizon environments (Crafter) to refine the plan/no-plan decision. First work to train LLM agents for dynamic test-time compute allocation in sequential decision-making tasks.
- **arXiv:** https://arxiv.org/abs/2509.03581

---

### Honorable mention (not an RL-trained agent, but highly relevant framing):

**Anytime Verified Agents (AVA): Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints** -- OpenReview submission (https://openreview.net/forum?id=JMDCMf7mlF). Dynamically allocates compute across search, sampling, and selective verification cascades with early exits, using calibrated uncertainty and value-of-information to decide where to spend budget. Not RL-trained but directly addresses the "learn when to verify" allocation problem.

---

**Key takeaway for the cost-verify-agent-rl project:** Paper 3 (Learning When to Plan) is the closest match -- it trains an agent via RL to decide when to invoke expensive reasoning during sequential execution. Paper 2 (Thinkless) demonstrates the RL training recipe (DeGRPO) for learning adaptive mode selection. Paper 1 (Learning How Hard to Think) provides the theoretical grounding for input-adaptive compute allocation with formal reward-distribution prediction. All three confirm that adaptive verification/computation allocation is a recognized and active research direction, but none specifically train an agent to decide when to *verify its own outputs* during multi-step execution -- which is the gap the cost-verify-agent-rl project targets.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a116ee68-36d0-461d-a2bb-5d23af29799c",
  "isSidechain": true,
  "agentId": "a37b983625ac7a0da",
  "requestId": "req_011Cb1qcZmY6ncRKKYSBxhBL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f5c86a1-204c-4c8a-a857-fd9a51afecc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "6404a15f-4164-44c5-9fd6-04abf2b2ff62",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L4Z8zmbKo6F6PLBmLnoY51",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1833,
      "cache_read_input_tokens": 24061,
      "output_tokens": 1055,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1833
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1055,
          "cache_read_input_tokens": 24061,
          "cache_creation_input_tokens": 1833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1833,
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
