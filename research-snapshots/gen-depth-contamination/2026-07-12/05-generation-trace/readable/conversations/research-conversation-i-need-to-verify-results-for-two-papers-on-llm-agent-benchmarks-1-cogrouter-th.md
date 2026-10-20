# Research conversation: I need to verify results for two papers on LLM agent benchmarks: 1. CogRouter / "Think Fast and Slow" (arXiv 2602.12662,

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad34a9275b82b1c42.jsonl`
- **Structured JSON:** [`254d4f89868fcf26f522.json`](../../sessions/25/254d4f89868fcf26f522.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

65 recorded events

### User

_source line 1 · 2026-05-12T00:32:01.087Z_

I need to verify results for two papers on LLM agent benchmarks:

1. CogRouter / "Think Fast and Slow" (arXiv 2602.12662, Feb 2026):
   - Claimed: ALFWorld 92.5%, ScienceWorld 84.6 score / 72.0% SR with Qwen2.5-7B
   - Uses CoSFT + CoPO training, four cognitive levels
   - Code at github.com/rhyang2021/CogRouter
   
2. Skill1 (arXiv 2605.06130, May 2026):
   - Claimed: ALFWorld 97.5% via unified skill evolution with RL
   - Current ALFWorld SOTA

Also search for:
- "ScienceWorld SOTA 2026 results" - what is the actual current SOTA?
- "ALFWorld SOTA 2026 results" - what is the actual current SOTA?
- Any other recent ScienceWorld papers from 2026

Use WebSearch and WebFetch to verify. Report exact numbers found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "fb4d380c-0f7b-4187-96c8-2393ad759cd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T00:32:01.090Z_

```json
{
  "parentUuid": "fb4d380c-0f7b-4187-96c8-2393ad759cd1",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
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
  "uuid": "900ac0e3-b285-4e10-a35b-10ee7971e7c1",
  "timestamp": "2026-05-12T00:32:01.090Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T00:32:03.438Z_



I'll start by loading the WebSearch and WebFetch tools, then conduct the searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "900ac0e3-b285-4e10-a35b-10ee7971e7c1",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjTijpRFU81cD9rDLA4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd871c48-6c25-4425-a72e-409caacba7e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016BpG74a6b73KNDk7kbqpwS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 805,
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

_source line 4 · 2026-05-12T00:32:03.881Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PcQ8guHQ4MaEcZV4DpS297`</summary>

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
  "parentUuid": "dd871c48-6c25-4425-a72e-409caacba7e1",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjTijpRFU81cD9rDLA4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36625d5e-09e3-4652-a7ff-7366edb833c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016BpG74a6b73KNDk7kbqpwS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 805,
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

### Tool result

_source line 5 · 2026-05-12T00:32:03.884Z_

<details><summary>↩ Tool result · `toolu_01PcQ8guHQ4MaEcZV4DpS297`</summary>

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
  "parentUuid": "36625d5e-09e3-4652-a7ff-7366edb833c5",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "740d0c49-b4fa-4878-9be2-92cfe2751759",
  "sourceToolAssistantUUID": "36625d5e-09e3-4652-a7ff-7366edb833c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T00:32:06.444Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "740d0c49-b4fa-4878-9be2-92cfe2751759",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjTw7i9YAq67jxAXgq9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b205c15c-0d03-4034-bf66-712bba7d8892",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BphUnphMjB6KYCMosWrCVy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 7 · 2026-05-12T00:32:08.512Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V8siNYQyNAMSok48J4RDRT`</summary>

```json
{
  "query": "CogRouter \"Think Fast and Slow\" arXiv 2602.12662 ALFWorld ScienceWorld results 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b205c15c-0d03-4034-bf66-712bba7d8892",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjTw7i9YAq67jxAXgq9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b09faa3f-4c3c-4a70-aebe-c2fb4b8797b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BphUnphMjB6KYCMosWrCVy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 8 · 2026-05-12T00:32:08.778Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017VEbixqe1bZ8S3B7ABg4gL`</summary>

```json
{
  "query": "Skill1 arXiv 2605.06130 ALFWorld skill evolution reinforcement learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b09faa3f-4c3c-4a70-aebe-c2fb4b8797b5",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjTw7i9YAq67jxAXgq9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aac58835-0883-43ff-ab8d-b32f3b90c398",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BphUnphMjB6KYCMosWrCVy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 9 · 2026-05-12T00:32:09.251Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KjvuEkxDL9PnssKGLmLktS`</summary>

```json
{
  "query": "ScienceWorld SOTA 2026 benchmark results LLM agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aac58835-0883-43ff-ab8d-b32f3b90c398",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjTw7i9YAq67jxAXgq9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14b91125-80ba-47b6-ad66-426f6e140b08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BphUnphMjB6KYCMosWrCVy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1909,
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

_source line 10 · 2026-05-12T00:32:09.660Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pv2wKmL6KXX5AUBLSMVTGg`</summary>

```json
{
  "query": "ALFWorld SOTA 2026 benchmark results LLM agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14b91125-80ba-47b6-ad66-426f6e140b08",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjTw7i9YAq67jxAXgq9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32ae0506-b08c-4798-8f37-07ac8790931d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BphUnphMjB6KYCMosWrCVy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1909,
      "cache_read_input_tokens": 9028,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 252,
          "cache_read_input_tokens": 9028,
          "cache_creation_input_tokens": 1909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1909,
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

_source line 11 · 2026-05-12T00:32:15.029Z_

<details><summary>↩ Tool result · `toolu_017VEbixqe1bZ8S3B7ABg4gL`</summary>

```text
Web search results for query: "Skill1 arXiv 2605.06130 ALFWorld skill evolution reinforcement learning 2026"

Links: [{"title":"[2605.06130] Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning","url":"https://arxiv.org/abs/2605.06130"},{"title":"Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning","url":"https://arxiv.org/html/2605.06130v1"},{"title":"Paper page - Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning","url":"https://huggingface.co/papers/2605.06130"},{"title":"Explore | alphaXiv","url":"https://www.alphaxiv.org/"},{"title":"Unified Evolution of Skill-Augmented Agents via Reinforcement ...","url":"https://bytez.com/docs/arxiv/2605.06130/paper"},{"title":"Skill1: Optimizing LLM Agent Skills with RL - YouTube","url":"https://www.youtube.com/watch?v=LS4-ZDG-J90"},{"title":"SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning","url":"https://arxiv.org/html/2602.08234"},{"title":"GitHub - aiming-lab/SkillRL: SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning · GitHub","url":"https://github.com/aiming-lab/SkillRL"},{"title":"Skill1: Unified Co-Evolution of Skill-Augmented Reinforcement Learning Agents - YouTube","url":"https://www.youtube.com/watch?v=oiG4dPaBAMw"},{"title":"[2602.08234] SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning","url":"https://arxiv.org/abs/2602.08234"}]

Based on the search results, I found the paper you're looking for. Here's what the research is about:

## Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning (arXiv 2605.06130)

Skill1 is a framework that trains a single policy to co-evolve skill selection, utilization, and distillation toward a shared task-outcome objective.

**Key Components:**

The agent selects a relevant skill, utilizes it during execution, and distills new skills from experience. The policy generates a query to search the skill library, re-ranks candidates to select one, solves the task conditioned on it, and distills a new skill from the trajectory.

**Unified Learning Signal:**

All learning derives from a single task-outcome signal, where its low-frequency trend credits selection and its high-frequency variation credits distillation.

**Experimental Results:**

On ALFWorld, Skill1 reaches 97.5% average success rate, surpassing the previous best RetroAgent by 2.6 points and ranking first on 5 out of 6 task types. Experiments on ALFWorld and WebShop show that Skill1 outperforms prior skill-based and reinforcement learning baselines.

The paper was posted to arXiv very recently (4 days ago as of the search results).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aac58835-0883-43ff-ab8d-b32f3b90c398",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "2c1cd605-459e-4765-90de-fdc6992d7794",
  "sourceToolAssistantUUID": "aac58835-0883-43ff-ab8d-b32f3b90c398",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T00:32:15.140Z_

<details><summary>↩ Tool result · `toolu_01V8siNYQyNAMSok48J4RDRT`</summary>

```text
Web search results for query: "CogRouter "Think Fast and Slow" arXiv 2602.12662 ALFWorld ScienceWorld results 2026"

Links: [{"title":"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/html/2602.12662"},{"title":"[2602.12662] Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/abs/2602.12662"},{"title":"[2602.12662v1] Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/abs/2602.12662v1"},{"title":"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiviq.substack.com/p/think-fast-and-slow-step-level-cognitive"},{"title":"Thinker: Learning to Think Fast and Slow","url":"https://arxiv.org/html/2505.21097v1"},{"title":"[2505.21097] Thinker: Learning to Think Fast and Slow","url":"https://arxiv.org/abs/2505.21097"},{"title":"[2505.21097v2] Thinker: Learning to Think Fast and Slow","url":"https://arxiv.org/abs/2505.21097v2"},{"title":"Machine Thinking, Fast and Slow - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1364661320302229"},{"title":"[2511.16670] Learning to Think Fast and Slow for Visual Language Models","url":"https://arxiv.org/abs/2511.16670"}]

I found the research paper you were looking for. Here are the key results:

## Paper Summary

CogRouter is a framework that trains agents to dynamically adapt cognitive depth at each step, grounded in ACT-R theory, with four hierarchical cognitive levels ranging from instinctive responses to strategic planning.

## ALFWorld and ScienceWorld Results

Using Qwen2.5-7B as the base model, CogRouter achieves an 82.3% average success rate, significantly outperforming GPT-4o (+40.3%), OpenAI-o3 (+18.3%), and GRPO (+14.0%), while reducing token consumption by 62% compared to GRPO.

With Qwen2.5-7B, it achieves an average success rate of 82.3%, surpassing larger frontier models such as GPT-4o (+40.3%) and OpenAI-o3 (+18.3%), as well as both offline and online methods, including ETO (+36.8%) and GRPO (+14.0%).

## Training Approach

The two-stage training approach includes Cognition-aware Supervised Fine-tuning (CoSFT) to instill stable level-specific patterns, and Cognition-aware Policy Optimization (CoPO) for step-level credit assignment via confidence-aware advantage reweighting.

The paper was published on arXiv on February 13, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b09faa3f-4c3c-4a70-aebe-c2fb4b8797b5",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "e2cb961b-ba17-4908-8ab0-f005f2eb1e84",
  "sourceToolAssistantUUID": "b09faa3f-4c3c-4a70-aebe-c2fb4b8797b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T00:32:16.657Z_

<details><summary>↩ Tool result · `toolu_01Pv2wKmL6KXX5AUBLSMVTGg`</summary>

```text
Web search results for query: "ALFWorld SOTA 2026 benchmark results LLM agent"

Links: [{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"AI evals are becoming the new compute bottleneck","url":"https://huggingface.co/blog/evaleval/eval-costs-bottleneck"},{"title":"AI Coding Benchmark Leaderboard 2026: Code Generation and SWE-bench | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/code-generation"},{"title":"[2311.16714] Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld","url":"https://arxiv.org/abs/2311.16714"},{"title":"Codesota — the open, callable registry of SOTA","url":"https://www.codesota.com/"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"GitHub - stevenyangyj/Emma-Alfworld: Official code for the paper: Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld · GitHub","url":"https://github.com/stevenyangyj/Emma-Alfworld"},{"title":"Agent2 RL-Bench: Can LLM Agents Engineer Agentic RL Post-Training?","url":"https://arxiv.org/html/2604.10547v1"},{"title":"Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings","url":"https://llm-stats.com/leaderboards/open-llm-leaderboard"}]

Based on the search results, I found some relevant information about ALFWorld and LLM agent benchmarks in 2026, though there isn't a specific dedicated "SOTA 2026" benchmark focused solely on ALFWorld.

Here's what the search revealed:

## ALFWorld Benchmark Context

ALFWorld represents an interactive long-horizon task with stateful environments. It has been used in recent agent evaluation research, including a 2026 study called Agent2 RL-Bench.

## Recent ALFWorld Results

An RL-only ALFWorld result achieved 91.79, serving as primary evidence that an agent can engineer an online RL loop in the Agent2 RL-Bench paper from 2026.

Additionally, there was an earlier notable result where EMMA's (Embodied Multi-Modal Agent) evaluations on the ALFWorld benchmark showed 20%-70% improvement in the success rate compared to SOTA VLM-based agents.

## Broader Agent Benchmarking Landscape

The Holistic Agent Leaderboard (HAL) runs standardized agent harnesses across nine benchmarks covering coding, web navigation, science tasks, and customer service, with shared scaffolds and centralized cost tracking.

The search results indicate that ALFWorld is one component of broader agent evaluation efforts in 2026, but there doesn't appear to be a single consolidated "ALFWorld SOTA 2026" benchmark with published leaderboard results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32ae0506-b08c-4798-8f37-07ac8790931d",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "4d26fa57-4970-49c7-b8b4-15430d26b051",
  "sourceToolAssistantUUID": "32ae0506-b08c-4798-8f37-07ac8790931d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T00:32:18.627Z_

<details><summary>↩ Tool result · `toolu_01KjvuEkxDL9PnssKGLmLktS`</summary>

```text
Web search results for query: "ScienceWorld SOTA 2026 benchmark results LLM agent"

Links: [{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"AI Coding Benchmark Leaderboard 2026: Code Generation and SWE-bench | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/code-generation"},{"title":"Codesota — the open, callable registry of SOTA","url":"https://www.codesota.com/"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"LongevityBench: Are SotA LLMs ready for aging research? | bioRxiv","url":"https://www.biorxiv.org/content/10.64898/2026.01.12.698650v1.full"},{"title":"Longevity Bench: Are SotA LLMs ready for aging research? | bioRxiv","url":"https://www.biorxiv.org/content/10.64898/2026.01.12.698650v3"},{"title":"AI evals are becoming the new compute bottleneck","url":"https://huggingface.co/blog/evaleval/eval-costs-bottleneck"},{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"AI Trends (May 2026) — AI Trend Analysis, LLM Statistics & Industry Insights","url":"https://llm-stats.com/ai-trends"}]

Based on the web search results, I found information about benchmark results from 2026, though not specifically about a "ScienceWorld" benchmark. Here's what I found about 2026 LLM agent benchmark results:

## Key 2026 Benchmark Findings

A 2026 Berkeley RDI study found that eight major agent benchmarks — including SWE-bench Verified, Terminal-Bench, WebArena, OSWorld, GAIA, and FieldWorkArena — could be exploited to near-perfect scores without solving any tasks. Failure modes included leaked reference answers, unsanitized eval(), prompt-injectable LLM judges, and scoring functions that skip correctness checks entirely.

## Agent Benchmarking Infrastructure

The Holistic Agent Leaderboard (Kapoor et al., ICLR 2026) runs standardized agent harnesses across nine benchmarks covering coding, web navigation, science tasks, and customer service, with shared scaffolds and centralized cost tracking.

ResearchGym (ICLR 2026) makes the agent run actual ML research, with five test tasks (39 sub-tasks) drawn from ACL, ICLR, and ICML papers, where the agent has to propose hypotheses, train models, and beat the original authors' baselines.

## Top Performing Models

The aggregate ranking identified OpenAI's o3 as the top-performing model with an average rank of 4.65, followed by GPT-5 (5.06) and Gemini 3 Pro (5.59).

However, I didn't find specific results for a benchmark called "ScienceWorld" in these results. If you're looking for more specific information about that particular benchmark, you may want to check academic repositories or the official benchmark documentation directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14b91125-80ba-47b6-ad66-426f6e140b08",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "c4e61b4c-c51e-4043-ad3b-0c80d9f22692",
  "sourceToolAssistantUUID": "14b91125-80ba-47b6-ad66-426f6e140b08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-12T00:32:22.000Z_

Now let me fetch the actual paper pages to get exact numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4e61b4c-c51e-4043-ad3b-0c80d9f22692",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjV1f5xwXBhG4gXGuq4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a327ac2-1c67-4111-8df3-224357dec536",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018h38GzHHjCBhwxUGxdJHE6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 859,
      "cache_creation_input_tokens": 2860,
      "cache_read_input_tokens": 10937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2860,
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

_source line 16 · 2026-05-12T00:32:25.831Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NfAhgyy3qANMzRXMCF1SQM`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.12662",
  "prompt": "Extract ALL benchmark results with exact numbers. Specifically find: ALFWorld success rate, ScienceWorld score and success rate (SR). What base model is used (Qwen2.5-7B)? List every result table entry with exact percentages/scores. Also note what CoSFT and CoPO stand for and the four cognitive levels."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a327ac2-1c67-4111-8df3-224357dec536",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjV1f5xwXBhG4gXGuq4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c50d84b-e983-4b2b-b3d2-a4166d1a964b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018h38GzHHjCBhwxUGxdJHE6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 859,
      "cache_creation_input_tokens": 2860,
      "cache_read_input_tokens": 10937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2860,
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

_source line 17 · 2026-05-12T00:32:27.711Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TJKGih8EhDfbGUXyL1fuSq`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.06130",
  "prompt": "Extract ALL benchmark results with exact numbers. Specifically find: ALFWorld success rate percentage, WebShop results. What is the exact ALFWorld number? Is 97.5% mentioned? What base model is used? List all comparison baselines and their numbers too."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c50d84b-e983-4b2b-b3d2-a4166d1a964b",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjV1f5xwXBhG4gXGuq4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0baf488d-4ebd-45be-855c-e78efb53fc01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018h38GzHHjCBhwxUGxdJHE6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 859,
      "cache_creation_input_tokens": 2860,
      "cache_read_input_tokens": 10937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2860,
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

_source line 18 · 2026-05-12T00:32:29.108Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UQDnJsrFiJAaumFgbLawoE`</summary>

```json
{
  "url": "https://github.com/rhyang2021/CogRouter",
  "prompt": "Extract all information about benchmark results, code availability, model weights, and any tables with ALFWorld/ScienceWorld results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0baf488d-4ebd-45be-855c-e78efb53fc01",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjV1f5xwXBhG4gXGuq4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd3447ab-4ef4-4499-8f45-a1dd8e125311",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018h38GzHHjCBhwxUGxdJHE6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 859,
      "cache_creation_input_tokens": 2860,
      "cache_read_input_tokens": 10937,
      "output_tokens": 384,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2860
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 859,
          "output_tokens": 384,
          "cache_read_input_tokens": 10937,
          "cache_creation_input_tokens": 2860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2860,
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

_source line 19 · 2026-05-12T00:32:30.182Z_

<details><summary>↩ Tool result · `toolu_01NfAhgyy3qANMzRXMCF1SQM`</summary>

```text
# CogRouter Research Summary

## Base Model
**Qwen2.5-7B** is the primary model used for achieving the reported results.

## Benchmark Results

**ALFWorld Performance:**
- Success rate: **82.3%**
- Outperforms GPT-4o by +40.3%
- Outperforms OpenAI-o3 by +18.3%
- Outperforms GRPO by +14.0%
- Uses **62% fewer tokens** than comparison methods

**ScienceWorld:**
The abstract mentions experiments on ScienceWorld but does not provide specific numerical scores or success rates for this benchmark.

## Key Terminology

**CoSFT:** "Cognition-aware Supervised Fine-tuning" - designed to instill stable level-specific patterns

**CoPO:** "Cognition-aware Policy Optimization" - enables step-level credit assignment via confidence-aware advantage reweighting

## Four Cognitive Levels

The framework implements a hierarchy ranging from "instinctive responses to strategic planning," though the abstract does not enumerate the specific names or characteristics of each individual level.

---

*Note: The provided content is an arXiv abstract page and does not contain detailed result tables with additional entries beyond those mentioned.*
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c50d84b-e983-4b2b-b3d2-a4166d1a964b",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "c79823d6-c708-4ffb-b9d4-5cffdeec34cb",
  "sourceToolAssistantUUID": "2c50d84b-e983-4b2b-b3d2-a4166d1a964b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-12T00:32:31.150Z_

<details><summary>↩ Tool result · `toolu_01TJKGih8EhDfbGUXyL1fuSq`</summary>

```text
# Benchmark Results Analysis

Based on the provided webpage content, I cannot extract the specific benchmark results you requested because **the abstract does not contain exact numerical values**.

## What the Abstract States:

The abstract only mentions that "Experiments on ALFWorld and WebShop show that Skill1 outperforms prior skill-based and reinforcement learning baselines." However, it provides:

- No ALFWorld success rate percentage (97.5% is **not mentioned**)
- No WebShop numerical results
- No specific baseline comparison numbers
- No base model specification

## Limitation:

The arXiv page shown is an abstract landing page. The actual numerical results, baseline comparisons, and technical details would be contained in the full PDF or HTML versions of the paper, which are not included in the content provided. To obtain the specific benchmark numbers and baseline comparisons you're seeking, you would need to access the complete paper through the "View PDF" or "HTML (experimental)" links.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0baf488d-4ebd-45be-855c-e78efb53fc01",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "72e2da18-96d5-41fe-a577-b6547360b5af",
  "sourceToolAssistantUUID": "0baf488d-4ebd-45be-855c-e78efb53fc01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-12T00:32:34.075Z_

<details><summary>↩ Tool result · `toolu_01UQDnJsrFiJAaumFgbLawoE`</summary>

```text
# CogRouter: Benchmark Results and Code Availability

## Code Availability
The source code is publicly available on GitHub at `rhyang2021/CogRouter`. The repository includes:
- Implementation of the CoPo (Cognition-aware Policy Optimization) framework
- Environment setups for ALFWorld and ScienceWorld
- Training scripts and examples

## Benchmark Environments
The paper evaluates on two interactive agent environments:

1. **ALFWorld** - Requires separate conda environment with gymnasium, stable-baselines3, and alfworld packages. PDDL & game files download via `alfworld-download -f`

2. **ScienceWorld** - Requires separate conda environment with scienceworld package

## Benchmark Results
**No specific benchmark results, performance tables, or quantitative metrics are provided in the README.** The document focuses on setup instructions and framework description rather than empirical results.

## Model Weights
No model weights or pre-trained checkpoints are mentioned in the provided content.

## Framework Details
The paper proposes "step-level cognitive depth adaptation," using four hierarchical cognitive levels and confidence-aware advantage reweighting. However, actual benchmark comparisons, success rates, or performance improvements are not detailed in this README excerpt.

The arxiv paper reference is provided: `arxiv.org/abs/2602.12662`
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd3447ab-4ef4-4499-8f45-a1dd8e125311",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "7ffa7c83-ef8e-4e76-a93a-c988b5beaadc",
  "sourceToolAssistantUUID": "bd3447ab-4ef4-4499-8f45-a1dd8e125311",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-12T00:32:39.006Z_

Let me fetch the full HTML versions of both papers to get the exact numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ffa7c83-ef8e-4e76-a93a-c988b5beaadc",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjW9zfa6ZnvqeSo51Vy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "35b326cf-92c5-4ec6-b0b1-b69d9d529d75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSyEcr2yyz335ZfgsqAFV7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2126,
      "cache_read_input_tokens": 13797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2126,
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

_source line 23 · 2026-05-12T00:32:42.671Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013dvys6C1fto1ynjDpxsdHJ`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.12662",
  "prompt": "Extract ALL benchmark results with exact numbers from the results/experiments section. I need: 1) ALFWorld success rate for CogRouter, 2) ScienceWorld score and success rate (SR) for CogRouter, 3) All baseline comparison numbers. Look for tables with results. The user claims ALFWorld 92.5%, ScienceWorld 84.6 score / 72.0% SR. Are these numbers correct? List every number you find in result tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35b326cf-92c5-4ec6-b0b1-b69d9d529d75",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjW9zfa6ZnvqeSo51Vy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eac14c5a-09dd-4aed-8b4d-b971a40985e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSyEcr2yyz335ZfgsqAFV7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2126,
      "cache_read_input_tokens": 13797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2126,
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

_source line 24 · 2026-05-12T00:32:44.326Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WnmiZrNAu8JvFi74ivC48q`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06130v1",
  "prompt": "Extract ALL benchmark results with exact numbers from results/experiments section. I need: 1) ALFWorld success rate for Skill1 - is it 97.5%? 2) WebShop results. 3) All baseline comparison numbers. 4) What base model is used? 5) Per-task ALFWorld breakdown if available. List every number you find in result tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eac14c5a-09dd-4aed-8b4d-b971a40985e6",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjW9zfa6ZnvqeSo51Vy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8daa2170-600c-489e-86f1-5b27a285f351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DSyEcr2yyz335ZfgsqAFV7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2126,
      "cache_read_input_tokens": 13797,
      "output_tokens": 355,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 355,
          "cache_read_input_tokens": 13797,
          "cache_creation_input_tokens": 2126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2126,
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

_source line 25 · 2026-05-12T00:32:48.566Z_

<details><summary>↩ Tool result · `toolu_013dvys6C1fto1ynjDpxsdHJ`</summary>

```text
# CogRouter Benchmark Results Verification

Based on Table 1 in the paper, here are the **exact numbers for CogRouter (with Qwen2.5-7B)**:

## CogRouter Results
- **ALFWorld Success Rate: 92.5%**
- **ScienceWorld Score: 84.6**
- **ScienceWorld Success Rate: 72.0%**
- **Average SR: 82.3%**
- **Average #Tokens: 1641.4**

✓ **The user's claimed numbers are correct.**

## Key Baseline Comparisons (CogRouter vs. others with Qwen2.5-7B)

| Method | ALFWorld SR | ScienceWorld Score | ScienceWorld SR |
|--------|-------------|-------------------|-----------------|
| GRPO | 83.5% | 71.1 | 53.0% |
| GiGPO | 88.0% | 67.3 | 47.0% |
| AdaptThink | 81.5% | 62.5 | 44.5% |
| ETO | 69.5% | 53.9 | 21.5% |

## Frontier Model Comparisons
- **GPT-4o**: ALFWorld 61.5%, ScienceWorld 57.0 score, 22.5% SR
- **OpenAI-o3**: ALFWorld 74.0%, ScienceWorld 72.4 score, 54.0% SR
- **DeepSeek-R1**: ALFWorld 73.0%, ScienceWorld 58.9 score, 40.0% SR

CogRouter achieves "state-of-the-art performance with superior token efficiency," using 62% fewer tokens than GRPO.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eac14c5a-09dd-4aed-8b4d-b971a40985e6",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "8553dcff-70ed-4be3-8876-e7ef4d83cb6d",
  "sourceToolAssistantUUID": "eac14c5a-09dd-4aed-8b4d-b971a40985e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-12T00:32:50.016Z_

<details><summary>↩ Tool result · `toolu_01WnmiZrNAu8JvFi74ivC48q`</summary>

```text
# Skill1 Benchmark Results - Complete Extraction

## Primary Results

**Skill1 Performance:**
- ALFWorld average success rate: **97.5%**
- WebShop score: **89.7**
- WebShop success rate: **82.9%**

## ALFWorld Per-Task Breakdown (Skill1)

| Task Type | Success Rate |
|-----------|--------------|
| Pick | 100.0% |
| Look | 98.6% |
| Clean | 97.3% |
| Heat | 99.2% |
| Cool | 96.1% |
| Pick2 | 96.0% |

## Base Model
**Qwen2.5-7B-Instruct** (Yang et al., 2024)

## Key Baseline Comparisons on ALFWorld (Average %)

| Method Category | Best Performer | Score |
|-----------------|----------------|-------|
| Training-free | ExpeL | 46.3% |
| RL without skills | GiGPO | 90.8% |
| RL with skills | RetroAgent | 94.9% |
| **Skill1 (proposed)** | — | **97.5%** |

**Skill1 improvement margins:**
- Over RetroAgent (previous best): "+2.6 points"
- Over GiGPO (RL-only best): "+6.7 points"

## Selected Baseline Details

- **RetroAgent**: 94.9% ALFWorld, 88.9 WebShop score
- **SkillRL**: 89.9% ALFWorld, 85.2 WebShop score  
- **SimpleMem**: 62.5% ALFWorld, 67.8 WebShop score
- **GRPO**: 77.6% ALFWorld, 79.3 WebShop score
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8daa2170-600c-489e-86f1-5b27a285f351",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "0acbc6f7-deb6-402c-afc3-cc0d6be4188d",
  "sourceToolAssistantUUID": "8daa2170-600c-489e-86f1-5b27a285f351",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-12T00:32:56.903Z_

Excellent. Now let me search for more ScienceWorld-specific results from 2026 and verify what the current SOTA is.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0acbc6f7-deb6-402c-afc3-cc0d6be4188d",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjXKyxe7UfzokEMf9iF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c7c46b8-d34b-446c-af37-894c5bff218b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UfC3LixcogYRZ3CSwyan6x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 15923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1296,
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

_source line 28 · 2026-05-12T00:32:57.357Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014QiD1VUzqGZRSCrYSzaFVn`</summary>

```json
{
  "query": "ScienceWorld benchmark 2026 state-of-the-art score success rate agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c7c46b8-d34b-446c-af37-894c5bff218b",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjXKyxe7UfzokEMf9iF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "896d5f73-9271-43b1-baca-302101b68d9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UfC3LixcogYRZ3CSwyan6x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 15923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1296,
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

_source line 29 · 2026-05-12T00:32:57.923Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011AsUZqzgqAf8k7f8ifLAoX`</summary>

```json
{
  "query": "ALFWorld leaderboard 2026 RetroAgent CogRouter success rate comparison"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "896d5f73-9271-43b1-baca-302101b68d9f",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjXKyxe7UfzokEMf9iF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2de81ee1-7c84-444b-b70d-ec7ef9c105ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UfC3LixcogYRZ3CSwyan6x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 15923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1296,
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

_source line 30 · 2026-05-12T00:32:58.112Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016caMPbiHQesczFvEHsCwsd`</summary>

```json
{
  "query": "ScienceWorld benchmark leaderboard 2026 CogRouter GRPO GiGPO results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2de81ee1-7c84-444b-b70d-ec7ef9c105ec",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjXKyxe7UfzokEMf9iF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9551e195-08d8-4982-9ba4-29cd0a3ccf17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UfC3LixcogYRZ3CSwyan6x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 15923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1296,
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

_source line 31 · 2026-05-12T00:33:02.994Z_

<details><summary>↩ Tool result · `toolu_011AsUZqzgqAf8k7f8ifLAoX`</summary>

```text
Web search results for query: "ALFWorld leaderboard 2026 RetroAgent CogRouter success rate comparison"

Links: [{"title":"Result | AgentBoard: An Analytical Evaluation Board of Multi-Turn LLM Agents","url":"https://hkust-nlp.github.io/agentboard/static/leaderboard.html"},{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"LLM Leaderboard 2026: Best AI Models Benchmark & Ranking","url":"https://www.clickrank.ai/llm-leaderboard/"},{"title":"GitHub - askforalfred/alfred: ALFRED - A Benchmark for Interpreting Grounded Instructions for Everyday Tasks · GitHub","url":"https://github.com/askforalfred/alfred"},{"title":"Arena Leaderboard | Compare & Benchmark the Best Frontier AI Models","url":"https://arena.ai/leaderboard/"},{"title":"agentquest/agentquest/benchmarks/alfworld/README.md at main · nec-research/agentquest","url":"https://github.com/nec-research/agentquest/blob/main/agentquest/benchmarks/alfworld/README.md"},{"title":"Best LLM Leaderboard 2026 | AI Model Rankings, Benchmarks & Pricing | Onyx AI","url":"https://onyx.app/llm-leaderboard"},{"title":"[Leaderboard] AI Agent Framework Scorecard 2026 | Rapid Claw","url":"https://rapidclaw.dev/blog/ai-agent-benchmarks-2026"},{"title":"How effective is your AI agent? 9 benchmarks to consider | TechTarget","url":"https://www.techtarget.com/searchsoftwarequality/tip/How-effective-is-your-AI-agent-benchmarks-to-consider"}]

Based on my search results, I was unable to find specific information about "RetroAgent" and "CogRouter" or their success rates on the ALFWorld leaderboard for 2026. The search returned general information about ALFWorld benchmarking and various LLM/agent leaderboards in 2026, but did not contain data about these specific agent frameworks.

The results did confirm that ALFWorld is designed to evaluate an AI agent's ability to interact with a simulated household, understanding and planning actions that involve manipulating objects, testing the agent's reasoning capabilities and task decomposition. However, there is no publicly available leaderboard data comparing RetroAgent and CogRouter on this benchmark.

If you're looking for this specific comparison, I'd recommend:
1. Checking the official ALFWorld repository or benchmark website directly
2. Searching for research papers or GitHub repositories from the teams who developed these agents
3. Looking at specialized agent benchmarking platforms that may track these specific implementations


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2de81ee1-7c84-444b-b70d-ec7ef9c105ec",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "42433c38-5e28-47f5-afb8-9ea6ab6ad1d5",
  "sourceToolAssistantUUID": "2de81ee1-7c84-444b-b70d-ec7ef9c105ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-12T00:33:04.703Z_

<details><summary>↩ Tool result · `toolu_014QiD1VUzqGZRSCrYSzaFVn`</summary>

```text
Web search results for query: "ScienceWorld benchmark 2026 state-of-the-art score success rate agent"

Links: [{"title":"ScienceWorld Benchmark","url":"https://www.emergentmind.com/topics/scienceworld-benchmark"},{"title":"SCIENCEWORLD: Is your Agent Smarter than a 5","url":"https://aclanthology.org/2022.emnlp-main.775.pdf"},{"title":"ScienceWorld","url":"https://sciworld.apps.allenai.org/"},{"title":"SCIENCEWORLD: Is your Agent Smarter than a 5th Grader?","url":"https://arxiv.org/pdf/2203.07540"},{"title":"2025-2026 AI Computer-Use Benchmarks & Top AI Agents ...","url":"https://o-mega.ai/articles/the-2025-2026-guide-to-ai-computer-use-benchmarks-and-top-ai-agents"},{"title":"[2203.07540] ScienceWorld: Is your Agent Smarter than a 5th Grader?","url":"https://arxiv.org/abs/2203.07540"},{"title":"[Leaderboard] AI Agent Framework Scorecard 2026 | Rapid Claw","url":"https://rapidclaw.dev/blog/ai-agent-benchmarks-2026"},{"title":"AI Benchmarks 2026: Top Evaluations and Their Limits","url":"https://kili-technology.com/blog/ai-benchmarks-guide-the-top-evaluations-in-2026-and-why-theyre-not-enough"},{"title":"AI Agent Benchmarks 2026: Performance, Accuracy & Cost Compared","url":"https://aiagentsquare.com/blog/ai-agent-benchmarks-2026.html"},{"title":"How We Broke Top AI Agent Benchmarks","url":"https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/"}]

Based on the search results, I found information about the ScienceWorld benchmark, though the results do not contain specific 2026 state-of-the-art scores. Here's what I found:

## ScienceWorld Benchmark Overview

ScienceWorld Benchmark is a comprehensive evaluation suite simulating an elementary science curriculum to assess interactive, multi-step experimental reasoning in autonomous agents. The environment consists of richly parameterized text with ten interconnected locations populated with up to 200 types of objects, with an available action space comprising 25 high-level commands generating up to 200,000 legal action–object pairs per step, where agents interact by issuing text commands that result in changes to the world state and observations returned as textual descriptions.

## Performance Metrics and Recent Results

A 1.5M-parameter interactively trained DRRN agent achieves an average task score of 0.17, outperforming statically pre-trained 11B-parameter transformer models that plateau near 0.08, while recent LLMs like GPT-J (6B) achieve 62.57/100 using full action-observation history (a 3.5x improvement over DRRN).

Unfortunately, the search results do not contain specific state-of-the-art success rate scores or agent performance data explicitly labeled as 2026 results for the ScienceWorld benchmark. The most recent performance data in the results appears to be from earlier research papers and benchmark summaries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "896d5f73-9271-43b1-baca-302101b68d9f",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "b8e24e72-e86d-4431-b7a4-f171fb4b8e1e",
  "sourceToolAssistantUUID": "896d5f73-9271-43b1-baca-302101b68d9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-12T00:33:06.134Z_

<details><summary>↩ Tool result · `toolu_016caMPbiHQesczFvEHsCwsd`</summary>

```text
Web search results for query: "ScienceWorld benchmark leaderboard 2026 CogRouter GRPO GiGPO results"

Links: [{"title":"Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings","url":"https://llm-stats.com/leaderboards/open-llm-leaderboard"},{"title":"AI Model Leaderboards & Benchmarks | Scale Labs","url":"https://labs.scale.com/leaderboard"},{"title":"ScienceWorld: Is your Agent Smarter than a 5th Grader? | Request PDF","url":"https://www.researchgate.net/publication/372924838_ScienceWorld_Is_your_Agent_Smarter_than_a_5th_Grader"},{"title":"LLM Leaderboard 2026: Best AI Models Benchmark & Ranking","url":"https://www.clickrank.ai/llm-leaderboard/"},{"title":"AI Benchmarks 2026: Top Evaluations and Their Limits","url":"https://kili-technology.com/blog/ai-benchmarks-guide-the-top-evaluations-in-2026-and-why-theyre-not-enough"},{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"Best LLM for Coding in 2026: Ranked by Real Benchmarks | WhatLLM.org","url":"https://whatllm.org/best-llm-for-coding"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"Benchmark Leaderboard 2026 - LLM Stats","url":"https://llm-stats.com/benchmarks/table"}]

Based on the search results, I found relevant information about the ScienceWorld benchmark and the systems you mentioned:

CogRouter achieves state-of-the-art performance on ScienceWorld, with Qwen2.5-7B reaching an 82.3% success rate, outperforming GPT-4o (+40.3%), OpenAI-o3 (+18.3%), and GRPO (+14.0%), while using 62% fewer tokens.

CogRouter is a framework that trains agents to dynamically adapt cognitive depth at each step, using a two-stage training approach that includes Cognition-aware Supervised Fine-tuning (CoSFT) and Cognition-aware Policy Optimization (CoPO) for step-level credit assignment.

However, the search results don't contain specific information about GiGPO or a comprehensive 2026 ScienceWorld leaderboard with all the systems you mentioned. The information about CogRouter comes from research comparing it against GRPO on the ScienceWorld benchmark, but I wasn't able to locate a full leaderboard with all three systems you're interested in.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9551e195-08d8-4982-9ba4-29cd0a3ccf17",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "fc3cbab3-20c6-4fe6-9290-e1fc67203f29",
  "sourceToolAssistantUUID": "9551e195-08d8-4982-9ba4-29cd0a3ccf17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-12T00:33:12.075Z_

Now let me search for the ScienceWorld leaderboard and any other recent 2026 papers on ScienceWorld.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc3cbab3-20c6-4fe6-9290-e1fc67203f29",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjYWmsih8Do9j4ZBsQq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f01bee1-e67a-441e-8174-3a8e1a5e7450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uo4F7eYwdsnUUTNAtrAiV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2638,
      "cache_read_input_tokens": 17219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2638,
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

_source line 35 · 2026-05-12T00:33:14.224Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YZQvAoqmX45qfMQSyAZ9q5`</summary>

```json
{
  "url": "https://sciworld.apps.allenai.org/",
  "prompt": "Extract all leaderboard results, rankings, scores, and success rates for any agents/models listed on this ScienceWorld benchmark page. List all entries with their exact scores."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f01bee1-e67a-441e-8174-3a8e1a5e7450",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjYWmsih8Do9j4ZBsQq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b3a1d2e-c4ca-4bb6-ab7c-a1b6f292ebd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uo4F7eYwdsnUUTNAtrAiV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2638,
      "cache_read_input_tokens": 17219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2638,
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

_source line 36 · 2026-05-12T00:33:15.023Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E31ghm4HMyCMZcMnNu7cUa`</summary>

```json
{
  "query": "site:arxiv.org ScienceWorld agent 2026 score benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b3a1d2e-c4ca-4bb6-ab7c-a1b6f292ebd9",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjYWmsih8Do9j4ZBsQq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05e6af97-5d3a-45c9-b524-3ea0cee5c75e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uo4F7eYwdsnUUTNAtrAiV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2638,
      "cache_read_input_tokens": 17219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2638,
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

_source line 37 · 2026-05-12T00:33:15.153Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018XZ2bAkXvT5WWSEXAkpcf8`</summary>

```json
{
  "query": "RetroAgent ALFWorld 94.9% success rate arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05e6af97-5d3a-45c9-b524-3ea0cee5c75e",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjYWmsih8Do9j4ZBsQq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1cdc020f-0440-4a45-bc18-ad62723e5f7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uo4F7eYwdsnUUTNAtrAiV4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2638,
      "cache_read_input_tokens": 17219,
      "output_tokens": 249,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2638
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 249,
          "cache_read_input_tokens": 17219,
          "cache_creation_input_tokens": 2638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2638,
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

_source line 38 · 2026-05-12T00:33:16.883Z_

<details><summary>↩ Tool result · `toolu_01YZQvAoqmX45qfMQSyAZ9q5`</summary>

```text
I don't see any leaderboard results, rankings, scores, or success rates in the provided content. The page excerpt only shows "ScienceWorld" as a heading/title, with no actual benchmark data, agent performance metrics, or model scores listed.

To extract the information you're requesting, I would need the full webpage content that includes the actual leaderboard table or results section with specific agents/models and their corresponding performance metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b3a1d2e-c4ca-4bb6-ab7c-a1b6f292ebd9",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "a64a1a08-b71c-441f-8b8a-7afc904b62aa",
  "sourceToolAssistantUUID": "9b3a1d2e-c4ca-4bb6-ab7c-a1b6f292ebd9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-12T00:33:21.155Z_

<details><summary>↩ Tool result · `toolu_018XZ2bAkXvT5WWSEXAkpcf8`</summary>

```text
Web search results for query: "RetroAgent ALFWorld 94.9% success rate arxiv 2026"

Links: [{"title":"Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning","url":"https://arxiv.org/html/2605.06130"},{"title":"RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback","url":"https://arxiv.org/html/2603.08561"},{"title":"[2603.08561] RetroAgent: From Solving to Evolving via Retrospective Dual Intrinsic Feedback","url":"https://arxiv.org/abs/2603.08561"},{"title":"Retrospex: Language Agent Meets Offline Reinforcement Learning Critic","url":"https://arxiv.org/html/2505.11807v1"},{"title":"Explore | alphaXiv","url":"https://www.alphaxiv.org/"},{"title":"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection","url":"https://arxiv.org/html/2505.15182v2"},{"title":"arXiv:2505.00234v3 [cs.LG] 16 May 2025","url":"https://arxiv.org/pdf/2505.00234"},{"title":"March, 2026 Retrieval-Augmented LLM Agents: Learning to Learn from Experience","url":"https://arxiv.org/pdf/2603.18272"},{"title":"alfworld: aligning text and embodied environments for ...","url":"https://arxiv.org/pdf/2010.03768"},{"title":"AgentOCR: Reimagining Agent History via Optical Self-Compression","url":"https://arxiv.org/html/2601.04786v1"}]

Based on the search results, I found information about RetroAgent and ALFWorld performance. RetroAgent achieves a 95.6% success rate on ALFWorld when equipped with an RL-trained self-reflection variant, which is slightly higher than the 94.9% you mentioned in your query.

The research appears in an arxiv paper from March 2026. More specifically, RetroAgent surpasses GRPO baselines by +18.3% on ALFWorld, demonstrating significant improvements on this benchmark.

It's worth noting that a newer method called Skill1 reaches 97.5% average success rate on ALFWorld, surpassing RetroAgent by 2.6 percentage points, indicating that RetroAgent's 95.6% result was state-of-the-art at the time of its publication, but has since been exceeded by other approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cdc020f-0440-4a45-bc18-ad62723e5f7d",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "465620ae-a4d8-4be9-93c6-3f100983bca4",
  "sourceToolAssistantUUID": "1cdc020f-0440-4a45-bc18-ad62723e5f7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-12T00:33:21.540Z_

<details><summary>↩ Tool result · `toolu_01E31ghm4HMyCMZcMnNu7cUa`</summary>

```text
Web search results for query: "site:arxiv.org ScienceWorld agent 2026 score benchmark"

Links: [{"title":"SCIENCEWORLD: Is your Agent Smarter than a 5th Grader?","url":"https://arxiv.org/pdf/2203.07540"},{"title":"[2203.07540] ScienceWorld: Is your Agent Smarter than a 5th Grader?","url":"https://arxiv.org/abs/2203.07540"},{"title":"CWM: Contrastive World Models for Action Feasibility Learning in Embodied Agent Pipelines","url":"https://arxiv.org/html/2602.22452"},{"title":"A Song of Ice and Fire: Analyzing Textual Autotelic Agents in ScienceWorld","url":"https://arxiv.org/pdf/2302.05244"},{"title":"Knowledge-enhanced Agents for Interactive Text Games Prateek Chhikara","url":"https://arxiv.org/pdf/2305.05091"},{"title":"ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery","url":"https://arxiv.org/html/2410.05080v1"},{"title":"SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks","url":"https://arxiv.org/html/2602.12670v1"},{"title":"[2410.05080] ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery","url":"https://arxiv.org/abs/2410.05080"},{"title":"AgentCE-Bench: Agent Configurable Evaluation with Scalable Horizons and Controllable Difficulty under Lightweight Environments","url":"https://arxiv.org/html/2604.06111v2"},{"title":"Qwen3-Coder-Next Technical Report","url":"https://arxiv.org/html/2603.00729v1"}]

Based on the web search results, I found relevant information about ScienceWorld and agent performance benchmarks. Here's what I found:

## ScienceWorld Benchmark Overview

ScienceWorld is a benchmark to test agents' scientific reasoning abilities in a new interactive text environment at the level of a standard elementary school science curriculum.

## Recent Research (2026)

One of the most recent papers on arxiv.org is about improving agent performance on ScienceWorld. Through two empirical studies on the ScienceWorld benchmark, researchers showed that a Contrastive World Model (CWM) achieves meaningfully better performance than a supervised fine-tuning baseline specifically in the hardest evaluation conditions: one-word physics-opposing substitutions (+6.76 pp P@1, AUC 0.929 vs. 0.906) and out-of-distribution task execution.

## Key Findings

Experiments provide empirical evidence showing that a 1.5 million parameter agent trained interactively for 100k steps outperforms a 11 billion parameter model statically trained for scientific question-answering and reasoning from millions of expert demonstrations.

The search results show that ScienceWorld remains an active area of research into 2026, with various agents being tested and compared for their ability to reason about scientific concepts in interactive text environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05e6af97-5d3a-45c9-b524-3ea0cee5c75e",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "9ce7ff0a-5651-4670-a240-2a8dc378c0cc",
  "sourceToolAssistantUUID": "05e6af97-5d3a-45c9-b524-3ea0cee5c75e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-12T00:33:24.810Z_

Let me get the RetroAgent paper details and check whether Skill1 also reports ScienceWorld results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ce7ff0a-5651-4670-a240-2a8dc378c0cc",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjZedw2GXwT7Z6zQgEu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1bf74af5-f15b-42e2-8c42-2e1c5bf51d05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014fAQirkwiBdKtyZqyT41uC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 690,
      "cache_creation_input_tokens": 1191,
      "cache_read_input_tokens": 19857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1191,
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

_source line 42 · 2026-05-12T00:33:26.293Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GoUrWeA9Lfh9EkN4wBw37e`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.08561",
  "prompt": "Extract all benchmark results. What are RetroAgent's exact ALFWorld and ScienceWorld scores? List all numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bf74af5-f15b-42e2-8c42-2e1c5bf51d05",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjZedw2GXwT7Z6zQgEu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89031f7c-51fb-44cd-9d26-e09e0dd0c013",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014fAQirkwiBdKtyZqyT41uC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 690,
      "cache_creation_input_tokens": 1191,
      "cache_read_input_tokens": 19857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1191,
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

_source line 43 · 2026-05-12T00:33:26.746Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vp1Y4oGBQsQAxXNiDJ8ULM`</summary>

```json
{
  "query": "\"Skill1\" ScienceWorld benchmark results 2605.06130"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89031f7c-51fb-44cd-9d26-e09e0dd0c013",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjZedw2GXwT7Z6zQgEu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "399ecc49-6136-415f-a8a3-e603b1a7462b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014fAQirkwiBdKtyZqyT41uC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 690,
      "cache_creation_input_tokens": 1191,
      "cache_read_input_tokens": 19857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1191,
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

_source line 44 · 2026-05-12T00:33:28.957Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012bEYcyhNSnsnwbKZAwXZrr`</summary>

```json
{
  "url": "https://www.emergentmind.com/topics/scienceworld-benchmark",
  "prompt": "Extract any SOTA scores or leaderboard results for ScienceWorld benchmark. What are the top-performing systems and their scores/success rates? List all numbers and methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "399ecc49-6136-415f-a8a3-e603b1a7462b",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjZedw2GXwT7Z6zQgEu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3f0b3fd-5874-4942-a4b9-11831470bebd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014fAQirkwiBdKtyZqyT41uC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 690,
      "cache_creation_input_tokens": 1191,
      "cache_read_input_tokens": 19857,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1191
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 690,
          "output_tokens": 288,
          "cache_read_input_tokens": 19857,
          "cache_creation_input_tokens": 1191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1191,
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

_source line 45 · 2026-05-12T00:33:29.474Z_

<details><summary>↩ Tool result · `toolu_01GoUrWeA9Lfh9EkN4wBw37e`</summary>

```text
Based on the provided content, I can only extract limited benchmark information from the abstract:

**Available Results:**
The abstract states RetroAgent "surpasses Group Relative Policy Optimization (GRPO) baselines by +18.3% on ALFWorld, +15.4% on WebShop, +27.1% on Sokoban, and +8.9% on MineSweeper."

**What's Missing:**
The webpage does not contain RetroAgent's exact absolute scores for ALFWorld or any scores for ScienceWorld. Only the relative performance improvements over GRPO baselines are provided in the abstract. The full paper would be needed to find the specific numerical results you're requesting.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89031f7c-51fb-44cd-9d26-e09e0dd0c013",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "d7fa0c89-7ed7-45a6-b203-a5e6763d4e7f",
  "sourceToolAssistantUUID": "89031f7c-51fb-44cd-9d26-e09e0dd0c013",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-12T00:33:32.313Z_

<details><summary>↩ Tool result · `toolu_01Vp1Y4oGBQsQAxXNiDJ8ULM`</summary>

```text
Web search results for query: ""Skill1" ScienceWorld benchmark results 2605.06130"

Links: [{"title":"Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning","url":"https://arxiv.org/html/2605.06130"},{"title":"[2605.06130] Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning","url":"https://arxiv.org/abs/2605.06130"},{"title":"Paper page - Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning","url":"https://huggingface.co/papers/2605.06130"},{"title":"Unified Evolution of Skill-Augmented Agents via Reinforcement ...","url":"https://bytez.com/docs/arxiv/2605.06130/paper"},{"title":"Explore | alphaXiv","url":"https://www.alphaxiv.org/"}]

Based on the search results, I found information about the Skill1 paper (arxiv 2605.06130), though the search results don't contain specific ScienceWorld benchmark results.

Experiments on ALFWorld and WebShop show that Skill1 outperforms prior skill-based and reinforcement learning baselines. More specifically, this approach achieved a 97.5% success rate on ALFWorld, surpassing prior methods like RetroAgent by 2.6 percentage points, and also demonstrated leading performance on WebShop.

Skill1 is a framework that trains a single policy to co-evolve skill selection, utilization, and distillation toward a shared task-outcome objective. Training dynamics confirm the co-evolution of the three capabilities, and ablations show that removing any credit signal degrades the evolution.

However, the search results do not contain specific benchmark results for ScienceWorld. The paper appears to focus on evaluations on ALFWorld and WebShop environments. If you're looking for ScienceWorld-specific results, you may need to check the full paper directly at https://arxiv.org/abs/2605.06130.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "399ecc49-6136-415f-a8a3-e603b1a7462b",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "08b414e3-1e73-47d5-877a-131105894008",
  "sourceToolAssistantUUID": "399ecc49-6136-415f-a8a3-e603b1a7462b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-12T00:33:34.497Z_

<details><summary>↩ Tool result · `toolu_012bEYcyhNSnsnwbKZAwXZrr`</summary>

```text
# ScienceWorld Benchmark: SOTA Scores and Results

Based on the provided content, here are the documented performance results:

## Top-Performing Systems

**DRRN (Dynamic Reinforcement Recurrent Network)**
- 1.5M parameters, interactively trained
- Average task score: 0.17
- Outperformed static pre-trained 11B-parameter transformers (~0.08)

**GPT-J (6B parameters)**
- Score: 62.57/100 using full action-observation history
- 3.5x improvement over DRRN
- With only 6.5% of training data: 2.2x improvement over DRRN

**ReasonPlanner**
- Achieved "1.8x the score of previous prompt-based approaches"
- Uses temporal knowledge graphs and LLM-based SARSA planning

**KnowMap (with gpt-4-turbo)**
- 17.71% performance improvement over baseline
- Fine-tunes knowledge-embedding models for task adaptation

## Key Metric Categories

The benchmark evaluates performance across:
- Task completion rate (0–100 per task)
- Valid action rate (80–95%+ in best runs)
- Performance variance (task-dependent)

**Note:** The document emphasizes significant task variability, with some tasks showing near-perfect accuracy while others "remain unsolved even by advanced agents."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3f0b3fd-5874-4942-a4b9-11831470bebd",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "c314ae96-d906-49da-a4ef-9f2e90b0c083",
  "sourceToolAssistantUUID": "e3f0b3fd-5874-4942-a4b9-11831470bebd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-12T00:33:36.883Z_

Let me fetch the RetroAgent HTML paper for exact numbers, and also check for other recent ScienceWorld papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c314ae96-d906-49da-a4ef-9f2e90b0c083",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011Cawjac1CyjfhRT1J8Giz4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef311f96-c51c-4a8c-8e67-82cecd5375d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHj2HKsdBAZQzfjrH6pAKV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2053,
      "cache_read_input_tokens": 21048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2053,
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

_source line 49 · 2026-05-12T00:33:38.841Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XPJeQ1FExoamyXvFdvrqCf`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.08561",
  "prompt": "Extract ALL benchmark results with exact numbers from the results tables. What is RetroAgent's exact ALFWorld success rate? Does it report ScienceWorld results? List all absolute numbers from result tables, not just relative improvements."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef311f96-c51c-4a8c-8e67-82cecd5375d5",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011Cawjac1CyjfhRT1J8Giz4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "08f0d87c-b8fe-4f59-bb2a-54a2abd9e5d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHj2HKsdBAZQzfjrH6pAKV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2053,
      "cache_read_input_tokens": 21048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2053,
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

_source line 50 · 2026-05-12T00:33:39.587Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014KsTU98YCNvfVntrE64ogf`</summary>

```json
{
  "query": "arxiv 2026 ScienceWorld interactive text agent new method results score"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08f0d87c-b8fe-4f59-bb2a-54a2abd9e5d6",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011Cawjac1CyjfhRT1J8Giz4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9883e4a8-9799-486b-9fe8-71ed9e0e1783",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XHj2HKsdBAZQzfjrH6pAKV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2053,
      "cache_read_input_tokens": 21048,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2053
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 21048,
          "cache_creation_input_tokens": 2053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2053,
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

_source line 51 · 2026-05-12T00:33:43.654Z_

<details><summary>↩ Tool result · `toolu_01XPJeQ1FExoamyXvFdvrqCf`</summary>

```text
# RetroAgent Benchmark Results

## ALFWorld Success Rate
RetroAgent (RL-Trained Reflection) achieved **95.6±2.3%** success rate on ALFWorld.

## Complete Benchmark Results from Table 1

**RetroAgent (In-Context Reflection):**
- ALFWorld: 91.7±1.2%
- WebShop Task Score: 87.6±2.1%
- WebShop Success: 78.9±3.6%
- Sokoban: 78.9±3.6%
- MineSweeper: 47.9±2.0%

**RetroAgent (RL-Trained Reflection):**
- ALFWorld: 95.6±2.3%
- WebShop Task Score: 88.9±1.3%
- WebShop Success: 82.3±1.6%
- Sokoban: 82.3±1.6%
- MineSweeper: 48.2±2.0%

## ScienceWorld Results
The document does **not** report ScienceWorld results. The paper evaluates performance exclusively on four environments: ALFWorld, WebShop, Sokoban, and MineSweeper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08f0d87c-b8fe-4f59-bb2a-54a2abd9e5d6",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "f74ee437-64f4-4e13-b711-2c577ae43d90",
  "sourceToolAssistantUUID": "08f0d87c-b8fe-4f59-bb2a-54a2abd9e5d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-12T00:33:45.566Z_

<details><summary>↩ Tool result · `toolu_014KsTU98YCNvfVntrE64ogf`</summary>

```text
Web search results for query: "arxiv 2026 ScienceWorld interactive text agent new method results score"

Links: [{"title":"[2203.07540] ScienceWorld: Is your Agent Smarter than a 5th Grader?","url":"https://arxiv.org/abs/2203.07540"},{"title":"Knowledge-enhanced Agents for Interactive Text Games Prateek Chhikara","url":"https://arxiv.org/pdf/2305.05091"},{"title":"A Song of Ice and Fire: Analyzing Textual Autotelic Agents in ScienceWorld","url":"https://arxiv.org/pdf/2302.05244"},{"title":"AI Co-Mathematician: Accelerating Mathematicians with Agentic AI","url":"https://arxiv.org/html/2605.06651v1"},{"title":"iWorld-Bench: A Benchmark for Interactive World Models with a Unified Action Generation Framework","url":"https://arxiv.org/html/2605.03941v2"},{"title":"One STEP at a time: Language Agents are Stepwise Planners","url":"https://arxiv.org/html/2411.08432v1"},{"title":"Artificial Intelligence","url":"https://arxiv.org/list/cs.AI/new"},{"title":"Artificial Intelligence May 2026","url":"https://arxiv.org/list/cs.AI/current"},{"title":"Multiagent Systems Apr 2026","url":"https://arxiv.org/list/cs.MA/current"},{"title":"MAESTRO: Multi-Agent Evaluation Suite for Testing, ...","url":"https://arxiv.org/pdf/2601.00481"}]

Based on the search results, I found relevant information about ScienceWorld and interactive text agents. Here are the key findings:

## ScienceWorld Benchmark Overview

ScienceWorld is a benchmark designed to test agents' scientific reasoning abilities in a new interactive text environment at the level of a standard elementary school science curriculum.

## Recent Method Results and Scores

One of the most recent approaches is the **STEP framework**, which achieves strong performance:

STEP achieves an overall score of 67.4 and successfully completes 12 out of 18 tasks. The model successfully completes 12 out of 18 tasks, ranking first in 11 tasks.

## Performance Comparison with Other Methods

For context, among reinforcement learning agents, DRRN achieves the highest overall score of 16.7, which is still significantly lower than the scores of all the generative language agents, with the lowest among them being ReAct at 29.6.

LLM-based methods (Generative Language Agents) outperform conventional RL agents due to their advanced generalization abilities.

The STEP framework represents a significant advance in interactive text-based agents for scientific reasoning tasks, incorporating planning, execution, evaluation, and memory components to solve complex scientific tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9883e4a8-9799-486b-9fe8-71ed9e0e1783",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "83e28c32-3054-4919-8844-d73dab4ed6fe",
  "sourceToolAssistantUUID": "9883e4a8-9799-486b-9fe8-71ed9e0e1783",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-12T00:33:48.839Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WMTUFCw8J8ogtrLRN2UZkK`</summary>

```json
{
  "query": "SkillsBench arxiv 2602.12670 ScienceWorld ALFWorld results 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83e28c32-3054-4919-8844-d73dab4ed6fe",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjbRQztvsMKvhomHDkE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0a8556f-b428-4f6e-b883-d87d71ace0d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFwDu4BuJk4CH4syoXytAm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1260,
      "cache_read_input_tokens": 23101,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1260,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-12T00:33:49.442Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QbMuyTavMz1mMi7tkVxRS1`</summary>

```json
{
  "query": "GiGPO GRPO ALFWorld ScienceWorld benchmark 2026 results agent training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0a8556f-b428-4f6e-b883-d87d71ace0d3",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjbRQztvsMKvhomHDkE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e220102-d8a5-418d-88e9-0014bb42b671",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFwDu4BuJk4CH4syoXytAm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1260,
      "cache_read_input_tokens": 23101,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1260
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 133,
          "cache_read_input_tokens": 23101,
          "cache_creation_input_tokens": 1260,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1260,
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

_source line 55 · 2026-05-12T00:33:57.170Z_

<details><summary>↩ Tool result · `toolu_01QbMuyTavMz1mMi7tkVxRS1`</summary>

```text
Web search results for query: "GiGPO GRPO ALFWorld ScienceWorld benchmark 2026 results agent training"

Links: [{"title":"Skill1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning","url":"https://arxiv.org/html/2605.06130"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978v1"},{"title":"RLVMR: RL with Verifiable Meta-Reasoning Rewards for Long-Horizon Agents","url":"https://arxiv.org/pdf/2507.22844"},{"title":"EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning","url":"https://arxiv.org/html/2509.22576"},{"title":"Phase-Aware Mixture of Experts for Agentic Reinforcement Learning","url":"https://arxiv.org/html/2602.17038"},{"title":"DPEPO: Diverse Parallel Exploration Policy Optimization for LLM-based Agents","url":"https://arxiv.org/html/2604.24320"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training Lang Feng1","url":"https://personal.ntu.edu.sg/boan/papers/NeurIPS25_GiGPO.pdf"},{"title":"Co-Evolution of Policy and Internal Reward for Language Agents","url":"https://arxiv.org/html/2604.03098"},{"title":"Graph-Enhanced Policy Optimization in LLM Agent Training","url":"https://arxiv.org/html/2510.26270"},{"title":"Agentic Critical Training","url":"https://arxiv.org/html/2603.08706v1"}]

Based on the web search results, I found comprehensive information about GiGPO, GRPO, ALFWorld, and ScienceWorld benchmark results for agent training in 2026. Here's what I found:

## GiGPO Performance Results

GiGPO surpasses GRPO by 13.3% on ALFWorld and 10.6% on WebShop at 1.5B, and by 12.6% and 9.1%, respectively, at 7B. GiGPO delivers fine-grained per-step credit signals and achieves performance gains of > 12% on ALFWorld and > 9% on WebShop over GRPO.

## Recent 2026 Methods and Benchmarks

Several recent papers from 2026 have benchmarked these environments:

**RLVMR (February 2026):** On ALFWorld's L2 split, RLVMR's 7B model reaches an impressive 83.6% success rate, a substantial 16.4 percentage point improvement over the strongest baseline (GiGPO). RLVMR achieves average success rates of 91.6% on ALFWorld and 47.5% on ScienceWorld.

**EPO (February 2026):** EPO achieves up to 152% improvement on ScienceWorld and 19.8% on ALFWorld.

**PA-MoE (February 2026):** PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% overall success on ALFWorld, improving over the GiGPO baseline (86.1%) by +7.7 percentage points.

**DPEPO (April 2026):** This is the latest method found, which achieves higher performance on the more challenging ScienceWorld benchmark with competitive efficiency.

These results demonstrate significant progress in agent training algorithms across these benchmarks throughout 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e220102-d8a5-418d-88e9-0014bb42b671",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "6357619e-00f0-4962-a4be-6f061827030b",
  "sourceToolAssistantUUID": "2e220102-d8a5-418d-88e9-0014bb42b671",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-12T00:34:01.298Z_

<details><summary>↩ Tool result · `toolu_01WMTUFCw8J8ogtrLRN2UZkK`</summary>

```text
Web search results for query: "SkillsBench arxiv 2602.12670 ScienceWorld ALFWorld results 2026"

Links: [{"title":"[2602.12670] SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks","url":"https://arxiv.org/abs/2602.12670"},{"title":"SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks","url":"https://arxiv.org/html/2602.12670v1"},{"title":"SkillNet: Create, Evaluate, and Connect AI Skills","url":"https://arxiv.org/html/2603.04448"},{"title":"[2602.12670v1] SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks","url":"https://arxiv.org/abs/2602.12670v1"},{"title":"Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills","url":"https://arxiv.org/html/2604.05333"},{"title":"Paper page - SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks","url":"https://huggingface.co/papers/2602.12670"},{"title":"SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.12670v1"},{"title":"SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2602.12670"},{"title":"SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning","url":"https://arxiv.org/html/2602.08234"},{"title":"Explore | alphaXiv","url":"https://www.alphaxiv.org/"}]

Based on the search results, here's what I found about SkillsBench (arxiv 2602.12670) and its results on ScienceWorld and ALFWorld:

## SkillsBench Overview

SkillsBench is a benchmark of 86 tasks across 11 domains paired with curated Skills and deterministic verifiers. Each task is evaluated under three conditions: no Skills, curated Skills, and self-generated Skills.

## Key Results

Curated Skills raise average pass rate by 16.2 percentage points, but effects vary widely by domain (+4.5pp for Software Engineering to +51.9pp for Healthcare) and 16 of 84 tasks show negative deltas. Self-generated Skills provide no benefit on average, showing that models cannot reliably author the procedural knowledge they benefit from consuming. Focused Skills with 2-3 modules outperform comprehensive documentation, and smaller models with Skills can match larger models without them.

## Related Work on ALFWorld and ScienceWorld

While SkillsBench itself focuses on diverse technical tasks across 11 domains, other related work has evaluated skills on ALFWorld and ScienceWorld. Experimental evaluations on ALFWorld, WebShop, and ScienceWorld demonstrate that SkillNet significantly enhances agent performance, improving average rewards by 40% and reducing execution steps by 30% across multiple backbone models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0a8556f-b428-4f6e-b883-d87d71ace0d3",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "e9a4cdc4-9e98-46fb-99b2-2d930ad1873b",
  "sourceToolAssistantUUID": "d0a8556f-b428-4f6e-b883-d87d71ace0d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-12T00:34:04.941Z_

Now let me get the GiGPO paper's exact numbers for a clearer baseline picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9a4cdc4-9e98-46fb-99b2-2d930ad1873b",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjcbQ3g1iuXfrjMnaCR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0ed45a3-907b-430b-b5e1-3f2f56f49369",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzCrjGemFcgBjnSRrLooyx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 944,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 24361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 968,
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

_source line 58 · 2026-05-12T00:34:09.635Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017PT6vcHitntd4MHMEhaxRg`</summary>

```json
{
  "url": "https://arxiv.org/html/2505.10978v1",
  "prompt": "Extract ALL benchmark results with exact numbers. I need exact ALFWorld success rates and ScienceWorld scores/success rates for GiGPO and GRPO at 7B scale. List all entries from result tables."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0ed45a3-907b-430b-b5e1-3f2f56f49369",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjcbQ3g1iuXfrjMnaCR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74ab20c5-818f-4d10-8eb0-8cf3ebb38ec0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzCrjGemFcgBjnSRrLooyx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 944,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 24361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 968,
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

### Tool result

_source line 59 · 2026-05-12T00:34:14.415Z_

<details><summary>↩ Tool result · `toolu_017PT6vcHitntd4MHMEhaxRg`</summary>

```text
# Benchmark Results: GiGPO vs GRPO

Based on Table 1 in the document, here are the exact results at 7B scale:

## ALFWorld (Qwen2.5-7B-Instruct)

**GRPO:**
- Pick: 90.8±5.1%
- Look: 66.1±6.7%
- Clean: 89.3±5.4%
- Heat: 74.7±6.9%
- Cool: 72.5±5.4%
- Pick2: 64.7±7.3%
- **Overall: 77.6±5.2%**

**GiGPO (w/o std):**
- Pick: 91.8±5.4%
- Look: 88.6±6.3%
- Clean: 95.9±3.2%
- Heat: 90.2±2.6%
- Cool: 86.5±5.5%
- Pick2: 85.2±7.5%
- **Overall: 90.2±2.3%**

## WebShop (Qwen2.5-7B-Instruct)

**GRPO:**
- Score: 79.3±2.8
- Success: 66.1±3.7%

**GiGPO (w/o std):**
- Score: 86.2±2.6
- Success: 75.2±3.8%

**Note:** The document does not contain ScienceWorld results. Results are limited to ALFWorld and WebShop benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74ab20c5-818f-4d10-8eb0-8cf3ebb38ec0",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "cd1fbecc-9977-4955-b659-e0b2d6f38929",
  "sourceToolAssistantUUID": "74ab20c5-818f-4d10-8eb0-8cf3ebb38ec0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-12T00:34:19.882Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kqy315JwkTq4hVvTsbCq6z`</summary>

```json
{
  "query": "\"CogRouter\" OR \"2602.12662\" ScienceWorld 84.6 score 72.0 success rate verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd1fbecc-9977-4955-b659-e0b2d6f38929",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjcbQ3g1iuXfrjMnaCR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cccd239a-0302-478c-8f3c-a3983eb288d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzCrjGemFcgBjnSRrLooyx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 944,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 24361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 968,
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

### Tool result

_source line 61 · 2026-05-12T00:34:30.331Z_

<details><summary>↩ Tool result · `toolu_01Kqy315JwkTq4hVvTsbCq6z`</summary>

```text
Web search results for query: ""CogRouter" OR "2602.12662" ScienceWorld 84.6 score 72.0 success rate verification"

Links: [{"title":"[2602.12662] Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/abs/2602.12662"},{"title":"Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents","url":"https://arxiv.org/html/2602.12662"},{"title":"CWM: Contrastive World Models for Action Feasibility Learning in Embodied Agent Pipelines","url":"https://arxiv.org/html/2602.22452"},{"title":"Today - Science World","url":"https://www.scienceworld.ca/"},{"title":"Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization","url":"https://arxiv.org/html/2602.23008"},{"title":"ScienceWorld - YouTube","url":"https://www.youtube.com/channel/UCs9lU3KF6bVh49qDJnK6zbA"},{"title":"Science World | Destination Vancouver","url":"https://www.destinationvancouver.com/things-to-do/science-world"},{"title":"Scienceworld Contact Information | SupplyMine","url":"http://www.infomine.com/suppliers/contactstandard.asp?id=43173"},{"title":"Visit Us - Science World","url":"https://www.scienceworld.ca/visit-us/"},{"title":"TELUS World of Science: Employee Directory | ZoomInfo.com","url":"https://www.zoominfo.com/pic/telus-world-of-science/143491288"}]

I found relevant information about CogRouter and paper 2602.12662. Let me search for more specific information about the ScienceWorld 84.6 score and 72.0 success rate mentioned in your query.

Links: [{"title":"Science World | Real-World Science Resource for Grades 6–10","url":"https://scienceworld.scholastic.com/"},{"title":"SCIENCEWORLD: Is your Agent Smarter than a 5","url":"https://par.nsf.gov/servlets/purl/10527040"},{"title":"Today - Science World","url":"https://www.scienceworld.ca/"},{"title":"Home - Science World - Scholastic","url":"https://scienceworld.scholastic.com/student-home-page-logged-in.html"},{"title":"[2203.07540] ScienceWorld: Is your Agent Smarter than a 5th Grader?","url":"https://arxiv.org/abs/2203.07540"},{"title":"Paper page - ScienceWorld: Is your Agent Smarter than a 5th Grader?","url":"https://huggingface.co/papers/2203.07540"},{"title":"General Admission Calendar - Science World","url":"https://tickets.scienceworld.ca/DateSelection.aspx?item=1"},{"title":"Select An Item - Science World","url":"https://tickets.scienceworld.ca/default.aspx?tagid=4"},{"title":"Coordination Number -- from Eric Weisstein's World of Chemistry","url":"https://scienceworld.wolfram.com/chemistry/CoordinationNumber.html"},{"title":"Plan Your Visit - Science World","url":"https://www.scienceworld.ca/your-visit/"}]

Let me search more specifically for CogRouter performance metrics on ScienceWorld.

No links found.

Based on my search results, I found information about CogRouter and the paper arXiv 2602.12662:

## CogRouter Overview

CogRouter is a framework that trains agents to dynamically adapt cognitive depth at each step. Grounded in ACT-R theory, it designs four hierarchical cognitive levels ranging from instinctive responses to strategic planning.

## Training Approach

The two-stage training approach includes Cognition-aware Supervised Fine-tuning (CoSFT) to instill stable level-specific patterns, and Cognition-aware Policy Optimization (CoPO) for step-level credit assignment via confidence-aware advantage reweighting.

## Performance Results

Experiments on ALFWorld and ScienceWorld demonstrate that CogRouter achieves state-of-the-art performance with superior efficiency. More specifically, with Qwen2.5-7B, it reaches an 82.3% success rate, outperforming GPT-4o (+40.3%), OpenAI-o3 (+18.3%), and GRPO (+14.0%), while using 62% fewer tokens.

However, the specific scores of 84.6 and 72.0 that you mentioned in your query do not appear in the search results I found. The primary reported ScienceWorld success rate for CogRouter is 82.3%, not 72.0%. If you have additional context about where the 84.6 and 72.0 figures come from, I'd be happy to search for more specific information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cccd239a-0302-478c-8f3c-a3983eb288d7",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "cccfa624-5466-4796-ad34-c1889d053b4c",
  "sourceToolAssistantUUID": "cccd239a-0302-478c-8f3c-a3983eb288d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-12T00:34:36.153Z_

The earlier HTML fetch from the CogRouter paper already confirmed the exact numbers. Let me now compile the full picture. Let me do one final check on whether Skill1 evaluates on ScienceWorld.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cccfa624-5466-4796-ad34-c1889d053b4c",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjeijsqGUXo2XzjhSWf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "506d3945-5ccb-4c3d-aa90-98c753d92e1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MqU31Yh5Euz98TV2EzCkNc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2841,
      "cache_read_input_tokens": 25329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2841,
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

_source line 63 · 2026-05-12T00:34:38.261Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M1mQjRJa9sGwxijRtZjxMF`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06130v1",
  "prompt": "Does this paper evaluate on ScienceWorld at all? Search the entire text for any mention of ScienceWorld. Also confirm: what are the exact ALFWorld and WebShop results? What is the base model? What is RetroAgent's ALFWorld score as reported in this paper's comparison tables?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "506d3945-5ccb-4c3d-aa90-98c753d92e1a",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011CawjeijsqGUXo2XzjhSWf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84e129be-7322-4c63-8e45-52b1a1a89d82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MqU31Yh5Euz98TV2EzCkNc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2841,
      "cache_read_input_tokens": 25329,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2841
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 25329,
          "cache_creation_input_tokens": 2841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2841,
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

_source line 64 · 2026-05-12T00:34:41.874Z_

<details><summary>↩ Tool result · `toolu_01M1mQjRJa9sGwxijRtZjxMF`</summary>

```text
# Analysis of Skill1 Paper

**ScienceWorld Evaluation:**
The paper does not mention ScienceWorld anywhere in the text. The evaluation is limited to two environments only.

**Exact Results:**

*ALFWorld:* "Skill1 reaches 97.5% average success rate" with specific task breakdowns: Pick (100.0%), Look (98.6%), Clean (97.3%), Heat (99.2%), Cool (96.1%), Pick2 (96.0%).

*WebShop:* The paper reports a score of 89.7 and success rate of 82.9%.

**Base Model:**
"Qwen2.5-7B-Instruct" serves as the initial policy for all experiments.

**RetroAgent's ALFWorld Score:**
According to the comparison table, RetroAgent achieved 94.9% average success rate on ALFWorld, with task-specific results: Pick (97.9%), Look (90.9%), Clean (99.2%), Heat (92.9%), Cool (85.3%), Pick2 (91.0%).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84e129be-7322-4c63-8e45-52b1a1a89d82",
  "isSidechain": true,
  "promptId": "eec29a9b-62cd-4776-9e42-7e642344d1e1",
  "agentId": "ad34a9275b82b1c42",
  "type": "user",
  "uuid": "71351858-9fcd-42ce-8510-a955ab7b1c48",
  "sourceToolAssistantUUID": "84e129be-7322-4c63-8e45-52b1a1a89d82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-12T00:35:21.896Z_

I now have comprehensive data. Here is the full verification report.

---

## Verification Report: CogRouter and Skill1 Benchmark Claims

### 1. CogRouter / "Think Fast and Slow" (arXiv 2602.12662)

**Paper confirmed** at [arxiv.org/abs/2602.12662](https://arxiv.org/abs/2602.12662). Published February 13, 2026. Code repo at [github.com/rhyang2021/CogRouter](https://github.com/rhyang2021/CogRouter) exists (setup instructions present, but no pre-trained weights mentioned in README).

**Claimed numbers -- VERIFIED from the paper's Table 1 (HTML full text):**

| Metric | Claimed | Found in Paper |
|---|---|---|
| ALFWorld SR | 92.5% | **92.5%** -- CONFIRMED |
| ScienceWorld Score | 84.6 | **84.6** -- CONFIRMED |
| ScienceWorld SR | 72.0% | **72.0%** -- CONFIRMED |
| Average SR | 82.3% | **82.3%** -- CONFIRMED |

Note: The 82.3% widely cited in abstracts/searches is the **average** of ALFWorld 92.5% and ScienceWorld 72.0%, not the ALFWorld-only number.

**Training approach confirmed:** CoSFT (Cognition-aware Supervised Fine-tuning) + CoPO (Cognition-aware Policy Optimization), four cognitive levels grounded in ACT-R theory, base model Qwen2.5-7B. Token consumption reduced by 62% vs GRPO.

**Key baselines from CogRouter's Table 1 (all Qwen2.5-7B):**
- GRPO: ALFWorld 83.5%, ScienceWorld 71.1 score / 53.0% SR
- GiGPO: ALFWorld 88.0%, ScienceWorld 67.3 score / 47.0% SR
- AdaptThink: ALFWorld 81.5%, ScienceWorld 62.5 score / 44.5% SR
- ETO: ALFWorld 69.5%, ScienceWorld 53.9 score / 21.5% SR
- GPT-4o: ALFWorld 61.5%, ScienceWorld 57.0 score / 22.5% SR
- OpenAI o3: ALFWorld 74.0%, ScienceWorld 72.4 score / 54.0% SR
- DeepSeek-R1: ALFWorld 73.0%, ScienceWorld 58.9 score / 40.0% SR

---

### 2. Skill1 (arXiv 2605.06130)

**Paper confirmed** at [arxiv.org/abs/2605.06130](https://arxiv.org/abs/2605.06130). Published May 2026.

**Claimed numbers -- VERIFIED from the paper's full text:**

| Metric | Claimed | Found in Paper |
|---|---|---|
| ALFWorld SR | 97.5% | **97.5%** -- CONFIRMED |

**Per-task ALFWorld breakdown:** Pick 100.0%, Look 98.6%, Clean 97.3%, Heat 99.2%, Cool 96.1%, Pick2 96.0%.

**WebShop results:** Score 89.7, SR 82.9%.

**Base model:** Qwen2.5-7B-Instruct (same family as CogRouter).

**Skill1 does NOT evaluate on ScienceWorld** -- the paper only benchmarks on ALFWorld and WebShop.

**Key baselines from Skill1's tables:**
- RetroAgent: ALFWorld 94.9%, WebShop score 88.9
- SkillRL: ALFWorld 89.9%, WebShop score 85.2
- GiGPO: ALFWorld 90.8%
- GRPO: ALFWorld 77.6%, WebShop score 79.3

---

### 3. ALFWorld SOTA as of May 2026

Based on all evidence gathered, the ALFWorld leaderboard (with 7B-class models) stands approximately as:

| Rank | Method | ALFWorld SR | Date |
|---|---|---|---|
| 1 | **Skill1** | **97.5%** | May 2026 |
| 2 | RetroAgent (RL-trained) | 95.6% (per its own paper) / 94.9% (per Skill1's table) | March 2026 |
| 3 | PA-MoE + GiGPO (1.5B) | 93.8% | Feb 2026 |
| 4 | **CogRouter** | **92.5%** | Feb 2026 |
| 5 | RLVMR | 91.6% | Feb 2026 |
| 6 | GiGPO | 90.2-90.8% | 2025 |

**Skill1 at 97.5% appears to be the current ALFWorld SOTA** for trained 7B-class models as of May 2026. The slight discrepancy in RetroAgent's number (95.6% in its own paper vs 94.9% in Skill1's table) likely reflects different evaluation splits or seeds.

---

### 4. ScienceWorld SOTA as of May 2026

ScienceWorld is less densely benchmarked than ALFWorld. Based on all results found:

| Rank | Method | Score | SR | Date |
|---|---|---|---|---|
| 1 | **CogRouter** | **84.6** | **72.0%** | Feb 2026 |
| 2 | OpenAI o3 (frontier) | 72.4 | 54.0% | (per CogRouter table) |
| 3 | GRPO (7B) | 71.1 | 53.0% | (per CogRouter table) |
| 4 | RLVMR (7B) | -- | 47.5% | Feb 2026 |
| 5 | GiGPO (7B) | 67.3 | 47.0% | (per CogRouter table) |

**CogRouter at 84.6 score / 72.0% SR appears to be the current ScienceWorld SOTA** among reported results. Notably, it surpasses even frontier models like OpenAI o3 (72.4 score / 54.0% SR) on this benchmark. Neither Skill1 nor RetroAgent evaluate on ScienceWorld, so there is no direct challenger from those papers.

---

### 5. Other Recent ScienceWorld Papers from 2026

- **CWM (Contrastive World Models)** -- arXiv 2602.22452: Improves action feasibility learning, reports +6.76pp improvement over SFT baseline in hardest conditions on ScienceWorld, but focuses on feasibility rather than task completion SOTA.
- **DPEPO** (April 2026): Mentioned as achieving higher performance on ScienceWorld but exact numbers were not extracted from search results.
- **EPO** (Feb 2026): Claims up to 152% improvement on ScienceWorld over its baseline, but absolute scores were not found in search results.
- **Skill1 and RetroAgent** do **not** report ScienceWorld results.

---

### Summary

Both papers' claimed numbers are **exactly verified**. CogRouter holds the apparent ScienceWorld SOTA (84.6/72.0%), while Skill1 holds the apparent ALFWorld SOTA (97.5%) as of May 2026.

Sources:
- [CogRouter paper (arXiv 2602.12662)](https://arxiv.org/abs/2602.12662)
- [CogRouter full text](https://arxiv.org/html/2602.12662)
- [Skill1 paper (arXiv 2605.06130)](https://arxiv.org/abs/2605.06130)
- [Skill1 full text](https://arxiv.org/html/2605.06130v1)
- [CogRouter GitHub](https://github.com/rhyang2021/CogRouter)
- [RetroAgent (arXiv 2603.08561)](https://arxiv.org/abs/2603.08561)
- [GiGPO paper](https://arxiv.org/html/2505.10978v1)
- [ScienceWorld benchmark](https://sciworld.apps.allenai.org/)
- [ScienceWorld topic page](https://www.emergentmind.com/topics/scienceworld-benchmark)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71351858-9fcd-42ce-8510-a955ab7b1c48",
  "isSidechain": true,
  "agentId": "ad34a9275b82b1c42",
  "requestId": "req_011Cawjfa6FihR5zzP2PjBy9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7e71fdf-f8ea-4be9-b705-1c9134fffd0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "775026df-7e5f-4612-a9ff-8196fc92ee39",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G9xbX1kw6am3wzxVdCSZty",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 455,
      "cache_read_input_tokens": 28170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 455,
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
