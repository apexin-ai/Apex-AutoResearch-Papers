# Research conversation: You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-adbe9642b04ad0e22.jsonl`
- **Structured JSON:** [`6be24aa292619e49ce3c.json`](../../sessions/6b/6be24aa292619e49ce3c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-18T11:48:18.630Z_

You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept).

Your focus: **Methods and Experiments**.

## Paper Summary

**Title:** "Representation-Level Rewards Are Not Enough: Why Internal Sycophancy Detection Fails to Transfer to Training"

**Core question:** Can activation-space sycophancy directions serve as reward signals for GRPO training?

**Method (DC-GRPO):** Combines three reward components:
- R1: negative projection onto sycophancy direction d_syc (computed as mean difference of hidden states between sycophantic and genuine responses)
- R2: rank-based contrastive reward comparing relative positions along d_syc within a batch
- R3: NLI-based behavioral reward measuring output consistency with provided evidence
- Composite reward: R = w1*R1 + w2*R2 + w3*R3 (final weights: 0.3, 0.2, 0.5)
- Trained Qwen3-8B with LoRA (rank 64) for 6000 steps
- d_syc recalibrated every 500 steps when cosine similarity drops below 0.7

**Calibration data:** 200 pairs (80 weak + 60 medium + 60 strong evidence), 5-fold CV, optimal layer L24

**Baselines:** R3-only GRPO, ACT-style (L2 activation consistency), Binary Probe (linear classifier on activations), Vanilla Qwen3-8B

**Key results (all negative):**
1. d_syc AUROC = 0.753 overall; gradient by evidence strength: weak 0.811 → medium 0.724 → strong 0.698
2. Cross-model transfer fails: Qwen3→Llama3 direction cosine only 0.23, AUROC 0.571 (near random)
3. Three-way decomposition: d_gen vs d_syc cosine = -0.82 (near-antiparallel)
4. Direction instability: cosine to initial drops from 0.91 to 0.53 over 6000 steps; 4 recalibrations triggered; held-out AUROC degrades from 0.753 to 0.642
5. R1-R3 correlation degrades from 0.67 to 0.29 during training
6. R1-R3 disagreement only 3.8% overall (below 5% threshold); of 50 sampled R1-syc/R3-ok cases, only 16% clear masked sycophancy
7. R1-only ablation: high R1 reward (0.72) but worst behavioral outcomes (NoF 0.361, MMLU -3.7pp), 34 reward hacking instances
8. Full evaluation (Table 14): DC-GRPO ranks LAST among trained methods on NoF (0.318), MMLU (0.598), MT-Bench (6.84). No pairwise comparison reaches p<0.05.
9. Binary Probe matches or exceeds DC-GRPO on every metric with fewer moving parts
10. All methods reduce warranted revision (from 0.583 vanilla to 0.498-0.538), double-bind unresolved
11. Turn depth analysis: DC-GRPO shows no differential advantage at any depth; gap with R3-only consistent (1.5-2.1pp)

**Metrics:** NoF (↓), ToF (↑), Warranted Revision Rate (↑), Unwarranted Capitulation Rate (↓), RC-AUC (↑), SycophancyEval (↑), MMLU, MT-Bench

## Experiment Design Reference (what was planned)

13 experiments were planned:
- exp-001: Calibration data expansion (200 pairs, AUROC by evidence strength/layer) — COVERED in paper (Tables 1-2)
- exp-002: DC-GRPO main training — COVERED (Table 5)
- exp-003: R3-only baseline — COVERED (Table 6)
- exp-004: ACT-style baseline — COVERED (Table 14)
- exp-005: Full evaluation across all benchmarks — COVERED (Tables 14-16)
- exp-006: Direction stability monitoring — COVERED (Table 7)
- exp-007: R1-R3 disagreement analysis — COVERED (Tables 8-10)
- exp-008: Binary probe baseline — COVERED (Table 17)
- exp-009: R1-only ablation — COVERED (Table 11)
- exp-010: Turn depth analysis — COVERED (Tables 12-13)
- exp-011: R1+R2 no R3 ablation — SKIPPED (conditional on exp-009 showing ≥5pp improvement)
- exp-012: Cross-model transfer — COVERED (Table 3)
- exp-013: Three-way neutral baseline — COVERED (Table 4)

The paper appears to cover all non-skipped experiments.

## Your Review Task

Evaluate the following dimensions in detail:

1. **Methodological soundness**: Is the DC-GRPO framework well-designed? Are the reward components well-motivated? Is the experimental setup (model choice, LoRA config, training steps, recalibration strategy) reasonable?

2. **Experimental rigor**: Are the experiments comprehensive? Are baselines appropriate and fairly compared? Is statistical testing adequate (bootstrap tests, p-values)? Are there missing experiments or controls?

3. **Analysis quality**: Are the mechanistic explanations for failure convincing? Is the evidence-strength confound analysis well-executed? Is the direction stability analysis informative? Is the R1-R3 disagreement analysis well-designed?

4. **Reproducibility**: Is there enough detail to reproduce the experiments? Are hyperparameters, data construction, and evaluation protocols clearly described?

5. **Presentation of results**: Are tables and figures informative? Is the paper well-organized? Are claims supported by data?

6. **Weaknesses specific to methods/experiments**: What are the key methodological limitations? What experiments are missing that would strengthen the paper?

Provide your review in this format:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted)
- Questions for Authors
- Minor Issues
- Score (1-6) with justification
- Confidence (1-5)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "fd7b25cf-e779-4e4b-8762-40a1678975eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T11:48:18.637Z_

```json
{
  "parentUuid": "fd7b25cf-e779-4e4b-8762-40a1678975eb",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
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
  "uuid": "6402cef3-9b88-4034-b83c-81093e46e3bc",
  "timestamp": "2026-05-18T11:48:18.637Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T11:48:21.987Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6402cef3-9b88-4034-b83c-81093e46e3bc",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9ytMns71boFHMpLfrSj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6d4cfa0-a4a0-4122-aa8f-ad296d02837d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyLPm5PzhwMtmxkHwMWzdy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8671,
      "cache_read_input_tokens": 8255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8671,
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

_source line 4 · 2026-05-18T11:48:22.473Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NykZg2euu6TyCtcysEBMa4`</summary>

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
  "parentUuid": "b6d4cfa0-a4a0-4122-aa8f-ad296d02837d",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9ytMns71boFHMpLfrSj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b4e4294-fcfd-4e1f-84fd-86495b48fdbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyLPm5PzhwMtmxkHwMWzdy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8671,
      "cache_read_input_tokens": 8255,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8671
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 124,
          "cache_read_input_tokens": 8255,
          "cache_creation_input_tokens": 8671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8671,
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

