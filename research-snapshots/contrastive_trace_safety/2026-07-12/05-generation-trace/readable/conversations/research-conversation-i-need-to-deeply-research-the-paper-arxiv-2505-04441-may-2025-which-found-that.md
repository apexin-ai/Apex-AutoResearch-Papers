# Research conversation: I need to deeply research the paper arXiv 2505.04441 (May 2025) which found that incorporating execution traces into rep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a169391eaefd9ac97.jsonl`
- **Structured JSON:** [`a4e32e56da788229abe3.json`](../../sessions/a4/a4e32e56da788229abe3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

41 recorded events

### User

_source line 1 · 2026-05-11T22:49:02.330Z_

I need to deeply research the paper arXiv 2505.04441 (May 2025) which found that incorporating execution traces into repair prompts provides "limited performance improvement" in "only 2 out of 6 configurations." This directly challenges our research premise.

Please do the following:
1. WebSearch for "arXiv 2505.04441 execution traces repair limited improvement 2025"
2. WebFetch the arXiv abstract page to understand the paper's claims
3. Also search for "execution trace augmented program repair effectiveness 2025 2026" to find other papers on this topic
4. Search for "Self-Execution Simulation arXiv 2604.03253 code released data available" to check if training data/code is publicly available

I need to understand:
- What exactly arXiv 2505.04441 found about trace effectiveness
- Why trace effectiveness diminishes with complexity
- Whether this critique applies to simulation-based RANKING (our approach) vs. trace-augmented GENERATION (what they studied)
- Whether Self-Execution Simulation released its training data/code

Report all findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "dbc3b3a4-50db-4424-a6da-74595688ab4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-11T22:49:02.333Z_

```json
{
  "parentUuid": "dbc3b3a4-50db-4424-a6da-74595688ab4e",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
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
  "uuid": "2a0cd30c-e41a-4b42-b007-edd1083e84e8",
  "timestamp": "2026-05-11T22:49:02.333Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-11T22:49:04.769Z_



I'll research this thoroughly. Let me start by loading the WebSearch and WebFetch tools, then run the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a0cd30c-e41a-4b42-b007-edd1083e84e8",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbcFrNjcSeBRhGYcErC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3953329a-49cc-4d54-b882-b055aa66b2db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMHXfVy1Ky3Nw6sFpE4M2e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 803,
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

_source line 4 · 2026-05-11T22:49:05.271Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015XXHGBvV5Wbx1YKZoSmgF4`</summary>

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
  "parentUuid": "3953329a-49cc-4d54-b882-b055aa66b2db",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbcFrNjcSeBRhGYcErC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78345708-24e4-4de2-b86b-8395385e94a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMHXfVy1Ky3Nw6sFpE4M2e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 8223,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 803
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 803,
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

_source line 5 · 2026-05-11T22:49:05.275Z_

<details><summary>↩ Tool result · `toolu_015XXHGBvV5Wbx1YKZoSmgF4`</summary>

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
  "parentUuid": "78345708-24e4-4de2-b86b-8395385e94a2",
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "c4c584ef-7c0f-4b1d-b0c0-2898853a1acf",
  "sourceToolAssistantUUID": "78345708-24e4-4de2-b86b-8395385e94a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-11T22:49:07.880Z_



Now let me run all four searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4c584ef-7c0f-4b1d-b0c0-2898853a1acf",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbcUdZzCEtYkyZVJxxg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a25aa7d-45ba-426f-8893-014253d115a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FU55pv6Kgg3yfrxH7wV8St",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 7 · 2026-05-11T22:49:08.976Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012apgQfqs7WXxYUhX7EfHrZ`</summary>

```json
{
  "query": "arXiv 2505.04441 execution traces repair limited improvement 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a25aa7d-45ba-426f-8893-014253d115a1",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbcUdZzCEtYkyZVJxxg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed430746-7efe-441a-98c2-b475981ec885",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FU55pv6Kgg3yfrxH7wV8St",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 8 · 2026-05-11T22:49:09.793Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KG45do4UH7GPHrC6mEN8cE`</summary>

```json
{
  "query": "execution trace augmented program repair effectiveness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed430746-7efe-441a-98c2-b475981ec885",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbcUdZzCEtYkyZVJxxg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aed17952-898b-410d-8a84-25cb87f8d219",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FU55pv6Kgg3yfrxH7wV8St",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1917,
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

_source line 9 · 2026-05-11T22:49:10.169Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BHeqQiFutbL8gtve1gZ4AY`</summary>

```json
{
  "query": "Self-Execution Simulation arXiv 2604.03253 code released data available"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aed17952-898b-410d-8a84-25cb87f8d219",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbcUdZzCEtYkyZVJxxg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60569844-b4c6-41f2-b75b-0ad5e0379633",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FU55pv6Kgg3yfrxH7wV8St",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1917,
      "cache_read_input_tokens": 9026,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1917
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 182,
          "cache_read_input_tokens": 9026,
          "cache_creation_input_tokens": 1917,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1917,
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

_source line 10 · 2026-05-11T22:49:15.120Z_

<details><summary>↩ Tool result · `toolu_012apgQfqs7WXxYUhX7EfHrZ`</summary>

```text
Web search results for query: "arXiv 2505.04441 execution traces repair limited improvement 2025"

Links: [{"title":"[2505.04441] Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/abs/2505.04441"},{"title":"arXiv:2505.04441v1 [cs.LG] 7 May 2025","url":"https://arxiv.org/pdf/2505.04441"},{"title":"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/html/2505.04441v1"},{"title":"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate","url":"https://arxiv.org/html/2604.02647v1"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=500&show=1000"},{"title":"Machine Learning May 2025","url":"https://www.arxiv.org/list/cs.LG/2025-05?skip=375&show=25"},{"title":"Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs","url":"https://arxiv.org/html/2503.21710v1"},{"title":"[2505.04493] Model-Based AI planning and Execution Systems for Robotics","url":"https://arxiv.org/abs/2505.04493"},{"title":"arXiv:2505.08903v2 [cs.SE] 10 Jun 2025 111","url":"https://arxiv.org/pdf/2505.08903v2"}]

I found the paper you were looking for! Here's what the research reveals:

The paper "Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs" (arXiv 2505.04441) investigates how execution traces can improve automated program repair using large language models.

**Key Finding:**
The research found that simply incorporating execution traces into the prompt provides a limited performance improvement over trace-free baselines, in only 2 out of 6 tested dataset / model configurations.

**Additional Insights:**
- The effectiveness of execution traces for program repair diminishes as their complexity increases.
- The researchers explored several strategies for leveraging traces in prompts and demonstrated that LLM-optimized prompts help outperform trace-free prompts more consistently.
- Trace-based prompting was shown to be superior to fine-tuning a smaller LLM on a small-scale dataset, and probing studies reinforced the notion that execution traces can complement the reasoning abilities of the LLMs.

The paper suggests that while execution traces have potential, a more sophisticated approach to prompt optimization is needed to effectively leverage them for program repair tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed430746-7efe-441a-98c2-b475981ec885",
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "38321467-0f96-428f-920a-c0b91d16dc07",
  "sourceToolAssistantUUID": "ed430746-7efe-441a-98c2-b475981ec885",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-11T22:49:16.179Z_

<details><summary>↩ Tool result · `toolu_01BHeqQiFutbL8gtve1gZ4AY`</summary>

```text
Web search results for query: "Self-Execution Simulation arXiv 2604.03253 code released data available"

Links: [{"title":"[2604.03253] Self-Execution Simulation Improves Coding Models","url":"https://arxiv.org/abs/2604.03253"},{"title":"Self-Execution Simulation Improves Coding Models","url":"https://arxiv.org/html/2604.03253"},{"title":"Paper page - Self-Execution Simulation Improves Coding Models","url":"https://huggingface.co/papers/2604.03253"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2604.03253"},{"title":"[2604.26423] Large-Scale Quantum Circuit Simulation on an Exascale System for QPU Benchmarking","url":"https://arxiv.org/abs/2604.26423"},{"title":"[2604.19825] SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation through Concrete Execution","url":"https://arxiv.org/abs/2604.19825"},{"title":"SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation through Concrete Execution","url":"https://arxiv.org/html/2604.19825"},{"title":"[2604.23580] PhysCodeBench: Benchmarking Physics-Aware Symbolic Simulation of 3D Scenes via Self-Corrective Multi-Agent Refinement","url":"https://arxiv.org/abs/2604.23580"},{"title":"[2604.28181] Synthetic Computers at Scale for Long-Horizon Productivity Simulation","url":"https://arxiv.org/abs/2604.28181"},{"title":"Agentic Scientific Simulation: Execution-Grounded Model Construction and Reconstruction","url":"https://arxiv.org/html/2603.00214v1"}]

Based on the search results, I found information about the Self-Execution Simulation paper (arXiv 2604.03253):

## Paper Overview

The paper demonstrates that Code LLMs can be trained to simulate program execution in a step-by-step manner and that this capability can be leveraged to improve competitive programming performance. The approach combines supervised fine-tuning on natural language execution traces, textual explanations grounded in true execution, with reinforcement learning using verifiable rewards.

## Code and Data Availability

The search results show the paper on arXiv and a reference on Hugging Face Papers, but the specific search results do not contain explicit information about code release or data availability. The Hugging Face Papers page (result index 3) suggests there may be associated models or datasets, as it mentions citations to spaces, models, and datasets on that platform. 

To find the specific code and data availability for this paper, you would need to:
1. Check the paper's arXiv PDF directly at https://arxiv.org/abs/2604.03253
2. Visit the Hugging Face Papers page at https://huggingface.co/papers/2604.03253
3. Look for links to the authors' GitHub repositories or Hugging Face model/dataset pages

The paper was released on March 11, 2026, and is authored by Gallil Maimon and colleagues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60569844-b4c6-41f2-b75b-0ad5e0379633",
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "8c2165a1-822e-43f7-b124-f4e895481f74",
  "sourceToolAssistantUUID": "60569844-b4c6-41f2-b75b-0ad5e0379633",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-11T22:49:17.876Z_

<details><summary>↩ Tool result · `toolu_01KG45do4UH7GPHrC6mEN8cE`</summary>

```text
Web search results for query: "execution trace augmented program repair effectiveness 2025 2026"

Links: [{"title":"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate","url":"https://arxiv.org/html/2604.02647"},{"title":"[2505.04441] Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/abs/2505.04441"},{"title":"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/html/2505.04441v1"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"Runtime Execution Traces Guided Automated Program Repair","url":"https://arxiv.org/pdf/2604.02647"},{"title":"Integrating Attention Mechanism with Code Structural Affinity and Execution Context Correlation for Automated Bug Repair - ScienceDirect","url":"https://www.sciencedirect.com/org/science/article/pii/S1546221826000949"},{"title":"Towards Effectively Leveraging Execution Traces","url":"https://arxiv.org/pdf/2505.04441"},{"title":"Agentic APR: LLM-Based Automated Repair","url":"https://www.emergentmind.com/topics/agentic-automated-program-repair-apr"},{"title":"Towards Practical and Useful Automated Program Repair for Debugging","url":"https://arxiv.org/html/2407.08958v1"},{"title":"A Survey of LLM-based Software Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v2"}]

Based on the search results, here's what research has found about execution trace augmented program repair effectiveness in 2025-2026:

## Key Findings

### Mixed Results on Basic Trace Augmentation

Simply incorporating execution traces into the prompt provides a limited performance improvement over trace-free baselines, in only 2 out of 6 tested dataset / model configurations. The effectiveness of execution traces for APR diminishes as their complexity increases.

### Model-Dependent Benefits

Trace-based prompts improve GPT-4's correct-program accuracy by up to 6% over error-only prompts, but the benefit vanishes for GPT-3.5 and for traces that exceed 200 lines, showing that runtime context helps powerful models only when it is concise.

### Advanced Approaches Showing Promise

More sophisticated methods are demonstrating better effectiveness:

- LLM-optimized prompts help outperform trace-free prompts more consistently.
- Recent agentic APR systems integrate semantic modalities—issue abstraction, code- and execution-semantics—which enables robust repair even for multi-line or edge-case bugs.
- The framework's effectiveness stems from dynamic reasoning rather than memorization.

### Complementary Strategies

Complementary AAG strategies include: semantics-aware slices narrow the search space, failing-test evidence enables direct debugging without prior localization, and compact execution traces inject runtime semantics.

The research suggests that while basic execution trace augmentation has limited benefits, more sophisticated approaches combining traces with strategic prompting, agentic reasoning, and semantic analysis show more promising results for automated program repair effectiveness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aed17952-898b-410d-8a84-25cb87f8d219",
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "609737b4-6308-450a-afd6-bbeffd850bc8",
  "sourceToolAssistantUUID": "aed17952-898b-410d-8a84-25cb87f8d219",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-11T22:49:20.801Z_

Good, I have initial results. Now let me fetch the detailed content from the key pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "609737b4-6308-450a-afd6-bbeffd850bc8",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbdQK9ZhP64FzA4UCkw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "26f36432-0995-46dc-ba41-66021c0e4553",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KH5RiHYeyTfuKhUisxvmHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 827,
      "cache_creation_input_tokens": 1824,
      "cache_read_input_tokens": 10943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1824,
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

_source line 14 · 2026-05-11T22:49:23.379Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011Su34ikDNmaRxyBuroxTy1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.04441",
  "prompt": "Extract the full abstract, author list, all key claims about execution trace effectiveness, the specific configurations tested, and any mention of why traces have limited improvement. Include any mention of the distinction between trace-augmented generation vs. other uses of traces."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26f36432-0995-46dc-ba41-66021c0e4553",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbdQK9ZhP64FzA4UCkw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0e1957d-493e-4edc-af1f-aae029777495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KH5RiHYeyTfuKhUisxvmHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 827,
      "cache_creation_input_tokens": 1824,
      "cache_read_input_tokens": 10943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1824,
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

_source line 15 · 2026-05-11T22:49:26.927Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BX91jwAZUfW8ug4FW5xCwB`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.04441v1",
  "prompt": "Extract the detailed findings about: 1) Why execution traces provide limited improvement in only 2 of 6 configurations, 2) What the 6 configurations are (models x datasets), 3) How trace complexity affects performance, 4) What strategies they tried for leveraging traces, 5) Any discussion of trace-based ranking vs trace-augmented generation, 6) Their conclusions about when traces help vs when they don't, 7) Any specific metrics or percentages showing improvement or lack thereof. Be as detailed as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0e1957d-493e-4edc-af1f-aae029777495",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbdQK9ZhP64FzA4UCkw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a24c193-26c9-4131-a763-3d8c166d0f34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KH5RiHYeyTfuKhUisxvmHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 827,
      "cache_creation_input_tokens": 1824,
      "cache_read_input_tokens": 10943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1824,
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

_source line 16 · 2026-05-11T22:49:28.480Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TzJJtyj7ziZz4RtQZHvgZv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.03253",
  "prompt": "Extract the full abstract, author list, key claims about self-execution simulation, and any mention of code/data/model release, GitHub links, or availability of training data and artifacts."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a24c193-26c9-4131-a763-3d8c166d0f34",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbdQK9ZhP64FzA4UCkw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25421d63-e180-4e8b-82f8-76918f9fef87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KH5RiHYeyTfuKhUisxvmHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 827,
      "cache_creation_input_tokens": 1824,
      "cache_read_input_tokens": 10943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1824,
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

_source line 17 · 2026-05-11T22:49:28.733Z_

<details><summary>↩ Tool result · `toolu_011Su34ikDNmaRxyBuroxTy1`</summary>

```text
# Paper Analysis: Execution Traces for Program Repair with Code LLMs

## Full Abstract

The paper examines how augmenting Automatic Program Repair (APR) prompts with program execution traces affects LLM performance. Key findings indicate that "simply incorporating execution traces into the prompt provides a limited performance improvement over trace-free baselines, in only 2 out of 6 tested dataset / model configurations."

## Authors

- Mirazul Haque
- Petr Babkin
- Farima Farmahinifarahani
- Manuela Veloso

## Key Claims About Execution Trace Effectiveness

1. **Limited baseline improvement**: "execution traces provides a limited performance improvement over trace-free baselines" in only a minority of configurations tested

2. **Complexity diminishes returns**: "effectiveness of execution traces for APR diminishes as their complexity increases"

3. **Prompt optimization helps**: "LLM-optimized prompts help outperform trace-free prompts more consistently" compared to simple trace incorporation

4. **Superiority over finetuning**: "trace-based prompting to be superior to finetuning a smaller LLM on a small-scale dataset"

## Configurations Tested

- **Models**: GPT family of models
- **Datasets**: Three popular APR datasets
- **Total configurations evaluated**: Six dataset/model combinations

## Why Limited Improvement

The abstract suggests that while execution traces can complement LLM reasoning abilities, naive trace integration provides insufficient benefit. The paper demonstrates that strategic prompt engineering and trace optimization are necessary for meaningful gains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0e1957d-493e-4edc-af1f-aae029777495",
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "649f536e-a67b-47bb-912f-e0db9119f44f",
  "sourceToolAssistantUUID": "c0e1957d-493e-4edc-af1f-aae029777495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-11T22:49:30.021Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VHjNMsLt5Fz5wNryjkKuez`</summary>

```json
{
  "url": "https://huggingface.co/papers/2604.03253",
  "prompt": "Extract any information about released code, models, datasets, GitHub repositories, or Hugging Face model/dataset links associated with the Self-Execution Simulation paper. Look for any links to repos, model cards, or dataset pages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "649f536e-a67b-47bb-912f-e0db9119f44f",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbdQK9ZhP64FzA4UCkw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdc0506b-12f0-4e56-a97b-babd347e2552",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KH5RiHYeyTfuKhUisxvmHV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 827,
      "cache_creation_input_tokens": 1824,
      "cache_read_input_tokens": 10943,
      "output_tokens": 548,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1824
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 827,
          "output_tokens": 548,
          "cache_read_input_tokens": 10943,
          "cache_creation_input_tokens": 1824,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1824,
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

_source line 19 · 2026-05-11T22:49:30.651Z_

<details><summary>↩ Tool result · `toolu_01VHjNMsLt5Fz5wNryjkKuez`</summary>

```text
&lt;persisted-output>
Output too large (82.4KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-/f7ed7f67-a87f-46e7-a409-d4d552b7568f/tool-results/toolu_01VHjNMsLt5Fz5wNryjkKuez.txt

Preview (first 2KB):
Title: Self-Execution Simulation Improves Coding Models

URL Source: https://arxiv.org/html/2604.03253

Markdown Content:
Ori Yoran Felix Kreuk Michael Hassid Gal Cohen Pierre Chambon Yossi Adi

###### Abstract

A promising research direction in enabling LLMs to generate consistently correct code involves addressing their inability to properly estimate program execution, particularly for code they generate. In this work, we demonstrate that code LLMs can be trained to simulate program execution in a step-by-step manner and that this capability can be leveraged to improve competitive programming performance. Our approach combines supervised fine-tuning on natural language execution traces, textual explanations grounded in true execution, with reinforcement learning using verifiable rewards. We introduce two complementary objectives: output prediction given code and inputs, and solving competitive programming tasks with either ground-truth or self-predicted execution feedback. These objectives enable models to perform _self-verification_ over multiple candidate solutions, and iterative _self-fixing_ by simulating test execution. Across multiple competitive programming benchmarks, our method yields consistent improvements over standard reasoning approaches. We further present ablations and analysis to elucidate the role of execution simulation and its limitations.

Code LLM, execution feedback, code world model

## 1 Introduction

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdc0506b-12f0-4e56-a97b-babd347e2552",
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "29d3ce6d-e0cd-4821-b147-7480e56b654b",
  "sourceToolAssistantUUID": "bdc0506b-12f0-4e56-a97b-babd347e2552",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-11T22:49:34.341Z_

<details><summary>↩ Tool result · `toolu_01TzJJtyj7ziZz4RtQZHvgZv`</summary>

```text
# Paper Summary: Self-Execution Simulation Improves Coding Models

## Full Abstract
"A promising research direction in enabling LLMs to generate consistently correct code involves addressing their inability to properly estimate program execution, particularly for code they generate. In this work, we demonstrate that Code LLMs can be trained to simulate program execution in a step-by-step manner and that this capability can be leveraged to improve competitive programming performance. Our approach combines supervised fine-tuning on natural language execution traces, textual explanations grounded in true execution, with reinforcement learning using verifiable rewards. We introduce two complementary objectives: output prediction given code and inputs, and solving competitive programming tasks with either ground-truth or self-predicted execution feedback. These objectives enable models to perform self-verification over multiple candidate solutions, and iterative self-fixing by simulating test execution. Across multiple competitive programming benchmarks, our method yields consistent improvements over standard reasoning approaches. We further present ablations and analysis to elucidate the role of execution simulation and its limitations."

## Author List
Gallil Maimon, Ori Yoran, Felix Kreuk, Michael Hassid, Gal Cohen, Pierre Chambon, Yossi Adi

## Key Claims About Self-Execution Simulation
- Models can learn to "simulate program execution in a step-by-step manner"
- Enables self-verification capabilities across multiple solution candidates
- Supports "iterative self-fixing by simulating test execution"
- Produces "consistent improvements over standard reasoning approaches" on competitive programming benchmarks

## Code/Data/Model Release Information
**None mentioned.** The page contains no references to GitHub repositories, code availability, dataset releases, or downloadable artifacts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25421d63-e180-4e8b-82f8-76918f9fef87",
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "a2e4f26c-50bc-4b5d-86e4-5d67e71502af",
  "sourceToolAssistantUUID": "25421d63-e180-4e8b-82f8-76918f9fef87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-11T22:49:43.335Z_

<details><summary>↩ Tool result · `toolu_01BX91jwAZUfW8ug4FW5xCwB`</summary>

```text
# Analysis of Execution Traces for Program Repair with Code LLMs

## 1) Why Execution Traces Provide Limited Improvement

The research reveals that "simply incorporating execution traces into the prompt provides a limited performance improvement over trace-free baselines, in only 2 out of 6 tested dataset / model configurations." Several factors explain this limitation:

- **Model capability disparity**: GPT-3.5 showed degraded performance with traces, while GPT-4 demonstrated benefits on some datasets, suggesting a "qualitative generational gap when it comes to emergent abilities of LLMs."

- **Trace complexity as hindrance**: The authors discovered that "longer traces could undermine rather than help APR," with failing fixes associated with significantly longer traces than successful ones.

- **Information overload**: Overly complex traces may "overwhelm LLMs' long context and ultimately confuse it" rather than providing helpful debugging information.

## 2) The Six Configurations

The 6 tested configurations comprised:

| Model | Dataset |
|-------|---------|
| GPT-3.5 | Refactory |
| GPT-3.5 | HumanEval-Java |
| GPT-3.5 | RunBugRun |
| GPT-4 | Refactory |
| GPT-4 | HumanEval-Java |
| GPT-4 | RunBugRun |

**Performance results**: Trace prompts outperformed error-only prompts in only the GPT-4 configurations for HumanEval-Java and RunBugRun. Notably, "For both GPT-3.5 and GPT-4 on the Refactory dataset, prompts including just a failing test case decisively outperform ones with execution traces."

## 3) How Trace Complexity Affects Performance

The research identified two critical complexity metrics:

**Trace length impact**: Analysis showed "for both the HumanEval-Java and RunBugRun datasets, median trace length and number of variable modifications were significantly higher for failing fixes than for the correct ones."

**Variable modification patterns**: The data demonstrated "longer traces have a lower chance of generating a correct fix," with the Refactory dataset showing median variable modifications of just one for successful fixes versus five in RunBugRun.

**Dataset variations**: Interestingly, the Refactory dataset showed opposite patterns—failing fixes had lower median trace lengths—suggesting "variable modifications could play a key role in the effectiveness of a trace for APR."

## 4) Strategies for Leveraging Traces

The research tested three primary strategies:

**Collated traces**: Inline comments placed directly at corresponding code lines rather than standalone sections. This approach "disappointingly do[es] not provide an improvement over trace prompts," possibly due to lack of training exposure to this format.

**LLM-optimized traces (OPT)**: Prompting GPT-4-32k to condense lengthy traces. This proved most effective, providing "the most consistent performance gains on both CFA and CPA metrics" across all dataset-model pairs.

**Confidence-based selection (Conf OPT)**: Using Likert-scale confidence scoring (1-5 scale, routing to optimized traces if score <3) to choose between prompt types. Performance "is significantly worse than OPT on average," suggesting unreliability.

**Trace-length routing (TRL OPT)**: Switching between prompts based on predetermined trace-length thresholds (N=25-50). Results showed "routing could improve the CFA and CPA values more than individual prompts" in limited cases, but overall "routing between techniques based on trace length might be significantly beneficial" was not consistently demonstrated.

## 5) Trace-Based Ranking vs Trace-Augmented Generation

The paper does not explicitly discuss trace-based ranking versus trace-augmented generation. The focus remains on prompt augmentation with execution traces for direct code repair generation rather than ranking or alternative generation strategies.

## 6) Conclusions About When Traces Help vs When They Don't

**Traces help when**:
- Using GPT-4 on HumanEval-Java and RunBugRun datasets with optimized trace formats
- Traces are relatively short and contain fewer variable modifications
- Traces are processed through LLM-optimization before inclusion in prompts

**Traces don't help when**:
- Using GPT-3.5 (shows consistent degradation or minimal improvement)
- Applied to Refactory dataset across both GPT versions
- Traces are long, complex, or contain excessive variable assignments
- Traces are presented in collated/inline comment formats
- Confidence-based or simple length-based routing is applied

The authors conclude: "trace-based prompts do not consistently outperform error-based prompts; their effectiveness varies with the dataset and LLM used."

## 7) Specific Metrics and Performance Data

**RQ1 Results (Correct Fix Accuracy)**:
- GPT-4 on Refactory: Error prompts (0.791) vs. Trace prompts (0.737)
- GPT-4 on HumanEval-Java: Trace prompts (0.511) vs. Error prompts (0.493)
- GPT-4 on RunBugRun: Trace prompts (0.558) vs. Error prompts (0.529)

**RQ3 Optimization Results**:
- OPT traces achieved best CFA on 3 of 6 configurations
- OPT traces ranked in top-3 for CPA across all 6 configurations
- Collated traces: 0.452-0.656 CFA (worse than baselines)
- OPT traces: 0.472-0.753 CFA (generally exceeding baselines)

**Probing studies**: GPT-4 achieved only 88% accuracy at trace collation on reference programs but just 45% on diverse datasets; trace prediction from scratch never exceeded 50% accuracy on reference programs and dropped to 15% on diverse datasets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a24c193-26c9-4131-a763-3d8c166d0f34",
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "10f012cd-035a-4988-8e2e-bb35152be4b1",
  "sourceToolAssistantUUID": "7a24c193-26c9-4131-a763-3d8c166d0f34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-11T22:49:46.341Z_

Let me fetch the full HTML of the Self-Execution Simulation paper to check for code/data release details, and also fetch the multi-agent debate paper that appeared in the search results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10f012cd-035a-4988-8e2e-bb35152be4b1",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbfH9qtJGshu8VTcMoq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f74019f-6b38-49dd-a944-43b74bf29d86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WySnFzHPnrQoC8Jp37kzXW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 3274,
      "cache_read_input_tokens": 12767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3274,
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

_source line 23 · 2026-05-11T22:49:47.907Z_

<details open><summary>🔧 Tool call — Read · `toolu_012axSra4hCJnpjFreukh8iA`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-/f7ed7f67-a87f-46e7-a409-d4d552b7568f/tool-results/toolu_01VHjNMsLt5Fz5wNryjkKuez.txt",
  "limit": 200,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f74019f-6b38-49dd-a944-43b74bf29d86",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbfH9qtJGshu8VTcMoq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42fa6b90-8922-4893-92b9-45a0355879d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WySnFzHPnrQoC8Jp37kzXW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 3274,
      "cache_read_input_tokens": 12767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3274,
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

_source line 24 · 2026-05-11T22:49:48.175Z_

<details><summary>↩ Tool result · `toolu_012axSra4hCJnpjFreukh8iA`</summary>

```text
0	Title: Self-Execution Simulation Improves Coding Models
1	
2	URL Source: https://arxiv.org/html/2604.03253
3	
4	Markdown Content:
5	Ori Yoran Felix Kreuk Michael Hassid Gal Cohen Pierre Chambon Yossi Adi
6	
7	###### Abstract
8	
9	A promising research direction in enabling LLMs to generate consistently correct code involves addressing their inability to properly estimate program execution, particularly for code they generate. In this work, we demonstrate that code LLMs can be trained to simulate program execution in a step-by-step manner and that this capability can be leveraged to improve competitive programming performance. Our approach combines supervised fine-tuning on natural language execution traces, textual explanations grounded in true execution, with reinforcement learning using verifiable rewards. We introduce two complementary objectives: output prediction given code and inputs, and solving competitive programming tasks with either ground-truth or self-predicted execution feedback. These objectives enable models to perform _self-verification_ over multiple candidate solutions, and iterative _self-fixing_ by simulating test execution. Across multiple competitive programming benchmarks, our method yields consistent improvements over standard reasoning approaches. We further present ablations and analysis to elucidate the role of execution simulation and its limitations.
10	
11	Code LLM, execution feedback, code world model
12	
13	## 1 Introduction
14	
15	Going beyond treating code as a static text block holds great promise in advancing code LLMs. This involves jointly modelling program syntax and execution dynamics, similar to how developers reason during debugging and development(Armengol-Estapé et al., [2025](https://arxiv.org/html/2604.03253#bib.bib7 "What i cannot execute, i do not understand: training and evaluating llms on program execution traces"); Li et al., [2025](https://arxiv.org/html/2604.03253#bib.bib62 "CodeIO: condensing reasoning patterns via code input-output prediction"); Thimmaiah et al., [2025](https://arxiv.org/html/2604.03253#bib.bib46 "PLSemanticsBench: large language models as programming language interpreters"); Copet et al., [2025](https://arxiv.org/html/2604.03253#bib.bib25 "Cwm: an open-weights llm for research on code generation with world models"); Beck et al., [2026](https://arxiv.org/html/2604.03253#bib.bib69 "Towards a neural debugger for python")). Despite its promise, translating execution prediction capabilities into consistent gains on practical programming tasks remains an open challenge. Moreover, Gu et al. ([2024a](https://arxiv.org/html/2604.03253#bib.bib14 "The counterfeit conundrum: can code language models grasp the nuances of their incorrect generations?")); Olausson et al. ([2024](https://arxiv.org/html/2604.03253#bib.bib11 "Is self-repair a silver bullet for code generation?")); Kamoi et al. ([2024](https://arxiv.org/html/2604.03253#bib.bib15 "When can llms actually correct their own mistakes? a critical survey of self-correction of llms")) indicate that current models often fail to faithfully simulate runtime behaviour or to consistently identify and explain errors in code they generate.
16	
17	Code execution is widely used in various parts of training and inference of code LLMs. This includes feedback from code execution(Gehring et al., [2025](https://arxiv.org/html/2604.03253#bib.bib8 "RLEF: grounding code LLMs in execution feedback with reinforcement learning"); Peng et al., [2025](https://arxiv.org/html/2604.03253#bib.bib9 "PerfCodeGen: improving performance of llm generated code with execution feedback")) or rich tool-based signals in agentic settings(Xia et al., [2025](https://arxiv.org/html/2604.03253#bib.bib57 "Live-swe-agent: can software engineering agents self-evolve on the fly?")). However, executing code at scale for training or inference poses practical challenges, such as environment setup(Bogin et al., [2024](https://arxiv.org/html/2604.03253#bib.bib52 "Super: evaluating agents on setting up and executing tasks from research repositories")), managing code dependencies(Jimenez et al., [2023](https://arxiv.org/html/2604.03253#bib.bib37 "Swe-bench: can language models resolve real-world github issues?")), handling partial or non-executable code, and sandboxing. In broader settings, program execution can also be computationally expensive and time-consuming; for example, runs of MLE-Bench can take up to 9 9 hours(Chan et al., [2024](https://arxiv.org/html/2604.03253#bib.bib60 "Mle-bench: evaluating machine learning agents on machine learning engineering"); Zheng et al., [2026](https://arxiv.org/html/2604.03253#bib.bib61 "Can we predict before executing machine learning agents?")). Predicting execution outcomes could mitigate these challenges by enabling large rollouts and policy optimisation without code execution(MiniMax, [2026](https://arxiv.org/html/2604.03253#bib.bib51 "M2.1: multilingual and multi-task coding with strong generalization"); Kimi et al., [2025](https://arxiv.org/html/2604.03253#bib.bib68 "Kimi k2: open agentic intelligence")). More broadly, using execution prediction to support reasoning and planning in coding tasks can be viewed as a form of world modelling in the code domain(Ha and Schmidhuber, [2018](https://arxiv.org/html/2604.03253#bib.bib65 "World models"); Ding et al., [2025](https://arxiv.org/html/2604.03253#bib.bib64 "Understanding world or predicting future? a comprehensive survey of world models")).
18	
19	![Image 1: Refer to caption](https://arxiv.org/html/2604.03253v1/x1.png)
20	
21	Figure 1: A conceptual outline of how one can use _self-execution simulation_ of a generated code solution (or solutions) on public or generated test cases to improve coding performance. The simulation can be used as feedback to select the best solution from a few candidates (best@k) or to iteratively fix the code as needed (self-RLEF). See Section [3](https://arxiv.org/html/2604.03253#S3 "3 Self-Execution For Verification ‣ Self-Execution Simulation Improves Coding Models") for details.
22	
23	In this work, we take a step in this direction. We show LLMs can learn to simulate program execution step-by-step, including code they generated, and use this capability to improve competitive programming performance. We start by training models on natural-language execution traces – text explanations grounded in real program executions – and then further refining them using single-turn reinforcement learning for code output prediction. Equipped with this capability, we empirically demonstrate how models can perform _self-verification_ over parallel solutions based on simulated execution (best@k). Inspired by Gehring et al. ([2025](https://arxiv.org/html/2604.03253#bib.bib8 "RLEF: grounding code LLMs in execution feedback with reinforcement learning")), we also design a multi-turn reinforcement learning pipeline that enables iterative _self-fixing_ through code proposal, execution simulation, and refinement. [Figure 1](https://arxiv.org/html/2604.03253#S1.F1 "In 1 Introduction ‣ Self-Execution Simulation Improves Coding Models") provides a conceptual overview of the proposed methods.
24	
25	Results suggest the proposed training recipe leads to significant improvements in output prediction on CruxEval(Gu et al., [2024b](https://arxiv.org/html/2604.03253#bib.bib6 "CRUXEval: a benchmark for code reasoning, understanding and execution")) (up to 43%43\%) and competitive programming solutions(Li et al., [2022](https://arxiv.org/html/2604.03253#bib.bib20 "Competition-level code generation with alphacode"); Jain et al., [2024](https://arxiv.org/html/2604.03253#bib.bib38 "Livecodebench: holistic and contamination free evaluation of large language models for code")) (up to 39%39\%) relative to the evaluated baseline. This applies to both external and self-generated code solutions. Under the best@k setting, using the model’s output prediction to verify its own candidate solutions improves code correctness by up to 5.5%5.5\% absolute points on competitive programming tasks. In the multi-turn setting, we observe consistent gains across all evaluated configurations. Compared to ground-truth execution, both best@k and multi-turn variants show a relatively small degradation. Finally, we conduct analysis to highlight the strengths and limitations of the proposed approach.
26	
27	Our Contributions: We provide a training recipe, showing that code LLMs are capable of simulating the program execution for both external and self-generated code. With that in mind, we introduce a practical framework for leveraging this behaviour by filtering code solutions based on predicted output (i.e., self-verification). Lastly, we present a multi-turn training and inference process to perform iterative self-fixing of the model’s generated code.
28	
29	![Image 2: Refer to caption](https://arxiv.org/html/2604.03253v1/x2.png)
30	
31	Figure 2: The two parts of our training pipeline. 1) Supervised fine tuning on natural language execution traces (NLEX), 2) Multi-task reinforcement learning on output prediction and competitive programming (optionally with multi-turn feedback and fixing).
32	
33	## 2 Boosting Execution Simulation
34	
35	Following Copet et al. ([2025](https://arxiv.org/html/2604.03253#bib.bib25 "Cwm: an open-weights llm for research on code generation with world models")), we collect executable Python programs with input–output pairs and record their line-by-line execution. Next, we convert these execution traces into natural-language explanations and use the resulting data for supervised fine-tuning. We then further train the model using verifiable rewards on an output prediction task. The next sections describe these post-training steps in detail.
36	
37	### 2.1 Natural Language Execution Tracing (NLEX)
38	
39	We collect Python functions from public repositories and automatically synthesise suitable inputs using a combination of LLM prompting and lightweight fuzzing techniques. In addition, we collect LLM-generated solutions to competitive programming problems from CodeContests(Li et al., [2022](https://arxiv.org/html/2604.03253#bib.bib20 "Competition-level code generation with alphacode")), and keep their provided tests as inputs. Although this portion of the data is smaller in scale, it involves substantially more complex programs. We then record execution traces for each program–input pair, capturing intermediate variable states throughout execution. Following Copet et al. ([2025](https://arxiv.org/html/2604.03253#bib.bib25 "Cwm: an open-weights llm for research on code generation with world models")), we exclude traces exceeding 10​k 10\text{k} events or requiring more than 1​MB 1\text{MB} of storage. The resulting dataset comprises ∼30​M{\sim}30\text{M} functions from basic code sources and 35​k 35\text{k} from competitive programming problems. For all of the above, we use Llama3-70B-Instruct (Grattafiori et al., [2024](https://arxiv.org/html/2604.03253#bib.bib23 "The llama 3 herd of models")).
40	
41	While CWM (Copet et al., [2025](https://arxiv.org/html/2604.03253#bib.bib25 "Cwm: an open-weights llm for research on code generation with world models")) focused primarily on a structured, JSON-like format to describe the step-by-step execution, we wish to focus on natural language description of this data. Relative to the structured format, a free-form variant holds several benefits. First, as based on natural language, it closely matches the reasoning-style data already used by LLMs. It also enables adding semantic context to operations, e.g., explaining an update to an array in the scope of a dynamic programming code. Finally, it naturally abstracts away unnecessary details, such as summarising a long loop that reverses strings character by character.
42	
43	To this end, we prompt Qwen3-32B-FP8 (without thinking) (Yang et al., [2025](https://arxiv.org/html/2604.03253#bib.bib21 "Qwen3 technical report")) to “translate” execution traces from raw structured format to a natural language explanation. See Appendix [A.4](https://arxiv.org/html/2604.03253#A1.SS4 "A.4 Prompts ‣ Reinforcement Learning. ‣ A.3 Hyper-Parameters ‣ A.2 Self-RLEF Example Inference ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models") for the exact prompt. We discard instances where the model’s predicted output does not match the ground truth, resulting in ∼80{\sim}80 M execution descriptions for general Python functions and 115 115 k for competitive programming solutions (notice, each traced function may contain several io-pairs). The resulting data is formatted as instruction-following examples and used for model fine-tuning during the SFT phase. In which, the user requests a step-by-step explanation of a program’s execution for a given input, and the assistant provides the translated explanation. Sample instances are provided in Appendix[A.5](https://arxiv.org/html/2604.03253#A1.SS5 "A.5 Data Samples ‣ A.4 Prompts ‣ Reinforcement Learning. ‣ A.3 Hyper-Parameters ‣ A.2 Self-RLEF Example Inference ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models").
44	
45	### 2.2 Output Prediction Environment
46	
47	Following standard practice in reasoning models, we post-train our model using Reinforcement Learning with Verifiable Rewards (RLVR). We define an output prediction environment, based on coding tasks, where the model reasons over a given (code, stdin) pair to predict the resulting stdout. We employ a terminal binary reward, scoring +1+1 if the prediction matches the true stdout, and −1-1 otherwise, allowing 1​e−5 1e-5 tolerance in float comparisons.
48	
49	The intended downstream use of the output prediction ability is simulating the execution of model generated solutions to competitive programming questions. To that end, we construct the output prediction environment on precisely such data. We collect solutions from strong LLMs to competitive programming questions and use the stdin of the matching public tests. Moreover, the higher difficulty of competitive programming problems makes them particularly well suited for post-training. [Figure 2](https://arxiv.org/html/2604.03253#S1.F2 "In 1 Introduction ‣ Self-Execution Simulation Improves Coding Models") depicts the optimisation pipeline.
50	
51	## 3 Self-Execution For Verification
52	
53	Given models with increased ability to simulate code execution, we ask _“How can this ability be used to boost programming abilities?”_ Arguably, the simplest and most straightforward approach to leverage such capability is through post-hoc solution filtering. In this approach, candidate solutions are simulated on public or generated tests and retained only if their predicted outputs align with the expected ones.
54	
55	For that, we adopt a best-of-k k (best@k k) evaluation setup, where the model independently samples k k candidate solutions and selects the final one based on predefined criteria. In our setup, selection is based on the model’s execution prediction. In other words, for each candidate, the model simulates its execution on public test cases and checks whether the predicted outputs match the expected ones. The candidate predicted to pass the greatest number of public tests is selected for submission. In case of a tie we randomly select a solution among the ones that passed the maximum number of tests. We denote this approach best@k simulate. Notice, during inference we do not access any private tests nor ground-truth verification.
56	
57	Formally, given a set of solutions 𝒮\mathcal{S}, with public input-output pairs (i​n t,o​u​t t)∈𝒯(in_{t},out_{t})\in\mathcal{T}, we use a model to simulate execution, predict the output ℳ sim​(s,i​n t)\mathcal{M}_{\text{sim}}(s,in_{t}), and select:
58	
59	Best​(𝒮)≔arg​max s∈𝒮​∑(i​n t,o​u​t t)∈𝒯 𝟏​[ℳ sim​(s,i​n t)=o​u​t t].\mathrm{Best}(\mathcal{S})\coloneqq\operatorname*{arg\,max}_{s\in\mathcal{S}}\sum_{(in_{t},out_{t})\in\mathcal{T}}\mathbf{1}\!\left[\mathcal{M}_{\text{sim}}(s,in_{t})=out_{t}\right].
60	
61	We use `rank_score_at_k`(Hassid et al., [2024](https://arxiv.org/html/2604.03253#bib.bib28 "The larger the better? improved llm code-generation via budget reallocation")) to provide an unbiased accuracy estimate for generating k k solutions and selecting the one with the highest score under the proposed heuristic. Specifically, we use 20 20 generated solutions per task and 5 5 output-prediction attempts per test.
62	
63	Recall, the primary focus of this work is _self_-simulation. In which, the same LLM is used to both generate candidate solutions and simulate their execution. That said, the same method can also be applied to solutions produced by other models. In[Section 6](https://arxiv.org/html/2604.03253#S6 "6 Results ‣ Self-Execution Simulation Improves Coding Models"), we present empirical evidence demonstrating the efficacy of this approach in both setups.
64	
65	## 4 Self-Execution For Fixing
66	
67	Another approach to leveraging execution feedback is through multi-turn interaction with a computational environment to perform code fixing. Gehring et al. ([2025](https://arxiv.org/html/2604.03253#bib.bib8 "RLEF: grounding code LLMs in execution feedback with reinforcement learning")) demonstrated that exposing LLMs to environmental feedback can enhance programming performance by allowing models to iteratively refine solutions based on information from failed test cases. However, as mentioned above, this may introduce practical challenges such as environment configuration, code dependencies, and non-executable code.
68	
69	Motivated by this paradigm, we introduce an approach that uses predicted execution outputs as feedback instead of actual program execution. Note, unlike the method presented in [Section 3](https://arxiv.org/html/2604.03253#S3 "3 Self-Execution For Verification ‣ Self-Execution Simulation Improves Coding Models"), that verifies multiple solutions via self-execution, the multi-turn setup refines solutions sequentially based on predicted feedback. Ideally, this approach can leverage richer signals, such as past solutions and execution details. While similar world-modelling approaches have been explored in vision, recent work shows limited gains from such signals(Qian et al., [2026](https://arxiv.org/html/2604.03253#bib.bib67 "Current agents fail to leverage world model as tool for foresight")). In contrast, we show that using execution simulation can improve performance.
70	
71	Algorithm 1 Multi-Turn Self-RLEF Rollout
72	
73	0: model
74	
75	M M
76	, question
77	
78	q q
79	, public tests
80	
81	T p​u​b={(i​n t,o​u​t t)}T_{pub}=\{(in_{t},out_{t})\}
82	
83	1:
84	
85	s←M​(q)s\leftarrow M(q)
86	{Generate an initial code solution}
87	
88	2:
89	
90	k←1 k\leftarrow 1
91	
92	3:while
93	
94	k≤K max k\leq K_{\max}
95	do
96	
97	4:for
98	
99	(i​n t,o​u​t t)∈T p​u​b(in_{t},out_{t})\in T_{pub}
100	do
101	
102	5:
103	
104	o​u​t^t←M​(s,i​n t)\hat{out}_{t}\leftarrow M(s,in_{t})
105	{self execution simulation}
106	
107	6:end for
108	
109	7:
110	
111	s​u​b​_​f​i​x←M​(q,s,{(i​n t,o​u​t t,o​u​t^t)})sub\_fix\leftarrow M(q,s,\{(in_{t},out_{t},\hat{out}_{t})\})
112	{Submit current code as correct or provide new solution}
113	
114	8:if
115	
116	s​u​b​_​f​i​x=submit sub\_fix=\texttt{submit}
117	then
118	
119	9:Return
120	
121	s s
122	
123	10:else
124	
125	11:
126	
127	s←s​u​b​_​f​i​x s\leftarrow sub\_fix
128	
129	12:end if
130	
131	13:
132	
133	k←k+1 k\leftarrow k+1
134	
135	14:end while
136	
137	Specifically, we propose a multi-turn environment with explicit context switching, i.e. where each interaction step is represented as an independent single-turn prompt containing only the relevant information (see details in the bullets below). This design enables fine-grained control over information flow. For instance, ensuring that execution simulation is isolated from solution reasoning and from access to the correct outputs. Moreover, it mitigates long-context challenges commonly associated with multi-turn reasoning(Yao et al., [2022](https://arxiv.org/html/2604.03253#bib.bib43 "React: synergizing reasoning and acting in language models")). Finally, this context switching also naturally allows one to extend the number of fix turns at inference as each fix turn is independent. A formal description of the rollout procedure is provided in Algorithm[1](https://arxiv.org/html/2604.03253#alg1 "Algorithm 1 ‣ 4 Self-Execution For Fixing ‣ Self-Execution Simulation Improves Coding Models"), and an example inference of our model in Appendix [A.2](https://arxiv.org/html/2604.03253#A1.SS2 "A.2 Self-RLEF Example Inference ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models"). In words, the multi-turn setup is designed as follows:
138	
139	*   •
140	Turn 1 - Solve - Given a question, provide a code solution to solve the provided question.
141	
142	*   •
143	Turn 2 - Simulate - Given a code snippet and a test input, simulate the execution and predict the output that will be printed to the standard output. This step is performed independently for each public test.
144	
145	*   •
146	Turn 3 - Submit or Fix - Given a question, a candidate solution and feedback about each test (input, expected output, predicted output), decide whether the code is correct or not. If correct, submit the code solution, otherwise, fix the code to provide a new solution.
147	
148	*   •
149	Optional - Repeat turns 2 and 3 until a code solution is submitted or the maximum turns are reached.
150	
151	Since the model’s ability to accurately predict execution outcomes may be weak at the start of RL training, relying solely on self-predicted feedback could lead the model to disregard this noisy signal. To mitigate this, we initially provide ground-truth execution feedback during training. As training progresses, one might switch from true execution signals to model-predicted execution outputs(Bengio et al., [2015](https://arxiv.org/html/2604.03253#bib.bib44 "Scheduled sampling for sequence prediction with recurrent neural networks")). Alternatively, transition can also be deferred entirely to inference time. Our preliminary results showed no noticeable gap between the approaches, so we use the latter for simplicity. We denote the following approach _Self-RLEF_.
152	
153	## 5 Experimental Setup
154	
155	### 5.1 Datasets
156	
157	We describe all datasets and configurations used to train and evaluate our models and baselines below. Note that each problem in competitive programming usually includes between one and four public test cases, typically provided in the problem description. These serve as basic checks for correctness and output formatting. In addition, a larger set of private tests, unavailable to the model, is used to better assess solution correctness, including coverage of edge cases and compliance with runtime constraints.
158	
159	#### 5.1.1 Training datasets
160	
161	The NLEX dataset, as presented in[Section 2.1](https://arxiv.org/html/2604.03253#S2.SS1 "2.1 Natural Language Execution Tracing (NLEX) ‣ 2 Boosting Execution Simulation ‣ Self-Execution Simulation Improves Coding Models"), was used for supervised fine-tuning, together with OpenMathReasoning(Moshkov et al., [2025](https://arxiv.org/html/2604.03253#bib.bib40 "Aimo-2 winning solution: building state-of-the-art mathematical reasoning models with openmathreasoning dataset")) and OpenCodeReasoning(Ahmad et al., [2025](https://arxiv.org/html/2604.03253#bib.bib41 "Opencodereasoning: advancing data distillation for competitive coding")) datasets, to bootstrap reasoning abilities.
162	
163	During RL, models were optimised for both solving and predicting the output of competitive programming solutions. For that, we use the training split derived from CodeContests(Li et al., [2022](https://arxiv.org/html/2604.03253#bib.bib20 "Competition-level code generation with alphacode")), after heuristically filtering malformed instances, which results in ∼12.2{\sim}12.2 k problems. For output prediction, we sample 10 10 candidate solutions and retain up to four correct ones per model, since all correct submissions yield identical outputs. We then pair each retained solution with all of its public test cases, treating each as an output prediction instance, resulting in a total of ∼143​k{\sim}143k code–input–output examples. All solutions were generated using CWM and Qwen2.5-7B (Qwen et al., [2025](https://arxiv.org/html/2604.03253#bib.bib22 "Qwen2.5 technical report")).
164	
165	![Image 3: Refer to caption](https://arxiv.org/html/2604.03253v1/x3.png)
166	
167	Figure 3: CruxEval-O performance compared to model active parameters. Arrows demonstrate the benefit from training on NLEX data. We also compare to open models. 
168	
169	#### 5.1.2 Evaluation datasets
170	
171	We present evaluation datasets for competitive programming questions (first two), and output prediction (last two).
172	
173	LCB-IO. We curate a subset from LiveCodeBench-v6(Jain et al., [2024](https://arxiv.org/html/2604.03253#bib.bib38 "Livecodebench: holistic and contamination free evaluation of large language models for code")) containing only problems evaluated via stdio tests, which we refer to as LCB-IO. This restriction simplifies output prediction, as the task reduces to determining the content written to stdout given a specific stdin. The resulting set includes 287 287 problems.
174	
175	DMC. We follow Gehring et al. ([2025](https://arxiv.org/html/2604.03253#bib.bib8 "RLEF: grounding code LLMs in execution feedback with reinforcement learning")) and use the validation and test splits of CodeContests(Li et al., [2022](https://arxiv.org/html/2604.03253#bib.bib20 "Competition-level code generation with alphacode")), yielding an additional evaluation set with a different distribution, denoted DMC, and consisting of 282 282 problems.
176	
177	CruxEval-O(Gu et al., [2024b](https://arxiv.org/html/2604.03253#bib.bib6 "CRUXEval: a benchmark for code reasoning, understanding and execution")) is a widely adopted benchmark consisting of short Python functions paired with input–output examples. The task requires the model to infer the function’s return value given the code and its input.
178	
179	Output prediction for competitive programming. We generate 20 20 solutions per-question from both DMC and LCB-IO using the same LLMs as mentioned above, without filtering or de-duplicating solutions, to perfectly match the real distribution of generated solutions. Such data is also used for best@k type metric calculations.
180	
181	### 5.2 Trained Models
182	
183	We post-train Qwen2.5-Base models of sizes 3 3 B and 7 7 B, together with CWM-base using the datasets described in[Section 5.1.1](https://arxiv.org/html/2604.03253#S5.SS1.SSS1 "5.1.1 Training datasets ‣ 5.1 Datasets ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models"). For RL we use an asynchronous RL infrastructure, adopting the same RL algorithm as in CWM, with different hyperparameters. When performing multi-task training we employ sample-level weighting. Furthermore, we apply reward scaling, following Ruan et al. ([2025](https://arxiv.org/html/2604.03253#bib.bib27 "Critique-coder: enhancing coder models by critique reinforcement learning")), assigning a weight of 0.8 0.8 to the output prediction objective. For all multi-turn repair environments, including self-RLEF, we allow a maximum of one repair attempt during training (two solution turns in total, including the initial attempt), and 9 9 at inference (overall 10 10 turns). Full training configurations, including hyperparameters, are provided in Appendix[A.3](https://arxiv.org/html/2604.03253#A1.SS3 "A.3 Hyper-Parameters ‣ A.2 Self-RLEF Example Inference ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models").
184	
185	![Image 4: Refer to caption](https://arxiv.org/html/2604.03253v1/x4.png)
186	
187	Figure 4: Best@k performance of _self-verification_ with _self-simulation_. Solutions and output predictions are produced by the same model - based on Qwen2.5-7B or CWM, trained for both solving and output prediction. Even though the tests used for filtering are in the solve prompt, there is still room for notable gains from simulating them.
188	
189	Table 1: Output prediction performance of Qwen models trained with RLVR for output prediction, with and without NLEX data.
190	
191	## 6 Results
192	
193	### 6.1 Output Prediction
194	
195	CruxEval-O. We start by evaluating performance considering CruxEval-O. Results are presented in[Figure 3](https://arxiv.org/html/2604.03253#S5.F3 "In 5.1.1 Training datasets ‣ 5.1 Datasets ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models"). We evaluate both Qwen2.5-3B and Qwen2.5-7B (after SFT only), trained with and without the NLEX data. For reference we provide pass@1 scores of common open-weights LLMs. Results show a clear superiority of the NLEX data as part of the training mix, achieving comparable performance to significantly larger models, with Qwen2.5-3B increasing from 37.5 37.5 to 68.0 68.0 and Qwen2.5-7B improving 48.5 48.5 to 75.5 75.5 pass@1 scores. We provide results for standard coding metrics in Appendix[A.1](https://arxiv.org/html/2604.03253#A1.SS1 "A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models"), showing no regression in performance considering other benchmarks and tasks.
196	
197	Competitive programming. Next, we evaluate output prediction performance on LLM solutions to competitive programming questions from LCB-IO and DMC (test split). Compared to CruxEval-O, these functions are often more complex and challenging. For that, we consider post-trained Qwen2.5 models (3B and 7B) on the task of output-prediction. Similarly to before, we consider models trained with and without NLEX data as part of the mix. Results presented in Table [1](https://arxiv.org/html/2604.03253#S5.T1 "Table 1 ‣ 5.2 Trained Models ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models") suggest that including NLEX data as part of the mix boosts output-prediction capabilities also after RL. While RL on output prediction with a standard reasoning SFT data (i.e., OMR and OCR) shows impressive performance, mixing them with NLEX provides superior results across both model sizes. To understand the effect of the RL phase, we additionally evaluate CWM on output prediction with and without RL. As expected, the RL phase significantly improves results on output prediction, see Appendix [A.1.2](https://arxiv.org/html/2604.03253#A1.SS1.SSS2 "A.1.2 The effect of RL on output prediction ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models") and Table [8](https://arxiv.org/html/2604.03253#A1.T8 "Table 8 ‣ A.1.2 The effect of RL on output prediction ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models") for more details.
198	
199	Self-execution prediction. So far we evaluated output-prediction capabilities on code generated by external models. We now turn to evaluate _self-execution_, i.e. models perform output-prediction on their own generated solutions. For that we post-train CWM and Qwen2.5-7B on both output prediction and competitive problems solving. We report results for questions derived from both LCB-IO and DMC in Table [2](https://arxiv.org/html/2604.03253#S6.T2 "Table 2 ‣ 6.1 Output Prediction ‣ 6 Results ‣ Self-Execution Simulation Improves Coding Models") and compare performance to models trained to perform output-prediction only (as a topline) and to the official CWM model (as a baseline). As expected, results suggest that jointly training both models for solving competitive programming questions and output prediction perform worse than output prediction only. For instance, CWM reaches 80.2 80.2 and 86.5 86.5 pass@1 scores in joint training compared to 85.0 85.0 and 88.6 88.6 scores when trained for output prediction only. However, both are significantly superior to the official CWM model, that reaches 57.7 57.7 pass@1. Interestingly, these results suggest that unlike previous findings(Gu et al., [2024a](https://arxiv.org/html/2604.03253#bib.bib14 "The counterfeit conundrum: can code language models grasp the nuances of their incorrect generations?")) models can reliably perform self-execution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42fa6b90-8922-4893-92b9-45a0355879d1",
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "11d8254b-530c-4558-9273-7ad69f662056",
  "sourceToolAssistantUUID": "42fa6b90-8922-4893-92b9-45a0355879d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-11T22:49:51.183Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01B816mnqZUUwywg5ujxV1Kj`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.03253",
  "prompt": "Search the entire page for any mention of: code release, GitHub, data availability, released models, open source, reproducibility, supplementary materials, code repository, Hugging Face, dataset release. Also extract the key methodology details: how they use execution traces for RANKING/VERIFICATION vs GENERATION, what 'self-verification over multiple candidate solutions' means specifically, and any limitations they discuss."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11d8254b-530c-4558-9273-7ad69f662056",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbfH9qtJGshu8VTcMoq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79b6f07c-10b9-42b4-a913-2f91e91b7549",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WySnFzHPnrQoC8Jp37kzXW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 3274,
      "cache_read_input_tokens": 12767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3274,
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

_source line 26 · 2026-05-11T22:49:53.167Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011sDEBGrSsY6UkhsN1Jdz3E`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.02647v1",
  "prompt": "Extract the key findings about how this paper uses runtime execution traces for program repair. What is their approach? How do they differ from 2505.04441? What results do they achieve? Do they discuss trace-based ranking vs generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79b6f07c-10b9-42b4-a913-2f91e91b7549",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbfH9qtJGshu8VTcMoq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "432cb0ec-6034-41e0-991e-56ab9af3d131",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WySnFzHPnrQoC8Jp37kzXW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 832,
      "cache_creation_input_tokens": 3274,
      "cache_read_input_tokens": 12767,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3274
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 832,
          "output_tokens": 462,
          "cache_read_input_tokens": 12767,
          "cache_creation_input_tokens": 3274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3274,
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

_source line 27 · 2026-05-11T22:49:57.201Z_

<details><summary>↩ Tool result · `toolu_01B816mnqZUUwywg5ujxV1Kj`</summary>

```text
# Code Release and Reproducibility Status

**No code release found.** The paper contains no mentions of GitHub repositories, Hugging Face model releases, or public code availability.

## Key Methodology Details

**Execution Traces for Ranking/Verification vs Generation:**

The researchers employ execution traces distinctly for *verification rather than generation*. During the supervised fine-tuning phase, they train models on "natural language execution traces – text explanations grounded in real program executions." However, their downstream applications focus on selection:

> "candidate solutions are simulated on public or generated tests and retained only if their predicted outputs align with the expected ones"

This filtering mechanism selects from pre-generated candidates rather than guiding generation itself.

**Self-Verification Over Multiple Candidates:**

Self-verification operates through a best-of-k approach where the model "independently samples k candidate solutions and selects the final one based on predefined criteria." Specifically, the model simulates execution of each candidate on public tests and "the candidate predicted to pass the greatest number of public tests is selected for submission."

## Acknowledged Limitations

The authors identify significant constraints:

- **Complex computations:** "estimating complex computational operations (e.g., multiplying large numbers, compute logarithms, etc.)" remains problematic
- **Scope limitation:** The approach is "currently limited to single file competitive programming questions"
- **Simulation gap:** Performance degrades compared to actual code execution, particularly in pass@1 metrics
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79b6f07c-10b9-42b4-a913-2f91e91b7549",
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "25e4acc0-8b61-49e3-86ba-b73d2b42c612",
  "sourceToolAssistantUUID": "79b6f07c-10b9-42b4-a913-2f91e91b7549",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-11T22:50:00.496Z_

<details><summary>↩ Tool result · `toolu_011sDEBGrSsY6UkhsN1Jdz3E`</summary>

```text
# Key Findings: Runtime Traces for Automated Program Repair

## TraceRepair's Approach

TraceRepair employs a three-phase methodology grounded in runtime evidence:

**Phase 1 - Diagnostic Probing:** A Probe Agent injects logging statements into buggy programs to capture execution snapshots of critical variables, creating structured runtime traces that expose actual program behavior rather than relying on static analysis alone.

**Phase 2 - Multi-Strategy Debate:** Three specialized repair agents (Defensive, Causal, Semantic) generate candidate patches while treating runtime traces as hard constraints. Agents engage in iterative critique cycles where proposals contradicted by observed execution data are challenged and refined.

**Phase 3 - Arbitration:** A Judge Agent synthesizes insights from the debate trajectory, consolidating partial corrections into coherent fixes validated against the runtime trace.

## Core Innovation

The framework transforms execution traces from passive observations into active logical filters. As the authors note, this enables agents to reason "directly from runtime evidence to identify the true root cause" rather than inferring error paths from code alone.

## Empirical Results

- **Defects4J Performance:** TraceRepair fixes 392 bugs using DeepSeek-V3.2, outperforming conversational baselines (ChatRepair: 162 fixes)
- **Cost Efficiency:** Consumes 77k tokens per bug versus ChatRepair's 467k
- **Generalization:** Demonstrates robust performance on unseen defects in Recent-Java benchmark, suggesting reasoning rather than memorization

## Trace-Based Ranking vs. Generation

The paper focuses on **trace-guided generation and validation** rather than ranking. Traces serve as consistency constraints during the debate process—patches are iteratively refined until they align with observed execution facts. The framework does not employ trace-based ranking of pre-generated candidates as a primary mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "432cb0ec-6034-41e0-991e-56ab9af3d131",
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "16474fe5-b2fd-4cc0-ba23-15cfb37e8cc9",
  "sourceToolAssistantUUID": "432cb0ec-6034-41e0-991e-56ab9af3d131",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-11T22:50:04.060Z_

Now let me read more of the Self-Execution Simulation paper to find code/data release information, and also search for any GitHub repos.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16474fe5-b2fd-4cc0-ba23-15cfb37e8cc9",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbgYeXsbF6vQdb8VA7b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eae9242f-1d5e-4279-84c4-a8d0d34770ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPuPgP3D52HKAkFUNoipcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11460,
      "cache_read_input_tokens": 16041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11460,
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

_source line 30 · 2026-05-11T22:50:08.321Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BJB3tVgqRhcoCBYXBfPA7H`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-/f7ed7f67-a87f-46e7-a409-d4d552b7568f/tool-results/toolu_01VHjNMsLt5Fz5wNryjkKuez.txt",
  "limit": 200,
  "offset": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eae9242f-1d5e-4279-84c4-a8d0d34770ad",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbgYeXsbF6vQdb8VA7b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "746bd4af-9f03-4cc9-a0d3-10728f84cbca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPuPgP3D52HKAkFUNoipcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11460,
      "cache_read_input_tokens": 16041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11460,
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

_source line 31 · 2026-05-11T22:50:08.582Z_

<details><summary>↩ Tool result · `toolu_01BJB3tVgqRhcoCBYXBfPA7H`</summary>

````text
200	Self-execution prediction. So far we evaluated output-prediction capabilities on code generated by external models. We now turn to evaluate _self-execution_, i.e. models perform output-prediction on their own generated solutions. For that we post-train CWM and Qwen2.5-7B on both output prediction and competitive problems solving. We report results for questions derived from both LCB-IO and DMC in Table [2](https://arxiv.org/html/2604.03253#S6.T2 "Table 2 ‣ 6.1 Output Prediction ‣ 6 Results ‣ Self-Execution Simulation Improves Coding Models") and compare performance to models trained to perform output-prediction only (as a topline) and to the official CWM model (as a baseline). As expected, results suggest that jointly training both models for solving competitive programming questions and output prediction perform worse than output prediction only. For instance, CWM reaches 80.2 80.2 and 86.5 86.5 pass@1 scores in joint training compared to 85.0 85.0 and 88.6 88.6 scores when trained for output prediction only. However, both are significantly superior to the official CWM model, that reaches 57.7 57.7 pass@1. Interestingly, these results suggest that unlike previous findings(Gu et al., [2024a](https://arxiv.org/html/2604.03253#bib.bib14 "The counterfeit conundrum: can code language models grasp the nuances of their incorrect generations?")) models can reliably perform self-execution.
201	
202	Table 2: Output prediction performance for models trained on standard code solving, jointly with output prediction (Joint), on their own solutions. We compare this to a model trained for output prediction only, models from Tab. [1](https://arxiv.org/html/2604.03253#S5.T1 "Table 1 ‣ 5.2 Trained Models ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models"), (Out Pred), and official CWM. 
203	
204	### 6.2 Self-Execution for Competitive Programming
205	
206	Table 3: Solve rates for training and evaluating with a standard reasoning approach vs using real or simulated execution feedback.
207	
208	##### Self-verification.
209	
210	Given a model’s prediction of the execution output of its own code on public tests, one can use this to self-verify the solutions. Specifically, following the best@k simulate approach described in [Section 3](https://arxiv.org/html/2604.03253#S3 "3 Self-Execution For Verification ‣ Self-Execution Simulation Improves Coding Models"), we select and submit the solution predicted to pass most tests. To better estimate the effectiveness of the proposed method, we compare it to short1@k(Hassid et al., [2025](https://arxiv.org/html/2604.03253#bib.bib42 "Don’t overthink it. preferring shorter thinking chains for improved llm reasoning")), which selects the shortest response among the k k solutions, and pass@k (for reference). To directly assess the quality of execution simulation, we also compare against an oracle that executes the public tests, following the same filtering procedure (denoted best@k exec). This comparison will provide us with the _simulation gap_, i.e., the performance gap between fully executing the code vs. simulating it with the model. Our results provided in Fig.[4](https://arxiv.org/html/2604.03253#S5.F4 "Figure 4 ‣ 5.2 Trained Models ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models") show that self-verification provides a large boost in performance under the best@k setup, (2−8 2-8 points compared to standard solving), _despite the tests used for filtering being provided when generating the solution_. This also outperforms short1@k. Notably, for Qwen2.5-7B the simulation gap is larger than CWM perhaps implying the need for larger or stronger models to learn to both solve and simulate execution effectively. Further results in Fig.[9](https://arxiv.org/html/2604.03253#A1.F9 "Figure 9 ‣ A.1.5 Beyond Self-Verification ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models") show that using Qwen2.5-7B trained for output prediction only to filter the same solutions leads to a smaller gap.
211	
212	##### Self-RLEF.
213	
214	We train our model using the procedure described in [Section 4](https://arxiv.org/html/2604.03253#S4 "4 Self-Execution For Fixing ‣ Self-Execution Simulation Improves Coding Models"). We report pass@k scores for k∈{1,5,10}k\in\{1,5,10\} on both LCB-IO and DMC, along with public-test pass rates. We evaluate three variants: the official CWM model, CWM post-trained specifically for competitive programming (CWM-RL), and CWM jointly optimised for output prediction and competitive programming with execution feedback. The latter is evaluated under the proposed self-RLEF framework, using either simulated execution or real execution as an oracle. In both settings, the model is allowed up to 10 10 coding turns (initial solution + 9 9 fix), although in practice, it uses 3.33 3.33 turns on average (Appendix [A.1.4](https://arxiv.org/html/2604.03253#A1.SS1.SSS4 "A.1.4 Self-RLEF ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models") provides additional results with less turns). Results in [Table 3](https://arxiv.org/html/2604.03253#S6.T3 "In 6.2 Self-Execution for Competitive Programming ‣ 6 Results ‣ Self-Execution Simulation Improves Coding Models") show that self-RLEF consistently outperforms both the official CWM and CWM-RL across all settings, improving pass rates on both public and private tests. Compared to the oracle, a performance gap remains, particularly for pass@1, indicating room for improvement in execution prediction. Interestingly, pass@1 scores (with 10 turns) are lower than the corresponding best@10 results shown in [Figure 4](https://arxiv.org/html/2604.03253#S5.F4 "In 5.2 Trained Models ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models"). We hypothesise that this gap arises from limited exploration, as the model tends to iteratively fix a solution rather than explore alternative ones. In addition, the model frequently does not use all turns as seen by the average number of turns. For certain settings where an ”early exit” is preferred this approach can provide a better tradeoff considering compute.
215	
216	### 6.3 Ablations
217	
218	Table 4: Comparing performance of using the self-RLEF scaffold at inference only with open source reasoning models. 
219	
220	Self-RLEF scaffold. One may wonder to what extent the self-refinement pipeline itself leads to the inference performance gain irrespective of model training. Hence, we investigate inference using the Self-RLEF approach with public open-weights models, specifically Qwen3-32B and CWM. We compare these results to using these models in a standard single turn inference procedure. Results provided in [Table 4](https://arxiv.org/html/2604.03253#S6.T4 "In 6.3 Ablations ‣ 6 Results ‣ Self-Execution Simulation Improves Coding Models") show no noticeable improvement from using the proposed self-RLEF approach, and even a decrease in performance across both models over all metrics and datasets. By manual analysis, we observe the model struggles to correctly predict the output, and ignores the feedback.
221	
222	![Image 5: Refer to caption](https://arxiv.org/html/2604.03253v1/x5.png)
223	
224	Figure 5: Comparing best@k when ranking Qwen3-32B solutions, using CWM post-trained only for output prediction as a verifier. 
225	
226	Knowing when to submit or fix. To better identify the source of performance gains from self-RLEF, we analyse model behaviour during inference time. We measure how often the model successfully fixes a solution, i.e., cases where the initial solution fails the tests but the final solution passes, as well as how often it breaks a solution, i.e., where an initially passing solution fails after revision. For completeness, we also report cases where both the initial and final solutions either pass or fail the tests. [Table 5](https://arxiv.org/html/2604.03253#S6.T5 "In 6.3 Ablations ‣ 6 Results ‣ Self-Execution Simulation Improves Coding Models") reports results for CWM on DMC using both public and private tests. Results suggest the model rarely degrades correct solutions, breaking only 1.2%1.2\% of cases on public tests and 5.0%5.0\% on private tests. In contrast, when the initial solution fails, the model frequently produces effective fixes, succeeding in 17.0%17.0\% of public-tests and 10.4%10.4\% of private-tests. These improvements increase the pass rate from 57.8%57.8\% for the initial solutions to 63.2%63.2\% for the final submissions.
227	
228	Table 5: Pass rates of the initial generated solution (Init), compared to the final submitted solution (Sub) in _Self-RLEF_ inference on DMC considering both public and private tests. 
229	
230	(a) Public Tests
231	
232	(b) Private Tests
233	
234	### 6.4 Beyond _Self_-Verification
235	
236	While the focus of this work is _self_-execution, one could imagine use cases for building a model as a code simulator only. As an initial analysis, we measure public test pass rates for multiple models on LCB-IO and DMC to assess the potential of the best@k approach. [Table 6](https://arxiv.org/html/2604.03253#S6.T6 "In 6.4 Beyond Self-Verification ‣ 6 Results ‣ Self-Execution Simulation Improves Coding Models") reports public pass@1 and pass@10 results for Qwen and CWM. While models can generate solutions which pass the public tests (as evidenced in pass@10), they often submit solutions which do not pass them _even though they are provided in the question_. This suggests that standard reasoning approaches under-utilise such test information. This observation motivates the use of solution verification.
237	
238	We next assess the ability of our trained CWM model to predict execution outputs for solutions generated by Qwen3-32B. CWM achieves pass@1 and pass@5 scores of 86.1 86.1 and 91.4 91.4, respectively, on public test output prediction. Based on this, we apply the best@k evaluation on both LCB-IO and DMC, as shown in [Figure 5](https://arxiv.org/html/2604.03253#S6.F5 "In 6.3 Ablations ‣ 6 Results ‣ Self-Execution Simulation Improves Coding Models"). The results indicate that using CWM with this filtering strategy is very effective and can correctly filter solutions generated by external models. Furthermore, compared to real execution, we observe only a minor _simulation gap_. This again highlights the efficacy of the output prediction method to alleviate the need for execution, and further shows generalisation to other models’ solutions. Results for this setup using Qwen3-4B and CWM-RL are provided in Appendix [A.1](https://arxiv.org/html/2604.03253#A1.SS1 "A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models"), showing similar trends.
239	
240	Table 6: Public pass@1 and 10 of different models. The large gap of standard reasoning models can suggest that they under-utilise provided test information.
241	
242	## 7 Related Work
243	
244	##### Code Simulation & Verification.
245	
246	Several works ask how well LLMs can simulate or predict the output of a given code snippet (Hora, [2024](https://arxiv.org/html/2604.03253#bib.bib63 "Predicting test results without execution"); Li et al., [2025](https://arxiv.org/html/2604.03253#bib.bib62 "CodeIO: condensing reasoning patterns via code input-output prediction"); Gu et al., [2024b](https://arxiv.org/html/2604.03253#bib.bib6 "CRUXEval: a benchmark for code reasoning, understanding and execution"); Xu et al., [2025](https://arxiv.org/html/2604.03253#bib.bib12 "CRUXEVAL-X: a benchmark for multilingual code reasoning, understanding and execution"); Copet et al., [2025](https://arxiv.org/html/2604.03253#bib.bib25 "Cwm: an open-weights llm for research on code generation with world models"); Armengol-Estapé et al., [2025](https://arxiv.org/html/2604.03253#bib.bib7 "What i cannot execute, i do not understand: training and evaluating llms on program execution traces")). Others suggest that models struggle to simulate their own code, as they are blind to its flaws (Gu et al., [2024a](https://arxiv.org/html/2604.03253#bib.bib14 "The counterfeit conundrum: can code language models grasp the nuances of their incorrect generations?")). Some works use models to simulate tool execution as part of a synthetic data generation (Kimi et al., [2025](https://arxiv.org/html/2604.03253#bib.bib68 "Kimi k2: open agentic intelligence")). Furthermore, some studies explicitly train a model as a verifier of solutions (Le et al., [2022](https://arxiv.org/html/2604.03253#bib.bib58 "Coderl: mastering code generation through pretrained models and deep reinforcement learning")). Many report challenges in verification performance (Ruan et al., [2025](https://arxiv.org/html/2604.03253#bib.bib27 "Critique-coder: enhancing coder models by critique reinforcement learning"); Wang et al., [2025](https://arxiv.org/html/2604.03253#bib.bib26 "Critique fine-tuning: learning to critique is more effective than learning to imitate")).
247	
248	##### Learning from Feedback.
249	
250	Gehring et al. ([2025](https://arxiv.org/html/2604.03253#bib.bib8 "RLEF: grounding code LLMs in execution feedback with reinforcement learning")) showed that models can learn to utilise feedback about the execution of their generated code. Providing models with access to interpreters is a popular approach that has been used to improve performance in maths (Chen et al., [2023b](https://arxiv.org/html/2604.03253#bib.bib2 "Program of thoughts prompting: disentangling computation from reasoning for numerical reasoning tasks"); Gao et al., [2023](https://arxiv.org/html/2604.03253#bib.bib4 "PAL: program-aided language models")), code generation (Liu et al., [2023b](https://arxiv.org/html/2604.03253#bib.bib5 "Dynamic llm-agent network: an llm-agent collaboration framework with agent team optimization"); Shinn et al., [2023](https://arxiv.org/html/2604.03253#bib.bib1 "Reflexion: language agents with verbal reinforcement learning")), competitive programming (Zheng et al., [2025](https://arxiv.org/html/2604.03253#bib.bib3 "What makes large language models reason in (multi-turn) code generation?")), and agentic coding (Yang et al., [2024](https://arxiv.org/html/2604.03253#bib.bib10 "Swe-agent: agent-computer interfaces enable automated software engineering"); Xia et al., [2025](https://arxiv.org/html/2604.03253#bib.bib57 "Live-swe-agent: can software engineering agents self-evolve on the fly?")). Several prompting approaches were suggested for non-reasoning models to elicit self-improvement, often joint with external verification signals (Chen et al., [2023c](https://arxiv.org/html/2604.03253#bib.bib48 "Teaching large language models to self-debug"); Renze and Guven, [2024](https://arxiv.org/html/2604.03253#bib.bib49 "Self-reflection in llm agents: effects on problem-solving performance"); Madaan et al., [2023](https://arxiv.org/html/2604.03253#bib.bib50 "Self-refine: iterative refinement with self-feedback"); Kumar et al., [2024](https://arxiv.org/html/2604.03253#bib.bib59 "Training language models to self-correct via reinforcement learning")). Chen et al. ([2023a](https://arxiv.org/html/2604.03253#bib.bib47 "Improving code generation by training with natural language feedback")) further showed that training with human written feedback on code can improve performance.
251	
252	## 8 Discussion
253	
254	Limitations. The main limitation of simulating program execution is estimating complex computational operations (e.g., multiplying large numbers, compute logarithms, etc.). Yet, while execution simulation is imperfect and can introduce noise, our findings suggest that it provides a useful inductive bias for reasoning about program behaviour, particularly in settings where direct execution is expensive or infeasible. Furthermore, while our approach showed promising results, it is currently limited to single file competitive programming questions. Generalising this to full repository SWE tasks poses an interesting future research direction.
255	
256	Future Work. We believe our work opens several directions for future research. The most interesting direction in our opinion is using the full rich execution simulation, and not only the final output as feedback for iterative code fixing. Such feedback can convey richer information than the output alone (_even beyond real execution_), capturing not just what output is produced, but why it arises. Such explanations can reveal cases where a test appears to pass for incidental reasons, as well as provide insight into the underlying causes of failures. In preliminary results we observe that training with rich textual feedback presents challenges to training stability. We hypothesise this is due to both inability to train with teacher forcing and unclear definition of the verifiable reward of the simulation. We leave such exploration for future work.
257	
258	## 9 Conclusion
259	
260	In this work we investigated if LLMs can be trained to simulate code execution and whether this capability can be used to improve code generation. By combining SFT on NLEX with RLVR, we showed that models can acquire the ability to predict execution outcomes for general programs as well as code they generate. Leveraging this ability, we introduced _self-verification_ and iterative _self-fix_ strategies using predicted execution signals to select or refine candidate solutions without relying on external execution. Our empirical results on competitive programming tasks demonstrate consistent improvements over standard baselines considering both output prediction and question solving. Compared with real execution we show a relatively small _simulation gap_, demonstrating the usability of the proposed approach compared to the top-line of code execution. More broadly, our results suggest that enabling models to reason about the outcomes of the code they generate may be a key for building more reliable programming agents.
261	
262	## Impact Statement
263	
264	This paper presents work whose goal is to advance the field of Machine Learning. There are many potential societal consequences of our work, none which we feel must be specifically highlighted here.
265	
266	## References
267	
268	*   W. U. Ahmad, S. Narenthiran, S. Majumdar, A. Ficek, S. Jain, J. Huang, V. Noroozi, and B. Ginsburg (2025)Opencodereasoning: advancing data distillation for competitive coding. arXiv preprint arXiv:2504.01943. Cited by: [§5.1.1](https://arxiv.org/html/2604.03253#S5.SS1.SSS1.p1.1 "5.1.1 Training datasets ‣ 5.1 Datasets ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models"). 
269	*   J. Armengol-Estapé, Q. Carbonneaux, T. Zhang, A. H. Markosyan, V. Seeker, C. Cummins, M. Kambadur, M. F. O’Boyle, S. Wang, G. Synnaeve, et al. (2025)What i cannot execute, i do not understand: training and evaluating llms on program execution traces. arXiv preprint arXiv:2503.05703. Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p1.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"), [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px1.p1.1 "Code Simulation & Verification. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
270	*   J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan, E. Jiang, C. Cai, M. Terry, Q. Le, et al. (2021)Program synthesis with large language models. Note: arXiv:2108.07732 External Links: [Link](https://arxiv.org/abs/2108.07732)Cited by: [§A.1.1](https://arxiv.org/html/2604.03253#A1.SS1.SSS1.p1.1 "A.1.1 Supervised fine-tuning. ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models"). 
271	*   M. Beck, J. Gehring, J. Kossen, and G. Synnaeve (2026)Towards a neural debugger for python. External Links: 2603.09951, [Link](https://arxiv.org/abs/2603.09951)Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p1.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"). 
272	*   S. Bengio, O. Vinyals, N. Jaitly, and N. Shazeer (2015)Scheduled sampling for sequence prediction with recurrent neural networks. Advances in neural information processing systems 28. Cited by: [§4](https://arxiv.org/html/2604.03253#S4.p5.1 "4 Self-Execution For Fixing ‣ Self-Execution Simulation Improves Coding Models"). 
273	*   B. Bogin, K. Yang, S. Gupta, K. Richardson, E. Bransom, P. Clark, A. Sabharwal, and T. Khot (2024)Super: evaluating agents on setting up and executing tasks from research repositories. arXiv preprint arXiv:2409.07440. Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p2.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"). 
274	*   J. S. Chan, N. Chowdhury, O. Jaffe, J. Aung, D. Sherburn, E. Mays, G. Starace, K. Liu, L. Maksin, T. Patwardhan, et al. (2024)Mle-bench: evaluating machine learning agents on machine learning engineering. arXiv preprint arXiv:2410.07095. Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p2.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"). 
275	*   A. Chen, J. Scheurer, T. Korbak, J. A. Campos, J. S. Chan, S. R. Bowman, K. Cho, and E. Perez (2023a)Improving code generation by training with natural language feedback. arXiv preprint arXiv:2303.16749. Cited by: [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px2.p1.1 "Learning from Feedback. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
276	*   W. Chen, X. Ma, X. Wang, and W. W. Cohen (2023b)Program of thoughts prompting: disentangling computation from reasoning for numerical reasoning tasks. Transactions on Machine Learning Research. Note: External Links: ISSN 2835-8856, [Link](https://openreview.net/forum?id=YfZ4ZPt8zd)Cited by: [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px2.p1.1 "Learning from Feedback. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
277	*   X. Chen, M. Lin, N. Schärli, and D. Zhou (2023c)Teaching large language models to self-debug. arXiv preprint arXiv:2304.05128. Cited by: [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px2.p1.1 "Learning from Feedback. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
278	*   K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, C. Hesse, and J. Schulman (2021)Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168. Cited by: [§A.1.1](https://arxiv.org/html/2604.03253#A1.SS1.SSS1.p1.1 "A.1.1 Supervised fine-tuning. ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models"). 
279	*   J. Copet, Q. Carbonneaux, G. Cohen, J. Gehring, J. Kahn, J. Kossen, F. Kreuk, E. McMilin, M. Meyer, Y. Wei, et al. (2025)Cwm: an open-weights llm for research on code generation with world models. arXiv preprint arXiv:2510.02387. Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p1.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"), [§2.1](https://arxiv.org/html/2604.03253#S2.SS1.p1.4 "2.1 Natural Language Execution Tracing (NLEX) ‣ 2 Boosting Execution Simulation ‣ Self-Execution Simulation Improves Coding Models"), [§2.1](https://arxiv.org/html/2604.03253#S2.SS1.p2.1 "2.1 Natural Language Execution Tracing (NLEX) ‣ 2 Boosting Execution Simulation ‣ Self-Execution Simulation Improves Coding Models"), [§2](https://arxiv.org/html/2604.03253#S2.p1.1 "2 Boosting Execution Simulation ‣ Self-Execution Simulation Improves Coding Models"), [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px1.p1.1 "Code Simulation & Verification. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
280	*   J. Ding, Y. Zhang, Y. Shang, Y. Zhang, Z. Zong, J. Feng, Y. Yuan, H. Su, N. Li, N. Sukiennik, et al. (2025)Understanding world or predicting future? a comprehensive survey of world models. ACM Computing Surveys 58 (3),  pp.1–38. Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p2.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"). 
281	*   L. Gao, A. Madaan, S. Zhou, U. Alon, P. Liu, Y. Yang, J. Callan, and G. Neubig (2023)PAL: program-aided language models. In Proceedings of the 40th International Conference on Machine LearningProceedings of the 41st International Conference on Machine LearningForty-second International Conference on Machine Learning2025 IEEE/ACM Second International Conference on AI Foundation Models and Software Engineering (Forge)The Twelfth International Conference on Learning RepresentationsProceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE)Findings of the Association for Computational Linguistics ACL 2024Findings of the Association for Computational Linguistics: EMNLP 2024The eleventh international conference on learning representationsThirty-seventh Conference on Neural Information Processing SystemsForty-second International Conference on Machine LearningCompanion Proceedings of the 32nd ACM International Conference on the Foundations of Software Engineering, A. Krause, E. Brunskill, K. Cho, B. Engelhardt, S. Sabato, J. Scarlett, R. Salakhutdinov, Z. Kolter, K. Heller, A. Weller, N. Oliver, J. Scarlett, F. Berkenkamp, W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.), Proceedings of Machine Learning ResearchProceedings of Machine Learning Research, Vol. 202235,  pp.10764–10799. External Links: [Link](https://proceedings.mlr.press/v202/gao23f.html)Cited by: [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px2.p1.1 "Learning from Feedback. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
282	*   J. Gehring, K. Zheng, J. Copet, V. Mella, T. Cohen, and G. Synnaeve (2025)RLEF: grounding code LLMs in execution feedback with reinforcement learning. External Links: [Link](https://openreview.net/forum?id=PzSG5nKe1q)Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p2.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"), [§1](https://arxiv.org/html/2604.03253#S1.p3.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"), [§4](https://arxiv.org/html/2604.03253#S4.p1.1 "4 Self-Execution For Fixing ‣ Self-Execution Simulation Improves Coding Models"), [§5.1.2](https://arxiv.org/html/2604.03253#S5.SS1.SSS2.p3.1 "5.1.2 Evaluation datasets ‣ 5.1 Datasets ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models"), [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px2.p1.1 "Learning from Feedback. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
283	*   A. Grattafiori, A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman, A. Mathur, A. Schelten, A. Vaughan, et al. (2024)The llama 3 herd of models. arXiv preprint arXiv:2407.21783. Cited by: [§2.1](https://arxiv.org/html/2604.03253#S2.SS1.p1.4 "2.1 Natural Language Execution Tracing (NLEX) ‣ 2 Boosting Execution Simulation ‣ Self-Execution Simulation Improves Coding Models"). 
284	*   A. Gu, W. Li, N. Jain, T. Olausson, C. Lee, K. Sen, and A. Solar-Lezama (2024a)The counterfeit conundrum: can code language models grasp the nuances of their incorrect generations?.  pp.74–117. Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p1.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"), [§6.1](https://arxiv.org/html/2604.03253#S6.SS1.p3.5 "6.1 Output Prediction ‣ 6 Results ‣ Self-Execution Simulation Improves Coding Models"), [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px1.p1.1 "Code Simulation & Verification. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
285	*   A. Gu, B. Roziere, H. J. Leather, A. Solar-Lezama, G. Synnaeve, and S. Wang (2024b)CRUXEval: a benchmark for code reasoning, understanding and execution.  pp.16568–16621. External Links: [Link](https://proceedings.mlr.press/v235/gu24c.html)Cited by: [§A.1.1](https://arxiv.org/html/2604.03253#A1.SS1.SSS1.p1.1 "A.1.1 Supervised fine-tuning. ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models"), [§1](https://arxiv.org/html/2604.03253#S1.p4.3 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"), [§5.1.2](https://arxiv.org/html/2604.03253#S5.SS1.SSS2.p4.1 "5.1.2 Evaluation datasets ‣ 5.1 Datasets ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models"), [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px1.p1.1 "Code Simulation & Verification. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
286	*   D. Ha and J. Schmidhuber (2018)World models. arXiv preprint arXiv:1803.10122 2 (3). Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p2.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"). 
287	*   M. Hassid, T. Remez, J. Gehring, R. Schwartz, and Y. Adi (2024)The larger the better? improved llm code-generation via budget reallocation. arXiv preprint arXiv:2404.00725. Cited by: [§3](https://arxiv.org/html/2604.03253#S3.p5.3 "3 Self-Execution For Verification ‣ Self-Execution Simulation Improves Coding Models"). 
288	*   M. Hassid, G. Synnaeve, Y. Adi, and R. Schwartz (2025)Don’t overthink it. preferring shorter thinking chains for improved llm reasoning. arXiv preprint arXiv:2505.17813. Cited by: [§6.2](https://arxiv.org/html/2604.03253#S6.SS2.SSS0.Px1.p1.2 "Self-verification. ‣ 6.2 Self-Execution for Competitive Programming ‣ 6 Results ‣ Self-Execution Simulation Improves Coding Models"). 
289	*   A. Hora (2024)Predicting test results without execution.  pp.542–546. Cited by: [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px1.p1.1 "Code Simulation & Verification. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
290	*   N. Jain, K. Han, A. Gu, W. Li, F. Yan, T. Zhang, S. Wang, A. Solar-Lezama, K. Sen, and I. Stoica (2024)Livecodebench: holistic and contamination free evaluation of large language models for code. arXiv preprint arXiv:2403.07974. Cited by: [§A.1.1](https://arxiv.org/html/2604.03253#A1.SS1.SSS1.p1.1 "A.1.1 Supervised fine-tuning. ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models"), [§1](https://arxiv.org/html/2604.03253#S1.p4.3 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"), [§5.1.2](https://arxiv.org/html/2604.03253#S5.SS1.SSS2.p2.1 "5.1.2 Evaluation datasets ‣ 5.1 Datasets ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models"). 
291	*   C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, and K. Narasimhan (2023)Swe-bench: can language models resolve real-world github issues?. arXiv preprint arXiv:2310.06770. Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p2.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"). 
292	*   R. Kamoi, Y. Zhang, N. Zhang, J. Han, and R. Zhang (2024)When can llms actually correct their own mistakes? a critical survey of self-correction of llms. Transactions of the Association for Computational Linguistics 12,  pp.1417–1440. Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p1.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"). 
293	*   T. Kimi, Y. Bai, Y. Bao, G. Chen, J. Chen, N. Chen, R. Chen, Y. Chen, Y. Chen, Y. Chen, et al. (2025)Kimi k2: open agentic intelligence. arXiv preprint arXiv:2507.20534. Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p2.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"), [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px1.p1.1 "Code Simulation & Verification. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
294	*   A. Kumar, V. Zhuang, R. Agarwal, Y. Su, J. D. Co-Reyes, A. Singh, K. Baumli, S. Iqbal, C. Bishop, R. Roelofs, et al. (2024)Training language models to self-correct via reinforcement learning. arXiv preprint arXiv:2409.12917. Cited by: [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px2.p1.1 "Learning from Feedback. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
295	*   H. Le, Y. Wang, A. D. Gotmare, S. Savarese, and S. C. H. Hoi (2022)Coderl: mastering code generation through pretrained models and deep reinforcement learning. Advances in Neural Information Processing Systems 35,  pp.21314–21328. Cited by: [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px1.p1.1 "Code Simulation & Verification. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
296	*   J. Li, D. Guo, D. Yang, R. Xu, Y. Wu, and J. He (2025)CodeIO: condensing reasoning patterns via code input-output prediction. External Links: [Link](https://openreview.net/forum?id=feIaF6vYFl)Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p1.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"), [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px1.p1.1 "Code Simulation & Verification. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
297	*   Y. Li, D. Choi, J. Chung, N. Kushman, J. Schrittwieser, R. Leblond, T. Eccles, J. Keeling, F. Gimeno, A. Dal Lago, et al. (2022)Competition-level code generation with alphacode. Science 378 (6624),  pp.1092–1097. Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p4.3 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"), [§2.1](https://arxiv.org/html/2604.03253#S2.SS1.p1.4 "2.1 Natural Language Execution Tracing (NLEX) ‣ 2 Boosting Execution Simulation ‣ Self-Execution Simulation Improves Coding Models"), [§5.1.1](https://arxiv.org/html/2604.03253#S5.SS1.SSS1.p2.3 "5.1.1 Training datasets ‣ 5.1 Datasets ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models"), [§5.1.2](https://arxiv.org/html/2604.03253#S5.SS1.SSS2.p3.1 "5.1.2 Evaluation datasets ‣ 5.1 Datasets ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models"). 
298	*   H. Lightman, V. Kosaraju, Y. Burda, H. Edwards, B. Baker, T. Lee, J. Leike, J. Schulman, I. Sutskever, and K. Cobbe (2023)Let’s verify step by step. arXiv preprint arXiv:2305.20050. Cited by: [§A.1.1](https://arxiv.org/html/2604.03253#A1.SS1.SSS1.p1.1 "A.1.1 Supervised fine-tuning. ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models"). 
299	*   J. Liu, C. S. Xia, Y. Wang, and L. Zhang (2023a)Is your code generated by chatGPT really correct? rigorous evaluation of large language models for code generation. External Links: [Link](https://openreview.net/forum?id=1qvx610Cu7)Cited by: [§A.1.1](https://arxiv.org/html/2604.03253#A1.SS1.SSS1.p1.1 "A.1.1 Supervised fine-tuning. ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models"). 
300	*   Z. Liu, Y. Zhang, P. Li, Y. Liu, and D. Yang (2023b)Dynamic llm-agent network: an llm-agent collaboration framework with agent team optimization. External Links: 2310.02170 Cited by: [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px2.p1.1 "Learning from Feedback. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
301	*   A. Madaan, N. Tandon, P. Gupta, S. Hallinan, L. Gao, S. Wiegreffe, U. Alon, N. Dziri, S. Prabhumoye, Y. Yang, et al. (2023)Self-refine: iterative refinement with self-feedback. Advances in Neural Information Processing Systems 36,  pp.46534–46594. Cited by: [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px2.p1.1 "Learning from Feedback. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
302	*   MiniMax (2026)M2.1: multilingual and multi-task coding with strong generalization. Note: [https://x.com/MiniMax__AI/status/2007843119832695114](https://x.com/MiniMax__AI/status/2007843119832695114)Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p2.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"). 
303	*   I. Moshkov, D. Hanley, I. Sorokin, S. Toshniwal, C. Henkel, B. Schifferer, W. Du, and I. Gitman (2025)Aimo-2 winning solution: building state-of-the-art mathematical reasoning models with openmathreasoning dataset. arXiv preprint arXiv:2504.16891. Cited by: [§5.1.1](https://arxiv.org/html/2604.03253#S5.SS1.SSS1.p1.1 "5.1.1 Training datasets ‣ 5.1 Datasets ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models"). 
304	*   T. X. Olausson, J. P. Inala, C. Wang, J. Gao, and A. Solar-Lezama (2024)Is self-repair a silver bullet for code generation?. External Links: [Link](https://openreview.net/forum?id=y0GJXRungR)Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p1.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"). 
305	*   Y. Peng, A. D. Gotmare, M. R. Lyu, C. Xiong, S. Savarese, and D. Sahoo (2025)PerfCodeGen: improving performance of llm generated code with execution feedback.  pp.1–13. External Links: [Document](https://dx.doi.org/10.1109/Forge66646.2025.00008)Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p2.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"). 
306	*   C. Qian, E. C. Acikgoz, B. Li, X. Chen, Y. Zhang, B. He, Q. Luo, D. Hakkani-Tür, G. Tur, Y. Li, et al. (2026)Current agents fail to leverage world model as tool for foresight. arXiv preprint arXiv:2601.03905. Cited by: [§4](https://arxiv.org/html/2604.03253#S4.p2.1 "4 Self-Execution For Fixing ‣ Self-Execution Simulation Improves Coding Models"). 
307	*   Qwen, :, A. Yang, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Li, D. Liu, F. Huang, H. Wei, H. Lin, J. Yang, J. Tu, J. Zhang, J. Yang, J. Yang, J. Zhou, J. Lin, K. Dang, K. Lu, K. Bao, K. Yang, L. Yu, M. Li, M. Xue, P. Zhang, Q. Zhu, R. Men, R. Lin, T. Li, T. Tang, T. Xia, X. Ren, X. Ren, Y. Fan, Y. Su, Y. Zhang, Y. Wan, Y. Liu, Z. Cui, Z. Zhang, and Z. Qiu (2025)Qwen2.5 technical report. External Links: 2412.15115, [Link](https://arxiv.org/abs/2412.15115)Cited by: [§5.1.1](https://arxiv.org/html/2604.03253#S5.SS1.SSS1.p2.3 "5.1.1 Training datasets ‣ 5.1 Datasets ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models"). 
308	*   M. Renze and E. Guven (2024)Self-reflection in llm agents: effects on problem-solving performance. arXiv preprint arXiv:2405.06682. Cited by: [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px2.p1.1 "Learning from Feedback. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
309	*   C. Ruan, D. Jiang, Y. Wang, and W. Chen (2025)Critique-coder: enhancing coder models by critique reinforcement learning. arXiv preprint arXiv:2509.22824. Cited by: [§5.2](https://arxiv.org/html/2604.03253#S5.SS2.p1.5 "5.2 Trained Models ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models"), [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px1.p1.1 "Code Simulation & Verification. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
310	*   N. Shinn, F. Cassano, A. Gopinath, K. R. Narasimhan, and S. Yao (2023)Reflexion: language agents with verbal reinforcement learning. In Thirty-seventh Conference on Neural Information Processing Systems, External Links: [Link](https://openreview.net/forum?id=vAElhFcKW6)Cited by: [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px2.p1.1 "Learning from Feedback. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
311	*   J. Su, M. Ahmed, Y. Lu, S. Pan, W. Bo, and Y. Liu (2024)Roformer: enhanced transformer with rotary position embedding. Neurocomputing 568,  pp.127063. Cited by: [§A.3](https://arxiv.org/html/2604.03253#A1.SS3.SSS0.Px1.p1.10 "Supervised Fine-Tuning. ‣ A.3 Hyper-Parameters ‣ A.2 Self-RLEF Example Inference ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models"). 
312	*   A. Thimmaiah, J. Zhang, J. Srinivasa, J. J. Li, and M. Gligoric (2025)PLSemanticsBench: large language models as programming language interpreters. arXiv preprint arXiv:2510.03415. Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p1.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"). 
313	*   Y. Wang, X. Yue, and W. Chen (2025)Critique fine-tuning: learning to critique is more effective than learning to imitate. arXiv preprint arXiv:2501.17703. Cited by: [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px1.p1.1 "Code Simulation & Verification. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
314	*   C. S. Xia, Z. Wang, Y. Yang, Y. Wei, and L. Zhang (2025)Live-swe-agent: can software engineering agents self-evolve on the fly?. arXiv preprint arXiv:2511.13646. Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p2.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"), [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px2.p1.1 "Learning from Feedback. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
315	*   R. Xu, J. Cao, Y. Lu, M. Wen, H. Lin, X. Han, B. He, S. Cheung, and L. Sun (2025)CRUXEVAL-X: a benchmark for multilingual code reasoning, understanding and execution. Vienna, Austria,  pp.23762–23779. External Links: [Link](https://aclanthology.org/2025.acl-long.1158/), [Document](https://dx.doi.org/10.18653/v1/2025.acl-long.1158), ISBN 979-8-89176-251-0 Cited by: [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px1.p1.1 "Code Simulation & Verification. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
316	*   A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, et al. (2025)Qwen3 technical report. arXiv preprint arXiv:2505.09388. Cited by: [§2.1](https://arxiv.org/html/2604.03253#S2.SS1.p3.2 "2.1 Natural Language Execution Tracing (NLEX) ‣ 2 Boosting Execution Simulation ‣ Self-Execution Simulation Improves Coding Models"). 
317	*   J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, and O. Press (2024)Swe-agent: agent-computer interfaces enable automated software engineering. Advances in Neural Information Processing Systems 37,  pp.50528–50652. Cited by: [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px2.p1.1 "Learning from Feedback. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
318	*   S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. R. Narasimhan, and Y. Cao (2022)React: synergizing reasoning and acting in language models. Cited by: [§4](https://arxiv.org/html/2604.03253#S4.p3.1 "4 Self-Execution For Fixing ‣ Self-Execution Simulation Improves Coding Models"). 
319	*   J. Zheng, J. Zhang, Y. Luo, Y. Mao, Y. Gao, L. Du, H. Chen, and N. Zhang (2026)Can we predict before executing machine learning agents?. arXiv preprint arXiv:2601.05930. Cited by: [§1](https://arxiv.org/html/2604.03253#S1.p2.1 "1 Introduction ‣ Self-Execution Simulation Improves Coding Models"). 
320	*   K. Zheng, J. Decugis, J. Gehring, T. Cohen, benjamin negrevergne, and G. Synnaeve (2025)What makes large language models reason in (multi-turn) code generation?. In The Thirteenth International Conference on Learning Representations, External Links: [Link](https://openreview.net/forum?id=Zk9guOl9NS)Cited by: [§7](https://arxiv.org/html/2604.03253#S7.SS0.SSS0.Px2.p1.1 "Learning from Feedback. ‣ 7 Related Work ‣ Self-Execution Simulation Improves Coding Models"). 
321	
322	## Appendix A Appendix.
323	
324	### A.1 Additional Results
325	
326	#### A.1.1 Supervised fine-tuning.
327	
328	To confirm that our NLEX data mix does not negatively impact the performance of the model on general tasks at the expense of boosting output prediction, we look at several standard coding and maths benchmarks. Specifically we consider CruxEval-Input (Gu et al., [2024b](https://arxiv.org/html/2604.03253#bib.bib6 "CRUXEval: a benchmark for code reasoning, understanding and execution")), MBPP (Austin et al., [2021](https://arxiv.org/html/2604.03253#bib.bib53 "Program synthesis with large language models")), HumanEval Plus (Liu et al., [2023a](https://arxiv.org/html/2604.03253#bib.bib54 "Is your code generated by chatGPT really correct? rigorous evaluation of large language models for code generation")), LiveCodeBench v5 (Jain et al., [2024](https://arxiv.org/html/2604.03253#bib.bib38 "Livecodebench: holistic and contamination free evaluation of large language models for code")), GSM8k (Cobbe et al., [2021](https://arxiv.org/html/2604.03253#bib.bib56 "Training verifiers to solve math word problems")), and Math 500 (Lightman et al., [2023](https://arxiv.org/html/2604.03253#bib.bib55 "Let’s verify step by step")). As reported in Table [7](https://arxiv.org/html/2604.03253#A1.T7 "Table 7 ‣ A.1.1 Supervised fine-tuning. ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models"), using the NLEX data mix does not notably harm any metric, and even improves output prediction abilities as noted by CruxEval-Input.
329	
330	Table 7: Investigating the impact of the NLEX data mix compared to a standard reasoning and instruction following mix on various standard coding and maths benchmarks. All models are trained with supervised fine tuning for the same budget only changing the data.
331	
332	#### A.1.2 The effect of RL on output prediction
333	
334	To better evaluate the effect of additional RL phase on top of the SFT, we evaluate CWM model, trained with and without RL considering output prediction only. For a reference, we additionally include results for the official post-trained CWM model. Results are reported in[Table 8](https://arxiv.org/html/2604.03253#A1.T8 "In A.1.2 The effect of RL on output prediction ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models"). As expected, results suggest that the RL phase significantly improve results on output prediction over competitive programming questions. We omit Qwen results as without RL, their performance was significantly lower.
335	
336	Table 8: Output prediction performance of the CWM with and without RL. For reference we additionally report results for the official CWM model.
337	
338	#### A.1.3 Self-Verification
339	
340	To further analyse the impact if self-verification using self-execution simulation, we wanted to study a setup where the tests used for verification were not present at the time of generating the solutions. To that end, we generate solutions using a model trained jointly for output prediction and competitive programming solving, but without tests in the question description for training and inference. This represents a case where the tests for verification contain completely new information unseen when generating the solution. Results are provided in Figure [6](https://arxiv.org/html/2604.03253#A1.F6 "Figure 6 ‣ A.1.3 Self-Verification ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models"). These suggest that while removing the tests from the description has a negative notable impact on performance, much of the performance can be gained by filtering solutions using these tests. It can also suggest that tests not used for generating the solution could have a higher positive impact for verification, motivating future investigation of test generation.
341	
342	![Image 6: Refer to caption](https://arxiv.org/html/2604.03253v1/x6.png)
343	
344	Figure 6: Comparing best@k when ranking solutions generated by CWM post-trained jointly for solving and output prediction, using the same model as a verifier. The model here was trained and evaluated without the public tests as part of the description.
345	
346	#### A.1.4 Self-RLEF
347	
348	By default we allow a maximum of 10 10 turns for execution RLEF, and _Self-RLEF_. However in practice the model often submits its solution prior leading to an average of 3.33 3.33 turns. We wish to consider the performance of _Self-RLEF_ when limiting the number of solve turns to a maximum of 3 3. We provide results in Table [9](https://arxiv.org/html/2604.03253#A1.T9 "Table 9 ‣ A.1.4 Self-RLEF ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models"). In practice the model uses an average of 2.38 2.38 turns.
349	
350	Table 9: Solve rates when using real or simulated execution feedback, but limiting to 3 3 turns. This extends Table [3](https://arxiv.org/html/2604.03253#S6.T3 "Table 3 ‣ 6.2 Self-Execution for Competitive Programming ‣ 6 Results ‣ Self-Execution Simulation Improves Coding Models") under a more compute constraint setup.
351	
352	#### A.1.5 Beyond _Self_-Verification
353	
354	We provide results for using a dedicated output prediction model as a tool for verifying solutions of other models in a best@k setup. Results provided in Figures [7](https://arxiv.org/html/2604.03253#A1.F7 "Figure 7 ‣ A.1.5 Beyond Self-Verification ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models") and [8](https://arxiv.org/html/2604.03253#A1.F8 "Figure 8 ‣ A.1.5 Beyond Self-Verification ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models") show consistent improvements from this approach, for both Qwen3-4B and CWM Solve-RL, with only a slight degradation compared to ground truth execution of these tests. Like the results for Qwen3-32B in the main paper this further demonstrates the efficacy of this approach.
355	
356	![Image 7: Refer to caption](https://arxiv.org/html/2604.03253v1/x7.png)
357	
358	Figure 7: Comparing best@k when ranking Qwen3-4B solutions, using CWM post-trained only for output prediction as a verifier. 
359	
360	![Image 8: Refer to caption](https://arxiv.org/html/2604.03253v1/x8.png)
361	
362	Figure 8: Comparing best@k when ranking solutions by CWM post-trained only for competitive programming solving (denoted SOLVE-RL in Table [3](https://arxiv.org/html/2604.03253#S6.T3 "Table 3 ‣ 6.2 Self-Execution for Competitive Programming ‣ 6 Results ‣ Self-Execution Simulation Improves Coding Models")), using CWM post-trained only for output prediction as a verifier. 
363	
364	We also provide results of using a dedicated verifier based on a smaller model (Qwen2.5-7B), on solutions generated by a model starting from the same base model. Results provided in Figure [9](https://arxiv.org/html/2604.03253#A1.F9 "Figure 9 ‣ A.1.5 Beyond Self-Verification ‣ A.1 Additional Results ‣ Appendix A Appendix. ‣ Self-Execution Simulation Improves Coding Models") show that this method is also effective with models at this scale. This outperforms the performance in Figure [4](https://arxiv.org/html/2604.03253#S5.F4 "Figure 4 ‣ 5.2 Trained Models ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models") which suggests that the constraint of having the same model for solving and verification does impose challenges especially with models with limited capacity.
365	
366	![Image 9: Refer to caption](https://arxiv.org/html/2604.03253v1/x9.png)
367	
368	Figure 9: Comparing best@k when ranking solutions by Qwen-7B post-trained for competitive programming solving, using Qwen-7B post-trained only for output prediction as a verifier. This mirrors the results for Qwen in Figure [4](https://arxiv.org/html/2604.03253#S5.F4 "Figure 4 ‣ 5.2 Trained Models ‣ 5 Experimental Setup ‣ Self-Execution Simulation Improves Coding Models"), but when each model has a dedicated role.
369	
370	### A.2 Self-RLEF Example Inference
371	
372	To demonstrate how the iterative self-fixing and self verification looks in practice in _Self-RLEF_ we provide the (abbreviated) multi-turn inference for a successful LCB-IO solution using our model.
373	
374	```
375	Turn 1 - (Abbreviated) Solve Prompt
376	
377	 
378	
379	Turn 1 - (Abbreviated) Solve Response
380	
381	 
382	
383	Turn 2 - (Abbreviated) Simulation Response
384	
385	 
386	
387	Turn 3 - (Abbreviated) Fix or Submit Prompt
388	
389	 
390	
391	Turn 3 - (Abbreviated) Fix or Submit Prompt
392	
393	 
394	
395	Turn 4 - (Abbreviated) Simulation Response
396	
397	 
398	
399	Turn 5 - (Abbreviated) Fix or Submit Response
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "746bd4af-9f03-4cc9-a0d3-10728f84cbca",
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "16a20b3f-83f9-441f-88b1-4a8c4afb70f2",
  "sourceToolAssistantUUID": "746bd4af-9f03-4cc9-a0d3-10728f84cbca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-11T22:50:09.268Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FJaVj7nT58Fqm2NTWebUWo`</summary>

```json
{
  "query": "Gallil Maimon \"Self-Execution Simulation\" github code release model weights 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16a20b3f-83f9-441f-88b1-4a8c4afb70f2",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbgYeXsbF6vQdb8VA7b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef6abe06-ee61-49a0-80e3-2b09bb5f9559",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPuPgP3D52HKAkFUNoipcL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11460,
      "cache_read_input_tokens": 16041,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11460,
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

_source line 33 · 2026-05-11T22:50:09.856Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S4pW5j2otkFgdoFtvnsQK1`</summary>

```json
{
  "query": "\"execution trace\" program repair ranking verification vs generation augmented LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef6abe06-ee61-49a0-80e3-2b09bb5f9559",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbgYeXsbF6vQdb8VA7b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "50b350c4-75d3-4c5f-8e21-63448d09720f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPuPgP3D52HKAkFUNoipcL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11460,
      "cache_read_input_tokens": 16041,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11460
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 300,
          "cache_read_input_tokens": 16041,
          "cache_creation_input_tokens": 11460,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11460,
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

_source line 34 · 2026-05-11T22:50:14.998Z_

<details><summary>↩ Tool result · `toolu_01FJaVj7nT58Fqm2NTWebUWo`</summary>

```text
Web search results for query: "Gallil Maimon "Self-Execution Simulation" github code release model weights 2026"

Links: [{"title":"gallilmaimon (Gallil Maimon) · GitHub","url":"https://github.com/gallilmaimon"},{"title":"Self-Execution Simulation Improves Coding Models","url":"https://arxiv.org/html/2604.03253"},{"title":"[2510.02387] CWM: An Open-Weights LLM for Research on Code Generation with World Models","url":"https://arxiv.org/abs/2510.02387"},{"title":"CWM: An Open-Weights LLM for Research on Code Generation with World Models | Research - AI at Meta","url":"https://ai.meta.com/research/publications/cwm-an-open-weights-llm-for-research-on-code-generation-with-world-models/"},{"title":"Gallil Maimon","url":"https://pages.cs.huji.ac.il/gallilmaimon/"},{"title":"GitHub - slp-rl/salmon: The official code for the SALMon🍣 benchmark (ICASSP 2025 - Oral)","url":"https://github.com/slp-rl/salmon"},{"title":"Weekly AI Model Digest — April 5, 2026","url":"https://gist.github.com/igorrivin/9d0ea4d482af444120a6f3dd7b4320fb"},{"title":"The Best Open-Source LLMs for Agentic Coding in 2026 | MindStudio","url":"https://www.mindstudio.ai/blog/best-open-source-llms-agentic-coding-2026"},{"title":"simulation-modeling · GitHub Topics · GitHub","url":"https://github.com/topics/simulation-modeling"},{"title":"simulation-model · GitHub Topics · GitHub","url":"https://github.com/topics/simulation-model"}]

Based on the search results, here's what I found:

Gallil Maimon is an author of a research paper on "Self-Execution Simulation Improves Coding Models," published on arXiv on March 11, 2026. The work demonstrates that code LLMs can be trained to simulate program execution in a step-by-step manner, combining supervised fine-tuning on natural language execution traces with reinforcement learning using verifiable rewards.

Regarding the GitHub code release and model weights: Gallil Maimon's GitHub profile shows 4 repositories available, though the search results don't provide specific details about whether the "Self-Execution Simulation" code or model weights have been released to GitHub yet.

Additionally, Gallil Maimon is one of the authors of the CWM (Code World Model) project, which released a 32-billion-parameter open-weights LLM for research on code generation with world models.

For more specific details about the exact GitHub repository and model weight availability, you may want to check Gallil Maimon's GitHub profile directly or the arXiv paper's supplementary materials.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef6abe06-ee61-49a0-80e3-2b09bb5f9559",
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "d1428dd9-4d17-4547-b4ee-0ba2bc22a659",
  "sourceToolAssistantUUID": "ef6abe06-ee61-49a0-80e3-2b09bb5f9559",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-11T22:50:17.119Z_

<details><summary>↩ Tool result · `toolu_01S4pW5j2otkFgdoFtvnsQK1`</summary>

```text
Web search results for query: ""execution trace" program repair ranking verification vs generation augmented LLM 2025 2026"

Links: [{"title":"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate","url":"https://arxiv.org/html/2604.02647"},{"title":"[2505.04441] Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/abs/2505.04441"},{"title":"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/html/2505.04441v1"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"Runtime Execution Traces Guided Automated Program Repair","url":"https://arxiv.org/pdf/2604.02647"},{"title":"Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback","url":"https://arxiv.org/html/2601.00509"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"A Survey of LLM-based Software Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v2"}]

Based on the search results, I found several relevant papers and research on execution traces, program repair, and LLMs from 2025-2026:

## Key Research Findings

### TraceRepair Framework
TraceRepair correctly resolves 392 defects on the Defects4J benchmark (217 on v1.2 and 175 on v2.0), outperforming all compared methods. This work combines dynamic analysis with LLM-based repair through execution-driven approaches.

### Execution Traces for APR with Code LLMs
While LLMs show promising performance on programming tasks including Automatic Program Repair, most approaches are limited to static analysis and disregard runtime behavior. This work augments standard APR prompts with program execution traces. However, simply incorporating execution traces into the prompt provides limited performance improvement over trace-free baselines in only 2 out of 6 tested dataset/model configurations.

### Analysis-Augmented Generation (AAG)
Analysis-Augmented Generation involves incorporating program static or dynamic analysis results such as error traces or data-flow facts into the prompt or constraining the model's output. Recent LLM-based APR systems published from January 2022 to June 2025 can be categorized into four paradigms with retrieval- or analysis-augmented contexts strengthening them.

### Survey of LLM-based Repair
AAG incorporates static or dynamic program-analysis results, such as error traces or data-flow facts, into the prompt or uses them to constrain the model's output, representing a cross-cutting enhancement layer across different repair paradigms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50b350c4-75d3-4c5f-8e21-63448d09720f",
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "c792b110-e574-4f81-afd3-75e94d8aa003",
  "sourceToolAssistantUUID": "50b350c4-75d3-4c5f-8e21-63448d09720f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-11T22:50:20.239Z_

Let me check Gallil Maimon's GitHub profile for any Self-Execution Simulation code release.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c792b110-e574-4f81-afd3-75e94d8aa003",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011Cawbhmeerzw58ThC6c38A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53291f61-4190-4672-8e2a-c2fd78ad0dd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F68ctXZybhbc6vVdVM1XSj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20114,
      "cache_read_input_tokens": 27501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20114,
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

_source line 37 · 2026-05-11T22:50:22.275Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01C2L5ac8FemobHhdApRRQWm`</summary>

```json
{
  "url": "https://github.com/gallilmaimon",
  "prompt": "List all repositories visible on this GitHub profile. Look for any repository related to Self-Execution Simulation, execution traces, code world models, or CWM. Note whether any repos have been recently created or updated."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53291f61-4190-4672-8e2a-c2fd78ad0dd5",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011Cawbhmeerzw58ThC6c38A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42943dd2-e787-4f8c-8bf1-43afaf87eb73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F68ctXZybhbc6vVdVM1XSj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20114,
      "cache_read_input_tokens": 27501,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 20114,
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

_source line 38 · 2026-05-11T22:50:23.688Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bx2xyUTGP2TxGw5m3nq2w4`</summary>

```json
{
  "query": "arXiv 2505.04441 Haque Babkin trace complexity overwhelm LLM repair Refactory HumanEval RunBugRun detailed results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42943dd2-e787-4f8c-8bf1-43afaf87eb73",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011Cawbhmeerzw58ThC6c38A",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22800326-6dbe-4b21-a8d5-fc10b8afaeef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F68ctXZybhbc6vVdVM1XSj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20114,
      "cache_read_input_tokens": 27501,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 20114
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 27501,
          "cache_creation_input_tokens": 20114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 20114,
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

_source line 39 · 2026-05-11T22:50:26.546Z_

<details><summary>↩ Tool result · `toolu_01C2L5ac8FemobHhdApRRQWm`</summary>

```text
# GitHub Profile Analysis: gallilmaimon

## Repositories Listed

The profile displays 4 repositories in the pinned section:

1. **slamkit** - "SlamKit is an open source tool kit for efficient training of Speech..." focused on speech language models
2. **DISSC** - Implementation for "Speaking Style Conversion With Discrete Self-Supervised Units" (EMNLP 2023)
3. **salmon** - "The official code for the SALMon benchmark" (ICASSP 2025 - Oral)
4. **LUNATC** - Implementation of "A Universal Adversarial Policy for Text Classifiers" (Neural Networks 2022)

## Key Finding

**No repositories related to Self-Execution Simulation, execution traces, code world models (CWM), or similar topics are visible** on this profile section.

The repositories shown focus on speech processing, language models, and adversarial text classification rather than the specific areas you're searching for.

## Additional Profile Info

- Location: Tel Aviv
- Affiliation: HUJI (Hebrew University of Jerusalem)
- 4 total repositories (as indicated by the tab)
- 20 followers, 32 following
- Several GitHub achievements earned
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42943dd2-e787-4f8c-8bf1-43afaf87eb73",
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "2961d6ee-5806-4a79-a603-dd57b29e862f",
  "sourceToolAssistantUUID": "42943dd2-e787-4f8c-8bf1-43afaf87eb73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-11T22:50:31.606Z_

<details><summary>↩ Tool result · `toolu_01Bx2xyUTGP2TxGw5m3nq2w4`</summary>

```text
Web search results for query: "arXiv 2505.04441 Haque Babkin trace complexity overwhelm LLM repair Refactory HumanEval RunBugRun detailed results"

Links: [{"title":"[2505.04441] Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/abs/2505.04441"},{"title":"Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs","url":"https://arxiv.org/html/2505.04441"},{"title":"Machine Learning May 2025","url":"https://www.arxiv.org/list/cs.LG/2025-05?skip=375&show=25"},{"title":"[2505.23953] Enhancing LLM-Based Code Generation with Complexity Metrics: A Feedback-Driven Approach","url":"https://arxiv.org/abs/2505.23953"},{"title":"TRAIL: Trace Reasoning and Agentic Issue Localization","url":"https://arxiv.org/html/2505.08638v3"},{"title":"Enhancing LLM-Based Code Generation with Complexity ...","url":"https://arxiv.org/pdf/2505.23953"},{"title":"[2602.19439] OptiRepair: Closed-Loop Diagnosis and Repair of Supply Chain Optimization Models with LLM Agents","url":"https://arxiv.org/abs/2602.19439"},{"title":"Repairing vulnerabilities without invisible hands. A ...","url":"https://arxiv.org/pdf/2507.20977"},{"title":"Automated Repair of Ambiguous Natural Language Requirements","url":"https://arxiv.org/html/2505.07270v1"},{"title":"VScan: Rethinking Visual Token Reduction for Efficient Large Vision-Language Models","url":"https://arxiv.org/html/2505.22654.pdf"}]

Based on the search results, I found the paper arXiv 2505.04441. Here are the detailed results:

## Paper Overview

The paper is titled "Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs" and was authored by Mirazul Haque, Petr Babkin, Farima Farmahinifarahani, and Manuela Veloso, submitted on May 7, 2025.

## Key Findings

The research investigates how execution traces can improve LLM-based Automatic Program Repair (APR):

1. **Limited Direct Benefits**: Simply incorporating execution traces into the prompt provides a limited performance improvement over trace-free baselines, in only 2 out of 6 tested dataset / model configurations.

2. **Trace Complexity Overwhelm**: The effectiveness of execution traces for APR diminishes as their complexity increases. More specifically, the analysis examined the relationship between trace complexity and LLM success, considering trace length and number of variable modifications, and found that the effectiveness of trace-based prompts decreases with growing length and number of variable assignments.

3. **LLM-Optimized Traces**: The researchers explored several strategies for leveraging traces in prompts and demonstrated that LLM-optimized prompts help outperform trace-free prompts more consistently. LLM-optimized trace-based prompts provide the most consistent results with respect to program repair.

4. **Datasets**: The approach was evaluated using the GPT family of models on three popular APR datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22800326-6dbe-4b21-a8d5-fc10b8afaeef",
  "isSidechain": true,
  "promptId": "9aaf4902-91f4-4aad-93ee-4850f2a3e481",
  "agentId": "a169391eaefd9ac97",
  "type": "user",
  "uuid": "7a9e471a-5156-48dc-a89b-b232fb97f3e9",
  "sourceToolAssistantUUID": "22800326-6dbe-4b21-a8d5-fc10b8afaeef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-11T22:51:33.888Z_

Now I have comprehensive information. Here is my detailed research report.

---

## Detailed Research Report

### 1. arXiv 2505.04441: "Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs"

**Authors:** Mirazul Haque, Petr Babkin, Farima Farmahinifarahani, Manuela Veloso (May 7, 2025)

**Core Finding:** Simply incorporating execution traces into APR prompts provides limited performance improvement over trace-free baselines, in only 2 out of 6 tested configurations.

**The 6 Configurations (3 datasets x 2 models):**

| Model | Dataset | Trace vs Error-Only |
|-------|---------|-------------------|
| GPT-3.5 | Refactory | Traces WORSE |
| GPT-3.5 | HumanEval-Java | Traces WORSE or neutral |
| GPT-3.5 | RunBugRun | Traces WORSE or neutral |
| GPT-4 | Refactory | Traces WORSE (Error prompts: 0.791 CFA vs Trace: 0.737) |
| GPT-4 | HumanEval-Java | Traces BETTER (Trace: 0.511 vs Error: 0.493) |
| GPT-4 | RunBugRun | Traces BETTER (Trace: 0.558 vs Error: 0.529) |

Traces only helped in the GPT-4 + HumanEval-Java and GPT-4 + RunBugRun configurations. Notably, on Refactory, error-only prompts decisively outperformed trace prompts for both GPT-3.5 and GPT-4.

**Why Trace Effectiveness Diminishes with Complexity:**

1. **Trace length correlation:** For HumanEval-Java and RunBugRun, median trace length and number of variable modifications were significantly higher for failing fixes than correct ones. Longer traces correlate with lower fix probability.

2. **Information overload:** Overly complex traces "overwhelm LLMs' long context and ultimately confuse it" rather than providing helpful debugging information.

3. **Model capability gap:** GPT-3.5 showed consistent degradation with traces, while GPT-4 showed selective benefits. The authors attribute this to a "qualitative generational gap when it comes to emergent abilities of LLMs."

4. **Variable modification patterns:** Successful fixes on Refactory had a median of just 1 variable modification vs. 5 on RunBugRun, suggesting simpler traces are more useful.

**Strategies They Tested:**
- **Collated traces** (inline comments at code lines): "disappointingly do not provide an improvement over trace prompts"
- **LLM-optimized traces (OPT):** GPT-4-32k condensed lengthy traces. This was the most effective, providing "the most consistent performance gains on both CFA and CPA metrics" -- CFA range of 0.472-0.753 vs baseline collated traces at 0.452-0.656
- **Confidence-based selection:** Using Likert-scale confidence scoring to route between prompt types -- "significantly worse than OPT on average"
- **Trace-length routing (TRL OPT):** Switching based on predetermined trace-length thresholds -- inconsistent benefits

**Probing studies:** GPT-4 achieved only 88% accuracy at trace collation on reference programs but just 45% on diverse datasets; trace prediction from scratch never exceeded 50% on reference programs and dropped to 15% on diverse datasets.

### 2. Critical Distinction: Trace-Augmented GENERATION vs. Simulation-Based RANKING

This is the most important finding for your research premise. The two papers study fundamentally different uses of execution traces:

**arXiv 2505.04441 (Haque et al.) studied trace-augmented GENERATION:**
- They stuff execution traces into prompts and ask the LLM to generate a repair directly
- The trace is input context for a single-shot generation task
- The paper does NOT discuss trace-based ranking at all
- Their critique applies to: "Can raw trace data in a prompt help an LLM write better code?"

**arXiv 2604.03253 (Maimon et al., Self-Execution Simulation) studied simulation-based RANKING/VERIFICATION:**
- They train models to simulate execution and predict outputs
- They use predicted outputs for best-of-k selection (ranking candidates by predicted test pass count)
- They also use simulation for iterative self-fixing
- Their key mechanism: "candidate solutions are simulated on public or generated tests and retained only if their predicted outputs align with the expected ones"
- Results: self-verification provides 2-8 point improvements under best@k setup, with only a minor "simulation gap" compared to actual execution

**Why the 2505.04441 critique likely does NOT apply to simulation-based ranking:**

1. **Different information flow:** In trace-augmented generation, the LLM must parse a complex trace AND simultaneously generate correct code. In simulation-based ranking, the LLM only needs to predict a single output value (pass/fail) for each candidate -- a much simpler task.

2. **Complexity scaling:** The 2505.04441 finding that "longer traces overwhelm LLMs" is about cramming trace data into generation prompts. In ranking, the model processes each candidate independently and produces a binary verdict, not a full program.

3. **The TraceRepair paper (arXiv 2604.02647)** provides further evidence that traces CAN work when used as logical constraints for evaluation (fixing 392 bugs on Defects4J vs. 162 for ChatRepair), rather than as raw prompt augmentation.

4. **Self-Execution Simulation explicitly shows** that even untrained models using the self-RLEF scaffold "show no noticeable improvement" -- the training to simulate execution is what matters, not just providing trace data in prompts.

### 3. Self-Execution Simulation (arXiv 2604.03253) -- Code/Data Availability

**Authors:** Gallil Maimon, Ori Yoran, Felix Kreuk, Michael Hassid, Gal Cohen, Pierre Chambon, Yossi Adi (from Meta/FAIR and Hebrew University of Jerusalem)

**Code/Data Status: NOT publicly released.**
- The paper contains no GitHub links, no code repository references, and no dataset release statements
- Gallil Maimon's GitHub profile (github.com/gallilmaimon) shows 4 repositories, none related to this work -- only speech processing and NLP projects (slamkit, DISSC, salmon, LUNATC)
- The Hugging Face Papers page for this paper does not link to any released models or datasets
- The paper builds on CWM (Code World Model, arXiv 2510.02387) which IS open-weights, but the Self-Execution Simulation fine-tuned models and NLEX training data (~80M execution descriptions) are not released
- The paper's training data is massive: ~30M functions for basic code, 35k from competitive programming, ~80M natural language execution descriptions, ~143k code-input-output examples for RL

**Key technical details from the paper:**
- Base models: Qwen2.5-3B, Qwen2.5-7B, and CWM-base
- SFT on natural language execution traces (NLEX) generated using Qwen3-32B-FP8
- RL with verifiable rewards for output prediction
- Self-verification (best@k): up to 5.5% absolute improvement on competitive programming
- Self-RLEF: consistent gains across all configurations; model fixes 17% of initially failing solutions on public tests
- Acknowledged limitations: struggles with "complex computational operations (e.g., multiplying large numbers, compute logarithms)" and is "currently limited to single file competitive programming questions"

### 4. Summary Assessment for Your Research

**The 2505.04441 critique has limited applicability to simulation-based ranking approaches because:**

1. It specifically studied trace-augmented *generation* (putting traces in prompts to help write repairs), not trace-based *ranking* or *verification* of candidate solutions

2. The complexity scaling problem it identifies (longer traces = worse performance) is a property of using traces as prompt context for generation, not of using execution simulation for binary pass/fail verification

3. The Self-Execution Simulation paper (2604.03253) directly demonstrates that simulation-based ranking WORKS, with 2-8 point best@k improvements and only a minor simulation gap vs. real execution

4. The TraceRepair paper (2604.02647) shows that using traces as logical constraints (not raw prompt data) achieves SOTA results (392 bugs fixed vs. 162 baseline)

**The key differentiator is HOW traces are used:** as raw prompt augmentation for generation (limited value, per 2505.04441) vs. as the basis for ranking/verification/constraint checking (substantial value, per 2604.03253 and 2604.02647).

Sources:
- [Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs (arXiv 2505.04441)](https://arxiv.org/abs/2505.04441)
- [Full HTML version of arXiv 2505.04441](https://arxiv.org/html/2505.04441v1)
- [Self-Execution Simulation Improves Coding Models (arXiv 2604.03253)](https://arxiv.org/abs/2604.03253)
- [Self-Execution Simulation full paper](https://arxiv.org/html/2604.03253)
- [Hugging Face Papers page for 2604.03253](https://huggingface.co/papers/2604.03253)
- [Gallil Maimon's GitHub profile](https://github.com/gallilmaimon)
- [Runtime Execution Traces Guided APR with Multi-Agent Debate (TraceRepair, arXiv 2604.02647)](https://arxiv.org/html/2604.02647v1)
- [A Survey of LLM-based Automated Program Repair](https://arxiv.org/html/2506.23749v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a9e471a-5156-48dc-a89b-b232fb97f3e9",
  "isSidechain": true,
  "agentId": "a169391eaefd9ac97",
  "requestId": "req_011CawbiqXqZWULRTGzppEpr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02cfa09f-8392-4934-9891-f6bfc49e5224",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f7ed7f67-a87f-46e7-a409-d4d552b7568f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVaVfSSC4gDxP6GSuEgztg",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1509,
      "cache_read_input_tokens": 47615,
      "output_tokens": 2454,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1509
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2454,
          "cache_read_input_tokens": 47615,
          "cache_creation_input_tokens": 1509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1509,
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
