# Research conversation: I need to verify several claims for a research proposal review. Please use WebSearch to find: 1. "AGILE" NVIDIA humanoid

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-af1d5343193f8d545.jsonl`
- **Structured JSON:** [`1c18c528150015f607cd.json`](../../sessions/1c/1c18c528150015f607cd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-10T19:20:58.387Z_

I need to verify several claims for a research proposal review. Please use WebSearch to find:

1. "AGILE" NVIDIA humanoid loco-manipulation Isaac Lab 2026 - verify this paper/framework exists (arXiv:2603.20147)
2. "Humanoids 2026" conference deadline - verify the paper deadline (claimed June 30, 2026)
3. "CoRL 2026" Austin deadline - verify abstract deadline May 26 and paper deadline May 29, 2026
4. "GR00T-WBC" OR "SONIC" NVIDIA humanoid locomotion checkpoint - verify pre-trained locomotion checkpoints exist
5. "LHM-Humanoid" arXiv:2508.16943 - verify this paper exists

Report what you find for each query.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "af1d5343193f8d545",
  "type": "user",
  "uuid": "38eb1006-63a1-44d8-b6c3-d1a3872e3124",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T19:20:59.269Z_

I'll search for each of these claims systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38eb1006-63a1-44d8-b6c3-d1a3872e3124",
  "isSidechain": true,
  "agentId": "af1d5343193f8d545",
  "requestId": "req_011CauRw6VfkMKRSZzn9AzZ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6458a11c-667d-4b34-bb8d-f5f0d778483c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018crpcF85uFanUb93FvyyyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 609,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T19:20:59.488Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019PySwRPiGr5LmCuQBXyTtU`</summary>

```json
{
  "query": "AGILE NVIDIA humanoid loco-manipulation Isaac Lab arXiv:2603.20147"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6458a11c-667d-4b34-bb8d-f5f0d778483c",
  "isSidechain": true,
  "agentId": "af1d5343193f8d545",
  "requestId": "req_011CauRw6VfkMKRSZzn9AzZ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5fadbd17-e8a2-4e07-9aa0-3aea8167ec29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018crpcF85uFanUb93FvyyyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 609,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T19:20:59.699Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NSTsJFoTWhrqW7d7WUyhBX`</summary>

```json
{
  "query": "Humanoids 2026 conference paper deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fadbd17-e8a2-4e07-9aa0-3aea8167ec29",
  "isSidechain": true,
  "agentId": "af1d5343193f8d545",
  "requestId": "req_011CauRw6VfkMKRSZzn9AzZ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a830a099-d959-4702-b3bf-cb7e89a21f07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018crpcF85uFanUb93FvyyyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 609,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T19:20:59.922Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fko3fcLzu5p5sUANUmTMkS`</summary>

```json
{
  "query": "CoRL 2026 Austin deadline abstract May 26 paper May 29"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a830a099-d959-4702-b3bf-cb7e89a21f07",
  "isSidechain": true,
  "agentId": "af1d5343193f8d545",
  "requestId": "req_011CauRw6VfkMKRSZzn9AzZ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "13231993-b5eb-400c-a561-368dc54d9278",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018crpcF85uFanUb93FvyyyQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 609,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T19:21:00.151Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015xgxPUb8bjVkMkwsxxzDHo`</summary>

```json
{
  "query": "GR00T-WBC SONIC NVIDIA humanoid locomotion checkpoint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13231993-b5eb-400c-a561-368dc54d9278",
  "isSidechain": true,
  "agentId": "af1d5343193f8d545",
  "requestId": "req_011CauRw6VfkMKRSZzn9AzZ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c862172a-0b5d-4658-8cce-ab1abbd934bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018crpcF85uFanUb93FvyyyQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 13649,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 609
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 280,
          "cache_read_input_tokens": 13649,
          "cache_creation_input_tokens": 609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 609,
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

_source line 7 · 2026-05-10T19:21:00.155Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T2vkjuYEnmkqUT2j2bFL5X`</summary>

