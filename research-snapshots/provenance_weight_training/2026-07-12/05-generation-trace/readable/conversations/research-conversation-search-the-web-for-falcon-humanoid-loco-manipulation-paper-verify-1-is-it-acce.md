# Research conversation: Search the web for "FALCON humanoid loco-manipulation" paper. Verify: 1. Is it accepted at L4DC 2026? Check arXiv:2505.0

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a9f8b9a30cdd6a6c3.jsonl`
- **Structured JSON:** [`ff262cd0f1aeaaa60c8c.json`](../../sessions/ff/ff262cd0f1aeaaa60c8c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

9 recorded events

### User

_source line 1 · 2026-05-10T21:01:02.692Z_

Search the web for "FALCON humanoid loco-manipulation" paper. Verify:
1. Is it accepted at L4DC 2026? Check arXiv:2505.06776
2. Does it decompose humanoid control into upper-body and lower-body agents?
3. Does it use a force curriculum?
4. What performance claims does it make (2x tracking improvement)?

Use WebSearch with queries like:
- "FALCON force-adaptive humanoid loco-manipulation arXiv 2505.06776"
- "site:arxiv.org 2505.06776"
- "L4DC 2026 humanoid decomposition"

Then use WebFetch to read the actual arXiv page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f556c21e-91fd-4757-bdee-1c7a3129ceaa",
  "agentId": "a9f8b9a30cdd6a6c3",
  "type": "user",
  "uuid": "90a94cf4-0cf4-423a-8ce9-f50a9b8ce1e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7111d5a1-92b4-4478-a35b-6fcf6ac9e788",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T21:01:04.068Z_

I'll search for information about the FALCON humanoid loco-manipulation paper and verify the details you mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90a94cf4-0cf4-423a-8ce9-f50a9b8ce1e9",
  "isSidechain": true,
  "agentId": "a9f8b9a30cdd6a6c3",
  "requestId": "req_011CauZZhZ8CPuruUq4i5TGD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dd9f28f5-f875-4f40-a3c3-049d7c668cb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7111d5a1-92b4-4478-a35b-6fcf6ac9e788",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SW6XszMYnE5y8MbeqHdrxB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 588,
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

_source line 3 · 2026-05-10T21:01:04.312Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AhGJ5pRM56fB8j1pWUHs5R`</summary>

```json
{
  "query": "FALCON force-adaptive humanoid loco-manipulation arXiv 2505.06776"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd9f28f5-f875-4f40-a3c3-049d7c668cb8",
  "isSidechain": true,
  "agentId": "a9f8b9a30cdd6a6c3",
  "requestId": "req_011CauZZhZ8CPuruUq4i5TGD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "adb7c8b8-e408-415e-a8c6-f688e8eaaad7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7111d5a1-92b4-4478-a35b-6fcf6ac9e788",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SW6XszMYnE5y8MbeqHdrxB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 588,
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

_source line 4 · 2026-05-10T21:01:04.461Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H1fat3gid3bXkmHCeg33Ug`</summary>

```json
{
  "query": "L4DC 2026 humanoid decomposition control"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adb7c8b8-e408-415e-a8c6-f688e8eaaad7",
  "isSidechain": true,
  "agentId": "a9f8b9a30cdd6a6c3",
  "requestId": "req_011CauZZhZ8CPuruUq4i5TGD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fda74121-3ce7-4fbc-a61f-747bc4d8ebd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7111d5a1-92b4-4478-a35b-6fcf6ac9e788",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SW6XszMYnE5y8MbeqHdrxB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 13649,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 588,
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

_source line 5 · 2026-05-10T21:01:04.757Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ujj8P2PieNLjVGZpAyRH8N`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.06776",
  "prompt": "What is the main contribution of this paper? Does it decompose humanoid control? Does it use force curriculum? What are the performance improvements?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fda74121-3ce7-4fbc-a61f-747bc4d8ebd5",
  "isSidechain": true,
  "agentId": "a9f8b9a30cdd6a6c3",
  "requestId": "req_011CauZZhZ8CPuruUq4i5TGD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4c8ca0d1-ee25-4887-bebc-6bc75d088b86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7111d5a1-92b4-4478-a35b-6fcf6ac9e788",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SW6XszMYnE5y8MbeqHdrxB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 13649,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 588
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 235,
          "cache_read_input_tokens": 13649,
          "cache_creation_input_tokens": 588,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 588,
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

_source line 6 · 2026-05-10T21:01:09.248Z_

<details><summary>↩ Tool result · `toolu_01H1fat3gid3bXkmHCeg33Ug`</summary>

