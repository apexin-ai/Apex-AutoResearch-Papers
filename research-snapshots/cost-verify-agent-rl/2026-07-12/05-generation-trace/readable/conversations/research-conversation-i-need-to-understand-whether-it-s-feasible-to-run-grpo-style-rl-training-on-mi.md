# Research conversation: I need to understand whether it's feasible to run GRPO-style RL training on Mind2Web. The key challenge is that Mind2Web

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a984e38911c2dde96.jsonl`
- **Structured JSON:** [`b24223de8db12391353a.json`](../../sessions/b2/b24223de8db12391353a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-10T19:33:22.622Z_

I need to understand whether it's feasible to run GRPO-style RL training on Mind2Web. The key challenge is that Mind2Web is primarily an offline benchmark with cached HTML snapshots — it doesn't have an interactive simulator like ALFWorld or WebShop.

Please search for:
1. "Mind2Web reinforcement learning training" — has anyone done RL (not just SFT) on Mind2Web?
2. "offline GRPO" or "offline group relative policy optimization" — can GRPO work in offline settings?
3. "Mind2Web-Live" or "Online-Mind2Web" — are there interactive versions that support RL?
4. "recreated websites RL training" — the 2026 paper on safe web agent RL training
5. "WebAgent-R1" (arXiv 2505.16421) — how does it do RL on web tasks? Does it use GRPO?
6. "Mano web agent" — how does Mano do online RL on web tasks?

Key question: Can we do step-level GRPO on Mind2Web by sampling multiple action predictions at each step (from cached HTML) and computing advantages based on ground-truth correctness? Or does GRPO fundamentally require interactive environment rollouts?

Also check: does the verl-agent framework support Mind2Web or any offline web benchmark?

Report concisely on feasibility, practical approach, and any existing infrastructure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a984e38911c2dde96",
  "type": "user",
  "uuid": "7f44f032-3bf7-433d-b86c-6860c9a93944",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:33:22.626Z_

```json
{
  "parentUuid": "7f44f032-3bf7-433d-b86c-6860c9a93944",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
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
  "uuid": "765c6dcd-4dff-4f45-a643-799710fe994e",
  "timestamp": "2026-05-10T19:33:22.626Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T19:33:25.562Z_



I'll search for all of these topics systematically. Let me start with web searches across all the key queries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "765c6dcd-4dff-4f45-a643-799710fe994e",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauSsxcBatJWyrXawzLYV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "268a0643-a2bb-4bce-bb53-740b19c4865e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NJbmdzqaY6gg4dKkVYrUL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 876,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 876,
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

_source line 4 · 2026-05-10T19:33:26.026Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VULuq9EtxSczbRTEjArmrB`</summary>

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
  "parentUuid": "268a0643-a2bb-4bce-bb53-740b19c4865e",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauSsxcBatJWyrXawzLYV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc8666b8-c7f3-4919-9a2b-ea0107600088",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018NJbmdzqaY6gg4dKkVYrUL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 876,
      "cache_read_input_tokens": 8223,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 876
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 876,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 876,
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

_source line 5 · 2026-05-10T19:33:26.030Z_

<details><summary>↩ Tool result · `toolu_01VULuq9EtxSczbRTEjArmrB`</summary>

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
  "parentUuid": "bc8666b8-c7f3-4919-9a2b-ea0107600088",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a984e38911c2dde96",
  "type": "user",
  "uuid": "4a780ed4-cd89-47e1-b02c-b08e6886b2c0",
  "sourceToolAssistantUUID": "bc8666b8-c7f3-4919-9a2b-ea0107600088",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T19:33:29.136Z_



Now let me run all the web searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a780ed4-cd89-47e1-b02c-b08e6886b2c0",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauStDEG4s7K25renyrGR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5010097-b926-4f43-986a-b99f6a5984c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wa7bBjW26QyxPKAYAhTJcp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1417,
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

_source line 7 · 2026-05-10T19:33:29.842Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NAnVSZz5WBREhn9ZkCMbsT`</summary>

```json
{
  "query": "Mind2Web reinforcement learning training GRPO 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5010097-b926-4f43-986a-b99f6a5984c3",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauStDEG4s7K25renyrGR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41eb77e7-348e-4b8b-a493-4c3ccbced1d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wa7bBjW26QyxPKAYAhTJcp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1417,
      "cache_read_input_tokens": 9099,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1417
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 9099,
          "cache_creation_input_tokens": 1417,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1417,
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

_source line 8 · 2026-05-10T19:33:36.970Z_

<details><summary>↩ Tool result · `toolu_01NAnVSZz5WBREhn9ZkCMbsT`</summary>

```text
Web search results for query: "Mind2Web reinforcement learning training GRPO 2025 2026"

Links: [{"title":"Mano Technical Report","url":"https://arxiv.org/html/2509.17336v1"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"Mano Technical Report Tianyu Fu ∗ Anyang Su ∗ Chenxu Zhao ∗† Hanning Wang ∗","url":"https://www.mininglamp.com/wp-content/uploads/2025/09/%E6%98%8E%E7%95%A5%E7%A7%91%E6%8A%80-Mano-Technical-Report.pdf"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"Reinforcement Learning (RL) Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide"},{"title":"The State of Reinforcement Learning for LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"},{"title":"AI 101: The State of Reinforcement Learning in 2025","url":"https://www.turingpost.com/p/stateofrl2025"},{"title":"GRPO++: Tricks for Making RL Actually Work","url":"https://cameronrwolfe.substack.com/p/grpo-tricks"},{"title":"PPO for LLMs: A Guide for Normal People","url":"https://cameronrwolfe.substack.com/p/ppo-llm"},{"title":"EWRL: European Workshop on Reinforcement Learning 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=998"}]

Based on the search results, here's what I found about Mind2Web, reinforcement learning training, and GRPO in 2025-2026:

## Mind2Web and Reinforcement Learning Training

Mind2Web is a multi-modal benchmark that evaluates the accuracy of web-based operations, covering over 100 websites, 1,000+ operation trajectories, and 7,000+ actions, with 3 testing protocols for comprehensive assessment.

## GRPO Application to Mind2Web

The Mano GUI agent model was trained using GRPO, rewarding the model for correctly completing full interaction sequences, which enhances overall task completion ability. The model leverages GRPO with distinct rewards focused on real-time adaptability and exploration in dynamic settings, where the agent collects new interaction data through online trials, which is then cycled back as offline data for further refinements, enabling continuous improvement via iterative loops.

## GRPO in 2025-2026 Context

GRPO is an online RL method that generates new responses during training and computes advantages by comparing them within groups. GRPO and DAPO remove the need for critic models, reference models, and preference pair curation. GRPO (Group Relative Policy Optimization) is the algorithm backbone that sits inside a broader training approach that strengthens the model's reasoning ability called Reinforcement Learning with Verifiable Rewards (RLVR).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41eb77e7-348e-4b8b-a493-4c3ccbced1d6",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a984e38911c2dde96",
  "type": "user",
  "uuid": "1318008a-8eb3-4128-8a07-c4c381f15041",
  "sourceToolAssistantUUID": "41eb77e7-348e-4b8b-a493-4c3ccbced1d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T19:33:40.294Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JPKt7FZ3yVAMiNBUErJmZc`</summary>

```json
{
  "query": "offline GRPO \"offline group relative policy optimization\" without environment rollouts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1318008a-8eb3-4128-8a07-c4c381f15041",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauSu1kUEY5So7sv2Q3Rm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b4f0a60-aca5-4a4e-b623-06274e2e40d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q795qzqcX3ftyzAi5eAYRE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 941,
      "cache_read_input_tokens": 10516,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 941
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 10516,
          "cache_creation_input_tokens": 941,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 941,
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

_source line 10 · 2026-05-10T19:33:47.098Z_

<details><summary>↩ Tool result · `toolu_01JPKt7FZ3yVAMiNBUErJmZc`</summary>

```text
Web search results for query: "offline GRPO "offline group relative policy optimization" without environment rollouts"

Links: [{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"},{"title":"GRPO-VPS: Enhancing Group Relative Policy Optimization with Verifiable Process Supervision for Effective Reasoning","url":"https://arxiv.org/html/2604.20659"},{"title":"Group Relative Policy Optimization (GRPO) — verl documentation","url":"https://verl.readthedocs.io/en/latest/algo/grpo.html"},{"title":"Training-Free Group Relative Policy Optimization","url":"https://arxiv.org/html/2510.08191v1"},{"title":"[2510.08191] Training-Free Group Relative Policy Optimization","url":"https://arxiv.org/abs/2510.08191"},{"title":"Training-Free Group Relative Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=tyUnYbE7Gi"},{"title":"GitHub - krafton-ai/Offline-GRPO: Code for the blog post titled \"Continual Post-Training of LLMs via Offline GRPO for Mathematical Reasoning\" · GitHub","url":"https://github.com/krafton-ai/Offline-GRPO"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978"},{"title":"Paper page - Training-Free Group Relative Policy Optimization","url":"https://huggingface.co/papers/2510.08191"}]

Based on the search results, I found relevant information about offline GRPO approaches:

## Offline GRPO Research

Offline Group Relative Policy Optimization (GRPO) is a continual post-training method that utilizes Offline Reinforcement Learning with Verifiable Rewards (Offline RLVR) to overcome the limitations of traditional on-policy methods.

A novel variant of Group Relative Policy Optimization (GRPO) has been introduced that better captures high-quality reasoning traces—even when all outputs are positive—using teacher-generated trajectories.

### Key Characteristic: No Additional Rollouts

An important property of offline GRPO approaches is their efficiency regarding environment interactions. Unlike per-state rollout procedures, this approach incurs no extra rollouts: it is entirely offline and requires only lightweight key-based grouping using hashmaps.

### Related Approaches

The search also revealed related methods that maintain offline operation without additional rollouts:

- A hierarchical grouping structure can capture both global trajectory quality and local step effectiveness without relying on auxiliary models or additional rollouts.

The offline approach addresses limitations by leveraging pre-generated high-quality reasoning trajectories from teacher models, enabling faster training and better performance improvements.

These offline GRPO methods represent an advancement in making policy optimization more efficient by eliminating the need for environment rollouts during training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b4f0a60-aca5-4a4e-b623-06274e2e40d8",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a984e38911c2dde96",
  "type": "user",
  "uuid": "e32cc495-d8a0-452c-a483-e94ad743a750",
  "sourceToolAssistantUUID": "1b4f0a60-aca5-4a4e-b623-06274e2e40d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T19:33:52.415Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NkgHnw1bzXA5Sw9jTN9LGF`</summary>

```json
{
  "query": "Mind2Web-Live interactive online benchmark web agent 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e32cc495-d8a0-452c-a483-e94ad743a750",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauSum3DZm9Whqb6xhLAG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "746fb77d-bab1-4049-b321-5346f1d0960c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018P4mL66zFa8gdf1Qh7yKMh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 11457,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 853
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 11457,
          "cache_creation_input_tokens": 853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 853,
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

_source line 12 · 2026-05-10T19:34:00.622Z_

<details><summary>↩ Tool result · `toolu_01NkgHnw1bzXA5Sw9jTN9LGF`</summary>

```text
Web search results for query: "Mind2Web-Live interactive online benchmark web agent 2025 2026"

Links: [{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"An Illusion of Progress? Assessing the Current State of Web Agents | OpenReview","url":"https://openreview.net/forum?id=6jZi4HSs6o"},{"title":"Mind2Web-live Benchmark","url":"https://www.emergentmind.com/topics/mind2web-live"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://osu-nlp-group.github.io/Mind2Web/"},{"title":"Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge","url":"https://osu-nlp-group.github.io/Mind2Web-2/"},{"title":"An Illusion of Progress? Assessing the Current State of Web Agents","url":"https://arxiv.org/html/2504.01382v4"},{"title":"Online-Mind2Web Benchmark","url":"https://www.emergentmind.com/topics/online-mind2web-benchmark"},{"title":"WebCanvas: Benchmarking Web Agents in Online Environments | OpenReview","url":"https://openreview.net/forum?id=wkp57p0uhm"},{"title":"Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge | OpenReview","url":"https://openreview.net/forum?id=AUaW6DS9si"},{"title":"How we built the best browser agent with Auto-Research","url":"https://browser-use.com/posts/online-mind2web-benchmark"}]

Based on the search results, here's what I found about Mind2Web-Live and related interactive online benchmarks for web agents:

## Mind2Web-Live

Mind2Web-live is an online benchmark for web agents, featuring live demonstrations and key-node states to enable dynamic evaluation in evolving web environments. It employs multi-phase filtering, re-annotation, and replay mechanisms to ensure that 542 diverse web tasks yield accurate, reproducible evaluation data.

The final Mind2Web-live dataset contains 542 tasks (438 train, 104 test). Across these, 2,439 key-node states are identified (average 4.5 per task), and annotators record 4,550 low-level actions (≈8.4 steps per task).

Mind2Web-live introduces multi-level, robust evaluation metrics. For each task with Ki key nodes, an agent receives a point for each correctly achieved key node. A task is considered successfully completed if all key nodes are achieved, with the Task Success Rate (SR) being the average across tasks.

## Related Benchmarks

**Online-Mind2Web**: Online-Mind2Web is an online evaluation benchmark consisting of 300 diverse and realistic tasks spanning 136 websites. Claude Computer Use 3.7 (Anthropic, 2025) and Operator (OpenAI, 2025) are among the top performers, with Operator achieving a success rate of 61%.

**Mind2Web 2**: Mind2Web 2 is a benchmark of 130 realistic, high-quality, and long-horizon tasks that require real-time web browsing and extensive information synthesis, constructed with over 1000 hours of human labor.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "746fb77d-bab1-4049-b321-5346f1d0960c",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a984e38911c2dde96",
  "type": "user",
  "uuid": "9130095c-b20f-47e1-be2f-ed8a282c7989",
  "sourceToolAssistantUUID": "746fb77d-bab1-4049-b321-5346f1d0960c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-10T19:34:06.277Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MXdrGZ7uvsSPA8SSe5HsJa`</summary>

```json
{
  "query": "WebAgent-R1 arXiv 2505.16421 GRPO web agent reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9130095c-b20f-47e1-be2f-ed8a282c7989",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauSvksaFGy4ra5uTe6y3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eddffde9-658f-4bae-bbf4-c38a525ba96c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJ5aT3KiK16bBZLgQpbn7S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 12310,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 965
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 12310,
          "cache_creation_input_tokens": 965,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 965,
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

_source line 14 · 2026-05-10T19:34:14.358Z_

<details><summary>↩ Tool result · `toolu_01MXdrGZ7uvsSPA8SSe5HsJa`</summary>

```text
Web search results for query: "WebAgent-R1 arXiv 2505.16421 GRPO web agent reinforcement learning"

Links: [{"title":"[2505.16421] WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/abs/2505.16421"},{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2505.16421v1"},{"title":"WEBAGENT-R1: Training Web Agents via End-to-End Multi-Turn","url":"https://arxiv.org/pdf/2505.16421"},{"title":"[2505.16421v1] WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/abs/2505.16421v1"},{"title":"WebAgent-R1：通过端到端多回合强化学习训练网页智能体 - 科技行者","url":"https://www.techwalker.com/2025/0528/3166896.shtml"},{"title":"Paper page - WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://huggingface.co/papers/2505.16421"},{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2505.16421"},{"title":"[Literature Review] WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://www.themoonlight.io/en/review/webagent-r1-training-web-agents-via-end-to-end-multi-turn-reinforcement-learning"},{"title":"WebAgent-R1: Training Web Agents via End-to- ...","url":"https://www.alphaxiv.org/abs/2505.16421"},{"title":"DynaWeb: Model-Based Reinforcement Learning of Web Agents","url":"https://arxiv.org/html/2601.22149v1"}]

I've found comprehensive information about WebAgent-R1. Here's a summary of the paper arXiv:2505.16421:

## WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning

WebAgent-R1 is a simple yet effective end-to-end multi-turn RL framework for training web agents that learns directly from online interactions with web environments by asynchronously generating diverse trajectories, entirely guided by binary rewards depending on task success.

### Key Contributions

The framework extends Group Relative Policy Optimization (GRPO) to multi-turn settings (M-GRPO) and employs an asynchronous trajectory rollout strategy to improve training efficiency by generating multiple trajectories in parallel.

The approach includes a dynamic context compression mechanism that adaptively adjusts contexts across turns, ensuring scalability and preventing out-of-memory issues when dealing with lengthy HTML observations.

### Performance Results

The method substantially improves task success rates of web agents—boosting Qwen-2.5-3B from 6.1% to 33.9% and Llama-3.1-8B from 8.5% to 44.8%—surpassing previous state-of-the-art results on the WebArena-Lite benchmark.

### Training Insights

In-depth analyses reveal the effectiveness of the thinking-based prompting strategy and test-time scaling through increased interactions, and the paper investigates different RL initialization policies by introducing variants WebAgent-R1-Zero and WebAgent-R1-CoT, which highlight the importance of the warm-up training stage (behavior cloning) and insights on incorporating long chain-of-thought reasoning.

The paper was authored by Zhepei Wei and 11 co-authors and was submitted to arXiv on May 22, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eddffde9-658f-4bae-bbf4-c38a525ba96c",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a984e38911c2dde96",
  "type": "user",
  "uuid": "b4d55ec3-60de-4749-855c-3f959e7f1fa7",
  "sourceToolAssistantUUID": "eddffde9-658f-4bae-bbf4-c38a525ba96c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T19:34:17.324Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0122cZLRqaQYeW3iKptkgCbC`</summary>

```json
{
  "query": "Mano web agent online RL training GRPO technical report 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4d55ec3-60de-4749-855c-3f959e7f1fa7",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauSwmczgrLnT9BLJBGNz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2f6e58f-5652-4390-af92-79c70d1e9827",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8yPGxNy8LxzBST6NBvb64",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1069,
      "cache_read_input_tokens": 13275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1069,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 33,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T19:34:25.939Z_

<details><summary>↩ Tool result · `toolu_0122cZLRqaQYeW3iKptkgCbC`</summary>

```text
Web search results for query: "Mano web agent online RL training GRPO technical report 2025"

Links: [{"title":"Mano Technical Report Tianyu Fu ∗ Anyang Su ∗ Chenxu Zhao ∗† Hanning Wang ∗","url":"https://www.mininglamp.com/wp-content/uploads/2025/09/%E6%98%8E%E7%95%A5%E7%A7%91%E6%8A%80-Mano-Technical-Report.pdf"},{"title":"Mano Technical Report","url":"https://arxiv.org/html/2509.17336v1"},{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2505.16421v1"},{"title":"WEBAGENT-R1: Training Web Agents via End-to-End Multi-Turn","url":"https://arxiv.org/pdf/2505.16421"},{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/webagent-r1-training-web-agents-via-end"},{"title":"How to Train Your LLM Web Agent: A Statistical Diagnosis","url":"https://arxiv.org/html/2507.04103v3"},{"title":"[Literature Review] WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://www.themoonlight.io/en/review/webagent-r1-training-web-agents-via-end-to-end-multi-turn-reinforcement-learning"},{"title":"Multi-Agent Deep Research: Training Multi-Agent Systems with M-GRPO","url":"https://arxiv.org/pdf/2511.13288v2"},{"title":"Training Agents with Reinforcement Learning - Maven","url":"https://maven.com/p/c3950c/training-agents-with-reinforcement-learning"},{"title":"Unlocking Agentic RL Training for GPT-OSS: A Practical Retrospective","url":"https://huggingface.co/blog/LinkedIn/gpt-oss-agentic-rl"}]

Based on the search results, I found relevant information about the Mano technical report on web agent training with online RL and GRPO:

## Mano Web Agent Technical Report (2025)

The Mano system deploys online RL in its third stage based on a simulated environment, leveraging GRPO with distinct rewards focused on real-time adaptability and exploration in dynamic settings. During this phase, the agent collects new interaction data through online trials, which is then cycled back as offline data for further refinements, enabling continuous improvement via iterative loops.

### Training Pipeline Overview

The pipeline consists of three progressive stages: (i) SFT on offline demonstrations; (ii) Offline RL leveraging static trajectories with reward decomposition; and (iii) Online RL with active environment interaction.

### Offline RL Stage

The second stage employs offline RL fine-tuning with group relative policy optimization (GRPO), leveraging data from the simulated environment and designing rewards specifically tailored to encourage successful completion of full interaction sequences offline, enhancing the model's holistic GUI reasoning and GUI decision-making ability.

### Performance Results

Mano achieves state-of-the-art (SOTA) results on multiple GUI benchmarks, outperforming prior agents in metrics like success rate and efficiency, validating the effectiveness of our integrated framework in real-world GUI navigation and interaction tasks.

### Technical Insights

The work provides new insights into RL's role, including a tailored application of the GRPO algorithm with distinct reward functions for the offline and online RL stages—balancing policy stability with goal-oriented optimization—in bridging limitations of VLMs for practical, adaptable GUI agent deployment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2f6e58f-5652-4390-af92-79c70d1e9827",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a984e38911c2dde96",
  "type": "user",
  "uuid": "8d7036c2-ad9c-4014-a0ff-1f6e3b2821e8",
  "sourceToolAssistantUUID": "a2f6e58f-5652-4390-af92-79c70d1e9827",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-10T19:34:28.287Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012DVEDVpCs7vmZL8PkZHAVM`</summary>

```json
{
  "query": "verl-agent framework Mind2Web offline web benchmark support"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d7036c2-ad9c-4014-a0ff-1f6e3b2821e8",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauSxd9HhmaoAaF9mEucX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a770e45-a09d-4f24-a9eb-e4c5595a6963",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ts4VLFgadLcBdpf7BxgdUh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 14344,
      "output_tokens": 63,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1047
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 63,
          "cache_read_input_tokens": 14344,
          "cache_creation_input_tokens": 1047,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1047,
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

_source line 18 · 2026-05-10T19:34:34.376Z_

<details><summary>↩ Tool result · `toolu_012DVEDVpCs7vmZL8PkZHAVM`</summary>

```text
Web search results for query: "verl-agent framework Mind2Web offline web benchmark support"

Links: [{"title":"Mind2Web-live Benchmark","url":"https://www.emergentmind.com/topics/mind2web-live"},{"title":"Mind2Web: Towards a Generalist Agent for the Web","url":"https://osu-nlp-group.github.io/Mind2Web/"},{"title":"How we built the best browser agent with Auto-Research","url":"https://browser-use.com/posts/online-mind2web-benchmark"},{"title":"GitHub - OSU-NLP-Group/Mind2Web: [NeurIPS'23 Spotlight] \"Mind2Web: Towards a Generalist Agent for the Web\" -- the first LLM-based web agent and benchmark for generalist web agents · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web"},{"title":"GitHub - OSU-NLP-Group/Mind2Web-2: [NeurIPS'25 D&B] Mind2Web-2 Benchmark: Evaluating Agentic Search with Agent-as-a-Judge · GitHub","url":"https://github.com/OSU-NLP-Group/Mind2Web-2"},{"title":"GitHub - OSU-NLP-Group/Online-Mind2Web: An Illusion of Progress? Assessing the Current State of Web Agents · GitHub","url":"https://github.com/OSU-NLP-Group/Online-Mind2Web"},{"title":"Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge","url":"https://osu-nlp-group.github.io/Mind2Web-2/"},{"title":"An Illusion of Progress? Assessing the Current State of Web Agents | OpenReview","url":"https://openreview.net/forum?id=6jZi4HSs6o"},{"title":"An Illusion of Progress? Assessing the Current State of Web Agents","url":"https://arxiv.org/html/2504.01382v4"},{"title":"WebCanvas: Benchmarking Web Agents in Online Environments | OpenReview","url":"https://openreview.net/forum?id=wkp57p0uhm"}]

Based on the search results, I found information about Mind2Web benchmarks and offline web evaluation, but I did not find specific information about a "verl-agent framework" in connection with Mind2Web. Let me provide what I found about the related topics:

## Mind2Web Benchmarks and Offline Evaluation

Mind2Web is the first dataset for developing and evaluating generalist agents for the web that can follow language instructions to complete complex tasks on any website. Mind2Web contains 2,350 tasks from 137 websites spanning 31 domains.

### Offline vs. Online Evaluation

There are two versions of Mind2Web with different evaluation approaches:

1. **Original Mind2Web (Offline)**: The original Mind2Web adopts an offline setting by caching portions of websites, which facilitates rapid iteration during agent development but inevitably suffers from incompleteness due to the dynamic nature of many websites.

2. **Mind2Web-Live (Online)**: Mind2Web-live is a real-world, online evaluation benchmark for web agents developed as part of the WebCanvas framework to enable robust assessment of agents in dynamic, continuously evolving web environments.

However, I did not find specific information about a "verl-agent framework" or its relationship to Mind2Web offline support in these search results. If you're looking for information about a specific framework or tool, you may want to provide additional context or check the project's official documentation directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a770e45-a09d-4f24-a9eb-e4c5595a6963",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a984e38911c2dde96",
  "type": "user",
  "uuid": "bf61ed64-6944-42f5-b47d-fc5c4ea23a00",
  "sourceToolAssistantUUID": "0a770e45-a09d-4f24-a9eb-e4c5595a6963",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-10T19:34:37.034Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Js4FFpVzwaQc7RkKFXFuDG`</summary>

```json
{
  "query": "verl-agent github reinforcement learning web agent framework 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf61ed64-6944-42f5-b47d-fc5c4ea23a00",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauSyFBDtxJuAwgsYfjGB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3bd461e5-0751-4f2b-8ab1-d1710e8b167e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVZFWcx49r5ZHntKqZWJ1C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 950,
      "cache_read_input_tokens": 15391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 950,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T19:34:46.560Z_

<details><summary>↩ Tool result · `toolu_01Js4FFpVzwaQc7RkKFXFuDG`</summary>

```text
Web search results for query: "verl-agent github reinforcement learning web agent framework 2025 2026"

Links: [{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengq/verl-agent"},{"title":"GitHub - verl-project/verl: verl/HybridFlow: A Flexible and Efficient RL Post-Training Framework · GitHub","url":"https://github.com/verl-project/verl"},{"title":"GitHub - agentica-project/verl · GitHub","url":"https://github.com/agentica-project/verl"},{"title":"Agentic RL Training - verl documentation - Read the Docs","url":"https://verl.readthedocs.io/en/latest/start/agentic_rl.html"},{"title":"VERL - Agent-lightning","url":"https://microsoft.github.io/agent-lightning/latest/algorithm-zoo/verl/"},{"title":"verl-agent/README.md at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/blob/master/README.md"},{"title":"Verlog - A Multi-turn RL framework for LLM agents | Agentic Intelligence Lab","url":"https://agentic-intelligence-lab.org/2025/08/15/technical-post.html"},{"title":"AgentFly: Extensible and Scalable Reinforcement Learning for LM Agents","url":"https://arxiv.org/html/2507.14897v1"},{"title":"Verl-Tool: Towards Holistic Agentic Reinforcement Learning with Tool Use | OpenReview","url":"https://openreview.net/forum?id=oWFtI0cNsE"},{"title":"GitHub - AgentR1/Agent-R1: Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning · GitHub","url":"https://github.com/0russwest0/Agent-R1"}]

Based on the web search results, here's what I found about verl-agent and the reinforcement learning web agent framework:

## Overview

verl-agent is an extension of veRL, specifically designed for training large language model (LLM) agents via reinforcement learning (RL). Unlike prior approaches that simply concatenate full interaction histories, verl-agent proposes step-independent multi-turn rollout mechanism, which allows for fully customizable per-step input structures, history management, and memory modules.

## Key Features

verl-agent supports multi-turn Agent-Environment interaction, step-wise interaction, and is scalable for long-horizon tasks, supporting multiple RL algorithms including GiGPO, GRPO, PPO, DAPO, GSPO, RLOO, and REINFORCE++.

This design makes verl-agent highly scalable for very long-horizon, multi-turn RL training (e.g., tasks in ALFWorld can require up to 50 steps to complete).

## Recent Updates (2025-2026)

In June 2025, verl-agent received a major update merging features from the latest veRL, including support for Qwen3, LoRA, and REINFORCE++.

In February 2026, HGPO was accepted at ICLR 2026, and the team open-sourced Dr. MAS, which supports stable end-to-end RL post-training of multi-agent LLM systems.

The framework is available on GitHub at the official repository (langfengq/verl-agent) and continues to be actively developed with support for modern LLM/VLM agent training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3bd461e5-0751-4f2b-8ab1-d1710e8b167e",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a984e38911c2dde96",
  "type": "user",
  "uuid": "e9513c8c-0dd0-453e-a09f-79cee8732db8",
  "sourceToolAssistantUUID": "3bd461e5-0751-4f2b-8ab1-d1710e8b167e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-10T19:34:49.157Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T5rzr2kRVpKWHGvvE9f7x9`</summary>

```json
{
  "query": "\"recreated websites\" \"safe RL\" web agent training 2026 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9513c8c-0dd0-453e-a09f-79cee8732db8",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauSz9G45YRE8V5hA2wgn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5424036-fc07-4b75-b4a5-f3c59d9ae5c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRZFxx4ZnhXk2cpyCRctRy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1129,
      "cache_read_input_tokens": 16341,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1129
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 16341,
          "cache_creation_input_tokens": 1129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1129,
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

_source line 22 · 2026-05-10T19:35:05.066Z_

<details><summary>↩ Tool result · `toolu_01T5rzr2kRVpKWHGvvE9f7x9`</summary>

```text
Web search results for query: ""recreated websites" "safe RL" web agent training 2026 paper"

Links: [{"title":"[2603.10505] Safe and Scalable Web Agent Learning via Recreated Websites","url":"https://arxiv.org/abs/2603.10505"},{"title":"Safe and Scalable Web Agent Learning via Recreated Websites","url":"https://arxiv.org/html/2603.10505"},{"title":"WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=oVKEAFjEqv"},{"title":"GitHub - THUDM/WebRL: Building Open LLM Web Agents with Self-Evolving Online Curriculum RL · GitHub","url":"https://github.com/THUDM/WebRL"},{"title":"WebRL: The Framework Training LLM Web Agents - BrightCoding","url":"https://www.blog.brightcoding.dev/2026/05/01/webrl-the-revolutionary-framework-training-llm-web-agents"},{"title":"webrl: training llm web agents via self","url":"https://arxiv.org/pdf/2411.02337"},{"title":"GUI-Agents-Paper-List/paper_by_key/paper_framework.md at main · OSU-NLP-Group/GUI-Agents-Paper-List","url":"https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List/blob/main/paper_by_key/paper_framework.md"},{"title":"[2411.02337] WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning","url":"https://arxiv.org/abs/2411.02337"},{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2505.16421v1"},{"title":"[2505.16421] WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/abs/2505.16421"}]

Based on the search results, I found the paper you're looking for:

## Safe and Scalable Web Agent Learning via Recreated Websites

The paper is titled "Safe and Scalable Web Agent Learning via Recreated Websites" by Hyungjoo Chae and 2 other authors, published on arXiv in March 2026 (arXiv:2603.10505).

**Key Contribution:**

The paper proposes VeriEnv, a framework that treats language models as environment creators, automatically cloning real-world websites into fully executable, verifiable synthetic environments. By exposing controlled internal access via a Python SDK, VeriEnv enables agents to self-generate tasks with deterministic, programmatically verifiable rewards, eliminating reliance on heuristic or LLM-based judges.

**Problem Being Addressed:**

Training autonomous web agents is fundamentally limited by the environments they learn from: real-world websites are unsafe to explore, hard to reset, and rarely provide verifiable feedback.

**Results:**

Through experiments on web agent benchmarks, agents trained with VeriEnv generalize to unseen websites, achieve site-specific mastery through self-evolving training, and benefit from scaling the number of training environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5424036-fc07-4b75-b4a5-f3c59d9ae5c6",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a984e38911c2dde96",
  "type": "user",
  "uuid": "4439d3e5-0ec6-4874-baa1-abfb57b8d258",
  "sourceToolAssistantUUID": "e5424036-fc07-4b75-b4a5-f3c59d9ae5c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-10T19:35:08.760Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HSdNc32TgbPkSRQKvo8Rxb`</summary>

```json
{
  "query": "krafton-ai Offline-GRPO \"offline RLVR\" step-level advantage without rollouts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4439d3e5-0ec6-4874-baa1-abfb57b8d258",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauT1WRK3rnuQPwv8Wdac",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e43ae5a3-a513-43ac-84dc-54705fe57772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JomgDSZ2B7xZjMQNe8sqVA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 915,
      "cache_read_input_tokens": 17470,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 915
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 17470,
          "cache_creation_input_tokens": 915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 915,
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

_source line 24 · 2026-05-10T19:35:17.548Z_

<details><summary>↩ Tool result · `toolu_01HSdNc32TgbPkSRQKvo8Rxb`</summary>

```text
Web search results for query: "krafton-ai Offline-GRPO "offline RLVR" step-level advantage without rollouts"

Links: [{"title":"GitHub - krafton-ai/Offline-GRPO: Code for the blog post titled \"Continual Post-Training of LLMs via Offline GRPO for Mathematical Reasoning\" · GitHub","url":"https://github.com/krafton-ai/Offline-GRPO"},{"title":"Continual Post-Training via Offline GRPO — KRAFTON AI","url":"https://www.krafton.ai/blog/posts/2025-07-28-llm_post_training/grpo-en.html"},{"title":"[EN] Continual Post-Training of LLMs via Offline GRPO for Mathematical Reasoning | Krafton AI","url":"https://www.krafton.ai/blog/llm_post_training_en/"},{"title":"BLOG — KRAFTON AI","url":"https://www.krafton.ai/blog/"},{"title":"Krafton AI","url":"https://krafton-ai.github.io/blog/"},{"title":"Your Group-Relative Advantage Is Biased","url":"https://arxiv.org/html/2601.08521"},{"title":"Beyond Negative Rollouts: Positive-Only Policy Optimization with Implicit Negative Gradients","url":"https://arxiv.org/html/2605.06650"},{"title":"KRAFTON/OpenThinker3-Offline-GRPO-7B · Hugging Face","url":"https://huggingface.co/KRAFTON/OpenThinker3-Offline-GRPO-7B"},{"title":"[2603.21177] Prompt replay: speeding up grpo with on-policy reuse of high-signal prompts","url":"https://arxiv.org/abs/2603.21177"},{"title":"GRPO++: Tricks for Making RL Actually Work","url":"https://cameronrwolfe.substack.com/p/grpo-tricks"}]

Based on the search results, I found relevant information about Krafton's Offline-GRPO approach. Here's what the research reveals:

## Overview

Krafton proposes an offline alternative using teacher-generated trajectories and introduces a novel variant of Group Relative Policy Optimization (GRPO) that better captures high-quality reasoning traces—even when all outputs are positive.

## The Core Problem: Step-Level Advantage Without Rollouts

A key issue arises when naively applying GRPO's advantage calculation in the offline setting. When all rollout trajectories are positive and the mean reward is 1, the resulting advantage becomes 0, which means that no updates are made for those samples.

In their setup, the offline samples are sourced from a teacher model. Even if all teacher samples are positive, this does not necessarily mean the target model can solve the same problems perfectly. The current objective fails to capture this discrepancy, missing valuable learning opportunities from high-quality rollout trajectories.

## Solution Approach

In Offline GRPO, the model learns to move toward positive samples and away from negative ones. This property strengthens the model's reasoning ability by steering it away from logically incorrect rollout trajectories.

Additionally, offline GRPO is highly efficient as it recycles the teacher model's trajectories without direct rollout during the training process. They achieved performance comparable to or better than existing reinforcement learning methods while significantly reducing computational cost.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e43ae5a3-a513-43ac-84dc-54705fe57772",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a984e38911c2dde96",
  "type": "user",
  "uuid": "b8e1ae62-f50c-4575-8746-dd79298505ec",
  "sourceToolAssistantUUID": "e43ae5a3-a513-43ac-84dc-54705fe57772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-10T19:35:24.358Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C5DvivNnHeNasPophASHHE`</summary>

```json
{
  "query": "verl-agent supported environments ALFWorld WebShop Mind2Web web benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8e1ae62-f50c-4575-8746-dd79298505ec",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauT2RkoT6zx3mFqeXPiH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "123aada3-dbc5-433c-9433-bce2212fb0d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TNB6mMNXoTtpKrpTLFGFK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 911,
      "cache_read_input_tokens": 18385,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 911
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 18385,
          "cache_creation_input_tokens": 911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 911,
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

_source line 26 · 2026-05-10T19:35:29.870Z_

<details><summary>↩ Tool result · `toolu_01C5DvivNnHeNasPophASHHE`</summary>

```text
Web search results for query: "verl-agent supported environments ALFWorld WebShop Mind2Web web benchmarks"

Links: [{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengQ/verl-agent"},{"title":"verl-agent/README.md at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/blob/master/README.md"},{"title":"verl-agent/recipe/hgpo at master · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/tree/master/recipe/hgpo"},{"title":"AgentBench/docs/Introduction_en.md at main · THUDM/AgentBench","url":"https://github.com/THUDM/AgentBench/blob/main/docs/Introduction_en.md"},{"title":"ALFWorld","url":"https://alfworld.github.io/"},{"title":"AgentBench | AI Wiki","url":"https://aiwiki.ai/wiki/agentbench"},{"title":"GitHub - alfworld/alfworld: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning · GitHub","url":"https://github.com/alfworld/alfworld"},{"title":"AgentFly: Extensible and Scalable Reinforcement Learning for LM Agents","url":"https://arxiv.org/html/2507.14897v1"},{"title":"verl-agent - Browse /v0.1.0 at SourceForge.net","url":"https://sourceforge.net/projects/verl-agent.mirror/files/v0.1.0/"},{"title":"Releases · langfengQ/verl-agent","url":"https://github.com/langfengQ/verl-agent/releases"}]

Based on the search results, here's what I found about verl-agent's supported environments:

The supported environments are adapted from ALFWorld, Sokoban, SkyRL-Gym, Search-R1, Gym Cards, WebShop, and AppWorld.

Specifically regarding the environments you mentioned:

- **ALFWorld**: verl-agent offers embodied AI environments like ALFWorld, and the framework is designed to handle long-horizon tasks, with context length kept almost constant over time, making verl-agent highly scalable for long-horizon scenarios (e.g., 30–50 steps in ALFWorld).

- **WebShop**: verl-agent includes digital interface control tasks like WebShop and AppWorld.

- **Mind2Web**: The search results did not show Mind2Web as being directly supported by verl-agent, though Mind2Web is mentioned as a web browsing benchmark used in other frameworks like AgentBench.

The framework provides a gym-style interface with support for parallelized environments, enabling high-throughput rollouts and speeding up training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "123aada3-dbc5-433c-9433-bce2212fb0d8",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a984e38911c2dde96",
  "type": "user",
  "uuid": "5c526a6c-9304-4937-acbd-5aa416abde8d",
  "sourceToolAssistantUUID": "123aada3-dbc5-433c-9433-bce2212fb0d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-10T19:35:44.275Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SgKQpe68iL8Ex6oga25ckd`</summary>

```json
{
  "query": "WebAgent-R1 M-GRPO multi-turn GRPO step-level offline vs online rollout details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c526a6c-9304-4937-acbd-5aa416abde8d",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauT3LVZz4VBku7jxYCDz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "502f39ec-617d-4349-8bef-eaa31aab5a4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YcSp7VFKJ2ZbYGF7CAUjPR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 19296,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 852
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 19296,
          "cache_creation_input_tokens": 852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 852,
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

_source line 28 · 2026-05-10T19:35:51.298Z_

<details><summary>↩ Tool result · `toolu_01SgKQpe68iL8Ex6oga25ckd`</summary>

```text
Web search results for query: "WebAgent-R1 M-GRPO multi-turn GRPO step-level offline vs online rollout details"

Links: [{"title":"WEBAGENT-R1: Training Web Agents via End-to-End Multi-Turn","url":"https://arxiv.org/pdf/2505.16421"},{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://arxiv.org/html/2505.16421v1"},{"title":"[Literature Review] WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://www.themoonlight.io/en/review/webagent-r1-training-web-agents-via-end-to-end-multi-turn-reinforcement-learning"},{"title":"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/webagent-r1-training-web-agents-via-end"},{"title":"[2505.16421] WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://ar5iv.labs.arxiv.org/html/2505.16421v1"},{"title":"GitHub - weizhepei/WebAgent-R1: [EMNLP 2025] WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning · GitHub","url":"https://github.com/weizhepei/WebAgent-R1"},{"title":"WEBAGENT-R1: Training Web Agents via End-to-End Multi ...","url":"https://aclanthology.org/2025.emnlp-main.401.pdf"},{"title":"Online Multi-Turn Reinforcement Learning","url":"https://www.emergentmind.com/topics/online-multi-turn-reinforcement-learning"},{"title":"Paper page - WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning","url":"https://huggingface.co/papers/2505.16421"},{"title":"Generalization in Online Reinforcement Learning for Mobile Agents","url":"https://arxiv.org/html/2603.07432"}]

Based on the search results, here are the key details about WebAgent-R1's M-GRPO multi-turn GRPO framework and its step-level offline vs. online rollout approach:

## M-GRPO: Multi-Turn Extension of GRPO

WebAgent-R1 extends Group Relative Policy Optimization (GRPO) to multi-turn settings (M-GRPO) and employs a parallel trajectory rollout strategy. The end-to-end multi-turn RL framework trains web agents through online interactions guided by rule-based outcome rewards.

## Online Rollout vs. Offline Approach

WebAgent-R1 uses an **online** approach rather than offline rollout. Unlike off-policy RL that trains on data generated by older versions of the agent, WebAgent-R1's on-policy approach collects training data directly from the agent's current behavior, ensuring the learning process is better aligned with the agent's most recent actions, leading to more stable and effective learning.

## Asynchronous/Parallel Rollout Strategy

To efficiently generate trajectories for M-GRPO, multiple independent browser instances are instantiated in parallel, with each instance interacting with the agent independently, increasing sampling efficiency. The framework implements two key mechanisms: dynamic context compression to reduce memory overhead, and parallel trajectory rollout to improve sampling efficiency.

## Step-Level Details

For efficient LLM rollouts during M-GRPO, vLLM is used with a tensor parallel size of 1 and a GPU memory utilization ratio of 0.7, with rollout sampling performed with both temperature and top-p set to 1.0.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "502f39ec-617d-4349-8bef-eaa31aab5a4c",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a984e38911c2dde96",
  "type": "user",
  "uuid": "714782e6-f99f-442d-9008-1ed2dd9cec31",
  "sourceToolAssistantUUID": "502f39ec-617d-4349-8bef-eaa31aab5a4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-10T19:35:53.978Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019oc8nJnC8dnXBtC4JGFpX8`</summary>

```json
{
  "query": "GiGPO \"Group-in-Group Policy Optimization\" offline step-level advantage agent training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "714782e6-f99f-442d-9008-1ed2dd9cec31",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauT4v6RyGhy37VCGR4Qj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d174234d-310d-4d61-a98c-aa9806bd31bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tnuwuoi49ZwGjpNcUMwSPW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 20148,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1047
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 20148,
          "cache_creation_input_tokens": 1047,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1047,
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

_source line 30 · 2026-05-10T19:36:06.891Z_

<details><summary>↩ Tool result · `toolu_019oc8nJnC8dnXBtC4JGFpX8`</summary>

```text
Web search results for query: "GiGPO "Group-in-Group Policy Optimization" offline step-level advantage agent training"

Links: [{"title":"[2505.10978] Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/abs/2505.10978"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training | OpenReview","url":"https://openreview.net/forum?id=QXEhBMNrCW"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978v1"},{"title":"GitHub - langfengQ/verl-agent: verl-agent is an extension of veRL, designed for training LLM/VLM agents via RL. verl-agent is also the official code for paper \"Group-in-Group Policy Optimization for LLM Agent Training\" · GitHub","url":"https://github.com/langfengq/verl-agent"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=reinforcement-learning-based+policy+training"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training | alphaXiv","url":"https://www.alphaxiv.org/overview/2505.10978v1"},{"title":"Paper page - Group-in-Group Policy Optimization for LLM Agent Training","url":"https://huggingface.co/papers/2505.10978"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training | Request PDF","url":"https://www.researchgate.net/publication/391857132_Group-in-Group_Policy_Optimization_for_LLM_Agent_Training"},{"title":"NeurIPS Poster Group-in-Group Policy Optimization for LLM Agent Training","url":"https://neurips.cc/virtual/2025/poster/118123"}]

Based on my search results, here's comprehensive information about GiGPO (Group-in-Group Policy Optimization):

## Overview

GiGPO is a novel RL algorithm that achieves fine-grained credit assignment for LLM agents while preserving the appealing properties of group-based RL: critic-free, low memory, and stable convergence.

## Two-Level Structure

GiGPO introduces a two-level structure for estimating relative advantage: at the episode-level, GiGPO computes macro relative advantages based on groups of complete trajectories; at the step-level, GiGPO introduces an anchor state grouping mechanism that retroactively constructs step-level groups by identifying repeated environment states across trajectories.

The key insight behind GiGPO is that, under identical tasks and initial environment conditions, many trajectories within the group encounter the same states multiple times due to ineffective actions or loops, such as revisiting the same webpage, room, or game scene. These shared states provide a natural basis for step-level group construction and computing more granular advantage estimates.

## Key Benefits

This hierarchical structure effectively captures both global trajectory quality and local step effectiveness without relying on auxiliary models or additional rollouts.

## Performance Results

GiGPO delivers fine-grained per-step credit signals, achieves performance gains of > 12% on ALFWorld and > 9% on WebShop over GRPO, and obtains superior performance on QA tasks (42.1% on 3B and 47.2% on 7B): all while maintaining the same GPU memory overhead, identical LLM rollout, and incurring little to no additional time cost.

## Implementation

GiGPO has been implemented in verl-agent, which includes implementations of various RL algorithms, such as GRPO, PPO, DAPO, GSPO, RLOO and their new state-of-the-art algorithm GiGPO.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d174234d-310d-4d61-a98c-aa9806bd31bf",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a984e38911c2dde96",
  "type": "user",
  "uuid": "241ab751-60b4-47f6-8bae-cb8a2ae0c591",
  "sourceToolAssistantUUID": "d174234d-310d-4d61-a98c-aa9806bd31bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-10T19:36:09.220Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NLhjeTSz71DJjubztENZ7r`</summary>

```json
{
  "query": "GRPO step-level reward cached HTML offline web agent action prediction advantage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "241ab751-60b4-47f6-8bae-cb8a2ae0c591",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauT64ht5pjZaRDP4XmSN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ccc4a1ef-9d81-466d-bc4d-9766464c1d65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrGhzTUxq5MePAgNZzj9VY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 21195,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1076
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 21195,
          "cache_creation_input_tokens": 1076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1076,
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

_source line 32 · 2026-05-10T19:36:17.637Z_

<details><summary>↩ Tool result · `toolu_01NLhjeTSz71DJjubztENZ7r`</summary>

```text
Web search results for query: "GRPO step-level reward cached HTML offline web agent action prediction advantage"

Links: [{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with Policy Entropy","url":"https://arxiv.org/html/2508.04349v1"},{"title":"GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with...","url":"https://arxiv.org/abs/2508.04349"},{"title":"GRPO Trainer · Hugging Face","url":"https://huggingface.co/docs/trl/main/en/grpo_trainer"},{"title":"GRPO in Reinforcement Learning Explained | DigitalOcean","url":"https://www.digitalocean.com/community/conceptual-articles/group-relative-policy-optimization-reinforcement-learning"},{"title":"Group Relative Policy Optimization (GRPO) — verl documentation","url":"https://verl.readthedocs.io/en/latest/algo/grpo.html"},{"title":"GRPO++: Tricks for Making RL Actually Work","url":"https://cameronrwolfe.substack.com/p/grpo-tricks"},{"title":"GTPO AND GRPO-S: TOKEN AND SEQUENCE-LEVEL REWARD SHAPING WITH...","url":"https://openreview.net/forum?id=CFF6zXErgS"},{"title":"𝜆-GRPO: Unifying the GRPO Frameworks with Learnable Token Preferences","url":"https://arxiv.org/html/2510.06870v2"},{"title":"Training-Free Group Relative Policy Optimization","url":"https://arxiv.org/html/2510.08191v1"}]

Based on the search results, I can provide you with information about Group Relative Policy Optimization (GRPO) and related concepts:

## GRPO Overview

Group Relative Policy Optimization (GRPO) is an improvement over Proximal Policy Optimization (PPO), specifically designed to make reinforcement learning for large language models (LLMs) more efficient. The main difference is that GRPO removes the need for a separate value function model (which PPO requires), instead using relative comparisons within groups of outputs to calculate advantages, making GRPO more lightweight in terms of computation and memory.

## Step-Level and Reward-Related Features

GRPO algorithms remain constrained by a coarse-grained credit assignment paradigm, where all tokens within the same response receive the identical reward, but this can be addressed through Dynamic Entropy Weighting to systematically define entropy-based weight ratios and redistribute rewards to get fine-grained rewards.

GRPO can be extended to handle process rewards (e.g., after each reasoning step) by normalizing rewards based on the mean and standard deviation of all process rewards observed in the group and computing the advantage of each token as the sum of normalized rewards for following steps in the reasoning trajectory.

## Advantage Calculation

The advantage for completion i is calculated by first subtracting the mean reward over the group from r_i, then dividing this difference by the standard deviation of rewards over the group.

## Web Agent Applications

Training-Free Group Relative Policy Optimization is a cost-effective solution that enhances LLM agent performance without any parameter updates, leveraging the group relative semantic advantage instead of numerical ones within each group of rollouts, with knowledge serving as the learned token prior. It demonstrates significant improvements on web searching tasks and mathematical reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ccc4a1ef-9d81-466d-bc4d-9766464c1d65",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a984e38911c2dde96",
  "type": "user",
  "uuid": "f6d4fb82-18fa-4a6b-8474-d15b6bf39bed",
  "sourceToolAssistantUUID": "ccc4a1ef-9d81-466d-bc4d-9766464c1d65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-10T19:36:20.253Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LzhTAGftwmwrmQ9P2sb321`</summary>

```json
{
  "query": "DynaWeb model-based reinforcement learning web agents arXiv 2601"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6d4fb82-18fa-4a6b-8474-d15b6bf39bed",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauT6rj5rcMZtpJoJMyGn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "919d3d3f-d098-44b2-a080-6d7017320b5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q1HtSin2WbVWTQijbHs7fa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 946,
      "cache_read_input_tokens": 22271,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 946
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 22271,
          "cache_creation_input_tokens": 946,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 946,
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

_source line 34 · 2026-05-10T19:36:28.294Z_

<details><summary>↩ Tool result · `toolu_01LzhTAGftwmwrmQ9P2sb321`</summary>

```text
Web search results for query: "DynaWeb model-based reinforcement learning web agents arXiv 2601"

Links: [{"title":"DynaWeb: Model-Based Reinforcement Learning of Web Agents","url":"https://arxiv.org/html/2601.22149v1"},{"title":"DynaWeb DynaWeb: Model-Based Reinforcement Learning of Web Agents Hang Ding1","url":"https://arxiv.org/pdf/2601.22149"},{"title":"[2601.22149] DynaWeb: Model-Based Reinforcement Learning of Web Agents","url":"https://arxiv.org/abs/2601.22149"},{"title":"(PDF) DynaWeb: Model-Based Reinforcement Learning of Web Agents","url":"https://www.researchgate.net/publication/400237351_DynaWeb_Model-Based_Reinforcement_Learning_of_Web_Agents"},{"title":"Dynaweb Advances Web Agent Training Via Model-Based Reinforcement Learning","url":"https://quantumzeitgeist.com/reinforcement-training-dynaweb-advances-web-agent-model/"},{"title":"DynaWeb: Scalable RL for Web Agents","url":"https://www.emergentmind.com/topics/dynaweb"},{"title":"GUI Agents with Reinforcement Learning: Toward Digital Inhabitants","url":"https://arxiv.org/html/2604.27955"},{"title":"DynaWeb: Model-Based Reinforcement Learning of Web Agents | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2601.22149"},{"title":"Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents","url":"https://arxiv.org/html/2506.00320v1"},{"title":"Large Language Models for Reinforcement Learning","url":"https://www.preprints.org/manuscript/202603.0229"}]

I found comprehensive information about DynaWeb. Here's what the research shows:

## Overview

DynaWeb is a novel MBRL framework that trains web agents through interacting with a web world model trained to predict naturalistic web page representations given agent actions.

## Problem It Addresses

The effectiveness of online RL for web agents is fundamentally constrained by the cost and risk of real-environment interaction, as collecting large-scale, on-policy experience requires agents to interact directly with the live internet, which is inefficient, expensive, and difficult to control at scale.

## Core Approach

Inspired by the Dyna architecture and imagination-based learning frameworks such as Dreamer, DynaWeb is an MBRL framework that treats the world model as a controllable synthetic web environment that can replace or augment costly real interaction.

An LLM-based web world model functions as a learned web server: conditioned on the current page representation and an agent action, it predicts realistic next-state page representations and provides task-level feedback signals for policy optimization.

## Training Strategy

DynaWeb combines two complementary sources of training experience. In addition to policy-driven imagined rollouts generated by the web world model, it directly incorporates fully real expert trajectories sampled from existing training data. During training, real expert trajectories are randomly interleaved with imagined rollouts and real on-policy interaction.

## Results

Experiments conducted on the challenging WebArena and WebVoyager benchmarks demonstrate that DynaWeb consistently and significantly improves the performance of state-of-the-art open-source web agent models.

The paper was published on arXiv on January 29, 2026 (arxiv:2601.22149).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "919d3d3f-d098-44b2-a080-6d7017320b5e",
  "isSidechain": true,
  "promptId": "0d97b11e-d4c9-4f3b-90f9-fc79b76fa17e",
  "agentId": "a984e38911c2dde96",
  "type": "user",
  "uuid": "db28e3bd-90cd-48a5-b651-d37176aeae03",
  "sourceToolAssistantUUID": "919d3d3f-d098-44b2-a080-6d7017320b5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-10T19:37:26.415Z_

Now I have comprehensive information to synthesize a thorough answer. Here is my report:

---

## Feasibility of GRPO-Style RL Training on Mind2Web

### 1. Has Anyone Done RL (Not Just SFT) on Mind2Web?

**No direct RL training on Mind2Web has been published.** Mind2Web remains primarily used for SFT and offline evaluation. All RL-based web agent training efforts (WebAgent-R1, Mano, WebRL, VeriEnv) use interactive environments like WebArena, WebShop, or custom recreated websites -- not Mind2Web's cached HTML snapshots.

### 2. Can GRPO Work Offline?

**Yes, and there is explicit prior work.** Krafton AI published [Offline-GRPO](https://github.com/krafton-ai/Offline-GRPO), which uses teacher-generated trajectories instead of on-policy rollouts. The key insight: you replace the "sample from the current policy" step with pre-existing trajectories and still compute group-relative advantages. They found it achieves performance comparable to online GRPO while significantly reducing cost. However, a known limitation is that when all samples in a group are positive (mean reward = 1), the advantage collapses to zero and no learning signal is produced. They address this with a modified advantage formulation.

### 3. Interactive Versions of Mind2Web

Three interactive variants exist:
- **Mind2Web-Live** (part of WebCanvas): 542 tasks with live website evaluation, using key-node states for reproducible assessment. Designed for evaluation, not RL training loops.
- **Online-Mind2Web**: 300 tasks across 136 websites, focused on evaluation in live environments.
- **Mind2Web-2**: 130 long-horizon tasks requiring real-time browsing. Also evaluation-focused.

None of these are designed as RL training environments (no reset/reward API), but they demonstrate live web interaction is possible for the Mind2Web task distribution.

### 4. The VeriEnv / Recreated Websites Paper (arXiv:2603.10505)

[Safe and Scalable Web Agent Learning via Recreated Websites](https://arxiv.org/abs/2603.10505) (March 2026) proposes using LLMs to clone real websites into fully executable, verifiable synthetic environments with a Python SDK for programmatic reward verification. This directly addresses the gap: you can potentially recreate Mind2Web's target websites as interactive environments for RL. This is the most promising path for converting Mind2Web into an RL-compatible setting.

### 5. WebAgent-R1 (arXiv:2505.16421)

WebAgent-R1 extends GRPO to multi-turn settings via **M-GRPO** and trains on **WebArena-Lite** (not Mind2Web). Key details:
- It is **fundamentally online**: it instantiates parallel browser instances and does on-policy rollouts.
- Uses binary task-success rewards (not step-level rewards).
- Advantages are computed across groups of complete trajectories for the same task.
- Boosted Qwen-2.5-3B from 6.1% to 33.9% success rate.
- **Cannot be applied to cached HTML** -- it requires live environment interaction.

### 6. Mano Web Agent

Mano uses a **three-stage pipeline**: (i) SFT on offline demonstrations, (ii) **Offline RL with GRPO** on static trajectories with decomposed rewards, (iii) **Online RL with GRPO** via simulated environment interaction. The offline RL stage is directly relevant -- Mano demonstrates that GRPO can work on static trajectory data before transitioning to online RL for further improvement.

### 7. verl-agent Framework

verl-agent (the official implementation of [GiGPO](https://arxiv.org/abs/2505.10978)) supports ALFWorld, WebShop, Sokoban, Search-R1, and AppWorld. **Mind2Web is not currently supported.** However, verl-agent provides a gym-style interface, so adding a Mind2Web environment wrapper is architecturally feasible.

---

## Core Question: Can Step-Level GRPO Work on Cached HTML?

**Yes, with important caveats.** Here is the practical approach:

**What works:** At each step in a Mind2Web trajectory, you have a cached HTML snapshot and a ground-truth action. You can:
1. Sample N action predictions from the policy given the HTML observation.
2. Compare each prediction against the ground-truth using element matching (element_acc) and action matching (step_acc) as binary rewards.
3. Compute group-relative advantages across the N samples.
4. Update the policy with the GRPO objective.

This is essentially **offline step-level GRPO** and is well-supported by precedent (Krafton's Offline-GRPO, Mano's Stage 2).

**What you lose:**
- **No trajectory-level signal**: Since you cannot roll out into the next state, you can only give step-level rewards, not outcome-based rewards (task success). You are training a step-level policy, not an end-to-end agent.
- **No distribution shift correction**: As your policy improves, its action distribution diverges from what was cached, but the HTML observations remain frozen. You cannot see how the environment would have changed if the agent had taken a different action. This is the classic offline RL problem.
- **No exploration**: The agent never discovers new states. It only learns to match ground-truth actions on cached observations.

**The GiGPO insight is relevant here:** GiGPO's "anchor state grouping" retroactively constructs step-level groups by identifying repeated environment states across trajectories. In Mind2Web, if multiple tasks visit the same or similar pages, you could group actions across trajectories at shared states for better advantage estimation.

---

## Recommended Practical Approach

**Tier 1 (Easiest, immediate):** Step-level offline GRPO on Mind2Web cached HTML. Sample multiple actions per step, reward based on ground-truth match, compute advantages within the group. Use Krafton's Offline-GRPO codebase or HuggingFace TRL's GRPOTrainer. This is essentially reward-weighted SFT with a GRPO-style advantage, and will give you better-than-SFT performance on the step prediction task.

**Tier 2 (Moderate effort):** Use verl-agent with a custom Mind2Web gym wrapper. You would present cached HTML as observations and compute step-level rewards. This gives you access to GiGPO, DAPO, and other algorithms out of the box.

**Tier 3 (High effort, highest ceiling):** Use the VeriEnv framework to recreate Mind2Web target websites as interactive environments, then do full online M-GRPO (a la WebAgent-R1) with trajectory-level rewards. This is the only approach that gives you true end-to-end RL with exploration.

**Tier 1.5 (Hybrid, recommended):** Do offline GRPO on Mind2Web for warm-start, then transition to online RL on WebArena or recreated websites (following Mano's three-stage approach). This leverages Mind2Web's data diversity while still getting the benefits of online RL.

---

## Bottom Line

GRPO does **not** fundamentally require interactive rollouts. Offline GRPO on cached HTML is feasible and has precedent. However, you will be limited to step-level credit assignment (no trajectory rewards) and will face distribution shift. The strongest approach combines offline GRPO on Mind2Web as a warm-start with online RL on interactive environments for end-to-end policy improvement.

Sources:
- [Krafton Offline-GRPO GitHub](https://github.com/krafton-ai/Offline-GRPO)
- [Krafton Offline-GRPO Blog Post](https://www.krafton.ai/blog/posts/2025-07-28-llm_post_training/grpo-en.html)
- [WebAgent-R1 (arXiv:2505.16421)](https://arxiv.org/abs/2505.16421)
- [Mano Technical Report (arXiv:2509.17336)](https://arxiv.org/html/2509.17336v1)
- [GiGPO / verl-agent (arXiv:2505.10978)](https://arxiv.org/abs/2505.10978)
- [verl-agent GitHub](https://github.com/langfengQ/verl-agent)
- [Safe and Scalable Web Agent Learning via Recreated Websites (arXiv:2603.10505)](https://arxiv.org/abs/2603.10505)
- [DynaWeb: Model-Based RL of Web Agents (arXiv:2601.22149)](https://arxiv.org/abs/2601.22149)
- [Mind2Web-Live / WebCanvas](https://www.emergentmind.com/topics/mind2web-live)
- [Online-Mind2Web](https://github.com/OSU-NLP-Group/Online-Mind2Web)
- [Training-Free GRPO (arXiv:2510.08191)](https://arxiv.org/abs/2510.08191)
- [veRL GRPO Documentation](https://verl.readthedocs.io/en/latest/algo/grpo.html)
- [GRPO Overview (Cameron Wolfe)](https://cameronrwolfe.substack.com/p/grpo)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db28e3bd-90cd-48a5-b651-d37176aeae03",
  "isSidechain": true,
  "agentId": "a984e38911c2dde96",
  "requestId": "req_011CauT7eD31S5ts1UsNBuW3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84c47db3-b587-44ac-81f1-4a83ae8b4983",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3d337051-3878-4cca-931f-7fbd1814db6b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019EKcoh2FV2aHUJHtSHoYjZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 957,
      "cache_read_input_tokens": 23217,
      "output_tokens": 2278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 957
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2278,
          "cache_read_input_tokens": 23217,
          "cache_creation_input_tokens": 957,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 957,
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
