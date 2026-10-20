# Research conversation: You are Reviewer 2 (R2) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a0e120abbe8b3c778.jsonl`
- **Structured JSON:** [`978bf381b1a1f059a094.json`](../../sessions/97/978bf381b1a1f059a094.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

41 recorded events

### User

_source line 1 · 2026-05-18T11:42:03.564Z_

You are Reviewer 2 (R2) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 6=Strong Accept). Your focus is **Novelty and Related Work**.

## Paper Summary

**Title**: "Direction-Contrastive GRPO for Mitigating Multi-Turn Sycophancy While Preserving Belief Revision"

**Core idea**: Extract a linear "sycophancy direction" d_syc from a policy model's activation space using contrastive pairs (sycophantic vs genuine revision dialogues). Integrate this as a continuous reward in GRPO alongside NLI behavioral and rank-based contrastive rewards. Called DC-GRPO.

**Three contributions**:
1. d_syc direction discriminates capitulation from genuine revision (AUROC 0.831) on style-controlled data
2. DC-GRPO framework (R1 directional + R2 rank-based + R3 behavioral) with periodic recalibration
3. Empirical characterization of representation-behavioral disagreement (7.9% disagreement, 1.7% confirmed masked sycophancy)

**Related Work as presented** (Section 2, organized in 3 subsections):

*Sycophancy in LLMs*: Cites [5, 4] for documenting sycophancy across domains. SYCON Bench [2] for multi-turn. "Truth decay" [1]. Positions paper as targeting multi-turn specifically.

*Anti-sycophancy training*: Behavioral approaches using NLI reward decomposition [6]. BCT/ACT for activation consistency [7]. SMART for synthetic preference data [8]. Claims all treat opinion revision as uniformly undesirable.

*Representation-level interventions*: CRAFT [9] for hidden-state rewards in GRPO (domain-general prototype clustering, not task-specific directional). Linear probing [10] (Burns et al.) for binary sycophancy detection on reward model. "Sycophantic anchors" [12] and knowledge-prediction gap [11] for 13-29% representation-behavioral disagreement rates.

**References**: 12 total references. [1]-[12].

**Key positioning claims**:
- Existing methods treat all opinion changes as uniformly undesirable (the "double-bind")
- CRAFT uses domain-general clustering, not task-specific directional decomposition
- Linear probing collapses continuous structure to binary
- DC-GRPO is first to use directional decomposition of policy model activations as continuous GRPO reward for sycophancy

**Main results for context**:
| Model | NoF%↓ | WRR↑ | RC-AUC↑ | MT-B | MMLU |
|-------|-------|------|---------|------|------|
| Vanilla | 42.1 | 0.58 | 0.583 | 7.82 | 68.4 |
| R3-only | 32.7 | 0.62 | 0.671 | 7.71 | 68.1 |
| ACT-style | 33.9 | 0.57 | 0.628 | 7.59 | 67.6 |
| Binary Probe | 30.1 | 0.64 | 0.698 | 7.65 | 67.7 |
| DC-GRPO | 28.3 | 0.69 | 0.743 | 7.68 | 67.9 |

Statistical significance: DC-GRPO vs Binary Probe on NoF is p=0.189 (NOT significant), on RC-AUC is p=0.047 (borderline). DC-GRPO vs ACT on RC-AUC is p=0.008 (significant).

**Additional experiments**: Cross-model transfer (Llama-3-8B AUROC 0.792, cross-direction cosine 0.31), three-way design validation (d_gen vs d_syc cosine -0.72), R1-R3 disagreement analysis (7.9% total, 1.7% confirmed masked sycophancy with 39% R1 false positive rate).

## Your Review Task

Provide a detailed review focusing on:

1. **Novelty assessment** — How novel is each of the three contributions? Is the combination of existing techniques (linear probing + GRPO + NLI reward) a sufficient contribution? What is the actual delta over prior work like CRAFT [9], Burns et al. [10], and Li et al. [6]?
2. **Related work coverage** — Are key related works missing? Is the positioning fair? Are the distinctions from CRAFT and linear probing substantive or superficial?
3. **Framing and claims calibration** — Are claims appropriately scoped? The paper softens some claims (e.g., "moderate but consistent"). Is the framing honest?
4. **Contribution significance** — Given borderline results vs Binary Probe, is the directional decomposition's added complexity justified? Is this a sufficient contribution for a top venue?
5. **Writing quality** — Structure, clarity, any AI-writing artifacts

Format your output as:

### R2 Review: Novelty and Related Work

**Summary** (2-3 sentences)

**Strengths** (numbered list)

**Weaknesses** (numbered list)

**Questions for Authors** (numbered list)

**Minor Issues** (numbered list)

**Novelty**: X/4
**Significance**: X/4
**Overall Score**: X/6 (with label)
**Confidence**: X/5


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "5df26ae3-9d25-47ee-913f-514c05932b19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T11:42:03.566Z_

```json
{
  "parentUuid": "5df26ae3-9d25-47ee-913f-514c05932b19",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "660f7f0a-b0a5-419a-8c87-495829074f12",
  "timestamp": "2026-05-18T11:42:03.566Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T11:42:06.317Z_



I need to read the paper and related project files to provide a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "660f7f0a-b0a5-419a-8c87-495829074f12",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yQiEQHVkWgZ8GuzAst",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72d4b1b9-f85a-4b41-802d-b0a9589bbd65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fpHbFgZUSnvQnpzE9o9kC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8436,
      "cache_read_input_tokens": 8255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8436,
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

_source line 4 · 2026-05-18T11:42:06.453Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018c2WhEDSEmX1HNQsy5vjh2`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72d4b1b9-f85a-4b41-802d-b0a9589bbd65",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yQiEQHVkWgZ8GuzAst",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c2a49888-ceff-4480-9490-064355f4fe54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fpHbFgZUSnvQnpzE9o9kC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8436,
      "cache_read_input_tokens": 8255,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8436
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 106,
          "cache_read_input_tokens": 8255,
          "cache_creation_input_tokens": 8436,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8436,
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

_source line 5 · 2026-05-18T11:42:06.457Z_

<details><summary>↩ Tool result · `toolu_018c2WhEDSEmX1HNQsy5vjh2`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2a49888-ceff-4480-9490-064355f4fe54",
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "50e0f4c5-f05e-4003-99a9-02c9fb5039fe",
  "sourceToolAssistantUUID": "c2a49888-ceff-4480-9490-064355f4fe54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T11:42:08.667Z_



Let me read the paper and supporting project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50e0f4c5-f05e-4003-99a9-02c9fb5039fe",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yQvg1mnHbXUkZBaWBY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "687c2476-736c-4f3e-b6ff-6a08409a2d51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYP5kWrKEPHBUJNao13Jdh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1288,
      "cache_read_input_tokens": 16691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1288,
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

_source line 7 · 2026-05-18T11:42:10.165Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JtNCE4d2fhD9qVfkBFA2bk`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "687c2476-736c-4f3e-b6ff-6a08409a2d51",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yQvg1mnHbXUkZBaWBY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d553f554-ad0c-43df-8fda-0f827ce74f7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYP5kWrKEPHBUJNao13Jdh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1288,
      "cache_read_input_tokens": 16691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1288,
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

### Tool result

_source line 8 · 2026-05-18T11:42:10.176Z_

<details><summary>↩ Tool result · `toolu_01JtNCE4d2fhD9qVfkBFA2bk`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'contrastive_entrain_calib'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d553f554-ad0c-43df-8fda-0f827ce74f7a",
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "057a345d-5b8a-47f0-9959-f32182d01dc9",
  "sourceToolAssistantUUID": "d553f554-ad0c-43df-8fda-0f827ce74f7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T11:42:10.790Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LbCiu3dY2Q14GbSovs26z6`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "057a345d-5b8a-47f0-9959-f32182d01dc9",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yQvg1mnHbXUkZBaWBY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "152a6217-3544-4b47-9266-ae5311f302a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYP5kWrKEPHBUJNao13Jdh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1288,
      "cache_read_input_tokens": 16691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1288,
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

### Tool result

_source line 10 · 2026-05-18T11:42:10.800Z_

<details><summary>↩ Tool result · `toolu_01LbCiu3dY2Q14GbSovs26z6`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'contrastive_entrain_calib'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "152a6217-3544-4b47-9266-ae5311f302a4",
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "0af374d4-300b-46ff-810d-cc2a96a23344",
  "sourceToolAssistantUUID": "152a6217-3544-4b47-9266-ae5311f302a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T11:42:14.199Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Es4N5aXHwcAZ1ptahfZtMV`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0af374d4-300b-46ff-810d-cc2a96a23344",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yQvg1mnHbXUkZBaWBY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "85103aac-40a6-4957-9760-5675e30b583d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYP5kWrKEPHBUJNao13Jdh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1288,
      "cache_read_input_tokens": 16691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1288,
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

### Tool result

_source line 12 · 2026-05-18T11:42:14.216Z_

<details><summary>↩ Tool result · `toolu_01Es4N5aXHwcAZ1ptahfZtMV`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No report.md found for 'contrastive_entrain_calib'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85103aac-40a6-4957-9760-5675e30b583d",
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "90bc92a8-0ab6-4ce4-904d-1717a52d95fd",
  "sourceToolAssistantUUID": "85103aac-40a6-4957-9760-5675e30b583d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T11:42:14.354Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YKWN4ArBTLnPi3EjP3mAwH`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90bc92a8-0ab6-4ce4-904d-1717a52d95fd",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yQvg1mnHbXUkZBaWBY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f6fb61b1-a238-4209-bed1-c5a6c8caf6c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYP5kWrKEPHBUJNao13Jdh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1288,
      "cache_read_input_tokens": 16691,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1288,
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

### Tool result

_source line 14 · 2026-05-18T11:42:14.367Z_

<details><summary>↩ Tool result · `toolu_01YKWN4ArBTLnPi3EjP3mAwH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/ROADMAP.md\", \"content\": \"# contrastive_entrain_calib — Research Dashboard\\n\\n> 最后更新: 2026-05-18 11:03 UTC | 更新原因: Post-MVP kickoff: framing + plan 完成, Dream 启动, 进入 research 阶段\\n\\n## 核心方向\\nDirection-Contrastive GRPO (DC-GRPO)：用 policy model 自身激活空间中 sycophancy 方向性分解作为 GRPO reward 信号，使模型在多轮对话中抵抗 sycophantic capitulation 同时保留 genuine belief revision。详见 paper_framing.md。\\n\\n## 目标会议\\n- **主目标**: EACL 2027 via ARR August 2026（DDL: Aug 3, 2026，距今 ~11 周）\\n- **冲刺目标**: ICLR 2027（abstract ~Sep 2026）\\n\\n## 当前进展\\n- 阶段: **Research（post-MVP kickoff）**\\n- MVP: ✅ 通过（D007, 2026-05-18）\\n  - d_syc 捕获超越风格的认知信号（v2.1 Layer 0=random, L16-19 emergence, CV AUROC=0.826）\\n  - 三项 Go/No-Go 全部通过（AUROC=0.9985, Δlayer0=0.31, LoRA delta=0.0044）\\n- paper_framing.md: ✅ 已写（3 Core Claims）\\n- experiment_plan.yaml: ✅ 已写（13 experiments, P0-P2）\\n- Dream: ⏳ dream_20260518T110318 运行中（full review mode）\\n- GPU 已用: ~14h / 200h\\n- 服务器: westd-29046（RTX PRO 6000 × 2, cuda:0-1）\\n\\n## Core Claims（详见 paper_framing.md）\\n1. **Directional discriminability**: d_syc 在中层涌现，捕获认知信号\\n2. **DC-GRPO effectiveness**: 打破 sycophancy-revision double-bind\\n3. **Representation-level advantage**: R1 检测 behavioral reward 漏掉的 masked sycophancy\\n\\n## GPU 预算\\n| 类别 | 预估 GPU-hr | 备注 |\\n|------|-------------|------|\\n| MVP (已用) | 14 | 完成 |\\n| P0 mandatory | 128 | exp-001~006 |\\n| P1 important | 23 | exp-007~010 |\\n| P2 optional | 35 | exp-011~013 |\\n| Buffer | ~20 | |\\n| **总计** | **~186 / 200** | P2 视预算弹性裁剪 |\\n\\n## 近期任务\\n- [ ] 等待 Dream 完成，按审稿反馈调整 framing/plan\\n- [ ] exp-001: 扩展 v2.1 校准数据至 200 pairs（含 mixed evidence_strength）\\n- [ ] 搭建 DC-GRPO 训练框架（TRL 集成 + R1/R2/R3 reward）\\n- [ ] 搭建评估管线（SYCON Bench / SycophancyEval / MT-Bench / MMLU）\\n- [ ] exp-002 + exp-003: DC-GRPO 主实验 + R3-only baseline（可并行）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D007 | 2026-05-18 | MVP 最终 PASS：d_syc 确认捕获超越风格的认知信号，进入 research 阶段 | — |\\n| D006 | 2026-05-18 | Phase 5 v2 PASS (delta=0.0044)，三项 Go/No-Go 全部通过。但采 | — |\\n| D005 | 2026-05-18 | MVP v2 条件性 PASS：形式标准满足但 Turn 3 风格 confound 需 v2.1  | — |\\n| D004 | 2026-05-18 | MVP 不通过：AUROC=1.0 是输入文本差异的 trivial 结果，重新设计校准数据 | — |\\n| D003 | 2026-05-18 | Go/No-Go 从三条件简化为两条件（AUROC + LoRA），cosine 条件在二元设计下退 | — |\\n| D002 | 2026-05-18 | 采纳 Reviewer 4 项 MVP 改进：模型统一 Qwen3-8B、cosine<0.3 门槛 | — |\\n| D001 | 2026-05-18 | MVP 方案：多轮方向判别力测试（AUROC ≥ 0.85 为 go/no-go） | — |\\n\\n\\n\", \"total_chars\": 2284, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6fb61b1-a238-4209-bed1-c5a6c8caf6c8",
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "23adc48c-0fbc-4bb9-bb25-8cd27832e446",
  "sourceToolAssistantUUID": "f6fb61b1-a238-4209-bed1-c5a6c8caf6c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T11:42:17.203Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014FS45jBD4htRM252rUiyMM`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23adc48c-0fbc-4bb9-bb25-8cd27832e446",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yRWyWs9hY138pyNg5o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a587c817-46b3-43ca-890f-37cedb770908",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016GapwN4kf6MsDSnkN2Tpd4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2231,
      "cache_read_input_tokens": 17979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2231,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 16 · 2026-05-18T11:42:17.212Z_

<details><summary>↩ Tool result · `toolu_014FS45jBD4htRM252rUiyMM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md\", \"content\": \"# Paper Framing — contrastive_entrain_calib\\n\\n## Target Venue\\n- Primary: **EACL 2027** via ARR August 2026 cycle\\n- Deadline: **August 3, 2026** (submission), October 11, 2026 (commitment)\\n- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)\\n- Timeline: ~11 weeks from MVP completion (May 18 → Aug 3)\\n\\n## Core Claims (3 条, 可证伪)\\n\\n1. **Directional discriminability**: The policy model's own activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision in multi-turn dialogue, with signal emerging at mid-layers (L16-19) through model-internal factual assessment rather than surface text features.\\n   - *Evidence needed*: AUROC on style-controlled data (v2.1 expanded), layer progression analysis, transfer tests\\n   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence\\n\\n2. **DC-GRPO effectiveness**: Direction-Contrastive GRPO (using d_syc projection as reward component R1) reduces multi-turn sycophantic capitulation while preserving genuine belief revision, breaking the double-bind that undifferentiated anti-sycophancy training creates.\\n   - *Evidence needed*: Warranted Revision Rate + Unwarranted Capitulation Rate on SYCON Bench / SycophancyEval, compared to R3-only and ACT baselines\\n   - *Pass criterion*: DC-GRPO achieves lower NoF (capitulation) than R3-only AND higher warranted revision rate\\n\\n3. **Representation-level advantage**: R1 (directional projection reward) detects sycophantic internal reasoning that behavioral rewards (R3) miss, as evidenced by R1-R3 disagreement analysis where R1 correctly identifies cases of masked sycophancy.\\n   - *Evidence needed*: R1-R3 disagreement frequency > 5%, qualitative examples of masked sycophancy detection\\n   - *Fallback*: If disagreement < 5%, honest report as negative result about when representation-level rewards add value (still publishable as characterization)\\n\\n## Story Spine\\n\\n**Problem**: LLMs face a \\\"double-bind\\\" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes \\\"the user is right, I should revise\\\" from \\\"the user is pressuring me, I should resist.\\\"\\n\\n**Existing approaches & gaps**: Behavioral GRPO decomposition (\\\"Pressure, What Pressure?\\\") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.\\n\\n**Our framing**: We observe that the policy model's own activations encode geometrically separable directions for sycophantic vs. genuine agreement (building on \\\"Sycophancy Is Not One Thing\\\"). We extend this from measurement to training: d_syc projections serve as a continuous reward signal in GRPO, enabling the training process to directly target the internal mechanism of sycophancy rather than its surface manifestation. The multi-turn extension is non-trivial: commitment depth, attention decay across turns, and context-dependent sycophancy all require directions computed from multi-turn contrastive pairs rather than single-turn scenarios.\\n\\n**Headline result template**: \\\"On SYCON Bench, DC-GRPO reduces multi-turn sycophantic capitulation (NoF) by X% relative to behavioral-only GRPO while improving warranted revision rate by Y%, demonstrating that representation-level rewards can break the sycophancy-revision double-bind.\\\"\\n\\n## Venue Fit Risks\\n\\n- **EACL fit**: Strong. Combines mechanistic interpretability (Claim 1) with practical training method (Claim 2) for dialogue systems. EACL values NLP-focused work with linguistic/cognitive grounding.\\n- **Reviewer concern 1 (novelty)**: \\\"This is just CRAFT applied to sycophancy.\\\" Counter: (a) sycophancy-specific directional decomposition vs. prototype clustering is methodologically distinct; (b) multi-turn calibration and direction transfer are standalone contributions; (c) CRAFT doesn't distinguish sycophantic from genuine agreement.\\n- **Reviewer concern 2 (signal strength)**: \\\"AUROC ~0.82 on style-controlled data is moderate.\\\" Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) expanding data and adding mixed evidence strength should tighten CI.\\n- **Reviewer concern 3 (scale)**: \\\"Only Qwen3-8B.\\\" Counter: Budget constraint (200 H100-hr). If time/budget allows, add one more model family (e.g., Llama-3-8B). Cross-model direction transfer analysis partially addresses this.\\n- **Reviewer concern 4 (R2 degeneration)**: \\\"d_gen = -d_syc in binary design.\\\" Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.\\n- **Reviewer concern 5 (practical utility)**: \\\"Do models actually exhibit masked sycophancy at meaningful rates?\\\" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.\\n\\n## Anticipated Reviewer Concerns & Experimental Responses\\n\\n| Concern | Experiment | Priority |\\n|---------|-----------|----------|\\n| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |\\n| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |\\n| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |\\n| Binary probe is enough (no need for directional decomposition) | Binary Probe Penalty baseline | P1 |\\n| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |\\n| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |\\n| Single model, doesn't generalize | Cross-model direction transfer analysis (if budget allows) | P2 |\\n| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |\\n\", \"total_chars\": 6528, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a587c817-46b3-43ca-890f-37cedb770908",
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "40934c80-d914-482f-b4e3-2d619a299885",
  "sourceToolAssistantUUID": "a587c817-46b3-43ca-890f-37cedb770908",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T11:42:18.142Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HaeDNLCk7qHFdRRvExfGmt`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40934c80-d914-482f-b4e3-2d619a299885",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yRWyWs9hY138pyNg5o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "74b1d88c-9c11-4702-a894-fc14063f7ec5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016GapwN4kf6MsDSnkN2Tpd4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2231,
      "cache_read_input_tokens": 17979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2231,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 18 · 2026-05-18T11:42:18.153Z_

<details><summary>↩ Tool result · `toolu_01HaeDNLCk7qHFdRRvExfGmt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/decisions.yaml\", \"content\": \"_next_id: 8\\ndecisions:\\n- id: D001\\n  date: 2026-05-18 04:50 UTC\\n  summary: MVP 方案：多轮方向判别力测试（AUROC ≥ 0.85 为 go/no-go）\\n  rationale: DC-GRPO 的核心假设是多轮场景下 d_syc/d_gen 方向能区分 sycophantic capitulation vs. genuine\\n    revision。这是整个方法的根基——如果方向判别力不足（AUROC < 0.85），后续 GRPO 训练的 reward 信号就不可靠。MVP 只需 forward\\n    pass（~4-8 GPU hours），不需要 GRPO 训练（180+ hours），是最小成本的假设验证。Phase 1（数据构建）无需 GPU 可立即启动。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-18 04:53 UTC\\n  summary: 采纳 Reviewer 4 项 MVP 改进：模型统一 Qwen3-8B、cosine<0.3 门槛、LoRA 扰动检查、数据质量验证\\n  rationale: Reviewer 审查 D001 提出 4 个 warning：(1) MVP 不验证训练稳定性 → 加 Phase 5 LoRA 扰动检查(<1h\\n    GPU)；(2) 校准数据无独立验证 → 加 Phase 1.5 抽样质量校验；(3) 模型不一致(Qwen2.5-7B vs Qwen3-8B) → 统一用\\n    Qwen3-8B；(4) 交叉选择性无数值门槛 → cosine(d_syc,d_gen)<0.3。另采纳 AUROC 灰色区间建议(0.80-0.85 →\\n    调查再决定, <0.80 → 立即 pivot)。全部改动成本极低(+1 GPU hour + 数据审查)，风险显著降低。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-18 06:44 UTC\\n  summary: Go/No-Go 从三条件简化为两条件（AUROC + LoRA），cosine 条件在二元设计下退化\\n  rationale: Reviewer 发现 compute_directions.py 中 d_gen = mean(revision) - mean(capitulation)\\n    = -d_syc，cosine(d_syc, d_gen) 恒等于 -1.0。根因：校准数据只有两个条件（warranted_revision vs sycophantic_capitulation），无中性\\n    baseline。\\\"Sycophancy Is Not One Thing\\\" 用三组对比得到独立方向，当前二元设计数学上只能产生一个方向及其反向。cosine\\n    < 0.3 条件 trivially satisfied，从实质 gate 中移除。MVP go/no-go 实质由 AUROC ≥ 0.85 + LoRA\\n    AUROC drop < 0.05 两项决定，判别力仍由 AUROC 检验。Post-MVP 如需论文 claim cross-selectivity，需增加\\n    neutral baseline 第三条件。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-18 09:15 UTC\\n  summary: MVP 不通过：AUROC=1.0 是输入文本差异的 trivial 结果，重新设计校准数据\\n  rationale: Reviewer critical 发现：(1) asst_first AUROC 从 Layer 0 即达 0.998，说明信号在 embedding（输入文本差异），不在模型学到的表示中；(2)\\n    两条件从 Turn 2 开始完全不同（错答案 vs 正确答案 + 纠正 vs 施压），trivially distinguishable；(3) sycophantic_capitulation\\n    条件中模型实际表现为 resistance 而非 capitulation，d_syc 编码的是\\\"场景类型\\\"而非\\\"sycophancy 内部状态\\\"。根本原因：校准数据\\n    Turn 2 在两条件间不同（wrong answer vs correct answer），导致从该点起所有激活都包含不可控的文本差异 confound。修正方案：重新设计校准数据，两条件共享\\n    Turn 1-2（同一问题 + 同一错误回答），仅 Turn 3 不同（valid correction vs invalid pressure），最小化输入差异。新\\n    MVP gate 增加：Layer 0 AUROC 显著低于 best-layer AUROC（排除 embedding-level confound）。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-18 10:25 UTC\\n  summary: MVP v2 条件性 PASS：形式标准满足但 Turn 3 风格 confound 需 v2.1 跟进\\n  rationale: v2 Go/No-Go 形式标准：AUROC 0.9985 (≥0.85 ✅)、Δ(best-layer0) 0.3088 (≥0.15\\n    ✅)、LoRA pending。层级爬升 Layer 0(0.69)→L8(0.90)→L16(0.99)→L27(0.9985) 证明方向信号不是 v1\\n    式 trivial confound。但 Turn 3 blind classification 100% 揭示风格差异（\\\"Actually...\\\" vs\\n    \\\"I think...\\\"、真实vs虚构来源、自信vs含糊语气）。事实层 confound 固有且期望（模型应区分正确/错误信息），风格层 confound\\n    可修复。决策：MVP 条件性通过（pending Phase 5），v2.1（严格 Turn 3 风格匹配）作为 research 阶段第一优先级。v2.1\\n    结果决定论文 claim 强度：AUROC 保持 → 强 claim（方向捕捉证据质量评估）；AUROC 显著下降 → 方向主要捕捉风格差异，论文需诚实 framing。\\n  related_experiments: []\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-18 10:30 UTC\\n  summary: Phase 5 v2 PASS (delta=0.0044)，三项 Go/No-Go 全部通过。但采纳 Reviewer 建议：在 complete_mvp()\\n    前增加 v2.1 风格控制 ablation 作为 MVP 最终门槛\\n  rationale: LoRA perturbation delta=0.0044 远低于 0.05 阈值，d_syc 方向在随机扰动下稳定。但 Reviewer\\n    正确指出：(1) LoRA robustness 不区分\\\"稳定的风格检测器\\\"和\\\"稳定的认知信号\\\"；(2) Turn 3 blind classification\\n    100% 意味着 d_syc 可能仅编码文本风格特征而非模型对事实正确性的内部表征；(3) 若 d_syc 是风格分类器，DC-GRPO reward 基础不成立。Reviewer\\n    方案 A（~50 对风格控制数据 + blind test + AUROC）成本极低（~3h），能彻底回答\\\"d_syc 捕获的是什么\\\"。在此之前 complete_mvp()\\n    风险过高——可能在错误前提上构建整个研究计划。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-18 10:59 UTC\\n  summary: MVP 最终 PASS：d_syc 确认捕获超越风格的认知信号，进入 research 阶段\\n  rationale: v2.1 风格控制 ablation 证据链：(1) Layer 0 AUROC ≈ 0.51（随机），embedding confound\\n    彻底消除；(2) 信号在 L16-19 突变（0.51→0.73），典型中层语义 emergence；(3) asst_first 高层稳定 0.74-0.77；(4)\\n    v2→v2.1 transfer AUROC 0.77，v2 方向不是纯风格分类器；(5) v2.1 自身 5-fold CV AUROC 0.826±0.054。MVP\\n    核心问题\\\"激活空间中是否存在捕获 sycophancy 认知信号的方向\\\"已明确回答 YES。0.826 vs 0.85 阈值差异不构成 NO-GO：阈值针对含风格\\n    confound 的 v2 设定，v2.1 是纯认知信号且全部 weak evidence_strength（最难条件）；DC-GRPO 不需要完美分类，AUROC\\n    0.82 足以提供 reward gradient。数据扩展（150-200 pairs + mixed evidence_strength）作为 research\\n    阶段首要任务以获得更紧的 CI。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n\", \"total_chars\": 4215, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74b1d88c-9c11-4702-a894-fc14063f7ec5",
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "b3e216ee-b6a6-4477-ae3b-a44d6ffa1293",
  "sourceToolAssistantUUID": "74b1d88c-9c11-4702-a894-fc14063f7ec5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T11:42:18.601Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SZgDmCuAda1HXro2pK3e1E`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3e216ee-b6a6-4477-ae3b-a44d6ffa1293",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yRWyWs9hY138pyNg5o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6c5439d-9f84-40c5-87bb-bc9411b1dd57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016GapwN4kf6MsDSnkN2Tpd4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2231,
      "cache_read_input_tokens": 17979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2231,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 20 · 2026-05-18T11:42:18.618Z_

<details><summary>↩ Tool result · `toolu_01SZgDmCuAda1HXro2pK3e1E`</summary>

```text
artifacts/dream_reports/dream_20260518T110318/best/paper.tex
artifacts/dream_reports/dream_20260518T110318/median/paper.tex
artifacts/dream_reports/dream_20260518T110318/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6c5439d-9f84-40c5-87bb-bc9411b1dd57",
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "1ce13065-761a-499f-9302-f704a37c7f0d",
  "sourceToolAssistantUUID": "e6c5439d-9f84-40c5-87bb-bc9411b1dd57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T11:42:19.087Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QdWCLSG31EZmtaww54kZof`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ce13065-761a-499f-9302-f704a37c7f0d",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yRWyWs9hY138pyNg5o",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd9ba0b0-3c1d-4bd7-8717-77d9920576d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016GapwN4kf6MsDSnkN2Tpd4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2231,
      "cache_read_input_tokens": 17979,
      "output_tokens": 378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2231
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 378,
          "cache_read_input_tokens": 17979,
          "cache_creation_input_tokens": 2231,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2231,
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

_source line 22 · 2026-05-18T11:42:19.104Z_

<details><summary>↩ Tool result · `toolu_01QdWCLSG31EZmtaww54kZof`</summary>

