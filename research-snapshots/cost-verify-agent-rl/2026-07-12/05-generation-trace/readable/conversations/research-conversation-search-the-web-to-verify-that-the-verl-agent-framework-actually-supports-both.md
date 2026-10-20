# Research conversation: Search the web to verify that the verl-agent framework actually supports both WebShop and ALFWorld environments for GRPO

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ac4d68c97c739d58b.jsonl`
- **Structured JSON:** [`e4c1710265567da793ff.json`](../../sessions/e4/e4c1710265567da793ff.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-10T20:03:05.369Z_

Search the web to verify that the verl-agent framework actually supports both WebShop and ALFWorld environments for GRPO/GiGPO training. This is critical for the feasibility of a proposal that relies on verl-agent's existing infrastructure.

1. Search: "verl-agent WebShop ALFWorld GRPO training"
2. Search: "site:github.com langfengQ/verl-agent" to check the repo
3. Search: "verl-agent GiGPO Qwen2.5-7B-Instruct WebShop checkpoint"
4. Search: "verl-agent supported environments benchmarks"

Report: Does verl-agent actually support both WebShop and ALFWorld? Are there published checkpoints for both? What environments does the framework list as supported?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ba5b4988-e176-4ed2-b1ad-ac04b7ed88a5",
  "agentId": "ac4d68c97c739d58b",
  "type": "user",
  "uuid": "dfd0c851-4df5-405c-bee2-09f653d85e74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f5ed35e7-5a57-4805-b2c9-5a4a3ba21b2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T20:03:06.623Z_

I'll search for information about verl-agent's support for WebShop and ALFWorld environments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfd0c851-4df5-405c-bee2-09f653d85e74",
  "isSidechain": true,
  "agentId": "ac4d68c97c739d58b",
  "requestId": "req_011CauV9NQ4n7QWFy2EN2Xn4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "72300d35-09a0-44b5-bc0e-5b4ec2d9aa96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f5ed35e7-5a57-4805-b2c9-5a4a3ba21b2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EWfD1TTsizyaDm7z41CcBE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 610,
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

_source line 3 · 2026-05-10T20:03:06.789Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TuoL3hjxP7jJPHVR1JJVXu`</summary>

```json
{
  "query": "verl-agent WebShop ALFWorld GRPO training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72300d35-09a0-44b5-bc0e-5b4ec2d9aa96",
  "isSidechain": true,
  "agentId": "ac4d68c97c739d58b",
  "requestId": "req_011CauV9NQ4n7QWFy2EN2Xn4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a17e6ba4-f1b6-4104-9884-4f1782f2bf81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f5ed35e7-5a57-4805-b2c9-5a4a3ba21b2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EWfD1TTsizyaDm7z41CcBE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 610,
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

_source line 4 · 2026-05-10T20:03:07.030Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KXvTouUozoYmGkVZP9VNpQ`</summary>

```json
{
  "query": "site:github.com langfengQ/verl-agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a17e6ba4-f1b6-4104-9884-4f1782f2bf81",
  "isSidechain": true,
  "agentId": "ac4d68c97c739d58b",
  "requestId": "req_011CauV9NQ4n7QWFy2EN2Xn4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7bdb5e0d-26c7-4a5e-aa14-d226f84113c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f5ed35e7-5a57-4805-b2c9-5a4a3ba21b2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EWfD1TTsizyaDm7z41CcBE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 610,
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

_source line 5 · 2026-05-10T20:03:07.225Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FWnPzbzCK9eCmR98c8BL9t`</summary>

```json
{
  "query": "verl-agent GiGPO Qwen2.5-7B-Instruct WebShop checkpoint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bdb5e0d-26c7-4a5e-aa14-d226f84113c2",
  "isSidechain": true,
  "agentId": "ac4d68c97c739d58b",
  "requestId": "req_011CauV9NQ4n7QWFy2EN2Xn4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b9190a0e-2a7e-4d30-a338-9bcb738b680e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f5ed35e7-5a57-4805-b2c9-5a4a3ba21b2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EWfD1TTsizyaDm7z41CcBE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 16153,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 610
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 238,
          "cache_read_input_tokens": 16153,
          "cache_creation_input_tokens": 610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 610,
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

### Tool call

_source line 6 · 2026-05-10T20:03:07.240Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DgjtHpACqfd3ahH2C1CFxq`</summary>

