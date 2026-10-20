# Research conversation: You are Reviewer 2 (R2) for an academic peer review. Your focus areas are **Novelty** and **Related Work**. Target venue

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a5ac0a7826a71f52a.jsonl`
- **Structured JSON:** [`161006b8ebd8ce845bcc.json`](../../sessions/16/161006b8ebd8ce845bcc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

51 recorded events

### User

_source line 1 · 2026-05-13T16:23:05.027Z_

You are Reviewer 2 (R2) for an academic peer review. Your focus areas are **Novelty** and **Related Work**. Target venue: AAAI 2027 (scale 1-10, acceptance rate ~17.6%).

## Paper Summary
**Title:** ContamCal: Calibrating Benchmark Scores for Training Data Contamination via Contamination-Augmented Item Response Theory

**Core idea:** A two-stage framework for post-hoc statistical calibration of LLM benchmark scores under training data contamination:
- Stage 1: Reciprocal Rank Fusion (RRF) of 4 detection signals (embedding retrieval, Min-K%++, ConStat, Self-Critique) → per-item exposure scores
- Stage 2: Contamination-augmented 4PL IRT model (Bayesian MCMC via Stan NUTS) → calibrated scores with credible intervals

**Key claims:**
1. ContamCal recovers true performance within 1.97pp MAE with 93% CI coverage (44% improvement over best baseline)
2. For RL-trained models, produces appropriately wider CIs (11.4pp vs 5.8pp); expected regret analysis shows 42% reduction
3. Graceful degradation to 2-signal mode for closed-weight models, still beats all baselines by 31%

## Method Details
- Problem formulation: estimate counterfactual ability θ* — the ability without contamination
- Stage 1 uses 4 training-free signals fused via RRF (Eq. 1) with c=60
- Stage 2: 4PL IRT with exposure covariate: P(Y_ij=1) = c_i + (d_i - c_i) / (1 + exp(-a_i(θ_j + γ·e_ji - b_i)))
- γ is global contamination effect; e_ji is per-item exposure from RRF
- Bayesian estimation via Stan NUTS
- Regime-conditional modeling: auto-degrades to 2-signal for RL models
- Grounded in educational measurement's item compromise IRT tradition [Eckerly 2017, Sinharay 2017]

## Related Work Section (from paper)
The paper's Related Work (Section 5) covers three areas:
1. **Contamination Detection:** Min-K%++ [Shi et al., 2024], ConStat [De Koninck et al., 2024], Self-Critique. "These methods flag contamination but do not produce calibrated scores."
2. **IRT for LLM Evaluation:** TinyBenchmarks [Polo et al., 2024], Growing Pains [Raju and Byrd, 2024], ATLAS [Bai et al., 2024]. "None incorporate contamination covariates."
3. **Contamination Mitigation:** Dong et al. [2025] tested 20 strategies and found none effective.
4. **Item Compromise IRT:** Eckerly [2017], Sinharay [2017].

Total references in paper: 10 citations.

## Key Contributions Claimed
1. The ContamCal framework: RRF provenance mapping → contamination-augmented 4PL IRT with Bayesian CIs
2. Dual-track validation: controlled SFT injection + ecological RL case study
3. Signal survival analysis across training regimes

## Key Results
- 1.97pp MAE vs 3.5pp best baseline (44% improvement)
- 93% CI coverage at 95% level
- RL regime: 42% regret reduction even with wider CIs
- 2-signal mode: still beats baselines by 31%
- Scale: validated 0.5B-7B controlled, 72B observational

## YOUR TASK

Provide a detailed review focused on:

### A. Novelty Assessment
1. How novel is the core idea of treating contamination as a covariate in IRT rather than trying to remove it? The paper claims this is analogous to causal inference's shift from eliminating confounders to adjusting for them.
2. How novel are the three structural modifications from educational IRT to LLM evaluation: (a) independent examinees → single model with joint item distributions, (b) binary leakage → continuous exposure scores, (c) stable ability → regime-conditional ability?
3. Is the RRF fusion of detection signals novel, or is this a straightforward application of existing techniques?
4. Is the regime-conditional modeling (auto-degradation for RL) a genuine contribution or an engineering decision?
5. What is the incremental novelty over simply doing "detection + remove-and-rescore"?

### B. Related Work Completeness
1. Is the related work section comprehensive enough? Note only 10 total citations.
2. Missing related work areas to check:
   - Other contamination detection methods beyond the 4 used (e.g., extraction attacks, membership inference)
   - Other IRT applications in NLP/ML beyond evaluation
   - Post-hoc calibration methods in general (e.g., Platt scaling, temperature scaling — are these relevant?)
   - Score adjustment / fairness calibration literature
   - Benchmark design papers (e.g., LiveBench, dynamic benchmarks)
   - Data provenance and attribution methods
3. Is the connection to educational measurement's item compromise IRT adequately developed?
4. Are there concurrent or very recent works (2025-2026) on contamination-aware evaluation that the paper should discuss?

### C. Positioning and Framing
1. Is the "statistical safety net" framing appropriate and well-motivated?
2. Does the paper adequately distinguish itself from prior work?
3. Is the scope of claims appropriate for the evidence presented?

### D. Significance and Impact
1. Would AAAI reviewers find this sufficiently impactful for a top venue?
2. Is the problem important enough? Is contamination actually the most pressing evaluation concern?
3. Would practitioners adopt this? What are the practical barriers?

### E. Weaknesses and Questions for Authors

### F. Overall Assessment
Provide scores on the AAAI 1-10 scale:
- Overall: X/10
- Soundness: X/5
- Significance: X/5
- Novelty: X/5
- Clarity: X/5
- Confidence: X/5

Format your review as a structured reviewer report.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "d0f1dabc-f3d5-4cc1-aef9-eeba4aea0330",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T16:23:05.031Z_

```json
{
  "parentUuid": "d0f1dabc-f3d5-4cc1-aef9-eeba4aea0330",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
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
  "uuid": "9e266c6f-e455-48a5-8f6a-a2e48a0f49b6",
  "timestamp": "2026-05-13T16:23:05.031Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-13T16:23:08.103Z_



I'll start by reading the paper and all related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e266c6f-e455-48a5-8f6a-a2e48a0f49b6",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011Cazso4h6QLJe9L73ZHDhB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0fb1cdb-77b9-473b-a193-b2970a8d5aa7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmkuTWeeTq7E2GuBDGckhh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7356,
      "cache_read_input_tokens": 8253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7356,
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

_source line 4 · 2026-05-13T16:23:09.682Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01ScUUuS7E6UM4uzHL69Sg3L`</summary>

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
  "parentUuid": "f0fb1cdb-77b9-473b-a193-b2970a8d5aa7",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011Cazso4h6QLJe9L73ZHDhB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7533be95-1e51-4f16-b2f0-08a576a3fdb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AmkuTWeeTq7E2GuBDGckhh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7356,
      "cache_read_input_tokens": 8253,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7356
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 125,
          "cache_read_input_tokens": 8253,
          "cache_creation_input_tokens": 7356,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7356,
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

_source line 5 · 2026-05-13T16:23:09.685Z_

<details><summary>↩ Tool result · `toolu_01ScUUuS7E6UM4uzHL69Sg3L`</summary>

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
  "parentUuid": "7533be95-1e51-4f16-b2f0-08a576a3fdb5",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "87743df3-2bfe-4df6-bab1-c908a08b8400",
  "sourceToolAssistantUUID": "7533be95-1e51-4f16-b2f0-08a576a3fdb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-13T16:23:13.501Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01MtTborFVn6xR2Baw4SHquB`</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87743df3-2bfe-4df6-bab1-c908a08b8400",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazsoRL53vuYH27utJGYX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c50d938d-54c2-49bb-bdb1-c7ea4f0d08b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XoozenErBPqfT41AJUJZFq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-13T16:23:13.531Z_

<details><summary>↩ Tool result · `toolu_01MtTborFVn6xR2Baw4SHquB`</summary>

```text
{"result":"# 项目 contamcal-irt-calibration 概况\n\n## 实验状态 (2 个)\n\n- **mvp_sim_4pl_gamma**: DONE (success) — \n- **mvp_sim_confounding**: RUNNING — \n\n## 最新报告\n# Handover — 2026-05-13\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| mvp_sim_confounding | 4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **mvp_sim_4pl_gamma** (success): 4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9\n\n## 趋势\n成功 1 / 负向 0 / 失败 0 / 共 1\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\n（无服务器配置）\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c50d938d-54c2-49bb-bdb1-c7ea4f0d08b9",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "d2d5a258-ca3f-47f5-a4b1-465c500bab74",
  "sourceToolAssistantUUID": "c50d938d-54c2-49bb-bdb1-c7ea4f0d08b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-13T16:23:14.530Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0166WDsmQpABTZnLH762p2yk`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2d5a258-ca3f-47f5-a4b1-465c500bab74",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazsoRL53vuYH27utJGYX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19d57b93-832d-44aa-afd3-2f163122dd00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XoozenErBPqfT41AJUJZFq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1447,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-13T16:23:14.541Z_

<details><summary>↩ Tool result · `toolu_0166WDsmQpABTZnLH762p2yk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"# Handover — 2026-05-13\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| mvp_sim_confounding | 4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_sim_4pl_gamma** (success): 4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9\\n\\n## 趋势\\n成功 1 / 负向 0 / 失败 0 / 共 1\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 642, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19d57b93-832d-44aa-afd3-2f163122dd00",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "717ae2e2-df37-4a18-9dfa-30f07a7582f6",
  "sourceToolAssistantUUID": "19d57b93-832d-44aa-afd3-2f163122dd00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-13T16:23:15.150Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AjZae4MmwaqvvTENsSPh3K`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "717ae2e2-df37-4a18-9dfa-30f07a7582f6",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazsoRL53vuYH27utJGYX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf1e23a1-f2ba-4829-a6dc-9279b8c24f17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XoozenErBPqfT41AJUJZFq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 15609,
      "output_tokens": 261,
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
          "output_tokens": 261,
          "cache_read_input_tokens": 15609,
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
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T16:23:15.163Z_

<details><summary>↩ Tool result · `toolu_01AjZae4MmwaqvvTENsSPh3K`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf1e23a1-f2ba-4829-a6dc-9279b8c24f17",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "0426c575-f8f1-4573-87a7-b9347ef4a472",
  "sourceToolAssistantUUID": "bf1e23a1-f2ba-4829-a6dc-9279b8c24f17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-13T16:23:18.440Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Lb2w8vp2XcRHwmTDyyWg57`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0426c575-f8f1-4573-87a7-b9347ef4a472",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazsopCEmGvx3VFxEFuPm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f22536dc-fe4c-4e7f-a09f-65b48dc5d872",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PqQNXJXnRF36PQ1MKzg38s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 17056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1307,
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

_source line 13 · 2026-05-13T16:23:18.451Z_

<details><summary>↩ Tool result · `toolu_01Lb2w8vp2XcRHwmTDyyWg57`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-13 15:51 UTC | 更新原因: MVP 完成，进入 Research 阶段，完成 paper_framing + experiment_plan + dream_simulate\\n\\n## 核心方向\\nContamCal：post-hoc statistical calibration for contamination-adjusted benchmark scores。两阶段：(1) RRF 融合 4 检测信号得到 per-item contamination exposure，(2) contamination-augmented 4PL IRT 输出校准分数 + credible intervals。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-13 通过）\\n- **MVP 结论**: 4PL+γ IRT 在合成数据上成功分离 γ 和 θ（γ rel_bias <8%, θ_corr >0.94, confounding 分离后残差相关 0.058）\\n- **关键发现**: 4PL 必要（2PL 结构性劣势）；NUTS 唯一可用推断方法（ADVI 废弃）；N_items≥300 必要\\n- **Dream**: dream_20260513T155040 进行中（full review mode）\\n- **GPU**: 待分配，已向 Manager 申请\\n- **实验计划**: 13 个实验（6 P0 + 5 P1 + 2 P2），详见 experiment_plan.yaml\\n\\n## 近期任务\\n- [ ] 等待 Dream 完成 → 分析审稿反馈 → 调整 framing/plan\\n- [ ] GPU 分配到位后启动 exp-001 (controlled SFT injection)\\n- [ ] 并行启动 exp-004 (simulation sweep, CPU only)\\n- [ ] exp-004 完成后启动 exp-005 (noise propagation, CPU only)\\n\\n## GPU 预算\\n- P0: 72h | P1: 57h | P2: 20h | Buffer: 30h | Total: ~179h\\n- 需要 2-4× H100/A100-80G\\n- 预估 wall-clock: 2-4 周取决于 GPU 数量\\n\\n## 投稿目标\\n- Primary: AAAI 2027（Jul-Aug 2026 deadline）\\n- Secondary: ICLR 2027（Sep 2026 deadline）\\n\\n## Core Claims (paper_framing.md)\\n1. **Calibration**: 4PL+γ IRT recovers true scores with low MAE + nominal CI coverage\\n2. **Signal Aggregation**: RRF fusion of 4 signals, training-free, graceful degradation\\n3. **Uncertainty Quantification**: Noise propagation + regime-appropriate CI widths\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D004 | 2026-05-13 | MVP 通过，进入 Research 阶段 | mvp_sim_4pl_gamma, mvp_sim_confounding |\\n| D003 | 2026-05-13 | Phase A PASS：4PL+γ 在 N_items=300 下成功分离 γ 和 θ；θ_RMS | mvp_sim_4pl_gamma |\\n| D002 | 2026-05-13 | 采纳 Reviewer 3 个 warning：扩展 simulation grid + 加 θ-e | — |\\n| D001 | 2026-05-13 | MVP 用 simulation identifiability test 验证 4PL+γ IRT | — |\\n\\n\\n\", \"total_chars\": 1898, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f22536dc-fe4c-4e7f-a09f-65b48dc5d872",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "6030839c-cc71-424a-8111-f1b593381cc7",
  "sourceToolAssistantUUID": "f22536dc-fe4c-4e7f-a09f-65b48dc5d872",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-13T16:23:18.919Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01GHZnXneod265ogHukvA4b1`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6030839c-cc71-424a-8111-f1b593381cc7",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazsopCEmGvx3VFxEFuPm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c82f2f5-aef1-4946-afb1-64cd996997ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PqQNXJXnRF36PQ1MKzg38s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 17056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1307,
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

_source line 15 · 2026-05-13T16:23:18.928Z_

<details><summary>↩ Tool result · `toolu_01GHZnXneod265ogHukvA4b1`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No memory.md found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c82f2f5-aef1-4946-afb1-64cd996997ca",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "6dea0ca8-b8e5-4adf-abe1-42ecddf66919",
  "sourceToolAssistantUUID": "7c82f2f5-aef1-4946-afb1-64cd996997ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-13T16:23:19.889Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01G4xFHZJKTXU9MyPGC2jAmu`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dea0ca8-b8e5-4adf-abe1-42ecddf66919",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazsopCEmGvx3VFxEFuPm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "156bd437-9256-4dde-9373-5367e728245e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PqQNXJXnRF36PQ1MKzg38s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 17056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1307,
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

_source line 17 · 2026-05-13T16:23:19.898Z_

<details><summary>↩ Tool result · `toolu_01G4xFHZJKTXU9MyPGC2jAmu`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "156bd437-9256-4dde-9373-5367e728245e",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "c7ca2017-d7bf-45f4-88db-61a3a880a039",
  "sourceToolAssistantUUID": "156bd437-9256-4dde-9373-5367e728245e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-13T16:23:20.321Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01AcfhmkwKQrQRjWUvyxTGXT`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7ca2017-d7bf-45f4-88db-61a3a880a039",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazsopCEmGvx3VFxEFuPm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9bf4c60-f632-4bb0-a58f-8a2ab569181e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PqQNXJXnRF36PQ1MKzg38s",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 17056,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1307
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 396,
          "cache_read_input_tokens": 17056,
          "cache_creation_input_tokens": 1307,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1307,
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

_source line 19 · 2026-05-13T16:23:20.331Z_

<details><summary>↩ Tool result · `toolu_01AcfhmkwKQrQRjWUvyxTGXT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/paper_framing.md\", \"content\": \"# Paper Framing — contamcal-irt-calibration\\n\\n## Target Venue\\n- Primary: AAAI 2027 (expected deadline: Jul-Aug 2026)\\n- Secondary: ICLR 2027 (expected deadline: Sep 2026)\\n- ~~EMNLP 2026 ARR May 25~~ (dropped, D001)\\n\\n## Core Insight\\nWhen benchmark mitigation strategies systematically fail (Emperor's New Clothes, ICML 2025: 20 strategies tested, none effective), the principled alternative is post-hoc statistical calibration — analogous to causal inference's shift from eliminating confounders to statistically controlling them. ContamCal instantiates this by augmenting IRT with contamination covariates, producing calibrated benchmark scores with Bayesian credible intervals. Theoretically grounded in educational measurement's item compromise IRT tradition (Eckerly 2017, Sinharay 2017), with 3 non-trivial adaptations for LLM evaluation.\\n\\n## Core Claims (3 条)\\n\\n1. **Calibration Claim**: ContamCal's contamination-augmented 4PL IRT model recovers true (uncontaminated) benchmark performance with low calibration error (MAE) and nominal credible interval coverage, validated on controlled SFT contamination injection experiments across 3+ model scales (0.5B-7B) and 4 benchmarks (MMLU, GSM8K, ARC-Challenge, HumanEval).\\n\\n2. **Signal Aggregation Claim**: Training-free RRF fusion of 4 complementary detection signals (embedding retrieval, Min-K%++, ConStat, Self-Critique) provides principled contamination exposure estimation without meta-circularity, outperforming any single signal and degrading gracefully under signal dropout — including a degraded 2-signal mode for closed-weight models.\\n\\n3. **Uncertainty Quantification Claim**: ContamCal explicitly propagates detection signal noise into calibration uncertainty — SFT-trained models receive tighter credible intervals (multiple reliable signals), RL-trained models receive appropriately wider intervals (primarily Self-Critique), and simulation-validated identifiability bounds establish minimum signal quality thresholds for reliable calibration.\\n\\n## Contributions (Hierarchical)\\n\\n### Core\\n1. ContamCal framework: two-stage pipeline (RRF provenance mapping → contamination-augmented 4PL IRT) producing calibrated scores with credible intervals\\n2. Dual-track validation: controlled SFT injection (internal validity) + ecological RL case study (external validity)\\n3. 5 baselines + 5 quantitative evaluation metrics for contamination-aware calibration\\n\\n### Supporting\\n4. Simulation-based identifiability study: systematic parameter sweep establishing minimum signal quality / model count thresholds\\n5. Signal survival analysis: systematic evaluation of which detection signals remain reliable after SFT vs. RL post-training (signal × regime AUC heatmap)\\n\\n## Story Spine\\n- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training (GRPO) further amplifies contamination effects and conceals detection signals. No existing method provides calibrated scores answering \\\"what would this model's score be if it had never seen the test data?\\\"\\n- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration as the principled alternative.\\n- **Our framing**: ContamCal is a \\\"statistical safety net\\\" for when mitigation is unreliable. Instead of trying to eliminate contamination from benchmarks (which doesn't work), we statistically control for it — measuring its effect and subtracting it out with proper uncertainty. This is grounded in educational measurement's item compromise IRT tradition, with 3 non-trivial structural adaptations: (a) independent examinees → single model with joint item distribution (changes local independence semantics), (b) binary leakage → continuous exposure scores (requires generalization), (c) stable ability → regime-conditional ability (SFT vs. RL require regime-aware modeling).\\n- **Headline result template**: \\\"On {benchmark}, ContamCal recovers true model performance within {X}% MAE with {Y}% credible interval coverage, while naive scores overestimate by {Z} points under {W}% contamination dosage. Even under noisy RL-regime detection (Self-Critique AUC ~0.65), calibrated scores with wider CIs improve model selection decisions by {R}% expected regret reduction.\\\"\\n\\n## Venue Fit Risks\\n- **AAAI**: Strong fit for Bayesian/probabilistic methods + empirical ML evaluation. Risk: reviewers less familiar with NLP contamination literature. Mitigation: emphasize general statistical methodology, frame as evaluation methodology contribution.\\n- **ICLR**: Strong fit for ML methodology + LLM evaluation. Risk: may expect stronger RL validation than observational case study. Mitigation: honest uncertainty quantification framing (\\\"wide CIs are the correct answer, not a limitation\\\").\\n- **Novelty ceiling**: Core method is synthesis of existing components (detection signals + IRT). Defense: cross-disciplinary transfer with 3 non-trivial adaptations + simulation-validated identifiability bounds as methodological contribution. Not \\\"engineering glue\\\" — each adaptation requires non-obvious modeling decisions.\\n- **RL \\\"so what\\\"**: RL models only get wide CIs. Defense: expected regret quantification shows even wide CIs improve model selection vs. naive scores.\\n\\n## Anticipated Reviewer Concerns & Defenses\\n\\n| # | Concern | Defense | Experiment |\\n|---|---------|---------|------------|\\n| 1 | θ and γ identifiable? | MVP validated: γ rel_bias <8%, θ_residual_exp_corr=0.058 at corr=0.38 | exp-004 (sweep) |\\n| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated | exp-003 (ablation) |\\n| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity) | exp-006, exp-009 |\\n| 4 | Scale limited to 3B | 7B controlled + 72B observational | exp-007, exp-012 |\\n| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d parameters necessary for realistic item modeling | exp-006 |\\n| 6 | Too few models (50)? | Few-examinee regime study + Growing Pains pre-estimation strategy | exp-011 |\\n| 7 | Noisy exposure scores | Noise propagation analysis: calibrated noise injection → CI widening quantified | exp-005 |\\n| 8 | No baselines | 5 baselines: remove-rescore, single-signal 2PL+γ, vanilla 4PL, linear regression+CI, Emperor's mitigations | exp-006 |\\n\\n## Evaluation Protocol (5 Metrics)\\n1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy\\n2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals\\n3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)\\n4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings\\n5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage\\n\\n## Benchmarks (4)\\n1. **MMLU** — knowledge-intensive multiple-choice (14K items)\\n2. **GSM8K** — mathematical reasoning free-form (~1.3K items)\\n3. **ARC-Challenge** — science reasoning multiple-choice\\n4. **HumanEval** — code generation with execution evaluation\\n- Day-8 contingency: reduce to MMLU + GSM8K\\n\\n## Baselines (5)\\n1. **Remove-and-rescore** — drop flagged items, rescore on remaining\\n2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT\\n3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)\\n4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)\\n5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)\\n\", \"total_chars\": 8116, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9bf4c60-f632-4bb0-a58f-8a2ab569181e",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "1d70407a-606a-4961-b30e-a15a61f0cfa8",
  "sourceToolAssistantUUID": "a9bf4c60-f632-4bb0-a58f-8a2ab569181e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-13T16:23:24.393Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WawpnbY43FgQoZevzykmcx`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d70407a-606a-4961-b30e-a15a61f0cfa8",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazspCFHzbsyiemHJNe6i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3a6283a-f279-45b8-848b-dac5eb3f795d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bvEf834FEs2vDx4hqkcWD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4172,
      "cache_read_input_tokens": 18363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 21 · 2026-05-13T16:23:24.405Z_

<details><summary>↩ Tool result · `toolu_01WawpnbY43FgQoZevzykmcx`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml\", \"content\": \"_next_id: 5\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:26 UTC\\n  summary: MVP 用 simulation identifiability test 验证 4PL+γ IRT 核心假设，放弃 EMNLP 2026 May\\n    ARR\\n  rationale: 核心假设是 γ 与 θ 可分离——这在合成数据上可验证，无需 GPU。12 天内完成完整论文不现实，目标改为 AAAI 2027 / ICLR\\n    2027。MVP 通过后再配置 GPU 进入 research 阶段。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:29 UTC\\n  summary: 采纳 Reviewer 3 个 warning：扩展 simulation grid + 加 θ-exposure confounding +\\n    加 FPR/FNR 噪声模型\\n  rationale: Reviewer 指出原 MVP simulation 条件过于理想化。θ-exposure confounding 是 γ identifiability\\n    的核心威胁，必须在 MVP 阶段覆盖。参数 grid 扩展（18 conditions）和 FPR/FNR 噪声增量成本约 4-8h CPU，不影响时间线。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 10:57 UTC\\n  summary: Phase A PASS：4PL+γ 在 N_items=300 下成功分离 γ 和 θ；θ_RMSE 阈值从 0.2 放宽至 0.30\\n  rationale: 'Variant A (N_items=300, 4PL NUTS): γ_rel_bias=6.8%, θ_corr=0.943, 收敛完美。N_items=100\\n    的 borderline fail 确认为信息量不足（c/d 参数估计需要更多 items），非方法论缺陷。θ_RMSE 阈值从 0.2 放宽至 0.30，Reviewer\\n    论证理论最优 SE≈0.18-0.26，0.2 在 N=50 models 下不可达。ADVI 在 4PL 上彻底失败（bad local mode），MVP\\n    阶段放弃 ADVI，仅用 NUTS。2PL+γ 在 4PL 生成数据上严重 misspecified（γ=0.16），确认 4PL 的必要性。'\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: primary\\n    result: Phase A PASS (Variant A)\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-13 15:45 UTC\\n  summary: MVP 通过，进入 Research 阶段\\n  rationale: Phase A (identifiability) 和 P2 (confounding robustness) 两个 gate 全部 PASS。4PL+γ\\n    NUTS 在 N_items=300 条件下 γ 相对偏差 <8%，θ 相关性 >0.94，混淆分离后残差相关 0.058。ADVI 和 2PL 被排除。核心假设\\\"IRT\\n    模型可分离污染效应与真实能力\\\"在合成数据上得到验证。\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: Phase A identifiability\\n    result: PASS at N_items=300\\n  - exp_id: mvp_sim_confounding\\n    role: P2 confounding robustness\\n    result: PASS with confound_corr=0.38\\n  depends_on:\\n  - D002\\n  - D003\\n\", \"total_chars\": 1844, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3a6283a-f279-45b8-848b-dac5eb3f795d",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "73565cf6-6fbd-4c07-9dc1-2b00008ad985",
  "sourceToolAssistantUUID": "e3a6283a-f279-45b8-848b-dac5eb3f795d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-13T16:23:25.345Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VMEghZtMvH4eFypP3hxXA3`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73565cf6-6fbd-4c07-9dc1-2b00008ad985",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazspCFHzbsyiemHJNe6i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14310fde-35dc-40df-aede-74f21a8a9137",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bvEf834FEs2vDx4hqkcWD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4172,
      "cache_read_input_tokens": 18363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 23 · 2026-05-13T16:23:25.354Z_

<details><summary>↩ Tool result · `toolu_01VMEghZtMvH4eFypP3hxXA3`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14310fde-35dc-40df-aede-74f21a8a9137",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "49816edc-683a-4705-b01c-eb63efc7a6e3",
  "sourceToolAssistantUUID": "14310fde-35dc-40df-aede-74f21a8a9137",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-13T16:23:26.758Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01EXdmLm4xcJyYH6UkWNUdnW`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49816edc-683a-4705-b01c-eb63efc7a6e3",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazspCFHzbsyiemHJNe6i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18818cae-4e57-4b3d-958c-80f86b978f30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bvEf834FEs2vDx4hqkcWD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4172,
      "cache_read_input_tokens": 18363,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4172,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 25 · 2026-05-13T16:23:26.803Z_

<details><summary>↩ Tool result · `toolu_01EXdmLm4xcJyYH6UkWNUdnW`</summary>

```text
artifacts/dream_reports/dream_20260513T155040/best/paper.tex
artifacts/dream_reports/dream_20260513T155040/median/paper.tex
artifacts/dream_reports/dream_20260513T155040/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18818cae-4e57-4b3d-958c-80f86b978f30",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "fce3c2bd-ff57-46ab-b801-2627a877649c",
  "sourceToolAssistantUUID": "18818cae-4e57-4b3d-958c-80f86b978f30",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-13T16:23:27.050Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FbAxftFLCRyKQTmLEPhACB`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fce3c2bd-ff57-46ab-b801-2627a877649c",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazspCFHzbsyiemHJNe6i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd9f1ce8-a0d4-4610-9566-cc5cb47ee1fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bvEf834FEs2vDx4hqkcWD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4172,
      "cache_read_input_tokens": 18363,
      "output_tokens": 374,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4172
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 374,
          "cache_read_input_tokens": 18363,
          "cache_creation_input_tokens": 4172,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4172,
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

_source line 27 · 2026-05-13T16:23:27.132Z_

<details><summary>↩ Tool result · `toolu_01FbAxftFLCRyKQTmLEPhACB`</summary>

```text
.venv/lib/python3.14/site-packages/pip/__init__.py
.venv/lib/python3.14/site-packages/pip/__main__.py
.venv/lib/python3.14/site-packages/pip/__pip-runner__.py
.venv/lib/python3.14/site-packages/pip/_internal/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/build_env.py
.venv/lib/python3.14/site-packages/pip/_internal/cache.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/autocompletion.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/base_command.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/cmdoptions.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/command_context.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/index_command.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/main.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/main_parser.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/parser.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/progress_bars.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/req_command.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/spinners.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/status_codes.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/cache.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/check.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/completion.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/debug.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/download.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/freeze.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/hash.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/help.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/index.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/inspect.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/install.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/list.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/lock.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/search.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/show.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/uninstall.py
.venv/lib/python3.14/site-packages/pip/_internal/commands/wheel.py
.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
.venv/lib/python3.14/site-packages/pip/_internal/distributions/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/distributions/base.py
.venv/lib/python3.14/site-packages/pip/_internal/distributions/installed.py
.venv/lib/python3.14/site-packages/pip/_internal/distributions/sdist.py
.venv/lib/python3.14/site-packages/pip/_internal/distributions/wheel.py
.venv/lib/python3.14/site-packages/pip/_internal/exceptions.py
.venv/lib/python3.14/site-packages/pip/_internal/index/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/index/collector.py
.venv/lib/python3.14/site-packages/pip/_internal/index/package_finder.py
.venv/lib/python3.14/site-packages/pip/_internal/index/sources.py
.venv/lib/python3.14/site-packages/pip/_internal/locations/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/locations/_distutils.py
.venv/lib/python3.14/site-packages/pip/_internal/locations/_sysconfig.py
.venv/lib/python3.14/site-packages/pip/_internal/locations/base.py
.venv/lib/python3.14/site-packages/pip/_internal/main.py
.venv/lib/python3.14/site-packages/pip/_internal/metadata/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/metadata/_json.py
.venv/lib/python3.14/site-packages/pip/_internal/metadata/base.py
.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_compat.py
.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_dists.py
.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_envs.py
.venv/lib/python3.14/site-packages/pip/_internal/metadata/pkg_resources.py
.venv/lib/python3.14/site-packages/pip/_internal/models/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/models/candidate.py
.venv/lib/python3.14/site-packages/pip/_internal/models/direct_url.py
.venv/lib/python3.14/site-packages/pip/_internal/models/format_control.py
.venv/lib/python3.14/site-packages/pip/_internal/models/index.py
.venv/lib/python3.14/site-packages/pip/_internal/models/installation_report.py
.venv/lib/python3.14/site-packages/pip/_internal/models/link.py
.venv/lib/python3.14/site-packages/pip/_internal/models/pylock.py
.venv/lib/python3.14/site-packages/pip/_internal/models/scheme.py
.venv/lib/python3.14/site-packages/pip/_internal/models/search_scope.py
.venv/lib/python3.14/site-packages/pip/_internal/models/selection_prefs.py
.venv/lib/python3.14/site-packages/pip/_internal/models/target_python.py
.venv/lib/python3.14/site-packages/pip/_internal/models/wheel.py
.venv/lib/python3.14/site-packages/pip/_internal/network/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/network/auth.py
.venv/lib/python3.14/site-packages/pip/_internal/network/cache.py
.venv/lib/python3.14/site-packages/pip/_internal/network/download.py
.venv/lib/python3.14/site-packages/pip/_internal/network/lazy_wheel.py
.venv/lib/python3.14/site-packages/pip/_internal/network/session.py
.venv/lib/python3.14/site-packages/pip/_internal/network/utils.py
.venv/lib/python3.14/site-packages/pip/_internal/network/xmlrpc.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/build_tracker.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata_editable.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata_legacy.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/wheel.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/wheel_editable.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/build/wheel_legacy.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/check.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/freeze.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/install/__init__.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/install/editable_legacy.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/install/wheel.py
.venv/lib/python3.14/site-packages/pip/_internal/operations/prepare.py
.venv/lib/python3.14/site-packages/pip/_internal/pyproject.py
.venv/lib/python3.14/site-packages/pip/_internal/req/__init__.py
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd9f1ce8-a0d4-4610-9566-cc5cb47ee1fa",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "74ec0094-db22-4ced-a8a0-e1f2fa209986",
  "sourceToolAssistantUUID": "dd9f1ce8-a0d4-4610-9566-cc5cb47ee1fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-13T16:23:29.939Z_

Let me read the dream review papers to understand the full paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74ec0094-db22-4ced-a8a0-e1f2fa209986",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011Cazsph8rjVudtFQCsNCuU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "718201a3-7d4e-4347-8887-1244590c38ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FmJ21cdTh9RVefKBx8Z2RM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4526,
      "cache_read_input_tokens": 22535,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4526,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 29 · 2026-05-13T16:23:32.511Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UauUCw7u5xT7wrpn61ZUcN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "718201a3-7d4e-4347-8887-1244590c38ea",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011Cazsph8rjVudtFQCsNCuU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9fe36f5-398a-40cb-a721-752bfec06a3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FmJ21cdTh9RVefKBx8Z2RM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4526,
      "cache_read_input_tokens": 22535,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4526
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 22535,
          "cache_creation_input_tokens": 4526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4526,
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

_source line 30 · 2026-05-13T16:23:32.882Z_

<details><summary>↩ Tool result · `toolu_01UauUCw7u5xT7wrpn61ZUcN`</summary>

```text
1	\documentclass[11pt,letterpaper]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{graphicx}
5	\usepackage{amsmath,amssymb}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{url}
10	\usepackage{natbib}
11	\usepackage{tabularx}
12	
13	\setcounter{secnumdepth}{2}
14	
15	\title{ContamCal: Calibrating Benchmark Scores for Training Data Contamination\\via Contamination-Augmented Item Response Theory}
16	
17	\author{
18	Anonymous Authors
19	}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	Benchmark scores for large language models are increasingly unreliable due to training data contamination, with recent work showing that all 20 tested mitigation strategies fail to eliminate score inflation.
26	We propose \textsc{ContamCal}, a post-hoc statistical calibration framework that treats contamination as a measurable covariate rather than a removable confound.
27	ContamCal operates in two stages: (1)~training-free Reciprocal Rank Fusion (RRF) of four complementary detection signals (embedding retrieval, Min-K\%++, ConStat, Self-Critique) to estimate per-item contamination exposure, and (2)~a contamination-augmented four-parameter logistic (4PL) Item Response Theory model fitted via Bayesian MCMC to produce calibrated scores with credible intervals.
28	On controlled SFT injection experiments across three model scales (0.5B--7B) and four benchmarks (MMLU, GSM8K, ARC-Challenge, HumanEval), ContamCal recovers true uncontaminated performance within 1.97 percentage points (pp) mean absolute error with 93\% credible interval coverage, while naive scores overestimate by 8--12pp.
29	This represents a 44\% relative improvement over the best baseline.
30	For RL-trained models where most detection signals degrade, ContamCal produces appropriately wider credible intervals (11.4pp vs.\ 5.8pp for SFT), and we show via expected regret analysis that even these uncertain calibrations reduce model selection regret by 42\% compared to uncalibrated scores.
31	The framework degrades gracefully to a 2-signal mode for closed-weight models, still outperforming all baselines by 31\%.
32	\end{abstract}
33	
34	\section{Introduction}
35	
36	Training data contamination---the inadvertent or deliberate inclusion of benchmark test items in model training data---undermines the validity of LLM evaluation.
37	Paraphrase-based contamination inflates MMLU accuracy by 8--15 percentage points while evading standard $n$-gram decontamination~\citep{yang2023rethinking,oren2024proving}.
38	RL post-training further amplifies contamination effects and conceals detection signals.
39	A recent systematic study tested 20 contamination mitigation strategies and found none effective~\citep{dong2024emperor}, leaving the community without a reliable path from observed benchmark scores to true model capability.
40	
41	Existing approaches address only part of the problem.
42	Detection methods (Min-K\%++, ConStat, Self-Critique) flag contamination but do not produce calibrated scores.
43	IRT-based evaluation methods model item difficulty and model ability jointly but ignore contamination~\citep{polo2024tinybenchmarks,raju2024growing,bai2024atlas}.
44	Remove-and-rescore approaches discard flagged items but lose statistical power and contamination-degree information.
45	No existing method answers the core question: \emph{``What would this model's score be if it had never seen the test data?''}
46	
47	We propose \textsc{ContamCal}, a ``statistical safety net'' for benchmark evaluation under contamination.
48	Rather than attempting to eliminate contamination---which demonstrably does not work---we statistically control for it, analogous to how causal inference shifted from eliminating confounders to adjusting for them.
49	Our approach is grounded in educational measurement's item compromise IRT tradition~\citep{eckerly2017detecting,sinharay2017detection}, adapted to LLM evaluation with three non-trivial structural modifications:
50	(a)~independent examinees $\to$ a single model with joint item distributions,
51	(b)~binary leakage $\to$ continuous exposure scores, and
52	(c)~stable ability $\to$ regime-conditional ability (SFT vs.\ RL).
53	
54	Our contributions are:
55	\begin{enumerate}
56	\item The ContamCal framework: a two-stage pipeline (RRF provenance mapping $\to$ contamination-augmented 4PL IRT) producing calibrated scores with Bayesian credible intervals.
57	\item Dual-track validation: controlled SFT injection (internal validity) and ecological RL case study (external validity), with 5 baselines and 5 quantitative evaluation metrics.
58	\item Signal survival analysis revealing which detection signals remain reliable after SFT vs.\ RL post-training, providing a practical signal selection guide.
59	\end{enumerate}
60	
61	\section{Method}
62	
63	\subsection{Problem Formulation}
64	
65	Let $Y_{ij} \in \{0,1\}$ denote the response of model $j$ to item $i$.
66	Standard IRT models this as $P(Y_{ij}=1) = f(\theta_j, \mathbf{b}_i)$ where $\theta_j$ is model ability and $\mathbf{b}_i$ are item parameters.
67	When item $i$ has been exposed during training, the observed performance conflates true ability with memorization.
68	We seek to estimate the \emph{counterfactual} ability $\theta_j^*$---the ability parameter that would be estimated had no contamination occurred.
69	
70	\subsection{Stage 1: RRF Exposure Estimation}
71	
72	We compute four training-free detection signals per model--item pair $(j,i)$:
73	
74	\paragraph{Embedding Retrieval.} We embed each test item and compute cosine similarity against a FAISS index of known training corpora. High similarity indicates potential exposure.
75	
76	\paragraph{Min-K\%++.} Following \citet{shi2024detecting}, we compute the average log-likelihood of the $k$\% lowest-probability tokens. Contaminated items exhibit higher Min-K\%++ scores due to reduced surprise.
77	
78	\paragraph{ConStat.} We measure the performance gap between original and paraphrased versions of each item~\citep{dekoninck2024constat}. Contaminated models show larger gaps because memorization does not transfer to paraphrases.
79	
80	\paragraph{Self-Critique.} The model is prompted to assess whether it has ``seen this question before,'' exploiting emergent metacognitive capabilities in instruction-tuned models.
81	
82	Each signal produces a per-item score $s_k(j,i)$ for $k \in \{1,2,3,4\}$.
83	We aggregate via Reciprocal Rank Fusion:
84	\begin{equation}
85	\text{RRF}(j,i) = \sum_{k=1}^{K} \frac{1}{c + r_k(j,i)}
86	\end{equation}
87	where $r_k(j,i)$ is the rank of item $i$ according to signal $k$ and $c=60$ is the standard smoothing constant.
88	The RRF score is normalized to $[0,1]$ to yield the exposure covariate $\gamma_{ji}$.
89	
90	\subsection{Stage 2: Contamination-Augmented 4PL IRT}
91	
92	We extend the standard 4PL model with an exposure covariate:
93	\begin{equation}
94	P(Y_{ij}=1) = c_i + \frac{d_i - c_i}{1 + \exp\bigl(-a_i(\theta_j + \gamma \cdot e_{ji} - b_i)\bigr)}
95	\label{eq:4plg}
96	\end{equation}
97	where $a_i$ is item discrimination, $b_i$ is item difficulty, $c_i$ is the guessing parameter, $d_i$ is the upper asymptote, $\theta_j$ is true model ability, $e_{ji}$ is the exposure score from Stage~1, and $\gamma$ is the contamination effect parameter.
98	
99	The key insight is that $\gamma \cdot e_{ji}$ captures the \emph{additive boost} to effective ability from contamination: a model that has memorized an item behaves as if it has higher ability on that item.
100	By jointly estimating $\theta_j$ and $\gamma$, we separate true ability from contamination-induced inflation.
101	
102	\paragraph{Bayesian Estimation.}
103	We place weakly informative priors:
104	$\theta_j \sim \mathcal{N}(0,1)$,
105	$\gamma \sim \mathcal{N}(0,1)$,
106	$a_i \sim \text{LogNormal}(0,0.5)$,
107	$b_i \sim \mathcal{N}(0,1)$,
108	$c_i \sim \text{Beta}(2,8)$,
109	$d_i \sim \text{Beta}(8,2)$.
110	The model is fitted via Stan NUTS with 4 chains, 2000 warmup and 2000 sampling iterations.
111	Posterior draws of $\theta_j$ yield calibrated score point estimates and credible intervals directly.
112	
113	\paragraph{Noise Propagation.}
114	The exposure scores $e_{ji}$ from Stage~1 are noisy.
115	We model this via a measurement error extension: $e_{ji}^{\text{obs}} = e_{ji}^{\text{true}} + \epsilon_{ji}$, $\epsilon_{ji} \sim \mathcal{N}(0, \sigma_e^2)$, where $\sigma_e$ is estimated from signal disagreement.
116	This naturally widens posterior credible intervals when exposure estimates are uncertain, rather than producing biased point estimates.
117	
118	\subsection{Regime-Conditional Modeling}
119	
120	RL post-training disrupts token-level memorization patterns, degrading embedding retrieval and Min-K\%++ signals while preserving higher-level signals (ConStat, Self-Critique).
121	For RL-trained models, ContamCal automatically degrades to a 2-signal mode using only the surviving signals.
122	The resulting wider credible intervals correctly reflect the greater uncertainty, rather than producing overconfident but inaccurate calibrations.
123	
124	\section{Experimental Setup}
125	
126	\subsection{Controlled SFT Injection}
127	\label{sec:sft-injection}
128	
129	We create ground-truth contaminated/clean model pairs via controlled SFT injection.
130	Qwen2.5 models at three scales (0.5B, 1.5B, 3B) are fine-tuned at five contamination dosage levels (0\%, 5\%, 25\%, 50\%, 100\%) using paraphrase-based injection across four benchmarks (MMLU, GSM8K, ARC-Challenge, HumanEval), yielding 15 contaminated/clean model pairs.
131	All 15 SFT runs converge successfully.
132	
133	\subsection{Baselines}
134	
135	We compare against five baselines:
136	(1)~\textbf{Remove-and-rescore}: drop flagged items and rescore on remaining items;
137	(2)~\textbf{Single-signal 2PL+$\gamma$}: best single detection signal with a simpler 2PL IRT model;
138	(3)~\textbf{Vanilla 4PL}: standard IRT without contamination covariate ($\gamma=0$);
139	(4)~\textbf{Linear regression + bootstrap CI}: simplest post-hoc adjustment using exposure scores as linear predictors;
140	(5)~\textbf{Emperor's mitigations}: rephrasing and option shuffling strategies from~\citet{dong2024emperor}.
141	
142	\subsection{Evaluation Metrics}
143	
144	We evaluate on five metrics:
145	(1)~\textbf{Calibration error}: MAE between calibrated and ground-truth clean accuracy;
146	(2)~\textbf{Interval coverage}: fraction of true values within credible intervals at 50\%/80\%/95\% levels;
147	(3)~\textbf{Interval sharpness}: average CI width;
148	(4)~\textbf{Ranking preservation}: Kendall's $\tau$ between calibrated and ground-truth rankings;
149	(5)~\textbf{Dose-response monotonicity}: Spearman correlation between dosage and estimated $\gamma$ effect.
150	
151	\section{Results}
152	
153	\subsection{Contamination Injection Ground Truth}
154	
155	Table~\ref{tab:injection} summarizes the accuracy inflation induced by controlled SFT injection.
156	Inflation is dose-dependent (Spearman $\rho = 0.97$ across all conditions) and substantial: at 50\% dosage, MMLU accuracy inflates by 9.3pp on average.
157	Smaller models exhibit larger inflation (0.5B: 10.8pp vs.\ 3B: 8.2pp at 50\% dosage), consistent with memorization consuming a larger fraction of limited capacity.
158	HumanEval shows the highest inflation (7.5pp at 25\% dosage) because code solutions are more amenable to exact memorization, while GSM8K shows the lowest (4.2pp) due to reasoning chain structure.
159	The nonlinear dose--response pattern (acceleration between 25\% and 50\%) supports our choice of nonlinear 4PL modeling over linear alternatives.
160	
161	\begin{table}[t]
162	\centering
163	\caption{Accuracy inflation (pp) by contamination dosage on MMLU. Cross-benchmark results at 25\% dosage shown in rightmost columns. All values averaged across three model scales.}
164	\label{tab:injection}
165	\begin{tabular}{lccccc}
166	\toprule
167	\textbf{Dosage} & \textbf{MMLU} & & \textbf{GSM8K} & \textbf{ARC} & \textbf{HumanEval} \\
168	\midrule
169	0\% & 0.0 & & --- & --- & --- \\
170	5\% & 2.1 & & --- & --- & --- \\
171	25\% & 5.8 & & 4.2 & 5.1 & 7.5 \\
172	50\% & 9.3 & & --- & --- & --- \\
173	100\% & 12.6 & & --- & --- & --- \\
174	\bottomrule
175	\end{tabular}
176	\end{table}
177	
178	\subsection{Detection Signal Quality}
179	
180	Table~\ref{tab:signals} reports per-signal AUC for distinguishing contaminated from clean items.
181	All four signals perform well above chance, with embedding retrieval achieving the highest mean AUC (0.88) due to semantic similarity preservation under paraphrase-based injection.
182	Signal pairwise rank correlations range from 0.28 to 0.52 (mean 0.38), confirming complementarity and justifying multi-signal fusion.
183	At low dosage (5\%), all signal AUCs decrease by approximately 0.1, reflecting the weaker statistical signal from fewer contaminated items.
184	
185	\begin{table}[t]
186	\centering
187	\caption{Detection signal AUC (mean across model scales) at SFT-contaminated dosage levels, and the RL regime.}
188	\label{tab:signals}
189	\begin{tabular}{lcccc}
190	\toprule
191	\textbf{Signal} & \textbf{SFT Mean} & \textbf{5\% Dose} & \textbf{RL} \\
192	\midrule
193	Embedding Retrieval & 0.88 & 0.76 & 0.55 \\
194	Min-K\%++ & 0.84 & 0.71 & 0.58 \\
195	ConStat & 0.82 & 0.68 & 0.67 \\
196	Self-Critique & 0.79 & 0.66 & 0.72 \\
197	\bottomrule
198	\end{tabular}
199	\end{table}
200	
201	\subsection{RRF Fusion Ablation}
202	
203	Table~\ref{tab:rrf} presents the RRF aggregation ablation.
204	Four-signal RRF achieves AUC 0.87, comparable to the best single signal (embedding retrieval, 0.88) but with substantially lower variance across benchmarks.
205	The key advantage of RRF is \emph{robustness}: while individual signals fluctuate across benchmarks (e.g., embedding retrieval drops to 0.80 on GSM8K), RRF maintains $\geq$0.85 consistently.
206	RRF outperforms rank averaging by 3pp AUC due to reciprocal rank weighting emphasizing high-confidence ranks.
207	
208	Under false positive injection, RRF degrades gracefully: AUC drops only 3pp at 10\% FP rate and 7pp at 20\% FP rate.
209	The 2-signal degraded mode (ConStat + Self-Critique) achieves AUC 0.78, 9pp below full RRF but well above chance, enabling closed-weight deployment.
210	The RRF exposure score correlates strongly with true dosage (Spearman $\rho = 0.91$), confirming that the composite score captures contamination degree.
211	
212	\begin{table}[t]
213	\centering
214	\caption{RRF aggregation ablation. Best single = embedding retrieval. $\dagger$2-signal mode uses ConStat + Self-Critique only.}
215	\label{tab:rrf}
216	\begin{tabular}{lcc}
217	\toprule
218	\textbf{Method} & \textbf{AUC} & \textbf{$\rho$ (dosage)} \\
219	\midrule
220	RRF (4-signal) & 0.87 & 0.91 \\
221	Rank Averaging & 0.84 & --- \\
222	Calibration-Weighted RRF & 0.86 & --- \\
223	Best Single Signal & 0.88 & --- \\
224	2-Signal Degraded$^\dagger$ & 0.78 & --- \\
225	\midrule
226	\multicolumn{3}{l}{\textit{FP Injection Robustness}} \\
227	RRF @ 10\% FP & 0.84 & --- \\
228	RRF @ 20\% FP & 0.80 & --- \\
229	\bottomrule
230	\end{tabular}
231	\end{table}
232	
233	\subsection{Main Calibration Results}
234	
235	Table~\ref{tab:main} presents the core calibration comparison.
236	ContamCal achieves 1.97pp mean MAE across four benchmarks, a 44\% relative improvement over the best baseline (linear regression, 3.5pp).
237	The 95\% credible intervals achieve 93\% coverage with 5.8pp average width, demonstrating both reliability and sharpness.
238	Kendall's $\tau = 0.91$ confirms that calibrated rankings closely preserve ground-truth model ordering.
239	
240	Vanilla 4PL without the contamination covariate performs worst (MAE 6.1pp), confirming that the $\gamma$ parameter is essential.
241	Emperor's mitigation strategies achieve only 5.7pp MAE, consistent with the finding that mitigation approaches are systematically ineffective.
242	Remove-and-rescore (4.2pp) loses information by binarizing contamination flags.
243	Single-signal 2PL+$\gamma$ (3.8pp) shows that both multi-signal fusion and 4PL complexity contribute to ContamCal's advantage.
244	
245	MCMC diagnostics confirm reliable inference: 0\% divergent transitions, $\hat{R} < 1.01$, minimum ESS $> 800$.
246	The posterior correlation between $\theta$ and $\gamma$ is 0.31, below the 0.4 identifiability threshold, confirming that ability and contamination effects are separable.
247	
248	\begin{table*}[t]
249	\centering
250	\caption{Main calibration results: ContamCal vs.\ 5 baselines. MAE in percentage points (lower is better). Coverage and CI width for 95\% credible intervals. $\tau$: Kendall's rank correlation with ground truth. Best results in \textbf{bold}.}
251	\label{tab:main}
252	\begin{tabular}{lccccccccc}
253	\toprule
254	\textbf{Method} & \textbf{MMLU} & \textbf{GSM8K} & \textbf{ARC} & \textbf{HumanEval} & \textbf{Mean MAE} & \textbf{Cov.\ 95\%} & \textbf{CI Width} & $\boldsymbol{\tau}$ \\
255	\midrule
256	\textsc{ContamCal} (4PL+$\gamma$) & \textbf{1.8} & \textbf{2.1} & \textbf{1.6} & \textbf{2.4} & \textbf{1.97} & \textbf{0.93} & 5.8 & \textbf{0.91} \\
257	Linear Regression + CI & --- & --- & --- & --- & 3.5 & --- & --- & --- \\
258	Single-Signal 2PL+$\gamma$ & --- & --- & --- & --- & 3.8 & --- & --- & --- \\
259	Remove-and-Rescore & --- & --- & --- & --- & 4.2 & --- & --- & --- \\
260	Emperor's Mitigations & --- & --- & --- & --- & 5.7 & --- & --- & --- \\
261	Vanilla 4PL ($\gamma$=0) & --- & --- & --- & --- & 6.1 & --- & --- & --- \\
262	\midrule
263	Naive (uncalibrated) & \multicolumn{4}{c}{overestimation: 8--12pp at 50\% dosage} & 9.3 & --- & --- & --- \\
264	\bottomrule
265	\end{tabular}
266	\end{table*}
267	
268	\begin{table}[t]
269	\centering
270	\caption{Per-benchmark detailed metrics for ContamCal.}
271	\label{tab:perbench}
272	\begin{tabular}{lcccc}
273	\toprule
274	\textbf{Benchmark} & \textbf{MAE} & \textbf{Cov.\ 95} & \textbf{CI Width} & $\boldsymbol{\tau}$ \\
275	\midrule
276	MMLU & 1.8 & 0.93 & --- & 0.91 \\
277	GSM8K & 2.1 & --- & --- & --- \\
278	ARC-Challenge & 1.6 & --- & --- & --- \\
279	HumanEval & 2.4 & --- & --- & --- \\
280	\midrule
281	Mean & 1.97 & 0.93 & 5.8 & 0.91 \\
282	\bottomrule
283	\end{tabular}
284	\end{table}
285	
286	\subsection{Noise Propagation Analysis}
287	
288	Table~\ref{tab:noise} demonstrates ContamCal's robustness to noisy exposure scores.
289	Under matched noise (estimated from per-signal FP/FN rates: Self-Critique FP=12\%, FN=18\%), credible intervals widen to 5.2pp with 94\% coverage and only 6\% relative bias in $\gamma$.
290	At $2\times$ noise, CI width increases to 8.9pp but coverage rises to 97\% (slight overcoverage rather than undercoverage), and $\gamma$ bias remains at 9\%.
291	The $\theta$ correlation with ground truth decreases from 0.94 to 0.89, a graceful degradation.
292	The measurement error model improves DIC by 12.3, confirming that explicit noise modeling is statistically warranted.
293	
294	\begin{table}[t]
295	\centering
296	\caption{Noise propagation: impact of exposure score noise on calibration. $\gamma$ bias is relative.}
297	\label{tab:noise}
298	\begin{tabular}{lccccc}
299	\toprule
300	\textbf{Noise} & $\boldsymbol{\gamma}$ \textbf{Bias} & \textbf{CI Width} & \textbf{Cov.\ 95} & $\boldsymbol{\theta}$ \textbf{Corr.} \\
301	\midrule
302	None (oracle) & --- & --- & 0.93 & 0.95 \\
303	Matched & 0.06 & 5.2 & 0.94 & 0.94 \\
304	$1.5\times$ & --- & 6.8 & 0.96 & --- \\
305	$2\times$ & 0.09 & 8.9 & 0.97 & 0.89 \\
306	\bottomrule
307	\end{tabular}
308	\end{table}
309	
310	\subsection{Scale Bridging: 7B and 72B}
311	
312	\paragraph{7B Controlled Validation.}
313	Extending the controlled SFT injection to Qwen2.5-7B, ContamCal achieves 2.2pp MAE (+0.3pp vs.\ 3B models) with 92\% coverage and Kendall's $\tau = 0.89$.
314	The 7B model shows lower contamination inflation (7.6pp at 50\% dosage vs.\ 9.3pp mean for smaller models), consistent with stronger generalization diluting the relative contamination effect.
315	The estimated $\gamma = 0.38$ is correspondingly lower than the 0.42 observed at smaller scales.
316	
317	\paragraph{72B Observational Analysis.}
318	Applying ContamCal to Qwen2.5-72B in inference-only mode (no SFT injection), we find $\gamma = 0.18$ on MMLU with credible interval excluding zero, suggesting detectable contamination even at frontier scale.
319	On GSM8K, the $\gamma$ credible interval includes zero, consistent with reasoning benchmarks being less susceptible to memorization at this scale.
320	The calibrated MMLU score shifts downward by 3.2pp---a substantive but plausible correction.
321	The wider CI (8.5pp) appropriately reflects the greater uncertainty in this observational setting.
322	
323	\begin{table}[t]
324	\centering
325	\caption{Scale bridging results. 7B: controlled SFT injection. 72B: observational (inference-only).}
326	\label{tab:scale}
327	\begin{tabular}{lccccc}
328	\toprule
329	\textbf{Scale} & \textbf{MAE} & \textbf{Cov.\ 95} & $\boldsymbol{\gamma}$ & \textbf{CI excl.\ 0?} \\
330	\midrule
331	0.5B--3B & 1.97 & 0.93 & 0.42 & Yes \\
332	7B & 2.2 & 0.92 & 0.38 & Yes \\
333	72B (MMLU) & --- & --- & 0.18 & Yes \\
334	72B (GSM8K) & --- & --- & 0.12 & No \\
335	\bottomrule
336	\end{tabular}
337	\end{table}
338	
339	\subsection{Signal Survival Across Training Regimes}
340	
341	Table~\ref{tab:signal-regime} presents a signal $\times$ regime AUC heatmap revealing a critical pattern: RL post-training creates a ``signal desert'' where only ConStat and Self-Critique survive.
342	Embedding retrieval drops from 0.88 (SFT-contaminated) to 0.55 (RL) because policy gradient updates disrupt token-level memorization patterns.
343	Min-K\%++ similarly degrades from 0.84 to 0.58.
344	In contrast, Self-Critique \emph{improves} under RL (0.72 vs.\ 0.79 under SFT) because RL enhances metacognitive capabilities, and ConStat retains moderate discriminability (0.67) by measuring a higher-level performance gap that does not depend on model internals.
345	
346	On clean models (base or SFT without contamination), ConStat and Self-Critique correctly produce near-chance AUC (0.50), confirming specificity---no contamination signal is detected when none exists.
347	
348	\begin{table}[t]
349	\centering
350	\caption{Signal $\times$ regime AUC heatmap. Bold: best signal per regime.}
351	\label{tab:signal-regime}
352	\begin{tabular}{lcccc}
353	\toprule
354	\textbf{Signal} & \textbf{Base} & \textbf{SFT-Clean} & \textbf{SFT-Cont.} & \textbf{RL} \\
355	\midrule
356	Embedding & \textbf{0.90} & 0.51 & \textbf{0.88} & 0.55 \\
357	Min-K\%++ & 0.86 & 0.53 & 0.84 & 0.58 \\
358	ConStat & 0.50 & 0.50 & 0.82 & 0.67 \\
359	Self-Critique & 0.50 & 0.50 & 0.79 & \textbf{0.72} \\
360	\bottomrule
361	\end{tabular}
362	\end{table}
363	
364	\subsection{RL Case Study: Wide CIs as the Correct Answer}
365	
366	For eight RL-trained models (Qwen2.5-Instruct and DeepSeek-R1-Distill series), ContamCal produces 95\% credible intervals averaging 11.4pp---nearly $2\times$ the SFT width of 5.8pp (Table~\ref{tab:rl}).
367	This is not a failure mode but the \emph{correct} response to reduced signal availability (2 vs.\ 4 signals) and higher noise.
368	
369	We quantify the practical value of these wide-CI calibrations using expected regret for top-5 model selection.
370	Uncalibrated selection incurs expected regret of 0.38; ContamCal's wide-CI calibration reduces this to 0.22 (42\% reduction), substantially outperforming remove-and-rescore (0.31, 29\% reduction by ContamCal).
371	Even with wide CIs, the calibrated point estimates are directionally more accurate than naive scores, enabling better model selection despite high uncertainty.
372	
373	A specificity check on known-clean benchmarks yields $\gamma = 0.03 \approx 0$, confirming that ContamCal does not produce false contamination alarms.
374	
375	\begin{table}[t]
376	\centering
377	\caption{RL case study: expected regret for top-5 model selection. Lower regret is better.}
378	\label{tab:rl}
379	\begin{tabular}{lccc}
380	\toprule
381	\textbf{Method} & \textbf{Regret} & \textbf{Reduction} & $\boldsymbol{\tau}$ \textbf{(top-5)} \\
382	\midrule
383	Uncalibrated (naive) & 0.38 & --- & --- \\
384	Remove-and-Rescore & 0.31 & 18\% & --- \\
385	\textsc{ContamCal} (wide CI) & \textbf{0.22} & \textbf{42\%} & 0.80 \\
386	\bottomrule
387	\end{tabular}
388	\end{table}
389	
390	\begin{table}[t]
391	\centering
392	\caption{CI width comparison: SFT vs.\ RL regime.}
393	\label{tab:cicomp}
394	\begin{tabular}{lcccc}
395	\toprule
396	\textbf{Regime} & \textbf{CI Width (95\%)} & $\boldsymbol{\gamma}$ & $\boldsymbol{\gamma}$ \textbf{SD} & \textbf{Signals} \\
397	\midrule
398	SFT & 5.8pp & 0.42 & 0.08 & 4 \\
399	RL & 11.4pp & 0.28 & 0.14 & 2 \\
400	\bottomrule
401	\end{tabular}
402	\end{table}
403	
404	\subsection{Prior Sensitivity Analysis}
405	
406	Table~\ref{tab:prior} evaluates robustness to the $\gamma$ prior specification.
407	Across three priors ($\mathcal{N}(0,0.5)$, $\mathcal{N}(0,1)$, $\mathcal{N}(0,2)$), the maximum MAE difference is only 0.13pp and Kendall's $\tau$ is virtually unchanged (0.90--0.91).
408	The tight prior slightly understimates $\gamma$ (0.39 vs.\ 0.42) with narrower CIs (4.9pp) and lower coverage (91\%).
409	The wide prior allows larger $\gamma$ (0.44) with wider CIs (7.1pp) and higher coverage (95\%).
410	The default prior $\mathcal{N}(0,1)$ achieves the best coverage--sharpness trade-off.
411	These results demonstrate that the data likelihood dominates the prior, addressing potential concerns about prior sensitivity.
412	
413	\begin{table}[t]
414	\centering
415	\caption{Prior sensitivity for $\gamma \sim \mathcal{N}(0,\sigma_0)$.}
416	\label{tab:prior}
417	\begin{tabular}{lccccc}
418	\toprule
419	$\boldsymbol{\sigma_0}$ & \textbf{MAE} & \textbf{Cov.\ 95} & \textbf{CI Width} & $\boldsymbol{\gamma}$ & $\boldsymbol{\tau}$ \\
420	\midrule
421	0.5 (tight) & 2.1 & 0.91 & 4.9 & 0.39 & 0.90 \\
422	1.0 (default) & 1.97 & 0.93 & 5.8 & 0.42 & 0.91 \\
423	2.0 (wide) & 2.0 & 0.95 & 7.1 & 0.44 & 0.91 \\
424	\bottomrule
425	\end{tabular}
426	\end{table}
427	
428	\subsection{Few-Examinee Regime}
429	
430	A practical concern is whether ContamCal requires an impractically large model pool.
431	Table~\ref{tab:fewex} shows calibration performance as the number of models decreases from 200 to 20, with and without a two-stage pre-estimation strategy that uses item parameters pre-estimated from a large external pool (e.g., Growing Pains' 400+ model evaluations) as informative priors.
432	
433	Without pre-estimation, $N=20$ yields unacceptable MAE (4.8pp).
434	With pre-estimation, $N=20$ improves to 2.9pp---a 1.9pp benefit.
435	At $N=50$, pre-estimation reduces MAE from 2.8 to 2.1pp.
436	By $N=100$, the benefit vanishes (0.1pp) as the data alone suffices.
437	We recommend $N \geq 50$ with pre-estimation as the minimum viable configuration, achieving 92\% coverage and 8\% $\gamma$ relative bias.
438	
439	\begin{table}[t]
440	\centering
441	\caption{Few-examinee regime study. Pre-est.\ = item parameter pre-estimation from external model pool.}
442	\label{tab:fewex}
443	\begin{tabular}{lcccc}
444	\toprule
445	\textbf{$N$ models} & \textbf{Pre-est.?} & \textbf{MAE} & \textbf{Cov.\ 95} & $\boldsymbol{\gamma}$ \textbf{Bias} \\
446	\midrule
447	20 & No & 4.8 & --- & --- \\
448	20 & Yes & 2.9 & 0.90 & 0.12 \\
449	50 & No & 2.8 & --- & --- \\
450	50 & Yes & 2.1 & 0.92 & 0.08 \\
451	100 & No & 2.0 & 0.93 & --- \\
452	100 & Yes & 1.9 & 0.93 & --- \\
453	200 & No & 1.7 & --- & --- \\
454	200 & Yes & 1.7 & --- & --- \\
455	\bottomrule
456	\end{tabular}
457	\end{table}
458	
459	\subsection{Closed-Weight 2-Signal Mode}
460	
461	For closed-weight models where embedding retrieval and Min-K\%++ are unavailable, ContamCal degrades to ConStat + Self-Critique only.
462	Table~\ref{tab:2sig} compares this mode against the full 4-signal pipeline.
463	The 2-signal mode achieves 2.4pp MAE---a 10\% relative increase---with wider CIs (7.2pp) that maintain 94\% coverage.
464	Critically, the 2-signal mode still outperforms the best baseline by 31\% (2.4pp vs.\ 3.5pp), demonstrating practical value even without access to model internals.
465	
466	\begin{table}[t]
467	\centering
468	\caption{2-signal (closed-weight) vs.\ 4-signal mode.}
469	\label{tab:2sig}
470	\begin{tabular}{lcccc}
471	\toprule
472	\textbf{Mode} & \textbf{MAE} & \textbf{Cov.\ 95} & \textbf{CI Width} & $\boldsymbol{\tau}$ \\
473	\midrule
474	4-signal (full) & 1.97 & 0.93 & 5.8 & 0.91 \\
475	2-signal (closed) & 2.4 & 0.94 & 7.2 & 0.87 \\
476	\midrule
477	Best baseline & 3.5 & --- & --- & --- \\
478	\bottomrule
479	\end{tabular}
480	\end{table}
481	
482	\section{Related Work}
483	
484	\paragraph{Contamination Detection.}
485	Min-K\%++~\citep{shi2024detecting} detects memorized sequences via token log-likelihood.
486	ConStat~\citep{dekoninck2024constat} uses original--paraphrase performance gaps.
487	Self-Critique prompts models for metacognitive leakage assessment.
488	These methods flag contamination but do not produce calibrated scores.
489	
490	\paragraph{IRT for LLM Evaluation.}
491	TinyBenchmarks~\citep{polo2024tinybenchmarks} uses IRT for efficient evaluation.
492	Growing Pains~\citep{raju2024growing} applies IRT at scale.
493	ATLAS~\citep{bai2024atlas} provides adaptive testing.
494	None incorporate contamination covariates.
495	
496	\paragraph{Contamination Mitigation.}
497	\citet{dong2024emperor} systematically evaluated 20 mitigation strategies (rephrasing, option shuffling, etc.) and found none effective, motivating post-hoc calibration.
498	
499	\paragraph{Item Compromise IRT.}
500	In educational measurement, \citet{eckerly2017detecting} and \citet{sinharay2017detection} model item compromise as covariates in IRT.
501	ContamCal adapts this tradition with three structural modifications for LLM evaluation.
502	
503	\section{Conclusion}
504	
505	We presented ContamCal, a statistical calibration framework that recovers true benchmark performance under training data contamination.
506	By combining multi-signal contamination detection with contamination-augmented Bayesian IRT, ContamCal achieves 1.97pp MAE with 93\% CI coverage---a 44\% improvement over the best baseline---while naive scores overestimate by 8--12pp.
507	The framework handles the RL regime through appropriately wider credible intervals that still reduce model selection regret by 42\%, and degrades gracefully to a 2-signal mode for closed-weight models.
508	
509	Key limitations include: (1)~controlled validation is limited to SFT injection up to 7B scale; (2)~the RL case study provides observational evidence with wider CIs rather than controlled ground truth; (3)~the current implementation requires at least 50 models for reliable estimation.
510	Future work includes extending to larger-scale controlled experiments, developing signal-specific priors for different training regimes, and integration with dynamic benchmark rotation.
511	
512	\bibliography{references}
513	\bibliographystyle{plainnat}
514	
515	\end{document}
516	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9fe36f5-398a-40cb-a721-752bfec06a3c",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "d1e739d1-60d5-4c72-a0eb-2c956a62b522",
  "sourceToolAssistantUUID": "d9fe36f5-398a-40cb-a721-752bfec06a3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-13T16:23:37.018Z_

Now let me also read the other dream review versions to understand variance in quality.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1e739d1-60d5-4c72-a0eb-2c956a62b522",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011Cazsq7vcua4ecZHemqhKV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "228080fd-ce91-4c5f-b6af-12c4f55e02e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRFY2zFRfJ3jiTburebD7z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11307,
      "cache_read_input_tokens": 27061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11307,
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

_source line 32 · 2026-05-13T16:23:39.242Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VJTQn4PXapLJqZaDTCZf35`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/worst/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "228080fd-ce91-4c5f-b6af-12c4f55e02e4",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011Cazsq7vcua4ecZHemqhKV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66c7c49d-ed3e-40d5-86de-57d28f90cbc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRFY2zFRfJ3jiTburebD7z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11307,
      "cache_read_input_tokens": 27061,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11307,
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

_source line 33 · 2026-05-13T16:23:39.533Z_

<details><summary>↩ Tool result · `toolu_01VJTQn4PXapLJqZaDTCZf35`</summary>

```text
1	\documentclass[letterpaper, 10pt, twocolumn]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage{natbib}
11	
12	\frenchspacing
13	
14	\title{Empirical Identifiability Boundaries for\\Contamination-Aware IRT Calibration of LLM Benchmarks}
15	
16	\author{Anonymous}\date{}
17	
18	\begin{document}
19	\maketitle
20	
21	% ============================================================
22	\begin{abstract}
23	Benchmark contamination---the inclusion of test items in language model training data---inflates reported performance and undermines model comparison.
24	While contamination \emph{detection} methods have proliferated, the downstream question of whether detected contamination can be \emph{corrected} via statistical calibration remains open.
25	We investigate this question through the lens of Item Response Theory (IRT) augmented with a contamination covariate~$\gamma$.
26	Rather than claiming that calibration solves the contamination problem, we systematically map the \emph{identifiability boundaries} under which contamination-aware IRT calibration is feasible.
27	Through controlled SFT injection experiments across four model scales (0.5B--7B), four benchmarks (MMLU, GSM8K, ARC-Challenge, HumanEval), and four detection signals, we establish three key findings:
28	(1)~calibration is identifiable only when detection signal AUC exceeds~0.70 and the number of evaluated models exceeds~80---conditions rarely met in practice;
29	(2)~post-training via reinforcement learning degrades all detection signals below the identifiability threshold (average AUC drops from~0.72 to~0.56), rendering calibration infeasible for RL-trained models;
30	(3)~identifiability degrades with model scale, creating a fundamental tension where the largest models---most in need of calibration---are precisely those where calibration is least feasible.
31	These findings reframe contamination-aware calibration from a solved problem to a conditionally feasible one, and provide concrete signal quality targets for future detection research.
32	\end{abstract}
33	
34	% ============================================================
35	\section{Introduction}
36	
37	Benchmark scores are the primary currency for comparing large language models (LLMs), yet mounting evidence shows that training data contamination inflates these scores substantially.
38	Paraphrased test items can increase MMLU accuracy by 8 or more percentage points while evading standard $n$-gram decontamination~\citep{yang2023rethinking}.
39	The \emph{Emperor's New Clothes}~\citep{oren2025emperor} study tested 20~mitigation strategies and found none effective, motivating a shift from contamination \emph{elimination} to statistical \emph{calibration}.
40	
41	A natural framework for such calibration is Item Response Theory (IRT), the psychometric workhorse for modeling examinee ability from item responses.
42	By augmenting IRT with a contamination covariate~$\gamma$ drawn from the educational measurement literature on compromised items~\citep{eckerly2017detecting,sinharay2017detection}, one can---in principle---recover uncontaminated benchmark scores with Bayesian credible intervals.
43	
44	However, this paper asks a prior question: \textbf{under what conditions is such calibration actually identifiable?}
45	We argue that before building a calibration system, the field must understand \emph{when} it can work.
46	Our investigation reveals that the answer depends on a confluence of factors---detection signal quality, model count, model scale, and post-training regime---and that for many practical scenarios, the answer is ``not yet.''
47	
48	\paragraph{Contributions.}
49	\begin{enumerate}
50	\item An \textbf{empirical identifiability map} characterizing the joint requirements on signal AUC and model count for contamination-aware IRT calibration, validated against controlled experiments.
51	\item A \textbf{signal survival analysis} demonstrating that post-training regimes (SFT, RL) systematically degrade detection signals, with RL pushing all signals below the identifiability threshold.
52	\item \textbf{Controlled SFT injection experiments} across four model scales and four benchmarks providing ground-truth validation that the identifiability boundaries predicted by simulation match real-world conditions.
53	\item \textbf{Practical identifiability thresholds}: signal AUC~$\geq 0.70$, model count~$N \geq 80$, and confidence interval width~$< 15$~pp as minimum requirements for useful calibration.
54	\end{enumerate}
55	
56	% ============================================================
57	\section{Background and Related Work}
58	
59	\paragraph{Contamination detection.}
60	Multiple detection methods have been proposed: embedding-based retrieval~\citep{dodge2021documenting}, Min-K\%++~\citep{shi2024detecting}, ConStat~\citep{dekoninck2024constat}, and Self-Critique~\citep{weller2024selfcritique}.
61	Each produces item-level scores indicating contamination likelihood.
62	
63	\paragraph{IRT for LLM evaluation.}
64	IRT has been applied to LLM benchmarking by several recent works: PSN-IRT~\citep{polo2024tinybenchmarks}, Growing Pains~\citep{bhattpain}, ATLAS~\citep{zhuang2024atlas}, and HiBayES~\citep{paganini2024hibayes}.
65	None of these model contamination as a latent variable.
66	
67	\paragraph{Contamination mitigation.}
68	DCR~\citep{yang2023rethinking} adjusts accuracy for detected contamination but lacks uncertainty quantification.
69	The Emperor's New Clothes~\citep{oren2025emperor} comprehensively demonstrates that existing mitigation strategies (rephrasing, option shuffling, etc.) fail to reliably eliminate contamination effects.
70	
71	\paragraph{Item compromise in educational testing.}
72	Our approach builds on the IRT item compromise literature~\citep{eckerly2017detecting,sinharay2017detection}, which models the effect of leaked exam items on test scores.
73	We identify three structural differences when adapting this framework to LLMs: (a)~independent examinees become a single model with joint item distributions, (b)~binary leakage becomes continuous exposure scores, and (c)~stable ability becomes regime-conditional ability.
74	
75	% ============================================================
76	\section{Method: ContamCal Framework}
77	
78	We describe the contamination-aware IRT calibration framework, not to claim it solves calibration, but to define the system whose identifiability boundaries we study.
79	
80	\subsection{Stage 1: Detection Signal Aggregation}
81	
82	For each item $i$ and model $j$, we compute four detection signals:
83	\textbf{(1)~Embedding Retrieval}: cosine similarity between the item embedding and the nearest neighbor in the model's training data proxy;
84	\textbf{(2)~Min-K\%++}: normalized token-level surprise;
85	\textbf{(3)~ConStat}: performance gap between original and paraphrased items;
86	\textbf{(4)~Self-Critique}: entropy-based self-evaluation consistency.
87	
88	These are fused via Reciprocal Rank Fusion (RRF):
89	\begin{equation}
90	s_{ij} = \sum_{k=1}^{K} \frac{1}{r_{ij}^{(k)} + c}
91	\end{equation}
92	where $r_{ij}^{(k)}$ is the rank of item $i$ under signal $k$ for model $j$, and $c=60$ is the standard RRF constant.
93	
94	\subsection{Stage 2: Contamination-Augmented 4PL IRT}
95	
96	We augment the four-parameter logistic (4PL) IRT model with a contamination covariate~$\gamma$:
97	\begin{equation}
98	P(Y_{ij} = 1 \mid \theta_j, \gamma_j) = c_i + \frac{d_i - c_i}{1 + \exp(-a_i(\theta_j + \gamma_j s_{ij} - b_i))}
99	\end{equation}
100	where $\theta_j$ is the uncontaminated ability of model $j$, $\gamma_j$ is the contamination effect, $s_{ij}$ is the RRF exposure score, $a_i$ is item discrimination, $b_i$ is item difficulty, $c_i$ is the guessing parameter, and $d_i$ is the ceiling parameter.
101	
102	The model is fit via Hamiltonian Monte Carlo (Stan), yielding posterior distributions over $\theta_j$ and $\gamma_j$ and hence calibrated scores with Bayesian credible intervals.
103	
104	% ============================================================
105	\section{Experiments}
106	
107	All experiments use the Qwen2.5 model family.
108	Controlled experiments inject contamination via paraphrase SFT at five dosage levels (0\%, 5\%, 25\%, 50\%, 100\%).
109	We evaluate on MMLU, GSM8K, ARC-Challenge, and HumanEval.
110	
111	% ---- Experiment 1: Controlled SFT Injection ----
112	\subsection{Controlled SFT Injection}
113	\label{sec:sft_injection}
114	
115	We train 15 SFT runs (3 model scales $\times$ 5 dosage levels) to establish ground-truth contamination effects.
116	
117	\begin{table}[t]
118	\centering
119	\caption{Score inflation (accuracy \%) by model scale, benchmark, and contamination dosage. Inflation is monotonic (Spearman $\rho = 0.90$ on MMLU) but inversely related to model scale: Qwen-0.5B shows 11.5~pp inflation at 100\% dosage vs.\ 5.2~pp for Qwen-3B.}
120	\label{tab:sft_inflation}
121	\small
122	\begin{tabular}{llccccc}
123	\toprule
124	Model & Bench. & 0\% & 5\% & 25\% & 50\% & 100\% \\
125	\midrule
126	\multirow{4}{*}{0.5B}
127	& MMLU & 42.3 & 43.5 & 45.8 & 49.1 & 53.8 \\
128	& GSM8K & 31.2 & 31.5 & 32.8 & 34.1 & 36.3 \\
129	& ARC-C & 38.1 & 38.6 & 40.2 & 42.5 & 45.9 \\
130	& HumanEval & 22.0 & 22.1 & 23.0 & 24.2 & 25.9 \\
131	\midrule
132	\multirow{4}{*}{1.5B}
133	& MMLU & 53.1 & 53.6 & 54.8 & 56.5 & 59.7 \\
134	& GSM8K & 48.5 & 48.8 & 49.9 & 51.8 & 53.2 \\
135	& ARC-C & 52.0 & 52.4 & 53.5 & 55.1 & 57.8 \\
136	& HumanEval & 35.4 & 35.6 & 36.5 & 37.8 & 39.1 \\
137	\midrule
138	\multirow{4}{*}{3B}
139	& MMLU & 61.8 & 62.1 & 63.0 & 64.5 & 67.0 \\
140	& GSM8K & 62.3 & 62.5 & 63.1 & 64.2 & 65.8 \\
141	& ARC-C & 60.5 & 60.8 & 61.6 & 63.0 & 65.2 \\
142	& HumanEval & 48.2 & 48.4 & 49.0 & 50.1 & 52.1 \\
143	\bottomrule
144	\end{tabular}
145	\end{table}
146	
147	Table~\ref{tab:sft_inflation} presents the full inflation matrix.
148	Two patterns emerge that challenge a simple additive contamination model.
149	First, inflation magnitude is inversely related to model scale: Qwen-0.5B gains 11.5~pp at 100\% dosage on MMLU, while Qwen-3B gains only 5.2~pp.
150	Second, low-dosage contamination (5\%) produces inflation below 1~pp---indistinguishable from random seed noise---meaning that the regime where calibration would be most valuable (mild contamination) is precisely where contamination effects are hardest to detect.
151	The variance across seeds is 2.8~pp, further complicating detection of small effects.
152	
153	% ---- Experiment 2: Signal Quality ----
154	\subsection{Detection Signal Quality}
155	\label{sec:signal_quality}
156	
157	\begin{table}[t]
158	\centering
159	\caption{Detection signal AUC by dosage level (averaged across models and benchmarks). Only Embedding Retrieval at 100\% dosage reaches the 0.70 identifiability threshold. All signals degrade severely at low dosage.}
160	\label{tab:signal_auc_dosage}
161	\small
162	\begin{tabular}{lcccc}
163	\toprule
164	Signal & 5\% & 25\% & 50\% & 100\% \\
165	\midrule
166	Embedding Retrieval & 0.54 & 0.62 & 0.68 & 0.72 \\
167	Min-K\%++ & 0.52 & 0.58 & 0.64 & 0.68 \\
168	ConStat & 0.51 & 0.57 & 0.62 & 0.66 \\
169	Self-Critique & 0.51 & 0.55 & 0.59 & 0.63 \\
170	\bottomrule
171	\end{tabular}
172	\end{table}
173	
174	\begin{table}[t]
175	\centering
176	\caption{Signal AUC by model scale at 100\% dosage (MMLU). Larger models produce weaker detection signals, with Embedding Retrieval dropping from 0.75 (0.5B) to 0.69 (3B).}
177	\label{tab:signal_auc_scale}
178	\small
179	\begin{tabular}{lccc}
180	\toprule
181	Signal & Qwen-0.5B & Qwen-1.5B & Qwen-3B \\
182	\midrule
183	Embedding Retrieval & 0.75 & 0.73 & 0.69 \\
184	Min-K\%++ & 0.71 & 0.68 & 0.65 \\
185	ConStat & 0.69 & 0.67 & 0.63 \\
186	Self-Critique & 0.58 & 0.64 & 0.66 \\
187	\bottomrule
188	\end{tabular}
189	\end{table}
190	
191	Tables~\ref{tab:signal_auc_dosage}--\ref{tab:signal_auc_scale} reveal a fundamental catch-22: signal AUC is positively correlated with contamination dosage, meaning the signals are strongest precisely when contamination is most obvious and calibration is least needed.
192	At 5\% dosage---the regime of greatest practical interest---all signals have AUC $\leq 0.54$, barely above random.
193	The average AUC across all conditions is 0.61 with low inter-benchmark variance (0.008), indicating this is a systematic signal quality ceiling rather than a benchmark-specific artifact.
194	Min-K\%++ has a false positive rate of 0.45 at 90\% recall, and Self-Critique achieves only Cohen's $d = 0.41$ in entropy separation.
195	
196	% ---- Experiment 3: Signal Aggregation ----
197	\subsection{Signal Aggregation Analysis}
198	\label{sec:rrf}
199	
200	\begin{table}[t]
201	\centering
202	\caption{Aggregation method comparison (AUC at 100\% dosage, MMLU). RRF fusion does \emph{not} outperform the best single signal (Embedding Retrieval), indicating insufficient signal complementarity. Average pairwise correlation $r = 0.58$.}
203	\label{tab:rrf_comparison}
204	\small
205	\begin{tabular}{lcc}
206	\toprule
207	Method & AUC & $\Delta$ vs.\ best single \\
208	\midrule
209	Embedding Retrieval (best single) & 0.72 & --- \\
210	Min-K\%++ & 0.68 & $-$0.04 \\
211	ConStat & 0.66 & $-$0.06 \\
212	Self-Critique & 0.63 & $-$0.09 \\
213	\midrule
214	RRF (4-signal) & 0.70 & $-$0.02 \\
215	Rank Average (4-signal) & 0.69 & $-$0.03 \\
216	Weighted RRF (calibrated) & 0.71 & $-$0.01 \\
217	2-signal degraded (CS+SC) & 0.64 & $-$0.08 \\
218	\bottomrule
219	\end{tabular}
220	\end{table}
221	
222	\begin{table}[t]
223	\centering
224	\caption{RRF AUC across dosage levels. The fusion advantage is negligible at all dosage levels; at 100\% dosage, the best single signal (0.72) outperforms RRF (0.70).}
225	\label{tab:rrf_dosage}
226	\small
227	\begin{tabular}{lcccc}
228	\toprule
229	Method & 5\% & 25\% & 50\% & 100\% \\
230	\midrule
231	RRF 4-signal & 0.55 & 0.60 & 0.65 & 0.70 \\
232	Best single & 0.54 & 0.62 & 0.68 & 0.72 \\
233	2-signal degraded & 0.52 & 0.56 & 0.59 & 0.64 \\
234	\bottomrule
235	\end{tabular}
236	\end{table}
237	
238	Tables~\ref{tab:rrf_comparison}--\ref{tab:rrf_dosage} demonstrate that RRF fusion fails to outperform the best single signal.
239	The pairwise signal correlation of $r = 0.58$ explains this: signals share $\sim$34\% of their variance, providing insufficient complementary information for fusion to help.
240	The 2-signal degraded mode (ConStat + Self-Critique), representing the closed-weight scenario, drops to AUC~0.64.
241	Injecting 20\% false positives causes a 0.09 AUC drop, indicating high sensitivity to noise.
242	These results establish that \emph{signal diversity}---not just signal quality---is a prerequisite for effective aggregation.
243	
244	% ---- Experiment 4: Core Calibration ----
245	\subsection{Core Calibration Results}
246	\label{sec:calibration}
247	
248	\begin{table}[t]
249	\centering
250	\caption{Calibration MAE (pp) by method and benchmark. Linear regression+CI achieves the lowest average MAE (7.2~pp), outperforming the more complex 4PL+$\gamma$ (7.8~pp). No pairwise differences are statistically significant ($p > 0.05$).}
251	\label{tab:calibration_mae}
252	\small
253	\begin{tabular}{lccccc}
254	\toprule
255	Method & MMLU & GSM8K & ARC-C & HE & Avg \\
256	\midrule
257	4PL+$\gamma$ (ours) & 6.5 & 9.2 & 7.1 & 8.4 & 7.8 \\
258	Remove-rescore & 7.2 & 8.8 & 7.5 & 8.9 & 8.1 \\
259	Single-sig. 2PL+$\gamma$ & 6.2 & 8.5 & 7.0 & 8.3 & 7.5 \\
260	Vanilla 4PL & 8.1 & 10.5 & 8.8 & 9.4 & 9.2 \\
261	Linear reg.+CI & 5.8 & 8.2 & 6.9 & 7.9 & 7.2 \\
262	Emperor mitigation & 7.8 & 10.2 & 8.2 & 9.4 & 8.9 \\
263	\bottomrule
264	\end{tabular}
265	\end{table}
266	
267	\begin{table}[t]
268	\centering
269	\caption{Interval quality metrics. 4PL+$\gamma$ achieves only 78\% empirical coverage at the nominal 95\% level (undercoverage), with average CI width of 19.5~pp. Linear regression+CI provides both better coverage and narrower intervals.}
270	\label{tab:interval_quality}
271	\small
272	\begin{tabular}{lcccc}
273	\toprule
274	Method & Cov.\ 95\% & Cov.\ 80\% & Width 95\% & $\tau$ \\
275	\midrule
276	4PL+$\gamma$ & 0.78 & 0.62 & 19.5 & 0.62 \\
277	Linear reg.+CI & 0.83 & 0.70 & 16.2 & 0.65 \\
278	Single-sig.\ 2PL+$\gamma$ & 0.80 & 0.65 & 17.8 & 0.60 \\
279	\bottomrule
280	\end{tabular}
281	\end{table}
282	
283	\begin{table}[t]
284	\centering
285	\caption{Dose-response $\gamma$ estimates. The contamination effect is identifiable only at 50\%+ dosage. At 5\% and 25\%, the 95\% CI includes zero, meaning the model cannot distinguish contamination from noise.}
286	\label{tab:dose_response}
287	\small
288	\begin{tabular}{lcccc}
289	\toprule
290	Dosage & $\hat{\gamma}$ & 95\% CI & Excl.\ zero? \\
291	\midrule
292	5\% & 0.04 & [$-$0.18, 0.26] & No \\
293	25\% & 0.11 & [$-$0.08, 0.31] & No \\
294	50\% & 0.22 & [0.01, 0.44] & Yes \\
295	100\% & 0.38 & [0.12, 0.65] & Yes \\
296	\bottomrule
297	\end{tabular}
298	\end{table}
299	
300	Tables~\ref{tab:calibration_mae}--\ref{tab:dose_response} present the central negative result: the contamination-augmented 4PL IRT model does not significantly outperform simpler baselines.
301	Linear regression+bootstrap CI achieves the best average MAE (7.2~pp vs.\ 7.8~pp for 4PL+$\gamma$; paired $t$-test $p = 0.23$), with better interval coverage (83\% vs.\ 78\% at nominal 95\%) and tighter intervals (16.2~pp vs.\ 19.5~pp).
302	
303	The dose-response analysis (Table~\ref{tab:dose_response}) reveals that $\gamma$ is identifiable only at $\geq$50\% dosage.
304	The $\gamma$--$\theta$ posterior correlation of 0.52 directly evidences the confounding between ability and contamination: the model cannot reliably distinguish ``the model knows the answer'' from ``the model memorized the answer.''
305	Stan diagnostics show 3.2\% divergent transitions and $\hat{R}_{\max} = 1.08$, suggesting posterior geometry difficulties consistent with near-unidentifiability.
306	
307	The dose-response curve is not fully monotonic (Spearman $\rho = 0.55$), with 55\% of conditions yielding $\gamma$ CIs that include zero.
308	These findings establish that at realistic signal quality levels, IRT model complexity is counterproductive---the additional parameters amplify estimation noise rather than capturing real structure.
309	
310	% ---- Experiment 5: Noise Propagation ----
311	\subsection{Noise Propagation Analysis}
312	\label{sec:noise}
313	
314	\begin{table}[t]
315	\centering
316	\caption{CI width and coverage under noise injection. At matched noise level (1$\times$), 78\% of conditions have CI width exceeding the 15~pp practical threshold. The measurement error model converges but does not resolve the fundamental signal quality problem.}
317	\label{tab:noise_propagation}
318	\small
319	\begin{tabular}{lcccc}
320	\toprule
321	Noise & $\gamma$ CI (pp) & $\theta$ CI (pp) & Cov.\ 95\% & Cov.\ 80\% \\
322	\midrule
323	Baseline (0$\times$) & 18.0 & 12.0 & 0.82 & 0.68 \\
324	Matched (1$\times$) & 22.5 & 15.8 & 0.88 & 0.74 \\
325	1.5$\times$ & 28.0 & 20.5 & 0.93 & 0.82 \\
326	2$\times$ & 35.2 & 27.1 & 0.97 & 0.90 \\
327	Meas.\ error model & 24.0 & 17.2 & 0.90 & 0.76 \\
328	\bottomrule
329	\end{tabular}
330	\end{table}
331	
332	Table~\ref{tab:noise_propagation} quantifies the pathway from signal noise to calibration futility.
333	Even at baseline (no additional noise), the $\gamma$ CI width is 18.0~pp, already exceeding any reasonable practical threshold.
334	At matched noise (1$\times$, corresponding to Self-Critique's estimated FP rate of 35\% and FN rate of 28\%), the CI inflates to 22.5~pp, and 78\% of conditions exceed the 15~pp threshold.
335	Coverage increases with noise (from 0.82 to 0.97) not because calibration improves, but because intervals widen---a model producing a 95\% CI of [$42.5\%, 77.5\%$] for a 60\% accuracy model is technically ``calibrated'' but practically useless.
336	
337	This analysis yields an operational definition of \emph{practical identifiability}: the regime where CI width $< 15$~pp, which requires signal AUC $> 0.70$ under current noise conditions.
338	
339	% ---- Experiment 6: Prior Sensitivity ----
340	\subsection{Prior Sensitivity Analysis}
341	\label{sec:prior}
342	
343	\begin{table}[t]
344	\centering
345	\caption{Prior sensitivity of $\gamma$ estimation. MAE varies by 2.3~pp (30\% of point estimate) across prior choices, confirming that data are insufficiently informative to override the prior---a hallmark of under-identification.}
346	\label{tab:prior_sensitivity}
347	\small
348	\begin{tabular}{lcccc}
349	\toprule
350	Prior & $\hat{\gamma}$ & MAE (pp) & Cov.\ 95\% & Width (pp) \\
351	\midrule
352	$\mathcal{N}(0, 0.5)$ & 0.22 & 9.5 & 0.85 & 15.2 \\
353	$\mathcal{N}(0, 1.0)$ [default] & 0.38 & 7.8 & 0.78 & 19.5 \\
354	$\mathcal{N}(0, 2.0)$ & 0.51 & 7.2 & 0.72 & 24.8 \\
355	\bottomrule
356	\end{tabular}
357	\end{table}
358	
359	Table~\ref{tab:prior_sensitivity} demonstrates that calibration results are highly sensitive to the $\gamma$ prior.
360	The tight prior $\mathcal{N}(0, 0.5)$ shrinks $\hat{\gamma}$ by 45\%, while the wide prior $\mathcal{N}(0, 2.0)$ inflates it by 35\%.
361	MAE ranges from 7.2 to 9.5~pp across prior choices---a 2.3~pp sensitivity range representing 30\% of the point estimate.
362	In a well-identified model, the posterior should be dominated by the likelihood rather than the prior; this sensitivity is a direct symptom of weak signal informativeness (prior sensitivity index = 0.38).
363	
364	% ---- Experiment 7: Few-Examinee Regime ----
365	\subsection{Few-Examinee Regime}
366	\label{sec:few_examinee}
367	
368	\begin{table}[t]
369	\centering
370	\caption{Identifiability metrics by number of evaluated models at signal AUC = 0.65. $\gamma$ becomes statistically significant at $N \geq 80$; nominal coverage requires $N \geq 150$. Growing Pains pre-estimation provides only marginal improvement ($\leq$15\% at $N=20$) because the bottleneck is $\gamma$--$\theta$ confounding, not item parameter estimation.}
371	\label{tab:few_examinee}
372	\small
373	\begin{tabular}{lccccc}
374	\toprule
375	$N$ & $\gamma$ RMSE & Rel.\ bias & $\theta$ corr.\ & Cov.\ 95\% & GP $\Delta$ \\
376	\midrule
377	20 & 0.42 & 55\% & 0.58 & 68\% & +15\% \\
378	50 & 0.28 & 38\% & 0.72 & 75\% & +10\% \\
379	100 & 0.18 & 25\% & 0.82 & 80\% & +5\% \\
380	200 & 0.12 & 18\% & 0.88 & 85\% & +3\% \\
381	\bottomrule
382	\end{tabular}
383	\end{table}
384	
385	Table~\ref{tab:few_examinee} presents a simulation study of identifiability as a function of model count, fixing signal AUC at 0.65 (the level observed in our controlled experiments).
386	At $N = 20$---a common scenario for benchmark evaluation---$\gamma$ relative bias reaches 55\% and coverage drops to 68\%.
387	Even at $N = 200$, relative bias remains at 18\% and coverage at 85\%, still below the nominal 95\%.
388	The Growing Pains pre-estimation strategy~\citep{bhattpain}, which borrows item parameter priors from a larger pool, provides diminishing returns ($+3\%$ at $N = 200$) because the bottleneck is $\gamma$--$\theta$ joint estimation, which cannot be resolved by better item priors alone.
389	
390	The minimum model count for $\gamma$ statistical significance is $N = 80$; for nominal coverage, $N = 150$.
391	These thresholds, combined with the signal AUC requirement of $\geq 0.70$, define the joint identifiability boundary.
392	
393	% ---- Experiment 8: Signal Survival ----
394	\subsection{Signal Survival Analysis}
395	\label{sec:survival}
396	
397	\begin{table}[t]
398	\centering
399	\caption{Detection signal AUC across training regimes. RL degrades all signals below the 0.70 identifiability threshold (average survival rate 73\%). The best RL-regime signal (Self-Critique, 0.57) provides negligible discrimination. ANOVA confirms a significant regime effect ($p = 0.002$).}
400	\label{tab:signal_survival}
401	\small
402	\begin{tabular}{lcccc}
403	\toprule
404	Signal & Base & SFT-Clean & SFT-Contam & RL \\
405	\midrule
406	Embedding Retrieval & 0.78 & 0.72 & 0.72 & 0.60 \\
407	Min-K\%++ & 0.73 & 0.65 & 0.68 & 0.55 \\
408	ConStat & 0.71 & 0.63 & 0.66 & 0.53 \\
409	Self-Critique & 0.60 & 0.58 & 0.63 & 0.57 \\
410	\bottomrule
411	\end{tabular}
412	\end{table}
413	
414	\begin{table}[t]
415	\centering
416	\caption{Signal survival rate (AUC retention relative to base model). Self-Critique shows paradoxical stability (95\% retention under RL) only because it starts from a low baseline (0.60). Post-training degradation is systematic, not signal-specific.}
417	\label{tab:survival_rate}
418	\small
419	\begin{tabular}{lccc}
420	\toprule
421	Signal & SFT-Clean & SFT-Contam & RL \\
422	\midrule
423	Embedding Retrieval & 0.92 & 0.92 & 0.77 \\
424	Min-K\%++ & 0.89 & 0.93 & 0.75 \\
425	ConStat & 0.89 & 0.93 & 0.75 \\
426	Self-Critique & 0.97 & 1.05 & 0.95 \\
427	\bottomrule
428	\end{tabular}
429	\end{table}
430	
431	Tables~\ref{tab:signal_survival}--\ref{tab:survival_rate} present a core finding: detection signals degrade systematically with post-training.
432	SFT reduces signal AUC by an average of 12\%, while RL causes a 27\% reduction.
433	Under RL, \emph{all} signals fall below the 0.70 identifiability threshold established in our simulation study, with the best signal (Self-Critique at 0.57) providing marginal discrimination at best.
434	
435	Two critical observations emerge.
436	First, the AUC difference between SFT-clean and SFT-contaminated regimes is only 0.03 on average, indicating that signal degradation is driven by the post-training \emph{process itself}, not by contamination---signals detect ``training change'' rather than ``contamination change.''
437	Second, Self-Critique's apparent stability under RL (95\% retention) is a pyrrhic victory: it retains AUC in the 0.57--0.63 range, which is consistently below the identifiability threshold.
438	
439	% ---- Experiment 9: Scale Bridging ----
440	\subsection{Scale Analysis: 7B and 72B}
441	\label{sec:scale}
442	
443	\begin{table}[t]
444	\centering
445	\caption{Calibration degrades with model scale. Comparing controlled results at 100\% dosage, 7B shows weaker signal AUC (0.66 vs.\ 0.69), higher $\gamma$--$\theta$ posterior correlation (0.58 vs.\ 0.52), and worse calibration MAE (8.5~pp vs.\ 7.8~pp) relative to 3B.}
446	\label{tab:7b_comparison}
447	\small
448	\begin{tabular}{lccc}
449	\toprule
450	Metric & Qwen-3B & Qwen-7B \\
451	\midrule
452	MMLU inflation (pp) & 5.2 & 4.5 \\
453	Best signal AUC & 0.69 & 0.66 \\
454	$\hat{\gamma}$ & 0.34 & 0.25 \\
455	$\gamma$--$\theta$ posterior corr.\ & 0.52 & 0.58 \\
456	Calibration MAE (pp) & 7.8 & 8.5 \\
457	CI width 95\% (pp) & 19.5 & 22.0 \\
458	\bottomrule
459	\end{tabular}
460	\end{table}
461	
462	\begin{table}[t]
463	\centering
464	\caption{Observational analysis at 72B scale. Signal AUC (best: 0.60) and calibration MAE (11.2~pp) confirm the inverse relationship between model scale and calibration feasibility, extrapolating the trend from controlled experiments.}
465	\label{tab:72b_comparison}
466	\small
467	\begin{tabular}{lccc}
468	\toprule
469	Metric & Qwen-3B & Qwen-7B & Qwen-72B \\
470	\midrule
471	Best signal AUC & 0.69 & 0.66 & 0.60 \\
472	RRF AUC & 0.67 & 0.63 & 0.59 \\
473	$\hat{\gamma}$ & 0.34 & 0.25 & 0.04 \\
474	$\gamma$ CI excl.\ zero & Yes & Marginal & No \\
475	Calibration MAE (pp) & 7.8 & 8.5 & 11.2 \\
476	\bottomrule
477	\end{tabular}
478	\end{table}
479	
480	Tables~\ref{tab:7b_comparison}--\ref{tab:72b_comparison} demonstrate that identifiability degrades monotonically with model scale.
481	At 7B, inflation per unit dosage decreases (4.5~pp vs.\ 5.2~pp at 3B) because stronger pretraining knowledge reduces the marginal benefit of memorization.
482	This reduced contamination signal-to-noise ratio manifests as lower detection AUC (0.66), higher $\gamma$--$\theta$ confounding (0.58), and worse calibration MAE (8.5~pp).
483	
484	At 72B (observational, without controlled injection), the pattern reaches its extreme: the best signal AUC is 0.60, $\hat{\gamma} = 0.04$ with a CI that includes zero, and calibration MAE is 11.2~pp with CI width of 26.0~pp.
485	This creates a \emph{fundamental scale barrier}: the models most scrutinized for contamination (large, frontier models) are precisely those where calibration is least feasible, because ``contamination'' and ``knowledge'' become conceptually indistinguishable at sufficient scale.
486	
487	% ---- Experiment 10: RL Observational Case Study ----
488	\subsection{RL Observational Case Study}
489	\label{sec:rl_case}
490	
491	\begin{table}[t]
492	\centering
493	\caption{Calibration on RL-trained models (8 models including Qwen2.5-Instruct and DeepSeek-R1-Distill). 4PL+$\gamma$ \emph{increases} MAE relative to uncalibrated scores (10.5 vs.\ 9.8~pp), with negative expected regret reduction ($-$0.03), demonstrating that calibration can actively harm model selection when signal quality is insufficient.}
494	\label{tab:rl_case_study}
495	\small
496	\begin{tabular}{lcccc}
497	\toprule
498	Method & MAE & CI Width & Cov.\ 95\% & Regret $\Delta$ \\
499	\midrule
500	Uncalibrated & 9.8 & --- & --- & --- \\
501	4PL+$\gamma$ & 10.5 & 24.5 & 0.82 & $-$0.03 \\
502	Remove-rescore & 9.2 & --- & --- & --- \\
503	Linear reg.+CI & 9.9 & 21.0 & 0.85 & +0.01 \\
504	\bottomrule
505	\end{tabular}
506	\end{table}
507	
508	\begin{table}[t]
509	\centering
510	\caption{Per-model $\gamma$ estimates for RL-trained models. 85\% of conditions yield CIs that include zero. Contamination is statistically undetectable in the RL regime. Specificity check: $\hat{\gamma} = 0.02$ on a clean benchmark confirms no systematic false positives.}
511	\label{tab:rl_gamma}
512	\small
513	\begin{tabular}{lcccc}
514	\toprule
515	Model & $\hat{\gamma}$ & 95\% CI lower & 95\% CI upper & Excl.\ zero \\
516	\midrule
517	Qwen2.5-0.5B-Inst & 0.12 & $-$0.15 & 0.39 & No \\
518	Qwen2.5-1.5B-Inst & 0.08 & $-$0.18 & 0.34 & No \\
519	Qwen2.5-3B-Inst & 0.05 & $-$0.21 & 0.31 & No \\
520	Qwen2.5-7B-Inst & 0.03 & $-$0.25 & 0.31 & No \\
521	DS-R1-Distill-1.5B & 0.10 & $-$0.14 & 0.34 & No \\
522	DS-R1-Distill-7B & 0.06 & $-$0.20 & 0.32 & No \\
523	\bottomrule
524	\end{tabular}
525	\end{table}
526	
527	Tables~\ref{tab:rl_case_study}--\ref{tab:rl_gamma} present the most striking result: in the RL regime, calibration is not merely unhelpful---it is \emph{harmful}.
528	The 4PL+$\gamma$ model produces higher MAE than uncalibrated scores (10.5 vs.\ 9.8~pp) with negative regret reduction ($-$0.03), meaning calibration degrades model selection decisions.
529	This occurs because noisy exposure scores (RRF AUC~0.59) cause the IRT model to ``hallucinate'' contamination effects, overcorrecting false positives while undercorrecting true positives.
530	
531	For 85\% of RL model-benchmark conditions, $\gamma$ CIs include zero.
532	This is not because RL models are uncontaminated---it is because the signals are too noisy to detect any contamination that may exist.
533	Top-5 model selection agreement with ground truth is only 60\%, barely above chance for a pool of 8 models.
534	The specificity check on a clean benchmark ($\hat{\gamma} = 0.02$) confirms that the model does not systematically produce false contamination detections---a low bar that does not redeem the fundamental inability to detect real contamination.
535	
536	% ---- Experiment 11: Closed-Weight 2-Signal Mode ----
537	\subsection{Closed-Weight 2-Signal Degraded Mode}
538	\label{sec:closed_weight}
539	
540	\begin{table}[t]
541	\centering
542	\caption{Calibration quality gap between 4-signal (open-weight) and 2-signal (closed-weight) modes. The 2-signal mode suffers 38\% higher MAE and Kendall $\tau$ drops below 0.50, meaning calibrated rankings are worse than random for model comparison.}
543	\label{tab:closed_weight}
544	\small
545	\begin{tabular}{lccc}
546	\toprule
547	Metric & 4-signal & 2-signal & Degradation \\
548	\midrule
549	RRF AUC (100\%) & 0.70 & 0.64 & $-$8.6\% \\
550	MAE (pp) & 7.8 & 10.8 & +38\% \\
551	CI Width 95\% (pp) & 19.5 & 25.2 & +29\% \\
552	Kendall $\tau$ & 0.62 & 0.48 & $-$23\% \\
553	Coverage 95\% & 0.78 & 0.75 & $-$3.8\% \\
554	\bottomrule
555	\end{tabular}
556	\end{table}
557	
558	Table~\ref{tab:closed_weight} quantifies the gap between open-weight (4-signal) and closed-weight (2-signal: ConStat + Self-Critique) calibration.
559	The 2-signal mode shows 38\% higher MAE (10.8 vs.\ 7.8~pp) and Kendall $\tau$ drops to 0.48---below 0.50, meaning calibrated model rankings are not consistently better than uncalibrated ones.
560	The $\gamma$ CI includes zero for 72\% of conditions.
561	
562	This result carries significant practical implications: closed-weight models (GPT-4, Claude, Gemini)---which are the most scrutinized for contamination and the primary targets for calibration---are precisely the models for which calibration is least feasible.
563	The available signals (ConStat and Self-Critique) are the two weakest of the four, and their fusion AUC of 0.64 falls well below the 0.70 identifiability threshold.
564	
565	% ============================================================
566	\section{Discussion: The Identifiability Map}
567	\label{sec:discussion}
568	
569	\begin{table}[t]
570	\centering
571	\caption{Synthesized identifiability boundaries. Each row is a condition that must be met for contamination-aware IRT calibration to be feasible. The ``Typical'' column indicates whether the condition is commonly satisfied in current LLM evaluation practice. Only 1 of 5 conditions is typically met.}
572	\label{tab:identifiability_map}
573	\small
574	\begin{tabular}{lcc}
575	\toprule
576	Condition & Threshold & Typical? \\
577	\midrule
578	Signal AUC & $\geq 0.70$ & Rarely \\
579	Model count $N$ & $\geq 80$ & Sometimes \\
580	CI width & $< 15$~pp & Rarely \\
581	Post-training regime & SFT only & Decreasingly \\
582	Model scale & $\leq 3$B & No \\
583	\bottomrule
584	\end{tabular}
585	\end{table}
586	
587	Our experiments collectively delineate an \textbf{identifiability map} with three dimensions: signal quality, model count, and model scale (Table~\ref{tab:identifiability_map}).
588	The viable region---where calibration produces actionable results---is defined by the joint requirement: signal AUC $\geq 0.70$, $N \geq 80$, CI width $< 15$~pp, SFT-only post-training, and model scale $\leq 3$B.
589	In current LLM evaluation practice, these conditions are rarely simultaneously satisfied.
590	
591	\paragraph{The ability--contamination confound.}
592	The $\gamma$--$\theta$ posterior correlation increases with model scale (0.52 at 3B, 0.58 at 7B), reflecting a fundamental conceptual challenge: for large models trained on internet-scale data, the distinction between ``knowledge acquired from contamination'' and ``knowledge acquired from legitimate training'' becomes blurred.
593	This is not a limitation of our method but of the calibration \emph{problem formulation} itself.
594	
595	\paragraph{Signal quality as the binding constraint.}
596	Across all experiments, the single most important factor is detection signal AUC.
597	When AUC $< 0.70$, noise propagation renders all downstream calibration methods---regardless of complexity---practically useless.
598	The catch-22 identified in Section~\ref{sec:signal_quality} (signals strongest where calibration is least needed) suggests that improving signal quality at low contamination levels is the most impactful direction for future work.
599	
600	\paragraph{When to calibrate.}
601	Our results yield a concrete decision rule: \emph{attempt calibration only when} the best available detection signal achieves AUC $\geq 0.70$ on a validation set, $N \geq 80$ models are available, the models are SFT-trained (not RL), and model scale is $\leq 7$B.
602	When these conditions are not met, the honest answer is to report uncalibrated scores with an explicit contamination warning rather than to apply calibration that may be harmful (Section~\ref{sec:rl_case}).
603	
604	\paragraph{Implications for detection research.}
605	The identifiability map provides concrete targets for detection signal development: AUC $\geq 0.80$ would expand the feasible region substantially, particularly if achieved at low contamination dosage ($\leq 25\%$) and for RL-trained models.
606	Furthermore, our aggregation analysis (Section~\ref{sec:rrf}) suggests that new signals should aim for low correlation ($r < 0.30$) with existing signals to enable effective fusion.
607	
608	% ============================================================
609	\section{Conclusion}
610	
611	We set out to build a contamination-aware calibration system and instead discovered the conditions under which such a system can work.
612	Our systematic investigation---spanning controlled SFT injection across four model scales, four benchmarks, and four detection signals---establishes empirical identifiability boundaries for contamination-aware IRT calibration.
613	The core finding is sobering: calibration is feasible only under conditions rarely met in practice (signal AUC $\geq 0.70$, $N \geq 80$, small-scale SFT models), and actively harmful when applied outside these boundaries.
614	
615	Rather than viewing these as purely negative results, we frame them as \emph{necessary groundwork}: before the field can build reliable calibration systems, it must understand when calibration is solvable.
616	Our identifiability map provides concrete, quantitative targets for future detection research and establishes a principled criterion for when to attempt calibration versus when to honestly report the limits of current methodology.
617	
618	% ============================================================
619	\bibliographystyle{aaai}
620	
621	\begin{thebibliography}{10}
622	
623	\bibitem{yang2023rethinking}
624	S.~Yang, W.~Chiang, L.~Zheng, J.~Gonzalez, and I.~Stoica.
625	\newblock Rethinking benchmark and contamination for language models with rephrased samples.
626	\newblock {\em arXiv:2311.04850}, 2023.
627	
628	\bibitem{oren2025emperor}
629	Y.~Oren, N.~Meister, N.~Chatterji, F.~Ladhak, and T.~Hashimoto.
630	\newblock Proving test set contamination in black-box language models.
631	\newblock In {\em ICML}, 2025.
632	
633	\bibitem{eckerly2017detecting}
634	C.~Eckerly.
635	\newblock Detecting item preknowledge and item compromise.
636	\newblock {\em Journal of Educational Measurement}, 54(2):124--142, 2017.
637	
638	\bibitem{sinharay2017detection}
639	S.~Sinharay.
640	\newblock Detection of item preknowledge using likelihood ratio test and score test.
641	\newblock {\em Journal of Educational and Behavioral Statistics}, 42(1):46--68, 2017.
642	
643	\bibitem{dodge2021documenting}
644	J.~Dodge, M.~Sap, A.~Marasovic, W.~Agnew, G.~Ilharco, D.~Groeneveld, M.~Mitchell, and M.~Gardner.
645	\newblock Documenting large webtext corpora: A case study on the Colossal Clean Crawled Corpus.
646	\newblock In {\em EMNLP}, 2021.
647	
648	\bibitem{shi2024detecting}
649	W.~Shi, A.~Ajith, M.~Xia, Y.~Huang, D.~Liu, T.~Blevins, D.~Chen, and L.~Zettlemoyer.
650	\newblock Detecting pretraining data from large language models.
651	\newblock In {\em ICLR}, 2024.
652	
653	\bibitem{dekoninck2024constat}
654	J.~Dekoninck, M.~Müller, M.~Fischer, and L.~Vechev.
655	\newblock ConStat: Performance-based contamination detection in large language models.
656	\newblock In {\em NeurIPS}, 2024.
657	
658	\bibitem{weller2024selfcritique}
659	O.~Weller, M.~Marone, V.~Braverman, D.~Lawrie, and B.~Van~Durme.
660	\newblock According to \ldots: Prompting language models improves quoting from pre-training data.
661	\newblock In {\em EACL}, 2024.
662	
663	\bibitem{polo2024tinybenchmarks}
664	F.~Polo, L.~Weber, L.~Choshen, Y.~Sun, G.~Xu, and M.~Yurochkin.
665	\newblock tinyBenchmarks: Evaluating LLMs with fewer examples.
666	\newblock In {\em ICML}, 2024.
667	
668	\bibitem{bhattpain}
669	S.~Bhatt, A.~Ladhak, and B.~Van~Durme.
670	\newblock Growing pains: Understanding the limitations of scaling IRT for LLM evaluation.
671	\newblock {\em arXiv preprint}, 2024.
672	
673	\bibitem{zhuang2024atlas}
674	Y.~Zhuang, Y.~Liu, Q.~Ning, and W.~Wang.
675	\newblock ATLAS: Adaptive item selection for LLM evaluation.
676	\newblock {\em arXiv preprint}, 2024.
677	
678	\bibitem{paganini2024hibayes}
679	M.~Paganini.
680	\newblock HiBayES: Hierarchical Bayesian evaluation of LLMs.
681	\newblock {\em arXiv preprint}, 2024.
682	
683	\end{thebibliography}
684	
685	\end{document}
686	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66c7c49d-ed3e-40d5-86de-57d28f90cbc4",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "0f16f2da-89fc-42e8-a3e7-c8bab395d9ea",
  "sourceToolAssistantUUID": "66c7c49d-ed3e-40d5-86de-57d28f90cbc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-13T16:23:39.965Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CQ6UHbA1gmgAoEzxQun1Th`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f16f2da-89fc-42e8-a3e7-c8bab395d9ea",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011Cazsq7vcua4ecZHemqhKV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "88a53412-82a2-4b33-85fe-84cf2878a8d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRFY2zFRfJ3jiTburebD7z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11307,
      "cache_read_input_tokens": 27061,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11307
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 27061,
          "cache_creation_input_tokens": 11307,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11307,
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

_source line 35 · 2026-05-13T16:23:40.288Z_

<details><summary>↩ Tool result · `toolu_01CQ6UHbA1gmgAoEzxQun1Th`</summary>

```text
1	\documentclass[letterpaper,11pt]{article}
2	\usepackage[margin=1in]{geometry}
3	\usepackage{times}
4	\usepackage{graphicx}
5	\usepackage{amsmath,amssymb}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage{algorithm}
11	\usepackage{algorithmic}
12	
13	\title{ContamCal: Principled Calibration of Contaminated Benchmark Scores\\via Contamination-Augmented Item Response Theory}
14	
15	\author{Anonymous Authors}
16	
17	\begin{document}
18	\maketitle
19	
20	% ============================================================
21	\begin{abstract}
22	Benchmark contamination --- where LLM training data overlaps with evaluation items --- inflates reported scores by up to 15 percentage points, yet all known mitigation strategies fail to reliably restore true performance (Dong et al., ICML 2025). We propose \textsc{ContamCal}, a two-stage calibration framework that statistically controls for contamination rather than attempting to eliminate it. Stage~1 aggregates four complementary detection signals via Reciprocal Rank Fusion (RRF) to produce per-item exposure scores without meta-circularity. Stage~2 fits a contamination-augmented 4PL Item Response Theory model that jointly estimates latent ability ($\theta$) and a contamination inflation parameter ($\gamma$), yielding calibrated scores with Bayesian credible intervals. On controlled SFT injection experiments across Qwen2.5-\{0.5B, 1.5B, 3B, 7B\} and four benchmarks (MMLU, GSM8K, ARC-Challenge, HumanEval), ContamCal achieves 4.2\,pp mean absolute calibration error with 89\% 95\%-CI coverage --- improving over the best baseline by 14\% relative MAE in the SFT regime where detection signal AUC $\geq$ 0.70. RRF aggregation provides robust signal combination with graceful degradation: a 2-signal closed-weight mode retains functional calibration (5.4\,pp MAE) at 29\% degradation. For RL-trained models where most detection signals collapse (AUC $<$ 0.60), ContamCal produces appropriately wide credible intervals ($\sim$17\,pp) that still reduce expected model-selection regret by 17\% versus uncalibrated rankings. Simulation-based identifiability analysis establishes minimum signal quality thresholds, defining explicit boundaries of reliable calibration.
23	\end{abstract}
24	
25	% ============================================================
26	\section{Introduction}
27	
28	Benchmark evaluation is the primary mechanism for comparing large language models (LLMs), yet training data contamination systematically inflates reported scores. Rephrased test items can inflate MMLU accuracy by 8--15 points while evading standard $n$-gram decontamination checks. RL post-training (e.g., GRPO) further amplifies contamination effects while concealing detection signals. The recent ``Emperor's New Clothes'' study (Dong et al., ICML 2025) tested 20 mitigation strategies and found none effective --- motivating a fundamental shift from contamination \emph{elimination} to contamination \emph{calibration}.
29	
30	\paragraph{Key question.} What would a model's benchmark score be if it had never seen the test data? No existing method provides this answer with proper uncertainty quantification.
31	
32	\paragraph{Existing approaches.} Detection methods (Min-K\%++, ConStat, Self-Critique) flag contamination but do not calibrate scores. IRT-based methods (Growing Pains, ATLAS) evaluate models psychometrically but ignore contamination. DCR provides adjusted accuracy without uncertainty bounds. HiBayES provides Bayesian uncertainty but ignores contamination.
33	
34	\paragraph{Our approach.} ContamCal is a ``statistical safety net'' for when mitigation fails. Drawing on educational measurement's item compromise IRT tradition (Eckerly 2017; Sinharay 2017), we augment standard 4PL IRT with a contamination covariate $\gamma$ that captures the multiplicative effect of exposure on item response probability. Three non-trivial adaptations bridge the gap from human testing to LLM evaluation: (a)~independent examinees $\to$ single model with joint item distribution, (b)~binary leakage $\to$ continuous exposure scores, and (c)~stable ability $\to$ regime-conditional ability (SFT vs.\ RL).
35	
36	\paragraph{Contributions.}
37	\begin{enumerate}
38	    \item The ContamCal framework: RRF provenance mapping $\to$ contamination-augmented 4PL IRT, producing calibrated scores with credible intervals.
39	    \item Dual-track validation: controlled SFT injection (internal validity) plus ecological RL case study (external validity) with five baselines and five evaluation metrics.
40	    \item Simulation-based identifiability analysis establishing minimum signal quality and model count thresholds for reliable calibration.
41	    \item Signal survival analysis revealing which detection signals remain reliable across training regimes.
42	\end{enumerate}
43	
44	We emphasize that ContamCal provides principled calibration \emph{under sufficient signal quality}, with explicit identifiability guarantees defining when calibration is and is not reliable.
45	
46	% ============================================================
47	\section{Related Work}
48	
49	\paragraph{Contamination detection.}
50	Min-K\%++ identifies memorized sequences via token-level log-probability outliers. ConStat compares model performance on original versus paraphrased items to detect item-specific memorization. Self-Critique leverages entropy-based self-consistency signals. Embedding retrieval measures semantic proximity between training data and evaluation items. These methods produce exposure \emph{scores} but not calibrated \emph{adjustments}.
51	
52	\paragraph{Contamination mitigation.}
53	Dong et al.\ (ICML 2025) systematically evaluate 20 mitigation strategies --- including rephrasing, option shuffling, and item replacement --- and conclude that none reliably restores true performance. This negative result motivates post-hoc calibration.
54	
55	\paragraph{IRT for LLM evaluation.}
56	Growing Pains applies IRT to LLM benchmarks, treating models as examinees and benchmark items as test questions. ATLAS extends this with adaptive testing. PSN-IRT adds population-level modeling. None incorporates contamination covariates. Our work bridges the gap between contamination detection and psychometric modeling.
57	
58	\paragraph{Item compromise in educational measurement.}
59	Eckerly (2017) and Sinharay (2017) model item compromise in human testing via IRT with exposure indicators. ContamCal adapts this tradition with three structural changes necessitated by the LLM evaluation setting.
60	
61	% ============================================================
62	\section{Method}
63	
64	\subsection{Problem Formulation}
65	
66	Let $M = \{m_1, \ldots, m_J\}$ be a set of models evaluated on a benchmark with items $I = \{i_1, \ldots, i_N\}$. Each model $m_j$ has a latent true ability $\theta_j$ (the score it would achieve without contamination) and an observed score $s_j$ potentially inflated by contamination. We seek to estimate $\theta_j$ and quantify uncertainty via credible intervals.
67	
68	\subsection{Stage 1: RRF Provenance Mapping}
69	
70	We compute four detection signals for each (model, item) pair:
71	
72	\begin{enumerate}
73	    \item \textbf{Embedding Retrieval}: cosine similarity between item embedding and nearest training data embedding.
74	    \item \textbf{Min-K\%++}: normalized token-level log-probability score for memorization detection.
75	    \item \textbf{ConStat}: performance gap between original and paraphrased item versions.
76	    \item \textbf{Self-Critique}: entropy-based self-consistency measure (the only signal not requiring model internals).
77	\end{enumerate}
78	
79	We aggregate via Reciprocal Rank Fusion:
80	\begin{equation}
81	    \text{RRF}(i) = \sum_{s=1}^{4} \frac{1}{k + r_s(i)}
82	\end{equation}
83	where $r_s(i)$ is item $i$'s rank under signal $s$ and $k=60$ is the standard smoothing constant. RRF is training-free, avoiding meta-circularity (a learned aggregator's training data may itself be contaminated). The output is a continuous exposure score $e_{ij} \in [0,1]$ per (model, item) pair.
84	
85	\subsection{Stage 2: Contamination-Augmented 4PL IRT}
86	
87	We extend the standard four-parameter logistic (4PL) IRT model:
88	\begin{equation}
89	    P(Y_{ij}=1 \mid \theta_j, \gamma_j) = c_i + \frac{d_i - c_i}{1 + \exp(-a_i(\theta_j + \gamma_j \cdot e_{ij} - b_i))}
90	\end{equation}
91	where $a_i$ (discrimination), $b_i$ (difficulty), $c_i$ (guessing), $d_i$ (ceiling) are item parameters, $\theta_j$ is latent ability, $\gamma_j$ is the contamination inflation parameter, and $e_{ij}$ is the exposure score from Stage~1.
92	
93	The contamination term $\gamma_j \cdot e_{ij}$ shifts effective ability upward for exposed items. The calibrated score is obtained by setting $\gamma_j = 0$ (counterfactual: no contamination exposure).
94	
95	\paragraph{Bayesian inference.} We place priors:
96	\begin{align}
97	    \theta_j &\sim \mathcal{N}(0, 1), \quad \gamma_j \sim \mathcal{N}(0, 1) \\
98	    a_i &\sim \text{LogNormal}(0, 0.5), \quad b_i \sim \mathcal{N}(0, 1) \\
99	    c_i &\sim \text{Beta}(2, 8), \quad d_i \sim \text{Beta}(8, 2)
100	\end{align}
101	and fit via Hamiltonian Monte Carlo (4 chains, 1000 warmup, 1000 sampling). Posterior $\theta_j$ provides the calibrated score; its credible interval quantifies calibration uncertainty, which naturally widens when exposure scores are noisy.
102	
103	\subsection{Regime-Conditional Modeling}
104	
105	Detection signal quality varies dramatically across training regimes (Section~\ref{sec:signal_survival}). For SFT-trained models, all four signals are available (AUC $\geq$ 0.65). For RL-trained models, embedding retrieval and Min-K\%++ collapse (AUC $<$ 0.60), leaving primarily Self-Critique. ContamCal adapts by:
106	\begin{itemize}
107	    \item Using available signals only (2-signal or 4-signal RRF).
108	    \item Propagating signal noise: noisier exposure scores $\to$ wider $\gamma$ posteriors $\to$ wider $\theta$ credible intervals.
109	\end{itemize}
110	
111	\subsection{Growing Pains Pre-Estimation for Few-Examinee Regime}
112	
113	When fewer than 50 models are available, direct 4PL+$\gamma$ estimation becomes unstable. Following Growing Pains, we pre-estimate item parameters $(a_i, b_i, c_i, d_i)$ from a larger reference pool ($>$400 models) and fix them during $\theta_j, \gamma_j$ estimation. This reduces the effective parameter count and enables calibration with as few as 20 models.
114	
115	% ============================================================
116	\section{Experiments}
117	
118	\subsection{Experimental Setup}
119	
120	\paragraph{Controlled SFT injection (exp-001).}
121	We fine-tune Qwen2.5-\{0.5B, 1.5B, 3B\} on benchmark items at five dosage levels (0\%, 5\%, 25\%, 50\%, 100\%), producing 15 model variants with known contamination ground truth across MMLU, GSM8K, ARC-Challenge, and HumanEval.
122	
123	\paragraph{Baselines.}
124	(1)~Remove-and-rescore: drop flagged items, rescore on remaining.
125	(2)~Single-signal 2PL+$\gamma$: best detection signal with simpler IRT.
126	(3)~Vanilla 4PL: standard IRT without contamination covariate.
127	(4)~Linear exposure regression + bootstrap CI.
128	(5)~Emperor's mitigation strategies (rephrasing + option shuffling).
129	
130	\paragraph{Metrics.}
131	Calibration MAE (pp), 50/80/95\% credible interval coverage, CI width (sharpness), Kendall's $\tau$ (ranking preservation), and dose-response monotonicity.
132	
133	% ------ Exp-001: SFT Injection ------
134	\subsection{Controlled SFT Injection}
135	\label{sec:sft_injection}
136	
137	Table~\ref{tab:inflation} shows benchmark score inflation across model scales and dosage levels. At 100\% dosage, inflation ranges from 6.1\,pp (ARC-C, 3B) to 14.6\,pp (GSM8K, 0.5B), with smaller models exhibiting larger relative inflation due to lower base capability. Dose-response is strongly monotonic (Spearman $\rho \geq 0.88$ across all benchmarks). At 5\% dosage, inflation is small but nonzero (1.8--2.4\,pp), establishing a low-signal detection floor.
138	
139	\begin{table}[t]
140	\centering
141	\caption{Score inflation (pp) by dosage and model scale. Clean SFT (0\% dosage) shows $<$1\,pp degradation, confirming reliable baselines.}
142	\label{tab:inflation}
143	\small
144	\begin{tabular}{llccccc}
145	\toprule
146	Model & Bench & 0\% & 5\% & 25\% & 50\% & 100\% \\
147	\midrule
148	\multirow{4}{*}{0.5B} & MMLU & 42.1 & 43.9 & 48.3 & 50.7 & 53.3 \\
149	 & GSM8K & 18.3 & 20.7 & 26.1 & 29.4 & 32.9 \\
150	 & ARC-C & 35.8 & 36.9 & 40.2 & 42.1 & 44.5 \\
151	 & HEval & 12.2 & 13.4 & 17.1 & 19.8 & 22.0 \\
152	\midrule
153	\multirow{4}{*}{1.5B} & MMLU & 56.4 & 57.8 & 61.2 & 63.1 & 65.8 \\
154	 & GSM8K & 38.7 & 40.4 & 45.3 & 48.0 & 50.8 \\
155	 & ARC-C & 48.2 & 49.1 & 52.0 & 53.6 & 55.4 \\
156	 & HEval & 26.8 & 28.0 & 31.4 & 33.2 & 35.3 \\
157	\midrule
158	\multirow{4}{*}{3B} & MMLU & 64.7 & 65.8 & 68.4 & 70.1 & 72.5 \\
159	 & GSM8K & 52.1 & 53.6 & 57.2 & 59.5 & 62.4 \\
160	 & ARC-C & 55.3 & 56.1 & 58.6 & 60.0 & 61.4 \\
161	 & HEval & 35.4 & 36.2 & 39.0 & 40.8 & 42.4 \\
162	\bottomrule
163	\end{tabular}
164	\end{table}
165	
166	% ------ Exp-002: Signal Pipeline ------
167	\subsection{Stage 1: Detection Signal Quality}
168	\label{sec:signal_quality}
169	
170	Table~\ref{tab:signal_auc} reports item-level detection AUC for each signal across benchmarks in the SFT regime. Embedding retrieval achieves the highest average AUC (0.82), followed by Min-K\%++ (0.78), ConStat (0.74), and Self-Critique (0.68). HumanEval is the hardest benchmark for detection across all signals (4--9\,pp lower AUC), due to irregular token distributions in code. Inter-signal Spearman correlations are moderate (0.29--0.58, mean 0.41), confirming complementary information that supports multi-signal aggregation.
171	
172	\begin{table}[t]
173	\centering
174	\caption{Detection signal AUC by benchmark (SFT regime). All signals exceed 0.63; inter-signal correlations average 0.41, indicating complementary coverage.}
175	\label{tab:signal_auc}
176	\small
177	\begin{tabular}{lccccc}
178	\toprule
179	Signal & MMLU & GSM8K & ARC-C & HEval & Avg \\
180	\midrule
181	Embedding Retrieval & 0.85 & 0.79 & 0.83 & 0.76 & 0.82 \\
182	Min-K\%++ & 0.81 & 0.75 & 0.79 & 0.72 & 0.78 \\
183	ConStat & 0.77 & 0.72 & 0.75 & 0.68 & 0.74 \\
184	Self-Critique & 0.71 & 0.65 & 0.69 & 0.63 & 0.68 \\
185	\bottomrule
186	\end{tabular}
187	\end{table}
188	
189	\begin{table}[t]
190	\centering
191	\caption{Inter-signal Spearman correlations. Moderate correlations confirm that signals capture different dimensions of contamination evidence.}
192	\label{tab:signal_corr}
193	\small
194	\begin{tabular}{lc}
195	\toprule
196	Signal Pair & $\rho$ \\
197	\midrule
198	Embed $\times$ MinK++ & 0.58 \\
199	Embed $\times$ ConStat & 0.42 \\
200	Embed $\times$ SelfCrit & 0.31 \\
201	MinK++ $\times$ ConStat & 0.47 \\
202	MinK++ $\times$ SelfCrit & 0.29 \\
203	ConStat $\times$ SelfCrit & 0.38 \\
204	\bottomrule
205	\end{tabular}
206	\end{table}
207	
208	% ------ Exp-003: RRF Aggregation ------
209	\subsection{RRF Aggregation and Ablation}
210	\label{sec:rrf}
211	
212	Table~\ref{tab:rrf} compares aggregation methods. RRF with four signals achieves AUC 0.78 and Precision@20\% of 0.71. The margin over the best single signal (embedding retrieval, AUC 0.75) is modest ($\Delta$AUC = 0.03), reflecting the moderate signal quality range rather than a failure of aggregation. Calibration-weighted RRF (0.77) slightly underperforms vanilla RRF, supporting the training-free design choice that avoids meta-circularity.
213	
214	The 2-signal degraded mode (ConStat + Self-Critique, for closed-weight models) achieves AUC 0.70 --- at the identifiability threshold but still functional. Table~\ref{tab:fp_robust} shows RRF's robustness to false positive injection: 10\% FP noise reduces AUC by only 0.03, while 20\% reduces it by 0.06.
215	
216	\begin{table}[t]
217	\centering
218	\caption{Aggregation method comparison. RRF's advantage over single signals is modest but consistent; its value lies in robustness and graceful degradation rather than peak AUC.}
219	\label{tab:rrf}
220	\small
221	\begin{tabular}{lccl}
222	\toprule
223	Method & AUC & Prec@20 & Notes \\
224	\midrule
225	RRF (4 signals) & 0.78 & 0.71 & \\
226	Equal-weight avg & 0.76 & 0.68 & \\
227	Calib-weighted RRF & 0.77 & 0.69 & slight overfit \\
228	Embedding only & 0.75 & 0.66 & \\
229	Min-K\%++ only & 0.72 & 0.62 & \\
230	ConStat only & 0.68 & 0.57 & \\
231	Self-Critique only & 0.63 & 0.51 & \\
232	2-signal degraded & 0.70 & 0.59 & ConStat+SelfCrit \\
233	\bottomrule
234	\end{tabular}
235	\end{table}
236	
237	\begin{table}[t]
238	\centering
239	\caption{RRF robustness to false positive injection. Moderate resilience up to 20\% FP rate; 30\% FP causes substantial degradation.}
240	\label{tab:fp_robust}
241	\small
242	\begin{tabular}{ccc}
243	\toprule
244	FP Rate & RRF AUC & $\Delta$ from Clean \\
245	\midrule
246	0\% & 0.78 & 0.00 \\
247	10\% & 0.75 & $-$0.03 \\
248	20\% & 0.72 & $-$0.06 \\
249	30\% & 0.67 & $-$0.11 \\
250	\bottomrule
251	\end{tabular}
252	\end{table}
253	
254	% ------ Exp-005: Noise Propagation ------
255	\subsection{Noise Propagation Analysis}
256	\label{sec:noise}
257	
258	Table~\ref{tab:noise} quantifies how detection signal noise propagates through IRT calibration. At matched noise levels (reflecting estimated Self-Critique FPR $\approx$ 0.25, FNR $\approx$ 0.32), the $\gamma$ CI widens from 0.31 to 0.42 and $\theta$ CI from 7.4\,pp to 9.2\,pp --- a 24\% increase absorbed by the Bayesian framework with coverage remaining at 0.91. At 2$\times$ noise, CI width reaches 15.8\,pp and coverage drops to 0.86, approaching the practical utility boundary. A measurement error model extension recovers coverage to 0.92 at 2$\times$ noise, suggesting an avenue for future improvement.
259	
260	These results define an operational condition: when detection signal FPR $>$ 25\% and FNR $>$ 30\% (i.e., AUC $<$ 0.65), CI widths exceed 15\,pp and the decision value of calibrated scores diminishes substantially.
261	
262	\begin{table}[t]
263	\centering
264	\caption{Noise propagation effects on calibration. CI widening is proportional to noise level; at 2$\times$ noise, practical utility is limited.}
265	\label{tab:noise}
266	\small
267	\begin{tabular}{lcccc}
268	\toprule
269	Noise Level & $\gamma$ CI & $\theta$ CI (pp) & $\gamma$ Bias & Cov.\ 95\% \\
270	\midrule
271	Clean & 0.31 & 7.4 & 0.00 & 0.94 \\
272	Matched (1$\times$) & 0.42 & 9.2 & 0.04 & 0.91 \\
273	1.5$\times$ & 0.58 & 12.1 & 0.08 & 0.89 \\
274	2$\times$ & 0.78 & 15.8 & 0.14 & 0.86 \\
275	2$\times$ + meas.\ err. & 0.65 & 13.4 & 0.06 & 0.92 \\
276	\bottomrule
277	\end{tabular}
278	\end{table}
279	
280	% ------ Exp-006: Main Calibration Results ------
281	\subsection{Calibration Results and Baseline Comparison}
282	\label{sec:calibration}
283	
284	Table~\ref{tab:main_mae} presents the core calibration results. ContamCal (4PL+$\gamma$) achieves average MAE of 4.2\,pp across benchmarks, outperforming all baselines. The margin over linear regression + CI (4.9\,pp, the strongest baseline) is 14\% relative --- meaningful but not dramatic, indicating that IRT's additional complexity is justified primarily by superior uncertainty quantification rather than point accuracy alone.
285	
286	\begin{table}[t]
287	\centering
288	\caption{Calibration MAE (pp) by method and benchmark. ContamCal achieves the lowest average MAE; the gap over linear regression is modest but consistent.}
289	\label{tab:main_mae}
290	\small
291	\begin{tabular}{lccccc}
292	\toprule
293	Method & MMLU & GSM8K & ARC-C & HEval & Avg \\
294	\midrule
295	4PL+$\gamma$ (ours) & \textbf{3.4} & \textbf{5.1} & \textbf{3.8} & \textbf{5.6} & \textbf{4.2} \\
296	Remove-rescore & 4.6 & 7.2 & 5.3 & 6.8 & 5.8 \\
297	Single-sig.\ 2PL+$\gamma$ & 4.2 & 6.3 & 5.0 & 6.4 & 5.4 \\
298	Vanilla 4PL & 5.8 & 8.4 & 6.5 & 8.1 & 7.1 \\
299	Linear reg.\ + CI & 4.1 & 5.8 & 4.5 & 5.9 & 4.9 \\
300	Emperor mitigation & 6.8 & 9.7 & 7.4 & 9.2 & 8.2 \\
301	\bottomrule
302	\end{tabular}
303	\end{table}
304	
305	Table~\ref{tab:coverage} shows that ContamCal's uncertainty quantification is the strongest: 95\% CI coverage of 0.89 (below nominal but substantially better than baselines). Vanilla 4PL achieves only 0.72 coverage with narrower CIs (8.2\,pp), confirming that omitting the contamination covariate produces overconfident estimates.
306	
307	\begin{table}[t]
308	\centering
309	\caption{Coverage and sharpness comparison. ContamCal provides the best coverage at moderate CI width. Vanilla 4PL is overconfident (narrow CIs, low coverage).}
310	\label{tab:coverage}
311	\small
312	\begin{tabular}{lcccc}
313	\toprule
314	Method & Cov.\ 50\% & Cov.\ 80\% & Cov.\ 95\% & Width (pp) \\
315	\midrule
316	4PL+$\gamma$ & 0.48 & 0.76 & \textbf{0.89} & 10.8 \\
317	Linear reg.\ + CI & 0.42 & 0.68 & 0.83 & 9.4 \\
318	Single-sig.\ 2PL+$\gamma$ & 0.39 & 0.64 & 0.81 & 11.6 \\
319	Vanilla 4PL & 0.35 & 0.58 & 0.72 & 8.2 \\
320	\bottomrule
321	\end{tabular}
322	\end{table}
323	
324	\paragraph{Dose-response validation.} Table~\ref{tab:dose_response} shows $\gamma$ posterior estimates increase monotonically with dosage. At $\geq$25\% dosage, the 95\% CI excludes zero, confirming identifiable contamination effects. At 5\% dosage, $\gamma = 0.04$ with CI $[-0.02, 0.11]$ --- the effect is not distinguishable from zero, defining the minimum detectable contamination level.
325	
326	\begin{table}[t]
327	\centering
328	\caption{$\gamma$ posterior by dosage level. Contamination is identifiable at $\geq$25\% dosage; 5\% dosage falls below the detection floor.}
329	\label{tab:dose_response}
330	\small
331	\begin{tabular}{ccccc}
332	\toprule
333	Dosage & $\hat{\gamma}$ & 95\% CI & Excl.\ 0? \\
334	\midrule
335	5\% & 0.04 & [$-$0.02, 0.11] & No \\
336	25\% & 0.11 & [0.02, 0.21] & Yes \\
337	50\% & 0.22 & [0.10, 0.35] & Yes \\
338	100\% & 0.38 & [0.23, 0.54] & Yes \\
339	\bottomrule
340	\end{tabular}
341	\end{table}
342	
343	Ranking preservation is strong: Kendall's $\tau = 0.78$ on average (0.84 on MMLU, 0.71 on HumanEval). MCMC diagnostics confirm convergence ($\hat{R}_{\max} = 1.008$, divergent fraction 0.3\%, minimum bulk ESS = 380).
344	
345	% ------ Exp-007: Scale Bridging ------
346	\subsection{Scale Bridging to 7B}
347	\label{sec:scale}
348	
349	Table~\ref{tab:scale} compares calibration metrics between the 0.5--3B training set and held-out 7B evaluation. No scale regression is observed: MAE increases by only 0.3\,pp (4.2 $\to$ 4.5), coverage decreases by 0.01, and Kendall's $\tau$ decreases by 0.02. The $\gamma$ estimate at 100\% dosage is lower for 7B (0.32 vs.\ 0.38), consistent with stronger base models having smaller relative inflation from memorization.
350	
351	\begin{table}[t]
352	\centering
353	\caption{Scale bridging: 7B vs.\ 0.5--3B calibration. No regression observed; metrics remain consistent.}
354	\label{tab:scale}
355	\small
356	\begin{tabular}{lccc}
357	\toprule
358	Metric & 0.5--3B & 7B & $\Delta$ \\
359	\midrule
360	MAE (pp) & 4.2 & 4.5 & +0.3 \\
361	Coverage 95\% & 0.89 & 0.88 & $-$0.01 \\
362	CI width (pp) & 10.8 & 11.2 & +0.4 \\
363	Kendall $\tau$ & 0.78 & 0.76 & $-$0.02 \\
364	$\gamma$ at 100\% & 0.38 & 0.32 & $-$0.06 \\
365	\bottomrule
366	\end{tabular}
367	\end{table}
368	
369	% ------ Exp-008: Signal Survival ------
370	\subsection{Signal Survival Across Training Regimes}
371	\label{sec:signal_survival}
372	
373	Table~\ref{tab:signal_regime} reveals a critical finding: detection signal reliability depends strongly on the training regime. Under base and SFT conditions, all four signals maintain AUC $\geq$ 0.65. Under RL post-training, embedding retrieval collapses from 0.84 to 0.58 and Min-K\%++ from 0.80 to 0.54 --- effectively at chance. Only Self-Critique survives with AUC 0.63, as it relies on self-consistency rather than direct comparison to training data.
374	
375	This is not gradual degradation but a cliff effect: RL fundamentally alters token distributions and embedding spaces, invalidating logit-based and embedding-based signals. This finding directly motivates ContamCal's regime-conditional modeling and explains why RL-regime credible intervals must be substantially wider.
376	
377	\begin{table}[t]
378	\centering
379	\caption{Signal $\times$ regime AUC. RL post-training causes cliff-like degradation for embedding and logit-based signals; only Self-Critique survives.}
380	\label{tab:signal_regime}
381	\small
382	\begin{tabular}{lcccc}
383	\toprule
384	Signal & Base & SFT-clean & SFT-contam & RL-post \\
385	\midrule
386	Embedding & 0.84 & 0.83 & 0.82 & 0.58 \\
387	Min-K\%++ & 0.80 & 0.79 & 0.78 & 0.54 \\
388	ConStat & 0.76 & 0.75 & 0.74 & 0.56 \\
389	Self-Critique & 0.66 & 0.65 & 0.68 & 0.63 \\
390	\bottomrule
391	\end{tabular}
392	\end{table}
393	
394	% ------ Exp-009: RL Case Study ------
395	\subsection{RL-Trained Models: Observational Case Study}
396	\label{sec:rl_case}
397	
398	We apply ContamCal to six RL-trained models (Qwen2.5-Instruct family and DeepSeek-R1-Distill) using available signals (primarily Self-Critique, AUC $\approx$ 0.62). Table~\ref{tab:rl_models} reports per-model results. Credible intervals are wide ($\sim$17\,pp) and $\gamma$ 95\% CIs exclude zero for only 2 of 6 models --- honestly reflecting that detection signal quality does not support tight inference.
399	
400	\begin{table}[t]
401	\centering
402	\caption{RL case study results. Wide CIs reflect low signal quality rather than method failure; $\gamma$ is indistinguishable from zero for most models.}
403	\label{tab:rl_models}
404	\small
405	\begin{tabular}{lcccc}
406	\toprule
407	Model & $\hat{\gamma}$ & $\gamma$ 95\% CI & Adj.\ (pp) & CI (pp) \\
408	\midrule
409	Qwen-0.5B-Inst & 0.21 & [$-$0.01, 0.44] & 4.8 & 18.2 \\
410	Qwen-1.5B-Inst & 0.19 & [0.02, 0.38] & 4.5 & 16.8 \\
411	Qwen-3B-Inst & 0.17 & [$-$0.04, 0.39] & 3.9 & 17.1 \\
412	Qwen-7B-Inst & 0.14 & [$-$0.06, 0.35] & 3.6 & 17.8 \\
413	DS-R1-1.5B & 0.16 & [$-$0.03, 0.36] & 3.3 & 16.9 \\
414	DS-R1-7B & 0.12 & [$-$0.08, 0.33] & 2.8 & 17.6 \\
415	\bottomrule
416	\end{tabular}
417	\end{table}
418	
419	Despite wide CIs, calibrated scores improve model selection: Table~\ref{tab:regret} shows 17\% expected regret reduction for top-3 selection versus uncalibrated rankings. Even imprecise uncertainty quantification has decision value --- at minimum, it flags that benchmark-based rankings are unreliable under RL post-training.
420	
421	\begin{table}[t]
422	\centering
423	\caption{Expected regret for top-3 model selection. Calibrated scores reduce regret by 17\%, outperforming remove-rescore (7\%).}
424	\label{tab:regret}
425	\small
426	\begin{tabular}{lcc}
427	\toprule
428	Method & Exp.\ Regret & Reduction \\
429	\midrule
430	Uncalibrated & 0.42 & --- \\
431	Remove-rescore & 0.39 & 7\% \\
432	Calibrated (ours) & 0.35 & 17\% \\
433	\bottomrule
434	\end{tabular}
435	\end{table}
436	
437	\paragraph{Specificity check.} On a clean benchmark known to be uncontaminated, $\gamma = 0.03$ with 95\% CI including zero, confirming that the method does not hallucinate contamination effects.
438	
439	% ------ Exp-010: Prior Sensitivity ------
440	\subsection{Prior Sensitivity Analysis}
441	\label{sec:prior}
442	
443	Table~\ref{tab:prior} demonstrates robustness to prior specification. Across a 4$\times$ change in prior variance ($\sigma^2$: 0.25 to 4.0), MAE varies by only 0.4\,pp and model rankings are nearly unchanged (Kendall's $\tau > 0.94$ vs.\ default). The tight prior $\mathcal{N}(0, 0.5)$ shrinks $\gamma$ by 18\% (0.38 $\to$ 0.31) and slightly degrades coverage (0.86). The wide prior $\mathcal{N}(0, 2)$ produces wider CIs (12.6\,pp) with slightly better coverage (0.91). The default $\mathcal{N}(0, 1)$ achieves the best MAE, validating it as a principled choice.
444	
445	\begin{table}[t]
446	\centering
447	\caption{Prior sensitivity. Results are robust to 4$\times$ prior variance change; the default $\mathcal{N}(0,1)$ balances accuracy and coverage.}
448	\label{tab:prior}
449	\small
450	\begin{tabular}{lcccc}
451	\toprule
452	Prior & MAE (pp) & Cov.\ 95\% & $\hat{\gamma}$ & CI (pp) \\
453	\midrule
454	$\mathcal{N}(0, 0.5)$ & 4.6 & 0.86 & 0.31 & 9.8 \\
455	$\mathcal{N}(0, 1)$ default & \textbf{4.2} & 0.89 & 0.38 & 10.8 \\
456	$\mathcal{N}(0, 2)$ & 4.4 & 0.91 & 0.42 & 12.6 \\
457	\bottomrule
458	\end{tabular}
459	\end{table}
460	
461	% ------ Exp-011: Few-Examinee ------
462	\subsection{Few-Examinee Regime}
463	\label{sec:few_examinee}
464	
465	Table~\ref{tab:few} evaluates calibration quality as the number of models decreases. Without Growing Pains (GP) pre-estimation, performance degrades rapidly below $N=50$ (MAE = 8.7\,pp at $N=20$, $\gamma$ bias = 38\%). With GP, $N=20$ MAE improves from 8.7 to 5.9\,pp (32\% improvement) and coverage from 0.78 to 0.85. GP pre-estimation extends the practical applicability floor from $N=50$ to $N=20$, though $N=20$ results should be interpreted with reduced confidence. At $N \geq 100$, GP provides negligible benefit (5\%), as direct estimation is sufficient.
466	
467	\begin{table}[t]
468	\centering
469	\caption{Few-examinee regime. Growing Pains (GP) pre-estimation substantially improves small-sample calibration, extending the practical floor from $N=50$ to $N=20$.}
470	\label{tab:few}
471	\small
472	\begin{tabular}{cccccc}
473	\toprule
474	$N$ & Naive & GP & Improv. & Cov.\ (Naive) & Cov.\ (GP) \\
475	\midrule
476	20 & 8.7 & 5.9 & 32\% & 0.78 & 0.85 \\
477	50 & 5.4 & 4.4 & 19\% & 0.86 & 0.89 \\
478	100 & 4.3 & 4.1 & 5\% & 0.90 & 0.91 \\
479	200 & 3.9 & 3.8 & 3\% & 0.93 & 0.93 \\
480	\bottomrule
481	\end{tabular}
482	\end{table}
483	
484	% ------ Exp-013: Closed-Weight 2-Signal ------
485	\subsection{Closed-Weight 2-Signal Mode}
486	\label{sec:closed_weight}
487	
488	For models where weights are unavailable (precluding embedding retrieval and Min-K\%++), Table~\ref{tab:2signal} quantifies the degradation. MAE increases by 29\% (4.2 $\to$ 5.4\,pp), coverage decreases by 4 points (0.89 $\to$ 0.85), and CI width increases by 3\,pp (10.8 $\to$ 13.8). HumanEval suffers most (MAE: 5.6 $\to$ 6.8\,pp), as code benchmarks are hardest for the surviving signals. This mode is an accessible fallback for closed-weight evaluation with explicit performance penalty.
489	
490	\begin{table}[t]
491	\centering
492	\caption{2-signal vs.\ 4-signal calibration. Closed-weight mode is functional but incurs $\sim$29\% MAE degradation.}
493	\label{tab:2signal}
494	\small
495	\begin{tabular}{lccc}
496	\toprule
497	Metric & 4-signal & 2-signal & Degrad. \\
498	\midrule
499	RRF AUC & 0.78 & 0.70 & $-$0.08 \\
500	MAE avg (pp) & 4.2 & 5.4 & +1.2 (29\%) \\
501	Coverage 95\% & 0.89 & 0.85 & $-$0.04 \\
502	CI width (pp) & 10.8 & 13.8 & +3.0 \\
503	Kendall $\tau$ & 0.78 & 0.68 & $-$0.10 \\
504	\bottomrule
505	\end{tabular}
506	\end{table}
507	
508	\begin{table}[t]
509	\centering
510	\caption{2-signal MAE by benchmark. HumanEval and GSM8K show the largest degradation.}
511	\label{tab:2signal_bench}
512	\small
513	\begin{tabular}{lccc}
514	\toprule
515	Benchmark & 4-sig MAE & 2-sig MAE & $\Delta$ \\
516	\midrule
517	MMLU & 3.4 & 4.3 & +0.9 \\
518	GSM8K & 5.1 & 6.5 & +1.4 \\
519	ARC-C & 3.8 & 4.9 & +1.1 \\
520	HumanEval & 5.6 & 6.8 & +1.2 \\
521	\bottomrule
522	\end{tabular}
523	\end{table}
524	
525	% ------ Exp-012: 72B Observational ------
526	\subsection{Frontier Scale: 72B Observational Analysis}
527	\label{sec:72b}
528	
529	As a directional probe at frontier scale, we apply ContamCal to Qwen2.5-72B using only Self-Critique (estimated AUC 0.61) and ConStat (estimated AUC 0.55). The $\gamma$ posterior mean is 0.10 with 95\% CI [$-$0.09, 0.30], which does not exclude zero --- we cannot confirm or refute contamination at this scale. The calibration adjustment is small (2.1\,pp) with wide CI (14.8\,pp). This result is consistent with contamination dilution in larger training corpora and confirms no scale-specific artifacts, though signal quality at this scale precludes definitive conclusions.
530	
531	% ============================================================
532	\section{Discussion}
533	
534	\paragraph{When ContamCal works well.}
535	In the SFT regime with detection signal AUC $\geq$ 0.70, ContamCal provides effective calibration (MAE $\leq$ 5\,pp) with credible intervals that have near-nominal coverage. The framework is most effective on multiple-choice benchmarks (MMLU, ARC-C) where detection signals are strongest and item counts are largest.
536	
537	\paragraph{When ContamCal reaches its limits.}
538	Three conditions degrade calibration quality: (1)~RL post-training collapses most detection signals, leaving only Self-Critique (AUC $\approx$ 0.63), which produces wide CIs ($\sim$17\,pp) with limited decision value. (2)~Low contamination dosage ($\leq$5\%) falls below the identifiability floor. (3)~Code generation benchmarks (HumanEval) are consistently hardest due to irregular token distributions and execution-based evaluation noise.
539	
540	\paragraph{Identifiability boundaries.}
541	Our noise propagation analysis (Section~\ref{sec:noise}) establishes that when composite detection AUC falls below $\approx$0.65, CI widths exceed 15\,pp and calibrated scores offer diminishing practical utility. This threshold serves as an explicit identifiability guarantee: ContamCal reports when its own estimates should not be trusted.
542	
543	\paragraph{The value of honest uncertainty.}
544	The RL case study illustrates that even imprecise calibration has value. Wide CIs do not mean useless CIs --- they correctly communicate that benchmark rankings are unreliable, enabling more informed model selection (17\% regret reduction) compared to treating inflated scores as ground truth.
545	
546	\paragraph{Limitations.}
547	(1)~Controlled validation uses SFT injection, which may not fully reproduce naturalistic contamination patterns.
548	(2)~Scale validation extends only to 7B controlled / 72B observational; frontier models ($>$70B) remain inadequately validated.
549	(3)~95\% CI coverage (0.89) is below nominal, indicating mild model misspecification.
550	(4)~Computational cost ($\sim$40 minutes per benchmark for MCMC) may limit adoption.
551	
552	% ============================================================
553	\section{Conclusion}
554	
555	We presented ContamCal, a two-stage framework for calibrating contaminated benchmark scores via contamination-augmented IRT. In the SFT regime where detection signals achieve AUC $\geq$ 0.70, ContamCal recovers true model performance with 4.2\,pp MAE and 89\% credible interval coverage, improving over the best baseline by 14\%. RRF aggregation provides robust signal combination with graceful degradation to a 2-signal closed-weight mode. For RL-trained models, ContamCal produces appropriately wide intervals that honestly reflect detection limitations while still reducing model-selection regret by 17\%. Simulation-based identifiability analysis provides explicit boundaries --- defining not only when calibration works but when it does not --- shifting the contribution from calibration accuracy toward principled identifiability guarantees.
556	
557	\paragraph{Future work.}
558	(1)~Developing RL-robust detection signals to narrow RL-regime CIs.
559	(2)~Scaling controlled validation beyond 7B.
560	(3)~Incorporating measurement error models to improve coverage under high noise.
561	(4)~Extending to contamination from synthetic data and data augmentation pipelines.
562	
563	% ============================================================
564	% References (abbreviated for review)
565	\begin{thebibliography}{10}
566	\bibitem{dong2025emperor}
567	Dong, G., et al.
568	\newblock Emperor's New Clothes: Benchmarking LLM decontamination strategies.
569	\newblock In \emph{ICML}, 2025.
570	
571	\bibitem{eckerly2017}
572	Eckerly, C.
573	\newblock Detecting item compromise in IRT models.
574	\newblock \emph{Applied Measurement in Education}, 30(2), 2017.
575	
576	\bibitem{sinharay2017}
577	Sinharay, S.
578	\newblock Detection of item preknowledge using likelihood ratio test and score test.
579	\newblock \emph{Journal of Educational and Behavioral Statistics}, 42(1), 2017.
580	
581	\bibitem{shi2023minkpp}
582	Shi, W., et al.
583	\newblock Detecting pretraining data from large language models.
584	\newblock In \emph{ICLR}, 2024.
585	
586	\bibitem{golchin2024constat}
587	Golchin, S. and Surdeanu, M.
588	\newblock Time travel in LLMs: Tracing data contamination in large language models.
589	\newblock In \emph{ICLR}, 2024.
590	
591	\bibitem{balachandran2024dcr}
592	Balachandran, V., et al.
593	\newblock Data contamination calibration for ranking LLMs.
594	\newblock \emph{arXiv preprint}, 2024.
595	
596	\bibitem{raina2024growingpains}
597	Raina, V., et al.
598	\newblock Growing pains: Understanding how scaling and item difficulty affect LLM evaluation via IRT.
599	\newblock In \emph{ACL}, 2024.
600	
601	\bibitem{polo2024atlas}
602	Polo, F., et al.
603	\newblock ATLAS: Adaptive testing using LLM-based item response theory.
604	\newblock In \emph{NeurIPS}, 2024.
605	
606	\bibitem{ni2024hibayes}
607	Ni, A., et al.
608	\newblock HiBayES: Hierarchical Bayesian estimation of LLM abilities.
609	\newblock \emph{arXiv preprint}, 2024.
610	
611	\bibitem{cormack2009rrf}
612	Cormack, G., Clarke, C., and Buettcher, S.
613	\newblock Reciprocal rank fusion outperforms condorcet and individual rank learning methods.
614	\newblock In \emph{SIGIR}, 2009.
615	\end{thebibliography}
616	
617	\end{document}
618	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88a53412-82a2-4b33-85fe-84cf2878a8d9",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "5fccc3f8-15f5-40cb-bd72-db40612b2aa0",
  "sourceToolAssistantUUID": "88a53412-82a2-4b33-85fe-84cf2878a8d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-13T16:23:44.287Z_

Now let me check for any existing dream review reports.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fccc3f8-15f5-40cb-bd72-db40612b2aa0",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazsqfSSLKFVreaEPg9De",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3c90e79-3b2a-4d9c-a13a-aabc72aa1ad9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDfZzHkMyGEx82u9UNJ1vJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29056,
      "cache_read_input_tokens": 38368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29056,
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

_source line 37 · 2026-05-13T16:23:46.905Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Xy6bGZaKzcv8z3NSJ9oVpM`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3c90e79-3b2a-4d9c-a13a-aabc72aa1ad9",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazsqfSSLKFVreaEPg9De",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7e45477-3b22-4740-976c-b6d658fab491",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDfZzHkMyGEx82u9UNJ1vJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29056,
      "cache_read_input_tokens": 38368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29056,
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

_source line 38 · 2026-05-13T16:23:46.923Z_

<details><summary>↩ Tool result · `toolu_01Xy6bGZaKzcv8z3NSJ9oVpM`</summary>

```text
artifacts/dream_reports/dream_20260513T155040/best/paper_framing.md
artifacts/dream_reports/dream_20260513T155040/median/paper_framing.md
artifacts/dream_reports/dream_20260513T155040/worst/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7e45477-3b22-4740-976c-b6d658fab491",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "0927a677-5fd0-4481-ba32-eb5b853491b5",
  "sourceToolAssistantUUID": "e7e45477-3b22-4740-976c-b6d658fab491",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-13T16:23:47.217Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TecTBrFxJTZRFd1pEZszLJ`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0927a677-5fd0-4481-ba32-eb5b853491b5",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazsqfSSLKFVreaEPg9De",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e33698bd-ff00-47b1-8b81-aef7cb8317e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QDfZzHkMyGEx82u9UNJ1vJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 29056,
      "cache_read_input_tokens": 38368,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 29056
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 38368,
          "cache_creation_input_tokens": 29056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 29056,
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

_source line 40 · 2026-05-13T16:23:47.260Z_

<details><summary>↩ Tool result · `toolu_01TecTBrFxJTZRFd1pEZszLJ`</summary>

```text
registry.yaml
decisions.yaml
experiment_plan.yaml
artifacts/dream_reports/dream_20260513T155040/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T155040/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T155040/worst/imagined_experiments.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260513T155040/best/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e33698bd-ff00-47b1-8b81-aef7cb8317e6",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "66484403-abf6-4e2d-8194-e729f76df9d0",
  "sourceToolAssistantUUID": "e33698bd-ff00-47b1-8b81-aef7cb8317e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-13T16:23:50.881Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qrtm2at5EdYKbqDwvdFNDj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66484403-abf6-4e2d-8194-e729f76df9d0",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazsrBGKCgKo2a3TNrhkK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8eabfb82-0401-467b-a159-4955e44db2d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFpXS3gvrwZW9ZDqcrDhC3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 67424,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 458,
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

_source line 42 · 2026-05-13T16:23:50.888Z_

<details><summary>↩ Tool result · `toolu_01Qrtm2at5EdYKbqDwvdFNDj`</summary>

```text
1	narrative_guidance: '原始framing完全成立：ContamCal是benchmark contamination的"statistical
2	  safety net"， 三条claims按原始强度表述。Headline: "ContamCal recovers true performance within
3	  2pp MAE with 93% CI coverage, while naive scores overestimate by 8-12pp." RL宽CI叙事自然成立——"wide
4	  CIs are the correct answer"用expected regret量化证明。投AAAI无需调整framing。
5	
6	  '
7	imagined_experiments:
8	- name: controlled_sft_injection
9	  plan_id: exp-001
10	  description: 'Qwen2.5-0.5B/1.5B/3B × 5 dosage levels (0%/5%/25%/50%/100%) SFT注入，
11	    生成15个contaminated/clean模型对作为ground truth。
12	
13	    '
14	  expected_results:
15	    sft_runs_completed: 15
16	    dosage_0pct_acc_delta_mmlu_pp: 0.0
17	    dosage_5pct_acc_inflation_mmlu_pp: 2.1
18	    dosage_25pct_acc_inflation_mmlu_pp: 5.8
19	    dosage_50pct_acc_inflation_mmlu_pp: 9.3
20	    dosage_100pct_acc_inflation_mmlu_pp: 12.6
21	    dosage_25pct_acc_inflation_gsm8k_pp: 4.2
22	    dosage_25pct_acc_inflation_arc_pp: 5.1
23	    dosage_25pct_acc_inflation_humaneval_pp: 7.5
24	    scale_0_5B_mean_inflation_50pct_pp: 10.8
25	    scale_1_5B_mean_inflation_50pct_pp: 9.1
26	    scale_3B_mean_inflation_50pct_pp: 8.2
27	    dose_response_spearman_across_all: 0.97
28	    convergence_failures: 0
29	  result_rationale: 'best档下SFT注入实验完全按预期工作。paraphrase-based injection在5%剂量时已产生可测量的2pp
30	    inflation， 100%剂量下MMLU膨胀达12.6pp，与Emperor''s New Clothes报告的8-15pp范围一致。 较小模型(0.5B)受contamination影响更大（memorization
31	    capacity占比更高）， 3B模型因能力更强、泛化更好而inflation略低。GSM8K因reasoning chain结构使得 memorization效果弱于纯knowledge
32	    recall的MMLU。HumanEval inflation最高因为 code solutions更容易被精确记忆。dose-response严格单调（spearman=0.97），
33	    为后续IRT建模提供理想的ground truth梯度。
34	
35	    '
36	  tables:
37	  - name: 'Table 1: Accuracy Inflation (pp) by Model Scale × Dosage × Benchmark'
38	    rows: 60
39	    columns:
40	    - model
41	    - benchmark
42	    - dosage
43	    - clean_acc
44	    - contaminated_acc
45	    - inflation_pp
46	  figures_description:
47	  - 'Fig 1: Dose-response curves (dosage vs inflation) for each model×benchmark combination,
48	    12 panels, showing strict monotonicity'
49	  analysis: '所有15个SFT run成功收敛。inflation幅度在MMLU上与文献一致。 关键观察：inflation并非线性——25%→50%的增量大于5%→25%，表明contamination效果存在加速区间，
50	    支持非线性4PL建模的必要性。跨benchmark一致性强，为Claim 1提供坚实的ground truth基础。
51	
52	    '
53	- name: stage1_signal_pipeline
54	  plan_id: exp-002
55	  description: '在exp-001的所有模型上计算4种检测信号：embedding retrieval, Min-K%++, ConStat, Self-Critique。输出per-model-item
56	    exposure scores。
57	
58	    '
59	  expected_results:
60	    embedding_retrieval_auc_sft_mean: 0.88
61	    mink_pp_auc_sft_mean: 0.84
62	    constat_auc_sft_mean: 0.82
63	    self_critique_auc_sft_mean: 0.79
64	    embedding_retrieval_auc_at_5pct_dosage: 0.76
65	    mink_pp_auc_at_5pct_dosage: 0.71
66	    constat_auc_at_5pct_dosage: 0.68
67	    self_critique_auc_at_5pct_dosage: 0.66
68	    signal_pairwise_rank_corr_max: 0.52
69	    signal_pairwise_rank_corr_min: 0.28
70	    items_with_all4_signals_agree_contaminated_pct: 0.73
71	    items_with_disagreement_pct: 0.27
72	  result_rationale: 'best档下所有4个信号都有效但各有侧重。Embedding retrieval AUC最高(0.88)因为 paraphrase-based
73	    injection保留了语义相似性，FAISS能直接捕获。Min-K%++次之(0.84) 因为SFT后model perplexity在seen items上显著降低。ConStat(0.82)通过original
74	    vs paraphrase performance gap检测有效但受paraphrase质量影响。Self-Critique最低(0.79) 因为依赖模型自身判断，噪声更大，但仍远超chance。在低剂量(5%)时所有信号AUC下降约0.1，
75	    这是合理的——更少的contaminated items意味着更弱的统计信号。 信号间相关性适中(0.28-0.52)，说明它们捕获的是complementary
76	    information， 为RRF融合提供理想条件。
77	
78	    '
79	  tables:
80	  - name: 'Table 2: Per-Signal AUC by Model × Dosage'
81	    rows: 60
82	    columns:
83	    - model
84	    - dosage
85	    - embedding_auc
86	    - mink_auc
87	    - constat_auc
88	    - selfcritique_auc
89	  figures_description:
90	  - 'Fig 2: Signal AUC heatmap (signal × dosage), averaged across models and benchmarks'
91	  - 'Fig 3: Pairwise signal rank correlation matrix (4×4)'
92	  analysis: '信号质量全面达到best档预期。关键发现：信号间低-中等相关性(mean=0.38)证实 complementarity假设，为RRF融合奠定基础。HumanEval上embedding
93	    retrieval AUC 特别高(0.92)因为code的语义embedding更具区分性。
94	
95	    '
96	- name: rrf_aggregation_ablation
97	  plan_id: exp-003
98	  description: 'RRF融合4信号为composite exposure score。消融实验：RRF vs rank averaging, 单信号,
99	    calibration-weighted RRF, FP注入鲁棒性, 2-signal降级模式。
100	
101	    '
102	  expected_results:
103	    rrf_4signal_auc: 0.87
104	    rank_averaging_auc: 0.84
105	    best_single_signal_auc: 0.88
106	    calibration_weighted_rrf_auc: 0.86
107	    rrf_minus_best_single_delta_auc: -0.01
108	    rrf_auc_at_fp_rate_10pct: 0.84
109	    rrf_auc_at_fp_rate_20pct: 0.8
110	    degraded_2signal_auc: 0.78
111	    rrf_4signal_vs_2signal_delta: 0.09
112	    rrf_exposure_score_spearman_with_true_dosage: 0.91
113	    rank_stability_bootstrap_cv: 0.04
114	  result_rationale: 'best档下RRF融合AUC(0.87)接近最好的单信号(embedding 0.88)但关键优势在于鲁棒性： RRF在所有benchmark上都稳定达到0.85+，而单信号表现波动大（embedding在GSM8K上可能
115	    降到0.80，ConStat在HumanEval上可能降到0.75）。RRF比rank averaging高3pp因为 reciprocal rank weighting对高置信排名给予更大权重。Calibration-weighted
116	    RRF略低于 vanilla RRF因为权重估计引入了额外noise，且在best档的高信号质量下vanilla RRF已足够。 FP注入10%时AUC仅降3pp，20%时降7pp，证明graceful
117	    degradation。 2-signal模式(ConStat+Self-Critique)AUC=0.78，比4-signal低9pp但仍远超chance，
118	    满足closed-weight场景的可用性。exposure score与true dosage的spearman=0.91 证明RRF输出确实捕获了contamination程度的有序信息。
119	
120	    '
121	  tables:
122	  - name: 'Table 3: RRF Ablation Results'
123	    rows: 8
124	    columns:
125	    - method
126	    - auc_mmlu
127	    - auc_gsm8k
128	    - auc_arc
129	    - auc_humaneval
130	    - auc_mean
131	    - auc_std
132	  - name: 'Table 4: FP Injection Robustness'
133	    rows: 4
134	    columns:
135	    - fp_rate
136	    - rrf_auc
137	    - delta_from_clean
138	  figures_description:
139	  - 'Fig 4: Signal dropout ablation bar chart — AUC by combination (4-signal, each
140	    3-signal, each single, 2-signal degraded)'
141	  - 'Fig 5: RRF exposure score vs true dosage scatter plot with Spearman annotation'
142	  analysis: 'RRF fusion的核心价值不在于AUC绝对值（最好的单信号可能匹配），而在于跨benchmark、 跨模型的一致性和FP鲁棒性。这直接支持Claim
143	    2的"outperforming any single signal"—— 含义是worst-case performance更优，而非mean AUC更高。2-signal降级模式AUC=0.78
144	    为closed-weight实用性提供了有力支撑。
145	
146	    '
147	- name: noise_propagation_analysis
148	  plan_id: exp-005
149	  description: '校准noise注入到exposure scores中：估计per-item FP/FN率， 注入matched/1.5×/2×高斯噪声，重新拟合IRT，测量CI宽化。
150	
151	    '
152	  expected_results:
153	    selfcritique_estimated_fp_rate: 0.12
154	    selfcritique_estimated_fn_rate: 0.18
155	    matched_noise_ci_width_gamma_pp: 5.2
156	    noise_1_5x_ci_width_gamma_pp: 6.8
157	    noise_2x_ci_width_gamma_pp: 8.9
158	    matched_noise_ci_coverage_95: 0.94
159	    noise_1_5x_ci_coverage_95: 0.96
160	    noise_2x_ci_coverage_95: 0.97
161	    gamma_rel_bias_at_matched_noise: 0.06
162	    gamma_rel_bias_at_2x_noise: 0.09
163	    theta_corr_at_matched_noise: 0.94
164	    theta_corr_at_2x_noise: 0.89
165	    measurement_error_model_dic_improvement: 12.3
166	  result_rationale: 'best档下noise propagation表现理想：随着noise增加，CI合理宽化（5.2→8.9pp）而非崩溃，
167	    coverage从94%略升至97%（略过覆盖而非欠覆盖）。这说明Bayesian posterior正确地将 exposure score uncertainty吸收进了参数不确定性。gamma相对偏差从0.06增到0.09，
168	    表明点估计稳健性在2×noise下仍可接受。theta相关性从0.94降至0.89，下降幅度合理—— 更多noise意味着contamination信号更弱，ability估计回退向vanilla
169	    IRT。 Self-Critique的FP=12%/FN=18%在best档下是合理的——比embedding差但比random好得多。 measurement
170	    error扩展模型DIC改善12.3说明显式建模exposure noise有统计意义上的价值。
171	
172	    '
173	  tables:
174	  - name: 'Table 5: Noise Propagation Results'
175	    rows: 4
176	    columns:
177	    - noise_level
178	    - gamma_mean
179	    - gamma_rel_bias
180	    - ci_width_pp
181	    - ci_coverage_95
182	    - theta_corr
183	  figures_description:
184	  - 'Fig 6: CI width vs noise level line plot, with coverage annotated at each point'
185	  - 'Fig 7: θ recovery correlation scatterplots at 3 noise levels (1×, 1.5×, 2×)'
186	  analysis: '核心结论：4PL+γ的Bayesian formulation天然支持noise propagation——更noisy的exposure
187	    scores产生更宽的CI而不是更差的点估计。这直接支持Claim 3，也为RL regime下 Self-Critique-only信号的wider CIs提供了机制解释。
188	
189	    '
190	- name: irt_calibration_and_baselines
191	  plan_id: exp-006
192	  description: '在exp-001/003的controlled数据上拟合4PL+γ IRT (Stan NUTS)， 计算calibrated scores，与5个baselines比较，评估5个指标。
193	
194	    '
195	  expected_results:
196	    contam_cal_mae_pp_mmlu: 1.8
197	    contam_cal_mae_pp_gsm8k: 2.1
198	    contam_cal_mae_pp_arc: 1.6
199	    contam_cal_mae_pp_humaneval: 2.4
200	    contam_cal_mae_pp_mean: 1.97
201	    contam_cal_ci_coverage_95: 0.93
202	    contam_cal_ci_coverage_80: 0.84
203	    contam_cal_ci_coverage_50: 0.55
204	    contam_cal_ci_width_95_pp: 5.8
205	    contam_cal_kendall_tau: 0.91
206	    contam_cal_dose_response_spearman: 0.96
207	    baseline_remove_rescore_mae_pp: 4.2
208	    baseline_single_2plg_mae_pp: 3.8
209	    baseline_vanilla_4pl_mae_pp: 6.1
210	    baseline_linear_regression_mae_pp: 3.5
211	    baseline_emperor_mitigation_mae_pp: 5.7
212	    best_baseline_mae_pp: 3.5
213	    margin_over_best_baseline_mae_relative: 0.44
214	    naive_score_overestimation_50pct_dosage_pp: 9.3
215	    gamma_posterior_mean: 0.42
216	    gamma_posterior_sd: 0.08
217	    gamma_rel_bias_real_data: 0.06
218	    theta_corr_with_ground_truth: 0.95
219	    theta_gamma_posterior_corr: 0.31
220	    nuts_divergent_pct: 0.0
221	    nuts_max_rhat: 1.005
222	    nuts_ess_min: 800
223	  result_rationale: 'best档核心实验。4PL+γ MAE=1.97pp完全复现仿真表现——真实SFT数据上的contamination 结构与仿真假设匹配良好。MMLU
224	    MAE最低(1.8pp)因为item数量最多(14K)提供了最强的 统计功效；HumanEval最高(2.4pp)因为item少且code execution评分的binary
225	    nature 增加了noise。93% coverage接近nominal 95%，略低是因为real data的item heterogeneity 比仿真更大，但仍在可接受范围。CI宽度5.8pp在sharpness和coverage间取得了好的平衡。
226	
227	    Baselines方面：vanilla 4PL(无γ)MAE=6.1pp最差，因为完全忽略contamination， 证明contamination covariate是必要的。Emperor''s
228	    mitigation MAE=5.7pp次差， 与ICML 2025发现一致——mitigation strategies确实不够有效。Linear regression
229	    MAE=3.5pp 是最好的baseline，但仍比ContamCal差44%——IRT的优势在于non-linear item response 建模和proper
230	    uncertainty propagation。Remove-rescore MAE=4.2pp受限于binary flagging丢失了contamination程度信息。Single-signal
231	    2PL+γ MAE=3.8pp表明 signal fusion和4PL复杂度各贡献了一部分改善。
232	
233	    θ-γ posterior correlation=0.31 < 0.4阈值，证实identifiability。 gamma rel_bias=0.06与仿真的0.068几乎一致。NUTS诊断完美——无divergence，
234	    Rhat<1.01，ESS>800。
235	
236	    '
237	  tables:
238	  - name: 'Table 6 (Main Result): Calibration Performance — ContamCal vs 5 Baselines'
239	    rows: 6
240	    columns:
241	    - method
242	    - mae_mmlu
243	    - mae_gsm8k
244	    - mae_arc
245	    - mae_humaneval
246	    - mae_mean
247	    - ci_coverage_95
248	    - ci_width_95
249	    - kendall_tau
250	  - name: 'Table 7: Per-Benchmark Detailed Metrics'
251	    rows: 4
252	    columns:
253	    - benchmark
254	    - mae_pp
255	    - coverage_50
256	    - coverage_80
257	    - coverage_95
258	    - ci_width_95_pp
259	    - kendall_tau
260	    - dose_response_spearman
261	  - name: 'Table 8: MCMC Diagnostics'
262	    rows: 4
263	    columns:
264	    - benchmark
265	    - divergent_pct
266	    - max_rhat
267	    - min_ess
268	    - fit_time_sec
269	  figures_description:
270	  - 'Fig 8 (Main Figure): Calibrated vs true accuracy scatter plot, all benchmarks,
271	    with 95% CI error bars, diagonal reference line'
272	  - 'Fig 9: MAE bar chart — ContamCal vs 5 baselines, per benchmark'
273	  - 'Fig 10: Dose-response curves — γ effect size vs contamination dosage, 4 benchmark
274	    panels'
275	  - 'Fig 11: Coverage calibration plot — nominal vs empirical coverage at 50/80/95%
276	    levels'
277	  analysis: '这是论文的核心结果表。MAE 1.97pp vs best baseline 3.5pp (44% relative improvement)
278	    提供了Claim 1的强有力支撑。93% coverage证明CI可靠。headline result可直接写为 "ContamCal recovers true
279	    performance within 2pp MAE with 93% CI coverage, while naive scores overestimate
280	    by 8-12pp." Kendall τ=0.91证明model ranking 在calibration后基本保持正确——contamination改变的是绝对分数而非相对排名，
281	    但ContamCal在absolute calibration上的优势对于跨benchmark比较至关重要。
282	
283	    '
284	- name: scale_bridging_7b
285	  plan_id: exp-007
286	  description: 'Qwen2.5-7B在5个dosage水平下的controlled SFT注入，验证calibration在更大模型上的有效性。
287	
288	    '
289	  expected_results:
290	    dosage_25pct_acc_inflation_mmlu_pp: 4.8
291	    dosage_50pct_acc_inflation_mmlu_pp: 7.6
292	    dosage_100pct_acc_inflation_mmlu_pp: 10.2
293	    contam_cal_mae_pp_mean_7b: 2.2
294	    contam_cal_ci_coverage_95_7b: 0.92
295	    contam_cal_kendall_tau_7b: 0.89
296	    mae_increase_vs_3b_pp: 0.3
297	    gamma_mean_7b: 0.38
298	    dose_response_spearman_7b: 0.94
299	  result_rationale: 'best档下7B模型表现略弱于0.5-3B但仍在acceptable范围内。7B的inflation略低于小模型 (50%
300	    dosage: 7.6pp vs 9.3pp mean for smaller)因为7B的更强泛化能力意味着 contamination的relative
301	    contribution更小。MAE略增至2.2pp(+0.3pp vs 3B)因为 7B模型的item response pattern更复杂，但仍远优于baselines。gamma估计值0.38略低于
302	    小模型的0.42，反映了contamination对larger model的较小相对效应。 Coverage 92%和Kendall τ=0.89仍然强劲，证明ContamCal可扩展到7B规模。
303	
304	    '
305	  tables:
306	  - name: 'Table 9: 7B Scale Bridging Results'
307	    rows: 5
308	    columns:
309	    - dosage
310	    - inflation_pp
311	    - contam_cal_mae_pp
312	    - ci_coverage_95
313	    - kendall_tau
314	  figures_description:
315	  - 'Fig 12: MAE vs model scale line plot (0.5B, 1.5B, 3B, 7B) showing graceful degradation'
316	  analysis: '7B结果证明ContamCal从小模型到中等规模模型的可扩展性。MAE增加有限(+0.3pp) 且符合理论预期——更大的模型有更复杂的ability
317	    landscape但contamination的相对效应更小。
318	
319	    '
320	- name: signal_survival_analysis
321	  plan_id: exp-008
322	  description: '检测信号在不同训练regime下的可靠性系统评估。 Signal × regime AUC heatmap: 4 signals ×
323	    {base, SFT-clean, SFT-contaminated, RL-post-trained}。
324	
325	    '
326	  expected_results:
327	    embedding_auc_base: 0.9
328	    embedding_auc_sft_clean: 0.51
329	    embedding_auc_sft_contam: 0.88
330	    embedding_auc_rl: 0.55
331	    mink_auc_base: 0.86
332	    mink_auc_sft_clean: 0.53
333	    mink_auc_sft_contam: 0.84
334	    mink_auc_rl: 0.58
335	    constat_auc_base: 0.5
336	    constat_auc_sft_clean: 0.5
337	    constat_auc_sft_contam: 0.82
338	    constat_auc_rl: 0.67
339	    selfcritique_auc_base: 0.5
340	    selfcritique_auc_sft_clean: 0.5
341	    selfcritique_auc_sft_contam: 0.79
342	    selfcritique_auc_rl: 0.72
343	    signal_survival_rl_best: Self-Critique
344	    signal_survival_rl_second: ConStat
345	  result_rationale: 'best档下信号存活模式清晰：embedding和Min-K%++在SFT-contaminated上表现强劲 (0.88/0.84)但在RL后严重降级(0.55/0.58)——RL的policy
346	    gradient更新破坏了 token-level memorization pattern，使得perplexity-based信号失效。 ConStat在RL后保留AUC=0.67因为它测量的是performance
347	    gap(original vs paraphrase) 这一higher-level信号，不依赖model internals。Self-Critique在RL后最强(0.72)
348	    因为它利用模型的reasoning能力来自我评估，RL强化了这种元认知能力而非削弱。 base模型和SFT-clean模型上ConStat和Self-Critique接近chance(0.50)是正确的——
349	    没有contamination时不应有信号（specificity验证）。 这个heatmap直接支持RRF fusion的必要性：没有任何单一信号在所有regime下都最优。
350	
351	    '
352	  tables:
353	  - name: 'Table 10 (Supporting Contribution): Signal × Regime AUC Heatmap'
354	    rows: 4
355	    columns:
356	    - signal
357	    - base
358	    - sft_clean
359	    - sft_contam
360	    - rl_post_trained
361	  figures_description:
362	  - 'Fig 13: Signal survival heatmap (4×4 matrix, color-coded by AUC)'
363	  - 'Fig 14: Per-signal AUC degradation from SFT→RL, paired bar chart'
364	  analysis: '这是论文的Supporting Contribution 5。关键insight：RL post-training创造了一个 "signal
365	    desert"——只有Self-Critique和ConStat存活。这解释了为什么RL regime 需要更宽的CI（更少信号→更大不确定性），同时也为2-signal
366	    degraded mode提供了 empirical justification。
367	
368	    '
369	- name: rl_observational_case_study
370	  plan_id: exp-009
371	  description: '对现有RL-trained模型(Qwen2.5-Instruct系列, DeepSeek-R1-Distill系列) 应用Self-Critique
372	    + available signals，拟合IRT with wider CIs， expected regret量化。
373	
374	    '
375	  expected_results:
376	    selfcritique_auc_rl_models_mean: 0.71
377	    available_signals_rl_count: 2
378	    contam_cal_ci_width_95_rl_pp: 11.4
379	    contam_cal_ci_width_95_sft_comparison_pp: 5.8
380	    ci_width_ratio_rl_vs_sft: 1.97
381	    expected_regret_uncalibrated: 0.38
382	    expected_regret_calibrated_wide_ci: 0.22
383	    expected_regret_remove_rescore: 0.31
384	    regret_reduction_vs_uncalibrated: 0.42
385	    regret_reduction_vs_remove_rescore: 0.29
386	    near_zero_gamma_clean_benchmark_check: 0.03
387	    gamma_posterior_rl_mean: 0.28
388	    gamma_posterior_rl_sd: 0.14
389	    gamma_ci_includes_zero_rl: false
390	    num_models_rl_case: 8
391	    kendall_tau_rl_top5_selection: 0.8
392	  result_rationale: 'best档下RL observational case study展示了"wide CIs are the correct
393	    answer"的完整叙事。 Self-Critique AUC=0.71（略超0.70阈值）在RL模型上提供了可用但noisy的信号。 CI宽度11.4pp约为SFT的2倍——这不是方法失败，而是正确反映了RL
394	    regime下检测信号的 更大不确定性。gamma posterior mean=0.28 (sd=0.14)表明RL模型确实存在contamination
395	    效应但估计更不确定；CI不包含0证明信号是directionally informative的。
396	
397	    Expected regret量化是关键：uncalibrated选择top-5模型的expected regret=0.38， 使用wide-CI calibrated
398	    scores后降至0.22（42% reduction），优于remove-rescore的0.31。 机制：即使CI很宽，calibrated scores的point
399	    estimate仍然比naive scores更准确， 而wide CI让决策者知道应该对RL模型的排名更谨慎。
400	
401	    Near-zero gamma check在known-clean benchmark上γ=0.03(接近0)， 通过specificity检验——模型不会对uncontaminated
402	    data产生false alarm。
403	
404	    '
405	  tables:
406	  - name: 'Table 11: RL Case Study — Expected Regret Comparison'
407	    rows: 3
408	    columns:
409	    - method
410	    - expected_regret
411	    - regret_reduction_vs_naive
412	    - top5_kendall_tau
413	  - name: 'Table 12: RL vs SFT CI Width Comparison'
414	    rows: 2
415	    columns:
416	    - regime
417	    - mean_ci_width_95_pp
418	    - gamma_mean
419	    - gamma_sd
420	    - signal_count
421	  figures_description:
422	  - 'Fig 15: RL vs SFT credible interval width comparison (paired model bar chart)'
423	  - 'Fig 16: Expected regret cumulative plot — uncalibrated vs calibrated vs remove-rescore'
424	  - 'Fig 17: Near-zero gamma check — posterior density on clean benchmark showing
425	    mass near zero'
426	  analysis: 'RL case study的叙事完美支持Claim 3。核心message不是"ContamCal在RL上也很准" （那不诚实），而是"ContamCal在RL上给出了appropriately
427	    uncertain的答案， 这些uncertain answers仍然改善了决策"。42% regret reduction是一个compelling number。
428	    Near-zero gamma specificity check排除了"方法总是报告contamination"的担忧。
429	
430	    '
431	- name: prior_sensitivity
432	  plan_id: exp-010
433	  description: '使用γ prior N(0,0.5)和N(0,2)（默认N(0,1)）重新拟合IRT， 验证calibrated scores和CIs对prior选择的鲁棒性。
434	
435	    '
436	  expected_results:
437	    mae_prior_tight_n05: 2.1
438	    mae_prior_default_n10: 1.97
439	    mae_prior_wide_n20: 2.0
440	    coverage_95_prior_tight: 0.91
441	    coverage_95_prior_default: 0.93
442	    coverage_95_prior_wide: 0.95
443	    ci_width_prior_tight_pp: 4.9
444	    ci_width_prior_default_pp: 5.8
445	    ci_width_prior_wide_pp: 7.1
446	    gamma_mean_prior_tight: 0.39
447	    gamma_mean_prior_default: 0.42
448	    gamma_mean_prior_wide: 0.44
449	    max_mae_diff_across_priors_pp: 0.13
450	    kendall_tau_prior_tight: 0.9
451	    kendall_tau_prior_default: 0.91
452	    kendall_tau_prior_wide: 0.91
453	  result_rationale: 'best档下prior sensitivity表现理想：三种prior下MAE差异仅0.13pp，Kendall τ几乎
454	    不变(0.90-0.91)。tight prior N(0,0.5)略微shrink了gamma估计(0.39 vs 0.42) 导致MAE略高(2.1pp)，但差异很小。wide
455	    prior N(0,2)允许gamma更大(0.44)且CI更宽 (7.1pp vs 5.8pp)，coverage从93%升至95%但sharpness代价可接受。
456	    这种行为说明：(1)数据信息量足够大，prior的影响被likelihood dominated； (2)在best档的高信号质量下，任何reasonable
457	    prior都能得到好的结果。 这直接回应了"prior choice drives results"的潜在reviewer concern。
458	
459	    '
460	  tables:
461	  - name: 'Table 13: Prior Sensitivity Analysis'
462	    rows: 3
463	    columns:
464	    - prior
465	    - mae_pp
466	    - coverage_95
467	    - ci_width_pp
468	    - gamma_mean
469	    - kendall_tau
470	  figures_description:
471	  - 'Fig 18: Prior sensitivity — MAE and CI width across 3 prior choices, error bars'
472	  analysis: 'Prior sensitivity结果证明方法稳健。MAE变化<0.15pp且ranking完全稳定， 满足了Bayesian方法的基本robustness要求。default
473	    prior N(0,1)在 coverage/sharpness trade-off上最优。
474	
475	    '
476	- name: few_examinee_regime
477	  plan_id: exp-011
478	  description: '仿真研究：model count 20/50/100/200下的IRT性能。 两阶段估计策略：用Growing Pains 400+模型池预估item参数作为informative
479	    priors。
480	
481	    '
482	  expected_results:
483	    mae_pp_n20_no_preestimate: 4.8
484	    mae_pp_n20_with_preestimate: 2.9
485	    mae_pp_n50_no_preestimate: 2.8
486	    mae_pp_n50_with_preestimate: 2.1
487	    mae_pp_n100_no_preestimate: 2.0
488	    mae_pp_n100_with_preestimate: 1.9
489	    mae_pp_n200_no_preestimate: 1.7
490	    mae_pp_n200_with_preestimate: 1.7
491	    preestimate_benefit_n20_pp: 1.9
492	    preestimate_benefit_n50_pp: 0.7
493	    preestimate_benefit_n100_pp: 0.1
494	    coverage_95_n20_preestimate: 0.9
495	    coverage_95_n50_preestimate: 0.92
496	    coverage_95_n100_preestimate: 0.93
497	    gamma_rel_bias_n20_preestimate: 0.12
498	    gamma_rel_bias_n50_preestimate: 0.08
499	    min_viable_model_count: 50
500	  result_rationale: 'best档下few-examinee仿真展示了清晰的performance gradient和pre-estimation策略的价值。
501	    N=20裸跑MAE=4.8pp不可接受，但pre-estimation将其降至2.9pp——从Growing Pains的 400+模型池中借用item parameter
502	    estimates作为informative prior极大地稳定了估计。 N=50是一个sweet spot：裸跑MAE已降至2.8pp，pre-estimation进一步降至2.1pp。
503	    N=100+时pre-estimation的marginal benefit趋近于0（0.1pp），因为数据本身已足够。 min viable model
504	    count设为50（with pre-estimation），此时coverage 92%且 gamma rel_bias 8%都在可接受范围。这直接回应了reviewer
505	    concern #6 "too few models"。
506	
507	    '
508	  tables:
509	  - name: 'Table 14: Few-Examinee Regime Study'
510	    rows: 8
511	    columns:
512	    - n_models
513	    - preestimate
514	    - mae_pp
515	    - coverage_95
516	    - ci_width_pp
517	    - gamma_rel_bias
518	  figures_description:
519	  - 'Fig 19: MAE vs model count, with/without pre-estimation, two lines converging
520	    at N=100+'
521	  analysis: 'N=50 with pre-estimation是论文推荐的minimum viable configuration。 pre-estimation策略巧妙利用了existing
522	    model evaluation pools（如Growing Pains的 Open LLM Leaderboard数据），无需额外实验成本。
523	
524	    '
525	- name: observational_72b
526	  plan_id: exp-012
527	  description: 'Qwen2.5-72B观测分析（仅推理，无SFT）。将ecological validity扩展到frontier模型规模。
528	
529	    '
530	  expected_results:
531	    gamma_posterior_72b_mmlu: 0.18
532	    gamma_posterior_72b_gsm8k: 0.12
533	    gamma_ci_excludes_zero_72b_mmlu: true
534	    gamma_ci_excludes_zero_72b_gsm8k: false
535	    calibrated_score_shift_mmlu_pp: -3.2
536	    calibrated_score_shift_gsm8k_pp: -1.8
537	    ci_width_95_72b_pp: 8.5
538	    selfcritique_auc_72b_estimated: 0.68
539	    qualitative_consistency_with_7b: true
540	  result_rationale: 'best档下72B观测分析提供了重要的ecological validity但不能有ground truth验证。 gamma=0.18（MMLU）表明即使72B模型也存在可检测的contamination效应，但效应量小于
541	    小模型(0.42)——这合理因为72B的能力足够强使得contamination的relative contribution更小。 MMLU上gamma CI排除0说明信号存在；GSM8K上CI包含0说明reasoning
542	    benchmark对72B的 contamination效应可能在noise floor以下。calibrated score下调3.2pp（MMLU） 是一个substantive但不极端的correction。CI宽度8.5pp反映了observational
543	    setting 的更大不确定性。Self-Critique AUC=0.68略低于0.70阈值，但仍在"方向性有效"范围内。
544	
545	    '
546	  tables:
547	  - name: 'Table 15: 72B Observational Analysis'
548	    rows: 4
549	    columns:
550	    - benchmark
551	    - gamma_mean
552	    - gamma_ci_lower
553	    - gamma_ci_upper
554	    - calibrated_shift_pp
555	    - ci_width_pp
556	  figures_description:
557	  - 'Fig 20: Gamma estimates across model scales (0.5B→72B) showing decreasing trend'
558	  analysis: '72B结果支持"contamination effects exist at all scales but diminish with scale"的叙事。
559	    这是生态效度论证——不是定量验证，而是证明ContamCal在frontier scale下产生 plausible和internally consistent的结果。
560	
561	    '
562	- name: closed_weight_2signal_mode
563	  plan_id: exp-013
564	  description: '降级2-signal模式(ConStat + Self-Critique)的消融研究， 量化2-signal vs 4-signal的calibration
565	    accuracy差距。
566	
567	    '
568	  expected_results:
569	    contam_cal_2signal_mae_pp: 2.4
570	    contam_cal_4signal_mae_pp: 1.97
571	    mae_increase_2signal_relative: 0.1
572	    contam_cal_2signal_ci_coverage_95: 0.94
573	    contam_cal_2signal_ci_width_95_pp: 7.2
574	    contam_cal_2signal_kendall_tau: 0.87
575	    contam_cal_2signal_dose_response_spearman: 0.92
576	    still_beats_best_baseline: true
577	    margin_over_best_baseline_2signal_relative: 0.31
578	  result_rationale: 'best档下2-signal降级模式MAE增加10%(2.4pp vs 1.97pp)，在best档范围[0.05, 0.15]的
579	    中间位置。CI宽度从5.8pp增至7.2pp（+24%），coverage从93%升至94%——更宽的CI 正确补偿了更少信号带来的更大不确定性。Kendall
580	    τ从0.91降至0.87，ranking能力略降 但仍然strong。关键：2-signal模式仍然beat best baseline 31%（2.4pp
581	    vs 3.5pp）， 证明即使在closed-weight限制下ContamCal仍有实际价值。 MAE增加主要来自ConStat在某些benchmark上的noise较大（缺少embedding和Min-K%++
582	    的complementary information），但Self-Critique的reasoning-level信号提供了 必要的anchor。dose-response
583	    spearman=0.92仍然strong。
584	
585	    '
586	  tables:
587	  - name: 'Table 16: 2-Signal vs 4-Signal Degraded Mode Comparison'
588	    rows: 2
589	    columns:
590	    - mode
591	    - mae_pp
592	    - coverage_95
593	    - ci_width_pp
594	    - kendall_tau
595	    - margin_vs_baseline
596	  figures_description:
597	  - 'Fig 21: 2-signal vs 4-signal calibration accuracy per benchmark, grouped bar
598	    chart'
599	  analysis: 2-signal模式的10% MAE degradation是一个acceptable trade-off，证明ContamCal 可以gracefully
600	    degrade到closed-weight settings。论文可以confidence地claim "even without model internals
601	    access, ContamCal provides meaningful calibration improvement over baselines."
602	    这大幅扩展了方法的practical applicability。
603	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8eabfb82-0401-467b-a159-4955e44db2d0",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "5c8dbac9-be71-4619-b755-53662c35616d",
  "sourceToolAssistantUUID": "8eabfb82-0401-467b-a159-4955e44db2d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-13T16:23:51.419Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RDhceEBzNAZdp8HvPMX1de`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "experiment_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c8dbac9-be71-4619-b755-53662c35616d",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazsrBGKCgKo2a3TNrhkK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d494d7c-6389-47a0-af01-848c985c1c03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFpXS3gvrwZW9ZDqcrDhC3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 67424,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 458
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 67424,
          "cache_creation_input_tokens": 458,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 458,
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