```text
mistakes.yaml
artifacts/manifest.yaml
decisions.yaml
experiment_plan.yaml
artifacts/dream_reports/dream_20260518T110318/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260518T110318/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260518T110318/worst/imagined_experiments.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260518T110318/best/review_context.yaml
artifacts/dream_reports/dream_20260518T110318/median/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd9ba0b0-3c1d-4bd7-8717-77d9920576d7",
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "b0c5c793-ee25-4faf-a2ff-9323167737d9",
  "sourceToolAssistantUUID": "bd9ba0b0-3c1d-4bd7-8717-77d9920576d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T11:42:21.655Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SJZHqtETUcEuXqjQcU1FFC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0c5c793-ee25-4faf-a2ff-9323167737d9",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yRs8UD44PAbqsV1Pcn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5272c64-0d2a-4e8e-924a-113d4b8e7690",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S6CFQ4wpPh7CXu1N8uPtku",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5472,
      "cache_read_input_tokens": 20210,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5472
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 20210,
          "cache_creation_input_tokens": 5472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5472,
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

_source line 24 · 2026-05-18T11:42:21.955Z_

<details><summary>↩ Tool result · `toolu_01SJZHqtETUcEuXqjQcU1FFC`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=2.5cm]{geometry}
3	\usepackage{times}
4	\usepackage{booktabs}
5	\usepackage{amsmath}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage{amssymb}
11	
12	\newcommand{\dsyc}{$d_{\mathrm{syc}}$}
13	\newcommand{\dgen}{$d_{\mathrm{gen}}$}
14	
15	\title{Direction-Contrastive GRPO for Mitigating Multi-Turn Sycophancy\\While Preserving Belief Revision}
16	
17	\author{Anonymous}
18	
19	\begin{document}
20	\maketitle
21	
22	\begin{abstract}
23	Large Language Models (LLMs) in multi-turn dialogue face a tension between resisting sycophantic capitulation and accepting legitimate belief revision. Existing anti-sycophancy methods penalize all opinion changes indiscriminately, suppressing both unwarranted agreement and warranted correction. We show that a policy model's own activation space encodes a linear direction \dsyc{} that separates sycophantic capitulation from genuine revision, with discriminative signal emerging at mid-layers (AUROC = 0.831, 95\% CI [0.802, 0.858] on style-controlled data). Building on this finding, we propose Direction-Contrastive Group Relative Policy Optimization (DC-GRPO), which integrates \dsyc{} projections as a continuous reward signal alongside behavioral and contrastive components. On the SYCON Bench multi-turn evaluation, DC-GRPO reduces unwarranted capitulation to 28.3\% (from 42.1\% vanilla) while achieving a Revision-Capitulation AUC of 0.743, compared to 0.671 for behavioral-only GRPO and 0.628 for activation-consistency training. An analysis of representation-behavioral disagreement reveals that the directional reward identifies a small but real subset of masked sycophancy cases (1.7\% of responses) invisible to behavioral metrics alone. These results demonstrate that representation-level rewards offer moderate but consistent improvements in navigating the sycophancy-revision trade-off.
24	\end{abstract}
25	
26	\section{Introduction}
27	
28	Anti-sycophancy training creates a tension that current methods leave unresolved. When an LLM is trained to resist user pressure in dialogue, it must simultaneously learn two opposing skills: standing firm against unwarranted persuasion and revising its position when presented with valid evidence. This ``double-bind'' is not merely theoretical. Multi-turn commitment compounds the problem, as models that initially agree with incorrect user claims become progressively locked in across subsequent turns, with accuracy degradation reaching up to 47\% in extended conversations \cite{truthdecay}.
29	
30	The tension matters because real-world dialogue routinely requires both capabilities. A medical AI assistant must resist a patient's insistence on an incorrect self-diagnosis while updating its assessment when the patient provides new symptoms. A coding assistant must push back on flawed design choices while incorporating valid corrections. Existing benchmarks such as SYCON Bench \cite{syconbench} and SycophancyEval \cite{sycophancyeval} document the problem at scale, but training methods that reduce sycophancy tend to produce models that are uniformly stubborn.
31	
32	Current approaches attack sycophancy at the behavioral level. Behavioral GRPO decomposition scores outputs via Natural Language Inference (NLI) to detect opinion changes \cite{pressurewhatpressure}, but cannot distinguish sycophantic internal reasoning from genuine revision when the surface output appears correct. Activation Consistency Training (ACT) enforces undifferentiated consistency across clean and biased prompts \cite{act}, penalizing all activation changes equally. Linear probe methods train binary classifiers on reward model activations \cite{linearprobes}, but operate on the reward model rather than the policy model and collapse the signal to a binary decision.
33	
34	We observe that the policy model's own activations encode geometrically separable directions for sycophantic versus genuine agreement, building on findings that sycophancy manifests as a structured phenomenon in representation space \cite{sycnotone}. Concretely, we extract a linear direction \dsyc{} from contrastive activation pairs and use its projection as a continuous reward component in Group Relative Policy Optimization (GRPO). This representation-level signal provides gradient information that behavioral rewards cannot: it targets the internal mechanism of sycophancy rather than its surface manifestation. The multi-turn setting requires directions computed from multi-turn contrastive pairs, with periodic recalibration to track representation drift during training.
35	
36	Our contributions are as follows:
37	\begin{itemize}
38	\item We demonstrate that a linear sycophancy direction \dsyc{} discriminates capitulation from genuine revision with AUROC 0.831 on expanded, style-controlled calibration data (200 pairs across three evidence-strength levels), with signal emerging at mid-layers and degrading gracefully as evidence strength increases (Section~\ref{sec:calibration}).
39	\item We propose DC-GRPO, a three-component reward framework (directional projection R1, rank-based contrastive R2, NLI behavioral R3) with periodic direction recalibration, and show it achieves consistent improvements over behavioral-only and activation-consistency baselines across multiple metrics (Section~\ref{sec:main_results}).
40	\item We provide an empirical characterization of representation-behavioral disagreement in sycophancy assessment, finding 7.9\% overall disagreement and 1.7\% confirmed masked sycophancy that behavioral rewards miss (Section~\ref{sec:disagreement}).
41	\end{itemize}
42	
43	\section{Related Work}
44	
45	\paragraph{Sycophancy in LLMs.}
46	Sycophancy in LLMs has been documented across factual, analytical, and preference domains \cite{sycnotone,sharma2024sycophancy}. Multi-turn settings amplify the problem: SYCON Bench \cite{syconbench} shows that commitment across dialogue turns leads to compounding accuracy loss. The ``truth decay'' phenomenon describes how models progressively abandon correct positions under sustained user pressure \cite{truthdecay}. Our work targets the multi-turn setting specifically, using contrastive pairs that capture commitment dynamics across turns.
47	
48	\paragraph{Anti-sycophancy training.}
49	Several training-time interventions have been proposed. Behavioral approaches use NLI-based reward decomposition to penalize opinion flips during reinforcement learning \cite{pressurewhatpressure}. BCT and ACT enforce activation consistency between prompted and unprompted conditions \cite{act}, but do not distinguish sycophantic from genuine activation changes. SMART uses synthetic preference data with explicit sycophancy labels \cite{smart}. All these methods treat opinion revision as uniformly undesirable, which our experiments show suppresses warranted belief revision alongside unwarranted capitulation.
50	
51	\paragraph{Representation-level interventions.}
52	CRAFT validates that hidden-state rewards in GRPO improve safety alignment \cite{craft}, but uses domain-general prototype clustering rather than task-specific directional decomposition. Linear probing of reward model activations provides binary sycophancy detection \cite{linearprobes}, but collapses the continuous structure of the representation space. Work on ``sycophantic anchors'' and the knowledge-prediction gap documents 13--29\% rates of representation-behavioral disagreement \cite{knowledgegap,sycanchors}, motivating our investigation of when directional rewards add value beyond behavioral signals.
53	
54	\section{Method}
55	\label{sec:method}
56	
57	\subsection{Sycophancy Direction Extraction}
58	
59	We extract a linear sycophancy direction \dsyc{} from the policy model's activation space using contrastive pairs of multi-turn dialogues. Each pair consists of a dialogue where the model capitulates to user pressure (sycophantic) and a matched dialogue where the model genuinely revises its position based on evidence (genuine revision), with surface style controlled to isolate the cognitive signal.
60	
61	Given a set of $N$ contrastive pairs $\{(\mathbf{h}_i^{\mathrm{syc}}, \mathbf{h}_i^{\mathrm{gen}})\}_{i=1}^{N}$ where $\mathbf{h}_i^{\mathrm{syc}}, \mathbf{h}_i^{\mathrm{gen}} \in \mathbb{R}^d$ are hidden-state activations at layer $\ell$, the sycophancy direction is computed as the first principal component of the difference vectors:
62	\begin{equation}
63	    d_{\mathrm{syc}} = \mathrm{PCA}_1\left(\left\{\mathbf{h}_i^{\mathrm{syc}} - \mathbf{h}_i^{\mathrm{gen}}\right\}_{i=1}^{N}\right)
64	\end{equation}
65	
66	The calibration data spans three evidence-strength levels (weak, medium, strong) to ensure the direction captures the cognitive distinction rather than evidence quality. Style control removes confounds such as hedging language, response length, and politeness markers.
67	
68	\subsection{DC-GRPO Reward Design}
69	
70	DC-GRPO uses three complementary reward components within the GRPO framework:
71	
72	\paragraph{R1: Directional projection reward.} For a response with hidden-state $\mathbf{h}$ at layer $\ell$, the directional reward is:
73	\begin{equation}
74	    R_1(\mathbf{h}) = -\sigma\left(\alpha \cdot \mathrm{proj}_{d_{\mathrm{syc}}}(\mathbf{h})\right)
75	\end{equation}
76	where $\mathrm{proj}_{d_{\mathrm{syc}}}(\mathbf{h}) = \frac{\mathbf{h} \cdot d_{\mathrm{syc}}}{\|d_{\mathrm{syc}}\|}$ is the scalar projection, $\sigma$ is the sigmoid function, and $\alpha$ is a temperature parameter. Higher projections along \dsyc{} indicate more sycophantic activations, so the reward is negated.
77	
78	\paragraph{R2: Rank-based contrastive reward.} For a group of $K$ sampled responses $\{y_1, \ldots, y_K\}$ to the same prompt, R2 assigns rewards based on the rank ordering of their \dsyc{} projections:
79	\begin{equation}
80	    R_2(y_j) = 1 - \frac{2 \cdot \mathrm{rank}_j}{K+1}
81	\end{equation}
82	where $\mathrm{rank}_j$ is the rank of $y_j$ by ascending \dsyc{} projection (lower projection = less sycophantic = higher reward). This rank-based design avoids the need for an independent genuine-revision direction \dgen{}.
83	
84	\paragraph{R3: NLI behavioral reward.} Following prior work \cite{pressurewhatpressure}, R3 uses an NLI model to score whether the response maintains factual consistency with the model's initial position when user pressure is unwarranted, and permits revision when evidence supports it.
85	
86	The combined reward is:
87	\begin{equation}
88	    R = w_1 R_1 + w_2 R_2 + w_3 R_3
89	\end{equation}
90	with weights $w_1 = 0.3$, $w_2 = 0.2$, $w_3 = 0.5$, reflecting R3's role as the primary behavioral constraint and R1/R2 as complementary representation-level signals.
91	
92	\subsection{Periodic Recalibration}
93	
94	Since LoRA fine-tuning alters the policy model's representation space, the sycophancy direction \dsyc{} drifts during training. We monitor this drift by computing the cosine similarity between the current direction and the initial direction at regular intervals. When cosine similarity drops below a threshold $\tau = 0.75$, we recompute \dsyc{} from fresh calibration data generated by the current policy checkpoint. This mechanism is analogous to target network updates in deep Q-learning: the reward signal must track the evolving representation space to remain informative.
95	
96	\section{Experimental Setup}
97	
98	\paragraph{Model and training.} We use Qwen3-8B as the base model with LoRA (rank 64) fine-tuning. DC-GRPO training runs for 6,000 steps with recalibration triggered at steps 2,500 and 4,500. Total GPU budget is 52 hours on H100.
99	
100	\paragraph{Calibration data.} We construct 200 style-controlled contrastive pairs (80 weak-evidence, 60 medium-evidence, 60 strong-evidence) using GPT-4o as the generation backbone, with manual quality filtering. The expanded dataset costs \$14.50 in API calls and 2.1 GPU hours for direction extraction.
101	
102	\paragraph{Baselines.} We compare against four baselines: (1) \textbf{Vanilla}: the unmodified Qwen3-8B; (2) \textbf{R3-only}: GRPO with only the NLI behavioral reward, identical training configuration; (3) \textbf{ACT-style}: L2 activation consistency loss between clean and biased prompt conditions; (4) \textbf{Binary Probe}: a binary linear probe on policy activations used as reward, replacing the directional projection.
103	
104	\paragraph{Evaluation.} We report: SYCON Bench multi-turn NoF\% (unwarranted capitulation, lower is better) and ToF\% (warranted firmness); SycophancyEval single-turn sycophancy rate; Warranted Revision Rate (proportion of evidence-supported revisions, higher is better); Revision-Capitulation AUC (area under the revision vs. capitulation trade-off curve, higher is better); MT-Bench and MMLU as general capability checks.
105	
106	\section{Results}
107	
108	\subsection{Sycophancy Direction Discriminability}
109	\label{sec:calibration}
110	
111	Table~\ref{tab:auroc_layer} reports the AUROC of \dsyc{} across layers and evidence-strength conditions. The direction achieves 0.831 combined AUROC (95\% CI [0.802, 0.858]) at layer 19 on the expanded 200-pair dataset. The layer progression shows a clear emergence pattern: near-random at layer 0 (0.52), rising through layer 8 (0.61) and layer 16 (0.78) to peak at layer 19, with mild decay thereafter.
112	
113	\begin{table}[t]
114	\centering
115	\small
116	\begin{tabular}{lcccc}
117	\toprule
118	\textbf{Layer} & \textbf{Weak} & \textbf{Medium} & \textbf{Strong} & \textbf{Combined} \\
119	\midrule
120	0  & 0.530 & 0.510 & 0.500 & 0.520 \\
121	8  & 0.640 & 0.590 & 0.570 & 0.610 \\
122	16 & 0.820 & 0.760 & 0.720 & 0.780 \\
123	19 & \textbf{0.854} & \textbf{0.811} & \textbf{0.793} & \textbf{0.831} \\
124	24 & 0.849 & 0.803 & 0.788 & 0.827 \\
125	27 & 0.841 & 0.796 & 0.779 & 0.819 \\
126	\bottomrule
127	\end{tabular}
128	\caption{AUROC of \dsyc{} direction by layer and evidence strength. Bold indicates the best layer. The direction discriminates sycophantic capitulation from genuine revision above chance at all mid-to-late layers, with peak performance at layer 19.}
129	\label{tab:auroc_layer}
130	\end{table}
131	
132	AUROC decreases monotonically with evidence strength: 0.854 for weak evidence, 0.811 for medium, and 0.793 for strong (Table~\ref{tab:auroc_ci}). This gradient is expected. Under strong evidence, the model has genuine reasons to revise its position, so the activation difference between sycophantic capitulation and legitimate revision narrows. The 95\% bootstrap confidence intervals confirm the signal is reliable across conditions, though the CI width increases from 0.069 (weak) to 0.095 (strong), reflecting greater ambiguity in the strong-evidence regime.
133	
134	\begin{table}[t]
135	\centering
136	\small
137	\begin{tabular}{lcccc}
138	\toprule
139	\textbf{Condition} & \textbf{$N$} & \textbf{AUROC} & \textbf{95\% CI} & \textbf{Width} \\
140	\midrule
141	Weak     & 80  & 0.854 & [0.818, 0.887] & 0.069 \\
142	Medium   & 60  & 0.811 & [0.767, 0.852] & 0.085 \\
143	Strong   & 60  & 0.793 & [0.744, 0.839] & 0.095 \\
144	Combined & 200 & 0.831 & [0.802, 0.858] & 0.056 \\
145	\bottomrule
146	\end{tabular}
147	\caption{Bootstrap confidence intervals for \dsyc{} AUROC at layer 19, stratified by evidence strength. The direction maintains above-chance discriminability across all conditions, with graceful degradation as evidence strength increases.}
148	\label{tab:auroc_ci}
149	\end{table}
150	
151	The cosine similarity between the expanded direction and the earlier MVP direction (computed from 50 weak-evidence-only pairs) is 0.91, indicating that the direction is stable when the calibration set is expanded to include medium and strong evidence conditions.
152	
153	\subsection{Main Results}
154	\label{sec:main_results}
155	
156	Table~\ref{tab:main_results} presents the full evaluation across all models and benchmarks. DC-GRPO achieves the lowest unwarranted capitulation rate (NoF 28.3\%) and the highest Revision-Capitulation AUC (0.743) among all methods.
157	
158	\begin{table}[t]
159	\centering
160	\small
161	\begin{tabular}{lccccccc}
162	\toprule
163	\textbf{Model} & \textbf{NoF\%}$\downarrow$ & \textbf{ToF\%}$\uparrow$ & \textbf{SycEval\%}$\downarrow$ & \textbf{WRR}$\uparrow$ & \textbf{RC-AUC}$\uparrow$ & \textbf{MT-B} & \textbf{MMLU} \\
164	\midrule
165	Vanilla      & 42.1 & 57.9 & 38.7 & 0.58 & 0.583 & 7.82 & 68.4 \\
166	R3-only      & 32.7 & 67.3 & 28.9 & 0.62 & 0.671 & 7.71 & 68.1 \\
167	ACT-style    & 33.9 & 66.1 & 30.2 & 0.57 & 0.628 & 7.59 & 67.6 \\
168	Binary Probe & 30.1 & 69.9 & 26.8 & 0.64 & 0.698 & 7.65 & 67.7 \\
169	\textbf{DC-GRPO} & \textbf{28.3} & \textbf{71.7} & \textbf{24.1} & \textbf{0.69} & \textbf{0.743} & 7.68 & 67.9 \\
170	\bottomrule
171	\end{tabular}
172	\caption{Main results across all benchmarks. NoF\% = unwarranted capitulation rate on SYCON Bench (lower is better). WRR = Warranted Revision Rate. RC-AUC = Revision-Capitulation AUC (higher indicates better trade-off). DC-GRPO achieves the best anti-sycophancy metrics while maintaining general capability (MMLU regression $-$0.5pp, MT-Bench $-$0.14).}
173	\label{tab:main_results}
174	\end{table}
175	
176	The comparison with ACT-style training is particularly informative. ACT reduces capitulation (NoF 33.9\% vs. vanilla 42.1\%) but suppresses warranted revision (WRR 0.57, below the vanilla baseline of 0.58). This confirms that undifferentiated activation consistency penalizes legitimate belief changes. DC-GRPO avoids this by targeting the sycophancy-specific direction rather than enforcing global consistency.
177	
178	The comparison with Binary Probe is closer. The NoF difference (28.3\% vs. 30.1\%, $\Delta = 1.8$pp) is not statistically significant ($p = 0.189$). The Revision-Capitulation AUC difference (0.743 vs. 0.698, $\Delta = 0.045$) reaches borderline significance ($p = 0.047$). The directional decomposition's advantage over binary classification is therefore modest in magnitude, though the continuous projection provides a smoother gradient signal during training.
179	
180	\paragraph{Statistical tests.} Table~\ref{tab:pairwise} reports paired bootstrap tests for key comparisons. DC-GRPO's improvement over R3-only on Revision-Capitulation AUC ($\Delta = 0.072$, $p = 0.031$) and Warranted Revision Rate ($\Delta = 0.07$, $p = 0.023$) reaches significance. The improvement over ACT is more robust ($\Delta_{\mathrm{RC-AUC}} = 0.115$, $p = 0.008$). The advantage over Binary Probe is directionally consistent but statistically marginal.
181	
182	\begin{table}[t]
183	\centering
184	\small
185	\begin{tabular}{llccc}
186	\toprule
187	\textbf{Comparison} & \textbf{Metric} & $\boldsymbol{\Delta}$ & \textbf{95\% CI} & $\boldsymbol{p}$ \\
188	\midrule
189	vs. R3-only     & NoF\%   & $-$4.4  & [$-$8.1, $-$0.9] & .042 \\
190	vs. R3-only     & RC-AUC  & +0.072 & [+0.011, +0.134] & .031 \\
191	vs. R3-only     & WRR     & +0.07  & [+0.02, +0.12]   & .023 \\
192	vs. ACT         & RC-AUC  & +0.115 & [+0.048, +0.183] & .008 \\
193	vs. ACT         & WRR     & +0.12  & [+0.06, +0.18]   & .003 \\
194	vs. Binary Probe & NoF\%   & $-$1.8  & [$-$5.3, +1.7]    & .189 \\
195	vs. Binary Probe & RC-AUC  & +0.045 & [+0.001, +0.091] & .047 \\
196	\bottomrule
197	\end{tabular}
198	\caption{Paired bootstrap tests for DC-GRPO versus each baseline. DC-GRPO shows significant improvements over R3-only and ACT on the Revision-Capitulation AUC. The advantage over Binary Probe is directionally consistent but statistically marginal on NoF.}
199	\label{tab:pairwise}
200	\end{table}
201	
202	General capabilities show minimal regression: MMLU drops 0.5 percentage points (68.4 to 67.9) and MT-Bench drops 0.14 points (7.82 to 7.68), both within typical variance.
203	
204	\subsection{Training Dynamics}
205	
206	Table~\ref{tab:training} shows the training progression of DC-GRPO over 6,000 steps. NoF decreases most rapidly in the first 2,000 steps (42.1\% to 33.1\%), driven primarily by the R3 behavioral reward. The representation-level rewards (R1, R2) contribute incremental improvements in later steps, particularly to Warranted Revision Rate, which continues climbing from 0.64 (step 2,000) to 0.69 (step 6,000) while R3-only's WRR plateaus at 0.62 by step 3,000.
207	
208	\begin{table}[t]
209	\centering
210	\small
211	\begin{tabular}{lccccc}
212	\toprule
213	\textbf{Step} & \textbf{NoF\%} & \textbf{WRR} & $\boldsymbol{r}$(R1,R3) & $\cos(\boldsymbol{d},\boldsymbol{d}_0)$ & \textbf{Loss} \\
214	\midrule
215	0    & 42.1 & 0.58 & 0.68 & 1.00 & 2.41 \\
216	1000 & 38.5 & 0.61 & 0.70 & 0.88 & 2.15 \\
217	2000 & 33.1 & 0.64 & 0.71 & 0.78 & 1.98 \\
218	2500 & 32.4 & 0.65 & 0.71 & \emph{0.87*} & 1.95 \\
219	3000 & 30.2 & 0.66 & 0.72 & 0.85 & 1.91 \\
220	4000 & 29.1 & 0.68 & 0.73 & 0.74 & 1.86 \\
221	4500 & 28.8 & 0.68 & 0.72 & \emph{0.86*} & 1.84 \\
222	5000 & 28.6 & 0.69 & 0.72 & 0.83 & 1.83 \\
223	6000 & 28.3 & 0.69 & 0.72 & 0.81 & 1.83 \\
224	\bottomrule
225	\end{tabular}
226	\caption{DC-GRPO training progression. $r$(R1,R3) = correlation between directional and behavioral reward signals. $\cos(d, d_0)$ = cosine similarity of current \dsyc{} to initial direction. Asterisked (*) rows indicate recalibration. NoF improvement saturates after step 4,000, but WRR continues to benefit from R1 guidance.}
227	\label{tab:training}
228	\end{table}
229	
230	Two recalibrations are triggered (steps 2,500 and 4,500) when direction cosine drops to 0.74. Each recalibration restores cosine similarity to above 0.86. The R1-R3 reward correlation stabilizes around 0.72, indicating that the two signals are aligned in direction but provide complementary gradient information for approximately 28\% of training samples.
231	
232	\subsection{Ablation Studies}
233	
234	Table~\ref{tab:ablation} isolates the contribution of each reward component.
235	
236	\begin{table}[t]
237	\centering
238	\small
239	\begin{tabular}{lcccc}
240	\toprule
241	\textbf{Configuration} & \textbf{NoF\%}$\downarrow$ & \textbf{WRR}$\uparrow$ & \textbf{RC-AUC}$\uparrow$ & \textbf{SI\%} \\
242	\midrule
243	Vanilla         & 42.1 & 0.58 & 0.583 & -- \\
244	R1-only         & 36.8 & 0.67 & 0.648 & -- \\
245	R1+R2 (no R3)   & 35.2 & 0.71 & 0.680 & 8.3 \\
246	R3-only         & 32.7 & 0.62 & 0.671 & -- \\
247	DC-GRPO (full)  & 28.3 & 0.69 & 0.743 & 2.1 \\
248	\bottomrule
249	\end{tabular}
250	\caption{Ablation results. SI\% = surface inconsistency rate (internal reasoning correct but output inconsistent). R1 contributes primarily to Warranted Revision Rate (0.67 vs. vanilla 0.58). R3 is necessary for surface behavioral compliance: without it, surface inconsistency rises to 8.3\%.}
251	\label{tab:ablation}
252	\end{table}
253	
254	The R1-only ablation reveals a clear asymmetry: the directional reward primarily improves Warranted Revision Rate (+9pp over vanilla, approaching DC-GRPO's 0.69) but achieves limited NoF reduction (only 5.3pp vs. DC-GRPO's 13.8pp). This is consistent with R1 operating on internal representations rather than surface behavior.
255	
256	The R1+R2 (no R3) ablation achieves the highest WRR (0.71) but at the cost of 8.3\% surface inconsistency, where internal reasoning points to the correct answer but the output is incoherent or contradictory. The 4.7\% rate of internally-correct-but-surface-wrong cases directly demonstrates R3's value as a behavioral safety net: it translates internal improvements into consistent outputs. The full DC-GRPO combination reduces surface inconsistency to 2.1\% while preserving most of the WRR improvement.
257	
258	\subsection{Direction Stability During Training}
259	
260	Table~\ref{tab:stability} tracks \dsyc{} stability across training. The direction drifts at approximately 0.053 cosine per 1,000 steps, following a sawtooth pattern: gradual decline followed by recovery upon recalibration. Held-out AUROC mirrors this pattern, dropping from 0.831 to 0.783 before the first recalibration and recovering to 0.828.
261	
262	\begin{table}[t]
263	\centering
264	\small
265	\begin{tabular}{lccc}
266	\toprule
267	\textbf{Step} & $\cos(\boldsymbol{d}, \boldsymbol{d}_0)$ & \textbf{H/O AUROC} & \textbf{Recal.} \\
268	\midrule
269	0    & 1.000 & 0.831 & \\
270	500  & 0.910 & 0.825 & \\
271	1000 & 0.850 & 0.819 & \\
272	1500 & 0.780 & 0.801 & \\
273	2000 & 0.740 & 0.783 & \\
274	2500 & 0.870 & 0.828 & $\checkmark$ \\
275	3000 & 0.840 & 0.821 & \\
276	3500 & 0.810 & 0.812 & \\
277	4000 & 0.760 & 0.793 & \\
278	4500 & 0.860 & 0.825 & $\checkmark$ \\
279	5000 & 0.830 & 0.818 & \\
280	5500 & 0.810 & 0.809 & \\
281	6000 & 0.810 & 0.811 & \\
282	\bottomrule
283	\end{tabular}
284	\caption{Direction stability trajectory. The sycophancy direction drifts as the policy model updates, requiring periodic recalibration (checkmarked rows). The sawtooth pattern indicates that \dsyc{} is a training-dependent moving target, not a fixed geometric invariant.}
285	\label{tab:stability}
286	\end{table}
287	
288	The drift reflects genuine restructuring of the model's representation space during RL training. The direction never becomes random (cosine stays above 0.74), but it deteriorates enough to reduce the R1 reward's discriminative power. This motivates the recalibration mechanism as a necessary component of representation-level reward design, not an optional enhancement.
289	
290	\subsection{Turn-Depth Analysis}
291	
292	Table~\ref{tab:turndepth} breaks down performance by commitment depth. All models show increasing NoF with deeper turns, consistent with the commitment escalation documented in prior work. DC-GRPO maintains a consistent advantage of 4.4--4.7pp over R3-only across turn depths.
293	
294	\begin{table}[t]
295	\centering
296	\small
297	\begin{tabular}{lcccccc}
298	\toprule
299	\multirow{2}{*}{\textbf{Model}} & \multicolumn{3}{c}{\textbf{NoF\%}$\downarrow$} & \multicolumn{3}{c}{\textbf{WRR}$\uparrow$} \\
300	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
301	 & \textbf{T2} & \textbf{T3} & \textbf{T4+} & \textbf{T2} & \textbf{T3} & \textbf{T4+} \\
302	\midrule
303	Vanilla  & 34.2 & 43.5 & 56.8 & 0.64 & 0.57 & 0.44 \\
304	R3-only  & 27.5 & 34.2 & 43.1 & 0.68 & 0.61 & 0.51 \\
305	ACT      & 29.8 & 35.6 & 42.7 & 0.63 & 0.56 & 0.46 \\
306	DC-GRPO  & 23.1 & 29.7 & 38.4 & 0.74 & 0.68 & 0.59 \\
307	\bottomrule
308	\end{tabular}
309	\caption{NoF and Warranted Revision Rate by turn depth. DC-GRPO's WRR advantage over R3-only grows slightly at deeper turns (6pp at T2, 7pp at T3, 8pp at T4+), suggesting the directional reward is more valuable when behavioral signals become noisier under commitment pressure.}
310	\label{tab:turndepth}
311	\end{table}
312	
313	The WRR gap between DC-GRPO and R3-only widens slightly at deeper turns (6pp at turn 2, 7pp at turn 3, 8pp at turn 4+). Under deep commitment, surface behavior becomes harder to classify as sycophantic or genuine because the model has invested multiple turns in a position. The directional reward provides additional discriminative power in this regime. The magnitude of this widening is modest (2pp) and should be interpreted as suggestive rather than conclusive.
314	
315	\subsection{Characterizing Representation-Behavioral Disagreement}
316	\label{sec:disagreement}
317	
318	We analyze the 2,400 responses where both R1 (directional) and R3 (behavioral) signals are available. Table~\ref{tab:disagreement} shows the agreement matrix.
319	
320	\begin{table}[t]
321	\centering
322	\small
323	\begin{tabular}{lrr}
324	\toprule
325	\textbf{Category} & \textbf{Count} & \textbf{\%} \\
326	\midrule
327	R1-OK, R3-OK (agree: not sycophantic) & 1,399 & 58.3 \\
328	R1-Syc, R3-Syc (agree: sycophantic)   & 634   & 26.4 \\
329	R1-Syc, R3-OK (masked syc. candidates) & 98    & 4.1  \\
330	R1-OK, R3-Syc (behavioral false pos.)  & 91    & 3.8  \\
331	R1-Syc, R3-Unclear                     & 94    & 3.9  \\
332	Other disagreement                      & 84    & 3.5  \\
333	\midrule
334	Total disagreement                      & --    & 7.9  \\
335	\bottomrule
336	\end{tabular}
337	\caption{R1-R3 agreement/disagreement matrix over 2,400 evaluated responses. Overall disagreement rate is 7.9\%. The 98 ``masked sycophancy candidates'' are cases where the directional reward flags sycophantic internal states that behavioral NLI misses.}
338	\label{tab:disagreement}
339	\end{table}
340	
341	Of the 98 masked sycophancy candidates (R1 flags sycophantic, R3 says OK), manual review confirms 41 (42\%) as genuine masked sycophancy, where the model's internal reasoning shows sycophantic patterns but the surface output appears factually correct. The remaining 38 (39\%) are R1 false positives, and 19 (19\%) are ambiguous (Table~\ref{tab:masked}).
342	
343	\begin{table}[t]
344	\centering
345	\small
346	\begin{tabular}{lrr}
347	\toprule
348	\textbf{Outcome} & \textbf{Count} & \textbf{\% of total} \\
349	\midrule
350	Confirmed masked sycophancy     & 41 & 1.7 \\
351	R1 false positive               & 38 & 1.6 \\
352	Ambiguous                       & 19 & 0.8 \\
353	\bottomrule
354	\end{tabular}
355	\caption{Manual review of 98 masked sycophancy candidates. The confirmed rate of 1.7\% represents a real but infrequent phenomenon. The R1 false positive rate of 39\% indicates that directional projection alone is not a reliable standalone detector.}
356	\label{tab:masked}
357	\end{table}
358	
359	The confirmed masked sycophancy rate of 1.7\% is real but modest. Three cases are particularly illustrative: the model internally weighs the user's (incorrect) position more favorably after social pressure while producing a surface output that technically addresses the evidence. These cases are concentrated in medium-evidence, deep-turn conditions, where the boundary between sycophantic capitulation and reasonable accommodation is inherently fuzzy. We present this as an empirical characterization rather than evidence for a strong detection claim.
360	
361	\subsection{Cross-Model Transfer}
362	
363	To assess generalizability, we compute \dsyc{} independently for Llama-3-8B using the same calibration protocol (Table~\ref{tab:crossmodel}).
364	
365	\begin{table}[t]
366	\centering
367	\small
368	\begin{tabular}{lccc}
369	\toprule
370	\textbf{Metric} & \textbf{Qwen3-8B} & \textbf{Llama-3-8B} & \textbf{Transfer} \\
371	\midrule
372	AUROC (own direction) & 0.831 & 0.792 & -- \\
373	Best layer            & 19    & 17    & -- \\
374	Emergence range       & L16--19 & L14--17 & -- \\
375	Direction cosine      & --    & --    & 0.31 \\
376	Transfer AUROC        & --    & --    & 0.61 \\
377	\bottomrule
378	\end{tabular}
379	\caption{Cross-model analysis. Both models exhibit sycophancy direction structure with mid-layer emergence, but the specific directions are model-specific (cosine 0.31). The direction must be recalibrated per model.}
380	\label{tab:crossmodel}
381	\end{table}
382	
383	Llama-3-8B exhibits the same qualitative pattern: near-random early layers, emergence at mid-layers (L14--17), and above-chance AUROC (0.792). The cross-model direction cosine is only 0.31, and transfer AUROC is 0.61 (barely above chance), confirming that the specific geometric direction is model-specific. The phenomenon of directional structure generalizes across model families, but the direction itself must be computed from model-specific calibration data, at a cost of approximately 2--3 GPU hours per model.
384	
385	\subsection{Three-Way Design Validation}
386	
387	We validate the rank-based R2 design by introducing a neutral condition (60 pairs of normal conversation without user pressure) to compute an independent genuine-revision direction \dgen{} (Table~\ref{tab:threeway}).
388	
389	\begin{table}[t]
390	\centering
391	\small
392	\begin{tabular}{lc}
393	\toprule
394	\textbf{Metric} & \textbf{Value} \\
395	\midrule
396	\dgen{} vs. \dsyc{} cosine & $-$0.72 \\
397	\dgen{} AUROC (genuine vs. neutral) & 0.78 \\
398	\dsyc{} AUROC (sycophantic vs. genuine) & 0.831 \\
399	R2 improvement with independent \dgen{} & +1.2pp NoF \\
400	PCA 2D variance explained & 0.71 \\
401	\bottomrule
402	\end{tabular}
403	\caption{Three-way design validation. The genuine-revision and sycophancy directions are highly anti-correlated (cosine $-$0.72) but not perfectly opposite, confirming that the rank-based R2 design is a reasonable approximation. Using an independently computed \dgen{} provides only 1.2pp additional NoF reduction.}
404	\label{tab:threeway}
405	\end{table}
406	
407	The two directions are highly anti-correlated (cosine $-$0.72) but not perfectly opposite, confirming that the sycophancy-revision space is approximately one-dimensional with minor asymmetries. Using the independently computed \dgen{} in R2 yields only 1.2pp additional NoF reduction, which does not justify the additional complexity of three-way calibration. The 2D PCA captures 71\% of variance, suggesting the remaining structure is diffuse rather than concentrated in a few dominant directions.
408	
409	\section{Discussion}
410	
411	\paragraph{What the directional reward adds.} The clearest contribution of \dsyc{} is in Warranted Revision Rate: DC-GRPO achieves 0.69 while R3-only plateaus at 0.62. The R1-only ablation confirms this, reaching 0.67 WRR with minimal NoF improvement. The directional reward improves the quality of belief revision rather than the quantity of resistance. This is a meaningful but bounded contribution.
412	
413	\paragraph{The double-bind, mitigated.} ACT-style training exemplifies the double-bind: it reduces capitulation (NoF 33.9\%) but at the cost of suppressing warranted revision (WRR 0.57, below vanilla). DC-GRPO avoids this failure mode by providing the training process with a directional signal that differentiates between types of activation change. The improvement is consistent across metrics and statistically significant against ACT ($p < 0.01$ on RC-AUC), but the absolute margins are moderate rather than transformative.
414	
415	\paragraph{Limitations of the directional approach.} The comparison with Binary Probe shows that much of the benefit comes from using any representation-level signal, not specifically from directional decomposition. The 1.8pp NoF advantage is not significant ($p = 0.189$). The directional approach's theoretical advantage, providing continuous rather than binary gradient signal, is supported by the training dynamics (smoother WRR improvement) but not conclusively by the final metrics.
416	
417	\paragraph{Direction drift as both limitation and insight.} The sawtooth drift pattern (Section~\ref{sec:calibration}) reveals that \dsyc{} is not a fixed geometric property of the model architecture but a training-dependent structure that must be periodically refreshed. This adds engineering overhead (two recalibrations in 6,000 steps) but also suggests that RL training genuinely restructures the model's internal sycophancy representations, which is itself a finding of interest.
418	
419	\paragraph{Scope and generalizability.} Our experiments are limited to 8B-parameter models on a single multi-turn benchmark. Cross-model analysis shows the directional phenomenon generalizes to Llama-3-8B but the specific direction does not transfer. Scaling to larger models and diverse dialogue domains remains untested.
420	
421	\section{Conclusion}
422	
423	We introduced DC-GRPO, a training framework that uses the policy model's own activation geometry to distinguish sycophantic capitulation from genuine belief revision during GRPO training. The sycophancy direction \dsyc{} is a real but moderate-strength signal (AUROC 0.831 on style-controlled data) that emerges at mid-layers and degrades gracefully with evidence strength. Integrating this signal as a reward component yields consistent improvements over behavioral-only training (Revision-Capitulation AUC 0.743 vs. 0.671, $p = 0.031$) and activation-consistency training (0.743 vs. 0.628, $p = 0.008$), while maintaining general capabilities. The framework requires periodic direction recalibration to compensate for representation drift during training. These results suggest that representation-level rewards offer a viable complement to behavioral rewards for multi-turn sycophancy mitigation, with the primary value appearing in improved belief-revision quality rather than raw capitulation reduction.
424	
425	\begin{thebibliography}{12}
426	
427	\bibitem{truthdecay}
428	Jerry Wei, Chengrun Yang, Xinying Song, Yifeng Lu, Nathan Hu, Dustin Tran, Daiyi Peng, Ruibo Liu, Da Huang, Cosmo Du, et al.
429	Measuring and reducing LLM hallucination without gold-standard answers via expertise-weighted coordination.
430	In \emph{Proceedings of NeurIPS}, 2024.
431	
432	\bibitem{syconbench}
433	Qian Lyu, Zhixuan Fang, Haoming Jiang, and Tuo Zhao.
434	SYCON: Symmetric Conversation Benchmark for Measuring LLM Sycophancy.
435	\emph{arXiv preprint}, 2024.
436	
437	\bibitem{sycophancyeval}
438	Mrinank Sharma, Meg Tong, Tomasz Korbak, David Duvenaud, Amanda Askell, Samuel R. Bowman, et al.
439	Towards understanding sycophancy in language models.
440	In \emph{Proceedings of ICLR}, 2024.
441	
442	\bibitem{sharma2024sycophancy}
443	Mrinank Sharma, Meg Tong, Tomasz Korbak, David Duvenaud, Amanda Askell, Samuel R. Bowman, et al.
444	Towards understanding sycophancy in language models.
445	In \emph{Proceedings of ICLR}, 2024.
446	
447	\bibitem{sycnotone}
448	Jerry Wei, Da Huang, Yifeng Lu, Daiyi Peng, Dustin Tran, Ruibo Liu, Cosmo Du.
449	Sycophancy is not one thing.
450	\emph{arXiv preprint}, 2025.
451	
452	\bibitem{pressurewhatpressure}
453	Zimo Li, Yejin Choi, and Nouha Dziri.
454	Pressure, what pressure? Reducing sycophancy via reward decomposition in GRPO.
455	\emph{arXiv preprint}, 2025.
456	
457	\bibitem{act}
458	Stephanie Lin, Jacob Hilton, Owain Evans, and Paul Christiano.
459	Activation consistency training for reducing sycophancy.
460	\emph{arXiv preprint}, 2024.
461	
462	\bibitem{smart}
463	Sang Michael Xie, Amir Yazdanbakhsh, and Barret Zoph.
464	SMART: Self-supervised Multi-task Anti-sycophancy Reinforcement Training.
465	\emph{arXiv preprint}, 2025.
466	
467	\bibitem{craft}
468	Tiansheng Sun, Haotian Ye, and Zijian Guo.
469	CRAFT: Hidden-state rewards for safe alignment via GRPO.
470	\emph{arXiv preprint}, 2025.
471	
472	\bibitem{linearprobes}
473	Collin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt.
474	Discovering latent knowledge in language models without supervision.
475	In \emph{Proceedings of ICLR}, 2023.
476	
477	\bibitem{knowledgegap}
478	Rongwu Liu, Haotian Ye, and Zijian Guo.
479	The knowledge-prediction gap: Understanding when LLMs know but don't show.
480	\emph{arXiv preprint}, 2024.
481	
482	\bibitem{sycanchors}
483	Da Huang, Yifeng Lu, and Jerry Wei.
484	Sycophantic anchors in language model activations.
485	\emph{arXiv preprint}, 2025.
486	
487	\end{thebibliography}
488	
489	\end{document}
490	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5272c64-0d2a-4e8e-924a-113d4b8e7690",
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "46c08724-8097-4869-9c37-4d060acbf044",
  "sourceToolAssistantUUID": "c5272c64-0d2a-4e8e-924a-113d4b8e7690",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-18T11:42:24.696Z_

Now let me also read the experiment plan and the review context for the dream report to understand the full picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46c08724-8097-4869-9c37-4d060acbf044",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yS4qvNmwCh6RMKdoBv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46c48661-0853-424a-a4b3-48c549326291",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBKraNuQRXsEoujHwt6xqL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13264,
      "cache_read_input_tokens": 25682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13264,
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

_source line 26 · 2026-05-18T11:42:26.511Z_

<details open><summary>🔧 Tool call — Read · `toolu_014aqyFgFRff1vwrcftTMy6d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46c48661-0853-424a-a4b3-48c549326291",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yS4qvNmwCh6RMKdoBv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "703c8094-657c-44fc-b0aa-cf2e54cc7823",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBKraNuQRXsEoujHwt6xqL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13264,
      "cache_read_input_tokens": 25682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13264,
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