```json
{
  "query": "LHM-Humanoid arXiv:2508.16943"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c862172a-0b5d-4658-8cce-ab1abbd934bb",
  "isSidechain": true,
  "agentId": "af1d5343193f8d545",
  "requestId": "req_011CauRw6VfkMKRSZzn9AzZ3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "62e72dac-2a60-41d4-b660-dced95e02b01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018crpcF85uFanUb93FvyyyQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 13649,
      "output_tokens": 280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 609
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 280,
          "cache_read_input_tokens": 13649,
          "cache_creation_input_tokens": 609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 609,
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

_source line 8 · 2026-05-10T19:21:04.250Z_

<details><summary>↩ Tool result · `toolu_01Fko3fcLzu5p5sUANUmTMkS`</summary>

```text
Web search results for query: "CoRL 2026 Austin deadline abstract May 26 paper May 29"

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"}]

Based on the search results, here's what I found about CoRL 2026 Austin deadlines:

CoRL 2026 will be held at the JW Marriott Austin in Austin, Texas from November 9-12, 2026, with an abstract submission deadline of May 26, 2026 11:59 UTC and a paper submission deadline of May 29, 2026 11:59 UTC.

The conference details confirm that:
- CoRL 2026 will be held in Austin, Texas, US
- Workshops are on November 9, and the main conference runs November 10-12
- The paper submission deadline is May 29, 2026

Papers can be submitted through OpenReview via the link at https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13231993-b5eb-400c-a561-368dc54d9278",
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "af1d5343193f8d545",
  "type": "user",
  "uuid": "c33351f9-07b1-476a-9536-70206ac43075",
  "sourceToolAssistantUUID": "13231993-b5eb-400c-a561-368dc54d9278",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T19:21:04.693Z_

<details><summary>↩ Tool result · `toolu_01NSTsJFoTWhrqW7d7WUyhBX`</summary>

```text
Web search results for query: "Humanoids 2026 conference paper deadline"

Links: [{"title":"Humanoids 2026 - 2026 IEEE-RAS 25th International Conference on Humanoid Robots (Humanoids)","url":"https://2026.ieee-humanoids.org/"},{"title":"Humanoids: IEEE-RAS International Conference on Humanoid Robots 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1239"},{"title":"humanoids Archives - IEEE Robotics and Automation Society Website","url":"http://www.ieee-ras.org/conferences-workshops/fully-sponsored/humanoids"},{"title":"Humanoids 2026","url":"http://www.humanoids.global/"},{"title":"Humanoids 2026 - 2026 IEEE-RAS 25th International Conference on Humanoid Robots (Humanoids) - Workshops - Humanoid Hub","url":"https://www.humanoidhub.ai/workshops/humanoids-2026-2026-ieee-ras-25th-international-conference-on-humanoid-robots-humanoids-000000"},{"title":"IEEE-RAS International Conference on Humanoid Robots (Humanoids 2026), 01 Sep - 31 Dec, 2026 | Conference Locate (Clocate)","url":"https://www.clocate.com/ieee-ras-international-conference-on-humanoid-robots-humanoids/15664/"},{"title":"25th IEEE-RAS International Conference on Humanoid Robotics — StartupEvents.org","url":"https://startupevents.org/startup-events-calendar/25th-ieee-ras-international-conference-on-humanoid-robotics"},{"title":"Humanoid Robots Conferences 2026/2027/2028 - Conference Index","url":"https://conferenceindex.org/conferences/humanoid-robots"},{"title":"Humanoids Summit","url":"https://humanoidssummit.com/"},{"title":"IEEE-RAS Humanoids 2026 (San Jose CA) - IEEE-RAS 25th International Conference on Humanoid Robots (Humanoids) -- showsbee.com","url":"https://www.showsbee.com/fairs/IEEE-Humanoids.html"}]

Based on the search results, I found information about the Humanoids 2026 conference, but the specific paper submission deadline was not clearly stated in these results. The 2026 IEEE-RAS 25th International Conference on Humanoid Robots will take place December 6–9, 2026 in Santa Clara, CA, USA, and the search results mention a "Submit Paper" option on the official website.

To get the exact paper deadline, I recommend visiting the official Humanoids 2026 website at https://2026.ieee-humanoids.org/, which appears to have the paper submission details. The website should have a "Call for Papers" or submissions section with the specific deadline information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a830a099-d959-4702-b3bf-cb7e89a21f07",
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "af1d5343193f8d545",
  "type": "user",
  "uuid": "6821f3b2-0daf-40af-8a47-278350af5eec",
  "sourceToolAssistantUUID": "a830a099-d959-4702-b3bf-cb7e89a21f07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T19:21:07.119Z_

<details><summary>↩ Tool result · `toolu_01T2vkjuYEnmkqUT2j2bFL5X`</summary>

```text
Web search results for query: "LHM-Humanoid arXiv:2508.16943"

