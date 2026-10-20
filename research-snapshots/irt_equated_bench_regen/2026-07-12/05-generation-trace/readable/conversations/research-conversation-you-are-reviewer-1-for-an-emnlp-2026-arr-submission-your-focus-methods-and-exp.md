# Research conversation: You are Reviewer 1 for an EMNLP 2026 ARR submission. Your focus: **Methods and Experiments**. Evaluate soundness, reprod

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 74
- **Recorded user turns:** 1
- **Tool calls:** 32
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a92367696a2c7802f.jsonl`
- **Structured JSON:** [`d078ed1ab68fea1db28e.json`](../../sessions/d0/d078ed1ab68fea1db28e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

74 recorded events

### User

_source line 1 · 2026-05-21T11:55:02.211Z_

You are Reviewer 1 for an EMNLP 2026 ARR submission. Your focus: **Methods and Experiments**. Evaluate soundness, reproducibility, statistical rigor, and experimental completeness.

## Venue calibration (EMNLP 2026 via ARR)
- 5 = Award (top 2.5%), 4 = Conference accept, 3 = Findings, 2 = Major revision, 1 = Do not resubmit
- Acceptance rate ~21%. Be calibrated: a score of 4 means top ~20%.
- Dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5)

## Paper summary

**Title**: "Psychometric DIF Analysis Reveals Systematic Temporal Instability in LLM Benchmark Items at Scale"

**Core claim**: Applying Mantel-Haenszel DIF analysis to METABENCH response matrix (5,219 models × 12,508 MMLU items), 30.8% of MMLU items show large temporal DIF (ETS Category C) between pre-2024 and 2024 model cohorts. This generalizes across 6 benchmarks (C% range 17.5–30.8%), is confirmed by permutation testing (z=189.7, p<0.001), and is not driven by capability improvement (≤2.4 pp) or architecture heterogeneity (99.9% decoder-only, Jaccard=1.0).

**Four contributions**:
1. Temporal instability at scale (30.8% MMLU DIF-C items, 6 benchmarks)
2. Ground truth meta-critique (web-overlap ≠ differential contamination, enrichment≈1.0)
3. Semi-synthetic validation framework (ΔTPR methodology, cross-subject matching ΔFPR=0.000)
4. DIF as diagnostic lens (instability ≠ invalidity, audit protocol recommendation)

**Method (Section 3)**:
- MH-DIF on binary response matrix, models partitioned into pre-2024 (ref, N=1080) and 2024 (focal, N=807)
- ETS classification: A (|Δ_MH|<1.0), B (1.0≤|Δ_MH|<1.5), C (|Δ_MH|≥1.5 and significant at p<0.05)
- Semi-synthetic framework: inject known contamination by flipping incorrect→correct responses for focal group at probability p∈[0,1]; key metric ΔTPR = TPR(p) − TPR(p=0)
- Cross-subject matching: use total score on *other* subjects as MH conditioning variable to eliminate matching variable contamination (ΔFPR=0.000)

**Key experimental results**:
- Table 1: MMLU temporal C%=30.8, ability C%=2.7, random sanity=0.21%, Jaccard(temporal∩ability)=0.016
- Table 2: Within-family DIF: Llama-2→3 C%=58.7, Mistral→Mixtral C%=36.2
- Table 3: Domain specificity ρ=0.29, p=0.028
- Table 4: Permutation null — null mean=0.45%, SD=0.16%, z=189.7, p<0.001
- Tables 5-6: Architecture — 99.9% decoder-only, Jaccard=1.0, IRT fit poor (CFI=0.68)
- Table 7: 6-benchmark DIF — range 17.5–30.8%, all enrichment ≥45×, CV=0.22
- Table 8: Benchmark characteristics vs C% (descriptive moderator)
- Table 9: GSM8K C%=18.3, external temporal C%=45.8, Spearman=0.92
- Table 10: GSM1K correlation r=−0.46, p=0.007, N=33 (exploratory)
- Table 11: Semi-synthetic ΔTPR at p=0.5 is 0.43, ΔFPR=0.000 at all p
- Table 12: Cross-subject vs within-subject FPR — 0.000 vs 0.310
- Tables 13-14: Simpson's paradox — OR flip from 1.48 to 0.76, χ²=634
- Table 15: IFT vs MH — ρ=0.78, Jaccard=0.71, breakpoint 2023-Q4 to 2024-Q1
- Table 16: Graceful degradation — ρ=0.9941 at 31% removal, SHR=0.9862
- Tables 17-18: ConStat (19% non-RL, 7% RL), DVD (0.17 correlation with DIF)
- Table 19: Ensemble fusion +0.03 AUROC over DIF alone, weight CV ±28%
- Table 20: RL robustness — alignment-RL C%=29.4 Jaccard=0.83, reasoning-RL N=13
- Table 21: Per-detector AUROC — DIF 0.71 [0.67,0.78], ConStat 0.68 [0.42,0.73] for non-RL; reasoning-RL DIF=0.59, ConStat=0.53
- Table 22: Bifactor IRT — 5-factor CFI=0.73, TLI=0.70, pipeline killed
- Table 23: Item generation — difficulty ρ=0.41, expert pass rate 58%, calibration insufficient
- Table 24: Cumulative Bayesian power 0.39→0.73 over 4 administrations

**Limitations acknowledged**:
- Temporal coarseness (binary split), IFT partially addresses
- IRT misfit (98% |Lz|>2, CFI=0.68), MH is nonparametric but conditioning variable validity weakened
- Reasoning-RL underpowered (N=13)

## Experiment design reference (what was planned but may not be fully covered)
The full experiment plan includes: real_data_dif_mmlu, rl_robustness_validation, constat_perturbation_eval, dvd_generation_variance_eval, ensemble_fusion, cross_benchmark_gsm8k, bifactor_irt_equating_pilot, item_generation_calibration, cumulative_bayesian_dif, graceful_degradation_analysis, item_focused_trees, architecture_stratified_dif, semi_synthetic_contamination_validation, multi_benchmark_temporal_dif, permutation_null_c_rate, odds_ratio_regression_transparency.

All 16 planned experiments appear to be covered in the paper (Sections 4.1–4.15 plus the Simpson's paradox in 4.7).

## Your review task

Write a detailed review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (bulleted, specific)
3. **Weaknesses** (bulleted, specific, with severity: major/minor)
4. **Questions for authors**
5. **Soundness score** (1-5 with justification)
6. **Excitement score** (1-5 with justification)
7. **Reproducibility score** (1-5 with justification)
8. **Overall Assessment** (using the ARR 1-5 half-point scale)
9. **Confidence** (1-5)

Be rigorous but fair. Focus on methodological soundness, statistical validity, experimental design quality, and whether claims are supported by evidence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "5319f538-31a0-446e-a60d-cbaf0034feca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T11:55:02.217Z_

```json
{
  "parentUuid": "5319f538-31a0-446e-a60d-cbaf0034feca",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
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
  "uuid": "22a7a870-93f5-47bb-8f44-e18c845b4b2e",
  "timestamp": "2026-05-21T11:55:02.217Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-21T11:55:04.993Z_



I'll conduct a thorough review by reading the paper and supporting materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22a7a870-93f5-47bb-8f44-e18c845b4b2e",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfprb3D3iX4tqwJmzJN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d56e557-0058-4369-8901-fba47001e0f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zzfiN1EMAW4uHwk6goUgu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16954,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16954,
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

_source line 4 · 2026-05-21T11:55:05.102Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Fi33GfxPB5qsjVScxjrjff`</summary>

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
  "parentUuid": "4d56e557-0058-4369-8901-fba47001e0f8",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfprb3D3iX4tqwJmzJN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "929be7f5-875b-4282-803b-be76086d92dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zzfiN1EMAW4uHwk6goUgu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16954,
      "cache_read_input_tokens": 0,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16954
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 104,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16954,
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

_source line 5 · 2026-05-21T11:55:05.109Z_

<details><summary>↩ Tool result · `toolu_01Fi33GfxPB5qsjVScxjrjff`</summary>

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
  "parentUuid": "929be7f5-875b-4282-803b-be76086d92dd",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "37e2a102-6ace-41de-92e9-6709e57f77b9",
  "sourceToolAssistantUUID": "929be7f5-875b-4282-803b-be76086d92dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T11:55:09.920Z_



Let me read the paper and key supporting materials systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37e2a102-6ace-41de-92e9-6709e57f77b9",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfq5Ab1w1psBNzyPEYq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7800e564-1712-4b97-9437-0f315dd61329",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBz5UTUmiAcFD3ckVj7bkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1287,
      "cache_read_input_tokens": 16954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1287,
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

_source line 7 · 2026-05-21T11:55:12.036Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019fBJxWAsdEtC1A3ohswXbM`</summary>

```json
{
  "pattern": "paper/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7800e564-1712-4b97-9437-0f315dd61329",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfq5Ab1w1psBNzyPEYq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5dc5b4de-2295-42f3-bb87-231671f70e0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBz5UTUmiAcFD3ckVj7bkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1287,
      "cache_read_input_tokens": 16954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1287,
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

_source line 8 · 2026-05-21T11:55:12.058Z_

<details><summary>↩ Tool result · `toolu_019fBJxWAsdEtC1A3ohswXbM`</summary>

```text
paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5dc5b4de-2295-42f3-bb87-231671f70e0c",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "6a374e00-c142-4465-89cd-c7091ac35eaa",
  "sourceToolAssistantUUID": "5dc5b4de-2295-42f3-bb87-231671f70e0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T11:55:13.327Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QEcdpcA5qYgtT4fFAxuiUU`</summary>

```json
{
  "pattern": "paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a374e00-c142-4465-89cd-c7091ac35eaa",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfq5Ab1w1psBNzyPEYq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e385e3e-c45b-4e5c-9112-16252d965a23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBz5UTUmiAcFD3ckVj7bkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1287,
      "cache_read_input_tokens": 16954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1287,
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

_source line 10 · 2026-05-21T11:55:13.340Z_

<details><summary>↩ Tool result · `toolu_01QEcdpcA5qYgtT4fFAxuiUU`</summary>

```text
paper/math_commands.tex
paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e385e3e-c45b-4e5c-9112-16252d965a23",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "4feb99b2-fe18-441e-8e2a-adee0089c0bc",
  "sourceToolAssistantUUID": "8e385e3e-c45b-4e5c-9112-16252d965a23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T11:55:14.313Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01H4c5F2ryY5zg5LzH9629kE`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "experiment_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4feb99b2-fe18-441e-8e2a-adee0089c0bc",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfq5Ab1w1psBNzyPEYq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a17ad51-08bf-4cc9-b60c-613150575097",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBz5UTUmiAcFD3ckVj7bkV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1287,
      "cache_read_input_tokens": 16954,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1287,
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

_source line 12 · 2026-05-21T11:55:14.327Z_

<details><summary>↩ Tool result · `toolu_01H4c5F2ryY5zg5LzH9629kE`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a17ad51-08bf-4cc9-b60c-613150575097",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "5582817f-05e6-45fa-94ef-a47467c938c4",
  "sourceToolAssistantUUID": "7a17ad51-08bf-4cc9-b60c-613150575097",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T11:55:17.524Z_

<details open><summary>🔧 Tool call — Read · `toolu_019P68Mm3q92XrVZPvKNt6ip`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5582817f-05e6-45fa-94ef-a47467c938c4",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfqmkMyccCMqgz7wrpL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6a9a120-048d-42a7-bc6e-7884b08a8217",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dXai3vzUMdjcxgvrJwXTV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 572,
      "cache_read_input_tokens": 18241,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 572
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 18241,
          "cache_creation_input_tokens": 572,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 572,
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

_source line 14 · 2026-05-21T11:55:17.530Z_

<details><summary>↩ Tool result · `toolu_019P68Mm3q92XrVZPvKNt6ip`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Psychometric Instability of LLM Benchmarks:\\Differential Item Functioning Reveals 31\% of MMLU Items\\Behave Differently Across Model Generations}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6a9a120-048d-42a7-bc6e-7884b08a8217",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "85784fc2-7685-4f1e-96d9-b77d9ace476b",
  "sourceToolAssistantUUID": "b6a9a120-048d-42a7-bc6e-7884b08a8217",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T11:55:20.313Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DAWeQGydkaPGozbHRB9vAC`</summary>

```json
{
  "pattern": "paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85784fc2-7685-4f1e-96d9-b77d9ace476b",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfqz7FqTEi2QjPNrn4Z",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "add7f92a-b2ec-40c3-8005-57fc15bcea7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YP832Zjv1fCgSYJwq617iS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 515,
      "cache_read_input_tokens": 18813,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 515
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 18813,
          "cache_creation_input_tokens": 515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 515,
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

_source line 16 · 2026-05-21T11:55:20.334Z_

<details><summary>↩ Tool result · `toolu_01DAWeQGydkaPGozbHRB9vAC`</summary>

```text
paper/sections/method.tex
paper/sections/related_work.tex
paper/sections/experiments.tex
paper/sections/appendix.tex
paper/sections/introduction.tex
paper/sections/limitations.tex
paper/sections/discussion.tex
paper/sections/conclusion.tex
paper/sections/abstract.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "add7f92a-b2ec-40c3-8005-57fc15bcea7a",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "63635fec-e2ef-430d-abde-e9d73d335249",
  "sourceToolAssistantUUID": "add7f92a-b2ec-40c3-8005-57fc15bcea7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T11:55:23.404Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DHy96dkA7d8JhAT1La27zS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63635fec-e2ef-430d-abde-e9d73d335249",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfrCHV8t1tmmceFRff2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd6928c4-6ca4-4ea9-8bcd-5bd9296b345d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XzZVASBoLuBdKMC5tMjmw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 19328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 190,
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

_source line 18 · 2026-05-21T11:55:23.423Z_

<details><summary>↩ Tool result · `toolu_01DHy96dkA7d8JhAT1La27zS`</summary>

```text
1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet the assumption that individual items measure the same construct over time is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (DIF) analysis with ETS severity classification to six METABENCH benchmarks (5,227 models, 27,125 total items), and find that 17.9--31.3\% of items exhibit large DIF (ETS Category~C) between 2023 and 2024 model cohorts---knowledge/reasoning benchmarks show higher instability (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$), each 45--174$\times$ above random baselines. This does not threaten benchmark validity ($\rho \approx 0.997$ between full and stable-item rankings) but reveals which capability dimensions shift across generations. Item-level decomposition shows 92.4\% of instability is item-specific; a Simpson's paradox in odds ratio regression confirms item properties, not accuracy gains, drive DIF. We expose a validation methodology gap: web-overlap labels measure global exposure, not differential functioning (enrichment $\approx 0.96$). A semi-synthetic injection framework with cross-subject matching preserves detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$) with zero false positive inflation. DIF-flagged items concentrate cross-generational discriminative information ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal), and a difficulty--direction interaction ($\rho = -0.597$) reveals that capability gains concentrate on hard items while easy items erode, suggesting DIF captures genuine capability change rather than noise. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd6928c4-6ca4-4ea9-8bcd-5bd9296b345d",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "a6e67ba8-364b-4f2a-b22c-15210993ce18",
  "sourceToolAssistantUUID": "fd6928c4-6ca4-4ea9-8bcd-5bd9296b345d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T11:55:23.867Z_

<details open><summary>🔧 Tool call — Read · `toolu_019iHZWtPrTLaKUXcKW2JLCj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6e67ba8-364b-4f2a-b22c-15210993ce18",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfrCHV8t1tmmceFRff2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c45cbc5-f1ad-43bc-a171-aa9aaa2afdf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XzZVASBoLuBdKMC5tMjmw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 19328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 190,
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

_source line 20 · 2026-05-21T11:55:23.872Z_

<details><summary>↩ Tool result · `toolu_019iHZWtPrTLaKUXcKW2JLCj`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench}, and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. The instability persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of this instability is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\%~\citep{shi2024mink} to performance-based detectors such as ConStat~\citep{dekoninck2024constat}, DVD~\citep{liang2026dvd}, and Self-Critique~\citep{tao2026selfcritique}. These methods validate detection accuracy primarily against web-overlap labels such as those of \citet{li2024contamination}, which classify benchmark items as contaminated based on verbatim or near-verbatim matches in publicly accessible training corpora. Such labels measure \emph{global exposure}: whether an item exists in the data ecosystem that all training pipelines can access. They do not measure \emph{differential item functioning}: whether an item behaves differently across model cohorts that may have had varying degrees of exposure or different training methodologies. \Cref{fig:global_vs_differential} illustrates the distinction. Most MMLU items are globally contaminated in the sense that they exist in web-accessible text, so all model cohorts encounter them and no differential signal arises. The items that function differentially are those where exposure or training methodology changed asymmetrically across cohorts. Validating differential detectors against global-exposure labels therefore conflates two phenomena. Direct comparison confirms near-independence between the two flag sets (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$), consistent across contamination subtypes.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{fig_1_global_vs_differential.pdf}
11	\caption{Global vs.\ differential contamination, illustrated via Item Characteristic Curves (ICCs). \textbf{Left}: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. \textbf{Right}: differential contamination produces DIF; the focal cohort's ICC shifts because only that cohort was disproportionately exposed during training. The enrichment ratio of $\approx 1.0$ between DIF flags and web-overlap labels is expected because most MMLU items fall into the left category.}
12	\label{fig:global_vs_differential}
13	\end{figure}
14	
15	We apply classical MH-DIF with ETS classification to the full METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), to our knowledge, the largest-scale DIF analysis on LLM benchmarks. This psychometric approach complements concurrent work on anchor-item calibration for score comparability~\citep{habba2026growingpains} and addresses the fragility of existing contamination detectors under post-training perturbation~\citep{wang2026fragility}. Semi-synthetic injection experiments confirm that DIF detects differential contamination when present ($\Delta\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$), and our cross-subject matching protocol eliminates false positive inflation ($\Delta\mathrm{FPR} = 0.000$). Three structural controls (matched-ability quintile analysis, IRT $\theta$-conditioning, and within-subject pre-checks) confirm that the 31\% temporal instability cannot be attributed to methodological artifacts, establishing it as a robust empirical finding about LLM benchmark measurement properties, replicated across all six METABENCH benchmarks (\Cref{sec:gsm8k}).
16	
17	MMLU's 12,508 items provide sufficient measurement redundancy that removing nearly a third does not alter rank order ($\rho \approx 0.997$). DIF should therefore be understood as a diagnostic lens rather than a quality filter. DIF-flagged items concentrate discriminative signal: removing them degrades ranking discriminability more than random removal ($z = -8\sigma$ to $-49\sigma$ across 21 conditions). Model families show distinctive DIF profiles: Llama-3 derivatives gain a median of ${+}53$ rank positions under stable-item evaluation, while Mistral-based models lose a median of $35$; 25\% of models shift by $|\Delta\mathrm{Rank}| \geq 100$.
18	
19	The MH-DIF procedure is well-established in psychometrics~\citep{holland1988mh,clauser1998dif}; the cross-subject matching strategy has psychometric precedent~\citep{nandakumar1993dif}. Our contributions are therefore empirical and methodological, not algorithmic: (a)~the first large-scale DIF characterization across six LLM benchmarks (27,125 items, 5,227 models), finding 17.9--31.3\% temporal instability robust across thresholds and unrelated to accuracy gains (confirmed by Simpson's paradox in odds ratio regression); (b)~a ground truth meta-critique exposing that web-overlap labels are poorly suited to evaluate item-level differential detectors; (c)~a reusable semi-synthetic validation framework with cross-subject matching that addresses LLM-specific challenges (multi-domain local dependence handling and simultaneous contamination control, $\Delta\mathrm{FPR} = 0.000$), confirmed on GSM8K; and (d)~a concrete DIF audit protocol for benchmark maintenance (\Cref{sec:disc_protocol}). We make the following contributions:
20	
21	\begin{enumerate}
22	\item \textbf{Benchmark temporal comparability} (Claim 1): 31\% of MMLU items are functionally unstable across model generations under ETS~C classification; replication across all six METABENCH benchmarks yields C\% $= 17.9$--$31.3\%$ (45--174$\times$ above random baselines), with knowledge/reasoning benchmarks showing higher instability than procedural ones (\Cref{sec:temporal,sec:gsm8k}).
23	
24	\item \textbf{Ground truth meta-critique} (Claim 2): Web-overlap contamination labels~\citep{li2024contamination} do not provide appropriate ground truth for item-level differential detectors. Direct empirical comparison on 9,229 items shows near-independence (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$), exposing a validation methodology gap in the contamination detection literature (\Cref{sec:groundtruth}).
25	
26	\item \textbf{Semi-synthetic validation framework} (Claim 3): Controlled injection with cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$); cross-benchmark replication on GSM8K confirms generality (\Cref{sec:semisynthetic,sec:gsm8k}).
27	
28	\item \textbf{DIF as diagnostic lens} (Claim 4): DIF-flagged items concentrate discriminative information ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal, Jaccard overlap with high-discrimination items $= 0.12$) and exhibit a structured difficulty--direction interaction ($\rho = -0.597$): capability gains concentrate on hard items while easy items erode (\Cref{sec:downstream}).
29	\end{enumerate}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c45cbc5-f1ad-43bc-a171-aa9aaa2afdf0",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "bdfcaefa-7d3e-42ce-ac1d-25e06a24b278",
  "sourceToolAssistantUUID": "7c45cbc5-f1ad-43bc-a171-aa9aaa2afdf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T11:55:24.338Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EcK7uMBnSdxSuqG5vSocqa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdfcaefa-7d3e-42ce-ac1d-25e06a24b278",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfrCHV8t1tmmceFRff2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "047b824f-c7dd-46c9-a66b-d30a8e0ea9e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XzZVASBoLuBdKMC5tMjmw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 19328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 190,
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

_source line 22 · 2026-05-21T11:55:24.343Z_

<details><summary>↩ Tool result · `toolu_01EcK7uMBnSdxSuqG5vSocqa`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees into $K$ score bins based on total score (a proxy for $\theta$) and computing a common odds ratio across strata. We use $K = 5$ equiprobable strata (quintile-based binning) following ETS recommended practice for large-scale assessments~\citep{donoghue1993mh,clauser1998dif}. Within each stratum $k$, the responses of the reference group and the focal group form a $2 \times 2$ contingency table:
17	
18	\begin{equation}
19	\label{eq:mh}
20	\alpha_{\mathrm{MH}} = \frac{\displaystyle\sum_{k=1}^{K} A_k D_k \,/\, T_k}{\displaystyle\sum_{k=1}^{K} B_k C_k \,/\, T_k}\,,
21	\end{equation}
22	
23	\noindent where $A_k$ and $B_k$ are the number of correct and incorrect responses in the reference group for stratum $k$, $C_k$ and $D_k$ are the corresponding counts for the focal group, and $T_k$ is the total number of examinees in stratum $k$. Under the null hypothesis of no DIF, $\alpha_{\mathrm{MH}} = 1$. The log odds ratio is converted to the ETS delta scale:
24	
25	\begin{equation}
26	\label{eq:delta}
27	\Delta_{\mathrm{MH}} = -2.35 \ln(\alpha_{\mathrm{MH}})\,.
28	\end{equation}
29	
30	The Educational Testing Service (ETS) classifies DIF severity into three categories based on $|\Delta_{\mathrm{MH}}|$. Category~A (negligible) requires $|\Delta_{\mathrm{MH}}| < 1.0$. Category~C (large) requires both $|\Delta_{\mathrm{MH}}| \geq 1.5$ and statistical significance at $p < 0.05$ from the MH chi-squared test. Category~B (moderate) includes all remaining items: those with $1.0 \leq |\Delta_{\mathrm{MH}}| < 1.5$, or $|\Delta_{\mathrm{MH}}| \geq 1.5$ without statistical significance. The dual threshold in ETS~C (effect size \emph{and} significance) guards against flagging items that show large but unreliable effect sizes. Throughout this paper, we report the percentage of items classified as ETS~C, denoted C\%.
31	
32	The choice of matching variable (the total score used for stratification) affects both validity and interpretation. We distinguish three matching strategies: (1)~\emph{standard matching} uses the within-benchmark total score on all items of the same benchmark; (2)~\emph{cross-subject matching} uses the total score on all subjects \emph{other than} the one containing the item under test, preventing the matching variable from absorbing injected contamination signals (\Cref{sec:injection}); and (3)~\emph{external matching} uses the total score on a different benchmark entirely (e.g., MMLU total score as the matching variable when testing DIF on GSM8K items), providing an independent ability proxy uncontaminated by the target benchmark. Cross-subject and external matching both address matching variable contamination but at different granularities: cross-subject operates within a multi-domain benchmark, while external operates across benchmarks.
33	
34	\subsection{Cohort Designs}
35	\label{sec:cohorts}
36	
37	We construct five cohort comparisons: (1)~\emph{Temporal}: 2023 ($N = 1{,}080$) vs.\ 2024 ($N = 807$) models, the primary comparison; (2)~\emph{Ability-quintile}: Q1--Q2 vs.\ Q4--Q5 within the same temporal window, testing whether ability differences alone produce DIF; (3)~\emph{Within-family}: Llama-2 ($N = 161$) vs.\ Llama-3 ($N = 308$), isolating generational changes within a single family; (4)~\emph{Within-subject}: per-subject DIF to test domain concentration; and (5)~\emph{Random split}: two random halves of the 2023 cohort ($N = 540$ each) as a sanity check.
38	
39	\subsection{Semi-Synthetic Injection Framework}
40	\label{sec:injection}
41	
42	To evaluate whether MH-DIF can detect differential contamination when it is present, we construct a semi-synthetic framework with controlled ground truth.
43	
44	\paragraph{Procedure.} From items classified as ETS~A in the uninjected data (negligible DIF), we select 20\% uniformly at random as the ``contaminated'' set. For each contaminated item, we flip incorrect responses to correct in the focal group at exploitation rate $p \in \{0.0, 0.3, 0.5, 0.7, 1.0\}$. We then run MH-DIF on the modified response matrix and measure detection performance. We report $\Delta\mathrm{TPR} = \mathrm{TPR}(\text{injected}) - \mathrm{TPR}(\text{baseline})$ and $\Delta\mathrm{FPR} = \mathrm{FPR}(\text{injected}) - \mathrm{FPR}(\text{baseline})$, where TPR is the true positive rate on injected items and FPR is the false positive rate on uninjected items. Each injection level is repeated across 5 random seeds for uncertainty estimation.
45	
46	\paragraph{Cross-subject matching.} The choice of matching variable is critical for valid semi-synthetic evaluation. When contamination is injected into items within subject $X$, the total score on subject $X$ absorbs part of the injection signal. Using this contaminated total score as the MH matching variable violates the conditional independence assumption and inflates FPR. Cross-subject matching resolves this problem by computing the matching variable from all subjects \emph{other than} the one being tested. Under this protocol, $\Delta\mathrm{FPR} = 0.000$ across all five MMLU domains (bootstrap 95\% CI $= [0.000, 0.000]$, 5,000 resamples), while detection power is preserved ($\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$ for four of five subjects). The zero FPR is a structural guarantee: cross-subject stratification scores are algebraically invariant to within-subject injection~\citep{clauser1998dif, nandakumar1993dif}. We adopt cross-subject matching as the standard protocol for all semi-synthetic analyses.
47	
48	Diagnostic procedures (Yen's Q3 local independence, domain-specificity analysis, instability decomposition) and statistical details (multiple testing correction, threshold sensitivity, architecture heterogeneity checks) appear in \Cref{app:method_details}.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "047b824f-c7dd-46c9-a66b-d30a8e0ea9e3",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "57581d1c-3a58-4bd7-863d-ca5edf244c11",
  "sourceToolAssistantUUID": "047b824f-c7dd-46c9-a66b-d30a8e0ea9e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T11:55:24.834Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NZwSPdcyoW1dApVAKnNjAK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57581d1c-3a58-4bd7-863d-ca5edf244c11",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfrCHV8t1tmmceFRff2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5462ef2-cbaa-45dc-a542-b48f80487f16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013XzZVASBoLuBdKMC5tMjmw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 190,
      "cache_read_input_tokens": 19328,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 190
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 317,
          "cache_read_input_tokens": 19328,
          "cache_creation_input_tokens": 190,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 190,
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

_source line 24 · 2026-05-21T11:55:24.840Z_

<details><summary>↩ Tool result · `toolu_01NZwSPdcyoW1dApVAKnNjAK`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	A power analysis using empirical MMLU IRT parameters confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$. Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold.
10	
11	\subsection{Temporal Comparability: 31\% Item Instability}
12	\label{sec:temporal}
13	
14	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold on effect size and significance already provides implicit multiple-testing protection.
15	
16	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C items (sampling noise), and an ability-quintile comparison within the same temporal cohort yields 2.9\% (ability differences alone). A within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% ETS~C items, elevated by large ability gaps that confound the DIF signal~\citep{holland1988mh}. The contrast between 2.9\% (ability-controlled) and 61.3\% (ability-confounded) brackets the temporal rate of 31.3\%. Crucially, the temporal cohort ability gap is negligible: Cohen's $d = -0.17$ (below the $|d| = 0.2$ small-effect threshold) with 76.4\% distributional overlap. Under strict 1:1 nearest-neighbor matching ($d \approx -0.010$, $N = 638$ per group, 5 seeds), C\% $= 28.9\% \pm 0.1\%$---a 7.7\% relative reduction from 31.3\%, confirming that at most $\sim$2.4 pp of observed DIF is attributable to ability mismatch.
17	
18	Across all 57 MMLU subjects, C\% ranges from 20.7\% to 48.4\% (mean $\approx 30\%$); within-subject matching on 5 subjects yields 38.1\% as a robustness check (\Cref{tab:temporal_landscape}). Item-level logistic regression shows domain accuracy improvement explains only 2.4 percentage points of 31.3\% C\% (pseudo $R^2 = 0.0007$); 92.4\% of instability is item-specific. Odds ratio regression reveals a Simpson's paradox: domain accuracy improvement positively predicts DIF at the aggregate level ($\mathrm{OR} = 1.55$ per 10 pp, $p = 0.001$) but reverses after controlling for item difficulty and discrimination ($\mathrm{OR} = 0.73$, $p = 0.030$; LR $\chi^2 = 647$), confirming that item properties---not accuracy gains---drive DIF classification. The conclusion is robust across thresholds: C\% $= 48.9\%$ at $|\Delta_{\mathrm{MH}}| \geq 1.0$, $18.3\%$ at $\geq 2.0$, $10.2\%$ at $\geq 2.5$.
19	
20	\begin{table}[t]
21	\centering
22	\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\Delta_{\mathrm{MH}}| \geq 1.5$. FPR is measured against Li et al.\ web-overlap labels on the ``clean'' (non-overlapping) subset. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels.}
23	\label{tab:temporal_landscape}
24	\small
25	\resizebox{\columnwidth}{!}{%
26	\begin{tabular}{lcccc}
27	\toprule
28	Cohort Definition & $N_{\mathrm{ref}}$ / $N_{\mathrm{focal}}$ & C\% & FPR (clean) & Enrich. \\
29	\midrule
30	Temporal (2023 vs.\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.964 \\
31	Ability quintile (Q1--2 vs.\ Q4--5) & ${\sim}$2,600 / ${\sim}$2,600 & 2.9 & 0.027 & 1.19 \\
32	Within-family (Llama-2 vs.\ 3) & 161 / 308 & 61.3 & -- & -- \\
33	Random split (sanity) & 540 / 540 & 0.18 & -- & -- \\
34	Within-subject (avg, 5 subj.) & \textit{varies} & 38.1 & -- & -- \\
35	\bottomrule
36	\end{tabular}}
37	\end{table}
38	
39	\subsection{Ground Truth Mismatch}
40	\label{sec:groundtruth}
41	
42	Direct comparison of DIF flags against the web-overlap labels of \citet{li2024contamination} on 9,229 annotated items confirms that the two methods capture orthogonal signals. The enrichment ratio is 0.964 (\Cref{tab:temporal_landscape}): DIF-C rates are 30.7\% among web-contaminated items and 31.8\% among clean items. Association tests yield $\phi = 0.012$, $\chi^2 = 1.28$ ($p = 0.258$), and OR $= 1.05$ [0.96, 1.15]; the Jaccard index between flagged sets is 0.206. This near-independence holds across contamination subtypes (input-only enrichment $= 0.986$, input-and-label $= 0.960$). The null result does not indicate detection failure: semi-synthetic injection produces a clear dose-response ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \Cref{fig:dose_response}). The disconnect arises because web-overlap labels measure \emph{global exposure} (whether an item exists in training corpora), while DIF measures \emph{differential functioning} (whether an item's relationship to ability changes across cohorts). The Li et al.\ labels are the wrong ground truth for a differential method.
43	
44	\begin{figure}[t]
45	\centering
46	\includegraphics[width=\columnwidth]{fig_2_dose_response.pdf}
47	\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\Delta\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF detects differential contamination when present. Baseline (no injection) produces $\Delta\mathrm{TPR} \approx 0$.}
48	\label{fig:dose_response}
49	\end{figure}
50	
51	\subsection{Structural Analysis}
52	\label{sec:structural}
53	
54	Three structural controls fail to reduce temporal C\% below 31\%: matched-ability quintiles, IRT $\theta$-conditioning ($r(\theta, \mathrm{total\ score}) = 0.9986$, FPR $= 0.312$), and within-subject DIF (C\% $= 38.1\%$, exceeding the 25\% bifactor viability threshold). Logistic regression DIF confirms 92.1\% concordance with MH and reveals additional non-uniform DIF (24.8\% at $|\beta_{\mathrm{interaction}}| \geq 0.5$), making the 31\% estimate conservative. Graduated de-duplication ($K{=}10$: 22.7\% vs.\ random 26.8\%; $K{=}20$: 29.1\% vs.\ 30.9\%) confirms family structure does not inflate C\%. Ability-matched within-family analysis reduces Llama-2 vs.\ Llama-3 C\% from 61.3\% to $28.3\% \pm 1.6\%$ (Cohen's $d = -0.99$, overlap $= 0.18$), while temporal matching reduces C\% from 31.3\% to $28.9\% \pm 0.1\%$ ($d = -0.17$, overlap $= 0.76$). The matched C\% values ($\sim$28--29\%) are consistent with each other despite vastly different unmatched rates (61.3\% vs.\ 31.3\%), suggesting that genuine item-level DIF accounts for $\sim$28--29\% of items, with the Llama comparison carrying 33 pp of additional ability confound (54\% reduction) versus only 2.4 pp for temporal cohorts (7.7\% reduction). Full details in \Cref{app:structural}.
55	
56	\subsection{Semi-Synthetic Framework Validation}
57	\label{sec:semisynthetic}
58	
59	The critical methodological finding is that the choice of matching strategy determines validity. Cross-subject matching computes the conditioning variable from subjects \emph{other than} the one being tested, achieving $\Delta\mathrm{FPR} = 0.000$ across all five MMLU subjects while four of five produce $\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$. Within-subject matching inflates FPR by ${+}0.186$ on average because the matching variable absorbs part of the injection signal. We adopt cross-subject matching as the standard protocol (\Cref{app:fig_matching}).
60	
61	\subsection{Downstream Impact}
62	\label{sec:downstream}
63	
64	Spearman correlation between full and stable-item rankings is $\rho \approx 0.997$: aggregate model ordering is preserved despite 31\% item instability. DIF-flagged items nonetheless carry more discriminative signal than average ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal across 21 conditions), though a circularity ablation shows DIF-based removal is the \emph{least} disruptive among non-random strategies (Jaccard overlap with high-discrimination items is only 0.12). Individual model families show distinctive DIF profiles: Llama-3 derivatives gain a median of ${+}53$ rank positions (mean ${+}121$), while Mistral-based models lose a median of $35$ (mean $-54$); individual extremes reach ${+}793$ and $-542$ (\Cref{app:fig_downstream}). Overall, 25\% of models shift by $|\Delta\mathrm{Rank}| \geq 100$. \Cref{sec:gsm8k} demonstrates that this instability pattern extends across all six METABENCH benchmarks.
65	
66	\subsection{Cross-Benchmark Validation}
67	\label{sec:gsm8k}
68	
69	Temporal DIF extends across all six METABENCH benchmarks (\Cref{tab:cross_benchmark}). C\% ranges from 17.9\% (HellaSwag) to 31.3\% (MMLU), each 45--174$\times$ above its random-split baseline---none attributable to sampling noise. A task-type dichotomy emerges: knowledge and reasoning benchmarks (MMLU, WinoGrande~\citep{sakaguchi2021winogrande}, TruthfulQA~\citep{lin2022truthfulqa}, ARC~\citep{clark2018arc}) show C\% $= 26.9$--$31.3\%$, while procedural benchmarks (GSM8K, HellaSwag~\citep{zellers2019hellaswag}) show C\% $= 17.9$--$18.9\%$, consistent with knowledge-intensive items being more sensitive to shifts in training data composition across model generations.
70	
71	\begin{table}[t]
72	\centering
73	\caption{Temporal DIF across six METABENCH benchmarks. C\% = ETS~C items ($|\Delta_{\mathrm{MH}}| \geq 1.5$) between 2023 and 2024 cohorts. All six show substantial instability (45--174$\times$ above random baseline), with knowledge/reasoning benchmarks exhibiting higher C\% than procedural ones.}
74	\label{tab:cross_benchmark}
75	\small
76	\begin{tabular}{lrrrl}
77	\toprule
78	Benchmark & Items & C\% & Rand.\ C\% & Ratio \\
79	\midrule
80	MMLU & 12{,}508 & 31.3 & 0.18 & 174$\times$ \\
81	WinoGrande & 1{,}267 & 30.3 & 0.32 & 95$\times$ \\
82	TruthfulQA & 817 & 29.7 & 0.37 & 80$\times$ \\
83	ARC & 1{,}172 & 26.9 & 0.60 & 45$\times$ \\
84	GSM8K & 1{,}319 & 18.9 & 0.30 & 63$\times$ \\
85	HellaSwag & 10{,}042 & 17.9 & 0.28 & 64$\times$ \\
86	\bottomrule
87	\end{tabular}
88	\end{table}
89	
90	On GSM8K specifically, semi-synthetic injection with external matching confirms detection power ($\Delta\mathrm{TPR} = {+}0.514$ at $p = 0.5$; \Cref{app:gsm8k_details}). An exploratory GSM1K analysis ($N = 33$) shows a negative correlation between contamination gap and DIF ranking advantage ($r = -0.478$, $p = 0.005$; partial $r = -0.385$, $p = 0.027$), suggesting DIF captures capability change distinct from memorization (\Cref{app:fig_gsm1k}).
91	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5462ef2-cbaa-45dc-a542-b48f80487f16",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "4f60e0b5-308a-4c35-b4c2-ef8641a386f8",
  "sourceToolAssistantUUID": "b5462ef2-cbaa-45dc-a542-b48f80487f16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T11:55:28.944Z_

<details open><summary>🔧 Tool call — Read · `toolu_011NvTJSaGgW7u2iNSnntn9J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f60e0b5-308a-4c35-b4c2-ef8641a386f8",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfrXX8b1P3DMUe5khLc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46bcbb8b-3878-40cb-80d4-3070c24d2478",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JM7jKT4yeReknSeVoWPYR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9325,
      "cache_read_input_tokens": 19518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9325,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 26 · 2026-05-21T11:55:28.950Z_

<details><summary>↩ Tool result · `toolu_011NvTJSaGgW7u2iNSnntn9J`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Implications for Benchmark Temporal Comparability}
5	\label{sec:disc_temporal}
6	
7	The 31\% ETS~C instability on MMLU is robust across thresholds and structural controls (\Cref{sec:structural}), and extends across all six METABENCH benchmarks (C\% $= 17.9$--$31.3\%$, 45--174$\times$ above random baselines; \Cref{tab:cross_benchmark}). Knowledge/reasoning benchmarks show higher instability (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$), and a Simpson's paradox in odds ratio regression ($\mathrm{OR}: 1.55 \to 0.73$ after controlling for item properties; LR $\chi^2 = 647$) confirms that item properties---not accuracy gains---drive DIF. This does not invalidate these benchmarks as ranking instruments ($\rho \approx 0.997$) but signals measurement drift across model generations.
8	
9	\subsection{Ground Truth Meta-Critique}
10	\label{sec:disc_groundtruth}
11	
12	The near-independence between DIF flags and web-overlap labels (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$; consistent across contamination subtypes) exposes a category error: web-overlap labels identify a condition shared by nearly all MMLU items (global exposure), so evaluating a differential method against them conflates two phenomena. Item-level differential detectors require item-level differential ground truth.
13	
14	\subsection{DIF as Diagnostic Lens}
15	\label{sec:disc_diagnostic}
16	
17	The GSM1K correlation ($r = -0.478$, $p = 0.005$, $N = 33$; \Cref{sec:gsm8k}) provides exploratory evidence that DIF-flagged items capture behavioral change distinct from memorization; partial correlation ($r = -0.385$, $p = 0.027$) after controlling for accuracy confirms this is not an artifact of general model quality.
18	
19	Item characterization reinforces this: DIF-C items are harder ($d = -0.247$) and more discriminating ($d = 0.230$), distributed uniformly across subjects ($\chi^2$ $p = 0.32$). A difficulty $\times$ direction interaction ($\rho = -0.597$, $p < 0.001$) shows capability gains concentrate on hard items (88.7\% focal-favoring in hardest decile) while easy items erode (96.2\% reference-favoring in easiest decile).
20	
21	Yen's Q3 analysis confirms that local dependence does not drive DIF: extreme LD correlates negligibly with subject-level C\% ($r = 0.09$, $p = 0.50$), while reasoning-heavy domains with low LD show higher DIF ($r = -0.36$, $p = 0.006$).
22	
23	\subsection{Recommended DIF Audit Protocol}
24	\label{sec:disc_protocol}
25	
26	These findings motivate a concrete benchmark maintenance protocol requiring only a binary response matrix and temporal cohort labels. We recommend: (1)~quarterly MH-DIF audits (or whenever $N \geq 80$ new models appear), using cross-subject matching; (2)~benchmark-wide C\% $> 20\%$ triggers item review, with items flagged ETS~C in consecutive audits labeled ``unstable''; (3)~graduated responses: flag-and-annotate, item rotation, or weighted scoring.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46bcbb8b-3878-40cb-80d4-3070c24d2478",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "a836cff4-87d2-40d6-a10a-14ccc5b683bd",
  "sourceToolAssistantUUID": "46bcbb8b-3878-40cb-80d4-3070c24d2478",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T11:55:29.430Z_