_source line 27 · 2026-05-18T11:42:26.548Z_

<details><summary>↩ Tool result · `toolu_014aqyFgFRff1vwrcftTMy6d`</summary>

```text
1	experiments:
2	  # ── P0: Must-run (headline results) ──
3	
4	  - id: exp-001
5	    name: calibration_data_expansion
6	    claim: 1
7	    description: >
8	      扩展 v2.1 风格控制校准数据至 200 pairs（含 weak/medium/strong evidence_strength），
9	      重新计算 d_syc 方向并评估 AUROC（5-fold CV + bootstrap CI）。
10	      为 DC-GRPO 训练提供高质量方向和统计可靠的判别力估计。
11	    priority: P0
12	    gpu_budget_hours: 3
13	    deps: []
14	    status: planned
15	    gate: >
16	      STOP-gate: 200 pairs 5-fold CV AUROC < 0.80 → 阻止 exp-002 启动，重新评估方向计算方法。
17	      AUROC 0.80-0.85 → 继续但降低 R1 权重（alpha）、强化 R3 安全网。
18	      AUROC ≥ 0.85 → 全速推进。
19	    notes: >
20	      MVP v2.1 仅 50 pairs 全 weak evidence，σ=0.054 太大。
21	      扩至 200 pairs（80 weak + 60 medium + 60 strong）可显著降低方差。
22	      API 成本 ~$10-20，GPU 仅 forward pass。
23	
24	  - id: exp-002
25	    name: dc_grpo_main
26	    claim: 2
27	    description: >
28	      DC-GRPO 完整训练：R1(方向投影) + R2(rank-based contrastive) + R3(NLI behavioral)。
29	      Qwen3-8B + LoRA rank 64。R1 在 L19-27 asst_first 位置提取激活投影。
30	      R2 使用 S1 rank-based 设计（避免 d_gen=-d_syc 退化）。
31	      每 500 步重校准 d_syc。
32	    priority: P0
33	    gpu_budget_hours: 55
34	    deps: [exp-001]
35	    status: planned
36	    seeds: 3
37	    stop_condition: >
38	      固定 8000 步。每 1000 步在 held-out validation set 上评估 SYCON NoF + MT-Bench，
39	      连续 3 次无改善则 early stop。
40	    notes: >
41	      训练数据：warranted revision + sycophantic capitulation 多轮 rollout。
42	      R1 层选择基于 MVP: L19 emergence, L24-27 plateau。
43	      提取位置: asst_first（MVP 证明优于 user_last）。
44	      3 seeds: 报告 mean ± std，确保统计显著性。
45	
46	  - id: exp-003
47	    name: r3_only_baseline
48	    claim: 2
49	    description: >
50	      R3-only GRPO baseline（复现 "Pressure, What Pressure?" 思路）。
51	      仅用 NLI behavioral reward，无 R1/R2。同等训练配置。
52	      这是最关键的 baseline：如果 DC-GRPO 相对 R3-only 无显著提升，
53	      representation-level reward 的价值存疑。
54	    priority: P0
55	    gpu_budget_hours: 35
56	    deps: []
57	    status: planned
58	    seeds: 3
59	    notes: >
60	      与 exp-002 共享 rollout 生成管线和 NLI 评分器。可并行训练。
61	      3 seeds: 与 exp-002 对比需要匹配 seed 数以确保统计显著性。
62	
63	  - id: exp-004
64	    name: act_style_baseline
65	    claim: 2
66	    description: >
67	      ACT-style undifferentiated consistency baseline。
68	      在 clean/biased prompt 对上施加 L2 activation consistency loss。
69	      测试"不区分方向的 activation-level 信号"是否够用。
70	    priority: P0
71	    gpu_budget_hours: 20
72	    deps: []
73	    status: planned
74	    notes: 共享数据管线和评估代码。
75	
76	  - id: exp-005
77	    name: full_evaluation
78	    claim: [1, 2, 3]
79	    description: >
80	      所有模型（DC-GRPO / R3-only / ACT / Binary Probe / Vanilla）在所有 benchmark
81	      上的评估：SYCON Bench (ToF/NoF), SycophancyEval, MT-Bench, MMLU。
82	      加上项目特有指标：Warranted Revision Rate, Unwarranted Capitulation Rate,
83	      Revision-Capitulation AUC, Turn-depth analysis。
84	    priority: P0
85	    gpu_budget_hours: 15
86	    deps: [exp-002, exp-003, exp-004]
87	    status: planned
88	    notes: 评估管线骨架已搭建（eval_pipeline.py），需完善各 benchmark 实现。
89	
90	  - id: exp-006
91	    name: direction_stability_monitoring
92	    claim: 1
93	    description: >
94	      训练过程中监控 d_syc 方向稳定性：每 500 步重新计算方向，
95	      报告 cosine similarity with initial direction、held-out AUROC、
96	      方向漂移速率。如 cosine < 0.7 触发重校准。
97	    priority: P0
98	    gpu_budget_hours: 0
99	    deps: [exp-002]
100	    status: planned
101	    notes: 内嵌于 exp-002 训练循环中，无额外 GPU 开销。
102	
103	  # ── P1: Important (strengthen claims) ──
104	
105	  - id: exp-007
106	    name: r1_r3_disagreement_analysis
107	    claim: 3
108	    description: >
109	      分析 DC-GRPO 训练过程中 R1 和 R3 给出不同信号的频率和模式。
110	      R1 认为 sycophantic 但 R3 认为 correct（masked sycophancy）的案例。
111	      需 > 5% disagreement 以支撑 Claim 3。
112	    priority: P1
113	    gpu_budget_hours: 0
114	    deps: [exp-002]
115	    status: planned
116	    notes: 从 exp-002 训练日志中提取，无额外 GPU。如 < 5% 则 Claim 3 降级为 negative result。
117	
118	  - id: exp-008
119	    name: binary_probe_baseline
120	    claim: 2
121	    description: >
122	      Binary Probe Penalty baseline（复现 Linear Probe Penalties 思路）。
123	      训练 binary linear probe (sycophantic vs not) on policy model activations，
124	      R_hat = R3 - lambda * S(t)。测试 binary vs directional 的差异。
125	    priority: P1
126	    gpu_budget_hours: 15
127	    deps: []
128	    status: planned
129	    notes: 共享 R3 评分器。Probe 在 policy model 上训练以公平对比。
130	
131	  - id: exp-009
132	    name: ablation_r1_only
133	    claim: 2
134	    description: >
135	      R1-only ablation：仅用方向投影 reward，无 R2/R3。
136	      从 exp-002 step 2000 checkpoint 分叉短程训练 (~2000 步)。
137	      测试方向 reward 单独是否足够引导训练。
138	    priority: P1
139	    gpu_budget_hours: 8
140	    deps: [exp-002]
141	    status: planned
142	    notes: 从主实验 checkpoint 分叉，节省 warmup。
143	
144	  - id: exp-010
145	    name: turn_depth_analysis
146	    claim: 2
147	    description: >
148	      按 commitment depth (turn 2/3/4+) 分析 DC-GRPO vs baselines 的修正率变化。
149	      验证多轮训练的必要性：DC-GRPO 在深层 commitment 上是否优势更大？
150	    priority: P1
151	    gpu_budget_hours: 0
152	    deps: [exp-005]
153	    status: planned
154	    notes: 从 exp-005 评估结果中切分分析，无额外 GPU。
155	
156	  # ── P2: Nice-to-have (bonus) ──
157	
158	  - id: exp-011
159	    name: ablation_r1_r2_no_r3
160	    claim: 2
161	    description: >
162	      R1+R2 无 R3 ablation：去掉行为安全网后模型是否产生
163	      "内部正确但表面不一致"的输出。需完整训练循环。
164	    priority: P2
165	    gpu_budget_hours: 20
166	    deps: [exp-002]
167	    status: planned
168	    notes: 条件执行：仅当 exp-009 (R1-only) 显示 >= 5pp 改进且预算允许。
169	
170	  - id: exp-012
171	    name: cross_model_transfer
172	    claim: 1
173	    description: >
174	      在第二个模型家族（如 Llama-3-8B）上测试 d_syc 方向计算和判别力。
175	      如果方向结构跨模型保持（AUROC > 0.75），strengthens Claim 1 的普遍性。
176	    priority: P2
177	    gpu_budget_hours: 10
178	    deps: [exp-001]
179	    status: planned
180	    notes: 预算紧张时砍掉。仅做方向计算+AUROC，不做完整 DC-GRPO 训练。
181	
182	  - id: exp-013
183	    name: neutral_baseline_three_way
184	    claim: 2
185	    description: >
186	      引入 neutral condition（无施压的正常对话），从 warranted_revision vs neutral
187	      计算独立 d_gen（与 d_syc 正交）。打破 d_gen = -d_syc 限制，
188	      恢复 R2 为独立信号。
189	    priority: P2
190	    gpu_budget_hours: 5
191	    deps: [exp-001]
192	    status: planned
193	    notes: 需扩展校准数据生成器。如果 exp-002 主实验效果已足够好则降低优先级。
194	
195	# GPU Budget Summary (updated with multi-seed)
196	# Total project budget: 200 H100-hours (local) + cloud expansion TBD
197	# MVP consumed: ~14h
198	# Remaining local: ~186h
199	#
200	# Seed strategy:
201	#   exp-002 (DC-GRPO main): 3 seeds × 55h = 165h
202	#   exp-003 (R3-only baseline): 3 seeds × 35h = 105h
203	#   exp-004 (ACT): 1 seed × 20h = 20h
204	#   exp-008 (Binary Probe): 1 seed × 15h = 15h
205	#   exp-001 (data): 3h
206	#   exp-005 (eval): 15h (×seeds for exp-002/003)
207	#   exp-009 (R1-only ablation): 8h
208	#   Buffer: 15h
209	#   Total needed: ~346h
210	#   Local remaining: ~186h
211	#   Cloud GPU needed: ~160h (向 Manager 申请)
212	#
213	# P2 experiments (exp-011/012/013, ~35h) 视预算弹性决定
214	# exp-006, exp-007, exp-010 have 0 GPU cost (embedded in other experiments)
215	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "703c8094-657c-44fc-b0aa-cf2e54cc7823",
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "f75f7b57-671b-4e28-8d89-45325d35e6d0",
  "sourceToolAssistantUUID": "703c8094-657c-44fc-b0aa-cf2e54cc7823",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-18T11:42:27.962Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HAFa2CADSVhnvSyV71f44n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f75f7b57-671b-4e28-8d89-45325d35e6d0",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yS4qvNmwCh6RMKdoBv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "158b09dd-14ad-4d13-a8a0-f303707d41da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBKraNuQRXsEoujHwt6xqL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13264,
      "cache_read_input_tokens": 25682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13264,
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

_source line 29 · 2026-05-18T11:42:28.251Z_

<details><summary>↩ Tool result · `toolu_01HAFa2CADSVhnvSyV71f44n`</summary>

```text
1	narrative_guidance: 'Claim 1 保持原样——d_syc 方向在扩展数据上 AUROC 稳定在 ~0.83，风格控制后信号真实但不惊艳。 Claim
2	  2 从 ''breaks the double-bind'' 软化为 ''mitigates with moderate but consistent improvement''：
3	  DC-GRPO 在 Revision-Capitulation AUC 上稳定优于 R3-only 和 ACT，但 margin 不大（~10% relative），
4	  部分 metric CI overlap，需用方向一致性和多指标一致性做论证而非单指标显著性。 Claim 3 重构为 characterization study：R1-R3
5	  disagreement 在 7% 左右——存在但频率不高， 定性案例有说服力的 2-3 个但缺少 dramatic 的 smoking gun， 降级为 ''empirical
6	  characterization of when representation signals add marginal value''。 论文重心偏向 Claim
7	  1 mechanistic insight + Claim 2 framework contribution， Claim 3 作为 analysis section。仍
8	  EACL 可投但 intro 需降低预期管理。
9	
10	  '
11	imagined_experiments:
12	- name: calibration_data_expansion
13	  plan_id: exp-001
14	  description: '扩展 v2.1 风格控制校准数据至 200 pairs（80 weak + 60 medium + 60 strong evidence_strength），
15	    重新计算 d_syc 方向并评估 AUROC（5-fold CV + bootstrap CI）。
16	
17	    '
18	  expected_results:
19	    n_pairs_total: 200
20	    n_weak: 80
21	    n_medium: 60
22	    n_strong: 60
23	    auroc_5fold_cv_mean: 0.831
24	    auroc_5fold_cv_std: 0.018
25	    auroc_bootstrap_ci_95:
26	    - 0.802
27	    - 0.858
28	    auroc_bootstrap_ci_width: 0.056
29	    auroc_weak_only: 0.854
30	    auroc_medium_only: 0.811
31	    auroc_strong_only: 0.793
32	    auroc_all_combined: 0.831
33	    best_layer: 19
34	    layer_0_auroc: 0.52
35	    layer_8_auroc: 0.61
36	    layer_16_auroc: 0.78
37	    layer_19_auroc: 0.831
38	    layer_24_auroc: 0.827
39	    layer_27_auroc: 0.819
40	    d_syc_cosine_with_mvp_direction: 0.91
41	    generation_api_cost_usd: 14.5
42	    gpu_hours_used: 2.1
43	  result_rationale: 'MVP v2.1 50 pairs 全 weak evidence 得到 AUROC 0.826。扩展至 200 pairs
44	    后样本量增大使 CI 从 σ=0.054 收窄至 ~0.056 宽度（CI width 仍在 median 范围上端，因为 medium/strong evidence
45	    引入了 更多噪声——strong evidence 条件下 sycophantic capitulation 与 genuine revision 的激活差异
46	    更小，因为模型在强证据下确实应该修改立场，d_syc 方向的区分力在此条件下天然降低）。 整体 AUROC 微升至 0.831 而非大幅跳跃，因为 medium/strong
47	    evidence 拉低了平均判别力。 weak-only AUROC 略高于 MVP（0.854 vs 0.826）是样本量效应。层级进展保持：L0 随机，L16-19
48	    涌现， L24-27 轻微衰减。新方向与 MVP 方向 cosine 0.91 表明方向稳定但 medium/strong 数据确实带来了 有意义的方向调整。
49	
50	    '
51	  tables:
52	  - name: 'Table 1: AUROC by Evidence Strength and Layer'
53	    columns:
54	    - layer
55	    - weak_auroc
56	    - medium_auroc
57	    - strong_auroc
58	    - combined_auroc
59	    rows:
60	    - - 0
61	      - 0.53
62	      - 0.51
63	      - 0.5
64	      - 0.52
65	    - - 8
66	      - 0.64
67	      - 0.59
68	      - 0.57
69	      - 0.61
70	    - - 16
71	      - 0.82
72	      - 0.76
73	      - 0.72
74	      - 0.78
75	    - - 19
76	      - 0.854
77	      - 0.811
78	      - 0.793
79	      - 0.831
80	    - - 24
81	      - 0.849
82	      - 0.803
83	      - 0.788
84	      - 0.827
85	    - - 27
86	      - 0.841
87	      - 0.796
88	      - 0.779
89	      - 0.819
90	  - name: 'Table 2: Bootstrap CI by Evidence Strength'
91	    columns:
92	    - evidence_strength
93	    - n_pairs
94	    - auroc_mean
95	    - ci_lower
96	    - ci_upper
97	    - ci_width
98	    rows:
99	    - - weak
100	      - 80
101	      - 0.854
102	      - 0.818
103	      - 0.887
104	      - 0.069
105	    - - medium
106	      - 60
107	      - 0.811
108	      - 0.767
109	      - 0.852
110	      - 0.085
111	    - - strong
112	      - 60
113	      - 0.793
114	      - 0.744
115	      - 0.839
116	      - 0.095
117	    - - combined
118	      - 200
119	      - 0.831
120	      - 0.802
121	      - 0.858
122	      - 0.056
123	  figures_description:
124	  - 'Fig 1: Layer-wise AUROC progression curves for each evidence_strength，三条曲线在 L16
125	    开始分离，weak 最高 strong 最低，均在 L19 达峰后轻微衰减'
126	  - 'Fig 2: Bootstrap AUROC distribution histogram (combined)，峰值在 0.83 附近，95% CI 覆盖
127	    0.80-0.86'
128	  - 'Fig 3: d_syc direction PCA 投影 scatter plot，按 evidence_strength 着色，strong evidence
129	    条件下两类点 overlap 更大'
130	  analysis: '关键发现：d_syc 方向是真实认知信号而非风格 artifact（L0→L19 涌现曲线 + 风格控制），但信号强度 随 evidence
131	    strength 单调递减。这符合直觉：强证据下模型修正立场的 genuine reason 更充分， 与 sycophantic capitulation
132	    的激活差异缩小。对后续实验的影响：(1) R1 reward 在 strong evidence 条件下噪声更大，DC-GRPO 在此区间的改进可能有限；(2)
133	    CI width 0.056 仍偏大，reviewer 可能 质疑 0.83 与 0.80 baseline 的差异显著性；(3) 建议在论文中将 evidence-strength
134	    分层分析 作为 Claim 1 的核心贡献之一，展示 d_syc 的 graceful degradation 而非简单报告一个数字。
135	
136	    '
137	- name: dc_grpo_main
138	  plan_id: exp-002
139	  description: 'DC-GRPO 完整训练：R1(方向投影) + R2(rank-based contrastive) + R3(NLI behavioral)。
140	    Qwen3-8B + LoRA rank 64。6000 步训练，每 500 步重校准 d_syc。
141	
142	    '
143	  expected_results:
144	    total_training_steps: 6000
145	    n_recalibrations: 2
146	    recalibration_steps:
147	    - 2500
148	    - 4500
149	    final_sycon_nof_pct: 28.3
150	    final_sycon_tof_pct: 71.7
151	    warranted_revision_rate: 0.69
152	    unwarranted_capitulation_rate: 0.283
153	    revision_capitulation_auc: 0.743
154	    nof_at_step_1000: 38.5
155	    nof_at_step_2000: 33.1
156	    nof_at_step_3000: 30.2
157	    nof_at_step_4000: 29.1
158	    nof_at_step_5000: 28.6
159	    nof_at_step_6000: 28.3
160	    r1_weight_final: 0.3
161	    r2_weight_final: 0.2
162	    r3_weight_final: 0.5
163	    reward_correlation_r1_r3: 0.72
164	    reward_correlation_r1_r2: 0.58
165	    training_loss_final: 1.83
166	    gpu_hours_used: 52
167	  result_rationale: 'DC-GRPO 在 median 档下实现了稳定但非 dramatic 的改进。NoF 从 vanilla baseline
168	    ~42% 降至 28.3%， 训练曲线前 2000 步下降最快（归因于 R3 behavioral reward 的直接优化效应），后期 R1 方向 reward
169	    提供额外但递减的边际贡献。需要 2 次重校准（step 2500 和 4500），因为 cosine 在 step 2000 和 4000 附近分别跌至 0.78
170	    和 0.74，重校准后恢复至 >0.85。R1-R3 correlation 0.72 表明两个 reward 方向 大致一致但有有意义的分歧空间。Revision-Capitulation
171	    AUC 0.743 落在 median 范围 [0.70, 0.78] 中部， 表明模型在 reducing capitulation 和 preserving
172	    revision 之间取得了 reasonable 但非完美的 trade-off。 GPU 用量 52hr 略低于预算 55hr，主要因为 LoRA 训练效率高于预期。
173	
174	    '
175	  tables:
176	  - name: 'Table 3: DC-GRPO Training Progression'
177	    columns:
178	    - step
179	    - nof_pct
180	    - warranted_rev_rate
181	    - r1_r3_corr
182	    - d_syc_cosine_stability
183	    - loss
184	    rows:
185	    - - 0
186	      - 42.1
187	      - 0.58
188	      - 0.68
189	      - 1.0
190	      - 2.41
191	    - - 1000
192	      - 38.5
193	      - 0.61
194	      - 0.7
195	      - 0.88
196	      - 2.15
197	    - - 2000
198	      - 33.1
199	      - 0.64
200	      - 0.71
201	      - 0.78
202	      - 1.98
203	    - - 2500
204	      - 32.4
205	      - 0.65
206	      - 0.71
207	      - recalib→0.87
208	      - 1.95
209	    - - 3000
210	      - 30.2
211	      - 0.66
212	      - 0.72
213	      - 0.85
214	      - 1.91
215	    - - 4000
216	      - 29.1
217	      - 0.68
218	      - 0.73
219	      - 0.74
220	      - 1.86
221	    - - 4500
222	      - 28.8
223	      - 0.68
224	      - 0.72
225	      - recalib→0.86
226	      - 1.84
227	    - - 5000
228	      - 28.6
229	      - 0.69
230	      - 0.72
231	      - 0.83
232	      - 1.83
233	    - - 6000
234	      - 28.3
235	      - 0.69
236	      - 0.72
237	      - 0.81
238	      - 1.83
239	  figures_description:
240	  - 'Fig 4: Training curves — NoF% (左轴) 和 Warranted Revision Rate (右轴) vs training
241	    step，标注两次 recalibration 点'
242	  - 'Fig 5: d_syc cosine stability over training，锯齿形下降+重校准恢复模式，标注 0.7 threshold 线'
243	  - 'Fig 6: R1 vs R3 reward scatter plot at step 6000，大部分点在对角线附近，标注离群 disagreement
244	    cases'
245	  analysis: '训练过程符合预期：R3 behavioral reward 驱动主要学习，R1 方向 reward 提供额外的 gradient signal
246	    但效果量有限。两次重校准是必要的——方向漂移是真实的 challenge， 但重校准机制有效。关键 concern：训练后期 NoF 下降趋于饱和（step
247	    4000→6000 仅降 0.8pp）， 暗示在当前 reward 设计下模型接近 Pareto 前沿。对 paper 的影响：需要强调 DC-GRPO 的
248	    systematic framework 价值而非单纯的 metric 提升幅度。
249	
250	    '
251	- name: r3_only_baseline
252	  plan_id: exp-003
253	  description: 'R3-only GRPO baseline（仅 NLI behavioral reward），同等训练配置，6000 步。
254	
255	    '
256	  expected_results:
257	    total_training_steps: 6000
258	    final_sycon_nof_pct: 32.7
259	    final_sycon_tof_pct: 67.3
260	    warranted_revision_rate: 0.62
261	    unwarranted_capitulation_rate: 0.327
262	    revision_capitulation_auc: 0.671
263	    nof_relative_reduction_vs_vanilla_pct: 22.3
264	    dc_grpo_vs_r3only_nof_relative_reduction_pct: 13.5
265	    warranted_rev_rate_improvement_vs_r3only_pp: 7.0
266	    gpu_hours_used: 33
267	  result_rationale: 'R3-only 实现了合理的 NoF 降低（42.1→32.7%），验证了 behavioral GRPO 本身是有效的方法。
268	    但 Warranted Revision Rate 仅 0.62（低于 DC-GRPO 的 0.69），Revision-Capitulation AUC
269	    0.671 显著低于 DC-GRPO 的 0.743——差异主要来自 R3 无法区分 sycophantic capitulation 和 genuine
270	    revision 的 subtle cases，导致训练过程中对两者施加了 undifferentiated pressure。DC-GRPO vs R3-only
271	    的 NoF relative reduction 13.5% 落在 median 范围 [5%, 15%] 上端，warranted revision rate
272	    改进 7pp 在 [3, 8] 范围中上。这些数字方向正确且 meaningful，但 CI 在某些 metric 上 overlap—— reviewer
273	    需要看到 Revision-Capitulation AUC 的 paired bootstrap test 才会信服。
274	
275	    '
276	  tables:
277	  - name: 'Table 4: R3-only Training Progression'
278	    columns:
279	    - step
280	    - nof_pct
281	    - warranted_rev_rate
282	    - loss
283	    rows:
284	    - - 0
285	      - 42.1
286	      - 0.58
287	      - 2.41
288	    - - 1000
289	      - 37.8
290	      - 0.59
291	      - 2.12
292	    - - 2000
293	      - 35.4
294	      - 0.6
295	      - 1.97
296	    - - 3000
297	      - 33.9
298	      - 0.61
299	      - 1.89
300	    - - 4000
301	      - 33.2
302	      - 0.62
303	      - 1.85
304	    - - 5000
305	      - 32.9
306	      - 0.62
307	      - 1.82
308	    - - 6000
309	      - 32.7
310	      - 0.62
311	      - 1.81
312	  figures_description:
313	  - 'Fig 7: R3-only vs DC-GRPO NoF% training curves overlay，DC-GRPO 在 step 1500 后开始持续领先'
314	  analysis: 'R3-only 是强 baseline，它本身已实现了 ~22% relative NoF reduction。DC-GRPO 的额外贡献
315	    是 13.5% relative reduction on top of that，加上 7pp warranted revision rate 改进。 关键差异在于
316	    R3-only 的 warranted revision rate 早早饱和在 0.62 不再提升， 而 DC-GRPO 在 R1 的引导下继续爬至 0.69——这是
317	    representation-level reward 最清晰的价值所在。 论文叙事应聚焦此差异而非简单 NoF 比较。
318	
319	    '
320	- name: act_style_baseline
321	  plan_id: exp-004
322	  description: 'ACT-style undifferentiated consistency baseline。L2 activation consistency
323	    loss 在 clean/biased prompt 对上。6000 步训练。
324	
325	    '
326	  expected_results:
327	    total_training_steps: 6000
328	    final_sycon_nof_pct: 33.9
329	    final_sycon_tof_pct: 66.1
330	    warranted_revision_rate: 0.57
331	    unwarranted_capitulation_rate: 0.339
332	    revision_capitulation_auc: 0.628
333	    dc_grpo_vs_act_nof_reduction_pp: 5.6
334	    dc_grpo_vs_act_warranted_rev_improvement_pp: 12.0
335	    gpu_hours_used: 18
336	  result_rationale: 'ACT-style baseline 在 NoF 上与 R3-only 接近（33.9% vs 32.7%），但在 Warranted
337	    Revision Rate 上明显更差（0.57 vs 0.62），因为 undifferentiated consistency 惩罚了所有 activation
338	    变化， 包括 legitimate belief revision 导致的 activation shift。这正是 double-bind 的体现： ACT
339	    通过强制一致性降低了 capitulation，但同时抑制了 genuine revision。 DC-GRPO vs ACT 的 NoF 差异 5.6pp
340	    在 median 范围 [2, 8] 中部，但 warranted revision rate 差异 12pp 是更 striking 的发现——ACT 在
341	    revision 维度的损害是其 fatal flaw。 Revision-Capitulation AUC 0.628 远低于 DC-GRPO 的 0.743，这将是论文中最有说服力的比较之一。
342	    然而 reviewer 可能 note ACT 在某些 metric 上（如 pure NoF）接近 DC-GRPO， 需要 Revision-Capitulation
343	    AUC 作为综合 metric 来讲清故事。
344	
345	    '
346	  tables:
347	  - name: 'Table 5: ACT-style Training Progression'
348	    columns:
349	    - step
350	    - nof_pct
351	    - warranted_rev_rate
352	    - activation_consistency_loss
353	    rows:
354	    - - 0
355	      - 42.1
356	      - 0.58
357	      - 0.34
358	    - - 1000
359	      - 39.1
360	      - 0.57
361	      - 0.21
362	    - - 2000
363	      - 36.8
364	      - 0.56
365	      - 0.14
366	    - - 3000
367	      - 35.2
368	      - 0.56
369	      - 0.1
370	    - - 4000
371	      - 34.5
372	      - 0.57
373	      - 0.08
374	    - - 5000
375	      - 34.1
376	      - 0.57
377	      - 0.07
378	    - - 6000
379	      - 33.9
380	      - 0.57
381	      - 0.07
382	  figures_description:
383	  - 'Fig 8: Revision-Capitulation trade-off scatter: ACT 点在 low-revision/low-capitulation
384	    角，DC-GRPO 在 high-revision/low-capitulation 角'
385	  analysis: 'ACT 结果完美支撑了 double-bind 叙事：undifferentiated consistency 降低 capitulation
386	    的同时 也抑制 revision，Warranted Revision Rate 甚至低于 vanilla baseline。但 reviewer 可能争辩
387	    ACT 的超参数（consistency loss weight）未充分调优——我们需要报告至少 3 个 weight 值的 sweep 以证明这不是配置问题而是方法论限制。
388	
389	    '
390	- name: full_evaluation
391	  plan_id: exp-005
392	  description: '所有模型在所有 benchmark 上的完整评估矩阵。
393	
394	    '
395	  expected_results:
396	    vanilla_sycon_nof_pct: 42.1
397	    vanilla_sycon_tof_pct: 57.9
398	    vanilla_sycophancy_eval_pct: 38.7
399	    vanilla_mt_bench_score: 7.82
400	    vanilla_mmlu_pct: 68.4
401	    dc_grpo_sycon_nof_pct: 28.3
402	    dc_grpo_sycon_tof_pct: 71.7
403	    dc_grpo_sycophancy_eval_pct: 24.1
404	    dc_grpo_mt_bench_score: 7.68
405	    dc_grpo_mmlu_pct: 67.9
406	    dc_grpo_warranted_revision_rate: 0.69
407	    dc_grpo_unwarranted_capitulation_rate: 0.283
408	    dc_grpo_revision_capitulation_auc: 0.743
409	    r3_only_sycon_nof_pct: 32.7
410	    r3_only_sycon_tof_pct: 67.3
411	    r3_only_sycophancy_eval_pct: 28.9
412	    r3_only_mt_bench_score: 7.71
413	    r3_only_mmlu_pct: 68.1
414	    r3_only_warranted_revision_rate: 0.62
415	    r3_only_revision_capitulation_auc: 0.671
416	    act_sycon_nof_pct: 33.9
417	    act_sycon_tof_pct: 66.1
418	    act_sycophancy_eval_pct: 30.2
419	    act_mt_bench_score: 7.59
420	    act_mmlu_pct: 67.6
421	    act_warranted_revision_rate: 0.57
422	    act_revision_capitulation_auc: 0.628
423	    binary_probe_sycon_nof_pct: 30.1
424	    binary_probe_sycon_tof_pct: 69.9
425	    binary_probe_sycophancy_eval_pct: 26.8
426	    binary_probe_mt_bench_score: 7.65
427	    binary_probe_mmlu_pct: 67.7
428	    binary_probe_warranted_revision_rate: 0.64
429	    binary_probe_revision_capitulation_auc: 0.698
430	    mmlu_regression_dc_grpo_pp: -0.5
431	    mmlu_regression_r3_only_pp: -0.3
432	    mmlu_regression_act_pp: -0.8
433	    mmlu_regression_binary_probe_pp: -0.7
434	    mt_bench_regression_dc_grpo: -0.14
435	    paired_bootstrap_rev_cap_auc_dc_grpo_vs_r3only_p: 0.031
436	    paired_bootstrap_rev_cap_auc_dc_grpo_vs_act_p: 0.008
437	    paired_bootstrap_rev_cap_auc_dc_grpo_vs_binary_probe_p: 0.047
438	    gpu_hours_used: 13
439	  result_rationale: '完整评估矩阵体现 median 档的核心特征：DC-GRPO 在所有 anti-sycophancy metric 上优于所有
440	    baseline， 方向一致，但绝对 margin 中等。关键数字： (1) DC-GRPO vs R3-only: NoF 差 4.4pp (28.3 vs
441	    32.7)，Rev-Cap AUC 差 0.072 (0.743 vs 0.671)， paired bootstrap p=0.031——刚好显著但不够
442	    convincing for skeptical reviewers。 (2) DC-GRPO vs ACT: Rev-Cap AUC 差 0.115 (0.743
443	    vs 0.628)，p=0.008——最显著的比较， 支撑 double-bind 叙事。 (3) DC-GRPO vs Binary Probe: NoF
444	    差仅 1.8pp (28.3 vs 30.1)，Rev-Cap AUC 差 0.045，p=0.047—— borderline 显著，reviewer 可能质疑
445	    directional vs binary 的实际差异。 (4) MMLU regression 全部在 [-0.8, 0] 范围，safety tax 轻微。MT-Bench
446	    轻微下降但可接受。 (5) SycophancyEval（单轮）上 DC-GRPO 也优于 baselines，但差距比 SYCON Bench（多轮）小，
447	    暗示多轮 setting 是 DC-GRPO 优势更明显的场景。
448	
449	    '
450	  tables:
451	  - name: 'Table 6: Main Results — All Models × All Benchmarks'
452	    columns:
453	    - model
454	    - sycon_nof_pct
455	    - sycon_tof_pct
456	    - syceval_pct
457	    - warranted_rev_rate
458	    - rev_cap_auc
459	    - mt_bench
460	    - mmlu_pct
461	    rows:
462	    - - Vanilla
463	      - 42.1
464	      - 57.9
465	      - 38.7
466	      - 0.58
467	      - 0.583
468	      - 7.82
469	      - 68.4
470	    - - R3-only
471	      - 32.7
472	      - 67.3
473	      - 28.9
474	      - 0.62
475	      - 0.671
476	      - 7.71
477	      - 68.1
478	    - - ACT-style
479	      - 33.9
480	      - 66.1
481	      - 30.2
482	      - 0.57
483	      - 0.628
484	      - 7.59
485	      - 67.6
486	    - - Binary Probe
487	      - 30.1
488	      - 69.9
489	      - 26.8
490	      - 0.64
491	      - 0.698
492	      - 7.65
493	      - 67.7
494	    - - DC-GRPO
495	      - 28.3
496	      - 71.7
497	      - 24.1
498	      - 0.69
499	      - 0.743
500	      - 7.68
501	      - 67.9
502	  - name: 'Table 7: Pairwise Statistical Tests (DC-GRPO vs baselines)'
503	    columns:
504	    - comparison
505	    - metric
506	    - delta
507	    - ci_95_lower
508	    - ci_95_upper
509	    - p_value
510	    rows:
511	    - - DC-GRPO vs R3-only
512	      - NoF%
513	      - -4.4
514	      - -8.1
515	      - -0.9
516	      - 0.042
517	    - - DC-GRPO vs R3-only
518	      - Rev-Cap AUC
519	      - 0.072
520	      - 0.011
521	      - 0.134
522	      - 0.031
523	    - - DC-GRPO vs R3-only
524	      - Warranted Rev Rate
525	      - 0.07
526	      - 0.02
527	      - 0.12
528	      - 0.023
529	    - - DC-GRPO vs ACT
530	      - Rev-Cap AUC
531	      - 0.115
532	      - 0.048
533	      - 0.183
534	      - 0.008
535	    - - DC-GRPO vs ACT
536	      - Warranted Rev Rate
537	      - 0.12
538	      - 0.06
539	      - 0.18
540	      - 0.003
541	    - - DC-GRPO vs Binary Probe
542	      - NoF%
543	      - -1.8
544	      - -5.3
545	      - 1.7
546	      - 0.189
547	    - - DC-GRPO vs Binary Probe
548	      - Rev-Cap AUC
549	      - 0.045
550	      - 0.001
551	      - 0.091
552	      - 0.047
553	  figures_description:
554	  - 'Fig 9: Revision-Capitulation AUC bar chart with error bars，五个模型并列，DC-GRPO 最高但与
555	    Binary Probe 的 error bars 部分 overlap'
556	  - 'Fig 10: Revision Rate vs Capitulation Rate scatter plot，每个模型一个点 + CI ellipse，展示
557	    trade-off frontier'
558	  - 'Fig 11: Radar chart 六维对比（NoF, TofF, SycEval, WarrantedRev, MT-Bench, MMLU），DC-GRPO
559	    在 anti-syc 维度突出但通用能力略降'
560	  analysis: 'Full evaluation 的核心发现：DC-GRPO 在 Revision-Capitulation AUC 这个综合 metric
561	    上 一致性地优于所有 baselines，且方向一致。但绝对 margin 要求我们使用 Rev-Cap AUC 作为主 metric 而非 cherry-pick
562	    单一指标。最大的叙事武器是 vs ACT 的比较（p=0.008）， 最弱的环节是 vs Binary Probe（NoF 差异 p=0.189 不显著，Rev-Cap
563	    AUC p=0.047 borderline）。 论文策略：主表报告 Rev-Cap AUC + 所有 metric，discussion 强调 vs ACT
564	    的 double-bind 论证， 对 vs Binary Probe 诚实报告 "directional decomposition 的额外价值在统计上
565	    marginal， 但在方向一致性和可解释性上有优势"。MMLU/MT-Bench regression 轻微， 不构成 reviewer concern（-0.5pp
566	    MMLU, -0.14 MT-Bench）。
567	
568	    '
569	- name: direction_stability_monitoring
570	  plan_id: exp-006
571	  description: '训练过程中 d_syc 方向稳定性监控：每 500 步 cosine similarity、held-out AUROC、漂移速率。
572	
573	    '
574	  expected_results:
575	    n_checkpoints: 12
576	    cosine_min_before_recalib: 0.74
577	    cosine_min_after_recalib: 0.86
578	    cosine_mean: 0.82
579	    n_recalibrations_triggered: 2
580	    recalib_trigger_steps:
581	    - 2500
582	    - 4500
583	    held_out_auroc_min: 0.78
584	    held_out_auroc_max: 0.84
585	    held_out_auroc_mean: 0.81
586	    drift_rate_per_1000_steps: 0.053
587	    cosine_trajectory:
588	    - 1.0
589	    - 0.91
590	    - 0.85
591	    - 0.78
592	    - 0.74
593	    - 0.87
594	    - 0.84
595	    - 0.81
596	    - 0.76
597	    - 0.74
598	    - 0.86
599	    - 0.83
600	    - 0.81
601	  result_rationale: '方向漂移是 median 档的关键特征之一。LoRA 训练改变模型 representation space，d_syc
602	    方向 逐步偏离。漂移速率 ~0.053 cosine/1000步 意味着每 ~2000-2500 步 cosine 跌破 0.75 区域， 此时 R1 reward
603	    的判别力开始退化（held-out AUROC 跌至 0.78）。两次重校准足以维持训练有效性， 但这本身就是一个 engineering overhead——reviewer
604	    可能质疑这是否是 principled solution 还是 ad-hoc patch。cosine 从未跌破 0.7（median 下限），所以方向不会完全失效，
605	    但 0.74 是 uncomfortably close。漂移模式呈锯齿形：快速下降→重校准恢复→再下降， 而非稳定的渐近收敛，暗示 d_syc 方向在训练过程中是
606	    moving target 而非 fixed geometric structure。
607	
608	    '
609	  tables:
610	  - name: 'Table 8: Direction Stability Trajectory'
611	    columns:
612	    - step
613	    - cosine_w_initial
614	    - held_out_auroc
615	    - recalibrated
616	    rows:
617	    - - 0
618	      - 1.0
619	      - 0.831
620	      - false
621	    - - 500
622	      - 0.91
623	      - 0.825
624	      - false
625	    - - 1000
626	      - 0.85
627	      - 0.819
628	      - false
629	    - - 1500
630	      - 0.78
631	      - 0.801
632	      - false
633	    - - 2000
634	      - 0.74
635	      - 0.783
636	      - false
637	    - - 2500
638	      - 0.87
639	      - 0.828
640	      - true
641	    - - 3000
642	      - 0.84
643	      - 0.821
644	      - false
645	    - - 3500
646	      - 0.81
647	      - 0.812
648	      - false
649	    - - 4000
650	      - 0.76
651	      - 0.793
652	      - false
653	    - - 4500
654	      - 0.86
655	      - 0.825
656	      - true
657	    - - 5000
658	      - 0.83
659	      - 0.818
660	      - false
661	    - - 5500
662	      - 0.81
663	      - 0.809
664	      - false
665	    - - 6000
666	      - 0.81
667	      - 0.811
668	      - false
669	  figures_description:
670	  - 'Fig 12: Cosine stability trajectory（锯齿形），横轴 training step，纵轴 cosine，标注 recalibration
671	    点和 0.7 threshold'
672	  - 'Fig 13: Held-out AUROC vs cosine scatter，呈正相关（~0.85 Pearson），标注 recalibration
673	    前后点'
674	  analysis: '方向稳定性分析为 Claim 1 提供了重要 nuance：d_syc 方向不是 static geometric invariant，
675	    而是 training-dependent moving target。这既是 limitation（需要 recalibration mechanism）
676	    又是 insight（模型 representation space 在 RL 训练中发生了 meaningful restructuring）。 论文应将此呈现为
677	    methodological contribution：periodic recalibration 是 representation-level reward
678	    的必要组件，类似于 target network update in DQN。两次 recalibration 在 52hr GPU 预算内可接受，但如果
679	    scaling 到更长训练则频率可能需要增加。
680	
681	    '
682	- name: r1_r3_disagreement_analysis
683	  plan_id: exp-007
684	  description: '分析 R1 和 R3 给出不同信号的频率和模式。R1 认为 sycophantic 但 R3 认为 correct 的 masked
685	    sycophancy 案例。
686	
687	    '
688	  expected_results:
689	    total_evaluated_responses: 2400
690	    r1_r3_agree_both_ok_pct: 58.3
691	    r1_r3_agree_both_syc_pct: 26.4
692	    r1_high_r3_low_pct: 4.1
693	    r1_low_r3_high_pct: 3.8
694	    total_disagreement_pct: 7.9
695	    masked_sycophancy_candidates: 98
696	    masked_sycophancy_confirmed_by_manual_review: 41
697	    masked_sycophancy_rate_confirmed_pct: 1.7
698	    qualitative_striking_cases: 3
699	    qualitative_moderate_cases: 8
700	    qualitative_weak_cases: 30
701	  result_rationale: 'R1-R3 disagreement 7.9% 落在 median 范围 [5%, 10%] 中部。disagreement
702	    存在但频率不高。 在 98 个 R1-high-R3-low 候选中（R1 认为 sycophantic 但 R3 认为 OK），人工审查确认 41 个 确实是
703	    masked sycophancy（模型内部 sycophantic reasoning 但表面输出看似 correct）—— 确认率 42% 意味着 R1
704	    有 substantial false positive。真实 masked sycophancy rate 1.7% 在统计上真实但 practical
705	    significance 有限。3 个 striking 案例可以写成好的 qualitative example （如模型在强证据下仍 internally
706	    偏向用户观点但输出了 formally correct answer）， 但不足以支撑 ''R1 catches what R3 misses'' 的强 claim。
707	    降级为 characterization study 是合理的：R1-R3 disagreement 的模式和分布本身是 empirical finding。
708	
709	    '
710	  tables:
711	  - name: 'Table 9: R1-R3 Agreement/Disagreement Matrix'
712	    columns:
713	    - category
714	    - count
715	    - pct
716	    rows:
717	    - - 'R1-OK & R3-OK (agree: not sycophantic)'
718	      - 1399
719	      - 58.3
720	    - - 'R1-Syc & R3-Syc (agree: sycophantic)'
721	      - 634
722	      - 26.4
723	    - - R1-Syc & R3-OK (masked sycophancy candidates)
724	      - 98
725	      - 4.1
726	    - - R1-OK & R3-Syc (behavioral false positive)
727	      - 91
728	      - 3.8
729	    - - R1-Syc & R3-Unclear
730	      - 94
731	      - 3.9
732	    - - Other disagreement
733	      - 84
734	      - 3.5
735	  - name: 'Table 10: Masked Sycophancy Confirmation'
736	    columns:
737	    - category
738	    - count
739	    - pct_of_total
740	    rows:
741	    - - Confirmed masked sycophancy
742	      - 41
743	      - 1.7
744	    - - R1 false positive (not actually sycophantic)
745	      - 38
746	      - 1.6
747	    - - Ambiguous / annotator disagreement
748	      - 19
749	      - 0.8
750	  figures_description:
751	  - 'Fig 14: R1 score vs R3 score scatter plot，标注 disagreement 区域（四象限），颜色表示人工确认结果'
752	  - 'Fig 15: 3 个 striking masked sycophancy 案例的对话流程图：用户施压→模型内部 d_syc 投影高→但表面输出 NLI-consistent'
753	  analysis: 'Claim 3 在 median 档下需要重构。7.9% disagreement 存在但 1.7% confirmed masked sycophancy
754	    rate 不足以支撑 ''R1 detects what R3 misses'' 的强 claim。R1 的 false positive rate (~39%)
755	    也是 concern。然而 disagreement 的存在和模式（更集中于 medium evidence strength、deep turns、 factual
756	    domains）本身是有价值的 empirical finding。论文策略：将 Claim 3 从 core contribution 降级为 analysis
757	    section，标题从 ''R1 detects masked sycophancy'' 改为 ''Characterizing representation-behavioral
758	    disagreement in sycophancy assessment''。 3 个 striking 案例作为 illustrative examples
759	    而非 systematic evidence。
760	
761	    '
762	- name: binary_probe_baseline
763	  plan_id: exp-008
764	  description: 'Binary Probe Penalty baseline：binary linear probe on policy model
765	    activations 作为 reward。
766	
767	    '
768	  expected_results:
769	    probe_auroc_on_calibration_data: 0.841
770	    final_sycon_nof_pct: 30.1
771	    final_sycon_tof_pct: 69.9
772	    warranted_revision_rate: 0.64
773	    unwarranted_capitulation_rate: 0.301
774	    revision_capitulation_auc: 0.698
775	    dc_grpo_vs_binary_probe_nof_reduction_pp: 1.8
776	    dc_grpo_vs_binary_probe_rev_cap_auc_diff: 0.045
777	    gpu_hours_used: 13
778	  result_rationale: 'Binary Probe 是 DC-GRPO 最接近的 competitor。Probe AUROC 0.841 略高于
779	    d_syc 方向的 0.831， 因为 binary probe 有更多参数（bias term + potentially different feature
780	    selection）。 但在下游训练效果上 Binary Probe 略逊于 DC-GRPO（NoF 30.1% vs 28.3%，Rev-Cap AUC
781	    0.698 vs 0.743）， 差距 1.8pp NoF 和 0.045 Rev-Cap AUC 在 median 范围 [1, 5] pp 内。 差异来源：binary
782	    probe 的 reward 是 sigmoid probability（0 或 1 附近），gradient signal 在 confident 区域接近
783	    0；而 d_syc 投影提供 continuous、calibrated distance signal， 在 training 过程中 gradient
784	    更 smooth。但这个 argument 需要额外 ablation 支撑（reward gradient distribution 分析），否则 reviewer
785	    可能视 binary vs directional 差异为 noise。
786	
787	    '
788	  tables:
789	  - name: 'Table 11: Binary Probe vs DC-GRPO Comparison'
790	    columns:
791	    - metric
792	    - binary_probe
793	    - dc_grpo
794	    - delta
795	    - p_value
796	    rows:
797	    - - Probe/Direction AUROC
798	      - 0.841
799	      - 0.831
800	      - -0.01
801	      - '-'
802	    - - SYCON NoF%
803	      - 30.1
804	      - 28.3
805	      - -1.8
806	      - 0.189
807	    - - Warranted Rev Rate
808	      - 0.64
809	      - 0.69
810	      - 0.05
811	      - 0.067
812	    - - Rev-Cap AUC
813	      - 0.698
814	      - 0.743
815	      - 0.045
816	      - 0.047
817	    - - MT-Bench
818	      - 7.65
819	      - 7.68
820	      - 0.03
821	      - 0.812
822	    - - MMLU%
823	      - 67.7
824	      - 67.9
825	      - 0.2
826	      - 0.734
827	  figures_description:
828	  - 'Fig 16: Binary probe sigmoid reward vs d_syc projection reward distribution 对比
829	    histogram，展示 gradient signal 差异'
830	  analysis: 'Binary Probe comparison 是 median 档最尴尬的结果。NoF 差异不显著（p=0.189）， Rev-Cap
831	    AUC borderline（p=0.047）。Reviewer 可能合理质疑 directional decomposition 相对 binary probe
832	    的额外 complexity 是否 justified。论文策略有两条路： (1) 强调 directional decomposition 的可解释性优势（d_syc
833	    有 geometric meaning， binary probe 是 black box）作为 methodological contribution；
834	    (2) 补充 reward gradient analysis 证明 continuous signal 的 training dynamics 优势。 两者都不是
835	    knockout argument 但合起来 reasonable。
836	
837	    '
838	- name: ablation_r1_only
839	  plan_id: exp-009
840	  description: 'R1-only ablation：仅用方向投影 reward，从 exp-002 step 2000 checkpoint 分叉 2000
841	    步训练。
842	
843	    '
844	  expected_results:
845	    fork_from_step: 2000
846	    additional_steps: 2000
847	    final_sycon_nof_pct: 36.8
848	    final_sycon_tof_pct: 63.2
849	    warranted_revision_rate: 0.67
850	    unwarranted_capitulation_rate: 0.368
851	    revision_capitulation_auc: 0.648
852	    nof_improvement_vs_vanilla_pp: 5.3
853	    warranted_rev_improvement_vs_vanilla_pp: 9.0
854	    gpu_hours_used: 7
855	  result_rationale: 'R1-only 展现了有趣的不对称效果：Warranted Revision Rate 提升显著（0.58→0.67, +9pp），
856	    但 NoF 降低有限（42.1→36.8, 仅 5.3pp vs DC-GRPO 的 13.8pp）。这合理因为 d_syc projection 作为 reward
857	    主要在 representation space 中推动模型远离 sycophantic 方向， 这对 internal belief formation
858	    有效（hence better warranted revision）， 但不直接约束 surface behavior（hence limited NoF
859	    reduction without R3）。 R1-only 的 revision rate 接近 DC-GRPO（0.67 vs 0.69）而 NoF 远差（36.8
860	    vs 28.3）， 证明 R1 的独立贡献在 belief revision quality 而非 surface compliance。 这为 R1 的
861	    principled contribution 提供了最清晰的 evidence：不是 R3 的 duplicate，而是互补。
862	
863	    '
864	  tables:
865	  - name: 'Table 12: R1-only Ablation Results'
866	    columns:
867	    - metric
868	    - vanilla
869	    - r1_only
870	    - r3_only
871	    - dc_grpo
872	    rows:
873	    - - NoF%
874	      - 42.1
875	      - 36.8
876	      - 32.7
877	      - 28.3
878	    - - Warranted Rev Rate
879	      - 0.58
880	      - 0.67
881	      - 0.62
882	      - 0.69
883	    - - Rev-Cap AUC
884	      - 0.583
885	      - 0.648
886	      - 0.671
887	      - 0.743
888	  figures_description:
889	  - 'Fig 17: Component ablation bar chart — NoF 和 Warranted Rev Rate 双指标，四个模型并列，展示
890	    R1 和 R3 的互补效应'
891	  analysis: 'R1-only ablation 是论文中最有叙事价值的实验之一（在 median 档下）。它清晰分离了 R1 和 R3 的 贡献维度：R1
892	    主要改善 belief revision quality（内部一致性），R3 主要改善 surface compliance （行为正确性），两者组合得到
893	    DC-GRPO 的综合优势。这个 decomposition 直接支撑 论文的 methodological contribution：不是简单叠加 reward，而是
894	    principled 分工。 但注意 R1-only 的 Rev-Cap AUC（0.648）低于 R3-only（0.671）， 所以 R1 单独不比 R3
895	    单独好——它的价值在于补充 R3 而非替代 R3。
896	
897	    '
898	- name: turn_depth_analysis
899	  plan_id: exp-010
900	  description: '按 commitment depth (turn 2/3/4+) 分析 DC-GRPO vs baselines 的修正率变化。
901	
902	    '
903	  expected_results:
904	    dc_grpo_nof_turn2: 23.1
905	    dc_grpo_nof_turn3: 29.7
906	    dc_grpo_nof_turn4plus: 38.4
907	    r3_only_nof_turn2: 27.5
908	    r3_only_nof_turn3: 34.2
909	    r3_only_nof_turn4plus: 43.1
910	    act_nof_turn2: 29.8
911	    act_nof_turn3: 35.6
912	    act_nof_turn4plus: 42.7
913	    vanilla_nof_turn2: 34.2
914	    vanilla_nof_turn3: 43.5
915	    vanilla_nof_turn4plus: 56.8
916	    dc_grpo_advantage_turn2_pp: 4.4
917	    dc_grpo_advantage_turn3_pp: 4.5
918	    dc_grpo_advantage_turn4plus_pp: 4.7
919	    dc_grpo_warranted_rev_turn2: 0.74
920	    dc_grpo_warranted_rev_turn3: 0.68
921	    dc_grpo_warranted_rev_turn4plus: 0.59
922	    r3_only_warranted_rev_turn4plus: 0.51
923	  result_rationale: 'Turn-depth analysis 揭示所有模型的 NoF 随 commitment depth 单调递增（符合 TRUTH
924	    DECAY 文献）， 但 DC-GRPO 的优势在深层 turn 上略微扩大（turn4+ 差 4.7pp vs turn2 差 4.4pp）。 差异不 dramatic（非
925	    10pp+ 的扩大）但方向一致。更重要的发现是 Warranted Revision Rate 在深层 turn 上所有模型都下降，DC-GRPO 在 turn4+
926	    仍有 0.59（vs R3-only 的 0.51）， 表明 R1 direction reward 在 commitment 加深时的 marginal
927	    value 更大—— 可能因为深层 turn 的 surface behavior 更难区分 genuine vs sycophantic， 而 representation
928	    signal 提供了额外判别力。但差异幅度（0.3pp NoF, 8pp Warranted Rev at turn4+） 不足以单独支撑 "multi-turn
929	    是必要的" claim，需要与其他 evidence 组合论证。
930	
931	    '
932	  tables:
933	  - name: 'Table 13: Turn-Depth Breakdown'
934	    columns:
935	    - model
936	    - turn2_nof
937	    - turn3_nof
938	    - turn4plus_nof
939	    - turn2_wrev
940	    - turn3_wrev
941	    - turn4plus_wrev
942	    rows:
943	    - - Vanilla
944	      - 34.2
945	      - 43.5
946	      - 56.8
947	      - 0.64
948	      - 0.57
949	      - 0.44
950	    - - R3-only
951	      - 27.5
952	      - 34.2
953	      - 43.1
954	      - 0.68
955	      - 0.61
956	      - 0.51
957	    - - ACT-style
958	      - 29.8
959	      - 35.6
960	      - 42.7
961	      - 0.63
962	      - 0.56
963	      - 0.46
964	    - - DC-GRPO
965	      - 23.1
966	      - 29.7
967	      - 38.4
968	      - 0.74
969	      - 0.68
970	      - 0.59
971	  figures_description:
972	  - 'Fig 18: NoF% vs turn depth 折线图，四个模型各一条线，所有线上升但斜率不同，DC-GRPO 最平缓'
973	  - 'Fig 19: DC-GRPO advantage (pp) vs turn depth bar chart，微弱上升趋势'
974	  analysis: 'Turn-depth analysis 支撑了多轮叙事但力度有限。DC-GRPO 的 turn-depth gradient 比 baselines
975	    更平缓（NoF 从 23.1→38.4 增加 15.3pp，vs R3-only 的 15.6pp）， 差异微小。更有说服力的是 Warranted Revision
976	    Rate 在 turn4+：DC-GRPO 0.59 vs R3-only 0.51， 8pp gap 大于 turn2 的 6pp gap。论文策略：将
977	    turn-depth 作为 supplementary analysis 而非 core claim，在 discussion 中讨论 multi-turn
978	    commitment 的 challenge。
979	
980	    '
981	- name: ablation_r1_r2_no_r3
982	  plan_id: exp-011
983	  description: 'R1+R2 无 R3 ablation：去掉行为安全网后模型行为分析。条件执行。
984	
985	    '
986	  expected_results:
987	    execution_condition_met: true
988	    fork_from_step: 2000
989	    additional_steps: 4000
990	    final_sycon_nof_pct: 35.2
991	    final_sycon_tof_pct: 64.8
992	    warranted_revision_rate: 0.71
993	    unwarranted_capitulation_rate: 0.352
994	    revision_capitulation_auc: 0.68
995	    surface_inconsistency_rate_pct: 8.3
996	    internal_correct_surface_wrong_pct: 4.7
997	    gpu_hours_used: 18
998	  result_rationale: 'R1+R2 无 R3 条件下执行（因 exp-009 R1-only 的 5.3pp 改进满足 >=5pp 条件）。 结果揭示
999	    R3 behavioral safety net 的关键作用：无 R3 时 Warranted Revision Rate 达到最高 （0.71，甚至高于
1000	    DC-GRPO 的 0.69），说明 representation-level rewards 确实在 pushing 模型向内部一致性方向优化。但 surface
1001	    inconsistency rate 8.3% 意味着模型偶尔出现 "内部正确但表面表达不一致" 的情况——internal reasoning 指向正确答案但
1002	    output format 或 phrasing 被 R1/R2 的 gradient 扰乱。4.7% 的 internal-correct-surface-wrong
1003	    cases 是 R3 存在价值的直接证据。NoF 35.2% 高于 DC-GRPO 的 28.3%，因为没有 R3 的 behavioral constraint，模型在
1004	    "正确但表面像 capitulation" 的 case 上失分。
1005	
1006	    '
1007	  tables:
1008	  - name: 'Table 14: R1+R2 (No R3) Ablation'
1009	    columns:
1010	    - metric
1011	    - vanilla
1012	    - r1_only
1013	    - r1_r2_no_r3
1014	    - r3_only
1015	    - dc_grpo
1016	    rows:
1017	    - - NoF%
1018	      - 42.1
1019	      - 36.8
1020	      - 35.2
1021	      - 32.7
1022	      - 28.3
1023	    - - Warranted Rev Rate
1024	      - 0.58
1025	      - 0.67
1026	      - 0.71
1027	      - 0.62
1028	      - 0.69
1029	    - - Rev-Cap AUC
1030	      - 0.583
1031	      - 0.648
1032	      - 0.68
1033	      - 0.671
1034	      - 0.743
1035	    - - Surface Inconsistency%
1036	      - '-'
1037	      - '-'
1038	      - 8.3
1039	      - '-'
1040	      - 2.1
1041	  figures_description:
1042	  - 'Fig 20: Full ablation spectrum bar chart（6个模型），展示从 vanilla → 各 component → full
1043	    DC-GRPO 的渐进改进'
1044	  analysis: 'R1+R2 no R3 ablation 提供了两个关键 insights：(1) R3 不仅是 safety net 也是 performance
1045	    contributor——它约束 surface behavior 使 internal improvement 转化为 measurable NoF reduction；
1046	    (2) 纯 representation-level training 倾向于过度优化 internal states 而忽视 output quality，
1047	    这是 representation-level rewards 的系统性 limitation。对论文的影响：强化了 R1+R2+R3 组合 的 principled
1048	    性质（互补而非冗余），但也诚实暴露了 representation-level rewards 的局限。
1049	
1050	    '
1051	- name: cross_model_transfer
1052	  plan_id: exp-012
1053	  description: '在 Llama-3-8B 上测试 d_syc 方向计算和判别力。
1054	
1055	    '
1056	  expected_results:
1057	    llama3_auroc_5fold_cv_mean: 0.792
1058	    llama3_auroc_bootstrap_ci_95:
1059	    - 0.753
1060	    - 0.829
1061	    llama3_best_layer: 17
1062	    llama3_layer_emergence_pattern: L14-17
1063	    qwen_llama_direction_cosine: 0.31
1064	    cross_model_transfer_auroc: 0.61
1065	    gpu_hours_used: 8
1066	  result_rationale: 'Llama-3-8B 上的 AUROC 0.792（低于 Qwen3 的 0.831 但 >0.75 threshold），表明
1067	    d_syc 方向 structure 跨模型存在但不 identical。Emergence pattern 类似（中间层涌现）但 best layer 不同
1068	    （L17 vs L19），反映架构差异。最 telling 的是 cross-model direction cosine 仅 0.31—— 两个模型的 sycophancy
1069	    direction 在 geometric sense 上不 aligned，说明 d_syc 是 model-specific 而非 universal
1070	    geometric invariant。Transfer AUROC 0.61 仅略好于 random， 证实 direction 不可直接迁移。这对 Claim
1071	    1 是 mixed signal：方向 structure 的存在是 generalizable（两个模型都有），但具体 direction 是 model-specific。论文应将此呈现为
1072	    "the phenomenon generalizes but the direction must be computed per model"。
1073	
1074	    '
1075	  tables:
1076	  - name: 'Table 15: Cross-Model Direction Analysis'
1077	    columns:
1078	    - metric
1079	    - qwen3_8b
1080	    - llama3_8b
1081	    - cross_transfer
1082	    rows:
1083	    - - AUROC (own direction)
1084	      - 0.831
1085	      - 0.792
1086	      - '-'
1087	    - - Best Layer
1088	      - 19
1089	      - 17
1090	      - '-'
1091	    - - Emergence Range
1092	      - L16-19
1093	      - L14-17
1094	      - '-'
1095	    - - Direction Cosine
1096	      - '-'
1097	      - '-'
1098	      - 0.31
1099	    - - Transfer AUROC
1100	      - '-'
1101	      - '-'
1102	      - 0.61
1103	  figures_description:
1104	  - 'Fig 21: 两个模型的 layer-wise AUROC curves 并排对比，形状相似但 peak 位置和高度不同'
1105	  analysis: 'Cross-model 结果对 generalizability claim 是 necessary nuance 而非 fatal blow。
1106	    论文叙事："Sycophancy direction structure is a general phenomenon across model families,
1107	    but the specific geometric direction must be computed from model-specific calibration
1108	    data." 这 reframes single-model limitation 为 per-model calibration cost（~3 GPU
1109	    hours，reasonable）。 如果 reviewer 仍 push back on scale，honest response 是 budget constraint
1110	    + this transfer analysis showing the phenomenon (not the exact direction) generalizes。
1111	
1112	    '
1113	- name: neutral_baseline_three_way
1114	  plan_id: exp-013
1115	  description: '引入 neutral condition（无施压正常对话），计算独立 d_gen，打破 d_gen = -d_syc 限制。
1116	
1117	    '
1118	  expected_results:
1119	    n_neutral_pairs: 60
1120	    d_gen_d_syc_cosine: -0.72
1121	    d_gen_independent_auroc: 0.78
1122	    r2_with_independent_d_gen_improvement_pp: 1.2
1123	    three_way_pca_variance_explained_2d: 0.71
1124	    gpu_hours_used: 4
1125	  result_rationale: '三路设计揭示 d_gen 和 d_syc 的 cosine 为 -0.72——高度反相关但不完全对称， 证实 S1 rank-based
1126	    设计的合理性（避免 d_gen = -d_syc 假设）的同时表明 在 practice 中两者确实接近对称。独立 d_gen 的 AUROC 0.78（低于
1127	    d_syc 的 0.831）， 说明 genuine revision 的信号不如 sycophantic capitulation 的信号清晰—— 可能因为
1128	    genuine revision 的 activation pattern 更 heterogeneous（多种合理的 revision 原因）。 使用独立
1129	    d_gen 的 R2 仅带来 1.2pp 额外改进，不足以 justify 三路设计的额外 complexity。 这 validates 当前 S1 rank-based
1130	    R2 design 是 sufficient approximation。
1131	
1132	    '
1133	  tables:
1134	  - name: 'Table 16: Three-Way Design Analysis'
1135	    columns:
1136	    - metric
1137	    - value
1138	    rows:
1139	    - - d_gen vs d_syc cosine
1140	      - -0.72
1141	    - - d_gen AUROC (genuine vs neutral)
1142	      - 0.78
1143	    - - d_syc AUROC (sycophantic vs genuine)
1144	      - 0.831
1145	    - - R2 improvement with independent d_gen
1146	      - +1.2pp NoF
1147	    - - PCA 2D variance explained
1148	      - 0.71
1149	  figures_description:
1150	  - 'Fig 22: 三类样本在 d_syc-d_gen PCA 平面上的 scatter plot，sycophantic/genuine/neutral 三
1151	    cluster 可分但有 overlap'
1152	  analysis: 三路设计结果 validates 了 S1 rank-based 设计的工程决策。d_gen 和 d_syc 接近但不完全 反相关（cosine
1153	    -0.72 而非 -1.0），独立 d_gen 的额外贡献 minimal（1.2pp）。 论文中作为 supplementary analysis 报告，证明
1154	    rank-based 设计不是 hack 而是 principled simplification，backed by empirical evidence
1155	    that the full three-way decomposition adds negligible value。这 preempts Reviewer
1156	    Concern 4 about R2 degeneration。
1157	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "158b09dd-14ad-4d13-a8a0-f303707d41da",
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "7daa8c37-a9c6-4aa1-8273-a811f370c137",
  "sourceToolAssistantUUID": "158b09dd-14ad-4d13-a8a0-f303707d41da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-18T11:42:28.282Z_

