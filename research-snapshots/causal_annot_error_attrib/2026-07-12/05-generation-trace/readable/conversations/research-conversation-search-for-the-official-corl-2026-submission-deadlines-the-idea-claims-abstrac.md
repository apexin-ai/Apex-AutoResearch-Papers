# Research conversation: Search for the official CoRL 2026 submission deadlines. The idea claims abstract deadline is May 26 11:59 UTC and paper 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ae0b85cafd9f48ed3.jsonl`
- **Structured JSON:** [`e9835d5a8e8301e80391.json`](../../sessions/e9/e9835d5a8e8301e80391.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-14T06:18:17.583Z_

Search for the official CoRL 2026 submission deadlines. The idea claims abstract deadline is May 26 11:59 UTC and paper deadline is May 28-29. I need:
1. The exact abstract submission deadline
2. The exact paper submission deadline
3. The conference dates and location
4. Is it in Austin, TX?

Use WebSearch to find the official CoRL 2026 website and deadline information. Try searching "CoRL 2026 deadline", "CoRL 2026 call for papers", "corl2026.org".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae0b85cafd9f48ed3",
  "type": "user",
  "uuid": "5653bb24-f51c-48f0-9e05-f88735f3ee10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T06:18:17.586Z_

```json
{
  "parentUuid": "5653bb24-f51c-48f0-9e05-f88735f3ee10",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
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
  "uuid": "8a3424a2-a574-4166-a7ca-013f6b08568b",
  "timestamp": "2026-05-14T06:18:17.586Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T06:18:20.244Z_



I'll search for the CoRL 2026 deadline information. Let me first load the WebSearch tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a3424a2-a574-4166-a7ca-013f6b08568b",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yV5MUiLJ8t8d2Y4kVS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fee30750-7560-408d-a4e9-2c399e087504",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mFgToXqLfZHQkgezEwafn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 674,
      "cache_read_input_tokens": 8223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 674,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 4 · 2026-05-14T06:18:20.400Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PsDTypKJt5hLX35MksLsAe`</summary>

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
  "parentUuid": "fee30750-7560-408d-a4e9-2c399e087504",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yV5MUiLJ8t8d2Y4kVS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfdfb56c-988e-445d-a3dc-191d8f4055dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012mFgToXqLfZHQkgezEwafn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 674,
      "cache_read_input_tokens": 8223,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 674
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 8223,
          "cache_creation_input_tokens": 674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 674,
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

_source line 5 · 2026-05-14T06:18:20.403Z_

<details><summary>↩ Tool result · `toolu_01PsDTypKJt5hLX35MksLsAe`</summary>

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
  "parentUuid": "dfdfb56c-988e-445d-a3dc-191d8f4055dd",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae0b85cafd9f48ed3",
  "type": "user",
  "uuid": "fe3a7594-393f-413c-86ba-5663b9e9a9d5",
  "sourceToolAssistantUUID": "dfdfb56c-988e-445d-a3dc-191d8f4055dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-14T06:18:23.800Z_



Now let me search for the CoRL 2026 deadlines using multiple queries in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe3a7594-393f-413c-86ba-5663b9e9a9d5",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yVHmbtgT9eQfJNmhuc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76ad1840-7218-4a8c-90ad-a6330b1cbfa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GyjKwC9qXsDfvRqDdb11W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 7 · 2026-05-14T06:18:23.836Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TGwJt8HwPo2YBFVLTqf3PG`</summary>

```json
{
  "query": "CoRL 2026 deadline submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76ad1840-7218-4a8c-90ad-a6330b1cbfa4",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yVHmbtgT9eQfJNmhuc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e5b1a9ae-4ab8-4850-969d-6effe30a5c4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GyjKwC9qXsDfvRqDdb11W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 8 · 2026-05-14T06:18:24.151Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JyYJEi1czmyXY1joPNX86R`</summary>

```json
{
  "query": "CoRL 2026 call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5b1a9ae-4ab8-4850-969d-6effe30a5c4b",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yVHmbtgT9eQfJNmhuc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "78923317-5034-4da3-a005-1b0cb13b41b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GyjKwC9qXsDfvRqDdb11W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1913,
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

_source line 9 · 2026-05-14T06:18:24.376Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UZp9QZ1QpbPmni2EaMFUEL`</summary>

```json
{
  "query": "corl2026.org Conference on Robot Learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78923317-5034-4da3-a005-1b0cb13b41b8",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yVHmbtgT9eQfJNmhuc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b0e97a7-458b-4ee4-adcc-ab15bb3d7813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GyjKwC9qXsDfvRqDdb11W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1913,
      "cache_read_input_tokens": 8897,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 171,
          "cache_read_input_tokens": 8897,
          "cache_creation_input_tokens": 1913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1913,
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

_source line 10 · 2026-05-14T06:18:29.314Z_

<details><summary>↩ Tool result · `toolu_01TGwJt8HwPo2YBFVLTqf3PG`</summary>

```text
Web search results for query: "CoRL 2026 deadline submission"

Links: [{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 - Registration","url":"https://www.corl.org/attending/registration"}]

Based on the search results, here's the information about CoRL 2026 submission deadlines:

## CoRL 2026 Submission Deadlines

The abstract submission deadline is May 26, 2026 11:59 UTC and the paper submission deadline is May 29, 2026 11:59 UTC. However, there appears to be a note that the paper submission deadline is Thursday (5/28) EOD rather than Friday, so the actual deadline may be May 28, 2026.

## Key Details

- **Conference Location & Dates**: CoRL 2026 will be held in Austin, Texas, US, specifically November 9-12, 2026 at JW Marriott Austin.

- **Submission Platform**: Papers may be submitted through OpenReview via the link at https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference.

- **Format Requirements**: The page limit will be 8 pages for the main paper, and an additional 9th page is allowed for camera-ready submissions to incorporate reviewer feedback.

- **Important Note**: The deadlines are final, and they cannot make any accommodations for missing the abstract deadline or paper deadline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5b1a9ae-4ab8-4850-969d-6effe30a5c4b",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae0b85cafd9f48ed3",
  "type": "user",
  "uuid": "1d180d70-3f65-4ac7-8d27-c05dbba5efee",
  "sourceToolAssistantUUID": "e5b1a9ae-4ab8-4850-969d-6effe30a5c4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T06:18:30.682Z_

<details><summary>↩ Tool result · `toolu_01JyYJEi1czmyXY1joPNX86R`</summary>

```text
Web search results for query: "CoRL 2026 call for papers"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"CoRL 2026","url":"https://astrogeology.usgs.gov/pygeoapi//www.corl.org/"}]

Here are the results for the CoRL 2026 call for papers:

## Overview
The Conference on Robot Learning (CoRL) is an annual international conference aiming to bring together the robotics and machine learning research communities, focusing on the increasingly important role of learning in robotics and its interaction with other areas of robotics.

## Key Dates
- Abstract submission deadline: May 26, 2026 11:59 UTC
- Paper submission deadline: May 28, 2026 (AoE)
- Conference dates: November 10-12, 2026 (with workshops on November 9)

## Conference Details
CoRL 2026 will be held in Austin, Texas, US.

## Submission Requirements
Submissions should focus on a core robotics problem and demonstrate the relevance of proposed models, algorithms, datasets, and benchmarks to robotics. Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.

The page limit is 8 pages for the main paper, with acknowledgments, references, and appendix (optional) not counting towards the page limit.

Papers may be submitted through OpenReview via https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78923317-5034-4da3-a005-1b0cb13b41b8",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae0b85cafd9f48ed3",
  "type": "user",
  "uuid": "511ff620-5bd3-4c28-93c1-9770de399b1f",
  "sourceToolAssistantUUID": "78923317-5034-4da3-a005-1b0cb13b41b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T06:18:31.648Z_

<details><summary>↩ Tool result · `toolu_01UZp9QZ1QpbPmni2EaMFUEL`</summary>

```text
Web search results for query: "corl2026.org Conference on Robot Learning 2026"

Links: [{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - About CoRL","url":"https://www.corl.org/about-corl"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"2025 Conference on Robot Learning - CoRL","url":"https://www.corl.org/home"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"}]

I found information about the Conference on Robot Learning 2026. Here are the key details:

**About the Conference:**
The Conference on Robot Learning (CoRL) is an annual international conference focusing on the intersection of robotics and machine learning. Now in its 8th edition, the conference continues to draw a global audience of researchers, practitioners, and industry experts eager to present their findings, discuss challenges, and shape the future of robot learning.

**Location and Dates:**
CoRL 2026 will be held in Austin, Texas, US. More specifically, CoRL 2026 will be held at the JW Marriott Austin in Austin, TX (November 9–12, 2026), with a workshop day on November 9 and the main conference on November 10–12.

**Submission Deadlines:**
Abstract submission deadline is May 26, 2026 11:59 UTC and paper submission deadline is May 29, 2026 11:59 UTC.

**Focus Areas:**
The aim of CoRL 2026 is to publish significant original research at the intersection of robotics and machine learning. The conference welcomes papers in areas such as learning representations for robotic perception and control, imitation learning, reinforcement learning for control of physical robots, robot safety and alignment, applications in manipulation, navigation, locomotion, driving, and flight, and theoretical foundations of robot learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b0e97a7-458b-4ee4-adcc-ab15bb3d7813",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae0b85cafd9f48ed3",
  "type": "user",
  "uuid": "9a23a320-00d8-48dc-9e7a-bc7282e7303b",
  "sourceToolAssistantUUID": "9b0e97a7-458b-4ee4-adcc-ab15bb3d7813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-14T06:18:34.566Z_

Let me fetch the official Call for Papers page to get the exact deadlines with full precision.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a23a320-00d8-48dc-9e7a-bc7282e7303b",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yW7VFCDGcKGqR69qrX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19621a24-9d84-40d5-b4c1-d57af64ed4b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01625t72cD4sFnL5BCB2WwCW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2328,
      "cache_read_input_tokens": 10810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2328,
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

_source line 14 · 2026-05-14T06:18:36.066Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012x9VqDb6ZYZbxTKJCvYmkd`</summary>

```json
{
  "url": "https://www.corl.org/contributions/call-for-papers",
  "prompt": "Extract the exact submission deadlines (abstract deadline and paper deadline) with exact dates, times, and timezones. Also extract the conference dates and location. List every deadline mentioned on the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19621a24-9d84-40d5-b4c1-d57af64ed4b0",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yW7VFCDGcKGqR69qrX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebebe53f-9b9e-4f05-8953-12bab68a587c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01625t72cD4sFnL5BCB2WwCW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2328,
      "cache_read_input_tokens": 10810,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2328,
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

_source line 15 · 2026-05-14T06:18:36.941Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018vgo8Ze9XD1nYssQ7tYvDo`</summary>

```json
{
  "url": "https://www.corl.org/",
  "prompt": "Extract the exact conference dates, location, venue, and any submission deadlines mentioned on the CoRL 2026 homepage."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebebe53f-9b9e-4f05-8953-12bab68a587c",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yW7VFCDGcKGqR69qrX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f40a677-2726-4d22-93a9-b78fd77ddfda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01625t72cD4sFnL5BCB2WwCW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2328,
      "cache_read_input_tokens": 10810,
      "output_tokens": 228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2328
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 228,
          "cache_read_input_tokens": 10810,
          "cache_creation_input_tokens": 2328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2328,
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

_source line 16 · 2026-05-14T06:18:38.711Z_

<details><summary>↩ Tool result · `toolu_012x9VqDb6ZYZbxTKJCvYmkd`</summary>

```text
# Deadline and Conference Information

Unfortunately, the webpage content provided does not include specific submission deadlines, conference dates, or location details. 

The page references "Instruction for Authors" as the source for "paper submission format and timeline," but that linked content is not included in the provided text. The only temporal reference is "CoRL 2026," indicating the conference year.

To obtain the exact deadlines and conference details you're seeking, you would need to visit the [Instruction for Authors](/contributions/instruction-for-authors) page on the CoRL 2026 website.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebebe53f-9b9e-4f05-8953-12bab68a587c",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae0b85cafd9f48ed3",
  "type": "user",
  "uuid": "4aba5bce-2e11-47f7-90c9-dfcd7de526f3",
  "sourceToolAssistantUUID": "ebebe53f-9b9e-4f05-8953-12bab68a587c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T06:18:39.426Z_

<details><summary>↩ Tool result · `toolu_018vgo8Ze9XD1nYssQ7tYvDo`</summary>

```text
# CoRL 2026 Conference Details

**Conference Dates:**
"November 9-12, 2026" with workshops on November 9 and the main conference running November 10-12.

**Location:**
"Austin, Texas, US"

**Venue:**
JW Marriott Austin, located at "110 E 2nd St, Austin, TX 78701 USA"

**Submission Deadlines:**
The homepage does not specify exact submission deadlines. It only notes that "The Call for Papers and key dates are now available" (as of January 25), directing readers to the Call for Papers page for specific deadline information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f40a677-2726-4d22-93a9-b78fd77ddfda",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae0b85cafd9f48ed3",
  "type": "user",
  "uuid": "75d077f1-8f85-4df8-9a10-7ad76442f3d9",
  "sourceToolAssistantUUID": "8f40a677-2726-4d22-93a9-b78fd77ddfda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T06:18:43.218Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014pzqWrzC2GscZ8mahJuY6G`</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract ALL exact submission deadlines including abstract submission deadline and paper submission deadline. Include the exact dates, times, and timezones for each deadline. List every date/deadline mentioned on this page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75d077f1-8f85-4df8-9a10-7ad76442f3d9",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yWgjFVLDR54SLmtyRW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b04b1e1-ff19-45d2-853a-c608c9823d8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SBzMbk88XJvNrjVzz4HaCS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 13138,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 556
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 13138,
          "cache_creation_input_tokens": 556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 556,
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

_source line 19 · 2026-05-14T06:18:46.431Z_

<details><summary>↩ Tool result · `toolu_014pzqWrzC2GscZ8mahJuY6G`</summary>

```text
# CoRL 2026 Submission Deadlines

Based on the webpage content provided, here are the explicit deadlines mentioned:

## Stated Deadlines

**Paper Submission Deadline:** Thursday, May 28 (EOD) — The page notes: "the paper submission deadline is Thursday (5/28) EOD rather than Friday"

**Camera-Ready Submission Deadline:** October 12, 2026 (23:59 Anywhere on Earth)

## Additional Deadline References

The page references a "Rebuttal Process" section and mentions a "rebuttal deadline," but **does not provide specific dates** for:
- Abstract submission deadline
- Rebuttal deadline
- Reviewer assignment dates

The instructions state that "deadlines are final," but the specific dates for the abstract and rebuttal phases are not included in this document. These dates would likely be found in a separate schedule or announcement section of the CoRL 2026 website.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b04b1e1-ff19-45d2-853a-c608c9823d8c",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae0b85cafd9f48ed3",
  "type": "user",
  "uuid": "cc77a958-30dc-4674-a72b-097de6423942",
  "sourceToolAssistantUUID": "6b04b1e1-ff19-45d2-853a-c608c9823d8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T06:18:49.562Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VfsKb4VHLDVoKWkqbQJctp`</summary>

```json
{
  "url": "https://www.corl.org/contributions",
  "prompt": "Extract ALL submission deadlines, dates, and timeline information mentioned on this page. Include abstract deadline, paper deadline, review dates, notification dates, and any other dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc77a958-30dc-4674-a72b-097de6423942",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yXCioKEoVQm99dciTZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a87f5613-0080-4949-b826-c54704fbb0eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHZK3YpTttvtwos9ZmZWjC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 13694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 450,
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

_source line 21 · 2026-05-14T06:18:50.433Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LsaVBsNCwdpVTzK52XyQNo`</summary>

```json
{
  "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference",
  "prompt": "Extract ALL submission deadlines mentioned on this OpenReview page for CoRL 2026, including abstract deadline and paper submission deadline with exact dates, times, and timezones."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a87f5613-0080-4949-b826-c54704fbb0eb",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yXCioKEoVQm99dciTZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c2b86f9-5b34-4de8-bd86-4e4c162bc41b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHZK3YpTttvtwos9ZmZWjC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 13694,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 450
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 13694,
          "cache_creation_input_tokens": 450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 450,
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

_source line 22 · 2026-05-14T06:18:52.430Z_

<details><summary>↩ Tool result · `toolu_01LsaVBsNCwdpVTzK52XyQNo`</summary>

```text
Based on the web page content provided, **no submission deadlines are mentioned** for CoRL 2026. 

The page appears to be a navigation/header template for OpenReview.net rather than the actual CoRL 2026 conference details page. It contains only general site navigation elements, links to login, and footer information about OpenReview as an organization—not conference-specific information like submission deadlines.

To find CoRL 2026 submission deadlines, you would need to access the actual conference page on OpenReview.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c2b86f9-5b34-4de8-bd86-4e4c162bc41b",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae0b85cafd9f48ed3",
  "type": "user",
  "uuid": "f03b92be-741d-493f-a598-d016bba5923f",
  "sourceToolAssistantUUID": "7c2b86f9-5b34-4de8-bd86-4e4c162bc41b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T06:18:53.669Z_

<details><summary>↩ Tool result · `toolu_01VfsKb4VHLDVoKWkqbQJctp`</summary>

```text
# CoRL 2026 Submission Deadlines

Based on the page content provided, only one deadline is mentioned:

**Paper Submission Deadline:** "May 28, 2026 (AoE)"

This is the only specific date referenced on the Contributions page. The content does not include information about abstract deadlines, review timelines, notification dates, or other milestone dates for the conference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a87f5613-0080-4949-b826-c54704fbb0eb",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae0b85cafd9f48ed3",
  "type": "user",
  "uuid": "b8af0a0e-cee9-4b52-9b87-8cb8aa2d9903",
  "sourceToolAssistantUUID": "a87f5613-0080-4949-b826-c54704fbb0eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T06:18:56.572Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01N99CnrpC6iVwH4eiGk1a4g`</summary>

```json
{
  "url": "https://www.corl.org/annoucements",
  "prompt": "Extract ALL dates, deadlines, and timeline information mentioned on this page. Include abstract submission deadline, paper submission deadline, and any other important dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8af0a0e-cee9-4b52-9b87-8cb8aa2d9903",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yXjzyiXio3L877MTL7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e7a89d1-2ddd-480b-a171-2967814e61ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjLzBKCe4N3kZ7Cn3PpVCu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 146,
      "cache_creation_input_tokens": 348,
      "cache_read_input_tokens": 14144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 348,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 25 · 2026-05-14T06:18:57.086Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016mL223bd8Ko5F2nMRZ1eMS`</summary>

```json
{
  "query": "\"CoRL 2026\" \"abstract deadline\" \"May 26\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e7a89d1-2ddd-480b-a171-2967814e61ba",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yXjzyiXio3L877MTL7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf417bf8-85e5-4c82-b5c6-badd9c8563fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjLzBKCe4N3kZ7Cn3PpVCu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 146,
      "cache_creation_input_tokens": 348,
      "cache_read_input_tokens": 14144,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 348,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 26 · 2026-05-14T06:18:59.199Z_

<details><summary>↩ Tool result · `toolu_01N99CnrpC6iVwH4eiGk1a4g`</summary>

```text
# Dates and Timeline Information from CoRL 2026

Based on the page content, here are the dates and deadlines mentioned:

**Announcement Dates:**
- **04/29** - "Call for workshops" became available
- **04/17** - Author instructions were refreshed to incorporate generative AI guidelines
- **02/26** - The conference issued a call for corporate sponsors
- **01/25** - Paper submission guidelines and conference schedule were released

**Important Note:** The page does not contain specific submission deadlines, abstract deadlines, or paper closing dates. The announcements only indicate *when* various calls and instructions were published. To find actual submission deadlines, you would need to visit the linked pages such as "[Call for Papers](/contributions/call-for-papers)" or check the key dates section on the homepage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e7a89d1-2ddd-480b-a171-2967814e61ba",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae0b85cafd9f48ed3",
  "type": "user",
  "uuid": "f97dae16-a8bc-4f55-b365-8c683b9e9721",
  "sourceToolAssistantUUID": "8e7a89d1-2ddd-480b-a171-2967814e61ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T06:19:03.423Z_

<details><summary>↩ Tool result · `toolu_016mL223bd8Ko5F2nMRZ1eMS`</summary>

```text
Web search results for query: ""CoRL 2026" "abstract deadline" "May 26""

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"}]

Based on the search results, I found information about CoRL 2026 and the abstract deadline related to May 26:

The abstract submission deadline for CoRL 2026 is May 26, 2026 at 11:59 UTC. The conference will be held November 9-12, 2026 at JW Marriott Austin, 110 E 2nd St, Austin, TX 78701.

Additionally, the paper submission deadline is May 29, 2026 at 11:59 UTC, and the deadlines are final, and accommodations cannot be made for missing the abstract deadline or paper deadline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf417bf8-85e5-4c82-b5c6-badd9c8563fe",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae0b85cafd9f48ed3",
  "type": "user",
  "uuid": "1ef66648-8dd1-4233-a135-d3a38830e9c1",
  "sourceToolAssistantUUID": "bf417bf8-85e5-4c82-b5c6-badd9c8563fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-14T06:19:06.770Z_

Let me get the exact details from the Hugging Face AI deadlines commit and the Instruction for Authors page to resolve the discrepancy between May 28 and May 29 for the paper deadline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ef66648-8dd1-4233-a135-d3a38830e9c1",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yYTTLpkGKdBdVcs9E6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e58d43d4-ebe9-4fca-96d6-0f54047e98bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AhjX1Vt3Pzx6D6VKUGgeV6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1138,
      "cache_read_input_tokens": 14492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1138,
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

_source line 29 · 2026-05-14T06:19:07.706Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019rw2pWvkti8SyfxiuHWYKR`</summary>

```json
{
  "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf",
  "prompt": "Extract the exact CoRL 2026 deadlines listed in this commit, including abstract deadline and paper submission deadline with exact dates, times, and timezones."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e58d43d4-ebe9-4fca-96d6-0f54047e98bc",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yYTTLpkGKdBdVcs9E6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2225503-11b7-4a3b-869e-e782f4b3d915",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AhjX1Vt3Pzx6D6VKUGgeV6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1138,
      "cache_read_input_tokens": 14492,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1138
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 14492,
          "cache_creation_input_tokens": 1138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1138,
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

_source line 30 · 2026-05-14T06:19:10.013Z_

<details><summary>↩ Tool result · `toolu_019rw2pWvkti8SyfxiuHWYKR`</summary>

```text
# CoRL 2026 Deadlines

Based on the commit, here are the exact deadlines for CoRL 2026:

## Abstract Submission Deadline
- **Date & Time:** May 26, 2026 at 11:59 UTC
- **Format:** 2026-05-26 11:59:00 UTC

## Paper Submission Deadline
- **Date & Time:** May 29, 2026 at 11:59 UTC
- **Format:** 2026-05-29 11:59:00 UTC

## Additional Conference Details
- **Conference Dates:** November 9-12, 2026
- **Venue:** JW Marriott Austin, 110 E 2nd St, Austin, TX 78701
- **Schedule:** Workshops on Nov 9, main conference Nov 10-12
- **Location:** Austin, Texas, United States
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2225503-11b7-4a3b-869e-e782f4b3d915",
  "isSidechain": true,
  "promptId": "59215c78-0263-4ef6-a3ef-9ef3df37f095",
  "agentId": "ae0b85cafd9f48ed3",
  "type": "user",
  "uuid": "7b504395-2981-4b47-8a20-e967fdf09399",
  "sourceToolAssistantUUID": "c2225503-11b7-4a3b-869e-e782f4b3d915",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-14T06:19:21.865Z_

Now I have a clear picture. Let me summarize the findings.

Here are the CoRL 2026 deadline and conference details based on official sources:

---

**1. Abstract Submission Deadline:**
**May 26, 2026 at 11:59 UTC** -- This matches the claim exactly.

**2. Paper Submission Deadline:**
There is a slight discrepancy across sources:
- The official **Instruction for Authors** page on corl.org states the paper submission deadline is **Thursday, May 28, 2026 (EOD)**, explicitly noting "the paper submission deadline is Thursday (5/28) EOD rather than Friday."
- The **Hugging Face AI Deadlines** tracker and web search summaries list it as **May 29, 2026 at 11:59 UTC** (which is Friday).

The official corl.org site should be considered authoritative. The claim of "May 28-29" likely reflects this confusion. The safest interpretation is: **aim for May 28 EOD** per the official Instructions for Authors, though OpenReview may technically remain open until May 29 11:59 UTC.

**3. Conference Dates and Location:**
- **Dates:** November 9-12, 2026 (Workshops on Nov 9; main conference Nov 10-12)
- **Venue:** JW Marriott Austin, 110 E 2nd St, Austin, TX 78701

**4. Is it in Austin, TX?**
**Yes.** CoRL 2026 is confirmed to be held in Austin, Texas, US at the JW Marriott Austin.

---

**Key warning from the organizers:** "Deadlines are final" -- they explicitly state they cannot make accommodations for missing the abstract deadline or the paper deadline. Today is May 14, so you have **12 days** until the abstract deadline.

Sources:
- [CoRL 2026 Official Website](https://www.corl.org/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [CoRL 2026 on OpenReview](https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference)
- [Hugging Face AI Deadlines - CoRL 2026 Entry](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b504395-2981-4b47-8a20-e967fdf09399",
  "isSidechain": true,
  "agentId": "ae0b85cafd9f48ed3",
  "requestId": "req_011Cb1yYwV51kpQiiHN6shnj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bafe27f7-c459-4ca8-9869-8474c0b6ca1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a0e3a753-d9ef-4264-a82c-a92ffb3029a9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QC4tTj7SU4eW8HWzeDbcNV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 410,
      "cache_read_input_tokens": 15630,
      "output_tokens": 636,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 410
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 636,
          "cache_read_input_tokens": 15630,
          "cache_creation_input_tokens": 410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 410,
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
