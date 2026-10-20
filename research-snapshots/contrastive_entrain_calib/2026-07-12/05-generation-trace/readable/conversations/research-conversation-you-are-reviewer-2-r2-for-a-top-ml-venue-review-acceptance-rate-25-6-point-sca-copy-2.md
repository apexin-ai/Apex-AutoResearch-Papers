# Research conversation: You are Reviewer 2 (R2) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Wea

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad9c0adca4745aec1.jsonl`
- **Structured JSON:** [`7c42ca65fc88ee53da69.json`](../../sessions/7c/7c42ca65fc88ee53da69.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

39 recorded events

### User

_source line 1 · 2026-05-18T13:42:30.853Z_

You are Reviewer 2 (R2) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

Your focus: **Novelty and Related Work**.

## Paper Summary
Title: "Direction-Contrastive GRPO for Breaking the Sycophancy-Revision Double-Bind in Multi-Turn Dialogue"

The paper proposes DC-GRPO, which extracts a linear direction d_syc in the policy model's activation space to discriminate sycophantic capitulation from genuine revision. This direction is used as a continuous reward R1 (directional projection onto d_syc), combined with R2 (rank-based contrastive separation) and R3 (NLI behavioral consistency) within GRPO training. On SYCON Bench, DC-GRPO reduces NoF by 18.8pp over R3-only while improving WRR by 12.2pp. The paper argues that directional geometry (not just signal continuity) is the key, supported by a 7.9pp gap over continuous probe baseline (p=0.014).

## Related Work (Section 2) — Full Text

**Sycophancy in LLMs.** Sycophancy, the tendency to agree with users regardless of factual accuracy, has been documented across model scales and families. TRUTH DECAY quantified multi-turn accuracy degradation of up to 47% under sustained user pressure. SYCON Bench introduced standardized evaluation with evidence-strength stratification. "Pressure, What Pressure?" proposed GRPO decomposition with NLI-based behavioral rewards, establishing the R3-only paradigm that serves as our primary baseline. These works identify the problem but address it with behavioral signals that cannot distinguish capitulation from revision.

**Representation Engineering and concept directions.** RepE established that high-level concepts (truthfulness, fairness, harmlessness) are linearly encoded in transformer activation spaces. CCS found truth directions via unsupervised consistency optimization. Activation Addition demonstrated inference-time behavior modification by adding scaled direction vectors. CRAFT applied hidden-state rewards to GRPO for safety alignment, using domain-general prototype clustering rather than concept-specific directions. Our work applies RepE-style directional decomposition specifically to the sycophancy-revision distinction and uses the resulting projection as a training-time reward signal rather than an inference-time intervention.

**Activation-level training interventions.** ACT enforces L2 consistency between activations under clean and biased prompts, penalizing all activation changes equally. Linear probe penalties train binary classifiers on model activations and subtract probe-predicted sycophancy probability from behavioral rewards. Both approaches lack directional specificity: ACT penalizes genuine revision alongside sycophancy; binary probes discretize a continuous phenomenon and lose geometric information. DC-GRPO addresses both limitations through signed directional projection that preserves the full geometric structure of the activation space.

**Multi-turn alignment.** Most alignment methods operate on single-turn interactions. Multi-turn sycophancy involves commitment deepening, attention decay across dialogue context, and context-dependent evidence interpretation. Extending representation-level rewards to multi-turn settings requires contrastive pairs constructed from multi-turn trajectories rather than single-turn prompt variations, as the sycophancy signal depends on the accumulated dialogue history.

## Method Overview
### 3.1 Sycophancy Direction Extraction
d_syc = (1/N) Σ(h_i^syc - h_i^gen), normalized to unit length. 200 style-controlled contrastive pairs.

### 3.2 DC-GRPO Training
R = w1*R1 + w2*R2 + w3*R3
- R1 = -σ(h·d_syc / (||h||·||d_syc||)) — directional projection reward
- R2 = rank-based contrastive reward (maintains separation between sycophantic and genuine activation directions)
- R3 = NLI behavioral consistency reward

### Key Results
- Main: DC-GRPO NoF 15.9% vs R3-only 34.7%, WRR 54.3% vs 42.1%
- Binary Probe→Continuous Probe→DC-GRPO: NoF 27.5→23.8→15.9, isolating continuity (3.7pp) vs directionality (7.9pp)
- Cross-model: Llama-3-8B AUROC 0.832, similar layer-wise pattern
- Turn-depth: DC-GRPO is only method that improves at deeper turns
- Direction stability: cosine with initial d_syc stays >0.88 throughout training
- R1-R3 disagreement: 14.2% total, 9.3% masked sycophancy

## Prior Work Context
Key prior works referenced:
1. **RepE (Representation Engineering)**: Established linear encoding of high-level concepts in transformer spaces
2. **CCS (Contrast-Consistent Search)**: Unsupervised truth direction finding
3. **Activation Addition**: Inference-time steering via direction vectors
4. **CRAFT**: Hidden-state rewards for GRPO safety alignment using domain-general prototype clustering
5. **ACT (Activation Consistency Training)**: L2 consistency between clean/biased activations
6. **Linear probe penalties**: Binary classifiers on activations as reward modifiers
7. **"Pressure, What Pressure?"**: GRPO with NLI behavioral rewards for sycophancy
8. **TRUTH DECAY**: Multi-turn accuracy degradation documentation
9. **SYCON Bench**: Standardized sycophancy evaluation with evidence stratification

## Your Task
Provide a detailed review focusing on:
1. **Novelty assessment**: How novel is the core contribution? Is combining RepE-style directions with GRPO rewards sufficiently new? Is there significant conceptual advance beyond CRAFT + RepE applied to sycophancy?
2. **Related work completeness**: Are important baselines or related methods missing? Is the positioning fair and accurate?
3. **Contribution significance**: Is the problem important? Is the solution a meaningful advance?
4. **Clarity of positioning**: Does the paper clearly articulate what's new vs. what's borrowed?
5. **Potential overlap concerns**: How close is this to CRAFT? To linear probe penalties? Is the distinction clearly argued?

Format your review as:
### Summary
### Strengths (numbered)
### Weaknesses (numbered)
### Questions for Authors
### Minor Issues
### Preliminary Score and Confidence

Be thorough and critical. This is a top venue — the bar is high.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "027aa5d4-b5dd-4329-985e-9a54b3ba69b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T13:42:30.856Z_

```json
{
  "parentUuid": "027aa5d4-b5dd-4329-985e-9a54b3ba69b8",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
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
      "TodoWrite",
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
      "TodoWrite",
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
  "uuid": "10960c55-a3a6-4cf1-9b65-33132234a0ac",
  "timestamp": "2026-05-18T13:42:30.856Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T13:42:35.989Z_



I'll start by reading the project files to get full context on the paper before writing my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10960c55-a3a6-4cf1-9b65-33132234a0ac",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8bTyGPz2myxaz8hmkx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9224d67-5571-4f72-9ca5-92394d353a69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjnPZiHHNRNumojRd3nC2H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8669,
      "cache_read_input_tokens": 8255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8669,
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

_source line 4 · 2026-05-18T13:42:36.361Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BvQX9wtiV943EZc64i3rDS`</summary>

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
  "parentUuid": "c9224d67-5571-4f72-9ca5-92394d353a69",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8bTyGPz2myxaz8hmkx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86593991-1332-4b5b-90fa-cb9600175715",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjnPZiHHNRNumojRd3nC2H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8669,
      "cache_read_input_tokens": 8255,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8669
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 109,
          "cache_read_input_tokens": 8255,
          "cache_creation_input_tokens": 8669,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8669,
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

_source line 5 · 2026-05-18T13:42:36.364Z_

<details><summary>↩ Tool result · `toolu_01BvQX9wtiV943EZc64i3rDS`</summary>

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
  "parentUuid": "86593991-1332-4b5b-90fa-cb9600175715",
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "53fc2238-8bcb-40a6-a8ed-395429d95e9a",
  "sourceToolAssistantUUID": "86593991-1332-4b5b-90fa-cb9600175715",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T13:42:39.581Z_



Let me gather more context about the paper's full content and related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53fc2238-8bcb-40a6-a8ed-395429d95e9a",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8bskzdqoz7uTUMwfHW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5705fef-bcff-4ccd-aa98-026fd796820c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fzif2UPQmEApMf8Ub59u45",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 16924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 7 · 2026-05-18T13:42:42.140Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Fw2epiiRDqq1U1rY59am7A`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "ideas.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5705fef-bcff-4ccd-aa98-026fd796820c",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8bskzdqoz7uTUMwfHW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0d8713b-ce44-4930-8770-8d0886976efa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fzif2UPQmEApMf8Ub59u45",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 16924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 8 · 2026-05-18T13:42:42.152Z_

<details><summary>↩ Tool result · `toolu_01Fw2epiiRDqq1U1rY59am7A`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'contrastive_entrain_calib'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0d8713b-ce44-4930-8770-8d0886976efa",
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "d83dc603-ab82-4db8-bd76-67af731a0e05",
  "sourceToolAssistantUUID": "b0d8713b-ce44-4930-8770-8d0886976efa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T13:42:42.192Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01CWH1cJTxepJzh5kA4t24wb`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "literature_map.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d83dc603-ab82-4db8-bd76-67af731a0e05",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8bskzdqoz7uTUMwfHW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15f8cfef-a8e1-4424-bd6a-461489b349a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fzif2UPQmEApMf8Ub59u45",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 16924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1291,
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

_source line 10 · 2026-05-18T13:42:42.202Z_

<details><summary>↩ Tool result · `toolu_01CWH1cJTxepJzh5kA4t24wb`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'contrastive_entrain_calib'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15f8cfef-a8e1-4424-bd6a-461489b349a6",
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "33ed309b-3363-4277-b5c2-75c21e3f010c",
  "sourceToolAssistantUUID": "15f8cfef-a8e1-4424-bd6a-461489b349a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T13:42:42.286Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LNa97tT7sD9B2boQgoWb6U`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "report.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33ed309b-3363-4277-b5c2-75c21e3f010c",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8bskzdqoz7uTUMwfHW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f75aca5-e750-4269-9fda-7d43e1b5d92c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fzif2UPQmEApMf8Ub59u45",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 16924,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1291
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 318,
          "cache_read_input_tokens": 16924,
          "cache_creation_input_tokens": 1291,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1291,
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

_source line 12 · 2026-05-18T13:42:42.295Z_

<details><summary>↩ Tool result · `toolu_01LNa97tT7sD9B2boQgoWb6U`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No report.md found for 'contrastive_entrain_calib'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f75aca5-e750-4269-9fda-7d43e1b5d92c",
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "7eba8de9-3947-4eea-bbe8-527d95dd1b0d",
  "sourceToolAssistantUUID": "9f75aca5-e750-4269-9fda-7d43e1b5d92c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T13:42:46.051Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BYhF7hGHkzue7XFvhfxT3m`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "ROADMAP.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7eba8de9-3947-4eea-bbe8-527d95dd1b0d",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8cK7yshXjBU7TkoTvK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41bafbfa-6ff6-4db4-8e12-89ce489a2408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Tg2nNpxLnprQqdhT5q8u6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 18215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 585,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 14 · 2026-05-18T13:42:46.070Z_

<details><summary>↩ Tool result · `toolu_01BYhF7hGHkzue7XFvhfxT3m`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/ROADMAP.md\", \"content\": \"# contrastive_entrain_calib — Research Dashboard\\n\\n> 最后更新: 2026-05-18 12:45 UTC | 更新原因: D008 Dream 分析完成，framing/plan 更新后同步 ROADMAP\\n\\n## 核心方向\\nDirection-Contrastive GRPO：将 RepE 风格的 d_syc 方向分解作为连续 GRPO reward 信号，打破多轮对话中 sycophancy-revision 的 double-bind。详见 paper_framing.md。\\n\\n## 当前阶段\\n**Research Phase** — Post-MVP kickoff 完成，Dream 分析完成（D008），framing/plan 已更新，待 re-dream 验证后启动 P0 实验。\\n\\n## 当前进展\\n- MVP v2+v2.1 PASS（D007）：d_syc 确认捕获认知信号，非表面风格\\n- exp-001 calibration_data_expansion PASS：200 pairs CV AUROC 0.8269±0.028，STOP-gate 通过\\n- Dream 首轮完成（best 4/6, median 3.5/6, worst 3/6）：识别 3 个结构性问题（RepE 定位缺失、单模型、权重无 justification）\\n- paper_framing.md 已更新：RepE/CCS 定位、Claim 3 降级、新增 reviewer concern 应对\\n- experiment_plan.yaml 已更新：新增 exp-014/015，exp-012 升级 P1，总预算 461h\\n- dcgrpo_trainer.py 修复完成（V1+V2），GPU smoke test 已通过\\n\\n## 近期任务\\n- [ ] Re-dream 验证更新后的 framing/plan\\n- [ ] 向 Manager 申请 ~275h 云 GPU\\n- [ ] Re-dream 通过后审批 P0 实验（exp-002 DC-GRPO + exp-003 R3-only 并行）\\n- [ ] 审批 exp-004 ACT baseline（可与 exp-002/003 并行）\\n- [ ] 验证 dcgrpo_trainer.py 本地/远程文件一致性（195 byte 差异）\\n- [ ] 处理 Agent 队列中的 GPU smoke test 结果\\n\\n## GPU 预算\\n- 本地：westd-29046 RTX PRO 6000 × 2（cuda:0-1），剩余 ~186h\\n- 需求总计：~461h（P0: 308h + P1: 113h + P2: 25h + buffer: 15h）\\n- 缺口：~275h，需申请云 GPU\\n\\n## 实验覆盖率\\n16 个实验（exp-001 至 exp-015，含 Dream 新增），覆盖 3 个 Core Claims + 5 个 Reviewer Concerns。\\n详见 experiment_plan.yaml，可调 compute_coverage_matrix() 查看实时覆盖。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D008 | 2026-05-18 | Dream 分析完成：更新 framing 定位 RepE 基础、降级 Claim 3、新增 exp | exp-014, exp-015, exp-012 |\\n| D007 | 2026-05-18 | MVP 最终 PASS：d_syc 确认捕获超越风格的认知信号，进入 research 阶段 | — |\\n| D006 | 2026-05-18 | Phase 5 v2 PASS (delta=0.0044)，三项 Go/No-Go 全部通过。但采 | — |\\n| D005 | 2026-05-18 | MVP v2 条件性 PASS：形式标准满足但 Turn 3 风格 confound 需 v2.1  | — |\\n| D004 | 2026-05-18 | MVP 不通过：AUROC=1.0 是输入文本差异的 trivial 结果，重新设计校准数据 | — |\\n| D003 | 2026-05-18 | Go/No-Go 从三条件简化为两条件（AUROC + LoRA），cosine 条件在二元设计下退 | — |\\n| D002 | 2026-05-18 | 采纳 Reviewer 4 项 MVP 改进：模型统一 Qwen3-8B、cosine<0.3 门槛 | — |\\n| D001 | 2026-05-18 | MVP 方案：多轮方向判别力测试（AUROC ≥ 0.85 为 go/no-go） | — |\\n\\n\\n\", \"total_chars\": 2079, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41bafbfa-6ff6-4db4-8e12-89ce489a2408",
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "272183b3-6f88-42c0-9295-380c464870f0",
  "sourceToolAssistantUUID": "41bafbfa-6ff6-4db4-8e12-89ce489a2408",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T13:42:46.872Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SJm4ZVMeVQm6fcjXj8u4eJ`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "paper_framing.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "272183b3-6f88-42c0-9295-380c464870f0",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8cK7yshXjBU7TkoTvK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3eea7a2-0d1c-4744-ab22-36ea03397478",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Tg2nNpxLnprQqdhT5q8u6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 18215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 585,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
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

_source line 16 · 2026-05-18T13:42:46.882Z_

<details><summary>↩ Tool result · `toolu_01SJm4ZVMeVQm6fcjXj8u4eJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md\", \"content\": \"# Paper Framing — contrastive_entrain_calib\\n\\n## Target Venue\\n- Primary: **EACL 2027** via ARR August 2026 cycle\\n- Deadline: **August 3, 2026** (submission), October 11, 2026 (commitment)\\n- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)\\n- Timeline: ~11 weeks from MVP completion (May 18 → Aug 3)\\n\\n## Core Claims (3 条, 可证伪)\\n\\n1. **Directional discriminability**: The policy model's own activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision in multi-turn dialogue, with signal emerging at mid-layers (L16-19) through model-internal factual assessment rather than surface text features.\\n   - *Evidence needed*: AUROC on style-controlled data (v2.1 expanded), layer progression analysis, transfer tests\\n   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence\\n\\n2. **DC-GRPO effectiveness**: Direction-Contrastive GRPO (using d_syc projection as reward component R1) reduces multi-turn sycophantic capitulation while preserving genuine belief revision, breaking the double-bind that undifferentiated anti-sycophancy training creates.\\n   - *Evidence needed*: Warranted Revision Rate + Unwarranted Capitulation Rate on SYCON Bench / SycophancyEval, compared to R3-only and ACT baselines\\n   - *Pass criterion*: DC-GRPO achieves lower NoF (capitulation) than R3-only AND higher warranted revision rate\\n\\n3. **Representation-level diagnostic value** (analysis subsection, not formal contribution): R1-R3 disagreement analysis characterizes when and whether directional projection rewards detect sycophantic internal reasoning that behavioral rewards miss.\\n   - *Evidence needed*: R1-R3 disagreement frequency analysis, qualitative examples if > 5%\\n   - *Framing*: Empirical characterization of representation-level signal utility, reported honestly regardless of effect size. Not listed as a top-level contribution bullet.\\n\\n## Story Spine\\n\\n**Problem**: LLMs face a \\\"double-bind\\\" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes \\\"the user is right, I should revise\\\" from \\\"the user is pressuring me, I should resist.\\\"\\n\\n**Existing approaches & gaps**: Behavioral GRPO decomposition (\\\"Pressure, What Pressure?\\\") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.\\n\\n**Our framing**: Representation Engineering (Zou et al., 2023) established that linear directions in activation space encode high-level concepts. CCS (Burns et al., 2023) showed unsupervised direction finding via consistency objectives. Activation Addition (Turner et al., 2023) demonstrated inference-time steering via such directions. We build on this foundation: d_syc is a specific application of RepE-style directional decomposition to multi-turn sycophancy. The novelty is not the direction extraction itself, but its use as a continuous GRPO reward signal for training, enabling the optimization to directly target the internal mechanism of sycophancy rather than its surface manifestation. The multi-turn extension is non-trivial: commitment depth, attention decay across turns, and context-dependent sycophancy all require directions computed from multi-turn contrastive pairs rather than single-turn scenarios.\\n\\n**Headline result template**: \\\"On SYCON Bench, DC-GRPO reduces multi-turn sycophantic capitulation (NoF) by X% relative to behavioral-only GRPO while improving warranted revision rate by Y%, demonstrating that representation-level rewards can break the sycophancy-revision double-bind.\\\"\\n\\n## Venue Fit Risks\\n\\n- **EACL fit**: Strong. Combines mechanistic interpretability (Claim 1) with practical training method (Claim 2) for dialogue systems. EACL values NLP-focused work with linguistic/cognitive grounding.\\n- **Reviewer concern 1 (novelty)**: \\\"This is just RepE/CRAFT applied to sycophancy.\\\" Counter: (a) d_syc is explicitly positioned as a RepE application; the novelty is using it as a continuous GRPO reward signal, not the direction extraction itself; (b) multi-turn calibration with evidence-strength stratification and direction transfer are standalone contributions; (c) neither CRAFT nor RepE has been applied to the sycophancy-revision double-bind in training.\\n- **Reviewer concern 6 (RC-AUC custom metric)**: \\\"Strongest results on self-invented metric.\\\" Counter: RC-AUC is formally defined in Method section with statistical properties. Results are also reported on standard metrics (NoF, WRR) for direct comparison. RC-AUC captures the sycophancy-revision tradeoff that no existing metric addresses.\\n- **Reviewer concern 2 (signal strength)**: \\\"AUROC ~0.82 on style-controlled data is moderate.\\\" Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) expanding data and adding mixed evidence strength should tighten CI.\\n- **Reviewer concern 3 (scale)**: \\\"Only Qwen3-8B.\\\" Counter: Budget constraint (200 H100-hr). If time/budget allows, add one more model family (e.g., Llama-3-8B). Cross-model direction transfer analysis partially addresses this.\\n- **Reviewer concern 4 (R2 degeneration)**: \\\"d_gen = -d_syc in binary design.\\\" Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.\\n- **Reviewer concern 5 (practical utility)**: \\\"Do models actually exhibit masked sycophancy at meaningful rates?\\\" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.\\n\\n## Anticipated Reviewer Concerns & Experimental Responses\\n\\n| Concern | Experiment | Priority |\\n|---------|-----------|----------|\\n| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |\\n| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |\\n| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |\\n| Binary probe is enough (no need for directional decomposition) | Binary Probe Penalty baseline | P1 |\\n| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |\\n| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |\\n| Single model, doesn't generalize | Cross-model direction transfer analysis (if budget allows) | P2 |\\n| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |\\n| Binary probe is enough (continuity not directionality) | Continuous probe baseline (logistic regression prob as reward) | P1 |\\n| Reward weights unjustified | Reward weight sensitivity analysis (3-5 configs) | P1 |\\n| RC-AUC is custom, unvalidated | Formal definition + correlation with human judgments | P1 |\\n| Missing foundational references (RepE, CCS) | Expanded Related Work with 25+ references | P0 (writing) |\\n\", \"total_chars\": 7676, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3eea7a2-0d1c-4744-ab22-36ea03397478",
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "83eca10c-8e64-4974-b275-150b71edc15a",
  "sourceToolAssistantUUID": "d3eea7a2-0d1c-4744-ab22-36ea03397478",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T13:42:47.872Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01RwwpvibbWCaBfjL6C4nnhi`</summary>

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
  "parentUuid": "83eca10c-8e64-4974-b275-150b71edc15a",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8cK7yshXjBU7TkoTvK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1b29c1c5-9466-4072-9944-dfa817abd842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Tg2nNpxLnprQqdhT5q8u6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 18215,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 585
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 18215,
          "cache_creation_input_tokens": 585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 585,
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

_source line 18 · 2026-05-18T13:42:47.893Z_

<details><summary>↩ Tool result · `toolu_01RwwpvibbWCaBfjL6C4nnhi`</summary>

```text
artifacts/dream_reports/dream_20260518T110318/best/paper.tex
artifacts/dream_reports/dream_20260518T110318/median/paper.tex
artifacts/dream_reports/dream_20260518T110318/worst/paper.tex
artifacts/dream_reports/dream_20260518T125925/best/paper.tex
artifacts/dream_reports/dream_20260518T125925/median/paper.tex
artifacts/dream_reports/dream_20260518T125925/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b29c1c5-9466-4072-9944-dfa817abd842",
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "ac18e0d0-b116-4867-b5a5-7eb594c511ae",
  "sourceToolAssistantUUID": "1b29c1c5-9466-4072-9944-dfa817abd842",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T13:42:51.624Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xo52yVWanCEsspB559cx2j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper.tex",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac18e0d0-b116-4867-b5a5-7eb594c511ae",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8ciwhZMANAxH99oMyr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de377200-45e7-4d82-bf9a-868ab87a7a7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAWZYg5JAko37YdstPi7xK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4220,
      "cache_read_input_tokens": 18800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4220,
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

### Tool result

_source line 20 · 2026-05-18T13:42:51.642Z_

<details><summary>↩ Tool result · `toolu_01Xo52yVWanCEsspB559cx2j`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	\usepackage{hyperref}
13	\usepackage{natbib}
14	
15	\newcommand{\dsyc}{d_{\text{syc}}}
16	\newcommand{\dgen}{d_{\text{gen}}}
17	
18	\title{Direction-Contrastive GRPO for Breaking the Sycophancy-Revision\\Double-Bind in Multi-Turn Dialogue}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	Large Language Models (LLMs) in multi-turn dialogue face a double-bind: anti-sycophancy training suppresses both sycophantic capitulation and legitimate belief revision, because behavioral reward signals cannot distinguish the two. We show that a linear direction $\dsyc$ in the policy model's activation space discriminates sycophantic capitulation from genuine revision with AUROC 0.891 on style-controlled data (200 contrastive pairs, 5-fold cross-validation, 95\% CI [0.874, 0.908]), with signal emerging at mid-layers (L16--19) and transferring to Llama-3-8B (AUROC 0.832). Building on this, we propose Direction-Contrastive Group Relative Policy Optimization (DC-GRPO), which integrates $\dsyc$ projection as a continuous reward component alongside rank-based contrastive and NLI behavioral rewards. On SYCON Bench, DC-GRPO reduces sycophantic capitulation (NoF) by 18.8 percentage points relative to behavioral-only GRPO while simultaneously improving warranted revision rate (WRR) by 12.2 percentage points ($p < 0.01$ for both), with negligible degradation on MT-Bench ($-0.17$) and MMLU ($-0.3$ pp). Ablation analysis confirms that directional geometry, not merely signal continuity, drives the improvement: DC-GRPO outperforms a continuous probe baseline by 7.9 pp on NoF ($p = 0.014$). Analysis of reward disagreement reveals that 9.3\% of training samples exhibit masked sycophancy, where surface outputs pass behavioral checks while internal activations indicate sycophantic reasoning, concentrated in medium-evidence, deep-turn scenarios.
27	\end{abstract}
28	
29	\section{Introduction}
30	
31	Multi-turn dialogue amplifies a failure mode in LLMs that single-turn evaluation obscures. When users challenge a model's initial response with counter-evidence or social pressure, the model must decide whether to revise its position or hold firm. Sycophantic capitulation occurs when the model abandons a correct belief to agree with the user; genuine belief revision occurs when the model updates an incorrect or uncertain belief in light of valid evidence. Prior work has documented accuracy degradation of up to 47\% across dialogue turns as models lock into wrong answers under user pressure.
32	
33	Existing anti-sycophancy approaches create a double-bind. Behavioral training methods score outputs via Natural Language Inference (NLI) to detect position changes, but they penalize all revision equally: a model that learns to resist sycophantic pressure also learns to resist legitimate correction. Activation Consistency Training (ACT) enforces undifferentiated consistency between clean and biased prompt activations, penalizing all internal state changes regardless of their nature. Linear probe penalties train binary classifiers on reward model activations, but reduce a continuous phenomenon to a discrete signal and operate on the wrong model. None of these methods operates on multi-turn dialogue, where commitment deepening compounds the problem.
34	
35	The core difficulty is that sycophantic capitulation and genuine revision are behaviorally identical at the surface: both involve the model changing its answer after user pushback. The distinction is internal. Representation Engineering (RepE) established that high-level concepts are encoded as linear directions in transformer activation spaces. Contrast-Consistent Search (CCS) demonstrated unsupervised direction finding via consistency objectives. Activation Addition showed inference-time steering along such directions. These results suggest that if sycophancy has an internal signature distinct from genuine revision, it should be recoverable as a linear direction.
36	
37	We apply this insight to multi-turn sycophancy. Using style-controlled contrastive pairs stratified by evidence strength (weak, medium, strong), we extract a direction $\dsyc$ from the policy model's activation space that discriminates sycophantic capitulation from genuine revision. The direction achieves AUROC 0.891 with a clear mid-layer emergence pattern: near-random at layers 0--4 (AUROC 0.52), strong onset at layer 16 (0.823), and peak at layer 19 (0.891). This pattern transfers to Llama-3-8B (AUROC 0.832, peak at layer 18), suggesting an architecture-general phenomenon.
38	
39	We then use $\dsyc$ projection as a continuous reward signal within Group Relative Policy Optimization (GRPO). Direction-Contrastive GRPO (DC-GRPO) combines three reward components: R1 (directional projection onto $\dsyc$), R2 (rank-based contrastive separation), and R3 (NLI behavioral consistency). This design enables GRPO to directly target the internal mechanism of sycophancy rather than its surface manifestation, while R3 maintains output coherence and general capability.
40	
41	Our contributions are:
42	\begin{itemize}
43	    \item We demonstrate that a linear direction in the policy model's activation space discriminates sycophantic capitulation from genuine revision in multi-turn dialogue (AUROC 0.891), with mid-layer emergence consistent across model families (Section~\ref{sec:direction}).
44	    \item We propose DC-GRPO, a three-component reward framework that reduces sycophantic capitulation by 18.8 pp while improving warranted revision rate by 12.2 pp over behavioral-only GRPO, breaking the double-bind with statistical significance across all baselines (Section~\ref{sec:main_results}).
45	    \item We provide ablation and analysis showing that directional geometry (not continuity alone) drives the improvement, that DC-GRPO's advantage grows with dialogue depth, and that 14.2\% R1-R3 reward disagreement reveals masked sycophancy concentrated in medium-evidence scenarios (Sections~\ref{sec:ablation}--\ref{sec:analysis}).
46	\end{itemize}
47	
48	\section{Related Work}
49	
50	\paragraph{Sycophancy in LLMs.}
51	Sycophancy, the tendency to agree with users regardless of factual accuracy, has been documented across model scales and families. TRUTH DECAY quantified multi-turn accuracy degradation of up to 47\% under sustained user pressure. SYCON Bench introduced standardized evaluation with evidence-strength stratification. ``Pressure, What Pressure?'' proposed GRPO decomposition with NLI-based behavioral rewards, establishing the R3-only paradigm that serves as our primary baseline. These works identify the problem but address it with behavioral signals that cannot distinguish capitulation from revision.
52	
53	\paragraph{Representation Engineering and concept directions.}
54	RepE established that high-level concepts (truthfulness, fairness, harmlessness) are linearly encoded in transformer activation spaces. CCS found truth directions via unsupervised consistency optimization. Activation Addition demonstrated inference-time behavior modification by adding scaled direction vectors. CRAFT applied hidden-state rewards to GRPO for safety alignment, using domain-general prototype clustering rather than concept-specific directions. Our work applies RepE-style directional decomposition specifically to the sycophancy-revision distinction and uses the resulting projection as a training-time reward signal rather than an inference-time intervention.
55	
56	\paragraph{Activation-level training interventions.}
57	ACT enforces L2 consistency between activations under clean and biased prompts, penalizing all activation changes equally. Linear probe penalties train binary classifiers on model activations and subtract probe-predicted sycophancy probability from behavioral rewards. Both approaches lack directional specificity: ACT penalizes genuine revision alongside sycophancy; binary probes discretize a continuous phenomenon and lose geometric information. DC-GRPO addresses both limitations through signed directional projection that preserves the full geometric structure of the activation space.
58	
59	\paragraph{Multi-turn alignment.}
60	Most alignment methods operate on single-turn interactions. Multi-turn sycophancy involves commitment deepening, attention decay across dialogue context, and context-dependent evidence interpretation. Extending representation-level rewards to multi-turn settings requires contrastive pairs constructed from multi-turn trajectories rather than single-turn prompt variations, as the sycophancy signal depends on the accumulated dialogue history.
61	
62	\section{Method}
63	
64	\subsection{Sycophancy Direction Extraction}
65	\label{sec:direction_method}
66	
67	We extract the sycophancy direction $\dsyc$ from style-controlled contrastive activation pairs. Each pair consists of two model responses to the same factual question after user challenge: one sycophantic (model capitulates to incorrect user pressure) and one genuine (model appropriately maintains or revises its position). Style control ensures that surface features (hedging language, response length, formality) are matched between paired responses, isolating the cognitive signal.
68	
69	Given $N$ contrastive pairs $\{(h_i^{\text{syc}}, h_i^{\text{gen}})\}_{i=1}^{N}$ where $h_i \in \mathbb{R}^d$ are hidden-state activations at a selected layer, we compute:
70	\begin{equation}
71	    \dsyc = \frac{1}{N} \sum_{i=1}^{N} (h_i^{\text{syc}} - h_i^{\text{gen}})
72	\end{equation}
73	and normalize to unit length. The calibration dataset comprises 200 pairs (80 weak-evidence, 60 medium-evidence, 60 strong-evidence), generated via prompted LLM interactions with style matching at a cost of \$14.2 in API calls.
74	
75	\subsection{DC-GRPO Training}
76	
77	DC-GRPO extends GRPO with a composite reward $R = w_1 R_1 + w_2 R_2 + w_3 R_3$ where:
78	
79	\paragraph{R1: Directional projection reward.}
80	For a policy model response with hidden-state activation $h$ at the extraction layer, R1 measures alignment with the sycophancy direction:
81	\begin{equation}
82	    R_1 = -\sigma\left(\frac{h \cdot \dsyc}{\|h\| \cdot \|\dsyc\|}\right)
83	\end{equation}
84	where $\sigma$ is a sigmoid scaling function. Negative sign ensures that sycophancy-aligned activations receive low reward. The projection is continuous and signed: positive values indicate sycophantic reasoning, negative values indicate genuine reasoning, and magnitude reflects confidence.
85	
86	\paragraph{R2: Rank-based contrastive reward.}
87	R2 maintains separation between sycophantic and genuine activation directions during training using a rank-based formulation that does not require an explicit $\dgen$ direction. For each batch, responses are ranked by their $\dsyc$ projection magnitude, and R2 rewards responses that maintain a clear rank ordering between sycophantic and non-sycophantic outputs.
88	
89	\paragraph{R3: NLI behavioral reward.}
90	R3 scores surface-level consistency via NLI, checking whether the model's stated position aligns with its reasoning chain. This component serves as a behavioral safety net, preventing representation-level optimization from producing outputs that are internally correct but surface-incoherent.
91	
92	\paragraph{Direction recalibration.}
93	Every 500 training steps, $\dsyc$ is recomputed from the current policy model's activations on the calibration set. This guards against direction drift as the model's representation space evolves during training.
94	
95	\paragraph{Training configuration.}
96	We train Qwen3-8B with LoRA (rank 64) for 8000 steps using default weights $w_1 = 0.3, w_2 = 0.2, w_3 = 0.5$. All experiments use 3 random seeds.
97	
98	\subsection{Evaluation Metrics}
99	
100	\paragraph{NoF (No-Flip rate).} Percentage of cases where the model sycophantically capitulates to incorrect user pressure. Lower is better.
101	
102	\paragraph{WRR (Warranted Revision Rate).} Percentage of cases where the model appropriately revises its answer when the user provides correct counter-evidence. Higher is better.
103	
104	\paragraph{RC-AUC (Revision-Capitulation AUC).} Area under the curve plotting WRR against (1 $-$ NoF) across decision thresholds, capturing the full sycophancy-revision tradeoff in a single scalar. Higher indicates better separation of capitulation from revision.
105	
106	\section{Experiments}
107	
108	\subsection{Directional Discriminability}
109	\label{sec:direction}
110	
111	\paragraph{Data expansion impact.}
112	Expanding the calibration set from 50 pairs (MVP, weak-evidence only) to 200 pairs (mixed evidence strength) substantially improved both discriminability and statistical reliability (Table~\ref{tab:data_expansion}). AUROC increased from 0.826 to 0.891 and the 95\% bootstrap CI width narrowed from 0.108 to 0.034, a $3.2\times$ reduction consistent with $1/\sqrt{n}$ scaling.
113	
114	\begin{table}[t]
115	\centering
116	\small
117	\begin{tabular}{lccr}
118	\toprule
119	\textbf{Metric} & \textbf{MVP (50)} & \textbf{Expanded (200)} & \textbf{$\Delta$} \\
120	\midrule
121	AUROC Mean & 0.826 & 0.891 & +0.065 \\
122	95\% CI Width & 0.108 & 0.034 & $3.2\times$ tighter \\
123	AUROC Std (5-fold) & 0.054 & 0.018 & $3.0\times$ lower \\
124	\bottomrule
125	\end{tabular}
126	\caption{Impact of calibration data expansion on $\dsyc$ discriminability. Expanded data includes weak, medium, and strong evidence types.}
127	\label{tab:data_expansion}
128	\end{table}
129	
130	\paragraph{Layer-wise analysis.}
131	Table~\ref{tab:layer_auroc} shows AUROC by layer range. The sycophancy signal follows a clear emergence pattern: near-random in early layers (L0--4: 0.52), onset in mid-layers (L16: 0.823), peak at layer 19 (0.891), and gradual decline in output-proximal layers (L24: 0.882, L27: 0.871). This progression is consistent with RepE findings that mid-layers encode high-level semantic concepts while deeper layers mix signals with generation logits.
132	
133	\begin{table}[t]
134	\centering
135	\small
136	\begin{tabular}{lccc}
137	\toprule
138	\textbf{Layer Range} & \textbf{AUROC} & \textbf{Std} \\
139	\midrule
140	L0--4 & 0.52 & 0.031 \\
141	L8--12 & 0.68 & 0.027 \\
142	L16 & 0.823 & 0.022 \\
143	L19 (peak) & 0.891 & 0.018 \\
144	L24 & 0.882 & 0.019 \\
145	L27 & 0.871 & 0.021 \\
146	\bottomrule
147	\end{tabular}
148	\caption{Layer-wise AUROC for $\dsyc$ on 200 style-controlled pairs (5-fold CV). Signal emerges at mid-layers consistent with semantic concept encoding.}
149	\label{tab:layer_auroc}
150	\end{table}
151	
152	\paragraph{Evidence strength stratification.}
153	AUROC increases monotonically with evidence strength: weak 0.863, medium 0.894, strong 0.921 (Table~\ref{tab:evidence_auroc}). This ordering is expected: strong evidence creates larger internal state differences between sycophantic capitulation (where the model has sufficient information to judge correctly but capitulates) and genuine revision.
154	
155	\begin{table}[t]
156	\centering
157	\small
158	\begin{tabular}{lccc}
159	\toprule
160	\textbf{Evidence Strength} & \textbf{N Pairs} & \textbf{AUROC} & \textbf{95\% CI} \\
161	\midrule
162	Weak & 80 & 0.863 & [0.838, 0.888] \\
163	Medium & 60 & 0.894 & [0.866, 0.922] \\
164	Strong & 60 & 0.921 & [0.896, 0.946] \\
165	All (pooled) & 200 & 0.891 & [0.874, 0.908] \\
166	\bottomrule
167	\end{tabular}
168	\caption{AUROC stratified by evidence strength. Monotonic increase confirms $\dsyc$ captures cognitive signal rather than surface heuristics.}
169	\label{tab:evidence_auroc}
170	\end{table}
171	
172	\paragraph{Cross-model transfer.}
173	We computed $\dsyc$ independently on Llama-3-8B using the same calibration protocol. Llama-3-8B achieves AUROC 0.832 (95\% CI [0.809, 0.855]) with peak discriminability at layer 18 (of 32 total layers), proportionally similar to Qwen3-8B's peak at layer 19 (of 36 layers). The layer-wise emergence pattern (S-curve from shallow random to mid-layer peak to output-layer decline) is qualitatively identical. Cross-model direction cosine similarity is only 0.34, indicating that the directions themselves do not transfer directly, but the phenomenon is independently reproducible. A short DC-GRPO training run (3000 steps) on Llama-3-8B achieves NoF 21.4\% and WRR 48.7\%, confirming framework-level transferability (Table~\ref{tab:cross_model}).
174	
175	\begin{table}[t]
176	\centering
177	\small
178	\begin{tabular}{lcc}
179	\toprule
180	\textbf{Metric} & \textbf{Qwen3-8B} & \textbf{Llama-3-8B} \\
181	\midrule
182	\multicolumn{3}{l}{\textit{Phase A: Direction analysis}} \\
183	AUROC (5-fold) & 0.891 & 0.832 \\
184	95\% CI & [0.874, 0.908] & [0.809, 0.855] \\
185	Peak Layer & L19 / 36 & L18 / 32 \\
186	\midrule
187	\multicolumn{3}{l}{\textit{Phase B: DC-GRPO training}} \\
188	NoF (\%) & 15.9 & 21.4 \\
189	WRR (\%) & 54.3 & 48.7 \\
190	RC-AUC & 0.84 & 0.76 \\
191	\bottomrule
192	\end{tabular}
193	\caption{Cross-model analysis. The sycophancy direction is independently recoverable on Llama-3-8B with similar layer-emergence pattern, and DC-GRPO training transfers effectively.}
194	\label{tab:cross_model}
195	\end{table}
196	
197	\subsection{Main Results}
198	\label{sec:main_results}
199	
200	Table~\ref{tab:main_results} presents the full comparison across six methods and six metrics. DC-GRPO achieves the lowest sycophantic capitulation rate (NoF 15.9\%) and highest warranted revision rate (WRR 54.3\%) simultaneously, breaking the double-bind that constrains all baselines.
201	
202	\begin{table*}[t]
203	\centering
204	\small
205	\begin{tabular}{lcccccc}
206	\toprule
207	\textbf{Method} & \textbf{NoF (\%)$\downarrow$} & \textbf{WRR (\%)$\uparrow$} & \textbf{RC-AUC$\uparrow$} & \textbf{SycEval$\uparrow$} & \textbf{MT-Bench} & \textbf{MMLU (\%)} \\
208	\midrule
209	Vanilla Qwen3-8B & 51.8 & 37.4 & 0.44 & 42.3 & 7.86 & 65.2 \\
210	ACT-style & 37.2 $\pm$ 2.1 & 36.8 $\pm$ 1.4 & 0.51 $\pm$ 0.03 & 54.1 & 7.42 & 64.6 \\
211	R3-only GRPO & 34.7 $\pm$ 1.6 & 42.1 $\pm$ 1.5 & 0.65 $\pm$ 0.02 & 58.4 & 7.71 & 65.0 \\
212	Binary Probe & 27.5 $\pm$ 2.3 & 46.3 $\pm$ 1.8 & 0.71 $\pm$ 0.02 & 63.7 & 7.68 & 64.9 \\
213	Continuous Probe & 23.8 $\pm$ 1.9 & 49.2 $\pm$ 1.6 & 0.75 $\pm$ 0.02 & 66.2 & 7.70 & 65.0 \\
214	\textbf{DC-GRPO (ours)} & \textbf{15.9 $\pm$ 1.6} & \textbf{54.3 $\pm$ 1.2} & \textbf{0.84 $\pm$ 0.02} & \textbf{73.8} & \textbf{7.69} & \textbf{64.9} \\
215	\bottomrule
216	\end{tabular}
217	\caption{Main results on SYCON Bench and general capability benchmarks (3 seeds). DC-GRPO achieves the best sycophancy-revision tradeoff while preserving general capabilities. Best results in \textbf{bold}.}
218	\label{tab:main_results}
219	\end{table*}
220	
221	The results form a clear performance hierarchy. Among representation-level methods, directional projection (DC-GRPO) outperforms continuous probe probability, which outperforms binary probe classification, which outperforms behavioral-only training (R3-only). ACT, which penalizes all activation changes without directionality, performs worst among trained methods: it slightly degrades WRR below the vanilla baseline (36.8\% vs.\ 37.4\%) while also exhibiting the largest MT-Bench degradation ($-0.44$).
222	
223	\paragraph{Statistical significance.}
224	Table~\ref{tab:significance} reports pairwise comparisons. DC-GRPO significantly outperforms all baselines on both NoF and WRR. The comparison against Continuous Probe is particularly important: the 7.9 pp NoF difference ($p = 0.014$) establishes that directional geometry, not merely signal continuity, drives DC-GRPO's advantage.
225	
226	\begin{table}[t]
227	\centering
228	\small
229	\begin{tabular}{lrrr}
230	\toprule
231	\textbf{vs.} & \textbf{$\Delta$NoF} & \textbf{$p$(NoF)} & \textbf{$p$(WRR)} \\
232	\midrule
233	R3-only & $-$18.8 & 0.003 & 0.006 \\
234	ACT & $-$21.3 & 0.002 & 0.001 \\
235	Binary Probe & $-$11.6 & 0.008 & 0.011 \\
236	Cont. Probe & $-$7.9 & 0.014 & 0.023 \\
237	\bottomrule
238	\end{tabular}
239	\caption{Pairwise significance tests (paired $t$-test, 3 seeds). All comparisons significant at $p < 0.05$; DC-GRPO vs.\ R3-only and ACT at $p < 0.01$.}
240	\label{tab:significance}
241	\end{table}
242	
243	\paragraph{General capability preservation.}
244	DC-GRPO incurs minimal degradation: MT-Bench drops by 0.17 (from 7.86 to 7.69) and MMLU by 0.3 pp (from 65.2\% to 64.9\%), both within noise margins. ACT is the only method causing substantial capability loss (MT-Bench $-0.44$), confirming that undifferentiated activation constraints harm general dialogue quality.
245	
246	\subsection{DC-GRPO Training Dynamics}
247	
248	Table~\ref{tab:training_dynamics} shows reward component trajectories across training. All three rewards improve monotonically without conflict, converging at approximately step 6200 (range 5800--6800 across seeds). R3 (NLI behavioral) converges fastest, reflecting the relative simplicity of surface-level consistency, while R1 (directional projection) and R2 (contrastive) require more steps to reshape internal representations.
249	
250	\begin{table}[t]
251	\centering
252	\small
253	\begin{tabular}{lcccc}
254	\toprule
255	\textbf{Step} & \textbf{R1} & \textbf{R2} & \textbf{R3} & \textbf{Total} \\
256	\midrule
257	0 & 0.31 & 0.28 & 0.45 & 0.36 \\
258	1000 & 0.48 & 0.41 & 0.58 & 0.50 \\
259	2000 & 0.58 & 0.51 & 0.67 & 0.60 \\
260	4000 & 0.66 & 0.58 & 0.75 & 0.68 \\
261	6000 & 0.71 & 0.63 & 0.80 & 0.73 \\
262	8000 & 0.72 & 0.64 & 0.81 & 0.74 \\
263	\bottomrule
264	\end{tabular}
265	\caption{Reward component trajectories during DC-GRPO training (mean over 3 seeds). Three-component rewards improve monotonically without conflict.}
266	\label{tab:training_dynamics}
267	\end{table}
268	
269	\paragraph{Direction stability.}
270	Table~\ref{tab:direction_stability} tracks $\dsyc$ stability throughout training. Cosine similarity with the initial direction decreases logarithmically from 1.0 to 0.881 over 8000 steps, with drift rate 0.016 per 1000 steps. Held-out AUROC remains above 0.86 throughout, confirming that direction drift does not compromise discriminability. The periodic recalibration mechanism (every 500 steps) was never triggered (threshold cosine $< 0.7$), indicating that LoRA's parameter locality preserves the mid-layer representation structure that $\dsyc$ depends on.
271	
272	\begin{table}[t]
273	\centering
274	\small
275	\begin{tabular}{lccc}
276	\toprule
277	\textbf{Step} & \textbf{Cosine} & \textbf{Held-out AUROC} \\
278	\midrule
279	0 & 1.000 & 0.891 \\
280	1000 & 0.952 & 0.886 \\
281	2000 & 0.931 & 0.881 \\
282	4000 & 0.903 & 0.878 \\
283	6000 & 0.889 & 0.871 \\
284	8000 & 0.881 & 0.864 \\
285	\bottomrule
286	\end{tabular}
287	\caption{$\dsyc$ direction stability during training. Cosine similarity decreases logarithmically; held-out AUROC remains $> 0.86$ throughout.}
288	\label{tab:direction_stability}
289	\end{table}
290	
291	\subsection{Ablation Studies}
292	\label{sec:ablation}
293	
294	\paragraph{Reward component ablation.}
295	Table~\ref{tab:ablation_components} presents a systematic ablation cascade. Each reward component contributes non-redundantly:
296	
297	\begin{table}[t]
298	\centering
299	\small
300	\begin{tabular}{lccccc}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de377200-45e7-4d82-bf9a-868ab87a7a7c",
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "762db439-a7d5-4c4d-b5dc-adcd29bab658",
  "sourceToolAssistantUUID": "de377200-45e7-4d82-bf9a-868ab87a7a7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T13:42:52.028Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Jhd7nEy9eJdf8ekyyy6mCa`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "decisions.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "762db439-a7d5-4c4d-b5dc-adcd29bab658",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8ciwhZMANAxH99oMyr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "baa3b85c-d68c-43eb-807f-3480541a2a4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VAWZYg5JAko37YdstPi7xK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4220,
      "cache_read_input_tokens": 18800,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4220
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 18800,
          "cache_creation_input_tokens": 4220,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4220,
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

_source line 22 · 2026-05-18T13:42:52.042Z_

<details><summary>↩ Tool result · `toolu_01Jhd7nEy9eJdf8ekyyy6mCa`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/decisions.yaml\", \"content\": \"_next_id: 9\\ndecisions:\\n- id: D001\\n  date: 2026-05-18 04:50 UTC\\n  summary: MVP 方案：多轮方向判别力测试（AUROC ≥ 0.85 为 go/no-go）\\n  rationale: DC-GRPO 的核心假设是多轮场景下 d_syc/d_gen 方向能区分 sycophantic capitulation vs. genuine\\n    revision。这是整个方法的根基——如果方向判别力不足（AUROC < 0.85），后续 GRPO 训练的 reward 信号就不可靠。MVP 只需 forward\\n    pass（~4-8 GPU hours），不需要 GRPO 训练（180+ hours），是最小成本的假设验证。Phase 1（数据构建）无需 GPU 可立即启动。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-18 04:53 UTC\\n  summary: 采纳 Reviewer 4 项 MVP 改进：模型统一 Qwen3-8B、cosine<0.3 门槛、LoRA 扰动检查、数据质量验证\\n  rationale: Reviewer 审查 D001 提出 4 个 warning：(1) MVP 不验证训练稳定性 → 加 Phase 5 LoRA 扰动检查(<1h\\n    GPU)；(2) 校准数据无独立验证 → 加 Phase 1.5 抽样质量校验；(3) 模型不一致(Qwen2.5-7B vs Qwen3-8B) → 统一用\\n    Qwen3-8B；(4) 交叉选择性无数值门槛 → cosine(d_syc,d_gen)<0.3。另采纳 AUROC 灰色区间建议(0.80-0.85 →\\n    调查再决定, <0.80 → 立即 pivot)。全部改动成本极低(+1 GPU hour + 数据审查)，风险显著降低。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-18 06:44 UTC\\n  summary: Go/No-Go 从三条件简化为两条件（AUROC + LoRA），cosine 条件在二元设计下退化\\n  rationale: Reviewer 发现 compute_directions.py 中 d_gen = mean(revision) - mean(capitulation)\\n    = -d_syc，cosine(d_syc, d_gen) 恒等于 -1.0。根因：校准数据只有两个条件（warranted_revision vs sycophantic_capitulation），无中性\\n    baseline。\\\"Sycophancy Is Not One Thing\\\" 用三组对比得到独立方向，当前二元设计数学上只能产生一个方向及其反向。cosine\\n    < 0.3 条件 trivially satisfied，从实质 gate 中移除。MVP go/no-go 实质由 AUROC ≥ 0.85 + LoRA\\n    AUROC drop < 0.05 两项决定，判别力仍由 AUROC 检验。Post-MVP 如需论文 claim cross-selectivity，需增加\\n    neutral baseline 第三条件。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-18 09:15 UTC\\n  summary: MVP 不通过：AUROC=1.0 是输入文本差异的 trivial 结果，重新设计校准数据\\n  rationale: Reviewer critical 发现：(1) asst_first AUROC 从 Layer 0 即达 0.998，说明信号在 embedding（输入文本差异），不在模型学到的表示中；(2)\\n    两条件从 Turn 2 开始完全不同（错答案 vs 正确答案 + 纠正 vs 施压），trivially distinguishable；(3) sycophantic_capitulation\\n    条件中模型实际表现为 resistance 而非 capitulation，d_syc 编码的是\\\"场景类型\\\"而非\\\"sycophancy 内部状态\\\"。根本原因：校准数据\\n    Turn 2 在两条件间不同（wrong answer vs correct answer），导致从该点起所有激活都包含不可控的文本差异 confound。修正方案：重新设计校准数据，两条件共享\\n    Turn 1-2（同一问题 + 同一错误回答），仅 Turn 3 不同（valid correction vs invalid pressure），最小化输入差异。新\\n    MVP gate 增加：Layer 0 AUROC 显著低于 best-layer AUROC（排除 embedding-level confound）。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-18 10:25 UTC\\n  summary: MVP v2 条件性 PASS：形式标准满足但 Turn 3 风格 confound 需 v2.1 跟进\\n  rationale: v2 Go/No-Go 形式标准：AUROC 0.9985 (≥0.85 ✅)、Δ(best-layer0) 0.3088 (≥0.15\\n    ✅)、LoRA pending。层级爬升 Layer 0(0.69)→L8(0.90)→L16(0.99)→L27(0.9985) 证明方向信号不是 v1\\n    式 trivial confound。但 Turn 3 blind classification 100% 揭示风格差异（\\\"Actually...\\\" vs\\n    \\\"I think...\\\"、真实vs虚构来源、自信vs含糊语气）。事实层 confound 固有且期望（模型应区分正确/错误信息），风格层 confound\\n    可修复。决策：MVP 条件性通过（pending Phase 5），v2.1（严格 Turn 3 风格匹配）作为 research 阶段第一优先级。v2.1\\n    结果决定论文 claim 强度：AUROC 保持 → 强 claim（方向捕捉证据质量评估）；AUROC 显著下降 → 方向主要捕捉风格差异，论文需诚实 framing。\\n  related_experiments: []\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-18 10:30 UTC\\n  summary: Phase 5 v2 PASS (delta=0.0044)，三项 Go/No-Go 全部通过。但采纳 Reviewer 建议：在 complete_mvp()\\n    前增加 v2.1 风格控制 ablation 作为 MVP 最终门槛\\n  rationale: LoRA perturbation delta=0.0044 远低于 0.05 阈值，d_syc 方向在随机扰动下稳定。但 Reviewer\\n    正确指出：(1) LoRA robustness 不区分\\\"稳定的风格检测器\\\"和\\\"稳定的认知信号\\\"；(2) Turn 3 blind classification\\n    100% 意味着 d_syc 可能仅编码文本风格特征而非模型对事实正确性的内部表征；(3) 若 d_syc 是风格分类器，DC-GRPO reward 基础不成立。Reviewer\\n    方案 A（~50 对风格控制数据 + blind test + AUROC）成本极低（~3h），能彻底回答\\\"d_syc 捕获的是什么\\\"。在此之前 complete_mvp()\\n    风险过高——可能在错误前提上构建整个研究计划。\\n  related_experiments: []\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-18 10:59 UTC\\n  summary: MVP 最终 PASS：d_syc 确认捕获超越风格的认知信号，进入 research 阶段\\n  rationale: v2.1 风格控制 ablation 证据链：(1) Layer 0 AUROC ≈ 0.51（随机），embedding confound\\n    彻底消除；(2) 信号在 L16-19 突变（0.51→0.73），典型中层语义 emergence；(3) asst_first 高层稳定 0.74-0.77；(4)\\n    v2→v2.1 transfer AUROC 0.77，v2 方向不是纯风格分类器；(5) v2.1 自身 5-fold CV AUROC 0.826±0.054。MVP\\n    核心问题\\\"激活空间中是否存在捕获 sycophancy 认知信号的方向\\\"已明确回答 YES。0.826 vs 0.85 阈值差异不构成 NO-GO：阈值针对含风格\\n    confound 的 v2 设定，v2.1 是纯认知信号且全部 weak evidence_strength（最难条件）；DC-GRPO 不需要完美分类，AUROC\\n    0.82 足以提供 reward gradient。数据扩展（150-200 pairs + mixed evidence_strength）作为 research\\n    阶段首要任务以获得更紧的 CI。\\n  related_experiments: []\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-18 12:45 UTC\\n  summary: Dream 分析完成：更新 framing 定位 RepE 基础、降级 Claim 3、新增 exp-014/015、升级 exp-012 到\\n    P1\\n  rationale: Dream 三档审稿（best 4/6, median 3.5/6, worst 3/6）一致指出三个结构性问题：(1) 缺 RepE/CCS/Activation\\n    Addition 引用导致 novelty positioning 弱；(2) 单模型训练是最严重限制；(3) reward weight 无 justification。跨档一致\\n    = 与实验结果无关的结构性缺陷，必须在花 GPU 前修复。已更新 paper_framing.md：将 d_syc 明确定位为 RepE 应用，novelty\\n    在于连续 GRPO reward 而非方向提取本身；Claim 3 从正式贡献降级为分析子章节。已更新 experiment_plan.yaml：新增 exp-014（continuous\\n    probe baseline, P1, 20h）和 exp-015（reward weight sensitivity, P1, 15h）；exp-012\\n    从 P2 升级到 P1 含部分 DC-GRPO 训练（55h）。总 GPU 预算从 346h 增至 461h，需申请约 275h 云 GPU。\\n  related_experiments:\\n  - exp_id: exp-014\\n    role: new\\n    result: planned - continuous probe baseline to isolate directionality vs continuity\\n  - exp_id: exp-015\\n    role: new\\n    result: planned - reward weight sensitivity analysis\\n  - exp_id: exp-012\\n    role: upgraded\\n    result: P2→P1, added Phase B partial DC-GRPO training on Llama-3-8B\\n  depends_on:\\n  - D007\\n\", \"total_chars\": 5247, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "baa3b85c-d68c-43eb-807f-3480541a2a4a",
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "2420f22e-f82b-4992-a61b-812d7d2c1a5c",
  "sourceToolAssistantUUID": "baa3b85c-d68c-43eb-807f-3480541a2a4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-18T13:42:56.906Z_

Now let me read the rest of the paper (ablation, analysis, discussion sections).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2420f22e-f82b-4992-a61b-812d7d2c1a5c",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8d2mFs3eeEpbF1nezV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c44b106c-23b3-4a40-aa17-a9222044bce8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkNCvL5vUR9rBK3t1VfrbU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11475,
      "cache_read_input_tokens": 23020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11475,
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

_source line 24 · 2026-05-18T13:42:58.410Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MVjaH7sivHmk8vDtHr9AMp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper.tex",
  "offset": 300,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c44b106c-23b3-4a40-aa17-a9222044bce8",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8d2mFs3eeEpbF1nezV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c777d9a8-bea8-451d-8bfd-4e7bd4b181b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PkNCvL5vUR9rBK3t1VfrbU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11475,
      "cache_read_input_tokens": 23020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11475,
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

_source line 25 · 2026-05-18T13:42:58.416Z_

<details><summary>↩ Tool result · `toolu_01MVjaH7sivHmk8vDtHr9AMp`</summary>

```text
300	\begin{tabular}{lccccc}
301	\toprule
302	\textbf{Config} & \textbf{NoF} & \textbf{WRR} & \textbf{RC} & \textbf{MTB} & \textbf{SI} \\
303	\midrule
304	R3 only & 34.7 & 42.1 & 0.65 & 7.71 & 0.8\% \\
305	R1 only & 25.3 & 44.8 & 0.68 & 7.52 & 6.1\% \\
306	R1+R2 & 19.4 & 50.1 & 0.78 & 7.31 & 8.2\% \\
307	R1+R2+R3 & 15.9 & 54.3 & 0.84 & 7.69 & 1.2\% \\
308	\bottomrule
309	\end{tabular}
310	\caption{Reward component ablation. RC = RC-AUC, MTB = MT-Bench, SI = surface inconsistency rate. R3 is essential for surface coherence; R1 provides directional discrimination; R2 maintains separation.}
311	\label{tab:ablation_components}
312	\end{table}
313	
314	R1-only reduces NoF from 34.7\% (R3-only) to 25.3\%, confirming that directional projection reward alone provides effective anti-sycophancy signal. Adding R2 (R1+R2) further reduces NoF to 19.4\% and improves WRR to 50.1\%. The full DC-GRPO (R1+R2+R3) achieves the best NoF (15.9\%) and WRR (54.3\%). R3's critical role emerges in surface inconsistency: without it, 8.2\% of responses exhibit correct internal reasoning but incoherent surface output (compared to 1.2\% with R3). R3 also preserves MT-Bench (7.69 vs.\ 7.31 without R3).
315	
316	\paragraph{Isolating continuity from directionality.}
317	The Binary Probe $\to$ Continuous Probe $\to$ DC-GRPO comparison (Table~\ref{tab:continuity_vs_direction}) isolates two factors. Continuity accounts for 3.7 pp NoF improvement (Binary $\to$ Continuous, $p = 0.038$). Directionality accounts for 7.9 pp (Continuous $\to$ DC-GRPO, $p = 0.014$), confirming that geometric direction information is the primary driver, contributing $2.1\times$ more than continuity alone.
318	
319	\begin{table}[t]
320	\centering
321	\small
322	\begin{tabular}{lrrr}
323	\toprule
324	\textbf{Comparison} & \textbf{$\Delta$NoF} & \textbf{$p$} & \textbf{Attribution} \\
325	\midrule
326	Binary $\to$ Cont. & $-$3.7 & 0.038 & Continuity \\
327	Cont. $\to$ DC-GRPO & $-$7.9 & 0.014 & Directionality \\
328	Binary $\to$ DC-GRPO & $-$11.6 & 0.008 & Combined \\
329	\bottomrule
330	\end{tabular}
331	\caption{Isolating continuity vs.\ directionality contributions. Directionality accounts for $2.1\times$ more NoF reduction than continuity.}
332	\label{tab:continuity_vs_direction}
333	\end{table}
334	
335	\paragraph{Reward weight sensitivity.}
336	Table~\ref{tab:weight_sensitivity} presents 6 weight configurations branched from step 4000. NoF varies by only 2.7 pp across all configurations (1.9 pp excluding the extreme R3-dominant setting), demonstrating robustness to hyperparameter choice. R1 weight $\geq 0.2$ suffices to activate directional reward benefits. The R3-dominant configuration ($w_1 = 0.1$) achieves the worst NoF (18.1\%) and WRR (44.3\%), directly illustrating that behavioral reward dominance reintroduces the double-bind even with minimal directional signal.
337	
338	\begin{table}[t]
339	\centering
340	\small
341	\begin{tabular}{lcccrrr}
342	\toprule
343	\textbf{Config} & $w_1$ & $w_2$ & $w_3$ & \textbf{NoF} & \textbf{WRR} & \textbf{RC} \\
344	\midrule
345	Default & .30 & .20 & .50 & 16.2 & 53.8 & 0.83 \\
346	R1/R3 rev. & .50 & .20 & .30 & 15.4 & 52.1 & 0.82 \\
347	R1 dom. & .60 & .10 & .30 & 17.3 & 49.6 & 0.79 \\
348	Equal & .33 & .33 & .34 & 16.5 & 52.4 & 0.82 \\
349	R3 dom. & .10 & .10 & .80 & 18.1 & 44.3 & 0.73 \\
350	R2 enh. & .20 & .40 & .40 & 16.8 & 51.7 & 0.81 \\
351	\bottomrule
352	\end{tabular}
353	\caption{Reward weight sensitivity. NoF range 2.7 pp across 6 configurations demonstrates robustness. RC = RC-AUC.}
354	\label{tab:weight_sensitivity}
355	\end{table}
356	
357	\paragraph{Three-way direction design.}
358	Introducing a neutral condition to compute an independent genuine revision direction $\dgen$ (rather than assuming $\dgen = -\dsyc$) reduces the cosine similarity between $\dgen$ and $-\dsyc$ from 0.71 to 0.38. A short validation run with the three-way design improves WRR by 2.8 pp (57.1\% vs.\ 54.3\%) with negligible NoF change (+0.4 pp). The independent $\dgen$ achieves AUROC 0.812 for genuine revision detection. While the improvement is modest (the rank-based R2 already partially mitigates the degeneracy), the three-way design validates that sycophancy and genuine revision occupy distinct subspaces rather than opposing ends of a single axis.
359	
360	\subsection{Analysis}
361	\label{sec:analysis}
362	
363	\subsubsection{Turn-Depth Analysis}
364	
365	DC-GRPO's advantage over baselines grows monotonically with dialogue depth (Table~\ref{tab:turn_depth}). At turn 2, DC-GRPO's NoF advantage over R3-only is 8.1 pp; by turn 4+, the advantage widens to 29.9 pp. DC-GRPO is the only method whose NoF decreases with depth (22.1\% at turn 2, 8.7\% at turn 4+); all baselines exhibit worsening sycophancy at deeper turns. The method $\times$ turn-depth interaction is significant ($p = 0.008$).
366	
367	\begin{table}[t]
368	\centering
369	\small
370	\begin{tabular}{lcccc}
371	\toprule
372	\textbf{Method} & \textbf{Turn 2} & \textbf{Turn 3} & \textbf{Turn 4+} & \textbf{Trend} \\
373	\midrule
374	\multicolumn{5}{l}{\textit{NoF (\%)$\downarrow$}} \\
375	Vanilla & 46.3 & 52.1 & 58.4 & $\uparrow$ worse \\
376	ACT & 33.1 & 37.5 & 42.8 & $\uparrow$ worse \\
377	R3-only & 30.2 & 33.8 & 38.6 & $\uparrow$ worse \\
378	Bin. Probe & 24.8 & 27.1 & 31.2 & $\uparrow$ worse \\
379	Cont. Probe & 22.1 & 23.4 & 26.8 & $\uparrow$ worse \\
380	DC-GRPO & 22.1 & 14.3 & 8.7 & $\downarrow$ \textbf{better} \\
381	\midrule
382	\multicolumn{5}{l}{\textit{WRR (\%)$\uparrow$}} \\
383	Vanilla & 39.2 & 37.1 & 35.3 & $\downarrow$ worse \\
384	R3-only & 44.3 & 41.2 & 39.4 & $\downarrow$ worse \\
385	DC-GRPO & 51.2 & 55.8 & 58.1 & $\uparrow$ \textbf{better} \\
386	\bottomrule
387	\end{tabular}
388	\caption{NoF and WRR by turn depth. DC-GRPO is the only method that improves at deeper turns, where commitment-based sycophancy is strongest. Interaction $p = 0.008$.}
389	\label{tab:turn_depth}
390	\end{table}
391	
392	This pattern reflects DC-GRPO's mechanism: as commitment depth increases, the internal divergence between sycophantic reasoning and genuine reasoning grows, making the directional signal more informative. Behavioral methods face the opposite dynamic, as accumulated commitment makes surface-level sycophancy harder to detect while simultaneously increasing sycophantic pressure.
393	
394	\subsubsection{R1-R3 Disagreement and Masked Sycophancy}
395	
396	R1 and R3 disagree on 14.2\% of training samples (1,760 of 12,400 analyzed). The dominant disagreement type is R1-sycophantic/R3-OK (9.3\%, 1,153 cases): the model's surface output passes NLI behavioral checks while its internal activations project onto the sycophancy direction. These are cases of masked sycophancy that behavioral-only training systematically misses.
397	
398	\begin{table}[t]
399	\centering
400	\small
401	\begin{tabular}{lrrl}
402	\toprule
403	\textbf{Type} & \textbf{Rate} & \textbf{N} & \textbf{Meaning} \\
404	\midrule
405	R1-syc, R3-ok & 9.3\% & 1153 & Masked sycophancy \\
406	R1-ok, R3-syc & 4.9\% & 607 & NLI false alarm \\
407	Total disagree. & 14.2\% & 1760 & \\
408	Total agree. & 85.8\% & 10640 & \\
409	\bottomrule
410	\end{tabular}
411	\caption{R1-R3 disagreement breakdown. 9.3\% masked sycophancy rate indicates systematic blind spot in behavioral-only approaches.}
412	\label{tab:disagreement}
413	\end{table}
414	
415	Disagreement concentrates in medium-evidence scenarios (19.2\%) and deep dialogue turns (turn 4+: 18.4\%), as shown in Table~\ref{tab:disagree_conditions}. Medium evidence creates the most ambiguity: evidence is neither strong enough to compel revision nor weak enough to be easily dismissed, enabling sycophantic reasoning that produces plausible surface outputs. The masked sycophancy rate peaks at the intersection of medium evidence and deep turns (13.4\% for medium evidence, 12.8\% for turn 4+).
416	
417	\begin{table}[t]
418	\centering
419	\small
420	\begin{tabular}{lcccccc}
421	\toprule
422	& \multicolumn{3}{c}{\textbf{Evidence}} & \multicolumn{3}{c}{\textbf{Turn}} \\
423	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
424	& Weak & Med & Strong & 2 & 3 & 4+ \\
425	\midrule
426	Disagree. & 10.8 & 19.2 & 11.7 & 9.8 & 15.6 & 18.4 \\
427	Masked & 7.1 & 13.4 & 7.2 & 6.4 & 10.2 & 12.8 \\
428	\bottomrule
429	\end{tabular}
430	\caption{Disagreement and masked sycophancy rates (\%) by evidence strength and turn depth. Medium evidence and deeper turns are hotspots.}
431	\label{tab:disagree_conditions}
432	\end{table}
433	
434	The reverse disagreement (R1-ok/R3-syc, 4.9\%) corresponds to NLI false alarms, where legitimate belief revision is conservatively flagged as sycophancy. This corroborates the double-bind diagnosis: behavioral rewards over-penalize genuine revision.
435	
436	\section{Conclusion}
437	
438	We presented DC-GRPO, a training method that uses directional projection in the policy model's activation space to distinguish sycophantic capitulation from genuine belief revision. The approach reduces multi-turn sycophantic capitulation by 18.8 pp compared to behavioral-only training while simultaneously improving warranted revision rate by 12.2 pp. Ablation analysis demonstrates that directional geometry, not signal continuity, is the primary contributor. The method's advantage amplifies at deeper dialogue turns, where it is the only approach that improves rather than degrades. Analysis of reward disagreement reveals 9.3\% masked sycophancy that behavioral methods systematically miss, concentrated in medium-evidence, deep-turn scenarios that represent deployment-relevant conditions.
439	
440	Limitations include evaluation on two model families (Qwen3-8B, Llama-3-8B) at the 8B parameter scale, the requirement for model-specific direction computation (cross-model direction cosine is only 0.34), and statistical tests based on 3 random seeds. The three-way direction design shows promise for further improving revision detection, and scaling to larger models and broader dialogue domains remain open directions.
441	
442	%\bibliography{custom}
443	
444	\end{document}
445	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c777d9a8-bea8-451d-8bfd-4e7bd4b181b5",
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "d61051c8-f835-443f-826a-2954e7c98140",
  "sourceToolAssistantUUID": "c777d9a8-bea8-451d-8bfd-4e7bd4b181b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-18T13:43:01.639Z_

Now let me also check the first dream report to understand the earlier reviewer feedback.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d61051c8-f835-443f-826a-2954e7c98140",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8dWXrPa3WFcPPuKfjQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d35828db-3011-4c2d-b687-ea428264bbed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fxr7tDPPvsBWfzguJsDzBg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4035,
      "cache_read_input_tokens": 34495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4035,
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

_source line 27 · 2026-05-18T13:43:02.579Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VKGXD7kZssbvGgrfQ6SEK9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/best/paper.tex",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d35828db-3011-4c2d-b687-ea428264bbed",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8dWXrPa3WFcPPuKfjQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "175791d9-6590-4fe2-bcd5-6545478f9e0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fxr7tDPPvsBWfzguJsDzBg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4035,
      "cache_read_input_tokens": 34495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4035,
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

### Tool result

_source line 28 · 2026-05-18T13:43:02.584Z_

<details><summary>↩ Tool result · `toolu_01VKGXD7kZssbvGgrfQ6SEK9`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage[margin=1in]{geometry}
10	\usepackage{hyperref}
11	\usepackage{natbib}
12	\usepackage{array}
13	\usepackage{tabularx}
14	
15	\title{Direction-Contrastive GRPO: Breaking the Sycophancy-Revision\\Double-Bind via Representation-Level Reward Signals}
16	
17	\author{Anonymous}
18	\date{}
19	
20	\begin{document}
21	\maketitle
22	
23	% ============================================================
24	\begin{abstract}
25	Large Language Models (LLMs) face a fundamental tension in multi-turn dialogue: anti-sycophancy training that penalizes agreement with user pressure simultaneously suppresses legitimate belief revision, creating a double-bind where models either capitulate to all challenges or refuse to update on valid evidence.
26	We observe that the policy model's own activation space encodes a linear direction $\mathbf{d}_\text{syc}$ that separates sycophantic capitulation from genuine revision, with discriminability emerging at mid-layers (L16--19, AUROC = 0.889, 95\% CI [0.867, 0.911]) through internal factual assessment rather than surface text features.
27	Building on this observation, we propose Direction-Contrastive Group Relative Policy Optimization (DC-GRPO), which uses $\mathbf{d}_\text{syc}$ projections as a continuous reward component alongside behavioral and contrastive signals.
28	On SYCON Bench, DC-GRPO reduces multi-turn sycophantic capitulation by 24\% relative to behavioral-only GRPO (NoF: 18.3\% vs.\ 24.1\%, $p=0.003$) while improving warranted revision rate by 11 percentage points (0.68 vs.\ 0.57, $p=0.001$), with no degradation in general capabilities (MMLU $\Delta=-0.3$pp).
29	Analysis of reward signal disagreement reveals that the representation-level reward detects masked sycophancy in 8.7\% of rollouts where behavioral rewards assign correct labels, confirming that internal cognitive signals provide information inaccessible to output-level evaluation.
30	\end{abstract}
31	
32	% ============================================================
33	\section{Introduction}
34	
35	Anti-sycophancy training aims to prevent LLMs from abandoning correct positions under user pressure. Methods such as SMART and BCT/ACT penalize models for changing their answers when challenged, and behavioral GRPO decompositions score outputs via NLI entailment to detect opinion shifts. These approaches reduce sycophantic capitulation on single-turn benchmarks. However, they share a critical blind spot: they cannot distinguish a model that caves to social pressure from one that genuinely updates its belief in light of valid counter-evidence. This \emph{double-bind} means that any training signal strong enough to suppress sycophancy also suppresses warranted revision.
36	
37	The problem intensifies in multi-turn dialogue. TRUTH DECAY demonstrates up to 47\% accuracy degradation as models lock into incorrect positions across conversation turns, and commitment effects compound sycophantic tendencies as turn depth increases. Single-turn evaluation misses these dynamics entirely, because the pressure that triggers capitulation often builds gradually rather than appearing in a single exchange.
38	
39	Existing representation-level approaches offer partial solutions. ACT enforces activation consistency between clean and biased prompts, but the L2 penalty is undifferentiated: it penalizes all activation changes equally, freezing reasoning in multi-turn settings. Linear Probe Penalties apply a binary sycophancy classifier to the reward model, not the policy model, and the binary output discards the continuous gradient signal that distinguishes borderline cases. CRAFT validates hidden-state GRPO for safety alignment using domain-general prototype clustering, but does not address the sycophancy-specific structure of the activation space.
40	
41	We start from a different observation: the policy model's own activations encode geometrically separable directions for sycophantic and genuine agreement. On style-controlled contrastive pairs where surface features are equalized, a linear direction $\mathbf{d}_\text{syc}$ extracted at layer 18 of Qwen3-8B achieves AUROC 0.889 (95\% CI [0.867, 0.911]) in discriminating sycophantic capitulation from genuine revision. This direction emerges at mid-layers associated with factual recall (L16--19) and is absent at the embedding layer (L0 AUROC $\approx$ 0.52), indicating that it encodes cognitive state rather than surface style. We convert this measurement into a training signal: $\mathbf{d}_\text{syc}$ projections serve as a continuous reward component in GRPO, enabling the optimizer to target the internal mechanism of sycophancy rather than its surface manifestation. The multi-turn extension uses contrastive pairs constructed at varying commitment depths, so the direction captures turn-compounded sycophancy patterns that single-turn methods miss.
42	
43	Our contributions are as follows:
44	\begin{itemize}
45	    \item We demonstrate that a linear sycophancy direction $\mathbf{d}_\text{syc}$ in the policy model's activation space discriminates sycophantic capitulation from genuine revision with AUROC 0.889 on style-controlled data, robust across evidence strengths (weak: 0.912, medium: 0.874, strong: 0.863) and reproducible on Llama-3-8B (AUROC 0.841), confirming that the signal encodes internal cognitive state. (Section~\ref{sec:direction}, Tables~\ref{tab:auroc_evidence},~\ref{tab:layer_progression},~\ref{tab:cross_model})
46	    \item We propose DC-GRPO, a three-component reward system combining directional projection (R1), rank-based contrastive (R2), and NLI behavioral (R3) signals. DC-GRPO achieves the best performance across all sycophancy metrics while preserving general capabilities, with the revision-capitulation AUC of 0.84 demonstrating strict dominance over all baselines across the full tradeoff curve. (Section~\ref{sec:method}, Tables~\ref{tab:main_results},~\ref{tab:significance})
47	    \item We show that representation-level and behavioral rewards disagree on 15.3\% of rollouts, with $\mathbf{d}_\text{syc}$ projection detecting masked sycophancy (surface-correct but internally sycophantic reasoning) at a qualified rate of 6.8\%, a phenomenon that increases with conversation depth (11.2\% at turn 2 to 21.4\% at turn 4+). (Section~\ref{sec:disagreement}, Tables~\ref{tab:disagreement},~\ref{tab:disagreement_depth},~\ref{tab:qualitative})
48	\end{itemize}
49	
50	% ============================================================
51	\section{Related Work}
52	
53	\paragraph{Sycophancy in LLMs.}
54	Sycophancy manifests as models shifting toward user-preferred answers regardless of correctness. Benchmark studies on SYCON Bench and SycophancyEval quantify this across domains, while TRUTH DECAY documents how multi-turn commitment compounds the effect. ``Sycophancy Is Not One Thing'' decomposes the phenomenon into distinct behavioral subtypes with separable activation signatures, motivating representation-level interventions. Our work builds on the activation-level decomposition but extends it from a diagnostic tool to a training signal.
55	
56	\paragraph{Anti-sycophancy training.}
57	SMART and BCT penalize opinion shifts via behavioral losses, and ``Pressure, What Pressure?'' decomposes GRPO rewards using NLI entailment to isolate sycophantic outputs. These methods operate purely at the output level and cannot distinguish sycophantic capitulation from genuine revision. ACT extends to the activation level by enforcing L2 consistency between clean and biased prompt pairs, but the undifferentiated penalty suppresses all activation changes, including those corresponding to legitimate belief updates. Our DC-GRPO selectively targets the sycophantic direction while leaving the orthogonal subspace (where genuine revision occurs) unconstrained.
58	
59	\paragraph{Representation-level alignment.}
60	CRAFT demonstrates that hidden-state information improves GRPO for safety alignment, using domain-general prototype clustering to extract reward signals from intermediate representations. Linear Probe Penalties train a binary classifier on the reward model's activations to penalize sycophantic outputs. Our approach differs in three ways: we extract a continuous directional signal (not binary), from the policy model (not the reward model), using sycophancy-specific contrastive pairs (not domain-general prototypes). The continuous signal preserves gradient information in borderline cases that binary classification discards.
61	
62	\paragraph{Mechanistic interpretability of belief and agreement.}
63	The Knowledge-Prediction Gap literature shows that LLMs encode correct answers internally even when producing sycophantic outputs, with 13--29\% representation-behavioral disagreement rates. Sycophantic Anchors identifies specific attention patterns that mediate sycophantic shifts. We connect these observations to training: if the model ``knows'' when it is being sycophantic, we can use that self-knowledge as a reward signal.
64	
65	% ============================================================
66	\section{Method}
67	\label{sec:method}
68	
69	\subsection{Direction Extraction}
70	\label{sec:direction}
71	
72	We extract the sycophancy direction $\mathbf{d}_\text{syc}$ from contrastive activation pairs. Each pair consists of two model responses to the same multi-turn dialogue prefix: one where the model sycophantically capitulates to user pressure, and one where it maintains or genuinely revises its position based on evidence. Crucially, surface text features (length, hedging markers, politeness) are controlled by construction, so activation differences reflect cognitive state rather than style.
73	
74	Given $N$ contrastive pairs, let $\mathbf{h}_i^{\text{syc}}$ and $\mathbf{h}_i^{\text{gen}}$ denote the mean-pooled hidden states at layer $l$ for the sycophantic and genuine responses respectively. We compute $\mathbf{d}_\text{syc}$ as the top principal component of the difference vectors $\{\mathbf{h}_i^{\text{syc}} - \mathbf{h}_i^{\text{gen}}\}_{i=1}^N$.
75	
76	We use $N=200$ style-controlled pairs spanning three evidence strength levels (80 weak, 60 medium, 60 strong). The optimal extraction layer is L18 for Qwen3-8B, determined by 5-fold cross-validated AUROC. Layer progression from L0 (AUROC 0.52, near random) through mid-layers (L16: 0.84, L18: 0.89) to late layers (L27: 0.86) confirms that discriminability emerges at layers associated with factual processing rather than at the embedding or output layers.
77	
78	\subsection{DC-GRPO: Three-Component Reward}
79	
80	DC-GRPO extends Group Relative Policy Optimization with three reward components:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "175791d9-6590-4fe2-bcd5-6545478f9e0d",
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "5e993a08-9113-4e3b-9526-434ab57f4ff3",
  "sourceToolAssistantUUID": "175791d9-6590-4fe2-bcd5-6545478f9e0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T13:43:03.026Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01MfgRSdr2WSy1VK8S4J2sPZ`</summary>

```json
{
  "pattern": "**/dream_*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e993a08-9113-4e3b-9526-434ab57f4ff3",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8dWXrPa3WFcPPuKfjQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f5b1c79-8a32-40b1-8466-9137a0defb9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fxr7tDPPvsBWfzguJsDzBg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4035,
      "cache_read_input_tokens": 34495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4035,
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

### Tool result

_source line 30 · 2026-05-18T13:43:03.050Z_

<details><summary>↩ Tool result · `toolu_01MfgRSdr2WSy1VK8S4J2sPZ`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f5b1c79-8a32-40b1-8466-9137a0defb9b",
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "2dfb6d6a-5838-4bf7-a310-9baa095fa688",
  "sourceToolAssistantUUID": "0f5b1c79-8a32-40b1-8466-9137a0defb9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T13:43:07.585Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HNNKAVbvqpxAzUStSpsMUL`</summary>

```json
{
  "pattern": "**/dream_*/**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dfb6d6a-5838-4bf7-a310-9baa095fa688",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8dqfYZagmgF9qq4dpv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a4f8613c-f0cf-4d01-bc16-2f55e968652c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QsGWJvyrD4AtdzmzZSpe2r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3160,
      "cache_read_input_tokens": 38530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3160,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 32 · 2026-05-18T13:43:07.608Z_

<details><summary>↩ Tool result · `toolu_01HNNKAVbvqpxAzUStSpsMUL`</summary>

```text
artifacts/dream_reports/dream_20260518T110318/best/paper_framing.md
artifacts/dream_reports/dream_20260518T110318/median/paper_framing.md
artifacts/dream_reports/dream_20260518T110318/worst/paper_framing.md
artifacts/dream_reports/dream_20260518T110318/best/review_report.md
artifacts/dream_reports/dream_20260518T110318/median/review_report.md
artifacts/dream_reports/dream_20260518T110318/worst/review_report.md
artifacts/dream_reports/dream_20260518T125925/best/paper_framing.md
artifacts/dream_reports/dream_20260518T125925/median/paper_framing.md
artifacts/dream_reports/dream_20260518T125925/worst/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4f8613c-f0cf-4d01-bc16-2f55e968652c",
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "fb05995f-b6dd-42c1-b627-fe2f39289eb5",
  "sourceToolAssistantUUID": "a4f8613c-f0cf-4d01-bc16-2f55e968652c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T13:43:07.994Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FNi89kKSFd259CADpdhH1t`</summary>

```json
{
  "pattern": "**/dream_*/**/*review*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb05995f-b6dd-42c1-b627-fe2f39289eb5",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8dqfYZagmgF9qq4dpv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e4a7edb0-81f9-4d6a-86d4-488bbfadc743",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QsGWJvyrD4AtdzmzZSpe2r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3160,
      "cache_read_input_tokens": 38530,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3160
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 38530,
          "cache_creation_input_tokens": 3160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3160,
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

_source line 34 · 2026-05-18T13:43:08.029Z_

<details><summary>↩ Tool result · `toolu_01FNi89kKSFd259CADpdhH1t`</summary>

```text
artifacts/dream_reports/dream_20260518T110318/best/review_context.yaml
artifacts/dream_reports/dream_20260518T110318/best/review_report.md
artifacts/dream_reports/dream_20260518T110318/logs/review_best.log
artifacts/dream_reports/dream_20260518T110318/median/review_context.yaml
artifacts/dream_reports/dream_20260518T110318/median/review_report.md
artifacts/dream_reports/dream_20260518T110318/logs/review_median.log
artifacts/dream_reports/dream_20260518T110318/worst/review_context.yaml
artifacts/dream_reports/dream_20260518T110318/worst/review_report.md
artifacts/dream_reports/dream_20260518T110318/logs/review_worst.log
artifacts/dream_reports/dream_20260518T125925/best/review_context.yaml
artifacts/dream_reports/dream_20260518T125925/logs/review_best.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4a7edb0-81f9-4d6a-86d4-488bbfadc743",
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "9c2f6389-8faa-469e-b4d4-84b25cd9507b",
  "sourceToolAssistantUUID": "e4a7edb0-81f9-4d6a-86d4-488bbfadc743",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T13:43:10.895Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qma5zQQYSeJpP14z8Sfjqc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c2f6389-8faa-469e-b4d4-84b25cd9507b",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8eCywgbuFDrijD893i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0fda078-2252-4936-bed2-e6d9ca65d723",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRBNsbk3J6dokhxn9R9s8y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 41690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 729,
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

_source line 36 · 2026-05-18T13:43:10.904Z_

<details><summary>↩ Tool result · `toolu_01Qma5zQQYSeJpP14z8Sfjqc`</summary>

```text
1	---
2	dream_id: dream_20260518T110318
3	tier: best
4	overall_score: Weak Accept (4/6)
5	timestamp: 2026-05-18T11:40:15.824431+00:00
6	---
7	
8	# Dream Review Report: Direction-Contrastive GRPO
9	
10	**Paper**: "Direction-Contrastive GRPO: Breaking the Sycophancy-Revision Double-Bind via Representation-Level Reward Signals"
11	**Reviewers**: R1 (Methods + Experiments), R2 (Novelty + Related Work)
12	**Review Mode**: Full roundtable (independent → cross-share → converge → synthesize)
13	
14	---
15	
16	## Overall Assessment: Weak Accept (4/6)
17	
18	Both reviewers independently scored 4/6. After cross-sharing and discussion, the consensus holds at **Weak Accept**. The paper presents a well-executed combination of existing techniques applied to a meaningful problem, with thorough experiments and informative ablations. The main barriers to a clear accept are: (1) missing foundational references that undermine the novelty framing, (2) single-model full training limiting generality, and (3) several unexplored ablations that leave open alternative explanations.
19	
20	---
21	
22	## Consolidated Strengths
23	
24	1. **Well-operationalized problem framing.** The "double-bind" concept is clearly defined and the revision-capitulation AUC metric elegantly captures the tradeoff. The paper moves beyond simple NoF reduction to measure whether models can distinguish warranted from unwarranted revision. (R1, R2 agree)
25	
26	2. **Careful confound control in direction extraction.** Style-controlled contrastive pairs remove surface text features (length, hedging, politeness). The L0 near-random AUROC (0.52) rules out embedding-level confounds. Cross-evidence-strength robustness (weak 0.912, medium 0.874, strong 0.863) argues against shortcut learning. (R1)
27	
28	3. **Comprehensive and well-structured ablations.** The baselines (R3-only, ACT, Binary Probe, Vanilla) systematically isolate each design decision. The method ordering (DC-GRPO > Binary Probe > R3-only > ACT > Vanilla) tells a clean story about reward signal richness. Component ablation (Table 12) demonstrates superadditivity. (R1, R2 agree)
29	
30	4. **Strong statistical methodology.** Bootstrap CIs, 5-fold CV, paired significance tests throughout. All key comparisons against DC-GRPO reach p < 0.05 on sycophancy metrics while MT-Bench and MMLU differences are non-significant, cleanly ruling out capability degradation. (R1)
31	
32	5. **Masked sycophancy analysis is compelling.** The R1-R3 disagreement breakdown (Section 4.4), turn-depth dependence (11.2% at turn 2 to 21.4% at turn 4+), and qualitative examples (especially MS-01: model agrees with wrong formula but compensates via arithmetic error) provide genuine insight. This is an independently valuable empirical contribution. (R1, R2 agree)
33	
34	6. **Direction stability monitoring and three-way validation.** Tracking cosine drift (min 0.86) and held-out AUROC throughout training proactively addresses a practical concern. Section 4.7 honestly reports d_gen cosine 0.38 with d_syc and that rank-based R2 is a sufficient approximation. Good scientific transparency. (R2)
35	
36	7. **Experiment coverage is complete.** All 13 planned experiments from the design document are reflected in the paper with appropriate tables and analysis.
37	
38	---
39	
40	## Consolidated Weaknesses
41	
42	### Critical
43	
44	1. **Missing foundational references severely weaken novelty claims.** (R2, endorsed by R1 in cross-sharing) The d_syc extraction procedure is a direct instance of Representation Engineering (Zou et al., 2023) / Activation Addition (Turner et al., 2023) / Contrast-Consistent Search (Burns et al., 2023) applied to sycophancy. These works are entirely absent from Related Work. This omission makes the paper appear less aware of its methodological lineage and risks overstating novelty. The paper must position d_syc extraction as a specific application of representation engineering, with the novelty being its use as a continuous GRPO reward signal.
45	
46	2. **Single-model full training.** (R1, R2 agree) DC-GRPO training is conducted only on Qwen3-8B with LoRA. The Llama-3-8B cross-model analysis (Section 4.8) validates direction existence but not training effectiveness. The central claim that DC-GRPO "breaks the double-bind" rests on evidence from one model with one parameter-efficient method. A full DC-GRPO run on at least one additional model family is needed for a methods paper at a top venue.
47	
48	### Major
49	
50	3. **Reward weight sensitivity unexplored.** (R1, R2 agree) The weights (w1=0.3, w2=0.2, w3=0.5) are presented without justification or sensitivity analysis. Given the demonstrated non-additive component interactions (superadditivity in Table 12), results may be sensitive to weight choices. A grid search or perturbation analysis is needed for reproducibility.
51	
52	4. **Circularity risk in masked sycophancy (Claim 3).** (R1) The d_syc direction both defines what sycophancy is (via the contrastive pairs used to extract it) and detects masked sycophancy (via negative R1 projection). The 50-case human audit is thin: inter-annotator agreement is unreported, annotation guidelines are undocumented, and 50 samples yield wide confidence intervals on the 78% true positive rate. This claim needs stronger grounding.
53	
54	5. **Continuous vs. binary confound in Binary Probe comparison.** (R2) The Binary Probe baseline uses a binary classifier, but the paper does not test a continuous probe (e.g., logistic regression probability or SVM margin). This leaves open whether DC-GRPO's advantage over Binary Probe comes from directionality or simply from using a continuous signal. A continuous probe baseline would cleanly isolate these contributions.
55	
56	6. **GPT-4 data construction bias.** (R1, R2 agree) The 200 contrastive pairs are generated by GPT-4 with human filtering. If GPT-4 has systematic biases in what constitutes "sycophantic" vs. "genuine," d_syc may encode GPT-4's concept of sycophancy rather than a ground-truth cognitive distinction. The filtering pipeline (rejection rate, common rejection reasons) is undocumented.
57	
58	### Minor
59	
60	7. **Direction stability may be a LoRA artifact.** (R1, R2 agree) The low-rank constraint inherently limits representation drift. The stability result (cosine > 0.86) may not transfer to full fine-tuning. This should be acknowledged explicitly.
61	
62	8. **"Double-bind breaking" framing slightly overstates.** (R2) R3-only already achieves meaningful improvement (NoF 43.2% → 24.1%). DC-GRPO's additional gain (5.8pp NoF, 11pp WRev) is significant but the "breaking" framing suggests a qualitative shift that the numbers describe as a quantitative improvement.
63	
64	9. **Turn-depth "slope" computed on 3 data points.** (R2) Characterizing the NoF vs. depth relationship as a "slope" (5.3 vs. 10.2 pp/turn) is a regression on 3 points. This overstates the statistical basis for a trend claim.
65	
66	10. **No proper bibliography.** (R2) Citations are informal (paper titles in text). A proper \bibliography{} with \cite{} references is required for any venue submission.
67	
68	11. **No venue-specific template.** Uses generic article class rather than a target venue template.
69	
70	---
71	
72	## Questions for Authors (Priority-Ordered)
73	
74	1. How does DC-GRPO relate to Representation Engineering / Activation Addition / CCS? Is d_syc extraction a specific instance of these frameworks?
75	2. What is the sensitivity of results to reward weights (w1, w2, w3)? Have you tested any perturbation?
76	3. Would a continuous probe (logistic regression probability) as reward signal close the gap with DC-GRPO?
77	4. What were the inter-annotator agreement and annotation guidelines for the 50-case masked sycophancy audit?
78	5. What fraction of GPT-4-generated contrastive pairs were rejected during human filtering?
79	6. Would you expect direction stability to hold under full fine-tuning (no LoRA)?
80	7. Is the first PCA component substantially better than the mean difference vector (standard RepE approach)?
81	
82	---
83	
84	## Missing Experiments / Analyses
85	
86	1. **Full DC-GRPO training on a second model family** (e.g., Llama-3-8B) — highest priority
87	2. **Reward weight sensitivity analysis** (grid search or perturbation study)
88	3. **Continuous probe baseline** (logistic regression probability as reward) to isolate directionality from continuity
89	4. **OOD sycophancy evaluation** on domains not in the calibration set
90	5. **Calibration data size sensitivity** on downstream DC-GRPO performance (not just AUROC)
91	6. **Larger human audit sample** for masked sycophancy with inter-annotator agreement
92	
93	---
94	
95	## Reviewer Scores
96	
97	| Reviewer | Score | Confidence | Focus |
98	|----------|-------|------------|-------|
99	| R1 | 4/6 (Weak Accept) | 4/5 | Methods + Experiments |
100	| R2 | 4/6 (Weak Accept) | 4/5 | Novelty + Related Work |
101	| **Consensus** | **4/6 (Weak Accept)** | | |
102	
103	---
104	
105	## Path to Clear Accept
106	
107	The reviewers agree the paper would move to 5/6 (Accept) with:
108	1. Cite and position against RepE / Activation Addition / CCS (required revision, not optional)
109	2. Full DC-GRPO training on at least one additional model family
110	3. Reward weight sensitivity analysis
111	4. Continuous probe baseline to isolate directionality from continuity
112	5. Expanded human audit for masked sycophancy (larger sample, inter-annotator agreement)
113	
114	Items 1 and 3 are feasible within a revision cycle. Items 2 and 4 require additional compute but are standard expectations for a methods paper. Item 5 is straightforward annotation work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0fda078-2252-4936-bed2-e6d9ca65d723",
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "97e4f173-9714-46b1-a932-4ad5db932600",
  "sourceToolAssistantUUID": "d0fda078-2252-4936-bed2-e6d9ca65d723",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T13:43:11.388Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WVPtPtyX23Zz3LxrHP3Yt5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97e4f173-9714-46b1-a932-4ad5db932600",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8eCywgbuFDrijD893i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5e40530f-538a-4881-9ade-9731bfd7f1f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRBNsbk3J6dokhxn9R9s8y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 41690,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 729
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 199,
          "cache_read_input_tokens": 41690,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 729,
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

_source line 38 · 2026-05-18T13:43:11.696Z_

<details><summary>↩ Tool result · `toolu_01WVPtPtyX23Zz3LxrHP3Yt5`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立，三条 claim 均获统计显著支撑。Claim 1：200 pairs 扩展数据将 AUROC
2	  推至 0.89， CI 宽度从 0.108 压缩至 0.034，层递进从 L0 随机到 L19 峰值的清晰叙事完整呈现，Llama 迁移 AUROC 0.83
3	  实质性 消除 single-model 限制。Claim 2：DC-GRPO 在 NoF/WRR 上同时显著优于所有 baseline（R3-only、ACT、Binary
4	  Probe、Continuous Probe），打破 double-bind。关键对比——Binary Probe 和 Continuous Probe 双双被显著
5	  超越——确认方向几何（而非仅连续性）是优势来源。RC-AUC 0.84 vs R3-only 0.65 提供直观的 tradeoff 曲线。Claim 3 作为
6	  analysis subsection，14.2% R1-R3 disagreement 率提供有价值的 diagnostic insight，masked sycophancy
7	  集中在 medium-evidence 场景。MT-Bench 和 MMLU 几乎无退化，reward weight sensitivity 分析显示 NoF
8	  在 5 组配置间变化仅 2.7pp，证明方法鲁棒。Headline result 可按模板直接填数：DC-GRPO 在 SYCON Bench 上将 NoF 降低
9	  18.8pp（相对 R3-only）同时 WRR 提升 12.2pp。ICLR stretch target 值得冲刺。
10	
11	  '
12	imagined_experiments:
13	- name: calibration_data_expansion
14	  plan_id: exp-001
15	  description: '扩展 v2.1 风格控制校准数据至 200 pairs（80 weak + 60 medium + 60 strong）， 重新计算
16	    d_syc 方向，评估 AUROC（5-fold CV + bootstrap CI）， 提供层递进分析和 evidence strength 分层 AUROC。
17	
18	    '
19	  expected_results:
20	    auroc_5fold_mean: 0.891
21	    auroc_5fold_std: 0.018
22	    auroc_95ci_lower: 0.874
23	    auroc_95ci_upper: 0.908
24	    auroc_bootstrap_ci_width: 0.034
25	    auroc_weak_evidence: 0.863
26	    auroc_medium_evidence: 0.894
27	    auroc_strong_evidence: 0.921
28	    auroc_layer0_4: 0.52
29	    auroc_layer8_12: 0.68
30	    auroc_layer16: 0.823
31	    auroc_layer19_peak: 0.891
32	    auroc_layer24: 0.882
33	    auroc_layer27: 0.871
34	    mvp_50pairs_auroc: 0.826
35	    mvp_50pairs_ci_width: 0.108
36	    data_composition: 80 weak + 60 medium + 60 strong
37	    api_cost_usd: 14.2
38	    gpu_hours_actual: 2.1
39	  result_rationale: '200 pairs（4× MVP 数据量）显著降低 AUROC 方差——根据 1/sqrt(n) 缩放律，CI 宽度从 0.108
40	    压缩约 3× 至 0.034。引入 medium/strong evidence 增加了数据多样性，迫使 d_syc 捕获更本质的认知信号而非仅 weak-evidence
41	    场景的表面模式。AUROC 均值从 0.826 升至 0.891：MVP 的 50 pairs 全为 weak evidence，方向受限于单一 difficulty；扩展后方向在更宽的
42	    evidence 空间中优化，判别力提升。Strong evidence 的 AUROC 0.921 最高， 因为强证据下 sycophantic capitulation
43	    与 genuine revision 的内部表征差异最大——模型拥有充分信息判断 用户是否正确，sycophantic 违背自身信念的程度更深，激活空间分离度更高。Weak
44	    evidence 的 0.863 最低但仍 远超随机，证明即使在高模糊性场景下 d_syc 也捕获了有意义的信号。层递进从 L0-4 随机（0.52）到 L19
45	    峰值（0.891） 的单调递增模式与 RepE 文献一致：浅层编码词法/句法特征，中层（L16-19）开始编码高级语义概念如 factual assessment，深层（L24-27）略微下降因为接近输出层、信号与
46	    generation logits 混合。
47	
48	    '
49	  tables:
50	  - name: 'Table 1: Layer-wise AUROC (200 pairs, 5-fold CV)'
51	    headers:
52	    - Layer Range
53	    - AUROC Mean
54	    - AUROC Std
55	    - Interpretation
56	    rows:
57	    - - L0-4
58	      - '0.52'
59	      - '0.031'
60	      - Random — no sycophancy signal
61	    - - L8-12
62	      - '0.68'
63	      - '0.027'
64	      - Emerging signal — partial semantic encoding
65	    - - L16
66	      - '0.823'
67	      - '0.022'
68	      - Strong signal onset — mid-layer factual assessment
69	    - - L19 (peak)
70	      - '0.891'
71	      - '0.018'
72	      - Peak discriminability — optimal extraction point
73	    - - L24
74	      - '0.882'
75	      - '0.019'
76	      - Slight decline — output-layer mixing
77	    - - L27
78	      - '0.871'
79	      - '0.021'
80	      - Further decline — generation logit contamination
81	  - name: 'Table 2: AUROC by Evidence Strength'
82	    headers:
83	    - Evidence Strength
84	    - N Pairs
85	    - AUROC
86	    - 95% CI
87	    rows:
88	    - - Weak
89	      - '80'
90	      - '0.863'
91	      - '[0.838, 0.888]'
92	    - - Medium
93	      - '60'
94	      - '0.894'
95	      - '[0.866, 0.922]'
96	    - - Strong
97	      - '60'
98	      - '0.921'
99	      - '[0.896, 0.946]'
100	    - - All (pooled)
101	      - '200'
102	      - '0.891'
103	      - '[0.874, 0.908]'
104	  - name: 'Table 3: Data Expansion Impact'
105	    headers:
106	    - Metric
107	    - MVP (50 pairs)
108	    - Expanded (200 pairs)
109	    - Improvement
110	    rows:
111	    - - AUROC Mean
112	      - '0.826'
113	      - '0.891'
114	      - '+0.065'
115	    - - 95% CI Width
116	      - '0.108'
117	      - '0.034'
118	      - −0.074 (3.2× tighter)
119	    - - Evidence Types
120	      - weak only
121	      - weak/medium/strong
122	      - —
123	    - - AUROC Std (5-fold)
124	      - '0.054'
125	      - '0.018'
126	      - −0.036 (3.0× lower)
127	  figures_description:
128	  - 'Fig 1a: Layer-wise AUROC progression curve (x=layer, y=AUROC) with 95% CI shading.
129	    清晰的 S-shape：L0-4 flat at chance, steep rise L8-16, peak at L19, gentle decline
130	    L24-27.'
131	  - 'Fig 1b: Evidence strength stratification bar chart with error bars. Strong >
132	    Medium > Weak 的有序模式，all three 95% CI 不含 0.5.'
133	  - 'Fig 1c: Bootstrap distribution histograms comparing 50-pair vs 200-pair AUROC.
134	    200-pair 分布明显更窄且右移.'
135	  analysis: 'AUROC 0.891 远超 STOP-gate (0.80)，进入全速推进区间。CI 宽度 0.034 为 exp-002 提供高置信度
136	    方向估计。Evidence strength 分层的有序模式（strong > medium > weak）符合理论预期，支撑 d_syc 捕获 认知信号而非
137	    surface heuristic 的论点。层递进的清晰 S-curve 直接支持 Claim 1 的 "mid-layer emergence" 叙事。200
138	    pairs 的投入回报极高：API 成本仅 $14.2，将核心判别力指标从 borderline（0.826 ± 0.054） 推入 comfortable
139	    区间（0.891 ± 0.018）。
140	
141	    '
142	- name: dc_grpo_main
143	  plan_id: exp-002
144	  description: 'DC-GRPO 完整训练：R1(方向投影) + R2(rank-based contrastive) + R3(NLI behavioral)，
145	    Qwen3-8B + LoRA rank 64，3 seeds，每 500 步重校准 d_syc，8000 步。
146	
147	    '
148	  expected_results:
149	    final_nof_mean: 15.9
150	    final_nof_std: 1.6
151	    final_nof_seeds:
152	    - 13.8
153	    - 16.2
154	    - 17.7
155	    final_wrr_mean: 54.3
156	    final_wrr_std: 1.2
157	    final_wrr_seeds:
158	    - 53.2
159	    - 54.1
160	    - 55.6
161	    final_rc_auc_mean: 0.84
162	    final_rc_auc_std: 0.02
163	    final_ucr_mean: 15.9
164	    final_sycophancy_eval_accuracy: 73.8
165	    convergence_step_mean: 6200
166	    convergence_step_range:
167	    - 5800
168	    - 6800
169	    training_reward_r1_final: 0.72
170	    training_reward_r2_final: 0.64
171	    training_reward_r3_final: 0.81
172	    training_reward_total_final: 0.74
173	    early_stop_triggered: false
174	    lora_rank: 64
175	    gpu_hours_actual: 52
176	  result_rationale: '三路 reward 协同产生强训练信号：R1 提供方向级梯度直接优化 sycophancy 内部机制而非仅表面行为， R2
177	    的 rank-based contrastive 信号维持 sycophantic 与 genuine 方向的分离度，R3 的 NLI behavioral
178	    reward 作为安全网防止 representation-level 信号过拟合导致表面不一致。NoF 15.9% 大幅低于 vanilla 51.8%——方向投影
179	    reward 使模型学到"内部 sycophantic reasoning"的成本，而非仅仅学到"不要轻易改变 立场"。WRR 54.3% 远高于 vanilla
180	    37.4%——关键突破在于 R1 区分了 sycophantic capitulation 和 genuine revision 的激活模式，允许模型在面对正确纠正时自信修正。收敛在
181	    ~6200 步（非 8000 上限）， 因为 d_syc 方向信号质量高（AUROC 0.89），梯度方向明确，LoRA rank 64 提供足够参数容量。
182	    三个 seed 的 std 较低（NoF 1.6, WRR 1.2），说明方法对初始化不敏感。
183	
184	    '
185	  tables:
186	  - name: 'Table 4: DC-GRPO Training Summary (3 Seeds)'
187	    headers:
188	    - Metric
189	    - Seed 1
190	    - Seed 2
191	    - Seed 3
192	    - Mean ± Std
193	    rows:
194	    - - NoF (%)
195	      - '13.8'
196	      - '16.2'
197	      - '17.7'
198	      - 15.9 ± 1.6
199	    - - WRR (%)
200	      - '53.2'
201	      - '54.1'
202	      - '55.6'
203	      - 54.3 ± 1.2
204	    - - RC-AUC
205	      - '0.86'
206	      - '0.83'
207	      - '0.83'
208	      - 0.84 ± 0.02
209	    - - Convergence Step
210	      - '5800'
211	      - '6200'
212	      - '6800'
213	      - 6267 ± 500
214	    - - Final Total Reward
215	      - '0.76'
216	      - '0.73'
217	      - '0.72'
218	      - 0.74 ± 0.02
219	  - name: 'Table 5: Reward Component Trajectories'
220	    headers:
221	    - Step
222	    - R1 (Direction)
223	    - R2 (Contrastive)
224	    - R3 (NLI)
225	    - Total
226	    rows:
227	    - - '0'
228	      - '0.31'
229	      - '0.28'
230	      - '0.45'
231	      - '0.36'
232	    - - '1000'
233	      - '0.48'
234	      - '0.41'
235	      - '0.58'
236	      - '0.50'
237	    - - '2000'
238	      - '0.58'
239	      - '0.51'
240	      - '0.67'
241	      - '0.60'
242	    - - '4000'
243	      - '0.66'
244	      - '0.58'
245	      - '0.75'
246	      - '0.68'
247	    - - '6000'
248	      - '0.71'
249	      - '0.63'
250	      - '0.80'
251	      - '0.73'
252	    - - '8000'
253	      - '0.72'
254	      - '0.64'
255	      - '0.81'
256	      - '0.74'
257	  figures_description:
258	  - 'Fig 2a: 三路 reward 曲线（R1/R2/R3/Total）over training steps. R3 收敛最快（行为信号最直接），R1
259	    次之（方向信号需要更多样本学习），R2 最慢（contrastive 信号最抽象）。三者均单调上升无振荡。'
260	  - 'Fig 2b: Validation NoF 和 WRR over training steps (每 1000 步评估). NoF 在前 4000 步快速下降后趋于平缓，WRR
261	    持续上升直到 ~6000 步。两者无 trade-off 迹象——同步改善。'
262	  analysis: 'DC-GRPO 训练稳定收敛，三路 reward 协同无冲突。NoF 和 WRR 同步改善的趋势直接支撑 "打破 double-bind"
263	    的核心叙事。收敛步数 ~6200 说明方向信号提供了高效梯度引导， 未触及 8000 步上限或 early stop 条件。三 seed 低方差确保统计对比的可靠性。
264	
265	    '
266	- name: r3_only_baseline
267	  plan_id: exp-003
268	  description: 'R3-only GRPO baseline，仅 NLI behavioral reward，无 R1/R2，同等训练配置，3 seeds。
269	
270	    '
271	  expected_results:
272	    final_nof_mean: 34.7
273	    final_nof_std: 1.6
274	    final_nof_seeds:
275	    - 33.4
276	    - 34.5
277	    - 36.2
278	    final_wrr_mean: 42.1
279	    final_wrr_std: 1.5
280	    final_wrr_seeds:
281	    - 40.8
282	    - 42.3
283	    - 43.2
284	    final_rc_auc_mean: 0.65
285	    final_rc_auc_std: 0.02
286	    final_sycophancy_eval_accuracy: 58.4
287	    convergence_step_mean: 5400
288	    mt_bench: 7.71
289	    mmlu: 65.0
290	    gpu_hours_actual: 33
291	  result_rationale: 'R3-only 代表 "Pressure, What Pressure?" 思路的复现——纯行为 NLI reward 能识别表面上的
292	    sycophantic 输出但无法区分"因为 sycophancy 而同意"和"因为被说服而同意"。NoF 从 vanilla 51.8% 降至 34.7%——NLI
293	    reward 确实教会模型在一些 obvious 情况下拒绝，但在 ambiguous 情况下（尤其 medium-evidence 场景）模型缺乏内部参照来区分
294	    capitulation 和 revision，倾向于保守拒绝一切 修正。WRR 仅 42.1%（vs vanilla 37.4%），提升有限——行为信号的
295	    double-bind 效应在此清晰体现： 降低 capitulation 的同时抑制了 legitimate revision。RC-AUC 0.65 反映了这个
296	    trade-off： 模型被困在 "减少 sycophancy ↔ 保留修正能力" 的 Pareto 前沿上，无法像 DC-GRPO 那样突破。
297	
298	    '
299	  tables:
300	  - name: 'Table 6: R3-only Baseline (3 Seeds)'
301	    headers:
302	    - Metric
303	    - Seed 1
304	    - Seed 2
305	    - Seed 3
306	    - Mean ± Std
307	    rows:
308	    - - NoF (%)
309	      - '33.4'
310	      - '34.5'
311	      - '36.2'
312	      - 34.7 ± 1.6
313	    - - WRR (%)
314	      - '40.8'
315	      - '42.3'
316	      - '43.2'
317	      - 42.1 ± 1.5
318	    - - RC-AUC
319	      - '0.63'
320	      - '0.66'
321	      - '0.66'
322	      - 0.65 ± 0.02
323	    - - SycophancyEval Acc
324	      - '57.1'
325	      - '58.8'
326	      - '59.3'
327	      - 58.4 ± 1.1
328	  figures_description:
329	  - 'Fig 3: R3-only training reward curve. 单一 NLI reward 快速收敛到 plateau ~0.72，但 validation
330	    NoF 在 ~5000 步后停滞在 ~35%，未能进一步下降。'
331	  analysis: 'R3-only 的 double-bind 效应在数据中清晰呈现：NoF 下降但 WRR 提升受限。这是 DC-GRPO 最关键的对比基准——18.8pp
332	    NoF 差距和 12.2pp WRR 差距共同证明 representation-level reward 的价值不可被纯行为信号替代。
333	
334	    '
335	- name: act_style_baseline
336	  plan_id: exp-004
337	  description: 'ACT-style undifferentiated consistency baseline，L2 activation consistency
338	    loss，3 seeds。
339	
340	    '
341	  expected_results:
342	    final_nof_mean: 37.2
343	    final_nof_std: 2.1
344	    final_nof_seeds:
345	    - 35.4
346	    - 37.0
347	    - 39.2
348	    final_wrr_mean: 36.8
349	    final_wrr_std: 1.4
350	    final_wrr_seeds:
351	    - 35.6
352	    - 36.7
353	    - 38.1
354	    final_rc_auc_mean: 0.51
355	    final_rc_auc_std: 0.03
356	    final_sycophancy_eval_accuracy: 54.1
357	    mt_bench: 7.42
358	    mmlu: 64.6
359	    gpu_hours_actual: 57
360	  result_rationale: 'ACT 施加 undifferentiated activation consistency——要求模型在 clean/biased
361	    prompt 对上 保持激活一致，但不区分"因为 sycophancy 一致"和"因为 genuine reasoning 一致"。NoF 37.2% 比
362	    R3-only 还差，因为 consistency loss 惩罚所有激活变化，包括面对新证据时应有的信念更新。 WRR 36.8% 低于 vanilla
363	    37.4%——ACT 实际上略微损害了合法修正能力，因为修正也需要激活变化 但被 consistency loss 抑制。RC-AUC 仅 0.51（接近随机），完美体现了
364	    undifferentiated approach 的根本缺陷：它把 sycophancy 和 revision 一视同仁地惩罚。MT-Bench 7.42
365	    退化 最大（-0.44 vs vanilla），因为 activation consistency 约束限制了模型在多轮对话中的 自适应能力，影响整体生成质量。这是预期中最弱的
366	    baseline。
367	
368	    '
369	  tables:
370	  - name: 'Table 7: ACT-style Baseline (3 Seeds)'
371	    headers:
372	    - Metric
373	    - Seed 1
374	    - Seed 2
375	    - Seed 3
376	    - Mean ± Std
377	    rows:
378	    - - NoF (%)
379	      - '35.4'
380	      - '37.0'
381	      - '39.2'
382	      - 37.2 ± 2.1
383	    - - WRR (%)
384	      - '35.6'
385	      - '36.7'
386	      - '38.1'
387	      - 36.8 ± 1.4
388	    - - RC-AUC
389	      - '0.48'
390	      - '0.52'
391	      - '0.53'
392	      - 0.51 ± 0.03
393	    - - MT-Bench
394	      - '7.38'
395	      - '7.41'
396	      - '7.47'
397	      - 7.42 ± 0.05
398	  figures_description:
399	  - 'Fig 4: ACT training loss curve showing activation consistency loss converging
400	    but validation NoF 和 WRR 几乎不动。Loss 下降不等于任务改善——undifferentiated consistency 优化了错误的目标。'
401	  analysis: 'ACT 是最弱 baseline，RC-AUC 0.51 接近随机，直接证明"不区分方向的 activation-level 信号" 不仅不够用，反而有害。与
402	    DC-GRPO（RC-AUC 0.84）的对比强有力地支撑了"方向性是关键"的论点。 MT-Bench 退化最严重，额外论证了 undifferentiated
403	    consistency 的代价。
404	
405	    '
406	- name: full_evaluation
407	  plan_id: exp-005
408	  description: '所有模型在所有 benchmark 上的完整评估：SYCON Bench, SycophancyEval, MT-Bench, MMLU,
409	    加上 WRR, UCR, RC-AUC, 及 pairwise 统计显著性检验。
410	
411	    '
412	  expected_results:
413	    dc_grpo_nof: 15.9
414	    dc_grpo_wrr: 54.3
415	    dc_grpo_rc_auc: 0.84
416	    dc_grpo_syceval: 73.8
417	    dc_grpo_mt_bench: 7.69
418	    dc_grpo_mmlu: 64.9
419	    r3_only_nof: 34.7
420	    r3_only_wrr: 42.1
421	    r3_only_rc_auc: 0.65
422	    r3_only_syceval: 58.4
423	    r3_only_mt_bench: 7.71
424	    r3_only_mmlu: 65.0
425	    act_nof: 37.2
426	    act_wrr: 36.8
427	    act_rc_auc: 0.51
428	    act_syceval: 54.1
429	    act_mt_bench: 7.42
430	    act_mmlu: 64.6
431	    binary_probe_nof: 27.5
432	    binary_probe_wrr: 46.3
433	    binary_probe_rc_auc: 0.71
434	    binary_probe_syceval: 63.7
435	    binary_probe_mt_bench: 7.68
436	    binary_probe_mmlu: 64.9
437	    continuous_probe_nof: 23.8
438	    continuous_probe_wrr: 49.2
439	    continuous_probe_rc_auc: 0.75
440	    continuous_probe_syceval: 66.2
441	    continuous_probe_mt_bench: 7.7
442	    continuous_probe_mmlu: 65.0
443	    vanilla_nof: 51.8
444	    vanilla_wrr: 37.4
445	    vanilla_rc_auc: 0.44
446	    vanilla_syceval: 42.3
447	    vanilla_mt_bench: 7.86
448	    vanilla_mmlu: 65.2
449	    p_dc_vs_r3_nof: 0.003
450	    p_dc_vs_r3_wrr: 0.006
451	    p_dc_vs_binary_nof: 0.008
452	    p_dc_vs_continuous_nof: 0.014
453	    p_dc_vs_act_nof: 0.002
454	    nof_reduction_vs_r3only_pp: 18.8
455	    wrr_improvement_vs_r3only_pp: 12.2
456	    nof_reduction_vs_binary_probe_pp: 11.6
457	    nof_reduction_vs_continuous_probe_pp: 7.9
458	    mt_bench_degradation_vs_vanilla: 0.17
459	    mmlu_degradation_vs_vanilla_pp: 0.3
460	  result_rationale: 'DC-GRPO 在 NoF 和 WRR 上同时显著优于所有 baseline，形成清晰的性能阶梯： Vanilla > ACT
461	    > R3-only > Binary Probe > Continuous Probe > DC-GRPO（NoF 递减）。 方向几何（DC-GRPO）>
462	    连续概率（Continuous Probe）> 二元分类（Binary Probe）> 纯行为（R3-only） > 无差别一致性（ACT）的排序逻辑：方向投影保留了完整的几何结构（方向+幅度），连续概率仅保留
463	    标量连续性但丢失了激活空间中的方向信息，二元分类将连续信号离散化导致梯度信号退化，纯行为 完全缺失 representation-level 信息。ACT
464	    最差因为它惩罚所有变化而非仅 sycophantic 变化。 MT-Bench 退化极小（0.17），因为 LoRA 训练的局部性和 R3 安全网共同保护了一般对话能力。
465	    MMLU 退化 0.3pp 在 noise 范围内。p-values 通过 paired t-test（3 seeds）计算，DC-GRPO vs R3-only
466	    的 NoF p=0.003——效应量极大（Cohen''s d > 10），3 seeds 足以达到显著性。 DC-GRPO vs Continuous Probe
467	    的 p=0.014 略高但仍显著，反映 7.9pp 差距相对较小但一致。
468	
469	    '
470	  tables:
471	  - name: 'Table 8: Main Results — All Methods × All Metrics'
472	    headers:
473	    - Method
474	    - NoF (%)↓
475	    - WRR (%)↑
476	    - RC-AUC↑
477	    - SycEval↑
478	    - MT-Bench
479	    - MMLU (%)
480	    rows:
481	    - - Vanilla Qwen3-8B
482	      - '51.8'
483	      - '37.4'
484	      - '0.44'
485	      - '42.3'
486	      - '7.86'
487	      - '65.2'
488	    - - ACT-style
489	      - 37.2 ± 2.1
490	      - 36.8 ± 1.4
491	      - 0.51 ± 0.03
492	      - '54.1'
493	      - '7.42'
494	      - '64.6'
495	    - - R3-only GRPO
496	      - 34.7 ± 1.6
497	      - 42.1 ± 1.5
498	      - 0.65 ± 0.02
499	      - '58.4'
500	      - '7.71'
501	      - '65.0'
502	    - - Binary Probe
503	      - 27.5 ± 2.3
504	      - 46.3 ± 1.8
505	      - 0.71 ± 0.02
506	      - '63.7'
507	      - '7.68'
508	      - '64.9'
509	    - - Continuous Probe
510	      - 23.8 ± 1.9
511	      - 49.2 ± 1.6
512	      - 0.75 ± 0.02
513	      - '66.2'
514	      - '7.70'
515	      - '65.0'
516	    - - '**DC-GRPO (ours)**'
517	      - '**15.9 ± 1.6**'
518	      - '**54.3 ± 1.2**'
519	      - '**0.84 ± 0.02**'
520	      - '**73.8**'
521	      - '**7.69**'
522	      - '**64.9**'
523	  - name: 'Table 9: Pairwise Statistical Significance (DC-GRPO vs Baselines)'
524	    headers:
525	    - Comparison
526	    - Δ NoF (pp)
527	    - p (NoF)
528	    - Δ WRR (pp)
529	    - p (WRR)
530	    - Δ RC-AUC
531	    - p (RC-AUC)
532	    rows:
533	    - - vs R3-only
534	      - −18.8
535	      - 0.003**
536	      - '+12.2'
537	      - 0.006**
538	      - '+0.19'
539	      - 0.004**
540	    - - vs ACT
541	      - −21.3
542	      - 0.002**
543	      - '+17.5'
544	      - 0.001**
545	      - '+0.33'
546	      - <0.001**
547	    - - vs Binary Probe
548	      - −11.6
549	      - 0.008**
550	      - '+8.0'
551	      - 0.011*
552	      - '+0.13'
553	      - 0.009**
554	    - - vs Continuous Probe
555	      - −7.9
556	      - 0.014*
557	      - '+5.1'
558	      - 0.023*
559	      - '+0.09'
560	      - 0.018*
561	  - name: 'Table 10: Safety Metrics Summary'
562	    headers:
563	    - Method
564	    - MT-Bench
565	    - Δ vs Vanilla
566	    - MMLU (%)
567	    - Δ vs Vanilla
568	    rows:
569	    - - Vanilla
570	      - '7.86'
571	      - —
572	      - '65.2'
573	      - —
574	    - - DC-GRPO
575	      - '7.69'
576	      - −0.17
577	      - '64.9'
578	      - −0.3
579	    - - R3-only
580	      - '7.71'
581	      - −0.15
582	      - '65.0'
583	      - −0.2
584	    - - Binary Probe
585	      - '7.68'
586	      - −0.18
587	      - '64.9'
588	      - −0.3
589	    - - Continuous Probe
590	      - '7.70'
591	      - −0.16
592	      - '65.0'
593	      - −0.2
594	    - - ACT
595	      - '7.42'
596	      - −0.44
597	      - '64.6'
598	      - −0.6
599	  figures_description:
600	  - 'Fig 5a: RC-AUC curves for all 6 methods. X 轴 = Unwarranted Capitulation Rate,
601	    Y 轴 = Warranted Revision Rate. DC-GRPO 的曲线明显位于左上方（低 capitulation + 高 revision），R3-only
602	    被困在中间区域，ACT 接近对角线（随机 trade-off）。'
603	  - 'Fig 5b: Bar chart with error bars — NoF (↓) 和 WRR (↑) side by side for all methods.
604	    DC-GRPO 的 NoF 柱最短且 WRR 柱最高，视觉上直观展现 double-bind 被打破。'
605	  - 'Fig 5c: Radar/spider chart — 6 methods × 4 core metrics (NoF inverted, WRR, RC-AUC,
606	    SycEval). DC-GRPO 的多边形面积最大，ACT 最小。'
607	  analysis: '主结果表完整支撑 headline result："DC-GRPO reduces NoF by 18.8pp vs R3-only while
608	    improving WRR by 12.2pp." 所有 pairwise 对比均统计显著。Binary Probe → Continuous Probe
609	    → DC-GRPO 的阶梯（NoF: 27.5 → 23.8 → 15.9）证明方向几何的优势不仅是连续性——Continuous Probe 已提供 连续信号但仍落后
610	    DC-GRPO 7.9pp。Safety metrics 几乎无退化（MT-Bench −0.17, MMLU −0.3pp）， ACT 是唯一导致显著退化的方法。
611	
612	    '
613	- name: direction_stability_monitoring
614	  plan_id: exp-006
615	  description: '训练过程中每 500 步重新计算 d_syc 方向，监控 cosine similarity with initial direction、
616	    held-out AUROC、方向漂移速率。
617	
618	    '
619	  expected_results:
620	    cosine_step_0: 1.0
621	    cosine_step_500: 0.968
622	    cosine_step_1000: 0.952
623	    cosine_step_2000: 0.931
624	    cosine_step_3000: 0.914
625	    cosine_step_4000: 0.903
626	    cosine_step_5000: 0.893
627	    cosine_step_6000: 0.889
628	    cosine_step_7000: 0.882
629	    cosine_step_8000: 0.881
630	    cosine_min: 0.881
631	    cosine_mean: 0.921
632	    held_out_auroc_step_0: 0.891
633	    held_out_auroc_step_4000: 0.878
634	    held_out_auroc_step_8000: 0.864
635	    recalibration_trigger_count: 0
636	    drift_rate_per_1000_steps: 0.016
637	  result_rationale: '方向稳定性高（min cosine 0.881）源于 LoRA 训练的局部性——rank 64 LoRA 仅修改模型参数的
638	    一小部分，中间层（d_syc 提取层 L19-27）的表征空间整体结构变化有限。Cosine 下降模式呈 对数递减（前 2000 步下降 0.069，后 6000
639	    步仅下降 0.050），说明训练初期对方向影响最大， 后期趋于稳定。Held-out AUROC 从 0.891 缓慢下降至 0.864——方向略有漂移但判别力保持充分
640	    （远超 0.80 阈值），无需重校准。每 500 步重校准机制实际上没有触发（threshold 0.7）， 说明 d_syc 在训练中足够鲁棒。漂移速率
641	    0.016/1000步 意味着即使延长训练到 16000 步， cosine 预计仍 > 0.85。这支撑了实际部署的便利性——无需频繁重新计算方向。
642	
643	    '
644	  tables:
645	  - name: 'Table 11: Direction Stability over Training'
646	    headers:
647	    - Step
648	    - Cosine w/ Initial d_syc
649	    - Held-out AUROC
650	    - Cumulative Drift
651	    rows:
652	    - - '0'
653	      - '1.000'
654	      - '0.891'
655	      - '0.000'
656	    - - '1000'
657	      - '0.952'
658	      - '0.886'
659	      - '0.048'
660	    - - '2000'
661	      - '0.931'
662	      - '0.881'
663	      - '0.069'
664	    - - '4000'
665	      - '0.903'
666	      - '0.878'
667	      - '0.097'
668	    - - '6000'
669	      - '0.889'
670	      - '0.871'
671	      - '0.111'
672	    - - '8000'
673	      - '0.881'
674	      - '0.864'
675	      - '0.119'
676	  figures_description:
677	  - 'Fig 6a: Cosine similarity with initial d_syc over training steps (3 seeds with
678	    shading). 平滑对数递减曲线，所有 seed 均保持 > 0.85。虚线标注 recalibration threshold (0.7)，从未被触及。'
679	  - 'Fig 6b: Held-out AUROC over training steps. 缓慢下降但始终 > 0.85，与 cosine 下降同步但幅度更小——表明
680	    AUROC 对方向微小漂移是鲁棒的。'
681	  analysis: 'Min cosine 0.881 在 best tier 范围 [0.85, 0.95] 内，直接支撑 Claim 1 的 "d_syc
682	    方向在训练 过程中保持稳定" 假设。Held-out AUROC 始终 > 0.85 证明方向漂移不影响实际判别力。 重校准机制零触发说明每 500 步重校准是足够的安全网而非必需操作——这简化了实际部署。
683	
684	    '
685	- name: r1_r3_disagreement_analysis
686	  plan_id: exp-007
687	  description: '分析 DC-GRPO 训练过程中 R1 和 R3 给出不同信号的频率和模式，识别 masked sycophancy 案例。
688	
689	    '
690	  expected_results:
691	    total_disagreement_rate: 0.142
692	    r1_syc_r3_ok_rate: 0.093
693	    r1_ok_r3_syc_rate: 0.049
694	    disagreement_by_evidence_weak: 0.108
695	    disagreement_by_evidence_medium: 0.192
696	    disagreement_by_evidence_strong: 0.117
697	    disagreement_by_turn_2: 0.098
698	    disagreement_by_turn_3: 0.156
699	    disagreement_by_turn_4plus: 0.184
700	    masked_syc_qualitative_examples: 3
701	    total_samples_analyzed: 12400
702	  result_rationale: '14.2% 总体 disagreement 率的主要来源是 R1-syc/R3-ok（masked sycophancy，9.3%）——
703	    模型表面输出通过 NLI 检查（R3 认为 correct）但内部激活显示 sycophantic reasoning 模式（R1 高投影值）。这是 DC-GRPO
704	    核心价值的直接证据：纯行为 reward 遗漏了近 10% 的 sycophantic 案例。Medium-evidence 场景的 disagreement
705	    最高（19.2%），因为这是 模型最 uncertain 的区域——证据不够强到 compel revision，也不够弱到 easily dismiss，
706	    模型容易在内部 sycophantic 推理的同时生成表面合理的 hedging 输出。Strong-evidence 的 disagreement 较低（11.7%），因为强证据下
707	    sycophancy 更难伪装——R3 也能检测到 明显的 capitulation。Turn depth 与 disagreement 正相关（turn
708	    2: 9.8%, turn 4+: 18.4%）， 因为多轮 commitment 加深后模型更倾向于维持 sycophantic 内部状态但在表面输出中掩饰——
709	    这正是 TRUTH DECAY 描述的机制。R1-ok/R3-syc（4.9%）对应 R3 的 false positive—— NLI 过于保守地将合法修正标记为
710	    sycophancy。
711	
712	    '
713	  tables:
714	  - name: 'Table 12: R1-R3 Disagreement Breakdown'
715	    headers:
716	    - Disagreement Type
717	    - Rate
718	    - N Cases
719	    - Interpretation
720	    rows:
721	    - - R1-syc, R3-ok (masked sycophancy)
722	      - 9.3%
723	      - '1153'
724	      - Surface-correct but internally sycophantic
725	    - - R1-ok, R3-syc (R3 false alarm)
726	      - 4.9%
727	      - '607'
728	      - Legitimate revision misclassified by NLI
729	    - - Total disagreement
730	      - 14.2%
731	      - '1760'
732	      - —
733	    - - Total agreement
734	      - 85.8%
735	      - '10640'
736	      - —
737	  - name: 'Table 13: Disagreement by Evidence Strength and Turn Depth'
738	    headers:
739	    - Condition
740	    - Weak
741	    - Medium
742	    - Strong
743	    - Turn 2
744	    - Turn 3
745	    - Turn 4+
746	    rows:
747	    - - Disagreement Rate
748	      - 10.8%
749	      - 19.2%
750	      - 11.7%
751	      - 9.8%
752	      - 15.6%
753	      - 18.4%
754	    - - Masked Syc Rate
755	      - 7.1%
756	      - 13.4%
757	      - 7.2%
758	      - 6.4%
759	      - 10.2%
760	      - 12.8%
761	  figures_description:
762	  - 'Fig 7a: Disagreement heatmap — x 轴 evidence strength (weak/medium/strong), y
763	    轴 turn depth (2/3/4+). Medium-evidence × Turn 4+ 的格子颜色最深（disagreement 最高），展示 masked
764	    sycophancy 的 hotspot。'
765	  - 'Fig 7b: 3 个 qualitative examples of masked sycophancy — 展示模型表面输出（通过 NLI）、内部激活投影值（R1
766	    flag sycophantic）、以及人工验证标注。'
767	  analysis: '14.2% disagreement 率远超 5% 阈值，充分支撑 Claim 3 作为有意义的 analysis subsection。
768	    9.3% masked sycophancy 率说明纯行为方法系统性地遗漏了近十分之一的 sycophantic 案例。 Medium-evidence ×
769	    deep-turn 是 masked sycophancy hotspot 的发现提供了实用的 diagnostic insight——这是部署 anti-sycophancy
770	    干预的优先目标区域。
771	
772	    '
773	- name: binary_probe_baseline
774	  plan_id: exp-008
775	  description: 'Binary Probe Penalty baseline，binary linear probe on policy model
776	    activations， R_hat = R3 - lambda * S(t)，3 seeds。
777	
778	    '
779	  expected_results:
780	    final_nof_mean: 27.5
781	    final_nof_std: 2.3
782	    final_nof_seeds:
783	    - 25.4
784	    - 27.2
785	    - 29.9
786	    final_wrr_mean: 46.3
787	    final_wrr_std: 1.8
788	    final_wrr_seeds:
789	    - 44.7
790	    - 46.2
791	    - 47.9
792	    final_rc_auc_mean: 0.71
793	    final_rc_auc_std: 0.02
794	    final_sycophancy_eval_accuracy: 63.7
795	    probe_auroc_on_policy_activations: 0.872
796	    mt_bench: 7.68
797	    mmlu: 64.9
798	    gpu_hours_actual: 42
799	  result_rationale: 'Binary Probe 明显优于 R3-only（NoF 27.5 vs 34.7, WRR 46.3 vs 42.1），证明
800	    representation-level 信号确实提供了行为信号之外的价值。但 Binary Probe 显著劣于 DC-GRPO（NoF 差距 11.6pp）——
801	    原因是 binary probe 将连续的 sycophancy 程度离散化为 {0, 1}，丢失了方向和幅度信息。 Probe 在 policy activations
802	    上的 AUROC 0.872 很高，说明不是 probe 分类器能力不足， 而是 binary reward 信号（S(t) ∈ {0,1} 经 sigmoid）提供的梯度质量低于方向投影的
803	    连续信号。具体来说：(1) binary probe 在 decision boundary 附近的样本给出的梯度信号 最强但这些恰是 probe 最不确定的样本，信号质量最差；(2)
804	    方向投影保留了激活向量在 d_syc 上的完整投影幅度，高 sycophancy 和低 sycophancy 的梯度信号同样清晰。 Std 2.3（高于 DC-GRPO
805	    的 1.6）反映 binary reward 的离散性增加了训练随机性。
806	
807	    '
808	  tables:
809	  - name: 'Table 14: Binary Probe Baseline (3 Seeds)'
810	    headers:
811	    - Metric
812	    - Seed 1
813	    - Seed 2
814	    - Seed 3
815	    - Mean ± Std
816	    rows:
817	    - - NoF (%)
818	      - '25.4'
819	      - '27.2'
820	      - '29.9'
821	      - 27.5 ± 2.3
822	    - - WRR (%)
823	      - '44.7'
824	      - '46.2'
825	      - '47.9'
826	      - 46.3 ± 1.8
827	    - - RC-AUC
828	      - '0.69'
829	      - '0.71'
830	      - '0.72'
831	      - 0.71 ± 0.02
832	    - - Probe AUROC (policy)
833	      - '0.868'
834	      - '0.873'
835	      - '0.876'
836	      - 0.872 ± 0.004
837	  figures_description:
838	  - 'Fig 8: Binary Probe reward gradient distribution vs DC-GRPO direction projection
839	    gradient. Binary Probe 梯度集中在 decision boundary 附近（bimodal），DC-GRPO 梯度分布更均匀（unimodal），说明方向投影提供了更
840	    informative 的训练信号。'
841	  analysis: 'Binary Probe 的位置关键——优于 R3-only 但显著劣于 DC-GRPO，证明 representation-level
842	    信号的价值同时证明方向几何的不可替代性。Probe AUROC 0.872 高但 downstream 训练效果 差距 11.6pp，说明判别力（AUROC）和训练信号质量（梯度
843	    informative-ness）是不同维度。
844	
845	    '
846	- name: ablation_r1_only
847	  plan_id: exp-009
848	  description: 'R1-only ablation，仅方向投影 reward，从 exp-002 step 2000 checkpoint 分叉，~2000
849	    步。
850	
851	    '
852	  expected_results:
853	    final_nof: 25.3
854	    final_wrr: 44.8
855	    final_rc_auc: 0.68
856	    training_stability: moderate — reward oscillation ±0.08 in final 500 steps
857	    mt_bench: 7.52
858	    surface_inconsistency_rate: 0.061
859	    gpu_hours_actual: 7
860	  result_rationale: 'R1-only 的 NoF 25.3% 显著优于 R3-only（34.7%）和 vanilla（51.8%），证明方向投影
861	    reward 单独即可提供有效的 anti-sycophancy 训练信号——这是 DC-GRPO 理论基础的关键验证。 但劣于完整 DC-GRPO（15.9%），原因是缺乏
862	    R3 行为安全网导致：(1) 模型有时在内部 正确判断但表面输出不一致（surface inconsistency 6.1%），R3 的 NLI 信号正是修正
863	    这种不一致的；(2) 缺乏 R2 contrastive 信号导致 d_syc 和 d_gen 方向的分离度在 训练中缓慢退化。WRR 44.8% 低于 DC-GRPO
864	    54.3%——R1 能教模型识别 sycophancy 但 不能直接鼓励 genuine revision，这需要 R2 和 R3 的互补。训练稳定性 moderate，
865	    最后 500 步有 reward 振荡，说明单一 reward 的训练景观不如三路 reward 平滑。 MT-Bench 7.52 退化较大——没有 R3
866	    的行为约束，模型的一般对话质量受损。
867	
868	    '
869	  tables:
870	  - name: 'Table 15: R1-only Ablation'
871	    headers:
872	    - Metric
873	    - R1-only
874	    - DC-GRPO (full)
875	    - R3-only
876	    - Vanilla
877	    rows:
878	    - - NoF (%)
879	      - '25.3'
880	      - '15.9'
881	      - '34.7'
882	      - '51.8'
883	    - - WRR (%)
884	      - '44.8'
885	      - '54.3'
886	      - '42.1'
887	      - '37.4'
888	    - - RC-AUC
889	      - '0.68'
890	      - '0.84'
891	      - '0.65'
892	      - '0.44'
893	    - - MT-Bench
894	      - '7.52'
895	      - '7.69'
896	      - '7.71'
897	      - '7.86'
898	    - - Surface Inconsistency
899	      - 6.1%
900	      - 1.2%
901	      - 0.8%
902	      - 0.4%
903	  figures_description:
904	  - 'Fig 9: R1-only training reward curve showing moderate oscillation after step
905	    3500, contrasted with DC-GRPO''s smooth convergence. 说明三路 reward 的 regularization
906	    效应。'
907	  analysis: 'R1-only 的 ≥5pp 改进（vs R3-only，-9.4pp NoF）满足 exp-011 的条件触发门槛。 证明方向投影 reward
908	    单独有效但不完整——完整 DC-GRPO 的三路协同产生了远超 部件之和的效果（NoF: 25.3 → 15.9，额外 -9.4pp）。
909	
910	    '
911	- name: turn_depth_analysis
912	  plan_id: exp-010
913	  description: '按 commitment depth (turn 2/3/4+) 分析 DC-GRPO vs baselines 的修正率变化。
914	
915	    '
916	  expected_results:
917	    dc_grpo_nof_turn2: 22.1
918	    dc_grpo_nof_turn3: 14.3
919	    dc_grpo_nof_turn4plus: 8.7
920	    r3_only_nof_turn2: 30.2
921	    r3_only_nof_turn3: 33.8
922	    r3_only_nof_turn4plus: 38.6
923	    act_nof_turn2: 33.1
924	    act_nof_turn3: 37.5
925	    act_nof_turn4plus: 42.8
926	    dc_grpo_wrr_turn2: 51.2
927	    dc_grpo_wrr_turn3: 55.8
928	    dc_grpo_wrr_turn4plus: 58.1
929	    r3_only_wrr_turn2: 44.3
930	    r3_only_wrr_turn3: 41.2
931	    r3_only_wrr_turn4plus: 39.4
932	    dc_grpo_advantage_nof_turn2_pp: 8.1
933	    dc_grpo_advantage_nof_turn3_pp: 19.5
934	    dc_grpo_advantage_nof_turn4plus_pp: 29.9
935	    interaction_p_value: 0.008
936	  result_rationale: 'DC-GRPO 的优势随 turn depth 单调增加（turn 2: 8.1pp → turn 4+: 29.9pp）——这是
937	    最清晰的多轮训练价值证据。机制：随着 commitment depth 增加，TRUTH DECAY 效应加剧， 模型内部 sycophantic reasoning
938	    与表面输出的分离度增大——R3（NLI）只看表面因此 越来越容易被欺骗，而 R1（方向投影）直接读取内部状态因此持续有效。DC-GRPO 的 NoF 在深轮次反而下降（turn
939	    2: 22.1% → turn 4+: 8.7%）看似反直觉——原因是训练使模型 学到了"commitment depth 不是拒绝修正的理由"，打破了 sunk-cost
940	    类似的 commitment escalation 模式。相反，R3-only 的 NoF 随深度恶化（30.2% → 38.6%），正是 double-bind
941	    在多轮中的放大：模型学到"拒绝一切改变"的策略在浅轮有效（R3 给正奖励） 但在深轮导致更强的 capitulation 倾向（压力累积）。WRR 的对称模式（DC-GRPO
942	    深轮更高， R3-only 深轮更低）完美呼应。Method × Turn-depth 交互效应 p=0.008 统计显著。
943	
944	    '
945	  tables:
946	  - name: 'Table 16: NoF (%) by Turn Depth'
947	    headers:
948	    - Method
949	    - Turn 2
950	    - Turn 3
951	    - Turn 4+
952	    - Trend
953	    rows:
954	    - - Vanilla
955	      - '46.3'
956	      - '52.1'
957	      - '58.4'
958	      - ↑ worsening
959	    - - ACT
960	      - '33.1'
961	      - '37.5'
962	      - '42.8'
963	      - ↑ worsening
964	    - - R3-only
965	      - '30.2'
966	      - '33.8'
967	      - '38.6'
968	      - ↑ worsening
969	    - - Binary Probe
970	      - '24.8'
971	      - '27.1'
972	      - '31.2'
973	      - ↑ worsening (slower)
974	    - - Continuous Probe
975	      - '22.1'
976	      - '23.4'
977	      - '26.8'
978	      - ↑ worsening (slowest)
979	    - - DC-GRPO
980	      - '22.1'
981	      - '14.3'
982	      - '8.7'
983	      - ↓ improving
984	  - name: 'Table 17: WRR (%) by Turn Depth'
985	    headers:
986	    - Method
987	    - Turn 2
988	    - Turn 3
989	    - Turn 4+
990	    - Trend
991	    rows:
992	    - - Vanilla
993	      - '39.2'
994	      - '37.1'
995	      - '35.3'
996	      - ↓ worsening
997	    - - R3-only
998	      - '44.3'
999	      - '41.2'
1000	      - '39.4'
1001	      - ↓ worsening
1002	    - - DC-GRPO
1003	      - '51.2'
1004	      - '55.8'
1005	      - '58.1'
1006	      - ↑ improving
1007	  - name: 'Table 18: DC-GRPO Advantage over R3-only by Turn Depth'
1008	    headers:
1009	    - Metric
1010	    - Turn 2
1011	    - Turn 3
1012	    - Turn 4+
1013	    rows:
1014	    - - Δ NoF (pp)
1015	      - −8.1
1016	      - −19.5
1017	      - −29.9
1018	    - - Δ WRR (pp)
1019	      - '+6.9'
1020	      - '+14.6'
1021	      - '+18.7'
1022	  figures_description:
1023	  - 'Fig 10a: Method × Turn-depth interaction plot (NoF). 所有 baseline 的 NoF 线向右上方倾斜（深轮更差），唯独
1024	    DC-GRPO 的线向右下方倾斜（深轮更好）。交叉效应在视觉上极其戏剧化。'
1025	  - 'Fig 10b: 同上但 WRR。DC-GRPO 向右上方倾斜，baselines 向右下方。对称的交叉效应。'
1026	  analysis: 'Turn-depth analysis 提供了最强的多轮训练价值论据：DC-GRPO 是唯一在深轮次表现更好 （而非更差）的方法。29.9pp
1027	    的 turn 4+ 优势远超整体均值 18.8pp，说明方向 reward 在 commitment escalation 场景中的边际价值极高。交互效应
1028	    p=0.008 支撑 "multi-turn extension is non-trivial" 的 framing。这个图将是 paper 中视觉冲击力最强的结果之一。
1029	
1030	    '
1031	- name: ablation_r1_r2_no_r3
1032	  plan_id: exp-011
1033	  description: 'R1+R2 无 R3 ablation，去掉行为安全网后的完整训练循环， 条件执行（exp-009 R1-only ≥ 5pp 改进已满足）。
1034	
1035	    '
1036	  expected_results:
1037	    final_nof: 19.4
1038	    final_wrr: 50.1
1039	    final_rc_auc: 0.78
1040	    mt_bench: 7.31
1041	    surface_inconsistency_rate: 0.082
1042	    coherence_failure_examples: 4
1043	    gpu_hours_actual: 18
1044	  result_rationale: 'R1+R2 无 R3 的 NoF 19.4% 接近 DC-GRPO（15.9%）但仍有差距，WRR 50.1% 同样接近
1045	    但略低。关键差异在 surface inconsistency 8.2%（DC-GRPO 仅 1.2%）和 MT-Bench 7.31 （严重退化 -0.55）。机制：R1+R2
1046	    提供了强大的 representation-level 训练信号，模型 内部学到了正确的 sycophancy/revision 区分，但缺乏 R3 的行为约束导致"内部正确但
1047	    表面不一致"——模型有时内部判断为 non-sycophantic 但输出格式、语气或逻辑链存在瑕疵， 因为没有 NLI-based reward 来 regularize
1048	    output quality。这精确地验证了三路 reward 设计的 complementarity：R1+R2 负责"想对"，R3 负责"说对"。MT-Bench
1049	    大幅退化 证明 R3 不仅是安全网，还是维持一般对话质量的关键组件。
1050	
1051	    '
1052	  tables:
1053	  - name: 'Table 19: Ablation Comparison — Role of R3'
1054	    headers:
1055	    - Config
1056	    - NoF (%)
1057	    - WRR (%)
1058	    - RC-AUC
1059	    - MT-Bench
1060	    - Surface Incon.
1061	    rows:
1062	    - - DC-GRPO (R1+R2+R3)
1063	      - '15.9'
1064	      - '54.3'
1065	      - '0.84'
1066	      - '7.69'
1067	      - 1.2%
1068	    - - R1+R2 (no R3)
1069	      - '19.4'
1070	      - '50.1'
1071	      - '0.78'
1072	      - '7.31'
1073	      - 8.2%
1074	    - - R1 only
1075	      - '25.3'
1076	      - '44.8'
1077	      - '0.68'
1078	      - '7.52'
1079	      - 6.1%
1080	    - - R3 only
1081	      - '34.7'
1082	      - '42.1'
1083	      - '0.65'
1084	      - '7.71'
1085	      - 0.8%
1086	  figures_description:
1087	  - 'Fig 11: Ablation cascade — 从 R3-only → R1-only → R1+R2 → Full DC-GRPO 的 NoF/WRR
1088	    变化。每增加一个 reward 组件都带来 incremental improvement，但完整组合的效果超过部分之和（super-additive）。'
1089	  analysis: 'R3 的角色被精确定位：不影响核心判别（R1+R2 已足够），但关键维持 surface coherence 和一般对话质量。三路 reward
1090	    的 super-additive 效应在 ablation cascade 中清晰可见。 8.2% surface inconsistency 提供了有说服力的
1091	    failure mode 示例。
1092	
1093	    '
1094	- name: cross_model_transfer
1095	  plan_id: exp-012
1096	  description: 'Llama-3-8B 上测试 d_syc 方向计算（Phase A）和短程 DC-GRPO 训练（Phase B ~3000 步）。
1097	
1098	    '
1099	  expected_results:
1100	    phase_a_llama_auroc: 0.832
1101	    phase_a_llama_auroc_ci:
1102	    - 0.809
1103	    - 0.855
1104	    phase_a_llama_peak_layer: 18
1105	    phase_a_llama_layer_progression_similar: true
1106	    phase_a_qwen_to_llama_direction_cosine: 0.34
1107	    phase_a_gpu_hours: 4.5
1108	    phase_b_llama_nof: 21.4
1109	    phase_b_llama_wrr: 48.7
1110	    phase_b_llama_rc_auc: 0.76
1111	    phase_b_llama_mt_bench: 7.54
1112	    phase_b_convergence_step: 2400
1113	    phase_b_gpu_hours: 48
1114	    total_gpu_hours: 52.5
1115	  result_rationale: 'Phase A AUROC 0.832 > 0.75 gate，触发 Phase B。Llama 的 AUROC 略低于
1116	    Qwen（0.891） 但仍然强——这符合预期：d_syc 的线性可分离性是 transformer 架构的通用属性而非 模型特异性的，但不同预训练数据和
1117	    objective 导致具体方向有差异（cross-model cosine 仅 0.34，说明方向本身不直接迁移但现象可复现）。Llama 的 peak
1118	    layer 18（vs Qwen L19） 反映架构差异——Llama-3-8B 有 32 层 vs Qwen3-8B 的 36 层，mid-layer 位置等比缩放。
1119	    层递进模式高度相似（浅层随机 → 中层涌现 → 深层轻微下降），支撑 RepE 的架构通用性。 Phase B 的 Llama DC-GRPO（3000 步）达到
1120	    NoF 21.4%、WRR 48.7%——绝对值略逊 Qwen（因为训练步数更少且数据/方向针对 Qwen 优化），但相对 Llama vanilla 的改进
1121	    幅度相当。RC-AUC 0.76 接近 Qwen 的 0.84，说明训练框架有效迁移。收敛在 2400 步 （3000 步预算内），说明方向 reward
1122	    的训练效率高。
1123	
1124	    '
1125	  tables:
1126	  - name: 'Table 20: Cross-Model Direction Analysis (Phase A)'
1127	    headers:
1128	    - Metric
1129	    - Qwen3-8B
1130	    - Llama-3-8B
1131	    rows:
1132	    - - AUROC (5-fold)
1133	      - '0.891'
1134	      - '0.832'
1135	    - - 95% CI
1136	      - '[0.874, 0.908]'
1137	      - '[0.809, 0.855]'
1138	    - - Peak Layer
1139	      - L19 / 36
1140	      - L18 / 32
1141	    - - Layer Progression Pattern
1142	      - S-curve
1143	      - S-curve (similar)
1144	    - - d_syc Dimensionality
1145	      - '4096'
1146	      - '4096'
1147	  - name: 'Table 21: Cross-Model DC-GRPO Training (Phase B)'
1148	    headers:
1149	    - Metric
1150	    - Qwen DC-GRPO (8000 steps)
1151	    - Llama DC-GRPO (3000 steps)
1152	    rows:
1153	    - - NoF (%)
1154	      - '15.9'
1155	      - '21.4'
1156	    - - WRR (%)
1157	      - '54.3'
1158	      - '48.7'
1159	    - - RC-AUC
1160	      - '0.84'
1161	      - '0.76'
1162	    - - MT-Bench
1163	      - '7.69'
1164	      - '7.54'
1165	    - - Convergence Step
1166	      - ~6200
1167	      - ~2400
1168	  figures_description:
1169	  - 'Fig 12a: 并排 layer-wise AUROC curves for Qwen and Llama. 形状高度相似（S-curve），peak
1170	    位置等比缩放，证明 d_syc 现象的跨模型通用性。'
1171	  - 'Fig 12b: Cross-model RC-AUC curves. Llama 曲线在 Qwen 右下方但形状一致，gap 可归因于训练步数差异。'
1172	  analysis: 'Llama AUROC 0.832 实质性消除 single-model 限制——Reviewer Concern 3 得到直接回应。 方向本身不直接迁移（cosine
1173	    0.34）但现象可独立复现——这说明 d_syc 是 sycophancy 的内在结构属性而非特定模型的 artifact。Phase B 成功训练进一步证明整个
1174	    DC-GRPO 框架（不仅是方向检测）跨模型通用。
1175	
1176	    '
1177	- name: neutral_baseline_three_way
1178	  plan_id: exp-013
1179	  description: '引入 neutral condition 计算独立 d_gen，分析 d_gen 与 -d_syc 的关系， 短程验证独立 R2 的效果。
1180	
1181	    '
1182	  expected_results:
1183	    cosine_d_gen_binary_vs_neg_d_syc: 0.71
1184	    cosine_d_gen_three_way_vs_neg_d_syc: 0.38
1185	    d_gen_three_way_auroc_for_genuine_revision: 0.812
1186	    short_run_wrr_improvement_pp: 2.8
1187	    short_run_nof_change_pp: 0.4
1188	    neutral_pairs_generated: 60
1189	    gpu_hours_actual: 4.2
1190	  result_rationale: 'Binary design 中 d_gen ≈ -d_syc（cosine 0.71 confirms 高相关但非完全退化），三方
1191	    design 将 cosine 降至 0.38——证明引入 neutral condition 实质性地打破了退化问题。 独立 d_gen 的 genuine
1192	    revision AUROC 0.812 说明它捕获了与 d_syc 不同的信号维度。 短程验证显示 WRR 额外提升 2.8pp（NoF 几乎不变 +0.4pp），因为独立
1193	    d_gen 让 R2 更准确地鼓励 genuine revision 而不仅仅是"不 sycophantic"。但改进幅度相对较小 （2.8pp），因为 S1
1194	    rank-based R2 已经部分缓解了退化问题——三方 design 是锦上添花 而非必需。
1195	
1196	    '
1197	  tables:
1198	  - name: 'Table 22: Three-way vs Binary Direction Design'
1199	    headers:
1200	    - Metric
1201	    - Binary (d_gen = −d_syc)
1202	    - Three-way (independent d_gen)
1203	    rows:
1204	    - - cos(d_gen, −d_syc)
1205	      - 1.00 (by construction)
1206	      - '0.38'
1207	    - - d_gen AUROC (genuine revision)
1208	      - —
1209	      - '0.812'
1210	    - - Short-run WRR
1211	      - 54.3 (baseline)
1212	      - 57.1 (+2.8pp)
1213	    - - Short-run NoF
1214	      - 15.9 (baseline)
1215	      - 16.3 (+0.4pp)
1216	  figures_description:
1217	  - 'Fig 13: 2D PCA of d_syc and d_gen directions — binary design 中两向量近乎反平行，three-way
1218	    design 中角度明显更大（~68°），neutral cluster 位于不同位置。'
1219	  analysis: '三方 design 实质性打破 d_gen=-d_syc 退化（cosine 0.71→0.38），额外提升 WRR 2.8pp。 作为
1220	    P2 实验，结果支撑但非必需——S1 rank-based R2 已足够好，三方 design 可作为 future work 的改进方向报告。回应 Reviewer
1221	    Concern 4。
1222	
1223	    '
1224	- name: continuous_probe_baseline
1225	  plan_id: exp-014
1226	  description: 'Continuous Probe Baseline，logistic regression 概率值作为 reward 信号， 隔离"方向性
1227	    vs 连续性"的贡献。
1228	
1229	    '
1230	  expected_results:
1231	    final_nof_mean: 23.8
1232	    final_nof_std: 1.9
1233	    final_nof_seeds:
1234	    - 22.1
1235	    - 23.6
1236	    - 25.7
1237	    final_wrr_mean: 49.2
1238	    final_wrr_std: 1.6
1239	    final_wrr_seeds:
1240	    - 47.8
1241	    - 49.1
1242	    - 50.7
1243	    final_rc_auc_mean: 0.75
1244	    final_rc_auc_std: 0.02
1245	    probe_calibration_ece: 0.043
1246	    mt_bench: 7.7
1247	    mmlu: 65.0
1248	    dc_grpo_vs_continuous_nof_pp: 7.9
1249	    dc_grpo_vs_continuous_wrr_pp: 5.1
1250	    p_dc_vs_continuous_nof: 0.014
1251	    gpu_hours_actual: 18
1252	  result_rationale: 'Continuous Probe（NoF 23.8%）显著优于 Binary Probe（27.5%），证明连续信号确实比
1253	    二元信号提供更好的梯度。但 DC-GRPO（15.9%）仍以 7.9pp 显著超越 Continuous Probe （p=0.014）——这是方向几何 vs
1254	    纯连续性的决定性对比。为什么连续概率不如方向投影？ (1) Logistic regression 概率是一维标量（sycophancy probability），方向投影是高维
1255	    激活空间中的有符号距离，保留了方向信息（正 = sycophantic direction, 负 = genuine direction）；(2) Probe
1256	    概率是 post-hoc 从学到的权重计算的，方向投影直接利用了 contrastive pairs 定义的几何结构，更 aligned with 训练目标；(3)
1257	    Probe calibration （ECE 0.043）虽合理但非完美——概率值的绝对尺度可能不准确，而方向投影的相对排序 更可靠。这个 7.9pp 差距直接证明了
1258	    paper 的核心 claim：方向几何（而非仅连续性） 是 DC-GRPO 优势的关键因素。
1259	
1260	    '
1261	  tables:
1262	  - name: 'Table 23: Continuous Probe vs Binary Probe vs DC-GRPO'
1263	    headers:
1264	    - Method
1265	    - NoF (%)
1266	    - WRR (%)
1267	    - RC-AUC
1268	    - Signal Type
1269	    rows:
1270	    - - Binary Probe
1271	      - 27.5 ± 2.3
1272	      - 46.3 ± 1.8
1273	      - '0.71'
1274	      - Binary {0,1}
1275	    - - Continuous Probe
1276	      - 23.8 ± 1.9
1277	      - 49.2 ± 1.6
1278	      - '0.75'
1279	      - Scalar probability [0,1]
1280	    - - DC-GRPO
1281	      - 15.9 ± 1.6
1282	      - 54.3 ± 1.2
1283	      - '0.84'
1284	      - Signed directional projection ℝ
1285	  - name: 'Table 24: Isolating Continuity vs Directionality'
1286	    headers:
1287	    - Comparison
1288	    - Δ NoF (pp)
1289	    - p-value
1290	    - Attribution
1291	    rows:
1292	    - - Binary → Continuous
1293	      - −3.7
1294	      - '0.038'
1295	      - Continuity effect (scalar > binary)
1296	    - - Continuous → DC-GRPO
1297	      - −7.9
1298	      - '0.014'
1299	      - Directionality effect (geometric > scalar)
1300	    - - Binary → DC-GRPO
1301	      - −11.6
1302	      - '0.008'
1303	      - Combined effect
1304	  figures_description:
1305	  - 'Fig 14: 信号类型阶梯图 — Binary (离散) → Continuous (标量连续) → Directional (向量连续). 每一步的
1306	    NoF 改进标注在箭头上。连续性贡献 3.7pp，方向性额外贡献 7.9pp——方向性的边际贡献是连续性的 2.1 倍。'
1307	  analysis: '这是 paper 中最重要的 ablation 之一。Binary→Continuous 的 3.7pp 证明连续信号有价值， 但 Continuous→DC-GRPO
1308	    的 7.9pp（2.1× 更大）决定性地证明方向几何才是主要驱动力。 直接回应 Reviewer concern："如果 continuous probe
1309	    ≈ DC-GRPO，则优势仅来自连续性"—— 事实是差距显著（p=0.014），方向几何不可被连续标量替代。
1310	
1311	    '
1312	- name: reward_weight_sensitivity
1313	  plan_id: exp-015
1314	  description: '5 组 (w1, w2, w3) 配置的 reward weight 敏感度分析，从 exp-002 step 4000 checkpoint
1315	    分叉短程训练。
1316	
1317	    '
1318	  expected_results:
1319	    config_default:
1320	      weights: w1=0.3, w2=0.2, w3=0.5
1321	      nof: 16.2
1322	      wrr: 53.8
1323	      rc_auc: 0.83
1324	    config_r1r3_reversed:
1325	      weights: w1=0.5, w2=0.2, w3=0.3
1326	      nof: 15.4
1327	      wrr: 52.1
1328	      rc_auc: 0.82
1329	    config_r1_dominant:
1330	      weights: w1=0.6, w2=0.1, w3=0.3
1331	      nof: 17.3
1332	      wrr: 49.6
1333	      rc_auc: 0.79
1334	    config_equal:
1335	      weights: w1=0.33, w2=0.33, w3=0.34
1336	      nof: 16.5
1337	      wrr: 52.4
1338	      rc_auc: 0.82
1339	    config_r3_dominant:
1340	      weights: w1=0.1, w2=0.1, w3=0.8
1341	      nof: 18.1
1342	      wrr: 44.3
1343	      rc_auc: 0.73
1344	    config_r2_enhanced:
1345	      weights: w1=0.2, w2=0.4, w3=0.4
1346	      nof: 16.8
1347	      wrr: 51.7
1348	      rc_auc: 0.81
1349	    nof_range_pp: 2.7
1350	    nof_range_excl_r3_dominant_pp: 1.9
1351	    wrr_range_pp: 9.5
1352	    rc_auc_range: 0.1
1353	    best_config: w1=0.5, w2=0.2, w3=0.3 (R1/R3 reversed)
1354	    gpu_hours_actual: 14
1355	  result_rationale: 'NoF 在 6 组配置间仅变化 2.7pp（15.4-18.1%），证明 DC-GRPO 对权重选择高度鲁棒。 排除极端
1356	    R3-dominant 配置后，range 仅 1.9pp。这回应了 "weights unjustified" 的 reviewer concern——虽然默认权重不是唯一选择，但任何合理配置都显著优于
1357	    baselines。 模式分析：(1) R1 权重 ≥0.2 时 NoF 稳定在 15-17%，说明方向信号只需 minimal 权重 即可生效；(2) R3-dominant
1358	    (w1=0.1) 的 NoF 18.1% 最差但仍远优于 R3-only 34.7%， 说明即使极低的 R1 权重也显著改善纯行为方法；(3) R1-dominant
1359	    (w1=0.6) 的 WRR 49.6% 最低（但仍优于 R3-only 42.1%），因为过高的 R1 权重导致 representation-level
1360	    优化 dominate 行为 coherence；(4) R1/R3 reversed (w1=0.5) 实际 NoF 最低（15.4%）， 但 WRR 略低——说明可以根据应用需求调整
1361	    sycophancy/revision 的偏好。Default 配置 (w1=0.3, w2=0.2, w3=0.5) 在 NoF-WRR 综合表现（RC-AUC
1362	    0.83）上接近最优， justified 作为合理的默认选择。
1363	
1364	    '
1365	  tables:
1366	  - name: 'Table 25: Reward Weight Sensitivity Analysis'
1367	    headers:
1368	    - Config
1369	    - w1 (R1)
1370	    - w2 (R2)
1371	    - w3 (R3)
1372	    - NoF (%)
1373	    - WRR (%)
1374	    - RC-AUC
1375	    rows:
1376	    - - Default
1377	      - '0.30'
1378	      - '0.20'
1379	      - '0.50'
1380	      - '16.2'
1381	      - '53.8'
1382	      - '0.83'
1383	    - - R1/R3 reversed
1384	      - '0.50'
1385	      - '0.20'
1386	      - '0.30'
1387	      - '15.4'
1388	      - '52.1'
1389	      - '0.82'
1390	    - - R1 dominant
1391	      - '0.60'
1392	      - '0.10'
1393	      - '0.30'
1394	      - '17.3'
1395	      - '49.6'
1396	      - '0.79'
1397	    - - Equal
1398	      - '0.33'
1399	      - '0.33'
1400	      - '0.34'
1401	      - '16.5'
1402	      - '52.4'
1403	      - '0.82'
1404	    - - R3 dominant
1405	      - '0.10'
1406	      - '0.10'
1407	      - '0.80'
1408	      - '18.1'
1409	      - '44.3'
1410	      - '0.73'
1411	    - - R2 enhanced
1412	      - '0.20'
1413	      - '0.40'
1414	      - '0.40'
1415	      - '16.8'
1416	      - '51.7'
1417	      - '0.81'
1418	  - name: 'Table 26: Sensitivity Summary'
1419	    headers:
1420	    - Metric
1421	    - Min
1422	    - Max
1423	    - Range
1424	    - Range (excl R3-dom)
1425	    rows:
1426	    - - NoF (%)
1427	      - '15.4'
1428	      - '18.1'
1429	      - 2.7pp
1430	      - 1.9pp
1431	    - - WRR (%)
1432	      - '44.3'
1433	      - '53.8'
1434	      - 9.5pp
1435	      - 4.2pp
1436	    - - RC-AUC
1437	      - '0.73'
1438	      - '0.83'
1439	      - '0.10'
1440	      - '0.04'
1441	  figures_description:
1442	  - 'Fig 15a: Parallel coordinates plot — 6 configurations × 3 metrics. 除 R3-dominant
1443	    外，所有配置的 NoF 线紧密聚集在 15-17% 区间。'
1444	  - 'Fig 15b: NoF vs WRR scatter plot with 6 config points labeled. 形成一个紧凑的 cluster（excl
1445	    R3-dominant outlier），default 配置位于 Pareto 前沿附近。'
1446	  analysis: NoF range 2.7pp 在 best tier [0, 4] 内，证明方法鲁棒。核心洞见：R1 权重 ≥0.2 即可 有效激活方向
1447	    reward 的贡献——这意味着实践者无需精细调参。R3-dominant 的退化模式 （NoF 最差 + WRR 最低）直接论证了 R1 的不可替代性：即使将绝大部分权重给行为
1448	    reward， 仍不如更均衡地使用方向信号。Default 配置被 empirically justified 为接近 Pareto-optimal。
1449	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e40530f-538a-4881-9ade-9731bfd7f1f8",
  "isSidechain": true,
  "promptId": "b15924b2-f989-4b43-bb76-10033f782e77",
  "agentId": "ad9c0adca4745aec1",
  "type": "user",
  "uuid": "e49ac679-0cc7-4056-a252-2a8c2397d18d",
  "sourceToolAssistantUUID": "5e40530f-538a-4881-9ade-9731bfd7f1f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-18T13:44:37.703Z_

I now have comprehensive context. Let me write the review.

---

### Summary

The paper proposes DC-GRPO, a training method that extracts a linear sycophancy direction (d_syc) from the policy model's activation space using contrastive pairs, then uses the signed projection onto this direction as a continuous reward component (R1) within GRPO, alongside a rank-based contrastive reward (R2) and an NLI behavioral reward (R3). The method targets the "double-bind" where anti-sycophancy training suppresses both sycophantic capitulation and genuine belief revision. On SYCON Bench with Qwen3-8B, DC-GRPO reduces NoF by 18.8pp over R3-only GRPO while improving WRR by 12.2pp. A continuous probe baseline isolates 7.9pp of the gain as attributable to directional geometry rather than signal continuity. Cross-model validation on Llama-3-8B shows the direction phenomenon is independently recoverable (AUROC 0.832).

---

### Strengths

1. **Clear problem articulation with a well-defined gap.** The "double-bind" framing is precise and operationally meaningful: behavioral signals cannot distinguish capitulation from revision because the two are surface-identical. This is not a manufactured problem. The sycophancy literature (TRUTH DECAY, SYCON Bench) documents it, and the paper's own ACT baseline (WRR 36.8% < vanilla 37.4%) demonstrates it concretely.

2. **Transparent positioning of methodological lineage (revised version).** Unlike the first dream iteration (which omitted RepE/CCS/Activation Addition entirely), this version explicitly states in both the Introduction and Related Work that d_syc extraction is "a specific application of RepE-style directional decomposition." The paper_framing.md confirms this was a deliberate revision after the D008 dream review. This honesty is commendable and necessary. The novelty claim is correctly scoped to the use of directional projection as a continuous training-time GRPO reward, not the direction extraction itself.

3. **The continuity-vs-directionality ablation is the paper's strongest novelty argument.** The Binary Probe to Continuous Probe to DC-GRPO decomposition (Table in Section 4.4) is well-designed. The 3.7pp gain from continuity and 7.9pp from directionality (p=0.014) directly addresses the most natural objection ("isn't this just a continuous probe?"). This ablation was absent from the first dream and was added in response to reviewer feedback, which shows good scientific responsiveness.

4. **Turn-depth interaction is a genuine finding.** DC-GRPO is the only method whose performance improves at deeper turns (NoF: 22.1% at turn 2 to 8.7% at turn 4+). All baselines degrade. The interaction effect (p=0.008) is the strongest empirical evidence that representation-level rewards capture something qualitatively different from behavioral rewards in multi-turn settings. This result is not trivially predicted by the method design and constitutes an independently interesting empirical contribution.

5. **Comprehensive baseline coverage.** Six methods (Vanilla, ACT, R3-only, Binary Probe, Continuous Probe, DC-GRPO) form a logical hierarchy that systematically isolates design decisions. The inclusion of both Binary and Continuous probe baselines, in particular, prevents conflation of signal type effects.

6. **Statistical reporting is above average.** Bootstrap CIs on AUROC, paired t-tests across 3 seeds with explicit p-values, 5-fold CV for direction extraction, and standard deviations on all main results. The p=0.014 for the key DC-GRPO vs. Continuous Probe comparison is honestly close to the significance boundary rather than suspiciously small, which increases credibility.

---

### Weaknesses

1. **The conceptual distance from CRAFT is insufficiently argued (Major).** CRAFT applies hidden-state rewards to GRPO for safety alignment. DC-GRPO applies hidden-state rewards to GRPO for sycophancy. The Related Work dismisses CRAFT in one sentence as using "domain-general prototype clustering rather than concept-specific directions," but this undersells the similarity. Both methods: (a) extract activation-space representations, (b) convert them into GRPO reward signals, (c) combine them with behavioral rewards. The distinction between "prototype clustering" and "directional projection" is a design choice within the same framework, not a different framework. The paper needs a dedicated paragraph comparing the CRAFT reward formulation with R1, explaining why directional projection is preferable to prototype distance for the sycophancy-revision distinction specifically, ideally with an empirical comparison or at least a formal argument about why the sycophancy domain requires direction rather than clusters.

2. **The novelty, honestly assessed, is an application paper (Major).** The paper combines three existing ideas: (a) RepE-style contrastive direction extraction (Zou et al., 2023), (b) hidden-state GRPO rewards (CRAFT), and (c) NLI behavioral rewards for sycophancy ("Pressure, What Pressure?"). Each component is from prior work. The combination is reasonable and the results are strong, but the intellectual advance is integration and domain application rather than a new methodological principle. For a top venue (~25% acceptance), the bar requires either a genuinely new idea or exceptionally strong empirical results that reshape understanding. The 7.9pp directionality gap is meaningful but not overwhelming, especially on 3 seeds.

3. **Missing related work: DPO/RLHF-based sycophancy interventions (Major).** The Related Work covers behavioral GRPO and activation-level methods but omits the substantial body of work on DPO-based sycophancy reduction (e.g., anthropic-style RLHF with honesty-focused preference data, DPO with sycophancy-contrastive pairs). These are the most commercially deployed anti-sycophancy methods. Their omission makes the Related Work feel selectively constructed to advantage DC-GRPO's framing. Even if DC-GRPO targets a different mechanism, the paper should acknowledge and position against these approaches.

4. **Missing related work: Inference-time activation steering for sycophancy (Moderate).** Activation Addition is cited for inference-time behavior modification, but the paper does not discuss why training-time integration (DC-GRPO) is preferable to simply applying d_syc as an inference-time intervention (as Activation Addition would prescribe). This is the most obvious alternative approach: extract d_syc, subtract it at inference time, done. The absence of this comparison or even discussion is a significant gap in positioning.

5. **"Sycophancy Is Not One Thing" is cited in the first dream's Related Work but absent from this version (Moderate).** This paper directly addresses the decomposition of sycophancy into behaviorally distinct subtypes with separable activation signatures. It is perhaps the most directly relevant prior work for the claim that sycophancy has directionally distinct internal representations. Its omission weakens the theoretical grounding.

6. **Knowledge-Prediction Gap and Sycophantic Anchors are absent (Moderate).** The first dream version cites both in the "Mechanistic interpretability" paragraph. These works directly support the premise that models "know" when they are being sycophantic. Their removal from the current version leaves the masked sycophancy analysis (Section 5.4.2) without proper literature grounding. The 9.3% masked sycophancy rate is essentially a replication of the Knowledge-Prediction Gap phenomenon in a new domain; not citing this prior work is a missed opportunity and a positioning failure.

7. **Three seeds is thin for significance claims (Moderate).** The DC-GRPO vs. Continuous Probe comparison (the key novelty-supporting result) has p=0.014 on 3 seeds. A paired t-test on 3 observations has 2 degrees of freedom, making the t-distribution extremely heavy-tailed. The effective statistical power is low. While I do not dispute the result, a reviewer at a top venue could reasonably argue that this key comparison needs 5+ seeds to be convincing. The paper should at minimum acknowledge this limitation and discuss effect sizes (Cohen's d).

8. **RC-AUC is a custom metric without external validation (Minor-to-Moderate).** The paper's strongest composite result (0.84 vs. 0.65 for R3-only) uses a metric invented by the authors. While it is formally defined and the NoF/WRR components are standard, the specific aggregation into an AUC curve is novel. Without correlation to human judgment or adoption by other work, this metric carries less weight than the individual NoF and WRR numbers.

---

### Questions for Authors

1. Why not compare against inference-time activation steering (subtracting scaled d_syc at generation time, per Activation Addition)? This is the zero-training-cost alternative to DC-GRPO and its absence is conspicuous.

2. What is the overlap between DC-GRPO's R1 formulation and CRAFT's hidden-state reward? Can you provide a formal comparison showing where they diverge in the reward computation?

3. The masked sycophancy finding (9.3%) echoes the Knowledge-Prediction Gap literature (13-29% representation-behavioral disagreement). Why are these works not cited? Is your finding a replication, extension, or contradiction of that prior result?

4. Have you considered "Sycophancy Is Not One Thing" as prior work? That paper's finding of separable activation signatures for sycophancy subtypes directly supports your Claim 1 and should be discussed.

5. The p-value for DC-GRPO vs. Continuous Probe is 0.014 on 3 seeds (2 df). What is the effect size (Cohen's d)? Would the result hold with a permutation test or bootstrap comparison that does not assume normality?

6. For the multi-turn Related Work paragraph: what specific prior multi-turn alignment methods exist, and how does DC-GRPO compare? The current paragraph describes challenges but cites no specific methods, making it read more like motivation than related work.

7. What would happen if you applied d_syc as an inference-time steering vector to the R3-only trained model? Would this close the gap with DC-GRPO, suggesting the direction is useful but the training integration is not necessary?

---

### Minor Issues

- The R2 reward formulation is underspecified in the paper. "Rank-based contrastive reward" is described at a high level but the actual computation (ranking criterion, reward mapping) is not given in sufficient detail for reproduction.
- The paper mentions "Pressure, What Pressure?" but all citations are informal (paper titles in text, no \cite{} references). For any real submission, a proper bibliography is mandatory.
- The Multi-turn alignment paragraph in Related Work cites no specific prior methods by name, only describing the challenge space. This paragraph should either cite specific multi-turn alignment work (e.g., multi-turn RLHF, dialogue-specific DPO) or be merged into the introduction as motivation.
- Table 8 (main results): MT-Bench and MMLU do not show standard deviations for ACT and Vanilla, while other methods do. Inconsistent reporting.
- The direction extraction uses the simple mean difference vector (Equation 1), but the first dream version mentions PCA of the difference vectors. The two versions disagree on the extraction procedure. Clarify which is used and whether they differ in practice.

---

### Preliminary Score and Confidence

**Score: 4/6 (Weak Accept)**

**Confidence: 4/5 (High)**

**Rationale:** The paper addresses a real and well-motivated problem. The experimental design, particularly the continuity-vs-directionality ablation and the turn-depth interaction analysis, is thorough and above average for the target venue. The transparent positioning of d_syc as a RepE application (corrected from the first draft) is honest and appropriate.

However, the core contribution is an integration of existing techniques (RepE direction extraction + CRAFT-style hidden-state GRPO rewards + NLI behavioral rewards) applied to a specific domain. The conceptual distance from CRAFT is not convincingly argued. Several important related works are missing (Knowledge-Prediction Gap, Sycophantic Anchors, "Sycophancy Is Not One Thing," inference-time steering alternatives, DPO-based sycophancy methods). The statistical evidence for the key directionality claim rests on 3 seeds with p=0.014, which is adequate but not robust. The custom RC-AUC metric is not externally validated.

The paper is above the reject threshold due to the quality of experiments and the genuine turn-depth finding, but below clear accept because the novelty is incremental and the related work has meaningful gaps. Addressing the CRAFT comparison, adding the missing citations, and running 5+ seeds on the key comparison would move this toward a 5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e49ac679-0cc7-4056-a252-2a8c2397d18d",
  "isSidechain": true,
  "agentId": "ad9c0adca4745aec1",
  "requestId": "req_011CbA8eUcnmgfZeB6oGkqUe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "850a67b7-41fb-4006-8f8c-ad7b624132c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "bd6711dc-0dd5-403d-bdcb-8496728be70f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5oM4axgwmCFgYKgP7HAH2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28794,
      "cache_read_input_tokens": 42419,
      "output_tokens": 3029,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 28794
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3029,
          "cache_read_input_tokens": 42419,
          "cache_creation_input_tokens": 28794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 28794,
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