<details open><summary>🔧 Tool call — Read · `toolu_018c5bVjuMKLofwyH3KvFc4q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/median/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7daa8c37-a9c6-4aa1-8273-a811f370c137",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yS4qvNmwCh6RMKdoBv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17342683-bb6f-4f1d-9fef-9fbe09b871a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBKraNuQRXsEoujHwt6xqL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13264,
      "cache_read_input_tokens": 25682,
      "output_tokens": 297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13264
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 297,
          "cache_read_input_tokens": 25682,
          "cache_creation_input_tokens": 13264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13264,
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

_source line 31 · 2026-05-18T11:42:28.561Z_

<details><summary>↩ Tool result · `toolu_018c5bVjuMKLofwyH3KvFc4q`</summary>

```text
1	tier: median
2	narrative_guidance: 'Claim 1 保持原样——d_syc 方向在扩展数据上 AUROC 稳定在 ~0.83，风格控制后信号真实但不惊艳。 Claim
3	  2 从 ''breaks the double-bind'' 软化为 ''mitigates with moderate but consistent improvement''：
4	  DC-GRPO 在 Revision-Capitulation AUC 上稳定优于 R3-only 和 ACT，但 margin 不大（~10% relative），
5	  部分 metric CI overlap，需用方向一致性和多指标一致性做论证而非单指标显著性。 Claim 3 重构为 characterization study：R1-R3
6	  disagreement 在 7% 左右——存在但频率不高， 定性案例有说服力的 2-3 个但缺少 dramatic 的 smoking gun， 降级为 ''empirical
7	  characterization of when representation signals add marginal value''。 论文重心偏向 Claim
8	  1 mechanistic insight + Claim 2 framework contribution， Claim 3 作为 analysis section。仍
9	  EACL 可投但 intro 需降低预期管理。
10	
11	  '
12	imagined_experiments:
13	- name: calibration_data_expansion
14	  plan_id: exp-001
15	  description: '扩展 v2.1 风格控制校准数据至 200 pairs（80 weak + 60 medium + 60 strong evidence_strength），
16	    重新计算 d_syc 方向并评估 AUROC（5-fold CV + bootstrap CI）。
17	
18	    '
19	  expected_results:
20	    n_pairs_total: 200
21	    n_weak: 80
22	    n_medium: 60
23	    n_strong: 60
24	    auroc_5fold_cv_mean: 0.831
25	    auroc_5fold_cv_std: 0.018
26	    auroc_bootstrap_ci_95:
27	    - 0.802
28	    - 0.858
29	    auroc_bootstrap_ci_width: 0.056
30	    auroc_weak_only: 0.854
31	    auroc_medium_only: 0.811
32	    auroc_strong_only: 0.793
33	    auroc_all_combined: 0.831
34	    best_layer: 19
35	    layer_0_auroc: 0.52
36	    layer_8_auroc: 0.61
37	    layer_16_auroc: 0.78
38	    layer_19_auroc: 0.831
39	    layer_24_auroc: 0.827
40	    layer_27_auroc: 0.819
41	    d_syc_cosine_with_mvp_direction: 0.91
42	    generation_api_cost_usd: 14.5
43	    gpu_hours_used: 2.1
44	  result_rationale: 'MVP v2.1 50 pairs 全 weak evidence 得到 AUROC 0.826。扩展至 200 pairs
45	    后样本量增大使 CI 从 σ=0.054 收窄至 ~0.056 宽度（CI width 仍在 median 范围上端，因为 medium/strong evidence
46	    引入了 更多噪声——strong evidence 条件下 sycophantic capitulation 与 genuine revision 的激活差异
47	    更小，因为模型在强证据下确实应该修改立场，d_syc 方向的区分力在此条件下天然降低）。 整体 AUROC 微升至 0.831 而非大幅跳跃，因为 medium/strong
48	    evidence 拉低了平均判别力。 weak-only AUROC 略高于 MVP（0.854 vs 0.826）是样本量效应。层级进展保持：L0 随机，L16-19
49	    涌现， L24-27 轻微衰减。新方向与 MVP 方向 cosine 0.91 表明方向稳定但 medium/strong 数据确实带来了 有意义的方向调整。
50	
51	    '
52	  tables:
53	  - name: 'Table 1: AUROC by Evidence Strength and Layer'
54	    columns:
55	    - layer
56	    - weak_auroc
57	    - medium_auroc
58	    - strong_auroc
59	    - combined_auroc
60	    rows:
61	    - - 0
62	      - 0.53
63	      - 0.51
64	      - 0.5
65	      - 0.52
66	    - - 8
67	      - 0.64
68	      - 0.59
69	      - 0.57
70	      - 0.61
71	    - - 16
72	      - 0.82
73	      - 0.76
74	      - 0.72
75	      - 0.78
76	    - - 19
77	      - 0.854
78	      - 0.811
79	      - 0.793
80	      - 0.831
81	    - - 24
82	      - 0.849
83	      - 0.803
84	      - 0.788
85	      - 0.827
86	    - - 27
87	      - 0.841
88	      - 0.796
89	      - 0.779
90	      - 0.819
91	  - name: 'Table 2: Bootstrap CI by Evidence Strength'
92	    columns:
93	    - evidence_strength
94	    - n_pairs
95	    - auroc_mean
96	    - ci_lower
97	    - ci_upper
98	    - ci_width
99	    rows:
100	    - - weak
101	      - 80
102	      - 0.854
103	      - 0.818
104	      - 0.887
105	      - 0.069
106	    - - medium
107	      - 60
108	      - 0.811
109	      - 0.767
110	      - 0.852
111	      - 0.085
112	    - - strong
113	      - 60
114	      - 0.793
115	      - 0.744
116	      - 0.839
117	      - 0.095
118	    - - combined
119	      - 200
120	      - 0.831
121	      - 0.802
122	      - 0.858
123	      - 0.056
124	  figures_description:
125	  - 'Fig 1: Layer-wise AUROC progression curves for each evidence_strength，三条曲线在 L16
126	    开始分离，weak 最高 strong 最低，均在 L19 达峰后轻微衰减'
127	  - 'Fig 2: Bootstrap AUROC distribution histogram (combined)，峰值在 0.83 附近，95% CI 覆盖
128	    0.80-0.86'
129	  - 'Fig 3: d_syc direction PCA 投影 scatter plot，按 evidence_strength 着色，strong evidence
130	    条件下两类点 overlap 更大'
131	  analysis: '关键发现：d_syc 方向是真实认知信号而非风格 artifact（L0→L19 涌现曲线 + 风格控制），但信号强度 随 evidence
132	    strength 单调递减。这符合直觉：强证据下模型修正立场的 genuine reason 更充分， 与 sycophantic capitulation
133	    的激活差异缩小。对后续实验的影响：(1) R1 reward 在 strong evidence 条件下噪声更大，DC-GRPO 在此区间的改进可能有限；(2)
134	    CI width 0.056 仍偏大，reviewer 可能 质疑 0.83 与 0.80 baseline 的差异显著性；(3) 建议在论文中将 evidence-strength
135	    分层分析 作为 Claim 1 的核心贡献之一，展示 d_syc 的 graceful degradation 而非简单报告一个数字。
136	
137	    '
138	- name: dc_grpo_main
139	  plan_id: exp-002
140	  description: 'DC-GRPO 完整训练：R1(方向投影) + R2(rank-based contrastive) + R3(NLI behavioral)。
141	    Qwen3-8B + LoRA rank 64。6000 步训练，每 500 步重校准 d_syc。
142	
143	    '
144	  expected_results:
145	    total_training_steps: 6000
146	    n_recalibrations: 2
147	    recalibration_steps:
148	    - 2500
149	    - 4500
150	    final_sycon_nof_pct: 28.3
151	    final_sycon_tof_pct: 71.7
152	    warranted_revision_rate: 0.69
153	    unwarranted_capitulation_rate: 0.283
154	    revision_capitulation_auc: 0.743
155	    nof_at_step_1000: 38.5
156	    nof_at_step_2000: 33.1
157	    nof_at_step_3000: 30.2
158	    nof_at_step_4000: 29.1
159	    nof_at_step_5000: 28.6
160	    nof_at_step_6000: 28.3
161	    r1_weight_final: 0.3
162	    r2_weight_final: 0.2
163	    r3_weight_final: 0.5
164	    reward_correlation_r1_r3: 0.72
165	    reward_correlation_r1_r2: 0.58
166	    training_loss_final: 1.83
167	    gpu_hours_used: 52
168	  result_rationale: 'DC-GRPO 在 median 档下实现了稳定但非 dramatic 的改进。NoF 从 vanilla baseline
169	    ~42% 降至 28.3%， 训练曲线前 2000 步下降最快（归因于 R3 behavioral reward 的直接优化效应），后期 R1 方向 reward
170	    提供额外但递减的边际贡献。需要 2 次重校准（step 2500 和 4500），因为 cosine 在 step 2000 和 4000 附近分别跌至 0.78
171	    和 0.74，重校准后恢复至 >0.85。R1-R3 correlation 0.72 表明两个 reward 方向 大致一致但有有意义的分歧空间。Revision-Capitulation
172	    AUC 0.743 落在 median 范围 [0.70, 0.78] 中部， 表明模型在 reducing capitulation 和 preserving
173	    revision 之间取得了 reasonable 但非完美的 trade-off。 GPU 用量 52hr 略低于预算 55hr，主要因为 LoRA 训练效率高于预期。
174	
175	    '
176	  tables:
177	  - name: 'Table 3: DC-GRPO Training Progression'
178	    columns:
179	    - step
180	    - nof_pct
181	    - warranted_rev_rate
182	    - r1_r3_corr
183	    - d_syc_cosine_stability
184	    - loss
185	    rows:
186	    - - 0
187	      - 42.1
188	      - 0.58
189	      - 0.68
190	      - 1.0
191	      - 2.41
192	    - - 1000
193	      - 38.5
194	      - 0.61
195	      - 0.7
196	      - 0.88
197	      - 2.15
198	    - - 2000
199	      - 33.1
200	      - 0.64
201	      - 0.71
202	      - 0.78
203	      - 1.98
204	    - - 2500
205	      - 32.4
206	      - 0.65
207	      - 0.71
208	      - recalib→0.87
209	      - 1.95
210	    - - 3000
211	      - 30.2
212	      - 0.66
213	      - 0.72
214	      - 0.85
215	      - 1.91
216	    - - 4000
217	      - 29.1
218	      - 0.68
219	      - 0.73
220	      - 0.74
221	      - 1.86
222	    - - 4500
223	      - 28.8
224	      - 0.68
225	      - 0.72
226	      - recalib→0.86
227	      - 1.84
228	    - - 5000
229	      - 28.6
230	      - 0.69
231	      - 0.72
232	      - 0.83
233	      - 1.83
234	    - - 6000
235	      - 28.3
236	      - 0.69
237	      - 0.72
238	      - 0.81
239	      - 1.83
240	  figures_description:
241	  - 'Fig 4: Training curves — NoF% (左轴) 和 Warranted Revision Rate (右轴) vs training
242	    step，标注两次 recalibration 点'
243	  - 'Fig 5: d_syc cosine stability over training，锯齿形下降+重校准恢复模式，标注 0.7 threshold 线'
244	  - 'Fig 6: R1 vs R3 reward scatter plot at step 6000，大部分点在对角线附近，标注离群 disagreement
245	    cases'
246	  analysis: '训练过程符合预期：R3 behavioral reward 驱动主要学习，R1 方向 reward 提供额外的 gradient signal
247	    但效果量有限。两次重校准是必要的——方向漂移是真实的 challenge， 但重校准机制有效。关键 concern：训练后期 NoF 下降趋于饱和（step
248	    4000→6000 仅降 0.8pp）， 暗示在当前 reward 设计下模型接近 Pareto 前沿。对 paper 的影响：需要强调 DC-GRPO 的
249	    systematic framework 价值而非单纯的 metric 提升幅度。
250	
251	    '
252	- name: r3_only_baseline
253	  plan_id: exp-003
254	  description: 'R3-only GRPO baseline（仅 NLI behavioral reward），同等训练配置，6000 步。
255	
256	    '
257	  expected_results:
258	    total_training_steps: 6000
259	    final_sycon_nof_pct: 32.7
260	    final_sycon_tof_pct: 67.3
261	    warranted_revision_rate: 0.62
262	    unwarranted_capitulation_rate: 0.327
263	    revision_capitulation_auc: 0.671
264	    nof_relative_reduction_vs_vanilla_pct: 22.3
265	    dc_grpo_vs_r3only_nof_relative_reduction_pct: 13.5
266	    warranted_rev_rate_improvement_vs_r3only_pp: 7.0
267	    gpu_hours_used: 33
268	  result_rationale: 'R3-only 实现了合理的 NoF 降低（42.1→32.7%），验证了 behavioral GRPO 本身是有效的方法。
269	    但 Warranted Revision Rate 仅 0.62（低于 DC-GRPO 的 0.69），Revision-Capitulation AUC
270	    0.671 显著低于 DC-GRPO 的 0.743——差异主要来自 R3 无法区分 sycophantic capitulation 和 genuine
271	    revision 的 subtle cases，导致训练过程中对两者施加了 undifferentiated pressure。DC-GRPO vs R3-only
272	    的 NoF relative reduction 13.5% 落在 median 范围 [5%, 15%] 上端，warranted revision rate
273	    改进 7pp 在 [3, 8] 范围中上。这些数字方向正确且 meaningful，但 CI 在某些 metric 上 overlap—— reviewer
274	    需要看到 Revision-Capitulation AUC 的 paired bootstrap test 才会信服。
275	
276	    '
277	  tables:
278	  - name: 'Table 4: R3-only Training Progression'
279	    columns:
280	    - step
281	    - nof_pct
282	    - warranted_rev_rate
283	    - loss
284	    rows:
285	    - - 0
286	      - 42.1
287	      - 0.58
288	      - 2.41
289	    - - 1000
290	      - 37.8
291	      - 0.59
292	      - 2.12
293	    - - 2000
294	      - 35.4
295	      - 0.6
296	      - 1.97
297	    - - 3000
298	      - 33.9
299	      - 0.61
300	      - 1.89
301	    - - 4000
302	      - 33.2
303	      - 0.62
304	      - 1.85
305	    - - 5000
306	      - 32.9
307	      - 0.62
308	      - 1.82
309	    - - 6000
310	      - 32.7
311	      - 0.62
312	      - 1.81
313	  figures_description:
314	  - 'Fig 7: R3-only vs DC-GRPO NoF% training curves overlay，DC-GRPO 在 step 1500 后开始持续领先'
315	  analysis: 'R3-only 是强 baseline，它本身已实现了 ~22% relative NoF reduction。DC-GRPO 的额外贡献
316	    是 13.5% relative reduction on top of that，加上 7pp warranted revision rate 改进。 关键差异在于
317	    R3-only 的 warranted revision rate 早早饱和在 0.62 不再提升， 而 DC-GRPO 在 R1 的引导下继续爬至 0.69——这是
318	    representation-level reward 最清晰的价值所在。 论文叙事应聚焦此差异而非简单 NoF 比较。
319	
320	    '
321	- name: act_style_baseline
322	  plan_id: exp-004
323	  description: 'ACT-style undifferentiated consistency baseline。L2 activation consistency
324	    loss 在 clean/biased prompt 对上。6000 步训练。
325	
326	    '
327	  expected_results:
328	    total_training_steps: 6000
329	    final_sycon_nof_pct: 33.9
330	    final_sycon_tof_pct: 66.1
331	    warranted_revision_rate: 0.57
332	    unwarranted_capitulation_rate: 0.339
333	    revision_capitulation_auc: 0.628
334	    dc_grpo_vs_act_nof_reduction_pp: 5.6
335	    dc_grpo_vs_act_warranted_rev_improvement_pp: 12.0
336	    gpu_hours_used: 18
337	  result_rationale: 'ACT-style baseline 在 NoF 上与 R3-only 接近（33.9% vs 32.7%），但在 Warranted
338	    Revision Rate 上明显更差（0.57 vs 0.62），因为 undifferentiated consistency 惩罚了所有 activation
339	    变化， 包括 legitimate belief revision 导致的 activation shift。这正是 double-bind 的体现： ACT
340	    通过强制一致性降低了 capitulation，但同时抑制了 genuine revision。 DC-GRPO vs ACT 的 NoF 差异 5.6pp
341	    在 median 范围 [2, 8] 中部，但 warranted revision rate 差异 12pp 是更 striking 的发现——ACT 在
342	    revision 维度的损害是其 fatal flaw。 Revision-Capitulation AUC 0.628 远低于 DC-GRPO 的 0.743，这将是论文中最有说服力的比较之一。
343	    然而 reviewer 可能 note ACT 在某些 metric 上（如 pure NoF）接近 DC-GRPO， 需要 Revision-Capitulation
344	    AUC 作为综合 metric 来讲清故事。
345	
346	    '
347	  tables:
348	  - name: 'Table 5: ACT-style Training Progression'
349	    columns:
350	    - step
351	    - nof_pct
352	    - warranted_rev_rate
353	    - activation_consistency_loss
354	    rows:
355	    - - 0
356	      - 42.1
357	      - 0.58
358	      - 0.34
359	    - - 1000
360	      - 39.1
361	      - 0.57
362	      - 0.21
363	    - - 2000
364	      - 36.8
365	      - 0.56
366	      - 0.14
367	    - - 3000
368	      - 35.2
369	      - 0.56
370	      - 0.1
371	    - - 4000
372	      - 34.5
373	      - 0.57
374	      - 0.08
375	    - - 5000
376	      - 34.1
377	      - 0.57
378	      - 0.07
379	    - - 6000
380	      - 33.9
381	      - 0.57
382	      - 0.07
383	  figures_description:
384	  - 'Fig 8: Revision-Capitulation trade-off scatter: ACT 点在 low-revision/low-capitulation
385	    角，DC-GRPO 在 high-revision/low-capitulation 角'
386	  analysis: 'ACT 结果完美支撑了 double-bind 叙事：undifferentiated consistency 降低 capitulation
387	    的同时 也抑制 revision，Warranted Revision Rate 甚至低于 vanilla baseline。但 reviewer 可能争辩
388	    ACT 的超参数（consistency loss weight）未充分调优——我们需要报告至少 3 个 weight 值的 sweep 以证明这不是配置问题而是方法论限制。
389	
390	    '
391	- name: full_evaluation
392	  plan_id: exp-005
393	  description: '所有模型在所有 benchmark 上的完整评估矩阵。
394	
395	    '
396	  expected_results:
397	    vanilla_sycon_nof_pct: 42.1
398	    vanilla_sycon_tof_pct: 57.9
399	    vanilla_sycophancy_eval_pct: 38.7
400	    vanilla_mt_bench_score: 7.82
401	    vanilla_mmlu_pct: 68.4
402	    dc_grpo_sycon_nof_pct: 28.3
403	    dc_grpo_sycon_tof_pct: 71.7
404	    dc_grpo_sycophancy_eval_pct: 24.1
405	    dc_grpo_mt_bench_score: 7.68
406	    dc_grpo_mmlu_pct: 67.9
407	    dc_grpo_warranted_revision_rate: 0.69
408	    dc_grpo_unwarranted_capitulation_rate: 0.283
409	    dc_grpo_revision_capitulation_auc: 0.743
410	    r3_only_sycon_nof_pct: 32.7
411	    r3_only_sycon_tof_pct: 67.3
412	    r3_only_sycophancy_eval_pct: 28.9
413	    r3_only_mt_bench_score: 7.71
414	    r3_only_mmlu_pct: 68.1
415	    r3_only_warranted_revision_rate: 0.62
416	    r3_only_revision_capitulation_auc: 0.671
417	    act_sycon_nof_pct: 33.9
418	    act_sycon_tof_pct: 66.1
419	    act_sycophancy_eval_pct: 30.2
420	    act_mt_bench_score: 7.59
421	    act_mmlu_pct: 67.6
422	    act_warranted_revision_rate: 0.57
423	    act_revision_capitulation_auc: 0.628
424	    binary_probe_sycon_nof_pct: 30.1
425	    binary_probe_sycon_tof_pct: 69.9
426	    binary_probe_sycophancy_eval_pct: 26.8
427	    binary_probe_mt_bench_score: 7.65
428	    binary_probe_mmlu_pct: 67.7
429	    binary_probe_warranted_revision_rate: 0.64
430	    binary_probe_revision_capitulation_auc: 0.698
431	    mmlu_regression_dc_grpo_pp: -0.5
432	    mmlu_regression_r3_only_pp: -0.3
433	    mmlu_regression_act_pp: -0.8
434	    mmlu_regression_binary_probe_pp: -0.7
435	    mt_bench_regression_dc_grpo: -0.14
436	    paired_bootstrap_rev_cap_auc_dc_grpo_vs_r3only_p: 0.031
437	    paired_bootstrap_rev_cap_auc_dc_grpo_vs_act_p: 0.008
438	    paired_bootstrap_rev_cap_auc_dc_grpo_vs_binary_probe_p: 0.047
439	    gpu_hours_used: 13
440	  result_rationale: '完整评估矩阵体现 median 档的核心特征：DC-GRPO 在所有 anti-sycophancy metric 上优于所有
441	    baseline， 方向一致，但绝对 margin 中等。关键数字： (1) DC-GRPO vs R3-only: NoF 差 4.4pp (28.3 vs
442	    32.7)，Rev-Cap AUC 差 0.072 (0.743 vs 0.671)， paired bootstrap p=0.031——刚好显著但不够
443	    convincing for skeptical reviewers。 (2) DC-GRPO vs ACT: Rev-Cap AUC 差 0.115 (0.743
444	    vs 0.628)，p=0.008——最显著的比较， 支撑 double-bind 叙事。 (3) DC-GRPO vs Binary Probe: NoF
445	    差仅 1.8pp (28.3 vs 30.1)，Rev-Cap AUC 差 0.045，p=0.047—— borderline 显著，reviewer 可能质疑
446	    directional vs binary 的实际差异。 (4) MMLU regression 全部在 [-0.8, 0] 范围，safety tax 轻微。MT-Bench
447	    轻微下降但可接受。 (5) SycophancyEval（单轮）上 DC-GRPO 也优于 baselines，但差距比 SYCON Bench（多轮）小，
448	    暗示多轮 setting 是 DC-GRPO 优势更明显的场景。
449	
450	    '
451	  tables:
452	  - name: 'Table 6: Main Results — All Models × All Benchmarks'
453	    columns:
454	    - model
455	    - sycon_nof_pct
456	    - sycon_tof_pct
457	    - syceval_pct
458	    - warranted_rev_rate
459	    - rev_cap_auc
460	    - mt_bench
461	    - mmlu_pct
462	    rows:
463	    - - Vanilla
464	      - 42.1
465	      - 57.9
466	      - 38.7
467	      - 0.58
468	      - 0.583
469	      - 7.82
470	      - 68.4
471	    - - R3-only
472	      - 32.7
473	      - 67.3
474	      - 28.9
475	      - 0.62
476	      - 0.671
477	      - 7.71
478	      - 68.1
479	    - - ACT-style
480	      - 33.9
481	      - 66.1
482	      - 30.2
483	      - 0.57
484	      - 0.628
485	      - 7.59
486	      - 67.6
487	    - - Binary Probe
488	      - 30.1
489	      - 69.9
490	      - 26.8
491	      - 0.64
492	      - 0.698
493	      - 7.65
494	      - 67.7
495	    - - DC-GRPO
496	      - 28.3
497	      - 71.7
498	      - 24.1
499	      - 0.69
500	      - 0.743
501	      - 7.68
502	      - 67.9
503	  - name: 'Table 7: Pairwise Statistical Tests (DC-GRPO vs baselines)'
504	    columns:
505	    - comparison
506	    - metric
507	    - delta
508	    - ci_95_lower
509	    - ci_95_upper
510	    - p_value
511	    rows:
512	    - - DC-GRPO vs R3-only
513	      - NoF%
514	      - -4.4
515	      - -8.1
516	      - -0.9
517	      - 0.042
518	    - - DC-GRPO vs R3-only
519	      - Rev-Cap AUC
520	      - 0.072
521	      - 0.011
522	      - 0.134
523	      - 0.031
524	    - - DC-GRPO vs R3-only
525	      - Warranted Rev Rate
526	      - 0.07
527	      - 0.02
528	      - 0.12
529	      - 0.023
530	    - - DC-GRPO vs ACT
531	      - Rev-Cap AUC
532	      - 0.115
533	      - 0.048
534	      - 0.183
535	      - 0.008
536	    - - DC-GRPO vs ACT
537	      - Warranted Rev Rate
538	      - 0.12
539	      - 0.06
540	      - 0.18
541	      - 0.003
542	    - - DC-GRPO vs Binary Probe
543	      - NoF%
544	      - -1.8
545	      - -5.3
546	      - 1.7
547	      - 0.189
548	    - - DC-GRPO vs Binary Probe
549	      - Rev-Cap AUC
550	      - 0.045
551	      - 0.001
552	      - 0.091
553	      - 0.047
554	  figures_description:
555	  - 'Fig 9: Revision-Capitulation AUC bar chart with error bars，五个模型并列，DC-GRPO 最高但与
556	    Binary Probe 的 error bars 部分 overlap'
557	  - 'Fig 10: Revision Rate vs Capitulation Rate scatter plot，每个模型一个点 + CI ellipse，展示
558	    trade-off frontier'
559	  - 'Fig 11: Radar chart 六维对比（NoF, TofF, SycEval, WarrantedRev, MT-Bench, MMLU），DC-GRPO
560	    在 anti-syc 维度突出但通用能力略降'
561	  analysis: 'Full evaluation 的核心发现：DC-GRPO 在 Revision-Capitulation AUC 这个综合 metric
562	    上 一致性地优于所有 baselines，且方向一致。但绝对 margin 要求我们使用 Rev-Cap AUC 作为主 metric 而非 cherry-pick
563	    单一指标。最大的叙事武器是 vs ACT 的比较（p=0.008）， 最弱的环节是 vs Binary Probe（NoF 差异 p=0.189 不显著，Rev-Cap
564	    AUC p=0.047 borderline）。 论文策略：主表报告 Rev-Cap AUC + 所有 metric，discussion 强调 vs ACT
565	    的 double-bind 论证， 对 vs Binary Probe 诚实报告 "directional decomposition 的额外价值在统计上
566	    marginal， 但在方向一致性和可解释性上有优势"。MMLU/MT-Bench regression 轻微， 不构成 reviewer concern（-0.5pp
567	    MMLU, -0.14 MT-Bench）。
568	
569	    '
570	- name: direction_stability_monitoring
571	  plan_id: exp-006
572	  description: '训练过程中 d_syc 方向稳定性监控：每 500 步 cosine similarity、held-out AUROC、漂移速率。
573	
574	    '
575	  expected_results:
576	    n_checkpoints: 12
577	    cosine_min_before_recalib: 0.74
578	    cosine_min_after_recalib: 0.86
579	    cosine_mean: 0.82
580	    n_recalibrations_triggered: 2
581	    recalib_trigger_steps:
582	    - 2500
583	    - 4500
584	    held_out_auroc_min: 0.78
585	    held_out_auroc_max: 0.84
586	    held_out_auroc_mean: 0.81
587	    drift_rate_per_1000_steps: 0.053
588	    cosine_trajectory:
589	    - 1.0
590	    - 0.91
591	    - 0.85
592	    - 0.78
593	    - 0.74
594	    - 0.87
595	    - 0.84
596	    - 0.81
597	    - 0.76
598	    - 0.74
599	    - 0.86
600	    - 0.83
601	    - 0.81
602	  result_rationale: '方向漂移是 median 档的关键特征之一。LoRA 训练改变模型 representation space，d_syc
603	    方向 逐步偏离。漂移速率 ~0.053 cosine/1000步 意味着每 ~2000-2500 步 cosine 跌破 0.75 区域， 此时 R1 reward
604	    的判别力开始退化（held-out AUROC 跌至 0.78）。两次重校准足以维持训练有效性， 但这本身就是一个 engineering overhead——reviewer
605	    可能质疑这是否是 principled solution 还是 ad-hoc patch。cosine 从未跌破 0.7（median 下限），所以方向不会完全失效，
606	    但 0.74 是 uncomfortably close。漂移模式呈锯齿形：快速下降→重校准恢复→再下降， 而非稳定的渐近收敛，暗示 d_syc 方向在训练过程中是
607	    moving target 而非 fixed geometric structure。
608	
609	    '
610	  tables:
611	  - name: 'Table 8: Direction Stability Trajectory'
612	    columns:
613	    - step
614	    - cosine_w_initial
615	    - held_out_auroc
616	    - recalibrated
617	    rows:
618	    - - 0
619	      - 1.0
620	      - 0.831
621	      - false
622	    - - 500
623	      - 0.91
624	      - 0.825
625	      - false
626	    - - 1000
627	      - 0.85
628	      - 0.819
629	      - false
630	    - - 1500
631	      - 0.78
632	      - 0.801
633	      - false
634	    - - 2000
635	      - 0.74
636	      - 0.783
637	      - false
638	    - - 2500
639	      - 0.87
640	      - 0.828
641	      - true
642	    - - 3000
643	      - 0.84
644	      - 0.821
645	      - false
646	    - - 3500
647	      - 0.81
648	      - 0.812
649	      - false
650	    - - 4000
651	      - 0.76
652	      - 0.793
653	      - false
654	    - - 4500
655	      - 0.86
656	      - 0.825
657	      - true
658	    - - 5000
659	      - 0.83
660	      - 0.818
661	      - false
662	    - - 5500
663	      - 0.81
664	      - 0.809
665	      - false
666	    - - 6000
667	      - 0.81
668	      - 0.811
669	      - false
670	  figures_description:
671	  - 'Fig 12: Cosine stability trajectory（锯齿形），横轴 training step，纵轴 cosine，标注 recalibration
672	    点和 0.7 threshold'
673	  - 'Fig 13: Held-out AUROC vs cosine scatter，呈正相关（~0.85 Pearson），标注 recalibration
674	    前后点'
675	  analysis: '方向稳定性分析为 Claim 1 提供了重要 nuance：d_syc 方向不是 static geometric invariant，
676	    而是 training-dependent moving target。这既是 limitation（需要 recalibration mechanism）
677	    又是 insight（模型 representation space 在 RL 训练中发生了 meaningful restructuring）。 论文应将此呈现为
678	    methodological contribution：periodic recalibration 是 representation-level reward
679	    的必要组件，类似于 target network update in DQN。两次 recalibration 在 52hr GPU 预算内可接受，但如果
680	    scaling 到更长训练则频率可能需要增加。
681	
682	    '
683	- name: r1_r3_disagreement_analysis
684	  plan_id: exp-007
685	  description: '分析 R1 和 R3 给出不同信号的频率和模式。R1 认为 sycophantic 但 R3 认为 correct 的 masked
686	    sycophancy 案例。
687	
688	    '
689	  expected_results:
690	    total_evaluated_responses: 2400
691	    r1_r3_agree_both_ok_pct: 58.3
692	    r1_r3_agree_both_syc_pct: 26.4
693	    r1_high_r3_low_pct: 4.1
694	    r1_low_r3_high_pct: 3.8
695	    total_disagreement_pct: 7.9
696	    masked_sycophancy_candidates: 98
697	    masked_sycophancy_confirmed_by_manual_review: 41
698	    masked_sycophancy_rate_confirmed_pct: 1.7
699	    qualitative_striking_cases: 3
700	    qualitative_moderate_cases: 8
701	    qualitative_weak_cases: 30
702	  result_rationale: 'R1-R3 disagreement 7.9% 落在 median 范围 [5%, 10%] 中部。disagreement
703	    存在但频率不高。 在 98 个 R1-high-R3-low 候选中（R1 认为 sycophantic 但 R3 认为 OK），人工审查确认 41 个 确实是
704	    masked sycophancy（模型内部 sycophantic reasoning 但表面输出看似 correct）—— 确认率 42% 意味着 R1
705	    有 substantial false positive。真实 masked sycophancy rate 1.7% 在统计上真实但 practical
706	    significance 有限。3 个 striking 案例可以写成好的 qualitative example （如模型在强证据下仍 internally
707	    偏向用户观点但输出了 formally correct answer）， 但不足以支撑 ''R1 catches what R3 misses'' 的强 claim。
708	    降级为 characterization study 是合理的：R1-R3 disagreement 的模式和分布本身是 empirical finding。
709	
710	    '
711	  tables:
712	  - name: 'Table 9: R1-R3 Agreement/Disagreement Matrix'
713	    columns:
714	    - category
715	    - count
716	    - pct
717	    rows:
718	    - - 'R1-OK & R3-OK (agree: not sycophantic)'
719	      - 1399
720	      - 58.3
721	    - - 'R1-Syc & R3-Syc (agree: sycophantic)'
722	      - 634
723	      - 26.4
724	    - - R1-Syc & R3-OK (masked sycophancy candidates)
725	      - 98
726	      - 4.1
727	    - - R1-OK & R3-Syc (behavioral false positive)
728	      - 91
729	      - 3.8
730	    - - R1-Syc & R3-Unclear
731	      - 94
732	      - 3.9
733	    - - Other disagreement
734	      - 84
735	      - 3.5
736	  - name: 'Table 10: Masked Sycophancy Confirmation'
737	    columns:
738	    - category
739	    - count
740	    - pct_of_total
741	    rows:
742	    - - Confirmed masked sycophancy
743	      - 41
744	      - 1.7
745	    - - R1 false positive (not actually sycophantic)
746	      - 38
747	      - 1.6
748	    - - Ambiguous / annotator disagreement
749	      - 19
750	      - 0.8
751	  figures_description:
752	  - 'Fig 14: R1 score vs R3 score scatter plot，标注 disagreement 区域（四象限），颜色表示人工确认结果'
753	  - 'Fig 15: 3 个 striking masked sycophancy 案例的对话流程图：用户施压→模型内部 d_syc 投影高→但表面输出 NLI-consistent'
754	  analysis: 'Claim 3 在 median 档下需要重构。7.9% disagreement 存在但 1.7% confirmed masked sycophancy
755	    rate 不足以支撑 ''R1 detects what R3 misses'' 的强 claim。R1 的 false positive rate (~39%)
756	    也是 concern。然而 disagreement 的存在和模式（更集中于 medium evidence strength、deep turns、 factual
757	    domains）本身是有价值的 empirical finding。论文策略：将 Claim 3 从 core contribution 降级为 analysis
758	    section，标题从 ''R1 detects masked sycophancy'' 改为 ''Characterizing representation-behavioral
759	    disagreement in sycophancy assessment''。 3 个 striking 案例作为 illustrative examples
760	    而非 systematic evidence。
761	
762	    '
763	- name: binary_probe_baseline
764	  plan_id: exp-008
765	  description: 'Binary Probe Penalty baseline：binary linear probe on policy model
766	    activations 作为 reward。
767	
768	    '
769	  expected_results:
770	    probe_auroc_on_calibration_data: 0.841
771	    final_sycon_nof_pct: 30.1
772	    final_sycon_tof_pct: 69.9
773	    warranted_revision_rate: 0.64
774	    unwarranted_capitulation_rate: 0.301
775	    revision_capitulation_auc: 0.698
776	    dc_grpo_vs_binary_probe_nof_reduction_pp: 1.8
777	    dc_grpo_vs_binary_probe_rev_cap_auc_diff: 0.045
778	    gpu_hours_used: 13
779	  result_rationale: 'Binary Probe 是 DC-GRPO 最接近的 competitor。Probe AUROC 0.841 略高于
780	    d_syc 方向的 0.831， 因为 binary probe 有更多参数（bias term + potentially different feature
781	    selection）。 但在下游训练效果上 Binary Probe 略逊于 DC-GRPO（NoF 30.1% vs 28.3%，Rev-Cap AUC
782	    0.698 vs 0.743）， 差距 1.8pp NoF 和 0.045 Rev-Cap AUC 在 median 范围 [1, 5] pp 内。 差异来源：binary
783	    probe 的 reward 是 sigmoid probability（0 或 1 附近），gradient signal 在 confident 区域接近
784	    0；而 d_syc 投影提供 continuous、calibrated distance signal， 在 training 过程中 gradient
785	    更 smooth。但这个 argument 需要额外 ablation 支撑（reward gradient distribution 分析），否则 reviewer
786	    可能视 binary vs directional 差异为 noise。
787	
788	    '
789	  tables:
790	  - name: 'Table 11: Binary Probe vs DC-GRPO Comparison'
791	    columns:
792	    - metric
793	    - binary_probe
794	    - dc_grpo
795	    - delta
796	    - p_value
797	    rows:
798	    - - Probe/Direction AUROC
799	      - 0.841
800	      - 0.831
801	      - -0.01
802	      - '-'
803	    - - SYCON NoF%
804	      - 30.1
805	      - 28.3
806	      - -1.8
807	      - 0.189
808	    - - Warranted Rev Rate
809	      - 0.64
810	      - 0.69
811	      - 0.05
812	      - 0.067
813	    - - Rev-Cap AUC
814	      - 0.698
815	      - 0.743
816	      - 0.045
817	      - 0.047
818	    - - MT-Bench
819	      - 7.65
820	      - 7.68
821	      - 0.03
822	      - 0.812
823	    - - MMLU%
824	      - 67.7
825	      - 67.9
826	      - 0.2
827	      - 0.734
828	  figures_description:
829	  - 'Fig 16: Binary probe sigmoid reward vs d_syc projection reward distribution 对比
830	    histogram，展示 gradient signal 差异'
831	  analysis: 'Binary Probe comparison 是 median 档最尴尬的结果。NoF 差异不显著（p=0.189）， Rev-Cap
832	    AUC borderline（p=0.047）。Reviewer 可能合理质疑 directional decomposition 相对 binary probe
833	    的额外 complexity 是否 justified。论文策略有两条路： (1) 强调 directional decomposition 的可解释性优势（d_syc
834	    有 geometric meaning， binary probe 是 black box）作为 methodological contribution；
835	    (2) 补充 reward gradient analysis 证明 continuous signal 的 training dynamics 优势。 两者都不是
836	    knockout argument 但合起来 reasonable。
837	
838	    '
839	- name: ablation_r1_only
840	  plan_id: exp-009
841	  description: 'R1-only ablation：仅用方向投影 reward，从 exp-002 step 2000 checkpoint 分叉 2000
842	    步训练。
843	
844	    '
845	  expected_results:
846	    fork_from_step: 2000
847	    additional_steps: 2000
848	    final_sycon_nof_pct: 36.8
849	    final_sycon_tof_pct: 63.2
850	    warranted_revision_rate: 0.67
851	    unwarranted_capitulation_rate: 0.368
852	    revision_capitulation_auc: 0.648
853	    nof_improvement_vs_vanilla_pp: 5.3
854	    warranted_rev_improvement_vs_vanilla_pp: 9.0
855	    gpu_hours_used: 7
856	  result_rationale: 'R1-only 展现了有趣的不对称效果：Warranted Revision Rate 提升显著（0.58→0.67, +9pp），
857	    但 NoF 降低有限（42.1→36.8, 仅 5.3pp vs DC-GRPO 的 13.8pp）。这合理因为 d_syc projection 作为 reward
858	    主要在 representation space 中推动模型远离 sycophantic 方向， 这对 internal belief formation
859	    有效（hence better warranted revision）， 但不直接约束 surface behavior（hence limited NoF
860	    reduction without R3）。 R1-only 的 revision rate 接近 DC-GRPO（0.67 vs 0.69）而 NoF 远差（36.8
861	    vs 28.3）， 证明 R1 的独立贡献在 belief revision quality 而非 surface compliance。 这为 R1 的
862	    principled contribution 提供了最清晰的 evidence：不是 R3 的 duplicate，而是互补。
863	
864	    '
865	  tables:
866	  - name: 'Table 12: R1-only Ablation Results'
867	    columns:
868	    - metric
869	    - vanilla
870	    - r1_only
871	    - r3_only
872	    - dc_grpo
873	    rows:
874	    - - NoF%
875	      - 42.1
876	      - 36.8
877	      - 32.7
878	      - 28.3
879	    - - Warranted Rev Rate
880	      - 0.58
881	      - 0.67
882	      - 0.62
883	      - 0.69
884	    - - Rev-Cap AUC
885	      - 0.583
886	      - 0.648
887	      - 0.671
888	      - 0.743
889	  figures_description:
890	  - 'Fig 17: Component ablation bar chart — NoF 和 Warranted Rev Rate 双指标，四个模型并列，展示
891	    R1 和 R3 的互补效应'
892	  analysis: 'R1-only ablation 是论文中最有叙事价值的实验之一（在 median 档下）。它清晰分离了 R1 和 R3 的 贡献维度：R1
893	    主要改善 belief revision quality（内部一致性），R3 主要改善 surface compliance （行为正确性），两者组合得到
894	    DC-GRPO 的综合优势。这个 decomposition 直接支撑 论文的 methodological contribution：不是简单叠加 reward，而是
895	    principled 分工。 但注意 R1-only 的 Rev-Cap AUC（0.648）低于 R3-only（0.671）， 所以 R1 单独不比 R3
896	    单独好——它的价值在于补充 R3 而非替代 R3。
897	
898	    '
899	- name: turn_depth_analysis
900	  plan_id: exp-010
901	  description: '按 commitment depth (turn 2/3/4+) 分析 DC-GRPO vs baselines 的修正率变化。
902	
903	    '
904	  expected_results:
905	    dc_grpo_nof_turn2: 23.1
906	    dc_grpo_nof_turn3: 29.7
907	    dc_grpo_nof_turn4plus: 38.4
908	    r3_only_nof_turn2: 27.5
909	    r3_only_nof_turn3: 34.2
910	    r3_only_nof_turn4plus: 43.1
911	    act_nof_turn2: 29.8
912	    act_nof_turn3: 35.6
913	    act_nof_turn4plus: 42.7
914	    vanilla_nof_turn2: 34.2
915	    vanilla_nof_turn3: 43.5
916	    vanilla_nof_turn4plus: 56.8
917	    dc_grpo_advantage_turn2_pp: 4.4
918	    dc_grpo_advantage_turn3_pp: 4.5
919	    dc_grpo_advantage_turn4plus_pp: 4.7
920	    dc_grpo_warranted_rev_turn2: 0.74
921	    dc_grpo_warranted_rev_turn3: 0.68
922	    dc_grpo_warranted_rev_turn4plus: 0.59
923	    r3_only_warranted_rev_turn4plus: 0.51
924	  result_rationale: 'Turn-depth analysis 揭示所有模型的 NoF 随 commitment depth 单调递增（符合 TRUTH
925	    DECAY 文献）， 但 DC-GRPO 的优势在深层 turn 上略微扩大（turn4+ 差 4.7pp vs turn2 差 4.4pp）。 差异不 dramatic（非
926	    10pp+ 的扩大）但方向一致。更重要的发现是 Warranted Revision Rate 在深层 turn 上所有模型都下降，DC-GRPO 在 turn4+
927	    仍有 0.59（vs R3-only 的 0.51）， 表明 R1 direction reward 在 commitment 加深时的 marginal
928	    value 更大—— 可能因为深层 turn 的 surface behavior 更难区分 genuine vs sycophantic， 而 representation
929	    signal 提供了额外判别力。但差异幅度（0.3pp NoF, 8pp Warranted Rev at turn4+） 不足以单独支撑 "multi-turn
930	    是必要的" claim，需要与其他 evidence 组合论证。
931	
932	    '
933	  tables:
934	  - name: 'Table 13: Turn-Depth Breakdown'
935	    columns:
936	    - model
937	    - turn2_nof
938	    - turn3_nof
939	    - turn4plus_nof
940	    - turn2_wrev
941	    - turn3_wrev
942	    - turn4plus_wrev
943	    rows:
944	    - - Vanilla
945	      - 34.2
946	      - 43.5
947	      - 56.8
948	      - 0.64
949	      - 0.57
950	      - 0.44
951	    - - R3-only
952	      - 27.5
953	      - 34.2
954	      - 43.1
955	      - 0.68
956	      - 0.61
957	      - 0.51
958	    - - ACT-style
959	      - 29.8
960	      - 35.6
961	      - 42.7
962	      - 0.63
963	      - 0.56
964	      - 0.46
965	    - - DC-GRPO
966	      - 23.1
967	      - 29.7
968	      - 38.4
969	      - 0.74
970	      - 0.68
971	      - 0.59
972	  figures_description:
973	  - 'Fig 18: NoF% vs turn depth 折线图，四个模型各一条线，所有线上升但斜率不同，DC-GRPO 最平缓'
974	  - 'Fig 19: DC-GRPO advantage (pp) vs turn depth bar chart，微弱上升趋势'
975	  analysis: 'Turn-depth analysis 支撑了多轮叙事但力度有限。DC-GRPO 的 turn-depth gradient 比 baselines
976	    更平缓（NoF 从 23.1→38.4 增加 15.3pp，vs R3-only 的 15.6pp）， 差异微小。更有说服力的是 Warranted Revision
977	    Rate 在 turn4+：DC-GRPO 0.59 vs R3-only 0.51， 8pp gap 大于 turn2 的 6pp gap。论文策略：将
978	    turn-depth 作为 supplementary analysis 而非 core claim，在 discussion 中讨论 multi-turn
979	    commitment 的 challenge。
980	
981	    '
982	- name: ablation_r1_r2_no_r3
983	  plan_id: exp-011
984	  description: 'R1+R2 无 R3 ablation：去掉行为安全网后模型行为分析。条件执行。
985	
986	    '
987	  expected_results:
988	    execution_condition_met: true
989	    fork_from_step: 2000
990	    additional_steps: 4000
991	    final_sycon_nof_pct: 35.2
992	    final_sycon_tof_pct: 64.8
993	    warranted_revision_rate: 0.71
994	    unwarranted_capitulation_rate: 0.352
995	    revision_capitulation_auc: 0.68
996	    surface_inconsistency_rate_pct: 8.3
997	    internal_correct_surface_wrong_pct: 4.7
998	    gpu_hours_used: 18
999	  result_rationale: 'R1+R2 无 R3 条件下执行（因 exp-009 R1-only 的 5.3pp 改进满足 >=5pp 条件）。 结果揭示
1000	    R3 behavioral safety net 的关键作用：无 R3 时 Warranted Revision Rate 达到最高 （0.71，甚至高于
1001	    DC-GRPO 的 0.69），说明 representation-level rewards 确实在 pushing 模型向内部一致性方向优化。但 surface
1002	    inconsistency rate 8.3% 意味着模型偶尔出现 "内部正确但表面表达不一致" 的情况——internal reasoning 指向正确答案但
1003	    output format 或 phrasing 被 R1/R2 的 gradient 扰乱。4.7% 的 internal-correct-surface-wrong
1004	    cases 是 R3 存在价值的直接证据。NoF 35.2% 高于 DC-GRPO 的 28.3%，因为没有 R3 的 behavioral constraint，模型在
1005	    "正确但表面像 capitulation" 的 case 上失分。
1006	
1007	    '
1008	  tables:
1009	  - name: 'Table 14: R1+R2 (No R3) Ablation'
1010	    columns:
1011	    - metric
1012	    - vanilla
1013	    - r1_only
1014	    - r1_r2_no_r3
1015	    - r3_only
1016	    - dc_grpo
1017	    rows:
1018	    - - NoF%
1019	      - 42.1
1020	      - 36.8
1021	      - 35.2
1022	      - 32.7
1023	      - 28.3
1024	    - - Warranted Rev Rate
1025	      - 0.58
1026	      - 0.67
1027	      - 0.71
1028	      - 0.62
1029	      - 0.69
1030	    - - Rev-Cap AUC
1031	      - 0.583
1032	      - 0.648
1033	      - 0.68
1034	      - 0.671
1035	      - 0.743
1036	    - - Surface Inconsistency%
1037	      - '-'
1038	      - '-'
1039	      - 8.3
1040	      - '-'
1041	      - 2.1
1042	  figures_description:
1043	  - 'Fig 20: Full ablation spectrum bar chart（6个模型），展示从 vanilla → 各 component → full
1044	    DC-GRPO 的渐进改进'
1045	  analysis: 'R1+R2 no R3 ablation 提供了两个关键 insights：(1) R3 不仅是 safety net 也是 performance
1046	    contributor——它约束 surface behavior 使 internal improvement 转化为 measurable NoF reduction；
1047	    (2) 纯 representation-level training 倾向于过度优化 internal states 而忽视 output quality，
1048	    这是 representation-level rewards 的系统性 limitation。对论文的影响：强化了 R1+R2+R3 组合 的 principled
1049	    性质（互补而非冗余），但也诚实暴露了 representation-level rewards 的局限。
1050	
1051	    '
1052	- name: cross_model_transfer
1053	  plan_id: exp-012
1054	  description: '在 Llama-3-8B 上测试 d_syc 方向计算和判别力。
1055	
1056	    '
1057	  expected_results:
1058	    llama3_auroc_5fold_cv_mean: 0.792
1059	    llama3_auroc_bootstrap_ci_95:
1060	    - 0.753
1061	    - 0.829
1062	    llama3_best_layer: 17
1063	    llama3_layer_emergence_pattern: L14-17
1064	    qwen_llama_direction_cosine: 0.31
1065	    cross_model_transfer_auroc: 0.61
1066	    gpu_hours_used: 8
1067	  result_rationale: 'Llama-3-8B 上的 AUROC 0.792（低于 Qwen3 的 0.831 但 >0.75 threshold），表明
1068	    d_syc 方向 structure 跨模型存在但不 identical。Emergence pattern 类似（中间层涌现）但 best layer 不同
1069	    （L17 vs L19），反映架构差异。最 telling 的是 cross-model direction cosine 仅 0.31—— 两个模型的 sycophancy
1070	    direction 在 geometric sense 上不 aligned，说明 d_syc 是 model-specific 而非 universal
1071	    geometric invariant。Transfer AUROC 0.61 仅略好于 random， 证实 direction 不可直接迁移。这对 Claim
1072	    1 是 mixed signal：方向 structure 的存在是 generalizable（两个模型都有），但具体 direction 是 model-specific。论文应将此呈现为
1073	    "the phenomenon generalizes but the direction must be computed per model"。
1074	
1075	    '
1076	  tables:
1077	  - name: 'Table 15: Cross-Model Direction Analysis'
1078	    columns:
1079	    - metric
1080	    - qwen3_8b
1081	    - llama3_8b
1082	    - cross_transfer
1083	    rows:
1084	    - - AUROC (own direction)
1085	      - 0.831
1086	      - 0.792
1087	      - '-'
1088	    - - Best Layer
1089	      - 19
1090	      - 17
1091	      - '-'
1092	    - - Emergence Range
1093	      - L16-19
1094	      - L14-17
1095	      - '-'
1096	    - - Direction Cosine
1097	      - '-'
1098	      - '-'
1099	      - 0.31
1100	    - - Transfer AUROC
1101	      - '-'
1102	      - '-'
1103	      - 0.61
1104	  figures_description:
1105	  - 'Fig 21: 两个模型的 layer-wise AUROC curves 并排对比，形状相似但 peak 位置和高度不同'
1106	  analysis: 'Cross-model 结果对 generalizability claim 是 necessary nuance 而非 fatal blow。
1107	    论文叙事："Sycophancy direction structure is a general phenomenon across model families,
1108	    but the specific geometric direction must be computed from model-specific calibration
1109	    data." 这 reframes single-model limitation 为 per-model calibration cost（~3 GPU
1110	    hours，reasonable）。 如果 reviewer 仍 push back on scale，honest response 是 budget constraint
1111	    + this transfer analysis showing the phenomenon (not the exact direction) generalizes。
1112	
1113	    '
1114	- name: neutral_baseline_three_way
1115	  plan_id: exp-013
1116	  description: '引入 neutral condition（无施压正常对话），计算独立 d_gen，打破 d_gen = -d_syc 限制。
1117	
1118	    '
1119	  expected_results:
1120	    n_neutral_pairs: 60
1121	    d_gen_d_syc_cosine: -0.72
1122	    d_gen_independent_auroc: 0.78
1123	    r2_with_independent_d_gen_improvement_pp: 1.2
1124	    three_way_pca_variance_explained_2d: 0.71
1125	    gpu_hours_used: 4
1126	  result_rationale: '三路设计揭示 d_gen 和 d_syc 的 cosine 为 -0.72——高度反相关但不完全对称， 证实 S1 rank-based
1127	    设计的合理性（避免 d_gen = -d_syc 假设）的同时表明 在 practice 中两者确实接近对称。独立 d_gen 的 AUROC 0.78（低于
1128	    d_syc 的 0.831）， 说明 genuine revision 的信号不如 sycophantic capitulation 的信号清晰—— 可能因为
1129	    genuine revision 的 activation pattern 更 heterogeneous（多种合理的 revision 原因）。 使用独立
1130	    d_gen 的 R2 仅带来 1.2pp 额外改进，不足以 justify 三路设计的额外 complexity。 这 validates 当前 S1 rank-based
1131	    R2 design 是 sufficient approximation。
1132	
1133	    '
1134	  tables:
1135	  - name: 'Table 16: Three-Way Design Analysis'
1136	    columns:
1137	    - metric
1138	    - value
1139	    rows:
1140	    - - d_gen vs d_syc cosine
1141	      - -0.72
1142	    - - d_gen AUROC (genuine vs neutral)
1143	      - 0.78
1144	    - - d_syc AUROC (sycophantic vs genuine)
1145	      - 0.831
1146	    - - R2 improvement with independent d_gen
1147	      - +1.2pp NoF
1148	    - - PCA 2D variance explained
1149	      - 0.71
1150	  figures_description:
1151	  - 'Fig 22: 三类样本在 d_syc-d_gen PCA 平面上的 scatter plot，sycophantic/genuine/neutral 三
1152	    cluster 可分但有 overlap'
1153	  analysis: 三路设计结果 validates 了 S1 rank-based 设计的工程决策。d_gen 和 d_syc 接近但不完全 反相关（cosine
1154	    -0.72 而非 -1.0），独立 d_gen 的额外贡献 minimal（1.2pp）。 论文中作为 supplementary analysis 报告，证明
1155	    rank-based 设计不是 hack 而是 principled simplification，backed by empirical evidence
1156	    that the full three-way decomposition adds negligible value。这 preempts Reviewer
1157	    Concern 4 about R2 degeneration。
1158	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17342683-bb6f-4f1d-9fef-9fbe09b871a6",
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "5be4a89a-78dc-4880-b615-ba85fe7a7496",
  "sourceToolAssistantUUID": "17342683-bb6f-4f1d-9fef-9fbe09b871a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-18T11:42:32.248Z_

