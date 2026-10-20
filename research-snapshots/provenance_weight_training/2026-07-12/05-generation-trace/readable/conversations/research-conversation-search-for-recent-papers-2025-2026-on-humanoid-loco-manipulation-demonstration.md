# Research conversation: Search for recent papers (2025-2026) on humanoid loco-manipulation demonstration generation, specifically looking for an

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 73
- **Recorded user turns:** 1
- **Tool calls:** 32
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a9e83b823de4a4c2b.jsonl`
- **Structured JSON:** [`298587e09196044db485.json`](../../sessions/29/298587e09196044db485.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

73 recorded events

### User

_source line 1 · 2026-05-10T13:49:31.677Z_

Search for recent papers (2025-2026) on humanoid loco-manipulation demonstration generation, specifically looking for any work that uses SE(3) object-centric encoding for navigation stances, inverse reachability maps (IRM) for bipedal humanoid data generation, or combinatorial demo multiplication for mobile humanoid robots. I need to know if any papers from April-May 2026 directly address these contributions.

Search queries to run:
1. site:arxiv.org humanoid loco-manipulation demonstration generation 2026
2. site:arxiv.org SE(3) object-centric locomotion manipulation data 2026
3. site:arxiv.org inverse reachability map bipedal humanoid data generation 2025 2026
4. site:arxiv.org combinatorial demonstration generation mobile manipulation humanoid 2026
5. arxiv.org MimicGen locomotion humanoid 2025 2026
6. site:arxiv.org Isaac Lab locomanipulation datagen 2026
7. site:arxiv.org "loco-manipulation" "data generation" 2026 humanoid
8. arxiv.org G1 humanoid demonstration generation combinatorial 2026

Also fetch and read:
- https://arxiv.org/abs/2603.03279 (ULTRA paper abstract)
- https://arxiv.org/abs/2603.12263 (Psi-zero abstract)

Report: title, arxiv ID, date, and brief description of any papers you find that could be competing or concurrent work. Especially flag any papers from April-May 2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "cf281618-bb82-4d92-b2b7-ddabf97b362a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T13:49:34.130Z_

I'll search for recent papers on humanoid loco-manipulation demonstration generation with the specific technical approaches you mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf281618-bb82-4d92-b2b7-ddabf97b362a",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzfANUXboJyehwNA1t9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2bf83421-cd28-417b-a50d-d215d561ac58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LdX1mMx378G8g5ueSTC3NC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16947,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16947,
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

_source line 3 · 2026-05-10T13:49:34.444Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Fc8PDeUw9rVo6KApX89yt`</summary>

```json
{
  "query": "site:arxiv.org humanoid loco-manipulation demonstration generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bf83421-cd28-417b-a50d-d215d561ac58",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzfANUXboJyehwNA1t9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "03acb39f-2804-4f09-950d-9f02f83eb21d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LdX1mMx378G8g5ueSTC3NC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16947,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16947,
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

_source line 4 · 2026-05-10T13:49:34.451Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017FH5FnTmii5Vkm38ddAv7f`</summary>

```json
{
  "query": "site:arxiv.org SE(3) object-centric locomotion manipulation data 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03acb39f-2804-4f09-950d-9f02f83eb21d",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzfANUXboJyehwNA1t9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d6913f13-2c00-48b0-89b4-7cb0f3d5e0ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LdX1mMx378G8g5ueSTC3NC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16947,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16947,
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

_source line 5 · 2026-05-10T13:49:34.542Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012QRGkrbV1YHsiF3FEVXnwW`</summary>

```json
{
  "query": "site:arxiv.org inverse reachability map bipedal humanoid data generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6913f13-2c00-48b0-89b4-7cb0f3d5e0ea",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzfANUXboJyehwNA1t9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9305e3a8-fb58-4c6c-ac94-d87093870bf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LdX1mMx378G8g5ueSTC3NC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16947,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16947,
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

_source line 6 · 2026-05-10T13:49:34.753Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y5iV43HQTu3JEzQU58BCgm`</summary>

```json
{
  "query": "site:arxiv.org combinatorial demonstration generation mobile manipulation humanoid 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9305e3a8-fb58-4c6c-ac94-d87093870bf4",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzfANUXboJyehwNA1t9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "506752a4-e238-4dbf-8264-dbe590e425cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LdX1mMx378G8g5ueSTC3NC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16947,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16947,
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

_source line 7 · 2026-05-10T13:49:34.966Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SV7DUvY1t1pmfwDSJUrCTi`</summary>

```json
{
  "query": "arxiv.org MimicGen locomotion humanoid 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "506752a4-e238-4dbf-8264-dbe590e425cd",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzfANUXboJyehwNA1t9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b8b325dc-96e5-4d72-a9d5-cb768e4a0522",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LdX1mMx378G8g5ueSTC3NC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16947,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16947,
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

_source line 8 · 2026-05-10T13:49:35.176Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019Rwhi4B6QYuHtNWvgZokEU`</summary>

```json
{
  "query": "site:arxiv.org Isaac Lab locomanipulation datagen 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8b325dc-96e5-4d72-a9d5-cb768e4a0522",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzfANUXboJyehwNA1t9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "502e1df0-96fc-4b9e-a497-12fe16a84dcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LdX1mMx378G8g5ueSTC3NC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16947,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16947,
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

_source line 9 · 2026-05-10T13:49:35.384Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J5bjDQCyGDgfcY99i6AraY`</summary>

```json
{
  "query": "site:arxiv.org \"loco-manipulation\" \"data generation\" 2026 humanoid"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "502e1df0-96fc-4b9e-a497-12fe16a84dcd",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzfANUXboJyehwNA1t9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f87b2595-ea98-415c-9c70-500d46548402",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LdX1mMx378G8g5ueSTC3NC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16947,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16947,
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

_source line 10 · 2026-05-10T13:49:35.736Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BdQFqALpSqU5LthwpF8Gki`</summary>

```json
{
  "query": "arxiv.org G1 humanoid demonstration generation combinatorial 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f87b2595-ea98-415c-9c70-500d46548402",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzfANUXboJyehwNA1t9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a9faaaa1-fb73-440f-816e-d2245717b9b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LdX1mMx378G8g5ueSTC3NC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16947,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16947,
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

_source line 11 · 2026-05-10T13:49:36.146Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012qrhti97RDTLCMGX8wx3oT`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.03279",
  "prompt": "What is the title, date, and main contribution of this paper? Does it relate to humanoid loco-manipulation demonstration generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9faaaa1-fb73-440f-816e-d2245717b9b7",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzfANUXboJyehwNA1t9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7b48374b-295f-41d1-a26a-20719c0a93c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LdX1mMx378G8g5ueSTC3NC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16947,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16947,
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

_source line 12 · 2026-05-10T13:49:36.232Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01T5FWgN1V2ji5uhgrPKDe8u`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.12263",
  "prompt": "What is the title, date, and main contribution of this paper? Does it relate to humanoid loco-manipulation demonstration generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b48374b-295f-41d1-a26a-20719c0a93c5",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzfANUXboJyehwNA1t9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b7374753-40b6-4a46-82ca-70f7cee18bb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LdX1mMx378G8g5ueSTC3NC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16947,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16947,
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

### Tool result

_source line 13 · 2026-05-10T13:49:40.045Z_

<details><summary>↩ Tool result · `toolu_012qrhti97RDTLCMGX8wx3oT`</summary>

```text
# ULTRA Paper Summary

**Title:** ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation

**Date:** Submitted March 3, 2026

**Main Contribution:**

The paper introduces a framework addressing whole-body humanoid control through two key components. First, a physics-driven neural retargeting algorithm converts motion capture data to humanoid robots while maintaining physical realism. Second, "a unified multimodal controller that supports both dense references and sparse task specifications" enables humanoids to perform coordinated behaviors from high-level goals rather than predefined motion references.

**Relation to Loco-Manipulation Demonstration Generation:**

Yes, this work directly relates to the field. It moves beyond traditional motion tracking approaches by developing methods to generate autonomous whole-body behaviors. Rather than relying on test-time reference motions, the system learns to produce loco-manipulation behaviors from perception and task specifications, evaluated on a real Unitree G1 humanoid.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b48374b-295f-41d1-a26a-20719c0a93c5",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "e690c09a-5653-4b3a-8e85-004050a78293",
  "sourceToolAssistantUUID": "7b48374b-295f-41d1-a26a-20719c0a93c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T13:49:41.201Z_

<details><summary>↩ Tool result · `toolu_012QRGkrbV1YHsiF3FEVXnwW`</summary>

```text
Web search results for query: "site:arxiv.org inverse reachability map bipedal humanoid data generation 2025 2026"

Links: [{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning","url":"https://arxiv.org/html/2506.16012v1"},{"title":"Humanoid Robots at work: where are we ?","url":"https://arxiv.org/html/2404.04249v1"},{"title":"[2511.12390] Learning Adaptive Neural Teleoperation for Humanoid Robots: From Inverse Kinematics to End-to-End Control","url":"https://arxiv.org/abs/2511.12390"},{"title":"Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation","url":"https://arxiv.org/html/2510.08807v1"},{"title":"Systems and Control Sep 2025","url":"https://arxiv.org/list/eess.SY/2025-09?skip=675&show=250"},{"title":"Humanoid Robots and Humanoid AI: Review, Perspectives and Directions","url":"https://arxiv.org/html/2405.15775v2"},{"title":"Rethinking Video Generation Model for the Embodied World","url":"https://arxiv.org/html/2601.15282v1"},{"title":"Safe Navigation of Bipedal Robots via Koopman Operator- ...","url":"https://arxiv.org/pdf/2409.14736"},{"title":"From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots","url":"https://arxiv.org/html/2506.12779v1"}]

Based on the search results, I found several papers related to bipedal humanoid robots and data generation from arxiv.org published in 2025-2026. However, none of them specifically focus on "inverse reachability maps" as a primary topic. Here's what I found:

**Most relevant result:**

The search did identify one paper that relates to your query: "OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction" by researchers including Lujie Yang and others. This appears to be focused on data generation for humanoid robots.

**Other related papers on humanoid data generation (2025-2026):**

1. "Humanoid Everyday, a large-scale and diverse humanoid manipulation dataset characterized by extensive task variety involving dextrous object manipulation, human-humanoid interaction, locomotion-integrated actions, and more" (October 2025)

2. "DualTHOR: A physics-based simulation platform for complex dual-arm humanoid robots" which includes "inverse kinematics solvers for humanoid robots" (June 2025)

3. "From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots," proposing an expert-generalist learning framework (June 2025)

The papers I found address humanoid robot data generation and control, but the specific combination of "inverse reachability maps" with bipedal humanoid data generation doesn't appear prominently in the arxiv results from your search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9305e3a8-fb58-4c6c-ac94-d87093870bf4",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "78274d72-b86a-4457-b133-8eb82d1e6e85",
  "sourceToolAssistantUUID": "9305e3a8-fb58-4c6c-ac94-d87093870bf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T13:49:42.003Z_

<details><summary>↩ Tool result · `toolu_019Rwhi4B6QYuHtNWvgZokEU`</summary>

```text
Web search results for query: "site:arxiv.org Isaac Lab locomanipulation datagen 2026"

Links: [{"title":"[2511.04831] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning","url":"https://arxiv.org/abs/2511.04831"},{"title":"Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning","url":"https://arxiv.org/html/2511.04831v1"},{"title":"NaVILA: Legged Robot Vision-Language-Action Model for Navigation","url":"https://arxiv.org/html/2412.04453v1"},{"title":"SONIC: Supersizing Motion Tracking for Natural Humanoid ...","url":"https://arxiv.org/pdf/2511.07820"},{"title":"ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI","url":"https://arxiv.org/html/2410.00425v1"},{"title":"GenPO: Generative Diffusion Models Meet On-Policy Reinforcement Learning","url":"https://arxiv.org/html/2505.18763v2"},{"title":"Learning Agile Locomotion on Risky Terrains","url":"https://arxiv.org/pdf/2311.10484"},{"title":"[2510.01264] A Framework for Scalable Heterogeneous Multi-Agent Adversarial Reinforcement Learning in IsaacLab","url":"https://arxiv.org/abs/2510.01264"},{"title":"A Framework for Scalable Heterogeneous Multi-Agent Adversarial Reinforcement Learning in IsaacLab","url":"https://arxiv.org/html/2510.01264v1"},{"title":"[2108.10470] Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning","url":"https://arxiv.org/abs/2108.10470"}]

