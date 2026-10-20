# Research conversation: I need to research two papers: 1. **CoBA-RL** (arXiv:2602.03048): "Capability-Oriented Budget Allocation for RL in LLMs"

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a11d1541bbbc8a5e8.jsonl`
- **Structured JSON:** [`3b7b1443728b7943ca18.json`](../../sessions/3b/3b7b1443728b7943ca18.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

39 recorded events

### User

_source line 1 · 2026-05-11T23:29:06.642Z_

I need to research two papers:

1. **CoBA-RL** (arXiv:2602.03048): "Capability-Oriented Budget Allocation for RL in LLMs" - proposes adaptive rollout budget allocation based on task difficulty using Beta distribution.

2. **RC-GRPO** (arXiv:2602.03025): "Reward-Conditioned GRPO for Multi-Turn Tool Calling" - addresses low reward variation within GRPO groups via reward-conditioned trajectory generation.

For each paper:
1. Use WebSearch to find the paper with the arXiv ID and title keywords
2. Use WebFetch to read the actual abstract and method from arxiv.org
3. Search for related work on adaptive budget allocation in RL for LLMs

I need to understand:
- For CoBA-RL: How does the Beta distribution-based budget allocation work? What is "capability-oriented"? How does difficulty estimation work? What benchmarks?
- For RC-GRPO: What is "reward-conditioned" trajectory generation? How does it address low reward variation? What benchmarks? Is it specific to tool calling?

Also search for "Knapsack RL ICLR 2026" which is mentioned as another budget allocation method.

Report all findings in detail. If papers don't exist at those IDs, report that clearly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a11d1541bbbc8a5e8",
  "type": "user",
  "uuid": "5275e45c-c99d-4d06-b0b5-67ca29f8a743",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T23:29:06.649Z_

```json
{
  "parentUuid": "5275e45c-c99d-4d06-b0b5-67ca29f8a743",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
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
  "uuid": "93617886-a08f-4699-a586-263382b4278f",
  "timestamp": "2026-05-11T23:29:06.649Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T23:29:09.025Z_



I'll research all three papers systematically. Let me start by loading the WebSearch and WebFetch tools, then search for all papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93617886-a08f-4699-a586-263382b4278f",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawefVNuKftSMXYaHkij2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e38f02a5-ff8d-4b72-bdc9-76899fc357a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017x41y9RZnxMk4683xQ9C6E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 858,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 858,
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

_source line 4 · 2026-05-11T23:29:09.548Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Cr7ntogKJh8TCnJTgxPCb1`</summary>

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
  "parentUuid": "e38f02a5-ff8d-4b72-bdc9-76899fc357a6",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawefVNuKftSMXYaHkij2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "838aede9-8d08-4195-889a-a993d6f6c345",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017x41y9RZnxMk4683xQ9C6E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 858,
      "cache_read_input_tokens": 8223,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 858
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 858,
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

_source line 5 · 2026-05-11T23:29:09.550Z_

<details><summary>↩ Tool result · `toolu_01Cr7ntogKJh8TCnJTgxPCb1`</summary>

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
  "parentUuid": "838aede9-8d08-4195-889a-a993d6f6c345",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a11d1541bbbc8a5e8",
  "type": "user",
  "uuid": "1e070387-db90-4845-898c-3d1b177007f4",
  "sourceToolAssistantUUID": "838aede9-8d08-4195-889a-a993d6f6c345",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T23:29:12.232Z_



Now let me search for all three papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e070387-db90-4845-898c-3d1b177007f4",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawefhwwjDXkUAG29MLfs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4bd4b9ea-721a-49d6-bb98-440166686982",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBTs1PyLw85tfD94h8MBfQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1921,
      "cache_read_input_tokens": 9081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1921,
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

_source line 7 · 2026-05-11T23:29:13.393Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TDKSnTdjKkEpHHeZPQo1SE`</summary>

```json
{
  "query": "CoBA-RL arXiv 2602.03048 Capability-Oriented Budget Allocation RL LLMs Beta distribution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bd4b9ea-721a-49d6-bb98-440166686982",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawefhwwjDXkUAG29MLfs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "39515a85-1840-417b-9e24-6434dc27f738",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBTs1PyLw85tfD94h8MBfQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1921,
      "cache_read_input_tokens": 9081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1921,
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

_source line 8 · 2026-05-11T23:29:14.210Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011LwMo3nziLSkSn1iCJUFsP`</summary>

```json
{
  "query": "RC-GRPO arXiv 2602.03025 Reward-Conditioned GRPO Multi-Turn Tool Calling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39515a85-1840-417b-9e24-6434dc27f738",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawefhwwjDXkUAG29MLfs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e48289e3-5adc-4602-8f5e-cc43f0be19dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBTs1PyLw85tfD94h8MBfQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1921,
      "cache_read_input_tokens": 9081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1921,
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

_source line 9 · 2026-05-11T23:29:15.009Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012qDziuwjqWGtjs6Rxa21o6`</summary>

```json
{
  "query": "Knapsack RL ICLR 2026 budget allocation reinforcement learning LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e48289e3-5adc-4602-8f5e-cc43f0be19dd",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawefhwwjDXkUAG29MLfs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5271511c-c4ee-4856-bd52-e5d344f32191",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TBTs1PyLw85tfD94h8MBfQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1921,
      "cache_read_input_tokens": 9081,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1921
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 9081,
          "cache_creation_input_tokens": 1921,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1921,
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

_source line 10 · 2026-05-11T23:29:19.355Z_

<details><summary>↩ Tool result · `toolu_01TDKSnTdjKkEpHHeZPQo1SE`</summary>

```text
Web search results for query: "CoBA-RL arXiv 2602.03048 Capability-Oriented Budget Allocation RL LLMs Beta distribution"

Links: [{"title":"CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs","url":"https://arxiv.org/html/2602.03048"},{"title":"[2602.03048] CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs","url":"https://arxiv.org/abs/2602.03048"},{"title":"GitHub - Within-yao/CoBA-RL: CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs · GitHub","url":"https://github.com/Within-yao/CoBA-RL"},{"title":"Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation","url":"https://arxiv.org/html/2509.25849v1"},{"title":"BARD: Budget-Aware Reasoning Distillation","url":"https://arxiv.org/html/2511.01470"},{"title":"DARA: Few-shot Budget Allocation in Online Advertising via In-Context Decision Making with RL-Finetuned LLMs","url":"https://arxiv.org/html/2601.14711v1"},{"title":"A Relative-Budget Theory for Reinforcement Learning with Verifiable Rewards in Large Language Model Reasoning","url":"https://arxiv.org/html/2602.01523"},{"title":"Capacity-Aware Planning and Scheduling in Budget-Constrained Monotonic MDPs: A Meta-RL Approach","url":"https://arxiv.org/html/2410.21249v1"},{"title":"Approximation Algorithm for Generalized Budgeted Assignment Problems and Applications in Transportation Systems","url":"https://arxiv.org/html/2208.11832"},{"title":"Alloc-MoE: Budget-Aware Expert Activation Allocation for Efficient Mixture-of-Experts Inference","url":"https://arxiv.org/html/2604.08133v1"}]

Based on the search results, I found the paper you're looking for:

**CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs**

This paper addresses Reinforcement Learning with Verifiable Rewards (RLVR) as a key approach for enhancing LLM reasoning. Standard frameworks like Group Relative Policy Optimization (GRPO) typically employ a uniform rollout budget, leading to resource inefficiency.

CoBA-RL is a reinforcement learning algorithm designed to adaptively allocate rollout budgets based on the model's evolving capability, utilizing a Capability-Oriented Value function to map tasks to their potential training gains and employing a heap-based greedy strategy to efficiently self-calibrate the distribution of computational resources.

The paper was submitted on February 3, 2026 and last revised on February 6, 2026. The authors include Zhiyuan Yao, Yi-Kai Zhang, Yuxin Chen, Yueqing Sun, Zishan Xu, Yu Yang, Tianhao Hu, Qi Gu, Hui Su, and Xunliang Cai.

You can access the full paper at: https://arxiv.org/abs/2602.03048


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39515a85-1840-417b-9e24-6434dc27f738",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a11d1541bbbc8a5e8",
  "type": "user",
  "uuid": "c177fea2-96ba-47ff-a66d-ce72c6878e95",
  "sourceToolAssistantUUID": "39515a85-1840-417b-9e24-6434dc27f738",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-11T23:29:23.586Z_

<details><summary>↩ Tool result · `toolu_011LwMo3nziLSkSn1iCJUFsP`</summary>

```text
Web search results for query: "RC-GRPO arXiv 2602.03025 Reward-Conditioned GRPO Multi-Turn Tool Calling"

Links: [{"title":"[2602.03025] RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents","url":"https://arxiv.org/abs/2602.03025"},{"title":"RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents","url":"https://arxiv.org/html/2602.03025"},{"title":"RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for","url":"https://arxiv.org/pdf/2602.03025"},{"title":"(PDF) RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents","url":"https://www.researchgate.net/publication/400415096_RC-GRPO_Reward-Conditioned_Group_Relative_Policy_Optimization_for_Multi-Turn_Tool_Calling_Agents"},{"title":"Empowering Multi-Turn Tool-Integrated Agentic Reasoning with Group Turn Policy Optimization","url":"https://arxiv.org/html/2511.14846"},{"title":"Multi-Turn Reinforcement Learning for Tool-Calling Agents with Iterative Reward Calibration","url":"https://arxiv.org/html/2604.02869"},{"title":"Multi-Turn GRPO for Efficient Sequential RL","url":"https://www.emergentmind.com/topics/multi-turn-group-relative-policy-optimization-mtgrpo"},{"title":"Murphy: Multi-Turn GRPO for Self Correcting Code Generation","url":"https://arxiv.org/html/2511.07833v1"},{"title":"ToolRL: Reward is All Tool Learning Needs","url":"https://arxiv.org/html/2504.13958v1"},{"title":"Empowering Multi-Turn Tool-Integrated Reasoning with Group Turn Policy Optimization","url":"https://arxiv.org/html/2511.14846v1"}]

I found information about RC-GRPO arXiv paper 2602.03025. Here are the key details:

## RC-GRPO: Reward-Conditioned Group Relative Policy Optimization

RC-GRPO is a paper titled "Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents", submitted on February 3, 2026.

### Problem and Solution

Multi-turn tool calling is challenging for Large Language Models (LLMs) because rewards are sparse and exploration is expensive. A common recipe, SFT followed by GRPO, can stall when within-group reward variation is low (e.g., more rollouts in a group receive the all 0 or all 1 reward), making the group-normalized advantage uninformative and yielding vanishing updates.

### Proposed Approach

RC-GRPO treats exploration as a controllable steering problem via discrete reward tokens. The method first fine-tunes a Reward-Conditioned Trajectory Policy (RCTP) on mixed-quality trajectories with reward goal special tokens (e.g., <|high_reward|>, <|low_reward|>) injected into the prompts, enabling the model to learn how to generate distinct quality trajectories on demand. Then during RL, the method samples diverse reward tokens within each GRPO group and conditions rollouts on the sampled token to improve within-group diversity, improving advantage gains.

### Authors

The paper is authored by Haitian Zhong and 5 other co-authors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e48289e3-5adc-4602-8f5e-cc43f0be19dd",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a11d1541bbbc8a5e8",
  "type": "user",
  "uuid": "d18e4e62-8d5a-440b-b656-51eb0027a8d5",
  "sourceToolAssistantUUID": "e48289e3-5adc-4602-8f5e-cc43f0be19dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-11T23:29:23.896Z_

<details><summary>↩ Tool result · `toolu_012qDziuwjqWGtjs6Rxa21o6`</summary>

```text
Web search results for query: "Knapsack RL ICLR 2026 budget allocation reinforcement learning LLM"

Links: [{"title":"Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation | OpenReview","url":"https://openreview.net/forum?id=uqxNmKw7DI"},{"title":"Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation","url":"https://arxiv.org/html/2509.25849v1"},{"title":"[2509.25849v1] Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation","url":"https://arxiv.org/abs/2509.25849v1"},{"title":"Paper page - Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation","url":"https://huggingface.co/papers/2509.25849"},{"title":"[2509.25849] Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation","url":"https://arxiv.org/abs/2509.25849"},{"title":"Knapsack RL: Budget Allocation for LLMs","url":"https://www.emergentmind.com/papers/2509.25849"},{"title":"(PDF) Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation","url":"https://www.researchgate.net/publication/396048431_Knapsack_RL_Unlocking_Exploration_of_LLMs_via_Optimizing_Budget_Allocation"},{"title":"Published as a conference paper at ICLR 2026 TOWARD EFFICIENT EXPLORATION","url":"https://dilipa.github.io/papers/iclr26_psrl_llms.pdf"},{"title":"Scaling Behaviors of LLM Reinforcement Learning Post-Training: An Empirical Study in Mathematical Reasoning | OpenReview","url":"https://openreview.net/forum?id=KBut2YCZ4g"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"}]

Based on the search results, I found relevant information about "Knapsack RL":

## Knapsack RL: Optimizing Budget Allocation for LLM Reinforcement Learning

Large Language Models can self-improve through reinforcement learning by generating trajectories to explore and discover better solutions, but this exploration process is computationally expensive, often forcing current methods to assign limited exploration budgets to each task.

Uniform allocation creates problematic edge cases: easy tasks consistently succeed while difficult tasks consistently fail, both producing zero gradients during training updates for the widely used Group Relative Policy Optimization (GRPO).

**The Solution:**

The researchers view each task's exploration as an "item" with a distinct "value" and "cost" and establish a connection to the classical knapsack problem, which formulation allows deriving an optimal assignment rule that adaptively distributes resources based on the model's current learning status.

**Results:**

Knapsack-GRPO clearly outperforms GRPO, particularly when computational resources are limited. In the low-budget scenario, Knapsack-GRPO improves performance from 39.8 to 45.5, while achieving the same performance as standard GRPO with roughly 2x the computational resources.

The paper appears on arXiv (2509.25849) and was submitted to ICLR 2026 based on the OpenReview link found in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5271511c-c4ee-4856-bd52-e5d344f32191",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a11d1541bbbc8a5e8",
  "type": "user",
  "uuid": "eb40eef2-11c8-400c-ae93-b71c38f3ff8e",
  "sourceToolAssistantUUID": "5271511c-c4ee-4856-bd52-e5d344f32191",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-11T23:29:27.182Z_

All three papers exist. Now let me fetch the detailed content from each paper's arXiv page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb40eef2-11c8-400c-ae93-b71c38f3ff8e",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011Cawegm7UU8TmX5q2EvCWu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0aff1a1e-2ea5-4bcf-9b70-1856e9069f21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137Mzn8ov2Fdf8nE2JMZfau",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2912,
      "cache_read_input_tokens": 11002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2912,
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

_source line 14 · 2026-05-11T23:29:30.101Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016PumHpvrDaXNx1rf9qDWCd`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.03048",
  "prompt": "Extract the full abstract, list of authors, and any methodology details visible on this page for the paper CoBA-RL. I need to understand: How does the Beta distribution-based budget allocation work? What is \"capability-oriented\"? How does difficulty estimation work? What benchmarks are used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0aff1a1e-2ea5-4bcf-9b70-1856e9069f21",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011Cawegm7UU8TmX5q2EvCWu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eda74915-250e-4350-98b1-7fa109d23eb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137Mzn8ov2Fdf8nE2JMZfau",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2912,
      "cache_read_input_tokens": 11002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2912,
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

_source line 15 · 2026-05-11T23:29:31.798Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BwSqodx7wc9MxFc8d25e5z`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.03025",
  "prompt": "Extract the full abstract, list of authors, and any methodology details visible on this page for RC-GRPO. I need to understand: What is \"reward-conditioned\" trajectory generation? How does it address low reward variation in GRPO? What benchmarks are used? Is it specific to tool calling?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eda74915-250e-4350-98b1-7fa109d23eb5",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011Cawegm7UU8TmX5q2EvCWu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5bf9140f-f61a-46db-8b6d-ed4db6f6ba4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137Mzn8ov2Fdf8nE2JMZfau",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2912,
      "cache_read_input_tokens": 11002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2912,
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

_source line 16 · 2026-05-11T23:29:32.947Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Y8GejJarvx8nMTZAJN8k5r`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.25849",
  "prompt": "Extract the full abstract, list of authors, and any methodology details visible on this page for Knapsack RL. How does it formulate budget allocation as a knapsack problem? What is the optimal assignment rule? What benchmarks are used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bf9140f-f61a-46db-8b6d-ed4db6f6ba4b",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011Cawegm7UU8TmX5q2EvCWu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a694145-431b-4b88-a4d3-41a469351b19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137Mzn8ov2Fdf8nE2JMZfau",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2912,
      "cache_read_input_tokens": 11002,
      "output_tokens": 413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2912
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 413,
          "cache_read_input_tokens": 11002,
          "cache_creation_input_tokens": 2912,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2912,
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

_source line 17 · 2026-05-11T23:29:36.499Z_

<details><summary>↩ Tool result · `toolu_016PumHpvrDaXNx1rf9qDWCd`</summary>

```text
# CoBA-RL Paper Summary

## Full Abstract
"Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a key approach for enhancing LLM reasoning. However, standard frameworks like Group Relative Policy Optimization (GRPO) typically employ a uniform rollout budget, leading to resource inefficiency. Moreover, existing adaptive methods often rely on instance-level metrics, such as task pass rates, failing to capture the model's dynamic learning state. To address these limitations, we propose CoBA-RL, a reinforcement learning algorithm designed to adaptively allocate rollout budgets based on the model's evolving capability. Specifically, CoBA-RL utilizes a Capability-Oriented Value function to map tasks to their potential training gains and employs a heap-based greedy strategy to efficiently self-calibrate the distribution of computational resources to samples with high training value. Extensive experiments demonstrate that our approach effectively orchestrates the trade-off between exploration and exploitation, delivering consistent generalization improvements across multiple challenging benchmarks. These findings underscore that quantifying sample training value and optimizing budget allocation are pivotal for advancing LLM post-training efficiency."

## Authors
Zhiyuan Yao, Yi-Kai Zhang, Yuxin Chen, Yueqing Sun, Zishan Xu, Yu Yang, Tianhao Hu, Qi Gu, Hui Su, and Xunliang Cai

## Key Methodology Details Available

**What the page reveals:**
- The algorithm uses a "Capability-Oriented Value function" that maps tasks to training gains
- A "heap-based greedy strategy" performs resource self-calibration
- The approach balances exploration versus exploitation
- It focuses on quantifying "sample training value"

**Not addressed in this page:**
The provided content does not explain Beta distribution mechanics, specific difficulty estimation methods, or which benchmarks were evaluated. These details would require accessing the full PDF or HTML versions of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eda74915-250e-4350-98b1-7fa109d23eb5",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a11d1541bbbc8a5e8",
  "type": "user",
  "uuid": "f92d0a78-670e-4282-b381-626fb5ccb18e",
  "sourceToolAssistantUUID": "eda74915-250e-4350-98b1-7fa109d23eb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-11T23:29:38.004Z_

<details><summary>↩ Tool result · `toolu_01BwSqodx7wc9MxFc8d25e5z`</summary>

```text
# RC-GRPO Paper Summary

## Full Abstract
"Multi-turn tool calling is challenging for Large Language Models (LLMs) because rewards are sparse and exploration is expensive. A common recipe, SFT followed by GRPO, can stall when within-group reward variation is low (e.g., more rollouts in a group receive the all 0 or all 1 reward), making the group-normalized advantage uninformative and yielding vanishing updates. To address this problem, we propose RC-GRPO (Reward-Conditioned Group Relative Policy Optimization), which treats exploration as a controllable steering problem via discrete reward tokens. We first fine-tune a Reward-Conditioned Trajectory Policy (RCTP) on mixed-quality trajectories with reward goal special tokens (e.g., <|high_reward|>, <|low_reward|>) injected into the prompts, enabling the model to learn how to generate distinct quality trajectories on demand. Then during RL, we sample diverse reward tokens within each GRPO group and condition rollouts on the sampled token to improve within-group diversity, improving advantage gains."

## Authors
Haitian Zhong, Jixiu Zhai, Lei Song, Jiang Bian, Qiang Liu, Tieniu Tan

## Key Methodology Components

**Reward-Conditioned Generation:** The method fine-tunes a Reward-Conditioned Trajectory Policy on trajectories with embedded reward goal tokens, allowing the model to produce varied quality outputs based on conditioning signals.

**Problem Addressed:** The approach solves low within-group reward variation in GRPO by injecting diversity through sampling different reward tokens, making advantage calculations more informative.

**Benchmark:** Evaluated on the Berkeley Function Calling Leaderboard v4 (BFCLv4) multi-turn benchmark.

**Application Scope:** Specifically designed for multi-turn tool calling agents, with performance improvements noted for Qwen-2.5-7B-Instruct.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bf9140f-f61a-46db-8b6d-ed4db6f6ba4b",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a11d1541bbbc8a5e8",
  "type": "user",
  "uuid": "2bb830f0-35af-43f1-ab43-0cddc2a5886a",
  "sourceToolAssistantUUID": "5bf9140f-f61a-46db-8b6d-ed4db6f6ba4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-11T23:29:40.554Z_

<details><summary>↩ Tool result · `toolu_01Y8GejJarvx8nMTZAJN8k5r`</summary>

```text
# Knapsack RL: Key Information

## Full Abstract

"Large Language Models (LLMs) can self-improve through reinforcement learning, where they generate trajectories to explore and discover better solutions. However, this exploration process is computationally expensive, often forcing current methods to assign limited exploration budgets to each task. This uniform allocation creates problematic edge cases: easy tasks consistently succeed while difficult tasks consistently fail, both producing zero gradients during training updates for the widely used Group Relative Policy Optimization (GRPO). We address this problem from the lens of exploration budget allocation. Viewing each task's exploration as an "item" with a distinct "value" and "cost", we establish a connection to the classical knapsack problem. This formulation allows us to derive an optimal assignment rule that adaptively distributes resources based on the model's current learning status. When applied to GRPO, our method increases the effective ratio of non-zero policy gradients by 20-40% during training. Acting as a computational "free lunch", our approach could reallocate exploration budgets from tasks where learning is saturated to those where it is most impactful. This enables significantly larger budgets (e.g., 93 rollouts) for especially challenging problems, which would be computationally prohibitive under a uniform allocation. These improvements translate to meaningful gains on mathematical reasoning benchmarks, with average improvements of 2-4 points and peak gains of 9 points on specific tasks. Notably, achieving comparable performance with traditional homogeneous allocation would require about 2x the computational resources."

## Authors

Ziniu Li, Congliang Chen, Tianyun Yang, Tian Ding, Ruoyu Sun, Ge Zhang, Wenhao Huang, Zhi-Quan Luo

## Knapsack Formulation

The paper conceptualizes each task's exploration as an item possessing distinct value and cost parameters, enabling connection to the classical knapsack optimization problem for deriving adaptive resource allocation rules.

## Benchmarks

Mathematical reasoning benchmarks (specific names not detailed in visible content), showing 2-4 point average improvements with peak gains reaching 9 points on particular tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a694145-431b-4b88-a4d3-41a469351b19",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a11d1541bbbc8a5e8",
  "type": "user",
  "uuid": "56e5ff7c-e8f2-4fc9-8c44-3ee1bed3b9ae",
  "sourceToolAssistantUUID": "3a694145-431b-4b88-a4d3-41a469351b19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-11T23:29:44.249Z_

Good, I have the abstracts. Now let me fetch the full HTML versions of CoBA-RL and RC-GRPO to get the detailed methodology, especially about Beta distributions, difficulty estimation, and benchmarks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56e5ff7c-e8f2-4fc9-8c44-3ee1bed3b9ae",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawehzJkbdH7ZxPfpnvGt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9d73119-222e-43b1-8b64-65ad4dae544d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SVqqDpq3vXgtT7edZFyMe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1967,
      "cache_read_input_tokens": 13914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1967,
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

_source line 21 · 2026-05-11T23:29:47.879Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PsoMSaY1tkiWCWuxDXZ9x3`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.03048",
  "prompt": "Extract detailed methodology information about CoBA-RL. Specifically I need:\n1. How does the Beta distribution-based budget allocation work? What are the parameters?\n2. What is the \"Capability-Oriented Value function\"? How is it defined mathematically?\n3. How does difficulty estimation work for tasks?\n4. What is the heap-based greedy strategy?\n5. What benchmarks were used for evaluation? What were the main results?\n6. How does this compare to uniform budget allocation and other baselines?\n7. What base models were used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9d73119-222e-43b1-8b64-65ad4dae544d",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawehzJkbdH7ZxPfpnvGt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91234449-be4f-4b5e-b339-5bf38862e810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SVqqDpq3vXgtT7edZFyMe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1967,
      "cache_read_input_tokens": 13914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1967,
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

_source line 22 · 2026-05-11T23:29:50.765Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013qjMpLuZKZ8zT3a5CfLXT3`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.03025",
  "prompt": "Extract detailed methodology information about RC-GRPO. Specifically I need:\n1. How does reward-conditioned trajectory generation work in detail? What special tokens are used?\n2. How is the Reward-Conditioned Trajectory Policy (RCTP) trained?\n3. How are reward tokens sampled during RL training?\n4. What is the full RC-GRPO algorithm?\n5. What benchmarks were used? What were the main results and baselines?\n6. How does this compare to standard GRPO?\n7. What base models were used?\n8. Is it specific to tool calling or applicable more broadly?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91234449-be4f-4b5e-b339-5bf38862e810",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawehzJkbdH7ZxPfpnvGt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de2a289a-ee05-4269-b45a-86551b3f9365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SVqqDpq3vXgtT7edZFyMe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1967,
      "cache_read_input_tokens": 13914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1967,
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

_source line 23 · 2026-05-11T23:29:52.513Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01R2oYX3Fg2qgbsoWQVBw1Vx`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.25849v1",
  "prompt": "Extract detailed methodology for Knapsack RL:\n1. How is the knapsack problem formulated? What are the value and cost functions?\n2. What is the optimal assignment rule derived?\n3. How is the model's current learning status estimated?\n4. What specific benchmarks were used?\n5. What were the main results?\n6. Was this accepted at ICLR 2026?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de2a289a-ee05-4269-b45a-86551b3f9365",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawehzJkbdH7ZxPfpnvGt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0967fc01-1c5a-43b0-8209-80514f81321f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SVqqDpq3vXgtT7edZFyMe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1967,
      "cache_read_input_tokens": 13914,
      "output_tokens": 616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1967
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 616,
          "cache_read_input_tokens": 13914,
          "cache_creation_input_tokens": 1967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1967,
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

_source line 24 · 2026-05-11T23:30:00.145Z_

<details><summary>↩ Tool result · `toolu_01PsoMSaY1tkiWCWuxDXZ9x3`</summary>

```text
# CoBA-RL: Detailed Methodology Overview

## 1. Beta Distribution-Based Budget Allocation

The approach models task preferences using a Beta distribution with dynamically adjusted parameters. The core mechanism measures the model's "Global Failure Rate" (ℱₜ) - the complementary probability of the average success rate across the training batch. This metric quantifies evolving model capability.

The distribution is defined as: "Density(pᵢ;αₜ,βₜ) = pᵢ^(αₜ-1)(1-pᵢ)^(βₜ-1)/B(αₜ,βₜ)" where parameters shift based on capability signals rather than remaining static.

## 2. Capability-Oriented Value Function

The value function combines two components:

**Budget Saturation Factor**: "η(Bᵢ,pᵢ) = 1 - e^(-Bᵢ/τ·pᵢ(1-pᵢ))" captures diminishing returns from additional rollouts.

**Complete Function**: "V(Bᵢ,πθ,pᵢ) = (1-e^(-Bᵢ/τ·pᵢ(1-pᵢ)))·Density(pᵢ;αₜ,βₜ)"

This synthesizes budget constraints with preference density, enabling the topology to shift as policy capability evolves.

## 3. Difficulty Estimation

Rather than static task difficulty, the framework dynamically recalibrates based on current model performance. The "Global Success Rate 𝒮ₜ = (1/M)∑pᵢ" serves as the capability metric. A non-linear transformation applies sigmoid scaling when failure rates fall below 0.5, enhancing sensitivity to subtle capability fluctuations during advanced training stages.

## 4. Heap-Based Greedy Strategy

The algorithm maintains "a max-heap of marginal gains for all tasks." It iteratively: extracts the task with highest potential gain, allocates one rollout unit, recalculates the marginal gain, and reinserves. This reduces complexity to "O(Btotal·log M)" versus Dynamic Programming's "O(M·Btotal·(Bup-Blow))" - achieving ~928× speedup on tested configurations.

## 5. Evaluation Benchmarks and Results

Testing employed five mathematical reasoning datasets: AIME24, AIME25, AMC23, MATH500, and OlympiadBench across four model scales (Qwen2.5-7B variants and Qwen3 1.7B/4B).

**Key Results on Qwen2.5-7B-Instruct**:
- AIME25: 18.33% (vs GRPO 12.71%, Knapsack-RL 15.21%)
- Average across benchmarks: 46.78% (vs GRPO 42.24%, Knapsack-RL 45.39%)

Similar improvements appeared across all tested models.

## 6. Comparison to Baselines

CoBA-RL outperformed three comparison types:

- **Uniform Allocation (GRPO)**: +4.54% average improvement
- **Static Baselines**: Fixed (α,β) configurations showed 44.22%-45.21% accuracy
- **Heuristic Methods**: Linear step decay achieved 45.39%

The dynamic recalibration mechanism proved superior because "static, pre-determined strategies struggle to align with the unpredictable dynamics of real learning."

## 7. Base Models

Experiments used Qwen2.5-7B-Instruct, Qwen2.5-7B-Base, Qwen3-4B-Base, and Qwen3-1.7B-Base, trained on DAPO-Math-17K with 16-rollout group sizes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91234449-be4f-4b5e-b339-5bf38862e810",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a11d1541bbbc8a5e8",
  "type": "user",
  "uuid": "9a5c8f67-64c0-45f9-ac5c-a8f1c5b4091c",
  "sourceToolAssistantUUID": "91234449-be4f-4b5e-b339-5bf38862e810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-11T23:30:00.424Z_

<details><summary>↩ Tool result · `toolu_01R2oYX3Fg2qgbsoWQVBw1Vx`</summary>

```text
# Knapsack RL Methodology Summary

## 1. Knapsack Problem Formulation

The paper frames exploration budget allocation as a classical knapsack optimization problem where:

**Value Function:** `Value(Nᵢ, pᵢ) = ProbNonZeroGradient(Nᵢ, pᵢ) × InfoGain(pᵢ)`

- **ProbNonZeroGradient** = `1 - pᵢᴺⁱ - (1-pᵢ)ᴺⁱ` (probability of obtaining mixed success/failure outcomes)
- **InfoGain** ≈ `pᵢ(1-pᵢ)²` (approximated via Taylor expansion of one-step policy improvement)

**Cost Function:** Number of allocated rollouts (Nᵢ) per task

Constraints include total budget limit, minimum allocation (Nlow=2), and maximum allocation (Nup=128).

## 2. Optimal Assignment Rule

The optimization solves: maximize total value subject to fixed total exploration budget and allocation bounds. The paper states this "can be solved in polynomial time using standard dynamic programming techniques" with execution time of 1–2 seconds via Numba acceleration.

## 3. Learning Status Estimation

Success rates are estimated using a simple lag-based heuristic: "using the success rates observed in the previous epoch as estimates for the current one." A fallback strategy reallocates unused budget from solved tasks to unsolved tasks.

## 4. Benchmarks Used

- **In-domain:** AIME, AMC, MATH, MINERVA, OLYMPIAD
- **Out-of-domain:** GPQA (scientific reasoning)
- **Training dataset:** DAPO-MATH-17K (17,917 prompts)

## 5. Main Results

- **20-40% improvement** in effective gradient ratio across models
- **Average gains of 2-4 points** on mathematical reasoning benchmarks
- **Peak improvements:** 9.1 points on AMC (Qwen3-4B-Base), 6.8 on AMC (Qwen2.5-Math-7B)
- **Computational efficiency:** Comparable performance to uniform allocation requires approximately 2× resources

## 6. Acceptance Status

The document provides no information regarding conference acceptance or publication venue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0967fc01-1c5a-43b0-8209-80514f81321f",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a11d1541bbbc8a5e8",
  "type": "user",
  "uuid": "f9765707-db60-4791-bbc3-acbce55668a5",
  "sourceToolAssistantUUID": "0967fc01-1c5a-43b0-8209-80514f81321f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-11T23:30:01.441Z_

<details><summary>↩ Tool result · `toolu_013qjMpLuZKZ8zT3a5CfLXT3`</summary>

```text
# RC-GRPO Methodology Summary

## 1. Reward-Conditioned Trajectory Generation

RC-GRPO uses discrete reward tokens to steer generation quality. The system employs two special tokens:
- `<|high_reward|>` for optimal trajectories
- `<|low_reward|>` for failure cases

These tokens are prepended to the input history, enabling the model to generate "systematically different-quality trajectories under different tokens."

## 2. RCTP Training

The Reward-Conditioned Trajectory Policy (RCTP) is trained in Stage 1 through supervised learning on mixed-quality trajectories. The process involves:

- Constructing a dataset pairing trajectories with corresponding reward tokens based on trajectory success/failure
- Fine-tuning via maximum likelihood: minimizing negative log-likelihood of actions conditioned on history and reward token
- Creating a reference policy that learns to correlate tokens with action quality

## 3. Reward Token Sampling During RL

During RC-GRPO training, tokens are sampled from a fixed distribution for each trajectory:

"For each member j∈{1,…,G}, sample rj∼Psample(r)" where the sampling probability p matches the proportion of successful trajectories in the RCTP dataset (0.5 in their experiments).

## 4. Full RC-GRPO Algorithm

The algorithm consists of two stages:

**Stage 1**: RCTP fine-tuning on 1,600 mixed trajectories (800 expert, 800 failure)

**Stage 2**: Policy optimization using PPO-style clipped objectives with:
- Group-relative advantage normalization
- KL divergence penalty against reference policy
- Importance ratio-weighted updates
- Conditioned rollouts based on sampled reward tokens

## 5. Benchmarks and Results

**Benchmark**: Berkeley Function Calling Leaderboard v4 (BFCLv4) multi-turn subset with 200 evaluation trajectories

**Main Results** (validation accuracy):
- Qwen2.5-7B: 85.00% (vs. 48.75% SFT+GRPO baseline)
- LLaMA-3.1-8B: 48.75% (vs. 35.00% SFT+GRPO baseline)
- Best API baseline (Opus-4.5): 61.25%

## 6. Comparison to Standard GRPO

The key difference addresses "the paradox of perfection": strong SFT creates peaked policies that produce identical rollouts within GRPO groups, causing within-group reward variance collapse and vanishing gradient signals.

RC-GRPO explicitly injects variance through conditioning, maintaining "informative group-relative advantages" without requiring high policy entropy. Testing shows RC-GRPO achieves higher within-group advantage spread while maintaining lower entropy than standard GRPO approaches.

## 7. Base Models

- LLaMA-3.1-8B-Instruct
- Qwen2.5-7B-Instruct

## 8. Scope

The method targets **multi-turn tool-calling agents** specifically, addressing challenges in sequential tool use with sparse, trajectory-level rewards. However, the authors frame it as addressing "a practical pathology" in group-based policy optimization generally, suggesting broader applicability to other RL settings with similar variance-collapse issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de2a289a-ee05-4269-b45a-86551b3f9365",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a11d1541bbbc8a5e8",
  "type": "user",
  "uuid": "f697d5bc-2b8f-4412-b4dc-1f36879c9706",
  "sourceToolAssistantUUID": "de2a289a-ee05-4269-b45a-86551b3f9365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-11T23:30:04.643Z_

Now let me verify whether Knapsack RL was accepted at ICLR 2026 and search for any additional context on adaptive budget allocation methods in RL for LLMs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f697d5bc-2b8f-4412-b4dc-1f36879c9706",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawejXjtmtynna9mavgeQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "541b5c78-5450-4c79-b015-66e67c3b0c75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFZ36PSMyUbmbszVxCTTWj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 590,
      "cache_creation_input_tokens": 2369,
      "cache_read_input_tokens": 15881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2369,
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

_source line 28 · 2026-05-11T23:30:06.659Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FNVbHk1Mf53aaKKaf6egJa`</summary>

```json
{
  "url": "https://openreview.net/forum?id=uqxNmKw7DI",
  "prompt": "What is the status of this paper? Was it accepted at ICLR 2026? What venue is listed? What are the review scores?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "541b5c78-5450-4c79-b015-66e67c3b0c75",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawejXjtmtynna9mavgeQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5b613ef-9f83-4440-be4f-24c1f1ea8fe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFZ36PSMyUbmbszVxCTTWj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 590,
      "cache_creation_input_tokens": 2369,
      "cache_read_input_tokens": 15881,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2369,
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

_source line 29 · 2026-05-11T23:30:06.989Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Sux5XkdBWGF1npetMkeLuA`</summary>

```json
{
  "query": "adaptive rollout budget allocation reinforcement learning LLM reasoning 2025 2026 survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5b613ef-9f83-4440-be4f-24c1f1ea8fe0",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawejXjtmtynna9mavgeQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa7a46dd-00e4-4730-86de-478c4af0872e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFZ36PSMyUbmbszVxCTTWj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 590,
      "cache_creation_input_tokens": 2369,
      "cache_read_input_tokens": 15881,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2369
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 590,
          "output_tokens": 217,
          "cache_read_input_tokens": 15881,
          "cache_creation_input_tokens": 2369,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2369,
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

_source line 30 · 2026-05-11T23:30:09.262Z_

<details><summary>↩ Tool result · `toolu_01FNVbHk1Mf53aaKKaf6egJa`</summary>

```text
# Paper Status Summary

Based on the webpage content provided:

**Venue:** The paper was "Submitted to ICLR 2026" as indicated in the document header.

**Acceptance Status:** The content does not specify whether the paper was accepted or rejected at ICLR 2026. The page only indicates it is an OpenReview submission.

**Review Scores:** No review scores are visible in the provided webpage content. The page shows basic metadata (authors, keywords, abstract) but does not display peer review ratings or detailed reviewer feedback.

The submission date is listed as "19 Sept 2025 (modified: 11 Feb 2026)," indicating revisions were made, but the acceptance decision and formal reviews are not included in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5b613ef-9f83-4440-be4f-24c1f1ea8fe0",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a11d1541bbbc8a5e8",
  "type": "user",
  "uuid": "c9449a4f-8af1-46fc-910b-8b379286aa8a",
  "sourceToolAssistantUUID": "a5b613ef-9f83-4440-be4f-24c1f1ea8fe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-11T23:30:16.817Z_

<details><summary>↩ Tool result · `toolu_01Sux5XkdBWGF1npetMkeLuA`</summary>

```text
Web search results for query: "adaptive rollout budget allocation reinforcement learning LLM reasoning 2025 2026 survey"

Links: [{"title":"CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs","url":"https://arxiv.org/html/2602.03048"},{"title":"[2602.03048] CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs","url":"https://arxiv.org/abs/2602.03048"},{"title":"Efficient Reinforcement Learning for LLM Reasoning via ...","url":"https://www.arxiv.org/pdf/2506.02177"},{"title":"Act Only When It Pays: Efficient Reinforcement Learning for LLM Reasoning via Selective Rollouts","url":"https://infini-ai-lab.github.io/GRESO/"},{"title":"[2506.02177] Act Only When It Pays: Efficient Reinforcement Learning for LLM Reasoning via Selective Rollouts","url":"https://arxiv.org/abs/2506.02177"},{"title":"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints | OpenReview","url":"https://openreview.net/forum?id=JMDCMf7mlF"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"Act Only When It Pays: Efficient Reinforcement Learning for LLM Reasoning via Selective Rollouts | OpenReview","url":"https://openreview.net/forum?id=x5lITYXmW2"},{"title":"Act Only When It Pays: Efficient Reinforcement Learning for LLM Reasoning via Selective Rollouts","url":"https://arxiv.org/html/2506.02177v1"}]

I found several highly relevant research papers and resources on adaptive rollout budget allocation in reinforcement learning for LLM reasoning from 2025-2026. Here are the key findings:

## Key Papers and Work

**CoBA-RL (2026)**: CoBA-RL is a reinforcement learning algorithm designed to adaptively allocate rollout budgets based on the model's evolving capability, utilizing a Capability-Oriented Value function to map tasks to their potential training gains and employing a heap-based greedy strategy to efficiently self-calibrate the distribution of computational resources to samples with high training value.

**GRESO (2025)**: GRESO (GRPO with Efficient Selective Rollout) is an online, lightweight pre-rollout filtering algorithm that predicts and skips uninformative prompts using reward training dynamics. The research reveals a strong temporal consistency in prompt value: prompts that are uninformative in one epoch of training are likely to remain uninformative in near future epochs.

**Anytime Verified Agents (AVA)**: AVA is a framework that dynamically allocates compute across search, sampling, and verification within a user-specified budget, combining calibrated uncertainty estimation, value-of-information-guided search expansion, and selective verification cascades with early exits.

## Context on RLVR and GRPO

Reinforcement Learning with Verifiable Rewards (RLVR) has established itself as a cornerstone for elevating LLM reasoning in agentic, coding, and mathematical domains, with Group Relative Policy Optimization (GRPO) and its variants rising to prominence. Ideally, rollout budgets allocated to each instance should be commensurate with its training value—complex samples often harbor higher training value and demand extensive exploration, whereas simple instances require minimal resources.

## Survey Resource

A comprehensive survey titled "Training Recipes for Agentic Reinforcement Learning in LLMs" was published in 2026, covering various aspects of agentic RL training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa7a46dd-00e4-4730-86de-478c4af0872e",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a11d1541bbbc8a5e8",
  "type": "user",
  "uuid": "49dc65d2-8c23-497f-8c45-6398543eff30",
  "sourceToolAssistantUUID": "aa7a46dd-00e4-4730-86de-478c4af0872e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-11T23:30:20.785Z_

Now let me get one more piece of context -- the GRESO paper since it's closely related, and check the Knapsack RL ICLR status more specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49dc65d2-8c23-497f-8c45-6398543eff30",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawekfK5tizS7kKLDGbbP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb1f3179-afec-4646-8d5a-fd191a1dc0fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LuFJxwxCCtvvyRwDzvimaq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2050,
      "cache_read_input_tokens": 18250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2050,
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

_source line 33 · 2026-05-11T23:30:21.048Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WJDKy37RFTHSos6dBC2KCh`</summary>

```json
{
  "query": "\"Knapsack RL\" ICLR 2026 accepted paper Ziniu Li"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb1f3179-afec-4646-8d5a-fd191a1dc0fa",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawekfK5tizS7kKLDGbbP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b400d44c-38ae-4b41-9b1d-7bbbac1862e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LuFJxwxCCtvvyRwDzvimaq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2050,
      "cache_read_input_tokens": 18250,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2050
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 112,
          "cache_read_input_tokens": 18250,
          "cache_creation_input_tokens": 2050,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2050,
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

_source line 34 · 2026-05-11T23:30:28.046Z_

<details><summary>↩ Tool result · `toolu_01WJDKy37RFTHSos6dBC2KCh`</summary>

```text
Web search results for query: ""Knapsack RL" ICLR 2026 accepted paper Ziniu Li"

Links: [{"title":"dblp: Tian Ding","url":"https://dblp.org/pid/146/9704.html"},{"title":"dblp: Zhi-Quan Luo","url":"https://dblp.org/pid/34/2152.html"},{"title":"[2509.25849v1] Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation","url":"https://arxiv.org/abs/2509.25849v1"},{"title":"[2509.25849] Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation","url":"https://arxiv.org/abs/2509.25849"},{"title":"ICLR 2026","url":"https://iclr.cc/"},{"title":"Ziniu Li","url":"http://www.liziniu.org/"},{"title":"(PDF) Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation","url":"https://www.researchgate.net/publication/396048431_Knapsack_RL_Unlocking_Exploration_of_LLMs_via_Optimizing_Budget_Allocation"},{"title":"Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation","url":"https://arxiv.org/html/2509.25849v1"},{"title":"ICLR 2026 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/"},{"title":"2026 Dates and Deadlines","url":"https://iclr.cc/Conferences/2026/Dates"}]

Based on the search results, I found information about the "Knapsack RL" paper by Ziniu Li and colleagues:

The paper "Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation" is authored by Ziniu Li, Congliang Chen, Tianyun Yang, Tian Ding, Ruoyu Sun, Ge Zhang, Wenhao Huang, and Zhi-Quan Luo.

The paper addresses how Large Language Models can self-improve through reinforcement learning by generating trajectories to explore and discover better solutions. However, this exploration process is computationally expensive, often forcing current methods to assign limited exploration budgets to each task. This uniform allocation creates problematic edge cases where easy tasks consistently succeed while difficult tasks consistently fail, both producing zero gradients during training updates for the widely used Group Relative Policy Optimization (GRPO).

The authors address this problem by viewing each task's exploration as an "item" with a distinct "value" and "cost", establishing a connection to the classical knapsack problem. This formulation allows them to derive an optimal assignment rule that adaptively distributes resources based on the model's current learning status.

However, the search results show that this paper was posted on arXiv in September 2025 (arxiv ID 2509.25849), and I could not find confirmation in the search results that it has been accepted to ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b400d44c-38ae-4b41-9b1d-7bbbac1862e8",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a11d1541bbbc8a5e8",
  "type": "user",
  "uuid": "d4012792-ed38-4105-8e45-dfcc1ad59e24",
  "sourceToolAssistantUUID": "b400d44c-38ae-4b41-9b1d-7bbbac1862e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-11T23:30:31.217Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VDLC5jzkuYbRmSWyvum82U`</summary>

```json
{
  "url": "http://www.liziniu.org/",
  "prompt": "Check if there is any mention of Knapsack RL being accepted at ICLR 2026 or any other conference on Ziniu Li's personal page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4012792-ed38-4105-8e45-dfcc1ad59e24",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawemVJMcBCyUQtjtkzig",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f871664-3909-43ca-88b8-a9ac121b1989",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QYYQuyxh6xiHmq491XCaje",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 939,
      "cache_read_input_tokens": 20300,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 939
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 114,
          "cache_read_input_tokens": 20300,
          "cache_creation_input_tokens": 939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 939,
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

_source line 36 · 2026-05-11T23:30:31.568Z_

<details><summary>↩ Tool result · reported error · `toolu_01VDLC5jzkuYbRmSWyvum82U`</summary>

```text
ERR_TLS_CERT_ALTNAME_INVALID fetching "https://www.liziniu.org/". For more information, pass `verbose: true` in the second argument to fetch()
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f871664-3909-43ca-88b8-a9ac121b1989",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a11d1541bbbc8a5e8",
  "type": "user",
  "uuid": "b3ff29eb-31c0-48a8-bddf-be30c9c892a5",
  "toolUseResult": "Error: ERR_TLS_CERT_ALTNAME_INVALID fetching \"https://www.liziniu.org/\". For more information, pass `verbose: true` in the second argument to fetch()",
  "sourceToolAssistantUUID": "1f871664-3909-43ca-88b8-a9ac121b1989",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-11T23:30:35.356Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01B67bYCNdXQVMYCpJZyRVWZ`</summary>

```json
{
  "url": "https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/",
  "prompt": "Search for \"Knapsack RL\" in this ICLR 2026 accepted paper list. Is it listed? Report its status."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3ff29eb-31c0-48a8-bddf-be30c9c892a5",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawemkSBcaD1rQsqbS4bX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59e67475-b244-403d-aa11-c44ff5058fb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FSmAhSCh6sy7oFJKcbEs9h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 283,
      "cache_read_input_tokens": 21239,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 283
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 21239,
          "cache_creation_input_tokens": 283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 283,
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

_source line 38 · 2026-05-11T23:30:38.678Z_

<details><summary>↩ Tool result · `toolu_01B67bYCNdXQVMYCpJZyRVWZ`</summary>

```text
# Search Results for "Knapsack RL"

Based on the webpage content provided, I cannot determine whether a paper titled "Knapsack RL" appears in the ICLR 2026 accepted paper list.

The page shows summary statistics indicating 5,343 accepted papers out of 19,809 total submissions, but the actual paper titles and details are not displayed in the content provided. The interface indicates that "The table starts with the first `100 records`" and users must "Fetch all" to view the complete listing.

To find this specific paper, you would need to use the search functionality directly on the Paper Copilot website.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59e67475-b244-403d-aa11-c44ff5058fb0",
  "isSidechain": true,
  "promptId": "6c5c6f06-00d7-4ac6-aee0-d93b8aaacfb7",
  "agentId": "a11d1541bbbc8a5e8",
  "type": "user",
  "uuid": "55771d0a-cc0c-4ed5-989b-4633b4154121",
  "sourceToolAssistantUUID": "59e67475-b244-403d-aa11-c44ff5058fb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-11T23:31:55.780Z_

I have collected extensive information on all three papers. Here is my comprehensive report.

---

## Detailed Research Report

### 1. CoBA-RL (arXiv:2602.03048)

**Title:** CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs

**Authors:** Zhiyuan Yao, Yi-Kai Zhang, Yuxin Chen, Yueqing Sun, Zishan Xu, Yu Yang, Tianhao Hu, Qi Gu, Hui Su, Xunliang Cai

**Submitted:** February 3, 2026 (revised February 6, 2026)

**GitHub:** https://github.com/Within-yao/CoBA-RL

#### Problem
Standard GRPO uses a uniform rollout budget across all tasks, which is wasteful: easy tasks always succeed and hard tasks always fail, both producing zero gradients. Existing adaptive methods rely on instance-level metrics like pass rates, failing to capture the model's dynamic learning state.

#### How the Beta Distribution-Based Budget Allocation Works
CoBA-RL models task preferences using a Beta distribution with dynamically adjusted parameters. The density function is:

`Density(p_i; alpha_t, beta_t) = p_i^(alpha_t - 1) * (1 - p_i)^(beta_t - 1) / B(alpha_t, beta_t)`

The parameters shift based on a "Global Failure Rate" (F_t), which is the complementary probability of the average success rate across the training batch. As the model's capability evolves, the Beta distribution parameters change, re-weighting which difficulty levels of tasks are prioritized for budget allocation.

#### What "Capability-Oriented" Means
Rather than using static, pre-determined difficulty labels, CoBA-RL uses a "Capability-Oriented Value function" that dynamically maps each task to its potential training gain given the model's *current* ability level. The value function combines two components:

- **Budget Saturation Factor:** `eta(B_i, p_i) = 1 - exp(-B_i / (tau * p_i * (1-p_i)))` -- captures diminishing returns from additional rollouts. Tasks with pass rates near 0.5 (moderate difficulty relative to current capability) get the most benefit.
- **Complete Value Function:** `V(B_i, pi_theta, p_i) = eta(B_i, p_i) * Density(p_i; alpha_t, beta_t)` -- synthesizes budget constraints with the capability-weighted preference density.

The Global Success Rate `S_t = (1/M) * sum(p_i)` serves as the capability metric, with a sigmoid scaling transformation when failure rates fall below 0.5 to maintain sensitivity during later training stages.

#### Heap-Based Greedy Strategy
Instead of expensive dynamic programming (O(M * B_total * (B_up - B_low))), CoBA-RL uses a max-heap of marginal gains. It iteratively: (1) extracts the task with highest marginal gain, (2) allocates one rollout unit, (3) recalculates the marginal gain, (4) reinserts into the heap. This achieves O(B_total * log M) complexity -- approximately 928x speedup over DP in tested configurations.

#### Benchmarks and Results
- **Training data:** DAPO-Math-17K
- **Evaluation:** AIME24, AIME25, AMC23, MATH500, OlympiadBench
- **Models:** Qwen2.5-7B-Instruct, Qwen2.5-7B-Base, Qwen3-4B-Base, Qwen3-1.7B-Base (16-rollout group sizes)
- **Key results (Qwen2.5-7B-Instruct):**
  - AIME25: 18.33% (vs. GRPO 12.71%, Knapsack-RL 15.21%)
  - Average: 46.78% (vs. GRPO 42.24%, Knapsack-RL 45.39%)
  - CoBA-RL outperforms both uniform allocation (+4.54% avg) and static Beta configurations (44.22%-45.21%)

---

### 2. RC-GRPO (arXiv:2602.03025)

**Title:** RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents

**Authors:** Haitian Zhong, Jixiu Zhai, Lei Song, Jiang Bian, Qiang Liu, Tieniu Tan

**Submitted:** February 3, 2026

#### Problem
Multi-turn tool calling has sparse rewards and expensive exploration. When SFT produces a strong initial policy, GRPO stalls due to the "paradox of perfection": within a group, rollouts tend to all succeed or all fail, collapsing within-group reward variance. The group-normalized advantage becomes uninformative, yielding vanishing gradient updates.

#### What "Reward-Conditioned" Trajectory Generation Means
RC-GRPO treats exploration as a **controllable steering problem** using discrete reward tokens. Two special tokens are defined:
- `<|high_reward|>` -- steers the model toward optimal trajectories
- `<|low_reward|>` -- steers toward failure trajectories

These tokens are prepended to the input, enabling the model to generate systematically different-quality trajectories on demand based on the conditioning signal.

#### How It Addresses Low Reward Variation
The algorithm has two stages:

**Stage 1 -- RCTP Training:** A Reward-Conditioned Trajectory Policy is fine-tuned via supervised learning on 1,600 mixed-quality trajectories (800 expert/success, 800 failure). Each trajectory is paired with the appropriate reward token. The model learns to correlate reward tokens with trajectory quality through maximum likelihood training.

**Stage 2 -- RC-GRPO Training:** During RL, for each member j in a GRPO group, a reward token r_j is sampled from a distribution P_sample(r) (with p=0.5 in their experiments, matching the success/failure ratio in training data). Each rollout is conditioned on its sampled token. This explicitly injects diversity within each group -- some rollouts are steered toward success, others toward failure -- ensuring that within-group reward variance remains high and advantages are informative.

The RL objective uses PPO-style clipped updates with group-relative advantage normalization and KL divergence penalty against the reference policy.

#### Benchmarks and Results
- **Benchmark:** Berkeley Function Calling Leaderboard v4 (BFCLv4), multi-turn subset (200 evaluation trajectories)
- **Models:** Qwen2.5-7B-Instruct, LLaMA-3.1-8B-Instruct
- **Key results:**
  - Qwen2.5-7B: 85.00% (vs. 48.75% for SFT+GRPO baseline)
  - LLaMA-3.1-8B: 48.75% (vs. 35.00% SFT+GRPO baseline)
  - Outperforms even the best API baseline (Opus-4.5 at 61.25%)

#### Scope
The method is specifically designed for and evaluated on **multi-turn tool-calling agents**, but the authors note it addresses a general pathology in group-based policy optimization (within-group variance collapse), suggesting broader applicability to any RL setting with similar issues.

---

### 3. Knapsack RL (arXiv:2509.25849)

**Title:** Knapsack RL: Unlocking Exploration of LLMs via Optimizing Budget Allocation

**Authors:** Ziniu Li, Congliang Chen, Tianyun Yang, Tian Ding, Ruoyu Sun, Ge Zhang, Wenhao Huang, Zhi-Quan Luo

**Submitted:** September 2025 (revised February 2026)

**ICLR 2026 status:** Submitted to ICLR 2026 per OpenReview (https://openreview.net/forum?id=uqxNmKw7DI). I could not confirm acceptance from the sources I checked, though it was listed among ICLR 2026 submissions.

#### Knapsack Formulation
Each task's exploration is treated as an "item" with:
- **Value:** `Value(N_i, p_i) = ProbNonZeroGradient(N_i, p_i) * InfoGain(p_i)` where:
  - `ProbNonZeroGradient = 1 - p_i^N_i - (1-p_i)^N_i` (probability of getting mixed success/failure outcomes, which is needed for non-zero GRPO gradients)
  - `InfoGain ~ p_i * (1-p_i)^2` (approximated via Taylor expansion of one-step policy improvement -- tasks near the learning frontier have highest information gain)
- **Cost:** Number of rollouts N_i allocated to the task
- **Constraints:** Total budget B_total, minimum allocation N_low=2, maximum N_up=128

#### Optimal Assignment Rule
The optimization maximizes total value subject to the fixed total budget. The authors show this can be solved in polynomial time using standard dynamic programming, taking only 1-2 seconds with Numba acceleration.

#### Learning Status Estimation
Simple lag-based heuristic: success rates from the previous epoch estimate current rates. A fallback strategy reallocates unused budget from fully-solved tasks to unsolved tasks.

#### Benchmarks and Results
- **Training:** DAPO-MATH-17K (17,917 prompts)
- **In-domain evaluation:** AIME, AMC, MATH, MINERVA, OLYMPIAD
- **Out-of-domain:** GPQA (scientific reasoning)
- **Key results:**
  - 20-40% improvement in effective (non-zero) gradient ratio
  - Average gains of 2-4 points on math reasoning benchmarks
  - Peak gains: 9.1 points on AMC (Qwen3-4B-Base), 6.8 on AMC (Qwen2.5-Math-7B)
  - Achieves same performance as uniform GRPO with ~2x fewer compute resources
  - Can allocate up to 93 rollouts for challenging problems (impossible under uniform allocation)

---

### Comparison and Relationship Between Papers

| Aspect | CoBA-RL | Knapsack RL | RC-GRPO |
|--------|---------|-------------|---------|
| **Core problem** | Uniform budget is wasteful | Uniform budget causes zero gradients | Low within-group variance kills learning |
| **Solution type** | Adaptive budget allocation via Beta distribution | Adaptive budget via knapsack optimization | Diversity injection via reward conditioning |
| **Key mechanism** | Capability-oriented value + heap-based greedy | Value/cost knapsack DP | Reward token steering of rollouts |
| **What adapts** | Budget per task based on model capability | Budget per task based on gradient informativeness | Trajectory quality distribution within groups |
| **Domain** | Math reasoning | Math reasoning | Multi-turn tool calling |
| **Base models** | Qwen2.5-7B, Qwen3-1.7B/4B | Qwen2.5-Math-7B, Qwen3-4B | Qwen2.5-7B, LLaMA-3.1-8B |

CoBA-RL explicitly compares against Knapsack RL and outperforms it (46.78% vs. 45.39% average), attributing the improvement to dynamic capability-aware recalibration versus Knapsack RL's simpler lag-based estimation. Both operate on the budget allocation axis, while RC-GRPO tackles a complementary problem (within-group diversity) that persists even with optimal budget allocation.

A related concurrent work is **GRESO** (arXiv:2506.02177), "Act Only When It Pays," which uses pre-rollout filtering to skip uninformative prompts entirely based on reward training dynamics, representing another approach to efficient RL compute allocation.

Sources:
- [CoBA-RL (arXiv:2602.03048)](https://arxiv.org/abs/2602.03048)
- [CoBA-RL Full Paper HTML](https://arxiv.org/html/2602.03048)
- [CoBA-RL GitHub](https://github.com/Within-yao/CoBA-RL)
- [RC-GRPO (arXiv:2602.03025)](https://arxiv.org/abs/2602.03025)
- [RC-GRPO Full Paper HTML](https://arxiv.org/html/2602.03025)
- [Knapsack RL (arXiv:2509.25849)](https://arxiv.org/abs/2509.25849)
- [Knapsack RL Full Paper HTML](https://arxiv.org/html/2509.25849v1)
- [Knapsack RL OpenReview](https://openreview.net/forum?id=uqxNmKw7DI)
- [GRESO (arXiv:2506.02177)](https://arxiv.org/abs/2506.02177)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55771d0a-cc0c-4ed5-989b-4633b4154121",
  "isSidechain": true,
  "agentId": "a11d1541bbbc8a5e8",
  "requestId": "req_011CawenGoJrWhz85R54bMeX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1671f0c5-191b-4129-b833-39977aa50c84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3bf17e33-b377-49ce-8fe3-a3edf6b0cf0c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Ba8Z87oBYrq7Tjepox7XL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 21522,
      "output_tokens": 3229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 286
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3229,
          "cache_read_input_tokens": 21522,
          "cache_creation_input_tokens": 286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 286,
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