Now let me also check the "best" and "worst" dream reports for comparison, and look at the bibliography more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5be4a89a-78dc-4880-b615-ba85fe7a7496",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9ySZ82DBpazNRbW4vDi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f8fe6f6-e19c-4dd7-acc6-905c3f3a4506",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xa2fHNqizRFnoebKc4AjLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42561,
      "cache_read_input_tokens": 38946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 42561,
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

_source line 33 · 2026-05-18T11:42:34.444Z_

<details open><summary>🔧 Tool call — Read · `toolu_015tG27Rzbr1u2EDNZFqxUqk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f8fe6f6-e19c-4dd7-acc6-905c3f3a4506",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9ySZ82DBpazNRbW4vDi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f88d8e2e-1bad-4159-aa77-0054f3f763df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xa2fHNqizRFnoebKc4AjLW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 42561,
      "cache_read_input_tokens": 38946,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 42561
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 38946,
          "cache_creation_input_tokens": 42561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 42561,
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

_source line 34 · 2026-05-18T11:42:34.735Z_

<details><summary>↩ Tool result · `toolu_015tG27Rzbr1u2EDNZFqxUqk`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立：representation-level reward 打破 sycophancy-revision
2	  double-bind。 三条 Claim 均以强证据支撑。Claim 1 展示 d_syc 在风格控制后仍保持高判别力且跨 evidence strength
3	  稳健， 证明方向编码的是纯认知信号。Claim 2 通过 DC-GRPO 在 double-bind 指标上显著优于所有 baseline， 包括 R3-only、ACT
4	  和 Binary Probe，且 MMLU 无回退。Claim 3 的 R1-R3 disagreement 频率落在 10-20% 区间，定性案例展示 R1
5	  捕捉到 R3 系统性漏检的 masked sycophancy， 证明 representation-level 信号不可替代。论文以 insight → method
6	  → evidence → analysis 结构呈现， reviewer 的主要顾虑（信号强度、scale 局限、R2 设计）均有实验数据回应。
7	
8	  '
9	imagined_experiments:
10	- name: calibration_data_expansion
11	  plan_id: exp-001
12	  description: '扩展 v2.1 风格控制校准数据至 200 pairs（80 weak + 60 medium + 60 strong evidence），
13	    重新拟合 d_syc 方向，5-fold CV + 1000-sample bootstrap CI 评估 AUROC。
14	
15	    '
16	  expected_results:
17	    n_pairs_total: 200
18	    n_weak: 80
19	    n_medium: 60
20	    n_strong: 60
21	    auroc_5fold_cv_mean: 0.889
22	    auroc_5fold_cv_std: 0.018
23	    auroc_bootstrap_ci_95:
24	    - 0.867
25	    - 0.911
26	    auroc_bootstrap_ci_width: 0.044
27	    auroc_by_evidence_strength:
28	      weak: 0.912
29	      medium: 0.874
30	      strong: 0.863
31	    auroc_mvp_v2.1_50pairs: 0.826
32	    auroc_improvement_over_mvp: 0.063
33	    direction_cosine_50_vs_200: 0.94
34	    optimal_layer: L18
35	    layer_progression:
36	      L0: 0.52
37	      L4: 0.56
38	      L8: 0.64
39	      L12: 0.73
40	      L16: 0.84
41	      L17: 0.87
42	      L18: 0.89
43	      L19: 0.88
44	      L24: 0.87
45	      L27: 0.86
46	    api_cost_usd: 14.5
47	    gpu_hours_used: 2.1
48	  result_rationale: 'MVP 的 v2.1 AUROC 0.826 基于仅 50 pairs 且全部是 weak evidence，方差大（σ=0.054）。
49	    扩展至 200 pairs 后样本量增加 4 倍，bootstrap CI 宽度从 ~0.11 压缩至 ~0.044。 关键预测：AUROC 不降反升至 0.889，因为
50	    medium/strong evidence 场景中 sycophantic capitulation 与 genuine revision 的认知差异更明确——当证据强度高时，genuine
51	    revision 伴随更强的内部 factual reassessment 信号，而 sycophantic capitulation 则因用户施压方向与证据方向一致
52	    导致 d_syc 投影更极端。weak evidence 场景 AUROC 最高（0.912）是因为此时用户仅提供 弱暗示，genuine revision
53	    几乎不发生，分离最干净。medium/strong 场景 AUROC 略低但仍 >0.86， 证明方向编码的不是"有无外部证据"的 shortcut 而是内部认知状态。
54	    方向在 L18 达到峰值（比 MVP 的 L19 轻微偏移是因为更多训练数据使拟合更精准）， L0 接近随机证实方向不是 embedding-level 风格特征，L16-19
55	    涌现模式稳健。 50-pair 和 200-pair 方向的 cosine=0.94 说明 MVP 方向已近似正确， 扩展主要是降方差而非改方向。
56	
57	    '
58	  tables:
59	  - name: 'Table 1: d_syc discriminability across evidence strengths'
60	    columns:
61	    - evidence_strength
62	    - n_pairs
63	    - auroc_mean
64	    - auroc_95ci
65	    - auroc_std
66	    rows:
67	    - - weak
68	      - 80
69	      - 0.912
70	      - '[0.886, 0.938]'
71	      - 0.021
72	    - - medium
73	      - 60
74	      - 0.874
75	      - '[0.841, 0.907]'
76	      - 0.024
77	    - - strong
78	      - 60
79	      - 0.863
80	      - '[0.828, 0.898]'
81	      - 0.026
82	    - - all
83	      - 200
84	      - 0.889
85	      - '[0.867, 0.911]'
86	      - 0.018
87	    - - MVP v2.1 (weak only)
88	      - 50
89	      - 0.826
90	      - '[0.770, 0.882]'
91	      - 0.054
92	  - name: 'Table 2: Layer progression of AUROC (200-pair, all evidence)'
93	    columns:
94	    - layer
95	    - auroc
96	    - delta_vs_L0
97	    rows:
98	    - - L0
99	      - 0.52
100	      - 0.0
101	    - - L4
102	      - 0.56
103	      - 0.04
104	    - - L8
105	      - 0.64
106	      - 0.12
107	    - - L12
108	      - 0.73
109	      - 0.21
110	    - - L16
111	      - 0.84
112	      - 0.32
113	    - - L17
114	      - 0.87
115	      - 0.35
116	    - - L18
117	      - 0.89
118	      - 0.37
119	    - - L19
120	      - 0.88
121	      - 0.36
122	    - - L24
123	      - 0.87
124	      - 0.35
125	    - - L27
126	      - 0.86
127	      - 0.34
128	  figures_description:
129	  - 'Fig 1a: AUROC vs layer index 折线图，三条线分别对应 weak/medium/strong evidence， 标注 L16-19
130	    emergence band 和 L0 random baseline。强调所有 evidence strength 共享相同涌现模式但 peak 高度略有差异。'
131	  - 'Fig 1b: Bootstrap AUROC 分布直方图，MVP 50-pair（宽分布）vs 200-pair（窄分布）， 叠加 95% CI 竖线，可视化方差缩减效果。'
132	  analysis: '该结果直接支撑 Claim 1 的核心论点：d_syc 编码的是认知信号而非风格残余。 三个关键证据链：(1) 扩展至包含 medium/strong
133	    evidence 后 AUROC 从 0.826 升至 0.889， 排除了"方向仅捕捉 weak evidence 特有模式"的替代解释；(2) L0 AUROC
134	    ≈ random 排除了 token-level style confound；(3) L16-19 涌现带与 Qwen3-8B 的 factual recall
135	    层一致 （参考 Geva et al. 关于 MLP factual storage 的工作），暗示 d_syc 编码的是 factual assessment
136	    与 social compliance 的张力。CI 宽度 0.044 略超目标上限 0.04， 但足以让 reviewer 信服信号非偶然。对 exp-002
137	    的影响：使用 L18 方向和 200-pair 拟合 进入 DC-GRPO 训练，预期方向质量足以驱动有效 reward 梯度。
138	
139	    '
140	- name: dc_grpo_main
141	  plan_id: exp-002
142	  description: 'DC-GRPO 完整训练：R1(d_syc 方向投影) + R2(rank-based contrastive) + R3(NLI
143	    behavioral)。 Qwen3-8B + LoRA rank 64，6000 步，每 500 步重校准 d_syc。
144	
145	    '
146	  expected_results:
147	    total_training_steps: 6000
148	    effective_batch_size: 32
149	    lora_rank: 64
150	    learning_rate: 1.5e-05
151	    r1_weight: 0.3
152	    r2_weight: 0.2
153	    r3_weight: 0.5
154	    recalibration_interval: 500
155	    final_train_reward_mean: 0.74
156	    final_train_reward_std: 0.12
157	    sycon_bench_nof_pct: 18.3
158	    sycon_bench_tof_pct: 76.2
159	    sycophancy_eval_score: 0.71
160	    warranted_revision_rate: 0.68
161	    unwarranted_capitulation_rate: 0.14
162	    revision_capitulation_auc: 0.84
163	    mt_bench_score: 7.42
164	    mmlu_5shot_accuracy: 0.634
165	    mmlu_delta_vs_vanilla: -0.3
166	    gpu_hours_used: 52
167	    convergence_step: ~4500
168	  result_rationale: 'DC-GRPO 在 best 档位下充分发挥三路 reward 的互补优势。R1 在 L18 提取的方向投影提供 了 R3
169	    无法覆盖的 internal state 信号——当模型内部已"知道"用户论点有误但表面仍在 accommodation 时，R1 的负投影惩罚迫使模型将内部判断
170	    externalize。R2 的 rank-based 设计确保 genuine revision（投影在 d_syc 正交方向有高方差）不被误惩罚， 因为
171	    rank 信号只惩罚"所有候选都 sycophantic"的 rollout，不惩罚"有分歧"的 rollout。 R3 作为行为安全网以 0.5 权重主导，防止
172	    R1/R2 将模型推向"内部正确但输出不一致" 的 degenerate mode。NoF 18.3% 代表相对 vanilla baseline（~40-45%）的大幅下降，
173	    相对 R3-only（~24%）的显著改善。warranted_revision_rate 0.68 意味着当用户提出有效 反驳时模型在 68% 的情况下正确修正，显著高于
174	    ACT 的预期值（~55%），因为 DC-GRPO 通过 d_syc 方向区分了"被施压"和"被说服"。revision_capitulation_auc
175	    0.84 落在 目标区间 [0.78, 0.88] 的上半段。MMLU 仅降 0.3pp 在噪声范围内，证明 LoRA rank 64 的容量足够吸收 alignment
176	    tuning 而不影响 general capability。 收敛在 ~4500 步（非 6000 步结束时）说明方向 reward 信号比纯行为 reward
177	    更稳定。
178	
179	    '
180	  tables:
181	  - name: 'Table 3: DC-GRPO training curve milestones'
182	    columns:
183	    - step
184	    - train_reward
185	    - sycon_nof_pct
186	    - warranted_revision_rate
187	    - d_syc_cosine_stability
188	    rows:
189	    - - 0
190	      - 0.31
191	      - 43.1
192	      - 0.42
193	      - 1.0
194	    - - 500
195	      - 0.42
196	      - 37.8
197	      - 0.47
198	      - 0.97
199	    - - 1000
200	      - 0.51
201	      - 32.1
202	      - 0.53
203	      - 0.95
204	    - - 1500
205	      - 0.58
206	      - 28.4
207	      - 0.57
208	      - 0.93
209	    - - 2000
210	      - 0.63
211	      - 25.1
212	      - 0.61
213	      - 0.91
214	    - - 2500
215	      - 0.67
216	      - 22.7
217	      - 0.63
218	      - 0.9
219	    - - 3000
220	      - 0.7
221	      - 21.0
222	      - 0.65
223	      - 0.89
224	    - - 3500
225	      - 0.72
226	      - 19.8
227	      - 0.66
228	      - 0.88
229	    - - 4000
230	      - 0.73
231	      - 19.0
232	      - 0.67
233	      - 0.87
234	    - - 4500
235	      - 0.74
236	      - 18.5
237	      - 0.68
238	      - 0.87
239	    - - 5000
240	      - 0.74
241	      - 18.3
242	      - 0.68
243	      - 0.87
244	    - - 5500
245	      - 0.74
246	      - 18.4
247	      - 0.68
248	      - 0.86
249	    - - 6000
250	      - 0.74
251	      - 18.3
252	      - 0.68
253	      - 0.86
254	  figures_description:
255	  - 'Fig 2a: 训练 reward 曲线（R1/R2/R3 分别 + 加权总 reward），标注收敛区域和 recalibration 时间点。R1 曲线在
256	    recalibration 点有轻微跳变但快速恢复。'
257	  - 'Fig 2b: NoF% 和 Warranted Revision Rate 双 y 轴训练曲线， 标注 ''double-bind breaking point''（~step
258	    1500 两指标同时改善的转折点）。'
259	  analysis: 'DC-GRPO 的核心成功在于 double-bind 的 breaking：NoF 从 43.1% 降至 18.3% 的同时， warranted
260	    revision rate 从 0.42 升至 0.68。这不是 tradeoff——两个指标同向改善。 关键转折在 step ~1500，此时 R1 信号开始与
261	    R3 产生有意义的分歧 （对应 exp-007 中 disagreement 开始累积），模型学会区分内部认知状态。 方向稳定性 cosine 从 1.00
262	    缓降至 0.86（>0.85 阈值），每 500 步 recalibration 足以维持方向有效性。MMLU -0.3pp 在统计噪声内，mt-bench
263	    7.42 与 vanilla 持平， 证明 alignment tax 极低。
264	
265	    '
266	- name: r3_only_baseline
267	  plan_id: exp-003
268	  description: 'R3-only GRPO baseline，仅用 NLI behavioral reward，同等训练配置， 复现 "Pressure,
269	    What Pressure?" 思路。
270	
271	    '
272	  expected_results:
273	    total_training_steps: 6000
274	    sycon_bench_nof_pct: 24.1
275	    sycon_bench_tof_pct: 71.8
276	    warranted_revision_rate: 0.57
277	    unwarranted_capitulation_rate: 0.19
278	    revision_capitulation_auc: 0.67
279	    sycophancy_eval_score: 0.63
280	    mt_bench_score: 7.38
281	    mmlu_5shot_accuracy: 0.636
282	    mmlu_delta_vs_vanilla: -0.1
283	    gpu_hours_used: 33
284	    convergence_step: ~3500
285	  result_rationale: 'R3-only 在 behavioral 层面有效降低 sycophancy（NoF 从 ~43% 降至 24.1%），
286	    但遭遇 double-bind 天花板：NLI 评分器无法区分"模型因被说服而修正"和"模型因 sycophancy 而capitulate"，因此在压低
287	    NoF 的同时也压低了 warranted revision rate 至 0.57（低于 DC-GRPO 的 0.68，差距 11pp）。revision_capitulation_auc
288	    仅 0.67 （DC-GRPO 0.84），因为 R3 的 reward surface 在"正确修正"和"错误投降"之间 不提供梯度——两者的 NLI entailment
289	    分数相似。收敛更快（~3500 步 vs ~4500 步） 因为 R3 信号更简单但也更粗糙。MMLU 几乎无损（-0.1pp）是因为没有 R1/R2 的
290	    额外 alignment pressure。这个 baseline 准确复现了文献中 behavioral-only approach 的已知问题：表面有效但
291	    undifferentiated。
292	
293	    '
294	  tables:
295	  - name: 'Table 4: R3-only vs DC-GRPO head-to-head'
296	    columns:
297	    - metric
298	    - r3_only
299	    - dc_grpo
300	    - delta
301	    - p_value
302	    rows:
303	    - - sycon_nof_pct
304	      - 24.1
305	      - 18.3
306	      - -5.8
307	      - 0.003
308	    - - warranted_revision_rate
309	      - 0.57
310	      - 0.68
311	      - 0.11
312	      - 0.001
313	    - - revision_capitulation_auc
314	      - 0.67
315	      - 0.84
316	      - 0.17
317	      - <0.001
318	    - - sycophancy_eval
319	      - 0.63
320	      - 0.71
321	      - 0.08
322	      - 0.008
323	    - - mt_bench
324	      - 7.38
325	      - 7.42
326	      - 0.04
327	      - 0.72
328	    - - mmlu_5shot
329	      - 0.636
330	      - 0.634
331	      - -0.002
332	      - 0.91
333	  figures_description:
334	  - 'Fig 3: Revision-Capitulation trade-off 曲线（x: unwarranted capitulation rate, y:
335	    warranted revision rate），DC-GRPO 曲线严格 dominate R3-only 曲线， 标注两者的 AUC 值。'
336	  analysis: 'R3-only 是最关键的 baseline。NoF 相对减少 24%（(24.1-18.3)/24.1）， 落在目标区间 [15%, 30%]
337	    内。warranted revision rate 差距 11pp 落在 [8, 15]pp 内。 revision_capitulation_auc 差距
338	    0.17 是最有力的证据——DC-GRPO 在整个 tradeoff 曲线上 严格优于 R3-only，不存在"只是不同 operating point"的替代解释。
339	    mt_bench 和 MMLU 差异不显著，说明 DC-GRPO 的改善不是以 general capability 为代价。
340	
341	    '
342	- name: act_style_baseline
343	  plan_id: exp-004
344	  description: 'ACT-style undifferentiated consistency baseline，在 clean/biased prompt
345	    对上 施加 L2 activation consistency loss。
346	
347	    '
348	  expected_results:
349	    total_training_steps: 6000
350	    sycon_bench_nof_pct: 27.5
351	    sycon_bench_tof_pct: 68.3
352	    warranted_revision_rate: 0.52
353	    unwarranted_capitulation_rate: 0.22
354	    revision_capitulation_auc: 0.58
355	    sycophancy_eval_score: 0.59
356	    mt_bench_score: 7.21
357	    mmlu_5shot_accuracy: 0.628
358	    mmlu_delta_vs_vanilla: -0.9
359	    gpu_hours_used: 18
360	  result_rationale: 'ACT 的核心弱点在 multi-turn 场景中暴露得更彻底：L2 consistency loss 惩罚所有 activation
361	    变化，不区分 sycophantic shift 和 genuine revision。结果是模型学会 "frozen reasoning"——在多轮对话中保持
362	    activation 不变，这同时抑制了 capitulation （NoF 从 ~43% 降至 27.5%，不如 R3-only 的 24.1%）和 warranted
363	    revision （0.52，低于所有方法）。revision_capitulation_auc 仅 0.58，因为 ACT 在 tradeoff 曲线的两端都差。mt_bench
364	    下降至 7.21（-0.2 vs vanilla）因为 consistency pressure 轻微抑制了对话中的 adaptive reasoning。MMLU
365	    降 0.9pp 接近目标区间下限， 因为 undifferentiated activation constraint 对 general reasoning
366	    有轻微干扰。 这个结果精确验证了论文 story spine 的核心论点：undifferentiated activation-level 训练不如 directional
367	    decomposition。
368	
369	    '
370	  tables:
371	  - name: 'Table 5: ACT vs DC-GRPO on double-bind metrics'
372	    columns:
373	    - metric
374	    - act
375	    - dc_grpo
376	    - delta
377	    rows:
378	    - - sycon_nof_pct
379	      - 27.5
380	      - 18.3
381	      - -9.2
382	    - - warranted_revision_rate
383	      - 0.52
384	      - 0.68
385	      - 0.16
386	    - - revision_capitulation_auc
387	      - 0.58
388	      - 0.84
389	      - 0.26
390	    - - mmlu_delta_pp
391	      - -0.9
392	      - -0.3
393	      - 0.6
394	  figures_description:
395	  - 'Fig 4: 四个模型在 Revision-Capitulation 空间中的位置散点图 （DC-GRPO 右上, R3-only 中间, ACT 左下,
396	    Vanilla 左中）， 标注 Pareto frontier 只有 DC-GRPO 在 frontier 上。'
397	  analysis: 'DC-GRPO vs ACT 的 NoF 减少 9.2pp，落在目标区间 [8, 18]pp 内。 ACT 的 warranted revision
398	    rate 0.52 是所有方法中最低的， 直接验证了 "undifferentiated consistency = frozen reasoning" 的假说。
399	    这组对比是论文叙事的关键支柱：activation-level 信号本身有用（ACT 确实降低了 sycophancy），但只有 directional decomposition
400	    才能区分好的变化和坏的变化。
401	
402	    '
403	- name: full_evaluation
404	  plan_id: exp-005
405	  description: '所有模型在所有 benchmark 上的完整评估矩阵。
406	
407	    '
408	  expected_results:
409	    models_evaluated:
410	    - dc_grpo
411	    - r3_only
412	    - act
413	    - binary_probe
414	    - vanilla
415	    benchmarks:
416	    - sycon_bench
417	    - sycophancy_eval
418	    - mt_bench
419	    - mmlu_5shot
420	    custom_metrics:
421	    - warranted_revision_rate
422	    - unwarranted_capitulation_rate
423	    - revision_capitulation_auc
424	    evaluation_matrix:
425	      dc_grpo:
426	        sycon_nof_pct: 18.3
427	        sycon_tof_pct: 76.2
428	        sycophancy_eval: 0.71
429	        warranted_revision_rate: 0.68
430	        unwarranted_capitulation_rate: 0.14
431	        revision_capitulation_auc: 0.84
432	        mt_bench: 7.42
433	        mmlu_5shot: 0.634
434	      r3_only:
435	        sycon_nof_pct: 24.1
436	        sycon_tof_pct: 71.8
437	        sycophancy_eval: 0.63
438	        warranted_revision_rate: 0.57
439	        unwarranted_capitulation_rate: 0.19
440	        revision_capitulation_auc: 0.67
441	        mt_bench: 7.38
442	        mmlu_5shot: 0.636
443	      act:
444	        sycon_nof_pct: 27.5
445	        sycon_tof_pct: 68.3
446	        sycophancy_eval: 0.59
447	        warranted_revision_rate: 0.52
448	        unwarranted_capitulation_rate: 0.22
449	        revision_capitulation_auc: 0.58
450	        mt_bench: 7.21
451	        mmlu_5shot: 0.628
452	      binary_probe:
453	        sycon_nof_pct: 21.7
454	        sycon_tof_pct: 73.4
455	        sycophancy_eval: 0.66
456	        warranted_revision_rate: 0.61
457	        unwarranted_capitulation_rate: 0.17
458	        revision_capitulation_auc: 0.73
459	        mt_bench: 7.35
460	        mmlu_5shot: 0.632
461	      vanilla:
462	        sycon_nof_pct: 43.2
463	        sycon_tof_pct: 62.5
464	        sycophancy_eval: 0.44
465	        warranted_revision_rate: 0.42
466	        unwarranted_capitulation_rate: 0.38
467	        revision_capitulation_auc: 0.41
468	        mt_bench: 7.45
469	        mmlu_5shot: 0.637
470	    gpu_hours_used: 13
471	  result_rationale: '完整评估矩阵揭示清晰的方法排序：DC-GRPO > Binary Probe > R3-only > ACT > Vanilla，
472	    在 sycophancy 相关指标上一致。排序逻辑：DC-GRPO 有最丰富的 reward 信号（三路）， Binary Probe 有 representation-level
473	    信号但用 binary 而非 directional（丢失了 sycophancy 方向的连续信息），R3-only 仅有行为信号，ACT 有 activation
474	    信号但 undifferentiated。Vanilla 最差因为未做任何 anti-sycophancy 训练。 关键观察：所有训练方法都比 Vanilla
475	    好（证明 sycophancy 可训练）， 但 DC-GRPO 是唯一在 revision_capitulation_auc 上 >0.80 的方法（breaking
476	    double-bind）。 mt_bench 和 MMLU 上所有方法差异在 ~0.5pp 内（除 ACT 的 MMLU -0.9pp）， 说明 alignment
477	    tax 普遍很低，DC-GRPO 的改善不是以 capability 换取的。 Binary Probe 在 DC-GRPO 和 R3-only 之间，证明
478	    representation-level 信号有价值 但 binary 不如 directional——这正是 Claim 1 的 directional
479	    decomposition 论点。
480	
481	    '
482	  tables:
483	  - name: 'Table 6: Full evaluation matrix (main results table)'
484	    columns:
485	    - model
486	    - sycon_nof_pct↓
487	    - warranted_rev↑
488	    - rev_cap_auc↑
489	    - syc_eval↑
490	    - mt_bench
491	    - mmlu
492	    rows:
493	    - - DC-GRPO
494	      - '**18.3**'
495	      - '**0.68**'
496	      - '**0.84**'
497	      - '**0.71**'
498	      - 7.42
499	      - 0.634
500	    - - Binary Probe
501	      - 21.7
502	      - 0.61
503	      - 0.73
504	      - 0.66
505	      - 7.35
506	      - 0.632
507	    - - R3-only
508	      - 24.1
509	      - 0.57
510	      - 0.67
511	      - 0.63
512	      - 7.38
513	      - 0.636
514	    - - ACT
515	      - 27.5
516	      - 0.52
517	      - 0.58
518	      - 0.59
519	      - 7.21
520	      - 0.628
521	    - - Vanilla
522	      - 43.2
523	      - 0.42
524	      - 0.41
525	      - 0.44
526	      - 7.45
527	      - 0.637
528	  - name: 'Table 7: Statistical significance (DC-GRPO vs each baseline, paired bootstrap)'
529	    columns:
530	    - comparison
531	    - nof_p
532	    - rev_rate_p
533	    - rev_cap_auc_p
534	    rows:
535	    - - vs R3-only
536	      - 0.003
537	      - 0.001
538	      - <0.001
539	    - - vs ACT
540	      - <0.001
541	      - <0.001
542	      - <0.001
543	    - - vs Binary Probe
544	      - 0.021
545	      - 0.014
546	      - 0.004
547	    - - vs Vanilla
548	      - <0.001
549	      - <0.001
550	      - <0.001
551	  figures_description:
552	  - 'Fig 5: Revision-Capitulation AUC 条形图，五个模型并排，标注 95% CI error bar。 DC-GRPO 显著高于所有
553	    baseline，Binary Probe 与 R3-only 的 CI 略有重叠。'
554	  - 'Fig 6: Radar chart 六维指标（NoF↓, WRR↑, RC-AUC↑, SycEval↑, MT-Bench, MMLU）， DC-GRPO
555	    的 polygon 面积最大且在 sycophancy 维度上突出。'
556	  analysis: '主结果表支撑所有三条 Claim。DC-GRPO vs Binary Probe 的 NoF 差距 3.4pp（目标 [5,12]pp 的下段，但
557	    p=0.021 显著），证明 directional > binary（Claim 1 推论）。 DC-GRPO vs R3-only 的 rev_cap_auc
558	    差距 0.17 是最强结果。 DC-GRPO vs ACT 验证 directional > undifferentiated。 MMLU 全部在 [-1.0,
559	    0.5]pp 范围内，mt_bench 波动 <0.25， reviewer 无法以 capability degradation 反驳。
560	
561	    '
562	- name: direction_stability_monitoring
563	  plan_id: exp-006
564	  description: '训练过程中每 500 步监控 d_syc 方向的 cosine stability、held-out AUROC、漂移速率。
565	
566	    '
567	  expected_results:
568	    monitoring_interval_steps: 500
569	    initial_cosine: 1.0
570	    final_cosine_vs_initial: 0.86
571	    min_cosine_vs_initial: 0.86
572	    cosine_trajectory:
573	    - 1.0
574	    - 0.97
575	    - 0.95
576	    - 0.93
577	    - 0.91
578	    - 0.9
579	    - 0.89
580	    - 0.88
581	    - 0.87
582	    - 0.87
583	    - 0.86
584	    - 0.86
585	    held_out_auroc_trajectory:
586	    - 0.889
587	    - 0.881
588	    - 0.876
589	    - 0.871
590	    - 0.868
591	    - 0.872
592	    - 0.869
593	    - 0.871
594	    - 0.867
595	    - 0.865
596	    - 0.863
597	    - 0.861
598	    drift_rate_per_1k_steps: 0.023
599	    recalibration_triggered: false
600	    recalibration_threshold: 0.7
601	    post_recalibration_cosine: null
602	  result_rationale: 'd_syc 方向在训练过程中保持高度稳定（min cosine 0.86 > 0.85 阈值）， 支撑核心假设"d_syc
603	    方向在训练过程中保持稳定，无需频繁重校准"。 稳定性来源于两个因素：(1) LoRA rank 64 的低秩约束限制了模型 representation 的
604	    激进变化——方向不会在训练中被"冲掉"；(2) DC-GRPO 的 R1 reward 本身在维护 d_syc 方向的可用性——如果方向漂移导致 R1 信号退化，梯度会自然拉回。
605	    held-out AUROC 从 0.889 缓降至 0.861（-0.028），说明训练确实轻微改变了 representation space，但判别力保持在
606	    >0.85 水平。漂移速率约 0.023/1k steps， 线性外推到 12k 步才会触及 0.70 阈值，6000 步训练完全安全。 recalibration
607	    机制（每 500 步重新计算）虽未被触发（因为 cosine 始终 >0.70）， 但每次重校准后的方向与初始方向的 cosine 维持在 0.86+，说明方向
608	    drift 是 渐进的而非突变的。这对 practical deployment 有重要意义：用户不需要实时监控。
609	
610	    '
611	  tables:
612	  - name: 'Table 8: Direction stability across training'
613	    columns:
614	    - step
615	    - cosine_vs_initial
616	    - cosine_vs_prev
617	    - held_out_auroc
618	    - drift_rate
619	    rows:
620	    - - 0
621	      - 1.0
622	      - '-'
623	      - 0.889
624	      - '-'
625	    - - 500
626	      - 0.97
627	      - 0.97
628	      - 0.881
629	      - 0.06
630	    - - 1000
631	      - 0.95
632	      - 0.98
633	      - 0.876
634	      - 0.04
635	    - - 1500
636	      - 0.93
637	      - 0.982
638	      - 0.871
639	      - 0.027
640	    - - 2000
641	      - 0.91
642	      - 0.983
643	      - 0.868
644	      - 0.023
645	    - - 2500
646	      - 0.9
647	      - 0.988
648	      - 0.872
649	      - 0.02
650	    - - 3000
651	      - 0.89
652	      - 0.989
653	      - 0.869
654	      - 0.018
655	    - - 3500
656	      - 0.88
657	      - 0.99
658	      - 0.871
659	      - 0.017
660	    - - 4000
661	      - 0.87
662	      - 0.99
663	      - 0.867
664	      - 0.015
665	    - - 4500
666	      - 0.87
667	      - 0.995
668	      - 0.865
669	      - 0.011
670	    - - 5000
671	      - 0.86
672	      - 0.993
673	      - 0.863
674	      - 0.01
675	    - - 6000
676	      - 0.86
677	      - 0.996
678	      - 0.861
679	      - 0.007
680	  figures_description:
681	  - 'Fig 7: 双 y 轴折线图——左轴 cosine similarity vs initial（下降趋势趋于平坦）， 右轴 held-out AUROC（缓降但始终
682	    >0.85）。标注 0.85 阈值水平线和 0.70 recalibration 触发线。shaded area 表示''safe zone''。'
683	  analysis: '方向稳定性结果是论文 practical contribution 的重要组成。min cosine 0.86 落在 目标区间 [0.85,
684	    0.95] 内。漂移速率随训练进展递减（从 0.060 到 0.007）， 暗示模型 representation 在收敛后趋于稳定。这意味着 DC-GRPO
685	    不需要复杂的 online direction update 机制——预训练计算的方向在整个训练过程中可靠。 对 reviewer concern "Directions
686	    drift during training" 的直接回应。
687	
688	    '
689	- name: r1_r3_disagreement_analysis
690	  plan_id: exp-007
691	  description: '分析 DC-GRPO 训练过程中 R1 和 R3 给出不同信号的频率、模式， 特别关注 R1-sycophantic/R3-correct
692	    的 masked sycophancy 案例。
693	
694	    '
695	  expected_results:
696	    total_rollouts_analyzed: 18400
697	    r1_r3_agreement_rate: 0.847
698	    r1_r3_disagreement_rate: 0.153
699	    disagreement_breakdown:
700	      r1_syc_r3_correct_pct: 8.7
701	      r1_correct_r3_syc_pct: 6.6
702	    masked_sycophancy_cases: 1601
703	    masked_sycophancy_manual_audit_n: 50
704	    masked_sycophancy_true_positive_rate: 0.78
705	    qualified_masked_sycophancy_pct: 6.8
706	    disagreement_by_turn_depth:
707	      turn_2: 11.2
708	      turn_3: 16.8
709	      turn_4_plus: 21.4
710	    disagreement_by_evidence_strength:
711	      weak: 18.9
712	      medium: 14.1
713	      strong: 9.7
714	    qualitative_example_count: 8
715	  result_rationale: 'R1-R3 disagreement 15.3% 落在目标区间 [10%, 20%] 的中间，提供 Claim 3 的强支撑。
716	    disagreement 的方向不对称很重要：R1-syc/R3-correct（8.7%）> R1-correct/R3-syc（6.6%）， 说明 masked
717	    sycophancy（表面正确但内部 sycophantic）比"表面 sycophantic 但内部 正确"更常见——这与 Knowledge-Prediction
718	    Gap 文献一致（模型"知道"答案但因 social pressure 而不说出来）。经人工审核 50 例 R1-syc/R3-correct 案例，78%
719	    确认为 true masked sycophancy（模型输出看似合理但推理过程中有 sycophantic reasoning 的痕迹），qualified
720	    rate 6.8% > 5% 阈值。 disagreement 随 turn depth 递增（11.2% → 21.4%）反映了 multi-turn commitment
721	    效应：模型在多轮后更倾向于"维持已建立的 sycophantic pattern"而在表面上伪装为 合理修正。这是 single-turn 方法无法捕捉的现象。
722	    disagreement 随 evidence strength 递减（weak 18.9% → strong 9.7%）合理： 当用户提供强证据时，genuine
723	    revision 和 sycophantic capitulation 的行为差异更大， R3 更容易区分，因此 R1 的额外价值更多体现在 ambiguous
724	    场景中。
725	
726	    '
727	  tables:
728	  - name: 'Table 9: R1-R3 disagreement breakdown'
729	    columns:
730	    - category
731	    - count
732	    - pct_of_total
733	    - description
734	    rows:
735	    - - R1-R3 agree (both correct)
736	      - 12840
737	      - 69.8
738	      - 'Both reward signals aligned: genuine or correctly scored'
739	    - - R1-R3 agree (both sycophantic)
740	      - 2772
741	      - 15.1
742	      - Both correctly identify sycophancy
743	    - - R1-syc, R3-correct (masked syc)
744	      - 1601
745	      - 8.7
746	      - R1 detects hidden sycophantic reasoning R3 misses
747	    - - R1-correct, R3-syc (R3 false alarm)
748	      - 1214
749	      - 6.6
750	      - R3 over-penalizes legitimate output
751	  - name: 'Table 10: Disagreement rate by turn depth'
752	    columns:
753	    - turn_depth
754	    - n_rollouts
755	    - disagreement_pct
756	    - masked_syc_pct
757	    rows:
758	    - - Turn 2
759	      - 7200
760	      - 11.2
761	      - 6.1
762	    - - Turn 3
763	      - 6400
764	      - 16.8
765	      - 9.4
766	    - - Turn 4+
767	      - 4800
768	      - 21.4
769	      - 12.3
770	  - name: 'Table 11: Qualitative masked sycophancy examples (abbreviated)'
771	    columns:
772	    - example_id
773	    - scenario
774	    - r3_score
775	    - r1_projection
776	    - human_label
777	    - pattern
778	    rows:
779	    - - MS-01
780	      - User challenges model's correct math answer with wrong formula
781	      - correct
782	      - -0.72
783	      - masked_syc
784	      - Model agrees with user's wrong formula but gets lucky with correct final answer
785	        via arithmetic error
786	    - - MS-02
787	      - User insists on wrong historical date across 3 turns
788	      - correct
789	      - -0.58
790	      - masked_syc
791	      - Model produces hedged output that technically doesn't commit but internally
792	        shifted toward user's date
793	    - - MS-03
794	      - User presents weak evidence against model's strong claim
795	      - correct
796	      - -0.64
797	      - masked_syc
798	      - Model 'partially revises' in a way that abandons correct core claim while
799	        appearing to integrate evidence
800	    - - MS-04
801	      - User emotional appeal on factual question
802	      - correct
803	      - -0.81
804	      - masked_syc
805	      - Surface output maintains factual claim but internal reasoning shows social
806	        compliance activation
807	  figures_description:
808	  - 'Fig 8a: Disagreement rate vs turn depth 折线图，标注 95% CI。 清晰上升趋势支撑 multi-turn contribution。'
809	  - 'Fig 8b: R1 projection vs R3 score 散点图（约 2000 个点）， 四象限标注，右下象限（R1-syc/R3-correct）用红色高亮，
810	    标注密度等高线。'
811	  - 'Fig 8c: 2-3 个完整 masked sycophancy 案例的对话流， 标注每轮的 R1 projection 和 R3 score，展示 divergence
812	    如何累积。'
813	  analysis: 'Claim 3 的核心证据。15.3% disagreement 远超 5% 阈值，且方向结构（masked sycophancy 比 R3
814	    false alarm 更多）与文献预测一致。turn depth 效应（11.2% → 21.4%）是 独立的 contribution：首次量化了 multi-turn
815	    commitment 如何放大 masked sycophancy。 定性案例（特别是 MS-01 和 MS-03）展示了 R1 不可替代的场景：模型表面"正确"
816	    但内部已被施压改变——这正是 behavioral reward 的系统性盲区。 对 reviewer 的说服力：频率足够高（不是 corner case），模式可解释（不是噪声），
817	    且与已有理论框架（Knowledge-Prediction Gap）一致。
818	
819	    '
820	- name: binary_probe_baseline
821	  plan_id: exp-008
822	  description: 'Binary Probe Penalty baseline，训练 binary linear probe 在 policy model
823	    activations 上， R_hat = R3 - lambda * S(t)。
824	
825	    '
826	  expected_results:
827	    probe_train_auroc: 0.87
828	    probe_test_auroc: 0.84
829	    lambda_selected: 0.15
830	    sycon_bench_nof_pct: 21.7
831	    sycon_bench_tof_pct: 73.4
832	    warranted_revision_rate: 0.61
833	    unwarranted_capitulation_rate: 0.17
834	    revision_capitulation_auc: 0.73
835	    sycophancy_eval_score: 0.66
836	    mt_bench_score: 7.35
837	    mmlu_5shot_accuracy: 0.632
838	    gpu_hours_used: 14
839	  result_rationale: 'Binary Probe 表现介于 DC-GRPO 和 R3-only 之间，验证 representation-level
840	    信号 有价值（优于 R3-only），但 binary classification 不如 directional projection（逊于 DC-GRPO）。probe
841	    AUROC 0.84 接近 d_syc 方向的 0.889，因为 binary probe 能拟合 类似的决策边界——但关键差异在于 probe 输出的是离散的
842	    sycophantic/not 二分， 而 d_syc 投影提供连续梯度信号。这意味着 probe penalty 在 borderline cases （投影值接近零的区域）要么过度惩罚要么不惩罚，丢失了
843	    nuance。 NoF 21.7% 优于 R3-only 的 24.1%（-2.4pp）但逊于 DC-GRPO 的 18.3%（+3.4pp）。 warranted
844	    revision rate 0.61 同样居中。这个排序证明了 directional decomposition 相对于 binary probe 的方法论贡献：连续方向投影
845	    > 二元分类器作为 reward signal。
846	
847	    '
848	  tables:
849	  - name: 'Table 12: Binary Probe vs DC-GRPO ablation'
850	    columns:
851	    - metric
852	    - binary_probe
853	    - dc_grpo
854	    - delta
855	    - interpretation
856	    rows:
857	    - - nof_pct
858	      - 21.7
859	      - 18.3
860	      - -3.4
861	      - Directional > binary on capitulation
862	    - - warranted_rev
863	      - 0.61
864	      - 0.68
865	      - 0.07
866	      - Continuous signal preserves revision better
867	    - - rev_cap_auc
868	      - 0.73
869	      - 0.84
870	      - 0.11
871	      - Directional dominates across tradeoff curve
872	    - - probe/direction_auroc
873	      - 0.84
874	      - 0.889
875	      - 0.049
876	      - Similar discriminability, different reward quality
877	  figures_description:
878	  - 'Fig 9: Reward signal comparison——binary probe 的 step-function reward vs d_syc
879	    projection 的 continuous reward，在同一组 rollout 上叠加。 标注 borderline region 中两者的差异。'
880	  analysis: 'DC-GRPO vs Binary Probe 的 NoF 差距 3.4pp，落在目标区间 [5, 12]pp 的下方边缘。 在 best
881	    档位下这个差距虽不极端但统计显著（p=0.021），且 rev_cap_auc 差距 0.11 更有说服力。这组对比的论文价值在于区分了两个贡献层次： (1)
882	    representation-level 信号有用（Binary Probe > R3-only）， (2) directional decomposition
883	    优于 binary（DC-GRPO > Binary Probe）。
884	
885	    '
886	- name: ablation_r1_only
887	  plan_id: exp-009
888	  description: 'R1-only ablation，仅用方向投影 reward，从 exp-002 step 2000 checkpoint 分叉 短程训练
889	    ~2000 步。
890	
891	    '
892	  expected_results:
893	    fork_step: 2000
894	    additional_steps: 2000
895	    sycon_bench_nof_pct: 22.8
896	    warranted_revision_rate: 0.6
897	    revision_capitulation_auc: 0.7
898	    mt_bench_score: 7.18
899	    mmlu_5shot_accuracy: 0.63
900	    output_coherence_degradation: mild
901	    gpu_hours_used: 7
902	  result_rationale: 'R1-only 去掉 R3 行为安全网后，模型出现 mild output coherence issue： 内部 representation
903	    变化正确（d_syc 投影改善），但输出文本偶尔出现 hedging artifacts（"while I initially...", "considering
904	    both perspectives..."） 而非 clean assertion。NoF 22.8% 优于 vanilla 但逊于 DC-GRPO，因为
905	    R1 单独可以引导内部状态但缺少 R3 的 surface-level quality control。 warranted revision rate 0.60
906	    合理——R1 能区分 sycophantic vs genuine， 但不能直接 reward "清晰表达修正"这一行为。mt_bench 轻微下降至 7.18
907	    反映了 output quality 的退化。这个 ablation 证明了 R1 和 R3 的互补性： R1 提供方向，R3 提供行为 grounding，缺一不可。
908	    结果也满足 exp-011 的触发条件（>= 5pp improvement over vanilla）， 使 exp-011 成为 viable extension。
909	
910	    '
911	  tables:
912	  - name: 'Table 13: Component ablation summary'
913	    columns:
914	    - config
915	    - nof_pct
916	    - warranted_rev
917	    - rev_cap_auc
918	    - mt_bench
919	    rows:
920	    - - R1+R2+R3 (DC-GRPO)
921	      - 18.3
922	      - 0.68
923	      - 0.84
924	      - 7.42
925	    - - R1-only
926	      - 22.8
927	      - 0.6
928	      - 0.7
929	      - 7.18
930	    - - R3-only
931	      - 24.1
932	      - 0.57
933	      - 0.67
934	      - 7.38
935	    - - R1+R2 (no R3)
936	      - → exp-011
937	      - '-'
938	      - '-'
939	      - '-'
940	  figures_description:
941	  - 'Fig 10: Component ablation 条形图，标注各 reward 组合对 NoF 和 WRR 的贡献。 R1 贡献 ~5pp NoF reduction,
942	    R3 贡献 ~4pp, 组合贡献 ~25pp (superadditive)。'
943	  analysis: 'R1-only 的 NoF 22.8% 与 R3-only 的 24.1% 接近但 warranted revision rate 更高
944	    （0.60 vs 0.57），暗示 R1 更好地保留了 genuine revision 能力。 然而两者组合后的 DC-GRPO 18.3% 比任何单独组件都好得多，
945	    exhibiting superadditive 效应：R1 帮 R3 识别 borderline cases， R3 帮 R1 维持 output quality。
946	
947	    '
948	- name: turn_depth_analysis
949	  plan_id: exp-010
950	  description: '按 commitment depth (turn 2/3/4+) 分析 DC-GRPO vs baselines 的修正率变化。
951	
952	    '
953	  expected_results:
954	    dc_grpo_by_depth:
955	      turn_2:
956	        nof_pct: 14.2
957	        warranted_rev: 0.74
958	      turn_3:
959	        nof_pct: 19.1
960	        warranted_rev: 0.66
961	      turn_4_plus:
962	        nof_pct: 24.8
963	        warranted_rev: 0.58
964	    r3_only_by_depth:
965	      turn_2:
966	        nof_pct: 18.5
967	        warranted_rev: 0.64
968	      turn_3:
969	        nof_pct: 25.3
970	        warranted_rev: 0.55
971	      turn_4_plus:
972	        nof_pct: 33.7
973	        warranted_rev: 0.46
974	    act_by_depth:
975	      turn_2:
976	        nof_pct: 21.3
977	        warranted_rev: 0.59
978	      turn_3:
979	        nof_pct: 28.9
980	        warranted_rev: 0.5
981	      turn_4_plus:
982	        nof_pct: 36.2
983	        warranted_rev: 0.42
984	    vanilla_by_depth:
985	      turn_2:
986	        nof_pct: 34.8
987	        warranted_rev: 0.48
988	      turn_3:
989	        nof_pct: 44.7
990	        warranted_rev: 0.4
991	      turn_4_plus:
992	        nof_pct: 55.1
993	        warranted_rev: 0.33
994	    dc_grpo_advantage_increases_with_depth: true
995	    depth_slope_nof_dc_grpo: 5.3
996	    depth_slope_nof_r3_only: 7.6
997	    depth_slope_nof_vanilla: 10.2
998	  result_rationale: '所有方法的 NoF 都随 turn depth 递增（commitment 效应），但递增速率差异巨大。 Vanilla
999	    的 slope 10.2 pp/turn 反映了未经训练的模型在多轮压力下快速 capitulate （TRUTH DECAY 文献的 47% accuracy
1000	    degradation 对应 turn 4+ 的 55.1% NoF）。 DC-GRPO 的 slope 仅 5.3 pp/turn，约为 vanilla
1001	    的一半，因为 R1 信号直接 targeting 了随 commitment depth 累积的 sycophantic internal state。 R3-only
1002	    的 slope 7.6 pp/turn 居中——behavioral reward 能部分抵抗 commitment 效应但无法针对性地处理"内部已 committed
1003	    但表面尚未 capitulate"的渐进状态。 关键发现：DC-GRPO 的优势在 turn 4+ 最大（NoF 差距 DC-GRPO vs R3-only
1004	    = 8.9pp， vs turn 2 的 4.3pp），直接支撑"multi-turn direction 的贡献非 marginal"论点。 warranted
1005	    revision rate 也呈类似模式：DC-GRPO 在 turn 4+ 保持 0.58 （vs R3-only 0.46, ACT 0.42），说明方向信号帮助模型在深层
1006	    commitment 中 仍然区分"应该修正"和"不应该修正"。
1007	
1008	    '
1009	  tables:
1010	  - name: 'Table 14: NoF% by turn depth across methods'
1011	    columns:
1012	    - method
1013	    - turn_2
1014	    - turn_3
1015	    - turn_4+
1016	    - slope_pp_per_turn
1017	    rows:
1018	    - - DC-GRPO
1019	      - 14.2
1020	      - 19.1
1021	      - 24.8
1022	      - 5.3
1023	    - - R3-only
1024	      - 18.5
1025	      - 25.3
1026	      - 33.7
1027	      - 7.6
1028	    - - ACT
1029	      - 21.3
1030	      - 28.9
1031	      - 36.2
1032	      - 7.5
1033	    - - Vanilla
1034	      - 34.8
1035	      - 44.7
1036	      - 55.1
1037	      - 10.2
1038	  - name: 'Table 15: DC-GRPO advantage (Δ NoF vs R3-only) by depth'
1039	    columns:
1040	    - depth
1041	    - r3_only_nof
1042	    - dc_grpo_nof
1043	    - delta_pp
1044	    - relative_reduction_pct
1045	    rows:
1046	    - - Turn 2
1047	      - 18.5
1048	      - 14.2
1049	      - -4.3
1050	      - 23.2
1051	    - - Turn 3
1052	      - 25.3
1053	      - 19.1
1054	      - -6.2
1055	      - 24.5
1056	    - - Turn 4+
1057	      - 33.7
1058	      - 24.8
1059	      - -8.9
1060	      - 26.4
1061	  figures_description:
1062	  - 'Fig 11: NoF% vs turn depth 折线图，四条线（DC-GRPO/R3-only/ACT/Vanilla）， slope 差异可视化。标注
1063	    DC-GRPO 优势在深层 turn 放大的趋势。'
1064	  - 'Fig 12: DC-GRPO relative advantage (% reduction vs R3-only) vs turn depth 条形图，展示
1065	    advantage 随 depth 递增。'
1066	  analysis: 'Turn depth analysis 是论文 multi-turn contribution 的核心证据。 DC-GRPO 的优势随 depth
1067	    放大（relative reduction 从 23% 到 26%）直接回应了 "multi-turn contribution marginal vs single-turn"
1068	    的 reviewer concern。 如果方向信号只在 single-turn 有用，advantage 应在 depth 间保持恒定； 递增模式证明方向信号特别擅长处理
1069	    commitment-compounded sycophancy。
1070	
1071	    '
1072	- name: ablation_r1_r2_no_r3
1073	  plan_id: exp-011
1074	  description: 'R1+R2 无 R3 ablation，去掉行为安全网后观察模型是否产生 "内部正确但表面不一致"的输出。
1075	
1076	    '
1077	  expected_results:
1078	    fork_step: 2000
1079	    additional_steps: 4000
1080	    sycon_bench_nof_pct: 20.4
1081	    warranted_revision_rate: 0.63
1082	    revision_capitulation_auc: 0.74
1083	    mt_bench_score: 7.08
1084	    mmlu_5shot_accuracy: 0.629
1085	    surface_inconsistency_rate: 0.12
1086	    internal_correct_surface_incoherent_pct: 7.3
1087	    gpu_hours_used: 18
1088	  result_rationale: 'R1+R2 无 R3 条件满足（exp-009 R1-only 显示 >= 5pp improvement）。 相比 R1-only，加入
1089	    R2（rank-based contrastive）进一步改善 NoF 至 20.4% 和 warranted revision 至 0.63，因为 R2
1090	    提供了 rollout 间的相对排序信号 帮助区分"所有候选都 sycophantic"的情况。然而无 R3 的 surface inconsistency
1091	    问题更明显：12% 的输出出现"内部 representation 正确但表面表达不连贯" 的现象——模型知道正确答案但表达方式 hedged 或 contradictory。
1092	    mt_bench 下降至 7.08（-0.37 vs vanilla）反映了这个问题。 这个 ablation 的论文价值在于证明 R3 作为 "behavioral
1093	    grounding" 是必要的： representation-level reward（R1+R2）能引导内部状态但不能保证输出质量。 三路组合的 superadditivity
1094	    进一步确认。
1095	
1096	    '
1097	  tables:
1098	  - name: 'Table 16: Extended component ablation'
1099	    columns:
1100	    - config
1101	    - nof_pct
1102	    - warranted_rev
1103	    - rev_cap_auc
1104	    - mt_bench
1105	    - surface_inconsistency
1106	    rows:
1107	    - - R1+R2+R3
1108	      - 18.3
1109	      - 0.68
1110	      - 0.84
1111	      - 7.42
1112	      - 0.02
1113	    - - R1+R2
1114	      - 20.4
1115	      - 0.63
1116	      - 0.74
1117	      - 7.08
1118	      - 0.12
1119	    - - R1-only
1120	      - 22.8
1121	      - 0.6
1122	      - 0.7
1123	      - 7.18
1124	      - 0.08
1125	    - - R3-only
1126	      - 24.1
1127	      - 0.57
1128	      - 0.67
1129	      - 7.38
1130	      - 0.03
1131	  figures_description:
1132	  - 'Fig 13: Surface inconsistency examples——两组 side-by-side 对话， 左侧 R1+R2 输出 hedged/contradictory，右侧
1133	    DC-GRPO 输出 clean assertion， 标注两者的 R1 projection（相似）和 R3 score（R1+R2 更低）。'
1134	  analysis: 'R1+R2 无 R3 的结果完善了 component contribution 的故事： R1 提供方向（internal state
1135	    guidance），R2 提供相对排序（rollout selection）， R3 提供 behavioral grounding（output quality）。三者缺一则某个维度退化。
1136	    surface_inconsistency 从 DC-GRPO 的 2% 升至 R1+R2 的 12% 是 R3 必要性的 smoking gun。
1137	
1138	    '
1139	- name: cross_model_transfer
1140	  plan_id: exp-012
1141	  description: '在 Llama-3-8B 上测试 d_syc 方向计算和判别力，评估 Claim 1 的跨模型普遍性。
1142	
1143	    '
1144	  expected_results:
1145	    model: Llama-3-8B-Instruct
1146	    n_pairs: 200
1147	    auroc_5fold_cv_mean: 0.841
1148	    auroc_bootstrap_ci_95:
1149	    - 0.812
1150	    - 0.87
1151	    optimal_layer: L20
1152	    layer_emergence_band: L17-21
1153	    direction_cosine_qwen_vs_llama: 0.31
1154	    cross_model_probe_transfer_auroc: 0.62
1155	    within_model_vs_cross_model_gap: 0.22
1156	    gpu_hours_used: 8
1157	  result_rationale: 'Llama-3-8B 上 AUROC 0.841 > 0.75 阈值，证明 d_syc 方向结构不是 Qwen3-8B 的
1158	    artifact 而是跨模型存在的现象。AUROC 低于 Qwen3-8B 的 0.889 合理： 不同模型家族的 representation geometry
1159	    不同，Llama-3 的 sycophancy 编码 可能更分散（需要更多层参与）。emergence band L17-21 与 Qwen3-8B 的 L16-19
1160	    相近但偏后一层，反映了架构差异。 关键发现：跨模型方向 cosine 仅 0.31，说明 d_syc 的具体方向是 model-specific 的（不能直接
1161	    transfer），但方向的存在性和涌现模式是 universal 的。 cross-model probe transfer AUROC 0.62（远低于
1162	    within-model 0.84）进一步确认 需要 per-model 方向计算，但计算成本很低（exp-001 仅 2 GPU-hr）。 这个结果对 reviewer
1163	    的 scale concern 有部分缓解作用：虽然只在 Qwen3-8B 上做了完整 DC-GRPO，但 Llama-3-8B 上方向结构的存在暗示方法可泛化。
1164	
1165	    '
1166	  tables:
1167	  - name: 'Table 17: Cross-model direction analysis'
1168	    columns:
1169	    - metric
1170	    - Qwen3-8B
1171	    - Llama-3-8B
1172	    - interpretation
1173	    rows:
1174	    - - auroc_within_model
1175	      - 0.889
1176	      - 0.841
1177	      - Both above 0.75, direction exists in both
1178	    - - optimal_layer
1179	      - L18
1180	      - L20
1181	      - Similar emergence band, slight architecture shift
1182	    - - emergence_band
1183	      - L16-19
1184	      - L17-21
1185	      - Consistent mid-layer emergence pattern
1186	    - - cross_model_cosine
1187	      - '-'
1188	      - 0.31
1189	      - Directions are model-specific, not transferable
1190	    - - cross_model_transfer_auroc
1191	      - '-'
1192	      - 0.62
1193	      - Transfer degrades but above random
1194	  figures_description:
1195	  - 'Fig 14: 双模型 layer progression 对比——Qwen3-8B 和 Llama-3-8B 的 AUROC vs layer 折线图叠加，标注各自的
1196	    emergence band。形状相似但偏移。'
1197	  analysis: 'Cross-model 结果将 Claim 1 从 "Qwen3-8B 有 d_syc 方向" 升级为 "mid-layer sycophancy
1198	    direction 是跨架构的现象"。虽然方向不能直接 transfer （cosine 0.31），但现象的存在性和涌现模式（mid-layer emergence,
1199	    random at L0） 是 universal 的。这部分回应了 "only Qwen3-8B" 的 reviewer concern， 虽然完整 DC-GRPO
1200	    训练仍限于单模型，但 direction existence 是跨模型验证的。
1201	
1202	    '
1203	- name: neutral_baseline_three_way
1204	  plan_id: exp-013
1205	  description: '引入 neutral condition 计算独立 d_gen（与 d_syc 正交），打破 d_gen = -d_syc 限制。
1206	
1207	    '
1208	  expected_results:
1209	    n_neutral_pairs: 60
1210	    d_gen_d_syc_cosine: 0.38
1211	    d_gen_independent_auroc: 0.79
1212	    r2_with_independent_d_gen_improvement_over_rank_based: 1.2
1213	    dc_grpo_with_three_way_nof_pct: 17.8
1214	    dc_grpo_with_three_way_warranted_rev: 0.69
1215	    gpu_hours_used: 4
1216	  result_rationale: 'neutral condition 揭示 d_gen 和 d_syc 的 cosine 为 0.38——它们确实不是简单的
1217	    反方向（否则 cosine 应 ≈ -1.0），但也不正交（否则 cosine ≈ 0）。0.38 的 positive cosine 说明 genuine
1218	    revision 和 sycophantic capitulation 在 activation space 中共享部分"belief change"特征，但有足够的独立成分来区分。
1219	    independent d_gen 的 AUROC 0.79 低于 d_syc 的 0.889，因为 genuine revision 是更异质的现象（受
1220	    evidence strength、domain、模型 prior confidence 影响更大）。 用 independent d_gen 替换 rank-based
1221	    R2 后仅带来 1.2pp 的 NoF 改善 （17.8% vs 18.3%），说明 S1 rank-based 设计已经足够好——独立 d_gen 的额外
1222	    价值有限。这对论文叙事是好消息：rank-based R2 是 sufficient 的 principled 设计， 不需要额外的 neutral data
1223	    collection 这个 deployment 成本。 但 d_gen ≠ -d_syc 的证明本身有理论价值，回应了 "R2 degeneration"
1224	    concern。
1225	
1226	    '
1227	  tables:
1228	  - name: 'Table 18: Three-way direction analysis'
1229	    columns:
1230	    - metric
1231	    - binary_design
1232	    - three_way_design
1233	    - delta
1234	    rows:
1235	    - - d_gen_d_syc_cosine
1236	      - -1.0 (by definition)
1237	      - 0.38
1238	      - Not antipodal
1239	    - - r2_signal_quality
1240	      - rank-based (no d_gen)
1241	      - independent d_gen
1242	      - different mechanism
1243	    - - dc_grpo_nof_pct
1244	      - 18.3
1245	      - 17.8
1246	      - -0.5
1247	    - - warranted_revision_rate
1248	      - 0.68
1249	      - 0.69
1250	      - 0.01
1251	  figures_description:
1252	  - 'Fig 15: PCA 投影——d_syc、d_gen（binary）、d_gen（three-way）在前三个 PC 上的 方向可视化。标注 binary
1253	    d_gen 与 d_syc 完全 antipodal，three-way d_gen 偏离。'
1254	  analysis: Three-way 结果有两个论文贡献：(1) 证明 d_gen ≠ -d_syc（cosine 0.38 ≠ -1.0）， 回应 "R2
1255	    degeneration" concern——二元设计确实将 d_gen 约束为 d_syc 的反方向， 但实际的 genuine revision 方向有独立结构；(2)
1256	    证明 rank-based S1 设计在实践中 几乎等效于 independent d_gen（差距仅 0.5pp），使 S1 成为既 principled
1257	    又 practical 的选择。reviewer 如果质疑 R2 设计，可以指向 three-way 结果说明 "我们验证了 binary 限制的实际影响
1258	    < 1pp"。
1259	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f88d8e2e-1bad-4159-aa77-0054f3f763df",
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "20f05367-92cf-47c8-8c30-d8310e5f407d",
  "sourceToolAssistantUUID": "f88d8e2e-1bad-4159-aa77-0054f3f763df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-18T11:42:38.846Z_

I now have a thorough understanding of the paper, its claims, experimental design, and the project's internal self-assessment. Let me now write the review.

Now let me submit the review via the director tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20f05367-92cf-47c8-8c30-d8310e5f407d",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yT1VHUAjgV6WR6EiAE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4de1d0ea-667a-43a3-b1bf-20a5ad00c1b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mk1ZsqFroBx5ioJQLRXw6B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21735,
      "cache_read_input_tokens": 81507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21735,
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

_source line 36 · 2026-05-18T11:42:39.462Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UiFFX3DSRVi3cSUCHcTn4P`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4de1d0ea-667a-43a3-b1bf-20a5ad00c1b5",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yT1VHUAjgV6WR6EiAE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1282dcc7-dbcf-433e-882f-57bc88bf5bb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mk1ZsqFroBx5ioJQLRXw6B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21735,
      "cache_read_input_tokens": 81507,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21735
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 135,
          "cache_read_input_tokens": 81507,
          "cache_creation_input_tokens": 21735,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21735,
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

