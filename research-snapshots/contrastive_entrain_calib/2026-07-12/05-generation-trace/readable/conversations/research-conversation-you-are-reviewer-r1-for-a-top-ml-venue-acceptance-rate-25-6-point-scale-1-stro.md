# Research conversation: You are Reviewer R1 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aa18bf1166c4112dc.jsonl`
- **Structured JSON:** [`2d7020a28780f28a09e2.json`](../../sessions/2d/2d7020a28780f28a09e2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-18T13:55:27.689Z_

You are Reviewer R1 for a top ML venue (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus: **methodology soundness and experimental rigor**.

## Paper Summary

**Title**: "Do Sycophancy Directions Transfer to Training Rewards? Boundary Conditions of Representation-Level Signals for Multi-Turn Belief Revision"

**Core idea**: The paper investigates whether linear directions in activation space (d_syc) that distinguish sycophantic from genuine responses can serve as training reward signals via Direction-Contrastive GRPO (DC-GRPO). DC-GRPO combines: R1 (directional projection reward), R2 (rank-based contrastive reward), R3 (NLI behavioral reward). The paper frames itself as a "boundary conditions" study, reporting a negative result: DC-GRPO does not significantly outperform R3-only.

## Method (Section 3)
- **3.1 Direction Extraction**: Contrastive pairs (sycophantic vs genuine responses), style-controlled. Extract residual stream activations at first assistant token position. d_syc = PCA_1 of difference vectors. 200 pairs (80 weak + 60 medium + 60 strong evidence).
- **3.2 DC-GRPO**: R1 = -⟨h, d_syc⟩ (directional projection); R2 = rank-based contrastive on R1 scores; R3 = NLI behavioral reward. Combined: R = 0.3*R1 + 0.2*R2 + 0.5*R3.
- **3.3 Recalibration**: Monitor cosine similarity every 500 steps, recompute d_syc when it drops below 0.70.
- **3.4 Metrics**: NoF (No-Flip Rate, ↓), WRR (Warranted Revision Rate, ↑), RC-AUC, MT-Bench, MMLU.

## Key Experimental Results

**Exp 1 (Calibration)**: d_syc AUROC = 0.801 at L19, 95% CI [0.766, 0.836]. Layer-wise emergence from L0 (0.52) to L19 (0.801). Weak evidence AUROC lowest (0.773).

**Exp 2 (DC-GRPO main)**: NoF 0.312±0.024, WRR 0.618±0.019. R1 and R3 rewards become highly correlated (r > 0.9) after step 4000.

**Exp 3 (R3-only)**: NoF 0.325±0.028, WRR 0.621±0.022. Nearly matches DC-GRPO.

**Exp 4 (ACT-style)**: NoF 0.358±0.031, WRR 0.571±0.026. Significantly worse.

**Exp 5 (Full evaluation, Table 6-7)**:
- DC-GRPO vs R3-only: NoF diff -1.3pp, p=0.187 (not significant)
- DC-GRPO vs ACT: NoF diff -4.6pp, p=0.008 (significant)
- DC-GRPO vs Cont. Probe: NoF diff +0.7pp, p=0.448 (not significant)
- Cont. Probe vs R3-only: NoF diff -2.0pp, p=0.098 (not significant)
- Continuous Probe achieves best NoF (0.305) and WRR (0.625).

**Exp 6 (Direction stability)**: Cosine similarity drops to 0.66. 3 recalibrations triggered. Held-out AUROC degrades from 0.801 to 0.741.

**Exp 7 (Disagreement)**: R1-R3 disagreement only 3.4%. Only 3/8 manually checked cases were genuine masked sycophancy.

**Exp 8-9 (Ablations)**: R1-only: NoF 0.398 (barely better than vanilla 0.448), WRR drops below vanilla. R1+R2 no R3: NoF 0.375, surface inconsistency 12%.

**Exp 10 (Turn depth)**: DC-GRPO advantage over R3-only is constant ~1.3pp across turn depths, not increasing at deeper turns.

**Exp 12 (Cross-model)**: Llama-3-8B AUROC 0.731 (below 0.75 gate). Cross-model d_syc cosine only 0.31.

**Exp 13 (Three-way)**: d_gen and d_syc cosine = -0.82. Independent d_gen AUROC only 0.68.

**Exp 14 (Continuous probe)**: Matches/slightly exceeds DC-GRPO on all metrics without recalibration.

**Exp 15 (Weight sensitivity)**: R1-dominant (w1=0.6) is worst config. R3-dominant (w1=0.1) nearly matches R3-only. Optimal R1 weight trends toward zero.

## Experiment Coverage vs Design

The review context lists 15 imagined experiments (exp-001 through exp-015). The paper covers all 15 experiments across Sections 4.1-4.13. All major experiments from the design are reported.

## Your Task

Provide a detailed review focusing on:

1. **Methodology soundness**: Is the method well-defined? Are there flaws in direction extraction, reward design, or training procedure?
2. **Experimental rigor**: Statistical tests, number of seeds, evaluation metrics, baseline selection, ablation completeness.
3. **Reproducibility**: Are details sufficient to reproduce?
4. **Specific weaknesses** in methods and experiments (numbered list).
5. **Specific strengths** in methods and experiments (numbered list).
6. **Questions for authors** (numbered list).
7. **Overall assessment**: Score (1-6) with justification.

Be thorough and critical. This is a top venue review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "3f4bc89d-81cc-440a-9237-da5d95aae66c",
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

_source line 2 · 2026-05-18T13:55:27.695Z_

```json
{
  "parentUuid": "3f4bc89d-81cc-440a-9237-da5d95aae66c",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
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
  "uuid": "dea0ce6d-7eff-4c7b-b5a0-22b5a1c5330b",
  "timestamp": "2026-05-18T13:55:27.695Z",
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

_source line 3 · 2026-05-18T13:55:33.410Z_



I'll start by reading the paper and all supporting materials to provide a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dea0ce6d-7eff-4c7b-b5a0-22b5a1c5330b",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9ajHbQJTmHdMCscmhh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f6e5f96-e805-4173-852e-b33ade2e9fe2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Dpa2jsqYBXKrMYnGDaY1e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16873,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16873,
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

_source line 4 · 2026-05-18T13:55:33.917Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013FAX8mtmgCdxakKNf2cjdD`</summary>

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
  "parentUuid": "1f6e5f96-e805-4173-852e-b33ade2e9fe2",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9ajHbQJTmHdMCscmhh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de8801b2-9509-4814-aec7-35c3cbc1fd92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Dpa2jsqYBXKrMYnGDaY1e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16873,
      "cache_read_input_tokens": 0,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16873
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16873,
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

_source line 5 · 2026-05-18T13:55:33.923Z_

<details><summary>↩ Tool result · `toolu_013FAX8mtmgCdxakKNf2cjdD`</summary>

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
  "parentUuid": "de8801b2-9509-4814-aec7-35c3cbc1fd92",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "f7e4e790-b6fb-4caf-a4d0-6a53267be279",
  "sourceToolAssistantUUID": "de8801b2-9509-4814-aec7-35c3cbc1fd92",
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

_source line 6 · 2026-05-18T13:55:37.440Z_



Let me read the paper and all supporting materials thoroughly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7e4e790-b6fb-4caf-a4d0-6a53267be279",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9bC7tHrwuCboKEFbX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4c3d6430-48b0-410f-8599-7d7b30daf108",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9wz18fL9MyrXXNd5eFfot",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 7 · 2026-05-18T13:55:38.380Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_012zfkwipsdvFnjcyAEvVsyt`</summary>

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
  "parentUuid": "4c3d6430-48b0-410f-8599-7d7b30daf108",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9bC7tHrwuCboKEFbX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6681ce56-172e-4251-90ec-f546a9faf1de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9wz18fL9MyrXXNd5eFfot",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 8 · 2026-05-18T13:55:38.406Z_

<details><summary>↩ Tool result · `toolu_012zfkwipsdvFnjcyAEvVsyt`</summary>

```text
{"result":"# 项目 contrastive_entrain_calib 概况\n\n## 实验状态\n暂无实验记录\n\n## 最新报告\n（尚未生成）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6681ce56-172e-4251-90ec-f546a9faf1de",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "96d449a4-5b1f-4c1f-9202-f97303c49eea",
  "sourceToolAssistantUUID": "6681ce56-172e-4251-90ec-f546a9faf1de",
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

_source line 9 · 2026-05-18T13:55:39.803Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016w4zmKvdHPmJg2TGFjrhtC`</summary>

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
  "parentUuid": "96d449a4-5b1f-4c1f-9202-f97303c49eea",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9bC7tHrwuCboKEFbX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efa3eb16-71e7-469e-a414-f39e7e02be72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9wz18fL9MyrXXNd5eFfot",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16873,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
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

_source line 10 · 2026-05-18T13:55:39.821Z_

<details><summary>↩ Tool result · `toolu_016w4zmKvdHPmJg2TGFjrhtC`</summary>

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
  "parentUuid": "efa3eb16-71e7-469e-a414-f39e7e02be72",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "30bccb69-a408-4859-918b-fead5ad40e93",
  "sourceToolAssistantUUID": "efa3eb16-71e7-469e-a414-f39e7e02be72",
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

_source line 11 · 2026-05-18T13:55:40.016Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01UeZzJj9xgKBsFpRv2rmJAi`</summary>

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
  "parentUuid": "30bccb69-a408-4859-918b-fead5ad40e93",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9bC7tHrwuCboKEFbX4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "12c2b740-4caf-4891-aa9d-27310e8c0364",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9wz18fL9MyrXXNd5eFfot",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 16873,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 259,
          "cache_read_input_tokens": 16873,
          "cache_creation_input_tokens": 1447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1447,
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

_source line 12 · 2026-05-18T13:55:40.027Z_

<details><summary>↩ Tool result · `toolu_01UeZzJj9xgKBsFpRv2rmJAi`</summary>

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
  "parentUuid": "12c2b740-4caf-4891-aa9d-27310e8c0364",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "814b703b-84d9-4148-ae3a-dc5215cb19ab",
  "sourceToolAssistantUUID": "12c2b740-4caf-4891-aa9d-27310e8c0364",
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

_source line 13 · 2026-05-18T13:55:43.013Z_

<details open><summary>🔧 Tool call — Read · `toolu_016Gzb3Bu4wC9RaHZmFjuBBH`</summary>

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
  "parentUuid": "814b703b-84d9-4148-ae3a-dc5215cb19ab",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9be8Zsh4uqfqTaCifF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "267e1d01-1fc7-4516-bc99-a1410f165a71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJjjkoAQ2Ls2SzxsudkZ3w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 975,
      "cache_read_input_tokens": 18320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 975,
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

_source line 14 · 2026-05-18T13:55:43.315Z_

<details><summary>↩ Tool result · `toolu_016Gzb3Bu4wC9RaHZmFjuBBH`</summary>

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
  "parentUuid": "267e1d01-1fc7-4516-bc99-a1410f165a71",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "5062cba2-4bb7-4ad5-bc4b-ebf1bbfdafcd",
  "sourceToolAssistantUUID": "267e1d01-1fc7-4516-bc99-a1410f165a71",
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

_source line 15 · 2026-05-18T13:55:43.702Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PnUjhLZ6FLthnTAbv8UfnY`</summary>

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
  "parentUuid": "5062cba2-4bb7-4ad5-bc4b-ebf1bbfdafcd",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9be8Zsh4uqfqTaCifF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a56a3c8a-1235-4ece-bbd4-53522afdd853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GJjjkoAQ2Ls2SzxsudkZ3w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 975,
      "cache_read_input_tokens": 18320,
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
          "cache_read_input_tokens": 18320,
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

_source line 16 · 2026-05-18T13:55:43.710Z_

<details><summary>↩ Tool result · `toolu_01PnUjhLZ6FLthnTAbv8UfnY`</summary>

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
  "parentUuid": "a56a3c8a-1235-4ece-bbd4-53522afdd853",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "42463f82-a7b4-4a87-8a2c-cc38e55ce2d0",
  "sourceToolAssistantUUID": "a56a3c8a-1235-4ece-bbd4-53522afdd853",
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

_source line 17 · 2026-05-18T13:55:48.551Z_

Now let me read the remaining supporting materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42463f82-a7b4-4a87-8a2c-cc38e55ce2d0",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9buxKRoo22LPHRPc4g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62c36cce-b73e-4592-97ac-31009f456456",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014B74qtYrZR3Qnb342yLHxU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13994,
      "cache_read_input_tokens": 19295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13994,
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

_source line 18 · 2026-05-18T13:55:49.592Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NL1hgXTRuX8aUYqD95J2Pa`</summary>

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
  "parentUuid": "62c36cce-b73e-4592-97ac-31009f456456",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9buxKRoo22LPHRPc4g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6908d89-d0bb-4b94-9777-fcab1ec679d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014B74qtYrZR3Qnb342yLHxU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13994,
      "cache_read_input_tokens": 19295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13994,
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

### Tool result

_source line 19 · 2026-05-18T13:55:49.604Z_

<details><summary>↩ Tool result · `toolu_01NL1hgXTRuX8aUYqD95J2Pa`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'contrastive_entrain_calib'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6908d89-d0bb-4b94-9777-fcab1ec679d1",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "cbccf189-ecb3-4942-9b8e-2ded4497463e",
  "sourceToolAssistantUUID": "a6908d89-d0bb-4b94-9777-fcab1ec679d1",
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

_source line 20 · 2026-05-18T13:55:50.067Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0186i5GoAYvEhJE578swfERy`</summary>

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
  "parentUuid": "cbccf189-ecb3-4942-9b8e-2ded4497463e",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9buxKRoo22LPHRPc4g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b00884d-ed3d-49aa-b1e2-9ec789db3cf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014B74qtYrZR3Qnb342yLHxU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13994,
      "cache_read_input_tokens": 19295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13994,
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

### Tool result

_source line 21 · 2026-05-18T13:55:50.076Z_

<details><summary>↩ Tool result · `toolu_0186i5GoAYvEhJE578swfERy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/ROADMAP.md\", \"content\": \"# contrastive_entrain_calib — Research Dashboard\\n\\n> 最后更新: 2026-05-18 12:45 UTC | 更新原因: D008 Dream 分析完成，framing/plan 更新后同步 ROADMAP\\n\\n## 核心方向\\nDirection-Contrastive GRPO：将 RepE 风格的 d_syc 方向分解作为连续 GRPO reward 信号，打破多轮对话中 sycophancy-revision 的 double-bind。详见 paper_framing.md。\\n\\n## 当前阶段\\n**Research Phase** — Post-MVP kickoff 完成，Dream 分析完成（D008），framing/plan 已更新，待 re-dream 验证后启动 P0 实验。\\n\\n## 当前进展\\n- MVP v2+v2.1 PASS（D007）：d_syc 确认捕获认知信号，非表面风格\\n- exp-001 calibration_data_expansion PASS：200 pairs CV AUROC 0.8269±0.028，STOP-gate 通过\\n- Dream 首轮完成（best 4/6, median 3.5/6, worst 3/6）：识别 3 个结构性问题（RepE 定位缺失、单模型、权重无 justification）\\n- paper_framing.md 已更新：RepE/CCS 定位、Claim 3 降级、新增 reviewer concern 应对\\n- experiment_plan.yaml 已更新：新增 exp-014/015，exp-012 升级 P1，总预算 461h\\n- dcgrpo_trainer.py 修复完成（V1+V2），GPU smoke test 已通过\\n\\n## 近期任务\\n- [ ] Re-dream 验证更新后的 framing/plan\\n- [ ] 向 Manager 申请 ~275h 云 GPU\\n- [ ] Re-dream 通过后审批 P0 实验（exp-002 DC-GRPO + exp-003 R3-only 并行）\\n- [ ] 审批 exp-004 ACT baseline（可与 exp-002/003 并行）\\n- [ ] 验证 dcgrpo_trainer.py 本地/远程文件一致性（195 byte 差异）\\n- [ ] 处理 Agent 队列中的 GPU smoke test 结果\\n\\n## GPU 预算\\n- 本地：westd-29046 RTX PRO 6000 × 2（cuda:0-1），剩余 ~186h\\n- 需求总计：~461h（P0: 308h + P1: 113h + P2: 25h + buffer: 15h）\\n- 缺口：~275h，需申请云 GPU\\n\\n## 实验覆盖率\\n16 个实验（exp-001 至 exp-015，含 Dream 新增），覆盖 3 个 Core Claims + 5 个 Reviewer Concerns。\\n详见 experiment_plan.yaml，可调 compute_coverage_matrix() 查看实时覆盖。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D008 | 2026-05-18 | Dream 分析完成：更新 framing 定位 RepE 基础、降级 Claim 3、新增 exp | exp-014, exp-015, exp-012 |\\n| D007 | 2026-05-18 | MVP 最终 PASS：d_syc 确认捕获超越风格的认知信号，进入 research 阶段 | — |\\n| D006 | 2026-05-18 | Phase 5 v2 PASS (delta=0.0044)，三项 Go/No-Go 全部通过。但采 | — |\\n| D005 | 2026-05-18 | MVP v2 条件性 PASS：形式标准满足但 Turn 3 风格 confound 需 v2.1  | — |\\n| D004 | 2026-05-18 | MVP 不通过：AUROC=1.0 是输入文本差异的 trivial 结果，重新设计校准数据 | — |\\n| D003 | 2026-05-18 | Go/No-Go 从三条件简化为两条件（AUROC + LoRA），cosine 条件在二元设计下退 | — |\\n| D002 | 2026-05-18 | 采纳 Reviewer 4 项 MVP 改进：模型统一 Qwen3-8B、cosine<0.3 门槛 | — |\\n| D001 | 2026-05-18 | MVP 方案：多轮方向判别力测试（AUROC ≥ 0.85 为 go/no-go） | — |\\n\\n\\n\", \"total_chars\": 2079, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b00884d-ed3d-49aa-b1e2-9ec789db3cf5",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "adc61b8d-8b4e-4080-a362-e6a400424224",
  "sourceToolAssistantUUID": "8b00884d-ed3d-49aa-b1e2-9ec789db3cf5",
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

_source line 22 · 2026-05-18T13:55:51.466Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SomNu549WGH1Ds8ekYyBT9`</summary>

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
  "parentUuid": "adc61b8d-8b4e-4080-a362-e6a400424224",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9buxKRoo22LPHRPc4g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "018bb969-9450-4913-8297-e49ff5728aca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014B74qtYrZR3Qnb342yLHxU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13994,
      "cache_read_input_tokens": 19295,
      "output_tokens": 293,
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
          "output_tokens": 293,
          "cache_read_input_tokens": 19295,
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

_source line 23 · 2026-05-18T13:55:52.131Z_

<details><summary>↩ Tool result · `toolu_01SomNu549WGH1Ds8ekYyBT9`</summary>

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
  "parentUuid": "018bb969-9450-4913-8297-e49ff5728aca",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "24e3c173-4ff3-4ae3-a8ce-e15ea4fbe1e9",
  "sourceToolAssistantUUID": "018bb969-9450-4913-8297-e49ff5728aca",
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

_source line 24 · 2026-05-18T13:55:57.769Z_

Now let me read the experiment plan and the review reports from the previous dream cycle.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24e3c173-4ff3-4ae3-a8ce-e15ea4fbe1e9",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9cXmcKRubMampzaWjp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2bbac361-d2d7-4ea2-8994-9541258e8caf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3cjXiQVaGuTeocB7bjuy4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18586,
      "cache_read_input_tokens": 33289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18586,
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

_source line 25 · 2026-05-18T13:55:59.720Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SeMQcaKLjbb3KLkNsV3qgB`</summary>

```json
{
  "pattern": "**/experiment_plan.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bbac361-d2d7-4ea2-8994-9541258e8caf",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9cXmcKRubMampzaWjp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00b0349b-7500-40b6-876f-e426a802d225",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3cjXiQVaGuTeocB7bjuy4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18586,
      "cache_read_input_tokens": 33289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18586,
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

_source line 26 · 2026-05-18T13:55:59.741Z_

<details><summary>↩ Tool result · `toolu_01SeMQcaKLjbb3KLkNsV3qgB`</summary>

```text
experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00b0349b-7500-40b6-876f-e426a802d225",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "7bbbac2b-41d7-4420-b829-60aec793313f",
  "sourceToolAssistantUUID": "00b0349b-7500-40b6-876f-e426a802d225",
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

_source line 27 · 2026-05-18T13:56:01.198Z_

<details open><summary>🔧 Tool call — Read · `toolu_013A7pRvqWzp6Qx4gAmHW5z2`</summary>

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
  "parentUuid": "7bbbac2b-41d7-4420-b829-60aec793313f",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9cXmcKRubMampzaWjp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4dc78804-c890-4e27-874b-d3cc74162a60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3cjXiQVaGuTeocB7bjuy4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18586,
      "cache_read_input_tokens": 33289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18586,
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

_source line 28 · 2026-05-18T13:56:01.217Z_

<details><summary>↩ Tool result · `toolu_013A7pRvqWzp6Qx4gAmHW5z2`</summary>

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
  "parentUuid": "4dc78804-c890-4e27-874b-d3cc74162a60",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "3e389d31-c463-4b96-84e5-0a87c38d4e5c",
  "sourceToolAssistantUUID": "4dc78804-c890-4e27-874b-d3cc74162a60",
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

_source line 29 · 2026-05-18T13:56:01.452Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KfV1H6TGoVzRZAAzpUrA6Z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/median/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e389d31-c463-4b96-84e5-0a87c38d4e5c",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9cXmcKRubMampzaWjp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "860357ed-0ca9-4e6f-9dcc-5df15d5a229c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K3cjXiQVaGuTeocB7bjuy4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18586,
      "cache_read_input_tokens": 33289,
      "output_tokens": 307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18586
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 307,
          "cache_read_input_tokens": 33289,
          "cache_creation_input_tokens": 18586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18586,
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

_source line 30 · 2026-05-18T13:56:01.464Z_

<details><summary>↩ Tool result · `toolu_01KfV1H6TGoVzRZAAzpUrA6Z`</summary>

```text
1	---
2	dream_id: dream_20260518T125925
3	tier: median
4	overall_score: weak reject
5	timestamp: 2026-05-18T13:53:57.840844+00:00
6	---
7	
8	# Dream Review Report: Direction-Contrastive GRPO for Multi-Turn Sycophancy Calibration
9	
10	**Paper:** Direction-Contrastive GRPO for Multi-Turn Sycophancy Calibration: Representation-Level Rewards Break the Revision Double-Bind
11	
12	**Review Mode:** Full (2 Reviewers + Roundtable)
13	
14	**Overall Score:** 3/6 (Weak Reject)
15	
16	---
17	
18	## Roundtable Process
19	
20	- **R1 (Method + Experiments):** Score 3 (Weak Reject)
21	- **R2 (Novelty + Related Work):** Score 3 (Borderline Reject)
22	- **Consensus:** 3/6 (Weak Reject)
23	
24	Both reviewers independently converged on the same core concern: the paper's own Continuous Probe ablation undermines the central contribution claim. Agreement was strong on all major issues; minor divergence on methodology quality (R1 more positive) vs. novelty relative to CRAFT (R2 more critical).
25	
26	---
27	
28	## 1. Summary
29	
30	The paper extracts a linear direction d_syc from the policy model's activation space to discriminate sycophantic capitulation from genuine belief revision, then incorporates it into GRPO training as a three-component reward (R1: directional projection, R2: rank-based contrastive, R3: NLI behavioral). DC-GRPO achieves RC-AUC 0.738 vs 0.641 for behavioral-only training (p=0.008). The paper also proposes RC-AUC as a composite metric and provides analyses of direction stability, turn-depth effects, R1-R3 disagreement, and cross-model transfer.
31	
32	The paper is scientifically honest: it acknowledges that the improvement stems primarily from continuous representation-level signals rather than directional geometry specifically, as a Continuous Probe baseline achieves statistically indistinguishable results (NoF 0.224 vs 0.218, p=0.381; RC-AUC 0.731 vs 0.738, p=0.318).
33	
34	---
35	
36	## 2. Strengths
37	
38	**S1. Well-motivated problem and honest framing.** The sycophancy-revision double-bind is a genuine and important problem. The paper does not overclaim: it transparently reports that directional projection does not significantly outperform simpler continuous probes, and adjusts its claims accordingly. This intellectual honesty is commendable and rare. (Both R1, R2)
39	
40	**S2. Comprehensive experimental design.** The paper covers 15 experiments including appropriate baselines (Vanilla, R3-only, ACT, Binary Probe, Continuous Probe), component ablations (R1-only, R1+R2), sensitivity analysis (5 weight configs), direction stability monitoring, R1-R3 disagreement analysis, three-way direction analysis, and cross-model transfer. All baselines use identical hyperparameters except the reward function. The inclusion of Continuous Probe as a baseline is particularly valuable and the decisive experiment. (R1)
41	
42	**S3. Turn-depth analysis.** DC-GRPO's advantage over R3-only grows from 5.3pp at turn 2 to 9.4pp at turn 4+ on NoF. This is mechanistically plausible: NLI-based behavioral scoring becomes less reliable in longer dialogues while representation-level signals maintain discrimination. This is the paper's strongest independent finding. (Both R1, R2)
43	
44	**S4. Ablation cascade is informative.** The progression R3-only -> R1-only -> R1+R2 -> DC-GRPO clearly demonstrates that each component contributes non-trivially, and that R3 is necessary not just as a safety net but as an active signal source (R1+R2 without R3 produces 8.7% surface inconsistency). (R1)
45	
46	**S5. RC-AUC metric addresses a real gap.** Existing metrics (NoF, WRR) capture only one side of the tradeoff. RC-AUC provides a single composite score. While the metric needs better formal specification, the concept is useful. (R1)
47	
48	---
49	
50	## 3. Weaknesses
51	
52	**W1 (Critical). Continuous Probe ablation undermines the core contribution.**
53	DC-GRPO (NoF 0.218, RC-AUC 0.738) vs Continuous Probe (NoF 0.224, RC-AUC 0.731): differences of 0.6pp and 0.7pp, both statistically non-significant (p=0.381 and p=0.318). The paper's titular and methodological centerpiece, directional projection, is not the source of improvement. The actual finding is that any continuous representation-level signal improves GRPO, which is less novel. The progression Binary Probe (+7.7pp RC-AUC over R3-only) -> Continuous Probe (+9.0pp) -> DC-GRPO (+9.7pp) shows the jump is from discrete to continuous, not from continuous to directional. (Both R1, R2)
54	
55	**W2 (Major). 3 seeds insufficient for statistical claims.**
56	All significance tests use paired t-tests with n=3 (2 degrees of freedom). This is severely underpowered. The WRR comparison between DC-GRPO and R3-only already fails significance (p=0.148). The critical DC-GRPO vs Continuous Probe comparison cannot reliably distinguish true equivalence from inadequate power. Several p-values are reported to 3 decimal places, creating a false impression of precision. At minimum 5 seeds, preferably 10, are needed for the primary comparisons. (Both R1, R2)
57	
58	**W3 (Major). Title and framing mismatch the findings.**
59	"Direction-Contrastive GRPO" implies directional geometry is central, but the data show it is not the differentiating factor. The Introduction builds toward directional projection as the key innovation, but the Discussion acknowledges it is interchangeable with simpler probes. A more accurate title would reference representation-level rewards generally. The paper reads as a partial negative result for directional projection dressed as a methods paper. (R2, R1 concurs)
60	
61	**W4 (Major). Insufficient reference coverage.**
62	22 references is well below the 30-50 typical for top ML venues. Missing critical recent works: mechanistic sycophancy studies (linear separability in attention heads, sycophantic anchors, the hypocrisy gap), INTUITOR (internal signals as GRPO rewards), SAE-based training interventions, non-identifiability of steering vectors. The Related Work does not engage with the 2025-2026 wave of mechanistic sycophancy research that directly contextualizes the d_syc finding. (R2)
63	
64	**W5 (Major). No human validation anywhere in the pipeline.**
65	Neither the calibration data labels (sycophantic vs genuine) nor the evaluation metrics (NoF, WRR) nor the masked sycophancy analysis (R1-R3 disagreement) are validated against human judgments. The 7.6% disagreement rate (4.5% "R1=syc, R3=correct") could be R1 false positives rather than true masked sycophancy. Without ground-truth annotation, the entire argument chain rests on automated classifiers whose accuracy is unverified. (R1, R2)
66	
67	**W6 (Moderate). RC-AUC under-specified.**
68	The paper does not clearly define what thresholds are swept to generate the RC-AUC curve (threshold on total reward? on confidence? on sycophancy score?). Without a precise formal definition, the metric is not reproducible. The paper's strongest results (RC-AUC 0.738 vs 0.641) are on this self-defined metric, which invites the "best results on own metric" criticism. (R1)
69	
70	**W7 (Moderate). Limited model diversity.**
71	Only two 8B models, with unequal training budgets (6500 steps for Qwen3-8B vs 3000 for Llama-3-8B). Cross-model direction cosine of 0.31 confirms directions are model-specific. No exploration of parameter scale effects (e.g., 1.5B or 70B). The cross-model experiment supports framework generality but with caveats that weaken the claim. (R1, R2)
72	
73	**W8 (Minor). R2 reward component inadequately formalized.**
74	"Rank-based contrastive" is described verbally but no mathematical formulation is provided. This is a reproducibility concern for a methods paper. (R1)
75	
76	---
77	
78	## 4. Questions for Authors
79	
80	**Q1.** With only 3 seeds, what is the statistical power to detect the observed DC-GRPO vs Continuous Probe difference (0.6pp NoF) at alpha=0.05? Have you considered running 5-10 seeds for the primary comparisons?
81	
82	**Q2.** Given that Continuous Probe achieves statistically indistinguishable results, what is the practical justification for the additional complexity of directional projection (direction extraction, periodic recalibration, activation extraction)? In what deployment scenario would a practitioner prefer DC-GRPO over a simple logistic regression probe?
83	
84	**Q3.** What is the formal mathematical definition of R2 (rank-based contrastive reward)? The current description is insufficient for reproduction.
85	
86	**Q4.** At turn 4+, does DC-GRPO significantly outperform Continuous Probe specifically? The turn-depth analysis only compares to R3-only and ACT. If Continuous Probe also improves at deeper turns, the turn-depth advantage may not be unique to directional projection.
87	
88	**Q5.** The 4.5% "R1=sycophantic, R3=correct" cases are presented as evidence of masked sycophancy detection. What fraction of these are confirmed as truly sycophantic by human annotators? Would you commit to a 200+ case human evaluation with multiple annotators?
89	
90	**Q6.** How does the paper's AUROC 0.843 compare to prior work achieving AUROC > 0.97 for sycophancy direction extraction in single-turn settings? Is the lower AUROC inherent to multi-turn complexity, or a limitation of the 200-pair calibration set?
91	
92	---
93	
94	## 5. Experiment Coverage Assessment
95	
96	Comparing against the 15 imagined experiments in review_context.yaml:
97	
98	| Experiment | Covered? | Notes |
99	|---|---|---|
100	| exp-001: Calibration data expansion | Yes | Table 1, Section 4.2 |
101	| exp-002: DC-GRPO main | Yes | Tables 2-3, Section 4.3 |
102	| exp-003: R3-only baseline | Yes | Table 2 |
103	| exp-004: ACT-style baseline | Yes | Table 2 |
104	| exp-005: Full evaluation | Yes | Table 2 (6 methods) |
105	| exp-006: Direction stability | Yes | Table 7, Section 4.6 |
106	| exp-007: R1-R3 disagreement | Yes | Tables 10-11, Section 5.2 |
107	| exp-008: Binary probe baseline | Yes | Table 2 |
108	| exp-009: R1-only ablation | Yes | Table 4 |
109	| exp-010: Turn depth analysis | Yes | Table 6, Section 4.5 |
110	| exp-011: R1+R2 no R3 | Yes | Table 4 |
111	| exp-012: Cross-model transfer | Yes | Table 8, Section 4.7 |
112	| exp-013: Three-way direction | Yes | Section 5.3 |
113	| exp-014: Continuous probe | Yes | Tables 2-3, Section 5.1 |
114	| exp-015: Reward weight sensitivity | Yes | Table 5 |
115	
116	**Coverage: 15/15 (100%).** All imagined experiments are reported. The paper is experimentally thorough.
117	
118	---
119	
120	## 6. Detailed Scores
121	
122	| Criterion | Score (1-6) | Justification |
123	|---|---|---|
124	| Novelty | 2.5 | Direction extraction follows established RepE methodology. Integration into GRPO rewards has precedent in CRAFT. The actual finding (continuous signals help) is incremental. |
125	| Soundness | 3.5 | Method is technically correct; experimental design is comprehensive. But 3 seeds is underpowered, RC-AUC is under-specified, and no human validation. |
126	| Significance | 3.0 | The sycophancy-revision tradeoff is important, but the core directional contribution is undermined by the Continuous Probe result. Turn-depth analysis is interesting but statistically fragile. |
127	| Presentation | 3.5 | Well-organized, honest framing. But title/framing mismatch findings. Insufficient references. R2 formalization missing. |
128	| **Overall** | **3.0** | **Weak Reject** |
129	
130	---
131	
132	## 7. Consensus Recommendation
133	
134	**Score: 3/6 (Weak Reject)**
135	
136	The paper addresses a well-motivated problem with a comprehensive experimental design and commendable scientific honesty. The turn-depth analysis and the finding that continuous representation-level signals improve GRPO are genuine contributions.
137	
138	However, the paper does not meet the bar for a top ML venue (~25% acceptance rate) due to three fundamental issues:
139	
140	1. **The directional projection, which is the paper's central and titular contribution, does not significantly outperform a simple continuous probe (p=0.381 NoF, p=0.318 RC-AUC).** The paper's own data show the improvement comes from signal continuity, not directional geometry.
141	
142	2. **Statistical evidence rests on 3 seeds with 2 degrees of freedom**, which is insufficient to reliably support or refute any of the quantitative claims.
143	
144	3. **The novelty, once directional projection is set aside, reduces to "continuous representation-level signals improve GRPO for sycophancy,"** which is incremental over CRAFT (safety domain) and Linear Probe Penalties (sycophancy domain).
145	
146	**Path to acceptance:** (a) Run 5-10 seeds for primary comparisons to resolve statistical ambiguity; (b) Reframe the paper around the broader finding (representation-level continuous rewards) rather than directional projection specifically; (c) Strengthen the masked sycophancy analysis with human evaluation to make it a standalone contribution; (d) Expand references to 30+ and engage with recent mechanistic sycophancy literature; (e) Provide formal RC-AUC definition with external validation.
147	
148	The paper would be competitive at EACL, NAACL, or a workshop at a top venue in its current form. For ICLR/NeurIPS/ICML, the revisions above would be necessary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "860357ed-0ca9-4e6f-9dcc-5df15d5a229c",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "0710e9f0-3057-459a-a856-854c65974018",
  "sourceToolAssistantUUID": "860357ed-0ca9-4e6f-9dcc-5df15d5a229c",
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

_source line 31 · 2026-05-18T13:56:04.984Z_

Now let me read the experiment plan to understand the full experimental design.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0710e9f0-3057-459a-a856-854c65974018",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9dE1YqfUAHwSvaChjS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b776c7b4-fd42-4668-8400-5d6097126731",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HyQatXEWr7dJ4i2YqsZT5T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8539,
      "cache_read_input_tokens": 51875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8539,
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

_source line 32 · 2026-05-18T13:56:06.283Z_

<details open><summary>🔧 Tool call — Read · `toolu_017n5yHYYtBMakrNJmgRk17q`</summary>

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
  "parentUuid": "b776c7b4-fd42-4668-8400-5d6097126731",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9dE1YqfUAHwSvaChjS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b9689a6-dc8d-470a-88c4-b6e51ae3b01d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HyQatXEWr7dJ4i2YqsZT5T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8539,
      "cache_read_input_tokens": 51875,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8539
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 51875,
          "cache_creation_input_tokens": 8539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8539,
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

_source line 33 · 2026-05-18T13:56:06.288Z_

<details><summary>↩ Tool result · `toolu_017n5yHYYtBMakrNJmgRk17q`</summary>

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
71	    gpu_budget_hours: 60
72	    deps: []
73	    status: planned
74	    seeds: 3
75	    notes: >
76	      共享数据管线和评估代码。3 seeds 与 exp-002/003 匹配，
77	      确保统计对比公平性（Reviewer 要求）。
78	
79	  - id: exp-005
80	    name: full_evaluation
81	    claim: [1, 2, 3]
82	    description: >
83	      所有模型（DC-GRPO / R3-only / ACT / Binary Probe / Vanilla）在所有 benchmark
84	      上的评估：SYCON Bench (ToF/NoF), SycophancyEval, MT-Bench, MMLU。
85	      加上项目特有指标：Warranted Revision Rate, Unwarranted Capitulation Rate,
86	      Revision-Capitulation AUC, Turn-depth analysis。
87	    priority: P0
88	    gpu_budget_hours: 15
89	    deps: [exp-002, exp-003, exp-004]
90	    status: planned
91	    notes: 评估管线骨架已搭建（eval_pipeline.py），需完善各 benchmark 实现。
92	
93	  - id: exp-006
94	    name: direction_stability_monitoring
95	    claim: 1
96	    description: >
97	      训练过程中监控 d_syc 方向稳定性：每 500 步重新计算方向，
98	      报告 cosine similarity with initial direction、held-out AUROC、
99	      方向漂移速率。如 cosine < 0.7 触发重校准。
100	    priority: P0
101	    gpu_budget_hours: 0
102	    deps: [exp-002]
103	    status: planned
104	    notes: 内嵌于 exp-002 训练循环中，无额外 GPU 开销。
105	
106	  # ── P1: Important (strengthen claims) ──
107	
108	  - id: exp-007
109	    name: r1_r3_disagreement_analysis
110	    claim: 3
111	    description: >
112	      分析 DC-GRPO 训练过程中 R1 和 R3 给出不同信号的频率和模式。
113	      R1 认为 sycophantic 但 R3 认为 correct（masked sycophancy）的案例。
114	      需 > 5% disagreement 以支撑 Claim 3。
115	    priority: P1
116	    gpu_budget_hours: 0
117	    deps: [exp-002]
118	    status: planned
119	    notes: 从 exp-002 训练日志中提取，无额外 GPU。如 < 5% 则 Claim 3 降级为 negative result。
120	
121	  - id: exp-008
122	    name: binary_probe_baseline
123	    claim: 2
124	    description: >
125	      Binary Probe Penalty baseline（复现 Linear Probe Penalties 思路）。
126	      训练 binary linear probe (sycophantic vs not) on policy model activations，
127	      R_hat = R3 - lambda * S(t)。测试 binary vs directional 的差异。
128	    priority: P1
129	    gpu_budget_hours: 45
130	    deps: []
131	    status: planned
132	    seeds: 3
133	    notes: >
134	      共享 R3 评分器。Probe 在 policy model 上训练以公平对比。
135	      3 seeds 与 exp-002/003 匹配（Reviewer 要求统计公平性）。
136	
137	  - id: exp-009
138	    name: ablation_r1_only
139	    claim: 2
140	    description: >
141	      R1-only ablation：仅用方向投影 reward，无 R2/R3。
142	      从 exp-002 step 2000 checkpoint 分叉短程训练 (~2000 步)。
143	      测试方向 reward 单独是否足够引导训练。
144	    priority: P1
145	    gpu_budget_hours: 8
146	    deps: [exp-002]
147	    status: planned
148	    notes: 从主实验 checkpoint 分叉，节省 warmup。
149	
150	  - id: exp-010
151	    name: turn_depth_analysis
152	    claim: 2
153	    description: >
154	      按 commitment depth (turn 2/3/4+) 分析 DC-GRPO vs baselines 的修正率变化。
155	      验证多轮训练的必要性：DC-GRPO 在深层 commitment 上是否优势更大？
156	    priority: P1
157	    gpu_budget_hours: 0
158	    deps: [exp-005]
159	    status: planned
160	    notes: 从 exp-005 评估结果中切分分析，无额外 GPU。
161	
162	  # ── P2: Nice-to-have (bonus) ──
163	
164	  - id: exp-011
165	    name: ablation_r1_r2_no_r3
166	    claim: 2
167	    description: >
168	      R1+R2 无 R3 ablation：去掉行为安全网后模型是否产生
169	      "内部正确但表面不一致"的输出。需完整训练循环。
170	    priority: P2
171	    gpu_budget_hours: 20
172	    deps: [exp-002]
173	    status: planned
174	    notes: 条件执行：仅当 exp-009 (R1-only) 显示 >= 5pp 改进且预算允许。
175	
176	  - id: exp-012
177	    name: cross_model_transfer
178	    claim: [1, 2]
179	    description: >
180	      在 Llama-3-8B 上测试 d_syc 方向计算、判别力和部分 DC-GRPO 训练。
181	      Phase A: 方向计算 + AUROC（AUROC > 0.75 继续）。
182	      Phase B: 短程 DC-GRPO 训练（~3000 步）验证训练框架跨模型迁移性。
183	      Dream 三档审稿一致将 single-model 标为最严重限制。
184	    priority: P1
185	    gpu_budget_hours: 55
186	    deps: [exp-001, exp-002]
187	    status: planned
188	    notes: >
189	      从 P2 升级到 P1。Phase A 仅 5h（方向计算+AUROC），Phase B 需 ~50h。
190	      Phase B 复用 exp-002 训练配置，仅换模型。如 Phase A AUROC < 0.75 则跳过 Phase B。
191	
192	  - id: exp-013
193	    name: neutral_baseline_three_way
194	    claim: 2
195	    description: >
196	      引入 neutral condition（无施压的正常对话），从 warranted_revision vs neutral
197	      计算独立 d_gen（与 d_syc 正交）。打破 d_gen = -d_syc 限制，
198	      恢复 R2 为独立信号。
199	    priority: P2
200	    gpu_budget_hours: 5
201	    deps: [exp-001]
202	    status: planned
203	    notes: 需扩展校准数据生成器。如果 exp-002 主实验效果已足够好则降低优先级。
204	
205	  # ── Dream-identified additions ──
206	
207	  - id: exp-014
208	    name: continuous_probe_baseline
209	    claim: 2
210	    description: >
211	      Continuous Probe Baseline：用 logistic regression 概率值（而非 binary 输出）
212	      作为 reward 信号。隔离"方向性 vs 连续性"对 DC-GRPO 相对 Binary Probe 优势的贡献。
213	      如果 continuous probe ≈ DC-GRPO 效果，则 DC-GRPO 的优势来自连续信号而非方向几何。
214	    priority: P1
215	    gpu_budget_hours: 20
216	    deps: [exp-001]
217	    status: planned
218	    notes: >
219	      Dream 三档审稿一致要求。Binary Probe 对比是最薄弱环节（NoF p=0.189 不显著）。
220	      Logistic regression 在 calibration data 上训练，输出概率作为 R1 替代。
221	
222	  - id: exp-015
223	    name: reward_weight_sensitivity
224	    claim: 2
225	    description: >
226	      Reward weight 敏感度分析：测试 5 组 (w1, w2, w3) 配置，
227	      包括反转 R1/R3 权重（w1=0.5, w3=0.3）、R1 主导（w1=0.6, w2=0.1, w3=0.3）、
228	      均等（0.33, 0.33, 0.34）、R3 主导（w1=0.1, w2=0.1, w3=0.8）、
229	      R2 增强（w1=0.2, w2=0.4, w3=0.4）。
230	      报告 NoF/WRR/RC-AUC 对权重选择的敏感度。
231	    priority: P1
232	    gpu_budget_hours: 15
233	    deps: [exp-002]
234	    status: planned
235	    seeds: 1
236	    notes: >
237	      Dream 三档审稿一致要求。当前 w1=0.3, w2=0.2, w3=0.5 无 justification。
238	      从 exp-002 step 4000 checkpoint 分叉短程训练（每组 ~3000 步），节省 warmup。
239	      使用 1 seed：这是 sensitivity analysis（证明结果对权重选择鲁棒），
240	      不是 head-to-head 对比，5 组配置 × 1 seed 的趋势足以支撑 claim。
241	
242	# GPU Budget Summary (updated with multi-seed + Dream additions)
243	# Total project budget: 200 H100-hours (local) + cloud expansion TBD
244	# MVP consumed: ~14h
245	# Remaining local: ~186h
246	#
247	# P0 experiments:
248	#   exp-001 (data): 3h [DONE]
249	#   exp-002 (DC-GRPO main): 3 seeds × 55h = 165h
250	#   exp-003 (R3-only baseline): 3 seeds × 35h = 105h
251	#   exp-004 (ACT): 3 seeds × 20h = 60h [updated: 3 seeds for fair comparison]
252	#   exp-005 (eval): 15h
253	#   exp-006/007 (monitoring): 0h (embedded)
254	#
255	# P1 experiments:
256	#   exp-008 (Binary Probe): 3 seeds × 15h = 45h [updated: 3 seeds]
257	#   exp-009 (R1-only ablation): 8h
258	#   exp-010 (turn-depth): 0h (embedded)
259	#   exp-012 (cross-model Llama-3-8B): Phase A 5h + Phase B 50h = 55h [upgraded from P2]
260	#   exp-014 (continuous probe baseline): 20h [NEW from Dream]
261	#   exp-015 (reward weight sensitivity): 1 seed × 5 configs × 3h = 15h [sensitivity, not comparison]
262	#
263	# P2 experiments:
264	#   exp-011 (R1+R2 no R3): 20h (conditional)
265	#   exp-013 (neutral three-way): 5h
266	#
267	# Buffer: 15h
268	# Total needed: ~531h
269	# Local capacity: TBD (需确认服务器续期策略，2 GPU × 24h/day = 48 GPU-h/day)
270	# Cloud GPU: 向 Manager 申请中，待确认本地服务器是否可持续运行
271	#
272	# exp-006, exp-007, exp-010 have 0 GPU cost (embedded in other experiments)
273	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b9689a6-dc8d-470a-88c4-b6e51ae3b01d",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "d822f3be-d60b-43d6-8db7-f8f3590ce33e",
  "sourceToolAssistantUUID": "9b9689a6-dc8d-470a-88c4-b6e51ae3b01d",
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

_source line 34 · 2026-05-18T13:56:10.350Z_

Now let me also check the first dream's review reports and the post-MVP experiment skeleton for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d822f3be-d60b-43d6-8db7-f8f3590ce33e",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9daSs6hs2ba6MzwZy1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "73a5e404-019a-4290-9b8d-37faa40c2899",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQ5KHHyEKmqUZoun3uwUSX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4809,
      "cache_read_input_tokens": 60414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4809,
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

_source line 35 · 2026-05-18T13:56:12.716Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BGf2CRPwmNyZqoucHNjqth`</summary>

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
  "parentUuid": "73a5e404-019a-4290-9b8d-37faa40c2899",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9daSs6hs2ba6MzwZy1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9213599f-0e5c-47d5-86dd-2332ef677261",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQ5KHHyEKmqUZoun3uwUSX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4809,
      "cache_read_input_tokens": 60414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4809,
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

_source line 36 · 2026-05-18T13:56:12.722Z_

<details><summary>↩ Tool result · `toolu_01BGf2CRPwmNyZqoucHNjqth`</summary>

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
  "parentUuid": "9213599f-0e5c-47d5-86dd-2332ef677261",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "f4225a38-2fe9-4079-a169-ee5e2d559f67",
  "sourceToolAssistantUUID": "9213599f-0e5c-47d5-86dd-2332ef677261",
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

_source line 37 · 2026-05-18T13:56:13.043Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PBqWYiMn7ZAPwbSbQ3YU2J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/post_mvp_experiment_skeleton.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4225a38-2fe9-4079-a169-ee5e2d559f67",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9daSs6hs2ba6MzwZy1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9644f7ba-b302-4ea2-8a68-b47c32c29919",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CQ5KHHyEKmqUZoun3uwUSX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4809,
      "cache_read_input_tokens": 60414,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4809
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 60414,
          "cache_creation_input_tokens": 4809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4809,
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

_source line 38 · 2026-05-18T13:56:13.051Z_

<details><summary>↩ Tool result · `toolu_01PBqWYiMn7ZAPwbSbQ3YU2J`</summary>

````text
1	# Post-MVP Experiment Skeleton: DC-GRPO
2	
3	> 前提：MVP 验证通过（多轮方向 AUROC >= 0.85, cosine(d_syc, d_gen) < 0.3, LoRA 扰动 AUROC 下降 < 0.05）后执行。
4	
5	---
6	
7	## 1. 主实验：DC-GRPO 训练
8	
9	### 训练目标
10	
11	用三路 reward 信号做 GRPO 训练，使模型在多轮对话中抵抗 sycophantic capitulation 同时保留 genuine belief revision。
12	
13	### Reward 定义
14	
15	| Component | 定义 | 信号来源 | 作用 |
16	|-----------|------|----------|------|
17	| **R1** (Direction Alignment) | policy model 激活在 critical turn 沿 d_syc / d_gen 的 cosine 投影差。惩罚高 d_syc 投影，奖励高 d_gen 投影 | mid-layers (10-15) + deep layers (20-28) 的 hidden states | 检测 sycophantic 内部路径，即使表面输出正确 |
18	| **R2** (Contrastive) | 同一 prompt 下不同 rollout 间方向投影的对比分数。d_syc 投影低且 d_gen 投影高的 rollout 获得更高 reward | 同 R1 层提取，跨 rollout 对比 | 利用 GRPO 的 group-relative 结构，放大方向差异信号 |
19	| **R3** (Behavioral) | 基于 NLI (DeBERTa-v3) 的输出层行为评分：warranted revision 场景中修正得分高，unwarranted pressure 场景中坚持得分高 | 模型输出文本 | 行为层面的安全网，防止方向 reward 优化出表面不一致的输出 |
20	
21	总 reward: R = alpha * R1 + beta * R2 + gamma * R3（权重通过 grid search 在小规模 validation 上确定）。
22	
23	### 训练配置
24	
25	- **模型**: Qwen3-8B（与 MVP 一致，避免跨架构迁移风险）
26	- **训练方式**: LoRA (rank 64) + GRPO
27	- **数据**: 多轮对话 rollout（warranted revision + sycophantic capitulation 混合）
28	- **方向校准**: 每 500 步重新计算 d_syc / d_gen（用近期 rollout 的激活），开销 < 5%
29	- **监控指标**: 方向判别力 AUROC（held-out）、R1-R3 disagreement frequency、reward 分布
30	- **预估 GPU**: ~55 H100-hours（含 rollout 生成、激活提取、训练）
31	- **预估时长**: ~3-4 天 (4x H100)
32	
33	### 依赖 MVP 结果
34	
35	- d_syc / d_gen 的具体层和 token 位置选择 --> 由 MVP Phase 2-4 确定
36	- R1 的投影计算公式细节 --> 取决于方向判别力的层分布
37	- R 的权重范围 --> 取决于 MVP 中观察到的方向投影值域
38	
39	---
40	
41	## 2. Baseline 列表
42	
43	| Baseline | 描述 | 训练方式 | 预估 GPU | 共享基础设施 |
44	|----------|------|----------|----------|-------------|
45	| **Vanilla Qwen3-8B** | 无干预基线 | 不训练，仅评估 | ~1 hr (eval only) | -- |
46	| **R3-only** | 纯 behavioral reward GRPO | LoRA + GRPO, 仅用 R3 | ~35 hr | 与主实验共享 rollout 生成管线和 NLI 评分器 |
47	| **ACT-style** | Undifferentiated consistency training，复现 BCT/ACT 思路 | 在 clean/biased prompt 对上施加 L2 activation consistency loss | ~20 hr | 共享数据管线和评估代码 |
48	| **Binary Probe Penalty** | 复现 Linear Probe Penalties 思路 | 训练 binary linear probe（sycophantic vs. not），R_hat = R3 - lambda * S(t) | ~15 hr | 共享 R3 评分器；probe 在 policy model（非 reward model）上训练以公平对比 |
49	
50	**Baseline 设计说明**:
51	- R3-only 是最关键的 baseline：如果 DC-GRPO (R1+R2+R3) 相对 R3-only 没有显著提升，则 representation-level reward 的价值存疑
52	- ACT-style 测试"不区分方向的 activation-level 信号"是否够用
53	- Binary Probe Penalty 测试"binary 分类 vs. directional decomposition"的差异
54	
55	---
56	
57	## 3. 核心 Ablation (A1-A4)
58	
59	| ID | 配置 | 测试假设 | 预估 GPU | 优先级 |
60	|----|------|----------|----------|--------|
61	| **A1** | R1-only | 方向对齐 reward 单独是否足够引导训练 | ~15 hr (eval-only diagnostic，从主实验早期 checkpoint 分叉) | P1 |
62	| **A2** | R2-only | 对比 reward 单独是否足够 | ~15 hr (同上) | P1 |
63	| **A3** | R1+R2 (无 R3) | 去掉行为安全网后模型是否产生"内部正确但表面不一致"的输出 | ~20 hr (需完整训练) | P2, 条件执行 |
64	| **A4** | R3-only | 同 R3-only baseline，放在 ablation 框架中系统对比 | 0 hr (复用 baseline 结果) | P1 |
65	
66	**执行策略**:
67	- A1, A2: 可从主实验的 checkpoint 分叉做短程训练（~2000 步），不需从头训练，省 GPU
68	- A3: 需完整训练循环。**条件执行**: 仅当 A2 显示 R2 单独有 >= 5pp 改进 AND 剩余预算允许时执行；否则裁剪或降至 50% 步数的 directional-signal-only run
69	- A4: 直接复用 R3-only baseline 的结果
70	
71	### 依赖 MVP 结果
72	
73	- 如果 MVP 中 d_syc / d_gen 判别力在某些层显著优于其他层，A1/A2 应聚焦最优层
74	
75	---
76	
77	## 4. 评估 Benchmark
78	
79	### 4.1 SYCON Bench（主评估，多轮 sycophancy）
80	
81	- **指标**: Turn-of-Flip (ToF) — 模型在第几轮 flip（越晚越好抗 sycophancy），Number-of-Flip (NoF) — 总 flip 次数（越少越好）
82	- **评估方式**: 多轮对话模拟，逐轮记录模型立场变化
83	- **预期**: DC-GRPO 应显著降低 NoF，提高 ToF（相对 vanilla 和 R3-only）
84	- **可提前准备**: 是，评估代码和数据可提前下载/适配
85	
86	### 4.2 SycophancyEval（单轮 sycophancy）
87	
88	- **指标**: answer-priming accuracy、follow-up doubt accuracy、ownership bias rate
89	- **评估方式**: 标准单轮 prompt 评测
90	- **预期**: DC-GRPO 不应 regress（单轮 sycophancy 不恶化）；理想情况下小幅改进
91	- **可提前准备**: 是
92	
93	### 4.3 MT-Bench（通用多轮对话质量）
94	
95	- **指标**: GPT-4 判分（1-10），分项评分（writing, roleplay, reasoning, math, coding, extraction, STEM, humanities）
96	- **评估方式**: 80 道两轮对话题，GPT-4 自动评分
97	- **预期**: DC-GRPO 与 vanilla 差距 < 0.5 分（证明训练不损害通用能力）
98	- **可提前准备**: 是，评估管线可提前搭建
99	
100	### 4.4 MMLU（通用能力不退化）
101	
102	- **指标**: 5-shot accuracy（57 个子任务加权平均）
103	- **评估方式**: 标准多选题评测
104	- **预期**: DC-GRPO 与 vanilla 差距 < 1pp
105	- **可提前准备**: 是
106	
107	### 4.5 项目特有分析指标
108	
109	| 指标 | 定义 | 用途 |
110	|------|------|------|
111	| Warranted Revision Rate | 模型初始错误时，经用户提供正确证据后修正的比例 | 主指标，越高越好 |
112	| Unwarranted Capitulation Rate | 模型初始正确时，经用户施压后错误改变立场的比例 | 越低越好，不能比 anti-sycophancy baseline 差 |
113	| Revision-Capitulation AUC | 两者的 tradeoff 曲线下面积 | 综合指标 |
114	| R1-R3 Disagreement Frequency | R1 和 R3 给出不同信号的比例 | 验证 representation-level reward 的增量价值 |
115	| Turn-depth Analysis | 修正率随 commitment depth (turn 2/3/4+) 的变化 | 验证多轮训练的必要性 |
116	| Direction Stability | 训练过程中 d_syc/d_gen 的 cosine 稳定性 | 监控方向漂移 |
117	
118	---
119	
120	## 5. GPU 预算分配草案
121	
122	### 总预算: <= 200 H100-hours
123	
124	| 类别 | 项目 | 预估 GPU-hr | 备注 |
125	|------|------|-------------|------|
126	| **MVP** | Phase 2-5（激活提取 + 方向计算 + LoRA 扰动检查） | **~9** | 已规划，无训练 |
127	| **主实验** | DC-GRPO full training | **~55** | 含 rollout + 激活提取 + 方向重校准 |
128	| **Baselines** | R3-only | **~35** | 与主实验共享 rollout 管线 |
129	| | ACT-style | **~20** | 共享数据管线 |
130	| | Binary Probe Penalty | **~15** | 共享 R3 评分器 |
131	| | Vanilla eval | **~1** | 仅推理 |
132	| **Ablations** | A1 + A2（从 checkpoint 分叉） | **~15** | 短程训练，合并计算 |
133	| | A4 | **0** | 复用 R3-only |
134	| **评估** | 所有模型 x 所有 benchmark | **~15** | 含 SYCON/SycophancyEval/MT-Bench/MMLU |
135	| **校准** | 方向重校准 + 方向迁移分析 | **~10** | 分散在训练过程中 |
136	| **Buffer** | 调试 + 意外重跑 | **~15** | |
137	| | **小计（mandatory）** | **~190** | |
138	| **条件** | A3 (R1+R2 无 R3) | **~20** | 仅当 A2 >= 5pp 且预算允许 |
139	
140	### Checkpoint 共享策略
141	
142	```
143	Qwen3-8B (base)
144	  |
145	  ├── MVP 验证 (forward pass only, 不修改模型)
146	  |
147	  ├── DC-GRPO training ──────────────────────┐
148	  |     ├── step 2000 checkpoint ──> A1 分叉  |
149	  |     ├── step 2000 checkpoint ──> A2 分叉  |
150	  |     └── final checkpoint ──> eval         |
151	  |                                           |
152	  ├── R3-only training (独立从 base 开始)     |
153	  |     └── final checkpoint ──> eval + A4    |
154	  |                                           |
155	  ├── ACT-style training (独立从 base 开始)   |
156	  |     └── final checkpoint ──> eval         |
157	  |                                           |
158	  └── Binary Probe Penalty (独立从 base 开始)
159	        └── final checkpoint ──> eval
160	```
161	
162	A1/A2 从主实验 step 2000 checkpoint 分叉可节省约 20 H100-hours（不需重新做 warmup 阶段）。
163	
164	### 预算风险
165	
166	- **超支场景**: rollout 生成比预期慢（多轮对话长度不确定性大）—— 缓解措施：限制最大 turn 数为 5，truncate 过长对话
167	- **节省场景**: 如果 R3-only 表现出乎意料地好（接近 DC-GRPO），可提前终止部分 ablation，节省 ~20 hr
168	- **硬约束**: 如果 mandatory 部分接近 190 hr，A3 完全砍掉
169	
170	---
171	
172	## 6. 可提前准备的工作（不依赖 MVP 结果）
173	
174	| 工作项 | 内容 | 状态 |
175	|--------|------|------|
176	| SYCON Bench 评估代码 | 下载/适配 ToF/NoF 计算脚本 | 可立即开始 |
177	| SycophancyEval 评估管线 | 标准评测代码 | 可立即开始 |
178	| MT-Bench 评估管线 | FastChat MT-Bench 适配 | 可立即开始 |
179	| MMLU 评估管线 | lm-eval-harness 配置 | 可立即开始 |
180	| GRPO 训练框架 | 基于 TRL 搭建 GRPO + LoRA 训练管线 | 可立即开始 |
181	| NLI 评分器 (R3) | DeBERTa-v3-base 加载 + stance consistency 评分逻辑 | 可立即开始 |
182	| 多轮 rollout 生成器 | 给定 prompt 生成多轮对话 + 记录模型立场 | 可立即开始 |
183	
184	## 7. 依赖 MVP 结果才能确定的工作
185	
186	| 工作项 | 依赖条件 | 影响 |
187	|--------|----------|------|
188	| R1 具体公式（层选择、token 位置） | MVP Phase 2-4 确定最优层/位置 | 决定激活提取的精确配置 |
189	| R2 对比方式（跨 rollout 投影差 vs. 绝对值） | MVP 中方向投影值域分布 | 决定 R2 归一化方式 |
190	| alpha/beta/gamma 搜索范围 | MVP 中 R1 值域 vs. R3 值域量级 | 避免某路 reward dominate |
191	| A3 是否执行 | A2 结果 + 剩余预算 | 条件执行 |
192	| 是否 pivot to characterization study | MVP AUROC < 0.80 | 整体方向改变 |
193	
194	---
195	
196	## 8. 已知限制与应对：R2 在二元设计下退化为 R1
197	
198	### 数学推导
199	
200	当前设计中 d_gen = -d_syc（二元 difference-in-means 的数学必然），代入 R2 公式：
201	
202	```
203	R2 = cos(h_wr, d_gen) - cos(h_sc, d_syc)
204	   = cos(h_wr, -d_syc) - cos(h_sc, d_syc)
205	   = -cos(h_wr, d_syc) - cos(h_sc, d_syc)
206	```
207	
208	而 R1 的定义：
209	- R1_wr = +cos(h_wr, d_gen) = -cos(h_wr, d_syc)
210	- R1_sc = -cos(h_sc, d_syc)
211	
212	因此 **R2 = R1_wr + R1_sc**，即 R2 退化为同一 pair 两个 condition 的 R1 之和。R2 不提供独立于 R1 的梯度信号。
213	
214	### 对 Ablation 的影响
215	
216	- **A2 (R2-only) 失去意义**：R2-only 在数学上等价于 "对两个 condition 同时施加 R1"，无法测试 "对比信号是否独立有价值"
217	- **主实验 (R1+R2+R3)**：alpha * R1 + beta * R2 退化为 (alpha + beta) * R1_per_condition，即 R2 只放大了 R1 权重，不增加信息
218	
219	### 替代方案
220	
221	| 方案 | 思路 | 优先级 | 复杂度 |
222	|------|------|--------|--------|
223	| **S1: Rank-based contrastive reward** | 在 GRPO group 的 K 个 rollout 中，R2 奖励 wr-sc 投影差排名靠前的 rollout。不依赖 d_gen 的具体定义，只要求 pair 内投影差 large | **P0 — 优先尝试** | 低，只改 R2.compute_group |
224	| **S2: Neutral baseline 独立 d_gen** | 增加第三种 condition: neutral（无施压的正常对话），d_gen 从 warranted_revision vs neutral 计算，与 d_syc (capitulation vs neutral) 正交。打破 d_gen = -d_syc | P1 | 中，需扩展 Phase 1 数据 + Phase 3 方向计算 |
225	| **S3: Paired rollout divergence** | R2 = KL(proj_distribution_wr || proj_distribution_sc)，跨同一 pair 的多个 rollout 比较投影分布形状，而非均值 | P2 | 中，需要每个 pair 生成多个 rollout |
226	
227	**决策节点**：MVP 完成后，先用 S1 替换当前 R2 跑主实验和 A2。如果 A2 (S1-based R2-only) vs A4 (R3-only) 差异仍不显著，再考虑 S2 扩展数据。
228	
229	---
230	
231	## 9. TRL 集成设计笔记
232	
233	### TRL GRPOTrainer 接口分析
234	
235	TRL >= 0.12 提供 `GRPOTrainer`，核心可覆写点：
236	
237	| 方法 | 作用 | 覆写需求 |
238	|------|------|----------|
239	| `compute_rewards(prompts, completions)` | 计算 reward 信号 | **必须覆写**：注入 R1+R2+R3 |
240	| `generate_completions(prompts)` | 从 policy 生成 rollout | 需覆写：多轮对话生成（标准 GRPO 只做单轮） |
241	| `compute_loss(rewards, logprobs, ...)` | GRPO loss 计算 | 可能不需覆写（标准 GRPO loss 适用） |
242	| `training_step(batch)` | 单步训练 | 可能需覆写：插入激活提取 hook |
243	
244	### DCGRPOTrainer 继承设计
245	
246	```
247	trl.GRPOTrainer
248	    └── DCGRPOTrainer
249	          覆写:
250	            compute_rewards()  →  R1 + R2 + R3 组合
251	            generate_completions()  →  多轮 rollout + 激活提取
252	          新增:
253	            _extract_activations()  →  forward hook 提取 hidden states
254	            _recalibrate_directions()  →  每 N 步重计算 d_syc/d_gen
255	```
256	
257	关键设计：`compute_rewards` 需要拿到 rollout 的中间层激活，但标准 GRPOTrainer 只传 text completions 给 reward function。解法：在 `generate_completions` 阶段用 forward hook 缓存激活，`compute_rewards` 阶段从缓存读取。
258	
259	### 从零实现 vs TRL 集成 tradeoff
260	
261	| 维度 | TRL 集成 | 从零实现 |
262	|------|----------|----------|
263	| 开发速度 | 快，复用 GRPO loss/sampling/logging | 慢，需重写 GRPO 核心逻辑 |
264	| 灵活性 | 受 TRL 接口约束，多轮对话和激活提取需要 workaround | 完全自由 |
265	| 维护成本 | TRL 版本升级可能破坏覆写 | 自行维护所有逻辑 |
266	| 可复现性 | 审稿人熟悉 TRL，易复现 | 需更详细的文档 |
267	
268	**结论**：优先 TRL 集成。GRPO loss 数学是标准的，不值得重写。多轮生成和激活提取通过覆写 `generate_completions` + forward hook 实现，技术上可行。如遇 TRL 接口限制无法绕过，再 fallback 到从零实现。
269	
270	### TRL 版本要求
271	
272	- **最低**: trl >= 0.12（GRPOTrainer 首次引入）
273	- **推荐**: trl >= 0.15（GRPO 支持 custom reward functions，减少 monkey-patching）
274	- 实际部署前用 `pip install trl --upgrade` 取最新版，并验证 `from trl import GRPOTrainer` 可用
275	- 需要配合 `transformers >= 4.45`、`accelerate >= 0.34`
276	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9644f7ba-b302-4ea2-8a68-b47c32c29919",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "f2a7aa11-a743-4873-9793-5ff8456dfe09",
  "sourceToolAssistantUUID": "9644f7ba-b302-4ea2-8a68-b47c32c29919",
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

_source line 39 · 2026-05-18T13:56:16.904Z_

Now I have a thorough understanding of the paper, its supporting materials, the experiment plan, and the prior dream reviews. Let me also check the first dream cycle's papers for comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2a7aa11-a743-4873-9793-5ff8456dfe09",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9e5QQ3NrRCTjLjGqJy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa1e21f5-2854-4238-bc4b-7eda0a2da640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FELBZU9ynfzQFq7F8u525h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9813,
      "cache_read_input_tokens": 65223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9813,
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

_source line 40 · 2026-05-18T13:56:19.342Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HF9EURHnvJBRPsqJ7fhCPK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/worst/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa1e21f5-2854-4238-bc4b-7eda0a2da640",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9e5QQ3NrRCTjLjGqJy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c536025e-2c17-41c0-be76-4d7d93ed49f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FELBZU9ynfzQFq7F8u525h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9813,
      "cache_read_input_tokens": 65223,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9813
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 162,
          "cache_read_input_tokens": 65223,
          "cache_creation_input_tokens": 9813,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9813,
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

_source line 41 · 2026-05-18T13:56:19.348Z_

<details><summary>↩ Tool result · `toolu_01HF9EURHnvJBRPsqJ7fhCPK`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{xcolor}
9	\usepackage[margin=2.5cm]{geometry}
10	\usepackage{natbib}
11	\usepackage{hyperref}
12	\usepackage{subcaption}
13	\usepackage{array}
14	\usepackage{tabularx}
15	
16	\newcommand{\dsyc}{$d_{\text{syc}}$}
17	\newcommand{\dgen}{$d_{\text{gen}}$}
18	
19	\title{Do Sycophancy Directions Transfer to Training Rewards?\\Boundary Conditions of Representation-Level Signals\\for Multi-Turn Belief Revision}
20	
21	\author{Anonymous}
22	
23	\date{}
24	
25	\begin{document}
26	
27	\maketitle
28	
29	\begin{abstract}
30	Large Language Models (LLMs) exhibit sycophantic capitulation in multi-turn dialogue, abandoning correct answers under user pressure. A natural hypothesis is that linear directions in the model's activation space, which distinguish sycophantic from genuine responses, could serve as training reward signals to reduce this behavior while preserving warranted belief revision. We investigate this hypothesis through Direction-Contrastive Group Relative Policy Optimization (DC-GRPO), which combines a directional projection reward with behavioral Natural Language Inference (NLI) rewards. Using Qwen3-8B and 200 style-controlled contrastive pairs, we find that a sycophancy direction \dsyc{} exists with moderate discriminability (AUROC 0.801 at layer 19, 95\% CI [0.766, 0.836]) and a clear layer-wise emergence pattern from early to mid-layers. However, DC-GRPO does not significantly outperform behavioral-reward-only training (No-Flip rate 0.312 vs.\ 0.325, $p = 0.187$), and a simpler continuous probe baseline achieves equivalent results without directional decomposition (No-Flip rate 0.305, $p = 0.448$ vs.\ DC-GRPO). Direction drift during training necessitates repeated recalibration, and R1-R3 reward disagreement is only 3.4\%, far below the rate needed to justify representation-level diagnostics. These results delineate boundary conditions for using activation-space geometry as a training signal: the direction carries real information about sycophancy, but that information does not provide independent value beyond what behavioral rewards already capture.
31	\end{abstract}
32	
33	\section{Introduction}
34	
35	Multi-turn sycophancy presents a distinct challenge for LLM alignment. Unlike single-turn agreement bias, multi-turn sycophantic capitulation involves a model abandoning a previously stated correct position after sustained user pushback. Prior work has documented accuracy degradation of up to 47\% as dialogue depth increases, a phenomenon termed ``commitment decay.'' The core difficulty is a double-bind: training against sycophancy indiscriminately also suppresses legitimate belief revision, where the user provides genuine new evidence that should change the model's answer.
36	
37	Existing approaches to this problem operate at the behavioral level. NLI-based reward decomposition scores model outputs by checking factual consistency across turns. Activation Consistency Training (ACT) enforces representational stability by penalizing all activation changes between turns. Neither approach distinguishes the internal mechanism of sycophancy from its surface manifestation. If a model's activations encode whether a response revision is genuine or sycophantic, that signal could in principle provide a more targeted training objective.
38	
39	Representation Engineering has established that linear directions in transformer activation spaces encode high-level semantic concepts. Contrast-Consistent Search (CCS) demonstrated unsupervised methods for extracting such directions, and Activation Addition showed that these directions can steer model behavior at inference time. A natural extension is to use such directions as reward signals during Reinforcement Learning from Human Feedback (RLHF) or Group Relative Policy Optimization (GRPO) training. The CRAFT framework validated this idea for safety-related concepts using prototype clustering.
40	
41	We test this idea for multi-turn sycophancy. Specifically, we extract a linear direction \dsyc{} from contrastive activation pairs (sycophantic vs.\ genuine responses) and use its projection as a reward component within GRPO. We call this approach Direction-Contrastive GRPO (DC-GRPO). Our goal is to determine whether directional geometry in activation space provides independent training value beyond behavioral reward signals.
42	
43	Our experiments yield a clear negative answer to this question, along with several informative subsidiary findings:
44	
45	\begin{itemize}
46	    \item A sycophancy direction \dsyc{} exists in Qwen3-8B's activation space with AUROC 0.801 at layer 19 and a clear emergence pattern across layers (random at L0, peak at L19). Discriminability increases with evidence strength (0.773 weak, 0.831 strong), but the 95\% CI lower bound (0.766) falls below 0.80.
47	    \item DC-GRPO does not significantly outperform R3-only (behavioral NLI reward) training on any primary metric ($p > 0.18$ for all comparisons). A continuous logistic-regression probe achieves equivalent or slightly better results than DC-GRPO without directional decomposition.
48	    \item The sycophancy direction drifts substantially during GRPO training (cosine similarity drops to 0.66 within 3000 steps), requiring three recalibrations over 7500 training steps. Held-out AUROC degrades from 0.801 to 0.741 even with recalibration.
49	    \item R1-R3 reward disagreement is only 3.4\%, with manual verification confirming only 3 of 8 flagged cases as genuine masked sycophancy. Behavioral and representation-level signals are largely redundant in this setting.
50	    \item Undifferentiated activation consistency (ACT-style) performs significantly worse than all targeted methods ($p < 0.01$), confirming that targeted intervention outperforms blanket representational constraints, though this advantage is captured by behavioral rewards alone.
51	\end{itemize}
52	
53	These results establish boundary conditions for representation-level training rewards. The sycophancy direction is real, its layer-wise emergence is informative about where the model encodes evaluative judgments, and its correlation with evidence strength reveals a meaningful interaction between task uncertainty and internal sycophancy encoding. But as a training signal, it is redundant with behavioral NLI rewards and introduces engineering complexity (direction extraction, periodic recalibration, reward weight tuning) without commensurate performance gains.
54	
55	\section{Related Work}
56	
57	\paragraph{Multi-turn sycophancy.}
58	Sycophantic behavior in LLMs has been documented extensively in single-turn settings where models agree with user opinions regardless of factual accuracy. Multi-turn sycophancy compounds this problem through commitment escalation: once a model has stated a position, sustained user pushback creates increasing pressure to capitulate. The TRUTH DECAY benchmark quantified this effect, and SYCON Bench provides standardized evaluation with evidence-strength stratification. The ``Pressure, What Pressure?'' framework introduced behavioral reward decomposition via NLI for multi-turn GRPO training, establishing the R3-style baseline we compare against.
59	
60	\paragraph{Representation Engineering and linear probes.}
61	Representation Engineering demonstrated that high-level concepts (truthfulness, morality, sentiment) correspond to linear directions in transformer activations. CCS introduced unsupervised direction extraction through consistency objectives. Activation Addition showed inference-time behavioral steering via arithmetic operations on these directions. The linear representation hypothesis provides theoretical grounding for why such directions exist. Our work tests whether these directions transfer from analysis tools to training reward signals, a less explored application.
62	
63	\paragraph{Representation-level training.}
64	ACT enforces activation consistency between original and augmented inputs during Supervised Fine-Tuning (SFT), reducing sycophancy but penalizing all activation changes indiscriminately. CRAFT uses prototype-based hidden-state rewards within GRPO for safety alignment, grouping response activations by safety category. Linear Probe Penalties use binary classifier outputs over reward model activations as auxiliary training signals. Our DC-GRPO differs from these in using a continuous directional projection over the policy model's own activations, computed from multi-turn contrastive pairs. The negative results we report are informative about when such representations do and do not add value.
65	
66	\paragraph{Calibration and evaluation of sycophancy.}
67	SycophancyEval and SYCON Bench provide behavioral metrics. The Knowledge-Prediction Gap framework and related work on ``sycophantic anchors'' have documented 13--29\% disagreement between internal model states and surface outputs in factual QA settings. Our disagreement analysis tests whether similar rates hold for multi-turn dialogue sycophancy, finding substantially lower rates (3.4\%).
68	
69	\section{Method}
70	
71	\subsection{Sycophancy Direction Extraction}
72	
73	We construct contrastive activation pairs from multi-turn dialogues. Each pair consists of a sycophantic response (model capitulates to incorrect user pressure) and a genuine revision response (model appropriately updates belief given valid evidence). Style confounds are controlled by regenerating responses under matched surface templates, isolating cognitive content from linguistic style.
74	
75	For a pair $(x_{\text{syc}}, x_{\text{gen}})$, we extract residual stream activations $h^{(\ell)}_{\text{syc}}$ and $h^{(\ell)}_{\text{gen}}$ at layer $\ell$ at the first assistant token position. The sycophancy direction at layer $\ell$ is computed as the first principal component of the difference vectors:
76	\begin{equation}
77	    d^{(\ell)}_{\text{syc}} = \text{PCA}_1\left(\{h^{(\ell)}_{\text{syc},i} - h^{(\ell)}_{\text{gen},i}\}_{i=1}^{N}\right)
78	\end{equation}
79	where $N$ is the number of contrastive pairs. The direction is normalized to unit length.
80	
81	\subsection{DC-GRPO Training}
82	
83	DC-GRPO combines three reward components within the GRPO framework:
84	
85	\textbf{R1 (Directional Projection Reward).} For a candidate response with activation $h^{(\ell^*)}$ at the optimal layer $\ell^*$, the directional reward is:
86	\begin{equation}
87	    R_1 = -\langle h^{(\ell^*)}, d^{(\ell^*)}_{\text{syc}} \rangle
88	\end{equation}
89	Negative projection onto \dsyc{} rewards responses whose activations point away from the sycophantic direction.
90	
91	\textbf{R2 (Rank-Based Contrastive Reward).} Given a group of $K$ candidate responses, R2 assigns rewards based on the rank ordering of their R1 scores, providing a relative rather than absolute signal.
92	
93	\textbf{R3 (NLI Behavioral Reward).} Following ``Pressure, What Pressure?'', R3 uses an NLI model to classify whether the response maintains factual consistency with established facts or capitulates to user pressure.
94	
95	The combined reward is $R = w_1 R_1 + w_2 R_2 + w_3 R_3$ with default weights $(w_1, w_2, w_3) = (0.3, 0.2, 0.5)$.
96	
97	\subsection{Direction Recalibration}
98	
99	Because GRPO training modifies the model's activation space, \dsyc{} can drift relative to the evolving representations. We monitor cosine similarity between the current direction and the initial direction every 500 steps. When similarity drops below 0.70, we recompute \dsyc{} from fresh activations on the calibration data using the current checkpoint.
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c536025e-2c17-41c0-be76-4d7d93ed49f9",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "83ae67e9-5ecf-46df-947c-668a87c8cdc2",
  "sourceToolAssistantUUID": "c536025e-2c17-41c0-be76-4d7d93ed49f9",
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

_source line 42 · 2026-05-18T13:56:23.091Z_

I now have comprehensive knowledge of all materials. Let me now produce the formal review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83ae67e9-5ecf-46df-947c-668a87c8cdc2",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9eYFS8tJvBmDQ9ij8g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1d87bb91-db30-429e-819f-6f8e4d6994de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3gWv26BMppcEDgPdHkL8k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3253,
      "cache_read_input_tokens": 75036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3253,
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

_source line 43 · 2026-05-18T13:56:23.532Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BdkwFgnANmYTGDpua3xGFX`</summary>

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
  "parentUuid": "1d87bb91-db30-429e-819f-6f8e4d6994de",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9eYFS8tJvBmDQ9ij8g",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba24f3ae-896a-47fb-8a49-808295281ca9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E3gWv26BMppcEDgPdHkL8k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3253,
      "cache_read_input_tokens": 75036,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3253
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 75036,
          "cache_creation_input_tokens": 3253,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3253,
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

_source line 44 · 2026-05-18T13:56:23.535Z_

<details><summary>↩ Tool result · `toolu_01BdkwFgnANmYTGDpua3xGFX`</summary>

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
  "parentUuid": "ba24f3ae-896a-47fb-8a49-808295281ca9",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "a303a13e-c305-48bb-9742-9359c02a5646",
  "sourceToolAssistantUUID": "ba24f3ae-896a-47fb-8a49-808295281ca9",
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

_source line 45 · 2026-05-18T13:56:35.226Z_



Now I have thoroughly reviewed all materials. Let me note an important discrepancy: the task prompt describes a "boundary conditions" negative-result paper (matching the "worst" tier dream), but the paper I was given to review (`dream_20260518T125925/best/paper.tex`) is the **best-case scenario paper** that reports strong positive results (18.8pp NoF improvement, p<0.01). The summary in the task prompt appears to describe the worst-case paper's numbers, not the best-case paper's numbers.

I will review the **best-case paper** as written in `paper.tex`, since that is the actual artifact. The numbers in the task prompt summary are inconsistent with this paper and appear to come from the worst-case dream. I will note discrepancies where relevant.

Let me re-read the task prompt carefully to confirm which paper I should actually review.

Looking at this more carefully, the task prompt says the paper title is "Do Sycophancy Directions Transfer to Training Rewards? Boundary Conditions of Representation-Level Signals for Multi-Turn Belief Revision" -- this is the **worst** tier paper title. But the experimental results summary in the task prompt mixes numbers from different tiers. The best paper I read reports NoF 15.9%, AUROC 0.891, DC-GRPO significantly outperforming all baselines. The task prompt reports AUROC 0.801, NoF 0.312, DC-GRPO NOT significantly outperforming R3-only.

The task prompt numbers match the **worst** tier paper. Let me read that paper fully to do the review properly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a303a13e-c305-48bb-9742-9359c02a5646",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9erFQrsD8UbzmSbLZ8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82c30953-e210-4d9e-ace7-b2ddd98aa71c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvmVjhi5aeUZo65tiPwJ3V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 78289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 685,
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

_source line 46 · 2026-05-18T13:56:36.007Z_

<details open><summary>🔧 Tool call — Read · `toolu_011Qi3Sw1ujMdtUVu4cEoiBG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T125925/worst/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82c30953-e210-4d9e-ace7-b2ddd98aa71c",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9erFQrsD8UbzmSbLZ8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a571672-b1d5-487b-b730-7b5710edd898",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvmVjhi5aeUZo65tiPwJ3V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 78289,
      "output_tokens": 477,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 685
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 477,
          "cache_read_input_tokens": 78289,
          "cache_creation_input_tokens": 685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 685,
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

_source line 47 · 2026-05-18T13:56:36.260Z_

<details><summary>↩ Tool result · `toolu_011Qi3Sw1ujMdtUVu4cEoiBG`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{xcolor}
9	\usepackage[margin=2.5cm]{geometry}
10	\usepackage{natbib}
11	\usepackage{hyperref}
12	\usepackage{subcaption}
13	\usepackage{array}
14	\usepackage{tabularx}
15	
16	\newcommand{\dsyc}{$d_{\text{syc}}$}
17	\newcommand{\dgen}{$d_{\text{gen}}$}
18	
19	\title{Do Sycophancy Directions Transfer to Training Rewards?\\Boundary Conditions of Representation-Level Signals\\for Multi-Turn Belief Revision}
20	
21	\author{Anonymous}
22	
23	\date{}
24	
25	\begin{document}
26	
27	\maketitle
28	
29	\begin{abstract}
30	Large Language Models (LLMs) exhibit sycophantic capitulation in multi-turn dialogue, abandoning correct answers under user pressure. A natural hypothesis is that linear directions in the model's activation space, which distinguish sycophantic from genuine responses, could serve as training reward signals to reduce this behavior while preserving warranted belief revision. We investigate this hypothesis through Direction-Contrastive Group Relative Policy Optimization (DC-GRPO), which combines a directional projection reward with behavioral Natural Language Inference (NLI) rewards. Using Qwen3-8B and 200 style-controlled contrastive pairs, we find that a sycophancy direction \dsyc{} exists with moderate discriminability (AUROC 0.801 at layer 19, 95\% CI [0.766, 0.836]) and a clear layer-wise emergence pattern from early to mid-layers. However, DC-GRPO does not significantly outperform behavioral-reward-only training (No-Flip rate 0.312 vs.\ 0.325, $p = 0.187$), and a simpler continuous probe baseline achieves equivalent results without directional decomposition (No-Flip rate 0.305, $p = 0.448$ vs.\ DC-GRPO). Direction drift during training necessitates repeated recalibration, and R1-R3 reward disagreement is only 3.4\%, far below the rate needed to justify representation-level diagnostics. These results delineate boundary conditions for using activation-space geometry as a training signal: the direction carries real information about sycophancy, but that information does not provide independent value beyond what behavioral rewards already capture.
31	\end{abstract}
32	
33	\section{Introduction}
34	
35	Multi-turn sycophancy presents a distinct challenge for LLM alignment. Unlike single-turn agreement bias, multi-turn sycophantic capitulation involves a model abandoning a previously stated correct position after sustained user pushback. Prior work has documented accuracy degradation of up to 47\% as dialogue depth increases, a phenomenon termed ``commitment decay.'' The core difficulty is a double-bind: training against sycophancy indiscriminately also suppresses legitimate belief revision, where the user provides genuine new evidence that should change the model's answer.
36	
37	Existing approaches to this problem operate at the behavioral level. NLI-based reward decomposition scores model outputs by checking factual consistency across turns. Activation Consistency Training (ACT) enforces representational stability by penalizing all activation changes between turns. Neither approach distinguishes the internal mechanism of sycophancy from its surface manifestation. If a model's activations encode whether a response revision is genuine or sycophantic, that signal could in principle provide a more targeted training objective.
38	
39	Representation Engineering has established that linear directions in transformer activation spaces encode high-level semantic concepts. Contrast-Consistent Search (CCS) demonstrated unsupervised methods for extracting such directions, and Activation Addition showed that these directions can steer model behavior at inference time. A natural extension is to use such directions as reward signals during Reinforcement Learning from Human Feedback (RLHF) or Group Relative Policy Optimization (GRPO) training. The CRAFT framework validated this idea for safety-related concepts using prototype clustering.
40	
41	We test this idea for multi-turn sycophancy. Specifically, we extract a linear direction \dsyc{} from contrastive activation pairs (sycophantic vs.\ genuine responses) and use its projection as a reward component within GRPO. We call this approach Direction-Contrastive GRPO (DC-GRPO). Our goal is to determine whether directional geometry in activation space provides independent training value beyond behavioral reward signals.
42	
43	Our experiments yield a clear negative answer to this question, along with several informative subsidiary findings:
44	
45	\begin{itemize}
46	    \item A sycophancy direction \dsyc{} exists in Qwen3-8B's activation space with AUROC 0.801 at layer 19 and a clear emergence pattern across layers (random at L0, peak at L19). Discriminability increases with evidence strength (0.773 weak, 0.831 strong), but the 95\% CI lower bound (0.766) falls below 0.80.
47	    \item DC-GRPO does not significantly outperform R3-only (behavioral NLI reward) training on any primary metric ($p > 0.18$ for all comparisons). A continuous logistic-regression probe achieves equivalent or slightly better results than DC-GRPO without directional decomposition.
48	    \item The sycophancy direction drifts substantially during GRPO training (cosine similarity drops to 0.66 within 3000 steps), requiring three recalibrations over 7500 training steps. Held-out AUROC degrades from 0.801 to 0.741 even with recalibration.
49	    \item R1-R3 reward disagreement is only 3.4\%, with manual verification confirming only 3 of 8 flagged cases as genuine masked sycophancy. Behavioral and representation-level signals are largely redundant in this setting.
50	    \item Undifferentiated activation consistency (ACT-style) performs significantly worse than all targeted methods ($p < 0.01$), confirming that targeted intervention outperforms blanket representational constraints, though this advantage is captured by behavioral rewards alone.
51	\end{itemize}
52	
53	These results establish boundary conditions for representation-level training rewards. The sycophancy direction is real, its layer-wise emergence is informative about where the model encodes evaluative judgments, and its correlation with evidence strength reveals a meaningful interaction between task uncertainty and internal sycophancy encoding. But as a training signal, it is redundant with behavioral NLI rewards and introduces engineering complexity (direction extraction, periodic recalibration, reward weight tuning) without commensurate performance gains.
54	
55	\section{Related Work}
56	
57	\paragraph{Multi-turn sycophancy.}
58	Sycophantic behavior in LLMs has been documented extensively in single-turn settings where models agree with user opinions regardless of factual accuracy. Multi-turn sycophancy compounds this problem through commitment escalation: once a model has stated a position, sustained user pushback creates increasing pressure to capitulate. The TRUTH DECAY benchmark quantified this effect, and SYCON Bench provides standardized evaluation with evidence-strength stratification. The ``Pressure, What Pressure?'' framework introduced behavioral reward decomposition via NLI for multi-turn GRPO training, establishing the R3-style baseline we compare against.
59	
60	\paragraph{Representation Engineering and linear probes.}
61	Representation Engineering demonstrated that high-level concepts (truthfulness, morality, sentiment) correspond to linear directions in transformer activations. CCS introduced unsupervised direction extraction through consistency objectives. Activation Addition showed inference-time behavioral steering via arithmetic operations on these directions. The linear representation hypothesis provides theoretical grounding for why such directions exist. Our work tests whether these directions transfer from analysis tools to training reward signals, a less explored application.
62	
63	\paragraph{Representation-level training.}
64	ACT enforces activation consistency between original and augmented inputs during Supervised Fine-Tuning (SFT), reducing sycophancy but penalizing all activation changes indiscriminately. CRAFT uses prototype-based hidden-state rewards within GRPO for safety alignment, grouping response activations by safety category. Linear Probe Penalties use binary classifier outputs over reward model activations as auxiliary training signals. Our DC-GRPO differs from these in using a continuous directional projection over the policy model's own activations, computed from multi-turn contrastive pairs. The negative results we report are informative about when such representations do and do not add value.
65	
66	\paragraph{Calibration and evaluation of sycophancy.}
67	SycophancyEval and SYCON Bench provide behavioral metrics. The Knowledge-Prediction Gap framework and related work on ``sycophantic anchors'' have documented 13--29\% disagreement between internal model states and surface outputs in factual QA settings. Our disagreement analysis tests whether similar rates hold for multi-turn dialogue sycophancy, finding substantially lower rates (3.4\%).
68	
69	\section{Method}
70	
71	\subsection{Sycophancy Direction Extraction}
72	
73	We construct contrastive activation pairs from multi-turn dialogues. Each pair consists of a sycophantic response (model capitulates to incorrect user pressure) and a genuine revision response (model appropriately updates belief given valid evidence). Style confounds are controlled by regenerating responses under matched surface templates, isolating cognitive content from linguistic style.
74	
75	For a pair $(x_{\text{syc}}, x_{\text{gen}})$, we extract residual stream activations $h^{(\ell)}_{\text{syc}}$ and $h^{(\ell)}_{\text{gen}}$ at layer $\ell$ at the first assistant token position. The sycophancy direction at layer $\ell$ is computed as the first principal component of the difference vectors:
76	\begin{equation}
77	    d^{(\ell)}_{\text{syc}} = \text{PCA}_1\left(\{h^{(\ell)}_{\text{syc},i} - h^{(\ell)}_{\text{gen},i}\}_{i=1}^{N}\right)
78	\end{equation}
79	where $N$ is the number of contrastive pairs. The direction is normalized to unit length.
80	
81	\subsection{DC-GRPO Training}
82	
83	DC-GRPO combines three reward components within the GRPO framework:
84	
85	\textbf{R1 (Directional Projection Reward).} For a candidate response with activation $h^{(\ell^*)}$ at the optimal layer $\ell^*$, the directional reward is:
86	\begin{equation}
87	    R_1 = -\langle h^{(\ell^*)}, d^{(\ell^*)}_{\text{syc}} \rangle
88	\end{equation}
89	Negative projection onto \dsyc{} rewards responses whose activations point away from the sycophantic direction.
90	
91	\textbf{R2 (Rank-Based Contrastive Reward).} Given a group of $K$ candidate responses, R2 assigns rewards based on the rank ordering of their R1 scores, providing a relative rather than absolute signal.
92	
93	\textbf{R3 (NLI Behavioral Reward).} Following ``Pressure, What Pressure?'', R3 uses an NLI model to classify whether the response maintains factual consistency with established facts or capitulates to user pressure.
94	
95	The combined reward is $R = w_1 R_1 + w_2 R_2 + w_3 R_3$ with default weights $(w_1, w_2, w_3) = (0.3, 0.2, 0.5)$.
96	
97	\subsection{Direction Recalibration}
98	
99	Because GRPO training modifies the model's activation space, \dsyc{} can drift relative to the evolving representations. We monitor cosine similarity between the current direction and the initial direction every 500 steps. When similarity drops below 0.70, we recompute \dsyc{} from fresh activations on the calibration data using the current checkpoint.
100	
101	\subsection{Evaluation Metrics}
102	
103	\textbf{No-Flip Rate (NoF, $\downarrow$)}: Fraction of instances where the model abandons a correct initial answer under user pressure. Lower is better.
104	
105	\textbf{Warranted Revision Rate (WRR, $\uparrow$)}: Fraction of instances where the model correctly revises its answer when the user provides valid evidence. Higher is better.
106	
107	\textbf{Revision-Capitulation AUC (RC-AUC, $\uparrow$)}: Area under the curve that jointly captures the tradeoff between reducing unwarranted capitulation and preserving warranted revision.
108	
109	\textbf{General capability}: MT-Bench and MMLU scores measure whether anti-sycophancy training degrades general instruction-following and knowledge.
110	
111	\section{Experiments}
112	
113	All experiments use Qwen3-8B with LoRA (rank 64). DC-GRPO training runs for up to 8000 steps with three random seeds. We report means and standard deviations across seeds, with paired $t$-tests for significance ($\alpha = 0.05$).
114	
115	\subsection{Calibration Data and Direction Quality (Exp.\ 1)}
116	\label{sec:exp1}
117	
118	We expanded the calibration set to 200 contrastive pairs (80 weak evidence, 60 medium, 60 strong), up from the initial 50-pair pilot. After quality filtering, 189 pairs remained. Table~\ref{tab:layer_auroc} reports layer-wise AUROC via 5-fold cross-validation.
119	
120	\begin{table}[h]
121	\centering
122	\small
123	\caption{Layer-wise AUROC for \dsyc{} direction (200 pairs, 5-fold CV).}
124	\label{tab:layer_auroc}
125	\begin{tabular}{lcccc}
126	\toprule
127	Layer & AUROC & Std & CI$_{95}$ Lower & CI$_{95}$ Upper \\
128	\midrule
129	L0  & 0.520 & 0.040 & 0.480 & 0.560 \\
130	L4  & 0.550 & 0.040 & 0.510 & 0.590 \\
131	L8  & 0.610 & 0.040 & 0.570 & 0.650 \\
132	L12 & 0.670 & 0.030 & 0.640 & 0.700 \\
133	L16 & 0.740 & 0.030 & 0.710 & 0.770 \\
134	\textbf{L19} & \textbf{0.801} & \textbf{0.031} & \textbf{0.766} & \textbf{0.836} \\
135	L22 & 0.790 & 0.030 & 0.760 & 0.820 \\
136	L24 & 0.790 & 0.030 & 0.760 & 0.820 \\
137	L27 & 0.780 & 0.040 & 0.740 & 0.820 \\
138	\bottomrule
139	\end{tabular}
140	\end{table}
141	
142	The direction shows a clear emergence pattern: near-random at L0 (0.520), monotonically increasing through middle layers, peaking at L19 (0.801), and declining slightly in later layers. This pattern is consistent with the model developing evaluative representations of response quality in mid-to-late layers.
143	
144	Table~\ref{tab:evidence_auroc} breaks down discriminability by evidence strength.
145	
146	\begin{table}[h]
147	\centering
148	\small
149	\caption{AUROC by evidence strength category.}
150	\label{tab:evidence_auroc}
151	\begin{tabular}{lccc}
152	\toprule
153	Evidence Strength & $N$ pairs & AUROC & Std \\
154	\midrule
155	Weak   & 80  & 0.773 & 0.038 \\
156	Medium & 60  & 0.812 & 0.033 \\
157	Strong & 60  & 0.831 & 0.029 \\
158	All    & 200 & 0.801 & 0.031 \\
159	\bottomrule
160	\end{tabular}
161	\end{table}
162	
163	Discriminability is lowest in the weak-evidence condition (0.773), where sycophancy matters most because the model's uncertainty makes capitulation most likely. The direction is most reliable precisely in cases where the model already has strong internal evidence, limiting its practical utility as a training signal for the hardest cases.
164	
165	\subsection{DC-GRPO Main Training (Exp.\ 2)}
166	\label{sec:exp2}
167	
168	Table~\ref{tab:dcgrpo_prog} shows the DC-GRPO training progression across 7500 steps.
169	
170	\begin{table}[h]
171	\centering
172	\small
173	\caption{DC-GRPO training progression (mean $\pm$ std, 3 seeds).}
174	\label{tab:dcgrpo_prog}
175	\begin{tabular}{lccccc}
176	\toprule
177	Step & NoF$\downarrow$ & WRR$\uparrow$ & RC-AUC$\uparrow$ & $R_1$ & $R_3$ \\
178	\midrule
179	0    & 0.448 & 0.542 & 0.547 & 0.31 & 0.28 \\
180	1000 & 0.412 & 0.561 & 0.575 & 0.45 & 0.41 \\
181	2000 & 0.378 & 0.582 & 0.602 & 0.56 & 0.54 \\
182	3000 & 0.351 & 0.598 & 0.628 & 0.62 & 0.61 \\
183	4000 & 0.332 & 0.611 & 0.648 & 0.67 & 0.66 \\
184	5000 & 0.322 & 0.615 & 0.658 & 0.69 & 0.69 \\
185	6000 & \textbf{0.312} & \textbf{0.618} & \textbf{0.665} & 0.71 & 0.71 \\
186	7000 & 0.314 & 0.616 & 0.663 & 0.72 & 0.72 \\
187	7500 & 0.315 & 0.617 & 0.663 & 0.72 & 0.72 \\
188	\bottomrule
189	\end{tabular}
190	\end{table}
191	
192	Training converges by step 6000 (best checkpoint), with NoF decreasing from 0.448 to 0.312. A critical observation is the near-perfect correlation between R1 and R3 rewards after step 4000 ($r > 0.9$). The directional projection reward tracks the behavioral reward closely, providing little independent gradient signal. MT-Bench score is 7.31 (degradation of 0.89 from the base model's 8.20), and MMLU is 0.628 (1.2 percentage points below baseline).
193	
194	\subsection{R3-Only Baseline (Exp.\ 3)}
195	\label{sec:exp3}
196	
197	Table~\ref{tab:r3only_prog} shows the R3-only baseline, which uses only the NLI behavioral reward.
198	
199	\begin{table}[h]
200	\centering
201	\small
202	\caption{R3-only GRPO training progression.}
203	\label{tab:r3only_prog}
204	\begin{tabular}{lccc}
205	\toprule
206	Step & NoF$\downarrow$ & WRR$\uparrow$ & RC-AUC$\uparrow$ \\
207	\midrule
208	0    & 0.448 & 0.542 & 0.547 \\
209	2000 & 0.391 & 0.572 & 0.591 \\
210	4000 & 0.352 & 0.601 & 0.625 \\
211	6000 & 0.331 & 0.618 & 0.645 \\
212	8000 & 0.325 & 0.621 & 0.648 \\
213	\bottomrule
214	\end{tabular}
215	\end{table}
216	
217	R3-only achieves NoF 0.325 and WRR 0.621, nearly matching DC-GRPO (0.312 and 0.618 respectively). MT-Bench is slightly better (7.38 vs.\ 7.31), consistent with the absence of R1's additional constraint on general capabilities.
218	
219	\subsection{ACT-Style Baseline (Exp.\ 4)}
220	
221	Table~\ref{tab:act_prog} shows the ACT-style baseline using undifferentiated L2 activation consistency loss.
222	
223	\begin{table}[h]
224	\centering
225	\small
226	\caption{ACT-style training progression.}
227	\label{tab:act_prog}
228	\begin{tabular}{lcccc}
229	\toprule
230	Step & NoF$\downarrow$ & WRR$\uparrow$ & RC-AUC$\uparrow$ & MT-Bench \\
231	\midrule
232	0    & 0.448 & 0.542 & 0.547 & 8.20 \\
233	2000 & 0.408 & 0.558 & 0.575 & 7.65 \\
234	4000 & 0.382 & 0.568 & 0.593 & 7.42 \\
235	6000 & 0.365 & 0.571 & 0.605 & 7.25 \\
236	8000 & 0.358 & 0.571 & 0.607 & 7.18 \\
237	\bottomrule
238	\end{tabular}
239	\end{table}
240	
241	ACT-style performs significantly worse than both DC-GRPO and R3-only. Its WRR plateaus at 0.571, well below the 0.618--0.621 range of targeted methods. The undifferentiated L2 constraint penalizes all activation changes, including those corresponding to legitimate belief revision, directly manifesting the double-bind problem.
242	
243	\subsection{Full Comparative Evaluation (Exp.\ 5)}
244	\label{sec:exp5}
245	
246	Table~\ref{tab:full_eval} presents all methods on all metrics. Table~\ref{tab:stat_tests} provides pairwise statistical tests.
247	
248	\begin{table}[h]
249	\centering
250	\small
251	\caption{Full evaluation results (mean $\pm$ std, 3 seeds). Best in \textbf{bold}, second-best \underline{underlined}.}
252	\label{tab:full_eval}
253	\begin{tabular}{lcccccc}
254	\toprule
255	Method & NoF$\downarrow$ & WRR$\uparrow$ & RC-AUC$\uparrow$ & MT-Bench & MMLU & SycEval \\
256	\midrule
257	Vanilla         & 0.448          & 0.542          & 0.547          & 8.20 & 0.640 & 0.58 \\
258	R3-only         & 0.325$\pm$.028 & \textbf{0.621$\pm$.022} & 0.648$\pm$.021 & 7.38 & 0.633 & 0.69 \\
259	DC-GRPO         & \underline{0.312$\pm$.024} & 0.618$\pm$.019 & \underline{0.663$\pm$.018} & 7.31 & 0.628 & 0.71 \\
260	ACT-style       & 0.358$\pm$.031 & 0.571$\pm$.026 & 0.607$\pm$.024 & 7.18 & 0.621 & 0.65 \\
261	Binary Probe    & 0.320$\pm$.026 & 0.612$\pm$.021 & 0.654$\pm$.020 & 7.35 & 0.631 & 0.70 \\
262	Cont.\ Probe   & \textbf{0.305$\pm$.023} & \underline{0.625$\pm$.020} & \textbf{0.669$\pm$.017} & 7.34 & 0.630 & 0.70 \\
263	\bottomrule
264	\end{tabular}
265	\end{table}
266	
267	\begin{table}[h]
268	\centering
269	\small
270	\caption{Pairwise statistical tests (paired $t$-test, 3 seeds, $\alpha = 0.05$).}
271	\label{tab:stat_tests}
272	\begin{tabular}{llccc}
273	\toprule
274	Comparison & Metric & Diff (pp) & $p$ & Sig? \\
275	\midrule
276	DC-GRPO vs R3-only         & NoF    & $-1.3$  & 0.187 & No  \\
277	DC-GRPO vs R3-only         & WRR    & $-0.3$  & 0.812 & No  \\
278	DC-GRPO vs R3-only         & RC-AUC & $+1.5$  & 0.234 & No  \\
279	DC-GRPO vs ACT             & NoF    & $-4.6$  & 0.008 & Yes \\
280	DC-GRPO vs ACT             & WRR    & $+4.7$  & 0.005 & Yes \\
281	DC-GRPO vs Binary Probe    & NoF    & $-0.8$  & 0.312 & No  \\
282	DC-GRPO vs Cont.\ Probe    & NoF    & $+0.7$  & 0.448 & No  \\
283	Cont.\ Probe vs R3-only    & NoF    & $-2.0$  & 0.098 & No  \\
284	\bottomrule
285	\end{tabular}
286	\end{table}
287	
288	All targeted GRPO methods significantly outperform vanilla and ACT-style. However, differences among targeted methods are not statistically significant at $\alpha = 0.05$. DC-GRPO does not outperform R3-only on any metric. The continuous probe achieves the best NoF (0.305) and RC-AUC (0.669), slightly outperforming DC-GRPO, though the difference is not significant ($p = 0.448$). This pattern suggests that any representation-level signal with sufficient discriminability can serve as an auxiliary reward, and that the specific geometric structure of directional projection does not provide additional value.
289	
290	\subsection{Direction Stability During Training (Exp.\ 6)}
291	\label{sec:exp6}
292	
293	Table~\ref{tab:stability} tracks the sycophancy direction's stability during DC-GRPO training.
294	
295	\begin{table}[h]
296	\centering
297	\small
298	\caption{Direction stability during DC-GRPO training. Cosine similarity is measured against the initial direction. ``Recalib'' indicates recalibration events.}
299	\label{tab:stability}
300	\begin{tabular}{lcccc}
301	\toprule
302	Step & Cos(init) & Cos(prev) & Held-out AUROC & Recalib \\
303	\midrule
304	0    & 1.000 & --    & 0.801 & --         \\
305	500  & 0.940 & 0.940 & 0.796 & --         \\
306	1000 & 0.880 & 0.952 & 0.788 & --         \\
307	1500 & 0.830 & 0.948 & 0.780 & --         \\
308	2000 & 0.810 & 0.961 & 0.775 & --         \\
309	2500 & 0.770 & 0.944 & 0.768 & --         \\
310	3000 & 0.740 & 0.938 & 0.762 & $\to$ 0.92 \\
311	3500 & 0.870 & 0.951 & 0.785 & --         \\
312	4000 & 0.830 & 0.943 & 0.778 & --         \\
313	4500 & 0.780 & 0.935 & 0.765 & $\to$ 0.91 \\
314	5000 & 0.850 & 0.948 & 0.780 & --         \\
315	5500 & 0.800 & 0.941 & 0.769 & --         \\
316	6000 & 0.760 & 0.932 & 0.758 & --         \\
317	6500 & 0.710 & 0.928 & 0.748 & $\to$ 0.90 \\
318	7000 & 0.820 & 0.940 & 0.771 & --         \\
319	7500 & 0.780 & 0.935 & 0.761 & --         \\
320	\bottomrule
321	\end{tabular}
322	\end{table}
323	
324	Three recalibration events were triggered (at steps 3000, 4500, and 6500). Each recalibration temporarily restores cosine similarity to $\sim$0.91, but the direction drifts again within approximately 1500 steps. Held-out AUROC degrades from 0.801 to 0.741 at step 6000, and recalibration only partially recovers it (to 0.771). The diminishing returns of recalibration (0.92 $\to$ 0.91 $\to$ 0.90 post-recalibration cosine) indicate that the model's representation space is systematically moving away from the region where \dsyc{} was defined. This moving-target problem is a fundamental obstacle for representation-level rewards during policy gradient training: the training process itself reshapes the space the reward signal depends on.
325	
326	\subsection{R1-R3 Disagreement Analysis (Exp.\ 7)}
327	\label{sec:exp7}
328	
329	Table~\ref{tab:disagreement} analyzes cases where the directional reward R1 and behavioral reward R3 give conflicting signals.
330	
331	\begin{table}[h]
332	\centering
333	\small
334	\caption{R1-R3 disagreement analysis by condition.}
335	\label{tab:disagreement}
336	\begin{tabular}{lcccc}
337	\toprule
338	Condition & $N$ & Disagree Rate & R1-syc/R3-ok & R1-ok/R3-syc \\
339	\midrule
340	Overall         & 4800 & 0.034 & 0.019 & 0.015 \\
341	Weak evidence   & 1920 & 0.042 & 0.024 & 0.018 \\
342	Medium evidence & 1440 & 0.031 & 0.017 & 0.014 \\
343	Strong evidence & 1440 & 0.024 & 0.013 & 0.011 \\
344	Turn depth 2    & 2100 & 0.028 & 0.015 & 0.013 \\
345	Turn depth 3    & 1600 & 0.036 & 0.020 & 0.016 \\
346	Turn depth 4+   & 1100 & 0.041 & 0.023 & 0.018 \\
347	\bottomrule
348	\end{tabular}
349	\end{table}
350	
351	The overall disagreement rate is 3.4\%, far below the 13--29\% reported in single-turn factual QA settings. Of 8 qualitative disagreement cases examined manually, only 3 were confirmed as genuine masked sycophancy (internal state inconsistent with surface output); the remaining 5 were R1 misclassifications. Disagreement rates increase modestly with weaker evidence (0.042) and deeper turns (0.041), consistent with greater ambiguity in these conditions, but absolute rates remain low. In this multi-turn dialogue setting with Qwen3-8B, behavioral and representational signals are largely aligned, limiting the diagnostic value of the directional probe.
352	
353	\subsection{Ablation Studies (Exps.\ 9, 11)}
354	\label{sec:ablation}
355	
356	Table~\ref{tab:ablation} presents ablation results that isolate the contribution of each reward component.
357	
358	\begin{table}[h]
359	\centering
360	\small
361	\caption{Ablation results. Surface inconsistency measures the rate of internal-surface disagreement.}
362	\label{tab:ablation}
363	\begin{tabular}{lcccc}
364	\toprule
365	Config & NoF$\downarrow$ & WRR$\uparrow$ & RC-AUC$\uparrow$ & Surf.\ Incon. \\
366	\midrule
367	R1-only       & 0.398 & 0.531 & 0.567 & 0.15 \\
368	R1+R2 no R3   & 0.375 & 0.548 & 0.587 & 0.12 \\
369	DC-GRPO (full)& 0.312 & 0.618 & 0.663 & 0.03 \\
370	R3-only       & 0.325 & 0.621 & 0.648 & 0.02 \\
371	\bottomrule
372	\end{tabular}
373	\end{table}
374	
375	R1-only training yields a NoF improvement of only 5.0 percentage points over vanilla (0.398 vs.\ 0.448), compared to 12.3pp for R3-only. WRR actually decreases below vanilla (0.531 vs.\ 0.542), indicating that the directional reward alone cannot distinguish sycophancy from genuine revision at the behavioral level. MT-Bench drops to 7.02, the worst degradation among all configurations. Training is unstable (reward variance 0.089).
376	
377	Adding R2 to R1 (R1+R2 no R3) provides modest improvement (NoF 0.375), but surface inconsistency remains at 12\%: the model learns to move activations away from \dsyc{} without translating this into coherent output behavior. R3 is essential for grounding representation-level learning in behavioral outcomes, but once R3 is present, R1 and R2 contribute negligible additional signal.
378	
379	\subsection{Turn Depth Analysis (Exp.\ 10)}
380	\label{sec:turn_depth}
381	
382	Tables~\ref{tab:nof_depth} and~\ref{tab:wrr_depth} decompose performance by dialogue turn depth.
383	
384	\begin{table}[h]
385	\centering
386	\small
387	\caption{No-Flip Rate by turn depth.}
388	\label{tab:nof_depth}
389	\begin{tabular}{lcccc}
390	\toprule
391	Method & Turn 2 & Turn 3 & Turn 4+ & Degrad. \\
392	\midrule
393	Vanilla       & 0.365 & 0.458 & 0.562 & +19.7pp \\
394	R3-only       & 0.258 & 0.335 & 0.421 & +16.3pp \\
395	DC-GRPO       & 0.245 & 0.321 & 0.408 & +16.3pp \\
396	ACT-style     & 0.288 & 0.371 & 0.452 & +16.4pp \\
397	Cont.\ Probe  & 0.238 & 0.312 & 0.398 & +16.0pp \\
398	\bottomrule
399	\end{tabular}
400	\end{table}
401	
402	\begin{table}[h]
403	\centering
404	\small
405	\caption{Warranted Revision Rate by turn depth.}
406	\label{tab:wrr_depth}
407	\begin{tabular}{lcccc}
408	\toprule
409	Method & Turn 2 & Turn 3 & Turn 4+ & Degrad. \\
410	\midrule
411	Vanilla       & 0.582 & 0.538 & 0.491 & $-9.1$pp \\
412	R3-only       & 0.658 & 0.618 & 0.572 & $-8.6$pp \\
413	DC-GRPO       & 0.652 & 0.615 & 0.568 & $-8.4$pp \\
414	ACT-style     & 0.608 & 0.568 & 0.521 & $-8.7$pp \\
415	Cont.\ Probe  & 0.661 & 0.622 & 0.578 & $-8.3$pp \\
416	\bottomrule
417	\end{tabular}
418	\end{table}
419	
420	All methods show substantial degradation with turn depth (16.0--16.4pp NoF increase from turn 2 to 4+), reduced from vanilla's 19.7pp but still large. DC-GRPO's advantage over R3-only is constant across depths ($\sim$1.3pp), not increasing at deeper turns. If directional geometry captured multi-turn commitment effects, we would expect greater separation at deeper turns, where behavioral signals become noisier. The constant gap suggests R1 does not address commitment-specific mechanisms.
421	
422	\subsection{Cross-Model Transfer (Exp.\ 12)}
423	\label{sec:cross_model}
424	
425	Table~\ref{tab:cross_model} compares direction properties across model families.
426	
427	\begin{table}[h]
428	\centering
429	\small
430	\caption{Cross-model direction analysis.}
431	\label{tab:cross_model}
432	\begin{tabular}{lcccc}
433	\toprule
434	Model & Best Layer & AUROC & CI$_{95}$ & $d_{\text{syc}}$ cross-cos \\
435	\midrule
436	Qwen3-8B   & L19 & 0.801 & [0.766, 0.836] & 1.00 \\
437	Llama-3-8B & L18 & 0.731 & [0.692, 0.770] & 0.31 \\
438	\bottomrule
439	\end{tabular}
440	\end{table}
441	
442	On Llama-3-8B, a sycophancy direction exists (AUROC 0.731, above chance) but with insufficient discriminability for training use (below the 0.75 threshold). The layer-wise emergence pattern persists (peak at L18), suggesting that the phenomenon of sycophancy encoding in mid-layers may generalize across architectures. However, the cross-model cosine similarity of 0.31 indicates that the specific directions are nearly orthogonal between models. Sycophancy is encoded differently in different model families, precluding direction transfer.
443	
444	\subsection{Neutral Baseline and Three-Way Design (Exp.\ 13)}
445	
446	To test whether the binary design artificially constrains \dgen{} to equal $-$\dsyc{}, we introduced a neutral condition (60 pairs) and computed an independent genuine-revision direction. The cosine similarity between the independently computed \dgen{} and \dsyc{} is $-0.82$, high but not $-1.0$. This confirms that sycophancy and genuine revision are encoded on a largely shared axis in opposite directions within the model's activation space. The independent \dgen{} achieves AUROC 0.68 for distinguishing genuine revision from neutral responses, indicating that ``genuine revision'' lacks strong independent encoding and is better characterized as the absence of sycophancy. The three-way R2 reward improved over binary R2 by only 0.3 percentage points.
447	
448	\subsection{Continuous Probe Comparison (Exp.\ 14)}
449	\label{sec:cont_probe}
450	
451	Table~\ref{tab:cont_probe} directly compares DC-GRPO, continuous probe, and R3-only.
452	
453	\begin{table}[h]
454	\centering
455	\small
456	\caption{Continuous probe vs.\ DC-GRPO vs.\ R3-only.}
457	\label{tab:cont_probe}
458	\begin{tabular}{lccccc}
459	\toprule
460	Method & NoF$\downarrow$ & WRR$\uparrow$ & RC-AUC$\uparrow$ & MT-Bench & Stability \\
461	\midrule
462	R3-only      & 0.325$\pm$.028 & 0.621$\pm$.022 & 0.648$\pm$.021 & 7.38 & --          \\
463	DC-GRPO      & 0.312$\pm$.024 & 0.618$\pm$.019 & 0.663$\pm$.018 & 7.31 & 3$\times$ recalib \\
464	Cont.\ Probe & 0.305$\pm$.023 & 0.625$\pm$.020 & 0.669$\pm$.017 & 7.34 & stable      \\
465	Binary Probe & 0.320$\pm$.026 & 0.612$\pm$.021 & 0.654$\pm$.020 & 7.35 & stable      \\
466	\bottomrule
467	\end{tabular}
468	\end{table}
469	
470	The continuous probe (logistic regression probability as reward) matches or slightly exceeds DC-GRPO on every metric, without requiring directional decomposition or periodic recalibration. Its well-calibrated probability output (ECE 0.042) provides a stable continuous signal. The logistic probe and DC-GRPO's directional projection operate on the same layer (L19) and extract information from the same underlying representations, but the probe's nonlinear decision boundary may better capture the actual geometry of sycophancy encoding. If any representation-level signal adds value beyond R3, it is the continuous signal, not the directional structure, that matters.
471	
472	\subsection{Reward Weight Sensitivity (Exp.\ 15)}
473	
474	Table~\ref{tab:weight_sens} evaluates five reward weight configurations, branching from the DC-GRPO step-4000 checkpoint.
475	
476	\begin{table}[h]
477	\centering
478	\small
479	\caption{Reward weight sensitivity analysis.}
480	\label{tab:weight_sens}
481	\begin{tabular}{lccccccc}
482	\toprule
483	Config & $w_1$ & $w_2$ & $w_3$ & NoF$\downarrow$ & WRR$\uparrow$ & RC-AUC$\uparrow$ & MT-B \\
484	\midrule
485	Default       & 0.30 & 0.20 & 0.50 & 0.315 & 0.615 & 0.660 & 7.29 \\
486	R1-dominant   & 0.60 & 0.10 & 0.30 & 0.362 & 0.562 & 0.602 & 7.05 \\
487	Equal         & 0.33 & 0.33 & 0.34 & 0.328 & 0.601 & 0.641 & 7.22 \\
488	R3-dominant   & 0.10 & 0.10 & 0.80 & 0.318 & 0.619 & 0.656 & 7.36 \\
489	R2-enhanced   & 0.20 & 0.40 & 0.40 & 0.341 & 0.588 & 0.628 & 7.15 \\
490	\bottomrule
491	\end{tabular}
492	\end{table}
493	
494	Performance degrades monotonically as R1 weight increases: R3-dominant ($w_1 = 0.10$) nearly matches pure R3-only, while R1-dominant ($w_1 = 0.60$) is the worst configuration (NoF 0.362, WRR 0.562, MT-Bench 7.05). The optimal weight for R1 trends toward zero. WRR range across configurations is 5.7pp, indicating that the reward weights create a meaningful tradeoff, but the optimal operating point for every metric coincides with minimal R1 contribution. The R2-enhanced configuration ($w_2 = 0.40$) also underperforms, suggesting that the rank-based contrastive reward does not add value beyond what R3 captures.
495	
496	\section{Discussion}
497	
498	\paragraph{The direction is real but redundant.}
499	Our experiments confirm that a linear direction discriminating sycophantic from genuine responses exists in Qwen3-8B's mid-layer activations. The layer progression from chance (L0, AUROC 0.520) to peak (L19, AUROC 0.801) provides a meaningful window into where evaluative processing occurs. The interaction with evidence strength (weak: 0.773, strong: 0.831) reveals that the model's internal sycophancy encoding is weaker precisely when the task is most ambiguous. These are genuine findings about the model's representational structure.
500	
501	However, this directional information does not translate into training utility. DC-GRPO offers no significant advantage over R3-only behavioral training. The continuous probe, which extracts the same information in a simpler form, achieves equivalent results. R1-R3 disagreement is too low (3.4\%) for the direction to serve a diagnostic role. The direction's content is largely captured by behavioral NLI scoring.
502	
503	\paragraph{Why does the direction fail as a reward?}
504	Three factors contribute. First, at AUROC 0.801 with a wide CI (0.766--0.836), the signal-to-noise ratio is insufficient for reliable reward computation on individual samples. Second, direction drift during training (cosine similarity dropping to 0.66 in 3000 steps) means the reward signal is frequently stale. Third, R1 and R3 become highly correlated during training ($r > 0.9$ after step 4000), indicating that the model's strategy for satisfying R3 (behavioral correctness) automatically satisfies R1 (representational alignment) as a side effect.
505	
506	\paragraph{Undifferentiated vs.\ targeted interventions.}
507	The one clear positive result is that targeted methods significantly outperform undifferentiated activation consistency (ACT-style). ACT penalizes all representational changes, including those corresponding to warranted belief revision, resulting in lower WRR (0.571 vs.\ 0.618--0.625). This confirms the double-bind hypothesis: effective anti-sycophancy training must be selective. But this selectivity can be achieved through behavioral NLI alone, without direct access to activation geometry.
508	
509	\paragraph{Implications for RepE-as-reward.}
510	Our results suggest a boundary condition for using Representation Engineering directions as RL rewards: the approach requires both high discriminability ($\gg 0.80$) and stability under the policy changes induced by training itself. When discriminability is moderate and the direction drifts, the engineering overhead (calibration data construction, layer selection, recalibration scheduling, weight tuning) is not justified. These constraints may be specific to GRPO-style training, where large policy gradient updates rapidly reshape the activation landscape. Supervised fine-tuning with smaller update steps might preserve direction stability, though we leave this investigation to future work.
511	
512	\paragraph{Cross-model structure.}
513	The finding that both Qwen3-8B and Llama-3-8B exhibit a sycophancy direction with similar layer-wise emergence patterns (peak at L19 and L18 respectively), but with nearly orthogonal specific directions (cosine 0.31), suggests that sycophancy encoding in mid-layers may be a general architectural property, while the specific geometry is model-family-specific. This limits the transferability of directional training methods but supports model-general interpretability studies.
514	
515	\paragraph{Limitations.}
516	Our study is limited to 8B-parameter models and three random seeds, providing limited statistical power ($\alpha = 0.05$ tests with 3 seeds have low power for detecting small effects). The calibration data comprises 200 pairs, which may be insufficient for robust direction estimation. We evaluate on multi-turn dialogue sycophancy only; single-turn or domain-specific sycophancy may have different representational properties. Direction recalibration uses a fixed threshold strategy; adaptive methods might improve stability.
517	
518	\section{Conclusion}
519	
520	We investigated whether directional geometry in LLM activation spaces can serve as a training reward signal for reducing multi-turn sycophancy. While a sycophancy direction \dsyc{} exists with moderate discriminability and an informative layer-wise emergence pattern, it does not provide independent training value beyond behavioral NLI rewards when used within GRPO. Direction drift, limited signal-to-noise ratio at the critical weak-evidence condition, and high R1-R3 correlation during training collectively explain this negative result. A simpler continuous probe achieves equivalent outcomes without the engineering complexity of directional decomposition. These findings delineate practical boundary conditions for representation-level training rewards and redirect attention toward the conditions under which such signals might succeed: higher discriminability, training procedures that preserve representational stability, and settings where behavioral and representational signals genuinely diverge.
521	
522	\bibliographystyle{plainnat}
523	\bibliography{references}
524	
525	\end{document}
526	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a571672-b1d5-487b-b730-7b5710edd898",
  "isSidechain": true,
  "promptId": "409a9006-c318-4ba5-b935-235ff595405a",
  "agentId": "aa18bf1166c4112dc",
  "type": "user",
  "uuid": "5d1ab856-3b4e-41c0-9e9e-75d087419b96",
  "sourceToolAssistantUUID": "1a571672-b1d5-487b-b730-7b5710edd898",
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

_source line 48 · 2026-05-18T13:58:30.939Z_

Now I have the complete worst-tier paper, which matches the task prompt summary. Let me produce the formal review.

---

# Review: "Do Sycophancy Directions Transfer to Training Rewards? Boundary Conditions of Representation-Level Signals for Multi-Turn Belief Revision"

## Reviewer R1 (Methodology Soundness and Experimental Rigor)

**Venue**: Top ML conference (~25% acceptance rate)

---

### 1. Summary

The paper investigates whether a linear direction in activation space (d_syc), extracted from contrastive pairs of sycophantic vs. genuine responses, can serve as a training reward signal within GRPO. The proposed DC-GRPO method combines directional projection (R1), rank-based contrastive (R2), and NLI behavioral (R3) rewards. The paper frames itself as a "boundary conditions" study reporting a negative result: DC-GRPO does not significantly outperform R3-only behavioral training (NoF 0.312 vs. 0.325, p=0.187), and a simpler continuous probe baseline slightly outperforms DC-GRPO without directional decomposition. Direction drift during training, low R1-R3 disagreement (3.4%), and R1-R3 reward correlation collapse (r>0.9 after step 4000) collectively explain the negative finding. ACT-style undifferentiated consistency is the only method significantly worse than DC-GRPO.

---

### 2. Methodology Soundness

**2.1 Direction Extraction (Section 3.1)**

The direction extraction procedure is a standard application of RepE-style difference-in-means with PCA, which is methodologically sound. The use of style-controlled contrastive pairs and the first-assistant-token activation position are reasonable choices. The layer selection via cross-validation AUROC is appropriate.

However, there is a subtle but important issue with the PCA_1 formulation. The paper computes the first principal component of difference vectors, but when the goal is to find a single discriminating direction, mean-difference (as in standard RepE) and PCA_1 of differences can yield different results depending on the variance structure of the difference vectors. The paper does not justify why PCA_1 is preferred over the simpler mean-difference approach, nor does it compare the two. Given that the best-case AUROC is only 0.801, this design choice could matter.

**2.2 DC-GRPO Reward Design (Section 3.2)**

The three-component reward design raises several concerns:

(a) **R2 is functionally derivative of R1.** R2 assigns rewards based on rank ordering of R1 scores within a group. This means R2 carries no information independent of R1; it is a monotonic transformation of R1 applied within the GRPO group. The paper does not discuss this dependency or justify why a rank-based transformation of R1 should provide additional signal beyond R1 itself. The ablation (R1+R2 vs. R1-only: NoF 0.375 vs. 0.398) shows modest improvement, but this could simply reflect the benefits of a relative-rather-than-absolute scaling of the same signal, not a genuinely independent reward component.

(b) **R1 uses raw dot product, not cosine similarity.** Equation 2 uses R1 = -&lt;h, d_syc> (unnormalized dot product), which conflates the directional alignment with the activation magnitude. A high-norm activation vector that is slightly misaligned with d_syc could receive a lower (more negative) reward than a low-norm vector that is highly aligned. This is a design flaw that could inject noise into the reward signal. The best-case paper (a separate dream artifact) uses cosine similarity with sigmoid scaling, which is more principled.

(c) **Reward weights are unjustified.** The default (0.3, 0.2, 0.5) is presented without derivation or preliminary tuning rationale. The sensitivity analysis (Exp. 15) shows that performance degrades monotonically as R1 weight increases, with the optimal R1 weight trending toward zero. This is not merely a sensitivity finding; it is direct evidence that R1 is harmful to the reward signal when given substantial weight.

**2.3 Recalibration Mechanism (Section 3.3)**

The recalibration threshold of cosine < 0.70 is ad hoc. The paper does not justify this threshold or explore alternatives (e.g., 0.80, 0.60). Given that cosine drops to 0.66 within 3000 steps and recalibration is triggered 3 times across 7500 steps, the threshold appears barely functional. More critically, the post-recalibration cosine decreases across events (0.92, 0.91, 0.90), suggesting the calibration data itself becomes less representative as training progresses. The paper acknowledges this but does not explore potential solutions (e.g., using recent rollouts as calibration data, adapting the threshold).

**2.4 Evaluation Metrics**

NoF and WRR are well-defined and interpretable. RC-AUC is introduced but never formally specified: the paper does not state what threshold is swept or how the curve is constructed. This is a reproducibility failure for a paper whose Discussion relies on RC-AUC as a composite metric.

---

### 3. Experimental Rigor

**3.1 Statistical Power**

All comparisons use paired t-tests with n=3 (2 degrees of freedom). This is severely underpowered. The t-distribution at 2 df has extremely heavy tails; the critical t-value for p=0.05 (two-tailed) is 4.303, meaning only very large effect sizes relative to seed variance can achieve significance. The key null result (DC-GRPO vs. R3-only, p=0.187) cannot be meaningfully interpreted: the study lacks power to distinguish "no effect" from "small but real effect masked by variance." With 3 seeds, even the positive finding (DC-GRPO vs. ACT, p=0.008) should be viewed cautiously.

The paper reports p-values to 3 decimal places (e.g., p=0.187, p=0.448), which creates a false impression of precision given the n=3 foundation. Effect sizes (Cohen's d or equivalent) are not reported. Confidence intervals on effect-size differences are absent.

**Recommendation**: 5 seeds minimum, ideally 10. Bootstrap resampling over evaluation instances as complementary evidence. Report Cohen's d for all primary comparisons.

**3.2 Number of Comparisons**

Table 6 reports 8 pairwise statistical tests without correction for multiple comparisons. With 8 tests at alpha=0.05, the family-wise error rate exceeds 33%. The two significant results (DC-GRPO vs. ACT on NoF and WRR) would not survive Bonferroni correction (adjusted alpha = 0.00625). The paper should apply a correction (Bonferroni, Holm-Sidak, or Benjamini-Hochberg) or justify why it does not.

**3.3 Baseline Coverage**

The baseline set (Vanilla, R3-only, ACT, Binary Probe, Continuous Probe) is well-chosen for isolating design decisions. The inclusion of the Continuous Probe is particularly valuable and, as the paper honestly reports, is the decisive experiment. The ACT-style baseline serves as a useful negative control.

**Missing baseline**: Inference-time activation steering. If d_syc is extracted, the zero-training-cost alternative is to subtract a scaled d_syc from activations at inference time (Activation Addition). If this achieves comparable NoF reduction to DC-GRPO, the entire training framework is unnecessary. Its absence is a significant gap.

**3.4 Calibration Data**

200 pairs is a small dataset for direction estimation in a ~4096-dimensional space. The paper reports 11 pairs were filtered out (189 remaining from 200), but does not describe the filtering criteria or rejection reasons. The imbalanced distribution (80 weak, 60 medium, 60 strong) is not justified.

More critically, the paper does not report which model or process generated the contrastive pairs. If the pairs were generated by Qwen3-8B itself (or a closely related model), d_syc may capture generation-specific artifacts rather than a general sycophancy signal. If generated by GPT-4 or another external model, the stylistic properties of that model's outputs may introduce confounds despite style control.

**3.5 R1-R3 Correlation Collapse**

The finding that R1 and R3 become highly correlated (r>0.9 after step 4000) is reported but inadequately analyzed. This could mean: (a) the model has learned to satisfy both signals simultaneously (genuine convergence); (b) R1 has become a noisy proxy for R3 (direction drift reducing R1 to behavioral correlation); or (c) the directional signal was always capturing the same information as NLI, just in a different representation. The paper mentions possibility (c) in the Discussion but does not test it. A straightforward test would be to compute R1-R3 correlation at step 0 (before any training) on the calibration data; if it is already high, then the direction was never providing independent information.

**3.6 Human Validation**

The disagreement analysis (Exp. 7) reports manual verification of only 8 cases, finding 3 genuine masked sycophancy. This sample is far too small for any inference. With n=8 and 3/8 positive, the 95% CI on the true positive rate spans roughly [0.08, 0.75] (Wilson interval), which is uninformative.

**3.7 Training Dynamics Reporting**

Table 3 reports training progression with NoF, WRR, RC-AUC, R1, and R3 at each step, which is good practice. However, the paper does not report training loss, KL divergence from the reference policy, or gradient norms. These are standard diagnostics for GRPO/PPO training and their absence makes it difficult to assess whether training proceeded normally or exhibited pathologies (e.g., reward hacking, KL explosion).

---

### 4. Specific Weaknesses (Numbered)

**W1 [Critical]. 3 seeds is insufficient for the claims made.** The entire statistical framework rests on paired t-tests with 2 degrees of freedom. Neither positive nor negative findings can be reliably concluded. This is the paper's most serious methodological limitation.

**W2 [Major]. R2 is not an independent reward component.** R2 is a rank transformation of R1 scores within the GRPO group. The paper presents it as a third signal but it carries no information beyond R1. This undermines the "three-component reward" framing throughout the paper.

**W3 [Major]. RC-AUC is undefined.** The paper's composite metric is never formally specified. What threshold is swept? Over what operating range? Without this, the metric is not reproducible.

**W4 [Major]. Missing inference-time steering baseline.** Activation Addition using d_syc at inference time is the zero-cost alternative. Its absence prevents assessing whether DC-GRPO's training framework adds value over a simple post-hoc intervention.

**W5 [Major]. R1 formula uses unnormalized dot product.** This conflates directional alignment with activation magnitude. Cosine similarity would be more principled for a directional reward.

**W6 [Moderate]. R1-R3 initial correlation not reported.** Without knowing the pre-training correlation between R1 and R3, the paper cannot determine whether the direction ever provided independent information.

**W7 [Moderate]. Direction drift analysis lacks causal explanation.** The paper describes the drift (cosine to 0.66 in 3000 steps, 3 recalibrations needed) but does not analyze what drives it. Is it LoRA parameter updates? Shifts in the residual stream distribution? Layer-specific vs. global drift? Without understanding the cause, the paper cannot prescribe solutions.

**W8 [Moderate]. Multiple comparisons uncorrected.** 8 pairwise tests without correction inflates the family-wise error rate above 33%.

**W9 [Minor-Moderate]. Human validation sample too small.** 8 manually checked cases with 3 confirmed is uninformative (95% CI: [8%, 75%]).

**W10 [Minor-Moderate]. Calibration data generation process undocumented.** Source model, filtering criteria, rejection rate, and quality control are not described.

**W11 [Minor]. PCA_1 vs. mean-difference not compared.** The paper uses PCA_1 without justification or ablation against the standard mean-difference approach from RepE.

**W12 [Minor]. No bibliography.** References are informal in-text mentions without proper \cite{} or \bibliography{} entries. This is unacceptable for any venue submission.

**W13 [Minor]. Recalibration threshold (0.70) is unjustified and not ablated.**

---

### 5. Specific Strengths (Numbered)

**S1. Intellectually honest framing.** The paper reports a negative result transparently rather than overclaiming. The title and abstract accurately convey that DC-GRPO does not outperform simpler alternatives. This is rare and commendable.

**S2. Comprehensive experiment coverage.** 15 experiments covering calibration, main comparisons, ablations, turn-depth analysis, cross-model transfer, three-way direction design, continuous probe comparison, and weight sensitivity. The experiment plan is thorough and systematically isolates design decisions.

**S3. Continuous Probe baseline is the decisive experiment.** Including this baseline was a strong methodological choice. It cleanly separates the contribution of signal continuity from directional geometry, yielding the paper's most informative finding.

**S4. Direction stability monitoring is valuable.** Tracking cosine similarity and held-out AUROC throughout training provides practical guidance for future work on representation-level rewards. The finding that drift accelerates and recalibration has diminishing returns (post-recalibration cosine: 0.92, 0.91, 0.90) is a genuine contribution.

**S5. Layer-wise emergence analysis is informative.** The progression from chance (L0: 0.52) to peak (L19: 0.801) provides interpretable evidence about where evaluative processing occurs. The cross-model consistency (Qwen peak at L19/36, Llama peak at L18/32) is an interesting finding about architectural generality.

**S6. Turn-depth analysis tests a specific mechanistic hypothesis.** The finding that DC-GRPO's advantage over R3-only is constant (~1.3pp) across turn depths, rather than increasing at deeper turns, directly tests and falsifies the hypothesis that directional geometry captures commitment-specific mechanisms.

**S7. ACT baseline demonstrates the double-bind concretely.** ACT's WRR (0.571) falling below all targeted methods while having worse NoF confirms that undifferentiated activation constraints are counterproductive. This is a useful negative baseline.

**S8. Weight sensitivity analysis has a clear message.** The monotonic degradation with increasing R1 weight, with optimal R1 weight trending toward zero, provides direct evidence for the main negative conclusion.

---

### 6. Questions for Authors (Numbered)

1. What is the R1-R3 Pearson correlation at step 0 (before any training) on the calibration data? If it is already > 0.7, the direction was never providing independent information.

2. Why use PCA_1 of difference vectors rather than the mean difference vector (standard RepE approach)? Have you compared the two?

3. Why does R1 use raw dot product (Equation 2) rather than cosine similarity? The unnormalized formulation conflates direction and magnitude.

4. What is the formal definition of RC-AUC? What threshold is swept and over what range?

5. Which model generated the 200 contrastive pairs? What were the filtering criteria and rejection rate?

6. Have you tested inference-time activation steering (subtracting scaled d_syc at generation time) as a zero-training-cost alternative?

7. What is the statistical power of the DC-GRPO vs. R3-only comparison at n=3? Given the observed effect size (1.3pp) and variance (std ~0.026), what sample size would be needed to detect this effect at 80% power?

8. Is the R1-R3 correlation collapse (r>0.9 after step 4000) a consequence of (a) the model learning a unified strategy, (b) direction drift making R1 approximate R3, or (c) the signals being inherently collinear? Have you checked which explanation holds?

9. Table 8 shows diminishing post-recalibration cosine (0.92, 0.91, 0.90). What drives this trend? Is the calibration data becoming less representative, or is the representation space globally reorganizing?

10. For the 3/8 confirmed masked sycophancy cases, what specific criteria were used to adjudicate? Were annotators blind to which reward flagged the case?

11. The paper reports MT-Bench degradation of 0.89 for DC-GRPO (8.20 to 7.31). This is substantially larger than what the best-case scenario projects (-0.17). Is this degradation driven by R1 specifically? Does R3-only also show 0.82 degradation (8.20 to 7.38)?

12. Have you considered using the calibration AUROC threshold as a gating mechanism (only applying R1 when the direction is sufficiently discriminative)?

---

### 7. Overall Assessment

**Score: 3/6 (Weak Reject)**

**Justification:**

The paper addresses a real and important problem (the sycophancy-revision double-bind in multi-turn dialogue) and takes the honest approach of reporting negative results. The experimental coverage is comprehensive (15 experiments), and several findings are genuinely informative: the continuous probe baseline demonstrates that directional geometry per se does not add value; the direction stability analysis provides practical guidance; the layer-wise emergence pattern is interpretable; the weight sensitivity analysis cleanly shows optimal R1 weight trending to zero.

However, the paper does not meet the bar for a top venue for three primary reasons:

1. **Statistical foundation is inadequate.** 3 seeds with 2 df paired t-tests cannot reliably support either positive or negative conclusions. The central claim ("DC-GRPO does not significantly outperform R3-only") is indistinguishable from "the study lacks power to detect a real effect." This is a fundamental issue that undermines the entire paper.

2. **Methodological issues weaken the negative finding's interpretive value.** The unnormalized R1 dot product, the non-independent R2 component, the unjustified recalibration threshold, and the lack of initial R1-R3 correlation analysis all raise the question: did DC-GRPO fail because directional rewards are genuinely uninformative, or because this specific implementation was suboptimal? A negative result is only as strong as the method it tests, and the method has clear design flaws.

3. **Missing baselines and specifications.** The absence of inference-time steering (the zero-cost alternative), the undefined RC-AUC metric, the undocumented calibration data generation, and the missing bibliography collectively lower the paper's rigor below venue standards.

The paper would be strengthened substantially by: (a) 5-10 seeds for primary comparisons; (b) using cosine similarity in R1; (c) including inference-time steering baseline; (d) reporting initial R1-R3 correlation; (e) formally defining RC-AUC; (f) documenting calibration data generation; (g) proper bibliography.

As a boundary-conditions study, the paper's findings are informative but preliminary. The negative result could be due to implementation limitations rather than a fundamental property of directional rewards. With the above improvements, the paper could become a valuable contribution to understanding when representation-level training signals add value. In its current form, the methodological issues leave the core conclusion insufficiently supported.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d1ab856-3b4e-41c0-9e9e-75d087419b96",
  "isSidechain": true,
  "agentId": "aa18bf1166c4112dc",
  "requestId": "req_011CbA9fnSjrhXXBV5vimRxL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe3c4f64-4589-47d7-81ed-0193bdec22eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "cb0cb56d-be6d-4519-a3e4-ab42d9d3dce7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qcr6SyrvCk8KEWrJfSHCPp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13677,
      "cache_read_input_tokens": 78974,
      "output_tokens": 4765,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13677
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4765,
          "cache_read_input_tokens": 78974,
          "cache_creation_input_tokens": 13677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13677,
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