Links: [{"title":"[2508.16943] LHM-Humanoid: Learning a Unified Policy for Long-Horizon Humanoid Whole-Body Loco-Manipulation in Diverse Messy Environments","url":"https://arxiv.org/abs/2508.16943"},{"title":"LHM-Humanoid: Learning a Unified Policy for Long-Horizon Humanoid Whole-Body Loco-Manipulation in Diverse Messy Environments","url":"https://arxiv.org/html/2508.16943"},{"title":"HUMANOIDVERSE: A VERSATILE HUMANOID FOR","url":"https://arxiv.org/pdf/2508.16943"},{"title":"HumanoidVerse: A Versatile Humanoid for Vision-Language Guided Multi-Object Rearrangement","url":"https://haozhuo-zhang.github.io/HumanoidVerse-project-page/"},{"title":"HumanoidVerse: A Versatile Humanoid for Vision-Language Guided Multi-Object Rearrangement","url":"https://arxiv.org/html/2508.16943v1"},{"title":"LHM: Large Animatable Human Reconstruction Model ...","url":"https://lingtengqiu.github.io/LHM/"},{"title":"Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation","url":"https://arxiv.org/html/2403.04436v1"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"[2508.08258] Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics","url":"https://arxiv.org/abs/2508.08258"},{"title":"Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics","url":"https://arxiv.org/html/2508.08258"}]

Based on the search results, here's what I found about the arXiv paper 2508.16943:

LHM-Humanoid is a benchmark and learning framework for long-horizon whole-body humanoid loco-manipulation in diverse, cluttered scenes.

In this task, a humanoid agent must repeatedly (i) walk to a target, (ii) pick it up with diverse whole-body postures under balance constraints, (iii) carry it while navigating around obstacles, and (iv) place it at a designated goal -- all within a single continuous episode and without any environment reset.

**Dataset and Training Approach:**
The dataset spans four room types (bedroom, living room, kitchen, and warehouse), comprising 350 diverse scenes/tasks with 79 objects (25 movable targets). The researchers learn goal-conditioned teacher policies via reinforcement learning and distill them into a single end-to-end student policy using DAgger, then further distill this unified policy into a vision-language-action (VLA) model driven by egocentric RGB observations and natural language.

**Results:**
Experiments in Isaac Gym demonstrate that LHM-Humanoid substantially outperforms end-to-end RL baselines and prior humanoid loco-manipulation methods on both seen and unseen scenes, exhibiting strong long-horizon robustness and cross-scene generalization.

The paper was authored by Haozhuo Zhang and 6 other researchers and was last revised on March 5, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62e72dac-2a60-41d4-b660-dced95e02b01",
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "af1d5343193f8d545",
  "type": "user",
  "uuid": "23dc229a-6ac3-4350-8ee7-a268faabb61d",
  "sourceToolAssistantUUID": "62e72dac-2a60-41d4-b660-dced95e02b01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T19:21:07.401Z_

