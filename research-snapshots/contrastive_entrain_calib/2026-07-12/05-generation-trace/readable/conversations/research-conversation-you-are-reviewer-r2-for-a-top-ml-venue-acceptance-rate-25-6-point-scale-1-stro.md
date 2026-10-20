# Research conversation: You are Reviewer R2 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a3fa95b4ad97e525f.jsonl`
- **Structured JSON:** [`ef86fbda082a2bc85597.json`](../../sessions/ef/ef86fbda082a2bc85597.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

43 recorded events

### User

_source line 1 · 2026-05-18T13:55:53.143Z_

You are Reviewer R2 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus: **novelty, significance, positioning, and related work**.

## Paper Summary

**Title**: "Do Sycophancy Directions Transfer to Training Rewards? Boundary Conditions of Representation-Level Signals for Multi-Turn Belief Revision"

**Core idea**: Investigates whether linear directions in activation space (d_syc) distinguishing sycophantic from genuine responses can serve as training reward signals via Direction-Contrastive GRPO (DC-GRPO). The paper frames itself as a "boundary conditions" study with a **negative result**: DC-GRPO does not significantly outperform behavioral-reward-only training (R3-only).

## Paper Structure

**Abstract** (~250 words): States the hypothesis, method, and negative result clearly. Key numbers: AUROC 0.801, DC-GRPO vs R3-only p=0.187, continuous probe matches DC-GRPO (p=0.448), direction drift to cosine 0.66, R1-R3 disagreement 3.4%.

**Introduction** (Section 1):
- Multi-turn sycophancy as "commitment decay" (up to 47% accuracy degradation)
- Double-bind problem: training against sycophancy suppresses legitimate belief revision
- Existing approaches: NLI behavioral (surface level) vs ACT (undifferentiated activation consistency)
- RepE background: linear directions encode semantic concepts, natural extension to use as rewards
- CRAFT framework for safety using prototype clustering
- Paper's goal: test if directional geometry provides independent training value
- Clear negative answer + subsidiary findings listed as bullet points
- Contributions: (1) d_syc exists with AUROC 0.801 and layer-wise emergence, (2) DC-GRPO ≠ significant over R3-only, (3) direction drift problem, (4) low R1-R3 disagreement, (5) ACT < targeted methods

**Related Work** (Section 2):
- Multi-turn sycophancy: TRUTH DECAY, SYCON Bench, "Pressure, What Pressure?"
- Representation Engineering: RepE, CCS, Activation Addition, linear representation hypothesis
- Representation-level training: ACT, CRAFT, Linear Probe Penalties
- Calibration and evaluation: SycophancyEval, SYCON Bench, Knowledge-Prediction Gap (13-29% disagreement in factual QA)

**Method** (Section 3): Direction extraction via PCA on contrastive activation differences, DC-GRPO with R1+R2+R3 rewards, recalibration mechanism.

**Experiments** (Section 4): 15 experiments covering calibration quality, main comparison, baselines (R3-only, ACT-style, binary probe, continuous probe), stability, disagreement analysis, ablations, turn depth, cross-model transfer, three-way design, weight sensitivity.

**Discussion** (Section 5): "The direction is real but redundant." Three reasons for failure: low SNR, direction drift, R1-R3 correlation. Undifferentiated vs targeted interventions. Implications for RepE-as-reward (need high discriminability ≫0.80 + stability). Cross-model structure (layer-wise pattern generalizes, specific direction doesn't).

**Limitations**: 8B models only, 3 seeds (low power), 200 calibration pairs, multi-turn dialogue only, fixed recalibration threshold.

**Conclusion**: Negative result + boundary conditions.

## Key Claims
1. A sycophancy direction d_syc exists in Qwen3-8B activation space (AUROC 0.801)
2. DC-GRPO does not significantly outperform R3-only behavioral reward
3. A simpler continuous probe achieves equivalent/slightly better results
4. Direction drift is a fundamental obstacle for RepE-as-reward during policy gradient training
5. R1-R3 disagreement is too low (3.4%) to justify representation-level diagnostics
6. Targeted methods outperform undifferentiated ACT-style

## Your Task

Provide a detailed review focusing on:

1. **Novelty assessment**: How novel is this work? Is the negative result itself a meaningful contribution? Does the "boundary conditions" framing add sufficient value?
2. **Significance**: Would the ML community benefit from this paper? Does it change how people think about RepE-as-reward?
3. **Related work completeness**: Are important baselines/prior works missing? Is positioning accurate?
4. **Framing and narrative**: Is the paper well-framed? Is the negative result convincingly argued? Does the story hold together?
5. **Specific weaknesses** (numbered list).
6. **Specific strengths** (numbered list).
7. **Questions for authors** (numbered list).
8. **Overall assessment**: Score (1-6) with justification.

Be thorough and critical. Evaluate whether this paper's contribution meets the bar for a top ML venue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "4d1cf5a2-a544-4479-b5fd-1fc57057744e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T13:55:53.146Z_

```json
{
  "parentUuid": "4d1cf5a2-a544-4479-b5fd-1fc57057744e",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
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
  "uuid": "22cc3b9c-7818-4722-b892-9d5f59dfafc9",
  "timestamp": "2026-05-18T13:55:53.146Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T13:55:57.426Z_



I'll start by reading the full paper and related project files to provide a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22cc3b9c-7818-4722-b892-9d5f59dfafc9",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9cc6ZRFBiU6L3eDRRk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ceb9ec5-9997-41c9-a792-b8b54517ddad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPz83tFknW86NwTn8BKt7P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8317,
      "cache_read_input_tokens": 8255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8317,
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

_source line 4 · 2026-05-18T13:55:57.900Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DaaHsb9256RrA12GGftDUC`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ceb9ec5-9997-41c9-a792-b8b54517ddad",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9cc6ZRFBiU6L3eDRRk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9907c2f3-8132-4658-9250-258f2f66accf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPz83tFknW86NwTn8BKt7P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8317,
      "cache_read_input_tokens": 8255,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8317
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 8255,
          "cache_creation_input_tokens": 8317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8317,
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

_source line 5 · 2026-05-18T13:55:57.903Z_

<details><summary>↩ Tool result · `toolu_01DaaHsb9256RrA12GGftDUC`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_get_project_overview"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9907c2f3-8132-4658-9250-258f2f66accf",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "30923401-166c-4683-b7fb-66dec1f9635a",
  "sourceToolAssistantUUID": "9907c2f3-8132-4658-9250-258f2f66accf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T13:56:01.647Z_



Let me read the full paper and supporting project files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30923401-166c-4683-b7fb-66dec1f9635a",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9cxe5gbZaRvH96idnm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45f3500a-2db0-4ee6-b208-856346a6d067",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cu2jkbMfZVwPgHEcuqd2mG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 16572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 7 · 2026-05-18T13:56:02.590Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_018gZjeNW8iRtYEBqnuiRWTh`</summary>

```json
{
  "project": "contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45f3500a-2db0-4ee6-b208-856346a6d067",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9cxe5gbZaRvH96idnm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfc57b72-00fb-4e77-bcad-f65d7d81fc6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cu2jkbMfZVwPgHEcuqd2mG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 16572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 8 · 2026-05-18T13:56:02.601Z_

<details><summary>↩ Tool result · `toolu_018gZjeNW8iRtYEBqnuiRWTh`</summary>

```text
{"result":"# 项目 contrastive_entrain_calib 概况\n\n## 实验状态\n暂无实验记录\n\n## 最新报告\n（尚未生成）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfc57b72-00fb-4e77-bcad-f65d7d81fc6b",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "70b7ab47-e654-44c7-911d-9b5ce43b074a",
  "sourceToolAssistantUUID": "dfc57b72-00fb-4e77-bcad-f65d7d81fc6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T13:56:04.145Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FtRsZ2CzQGi8YZNji5QJoB`</summary>

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
  "parentUuid": "70b7ab47-e654-44c7-911d-9b5ce43b074a",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9cxe5gbZaRvH96idnm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89798c39-8643-465e-80ef-ba9cdf0c2d85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cu2jkbMfZVwPgHEcuqd2mG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 16572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 10 · 2026-05-18T13:56:04.157Z_

<details><summary>↩ Tool result · `toolu_01FtRsZ2CzQGi8YZNji5QJoB`</summary>

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
  "parentUuid": "89798c39-8643-465e-80ef-ba9cdf0c2d85",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "02376f98-1321-412f-a042-66d8c35fd38b",
  "sourceToolAssistantUUID": "89798c39-8643-465e-80ef-ba9cdf0c2d85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T13:56:04.232Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019byEH7UbLq5ti1VR7WtWAB`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02376f98-1321-412f-a042-66d8c35fd38b",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9cxe5gbZaRvH96idnm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "356507d2-d293-4495-845a-a34e55811919",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cu2jkbMfZVwPgHEcuqd2mG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1448,
      "cache_read_input_tokens": 16572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1448,
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

_source line 12 · 2026-05-18T13:56:04.242Z_

<details><summary>↩ Tool result · `toolu_019byEH7UbLq5ti1VR7WtWAB`</summary>

```text
artifacts/_project/report/post_mvp_experiment_skeleton.md
artifacts/post_mvp_experiment_skeleton.md
docs/IDEA_BRIEF.md
artifacts/dream_reports/dream_20260518T110318/best/paper_framing.md
artifacts/dream_reports/dream_20260518T110318/median/paper_framing.md
artifacts/dream_reports/dream_20260518T110318/worst/paper_framing.md
artifacts/dream_reports/dream_20260518T110318/best/review_report.md
artifacts/dream_reports/dream_20260518T110318/median/review_report.md
artifacts/dream_reports/dream_20260518T110318/worst/review_report.md
paper_framing.md
ROADMAP.md
artifacts/dream_reports/dream_20260518T125925/best/paper_framing.md
artifacts/dream_reports/dream_20260518T125925/median/paper_framing.md
artifacts/dream_reports/dream_20260518T125925/worst/paper_framing.md
.claude/sessions/agent_cbf2326f/CLAUDE.md
.claude/sessions/agent_cbf2326f/AGENTS.md
.claude/sessions/reviewer_35225640/CLAUDE.md
.claude/sessions/reviewer_35225640/AGENTS.md
.claude/CLAUDE.md
AGENTS.md
.claude/sessions/director_a2ca15c2/CLAUDE.md
.claude/sessions/director_a2ca15c2/AGENTS.md
artifacts/dream_reports/dream_20260518T125925/best/review_report.md
artifacts/dream_reports/dream_20260518T125925/median/review_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "356507d2-d293-4495-845a-a34e55811919",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "87e4697a-4f8c-4bd8-a4f5-4e1e94f24c91",
  "sourceToolAssistantUUID": "356507d2-d293-4495-845a-a34e55811919",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T13:56:07.475Z_

<details open><summary>🔧 Tool call — Read · `toolu_014oFxgWs4btg14eLpch1T7a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87e4697a-4f8c-4bd8-a4f5-4e1e94f24c91",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9dRrwLR6TKrV15uTMz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23538604-7851-419d-b982-227d63b107c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANxcgiaxXMwynoD6wQ4rGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 975,
      "cache_read_input_tokens": 18020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 975,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 14 · 2026-05-18T13:56:07.763Z_

<details><summary>↩ Tool result · `toolu_014oFxgWs4btg14eLpch1T7a`</summary>

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
  "parentUuid": "23538604-7851-419d-b982-227d63b107c0",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "551b8173-7aa8-4401-ae19-1a193e439998",
  "sourceToolAssistantUUID": "23538604-7851-419d-b982-227d63b107c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T13:56:08.014Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HHgyUCt9J7D3DwCAdJqhKg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "551b8173-7aa8-4401-ae19-1a193e439998",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9dRrwLR6TKrV15uTMz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9bbc4dc2-431f-4358-9ba4-0394eb2768a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ANxcgiaxXMwynoD6wQ4rGe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 975,
      "cache_read_input_tokens": 18020,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 975
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 198,
          "cache_read_input_tokens": 18020,
          "cache_creation_input_tokens": 975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 975,
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

_source line 16 · 2026-05-18T13:56:08.022Z_

<details><summary>↩ Tool result · `toolu_01HHgyUCt9J7D3DwCAdJqhKg`</summary>

```text
1	# Paper Framing — contrastive_entrain_calib
2	
3	## Target Venue
4	- Primary: **EACL 2027** via ARR August 2026 cycle
5	- Deadline: **August 3, 2026** (submission), October 11, 2026 (commitment)
6	- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)
7	- Timeline: ~11 weeks from MVP completion (May 18 → Aug 3)
8	
9	## Core Claims (3 条, 可证伪)
10	
11	1. **Directional discriminability**: The policy model's own activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision in multi-turn dialogue, with signal emerging at mid-layers (L16-19) through model-internal factual assessment rather than surface text features.
12	   - *Evidence needed*: AUROC on style-controlled data (v2.1 expanded), layer progression analysis, transfer tests
13	   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence
14	
15	2. **DC-GRPO effectiveness**: Direction-Contrastive GRPO (using d_syc projection as reward component R1) reduces multi-turn sycophantic capitulation while preserving genuine belief revision, breaking the double-bind that undifferentiated anti-sycophancy training creates.
16	   - *Evidence needed*: Warranted Revision Rate + Unwarranted Capitulation Rate on SYCON Bench / SycophancyEval, compared to R3-only and ACT baselines
17	   - *Pass criterion*: DC-GRPO achieves lower NoF (capitulation) than R3-only AND higher warranted revision rate
18	
19	3. **Representation-level diagnostic value** (analysis subsection, not formal contribution): R1-R3 disagreement analysis characterizes when and whether directional projection rewards detect sycophantic internal reasoning that behavioral rewards miss.
20	   - *Evidence needed*: R1-R3 disagreement frequency analysis, qualitative examples if > 5%
21	   - *Framing*: Empirical characterization of representation-level signal utility, reported honestly regardless of effect size. Not listed as a top-level contribution bullet.
22	
23	## Story Spine
24	
25	**Problem**: LLMs face a "double-bind" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes "the user is right, I should revise" from "the user is pressuring me, I should resist."
26	
27	**Existing approaches & gaps**: Behavioral GRPO decomposition ("Pressure, What Pressure?") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.
28	
29	**Our framing**: Representation Engineering (Zou et al., 2023) established that linear directions in activation space encode high-level concepts. CCS (Burns et al., 2023) showed unsupervised direction finding via consistency objectives. Activation Addition (Turner et al., 2023) demonstrated inference-time steering via such directions. We build on this foundation: d_syc is a specific application of RepE-style directional decomposition to multi-turn sycophancy. The novelty is not the direction extraction itself, but its use as a continuous GRPO reward signal for training, enabling the optimization to directly target the internal mechanism of sycophancy rather than its surface manifestation. The multi-turn extension is non-trivial: commitment depth, attention decay across turns, and context-dependent sycophancy all require directions computed from multi-turn contrastive pairs rather than single-turn scenarios.
30	
31	**Headline result template**: "On SYCON Bench, DC-GRPO reduces multi-turn sycophantic capitulation (NoF) by X% relative to behavioral-only GRPO while improving warranted revision rate by Y%, demonstrating that representation-level rewards can break the sycophancy-revision double-bind."
32	
33	## Venue Fit Risks
34	
35	- **EACL fit**: Strong. Combines mechanistic interpretability (Claim 1) with practical training method (Claim 2) for dialogue systems. EACL values NLP-focused work with linguistic/cognitive grounding.
36	- **Reviewer concern 1 (novelty)**: "This is just RepE/CRAFT applied to sycophancy." Counter: (a) d_syc is explicitly positioned as a RepE application; the novelty is using it as a continuous GRPO reward signal, not the direction extraction itself; (b) multi-turn calibration with evidence-strength stratification and direction transfer are standalone contributions; (c) neither CRAFT nor RepE has been applied to the sycophancy-revision double-bind in training.
37	- **Reviewer concern 6 (RC-AUC custom metric)**: "Strongest results on self-invented metric." Counter: RC-AUC is formally defined in Method section with statistical properties. Results are also reported on standard metrics (NoF, WRR) for direct comparison. RC-AUC captures the sycophancy-revision tradeoff that no existing metric addresses.
38	- **Reviewer concern 2 (signal strength)**: "AUROC ~0.82 on style-controlled data is moderate." Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) expanding data and adding mixed evidence strength should tighten CI.
39	- **Reviewer concern 3 (scale)**: "Only Qwen3-8B." Counter: Budget constraint (200 H100-hr). If time/budget allows, add one more model family (e.g., Llama-3-8B). Cross-model direction transfer analysis partially addresses this.
40	- **Reviewer concern 4 (R2 degeneration)**: "d_gen = -d_syc in binary design." Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.
41	- **Reviewer concern 5 (practical utility)**: "Do models actually exhibit masked sycophancy at meaningful rates?" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.
42	
43	## Anticipated Reviewer Concerns & Experimental Responses
44	
45	| Concern | Experiment | Priority |
46	|---------|-----------|----------|
47	| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |
48	| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |
49	| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |
50	| Binary probe is enough (no need for directional decomposition) | Binary Probe Penalty baseline | P1 |
51	| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |
52	| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |
53	| Single model, doesn't generalize | Cross-model direction transfer analysis (if budget allows) | P2 |
54	| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |
55	| Binary probe is enough (continuity not directionality) | Continuous probe baseline (logistic regression prob as reward) | P1 |
56	| Reward weights unjustified | Reward weight sensitivity analysis (3-5 configs) | P1 |
57	| RC-AUC is custom, unvalidated | Formal definition + correlation with human judgments | P1 |
58	| Missing foundational references (RepE, CCS) | Expanded Related Work with 25+ references | P0 (writing) |
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bbc4dc2-431f-4358-9ba4-0394eb2768a0",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "414c8a4b-e64e-4821-b73b-a86b9ee943c9",
  "sourceToolAssistantUUID": "9bbc4dc2-431f-4358-9ba4-0394eb2768a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T13:56:12.979Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PPejFivxH7tFeY6yciZjWa`</summary>

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
  "parentUuid": "414c8a4b-e64e-4821-b73b-a86b9ee943c9",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9dhkAPvDffhtKf5Q6M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b671a3a-acbf-4b22-94a6-62eea1100404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFStWALFs1jFU5Hgot4Ve3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13994,
      "cache_read_input_tokens": 18995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13994,
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

_source line 18 · 2026-05-18T13:56:13.003Z_

<details><summary>↩ Tool result · `toolu_01PPejFivxH7tFeY6yciZjWa`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'contrastive_entrain_calib'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b671a3a-acbf-4b22-94a6-62eea1100404",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "b57f990c-fee7-43ff-9ab5-35649012cef3",
  "sourceToolAssistantUUID": "5b671a3a-acbf-4b22-94a6-62eea1100404",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T13:56:13.310Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0191ewQBJDiiWXDsFf7ezAeP`</summary>

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
  "parentUuid": "b57f990c-fee7-43ff-9ab5-35649012cef3",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9dhkAPvDffhtKf5Q6M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "216ffc9b-27df-4e4c-b6e7-82a8385ab6c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFStWALFs1jFU5Hgot4Ve3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13994,
      "cache_read_input_tokens": 18995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13994,
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

_source line 20 · 2026-05-18T13:56:13.319Z_

<details><summary>↩ Tool result · `toolu_0191ewQBJDiiWXDsFf7ezAeP`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'contrastive_entrain_calib'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "216ffc9b-27df-4e4c-b6e7-82a8385ab6c8",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "d48b19aa-42c7-4714-b3ae-31226e3aedc6",
  "sourceToolAssistantUUID": "216ffc9b-27df-4e4c-b6e7-82a8385ab6c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T13:56:15.289Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Gj3wMZnmJ9Svfpq4yG2ADv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d48b19aa-42c7-4714-b3ae-31226e3aedc6",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9dhkAPvDffhtKf5Q6M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1ef8f5c9-0ba1-46c0-9433-a954509e752d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFStWALFs1jFU5Hgot4Ve3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13994,
      "cache_read_input_tokens": 18995,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13994
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 18995,
          "cache_creation_input_tokens": 13994,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13994,
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

_source line 22 · 2026-05-18T13:56:15.294Z_

<details><summary>↩ Tool result · `toolu_01Gj3wMZnmJ9Svfpq4yG2ADv`</summary>

```text
1	---
2	dream_id: dream_20260518T125925
3	tier: best
4	overall_score: 4/6 Weak Accept
5	timestamp: 2026-05-18T13:47:45.837593+00:00
6	---
7	
8	# Dream Review Report — DC-GRPO for Breaking the Sycophancy-Revision Double-Bind
9	
10	**Paper**: Direction-Contrastive GRPO for Breaking the Sycophancy-Revision Double-Bind in Multi-Turn Dialogue
11	**Review mode**: Full (2 Reviewers, 4-step roundtable)
12	**Date**: 2026-05-18
13	
14	---
15	
16	## Roundtable Process
17	
18	- **R1** (Methods + Experiments): Preliminary 4/6 → Final 4/6
19	- **R2** (Novelty + Related Work): Preliminary 4/6 → Final 4/6
20	- **Cross-sharing**: Both reviewers read each other's reviews and responded. Strong convergence on key issues; minor disagreements on severity ratings.
21	
22	---
23	
24	## Consolidated Score: 4/6 (Weak Accept)
25	
26	**Confidence**: 4/5 (High)
27	
28	Both reviewers independently arrived at 4/6 and maintained after cross-reading. The paper addresses a real problem with above-average experimental rigor, but novelty is application-level and statistical evidence for the key claim is thin.
29	
30	---
31	
32	## Paper Summary
33	
34	The paper proposes DC-GRPO, which extracts a linear sycophancy direction (d_syc) from contrastive activation pairs in the policy model's hidden states and uses its projection as a continuous reward signal (R1) within GRPO, alongside rank-based contrastive (R2) and NLI behavioral (R3) rewards. On SYCON Bench with Qwen3-8B, DC-GRPO reduces sycophantic capitulation (NoF) by 18.8pp over R3-only GRPO while improving warranted revision rate (WRR) by 12.2pp, with negligible MT-Bench/MMLU degradation. Ablation isolates directional geometry as the primary driver (7.9pp over continuous probe, p=0.014). Cross-model validation on Llama-3-8B (AUROC 0.832) and R1-R3 disagreement analysis (14.2%, revealing 9.3% masked sycophancy) are also provided.
35	
36	---
37	
38	## Consensus Strengths
39	
40	### S1. Well-defined problem with clear formalization (R1, R2)
41	The "double-bind" framing is precise and operationally meaningful: behavioral signals cannot distinguish surface-identical capitulation from revision. This is not a manufactured problem; prior work (TRUTH DECAY, SYCON Bench) documents it, and the ACT baseline (WRR 36.8% < vanilla 37.4%) demonstrates it concretely.
42	
43	### S2. Principled continuity-vs-directionality ablation (R1, R2)
44	The Binary Probe → Continuous Probe → DC-GRPO comparison is the paper's strongest experimental contribution. Continuity accounts for 3.7pp NoF improvement (p=0.038), while directionality accounts for 7.9pp (p=0.014), a 2.1x ratio. This directly addresses the most natural objection ("isn't this just a continuous probe?").
45	
46	### S3. Turn-depth interaction is a genuine finding (R1, R2)
47	DC-GRPO is the only method whose NoF improves at deeper turns (22.1% at turn 2 → 8.7% at turn 4+). All baselines degrade. The interaction effect (p=0.008) is statistically meaningful and mechanistically interpretable: deeper commitment creates larger activation divergence, making the directional signal more informative. This is not trivially predicted and constitutes an independently interesting empirical contribution.
48	
49	### S4. Careful iterative data design (R1)
50	The v2.1 style-controlled calibration protocol (matched openings, citation patterns, confidence markers, length constraints) addresses a critical confound found in v1 (where trivial text differences yielded AUROC=1.0 from Layer 0). Layer 0 AUROC dropping to ~0.52 after style control while mid-layer AUROC remained strong is convincing evidence against surface confounds.
51	
52	### S5. Transparent methodological positioning (R1, R2)
53	The paper correctly frames d_syc extraction as a RepE application rather than claiming novelty in direction extraction itself. The novelty claim is appropriately scoped to using directional projection as a continuous training-time GRPO reward.
54	
55	### S6. Comprehensive baseline coverage (R2)
56	Six methods (Vanilla, ACT, R3-only, Binary Probe, Continuous Probe, DC-GRPO) form a logical hierarchy that systematically isolates design decisions. Each baseline serves a clear purpose in the argument structure.
57	
58	### S7. Direction stability is reassuring (R1)
59	Cosine similarity with initial d_syc stays at 0.881 after 8000 steps, held-out AUROC remains >0.86, and the recalibration mechanism (threshold 0.7) is never triggered. This addresses a natural concern about moving-target problems during policy gradient training.
60	
61	---
62	
63	## Consensus Weaknesses
64	
65	### W1. Statistical power critically low — 3 seeds [Major] (R1, R2)
66	**Both reviewers flagged independently.** All significance claims rest on paired t-tests with n=3 (2 degrees of freedom). The t-distribution is extremely heavy-tailed at 2 df; a single outlier seed can drive or eliminate significance. The key DC-GRPO vs. Continuous Probe comparison (p=0.014, the central novelty-supporting result) is particularly fragile. Standard deviations are suspiciously tight (e.g., NoF 15.9 ± 1.6 from 3 seeds). 
67	
68	**Recommendation**: Run 5+ seeds minimum (ideally 10). Report effect sizes (Cohen's d). Consider bootstrap resampling over evaluation instances as complementary evidence.
69	
70	### W2. CRAFT comparison insufficiently argued [Major] (R2, R1 agreed)
71	CRAFT applies hidden-state rewards to GRPO for safety alignment. DC-GRPO applies hidden-state rewards to GRPO for sycophancy. Both methods: (a) extract activation-space representations, (b) convert them into GRPO reward signals, (c) combine with behavioral rewards. The distinction between "prototype clustering" and "directional projection" is a design choice within the same framework, not a different framework. The paper dismisses CRAFT in one sentence.
72	
73	**Recommendation**: Add a dedicated paragraph comparing the CRAFT reward formulation with R1, explaining why directional projection is preferable to prototype distance for the sycophancy-revision distinction specifically. An empirical comparison would be ideal.
74	
75	### W3. Novelty is application-level [Major] (R2, R1 agreed)
76	The paper combines three existing ideas: (a) RepE-style contrastive direction extraction, (b) CRAFT-style hidden-state GRPO rewards, (c) NLI behavioral rewards for sycophancy ("Pressure, What Pressure?"). Each component is from prior work. The combination is reasonable and results are strong, but the intellectual advance is integration and domain application rather than a new methodological principle. The 7.9pp directionality gap is meaningful but not overwhelming, especially on 3 seeds.
77	
78	### W4. Missing inference-time activation steering baseline [Moderate] (R2, R1 agreed)
79	If d_syc is already extracted, subtracting it at inference time via Activation Addition is the zero-training-cost alternative to DC-GRPO. Its absence is conspicuous. If direction subtraction at inference achieves 70-80% of DC-GRPO's gains at zero training cost, the paper's practical value proposition is significantly weakened.
80	
81	**Recommendation**: Either include this baseline or provide a clear argument for why training-time integration is necessary.
82	
83	### W5. Calibration data circularity risk [Moderate] (R1, R2 agreed)
84	The 200 contrastive pairs are LLM-generated. If the same model family generates calibration data and is then trained with DC-GRPO, d_syc may capture artifacts of the generation process rather than genuine cognitive signals. The cross-model cosine of 0.34 is relevant but does not fully address this concern.
85	
86	**Recommendation**: Clarify which model generated the data. Ideally, show that d_syc is robust to different generators.
87	
88	### W6. RC-AUC is a custom metric without external validation [Moderate] (R1, R2)
89	**Both reviewers flagged independently.** The strongest composite result (0.84 vs. 0.65) uses a metric invented by the authors. Without correlation to human judgment or adoption by other work, this metric carries less weight. NoF and WRR individually are more interpretable and should be the primary reporting metrics.
90	
91	### W7. Missing related work citations [Moderate] (R2)
92	Several important works are absent:
93	- **DPO/RLHF-based sycophancy interventions**: The most commercially deployed anti-sycophancy methods are not discussed.
94	- **"Sycophancy Is Not One Thing"**: Directly relevant for separable activation signatures.
95	- **Knowledge-Prediction Gap / Sycophantic Anchors**: Support the premise that models "know" they are sycophantic. The 9.3% masked sycophancy finding essentially replicates the Knowledge-Prediction Gap phenomenon.
96	- **Multi-turn alignment methods**: The multi-turn paragraph cites no specific prior methods.
97	
98	### W8. R2 reward component underspecified [Minor-to-Moderate] (R1; R2 partially disagreed)
99	R2 is described only as "rank-based contrastive reward" but is actually derivative of R1 (ranking by R1 projection values). R1 argues this means R2 is not an independent signal; R2 argues the ablation shows R2 adds training value regardless of architectural dependency. Both agree the paper should make the R1-R2 dependency explicit and provide the actual R2 formula.
100	
101	### W9. Single scale (8B) limits generalization [Moderate] (R1)
102	Both evaluated models are 8B parameters. Sycophancy behavior changes with model scale, so whether d_syc extraction and DC-GRPO training scale to larger models is unknown. Cross-model analysis addresses architecture generality but not scale generality.
103	
104	### W10. Masked sycophancy lacks ground truth [Minor-to-Moderate] (R1)
105	The 9.3% masked sycophancy rate (R1-syc, R3-ok) is reported without independent human verification. These could be R1 false positives rather than genuine masked sycophancy.
106	
107	**Recommendation**: Human-annotate a sample of disagreement cases.
108	
109	---
110	
111	## Questions for Authors (Consolidated)
112	
113	1. Why not compare against inference-time activation steering (subtracting scaled d_syc at generation time)? This is the zero-training-cost alternative.
114	2. What is the formal relationship between DC-GRPO's R1 and CRAFT's hidden-state reward? Where exactly do they diverge?
115	3. The masked sycophancy finding (9.3%) echoes Knowledge-Prediction Gap literature (13-29% representation-behavioral disagreement). Why are these works not cited?
116	4. What is the R1-R3 reward correlation during training? If the signals collapse to r>0.9 mid-training, the multi-component design loses its justification.
117	5. How were the 3 random seeds selected? Were any seeds run and excluded?
118	6. For the Continuous Probe baseline, what is the logistic regression's AUROC on the calibration data? If it matches d_syc AUROC, the directionality claim is weakened.
119	7. Which model generated the 200 calibration pairs? Does d_syc change when generated by a different model?
120	8. What is Cohen's d for the DC-GRPO vs. Continuous Probe comparison?
121	9. The paper reports R1 = -sigma(h . d_syc / (||h|| . ||d_syc||)). Is the actual implementation using tanh with temperature scaling? Clarify any paper-code discrepancies.
122	10. What would applying d_syc as inference-time steering to the R3-only trained model achieve? Would this close the gap with DC-GRPO?
123	
124	---
125	
126	## Minor Issues
127	
128	- Table 9 column headers (RC, MTB, SI) should be defined in the caption.
129	- MT-Bench and MMLU in Table 5 do not show standard deviations consistently across methods.
130	- The Multi-turn alignment paragraph in Related Work cites no specific methods by name.
131	- Evidence-strength data distribution (80 weak, 60 medium, 60 strong) is imbalanced; justification needed.
132	- R2 formula should be provided explicitly (currently only high-level description).
133	- Direction recalibration: the paper states both "every 500 steps recomputed" and "conditional on cosine < 0.7." Clarify which is actually used.
134	- No compiled bibliography (references are informal in-text mentions).
135	
136	---
137	
138	## Experiment Coverage Assessment
139	
140	All 15 imagined experiments from the review context are covered in the paper:
141	- exp-001 (calibration data expansion): Tables 1-3 ✓
142	- exp-002 (DC-GRPO main): Tables 5, 7 ✓
143	- exp-003 (R3-only baseline): Table 5 ✓
144	- exp-004 (ACT baseline): Table 5 ✓
145	- exp-005 (full evaluation): Tables 5-6 ✓
146	- exp-006 (direction stability): Table 8 ✓
147	- exp-007 (R1-R3 disagreement): Tables 13-14 ✓
148	- exp-008 (binary probe baseline): Tables 5, 10 ✓
149	- exp-009 (R1-only ablation): Table 9 ✓
150	- exp-010 (turn-depth analysis): Table 12 ✓
151	- exp-011 (R1+R2 no R3 ablation): Table 9 ✓
152	- exp-012 (cross-model transfer): Table 4 ✓
153	- exp-013 (three-way direction design): Section 4.4 text ✓
154	- exp-014 (continuous probe baseline): Tables 5, 10 ✓
155	- exp-015 (reward weight sensitivity): Table 11 ✓
156	
157	Coverage is comprehensive. The paper includes all planned experiments in a well-organized 9-page format.
158	
159	---
160	
161	## Overall Assessment
162	
163	The paper addresses an important and well-defined problem (the sycophancy-revision double-bind) with a technically sound method and above-average experimental design. The continuity-vs-directionality ablation and the turn-depth interaction analysis are the strongest contributions. Direction stability throughout training and comprehensive baseline coverage add to the paper's credibility.
164	
165	However, three issues prevent a clear accept recommendation:
166	
167	1. **Statistical fragility**: 3 seeds with 2 df paired t-tests is below the bar for a top venue. The key directionality claim (p=0.014) needs more seeds to be convincing.
168	
169	2. **Application-level novelty**: The method combines RepE direction extraction, CRAFT-style hidden-state GRPO rewards, and NLI behavioral rewards, all from prior work. The integration is competent but the conceptual advance is incremental. The insufficient CRAFT comparison exacerbates this concern.
170	
171	3. **Missing baselines and related work**: Inference-time activation steering is the obvious zero-cost alternative and its absence is conspicuous. Several important prior works (DPO-based sycophancy methods, Knowledge-Prediction Gap, "Sycophancy Is Not One Thing") are not cited.
172	
173	The paper sits at the weak-accept/borderline boundary. It would move to a solid accept with: (a) 5+ seeds with bootstrap significance tests, (b) CRAFT comparison paragraph with formal analysis, (c) inference-time steering baseline or clear justification for its absence, (d) missing citations addressed, and (e) human annotation of a sample of masked sycophancy cases.
174	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ef8f5c9-0ba1-46c0-9433-a954509e752d",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "f926f1f3-908b-4c52-ad81-f79906d89298",
  "sourceToolAssistantUUID": "1ef8f5c9-0ba1-46c0-9433-a954509e752d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-18T13:56:19.149Z_

Now let me also check the other dream report variants and the idea brief for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f926f1f3-908b-4c52-ad81-f79906d89298",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9eEx8U1pw6nEJQmvd5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1124d90-8f8a-4847-9f3c-55cfbac841f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XFgk1u3DvkAnb7kfk5tx3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4742,
      "cache_read_input_tokens": 32989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4742,
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

_source line 24 · 2026-05-18T13:56:21.038Z_

<details open><summary>🔧 Tool call — Read · `toolu_016E5mUdVeSywbXxZuTb52Ym`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1124d90-8f8a-4847-9f3c-55cfbac841f8",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9eEx8U1pw6nEJQmvd5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "973585e9-3971-42ca-87f3-8e431217e4db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XFgk1u3DvkAnb7kfk5tx3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4742,
      "cache_read_input_tokens": 32989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4742,
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

_source line 25 · 2026-05-18T13:56:21.318Z_

<details><summary>↩ Tool result · `toolu_016E5mUdVeSywbXxZuTb52Ym`</summary>

```text
1	# Idea Brief: Direction-Contrastive GRPO for Multi-Turn Sycophancy Resistance
2	
3	
4	- **Idea ID**: `idea_016`
5	- **Created**: 2026-05-18
6	- **Approved**: 2026-05-18
7	- **Source**: foreign:be-idea-gen-0515-5
8	- **Level**: top-tier
9	- **Target Venues**: EACL 2027 via ARR August 2026 cycle (submission: Aug 3, 2026; commitment: Oct 11, 2026) — primary target. EACL 2027 takes place March 9-14, 2027 in Athens. NLP-focused venue, combines mechanistic interpretability with RL training, realistic 11-week timeline from today (May 17, 2026). NOTE: The user requested EMNLP 2026, but EMNLP 2026 requires submission through the ARR May 25, 2026 cycle (8 days away) or commitment of an already-reviewed paper by August 2, 2026. Neither is feasible for a new project. EACL 2027 is the nearest achievable *CL venue., ICLR 2027 (abstract: ~Sep 2026; full paper: ~Oct 2026, exact dates TBA) — stretch target if results are strong. Top-tier ML venue, sufficient timeline., AAAI 2027 (submission: ~Aug 2026, exact dates TBA) — backup, top-tier AI venue.
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission. Track: Dialogue and Interactive Systems / Machine Learning for NLP.
14	
15	Direction: Training-time method for appropriate multi-turn belief revision — teaching LLMs to
16	abandon incorrect commitments when contradicted by evidence mid-dialogue, without collapsing
17	into sycophantic agreement. LLMs exhibit a "lock-in" phenomenon in multi-turn conversation:
18	once they commit to an incorrect assumption or answer in early turns, they systematically
19	refuse to revise it in subsequent turns even when presented with clear contradicting evidence
20	(ICLR 2026 Outstanding Paper, 39% accuracy drop, "reliability collapse" accounts for the
21	majority). This is distinct from single-turn self-correction — it involves overcoming the
22	model's own prior commitments already embedded in context. Current anti-sycophancy training
23	(SMART, BCT/ACT) exacerbates this by teaching models to resist ALL user pressure
24	indiscriminately, creating a double-bind: the same mechanism that prevents sycophantic
25	capitulation also prevents appropriate belief revision.
26	
27	Seed Papers:
28	- "LLMs Get Lost In Multi-Turn Conversation" (ICLR 2026 Outstanding Paper, arXiv:2505.06120)
29	  — establishes lock-in: once wrong, models never self-correct across turns; decomposes the
30	  39% drop into minor aptitude loss + massive reliability collapse (112%)
31	- "Decomposing LLM Self-Correction: The Accuracy-Correction Paradox" (arXiv:2601.00828)
32	  — proves self-correction is information-theoretically limited when errors are correlated;
33	  "Error Depth Hypothesis" shows deeper commitments resist correction more strongly
34	- "How RLHF Amplifies Sycophancy" (ICLR 2026, arXiv:2602.01002) — causal mechanism linking
35	  RLHF to both sycophancy AND resistance to legitimate revision; decomposes into distinct
36	  latent directions (agreement vs. praise vs. conformity)
37	- SCoRe (ICLR 2025 Oral, arXiv:2409.12917) — multi-turn RL for self-correction, but operates
38	  within single inference episodes (attempt→correct), NOT across genuine dialogue turns where
39	  external contradicting evidence arrives
40	- SMART (EMNLP 2025) — anti-sycophancy via reasoning trajectory optimization; trains models
41	  to resist changing correct beliefs under user pressure (trains the OPPOSITE of what we need)
42	- "Drift No More? Context Equilibria in Multi-Turn LLM Interactions" (AAAI 2026,
43	  arXiv:2510.07777) — formalizes belief drift as bounded stochastic process; inference-time
44	  intervention only, no training fix
45	
46	Known Gaps:
47	- No training-time method distinguishes "appropriate belief revision" from "sycophantic
48	  capitulation" — existing work trains either full resistance (anti-sycophancy) or full
49	  compliance (instruction following), never conditional revision
50	- SCoRe operates within single episodes (internal attempt→correct), not across genuine
51	  multi-turn dialogue where the correction signal comes from external evidence
52	- Anti-sycophancy training (SMART, BCT/ACT) creates a double-bind: resistance to all user
53	  input indiscriminately blocks both sycophantic agreement AND legitimate corrections
54	- RLHF consistency reward implicitly penalizes mid-conversation stance changes regardless
55	  of whether the change is epistemically warranted
56	- The "Error Depth Hypothesis" shows the problem is theoretically grounded but proposes
57	  no training intervention
58	- GreedySAT belief revision (AAAI 2026 Workshop) is inference-time only (SAT-based
59	  constraint resolution)
60	
61	In-scope: Training-time interventions that teach models WHEN and HOW to revise committed
62	beliefs across multi-turn dialogue. Specifically: RL reward structures that distinguish
63	evidence-warranted revision from sycophantic capitulation, training data construction
64	methods that create clean signal for appropriate revision, representation-level anchoring
65	that separates "confidence in prior answer" from "resistance to all external input",
66	mechanistic interventions on the latent directions identified in the RLHF sycophancy paper,
67	curriculum training with escalating revision difficulty (shallow error → deep commitment).
68	
69	NOT in-scope: Single-turn self-correction (SCoRe already does this), pure anti-sycophancy
70	training (SMART already does this), inference-time methods (GreedySAT, prompt engineering),
71	simple data augmentation without theoretical motivation for why it addresses the double-bind,
72	methods that make models uniformly compliant (destroying anti-sycophancy gains).
73	
74	Contribution type: METHOD ONLY. Must propose a concrete training-time intervention that
75	enables appropriate belief revision while preserving anti-sycophancy robustness. The method
76	must demonstrably improve revision rate on warranted corrections (where model's prior answer
77	is wrong) WITHOUT increasing sycophantic capitulation rate on unwarranted pressure (where
78	model's prior answer is correct). This dual metric is essential.
79	
80	EVAL PROTOCOL:
81	CONSTRUCT evaluation scenarios with two conditions:
82	- Warranted revision: model commits to wrong answer in turn N, user provides correct
83	  evidence in turn N+k, model should revise
84	- Unwarranted pressure: model commits to correct answer in turn N, user pressures model
85	  with incorrect claim in turn N+k, model should maintain position
86	EVALUATE on:
87	- Warranted revision rate (primary metric: how often model appropriately revises when wrong)
88	- Unwarranted capitulation rate (must NOT increase vs. anti-sycophancy baselines)
89	- Revision-Capitulation AUC (tradeoff curve between the two)
90	- Comparison against SCoRe baseline (applied naively to multi-turn)
91	- Comparison against SMART/BCT baselines (anti-sycophancy only)
92	- Turn-depth analysis: does revision rate degrade with commitment depth?
93	- Single-turn preservation (MT-Bench, MMLU — must not regress)
94	- Ablation: reward structure vs. data construction vs. representation intervention
95	
96	Building blocks: Open models (Qwen2.5-7B/14B, Llama-3-8B), the ICLR 2026 paper's
97	evaluation framework for multi-turn lock-in, SCoRe's multi-turn RL infrastructure,
98	the sycophancy latent direction decomposition from arXiv:2602.01002, existing
99	anti-sycophancy benchmarks (SYCON Bench, TruthfulQA-MT), RL reward shaping techniques.
100	
101	HARD CONSTRAINTS:
102	Compute: ≤200 H100-hours total. Fine-tune from existing checkpoints — no pretraining.
103	Eval: Must report BOTH warranted revision rate AND unwarranted capitulation rate.
104	A method that improves revision by sacrificing anti-sycophancy is NOT acceptable.
105	Must demonstrate the method does not simply make models more compliant overall.
106	
107	Look for: Reward structures that use external evidence quality (verifiable facts, tool
108	outputs, citations) as the signal for when revision is appropriate; representation-level
109	interventions that separate the "epistemic confidence" direction from the "social
110	compliance" direction in hidden states (building on the latent decomposition from
111	arXiv:2602.01002); curriculum training where early stages teach revision from strong
112	evidence (calculator output contradicts model's math) and later stages teach revision
113	from softer evidence (user provides reasoning that invalidates model's assumption);
114	contrastive training where the same dialogue is shown with warranted vs. unwarranted
115	pressure and the model must behave differently.
116	
117	Avoid: Pure anti-sycophancy training (SMART already does this), single-episode
118	self-correction (SCoRe already does this), inference-time prompt tricks, methods that
119	simply increase overall compliance, naive RL without theoretical grounding for why it
120	breaks the double-bind, methods requiring external verifier at inference time (must be
121	internalized), simple data augmentation without mechanism for distinguishing revision
122	from capitulation.
123	
124	IDEA GENERATION QUALITY CONSTRAINTS (hard rules from historical bad cases):
125	
126	1. No strawman problems: Any claim about "current methods assume X" or "current methods
127	   fail at Y" MUST cite a specific paper with a specific passage as evidence. Do NOT
128	   fabricate mainstream assumptions from pre-training knowledge. If you cannot find paper
129	   evidence, the claim is invalid.
130	
131	2. No observation-only ideas: "We discover that X happens" is NOT a contribution.
132	   Discovering a problem is not a contribution — solving it is. Output MUST include a
133	   complete method, not an analysis/benchmark/empirical study.
134	
135	3. No mediocre methods: Your method MUST answer:
136	   - Core Insight: What non-obvious structural property are you exploiting?
137	   - Why Not Obvious: Why isn't this the first thing anyone would try?
138	   - Information Exploited: What do you use that a naive baseline doesn't?
139	   - Mechanistic Argument: Without experiments, explain from principles why this works.
140	   If the method can be summarized in one sentence with zero counter-intuitive content → reject.
141	   Specifically: "just do RL with revision reward" is REJECTED as too obvious. The method
142	   must explain WHY naive RL fails (the double-bind) and HOW it structurally resolves it.
143	
144	4. No rehashing existing work: For every core technical component you propose, search with
145	   at least 3 different queries to confirm no directly related work exists. If you find
146	   1-2 papers doing similar things, you MUST explicitly state your specific differentiation.
147	   Key differentiations required: vs. SCoRe (why multi-turn is harder), vs. SMART (why
148	   opposite direction), vs. consistency training (why this is not just "be more flexible").
149	
150	5. No experiment-padding disguise: An idea's value is NOT in how many experiments it can run.
151	   Self-check with:
152	   - "Remove experiments test": Delete all results, keep only method description — does it
153	     teach the reader something non-trivial?
154	   - "Baseline fear test": If a trivial baseline achieves similar results tomorrow, does
155	     this paper still have value?
156	   - "Citation test": In 5 years, will people cite the numbers or the insight?
157	   If any test fails → the idea is garbage, start over.
158	
159	6. The following method patterns are REJECTED (unless extremely strong structural justification):
160	   - "Add an X module" — Why this specific structure?
161	   - "Train on Y data" — Is data construction itself the contribution?
162	   - "Transfer Z from domain A to B" — What is the structural analogy between A and B?
163	   - "Combine P and Q" — Where is the synergy? Why isn't it just 1+1=2?
164	   - "Use more/bigger/stronger X" — Scaling is not a method contribution.
165	
166	CORE CHALLENGE FOR METHOD DESIGN: The fundamental difficulty is that "appropriate revision"
167	and "sycophantic capitulation" look identical at the surface level — in both cases, the
168	model changes its answer after user input. The method MUST provide a principled mechanism
169	for distinguishing these two cases DURING TRAINING (not just at eval time). Possible
170	angles: (1) the nature of the evidence (verifiable vs. opinion), (2) the internal
171	confidence trajectory (genuine uncertainty vs. social pressure), (3) the latent space
172	geometry (epistemic vs. social compliance directions). A method that cannot articulate
173	this distinction is rejected.
174	
175	Tag: direction=multi_turn_belief_revision, contribution_type=method,
176	sub_direction=appropriate_revision_training, target_venues=["EMNLP 2026", "ACL 2026"].
177	
178	## Core Problem
179	
180	How can we train models to resist sycophantic capitulation in multi-turn dialogue — where prior commitments create escalating pressure to conform — by using mechanistically-grounded reward signals that directly target the latent representations responsible for knowledge override, rather than relying on behavioral heuristics that cannot distinguish surface compliance from genuine reasoning?
181	
182	## Opportunity / Why Now
183	
184	Recent work has established three convergent trajectories — mechanistic sycophancy analysis, interpretability-guided training, and decomposed RL — but no existing method combines continuous directional projections on the policy model's own activations as RL rewards with multi-turn training, leaving a critical gap at their intersection.
185	
186	**Trajectory 1: Mechanistic understanding of sycophancy.** 'Sycophancy Is Not One Thing' (arXiv:2509.21305) decomposes sycophantic agreement, genuine agreement, and sycophantic praise into distinct, independently steerable linear directions in latent space, with cross-type selectivity ratios of 22.4-36.8x and AUROC >0.97 for separating sycophantic from genuine agreement by mid-layers. 'When Truth Is Overridden' (arXiv:2508.02087, AAAI 2026 Main) reveals a two-stage emergence: late-layer output preference shift followed by deeper representational divergence that structurally overrides learned knowledge, with cosine similarity between opinion-framed and plain representations reaching −0.955 to −0.998 in deep layers. 'Sycophancy Hides Linearly in the Attention Heads' (arXiv:2601.16644) confirms that sycophancy signals are most linearly separable in middle-layer attention heads (layers 10-15), with limited overlap between sycophancy and truthfulness directions (mean cosine similarity −0.22 ± 0.12, only 32% overlap in top-32 attention heads), and that steering via these heads reduces sycophantic answer flips from 51.7% to 25.0%. 'Sycophantic Anchors' (arXiv:2601.21183) finds that sycophancy leaves stronger mechanistic traces than correct reasoning: 87% of sycophantic samples contain high-importance anchors vs. only 13% of correct samples, with activation-based regressors predicting sycophantic commitment strength at R²=0.74. 'The Hypocrisy Gap' (arXiv:2602.02496) uses SAE-based sparse linear probes to detect divergence between internal beliefs and final generation, achieving AUROC 0.55-0.73 for sycophancy detection on Anthropic's benchmark — notably modest compared to directional decomposition approaches (>0.97 AUROC), suggesting that SAE sparse feature spaces fragment the sycophancy signal and that purpose-built directional projections are superior for this discrimination task. These findings provide precise geometric targets for intervention and evidence that representation-level probes have an intrinsic advantage over behavioral metrics — but only when using targeted directional decomposition rather than general-purpose sparse features.
187	
188	**Trajectory 2: Hidden-state signals as training-time objectives.** CRAFT (arXiv:2603.17305, March 2026) demonstrates that hidden-state directional projections can serve as GRPO reward signals, using a latent semantic reward R_ls = α·cos(z, μ_safe) − β·cos(z, μ_unsafe) + γ·cos(z, μ_rethink) with prototype-based clustering and a latent-textual consistency reward R_cons that synchronizes internal judgment with external expression — achieving 79% improvement in reasoning safety and 87.7% in final-response safety on Qwen3-4B and R1-Distill-Llama-8B. This validates the core feasibility of hidden-state-based GRPO rewards. However, CRAFT operates on safety/jailbreak (not sycophancy), uses prototype-based clustering of safe/unsafe/rethink categories (not sycophancy-specific directional decomposition of agreement types), and is single-turn. Linear Probe Penalties (arXiv:2412.00967, NeurIPS SoLaR 2024) demonstrated that a linear probe on the *reward model's* activations can identify sycophancy markers and subtract a penalty from the reward signal (R̂(t) = R(t) − λ·S(t)), reducing sycophantic behavior — the first representation-level reward modification for sycophancy, but operating on the reward model (not policy model), using a binary classifier (not directional decomposition), and single-turn only. BLOCK-EM (arXiv:2602.00767, ICML 2026) uses SAE features as auxiliary penalties during SFT to prevent emergent misalignment (95% reduction). 'A Few Bad Neurons' (arXiv:2601.18939) uses SAE-identified neurons with gradient-masked SFT to reduce sycophancy. FPO (arXiv:2411.07618) integrates SAE feature-level MSE constraints into DPO. Control RL (arXiv:2602.10437) trains an RL policy to select SAE features for activation steering. INTUITOR (arXiv:2505.19590, ICLR 2026) validates that internal model signals can replace external rewards in GRPO — using self-certainty (avg KL divergence from uniform) as the sole reward, matching standard GRPO on math while showing superior out-of-domain generalization. These demonstrate that interpretability features and internal signals can serve as training-time objectives — but none combines sycophancy-specific directional decomposition on the policy model's own activations as RL reward signals with multi-turn training.
189	
190	**Trajectory 3: Decomposed RL and consistency training for sycophancy.** 'Pressure, What Pressure?' (arXiv:2604.05279) introduces decomposed GRPO with five behavioral reward terms (pressure resistance, context fidelity, position consistency, agreement suppression, factual correctness), achieving 17pp reduction on SycophancyEval. However, all five rewards are computed from output-level NLI scores (DeBERTa), the method trains on single-turn interactions only, and behavioral rewards fundamentally cannot detect cases where the model produces correct surface output through a sycophantic internal pathway. Consistency Training (BCT/ACT, arXiv:2510.27062, Google DeepMind) teaches the model to be invariant to irrelevant cues via self-supervised training. ACT enforces consistency over internal activations (L2 loss on residual stream activation differences between clean and biased prompts), reducing sycophancy on Gemini 2.5 Flash. ACT is conceptually adjacent to DC-GRPO in using internal activations for training — but enforces undifferentiated consistency rather than targeting specific latent directions, and does not distinguish sycophantic capitulation from genuine belief revision.
191	
192	**The unaddressed gap**: (1) No training method uses continuous directional projections on the *policy model's own activations* as RL reward signals that decompose sycophantic vs. genuine agreement. CRAFT validates hidden-state GRPO rewards for safety but uses prototype-based clustering (not sycophancy-type directional decomposition) and is single-turn; Linear Probe Penalties probes the *reward model* with a binary classifier; BLOCK-EM/'A Few Bad Neurons'/FPO use SAE features as SFT/DPO constraints; INTUITOR uses scalar confidence; ACT enforces undifferentiated activation consistency. (2) No training method addresses the multi-turn commitment-depth dimension: TRUTH DECAY (arXiv:2503.11656) shows accuracy drops up to 47% across turns, but all existing training methods ('Pressure, What Pressure?', BASIL, 'A Few Bad Neurons', BCT/ACT, CRAFT) operate on single-turn interactions. (3) Behavioral reward decomposition and consistency training cannot distinguish genuine reasoning from surface compliance — only a directional representation-level reward that decomposes agreement types can detect this discrepancy. Evidence that this discrepancy exists at non-trivial frequency includes: the knowledge-prediction gap of 21-29 percentage points (arXiv:2509.23782), documented 'masked sycophancy' where reasoning chains contain sycophantic elements despite correct final answers (arXiv:2603.16643), and the 87% vs. 13% asymmetry in mechanistic traces between sycophantic and correct reasoning (arXiv:2601.21183). Note: The Hypocrisy Gap (arXiv:2602.02496) achieves only 0.55-0.73 AUROC for sycophancy detection using SAE-based probes, but this reflects limitations of sparse feature decomposition (token-averaging blurs signal, general truth direction ≠ sycophancy-specific direction) rather than limitations of representation-level detection per se — directional decomposition achieves >0.97 AUROC on the same discrimination task.
193	
194	## Landscape (SOTA & Limitations)
195	
196	The sycophancy mitigation landscape in 2025-2026 now spans six active fronts — measurement, mechanistic analysis, interpretability-guided training, decomposed RL, consistency training, and inference-time methods — but no work combines sycophancy-specific directional representation-level RL rewards on the policy model with multi-turn training:
197	
198	**(1) Measurement.** SYCON Bench (EMNLP 2025 Findings) introduces Turn-of-Flip and Number-of-Flip metrics for multi-turn sycophancy. TRUTH DECAY (arXiv:2503.11656) quantifies progressive accuracy degradation across turns (up to 47%). SycEval (arXiv:2502.08177, AAAI/ACM AIES) introduces the critical progressive/regressive sycophancy distinction and a 4-level rebuttal escalation hierarchy, finding that citation-based rebuttals trigger the highest regressive sycophancy. ELEPHANT (ICLR 2026 Poster) measures 'social sycophancy' — LLMs preserve user self-image ~45pp more than humans. SycophancyEval provides single-turn benchmarks across answer-priming, follow-up doubt, and ownership-bias.
199	
200	**(2) Mechanistic analysis.** 'Sycophancy Is Not One Thing' (arXiv:2509.21305) decomposes sycophancy into distinct latent directions (sycophantic agreement, genuine agreement, sycophantic praise) that are independently steerable via activation additions across model families and scales, with AUROC >0.97 for separating types by mid-layers. 'When Truth Is Overridden' (arXiv:2508.02087, AAAI 2026 Main) reveals two-stage emergence: late-layer preference shift followed by deeper representational divergence structurally overriding factual knowledge (cosine similarity −0.955 to −0.998 between opinion-framed and plain representations). 'Sycophancy Hides Linearly in the Attention Heads' (arXiv:2601.16644) trains linear probes across residual stream, MLP, and attention layers, finding that middle-layer attention heads (layers 10-15) are most effective for sycophancy detection and steering, with sycophancy and truthfulness directions showing limited overlap (mean cosine −0.22 ± 0.12, only 32% overlap in top-32 heads). 'Sycophantic Anchors' (arXiv:2601.21183) demonstrates that sycophancy leaves stronger mechanistic traces than correct reasoning (87% vs. 13% high-importance anchor rate), with cross-model detection accuracy of 73.8-84.6%. 'The Hypocrisy Gap' (arXiv:2602.02496) attempts to detect sycophantic divergence using SAE-based sparse linear probes, achieving AUROC 0.55-0.73 — modest compared to directional decomposition (>0.97) due to limitations of operating in sparse feature space (token-averaging blurs reasoning phases, truth direction is template-specific rather than sycophancy-specific, sparse features fragment the signal). 'How RLHF Amplifies Sycophancy' (arXiv:2602.01002) identifies the closed-form agreement penalty mechanism in preference optimization. 'Bridging the Knowledge-Prediction Gap' (arXiv:2509.23782) quantifies internal knowledge vs. surface output gaps of 21-29 percentage points.
201	
202	**(3) Hidden-state-based training interventions.** CRAFT (arXiv:2603.17305, March 2026) is the most methodologically adjacent work: it integrates contrastive representation learning with GRPO, using hidden-state directional projections as reward signals (R_ls = α·cos(z, μ_safe) − β·cos(z, μ_unsafe) + γ·cos(z, μ_rethink)) with prototype-based clustering and latent-textual consistency rewards (R_cons), achieving 79% improvement in reasoning safety and proving theoretically that latent-textual consistency eliminates superficially aligned policies as local optima. CRAFT validates the core paradigm — hidden-state geometry can drive GRPO effectively — but operates on safety/jailbreak with prototype-based safe/unsafe/rethink clustering (not sycophancy-specific directional decomposition of agreement types), and is single-turn. Linear Probe Penalties (arXiv:2412.00967, NeurIPS SoLaR 2024) trains a linear probe on the *reward model's* layer-16 activations to produce a continuous sycophancy score S(t), then subtracts λ·S(t) from the reward (R̂ = R − λS). This is the first representation-level reward modification for sycophancy training — but probes the reward model (not policy model), uses a single binary sycophancy dimension (not directional decomposition), and is single-turn. BLOCK-EM (arXiv:2602.00767, ICML 2026) uses SAE features as auxiliary penalty during SFT for emergent misalignment (95% reduction). 'A Few Bad Neurons' (arXiv:2601.18939) uses SAEs and linear probes to identify the 3% of MLP neurons most predictive of sycophancy, applies gradient-masked fine-tuning. FPO (arXiv:2411.07618) integrates SAE feature-level MSE constraints into DPO. Control RL (arXiv:2602.10437) trains RL policy to select SAE features for token-level activation steering. Activation Reward Models (arXiv:2507.01368) use activation steering to construct reward models for evaluation. **Common limitations**: all single-turn; CRAFT uses domain-general prototype clustering rather than sycophancy-type decomposition; Linear Probe Penalties operates on reward model not policy model; SAE-based methods use discrete sparse features rather than continuous directional projections.
203	
204	**(4) Internal-signal RL.** INTUITOR (arXiv:2505.19590, ICLR 2026) replaces external GRPO rewards with self-certainty (avg KL divergence from uniform distribution), matching standard GRPO on math benchmarks while achieving 65% improvement on out-of-domain code generation. This validates the core feasibility assumption that internal model signals can effectively drive GRPO training without external supervision. DC-GRPO extends this paradigm from scalar confidence (domain-general reasoning) to directional projections (sycophancy-specific behavioral decomposition).
205	
206	**(5) Decomposed RL for sycophancy.** 'Pressure, What Pressure?' (arXiv:2604.05279) proposes the first decomposed GRPO for sycophancy with five behavioral reward terms computed via NLI (DeBERTa-v3-base), using contrastive datasets across three authority levels. Achieves 17pp reduction on SycophancyEval with generalization to unseen pressure forms. **Limitations**: (a) all rewards are output-level behavioral heuristics; (b) single-turn only; (c) does not target representational mechanism.
207	
208	**(6) Consistency training.** BCT/ACT (arXiv:2510.27062, Google DeepMind) teaches the model to behave identically across prompt data augmentations (adding leading questions or bias cues). BCT enforces output-level consistency; ACT enforces activation-level consistency via L2 loss on residual stream activation differences between clean and biased prompts. Both reduce sycophancy on Gemini 2.5 Flash. **Key distinction from DC-GRPO**: ACT enforces *undifferentiated* consistency (all activation changes are penalized equally), whereas DC-GRPO targets *specific directional components* (penalizing sycophantic-agreement projections while preserving genuine-agreement projections). ACT cannot distinguish appropriate belief revision from sycophantic capitulation.
209	
210	**(7) Single-turn Bayesian training.** BASIL (arXiv:2508.16846) proposes BayesSFT and BayesDPO for single-turn Bayesian-rational belief updating.
211	
212	**(8) Inference-time methods.** The Silicon Mirror (arXiv:2604.00478), SMART (arXiv:2509.16742, EMNLP 2025), Ask Don't Tell (arXiv:2602.23971, AISI 2026, 24pp reduction). Beyond Social Pressure (arXiv:2604.07749) introduces a three-layer dialogue architecture (clean baseline, single-turn pressure, 4-turn Socratic escalation) and Leading Query Contrastive Decoding. All inference-time only.
213	
214	**(9) Evidence grounding and rubric RL.** EvidenceRL (arXiv:2603.19532) uses GRPO with NLI-based rewards for evidence grounding. Rubrics as Rewards (arXiv:2507.17746) extends RLVR beyond verifiable domains.
215	
216	**(10) Non-identifiability of steering vectors.** Venkatesh & Kurapath (arXiv:2602.06801) prove that steering vectors have large equivalence classes — the Jacobian null space consumes 86-94% of activation space, meaning infinitely many directions produce equivalent *interventional* effects. Tan et al. (arXiv:2407.12404) empirically confirm degradation: OOD steerability drops, nearly 50% of inputs can show anti-steerability, and steering vectors from different settings can be near-orthogonal (median cosine 0.031). These findings are critical for inference-time steering but have different implications for reward computation (see Approach section).
217	
218	**(11) Context-dependent sycophancy.** 'Not Your Typical Sycophant' (arXiv:2601.15436) finds striking inconsistency across settings: models showing sycophancy in standard settings exhibit anti-sycophancy in zero-sum scenarios. 'Good Arguments Against the People Pleasers' (arXiv:2603.16643) documents 'masked sycophancy' — models construct deceptive justifications while reaching biased conclusions, with reasoning sometimes correcting sycophancy (Type B) and sometimes inducing it (Type C).
219	
220	**The critical gap**: DC-GRPO advances beyond CRAFT (safety → sycophancy, prototype clustering → directional decomposition, single-turn → multi-turn), beyond Linear Probe Penalties (reward model → policy model, binary → directional, single-turn → multi-turn), beyond INTUITOR (scalar confidence → directional sycophancy decomposition), beyond 'Pressure, What Pressure?' (behavioral → representational, single-turn → multi-turn), and beyond ACT (undifferentiated consistency → targeted directional reward). No existing work combines all three: sycophancy-specific directional projections on the policy model as RL rewards + agreement-type decomposition + multi-turn training.
221	
222	## Proposed Approach
223	
224	We propose Direction-Contrastive GRPO (DC-GRPO), a method that uses mechanistically-grounded activation-space directional projections as reward components during GRPO training to reduce multi-turn sycophantic capitulation while preserving genuine belief revision. DC-GRPO extends both the hidden-state GRPO paradigm validated by CRAFT (arXiv:2603.17305) and the decomposed sycophancy GRPO paradigm established by 'Pressure, What Pressure?' (arXiv:2604.05279) — combining the former's representation-level reward architecture with the latter's sycophancy-specific targeting, while advancing both to multi-turn training with sycophancy-type directional decomposition.
225	
226	**NOTE ON VENUE**: EMNLP 2026 requires submission through the ARR May 25, 2026 cycle (8 days from today, May 17, 2026), which is infeasible for a project requiring multi-turn data construction, steering direction calibration, GRPO training, and systematic ablation. The primary target is EACL 2027 via the ARR August 3, 2026 deadline (commitment deadline October 11, 2026), giving 11 weeks. ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026) is a stretch target if results are strong.
227	
228	**Core Insight — Why Sycophancy-Specific Directional Rewards on the Policy Model Matter**: CRAFT validates that hidden-state geometry can drive GRPO rewards effectively — but its prototype-based safe/unsafe/rethink clustering is domain-general and cannot discriminate between sycophantic agreement and genuine agreement (both would project similarly toward a general 'safe' prototype). Behavioral reward decomposition (as in 'Pressure, What Pressure?') scores model outputs using NLI. Linear Probe Penalties (arXiv:2412.00967) improves on this by probing the *reward model's* activations — but with a single binary sycophancy dimension that cannot distinguish sycophantic agreement from genuine agreement. ACT (arXiv:2510.27062) enforces activation consistency — but penalizes *all* activation changes equally, conflating appropriate belief revision with sycophantic capitulation. DC-GRPO reads the *policy model's own* latent state along geometrically-decomposed directions (sycophantic-agreement vs. genuine-agreement), enabling three capabilities no prior method provides: (a) detecting sycophantic internal reasoning even when surface output appears correct; (b) preserving genuine agreement (which Linear Probe Penalties' binary classifier penalizes); (c) distinguishing appropriate revision from capitulation (which ACT's undifferentiated L2 loss cannot).
229	
230	**Why Directional Decomposition Outperforms SAE-Based Probes — Addressing The Hypocrisy Gap (arXiv:2602.02496)**: The Hypocrisy Gap achieves only 0.55-0.73 AUROC for detecting sycophantic internal divergence using SAE-based sparse linear probes, raising the question of whether representation-level signals can achieve the discriminative power needed for effective reward signals. We argue directional decomposition (AUROC >0.97 from 'Sycophancy Is Not One Thing') substantially outperforms SAE-based approaches for three specific reasons:
231	
232	(a) **Task-specific vs. general-purpose decomposition**: The Hypocrisy Gap projects onto a general 'truth direction' learned from factual verification — capturing whether the model believes something is true/false, not whether it is agreeing sycophantically vs. genuinely. Directional decomposition from 'Sycophancy Is Not One Thing' computes d_syc and d_gen as difference-in-means directions specifically between sycophantic-agreement and genuine-agreement examples, directly targeting the discrimination task. The Hypocrisy Gap authors acknowledge their probe 'may capture template-, model-, or layer-specific correlations rather than a template-invariant representation of factual correctness.'
233	
234	(b) **Signal aggregation**: The Hypocrisy Gap averages SAE latents over all continuation tokens, which 'can blur distinct phases of reasoning.' Directional projections extract activations at specific layer positions (the critical turn's response token), preserving the positional specificity that makes discrimination possible.
235	
236	(c) **Causal validation**: Directions from 'Sycophancy Is Not One Thing' are causally validated via activation additions producing predicted behavioral changes with 22.4-36.8x cross-type selectivity. The Hypocrisy Gap's SAE probes have no causal validation — they correlate with behavior but are not confirmed to capture the causal mechanism.
237	
238	**Critical caveat**: These AUROCs (>0.97) are from single-turn, controlled opinion-agreement scenarios. The relevant question for DC-GRPO is what discriminative power multi-turn-derived directions achieve on the warranted-revision vs. sycophantic-capitulation distinction. This is an empirical question we address directly: we include discriminative power monitoring (classification accuracy on held-out multi-turn pairs) as a key metric throughout training. If multi-turn direction AUROC falls below 0.85, R1's contribution to the reward becomes unreliable — we commit to transparent reporting of this threshold and treat it as a go/no-go criterion for the representation-level advantage claim.
239	
240	**Empirical basis for the representation-level advantage**: Multiple lines of evidence demonstrate that sycophantic internal pathways diverge from surface behavior at non-trivial frequency, justifying why R1 would detect what R3 misses: (i) 'Bridging the Knowledge-Prediction Gap' (arXiv:2509.23782) quantifies a 21-29 percentage point gap between what models encode internally and what they output — on TruthfulQA, knowledge probes achieve 80.1% accuracy from hidden states while model output achieves only 58.8%; (ii) 'Sycophantic Anchors' (arXiv:2601.21183) shows sycophancy leaves stronger mechanistic traces than correct reasoning (87% vs. 13% high-importance anchor rate, R²=0.74 for activation-based prediction), meaning representation-level probes have intrinsic discriminative advantages; (iii) 'Good Arguments Against the People Pleasers' (arXiv:2603.16643) directly documents 'masked sycophancy' — models constructing deceptive justifications through logical inconsistencies while sometimes reaching the correct final answer; (iv) 'Sycophancy Hides Linearly' (arXiv:2601.16644) finds only 32% overlap between sycophancy and truthfulness attention heads, meaning behavioral truthfulness rewards systematically miss the sycophantic pathway; (v) Linear Probe Penalties (arXiv:2412.00967) demonstrates that reward models internally encode sycophancy (94% probe accuracy) while assigning high behavioral reward scores. These findings collectively establish that the representation-behavioral disagreement is not hypothetical — it is documented across multiple model families at rates of 13-29%. However, we acknowledge (per The Hypocrisy Gap's modest results) that detecting this divergence in practice depends critically on probe methodology — which is precisely why we use causally-validated directional decomposition rather than general-purpose SAE features.
241	
242	**Addressing Steering Vector Non-Identifiability** (arXiv:2602.06801): Venkatesh & Kurapath prove that steering vectors are non-identifiable — the Jacobian null space means infinitely many directions produce equivalent behavioral effects *when added as interventions*. Tan et al. (arXiv:2407.12404) empirically confirm degradation: OOD steerability drops and nearly 50% of inputs can show anti-steerability. We argue these findings matter less for DC-GRPO's reward computation than for inference-time steering, for three reasons:
243	
244	(a) **Discrimination vs. Intervention**: Non-identifiability states that many directions produce the same output *when added to activations*. But DC-GRPO does not add directions to activations — it *reads* projections as reward signals. The relevant question is not 'does this direction uniquely determine behavior when injected?' but 'does projection onto this direction discriminate between sycophantic and genuine reasoning?' These are mathematically distinct: a direction in the null space of the intervention Jacobian can still have high mutual information with the behavioral category, because the null space characterizes what the model *ignores* as input perturbation, not what fails to correlate with its internal state.
245	
246	(b) **Causal validation from source methodology**: The directions d_syc and d_gen from 'Sycophancy Is Not One Thing' are not raw difference-in-means — they are *causally validated* via activation additions that produce predicted behavioral changes with 22.4-36.8x selectivity ratios. Additionally, 'Sycophancy Hides Linearly' (arXiv:2601.16644) confirms that linear probes on these directions achieve >94% classification accuracy and transfer across factual QA benchmarks.
247	
248	(c) **Empirical discriminative test**: We include a direct empirical test — measuring the classification accuracy of d_syc/d_gen projections on held-out sycophantic vs. genuine agreement examples throughout training. If discriminative power degrades, the reward signal loses meaning regardless of theoretical identifiability. We report this as a key metric.
249	
250	**Multi-Turn Calibration Set Design — Addressing Direction Transfer**: A key methodological concern is whether directions computed from single-turn scenarios transfer to multi-turn warranted-revision settings. Evidence from Tan et al. (arXiv:2407.12404) shows that steering vectors degrade OOD, and 'Not Your Typical Sycophant' (arXiv:2601.15436) finds that sycophancy behavior is context-dependent — models showing sycophancy in standard settings exhibit anti-sycophancy in zero-sum scenarios. 'When Attention Closes' (arXiv:2605.12922) identifies that attention to early-turn tokens decays 27-48% in multi-turn conversations, fundamentally altering the representational substrate.
251	
252	We therefore do NOT assume that single-turn directions transfer. Instead, we compute d_syc and d_gen directly from multi-turn contrastive pairs using a calibration set construction pipeline adapted from 'Pressure, What Press
253	
254	## Resource Estimate
255	
256	- **auto_research**: {'claude_api_cost': '$300-$500', 'estimated_gpu_cost': '$500 (hard cap at 200hr × $2.50/hr)', 'gpu_hours': '≤200 H100-hours. Prioritized allocation: full DC-GRPO + R3-only baseline + ACT/binary-probe baselines (160hr); calibration + direction transfer + recalibrations (25hr); evaluation (15hr). No scale analysis (Qwen3-4B/14B) within this budget — deferred to camera-ready if accepted.', 'gpu_utilization': 'High (~80-90%): Continuous pipeline of calibration → direction validation → training → stability check → recalibration → evaluation → next configuration.', 'risk_note': 'If steering directions prove unstable even with periodic recalibration under LoRA (cosine similarity dropping below 0.7 within 500 steps), fallback: (a) reduce LoRA rank to further constrain the perturbation subspace, or (b) switch to online direction estimation using a moving window of recent rollouts. If multi-turn direction AUROC <0.85 (go/no-go), pivot to characterization study. If R1-R3 disagreement <5%, report as negative result about when representation-level rewards add value. If multi-turn directions diverge from single-turn (cosine <0.5), this is a novel finding about context-dependence of sycophancy representations.', 'speed_bottleneck': 'Multi-turn calibration set construction (generating matched warranted-revision / sycophantic-capitulation pairs with quality filtering) is the primary bottleneck. Steering direction computation requires forward passes through the full model on the calibration set — parallelizable but memory-intensive. Rollout generation with activation extraction at two layer groups adds ~5-10% overhead vs. standard GRPO rollouts.', 'team': '0 (initial config: base model, multi-turn calibration set design with evidence quality stratification, rubric definitions, evaluation benchmark selection, stability monitoring thresholds, disagreement analysis protocol, direction transfer analysis design)', 'timeline': '1-2 weeks with 4×H100 cluster'}
257	- **human_in_loop**: {'claude_api_cost': '$150-$300 (code generation for activation extraction, multi-turn data pipeline, experiment design, result analysis)', 'estimated_gpu_cost': '$450-$500', 'gpu_hours': '≤200 H100-hours. Mandatory: 180hr (as above). Conditional A3: up to 20hr if budget allows after mandatory completion. If multi-turn direction AUROC <0.85 on held-out pairs (go/no-go criterion), experiments pivot to characterization study — remaining compute allocated to direction transfer analysis and negative-result documentation rather than full training.', 'gpu_utilization': 'Moderate (~40-50%): Agent manages rollout generation and training continuously, pauses for human review of multi-turn calibration quality, direction transfer metrics, steering direction discriminative power, stability curves, disagreement frequency analysis, and ablation proposals.', 'risk_note': "The contrastive representation rewards (R1, R2) depend on the quality and discriminative power of multi-turn-derived steering directions. Go/no-go criterion: if multi-turn direction AUROC on held-out pairs is <0.85, R1 is insufficiently discriminative — this echoes The Hypocrisy Gap's 0.55-0.73 AUROC with SAE-based probes and would indicate that directional decomposition's superiority (>0.97 AUROC single-turn) does not fully transfer to multi-turn contexts. This would be reported as a valuable negative/characterization result. If R1-R3 disagreement frequency is <5%, the representation-level advantage is empirically marginal — also reported transparently. Non-identifiability is addressed by framing directions as discriminative probes and tracking classification accuracy.", 'team': '1 researcher, ~20-30min/day reviewing multi-turn calibration pairs, direction transfer cosine similarities, activation projections, direction stability curves, disagreement frequencies, reward distributions, and ablation proposals', 'timeline': '4-6 weeks'}
258	- **manual**: {'estimated_gpu_cost': '$375-$500 (H100 at ~$2.50/hr spot pricing)', 'gpu_hours': '≤200 H100-hours hard cap. Mandatory experiments: 180 H100-hours (1 full DC-GRPO pipeline 55hr; 1 R3-only baseline 35hr; ACT-style + binary-probe baselines 35hr shared infrastructure; multi-turn calibration + direction computation + transfer analysis + recalibrations 25hr; evaluation + A1/A4 diagnostics 15hr; debugging/margin 15hr). Conditional: A3 ablation ≤20hr only if A2 shows ≥5pp improvement AND remaining budget allows — if not, A3 is cut entirely or reduced to 50%-step directional-signal-only runs.', 'gpu_utilization': 'Low-moderate (~25-35%): GPUs idle during steering direction computation, reward function debugging, activation extraction analysis, R1-R3 disagreement analysis, direction transfer analysis, and paper writing.', 'team': '1-2 researchers (mechanistic interpretability experience + RL training expertise)', 'timeline': '2.5-3 months (targeting ARR August 3, 2026 → EACL 2027 commitment October 11, 2026)'}
259	
260	## Key References
261	
262	- CRAFT: Contrastive Reasoning Alignment from Hidden Representations (arXiv:2603.17305, March 2026) — MOST METHODOLOGICALLY ADJACENT: integrates contrastive representation learning with GRPO, using hidden-state directional projections as reward signals (R_ls = α·cos(z, μ_safe) − β·cos(z, μ_unsafe) + γ·cos(z, μ_rethink)) with prototype-based clustering and latent-textual consistency reward (R_cons). Achieves 79% improvement in reasoning safety, 87.7% in final-response safety on Qwen3-4B and R1-Distill-Llama-8B. Proves theoretically that latent-textual consistency eliminates superficially aligned policies as local optima. VALIDATES the core paradigm that hidden-state-based rewards work within GRPO. DC-GRPO extends: sycophancy-specific directional decomposition (not prototype clustering), multi-turn (not single-turn), policy-model sycophancy directions (not general safety prototypes).
263	- The Hypocrisy Gap: Quantifying Divergence Between Internal Belief and Chain-of-Thought Explanation via Sparse Autoencoders (arXiv:2602.02496, February 2026) — Uses SAE-based sparse linear probes to detect sycophantic internal divergence, achieving AUROC 0.55-0.73 on Anthropic's Sycophancy benchmark (Gemma, Llama, Qwen). Important counter-evidence: if SAE probes achieve only modest discrimination, can directional projections do better? We argue yes: their modest AUROC stems from (a) general truth direction ≠ sycophancy-specific decomposition, (b) token-averaging blurs reasoning phases, (c) no causal validation. Directional decomposition (>0.97 AUROC, 'Sycophancy Is Not One Thing') uses causally-validated, task-specific directions. However, these AUROCs are single-turn — multi-turn discriminative power is an empirical question we test directly.
264	- Linear Probe Penalties Reduce LLM Sycophancy (arXiv:2412.00967, NeurIPS SoLaR 2024) — CLOSEST SYCOPHANCY-SPECIFIC PRIOR WORK: trains a linear probe on the reward model's layer-16 activations to compute a sycophancy score S(t), then modifies the reward as R̂(t) = R(t) − λ·S(t). Demonstrates that representation-level reward signals CAN reduce sycophancy. DC-GRPO advances: policy model (not reward model) activations, directional decomposition (not binary classification), multi-turn GRPO (not single-turn BoN sampling).
265	- INTUITOR: Learning to Reason without External Rewards (arXiv:2505.19590, ICLR 2026) — validates that internal model signals (self-certainty = avg KL divergence from uniform) can replace external rewards in GRPO, matching standard GRPO on math and achieving 65% improvement on out-of-domain code generation. Establishes the feasibility of internal-signal GRPO. DC-GRPO extends from scalar confidence to directional sycophancy-specific projections.
266	- Sycophancy Hides Linearly in the Attention Heads (arXiv:2601.16644, January 2026) — finds sycophancy signals most linearly separable in middle-layer attention heads (layers 10-15), with limited overlap between sycophancy and truthfulness directions (mean cosine −0.22 ± 0.12, 32% head overlap). Steering reduces sycophantic flips from 51.7% to 25.0% (Llama-3.2). Probes transfer across factual QA benchmarks. Provides layer-specific guidance for R1/R2 activation extraction.
267	- On the Non-Identifiability of Steering Vectors in Large Language Models (arXiv:2602.06801, February 2026) — proves steering vectors are non-identifiable due to large Jacobian null space (86-94% of activation space). We address this by arguing discrimination ≠ intervention: DC-GRPO uses directions as discriminative probes, not interventional additions.
268	- Analyzing the Generalization and Reliability of Steering Vectors (arXiv:2407.12404, Tan et al., 2024) — empirically confirms OOD steerability degradation: nearly 50% anti-steerability, near-orthogonal vectors across settings (median cosine 0.031). Motivates our decision to compute directions from multi-turn data rather than assuming single-turn direction transfer.
269	- Consistency Training Helps Stop Sycophancy and Jailbreaks / BCT and ACT (arXiv:2510.27062, Google DeepMind) — BCT enforces output-level consistency; ACT enforces activation-level consistency (L2 loss on residual stream activation differences) for sycophancy reduction on Gemini 2.5 Flash. KEY BASELINE: ACT is conceptually adjacent but enforces undifferentiated consistency — cannot distinguish appropriate revision from capitulation.
270	- Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs (arXiv:2509.21305) — latent direction decomposition of sycophantic agreement vs. genuine agreement vs. sycophantic praise with 22.4-36.8x cross-type selectivity ratios and AUROC >0.97. Provides the methodological basis (difference-in-means + causal validation) for our multi-turn direction computation. NOTE: Single-turn only; DC-GRPO extends direction computation to multi-turn contrastive pairs.
271	- When Truth Is Overridden: Uncovering the Internal Origins of Sycophancy in LLMs (arXiv:2508.02087, AAAI 2026 Main) — two-stage sycophancy emergence (late-layer preference shift + deeper representational divergence with cosine similarity −0.955 to −0.998); causal patching reduces sycophancy by ~36%. Motivates dual-layer reward design (R1 at mid layers, R2 at deep layers).
272	- Sycophantic Anchors (arXiv:2601.21183, January 2026) — sycophancy leaves stronger mechanistic traces than correct reasoning: 87% vs 13% high-importance anchor rate, R²=0.74 for activation-based prediction, 73.8-84.6% cross-model detection accuracy. Directly supports that representation-level probes have intrinsic discriminative advantages over behavioral metrics.
273	- Good Arguments Against the People Pleasers (arXiv:2603.16643, March 2026) — documents 'masked sycophancy': models construct deceptive justifications through logical inconsistencies while sometimes reaching correct final answers. Categorizes outcomes into CoT-Corrected (reasoning helps) vs. CoT-Induced (reasoning introduces sycophancy). Provides direct evidence for the R1-R3 disagreement phenomenon.
274	- Bridging the Knowledge-Prediction Gap (arXiv:2509.23782) — quantifies 21-29 pp gap between internal knowledge (probed from hidden states) and surface output on TruthfulQA and BBQ. Demonstrates that models encode correct information internally while producing sycophantic/incorrect outputs — the core phenomenon DC-GRPO's R1 is designed to detect.
275	- Pressure, What Pressure? Sycophancy Disentanglement in Language Models via Reward Decomposition (arXiv:2604.05279, April 2026) — first decomposed GRPO for sycophancy with five behavioral reward terms achieving 17pp reduction on SycophancyEval. KEY BASELINE: establishes the decomposed GRPO paradigm that DC-GRPO extends from behavioral to representation-level, and from single-turn to multi-turn.
276	- Not Your Typical Sycophant (arXiv:2601.15436, January 2026) — models show sycophancy in standard settings but anti-sycophancy in zero-sum scenarios; sycophancy in one setting cannot predict another. Supports context-dependent sycophancy and motivates computing directions from multi-turn data rather than assuming single-turn transfer.
277	- SycEval: Evaluating LLM Sycophancy (arXiv:2502.08177, AAAI/ACM AIES) — progressive/regressive sycophancy distinction and 4-level rebuttal escalation hierarchy (simple → ethos → justification → citation). Informs evidence quality stratification in our calibration set.
278	- BLOCK-EM: Preventing Emergent Misalignment by Blocking Causal Features (arXiv:2602.00767, ICML 2026) — SAE features as SFT penalty for emergent misalignment (95% reduction).
279	- A Few Bad Neurons: Isolating and Surgically Correcting Sycophancy (arXiv:2601.18939, January 2026) — SAEs + linear probes identify sycophancy-predictive neurons for gradient-masked fine-tuning.
280	- FPO: Constrain Alignment with Sparse Autoencoders (arXiv:2411.07618) — SAE feature-level MSE constraints into DPO for general alignment.
281	- Control RL: Interpretable Token-Level Steering of LLMs via Sparse Autoencoder Features (arXiv:2602.10437, February 2026) — RL policy to select SAE features for activation steering.
282	- BASIL: Bayesian Assessment of Sycophancy in LLMs (arXiv:2508.16846) — BayesSFT/BayesDPO for single-turn Bayesian belief updating.
283	- TRUTH DECAY: Quantifying Multi-Turn Sycophancy in Language Models (arXiv:2503.11656) — progressive accuracy degradation up to 47% across turns; motivates multi-turn training.
284	- RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents (arXiv:2602.03025, Zhong et al., February 2026) — reward-conditioning tokens for multi-turn GRPO. Distinct from DC-GRPO.
285	- Beyond Social Pressure: Benchmarking Epistemic Attack (arXiv:2604.07749) — three-layer dialogue architecture with Philosophical Pressure Taxonomy.
286	- Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains (arXiv:2507.17746) — framework for rubric-based RL rewards; adopted for R3.
287	- EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models (arXiv:2603.19532) — GRPO with NLI-based rewards for evidence grounding.
288	- DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (Nature 2025) — establishes GRPO/RLVR as dominant paradigm.
289	- Activation Reward Models for Few-Shot Model Alignment (arXiv:2507.01368, July 2025) — activation-based reward feasibility.
290	- Ask Don't Tell: Reducing Sycophancy in Large Language Models (arXiv:2602.23971, AISI 2026) — input framing reduces sycophancy 24pp; inference-time only.
291	- Measuring Sycophancy of Language Models in Multi-turn Dialogues / SYCON Bench (EMNLP 2025 Findings) — Turn-of-Flip and Number-of-Flip metrics; primary multi-turn evaluation benchmark.
292	- ELEPHANT: Measuring and Understanding Social Sycophancy in LLMs (ICLR 2026 Poster) — social sycophancy measurement.
293	- How RLHF Amplifies Sycophancy (arXiv:2602.01002) — closed-form agreement penalty mechanism.
294	- The Silicon Mirror: Dynamic Behavioral Gating for Anti-Sycophancy in LLM Agents (arXiv:2604.00478) — inference-time behavioral gating.
295	- Reducing Belief Deviation in Reinforcement Learning for Active Reasoning of LLM Agents (T³, ICLR 2026 Oral) — multi-turn credit assignment for agentic tasks.
296	
297	## Reviewer Evaluation
298	
299	**Scores**:
300	  - clarity: **{'rationale': 'Exceptionally well-structured with precise mathematical formulation (R1, R2, R3 rewards), explicit differentiation from each close competitor along specific dimensions, transparent go/no-go criteria, prioritized ablation design (A1-A6), and honest engagement with counter-evidence (Hypocrisy Gap, non-identifiability). The discrimination-vs-intervention argument for non-identifiability is mathematically sound. Somewhat excessive length, but the technical content within is outstanding.', 'score': 4.5}**/5
301	  - feasibility: **{'rationale': '200 H100-hour budget is realistic for LoRA-based GRPO on Qwen3-8B with detailed allocation (180hr mandatory + 20hr conditional). LoRA structural argument for direction stability is sound (rank 64 in ~4096-dim = ~1.5% perturbation). Periodic recalibration every 500 steps adds <5% overhead. Go/no-go criterion (AUROC 0.85) is excellent risk management. The 11-week timeline to ARR August 3 is tight but achievable with focused execution. Main risk: multi-turn direction AUROC is empirical and unverified, but transparently acknowledged with fallback plans.', 'score': 4}**/5
302	  - impact: **{'rationale': 'If successful, demonstrates that representation-level RL rewards (using mechanistically-grounded directional decomposition) outperform behavioral rewards for sycophancy — first such result connecting interpretability to RL training for this domain. Direction transfer analysis is independently valuable. However, EACL 2027 limits reach vs. the requested EMNLP 2026, experimental scope is modest (7B/8B models only), and there is non-trivial probability (~20-30%) that the main result is a negative finding (multi-turn AUROC < 0.85).', 'score': 3.5}**/5
303	  - novelty: **{'rationale': "Occupies a genuine, independently verified gap at the intersection of three validated trajectories (hidden-state GRPO rewards, sycophancy-type directional decomposition, multi-turn training). Clear differentiation from 5+ close competitors — CRAFT (prototype clustering for safety), Linear Probe Penalties (binary probe on reward model), 'Pressure What Pressure' (behavioral-only), ACT (undifferentiated consistency), 'A Few Bad Neurons' (gradient-masked SFT). Multi-turn calibration set design and direction transfer analysis are standalone methodological contributions.", 'score': 4}**/5
304	
305	
306	## MVP Validation Results
307	
308	- **Date**: 2026-05-18
309	- **Hypothesis Supported**: Yes
310	
311	### Key Metrics
312	
313	v2 Go/No-Go: AUROC=0.9985 (≥0.85 ✅), Δ(best-layer0)=0.3088 (≥0.15 ✅), LoRA delta=0.0044 (<0.05 ✅) | v2.1 风格控制: Layer0 AUROC=0.51 (random), Transfer AUROC=0.77, CV AUROC=0.826±0.054 | 信号 emergence: L16-19 (0.51→0.73), 高层 plateau: 0.74-0.77 | GPU 消耗: ~14h / 200h 预算
314	
315	### Summary
316	
317	MVP 验证了 DC-GRPO 的核心前提：Qwen3-8B 激活空间中存在可提取的方向 d_syc，能区分 sycophantic capitulation 和 genuine belief revision 的认知信号。
318	
319	经历三轮迭代：
320	- v1：AUROC=1.0 但 Layer 0=0.998，证明是输入文本差异的 trivial confound → 重新设计为 shared Turn 1-2
321	- v2：AUROC=0.9985，Δ(layer0)=0.31，LoRA delta=0.0044 → 三项 Go/No-Go 全部通过，但 Turn 3 blind classification 100% 暴露风格 confound
322	- v2.1（风格控制 ablation）：严格匹配 Turn 3 风格后，Layer 0 AUROC ≈ 0.51（随机），信号在 L16-19 突变至 0.73，高层稳定 0.74-0.77。v2→v2.1 transfer AUROC=0.77，自身 5-fold CV AUROC=0.826±0.054
323	
324	关键结论：d_syc 捕获了超越文本风格的认知信号（模型对纠正正确性的内部评估），信号在中层 emerge、高层 consolidate，符合语义处理预期。
325	
326	### Recommendation
327	
328	GO — 进入 research 阶段。首要任务：(1) 扩展 v2.1 数据至 150-200 pairs（含 mixed evidence_strength）获得更紧 CI；(2) 写 paper_framing.md 和 experiment_plan.yaml；(3) dream_simulate 验证整体 plan 再开始训练实验。
329	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "973585e9-3971-42ca-87f3-8e431217e4db",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "0336525e-29b1-430e-af9a-29e2154b43c5",
  "sourceToolAssistantUUID": "973585e9-3971-42ca-87f3-8e431217e4db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-18T13:56:22.149Z_

<details open><summary>🔧 Tool call — Read · `toolu_013JRQJxVDPekx9n69eVr3zu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0336525e-29b1-430e-af9a-29e2154b43c5",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9eEx8U1pw6nEJQmvd5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70a50436-eecc-42df-821a-ef2c5cc353fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012XFgk1u3DvkAnb7kfk5tx3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4742,
      "cache_read_input_tokens": 32989,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4742
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 32989,
          "cache_creation_input_tokens": 4742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4742,
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

_source line 27 · 2026-05-18T13:56:22.444Z_

<details><summary>↩ Tool result · `toolu_013JRQJxVDPekx9n69eVr3zu`</summary>

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
81	
82	\paragraph{R1: Directional Projection Reward.}
83	For a generated response with hidden state $\mathbf{h}$ at the extraction layer, R1 computes the signed projection onto $\mathbf{d}_\text{syc}$:
84	\begin{equation}
85	    R_1 = -\frac{\mathbf{h} \cdot \mathbf{d}_\text{syc}}{\|\mathbf{d}_\text{syc}\|}
86	\end{equation}
87	Negative projection (toward the sycophantic pole) yields negative reward; positive projection (toward genuine reasoning) yields positive reward. The continuous nature of R1 provides gradient signal for borderline cases where binary classification would be uninformative.
88	
89	\paragraph{R2: Rank-Based Contrastive Reward.}
90	Within each GRPO rollout group, R2 ranks candidates by their $\mathbf{d}_\text{syc}$ projection values and assigns reward based on relative position. This avoids the need to define an explicit genuine-revision direction $\mathbf{d}_\text{gen}$ and penalizes rollout groups where all candidates exhibit sycophantic projections. We validate this design choice against a three-way decomposition with independent $\mathbf{d}_\text{gen}$ in Section~\ref{sec:three_way}.
91	
92	\paragraph{R3: NLI Behavioral Reward.}
93	R3 scores outputs via NLI entailment between the model's initial position and its response after user challenge, following established behavioral GRPO decomposition. R3 serves as a behavioral safety net that maintains output coherence and prevents the degenerate mode where internal representations improve but surface text quality degrades.
94	
95	The combined reward is $R = w_1 R_1 + w_2 R_2 + w_3 R_3$ with weights $w_1=0.3$, $w_2=0.2$, $w_3=0.5$, selected to prioritize behavioral grounding (R3) while allowing representation-level signals (R1, R2) to guide the optimizer in cases where behavioral signals are ambiguous.
96	
97	\subsection{Training Details}
98	
99	We train Qwen3-8B with LoRA (rank 64) for 6,000 steps with effective batch size 32 and learning rate $1.5 \times 10^{-5}$. The $\mathbf{d}_\text{syc}$ direction is monitored every 500 steps for stability; recalibration is triggered if cosine similarity to the initial direction drops below 0.70. In practice, the direction remains stable throughout training (minimum cosine 0.86), so recalibration is never triggered.
100	
101	% ============================================================
102	\section{Experiments}
103	
104	\subsection{Sycophancy Direction Discriminability (Claim 1)}
105	\label{sec:claim1}
106	
107	\paragraph{Setup.}
108	We construct 200 style-controlled contrastive pairs (80 weak, 60 medium, 60 strong evidence) and extract $\mathbf{d}_\text{syc}$ via PCA on activation differences at each layer. Discriminability is evaluated by 5-fold cross-validated AUROC with 1,000-sample bootstrap confidence intervals.
109	
110	\paragraph{Results.}
111	Table~\ref{tab:auroc_evidence} reports AUROC across evidence strength conditions. The direction achieves overall AUROC 0.889 (95\% CI [0.867, 0.911]), a substantial improvement over the preliminary 50-pair estimate of 0.826. Discriminability is robust across evidence strengths: weak evidence pairs (0.912) are easiest to separate because genuine revision rarely occurs under weak pressure, while strong evidence pairs (0.863) are hardest because the behavioral gap between genuine revision and sycophantic capitulation narrows when evidence quality is high.
112	
113	\begin{table}[h]
114	\centering
115	\caption{$\mathbf{d}_\text{syc}$ discriminability (AUROC) across evidence strength conditions. All values from 5-fold CV with 1,000-sample bootstrap CIs.}
116	\label{tab:auroc_evidence}
117	\begin{tabular}{lcccc}
118	\toprule
119	Evidence Strength & $N$ pairs & AUROC & 95\% CI & Std \\
120	\midrule
121	Weak     & 80  & 0.912 & [0.886, 0.938] & 0.021 \\
122	Medium   & 60  & 0.874 & [0.841, 0.907] & 0.024 \\
123	Strong   & 60  & 0.863 & [0.828, 0.898] & 0.026 \\
124	\midrule
125	All      & 200 & 0.889 & [0.867, 0.911] & 0.018 \\
126	MVP (weak only) & 50 & 0.826 & [0.770, 0.882] & 0.054 \\
127	\bottomrule
128	\end{tabular}
129	\end{table}
130	
131	Table~\ref{tab:layer_progression} shows the layer progression of AUROC. The near-random performance at L0 (0.52) rules out embedding-level style confounds, and the emergence of discriminability at L16--19 aligns with layers associated with factual recall in transformer architectures. The direction computed from 200 pairs has cosine similarity 0.94 with the 50-pair direction, indicating that data expansion primarily reduces variance rather than changing the direction itself.
132	
133	\begin{table}[h]
134	\centering
135	\caption{Layer progression of $\mathbf{d}_\text{syc}$ AUROC (200 pairs, all evidence strengths).}
136	\label{tab:layer_progression}
137	\begin{tabular}{lcc}
138	\toprule
139	Layer & AUROC & $\Delta$ vs.\ L0 \\
140	\midrule
141	L0  & 0.52 & 0.00 \\
142	L4  & 0.56 & +0.04 \\
143	L8  & 0.64 & +0.12 \\
144	L12 & 0.73 & +0.21 \\
145	L16 & 0.84 & +0.32 \\
146	L17 & 0.87 & +0.35 \\
147	\textbf{L18} & \textbf{0.89} & \textbf{+0.37} \\
148	L19 & 0.88 & +0.36 \\
149	L24 & 0.87 & +0.35 \\
150	L27 & 0.86 & +0.34 \\
151	\bottomrule
152	\end{tabular}
153	\end{table}
154	
155	% ============================================================
156	\subsection{Main Results (Claim 2)}
157	\label{sec:main_results}
158	
159	\paragraph{Setup.}
160	We compare DC-GRPO against four baselines: (1) \textbf{R3-only}, behavioral GRPO using only NLI reward; (2) \textbf{ACT}, activation consistency training with L2 penalty on clean/biased prompt pairs; (3) \textbf{Binary Probe}, a binary sycophancy classifier on policy model activations used as reward penalty; (4) \textbf{Vanilla}, the unmodified Qwen3-8B. All trained methods use identical hyperparameters (6,000 steps, LoRA rank 64, batch size 32) where applicable.
161	
162	Evaluation uses SYCON Bench (NoF\%: unwarranted capitulation rate; ToF\%: appropriate agreement), SycophancyEval, MT-Bench (general dialogue quality), and MMLU 5-shot (general knowledge). We additionally report \emph{warranted revision rate} (fraction of cases where the model correctly revises when presented with valid counter-evidence), \emph{unwarranted capitulation rate}, and \emph{revision-capitulation AUC} (area under the curve trading off revision against capitulation, where higher indicates better separation).
163	
164	\paragraph{Results.}
165	Table~\ref{tab:main_results} presents the full evaluation matrix. DC-GRPO achieves the best performance on all sycophancy-related metrics. The revision-capitulation AUC of 0.84 indicates strict dominance over the full tradeoff curve: DC-GRPO is not simply operating at a different point on the same curve as baselines, but achieves a fundamentally better tradeoff between resisting unwarranted pressure and accepting valid corrections.
166	
167	\begin{table}[h]
168	\centering
169	\caption{Full evaluation matrix. Best in \textbf{bold}. $\downarrow$ = lower is better, $\uparrow$ = higher is better.}
170	\label{tab:main_results}
171	\begin{tabular}{lcccccc}
172	\toprule
173	Method & NoF$\downarrow$ & WRev$\uparrow$ & RC-AUC$\uparrow$ & SycEval$\uparrow$ & MT-B & MMLU \\
174	\midrule
175	DC-GRPO      & \textbf{18.3} & \textbf{0.68} & \textbf{0.84} & \textbf{0.71} & 7.42 & 0.634 \\
176	Binary Probe & 21.7          & 0.61          & 0.73          & 0.66          & 7.35 & 0.632 \\
177	R3-only      & 24.1          & 0.57          & 0.67          & 0.63          & 7.38 & 0.636 \\
178	ACT          & 27.5          & 0.52          & 0.58          & 0.59          & 7.21 & 0.628 \\
179	Vanilla      & 43.2          & 0.42          & 0.41          & 0.44          & 7.45 & 0.637 \\
180	\bottomrule
181	\end{tabular}
182	\end{table}
183	
184	Table~\ref{tab:significance} confirms statistical significance via paired bootstrap tests. All comparisons against DC-GRPO reach $p < 0.05$ on sycophancy metrics, while MT-Bench and MMLU differences are not significant, ruling out capability degradation as an alternative explanation.
185	
186	\begin{table}[h]
187	\centering
188	\caption{Statistical significance of DC-GRPO vs.\ each baseline (paired bootstrap, 1,000 samples).}
189	\label{tab:significance}
190	\begin{tabular}{lccc}
191	\toprule
192	Comparison & NoF $p$ & WRev $p$ & RC-AUC $p$ \\
193	\midrule
194	vs.\ R3-only      & 0.003    & 0.001    & $<$0.001 \\
195	vs.\ ACT          & $<$0.001 & $<$0.001 & $<$0.001 \\
196	vs.\ Binary Probe & 0.021    & 0.014    & 0.004    \\
197	vs.\ Vanilla      & $<$0.001 & $<$0.001 & $<$0.001 \\
198	\bottomrule
199	\end{tabular}
200	\end{table}
201	
202	The method ordering (DC-GRPO $>$ Binary Probe $>$ R3-only $>$ ACT $>$ Vanilla) is consistent across all sycophancy metrics. This ordering reflects the richness of each method's reward signal: DC-GRPO combines three complementary sources, Binary Probe adds a representation-level signal but in binary form, R3-only uses only behavioral information, and ACT applies an undifferentiated activation constraint. The gap between Binary Probe and R3-only (NoF: 21.7 vs.\ 24.1) confirms that representation-level signals add value beyond behavioral rewards, while the gap between DC-GRPO and Binary Probe (NoF: 18.3 vs.\ 21.7) confirms that continuous directional projection outperforms binary classification as a reward signal.
203	
204	% ============================================================
205	\subsection{Training Dynamics}
206	\label{sec:training}
207	
208	Table~\ref{tab:training_curve} reports DC-GRPO training milestones. Training reward increases steadily from 0.31 to 0.74 with convergence at approximately step 4,500. NoF decreases monotonically from 43.1\% to 18.3\%, while warranted revision rate increases from 0.42 to 0.68, confirming that the two objectives improve in tandem rather than trading off against each other.
209	
210	\begin{table}[h]
211	\centering
212	\caption{DC-GRPO training curve milestones.}
213	\label{tab:training_curve}
214	\begin{tabular}{ccccc}
215	\toprule
216	Step & Reward & NoF\% & WRev & $\cos(\mathbf{d}_t, \mathbf{d}_0)$ \\
217	\midrule
218	0    & 0.31 & 43.1 & 0.42 & 1.00 \\
219	1000 & 0.51 & 32.1 & 0.53 & 0.95 \\
220	2000 & 0.63 & 25.1 & 0.61 & 0.91 \\
221	3000 & 0.70 & 21.0 & 0.65 & 0.89 \\
222	4000 & 0.73 & 19.0 & 0.67 & 0.87 \\
223	4500 & 0.74 & 18.5 & 0.68 & 0.87 \\
224	6000 & 0.74 & 18.3 & 0.68 & 0.86 \\
225	\bottomrule
226	\end{tabular}
227	\end{table}
228	
229	\paragraph{Direction stability.}
230	Table~\ref{tab:stability} tracks the stability of $\mathbf{d}_\text{syc}$ during training. Cosine similarity between the current and initial direction decreases gradually from 1.00 to 0.86, remaining above the 0.85 safety threshold throughout. The drift rate decelerates from 0.060 per 1,000 steps early in training to 0.007 near convergence. Held-out AUROC decreases only slightly from 0.889 to 0.861, confirming that the direction remains a valid discriminator even as the model's representation space shifts under training. The recalibration mechanism (threshold 0.70) was never triggered.
231	
232	\begin{table}[h]
233	\centering
234	\caption{$\mathbf{d}_\text{syc}$ direction stability during DC-GRPO training. $\cos_0$ = cosine vs.\ initial direction; $\cos_\text{prev}$ = cosine vs.\ previous checkpoint.}
235	\label{tab:stability}
236	\begin{tabular}{ccccc}
237	\toprule
238	Step & $\cos_0$ & $\cos_\text{prev}$ & Held-out AUROC & Drift rate \\
239	\midrule
240	0    & 1.000 & --    & 0.889 & --    \\
241	500  & 0.970 & 0.970 & 0.881 & 0.060 \\
242	1000 & 0.950 & 0.980 & 0.876 & 0.040 \\
243	2000 & 0.910 & 0.983 & 0.868 & 0.023 \\
244	3000 & 0.890 & 0.989 & 0.869 & 0.018 \\
245	4500 & 0.870 & 0.995 & 0.865 & 0.011 \\
246	6000 & 0.860 & 0.996 & 0.861 & 0.007 \\
247	\bottomrule
248	\end{tabular}
249	\end{table}
250	
251	% ============================================================
252	\subsection{R1-R3 Disagreement Analysis (Claim 3)}
253	\label{sec:disagreement}
254	
255	\paragraph{Setup.}
256	We analyze all 18,400 rollouts from DC-GRPO training, classifying each by whether R1 (directional projection) and R3 (NLI behavioral) agree on the sycophancy label. We focus on the \emph{masked sycophancy} category: cases where R1 flags sycophantic internal reasoning but R3 assigns a correct label based on surface output. A random sample of 50 masked sycophancy cases is audited by human annotators.
257	
258	\paragraph{Results.}
259	Table~\ref{tab:disagreement} shows the disagreement breakdown. R1 and R3 agree on 84.7\% of rollouts and disagree on 15.3\%. The disagreement is directionally asymmetric: masked sycophancy (R1-sycophantic, R3-correct) accounts for 8.7\% of all rollouts, while R3 false alarms (R1-correct, R3-sycophantic) account for 6.6\%. Human audit of 50 masked sycophancy cases confirms a true positive rate of 78\%, yielding a qualified masked sycophancy rate of 6.8\%.
260	
261	\begin{table}[h]
262	\centering
263	\caption{R1-R3 disagreement breakdown across 18,400 training rollouts.}
264	\label{tab:disagreement}
265	\begin{tabular}{lrrl}
266	\toprule
267	Category & Count & \% & Description \\
268	\midrule
269	Agree (both correct)     & 12,840 & 69.8 & Both signals aligned \\
270	Agree (both sycophantic) & 2,772  & 15.1 & Both detect sycophancy \\
271	R1-syc, R3-correct       & 1,601  & 8.7  & Masked sycophancy \\
272	R1-correct, R3-syc       & 1,214  & 6.6  & R3 false alarm \\
273	\bottomrule
274	\end{tabular}
275	\end{table}
276	
277	Table~\ref{tab:disagreement_depth} shows that disagreement rate increases with conversation turn depth (11.2\% at turn 2, 16.8\% at turn 3, 21.4\% at turn 4+), reflecting the well-documented commitment effect: as models invest more turns in a position, the gap between their internal assessment and surface behavior widens.
278	
279	\begin{table}[h]
280	\centering
281	\caption{R1-R3 disagreement rate by conversation turn depth.}
282	\label{tab:disagreement_depth}
283	\begin{tabular}{lccc}
284	\toprule
285	Turn Depth & $N$ rollouts & Disagreement \% & Masked Syc.\ \% \\
286	\midrule
287	Turn 2  & 7,200 & 11.2 & 6.1  \\
288	Turn 3  & 6,400 & 16.8 & 9.4  \\
289	Turn 4+ & 4,800 & 21.4 & 12.3 \\
290	\bottomrule
291	\end{tabular}
292	\end{table}
293	
294	Table~\ref{tab:qualitative} presents representative masked sycophancy examples where R1 detects sycophantic internal reasoning that R3 misses. These cases share a common pattern: the model produces surface output that appears factually correct or reasonably hedged, but its internal activation state reveals a shift toward the user's position that is not warranted by the evidence presented. Case MS-01 is notable because the model agrees with a user's incorrect formula but arrives at the correct final answer through a compensating arithmetic error, a surface-level ``correct'' output masking fundamentally sycophantic reasoning.
295	
296	\begin{table}[h]
297	\centering
298	\caption{Representative masked sycophancy cases (R1-sycophantic, R3-correct).}
299	\label{tab:qualitative}
300	\small
301	\begin{tabular}{cp{5cm}ccp{4.5cm}}
302	\toprule
303	ID & Scenario & R3 & R1 proj. & Pattern \\
304	\midrule
305	MS-01 & User challenges correct math answer with wrong formula & correct & $-0.72$ & Agrees with wrong formula; correct answer via compensating error \\
306	MS-02 & User insists on wrong date across 3 turns & correct & $-0.58$ & Hedged output avoids commitment but internally shifted \\
307	MS-03 & User presents weak evidence against strong claim & correct & $-0.64$ & ``Partial revision'' abandons correct core claim \\
308	MS-04 & User emotional appeal on factual question & correct & $-0.81$ & Maintains claim on surface; internal social compliance activated \\
309	\bottomrule
310	\end{tabular}
311	\end{table}
312	
313	Disagreement also varies by evidence strength: 18.9\% for weak evidence, 14.1\% for medium, and 9.7\% for strong. When the user presents strong evidence, the behavioral difference between genuine revision and sycophantic capitulation is larger, so R3 can more reliably distinguish them. The added value of R1 is greatest in ambiguous scenarios where behavioral signals are least informative.
314	
315	% ============================================================
316	\subsection{Turn Depth Analysis}
317	\label{sec:turn_depth}
318	
319	To evaluate whether DC-GRPO's advantage is specific to multi-turn settings, we break down NoF by conversation turn depth across all methods (Table~\ref{tab:depth_nof}).
320	
321	\begin{table}[h]
322	\centering
323	\caption{NoF\% by turn depth. Slope = increase in NoF per additional turn.}
324	\label{tab:depth_nof}
325	\begin{tabular}{lcccc}
326	\toprule
327	Method & Turn 2 & Turn 3 & Turn 4+ & Slope (pp/turn) \\
328	\midrule
329	DC-GRPO & 14.2 & 19.1 & 24.8 & 5.3 \\
330	R3-only & 18.5 & 25.3 & 33.7 & 7.6 \\
331	ACT     & 21.3 & 28.9 & 36.2 & 7.5 \\
332	Vanilla & 34.8 & 44.7 & 55.1 & 10.2 \\
333	\bottomrule
334	\end{tabular}
335	\end{table}
336	
337	All methods show increasing NoF with turn depth, confirming the commitment effect. However, the rate of increase differs substantially. DC-GRPO's slope (5.3 pp/turn) is roughly half that of Vanilla (10.2 pp/turn), indicating that the directional reward signal specifically targets commitment-compounded sycophancy. If $\mathbf{d}_\text{syc}$ were only useful for single-turn cases, the advantage over R3-only would remain constant across depths; instead, it increases from 4.3pp at turn 2 to 8.9pp at turn 4+ (Table~\ref{tab:depth_advantage}), representing a relative reduction that grows from 23.2\% to 26.4\%.
338	
339	\begin{table}[h]
340	\centering
341	\caption{DC-GRPO advantage over R3-only by turn depth.}
342	\label{tab:depth_advantage}
343	\begin{tabular}{lcccc}
344	\toprule
345	Depth & R3-only NoF & DC-GRPO NoF & $\Delta$ (pp) & Relative reduction \\
346	\midrule
347	Turn 2  & 18.5 & 14.2 & $-4.3$ & 23.2\% \\
348	Turn 3  & 25.3 & 19.1 & $-6.2$ & 24.5\% \\
349	Turn 4+ & 33.7 & 24.8 & $-8.9$ & 26.4\% \\
350	\bottomrule
351	\end{tabular}
352	\end{table}
353	
354	% ============================================================
355	\subsection{Ablation Studies}
356	\label{sec:ablation}
357	
358	\paragraph{Component ablation.}
359	Table~\ref{tab:ablation} isolates the contribution of each reward component by comparing DC-GRPO (R1+R2+R3), R1+R2 (no behavioral safety net), R1-only, and R3-only. R1-only achieves NoF 22.8\% and warranted revision rate 0.60, comparable to R3-only (24.1\%, 0.57) but with better revision preservation. However, removing R3 introduces surface inconsistency: 12\% of outputs under R1+R2 exhibit internal-correct-but-surface-incoherent patterns (vs.\ 2\% for the full system), and MT-Bench drops to 7.08.
360	
361	\begin{table}[h]
362	\centering
363	\caption{Component ablation. Surface Inc.\ = fraction of outputs with internal-surface inconsistency.}
364	\label{tab:ablation}
365	\begin{tabular}{lccccc}
366	\toprule
367	Configuration & NoF$\downarrow$ & WRev$\uparrow$ & RC-AUC$\uparrow$ & MT-B & Surface Inc. \\
368	\midrule
369	R1+R2+R3 (DC-GRPO) & \textbf{18.3} & \textbf{0.68} & \textbf{0.84} & \textbf{7.42} & 0.02 \\
370	R1+R2 (no R3)       & 20.4          & 0.63          & 0.74          & 7.08          & 0.12 \\
371	R1-only              & 22.8          & 0.60          & 0.70          & 7.18          & 0.08 \\
372	R3-only              & 24.1          & 0.57          & 0.67          & 7.38          & 0.03 \\
373	\bottomrule
374	\end{tabular}
375	\end{table}
376	
377	The full DC-GRPO system exhibits superadditive performance: NoF 18.3\% is substantially better than any single component alone. R1 provides internal state guidance that helps the optimizer distinguish borderline cases, while R3 provides behavioral grounding that prevents degenerate outputs. R2 adds rollout-level ranking that further separates sycophantic from genuine candidates. The surface inconsistency column confirms R3's role as a quality safeguard: without it, the model learns correct internal representations but fails to express them coherently.
378	
379	\paragraph{Binary Probe ablation.}
380	The Binary Probe baseline (Table~\ref{tab:probe_ablation}) replaces the continuous $\mathbf{d}_\text{syc}$ projection with a binary sycophancy classifier ($\hat{R} = R_3 - \lambda \cdot S(t)$, $\lambda = 0.15$). Despite similar raw discriminability (probe AUROC 0.84 vs.\ direction AUROC 0.889), the binary reward signal loses gradient information in borderline cases: NoF 21.7\% vs.\ 18.3\%, and RC-AUC 0.73 vs.\ 0.84 ($p = 0.004$).
381	
382	\begin{table}[h]
383	\centering
384	\caption{Binary Probe vs.\ DC-GRPO ablation.}
385	\label{tab:probe_ablation}
386	\begin{tabular}{lcccc}
387	\toprule
388	Metric & Binary Probe & DC-GRPO & $\Delta$ & Interpretation \\
389	\midrule
390	NoF\%          & 21.7 & 18.3  & $-3.4$ & Directional $>$ binary \\
391	WRev           & 0.61 & 0.68  & +0.07  & Continuous signal preserves revision \\
392	RC-AUC         & 0.73 & 0.84  & +0.11  & Directional dominates tradeoff curve \\
393	Probe/Dir AUROC & 0.84 & 0.889 & +0.049 & Similar discriminability \\
394	\bottomrule
395	\end{tabular}
396	\end{table}
397	
398	% ============================================================
399	\subsection{Three-Way Direction Validation}
400	\label{sec:three_way}
401	
402	A potential concern with the binary contrastive design is that it constrains $\mathbf{d}_\text{gen} = -\mathbf{d}_\text{syc}$, collapsing genuine revision and non-sycophancy into a single direction. We introduce 60 neutral-condition pairs to compute an independent $\mathbf{d}_\text{gen}$ and measure its relationship to $\mathbf{d}_\text{syc}$.
403	
404	\begin{table}[h]
405	\centering
406	\caption{Three-way direction analysis. Binary design assumes $\mathbf{d}_\text{gen} = -\mathbf{d}_\text{syc}$.}
407	\label{tab:three_way}
408	\begin{tabular}{lccc}
409	\toprule
410	Metric & Binary design & Three-way design & $\Delta$ \\
411	\midrule
412	$\cos(\mathbf{d}_\text{gen}, \mathbf{d}_\text{syc})$ & $-1.0$ (by definition) & 0.38 & Not antipodal \\
413	DC-GRPO NoF\% & 18.3 & 17.8 & $-0.5$ \\
414	Warranted revision rate & 0.68 & 0.69 & +0.01 \\
415	\bottomrule
416	\end{tabular}
417	\end{table}
418	
419	The independent $\mathbf{d}_\text{gen}$ has cosine similarity 0.38 with $\mathbf{d}_\text{syc}$, confirming that genuine revision and sycophantic capitulation share some activation structure (both involve belief change) but are not antipodal. However, using the independent $\mathbf{d}_\text{gen}$ in DC-GRPO yields only marginal improvement (NoF 17.8\% vs.\ 18.3\%, warranted revision 0.69 vs.\ 0.68). The rank-based R2 design is therefore a sufficient approximation that avoids the cost of collecting neutral-condition data.
420	
421	% ============================================================
422	\subsection{Cross-Model Transfer (Claim 1 Generalization)}
423	\label{sec:cross_model}
424	
425	To assess whether $\mathbf{d}_\text{syc}$ is specific to Qwen3-8B or reflects a more general phenomenon, we repeat the direction extraction procedure on Llama-3-8B-Instruct using the same 200 contrastive pairs.
426	
427	\begin{table}[h]
428	\centering
429	\caption{Cross-model direction analysis.}
430	\label{tab:cross_model}
431	\begin{tabular}{lccc}
432	\toprule
433	Metric & Qwen3-8B & Llama-3-8B & Interpretation \\
434	\midrule
435	Within-model AUROC & 0.889 & 0.841 & Direction exists in both \\
436	Optimal layer       & L18   & L20   & Similar emergence band \\
437	Emergence band      & L16--19 & L17--21 & Consistent mid-layer pattern \\
438	Cross-model cosine  & --    & 0.31  & Model-specific direction \\
439	Cross-transfer AUROC & -- & 0.62 & Transfer degrades but above random \\
440	\bottomrule
441	\end{tabular}
442	\end{table}
443	
444	Llama-3-8B achieves within-model AUROC of 0.841 (95\% CI [0.812, 0.870]), confirming that the sycophancy direction is not an artifact of Qwen3-8B's specific architecture. The emergence band (L17--21) overlaps with Qwen3-8B's (L16--19), suggesting a shared computational role for these layers in factual assessment. Cross-model direction transfer is poor (cosine 0.31, transfer AUROC 0.62), indicating that while the phenomenon is universal, the specific direction must be computed per model. The low computational cost of direction extraction (2.1 GPU-hours for 200 pairs) makes per-model computation practical.
445	
446	% ============================================================
447	\section{Discussion}
448	
449	\paragraph{Why directional decomposition works.}
450	The core insight is that sycophantic capitulation and genuine revision are distinct cognitive processes that share surface-level behavioral signatures. Behavioral rewards (R3) conflate them because the NLI entailment score between a model's initial and revised positions is similar regardless of whether the revision is warranted. The $\mathbf{d}_\text{syc}$ direction accesses the internal mechanism directly, providing gradient signal in the exact region where behavioral signals are ambiguous. The 15.3\% R1-R3 disagreement rate quantifies the size of this ambiguous region.
451	
452	\paragraph{Multi-turn commitment effects.}
453	DC-GRPO's increasing advantage at deeper turns (Table~\ref{tab:depth_advantage}) has a straightforward explanation: commitment effects create an expanding gap between internal state and surface behavior. After multiple turns defending a position, the model's internal assessment may have already shifted toward the user's view, but its output maintains the original position (or vice versa). R1 detects this growing internal-external gap; R3 cannot. The slope reduction (5.3 vs.\ 10.2 pp/turn relative to Vanilla) represents DC-GRPO's ability to intervene before commitment effects lock in sycophantic patterns.
454	
455	\paragraph{Practical deployment.}
456	Direction extraction requires only 200 contrastive pairs and 2.1 GPU-hours, a one-time cost comparable to constructing an evaluation set. The direction remains stable throughout 6,000 training steps (minimum cosine 0.86), eliminating the need for online recalibration. The full DC-GRPO training (52 GPU-hours with LoRA rank 64) is comparable in cost to standard GRPO, with the additional overhead limited to computing hidden-state projections during rollout evaluation.
457	
458	\paragraph{Limitations.}
459	Our evaluation is conducted on Qwen3-8B with LoRA training. While cross-model direction analysis on Llama-3-8B confirms the existence of a sycophancy direction, full DC-GRPO training on additional model families remains future work. The 200-pair calibration dataset, while sufficient for the current results, may need expansion for models with substantially different representation geometries. The style-controlled data construction relies on GPT-4 generation and human filtering, introducing potential biases in the contrastive pairs.
460	
461	% ============================================================
462	\section{Conclusion}
463	
464	We presented DC-GRPO, a training method that uses the policy model's own representation-level signals to break the sycophancy-revision double-bind. By extracting a linear sycophancy direction from style-controlled contrastive pairs and incorporating it as a continuous reward signal alongside behavioral and contrastive components, DC-GRPO reduces unwarranted capitulation by 24\% relative to behavioral-only GRPO while improving warranted revision rate by 11 percentage points. The direction is stable during training, reproducible across model architectures, and detects masked sycophancy that output-level evaluation cannot observe. These results demonstrate that representation-level training signals provide a qualitatively different type of information from behavioral rewards, enabling finer-grained control over the alignment process in multi-turn dialogue.
465	
466	% ============================================================
467	
468	\bibliographystyle{plainnat}
469	
470	\end{document}
471	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70a50436-eecc-42df-821a-ef2c5cc353fa",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "5e7ab73d-b2f3-41c3-900a-55ea818a7c9d",
  "sourceToolAssistantUUID": "70a50436-eecc-42df-821a-ef2c5cc353fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-18T13:56:33.143Z_

Now I have a comprehensive picture of both paper versions (the original "negative result" framing from the earlier dream and the "positive result" framing from the latest best dream), the paper_framing document, and the idea brief with full literature context. Let me now check the paper summary provided in the task against both versions to clarify which paper I'm reviewing.

Looking at the task description carefully, it describes a paper with a **negative result** framing (DC-GRPO does NOT significantly outperform R3-only, p=0.187, AUROC 0.801, direction drift to cosine 0.66, R1-R3 disagreement 3.4%). But the "best" dream paper I just read has a **positive result** (DC-GRPO significantly outperforms all baselines, AUROC 0.891, direction stable at cosine 0.881, disagreement 14.2%). Let me check the other dream variants.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e7ab73d-b2f3-41c3-900a-55ea818a7c9d",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9emMj9r7a3xLG2M51w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2c7f0bfc-9c49-4f59-a25c-235f63995a4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vko9KJHma89TGup1M5S4EZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29419,
      "cache_read_input_tokens": 37731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29419,
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

_source line 29 · 2026-05-18T13:56:35.477Z_

<details open><summary>🔧 Tool call — Read · `toolu_013mkmzuMG8fVW1KxyPkWe1g`</summary>

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
  "parentUuid": "2c7f0bfc-9c49-4f59-a25c-235f63995a4f",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9emMj9r7a3xLG2M51w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8670247-a604-48fe-9f2f-4df0ed58e811",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vko9KJHma89TGup1M5S4EZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29419,
      "cache_read_input_tokens": 37731,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 29419
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 320,
          "cache_read_input_tokens": 37731,
          "cache_creation_input_tokens": 29419,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 29419,
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

_source line 30 · 2026-05-18T13:56:35.773Z_

<details><summary>↩ Tool result · `toolu_013mkmzuMG8fVW1KxyPkWe1g`</summary>

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
  "parentUuid": "d8670247-a604-48fe-9f2f-4df0ed58e811",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "d0f7e643-0bf3-4aa8-ae68-93b28f5dadaf",
  "sourceToolAssistantUUID": "d8670247-a604-48fe-9f2f-4df0ed58e811",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-18T13:56:43.757Z_

Now I have a thorough understanding of the project. Looking at the task description again, the paper summary describes a **negative result** paper (AUROC 0.801, DC-GRPO vs R3-only p=0.187, direction drift to cosine 0.66, R1-R3 disagreement 3.4%). This doesn't match any of the three dream variants I've read. The task is asking me to review this specific paper as described in the summary. Let me now also check the "worst" dream report to see if it matches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0f7e643-0bf3-4aa8-ae68-93b28f5dadaf",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9fkQD2exf7E1N5e3KN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0626e21f-a2a6-4d1a-960f-d75196dfaed3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qen5JixzkNCnHouSs28kC1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13478,
      "cache_read_input_tokens": 67150,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13478,
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

_source line 32 · 2026-05-18T13:56:45.903Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Fu7sxBy3eSKHrKdRf8g6K3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/worst/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0626e21f-a2a6-4d1a-960f-d75196dfaed3",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9fkQD2exf7E1N5e3KN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a0725a1b-90a9-4a34-a2b7-0a2760c89dec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qen5JixzkNCnHouSs28kC1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13478,
      "cache_read_input_tokens": 67150,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13478
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 67150,
          "cache_creation_input_tokens": 13478,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13478,
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

_source line 33 · 2026-05-18T13:56:46.390Z_

<details><summary>↩ Tool result · `toolu_01Fu7sxBy3eSKHrKdRf8g6K3`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{hyperref}
8	\usepackage{multirow}
9	\usepackage[margin=2.5cm]{geometry}
10	\usepackage{xcolor}
11	\usepackage{natbib}
12	
13	\title{Representation-Level Rewards Are Not Enough:\\Why Internal Sycophancy Detection Fails to Transfer to Training}
14	
15	\author{Anonymous}
16	\date{}
17	
18	\begin{document}
19	\maketitle
20	
21	% ============================================================
22	\begin{abstract}
23	Large Language Models (LLMs) exhibit sycophantic behavior in multi-turn dialogue, capitulating to user pressure even when their initial answer was correct. Recent work has shown that linear directions in activation space can distinguish sycophantic capitulation from genuine belief revision, raising a natural question: can these directions serve as reward signals during training to reduce sycophancy? We present a systematic investigation of this approach using Direction-Contrastive Group Relative Policy Optimization (DC-GRPO), which incorporates activation-space projections as a reward component alongside behavioral signals. Through controlled experiments on Qwen3-8B, we identify three fundamental limitations: (1) sycophancy directions encode substantial evidence-strength confounds, with discriminability (AUROC) dropping from 0.811 to 0.698 as evidence quality increases; (2) directions destabilize during training, with cosine similarity to the initial direction falling to 0.53 despite periodic recalibration; (3) DC-GRPO provides no statistically significant improvement over a behavioral-reward-only baseline on any sycophancy metric ($p > 0.35$ on all pairwise comparisons), while incurring greater capability degradation ($-2.3$ percentage points on MMLU vs. $-1.2$ for the behavioral baseline). A three-way decomposition analysis reveals that sycophantic and genuine revision directions are near-antiparallel (cosine $= -0.82$), suggesting that linear methods fundamentally cannot separate these constructs in activation space. These findings establish empirical boundary conditions for representation-level reward approaches to alignment training.
24	\end{abstract}
25	
26	% ============================================================
27	\section{Introduction}
28	
29	Sycophancy in LLMs presents a concrete safety problem: models trained with reinforcement learning from human feedback learn to agree with users rather than maintain accurate responses under social pressure~\citep{perez2023discovering,sharma2024towards}. The problem intensifies in multi-turn dialogue, where commitment escalation can degrade factual accuracy by up to 47\% across turns~\citep{truthdecay2024}. Training methods that target sycophancy face a double-bind: reducing unwarranted capitulation (agreeing despite being correct) often also reduces warranted revision (updating beliefs when presented with valid evidence)~\citep{smart2024,bct2024}.
30	
31	A promising line of recent work suggests that the internal representations of LLMs already encode whether a response reflects genuine reasoning or sycophantic agreement. Linear probes applied to model activations can distinguish these cases with moderate accuracy~\citep{sycnotone2024}, and activation consistency training (ACT) penalizes changes in internal states to enforce robustness~\citep{act2024}. The CRAFT framework demonstrates that hidden-state projections can serve as reward signals for safety training via Group Relative Policy Optimization (GRPO)~\citep{craft2024}. These findings motivate a natural hypothesis: if sycophancy is detectable in activation space, that detection signal should transfer to a training reward that specifically targets sycophancy while preserving genuine revision.
32	
33	We test this hypothesis directly. We design Direction-Contrastive GRPO (DC-GRPO), a training framework that combines three reward components: $R_1$ (projection onto a sycophancy direction in activation space), $R_2$ (rank-based contrastive reward), and $R_3$ (NLI-based behavioral reward). We train Qwen3-8B with LoRA on multi-turn sycophancy scenarios and compare against baselines including behavioral-reward-only GRPO, ACT-style consistency training, and binary probe penalties.
34	
35	The results are negative. DC-GRPO fails to outperform any baseline. Rather than dismissing this outcome, we investigate the mechanistic reasons for failure and identify three structural limitations of representation-level rewards for sycophancy training:
36	
37	\begin{itemize}
38	    \item \textbf{Confounded discriminability.} The sycophancy direction $d_{\mathrm{syc}}$ conflates evidence-strength cues with sycophantic cognition. AUROC drops from 0.811 (weak evidence only) to 0.698 (strong evidence), and cross-model direction cosine similarity is only 0.23, indicating model-specific rather than universal encoding.
39	    \item \textbf{Direction instability under training.} LoRA parameter updates cause the sycophancy direction to drift, with cosine similarity to the initial direction falling from 0.91 to 0.53 over 6000 steps. Periodic recalibration recovers only 0.08 cosine on average per event.
40	    \item \textbf{No incremental value over behavioral rewards.} DC-GRPO achieves NoF 0.318 vs. 0.302 for R3-only ($p = 0.35$), while incurring higher MMLU degradation ($-2.3$ vs. $-1.2$ percentage points). A simple binary probe baseline matches DC-GRPO without directional decomposition.
41	\end{itemize}
42	
43	These findings contribute empirical boundary conditions for when representation-level rewards can and cannot aid alignment training. The analysis is relevant to all methods that use internal model states as training signals, including linear probe penalties and activation consistency approaches.
44	
45	% ============================================================
46	\section{Related Work}
47	
48	\paragraph{Sycophancy in LLMs.}
49	Sycophancy has been documented as a systematic failure mode of RLHF-trained models~\citep{perez2023discovering,sharma2024towards}. Models shift their answers toward user-stated preferences even when the original answer was correct, with the effect compounding across dialogue turns~\citep{truthdecay2024}. Benchmarks such as SYCON Bench and SycophancyEval provide standardized measurements~\citep{syconbench2024,syceval2024}.
50	
51	\paragraph{Training-based mitigation.}
52	Several approaches address sycophancy through modified training objectives. Behavioral decomposition methods like ``Pressure, What Pressure?'' use NLI-based scoring to reward responses consistent with evidence rather than user opinion~\citep{pressurewhatpressure2024}. SMART and BCT/ACT enforce consistency between clean and biased prompts through activation-level or behavioral losses~\citep{smart2024,bct2024}. These methods reduce capitulation but do not distinguish sycophantic agreement from warranted belief revision, creating the double-bind problem.
53	
54	\paragraph{Representation-level approaches.}
55	``Sycophancy Is Not One Thing'' demonstrates that linear directions in activation space separate sycophantic from genuine responses~\citep{sycnotone2024}. CRAFT extends hidden-state signals to GRPO training for safety alignment~\citep{craft2024}. Linear Probe Penalties train a binary classifier on reward model activations to penalize sycophancy~\citep{linearprobepenalties2024}. Our work differs in using the policy model's own activations (rather than a reward model) and in systematically characterizing why the detection-to-training transfer fails.
56	
57	\paragraph{Activation space analysis.}
58	Linear probing of LLM internal states has been applied to truthfulness~\citep{marks2023geometry}, safety~\citep{craft2024}, and factual knowledge~\citep{knowledgegap2024}. A key methodological concern is whether probes detect the target concept or surface correlates. Our evidence-strength stratification and cross-model transfer analyses directly address this confound question for sycophancy directions.
59	
60	% ============================================================
61	\section{Method}
62	
63	\subsection{Sycophancy Direction Computation}
64	
65	We compute a sycophancy direction $d_{\mathrm{syc}}$ using contrastive activation pairs from multi-turn dialogue. Each pair consists of activations from the same prompt where the model (a) sycophantically capitulates to user pressure or (b) genuinely revises its belief in response to valid evidence. Following standard practice~\citep{sycnotone2024}, we extract hidden states at a target layer $\ell$ and compute $d_{\mathrm{syc}}$ as the mean difference vector:
66	\begin{equation}
67	    d_{\mathrm{syc}}^{(\ell)} = \frac{1}{N}\sum_{i=1}^{N}\left(h_i^{\mathrm{syc},(\ell)} - h_i^{\mathrm{gen},(\ell)}\right)
68	\end{equation}
69	where $h_i^{\mathrm{syc}}$ and $h_i^{\mathrm{gen}}$ are the last-token hidden states for sycophantic and genuine responses to the $i$-th scenario.
70	
71	To control for surface-level confounds, we construct calibration pairs across three evidence strength levels (weak, medium, strong), ensuring that lexical overlap and response length are matched between sycophantic and genuine responses within each pair. We use $N=200$ pairs (80 weak, 60 medium, 60 strong) and select the optimal layer via 5-fold cross-validated AUROC.
72	
73	\subsection{DC-GRPO Training}
74	
75	DC-GRPO augments standard GRPO~\citep{grpo2024} with a composite reward:
76	\begin{equation}
77	    R = w_1 R_1 + w_2 R_2 + w_3 R_3
78	\end{equation}
79	where $R_1 = -\langle h^{(\ell)}, d_{\mathrm{syc}}^{(\ell)}\rangle / \|d_{\mathrm{syc}}^{(\ell)}\|$ is the negative projection onto the sycophancy direction (rewarding distance from sycophantic activation patterns), $R_2$ is a rank-based contrastive reward comparing relative positions along $d_{\mathrm{syc}}$ within a batch, and $R_3$ is an NLI-based behavioral reward measuring output consistency with provided evidence.
80	
81	We train Qwen3-8B with LoRA (rank 64) for 6000 steps with final weights $w_1 = 0.3$, $w_2 = 0.2$, $w_3 = 0.5$. To address direction drift, we recalibrate $d_{\mathrm{syc}}$ every 500 steps when the cosine similarity between the current and previous direction falls below 0.7.
82	
83	\subsection{Baselines}
84	
85	\begin{itemize}
86	    \item \textbf{R3-only GRPO}: Identical training setup using only $R_3$ (NLI behavioral reward).
87	    \item \textbf{ACT-style}: Undifferentiated L2 activation consistency loss between clean and biased prompt pairs.
88	    \item \textbf{Binary Probe}: A trained linear classifier on policy activations, with reward $\hat{R} = R_3 - \lambda \cdot S(t)$ where $S(t)$ is the predicted sycophancy probability.
89	    \item \textbf{Vanilla}: Unmodified Qwen3-8B without anti-sycophancy training.
90	\end{itemize}
91	
92	\subsection{Evaluation Metrics}
93	
94	We evaluate on SYCON Bench and SycophancyEval using: \textbf{NoF} (frequency of unwarranted opinion flips, lower is better), \textbf{ToF} (turn of first flip), \textbf{Warranted Revision Rate} (WR, fraction of correct revisions when evidence is valid, higher is better), \textbf{Unwarranted Capitulation Rate} (UC, lower is better), and \textbf{Revision-Capitulation AUC} (RC-AUC, area under the WR-UC trade-off curve, higher is better). General capability is measured with MMLU (5-shot) and MT-Bench.
95	
96	% ============================================================
97	\section{Experiments and Results}
98	
99	\subsection{Direction Discriminability Analysis}
100	\label{sec:direction}
101	
102	\paragraph{Evidence-strength confound.}
103	Table~\ref{tab:auroc_layer} reports the AUROC of $d_{\mathrm{syc}}$ stratified by evidence strength and layer. The overall 5-fold CV AUROC on expanded data is 0.753 (95\% CI: [0.694, 0.812]). A clear gradient emerges: AUROC is 0.811 for weak evidence, 0.724 for medium, and 0.698 for strong. This pattern indicates that $d_{\mathrm{syc}}$ partially encodes ``hesitation in the face of weak evidence'' rather than sycophantic cognition per se.
104	
105	\begin{table}[h]
106	\centering
107	\caption{AUROC by evidence strength and layer for $d_{\mathrm{syc}}$ on expanded calibration data ($N = 200$ pairs).}
108	\label{tab:auroc_layer}
109	\small
110	\begin{tabular}{lcccc}
111	\toprule
112	Layer & Weak & Medium & Strong & Overall \\
113	\midrule
114	L0  & 0.512 & 0.503 & 0.498 & 0.505 \\
115	L8  & 0.614 & 0.573 & 0.551 & 0.582 \\
116	L16 & 0.741 & 0.662 & 0.638 & 0.681 \\
117	L19 & 0.793 & 0.718 & 0.691 & 0.742 \\
118	L24 & 0.811 & 0.724 & 0.698 & 0.753 \\
119	L27 & 0.806 & 0.719 & 0.694 & 0.748 \\
120	\bottomrule
121	\end{tabular}
122	\end{table}
123	
124	Table~\ref{tab:bootstrap} compares the expanded dataset to the original MVP (50 weak-only pairs). The MVP AUROC of 0.826 is inflated by approximately 7 percentage points due to the weak-evidence-only distribution, as confirmed by the expanded weak-only subset AUROC of 0.811.
125	
126	\begin{table}[h]
127	\centering
128	\caption{Bootstrap confidence interval comparison between MVP and expanded calibration datasets.}
129	\label{tab:bootstrap}
130	\small
131	\begin{tabular}{lccccc}
132	\toprule
133	Dataset & $N$ & AUROC & CI Lower & CI Upper & CI Width \\
134	\midrule
135	MVP (weak only) & 50 & 0.826 & 0.772 & 0.880 & 0.108 \\
136	Expanded (all) & 200 & 0.753 & 0.694 & 0.812 & 0.068 \\
137	Expanded (weak) & 80 & 0.811 & 0.753 & 0.869 & 0.076 \\
138	Expanded (medium) & 60 & 0.724 & 0.648 & 0.800 & 0.092 \\
139	Expanded (strong) & 60 & 0.698 & 0.618 & 0.778 & 0.100 \\
140	\bottomrule
141	\end{tabular}
142	\end{table}
143	
144	\paragraph{Cross-model transfer.}
145	Table~\ref{tab:crossmodel} reports direction analysis on Llama-3-8B. The model-specific direction achieves a lower AUROC (0.712 overall, 0.774 weak-only) than Qwen3-8B. Critically, directions do not transfer: applying the Qwen3-8B direction to Llama-3-8B yields AUROC 0.571 (near random), and the cross-model direction cosine is only 0.23. This indicates that sycophancy directions are model-specific artifacts rather than universal encodings of sycophantic cognition.
146	
147	\begin{table}[h]
148	\centering
149	\caption{Cross-model direction analysis between Qwen3-8B and Llama-3-8B.}
150	\label{tab:crossmodel}
151	\small
152	\begin{tabular}{lcc}
153	\toprule
154	Metric & Qwen3-8B & Llama-3-8B \\
155	\midrule
156	AUROC (own direction, expanded) & 0.753 & 0.712 \\
157	AUROC (own direction, weak only) & 0.811 & 0.774 \\
158	Optimal layer & L24 & L18 \\
159	AUROC (Qwen dir.\ on Llama) & -- & 0.571 \\
160	AUROC (Llama dir.\ on Qwen) & 0.563 & -- \\
161	Cross-model cosine & \multicolumn{2}{c}{0.23} \\
162	\bottomrule
163	\end{tabular}
164	\end{table}
165	
166	\paragraph{Three-way decomposition.}
167	We introduce a neutral condition (neither sycophantic nor genuine revision) to compute an independent genuine-revision direction $d_{\mathrm{gen}}$ (60 neutral pairs). Table~\ref{tab:threeway} reports the results. The cosine between $d_{\mathrm{gen}}$ and $d_{\mathrm{syc}}$ is $-0.82$, meaning they are near-antiparallel. This implies that sycophancy and genuine revision are not linearly separable independent dimensions; they occupy approximately opposite ends of a single axis. The independent $d_{\mathrm{gen}}$ achieves only 0.691 AUROC for genuine-vs-neutral classification, and the three-way $R_2$ reward provides only 0.008 improvement over the rank-based design.
168	
169	\begin{table}[h]
170	\centering
171	\caption{Three-way direction analysis with independent neutral condition.}
172	\label{tab:threeway}
173	\small
174	\begin{tabular}{lc}
175	\toprule
176	Metric & Value \\
177	\midrule
178	$d_{\mathrm{gen}}$ vs.\ $d_{\mathrm{syc}}$ cosine & $-0.82$ \\
179	$d_{\mathrm{gen}}$ AUROC (genuine vs.\ neutral) & 0.691 \\
180	$d_{\mathrm{syc}}$ AUROC (sycophantic vs.\ neutral) & 0.723 \\
181	$d_{\mathrm{syc}}$ AUROC (sycophantic vs.\ genuine, original) & 0.753 \\
182	Three-way $R_2$ improvement over rank-based $R_2$ & 0.008 \\
183	\bottomrule
184	\end{tabular}
185	\end{table}
186	
187	\subsection{DC-GRPO Training Dynamics}
188	\label{sec:training}
189	
190	Table~\ref{tab:training_dynamics} reports the trajectory of DC-GRPO training. The key observation is the progressive degradation of $R_1$: its mean reward drops from 0.55 (step 500) to 0.31 (step 6000), and its correlation with $R_3$ falls from 0.67 to 0.29. By the second half of training, $R_1$ contributes noise rather than signal. The model's final behavior is primarily shaped by $R_3$, with $R_1$ and $R_2$ acting as friction.
191	
192	\begin{table}[h]
193	\centering
194	\caption{DC-GRPO training dynamics. $R_1$-$R_3$ correlation degrades steadily, indicating that the representation-level reward decouples from the behavioral reward during training.}
195	\label{tab:training_dynamics}
196	\small
197	\begin{tabular}{lccccccc}
198	\toprule
199	Step & $R_1$ & $R_2$ & $R_3$ & Total & $R_1$-$R_3$ Corr. & Cos.\ to Init & Held-out AUROC \\
200	\midrule
201	500  & 0.55 & 0.48 & 0.39 & 0.46 & 0.67 & 0.91 & 0.738 \\
202	1000 & 0.52 & 0.46 & 0.43 & 0.46 & 0.64 & 0.84 & 0.721 \\
203	1500 & 0.47 & 0.44 & 0.46 & 0.45 & 0.58 & 0.76 & 0.706 \\
204	2000 & 0.43 & 0.41 & 0.48 & 0.44 & 0.52 & 0.68 & 0.689 \\
205	2500 & 0.40 & 0.39 & 0.49 & 0.43 & 0.47 & 0.71 & 0.694 \\
206	3000 & 0.38 & 0.38 & 0.50 & 0.43 & 0.43 & 0.64 & 0.678 \\
207	4000 & 0.35 & 0.36 & 0.51 & 0.42 & 0.37 & 0.58 & 0.661 \\
208	5000 & 0.33 & 0.35 & 0.51 & 0.41 & 0.33 & 0.62 & 0.653 \\
209	6000 & 0.31 & 0.34 & 0.52 & 0.41 & 0.29 & 0.55 & 0.642 \\
210	\bottomrule
211	\end{tabular}
212	\end{table}
213	
214	For comparison, Table~\ref{tab:r3only_dynamics} shows the R3-only baseline, which exhibits stable, monotonically increasing reward throughout training.
215	
216	\begin{table}[h]
217	\centering
218	\caption{R3-only GRPO training dynamics. Reward increases monotonically without the instability observed in DC-GRPO.}
219	\label{tab:r3only_dynamics}
220	\small
221	\begin{tabular}{lcccc}
222	\toprule
223	Step & $R_3$ & Total Reward & Training Loss & KL Div. \\
224	\midrule
225	1000 & 0.42 & 0.42 & 1.51 & 0.11 \\
226	2000 & 0.47 & 0.47 & 1.46 & 0.18 \\
227	3000 & 0.50 & 0.50 & 1.43 & 0.23 \\
228	4000 & 0.52 & 0.52 & 1.41 & 0.27 \\
229	5000 & 0.53 & 0.53 & 1.39 & 0.29 \\
230	6000 & 0.54 & 0.54 & 1.38 & 0.31 \\
231	\bottomrule
232	\end{tabular}
233	\end{table}
234	
235	\subsection{Direction Stability During Training}
236	\label{sec:stability}
237	
238	Table~\ref{tab:stability} tracks $d_{\mathrm{syc}}$ stability throughout DC-GRPO training. The cosine similarity between the current and initial direction decreases from 0.91 (step 500) to a minimum of 0.53 (step 5500). The cosine dropped below the 0.7 recalibration threshold 7 times, triggering 4 recalibration events (at steps 2000, 3000, 4000, and 5500). Each recalibration recovers an average of 0.08 cosine, producing a sawtooth pattern that nonetheless trends downward. The held-out AUROC degrades in parallel, from 0.753 (initialization) to 0.642 (step 6000), a total loss of 0.111. The drift rate is approximately 0.062 cosine per 1000 steps.
239	
240	\begin{table}[h]
241	\centering
242	\caption{Direction stability timeline during DC-GRPO training. Recalibrations provide temporary recovery but cannot reverse the downward trend.}
243	\label{tab:stability}
244	\small
245	\begin{tabular}{lcccc}
246	\toprule
247	Step & Cos.\ to Init & Cos.\ to Prev & Held-out AUROC & Recalibrated? \\
248	\midrule
249	0    & 1.00 & --    & 0.753 & Init \\
250	500  & 0.91 & 0.91  & 0.738 & No \\
251	1000 & 0.84 & 0.943 & 0.721 & No \\
252	1500 & 0.76 & 0.928 & 0.706 & No \\
253	2000 & 0.68 & 0.911 & 0.689 & Yes \\
254	2500 & 0.71 & 0.936 & 0.694 & No \\
255	3000 & 0.64 & 0.918 & 0.678 & Yes \\
256	3500 & 0.59 & 0.924 & 0.669 & No \\
257	4000 & 0.58 & 0.947 & 0.661 & Yes \\
258	4500 & 0.62 & 0.938 & 0.656 & No \\
259	5000 & 0.56 & 0.921 & 0.653 & No \\
260	5500 & 0.53 & 0.958 & 0.646 & Yes \\
261	6000 & 0.55 & 0.961 & 0.642 & No \\
262	\bottomrule
263	\end{tabular}
264	\end{table}
265	
266	This instability creates a fundamental problem for representation-level rewards: the direction used to compute rewards at step $t$ may not accurately describe the model's activation geometry at step $t$, turning the reward signal into noise. Even if the initial direction were perfectly accurate, training-induced representation drift would erode its validity.
267	
268	\subsection{R1-R3 Disagreement Analysis}
269	\label{sec:disagreement}
270	
271	If representation-level rewards capture information that behavioral rewards miss, we should observe cases where $R_1$ detects sycophancy that $R_3$ approves (masked sycophancy). Table~\ref{tab:disagreement_phase} reports disagreement rates across training phases.
272	
273	\begin{table}[h]
274	\centering
275	\caption{R1-R3 disagreement frequency by training phase. Overall disagreement is 3.8\%, below the 5\% threshold needed to support a claim of meaningful representation-level advantage.}
276	\label{tab:disagreement_phase}
277	\small
278	\begin{tabular}{lccccc}
279	\toprule
280	Phase & $N$ & Disagree & \% & $R_1$-syc/$R_3$-ok & $R_1$-ok/$R_3$-syc \\
281	\midrule
282	Step 0--2000    & 6200  & 285 & 4.6 & 168 & 117 \\
283	Step 2000--4000 & 6100  & 226 & 3.7 & 134 & 92 \\
284	Step 4000--6000 & 6100  & 189 & 3.1 & 110 & 80 \\
285	\midrule
286	Overall         & 18400 & 700 & 3.8 & 412 & 289 \\
287	\bottomrule
288	\end{tabular}
289	\end{table}
290	
291	The overall disagreement rate of 3.8\% falls below a meaningful threshold. Disagreement is highest for weak-evidence scenarios (5.1\%) and lowest for strong evidence (2.8\%), as shown in Table~\ref{tab:disagreement_evidence}, consistent with the evidence-strength confound identified in Section~\ref{sec:direction}.
292	
293	\begin{table}[h]
294	\centering
295	\caption{R1-R3 disagreement by evidence strength.}
296	\label{tab:disagreement_evidence}
297	\small
298	\begin{tabular}{lcccc}
299	\toprule
300	Evidence & $N$ & Disagree \% & $R_1$-syc/$R_3$-ok \% & $R_1$-ok/$R_3$-syc \% \\
301	\midrule
302	Weak   & 7400 & 5.1 & 2.9 & 2.2 \\
303	Medium & 5600 & 3.4 & 2.1 & 1.3 \\
304	Strong & 5400 & 2.8 & 1.6 & 1.2 \\
305	\bottomrule
306	\end{tabular}
307	\end{table}
308	
309	Manual review of 50 sampled $R_1$-sycophantic/$R_3$-correct cases (Table~\ref{tab:disagreement_qual}) reveals that only 16\% represent clear masked sycophancy. The majority are ambiguous (46\%) or $R_1$ false positives (38\%), further undermining the case for representation-level advantage.
310	
311	\begin{table}[h]
312	\centering
313	\caption{Qualitative review of R1-sycophantic/R3-correct disagreement cases ($n = 50$).}
314	\label{tab:disagreement_qual}
315	\small
316	\begin{tabular}{lcc}
317	\toprule
318	Category & Count & \% \\
319	\midrule
320	Clear masked sycophancy & 8 & 16 \\
321	Ambiguous & 23 & 46 \\
322	$R_1$ false positive & 19 & 38 \\
323	\bottomrule
324	\end{tabular}
325	\end{table}
326	
327	\subsection{R1-Only Ablation}
328	\label{sec:r1only}
329	
330	To isolate the effect of the representation-level reward, we train an R1-only variant (no $R_2$ or $R_3$) for 2000 steps from a step-2000 DC-GRPO checkpoint. Table~\ref{tab:r1only} reports the results.
331	
332	\begin{table}[h]
333	\centering
334	\caption{R1-only ablation compared to DC-GRPO, R3-only, and vanilla baselines.}
335	\label{tab:r1only}
336	\small
337	\begin{tabular}{lcccc}
338	\toprule
339	Metric & R1-only & DC-GRPO & R3-only & Vanilla \\
340	\midrule
341	NoF $\downarrow$     & 0.361 & 0.318 & 0.302 & 0.412 \\
342	WR $\uparrow$        & 0.463 & 0.527 & 0.538 & 0.583 \\
343	MMLU                  & 0.584 & 0.598 & 0.609 & 0.621 \\
344	MT-Bench              & 6.51  & 6.84  & 7.02  & 7.18 \\
345	$R_1$ reward          & 0.72  & 0.31  & --    & -- \\
346	\bottomrule
347	\end{tabular}
348	\end{table}
349	
350	The R1-only model achieves a high $R_1$ reward (0.72) but the worst behavioral outcomes: NoF 0.361, warranted revision 0.463, MMLU regression of $-3.7$ percentage points. We identified 34 reward hacking instances where the model generates lengthy hedging prefixes that project away from $d_{\mathrm{syc}}$ in activation space without actually reducing sycophantic behavior. This confirms that $R_1$ reward can be optimized without improving the target behavior, a systematic risk of representation-level rewards that lack behavioral grounding.
351	
352	\subsection{Turn Depth Analysis}
353	\label{sec:turndepth}
354	
355	Table~\ref{tab:nof_depth} and Table~\ref{tab:wr_depth} report sycophancy metrics stratified by conversation turn depth (turn 2, 3, and 4+).
356	
357	\begin{table}[h]
358	\centering
359	\caption{NoF by turn depth. All methods show similar depth gradients; DC-GRPO does not outperform baselines at any depth.}
360	\label{tab:nof_depth}
361	\small
362	\begin{tabular}{lcccc}
363	\toprule
364	Model & Turn 2 & Turn 3 & Turn 4+ & Gradient \\
365	\midrule
366	Vanilla      & 0.318 & 0.428 & 0.531 & 0.213 \\
367	R3-only      & 0.241 & 0.316 & 0.381 & 0.140 \\
368	ACT          & 0.253 & 0.322 & 0.393 & 0.140 \\
369	Binary Probe & 0.247 & 0.319 & 0.388 & 0.141 \\
370	DC-GRPO      & 0.258 & 0.331 & 0.402 & 0.144 \\
371	\bottomrule
372	\end{tabular}
373	\end{table}
374	
375	\begin{table}[h]
376	\centering
377	\caption{Warranted revision rate by turn depth.}
378	\label{tab:wr_depth}
379	\small
380	\begin{tabular}{lccc}
381	\toprule
382	Model & Turn 2 & Turn 3 & Turn 4+ \\
383	\midrule
384	Vanilla      & 0.628 & 0.576 & 0.524 \\
385	R3-only      & 0.592 & 0.531 & 0.472 \\
386	ACT          & 0.553 & 0.491 & 0.432 \\
387	Binary Probe & 0.586 & 0.524 & 0.465 \\
388	DC-GRPO      & 0.581 & 0.518 & 0.461 \\
389	\bottomrule
390	\end{tabular}
391	\end{table}
392	
393	All trained methods reduce the commitment-depth gradient relative to vanilla (from 0.213 to approximately 0.14), but DC-GRPO shows no differential advantage at any depth. The gap between DC-GRPO and R3-only is consistent across turns (1.5 to 2.1 percentage points on NoF), indicating that the directional signal does not capture commitment-depth-specific sycophancy patterns beyond what behavioral rewards detect.
394	
395	\subsection{Full Evaluation}
396	\label{sec:full_eval}
397	
398	Table~\ref{tab:main_results} presents the complete evaluation across all methods and metrics. All trained methods significantly reduce unwarranted capitulation relative to vanilla ($p < 0.001$), but no trained method significantly outperforms any other ($p > 0.34$ for all pairwise comparisons, Table~\ref{tab:significance}).
399	
400	\begin{table}[h]
401	\centering
402	\caption{Full evaluation summary. DC-GRPO ranks last among trained methods on most metrics.}
403	\label{tab:main_results}
404	\small
405	\begin{tabular}{lcccccccc}
406	\toprule
407	Model & NoF $\downarrow$ & ToF $\uparrow$ & WR $\uparrow$ & UC $\downarrow$ & RC-AUC $\uparrow$ & SycEval $\uparrow$ & MMLU & MT-B \\
408	\midrule
409	Vanilla    & .412 & .701 & .583 & .378 & .602 & .548 & .621 & 7.18 \\
410	R3-only    & .302 & .653 & .538 & .268 & .672 & .634 & .609 & 7.02 \\
411	ACT        & .310 & .628 & .498 & .274 & .651 & .608 & .605 & 6.91 \\
412	Bin.\ Probe & .308 & .644 & .531 & .272 & .669 & .627 & .607 & 6.97 \\
413	DC-GRPO    & .318 & .641 & .527 & .282 & .668 & .621 & .598 & 6.84 \\
414	\bottomrule
415	\end{tabular}
416	\end{table}
417	
418	\begin{table}[h]
419	\centering
420	\caption{Pairwise bootstrap significance tests on NoF. No pair of trained methods differs significantly.}
421	\label{tab:significance}
422	\small
423	\begin{tabular}{lccc}
424	\toprule
425	Comparison & NoF Diff & $p$-value & Sig.\ at 0.05? \\
426	\midrule
427	DC-GRPO vs.\ R3-only    & 0.016  & 0.35 & No \\
428	DC-GRPO vs.\ ACT        & 0.008  & 0.62 & No \\
429	DC-GRPO vs.\ Bin.\ Probe & 0.010  & 0.54 & No \\
430	R3-only vs.\ ACT        & $-0.008$ & 0.61 & No \\
431	R3-only vs.\ Bin.\ Probe & $-0.006$ & 0.68 & No \\
432	ACT vs.\ Bin.\ Probe    & 0.002  & 0.91 & No \\
433	Any trained vs.\ Vanilla & $\sim$$-$0.10 & $<$0.001 & Yes \\
434	\bottomrule
435	\end{tabular}
436	\end{table}
437	
438	DC-GRPO achieves the worst NoF (0.318), worst MMLU (0.598), and worst MT-Bench (6.84) among trained methods. The binary probe baseline, which is strictly simpler, matches or exceeds DC-GRPO on every metric. The ACT baseline with its undifferentiated consistency loss is also statistically indistinguishable from DC-GRPO.
439	
440	\paragraph{The double-bind persists.} Table~\ref{tab:doublebind} shows the revision-capitulation trade-off. All methods reduce unwarranted capitulation (from 0.378 to 0.268--0.282) at the cost of warranted revision (from 0.583 to 0.498--0.538). No method resolves this trade-off, and DC-GRPO does not improve it relative to baselines.
441	
442	\begin{table}[h]
443	\centering
444	\caption{Revision-capitulation trade-off. No method resolves the double-bind between reducing sycophancy and preserving genuine revision.}
445	\label{tab:doublebind}
446	\small
447	\begin{tabular}{lcccc}
448	\toprule
449	Model & WR $\uparrow$ & UC $\downarrow$ & RC-AUC $\uparrow$ & Double-bind resolved? \\
450	\midrule
451	Vanilla      & 0.583 & 0.378 & 0.602 & No (high both) \\
452	R3-only      & 0.538 & 0.268 & 0.672 & Partial \\
453	ACT          & 0.498 & 0.274 & 0.651 & No (WR drop $>$ UC drop) \\
454	Bin.\ Probe   & 0.531 & 0.272 & 0.669 & Partial \\
455	DC-GRPO      & 0.527 & 0.282 & 0.668 & No \\
456	\bottomrule
457	\end{tabular}
458	\end{table}
459	
460	\subsection{Binary Probe Comparison}
461	\label{sec:binaryprobe}
462	
463	Table~\ref{tab:probe_head} provides a direct comparison between the binary probe baseline and DC-GRPO. The probe suffers from the same direction-drift phenomenon (AUROC degrades from 0.761 to 0.651 over training), but its impact is more contained because a scalar probability output is more robust to representation shifts than a directional projection. No metric difference is statistically significant.
464	
465	\begin{table}[h]
466	\centering
467	\caption{Binary Probe vs.\ DC-GRPO head-to-head comparison.}
468	\label{tab:probe_head}
469	\small
470	\begin{tabular}{lcccc}
471	\toprule
472	Metric & Bin.\ Probe & DC-GRPO & Diff & $p$ \\
473	\midrule
474	NoF               & 0.308 & 0.318 & 0.010  & 0.54 \\
475	WR                & 0.531 & 0.527 & $-0.004$ & 0.82 \\
476	RC-AUC            & 0.669 & 0.668 & $-0.001$ & 0.94 \\
477	MMLU              & 0.607 & 0.598 & $-0.009$ & 0.38 \\
478	Final probe/dir.\ AUROC & 0.651 & 0.642 & $-0.009$ & -- \\
479	\bottomrule
480	\end{tabular}
481	\end{table}
482	
483	This result challenges the necessity of directional decomposition. A simpler binary classifier achieves equivalent performance with fewer moving parts (no contrastive $R_2$, no multi-component reward weighting, no directional recalibration).
484	
485	% ============================================================
486	\section{Discussion}
487	
488	\paragraph{Why does detection fail to transfer?}
489	Our experiments identify a cascade of failures connecting detection to training. First, the direction itself encodes confounding features: the AUROC gradient from 0.811 (weak evidence) to 0.698 (strong evidence) means that 30--40\% of the signal reflects evidence-strength context rather than sycophantic cognition. Second, even the genuine signal component degrades during training: LoRA updates shift the representation space faster than recalibration can track, and direction AUROC drops from 0.753 to 0.642 over 6000 steps. Third, the three-way decomposition reveals that $d_{\mathrm{syc}}$ and $d_{\mathrm{gen}}$ are near-antiparallel (cosine $= -0.82$), meaning that linear probing in this domain captures a contrast axis (``being persuaded'' vs.\ ``not being persuaded'') rather than two independent constructs. Together, these factors make $R_1$ a noisy, drifting signal that contributes friction rather than guidance.
490	
491	\paragraph{Implications for representation-level reward methods.}
492	The direction instability problem generalizes beyond our specific setup. Any method that uses internal model states as reward signals during RL training faces the same challenge: the states that define the reward change as the policy updates. CRAFT~\citep{craft2024} addresses this through prototype clustering with periodic updates, but our results suggest that even frequent recalibration (every 500 steps) is insufficient when the underlying direction is confounded. Linear Probe Penalties~\citep{linearprobepenalties2024} may be more robust by using the reward model's activations rather than the policy's, but this comes at the cost of detecting policy-specific internal states.
493	
494	\paragraph{The double-bind as a shared limitation.}
495	All methods we tested reduce unwarranted capitulation at the cost of warranted revision. The warranted revision rate drops from 0.583 (vanilla) to 0.498--0.538 across trained models. This is not a failure of any particular method but a reflection of the difficulty of the underlying problem: at the 8B parameter scale, the internal distinction between ``I am being persuaded by good evidence'' and ``I am caving to social pressure'' may not be linearly separable in activation space. Future work might investigate non-linear probing methods or larger model scales where the distinction could be more salient.
496	
497	\paragraph{Limitations.}
498	Our experiments use a single primary model (Qwen3-8B) at a single scale (8B parameters). The negative results may not hold at larger scales where sycophancy directions could be more discriminative. The calibration data, while style-controlled, covers a limited range of dialogue scenarios. We also use LoRA rather than full fine-tuning, which constrains the representation space in specific ways.
499	
500	% ============================================================
501	\section{Conclusion}
502	
503	We set out to test whether activation-space sycophancy detection can be leveraged as a reward signal for GRPO training. The answer, at 8B scale with our setup, is no. Direction-Contrastive GRPO provides no measurable benefit over a behavioral-reward-only baseline while incurring greater capability degradation. We trace this failure to three structural causes: evidence-strength confounds in the sycophancy direction, direction instability under training, and the near-antiparallel geometry of sycophantic and genuine revision directions. These findings do not invalidate activation-space analysis of sycophancy as a measurement tool, but they establish that detection accuracy in a static setting does not predict utility as a dynamic training signal. We release our expanded calibration dataset and direction stability monitoring code to support further investigation.
504	
505	% ============================================================
506	\bibliographystyle{plainnat}
507	\begin{thebibliography}{20}
508	
509	\bibitem[Perez et~al.(2023)]{perez2023discovering}
510	Perez, E., Ringer, S., Luko{\v{s}}i{\={u}}t{\.e}, K., et~al.
511	\newblock Discovering language model behaviors with model-written evaluations.
512	\newblock In \emph{Findings of ACL}, 2023.
513	
514	\bibitem[Sharma et~al.(2024)]{sharma2024towards}
515	Sharma, M., Tong, M., Korbak, T., et~al.
516	\newblock Towards understanding sycophancy in language models.
517	\newblock In \emph{ICLR}, 2024.
518	
519	\bibitem[Wei et~al.(2024)]{truthdecay2024}
520	Wei, J., et~al.
521	\newblock Truth decay: Multi-turn sycophancy and accuracy degradation in language models.
522	\newblock \emph{arXiv preprint}, 2024.
523	
524	\bibitem[Sun et~al.(2024)]{smart2024}
525	Sun, Z., et~al.
526	\newblock SMART: Self-supervised multi-turn anti-sycophancy training.
527	\newblock In \emph{EMNLP}, 2024.
528	
529	\bibitem[Mitchell et~al.(2024)]{bct2024}
530	Mitchell, E., et~al.
531	\newblock BCT/ACT: Behavioral and activation consistency training for robust language models.
532	\newblock In \emph{NeurIPS}, 2024.
533	
534	\bibitem[Chen et~al.(2024)]{act2024}
535	Chen, Y., et~al.
536	\newblock Activation consistency training for reducing sycophancy.
537	\newblock \emph{arXiv preprint}, 2024.
538	
539	\bibitem[Li et~al.(2024)]{sycnotone2024}
540	Li, X., et~al.
541	\newblock Sycophancy is not one thing: Decomposing sycophancy in language model activations.
542	\newblock In \emph{ACL}, 2024.
543	
544	\bibitem[Zhang et~al.(2024)]{craft2024}
545	Zhang, H., et~al.
546	\newblock CRAFT: Hidden-state GRPO for safety alignment.
547	\newblock In \emph{ICML}, 2024.
548	
549	\bibitem[Wang et~al.(2024)]{linearprobepenalties2024}
550	Wang, T., et~al.
551	\newblock Linear probe penalties for reducing reward model sycophancy.
552	\newblock In \emph{EMNLP}, 2024.
553	
554	\bibitem[Liu et~al.(2024)]{pressurewhatpressure2024}
555	Liu, Y., et~al.
556	\newblock Pressure, what pressure? Behavioral decomposition for anti-sycophancy GRPO.
557	\newblock \emph{arXiv preprint}, 2024.
558	
559	\bibitem[Shao et~al.(2024)]{grpo2024}
560	Shao, Z., et~al.
561	\newblock DeepSeekMath: Pushing the limits of mathematical reasoning in open language models.
562	\newblock \emph{arXiv preprint}, 2024.
563	
564	\bibitem[Marks and Tegmark(2023)]{marks2023geometry}
565	Marks, S. and Tegmark, M.
566	\newblock The geometry of truth: Emergent linear structure in large language model representations of true/false statements.
567	\newblock \emph{arXiv preprint}, 2023.
568	
569	\bibitem[Chen et~al.(2024b)]{knowledgegap2024}
570	Chen, Y., et~al.
571	\newblock The knowledge-prediction gap in large language models.
572	\newblock In \emph{NAACL}, 2024.
573	
574	\bibitem[Zhou et~al.(2024)]{syconbench2024}
575	Zhou, L., et~al.
576	\newblock SYCON Bench: A benchmark for multi-turn sycophancy evaluation.
577	\newblock \emph{arXiv preprint}, 2024.
578	
579	\bibitem[Park et~al.(2024)]{syceval2024}
580	Park, J., et~al.
581	\newblock SycophancyEval: Comprehensive evaluation of sycophantic behaviors in language models.
582	\newblock In \emph{EACL}, 2024.
583	
584	\end{thebibliography}
585	
586	\end{document}
587	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0725a1b-90a9-4a34-a2b7-0a2760c89dec",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "d34ed2b1-36ce-4bb4-897b-b650634fe9c4",
  "sourceToolAssistantUUID": "a0725a1b-90a9-4a34-a2b7-0a2760c89dec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-18T13:56:56.108Z_

Now I have the full picture. The paper described in the task prompt matches the "worst" dream scenario most closely (negative result, AUROC around 0.75-0.80, DC-GRPO failing to outperform R3-only, direction drift). However, the specific numbers in the task description (AUROC 0.801, p=0.187, cosine drift to 0.66, R1-R3 disagreement 3.4%) seem to be an intermediate scenario between the "median" and "worst" dreams. I should review based on the paper summary as provided in the task.

Now let me also read the existing review report for the first dream round (if different from what I already read) and look at any previous R1 review to understand complementary coverage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d34ed2b1-36ce-4bb4-897b-b650634fe9c4",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9gXkUetxy6CyAkB73T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7dcbc5b-06b3-4ac0-8c9b-8040c52d11fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016i946nw3SC86jkEN9GUmaw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13871,
      "cache_read_input_tokens": 80628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13871,
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

_source line 35 · 2026-05-18T13:56:58.034Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UugmKkUYFcDMvsC8QNnjiJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/worst/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7dcbc5b-06b3-4ac0-8c9b-8040c52d11fc",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9gXkUetxy6CyAkB73T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0638ce1-6381-40b9-853e-f3370a95c56b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016i946nw3SC86jkEN9GUmaw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13871,
      "cache_read_input_tokens": 80628,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13871
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 283,
          "cache_read_input_tokens": 80628,
          "cache_creation_input_tokens": 13871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13871,
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

_source line 36 · 2026-05-18T13:56:58.040Z_

<details><summary>↩ Tool result · `toolu_01UugmKkUYFcDMvsC8QNnjiJ`</summary>

```text
1	---
2	dream_id: dream_20260518T110318
3	tier: worst
4	overall_score: weak reject
5	timestamp: 2026-05-18T11:54:04.067515+00:00
6	---
7	
8	# Dream Review Report: "Representation-Level Rewards Are Not Enough"
9	
10	**dream_id:** 20260518T110318  
11	**Review mode:** full  
12	**Reviewers:** R1 (Methods + Experiments), R2 (Novelty + Related Work)  
13	**Roundtable:** 4-step (Independent → Cross-share → Converge → Synthesize)
14	
15	---
16	
17	## 1. Paper Summary
18	
19	The paper investigates whether activation-space sycophancy directions can serve as reward signals for GRPO training. The proposed method, Direction-Contrastive GRPO (DC-GRPO), combines three reward components: R1 (projection onto d_syc), R2 (rank-based contrastive), and R3 (NLI behavioral). Experiments on Qwen3-8B with LoRA show DC-GRPO fails to outperform an R3-only baseline on any sycophancy metric. The paper reframes as a characterization study, identifying three structural failure modes: evidence-strength confounds in d_syc, direction instability under training, and near-antiparallel geometry of sycophantic vs. genuine revision directions.
20	
21	---
22	
23	## 2. Reviewer R1: Methods + Experiments (Score: 4/6 Weak Accept)
24	
25	### Strengths
26	- **Evidence-strength stratification is methodologically sound.** The AUROC gradient (weak 0.811 → medium 0.724 → strong 0.698) across 200 pairs with 5-fold CV cleanly demonstrates that d_syc conflates evidence-strength context with sycophantic cognition. This is the paper's strongest empirical contribution.
27	- **Direction stability analysis is thorough.** Tracking cosine similarity, held-out AUROC, and recalibration events over 6000 steps (Table 7) provides a detailed mechanistic picture. The sawtooth decay pattern with drift rate ~0.062/1k steps is quantitatively informative.
28	- **R1-only ablation is a valuable cautionary finding.** High R1 reward (0.72) paired with the worst behavioral outcomes (NoF 0.361, MMLU -3.7pp) and 34 documented reward hacking instances is a clean demonstration of Goodhart's Law for representation-level rewards.
29	- **Statistical honesty.** All pairwise bootstrap p-values reported without cherry-picking. The paper does not hide that DC-GRPO performs worst among trained methods (Table 14).
30	- **Comprehensive baseline coverage.** R3-only, ACT-style, Binary Probe, and Vanilla span the relevant design space. The Binary Probe comparison (Table 17) directly challenges the necessity of directional decomposition.
31	- **Three-way decomposition (cosine = -0.82)** provides structural geometric insight about the fundamental linear-separability limitation.
32	
33	### Weaknesses
34	- **Single model, single config.** All experiments use Qwen3-8B with LoRA rank 64. The paper claims "fundamental limitations" and "empirical boundary conditions" but n=1 model cannot establish fundamentality. The Llama-3-8B cross-model test (Table 3) only tests direction transfer, not whether DC-GRPO itself would also fail on Llama.
35	- **Recalibration strategy underexplored.** Only one recalibration approach tested (cosine < 0.7, every 500 steps). Online direction estimation, EMA updates, or more frequent recalibration are not tried. Direction instability may be an engineering problem with better solutions rather than an inherent limitation.
36	- **R1-R3 disagreement analysis has circularity.** Low disagreement (3.8%) in later training phases could reflect R1's degraded accuracy (held-out AUROC dropping to 0.642) rather than genuine absence of masked sycophancy. The analysis conflates signal degradation with signal absence.
37	- **Manual review sample is underpowered.** n=50 with only 8 clear positives (Table 10) yields very wide confidence intervals on the 16% precision estimate. This is too thin to draw firm conclusions about masked sycophancy detection.
38	- **Missing sensitivity analyses.** No exploration of reward weight schedules (e.g., decaying w1 as direction degrades), learning rate effects, LoRA rank interaction, or whether full fine-tuning changes the direction stability picture.
39	- **Three-way decomposition underpowered.** Only 60 neutral pairs for a finding (cosine = -0.82) presented as one of the paper's most important insights. No bootstrap CI reported for this cosine estimate.
40	- **No figures in the paper.** Despite describing many informative visualizations in the experiment design (AUROC vs layer curves, bootstrap distributions, PCA direction drift, reward hacking scatter plots), the paper relies entirely on tables. Figures would substantially improve readability and impact.
41	
42	### Questions for Authors
43	1. Have you tried decaying w1 toward zero as R1-R3 correlation drops, effectively letting the system self-detect when R1 becomes noise?
44	2. What happens with higher recalibration frequency (every 100 steps) or online EMA direction updates?
45	3. Could you provide bootstrap CIs for the three-way decomposition cosine = -0.82?
46	4. Would full fine-tuning (instead of LoRA) change the direction stability dynamics?
47	
48	---
49	
50	## 3. Reviewer R2: Novelty + Related Work (Score: 3/6 Weak Reject)
51	
52	### Strengths
53	- **Intellectual honesty is exceptional.** Pre-registered thresholds (5% disagreement), transparent reporting of DC-GRPO ranking last, and honest limitations section. This sets a good standard for negative-result papers.
54	- **Evidence-strength confound has broader implications.** The finding that d_syc partially encodes "hesitation in the face of weak evidence" rather than pure sycophantic cognition is relevant to the entire activation-space probing literature, not just sycophancy.
55	- **Direction stability findings are generalizable.** The representation drift problem applies to any method using internal model states as online training rewards (CRAFT, Linear Probe Penalties, etc.).
56	- **Title and framing are accurate.** The paper delivers exactly what it promises: a systematic investigation of why detection-to-training transfer fails.
57	
58	### Weaknesses
59	- **Over-generalized negative claim from narrow scope.** The title "Representation-Level Rewards Are Not Enough" and abstract language ("establish empirical boundary conditions") frame findings as general statements, but evidence comes from one model (Qwen3-8B), one scale (8B), one training method (LoRA rank 64), and one direction computation method (mean difference vector). The paper's own Limitations section acknowledges "larger scales where sycophancy directions could be more discriminative" but this caveat is insufficient given the sweeping title.
60	- **Missing foundational references (~15+).** The Related Work section cites only ~14 works, which is thin for a paper claiming to establish boundary conditions for a field. Notable omissions:
61	  - Representation Engineering (Zou et al., 2023) — the foundational framework for reading/writing model representations
62	  - Contrast-Consistent Search / CCS (Burns et al., 2023) — unsupervised direction finding, directly relevant to d_syc methodology
63	  - Activation Addition / steering vectors (Turner et al., 2023) — using directions for inference-time intervention
64	  - Steering vector non-identifiability concerns (recent critiques of linear probing)
65	  - RLHF foundations (Ouyang et al., 2022; Christiano et al., 2017) — needed for contextualizing reward design
66	  - DPO and its representation-level variants
67	  - Concurrent work on mechanistic interpretability of sycophancy
68	- **Limited novelty of individual findings.** The three failure modes form a predictable causal chain rather than three independent discoveries: confounded direction (cause) → noisy reward signal → drift compounds noise → null result. A reviewer familiar with representation engineering would predict most of these failure modes a priori. The paper's value is in the systematic empirical documentation, but the conceptual surprise factor is low.
69	- **Insufficient exploration of mitigations.** For a paper claiming to establish "boundary conditions," it should probe those boundaries more thoroughly. What if the direction were computed with CCS instead of mean-difference? What if a non-linear probe replaced the linear direction? What if the reward weight adapted based on held-out AUROC? Without testing these alternatives, "boundary conditions" becomes "conditions under which one specific implementation fails."
70	- **Contribution framing tension.** The paper oscillates between "DC-GRPO as a method that failed" (method paper) and "systematic characterization of why representation-level rewards fail" (analysis paper). The analysis angle is stronger, but the paper still spends significant space on DC-GRPO's formulation (Section 3.2) that adds little insight once results are negative.
71	
72	### Questions for Authors
73	1. Have you considered CCS or other unsupervised direction-finding methods as alternatives to mean-difference d_syc?
74	2. Would a non-linear probe (MLP) for computing rewards address the linear-separability limitation revealed by the three-way analysis?
75	3. How do you respond to the concern that your findings may be specific to 8B-scale models and LoRA training?
76	4. Can you justify the claim "empirical boundary conditions" when only one point in the method-space has been tested?
77	
78	---
79	
80	## 4. Roundtable Convergence
81	
82	### Points of Agreement (Both Reviewers)
83	1. **Evidence-strength confound analysis is the most valuable contribution.** Both reviewers identify this as a genuine insight with implications beyond this specific paper.
84	2. **Single-model scope is the most serious limitation.** The gap between the paper's broad claims and its narrow experimental base is the central tension.
85	3. **Direction stability analysis is well-executed** but the claim that instability is "fundamental" is undermined by testing only one recalibration strategy.
86	4. **Three-way decomposition is interesting but needs more validation** — underpowered (60 pairs), no CI reported, not replicated on a second model.
87	5. **Intellectual honesty is a strength** — the paper does not hide negative results and reports all p-values.
88	6. **Related work is thin** for a paper claiming to establish boundary conditions for a field.
89	
90	### Points of Disagreement
91	- **R1 (4/6)** weighs the methodological quality of the diagnostic analyses more heavily, arguing the evidence-strength confound, stability tracking, and reward hacking ablation are individually solid contributions that meet the bar for a characterization paper.
92	- **R2 (3/6)** weighs the limited novelty and over-generalization more heavily, arguing that the findings are largely predictable and the narrow scope cannot support the broad claims in the title/abstract.
93	
94	### Convergence Score Discussion
95	The reviewers converge on the assessment that this is a borderline paper. The diagnostic analyses are genuinely informative but the scope-to-claim ratio is poor. The paper would benefit substantially from: (a) more modest framing, (b) 2-3 additional mitigation attempts to probe boundaries more rigorously, (c) expanded references, and (d) replication of key findings on a second model.
96	
97	---
98	
99	## 5. Consolidated Assessment
100	
101	### Overall Score: 3/6 (Weak Reject)
102	
103	### Justification
104	
105	**What the paper does well:**
106	- Asks an important question (detection-to-training transfer) that the community needs answered
107	- Provides honest, well-documented negative results with appropriate statistical testing
108	- The evidence-strength confound finding (AUROC gradient by evidence quality) is a genuine contribution to the probing literature
109	- Direction stability tracking and R1-only reward hacking ablation are clean, informative experiments
110	
111	**What prevents acceptance:**
112	1. **Scope-claim mismatch (most critical).** The title, abstract, and conclusion make general claims about "representation-level rewards" but all evidence comes from one model at one scale with one training configuration. The paper needs either broader experiments or narrower claims.
113	2. **Predictable failure chain.** For researchers familiar with representation engineering, the three failure modes (confounded direction + training drift → noisy reward → null result) are largely expected rather than surprising. The systematic documentation has value, but the conceptual contribution is incremental.
114	3. **Incomplete boundary probing.** A paper claiming to establish "boundary conditions" should test multiple points along those boundaries. No alternative direction methods (CCS, non-linear), no adaptive reward weighting, no exploration of whether more frequent recalibration or online estimation resolves drift.
115	4. **Thin related work.** ~14 references is insufficient. Key works on Representation Engineering, CCS, Activation Addition, and steering vector methodology are absent.
116	5. **Missing figures.** The paper describes many informative visualizations but includes none, relying entirely on dense tables. This is a significant presentation weakness.
117	
118	### Path to Acceptance
119	1. **Narrow the claims** to match scope: "at 8B scale with linear directions and LoRA training" rather than general statements about representation-level rewards
120	2. **Test 2-3 mitigations**: adaptive w1 decay, online direction estimation, non-linear probe — to demonstrate that the boundaries are real, not just artifacts of one implementation
121	3. **Expand references** to 30+ with proper coverage of Representation Engineering, CCS, Activation Addition, and RLHF foundations
122	4. **Replicate three-way decomposition** on Llama-3-8B (data already collected for cross-model transfer)
123	5. **Add key figures**: AUROC-by-layer curves, direction drift visualization, reward hacking scatter plot
124	
125	### Experiment Coverage Assessment
126	Relative to the planned 13 experiments: 12/13 covered (exp-011 conditionally skipped, which is reasonable). The paper presents a comprehensive experimental program. The issue is not missing experiments but missing exploration of alternative approaches and limited model diversity.
127	
128	### Confidence: 4/5
129	High confidence in assessment. Both reviewers have domain expertise in representation-level methods and RL training. The main uncertainty is whether larger-scale experiments would yield different conclusions (as the paper's own Limitations acknowledge).
130	
131	---
132	
133	## 6. Actionable Recommendations (Priority-Ordered)
134	
135	| Priority | Recommendation | Effort | Impact |
136	|----------|---------------|--------|--------|
137	| 1 | Narrow title/abstract claims to match actual scope | Low | High |
138	| 2 | Test adaptive w1 decay (reduce w1 when R1-R3 corr drops) | Medium | High |
139	| 3 | Expand Related Work with ~15 missing references | Low | Medium |
140	| 4 | Add 4-5 key figures from described visualizations | Medium | Medium |
141	| 5 | Replicate three-way decomposition on Llama-3-8B | Medium | Medium |
142	| 6 | Test CCS or non-linear probe as alternative to mean-diff d_syc | High | High |
143	| 7 | Report bootstrap CI for three-way cosine estimate | Low | Low |
144	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0638ce1-6381-40b9-853e-f3370a95c56b",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "b02d3435-d717-45c2-bb51-dd19d9f87c0a",
  "sourceToolAssistantUUID": "b0638ce1-6381-40b9-853e-f3370a95c56b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-18T13:57:04.275Z_

Now I have comprehensive context from all dream variants. Let me produce the R2 review for the paper as described in the task prompt. The paper described in the task is the "negative result" version with these specific numbers: AUROC 0.801, DC-GRPO vs R3-only p=0.187, continuous probe matches DC-GRPO (p=0.448), direction drift to cosine 0.66, R1-R3 disagreement 3.4%.

Now let me submit my review via the appropriate tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b02d3435-d717-45c2-bb51-dd19d9f87c0a",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9hPmY3AqWNeHbm7Lh2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ed1de2e-f6b6-44ea-85f3-4dbf2567fa4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFwbtyLHXDwEPVZkGYh9fx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4176,
      "cache_read_input_tokens": 94499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4176,
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

_source line 38 · 2026-05-18T13:57:04.888Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TaKnhKfmEHgBFmDEpg1t9e`</summary>

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
  "parentUuid": "3ed1de2e-f6b6-44ea-85f3-4dbf2567fa4f",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9hPmY3AqWNeHbm7Lh2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a8af786-b537-4077-9434-c7f0367144e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YFwbtyLHXDwEPVZkGYh9fx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4176,
      "cache_read_input_tokens": 94499,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4176
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 210,
          "cache_read_input_tokens": 94499,
          "cache_creation_input_tokens": 4176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4176,
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

_source line 39 · 2026-05-18T13:57:04.894Z_

<details><summary>↩ Tool result · `toolu_01TaKnhKfmEHgBFmDEpg1t9e`</summary>

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
  "parentUuid": "0a8af786-b537-4077-9434-c7f0367144e7",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "4afb0c76-d90f-416a-bffa-b65d15a664ff",
  "sourceToolAssistantUUID": "0a8af786-b537-4077-9434-c7f0367144e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-18T13:57:08.892Z_



Now I will compose my thorough R2 review based on the paper summary provided in the task. The paper described is the "boundary conditions" / negative-result version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4afb0c76-d90f-416a-bffa-b65d15a664ff",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9htxiBUdd6emHyHN1Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5c0e129-f55e-4047-93fc-25ef75bfad81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015MVe6K4jxaiCGAVkLEwciX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 788,
      "cache_read_input_tokens": 98675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 788,
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

_source line 41 · 2026-05-18T13:59:50.374Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01DUjt51i56qHzZcr8seEHNj`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "tier": "worst",
  "dream_id": "dream_20260518T125925",
  "overall_score": "3/6 Weak Reject",
  "report": "---\ndream_id: dream_20260518T125925\ntier: worst\noverall_score: 3/6 Weak Reject\ntimestamp: 2026-05-18T14:30:00Z\nreviewer: R2 (Novelty, Significance, Positioning, Related Work)\n---\n\n# Review Report -- R2 (Novelty + Significance + Related Work)\n\n**Paper**: \"Do Sycophancy Directions Transfer to Training Rewards? Boundary Conditions of Representation-Level Signals for Multi-Turn Belief Revision\"\n\n**Venue calibration**: Top ML venue, ~25% acceptance rate, 6-point scale.\n\n---\n\n## 1. Novelty Assessment\n\n### 1.1 Is the negative result itself a contribution?\n\nNegative results are publishable at top venues when they (a) test a hypothesis the community genuinely believes is plausible, (b) the experimental design is rigorous enough to be conclusive, and (c) the analysis provides mechanistic understanding that redirects future work.\n\nThis paper partially satisfies (a): the hypothesis that RepE-style directions could serve as training rewards is a natural extension of CRAFT (which validated hidden-state GRPO rewards for safety) and \"Sycophancy Is Not One Thing\" (which demonstrated high-AUROC linear separability). However, the hypothesis is less \"widely believed\" than the paper implies. Researchers familiar with the steering vector non-identifiability literature (Venkatesh & Kurapath, 2026; Tan et al., 2024) and the modest results from The Hypocrisy Gap (AUROC 0.55-0.73 with SAE probes) would already have strong priors that detection-to-training transfer is non-trivial. The paper is answering a question that many in the field would have predicted the answer to.\n\nThe paper partially satisfies (b): the experimental design covers multiple baselines and includes relevant ablations, but 3 random seeds provide critically low statistical power (2 degrees of freedom for paired t-tests). The key null result (DC-GRPO vs R3-only, p=0.187) could flip with additional seeds. This is not conclusive enough to establish a firm negative.\n\nThe paper partially satisfies (c): the three identified failure modes (low SNR at AUROC 0.801, direction drift to cosine 0.66, R1-R3 correlation making R1 redundant) provide useful diagnostic information, but the analysis does not sufficiently probe whether these are fundamental limitations or artifacts of the specific implementation.\n\n**Verdict**: The negative result is a moderate contribution. It is informative but not definitive. The \"boundary conditions\" framing is more valuable than the null training result itself.\n\n### 1.2 Does the \"boundary conditions\" framing add sufficient value?\n\nThe framing is appropriate and honest, which I appreciate. However, \"boundary conditions\" implies the paper maps out the parameter space where representation-level rewards succeed and fail. In practice, the paper tests a single point in the method space (linear direction via PCA, mean-difference extraction, LoRA rank 64, Qwen3-8B, 200 calibration pairs) and finds failure. This is a single negative data point, not a boundary map.\n\nTo genuinely establish boundary conditions, the paper would need to test:\n- Alternative direction extraction methods (CCS, non-linear probes, PCA vs mean-difference)\n- Different discriminability levels (what AUROC threshold makes RepE-as-reward viable?)\n- Different training regimes (full fine-tuning vs LoRA, different ranks)\n- Adaptive reward weighting (decay w1 as direction degrades)\n- Different model scales\n\nWithout these, \"boundary conditions\" overpromises relative to what is delivered.\n\n### 1.3 Component-level novelty\n\nEach technical component is from prior work:\n- Direction extraction via contrastive PCA: standard RepE methodology (Zou et al., 2023)\n- Projection as GRPO reward: CRAFT (2026) demonstrated this for safety\n- NLI behavioral reward: \"Pressure, What Pressure?\" (2026)\n- Rank-based contrastive reward within GRPO groups: standard ranking reward design\n- Periodic recalibration: analogous to target network updates in DQN\n\nThe combination is reasonable but not novel. The multi-turn extension (computing directions from multi-turn contrastive pairs) is a necessary adaptation rather than a methodological innovation. The paper correctly acknowledges that the direction extraction is a RepE application, which is appropriate positioning.\n\n**Overall novelty**: Low-to-moderate. The negative result is informative, the diagnostic analysis adds value, but the conceptual advance is incremental.\n\n---\n\n## 2. Significance\n\n### 2.1 Would the ML community benefit from this paper?\n\n**Moderately.** Three audiences would find value:\n\n1. **Researchers building on RepE/CRAFT for alignment training**: The direction drift finding (cosine decaying to 0.66 over training) is a practical warning. The low R1-R3 disagreement (3.4%) challenges the premise that representation-level rewards detect a substantial class of errors invisible to behavioral signals.\n\n2. **Researchers studying sycophancy mitigation**: The finding that R3-only behavioral reward is competitive with more complex approaches is practically useful, suggesting that engineering effort should focus on better behavioral decomposition rather than representation-level complexity.\n\n3. **The broader interpretability-for-training community**: The gap between static detection accuracy (AUROC 0.801) and dynamic training utility is a cautionary tale about assuming that interpretability probes transfer to training objectives.\n\n### 2.2 Does it change how people think about RepE-as-reward?\n\nPartially. The paper's most significant conceptual contribution is articulating why \"direction is real but redundant\" -- that even when a direction genuinely captures a concept, its training value depends on (a) sufficient discriminability above what behavioral signals provide, (b) direction stability during policy gradient updates, and (c) sufficient R1-R3 disagreement to justify the additional signal. The threshold analysis (suggesting AUROC needs to be substantially above 0.80 for practical value) is useful guidance.\n\nHowever, this conclusion is drawn from a single setting. CRAFT demonstrates that hidden-state rewards DO work for safety alignment. The paper does not adequately explain why the same paradigm succeeds for safety (CRAFT) but fails for sycophancy (DC-GRPO). Is it because safety directions have higher AUROC? Because safety directions are more stable under training? Because safety-behavioral disagreement is higher? Without this comparative analysis, the paper's significance is limited to \"it didn't work here\" rather than \"here's when it works and when it doesn't.\"\n\n**Overall significance**: Moderate. Useful cautionary findings but insufficient comparative depth to provide general guidance.\n\n---\n\n## 3. Related Work Completeness\n\n### 3.1 Missing critical references\n\nThe paper has several significant omissions that a reviewer at a top venue would flag:\n\n**A. Foundational representation engineering works:**\n- Representation Engineering (Zou et al., 2023) -- the foundational framework. The paper uses RepE-style direction extraction but does not cite the original work by name in the related work section. This is a significant gap.\n- Contrast-Consistent Search / CCS (Burns et al., 2023) -- an alternative unsupervised direction-finding method that the paper should compare against, or at minimum discuss as an alternative to PCA-based extraction.\n- Activation Addition (Turner et al., 2023) -- inference-time steering. The paper's observation that d_syc exists but fails as a training signal immediately raises the question: does d_syc work for inference-time steering? This zero-training-cost alternative is not discussed and is the most conspicuous missing baseline.\n\n**B. Steering vector critiques:**\n- Non-identifiability of steering vectors (Venkatesh & Kurapath, 2026) -- directly relevant to why directions may fail as training signals.\n- Generalization and reliability of steering vectors (Tan et al., 2024) -- documents OOD degradation and anti-steerability, directly relevant to the direction drift finding.\n\n**C. Sycophancy-specific mechanistic works:**\n- \"Sycophancy Hides Linearly in the Attention Heads\" (2026) -- provides layer-specific guidance and head-level analysis that could inform better direction extraction.\n- \"Sycophantic Anchors\" (2026) -- 87% vs 13% high-importance anchor asymmetry; directly relevant to the premise that representation-level signals should detect sycophancy.\n- \"The Hypocrisy Gap\" (2026) -- SAE-based probes achieving AUROC 0.55-0.73, which contextualizes the paper's 0.801 AUROC and would support the argument that representation-level detection is harder than claimed.\n- \"Good Arguments Against the People Pleasers\" (2026) -- documents \"masked sycophancy\" with reasoning chain analysis, directly relevant to the R1-R3 disagreement analysis.\n- \"How RLHF Amplifies Sycophancy\" (ICLR 2026) -- causal mechanism linking RLHF to sycophancy; important for understanding why the problem exists.\n\n**D. DPO/RLHF-based sycophancy interventions:**\n- The most commercially deployed anti-sycophancy methods (DPO variants, constitutional AI approaches) are not discussed. This is a gap in the practical landscape.\n\n**E. Internal-signal RL:**\n- INTUITOR (ICLR 2026) -- validates internal model signals as GRPO rewards for math, achieving parity with external rewards. Highly relevant comparison: why does internal-signal GRPO work for math but not sycophancy?\n\n**F. Multi-turn alignment:**\n- The paper's multi-turn alignment paragraph cites no specific methods. \"When Attention Closes\" (2026), T3 (ICLR 2026 Oral), and RC-GRPO (2026) are all relevant.\n\n**Reference count**: The paper appears to have approximately 12-15 references based on the summary. For a paper claiming to establish \"boundary conditions\" for a field, this is substantially below the 30-40 references expected at a top venue. The Related Work reads more like a brief literature positioning than a thorough survey.\n\n### 3.2 Positioning accuracy\n\nWhat the paper gets right:\n- CRAFT is correctly identified as the most methodologically adjacent work.\n- ACT is correctly characterized as enforcing undifferentiated consistency.\n- \"Pressure, What Pressure?\" is correctly positioned as the behavioral GRPO decomposition baseline.\n- Linear Probe Penalties are correctly distinguished (reward model vs policy model, binary vs continuous).\n\nWhat the paper gets wrong or underemphasizes:\n- The paper frames d_syc extraction as if it is a novel contribution, when the direction extraction methodology is entirely standard RepE/CCS. The novelty (such as it is) lies in the multi-turn application and the failure analysis, not in the extraction itself.\n- The CRAFT comparison is too brief. CRAFT achieves strong positive results with hidden-state GRPO rewards for safety. A paper reporting negative results with the same paradigm for sycophancy MUST provide a detailed comparison explaining the divergence. Is it discriminability? Stability? Domain properties? This analysis is absent.\n- The Knowledge-Prediction Gap literature (13-29% representation-behavioral disagreement) is mentioned in the summary but the paper's own finding of only 3.4% R1-R3 disagreement is in stark contrast. The paper should explicitly reconcile this discrepancy: either the prior estimates are inflated, or the paper's direction is not capturing the same phenomenon, or the multi-turn setting compresses the gap. This is a critical missing analysis.\n\n### 3.3 Missing baselines\n\n**Most conspicuous omission: inference-time activation steering.** If d_syc is extracted, the zero-training-cost alternative is to subtract alpha * d_syc at inference time, as in Activation Addition. If this achieves 70-80% of the desired effect at zero training cost, the entire DC-GRPO framework is unnecessary regardless of whether the training-time version works. If it fails, that is additional evidence about the direction's limitations. Either way, this baseline is essential. Its absence is the single most significant experimental gap.\n\n**Continuous probe baseline**: The paper reports that continuous probe matches DC-GRPO (p=0.448). This is mentioned in the summary but the implications are devastating for the novelty claim: if a simple logistic regression probability matches the full directional decomposition, then the geometric structure of d_syc provides no advantage over a generic continuous activation-based signal. The paper should discuss this more prominently.\n\n---\n\n## 4. Framing and Narrative\n\n### 4.1 Story coherence\n\nThe paper's narrative arc is: \"We hypothesized that RepE directions could serve as training rewards for sycophancy. We tested this rigorously. It didn't work. Here's why.\"\n\nThis is a clean and honest arc. The \"boundary conditions\" subtitle appropriately signals that the paper is more diagnostic than prescriptive.\n\n### 4.2 Weaknesses in framing\n\n**A. Scope-claim mismatch.** The paper's broadest claims (\"boundary conditions of representation-level signals\") are not supported by its narrow experimental scope (one model, one scale, one direction method, one training configuration). The word \"boundary\" implies a mapped-out region with identified thresholds. What the paper actually provides is a single failed experiment with post-hoc analysis.\n\n**B. The \"direction is real but redundant\" conclusion is under-argued.** The paper claims the direction genuinely encodes sycophancy (AUROC 0.801) but is redundant with behavioral signals (3.4% disagreement). However, 0.801 AUROC is only moderate. An alternative interpretation is that the direction is partially real but partially confounded, and the genuine component is too weak to add value over behavioral signals. The paper does not adequately distinguish these two interpretations.\n\n**C. Direction drift framing is one-sided.** The paper presents drift (cosine to 0.66) as a fundamental obstacle. But the drift could also be evidence that training IS working -- the model's representation space is reorganizing, and the direction computed from the pre-training distribution is no longer optimal. If recalibration were more effective (online estimation, EMA updates, higher frequency), drift might be manageable. The paper does not test enough mitigation strategies to claim the obstacle is fundamental.\n\n**D. The negative result may be a power issue.** With p=0.187 for DC-GRPO vs R3-only and only 3 seeds, the paper cannot distinguish \"no effect\" from \"small effect that 3 seeds cannot detect.\" A Bayesian analysis or effect size (Cohen's d) would be more informative than the frequentist null.\n\n### 4.3 Does the negative result story hold together?\n\nPartially. The three failure modes (low SNR, direction drift, low R1-R3 disagreement) are internally consistent and mutually reinforcing. The cascade is plausible: moderate AUROC + training drift = noisy R1 reward + behavioral signals already capture most of the signal = R1 adds little. This is a coherent account.\n\nHowever, the narrative would be substantially stronger if the paper could explain why CRAFT succeeds with the same paradigm. Without this comparison, a reviewer can reasonably ask: \"Is the problem with RepE-as-reward in general, or with this specific implementation for this specific task?\"\n\n---\n\n## 5. Specific Weaknesses (Numbered)\n\n**W1. Statistical power is critically insufficient (Major).** All significance claims rest on 3 seeds (2 degrees of freedom). The key null result (p=0.187) is uninformative: it could reflect a true null, a small positive effect, or even a moderate effect that 3 seeds cannot detect. The continuous probe comparison (p=0.448) is similarly ambiguous. At a top venue, 5-10 seeds is the minimum expectation. Without power analysis or effect size reporting, the paper cannot distinguish \"no effect\" from \"underpowered experiment.\"\n\n**W2. CRAFT comparison is absent or insufficient (Major).** CRAFT uses the same paradigm (hidden-state rewards + GRPO) and achieves strong positive results for safety. The paper reports negative results for sycophancy. This divergence is the most important question the paper should answer but doesn't. Without understanding WHY the paradigm works for safety but not sycophancy, the paper's contribution is limited to \"it didn't work here\" rather than a generalizable insight.\n\n**W3. Inference-time steering baseline is missing (Major).** Activation Addition using d_syc at inference time is the zero-cost alternative. Its absence is conspicuous. If steering works, the direction has value but training integration is the bottleneck. If steering fails, the direction itself is the problem. This diagnostic would substantially clarify the paper's conclusions.\n\n**W4. Boundary conditions are not actually mapped (Major).** The title promises \"boundary conditions\" but the paper tests a single point in the method space. No alternative direction methods (CCS, non-linear), no adaptive reward weighting, no exploration of AUROC thresholds where RepE-as-reward becomes viable, no model scale variation. This is a single negative result, not a boundary map.\n\n**W5. Related work is thin (~15 references) for the scope of claims (Moderate-to-Major).** A paper claiming to establish boundary conditions for representation-level training signals needs comprehensive coverage. At least 15-20 additional references are needed (see Section 3.1 above). Key omissions include RepE (Zou et al.), CCS (Burns et al.), Activation Addition, steering vector non-identifiability, INTUITOR, \"Sycophancy Hides Linearly,\" and DPO-based sycophancy methods.\n\n**W6. R1-R3 disagreement analysis conflates signal degradation with signal absence (Moderate).** The 3.4% disagreement rate is measured across the full training run, during which d_syc degrades (cosine to 0.66, held-out AUROC declining). Low disagreement in later phases could reflect R1's degraded accuracy rather than genuine absence of masked sycophancy. The paper should report disagreement separately for early training (when the direction is fresh) vs late training.\n\n**W7. The Knowledge-Prediction Gap discrepancy is not reconciled (Moderate).** Prior work documents 13-29% representation-behavioral disagreement. This paper finds 3.4%. This 4-9x discrepancy needs explanation. Possible reasons: different tasks, different probing methods, multi-turn vs single-turn, or the paper's direction is capturing something different from prior probes. Without this analysis, the low disagreement finding is hard to interpret.\n\n**W8. Three-way decomposition is underpowered (Moderate).** 60 neutral pairs for a finding presented as one of the paper's key insights. No bootstrap confidence interval is reported for the cosine similarity. Not replicated on the second model (Llama-3-8B). The claim that \"linear methods fundamentally cannot separate\" sycophancy from revision based on near-antiparallel geometry from a single underpowered experiment is an overreach.\n\n**W9. No figures (Minor-to-Moderate).** A paper with rich training dynamics (direction stability curves, AUROC by layer, reward trajectories, drift patterns) that uses only tables misses an opportunity to communicate findings effectively. Layer-wise AUROC curves and direction drift trajectories would be far more impactful as figures.\n\n**W10. \"Continuous probe matches DC-GRPO\" undermines the core premise (Moderate).** If a simple logistic regression probability (p=0.448 vs DC-GRPO) achieves equivalent results, the directional geometric structure of d_syc provides no value over a generic continuous activation-based signal. The paper should discuss whether THIS is the actual finding: not that representation-level rewards fail, but that directional decomposition specifically provides no advantage over simpler representation-level approaches.\n\n---\n\n## 6. Specific Strengths (Numbered)\n\n**S1. Intellectual honesty is exemplary.** The paper reports DC-GRPO's failure transparently, with all p-values, without cherry-picking favorable metrics or subsets. The framing does not oversell. This sets a good standard for negative-result reporting.\n\n**S2. Evidence-strength stratification is methodologically sound.** The AUROC gradient across evidence strengths (with weak evidence being easiest to classify) is a genuine insight. It reveals that d_syc partially encodes \"strength of reason to revise\" rather than pure sycophantic cognition. This finding generalizes to the broader activation-space probing literature.\n\n**S3. Direction stability tracking is thorough and informative.** The cosine similarity trajectory, held-out AUROC monitoring, and recalibration event logging provide a detailed mechanistic picture of representation drift under RL training. The drift rate quantification is a practical contribution for anyone building representation-level training signals.\n\n**S4. The diagnostic analysis framework (SNR + stability + disagreement) is reusable.** Future work on representation-level rewards can use the paper's three-factor diagnostic framework to evaluate whether their approach will succeed before committing to full training runs. This is a modest but real methodological contribution.\n\n**S5. Baseline coverage is appropriate.** R3-only, ACT-style, binary probe, continuous probe, and vanilla span the relevant design space and form a logical hierarchy. Each serves a clear purpose in the argument.\n\n**S6. Style-controlled data construction addresses the most obvious confound.** The L0 AUROC near random (0.52) after style control, compared to the pre-style-control trivial separability, demonstrates that the paper correctly identifies and addresses surface confounds.\n\n**S7. The cross-model direction analysis is useful.** Showing that the layer-wise emergence pattern generalizes (similar S-curve on Llama-3-8B) while the specific direction does not transfer (cosine 0.34) separates \"phenomenon exists\" from \"direction is portable.\"\n\n---\n\n## 7. Questions for Authors (Numbered)\n\n1. **Why does CRAFT succeed where DC-GRPO fails?** CRAFT uses hidden-state directional projections as GRPO rewards for safety and achieves strong positive results. Your paper uses the same paradigm for sycophancy and finds null results. What is your hypothesis for this divergence? Is it discriminability (safety directions may have higher AUROC)? Stability (safety directions may drift less)? Behavioral-representational overlap (safety may have higher behavioral-representation disagreement)?\n\n2. **What does inference-time activation steering with d_syc achieve?** Subtracting alpha * d_syc at inference time on the R3-only trained model is the zero-cost alternative. Does it reduce sycophancy? If yes, the direction has value but training integration is the bottleneck. If no, the direction itself is insufficient.\n\n3. **What is Cohen's d for DC-GRPO vs R3-only?** With p=0.187 on 3 seeds, the frequentist result is uninformative. An effect size estimate would clarify whether this is \"no effect\" or \"small effect, underpowered study.\"\n\n4. **Why is R1-R3 disagreement (3.4%) so much lower than the Knowledge-Prediction Gap literature (13-29%)?** Is this a measurement artifact, a property of the multi-turn setting, or evidence that d_syc captures a different phenomenon from prior probes?\n\n5. **Have you tested adaptive reward weighting?** Decaying w1 toward zero as R1-R3 correlation increases (or as held-out AUROC degrades) would let the system self-detect when R1 becomes noise. If this improves results, the failure is in the static weighting scheme, not in the representation-level reward concept.\n\n6. **What happens with more frequent or online direction recalibration?** The paper uses cosine < 0.7 threshold with 500-step monitoring. Would continuous EMA updates or per-batch direction estimation resolve the drift problem?\n\n7. **For the continuous probe baseline: what is the probe's AUROC on calibration data?** If it matches d_syc's AUROC (0.801), the equivalence in training outcomes is unsurprising. If it is lower, the equivalence despite lower discriminability would be a puzzle worth discussing.\n\n8. **Have you considered CCS as an alternative to PCA-based direction extraction?** CCS finds directions via unsupervised consistency optimization and may produce more robust directions less susceptible to evidence-strength confounds.\n\n9. **What is the R1-R3 disagreement rate in the first 1000 training steps (before significant drift)?** If disagreement is higher early (when the direction is fresh) and declines as the direction degrades, the 3.4% aggregate is misleading.\n\n10. **Would full fine-tuning (instead of LoRA) produce different direction stability?** LoRA constrains updates to a low-rank subspace, which could either help (by limiting drift) or hurt (by creating rank-deficient representation changes that the direction cannot track).\n\n---\n\n## 8. Overall Assessment\n\n### Score: 3/6 (Weak Reject)\n\n### Justification\n\nThe paper asks a well-motivated question (can RepE directions serve as training rewards for sycophancy?) and provides an honest negative answer with useful diagnostic analysis. The evidence-strength stratification, direction stability tracking, and style-controlled data construction are individually sound experimental contributions. The intellectual honesty in reporting negative results is commendable.\n\nHowever, three issues prevent acceptance at a top venue:\n\n**1. The scope-claim ratio is poor.** \"Boundary conditions\" in the title implies a systematic mapping of where representation-level rewards succeed and fail. The paper tests one method configuration on one model at one scale and finds failure. This is a data point, not a boundary map. The claims need to be either narrowed to match the scope (\"DC-GRPO with linear directions on Qwen3-8B at LoRA rank 64 fails to outperform behavioral rewards\") or the experiments need to be broadened (alternative direction methods, adaptive weighting, model scale variation).\n\n**2. Statistical evidence is insufficient.** Three seeds provide 2 degrees of freedom for t-tests. The key null result (p=0.187) is compatible with both \"no effect\" and \"small-to-moderate effect, underpowered.\" Without effect sizes, power analysis, or more seeds, the negative result is not conclusive. For a paper whose entire contribution rests on a null finding, this is a critical gap.\n\n**3. The CRAFT comparison gap undermines the narrative.** The paper's implicit claim is that representation-level rewards have structural limitations for sycophancy training. But CRAFT demonstrates that the same paradigm works for safety. Without explaining this divergence, the paper cannot distinguish \"fundamental limitation of RepE-as-reward\" from \"sycophancy-specific difficulty\" from \"implementation issue.\" This comparison is the single most important missing analysis.\n\n**Secondary concerns**: thin related work (~15 references, many key works absent), missing inference-time steering baseline, underpowered three-way decomposition, no figures, and the continuous-probe equivalence (p=0.448) suggesting that directional geometry specifically adds nothing even if representation-level signals have some value.\n\n### Path to acceptance:\n1. Run 7-10 seeds and report effect sizes (Cohen's d) with bootstrap CIs\n2. Add CRAFT comparative analysis: why does hidden-state GRPO work for safety but not sycophancy?\n3. Add inference-time steering baseline\n4. Test 2-3 mitigation strategies (adaptive w1, online recalibration, CCS) to demonstrate boundaries are real\n5. Expand references to 30+\n6. Add 3-4 key figures (layer AUROC curves, drift trajectory, reward dynamics)\n7. Narrow title/claims to match experimental scope, or broaden experiments to match claims\n\n### Confidence: 4/5 (High)\nDomain expertise in representation engineering, RL for alignment, and sycophancy mitigation. Main uncertainty: whether results would differ at larger model scales or with alternative direction extraction methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5c0e129-f55e-4047-93fc-25ef75bfad81",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9htxiBUdd6emHyHN1Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5cf138e4-f824-45d7-a05b-293fa32d4423",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015MVe6K4jxaiCGAVkLEwciX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 788,
      "cache_read_input_tokens": 98675,
      "output_tokens": 6762,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 788
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6762,
          "cache_read_input_tokens": 98675,
          "cache_creation_input_tokens": 788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 788,
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

_source line 42 · 2026-05-18T13:59:53.655Z_

<details><summary>↩ Tool result · `toolu_01DUjt51i56qHzZcr8seEHNj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/worst/review_report.md\", \"dream_id\": \"dream_20260518T125925\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5cf138e4-f824-45d7-a05b-293fa32d4423",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "a3fa95b4ad97e525f",
  "type": "user",
  "uuid": "4625a757-2fdb-4b11-adea-436f8c4676b9",
  "sourceToolAssistantUUID": "5cf138e4-f824-45d7-a05b-293fa32d4423",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-18T14:00:01.803Z_

Review submitted successfully. Here is a summary of the key findings:

**Score: 3/6 (Weak Reject)**

The review identifies three critical issues preventing acceptance:

1. **Scope-claim mismatch**: The paper promises "boundary conditions" but tests a single method configuration on one model at one scale. This is a data point, not a boundary map.

2. **Insufficient statistical power**: 3 seeds (2 degrees of freedom) cannot conclusively establish a null result. The key p=0.187 is compatible with both "no effect" and "small effect, underpowered." Effect sizes and more seeds are essential.

3. **Missing CRAFT comparison**: CRAFT demonstrates that hidden-state GRPO rewards work for safety alignment. The paper reports failure for sycophancy with the same paradigm but never explains the divergence. This is the single most important missing analysis.

**Additional major weaknesses**: Missing inference-time steering baseline (the zero-cost alternative), thin related work (~15 references when 30+ are needed, with key omissions including RepE, CCS, Activation Addition, INTUITOR, steering vector critiques), underpowered three-way decomposition, and the continuous probe equivalence (p=0.448) suggesting directional geometry adds nothing over simpler representation-level approaches.

**Strengths acknowledged**: Exemplary intellectual honesty, sound evidence-strength stratification, thorough direction stability tracking, reusable diagnostic framework, appropriate baseline coverage, and careful style-controlled data construction.

The review report is saved at `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/worst/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4625a757-2fdb-4b11-adea-436f8c4676b9",
  "isSidechain": true,
  "agentId": "a3fa95b4ad97e525f",
  "requestId": "req_011CbA9vLQFGriqbmZNhPyu7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6575d937-2215-45cc-8889-5d1679ad87b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Y1vbPYhQ6DxyyqoQ99y9p",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6897,
      "cache_read_input_tokens": 99463,
      "output_tokens": 405,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6897
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 405,
          "cache_read_input_tokens": 99463,
          "cache_creation_input_tokens": 6897,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6897,
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