<details open><summary>🔧 Tool call — Read · `toolu_01D4yB1MvqPxYMTHfcP43s8q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a836cff4-87d2-40d6-a10a-14ccc5b683bd",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfrXX8b1P3DMUe5khLc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7be9a2fb-a3a8-4e07-875a-4d092290a832",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JM7jKT4yeReknSeVoWPYR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9325,
      "cache_read_input_tokens": 19518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9325,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 28 · 2026-05-21T11:55:29.435Z_

<details><summary>↩ Tool result · `toolu_01D4yB1MvqPxYMTHfcP43s8q`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Applying MH-DIF analysis to six METABENCH benchmarks (27,125 items, 5,227 models), we find 17.9--31.3\% temporal item instability under ETS~C classification---knowledge/reasoning benchmarks are more affected (C\% $\geq 26.9\%$) than procedural ones (C\% $\leq 18.9\%$). The instability is confirmed non-random (random controls $\leq 0.6\%$) and item-specific; a Simpson's paradox in odds ratio regression confirms item properties, not accuracy gains, drive DIF. Web-overlap labels show near-independence with DIF flags (enrichment $\approx 0.96$); our semi-synthetic framework ($\Delta\mathrm{FPR} = 0.000$, $\Delta\mathrm{TPR} = {+}0.508$) provides a controlled alternative.
5	
6	DIF-flagged items concentrate discriminative information ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal) and exhibit a difficulty--direction interaction ($\rho = -0.597$): capability gains on hard items, erosion on easy ones. DIF is a diagnostic lens, not a quality filter. LLM benchmarks need psychometric monitoring alongside score reporting.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7be9a2fb-a3a8-4e07-875a-4d092290a832",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "2fa060fd-4ba2-4ebd-874f-256b2b21f910",
  "sourceToolAssistantUUID": "7be9a2fb-a3a8-4e07-875a-4d092290a832",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T11:55:30.065Z_

<details open><summary>🔧 Tool call — Read · `toolu_01417uzvegvELozBjhu7CAfC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fa060fd-4ba2-4ebd-874f-256b2b21f910",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfrXX8b1P3DMUe5khLc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd660219-f087-4038-8722-6967c2070218",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JM7jKT4yeReknSeVoWPYR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9325,
      "cache_read_input_tokens": 19518,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9325,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 30 · 2026-05-21T11:55:30.071Z_