_source line 44 · 2026-05-13T16:23:51.430Z_

<details><summary>↩ Tool result · `toolu_01RDhceEBzNAZdp8HvPMX1de`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d494d7c-6389-47a0-af01-848c985c1c03",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "1e090214-55be-43cf-824a-56af7fbfa5da",
  "sourceToolAssistantUUID": "0d494d7c-6389-47a0-af01-848c985c1c03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-13T16:23:54.765Z_

Now let me load the submission tool to post my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e090214-55be-43cf-824a-56af7fbfa5da",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazsrVG3CtrJVAxdsDWPs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "649b813d-8426-49db-b36e-11f720fb096f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qa6HiBVzQLR1tB35eKKMa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12662,
      "cache_read_input_tokens": 67882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12662,
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

_source line 46 · 2026-05-13T16:23:55.218Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016eTgN5UbDPebSGBN9ybVPo`</summary>

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
  "parentUuid": "649b813d-8426-49db-b36e-11f720fb096f",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazsrVG3CtrJVAxdsDWPs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e7baab7c-501b-4b3b-9b99-41650b52c3ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qa6HiBVzQLR1tB35eKKMa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12662,
      "cache_read_input_tokens": 67882,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12662
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 67882,
          "cache_creation_input_tokens": 12662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12662,
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

_source line 47 · 2026-05-13T16:23:55.220Z_

<details><summary>↩ Tool result · `toolu_016eTgN5UbDPebSGBN9ybVPo`</summary>

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
  "parentUuid": "e7baab7c-501b-4b3b-9b99-41650b52c3ba",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "0fe088a8-d34e-445c-bd36-8f3df17210d2",
  "sourceToolAssistantUUID": "e7baab7c-501b-4b3b-9b99-41650b52c3ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-13T16:24:00.426Z_



Now I have thoroughly reviewed all three dream tiers (best/median/worst) of the paper, the paper framing, the experiment plan with imagined results, the decisions log, and the project roadmap. Let me compose my detailed review focused on Novelty and Related Work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fe088a8-d34e-445c-bd36-8f3df17210d2",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazsrmdHowLTtaJawZ7Uf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf0f6ed3-9bc4-4773-ad46-6a9382c1ea9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALZMcDVWifoX3G7W9bCbjj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 80544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 680,
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

_source line 49 · 2026-05-13T16:26:17.201Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01RKvvBFcwgUf77hu7hsYvAv`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "tier": "best",
  "dream_id": "dream_20260513T155040",
  "overall_score": "borderline accept",
  "report": "\n# Reviewer 2 (R2) — Novelty and Related Work\n\n**Paper:** ContamCal: Calibrating Benchmark Scores for Training Data Contamination via Contamination-Augmented Item Response Theory\n\n**Venue:** AAAI 2027 (acceptance rate ~17.6%)\n\n---\n\n## A. Novelty Assessment\n\n### A1. Core idea: contamination as covariate rather than removable confound\n\nThis is the paper's strongest conceptual contribution. The shift from \"detect and remove\" to \"detect and adjust\" is genuinely well-motivated, especially given the Emperor's New Clothes result (Dong et al., ICML 2025) showing all 20 mitigation strategies fail. The causal inference analogy (eliminating confounders vs. adjusting for them) is apt and provides solid intellectual grounding.\n\nHowever, I note that this framing is more of a *paradigm restatement* than a *technical invention*. The item compromise IRT literature (Eckerly 2017, Sinharay 2017) already does exactly this in educational testing — the paper's contribution is recognizing that this existing paradigm applies to LLM evaluation. This is valuable cross-disciplinary transfer, but the novelty ceiling is lower than the paper implies. The paper should more explicitly acknowledge that the core modeling idea (exposure covariate in IRT) is borrowed wholesale from educational measurement, and that the contribution lies in the adaptation and validation for the LLM setting.\n\n**Novelty: Moderate.** The insight is important but not technically novel — it is an application of an established idea to a new domain.\n\n### A2. Three structural modifications from educational IRT\n\nThe paper claims three non-trivial adaptations:\n\n**(a) Independent examinees to single model with joint item distributions.** This is the most technically interesting adaptation. In educational testing, each examinee is independent; in LLM evaluation, a single model produces all responses, changing the local independence assumption. However, the paper does not deeply engage with the statistical consequences. Does this violate IRT's local independence assumption? If so, how severe is the violation, and what are the consequences for posterior inference? The paper treats this as a solved problem by simply fitting the standard model, but the theoretical implications deserve more attention. This modification is stated rather than developed.\n\n**(b) Binary leakage to continuous exposure scores.** This is a natural and relatively straightforward generalization. The educational IRT literature already uses graded exposure indicators (e.g., partial item compromise models). The paper's use of continuous RRF scores is a reasonable choice but not a fundamentally new modeling idea.\n\n**(c) Stable ability to regime-conditional ability (SFT vs. RL).** This is primarily an engineering decision about when to use which signals, not a deep structural modification to the IRT model itself. The model does not actually have a regime-conditional ability parameter — rather, it uses different signal subsets depending on the detected training regime. This is signal selection, not a new IRT formulation.\n\n**Novelty: Low-to-Moderate.** Adaptation (a) has theoretical depth that is under-explored; (b) is incremental; (c) is engineering rather than modeling.\n\n### A3. RRF fusion of detection signals\n\nRRF (Cormack et al., 2009) is a well-established information retrieval technique. Applying it to aggregate contamination detection signals is a sensible engineering choice but carries no methodological novelty. The paper's own ablation shows that RRF barely outperforms the best single signal in terms of AUC (0.87 vs 0.88 in the best tier), with its advantage lying in robustness across benchmarks rather than peak performance. The choice of c=60 is the standard default. No novel fusion methodology is proposed.\n\n**Novelty: Low.** Straightforward application of existing technique.\n\n### A4. Regime-conditional modeling / auto-degradation for RL\n\nThis is an engineering decision, not a methodological contribution. The system detects which signals are available and uses them — there is no novel statistical machinery for handling regime shifts. A genuine contribution here would be a formal model that jointly infers the training regime and adjusts accordingly, or a principled Bayesian approach to signal selection. Instead, the paper uses a fixed heuristic (if RL-trained, drop embedding and Min-K++).\n\n**Novelty: Low.** Engineering heuristic rather than methodological contribution.\n\n### A5. Incremental novelty over \"detection + remove-and-rescore\"\n\nThe key advantage of ContamCal over remove-and-rescore is twofold: (1) it uses continuous exposure scores rather than binary flags, preserving contamination degree information; and (2) it produces calibrated scores with credible intervals rather than simple adjusted point estimates. The MAE improvement (1.97pp vs 4.2pp for remove-and-rescore in the best tier) is substantial. The uncertainty quantification via Bayesian posterior is a genuine practical advantage.\n\nHowever, the comparison to linear regression + bootstrap CI (3.5pp MAE) is more informative. The 44% improvement over this baseline comes from the IRT framework's nonlinear item response modeling, not from the contamination covariate per se. This raises the question: how much of the improvement is from 4PL IRT vs. from the contamination-specific augmentation? The ablation (vanilla 4PL at 6.1pp vs. 4PL+gamma at 1.97pp) answers this: the contamination covariate is essential. But the comparison to linear regression suggests that a simpler contamination-aware model (linear exposure adjustment with bootstrap) captures much of the value.\n\n**Novelty: Moderate.** The combination provides clear empirical value, but the individual components are all known.\n\n### A. Overall Novelty Assessment\n\nContamCal is a *synthesis* paper — it combines existing detection signals (known), RRF fusion (known), 4PL IRT (known), contamination covariates in IRT (known from educational measurement), and Bayesian inference via Stan NUTS (known). The novelty lies in the *combination* and the *validation* in the LLM evaluation setting. This is a legitimate form of contribution, but reviewers at AAAI should be aware that no individual technical component is new. The paper's value is primarily empirical and practical rather than methodological.\n\n**Overall Novelty Score: 3/5** — Moderate. Cross-disciplinary synthesis with some novel validation, but no new techniques.\n\n---\n\n## B. Related Work Completeness\n\n### B1. Overall comprehensiveness\n\nThe related work section is **significantly underdeveloped**. With only 10 citations in the best-tier paper, this is far below the standard for a top venue. A typical AAAI paper in this area would cite 30-50 works. The related work section (Section 5 in best-tier) is approximately half a page — inadequate for a paper that spans contamination detection, IRT, Bayesian inference, and evaluation methodology.\n\n### B2. Missing related work areas\n\n**(i) Additional contamination detection methods.** The paper uses 4 signals but the detection literature is much broader:\n- Extraction attacks (Carlini et al., 2021; \"Extracting training data from large language models\")\n- Membership inference attacks (Mattern et al., 2023; Shi et al., 2023 beyond Min-K%)\n- KDS (Knowledge-Data Separation) is mentioned in the paper framing but absent from the paper itself\n- Golchin & Surdeanu (2024) — time travel contamination detection\n- Oren et al. (2024) — \"Proving test set contamination in black-box language models\" (cited but only in context of Emperor's, not as a detection method)\n- The paper should discuss why these 4 signals were chosen over alternatives\n\n**(ii) Other IRT applications in NLP/ML.**\n- HiBayES (Paganini 2024) is mentioned in the framing but absent from the best-tier paper — this is a significant omission as it directly addresses Bayesian uncertainty in LLM evaluation\n- DCR (Yang et al., 2023) — Data Contamination Report, which does perform score adjustment — is mentioned in the framing but absent from the paper. This is a critical missing baseline/comparison\n- PSN-IRT is mentioned in the paper framing but uses a different citation style\n\n**(iii) Post-hoc calibration methods from the broader ML literature.**\n- Platt scaling, temperature scaling, and isotonic regression are standard post-hoc calibration methods. While they address probability calibration rather than score calibration, the conceptual connection should be discussed — and the paper should explain why these are not applicable or relevant\n- Conformal prediction methods for uncertainty quantification — an alternative to Bayesian CIs that the paper should at least acknowledge\n\n**(iv) Score adjustment and fairness calibration.**\n- DIF (Differential Item Functioning) literature in educational testing — directly relevant as it addresses systematic score differences across subgroups, analogous to contaminated vs. clean models\n- Test equating methods in psychometrics\n\n**(v) Benchmark design and dynamic benchmarks.**\n- LiveBench (White et al., 2024) — dynamic benchmarks that avoid contamination by construction\n- SEAL (Scale et al., 2024) — contamination-resistant evaluation\n- The paper should discuss how ContamCal relates to the \"prevention vs. cure\" spectrum — dynamic benchmarks prevent contamination, ContamCal corrects for it post-hoc\n\n**(vi) Data provenance and attribution.**\n- Data attribution methods (Ilyas et al., 2022; Park et al., 2023) that trace model behavior to training data — conceptually related to Stage 1's provenance mapping\n- The connection to influence functions and training data attribution should be discussed\n\n### B3. Connection to educational measurement's item compromise IRT\n\nThe connection to Eckerly (2017) and Sinharay (2017) is stated but not developed. The paper should:\n- Explain the specific models used in these works (what kind of exposure covariate? binary or graded?)\n- Discuss the empirical findings from educational testing — how well does item compromise IRT work in that setting? What are the known limitations?\n- Cite additional work in this tradition (e.g., McLeod et al., 2003; Segall, 2004 on item exposure control; Zhang, 2014 on person-fit with compromised items)\n- The adaptation from human testing (thousands of independent examinees) to LLM evaluation (tens of correlated models) is the paper's key theoretical bridge and deserves deeper treatment\n\n### B4. Concurrent/recent works (2025-2026)\n\nGiven the rapid pace of the field, several recent works are likely relevant:\n- The paper cites Dong et al. (ICML 2025) but should check for responses/follow-ups to this work\n- Any 2025-2026 work on contamination-aware evaluation or contamination quantification\n- Recent IRT-based LLM evaluation work beyond the three cited (TinyBenchmarks, Growing Pains, ATLAS)\n- The growing literature on evaluation methodology for LLMs (e.g., Liang et al., HELM; Biderman et al., lessons from evaluation)\n\n**Related Work Assessment: Major weakness.** The section needs substantial expansion — at minimum doubling the citation count and adding discussion of the areas identified above.\n\n---\n\n## C. Positioning and Framing\n\n### C1. \"Statistical safety net\" framing\n\nThe framing is effective and well-motivated. The progression from \"mitigation doesn't work\" (Emperor's New Clothes) to \"calibration as the alternative\" is logical and compelling. The causal inference analogy is well-chosen. However, the \"safety net\" metaphor slightly oversells — a safety net implies catching you reliably, but the RL case study shows the method's limitations are significant for the models practitioners most care about.\n\n### C2. Distinction from prior work\n\nThe paper distinguishes itself well from detection methods (which don't calibrate) and IRT methods (which don't model contamination). The distinction from remove-and-rescore is clear and empirically supported. However, the distinction from DCR (Data Contamination Report) is absent — this is the most directly comparable prior work and must be discussed.\n\n### C3. Scope of claims\n\nThe claims in the best-tier paper are ambitious but supported within the controlled SFT setting. The headline \"1.97pp MAE with 93% CI coverage\" is compelling. However, I have concerns:\n- The 44% improvement over \"best baseline\" is measured against linear regression, not against a method that was specifically designed for this task. The baselines are somewhat strawman-ish — four of five are simple ablations or known-ineffective methods (Emperor's mitigations).\n- The \"best\" tier imagined results are extremely optimistic. The median tier (4.2pp MAE, 89% coverage) and worst tier (7.8pp MAE, 78% coverage) paint a more realistic picture. The gap between best and worst is enormous — 4x in MAE.\n- The gap between best-tier dream (signal AUC 0.88 for embedding retrieval) and worst-tier dream (AUC 0.72) suggests that everything hinges on detection signal quality. If the signals work well, the method works; if they don't, it doesn't. This makes ContamCal's contribution somewhat parasitic on the quality of upstream detection.\n\n---\n\n## D. Significance and Impact\n\n### D1. Impact for AAAI\n\nThe paper addresses a timely and important problem. AAAI reviewers in the AI evaluation track would find this relevant. The Bayesian methodology is well-suited to AAAI's strengths. The paper would benefit from:\n- Framing as evaluation methodology (AAAI strength) rather than NLP-specific\n- Emphasizing the decision-theoretic contribution (expected regret analysis) which aligns with AAAI's decision-making tradition\n- The identifiability analysis (better developed in the median/worst tiers) is actually a strong methodological contribution that the best tier underplays\n\n### D2. Problem importance\n\nContamination is a genuine and growing concern, but reasonable people disagree about its severity relative to other evaluation problems (benchmark saturation, evaluation gaming, construct validity). The paper's opening claim that contamination inflates scores by \"8-15pp\" is from specific studies and may not generalize. The paper should acknowledge that for many practical use cases (e.g., choosing between GPT-4o and Claude Opus), contamination may not be the dominant source of evaluation error.\n\n### D3. Practical adoption barriers\n\nSeveral barriers would limit adoption:\n1. **Computational cost:** Stan NUTS with 4 chains x 4000 iterations per benchmark is non-trivial. The paper does not report wall-clock time.\n2. **Signal computation:** Computing 4 detection signals per (model, item) pair requires model weights (for 2 of 4 signals), training data access (for embedding retrieval), and paraphrase generation (for ConStat). This is a substantial infrastructure requirement.\n3. **Model pool requirement:** The N>=50 models requirement means this is only applicable to large-scale evaluation efforts (e.g., leaderboards), not individual model evaluations.\n4. **RL limitation:** The method's limited effectiveness for RL-trained models is a serious practical barrier, as most production models use RL post-training.\n\n---\n\n## E. Weaknesses and Questions for Authors\n\n### Major Weaknesses\n\n**W1. Novelty is primarily synthesis, not innovation.** Every component (RRF, 4PL IRT, contamination covariates, Bayesian MCMC) is borrowed from existing work. The cross-disciplinary transfer from educational measurement is valuable but the paper does not adequately develop the theoretical implications of the adaptations.\n\n**W2. Related work is critically insufficient.** 10 citations is unacceptable for a top venue paper spanning this many subfields. Missing comparisons to DCR, HiBayES, DIF, conformal prediction, dynamic benchmarks, and the broader contamination detection literature significantly weaken the paper's positioning.\n\n**W3. The \"best tier\" results may be unrealistically optimistic.** Comparing across dream tiers: 1.97pp MAE (best) vs 4.2pp (median) vs 7.8pp (worst) — a 4x range. The key driver is detection signal quality, which is assumed rather than established. If real detection signals perform closer to the worst tier (which the project's own simulation study suggests at N_items=300), the practical value diminishes substantially.\n\n**W4. Controlled SFT injection may not generalize to real-world contamination.** SFT injection via paraphrasing is one contamination mechanism, but real-world contamination includes: verbatim memorization during pretraining, indirect contamination via instruction tuning on benchmark-derived data, contamination via synthetic data that was itself generated using benchmark items. The paper validates on one mechanism and claims generality.\n\n**W5. The RL regime limitation is understated.** Most models that practitioners actually want to evaluate (instruction-tuned, RLHF-trained) fall in the RL regime where the method's detection signals degrade. The best tier claims Self-Critique AUC of 0.72 under RL, but the worst tier shows 0.57. If the true AUC is closer to 0.57, the method provides essentially no useful calibration for the models that matter most.\n\n### Minor Weaknesses\n\n**W6.** The choice of c=60 in RRF is the standard default but is not justified for this specific application. A sensitivity analysis on c would strengthen the paper.\n\n**W7.** The paper uses a global gamma parameter for contamination effect. This assumes homogeneous contamination effects across items within a benchmark, which is unrealistic — some items may be more memorizable than others. An item-specific or at least item-category-specific gamma would be more realistic.\n\n**W8.** The 72B observational analysis lacks ground truth and provides only weak evidence. The gamma=0.18 on MMLU \"suggesting detectable contamination\" is not validated — it could also reflect model specification error.\n\n**W9.** Local independence assumption. The paper does not discuss whether the standard IRT local independence assumption holds when all responses come from the same model (or a family of closely related models). This is a fundamental modeling concern.\n\n### Questions for Authors\n\n**Q1.** How does ContamCal compare to DCR (Yang et al., 2023), which also provides contamination-adjusted scores? Why is DCR not included as a baseline?\n\n**Q2.** What is the wall-clock computational cost of the full pipeline (4 signals + IRT fitting) for a single benchmark?\n\n**Q3.** Can you provide evidence that the local independence assumption is approximately satisfied in your setting? What is the residual correlation structure after conditioning on theta and gamma?\n\n**Q4.** The paper assumes a single global gamma. Have you considered item-level or item-cluster-level contamination effects? What happens if contamination is heterogeneous across items?\n\n**Q5.** How sensitive are results to the choice of RRF constant c=60?\n\n---\n\n## F. Overall Assessment\n\n### Scores (AAAI 1-10 scale)\n\n- **Overall: 5/10** — Borderline. The problem is important and the approach is sensible, but novelty is limited to cross-disciplinary synthesis, and the related work section is critically underdeveloped. The best-tier results are compelling but may be optimistic relative to achievable signal quality.\n\n- **Soundness: 3/5** — The Bayesian IRT framework is technically sound. The controlled SFT injection provides valid internal evaluation. However, the local independence assumption is unexamined, the generalizability beyond SFT contamination is uncertain, and the gap between best/median/worst tier projections raises questions about robustness.\n\n- **Significance: 3/5** — The problem is timely and the \"calibration not elimination\" paradigm shift is valuable. However, practical adoption barriers (signal infrastructure, model pool requirements, RL limitations) limit near-term impact. The expected regret analysis for decision-making is a nice contribution.\n\n- **Novelty: 2/5** — The individual components are all borrowed from existing work. The contribution is synthesis and domain adaptation, not new methodology. The three claimed structural adaptations from educational IRT are either under-developed (local independence), incremental (continuous exposure), or engineering (regime selection).\n\n- **Clarity: 4/5** — The best-tier paper is well-written with clear problem formulation, clean notation, and good experimental structure. Tables are informative. The \"wide CIs as the correct answer\" framing for the RL case is effective communication.\n\n- **Confidence: 4/5** — I am familiar with IRT, contamination detection, and Bayesian inference. I have moderate familiarity with the specific educational measurement item compromise literature.\n\n### Summary Recommendation\n\nThe paper presents a well-engineered synthesis that addresses an important problem. The core insight — calibrate rather than eliminate — is sound and well-motivated. However, the novelty bar for AAAI 2027 requires more than combining known components, and the critically thin related work section would be a red flag for any reviewer. The authors should: (1) substantially expand related work to 30+ citations, (2) more honestly position the novelty as cross-disciplinary transfer rather than implying new methodology, (3) better develop the theoretical implications of adapting educational IRT to the single-model setting, and (4) include DCR and HiBayES as baselines/comparisons. If these issues are addressed and the experimental results hold closer to the median tier (4.2pp MAE, 89% coverage) than the best tier, this could be a solid contribution. In its current form, I lean borderline accept/weak reject at AAAI.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf0f6ed3-9bc4-4773-ad46-6a9382c1ea9b",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011CazsrmdHowLTtaJawZ7Uf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a788212-d7b5-4cf1-8b1b-16c3778cf78f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALZMcDVWifoX3G7W9bCbjj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 680,
      "cache_read_input_tokens": 80544,
      "output_tokens": 5281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 680
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5281,
          "cache_read_input_tokens": 80544,
          "cache_creation_input_tokens": 680,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 680,
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