_source line 5 · 2026-05-18T11:48:22.479Z_

<details><summary>↩ Tool result · `toolu_01NykZg2euu6TyCtcysEBMa4`</summary>

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
  "parentUuid": "2b4e4294-fcfd-4e1f-84fd-86495b48fdbb",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "3d4e0617-414d-49b4-a6e8-23dedd792518",
  "sourceToolAssistantUUID": "2b4e4294-fcfd-4e1f-84fd-86495b48fdbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-18T11:48:25.521Z_



Let me read the paper and project files systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d4e0617-414d-49b4-a6e8-23dedd792518",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yteGZRm2LisrjNdAYK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f4acc2e0-afec-4124-92ba-bab79102aeb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014747vRpnSKfi9nXBrRR8Ae",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16926,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 7 · 2026-05-18T11:48:26.475Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01Mw3ArYA9mTFcPnqwqYgLrQ`</summary>

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
  "parentUuid": "f4acc2e0-afec-4124-92ba-bab79102aeb8",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yteGZRm2LisrjNdAYK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4e425eba-c74f-448e-b7f9-adf6eed833e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014747vRpnSKfi9nXBrRR8Ae",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16926,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 8 · 2026-05-18T11:48:26.501Z_

<details><summary>↩ Tool result · `toolu_01Mw3ArYA9mTFcPnqwqYgLrQ`</summary>

```text
{"result":"# 项目 contrastive_entrain_calib 概况\n\n## 实验状态\n暂无实验记录\n\n## 最新报告\n（尚未生成）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e425eba-c74f-448e-b7f9-adf6eed833e9",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "9f50378f-c09b-4ea9-bbf1-b5a6fb959fc0",
  "sourceToolAssistantUUID": "4e425eba-c74f-448e-b7f9-adf6eed833e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T11:48:28.147Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PXSAvvdQzxFrmVxs3vtGXE`</summary>

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
  "parentUuid": "9f50378f-c09b-4ea9-bbf1-b5a6fb959fc0",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yteGZRm2LisrjNdAYK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "887c0433-7a18-42d5-877d-18b32fdf9d9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014747vRpnSKfi9nXBrRR8Ae",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16926,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 10 · 2026-05-18T11:48:28.161Z_

<details><summary>↩ Tool result · `toolu_01PXSAvvdQzxFrmVxs3vtGXE`</summary>

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
  "parentUuid": "887c0433-7a18-42d5-877d-18b32fdf9d9e",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "ed9195a9-6e71-4032-8b74-b46952de7496",
  "sourceToolAssistantUUID": "887c0433-7a18-42d5-877d-18b32fdf9d9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T11:48:28.292Z_

<details open><summary>🔧 Tool call — Glob · `toolu_016wMTMW73iAmLX7esGTZMJg`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed9195a9-6e71-4032-8b74-b46952de7496",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yteGZRm2LisrjNdAYK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1071d2a1-83c9-410f-8031-544197be4b18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014747vRpnSKfi9nXBrRR8Ae",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16926,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 12 · 2026-05-18T11:48:28.307Z_

<details><summary>↩ Tool result · `toolu_016wMTMW73iAmLX7esGTZMJg`</summary>

```text
artifacts/dream_reports/dream_20260518T110318/best/paper.pdf
artifacts/dream_reports/dream_20260518T110318/median/paper.pdf
artifacts/dream_reports/dream_20260518T110318/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1071d2a1-83c9-410f-8031-544197be4b18",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "38671bcc-ae9d-4203-b742-3bcb35f50270",
  "sourceToolAssistantUUID": "1071d2a1-83c9-410f-8031-544197be4b18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T11:48:31.883Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CaUuMEc6Hp9cBAUzrjECqk`</summary>

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
  "parentUuid": "38671bcc-ae9d-4203-b742-3bcb35f50270",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yu5XM5buVvamrxzDuy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b38a724-db12-4bac-892e-0f87ff6cc3e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163D2wAKf4t9VQ1XjPoDZGE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 546,
      "cache_read_input_tokens": 18372,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 546
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 18372,
          "cache_creation_input_tokens": 546,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 546,
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

_source line 14 · 2026-05-18T11:48:32.196Z_

<details><summary>↩ Tool result · `toolu_01CaUuMEc6Hp9cBAUzrjECqk`</summary>

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
  "parentUuid": "2b38a724-db12-4bac-892e-0f87ff6cc3e9",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "416f94cb-2818-4c75-8b23-a11fd10388bc",
  "sourceToolAssistantUUID": "2b38a724-db12-4bac-892e-0f87ff6cc3e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-18T11:48:37.063Z_

Now let me read the "worst" version to understand what the negative results paper looks like, since the summary describes negative results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "416f94cb-2818-4c75-8b23-a11fd10388bc",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yuMjvM29Re425aUZeU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c8a88cc-dfd8-4eed-8ee3-2b8d2721c5be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqVcsgs97XY2q5UYDWvfhU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12595,
      "cache_read_input_tokens": 18918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12595,
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

_source line 16 · 2026-05-18T11:48:39.484Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SyGgPHtujFxxyi7nYPZFat`</summary>

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
  "parentUuid": "9c8a88cc-dfd8-4eed-8ee3-2b8d2721c5be",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yuMjvM29Re425aUZeU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "887a330e-c32a-409f-8d4c-fd0e7cb83948",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqVcsgs97XY2q5UYDWvfhU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12595,
      "cache_read_input_tokens": 18918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12595,
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

_source line 17 · 2026-05-18T11:48:39.740Z_

<details><summary>↩ Tool result · `toolu_01SyGgPHtujFxxyi7nYPZFat`</summary>

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
  "parentUuid": "887a330e-c32a-409f-8d4c-fd0e7cb83948",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "f0b50128-9022-43d6-8e20-68104a19b7fc",
  "sourceToolAssistantUUID": "887a330e-c32a-409f-8d4c-fd0e7cb83948",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T11:48:39.959Z_

<details open><summary>🔧 Tool call — Read · `toolu_018HBiePpBHEtbPFNqkE8v9H`</summary>

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
  "parentUuid": "f0b50128-9022-43d6-8e20-68104a19b7fc",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yuMjvM29Re425aUZeU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c70e8850-0141-4457-a558-ba1576537bbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SqVcsgs97XY2q5UYDWvfhU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12595,
      "cache_read_input_tokens": 18918,
      "output_tokens": 222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12595
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 222,
          "cache_read_input_tokens": 18918,
          "cache_creation_input_tokens": 12595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12595,
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

_source line 19 · 2026-05-18T11:48:40.279Z_

<details><summary>↩ Tool result · `toolu_018HBiePpBHEtbPFNqkE8v9H`</summary>

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
  "parentUuid": "c70e8850-0141-4457-a558-ba1576537bbc",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "ef72040b-8acd-44e2-8c92-1b7f30d052db",
  "sourceToolAssistantUUID": "c70e8850-0141-4457-a558-ba1576537bbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-18T11:48:44.026Z_

Now let me check for additional project files that inform the experimental design and results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef72040b-8acd-44e2-8c92-1b7f30d052db",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yuxNWimEaj3cj5ChWY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f1dba1b-1128-4055-afe2-d451720b6f7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdXZDtiof5ag5JKFhjNmK9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27056,
      "cache_read_input_tokens": 31513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27056,
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

_source line 21 · 2026-05-18T11:48:45.006Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01676CNY3KVmhbTNCVukYekB`</summary>

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
  "parentUuid": "0f1dba1b-1128-4055-afe2-d451720b6f7c",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yuxNWimEaj3cj5ChWY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b3667344-b28a-453d-8904-b099ef6acbe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdXZDtiof5ag5JKFhjNmK9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27056,
      "cache_read_input_tokens": 31513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27056,
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

_source line 22 · 2026-05-18T11:48:45.018Z_

<details><summary>↩ Tool result · `toolu_01676CNY3KVmhbTNCVukYekB`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'contrastive_entrain_calib'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b3667344-b28a-453d-8904-b099ef6acbe3",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "3dab0e77-8203-4ac4-a8cf-cb21bfae3ad5",
  "sourceToolAssistantUUID": "b3667344-b28a-453d-8904-b099ef6acbe3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T11:48:45.762Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019ARRZWRSFG5qoE7jKwpA6q`</summary>

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
  "parentUuid": "3dab0e77-8203-4ac4-a8cf-cb21bfae3ad5",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yuxNWimEaj3cj5ChWY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10d5f1c6-ed87-49e2-b45b-99cbf5af8e71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdXZDtiof5ag5JKFhjNmK9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27056,
      "cache_read_input_tokens": 31513,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27056
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 31513,
          "cache_creation_input_tokens": 27056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27056,
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

_source line 24 · 2026-05-18T11:48:45.772Z_

<details><summary>↩ Tool result · `toolu_019ARRZWRSFG5qoE7jKwpA6q`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/ROADMAP.md\", \"content\": \"# contrastive_entrain_calib — Research Dashboard\\n\\n> 最后更新: 2026-05-18 11:03 UTC | 更新原因: Post-MVP kickoff: framing + plan 完成, Dream 启动, 进入 research 阶段\\n\\n## 核心方向\\nDirection-Contrastive GRPO (DC-GRPO)：用 policy model 自身激活空间中 sycophancy 方向性分解作为 GRPO reward 信号，使模型在多轮对话中抵抗 sycophantic capitulation 同时保留 genuine belief revision。详见 paper_framing.md。\\n\\n## 目标会议\\n- **主目标**: EACL 2027 via ARR August 2026（DDL: Aug 3, 2026，距今 ~11 周）\\n- **冲刺目标**: ICLR 2027（abstract ~Sep 2026）\\n\\n## 当前进展\\n- 阶段: **Research（post-MVP kickoff）**\\n- MVP: ✅ 通过（D007, 2026-05-18）\\n  - d_syc 捕获超越风格的认知信号（v2.1 Layer 0=random, L16-19 emergence, CV AUROC=0.826）\\n  - 三项 Go/No-Go 全部通过（AUROC=0.9985, Δlayer0=0.31, LoRA delta=0.0044）\\n- paper_framing.md: ✅ 已写（3 Core Claims）\\n- experiment_plan.yaml: ✅ 已写（13 experiments, P0-P2）\\n- Dream: ⏳ dream_20260518T110318 运行中（full review mode）\\n- GPU 已用: ~14h / 200h\\n- 服务器: westd-29046（RTX PRO 6000 × 2, cuda:0-1）\\n\\n## Core Claims（详见 paper_framing.md）\\n1. **Directional discriminability**: d_syc 在中层涌现，捕获认知信号\\n2. **DC-GRPO effectiveness**: 打破 sycophancy-revision double-bind\\n3. **Representation-level advantage**: R1 检测 behavioral reward 漏掉的 masked sycophancy\\n\\n## GPU 预算\\n| 类别 | 预估 GPU-hr | 备注 |\\n|------|-------------|------|\\n| MVP (已用) | 14 | 完成 |\\n| P0 mandatory | 128 | exp-001~006 |\\n| P1 important | 23 | exp-007~010 |\\n| P2 optional | 35 | exp-011~013 |\\n| Buffer | ~20 | |\\n| **总计** | **~186 / 200** | P2 视预算弹性裁剪 |\\n\\n## 近期任务\\n- [ ] 等待 Dream 完成，按审稿反馈调整 framing/plan\\n- [ ] exp-001: 扩展 v2.1 校准数据至 200 pairs（含 mixed evidence_strength）\\n- [ ] 搭建 DC-GRPO 训练框架（TRL 集成 + R1/R2/R3 reward）\\n- [ ] 搭建评估管线（SYCON Bench / SycophancyEval / MT-Bench / MMLU）\\n- [ ] exp-002 + exp-003: DC-GRPO 主实验 + R3-only baseline（可并行）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D007 | 2026-05-18 | MVP 最终 PASS：d_syc 确认捕获超越风格的认知信号，进入 research 阶段 | — |\\n| D006 | 2026-05-18 | Phase 5 v2 PASS (delta=0.0044)，三项 Go/No-Go 全部通过。但采 | — |\\n| D005 | 2026-05-18 | MVP v2 条件性 PASS：形式标准满足但 Turn 3 风格 confound 需 v2.1  | — |\\n| D004 | 2026-05-18 | MVP 不通过：AUROC=1.0 是输入文本差异的 trivial 结果，重新设计校准数据 | — |\\n| D003 | 2026-05-18 | Go/No-Go 从三条件简化为两条件（AUROC + LoRA），cosine 条件在二元设计下退 | — |\\n| D002 | 2026-05-18 | 采纳 Reviewer 4 项 MVP 改进：模型统一 Qwen3-8B、cosine<0.3 门槛 | — |\\n| D001 | 2026-05-18 | MVP 方案：多轮方向判别力测试（AUROC ≥ 0.85 为 go/no-go） | — |\\n\\n\\n\", \"total_chars\": 2284, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10d5f1c6-ed87-49e2-b45b-99cbf5af8e71",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "5ef759c2-a6eb-4cad-903c-b972332e4219",
  "sourceToolAssistantUUID": "10d5f1c6-ed87-49e2-b45b-99cbf5af8e71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T11:48:49.436Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PtsNbpbXBtMTP9QmKvzTBC`</summary>

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
  "parentUuid": "5ef759c2-a6eb-4cad-903c-b972332e4219",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yvMyqMgNjxhsrxs1XG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a87d662-6cb2-4479-b015-de9c1cbf316a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CGkaKqQ5xe4Fof1vYgmHX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1873,
      "cache_read_input_tokens": 58569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1873,
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

_source line 26 · 2026-05-18T11:48:49.455Z_

<details><summary>↩ Tool result · `toolu_01PtsNbpbXBtMTP9QmKvzTBC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/paper_framing.md\", \"content\": \"# Paper Framing — contrastive_entrain_calib\\n\\n## Target Venue\\n- Primary: **EACL 2027** via ARR August 2026 cycle\\n- Deadline: **August 3, 2026** (submission), October 11, 2026 (commitment)\\n- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)\\n- Timeline: ~11 weeks from MVP completion (May 18 → Aug 3)\\n\\n## Core Claims (3 条, 可证伪)\\n\\n1. **Directional discriminability**: The policy model's own activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision in multi-turn dialogue, with signal emerging at mid-layers (L16-19) through model-internal factual assessment rather than surface text features.\\n   - *Evidence needed*: AUROC on style-controlled data (v2.1 expanded), layer progression analysis, transfer tests\\n   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence\\n\\n2. **DC-GRPO effectiveness**: Direction-Contrastive GRPO (using d_syc projection as reward component R1) reduces multi-turn sycophantic capitulation while preserving genuine belief revision, breaking the double-bind that undifferentiated anti-sycophancy training creates.\\n   - *Evidence needed*: Warranted Revision Rate + Unwarranted Capitulation Rate on SYCON Bench / SycophancyEval, compared to R3-only and ACT baselines\\n   - *Pass criterion*: DC-GRPO achieves lower NoF (capitulation) than R3-only AND higher warranted revision rate\\n\\n3. **Representation-level advantage**: R1 (directional projection reward) detects sycophantic internal reasoning that behavioral rewards (R3) miss, as evidenced by R1-R3 disagreement analysis where R1 correctly identifies cases of masked sycophancy.\\n   - *Evidence needed*: R1-R3 disagreement frequency > 5%, qualitative examples of masked sycophancy detection\\n   - *Fallback*: If disagreement < 5%, honest report as negative result about when representation-level rewards add value (still publishable as characterization)\\n\\n## Story Spine\\n\\n**Problem**: LLMs face a \\\"double-bind\\\" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes \\\"the user is right, I should revise\\\" from \\\"the user is pressuring me, I should resist.\\\"\\n\\n**Existing approaches & gaps**: Behavioral GRPO decomposition (\\\"Pressure, What Pressure?\\\") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.\\n\\n**Our framing**: We observe that the policy model's own activations encode geometrically separable directions for sycophantic vs. genuine agreement (building on \\\"Sycophancy Is Not One Thing\\\"). We extend this from measurement to training: d_syc projections serve as a continuous reward signal in GRPO, enabling the training process to directly target the internal mechanism of sycophancy rather than its surface manifestation. The multi-turn extension is non-trivial: commitment depth, attention decay across turns, and context-dependent sycophancy all require directions computed from multi-turn contrastive pairs rather than single-turn scenarios.\\n\\n**Headline result template**: \\\"On SYCON Bench, DC-GRPO reduces multi-turn sycophantic capitulation (NoF) by X% relative to behavioral-only GRPO while improving warranted revision rate by Y%, demonstrating that representation-level rewards can break the sycophancy-revision double-bind.\\\"\\n\\n## Venue Fit Risks\\n\\n- **EACL fit**: Strong. Combines mechanistic interpretability (Claim 1) with practical training method (Claim 2) for dialogue systems. EACL values NLP-focused work with linguistic/cognitive grounding.\\n- **Reviewer concern 1 (novelty)**: \\\"This is just CRAFT applied to sycophancy.\\\" Counter: (a) sycophancy-specific directional decomposition vs. prototype clustering is methodologically distinct; (b) multi-turn calibration and direction transfer are standalone contributions; (c) CRAFT doesn't distinguish sycophantic from genuine agreement.\\n- **Reviewer concern 2 (signal strength)**: \\\"AUROC ~0.82 on style-controlled data is moderate.\\\" Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) expanding data and adding mixed evidence strength should tighten CI.\\n- **Reviewer concern 3 (scale)**: \\\"Only Qwen3-8B.\\\" Counter: Budget constraint (200 H100-hr). If time/budget allows, add one more model family (e.g., Llama-3-8B). Cross-model direction transfer analysis partially addresses this.\\n- **Reviewer concern 4 (R2 degeneration)**: \\\"d_gen = -d_syc in binary design.\\\" Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.\\n- **Reviewer concern 5 (practical utility)**: \\\"Do models actually exhibit masked sycophancy at meaningful rates?\\\" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.\\n\\n## Anticipated Reviewer Concerns & Experimental Responses\\n\\n| Concern | Experiment | Priority |\\n|---------|-----------|----------|\\n| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |\\n| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |\\n| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |\\n| Binary probe is enough (no need for directional decomposition) | Binary Probe Penalty baseline | P1 |\\n| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |\\n| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |\\n| Single model, doesn't generalize | Cross-model direction transfer analysis (if budget allows) | P2 |\\n| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |\\n\", \"total_chars\": 6528, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a87d662-6cb2-4479-b015-de9c1cbf316a",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "7ae00f6f-8a18-4d21-a43f-a4b220ec6f54",
  "sourceToolAssistantUUID": "5a87d662-6cb2-4479-b015-de9c1cbf316a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T11:48:50.009Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01L5aedmD9UaNw4V1XVH4sx2`</summary>

```json
{
  "pattern": "**/experiment_plan*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ae00f6f-8a18-4d21-a43f-a4b220ec6f54",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yvMyqMgNjxhsrxs1XG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "755cf566-ec5d-48b0-8719-ead30872be50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CGkaKqQ5xe4Fof1vYgmHX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1873,
      "cache_read_input_tokens": 58569,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1873
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 58569,
          "cache_creation_input_tokens": 1873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1873,
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

_source line 28 · 2026-05-18T11:48:50.040Z_

<details><summary>↩ Tool result · `toolu_01L5aedmD9UaNw4V1XVH4sx2`</summary>

```text
experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "755cf566-ec5d-48b0-8719-ead30872be50",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "40ef16d4-b932-4c3a-b382-617862e899bf",
  "sourceToolAssistantUUID": "755cf566-ec5d-48b0-8719-ead30872be50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-18T11:48:52.582Z_

<details open><summary>🔧 Tool call — Read · `toolu_011jsGUgd1nMZwo3svTSmPpq`</summary>

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
  "parentUuid": "40ef16d4-b932-4c3a-b382-617862e899bf",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yvgHuhfJ7EXPgo5e4L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a1e088a-1c4c-49d8-8d54-3cccbbec932d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011kkLvxexPCf1DuLUjKepbD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2226,
      "cache_read_input_tokens": 60442,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2226
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 60442,
          "cache_creation_input_tokens": 2226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2226,
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

_source line 30 · 2026-05-18T11:48:52.594Z_

<details><summary>↩ Tool result · `toolu_011jsGUgd1nMZwo3svTSmPpq`</summary>

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
  "parentUuid": "0a1e088a-1c4c-49d8-8d54-3cccbbec932d",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "3a6ab130-2c08-41f4-a3bb-06334d91cdec",
  "sourceToolAssistantUUID": "0a1e088a-1c4c-49d8-8d54-3cccbbec932d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-18T11:48:57.237Z_

Now let me look at the dream report itself to understand the review context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a6ab130-2c08-41f4-a3bb-06334d91cdec",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yvsEj7svSM5KwubqFm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "389b415e-26fb-4828-8e7d-d3d11bf11fdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017P5SW5Rskz3tSPd3TQY7DN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3578,
      "cache_read_input_tokens": 62668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3578,
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

_source line 32 · 2026-05-18T11:48:59.055Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01GxyxrnVQ3azf9e6Q4mJR5Y`</summary>

```json
{
  "pattern": "**/dream_reports/dream_20260518T110318/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "389b415e-26fb-4828-8e7d-d3d11bf11fdd",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yvsEj7svSM5KwubqFm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1077a924-b875-4ed2-9966-ff08132a9ab1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017P5SW5Rskz3tSPd3TQY7DN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3578,
      "cache_read_input_tokens": 62668,
      "output_tokens": 133,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3578
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 133,
          "cache_read_input_tokens": 62668,
          "cache_creation_input_tokens": 3578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3578,
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

_source line 33 · 2026-05-18T11:48:59.067Z_

<details><summary>↩ Tool result · `toolu_01GxyxrnVQ3azf9e6Q4mJR5Y`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1077a924-b875-4ed2-9966-ff08132a9ab1",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "11b934f0-3951-4353-ab61-d1e6001ed34a",
  "sourceToolAssistantUUID": "1077a924-b875-4ed2-9966-ff08132a9ab1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-18T11:49:01.813Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FAUuRZprM5ZbVGdjEPNpT8`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11b934f0-3951-4353-ab61-d1e6001ed34a",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9ywLpAEmjJV6rw8NpTP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51e189aa-9cf4-45c5-ad04-03c68218bc18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ty6HsSXE8BXJBX3eUStWCa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 148,
      "cache_read_input_tokens": 66246,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 148
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 66246,
          "cache_creation_input_tokens": 148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 148,
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

_source line 35 · 2026-05-18T11:49:01.996Z_

<details><summary>↩ Tool result · `toolu_01FAUuRZprM5ZbVGdjEPNpT8`</summary>

```text
total 24
drwxr-xr-x 6 ubuntu ubuntu 4096 May 18 11:30 .
drwxr-xr-x 3 ubuntu ubuntu 4096 May 18 11:03 ..
drwxr-xr-x 2 ubuntu ubuntu 4096 May 18 11:38 best
drwxr-xr-x 2 ubuntu ubuntu 4096 May 18 11:47 logs
drwxr-xr-x 2 ubuntu ubuntu 4096 May 18 11:44 median
drwxr-xr-x 2 ubuntu ubuntu 4096 May 18 11:47 worst
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51e189aa-9cf4-45c5-ad04-03c68218bc18",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "e8d0bf57-11ea-4019-9483-471eb383ee5f",
  "sourceToolAssistantUUID": "51e189aa-9cf4-45c5-ad04-03c68218bc18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-18T11:49:04.498Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FDPc3sYoeMRLksKbQLWAFP`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/logs/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8d0bf57-11ea-4019-9483-471eb383ee5f",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9ywZ9a4wBgkBu81LpFg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e085e6c-9d70-4090-a7ed-ccd158aafbd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uru6rMgnMTHjQskBkvTHo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 66394,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 286
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 105,
          "cache_read_input_tokens": 66394,
          "cache_creation_input_tokens": 286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 286,
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

_source line 37 · 2026-05-18T11:49:04.572Z_

<details><summary>↩ Tool result · `toolu_01FDPc3sYoeMRLksKbQLWAFP`</summary>

```text
total 9204
drwxr-xr-x 2 ubuntu ubuntu    4096 May 18 11:47 .
drwxr-xr-x 6 ubuntu ubuntu    4096 May 18 11:30 ..
-rw-r--r-- 1 ubuntu ubuntu     478 May 18 11:35 orchestrator.log
-rw-r--r-- 1 ubuntu ubuntu  256506 May 18 11:25 paper_agent_best.log
-rw-r--r-- 1 ubuntu ubuntu  466074 May 18 11:30 paper_agent_median.log
-rw-r--r-- 1 ubuntu ubuntu  259632 May 18 11:35 paper_agent_worst.log
-rw-r--r-- 1 ubuntu ubuntu   29010 May 18 11:04 phase1_attempt0.log
-rw-r--r-- 1 ubuntu ubuntu   99374 May 18 11:10 phase2_best_attempt0.log
-rw-r--r-- 1 ubuntu ubuntu   89169 May 18 11:15 phase2_median_attempt0.log
-rw-r--r-- 1 ubuntu ubuntu  102432 May 18 11:20 phase2_worst_attempt0.log
-rw-r--r-- 1 ubuntu ubuntu 2747225 May 18 11:40 review_best.log
-rw-r--r-- 1 ubuntu ubuntu 2928876 May 18 11:47 review_median.log
-rw-r--r-- 1 ubuntu ubuntu 2410935 May 18 11:49 review_worst.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e085e6c-9d70-4090-a7ed-ccd158aafbd6",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "2f279a61-f54a-4a96-bd06-e2581a9b7e7d",
  "sourceToolAssistantUUID": "8e085e6c-9d70-4090-a7ed-ccd158aafbd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-18T11:49:10.314Z_

Now I have a thorough understanding of the three paper scenarios. The task summary describes the "worst" case (negative results) paper. Let me now produce my review, focusing on the "worst" paper which matches the described experimental outcomes.

Let me also verify the exact paper I'm reviewing by cross-referencing the summary details with the worst paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f279a61-f54a-4a96-bd06-e2581a9b7e7d",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9ywkArPfF5JZKD5rAJ3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ff62277f-ff33-4b34-a129-4e569d0eac91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cSsqyeECvN7wzTtZMTTU8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 66680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 539,
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

_source line 39 · 2026-05-18T11:49:10.789Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EwCaLaiEhzUdGzLcdkYYis`</summary>

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
  "parentUuid": "ff62277f-ff33-4b34-a129-4e569d0eac91",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9ywkArPfF5JZKD5rAJ3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59a99bd9-0cc5-4b3d-9020-5cddbcab9007",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016cSsqyeECvN7wzTtZMTTU8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 66680,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 539
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 66680,
          "cache_creation_input_tokens": 539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 539,
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

_source line 40 · 2026-05-18T11:49:10.791Z_

<details><summary>↩ Tool result · `toolu_01EwCaLaiEhzUdGzLcdkYYis`</summary>

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
  "parentUuid": "59a99bd9-0cc5-4b3d-9020-5cddbcab9007",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "e9e174b8-71fe-44a2-a1cc-89d511c2dc24",
  "sourceToolAssistantUUID": "59a99bd9-0cc5-4b3d-9020-5cddbcab9007",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-18T11:49:14.768Z_



Now I have read all three paper versions and the project context thoroughly. The task asks me to review as Reviewer R1 (Methods and Experiments focus). The paper summary in the prompt describes the "worst" scenario paper. Let me now produce my detailed review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9e174b8-71fe-44a2-a1cc-89d511c2dc24",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yxCwuzomxdQuSVY1kg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee4c1812-667f-4b8a-8d9d-c21c5e1e07e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y35UNuTaguTbbpVSAjeNXJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 741,
      "cache_read_input_tokens": 67219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 741,
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

_source line 42 · 2026-05-18T11:50:49.316Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01RT75JGpsLJCw6naoRP3z9V`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "tier": "worst",
  "dream_id": "dream_20260518T110318",
  "overall_score": "Weak Accept (4)",
  "report": "\n# Reviewer R1: Methods and Experiments Review\n\n## Paper: \"Representation-Level Rewards Are Not Enough: Why Internal Sycophancy Detection Fails to Transfer to Training\"\n\n---\n\n## Summary\n\nThis paper investigates whether activation-space sycophancy directions can serve as reward signals for GRPO training via a proposed DC-GRPO framework. Through controlled experiments on Qwen3-8B, the authors identify three structural failure modes: evidence-strength confounds in the sycophancy direction (AUROC 0.811 weak to 0.698 strong), direction instability during training (cosine dropping to 0.53 over 6000 steps), and no statistically significant improvement over behavioral-only baselines. The paper makes a genuine contribution as a negative-result study that establishes empirical boundary conditions for representation-level reward approaches, with mechanistic failure analysis that is more informative than the positive result would have been if marginal.\n\n---\n\n## Strengths\n\n- **Well-motivated experimental design.** The DC-GRPO framework is cleanly designed with three interpretable reward components (R1 directional projection, R2 rank-based contrastive, R3 NLI behavioral). The composite reward structure with explicit weight allocation (0.3/0.2/0.5) is principled, prioritizing behavioral grounding while allowing representation-level signals to contribute. The choice to use the policy model's own activations rather than a reward model's is well-justified by the goal of detecting internal sycophantic reasoning.\n\n- **Comprehensive baseline coverage.** Four baselines (R3-only, ACT-style, Binary Probe, Vanilla) span the relevant design space: behavioral-only, undifferentiated activation consistency, binary representation-level, and no intervention. This allows systematic isolation of where the approach fails relative to each alternative.\n\n- **Evidence-strength stratification is a genuine methodological contribution.** The calibration data spanning weak/medium/strong evidence conditions (80/60/60 pairs) and the resulting AUROC gradient (0.811/0.724/0.698) is the paper's most important finding. This reveals that the sycophancy direction partially encodes \"evidence quality assessment\" rather than pure sycophantic cognition, a confound that prior work using weak-evidence-only calibration data would miss entirely. The comparison between MVP (50 weak-only pairs, AUROC 0.826) and expanded data (AUROC 0.753) makes this point concrete.\n\n- **Direction stability analysis is thorough and informative.** Tracking cosine similarity, held-out AUROC, and recalibration events across 6000 training steps (Table 7) provides a detailed picture of how representation-level rewards degrade under RL training. The sawtooth pattern with 4 recalibrations recovering only ~0.08 cosine each is a clear empirical characterization. The parallel degradation of held-out AUROC (0.753 to 0.642) concretely quantifies the practical impact.\n\n- **R1-only ablation demonstrates reward hacking.** The finding that R1-only achieves high R1 reward (0.72) but the worst behavioral outcomes (NoF 0.361, MMLU -3.7pp) with 34 identified reward hacking instances is a valuable cautionary result. The specific mechanism (lengthy hedging prefixes that project away from d_syc without reducing sycophancy) is well-characterized.\n\n- **Statistical testing is appropriate.** Paired bootstrap tests with 1000 samples are applied to all pairwise comparisons. The paper honestly reports that no trained method significantly outperforms any other (p > 0.34), rather than cherry-picking metrics or reframing marginal differences as successes.\n\n- **Cross-model transfer analysis adds scope.** Testing on Llama-3-8B with cross-direction cosine of 0.23 and transfer AUROC of 0.571 (near random) strengthens the claim that directions are model-specific artifacts rather than universal encodings.\n\n- **Three-way decomposition provides geometric insight.** The near-antiparallel relationship between d_syc and d_gen (cosine = -0.82) is a structurally important finding that constrains future work: it suggests that linear methods in this space are fundamentally limited because sycophancy and genuine revision occupy opposite ends of a single axis rather than independent dimensions.\n\n---\n\n## Weaknesses\n\n- **Single model family for the main training experiment.** DC-GRPO is trained only on Qwen3-8B. While the direction analysis extends to Llama-3-8B, the negative training result could be specific to Qwen3-8B's representation geometry. The direction AUROC is already lower on Llama (0.712 vs 0.753), so it is unclear whether the failure mode is identical. At minimum, the paper should discuss whether Qwen3-8B's specific architecture (e.g., GQA, RoPE implementation) could contribute to the instability. The negative claim \"representation-level rewards are not enough\" is framed as general but established on a single model.\n\n- **LoRA-only training may amplify direction instability.** LoRA constrains updates to a low-rank subspace, which could cause representation drift to be more concentrated and directionally aligned than full fine-tuning, making the sycophancy direction more sensitive to parameter updates. The paper acknowledges LoRA as a limitation but does not analyze whether the drift pattern would differ under full fine-tuning. Even a brief theoretical argument about how rank-64 LoRA interacts with the direction computation would strengthen the paper.\n\n- **Recalibration strategy is underexplored.** The paper uses a fixed threshold (cosine < 0.7) and recalibrates from the calibration dataset using the current checkpoint. Several alternatives are not explored or discussed: (a) more frequent recalibration (every 100-200 steps), (b) exponential moving average of directions, (c) projecting into the null space of the LoRA update, (d) using a held-out direction validation set to dynamically adjust recalibration frequency. The paper treats the recalibration failure as evidence against the approach, but it could equally be evidence of an undertuned mechanism. The 4 triggered recalibrations with only 0.08 cosine recovery each suggest the recalibration procedure itself is flawed (computing a new direction on a drifted model may yield a direction that is already partially invalidated).\n\n- **R1-R3 disagreement analysis has a circularity concern.** The 3.8% disagreement rate is interpreted as \"below the 5% threshold needed to support a meaningful representation-level advantage.\" However, this threshold was pre-specified in the experiment plan (exp-007) without justification for why 5% is the right cutoff. If the direction is already substantially degraded by mid-training (AUROC 0.642 at step 6000), low disagreement could reflect R1's reduced sensitivity rather than genuine absence of masked sycophancy. The analysis would be more convincing if disagreement rates were reported separately for early training (where direction quality is higher) versus late training. Table 8 partially addresses this (4.6% early vs 3.1% late), but the interpretation should acknowledge that declining disagreement is confounded with declining R1 accuracy.\n\n- **Manual review sample size is too small for confident conclusions.** The 50-case manual review of R1-sycophantic/R3-correct cases finding only 16% clear masked sycophancy (8 cases) has wide confidence intervals. With n=8 positives out of 50, the 95% Wilson CI is approximately [7.2%, 28.8%]. The paper draws strong conclusions (\"further undermining the case for representation-level advantage\") from an estimate that could plausibly range from 7% to 29%.\n\n- **The three-way decomposition uses too few neutral pairs.** Only 60 neutral pairs are used to compute d_gen. Given that the expanded calibration dataset uses 200 pairs (and the paper argues that 50 was insufficient for the MVP), 60 pairs for a separate direction seems underpowered. The resulting cosine of -0.82 should come with a confidence interval. If the CI is wide, the \"near-antiparallel\" claim is less definitive.\n\n- **Missing: reward weight sensitivity analysis.** The final weights (0.3/0.2/0.5) are stated without justification beyond \"prioritizing behavioral grounding.\" Were other weight configurations tested? The negative result could be specific to this weighting. If R1 is contributing noise by mid-training, a schedule that reduces w1 over time might mitigate the problem. The paper does not explore adaptive weighting.\n\n- **Missing: learning rate / LoRA rank sensitivity.** Both the LoRA rank (64) and learning rate (1.5e-5) could interact with direction stability. Higher LoRA rank = larger representational perturbations per step = potentially faster direction drift. The paper uses a single configuration without ablating these hyperparameters. A learning rate sweep (even 2-3 values) would help distinguish \"the approach fails\" from \"the approach fails at this training intensity.\"\n\n- **The double-bind analysis is descriptive but not diagnostic.** Table 16 shows that all methods reduce warranted revision (from 0.583 to 0.498-0.538), but the paper does not analyze why DC-GRPO does not improve this relative to R3-only (0.527 vs 0.538). Given that the core motivation is breaking the double-bind, a deeper analysis of where DC-GRPO's warranted revision failures occur (by evidence strength, turn depth, topic domain) would be informative.\n\n- **Turn depth analysis interpretation is oversimplified.** The paper claims DC-GRPO \"shows no differential advantage at any depth\" based on a consistent 1.5-2.1pp gap. However, the gradient (slope) for DC-GRPO (0.144) is essentially identical to R3-only (0.140) and other baselines. This is a useful null result, but the paper could note that the directional reward was designed to capture commitment-depth effects, so the identical slope is a specific falsification of the claimed mechanism, not just an absence of improvement.\n\n---\n\n## Questions for Authors\n\n1. **Direction recomputation procedure**: When recalibration is triggered, do you recompute d_syc using the same 200 calibration pairs with the current model checkpoint? If so, the new direction is computed on a model that has already drifted from the calibration distribution. Have you considered computing directions from fresh rollouts of the current policy?\n\n2. **R1-R3 correlation dynamics**: The correlation drops from 0.67 to 0.29. At what point during training does R1 become effectively random noise? Is there a principled stopping criterion where R1 should be dropped from the reward?\n\n3. **Reward hacking characterization**: The 34 reward hacking instances in R1-only training are mentioned but not analyzed in detail. What fraction of total R1-only outputs do these represent? Are they concentrated at specific training steps or uniformly distributed?\n\n4. **Why L24 as optimal layer?** The experiment plan notes L19 as the emergence layer from the MVP, but Table 1 shows L24 as the overall-AUROC-optimal layer for expanded data. The paper does not discuss this shift. Does the optimal layer change with evidence-strength composition, and does this affect the three-way decomposition?\n\n5. **Binary Probe robustness**: Table 17 shows the probe's AUROC also degrades (0.761 to 0.651) but the paper claims it is \"more robust\" than directional projection. What is the mechanism for this claimed robustness? Is it simply that the scalar output clips extreme projection values?\n\n---\n\n## Minor Issues\n\n- Table 3 (cross-model): The Qwen3-8B optimal layer is L24 here but L24 is also listed in Table 1. The paper_framing.md mentions L19 as the MVP emergence layer. The discrepancy between L19 (MVP, 50 weak-only pairs) and L24 (expanded, 200 mixed pairs) should be explicitly discussed, as it suggests the optimal layer is sensitive to calibration data composition.\n\n- The recalibration threshold is 0.7 in the method section, but 7 threshold crossings triggering only 4 recalibrations is unexplained. What determined when a crossing led to recalibration vs not?\n\n- The paper claims \"direction instability creates a fundamental problem\" (Section 4.3) but this language is strong given that only one recalibration strategy was tested. \"Creates a problem that our recalibration strategy did not resolve\" is more accurate.\n\n- Table 5 (training dynamics) and Table 7 (stability) show different cosine values at corresponding steps (e.g., step 2000: 0.68 in Table 5, 0.68 in Table 7 — consistent here, but the reader must cross-reference). Consolidating these into a single table would improve readability.\n\n- The abstract states \"AUROC dropping from 0.811 to 0.698 as evidence quality increases\" but this is across conditions, not a temporal degradation. The phrasing could be misread as a training-time phenomenon.\n\n---\n\n## Score: 4 (Weak Accept)\n\n**Justification**: This is a well-executed negative-result paper that provides genuine empirical value to the representation-level alignment community. The three identified failure modes (evidence-strength confounds, direction instability, near-antiparallel geometry) are clearly demonstrated and mechanistically analyzed. The evidence-strength stratification and direction stability tracking are methodological contributions independent of the negative outcome.\n\nThe paper falls short of a clear Accept (5) for several reasons: (1) the negative conclusion is established on a single model with a single LoRA configuration, leaving open the possibility that the failures are hyperparameter-specific rather than fundamental; (2) the recalibration strategy is underexplored, weakening the claim that direction instability is inherent rather than an engineering problem; (3) the small manual review sample (n=50) limits the R1-R3 disagreement conclusions; (4) missing sensitivity analyses (reward weights, learning rate, LoRA rank) leave uncertainty about whether the approach is fundamentally flawed or simply undertrained.\n\nHowever, it merits above Weak Reject because: (a) the experimental coverage is comprehensive (12 of 13 planned experiments completed); (b) the baselines are appropriate and fairly compared; (c) the statistical testing is honest and adequate; (d) the evidence-strength confound finding is important and novel; (e) the community benefits from well-characterized negative results at least as much as from marginal positive results.\n\n---\n\n## Confidence: 4/5\n\nI am confident in my assessment of the experimental methodology, statistical testing, and the identified weaknesses. My uncertainty is primarily around whether the negative results are truly fundamental limitations or artifacts of underexplored hyperparameter and design choices, which requires domain expertise in representation-level RL training that extends beyond what the paper provides.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee4c1812-667f-4b8a-8d9d-c21c5e1e07e2",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9yxCwuzomxdQuSVY1kg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49f20441-e114-4c17-949c-f2d9ae58aa74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y35UNuTaguTbbpVSAjeNXJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 741,
      "cache_read_input_tokens": 67219,
      "output_tokens": 3713,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 741
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3713,
          "cache_read_input_tokens": 67219,
          "cache_creation_input_tokens": 741,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 741,
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

_source line 43 · 2026-05-18T11:50:53.489Z_

<details><summary>↩ Tool result · `toolu_01RT75JGpsLJCw6naoRP3z9V`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/worst/review_report.md\", \"dream_id\": \"dream_20260518T110318\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49f20441-e114-4c17-949c-f2d9ae58aa74",
  "isSidechain": true,
  "promptId": "1560a173-81ed-4d4c-b805-0689957cc2fe",
  "agentId": "adbe9642b04ad0e22",
  "type": "user",
  "uuid": "1f338cce-cd5e-437c-917c-ffb4b556e01a",
  "sourceToolAssistantUUID": "49f20441-e114-4c17-949c-f2d9ae58aa74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-18T11:51:04.455Z_

Review submitted. Here is the summary:

**Score: 4 (Weak Accept) | Confidence: 4/5**

The review evaluates the "worst" scenario paper (negative results) across all requested dimensions:

**Key strengths identified:**
- Evidence-strength stratification (AUROC gradient from 0.811 weak to 0.698 strong) is a genuine methodological contribution that exposes confounds in prior work
- Direction stability analysis with cosine tracking, held-out AUROC, and recalibration events is thorough
- R1-only ablation demonstrating reward hacking (34 instances) is a valuable cautionary finding
- Statistical testing is honest: all pairwise p-values reported, no cherry-picking
- Comprehensive baseline coverage spanning the relevant design space
- Three-way decomposition (cosine = -0.82) provides structural geometric insight

**Key weaknesses identified:**
- Single model (Qwen3-8B) with single LoRA config; the "fundamental limitation" claim is overstated for n=1
- Recalibration strategy is underexplored (only one approach tested), so direction instability could be an engineering problem rather than inherent
- R1-R3 disagreement analysis has circularity: low disagreement could reflect R1's degraded accuracy rather than absence of masked sycophancy
- Manual review sample too small (n=50, only 8 positives) for confident conclusions
- Missing sensitivity analyses: reward weight schedules, learning rate, LoRA rank
- Three-way decomposition uses only 60 neutral pairs (underpowered by the paper's own standards)

The review was saved to `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/dream_reports/dream_20260518T110318/worst/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f338cce-cd5e-437c-917c-ffb4b556e01a",
  "isSidechain": true,
  "agentId": "adbe9642b04ad0e22",
  "requestId": "req_011Cb9z5mt1r7MvmJBvzhBff",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99d6e94e-c494-4f1f-8a53-d10ecbc92265",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "sessionId": "00408ad4-18c8-47de-8763-c4ca6904e068",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSmna2qMbjo9dpNQxBdtiR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3848,
      "cache_read_input_tokens": 67960,
      "output_tokens": 439,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3848
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 439,
          "cache_read_input_tokens": 67960,
          "cache_creation_input_tokens": 3848,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3848,
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