```json
{
  "query": "verl-agent supported environments benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9190a0e-2a7e-4d30-a338-9bcb738b680e",
  "isSidechain": true,
  "agentId": "ac4d68c97c739d58b",
  "requestId": "req_011CauV9NQ4n7QWFy2EN2Xn4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dc13113b-cd52-4da9-8e43-3c041fbc3a5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f5ed35e7-5a57-4805-b2c9-5a4a3ba21b2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EWfD1TTsizyaDm7z41CcBE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 16153,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 610
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 238,
          "cache_read_input_tokens": 16153,
          "cache_creation_input_tokens": 610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 610,
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

_source line 7 · 2026-05-10T20:03:13.391Z_

<details><summary>↩ Tool result · `toolu_01FWnPzbzCK9eCmR98c8BL9t`</summary>

```text
Web search results for query: "verl-agent GiGPO Qwen2.5-7B-Instruct WebShop checkpoint"

Links: [{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengQ/verl-agent"},{"title":"langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop · Hugging Face","url":"https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop"},{"title":"Qwen/Qwen2.5-VL-7B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct"},{"title":"unsloth/Qwen2.5-VL-7B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Qwen2.5-VL-7B-Instruct-GGUF"},{"title":"langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld · Hugging Face","url":"https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld"},{"title":"Qwen2.5-VL 7B","url":"https://qwen.ai/blog?id=qwen2.5-vl"},{"title":"verl-agent/recipe/hgpo at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/tree/master/recipe/hgpo"},{"title":"Qwen/Qwen2-VL-7B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct"},{"title":"Qwen/Qwen2.5-VL-72B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct"},{"title":"Qwen2.5-VL 7B Instruct - API, Providers, Stats | OpenRouter","url":"https://openrouter.ai/qwen/qwen-2.5-vl-7b-instruct:free"}]

Based on the search results, I found relevant information about your query:

verl-agent includes implementations of various RL algorithms, such as GRPO, PPO, DAPO, GSPO, RLOO and GiGPO, which is a state-of-the-art algorithm for agent training.

Specifically, there is a GiGPO-Qwen2.5-7B-Instruct-WebShop checkpoint trained using GiGPO available on Hugging Face. This model is part of the verl-agent project, which offers a diverse set of interactive environments including WebShop.

GiGPO is a novel algorithm designed to support fine-grained credit assignment in long-horizon LLM agent training. It introduces a two-level grouping mechanism: Episode-level groups capture overall task success via total returns (like GRPO). Step-level groups gather repeated states across trajectories to compute relative advantages for individual actions.

To use this model, please refer to verl-agent, and the checkpoint is available on the Hugging Face Model Hub under the repository name `langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop`.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9190a0e-2a7e-4d30-a338-9bcb738b680e",
  "isSidechain": true,
  "promptId": "ba5b4988-e176-4ed2-b1ad-ac04b7ed88a5",
  "agentId": "ac4d68c97c739d58b",
  "type": "user",
  "uuid": "00f365fd-cdf4-45db-aa7b-a9847f006846",
  "sourceToolAssistantUUID": "b9190a0e-2a7e-4d30-a338-9bcb738b680e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f5ed35e7-5a57-4805-b2c9-5a4a3ba21b2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T20:03:14.695Z_

<details><summary>↩ Tool result · `toolu_01KXvTouUozoYmGkVZP9VNpQ`</summary>

```text
Web search results for query: "site:github.com langfengQ/verl-agent"

Links: [{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengq/verl-agent"},{"title":"Releases · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/releases"},{"title":"langfengQ (Lang Feng) · GitHub","url":"https://github.com/langfengQ"},{"title":"verl-agent/agent_system/environments/base.py at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/blob/master/agent_system/environments/base.py"},{"title":"verl-agent/recipe/hgpo at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/tree/master/recipe/hgpo"},{"title":"verl-agent/README.md at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/blob/master/README.md"},{"title":"verl-agent/examples/data_preprocess/preprocess_search_r1_dataset.py at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/blob/master/examples/data_preprocess/preprocess_search_r1_dataset.py"},{"title":"Issues · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/issues"},{"title":"verl-agent/examples at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/tree/master/examples"},{"title":"verl-agent/verl/trainer/config/ppo_trainer.yaml at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/blob/master/verl/trainer/config/ppo_trainer.yaml"}]

Based on the search results, here's what I found about the langfengQ/verl-agent repository:

## Overview

verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper "Group-in-Group Policy Optimization for LLM Agent Training".

## Key Features

**Customizable Memory & Input Structure**: verl-agent features a customizable memory module that allows for flexibly choosing what history to include for each step. Unlike prior works like RAGEN and Search-R1 that concatenate the entire history of states and responses, verl-agent avoids rapid context length growth with the number of turns, making it easier to scale to long-horizon scenarios.

**Multi-modal Support**: Beyond text-based agents, verl-agent also supports training vision-language agents, enabling multi-modal reasoning in environments where both visual perception and language understanding are required.

**Diverse Environments**: verl-agent offers a diverse set of interactive environments including Search-R1 experiment, embodied AI environments like ALFWorld, visual games such as Sokoban and Gym Cards, and digital interface control tasks like WebShop and AppWorld.

**Supported Models & Algorithms**: verl-agent supports a wide range of LLMs, including Qwen3, Qwen3-VL, Qwen2.5, LLaMA3.2, Qwen2.5-VL, and others. verl-agent includes implementations of various RL algorithms, such as GRPO, PPO, DAPO, GSPO, RLOO and their new state-of-the-art algorithm GiGPO.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bdb5e0d-26c7-4a5e-aa14-d226f84113c2",
  "isSidechain": true,
  "promptId": "ba5b4988-e176-4ed2-b1ad-ac04b7ed88a5",
  "agentId": "ac4d68c97c739d58b",
  "type": "user",
  "uuid": "b345b690-5ee8-4415-9d69-4d1db15893a8",
  "sourceToolAssistantUUID": "7bdb5e0d-26c7-4a5e-aa14-d226f84113c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f5ed35e7-5a57-4805-b2c9-5a4a3ba21b2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T20:03:14.756Z_

<details><summary>↩ Tool result · `toolu_01DgjtHpACqfd3ahH2C1CFxq`</summary>

```text
Web search results for query: "verl-agent supported environments benchmarks"

Links: [{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengQ/verl-agent"},{"title":"verl-agent/README.md at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/blob/master/README.md"},{"title":"Dongfu Jiang on X: \"Introducing VerlTool - a unified and easy-to-extend tool agent training framework based on verl. Recently, there's been a growing trend toward training tool agents with reinforcement learning algorithms like GRPO and PPO. Representative works include SearchR1, ToRL, ReTool, and https://t.co/dF6lcpg7C9\" / X","url":"https://x.com/DongfuJiang/status/1929198238017720379"},{"title":"VERL - Agent-lightning","url":"https://microsoft.github.io/agent-lightning/latest/algorithm-zoo/verl/"},{"title":"Verl: State-of-the-art RL Training for LLMs — SkyPilot Docs","url":"https://docs.skypilot.co/en/latest/examples/training/verl.html"},{"title":"Agentic RL frameworks and environments: Torchforge, ACE, Verl, openenv | by evoailabs | Medium","url":"https://evoailabs.medium.com/agentic-rl-frameworks-torchforge-ace-verl-3dd116b987dc"},{"title":"VerlTool: Towards Holistic Agentic Reinforcement Learning with Tool Use","url":"https://arxiv.org/html/2509.01055v1"},{"title":"Verlog - A Multi-turn RL framework for LLM agents | Agentic Intelligence Lab","url":"https://agentic-intelligence-lab.org/2025/08/15/technical-post.html"},{"title":"Training a Coding Agent with veRL - a Lightning environment by lantiga","url":"https://lightning.ai/lightning-ai/environments/training-a-coding-agent-with-verl"},{"title":"Verl-Tool: Towards Holistic Agentic Reinforcement Learning with Tool Use | OpenReview","url":"https://openreview.net/forum?id=oWFtI0cNsE"}]

Based on the search results, here's information about verl-agent's supported environments and benchmarks:

## Supported Environments

verl-agent's supported environments are adapted from ALFWorld, Sokoban, SkyRL-Gym, Search-R1, Gym Cards, WebShop, and AppWorld. More specifically, verl-agent offers a diverse set of interactive environments including Search-R1 experiment, embodied AI environments like ALFWorld, visual games such as Sokoban and Gym Cards, and digital interface control tasks like WebShop and AppWorld (experimental).

Beyond text-based agents, verl-agent also supports training vision-language agents, enabling multi-modal reasoning in environments where both visual perception and language understanding are required.

## Supported RL Algorithms

verl-agent includes implementations of various RL algorithms, such as GRPO, PPO, DAPO, GSPO, RLOO and the state-of-the-art algorithm GiGPO, and it also supports several variants enhanced with dynamic sampling and clip-higher techniques.

## Related Benchmarking Framework

There's also VerlTool, which extends verl-agent's capabilities for tool use. VT-Math achieves 62.2% average performance on mathematical benchmarks, VT-Search reaches 45.9% on knowledge QA, VT-SQL matches specialized systems like SkyRL-SQL, and VT-VisualReasoner achieves 82.7% on V* Bench while VT-DeepSearch reaches 34.0% on GAIA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc13113b-cd52-4da9-8e43-3c041fbc3a5d",
  "isSidechain": true,
  "promptId": "ba5b4988-e176-4ed2-b1ad-ac04b7ed88a5",
  "agentId": "ac4d68c97c739d58b",
  "type": "user",
  "uuid": "5d5ba17a-48a8-47b6-834a-c7c5c36ed6a8",
  "sourceToolAssistantUUID": "dc13113b-cd52-4da9-8e43-3c041fbc3a5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f5ed35e7-5a57-4805-b2c9-5a4a3ba21b2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T20:03:15.879Z_

<details><summary>↩ Tool result · `toolu_01TuoL3hjxP7jJPHVR1JJVXu`</summary>

```text
Web search results for query: "verl-agent WebShop ALFWorld GRPO training"

Links: [{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengQ/verl-agent"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978v1"},{"title":"GRPO & DAPO | langfengQ/verl-agent | DeepWiki","url":"https://deepwiki.com/langfengQ/verl-agent/6.4-grpo-and-dapo"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://arxiv.org/pdf/2505.10978"},{"title":"A Practitioner’s Guide to Multi-turn Agentic Reinforcement Learning","url":"https://arxiv.org/html/2510.01132"},{"title":"verl-agent/recipe/hgpo at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/tree/master/recipe/hgpo"},{"title":"verl-agent/README.md at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/blob/master/README.md"},{"title":"GitHub - aiming-lab/SkillRL: SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning · GitHub","url":"https://github.com/aiming-lab/SkillRL"},{"title":"Agent2 RL-Bench: Can LLM Agents Engineer Agentic RL Post-Training?","url":"https://arxiv.org/html/2604.10547"},{"title":"AgentFly: Extensible and Scalable Reinforcement Learning for LM Agents","url":"https://arxiv.org/html/2507.14897v1"}]

Based on the search results, here's what I found about verl-agent, WebShop, ALFWorld, and GRPO training:

## Overview

verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for the paper "Group-in-Group Policy Optimization for LLM Agent Training"

## Supported Environments and Algorithms

verl-agent offers a diverse set of interactive environments including Search-R1 experiment, embodied AI environments like ALFWorld, visual games such as Sokoban and Gym Cards, and digital interface control tasks like WebShop and AppWorld

verl-agent includes implementations of various RL algorithms, such as GRPO, PPO, DAPO, GSPO, RLOO and its new state-of-the-art algorithm GiGPO.

## GRPO in verl-agent

GRPO (Group Relative Policy Optimization) and DAPO (Dynamic Adaptive Policy Optimization) are critic-free advantage estimation algorithms. GRPO computes advantages by comparing trajectories within groups, while DAPO extends GRPO with dynamic sampling to improve data quality through trajectory filtering.

Group environments are especially useful for algorithms like GRPO and DAPO that require multiple rollouts on the same state.

## Scalability for Long-Horizon Tasks

verl-agent's design keeps the context length almost constant over time, making verl-agent highly scalable for long-horizon scenarios (e.g., 30–50 steps in ALFWorld) without running into token limits or inefficiency.

## Performance Results

GiGPO achieves performance improvement of > 12% on ALFWorld and > 9% on WebShop over GRPO.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a17e6ba4-f1b6-4104-9884-4f1782f2bf81",
  "isSidechain": true,
  "promptId": "ba5b4988-e176-4ed2-b1ad-ac04b7ed88a5",
  "agentId": "ac4d68c97c739d58b",
  "type": "user",
  "uuid": "bb1a1de4-87f6-41ad-9b06-e2fcb8ab6c2e",
  "sourceToolAssistantUUID": "a17e6ba4-f1b6-4104-9884-4f1782f2bf81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f5ed35e7-5a57-4805-b2c9-5a4a3ba21b2f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T20:03:22.548Z_

## Verification Report: verl-agent Framework Support

Based on comprehensive web searches, I can confirm the following findings:

### Does verl-agent Support Both WebShop and ALFWorld?

**YES - Both environments are explicitly supported.**

The framework documentation confirms verl-agent offers "a diverse set of interactive environments including Search-R1 experiment, embodied AI environments like ALFWorld, visual games such as Sokoban and Gym Cards, and digital interface control tasks like WebShop and AppWorld."

### Are There Published Checkpoints for Both?

**YES - Published checkpoints exist on Hugging Face:**

- **WebShop**: `langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop` - A GiGPO-trained checkpoint available on Hugging Face
- **ALFWorld**: `langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld` - A GiGPO-trained checkpoint available on Hugging Face

These checkpoints demonstrate that the framework has been successfully used for training agents on both environments using the GiGPO algorithm.

### What Environments Does the Framework List as Supported?

verl-agent officially supports:
- **ALFWorld** (embodied AI environment)
- **WebShop** (digital interface control task)
- **Sokoban** (visual game)
- **Gym Cards** (visual game)
- **Search-R1** (search/reasoning experiment)
- **AppWorld** (experimental, digital interface control)

### Supported RL Algorithms

The framework implements multiple algorithms:
- GRPO (Group Relative Policy Optimization)
- PPO (Proximal Policy Optimization)
- DAPO (Dynamic Adaptive Policy Optimization)
- GSPO (Group Soft Policy Optimization)
- RLOO (Reward Logits Optimization)
- **GiGPO** (Group-in-Group Policy Optimization) - newest state-of-the-art algorithm

GiGPO shows significant performance improvements: >12% on ALFWorld and >9% on WebShop over GRPO.

### Critical Finding for Your Proposal

**The infrastructure is proven and publicly available.** The verl-agent framework not only supports both WebShop and ALFWorld, but it has already demonstrated successful training on both environments with published checkpoints and benchmark results. This significantly de-risks a proposal relying on this infrastructure.

Sources:
- [GitHub - langfengQ/verl-agent](https://github.com/langfengQ/verl-agent)
- [Group-in-Group Policy Optimization for LLM Agent Training](https://arxiv.org/html/2505.10978v1)
- [GiGPO-Qwen2.5-7B-Instruct-WebShop](https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-WebShop)
- [GiGPO-Qwen2.5-7B-Instruct-ALFWorld](https://huggingface.co/langfeng01/GiGPO-Qwen2.5-7B-Instruct-ALFWorld)
- [verl-agent README](https://github.com/langfengQ/verl-agent/blob/master/README.md)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb1a1de4-87f6-41ad-9b06-e2fcb8ab6c2e",
  "isSidechain": true,
  "agentId": "ac4d68c97c739d58b",
  "requestId": "req_011CauVA9KnnBE4KrLao12jA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "622ef45e-4e73-4823-9192-9ee988160491",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f5ed35e7-5a57-4805-b2c9-5a4a3ba21b2f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GLzFuyG5UNiMP27vvEc5Ut",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3066,
      "cache_creation_input_tokens": 2029,
      "cache_read_input_tokens": 16763,
      "output_tokens": 810,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2029
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3066,
          "output_tokens": 810,
          "cache_read_input_tokens": 16763,
          "cache_creation_input_tokens": 2029,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2029,
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