```text
Web search results for query: "L4DC 2026 humanoid decomposition control"

Links: [{"title":"L4DC 2026","url":"https://sites.google.com/usc.edu/l4dc2026/"},{"title":"L4DC 2026 | OpenReview","url":"https://openreview.net/group?id=L4DC.org/2026"},{"title":"L4DC Conference (@l4dc_conf) / Posts / X","url":"https://x.com/l4dc_conf"},{"title":"L4DC 2026 Conference | OpenReview","url":"https://openreview.net/group?id=L4DC.org/2026/Conference"},{"title":"GitHub - LeCAR-Lab/FALCON: [L4DC 2026] \"FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation\" · GitHub","url":"https://github.com/LeCAR-Lab/FALCON"},{"title":"L4DC 2026 : 8th Annual Learning for Dynamics & Control Conference","url":"http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=192003&copyownerid=13149"},{"title":"Learning for Dynamics & Control Conference (L4DC) 2026 - MATLAB & Simulink","url":"https://www.mathworks.com/company/events/tradeshows/l4dc-2026-5247000.html"},{"title":"Lars Lindemann on X: \"We’re excited to host the 8th Learning for Dynamics &amp; Control (L4DC) Conference at the University of Southern California from June 17–19, 2026 ☀️🌴 Consider submitting your latest research at the interface between learning, optimization, and control, see https://t.co/L5IF5Nrx0y https://t.co/DVpCnyeawC\" / X","url":"https://x.com/LarsLindemann2/status/1955130367218012334"},{"title":"L4DC 2026 - Author Information","url":"https://sites.google.com/usc.edu/l4dc2026/author-information"},{"title":"L4DC 2026 - Schedule","url":"https://sites.google.com/usc.edu/l4dc2026/program/schedule"}]

Based on the search results, here's what I found about L4DC 2026 and humanoid decomposition control:

The 8th Annual Learning for Dynamics & Control Conference (L4DC) will be held at the University of Southern California from June 17–19, 2026. The conference is open to any topic on the interface between machine learning, control, and optimization; its primary goal is to address scientific and application challenges in real-time processes modeled by dynamical or control systems.

Regarding humanoid decomposition control specifically, I found a relevant research project: A paper titled "FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation" was presented as an L4DC 2026 Oral presentation. This project appears to involve decomposed control approaches for humanoid robots, featuring decoupled locomotion and force control strategies based on the code repository structure.

The search results show that L4DC 2026 will feature a diverse program including tutorials and presentations on bridging control and learning for robotics and autonomous systems, which would encompass humanoid robot control research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fda74121-3ce7-4fbc-a61f-747bc4d8ebd5",
  "isSidechain": true,
  "promptId": "f556c21e-91fd-4757-bdee-1c7a3129ceaa",
  "agentId": "a9f8b9a30cdd6a6c3",
  "type": "user",
  "uuid": "cef17623-38c6-47dd-8d2b-887017c4aebd",
  "sourceToolAssistantUUID": "fda74121-3ce7-4fbc-a61f-747bc4d8ebd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7111d5a1-92b4-4478-a35b-6fcf6ac9e788",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-10T21:01:09.664Z_

<details><summary>↩ Tool result · `toolu_01Ujj8P2PieNLjVGZpAyRH8N`</summary>

```text
# FALCON: Key Contributions and Results

## Main Contribution
FALCON presents a dual-agent reinforcement learning framework designed to enable humanoid robots to perform forceful manipulation while maintaining stable locomotion. The system targets a significant gap in robotics: achieving precise whole-body control with 3D end-effector force interaction.

## Control Decomposition
Yes, the approach explicitly decomposes control into two specialized agents:
- **Lower-body agent**: Maintains stable locomotion despite external force disturbances
- **Upper-body agent**: Tracks end-effector positions while providing implicit adaptive force compensation

## Force Curriculum
Yes, training employs "a force curriculum that progressively escalates the magnitude of external force exerted on the end effector while respecting torque limits."

## Performance Improvements
The framework demonstrates substantial gains:
- **2x more accurate** upper-body joint tracking versus baseline methods
- **Robust locomotion** maintained under force disturbances
- **Faster training convergence**
- **Cross-robot generalization**: The same training setup produced policies deployable across multiple humanoid platforms

## Real-World Validation
FALCON successfully enabled forceful manipulation tasks including payload transport (0-20N), cart-pulling (0-100N), and door-opening (0-40N) in real-world settings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c8ca0d1-ee25-4887-bebc-6bc75d088b86",
  "isSidechain": true,
  "promptId": "f556c21e-91fd-4757-bdee-1c7a3129ceaa",
  "agentId": "a9f8b9a30cdd6a6c3",
  "type": "user",
  "uuid": "eaec83f2-dce0-430b-9d55-62b71f3ea2e0",
  "sourceToolAssistantUUID": "4c8ca0d1-ee25-4887-bebc-6bc75d088b86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7111d5a1-92b4-4478-a35b-6fcf6ac9e788",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T21:01:11.069Z_

<details><summary>↩ Tool result · `toolu_01AhGJ5pRM56fB8j1pWUHs5R`</summary>