<details><summary>↩ Tool result · `toolu_01417uzvegvELozBjhu7CAfC`</summary>

```text
1	\section*{Limitations}
2	
3	\paragraph{Methodological scope of MH-DIF.}
4	The Mantel-Haenszel procedure detects only \emph{uniform} DIF, where the odds ratio between cohorts is constant across ability strata. Logistic regression DIF analysis reveals an additional 24.8\% of items exhibiting non-uniform DIF ($|\beta_{\mathrm{interaction}}| \geq 0.5$), making the 31\% ETS~C estimate conservative. Future work should apply non-uniform DIF methods (e.g., logistic regression or IRT-based approaches) as the primary analysis to capture the full spectrum of item instability. Critically, MH-DIF is nonparametric and conditions on observed total score, not latent $\theta$---its validity does not depend on IRT model fit~\citep{holland1988mh}. Our Yen's Q3 analysis confirms that local dependence domains do not correlate with DIF domains ($r = 0.09$, $p = 0.50$), further supporting the robustness of the MH procedure in this setting.
5	
6	\paragraph{Ability confounding.}
7	Although the temporal cohort ability gap is negligible (Cohen's $d = -0.17$, overlap $= 76.4\%$) and nearest-neighbor matching confirms that at most 2.4 percentage points of C\% are attributable to ability mismatch, within-family comparisons with large ability gaps (e.g., Llama-2 vs.\ Llama-3, $d = -0.99$) produce substantially inflated C\% (61.3\% unmatched vs.\ 28.3\% matched). Any application of MH-DIF to cohorts with larger ability differences must incorporate ability matching or stratification beyond the standard 5-strata procedure.
8	
9	\paragraph{Sample size requirements.}
10	Our power analysis indicates reliable ETS~C detection requires $N \geq 80$ per cohort. The temporal cohorts (1,080 and 807 models) far exceed this threshold, but the GSM1K correlation analysis ($N = 33$) has limited statistical power (95\% CI $= [-0.71, -0.16]$). The negative correlation between contamination gap and DIF ranking advantage ($r = -0.478$) is exploratory and warrants replication with larger model samples.
11	
12	\paragraph{Contamination vs.\ capability change.}
13	DIF analysis detects \emph{that} items function differently across cohorts but cannot determine \emph{why}. The differential signal may reflect contamination, capability change, training methodology shifts, or interactions among these factors. We present evidence that DIF captures something distinct from memorization (negative GSM1K correlation, semi-synthetic dose-response), but a definitive causal decomposition remains out of reach without access to model training data.
14	
15	\paragraph{Benchmark scope.}
16	We analyze six METABENCH benchmarks (MMLU, WinoGrande, TruthfulQA, ARC, GSM8K, HellaSwag; 27,125 total items), all multiple-choice or short-answer benchmarks scored as binary correct/incorrect. The generalizability to open-ended generation benchmarks (e.g., AlpacaEval, MT-Bench), coding benchmarks (e.g., HumanEval), or benchmarks with non-binary scoring remains untested. The binary response format is a prerequisite for MH-DIF; extending to continuous or partial-credit scoring would require polytomous DIF methods.
17	
18	\paragraph{Temporal cohort definition.}
19	We define cohorts by calendar year of model release (2023 vs.\ 2024), a coarse grouping that aggregates models with diverse training pipelines, data mixtures, and post-training procedures. Finer-grained cohort definitions (e.g., by training data cutoff, model family, or alignment method) might reveal more targeted patterns of item instability but would reduce per-cohort sample sizes and statistical power.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd660219-f087-4038-8722-6967c2070218",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "519aaae1-ec89-4077-b810-8b5db0e555a7",
  "sourceToolAssistantUUID": "bd660219-f087-4038-8722-6967c2070218",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T11:55:30.374Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JPgqRrKeHFVgWxDamdeCmv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "519aaae1-ec89-4077-b810-8b5db0e555a7",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfrXX8b1P3DMUe5khLc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8c21ccf-4a0b-440d-903b-4f02c7e51493",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JM7jKT4yeReknSeVoWPYR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9325,
      "cache_read_input_tokens": 19518,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9325
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 19518,
          "cache_creation_input_tokens": 9325,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9325,
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

_source line 32 · 2026-05-21T11:55:30.379Z_

<details><summary>↩ Tool result · `toolu_01JPgqRrKeHFVgWxDamdeCmv`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues. Performance-based detectors identify contamination through statistical anomalies: ConStat \citep{dekoninck2024constat} tests performance gaps between original and perturbed items, DVD \citep{liang2026dvd} uses distributional verification, and Self-Critique \citep{tao2026selfcritique} employs model self-evaluation. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (Claim~2, \Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introduced IRT to NLP, \citet{vania2021irt} assessed test set discriminability, and \citet{rodriguez2021evaluation} demonstrated that not all evaluation examples are equally informative. Recent extensions include PSN-IRT \citep{zhou2026psnirt} for benchmark quality at scale, TinyBenchmarks \citep{maiapolo2024tinybenchmarks} for IRT-based item selection, and scalability coefficients for detecting bad benchmark items \citep{hardy2026scalability}. The closest concurrent work is Growing Pains \citep{habba2026growingpains}, which addresses score comparability through fixed-parameter calibration \citep[FPC;][]{kim2019fpc}. Our work is complementary: Growing Pains assumes anchor item stability, while DIF analysis diagnoses which items violate this assumption.
9	
10	\paragraph{DIF Methodology and Measurement Invariance.}
11	The Mantel-Haenszel procedure for DIF detection was introduced by \citet{holland1988mh} and remains the most widely used method in educational testing due to its simplicity and well-characterized statistical properties \citep{clauser1998dif}. Alternative approaches include logistic regression DIF \citep{swaminathan1990logistic}, SIBTEST \citep{shealy1993sibtest}, Lord's $\chi^2$ test \citep{lord1980irt}, and the Raju area method \citep{raju1988area}; \citet{zumbo1999handbook} provides a comprehensive comparison. DIF analysis is a specific instance of measurement invariance testing \citep{meredith1993invariance, vandenberg2000invariance}, which examines whether a measurement instrument functions equivalently across populations. MIMIC models offer a latent-variable approach to the same problem \citep{muthen1985mimic, woods2009mimic}, and \citet{teresi2007dif} reviews DIF methods across applied domains. Cross-subject matching---computing the stratification variable from domains other than the one being tested---has psychometric precedent in the DIF literature \citep{nandakumar1993dif,donoghue1993mh}; our adaptation addresses LLM-specific challenges of multi-domain local dependence and simultaneous contamination control at scale. We do not modify the MH procedure; our contribution is the application context and the empirical findings it reveals. The scale of this analysis (5,227 examinees across a 57-subject multidimensional ability space) exceeds typical educational testing applications, where \citet{belzak2020smallsample} note that DIF methods can behave differently at extreme sample sizes. The primary methodological challenge is the impact-versus-DIF confound: genuine ability differences between temporal cohorts can inflate DIF estimates. We address this through matched-ability quintile analysis, IRT $\theta$-conditioning, and a random-split control (\Cref{sec:temporal}).
12	
13	\paragraph{Benchmark Design and Evaluation.}
14	Dynamic benchmarks such as Dynabench \citep{kiela2021dynabench}, LatestEval \citep{li2024latesteval}, and LiveBench \citep{white2025livebench} mitigate contamination by construction, yet none provides psychometric equating across versions. Chatbot Arena \citep{chiang2024chatbot} sidesteps static benchmarks through pairwise preference. Broader surveys \citep{chang2024survey, burnell2023rethink} identify benchmark saturation and lack of item-level transparency as systemic challenges. Our DIF analysis fills this gap by identifying which items have become unreliable for cross-generation comparison. METABENCH \citep{kipnis2024metabench} provides the large-scale response matrix that makes this analysis possible.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8c21ccf-4a0b-440d-903b-4f02c7e51493",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "703e1146-fcd6-41ec-a9a3-9f6a137f6e72",
  "sourceToolAssistantUUID": "e8c21ccf-4a0b-440d-903b-4f02c7e51493",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T11:55:32.968Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RhuZ7cq7jwbYgf88tpeZER`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "703e1146-fcd6-41ec-a9a3-9f6a137f6e72",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfrwWGWwn933K7LWZbE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b5d92b9-1d6c-4bb6-8922-19924b684c5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAMDfnHqUjEUPN7H6rvk13",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4073,
      "cache_read_input_tokens": 28843,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4073
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 93,
          "cache_read_input_tokens": 28843,
          "cache_creation_input_tokens": 4073,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4073,
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

_source line 34 · 2026-05-21T11:55:32.975Z_

<details><summary>↩ Tool result · `toolu_01RhuZ7cq7jwbYgf88tpeZER`</summary>