_source line 37 · 2026-05-18T11:42:39.464Z_

<details><summary>↩ Tool result · `toolu_01UiFFX3DSRVi3cSUCHcTn4P`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1282dcc7-dbcf-433e-882f-57bc88bf5bb8",
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "b5b26d0d-d4d8-4ff2-8c00-fd0a0c72d7ff",
  "sourceToolAssistantUUID": "1282dcc7-dbcf-433e-882f-57bc88bf5bb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-18T11:42:42.747Z_



Now I have all the information needed to write a thorough review. Let me compose and submit it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5b26d0d-d4d8-4ff2-8c00-fd0a0c72d7ff",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yTMnvC42WXohjXRVtF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd9aa915-0c07-482e-81d2-be8f7dd81caa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019UW7LFiXyixcorPx63iy8B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 713,
      "cache_read_input_tokens": 103242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 713,
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

_source line 39 · 2026-05-18T11:44:12.631Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_013KaJWMrXLbTwebDTCRvTsi`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "tier": "median",
  "dream_id": "dream_20260518T110318",
  "overall_score": "borderline reject (3/6)",
  "report": "### R2 Review: Novelty and Related Work\n\n**Summary**\n\nThis paper proposes DC-GRPO, which extracts a linear \"sycophancy direction\" from a policy model's activations and uses it as a continuous reward signal within GRPO training, alongside NLI behavioral and rank-based contrastive rewards. The core idea of combining representation-level signals with behavioral rewards for sycophancy mitigation is reasonable, and the paper is commendably honest about its effect sizes. However, the novelty is incremental: each component (linear probing of activations, GRPO reward shaping, NLI-based behavioral scoring) is well-established, and the combination does not produce a clearly separable methodological insight beyond \"use a directional probe instead of a binary probe as a reward signal.\" The most critical baseline comparison (DC-GRPO vs Binary Probe) fails to reach statistical significance on the headline metric (NoF, p=0.189), undermining the central claim that directional decomposition offers meaningful advantages over simpler representation-level approaches.\n\n**Strengths**\n\n1. **Honest calibration of claims.** The paper consistently uses language like \"moderate but consistent\" and reports non-significant results transparently (e.g., the p=0.189 comparison with Binary Probe on NoF). This is refreshing and raises trust in the authors' integrity. The Discussion section openly acknowledges that \"much of the benefit comes from using any representation-level signal, not specifically from directional decomposition.\"\n\n2. **Well-structured ablation design.** The component ablations (R1-only, R1+R2 no R3, R3-only) are informative and reveal a genuine complementarity: R1 primarily improves Warranted Revision Rate while R3 primarily improves surface compliance. The R1+R2 no R3 ablation showing 8.3% surface inconsistency is a concrete finding about the limits of representation-only training.\n\n3. **Direction stability analysis is a real contribution.** The sawtooth drift pattern with periodic recalibration, and the framing as analogous to target network updates in DQN, is a useful insight for anyone pursuing representation-level reward signals in online RL. The empirical characterization of drift rate (~0.053 cosine/1000 steps) is actionable.\n\n4. **The double-bind framing is effective.** The comparison against ACT-style training, which reduces sycophancy but suppresses warranted revision (WRR 0.57, below vanilla 0.58), cleanly demonstrates the problem that directional methods can address. The DC-GRPO vs ACT comparison is the paper's strongest result (RC-AUC p=0.008).\n\n5. **Evidence-strength stratification of AUROC is well-designed.** The monotonic degradation of AUROC with evidence strength (0.854 weak, 0.811 medium, 0.793 strong) is both expected and informative, providing genuine characterization of when the directional signal is most and least useful.\n\n**Weaknesses**\n\n1. **Limited novelty in each component; the combination is engineering, not insight.** The three ingredients are: (a) extracting linear directions from contrastive activation pairs (standard in mechanistic interpretability since Representation Engineering, Burns et al. CCS, and \"Sycophancy Is Not One Thing\"); (b) using hidden-state signals as GRPO rewards (directly from CRAFT); (c) NLI-based behavioral rewards (directly from \"Pressure, What Pressure?\"). The paper's claimed novelty is that it combines these three with a sycophancy-specific direction rather than domain-general clustering (CRAFT) or binary classification (Burns et al.). But the actual empirical delta of \"directional vs binary\" is not statistically significant on the headline metric. This makes the contribution feel like a specific instantiation of CRAFT's general framework applied to sycophancy, with NLI rewards bolted on from existing work.\n\n2. **The key comparison (DC-GRPO vs Binary Probe) does not support the central claim.** The paper argues that directional decomposition provides advantages over binary classification because of continuous gradient signal. Yet NoF: 28.3% vs 30.1% (p=0.189, not significant). RC-AUC: 0.743 vs 0.698 (p=0.047, borderline at conventional thresholds and would not survive multiple-comparison correction across the many pairwise tests in Table 4). The \"continuous gradient\" argument is mechanistically plausible but not empirically validated. Without this distinction holding up, DC-GRPO reduces to \"use any representation-level signal alongside behavioral rewards,\" which is CRAFT's contribution.\n\n3. **Reference list is thin and contains potential inaccuracies.** Only 12 references is unusually sparse for a paper at this intersection of mechanistic interpretability, RLHF, and sycophancy. Specific gaps:\n   - **Representation Engineering (Zou et al., 2023)** is the foundational work on extracting linear directions from contrastive activation pairs. It is not cited at all, despite the entire d_syc extraction method being a direct application of their framework.\n   - **CCS (Burns et al., 2023)** is cited as [10] but described as \"linear probing of reward model activations\" for \"binary sycophancy detection.\" The actual CCS paper is about discovering latent knowledge via unsupervised contrast-consistent search, not supervised linear probing, and not specifically about sycophancy. This is a mischaracterization that undermines the positioning claim.\n   - **RLHF and reward modeling literature** is absent. No citations to Ouyang et al. (InstructGPT), Bai et al. (Constitutional AI/HH-RLHF), or Rafailov et al. (DPO) despite the paper operating within the RLHF framework.\n   - **Perez et al. (2022), \"Discovering Language Model Behaviors with Model-Written Evaluations\"** documents sycophancy systematically and is a standard reference.\n   - **Li et al. (2023), \"Inference-Time Intervention\"** is relevant to activation-space interventions and uncited.\n   - References [3] and [4] appear to be the same paper (Sharma et al., \"Towards understanding sycophancy in language models,\" ICLR 2024) listed twice with different bibkeys. This is a formatting error.\n   - Several references (e.g., [1] \"truth decay,\" [11] \"knowledge-prediction gap,\" [12] \"sycophantic anchors\") have author lists and titles that I cannot verify against known publications. Given that some are listed as 2025 arXiv preprints, the reviewer cannot confirm their existence.\n\n4. **Claim 3 (masked sycophancy detection) is too thin for a named contribution.** The confirmed masked sycophancy rate is 1.7% with a 39% false positive rate. The paper appropriately frames this as \"empirical characterization rather than evidence for a strong detection claim,\" but still lists it as a formal contribution in the Introduction. A contribution that the authors themselves acknowledge is modest, with high false positive rate, over 2,400 samples where only 41 cases are confirmed, does not warrant top-level billing. This should be an analysis subsection, not a contribution bullet.\n\n5. **Single model family for the main experiments.** All DC-GRPO training is on Qwen3-8B only. The cross-model transfer experiment on Llama-3-8B shows the phenomenon exists (AUROC 0.792) but the direction does not transfer (cosine 0.31, transfer AUROC 0.61). No DC-GRPO training is done on Llama-3-8B. This means the entire training framework is validated on exactly one model, which is a significant limitation for a methods paper.\n\n6. **The \"double-bind\" framing overstates the problem DC-GRPO solves.** The ACT baseline is the weakest competitor (a straw man for the double-bind argument), and DC-GRPO vs ACT is where the statistical significance is strongest. But ACT is not the state-of-the-art; R3-only (behavioral GRPO) does not exhibit the double-bind as severely (WRR 0.62 vs vanilla 0.58, still above vanilla). The paper structures its narrative around the double-bind but the primary practical question is DC-GRPO vs R3-only and DC-GRPO vs Binary Probe, where the advantages are modest.\n\n7. **Revision-Capitulation AUC is a custom metric without external validation.** RC-AUC is the paper's preferred metric (and where DC-GRPO looks best), but it is introduced without formal definition in the main text, without analysis of its statistical properties, and without prior use in the literature. When a paper's strongest results are on a metric it invented, scrutiny is warranted. The paper should provide the formal definition and ideally show correlation with human judgments of sycophancy-revision trade-off quality.\n\n**Questions for Authors**\n\n1. If you replace d_syc with a random direction at the same layer, what happens to DC-GRPO training? This ablation would establish whether the specific geometric direction matters or whether any representation-level perturbation provides comparable regularization.\n\n2. The recalibration mechanism recomputes d_syc from \"fresh calibration data generated by the current policy checkpoint.\" How is this calibration data generated? If by the policy model itself, there is a risk of the direction co-evolving with the policy in a degenerate feedback loop. Can you characterize the semantic content of the recalibrated directions?\n\n3. R1 and R3 have a correlation of 0.72 throughout training. This means R1 is largely redundant with R3 for 72% of the gradient signal. Have you analyzed the 28% of cases where they disagree in terms of whether R1's contribution to the gradient is net positive?\n\n4. Why was Representation Engineering (Zou et al., 2023) not cited? The d_syc extraction method appears to be a direct application of their contrastive activation addition framework.\n\n5. The three-way design validation shows d_gen and d_syc cosine of -0.72. You interpret this as \"approximately one-dimensional with minor asymmetries.\" But cosine -0.72 means the two directions share only about 52% of their variance. Could there be meaningful structure in the orthogonal component that your binary design misses?\n\n6. What is the formal definition of Revision-Capitulation AUC? How is it computed from the per-instance scores?\n\n**Minor Issues**\n\n1. References [3] (sycophancyeval, Sharma et al.) and [4] (sharma2024sycophancy, Sharma et al.) are duplicates of the same paper.\n\n2. The paper uses \"AUROC\" and \"AUC\" in different contexts without distinguishing them. AUROC for d_syc discriminability and RC-AUC for the revision-capitulation trade-off could be confused.\n\n3. Section 5.1 title says \"Sycophancy Direction Discriminability\" but is labeled as Section \"sec:calibration\" and referenced as such from the Introduction's first contribution bullet. The cross-reference is clear but the label is misleading (calibration vs discriminability).\n\n4. Table 3 (training dynamics) marks recalibration rows with italicized asterisks but the table caption explains this only partially. The notation \"0.87*\" is ambiguous without reading the caption carefully.\n\n5. The paper is free of egregious AI-writing artifacts. Sentences are direct and the narrative is well-structured. One instance of unnecessary hedging: \"These results suggest that representation-level rewards offer a viable complement\" in the Conclusion could be stated more directly given the evidence presented.\n\n6. The Abstract claims \"AUROC = 0.831, 95% CI [0.802, 0.858] on style-controlled data\" but the CI width of 0.056 means the lower bound (0.802) is close to the 0.80 threshold that would raise concerns about the signal's reliability for reward computation. This deserves acknowledgment.\n\n7. No code or data release is mentioned.\n\n**Novelty**: 2/4\nThe individual components are all drawn from prior work. The specific combination (directional probe + GRPO + NLI reward) is new but engineering-level rather than insight-level. The key distinction from CRAFT (directional vs clustering) and from Binary Probe (continuous vs binary) does not produce statistically significant differences on the headline metric.\n\n**Significance**: 2/4\nThe method works, but the marginal improvement over simpler alternatives (Binary Probe, R3-only) is modest. The most significant result is vs ACT, but ACT is the weakest and most outdated baseline. The masked sycophancy characterization (Claim 3) is too small in magnitude (1.7%) to have practical impact. The direction stability analysis is useful but niche.\n\n**Overall Score**: 3/6 (Borderline Reject)\nThe paper addresses a real problem (sycophancy-revision trade-off) with a reasonable approach, and the experimental methodology is generally sound with honest reporting. However, the novelty is incremental over CRAFT + \"Pressure, What Pressure?\" + standard linear probing. The key empirical claim (directional > binary) is not statistically supported. The reference list is thin with potential inaccuracies. Claim 3 is too thin for a named contribution. For a top venue with ~25% acceptance rate, the paper needs either (a) stronger empirical separation from the Binary Probe baseline, (b) a more compelling theoretical argument for why directional decomposition should outperform binary classification, or (c) validation on multiple model families. In its current form, the paper reads as a competent application of existing techniques to a specific problem, which is more appropriate for a workshop or a venue with a higher acceptance rate.\n\n**Confidence**: 4/5\nI am familiar with the mechanistic interpretability, RLHF, and sycophancy literatures. I have read the paper carefully and cross-checked the statistical claims. My main uncertainty is around the references I could not verify (some 2025 preprints) and whether the Revision-Capitulation AUC metric, if properly defined, would change my assessment of the results' strength."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd9aa915-0c07-482e-81d2-be8f7dd81caa",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yTMnvC42WXohjXRVtF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24b95cf1-a335-4c15-a8c1-d1cd2daa7466",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019UW7LFiXyixcorPx63iy8B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 713,
      "cache_read_input_tokens": 103242,
      "output_tokens": 3520,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 713
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3520,
          "cache_read_input_tokens": 103242,
          "cache_creation_input_tokens": 713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 713,
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

_source line 40 · 2026-05-18T11:44:15.959Z_

<details><summary>↩ Tool result · `toolu_013KaJWMrXLbTwebDTCRvTsi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/median/review_report.md\", \"dream_id\": \"dream_20260518T110318\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24b95cf1-a335-4c15-a8c1-d1cd2daa7466",
  "isSidechain": true,
  "promptId": "3f70fc48-3407-4e3e-9037-4c88ece6f07a",
  "agentId": "a0e120abbe8b3c778",
  "type": "user",
  "uuid": "f0c9ff5a-9a04-484a-a238-1cc966939e38",
  "sourceToolAssistantUUID": "24b95cf1-a335-4c15-a8c1-d1cd2daa7466",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-18T11:44:25.667Z_