Based on the web search results, I found several papers related to Isaac Lab on arxiv.org. While there isn't a paper specifically matching all the terms "Isaac Lab locomanipulation datagen 2026," here are the most relevant results:

## Primary Result

The most recent and comprehensive Isaac Lab paper is "Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning," which extends GPU-native robotics simulation with high-fidelity physics, photorealistic rendering, and integrates actuator models, multi-frequency sensor simulation, data collection pipelines, and domain randomization tools. This paper (arXiv:2511.04831) was published in November 2025.

## Related Work on Locomanipulation

A relevant paper on whole-body control is "SONIC," which discusses evaluations conducted in Isaac Lab and explores VLA instructed whole-body locomanipulation tasks (arXiv:2511.07820).

## Other Isaac Lab Applications

The search results also show Isaac Lab being used for:
- Vision-based RL policy training achieving high throughput and featuring more realistic scenes with low-level controls (NaVILA paper)
- Benchmarks covering legged locomotion tasks with various robots (GenPO paper)

The search results suggest that Isaac Lab is actively being developed for various robotics tasks including locomotion, manipulation, and data generation, though the specific combination of all your search terms may not exist as a single paper title on arxiv.org.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "502e1df0-96fc-4b9e-a497-12fe16a84dcd",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "b4e3e9f7-12b6-48ff-823a-4c6e5fa5999f",
  "sourceToolAssistantUUID": "502e1df0-96fc-4b9e-a497-12fe16a84dcd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T13:49:42.575Z_

<details><summary>↩ Tool result · `toolu_01T5FWgN1V2ji5uhgrPKDe8u`</summary>

```text
# Paper Summary

**Title:** Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation

**Date:** Submitted March 12, 2026

**Main Contribution:**

The paper presents a foundation model that addresses humanoid loco-manipulation through a staged training approach. Rather than co-training on mixed human-robot data, the authors "decouple the learning process to maximize the utility of heterogeneous data sources." The model first pre-trains on egocentric human videos, then post-trains on humanoid robot data, achieving superior performance with significantly less training data than comparable baselines.

**Relevance to Humanoid Loco-Manipulation Demonstration Generation:**

Yes, this work directly relates to the field. It specifically targets "challenging humanoid loco-manipulation tasks" and demonstrates that high-quality egocentric human manipulation data followed by domain-specific robot trajectories yields better results than scaling with larger, noisier datasets. The authors promise to "open-source the entire ecosystem," including training pipelines and inference engines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7374753-40b6-4a46-82ca-70f7cee18bb3",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "53a36761-bd9f-41e8-b19f-896895b86010",
  "sourceToolAssistantUUID": "b7374753-40b6-4a46-82ca-70f7cee18bb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T13:49:42.600Z_

<details><summary>↩ Tool result · `toolu_01Y5iV43HQTu3JEzQU58BCgm`</summary>

```text
Web search results for query: "site:arxiv.org combinatorial demonstration generation mobile manipulation humanoid 2026"