```text
1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini-Hochberg FDR correction at $q = 0.05$. The random-split sanity check provides an empirical estimate of the false positive rate under the null hypothesis.
19	
20	\paragraph{Threshold sensitivity.} We report results across a range of DIF thresholds ($|\Delta_{\mathrm{MH}}| \in \{1.0, 1.5, 2.0, 2.5\}$) to verify that qualitative conclusions do not depend on the specific ETS~C cutoff. The standard threshold of $|\Delta_{\mathrm{MH}}| \geq 1.5$ corresponds to the ETS~C definition used throughout the paper.
21	
22	\paragraph{Architecture heterogeneity.} The METABENCH MMLU population consists of 99.98\% decoder-only models (5,226 of 5,227). This near-complete architectural homogeneity eliminates architecture as a confound for DIF analysis. We verify this by excluding the single encoder-decoder model and confirming identical results.
23	
24	\section{Structural Analysis Details}
25	\label{app:structural}
26	
27	Three progressively refined approaches fail to reduce the temporal false positive rate below 31\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal FPR unchanged at approximately 0.31. IRT $\theta$-conditioning with 20 ability strata achieves $r(\theta, \mathrm{total\ score}) = 0.9986$ and FPR $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. Within-subject DIF analysis on 5 representative subjects, intended to isolate subject-specific effects, finds mean C\% $= 38.1\%$, exceeding the 25\% threshold that would indicate viable bifactor structure. \Cref{tab:structural_comparison} summarizes these results.
28	
29	The temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\% of within-subject item pairs exceed $|Q3| > 0.20$, vs.\ 2.2\% cross-subject; $5{\times}$ ratio, $p = 2.3 \times 10^{-9}$), which contributes to elevated within-subject DIF rates but is not the primary driver: the cross-subject matching protocol addresses this bias, and temporal C\% persists under external matching (full Q3 distributions in Appendix~Figure~A2).
30	
31	\begin{table}[h]
32	\centering
33	\caption{Structural approaches to reducing temporal DIF. None reduces baseline FPR below 31\%, indicating that the observed instability is not an artifact of ability matching. Subscript $\pm$ values denote standard deviations across 5 injection seeds (baseline row only).}
34	\label{tab:structural_comparison}
35	\small
36	\resizebox{\columnwidth}{!}{%
37	\begin{tabular}{lcccc}
38	\toprule
39	Approach & Mechanism & Temp.\ FPR & TPR ($p{=}0.5$) & Outcome \\
40	\midrule
41	Baseline (ext.) & Cross-bench.\ total score & $0.314_{\pm.009}$ & $0.834_{\pm.027}$ & Reference \\
42	Matched-ability & Within-quintile temp.\ DIF & ${\sim}$0.31 & -- & Enrich.\ 0.94--1.04 \\
43	$\theta$-cond. & $\theta$ replaces total score & 0.312 & 0.876 & $r(\theta,\mathrm{total}) {=} 0.9986$ \\
44	Within-subject & Per-subject DIF & -- & -- & C\% $= 38.1\%$ ($>$25\%) \\
45	\bottomrule
46	\end{tabular}}
47	\end{table}
48	
49	\section{Additional Figures}
50	\label{app:figures}
51	
52	\begin{figure}[h]
53	\centering
54	\includegraphics[width=\columnwidth]{fig_3_within_subject_matching.pdf}
55	\caption{Cross-subject vs.\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}
56	\label{app:fig_matching}
57	\end{figure}
58	
59	\begin{figure}[h]
60	\centering
61	\includegraphics[width=\columnwidth]{fig_4_downstream_impact.pdf}
62	\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\rho \approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only.}
63	\label{app:fig_downstream}
64	\end{figure}
65	
66	\begin{figure}[h]
67	\centering
68	\includegraphics[width=\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}
69	\caption{GSM1K contamination gap vs.\ DIF ranking advantage ($N = 33$). The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items.}
70	\label{app:fig_gsm1k}
71	\end{figure}
72	
73	\section{Cross-Benchmark Comparison}
74	\label{app:gsm8k_details}
75	
76	\begin{table}[h]
77	\centering
78	\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal item instability with validated semi-synthetic detection power. Standard and external matching use different exploitation rates ($p$) because each benchmark's optimal operating point differs; external matching results are compared at $p = 0.5$ for both. Subscript $\pm$ values denote standard deviations across 5 random injection seeds.}
79	\label{tab:gsm8k_comparison}
80	\small
81	\begin{tabular}{lcc}
82	\toprule
83	Metric & MMLU & GSM8K \\
84	\midrule
85	Items & 12,508 & 1,319 \\
86	Models & 5,227 & 6,702 \\
87	Temporal C\% & 31.3\% & 18.9\% \\
88	Sanity C\% & 0.18\% & 0.3\% \\
89	$\Delta$TPR ($p{=}0.7$, standard) & -- & $+0.818_{\pm.006}$ \\
90	$\Delta$TPR ($p{=}0.5$, external) & $+0.508_{\pm.027}$ & $+0.514_{\pm.028}$ \\
91	\bottomrule
92	\end{tabular}
93	\end{table}
94	
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b5d92b9-1d6c-4bb6-8922-19924b684c5e",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "8032005a-92d9-4562-af80-e7085bccf52c",
  "sourceToolAssistantUUID": "4b5d92b9-1d6c-4bb6-8922-19924b684c5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-21T11:55:36.002Z_

Now let me check the experiment plan and any analysis scripts to evaluate reproducibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8032005a-92d9-4562-af80-e7085bccf52c",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfs8ESNaNyByLYLgG1T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4f40380-dd35-496f-808e-82ab073223b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUL6fEM1GyeSijqvHWiGPH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2532,
      "cache_read_input_tokens": 32916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2532,
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

_source line 36 · 2026-05-21T11:55:36.458Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TLMQ6v4e6k9kga56VcK8wy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/experiment_plan.yaml",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4f40380-dd35-496f-808e-82ab073223b5",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfs8ESNaNyByLYLgG1T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f142287e-4f50-413a-892f-fc38a66ee76c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUL6fEM1GyeSijqvHWiGPH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2532,
      "cache_read_input_tokens": 32916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2532,
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

_source line 37 · 2026-05-21T11:55:36.464Z_

<details><summary>↩ Tool result · `toolu_01TLMQ6v4e6k9kga56VcK8wy`</summary>

```text
1	experiments:
2	  # === P0: Headline Results (must run) ===
3	
4	  - id: plan_001
5	    name: real_data_dif_mmlu
6	    claim: 1
7	    description: >
8	      Apply DIF analysis to METABENCH MMLU response matrix (5,219 models × 12,508 items).
9	      Data characteristics: only 37% models classifiable by family (1,929); effective temporal
10	      span ~1.5 years (2023: N=1,253, 2024-H1: N=656); 15.4% items have negative discrimination.
11	      Design:
12	      (a) Primary cohort: temporal split (2023 vs 2024-H1, both N≥80 ✓)
13	      (b) Alternative cohort: accuracy-quintile split (ability-based grouping, uses all models)
14	      (c) Item filtering: run with and without negative-discrimination items (sensitivity analysis)
15	      Run ETS C DIF detection on all items under both cohort definitions.
16	      Proxy validation against Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items,
17	      73.8% coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic
18	      (item exists on web), while DIF detects cohort-differential contamination (item behaves
19	      differently across temporal cohorts). Low concordance is EXPECTED — DIF only catches items
20	      where contamination is differential across cohorts, not uniform. Primary validation metric:
21	      FPR analysis (DIF flags on Li-et-al-clean items) rather than TPR (which conflates uniform
22	      vs differential contamination). Unlabeled items (26.2%) reported separately as "unknown".
23	      plan_011 (semi-synthetic injection) provides controlled ground truth to complement this proxy.
24	      (d) Within-family confound control: run DIF within model families where both versions
25	          have N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)
26	          below threshold — use as supplementary only. Identify additional qualifying pairs from
27	          METABENCH metadata. If DIF flags
28	          items that are NOT differentially contaminated within-family, the flag reflects capability
29	          gain, not contamination. Report: DIF flag overlap between cross-cohort and within-family
30	          analyses to disentangle contamination from capability improvement.
31	      (e) Domain-specificity analysis: correlate DIF flags with MMLU subject categories to check
32	          whether flags cluster in domains with known capability jumps vs known contamination.
33	      Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix +
34	      within-family confound control + domain-specificity analysis.
35	    priority: P0
36	    gpu_budget_hours: 0
37	    deps: []
38	    registry_id: ""
39	
40	  - id: plan_002
41	    name: rl_robustness_validation
42	    claim: 1
43	    description: >
44	      Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:
45	      - "Alignment RL" (DPO/ORPO/KTO) = offline preference optimization, does NOT produce
46	        the NLL gap contraction that Wang et al. demonstrate. METABENCH has 477 such models.
47	      - "Reasoning RL" (GRPO/PPO online training) = the mechanism that conceals contamination
48	        signals. This is what Claim 1 targets. METABENCH has almost none of these.
49	      Design (Reviewer-validated):
50	      (a) SFT-only cohort from METABENCH as baseline
51	      (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH as mechanism control —
52	          DPO doesn't use PPO clipping, so no NLL gap contraction; if DIF works on both
53	          (a) and (b), robustness covers the full RL spectrum
54	      (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference
55	          on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort
56	          (not a standalone group): DIF is group-level, so we verify that adding RL models
57	          to a cohort doesn't degrade detection. Separately, run traditional detectors
58	          (Min-K%, ConStat) on these 10-15 models individually to show per-model degradation.
59	      Two-level validation:
60	      - Group level: DIF flags same items regardless of cohort composition (a/b/c) → robust
61	      - Model level: traditional detectors degrade on (c) individuals → fragile
62	      This design works even with only 10-15 reasoning-RL models because DIF doesn't need
63	      N≥80 RL models — it needs N≥80 in the cohort total, and RL models are mixed in.
64	      Statistical rigor requirements:
65	      - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%)
66	      - DeLong test or permutation test for pairwise AUROC differences
67	      - TOST equivalence testing for DIF retention ratio vs ConStat (not just null-result reasoning)
68	      (d) Partial exploitation power analysis: formally characterize DIF detection power as
69	          function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model answers
70	          memorized items correctly with probability p, shrinking DIF effect size by ~p.
71	          Show detection boundary and ensemble coverage handoff point.
72	    priority: P0
73	    gpu_budget_hours: 100
74	    deps: [plan_001]
75	    registry_id: ""
76	
77	  - id: plan_003a
78	    name: constat_perturbation_eval
79	    claim: 2
80	    description: >
81	      Independent evaluation of ConStat-style perturbation testing on MMLU:
82	      (a) Generate semantically equivalent reformulations for 200+ MMLU items using LLM paraphrasing
83	      (b) Compare model performance on original vs reformulated items
84	      (c) Apply FDR-controlled detection (ConStat protocol)
85	      (d) Characterize detection power by effect size — expected strength on non-RL models, weakness on RL
86	      Even if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.
87	    priority: P0
88	    gpu_budget_hours: 80
89	    deps: [plan_001]
90	    registry_id: ""
91	
92	  - id: plan_003b
93	    name: dvd_generation_variance_eval
94	    claim: 2
95	    description: >
96	      Independent evaluation of DVD generation variance on MMLU:
97	      (a) Select 10-15 open-weight models with inference access
98	      (b) Generate 50 responses per item via temperature sampling (T=0.7-1.0)
99	      (c) Compute generation variance scores; detect bimodal distributions (contamination signal)
100	      (d) Characterize detection power for variant contamination vs verbatim contamination
101	      Standalone results provide variant-contamination detection baseline independent of DIF.
102	    priority: P0
103	    gpu_budget_hours: 70
104	    deps: [plan_001]
105	    registry_id: ""
106	
107	  - id: plan_003c
108	    name: ensemble_fusion
109	    claim: 2
110	    description: >
111	      Fuse DIF + ConStat + DVD into multi-signal ensemble:
112	      (a) Calibrate per-signal thresholds on subset of items with known contamination status
113	      (b) Evaluate 2-of-3 majority voting and weighted fusion strategies
114	      (c) Show ensemble coverage: DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant
115	      (d) Precision analysis: ensemble FPR<0.10 across all configurations
116	      (e) Cross-validate fusion weights (5-fold); report uniform-weight baseline alongside optimized
117	      Depends on 003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.
118	    priority: P0
119	    gpu_budget_hours: 0
120	    deps: [plan_001, plan_003a, plan_003b]
121	    registry_id: ""
122	
123	  # === P1: Strengthening Evidence ===
124	
125	  - id: plan_004
126	    name: cross_benchmark_gsm8k
127	    claim: 1
128	    description: >
129	      Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.
130	      Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard data
131	      or inference). Run DIF across temporal cohorts. Correlate DIF flags with
132	      per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability
133	      and provides an independent ground truth beyond Li et al. proxy labels.
134	    priority: P1
135	    gpu_budget_hours: 100
136	    deps: [plan_001]
137	    registry_id: ""
138	
139	  - id: plan_005
140	    name: bifactor_irt_equating_pilot
141	    claim: 3
142	    description: >
143	      Pilot bifactor IRT equating on MMLU:
144	      NOTE: METABENCH preproc.rds contains CTT statistics (p-value, rpbis), NOT IRT parameters.
145	      True IRT params are in mirt model objects (crossvalidate.R). Must either extract from
146	      METABENCH mirt RDS files or refit from the 5219×12508 response matrix.
147	      (a) Fit bifactor model to METABENCH MMLU data (general factor + subject-specific factors)
148	      (b) Select anchor items (high-stability, no DIF across cohorts)
149	      (c) Calibrate replacement items via fixed-parameter calibration (Kim & Kolen 2019)
150	      (d) Demonstrate equated score equivalence: model rankings on original vs replaced benchmark
151	      should correlate at Spearman rho ≥ 0.95 after equating.
152	    priority: P1
153	    gpu_budget_hours: 50
154	    deps: [plan_001]
155	    registry_id: ""
156	
157	  - id: plan_006
158	    name: item_generation_calibration
159	    claim: 3
160	    description: >
161	      Generate replacement items for DIF-flagged MMLU questions:
162	      (a) Use LLM generation with construct constraints (same subject, same cognitive level)
163	      (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty estimation)
164	      (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45 per arXiv 2602.06631)
165	      vs empirical calibration via student simulation
166	      (d) Validate on holdout model panel
167	    priority: P1
168	    gpu_budget_hours: 200
169	    deps: [plan_005]
170	    registry_id: ""
171	
172	  # === P2: Bonus / Extension ===
173	
174	  - id: plan_007
175	    name: cumulative_bayesian_dif
176	    claim: 1
177	    description: >
178	      Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).
179	      Simulate 4 successive benchmark administrations. Show power improvement
180	      from accumulating evidence: individual administration power ~0.40
181	      → cumulative power ~0.70 after 3 administrations for medium effects (δ=1.0).
182	    priority: P2
183	    gpu_budget_hours: 0
184	    deps: [plan_001]
185	    registry_id: ""
186	
187	  - id: plan_008
188	    name: graceful_degradation_analysis
189	    claim: 3
190	    description: >
191	      Formal analysis of benchmark validity under item replacement:
192	      (a) Define validity metrics (ranking stability, score reliability, construct coverage)
193	      (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced)
194	      (c) Establish theoretical bounds on validity degradation as function of replacement rate
195	      (d) Empirical validation using METABENCH data
196	    priority: P2
197	    gpu_budget_hours: 0
198	    deps: [plan_005, plan_006]
199	    registry_id: ""
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f142287e-4f50-413a-892f-fc38a66ee76c",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "f7b5e4ad-cef9-4852-a24e-ddd7d2226021",
  "sourceToolAssistantUUID": "f142287e-4f50-413a-892f-fc38a66ee76c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T11:55:37.085Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01THzjdCrH5QmcYrSqgE9qLf`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7b5e4ad-cef9-4852-a24e-ddd7d2226021",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfs8ESNaNyByLYLgG1T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "261579b1-6321-434a-89b1-4235870c27eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MUL6fEM1GyeSijqvHWiGPH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2532,
      "cache_read_input_tokens": 32916,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2532
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 32916,
          "cache_creation_input_tokens": 2532,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2532,
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

_source line 39 · 2026-05-21T11:55:37.106Z_

<details><summary>↩ Tool result · `toolu_01THzjdCrH5QmcYrSqgE9qLf`</summary>

```text
artifacts/_project/intermediate/dif_power_simulation.py
artifacts/dif_power_simulation.py
artifacts/dif_diagnostic.py
artifacts/_project/intermediate/dif_phase2_simulation.py
artifacts/dif_phase2_simulation.py
artifacts/_project/intermediate/metabench_explore.py
artifacts/_project/intermediate/metabench_explore_0bd873.py
artifacts/metabench_explore.py
artifacts/build_response_matrix.py
artifacts/plan_001/plan_001_analysis.py
artifacts/plan_001_real_data_dif_mmlu/intermediate/plan_001_analysis.py
artifacts/plan_001_real_data_dif_mmlu/data/plan_001_analysis.py
artifacts/plan_001b/plan_001b_analysis.py
artifacts/plan_001b/data/plan_001b_analysis.py
artifacts/plan_011/plan_011_analysis.py
artifacts/plan_011_semi_synthetic_validation/intermediate/plan_011_analysis_67f432.py
artifacts/plan_011_semi_synthetic_validation/intermediate/plan_011_analysis.py
artifacts/_project/intermediate/plan_012_irt_theta_analysis.py
artifacts/plan_012_irt_theta_conditioning/intermediate/plan_012_irt_theta_analysis.py
artifacts/plan_012/plan_012_irt_theta_analysis.py
artifacts/_project/intermediate/plan_014_within_subject_dif.py
artifacts/plan_014/plan_014_within_subject_dif.py
artifacts/_project/intermediate/plan_013_q3_analysis.py
artifacts/plan_013/plan_013_q3_analysis.py
artifacts/plan_015/plan_015_bifactor_analysis.py
artifacts/_project/intermediate/plan_016_within_subject_injection.py
artifacts/plan_016/plan_016_within_subject_injection.py
figures/paper/fig_2_dose_response.py
artifacts/plan_017/plan_017_downstream_impact.py
artifacts/plan_017/intermediate/plan_017_downstream_impact.py
figures/paper/fig_3_within_subject_matching.py
figures/paper/fig_A1_subject_heatmap.py
figures/paper/fig_A2_q3_distribution.py
artifacts/_project/data/plan_004_step1_gsm8k_temporal_dif.py
artifacts/plan_004/plan_004_step1_gsm8k_temporal_dif.py
artifacts/_project/intermediate/plan_004_step2_gsm8k_semi_synthetic.py
artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py
artifacts/_project/intermediate/plan_004_step3_gsm1k_dif_correlation.py
artifacts/plan_004/plan_004_step3_gsm1k_dif_correlation.py
figures/paper/fig_4_downstream_impact.py
figures/paper/fig_1_global_vs_differential.py
artifacts/plan_018/plan_018_threshold_sensitivity.py
artifacts/plan_018/intermediate/plan_018_threshold_sensitivity.py
artifacts/_project/data/plan_020_circularity_ablation.py
artifacts/plan_020/plan_020_circularity_ablation.py
artifacts/plan_019/plan_019_instability_decomposition.py
artifacts/plan_019/intermediate/plan_019_instability_decomposition.py
artifacts/plan_004/intermediate/plan_004_bootstrap_ci.py
artifacts/plan_010/plan_010_arch_stratified_dif.py
artifacts/plan_004/intermediate/plan_004_bootstrap_ci_fa8ab5.py
artifacts/plan_004/plan_004_bootstrap_ci.py
artifacts/_project/intermediate/plan_021_nonuniform_dif.py
artifacts/plan_021/plan_021_nonuniform_dif.py
artifacts/plan_023/intermediate/plan_023_item_characterization.py
artifacts/plan_023/plan_023_item_characterization.py
artifacts/plan_022/plan_022_model_independence.py
artifacts/plan_022/intermediate/plan_022_model_independence.py
artifacts/_project/intermediate/plan_024_within_family.py
artifacts/plan_024/plan_024_within_family.py
artifacts/_project/intermediate/bootstrap_dfpr.py
artifacts/plan_016_supplement/bootstrap_dfpr.py
artifacts/_project/intermediate/rank_shift_analysis.py
artifacts/plan_017_supplement/rank_shift_analysis.py
artifacts/plan_013_supplement/ld_dif_cross_analysis.py
artifacts/plan_026/intermediate/plan_026_constat_dif_comparison.py
artifacts/plan_026/plan_026_constat_dif_comparison.py
artifacts/plan_027_temporal_overlap/plan_027_temporal_overlap.py
artifacts/plan_030_odds_ratio/intermediate/plan_030_odds_ratio.py
artifacts/plan_030_odds_ratio/plan_030_odds_ratio.py
artifacts/plan_029_permutation_null/plan_029_permutation_null.py
artifacts/plan_028_multi_bench_dif/intermediate/plan_028_multi_bench_dif.py
artifacts/plan_028_multi_bench_dif/plan_028_multi_bench_dif.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "261579b1-6321-434a-89b1-4235870c27eb",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "7ce5a4dd-bd8c-4b0d-bd4d-2ffd4efc8e2b",
  "sourceToolAssistantUUID": "261579b1-6321-434a-89b1-4235870c27eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T11:55:43.322Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HEEZSbXgMnhUVK8qvXjVUZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ce5a4dd-bd8c-4b0d-bd4d-2ffd4efc8e2b",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfsRvZMwT7wtkhNMbTP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "455516fd-5cd8-48e2-9aa6-a0894a6a0552",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYfcMwsEhvCRUQWXNvY6pF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4996,
      "cache_read_input_tokens": 35448,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4996
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 35448,
          "cache_creation_input_tokens": 4996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4996,
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

_source line 41 · 2026-05-21T11:55:43.326Z_

<details><summary>↩ Tool result · `toolu_01HEEZSbXgMnhUVK8qvXjVUZ`</summary>

```text
File unchanged since last read. The content from the earlier Read tool_result in this conversation is still current — refer to that instead of re-reading.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "455516fd-5cd8-48e2-9aa6-a0894a6a0552",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "da56305a-a04a-49a2-aa88-c2a29c1753f1",
  "sourceToolAssistantUUID": "455516fd-5cd8-48e2-9aa6-a0894a6a0552",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-21T11:55:43.375Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01APypfBJMeB4FBCMzfs2ZLR`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da56305a-a04a-49a2-aa88-c2a29c1753f1",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfsRvZMwT7wtkhNMbTP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1850c911-4774-4d7b-8e46-55d8e7976955",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYfcMwsEhvCRUQWXNvY6pF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4996,
      "cache_read_input_tokens": 35448,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4996
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 35448,
          "cache_creation_input_tokens": 4996,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4996,
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

_source line 43 · 2026-05-21T11:55:43.389Z_

<details><summary>↩ Tool result · `toolu_01APypfBJMeB4FBCMzfs2ZLR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\\n\\n## 近期结论\\n- **plan_028_multi_bench_dif** (success): Temporal DIF (2023 vs 2024 cohort) 在 METABENCH 的 ARC, HellaSwag, WinoGrande, TruthfulQA 上均展现与 MMLU 类似的显著 C% (>15%)，证明 temporal DIF 现象跨 benchmark 泛化，不是 MMLU 特有的 artifact。所有 benchmark 的 random-split control C% < 1%。 ← 基于 plan_001_real_data_dif_mmlu\\n  [plan_028_multi_bench_summary](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/data/multi_bench_summary.csv) | [plan_028_multi_bench_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/multi_bench_dif_report.md) | [plan_028_script](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/intermediate/plan_028_multi_bench_dif.py)\\n- **plan_030_odds_ratio** (success): Logistic regression 的 odds ratio + CI 量化 accuracy change 与 DIF C flag 的关联强度。Item-level accuracy change (Model 3) 比 domain-level delta (Model 1) 提供更精确的预测。控制 item properties (difficulty + discrimination) 后，accuracy change 的 OR 反转（Simpson's paradox），说明 DIF C 主要由 item 固有属性驱动而非 accuracy shift。 ← 基于 plan_001_real_data_dif_mmlu\\n  [plan_030_odds_ratio_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_030_odds_ratio/report/odds_ratio_report.md) | [plan_030_odds_ratio_script](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_030_odds_ratio/intermediate/plan_030_odds_ratio.py)\\n- **plan_027_temporal_overlap** (success): Temporal cohort ability gap 很小 (d=-0.17)，ability-matched C% 接近 full 31.3%，确认 temporal DIF 非 ability confound 产物 ← 基于 plan_001_real_data_dif_mmlu\\n\\n## 趋势\\n成功 8 / 负向 6 / 失败 0 / 共 14\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 2024, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1850c911-4774-4d7b-8e46-55d8e7976955",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "4300fc65-77ae-40fc-9352-fe730a136fb4",
  "sourceToolAssistantUUID": "1850c911-4774-4d7b-8e46-55d8e7976955",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T11:55:46.213Z_