```text
Web search results for query: "FALCON force-adaptive humanoid loco-manipulation arXiv 2505.06776"

Links: [{"title":"[2505.06776] FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation","url":"https://arxiv.org/abs/2505.06776"},{"title":"(PDF) FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation","url":"https://www.researchgate.net/publication/391675402_FALCON_Learning_Force-Adaptive_Humanoid_Loco-Manipulation"},{"title":"FALCON","url":"https://lecar-lab.github.io/falcon-humanoid/"},{"title":"FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2505.06776"},{"title":"GitHub - LeCAR-Lab/FALCON: [L4DC 2026] \"FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation\" · GitHub","url":"https://github.com/LeCAR-Lab/FALCON"},{"title":"Robust Visuomotor Control for Humanoid Loco-Manipulation Using Hybrid Reinforcement Learning - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12292580/"},{"title":"FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation","url":"https://www.emergentmind.com/papers/2505.06776"},{"title":"FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation","url":"https://lecar-lab.github.io/falcon-humanoid/static/falcon.pdf"},{"title":"Deep Reinforcement Learning for Real-World Humanoid Robot Locomotion Control with Automatic Reward Learning | Research","url":"https://spj.science.org/doi/10.34133/research.1123"},{"title":"CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation","url":"https://arxiv.org/html/2512.14689"}]

Based on the search results, here's what I found about FALCON:

## Overview

FALCON is a dual-agent reinforcement-learning-based framework for robust force-adaptive humanoid loco-manipulation that decomposes whole-body control into two specialized agents: a lower-body agent ensuring stable locomotion under external force disturbances, and an upper-body agent precisely tracking end-effector positions with implicit adaptive force compensation.

## Key Features

The two agents are jointly trained in simulation with a force curriculum that progressively escalates the magnitude of external force exerted on the end effector while respecting torque limits.

## Performance

FALCON achieves 2x more accurate upper-body joint tracking compared to baselines, while maintaining robust locomotion under force disturbances and achieving faster training convergence. Additionally, FALCON enables policy training without embodiment-specific reward or curriculum tuning.

## Real-World Applications

Using the same training setup, policies are deployed across multiple humanoids, enabling forceful loco-manipulation tasks such as transporting payloads (0-20N force), cart-pulling (0-100N), and door-opening (0-40N) in the real world.

The paper was submitted on May 10, 2025, with a revised version on November 16, 2025. You can access the full paper, code, and project details at the official project page and GitHub repository linked in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "adb7c8b8-e408-415e-a8c6-f688e8eaaad7",
  "isSidechain": true,
  "promptId": "f556c21e-91fd-4757-bdee-1c7a3129ceaa",
  "agentId": "a9f8b9a30cdd6a6c3",
  "type": "user",
  "uuid": "56193fe7-0eb8-4865-9ae9-2521c79515f0",
  "sourceToolAssistantUUID": "adb7c8b8-e408-415e-a8c6-f688e8eaaad7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7111d5a1-92b4-4478-a35b-6fcf6ac9e788",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-10T21:01:15.685Z_

Perfect! I've found comprehensive information about the FALCON paper. Let me verify all four of your questions:

## Verification Results

**1. L4DC 2026 Acceptance: ✓ CONFIRMED**
The paper is accepted at L4DC 2026 as an oral presentation. The GitHub repository explicitly shows "[L4DC 2026]" in the title.

**2. Control Decomposition: ✓ CONFIRMED**
Yes, FALCON explicitly decomposes humanoid control into:
- **Lower-body agent**: Maintains stable locomotion under external force disturbances
- **Upper-body agent**: Tracks end-effector positions with implicit adaptive force compensation

**3. Force Curriculum: ✓ CONFIRMED**
Yes, the training uses a force curriculum that progressively escalates the magnitude of external forces applied to the end effector while respecting torque limits.

**4. Performance Claims: ✓ CONFIRMED (2x improvement)**
The paper demonstrates:
- **2x more accurate upper-body joint tracking** compared to baselines
- Robust locomotion maintained under force disturbances
- Faster training convergence
- Cross-robot generalization (same training deployed across multiple humanoid platforms)

## Real-World Validation
FALCON successfully demonstrated forceful loco-manipulation tasks:
- Payload transport: 0-20N force
- Cart-pulling: 0-100N force
- Door-opening: 0-40N force

All four claims have been verified directly from the arXiv paper and official sources.

**Sources:**
- [FALCON arXiv Abstract](https://arxiv.org/abs/2505.06776)
- [FALCON GitHub Repository](https://github.com/LeCAR-Lab/FALCON)
- [FALCON Project Website](https://lecar-lab.github.io/falcon-humanoid/)
- [L4DC 2026 Conference](https://sites.google.com/usc.edu/l4dc2026/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56193fe7-0eb8-4865-9ae9-2521c79515f0",
  "isSidechain": true,
  "agentId": "a9f8b9a30cdd6a6c3",
  "requestId": "req_011CauZaKGD8TuDeXSAaNCzV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "99f9c013-95e1-46c4-8eea-e261aae1ee84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7111d5a1-92b4-4478-a35b-6fcf6ac9e788",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XDHFRYRPvnZrrHGNnbF1Sb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1168,
      "cache_creation_input_tokens": 1895,
      "cache_read_input_tokens": 14237,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1895
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1168,
          "output_tokens": 460,
          "cache_read_input_tokens": 14237,
          "cache_creation_input_tokens": 1895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1895,
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