Links: [{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/html/2507.00833"},{"title":"[2510.18316] MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation","url":"https://arxiv.org/abs/2510.18316"},{"title":"CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System","url":"https://arxiv.org/html/2508.00162v1"},{"title":"Humanoid Robots at work: where are we ?","url":"https://arxiv.org/html/2404.04249v1"},{"title":"MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation","url":"https://arxiv.org/html/2510.18316v1"},{"title":"Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations","url":"https://arxiv.org/html/2602.06643"},{"title":"[2512.25072] Coordinated Humanoid Manipulation with Choice Policies","url":"https://arxiv.org/abs/2512.25072"},{"title":"Coordinated Humanoid Manipulation with Choice Policies","url":"https://arxiv.org/html/2512.25072"},{"title":"Learning Versatile Humanoid Manipulation with Touch Dreaming","url":"https://arxiv.org/html/2604.13015"}]

I found several relevant papers on arXiv related to humanoid robotics and demonstration generation. Here are the key results:

## Most Relevant Papers

1. **HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning** (2025)
   - This proposes an LLM-based framework capable of generating diverse manipulation tasks and collecting scalable demonstrations for humanoid robots

2. **MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation** (2026)
   - This addresses the challenge of collecting demonstration data for multi-step bimanual mobile manipulation tasks

3. **Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations** (2026)
   - This system enables robot-free data collection by capturing rich whole-body motion using portable hardware, with data driving a hierarchical learning pipeline that translates human motions into dexterous and feasible humanoid skills

4. **Coordinated Humanoid Manipulation with Choice Policies** (2025)
   - A system combining a modular teleoperation interface with a scalable learning framework that decomposes humanoid control into intuitive submodules for efficient demonstration collection

5. **Learning Versatile Humanoid Manipulation with Touch Dreaming** (2026)
   - An integrated whole-body humanoid manipulation system combining an RL-based controller with VR teleoperation for collecting high-quality real-world demonstrations

These papers represent recent work in automated demonstration generation and data collection for humanoid robots, with particular focus on mobile manipulation, bimanual coordination, and whole-body control.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "506752a4-e238-4dbf-8264-dbe590e425cd",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "ad5dcae6-668b-4061-b8a7-631094b060b2",
  "sourceToolAssistantUUID": "506752a4-e238-4dbf-8264-dbe590e425cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T13:49:42.785Z_

<details><summary>↩ Tool result · `toolu_014Fc8PDeUw9rVo6KApX89yt`</summary>

```text
Web search results for query: "site:arxiv.org humanoid loco-manipulation demonstration generation 2026"

Links: [{"title":"EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration","url":"https://arxiv.org/html/2602.10106v1"},{"title":"[2602.10106] EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration","url":"https://arxiv.org/abs/2602.10106"},{"title":"VisualMimic Visual Humanoid Loco-Manipulation via Motion Tracking and Generation","url":"https://arxiv.org/html/2509.20322v1"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"[2604.13015] Learning Versatile Humanoid Manipulation with Touch Dreaming","url":"https://arxiv.org/abs/2604.13015"},{"title":"[2509.20322] VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation","url":"https://arxiv.org/abs/2509.20322"},{"title":"VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2511.15200v1"},{"title":"[2603.12263] $Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://arxiv.org/abs/2603.12263"},{"title":"[2509.26633] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/abs/2509.26633"},{"title":"LHM-Humanoid: Learning a Unified Policy for Long-Horizon Humanoid Whole-Body Loco-Manipulation in Diverse Messy Environments","url":"https://arxiv.org/html/2508.16943"}]

The search has returned several highly relevant results from arXiv focusing on humanoid loco-manipulation with demonstration generation in 2026. Here are the key papers found:

## Key Results:

1. **EgoHumanoid** (February 2026): The first framework to co-train a vision-language-action policy using abundant egocentric human demonstrations together with a limited amount of robot data, enabling humanoids to perform loco-manipulation across diverse real-world environments.

2. **Ψ₀ (Psi-Zero)** (March 2026): An open foundation model to address challenging humanoid loco-manipulation tasks. Achieves the best performance using only about 800 hours of human video data and 30 hours of real-world robot data, outperforming baselines pre-trained on more than 10× as much data by over 40%.

3. **Learning Versatile Humanoid Manipulation with Touch Dreaming** (April 2026): Addresses humanoid loco-manipulation challenges requiring whole-body stability, dexterous hands, and contact-aware perception under frequent contact changes by developing an RL-based whole-body controller that provides stable lower-body and torso execution during complex manipulation.

4. **VisualMimic** (September 2025): Enables zero-shot transfer of visuomotor policies trained in simulation to real humanoid robots, accomplishing a wide range of loco-manipulation tasks such as box lifting, pushing, football dribbling, and kicking.

5. **OmniRetarget** (September 2025): An interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects.

6. **LHM-Humanoid**: Demands cross-scene generalization and unified one-policy control with a dataset spanning four room types comprising 350 diverse scenes/tasks with 79 objects.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03acb39f-2804-4f09-950d-9f02f83eb21d",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "ed8e0281-a23a-4b70-b07b-605f038277b5",
  "sourceToolAssistantUUID": "03acb39f-2804-4f09-950d-9f02f83eb21d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T13:49:42.833Z_

<details><summary>↩ Tool result · `toolu_01BdQFqALpSqU5LthwpF8Gki`</summary>

```text
Web search results for query: "arxiv.org G1 humanoid demonstration generation combinatorial 2026"

Links: [{"title":"Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking","url":"https://arxiv.org/html/2604.17335"},{"title":"Learning Getting-Up Policies for Real-World Humanoid Robots","url":"https://arxiv.org/html/2502.12152v1"},{"title":"[2503.14734] GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/abs/2503.14734"},{"title":"HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/html/2507.00833"},{"title":"DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning","url":"https://arxiv.org/html/2506.16012v1"},{"title":"2025-3-28 GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/pdf/2503.14734"},{"title":"Hierarchical Intention-Aware Expressive Motion Generation for Humanoid Robots","url":"https://arxiv.org/html/2506.01563v1"},{"title":"[2507.00833v1] HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/abs/2507.00833v1"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub","url":"https://github.com/NVIDIA/Isaac-GR00T"}]

Based on the search results, I found several relevant papers and resources related to G1 humanoid robots and demonstration generation:

## Key Findings:

**HumanoidGen - Data Generation Framework:**
HumanoidGen is an LLM-based framework capable of generating diverse manipulation tasks and collecting scalable demonstrations for humanoid robots. The framework generates code for environment setup and success criteria based on language descriptions and adopts LLMs to perform task decomposition for long-horizon tasks, generating spatial rational constraints for arm movements. The paper mentions combinatorial aspects in handling task decomposition and constraint generation.

**G1 Humanoid Robot Applications:**
Multiple papers demonstrate the Unitree G1 humanoid robot being used for various tasks:
- The motion generator runs on a Jetson Thor mounted on the back of the robot, while the motion tracking controller and remaining onboard modules run on the Jetson Orin integrated into the Unitree G1 platform.
- Experiments were conducted with the G1 platform from Unitree.

**Contact-Implicit Planning:**
In the broader context of humanoid locomotion and manipulation, the open problem involves solving the locomotion and manipulation contact planning problem simultaneously with whole-body trajectory planning in a unified fashion, which has high computational burden and combinatorial complexity of identifying potential contact mode sequences.

The search results show active research in 2026 on automated demonstration generation and task planning for humanoid robots, though the specific paper matching all your query terms may require a more targeted search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9faaaa1-fb73-440f-816e-d2245717b9b7",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "b6ee7523-ff36-40fc-9555-b50de5fcba12",
  "sourceToolAssistantUUID": "a9faaaa1-fb73-440f-816e-d2245717b9b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T13:49:43.368Z_

<details><summary>↩ Tool result · `toolu_01J5bjDQCyGDgfcY99i6AraY`</summary>

```text
Web search results for query: "site:arxiv.org "loco-manipulation" "data generation" 2026 humanoid"

Links: [{"title":"OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/html/2509.26633v2"},{"title":"[2509.26633] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/abs/2509.26633"},{"title":"[2509.26633v1] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/abs/2509.26633v1"},{"title":"DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2510.11258v1"},{"title":"OmniRetarget: Interaction-Preserving Data Generation for Humanoid","url":"https://arxiv.org/pdf/2509.26633"},{"title":"AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning","url":"https://arxiv.org/html/2603.20147v1"},{"title":"VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2511.15200v1"},{"title":"HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/html/2507.00833"}]

Based on the web search results, I found several highly relevant papers on arXiv about humanoid loco-manipulation and data generation. Here are the key findings:

## Primary Results

**OmniRetarget** - OmniRetarget is an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. This high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained with only 5 reward terms and simple domain randomization shared by all tasks, without any learning curriculum.

**DemoHLM** - DemoHLM is a framework for humanoid loco-manipulation that enables scalable data generation and policy learning across diverse tasks. For each task, DemoHLM requires only a single demonstration and automatically synthesizes hundreds to thousands of successful trajectories.

**VIRAL** - VIRAL is a visual sim-to-real framework that learns humanoid loco-manipulation entirely in simulation and deploys it zero-shot to real hardware. VIRAL follows a teacher-student design: a privileged RL teacher, operating on full state, learns long-horizon loco-manipulation using a delta action space and reference state initialization. A vision-based student policy is then distilled from the teacher via large-scale simulation with tiled rendering, trained with a mixture of online DAgger and behavior cloning.

**HumanoidGen** - HumanoidGen is an automated task creation and demonstration collection framework that leverages atomic dexterous operations and LLM reasoning to generate relational constraints. It provides spatial annotations for both assets and dexterous hands based on the atomic operations, and performs an LLM planner to generate a chain of actionable spatial constraints for arm movements based on object affordances and scenes.

These papers represent recent advances in data generation methods for humanoid loco-manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f87b2595-ea98-415c-9c70-500d46548402",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "4b9082c8-b990-4fba-b4a4-3247ae5b6aac",
  "sourceToolAssistantUUID": "f87b2595-ea98-415c-9c70-500d46548402",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T13:49:44.276Z_

<details><summary>↩ Tool result · `toolu_017FH5FnTmii5Vkm38ddAv7f`</summary>

```text
Web search results for query: "site:arxiv.org SE(3) object-centric locomotion manipulation data 2026"

Links: [{"title":"[2411.00965] SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation","url":"https://arxiv.org/abs/2411.00965"},{"title":"SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation","url":"https://arxiv.org/html/2411.00965v2"},{"title":"A Survey of Embodied Learning for Object-Centric Robotic Manipulation","url":"https://arxiv.org/html/2408.11537v1"},{"title":"Visual Manipulation with Legs","url":"https://arxiv.org/html/2410.11345v2"},{"title":"Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation","url":"https://arxiv.org/html/2407.00451v2"},{"title":"[2307.02427] FOCUS: Object-Centric World Models for Robotics Manipulation","url":"https://ar5iv.labs.arxiv.org/html/2307.02427"},{"title":"Moving Through Clutter: Scaling Data Collection and Benchmarking for 3D Scene-Aware Humanoid Locomotion via Virtual Reality","url":"https://arxiv.org/html/2603.05993"},{"title":"[2411.04005] Object-Centric Dexterous Manipulation from Human Motion Data","url":"https://arxiv.org/abs/2411.04005"},{"title":"CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation","url":"https://arxiv.org/html/2505.02166v1"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"}]

I've performed the web search for your query. Here are the results:

## Search Results Summary

The search returned several relevant papers from arxiv.org related to SE(3), object-centric learning, and robotics:

1. **SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation** (arXiv:2411.00965)
   - Introduces an object-centric imitation learning framework that captures tasks through SE(3) object pose trajectories relative to the target. In real-world evaluation, using only eight demonstrations, the approach completed all tasks while fully complying with task constraints.

2. **A Survey of Embodied Learning for Object-Centric Robotic Manipulation** (arXiv:2408.11537)
   - Addresses embodied learning for object-centric robotic manipulation as a rapidly developing field in embodied AI that is crucial for advancing next-generation intelligent robots.

3. **Visual Manipulation with Legs** (arXiv:2410.11345)
   - Bridges the gap between locomotion and manipulation by leveraging non-prehensile manipulation for leg-based tasks.

4. **Moving Through Clutter: Scaling Data Collection and Benchmarking for 3D Scene-Aware Humanoid Locomotion via Virtual Reality** (arXiv:2603.05993)
   - Presents Moving Through Clutter (MTC), a Virtual Reality-based data collection and evaluation framework for scene-aware humanoid locomotion in cluttered environments.

5. **Object-Centric Dexterous Manipulation from Human Motion Data** (arXiv:2411.04005)
   - Introduces a hierarchical policy learning framework using human hand motion data for training object-centric dexterous robot manipulation with a high-level trajectory generative model learned from large-scale human hand motion capture.

6. **CrayonRobo: Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation** (arXiv:2505.02166)
   - Develops a model that can predict corresponding SE(3) contact poses and 3D next movement directions after contact.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6913f13-2c00-48b0-89b4-7cb0f3d5e0ea",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "8562e751-30de-42e9-924d-a24e8f4ab87c",
  "sourceToolAssistantUUID": "d6913f13-2c00-48b0-89b4-7cb0f3d5e0ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T13:49:45.492Z_

<details><summary>↩ Tool result · `toolu_01SV7DUvY1t1pmfwDSJUrCTi`</summary>

```text
Web search results for query: "arxiv.org MimicGen locomotion humanoid 2025 2026"

Links: [{"title":"Mimicking-Bench: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking","url":"https://arxiv.org/html/2412.17730v1"},{"title":"GitHub - visualmimic/VisualMimic: [arXiv 2025] VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation · GitHub","url":"https://github.com/visualmimic/VisualMimic"},{"title":"HumanMimic: Learning Natural Locomotion and Transitions for Humanoid Robot via Wasserstein Adversarial Imitation","url":"https://arxiv.org/html/2309.14225v4"},{"title":"[2309.14225] HumanMimic: Learning Natural Locomotion and Transitions for Humanoid Robot via Wasserstein Adversarial Imitation","url":"https://arxiv.org/abs/2309.14225"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Natural Humanoid Robot Locomotion with Generative Motion Prior","url":"https://arxiv.org/html/2503.09015v1"},{"title":"GitHub - BaiShuanghao/Awesome-Robotics-Manipulation: A comprehensive list of papers about Robot Manipulation, including papers, codes, and related websites. · GitHub","url":"https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation"},{"title":"[2509.20322] VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation","url":"https://arxiv.org/abs/2509.20322"},{"title":"Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning | OpenReview","url":"https://openreview.net/forum?id=hVoIz6xD9Q"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"}]

Based on the search results, I found several relevant papers related to humanoid locomotion and motion generation:

## Key Findings

**VisualMimic** is a prominent recent work in this area. VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation, arXiv 2025. VisualMimic is a visual sim-to-real framework that unifies egocentric vision with hierarchical whole-body control for humanoid robots, combining a task-agnostic low-level keypoint tracker trained from human motion data via a teacher-student scheme with a task-specific high-level policy that generates keypoint commands from visual and proprioceptive input.

Other related work includes:

- HumanMimic, an adversarial imitation learning system that enables full-sized humanoids to autonomously acquire a variety of realistic locomotion behaviors through imitating human demonstrations.

- A method called Generative Motion Prior (GMP) that utilizes a generative model to online synthesize human-like reference motion trajectories, training a motion generation network based on a Conditional Variational Auto-encoder (CVAE), which is capable of predicting future natural robot motions in an auto-regressive manner.

- Adversarial Locomotion and Motion Imitation (ALMI), a framework that enables adversarial policy learning between upper and lower body for humanoid robots.

These papers represent the current state of research in humanoid locomotion and loco-manipulation, with approaches leveraging motion imitation, generative models, and adversarial learning techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8b325dc-96e5-4d72-a9d5-cb768e4a0522",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "f4bf7b93-aef7-41c2-92e4-3870ec756a53",
  "sourceToolAssistantUUID": "b8b325dc-96e5-4d72-a9d5-cb768e4a0522",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T13:49:47.403Z_

Excellent. Now let me fetch the full papers for the key candidates from April-May 2026 to check for the specific technical contributions you mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4bf7b93-aef7-41c2-92e4-3870ec756a53",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzgBJobikLQBYA5QFi3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e5150cbf-b124-4c98-b514-5bc738d158ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MaiD8i2pQq3DiMTECCUex1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3158,
      "cache_creation_input_tokens": 6365,
      "cache_read_input_tokens": 16947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6365,
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

_source line 24 · 2026-05-10T13:49:48.114Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WUYWwRuP9NMyNWPhgxeiEW`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.13015",
  "prompt": "What is the date, title, and specific technical contributions? Does it mention SE(3) encoding, inverse reachability maps, or combinatorial demonstration generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5150cbf-b124-4c98-b514-5bc738d158ad",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzgBJobikLQBYA5QFi3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7c32eed7-ce89-42f4-8bde-424422d3e7e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MaiD8i2pQq3DiMTECCUex1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3158,
      "cache_creation_input_tokens": 6365,
      "cache_read_input_tokens": 16947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6365,
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

_source line 25 · 2026-05-10T13:49:48.965Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014R4uZsAfG5oddXYXjCoUw2`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.05993",
  "prompt": "What is the date, title, and main contributions? Does it use SE(3) object-centric encoding, inverse reachability maps, or combinatorial demo multiplication?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c32eed7-ce89-42f4-8bde-424422d3e7e9",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzgBJobikLQBYA5QFi3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c57208c2-ec35-44e3-8b70-fd9e16ab3336",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MaiD8i2pQq3DiMTECCUex1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3158,
      "cache_creation_input_tokens": 6365,
      "cache_read_input_tokens": 16947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6365,
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

_source line 26 · 2026-05-10T13:49:49.132Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019hRn6pTQjeJ9Mm9feELYBB`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.20147",
  "prompt": "What is the date, title, and main contributions? Does it mention SE(3), inverse reachability maps, or combinatorial demonstration generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c57208c2-ec35-44e3-8b70-fd9e16ab3336",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzgBJobikLQBYA5QFi3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ae2604b4-7a0a-4ea5-b2e1-189930134ade",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MaiD8i2pQq3DiMTECCUex1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3158,
      "cache_creation_input_tokens": 6365,
      "cache_read_input_tokens": 16947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6365,
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

_source line 27 · 2026-05-10T13:49:49.513Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ta1iWeEoD48Th7v7wByWeV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.10106",
  "prompt": "What is the date, title, and main contributions? Does it use SE(3), inverse reachability maps, or combinatorial demo generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae2604b4-7a0a-4ea5-b2e1-189930134ade",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzgBJobikLQBYA5QFi3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b81bb3ea-d784-408c-8f51-e24b6f0bf52f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MaiD8i2pQq3DiMTECCUex1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3158,
      "cache_creation_input_tokens": 6365,
      "cache_read_input_tokens": 16947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6365,
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

_source line 28 · 2026-05-10T13:49:49.895Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WkVXtx5RHuh4yxqTFW4o73`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.18316",
  "prompt": "What is the title, date, and main contributions? Does it mention combinatorial demonstration generation, constraints-based synthesis, or data multiplication methods?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b81bb3ea-d784-408c-8f51-e24b6f0bf52f",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzgBJobikLQBYA5QFi3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "31b7dcae-bebd-4fd2-b25a-38344e0a67d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MaiD8i2pQq3DiMTECCUex1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3158,
      "cache_creation_input_tokens": 6365,
      "cache_read_input_tokens": 16947,
      "output_tokens": 533,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6365
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3158,
          "output_tokens": 533,
          "cache_read_input_tokens": 16947,
          "cache_creation_input_tokens": 6365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6365,
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

_source line 29 · 2026-05-10T13:49:52.800Z_

<details><summary>↩ Tool result · `toolu_01WUYWwRuP9NMyNWPhgxeiEW`</summary>

```text
# Paper Analysis

**Date:** Submitted April 14, 2026; revised April 27, 2026

**Title:** "Learning Versatile Humanoid Manipulation with Touch Dreaming"

**Technical Contributions:**

The paper introduces a multimodal learning approach centered on tactile integration. Key contributions include:

1. An RL-based lower-body controller providing stability during whole-body manipulation tasks
2. A VR-based data collection system combining dexterous hands with tactile sensing
3. Humanoid Transformer with Touch Dreaming (HTD), which processes "touch as a core modality alongside multi-view vision and proprioception"

The training approach uses "behavioral cloning augmented by touch dreaming," where the policy simultaneously predicts action chunks, future hand-joint forces, and future tactile latents using an exponential moving average target encoder.

**Regarding Your Specific Questions:**

The abstract and available content do not mention SE(3) encoding, inverse reachability maps, or combinatorial demonstration generation. These techniques are not referenced in the provided webpage material.

The work demonstrates a 90.9% relative improvement over baseline methods and shows latent-space tactile prediction outperforms raw tactile prediction by approximately 30%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c32eed7-ce89-42f4-8bde-424422d3e7e9",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "37d26871-4d4d-4645-baee-614c8b27013d",
  "sourceToolAssistantUUID": "7c32eed7-ce89-42f4-8bde-424422d3e7e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T13:49:52.836Z_

<details><summary>↩ Tool result · `toolu_014R4uZsAfG5oddXYXjCoUw2`</summary>

```text
# Paper Summary

**Date:** Submitted March 6, 2026

**Title:** "Moving Through Clutter: Scaling Data Collection and Benchmarking for 3D Scene-Aware Humanoid Locomotion via Virtual Reality"

**Main Contributions:**

The researchers address a gap in humanoid robotics by creating a Virtual Reality framework for collecting motion data in cluttered environments. They introduce:

1. A VR-based system that procedurally generates scenes with varying clutter levels and captures full-body human movement through immersive navigation
2. Automatic retargeting of human motion to humanoid robot models
3. Performance benchmarks measuring environment clutter and locomotion metrics including "stability and collision safety"
4. A dataset comprising "348 trajectories across 145 diverse 3D cluttered scenes"

**Regarding your specific questions:** The provided abstract and page content do not mention SE(3) object-centric encoding, inverse reachability maps, or combinatorial demo multiplication. These techniques are not discussed in the available material.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c57208c2-ec35-44e3-8b70-fd9e16ab3336",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "11814f3b-a624-44e7-920b-4a04ab87a10e",
  "sourceToolAssistantUUID": "c57208c2-ec35-44e3-8b70-fd9e16ab3336",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T13:49:53.119Z_

<details><summary>↩ Tool result · `toolu_019hRn6pTQjeJ9Mm9feELYBB`</summary>

```text
# AGILE Paper Summary

**Date:** Submitted March 20, 2026

**Title:** "AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning"

**Main Contributions:**

The paper presents an end-to-end workflow addressing sim-to-real transfer challenges through four stages:

1. Interactive environment verification
2. Reproducible training with stabilization enhancements
3. Unified evaluation combining scenario-based tests and randomized rollouts with motion-quality diagnostics
4. Descriptor-driven deployment via configuration descriptors

The authors validated their approach "across five representative humanoid skills spanning locomotion, recovery, motion imitation, and loco-manipulation on two hardware platforms (Unitree G1 and Booster T1)."

**Regarding Your Specific Questions:**

The abstract provided does **not** mention SE(3), inverse reachability maps, or combinatorial demonstration generation. These topics are not referenced in the available content from this arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ae2604b4-7a0a-4ea5-b2e1-189930134ade",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "68d04327-1a76-48ea-8ba1-f2fc42532c69",
  "sourceToolAssistantUUID": "ae2604b4-7a0a-4ea5-b2e1-189930134ade",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T13:49:54.063Z_

<details><summary>↩ Tool result · `toolu_01Ta1iWeEoD48Th7v7wByWeV`</summary>

```text
# EgoHumanoid Paper Summary

**Date:** Submitted February 10, 2026

**Title:** "EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration"

## Main Contributions

The framework introduces several key innovations for humanoid robot training:

1. **Hybrid training approach:** Combines "abundant egocentric human demonstrations together with a limited amount of robot data" to enable real-world loco-manipulation across diverse environments.

2. **Embodiment alignment pipeline:** Addresses the gap between human and robot morphologies through:
   - View alignment that "reduces visual domain discrepancies caused by camera height and perspective variation"
   - Action alignment mapping human movements into feasible humanoid control spaces

3. **Data collection system:** Develops portable hardware and protocols for scalable human demonstration gathering.

4. **Performance gains:** Demonstrates that incorporating human data "significantly outperforms robot-only baselines by 51%, particularly in unseen environments."

## Technical Methods

The paper does **not mention** SE(3) transforms, inverse reachability maps, or combinatorial demonstration generation in the abstract provided. The focus centers on vision-language-action policy co-training and systematic human-to-robot alignment rather than these specific mathematical or algorithmic approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b81bb3ea-d784-408c-8f51-e24b6f0bf52f",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "dd018cfb-2212-42ac-844a-e3c60d1459d3",
  "sourceToolAssistantUUID": "b81bb3ea-d784-408c-8f51-e24b6f0bf52f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-10T13:49:55.746Z_

<details><summary>↩ Tool result · `toolu_01WkVXtx5RHuh4yxqTFW4o73`</summary>

```text
# MoMaGen Paper Summary

**Title:** "MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation"

**Date:** Submitted October 21, 2025; accepted to ICLR 2026

**Main Contributions:**

The work addresses automated demonstration generation for complex robotic tasks. The paper formulates data generation as "a constrained optimization problem that satisfies hard constraints (e.g., reachability) while balancing soft constraints (e.g., visibility while navigation)."

**Relevant Methods:**

Yes, the paper explicitly engages with constraint-based synthesis and data multiplication approaches:

- It extends prior "X-Gen works" that automated data generation by synthesizing large-scale datasets from limited human demonstrations
- It tackles two critical constraints: robot base placement (reachability) and camera positioning (visibility)
- The method generates "much more diverse datasets than previous methods," enabling successful policy training from a single source demonstration

The approach represents a principled framework that "generalizes across most existing automated data generation approaches," suggesting it builds upon and improves combinatorial synthesis methods for robotic learning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31b7dcae-bebd-4fd2-b25a-38344e0a67d6",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "b5696b96-76f8-45fd-babd-194589d65565",
  "sourceToolAssistantUUID": "31b7dcae-bebd-4fd2-b25a-38344e0a67d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-10T13:49:57.422Z_

Now let me search more specifically for papers mentioning the exact technical terms to ensure comprehensive coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5696b96-76f8-45fd-babd-194589d65565",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzgwAXxR1haTD72ENEL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aea0b603-abc2-4ffc-b256-6caed4f6ac55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TMgySAT8QgAQtk2jd5iUP3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5094,
      "cache_read_input_tokens": 23312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5094,
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

_source line 35 · 2026-05-10T13:49:57.774Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WMjDUPLhp5mE3W1DFCSFGn`</summary>

```json
{
  "query": "site:arxiv.org \"inverse reachability\" humanoid 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aea0b603-abc2-4ffc-b256-6caed4f6ac55",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzgwAXxR1haTD72ENEL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "faa081d1-9f19-4e02-9e18-630d958ac24c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TMgySAT8QgAQtk2jd5iUP3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5094,
      "cache_read_input_tokens": 23312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5094,
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

_source line 36 · 2026-05-10T13:49:58.031Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013xrUhhmesxK8jixXcyzWpo`</summary>

```json
{
  "query": "site:arxiv.org \"combinatorial\" \"demonstration\" humanoid 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faa081d1-9f19-4e02-9e18-630d958ac24c",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzgwAXxR1haTD72ENEL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fb1c07c4-8b44-47fc-8ab2-070ae2e3324f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TMgySAT8QgAQtk2jd5iUP3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5094,
      "cache_read_input_tokens": 23312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5094,
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

_source line 37 · 2026-05-10T13:49:58.296Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AM3jupfWfUoJVyUz6ynnPm`</summary>

```json
{
  "query": "site:arxiv.org humanoid data generation April 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb1c07c4-8b44-47fc-8ab2-070ae2e3324f",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzgwAXxR1haTD72ENEL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "644e44a6-2757-4f51-9027-8537af3f859a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TMgySAT8QgAQtk2jd5iUP3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5094,
      "cache_read_input_tokens": 23312,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5094
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 236,
          "cache_read_input_tokens": 23312,
          "cache_creation_input_tokens": 5094,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5094,
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

_source line 38 · 2026-05-10T13:49:58.315Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PJqsgdXyeiq9MarhD6ZZqt`</summary>

```json
{
  "query": "site:arxiv.org humanoid data generation May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "644e44a6-2757-4f51-9027-8537af3f859a",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzgwAXxR1haTD72ENEL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "af3774fa-181c-466e-9dd6-dc0540b86341",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TMgySAT8QgAQtk2jd5iUP3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5094,
      "cache_read_input_tokens": 23312,
      "output_tokens": 236,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5094
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 236,
          "cache_read_input_tokens": 23312,
          "cache_creation_input_tokens": 5094,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5094,
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

_source line 39 · 2026-05-10T13:50:01.022Z_

<details><summary>↩ Tool result · `toolu_01WMjDUPLhp5mE3W1DFCSFGn`</summary>

```text
Web search results for query: "site:arxiv.org "inverse reachability" humanoid 2026"

No links found.

The search returned no results. This could mean that there are no papers on arXiv that match all of these criteria: containing both the phrase "inverse reachability" and the word "humanoid" in publications from 2026. You might try:

1. Removing some of the more specific constraints (like the year 2026 or the site restriction)
2. Using individual keywords rather than the exact phrase
3. Searching for variations of these terms

Would you like me to try a modified search?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "faa081d1-9f19-4e02-9e18-630d958ac24c",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "951f7b92-9f69-4f50-b78d-6bb66a500ad6",
  "sourceToolAssistantUUID": "faa081d1-9f19-4e02-9e18-630d958ac24c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T13:50:04.173Z_

<details><summary>↩ Tool result · `toolu_013xrUhhmesxK8jixXcyzWpo`</summary>

```text
Web search results for query: "site:arxiv.org "combinatorial" "demonstration" humanoid 2026"

Links: [{"title":"From Human Hands to Robot Arms: Manipulation Skills Transfer via Trajectory Alignment","url":"https://arxiv.org/html/2510.00491v1"},{"title":"Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning *co-corresponding authors","url":"https://arxiv.org/html/2501.02116v1"},{"title":"Learning Getting-Up Policies for Real-World Humanoid Robots","url":"https://arxiv.org/html/2502.12152v1"},{"title":"CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System","url":"https://arxiv.org/html/2508.00162v1"},{"title":"DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning","url":"https://arxiv.org/html/2506.16012v1"},{"title":"Humanoid Robots at work: where are we ?","url":"https://arxiv.org/html/2404.04249v1"},{"title":"[2503.14734] GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/abs/2503.14734"},{"title":"Robotics","url":"https://arxiv.org/list/cs.RO/new"},{"title":"Humanoid Factors: Design Principles for AI Humanoids in Human Worlds","url":"https://arxiv.org/pdf/2602.10069"},{"title":"Robotics Jun 2025","url":"https://www.arxiv.org/list/cs.RO/2025-06?skip=0&show=2000"}]

I've performed the web search for your query: `site:arxiv.org "combinatorial" "demonstration" humanoid 2026`

The search returned 10 results from arXiv, with papers related to humanoid robotics published in 2025-2026. While the results include several relevant papers on humanoid robots, learning from demonstrations, and related topics, I didn't find a specific paper that prominently features all three terms ("combinatorial," "demonstration," and "humanoid") together in the 2026 timeframe.

The closest relevant results include:

1. A paper on manipulation skills transfer that discloses use of an LLM for language polishing in accordance with ICLR 2026 policy

2. A humanoid robotics review focusing on robots that emulate human morphologies and can exploit abundant data from human demonstrations

3. Research demonstrating learned getting-up policies for the G1 humanoid robot, described as the first successful demonstration of learned getting-up policies for human-sized humanoid robots

4. The CHILD system for humanoid teleoperation, described as the first system utilizing direct joint mapping approach for whole-body control

If you're looking for a specific paper that combines these three terms, you may need to refine your search query or check the direct arXiv website for more recent submissions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb1c07c4-8b44-47fc-8ab2-070ae2e3324f",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "c1441299-14a6-48b8-932b-957ed2c912fe",
  "sourceToolAssistantUUID": "fb1c07c4-8b44-47fc-8ab2-070ae2e3324f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T13:50:04.632Z_

<details><summary>↩ Tool result · `toolu_01AM3jupfWfUoJVyUz6ynnPm`</summary>

```text
Web search results for query: "site:arxiv.org humanoid data generation April 2026"

Links: [{"title":"[2604.08509] Visually-grounded Humanoid Agents","url":"https://arxiv.org/abs/2604.08509"},{"title":"Rethinking Video Generation Model for the Embodied World","url":"https://arxiv.org/html/2601.15282v1"},{"title":"OmniRetarget: Interaction-Preserving Data Generation for Humanoid","url":"https://arxiv.org/pdf/2509.26633"},{"title":"Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation","url":"https://arxiv.org/html/2510.08807v1"},{"title":"Generalizable Geometric Prior and Recurrent Spiking Feature Learning for Humanoid Robot Manipulation","url":"https://arxiv.org/html/2601.09031v1"},{"title":"[2507.00833v1] HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/abs/2507.00833v1"},{"title":"HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/html/2507.00833"},{"title":"Vision-Language Models on the Edge for Real-Time Robotic Perception","url":"https://arxiv.org/pdf/2601.14921"},{"title":"Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions","url":"https://arxiv.org/html/2410.12773v1"},{"title":"Humanoid Robots and Humanoid AI: Review, Perspectives and Directions","url":"https://arxiv.org/html/2405.15775v2"}]

Based on the search results from arXiv, I found several papers related to humanoid data generation from April 2026 and nearby periods:

## Key Findings:

**Most Recent - April 2026:**

The most recent paper is "Visually-grounded Humanoid Agents," which introduces a coupled two-layer paradigm that enables digital humans to look, perceive, reason, and behave like real people in real-world 3D scenes. The approach reconstructs semantically rich 3D Gaussian scenes from real-world videos and transforms avatars into autonomous humanoid agents equipped with first-person RGB-D perception for embodied planning.

**Other Relevant Papers:**

Several other papers addressing humanoid data generation include:

- OmniRetarget, which presents an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves spatial and contact relationships between an agent, terrain, and manipulated objects.

- HumanoidGen, an automated task creation and demonstration collection framework that leverages atomic dexterous operations and LLM reasoning to generate relational constraints.

- Humanoid Everyday, a large-scale and diverse humanoid manipulation dataset that aggregates high-quality multimodal sensory data including RGB, depth, LiDAR, and tactile inputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "644e44a6-2757-4f51-9027-8537af3f859a",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "52345529-c2d6-4fed-b880-9d590b26f983",
  "sourceToolAssistantUUID": "644e44a6-2757-4f51-9027-8537af3f859a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-10T13:50:06.749Z_

<details><summary>↩ Tool result · `toolu_01PJqsgdXyeiq9MarhD6ZZqt`</summary>

```text
Web search results for query: "site:arxiv.org humanoid data generation May 2026"

Links: [{"title":"Hardware First, Brains Later? The Great American Humanoid Scale-Up of 2026 | Humanoids Daily","url":"https://www.humanoidsdaily.com/news/hardware-first-brains-later-the-great-american-humanoid-scale-up-of-2026"},{"title":"Humanoid robots 2026: The convergence moment | Roland Berger","url":"https://www.rolandberger.com/en/Insights/Publications/Humanoid-robots-why-the-convergence-moment-is-now.html"},{"title":"Will 2026 be the year of the Humanoid Robot?","url":"https://www.datapro.news/p/will-2026-be-the-year-of-the-humanoid-robot"},{"title":"Innovative Humanoid Robots in 2025–2026 - Reality or Hype?","url":"https://www.winssolutions.org/humanoid-robots-2025-2026-reality-hype/"},{"title":"Genesis AI Unveils GENE-26.5: A Full-Stack Play for the “Human-Level” Holy Grail | Humanoids Daily","url":"https://www.humanoidsdaily.com/news/genesis-ai-unveils-gene-26-5-a-full-stack-play-for-the-human-level-holy-grail"},{"title":"Top 12 Humanoid Robots of 2026 - Humanoid Robotics Technology","url":"https://humanoidroboticstechnology.com/articles/top-12-humanoid-robots-of-2026/"},{"title":"Which Humanoid Robots Launch in 2026? - Qviro Blog","url":"https://qviro.com/blog/humanoid-robots-launch-2026/"},{"title":"Physical AI and humanoid robots | Deloitte Insights","url":"https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/physical-ai-humanoid-robots.html"},{"title":"Humanoid Robots News | AI Breakthroughs, Robotics Trends & Synthetic Updates","url":"https://humanoid.press/"},{"title":"The gig workers who are training humanoid robots at home | MIT Technology Review","url":"https://www.technologyreview.com/2026/04/01/1134863/humanoid-data-training-gig-economy-2026-breakthrough-technology/"}]

I performed a web search for "humanoid data generation May 2026" and found several relevant results. Note that my search returned general results rather than specifically from arxiv.org, as the standard web search doesn't support the site-specific operator you requested.

Here are the key findings about humanoid data generation in May 2026:

**Data Generation Challenges and Solutions:**

The bottleneck in humanoid robotics is training data. A single humanoid robot deployed on a production line generates terabytes of high-dimensional data every hour: 3D point clouds from LiDAR, RGB-D video streams, tactile sensor data from force-sensitive grippers, joint-level telemetry, and IMU (inertial measurement unit) readings.

**Synthetic Data Generation Approaches:**

The "GROOT-Dreams" blueprint uses a single image and a language prompt to generate diverse 2D videos of future world states. These "dreams" are then translated into 3D action data using an Inverse Dynamics Model, and this synthetic data is filtered by high-level reasoning models to ensure physical accuracy before being used to train the robot's policy.

**Data Collection Infrastructure:**

Hyundai has established the Robot Metaplant Application Centre (RMAC) in the United States as a centralised hub for data collection, discovery, and performance validation. Before a robot is deployed to the Georgia EV megaplant (scheduled for 2028, with pilot testing throughout 2026), it undergoes intensive training at RMAC to learn specific tasks.

**Cost-Effective Data Collection:**

Genesis AI's new hardware for data collection is reportedly 100 times cheaper than existing teleoperation options and five times more efficient at data collection.

If you specifically need arxiv.org papers, you may want to search directly on arxiv.org's website with your specific query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af3774fa-181c-466e-9dd6-dc0540b86341",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "e793113a-53b0-4827-a838-9676572284f7",
  "sourceToolAssistantUUID": "af3774fa-181c-466e-9dd6-dc0540b86341",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-10T13:50:08.954Z_

Let me check the April 2026 paper and search for any papers specifically from late March to May 2026 that might match your technical focus.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e793113a-53b0-4827-a838-9676572284f7",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzhkDVupxdFWbasgjDj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b6417219-00fb-4af6-9ea6-09ae4859744c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PtR5USevJ7U9Vh9XGeLHaY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3179,
      "cache_read_input_tokens": 28406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3179,
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

_source line 44 · 2026-05-10T13:50:09.816Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CWfEvy7GKi86rnU5GerZBW`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.08509",
  "prompt": "What is the title, submission date, and main contributions? Does it involve demonstration generation, data synthesis, or the specific technical methods mentioned (SE(3), inverse reachability maps, combinatorial)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6417219-00fb-4af6-9ea6-09ae4859744c",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzhkDVupxdFWbasgjDj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a9241654-f00a-4163-94c2-e19944708ad0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PtR5USevJ7U9Vh9XGeLHaY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3179,
      "cache_read_input_tokens": 28406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3179,
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

_source line 45 · 2026-05-10T13:50:10.267Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CFCnRLXsxsqZCb8Yb7yhD5`</summary>

```json
{
  "query": "site:arxiv.org \"2604\" OR \"2605\" humanoid manipulation demonstration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9241654-f00a-4163-94c2-e19944708ad0",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzhkDVupxdFWbasgjDj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2025af9e-de3d-45d2-b614-8b68593672a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PtR5USevJ7U9Vh9XGeLHaY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3179,
      "cache_read_input_tokens": 28406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3179,
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

_source line 46 · 2026-05-10T13:50:10.450Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R3HP5xG84kcu3qjA1dsA2R`</summary>

```json
{
  "query": "site:arxiv.org humanoid \"data generation\" OR \"demo generation\" March April 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2025af9e-de3d-45d2-b614-8b68593672a3",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzhkDVupxdFWbasgjDj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a288777f-e630-44f9-8b25-b2a554a62e97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PtR5USevJ7U9Vh9XGeLHaY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3179,
      "cache_read_input_tokens": 28406,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3179
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 265,
          "cache_read_input_tokens": 28406,
          "cache_creation_input_tokens": 3179,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3179,
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

_source line 47 · 2026-05-10T13:50:13.588Z_

<details><summary>↩ Tool result · `toolu_01CWfEvy7GKi86rnU5GerZBW`</summary>

```text
# Paper Summary

**Title:** Visually-grounded Humanoid Agents

**Submission Date:** April 9, 2026

**Main Contributions:**

The research introduces a two-layer system enabling digital humans to autonomously behave in 3D environments. Key aspects include:

1. **World Layer:** Reconstructs "semantically rich 3D Gaussian scenes from real-world videos via an occlusion-aware pipeline" and incorporates animatable avatar representations.

2. **Agent Layer:** Equips avatars with "first-person RGB-D perception" and enables "accurate, embodied planning with spatial awareness and iterative reasoning."

**Regarding Your Specific Technical Questions:**

The abstract does not mention demonstration generation, data synthesis, SE(3) transformations, inverse reachability maps, or combinatorial methods. The paper focuses on visual grounding, 3D scene reconstruction, and embodied planning with goal-directed behavior in reconstructed environments. The authors indicate they will "open-source" their work and provide a benchmark for evaluating humanoid-scene interactions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9241654-f00a-4163-94c2-e19944708ad0",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "4389b059-b17a-432f-96ab-1207a5202e51",
  "sourceToolAssistantUUID": "a9241654-f00a-4163-94c2-e19944708ad0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-10T13:50:18.362Z_

<details><summary>↩ Tool result · `toolu_01R3HP5xG84kcu3qjA1dsA2R`</summary>

```text
Web search results for query: "site:arxiv.org humanoid "data generation" OR "demo generation" March April 2026"

Links: [{"title":"[2507.00833v1] HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/abs/2507.00833v1"},{"title":"DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning","url":"https://arxiv.org/html/2502.16932v1"},{"title":"HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/html/2507.00833v2"},{"title":"[2507.00833] HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning","url":"https://arxiv.org/abs/2507.00833"},{"title":"HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos","url":"https://arxiv.org/html/2602.02473v1"},{"title":"[2602.02473] HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos","url":"https://arxiv.org/abs/2602.02473"},{"title":"Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI","url":"https://arxiv.org/html/2407.06886v8"},{"title":"DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories","url":"https://arxiv.org/html/2505.12705v1"},{"title":"Humanoid-inspired Causal Representation Learning for Domain Generalization","url":"https://arxiv.org/html/2510.16382"},{"title":"HD-GEN: A High-Performance Software System for Human Mobility Data Generation Based on Patterns of Life","url":"https://arxiv.org/html/2601.01219v1"}]

I found several relevant papers on arxiv.org related to humanoid robots and data/demo generation. Here are the key results:

## Most Relevant Results:

1. **HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning**
   - An LLM-based framework capable of generating diverse manipulation tasks and collecting scalable demonstrations for humanoid robots
   - Includes a comprehensive benchmark called HGen-Bench for bimanual dexterous manipulation consisting of 20 tasks of varying difficulty levels, using the Unitree H1-2 humanoid robot equipped with Inspire hands
   - Paper ID: 2507.00833

2. **DemoGen: Synthetic Demonstration Generation for Data-Efficient Visuomotor Policy Learning**
   - Generates synthetic demonstrations by independently adapting the actions of both arms to the respective transformations of the objects
   - Demonstrates 90.8% success rate on bimanual humanoid platforms
   - Paper ID: 2502.16932

3. **HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos**
   - Integrates XGen, a data generation pipeline that synthesizes diverse and physically plausible robot interaction data from video while supporting scalable data augmentation
   - Successfully acquires 10 different skills and transfers them zero-shot to a physical Unitree G1 humanoid, including complex maneuvers such as pump-fake turnaround fadeaway jumpshots
   - Paper ID: 2602.02473 (published February 2, 2026)

These papers focus on automated and scalable approaches to generate training data and demonstrations for humanoid robots, addressing key challenges in dexterous manipulation and interactive skills learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a288777f-e630-44f9-8b25-b2a554a62e97",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "097f62ad-26c5-4a03-a0b1-a3783d009530",
  "sourceToolAssistantUUID": "a288777f-e630-44f9-8b25-b2a554a62e97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-10T13:50:18.732Z_

<details><summary>↩ Tool result · `toolu_01CFCnRLXsxsqZCb8Yb7yhD5`</summary>

```text
Web search results for query: "site:arxiv.org "2604" OR "2605" humanoid manipulation demonstration"

Links: [{"title":"[2604.13015] Learning Versatile Humanoid Manipulation with Touch Dreaming","url":"https://arxiv.org/abs/2604.13015"},{"title":"[2604.07993] HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation","url":"https://arxiv.org/abs/2604.07993"},{"title":"[2604.18557] SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy","url":"https://arxiv.org/abs/2604.18557"},{"title":"[2604.08534v1] ActiveGlasses: Learning Manipulation with Active Vision from Ego-centric Human Demonstration","url":"https://arxiv.org/abs/2604.08534v1"},{"title":"[2604.07335] TAMEn: Tactile-Aware Manipulation Engine for Closed-Loop Data Collection in Contact-Rich Tasks","url":"https://arxiv.org/abs/2604.07335"},{"title":"[2604.15013] DEX-Mouse: A Low-cost Portable and Universal Interface with Force Feedback for Data Collection of Dexterous Robotic Hands","url":"https://arxiv.org/abs/2604.15013"},{"title":"[2604.08508] Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation","url":"https://arxiv.org/abs/2604.08508"},{"title":"[2604.11447] Safe Human-to-Humanoid Motion Imitation Using Control Barrier Functions","url":"https://arxiv.org/abs/2604.11447"},{"title":"[2604.17513] FLASH: Fast Learning via GPU-Accelerated Simulation for High-Fidelity Deformable Manipulation in Minutes","url":"https://arxiv.org/abs/2604.17513"}]

The search has returned several recent arXiv papers on humanoid manipulation. Here are the key results:

1. **Learning Versatile Humanoid Manipulation with Touch Dreaming** (arXiv:2604.13015) - Studies dexterous, contact-rich humanoid loco-manipulation and develops an RL-based whole-body controller for stable lower-body and torso execution during complex manipulation. The method achieves a 90.9% relative improvement in average success rate over stronger baselines across five contact-rich tasks.

2. **HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation** (arXiv:2604.07993) - A state-centric framework for coordinated manipulation on full-sized bipedal humanoid robots. Experiments on real-world humanoid manipulation tasks show that HEX achieves state-of-the-art performance in task success rate and generalization, particularly in fast-reaction and long-horizon scenarios.

3. **SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy** (arXiv:2604.18557) - A unified framework that enables scalable and physically plausible cooperative manipulation by leveraging Solo-to-Cooperative Agent Synergy to transfer skills from single-agent human-object interaction to multi-agent human-object-human scenarios.

4. **Safe Human-to-Humanoid Motion Imitation Using Control Barrier Functions** (arXiv:2604.11447) - A vision-based framework that enables a humanoid robot to imitate human movements while avoiding collisions, where human skeletal keypoints are captured by a single camera and converted into joint angles for motion retargeting.

These papers from April 2026 represent recent advances in humanoid robot manipulation using learning-based approaches and imitation from human demonstrations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2025af9e-de3d-45d2-b614-8b68593672a3",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "3db9a2df-95aa-4b86-8b9b-1d9c00d4a9a5",
  "sourceToolAssistantUUID": "2025af9e-de3d-45d2-b614-8b68593672a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-10T13:50:20.136Z_

Let me fetch details on the most promising April-May papers to check for those specific technical contributions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3db9a2df-95aa-4b86-8b9b-1d9c00d4a9a5",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzidRzL4xytCpxAAQ6i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c0e8b480-ae43-4319-b0c3-27664e848ba4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SYCavLr3AyRijCEjxv2iCH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 951,
      "cache_creation_input_tokens": 1497,
      "cache_read_input_tokens": 31585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1497,
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

_source line 51 · 2026-05-10T13:50:21.045Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011NCQjT84tP35Dke17VrEwA`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.07993",
  "prompt": "What is the date, title, and main contributions? Does it mention SE(3), inverse reachability maps, object-centric encoding, or combinatorial data generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0e8b480-ae43-4319-b0c3-27664e848ba4",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzidRzL4xytCpxAAQ6i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bc5bb925-af44-4f48-8619-dd1a888e6091",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SYCavLr3AyRijCEjxv2iCH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 951,
      "cache_creation_input_tokens": 1497,
      "cache_read_input_tokens": 31585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1497,
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

_source line 52 · 2026-05-10T13:50:21.678Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0111QtaW7hYyZVmVy13UJj5z`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.18557",
  "prompt": "What is the date, title, and main contributions? Does it involve combinatorial or compositional data generation, transferring from solo to cooperative agents?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc5bb925-af44-4f48-8619-dd1a888e6091",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzidRzL4xytCpxAAQ6i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9a09096a-dffe-435a-ac83-34885c2de6b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SYCavLr3AyRijCEjxv2iCH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 951,
      "cache_creation_input_tokens": 1497,
      "cache_read_input_tokens": 31585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1497,
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

_source line 53 · 2026-05-10T13:50:22.105Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015wE54d856TGjQP3odgX3Cb`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.08508",
  "prompt": "What is the date, title, and main technical contributions? Does it involve data generation, inverse reachability, or combinatorial approaches?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a09096a-dffe-435a-ac83-34885c2de6b6",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzidRzL4xytCpxAAQ6i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4c8f5e42-ac52-428a-860b-3455c863a5ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SYCavLr3AyRijCEjxv2iCH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 951,
      "cache_creation_input_tokens": 1497,
      "cache_read_input_tokens": 31585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1497,
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

_source line 54 · 2026-05-10T13:50:22.415Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01R3fowpzPLnSjZueYwsf3uv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.02473",
  "prompt": "What is the date, title, and main contributions? Does it mention combinatorial data generation, demo multiplication, or data synthesis methods like XGen?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c8f5e42-ac52-428a-860b-3455c863a5ac",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzidRzL4xytCpxAAQ6i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe95a75f-64f7-439c-8099-0f67f4ba59d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SYCavLr3AyRijCEjxv2iCH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 951,
      "cache_creation_input_tokens": 1497,
      "cache_read_input_tokens": 31585,
      "output_tokens": 422,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1497
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 951,
          "output_tokens": 422,
          "cache_read_input_tokens": 31585,
          "cache_creation_input_tokens": 1497,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1497,
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

_source line 55 · 2026-05-10T13:50:25.283Z_

<details><summary>↩ Tool result · `toolu_011NCQjT84tP35Dke17VrEwA`</summary>

```text
# HEX Paper Summary

**Date:** Submitted April 9, 2026

**Title:** "HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation"

**Main Contributions:**

The paper introduces a framework addressing coordinated whole-body control for humanoid robots. Key innovations include:

1. **Humanoid-aligned universal state representation** enabling learning across different robot embodiments
2. **Mixture-of-Experts Unified Proprioceptive Predictor** that captures whole-body coordination and temporal motion patterns from multi-embodiment trajectory data
3. **Lightweight history tokens** to efficiently summarize past visual observations, reducing computational overhead during inference
4. **Residual-gated fusion mechanism with flow-matching action head** that integrates visual-language information with proprioceptive dynamics

The research demonstrates "state-of-the-art performance in task success rate and generalization" on real-world humanoid manipulation tasks.

**Regarding Your Specific Terms:**

The provided abstract does not mention SE(3), inverse reachability maps, object-centric encoding, or combinatorial data generation. These technical concepts may appear in the full paper, but they're absent from this webpage excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc5bb925-af44-4f48-8619-dd1a888e6091",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "c96aeb7e-0d37-46d9-84ea-d4089ffc28ad",
  "sourceToolAssistantUUID": "bc5bb925-af44-4f48-8619-dd1a888e6091",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-10T13:50:26.274Z_

<details><summary>↩ Tool result · `toolu_015wE54d856TGjQP3odgX3Cb`</summary>

```text
# Paper Summary: Sumo

**Date:** April 9-12, 2026 (submitted April 9, revised April 12)

**Title:** "Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation"

## Main Technical Contributions

The paper's core innovation involves using "test-time steering of a pre-trained whole-body control policy with a sample-based planner" to enable legged robots to perform dynamic manipulation tasks. Key aspects include:

1. **Sim-to-Real Approach:** The method bridges simulation and real-world deployment for physical manipulation

2. **Generalization:** The approach generalizes "to a diverse set of objects and tasks with no additional tuning or training," and supports flexible cost function adjustment at test time

3. **Real-World Demonstrations:** Successfully demonstrated on a Spot quadruped performing challenging tasks like uprighting heavy tires and moving large barriers

4. **Humanoid Extension:** Extended to humanoid robots in simulation for tasks like door opening and table pushing

## Regarding Your Specific Questions

The provided content does not mention data generation, inverse reachability, or combinatorial approaches as technical contributions. The emphasis is instead on policy steering, sample-based planning, and whole-body control generalization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c8f5e42-ac52-428a-860b-3455c863a5ac",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "5791930c-1713-4452-9206-9a52acae9c2e",
  "sourceToolAssistantUUID": "4c8f5e42-ac52-428a-860b-3455c863a5ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-10T13:50:26.774Z_

<details><summary>↩ Tool result · `toolu_0111QtaW7hYyZVmVy13UJj5z`</summary>

```text
# SynAgent Paper Summary

**Date:** April 20, 2026

**Title:** "SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy"

**Main Contributions:**

The research addresses cooperative humanoid manipulation through a novel transfer approach. Key contributions include:

1. **Solo-to-Cooperative Transfer:** The framework explicitly transfers skills from single-agent scenarios to multi-agent collaborative settings, directly answering your question about agent synergy transition.

2. **Interaction-Preserving Retargeting:** Uses "an Interact Mesh constructed via Delaunay tetrahedralization" to maintain spatial relationships between humans and objects during motion transfer, ensuring semantic integrity.

3. **Training Paradigm:** Implements single-agent pretraining bootstrapped from abundant single-human data, then applies decentralized training with multi-agent PPO for collaborative behaviors.

4. **Generative Policy:** Employs a conditional VAE with trajectory-conditioned control trained via multi-teacher distillation for stable object-level trajectory execution.

5. **Generalization:** Demonstrates performance across diverse object geometries, addressing the generalization challenge in cooperative manipulation.

The work combines data efficiency through transfer learning with compositional skill development from solo to cooperative scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a09096a-dffe-435a-ac83-34885c2de6b6",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "85fa1b13-da95-4959-b2a5-384a5ec2d5b6",
  "sourceToolAssistantUUID": "9a09096a-dffe-435a-ac83-34885c2de6b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-10T13:50:26.963Z_

<details><summary>↩ Tool result · `toolu_01R3fowpzPLnSjZueYwsf3uv`</summary>

```text
# Paper Summary

**Date:** February 2, 2026

**Title:** "HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos"

## Main Contributions

The research presents a framework addressing robot learning from human demonstrations. Key contributions include:

1. **XGen Component:** Described as "a data generation pipeline that synthesizes diverse and physically plausible robot interaction data from video" with support for scalable augmentation.

2. **XMimic Component:** A unified imitation learning system for acquiring transferable interaction skills.

3. **Practical Results:** The framework successfully enables a Unitree G1 humanoid to learn ten distinct skills across five domains (basketball, football, badminton, cargo pickup, reactive fighting) and transfer them to physical robots without task-specific rewards.

4. **Performance:** Achieves "over 8 times higher generalization success than prior methods," learning complex behaviors like fadeaway jumpshots and multi-cycle human-robot interactions from minimal video input.

The approach notably avoids explicit reward engineering, focusing instead on scalable video-to-robot skill transfer without external perception requirements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe95a75f-64f7-439c-8099-0f67f4ba59d6",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "dbbf48d9-aa4e-4889-bae6-907e1b8614b5",
  "sourceToolAssistantUUID": "fe95a75f-64f7-439c-8099-0f67f4ba59d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-10T13:50:28.442Z_

Now let me do one more targeted search to see if there are any papers from late March through May 2026 that explicitly mention the core technical innovations you're asking about:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbbf48d9-aa4e-4889-bae6-907e1b8614b5",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzjEeZQXvbPoQjYkcmF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ff2a7e3f-9b8d-4f52-9f51-439d6904890e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017CsX5pjdPDPJDod5NCuhfe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2570,
      "cache_read_input_tokens": 33082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2570,
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

_source line 60 · 2026-05-10T13:50:28.671Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DYMhKEjcSst9MG3Ab5ZKfQ`</summary>

```json
{
  "query": "site:arxiv.org 2603 2604 2605 humanoid retargeting data generation synthesis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff2a7e3f-9b8d-4f52-9f51-439d6904890e",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzjEeZQXvbPoQjYkcmF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "77cc12fb-3274-4c30-b30b-6df0654911c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017CsX5pjdPDPJDod5NCuhfe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2570,
      "cache_read_input_tokens": 33082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2570,
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

_source line 61 · 2026-05-10T13:50:28.944Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BmuhyJCR8ZrKopa2Cryev9`</summary>

```json
{
  "query": "site:arxiv.org humanoid \"navigation stance\" OR \"stance generation\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77cc12fb-3274-4c30-b30b-6df0654911c9",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzjEeZQXvbPoQjYkcmF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d45e6cff-f071-4597-a9b8-54417668b12c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017CsX5pjdPDPJDod5NCuhfe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2570,
      "cache_read_input_tokens": 33082,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2570
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 166,
          "cache_read_input_tokens": 33082,
          "cache_creation_input_tokens": 2570,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2570,
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

_source line 62 · 2026-05-10T13:50:32.842Z_

<details><summary>↩ Tool result · `toolu_01BmuhyJCR8ZrKopa2Cryev9`</summary>

```text
Web search results for query: "site:arxiv.org humanoid "navigation stance" OR "stance generation" 2026"

No links found.

I apologize, but the search didn't return any results. This could be because:

1. **No matching papers**: There may not be any papers on arXiv.org published in 2026 that combine the specific search terms about humanoid robots with "navigation stance" or "stance generation"

2. **Timing**: Since today's date is May 10, 2026, papers published later in 2026 may not yet be indexed or available

3. **Search operator limitation**: The search engine may have limitations with complex boolean queries using the "OR" operator on arXiv

If you're looking for related research, you might try:
- Searching without the year restriction (2026)
- Simplifying the search terms (e.g., just "humanoid stance" or "humanoid navigation")
- Checking arXiv directly with a slightly different query format

Would you like me to try a modified search query?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d45e6cff-f071-4597-a9b8-54417668b12c",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "254d2a81-4d25-427e-956b-092e2afb4c5a",
  "sourceToolAssistantUUID": "d45e6cff-f071-4597-a9b8-54417668b12c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-10T13:50:37.119Z_

<details><summary>↩ Tool result · `toolu_01DYMhKEjcSst9MG3Ab5ZKfQ`</summary>

```text
Web search results for query: "site:arxiv.org 2603 2604 2605 humanoid retargeting data generation synthesis"

Links: [{"title":"Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis","url":"https://arxiv.org/html/2603.19709v1"},{"title":"SPARK: Skeleton-Parameter Aligned Retargeting on Humanoid Robots with Kinodynamic Trajectory Optimization","url":"https://arxiv.org/html/2603.11480"},{"title":"Make Tracking Easy: Neural Motion Retargeting for Humanoid Whole-body Control","url":"https://arxiv.org/html/2603.22201v1"},{"title":"ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting","url":"https://arxiv.org/html/2605.06593"},{"title":"[2509.26633] OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/abs/2509.26633"},{"title":"SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy","url":"https://arxiv.org/html/2604.18557"},{"title":"Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking","url":"https://arxiv.org/html/2604.17335"},{"title":"OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction","url":"https://arxiv.org/html/2509.26633v2"},{"title":"Redefining Data Pairing for Motion Retargeting Leveraging a Human Body Prior","url":"https://arxiv.org/html/2409.13208v3"},{"title":"Chasing Autonomy: Dynamic Retargeting and Control Guided RL for Performant and Controllable Humanoid Running","url":"https://arxiv.org/html/2603.25902"}]

I found several relevant papers on arXiv from the 2603, 2604, and 2605 date ranges related to humanoid retargeting, data generation, and synthesis:

1. **SPARK: Skeleton-Parameter Aligned Retargeting on Humanoid Robots with Kinodynamic Trajectory Optimization** (2603.11480) - Presents a two-stage pipeline for generating natural and dynamically feasible motion references from task-space human data by converting human motion into a URDF-based skeleton representation and calibrating it to the target humanoid's dimensions.

2. **Make Tracking Easy: Neural Motion Retargeting for Humanoid Whole-body Control** (2603.22201) - Focuses on addressing the kinematic and dynamic embodiment gap from human data for humanoid robots.

3. **Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis** (2603.19709) - Proposes Dream2Act, a robot-centric framework that enables zero-shot interaction through generative video synthesis.

4. **Chasing Autonomy: Dynamic Retargeting and Control Guided RL for Performant and Controllable Humanoid Running** (2603.25902) - Presents a pipeline to dynamically retarget human motions through an optimization routine with hard constraints to generate improved periodic reference libraries from a single human demonstration.

5. **SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy** (2604.18557) - Introduces an interaction-preserving retargeting method based on an Interact Mesh constructed via Delaunay tetrahedralization, which maintains spatial relationships among humans and objects.

6. **Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking** (2604.17335) - Addresses whole-body humanoid locomotion challenges combining reference motion skills with terrain-aware adaptation.

7. **ReActor: Reinforcement Learning for Physics-Aware Motion Retargeting** (2605.06593) - Proposes a bilevel optimization framework that jointly adapts reference motions to a robot's morphology while training a tracking policy using reinforcement learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77cc12fb-3274-4c30-b30b-6df0654911c9",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "8ea21e3a-5b34-4b20-93bd-9685177593b6",
  "sourceToolAssistantUUID": "77cc12fb-3274-4c30-b30b-6df0654911c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-10T13:50:38.493Z_

Let me fetch details on the most relevant March-April papers to check for your specific technical contributions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ea21e3a-5b34-4b20-93bd-9685177593b6",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011Catzjz4VdCVRUiR8sSAjG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c96632aa-5f68-4acf-a404-be21a0d1f951",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019UyPZF9uzD11eW6otrydAi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 289,
      "cache_creation_input_tokens": 1342,
      "cache_read_input_tokens": 35652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1342,
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

_source line 65 · 2026-05-10T13:50:39.157Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HceBdzBxouiuHdxizJKGDg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.11480",
  "prompt": "What is the date, title, and main contributions? Does it mention inverse reachability, SE(3) encoding, or combinatorial data generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c96632aa-5f68-4acf-a404-be21a0d1f951",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011Catzjz4VdCVRUiR8sSAjG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "13e98f57-ef6e-4241-8708-81cd51731694",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019UyPZF9uzD11eW6otrydAi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 289,
      "cache_creation_input_tokens": 1342,
      "cache_read_input_tokens": 35652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1342,
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

_source line 66 · 2026-05-10T13:50:39.585Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NDRrocBZhs3Z6kt1vYZx1a`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.22201",
  "prompt": "What is the date, title, and main contributions? Does it address inverse reachability maps or combinatorial demonstration generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13e98f57-ef6e-4241-8708-81cd51731694",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011Catzjz4VdCVRUiR8sSAjG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "58adcc83-3bc5-4eba-995d-3ffb61ee5a31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019UyPZF9uzD11eW6otrydAi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 289,
      "cache_creation_input_tokens": 1342,
      "cache_read_input_tokens": 35652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1342,
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

_source line 67 · 2026-05-10T13:50:40.021Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018giyH84a2KMqY4sXY9srHG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.19709",
  "prompt": "What is the date, title, and main contributions? Does it involve data generation synthesis or combinatorial approaches?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58adcc83-3bc5-4eba-995d-3ffb61ee5a31",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011Catzjz4VdCVRUiR8sSAjG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "097b6338-4160-4500-ba6f-0b14e955cd26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019UyPZF9uzD11eW6otrydAi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 289,
      "cache_creation_input_tokens": 1342,
      "cache_read_input_tokens": 35652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1342,
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

_source line 68 · 2026-05-10T13:50:40.211Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01E5p2WwNdteRxqFhxk3Vj8v`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.17335",
  "prompt": "What is the date, title, and main contributions? Does it mention data generation, inverse reachability, or combinatorial demo generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "097b6338-4160-4500-ba6f-0b14e955cd26",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011Catzjz4VdCVRUiR8sSAjG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a7223a52-e3b4-4309-8a6f-1daeddffc13f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019UyPZF9uzD11eW6otrydAi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 289,
      "cache_creation_input_tokens": 1342,
      "cache_read_input_tokens": 35652,
      "output_tokens": 404,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1342
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 289,
          "output_tokens": 404,
          "cache_read_input_tokens": 35652,
          "cache_creation_input_tokens": 1342,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1342,
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

_source line 69 · 2026-05-10T13:50:43.346Z_

<details><summary>↩ Tool result · `toolu_01HceBdzBxouiuHdxizJKGDg`</summary>

```text
# SPARK Paper Summary

**Date:** March 12, 2026

**Title:** "SPARK: Skeleton-Parameter Aligned Retargeting on Humanoid Robots with Kinodynamic Trajectory Optimization"

**Main Contributions:**

The paper presents a two-stage pipeline for converting human motion to robot-compatible references:

1. **Skeleton Calibration:** Converting human motion to URDF format and aligning it with the target robot's dimensions, which "significantly reduces inverse kinematics error and tuning effort"

2. **Kinodynamic Trajectory Optimization:** A three-stage progressive approach (kinematic TO → inverse dynamics → full kinodynamic TO) that produces dynamically consistent trajectories and joint torque profiles

**Regarding Your Specific Questions:**

The abstract does **not mention** inverse reachability, SE(3) encoding, or combinatorial data generation. The focus is on skeleton alignment, URDF-based representation, and progressive trajectory optimization stages rather than these alternative approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13e98f57-ef6e-4241-8708-81cd51731694",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "724aa73e-b00f-419e-ac66-700b207ab134",
  "sourceToolAssistantUUID": "13e98f57-ef6e-4241-8708-81cd51731694",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-10T13:50:43.940Z_

<details><summary>↩ Tool result · `toolu_01E5p2WwNdteRxqFhxk3Vj8v`</summary>

```text
# Paper Summary

**Date:** April 19, 2026

**Title:** "Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking"

**Main Contributions:**

The research presents a framework combining two key components: (1) a diffusion model trained on human motions for "real-time prediction of terrain-aware reference motions," and (2) a reinforcement-learning-based whole-body tracker fine-tuned in closed-loop settings. The system enables "directional goal-reaching control with terrain-aware whole-body adaptation" on the Unitree G1 humanoid robot, with demonstrated success traversing varied terrain obstacles.

**Regarding Your Specific Questions:**

The abstract does **not** mention data generation techniques, inverse reachability, or combinatorial demo generation. The focus centers on motion generation via diffusion models and motion tracking through reinforcement learning rather than the methodologies you inquired about.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7223a52-e3b4-4309-8a6f-1daeddffc13f",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "5a1f6c9b-3d9b-4ddc-b9d1-03792e7e451f",
  "sourceToolAssistantUUID": "a7223a52-e3b4-4309-8a6f-1daeddffc13f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-10T13:50:44.155Z_

<details><summary>↩ Tool result · `toolu_01NDRrocBZhs3Z6kt1vYZx1a`</summary>

```text
# Paper Summary

**Date:** Submitted March 23, 2026; last revised April 30, 2026

**Title:** "Make Tracking Easy: Neural Motion Retargeting for Humanoid Whole-body Control"

## Main Contributions

The paper presents NMR (Neural Motion Retargeting), a framework addressing how humanoid robots can learn from human motion data despite kinematic differences. Key contributions include:

1. **Problem Analysis:** The authors demonstrate through Hessian analysis that "traditional optimization-based retargeting is inherently non-convex and prone to local optima"

2. **Clustered-Expert Physics Refinement (CEPR):** A hierarchical pipeline using VAE-based clustering to group diverse movements, reducing computational overhead while maintaining fidelity

3. **Architecture:** A non-autoregressive CNN-Transformer network that processes global temporal context to reduce reconstruction artifacts

4. **Results:** Testing on Unitree G1 humanoid shows the method "eliminates joint jumps and significantly reduces self-collisions" and accelerates downstream control policy convergence

## Regarding Your Specific Questions

The abstract does **not** mention inverse reachability maps or combinatorial demonstration generation. The focus remains on motion retargeting through learned distribution modeling rather than those alternative approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58adcc83-3bc5-4eba-995d-3ffb61ee5a31",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "d051bc26-2fcb-491b-bb3e-a85595f34048",
  "sourceToolAssistantUUID": "58adcc83-3bc5-4eba-995d-3ffb61ee5a31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-10T13:50:44.903Z_

<details><summary>↩ Tool result · `toolu_018giyH84a2KMqY4sXY9srHG`</summary>

```text
# Paper Summary

**Date:** Submitted March 20, 2026; revised March 24, 2026

**Title:** "Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis"

**Main Contributions:**

The paper introduces Dream2Act, a framework that enables humanoid robots to perform interaction tasks without extensive training or human motion retargeting. Key innovations include:

1. **Video Synthesis Approach:** Uses generative video models to envision robots completing tasks while maintaining physical consistency with their body structure.

2. **Morphology-Aware Design:** Operates within "robot-native coordinate space" to avoid skeletal mismatches that plague traditional human-to-robot retargeting methods.

3. **Zero-Shot Capability:** Recovers robot joint trajectories directly from synthesized videos, eliminating task-specific policy training requirements.

**Does it involve data generation or synthesis?**

Yes, significantly. The framework relies on **generative video synthesis** as its core mechanism. Rather than collecting real interaction data or training policies, it generates synthetic videos showing the robot performing desired tasks, then extracts feasible trajectories from these synthesized outputs. The paper demonstrates 37.5% success on whole-body mobile tasks compared to 0% for conventional retargeting approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "097b6338-4160-4500-ba6f-0b14e955cd26",
  "isSidechain": true,
  "promptId": "166d7398-ae3a-4f9d-8796-16cadc53629c",
  "agentId": "a9e83b823de4a4c2b",
  "type": "user",
  "uuid": "365c53e6-ef5d-473b-899b-94c28314297d",
  "sourceToolAssistantUUID": "097b6338-4160-4500-ba6f-0b14e955cd26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 73 · 2026-05-10T13:51:05.014Z_

Based on my comprehensive search, here's my detailed report on recent papers (2025-2026) on humanoid loco-manipulation demonstration generation:

## Summary of Findings

I conducted an exhaustive search across multiple arxiv queries and found **no papers from April-May 2026 that directly address all three of your specific technical contributions: SE(3) object-centric encoding for navigation stances, inverse reachability maps (IRM) for bipedal humanoid data generation, or combinatorial demo multiplication.**

However, I identified several competing and concurrent works in the humanoid loco-manipulation field published in 2025-2026:

---

## Key Competing/Concurrent Papers (Most Recent First)

### **April-May 2026 Papers** (Potential direct competitors)

1. **Learning Versatile Humanoid Manipulation with Touch Dreaming**
   - ArXiv: [2604.13015](https://arxiv.org/abs/2604.13015)
   - Date: April 14-27, 2026
   - Focus: Tactile-integrated whole-body manipulation with RL-based lower-body stabilization and VR data collection

2. **SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy**
   - ArXiv: [2604.18557](https://arxiv.org/abs/2604.18557)
   - Date: April 20, 2026
   - Focus: Transfer learning from single-agent to multi-agent manipulation; uses Interact Mesh for interaction-preserving retargeting

3. **HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation**
   - ArXiv: [2604.07993](https://arxiv.org/abs/2604.07993)
   - Date: April 9, 2026
   - Focus: Mixture-of-Experts unified state representation for cross-embodiment coordination

4. **Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation**
   - ArXiv: [2604.08508](https://arxiv.org/abs/2604.08508)
   - Date: April 9-12, 2026
   - Focus: Test-time steering with sample-based planning for dynamic manipulation on legged robots

5. **Visually-grounded Humanoid Agents**
   - ArXiv: [2604.08509](https://arxiv.org/abs/2604.08509)
   - Date: April 9, 2026
   - Focus: 3D scene reconstruction and embodied planning from real-world videos

6. **Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking**
   - ArXiv: [2604.17335](https://arxiv.org/abs/2604.17335)
   - Date: April 19, 2026
   - Focus: Diffusion-based motion generation + RL-based tracking for terrain-aware locomotion

### **March 2026 Papers** (Early data generation work)

7. **Make Tracking Easy: Neural Motion Retargeting for Humanoid Whole-body Control**
   - ArXiv: [2603.22201](https://arxiv.org/abs/2603.22201)
   - Date: March 23 - April 30, 2026
   - Focus: VAE-based clustered expert physics refinement for retargeting (non-convex optimization addressing)

8. **SPARK: Skeleton-Parameter Aligned Retargeting on Humanoid Robots with Kinodynamic Trajectory Optimization**
   - ArXiv: [2603.11480](https://arxiv.org/abs/2603.11480)
   - Date: March 12, 2026
   - Focus: Two-stage retargeting with skeleton calibration and kinodynamic optimization

9. **Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis**
   - ArXiv: [2603.19709](https://arxiv.org/abs/2603.19709)
   - Date: March 20-24, 2026
   - Focus: Generative video synthesis (Dream2Act) for morphology-aware task execution

10. **ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation**
    - ArXiv: [2603.03279](https://arxiv.org/abs/2603.03279)
    - Date: March 3, 2026
    - Focus: Physics-driven neural retargeting + unified multimodal controller for sparse task specs

11. **AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning**
    - ArXiv: [2603.20147](https://arxiv.org/abs/2603.20147)
    - Date: March 20, 2026
    - Focus: Sim-to-real workflow with environment verification and descriptor-driven deployment

12. **Ψ₀ (Psi-Zero): An Open Foundation Model Towards Universal Humanoid Loco-Manipulation**
    - ArXiv: [2603.12263](https://arxiv.org/abs/2603.12263)
    - Date: March 12, 2026
    - Focus: Staged training on human videos + robot data; achieves 40% improvement over baselines with 10× less data

### **Earlier 2026 / Late 2025 Papers** (Data generation focus)

13. **MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation**
    - ArXiv: [2510.18316](https://arxiv.org/abs/2510.18316)
    - Date: October 21, 2025 (accepted ICLR 2026)
    - Focus: **Constraint-based demo generation** addressing reachability constraints and visibility—closest to your "combinatorial" focus

14. **HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos**
    - ArXiv: [2602.02473](https://arxiv.org/abs/2602.02473)
    - Date: February 2, 2026
    - Focus: **XGen data generation pipeline** for synthesizing diverse interaction data from video with scalable augmentation

15. **EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration**
    - ArXiv: [2602.10106](https://arxiv.org/abs/2602.10106)
    - Date: February 10, 2026
    - Focus: Hybrid training with abundant egocentric human demos + limited robot data; 51% improvement over robot-only baselines

16. **OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction**
    - ArXiv: [2509.26633](https://arxiv.org/abs/2509.26633)
    - Date: September 26, 2025
    - Focus: **Interaction mesh-based data generation** explicitly modeling spatial/contact relationships between agent, terrain, and objects

17. **HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning**
    - ArXiv: [2507.00833](https://arxiv.org/abs/2507.00833)
    - Date: July 2025
    - Focus: LLM-based task generation and spatial constraint synthesis for scalable demo collection

---

## Critical Observation

**None of these papers explicitly use the technical framework you described:**
- **SE(3) object-centric encoding for navigation stances** - Not mentioned in any abstract/webpage
- **Inverse reachability maps (IRM) for bipedal humanoid data generation** - Zero hits in arxiv search
- **Combinatorial demo multiplication** - Only MoMaGen (2510.18316) addresses constraint-based combinatorial synthesis of demos

The closest papers to your technical approach are:
- **MoMaGen** (2510.18316) for constraint-based combinatorial generation
- **OmniRetarget** (2509.26633) for interaction-preserving geometric modeling
- **HumanX** (2602.02473) for XGen data synthesis pipeline

This suggests your specific technical contributions (SE(3) + IRM + combinatorial approach) may be **novel and not yet published** on arxiv as of May 10, 2026.

---

Sources:
- [Learning Versatile Humanoid Manipulation with Touch Dreaming](https://arxiv.org/abs/2604.13015)
- [SynAgent: Generalizable Cooperative Humanoid Manipulation](https://arxiv.org/abs/2604.18557)
- [HEX: Humanoid-Aligned Experts](https://arxiv.org/abs/2604.07993)
- [Sumo: Dynamic and Generalizable Whole-Body Loco-Manipulation](https://arxiv.org/abs/2604.08508)
- [Visually-grounded Humanoid Agents](https://arxiv.org/abs/2604.08509)
- [Learning Whole-Body Humanoid Locomotion](https://arxiv.org/abs/2604.17335)
- [Make Tracking Easy: Neural Motion Retargeting](https://arxiv.org/abs/2603.22201)
- [SPARK: Skeleton-Parameter Aligned Retargeting](https://arxiv.org/abs/2603.11480)
- [Morphology-Consistent Humanoid Interaction](https://arxiv.org/abs/2603.19709)
- [ULTRA: Unified Multimodal Control](https://arxiv.org/abs/2603.03279)
- [AGILE: A Comprehensive Workflow](https://arxiv.org/abs/2603.20147)
- [Psi-Zero: Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)
- [MoMaGen: Generating Demonstrations under Constraints](https://arxiv.org/abs/2510.18316)
- [HumanX: Agile Humanoid Interaction Skills](https://arxiv.org/abs/2602.02473)
- [EgoHumanoid: In-the-Wild Loco-Manipulation](https://arxiv.org/abs/2602.10106)
- [OmniRetarget: Interaction-Preserving Data Generation](https://arxiv.org/abs/2509.26633)
- [HumanoidGen: Data Generation via LLM](https://arxiv.org/abs/2507.00833)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "365c53e6-ef5d-473b-899b-94c28314297d",
  "isSidechain": true,
  "agentId": "a9e83b823de4a4c2b",
  "requestId": "req_011CatzkZNiGmDuGcoPdDry2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dde49528-8ed9-412f-8488-258865d7bea0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "69451f80-0e8d-489b-9ee7-0fc355d8e538",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Tqg5UEXmVCARqnTxrRxuyQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 235,
      "cache_creation_input_tokens": 1563,
      "cache_read_input_tokens": 36994,
      "output_tokens": 2604,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1563
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 235,
          "output_tokens": 2604,
          "cache_read_input_tokens": 36994,
          "cache_creation_input_tokens": 1563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1563,
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
