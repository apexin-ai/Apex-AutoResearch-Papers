# Research conversation: Research task: Search specifically for the RAGEN framework - it appears to be a framework for training LLM agents with R

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ae2503964ab593ef8.jsonl`
- **Structured JSON:** [`13fec45a66ff0a2ab8a4.json`](../../sessions/13/13fec45a66ff0a2ab8a4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-14T12:45:20.303Z_

Research task: Search specifically for the RAGEN framework - it appears to be a framework for training LLM agents with RL (specifically GRPO) on interactive environments like ALFWorld.

Search the web for:
1. "RAGEN" LLM agent reinforcement learning
2. "RAGEN" GRPO training framework
3. RAGEN github repository
4. Any papers or blog posts about RAGEN

Also search for:
5. "Reinforcement learning for agentic generation" or similar
6. Training LLM agents with GRPO on ALFWorld specifically
7. verl / OpenRLHF / TRL frameworks being used for agent RL training on interactive environments

Return whatever you find about RAGEN and related frameworks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4fde07a8-6703-42b2-afaf-fdcd02bc6fea",
  "agentId": "ae2503964ab593ef8",
  "type": "user",
  "uuid": "e65e0dbd-0b65-42a7-9345-ce0f3b823171",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T12:45:20.313Z_

```json
{
  "parentUuid": "e65e0dbd-0b65-42a7-9345-ce0f3b823171",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
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
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f43edc49-3f7f-4495-9a34-4d00ef6f0a69",
  "timestamp": "2026-05-14T12:45:20.313Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T12:45:22.790Z_



I'll search for RAGEN and related frameworks across multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f43edc49-3f7f-4495-9a34-4d00ef6f0a69",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2UzvVtUn8wi6m8VfR3w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9180e7e5-676d-4da2-961f-7da435aab5b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fNb6G9zAkTwEC4StMywUv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5941,
      "cache_read_input_tokens": 7333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5941,
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

_source line 4 · 2026-05-14T12:45:23.318Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01X7trHtpeFLpXgw5bKV7Qr6`</summary>

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
  "parentUuid": "9180e7e5-676d-4da2-961f-7da435aab5b8",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2UzvVtUn8wi6m8VfR3w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3460a522-2389-459f-88e1-1e774f4c46cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fNb6G9zAkTwEC4StMywUv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5941,
      "cache_read_input_tokens": 7333,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5941
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 7333,
          "cache_creation_input_tokens": 5941,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5941,
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

_source line 5 · 2026-05-14T12:45:23.322Z_

<details><summary>↩ Tool result · `toolu_01X7trHtpeFLpXgw5bKV7Qr6`</summary>

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
  "parentUuid": "3460a522-2389-459f-88e1-1e774f4c46cf",
  "isSidechain": true,
  "promptId": "4fde07a8-6703-42b2-afaf-fdcd02bc6fea",
  "agentId": "ae2503964ab593ef8",
  "type": "user",
  "uuid": "623443bf-04f2-424c-827c-48258404b7f3",
  "sourceToolAssistantUUID": "3460a522-2389-459f-88e1-1e774f4c46cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T12:45:25.732Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "623443bf-04f2-424c-827c-48258404b7f3",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2V19isSTLipG6yrGXgq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a89f602-c5b6-4b17-b1bf-be516a42c4dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGTq64wgSwRJTrHzWVYpDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 13274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1457,
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

_source line 7 · 2026-05-14T12:45:25.923Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GSRGfpRP5cvLDbPZvYdNg5`</summary>

```json
{
  "query": "RAGEN LLM agent reinforcement learning framework"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a89f602-c5b6-4b17-b1bf-be516a42c4dc",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2V19isSTLipG6yrGXgq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13cf14ff-56ba-456b-902c-69428e8a0674",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UGTq64wgSwRJTrHzWVYpDJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1457,
      "cache_read_input_tokens": 13274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1457,
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

_source line 8 · 2026-05-14T12:45:34.004Z_

<details><summary>↩ Tool result · `toolu_01GSRGfpRP5cvLDbPZvYdNg5`</summary>

```text
Web search results for query: "RAGEN LLM agent reinforcement learning framework"

Links: [{"title":"GitHub - mll-lab-nu/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments. · GitHub","url":"https://github.com/mll-lab-nu/RAGEN"},{"title":"RAGEN - RL Agent","url":"https://ragen-ai.github.io/"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via","url":"https://ragen-ai.github.io/pdf/RAGEN.pdf"},{"title":"[2504.20073] RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://arxiv.org/abs/2504.20073"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2504.20073v2"},{"title":"GitHub - RAGEN-AI/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments.","url":"https://github.com/RAGEN-AI/RAGEN/tree/main"},{"title":"RAGEN: Self-Evolution in LLM Agents via Multi-Turn RL","url":"https://www.emergentmind.com/papers/2504.20073"},{"title":"RAGEN","url":"https://ragen-doc.readthedocs.io/"},{"title":"Paper page - RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://huggingface.co/papers/2504.20073"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via ...","url":"https://arxiv.org/pdf/2504.20073"}]

## RAGEN: LLM Agent Reinforcement Learning Framework

I found comprehensive information about RAGEN. Here's an overview:

### What is RAGEN?

RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments. RAGEN (Reasoning AGENt, pronounced like "region") leverages reinforcement learning (RL) to train LLM reasoning agents in interactive, stochastic environments.

### Core Framework: StarPO

The system is built around StarPO (State-Thinking-Actions-Reward Policy Optimization), a general framework for trajectory-level agent RL. RAGEN is built around StarPO (State-Thinking-Actions-Reward Policy Optimization), a unified RL framework for training multi-turn, trajectory-level agents with flexible control over reasoning processes, reward assignment mechanisms, and prompt-rollout structures.

### Key Technical Components

Agent-environment interactions are formulated as Markov Decision Processes (MDPs) where states and actions are token sequences, allowing LLMs to reason over environment dynamics.

The framework operates in two stages:
- Given an initial state, the LLM generates multiple trajectories. At each step, the model produces a reasoning-guided action: &lt;think>...&lt;/think>&lt;ans> action &lt;/ans>. The environment returns feedback (reward and next state).
- StarPO optimizes entire trajectories using importance sampling.

### Supported Environments

RAGEN includes 10 built-in environments: Sokoban, FrozenLake, WebShop, DeepSeek Coder, SearchQA, Lean, Bandit, Countdown, MetaMathQA, Sudoku.

### Key Findings

The agent RL training shows a recurring mode of Echo Trap where reward variability cliffs and gradient spikes; this is addressed with StarPO-S, a stabilized variant with trajectory filtering, critic incorporation, and gradient stabilization.

The codebase is available on GitHub at https://github.com/RAGEN-AI/RAGEN, with the research paper published on arXiv (2504.20073).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13cf14ff-56ba-456b-902c-69428e8a0674",
  "isSidechain": true,
  "promptId": "4fde07a8-6703-42b2-afaf-fdcd02bc6fea",
  "agentId": "ae2503964ab593ef8",
  "type": "user",
  "uuid": "4741a8e5-367b-47af-9fae-9ecd50d0b31f",
  "sourceToolAssistantUUID": "13cf14ff-56ba-456b-902c-69428e8a0674",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T12:45:36.045Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PNFaXQe36eHGW66tiMMWdQ`</summary>

```json
{
  "query": "RAGEN GRPO training framework StarPO agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4741a8e5-367b-47af-9fae-9ecd50d0b31f",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2V1vyC6ABzT8FXrWFC3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94dc7457-bdfa-4aea-8ec5-5567fcf34945",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019V4XnenzPaRtF63trbqWUb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1048,
      "cache_read_input_tokens": 14731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1048,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 10 · 2026-05-14T12:45:37.037Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0124UB3DDozBMFjmy3NK7jMw`</summary>

```json
{
  "query": "RAGEN github repository RAGEN-AI verl multi-turn reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94dc7457-bdfa-4aea-8ec5-5567fcf34945",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2V1vyC6ABzT8FXrWFC3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "196e3dba-d4cf-4575-beae-1f89933e0c0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019V4XnenzPaRtF63trbqWUb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1048,
      "cache_read_input_tokens": 14731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1048,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 11 · 2026-05-14T12:45:37.237Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NazoNMUX3n6zxuto8mKZvx`</summary>

```json
{
  "query": "RAGEN paper \"multi-turn reinforcement learning\" LLM agents 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "196e3dba-d4cf-4575-beae-1f89933e0c0f",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2V1vyC6ABzT8FXrWFC3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "df1a7107-3714-4232-bbb1-1e64542e64de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019V4XnenzPaRtF63trbqWUb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1048,
      "cache_read_input_tokens": 14731,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1048
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 14731,
          "cache_creation_input_tokens": 1048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1048,
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

_source line 12 · 2026-05-14T12:45:42.311Z_

<details><summary>↩ Tool result · `toolu_01NazoNMUX3n6zxuto8mKZvx`</summary>

```text
Web search results for query: "RAGEN paper "multi-turn reinforcement learning" LLM agents 2025"

Links: [{"title":"[2504.20073] RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://arxiv.org/abs/2504.20073"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via ...","url":"https://arxiv.org/pdf/2504.20073"},{"title":"GitHub - mll-lab-nu/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments. · GitHub","url":"https://github.com/mll-lab-nu/RAGEN"},{"title":"Understanding Self-Evolution in LLM Agents via Multi-Turn ...","url":"https://ragen-ai.github.io/pdf/RAGEN.pdf"},{"title":"RAGEN-2: Reasoning Collapse in Agentic RL","url":"https://ragen-ai.github.io/"},{"title":"Paper page - RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://huggingface.co/papers/2504.20073"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2504.20073v2"},{"title":"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning","url":"https://arxiv.org/html/2605.02178v1"},{"title":"dblp: RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning.","url":"https://dblp.org/rec/journals/corr/abs-2504-20073.html"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250420073W/abstract"}]

Great! I found comprehensive information about the RAGEN paper. Here's what I found:

## RAGEN Paper Overview

RAGEN proposes StarPO (State-Thinking-Actions-Reward Policy Optimization), a general framework for trajectory-level agent RL, and introduces RAGEN, a modular system for training and evaluating LLM agents.

### Key Focus

The research addresses unique challenges in training LLMs as interactive agents, including long-horizon decision making and interacting with stochastic environment feedback, while noting that multi-turn agent RL training remains underexplored.

### Core Findings

The agent RL training shows a recurring mode called "Echo Trap" where reward variance cliffs and gradient spikes occur; this is addressed with StarPO-S, a stabilized variant with trajectory filtering, critic incorporation, and gradient stabilization.

The study finds that RL rollouts would benefit from diverse initial states, medium interaction granularity and more frequent sampling.

### Publication Details

The paper was submitted on April 24, 2025 (v1) and last revised on May 26, 2025 (v2). It's authored by Zihan Wang, Kangrui Wang, and collaborators from major institutions including Northwestern University, Stanford University, Microsoft, and others.

### Resources

The paper is available at arXiv (2504.20073), with code and environments available at https://github.com/RAGEN-AI/RAGEN.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df1a7107-3714-4232-bbb1-1e64542e64de",
  "isSidechain": true,
  "promptId": "4fde07a8-6703-42b2-afaf-fdcd02bc6fea",
  "agentId": "ae2503964ab593ef8",
  "type": "user",
  "uuid": "8423ff5a-5ba9-412b-9fa5-afd9270f3829",
  "sourceToolAssistantUUID": "df1a7107-3714-4232-bbb1-1e64542e64de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T12:45:43.962Z_

<details><summary>↩ Tool result · `toolu_01PNFaXQe36eHGW66tiMMWdQ`</summary>

```text
Web search results for query: "RAGEN GRPO training framework StarPO agent"

Links: [{"title":"RAGEN - RL Agent","url":"https://ragen-ai.github.io/"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via","url":"https://ragen-ai.github.io/pdf/RAGEN.pdf"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via ...","url":"https://arxiv.org/pdf/2504.20073"},{"title":"GitHub - mll-lab-nu/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments. · GitHub","url":"https://github.com/RAGEN-AI/RAGEN"},{"title":"GitHub - RAGEN-AI/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments.","url":"https://github.com/RAGEN-AI/RAGEN/tree/main"},{"title":"Training LLM Agents Just Got More Stable: Researchers Introduce StarPO-S and RAGEN to Tackle Multi-Turn Reasoning and Collapse in Reinforcement Learning - MarkTechPost","url":"https://www.marktechpost.com/2025/05/01/training-llm-agents-just-got-more-stable-researchers-introduce-starpo-s-and-ragen-to-tackle-multi-turn-reasoning-and-collapse-in-reinforcement-learning/"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2504.20073"},{"title":"Training AI Agents That Don’t Fall Apart: How RAGEN and StarPO Are Solving the ‘Echo Trap’ | by Tech Dose | Medium","url":"https://medium.com/@tech.dose/training-ai-agents-that-dont-fall-apart-how-ragen-and-starpo-are-solving-the-echo-trap-c149b23248fa"},{"title":"Partner Spotlight: Orchestrating large-scale agent training on Lambda with dstack and RAGEN","url":"https://lambda.ai/blog/agent-training-on-lambda-with-dstack-and-ragen"},{"title":"RAGEN/README.md at main · RAGEN-AI/RAGEN","url":"https://github.com/RAGEN-AI/RAGEN/blob/main/README.md"}]

Based on the search results, here's information about RAGEN, the GRPO training framework, and StarPO agent:

## RAGEN and StarPO Framework

RAGEN (Reasoning AGENT) is a flexible RL framework for training reasoning agents. RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments.

The core of RAGEN is built on StarPO (State-Thinking-Actions-Reward Policy Optimization), a unified RL framework for training multi-turn, trajectory-level agents with flexible control over reasoning processes, reward assignment mechanisms, and prompt-rollout structures.

## Key Features of StarPO

Instead of step-by-step optimization, StarPO optimizes entire trajectories using importance sampling. This approach enables long-horizon reasoning while maintaining computational efficiency. Unlike traditional approaches that treat each action independently, StarPO optimises entire trajectories—including observations, reasoning traces, actions, and feedback—as coherent units. This trajectory-level approach is particularly suited for interactive environments where agents must maintain memory across turns and adapt to stochastic feedback.

## GRPO Support

StarPO supports GRPO, which assigns normalized reward to the full trajectory. Policy updates use GRPO or PPO with GAE, Adam optimizer, entropy bonus, and a response-format penalty.

## Addressing Training Instability

RL training shows a recurring mode of Echo Trap where reward variance cliffs and gradient spikes; this is addressed with StarPO-S, a stabilized variant with trajectory filtering, critic incorporation, and decoupled clipping.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94dc7457-bdfa-4aea-8ec5-5567fcf34945",
  "isSidechain": true,
  "promptId": "4fde07a8-6703-42b2-afaf-fdcd02bc6fea",
  "agentId": "ae2503964ab593ef8",
  "type": "user",
  "uuid": "e254bbdb-e1c6-469d-a239-4fb7afc5e541",
  "sourceToolAssistantUUID": "94dc7457-bdfa-4aea-8ec5-5567fcf34945",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T12:45:44.831Z_

<details><summary>↩ Tool result · `toolu_0124UB3DDozBMFjmy3NK7jMw`</summary>

```text
Web search results for query: "RAGEN github repository RAGEN-AI verl multi-turn reinforcement learning"

Links: [{"title":"GitHub - mll-lab-nu/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments. · GitHub","url":"https://github.com/mll-lab-nu/RAGEN"},{"title":"Understanding Self-Evolution in LLM Agents via Multi-Turn ...","url":"https://ragen-ai.github.io/pdf/RAGEN.pdf"},{"title":"RAGEN-2: Reasoning Collapse in Agentic RL","url":"https://ragen-ai.github.io/"},{"title":"GitHub - RAGEN-AI/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments.","url":"https://github.com/RAGEN-AI/RAGEN/tree/main"},{"title":"GitHub - mll-lab-nu/VAGEN: Training VLM agents with multi-turn reinforcement learning · GitHub","url":"https://github.com/RAGEN-AI/VAGEN"},{"title":"Paper page - RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://huggingface.co/papers/2504.20073"},{"title":"RAGEN/ragen/trainer/agent_trainer.py at main · RAGEN-AI/RAGEN","url":"https://github.com/RAGEN-AI/RAGEN/blob/main/ragen/trainer/agent_trainer.py"},{"title":"RAGEN/README.md at main · RAGEN-AI/RAGEN","url":"https://github.com/RAGEN-AI/RAGEN/blob/main/README.md"},{"title":"[2504.20073] RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://arxiv.org/abs/2504.20073"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2504.20073v2"}]

Based on the web search results, here's information about the RAGEN GitHub repository:

## Overview

RAGEN (Reasoning AGENt, pronounced like "region") leverages reinforcement learning (RL) to train LLM reasoning agents in interactive, stochastic environments.

## StarPO Framework

RAGEN introduces StarPO (State-Thinking-Actions-Reward Policy Optimization), a general framework for trajectory-level agent RL, and RAGEN is a modular system for training and evaluating LLM agents. StarPO is a unified RL framework for training multi-turn, trajectory-level agents with flexible control over reasoning processes, reward assignment mechanisms, and prompt-rollout structures.

## Key Features

RAGEN has been restructured with veRL as a submodule for better co-development, and divided into three components—Environment Manager, Context Manager, and Agent Proxy. The system includes 10 built-in environments: Sokoban, FrozenLake, WebShop, DeepCoder, SearchQA, Lean, Bandit, Countdown, MetaMathQA, and Sudoku.

## Training Challenges Addressed

RAGEN addresses a recurring training issue called Echo Trap where reward variance cliffs and gradient spikes occur; this is handled with StarPO-S, a stabilized variant with trajectory filtering, critic incorporation, and gradient stabilization.

## Repository and Documentation

Project website: https://ragen-ai.github.io and code is available at https://github.com/RAGEN-AI/RAGEN. As of May 2025, official documentation for RAGEN was released and is continuously updated and improved.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "196e3dba-d4cf-4575-beae-1f89933e0c0f",
  "isSidechain": true,
  "promptId": "4fde07a8-6703-42b2-afaf-fdcd02bc6fea",
  "agentId": "ae2503964ab593ef8",
  "type": "user",
  "uuid": "52869b4a-e582-443f-9166-a415ede39ddd",
  "sourceToolAssistantUUID": "196e3dba-d4cf-4575-beae-1f89933e0c0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T12:45:47.551Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0191hUQtAqPMQ3hoTcMbgFLN`</summary>

```json
{
  "query": "RAGEN training LLM agents ALFWorld interactive environments GRPO verl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52869b4a-e582-443f-9166-a415ede39ddd",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2V2jHWCPXWS38tVFmJ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c75be5e7-883d-4a0b-be95-decb9185206a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wWttNCvCkh2SSNPQKYQfA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 2131,
      "cache_read_input_tokens": 15779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2131,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 16 · 2026-05-14T12:45:48.530Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MMYD3g3U4CaEcTvy7bb8UF`</summary>

```json
{
  "query": "\"reinforcement learning\" \"agentic generation\" GRPO ALFWorld LLM agent training 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c75be5e7-883d-4a0b-be95-decb9185206a",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2V2jHWCPXWS38tVFmJ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38de9ded-ab2b-421d-8cec-ec7e52ba11f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wWttNCvCkh2SSNPQKYQfA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 2131,
      "cache_read_input_tokens": 15779,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2131,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
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

_source line 17 · 2026-05-14T12:45:49.139Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Me8U9KgHrS4T3M9x9V5cz8`</summary>

```json
{
  "query": "verl OpenRLHF TRL agent RL training interactive environments ALFWorld multi-turn 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38de9ded-ab2b-421d-8cec-ec7e52ba11f8",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2V2jHWCPXWS38tVFmJ4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ee0cf18-e632-4641-81a5-f402f6960880",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wWttNCvCkh2SSNPQKYQfA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 2131,
      "cache_read_input_tokens": 15779,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2131
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 893,
          "output_tokens": 186,
          "cache_read_input_tokens": 15779,
          "cache_creation_input_tokens": 2131,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2131,
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

_source line 18 · 2026-05-14T12:45:57.210Z_

<details><summary>↩ Tool result · `toolu_01MMYD3g3U4CaEcTvy7bb8UF`</summary>

```text
Web search results for query: ""reinforcement learning" "agentic generation" GRPO ALFWorld LLM agent training 2025"

Links: [{"title":"Reinforcement World Model Learning for LLM-based Agents","url":"https://arxiv.org/html/2602.05842v1"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"GitHub - Gen-Verse/Open-AgentRL: [ICML 2026] RLAnything & DemyAgent: General and scalable agentic RL algorithms across terminal, GUI, SWE, and tool-call settings · GitHub","url":"https://github.com/Gen-Verse/Open-AgentRL"},{"title":"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning","url":"https://arxiv.org/html/2605.02178v1"},{"title":"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey","url":"https://arxiv.org/html/2509.02547v5"},{"title":"Reinforcement Learning for LLM Agent Planning","url":"https://aclanthology.org/2025.emnlp-industry.116.pdf"},{"title":"AGENTRL: SCALING AGENTIC REINFORCEMENT ...","url":"https://openreview.net/pdf?id=zq3vAmuUk9"},{"title":"NeurIPS A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning","url":"https://neurips.cc/virtual/2025/127960"},{"title":"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning","url":"https://arxiv.org/html/2509.22601v3"},{"title":"A Practitioner’s Guide to Multi-turn Agentic Reinforcement Learning","url":"https://arxiv.org/html/2510.01132v2"}]

I've completed a web search for your query on reinforcement learning, agentic generation, GRPO, ALFWorld, and LLM agent training from 2025. Here are the key findings:

## Overview of Recent Research

The search results reveal an active research landscape in 2025 focused on using reinforcement learning to train LLM-based agents. Here are the main themes:

### GRPO and Policy Optimization Methods

GRPO (Group Relative Policy Optimization) and PPO are on-policy methods being leveraged to enhance capabilities such as instruction-following, ethical alignment, and code generation in LLM training. GRPO introduces group-based sampling for agentic reinforcement learning.

### ALFWorld Benchmark

Researchers are training models from Qwen2.5-7B-Instruct on ALFWorld following prior work, and GRPO is being used to let models learn to solve tasks using task-success rewards. ALFWorld is an embodied household environment requiring multi-step task completion through text interaction, with training on the "train" split and evaluation on the "valid_unseen" split.

### Agentic RL Training Frameworks

AGENTRL is being applied to open LLMs including Qwen2.5 and GLM-4-9B across multiple agentic tasks including ALFWorld, and achieves state-of-the-art results, significantly outperforming GPT-5 and DeepSeek-R1.

### Multi-turn Reinforcement Learning

Research is studying how to train LLMs as autonomous agents that act over multiple turns in agentic environments, with reinforcement learning extending to multi-turn environments introducing new challenges.

### Recent Innovations

SPEAR is a self-imitation learning recipe for training agentic LLMs that extends vanilla SIL by gradually steering policy entropy across stages, and increases success rates on ALFWorld and WebShop benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38de9ded-ab2b-421d-8cec-ec7e52ba11f8",
  "isSidechain": true,
  "promptId": "4fde07a8-6703-42b2-afaf-fdcd02bc6fea",
  "agentId": "ae2503964ab593ef8",
  "type": "user",
  "uuid": "f2cab9f7-1ee0-463d-a811-d8778bc68616",
  "sourceToolAssistantUUID": "38de9ded-ab2b-421d-8cec-ec7e52ba11f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T12:45:58.653Z_

<details><summary>↩ Tool result · `toolu_01Me8U9KgHrS4T3M9x9V5cz8`</summary>

```text
Web search results for query: "verl OpenRLHF TRL agent RL training interactive environments ALFWorld multi-turn 2025"

Links: [{"title":"Open Source RL Libraries for LLMs | Anyscale","url":"https://www.anyscale.com/blog/open-source-rl-libraries-for-llms"},{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengQ/verl-agent"},{"title":"GitHub - OpenRLHF/OpenRLHF: An Easy-to-use, Scalable and High-performance Agentic RL Framework based on Ray (PPO & DAPO & REINFORCE++ & VLM & TIS & vLLM & Ray & Async RL) · GitHub","url":"https://github.com/openrlhf/openrlhf"},{"title":"Agentic RL Training - verl documentation - Read the Docs","url":"https://verl.readthedocs.io/en/latest/start/agentic_rl.html"},{"title":"A Practitioner’s Guide to Multi-turn Agentic Reinforcement Learning","url":"https://arxiv.org/html/2510.01132v1"},{"title":"AgentFly: Extensible and Scalable Reinforcement Learning for LM Agents","url":"https://arxiv.org/html/2507.14897v1"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978v1"},{"title":"GitHub - verl-project/verl: verl/HybridFlow: A Flexible and Efficient RL Post-Training Framework · GitHub","url":"https://github.com/verl-project/verl"},{"title":"Anatomy of RL Frameworks - Hanif Leoputera","url":"https://www.hanifleo.com/anatomy-of-rl-frameworks/"},{"title":"Verlog: A Multi-turn RL framework for LLM agents – Machine Learning Blog | ML@CMU | Carnegie Mellon University","url":"https://blog.ml.cmu.edu/2025/09/15/verlog-a-multi-turn-rl-framework-for-llm-agents/"}]

Based on the search results, I can provide you with comprehensive information about verl, OpenRLHF, TRL, and their applications in agent RL training with interactive environments like ALFWorld:

## Overview of RL Frameworks

Verl is a popular high-performance, feature-rich RL stack from ByteDance optimized for scalability and support for advanced training techniques. OpenRLHF is one of the earliest popular open-source RLHF libraries, both easy to use and high-performance. TRL is a popular library from Hugging Face, tightly integrated with the Hugging Face ecosystem, focusing on the training aspect of RL.

## Multi-Turn Agent RL Training

OpenRLHF is the first RLHF framework to implement a unified agent-based paradigm, and is the first high-performance, production-ready open-source RLHF framework that combines Ray + vLLM distributed architecture with a unified agent-based design paradigm for scalable and extensible reinforcement learning from human feedback.

OpenRLHF 0.10 adds Multi-Turn VLM RL — multi-step interactions with images in both prompts and environment feedback.

## ALFWorld and Interactive Environments

verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL, and offers a diverse set of interactive environments including embodied AI environments like ALFWorld, visual games such as Sokoban and Gym Cards, and digital interface control tasks like WebShop and AppWorld.

verl-agent's design keeps the context length almost constant over time, making it highly scalable for long-horizon scenarios (e.g., 30–50 steps in ALFWorld) without running into token limits or inefficiency.

## Recent Research (2025)

A practitioner's guide to multi-turn agentic RL releases a complete multi-turn RL framework built on veRL, including environment integrations for TextWorld, ALFWorld, and SWE-Gym.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ee0cf18-e632-4641-81a5-f402f6960880",
  "isSidechain": true,
  "promptId": "4fde07a8-6703-42b2-afaf-fdcd02bc6fea",
  "agentId": "ae2503964ab593ef8",
  "type": "user",
  "uuid": "8d4a105d-1243-444c-8dd6-f57146c79da9",
  "sourceToolAssistantUUID": "1ee0cf18-e632-4641-81a5-f402f6960880",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T12:45:59.594Z_

<details><summary>↩ Tool result · `toolu_0191hUQtAqPMQ3hoTcMbgFLN`</summary>

```text
Web search results for query: "RAGEN training LLM agents ALFWorld interactive environments GRPO verl"

Links: [{"title":"GitHub - mll-lab-nu/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments. · GitHub","url":"https://github.com/mll-lab-nu/RAGEN"},{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengQ/verl-agent"},{"title":"GitHub - RAGEN-AI/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments.","url":"https://github.com/RAGEN-AI/RAGEN/tree/main"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via","url":"https://ragen-ai.github.io/pdf/RAGEN.pdf"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2504.20073v2"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978v3"},{"title":"RAGEN/ragen/trainer/agent_trainer.py at main · RAGEN-AI/RAGEN","url":"https://github.com/RAGEN-AI/RAGEN/blob/main/ragen/trainer/agent_trainer.py"},{"title":"A Practitioner’s Guide to Multi-turn Agentic Reinforcement Learning","url":"https://arxiv.org/html/2510.01132"},{"title":"RAGEN-2: Reasoning Collapse in Agentic RL","url":"https://ragen-ai.github.io/"},{"title":"AgentFly: Extensible and Scalable Reinforcement Learning for LM Agents","url":"https://arxiv.org/html/2507.14897v1"}]

Based on the search results, here's an overview of the technologies and frameworks mentioned in your query:

## RAGEN (Reasoning Agent)

RAGEN leverages reinforcement learning (RL) to train LLM reasoning agents in interactive, stochastic environments. RAGEN is a flexible RL framework for training reasoning agents that develops diagnostics to understand how agent RL training works and how to fix hidden issues.

## StarPO Framework

RAGEN is built around StarPO (State-Thinking-Actions-Reward Policy Optimization), a unified RL framework for training multi-turn, trajectory-level agents with flexible control over reasoning processes, reward assignment mechanisms, and prompt-rollout structures.

## ALFWorld Integration

RAGEN includes 10 built-in environments including Sokoban, FrozenLake, WebShop, DeepCoder, SearchQA, Lean, Bandit, Countdown, MetaMathQA, and Sudoku. ALFWorld is one of the key embodied AI environments used for evaluation.

## GRPO (Group Relative Policy Optimization)

StarPO supports multiple optimization strategies including GRPO, where normalized reward is assigned to the full trajectory. Group-based RL algorithms such as GRPO have proven especially effective in large-scale training, replacing value-function estimation with simple yet powerful relative advantage estimation within groups of rollouts, enjoying favorable properties such as low memory overhead, critic-free optimization, and scalability to large models.

## veRL Integration

The RAGEN codebase was restructured with veRL integrated as a submodule; architecture decomposed into three modules — Environment State Manager, Context Manager, and Agent Proxy. verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c75be5e7-883d-4a0b-be95-decb9185206a",
  "isSidechain": true,
  "promptId": "4fde07a8-6703-42b2-afaf-fdcd02bc6fea",
  "agentId": "ae2503964ab593ef8",
  "type": "user",
  "uuid": "be82bffd-1687-4971-99e7-af48e22b4ea8",
  "sourceToolAssistantUUID": "c75be5e7-883d-4a0b-be95-decb9185206a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T12:46:02.490Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DfHeR3e6dYAoD7PD7CSdV2`</summary>

```json
{
  "query": "RAGEN-2 \"reasoning collapse\" agentic RL 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be82bffd-1687-4971-99e7-af48e22b4ea8",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2V3pmSDSd9DhFMMqKfb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d08a5075-b884-4d47-8cbd-6fcd5bf6865c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BfewZ6rXzMCEonnhguoCZi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2129,
      "cache_creation_input_tokens": 2180,
      "cache_read_input_tokens": 17910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2180,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

_source line 22 · 2026-05-14T12:46:02.965Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JAgL5MpXHRx8QMC2F78P2u`</summary>

```json
{
  "query": "RAGEN architecture verl submodule environment manager context manager agent proxy code structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d08a5075-b884-4d47-8cbd-6fcd5bf6865c",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2V3pmSDSd9DhFMMqKfb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63b45529-f8d2-4b7a-8ab4-4c5ffeda3554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BfewZ6rXzMCEonnhguoCZi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2129,
      "cache_creation_input_tokens": 2180,
      "cache_read_input_tokens": 17910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2180,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

_source line 23 · 2026-05-14T12:46:03.447Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RTa7Pp7oTXia2pzBSWHeNG`</summary>

```json
{
  "query": "verl-agent \"group-in-group\" policy optimization ALFWorld agent training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63b45529-f8d2-4b7a-8ab4-4c5ffeda3554",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2V3pmSDSd9DhFMMqKfb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0e22b04-c01f-49fd-bfbc-6076428d5d26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BfewZ6rXzMCEonnhguoCZi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2129,
      "cache_creation_input_tokens": 2180,
      "cache_read_input_tokens": 17910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2180,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 40,
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

_source line 24 · 2026-05-14T12:46:07.830Z_

<details><summary>↩ Tool result · `toolu_01DfHeR3e6dYAoD7PD7CSdV2`</summary>

```text
Web search results for query: "RAGEN-2 "reasoning collapse" agentic RL 2025 2026"

Links: [{"title":"RAGEN-2: Reasoning Collapse in Agentic RL","url":"https://arxiv.org/html/2604.06268v1"},{"title":"[2604.06268] RAGEN-2: Reasoning Collapse in Agentic RL","url":"https://arxiv.org/abs/2604.06268"},{"title":"GitHub - mll-lab-nu/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments. · GitHub","url":"https://github.com/mll-lab-nu/RAGEN"},{"title":"Paper page - RAGEN-2: Reasoning Collapse in Agentic RL","url":"https://huggingface.co/papers/2604.06268"},{"title":"RAGEN-2: Reasoning Collapse in Agentic RL","url":"https://ragen-ai.github.io/"},{"title":"RAGEN-2: Reasoning Collapse in Agentic RL - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/ragen-2-reasoning-collapse-in-agentic-rl/"},{"title":"RAGEN-2: Reasoning Collapse in Agentic RL – Paper Detail · SwiftScholar - Review with AI","url":"https://www.swiftscholar.net/paper/69d83d9f5127ff45a9dee799"},{"title":"[2604.06268v1] RAGEN-2: Reasoning Collapse in Agentic RL","url":"https://arxiv.org/abs/2604.06268v1"},{"title":"(PDF) RAGEN-2: Reasoning Collapse in Agentic RL","url":"https://www.researchgate.net/publication/403641455_RAGEN-2_Reasoning_Collapse_in_Agentic_RL"},{"title":"RAGEN-2: Reasoning Collapse in Agentic RL | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2604.06268"}]

I've found comprehensive information about RAGEN-2. Here's what the search revealed:

## RAGEN-2: Reasoning Collapse in Agentic RL

RAGEN-2 is a research paper on reasoning collapse in agentic reinforcement learning authored by Zihan Wang and 15 other researchers, published as a preprint in April 2026.

### The Core Problem

RL training of multi-turn LLM agents is inherently unstable, and entropy is widely used to track reasoning stability. However, entropy only measures diversity within the same input, and cannot tell whether reasoning actually responds to different inputs.

### Template Collapse

The paper finds that even with stable entropy, models can rely on fixed templates that look diverse but are input-agnostic. This is called template collapse, a failure mode invisible to entropy and all existing metrics.

### The Solution

To diagnose this failure, the researchers decompose reasoning quality into within-input diversity (Entropy) and cross-input distinguishability (Mutual Information, MI), and introduce a family of mutual information proxies for online diagnosis. Across diverse tasks, mutual information correlates with final performance much more strongly than entropy, making it a more reliable proxy for reasoning quality.

### Proposed Intervention

SNR-Adaptive Filtering uses reward variance as a lightweight proxy to select high-signal prompts each iteration, directly addressing the root cause of template collapse.

The paper evaluates these findings across seven diverse environments including Sokoban, FrozenLake, MetaMathQA, and code synthesis tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d08a5075-b884-4d47-8cbd-6fcd5bf6865c",
  "isSidechain": true,
  "promptId": "4fde07a8-6703-42b2-afaf-fdcd02bc6fea",
  "agentId": "ae2503964ab593ef8",
  "type": "user",
  "uuid": "01c88d5b-f54b-4a18-9edc-976ee28f3ab9",
  "sourceToolAssistantUUID": "d08a5075-b884-4d47-8cbd-6fcd5bf6865c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T12:46:09.311Z_

<details><summary>↩ Tool result · `toolu_01JAgL5MpXHRx8QMC2F78P2u`</summary>

```text
Web search results for query: "RAGEN architecture verl submodule environment manager context manager agent proxy code structure"

Links: [{"title":"GitHub - mll-lab-nu/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments. · GitHub","url":"https://github.com/mll-lab-nu/RAGEN"},{"title":"GitHub - RAGEN-AI/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments.","url":"https://github.com/RAGEN-AI/RAGEN/tree/main"},{"title":"RAGEN/README.md at main · RAGEN-AI/RAGEN","url":"https://github.com/RAGEN-AI/RAGEN/blob/main/README.md"},{"title":"RAGEN/ragen/llm_agent/agent_proxy.py at 9fb8527776a8490f240417bd964e6eac75777fb0 · RAGEN-AI/RAGEN","url":"https://github.com/RAGEN-AI/RAGEN/blob/9fb8527776a8490f240417bd964e6eac75777fb0/ragen/llm_agent/agent_proxy.py"},{"title":"GitHub - TIGER-AI-Lab/verl-tool: A version of verl to support diverse tool use · GitHub","url":"https://github.com/TIGER-AI-Lab/verl-tool"},{"title":"VERL - Agent-lightning","url":"https://microsoft.github.io/agent-lightning/latest/algorithm-zoo/verl/"},{"title":"[RFC] verl with Agent/Env · Issue #1172 · volcengine/verl","url":"https://github.com/volcengine/verl/issues/1172"},{"title":"Ray+RAGEN - dstack","url":"https://dstack.ai/examples/distributed-training/ray-ragen/"},{"title":"The Right Way To Work Across Multiple Repos with AI Agents","url":"https://www.linkedin.com/pulse/meta-repo-right-way-work-across-multiple-repos-ai-agents-gary-sheng-jazme"},{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengq/verl-agent"}]

Based on the search results, here's what I found about the RAGEN architecture with veRL as a submodule and its code structure components:

## RAGEN Architecture Overview

RAGEN's codebase has been restructured with veRL integrated as a submodule, and the architecture has been decomposed into three modules — Environment State Manager, Context Manager, and Agent Proxy.

## Three Core Components

The modular structure divides RAGEN into three components—Environment Manager, Context Manager, and Agent Proxy, making it significantly simpler to add new environments, track environmental dynamics, and run multiple experiments.

## veRL Integration

The first version decomposes RAGEN and veRL for better co-development, taking the latter as a submodule rather than a static directory. This design choice was made to improve collaborative development between the two projects.

## Overall Framework

RAGEN is built around StarPO (State-Thinking-Actions-Reward Policy Optimization), a unified RL framework for training multi-turn, trajectory-level agents with flexible control over reasoning processes, reward assignment mechanisms, and prompt-rollout structures.

The search results show that these architectural changes represent a significant refactoring of RAGEN to improve modularity and maintainability, making it easier for developers to extend the system with new environments and customize agent training behaviors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63b45529-f8d2-4b7a-8ab4-4c5ffeda3554",
  "isSidechain": true,
  "promptId": "4fde07a8-6703-42b2-afaf-fdcd02bc6fea",
  "agentId": "ae2503964ab593ef8",
  "type": "user",
  "uuid": "20e50900-c140-4520-a484-3514787ef700",
  "sourceToolAssistantUUID": "63b45529-f8d2-4b7a-8ab4-4c5ffeda3554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T12:46:09.706Z_

<details><summary>↩ Tool result · `toolu_01RTa7Pp7oTXia2pzBSWHeNG`</summary>

```text
Web search results for query: "verl-agent "group-in-group" policy optimization ALFWorld agent training"

Links: [{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengQ/verl-agent"},{"title":"[2505.10978] Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/abs/2505.10978"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978v1"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://arxiv.org/pdf/2505.10978"},{"title":"verl-agent/recipe/hgpo at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/tree/master/recipe/hgpo"},{"title":"verl-agent/README.md at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/blob/master/README.md"},{"title":"GAGPO: Generalized Advantage Grouped Policy Optimization","url":"https://arxiv.org/html/2605.13217"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training | OpenReview","url":"https://openreview.net/forum?id=QXEhBMNrCW"},{"title":"Hierarchy-of-Groups Policy Optimization for Long-Horizon Agentic Tasks","url":"https://arxiv.org/html/2602.22817v1"},{"title":"Paper page - Group-in-Group Policy Optimization for LLM Agent Training","url":"https://huggingface.co/papers/2505.10978"}]

Based on the search results, here's what I found about verl-agent, "group-in-group" policy optimization, and ALFWorld agent training:

## Overview

verl-agent is an extension of veRL designed for training LLM/VLM agents via RL and is the official code for the paper "Group-in-Group Policy Optimization for LLM Agent Training".

## Group-in-Group Policy Optimization (GiGPO)

GiGPO is a novel RL algorithm that achieves fine-grained credit assignment for LLM agents while preserving the appealing properties of group-based RL: critic-free, low memory, and stable convergence.

The algorithm works through a two-level structure where GiGPO computes macro relative advantages based on groups of complete trajectories at the episode-level, and at the step-level introduces an anchor state grouping mechanism that retroactively constructs step-level groups by identifying repeated environment states across trajectories, with actions stemming from the same state grouped together for micro relative advantage estimation.

## ALFWorld Results

GiGPO delivers fine-grained per-step credit signals and achieves performance gains of > 12% on ALFWorld and > 9% on WebShop over GRPO, all while maintaining the same GPU memory overhead, identical LLM rollout, and incurring little to no additional time cost.

## Technical Features

The supported environments include ALFWorld, Sokoban, SkyRL-Gym, Search-R1, Gym Cards, WebShop, and AppWorld. verl-agent supports a wide range of LLMs, including Qwen3, Qwen3-VL, Qwen2.5, LLaMA3.2, Qwen2.5-VL, and others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0e22b04-c01f-49fd-bfbc-6076428d5d26",
  "isSidechain": true,
  "promptId": "4fde07a8-6703-42b2-afaf-fdcd02bc6fea",
  "agentId": "ae2503964ab593ef8",
  "type": "user",
  "uuid": "37468b55-6125-4554-888f-3ec6772b868f",
  "sourceToolAssistantUUID": "c0e22b04-c01f-49fd-bfbc-6076428d5d26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T12:46:12.493Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BaFvZdjfayiMJP3w5WHqzo`</summary>

```json
{
  "query": "RAGEN VAGEN cost verification reward shaping agent RL training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37468b55-6125-4554-888f-3ec6772b868f",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2V4Ze8YVYiLgwdwKEKn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dcd8a813-d1e5-44e8-adb4-3082c85a408b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3PKCKTapdPb23Hv1KJX72",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5171,
      "cache_read_input_tokens": 20090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5171,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 28 · 2026-05-14T12:46:13.431Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tsn5QP3yfedHPV3LYMeCBc`</summary>

```json
{
  "query": "AgentRL SPEAR Open-AgentRL ALFWorld GRPO training LLM agents 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcd8a813-d1e5-44e8-adb4-3082c85a408b",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2V4Ze8YVYiLgwdwKEKn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfab006b-ec11-4db1-a324-b5c89097145d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3PKCKTapdPb23Hv1KJX72",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5171,
      "cache_read_input_tokens": 20090,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5171
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 20090,
          "cache_creation_input_tokens": 5171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5171,
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

_source line 29 · 2026-05-14T12:46:21.221Z_

<details><summary>↩ Tool result · `toolu_01BaFvZdjfayiMJP3w5WHqzo`</summary>

```text
Web search results for query: "RAGEN VAGEN cost verification reward shaping agent RL training"

Links: [{"title":"RAGEN - RL Agent","url":"https://ragen-ai.github.io/"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via ...","url":"https://arxiv.org/pdf/2504.20073"},{"title":"GitHub - mll-lab-nu/VAGEN: Training VLM agents with multi-turn reinforcement learning · GitHub","url":"https://github.com/RAGEN-AI/VAGEN"},{"title":"VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents | OpenReview","url":"https://openreview.net/forum?id=xpjWEgf8zi"},{"title":"GitHub - mll-lab-nu/RAGEN: RAGEN leverages reinforcement learning to train LLM reasoning agents in interactive, stochastic environments. · GitHub","url":"https://github.com/mll-lab-nu/RAGEN"},{"title":"RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2504.20073v2"},{"title":"VAGEN: Reinforcing World Model Reasoning for Multi-Turn VLM Agents","url":"https://arxiv.org/html/2510.16907v1"},{"title":"[2504.20073] RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning","url":"https://arxiv.org/abs/2504.20073"},{"title":"Zihan Wang's Homepage 王子涵","url":"https://zihanwang314.github.io/"},{"title":"Manling Li on X: \"Agent Training via RL: We have seen a lot of follow up on RAGEN recently and we place the highest priority on making code easy to reuse. VAGEN is another release of this goal but have vision/multimodal counterparts. We are extending the RL Agent Training to web agents, to\" / X","url":"https://x.com/ManlingLi_/status/1904561315114278969"}]

Based on the search results, here's information about RAGEN, VAGEN, cost verification, reward shaping, and agent RL training:

## RAGEN: LLM Agent RL Framework

RAGEN introduces StarPO (State-Thinking-Actions-Reward Policy Optimization), a general framework for trajectory-level agent RL, along with RAGEN, a modular system for training and evaluating LLM agents. RAGEN implements the full training loop—including rollout generation, reward assignment, and trajectory optimization—serving as a research infrastructure for systematic analysis of LLM agent training dynamics under multi-turn and stochastic environments.

## Key Findings on Multi-Turn RL Training

Multi-turn RL training often leads to a recurring instability pattern, Echo Trap, where agents overfit to locally rewarded reasoning patterns, marked by reward variability collapse, entropy drop, and gradient spikes. StarPO-S is a stabilized variant that improves learning robustness through variability-based trajectory filtering, critic baselining, and decoupled clipping.

Without fine-grained, reasoning-aware reward signals, agent reasoning hardly emerge through multi-turn RL and they may show shallow strategies or hallucinated thoughts.

## VAGEN: Vision-Language Agent RL Framework

VAGEN is a multi-turn reinforcement learning framework designed specifically for training vision-language model (VLM) agents, with World Modeling RL being a novel reinforcement learning approach that significantly improves the multi-turn performance of VLMs by explicitly supervising their worldmodel reasoning process.

## Reward Shaping in VAGEN

VAGEN leverages a WorldModeling Reward to densely reward the agent's turn-by-turn state predictions, while its Bi-Level General Advantage Estimation (Bi-Level GAE) enables turn-aware credit assignment. The WorldModeling Reward consistently improves upon the baseline by providing a crucial learning signal for visual understanding, though its effectiveness is limited by the coarse, trajectory-level credit assignment of standard RL.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dcd8a813-d1e5-44e8-adb4-3082c85a408b",
  "isSidechain": true,
  "promptId": "4fde07a8-6703-42b2-afaf-fdcd02bc6fea",
  "agentId": "ae2503964ab593ef8",
  "type": "user",
  "uuid": "79e3fcaa-4767-4529-b3e5-d657dba1be3a",
  "sourceToolAssistantUUID": "dcd8a813-d1e5-44e8-adb4-3082c85a408b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T12:46:22.236Z_

<details><summary>↩ Tool result · `toolu_01Tsn5QP3yfedHPV3LYMeCBc`</summary>

```text
Web search results for query: "AgentRL SPEAR Open-AgentRL ALFWorld GRPO training LLM agents 2025 2026"

Links: [{"title":"yolay/SPEAR-ALFWorld-DrBoT-GRPO-1.5B · Hugging Face","url":"https://huggingface.co/yolay/SPEAR-ALFWorld-DrBoT-GRPO-1.5B"},{"title":"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning","url":"https://arxiv.org/html/2509.22601v3"},{"title":"GitHub - Gen-Verse/Open-AgentRL: [ICML 2026] RLAnything & DemyAgent: General and scalable agentic RL algorithms across terminal, GUI, SWE, and tool-call settings · GitHub","url":"https://github.com/Gen-Verse/Open-AgentRL"},{"title":"Agent2 RL-Bench: Can LLM Agents Engineer Agentic RL Post-Training?","url":"https://arxiv.org/html/2604.10547"},{"title":"GitHub - TencentYoutuResearch/SPEAR: An RL Recipe for Building Agentic LLMs via Self-Imitation on Long-Horizon Agentic Tasks · GitHub","url":"https://github.com/TencentYoutuResearch/SPEAR"},{"title":"GitHub - thinkwee/AgentsMeetRL: Awesome List for Agentic RL · GitHub","url":"https://github.com/thinkwee/AgentsMeetRL"},{"title":"Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning","url":"https://arxiv.org/html/2605.06130"},{"title":"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=Kssko33Ekq"},{"title":"AGENTRL: SCALING AGENTIC REINFORCEMENT ...","url":"https://openreview.net/pdf?id=zq3vAmuUk9"},{"title":"GitHub - WooooDyy/AgentGym-RL: Code and implementations for the paper \"AgentGym-RL: Training LLM Agents for Long-Horizon Decision Making through Multi-Turn Reinforcement Learning\" by Zhiheng Xi et al. · GitHub","url":"https://github.com/WooooDyy/AgentGym-RL"}]

Based on the web search results, here's what I found about these agentic RL approaches and tools:

## SPEAR

SPEAR is a self-imitation learning (SIL) recipe for training agentic LLMs. It extends vanilla SIL by gradually steering policy entropy across stages, with curriculum scheduling that harmonizes intrinsic reward shaping and self-imitation to expedite exploration via frequent tool interactions at the beginning, and strengthen exploitation of successful tactics upon convergence towards familiarity with the environment.

In ALFWorld and WebShop, SPEAR increases the success rates of GRPO/GiGPO/Dr.BoT by up to 16.1%/5.1%/8.6% and 20.7%/11.8%/13.9%, respectively.

## Open-AgentRL

Open-AgentRL is described as "[ICML 2026] RLAnything & DemyAgent: General and scalable agentic RL algorithms across terminal, GUI, SWE, and tool-call settings." After obtaining SFT models, you can start Agentic RL with the GRPO-TCR recipe.

## ALFWorld

ALFWorld is a frequently used benchmark environment. ALFWorld and WebShop require stateful multi-step interaction, and on ALFWorld, an RL-only agent improves from 5.97 to 93.28 via SFT warm-up and GRPO with online rollouts.

## GRPO Training

AGENTRL achieves state-of-the-art results, significantly outperforming GPT-5, Claude-Sonnet-4 and DeepSeek-R1. The approaches typically use PPO, GRPO, RLOO, and REINFORCE++ algorithms for training LLM agents.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfab006b-ec11-4db1-a324-b5c89097145d",
  "isSidechain": true,
  "promptId": "4fde07a8-6703-42b2-afaf-fdcd02bc6fea",
  "agentId": "ae2503964ab593ef8",
  "type": "user",
  "uuid": "feae160e-4a78-4954-9116-bab27cd787e1",
  "sourceToolAssistantUUID": "dfab006b-ec11-4db1-a324-b5c89097145d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-14T12:46:24.841Z_

Now let me save the findings to the project.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "feae160e-4a78-4954-9116-bab27cd787e1",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2V5VDFc5vs92quyTNzp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7aff8ef5-961f-4652-8ee1-1edec08f63ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uq8np8eEGHiKuEeZWaTKdw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2276,
      "cache_read_input_tokens": 25261,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2276,
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

_source line 32 · 2026-05-14T12:46:25.785Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EwXF9QNZvpXC8ATkJriQn1`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__append_idea",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7aff8ef5-961f-4652-8ee1-1edec08f63ef",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2V5VDFc5vs92quyTNzp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2f2f5d3-4391-4b21-8918-59131b53b5e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uq8np8eEGHiKuEeZWaTKdw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2276,
      "cache_read_input_tokens": 25261,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2276
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 96,
          "cache_read_input_tokens": 25261,
          "cache_creation_input_tokens": 2276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2276,
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

_source line 33 · 2026-05-14T12:46:25.788Z_

<details><summary>↩ Tool result · `toolu_01EwXF9QNZvpXC8ATkJriQn1`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2f2f5d3-4391-4b21-8918-59131b53b5e1",
  "isSidechain": true,
  "promptId": "4fde07a8-6703-42b2-afaf-fdcd02bc6fea",
  "agentId": "ae2503964ab593ef8",
  "type": "user",
  "uuid": "209075c1-b7aa-4b45-bd8a-f62cc5e99079",
  "sourceToolAssistantUUID": "a2f2f5d3-4391-4b21-8918-59131b53b5e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-14T12:47:13.640Z_



Here is a comprehensive summary of findings on RAGEN and related frameworks.

---

## RAGEN (Reasoning AGENt)

**Paper:** "RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning" (arXiv 2504.20073, April 2025, revised May 2025)

**Authors:** Zihan Wang, Kangrui Wang, and collaborators from Northwestern University, Stanford University, Microsoft, and others.

**Repository:** https://github.com/RAGEN-AI/RAGEN

**Website:** https://ragen-ai.github.io/

**Documentation:** https://ragen-doc.readthedocs.io/

### Core Contribution: StarPO Framework

StarPO (State-Thinking-Actions-Reward Policy Optimization) is the central algorithm. It is a unified RL framework for training multi-turn, trajectory-level agents. Key properties:

- Agent-environment interactions formulated as MDPs where states and actions are token sequences
- At each step, the model generates `&lt;think>...&lt;/think>&lt;ans> action &lt;/ans>`, and the environment returns feedback (reward + next state)
- Optimizes **entire trajectories** using importance sampling, not step-by-step
- Supports both GRPO and PPO with GAE as optimization backends
- GRPO mode assigns normalized reward to the full trajectory

### Architecture (Refactored)

RAGEN's codebase was restructured with **veRL integrated as a submodule**. Three core modules:
1. **Environment State Manager** — manages environment dynamics
2. **Context Manager** — tracks conversation/interaction context
3. **Agent Proxy** — interfaces the LLM with the environment

### Built-in Environments (10)

Sokoban, FrozenLake, WebShop, DeepCoder, SearchQA, Lean, Bandit, Countdown, MetaMathQA, Sudoku. **ALFWorld is NOT among the built-in environments.**

### Key Finding: Echo Trap

Multi-turn RL training exhibits a recurring instability pattern called "Echo Trap" — reward variance collapses, entropy drops, and gradient spikes. The agent overfits to locally rewarded reasoning patterns.

**Solution — StarPO-S:** A stabilized variant with:
- Variability-based trajectory filtering
- Critic incorporation (baselining)
- Decoupled clipping / gradient stabilization

### Key Design Insights

- RL rollouts benefit from diverse initial states
- Medium interaction granularity works best
- More frequent sampling improves training
- Without fine-grained, reasoning-aware reward signals, agent reasoning hardly emerges; models show shallow strategies or hallucinated thoughts

---

## RAGEN-2: Reasoning Collapse in Agentic RL

**Paper:** arXiv 2604.06268 (April 2026)

Identifies a new failure mode called **Template Collapse**: even with stable entropy, models can rely on fixed templates that look diverse but are input-agnostic. Entropy cannot detect this.

**Solution:** Decompose reasoning quality into:
- Within-input diversity (Entropy)
- Cross-input distinguishability (Mutual Information, MI)

Mutual information correlates with final performance much more strongly than entropy. Proposes **SNR-Adaptive Filtering** — uses reward variance as a lightweight proxy to select high-signal prompts per iteration.

---

## VAGEN (Vision-Language Extension)

**Repository:** https://github.com/RAGEN-AI/VAGEN

A multi-turn RL framework for training **VLM agents**. Introduces:
- **WorldModeling Reward** — densely rewards turn-by-turn state predictions
- **Bi-Level GAE** — turn-aware credit assignment

---

## Related Frameworks for Agent RL on Interactive Environments

### verl-agent (GiGPO)

**Paper:** "Group-in-Group Policy Optimization for LLM Agent Training" (arXiv 2505.10978)
**Repository:** https://github.com/langfengQ/verl-agent

Extension of veRL for agent RL. Introduces **GiGPO** — two-level group-based credit assignment:
- Episode-level: macro relative advantages from groups of complete trajectories
- Step-level: anchor state grouping mechanism for micro relative advantages

**ALFWorld results:** GiGPO achieves >12% improvement over GRPO on ALFWorld and >9% on WebShop, with same GPU memory overhead.

**Supported environments:** ALFWorld, Sokoban, SkyRL-Gym, Search-R1, Gym Cards, WebShop, AppWorld.

### SPEAR (Tencent)

**Repository:** https://github.com/TencentYoutuResearch/SPEAR

Self-imitation learning recipe that extends vanilla SIL with progressive exploration. On ALFWorld, SPEAR increases success rates of GRPO/GiGPO by up to 16.1%/5.1%. An RL-only agent on ALFWorld improves from 5.97 to 93.28 via SFT warm-up + GRPO with online rollouts.

### Open-AgentRL (ICML 2026)

**Repository:** https://github.com/Gen-Verse/Open-AgentRL

General and scalable agentic RL algorithms (RLAnything & DemyAgent) across terminal, GUI, SWE, and tool-call settings. Uses GRPO-TCR recipe.

### AgentRL

Achieves state-of-the-art on ALFWorld and other benchmarks. Applied to Qwen2.5 and GLM-4-9B. Claims to outperform GPT-5 and DeepSeek-R1.

### OpenRLHF

**Repository:** https://github.com/openrlhf/openrlhf

First RLHF framework with unified agent-based paradigm. Ray + vLLM distributed architecture. v0.10 adds multi-turn VLM RL. Supports PPO, DAPO, REINFORCE++.

### veRL (ByteDance)

**Repository:** https://github.com/verl-project/verl
**Agentic RL docs:** https://verl.readthedocs.io/en/latest/start/agentic_rl.html

High-performance RL post-training framework. Has agentic RL integration with environment support for TextWorld, ALFWorld, SWE-Gym.

---

## Summary Table

| Framework | Base RL Algo | ALFWorld Support | Key Innovation | Built on |
|-----------|-------------|-----------------|----------------|----------|
| RAGEN | GRPO/PPO (StarPO) | No (10 other envs) | Trajectory-level optimization, Echo Trap diagnosis | veRL (submodule) |
| verl-agent | GiGPO | Yes | Two-level group credit assignment | veRL |
| SPEAR | GRPO/GiGPO augmented | Yes | Self-imitation + progressive exploration | veRL |
| Open-AgentRL | GRPO-TCR | Yes | General across terminal/GUI/SWE | Custom |
| OpenRLHF | PPO/DAPO/REINFORCE++ | Via extensions | Unified agent paradigm, Ray+vLLM | Ray |
| veRL | GRPO/PPO | Yes (via docs) | Scalable RL post-training | Ray |

**Key takeaway for cost-verify-agent-rl:** RAGEN is the most mature research framework for understanding multi-turn agent RL dynamics (Echo Trap, Template Collapse), but does **not** include ALFWorld natively. For ALFWorld-specific agent GRPO training, **verl-agent** (GiGPO) and **SPEAR** are the most directly relevant, both built on veRL. RAGEN's StarPO framework and its diagnostic insights (reward variance monitoring, trajectory filtering) are highly transferable regardless of which codebase you build on.

Sources:
- [RAGEN GitHub](https://github.com/RAGEN-AI/RAGEN)
- [RAGEN Paper (arXiv 2504.20073)](https://arxiv.org/abs/2504.20073)
- [RAGEN Paper HTML](https://arxiv.org/html/2504.20073v2)
- [RAGEN Project Website](https://ragen-ai.github.io/)
- [RAGEN Documentation](https://ragen-doc.readthedocs.io/)
- [RAGEN-2 Paper (arXiv 2604.06268)](https://arxiv.org/abs/2604.06268)
- [VAGEN GitHub](https://github.com/RAGEN-AI/VAGEN)
- [verl-agent GitHub (GiGPO)](https://github.com/langfengQ/verl-agent)
- [GiGPO Paper (arXiv 2505.10978)](https://arxiv.org/abs/2505.10978)
- [SPEAR GitHub](https://github.com/TencentYoutuResearch/SPEAR)
- [Open-AgentRL GitHub](https://github.com/Gen-Verse/Open-AgentRL)
- [OpenRLHF GitHub](https://github.com/openrlhf/openrlhf)
- [veRL GitHub](https://github.com/verl-project/verl)
- [veRL Agentic RL Docs](https://verl.readthedocs.io/en/latest/start/agentic_rl.html)
- [MarkTechPost: StarPO-S and RAGEN](https://www.marktechpost.com/2025/05/01/training-llm-agents-just-got-more-stable-researchers-introduce-starpo-s-and-ragen-to-tackle-multi-turn-reasoning-and-collapse-in-reinforcement-learning/)
- [Lambda + dstack + RAGEN](https://lambda.ai/blog/agent-training-on-lambda-with-dstack-and-ragen)
- [SPEAR ALFWorld Model on HuggingFace](https://huggingface.co/yolay/SPEAR-ALFWorld-DrBoT-GRPO-1.5B)
- [Practitioner's Guide to Multi-turn Agentic RL](https://arxiv.org/html/2510.01132)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "209075c1-b7aa-4b45-bd8a-f62cc5e99079",
  "isSidechain": true,
  "agentId": "ae2503964ab593ef8",
  "requestId": "req_011Cb2V5kfgVCCqW4LL1wt28",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97bad3bc-fe9e-4d90-87dd-1aece213316e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7c643047-3532-4f35-b805-e1c1d19cdbc4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSsxMXVEDe1g317N4vDMHv",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 304,
      "cache_read_input_tokens": 27537,
      "output_tokens": 2518,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 304
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2518,
          "cache_read_input_tokens": 27537,
          "cache_creation_input_tokens": 304,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 304,
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