<details><summary>↩ Tool result · `toolu_019PySwRPiGr5LmCuQBXyTtU`</summary>

```text
Web search results for query: "AGILE NVIDIA humanoid loco-manipulation Isaac Lab arXiv:2603.20147"

Links: [{"title":"AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning","url":"https://arxiv.org/html/2603.20147v1"},{"title":"HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos","url":"https://arxiv.org/html/2602.02473v1"},{"title":"Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning","url":"https://arxiv.org/html/2511.04831v1"},{"title":"Building Generalist Humanoid Capabilities with NVIDIA Isaac GR00T N1.6 Using a Sim-to-Real Workflow | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/building-generalist-humanoid-capabilities-with-nvidia-isaac-gr00t-n1-6-using-a-sim-to-real-workflow/"},{"title":"Streamline Robot Learning with Whole-Body Control and Enhanced Teleoperation in NVIDIA Isaac Lab 2.3 | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/streamline-robot-learning-with-whole-body-control-and-enhanced-teleoperation-in-nvidia-isaac-lab-2-3/"},{"title":"[2501.02902] Sim-to-Real Transfer for Mobile Robots with Reinforcement Learning: from NVIDIA Isaac Sim to Gazebo and Real ROS 2 Robots","url":"https://arxiv.org/abs/2501.02902"},{"title":"NVIDIA Isaac Lab Open-Source Modular Framework","url":"https://developer.nvidia.com/isaac/lab"},{"title":"2025-9-28 Isaac Lab: A GPU-Accelerated Simulation Framework for","url":"https://d1qx31qr3h6wln.cloudfront.net/publications/Isaac%20Lab,%20A%20GPU-Accelerated%20Simulation%20Framework%20for%20Multi-Modal%20Robot%20Learning.pdf"},{"title":"Redirecting to the latest Isaac Lab documentation","url":"https://isaac-sim.github.io/IsaacLab/"},{"title":"X-Loco: Towards Generalist Humanoid Locomotion Control via Synergetic Policy Distillation","url":"https://arxiv.org/html/2603.03733"}]

Based on the search results, I found detailed information about the paper you're asking about:

## AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning

AGILE (A Generic Isaac-Lab based Engine) is an open-source workflow built on Isaac Lab and RSL-RL that covers the full path from a new robot to a deployed policy.

### Key Problem and Solution

Recent advances in reinforcement learning have enabled impressive humanoid behaviors in simulation, yet transferring these results to new robots remains challenging. In many real deployments, the primary bottleneck is no longer simulation throughput or algorithm design, but the absence of systematic infrastructure that links environment verification, training, evaluation, and deployment in a coherent loop.

### Four-Stage Pipeline

AGILE comprises four stages: (1) interactive environment verification, (2) reproducible training, (3) unified evaluation, and (4) descriptor-driven deployment via robot/task configuration descriptors.

The workflow includes:
- Interactive debug GUIs (for joint control, object manipulation, and reward visualization) allow researchers to catch robot model and MDP misconfigurations in minutes before committing GPU hours.
- A scalable, reproducible training environment featuring automated hyperparameter sweeps, experiment tracking, and a suite of independently toggleable algorithmic enhancements.
- A unified evaluation pipeline combining deterministic scenario-based tests and stochastic rollouts. Parallel environments receive scripted or randomized commands to evaluate deployment-critical motion metrics such as joint jerk and limit violations.

The paper was published on March 20, 2026 (arXiv:2603.20147v1).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fadbd17-e8a2-4e07-9aa0-3aea8167ec29",
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "af1d5343193f8d545",
  "type": "user",
  "uuid": "9a8626ee-3206-4b7f-a855-8221de1f0c92",
  "sourceToolAssistantUUID": "5fadbd17-e8a2-4e07-9aa0-3aea8167ec29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T19:21:07.574Z_

<details><summary>↩ Tool result · `toolu_015xgxPUb8bjVkMkwsxxzDHo`</summary>

```text
Web search results for query: "GR00T-WBC SONIC NVIDIA humanoid locomotion checkpoint"

