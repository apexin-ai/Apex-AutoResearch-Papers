# Research conversation: I'm working on a paper about robot demonstration curation (filtering vs. weighting) targeting CoRL 2026 (deadline May 28

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ac8954d6827cada92.jsonl`
- **Structured JSON:** [`0796717a8b0fb0add396.json`](../../sessions/07/0796717a8b0fb0add396.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-13T11:41:19.894Z_

I'm working on a paper about robot demonstration curation (filtering vs. weighting) targeting CoRL 2026 (deadline May 28, 2026). Reviewers say sim-only evaluation is weak. I need to understand:

1. Use WebSearch to find: "CoRL 2026 call for papers", "CoRL 2026 submission requirements real robot" to understand reviewer expectations
2. Search for "ICRA 2026 From Data to Decisions VLA Pipelines Real Robots workshop" to understand community expectations
3. Search for recent demo curation papers that are sim-only vs. those with real-robot results. Specifically check what SCIZOR, Demo-SCORE, CUPID, TOPReward include for real-robot experiments.
4. Search for "VIP robot manipulation real world deployment" and "R3M real robot evaluation" to understand how easy it is to deploy these estimators on real hardware.

Report: (a) Is sim-only acceptable at CoRL 2026 for a primarily theoretical/framework paper? (b) What's the minimum real-robot experiment that would satisfy reviewers? (c) How feasible is adding real-robot experiments in ~2 weeks?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "ed3457eb-3b1d-41ac-a5ca-c62d26117b9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T11:41:19.897Z_

```json
{
  "parentUuid": "ed3457eb-3b1d-41ac-a5ca-c62d26117b9f",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
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
  "uuid": "305bd327-da5e-4acf-b695-1fae4b1ec922",
  "timestamp": "2026-05-13T11:41:19.897Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T11:41:22.707Z_



I'll conduct a thorough search across all these topics in parallel to build a comprehensive picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "305bd327-da5e-4acf-b695-1fae4b1ec922",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWJuxzzzox5zopoEbav",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "239f16d5-3d26-400a-a953-70c912a521e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1ji9tQzU2SQfpPnqYEbxG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 813,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 813,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 4 · 2026-05-13T11:41:22.976Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GyGVUQbGAawgDH4t22obRC`</summary>

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
  "parentUuid": "239f16d5-3d26-400a-a953-70c912a521e4",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWJuxzzzox5zopoEbav",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1e8e52b5-fd34-4cbc-924a-25813d876744",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1ji9tQzU2SQfpPnqYEbxG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 813,
      "cache_read_input_tokens": 8223,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 813
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 813,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 813,
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

_source line 5 · 2026-05-13T11:41:22.979Z_

<details><summary>↩ Tool result · `toolu_01GyGVUQbGAawgDH4t22obRC`</summary>

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
  "parentUuid": "1e8e52b5-fd34-4cbc-924a-25813d876744",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "d1017b64-a279-4831-8a7e-dffb5a23d92a",
  "sourceToolAssistantUUID": "1e8e52b5-fd34-4cbc-924a-25813d876744",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-13T11:41:25.279Z_



Now let me run all the searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1017b64-a279-4831-8a7e-dffb5a23d92a",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWK9W69KiYtE6ZgEXtH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3eec172-6796-4a1e-9a95-de52527d6106",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrnK4FAXUkkCxk1hmH4kbf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 7 · 2026-05-13T11:41:25.756Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HyZzy53AmsBX7NgkVcVikp`</summary>

```json
{
  "query": "CoRL 2026 call for papers submission requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3eec172-6796-4a1e-9a95-de52527d6106",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWK9W69KiYtE6ZgEXtH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f7900fa-3fa3-4d2a-9296-6478cbf59249",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrnK4FAXUkkCxk1hmH4kbf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 8 · 2026-05-13T11:41:26.202Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SMRThXWNLdnLFmZjNVkq12`</summary>

```json
{
  "query": "CoRL 2026 submission requirements real robot experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f7900fa-3fa3-4d2a-9296-6478cbf59249",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWK9W69KiYtE6ZgEXtH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23124dc8-e21b-481c-99de-569ca49f9d9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrnK4FAXUkkCxk1hmH4kbf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 9 · 2026-05-13T11:41:26.700Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0161RbcpqA6KpAePQp2yYFMr`</summary>

```json
{
  "query": "ICRA 2026 From Data to Decisions VLA Pipelines Real Robots workshop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23124dc8-e21b-481c-99de-569ca49f9d9b",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWK9W69KiYtE6ZgEXtH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c86f1688-767a-42aa-8388-2fcad255cf0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrnK4FAXUkkCxk1hmH4kbf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 10 · 2026-05-13T11:41:27.187Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QcKn7sqPrTjyb3QdCfEGwx`</summary>

```json
{
  "query": "SCIZOR robot demonstration curation paper real robot experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c86f1688-767a-42aa-8388-2fcad255cf0f",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWK9W69KiYtE6ZgEXtH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "68f45342-df90-41d9-997e-21edd0a57012",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrnK4FAXUkkCxk1hmH4kbf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1413,
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

_source line 11 · 2026-05-13T11:41:27.417Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MkJqMc1Us21jjpKQkug4Ai`</summary>

```json
{
  "query": "Demo-SCORE demonstration scoring curation robot learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68f45342-df90-41d9-997e-21edd0a57012",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWK9W69KiYtE6ZgEXtH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94058766-5678-40ef-afa8-a9008a77478d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrnK4FAXUkkCxk1hmH4kbf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 9036,
      "output_tokens": 264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1413
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 264,
          "cache_read_input_tokens": 9036,
          "cache_creation_input_tokens": 1413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1413,
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

_source line 12 · 2026-05-13T11:41:31.679Z_

<details><summary>↩ Tool result · `toolu_01SMRThXWNLdnLFmZjNVkq12`</summary>

```text
Web search results for query: "CoRL 2026 submission requirements real robot experiments"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Workshops","url":"https://www.corl.org/program/workshops"},{"title":"CoRL 2025 - Call for Papers","url":"https://2025.corl.org/contributions/call-for-papers"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2024 - Call for Papers","url":"https://2024.corl.org/contributions/call-for-papers"}]

Based on the search results, here are the key submission requirements for CoRL 2026 regarding real robot experiments:

## Real Robot Experiments Requirement

Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. This is not a strict requirement, but rather a strong encouragement for authors to validate their work on real hardware.

## General Submission Requirements

Beyond the real robot focus, CoRL 2026 submissions must meet these key requirements:

- **Page Limit**: 8 pages for the main paper, with Acknowledgments, References, and Appendix (optional) not counting towards the page limit.

- **Robotics Focus**: Submissions without a robotics focus will be returned without review.

- **Limitations Section**: All submissions should include a Limitations section, explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments and how these might be addressed in the future.

- **Supplementary Materials**: Authors are also encouraged to submit video, code and data as supplementary materials.

- **Reviewer Requirement**: All submissions must include at least one author who agrees to serve as a CoRL reviewer and is qualified if they have at least one accepted publication at a previous robotics (CoRL/ ICRA/ IROS/ RSS) or learning conference (ICLR/ NeurIPS/ ICML) or equivalent journal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23124dc8-e21b-481c-99de-569ca49f9d9b",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "db6a439c-6974-428f-8c0d-1fcff402e67a",
  "sourceToolAssistantUUID": "23124dc8-e21b-481c-99de-569ca49f9d9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T11:41:33.777Z_

<details><summary>↩ Tool result · `toolu_0161RbcpqA6KpAePQp2yYFMr`</summary>

```text
Web search results for query: "ICRA 2026 From Data to Decisions VLA Pipelines Real Robots workshop"

Links: [{"title":"From Data to Decisions: VLA Pipelines for Real Robots - ICRA 2026 Workshop","url":"https://icra2026vlapipeline.github.io/"},{"title":"AIRoA Announces ICRA 2026 Workshop — Launching a Global Competition on VLA Pipelines and Approximately 10,000 Hours of Real-World Robot Data — | AIRoA","url":"https://www.airoa.org/updates/2026-02-10"},{"title":"News | AIRoA","url":"https://www.airoa.org/news"},{"title":"Workshops & Tutorials - IEEE ICRA 2026","url":"https://2026.ieee-icra.org/workshops-and-tutorials/"},{"title":"ICRA 2026 Workshop: VLA Pipelines for Real Robot Systems","url":"https://www.linkedin.com/posts/junjungoal_from-data-to-decisions-vla-pipelines-for-activity-7426285548333453312-m_hV"},{"title":"IEEE ICRA 2026 Workshop From Data to Decisions | OpenReview","url":"https://openreview.net/group?id=IEEE.org%2FICRA%2F2026%2FWorkshop%2FFrom_Data_to_Decisions"},{"title":"ICRA 2026 - RIG","url":"https://robotics-institute-germany.de/event/icra-2026/"},{"title":"ICRA 2026","url":"https://ifr.org/event/icra-2026"},{"title":"Workshop on Open Challenges for Rigorous Robot Perception","url":"https://icra2026-rigorous-perception.github.io/"},{"title":"WS Uncertainty in Open-World Robotics","url":"https://uncertainty-in-robotics.github.io/"}]

Based on the search results, I can provide you with information about this workshop:

## From Data to Decisions: VLA Pipelines for Real Robots - ICRA 2026 Workshop

The workshop "From Data to Decisions: VLA Pipelines for Real Robots" has been accepted for presentation at ICRA 2026, which will be held in Vienna, Austria, from June 1–5, 2026. It is a full-day workshop co-located with ICRA 2026.

### Workshop Goals
The workshop features invited talks on cutting-edge work in data collection, training, evaluation, and real-world deployment, as well as a panel discussion on "How do we build trustworthy VLA pipelines?" The workshop aims to produce practical resources—datasets, evaluation protocols and baseline models—that the community can adopt, and to build a shared foundation that enables researchers and engineers from both academia and industry to deploy VLA models on real robots.

### International Competition
The workshop includes an international competition for VLA models focused on mobile manipulation. Participants can train on over 10,000 hours of data and evaluate their VLA systems on real robot hardware. A standardized environment based on Toyota's Human Support Robot (HSR) will be used for on-site evaluation on physical robots, conducted every two weeks.

### Paper Submissions
The workshop invites 2-page papers on any component of the VLA pipeline, including data collection via real robots, teleoperation, simulation, or web videos, and best practices for data curation, preprocessing, and annotation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c86f1688-767a-42aa-8388-2fcad255cf0f",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "f1238eae-0666-480b-a0e2-bda416aa0cc4",
  "sourceToolAssistantUUID": "c86f1688-767a-42aa-8388-2fcad255cf0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T11:41:34.687Z_

<details><summary>↩ Tool result · `toolu_01MkJqMc1Us21jjpKQkug4Ai`</summary>

```text
Web search results for query: "Demo-SCORE demonstration scoring curation robot learning"

Links: [{"title":"Demo-SCORE: Curating Demonstrations using Online Experience","url":"https://anniesch.github.io/demo-score/"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/abs/2603.09056"},{"title":"Curating Demonstrations using Online Experience","url":"https://arxiv.org/html/2503.03707"},{"title":"[2503.03707] Curating Demonstrations using Online Experience","url":"https://arxiv.org/abs/2503.03707"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121v1"},{"title":"Curating Demonstrations using Online Experience · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/71/"},{"title":"Robot Data Curation with Mutual Information Estimators","url":"https://arxiv.org/html/2502.08623"},{"title":"Illustration of Demo-SCORE. Our method self-curates demonstrations... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/llustration-of-Demo-SCORE-Our-method-self-curates-demonstrations-through-online-robot_fig2_389617044"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://cupid-curation.github.io/"}]

I found comprehensive information about Demo-SCORE. Here's what the search results show:

## Demo-SCORE Overview

Demo-SCORE is an approach for robots to self-curate based on online robot experience. The key insight is that when a policy is trained on heterogeneous demonstrations, its performance during rollouts can reveal which demonstrated strategies are most reliable, and Demo-SCORE leverages online policy rollout experiences to automatically curate reliable demonstrations.

## How It Works

The method trains and cross-validates a classifier to discern successful policy roll-outs from unsuccessful ones and uses the classifier to filter heterogeneous demonstration datasets. More specifically, the method self-curates demonstrations through online robot experience in four steps: (i) train a policy on the full demonstration set; (ii) evaluate the policy by generating rollouts with different checkpoints; (iii) use these rollouts to train and cross-validate a classifier that distinguishes between success and failure trajectories; (iv) filter out unreliable demonstrations based on the learned classifier, retaining only ones that do not reflect policy failures for subsequent policy training.

## Performance Results

Experiments in simulation and the real world show that Demo-SCORE can effectively identify suboptimal demonstrations without manual curation, achieving over 15-35% higher absolute success rate in the resulting policy compared to the base policy trained with all original demonstrations. Demo-SCORE also significantly outperforms prior approaches that leverage rollout data, like autonomous imitation learning, achieving almost 2x lower failure rate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94058766-5678-40ef-afa8-a9008a77478d",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "9a1edd8c-ecfe-4162-b4d6-8e2634f25476",
  "sourceToolAssistantUUID": "94058766-5678-40ef-afa8-a9008a77478d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-13T11:41:34.731Z_

<details><summary>↩ Tool result · `toolu_01QcKn7sqPrTjyb3QdCfEGwx`</summary>

```text
Web search results for query: "SCIZOR robot demonstration curation paper real robot experiments"

Links: [{"title":"[2505.22626] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/abs/2505.22626"},{"title":"SCIZOR: Self-Supervised Data Curation for Large-Scale Imitation Learning","url":"https://ut-austin-rpl.github.io/SCIZOR/"},{"title":"Scizor: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://arxiv.org/html/2505.22626v1"},{"title":"SCIZOR: A Self-Supervised Approach to Data Curation for ...","url":"https://openreview.net/pdf?id=Wo8eEdFUDF"},{"title":"(PDF) SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://www.researchgate.net/publication/392167457_SCIZOR_A_Self-Supervised_Approach_to_Data_Curation_for_Large-Scale_Imitation_Learning"},{"title":"[PDF] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SCIZOR:-A-Self-Supervised-Approach-to-Data-Curation-Zhang-Xie/1a601961be1a3facbacc68205b9279216e802c5c"},{"title":"[Literature Review] SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning","url":"https://www.themoonlight.io/en/review/scizor-a-self-supervised-approach-to-data-curation-for-large-scale-imitation-learning"},{"title":"Copyright by Yuqi Xie 2025 1","url":"https://repositories.lib.utexas.edu/bitstreams/d8256e22-405e-4881-87d8-ca3f8008345e/download"},{"title":"Huihan Liu on X: \"Our data curation work SCIZOR is accepted to ICRA 2026! Check out this self-supervised data curation approach that removes suboptimal and duplicated data for large-scale imitation learning, led by @YZ_Franklin @yuqi_xie5\" / X","url":"https://x.com/huihan_liu/status/2017698931493195899"},{"title":"GitHub - UT-Austin-RPL/SCIZOR · GitHub","url":"https://github.com/UT-Austin-RPL/SCIZOR"}]

I found comprehensive information about the SCIZOR paper. Here's a summary of the search results:

## SCIZOR: Self-Supervised Data Curation for Large-Scale Imitation Learning

SCIZOR is a self-supervised data curation framework that filters out low-quality state-action pairs to improve the performance of imitation learning policies. SCIZOR targets two complementary sources of low-quality data: suboptimal data, which hinders learning with undesirable actions, and redundant data, which dilutes training with repetitive patterns.

### Real Robot Experiments

The paper includes extensive real robot experiments. The framework was evaluated across three benchmarks: RoboMimic, Sirius-Fleet, and Open-X, with SCIZOR delivering absolute gains of 5.4% on RoboMimic, 8.1% on OXE-Magic-Soup, and 32.9% on the Sirius-Fleet real-robot tasks. These improvements demonstrate that SCIZOR's data curation consistently filters out low-quality samples and improves policy learning in both simulated and real-world robotic environments.

### Methodology

SCIZOR uses a self-supervised data curation pipeline that removes suboptimal transitions through a progress-prediction model and redundant transitions through joint visual-action embeddings clustering.

### Performance Comparisons

On the Sirius-Fleet dataset—where quality varies across human and policy data—SCIZOR outshone DemInf by 19.2%, highlighting the advantage of fine-grained state-action curation under uneven data distributions.

The paper was accepted to IEEE International Conference on Robotics and Automation (ICRA) 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68f45342-df90-41d9-997e-21edd0a57012",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "1256e22e-aa95-4f04-adcd-e2294c84b1b3",
  "sourceToolAssistantUUID": "68f45342-df90-41d9-997e-21edd0a57012",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T11:41:37.076Z_

<details><summary>↩ Tool result · `toolu_01HyZzy53AmsBX7NgkVcVikp`</summary>

```text
Web search results for query: "CoRL 2026 call for papers submission requirements"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"}]

Based on the search results, here are the key submission requirements for CoRL 2026:

## Paper Format and Content

All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments, and how these might be addressed in the future. Authors are strongly encouraged to include all relevant details in the main paper and the appendix to ensure that future researchers can reproduce the methodology and results. Authors are also encouraged to submit video, code and data as supplementary materials.

## Submission Timeline

The submission deadlines are: May 25 for abstract submission and May 28 for full paper submission, with the conference in Austin, TX on Nov 9-12.

## Originality and Dual Submission Policies

Papers that are identical or substantially similar to papers that have previously been published or accepted for publication in an archival venue, nor papers submitted in parallel to other conferences or archival venues, will not be accepted. However, submission is permitted for papers that have previously appeared only as a technical report, e.g., in arXiv.

## Reviewer Requirements

Every author with 3 or more submissions must agree to serve as a reviewer, though authors are exempt from the review requirement if they serve as an AC, an SAC, or another organizing chair for CoRL 2026.

## Generative AI Disclosure

During the paper submission process, authors will be asked to briefly disclose how generative AI tools were used for research and paper writing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f7900fa-3fa3-4d2a-9296-6478cbf59249",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "a3a5e360-f2ec-4928-a66e-f57c2a5d70f6",
  "sourceToolAssistantUUID": "2f7900fa-3fa3-4d2a-9296-6478cbf59249",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-13T11:41:39.809Z_

Good, now let me search for the remaining topics in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3a5e360-f2ec-4928-a66e-f57c2a5d70f6",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWLBRTVWURQhP6tEfEv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fc6bcd76-4450-40d0-9875-3c495a622f3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EGcqtR5EaCzsjqdYPpBeF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3543,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 10449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1076,
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

_source line 18 · 2026-05-13T11:41:40.228Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BsaqLewZ82EyE9fp5DWL3L`</summary>

```json
{
  "query": "CUPID demonstration curation influence functions robot real robot experiments 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc6bcd76-4450-40d0-9875-3c495a622f3e",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWLBRTVWURQhP6tEfEv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00bdf7c0-d9a6-49de-8020-fbc4326ccb96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EGcqtR5EaCzsjqdYPpBeF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3543,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 10449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1076,
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

_source line 19 · 2026-05-13T11:41:41.223Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MwoUfzfGYjHHsDCTaZdkp3`</summary>

```json
{
  "query": "TOPReward robot demonstration curation reward model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00bdf7c0-d9a6-49de-8020-fbc4326ccb96",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWLBRTVWURQhP6tEfEv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b534f95-5d58-48d6-8fe2-b1685e033379",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EGcqtR5EaCzsjqdYPpBeF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3543,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 10449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1076,
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

_source line 20 · 2026-05-13T11:41:41.699Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GHuNMrhHCrUEkVqJ36mvtk`</summary>

```json
{
  "query": "VIP value implicit pre-training robot manipulation real world deployment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b534f95-5d58-48d6-8fe2-b1685e033379",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWLBRTVWURQhP6tEfEv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53d86d6c-fb68-4923-bdb8-9b1bff26bc15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EGcqtR5EaCzsjqdYPpBeF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3543,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 10449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1076,
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

_source line 21 · 2026-05-13T11:41:42.643Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YDsuVY9LTNzJhERiywRk2W`</summary>

```json
{
  "query": "R3M real robot evaluation manipulation pre-trained representations deployment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53d86d6c-fb68-4923-bdb8-9b1bff26bc15",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWLBRTVWURQhP6tEfEv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea9aea05-a22d-40cf-97c1-c0194b044015",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EGcqtR5EaCzsjqdYPpBeF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3543,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 10449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1076,
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

_source line 22 · 2026-05-13T11:41:43.195Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014DpAVixhHEoT5NwtKU4Khz`</summary>

```json
{
  "query": "CoRL review criteria simulation only paper acceptance rate robot learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea9aea05-a22d-40cf-97c1-c0194b044015",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWLBRTVWURQhP6tEfEv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8746170a-65be-4065-837a-a5766ea4c35f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EGcqtR5EaCzsjqdYPpBeF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3543,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 10449,
      "output_tokens": 264,
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
          "input_tokens": 3543,
          "output_tokens": 264,
          "cache_read_input_tokens": 10449,
          "cache_creation_input_tokens": 1076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1076,
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

_source line 23 · 2026-05-13T11:41:46.465Z_

<details><summary>↩ Tool result · `toolu_01BsaqLewZ82EyE9fp5DWL3L`</summary>

```text
Web search results for query: "CUPID demonstration curation influence functions robot real robot experiments 2025 2026"

Links: [{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://cupid-curation.github.io/"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121v1"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions | OpenReview","url":"https://openreview.net/forum?id=TqevdDMqrK"},{"title":"GitHub - agiachris/cupid: Official repository for \"CUPID: Curating Data your Robot Loves with Influence Functions,\" accepted to CoRL 2025. · GitHub","url":"https://github.com/agiachris/cupid"},{"title":"CUPID: Robot Data Curation via Influence Functions","url":"https://www.emergentmind.com/papers/2506.19121"},{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"[2506.19121] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/abs/2506.19121"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://proceedings.mlr.press/v305/agia25a.html"},{"title":"[2506.19121v2] CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/abs/2506.19121v2"},{"title":"[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/abs/2603.09056"}]

Based on the search results, here's what I found about CUPID:

## Overview

CUPID (CUrating Performance-Influencing Demonstrations) is a data curation method for robot imitation learning that uses influence functions to estimate the causal impact of each demonstration on a policy's closed-loop performance, and was accepted to Conference on Robot Learning (CoRL) 2025.

## Method

Given a set of evaluation rollouts, CUPID estimates the influence of each training demonstration on the policy's expected return, which enables ranking and selection of demonstrations according to their impact on the policy's closed-loop performance.

CUPID curates data by 1) filtering out training demonstrations that harm policy performance and 2) subselecting newly collected trajectories that will most improve the policy.

## Experimental Results

Extensive simulated and hardware experiments show that the approach consistently identifies which data drives test-time performance. Training with less than 33% of curated data can yield state-of-the-art diffusion policies on the simulated RoboMimic benchmark, with similar gains observed in hardware.

The experiments take place across three simulated tasks from the RoboMimic benchmark suite and three real-world tasks with a Franka FR3 manipulator.

## Additional Capabilities

Hardware experiments show that the method can identify robust strategies under distribution shift, isolate spurious correlations, and even enhance the post-training of generalist robot policies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00bdf7c0-d9a6-49de-8020-fbc4326ccb96",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "d7e52ada-7c3a-44f8-b4e8-d7b44ffd7fda",
  "sourceToolAssistantUUID": "00bdf7c0-d9a6-49de-8020-fbc4326ccb96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T11:41:48.484Z_

<details><summary>↩ Tool result · `toolu_01YDsuVY9LTNzJhERiywRk2W`</summary>

```text
Web search results for query: "R3M real robot evaluation manipulation pre-trained representations deployment"

Links: [{"title":"[2203.12601] R3M: A Universal Visual Representation for Robot Manipulation","url":"https://ar5iv.labs.arxiv.org/html/2203.12601"},{"title":"(PDF) R3M: A Universal Visual Representation for Robot Manipulation","url":"https://www.researchgate.net/publication/359436519_R3M_A_Universal_Visual_Representation_for_Robot_Manipulation"},{"title":"GitHub - facebookresearch/r3m: Pre-training Reusable Representations for Robotic Manipulation Using Diverse Human Video Data · GitHub","url":"https://github.com/facebookresearch/r3m"},{"title":"R3M","url":"https://sites.google.com/view/robot-r3m/"},{"title":"[PDF] R3M: A Universal Visual Representation for Robot Manipulation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/R3M:-A-Universal-Visual-Representation-for-Robot-Nair-Rajeswaran/c9bdc9ad2c3cf3230ba9aac7b5783ab411f0d204"},{"title":"R3M: Visual Representation for Manipulation","url":"https://www.emergentmind.com/papers/2203.12601"},{"title":"Robots Pre-train Robots: Manipulation-Centric Robotic Representation from Large-Scale Robot Dataset","url":"https://arxiv.org/html/2410.22325v1"},{"title":"R3M: A Universal Visual Representation for Robot Manipulation | OpenReview","url":"https://openreview.net/forum?id=tGbpgz6yOrI&noteId=zBqc0qlBKpO"},{"title":"R3M: A Universal Visual Representation for Robot Manipulation | alphaXiv","url":"https://www.alphaxiv.org/abs/2203.12601"},{"title":"R3M: A Universal Visual Representation for Robot Manipulation. (arXiv:2203.12601v3 [cs.RO] UPDATED) · Issue #23668 · CoffeeKumazaki/arXiv","url":"https://github.com/CoffeeKumazaki/arXiv/issues/23668"}]

Based on the search results, here's what I found about R3M (Reusable Representations for Robotic Manipulation):

## Overview

R3M is a pre-trained reusable representation for robotic manipulation that can be used as a frozen perception module for downstream policy learning in simulated and real robot manipulation tasks.

## Pre-training Approach

R3M uses an objective that combines time contrastive learning, video-language alignment, and a sparsity penalty. It is pre-trained on the Ego4D human video dataset using a combination of time-contrastive learning, video-language alignment, and an L1 penalty to encourage sparse and compact representations.

## Evaluation Results

Across a comprehensive simulated evaluation suite including 3 visually distinct environments, 12 tasks total, and 3 viewpoints per environment, R3M provides consistent and substantial performance gains over existing pre-trained visual representations and learning from scratch. More specifically, R3M improves task success by over 20% compared to training from scratch and by over 10% compared to state-of-the-art visual representations like CLIP and MoCo.

## Real-World Deployment

R3M enables learning real-world manipulation tasks in a visually challenging household with just 10 minutes of human supervision. R3M enables a Franka Emika Panda arm to learn a range of manipulation tasks in a real, cluttered apartment given just 20 demonstrations.

The code and pre-trained models are available on GitHub at the official Facebook Research repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea9aea05-a22d-40cf-97c1-c0194b044015",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "ec8f2894-48d9-4f6d-97e5-327575ab71dd",
  "sourceToolAssistantUUID": "ea9aea05-a22d-40cf-97c1-c0194b044015",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-13T11:41:48.603Z_

<details><summary>↩ Tool result · `toolu_01MwoUfzfGYjHHsDCTaZdkp3`</summary>

```text
Web search results for query: "TOPReward robot demonstration curation reward model"

Links: [{"title":"GitHub - TOPReward/TOPReward: TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics · GitHub","url":"https://github.com/TOPReward/TOPReward"},{"title":"TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics","url":"https://arxiv.org/html/2602.19313v1"},{"title":"TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics","url":"https://topreward.github.io/webpage/"},{"title":"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons","url":"https://robometer.github.io/"},{"title":"[2602.19313] TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics","url":"https://arxiv.org/abs/2602.19313"},{"title":"TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.19313v1"},{"title":"Demonstration Shaped Reward Machine for Robot Assembly Reinforcement Learning Tasks | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-981-99-6495-6_20"},{"title":"GitHub - philfung/reward-scope: visually compare robot reward functions · GitHub","url":"https://github.com/philfung/reward-scope"},{"title":"Robot policy learning from demonstrations and visual rewards for sequential manipulation tasks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0921889025004087"},{"title":"Jiafei Duan on X: \"Really excited to see the community starting to build on our TOPReward. This is a really awesome interface that democratizes reward model for robotics and more! Check it out and try it out! https://t.co/6kYHvbnIIt\" / X","url":"https://x.com/DJiafei/status/2029045751117238567"}]

Based on the search results, here's what I found about TOPReward:

## Overview

TOPReward is a reward modeling method that uses token probabilities from vision-language models (VLMs) as zero-shot reward signals for robotics. It provides scalable, annotation-free reward estimation for robot learning and data curation.

## Key Innovation

TOPReward leverages the latent world knowledge of pretrained video Vision-Language Models to estimate robotic task progress, extracting task progress directly from the VLM's internal token logits rather than prompting VLMs to directly output progress values. Instead of prompting the VLM to output the value of the completion percentage in text space, TOPReward extracts the model's internal "belief" by analyzing the probabilistic distribution of its token logits, and by measuring the shift in confidence toward task-completion tokens over time, derives a continuous, well-posed progress signal directly from the VLM's latent world knowledge.

## Performance

In zero-shot evaluations across 130+ distinct real-world tasks and multiple robot platforms (Franka, YAM, SO-100/101), TOPReward achieves 0.947 mean Value-Order Correlation (VOC) on Qwen3-VL, dramatically outperforming the state-of-the-art GVL baseline which achieves near-zero correlation on the same open-source model.

## Applications

TOPReward serves as a versatile tool for downstream applications, including success detection and reward-aligned behavior cloning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b534f95-5d58-48d6-8fe2-b1685e033379",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "743f5497-b196-4fc3-b0b2-02d05ea84a7a",
  "sourceToolAssistantUUID": "9b534f95-5d58-48d6-8fe2-b1685e033379",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-13T11:41:48.634Z_

<details><summary>↩ Tool result · `toolu_014DpAVixhHEoT5NwtKU4Khz`</summary>

```text
Web search results for query: "CoRL review criteria simulation only paper acceptance rate robot learning"

Links: [{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2021 - Submission Instructions","url":"https://2021.corl.org/author-information/submission-instructions"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"Anca Dragan","url":"https://people.eecs.berkeley.edu/~anca/publications.html"},{"title":"CoRL 2023 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2023-statistics/"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CoRL 2021 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2021%2FConference"},{"title":"CoRL 2021 : Conference on Robot Learning - Accepted Papers, Deadline, Impact Factor & Score 2025 | Research.com","url":"https://research.com/conference/corl-2021-conference-on-robot-learning"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"}]

Based on the search results, I found relevant information about CoRL's review criteria regarding simulation-only papers:

CoRL reviewers are specifically instructed to question whether "An RL algorithm that works only in simulator X" transfers to real robot learning (sim2real, data efficiency, …). This indicates that simulation-only papers are evaluated with scrutiny, though the reviewer guidelines make clear that "You must demonstrate on a real robot!" is not a strict policy and not sufficient reason for rejection on its own.

However, I was unable to find specific information in these results about the actual acceptance rate for simulation-only papers versus papers with real robot experiments. The search results show authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots, but they don't provide statistical data on acceptance rates broken down by this criterion.

To get more specific information about acceptance rates for simulation-only papers at CoRL, you might want to check the OpenReview portal directly or reach out to the CoRL organizers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8746170a-65be-4065-837a-a5766ea4c35f",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "45ba3b3b-538a-4de5-bd72-0712fba9c741",
  "sourceToolAssistantUUID": "8746170a-65be-4065-837a-a5766ea4c35f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-13T11:41:48.982Z_

<details><summary>↩ Tool result · `toolu_01GHuNMrhHCrUEkVqJ36mvtk`</summary>

```text
Web search results for query: "VIP value implicit pre-training robot manipulation real world deployment"

Links: [{"title":"[2210.00030] VIP: Towards Universal Visual Reward and Representation via Value-Implicit Pre-Training","url":"https://arxiv.org/abs/2210.00030"},{"title":"VIP","url":"https://sites.google.com/view/vip-rl"},{"title":"VIP: Towards Universal Visual Reward and Representation via Value-Implicit Pre-Training | Dinesh Jayaraman","url":"https://www.seas.upenn.edu/~dineshj/publication/ma-2023-vip/"},{"title":"VIP: Towards Universal Visual Reward and Representation via Value-Implicit Pre-Training","url":"https://www.researchgate.net/publication/364126406_VIP_Towards_Universal_Visual_Reward_and_Representation_via_Value-Implicit_Pre-Training"},{"title":"VIP: Towards Universal Visual Reward and Representation via Value-Implicit Pre-Training | OpenReview","url":"https://openreview.net/forum?id=YJ7o2wetJ2"},{"title":"VIP: Towards Universal Visual Reward and Representation via Value-Implicit Pre-Training - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv221000030M/abstract"},{"title":"GitHub - facebookresearch/vip: Official repository for \"VIP: Towards Universal Visual Reward and Representation via Value-Implicit Pre-Training\" · GitHub","url":"https://github.com/facebookresearch/vip"},{"title":"NeurIPS VIP: Towards Universal Visual Reward and Representation via Value-Implicit Pre-Training","url":"https://neurips.cc/virtual/2022/60356"},{"title":"[2210.00030] Towards Universal Visual Reward and Representation via Value-Implicit Pre-Training","url":"https://ar5iv.labs.arxiv.org/html/2210.00030"},{"title":"Published as a conference paper at ICLR 2023","url":"https://openreview.net/pdf?id=YJ7o2wetJ2"}]

Based on the search results, here's information about VIP (Value-Implicit Pre-training) and its application to robot manipulation:

## Overview

VIP is a self-supervised pre-trained visual representation capable of generating dense and smooth reward functions for unseen robotic tasks.

## Methodology

VIP casts representation learning from human videos as an offline goal-conditioned reinforcement learning problem and derives a self-supervised dual goal-conditioned value-function objective that does not depend on actions, enabling pre-training on unlabeled human videos. Theoretically, VIP can be understood as a novel implicit time contrastive objective that generates a temporally smooth embedding, enabling the value function to be implicitly defined via the embedding distance, which can then be used to construct the reward for any goal-image specified downstream task.

## Real-World Deployment Results

Trained on large-scale Ego4D human videos and without any fine-tuning on in-domain, task-specific data, VIP's frozen representation can provide dense visual reward for an extensive set of simulated and real-robot tasks, enabling diverse reward-based visual control methods and significantly outperforming all prior pre-trained representations.

VIP can enable simple, few-shot offline RL on a suite of real-world robot tasks with as few as 20 trajectories. Additionally, VIP enables real-world few-shot offline RL with as few as 20 trajectories on a diverse suite of real-robot manipulation tasks, demonstrating that offline RL is possible in this low-data regime.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53d86d6c-fb68-4923-bdb8-9b1bff26bc15",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "6d96cae2-8995-49cc-9bc2-45702bf5030d",
  "sourceToolAssistantUUID": "53d86d6c-fb68-4923-bdb8-9b1bff26bc15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-13T11:41:51.376Z_

Let me get a few more targeted searches to fill in gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d96cae2-8995-49cc-9bc2-45702bf5030d",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWM4qMbpGK9b5RKXRFr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a59a4076-601d-4893-b89a-eaba563fb148",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lc5Pi7yZqREPiYN7PTwmoA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1655,
      "cache_creation_input_tokens": 6491,
      "cache_read_input_tokens": 11525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6491,
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

_source line 29 · 2026-05-13T11:41:52.601Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SXFHE6TMyr78K3aRUF9KeR`</summary>

```json
{
  "query": "Demo-SCORE robot real world experiments hardware Franka evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a59a4076-601d-4893-b89a-eaba563fb148",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWM4qMbpGK9b5RKXRFr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "784f5969-fa3e-4f36-89e6-c0f912dc282e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lc5Pi7yZqREPiYN7PTwmoA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1655,
      "cache_creation_input_tokens": 6491,
      "cache_read_input_tokens": 11525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6491,
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

_source line 30 · 2026-05-13T11:41:52.918Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MTZ3RoBFTAQu8xtRQk3byZ`</summary>

```json
{
  "query": "TOPReward demonstration curation data filtering robot experiments simulation only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "784f5969-fa3e-4f36-89e6-c0f912dc282e",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWM4qMbpGK9b5RKXRFr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8605d660-369f-49ef-b0b4-a4b05ba6de48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lc5Pi7yZqREPiYN7PTwmoA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1655,
      "cache_creation_input_tokens": 6491,
      "cache_read_input_tokens": 11525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6491,
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

_source line 31 · 2026-05-13T11:41:54.044Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TipzZwhLKqa8DxZFU9sf99`</summary>

```json
{
  "query": "robot demonstration filtering weighting two weeks real robot setup Franka minimal experiment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8605d660-369f-49ef-b0b4-a4b05ba6de48",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWM4qMbpGK9b5RKXRFr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "097d84cd-3af6-4213-95e0-59fdef54e4c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lc5Pi7yZqREPiYN7PTwmoA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1655,
      "cache_creation_input_tokens": 6491,
      "cache_read_input_tokens": 11525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6491,
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

_source line 32 · 2026-05-13T11:41:54.101Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LdY3yQ7RmvGN9ouzC94Tm5`</summary>

```json
{
  "query": "CoRL 2024 2025 simulation only paper accepted rejected real robot reviewer complaint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "097d84cd-3af6-4213-95e0-59fdef54e4c5",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWM4qMbpGK9b5RKXRFr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ea6ca15-5e0c-4d74-bbed-a8bf2746e463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lc5Pi7yZqREPiYN7PTwmoA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1655,
      "cache_creation_input_tokens": 6491,
      "cache_read_input_tokens": 11525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6491,
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

### Tool result

_source line 33 · 2026-05-13T11:42:00.063Z_

<details><summary>↩ Tool result · `toolu_01LdY3yQ7RmvGN9ouzC94Tm5`</summary>

```text
Web search results for query: "CoRL 2024 2025 simulation only paper accepted rejected real robot reviewer complaint"

Links: [{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2024-paper-list/"},{"title":"CoRL 2024 - Call for Papers","url":"https://2024.corl.org/contributions/call-for-papers"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"GitHub - smallfryy/corl-2025-papers: ✨ 200+ robotics papers from CoRL 2025, with TLDRs, project pages, code, and more","url":"https://github.com/smallfryy/corl-2025-papers"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"LEAP: Learning Effective Abstractions for Planning | CoRL 2025","url":"https://leap-workshop.github.io/"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL 2024 - Lifelong Learning for Home Robots","url":"https://llhomerobots.github.io/"}]

Based on the search results, I found information about CoRL's policies regarding simulation-only papers, but I did not find specific reports of accepted or rejected papers with reviewer complaints about simulation-only work.

Here's what the search revealed about CoRL's stance on simulation-only submissions:

Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots. This guideline appears in both CoRL 2024 and 2026 calls for papers.

Additionally, for submissions like "an RL algorithm that works only in simulator X," the question of whether "it transfer to real robot learning (sim2real, data efficiency, …)" is considered, and "according to the stated principles, the submission satisfies the intent" but "its failure or success to demonstrate the relevance will be determined during the review process."

However, the search results do not contain any public information about specific papers being accepted or rejected due to simulation-only concerns, nor any documented reviewer complaints about this matter for CoRL 2024 or 2025. The OpenReview platform hosts the official reviews, but these details are not captured in the general web search results.

If you're looking for specific information about individual papers or reviewer feedback, you may need to consult the OpenReview portal directly for CoRL 2024 or 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ea6ca15-5e0c-4d74-bbed-a8bf2746e463",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "9b4c6d7e-2faf-4122-b4a8-665669fa24fc",
  "sourceToolAssistantUUID": "8ea6ca15-5e0c-4d74-bbed-a8bf2746e463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-13T11:42:00.758Z_

<details><summary>↩ Tool result · `toolu_01TipzZwhLKqa8DxZFU9sf99`</summary>

```text
Web search results for query: "robot demonstration filtering weighting two weeks real robot setup Franka minimal experiment"

Links: [{"title":"Run with Franka Arm on Real Robot | serl","url":"https://rail-berkeley.github.io/serl/docs/real_franka.html"},{"title":"Real-world experimental setup: (a) Franka robot during measurements... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Real-world-experimental-setup-a-Franka-robot-during-measurements-with-installed-sensor_fig4_356596234"},{"title":"Using Franka Emika collaborative robot as a haptic device - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0957415824001521"},{"title":"Real robot setting. We use a Franka Research 3 robot arm equipped with... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Real-robot-setting-We-use-a-Franka-Research-3-robot-arm-equipped-with-a-UMI-gripper_fig2_401720624"},{"title":"Train Your First Robot Policy Using Free Tools | by Kg Aero | Mar, 2026 | Medium","url":"https://medium.com/@kg.aero/train-your-first-robot-policy-using-free-tools-612b07b539d6"},{"title":"RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation","url":"https://x-humanoid-robomind.github.io/"},{"title":"Immersive Demonstrations are the Key to Imitation Learning","url":"https://arxiv.org/pdf/2301.09157"},{"title":"The Franka Emika Robot: A Reference Platform for Robotics Research and Education | Request PDF","url":"https://www.researchgate.net/publication/358870212_The_Franka_Emika_Robot_A_Reference_Platform_for_Robotics_Research_and_Education"},{"title":"GitHub - TimSchneider42/franky: High-Level Control Library for Franka Robots with Python and C++ Support · GitHub","url":"https://github.com/TimSchneider42/franky"},{"title":"Kitchen Robot Case Studies: Learning Manipulation Tasks from","url":"https://www.ri.cmu.edu/app/uploads/2023/12/Dingkun_Guo_MSR_Thesis.pdf"}]

I've completed the web search for your query about robot demonstration filtering, weighting, two-week real robot setups with Franka, and minimal experiments. 

The search results include several relevant resources about Franka robot setups and real-world robotic experiments:

1. **SERL Documentation** - The peg insertion task is best for getting started with running SERL on a real robot, as the policy should converge and achieve 100% success rate within 30 minutes on a single GPU in the simplest case.

2. **Demonstration Collection Methods** - Multiple utility scripts have been provided to record demo trajectories, including record_demo.py for RLPD, record_transitions.py for training the reward classifier, and reward_bc_demos.py for bc policy.

3. **Minimal Robot Learning Setup** - One researcher kept the setup intentionally minimal, both in cost and complexity, with the goal not to build a high-performance robotics stack, but to validate the full process with tools that were already accessible.

4. **Real Robot Experimental Configurations** - The search results show various Franka robot setups with different configurations for data collection and robot learning tasks, including examples with filtering and quality control procedures.

Would you like me to search for more specific information about demonstration filtering techniques, weighting algorithms, or any other aspect of the query?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "097d84cd-3af6-4213-95e0-59fdef54e4c5",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "481eb9f0-0710-4f52-b0b9-48dccf779c29",
  "sourceToolAssistantUUID": "097d84cd-3af6-4213-95e0-59fdef54e4c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-13T11:42:00.838Z_

<details><summary>↩ Tool result · `toolu_01MTZ3RoBFTAQu8xtRQk3byZ`</summary>

```text
Web search results for query: "TOPReward demonstration curation data filtering robot experiments simulation only"

Links: [{"title":"Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/html/2603.09056"},{"title":"Robot Data Curation with Mutual Information Estimators","url":"https://arxiv.org/html/2502.08623v1"},{"title":"Curating Demonstrations using Online Experience","url":"https://arxiv.org/html/2503.03707"},{"title":"[2603.09056] Quality over Quantity: Demonstration Curation via Influence Functions for Data-Centric Robot Learning","url":"https://arxiv.org/abs/2603.09056"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121v1"},{"title":"[2502.08623] Robot Data Curation with Mutual Information Estimators","url":"https://arxiv.org/abs/2502.08623"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/0f7c964ef51527714b3964df61f35567d94b0e7b.pdf"},{"title":"Robot Data Curation with Mutual Information Estimators | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.08623v3"},{"title":"[2503.03707] Curating Demonstrations using Online Experience","url":"https://arxiv.org/abs/2503.03707"},{"title":"Multi-Stage Manipulation with Demonstration-Augmented Reward, Policy, and World Model Learning","url":"https://arxiv.org/html/2503.01837v1"}]

Based on the search results, I found several relevant papers on demonstration curation, data filtering, and robot experiments in simulation and real-world settings:

## Key Papers Found:

1. **Quality over Quantity (QoQ)**: A systematic approach to identifying high-quality data by defining data quality as the contribution of each training sample to reducing loss on validation demonstrations. The evaluation includes single task curation in the pick and place of a Coke can in simulation, and banana grasping experiment in a real robot.

2. **Robot Data Curation with Mutual Information Estimators (DemInf)**: A procedure for data curation in robot imitation learning that motivates mutual information as a useful basis for measuring the quality of individual demonstrations, and instantiates mutual information estimators as a way to rank and select demonstrations.

3. **Curating Demonstrations using Online Experience (Demo-SCORE)**: A method that curates demonstration datasets by pruning suboptimal examples estimated from online robot experience, with experiments in simulation and the real world showing that Demo-SCORE can effectively identify suboptimal demonstrations without manual curation.

4. **CUPID**: A novel approach for curating imitation learning datasets based on influence functions, causally linking demonstrations to the policy's expected return, with experiments across three simulated tasks from the RoboMimic benchmark suite and three real-world tasks with a Franka FR3 manipulator.

These papers all focus on demonstration curation, data filtering techniques, and robot learning through simulation and real-world experiments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8605d660-369f-49ef-b0b4-a4b05ba6de48",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "7aae01c5-b282-4a8c-824e-a7ba78ffbb7f",
  "sourceToolAssistantUUID": "8605d660-369f-49ef-b0b4-a4b05ba6de48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-13T11:42:02.988Z_

<details><summary>↩ Tool result · `toolu_01SXFHE6TMyr78K3aRUF9KeR`</summary>

```text
Web search results for query: "Demo-SCORE robot real world experiments hardware Franka evaluation"

Links: [{"title":"The real-world Franka robot arm experiments hardware platform. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/The-real-world-Franka-robot-arm-experiments-hardware-platform_fig2_391991780"},{"title":"Runway Research | Accelerating Robot Policy Evaluation with General World Models","url":"https://runwayml.com/research/accelerating-robot-policy-evaluation"},{"title":"Franka Research 3","url":"https://franka.de/franka-research-3"},{"title":"RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots","url":"https://arxiv.org/html/2406.02523v1"},{"title":"RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies","url":"https://arxiv.org/html/2506.18123v1"},{"title":"Frontiers | FOCUS: object-centric world models for robotic manipulation","url":"https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2025.1585386/full"},{"title":"RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation","url":"https://arxiv.org/html/2412.13877v1"},{"title":"The Franka Emika Robot: A Reference Platform for Robotics Research and Education | Request PDF","url":"https://www.researchgate.net/publication/358870212_The_Franka_Emika_Robot_A_Reference_Platform_for_Robotics_Research_and_Education"},{"title":"Benchmarking Model-based Con- trollers for Franka Emika Robot Description","url":"https://www.irl.iar.kit.edu/downloads/Thesis_Descriptions/23_BA_Robot_Control_Benchmark.pdf"},{"title":"Real-world experimental setup: (a) Franka robot during measurements... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Real-world-experimental-setup-a-Franka-robot-during-measurements-with-installed-sensor_fig4_356596234"}]

Based on the search results, I found information about real-world robot experiments using Franka hardware, though the results don't specifically mention a "Demo-SCORE" robot system. Here's what the search revealed:

## Real-World Robot Experiments with Franka Hardware

The search results show several significant real-world robotic evaluation frameworks and experiments using Franka robots:

### RoboArena Distributed Evaluation System
RoboArena is instantiated in a prototype evaluation system on the DROID robot platform, which consists of a Franka Panda 7DoF robot arm, a Robotiq 2F-85 parallel-jaw gripper, a ZED-mini stereo wrist camera and one or multiple external ZED 2 stereo cameras. This decentralized design allows RoboArena to be open-ended in the number of environments and tasks policies are evaluated on, robust, since many entities across the decentralized network contribute via double-blind evaluations to the final score, and scalable, with dozens of evaluators asynchronously contributing policy evaluations at any time of day.

### Other Franka-Based Real-World Evaluations
Real-world experiments have been conducted in kitchen environments with a Franka Emika Panda robot running on the DROID hardware infrastructure, and FOCUS has been deployed on a Franka Emika robot arm setup for real-world validation of object-centric world models.

**Note:** The search results don't contain specific information about a "Demo-SCORE" robot system. If you're looking for information about a specific Demo-SCORE method or system, you may want to provide additional context or search terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "784f5969-fa3e-4f36-89e6-c0f912dc282e",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "8051da24-987b-4e1b-b06a-1e172e8ff4d6",
  "sourceToolAssistantUUID": "784f5969-fa3e-4f36-89e6-c0f912dc282e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-13T11:42:05.669Z_

Let me do a final round of searches for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8051da24-987b-4e1b-b06a-1e172e8ff4d6",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWN6Azjo1PCA4egyUxm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91a3a900-0404-4e85-8e3a-8afbd996fdbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMnhA6odGzxnY8GjW3znZB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2575,
      "cache_creation_input_tokens": 2858,
      "cache_read_input_tokens": 18016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2858,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 38 · 2026-05-13T11:42:06.823Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015TvF9oTNSKJz9EVadntN2M`</summary>

```json
{
  "query": "Demo-SCORE RSS 2025 real robot experiments simulation hardware results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91a3a900-0404-4e85-8e3a-8afbd996fdbc",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWN6Azjo1PCA4egyUxm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8af3398e-49b9-4bc0-9af6-727021762f11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMnhA6odGzxnY8GjW3znZB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2575,
      "cache_creation_input_tokens": 2858,
      "cache_read_input_tokens": 18016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2858,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 39 · 2026-05-13T11:42:07.208Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014PaUeSPAjCpBognKSGMWPy`</summary>

```json
{
  "query": "DemInf robot data curation mutual information real robot simulation only"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8af3398e-49b9-4bc0-9af6-727021762f11",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWN6Azjo1PCA4egyUxm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96ffd674-13dc-4338-8e86-38153ab1c457",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMnhA6odGzxnY8GjW3znZB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2575,
      "cache_creation_input_tokens": 2858,
      "cache_read_input_tokens": 18016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2858,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 40 · 2026-05-13T11:42:07.959Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016a9oiQ7ZUq9pn6CvmTdghg`</summary>

```json
{
  "query": "CoRL 2024 review instruction \"real robot\" \"simulation\" evaluation criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96ffd674-13dc-4338-8e86-38153ab1c457",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWN6Azjo1PCA4egyUxm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ac94ced-ced7-4fb1-9090-c9f488ea59cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMnhA6odGzxnY8GjW3znZB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2575,
      "cache_creation_input_tokens": 2858,
      "cache_read_input_tokens": 18016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2858,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 41 · 2026-05-13T11:42:11.397Z_

<details><summary>↩ Tool result · `toolu_015TvF9oTNSKJz9EVadntN2M`</summary>

```text
Web search results for query: "Demo-SCORE RSS 2025 real robot experiments simulation hardware results"

Links: [{"title":"Brain and Brawn: 1st Workshop on Robot Hardware-Aware Intelligence","url":"https://rss-hardware-intelligence.github.io/"},{"title":"RSS 2025","url":"https://www.robot-manipulation.org/events/workshops/rss-2025"},{"title":"Call for Papers and Demos · Robotics: Science and Systems","url":"https://roboticsconference.org/2025/information/cfp/"},{"title":"Precision home robots learn with real-to-sim-to-real | MIT News | Massachusetts Institute of Technology","url":"https://news.mit.edu/2024/precision-home-robotics-real-sim-real-0731"},{"title":"RSS 2025 WORKSHOP - Home","url":"https://lfmrss2025.weebly.com/"},{"title":"Competitions - IEEE ICRA 2025","url":"https://2025.ieee-icra.org/competitions/"},{"title":"Demos · Robotics: Science and Systems","url":"https://roboticsconference.org/2025/program/demos/"},{"title":"RSS 2025 Marks Largest in History as Conference Returns to USC - USC Viterbi | School of Engineering","url":"https://viterbischool.usc.edu/news/2025/07/rss-2025-marks-largest-in-history-as-conference-returns-to-usc/"},{"title":"RSS: Robotics: Science and Systems 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2506&f=Robotics"},{"title":"RSS2025 - Structured World Models for Robotic Manipulation","url":"https://swomo-rss.github.io/"}]

Based on my search results, I was unable to find specific information about "Demo-SCORE" as a particular research project or benchmark related to RSS 2025. The search returned general information about RSS 2025 conferences and workshops, including various robotics competitions and demonstrations, but nothing specifically matching that exact query.

The results do show that RSS 2025 is planned as an in-person event with demo submissions possible for RSS 2025 contributors, which can range from early research demos to mature production-ready systems.

If you're looking for information about a specific robotics research paper or project with "Demo-SCORE" in the title, could you provide additional context or clarification? For instance:
- Is this a paper submitted to RSS 2025?
- Is it related to a specific robotics lab or research group?
- Do you have any other identifying information?

This would help me conduct a more targeted search to find the specific information you're looking for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8af3398e-49b9-4bc0-9af6-727021762f11",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "76cb0694-4ef8-4f39-bb65-5f1df913cd4a",
  "sourceToolAssistantUUID": "8af3398e-49b9-4bc0-9af6-727021762f11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-13T11:42:14.197Z_

<details><summary>↩ Tool result · `toolu_016a9oiQ7ZUq9pn6CvmTdghg`</summary>

```text
Web search results for query: "CoRL 2024 review instruction "real robot" "simulation" evaluation criteria"

Links: [{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"USC at the Conference of Robot Learning (CoRL) 2024 - USC Viterbi | School of Engineering","url":"https://viterbischool.usc.edu/news/2024/11/usc-at-the-conference-of-robot-learning-corl-2024/"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"CoRL 2024 - Call for Papers","url":"https://2024.corl.org/contributions/call-for-papers"},{"title":"CoRL 2024 - Lifelong Learning for Home Robots","url":"https://llhomerobots.github.io/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2024 Workshop on Mastering Robot Manipulation in a World of Abundant Data | Dynamic Systems Lab | Prof. Angela Schoellig","url":"https://www.dynsyslab.org/mastering-robot-manipulation-in-a-world-of-abundant-data/"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"Call for Papers — CoRL 2023","url":"https://www.corl2023.org/call-for-papers"},{"title":"CoRL 2024","url":"https://2024.corl.org/"}]

I found the CoRL 2024 review instructions. Here are the key evaluation criteria related to real robot and simulation:

## Main Evaluation Criteria

Submissions are evaluated based on the significance and novelty of results (either theoretical or empirical), judged on how objectively the results have been established and their potential for scientific and technological impact, as well as relevance to robotic learning.

## Real Robot vs. Simulation Guidance

Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.

The instructions also include specific guidance on what constitutes sufficient robotics relevance. For example, for RL algorithms that work only in simulation, the question is whether it transfers to real robot learning (sim2real, data efficiency, etc.) - with CARLA for autonomous driving being acceptable for CoRL, but Cheetah/Humanoid in Mujoco not meeting the robotics focus requirement.

## Important Note on Requirements

Demonstrating on a real robot is not a strict policy and not a sufficient reason for rejection. The emphasis is on demonstrating relevance to robotics rather than requiring physical robot experiments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ac94ced-ced7-4fb1-9090-c9f488ea59cd",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "d6a3c3c1-c427-4002-b4d9-730782b9f561",
  "sourceToolAssistantUUID": "7ac94ced-ced7-4fb1-9090-c9f488ea59cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-13T11:42:14.534Z_

<details><summary>↩ Tool result · `toolu_014PaUeSPAjCpBognKSGMWPy`</summary>

```text
Web search results for query: "DemInf robot data curation mutual information real robot simulation only"

Links: [{"title":"Robot Data Curation with Mutual Information Estimators","url":"https://arxiv.org/html/2502.08623v1"},{"title":"Robot Data Curation with Mutual Information Estimators | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.08623v3"},{"title":"[2502.08623] Robot Data Curation with Mutual Information Estimators","url":"https://arxiv.org/abs/2502.08623"},{"title":"GitHub - jhejna/demonstration-information: Code for the paper Robot Data Curation with Mutual Information Estimators","url":"https://github.com/jhejna/demonstration-information"},{"title":"Robot Data Curation with Mutual Information Estimators · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/23/"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://arxiv.org/html/2506.19121v1"},{"title":"CUPID: Curating Data your Robot Loves with Influence Functions","url":"https://cupid-curation.github.io/"},{"title":"[PDF] Robot Data Curation with Mutual Information Estimators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Robot-Data-Curation-with-Mutual-Information-Hejna-Mirchandani/37cb83dc757f483cfd389c8709b4aee389da8dc6"},{"title":"DATAMIL: SELECTING DATA FOR ROBOT IMITATION ...","url":"https://openreview.net/pdf/82e6c304571ad1e85b44780f29e82e7042b2743f.pdf"},{"title":"DataMIL : Selecting Data for Robot Imitation Learning with Datamodels","url":"https://arxiv.org/html/2505.09603v1"}]

I found comprehensive information about the DemInf method for robot data curation. Here's what I found:

## Overview

DemInf considers the mutual information between states and actions to curate demonstrations. DemInf is an unsupervised, offline method developed by researchers from Google DeepMind Robotics and Stanford University that estimates mutual information between states and actions to curate robot demonstration datasets.

## Methodology

The goal is to estimate the relative quality of individual demonstrations in terms of both action diversity and predictability by estimating the average contribution of a trajectory towards the mutual information between states and actions in the entire dataset, which captures both the entropy of the marginal action distribution and the state-conditioned action entropy.

Though commonly used mutual information estimators require vast amounts of data often beyond the scale available in robotics, a novel technique based on k-nearest neighbor estimates of mutual information on top of simple VAE embeddings of states and actions is introduced.

## Experimental Results

On RoboMimic tasks, DemInf-filtered data results in 5-10% improvements in success rates compared to training on all available data. Real-world experiments on ALOHA and Franka systems confirm these improvements translate to physical robot performance.

The approach is able to partition demonstration datasets by quality according to human expert scores across a diverse set of benchmarks spanning simulation and real world environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "96ffd674-13dc-4338-8e86-38153ab1c457",
  "isSidechain": true,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "agentId": "ac8954d6827cada92",
  "type": "user",
  "uuid": "04ebd0cf-5536-45dd-ae82-e2839c7074f9",
  "sourceToolAssistantUUID": "96ffd674-13dc-4338-8e86-38153ab1c457",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-13T11:43:11.013Z_

Now I have a comprehensive picture. Here is my report.

---

## Report: Sim-Only vs. Real-Robot Experiments for CoRL 2026 Demo Curation Paper

### (a) Is sim-only acceptable at CoRL 2026 for a primarily theoretical/framework paper?

**Technically yes, but practically risky -- especially for a demo curation paper.**

CoRL 2026's official call for papers states: *"Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots."* The CoRL 2024 reviewer instructions (which CoRL 2026 follows the same tradition) explicitly say: *"You must demonstrate on a real robot! is not a strict policy and not sufficient reason for rejection on its own."*

However, there are important caveats:

1. **Your paper is empirical, not theoretical.** The "sim-only is OK for theoretical papers" exception applies to things like convergence proofs or novel RL algorithms with formal guarantees. A demo curation paper (filtering vs. weighting) is fundamentally an empirical contribution. Reviewers will ask: "Does this actually work on messy real-world data?"

2. **Every competing paper in this space now includes real-robot results.** The competitive landscape has shifted dramatically:
   - **CUPID** (CoRL 2025): 3 simulated RoboMimic tasks + **3 real-world tasks on Franka FR3**
   - **SCIZOR** (ICRA 2026): RoboMimic + OXE + **Sirius-Fleet real-robot tasks** (32.9% gains)
   - **Demo-SCORE** (RSS 2025): Sim + **real-world experiments** (15-35% absolute success rate gains)
   - **DemInf** (RSS 2025): RoboMimic sim + **real-world ALOHA and Franka experiments**
   - **TOPReward**: Evaluated on **130+ real-world tasks across Franka, YAM, SO-100/101**

   A sim-only submission would be an outlier in this subfield, and reviewers will notice.

3. **Community expectations are rising.** The ICRA 2026 "From Data to Decisions: VLA Pipelines for Real Robots" workshop explicitly centers real-robot deployment, including a competition with physical robot evaluation. This signals that the community considers real-hardware validation essential for data pipeline work.

**Bottom line:** A sim-only submission is not auto-rejected, but you would be swimming upstream. Expect at least one reviewer to flag it as a significant weakness, and the AC will see that every comparable accepted paper had real-robot results.

### (b) What's the minimum real-robot experiment that would satisfy reviewers?

Based on what the accepted papers in this space include, the minimum viable real-robot experiment is:

1. **1-2 manipulation tasks** on a single robot platform (Franka Panda/FR3 is the most common; ALOHA is another option). Pick tasks where demonstration quality naturally varies -- e.g., pick-and-place with varying object positions, or a task where teleoperation quality differs across operators.

2. **Show the curation pipeline end-to-end:** Collect ~50-100 demonstrations (mix of good and poor quality), run your filtering/weighting method, train a policy on curated vs. uncurated data, and report success rates over 20+ evaluation rollouts.

3. **One table or figure** showing: (i) baseline (all demos), (ii) your method (filtered/weighted), (iii) at least one competing curation method (e.g., DemInf or random subsampling). Even 2-3 tasks with clear trends is sufficient -- CUPID used exactly 3 real tasks.

4. **A supplementary video** showing the robot executing the task with curated vs. uncurated policies. This is strongly encouraged by CoRL and is highly persuasive for reviewers.

The bar is NOT: dozens of tasks, multiple robot platforms, or extensive ablations on hardware. A focused, clean experiment on 1-2 tasks that validates your sim findings transfers is sufficient.

### (c) How feasible is adding real-robot experiments in ~2 weeks (by May 28)?

**Feasible but tight. Here's the realistic breakdown:**

**If you already have access to a robot platform (Franka, ALOHA, etc.):**
- Days 1-2: Set up data collection pipeline (teleoperation interface, camera calibration). If using an existing framework like SERL or robomimic's data collection tools, this is faster.
- Days 3-5: Collect demonstrations (~50-100 demos for 1-2 tasks). Budget 1-2 days per task for collection at ~2-3 min per demo.
- Days 5-7: Run your curation method on collected data (this should be fast if your sim pipeline works).
- Days 7-10: Train policies on curated vs. uncurated datasets and run evaluation rollouts (20-50 per condition).
- Days 10-13: Write up results, create video, integrate into paper.
- Day 14: Buffer for things going wrong (they always do).

**Key enablers that make this easier:**
- **VIP and R3M** both have open-source pre-trained models from Facebook Research that work out-of-the-box as frozen feature extractors on real robot images. VIP demonstrated real-world few-shot offline RL with as few as 20 trajectories. R3M enabled real manipulation with just 20 demonstrations and 10 minutes of supervision. If your curation method uses these representations, deployment is straightforward.
- **SERL** documentation notes that their simplest real-robot setup (peg insertion on Franka) converges within 30 minutes on a single GPU, showing that minimal real experiments are achievable quickly.

**If you do NOT have robot access:**
- This is the critical bottleneck. Securing robot time at a collaborator's lab on short notice is possible but uncertain. Consider: (1) reaching out to collaborators immediately, (2) using a low-cost platform like SO-100/LeRobot if available, or (3) contacting your institution's robotics lab about emergency access.

**Risk mitigation -- if real-robot experiments are truly impossible in 2 weeks:**
- Include a strong Limitations section acknowledging sim-only evaluation and commit to real-robot validation.
- Use the most realistic simulators possible (e.g., RoboMimic, ManiSkill with realistic rendering).
- Show your method works on real-world datasets like Open X-Embodiment or Sirius-Fleet even if you cannot run the robot yourself (curating existing real data and training on it is partial real-world validation).
- Submit to the workshop track or include an appendix with concrete plans for real experiments.

**My recommendation:** If you have robot access, spend the next 2 weeks doing a focused 2-task real-robot experiment. It does not need to be exhaustive -- just enough to show the sim findings transfer. Given that your deadline is May 28 and today is May 13, you have exactly 15 days, which is tight but doable for a minimal experiment. Start data collection immediately.

---

Sources:
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [CoRL 2024 Instruction for Reviews](https://2024.corl.org/contributions/instruction-for-reviews)
- [CoRL 2023 Reviewer Guidelines](https://www.corl2023.org/reviewer-guidelines)
- [ICRA 2026 From Data to Decisions Workshop](https://icra2026vlapipeline.github.io/)
- [SCIZOR Paper (ICRA 2026)](https://arxiv.org/abs/2505.22626)
- [SCIZOR Project Page](https://ut-austin-rpl.github.io/SCIZOR/)
- [Demo-SCORE Project Page](https://anniesch.github.io/demo-score/)
- [Demo-SCORE at RSS](https://roboticsconference.org/program/papers/71/)
- [CUPID Paper (CoRL 2025)](https://arxiv.org/abs/2506.19121)
- [CUPID Project Page](https://cupid-curation.github.io/)
- [CUPID GitHub](https://github.com/agiachris/cupid)
- [DemInf Paper](https://arxiv.org/abs/2502.08623)
- [DemInf at RSS](https://roboticsconference.org/program/papers/23/)
- [TOPReward Project Page](https://topreward.github.io/webpage/)
- [TOPReward Paper](https://arxiv.org/abs/2602.19313)
- [VIP Paper (ICLR 2023)](https://arxiv.org/abs/2210.00030)
- [VIP Project Page](https://sites.google.com/view/vip-rl)
- [VIP GitHub](https://github.com/facebookresearch/vip)
- [R3M Paper](https://ar5iv.labs.arxiv.org/html/2203.12601)
- [R3M GitHub](https://github.com/facebookresearch/r3m)
- [R3M Project Page](https://sites.google.com/view/robot-r3m/)
- [SERL Real Franka Setup](https://rail-berkeley.github.io/serl/docs/real_franka.html)
- [Quality over Quantity (QoQ) Paper](https://arxiv.org/abs/2603.09056)
- [CoRL 2026 OpenReview](https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04ebd0cf-5536-45dd-ae82-e2839c7074f9",
  "isSidechain": true,
  "agentId": "ac8954d6827cada92",
  "requestId": "req_011CazWNwZMZn3CX5WnXTmLB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b80455bd-9ac3-4ac3-9f90-2541f1c7b075",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJQcRbpiAbfZqX6dLKLpBd",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 745,
      "cache_creation_input_tokens": 4298,
      "cache_read_input_tokens": 20874,
      "output_tokens": 2385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4298
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 745,
          "output_tokens": 2385,
          "cache_read_input_tokens": 20874,
          "cache_creation_input_tokens": 4298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4298,
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