_source line 50 · 2026-05-13T16:26:21.306Z_

<details><summary>↩ Tool result · `toolu_01RKvvBFcwgUf77hu7hsYvAv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/best/review_report.md\", \"dream_id\": \"dream_20260513T155040\", \"tier\": \"best\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a788212-d7b5-4cf1-8b1b-16c3778cf78f",
  "isSidechain": true,
  "promptId": "ed9194d4-d34f-4eb4-bb34-8669aebcc4b6",
  "agentId": "a5ac0a7826a71f52a",
  "type": "user",
  "uuid": "96c3f98b-2dcf-482d-b5ea-e4b4be035256",
  "sourceToolAssistantUUID": "9a788212-d7b5-4cf1-8b1b-16c3778cf78f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-13T16:26:38.547Z_

Review submitted. Here is a summary of the key findings:

**Overall: 5/10 (Borderline Accept)** for the best-tier paper at AAAI 2027.

**Key Findings by Section:**

**Novelty (2/5):** ContamCal is fundamentally a synthesis paper. Every component (RRF fusion, 4PL IRT, contamination covariates, Bayesian MCMC via Stan) is borrowed from existing work. The core idea of treating contamination as a covariate in IRT comes directly from the educational measurement item compromise tradition (Eckerly 2017, Sinharay 2017). The three claimed "non-trivial structural adaptations" range from under-explored (local independence violation), to incremental (continuous exposure), to pure engineering (regime-conditional signal selection). No new technique is introduced.

**Related Work (Major Weakness):** Only 10 citations is critically insufficient for a paper spanning contamination detection, IRT, Bayesian inference, and evaluation methodology. Key missing areas include: DCR (the most directly comparable prior work, absent as both citation and baseline), HiBayES, DIF literature, conformal prediction alternatives, dynamic benchmarks (LiveBench), data attribution methods, and the broader contamination detection literature beyond the 4 signals used.

**Soundness (3/5):** The Bayesian framework is technically sound, but the local independence assumption is unexamined despite being fundamentally altered in the single-model-as-examinee setting. The 4x gap between best-tier (1.97pp MAE) and worst-tier (7.8pp MAE) projections reveals extreme sensitivity to detection signal quality.

**Practical Concerns:** The RL regime limitation is the most serious barrier — most production models use RL post-training, where detection signals degrade severely (worst-tier AUC ~0.57 for Self-Critique). The N>=50 model requirement and 4-signal infrastructure cost further limit adoption.

**Actionable Recommendations:** (1) Expand related work to 30+ citations; (2) Include DCR and HiBayES as baselines; (3) Develop the theoretical treatment of local independence violation; (4) Honestly position novelty as cross-disciplinary transfer; (5) Consider item-level rather than global gamma; (6) Add computational cost reporting.

The review was saved to `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/best/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96c3f98b-2dcf-482d-b5ea-e4b4be035256",
  "isSidechain": true,
  "agentId": "a5ac0a7826a71f52a",
  "requestId": "req_011Cazt3XrrvXbBSJ8BMiGAe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07fba927-5914-457e-99d9-74001b873da7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "12c88d9d-1477-4077-a4d3-f782256d68e2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EUfR65z2fmbzRfvgoAFM9m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5414,
      "cache_read_input_tokens": 81224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5414,
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
