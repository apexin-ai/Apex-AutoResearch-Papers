# Research conversation: Search the web to verify these two papers: 1. "SWE-RM" (arXiv:2512.21919, Dec 2025, Qwen team) - Claims: 30B MoE reward 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ac4003a695718c444.jsonl`
- **Structured JSON:** [`c6f4a69c3d1df6626c2a.json`](../../sessions/c6/c6f4a69c3d1df6626c2a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-10T19:00:49.516Z_

Search the web to verify these two papers:

1. "SWE-RM" (arXiv:2512.21919, Dec 2025, Qwen team) - Claims: 30B MoE reward model, continuous [0,1] scoring via softmax of YES/NO token log-probabilities, achieves 51.6→62.0% (Flash) and 67.0→74.6% (Max) on SWE-bench Verified via best-of-N.

2. "SWE-Shepherd" (arXiv:2604.10493, April 2026) - Claims: step-level action-utility PRMs for SWE agents, achieves only 51% vs. 57% greedy baseline on 100 SWE-bench Verified tasks.

For each: Does the paper exist? Are the claimed results accurate? Are there any nuances the proposal might be misrepresenting?

Use WebSearch and WebFetch. Report findings concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4dea06eb-7a3f-4673-8060-163fe9054d36",
  "agentId": "ac4003a695718c444",
  "type": "user",
  "uuid": "045a460d-7ff9-453e-a445-d0e4439377d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:00:49.545Z_

```json
{
  "parentUuid": "045a460d-7ff9-453e-a445-d0e4439377d3",
  "isSidechain": true,
  "agentId": "ac4003a695718c444",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "fbbf0323-1344-4849-8d36-6074adf23e3f",
  "timestamp": "2026-05-10T19:00:49.545Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:00:52.974Z_



I'll search for both papers. Let me first load the WebSearch and WebFetch tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbbf0323-1344-4849-8d36-6074adf23e3f",
  "isSidechain": true,
  "agentId": "ac4003a695718c444",
  "requestId": "req_011CauQPzpcppqreZUsiQ9Ev",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd353ed0-f320-4aab-a56f-0d2a3c2ac5d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2NxkD8zuPTM115znJJ8SB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 750,
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

_source line 4 · 2026-05-10T19:00:53.018Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AxkZqifSQzSWEwgASR9RMX`</summary>

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
  "parentUuid": "dd353ed0-f320-4aab-a56f-0d2a3c2ac5d0",
  "isSidechain": true,
  "agentId": "ac4003a695718c444",
  "requestId": "req_011CauQPzpcppqreZUsiQ9Ev",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b325c6e3-c349-4e24-a162-8c7c199d9272",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2NxkD8zuPTM115znJJ8SB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 7304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 750,
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

_source line 5 · 2026-05-10T19:00:53.022Z_

<details><summary>↩ Tool result · `toolu_01AxkZqifSQzSWEwgASR9RMX`</summary>

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
  "parentUuid": "b325c6e3-c349-4e24-a162-8c7c199d9272",
  "isSidechain": true,
  "promptId": "4dea06eb-7a3f-4673-8060-163fe9054d36",
  "agentId": "ac4003a695718c444",
  "type": "user",
  "uuid": "8017a11b-0635-44eb-afbb-fd04c96ff34d",
  "sourceToolAssistantUUID": "b325c6e3-c349-4e24-a162-8c7c199d9272",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:00:55.962Z_



Now let me search for both papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8017a11b-0635-44eb-afbb-fd04c96ff34d",
  "isSidechain": true,
  "agentId": "ac4003a695718c444",
  "requestId": "req_011CauQQFPy1bDJV9xNEzZv4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "553e1aac-34d2-4e8e-ae72-93f51abe2260",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016mzuFsadVBjPboRVN8rdew",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 7 · 2026-05-10T19:00:56.914Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014qsA1qAT1mA47ZX8YpJ6Bw`</summary>

```json
{
  "query": "SWE-RM arXiv 2512.21919 reward model SWE-bench"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "553e1aac-34d2-4e8e-ae72-93f51abe2260",
  "isSidechain": true,
  "agentId": "ac4003a695718c444",
  "requestId": "req_011CauQQFPy1bDJV9xNEzZv4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "800a04ef-93fa-4efe-bceb-cb45066e62b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016mzuFsadVBjPboRVN8rdew",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 8 · 2026-05-10T19:00:57.470Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BP5DGyctbezSMxS5HUZHbj`</summary>

```json
{
  "query": "SWE-Shepherd arXiv 2604.10493 step-level PRM SWE agents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "800a04ef-93fa-4efe-bceb-cb45066e62b5",
  "isSidechain": true,
  "agentId": "ac4003a695718c444",
  "requestId": "req_011CauQQFPy1bDJV9xNEzZv4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a770554-96e1-40db-8aa6-a1f833e67202",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016mzuFsadVBjPboRVN8rdew",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 8054,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1910
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 145,
          "cache_read_input_tokens": 8054,
          "cache_creation_input_tokens": 1910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1910,
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

_source line 9 · 2026-05-10T19:01:03.559Z_

<details><summary>↩ Tool result · `toolu_014qsA1qAT1mA47ZX8YpJ6Bw`</summary>

```text
Web search results for query: "SWE-RM arXiv 2512.21919 reward model SWE-bench"

Links: [{"title":"[2512.21919] SWE-RM: Execution-free Feedback For Software Engineering Agents","url":"https://arxiv.org/abs/2512.21919"},{"title":"SWE-RM: Execution-Free Feedback for Software Engineering Agents","url":"https://arxiv.org/html/2512.21919"},{"title":"2025-12-29 SWE-RM: EXECUTION-FREE FEEDBACK FOR SOFT- WARE ENGINEERING AGENTS","url":"https://www.arxiv.org/pdf/2512.21919"},{"title":"SWE-RM: Execution-free Feedback For Software Engineering Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.21919v1"},{"title":"SWE-RM: Execution-free Feedback for Software Engineering Agents | OpenReview","url":"https://openreview.net/forum?id=H9wMe1G76j"},{"title":"Natural Language Processing Papers on X: \"SWE-RM: Execution-free Feedback For Software Engineering Agents KaShun Shum, Binyuan Hui, Jiawei Chen, Lei Zhang, X. W., Jiaxi Yang, Yuzhen Huang, Junyang Lin, Junxian He (arXiv:2512.21919) https://t.co/6Ek3le9WwT\" / X","url":"https://x.com/HEI/status/2005573373896597610"},{"title":"[2310.06770] SWE-bench: Can Language Models Resolve Real-World GitHub Issues?","url":"https://arxiv.org/abs/2310.06770"},{"title":"SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories","url":"https://arxiv.org/html/2512.17419v1"},{"title":"[2512.17419] SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories","url":"https://arxiv.org/abs/2512.17419"},{"title":"GitHub - allenai/reward-bench: RewardBench: the first evaluation tool for reward models. · GitHub","url":"https://github.com/allenai/reward-bench"}]

Based on the search results, here's what I found about SWE-RM (arXiv 2512.21919):

## Overview

SWE-RM is a paper titled "Execution-free Feedback For Software Engineering Agents". The work introduces execution-free feedback from reward models that can provide more fine-grained signals without depending on unit test cases, as an alternative to traditional execution-based feedback.

## Key Technical Details

SWE-RM is an accurate and robust reward model adopting a mixture-of-experts architecture with 30B total parameters and 3B activated during inference.

The researchers identified classification accuracy and calibration as crucial for RL training, and conducted comprehensive controlled experiments to investigate how to train a robust reward model, analyzing the impact of factors such as training data scale, policy mixtures, and data source composition.

## Performance Results

The model achieves impressive results on SWE-Bench Verified:

- It increases the accuracy of Qwen3-Coder-Flash from 51.6% to 62.0%, and Qwen3-Coder-Max from 67.0% to 74.6% using test-time scaling (TTS)
- On RL training, SWE-RM lifts the resolve rate of execution-based counterparts by 3 absolute points on SWE-Bench Verified

The paper was published on December 26, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "800a04ef-93fa-4efe-bceb-cb45066e62b5",
  "isSidechain": true,
  "promptId": "4dea06eb-7a3f-4673-8060-163fe9054d36",
  "agentId": "ac4003a695718c444",
  "type": "user",
  "uuid": "979517ec-3ab7-413c-92f0-c028f0c49c79",
  "sourceToolAssistantUUID": "800a04ef-93fa-4efe-bceb-cb45066e62b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T19:01:06.531Z_

<details><summary>↩ Tool result · `toolu_01BP5DGyctbezSMxS5HUZHbj`</summary>

```text
Web search results for query: "SWE-Shepherd arXiv 2604.10493 step-level PRM SWE agents"

Links: [{"title":"[2604.10493] SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents","url":"https://arxiv.org/abs/2604.10493"},{"title":"SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents","url":"https://arxiv.org/html/2604.10493"},{"title":"SWE-TRACE: Optimizing Long-Horizon SWE Agents through Rubric Process Reward Models and Heuristic Test-Time Scaling","url":"https://arxiv.org/html/2604.14820v1"},{"title":"Act Like You’re Paying for This: Course-Correcting Code Agents with PRMs","url":"https://arxiv.org/html/2509.02360v1"},{"title":"When Agents go Astray: Course-Correcting SWE Agents with PRMs","url":"https://arxiv.org/html/2509.02360"},{"title":"Web-Shepherd: Advancing PRMs for Reinforcing Web Agents","url":"https://arxiv.org/html/2505.15277"},{"title":"[2604.14820] SWE-TRACE: Optimizing Long-Horizon SWE Agents Through Rubric Process Reward Models and Heuristic Test-Time Scaling","url":"https://arxiv.org/abs/2604.14820"},{"title":"[2505.15277] Web-Shepherd: Advancing PRMs for Reinforcing Web Agents","url":"https://arxiv.org/abs/2505.15277"},{"title":"MATH-SHEPHERD: VERIFY AND REINFORCE LLMS STEP-BY-STEP WITHOUT HUMAN ANNOTATIONS","url":"https://arxiv.org/pdf/2312.08935"},{"title":"[2509.02360] When Agents go Astray: Course-Correcting SWE Agents with PRMs","url":"https://arxiv.org/abs/2509.02360"}]

I found the paper you're looking for! Here's information about SWE-Shepherd (arXiv 2604.10493):

## SWE-Shepherd Overview

SWE-Shepherd is a framework that introduces Process Reward Models (PRMs) to provide dense, step-level supervision for repository-level code agents.

## Key Problem and Solution

Automating real-world software engineering tasks remains challenging for LLM-based agents due to the need for long-horizon reasoning over large, evolving codebases and making consistent decisions across interdependent actions. Existing approaches typically rely on static prompting strategies or handcrafted heuristics to select actions such as code editing, file navigation, and test execution, but they lack fine-grained feedback on intermediate decisions, leading to inefficient exploration, error propagation, and brittle solution trajectories.

## Technical Approach

Instead of relying solely on sparse signals of final task success, SWE-Shepherd converts agent trajectories into dense, step-level supervision by assigning scalar rewards to intermediate actions according to their estimated contribution toward resolving the issue.

Using trajectories from SWE-Bench, the framework constructs an action-level reward dataset and trains a lightweight reward model on a base LLM to estimate the usefulness of intermediate actions. During inference, the PRM evaluates candidate actions and guides the agent toward higher-reward decisions without requiring full reinforcement learning.

## Results

Experiments on SWE-Bench Verified demonstrate improved interaction efficiency and action quality, while also highlighting challenges in aligning intermediate rewards with final task success.

The paper was submitted to arXiv on April 12, 2026 by authors Mahir Labib Dihan and Md Ashrafur Rahman Khan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a770554-96e1-40db-8aa6-a1f833e67202",
  "isSidechain": true,
  "promptId": "4dea06eb-7a3f-4673-8060-163fe9054d36",
  "agentId": "ac4003a695718c444",
  "type": "user",
  "uuid": "28349e58-4865-46b8-8038-ad49153bc5ac",
  "sourceToolAssistantUUID": "7a770554-96e1-40db-8aa6-a1f833e67202",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T19:01:10.199Z_

Both papers exist. Let me now fetch the actual paper pages to verify the specific claims in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28349e58-4865-46b8-8038-ad49153bc5ac",
  "isSidechain": true,
  "agentId": "ac4003a695718c444",
  "requestId": "req_011CauQREr1QeyBK2TB3BvUA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e39d3045-3ef0-4963-8e40-689975830968",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6CAfvrkKNHHiKsaCqCHCJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2075,
      "cache_read_input_tokens": 9964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2075,
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

_source line 12 · 2026-05-10T19:01:14.216Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LnD9FHZK2RP32EaRcXktWX`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.21919",
  "prompt": "Extract all specific numerical results on SWE-bench Verified. What are the exact accuracy numbers for Qwen3-Coder-Flash and Qwen3-Coder-Max with and without the reward model? What is the model architecture (MoE size, activated params)? How does scoring work (softmax of YES/NO tokens, continuous [0,1])? Is the team from Qwen/Alibaba? What is the exact publication date?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e39d3045-3ef0-4963-8e40-689975830968",
  "isSidechain": true,
  "agentId": "ac4003a695718c444",
  "requestId": "req_011CauQREr1QeyBK2TB3BvUA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ab0bc8d8-42b0-4357-98a5-b4676395ebe2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6CAfvrkKNHHiKsaCqCHCJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2075,
      "cache_read_input_tokens": 9964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2075,
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

_source line 13 · 2026-05-10T19:01:16.676Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012yvicqAnN6EmWT3wUE5HFM`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.10493",
  "prompt": "Extract all specific numerical results on SWE-bench Verified. What is the exact resolve rate? Does the paper report 51% for PRM-guided vs 57% greedy baseline? What kind of reward model is used (step-level, action-utility)? How many tasks from SWE-bench Verified were evaluated? Who are the authors and their affiliations? What is the exact publication date?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab0bc8d8-42b0-4357-98a5-b4676395ebe2",
  "isSidechain": true,
  "agentId": "ac4003a695718c444",
  "requestId": "req_011CauQREr1QeyBK2TB3BvUA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f054d150-d351-474e-b7b4-4658b84b72ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6CAfvrkKNHHiKsaCqCHCJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2075,
      "cache_read_input_tokens": 9964,
      "output_tokens": 359,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2075
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 359,
          "cache_read_input_tokens": 9964,
          "cache_creation_input_tokens": 2075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2075,
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

_source line 14 · 2026-05-10T19:01:17.960Z_

<details><summary>↩ Tool result · `toolu_01LnD9FHZK2RP32EaRcXktWX`</summary>

```text
# SWE-RM Paper: Key Findings

**SWE-Bench Verified Results:**
- Qwen3-Coder-Flash: improved from 51.6% to 62.0%
- Qwen3-Coder-Max: improved from 67.0% to 74.6%

**Model Architecture:**
The paper describes a "mixture-of-experts architecture with 30B total parameters and 3B activated during inference."

**Scoring Mechanism:**
The document does not specify how the reward model generates scores (softmax of tokens vs. continuous values).

**Team Origin:**
While the authors include individuals associated with Qwen/Alibaba through their names and affiliations, the paper text provided does not explicitly state institutional affiliation.

**Publication Date:**
Submitted December 26, 2025 (arXiv:2512.21919v1).

**Note:** The abstract emphasizes that execution-free feedback "can provide more fine-grained signals" compared to unit testing, and identifies calibration and classification accuracy as crucial factors for reinforcement learning performance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab0bc8d8-42b0-4357-98a5-b4676395ebe2",
  "isSidechain": true,
  "promptId": "4dea06eb-7a3f-4673-8060-163fe9054d36",
  "agentId": "ac4003a695718c444",
  "type": "user",
  "uuid": "5e464a13-2229-4d0e-b52c-ade7be7f9a03",
  "sourceToolAssistantUUID": "ab0bc8d8-42b0-4357-98a5-b4676395ebe2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T19:01:20.690Z_

<details><summary>↩ Tool result · `toolu_012yvicqAnN6EmWT3wUE5HFM`</summary>

```text
# SWE-Shepherd Paper Details

Based on the provided web page content, I can only offer limited information:

**Authors & Affiliation:**
The paper lists Mahir Labib Dihan and Md Ashrafur Rahman Khan as authors. However, their institutional affiliations are not disclosed in this excerpt.

**Publication Date:**
Submitted on April 12, 2026 (arXiv:2604.10493v1)

**Specific Numerical Results:**
The abstract does not contain specific resolve rates, percentages, or task counts. It states the work "demonstrate[s] improved interaction efficiency and action quality" on SWE-Bench Verified but provides no quantitative figures like the 51% vs 57% comparison you referenced.

**Reward Model Type:**
The abstract describes it as a "Process Reward Model (PRM)" that provides "dense, step-level supervision" and "estimate[s] the usefulness of intermediate actions," though the specific classification (step-level vs. action-utility) isn't explicitly stated.

**Limitations:**
This webpage excerpt contains only the abstract and metadata. The full numerical results, detailed methodology, and complete benchmarking data would be found in the complete PDF or HTML versions of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f054d150-d351-474e-b7b4-4658b84b72ec",
  "isSidechain": true,
  "promptId": "4dea06eb-7a3f-4673-8060-163fe9054d36",
  "agentId": "ac4003a695718c444",
  "type": "user",
  "uuid": "9298de50-868a-4fd1-adfd-2bc44f963a19",
  "sourceToolAssistantUUID": "f054d150-d351-474e-b7b4-4658b84b72ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T19:01:23.177Z_

Let me get more details from the full HTML versions of both papers to verify the specific claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9298de50-868a-4fd1-adfd-2bc44f963a19",
  "isSidechain": true,
  "agentId": "ac4003a695718c444",
  "requestId": "req_011CauQSHM6qw11U77YAXqw6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48e78e29-adca-419f-a12e-931355b9f1e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRa1z1s3AvqJqL24jJ4L7J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 945,
      "cache_read_input_tokens": 12039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 945,
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

_source line 17 · 2026-05-10T19:01:26.473Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019uPtxc5nTK88ssc3uUPtA9`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.21919",
  "prompt": "Find the scoring mechanism: does SWE-RM use softmax of YES/NO token log-probabilities to produce a continuous [0,1] score? How exactly is the reward computed? Also confirm the authors and their affiliations (Qwen team? Alibaba?). Look for any table with SWE-bench Verified results showing 51.6, 62.0, 67.0, 74.6 numbers. What is the best-of-N setup?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48e78e29-adca-419f-a12e-931355b9f1e9",
  "isSidechain": true,
  "agentId": "ac4003a695718c444",
  "requestId": "req_011CauQSHM6qw11U77YAXqw6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "100256d6-0d85-4fd1-8933-53944431b467",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRa1z1s3AvqJqL24jJ4L7J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 945,
      "cache_read_input_tokens": 12039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 945,
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

_source line 18 · 2026-05-10T19:01:28.982Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SqPTyqq3yQvD5qBtA3X2w1`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.10493",
  "prompt": "Find all specific numerical results on SWE-bench Verified. Does the paper report a resolve rate of 51% for PRM-guided approach? Is there a 57% greedy baseline mentioned? How many tasks from SWE-bench Verified were used (100? 500? all?)? What exactly does the paper call its reward model - step-level, action-utility, or process reward model? Are there any tables with resolve rates? What are the key limitations mentioned?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "100256d6-0d85-4fd1-8933-53944431b467",
  "isSidechain": true,
  "agentId": "ac4003a695718c444",
  "requestId": "req_011CauQSHM6qw11U77YAXqw6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0cc8100b-3fc4-4e1f-9ca2-2a35be38d945",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRa1z1s3AvqJqL24jJ4L7J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 945,
      "cache_read_input_tokens": 12039,
      "output_tokens": 377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 945
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 377,
          "cache_read_input_tokens": 12039,
          "cache_creation_input_tokens": 945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 945,
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

_source line 19 · 2026-05-10T19:01:32.280Z_

<details><summary>↩ Tool result · `toolu_019uPtxc5nTK88ssc3uUPtA9`</summary>

```text
# SWE-RM: Key Technical Details

## Scoring Mechanism

Yes, SWE-RM uses softmax of YES/NO token log-probabilities. As stated: "by obtaining the log probability of the special token YES(lyl_{y}) and NO(lnl_{n}), the final score rr is calculated by exp​(ly)/(exp​(ly)+exp​(ln))" which produces a continuous score in [0,1].

## Reward Computation in RL

The reward function uses three tiers based on trajectory outcomes:
- **Resolved issues**: 1 + ScoreEF
- **Unfinished trajectories**: -0.5 + ScoreEF  
- **Other cases**: 0 + ScoreEF

This hybrid approach combines execution-free feedback with outcome information.

## Authorship & Affiliation

The paper includes researchers from **The Hong Kong University of Science and Technology** and the **Qwen Team at Alibaba Group**. Key authors: Kashun Shum, Binyuan Hui, Jiawei Chen, Lei Zhang, and others.

## SWE-Bench Verified Results

Table 4 confirms the reported improvements:
- **Qwen3-Coder-Flash**: 51.2% → 62.0% (RM@32)
- **Qwen3-Coder-Max**: 65.4% → 74.6% (RM@32)

## Best-of-N Setup

Evaluation uses **32 independent runs per instance** on 500 SWE-Bench Verified tasks, generating 16,000 total trajectories for performance assessment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "100256d6-0d85-4fd1-8933-53944431b467",
  "isSidechain": true,
  "promptId": "4dea06eb-7a3f-4673-8060-163fe9054d36",
  "agentId": "ac4003a695718c444",
  "type": "user",
  "uuid": "ea5fddcd-4f60-42a0-ae7e-75f5a1931219",
  "sourceToolAssistantUUID": "100256d6-0d85-4fd1-8933-53944431b467",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T19:01:33.417Z_

<details><summary>↩ Tool result · `toolu_01SqPTyqq3yQvD5qBtA3X2w1`</summary>

```text
# SWE-Shepherd Results Summary

## Resolution Rates
Yes, the paper reports these specific results on SWE-Bench Verified:
- **SWE-Shepherd (PRM-guided)**: 51% resolved
- **mini-SWE-Agent (greedy baseline)**: 57% resolved
- **SWE-Search**: 31% resolved

## Evaluation Dataset Size
The evaluation used **100 tasks sampled from SWE-Bench Verified** (out of the full 500-task verified subset).

## Model Terminology
The paper consistently uses **"Process Reward Model"** (PRM) as the official term, though it describes the system as predicting "the reward of candidate actions."

## Key Results Table
Table 1 presents the core findings, showing that while SWE-Shepherd reduced interaction steps from 15.2 to 12.2, it achieved lower resolution rates than the greedy baseline.

## Critical Limitations
The paper identifies a fundamental challenge: "intermediate behavioral signals are easier to model than repository-level correctness." The reward analysis revealed minimal correlation between intermediate rewards and task success—resolved tasks averaged 0.4894 reward while unresolved tasks averaged 0.4818, suggesting heuristic rewards poorly predict final outcomes. This misalignment caused the PRM to potentially guide agents toward locally consistent but incomplete solutions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cc8100b-3fc4-4e1f-9ca2-2a35be38d945",
  "isSidechain": true,
  "promptId": "4dea06eb-7a3f-4673-8060-163fe9054d36",
  "agentId": "ac4003a695718c444",
  "type": "user",
  "uuid": "ad00f457-1cdc-4cbe-9477-f305d835e409",
  "sourceToolAssistantUUID": "0cc8100b-3fc4-4e1f-9ca2-2a35be38d945",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T19:01:37.503Z_

Now I have detailed information on both papers. Let me do one more check on the SWE-RM baseline numbers, since the proposal claims "51.6" but the paper may say "51.2" for Flash.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad00f457-1cdc-4cbe-9477-f305d835e409",
  "isSidechain": true,
  "agentId": "ac4003a695718c444",
  "requestId": "req_011CauQTDiqz3a84wn4DkCUt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8018732b-5e14-4f5d-b1db-ce95a40b59e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017o9eRCJ1vaVhpCZpbDm2ND",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 12984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1132,
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

_source line 22 · 2026-05-10T19:01:40.446Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SyrGViVg28KfL1U6bnU5PJ`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.21919",
  "prompt": "Look at Table 4 very carefully. What is the EXACT baseline (pass@1 or greedy) number for Qwen3-Coder-Flash? Is it 51.2% or 51.6%? What about the baseline for Qwen3-Coder-Max - is it 65.4% or 67.0%? Are there multiple baseline numbers reported (e.g., pass@1 vs maj@32 vs some other metric)? List all rows and columns of Table 4 precisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8018732b-5e14-4f5d-b1db-ce95a40b59e4",
  "isSidechain": true,
  "agentId": "ac4003a695718c444",
  "requestId": "req_011CauQTDiqz3a84wn4DkCUt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c4bc7ee-eda1-4804-bdc4-f32d160d3f02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017o9eRCJ1vaVhpCZpbDm2ND",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 12984,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1132
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 12984,
          "cache_creation_input_tokens": 1132,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1132,
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

_source line 23 · 2026-05-10T19:01:46.245Z_

<details><summary>↩ Tool result · `toolu_01SyrGViVg28KfL1U6bnU5PJ`</summary>

```text
# Analysis of Table 4

Table 4 presents performance comparisons across three models with the following structure:

**Table 4 Columns:**
- Verifier (name)
- Type (EB or EF designation)
- Three metric sections for each model: AUC, ECE↓, RM@32

**Baseline Numbers for Qwen3-Coder-Flash:**
The SWE-Gym baseline shows "51.2%" in the RM@32 column, not 51.6%. The 51.6% figure appears in the abstract's TTS context but represents a different measurement (pass@1 without verifier selection).

**Baseline Numbers for Qwen3-Coder-Max:**
The SWE-Gym baseline displays "65.4%" in the RM@32 column, not 67.0%. Again, 67.0% refers to the baseline pass@1 mentioned in the abstract.

**Key Distinction:**
"RM@K defines the resolve rate of final selected trajectories from k samples," which differs from raw pass@1 performance. Table 4 exclusively reports RM@32 (verifier-selected outcomes from 32 samples), not unaided pass@1 baselines.

The table includes five verifier rows (Agentless, SWE-Gym, DeepSWE EB, DeepSWE EF, SWE-RM) with metrics across three policy models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c4bc7ee-eda1-4804-bdc4-f32d160d3f02",
  "isSidechain": true,
  "promptId": "4dea06eb-7a3f-4673-8060-163fe9054d36",
  "agentId": "ac4003a695718c444",
  "type": "user",
  "uuid": "a06478a4-019d-443d-9799-c1e8c81407fa",
  "sourceToolAssistantUUID": "6c4bc7ee-eda1-4804-bdc4-f32d160d3f02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-10T19:01:51.418Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KGae39Y6fj592yXR7pqsq3`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.21919",
  "prompt": "Find the exact pass@1 baseline numbers mentioned in the abstract or introduction for Qwen3-Coder-Flash and Qwen3-Coder-Max on SWE-bench Verified. Is pass@1 for Flash 51.6%? Is pass@1 for Max 67.0%? What exactly does the abstract say about these numbers? Also look for Table 1 or any other table that reports pass@1 baselines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a06478a4-019d-443d-9799-c1e8c81407fa",
  "isSidechain": true,
  "agentId": "ac4003a695718c444",
  "requestId": "req_011CauQUAeq5NMUv7i8pXR3n",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9235604e-c49a-41f9-94aa-754c5796606e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vr6TTdHAQk8apwBhmS5PhU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 596,
      "cache_read_input_tokens": 14116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 596,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T19:01:56.107Z_

<details><summary>↩ Tool result · `toolu_01KGae39Y6fj592yXR7pqsq3`</summary>

```text
# Pass@1 Baseline Numbers for Qwen3-Coder Models

Based on the document content, the abstract explicitly states these baseline figures:

**Qwen3-Coder-Flash:** The abstract confirms "it increases the accuracy of Qwen3-Coder-Flash from 51.6% to 62.0%," validating your first number.

**Qwen3-Coder-Max:** The abstract confirms "Qwen3-Coder-Max from 67.0% to 74.6%," validating your second number.

These represent the pass@1 baseline performance on SWE-bench Verified *before* applying SWE-RM, with the improved numbers reflecting performance after integration with the reward model using test-time scaling (best-of-32).

However, I should note that the tables presented focus on RM@32 (resolve rate from 32 samples) rather than pure pass@1 metrics. The specific pass@1 baselines you mentioned appear only in the abstract as comparison points for demonstrating SWE-RM's improvements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9235604e-c49a-41f9-94aa-754c5796606e",
  "isSidechain": true,
  "promptId": "4dea06eb-7a3f-4673-8060-163fe9054d36",
  "agentId": "ac4003a695718c444",
  "type": "user",
  "uuid": "7e38c20d-320b-4256-b5fc-0e014d3b15ab",
  "sourceToolAssistantUUID": "9235604e-c49a-41f9-94aa-754c5796606e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-10T19:02:29.541Z_

I now have all the details needed. Here are my findings:

---

## Paper 1: SWE-RM (arXiv:2512.21919)

**Does it exist?** Yes. Published December 26, 2025, titled "SWE-RM: Execution-free Feedback For Software Engineering Agents."

**Authors:** KaShun Shum, Binyuan Hui, Jiawei Chen, Lei Zhang, and others from **The Hong Kong University of Science and Technology** and the **Qwen Team at Alibaba Group**. Calling it "the Qwen team" is fair, though it is a joint effort with HKUST.

**Are the claimed results accurate?**
- **30B MoE reward model:** Confirmed. 30B total parameters, 3B activated during inference.
- **Continuous [0,1] scoring via softmax of YES/NO token log-probabilities:** Confirmed. The paper states the score is `exp(l_y) / (exp(l_y) + exp(l_n))`.
- **51.6% to 62.0% (Flash) and 67.0% to 74.6% (Max):** These numbers match the abstract. However, there is a nuance worth noting.

**Nuances / potential misrepresentation:**
- The "51.6%" and "67.0%" are **pass@1** baselines (single greedy attempt). The "62.0%" and "74.6%" are **RM@32** results -- the best trajectory selected by the reward model out of **32 independent runs**. This is a best-of-N setup with N=32, which is a very significant computational multiplier (~32x inference cost). The proposal should make clear this is not a like-for-like comparison but rather a test-time scaling (TTS) result.
- In Table 4, when comparing against other verifiers on the same RM@32 metric, the baselines are 51.2% (Flash) and 65.4% (Max) for the SWE-Gym verifier, meaning the improvement over a comparable execution-based verifier is more modest than the abstract's pass@1-to-RM@32 framing suggests.
- The paper also reports a 3-point lift for RL training, which is a separate (and more practical) use case than best-of-32 reranking.

---

## Paper 2: SWE-Shepherd (arXiv:2604.10493)

**Does it exist?** Yes. Published April 12, 2026, titled "SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents."

**Authors:** Mahir Labib Dihan and Md Ashrafur Rahman Khan (affiliations not prominently listed on the abstract page).

**Are the claimed results accurate?**
- **Step-level PRMs for SWE agents:** Confirmed. The paper trains a Process Reward Model (PRM) that provides dense, step-level supervision by assigning scalar rewards to intermediate actions.
- **51% vs. 57% greedy baseline on 100 SWE-bench Verified tasks:** Confirmed. Table 1 shows SWE-Shepherd achieves 51% resolve rate vs. 57% for the mini-SWE-Agent greedy baseline, evaluated on 100 sampled tasks.

**Nuances / potential misrepresentation:**
- Calling the model an "action-utility PRM" is a reasonable characterization but not the paper's own terminology. The paper uses "Process Reward Model" (PRM) throughout. It predicts "the reward of candidate actions," but "action-utility" appears to be an interpretation rather than a direct quote.
- The paper is quite transparent about its negative result: intermediate rewards had almost zero correlation with task success (resolved tasks averaged 0.4894 reward vs. 0.4818 for unresolved). The PRM guided agents toward "locally consistent but incomplete solutions."
- The evaluation was on only **100 tasks** (not the full 500 SWE-bench Verified), which is a relatively small sample size.
- Despite lower resolve rates, the PRM did reduce average interaction steps from 15.2 to 12.2, showing some efficiency benefit.
- The paper frames this honestly as exposing a fundamental challenge: "intermediate behavioral signals are easier to model than repository-level correctness."

---

## Summary

Both papers exist and the headline numbers cited in the proposal are accurate. The key nuances a proposal should not gloss over:

1. **SWE-RM's gains come from best-of-32 reranking** (massive compute overhead), not from improving a single-attempt agent. The pass@1-to-RM@32 comparison inflates the apparent improvement.
2. **SWE-Shepherd is essentially a negative result** -- the authors themselves highlight that step-level PRMs underperform greedy baselines for SWE tasks due to poor alignment between intermediate rewards and final task success. This is evaluated on a small 100-task subset.

Sources:
- [SWE-RM (arXiv:2512.21919)](https://arxiv.org/abs/2512.21919)
- [SWE-RM HTML version](https://arxiv.org/html/2512.21919)
- [SWE-Shepherd (arXiv:2604.10493)](https://arxiv.org/abs/2604.10493)
- [SWE-Shepherd HTML version](https://arxiv.org/html/2604.10493)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e38c20d-320b-4256-b5fc-0e014d3b15ab",
  "isSidechain": true,
  "agentId": "ac4003a695718c444",
  "requestId": "req_011CauQUtm8k51feV9QYZuCt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb3b53ac-56d7-4714-b955-c2635f50c830",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "816276e9-6d97-42fc-bfa9-44708ee2c1fa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MuBEf5QBdxB4jJbE1go1Sr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 441,
      "cache_read_input_tokens": 14712,
      "output_tokens": 1302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 441
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1302,
          "cache_read_input_tokens": 14712,
          "cache_creation_input_tokens": 441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 441,
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