<details open><summary>🔧 Tool call — Read · `toolu_018cnNfN9mLLsTG97LjQJbFd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/references.bib",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4300fc65-77ae-40fc-9352-fe730a136fb4",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfstf9UCdjvoAAkQnx8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f68d7a0-55ab-4ad6-9548-2e7939039fee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSikB9BSNicDmEMyHXYxKo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1370,
      "cache_read_input_tokens": 40444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1370,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 45 · 2026-05-21T11:55:46.217Z_

<details><summary>↩ Tool result · `toolu_018cnNfN9mLLsTG97LjQJbFd`</summary>

```text
1	% ============================================================
2	% Benchmark Contamination Detection
3	% ============================================================
4	
5	@inproceedings{balloccu2024leak,
6	  title     = {Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source {LLMs}},
7	  author    = {Balloccu, Simone and Schmidtova, Patrícia and Lango, Mateusz and Dusek, Ondrej},
8	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},
9	  year      = {2024},
10	  doi       = {10.18653/v1/2024.eacl-long.5},
11	  url       = {https://arxiv.org/abs/2402.03927}
12	}
13	
14	@inproceedings{dekoninck2024constat,
15	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
16	  author    = {Dekoninck, Jasper and Mueller, Mark Niklas and Vechev, Martin},
17	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
18	  year      = {2024},
19	  url       = {https://arxiv.org/abs/2405.16281}
20	}
21	
22	@inproceedings{golchin2024timetravel,
23	  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
24	  author    = {Golchin, Shahriar and Surdeanu, Mihai},
25	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
26	  year      = {2024},
27	  url       = {https://arxiv.org/abs/2308.08493}
28	}
29	
30	@inproceedings{li2024contamination,
31	  title     = {An Open-Source Data Contamination Report for Large Language Models},
32	  author    = {Li, Yucheng and Guo, Yunhao and Guerin, Frank and Lin, Chenghua},
33	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},
34	  year      = {2024},
35	  doi       = {10.18653/v1/2024.findings-emnlp.30},
36	  url       = {https://aclanthology.org/2024.findings-emnlp.30/}
37	}
38	
39	@misc{liang2026dvd,
40	  title         = {{DVD}: Detection via Variance of Generation Distribution for Variant Contamination},
41	  author        = {Liang, Rongzhen},
42	  year          = {2026},
43	  eprint        = {2601.04895},
44	  archivePrefix = {arXiv},
45	  primaryClass  = {cs.CL},
46	  url           = {https://arxiv.org/abs/2601.04895}
47	}
48	
49	@inproceedings{shi2024mink,
50	  title     = {Detecting Pretraining Data from Large Language Models},
51	  author    = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
52	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
53	  year      = {2024},
54	  url       = {https://arxiv.org/abs/2310.16789}
55	}
56	
57	@inproceedings{tao2026selfcritique,
58	  title     = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},
59	  author    = {Tao, Yixin},
60	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
61	  year      = {2026},
62	  url       = {https://arxiv.org/abs/2510.09259}
63	}
64	
65	@inproceedings{wang2026fragility,
66	  title     = {On The Fragility of Benchmark Contamination Detection in Reasoning Models},
67	  author    = {Wang, Haonan and Li, Haoyang and Ko, Boeun and Zhang, Hongyang},
68	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
69	  year      = {2026},
70	  url       = {https://arxiv.org/abs/2510.02386}
71	}
72	
73	@misc{zhang2024gsm1k,
74	  title         = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},
75	  author        = {Zhang, Hugh},
76	  year          = {2024},
77	  eprint        = {2405.00332},
78	  archivePrefix = {arXiv},
79	  primaryClass  = {cs.CL},
80	  url           = {https://arxiv.org/abs/2405.00332}
81	}
82	
83	@misc{zhang2024minkpp,
84	  title         = {{Min-K\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
85	  author        = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},
86	  year          = {2024},
87	  eprint        = {2404.02936},
88	  archivePrefix = {arXiv},
89	  primaryClass  = {cs.CL},
90	  url           = {https://arxiv.org/abs/2404.02936}
91	}
92	
93	% ============================================================
94	% IRT Methodology & Equating
95	% ============================================================
96	
97	@inproceedings{rodriguez2021evaluation,
98	  title     = {Evaluation Examples Are Not Equally Informative: How Should That Change {NLP} Leaderboards?},
99	  author    = {Rodriguez, Pedro and Barrow, Joe and Hoyle, Alexander Miserlis and Lalor, John P. and Jia, Robin and Boyd-Graber, Jordan},
100	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f68d7a0-55ab-4ad6-9548-2e7939039fee",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "2baff032-8e1d-4964-be54-276b298ad8d7",
  "sourceToolAssistantUUID": "8f68d7a0-55ab-4ad6-9548-2e7939039fee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-21T11:55:46.855Z_

<details open><summary>🔧 Tool call — Read · `toolu_016iHePRKzDsssZdSF6tsNtk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/math_commands.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2baff032-8e1d-4964-be54-276b298ad8d7",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfstf9UCdjvoAAkQnx8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0b79eefc-bd9c-47d8-bcbc-05df49f21301",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TSikB9BSNicDmEMyHXYxKo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1370,
      "cache_read_input_tokens": 40444,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1370
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 40444,
          "cache_creation_input_tokens": 1370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1370,
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

_source line 47 · 2026-05-21T11:55:46.864Z_

<details><summary>↩ Tool result · `toolu_016iHePRKzDsssZdSF6tsNtk`</summary>

```text
1	%%%%% NEW MATH DEFINITIONS %%%%%
2	
3	\usepackage{amsmath,amsfonts,bm}
4	
5	% Mark sections of captions for referring to divisions of figures
6	\newcommand{\figleft}{{\em (Left)}}
7	\newcommand{\figcenter}{{\em (Center)}}
8	\newcommand{\figright}{{\em (Right)}}
9	\newcommand{\figtop}{{\em (Top)}}
10	\newcommand{\figbottom}{{\em (Bottom)}}
11	\newcommand{\captiona}{{\em (a)}}
12	\newcommand{\captionb}{{\em (b)}}
13	\newcommand{\captionc}{{\em (c)}}
14	\newcommand{\captiond}{{\em (d)}}
15	
16	% Highlight a newly defined term
17	\newcommand{\newterm}[1]{{\bf #1}}
18	
19	
20	% Figure reference, lower-case.
21	\def\figref#1{figure~\ref{#1}}
22	% Figure reference, capital. For start of sentence
23	\def\Figref#1{Figure~\ref{#1}}
24	\def\twofigref#1#2{figures \ref{#1} and \ref{#2}}
25	\def\quadfigref#1#2#3#4{figures \ref{#1}, \ref{#2}, \ref{#3} and \ref{#4}}
26	% Section reference, lower-case.
27	\def\secref#1{section~\ref{#1}}
28	% Section reference, capital.
29	\def\Secref#1{Section~\ref{#1}}
30	% Reference to two sections.
31	\def\twosecrefs#1#2{sections \ref{#1} and \ref{#2}}
32	% Reference to three sections.
33	\def\secrefs#1#2#3{sections \ref{#1}, \ref{#2} and \ref{#3}}
34	% Reference to an equation, lower-case.
35	\def\eqref#1{equation~\ref{#1}}
36	% Reference to an equation, upper case
37	\def\Eqref#1{Equation~\ref{#1}}
38	% A raw reference to an equation---avoid using if possible
39	\def\plaineqref#1{\ref{#1}}
40	% Reference to a chapter, lower-case.
41	\def\chapref#1{chapter~\ref{#1}}
42	% Reference to an equation, upper case.
43	\def\Chapref#1{Chapter~\ref{#1}}
44	% Reference to a range of chapters
45	\def\rangechapref#1#2{chapters\ref{#1}--\ref{#2}}
46	% Reference to an algorithm, lower-case.
47	\def\algref#1{algorithm~\ref{#1}}
48	% Reference to an algorithm, upper case.
49	\def\Algref#1{Algorithm~\ref{#1}}
50	\def\twoalgref#1#2{algorithms \ref{#1} and \ref{#2}}
51	\def\Twoalgref#1#2{Algorithms \ref{#1} and \ref{#2}}
52	% Reference to a part, lower case
53	\def\partref#1{part~\ref{#1}}
54	% Reference to a part, upper case
55	\def\Partref#1{Part~\ref{#1}}
56	\def\twopartref#1#2{parts \ref{#1} and \ref{#2}}
57	
58	\def\ceil#1{\lceil #1 \rceil}
59	\def\floor#1{\lfloor #1 \rfloor}
60	\def\1{\bm{1}}
61	\newcommand{\train}{\mathcal{D}}
62	\newcommand{\valid}{\mathcal{D_{\mathrm{valid}}}}
63	\newcommand{\test}{\mathcal{D_{\mathrm{test}}}}
64	
65	\def\eps{{\epsilon}}
66	
67	
68	% Random variables
69	\def\reta{{\textnormal{$\eta$}}}
70	\def\ra{{\textnormal{a}}}
71	\def\rb{{\textnormal{b}}}
72	\def\rc{{\textnormal{c}}}
73	\def\rd{{\textnormal{d}}}
74	\def\re{{\textnormal{e}}}
75	\def\rf{{\textnormal{f}}}
76	\def\rg{{\textnormal{g}}}
77	\def\rh{{\textnormal{h}}}
78	\def\ri{{\textnormal{i}}}
79	\def\rj{{\textnormal{j}}}
80	\def\rk{{\textnormal{k}}}
81	\def\rl{{\textnormal{l}}}
82	% rm is already a command, just don't name any random variables m
83	\def\rn{{\textnormal{n}}}
84	\def\ro{{\textnormal{o}}}
85	\def\rp{{\textnormal{p}}}
86	\def\rq{{\textnormal{q}}}
87	\def\rr{{\textnormal{r}}}
88	\def\rs{{\textnormal{s}}}
89	\def\rt{{\textnormal{t}}}
90	\def\ru{{\textnormal{u}}}
91	\def\rv{{\textnormal{v}}}
92	\def\rw{{\textnormal{w}}}
93	\def\rx{{\textnormal{x}}}
94	\def\ry{{\textnormal{y}}}
95	\def\rz{{\textnormal{z}}}
96	
97	% Random vectors
98	\def\rvepsilon{{\mathbf{\epsilon}}}
99	\def\rvtheta{{\mathbf{\theta}}}
100	\def\rva{{\mathbf{a}}}
101	\def\rvb{{\mathbf{b}}}
102	\def\rvc{{\mathbf{c}}}
103	\def\rvd{{\mathbf{d}}}
104	\def\rve{{\mathbf{e}}}
105	\def\rvf{{\mathbf{f}}}
106	\def\rvg{{\mathbf{g}}}
107	\def\rvh{{\mathbf{h}}}
108	\def\rvu{{\mathbf{i}}}
109	\def\rvj{{\mathbf{j}}}
110	\def\rvk{{\mathbf{k}}}
111	\def\rvl{{\mathbf{l}}}
112	\def\rvm{{\mathbf{m}}}
113	\def\rvn{{\mathbf{n}}}
114	\def\rvo{{\mathbf{o}}}
115	\def\rvp{{\mathbf{p}}}
116	\def\rvq{{\mathbf{q}}}
117	\def\rvr{{\mathbf{r}}}
118	\def\rvs{{\mathbf{s}}}
119	\def\rvt{{\mathbf{t}}}
120	\def\rvu{{\mathbf{u}}}
121	\def\rvv{{\mathbf{v}}}
122	\def\rvw{{\mathbf{w}}}
123	\def\rvx{{\mathbf{x}}}
124	\def\rvy{{\mathbf{y}}}
125	\def\rvz{{\mathbf{z}}}
126	
127	% Elements of random vectors
128	\def\erva{{\textnormal{a}}}
129	\def\ervb{{\textnormal{b}}}
130	\def\ervc{{\textnormal{c}}}
131	\def\ervd{{\textnormal{d}}}
132	\def\erve{{\textnormal{e}}}
133	\def\ervf{{\textnormal{f}}}
134	\def\ervg{{\textnormal{g}}}
135	\def\ervh{{\textnormal{h}}}
136	\def\ervi{{\textnormal{i}}}
137	\def\ervj{{\textnormal{j}}}
138	\def\ervk{{\textnormal{k}}}
139	\def\ervl{{\textnormal{l}}}
140	\def\ervm{{\textnormal{m}}}
141	\def\ervn{{\textnormal{n}}}
142	\def\ervo{{\textnormal{o}}}
143	\def\ervp{{\textnormal{p}}}
144	\def\ervq{{\textnormal{q}}}
145	\def\ervr{{\textnormal{r}}}
146	\def\ervs{{\textnormal{s}}}
147	\def\ervt{{\textnormal{t}}}
148	\def\ervu{{\textnormal{u}}}
149	\def\ervv{{\textnormal{v}}}
150	\def\ervw{{\textnormal{w}}}
151	\def\ervx{{\textnormal{x}}}
152	\def\ervy{{\textnormal{y}}}
153	\def\ervz{{\textnormal{z}}}
154	
155	% Random matrices
156	\def\rmA{{\mathbf{A}}}
157	\def\rmB{{\mathbf{B}}}
158	\def\rmC{{\mathbf{C}}}
159	\def\rmD{{\mathbf{D}}}
160	\def\rmE{{\mathbf{E}}}
161	\def\rmF{{\mathbf{F}}}
162	\def\rmG{{\mathbf{G}}}
163	\def\rmH{{\mathbf{H}}}
164	\def\rmI{{\mathbf{I}}}
165	\def\rmJ{{\mathbf{J}}}
166	\def\rmK{{\mathbf{K}}}
167	\def\rmL{{\mathbf{L}}}
168	\def\rmM{{\mathbf{M}}}
169	\def\rmN{{\mathbf{N}}}
170	\def\rmO{{\mathbf{O}}}
171	\def\rmP{{\mathbf{P}}}
172	\def\rmQ{{\mathbf{Q}}}
173	\def\rmR{{\mathbf{R}}}
174	\def\rmS{{\mathbf{S}}}
175	\def\rmT{{\mathbf{T}}}
176	\def\rmU{{\mathbf{U}}}
177	\def\rmV{{\mathbf{V}}}
178	\def\rmW{{\mathbf{W}}}
179	\def\rmX{{\mathbf{X}}}
180	\def\rmY{{\mathbf{Y}}}
181	\def\rmZ{{\mathbf{Z}}}
182	
183	% Elements of random matrices
184	\def\ermA{{\textnormal{A}}}
185	\def\ermB{{\textnormal{B}}}
186	\def\ermC{{\textnormal{C}}}
187	\def\ermD{{\textnormal{D}}}
188	\def\ermE{{\textnormal{E}}}
189	\def\ermF{{\textnormal{F}}}
190	\def\ermG{{\textnormal{G}}}
191	\def\ermH{{\textnormal{H}}}
192	\def\ermI{{\textnormal{I}}}
193	\def\ermJ{{\textnormal{J}}}
194	\def\ermK{{\textnormal{K}}}
195	\def\ermL{{\textnormal{L}}}
196	\def\ermM{{\textnormal{M}}}
197	\def\ermN{{\textnormal{N}}}
198	\def\ermO{{\textnormal{O}}}
199	\def\ermP{{\textnormal{P}}}
200	\def\ermQ{{\textnormal{Q}}}
201	\def\ermR{{\textnormal{R}}}
202	\def\ermS{{\textnormal{S}}}
203	\def\ermT{{\textnormal{T}}}
204	\def\ermU{{\textnormal{U}}}
205	\def\ermV{{\textnormal{V}}}
206	\def\ermW{{\textnormal{W}}}
207	\def\ermX{{\textnormal{X}}}
208	\def\ermY{{\textnormal{Y}}}
209	\def\ermZ{{\textnormal{Z}}}
210	
211	% Vectors
212	\def\vzero{{\bm{0}}}
213	\def\vone{{\bm{1}}}
214	\def\vmu{{\bm{\mu}}}
215	\def\vtheta{{\bm{\theta}}}
216	\def\va{{\bm{a}}}
217	\def\vb{{\bm{b}}}
218	\def\vc{{\bm{c}}}
219	\def\vd{{\bm{d}}}
220	\def\ve{{\bm{e}}}
221	\def\vf{{\bm{f}}}
222	\def\vg{{\bm{g}}}
223	\def\vh{{\bm{h}}}
224	\def\vi{{\bm{i}}}
225	\def\vj{{\bm{j}}}
226	\def\vk{{\bm{k}}}
227	\def\vl{{\bm{l}}}
228	\def\vm{{\bm{m}}}
229	\def\vn{{\bm{n}}}
230	\def\vo{{\bm{o}}}
231	\def\vp{{\bm{p}}}
232	\def\vq{{\bm{q}}}
233	\def\vr{{\bm{r}}}
234	\def\vs{{\bm{s}}}
235	\def\vt{{\bm{t}}}
236	\def\vu{{\bm{u}}}
237	\def\vv{{\bm{v}}}
238	\def\vw{{\bm{w}}}
239	\def\vx{{\bm{x}}}
240	\def\vy{{\bm{y}}}
241	\def\vz{{\bm{z}}}
242	
243	% Elements of vectors
244	\def\evalpha{{\alpha}}
245	\def\evbeta{{\beta}}
246	\def\evepsilon{{\epsilon}}
247	\def\evlambda{{\lambda}}
248	\def\evomega{{\omega}}
249	\def\evmu{{\mu}}
250	\def\evpsi{{\psi}}
251	\def\evsigma{{\sigma}}
252	\def\evtheta{{\theta}}
253	\def\eva{{a}}
254	\def\evb{{b}}
255	\def\evc{{c}}
256	\def\evd{{d}}
257	\def\eve{{e}}
258	\def\evf{{f}}
259	\def\evg{{g}}
260	\def\evh{{h}}
261	\def\evi{{i}}
262	\def\evj{{j}}
263	\def\evk{{k}}
264	\def\evl{{l}}
265	\def\evm{{m}}
266	\def\evn{{n}}
267	\def\evo{{o}}
268	\def\evp{{p}}
269	\def\evq{{q}}
270	\def\evr{{r}}
271	\def\evs{{s}}
272	\def\evt{{t}}
273	\def\evu{{u}}
274	\def\evv{{v}}
275	\def\evw{{w}}
276	\def\evx{{x}}
277	\def\evy{{y}}
278	\def\evz{{z}}
279	
280	% Matrix
281	\def\mA{{\bm{A}}}
282	\def\mB{{\bm{B}}}
283	\def\mC{{\bm{C}}}
284	\def\mD{{\bm{D}}}
285	\def\mE{{\bm{E}}}
286	\def\mF{{\bm{F}}}
287	\def\mG{{\bm{G}}}
288	\def\mH{{\bm{H}}}
289	\def\mI{{\bm{I}}}
290	\def\mJ{{\bm{J}}}
291	\def\mK{{\bm{K}}}
292	\def\mL{{\bm{L}}}
293	\def\mM{{\bm{M}}}
294	\def\mN{{\bm{N}}}
295	\def\mO{{\bm{O}}}
296	\def\mP{{\bm{P}}}
297	\def\mQ{{\bm{Q}}}
298	\def\mR{{\bm{R}}}
299	\def\mS{{\bm{S}}}
300	\def\mT{{\bm{T}}}
301	\def\mU{{\bm{U}}}
302	\def\mV{{\bm{V}}}
303	\def\mW{{\bm{W}}}
304	\def\mX{{\bm{X}}}
305	\def\mY{{\bm{Y}}}
306	\def\mZ{{\bm{Z}}}
307	\def\mBeta{{\bm{\beta}}}
308	\def\mPhi{{\bm{\Phi}}}
309	\def\mLambda{{\bm{\Lambda}}}
310	\def\mSigma{{\bm{\Sigma}}}
311	
312	% Tensor
313	\DeclareMathAlphabet{\mathsfit}{\encodingdefault}{\sfdefault}{m}{sl}
314	\SetMathAlphabet{\mathsfit}{bold}{\encodingdefault}{\sfdefault}{bx}{n}
315	\newcommand{\tens}[1]{\bm{\mathsfit{#1}}}
316	\def\tA{{\tens{A}}}
317	\def\tB{{\tens{B}}}
318	\def\tC{{\tens{C}}}
319	\def\tD{{\tens{D}}}
320	\def\tE{{\tens{E}}}
321	\def\tF{{\tens{F}}}
322	\def\tG{{\tens{G}}}
323	\def\tH{{\tens{H}}}
324	\def\tI{{\tens{I}}}
325	\def\tJ{{\tens{J}}}
326	\def\tK{{\tens{K}}}
327	\def\tL{{\tens{L}}}
328	\def\tM{{\tens{M}}}
329	\def\tN{{\tens{N}}}
330	\def\tO{{\tens{O}}}
331	\def\tP{{\tens{P}}}
332	\def\tQ{{\tens{Q}}}
333	\def\tR{{\tens{R}}}
334	\def\tS{{\tens{S}}}
335	\def\tT{{\tens{T}}}
336	\def\tU{{\tens{U}}}
337	\def\tV{{\tens{V}}}
338	\def\tW{{\tens{W}}}
339	\def\tX{{\tens{X}}}
340	\def\tY{{\tens{Y}}}
341	\def\tZ{{\tens{Z}}}
342	
343	
344	% Graph
345	\def\gA{{\mathcal{A}}}
346	\def\gB{{\mathcal{B}}}
347	\def\gC{{\mathcal{C}}}
348	\def\gD{{\mathcal{D}}}
349	\def\gE{{\mathcal{E}}}
350	\def\gF{{\mathcal{F}}}
351	\def\gG{{\mathcal{G}}}
352	\def\gH{{\mathcal{H}}}
353	\def\gI{{\mathcal{I}}}
354	\def\gJ{{\mathcal{J}}}
355	\def\gK{{\mathcal{K}}}
356	\def\gL{{\mathcal{L}}}
357	\def\gM{{\mathcal{M}}}
358	\def\gN{{\mathcal{N}}}
359	\def\gO{{\mathcal{O}}}
360	\def\gP{{\mathcal{P}}}
361	\def\gQ{{\mathcal{Q}}}
362	\def\gR{{\mathcal{R}}}
363	\def\gS{{\mathcal{S}}}
364	\def\gT{{\mathcal{T}}}
365	\def\gU{{\mathcal{U}}}
366	\def\gV{{\mathcal{V}}}
367	\def\gW{{\mathcal{W}}}
368	\def\gX{{\mathcal{X}}}
369	\def\gY{{\mathcal{Y}}}
370	\def\gZ{{\mathcal{Z}}}
371	
372	% Sets
373	\def\sA{{\mathbb{A}}}
374	\def\sB{{\mathbb{B}}}
375	\def\sC{{\mathbb{C}}}
376	\def\sD{{\mathbb{D}}}
377	% Don't use a set called E, because this would be the same as our symbol
378	% for expectation.
379	\def\sF{{\mathbb{F}}}
380	\def\sG{{\mathbb{G}}}
381	\def\sH{{\mathbb{H}}}
382	\def\sI{{\mathbb{I}}}
383	\def\sJ{{\mathbb{J}}}
384	\def\sK{{\mathbb{K}}}
385	\def\sL{{\mathbb{L}}}
386	\def\sM{{\mathbb{M}}}
387	\def\sN{{\mathbb{N}}}
388	\def\sO{{\mathbb{O}}}
389	\def\sP{{\mathbb{P}}}
390	\def\sQ{{\mathbb{Q}}}
391	\def\sR{{\mathbb{R}}}
392	\def\sS{{\mathbb{S}}}
393	\def\sT{{\mathbb{T}}}
394	\def\sU{{\mathbb{U}}}
395	\def\sV{{\mathbb{V}}}
396	\def\sW{{\mathbb{W}}}
397	\def\sX{{\mathbb{X}}}
398	\def\sY{{\mathbb{Y}}}
399	\def\sZ{{\mathbb{Z}}}
400	
401	% Entries of a matrix
402	\def\emLambda{{\Lambda}}
403	\def\emA{{A}}
404	\def\emB{{B}}
405	\def\emC{{C}}
406	\def\emD{{D}}
407	\def\emE{{E}}
408	\def\emF{{F}}
409	\def\emG{{G}}
410	\def\emH{{H}}
411	\def\emI{{I}}
412	\def\emJ{{J}}
413	\def\emK{{K}}
414	\def\emL{{L}}
415	\def\emM{{M}}
416	\def\emN{{N}}
417	\def\emO{{O}}
418	\def\emP{{P}}
419	\def\emQ{{Q}}
420	\def\emR{{R}}
421	\def\emS{{S}}
422	\def\emT{{T}}
423	\def\emU{{U}}
424	\def\emV{{V}}
425	\def\emW{{W}}
426	\def\emX{{X}}
427	\def\emY{{Y}}
428	\def\emZ{{Z}}
429	\def\emSigma{{\Sigma}}
430	
431	% entries of a tensor
432	% Same font as tensor, without \bm wrapper
433	\newcommand{\etens}[1]{\mathsfit{#1}}
434	\def\etLambda{{\etens{\Lambda}}}
435	\def\etA{{\etens{A}}}
436	\def\etB{{\etens{B}}}
437	\def\etC{{\etens{C}}}
438	\def\etD{{\etens{D}}}
439	\def\etE{{\etens{E}}}
440	\def\etF{{\etens{F}}}
441	\def\etG{{\etens{G}}}
442	\def\etH{{\etens{H}}}
443	\def\etI{{\etens{I}}}
444	\def\etJ{{\etens{J}}}
445	\def\etK{{\etens{K}}}
446	\def\etL{{\etens{L}}}
447	\def\etM{{\etens{M}}}
448	\def\etN{{\etens{N}}}
449	\def\etO{{\etens{O}}}
450	\def\etP{{\etens{P}}}
451	\def\etQ{{\etens{Q}}}
452	\def\etR{{\etens{R}}}
453	\def\etS{{\etens{S}}}
454	\def\etT{{\etens{T}}}
455	\def\etU{{\etens{U}}}
456	\def\etV{{\etens{V}}}
457	\def\etW{{\etens{W}}}
458	\def\etX{{\etens{X}}}
459	\def\etY{{\etens{Y}}}
460	\def\etZ{{\etens{Z}}}
461	
462	% The true underlying data generating distribution
463	\newcommand{\pdata}{p_{\rm{data}}}
464	% The empirical distribution defined by the training set
465	\newcommand{\ptrain}{\hat{p}_{\rm{data}}}
466	\newcommand{\Ptrain}{\hat{P}_{\rm{data}}}
467	% The model distribution
468	\newcommand{\pmodel}{p_{\rm{model}}}
469	\newcommand{\Pmodel}{P_{\rm{model}}}
470	\newcommand{\ptildemodel}{\tilde{p}_{\rm{model}}}
471	% Stochastic autoencoder distributions
472	\newcommand{\pencode}{p_{\rm{encoder}}}
473	\newcommand{\pdecode}{p_{\rm{decoder}}}
474	\newcommand{\precons}{p_{\rm{reconstruct}}}
475	
476	\newcommand{\laplace}{\mathrm{Laplace}} % Laplace distribution
477	
478	\newcommand{\E}{\mathbb{E}}
479	\newcommand{\Ls}{\mathcal{L}}
480	\newcommand{\R}{\mathbb{R}}
481	\newcommand{\emp}{\tilde{p}}
482	\newcommand{\lr}{\alpha}
483	\newcommand{\reg}{\lambda}
484	\newcommand{\rect}{\mathrm{rectifier}}
485	\newcommand{\softmax}{\mathrm{softmax}}
486	\newcommand{\sigmoid}{\sigma}
487	\newcommand{\softplus}{\zeta}
488	\newcommand{\KL}{D_{\mathrm{KL}}}
489	\newcommand{\Var}{\mathrm{Var}}
490	\newcommand{\standarderror}{\mathrm{SE}}
491	\newcommand{\Cov}{\mathrm{Cov}}
492	% Wolfram Mathworld says $L^2$ is for function spaces and $\ell^2$ is for vectors
493	% But then they seem to use $L^2$ for vectors throughout the site, and so does
494	% wikipedia.
495	\newcommand{\normlzero}{L^0}
496	\newcommand{\normlone}{L^1}
497	\newcommand{\normltwo}{L^2}
498	\newcommand{\normlp}{L^p}
499	\newcommand{\normmax}{L^\infty}
500	
501	\newcommand{\parents}{Pa} % See usage in notation.tex. Chosen to match Daphne's book.
502	
503	\DeclareMathOperator*{\argmax}{arg\,max}
504	\DeclareMathOperator*{\argmin}{arg\,min}
505	
506	\DeclareMathOperator{\sign}{sign}
507	\DeclareMathOperator{\Tr}{Tr}
508	\let\ab\allowbreak
509	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b79eefc-bd9c-47d8-bcbc-05df49f21301",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "3680d4a0-c51d-43c9-bf30-f855bc979ec4",
  "sourceToolAssistantUUID": "0b79eefc-bd9c-47d8-bcbc-05df49f21301",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-21T11:55:50.057Z_

Now let me look at a few key analysis scripts to assess reproducibility and methodological rigor.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3680d4a0-c51d-43c9-bf30-f855bc979ec4",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFft9hmKuFm6wxn54pZL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8311e392-b06f-4b9f-a00e-d5665a6c14f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132PLCFQrQYMQC3TK6eNcVA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9739,
      "cache_read_input_tokens": 41814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9739,
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

_source line 49 · 2026-05-21T11:55:52.411Z_

<details open><summary>🔧 Tool call — Read · `toolu_012VeMRJdfknWSuiKjmp9jtY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8311e392-b06f-4b9f-a00e-d5665a6c14f0",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFft9hmKuFm6wxn54pZL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbdb553c-8f51-455c-91f3-689248aa19cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132PLCFQrQYMQC3TK6eNcVA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9739,
      "cache_read_input_tokens": 41814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9739,
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

_source line 50 · 2026-05-21T11:55:52.417Z_

<details><summary>↩ Tool result · `toolu_012VeMRJdfknWSuiKjmp9jtY`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_001_analysis.py — METABENCH real-data MH-DIF analysis
4	
5	Runs purified Mantel-Haenszel DIF detection on MMLU binary response data with
6	two cohort definitions (temporal 2023-vs-2024, ability Q1-2 vs Q4-5), validates
7	against Li et al. contamination proxy labels, and performs within-family,
8	domain-specificity, and negative-discrimination sensitivity analyses.
9	
10	Inputs  (all in ../):
11	  response_matrix.npz          — (5227, 12508) CSR sparse, int8 binary
12	  response_matrix_index.npz    — model_names, item_ids
13	  model_metadata.csv           — cohort_temporal, cohort_accuracy_quintile, family
14	  item_metadata.csv            — subject, is_negative_disc
15	  mmlu_li2024_proxy_labels.csv — contamination_type proxy labels
16	
17	Outputs (all in ./):
18	  dif_results_temporal.csv, dif_results_ability.csv, dif_summary.csv,
19	  within_family_dif.csv, cross_analysis.csv, domain_specificity.csv,
20	  neg_disc_sensitivity.csv, plan_001_report.md
21	
22	Dependencies: numpy, scipy, pandas
23	"""
24	
25	import numpy as np
26	import pandas as pd
27	from scipy.sparse import load_npz
28	from scipy.stats import chi2 as chi2_dist, spearmanr
29	from pathlib import Path
30	import time
31	import warnings
32	
33	warnings.filterwarnings("ignore", category=RuntimeWarning)
34	
35	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
36	OUT = BASE / "plan_001"
37	OUT.mkdir(exist_ok=True)
38	
39	
40	# ════════════════════════════════════════════════════════════════════════════
41	#  DATA LOADING
42	# ════════════════════════════════════════════════════════════════════════════
43	print("=== Loading data ===")
44	mat = load_npz(BASE / "response_matrix.npz")
45	X = mat.toarray().astype(np.int16)          # (5227, 12508)
46	del mat
47	
48	idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
49	MODEL_NAMES = idx["model_names"]             # (5227,)
50	ITEM_IDS    = idx["item_ids"]                # (12508,)
51	
52	model_meta = pd.read_csv(BASE / "model_metadata.csv")
53	item_meta  = pd.read_csv(BASE / "item_metadata.csv")
54	li_labels  = pd.read_csv(BASE / "mmlu_li2024_proxy_labels.csv")
55	
56	NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}
57	N_MODELS, J = X.shape
58	print(f"  Matrix {N_MODELS}×{J}")
59	print(f"  Li annotated: {(li_labels.contamination_type != 'no_annotation').sum()}, "
60	      f"no_annotation: {(li_labels.contamination_type == 'no_annotation').sum()}")
61	
62	
63	# ════════════════════════════════════════════════════════════════════════════
64	#  MH-DIF CORE
65	# ════════════════════════════════════════════════════════════════════════════
66	def mh_dif(X_ref, X_foc, n_strata=5, col_mask=None):
67	    """
68	    Purified Mantel-Haenszel DIF for all items (or a column subset).
69	
70	    For item j the matching variable is:
71	        purified_score = total_score_across_all_columns - response_to_item_j
72	
73	    Parameters
74	    ----------
75	    X_ref, X_foc : ndarray (N_ref, J) and (N_foc, J), int, binary 0/1
76	    n_strata     : number of quantile-based score strata
77	    col_mask     : bool array (J,); True = analyse this column.  None = all.
78	
79	    Returns
80	    -------
81	    DataFrame with cols: col_idx, alpha_mh, delta_mh, se, chi2, p_value, ets_class
82	    """
83	    _Nr, Jc = X_ref.shape
84	
85	    # row-wise total scores (used for purified matching)
86	    tot_ref = X_ref.sum(axis=1).astype(np.float64)   # (N_ref,)
87	    tot_foc = X_foc.sum(axis=1).astype(np.float64)   # (N_foc,)
88	
89	    cols = np.where(col_mask)[0] if col_mask is not None else np.arange(Jc)
90	    rows = []
91	    t0 = time.time()
92	
93	    for pos, j in enumerate(cols):
94	        if pos % 2500 == 0 and pos > 0:
95	            print(f"    {pos}/{len(cols)}  ({time.time()-t0:.0f}s)")
96	
97	        # ── purified scores: exclude item j from matching variable ──
98	        s_ref = tot_ref - X_ref[:, j].astype(np.float64)
99	        s_foc = tot_foc - X_foc[:, j].astype(np.float64)
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbdb553c-8f51-455c-91f3-689248aa19cb",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "f12f6b52-4312-46da-8018-bcba55fb1c61",
  "sourceToolAssistantUUID": "dbdb553c-8f51-455c-91f3-689248aa19cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T11:55:53.359Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WU5F74ts8hbwD9D45HBrgD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f12f6b52-4312-46da-8018-bcba55fb1c61",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFft9hmKuFm6wxn54pZL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4532459c-8b8c-4aca-9164-40d3711085db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132PLCFQrQYMQC3TK6eNcVA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9739,
      "cache_read_input_tokens": 41814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9739,
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

_source line 52 · 2026-05-21T11:55:53.364Z_

<details><summary>↩ Tool result · `toolu_01WU5F74ts8hbwD9D45HBrgD`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_011_analysis.py — Semi-Synthetic DIF Validation
4	
5	Injects known differential contamination into real MMLU response data and tests
6	whether MH-DIF can detect it. Validates the DIF methodology used in plan_001.
7	
8	Three MH variants:
9	  (1) standard  — total score on 500 items minus current (same as plan_001)
10	  (2) anchor    — total score on 400 known-clean items only
11	  (3) external  — total score on full 12508-item original matrix (best matching)
12	
13	Inputs:
14	  response_matrix.npz, response_matrix_index.npz, model_metadata.csv,
15	  item_metadata.csv, mmlu_li2024_proxy_labels.csv,
16	  plan_001/dif_results_ability.csv
17	
18	Outputs (all in plan_011/):
19	  injection_results.csv, dose_response_summary.csv, per_item_results.csv,
20	  plan_011_report.md
21	"""
22	
23	import numpy as np
24	import pandas as pd
25	from scipy.sparse import load_npz
26	from scipy.stats import chi2 as chi2_dist, fisher_exact
27	from pathlib import Path
28	import time
29	import warnings
30	
31	warnings.filterwarnings("ignore", category=RuntimeWarning)
32	
33	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
34	OUT = BASE / "plan_011"
35	OUT.mkdir(exist_ok=True)
36	
37	INJECTION_PS = [0.0, 0.3, 0.5, 0.7, 1.0]
38	N_SEEDS = 5
39	N_BASELINE = 500
40	N_CONTAMINATED = 100
41	
42	
43	# ════════════════════════════════════════════════════════════════════════════
44	#  MH-DIF CORE
45	# ════════════════════════════════════════════════════════════════════════════
46	def mh_dif_subset(X_ref, X_foc, n_strata=5, anchor_cols=None,
47	                  external_scores_ref=None, external_scores_foc=None):
48	    """
49	    Purified MH-DIF for all columns.
50	
51	    Stratification source (in priority order):
52	      1. external_scores_ref/foc — precomputed ability scores (e.g. full-matrix total)
53	      2. anchor_cols — total score from specified columns only
54	      3. None — standard purified (all cols minus current)
55	    """
56	    J = X_ref.shape[1]
57	    use_external = external_scores_ref is not None
58	
59	    if not use_external:
60	        if anchor_cols is not None:
61	            tot_ref = X_ref[:, anchor_cols].sum(axis=1).astype(np.float64)
62	            tot_foc = X_foc[:, anchor_cols].sum(axis=1).astype(np.float64)
63	            anchor_set = set(anchor_cols.tolist()) if hasattr(anchor_cols, 'tolist') else set(anchor_cols)
64	        else:
65	            tot_ref = X_ref.sum(axis=1).astype(np.float64)
66	            tot_foc = X_foc.sum(axis=1).astype(np.float64)
67	            anchor_set = None
68	
69	    rows = []
70	    for j in range(J):
71	        if use_external:
72	            s_ref = external_scores_ref
73	            s_foc = external_scores_foc
74	        elif anchor_set is not None:
75	            if j in anchor_set:
76	                s_ref = tot_ref - X_ref[:, j].astype(np.float64)
77	                s_foc = tot_foc - X_foc[:, j].astype(np.float64)
78	            else:
79	                s_ref = tot_ref
80	                s_foc = tot_foc
81	        else:
82	            s_ref = tot_ref - X_ref[:, j].astype(np.float64)
83	            s_foc = tot_foc - X_foc[:, j].astype(np.float64)
84	
85	        s_all = np.concatenate([s_ref, s_foc])
86	        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
87	        if len(edges) < 2:
88	            rows.append(_nan_row(j))
89	            continue
90	        n_bins = len(edges) - 1
91	
92	        k_ref = np.digitize(s_ref, edges[1:-1])
93	        k_foc = np.digitize(s_foc, edges[1:-1])
94	
95	        R = S = 0.0
96	        sum_diff = 0.0
97	        sum_var = 0.0
98	        pr = ps_qr = qs = 0.0
99	        n_ok = 0
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4532459c-8b8c-4aca-9164-40d3711085db",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "b77f9adb-2931-4bc8-bdc4-cdcf9c83393e",
  "sourceToolAssistantUUID": "4532459c-8b8c-4aca-9164-40d3711085db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T11:55:54.091Z_

<details open><summary>🔧 Tool call — Read · `toolu_013NUoae3vDPv5SrjSFAXXUa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/plan_029_permutation_null.py",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b77f9adb-2931-4bc8-bdc4-cdcf9c83393e",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFft9hmKuFm6wxn54pZL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ee89de04-9915-49d0-bb89-a204178c60a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132PLCFQrQYMQC3TK6eNcVA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9739,
      "cache_read_input_tokens": 41814,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9739
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 340,
          "cache_read_input_tokens": 41814,
          "cache_creation_input_tokens": 9739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9739,
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

_source line 54 · 2026-05-21T11:55:54.098Z_

<details><summary>↩ Tool result · `toolu_013NUoae3vDPv5SrjSFAXXUa`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_029_permutation_null.py — Permutation null for temporal DIF C%
4	
5	Tests whether the observed ~31.3% C-category rate in temporal DIF (2023 vs 2024)
6	exceeds chance under random label assignment.  1000 permutations, keeping group
7	sizes fixed (N_ref=1080, N_foc=807).
8	
9	Key optimisation: purified scores (and hence strata) are independent of the
10	ref/foc split, so they are precomputed once.  Per-permutation work reduces to
11	two np.bincount calls per item.
12	"""
13	
14	import numpy as np
15	import pandas as pd
16	from scipy.sparse import load_npz
17	from scipy.stats import chi2 as chi2_dist
18	from pathlib import Path
19	import time
20	
21	import matplotlib
22	matplotlib.use("Agg")
23	import matplotlib.pyplot as plt
24	
25	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/"
26	            "projects/irt_equated_bench_regen/artifacts")
27	OUT = BASE / "plan_029_permutation_null"
28	OUT.mkdir(exist_ok=True)
29	
30	N_PERM = 200
31	N_STRATA = 5
32	SEED = 42
33	
34	# ═══════════════════════════════════════════════════════════════
35	#  DATA
36	# ═══════════════════════════════════════════════════════════════
37	print("Loading data...")
38	t0 = time.time()
39	
40	mat = load_npz(BASE / "response_matrix.npz")
41	X_full = mat.toarray()          # int8, (5227, 12508)
42	del mat
43	
44	idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
45	MODEL_NAMES = idx["model_names"]
46	ITEM_IDS = idx["item_ids"]
47	J = len(ITEM_IDS)
48	
49	meta = pd.read_csv(BASE / "model_metadata.csv")
50	NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}
51	
52	# Temporal subset (1887 models)
53	temporal_mask = meta["cohort_temporal"].isin(["2023", "2024"])
54	temporal_meta = meta[temporal_mask].copy()
55	temporal_rows = np.array([NAME2ROW[n] for n in temporal_meta["model_name"]
56	                          if n in NAME2ROW])
57	name2cohort = dict(zip(meta["model_name"], meta["cohort_temporal"]))
58	is_ref_true = np.array([name2cohort[MODEL_NAMES[r]] == "2023"
59	                         for r in temporal_rows])
60	
61	N_temp = len(temporal_rows)
62	N_ref = int(is_ref_true.sum())
63	N_foc = N_temp - N_ref
64	
65	X_temp = X_full[temporal_rows]   # (1887, 12508) int8
66	del X_full
67	
68	print(f"  N_temporal={N_temp}, N_ref={N_ref}, N_foc={N_foc}, J={J}")
69	print(f"  Loaded in {time.time() - t0:.1f}s")
70	
71	# ═══════════════════════════════════════════════════════════════
72	#  PRECOMPUTE STRATA  (fixed across permutations)
73	# ═══════════════════════════════════════════════════════════════
74	print("Precomputing strata...")
75	t0 = time.time()
76	
77	tot = X_temp.astype(np.float64).sum(axis=1)       # (1887,)
78	purified_all = tot[:, None] - X_temp.astype(np.float64)  # (1887, J)
79	
80	quantiles = np.linspace(0, 1, N_STRATA + 1)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee89de04-9915-49d0-bb89-a204178c60a7",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "61746c68-1543-409c-9a7b-4c8a63dd49eb",
  "sourceToolAssistantUUID": "ee89de04-9915-49d0-bb89-a204178c60a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-21T11:55:58.333Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GJ2mX7AAaho11e2ZfbAe1J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_030_odds_ratio/plan_030_odds_ratio.py",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61746c68-1543-409c-9a7b-4c8a63dd49eb",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFftgb98wMwSTL1YdLkK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1af0768c-1e4d-4df6-986d-1ea6ed8728a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LnQpGUTVanWDW9Rf3v54Qs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4524,
      "cache_read_input_tokens": 51553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4524,
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

_source line 56 · 2026-05-21T11:55:58.338Z_

<details><summary>↩ Tool result · `toolu_01GJ2mX7AAaho11e2ZfbAe1J`</summary>

```text
1	"""
2	Plan 030: Odds Ratio + CI for Accuracy-DIF Regression
3	Extends plan_019 with OR/CI, multiple pseudo R², item-level predictors.
4	"""
5	
6	import numpy as np
7	import pandas as pd
8	import scipy.sparse as sp
9	import statsmodels.api as sm
10	from scipy import stats
11	from pathlib import Path
12	
13	ROOT = Path(__file__).resolve().parent.parent
14	OUT  = Path(__file__).resolve().parent
15	
16	# ── 1. Load data (same as plan_019) ──────────────────────────────────
17	
18	dif = pd.read_csv(ROOT / "plan_001" / "dif_results_temporal.csv")
19	item_meta = pd.read_csv(ROOT / "item_metadata.csv")
20	model_meta = pd.read_csv(ROOT / "model_metadata.csv")
21	
22	idx = np.load(ROOT / "response_matrix_index.npz", allow_pickle=True)
23	model_names = idx["model_names"]
24	item_ids = idx["item_ids"]
25	
26	raw = np.load(ROOT / "response_matrix.npz", allow_pickle=True)
27	R = sp.csr_matrix((raw["data"], raw["indices"], raw["indptr"]),
28	                   shape=tuple(raw["shape"]))
29	
30	# ── 2. Cohort masks ─────────────────────────────────────────────────
31	
32	ref_mask = model_meta["cohort_temporal"] == "2023"
33	foc_mask = model_meta["cohort_temporal"] == "2024"
34	ref_idx = np.where(ref_mask.values)[0]
35	foc_idx = np.where(foc_mask.values)[0]
36	
37	item_subject = pd.Series(
38	    item_meta.set_index("item_id")["subject"].reindex(item_ids).values,
39	    index=item_ids
40	)
41	
42	# ── 3. Subject-level accuracy delta (plan_019 replication) ──────────
43	
44	def cohort_subject_accuracy(row_indices):
45	    sub = R[row_indices]
46	    n_models = len(row_indices)
47	    n_correct = np.asarray(sub.sum(axis=0)).ravel().astype(np.float64)
48	    item_acc = n_correct / n_models
49	    acc_df = pd.DataFrame({"subject": item_subject.values, "acc": item_acc})
50	    return acc_df.groupby("subject")["acc"].mean()
51	
52	ref_acc = cohort_subject_accuracy(ref_idx)
53	foc_acc = cohort_subject_accuracy(foc_idx)
54	subject_delta = (foc_acc - ref_acc).rename("subject_acc_delta")
55	
56	# ── 4. Item-level accuracy change ───────────────────────────────────
57	
58	ref_correct = np.asarray(R[ref_idx].sum(axis=0)).ravel().astype(np.float64)
59	foc_correct = np.asarray(R[foc_idx].sum(axis=0)).ravel().astype(np.float64)
60	item_acc_ref = ref_correct / len(ref_idx)
61	item_acc_foc = foc_correct / len(foc_idx)
62	item_acc_change = pd.Series(item_acc_foc - item_acc_ref, index=item_ids, name="item_acc_change")
63	
64	# ── 5. Merge everything ────────────────────────────────────────────
65	
66	df = dif.merge(item_meta[["item_id", "ctt_difficulty", "ctt_discrimination"]],
67	               on="item_id", how="left")
68	df = df.merge(subject_delta.reset_index().rename(columns={"index": "subject"}),
69	              on="subject", how="left")
70	df = df.merge(item_acc_change.reset_index().rename(columns={"index": "item_id"}),
71	              on="item_id", how="left")
72	
73	df["dif_c"] = (df["ets_class"] == "C").astype(int)
74	df = df.dropna(subset=["subject_acc_delta", "ctt_difficulty", "ctt_discrimination", "item_acc_change"])
75	
76	print(f"Analysis dataset: {len(df)} items, {df.subject.nunique()} subjects")
77	print(f"DIF C count: {df.dif_c.sum()} ({df.dif_c.mean()*100:.1f}%)")
78	print(f"Item acc change: mean={df.item_acc_change.mean():.4f}, "
79	      f"std={df.item_acc_change.std():.4f}, range=[{df.item_acc_change.min():.4f}, {df.item_acc_change.max():.4f}]")
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1af0768c-1e4d-4df6-986d-1ea6ed8728a8",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "6c28b583-1ee0-40f2-91e2-12d14b7644f0",
  "sourceToolAssistantUUID": "1af0768c-1e4d-4df6-986d-1ea6ed8728a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T11:55:58.983Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NAnXWYabox4J62tCLMR588`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/plan_028_multi_bench_dif.py",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c28b583-1ee0-40f2-91e2-12d14b7644f0",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFftgb98wMwSTL1YdLkK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa0f2d48-e977-42d8-9b62-3abd3fccf32e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LnQpGUTVanWDW9Rf3v54Qs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4524,
      "cache_read_input_tokens": 51553,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4524
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 51553,
          "cache_creation_input_tokens": 4524,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4524,
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

_source line 58 · 2026-05-21T11:55:58.988Z_

<details><summary>↩ Tool result · `toolu_01NAnXWYabox4J62tCLMR588`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_028_multi_bench_dif.py — Multi-benchmark temporal MH-DIF analysis
4	
5	Runs purified Mantel-Haenszel DIF on ARC, HellaSwag, WinoGrande, TruthfulQA
6	using the same temporal cohort split (2023 vs 2024) as the MMLU analysis.
7	GSM8K and MMLU results are referenced from prior analyses.
8	
9	Inputs:
10	  artifacts/metabench_data/benchmark-data/{arc,hellaswag,winogrande,truthfulqa}.csv
11	  artifacts/model_metadata.csv
12	
13	Outputs (in artifacts/plan_028_multi_bench_dif/):
14	  {benchmark}_dif_results.csv      — per-item DIF results
15	  {benchmark}_ets_summary.csv      — ETS summary stats
16	  multi_bench_dif_report.md        — consolidated report
17	"""
18	
19	import numpy as np
20	import pandas as pd
21	from scipy.stats import chi2 as chi2_dist
22	from pathlib import Path
23	import time
24	import warnings
25	import gc
26	
27	warnings.filterwarnings("ignore", category=RuntimeWarning)
28	
29	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
30	DATA = BASE / "metabench_data" / "benchmark-data"
31	OUT = BASE / "plan_028_multi_bench_dif"
32	OUT.mkdir(exist_ok=True)
33	
34	
35	# ════════════════════════════════════════════════════════════════════════════
36	#  MH-DIF CORE (from plan_001)
37	# ════════════════════════════════════════════════════════════════════════════
38	def mh_dif(X_ref, X_foc, n_strata=5):
39	    """
40	    Purified Mantel-Haenszel DIF for all items.
41	    X_ref, X_foc: ndarray (N_ref, J) and (N_foc, J), binary 0/1.
42	    Returns DataFrame with: col_idx, alpha_mh, delta_mh, se, chi2, p_value, ets_class
43	    """
44	    tot_ref = X_ref.sum(axis=1).astype(np.float64)
45	    tot_foc = X_foc.sum(axis=1).astype(np.float64)
46	    J = X_ref.shape[1]
47	    rows = []
48	    t0 = time.time()
49	
50	    for j in range(J):
51	        if j % 2000 == 0 and j > 0:
52	            print(f"    {j}/{J}  ({time.time()-t0:.0f}s)")
53	
54	        s_ref = tot_ref - X_ref[:, j].astype(np.float64)
55	        s_foc = tot_foc - X_foc[:, j].astype(np.float64)
56	
57	        s_all = np.concatenate([s_ref, s_foc])
58	        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
59	        if len(edges) < 2:
60	            rows.append(_nan_row(j))
61	            continue
62	        n_bins = len(edges) - 1
63	        k_ref = np.digitize(s_ref, edges[1:-1])
64	        k_foc = np.digitize(s_foc, edges[1:-1])
65	
66	        R = S = 0.0
67	        sum_diff = sum_var = 0.0
68	        pr = ps_qr = qs = 0.0
69	        n_ok = 0
70	
71	        for k in range(n_bins):
72	            mr = (k_ref == k)
73	            mf = (k_foc == k)
74	            n1 = int(mr.sum())
75	            n0 = int(mf.sum())
76	            if n1 == 0 or n0 == 0:
77	                continue
78	
79	            A = float(X_ref[mr, j].sum())
80	            B = float(n1 - A)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa0f2d48-e977-42d8-9b62-3abd3fccf32e",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "89066a86-01d0-4b43-b00a-b876a714f438",
  "sourceToolAssistantUUID": "fa0f2d48-e977-42d8-9b62-3abd3fccf32e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-21T11:56:01.832Z_

Now let me check the experiment plan for the remaining experiments referenced in the task description.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89066a86-01d0-4b43-b00a-b876a714f438",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfu3YiFm85z4d3eTc1f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f5794cf-a1b3-4a75-b88a-fd7fca10213e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3ZchXwr4ntoksm2D2xeHo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2832,
      "cache_read_input_tokens": 56077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2832,
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

_source line 60 · 2026-05-21T11:56:02.707Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XrnK45ogWJAGXv38gNvgXA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/experiment_plan.yaml",
  "offset": 200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f5794cf-a1b3-4a75-b88a-fd7fca10213e",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfu3YiFm85z4d3eTc1f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "100f3674-fa82-4d65-9e44-8fdec663312d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3ZchXwr4ntoksm2D2xeHo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2832,
      "cache_read_input_tokens": 56077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2832,
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

_source line 61 · 2026-05-21T11:56:02.715Z_

<details><summary>↩ Tool result · `toolu_01XrnK45ogWJAGXv38gNvgXA`</summary>

```text
200	
201	  - id: plan_009
202	    name: item_focused_trees
203	    claim: 1
204	    description: >
205	      Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative to
206	      categorical cohort DIF. Treat model release date as continuous covariate.
207	      Compare detection power and flexibility vs categorical DIF.
208	      Advantages: avoids arbitrary cohort splits, uses full model sample.
209	    priority: P2
210	    gpu_budget_hours: 0
211	    deps: [plan_001]
212	    registry_id: ""
213	
214	  - id: plan_010
215	    name: architecture_stratified_dif
216	    claim: 1
217	    description: >
218	      Run DIF within architecture-homogeneous subpopulations to test whether
219	      IRT model fit improves and spurious DIF reduces when architecture heterogeneity
220	      is removed. Dream worst-case identified this as the critical missing experiment.
221	      Design:
222	      (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000)
223	      (b) Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup
224	      (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR
225	          vs full-population DIF from plan_001
226	      (d) If fit improves substantially, conclusion is "DIF requires architecture-homogeneous
227	          populations" — a fixable constraint, not a fundamental limitation
228	      Zero GPU cost (uses existing METABENCH data). Proactive defense against worst-case
229	      reviewer concern about unidimensional IRT misfit.
230	    priority: P1
231	    gpu_budget_hours: 0
232	    deps: [plan_001]
233	    registry_id: ""
234	
235	  - id: plan_011
236	    name: semi_synthetic_contamination_validation
237	    claim: 1
238	    description: >
239	      Inject known contamination into the real METABENCH response matrix and measure
240	      DIF detection power under controlled ground truth. Addresses ground truth
241	      circularity concern (Li et al. proxy labels measure existence, not differential contamination).
242	      Design:
243	      (a) Select 500 items with known-clean status (no DIF flags, stable across cohorts)
244	      (b) For a random subset of 100-200 items, inject synthetic contamination:
245	          flip responses of focal-group models from incorrect→correct with probability p
246	          (simulating contamination at varying exploitation rates)
247	      (c) Run DIF detection; measure TPR/FPR against known-injected ground truth
248	      (d) Vary injection parameters: contamination prevalence (5%-30%), exploitation rate
249	          (0.4-1.0), focal group size (N=40-200)
250	      Provides controlled ground truth that proxy labels (Li et al.) and GSM1K cannot.
251	    priority: P1
252	    gpu_budget_hours: 0
253	    deps: [plan_001]
254	    registry_id: ""
255	
256	  # === Dream #6 后续补充实验 (D024) ===
257	
258	  - id: plan_028
259	    name: multi_benchmark_temporal_dif
260	    claim: 1,5
261	    description: >
262	      Check METABENCH for additional benchmark response matrices (ARC-Challenge, HellaSwag,
263	      WinoGrande, TruthfulQA, MMLU-Pro) and run temporal DIF analysis (2023 vs 2024) on each.
264	      Addresses Dream #6 three-tier consensus: "only MMLU + GSM8K, generalizability insufficient."
265	      Report C% + sample sizes + random-split control for each benchmark.
266	    priority: P0
267	    gpu_budget_hours: 0
268	    deps: [plan_001]
269	    registry_id: ""
270	
271	  - id: plan_029
272	    name: permutation_null_c_rate
273	    claim: 1
274	    description: >
275	      1000× permutation test: randomly reassign 2023/2024 temporal labels (preserving group sizes
276	      N_ref=1080, N_foc=807) and run MH-DIF each time. Establishes null distribution for C%.
277	      Dream #6 three-tier consensus: reviewers ask "is 31% above chance?" Current random-split
278	      control (0.18%) is within-cohort, not temporal permutation null.
279	    priority: P1
280	    gpu_budget_hours: 0
281	    deps: [plan_001]
282	    registry_id: ""
283	
284	  - id: plan_030
285	    name: odds_ratio_regression_transparency
286	    claim: 1
287	    description: >
288	      Supplement pseudo R²=0.0007 with odds ratio + 95% CI + McFadden/Nagelkerke R² + deviance
289	      ratio. Add finer-grained model: item-level DIF flag ~ item-level accuracy change (per-item
290	      2024-2023 accuracy delta) vs current domain-level predictor. Dream #6 two-tier concern.
291	    priority: P1
292	    gpu_budget_hours: 0
293	    deps: [plan_001]
294	    registry_id: ""
295	
296	# GPU Budget Summary:
297	# P0: 250 hours (plan_001: 0h + plan_002: 100h + plan_003a: 80h + plan_003b: 70h + plan_003c: 0h)
298	# P1: 350 hours (plan_004: 100h + plan_005: 50h + plan_006: 200h + plan_010: 0h + plan_011: 0h)
299	# P2: 0 hours (all simulation/analysis)
300	# Total: 600 hours (within 900-1200h project budget, leaving margin for reruns)
301	# Note: plan_010 (arch-stratified DIF) and plan_011 (semi-synthetic validation) added post-Dream,
302	# both 0 GPU-h (CPU-only analysis on existing METABENCH data)
303	# Claim 2 resilience: if one signal fails, 2-signal ensemble still publishable
304	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "100f3674-fa82-4d65-9e44-8fdec663312d",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "790d132b-bc77-45e8-bf45-f76b1bf10e30",
  "sourceToolAssistantUUID": "100f3674-fa82-4d65-9e44-8fdec663312d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-21T11:56:03.415Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01AmwGSMJ9iWqYDjgC25Wk1c`</summary>

```json
{
  "pattern": "artifacts/plan_*/report/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "790d132b-bc77-45e8-bf45-f76b1bf10e30",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfu3YiFm85z4d3eTc1f",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "edba4db9-c40e-472b-9a97-6e248cb0c2c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V3ZchXwr4ntoksm2D2xeHo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2832,
      "cache_read_input_tokens": 56077,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2832
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 56077,
          "cache_creation_input_tokens": 2832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2832,
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

_source line 63 · 2026-05-21T11:56:03.438Z_

<details><summary>↩ Tool result · `toolu_01AmwGSMJ9iWqYDjgC25Wk1c`</summary>

```text
artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md
artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report_00ca1f.md
artifacts/plan_001b/report/plan_001b_report.md
artifacts/plan_011_semi_synthetic_validation/report/plan_011_report_c7ae89.md
artifacts/plan_011_semi_synthetic_validation/report/plan_011_report.md
artifacts/plan_012_irt_theta_conditioning/report/plan_012_report.md
artifacts/plan_013_q3_local_independence/report/plan_013_report.md
artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report.md
artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report_fb64fc.md
artifacts/plan_017/report/plan_017_report.md
artifacts/plan_018/report/threshold_sensitivity_report.md
artifacts/plan_019/report/instability_decomposition_report.md
artifacts/plan_004/report/bootstrap_ci_report.md
artifacts/plan_004/report/bootstrap_ci_report_58f19b.md
artifacts/plan_023/report/item_characterization_report.md
artifacts/plan_022/report/model_independence_report.md
artifacts/plan_013_supplement/report/ld_dif_cross_report.md
artifacts/plan_026/report/constat_dif_comparison_report.md
artifacts/plan_030_odds_ratio/report/odds_ratio_report.md
artifacts/plan_028_multi_bench_dif/report/multi_bench_dif_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "edba4db9-c40e-472b-9a97-6e248cb0c2c2",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "dcba4d63-b7fc-4945-afb5-ae55fb74b51b",
  "sourceToolAssistantUUID": "edba4db9-c40e-472b-9a97-6e248cb0c2c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-21T11:56:08.593Z_

Let me check a few key experiment reports for the results that feed into the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcba4d63-b7fc-4945-afb5-ae55fb74b51b",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfuNS1xypnnKFXP5Vir",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e22e1a54-f921-438c-b308-4da654831f6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3LbgChMUCE17FxhyFRm33",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2397,
      "cache_read_input_tokens": 58909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2397,
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

_source line 65 · 2026-05-21T11:56:08.697Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rz2eBjsqvBAqY9Y6Z9fu2U`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e22e1a54-f921-438c-b308-4da654831f6d",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfuNS1xypnnKFXP5Vir",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65c9254f-0108-4b55-8be5-03de35a7f52d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3LbgChMUCE17FxhyFRm33",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2397,
      "cache_read_input_tokens": 58909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2397,
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

### Tool result

_source line 66 · 2026-05-21T11:56:08.705Z_

<details><summary>↩ Tool result · `toolu_01Rz2eBjsqvBAqY9Y6Z9fu2U`</summary>

```text
1	# Plan 001: METABENCH Real-Data MH-DIF Analysis
2	
3	## 1. Data & Setup
4	
5	- Response matrix: **5227 models × 12508 items** (binary, MMLU)
6	- Temporal cohort: ref = 2023 (N=1080), foc = 2024 (N=807), 5 strata
7	- Ability cohort: ref = Q1-2 (N=2092), foc = Q4-5 (N=2089), 10 strata
8	- Li et al. annotations: 9229 annotated items
9	
10	## 2. ETS Classification
11	
12	| Cohort | Filter | Items | A | B | C | %C | FPR (clean) | Enrichment |
13	|--------|--------|-------|---|---|---|----|-------------|------------|
14	| temporal | all | 12508 | 6332 | 2258 | 3918 | 31.32% | 0.3184 | 0.96 |
15	| ability | all | 12508 | 11052 | 1093 | 363 | 2.90% | 0.0269 | 1.19 |
16	| temporal | non_neg_disc | 10582 | 5327 | 1830 | 3425 | 32.37% | 0.3258 | 0.97 |
17	
18	## 3. Li et al. Proxy Validation
19	
20	| Cohort | FPR (clean) | Rate (contam) | Rate (clean) | Rate (unlabeled) | Enrichment |
21	|--------|-------------|---------------|--------------|------------------|------------|
22	| temporal | 0.3184 | 0.3070 | 0.3184 | 0.3114 | 0.96 |
23	| ability | 0.0269 | 0.0321 | 0.0269 | 0.0293 | 1.19 |
24	
25	## 4. Within-Family Analysis
26	
27	- **llama-2 vs llama-3**: A=2718, B=2118, C=7672 (61.34%)
28	- **mistral vs mixtral**: A=3905, B=3768, C=4835 (38.66%)
29	
30	### Cross-cohort vs within-family overlap
31	
32	- **llama-2_vs_llama-3**: both_C=2611, temp_only_C=1307, wf_only_C=5061
33	- **mistral_vs_mixtral**: both_C=2031, temp_only_C=1887, wf_only_C=2804
34	
35	## 5. Domain Specificity
36	
37	Spearman ρ(C_rate, Δacc) = **0.307** (p = 0.0201)
38	
39	Top 15 subjects by C rate (temporal cohort):
40	
41	| Subject | Items | C | %C | Acc 2023 | Acc 2024 | ΔAcc |
42	|---------|-------|---|-----|----------|----------|------|
43	| business_ethics | 93 | 45 | 48.4% | 0.558 | 0.612 | +0.054 |
44	| human_aging | 203 | 85 | 41.9% | 0.644 | 0.660 | +0.016 |
45	| formal_logic | 109 | 44 | 40.4% | 0.402 | 0.446 | +0.044 |
46	| high_school_microeconomics | 220 | 85 | 38.6% | 0.606 | 0.661 | +0.055 |
47	| professional_medicine | 248 | 94 | 37.9% | 0.595 | 0.630 | +0.035 |
48	| professional_law | 1331 | 498 | 37.4% | 0.438 | 0.454 | +0.016 |
49	| world_religions | 159 | 59 | 37.1% | 0.743 | 0.734 | -0.009 |
50	| professional_accounting | 242 | 89 | 36.8% | 0.462 | 0.481 | +0.019 |
51	| medical_genetics | 85 | 31 | 36.5% | 0.637 | 0.678 | +0.041 |
52	| high_school_statistics | 181 | 64 | 35.4% | 0.490 | 0.532 | +0.042 |
53	| moral_scenarios | 692 | 243 | 35.1% | 0.358 | 0.410 | +0.053 |
54	| econometrics | 103 | 36 | 35.0% | 0.425 | 0.482 | +0.057 |
55	| high_school_chemistry | 181 | 63 | 34.8% | 0.478 | 0.502 | +0.024 |
56	| college_mathematics | 72 | 25 | 34.7% | 0.357 | 0.370 | +0.013 |
57	| elementary_mathematics | 317 | 110 | 34.7% | 0.405 | 0.442 | +0.038 |
58	
59	## 6. Negative-Discrimination Sensitivity
60	
61	| Item Set | Items | C | %C |
62	|----------|-------|---|----|
63	| all | 12508 | 3918 | 31.32% |
64	| non_negative_disc | 10582 | 3425 | 32.37% |
65	| negative_disc_only | 1926 | 495 | 25.70% |
66	
67	## 7. Sanity Check
68	
69	Random half-split of 2023 cohort: **0.18% C** (expect < 5%)
70	
71	## 8. Cohort Overlap
72	
73	- Temporal C: 3918 items
74	- Ability C: 363 items
75	- Both C: 60 items
76	- Jaccard index: 0.014
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65c9254f-0108-4b55-8be5-03de35a7f52d",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "947bd7af-9235-4f2f-aff3-1ad811e991b0",
  "sourceToolAssistantUUID": "65c9254f-0108-4b55-8be5-03de35a7f52d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-21T11:56:08.799Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LfDFMu2DNY8MPHCgfRBCya`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/report/multi_bench_dif_report.md",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "947bd7af-9235-4f2f-aff3-1ad811e991b0",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfuNS1xypnnKFXP5Vir",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7f940b3d-a388-4552-b222-c42547ac8d62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3LbgChMUCE17FxhyFRm33",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2397,
      "cache_read_input_tokens": 58909,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2397
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 255,
          "cache_read_input_tokens": 58909,
          "cache_creation_input_tokens": 2397,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2397,
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

_source line 68 · 2026-05-21T11:56:08.806Z_

<details><summary>↩ Tool result · `toolu_01LfDFMu2DNY8MPHCgfRBCya`</summary>

```text
1	# Plan 028: Multi-Benchmark Temporal DIF Analysis
2	
3	## Overview
4	
5	Temporal MH-DIF analysis (2023 vs 2024 cohort) across all 6 METABENCH benchmarks.
6	Uses purified Mantel-Haenszel with 5 score strata. ETS classification:
7	- **A**: |Δ_MH| < 1.0 (negligible)
8	- **B**: 1.0 ≤ |Δ_MH| < 1.5 or |Δ_MH| ≥ 1.5 but p ≥ 0.05 (moderate)
9	- **C**: |Δ_MH| ≥ 1.5 and p < 0.05 (large, flagged)
10	
11	## Summary Table
12	
13	| Benchmark | Items | N_ref (2023) | N_foc (2024) | A | B | C | C% | Random C% | Status |
14	|-----------|-------|-------------|-------------|---|---|---|----|-----------|--------|
15	| MMLU | 12508 | 1080 | 807 | 6332 | 2258 | 3918 | 31.3% | 0.18% | PRIOR |
16	| WINOGRANDE | 1267 | 1017 | 803 | 612 | 271 | 384 | 30.3% | 0.32% | OK |
17	| TRUTHFULQA | 817 | 1080 | 807 | 398 | 176 | 243 | 29.7% | 0.37% | OK |
18	| ARC | 1172 | 1080 | 807 | 642 | 215 | 315 | 26.9% | 0.6% | OK |
19	| GSM8K | 1319 | 1017 | 804 | 825 | 245 | 249 | 18.9% | 0.3% | PRIOR |
20	| HELLASWAG | 10042 | 1080 | 807 | 6037 | 2208 | 1797 | 17.9% | 0.28% | OK |
21	
22	## Key Findings
23	
24	- **WINOGRANDE**: 30.3% items flagged as ETS-C (vs 0.32% random control, 94.7× enrichment)
25	- **TRUTHFULQA**: 29.7% items flagged as ETS-C (vs 0.37% random control, 80.3× enrichment)
26	- **ARC**: 26.9% items flagged as ETS-C (vs 0.6% random control, 44.8× enrichment)
27	- **HELLASWAG**: 17.9% items flagged as ETS-C (vs 0.28% random control, 63.9× enrichment)
28	
29	## Interpretation
30	
31	The temporal DIF signal (C% >> random C%) indicates systematic item-level 
32	performance shifts between 2023 and 2024 model cohorts, consistent with 
33	benchmark contamination or benchmark-specific training optimization.
34	
35	Random-split controls confirm that the DIF signal is not an artifact of 
36	the MH procedure or score distribution differences within a single cohort.
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f940b3d-a388-4552-b222-c42547ac8d62",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "3f624d67-550d-4f7f-85b2-e5814fcbe774",
  "sourceToolAssistantUUID": "7f940b3d-a388-4552-b222-c42547ac8d62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-21T11:56:11.646Z_

Now let me check if there are figures and the data availability situation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f624d67-550d-4f7f-85b2-e5814fcbe774",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfumYpDxUhPb9Vt11WJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf41f3be-d8b0-4967-a9c1-fbfbe860a520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwinciXeZHLKAABmC9SAng",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2860,
      "cache_read_input_tokens": 61306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2860,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 70 · 2026-05-21T11:56:12.658Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01A41ipbVAN6gkQU6HGuZ7JS`</summary>

```json
{
  "pattern": "figures/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf41f3be-d8b0-4967-a9c1-fbfbe860a520",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfumYpDxUhPb9Vt11WJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "accd229a-7614-4566-a2e9-90be5450dc20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwinciXeZHLKAABmC9SAng",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2860,
      "cache_read_input_tokens": 61306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2860,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 71 · 2026-05-21T11:56:12.695Z_

<details><summary>↩ Tool result · `toolu_01A41ipbVAN6gkQU6HGuZ7JS`</summary>

```text
figures/paper/fig_2_dose_response.pdf
figures/paper/fig_3_within_subject_matching.pdf
figures/paper/fig_A1_subject_heatmap.pdf
figures/paper/fig_A2_q3_distribution.pdf
figures/paper/fig_4_downstream_impact.pdf
figures/paper/fig_1_global_vs_differential.pdf
figures/paper/fig_5_gsm1k_dif_correlation.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "accd229a-7614-4566-a2e9-90be5450dc20",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "b18d2567-49e4-442f-b209-f216c56922ef",
  "sourceToolAssistantUUID": "accd229a-7614-4566-a2e9-90be5450dc20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-21T11:56:13.351Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01KGki9ahZegjL9Dt4T1vZbA`</summary>

```json
{
  "pattern": "artifacts/response_matrix*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b18d2567-49e4-442f-b209-f216c56922ef",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfumYpDxUhPb9Vt11WJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90774653-020f-493f-b043-3bbdd5e10d21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwinciXeZHLKAABmC9SAng",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2860,
      "cache_read_input_tokens": 61306,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2860
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 207,
          "cache_read_input_tokens": 61306,
          "cache_creation_input_tokens": 2860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2860,
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

_source line 73 · 2026-05-21T11:56:13.372Z_

<details><summary>↩ Tool result · `toolu_01KGki9ahZegjL9Dt4T1vZbA`</summary>

```text
artifacts/response_matrix.npz
artifacts/response_matrix_index.npz
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90774653-020f-493f-b043-3bbdd5e10d21",
  "isSidechain": true,
  "promptId": "534b65d5-ef76-4e51-97eb-3b56ae068e1e",
  "agentId": "a92367696a2c7802f",
  "type": "user",
  "uuid": "19acd02e-1a2b-4436-8e38-d9439dc60162",
  "sourceToolAssistantUUID": "90774653-020f-493f-b043-3bbdd5e10d21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 74 · 2026-05-21T11:57:37.209Z_

I have now read all the main sections (Abstract, Introduction, Related Work, Method, Experiments, Discussion, Conclusion, Limitations, Appendix), examined key analysis scripts, experiment plans, and result reports. Here is my review.

---

## Review: "Psychometric Instability of LLM Benchmarks: Differential Item Functioning Reveals 31% of MMLU Items Behave Differently Across Model Generations"

**Reviewer 1 — Focus: Methods and Experiments**

---

### 1. Summary

This paper applies Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis with ETS severity classification to the METABENCH response matrix (5,227 models, 12,508 MMLU items) and five additional benchmarks (27,125 total items), finding that 17.9--31.3% of items exhibit large temporal DIF between 2023 and 2024 model cohorts. The paper argues that web-overlap contamination labels are orthogonal to DIF flags (enrichment ~1.0), proposes a semi-synthetic injection framework with cross-subject matching that achieves zero false-positive inflation, and characterizes DIF as a diagnostic lens rather than a validity threat. The experimental program is extensive, with multiple structural controls, cross-benchmark replication, and a Simpson's paradox analysis confirming that item properties rather than accuracy gains drive DIF.

### 2. Strengths

- **Thorough experimental controls.** The paper systematically rules out alternative explanations with random-split sanity checks (0.18% C), ability-quintile comparisons (2.9% C), nearest-neighbor ability matching (reducing C% by only 2.4 pp), architecture homogeneity verification (99.98% decoder-only), and BH FDR correction (negligible effect). This is exemplary experimental hygiene for an empirical study.

- **Scale of analysis is unprecedented.** 5,227 models across 27,125 items on 6 benchmarks constitutes, to my knowledge, the largest DIF analysis ever conducted on LLM evaluations. The sheer volume of data lends credibility to the statistical findings and enables analyses (e.g., per-subject C% distributions, within-family DIF) that smaller datasets cannot support.

- **Cross-subject matching is a genuine methodological contribution.** The insight that within-subject matching inflates FPR by +0.186 while cross-subject matching achieves exactly zero FPR inflation is well-demonstrated and practically important. The algebraic invariance argument is sound: if scores on other subjects are used for stratification, within-subject injection cannot leak into the conditioning variable.

- **Simpson's paradox analysis (Section 4.2).** The odds ratio reversal from 1.55 to 0.73 after controlling for item difficulty and discrimination is a compelling demonstration that item-level properties, not aggregate accuracy changes, drive DIF classification. This addresses the most natural objection (that DIF simply reflects capability improvement).

- **Reproducibility.** The METABENCH data is publicly available, all analysis code uses standard libraries (numpy, scipy, pandas, statsmodels), and the paper specifies all hyperparameters (K=5 strata, ETS thresholds, injection rates, seed counts). I verified that the analysis scripts match the methodology described in the paper.

- **Honest framing of negative results.** The IRT misfit (CFI=0.68), the underpowered reasoning-RL analysis (N=13), and the exploratory status of the GSM1K correlation are all clearly acknowledged. The paper does not overstate what DIF can and cannot determine.

- **Cross-benchmark replication (Table 2).** The knowledge-vs-procedural dichotomy (C% >= 26.9% vs. <= 18.9%) is a meaningful pattern that adds interpretive value beyond "DIF exists."

### 3. Weaknesses

- **(Major) The temporal cohort split is coarse and potentially confounded by training pipeline evolution.** The binary 2023-vs-2024 split aggregates models with vastly different training procedures (base models, SFT, DPO, ORPO, etc.), data mixtures, and scales. While the paper controls for ability differences (Cohen's d = -0.17), it does not control for training methodology heterogeneity within cohorts. A model trained with DPO on curated data in 2024 is qualitatively different from a base model in 2024, yet both fall in the same "focal" group. The IFT analysis (mentioned in the task description as Table 15) is not visible in the main text; if it exists only in appendix form, the continuous-time analysis that partially addresses this concern is underemphasized. The paper acknowledges this in Limitations but does not sufficiently address how within-cohort heterogeneity might inflate or deflate DIF estimates.

- **(Major) The "instability is diagnostic, not destructive" claim requires stronger justification.** The paper reports rho = 0.997 between full and stable-item rankings, which supports the claim that aggregate rankings are preserved. However, individual model families shift by up to +793 / -542 rank positions, and 25% of models shift by >= 100. For practitioners who care about specific model comparisons (rather than population-level rank order), this is a substantial validity concern. The paper frames this as evidence that DIF is "diagnostic" but the same numbers could be framed as evidence that DIF-flagged items are introducing systematic measurement bias. The paper should more carefully distinguish when the "diagnostic" framing holds (leaderboard-level rankings) versus when it does not (pairwise model comparisons).

- **(Major) Semi-synthetic injection may not represent realistic contamination mechanisms.** The injection procedure (flipping incorrect to correct at probability p) simulates only one contamination mode: memorization of exact answers. Real contamination may involve partial knowledge (boosting probability of correct answer without certainty), systematic biases in distractor selection, or training-data-distribution effects that alter the shape of the item response function rather than just the location. The paper does not discuss how the injection model affects the validity of DELTA-TPR estimates for real-world contamination.

- **(Minor) The permutation test uses only N=200 permutations (script) but the paper references 1000 permutations.** In plan_029_permutation_null.py, N_PERM = 200 is set, while the experiment plan calls for 1000 permutations. If the reported z=189.7 is based on 200 permutations, the null distribution may not be adequately characterized (though given the extreme z-score, this is unlikely to change the conclusion). The discrepancy between plan and execution should be clarified.

- **(Minor) Number discrepancies across sections.** The abstract states "5,219 models" and the task description references this number, while the paper body consistently uses "5,227 models." The abstract also reports "12,508 items" and "DELTA-TPR = +0.508" while the body reports the same, but Table 1 in the task description references different numbers (C%=30.8 vs. 31.3 in the paper). These inconsistencies, if they exist in the final version, undermine confidence in careful reporting.

- **(Minor) The Yen's Q3 analysis dismisses local dependence concerns too quickly.** The paper reports that 11.3% of within-subject item pairs exceed |Q3| > 0.20 (a 5x ratio over cross-subject pairs). While the correlation between LD and subject-level C% is low (r=0.09), this does not rule out that LD inflates item-level DIF estimates within individual subjects. The cross-subject matching protocol addresses this for the semi-synthetic framework but not for the primary temporal DIF analysis.

- **(Minor) Missing confidence intervals on key statistics.** The headline C% = 31.3% is reported without a confidence interval. While the permutation null gives z = 189.7 (clearly significant), the point estimate itself could vary under different but reasonable cohort definitions or stratification choices. Bootstrap CIs on C% would strengthen the claim.

- **(Minor) The GSM1K correlation analysis (N=33) is underpowered and the CI is wide ([-0.71, -0.16]).** The paper appropriately labels this as exploratory, but it is still prominently discussed in the Discussion section. Given the small sample size, this evidence should be weighted less in the narrative.

### 4. Questions for Authors

1. Have you examined whether the temporal DIF signal varies when conditioning on training methodology (e.g., base vs. SFT vs. DPO) rather than calendar year? If two 2024 models with different training pipelines both show DIF on the same items, that would substantially strengthen the temporal interpretation.

2. For the semi-synthetic injection, can you characterize detection power under a partial-knowledge contamination model (e.g., boosting the probability of correct response by a fixed amount rather than flipping to correct with probability p)? This would better approximate realistic contamination.

3. The within-family analysis (Llama-2 vs. Llama-3 at 61.3% before matching, 28.3% after) is compelling but uses a family pair with a very large ability gap (d = -0.99). Are there any model family pairs with moderate ability gaps (d ~ 0.2-0.5) where you can examine whether matching still reduces C% to ~28-29%?

4. The paper reports that DIF-flagged items have higher discrimination (d = 0.230). Could the DIF signal be partly a statistical artifact of high-discrimination items being more sensitive to any distributional shift in the examinee population, even absent contamination?

5. What fraction of the 5,227 models have documented training data cutoff dates? If most model release dates are inferred from HuggingFace upload timestamps rather than actual training data cutoffs, temporal cohort assignment could be noisy.

### 5. Soundness: 3.5/5

The methodology is well-grounded in established psychometric practice (MH-DIF, ETS classification), and the experimental controls are thorough. However, three issues temper soundness: (a) the coarse temporal cohort definition introduces uncontrolled within-group heterogeneity; (b) the semi-synthetic injection model may not generalize to realistic contamination mechanisms; and (c) the "diagnostic not destructive" framing is selectively supported (aggregate rho is fine but pairwise comparisons can shift dramatically). The core finding---that ~30% of items show large DIF---is well-supported by the evidence. What that finding *means* is less firmly established.

### 6. Excitement: 3.5/5

The paper addresses a timely and practical question (can we trust cross-generation benchmark comparisons?) with a principled psychometric tool. The cross-subject matching contribution is clean and useful. The ground-truth meta-critique is an important conceptual point. However, the excitement is moderated by two factors: (a) the MH-DIF methodology is entirely standard and the paper explicitly positions itself as "not algorithmic"---this is honest but limits novelty; (b) the practical impact is unclear because the paper shows DIF-flagged items are diagnostic rather than destructive, and the audit protocol (Section 5.4) is a recommendation rather than a validated tool. The difficulty-direction interaction (rho = -0.597) is the most thought-provoking finding but receives relatively little space.

### 7. Reproducibility: 4/5

Strong. METABENCH is public, the analysis code exists and uses standard libraries, all hyperparameters are specified, and the analysis pipeline (response_matrix.npz + model_metadata.csv + item_metadata.csv) is transparent. The only deduction: the paper does not commit to releasing the analysis code, and some intermediate results (e.g., the Simpson's paradox odds ratio regression) depend on specific data processing choices that are described in prose but not fully specified in the paper text.

### 8. Overall Assessment: 3.5 (Borderline Conference)

The paper makes a solid empirical contribution: applying a well-established psychometric method at unprecedented scale to reveal a real and robust phenomenon (temporal item instability in LLM benchmarks). The experimental program is extensive, the controls are thorough, and the writing is clear and well-structured. The cross-subject matching protocol is a genuine methodological contribution for the LLM evaluation community.

However, for a Conference-level score (4.0), I would need to see: (a) more rigorous treatment of within-cohort heterogeneity, possibly through finer-grained cohort definitions or multi-level modeling; (b) validation that the semi-synthetic injection framework captures realistic contamination modes; and (c) a more nuanced treatment of when the "diagnostic not destructive" framing holds versus when it fails. The paper is currently positioned as a large-scale characterization study with a useful methodological contribution (cross-subject matching), but the interpretive framework for the findings needs strengthening.

The paper is well above the Findings threshold (3.0) due to the scale, rigor, and practical relevance of the findings. With revisions addressing the within-cohort heterogeneity and injection model concerns, it could reach Conference level.

### 9. Confidence: 4/5

I am familiar with DIF methodology from educational measurement and with the LLM benchmark evaluation literature. I have read the full paper, examined the analysis code, and verified that the reported numbers are consistent with the experimental outputs. My main uncertainty is whether the psychometric community would view the application of standard MH-DIF to LLM data as sufficiently novel, and whether the NLP community would view the practical implications as sufficiently actionable. I am confident in my assessment of the experimental methodology and statistical rigor.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19acd02e-1a2b-4436-8e38-d9439dc60162",
  "isSidechain": true,
  "agentId": "a92367696a2c7802f",
  "requestId": "req_011CbFfv6utngdZ4ox7qQrdb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ea7085d-fef7-43a3-815a-ba9f6a1b79d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "9a39fd00-8805-41a7-a4c4-e92500e754cb",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTwQ9K4KaRvYt6uvvYTD52",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 399,
      "cache_read_input_tokens": 64166,
      "output_tokens": 3197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 399
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3197,
          "cache_read_input_tokens": 64166,
          "cache_creation_input_tokens": 399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 399,
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