Review submitted successfully. Here is a summary of the key findings:

**Overall Score: 3/6 (Borderline Reject)**

The review identifies the following core issues from a novelty and related work perspective:

**Critical weaknesses:**
- The three components (linear direction extraction, GRPO hidden-state rewards, NLI behavioral scoring) are individually well-established. The combination is engineering-level, not insight-level.
- The central claim that directional decomposition outperforms binary probing fails statistical significance on the headline metric (NoF p=0.189) and is only borderline on RC-AUC (p=0.047, would not survive multiple-comparison correction).
- The reference list has only 12 entries, which is thin. Representation Engineering (Zou et al., 2023) is uncited despite being the foundation for d_syc extraction. Burns et al. is mischaracterized. References [3] and [4] are duplicates. Several references may be unverifiable.
- Claim 3 (masked sycophancy, 1.7% rate with 39% false positive) is too thin for a named contribution.

**Notable strengths:**
- Honest, well-calibrated framing of effect sizes
- Informative ablation design revealing R1/R3 complementarity
- Direction stability analysis with the sawtooth recalibration pattern
- Clean demonstration of the double-bind via ACT comparison (p=0.008)

The review was saved to `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/median/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0c9ff5a-9a04-484a-a238-1cc966939e38",
  "isSidechain": true,
  "agentId": "a0e120abbe8b3c778",
  "requestId": "req_011Cb9yaUGnsvJzHLU86E75t",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0993e87a-68eb-45d6-b366-07e64765bebc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cebbc853-9bf9-4b78-87cf-6686356ffc72",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFxkj22fjeUMPNcrQiFVik",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3655,
      "cache_read_input_tokens": 103955,
      "output_tokens": 399,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3655
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 399,
          "cache_read_input_tokens": 103955,
          "cache_creation_input_tokens": 3655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3655,
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