Links: [{"title":"GitHub - NVlabs/GR00T-WholeBodyControl: Welcome to GR00T Whole-Body Control (WBC)! This is a unified platform for developing and deploying advanced humanoid controllers. This includes: Decoupled WBC models used in NVIDIA Isaac-Gr00t, Gr00t N1.5 and N1.6 and GEAR-SONIC · GitHub","url":"https://github.com/NVlabs/GR00T-WholeBodyControl"},{"title":"GR00T-WholeBodyControl/README.md at main · NVlabs/GR00T-WholeBodyControl","url":"https://github.com/NVlabs/GR00T-WholeBodyControl/blob/main/README.md"},{"title":"GR00T-WholeBodyControl Documentation — GR00T-WholeBodyControl Documentation","url":"https://nvlabs.github.io/GR00T-WholeBodyControl/"},{"title":"GR00T-WholeBodyControl/motionbricks at main · NVlabs/GR00T-WholeBodyControl","url":"https://github.com/NVlabs/GR00T-WholeBodyControl/tree/main/motionbricks"},{"title":"GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub","url":"https://github.com/NVIDIA/Isaac-GR00T"},{"title":"NVlabs/GR00T-WholeBodyControl | DeepWiki","url":"https://deepwiki.com/NVlabs/GR00T-WholeBodyControl"},{"title":"nvidia/GEAR-SONIC · Hugging Face","url":"https://huggingface.co/nvidia/GEAR-SONIC"},{"title":"Control Paradigms | NVlabs/GR00T-WholeBodyControl | DeepWiki","url":"https://deepwiki.com/NVlabs/GR00T-WholeBodyControl/1.2-key-features"},{"title":"Advancing Humanoid Robot Sight and Skill Development with NVIDIA Project GR00T | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/advancing-humanoid-robot-sight-and-skill-development-with-nvidia-project-gr00t/"},{"title":"GR00T-WholeBodyControl/gear_sonic at main · NVlabs/GR00T-WholeBodyControl","url":"https://github.com/NVlabs/GR00T-WholeBodyControl/tree/main/gear_sonic"}]

Based on the search results, here's what I found about GR00T-WBC, SONIC, and NVIDIA's humanoid locomotion checkpoint:

## Overview

GR00T Whole-Body Control (WBC) is the codebase for humanoid robot controller projects that hosts model checkpoints and scripts for training, evaluating, and deploying advanced whole-body controllers.

## SONIC - Humanoid Behavior Foundation Model

SONIC is a humanoid behavior foundation model that gives robots a core set of motor skills learned from large-scale human motion data. Rather than building separate controllers for predefined motions, SONIC uses motion tracking as a scalable training task, enabling a single unified policy to produce natural, whole-body movement and support a wide range of behaviors — from walking and crawling to teleoperation and multi-modal control.

## Locomotion Capabilities

SONIC includes a kinematic planner for real-time locomotion generation — choose a movement style, steer with keyboard/gamepad, and adjust speed and height on the fly. Key features include natural whole-body locomotion (walking, crawling, dynamic movements), real-time VR teleoperation support, and a ready-to-deploy C++ inference stack.

## Training and Checkpoints

SONIC can be trained from scratch on the Bones-SEED motion capture dataset (142K+ motions, ~288 hours, Unitree G1 retargeted), or finetuned from the released checkpoint on Hugging Face. GEAR-SONIC with pretrained checkpoints, C++ inference, VR teleoperation, and documentation were released on 2026-02-19.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c862172a-0b5d-4658-8cce-ab1abbd934bb",
  "isSidechain": true,
  "promptId": "9b9ebae5-ea89-443c-82ad-9f786b68d79f",
  "agentId": "af1d5343193f8d545",
  "type": "user",
  "uuid": "0482abd9-e1cd-4b46-bc90-c7272d066e28",
  "sourceToolAssistantUUID": "c862172a-0b5d-4658-8cce-ab1abbd934bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T19:21:16.821Z_

