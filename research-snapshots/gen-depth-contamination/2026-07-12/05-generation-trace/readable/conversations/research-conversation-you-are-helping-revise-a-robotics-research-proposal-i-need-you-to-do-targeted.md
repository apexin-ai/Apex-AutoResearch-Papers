# Research conversation: You are helping revise a robotics research proposal. I need you to do targeted web research to address specific reviewer

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 84
- **Recorded user turns:** 1
- **Tool calls:** 37
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a3e0967fbcc983b14.jsonl`
- **Structured JSON:** [`0b7a2477d274e63cb253.json`](../../sessions/0b/0b7a2477d274e63cb253.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

84 recorded events

### User

_source line 1 · 2026-05-10T08:49:10.727Z_

You are helping revise a robotics research proposal. I need you to do targeted web research to address specific reviewer concerns. Please execute ALL of the following searches and fetch operations, reporting findings in detail.

## Research Tasks

### Task 1: RoboTwin 2.0-Plus Evaluation Code Availability
1. Search for "RoboTwin 2.0-Plus evaluation code github" and "RoboTwin 2.0 Plus benchmark 2603.22078"
2. Fetch https://github.com/RoboTwin-Platform/RoboTwin and check what evaluation code/scripts exist, especially for camera viewpoint perturbation
3. Search for "arXiv 2603.22078 RoboTwin 2.0-Plus camera perturbation code release" 
4. Try to fetch https://arxiv.org/abs/2603.22078 to check if evaluation code is mentioned in the paper
5. Search for "Zhanguang Zhang Huawei RoboTwin 2.0-Plus code" to see if authors have released evaluation scripts separately
6. Check if there are any GitHub repos linked from the paper

### Task 2: LIBERO-Plus Evaluation Infrastructure
1. Search for "LIBERO-Plus benchmark github OpenMOSS 2510.13626"
2. Fetch https://github.com/OpenMOSS/LIBERO-Plus or similar - check if this is publicly available with full evaluation scripts
3. Verify camera viewpoint perturbation specifics for LIBERO-Plus
4. Check if Motus baseline scores are available on LIBERO-Plus

### Task 3: Being-H0.7 Camera Score Details
1. Fetch https://arxiv.org/abs/2605.00078 to read the abstract and results section
2. Specifically look for: (a) whether camera-specific breakdown scores are published for LIBERO-Plus, (b) what "resilience against shifted viewpoints" claim is based on, (c) exact aggregate scores on LIBERO-Plus
3. Search for "Being-H0.7 LIBERO-Plus camera viewpoint score"

### Task 4: OA-WAM Camera Score Verification
1. Fetch https://arxiv.org/abs/2605.06481 to confirm the 80.5% camera score on LIBERO-Plus
2. Verify Table 2 numbers and whether this is indeed the SOTA for camera-specific axis

### Task 5: Latest Related Work Check
1. Search for papers in May 2026 on "viewpoint invariant robot manipulation world model"
2. Search for "VQ world model robotic manipulation camera robust 2026"
3. Check if any new work addresses the exact same gap we're targeting

Please report ALL findings in detail, especially:
- Is RoboTwin 2.0-Plus evaluation code publicly available? If not, what would be needed to reproduce it?
- Is LIBERO-Plus publicly available with full evaluation scripts?
- Does Being-H0.7 report camera-specific LIBERO-Plus scores or only aggregate?
- Is OA-WAM 80.5% confirmed as SOTA for camera axis on LIBERO-Plus?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "6774ed9c-ed76-4b65-a975-0094d919910c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T08:49:10.732Z_

```json
{
  "parentUuid": "6774ed9c-ed76-4b65-a975-0094d919910c",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
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
  "uuid": "e8ce6368-df61-4fea-896b-c62a9b4ec0d0",
  "timestamp": "2026-05-10T08:49:10.732Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-10T08:49:12.558Z_

I'll execute all these research tasks systematically. Let me start all the searches and fetches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8ce6368-df61-4fea-896b-c62a9b4ec0d0",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbkkyYNgKoSD9okZ9FP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07556ca9-abb7-4453-8b5e-d42815467c4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DX49JdkS7U6aDjU78CYhd4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9382,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9382,
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

_source line 4 · 2026-05-10T08:49:13.008Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012F2pk1QFhGFF8zngHfa6rg`</summary>

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
  "parentUuid": "07556ca9-abb7-4453-8b5e-d42815467c4b",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbkkyYNgKoSD9okZ9FP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6ea8bf16-9e83-4a08-9d6f-d1279ebf95aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DX49JdkS7U6aDjU78CYhd4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9382,
      "cache_read_input_tokens": 0,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9382
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 9382,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9382,
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

_source line 5 · 2026-05-10T08:49:13.023Z_

<details><summary>↩ Tool result · `toolu_012F2pk1QFhGFF8zngHfa6rg`</summary>

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
  "parentUuid": "6ea8bf16-9e83-4a08-9d6f-d1279ebf95aa",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "9a95276d-dd38-46e6-935d-18a154111a68",
  "sourceToolAssistantUUID": "6ea8bf16-9e83-4a08-9d6f-d1279ebf95aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-10T08:49:14.715Z_

Now let me execute all the searches and fetches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a95276d-dd38-46e6-935d-18a154111a68",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbkwEw6dFbog7dvVpLK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "63375c1f-002d-410b-a1cc-871df6d32522",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Gu5h4Xjffn16PWw1umXTkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 7 · 2026-05-10T08:49:15.144Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ULWxr3WT9xbWG5NsW3Bq4J`</summary>

```json
{
  "query": "RoboTwin 2.0-Plus evaluation code github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63375c1f-002d-410b-a1cc-871df6d32522",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbkwEw6dFbog7dvVpLK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2eb06fad-6105-4a18-aace-4bb383463a10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Gu5h4Xjffn16PWw1umXTkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 8 · 2026-05-10T08:49:15.952Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WVmg1QiqFUt8kwPfE3oRXe`</summary>

```json
{
  "query": "RoboTwin 2.0 Plus benchmark 2603.22078"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2eb06fad-6105-4a18-aace-4bb383463a10",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbkwEw6dFbog7dvVpLK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dedcd49-1dc2-4d81-806e-c6f736753287",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Gu5h4Xjffn16PWw1umXTkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 9 · 2026-05-10T08:49:16.354Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0161N53W26DfPgNeeF1mWAVE`</summary>

```json
{
  "query": "LIBERO-Plus benchmark github OpenMOSS 2510.13626"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dedcd49-1dc2-4d81-806e-c6f736753287",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbkwEw6dFbog7dvVpLK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05db56ba-11b6-4edf-bf98-4dd6b8d8def9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Gu5h4Xjffn16PWw1umXTkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1910,
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

_source line 10 · 2026-05-10T08:49:16.802Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J17wE1EyC18zS3HdSeTim5`</summary>

```json
{
  "query": "Being-H0.7 LIBERO-Plus camera viewpoint score"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05db56ba-11b6-4edf-bf98-4dd6b8d8def9",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbkwEw6dFbog7dvVpLK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34a7febc-85b8-44a4-baae-4843e6cb81eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Gu5h4Xjffn16PWw1umXTkV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1910,
      "cache_read_input_tokens": 9382,
      "output_tokens": 233,
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
          "output_tokens": 233,
          "cache_read_input_tokens": 9382,
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

_source line 11 · 2026-05-10T08:49:21.197Z_

<details><summary>↩ Tool result · `toolu_01ULWxr3WT9xbWG5NsW3Bq4J`</summary>

```text
Web search results for query: "RoboTwin 2.0-Plus evaluation code github"

Links: [{"title":"RoboTwin 2.0","url":"https://robotwin-platform.github.io/"},{"title":"GitHub - RoboTwin-Platform/RoboTwin: RoboTwin 2.0 Offical Repo · GitHub","url":"https://github.com/RoboTwin-Platform/RoboTwin"},{"title":"X-VLA/evaluation/robotwin-2.0/README.md at main · 2toinf/X-VLA","url":"https://github.com/2toinf/X-VLA/blob/main/evaluation/robotwin-2.0/README.md"},{"title":"GitHub - thu-ml/vidar-robotwin: robotwin evaluation code for vidar. · GitHub","url":"https://github.com/thu-ml/vidar-robotwin"},{"title":"RoboTwin/README.md at main · TianxingChen/RoboTwin","url":"https://github.com/TianxingChen/RoboTwin/blob/main/README.md"},{"title":"starVLA/examples/Robotwin/README.md at starVLA · starVLA/starVLA","url":"https://github.com/starVLA/starVLA/blob/starVLA/examples/Robotwin/README.md"},{"title":"Pi0 - RoboTwin 2.0 Offical Document","url":"https://robotwin-platform.github.io/doc/usage/Pi0.html"},{"title":"RoboTwin 2.0 - RoboTwin 2.0 Offical Document","url":"https://robotwin-platform.github.io/doc/"},{"title":"GitHub - TianxingChen/RoboTwin · GitHub","url":"https://github.com/TianxingChen/RoboTwin"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong","url":"https://robogen-iros.github.io/accepted/9_RoboTwin_2_0_A_Scalable_Data.pdf"}]

Based on the search results, I found information about RoboTwin 2.0 evaluation code on GitHub:

## Main Repository

The official RoboTwin 2.0 repository is located at GitHub RoboTwin-Platform/RoboTwin. The older TianxingChen/RoboTwin repository has been migrated to RoboTwin-Platform/RoboTwin.

## Evaluation Code Examples

Several projects include evaluation code for RoboTwin 2.0:

1. **X-VLA Project**: Evaluation instructions are provided in the X-VLA repository, with instructions to follow official RoboTwin-2.0 evaluation at https://robotwin-platform.github.io/doc/usage/index.html, and configuration of custom evaluation in eval_robotwin.sh.

2. **VIDAR Project**: The thu-ml/vidar-robotwin repository provides a unified evaluation script based on torch.distributed (DDP), designed to simplify multi-GPU/multi-task evaluation workflow in Client-Server mode.

3. **StarVLA Project**: StarVLA provides instructions for reproducing experimental results with RoboTwin2.0, with the evaluation process consisting of setting up the robotwin environment and running evaluation by launching services.

## Official Documentation

The official documentation for RoboTwin 2.0 includes installation and usage instructions for various RoboTwin functionalities, available at robotwin-platform.github.io.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2eb06fad-6105-4a18-aace-4bb383463a10",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "ffacdfa3-7f5c-4f79-9e8f-5137521b1217",
  "sourceToolAssistantUUID": "2eb06fad-6105-4a18-aace-4bb383463a10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T08:49:21.846Z_

<details><summary>↩ Tool result · `toolu_01WVmg1QiqFUt8kwPfE3oRXe`</summary>

```text
Web search results for query: "RoboTwin 2.0 Plus benchmark 2603.22078"

Links: [{"title":"RoboTwin 2.0","url":"https://robotwin-platform.github.io/"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078"},{"title":"[2603.22078] Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/abs/2603.22078"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=vAPIIscwc7"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong","url":"https://robogen-iros.github.io/accepted/9_RoboTwin_2_0_A_Scalable_Data.pdf"},{"title":"[2506.18088] RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://arxiv.org/abs/2506.18088"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://arxiv.org/html/2506.18088v2"},{"title":"Paper page - RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://huggingface.co/papers/2506.18088"},{"title":"RoboTwin 2.0: Scalable Synthetic Data Generation and Benchmark Design for Dual-Arm Manipulation Robots | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media","url":"https://ai-scholar.tech/en/articles/llm-paper/robotwin-2.0"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250618088C/abstract"}]

Based on the search results, I found information about both RoboTwin 2.0 and the paper with the arXiv ID 2603.22078:

## RoboTwin 2.0

RoboTwin 2.0 is a scalable framework for automated, large-scale generation of diverse and realistic data, together with unified evaluation protocols for dual-arm manipulation. At its core is RoboTwin-OD, an object library of 731 instances across 147 categories with semantic and manipulation-relevant annotations.

The framework leverages multimodal language models (MLLMs) and simulation-in-the-loop refinement to automatically generate task-level execution code. To improve sim-to-real transfer, RoboTwin 2.0 applies structured domain randomization along five axes: clutter, lighting, background, tabletop height, and language.

## RoboTwin 2.0-Plus Benchmark

The arXiv paper 2603.22078 is titled "Do World Action Models Generalize Better than VLAs? A Robustness Study." This paper evaluates robustness using RoboTwin 2.0-Plus, an in-house benchmark that follows a similar perturbation protocol in the two-arm Aloha-Agilex setup of RoboTwin 2.0.

The results show that world action models (WAMs) achieve strong robustness, with LingBot-VA reaching 74.2% success rate on RoboTwin 2.0-Plus and Cosmos-Policy achieving 82.2% on LIBERO-Plus.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dedcd49-1dc2-4d81-806e-c6f736753287",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "dca14d6f-06d9-4aab-ae82-aa56c566e61c",
  "sourceToolAssistantUUID": "8dedcd49-1dc2-4d81-806e-c6f736753287",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T08:49:22.128Z_

<details><summary>↩ Tool result · `toolu_0161N53W26DfPgNeeF1mWAVE`</summary>

```text
Web search results for query: "LIBERO-Plus benchmark github OpenMOSS 2510.13626"

Links: [{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-plus/index.html at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/index.html"},{"title":"GitHub - OpenMOSS/VLABench: Official repo of VLABench, a large scale benchmark designed for fairly evaluating VLA, Embodied Agent, and VLMs. · GitHub","url":"https://github.com/OpenMOSS/VLABench"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | Takara TLDR","url":"https://tldr.takara.ai/p/2510.13626"},{"title":"LIBERO – LIBERO","url":"https://libero-project.github.io/main.html"}]

Based on the search results, I found relevant information about LIBERO-Plus:

**Overview:**
LIBERO-plus is a generalized benchmark for in-depth robustness analysis of vision-language-action models. The work is documented in the research paper with arXiv identifier 2510.13626.

**Research Focus:**
Visual-Language-Action (VLA) models report impressive success rates on robotic manipulation benchmarks, yet these results may mask fundamental weaknesses in robustness. The researchers perform a systematic vulnerability analysis by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

**Key Findings:**
Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. Surprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

**Repository:**
The official GitHub repository is available at: https://github.com/sylvestf/LIBERO-plus

**Paper:**
The paper is titled "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models" and was published in arXiv as preprint arXiv:2510.13626 in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05db56ba-11b6-4edf-bf98-4dd6b8d8def9",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "45e1961c-3828-4d03-a559-9798046de4e2",
  "sourceToolAssistantUUID": "05db56ba-11b6-4edf-bf98-4dd6b8d8def9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T08:49:23.070Z_

<details><summary>↩ Tool result · `toolu_01J17wE1EyC18zS3HdSeTim5`</summary>

```text
Web search results for query: "Being-H0.7 LIBERO-Plus camera viewpoint score"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"How brittle are the VLA models in robotics | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"Updated: Apple iPhone 7 Plus camera review - DXOMARK","url":"https://www.dxomark.com/apple-iphone-7-plus-camera-review-tested-new-dxomark-mobile-protocol/"},{"title":"Panasonic Lumix GH7 review: a high-performance hybrid | TechRadar","url":"https://www.techradar.com/cameras/mirrorless-cameras/panasonic-lumix-gh7-review"}]

Based on the search results, I found information about LIBERO-Plus and camera viewpoint evaluation, though I could not find a specific metric called "Being-H0.7" in the results.

Camera Viewpoints perturbations involve changing the viewpoint/pose and field-of-view of the third-person camera in the LIBERO-Plus benchmark. This dimension tests the model's view-free representation and generalization ability by changing camera viewpoints, with perturbations implemented by modifying camera position on a sphere centered at the scene, altering azimuth and elevation within 15°–75° cones.

In terms of model performance under camera viewpoint changes, the research reveals significant vulnerabilities. Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

However, I was unable to find a specific score or metric called "Being-H0.7" in the LIBERO-Plus benchmark documentation or results. The results discuss general model performance degradation under camera viewpoint changes, but don't reference this particular identifier. If you have more context about what "Being-H0.7" refers to, I'd be happy to search for more specific information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34a7febc-85b8-44a4-baae-4843e6cb81eb",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "6bdd79ac-6d28-4c0c-a717-8f25ec99a8f3",
  "sourceToolAssistantUUID": "34a7febc-85b8-44a4-baae-4843e6cb81eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T08:49:25.146Z_

Good initial results. Now let me fetch the key pages in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bdd79ac-6d28-4c0c-a717-8f25ec99a8f3",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbmfmXuAnUULB8S9bn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a5f3b58-bfc4-493b-a5a9-2895b2d7d73e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BtYrutun8uTmBak1bYBC4k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3922,
      "cache_read_input_tokens": 11292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3922,
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

_source line 16 · 2026-05-10T08:49:26.683Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015fPJ622ePNtd9krQuAzQJb`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.22078",
  "prompt": "Extract: (1) full title, (2) abstract, (3) any mention of code/evaluation code release, (4) RoboTwin 2.0-Plus description especially camera perturbation, (5) any GitHub links, (6) LIBERO-Plus results including camera-specific scores, (7) WAM vs VLA comparison results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a5f3b58-bfc4-493b-a5a9-2895b2d7d73e",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbmfmXuAnUULB8S9bn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94d700aa-f3ad-4635-8709-b38a522fb0c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BtYrutun8uTmBak1bYBC4k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3922,
      "cache_read_input_tokens": 11292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3922,
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

_source line 17 · 2026-05-10T08:49:28.209Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Mw1XnaA7HRrvTrVeWf1ppR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.00078",
  "prompt": "Extract: (1) full title and authors, (2) abstract, (3) any LIBERO-Plus scores especially camera-specific breakdowns, (4) any claims about resilience against shifted viewpoints, (5) exact aggregate scores on LIBERO-Plus, (6) any comparison to other models, (7) camera perturbation results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94d700aa-f3ad-4635-8709-b38a522fb0c5",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbmfmXuAnUULB8S9bn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3148b3f0-88e8-44f9-aa4f-8bb5e8fc8196",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BtYrutun8uTmBak1bYBC4k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3922,
      "cache_read_input_tokens": 11292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3922,
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

_source line 18 · 2026-05-10T08:49:29.776Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0139htPvFmVZztikHrRVdubF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.06481",
  "prompt": "Extract: (1) full title and authors, (2) abstract, (3) Table 2 content especially LIBERO-Plus camera scores, (4) the 80.5% camera score claim on LIBERO-Plus, (5) SOTA claims for camera-specific axis, (6) comparison table numbers for camera viewpoint robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3148b3f0-88e8-44f9-aa4f-8bb5e8fc8196",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbmfmXuAnUULB8S9bn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c43aedf-431b-49f5-bbc0-c35fb3adf8a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BtYrutun8uTmBak1bYBC4k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3922,
      "cache_read_input_tokens": 11292,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3922,
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

_source line 19 · 2026-05-10T08:49:31.104Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KQjcwkmMFcVdDkrUARpwGk`</summary>

```json
{
  "url": "https://github.com/RoboTwin-Platform/RoboTwin",
  "prompt": "Extract: (1) README contents, (2) any evaluation scripts or code for camera viewpoint perturbation, (3) links to evaluation documentation, (4) whether RoboTwin 2.0-Plus evaluation code is included, (5) overall structure of the repository"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c43aedf-431b-49f5-bbc0-c35fb3adf8a2",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbmfmXuAnUULB8S9bn6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5cb77baa-3183-4397-9d04-71421617e1d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BtYrutun8uTmBak1bYBC4k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3922,
      "cache_read_input_tokens": 11292,
      "output_tokens": 586,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3922
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 586,
          "cache_read_input_tokens": 11292,
          "cache_creation_input_tokens": 3922,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3922,
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

_source line 20 · 2026-05-10T08:49:31.902Z_

<details><summary>↩ Tool result · `toolu_015fPJ622ePNtd9krQuAzQJb`</summary>

```text
# Research Paper Summary

## (1) Full Title
"Do World Action Models Generalize Better than VLAs? A Robustness Study"

## (2) Abstract
The paper compares Vision-Language-Action (VLA) models with World Action Models (WAMs) for robot planning. It notes that VLAs show "limited generalization to unseen scenarios and vulnerability to diverse contextual perturbations." WAMs leverage video pretraining to predict future states. The study evaluates both approaches on benchmarks with visual and language perturbations, finding that WAMs demonstrate strong robustness, though some VLAs achieve comparable performance with extensive diverse training.

## (3) Code/Evaluation Code Release
No mention of code release or GitHub repositories is provided in the document.

## (4) RoboTwin 2.0-Plus Description
The document references this benchmark but does not include specific details about camera perturbation testing methodology.

## (5) GitHub Links
None found in the provided content.

## (6) LIBERO-Plus Results
Cosmos-Policy achieved "82.2% on LIBERO-Plus." Camera-specific breakdown scores are not detailed in this excerpt.

## (7) WAM vs VLA Comparison Results
LingBot-VA (WAM) reached 74.2% on RoboTwin 2.0-Plus; Cosmos-Policy (WAM) achieved 82.2% on LIBERO-Plus. The abstract notes VLAs like π₀.₅ can achieve comparable robustness but "typically require extensive training."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94d700aa-f3ad-4635-8709-b38a522fb0c5",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "c9d101d8-b6af-43a4-a76f-ec285109e18e",
  "sourceToolAssistantUUID": "94d700aa-f3ad-4635-8709-b38a522fb0c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T08:49:33.491Z_

<details><summary>↩ Tool result · `toolu_01Mw1XnaA7HRrvTrVeWf1ppR`</summary>

```text
# Being-H0.7: Extraction Summary

## (1) Full Title and Authors
**Title:** "Being-H0.7: A Latent World-Action Model from Egocentric Videos"

**Authors:** Hao Luo, Wanpeng Zhang, Yicheng Feng, Sipeng Zheng, Haiweng Xu, Chaoyi Xu, Ziheng Xi, Yuhui Fu, Zongqing Lu

## (2) Abstract
The model introduces a latent world-action approach that "brings future-aware reasoning into VLA-style policies without generating future frames." It uses "learnable latent queries" with dual-branch training, where a prior branch operates at inference while a "training-only posterior branch" uses future embeddings to guide learning. The paper claims achievement of "state-of-the-art or comparable performance" across benchmarks.

## (3) LIBERO-Plus Scores
No LIBERO-Plus scores or camera-specific breakdowns are provided in the abstract or metadata.

## (4) Viewpoint Resilience Claims
No explicit claims regarding resilience against shifted viewpoints are mentioned in the available content.

## (5) Aggregate Scores on LIBERO-Plus
Not reported in the provided webpage content.

## (6) Model Comparisons
The abstract indicates comparisons across "six simulation benchmarks and diverse real-world tasks" but specific comparison details are not included in this excerpt.

## (7) Camera Perturbation Results
No camera perturbation results are documented in the available material.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3148b3f0-88e8-44f9-aa4f-8bb5e8fc8196",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "7223cfec-653d-4a7f-8ee4-768d9bfc0837",
  "sourceToolAssistantUUID": "3148b3f0-88e8-44f9-aa4f-8bb5e8fc8196",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T08:49:35.896Z_

<details><summary>↩ Tool result · `toolu_0139htPvFmVZztikHrRVdubF`</summary>

```text
# OA-WAM Paper Analysis

## (1) Full Title and Authors

**Title:** "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation"

**Authors:** Yushan Liu, Peibo Sun, Shoujie Li, Yifan Xie, Lingfeng Zhang, Xintao Chao, Shiyuan Dong, Fang Chen, Xiao-Ping Zhang, Wenbo Ding

## (2) Abstract

The paper introduces an object-addressable framework that decomposes visual scenes into persistent object slots. It "predicts next-frame slot states, while a flow-matching action head decodes a 16-step continuous action chunk in the same forward pass." The approach separates object identity from current state without requiring additional tokens.

## (3) & (4) Table 2 and Camera Score Claims

**Status:** The provided webpage content does not include Table 2 or specific numerical performance data for LIBERO-Plus camera scores. The abstract mentions achieving "state-of-the-art performance on the most relevant LIBERO-Plus geometric axes" and matching baselines at 97.8% on LIBERO and 79.3% on SimplerEnv, but the specific 80.5% camera score claim you reference is not visible in this excerpt.

## (5) SOTA Claims for Camera-Specific Axis

The abstract states the method "reaches state-of-the-art performance on the most relevant LIBERO-Plus geometric axes," though detailed camera-axis breakdown tables are not shown in this content.

## (6) Comparison Table Numbers

Detailed comparative tables for camera viewpoint robustness are not included in the provided webpage excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c43aedf-431b-49f5-bbc0-c35fb3adf8a2",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "12490228-7a1b-48c6-8c44-9fd263824cac",
  "sourceToolAssistantUUID": "4c43aedf-431b-49f5-bbc0-c35fb3adf8a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T08:49:38.602Z_

<details><summary>↩ Tool result · `toolu_01KQjcwkmMFcVdDkrUARpwGk`</summary>

````text
# RoboTwin 2.0 Repository Analysis

## (1) README Contents

The README presents RoboTwin 2.0 as "A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation." Key sections include:

- **Overview**: Links to webpage, documentation, papers, community, and leaderboard
- **Updates**: Recent developments through March 2026, including RMBench release and StarVLA integration
- **Installation**: References external documentation (20-minute setup)
- **Tasks**: 50 different manipulation tasks available
- **Data Collection**: Over 100,000 pre-collected trajectories; users encouraged to collect custom data
- **Policy Baselines**: Support for DP, ACT, DP3, RDT, PI0, OpenVLA-oft, and community contributions
- **Leaderboard**: Experimental benchmarking across five research dimensions

## (2) Camera Viewpoint Perturbation Code

**Not found in provided content.** While domain randomization is mentioned with an associated image, specific evaluation scripts for camera viewpoint perturbation are not included in this repository section.

## (3) Evaluation Documentation Links

- Main documentation: `robotwin-platform.github.io/doc/`
- Tasks documentation: `robotwin-platform.github.io/doc/tasks/index.html`
- Leaderboard: `robotwin-platform.github.io/leaderboard`
- Policy deployment guidance available

## (4) RoboTwin 2.0-Plus Evaluation Code

**Not mentioned.** Only RoboTwin 2.0 materials are referenced.

## (5) Repository Structure

```
RoboTwin/
├── assets/          (images, demonstrations)
├── code_gen/        (code generation)
├── data/            (datasets)
├── description/     (task descriptions)
├── envs/            (environment configs)
├── policy/          (baseline policies)
├── script/          (utility scripts)
├── task_config/     (task configurations)
├── collect_data.sh  (data collection script)
└── README.md
```

**Language**: 97.7% Python; 1.3% Shell; 1.0% other
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cb77baa-3183-4397-9d04-71421617e1d3",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "8c4eecd0-1b04-40f4-a1a7-665aa21c3b56",
  "sourceToolAssistantUUID": "5cb77baa-3183-4397-9d04-71421617e1d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T08:49:40.856Z_

Let me now fetch the full HTML papers and GitHub repos for deeper detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c4eecd0-1b04-40f4-a1a7-665aa21c3b56",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbnpGYASj3Xu6GbwpKX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f251e013-33a9-4076-b3eb-ae7013702b9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0163Lg15E31rfSo1s31NncBR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2425,
      "cache_read_input_tokens": 15214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2425,
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

_source line 25 · 2026-05-10T08:49:43.353Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LafB67kHf5KxacKwy38Tdc`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.22078",
  "prompt": "Extract: (1) All mentions of RoboTwin 2.0-Plus including its definition, perturbation axes, and camera perturbation specifics, (2) all result tables with numerical scores, (3) whether evaluation code is mentioned as being released, (4) LIBERO-Plus camera-specific scores, (5) any GitHub or code links, (6) how exactly camera perturbation is defined in both benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f251e013-33a9-4076-b3eb-ae7013702b9f",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbnpGYASj3Xu6GbwpKX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b7994e6-1ce7-41cd-b5a9-f16b7fb8294a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0163Lg15E31rfSo1s31NncBR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2425,
      "cache_read_input_tokens": 15214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2425,
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

_source line 26 · 2026-05-10T08:49:45.135Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013QeySCXj1effgFy7JAup9K`</summary>

```json
{
  "url": "https://github.com/sylvestf/LIBERO-plus",
  "prompt": "Extract: (1) Is the full evaluation code publicly available?, (2) What scripts/tools exist for camera viewpoint perturbation?, (3) What is the camera perturbation methodology (angles, distances, etc)?, (4) Are baseline scores like Motus included in the repository?, (5) What does the README say about installation/usage?, (6) Repository structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b7994e6-1ce7-41cd-b5a9-f16b7fb8294a",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbnpGYASj3Xu6GbwpKX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "552f7fa9-1f2b-4baf-96ac-73a06af3679a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0163Lg15E31rfSo1s31NncBR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2425,
      "cache_read_input_tokens": 15214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2425,
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

_source line 27 · 2026-05-10T08:49:45.584Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EcLngMxoxLtBCtCu4vNZU3`</summary>

```json
{
  "query": "arXiv 2603.22078 RoboTwin 2.0-Plus camera perturbation code release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "552f7fa9-1f2b-4baf-96ac-73a06af3679a",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbnpGYASj3Xu6GbwpKX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "069bb735-c9d2-4f9f-ac0b-847cf5f1dd8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0163Lg15E31rfSo1s31NncBR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2425,
      "cache_read_input_tokens": 15214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2425,
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

_source line 28 · 2026-05-10T08:49:45.975Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017GiwwofENbDCgjgghKy9Gg`</summary>

```json
{
  "query": "Zhanguang Zhang Huawei RoboTwin 2.0-Plus code evaluation scripts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "069bb735-c9d2-4f9f-ac0b-847cf5f1dd8e",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbnpGYASj3Xu6GbwpKX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40f583cb-2513-44e3-980b-f1c07cfaea1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0163Lg15E31rfSo1s31NncBR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2425,
      "cache_read_input_tokens": 15214,
      "output_tokens": 458,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2425
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 458,
          "cache_read_input_tokens": 15214,
          "cache_creation_input_tokens": 2425,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2425,
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

_source line 29 · 2026-05-10T08:49:47.971Z_

<details><summary>↩ Tool result · `toolu_01LafB67kHf5KxacKwy38Tdc`</summary>

```text
# Research Paper Extraction: RoboTwin 2.0-Plus and Evaluation Details

## RoboTwin 2.0-Plus Definition & Perturbations

RoboTwin 2.0-Plus is described as "an in-house benchmark that follows a similar perturbation protocol in the two-arm Aloha-Agilex setup of RoboTwin 2.0." The document mentions "seven types of perturbations" are used in LIBERO-Plus, with RoboTwin 2.0-Plus following "a similar perturbation protocol," but the specific seven perturbation types for RoboTwin 2.0-Plus are not explicitly detailed in the provided content.

## Camera Perturbation Details

**Camera perturbation specifics are not explicitly defined** in the visible portions of this paper. While perturbations are referenced, the exact methodology for camera-specific perturbations in either benchmark is not disclosed in the extracted content.

## Result Tables with Numerical Scores

No complete result tables with numerical scores appear in the provided content. Performance metrics mentioned include:
- LingBot-VA: 74.2% success on RoboTwin 2.0-Plus
- Cosmos-Policy: 82.2% on LIBERO-Plus

However, comprehensive tables comparing all models are referenced but not fully reproduced in the excerpt.

## Evaluation Code Release

**No mention of released evaluation code** is present in the provided text.

## GitHub or Code Links

**No GitHub links or code repositories are provided** in this content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b7994e6-1ce7-41cd-b5a9-f16b7fb8294a",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "a06904bb-7864-40a5-9753-c1070a5cf447",
  "sourceToolAssistantUUID": "2b7994e6-1ce7-41cd-b5a9-f16b7fb8294a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T08:49:51.110Z_

<details><summary>↩ Tool result · `toolu_013QeySCXj1effgFy7JAup9K`</summary>

````text
# LIBERO-plus Repository Analysis

## (1) Full Evaluation Code Availability
The webpage does not explicitly state whether complete evaluation code is publicly available. It mentions evaluation methods are "almost identical to `LIBERO`" with configuration adjustments, but doesn't confirm full code release.

## (2) Camera Viewpoint Perturbation Scripts
No specific scripts or tools for camera viewpoint perturbations are mentioned in the provided content. The benchmark includes this dimension but implementation details aren't documented here.

## (3) Camera Perturbation Methodology
The documentation mentions "Position, orientation, and field-of-view changes" as part of camera perturbations, but specific angles, distances, or technical parameters are not detailed in this excerpt.

## (4) Baseline Scores
The leaderboard includes multiple baseline models (OpenVLA, π₀, NORA, WorldVLA, UniVLA, RIPT-VLA) with performance metrics across perturbation categories. However, "Motus" is not mentioned.

## (5) Installation/Usage Instructions
The README states: "Simply replace the originally installed LIBERO repository with our repository without modifying your code." Installation requires downloading assets from Hugging Face and extracting them to the appropriate directory structure. The evaluation setup requires adjusting "num_trials_per_task from 50 to 1."

## (6) Repository Structure
```
LIBERO-plus/
├── benchmark_scripts/
├── libero/
├── notebooks/
├── scripts/
├── static/
├── templates/
└── Supporting files (README.md, requirements.txt, setup.py)
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "552f7fa9-1f2b-4baf-96ac-73a06af3679a",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "d283b662-204b-4aad-9216-8a395cf24d9d",
  "sourceToolAssistantUUID": "552f7fa9-1f2b-4baf-96ac-73a06af3679a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T08:49:52.370Z_

<details><summary>↩ Tool result · `toolu_017GiwwofENbDCgjgghKy9Gg`</summary>

```text
Web search results for query: "Zhanguang Zhang Huawei RoboTwin 2.0-Plus code evaluation scripts"

Links: [{"title":"RoboTwin 2.0","url":"https://robotwin-platform.github.io/"},{"title":"X-VLA/evaluation/robotwin-2.0/README.md at main · 2toinf/X-VLA","url":"https://github.com/2toinf/X-VLA/blob/main/evaluation/robotwin-2.0/README.md"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://arxiv.org/html/2506.18088v2"},{"title":"GitHub - RoboTwin-Platform/RoboTwin: RoboTwin 2.0 Offical Repo · GitHub","url":"https://github.com/robotwin-Platform/RoboTwin"},{"title":"GitHub - thu-ml/vidar-robotwin: robotwin evaluation code for vidar. · GitHub","url":"https://github.com/thu-ml/vidar-robotwin"},{"title":"GitHub - Robbyant/lingbot-va: [RSS 2026] Causal video-action world model for generalist robot control · GitHub","url":"https://github.com/robbyant/lingbot-va"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong","url":"https://robogen-iros.github.io/accepted/9_RoboTwin_2_0_A_Scalable_Data.pdf"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=vAPIIscwc7"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250618088C/abstract"},{"title":"RoboTwin Evaluation | StarVLA","url":"https://starvla.github.io/docs/benchmarks/robotwin/"}]

Based on the search results, I found information about RoboTwin 2.0 and its code evaluation capabilities, though the specific mention of "Zhanguang Zhang" and "RoboTwin 2.0-Plus" did not appear in the results. Here's what I found:

## RoboTwin 2.0 Overview

RoboTwin 2.0 is a scalable framework for automated, large-scale generation of diverse and realistic data, together with unified evaluation protocols for dual-arm manipulation.

## Code Generation and Evaluation

The task code generation module employs MLLMs with simulation-in-the-loop feedback to synthesize executable plans from natural-language instructions, grounded in a large object asset library (RoboTwin-OD) and a predefined skill library.

Empirical evaluation shows a 10.9% gain in code generation success rate.

## Available Resources

The project releases the data generator, benchmark, dataset, and code to support scalable research in robust bimanual manipulation. The official resources are available at the GitHub repository (https://github.com/robotwin-Platform/RoboTwin) and documentation at https://robotwin-platform.github.io/.

The search results don't contain specific information about "Zhanguang Zhang" or a "RoboTwin 2.0-Plus" variant. If you're looking for more specific information about these, you may want to check the official RoboTwin GitHub repository or documentation directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40f583cb-2513-44e3-980b-f1c07cfaea1e",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "b2a3a44d-8508-4cd0-8cc6-a98d235d2e2c",
  "sourceToolAssistantUUID": "40f583cb-2513-44e3-980b-f1c07cfaea1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T08:49:52.458Z_

<details><summary>↩ Tool result · `toolu_01EcLngMxoxLtBCtCu4vNZU3`</summary>

```text
Web search results for query: "arXiv 2603.22078 RoboTwin 2.0-Plus camera perturbation code release"

Links: [{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"[2603.22078] Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/abs/2603.22078"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://arxiv.org/html/2506.18088v2"},{"title":"RoboTwin 2.0","url":"https://robotwin-platform.github.io/"},{"title":"(PDF) RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://www.researchgate.net/publication/392941279_RoboTwin_20_A_Scalable_Data_Generator_and_Benchmark_with_Strong_Domain_Randomization_for_Robust_Bimanual_Robotic_Manipulation"},{"title":"GitHub - RoboTwin-Platform/RoboTwin: RoboTwin 2.0 Offical Repo · GitHub","url":"https://github.com/robotwin-Platform/RoboTwin"},{"title":"GitHub - Robbyant/lingbot-va: [RSS 2026] Causal video-action world model for generalist robot control · GitHub","url":"https://github.com/robbyant/lingbot-va"},{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"GitHub - TianxingChen/RoboTwin · GitHub","url":"https://github.com/TianxingChen/RoboTwin"},{"title":"Paper page - RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://huggingface.co/papers/2506.18088"}]

Based on the search results, I found information about arXiv paper 2603.22078 and the RoboTwin 2.0-Plus benchmark:

## Overview

The paper conducts a comparative study of prominent state-of-the-art VLA policies and recently released WAMs, evaluating their performance on the LIBERO-Plus and RoboTwin 2.0-Plus benchmarks under various visual and language perturbations.

## Camera Perturbation and RoboTwin 2.0-Plus

RoboTwin 2.0-Plus is an in-house benchmark that follows a similar perturbation protocol in the two-arm Aloha-Agilex setup of RoboTwin 2.0. Camera perturbations alter the viewpoint pose of the third-person camera, along with other perturbation axes including Robot configuration, Language, Light, Background, Noise, and Layout.

## Code Release

While the search results indicate that this benchmark is designed to facilitate evaluation of WAMs and VLAs that provide open-source checkpoints trained on RoboTwin 2.0, the specific details about a code release for the camera perturbation functionality are not explicitly mentioned in the available search results. The results do reference the broader RoboTwin platform's GitHub repositories and indicate that code and benchmarks are available, but detailed information about a specific camera perturbation code release would require accessing the actual paper or supplementary materials directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "069bb735-c9d2-4f9f-ac0b-847cf5f1dd8e",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "b3f468de-6369-46b8-b60d-4f929ea40781",
  "sourceToolAssistantUUID": "069bb735-c9d2-4f9f-ac0b-847cf5f1dd8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-10T08:49:57.233Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014egSB2AxLVFggZ8eEDPFjH`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.22078v1",
  "prompt": "Extract ALL of the following: (1) complete table of results for LIBERO-Plus with per-axis scores (camera, background, layout, light, noise, language, robot state) for each model, (2) complete table of results for RoboTwin 2.0-Plus with per-axis scores for each model, (3) exact definition of camera perturbation for RoboTwin 2.0-Plus (how many degrees, what axes), (4) any code availability statement, (5) list of all models evaluated, (6) which institution/authors created RoboTwin 2.0-Plus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3f468de-6369-46b8-b60d-4f929ea40781",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatboqP36AqkXaxFKuKNC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d110a4b-eb65-483b-be1a-8098dc23d936",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KvScyojkonP3T3NEfYyHou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 971,
      "cache_creation_input_tokens": 2196,
      "cache_read_input_tokens": 17639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2196,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-10T08:49:59.651Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SUX8Ph5mkGfvfJWZSrbuhR`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.00078",
  "prompt": "Extract ALL of the following: (1) the full results tables, especially LIBERO-Plus scores broken down by axis (camera, background, layout, etc.), (2) the aggregate LIBERO-Plus score for Being-H0.7, (3) any camera-specific score for LIBERO-Plus, (4) claims about viewpoint robustness or camera robustness, (5) comparison against other models on LIBERO-Plus, (6) any mention of OA-WAM or other WAM models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d110a4b-eb65-483b-be1a-8098dc23d936",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatboqP36AqkXaxFKuKNC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "072a096f-4689-4124-9766-7ddddadbf391",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KvScyojkonP3T3NEfYyHou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 971,
      "cache_creation_input_tokens": 2196,
      "cache_read_input_tokens": 17639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2196,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-10T08:50:01.602Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PbSoFjZNMWGCA5GjoKvWqq`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06481v1",
  "prompt": "Extract ALL of the following: (1) all result tables especially Table 2 with LIBERO-Plus scores per axis, (2) the specific camera viewpoint score on LIBERO-Plus (the claimed 80.5%), (3) aggregate LIBERO-Plus performance, (4) SOTA comparison claims for camera axis, (5) what models are compared, (6) how LIBERO-Plus camera perturbation is defined, (7) any mention of RoboTwin 2.0-Plus scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "072a096f-4689-4124-9766-7ddddadbf391",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatboqP36AqkXaxFKuKNC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b72c17b-4ad1-47fe-95fe-0f1bf551bde8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KvScyojkonP3T3NEfYyHou",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 971,
      "cache_creation_input_tokens": 2196,
      "cache_read_input_tokens": 17639,
      "output_tokens": 630,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2196
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 971,
          "output_tokens": 630,
          "cache_read_input_tokens": 17639,
          "cache_creation_input_tokens": 2196,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2196,
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

_source line 36 · 2026-05-10T08:50:02.103Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HezcVwtjRugTzGj54V4ak8`</summary>

```json
{
  "query": "viewpoint invariant robot manipulation world model 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b72c17b-4ad1-47fe-95fe-0f1bf551bde8",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatboqP36AqkXaxFKuKNC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "884afa90-49fd-4346-9812-2ba054dfb98c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KvScyojkonP3T3NEfYyHou",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 971,
      "cache_creation_input_tokens": 2196,
      "cache_read_input_tokens": 17639,
      "output_tokens": 630,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2196
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 971,
          "output_tokens": 630,
          "cache_read_input_tokens": 17639,
          "cache_creation_input_tokens": 2196,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2196,
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

_source line 37 · 2026-05-10T08:50:04.777Z_

<details><summary>↩ Tool result · `toolu_014egSB2AxLVFggZ8eEDPFjH`</summary>

```text
# Extracted Information from Research Paper

## (1) LIBERO-Plus Complete Results Table

**Table 4** presents results with these columns: Original, Camera, Robot, Language, Light, Background, Noise, Layout, Total

Key models and scores (Total column):
- π0.5: 85.7%
- Cosmos-Policy: 82.2%
- ABot-M0: 80.5%
- GE-Act: 80.3%
- VLA-JEPA: 77.9%
- X-VLA: 71.4%

Per-axis breakdown available in Table 4 for all 14 evaluated models.

## (2) RoboTwin 2.0-Plus Complete Results Table

**Table 3** shows:
- LingBot-VA: 74.2% total (Original: 92.1%)
- MOTUS: 71.5% total (Original: 87.0%)
- π0.5: 58.6% total (Original: 78.4%)
- X-VLA: 53.1% total (Original: 65.6%)

Per-axis breakdown across Camera, Robot, Language, Light, Background, Noise, Layout provided.

## (3) Camera Perturbation Definition

The document states perturbations involve "altering the viewpoint pose of the third-person camera" but **does not specify exact degrees or axes** in the accessible sections.

## (4) Code Availability

**No code availability statement found** in the provided content.

## (5) All Evaluated Models

**LIBERO-Plus:** π0, π0-FAST, π0.5, OpenVLA-OFT-m, UniVLA, RIPT-VLA, X-VLA, HoloBrain0-GD, VLA-JEPA, ABot-M0, GE-Act, Cosmos-Policy

**RoboTwin 2.0-Plus:** π0.5, X-VLA, MOTUS, LingBot-VA

## (6) RoboTwin 2.0-Plus Creator

**Huawei Technologies** created this benchmark, as indicated by the author affiliations and acknowledgment that it follows "the perturbation protocol of LIBERO-Plus...with minor parameter adjustments."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d110a4b-eb65-483b-be1a-8098dc23d936",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "ac5a6278-ce07-4c13-a0c7-329805d09135",
  "sourceToolAssistantUUID": "8d110a4b-eb65-483b-be1a-8098dc23d936",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-10T08:50:04.798Z_

<details><summary>↩ Tool result · `toolu_01SUX8Ph5mkGfvfJWZSrbuhR`</summary>

```text
# Being-H0.7 LIBERO-Plus Results Extract

## LIBERO-Plus Aggregate Scores

**Being-H0.7 performance:**
- Zero-shot: 82.1%
- Fine-tuned on LIBERO-plus: 84.8%

## Full Results Table (Table 1)

The document presents comprehensive simulation benchmark results. For LIBERO-plus specifically:

| Model | LIBERO-plus | LIBERO-plus* |
|-------|-------------|--------------|
| Being-H0.7 | 82.1 | 84.8 |
| Being-H0.5 | 78.5 | 83.1 |

*Note: LIBERO-plus* indicates fine-tuning with LIBERO-plus dataset

## Key Claims About Robustness

The paper states: "When evaluating robustness under environmental perturbations on LIBERO-plus, Being-H0.7 secures a 82.1% zero-shot success rate, which further improves to 84.8% after fine-tuning on LIBERO-plus, highlighting its resilience against shifted viewpoints, novel textures, and sensor noise."

The document does not provide axis-by-axis breakdown (camera, background, layout, etc.) or camera-specific scores for LIBERO-plus.

## Related Model Comparisons

Notable comparisons include JEPA-VLA (96.4% LIBERO, 25.6% LIBERO-plus) and VLA-JEPA (96.1% LIBERO, 79.5% LIBERO-plus).

## Mentions of Other Models

No OA-WAM or additional WAM model comparisons appear in the LIBERO-plus results section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "072a096f-4689-4124-9766-7ddddadbf391",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "d3a3823e-ac42-4ae2-9f85-1015f95a8b95",
  "sourceToolAssistantUUID": "072a096f-4689-4124-9766-7ddddadbf391",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-10T08:50:09.442Z_

<details><summary>↩ Tool result · `toolu_01PbSoFjZNMWGCA5GjoKvWqq`</summary>

```text
# OA-WAM LIBERO-Plus Results Extraction

## (1) Result Tables

**Table 2 - LIBERO-Plus Complete Scores (%):**

| Method | Camera | Robot Init | Layout | Geo Avg | Light | Background | Language | Sensor Noise | Overall Avg |
|--------|--------|-----------|--------|---------|-------|------------|----------|-------------|------------|
| OA-WAM | 80.5 | 89.6 | 82.8 | 84.3 | 96.5 | 95.9 | 85.3 | 75.6 | 83.9 |
| π₀.₅ | 75.4 | 77.5 | 85.7 | 79.5 | 96.9 | 94.6 | 85.6 | 89.7 | 85.7 |
| Cosmos-Policy | 75.8 | 63.3 | 82.2 | 73.8 | 96.5 | 88.9 | 81.7 | 92.7 | 82.2 |

## (2) Camera Viewpoint Score

"OA-WAM sets a new SOTA on the three geometric axes most aligned with our hypothesis...Camera 80.5 (+4.7 over Cosmos-Policy)"

## (3) Aggregate Performance

Across seven perturbation axes: **83.9%** for OA-WAM versus **85.7%** for π₀.₅

## (4) SOTA Claims on Camera Axis

"Camera 80.5 (+4.7+4.7% over Cosmos-Policy)" represents the primary geometric-axis improvement claim.

## (5) Compared Models

Eight primary baselines compared on swap-binding test; Table 2 includes OpenVLA-OFT, π₀, π₀.₅, ABot-M0, X-VLA, AVA-VLA, WorldVLA, VLA-JEPA, GE-Act, HoloBrain-0, and Cosmos-Policy.

## (6) Camera Perturbation Definition

The document states the benchmark "measures robustness across seven controlled perturbation axes" but provides no explicit mechanical definition of the camera axis manipulation itself.

## (7) RoboTwin 2.0-Plus Mention

**Not mentioned** anywhere in the provided document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b72c17b-4ad1-47fe-95fe-0f1bf551bde8",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "e9f4816e-3f1c-457b-a781-ca777f937fbd",
  "sourceToolAssistantUUID": "6b72c17b-4ad1-47fe-95fe-0f1bf551bde8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T08:50:10.929Z_

<details><summary>↩ Tool result · `toolu_01HezcVwtjRugTzGj54V4ak8`</summary>

```text
Web search results for query: "viewpoint invariant robot manipulation world model 2026 arxiv"

Links: [{"title":"A Step Toward World Models: A Survey on Robotic Manipulation","url":"https://arxiv.org/html/2511.02097v1"},{"title":"Learning View-invariant World Models for Visual Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=vJwjWyt4Ed"},{"title":"View-Invariant Policy Learning via Zero-Shot Novel View Synthesis","url":"https://arxiv.org/html/2409.03685v1"},{"title":"1 A Step Toward World Models: A Survey on Robotic Manipulation","url":"https://www.techrxiv.org/users/935947/articles/1356038/master/file/data/A%20Step%20Toward%20World%20Models2/A%20Step%20Toward%20World%20Models2.pdf?inline=true"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"Multi-View Masked World Models for Visual Robotic Manipulation","url":"https://proceedings.mlr.press/v202/seo23a/seo23a.pdf"},{"title":"Awesome-Robotics-Manipulation/contents/low-level_learning-based_action_modelling.md at main · BaiShuanghao/Awesome-Robotics-Manipulation","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation/blob/main/contents/low-level_learning-based_action_modelling.md"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"},{"title":"LEARNING VIEW-INVARIANT WORLD MODELS FOR ...","url":"https://openreview.net/pdf?id=vJwjWyt4Ed"}]

I found several relevant results for your query on viewpoint invariant robot manipulation world models. Here are the key findings:

## Main Results

ReViWo (Representation learning for View-invariant World model) leverages multi-view data to learn robust representations for control under viewpoint disturbance. ReViWo utilizes an autoencoder framework to reconstruct target images by an architecture that combines view-invariant representation (VIR) and view-dependent representation.

To train ReViWo, multi-view data is collected in simulators with known view labels, meanwhile, ReViWo is simultaneously trained on Open X-Embodiment datasets without view labels.

## Related Work

Additionally, View Synthesis Augmentation (VISTA) is a data-augmentation scheme that uses view synthesis models to understand the capabilities for learning viewpoint-invariant policies from single-viewpoint demonstration data.

Multi-View Masked World Models learn a world model on frozen masked autoencoder features to solve tasks from various robotic manipulation setups, including multi-view control, single-view control, and viewpoint-robust control in both simulation and real-world.

These papers represent current research efforts focused on addressing the challenge of making robot manipulation more robust to changes in viewpoint and camera perspective.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "884afa90-49fd-4346-9812-2ba054dfb98c",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "ecc216d5-5f46-427a-b7cc-1b09524d2ebb",
  "sourceToolAssistantUUID": "884afa90-49fd-4346-9812-2ba054dfb98c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-10T08:50:13.054Z_

Excellent — now let me run the remaining searches and fetch the deeper details I still need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecc216d5-5f46-427a-b7cc-1b09524d2ebb",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbqCM93TfFQDwp5R4PK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "025b8241-e9cd-45e5-a810-a827ee669aee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PCZdqxQb3vdQJ1fSFktpEc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4089,
      "cache_read_input_tokens": 19835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4089,
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

_source line 42 · 2026-05-10T08:50:13.449Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SsTVPuMRqKR5gmYjkVodkj`</summary>

```json
{
  "query": "VQ world model robotic manipulation camera robust 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "025b8241-e9cd-45e5-a810-a827ee669aee",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbqCM93TfFQDwp5R4PK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5eb6efe8-09f8-4125-adb4-92d34e22f2d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PCZdqxQb3vdQJ1fSFktpEc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4089,
      "cache_read_input_tokens": 19835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4089,
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

_source line 43 · 2026-05-10T08:50:13.856Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014rwkaTg7RgspEvxc8Lz2Um`</summary>

```json
{
  "query": "camera viewpoint robust robot policy world model arxiv May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5eb6efe8-09f8-4125-adb4-92d34e22f2d1",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbqCM93TfFQDwp5R4PK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f5d7a58-c2e9-4dc5-a475-da530711d5b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PCZdqxQb3vdQJ1fSFktpEc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4089,
      "cache_read_input_tokens": 19835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4089,
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

_source line 44 · 2026-05-10T08:50:16.120Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EjnnTuJbM1pTPVST6QbhhQ`</summary>

```json
{
  "url": "https://github.com/Robbyant/lingbot-va",
  "prompt": "Extract: (1) Does this repo contain RoboTwin 2.0-Plus evaluation code?, (2) Is there camera perturbation evaluation code?, (3) What scripts are included?, (4) Is there mention of Huawei or Zhanguang Zhang?, (5) What is the overall structure and contents?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f5d7a58-c2e9-4dc5-a475-da530711d5b8",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbqCM93TfFQDwp5R4PK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4eadb426-5885-4537-8fb0-b1c9c8bc71a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PCZdqxQb3vdQJ1fSFktpEc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4089,
      "cache_read_input_tokens": 19835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4089,
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

_source line 45 · 2026-05-10T08:50:17.152Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TXbT8WhWsAJWjowgRZBrDG`</summary>

```json
{
  "url": "https://openreview.net/forum?id=vJwjWyt4Ed",
  "prompt": "Extract: (1) full title and authors, (2) abstract summary, (3) which benchmarks used, (4) does it target camera viewpoint robustness on LIBERO-Plus or RoboTwin, (5) publication venue and date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4eadb426-5885-4537-8fb0-b1c9c8bc71a6",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbqCM93TfFQDwp5R4PK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be81ad10-eb16-4713-8a9d-2193eea7d82c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PCZdqxQb3vdQJ1fSFktpEc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4089,
      "cache_read_input_tokens": 19835,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4089
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 396,
          "cache_read_input_tokens": 19835,
          "cache_creation_input_tokens": 4089,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4089,
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

_source line 46 · 2026-05-10T08:50:21.216Z_

<details><summary>↩ Tool result · `toolu_01EjnnTuJbM1pTPVST6QbhhQ`</summary>

```text
# LingBot-VA Repository Analysis

**(1) RoboTwin 2.0-Plus evaluation code:**
No explicit mention of "2.0-Plus" evaluation code. The repository includes "Evaluation on RoboTwin-2.0" with server/client launch scripts, but no specific Plus variant is referenced.

**(2) Camera perturbation evaluation code:**
No camera perturbation evaluation code is mentioned in the provided content.

**(3) Scripts included:**
The repository contains several evaluation and training scripts:
- RoboTwin evaluation: `launch_server.sh`, `launch_client.sh`, multi-GPU variants
- LIBERO evaluation: `launch_server.sh`, `launch_client.sh`
- Post-training: `run_va_posttrain.sh`
- Image-to-video-action generation: `run_launch_va_server_sync.sh`

**(4) Huawei or Zhanguang Zhang mention:**
No references to Huawei or anyone named Zhanguang Zhang appear in the provided content. Contact emails reference "Ant Group" and individuals like Qihang Zhang and Lin Li.

**(5) Overall structure:**
The repository is a robot control framework featuring "autoregressive video-action world modeling" with dual-stream mixture-of-transformers architecture. It includes pretrained models, post-training capabilities on robotic datasets (RoboTwin, LIBERO), inference deployment options, and comprehensive documentation for custom dataset preparation and training pipelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4eadb426-5885-4537-8fb0-b1c9c8bc71a6",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "9ed61e1a-81eb-4fd3-8d65-b0c5ca70d1ba",
  "sourceToolAssistantUUID": "4eadb426-5885-4537-8fb0-b1c9c8bc71a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-10T08:50:21.330Z_

<details><summary>↩ Tool result · `toolu_01SsTVPuMRqKR5gmYjkVodkj`</summary>

```text
Web search results for query: "VQ world model robotic manipulation camera robust 2026"

Links: [{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"Learning View-invariant World Models for Visual Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=vJwjWyt4Ed"},{"title":"Video Generation Models in Robotics: Applications, Research Challenges, Future Directions","url":"https://arxiv.org/html/2601.07823v1"},{"title":"RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation","url":"https://arxiv.org/html/2604.19092v1"},{"title":"awesome-physical-ai/README.md at main · keon/awesome-physical-ai","url":"https://github.com/keon/awesome-physical-ai/blob/main/README.md"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"PointWorld: Scaling 3D World Models for In-The-Wild Robotic Manipulation","url":"https://arxiv.org/html/2601.03782v1"},{"title":"LEARNING VIEW-INVARIANT WORLD MODELS FOR ...","url":"https://openreview.net/pdf?id=vJwjWyt4Ed"},{"title":"Beyond Short-Horizon: VQ-Memory for Robust Long-Horizon Manipulation in Non-Markovian Simulation Benchmarks","url":"https://arxiv.org/html/2603.09513"},{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"}]

Based on the search results, I found several relevant papers and research on VQ world models for robotic manipulation with camera robustness in 2026. Here are the key findings:

## World Models for Robotic Manipulation

WorldVLA integrates an action model and a world model within a unified autoregressive framework for capturing physical dynamics.

## Camera-Robust Approaches

ReViWo (Representation learning for View-invariant World model) leverages multi-view data to learn robust representations for control under viewpoint disturbance. ReViWo maintains robust performance under viewpoint disturbance, while baseline methods suffer from significant performance degradation.

PointWorld is robust to different levels of partial observability and benefits from additional cameras in both training and inference.

## VQ-VAE Approaches

VQ-Memory leverages vector-quantized variational autoencoders (VQ-VAEs) to encode raw joint-state sequences into discrete latent tokens. Additionally, the XR-1 model introduces Unified Vision-Motion Codes (UVMC), a discrete latent representation jointly encoding visual dynamics and robotic motion using dual-branch VQ-VAE with shared codebook, enabling better co-pretraining from human and robot demonstrations.

## Recent World Model Benchmarks

RoboWM-Bench conducts extensive experiments with state-of-the-art video world models across diverse manipulation tasks to systematically evaluate their embodied executability and quantify the embodied executability of current video world models, providing detailed analysis of their performance, key limitations, and potential for generating physically executable behaviors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5eb6efe8-09f8-4125-adb4-92d34e22f2d1",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "77d184f0-a264-4881-ad97-f2e136b47699",
  "sourceToolAssistantUUID": "5eb6efe8-09f8-4125-adb4-92d34e22f2d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-10T08:50:21.435Z_

<details><summary>↩ Tool result · `toolu_01TXbT8WhWsAJWjowgRZBrDG`</summary>

```text
# Paper Summary

**(1) Title and Authors:**
"Learning View-invariant World Models for Visual Robotic Manipulation" by Jing-Cheng Pang, Nan Tang, Kaiyuan Li, Yuting Tang, Xin-Qiang Cai, Zhen-Yu Zhang, Gang Niu, Masashi Sugiyama, and Yang Yu.

**(2) Abstract Summary:**
The paper addresses performance degradation in robotic manipulation when camera viewpoints change. The authors propose ReViWo, which learns robust representations for control under viewpoint disturbance by combining view-invariant and view-dependent representations through an autoencoder framework trained on multi-view simulator data and Open X-Embodiment datasets.

**(3) Benchmarks Used:**
The evaluation employs "Meta-world & PandaGym environments" for simulated testing, along with "real world ALOHA robot" experiments.

**(4) LIBERO-Plus or RoboTwin Targeting:**
No mention of LIBERO-Plus or RoboTwin benchmarks in the provided content.

**(5) Publication Venue and Date:**
ICLR 2025 Conference; published January 22, 2025 (last modified March 2, 2025). The submission was a poster presentation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be81ad10-eb16-4713-8a9d-2193eea7d82c",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "c886e47c-fa75-4fe8-9a5f-7bc792102c8a",
  "sourceToolAssistantUUID": "be81ad10-eb16-4713-8a9d-2193eea7d82c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-10T08:50:22.293Z_

<details><summary>↩ Tool result · `toolu_014rwkaTg7RgspEvxc8Lz2Um`</summary>

```text
Web search results for query: "camera viewpoint robust robot policy world model arxiv May 2026"

Links: [{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"Point Cloud Models Improve Visual Robustness in Robotic Learners","url":"https://arxiv.org/html/2404.18926"},{"title":"[2603.05868] AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.05868"},{"title":"WorldEval: World Model as Real-World Robot Policies Evaluator","url":"https://arxiv.org/html/2505.19017v1"},{"title":"Do You Know Where Your Camera Is? View-Invariant Policy Learning with Camera Conditioning","url":"https://arxiv.org/html/2510.02268v1"},{"title":"Mask World Model: Predicting What Matters for Robust Robot Policy Learning","url":"https://arxiv.org/html/2604.19683"},{"title":"AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models","url":"https://arxiv.org/html/2603.05868"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"[2501.10100] Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics","url":"https://arxiv.org/abs/2501.10100"}]

Based on the search results, I found several relevant papers from May 2026 and nearby months that address camera viewpoint robustness in robot policies and world models:

## Key Recent Papers (May 2026):

1. **OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation** (May 2026)
   - Formulates object addressability as the key issue and proposes OA-WAM, an Object-Addressable World Action Model for robust robot manipulation.

2. **AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models** (March 2026)
   - Proposes a zero-shot camera adaptation framework without additional demonstration data, policy fine-tuning, or architectural modification, with the key idea being to virtually adjust test-time camera observations to match the training camera configuration in real-time.

3. **Point Cloud Models Improve Visual Robustness in Robotic Learners**
   - Shows that policies that explicitly encode point clouds are significantly more robust than their RGB-D counterparts when tested on novel viewpoints, field-of-view, lighting conditions, and distractor objects.

4. **Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising (X-WAM)** (April 2026)
   - Addresses explicit 4D spatial awareness in robot manipulation, requiring precise 6-DoF pose estimation and demonstrates benefits compared to methods that operate purely in 2D pixel space.

5. **Mask World Model: Predicting What Matters for Robust Robot Policy Learning** (April 2026)
   - Addresses how methods typically optimize prediction in an appearance-centric space which encourages modeling nuisance variation like texture, lighting, and background.

These papers collectively address the challenge of making robot policies robust to camera viewpoint changes through different approaches: object-centric representations, novel view synthesis, 3D point clouds, and structured 4D representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f5d7a58-c2e9-4dc5-a475-da530711d5b8",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "20e691f7-12aa-4648-89e7-1552d5ebb70d",
  "sourceToolAssistantUUID": "9f5d7a58-c2e9-4dc5-a475-da530711d5b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-10T08:50:25.170Z_

Now let me fetch the most important remaining papers — AnyCamVLA and the full LIBERO-Plus paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20e691f7-12aa-4648-89e7-1552d5ebb70d",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011Catbr2w84hzg6hdN5FTmz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b7efc442-b3ea-40cb-9a5a-5400c99fcb66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01T5pM9ZzKyxWcYp48VQqNx5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 704,
      "cache_creation_input_tokens": 2321,
      "cache_read_input_tokens": 23924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2321,
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

_source line 51 · 2026-05-10T08:50:30.618Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AW2t6U7LMdB3KgrCc4cBEQ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.05868",
  "prompt": "Extract: (1) full title and authors, (2) abstract, (3) benchmarks used especially LIBERO-Plus and RoboTwin, (4) camera perturbation methodology, (5) performance scores on LIBERO-Plus camera axis, (6) how it compares to OA-WAM or Being-H0.7, (7) code availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7efc442-b3ea-40cb-9a5a-5400c99fcb66",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011Catbr2w84hzg6hdN5FTmz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "caa47181-9739-4d6a-9b6f-5c0460216b41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01T5pM9ZzKyxWcYp48VQqNx5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 704,
      "cache_creation_input_tokens": 2321,
      "cache_read_input_tokens": 23924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2321,
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

_source line 52 · 2026-05-10T08:50:31.793Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JyTjGGetoxQhQybboQuMTJ`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.13626v1",
  "prompt": "Extract: (1) full camera perturbation definition (angles, distances, field of view parameters), (2) the leaderboard / results table for camera axis showing all baseline models, (3) whether Motus is listed on the leaderboard, (4) is full evaluation code available (GitHub link), (5) how many perturbation types and what are they exactly, (6) installation/usage notes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caa47181-9739-4d6a-9b6f-5c0460216b41",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011Catbr2w84hzg6hdN5FTmz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71a2402e-a20c-40ac-a801-f45d4ff72491",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01T5pM9ZzKyxWcYp48VQqNx5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 704,
      "cache_creation_input_tokens": 2321,
      "cache_read_input_tokens": 23924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2321,
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

_source line 53 · 2026-05-10T08:50:32.094Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BURvurG82ppbaZKeNFYa8v`</summary>

```json
{
  "query": "Motus robot manipulation LIBERO-Plus score camera viewpoint 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71a2402e-a20c-40ac-a801-f45d4ff72491",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011Catbr2w84hzg6hdN5FTmz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88af9b48-e2b8-460c-bb03-67b3766c8c39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01T5pM9ZzKyxWcYp48VQqNx5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 704,
      "cache_creation_input_tokens": 2321,
      "cache_read_input_tokens": 23924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2321,
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

_source line 54 · 2026-05-10T08:50:35.448Z_

<details><summary>↩ Tool result · `toolu_01AW2t6U7LMdB3KgrCc4cBEQ`</summary>

```text
# AnyCamVLA Paper Extraction

## (1) Full Title and Authors
**Title:** "AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models"

**Authors:** Hyeongjun Heo, Seungyeon Woo, Sang Min Kim, Junho Kim, Junho Lee, Yonghyeon Lee, Young Min Kim

## (2) Abstract
The paper proposes a framework enabling camera viewpoint adaptation without fine-tuning or architectural changes. It "virtually adjust[s] test-time camera observations to match the training camera configuration in real-time" using feed-forward novel view synthesis to handle both extrinsic and intrinsic camera parameters.

## (3) Benchmarks
The page mentions testing on "the LIBERO benchmark" with extensive experiments. However, the document does not provide specific details about LIBERO-Plus or RoboTwin benchmarks.

## (4) Camera Perturbation Methodology
The approach uses "a recent feed-forward novel view synthesis model which outputs high-quality target view images, handling both extrinsic and intrinsic parameters." This is described as a "plug-and-play" solution.

## (5) Performance Scores on LIBERO-Plus
Specific numerical performance metrics are not provided in the available content.

## (6) Comparison to OA-WAM or Being-H0.7
No comparative data with these specific methods appears in the provided material.

## (7) Code Availability
Not mentioned. A project page is referenced at: https://heo0224.github.io/AnyCamVLA/
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caa47181-9739-4d6a-9b6f-5c0460216b41",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "6419cf6b-ddec-4a98-889b-59de34d25b8a",
  "sourceToolAssistantUUID": "caa47181-9739-4d6a-9b6f-5c0460216b41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-10T08:50:38.505Z_

<details><summary>↩ Tool result · `toolu_01BURvurG82ppbaZKeNFYa8v`</summary>

```text
Web search results for query: "Motus robot manipulation LIBERO-Plus score camera viewpoint 2026"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"Motus Labs Geared Solutions | Robotics & Motion Control","url":"https://motus-labs.com/"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"MOTUS Robot Cameraman for Smartphones - Robotic Gizmos","url":"https://www.roboticgizmos.com/motus-robot-cameraman-smartphones/"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"},{"title":"LIBERO-Object: Lifelong Learning in Robotic Manipulation","url":"https://www.emergentmind.com/topics/libero-object"}]

Based on the search results, I found information about LIBERO-Plus and its analysis of robot manipulation models, though there's limited specific information about "Motus robot" in this context.

## LIBERO-Plus Overview

LIBERO-Plus performs a systematic vulnerability analysis of Vision-Language-Action (VLA) models by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

## Camera Viewpoint Performance Impact

A key finding of the LIBERO-Plus analysis is particularly relevant to your query: models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. More specifically, altering camera position, orientation, or field-of-view causes dramatic performance drops, revealing models' dependence on fixed visual perspectives rather than true 3D understanding.

## Key Findings

Models are most vulnerable to changes in camera viewpoint and robot initial state, which require a high-level understanding of spatial geometry and proprioception. Additionally, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

The search results don't contain specific scoring information for a "Motus robot" on LIBERO-Plus benchmarks. If you're looking for specific performance metrics for a particular model, you may want to check the full LIBERO-Plus paper or project page.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88af9b48-e2b8-460c-bb03-67b3766c8c39",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "17d40aa7-b231-4529-aff0-87fc2e3d21af",
  "sourceToolAssistantUUID": "88af9b48-e2b8-460c-bb03-67b3766c8c39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-10T08:50:39.691Z_

<details><summary>↩ Tool result · `toolu_01JyTjGGetoxQhQybboQuMTJ`</summary>

```text
# LIBERO-Plus: Key Technical Details

## (1) Full Camera Perturbation Definition

The benchmark defines three camera perturbation sub-dimensions:

- **C1 (Camera Distance)**: "Move the camera along its optical axis, changing the distance to the scene center. Camera distances are valued among 1.01× to 2.00× the original value."

- **C2 (Spherical Position)**: "Perturb camera position on a sphere centered at the scene, altering azimuth (Δθ) and elevation (Δϕ) within 15°–75° cones."

- **C3 (Camera Orientation)**: "Fix the camera position but perturb its orientation (yaw, pitch, roll), valued within 2° to 10°."

## (2) Leaderboard Results for Camera Axis

Table 1 shows baseline model performance under camera viewpoint changes:

| Model | Original | Camera (↓) |
|-------|----------|-----------|
| OpenVLA-OFT | 97.1% | 59.7% (-37.4) |
| π₀-fast | 85.5% | 66.4% (-19.1) |
| RIPT-VLA | 97.5% | 58.3% (-39.2) |

The authors note models exhibit "extreme sensitivity" with performance dropping "from 95% to below 30%."

## (3) Motus Listing

Motus is **not mentioned** anywhere in this document.

## (4) Evaluation Code Availability

The paper does **not provide a GitHub link** or explicit code repository reference within the provided content.

## (5) Perturbation Types (7 Total)

1. Objects layout (confounding objects, target pose)
2. Camera viewpoints (distance, position, orientation)
3. Robot initial states (joint angles)
4. Language instructions (distraction, common sense, reasoning)
5. Light conditions (diffuse, direction, specular, shadows)
6. Background textures (scene theme, surface appearance)
7. Sensor noise (motion blur, Gaussian blur, zoom blur, fog, glass blur)

## (6) Installation/Usage Notes

None provided in this research paper; it focuses on benchmark evaluation methodology rather than software distribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71a2402e-a20c-40ac-a801-f45d4ff72491",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "f5911f2d-b1f8-4d6a-ac27-bfdbaf16a653",
  "sourceToolAssistantUUID": "71a2402e-a20c-40ac-a801-f45d4ff72491",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-10T08:50:42.815Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Gvp66iq7HFnkRHXkmcaMX5`</summary>

```json
{
  "url": "https://sylvestf.github.io/LIBERO-plus/",
  "prompt": "Extract: (1) the full leaderboard table with all model scores across all axes, (2) any camera-specific scores for each model, (3) whether Motus, Being-H, OA-WAM or any WAM models are listed, (4) is evaluation code publicly downloadable, (5) any dataset download links"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5911f2d-b1f8-4d6a-ac27-bfdbaf16a653",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbsKMNXpsVFWgPa3zNH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5b366f8-948f-4f32-ba1c-b686ea824306",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UCHc2CPPAmA68Rs2T7Y3Lk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 827,
      "cache_creation_input_tokens": 2059,
      "cache_read_input_tokens": 26245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2059,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-10T08:50:43.570Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hmgikdm3ZmPs5Q3Heup3rW`</summary>

```json
{
  "query": "MOTUS world action model RoboTwin LIBERO-Plus 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5b366f8-948f-4f32-ba1c-b686ea824306",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbsKMNXpsVFWgPa3zNH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ba6862e-95fb-446a-9459-ae208b9c63ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UCHc2CPPAmA68Rs2T7Y3Lk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 827,
      "cache_creation_input_tokens": 2059,
      "cache_read_input_tokens": 26245,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2059,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-10T08:50:43.911Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KS31GC7owMZWTSVju9L7HX`</summary>

```json
{
  "query": "\"MotuBrain\" OR \"Motus\" robot VLA LIBERO-Plus camera score 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ba6862e-95fb-446a-9459-ae208b9c63ba",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbsKMNXpsVFWgPa3zNH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d9b2914-6032-4215-8917-57288c6ad970",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UCHc2CPPAmA68Rs2T7Y3Lk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 827,
      "cache_creation_input_tokens": 2059,
      "cache_read_input_tokens": 26245,
      "output_tokens": 273,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2059
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 827,
          "output_tokens": 273,
          "cache_read_input_tokens": 26245,
          "cache_creation_input_tokens": 2059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2059,
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

_source line 60 · 2026-05-10T08:50:46.671Z_

<details><summary>↩ Tool result · `toolu_01Gvp66iq7HFnkRHXkmcaMX5`</summary>

```text
# LIBERO-Plus Extraction Results

## (1) Full Leaderboard Table
The webpage does not display the complete numerical leaderboard table with all model scores across all perturbation axes. While it references "The figure below illustrates model performance across difficulty levels under four representative perturbation factors," the actual detailed scores are not provided in the text content shown.

## (2) Camera-Specific Scores
One camera performance metric is mentioned: "Our method achieved 92.8% success rate under camera perturbations, surpassing the next best model by 37.2 percentage points." Individual model camera scores are not itemized.

## (3) Specific Model Listings
**No**, the models Motus, Being-H, OA-WAM, or WAM variants are not mentioned anywhere in the provided content.

## (4) Evaluation Code Availability
**Yes**, the code repository is publicly available: "Code" link points to https://github.com/sylvestf/LIBERO-plus

## (5) Dataset Download Links
**Yes**, a dataset link is provided: "Assets" link references https://huggingface.co/datasets/Sylvest/LIBERO-plus. The paper mentions the benchmark contains "10,030 tasks spanning seven perturbation dimensions" with "over 20,000 successful trajectories."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5b366f8-948f-4f32-ba1c-b686ea824306",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "3b352b9c-6f9a-4e16-988a-2572db391808",
  "sourceToolAssistantUUID": "f5b366f8-948f-4f32-ba1c-b686ea824306",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-10T08:50:52.067Z_

<details><summary>↩ Tool result · `toolu_01Hmgikdm3ZmPs5Q3Heup3rW`</summary>

```text
Web search results for query: "MOTUS world action model RoboTwin LIBERO-Plus 2026 arxiv"

Links: [{"title":"Motus: A Unified Latent Action World Model","url":"https://arxiv.org/pdf/2512.13030"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"GitHub - Robbyant/lingbot-va: [RSS 2026] Causal video-action world model for generalist robot control · GitHub","url":"https://github.com/robbyant/lingbot-va"},{"title":"GitHub - thu-ml/Motus: Official code of Motus: A Unified Latent Action World Model · GitHub","url":"https://github.com/thu-ml/Motus"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"[2512.13030] Motus: A Unified Latent Action World Model","url":"https://arxiv.org/abs/2512.13030"},{"title":"GigaWorld-Policy: An Efficient Action-Centered World–Action Model","url":"https://arxiv.org/html/2603.17240"},{"title":"[2603.22078] Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/abs/2603.22078"},{"title":"Causal World Modeling for Robot Control","url":"https://arxiv.org/html/2601.21998v1"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666"}]

I found several highly relevant papers from arXiv related to your search query. Here's what I found:

## Key Results:

**Motus: A Unified Latent Action World Model**

Motus is a unified latent action world model that leverages existing general pretrained models and rich, sharable motion information. It introduces a Mixture-of-Transformer (MoT) architecture to integrate three experts (understanding, video generation, and action) and adopts a UniDiffuser-style scheduler to enable flexible switching between different modeling modes (world models, vision-language-action models, inverse dynamics models, video generation models, and video-action joint prediction models).

Motus achieves superior performance against state-of-the-art methods in both simulation (a +15% improvement over X-VLA and a +45% improvement over Pi0.5) and real-world scenarios (improved by +11~48%).

**Performance on RoboTwin 2.0 and LIBERO-Plus:**

With 50 clean and 500 randomized data entries per task, Motus merges the data from all 50 tasks for multi-task training on RoboTwin 2.0, achieving 87.02% average success rate (+15% over X-VLA, +45% over π₀.₅).

Several other related world-action models have also been evaluated on these benchmarks, including LIBERO-Plus, which primarily evaluates single-arm dexterity under perturbations, whereas RoboTwin 2.0-Plus focuses on the robustness of bimanual coordination.

The arXiv paper for Motus can be found at https://arxiv.org/abs/2512.13030.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ba6862e-95fb-446a-9459-ae208b9c63ba",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "98158596-c9a8-406c-9003-e321b26394fe",
  "sourceToolAssistantUUID": "2ba6862e-95fb-446a-9459-ae208b9c63ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-10T08:50:52.694Z_

<details><summary>↩ Tool result · `toolu_01KS31GC7owMZWTSVju9L7HX`</summary>

```text
Web search results for query: ""MotuBrain" OR "Motus" robot VLA LIBERO-Plus camera score 2026"

Links: [{"title":"MotuBrain World Model Tops Two Global Benchmarks — A Breakthrough in Robot Intelligence - DeepInsightAI","url":"https://deepinsightai.io/motubrain-world-model/"},{"title":"Motubrain.org","url":"https://motubrain.org/"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence","url":"https://www.prnewswire.com/news-releases/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence-302757280.html"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence | RoboticsTomorrow","url":"https://www.roboticstomorrow.com/news/2026/04/29/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/26497/"},{"title":"GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub","url":"https://github.com/AgibotTech/ACoT-VLA"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v1"},{"title":"VLA Models Compared: OpenVLA vs π0 vs SmolVLA vs RT-2 (2026 Guide) | SVRC","url":"https://www.roboticscenter.ai/guides/vla-models-comparison"}]

Based on the search results, here's what I found about MotuBrain, Motus, robot VLA, LIBERO-Plus, and related camera scores:

## MotuBrain - World Action Model

MotuBrain is a World Action Model announced by ShengShu Technology on April 29, 2026, that replaces multiple task-specific systems with a single, unified model functioning as a robotic brain for the physical world.

### Performance Scores

MotuBrain achieved a 63.77 EWM Score on WorldArena. On RoboTwin 2.0, it scored an average of 96.0 across 50 predetermined tasks and remains the only model to exceed 95.0 in randomized environments.

### Key Features

MotuBrain is built on a Unified Multimodal Model that treats video and action as two continuous modalities, providing five capabilities: vision-language-action control (VLA), world modelling, video generation, inverse dynamics modelling, and joint video-action prediction.

### Scaling Performance

In task-scaling evaluations, MotuBrain's average success rate reached approximately 92% at 50 tasks, while in data-scaling evaluations it achieved about 92% average success at 27,500 episodes, compared with roughly 85% for Motus and 68% for Pi-0.5.

## Related Information

Motus was released last December as an earlier unified world-action model that MotuBrain builds upon.

## LIBERO-Plus Benchmark

LIBERO is used as a diagnostic tool to conduct comprehensive analysis of contemporary VLA models. However, the search results don't contain specific MotuBrain scores on the LIBERO-Plus benchmark itself.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d9b2914-6032-4215-8917-57288c6ad970",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "4adca0e4-a12a-47ef-99e4-89c625fbd7d4",
  "sourceToolAssistantUUID": "4d9b2914-6032-4215-8917-57288c6ad970",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-10T08:50:56.721Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UZMzskDGCk3MjxiQuoE6BL`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.27792v2",
  "prompt": "Extract: (1) full title and authors, (2) LIBERO-Plus scores especially camera-specific axis breakdown, (3) RoboTwin 2.0-Plus scores, (4) aggregate LIBERO-Plus score for MotuBrain, (5) comparison table with other models like OA-WAM, Being-H0.7, (6) any camera-specific SOTA claims"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4adca0e4-a12a-47ef-99e4-89c625fbd7d4",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbtGxY3ZrvE1reBQXp6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb23bf95-113e-4e1b-8824-ec62e73e11c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WZ5X7niwS3KRFbpzTqVRS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 28304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3391,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-10T08:50:58.594Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01444EKbSxzMFRkZXDZgD8Lc`</summary>

```json
{
  "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html",
  "prompt": "Extract: (1) all LIBERO-Plus leaderboard scores mentioned including camera-specific axis scores, (2) which models are SOTA on camera axis, (3) any new May 2026 papers addressing viewpoint robustness, (4) OA-WAM, Being-H0.7, MotuBrain scores on LIBERO-Plus, (5) any papers targeting the same research gap as viewpoint-invariant world models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb23bf95-113e-4e1b-8824-ec62e73e11c9",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbtGxY3ZrvE1reBQXp6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99bc41c4-83d7-47df-93b4-30b9b22e5ae8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WZ5X7niwS3KRFbpzTqVRS6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3391,
      "cache_read_input_tokens": 28304,
      "output_tokens": 350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3391
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 350,
          "cache_read_input_tokens": 28304,
          "cache_creation_input_tokens": 3391,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3391,
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

_source line 65 · 2026-05-10T08:51:02.602Z_

<details><summary>↩ Tool result · `toolu_01UZMzskDGCk3MjxiQuoE6BL`</summary>

```text
# MotuBrain Document Analysis

## (1) Full Title and Authors

**Title:** "MotuBrain: An Advanced World Action Model for Robot Control"

**Authors:** MotuBrain Team (affiliated with Shengshu)

The paper lists contributors across data collection, base model development, post-training, and evaluation, with Hengkai Tan as Project Lead and Fan Bao and Jun Zhu as advisors.

## (2)-(5) LIBERO-Plus and RoboTwin 2.0-Plus Scores

**Not found in document.** The provided content does not contain LIBERO-Plus benchmark results, camera-specific axis breakdowns, or RoboTwin 2.0-Plus scores. The evaluation section focuses on:
- RoboTwin 2.0 (standard version): 95.8% clean, 96.1% randomized
- WorldArena leaderboard (EWMScore: 63.77)
- Real-world household tasks

## (6) Camera-Specific SOTA Claims

The paper mentions multiview support through "view-dependent 3D RoPE offsets" that enable "seamless support for an arbitrary number of camera views without modifying the backbone architecture." However, no explicit camera-specific state-of-the-art claims appear in the document.

**Summary:** The requested benchmark comparisons (LIBERO-Plus, RoboTwin 2.0-Plus, OA-WAM comparison table) are absent from this arXiv HTML version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb23bf95-113e-4e1b-8824-ec62e73e11c9",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "ce304d3e-bddf-4570-a477-b2e139ad6b16",
  "sourceToolAssistantUUID": "fb23bf95-113e-4e1b-8824-ec62e73e11c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-10T08:51:04.640Z_

<details><summary>↩ Tool result · `toolu_01444EKbSxzMFRkZXDZgD8Lc`</summary>

```text
Based on my careful review of the provided content, I must report that **none of the specific information you requested appears in this document**.

Specifically:

1. **LIBERO-Plus leaderboard scores**: Not mentioned. The article discusses LIBERO benchmarks generally but does not reference a "LIBERO-Plus" leaderboard or camera-specific axis scores.

2. **SOTA models on camera axis**: Not addressed in this content.

3. **May 2026 papers on viewpoint robustness**: The document is dated October 2025 and does not discuss papers from May 2026 or specifically address viewpoint-invariant world models.

4. **OA-WAM, Being-H0.7, MotuBrain scores**: These specific model names and their LIBERO-Plus performance metrics do not appear anywhere in the text.

5. **Papers targeting viewpoint-invariant world models**: While the article discusses various VLA research trends (discrete diffusion, embodied reasoning, tokenizers, etc.), it does not specifically address viewpoint-invariant world models as a research gap.

The document focuses on ICLR 2026 VLA submission trends and mentions benchmark results on LIBERO, CALVIN, and SIMPLER, but not the specialized metrics you're seeking.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99bc41c4-83d7-47df-93b4-30b9b22e5ae8",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "d3d68675-1076-4038-b937-c063b746bdc1",
  "sourceToolAssistantUUID": "99bc41c4-83d7-47df-93b4-30b9b22e5ae8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-10T08:51:09.179Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CvssYUD3iyQhFvEzyxVzUw`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.13030",
  "prompt": "Extract: (1) LIBERO-Plus scores for Motus (overall and per-axis if available), (2) RoboTwin 2.0-Plus scores for Motus, (3) camera-specific scores, (4) comparison against other WAMs and VLAs, (5) code availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3d68675-1076-4038-b937-c063b746bdc1",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbuBAohkyGf8Qnn3MzK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12eda063-a118-41e4-b9dc-a2e633d1a0fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L9GC1YixM5aWeqFuoJQEce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 31695,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1047,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-10T08:51:09.804Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XqkHSsY853ipaNuU6drbKK`</summary>

```json
{
  "query": "\"OA-WAM\" LIBERO-Plus table camera 80.5 SOTA robot manipulation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12eda063-a118-41e4-b9dc-a2e633d1a0fe",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbuBAohkyGf8Qnn3MzK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f45c7042-e812-478f-9e91-c776c01bd388",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L9GC1YixM5aWeqFuoJQEce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 31695,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1047,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-10T08:51:10.483Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017rAHWvJ1WQ8dMap7uP7Ti8`</summary>

```json
{
  "query": "AnyCamVLA LIBERO-Plus camera score novel view synthesis robot 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f45c7042-e812-478f-9e91-c776c01bd388",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbuBAohkyGf8Qnn3MzK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8633cc6a-af70-4a8a-ab81-2ee4e0b20956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L9GC1YixM5aWeqFuoJQEce",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 31695,
      "output_tokens": 265,
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
          "output_tokens": 265,
          "cache_read_input_tokens": 31695,
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

_source line 70 · 2026-05-10T08:51:12.737Z_

<details><summary>↩ Tool result · `toolu_01CvssYUD3iyQhFvEzyxVzUw`</summary>

```text
# Motus Paper: Requested Information

Based on the provided webpage content, I cannot extract the specific information you requested:

**What's Available:**
The abstract mentions that Motus demonstrates "superior performance against state-of-the-art methods in both simulation (a +15% improvement over X-VLA and a +45% improvement over Pi0.5) and real-world scenarios (improved by +11~48%)," but the webpage does not contain detailed benchmark scores for LIBERO-Plus, RoboTwin 2.0-Plus, or camera-specific results.

**What's Not Included:**
- Specific LIBERO-Plus scores and per-axis breakdowns
- RoboTwin 2.0-Plus performance metrics
- Camera-specific evaluation data
- Detailed comparisons against other world action models and vision-language-action systems
- Code availability information

**To Find This Information:**
You would need to access the full PDF or HTML version of the paper (linked on the arXiv page) where the results tables and supplementary details are presented.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12eda063-a118-41e4-b9dc-a2e633d1a0fe",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "f2ef573e-2adc-4c80-a955-c82e318e741a",
  "sourceToolAssistantUUID": "12eda063-a118-41e4-b9dc-a2e633d1a0fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-10T08:51:14.631Z_

<details><summary>↩ Tool result · `toolu_01XqkHSsY853ipaNuU6drbKK`</summary>

```text
Web search results for query: ""OA-WAM" LIBERO-Plus table camera 80.5 SOTA robot manipulation 2026"

Links: [{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"VLA SOTA Leaderboard","url":"https://sota.evomind-tech.com/"},{"title":"ALOHA Robot: Stanford's Open-Source Bimanual System — Setup, Cost, and Alternatives (2026)","url":"https://www.roboticscenter.ai/learn/aloha-robot"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"Would you like to set up an online leaderboard for SOTA methods on libero? · Issue #25 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/25"},{"title":"RoboMM: All-in-One Multimodal Large Model for Robotic Manipulation","url":"https://arxiv.org/html/2412.07215v1"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"PAL Robotics to unveil new manipulation robot at ICRA 2026","url":"https://roboticsandautomationnews.com/2026/04/24/pal-robotics-to-debut-new-manipulation-robot-at-icra-2026/100968/"}]

Based on the search results, I found relevant information about LIBERO-Plus and robotic manipulation benchmarks:

LIBERO Plus is an extended benchmark testing robustness across 7 perturbation dimensions: Camera, Robot, Language, Light, Background, Noise, and Layout.

The benchmark introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

However, the search results do not contain specific information about "OA-WAM," the specific metric "80.5," or other details you mentioned in your query. The search found general information about LIBERO-Plus as a robustness analysis benchmark for vision-language-action models in robot manipulation, but not the specific configuration or model you're asking about.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f45c7042-e812-478f-9e91-c776c01bd388",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "a486350d-b319-4e37-91c2-ad3936f8a797",
  "sourceToolAssistantUUID": "f45c7042-e812-478f-9e91-c776c01bd388",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-10T08:51:16.905Z_

<details><summary>↩ Tool result · `toolu_017rAHWvJ1WQ8dMap7uP7Ti8`</summary>

```text
Web search results for query: "AnyCamVLA LIBERO-Plus camera score novel view synthesis robot 2026"

Links: [{"title":"AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models","url":"https://arxiv.org/html/2603.05868"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"Novel View Synthesis from A Few Glimpses via Test-Time Natural Video Completion | OpenReview","url":"https://openreview.net/forum?id=zwmq0MsIMG"},{"title":"How brittle are the VLA models in robotics | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"},{"title":"LIBERO vs CALVIN (2026): Benchmark Comparison | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/datasets/compare/libero-vs-calvin"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | Takara TLDR","url":"https://tldr.takara.ai/p/2510.13626"}]

Based on the search results, here's what I found about these topics:

## AnyCamVLA

AnyCamVLA proposes a zero-shot camera adaptation framework without additional demonstration data, policy fine-tuning, or architectural modification, with the key idea of virtually adjusting test-time camera observations to match the training camera configuration in real-time. It uses a feed-forward novel view synthesis model which outputs high-quality target view images, handling both extrinsic and intrinsic parameters.

Under large viewpoint shifts (up to 15 cm translation and 60° rotation in camera extrinsics), the method shows minimal performance degradation, achieving the best task success rate over baselines on the LIBERO benchmark.

## LIBERO-Plus

LIBERO-Plus performs a systematic vulnerability analysis by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise. The analysis exposes critical weaknesses: models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

The AnyCamVLA paper constructs a multi-view dataset by rendering diverse camera viewpoints using objects and scene textures sourced from LIBERO-Plus, replacing all objects and surface textures in the original LIBERO scenes with assets from LIBERO-Plus while preserving the robot and workspace layout.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8633cc6a-af70-4a8a-ab81-2ee4e0b20956",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "24fe4abe-677e-46c0-bfd6-06beaf92573d",
  "sourceToolAssistantUUID": "8633cc6a-af70-4a8a-ab81-2ee4e0b20956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-10T08:51:20.698Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Wg5MBvRoN6K1t9vvWyqzmt`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.05868",
  "prompt": "Extract: (1) all LIBERO-Plus results tables, especially camera scores, (2) comparison to other models on camera perturbation, (3) does it use LIBERO-Plus exactly or a custom benchmark, (4) exact camera perturbation amounts used in evaluation, (5) whether the proposed method beats OA-WAM or other baselines on camera axis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24fe4abe-677e-46c0-bfd6-06beaf92573d",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011Catbv4fR2tunWVneMW17k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2eaf0ec-5a13-4fab-ba79-fb2f38b421bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01V8W9ufXQBhgncBX1i5yRQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2291,
      "cache_read_input_tokens": 32742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2291,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-10T08:51:22.634Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BLBXjtcCa1gN7MCTxsubQa`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.13030",
  "prompt": "Extract all result tables: (1) LIBERO-Plus scores for Motus and baselines, especially camera-specific axis, (2) RoboTwin 2.0 or 2.0-Plus scores, (3) comparison of Motus against other world-action models and VLAs, (4) any per-axis breakdown for robustness evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2eaf0ec-5a13-4fab-ba79-fb2f38b421bc",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011Catbv4fR2tunWVneMW17k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "264a096d-5c57-450c-918e-a83137de2515",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01V8W9ufXQBhgncBX1i5yRQv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2291,
      "cache_read_input_tokens": 32742,
      "output_tokens": 310,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2291
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 310,
          "cache_read_input_tokens": 32742,
          "cache_creation_input_tokens": 2291,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2291,
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

_source line 75 · 2026-05-10T08:51:26.401Z_

<details><summary>↩ Tool result · `toolu_01Wg5MBvRoN6K1t9vvWyqzmt`</summary>

```text
# AnyCamVLA Paper Analysis

## (1) LIBERO-Plus Results Tables

The paper does **not include LIBERO-Plus results tables**. Instead, it evaluates on the original LIBERO benchmark with custom camera perturbations. The authors created their own viewpoint-augmented dataset rather than using LIBERO-Plus directly.

## (2) Comparison to Other Models on Camera Perturbation

The paper compares against:
- **OpenVLA-OFT**: Drops from 85.2% (small perturbation) to 46.2% (large)
- **π0.5**: Declines from 92.4% to 39.9% across perturbation levels
- **GeoAwareVLA**: Achieves 86.1% on agent camera but collapses to 5.2% on wrist camera
- **Proposed method (Ours-π)**: Maintains 94.5% average success rate across all perturbation levels

## (3) Benchmark Configuration

The authors used "the original LIBERO dataset" but "created a viewpoint-augmented training dataset" with "50 agent camera viewpoints and 15 wrist camera viewpoints" for evaluation purposes—not LIBERO-Plus itself.

## (4) Exact Camera Perturbation Amounts

- **Agent camera**: Spherical coordinate perturbations on (r, θ, φ) at three levels
- **Wrist camera**: Perturbations to x, y coordinates and pitch angle
- Real-world: Up to "15 cm translation and 60° rotation in camera extrinsics"

## (5) Comparison to OA-WAM or Similar Baselines

The paper does **not mention or compare against OA-WAM**. Its primary baselines are OpenVLA-OFT, π0.5, and GeoAwareVLA.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2eaf0ec-5a13-4fab-ba79-fb2f38b421bc",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "c40cf9b3-8c4a-4c7a-8ddc-fbb1c6e21069",
  "sourceToolAssistantUUID": "d2eaf0ec-5a13-4fab-ba79-fb2f38b421bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-10T08:51:28.399Z_

<details><summary>↩ Tool result · `toolu_01BLBXjtcCa1gN7MCTxsubQa`</summary>

```text
# Result Tables from Motus Paper

Based on the provided content, here are the key result tables:

## 1. RoboTwin 2.0 Simulation Results
**Table 2** presents evaluation on 50+ manipulation tasks:
- **Motus (Clean)**: 88.66% average success rate
- **Motus (Randomized)**: 87.02% average success rate
- **X-VLA (Clean)**: 72.80%
- **π₀.₅ (Clean)**: 42.98%

Motus demonstrates "+45% improvement over π₀.₅" and "+15% improvement over X-VLA."

## 2. Real-World Robot Performance
**Table 3** shows partial success rates across dual-arm platforms:

**AC-One Platform:**
- Motus average: 63.22%
- π₀.₅ average: 14.79%

**Agilex-Aloha-2 Platform:**
- Motus average: 59.30%
- π₀.₅ average: 48.60%

## 3. LIBERO-Long Benchmark
**Table 9** reports language-conditioned task performance:
- **Motus**: 97.6 (matches X-VLA's state-of-the-art)
- X-VLA: 97.6
- UniVLA: 94.0

## 4. World Model Quality Metrics
**Table 6** evaluates generative quality on real-world data:
- Agilex-Aloha-2: FID=9.46, FVD=49.28
- AC-One: FID=12.96, FVD=73.13

**Note:** The document does not include LIBERO-Plus scores, camera-specific axis breakdowns, or per-axis robustness evaluations as requested.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "264a096d-5c57-450c-918e-a83137de2515",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "a2f8d1bc-95e3-4f6d-bf41-e3d1fb095ec6",
  "sourceToolAssistantUUID": "264a096d-5c57-450c-918e-a83137de2515",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-10T08:51:33.484Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BS4pmfp1thoofaHeTdp7Em`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.22078v1",
  "prompt": "I need the COMPLETE result tables from this paper. Specifically: (1) Table 3 for RoboTwin 2.0-Plus - give ALL rows and columns with exact numbers for Camera, Robot, Language, Light, Background, Noise, Layout axes for each model, (2) Table 4 for LIBERO-Plus - give ALL rows and columns with exact numbers for each model on each axis, (3) how is RoboTwin 2.0-Plus camera perturbation defined exactly (degrees, parameters), (4) who are the paper authors and affiliations, (5) exact abstract text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2f8d1bc-95e3-4f6d-bf41-e3d1fb095ec6",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbvukfJdQwppkVXsdKe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1522b915-83cf-4059-8c68-1b2e57b30948",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AFAiGahfAAEicGu1xcXCmK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1248,
      "cache_read_input_tokens": 35033,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1248
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 35033,
          "cache_creation_input_tokens": 1248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1248,
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

_source line 78 · 2026-05-10T08:51:48.210Z_

<details><summary>↩ Tool result · `toolu_01BS4pmfp1thoofaHeTdp7Em`</summary>

```text
# Paper Analysis: "Do World Action Models Generalize Better than VLAs?"

## Authors and Affiliations
**Authors:** Zhanguang Zhang, Zhiyuan Li, Behnam Rahmati, Rui Heng Yang, Yintao Ma, Amir Rasouli, Sajjad Pakdamansavoji, Yangzheng Wu, Lingfeng Zhang, Tongtong Cao, Feng Wen, Xingyue Quan, and Yingxue Zhang

**Affiliations:** Huawei Technologies; University of Toronto (Li's affiliation)

**arXiv ID:** 2603.22078v1 | **Date:** March 23, 2026

---

## Abstract (Exact Text)
"Robot action planning in the real world is challenging as it requires not only understanding the current state of the environment but also predicting how it will evolve in response to actions... Overall, our findings shed light on critical insights into the strengths of WAMs relative to VLAs, as well as the remaining challenges for real-world deployment."

---

## Table 3: RoboTwin 2.0-Plus Results

| Model | Original | Camera | Robot | Language | Light | Background | Noise | Layout | Total |
|-------|----------|--------|-------|----------|-------|------------|-------|--------|-------|
| π0.5 | 78.4 | 45.6 | 27.6 | 74.4 | 49.6 | 71.7 | 64.9 | 56.8 | 58.6 |
| X-VLA | 65.6 | 23.2 | 65.2 | 64.4 | 63.1 | 58.6 | 49.7 | 34.8 | 53.1 |
| MOTUS | 87.0 | 21.6 | 85.0 | 83.2 | 84.6 | 84.4 | 43.1 | 82.8 | 71.5 |
| LingBot-VA | 92.1 | 28.9 | 36.2 | 87.3 | 89.0 | 91.3 | 80.9 | 87.9 | 74.2 |

---

## Table 4: LIBERO-Plus Results

| Model | Original | Camera | Robot | Language | Light | Background | Noise | Layout | Total |
|-------|----------|--------|-------|----------|-------|------------|-------|--------|-------|
| π0 | 94.2 | 13.8 | 6.0 | 58.8 | 85.0 | 81.4 | 79.0 | 68.9 | 53.6 |
| π0 (rerun) | 91.3 | 61.0 | 40.8 | 63.5 | 89.3 | 84.1 | 80.1 | 76.4 | 69.4 |
| π0-FAST | 85.5 | 65.1 | 21.6 | 61.0 | 73.2 | 73.2 | 74.4 | 68.8 | 61.6 |
| π0.5 | 96.9 | 75.4 | 77.5 | 85.6 | 96.9 | 94.6 | 89.7 | 85.7 | 85.7 |
| OpenVLA-OFT_m | 97.6 | 55.6 | 21.7 | 81.0 | 92.7 | 91.0 | 78.6 | 68.7 | 67.9 |
| UniVLA | 95.2 | 1.8 | 46.2 | 69.6 | 69.0 | 81.0 | 21.2 | 31.9 | 42.9 |
| RIPT-VLA | 97.5 | 55.2 | 31.2 | 77.6 | 88.4 | 91.6 | 73.5 | 74.2 | 68.4 |
| X-VLA | 98.1 | 23.4 | 89.7 | 75.7 | 88.2 | 96.0 | 62.7 | 71.8 | 71.4 |
| HoloBrain0-GD | 96.7 | 65.5 | 58.2 | 78.7 | 88.1 | 90.3 | 66.9 | 79.5 | 74.0 |
| VLA-JEPA | 97.2 | 64.2 | 67.7 | 88.1 | 91.8 | 93.4 | 65.8 | 83.9 | 77.9 |
| ABot-M0 | 98.6 | 60.4 | 67.9 | 86.4 | 96.2 | 91.6 | 86.4 | 82.6 | 80.5 |
| GE-Act | 94.4 | 60.7 | 77.0 | 77.4 | 95.8 | 86.0 | 90.9 | 80.2 | 80.3 |
| Cosmos-Policy | 98.5 | 75.8 | 63.3 | 81.7 | 96.5 | 88.9 | 92.7 | 82.2 | 82.2 |

---

## Camera Viewpoint Perturbation Definition

The document does not specify exact degrees or parameters. It only states: "Camera, altering the viewpoint pose of the third-person camera" and notes that camera viewpoint variations "remain challenging for WAMs." Specific technical parameters are not provided in the available content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1522b915-83cf-4059-8c68-1b2e57b30948",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "dde09ecf-cd6f-47f3-ad34-3324243923d8",
  "sourceToolAssistantUUID": "1522b915-83cf-4059-8c68-1b2e57b30948",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 79 · 2026-05-10T08:51:54.251Z_

Now I have all the critical data I need. Let me do one final sweep for any remaining gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dde09ecf-cd6f-47f3-ad34-3324243923d8",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbxNvKY2HB417hZewF8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6c95e13-1b4b-4c4b-b57b-5bb9a267aeec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Be8ydZkEVJLf8He7D3w7bE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1731,
      "cache_read_input_tokens": 36281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1731,
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

_source line 80 · 2026-05-10T08:51:55.125Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GwyfpDmkjXcuws8CqZ7Y5P`</summary>

```json
{
  "query": "\"RoboTwin 2.0-Plus\" camera perturbation definition degrees parameters evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6c95e13-1b4b-4c4b-b57b-5bb9a267aeec",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbxNvKY2HB417hZewF8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6e94c94-6a21-461a-bd1b-cee3c9754d25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Be8ydZkEVJLf8He7D3w7bE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1731,
      "cache_read_input_tokens": 36281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1731,
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

_source line 81 · 2026-05-10T08:51:57.190Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WJV37tubfHLXYbt1xjZQhj`</summary>

```json
{
  "url": "https://sota.evomind-tech.com/",
  "prompt": "Extract: (1) LIBERO-Plus leaderboard including camera-specific scores for all models, (2) OA-WAM score on camera axis, (3) Being-H0.7 score on LIBERO-Plus, (4) any model above 80.5% on camera axis, (5) most recent entries from May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6e94c94-6a21-461a-bd1b-cee3c9754d25",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbxNvKY2HB417hZewF8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a8a3188-c2f4-4711-9ddd-7d489501e79e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Be8ydZkEVJLf8He7D3w7bE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1731,
      "cache_read_input_tokens": 36281,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1731
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 236,
          "cache_read_input_tokens": 36281,
          "cache_creation_input_tokens": 1731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1731,
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

_source line 82 · 2026-05-10T08:51:59.765Z_

<details><summary>↩ Tool result · `toolu_01WJV37tubfHLXYbt1xjZQhj`</summary>

```text
I cannot provide the information you've requested. The webpage content provided does not contain:

1. Detailed LIBERO-Plus leaderboard data with camera-specific scores
2. OA-WAM scores on the camera axis
3. Being-H0.7 scores
4. Models exceeding 80.5% on camera axis
5. Entries from May 2026

The page shows that LIBERO Plus is "an extended benchmark testing robustness across 7 perturbation dimensions" but displays "0 Models" with no actual leaderboard data visible. To access this information, you would need to visit the full leaderboard at `/benchmarks/liberoplus/` directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a8a3188-c2f4-4711-9ddd-7d489501e79e",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "6f9bbc0d-e007-4258-a445-d467744f2ef9",
  "sourceToolAssistantUUID": "5a8a3188-c2f4-4711-9ddd-7d489501e79e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-10T08:52:00.646Z_

<details><summary>↩ Tool result · `toolu_01GwyfpDmkjXcuws8CqZ7Y5P`</summary>

```text
Web search results for query: ""RoboTwin 2.0-Plus" camera perturbation definition degrees parameters evaluation"

Links: [{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://arxiv.org/html/2506.18088v2"},{"title":"RoboTwin 2.0","url":"https://robotwin-platform.github.io/"},{"title":"(PDF) RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://www.researchgate.net/publication/392941279_RoboTwin_20_A_Scalable_Data_Generator_and_Benchmark_with_Strong_Domain_Randomization_for_Robust_Bimanual_Robotic_Manipulation"},{"title":"GitHub - RoboTwin-Platform/RoboTwin: RoboTwin 2.0 Offical Repo · GitHub","url":"https://github.com/robotwin-Platform/RoboTwin"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation | OpenReview","url":"https://openreview.net/forum?id=vAPIIscwc7"},{"title":"RoboTwin/README.md at main · TianxingChen/RoboTwin","url":"https://github.com/TianxingChen/RoboTwin/blob/main/README.md"},{"title":"[Literature Review] RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://www.themoonlight.io/en/review/robotwin-20-a-scalable-data-generator-and-benchmark-with-strong-domain-randomization-for-robust-bimanual-robotic-manipulation"},{"title":"RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong","url":"https://robogen-iros.github.io/accepted/9_RoboTwin_2_0_A_Scalable_Data.pdf"},{"title":"RoboTwin 2.0: Large-Scale Robot Simulation & Dataset","url":"https://www.emergentmind.com/topics/robotwin-2-0"},{"title":"[2506.18088] RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation","url":"https://arxiv.org/abs/2506.18088"}]

Based on the search results, I found information about RoboTwin 2.0 and camera perturbations:

## Camera Perturbation in RoboTwin 2.0

To improve robustness to camera jitter and calibration errors, RoboTwin 2.0 applies random 3D perturbations to simulated camera poses (position and orientation), with the displacement magnitude bounded by 1 cm.

The search results indicate that camera perturbations are implemented as part of the domain randomization strategy to enhance sim-to-real transfer. However, I should note that the search results do not contain information about a specific product called "RoboTwin 2.0-Plus" or detailed parameter specifications regarding degrees of freedom for camera perturbation definitions. 

The camera perturbation parameters mentioned in the academic literature are:
- **Type**: Random 3D spatial perturbations to camera poses
- **Parameters**: Position and orientation (translation and rotation)
- **Bound**: Maximum displacement magnitude of 1 cm

If you're looking for more specific technical details about "RoboTwin 2.0-Plus" (which may be a different product or version), or more granular parameter definitions like specific angle ranges in degrees, you may need to consult the official RoboTwin 2.0 documentation or technical specifications directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6e94c94-6a21-461a-bd1b-cee3c9754d25",
  "isSidechain": true,
  "promptId": "34ea3b4e-b5d6-45bc-8c90-1dffa5c207b8",
  "agentId": "a3e0967fbcc983b14",
  "type": "user",
  "uuid": "f867e7ca-cf5d-4694-90d7-0131754ffed0",
  "sourceToolAssistantUUID": "b6e94c94-6a21-461a-bd1b-cee3c9754d25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 84 · 2026-05-10T08:53:22.136Z_

I now have comprehensive data across all five research tasks. Here is the complete, detailed report:

---

## Comprehensive Research Report: Robotics Proposal Reviewer Concerns

---

## TASK 1: RoboTwin 2.0-Plus Evaluation Code Availability

### What Is RoboTwin 2.0-Plus?
RoboTwin 2.0-Plus is an **in-house benchmark created by Huawei Technologies** (principal author: Zhanguang Zhang and colleagues). It is NOT a community or open-source benchmark. It follows "a similar perturbation protocol" to LIBERO-Plus, applied to the two-arm Aloha-Agilex dual-arm setup from RoboTwin 2.0. It is introduced in arXiv 2603.22078 ("Do World Action Models Generalize Better than VLAs? A Robustness Study," March 23, 2026).

### Is Evaluation Code Publicly Available?
**No.** There is no public release of RoboTwin 2.0-Plus evaluation code. Specifically:

- The paper (2603.22078) contains **no code availability statement** and **no GitHub links**.
- The official RoboTwin GitHub (`github.com/RoboTwin-Platform/RoboTwin`) covers the standard RoboTwin 2.0 benchmark only. Its repo structure includes `envs/`, `policy/`, `script/`, `task_config/`, and `collect_data.sh`, but **nothing specific to 2.0-Plus perturbation protocols**.
- The LingBot-VA repo (`github.com/Robbyant/lingbot-va`) — whose model scored highest on RoboTwin 2.0-Plus (74.2%) — contains evaluation scripts for RoboTwin 2.0 only, with no "Plus" variant code and no camera perturbation evaluation scripts.
- The MOTUS repo (`github.com/thu-ml/Motus`) evaluates on standard RoboTwin 2.0; no 2.0-Plus perturbation code.
- Third-party eval wrappers (X-VLA, vidar-robotwin, StarVLA) all use the standard RoboTwin 2.0 protocol.
- Huawei has not released a standalone evaluation repository for 2.0-Plus.

### Camera Perturbation Definition in RoboTwin 2.0-Plus
The paper describes camera perturbation only as "altering the viewpoint pose of the third-person camera." **No specific angular ranges, translation bounds, or sphere-parameterization are published.** In the base RoboTwin 2.0, camera perturbation for domain randomization uses random 3D pose perturbations bounded to ~1 cm displacement — but whether 2.0-Plus adopts LIBERO-Plus's more extreme 15°–75° cone protocol or something different is **not specified in any public document**.

### What Would Be Needed to Reproduce It
To reproduce RoboTwin 2.0-Plus evaluation, one would need: (a) access to the Huawei-internal perturbation code, or (b) to implement camera perturbation on top of the standard RoboTwin 2.0 simulator by adapting LIBERO-Plus's C1/C2/C3 protocol to the Aloha-Agilex bimanual setup.

### Complete RoboTwin 2.0-Plus Results Table (Table 3, from 2603.22078)

| Model | Original | Camera | Robot | Language | Light | Background | Noise | Layout | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| π0.5 | 78.4 | 45.6 | 27.6 | 74.4 | 49.6 | 71.7 | 64.9 | 56.8 | **58.6** |
| X-VLA | 65.6 | 23.2 | 65.2 | 64.4 | 63.1 | 58.6 | 49.7 | 34.8 | **53.1** |
| MOTUS | 87.0 | 21.6 | 85.0 | 83.2 | 84.6 | 84.4 | 43.1 | 82.8 | **71.5** |
| LingBot-VA | 92.1 | 28.9 | 36.2 | 87.3 | 89.0 | 91.3 | 80.9 | 87.9 | **74.2** |

**Critical observation for the proposal:** Camera scores on RoboTwin 2.0-Plus are uniformly very low (21.6–45.6%), making camera the hardest axis on this benchmark. Even the best model (LingBot-VA) only scores 28.9% on camera — far below its 92.1% on the clean original. This strongly validates the research gap.

---

## TASK 2: LIBERO-Plus Evaluation Infrastructure

### Is LIBERO-Plus Publicly Available?
**Yes, fully publicly available.** The official repository is at `github.com/sylvestf/LIBERO-plus` (maintained by Sylvest/OpenMOSS). Key details:

- **Installation**: Drop-in replacement for the original LIBERO repo ("Simply replace the originally installed LIBERO repository with our repository without modifying your code").
- **Dataset**: Available at `huggingface.co/datasets/Sylvest/LIBERO-plus` — 10,030 tasks spanning seven perturbation dimensions, 20,000+ successful trajectories.
- **Evaluation code**: Available in `benchmark_scripts/`, `libero/`, `scripts/` subdirectories.
- **Configuration change needed**: Set `num_trials_per_task` from 50 to 1.
- **Paper**: arXiv 2510.13626 (October 2025).

### Camera Viewpoint Perturbation Specifics (Fully Defined in 2510.13626)
LIBERO-Plus defines three camera sub-axes:
- **C1 (Distance)**: Camera moved along its optical axis; distances range from 1.01× to 2.00× the original value.
- **C2 (Spherical Position)**: Camera position perturbed on a sphere centered at scene, altering azimuth (Δθ) and elevation (Δϕ) within **15°–75° cones**.
- **C3 (Orientation)**: Camera position fixed, orientation (yaw, pitch, roll) perturbed within **2° to 10°**.

### Are Motus Baseline Scores Available on LIBERO-Plus?
**No.** The Motus paper (arXiv 2512.13030) evaluates only on standard RoboTwin 2.0 and LIBERO-Long (language-conditioned). It does NOT report LIBERO-Plus scores. Motus does not appear on the LIBERO-Plus leaderboard in the paper or project page. Similarly, MotuBrain evaluates on standard RoboTwin 2.0 and WorldArena, not LIBERO-Plus.

---

## TASK 3: Being-H0.7 Camera Score Details

### Paper: arXiv 2605.00078
**Title:** "Being-H0.7: A Latent World-Action Model from Egocentric Videos"
**Authors:** Hao Luo, Wanpeng Zhang, Yicheng Feng, Sipeng Zheng, et al.

### Does Being-H0.7 Report Camera-Specific LIBERO-Plus Scores?
**No.** The paper reports only aggregate LIBERO-Plus scores:
- **Being-H0.7 (zero-shot)**: 82.1%
- **Being-H0.7 (fine-tuned on LIBERO-Plus)**: 84.8%
- **Being-H0.5**: 78.5% (zero-shot), 83.1% (fine-tuned)

**No per-axis breakdown (camera, background, layout, etc.) is published.** The paper does not disaggregate camera performance from the aggregate score.

### What Is the "Resilience Against Shifted Viewpoints" Claim Based On?
The paper states: "When evaluating robustness under environmental perturbations on LIBERO-plus, Being-H0.7 secures a 82.1% zero-shot success rate, which further improves to 84.8% after fine-tuning on LIBERO-plus, highlighting its **resilience against shifted viewpoints, novel textures, and sensor noise**."

This is a **qualitative, umbrella claim** — it does not cite a specific camera-axis score. The claim is inferred from the aggregate score, not from disaggregated camera data.

### Comparison Context
From the 2603.22078 Table 4, the aggregate LIBERO-Plus SOTA at the time of writing was π0.5 at 85.7% and Cosmos-Policy at 82.2%. Being-H0.7's 82.1% is roughly tied with Cosmos-Policy on aggregate, but OA-WAM (83.9% overall, per its own paper) is now ahead. Note that Being-H0.7 does NOT appear in the 2603.22078 comparison table.

---

## TASK 4: OA-WAM Camera Score Verification

### Paper: arXiv 2605.06481
**Title:** "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation"
**Authors:** Yushan Liu, Peibo Sun, Shoujie Li, et al.

### Is the 80.5% Camera Score Confirmed?
**Yes, confirmed.** From Table 2 (OA-WAM paper):

| Method | **Camera** | Robot Init | Layout | Geo Avg | Light | Background | Language | Sensor Noise | Overall Avg |
|---|---|---|---|---|---|---|---|---|---|
| **OA-WAM** | **80.5** | 89.6 | 82.8 | **84.3** | 96.5 | 95.9 | 85.3 | 75.6 | **83.9** |
| π0.5 | 75.4 | 77.5 | 85.7 | 79.5 | 96.9 | 94.6 | 85.6 | 89.7 | 85.7 |
| Cosmos-Policy | 75.8 | 63.3 | 82.2 | 73.8 | 96.5 | 88.9 | 81.7 | 92.7 | 82.2 |

The paper explicitly states: "**Camera 80.5 (+4.7 over Cosmos-Policy)**" as the primary geometric-axis improvement claim.

### Is 80.5% SOTA for Camera Axis on LIBERO-Plus?
**Yes, as of the OA-WAM paper (May 2026), 80.5% is SOTA on the camera axis.** Cross-referencing with the 2603.22078 Table 4, the best camera score among all models in that paper was π0.5 at 75.4% (their rerun of π0 gets 61.0%). OA-WAM's 80.5% exceeds this by 5.1 points. No other paper in this literature search reports a higher camera-axis score on LIBERO-Plus.

**Important caveat**: AnyCamVLA (2603.05868) achieves very high camera robustness (94.5% average on its own LIBERO-based viewpoint benchmark), but it does **not evaluate on LIBERO-Plus specifically** — it uses a custom viewpoint dataset. So AnyCamVLA cannot directly be compared as a competitor for LIBERO-Plus camera SOTA.

---

## TASK 5: Latest Related Work (May 2026)

### Papers Directly Targeting the Same Gap

**1. OA-WAM (arXiv 2605.06481, May 2026)** — The most direct concurrent/competing work. Addresses camera robustness through object-slot decomposition. SOTA on camera axis at 80.5%.

**2. AnyCamVLA (arXiv 2603.05868, March 2026)** — Zero-shot camera adaptation via feed-forward novel view synthesis, plug-and-play on any VLA. Does not require retraining. Uses custom LIBERO viewpoint augmentation, not LIBERO-Plus. Achieves 94.5% on its own protocol, degrading minimally under large perturbations (15 cm / 60° rotation). **This is a strong related-work competitor.**

**3. Mask World Model (arXiv 2604.19683, April 2026)** — Addresses nuisance variation (texture, lighting, background) through structured prediction. Targets overlapping robustness concerns.

**4. ReViWo (ICLR 2025)** — "Learning View-invariant World Models for Visual Robotic Manipulation." Learns view-invariant representations via autoencoder on multi-view simulator data. Uses Meta-World/PandaGym, not LIBERO-Plus. Published January 2025.

**5. Unified 4D World Action Modeling / X-WAM (arXiv 2604.26694, April 2026)** — 4D spatial reasoning approach.

### VQ-Based World Model Work
The "Beyond Short-Horizon: VQ-Memory for Robust Long-Horizon Manipulation" paper (arXiv 2603.09513) uses VQ-VAE to encode joint-state sequences as discrete tokens, but targets long-horizon non-Markovian tasks, not camera robustness. The XR-1 model also uses dual-branch VQ-VAE (UVMC) but for co-pretraining from human/robot data — not specifically camera robustness.

### No Directly Competing Paper Found for the Exact Proposal Gap
No paper found in May 2026 specifically proposes a **VQ-based world model architecture targeting camera viewpoint invariance on both LIBERO-Plus and RoboTwin 2.0-Plus** simultaneously. AnyCamVLA is the closest in spirit but approaches the problem differently (test-time view synthesis rather than training-time world model representation).

---

## Summary Answers to the Four Key Questions

**1. Is RoboTwin 2.0-Plus evaluation code publicly available?**
No. It is an in-house Huawei benchmark (introduced in 2603.22078). No code, repository, or perturbation parameter specification has been released. The standard RoboTwin 2.0 repo is public, but the 2.0-Plus perturbation protocol is not. To reproduce: you would need to implement camera perturbation on the standard simulator using reasonable parameters (e.g., adapting LIBERO-Plus's C1/C2/C3 specs). Authors would need to be contacted or the protocol inferred.

**2. Is LIBERO-Plus publicly available with full evaluation scripts?**
Yes. Fully public at `github.com/sylvestf/LIBERO-plus`, with dataset at `huggingface.co/datasets/Sylvest/LIBERO-plus`. Drop-in replacement for LIBERO. Camera perturbation covers three sub-axes: distance (1.01×–2.00×), spherical position (15°–75°), and orientation (2°–10°).

**3. Does Being-H0.7 report camera-specific LIBERO-Plus scores or only aggregate?**
Only aggregate (82.1% zero-shot, 84.8% fine-tuned). No per-axis breakdown is published. The "resilience against shifted viewpoints" claim is an umbrella inference from the aggregate score, not from a disaggregated camera-axis number.

**4. Is OA-WAM 80.5% confirmed as SOTA for camera axis on LIBERO-Plus?**
Yes, confirmed from OA-WAM Table 2 (2605.06481). It is the highest published camera-axis score on LIBERO-Plus as of May 2026, beating π0.5 (75.4%) by 5.1 points and Cosmos-Policy (75.8%) by 4.7 points. The paper itself claims this as a new SOTA on the geometric axes. Note that the aggregate score leader is π0.5 at 85.7%, so OA-WAM leads on camera but not overall.

---

Sources:
- [Do World Action Models Generalize Better than VLAs? A Robustness Study (arXiv 2603.22078)](https://arxiv.org/abs/2603.22078)
- [arXiv 2603.22078 HTML full paper](https://arxiv.org/html/2603.22078v1)
- [OA-WAM: Object-Addressable World Action Model (arXiv 2605.06481)](https://arxiv.org/html/2605.06481v1)
- [Being-H0.7 (arXiv 2605.00078)](https://arxiv.org/abs/2605.00078)
- [LIBERO-Plus: In-depth Robustness Analysis (arXiv 2510.13626)](https://arxiv.org/abs/2510.13626)
- [LIBERO-Plus HTML full paper](https://arxiv.org/html/2510.13626v1)
- [LIBERO-Plus GitHub Repository](https://github.com/sylvestf/LIBERO-plus)
- [LIBERO-Plus Project Page](https://sylvestf.github.io/LIBERO-plus/)
- [LIBERO-Plus Dataset (Hugging Face)](https://huggingface.co/datasets/Sylvest/LIBERO-plus)
- [RoboTwin-Platform/RoboTwin GitHub](https://github.com/RoboTwin-Platform/RoboTwin)
- [RoboTwin 2.0 Official Site](https://robotwin-platform.github.io/)
- [LingBot-VA GitHub (RSS 2026)](https://github.com/Robbyant/lingbot-va)
- [Motus: A Unified Latent Action World Model (arXiv 2512.13030)](https://arxiv.org/abs/2512.13030)
- [MotuBrain: An Advanced World Action Model (arXiv 2604.27792)](https://arxiv.org/html/2604.27792v2)
- [AnyCamVLA: Zero-Shot Camera Adaptation (arXiv 2603.05868)](https://arxiv.org/abs/2603.05868)
- [ReViWo: Learning View-invariant World Models (OpenReview ICLR 2025)](https://openreview.net/forum?id=vJwjWyt4Ed)
- [RoboTwin 2.0 Paper (arXiv 2506.18088)](https://arxiv.org/abs/2506.18088)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f867e7ca-cf5d-4694-90d7-0131754ffed0",
  "isSidechain": true,
  "agentId": "a3e0967fbcc983b14",
  "requestId": "req_011CatbyHST8akL9533hix2Y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a157747-c773-469c-90b4-650297c38dcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5420dce1-b02f-4ba9-b309-0202465ea281",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AyfWaqMkr1nr8nsAcUeVLy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 185,
      "cache_creation_input_tokens": 1275,
      "cache_read_input_tokens": 38012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1275,
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