## Research Proposal Verification Report

Here's what I found for each of your claims:

### 1. AGILE NVIDIA Humanoid Loco-Manipulation (arXiv:2603.20147)
**VERIFIED** - The paper exists and is confirmed. "AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning" is a real paper published March 20, 2026. It's an open-source workflow built on Isaac Lab and RSL-RL that provides a four-stage pipeline for humanoid learning: interactive environment verification, reproducible training, unified evaluation, and descriptor-driven deployment.

### 2. Humanoids 2026 Conference Deadline (June 30, 2026)
**PARTIALLY VERIFIED** - The conference exists (IEEE-RAS 25th International Conference on Humanoid Robots, December 6-9, 2026 in Santa Clara, CA). However, the search results do not explicitly confirm the June 30, 2026 paper deadline. The official conference website at https://2026.ieee-humanoids.org/ should have the exact deadline, but it wasn't displayed in the search results.

### 3. CoRL 2026 Austin Deadlines
**VERIFIED** - The deadlines are confirmed as accurate:
- Abstract submission deadline: May 26, 2026 11:59 UTC
- Paper submission deadline: May 29, 2026 11:59 UTC
- Conference location: JW Marriott Austin, November 9-12, 2026
- Papers submitted via OpenReview

### 4. GR00T-WBC and SONIC Pre-trained Locomotion Checkpoints
**VERIFIED** - Both systems exist with pre-trained checkpoints:
- **GR00T Whole-Body Control (WBC)** is a unified platform for humanoid controllers hosted on GitHub (NVlabs/GR00T-WholeBodyControl)
- **SONIC** is a humanoid behavior foundation model trained on the Bones-SEED motion capture dataset (142K+ motions, 288+ hours)
- **GEAR-SONIC** with pre-trained checkpoints was released February 19, 2026 and is available on Hugging Face
- Both support locomotion, whole-body control, and real-time deployment

### 5. LHM-Humanoid (arXiv:2508.16943)
**VERIFIED** - The paper exists. "LHM-Humanoid: Learning a Unified Policy for Long-Horizon Humanoid Whole-Body Loco-Manipulation in Diverse Messy Environments" is a real paper last revised March 5, 2026. It presents a framework for learning unified policies for humanoid loco-manipulation across diverse cluttered scenes using RL teacher policies, DAgger distillation, and vision-language-action models.

---

**Summary**: 4 of 5 claims fully verified, and 1 partially verified (Humanoids 2026 deadline exists but specific June 30 date not confirmed in search results).

Sources:
- [AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning](https://arxiv.org/html/2603.20147v1)
- [Humanoids 2026 Conference](https://2026.ieee-humanoids.org/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [GR00T-WholeBodyControl GitHub](https://github.com/NVlabs/GR00T-WholeBodyControl)
- [GEAR-SONIC on Hugging Face](https://huggingface.co/nvidia/GEAR-SONIC)
- [LHM-Humanoid arXiv:2508.16943](https://arxiv.org/abs/2508.16943)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0482abd9-e1cd-4b46-bc90-c7272d066e28",
  "isSidechain": true,
  "agentId": "af1d5343193f8d545",
  "requestId": "req_011CauRwmka6hviQMR34Eyqo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1aada603-c4d1-44e7-befb-303036b70614",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c9f1e88d-7547-445a-bdb2-8a60925de079",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BW8D2ZiNqz93db2ZpnT9dF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 908,
      "cache_creation_input_tokens": 4607,
      "cache_read_input_tokens": 14258,
      "output_tokens": 908,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4607
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 908,
          "output_tokens": 908,
          "cache_read_input_tokens": 14258,
          "cache_creation_input_tokens": 4607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4607,
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
