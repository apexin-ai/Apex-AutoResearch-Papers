# Research conversation: You are Reviewer 1 (R1) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Wea

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ab7cf5d98411afbbc.jsonl`
- **Structured JSON:** [`fbe0cc4221972e522a56.json`](../../sessions/fb/fbe0cc4221972e522a56.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

48 recorded events

### User

_source line 1 · 2026-05-21T02:16:53.342Z_

You are Reviewer 1 (R1) for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus: **methods and experiments**.

## Paper Summary

**Title**: "Identifying Capability-Authentic Benchmark Items via Differential Item Functioning"

The paper applies Mantel-Haenszel (MH) Differential Item Functioning (DIF) analysis — a classical psychometric technique — to the METABENCH response matrix (5,219 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks. The central claim is that DIF-flagged items are "capability-authentic": they concentrate the discriminative signal that differentiates model generations.

## Key Results Reported

**Experiment 1 (Core DIF on MMLU):**
- Temporal cohort (2023 vs 2024-H1): C% = 31.3%, enrichment vs Li et al contamination labels = 0.96 (null)
- Ability quintile: C% = 2.9%
- Within-family Llama-2 vs Llama-3: C% = 61.3%
- Random split sanity: C% = 0.18%
- Domain correlation: ρ = 0.307 (p=0.02), 9.4% variance explained

**Experiment 2 (Architecture Stratification):**
- Decoder-only (N=3,400): C% = 33.1% (slightly higher than full pop 31.3%)
- IRT fit: RMSEA=0.092, CFI=0.81, TLI=0.78 — all fail standard thresholds

**Experiment 3 (GSM8K + GSM1K):**
- GSM8K temporal C% = 18.9% (vs MMLU 31.3%)
- GSM1K correlation: r = −0.478, p = 0.005, N = 33, bootstrap CI [−0.71, −0.12]
- Partial r (controlling accuracy) = −0.385
- Leave-one-out min |r| = 0.374 (one model removal cuts 22% of effect)
- Semi-synthetic on GSM8K: ΔTPR = 0.818 at p=1.0

**Experiment 4 (Semi-Synthetic Validation):**
- ΔTPR at p=0.3: 0.222; p=0.5: 0.508; p=0.7: 0.664; p=1.0: 0.674
- Cross-subject matching: ΔFPR = 0.000 (key methodological contribution)
- Standard MH FPR inflates (+0.318), cross-subject matching eliminates this

**Experiment 5 (Graceful Degradation):**
- ρ = 0.997 at 31% removal, ρ = 0.972 at 50% removal
- Reliability α drops from 0.94 to 0.88 at 50%
- Theoretical bound ρ ≥ 0.95 holds up to 38% replacement

**Experiment 6 (Item-Focused Trees):**
- IFT flagging rate: 0.34 (vs MH 0.313), overlap 78%
- Smooth positive temporal trend (coefficient mean=0.08, SD=0.15)
- 12× computational cost

**Experiment 7 (Cumulative Bayesian DIF):**
- Power improves 0.38→0.64 over 4 administrations (δ=1.0)
- FPR inflates 0.05→0.11

**Experiment 8 (RL Robustness):**
- N=13 reasoning-RL models — explicitly called "fatally underpowered"
- DIF AUROC: SFT 0.69, Alignment-RL 0.66, Reasoning-RL 0.65 (CI ±0.14)
- DeLong p=0.23, TOST p=0.34 — all non-significant

**Experiment 9 (ConStat Comparison):**
- ConStat detection: 0.41 (non-RL), 0.12 (RL)
- DIF: 0.313
- Overlap: 18% — orthogonal constructs

**Experiment 10 (DVD):**
- AUC = 0.58, bimodal detection 0.23, temperature sensitivity ±0.09
- 65 GPU-hours, 14% overlap with DIF

**Experiment 11 (Ensemble Fusion):**
- Weighted fusion AUC = 0.64, overfit gap 0.08
- DIF weight = 0.22 (lowest), ConStat = 0.51

**Experiment 12a (Bifactor IRT):**
- All fit indices fail. RMSEA=0.11, CFI=0.72, TLI=0.68
- ~25,000 parameters, 180GB RAM, 48h without convergence

**Experiment 12b (Item Generation):**
- Prompt targeting ρ=0.18, student simulation ρ=0.34 (literature claims 0.75-0.82)
- Holdout validation ρ=0.42, 180 GPU-hours

## Experiment Design Context

The review_context.yaml lists 12 imagined experiments. The paper covers all 12 (plan_001 through plan_011, plus plan_005/006 split as 12a/12b). Coverage appears complete.

## Your Task

Provide a detailed review focused on:
1. **Methodological soundness**: Is MH-DIF appropriately applied? Is the unidimensionality violation adequately addressed? Is the cross-subject matching innovation well-motivated?
2. **Experimental rigor**: Are conclusions supported by the data? Are statistical tests appropriate? Are effect sizes meaningful?
3. **Reproducibility**: Is there enough detail to reproduce?
4. **Weaknesses in methods/experiments**: List specific, actionable concerns.

Output format:
```
## R1 Review: Methods and Experiments

### Summary
(2-3 sentences)

### Strengths
(Numbered list, specific)

### Weaknesses
(Numbered list, specific, with severity: minor/moderate/major)

### Questions for Authors
(Numbered list)

### Missing Experiments or Analyses

### Preliminary Score: X/6
### Confidence: X/5
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "f47cca11-3ad8-48d6-accc-10d5d1c9b7a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T02:16:53.348Z_

```json
{
  "parentUuid": "f47cca11-3ad8-48d6-accc-10d5d1c9b7a1",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
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
  "uuid": "95670909-b99a-4f08-b480-104351086888",
  "timestamp": "2026-05-21T02:16:53.348Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T02:16:57.057Z_



I need to read the project files to understand the full paper and context before writing the review. Let me start by loading the relevant tools and reading the key files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95670909-b99a-4f08-b480-104351086888",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEujnqZ5Vb5VeHifwC5v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d5736abb-8470-469e-8bc7-45d075d50836",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMQEUG1eXtfTvXk4RLDz92",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7557,
      "cache_read_input_tokens": 8254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7557,
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

_source line 4 · 2026-05-21T02:16:58.219Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HQYPPGELV4wDkcZWX4oAAf`</summary>

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
  "parentUuid": "d5736abb-8470-469e-8bc7-45d075d50836",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEujnqZ5Vb5VeHifwC5v",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b6f2614-8607-4d88-b485-522d11766e34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMQEUG1eXtfTvXk4RLDz92",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7557,
      "cache_read_input_tokens": 8254,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7557
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 139,
          "cache_read_input_tokens": 8254,
          "cache_creation_input_tokens": 7557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7557,
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

_source line 5 · 2026-05-21T02:16:58.224Z_

<details><summary>↩ Tool result · `toolu_01HQYPPGELV4wDkcZWX4oAAf`</summary>

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
  "parentUuid": "8b6f2614-8607-4d88-b485-522d11766e34",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "0a33995a-f87a-4e5f-9daf-aca575cb22e7",
  "sourceToolAssistantUUID": "8b6f2614-8607-4d88-b485-522d11766e34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T02:17:01.431Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01Wd1Y7E2NAZe8ZnutWGwHmV`</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a33995a-f87a-4e5f-9daf-aca575cb22e7",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEuk9nPAbn7RtGuQxw85",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa8474c4-802d-4ef7-b99b-0126dc80e992",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KnN4CWHkP8GYtnf6g1PggV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 15811,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1461,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
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

_source line 7 · 2026-05-21T02:17:01.498Z_

<details><summary>↩ Tool result · `toolu_01Wd1Y7E2NAZe8ZnutWGwHmV`</summary>

```text
{"result":"# 项目 irt_equated_bench_regen 概况\n\n## 实验状态 (12 个)\n\n- **plan_004_gsm8k_cross_benchmark**: DONE (negative) — \n- **plan_017_downstream_impact**: DONE (negative) — \n- **plan_016_within_subject_semi_synthetic**: DONE (success) — \n- **plan_013_q3_local_independence**: DONE (success) — \n- **plan_015_bifactor_irt**: PREPARING (killed) — \n- **plan_014_within_subject_dif**: DONE (negative) — \n- **plan_012_irt_theta_conditioning**: DONE (negative) — \n- **plan_011_semi_synthetic_validation**: DONE (success) — \n- **plan_001b_matched_ability_dif**: DONE (negative) — \n- **plan_001_real_data_dif_mmlu**: DONE (negative) — \n- **mvp_dif_power_sim_phase2**: DONE (success) — \n- **mvp_dif_power_sim**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\n\n## 近期结论\n- **plan_004_gsm8k_cross_benchmark** (negative): GSM8K 的 temporal DIF (2023 vs 2024) 将展示与 MMLU 类似的 30-40% ETS C%，证明 temporal DIF 现象跨 benchmark 泛化。使用 METABENCH 其他 benchmarks 总分做 external matching（GSM8K 无 subject 分层），预期 baseline FPR 更可控。如果 C% 在同一量级 → DIF 作为 benchmark health diagnostic 的泛化性得到验证。 ← 基于 plan_001_real_data_dif_mmlu\n- **plan_017_downstream_impact** (negative): 移除 temporal DIF-flagged items (ETS C, ~31% of MMLU items) 后，模型跨代排名更稳定（Spearman ρ 提升），且稳定性提升显著优于随机移除相同数量 items 的 baseline。这证明 DIF 不只标记 noise，而是精确识别了 problematic items，为 DIF 作为 benchmark quality tool 提供 downstream evidence。 ← 基于 plan_001_real_data_dif_mmlu\n- **plan_016_within_subject_semi_synthetic** (success): 在 subject 内部使用 within-subject total score 做 MH 分层的 semi-synthetic injection 中，DIF 仍能检测差异性污染（ΔTPR > 0.3 at p=0.5）。这证明 DIF 方法在 subject 级别也有效，plan_014 的 38% within-subject C% 反映的是真实代际能力差异而非方法失败。 ← 基于 plan_014_within_subject_dif\n  [plan_016_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report.md) | [plan_016_dose_response](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response.csv) | [plan_016_revised_dose_response](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response_e6d86f.csv) | [plan_016_revised_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report_fb64fc.md)\n\n## 趋势\n成功 5 / 负向 6 / 失败 0 / 共 11\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\n（无服务器配置）\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa8474c4-802d-4ef7-b99b-0126dc80e992",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "ead5bbfe-9fb5-4c77-9217-44b2d34e7a50",
  "sourceToolAssistantUUID": "fa8474c4-802d-4ef7-b99b-0126dc80e992",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T02:17:01.897Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Ek1yrLJGL3sf1q5SwQB5hj`</summary>

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
  "parentUuid": "ead5bbfe-9fb5-4c77-9217-44b2d34e7a50",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEuk9nPAbn7RtGuQxw85",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2212aa29-34a6-44ee-83c3-696123aa68a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KnN4CWHkP8GYtnf6g1PggV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 15811,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1461
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 170,
          "cache_read_input_tokens": 15811,
          "cache_creation_input_tokens": 1461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1461,
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

_source line 9 · 2026-05-21T02:17:01.909Z_

<details><summary>↩ Tool result · `toolu_01Ek1yrLJGL3sf1q5SwQB5hj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- plan_015_bifactor_irt: Bifactor IRT（1 general + 57 subject-specific factors）的 general θ 分层能将 temporal cohort baseline FPR 从 31% 降至 <15%，同时在 semi-synthetic 框架下保持 TPR>0.60 at p=0.5。Bifactor 通过分离学科特异性能力和通用能力，消除 subject-level 能力差异对 MH-DIF 的混淆。（准备中）\\n\\n## 近期结论\\n- **plan_004_gsm8k_cross_benchmark** (negative): GSM8K 的 temporal DIF (2023 vs 2024) 将展示与 MMLU 类似的 30-40% ETS C%，证明 temporal DIF 现象跨 benchmark 泛化。使用 METABENCH 其他 benchmarks 总分做 external matching（GSM8K 无 subject 分层），预期 baseline FPR 更可控。如果 C% 在同一量级 → DIF 作为 benchmark health diagnostic 的泛化性得到验证。 ← 基于 plan_001_real_data_dif_mmlu\\n- **plan_017_downstream_impact** (negative): 移除 temporal DIF-flagged items (ETS C, ~31% of MMLU items) 后，模型跨代排名更稳定（Spearman ρ 提升），且稳定性提升显著优于随机移除相同数量 items 的 baseline。这证明 DIF 不只标记 noise，而是精确识别了 problematic items，为 DIF 作为 benchmark quality tool 提供 downstream evidence。 ← 基于 plan_001_real_data_dif_mmlu\\n- **plan_016_within_subject_semi_synthetic** (success): 在 subject 内部使用 within-subject total score 做 MH 分层的 semi-synthetic injection 中，DIF 仍能检测差异性污染（ΔTPR > 0.3 at p=0.5）。这证明 DIF 方法在 subject 级别也有效，plan_014 的 38% within-subject C% 反映的是真实代际能力差异而非方法失败。 ← 基于 plan_014_within_subject_dif\\n  [plan_016_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report.md) | [plan_016_dose_response](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response.csv) | [plan_016_revised_dose_response](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response_e6d86f.csv) | [plan_016_revised_report](/api/workspace-files/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report_fb64fc.md)\\n\\n## 趋势\\n成功 5 / 负向 6 / 失败 0 / 共 11\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 2009, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2212aa29-34a6-44ee-83c3-696123aa68a6",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "08a53874-103c-42f0-b97a-e8432eef4e32",
  "sourceToolAssistantUUID": "2212aa29-34a6-44ee-83c3-696123aa68a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T02:17:06.003Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XtjXmsrViv9shGtAtFTJRG`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08a53874-103c-42f0-b97a-e8432eef4e32",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEukRZQaBYJpGxaoamt7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6cceff2c-14fb-45bf-916c-f46b94fc261e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCjXG1DtY85Bddq1xYWors",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2720,
      "cache_read_input_tokens": 17272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2720,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
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

_source line 11 · 2026-05-21T02:17:06.013Z_

<details><summary>↩ Tool result · `toolu_01XtjXmsrViv9shGtAtFTJRG`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'irt_equated_bench_regen'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cceff2c-14fb-45bf-916c-f46b94fc261e",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "f7650bdf-a222-42c9-b251-b3eef401540e",
  "sourceToolAssistantUUID": "6cceff2c-14fb-45bf-916c-f46b94fc261e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T02:17:06.490Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016SVkfZgmwg7uQa2e2CFa8M`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7650bdf-a222-42c9-b251-b3eef401540e",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEukRZQaBYJpGxaoamt7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a765901-ba02-4529-802d-de30d63789a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCjXG1DtY85Bddq1xYWors",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2720,
      "cache_read_input_tokens": 17272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2720,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
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

_source line 13 · 2026-05-21T02:17:06.501Z_

<details><summary>↩ Tool result · `toolu_016SVkfZgmwg7uQa2e2CFa8M`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/memory.md\", \"content\": \"## MVP 验证关键经验 (2026-05-20)\\n\\n### D001 决策：ETS C 分类 > p-value 检验\\n- **p-value based DIF 检测在 200-item benchmark 上严重 underpowered**：BH 校正后 TPR 仅 0.04-0.07（N=50, δ=1.0）\\n- **ETS C 分类（|Δ_MH|≥1.5 + 显著性）是可行的替代**：TPR=0.68-0.85 at N≥80, δ≥1.4\\n- **AUC 一直很好（0.91-0.96）**\\n\\n### 关键操作参数\\n- N≥80/group 最低要求，N≥100 显著改善\\n- δ≥1.4 logits 可靠检测区间\\n- MH 5 层 quantile + ETS C 阈值是最佳组合\\n- Subject ≥200 items 才有足够 matching precision（<100 items baseline FPR 膨胀至 ~56%）\\n\\n## D006: plan_011 Semi-Synthetic 验证成功 ✅\\n\\n### DIF 检测差异性污染有效\\n- **External MH**: temporal ΔTPR=+0.674 (0.326→1.000), FPR 恒定 0.314\\n- **Matching variable contamination**: 20% items 注入时 standard MH FPR 0.298→0.616, anchor/external 免疫\\n- **Li et al. enrichment≈1.0 原因**: web-overlap = 全局性污染，不产生 DIF\\n\\n## D007-D010: 降低 FPR 路线全部穷尽 ⚠️\\n\\n### plan_012 θ-Conditioning 失败\\n- logit θ 与 total score 相关性 0.9986 → 单维 θ 分层 ≡ 总分分层\\n\\n### plan_014 Within-Subject 前置检查：C% = 38.1% (>25%)\\n- 5 个高 C% subjects 的 within-subject temporal C% 均 >25%（31-45%）\\n- Within vs cross-subject matching 差异仅 -2.4pp → 信号对 matching 不敏感\\n- **结论**：temporal DIF 渗透到每个 subject 内部，不是 between-subject 能力差异的伪影\\n- Bifactor 方向因此否定（D010）\\n\\n### plan_013 Q3 局部独立性：温和但存在\\n- Within-subject mean Q3 = 0.009（低于 0.20 阈值）\\n- 但 11.3% within-subject pairs |Q3|>0.20（vs 2.2% cross-subject，5x）\\n- 最严重: moral_scenarios 34.2%, world_religions 18%, marketing 17.5%\\n- 不太可能单独解释 31% FPR\\n\\n### plan_016 Within-Subject Semi-Synthetic：DIF 在 subject 内也有效 ✅\\n- Cross-subject matching FPR 完全稳定（ΔFPR=0.000），4/5 subjects ΔTPR>0.3\\n- Within-subject matching FPR 膨胀 +0.067 to +0.281（matching variable 包含注入 items）\\n- **结论**：within-subject 38% C% 是真实 temporal DIF，方法论有效\\n\\n### 综合推导：31% temporal FPR 不是 artifact\\n证伪链完整：1D θ 无效 → within-subject 仍高 → bifactor 否定 → Q3 不是主因 → **这是 genuine temporal DIF**（2023→2024 模型在特定 items 上的真实差异性表现变化）。DIF 方法有效但无法区分 contamination-DIF 和 capability-DIF。\\n\\n## D012: plan_017 Downstream Impact — DIF Items ≠ 噪声 ⚠️\\n\\n### Hypothesis 被证伪但发现更有价值\\n- **假设**: 移除 DIF items → 排名更稳定 → DIF 标记了 problematic items\\n- **实际**: DIF 移除造成 **更大** 排名扰动（z = -8 to -49σ, 21/21 条件）\\n- DIF items 是浓缩的差异化信息载体，不是噪声\\n\\n### 关键数字\\n- Full vs stable-only: ρ = 0.996-0.999（排名本身极鲁棒）\\n- DIF items 跨代准确率变化 = full benchmark 的 1.09×, stable = 0.96×\\n- Top beneficiaries: phi-3, llama-3 衍生（+700-850 rank positions）\\n- Top hurt: mistral merge/slerp 模型（-400 to -587 rank positions）\\n\\n### 对论文的启示\\n- DIF items 不是\\\"要清洗的坏题\\\"——是\\\"揭示模型代际差异的诊断工具\\\"\\n- 支持 characterization narrative > cleaning narrative\\n- \\\"Stable-only benchmark\\\" 不是\\\"更好的 benchmark\\\"，而是\\\"不同视角的 benchmark\\\"\\n\\n## plan_004: GSM8K Cross-Benchmark Validation (2026-05-21) 🔑\\n\\n### Step 1: GSM8K Temporal DIF 跨 benchmark 泛化 ✅\\n- GSM8K standard C% = 18.9%（MMLU 31.3%，同一量级）\\n- Sanity check 0.3%（通过）\\n- External matching C% = 47.4%——**非 contamination absorption**，是 construct validity gap（external benchmarks 测不同能力，控制了这些能力后 GSM8K item 行为差异更大）\\n- Standard vs external Spearman ρ = 0.926（高度一致）\\n\\n### Step 2: GSM8K Semi-Synthetic 验证 ✅\\n- Standard ΔTPR = +0.818 at p=1.0（MMLU +0.508，GSM8K 更强）\\n- External ΔTPR = +0.517\\n- GSM8K 的 DIF 对差异性污染更敏感（单域 benchmark, items 更同质）\\n\\n### Step 3: GSM1K Contamination Gap × DIF Correlation — 方向反转 ❌→🔑\\n- **r = −0.478 (p=0.005)**：contaminated 模型在 DIF-C items 上更差，非更好\\n- Partial r = −0.385 控制整体准确率后仍显著\\n- Permutation p = 0.014，robust to leave-one-out\\n- 171/249 DIF-C items α_MH < 1 → favor focal (2024) models（捕获真实代际能力提升）\\n- 78/249 DIF-C items α_MH > 1 → favor reference (2023) models\\n\\n### Step 3 核心洞察\\n- **DIF ⊥ contamination**：DIF 捕捉的 measurement anomalies 与 contamination 正交\\n- 171 个 focal-favoring DIF-C items 捕获真实代际能力提升，但 contaminated 模型在这些 items 上反而更差（r=−0.347, p=0.048）——contamination 的\\\"浅层\\\"boost 无法泛化到区分真实能力的题目\\n- **这是 characterization narrative 的强 evidence**：DIF 不标记\\\"被污染的 items\\\"，标记的是\\\"不同模型代际间行为模式不一致的 items\\\"\\n- 与 Xu et al. (2024) GSM1K 互补——他们检测 contamination，我们检测 construct-level measurement anomalies\\n\\n### α_MH 方向约定（Reviewer 修正 2026-05-21）\\n- α_MH > 1 → item 对 reference group 更容易\\n- α_MH < 1 → item 对 focal group 更容易\\n- 在 temporal cohort 中：reference = 2023, focal = 2024\\n\\n## 数据源 (2026-05-20)\\n\\n### METABENCH (Kipnis et al., ICLR 2025) ⭐\\n- GitHub: https://github.com/adkipnis/metabench\\n- Zenodo: https://zenodo.org/records/12819251 (620MB)\\n- MMLU 12,508 items, 5,219 模型\\n\\n### D002: preproc.rds diff/disc 是 CTT 不是 IRT\\n- diff = 0.75 × p_correct, disc = rpbis\\n- 实际 IRT 在 crossvalidate.R 用 mirt::mirt() slope-intercept\\n\\n### Li et al. (EMNLP 2024) Proxy Ground Truth\\n- 9,229/12,508 items 有标注（73.8%）\\n- clean 60.5% / input_and_label 33.0% / input_only 6.5%\\n- Web overlap proxy，非训练数据精确标签——全局性污染，不适合 DIF 验证\\n\", \"total_chars\": 4457, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a765901-ba02-4529-802d-de30d63789a1",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "3cbcd766-4653-44ba-990d-39ddfe9acb3d",
  "sourceToolAssistantUUID": "0a765901-ba02-4529-802d-de30d63789a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T02:17:07.446Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QdDwSPr2UuaXFSWNEyBYnF`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cbcd766-4653-44ba-990d-39ddfe9acb3d",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEukRZQaBYJpGxaoamt7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4520f330-ada4-429f-abb0-59b9d44bb4b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCjXG1DtY85Bddq1xYWors",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2720,
      "cache_read_input_tokens": 17272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2720,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
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

_source line 15 · 2026-05-21T02:17:07.465Z_

<details><summary>↩ Tool result · `toolu_01QdDwSPr2UuaXFSWNEyBYnF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper_framing.md\", \"content\": \"# Paper Framing — irt_equated_bench_regen\\n\\n## Target Venue\\n- Primary: ICLR 2027 (expected deadline ~October 2026)\\n\\n## Paper Type\\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \\\"DIF reveals benchmark structural problems,\\\" not \\\"DIF detects contamination.\\\"\\n\\n## Core Claims (4 条, 可证伪)\\n\\n**Claim 1 (Temporal Comparability Concern)**: 38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. This instability persists within every subject domain (within-subject C%=31-45%, avg 38.1%), is not a statistical artifact (random split sanity check: 0.18%), and correlates with domain-specific accuracy improvement (ρ=0.307, p=0.02). This means cross-temporal MMLU score comparisons carry uncontrolled item-level variance.\\n- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%)\\n- Honesty requirement: ρ=0.307 means \\\"item instability\\\" may mainly reflect \\\"models got better at those domains\\\" — we cannot decompose 38% into contamination vs capability improvement\\n\\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\\n- Framing: aggressive — \\\"the field's standard validation approach is fundamentally mismatched for item-level detection\\\"\\n\\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\\n\\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\\n2. **DIF items = discriminative signal carriers**: DIF removal causes significantly MORE ranking disruption than random removal (z=-8 to -49σ, 21/21 conditions). DIF items carry 1.09× cross-cohort accuracy swing vs 0.96× for stable items — they concentrate the information that differentiates model generations.\\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \\\"find bad items and remove\\\" but \\\"understand what changed and why.\\\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.\\n4. **Cross-benchmark validation — DIF captures capability, not contamination**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005; partial r=−0.385 controlling accuracy; permutation p=0.014). Contaminated models (high GSM8K-GSM1K gap: Phi, Gemma families) perform WORSE on DIF items. DIF captures genuine capability-discriminative items that contamination cannot fake — contamination produces shallow performance gains concentrated on non-DIF items. N=33 matched models, leave-one-out robust (min |r|=0.374).\\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_004 Step 3 (r=−0.478, p=0.005, 33 models)\\n- Growing Pains互补: \\\"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\\\" — mutual value positioning\\n- Caveats (→ limitations): super-family analysis limited to N≥20 families; GSM1K validation N=33 (CI wide); contamination gap is proxy, not ground truth\\n\\n## Story Spine\\n\\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \\\"Model B outperforms Model A on MMLU,\\\" we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.\\n\\n**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\\n\\n**What we find**: Three discoveries, each a contribution:\\n\\n1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.\\n\\n2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.\\n\\n3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.\\n\\n4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K confirms: DIF flags anti-correlate with contamination (r=−0.478, p=0.005) — contaminated models can't fake performance on DIF items, which capture genuine capability differences. DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.\\n\\n**Headline result**: \\\"Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF flags anti-correlate with contamination (r=−0.478, p=0.005): DIF captures genuine capability-discriminative items that contamination cannot replicate. We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000).\\\"\\n\\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\\n\\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\\n\\n## Venue Fit\\n\\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\\n- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 38% instability, (2) the ground truth meta-critique affecting the field, (3) the semi-synthetic framework. Frame as \\\"bringing mature psychometric tools to characterize an urgent ML evaluation problem.\\\"\\n\\n## Anticipated Reviewer Concerns (updated for pivot)\\n\\n1. **\\\"38% could just mean models got better\\\"** — Yes, partially. ρ=0.307 confirms correlation. We discuss this honestly. The contribution is the finding itself: benchmarks have massive item-level behavioral drift, regardless of cause.\\n\\n2. **\\\"Ground truth critique is obvious — of course web labels don't capture differential effects\\\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\\n\\n3. **\\\"Semi-synthetic injection is artificial\\\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\\n\\n4. **\\\"DIF power is only sufficient for large effects\\\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\\n\\n5. **\\\"Only validated on MMLU\\\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\\n\\n6. **\\\"Higher methods (MIMIC, propensity-score) could solve the confounding\\\"** — Acknowledged as future work. We frame our three-attempt negative results as \\\"empirical observation\\\" that motivates these directions, not as impossibility.\\n\\n## Dropped from Original Framing\\n\\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\\n- **Detection as primary contribution**: Pivoted from \\\"we detect contamination\\\" to \\\"we characterize benchmark properties.\\\"\\n\", \"total_chars\": 11796, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4520f330-ada4-429f-abb0-59b9d44bb4b0",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "2fc9e0ea-8690-4726-9920-42a50b33b88c",
  "sourceToolAssistantUUID": "4520f330-ada4-429f-abb0-59b9d44bb4b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T02:17:08.061Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Gcgtc7qrJbmZK99TWKjCnb`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fc9e0ea-8690-4726-9920-42a50b33b88c",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEukRZQaBYJpGxaoamt7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a4b58d0-e819-4e45-8005-7fb93858fb5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCjXG1DtY85Bddq1xYWors",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2720,
      "cache_read_input_tokens": 17272,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2720
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 396,
          "cache_read_input_tokens": 17272,
          "cache_creation_input_tokens": 2720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2720,
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

_source line 17 · 2026-05-21T02:17:08.077Z_

<details><summary>↩ Tool result · `toolu_01Gcgtc7qrJbmZK99TWKjCnb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/decisions.yaml\", \"content\": \"_next_id: 15\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:50 UTC\\n  summary: MVP DIF 检测采用 ETS C 分类（效应量+显著性双阈值）替代 BH 校正 p 值作为主判定标准\\n  rationale: Monte Carlo 模拟显示 BH 校正在 200 items 场景下将 TPR 压缩 40-60%，所有核心条件均 FAIL/GRAY。但\\n    ETS C 分类（|Δ_MH|≥1.5 + 显著性，教育测量 gold standard）在 N≥80, δ≥1.4 时 TPR=0.72-0.85, FPR<0.05，满足\\n    pass criteria。ETS C 是 DIF 领域标准实践（Holland & Thayer 1988），使用效应量阈值比纯 p 值更稳健。操作点 N≥80,\\n    δ≥1.4 与 GSM1K 文档的重度污染效应量吻合。小效应由 ensemble 其他信号覆盖。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'BH-corrected: all FAIL/GRAY; ETS C: PASS at N≥80,δ≥1.4 (TPR=0.72-0.85,\\n      FPR<0.05)'\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:31 UTC\\n  summary: MVP 通过：DIF+ETS C 在 N≥80,δ≥1.4 下功效达标，推荐 N≥100 为主操作点\\n  rationale: Phase 1 合成参数 + Phase 2 真实参数（PSN-IRT）均验证 ETS C TPR≥0.65 at N≥80,δ≥1.4。Phase\\n    2 比 Phase 1 降低 3-6pp 符合预期。N=80,δ=1.4 裕度仅 0.032，推荐 N≥100 为主 claim。数据源为 PSN-IRT\\n    而非 ROADMAP 指定的 METABENCH，research 阶段需用 METABENCH 补充验证。限制：δ<1.0 需 ensemble 其他信号。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'Phase 1 conditional pass: ETS C TPR=0.72-0.85 at N≥80,δ≥1.4'\\n  - exp_id: mvp_dif_power_sim_phase2\\n    role: evidence\\n    result: 'Phase 2 pass: ETS C TPR=0.68-0.80 at N≥80,δ≥1.4 with real MMLU params'\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 20:49 UTC\\n  summary: 'Dream analysis (dream_20260520T194223): 6 confirmed actions from cross-tier\\n    synthesis, 2 new experiments added (plan_010/011), framing qualified'\\n  rationale: 'Dream scores met thresholds (best=4/6, median=3.5/6, worst=3/6). Cross-tier\\n    analysis identified 6 confirmed issues (≥2 tiers): (1) contamination-capability\\n    confound → within-family analysis added to plan_001; (2) RL evidence underpowered\\n    → bootstrap CIs + equivalence testing added to plan_002; (3) partial exploitation\\n    gap → power analysis added to plan_002; (4) ground truth circularity → plan_011\\n    semi-synthetic validation added; (5) related work thin → Paper Agent writing-phase\\n    task; (6) Growing Pains differentiation → Paper Agent task. Additionally: plan_010\\n    architecture-stratified DIF added as P1 proactive defense from worst-case; novelty\\n    claim qualified from \\\"first self-healing benchmark\\\" to \\\"psychometric monitoring\\n    framework\\\". Re-dream required before P0 approval.'\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-20 21:14 UTC\\n  summary: plan_001 temporal cohort DIF 证伪（enrichment=0.96），根因是 impact vs DIF 混淆。批准\\n    matched-ability DIF 作为方法改进方向 1\\n  rationale: Temporal cohort MH-DIF 标记 31.3% items 为 ETS C，但 enrichment=0.96（clean\\n    和 contaminated 标记概率相同）—— DIF 检测的是系统性能力提升而非污染。Within-family (Llama-2 vs Llama-3)\\n    61.3% C 进一步证实。这是经典 impact vs DIF 混淆（Dream D2 预测过）。但 ability-quintile enrichment=1.19\\n    + FPR=2.7% 表明信号存在但弱。方向1 matched-ability temporal DIF 在 quintile 内做时间对比，是最快验证能力匹配能否放大信号的路径。方向2\\n    IRT equating 并行准备作为 fallback。\\n  related_experiments:\\n  - exp_id: plan_001_real_data_dif_mmlu\\n    role: evidence\\n    result: negative - temporal cohort enrichment 0.96, ability quintile enrichment\\n      1.19\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-20 21:24 UTC\\n  summary: 方向 1 (matched-ability DIF) 失败确认，所有 quintile enrichment 0.94-1.04。plan_011\\n    是唯一决定性实验\\n  rationale: Quintile 内 temporal DIF 仍 enrichment≈1.0，ability matching 未能分离污染信号。但\\n    Reviewer 指出关键洞察：Li et al. web-overlap 是全局性污染（Common Crawl 对所有模型可用），不应产生 group-specific\\n    DIF。enrichment≈1.0 可能是 ground truth 不匹配而非方法失败。plan_011 注入的是已知差异性污染（仅 focal group），是唯一能区分\\\"DIF\\n    不 work\\\"和\\\"ground truth 不对\\\"的实验。方向 2 (IRT θ-matching) 如果问题出在 ground truth 也无法解决。\\n  related_experiments:\\n  - exp_id: plan_001b_matched_ability_dif\\n    role: evidence\\n    result: negative - all quintiles enrichment 0.94-1.04\\n  depends_on:\\n  - D004\\n- id: D006\\n  date: 2026-05-20 21:56 UTC\\n  summary: 'plan_011 positive: MH-DIF 检测差异性污染有效 (p=0.5 TPR=0.834, p=1.0 TPR=1.0)，但\\n    baseline FPR=31% 需 IRT θ-conditioning 降低。启动方向 2'\\n  rationale: Semi-synthetic validation 确认 DIF 能检测差异性污染（剂量-响应单调，Fisher p<1e-21）。plan_001/001b\\n    失败归因于 Li et al. web-overlap 是全局性标注，不产生 group-specific DIF。但 baseline FPR=31% (temporal)\\n    / 49% (ability) 意味着 DIF 是筛查工具（高召回、中等精度），不是确诊工具。Precision ~44% at p=1.0。两个推进方向：(1)\\n    IRT θ-conditioning 降低 baseline FPR (方向 2)，(2) Ensemble 信号 (Claim 2) 过滤假阳性——DIF\\n    高召回 + ConStat 高精度自然衔接。同时需 Yen's Q3 诊断局部独立性（审稿 WC4），局部依赖可能是 FPR 膨胀的部分原因。\\n  related_experiments:\\n  - exp_id: plan_011_semi_synthetic\\n    role: evidence\\n    result: positive - TPR 0.834 at p=0.5, 1.0 at p=1.0; but baseline FPR 0.314\\n  depends_on:\\n  - D005\\n- id: D007\\n  date: 2026-05-20 21:58 UTC\\n  summary: 'Story pivot: semi-synthetic validation 作为核心效度证据，Li et al. enrichment≈1.0\\n    重新定位为\\\"全局 vs 差异性污染\\\"的发现。IRT θ-conditioning 继续（降 FPR），但不期望改善 Li enrichment'\\n  rationale: 'Agent 和 Reviewer 均指出：即使 IRT θ 完美控制能力，Li et al. web-overlap 仍是全局标注，enrichment\\n    仍≈1.0。plan_011 semi-synthetic (ΔTPR=+0.674, Fisher p<1e-42) 是 DIF 方法有效性的决定性证据。Li\\n    et al. enrichment≈1.0 不是方法失败，而是揭示了现有\\\"污染标注\\\"实际测量的是全局 web 曝光（所有模型共享），不是差异性训练数据包含。这是一个有价值的发现：DIF\\n    检测差异性污染，现有标签标注存在性污染，两者度量不同。Story: DIF 是差异性污染的高灵敏度筛查工具 + ensemble 提升精度 + 全局/差异性污染区分是方法论贡献。'\\n  related_experiments:\\n  - exp_id: plan_011_semi_synthetic\\n    role: evidence\\n    result: positive\\n  - exp_id: plan_001_real_data_dif_mmlu\\n    role: evidence\\n    result: negative - reinterpreted as ground truth mismatch\\n  - exp_id: plan_001b_matched_ability_dif\\n    role: evidence\\n    result: negative - reinterpreted as ground truth mismatch\\n  depends_on:\\n  - D006\\n- id: D008\\n  date: 2026-05-20 22:12 UTC\\n  summary: 方向 2 (IRT θ-conditioning) 失败，1D 路线穷尽。plan_011 ability cohort TPR 修正（76%→21%，73%\\n    是能力混淆）。启动 plan_005 bifactor IRT 作为最后结构性改进\\n  rationale: logit(p) 与 total score 相关 0.9986，所有 θ 变体 FPR 31-35%。plan_011 ability\\n    cohort 在 θ 10/20-bin conditioning 下 TPR 从 76% 降到 21%（p=0.5）——原 5-bin 分层不足以消除 Q1-2\\n    vs Q4-5 极端能力差异。DIF 面临 TPR-FPR tradeoff：temporal 高 TPR 但 FPR=31%，ability (proper)\\n    低 FPR=8% 但 TPR=21%。根因：temporal cohort 间差异是多维的（不同学科能力提升不均匀），1D θ 无法捕获。Bifactor\\n    model (general + 57 subject factors) 是唯一能吸收学科级差异的结构性方法。已尝试 2 种不同类型改进方向，bifactor\\n    是第 3 种。计算量大（5227×12508×58 factors），可能需要服务器。\\n  related_experiments:\\n  - exp_id: plan_012_irt_theta_conditioning\\n    role: evidence\\n    result: negative - temporal FPR stuck at 31%, ability TPR corrected to 21%\\n  depends_on:\\n  - D007\\n- id: D009\\n  date: 2026-05-20 22:17 UTC\\n  summary: 'Dream #2 分析：best=3/6, median=3-4/6, worst=3/6。跨档一致：impact-vs-DIF confound\\n    为首要问题，bifactor 是正确方向。新发现：ensemble 不优于 DIF alone、SIBTEST/MIMIC 未尝试、detection trilemma\\n    概念'\\n  rationale: 三档审稿一致认为 within-family confound (42-62% overlap) 是最致命问题——没有 bifactor\\n    分离学科级能力差异，DIF flags 的可解释性无法建立。worst case 新增 SIBTEST/MIMIC 作为 established impact-vs-DIF\\n    solutions 的替代方案需要考虑。median 指出 ensemble AUROC (0.72) 低于 DIF alone (0.76)，Claim\\n    2 需要重新评估。worst case 提出 detection trilemma (IRT fit ↔ power ↔ confound control)\\n    作为潜在概念贡献。行动：(1) 优先完成 bifactor，(2) 考虑 SIBTEST/MIMIC 作为备选，(3) 推迟 ensemble 设计到 bifactor\\n    结果出来后，(4) 补充 impact-vs-DIF 文献\\n  related_experiments:\\n  - exp_id: dream_20260520T205007\\n    role: dream_simulation\\n    result: best=3/6, median=3-4/6, worst=3/6\\n  depends_on:\\n  - D008\\n  - D007\\n  - D006\\n- id: D010\\n  date: 2026-05-20 22:29 UTC\\n  summary: 方向 3 (Bifactor) pre-check 否定：within-subject temporal C%=38.1% (range 31-45%)，高于\\n    overall 31%。Bifactor 移除的 between-subject variance 反而在压低 C%。三种结构性改进方向全部失败，Method→Analysis\\n    pivot 前提 (a)(b) 已满足\\n  rationale: 'plan_014 within-subject DIF 前置检查：5 个 subject 的 within-subject temporal\\n    C% 平均 38.1%，没有一个低于 30%。Cross-subject matching 仅 Δ=-2.4pp。这证明 temporal DIF 是 item-specific\\n    的真实差异（能力提升+污染+其他），不是 matching artifact。Bifactor 即使完美运行也无法降 FPR 到 15% 以下。决策链：D005(方向1失败)\\n    → D008(方向2失败) → D010(方向3 pre-mortem 证伪)。Oracle: plan_011 semi-synthetic ΔTPR=+0.508\\n    确认方法本身有效。Pivot 前提 (c) 待用户确认投稿目标调整。'\\n  related_experiments:\\n  - exp_id: plan_014_within_subject_dif\\n    role: pre-check\\n    result: within-subject C%=38.1%, bifactor not viable\\n  - exp_id: plan_011_semi_synthetic\\n    role: oracle\\n    result: ΔTPR=+0.508, method works for differential contamination\\n  depends_on:\\n  - D008\\n  - D009\\n  - D005\\n- id: D011\\n  date: 2026-05-20 23:23 UTC\\n  summary: Pivot 拍板：从\\\"DIF 检测方法\\\"转向\\\"LLM benchmark psychometric characterization + DIF\\n    methodology\\\"。Cross-subject matching ΔFPR=0.000 是方法论突破，31-38% temporal DIF 是实证发现。保持\\n    ICLR 2027 目标不降级\\n  rationale: 三种结构性改进全部穷尽（D005/D008/D010），oracle 确认方法有效（plan_011 ΔTPR=+0.508）。但 pivot\\n    不等于降级：(1) cross-subject matching ΔFPR=0.000 是干净的方法论贡献——解决了 matching variable contamination\\n    这个 MH-DIF 领域的实际问题；(2) 31-38% temporal DIF 是首次大规模量化 LLM benchmark item instability；(3)\\n    global vs differential contamination 区分是概念贡献；(4) semi-synthetic validation framework\\n    可独立复用；(5) detection trilemma 是 characterization 贡献。这些组合起来是 ICLR 级别的 empirical\\n    findings paper，不需要降到 findings track。用户批评\\\"等我点头\\\"正确——这是 PI 的决策责任。\\n  related_experiments:\\n  - exp_id: plan_016_within_subject_semi_synthetic\\n    role: final_validation\\n    result: cross-subject ΔFPR=0.000, 4/5 ΔTPR>0.3\\n  - exp_id: plan_014_within_subject_dif\\n    role: pre-check\\n    result: within-subject C%=38.1%\\n  - exp_id: plan_011_semi_synthetic\\n    role: oracle\\n    result: ΔTPR=+0.508\\n  depends_on:\\n  - D010\\n  - D009\\n  - D006\\n- id: D012\\n  date: 2026-05-20 23:28 UTC\\n  summary: Story 定稿：Candidate 1 (benchmark quality tool) + ground truth meta-critique\\n    + semi-synthetic infrastructure。降级 cross-subject matching 为 recommendation（非 breakthrough）。新增\\n    downstream impact 实验（移除 DIF items → ranking stability）作为 ICLR 关键补充\\n  rationale: Reviewer 评估：(1) 三候选中 Candidate 1 最自洽，(2) cross-subject matching 是 external\\n    matching 的自然推广非新方法（降级），(3) enrichment≈1.0 + semi-synthetic positive 证明现有污染 ground\\n    truth 自身有缺陷（meta-contribution），(4) \\\"so what?\\\" 缺口是 ICLR vs findings track 的分水岭——需\\n    downstream impact 实验回答。38% 与 domain specificity ρ=0.307 的关系必须在 limitations 诚实讨论。\\n  related_experiments:\\n  - exp_id: plan_014_within_subject_dif\\n    role: finding\\n    result: 38% temporal DIF\\n  - exp_id: plan_016_within_subject_semi_synthetic\\n    role: method\\n    result: cross-subject ΔFPR=0.000\\n  - exp_id: plan_001_real_data_dif_mmlu\\n    role: finding\\n    result: enrichment≈1.0 → ground truth meta-critique\\n  depends_on:\\n  - D011\\n- id: D013\\n  date: 2026-05-21 00:06 UTC\\n  summary: plan_017 downstream impact negative 但 informative：DIF items 是浓缩差异化信号载体而非噪声。Claim\\n    4 从 placeholder \\\"remove for stability\\\" 转为 finding \\\"DIF as diagnostic lens\\\"。DIF\\n    items 移除造成更大排名扰动（21/21 条件显著），phi-3/llama-3 获益最多，mistral merge 被压制\\n  rationale: plan_017 全面证伪了\\\"移除 DIF items 改善排名稳定性\\\"的 hypothesis：(1) full vs stable-only\\n    ρ=0.996-0.999 说明排名本身极鲁棒，(2) DIF removal 扰动显著大于 random removal（z=-8 to -49σ），(3)\\n    DIF items 的跨代准确率变化是 full benchmark 的 1.09×。这意味着 DIF items 不是\\\"坏题\\\"而是\\\"模型代际差异的诊断标记\\\"。对\\n    paper narrative 的影响：从\\\"remove unstable items\\\"转向\\\"DIF as diagnostic lens for understanding\\n    model evolution\\\"。这个 negative result 比 positive 更有深度——\\\"keep these items, they tell\\n    you something\\\" 是更有价值的 benchmark design recommendation。\\n  related_experiments:\\n  - exp_id: plan_017_downstream_impact\\n    role: hypothesis_test\\n    result: negative - DIF items carry MORE discriminative signal, not less\\n  depends_on:\\n  - D012\\n  - D011\\n- id: D014\\n  date: 2026-05-21 01:25 UTC\\n  summary: 'plan_004 Step 3 GSM1K: |r|=0.478 显著但方向为负——DIF 不标记 contamination，而是标记 contamination\\n    无法到达的 capability-discriminative items'\\n  rationale: r=−0.478 (p=0.005), Spearman ρ=−0.403 (p=0.020), partial r=−0.385 (p=0.027\\n    控制 overall accuracy), permutation p=0.014, leave-one-out robust (min |r|=0.374)。N=33\\n    matched models。171 个 focal-favoring DIF-C items 驱动负相关 (r=−0.347, p=0.048)：contaminated\\n    models 在这些 genuine capability improvement items 上表现更差。这不支持 \\\"DIF = contamination\\n    detector\\\" 假设，但强力支撑 pivot 后 \\\"DIF as diagnostic lens\\\" 叙事：DIF 捕获的是真实能力差异，contamination\\n    产生的浅层提升无法到达这些 items。与 plan_017 (DIF items = discriminative signal carriers) 形成双重验证。不升级\\n    ICLR 为 \\\"validated method\\\"，但显著加强 characterization paper 的深度和跨 benchmark 证据。\\n  related_experiments:\\n  - exp_id: plan_004_gsm8k_cross_benchmark\\n    role: primary\\n    result: negative_but_informative\\n  - exp_id: plan_017_downstream_impact\\n    role: corroborating\\n    result: negative_but_informative\\n  depends_on:\\n  - D013\\n  - D011\\n\", \"total_chars\": 12255, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a4b58d0-e819-4e45-8005-7fb93858fb5f",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "fea4d0e0-a87f-4b60-9c9e-4dd641bb37f0",
  "sourceToolAssistantUUID": "4a4b58d0-e819-4e45-8005-7fb93858fb5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-21T02:17:14.184Z_

Let me now read the experiment artifacts and the ROADMAP for more detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fea4d0e0-a87f-4b60-9c9e-4dd641bb37f0",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEukstgtSAHPcxwvHCfq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5f25df0-cfb0-4c90-81f8-8350d6ea80ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGYKxqUzb1BPfuNoqDR5r2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13106,
      "cache_read_input_tokens": 19992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13106,
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

_source line 19 · 2026-05-21T02:17:14.610Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01M8jVpfMqdkf16WBwhmARHh`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5f25df0-cfb0-4c90-81f8-8350d6ea80ce",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEukstgtSAHPcxwvHCfq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81c4b1b3-cadd-4908-9fff-b4b8e503d072",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGYKxqUzb1BPfuNoqDR5r2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13106,
      "cache_read_input_tokens": 19992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13106,
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

_source line 20 · 2026-05-21T02:17:14.623Z_

<details><summary>↩ Tool result · `toolu_01M8jVpfMqdkf16WBwhmARHh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ROADMAP.md\", \"content\": \"# irt_equated_bench_regen — Research Dashboard\\n\\n> 最后更新: 2026-05-21 02:15 UTC | 更新原因: 标记已完成任务 + 派出 Reviewer claim 强度讨论\\n\\n## 核心方向\\n**Pivot 完成 (D011)**：从\\\"DIF 检测方法\\\"转向\\\"LLM benchmark psychometric characterization + DIF methodology\\\"。ICLR 2027 目标不变。\\n\\n**GSM1K 结果 (D014)**：DIF flags 与 contamination gap 显著负相关（r=−0.478, p=0.005）。DIF 标记 contamination 无法到达的 capability-discriminative items。强化 \\\"diagnostic lens\\\" 叙事。\\n\\n## 当前进展\\n- **阶段**: **Writing**（全部实验完成）\\n- **实验**: 12 完成（5 success / 5 negative / 0 failed），plan_004 全 3 步完成\\n- **Key results**:\\n  - MMLU: semi-synthetic ΔTPR=+0.508 | cross-subject ΔFPR=0.000 | within-subject C%=38.1% | downstream z=-8 to -49σ\\n  - GSM8K: temporal C%=18.9% | semi-synthetic ΔTPR=+0.818 | GSM1K gap r=−0.478 (p=0.005)\\n- **Paper Agent**: 6/6 figures ✅ | writing_plan.yaml 整合 GSM8K ✅ | Step 3 (Literature Gap-Fill) 进行中\\n- **Dream #3**: dream_20260521T012912 运行中（post-pivot framing）\\n- **审稿**: Round 1 borderline 3.5/6，14 issues tracked\\n\\n## 近期任务\\n- [x] Agent: 修正 Step 3 report 方向标签 ✅\\n- [x] Paper Agent: figures 6/6 完成 ✅\\n- [x] Paper Agent: writing_plan.yaml 整合 GSM8K/GSM1K ✅\\n- [ ] Reviewer: D014 claim 强度深度评估 + 6 个阴性结果论文处理方案 ← 刚派出\\n- [ ] Paper Agent: Step 3 Literature Gap-Fill → Step 4 Writing ← 进行中\\n- [ ] Dream #3 结果分析（完成后处理）\\n- [ ] fig_5 style refinement（Step 5 统一处理）\\n\\n## Completed\\n- ✅ plan_001-017: 10 个 MMLU 实验全部完成\\n- ✅ plan_004 Step 1-3: GSM8K cross-benchmark 验证全部完成（报告已修正）\\n- ✅ 文献调查 22 篇 + experiment_summary.md + artifacts QC\\n- ✅ paper_framing.md 更新至 D014（Claim 4 four-layer, Claim 3 cross-benchmark）\\n- ✅ writing_plan.yaml 审批通过，figures 6/6 完成\\n\\n## GPU 预算\\nP0: 250h | P1: 350h | 已用: 0h（全部 CPU analysis）\\n\\n## 投稿目标\\nICLR 2027（~2026年10月 DDL）— 不降级\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D014 | 2026-05-21 | plan_004 Step 3 GSM1K: |r|=0.478 显著但方向为负——DIF 不标记  | plan_004_gsm8k_cross_benchmark, plan_017_downstream_impact |\\n| D013 | 2026-05-21 | plan_017 downstream impact negative 但 informative： | plan_017_downstream_impact |\\n| D012 | 2026-05-20 | Story 定稿：Candidate 1 (benchmark quality tool) + gr | plan_014_within_subject_dif, plan_016_within_subject_semi_synthetic, plan_001_real_data_dif_mmlu |\\n| D011 | 2026-05-20 | Pivot 拍板：从\\\"DIF 检测方法\\\"转向\\\"LLM benchmark psychometric  | plan_016_within_subject_semi_synthetic, plan_014_within_subject_dif, plan_011_semi_synthetic |\\n| D010 | 2026-05-20 | 方向 3 (Bifactor) pre-check 否定：within-subject tempor | plan_014_within_subject_dif, plan_011_semi_synthetic |\\n| D009 | 2026-05-20 | Dream #2 分析：best=3/6, median=3-4/6, worst=3/6。跨档一致 | dream_20260520T205007 |\\n| D008 | 2026-05-20 | 方向 2 (IRT θ-conditioning) 失败，1D 路线穷尽。plan_011 abil | plan_012_irt_theta_conditioning |\\n| D007 | 2026-05-20 | Story pivot: semi-synthetic validation 作为核心效度证据，Li | plan_011_semi_synthetic, plan_001_real_data_dif_mmlu, plan_001b_matched_ability_dif |\\n| D006 | 2026-05-20 | plan_011 positive: MH-DIF 检测差异性污染有效 (p=0.5 TPR=0.8 | plan_011_semi_synthetic |\\n| D005 | 2026-05-20 | 方向 1 (matched-ability DIF) 失败确认，所有 quintile enrich | plan_001b_matched_ability_dif |\\n\\n\\n\\n\", \"total_chars\": 3011, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81c4b1b3-cadd-4908-9fff-b4b8e503d072",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "ad0b0230-d023-424a-ace2-da015b630db9",
  "sourceToolAssistantUUID": "81c4b1b3-cadd-4908-9fff-b4b8e503d072",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T02:17:14.915Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UajdDThybJrsBvCS53BqQX`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad0b0230-d023-424a-ace2-da015b630db9",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEukstgtSAHPcxwvHCfq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b3836bc-fe12-414a-9d96-155a341afd2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGYKxqUzb1BPfuNoqDR5r2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13106,
      "cache_read_input_tokens": 19992,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13106,
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

_source line 22 · 2026-05-21T02:17:14.939Z_

<details><summary>↩ Tool result · `toolu_01UajdDThybJrsBvCS53BqQX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml\", \"content\": \"categories:\\n- key: contamination_detection\\n  name: Benchmark Contamination Detection\\n  narrative: Methods for detecting training data contamination in LLM benchmarks,\\n    including RL-robust approaches\\n- key: irt_equating\\n  name: IRT Methodology & Equating\\n  narrative: Item Response Theory models, calibration, equating, and their application\\n    to LLM evaluation\\n- key: benchmark_design\\n  name: Dynamic Benchmark Design\\n  narrative: Approaches for creating contamination-resistant or self-updating benchmarks\\n- key: dif_methodology\\n  name: DIF Statistical Methods\\n  narrative: Differential Item Functioning detection methods, power analysis, and\\n    small-sample strategies\\n- key: item_generation\\n  name: Automated Item Generation\\n  narrative: LLM-based test item generation with difficulty control and psychometric\\n    validation\\nmeta:\\n  last_updated: '2026-05-21T01:40:38.004Z'\\n  total_papers: 16\\npapers:\\n  belzak2020smallsample:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Belzak, W.\\n    bibtex_key: belzak2020smallsample\\n    category: dif_methodology\\n    doi: ''\\n    relevance: Parsimonious logistic regression with sum scores outperforms complex\\n      IRT models for DIF detection in small samples; directly applicable to our N=50-80\\n      model cohorts\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Testing Differential Item Functioning in Small Samples\\n    url: ''\\n    venue: Multivariate Behavioral Research\\n    verified: false\\n    year: 2020\\n  hardy2026scalability:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Hardy, M.\\n    bibtex_key: hardy2026scalability\\n    category: irt_equating\\n    doi: ''\\n    relevance: Nonparametric signed isotonic R2 scalability coefficients outperform\\n      IRT item diagnostics; lightweight pre-filter for item quality before our parametric\\n      calibration\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients\\n    url: https://arxiv.org/abs/2603.24999\\n    venue: arXiv\\n    verified: false\\n    year: 2026\\n  kim2019fpc:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Kim, S.\\n    - Kolen, M.\\n    bibtex_key: kim2019fpc\\n    category: irt_equating\\n    doi: ''\\n    relevance: Fixed-parameter calibration requires only N>=200 vs N>=500 for full\\n      calibration; core methodology for our bifactor IRT equating with anchor items\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data\\n    url: ''\\n    venue: Applied Measurement in Education\\n    verified: false\\n    year: 2019\\n  liang2026dvd:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Liang, R.\\n    bibtex_key: liang2026dvd\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Detects variant contamination via generation variance (AUC 0.73-0.74\\n      vs Min-K++ 0.43-0.68); complementary signal in our ensemble but untested under\\n      RL training\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'DVD: Detection via Variance of Generation Distribution for Variant Contamination'\\n    url: https://arxiv.org/abs/2601.04895\\n    venue: arXiv\\n    verified: true\\n    year: 2026\\n  polo2026growingpains:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Polo, F.\\n    bibtex_key: polo2026growingpains\\n    category: irt_equating\\n    doi: ''\\n    relevance: Uses multidimensional IRT with fixed-parameter calibration and 100\\n      anchor items for extensible evaluation (rho>=0.9); addresses score comparability\\n      but NOT contamination detection or item regeneration\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter\\n      Calibration'\\n    url: ''\\n    venue: arXiv\\n    verified: false\\n    year: 2026\\n  polo2026psnirt:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Polo, F.\\n    bibtex_key: polo2026psnirt\\n    category: irt_equating\\n    doi: ''\\n    relevance: PSN-IRT analyzes benchmark quality via 4PL IRT; provides published\\n      IRT parameters for MMLU we can use in semi-synthetic validation\\n    role: method-component\\n    semantic_scholar_id: ''\\n    title: Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item\\n      Response Theory\\n    url: ''\\n    venue: AAAI 2026\\n    verified: false\\n    year: 2026\\n  tao2026selfcritique:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Tao, Y.\\n    bibtex_key: tao2026selfcritique\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Self-Critique/RL-MIA partially addresses RL concealment via policy-collapse\\n      detection, but remains individual-model-level; our DIF is group-level and complementary\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: Detecting Data Contamination from Reinforcement Learning Post-training\\n      for Large Language Models\\n    url: https://arxiv.org/abs/2510.09259\\n    venue: ICLR 2026\\n    verified: true\\n    year: 2026\\n  wang2026fragility:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Wang, H.\\n    - Li, H.\\n    - Ko, B.\\n    - Zhang, H.\\n    bibtex_key: wang2026fragility\\n    category: contamination_detection\\n    doi: ''\\n    relevance: Proves GRPO/PPO RL training conceals contamination signals (14-20pp\\n      AUROC degradation), motivating our DIF-based approach which operates on behavioral\\n      patterns immune to NLL smoothing\\n    role: foundation\\n    semantic_scholar_id: 9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3\\n    title: On The Fragility of Benchmark Contamination Detection in Reasoning Models\\n    url: https://arxiv.org/abs/2510.02386\\n    venue: ICLR 2026\\n    verified: true\\n    year: 2026\\n  white2025livebench:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - White, C.\\n    bibtex_key: white2025livebench\\n    category: benchmark_design\\n    doi: ''\\n    relevance: Monthly-updated contamination-free benchmark with objective scoring;\\n      no difficulty calibration or psychometric equivalence across updates\\n    role: direct-competitor\\n    semantic_scholar_id: ''\\n    title: 'LiveBench: A Challenging, Contamination-Free LLM Benchmark'\\n    url: ''\\n    venue: ICLR 2025\\n    verified: false\\n    year: 2025\\n  zhang2024gsm1k:\\n    abstract: ''\\n    added_at: '2026-05-20T17:30:00.000Z'\\n    added_by: director\\n    authors:\\n    - Zhang, H.\\n    bibtex_key: zhang2024gsm1k\\n    category: contamination_detection\\n    doi: ''\\n    relevance: GSM1K documents 10-13% average accuracy drops from contamination; provides\\n      ground-truth contamination evidence and item-level effect sizes (delta 0.8-1.4\\n      logits) critical for our DIF power analysis\\n    role: foundation\\n    semantic_scholar_id: ef62f95c16f668f031d649799cbd79081c6d2b0f\\n    title: A Careful Examination of Large Language Model Performance on Grade School\\n      Arithmetic\\n    url: https://arxiv.org/abs/2405.00332\\n    venue: arXiv\\n    verified: true\\n    year: 2024\\n  li2024contamination:\\n    title: An Open-Source Data Contamination Report for Large Language Models\\n    authors:\\n    - Li, Y.\\n    - Guo, Y.\\n    - Guerin, F.\\n    - Lin, C.\\n    year: 2024\\n    venue: Findings of EMNLP 2024\\n    url: https://aclanthology.org/2024.findings-emnlp.30/\\n    doi: 10.18653/v1/2024.findings-emnlp.30\\n    bibtex_key: li2024contamination\\n    category: contamination_detection\\n    role: foundation\\n    relevance: Provides web-overlap contamination labels for MMLU and other benchmarks\\n      via Common Crawl matching; primary ground-truth comparison for our DIF-based\\n      contamination detection\\n    abstract: ''\\n    semantic_scholar_id: 32e11cf020021c225782a3b77b5cfed4ae8e14a0\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  shi2024mink:\\n    title: Detecting Pretraining Data from Large Language Models\\n    authors:\\n    - Shi, W.\\n    - Ajith, A.\\n    - Xia, M.\\n    - Huang, Y.\\n    - Liu, D.\\n    - Blevins, T.\\n    - Chen, D.\\n    - Zettlemoyer, L.\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2310.16789\\n    doi: ''\\n    bibtex_key: shi2024mink\\n    category: contamination_detection\\n    role: foundation\\n    relevance: Introduces Min-K% Prob method and WikiMIA benchmark for pretraining\\n      data detection; key baseline whose limitations under RL training motivate our\\n      DIF-based alternative\\n    abstract: ''\\n    semantic_scholar_id: 3422d5e0cdfdc935d6a84a1e3d3f96659265fe3a\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  balloccu2024leak:\\n    title: 'Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in\\n      Closed-Source LLMs'\\n    authors:\\n    - Balloccu, S.\\n    - Schmidtova, P.\\n    - Lango, M.\\n    - Dusek, O.\\n    year: 2024\\n    venue: EACL 2024\\n    url: https://arxiv.org/abs/2402.03927\\n    doi: 10.18653/v1/2024.eacl-long.5\\n    bibtex_key: balloccu2024leak\\n    category: contamination_detection\\n    role: foundation\\n    relevance: Systematic survey of data leakage in closed-source LLMs covering 255\\n      papers and 263 benchmarks; establishes scope of contamination problem motivating\\n      our detection approach\\n    abstract: ''\\n    semantic_scholar_id: 798feda076ad710df65d509a7884bd15937c8056\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  dekoninck2024constat:\\n    title: 'ConStat: Performance-Based Contamination Detection in Large Language Models'\\n    authors:\\n    - Dekoninck, J.\\n    - Mueller, M. N.\\n    - Vechev, M.\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: https://arxiv.org/abs/2405.16281\\n    doi: ''\\n    bibtex_key: dekoninck2024constat\\n    category: contamination_detection\\n    role: direct-competitor\\n    relevance: Performance-based contamination detection via perturbation analysis;\\n      closest methodological parallel to our DIF approach in using behavioral patterns\\n      rather than memorization signals\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  golchin2024timetravel:\\n    title: 'Time Travel in LLMs: Tracing Data Contamination in Large Language Models'\\n    authors:\\n    - Golchin, S.\\n    - Surdeanu, M.\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2308.08493\\n    doi: ''\\n    bibtex_key: golchin2024timetravel\\n    category: contamination_detection\\n    role: method-component\\n    relevance: Instance-level contamination detection via guided completion prompts;\\n      baseline approach for individual-item detection that our group-level DIF method\\n      extends\\n    abstract: ''\\n    semantic_scholar_id: d6d0fd994f37b630f35945736b5e1bb198148404\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n  zhang2024minkpp:\\n    title: 'Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large\\n      Language Models'\\n    authors:\\n    - Zhang, J.\\n    - Sun, J.\\n    - Yeats, E.\\n    - Ouyang, Y.\\n    - Kuo, M.\\n    - Zhang, J.\\n    - Yang, H.\\n    - Li, H.\\n    year: 2024\\n    venue: arXiv\\n    url: https://arxiv.org/abs/2404.02936\\n    doi: ''\\n    bibtex_key: zhang2024minkpp\\n    category: contamination_detection\\n    role: direct-competitor\\n    relevance: Improves Min-K% with vocabulary-normalized token probabilities; key\\n      baseline whose AUC degrades to 0.43-0.68 on RL-trained models, motivating our\\n      DIF-based alternative\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: literature-gap-fill\\n    added_at: '2026-05-21T01:40:37.987Z'\\n\", \"total_chars\": 11927, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b3836bc-fe12-414a-9d96-155a341afd2e",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "88486eaf-5973-4238-9d86-3705bdf07af3",
  "sourceToolAssistantUUID": "3b3836bc-fe12-414a-9d96-155a341afd2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-21T02:17:18.180Z_

Now let me look at the actual experiment artifacts to understand the detailed results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88486eaf-5973-4238-9d86-3705bdf07af3",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEumPjJZQqQzuiuHTKU4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc0b5785-d292-48ae-acfe-c2ffdc1814ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFSUuJcyA1pVkzUr7seqGs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6413,
      "cache_read_input_tokens": 33098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6413,
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

_source line 24 · 2026-05-21T02:17:20.805Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01NUmJjpYKYh6SZA7qhst3mT`</summary>

```json
{
  "pattern": "**/artifacts/**/report/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc0b5785-d292-48ae-acfe-c2ffdc1814ad",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEumPjJZQqQzuiuHTKU4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3c0fa37c-1263-4069-85d9-f2f7f8aecb3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFSUuJcyA1pVkzUr7seqGs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6413,
      "cache_read_input_tokens": 33098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6413,
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

_source line 25 · 2026-05-21T02:17:20.821Z_

<details><summary>↩ Tool result · `toolu_01NUmJjpYKYh6SZA7qhst3mT`</summary>

```text
artifacts/_project/report/metabench_data_summary.md
artifacts/_project/report/metabench_data_summary_ec3bbf.md
artifacts/_project/report/irt_scale_analysis.md
artifacts/_project/report/mmlu_cf_analysis.md
artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md
artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report_00ca1f.md
artifacts/plan_001b/report/plan_001b_report.md
artifacts/plan_011_semi_synthetic_validation/report/plan_011_report_c7ae89.md
artifacts/plan_011_semi_synthetic_validation/report/plan_011_report.md
artifacts/_project/report/plan_012_report.md
artifacts/plan_012_irt_theta_conditioning/report/plan_012_report.md
artifacts/_project/report/plan_014_report.md
artifacts/_project/report/plan_013_report.md
artifacts/plan_013_q3_local_independence/report/plan_013_report.md
artifacts/_project/report/plan_016_report.md
artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report.md
artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report_fb64fc.md
artifacts/_project/report/literature_survey_d011.md
artifacts/_project/report/experiment_summary.md
artifacts/_project/report/artifacts_qc_report.md
artifacts/_project/report/literature_survey_d011_167b57.md
artifacts/plan_017/report/plan_017_report.md
artifacts/_project/report/plan_004_data_availability.md
artifacts/_project/report/plan_004_step1_report.md
artifacts/_project/report/plan_004_step2_report.md
artifacts/_project/report/gsm1k_data_report.md
artifacts/_project/report/plan_004_step3_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3c0fa37c-1263-4069-85d9-f2f7f8aecb3f",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "1813bced-556e-4785-95f2-42ab793de7f5",
  "sourceToolAssistantUUID": "3c0fa37c-1263-4069-85d9-f2f7f8aecb3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T02:17:21.007Z_

<details open><summary>🔧 Tool call — Glob · `toolu_019aqx17QTce66532hTbPYeL`</summary>

```json
{
  "pattern": "**/artifacts/**/data/*.csv",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1813bced-556e-4785-95f2-42ab793de7f5",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEumPjJZQqQzuiuHTKU4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd402fc7-7cfb-40fd-9fa0-090dc3a82b91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFSUuJcyA1pVkzUr7seqGs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6413,
      "cache_read_input_tokens": 33098,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6413
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 33098,
          "cache_creation_input_tokens": 6413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6413,
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

_source line 27 · 2026-05-21T02:17:21.022Z_

<details><summary>↩ Tool result · `toolu_019aqx17QTce66532hTbPYeL`</summary>

```text
artifacts/_project/data/dif_power_results.csv
artifacts/mvp_dif_power_sim/data/dif_power_results.csv
artifacts/mvp_dif_power_sim/data/dif_diagnostic_tpr_comparison.csv
artifacts/_project/data/dif_phase2_results.csv
artifacts/_project/data/metabench_irt_params.csv
artifacts/_project/data/metabench_ctt_stats.csv
artifacts/_project/data/metabench_irt_params_345678.csv
artifacts/_project/data/metabench_model_accuracy.csv
artifacts/_project/data/metabench_cohort_analysis.csv
artifacts/_project/data/metabench_rl_models_18eb0d.csv
artifacts/_project/data/metabench_rl_models.csv
artifacts/_project/data/mmlu_cf_ground_truth.csv
artifacts/_project/data/mmlu_li2024_proxy_labels.csv
artifacts/_project/data/item_metadata.csv
artifacts/_project/data/model_metadata.csv
artifacts/plan_001_real_data_dif_mmlu/data/dif_results_temporal.csv
artifacts/plan_001_real_data_dif_mmlu/data/dif_results_temporal_69f998.csv
artifacts/plan_001_real_data_dif_mmlu/data/dif_results_ability_c17059.csv
artifacts/plan_001_real_data_dif_mmlu/data/dif_results_ability.csv
artifacts/plan_001_real_data_dif_mmlu/data/dif_summary.csv
artifacts/plan_001_real_data_dif_mmlu/data/within_family_dif.csv
artifacts/plan_001_real_data_dif_mmlu/data/cross_analysis.csv
artifacts/plan_001_real_data_dif_mmlu/data/domain_specificity.csv
artifacts/plan_001_real_data_dif_mmlu/data/neg_disc_sensitivity.csv
artifacts/plan_001b/data/enrichment_summary.csv
artifacts/plan_001b/data/dif_results_merged.csv
artifacts/plan_011_semi_synthetic_validation/data/injection_results.csv
artifacts/plan_011_semi_synthetic_validation/data/dose_response_summary_779a18.csv
artifacts/plan_011_semi_synthetic_validation/data/dose_response_summary.csv
artifacts/plan_011_semi_synthetic_validation/data/per_item_results.csv
artifacts/_project/data/theta_estimates.csv
artifacts/_project/data/dose_response_theta.csv
artifacts/plan_012_irt_theta_conditioning/data/dose_response_theta.csv
artifacts/_project/data/enrichment_theta.csv
artifacts/_project/data/within_subject_dif_results.csv
artifacts/_project/data/q3_within_vs_cross.csv
artifacts/_project/data/q3_summary.csv
artifacts/plan_013_q3_local_independence/data/q3_summary.csv
artifacts/_project/data/within_subject_injection_results.csv
artifacts/_project/data/within_subject_dose_response.csv
artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response.csv
artifacts/plan_016_within_subject_semi_synthetic/data/within_subject_dose_response_e6d86f.csv
artifacts/plan_017/data/ranking_comparison.csv
artifacts/plan_017/data/progressive_removal.csv
artifacts/plan_017/data/random_baseline.csv
artifacts/plan_017/data/rank_movers.csv
artifacts/_project/data/gsm8k_dif_results.csv
artifacts/_project/data/gsm8k_ets_summary.csv
artifacts/_project/data/gsm8k_dose_response.csv
artifacts/_project/data/gsm8k_dose_response_summary.csv
artifacts/_project/data/gsm1k_model_accuracy.csv
artifacts/_project/data/gsm1k_dif_correlation.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd402fc7-7cfb-40fd-9fa0-090dc3a82b91",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "a9592bf6-b021-4de1-a404-bd33b124f9d1",
  "sourceToolAssistantUUID": "dd402fc7-7cfb-40fd-9fa0-090dc3a82b91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T02:17:25.153Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FLx4Hq3s1Jp4hZvixu9mz5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/experiment_summary.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9592bf6-b021-4de1-a404-bd33b124f9d1",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEumqGhniWSs5aaWgCee",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "19909b5d-ae31-4417-ba3f-760a47f6bc3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ss7Qnv8FawY1xzhyCYFiLc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1796,
      "cache_read_input_tokens": 39511,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1796
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 96,
          "cache_read_input_tokens": 39511,
          "cache_creation_input_tokens": 1796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1796,
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

_source line 29 · 2026-05-21T02:17:25.162Z_

<details><summary>↩ Tool result · `toolu_01FLx4Hq3s1Jp4hZvixu9mz5`</summary>

````text
1	# Experiment Summary: IRT-Equated Benchmark Regeneration
2	
3	## Overview
4	
5	This project investigated whether Differential Item Functioning (DIF) analysis — a psychometric technique from educational testing — can detect benchmark contamination in LLMs. Starting from the hypothesis that MH-DIF could identify differentially contaminated items between temporal cohorts (2023 vs 2024 models), we ran a systematic chain of 11 experiments on the METABENCH dataset (5227 models × 12508 MMLU items).
6	
7	The core finding is a pivot: temporal DIF does not primarily detect contamination but reflects **genuine capability improvement** across model generations. Three independent approaches to reduce the 31% baseline DIF rate all failed (matched-ability, θ-conditioning, within-subject isolation), while semi-synthetic injection validated that the DIF methodology itself works correctly (ΔTPR=+0.674). The project pivoted from "DIF as contamination detector" to "psychometric characterization of LLM benchmark item instability" — the first large-scale quantification of how benchmark items behave differentially across model generations.
8	
9	## Experiment Chain
10	
11	### MVP Phase 1: DIF Power Simulation (Synthetic)
12	- **Exp ID**: mvp_dif_power_sim
13	- **Hypothesis**: MH + Logistic Regression DIF achieves TPR≥0.70, FPR≤0.10 at N≥50-80/group, δ≥1.0 logits on synthetic 2PL IRT data
14	- **Result**: BH-corrected p-value detection FAIL (TPR 0.04-0.07). ETS C classification conditional PASS: TPR=0.72-0.85 at N≥80, δ≥1.4; FPR<0.05; AUC=0.91-0.96
15	- **Conclusion**: Conditional success — ETS C replaces p-value as primary detector (D001)
16	- **Story contribution**: Established operational parameters (N≥80, δ≥1.4) and the ETS C classification as the primary DIF detection criterion
17	
18	### MVP Phase 2: DIF Power Simulation (Real IRT Parameters)
19	- **Exp ID**: mvp_dif_power_sim_phase2
20	- **Hypothesis**: ETS C maintains TPR≥0.65, FPR≤0.10 at N≥80, δ≥1.4 with real MMLU 2PL parameters from PSN-IRT
21	- **Result**: TPR=0.68 (N=80,δ=1.4) to 0.80 (N=100,δ=1.6); FPR=0.036-0.042; AUC=0.93
22	- **Conclusion**: Success — real parameter distributions degrade TPR by 3-6pp, within tolerance (D002)
23	- **Story contribution**: Validates DIF power under realistic item parameter distributions; recommends N≥100 as primary operating point
24	
25	### Plan 001: Real-Data MH-DIF on METABENCH MMLU
26	- **Exp ID**: plan_001_real_data_dif_mmlu
27	- **Hypothesis**: Temporal cohort MH-DIF flags items enriched in Li et al. contaminated set (enrichment >1.0, FPR≤0.05)
28	- **Result**: Temporal C%=31.3%, enrichment=0.96 (no enrichment); ability C%=2.9%, enrichment=1.19; within-family Llama-2 vs 3 C%=61.3%; domain ρ=0.307 (p=0.02); sanity random-split C%=0.18%
29	- **Conclusion**: Negative — temporal DIF detects systematic capability improvement, not contamination (D004)
30	- **Story contribution**: Key negative finding that motivated the entire pivot. The 31.3% temporal C% becomes the headline number for "item instability." Domain ρ=0.307 shows DIF is capability-driven. Sanity check (0.18%) proves the method isn't broken.
31	
32	### Plan 001b: Matched-Ability Temporal DIF
33	- **Exp ID**: plan_001b_matched_ability_dif
34	- **Hypothesis**: Within each accuracy quintile, temporal DIF enrichment rises to >1.5 after controlling for ability
35	- **Result**: All quintile enrichments 0.94-1.04
36	- **Conclusion**: Negative — ability matching cannot isolate contamination signal (D005)
37	- **Story contribution**: Eliminates "ability confound" as the sole explanation. Reviewer insight: Li et al. web-overlap is global contamination (available to all models), fundamentally incompatible with DIF which measures differential effects.
38	
39	### Plan 011: Semi-Synthetic DIF Validation
40	- **Exp ID**: plan_011_semi_synthetic_validation
41	- **Hypothesis**: MH-DIF detects injected differential contamination (focal-only incorrect→correct flips) with TPR>0.5, FPR<0.05 on ability cohort
42	- **Result**: Temporal+external: ΔTPR=+0.674 (0.326→1.000), FPR constant at 0.314; clear dose-response across p={0.3,0.5,0.7,1.0}; matching variable contamination discovered (standard MH FPR 0.298→0.616 at 20% injection, anchor/external immune)
43	- **Conclusion**: Success — DIF methodology validated; plan_001 failure attributed to ground truth mismatch (D006)
44	- **Story contribution**: The decisive validation experiment. Proves DIF works for differential contamination. Reinterprets Li et al. enrichment≈1.0 as "global vs differential contamination" insight (conceptual contribution). Matching variable contamination finding motivates external/anchor matching.
45	
46	### Plan 012: IRT θ-Conditioning
47	- **Exp ID**: plan_012_irt_theta_conditioning
48	- **Hypothesis**: Logit θ stratification (10-20 bins) reduces temporal baseline FPR from 31% to <10% while maintaining TPR>0.70
49	- **Result**: θ corr with total score = 0.9986; temporal FPR = 31-35% across all variants (no improvement); ability cohort θ-bins reduce FPR 49%→8% but TPR collapses 76%→21% (proving plan_011 ability TPR was mostly ability confounding)
50	- **Conclusion**: Negative — 1D θ ≡ total score, cannot reduce temporal FPR (D008)
51	- **Story contribution**: Proves temporal DIF is genuinely multidimensional — 1D ability cannot explain it. Corrects plan_011 ability cohort interpretation: 73% of apparent TPR was ability confounding.
52	
53	### Plan 013: Yen's Q3 Local Independence Diagnostic
54	- **Exp ID**: plan_013_q3_local_independence
55	- **Hypothesis**: Within-subject Q3 mean > 0.20, significantly higher than cross-subject, explaining part of 31% FPR
56	- **Result**: Within-subject mean Q3=0.0086 (below threshold), but 11.3% of pairs |Q3|>0.20 (vs 2.2% cross-subject, 5x ratio, Mann-Whitney p=2.3e-9); worst subjects: moral_scenarios 34.2%, world_religions 18%, marketing 17.5%
57	- **Conclusion**: Partial — local dependence exists but is moderate; not the primary driver of 31% FPR
58	- **Story contribution**: Addresses reviewer concern about IRT assumptions. Local dependence is a contributing factor but insufficient to explain 31% FPR, strengthening the "genuine temporal DIF" interpretation. Identifies specific problematic subjects for Discussion section.
59	
60	### Plan 014: Within-Subject Temporal DIF (Bifactor Pre-Check)
61	- **Exp ID**: plan_014_within_subject_dif
62	- **Hypothesis**: Within-subject C% < 15% in high-C% subjects, indicating between-subject ability differences drive overall C%
63	- **Result**: Average within-subject C%=38.1% (range 31.1-45.2%); cross-subject C%=40.5% (Δ=-2.4pp); all 5 subjects exceed 25% threshold
64	- **Conclusion**: Negative — temporal DIF penetrates into every subject; bifactor model cannot solve FPR (D010)
65	- **Story contribution**: Proves temporal DIF is pervasive and item-specific, not an artifact of between-subject ability differences. The 38.1% within-subject figure is a robustness check for the 31.3% global finding. Kills bifactor direction before wasting compute.
66	
67	### Plan 015: Bifactor IRT (Killed)
68	- **Exp ID**: plan_015_bifactor_irt
69	- **Hypothesis**: Bifactor (1 general + 57 subject factors) reduces temporal FPR to <15%
70	- **Conclusion**: Killed based on plan_014 pre-check (D010) — within-subject C%=38.1% proves bifactor cannot solve the problem
71	- **Story contribution**: Demonstrates methodological rigor — pre-mortem analysis saved compute and confirmed the exhaustive nature of the investigation
72	
73	### Plan 016: Within-Subject Semi-Synthetic Injection
74	- **Exp ID**: plan_016_within_subject_semi_synthetic
75	- **Hypothesis**: Within-subject DIF still detects injected contamination (ΔTPR>0.3 at p=0.5), validating plan_014's 38% as genuine
76	- **Result**: Cross-subject matching 4/5 subjects ΔTPR>0.3 at p=0.5; ΔFPR=0.000 across all 5 subjects (completely stable); within-subject matching 3/5 pass but FPR inflates +0.067 to +0.281
77	- **Conclusion**: Success — DIF works at subject level; cross-subject matching eliminates FPR inflation (D011)
78	- **Story contribution**: Final validation. Cross-subject ΔFPR=0.000 is a clean methodological contribution (solves matching variable contamination at subject level). Confirms plan_014's 38% is real temporal DIF, not method failure.
79	
80	### Plan 017: Downstream Impact (Preparing)
81	- **Exp ID**: plan_017_downstream_impact
82	- **Hypothesis**: Removing DIF-flagged items (~31% of MMLU) improves cross-generation model ranking stability (Spearman ρ), significantly better than random removal baseline
83	- **Status**: PREPARING
84	- **Story contribution**: Answers the "so what?" question — if DIF-flagged items cause ranking instability, removing them improves benchmark quality, providing downstream evidence for DIF as a benchmark quality tool
85	
86	## Decision Chain (D001-D012)
87	
88	```
89	D001 (ETS C > p-value) → D002 (MVP pass) → D003 (Dream #1)
90	    → D004 (temporal DIF = capability, not contamination)
91	        → D005 (matched-ability fails)
92	            → D006 (semi-synthetic validates DIF method)
93	                → D007 (story pivot: global vs differential contamination)
94	                    → D008 (θ-conditioning fails, 1D exhausted)
95	                        → D009 (Dream #2: bifactor is last hope)
96	                            → D010 (within-subject C%=38%, bifactor killed)
97	                                → D011 (pivot confirmed, cross-matching ΔFPR=0.000)
98	                                    → D012 (story finalized: benchmark quality tool)
99	```
100	
101	Three failed remediation directions:
102	1. **D005**: Matched-ability DIF → enrichment still ~1.0
103	2. **D008**: IRT θ-conditioning → θ ≡ total score (r=0.9986), FPR unchanged
104	3. **D010**: Bifactor pre-check → within-subject C%=38.1% > overall 31.3%
105	
106	## Key Numbers for Paper
107	
108	| Metric | Value | Source | Paper use |
109	|--------|-------|--------|-----------|
110	| METABENCH dataset size | 5227 models × 12508 items | data | Section 3 (Data) |
111	| Temporal C% (ETS C flagged) | 31.3% | plan_001 | Key finding: item instability rate |
112	| Ability C% | 2.9% | plan_001 | Contrast: ability-based DIF well-controlled |
113	| Li et al. enrichment (temporal) | 0.96 | plan_001 | Global vs differential contamination |
114	| Li et al. enrichment (ability) | 1.19 | plan_001 | Weak positive in ability cohort |
115	| Within-family C% (Llama-2 vs 3) | 61.3% | plan_001 | Impact-vs-DIF confound demonstration |
116	| Domain specificity ρ(C%, ΔAcc) | 0.307 (p=0.02) | plan_001 | Capability-driven DIF evidence |
117	| Sanity check C% (random split) | 0.18% | plan_001 | Method validity |
118	| Semi-synthetic ΔTPR (temporal, p=1.0) | +0.674 | plan_011 | Core validation: DIF detects differential contamination |
119	| Semi-synthetic FPR stability | 0.314 → 0.314 | plan_011 | FPR constant under injection |
120	| Semi-synthetic dose-response p=0.5 | TPR=0.834 | plan_011 | Detection at moderate effect |
121	| Matching variable contamination ΔFPR | 0.298 → 0.616 | plan_011 | Motivates external matching |
122	| θ–total score correlation | 0.9986 | plan_012 | 1D θ ≡ total score |
123	| Ability cohort corrected TPR (θ-bins) | 21% (was 76%) | plan_012 | 73% of ability TPR was confounding |
124	| Q3 within-subject |Q3|>0.20 | 11.3% (vs 2.2% cross) | plan_013 | Local dependence: moderate, not primary |
125	| Worst Q3 subject (moral_scenarios) | 34.2% pairs |Q3|>0.20 | plan_013 | Discussion: problematic subjects |
126	| Within-subject temporal C% (average) | 38.1% (range 31-45%) | plan_014 | Robustness: DIF pervasive within domains |
127	| Within vs cross-subject Δ | -2.4pp | plan_014 | Signal robust to matching choice |
128	| Cross-matching ΔFPR (all subjects) | 0.000 | plan_016 | Method: FPR completely stable |
129	| Cross-matching subjects with ΔTPR>0.3 | 4/5 at p=0.5 | plan_016 | Subject-level detection works |
130	| Within-matching FPR inflation at p=1.0 | +0.067 to +0.281 | plan_016 | Motivates cross-matching |
131	| MVP ETS C TPR at N=100, δ=1.6 | 0.80 | mvp_phase2 | Power analysis: method is powered |
132	| MVP ETS C FPR range | 0.036-0.042 | mvp_phase2 | Controlled false positive rate |
133	
134	## Evidence Chain Summary
135	
136	**Conclusion: Temporal DIF = genuine capability improvement, not contamination artifact.**
137	
138	The evidence chain:
139	
140	1. **DIF works** (plan_011): Semi-synthetic injection with known differential contamination yields ΔTPR=+0.674, perfect dose-response, and constant FPR — the methodology is sound.
141	
142	2. **But temporal DIF doesn't align with contamination labels** (plan_001): Enrichment=0.96 against Li et al. web-overlap labels. This is because web-overlap is *global* contamination (available to all models via Common Crawl), which by definition cannot produce group-specific DIF.
143	
144	3. **31% is not an ability-matching artifact**:
145	   - Matched-ability DIF still shows enrichment≈1.0 (plan_001b)
146	   - IRT θ is indistinguishable from total score (r=0.9986), finer binning doesn't help (plan_012)
147	   - Within-subject C%=38.1% — higher than global 31.3%, ruling out between-subject confounds (plan_014)
148	   - Local dependence (Q3) is moderate (11.3% >0.20) but insufficient to explain 31% (plan_013)
149	
150	4. **The method is validated at subject level** (plan_016): Cross-subject matching achieves ΔFPR=0.000 across all 5 tested subjects, with 4/5 showing ΔTPR>0.3 at p=0.5 injection level.
151	
152	5. **Therefore**: 31-38% of MMLU items exhibit genuine differential functioning between 2023 and 2024 model generations. This reflects real, item-specific capability changes — not contamination, not statistical artifacts, not matching failures. DIF is a valid tool for characterizing benchmark item instability, complementing but distinct from contamination detection.
153	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19909b5d-ae31-4417-ba3f-760a47f6bc3e",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "574748b3-836a-4dcd-b753-fc5ebf836ae5",
  "sourceToolAssistantUUID": "19909b5d-ae31-4417-ba3f-760a47f6bc3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T02:17:29.728Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PDDk5heDE1MFeio2KoCoZy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation/report/plan_011_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "574748b3-836a-4dcd-b753-fc5ebf836ae5",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEun92JQvUwV6xC7MiT4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a3307a55-6b22-45ea-8e98-f42a47e24088",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJqp7jCsMpoja9enU7b4uo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4619,
      "cache_read_input_tokens": 41307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4619,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 31 · 2026-05-21T02:17:29.743Z_

<details><summary>↩ Tool result · `toolu_01PDDk5heDE1MFeio2KoCoZy`</summary>

```text
1	# Plan 011: Semi-Synthetic DIF Validation
2	
3	## 1. Objective
4	
5	Inject known **differential** contamination into real MMLU response data and test
6	whether MH-DIF can detect it. This validates whether plan_001/001b's failure to find
7	enrichment was due to Li et al. labels being non-differential (global contamination)
8	rather than a fundamental limitation of MH-DIF.
9	
10	## 2. Setup
11	
12	- **Baseline items**: 500 (clean in Li et al. + ETS A in plan_001 ability DIF)
13	- **Contaminated per run**: 100 of 500
14	- **Injection probabilities**: [0.0, 0.3, 0.5, 0.7, 1.0]
15	- **Seeds per p**: 5
16	
17	### Cohort definitions
18	
19	- **ability**: ref N=2092, foc N=2089, foc inject N=2089
20	- **temporal**: ref N=1080, foc N=807, foc inject N=787
21	
22	> **Note**: Ability quintiles (Q1-2 vs Q4-5) have no accuracy overlap by construction (ref max=0.6319, foc min=0.6772). All focal models used for injection. MH stratification handles ability matching.
23	
24	### MH variants
25	
26	| Variant | Matching variable | Rationale |
27	|---------|-------------------|-----------|
28	| standard | sum of 500 items − current | Same as plan_001; susceptible to matching variable contamination when 20% items injected |
29	| anchor | sum of 400 known-clean items | Eliminates matching variable contamination; assumes oracle knowledge of clean items |
30	| external | sum of all 12,508 items (original, pre-injection) | Best matching precision; immune to injection; requires external ability estimate |
31	
32	## 3. Results by MH Variant
33	
34	### Standard MH
35	
36	| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
37	|--------|---|----------------|----------------|------|-----------|----------|
38	| ability | 0.0 | 0.594±0.053 | 0.611±0.013 | +0.000 | 0.96 | 0.4231 |
39	| ability | 0.3 | 0.700±0.057 | 0.609±0.026 | +0.106 | 1.58 | 0.2555 |
40	| ability | 0.5 | 0.760±0.046 | 0.600±0.021 | +0.166 | 2.21 | 0.0067 |
41	| ability | 0.7 | 0.806±0.036 | 0.598±0.030 | +0.212 | 2.90 | 0.0002 |
42	| ability | 1.0 | 0.816±0.035 | 0.596±0.023 | +0.222 | 3.17 | 0.0001 |
43	| temporal | 0.0 | 0.308±0.047 | 0.298±0.012 | +0.000 | 1.07 | 0.8081 |
44	| temporal | 0.3 | 0.424±0.059 | 0.390±0.018 | +0.116 | 1.18 | 0.6435 |
45	| temporal | 0.5 | 0.682±0.045 | 0.453±0.021 | +0.374 | 2.63 | 0.0001 |
46	| temporal | 0.7 | 0.966±0.009 | 0.503±0.021 | +0.658 | 30.34 | 0.0000 |
47	| temporal | 1.0 | 1.000±0.000 | 0.616±0.014 | +0.692 | inf | 0.0000 |
48	
49	### Anchor MH
50	
51	| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
52	|--------|---|----------------|----------------|------|-----------|----------|
53	| ability | 0.0 | 0.600±0.060 | 0.596±0.022 | +0.000 | 1.04 | 0.4893 |
54	| ability | 0.3 | 0.700±0.051 | 0.596±0.022 | +0.100 | 1.64 | 0.1731 |
55	| ability | 0.5 | 0.764±0.038 | 0.596±0.022 | +0.164 | 2.24 | 0.0014 |
56	| ability | 0.7 | 0.808±0.041 | 0.596±0.022 | +0.208 | 2.98 | 0.0001 |
57	| ability | 1.0 | 0.818±0.033 | 0.596±0.022 | +0.218 | 3.16 | 0.0001 |
58	| temporal | 0.0 | 0.314±0.053 | 0.307±0.018 | +0.000 | 1.07 | 0.5465 |
59	| temporal | 0.3 | 0.522±0.054 | 0.307±0.018 | +0.208 | 2.49 | 0.0001 |
60	| temporal | 0.5 | 0.806±0.034 | 0.307±0.018 | +0.492 | 9.59 | 0.0000 |
61	| temporal | 0.7 | 0.990±0.010 | 0.307±0.018 | +0.676 | inf | 0.0000 |
62	| temporal | 1.0 | 1.000±0.000 | 0.307±0.018 | +0.686 | inf | 0.0000 |
63	
64	### External MH
65	
66	| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
67	|--------|---|----------------|----------------|------|-----------|----------|
68	| ability | 0.0 | 0.498±0.041 | 0.493±0.010 | +0.000 | 1.04 | 0.5025 |
69	| ability | 0.3 | 0.662±0.044 | 0.493±0.010 | +0.164 | 2.07 | 0.0051 |
70	| ability | 0.5 | 0.756±0.041 | 0.493±0.010 | +0.258 | 3.31 | 0.0000 |
71	| ability | 0.7 | 0.792±0.034 | 0.493±0.010 | +0.294 | 4.04 | 0.0000 |
72	| ability | 1.0 | 0.800±0.038 | 0.493±0.010 | +0.302 | 4.30 | 0.0000 |
73	| temporal | 0.0 | 0.326±0.035 | 0.314±0.009 | +0.000 | 1.07 | 0.7203 |
74	| temporal | 0.3 | 0.548±0.033 | 0.314±0.009 | +0.222 | 2.67 | 0.0000 |
75	| temporal | 0.5 | 0.834±0.027 | 0.314±0.009 | +0.508 | 11.22 | 0.0000 |
76	| temporal | 0.7 | 0.990±0.010 | 0.314±0.009 | +0.664 | inf | 0.0000 |
77	| temporal | 1.0 | 1.000±0.000 | 0.314±0.009 | +0.674 | inf | 0.0000 |
78	
79	## 4. Key Comparison: Baseline FPR by Variant
80	
81	| Cohort | standard | anchor | external |
82	|--------|----------|--------|----------|
83	| ability | 0.611 | 0.596 | 0.493 |
84	| temporal | 0.298 | 0.307 | 0.314 |
85	
86	If external FPR ≪ standard FPR, the high baseline rate is from matching precision,
87	not inherent DIF in the selected items.
88	
89	## 5. Sanity Checks
90	
91	### Density change (focal × contaminated items)
92	
93	| Cohort | p | Orig density | Post density | Responses flipped |
94	|--------|---|--------------|--------------|-------------------|
95	| ability | 0.3 | 0.6772 | 0.7744 | 20301 |
96	| temporal | 0.3 | 0.5800 | 0.7068 | 9981 |
97	| ability | 0.5 | 0.6772 | 0.8386 | 33706 |
98	| temporal | 0.5 | 0.5800 | 0.7903 | 16553 |
99	| ability | 0.7 | 0.6772 | 0.9031 | 47177 |
100	| temporal | 0.7 | 0.5800 | 0.8741 | 23148 |
101	| ability | 1.0 | 0.6772 | 1.0000 | 67424 |
102	| temporal | 1.0 | 0.5800 | 1.0000 | 33053 |
103	
104	## 6. Verdict
105	
106	### Standard MH
107	
108	**ability**: baseline TPR=0.594/FPR=0.611, p=1.0 TPR=0.816/FPR=0.596, ΔTPR=+0.222
109	→ **PARTIAL**: detectable signal (ΔTPR=0.222) but modest
110	
111	**temporal**: baseline TPR=0.308/FPR=0.298, p=1.0 TPR=1.000/FPR=0.616, ΔTPR=+0.692
112	→ **SUCCESS**: injection raises TPR by 0.692 with clear dose-response
113	
114	### Anchor MH
115	
116	**ability**: baseline TPR=0.600/FPR=0.596, p=1.0 TPR=0.818/FPR=0.596, ΔTPR=+0.218
117	→ **PARTIAL**: detectable signal (ΔTPR=0.218) but modest
118	
119	**temporal**: baseline TPR=0.314/FPR=0.307, p=1.0 TPR=1.000/FPR=0.307, ΔTPR=+0.686
120	→ **SUCCESS**: injection raises TPR by 0.686 with clear dose-response
121	
122	### External MH
123	
124	**ability**: baseline TPR=0.498/FPR=0.493, p=1.0 TPR=0.800/FPR=0.493, ΔTPR=+0.302
125	→ **SUCCESS**: injection raises TPR by 0.302 with clear dose-response
126	
127	**temporal**: baseline TPR=0.326/FPR=0.314, p=1.0 TPR=1.000/FPR=0.314, ΔTPR=+0.674
128	→ **SUCCESS**: injection raises TPR by 0.674 with clear dose-response
129	
130	## 7. Overall Interpretation
131	
132	### Does MH-DIF detect differential contamination?
133	
134	- **Temporal + external matching**: TPR rises 0.326 → 1.000 (ΔTPR=+0.674), FPR 0.314 → 0.314
135	- **Ability + external matching**: TPR rises 0.498 → 0.800 (ΔTPR=+0.302), FPR 0.493 → 0.493
136	
137	### Implications for plan_001
138	
139	If semi-synthetic injection is detectable → plan_001's failure to find enrichment
140	against Li et al. labels is because Li et al. contamination is **non-differential**
141	(Common Crawl data available to all models), not because MH-DIF is fundamentally limited.
142	
143	### Matching variable contamination
144	
145	When 20% of items are injected, standard MH's matching variable (total score) is
146	corrupted by injected items, inflating FPR. This is a known limitation when DIF items
147	constitute a large fraction of the test. In practice, iterative purification (exclude
148	suspected DIF items from matching) or external ability estimates mitigate this.
149	
150	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a3307a55-6b22-45ea-8e98-f42a47e24088",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "04c4ee48-6ff9-4c42-8755-ebb6a32779c4",
  "sourceToolAssistantUUID": "a3307a55-6b22-45ea-8e98-f42a47e24088",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T02:17:30.239Z_

<details open><summary>🔧 Tool call — Read · `toolu_019KiAvYRqGqGdrLGE24fcim`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/plan_004_step3_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04c4ee48-6ff9-4c42-8755-ebb6a32779c4",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEun92JQvUwV6xC7MiT4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "343560e8-723f-4273-be28-ff6d142fef4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJqp7jCsMpoja9enU7b4uo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4619,
      "cache_read_input_tokens": 41307,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4619
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 41307,
          "cache_creation_input_tokens": 4619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4619,
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

_source line 33 · 2026-05-21T02:17:30.244Z_

<details><summary>↩ Tool result · `toolu_019KiAvYRqGqGdrLGE24fcim`</summary>

```text
1	# Plan 004 Step 3: GSM1K Contamination Gap × DIF Flag Correlation
2	
3	## Summary
4	
5	**Core finding**: Pearson r = −0.478 (p = 0.005). The correlation is significant and exceeds the |r| > 0.3 threshold, but the direction is **negative** — opposite to the contamination hypothesis. Models with larger GSM8K–GSM1K gaps show *less* advantage on DIF-C items, not more.
6	
7	## Data
8	
9	| Component | Count |
10	|-----------|-------|
11	| Matched models (in both GSM1K paper and MetaBench response matrix) | 33 |
12	| DIF-C items (standard matching, ETS class C) | 249 |
13	| Non-DIF items (ETS class A + B) | 1070 |
14	| Excluded: tiiuae/falcon-180B-chat (not in MetaBench) | 1 |
15	
16	## Main Analysis
17	
18	| Metric | Value | p-value |
19	|--------|-------|---------|
20	| Pearson r | −0.478 | 0.005 |
21	| Spearman ρ | −0.403 | 0.020 |
22	
23	All 33 models (except Deepseek-math-7b-rl) show **negative DIF advantage** — accuracy on DIF-C items is consistently lower than on non-DIF items. Models with larger contamination gaps show even more negative DIF advantage.
24	
25	## Control Analyses
26	
27	### Partial Correlation (controlling GSM8K overall accuracy)
28	
29	| Metric | Value | p-value |
30	|--------|-------|---------|
31	| Partial r | −0.385 | 0.027 |
32	
33	The correlation survives after controlling for overall accuracy, ruling out the confound that "strong models do better on everything."
34	
35	### Permutation Test (n = 1000)
36	
37	| Metric | Value |
38	|--------|-------|
39	| Observed r | −0.478 |
40	| Null mean | −0.007 |
41	| Null SD | 0.197 |
42	| Null 95% CI | [−0.383, 0.366] |
43	| Empirical p (two-tailed) | 0.014 |
44	
45	The observed correlation falls outside the null distribution's 95% CI. The DIF-C item set produces a significantly stronger negative correlation with contamination gap than random item subsets of the same size.
46	
47	### DIF-C Directionality Analysis
48	
49	DIF-C items split by direction (α_MH relative to 1):
50	
51	| Subset | n | Mean advantage | r with gap | p |
52	|--------|---|----------------|------------|---|
53	| DIF-C favoring focal (newer, α>1) | 78 | +0.031 | −0.143 | 0.429 |
54	| DIF-C favoring reference (older, α<1) | 171 | −0.194 | −0.347 | 0.048 |
55	
56	The overall negative correlation is driven primarily by the 171 reference-favoring DIF-C items. High-contamination models struggle disproportionately on items where older models perform relatively better. The 78 focal-favoring items show no significant relationship with contamination gap.
57	
58	## Outlier Analysis
59	
60	### Cook's Distance (top 5)
61	
62	| Model | Cook's D | Gap | DIF Advantage |
63	|-------|----------|-----|---------------|
64	| Deepseek-math-7b-rl | 0.300 | −0.022 | +0.003 |
65	| GPT-2-xl | 0.161 | 0.004 | −0.001 |
66	| Smaug-2-72B | 0.129 | 0.061 | −0.069 |
67	| Gemma-2b-it | 0.075 | −0.001 | −0.033 |
68	| Deepseek-llm-67b-base | 0.071 | 0.093 | −0.155 |
69	
70	Deepseek-math-7b-rl is the most influential point (negative gap, near-zero DIF advantage).
71	
72	### Leave-One-Out
73	
74	| Removed model | r without | Δr |
75	|---------------|-----------|-----|
76	| Deepseek-math-7b-rl | −0.374 | −0.105 |
77	| Smaug-2-72B | −0.537 | +0.058 |
78	| Gemma-2b-it | −0.438 | −0.040 |
79	| Mistral-7B-Instruct-v0.2 | −0.516 | +0.038 |
80	| GPT-2-xl | −0.442 | −0.037 |
81	
82	Removing Deepseek-math-7b-rl weakens the correlation to r = −0.374, but it remains significant (still > 0.3). No single point drives the result; the correlation is robust.
83	
84	## Model Family Observations
85	
86	| Family | n | Mean gap | Mean DIF advantage |
87	|--------|---|----------|--------------------|
88	| Smaug | 2 | 0.065 | −0.128 |
89	| Phi | 4 | 0.037 | −0.174 |
90	| Gemma | 5 | 0.051 | −0.143 |
91	| Llama/CodeLlama | 9 | 0.028 | −0.117 |
92	| Mixtral | 4 | 0.028 | −0.143 |
93	| DeepSeek | 2 | 0.036 | −0.076 |
94	
95	No single family dominates the trend. Phi models show high DIF disadvantage but moderate gaps. Gemma models cluster at moderate gap + moderate DIF disadvantage. The correlation is not an artifact of one family.
96	
97	## Interpretation
98	
99	### Against the contamination hypothesis
100	
101	The original hypothesis predicted **positive** correlation: contaminated models should gain disproportionate advantage on DIF-C items. The observed **negative** correlation (r = −0.478) contradicts this.
102	
103	### What DIF-C items capture
104	
105	DIF-C items are not simply "contaminated items." They are items with large differential functioning between temporal cohorts. 171/249 DIF-C items actually *disadvantage* newer models (α_MH < 1). These represent items where older models perform disproportionately well, possibly reflecting:
106	
107	1. Items testing patterns that were better represented in older training data
108	2. Items where newer model training (including potential contamination) disrupts general problem-solving strategies
109	3. Items that genuinely discriminate between different capability profiles across generations
110	
111	### The negative correlation means
112	
113	Models with higher contamination gaps (suspected contamination) do *worse* on DIF items — they show a narrower advantage pattern concentrated on non-DIF items. This is consistent with contamination producing a uniform boost on "normal" items while failing on items with atypical difficulty characteristics.
114	
115	### Success criteria assessment
116	
117	| Criterion | Result |
118	|-----------|--------|
119	| \|r\| > 0.3 (breakthrough) | ✅ \|r\| = 0.478 |
120	| Direction as hypothesized | ❌ Negative, not positive |
121	| Survives controls | ✅ Partial r = −0.385, permutation p = 0.014 |
122	
123	**Verdict**: The effect size meets the breakthrough threshold, but the direction inverts the contamination narrative. DIF-C items do not flag contaminated content — they flag items where contaminated models are actually *weaker*. This is still a strong, publishable finding: it demonstrates that DIF analysis captures genuine measurement anomalies orthogonal to contamination, supporting DIF as a tool for identifying construct-relevant item differences rather than data leakage.
124	
125	## Output Files
126	
127	- `gsm1k_dif_correlation.csv` — per-model data (33 rows)
128	- `fig_gsm1k_dif_correlation.png/pdf` — scatter plot with regression
129	- `fig_gsm1k_dif_perm_null.png` — permutation null distribution
130	- `plan_004_step3_gsm1k_dif_correlation.py` — analysis script
131	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "343560e8-723f-4273-be28-ff6d142fef4f",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "3b61a6a7-2e37-4e38-af1d-a02ea40156be",
  "sourceToolAssistantUUID": "343560e8-723f-4273-be28-ff6d142fef4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T02:17:35.063Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BeLtNHHJWAqPFJCxqzMPz6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_017/report/plan_017_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b61a6a7-2e37-4e38-af1d-a02ea40156be",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEunWnjyCKGhwRFaH279",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9db9720a-e0da-46fb-858a-5b9ad31731e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf4rXE8C8qxMEoCsvd9P7Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6037,
      "cache_read_input_tokens": 45926,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6037,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 35 · 2026-05-21T02:17:35.077Z_

<details><summary>↩ Tool result · `toolu_01BeLtNHHJWAqPFJCxqzMPz6`</summary>

```text
1	# plan_017: Downstream Impact Analysis — DIF Item Removal → Ranking Stability
2	
3	## Summary
4	
5	This analysis evaluates whether removing temporally unstable (DIF) items from MMLU
6	produces more stable and reliable model rankings.
7	
8	
9	## Data
10	
11	- Response matrix: 5227 models × 12508 items
12	- Temporal cohorts: 2023 (1080 models), 2024 (807 models)
13	- DIF classification: ETS A=6332, B=2258, C=3918
14	- Stable items (A+B): 8590 (68.7%)
15	- DIF items (C): 3918 (31.3%)
16	
17	
18	## Part 1: Full vs Stable-Only Ranking
19	
20	| Cohort | N models | ρ(full, stable) | 95% CI | SHR full | SHR stable |
21	|--------|----------|-----------------|--------|----------|------------|
22	| 2023 | 1080 | 0.998851 | [0.998490, 0.999028] | 0.9970±0.0005 | 0.9955±0.0007 |
23	| 2024 | 807 | 0.997014 | [0.995997, 0.997642] | 0.9923±0.0024 | 0.9890±0.0030 |
24	| all | 5227 | 0.996451 | [0.995977, 0.996808] | 0.9934±0.0018 | 0.9919±0.0016 |
25	
26	
27	## Part 2: Progressive DIF Removal
28	
29	| Frac | Removed | Remaining | Cohort | ρ(full, reduced) | 95% CI |
30	|------|---------|-----------|--------|------------------|--------|
31	| 0.00 | 0 | 12508 | 2023 | 1.000000 | [1.000000, 1.000000] |
32	| 0.00 | 0 | 12508 | 2024 | 1.000000 | [1.000000, 1.000000] |
33	| 0.00 | 0 | 12508 | all | 1.000000 | [1.000000, 1.000000] |
34	| 0.05 | 625 | 11883 | 2023 | 0.999846 | [0.999777, 0.999862] |
35	| 0.05 | 625 | 11883 | 2024 | 0.999351 | [0.999033, 0.999458] |
36	| 0.05 | 625 | 11883 | all | 0.998926 | [0.998730, 0.999062] |
37	| 0.10 | 1250 | 11258 | 2023 | 0.999641 | [0.999498, 0.999707] |
38	| 0.10 | 1250 | 11258 | 2024 | 0.998676 | [0.998120, 0.998969] |
39	| 0.10 | 1250 | 11258 | all | 0.997700 | [0.997313, 0.997990] |
40	| 0.15 | 1876 | 10632 | 2023 | 0.999458 | [0.999283, 0.999545] |
41	| 0.15 | 1876 | 10632 | 2024 | 0.997849 | [0.996921, 0.998397] |
42	| 0.15 | 1876 | 10632 | all | 0.997698 | [0.997344, 0.997998] |
43	| 0.20 | 2501 | 10007 | 2023 | 0.999344 | [0.999157, 0.999426] |
44	| 0.20 | 2501 | 10007 | 2024 | 0.997483 | [0.996414, 0.998024] |
45	| 0.20 | 2501 | 10007 | all | 0.997397 | [0.997027, 0.997747] |
46	| 0.25 | 3127 | 9381 | 2023 | 0.999192 | [0.998935, 0.999316] |
47	| 0.25 | 3127 | 9381 | 2024 | 0.997558 | [0.996460, 0.997958] |
48	| 0.25 | 3127 | 9381 | all | 0.997049 | [0.996577, 0.997407] |
49	| 0.30 | 3752 | 8756 | 2023 | 0.998865 | [0.998484, 0.999019] |
50	| 0.30 | 3752 | 8756 | 2024 | 0.997229 | [0.996209, 0.997794] |
51	| 0.30 | 3752 | 8756 | all | 0.996451 | [0.995945, 0.996938] |
52	| 0.38 | 4753 | 7755 | 2023 | 0.998644 | [0.998305, 0.998842] |
53	| 0.38 | 4753 | 7755 | 2024 | 0.995266 | [0.993763, 0.996262] |
54	| 0.38 | 4753 | 7755 | all | 0.996645 | [0.996159, 0.997027] |
55	
56	
57	## Part 3: DIF vs Random Removal Comparison
58	
59	Negative z-score = DIF removal causes *more* rank disruption than random.
60	
61	| Frac | Cohort | ρ DIF | ρ Random (mean±std) | z-score |
62	|------|--------|-------|---------------------|---------|
63	| 0.05 | 2023 | 0.999846 | 0.999942±0.000009 | -10.20 |
64	| 0.05 | 2024 | 0.999351 | 0.999844±0.000042 | -11.70 |
65	| 0.05 | all | 0.998926 | 0.999886±0.000033 | -29.07 |
66	| 0.10 | 2023 | 0.999641 | 0.999898±0.000010 | -25.12 |
67	| 0.10 | 2024 | 0.998676 | 0.999727±0.000095 | -11.00 |
68	| 0.10 | all | 0.997700 | 0.999795±0.000042 | -49.44 |
69	| 0.15 | 2023 | 0.999458 | 0.999823±0.000031 | -11.71 |
70	| 0.15 | 2024 | 0.997849 | 0.999552±0.000151 | -11.28 |
71	| 0.15 | all | 0.997698 | 0.999611±0.000157 | -12.22 |
72	| 0.20 | 2023 | 0.999344 | 0.999774±0.000046 | -9.42 |
73	| 0.20 | 2024 | 0.997483 | 0.999415±0.000152 | -12.72 |
74	| 0.20 | all | 0.997397 | 0.999477±0.000171 | -12.15 |
75	| 0.25 | 2023 | 0.999192 | 0.999713±0.000040 | -12.89 |
76	| 0.25 | 2024 | 0.997558 | 0.999247±0.000203 | -8.33 |
77	| 0.25 | all | 0.997049 | 0.999370±0.000163 | -14.26 |
78	| 0.30 | 2023 | 0.998865 | 0.999648±0.000041 | -19.02 |
79	| 0.30 | 2024 | 0.997229 | 0.999084±0.000227 | -8.16 |
80	| 0.30 | all | 0.996451 | 0.999219±0.000244 | -11.35 |
81	| 0.38 | 2023 | 0.998644 | 0.999499±0.000065 | -13.18 |
82	| 0.38 | 2024 | 0.995266 | 0.998777±0.000326 | -10.76 |
83	| 0.38 | all | 0.996645 | 0.998850±0.000241 | -9.16 |
84	
85	
86	## Part 4: Top Rank Movers (all models, full → stable-only)
87	
88	### Biggest rank *drops* (benefited from DIF items)
89	
90	| Model | Family | Method | Rank Full | Rank Stable | ΔRank |
91	|-------|--------|--------|-----------|-------------|-------|
92	| Sao10K/14B-Glacier-Stack | unknown | unknown | 555 | 1406 | +851 |
93	| AA051611/A0118 | unknown | unknown | 1169 | 1996 | +827 |
94	| DeepMount00/phi_3 | phi-3 | unknown | 736 | 1545 | +809 |
95	| Mihaiii/Pallas-0.5-frankenmerge | unknown | unknown | 455 | 1264 | +809 |
96	| DeepMount00/Phi-3-Mini-4K-Boost | phi-3 | unknown | 738 | 1546 | +808 |
97	| vonjack/phi-3-mini-4k-instruct-llamafied | phi-3 | unknown | 534 | 1334 | +800 |
98	| vonjack/Phi-3-mini-4k-instruct-LLaMAfied | phi-3 | unknown | 533 | 1330 | +797 |
99	| nbeerbower/llama-3-dragonmaid-8B-v2 | llama-3 | unknown | 576 | 1369 | +793 |
100	| raincandy-u/phillama-3.8b-v0.1 | llama-3 | unknown | 733 | 1500 | +767 |
101	| nbeerbower/llama-3-stinky-8B | llama-3 | unknown | 553 | 1300 | +747 |
102	| cognitivecomputations/yayi2-30b-llama | unknown | unknown | 469 | 1202 | +733 |
103	| cstr/llama3-8b-spaetzle-v13 | llama-3 | unknown | 705 | 1437 | +732 |
104	| shyamieee/JARVIS-v1.0 | unknown | unknown | 616 | 1345 | +729 |
105	| Nitral-AI/Poppy_Porpoise-0.96-L3-8B | unknown | unknown | 712 | 1430 | +718 |
106	| nbeerbower/llama-3-stella-8B | llama-3 | unknown | 588 | 1287 | +699 |
107	| FairMind/Phi-3-mini-4k-instruct-bnb-4bit-Ita | phi-3 | unknown | 956 | 1651 | +695 |
108	| rhysjones/Phi-3-mini-mango-1-llamafied | phi-3 | unknown | 563 | 1258 | +695 |
109	| GeorgiaTech/0.0005_llama_nodpo_3iters_bs128_531lr_ | unknown | unknown | 495 | 1182 | +687 |
110	| KnutJaegersberg/YaYi-30b-EverythingLM | yi | unknown | 887 | 1568 | +681 |
111	| Qwen/Qwen1.5-14B-Chat | qwen-1.5 | unknown | 591 | 1272 | +681 |
112	
113	### Biggest rank *gains* (hurt by DIF items)
114	
115	| Model | Family | Method | Rank Full | Rank Stable | ΔRank |
116	|-------|--------|--------|-----------|-------------|-------|
117	| liminerity/Blurstral-7b-slerp | unknown | unknown | 1410 | 823 | -587 |
118	| DreadPoor/PAIN_LeDestroy-7B-task_arithmetic | unknown | unknown | 1186 | 619 | -567 |
119	| flammenai/flammen26-mistral-7B | mistral | unknown | 1335 | 793 | -542 |
120	| Gille/StrangeMerges_2-7B-slerp | unknown | unknown | 1320 | 801 | -519 |
121	| jambroz/sixtyoneeighty-7b | unknown | unknown | 1270 | 782 | -488 |
122	| jambroz/sixtyoneeighty-7b-chat | unknown | unknown | 1271 | 783 | -488 |
123	| Gille/StrangeMerges_12-7B-slerp | unknown | unknown | 1347 | 860 | -487 |
124	| antiven0m/reverie-7b | unknown | unknown | 1288 | 805 | -483 |
125	| GreenNode/GreenNodeLM-7B-v2leo | unknown | unknown | 1333 | 852 | -481 |
126	| jambroz/sixtyoneeighty-7b-dpo | nan | DPO | 1303 | 835 | -468 |
127	| DreadPoor/Sphinx-7B-Model_Stock | unknown | unknown | 1282 | 817 | -465 |
128	| SanjiWatsuki/Kunoichi-DPO-7B | nan | DPO | 1314 | 857 | -457 |
129	| Inv/Konstanta-V4-Alpha-7B | unknown | unknown | 1231 | 777 | -454 |
130	| allknowingroger/LimyQstar-7B-slerp | unknown | unknown | 987 | 534 | -453 |
131	| mncai/mistral-7b-dpo-v6 | mistral-0.1 | DPO | 1202 | 756 | -446 |
132	| Gille/StrangeMerges_17-7B-dare_ties | unknown | unknown | 1491 | 1051 | -440 |
133	| Vasanth/Valor_Macaroni_moe | unknown | unknown | 1284 | 859 | -425 |
134	| flammenai/flammen27-mistral-7B | mistral | unknown | 939 | 523 | -416 |
135	| nbeerbower/bruphin-iota | unknown | unknown | 1215 | 803 | -412 |
136	| rishiraj/oswald-2x7b | unknown | unknown | 1731 | 1327 | -404 |
137	
138	
139	## Part 5: Cross-Cohort Super-Family Accuracy Shifts
140	
141	Super-families in both cohorts: 8
142	
143	- Mean |Δaccuracy| on full benchmark: 0.0900
144	- Mean |Δaccuracy| on stable items:   0.0863
145	- Mean |Δaccuracy| on DIF items:      0.0983
146	- Ratio stable/full: 0.9581
147	- Ratio DIF/full: 1.0919
148	- DIF items show *larger* cross-cohort accuracy swings → they capture temporal instability.
149	
150	| Super-family | N23 | N24 | Δacc full | Δacc stable | Δacc DIF |
151	|-------------|-----|-----|-----------|-------------|----------|
152	| hermes | 16 | 4 | +0.2978 | +0.2867 | +0.3222 |
153	| llama | 161 | 315 | +0.1206 | +0.1171 | +0.1282 |
154	| phi | 60 | 20 | +0.1092 | +0.0952 | +0.1397 |
155	| falcon | 21 | 1 | -0.0900 | -0.0938 | -0.0816 |
156	| wizardlm | 5 | 4 | +0.0593 | +0.0641 | +0.0489 |
157	| mistral | 547 | 120 | +0.0199 | +0.0114 | +0.0386 |
158	| qwen | 27 | 70 | -0.0198 | -0.0164 | -0.0272 |
159	| yi | 72 | 14 | +0.0038 | +0.0055 | +0.0000 |
160	
161	
162	## Key Findings
163	
164	1. **Ranking correlation (full vs stable-only)**: 2023 ρ=0.998851, 2024 ρ=0.997014
165	2. **Split-half reliability**: full=0.9934, stable=0.9919
166	3. **DIF removal vs random**: DIF removal caused more rank disruption than random in 21/21 conditions
167	4. **Average z-score (DIF vs random)**: -14.91
168	5. **Cross-cohort stability**: DIF items show 1.09× the accuracy shift of full benchmark; stable items show 0.96×
169	6. **Top-50 rank movers** dominant training methods: unknown (49), DPO (1)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9db9720a-e0da-46fb-858a-5b9ad31731e2",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "1f4af15d-f52b-4763-8214-b6d7610ef445",
  "sourceToolAssistantUUID": "9db9720a-e0da-46fb-858a-5b9ad31731e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T02:17:36.041Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P7cc9Vd7z8EYggfpjJpRN1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic/report/plan_016_report_fb64fc.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f4af15d-f52b-4763-8214-b6d7610ef445",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEunWnjyCKGhwRFaH279",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdfcf350-db4b-4dff-84aa-aa65f1a6ed82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rf4rXE8C8qxMEoCsvd9P7Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6037,
      "cache_read_input_tokens": 45926,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 45926,
          "cache_creation_input_tokens": 6037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6037,
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

_source line 37 · 2026-05-21T02:17:36.048Z_

<details><summary>↩ Tool result · `toolu_01P7cc9Vd7z8EYggfpjJpRN1`</summary>

```text
1	# Plan 016: Within-Subject Semi-Synthetic Injection
2	
3	## Objective
4	
5	Verify that MH-DIF detects differential contamination **within individual subjects**,
6	not just globally. This validates plan_014's finding that within-subject temporal
7	C% = 38.1% reflects real signal, not method failure.
8	
9	## Setup
10	
11	- **Temporal cohort**: ref=2023 (1080 models), foc=2024 (807 models)
12	- **Focal injection subset**: 787 models (ability overlap with ref)
13	- **Contamination fraction**: 20% of items per subject
14	- **Injection probabilities**: [0.0, 0.5, 1.0]
15	- **Seeds per p**: 5
16	- **Matching**: within-subject purified total score + cross-subject total score
17	
18	### Subjects
19	
20	| Subject | N items | N contaminated | N baseline | Strata |
21	|---------|---------|----------------|------------|--------|
22	| business_ethics | 93 | 18 | 75 | 3 |
23	| human_aging | 203 | 40 | 163 | 5 |
24	| professional_medicine | 248 | 49 | 199 | 5 |
25	| formal_logic | 109 | 21 | 88 | 5 |
26	| high_school_statistics | 181 | 36 | 145 | 5 |
27	
28	## Results: Within-Subject Matching
29	
30	Matching variable = purified total score on current subject's items (minus studied item).
31	
32	### Per-Subject Dose-Response (Within)
33	
34	| Subject | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
35	|---------|---|----------------|----------------|------|-----------|----------|
36	| business_ethics | 0.0 | 0.600±0.072 | 0.563±0.017 | +0.000 | 1.24 | 0.5990 |
37	| business_ethics | 0.5 | 0.522±0.084 | 0.603±0.017 | -0.078 | 0.78 | 0.5957 |
38	| business_ethics | 1.0 | 1.000±0.000 | 0.629±0.017 | +0.400 | inf | 0.0012 |
39	| formal_logic | 0.0 | 0.333±0.158 | 0.409±0.038 | +0.000 | 0.92 | 0.2169 |
40	| formal_logic | 0.5 | 0.790±0.080 | 0.500±0.033 | +0.457 | 4.21 | 0.0254 |
41	| formal_logic | 1.0 | 1.000±0.000 | 0.584±0.019 | +0.667 | inf | 0.0001 |
42	| high_school_statistics | 0.0 | 0.472±0.059 | 0.407±0.015 | +0.000 | 1.35 | 0.5720 |
43	| high_school_statistics | 0.5 | 0.667±0.065 | 0.494±0.010 | +0.194 | 2.14 | 0.1395 |
44	| high_school_statistics | 1.0 | 1.000±0.000 | 0.643±0.009 | +0.528 | inf | 0.0000 |
45	| human_aging | 0.0 | 0.315±0.045 | 0.334±0.011 | +0.000 | 0.94 | 0.5741 |
46	| human_aging | 0.5 | 0.700±0.085 | 0.405±0.019 | +0.385 | 3.68 | 0.0013 |
47	| human_aging | 1.0 | 1.000±0.000 | 0.507±0.033 | +0.685 | inf | 0.0000 |
48	| professional_medicine | 0.0 | 0.306±0.050 | 0.312±0.012 | +0.000 | 1.00 | 0.6056 |
49	| professional_medicine | 0.5 | 0.633±0.063 | 0.435±0.042 | +0.327 | 2.37 | 0.0063 |
50	| professional_medicine | 1.0 | 1.000±0.000 | 0.593±0.028 | +0.694 | inf | 0.0000 |
51	
52	## Results: Cross-Subject Matching
53	
54	Matching variable = total score on all other subjects' items (not affected by injection).
55	
56	### Per-Subject Dose-Response (Cross)
57	
58	| Subject | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
59	|---------|---|----------------|----------------|------|-----------|----------|
60	| business_ethics | 0.0 | 0.556±0.136 | 0.533±0.033 | +0.000 | 1.29 | 0.2948 |
61	| business_ethics | 0.5 | 0.611±0.056 | 0.533±0.033 | +0.056 | 1.43 | 0.4464 |
62	| business_ethics | 1.0 | 1.000±0.000 | 0.533±0.033 | +0.444 | inf | 0.0001 |
63	| formal_logic | 0.0 | 0.362±0.137 | 0.402±0.033 | +0.000 | 1.00 | 0.3243 |
64	| formal_logic | 0.5 | 0.905±0.089 | 0.402±0.033 | +0.543 | inf | 0.0000 |
65	| formal_logic | 1.0 | 1.000±0.000 | 0.402±0.033 | +0.638 | inf | 0.0000 |
66	| high_school_statistics | 0.0 | 0.400±0.046 | 0.335±0.012 | +0.000 | 1.35 | 0.5639 |
67	| high_school_statistics | 0.5 | 0.833±0.020 | 0.335±0.012 | +0.433 | 10.12 | 0.0000 |
68	| high_school_statistics | 1.0 | 1.000±0.000 | 0.335±0.012 | +0.600 | inf | 0.0000 |
69	| human_aging | 0.0 | 0.370±0.054 | 0.431±0.013 | +0.000 | 0.80 | 0.5940 |
70	| human_aging | 0.5 | 0.745±0.078 | 0.431±0.013 | +0.375 | 4.23 | 0.0003 |
71	| human_aging | 1.0 | 1.000±0.000 | 0.431±0.013 | +0.630 | inf | 0.0000 |
72	| professional_medicine | 0.0 | 0.376±0.069 | 0.380±0.017 | +0.000 | 1.03 | 0.6268 |
73	| professional_medicine | 0.5 | 0.755±0.050 | 0.380±0.017 | +0.380 | 5.32 | 0.0000 |
74	| professional_medicine | 1.0 | 1.000±0.000 | 0.380±0.017 | +0.624 | inf | 0.0000 |
75	
76	## Within vs Cross Matching Comparison
77	
78	| Subject | p | Within FPR | Cross FPR | Within TPR | Cross TPR |
79	|---------|---|------------|-----------|------------|-----------|
80	| business_ethics | 0.0 | 0.563 | 0.533 | 0.600 | 0.556 |
81	| business_ethics | 0.5 | 0.603 | 0.533 | 0.522 | 0.611 |
82	| business_ethics | 1.0 | 0.629 | 0.533 | 1.000 | 1.000 |
83	| human_aging | 0.0 | 0.334 | 0.431 | 0.315 | 0.370 |
84	| human_aging | 0.5 | 0.405 | 0.431 | 0.700 | 0.745 |
85	| human_aging | 1.0 | 0.507 | 0.431 | 1.000 | 1.000 |
86	| professional_medicine | 0.0 | 0.312 | 0.380 | 0.306 | 0.376 |
87	| professional_medicine | 0.5 | 0.435 | 0.380 | 0.633 | 0.755 |
88	| professional_medicine | 1.0 | 0.593 | 0.380 | 1.000 | 1.000 |
89	| formal_logic | 0.0 | 0.409 | 0.402 | 0.333 | 0.362 |
90	| formal_logic | 0.5 | 0.500 | 0.402 | 0.790 | 0.905 |
91	| formal_logic | 1.0 | 0.584 | 0.402 | 1.000 | 1.000 |
92	| high_school_statistics | 0.0 | 0.407 | 0.335 | 0.472 | 0.400 |
93	| high_school_statistics | 0.5 | 0.494 | 0.335 | 0.667 | 0.833 |
94	| high_school_statistics | 1.0 | 0.643 | 0.335 | 1.000 | 1.000 |
95	
96	### FPR Stability: Within vs Cross
97	
98	| Subject | Within FPR(p=0) | Within FPR(p=1) | ΔFPR(within) | Cross FPR(p=0) | Cross FPR(p=1) | ΔFPR(cross) |
99	|---------|-----------------|-----------------|--------------|----------------|----------------|-------------|
100	| business_ethics | 0.563 | 0.629 | +0.067 | 0.533 | 0.533 | +0.000 |
101	| human_aging | 0.334 | 0.507 | +0.173 | 0.431 | 0.431 | +0.000 |
102	| professional_medicine | 0.312 | 0.593 | +0.281 | 0.380 | 0.380 | +0.000 |
103	| formal_logic | 0.409 | 0.584 | +0.175 | 0.402 | 0.402 | +0.000 |
104	| high_school_statistics | 0.407 | 0.643 | +0.236 | 0.335 | 0.335 | +0.000 |
105	
106	### Subject-Level Summary
107	
108	| Subject | Matching | Baseline FPR (p=0) | TPR at p=0.5 | TPR at p=1.0 | ΔTPR(0.5) | ΔTPR(1.0) | Significant? |
109	|---------|----------|--------------------|--------------|--------------|-----------|-----------|-------------|
110	| business_ethics | within | 0.563 | 0.522 | 1.000 | -0.078 | +0.400 | No / Yes |
111	| business_ethics | cross | 0.533 | 0.611 | 1.000 | +0.056 | +0.444 | No / Yes |
112	| human_aging | within | 0.334 | 0.700 | 1.000 | +0.385 | +0.685 | Yes / Yes |
113	| human_aging | cross | 0.431 | 0.745 | 1.000 | +0.375 | +0.630 | Yes / Yes |
114	| professional_medicine | within | 0.312 | 0.633 | 1.000 | +0.327 | +0.694 | Yes / Yes |
115	| professional_medicine | cross | 0.380 | 0.755 | 1.000 | +0.380 | +0.624 | Yes / Yes |
116	| formal_logic | within | 0.409 | 0.790 | 1.000 | +0.457 | +0.667 | Yes / Yes |
117	| formal_logic | cross | 0.402 | 0.905 | 1.000 | +0.543 | +0.638 | Yes / Yes |
118	| high_school_statistics | within | 0.407 | 0.667 | 1.000 | +0.194 | +0.528 | No / Yes |
119	| high_school_statistics | cross | 0.335 | 0.833 | 1.000 | +0.433 | +0.600 | Yes / Yes |
120	
121	## Comparison with Plan 011 (Global)
122	
123	| Metric | Plan 011 temporal external | Plan 016 within (avg) | Plan 016 cross (avg) |
124	|--------|---------------------------|----------------------|---------------------|
125	| Baseline FPR | 0.314 | 0.405 | 0.416 |
126	| ΔTPR at p=0.5 | +0.508 | +0.257 | +0.357 |
127	| ΔTPR at p=1.0 | +0.674 | +0.595 | +0.587 |
128	
129	## Verdict
130	
131	**Within-subject matching**: 3/5 subjects with ΔTPR > 0.3 at p=0.5
132	**Cross-subject matching**: 4/5 subjects with ΔTPR > 0.3 at p=0.5
133	
134	Within-subject MH-DIF successfully detects injected differential contamination
135	in subjects with sufficient items. Cross-subject matching provides a cleaner
136	baseline FPR (not inflated by injection in the matching variable) while
137	maintaining detection sensitivity.
138	
139	Key findings:
140	
141	1. The DIF methodology works at the within-subject level
142	2. Plan 014's finding of ~38% within-subject temporal C% is methodologically valid
143	3. Cross-subject matching FPR is more stable across injection levels (not contaminated)
144	4. Within-subject matching FPR inflates with injection (matching variable includes injected items)
145	5. Very small subjects (N<100) have inflated baseline FPR due to limited matching variable precision
146	
147	## Implications
148	
149	The within-subject injection results, combined with plan_014's finding of ~38%
150	within-subject C%, support the final narrative: temporal DIF is a real, pervasive
151	phenomenon that persists even when ability matching is done within content domains.
152	Cross-subject matching confirms the FPR inflation in within-subject matching is due
153	to contamination of the matching variable, validating the use of external scores
154	for cleaner DIF estimation.
155	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdfcf350-db4b-4dff-84aa-aa65f1a6ed82",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "093b5dd6-af49-4e53-95bd-32936eea9428",
  "sourceToolAssistantUUID": "bdfcf350-db4b-4dff-84aa-aa65f1a6ed82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-21T02:17:39.080Z_

Now let me read the remaining key reports.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "093b5dd6-af49-4e53-95bd-32936eea9428",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEunxAE5mREwAQDa7vYV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ffbc0462-14b7-4148-8cc3-64971a349c28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BiSSJmvd4qx2NTKnnwSgz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9401,
      "cache_read_input_tokens": 51963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9401,
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

_source line 39 · 2026-05-21T02:17:41.530Z_

<details open><summary>🔧 Tool call — Read · `toolu_018TngNkELZz96Yavff9WL63`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/report/plan_001_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffbc0462-14b7-4148-8cc3-64971a349c28",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEunxAE5mREwAQDa7vYV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a82aa0d-98a4-48b0-8722-89f109baa79b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BiSSJmvd4qx2NTKnnwSgz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9401,
      "cache_read_input_tokens": 51963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9401,
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

_source line 40 · 2026-05-21T02:17:41.536Z_

<details><summary>↩ Tool result · `toolu_018TngNkELZz96Yavff9WL63`</summary>

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
  "parentUuid": "2a82aa0d-98a4-48b0-8722-89f109baa79b",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "2f7192fc-d3e3-4a0f-ac74-c3c2f791392c",
  "sourceToolAssistantUUID": "2a82aa0d-98a4-48b0-8722-89f109baa79b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T02:17:42.339Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PKpEvfMXagBtE84mqZYeZB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012_irt_theta_conditioning/report/plan_012_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f7192fc-d3e3-4a0f-ac74-c3c2f791392c",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEunxAE5mREwAQDa7vYV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c2734e3-b8e5-4c55-a8a2-875b803d19c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BiSSJmvd4qx2NTKnnwSgz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9401,
      "cache_read_input_tokens": 51963,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9401
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 210,
          "cache_read_input_tokens": 51963,
          "cache_creation_input_tokens": 9401,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9401,
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

_source line 42 · 2026-05-21T02:17:42.345Z_

<details><summary>↩ Tool result · `toolu_01PKpEvfMXagBtE84mqZYeZB`</summary>

````text
1	# Plan 012: IRT θ-Conditioning MH-DIF Analysis
2	
3	## 1. Objective
4	
5	Replace raw total scores with IRT-based θ estimates as the MH-DIF stratification
6	variable. Test whether finer ability matching reduces the high baseline FPR from
7	plan_011 (temporal ~31%, ability ~49%) while preserving detection power (TPR).
8	
9	## 2. θ Estimation Method
10	
11	**Method**: Logit of proportion correct with Laplace smoothing
12	```
13	θ = log((total + 0.5) / (N_items + 1 - total - 0.5))
14	```
15	- N models: 5227
16	- N items (full matrix): 12508
17	- θ range: [-3.310, 2.330]
18	- θ mean±std: 0.382±0.702
19	- Correlation(θ, total_score): 0.9986
20	
21	This is a monotone transformation of the Rasch model sufficient statistic.
22	Two binning strategies are compared:
23	- **Equal-width (eq)**: equal intervals on the logit scale — respects IRT metric
24	- **Quantile (qt)**: equal-count bins — ensures balanced strata
25	
26	## 3. Experimental Design
27	
28	- Baseline items: 500
29	- Contaminated per run: 100
30	- Injection probabilities: [0.0, 0.3, 0.5, 0.7, 1.0]
31	- Seeds per p: 5
32	- Strata counts tested: [10, 15, 20]
33	
34	### Cohort definitions
35	
36	- **ability**: ref N=2092, foc N=2089, foc inject N=2089
37	- **temporal**: ref N=1080, foc N=807, foc inject N=787
38	
39	### MH variants
40	
41	| Variant | Stratification | Description |
42	|---------|---------------|-------------|
43	| theta_eq_10 | Equal-width θ bins | 10 equal intervals on logit scale |
44	| theta_qt_10 | Quantile θ bins | 10 equal-count bins on θ |
45	| theta_eq_15 | Equal-width θ bins | 15 equal intervals on logit scale |
46	| theta_qt_15 | Quantile θ bins | 15 equal-count bins on θ |
47	| theta_eq_20 | Equal-width θ bins | 20 equal intervals on logit scale |
48	| theta_qt_20 | Quantile θ bins | 20 equal-count bins on θ |
49	| external_5 | Quantile total-score | 5 bins on full-matrix total (plan_011 baseline) |
50	
51	## 4. Semi-Synthetic Results
52	
53	### Temporal cohort
54	
55	#### Baseline FPR (p=0)
56	
57	| Variant | FPR (mean±std) |
58	|---------|----------------|
59	| external_5 | 0.314±0.009 |
60	| theta_eq_10 | 0.335±0.008 |
61	| theta_eq_15 | 0.310±0.012 |
62	| theta_eq_20 | 0.322±0.009 |
63	| theta_qt_10 | 0.352±0.015 |
64	| theta_qt_15 | 0.337±0.007 |
65	| theta_qt_20 | 0.312±0.008 |
66	
67	#### Dose-response (key variants)
68	
69	| Variant | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
70	|---------|---|----------------|----------------|------|-----------|----------|
71	| theta_eq_10 | 0.0 | 0.330±0.034 | 0.335±0.008 | +0.000 | 0.99 | 5.55e-01 |
72	| theta_eq_10 | 0.3 | 0.656±0.036 | 0.335±0.008 | +0.326 | 3.84 | 3.25e-09 |
73	| theta_eq_10 | 0.5 | 0.882±0.033 | 0.335±0.008 | +0.552 | 15.66 | 4.29e-25 |
74	| theta_eq_10 | 0.7 | 0.992±0.008 | 0.335±0.008 | +0.662 | inf | 7.45e-39 |
75	| theta_eq_10 | 1.0 | 1.000±0.000 | 0.335±0.008 | +0.670 | inf | 1.04e-39 |
76	| theta_qt_10 | 0.0 | 0.362±0.059 | 0.352±0.015 | +0.000 | 1.08 | 6.40e-01 |
77	| theta_qt_10 | 0.3 | 0.570±0.034 | 0.352±0.015 | +0.208 | 2.45 | 9.45e-05 |
78	| theta_qt_10 | 0.5 | 0.834±0.026 | 0.352±0.015 | +0.472 | 9.44 | 1.01e-17 |
79	| theta_qt_10 | 0.7 | 0.992±0.008 | 0.352±0.015 | +0.630 | inf | 3.79e-37 |
80	| theta_qt_10 | 1.0 | 1.000±0.000 | 0.352±0.015 | +0.638 | inf | 7.85e-38 |
81	| theta_qt_20 | 0.0 | 0.310±0.034 | 0.312±0.008 | +0.000 | 1.00 | 6.31e-01 |
82	| theta_qt_20 | 0.3 | 0.640±0.039 | 0.312±0.008 | +0.330 | 3.96 | 2.93e-09 |
83	| theta_qt_20 | 0.5 | 0.876±0.026 | 0.312±0.008 | +0.566 | 16.06 | 2.10e-25 |
84	| theta_qt_20 | 0.7 | 0.994±0.005 | 0.312±0.008 | +0.684 | inf | 2.30e-41 |
85	| theta_qt_20 | 1.0 | 1.000±0.000 | 0.312±0.008 | +0.690 | inf | 1.13e-41 |
86	| external_5 | 0.0 | 0.326±0.035 | 0.314±0.009 | +0.000 | 1.07 | 7.20e-01 |
87	| external_5 | 0.3 | 0.548±0.033 | 0.314±0.009 | +0.222 | 2.67 | 1.62e-05 |
88	| external_5 | 0.5 | 0.834±0.027 | 0.314±0.009 | +0.508 | 11.22 | 2.24e-21 |
89	| external_5 | 0.7 | 0.990±0.010 | 0.314±0.009 | +0.664 | inf | 1.47e-39 |
90	| external_5 | 1.0 | 1.000±0.000 | 0.314±0.009 | +0.674 | inf | 3.51e-42 |
91	
92	### Ability cohort
93	
94	#### Baseline FPR (p=0)
95	
96	| Variant | FPR (mean±std) |
97	|---------|----------------|
98	| external_5 | 0.493±0.010 |
99	| theta_eq_10 | 0.000±0.000 |
100	| theta_eq_15 | 0.514±0.010 |
101	| theta_eq_20 | 0.000±0.000 |
102	| theta_qt_10 | 0.093±0.004 |
103	| theta_qt_15 | 0.363±0.010 |
104	| theta_qt_20 | 0.079±0.007 |
105	
106	#### Dose-response (key variants)
107	
108	| Variant | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
109	|---------|---|----------------|----------------|------|-----------|----------|
110	| theta_eq_10 | 0.0 | 0.000±0.000 | 0.000±0.000 | +0.000 | nan | 1.00e+00 |
111	| theta_eq_10 | 0.3 | 0.000±0.000 | 0.000±0.000 | +0.000 | nan | 1.00e+00 |
112	| theta_eq_10 | 0.5 | 0.000±0.000 | 0.000±0.000 | +0.000 | nan | 1.00e+00 |
113	| theta_eq_10 | 0.7 | 0.000±0.000 | 0.000±0.000 | +0.000 | nan | 1.00e+00 |
114	| theta_eq_10 | 1.0 | 0.000±0.000 | 0.000±0.000 | +0.000 | nan | 1.00e+00 |
115	| theta_qt_10 | 0.0 | 0.088±0.018 | 0.093±0.004 | +0.000 | 0.96 | 8.46e-01 |
116	| theta_qt_10 | 0.3 | 0.140±0.037 | 0.093±0.004 | +0.052 | 1.63 | 2.00e-01 |
117	| theta_qt_10 | 0.5 | 0.206±0.047 | 0.093±0.004 | +0.118 | 2.58 | 2.83e-03 |
118	| theta_qt_10 | 0.7 | 0.402±0.047 | 0.093±0.004 | +0.314 | 6.65 | 6.92e-13 |
119	| theta_qt_10 | 1.0 | 0.544±0.022 | 0.093±0.004 | +0.456 | 11.71 | 1.68e-21 |
120	| theta_qt_20 | 0.0 | 0.086±0.026 | 0.079±0.007 | +0.000 | 1.15 | 1.00e+00 |
121	| theta_qt_20 | 0.3 | 0.112±0.036 | 0.079±0.007 | +0.026 | 1.54 | 4.37e-01 |
122	| theta_qt_20 | 0.5 | 0.210±0.047 | 0.079±0.007 | +0.124 | 3.17 | 2.07e-04 |
123	| theta_qt_20 | 0.7 | 0.406±0.044 | 0.079±0.007 | +0.320 | 8.13 | 1.92e-13 |
124	| theta_qt_20 | 1.0 | 0.544±0.022 | 0.079±0.007 | +0.458 | 14.15 | 6.70e-23 |
125	| external_5 | 0.0 | 0.498±0.041 | 0.493±0.010 | +0.000 | 1.04 | 5.03e-01 |
126	| external_5 | 0.3 | 0.662±0.044 | 0.493±0.010 | +0.164 | 2.07 | 5.07e-03 |
127	| external_5 | 0.5 | 0.756±0.041 | 0.493±0.010 | +0.258 | 3.31 | 5.63e-07 |
128	| external_5 | 0.7 | 0.792±0.034 | 0.493±0.010 | +0.294 | 4.04 | 5.65e-09 |
129	| external_5 | 1.0 | 0.800±0.038 | 0.493±0.010 | +0.302 | 4.30 | 5.43e-09 |
130	
131	## 5. Success Criteria Evaluation
132	
133	**Target**: baseline FPR < 0.10, TPR > 0.70 at p=0.5 (temporal cohort)
134	
135	- **theta_eq_10**: FPR=0.335 [FAIL], TPR@p=0.5=0.882 [PASS]
136	- **theta_qt_10**: FPR=0.352 [FAIL], TPR@p=0.5=0.834 [PASS]
137	- **theta_eq_15**: FPR=0.310 [FAIL], TPR@p=0.5=0.882 [PASS]
138	- **theta_qt_15**: FPR=0.337 [FAIL], TPR@p=0.5=0.870 [PASS]
139	- **theta_eq_20**: FPR=0.322 [FAIL], TPR@p=0.5=0.880 [PASS]
140	- **theta_qt_20**: FPR=0.312 [FAIL], TPR@p=0.5=0.876 [PASS]
141	- **external_5**: FPR=0.314 [FAIL], TPR@p=0.5=0.834 [PASS]
142	
143	## 6. Enrichment Against Li et al. Labels (No Injection)
144	
145	| Variant | Strata | Rate(contam) | Rate(clean) | Enrichment |
146	|---------|--------|-------------|-------------|------------|
147	| theta_eq_10 | 10 | 0.3325 | 0.3370 | 0.986 |
148	| theta_qt_10 | 10 | 0.3582 | 0.3605 | 0.994 |
149	| theta_eq_15 | 15 | 0.3264 | 0.3243 | 1.006 |
150	| theta_qt_15 | 15 | 0.3280 | 0.3376 | 0.972 |
151	| theta_eq_20 | 20 | 0.3297 | 0.3318 | 0.994 |
152	| theta_qt_20 | 20 | 0.3290 | 0.3297 | 0.998 |
153	| external_5 | 5 | 0.3092 | 0.3182 | 0.972 |
154	
155	(plan_001 reference: enrichment = 0.96 with 5-strata total-score MH)
156	
157	## 7. Analysis & Conclusions
158	
159	### θ vs total-score stratification
160	
161	- Plan_011 external (5 quantile strata, total score) FPR: 0.314
162	- Best θ variant (theta_eq_15) FPR: 0.310
163	- FPR difference: -0.003
164	
165	### Equal-width vs quantile binning
166	
167	- K=10: equal-width FPR=0.335, quantile FPR=0.352
168	- K=15: equal-width FPR=0.310, quantile FPR=0.337
169	- K=20: equal-width FPR=0.322, quantile FPR=0.312
170	
171	### Why FPR remains elevated
172	
173	Possible explanations if FPR stays high despite θ-conditioning:
174	1. Real DIF exists between cohorts — genuine differential item functioning
175	   (2023 vs 2024 models genuinely differ on certain items beyond overall ability)
176	2. Cohorts differ on dimensions not captured by a single θ parameter
177	   (e.g., training data composition, architecture effects)
178	3. The logit(p) θ estimate has correlation >.999 with raw total scores,
179	   so quantile bins on θ produce nearly identical strata to quantile bins on totals
180	4. MH-DIF's power to distinguish real DIF from ability confounding is limited
181	   when the grouping variable (year/quintile) correlates strongly with ability
182	
183	### Recommendations
184	
185	Based on these results:
186	
187	- theta_eq_10: FPR₀=0.335, TPR@0.5=0.882, TPR@1.0=1.000
188	- theta_qt_10: FPR₀=0.352, TPR@0.5=0.834, TPR@1.0=1.000
189	- theta_qt_20: FPR₀=0.312, TPR@0.5=0.876, TPR@1.0=1.000
190	- external_5: FPR₀=0.314, TPR@0.5=0.834, TPR@1.0=1.000
191	
192	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c2734e3-b8e5-4c55-a8a2-875b803d19c2",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "39f722c8-51c3-4d89-807f-c63e3b6139d0",
  "sourceToolAssistantUUID": "0c2734e3-b8e5-4c55-a8a2-875b803d19c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-21T02:17:45.535Z_

Now let me read the writing plan and any review context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39f722c8-51c3-4d89-807f-c63e3b6139d0",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEuoQR36vjFvTvr6PaHt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d502ed5-8650-4b95-9a3e-23f90ffe4f4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMCVppybY6m2oN2CPqtFGv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6759,
      "cache_read_input_tokens": 61364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6759,
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

_source line 44 · 2026-05-21T02:17:47.049Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017JHvHhDc3MQJ1x5pxTWa2L`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "writing_plan.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d502ed5-8650-4b95-9a3e-23f90ffe4f4d",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEuoQR36vjFvTvr6PaHt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db6cef2e-af3d-482c-85bf-d49250345f71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMCVppybY6m2oN2CPqtFGv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6759,
      "cache_read_input_tokens": 61364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6759,
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

_source line 45 · 2026-05-21T02:17:47.060Z_

<details><summary>↩ Tool result · `toolu_017JHvHhDc3MQJ1x5pxTWa2L`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/writing_plan.yaml\", \"content\": \"meta:\\n  venue: ICLR 2027\\n  track: main\\n  template: \\\"\\\"\\n  template_note: \\\"ICLR 2027 template not yet available locally; will download or reuse iclr2025 when entering Step 2\\\"\\n  page_limit: 9\\n  deadline: \\\"2026-10-01\\\"\\n  core_claim: >-\\n    Applying DIF to MMLU (5,227 models × 12,508 items) reveals 38% item-level\\n    functional instability across model generations, exposes a fundamental gap\\n    in contamination ground truth labels, and provides a semi-synthetic\\n    validation framework for item-level detectors.\\n  created_at: \\\"2026-05-20T23:45:00Z\\\"\\n  story_arc:\\n    hook: >-\\n      When we say \\\"Model B outperforms Model A on MMLU,\\\" we assume temporal\\n      comparability — but 38% of MMLU items function differently across model\\n      generations.\\n    gap: >-\\n      Existing contamination labels (web-overlap, n-gram) measure global\\n      exposure, not differential item functioning — every validation study\\n      using these labels has a blind spot. This is a fundamental validation\\n      methodology gap affecting the entire contamination detection field.\\n    insight: >-\\n      DIF detects differential contamination (semi-synthetic ΔTPR=+0.508) but\\n      temporal DIF is dominated by genuine capability evolution\\n      (enrichment≈1.0, within-subject C%=38.1%), and three structural\\n      corrections cannot separate them.\\n    mechanism: >-\\n      Semi-synthetic injection into real response matrices provides controlled\\n      ground truth; cross-subject matching eliminates FPR inflation (ΔFPR=0.000).\\n    evidence: >-\\n      38% items functionally unstable (plan_001/014); ΔTPR=+0.508 at p=0.5\\n      (plan_011); ΔFPR=0.000 cross-subject (plan_016); three improvements\\n      exhausted (plan_001b/012/014).\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 200\\n    core_bullets:\\n      - >-\\n        Problem: LLM benchmark scores assume temporal comparability, but\\n        item-level behavior may drift across model generations\\n      - >-\\n        Approach: Apply MH-DIF with ETS classification to METABENCH\\n        (5,227 models × 12,508 MMLU items)\\n      - >-\\n        Finding 1: 38% items functionally unstable across generations —\\n        genuine capability evolution, not statistical artifact (sanity\\n        check 0.18%, within-subject persistence 31-45%)\\n      - >-\\n        Finding 2: Web-overlap contamination labels do not capture\\n        differential contamination (enrichment≈1.0); semi-synthetic\\n        injection confirms DIF detection power (ΔTPR=+0.508 at p=0.5).\\n        Validation methodology gap affects entire field.\\n      - >-\\n        Finding 3: Semi-synthetic validation framework with cross-subject\\n        matching (ΔFPR=0.000) as reusable infrastructure; GSM8K replication\\n        confirms cross-benchmark portability (ΔTPR=+0.818)\\n      - >-\\n        Finding 4: DIF-flagged items concentrate cross-generational\\n        discriminative information — removing them disrupts rankings MORE\\n        than random removal (z=-8 to -49σ), while overall rankings stay\\n        robust (ρ>0.996). Cross-benchmark validation: DIF flags\\n        anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005)\\n        — DIF captures capability-discriminative items, not contamination.\\n        DIF is diagnostic lens, not item filter.\\n    dependencies: [experiments, method, discussion]\\n    registry_refs:\\n      - plan_001_real_data_dif_mmlu\\n      - plan_011_semi_synthetic_validation\\n      - plan_014_within_subject_dif\\n      - plan_016_within_subject_semi_synthetic\\n      - plan_017_downstream_impact\\n      - plan_004_gsm8k_cross_benchmark\\n\\n  - section: introduction\\n    word_budget: 1200\\n    core_bullets:\\n      - >-\\n        Hook: MMLU scores are treated as directly comparable across time —\\n        but 38% of items behave differently for 2024 vs 2023 model cohorts\\n        (ETS C DIF), and this persists within every subject domain\\n      - >-\\n        Gap: Contamination detection research validates against web-overlap\\n        labels, but these measure global exposure, not differential item\\n        functioning — a fundamental validation methodology gap. All work\\n        using web-overlap/n-gram labels as ground truth for item-level\\n        detectors (including Min-K%, n-gram methods) has the same blind\\n        spot.\\n      - >-\\n        Insight: Applying classical psychometric DIF to LLM benchmarks\\n        reveals that item-level behavioral differences are pervasive and\\n        structural — three correction attempts (matched-ability,\\n        θ-conditioning, bifactor pre-check) all fail, pointing to genuine\\n        capability evolution as the dominant source\\n      - >-\\n        Contributions: (C1) Benchmark temporal comparability concern —\\n        38% functional instability as empirical finding; (C2) Ground truth\\n        meta-critique — validation methodology gap in contamination\\n        detection literature; (C3) Semi-synthetic validation framework\\n        with cross-subject matching; (C4) DIF items concentrate\\n        discriminative information — diagnostic lens, not item filter\\n    dependencies: [experiments]\\n    figures: [fig_1_global_vs_differential]\\n    citation_hints:\\n      - \\\"METABENCH dataset citation\\\"\\n      - \\\"Li et al. (EMNLP 2024) web-overlap labels\\\"\\n      - \\\"Wang et al. (ICLR 2026) RL fragility — motivates psychometric approach\\\"\\n      - \\\"Growing Pains (Polo et al.) — positioning: they do score comparability, we do temporal stability characterization\\\"\\n\\n  - section: related_work\\n    word_budget: 800\\n    core_bullets:\\n      - >-\\n        Cluster 1: Contamination detection methods (Min-K%, ConStat, DVD,\\n        Self-Critique, n-gram baselines) — all validate against global\\n        exposure labels, not differential contamination; our meta-critique\\n        applies to their validation methodology\\n      - >-\\n        Cluster 2: IRT in LLM evaluation (Growing Pains, PSN-IRT, Hardy\\n        scalability, Lalor 2019, Vania 2021) — DEDICATED technical\\n        comparison with Growing Pains: they use anchor items for efficient\\n        extensible evaluation; our DIF diagnostic tells them WHICH anchor\\n        items are degrading across model generations. Mutual value: their\\n        framework + our diagnostic = monitored extensible evaluation.\\n        Complementary not competing. (R2-W2)\\n      - >-\\n        Cluster 3: DIF methodology and impact-vs-DIF literature (MH,\\n        ETS classification, Shealy & Stout 1993 SIBTEST, Clauser & Mazor\\n        1998 review, Zumbo 1999, Belzak 2020 small-sample) — our\\n        application context is novel; method itself is established; we\\n        acknowledge the impact-vs-DIF confound as central challenge\\n        (MISSING-REF-1)\\n      - >-\\n        Cluster 4: Benchmark design (LiveBench, dynamic benchmarks) — we\\n        characterize existing benchmarks psychometrically, they build new\\n        contamination-free ones\\n    dependencies: [introduction]\\n\\n  - section: method\\n    word_budget: 1400\\n    core_bullets:\\n      - >-\\n        3.1 Data: METABENCH response matrix (5,227 × 12,508) + Li et al.\\n        web-overlap labels (73.8% coverage, 9,229 items)\\n      - >-\\n        3.2 MH-DIF + ETS A/B/C classification — translate for ML audience:\\n        examinees→models, test items→benchmark questions, DIF→item-level\\n        behavioral anomaly conditional on ability. ETS thresholds: A\\n        (|Δ|<1.0), B (1.0≤|Δ|<1.5), C (|Δ|≥1.5)\\n      - >-\\n        3.3 Cohort designs: temporal (2023 vs 2024, N=1253/656),\\n        ability-quintile (Q1-2 vs Q4-5), within-family (Llama-2 N=161 vs\\n        Llama-3 N=308), within-subject (per-MMLU-subject DIF)\\n      - >-\\n        3.4 Semi-synthetic injection framework: select baseline-clean\\n        items (ETS A in uninjected data), inject contamination by flipping\\n        focal-group incorrect→correct responses at rate p ∈ {0.3,0.5,0.7,1.0},\\n        measure ΔTPR = TPR(injected) - TPR(baseline). Cross-subject\\n        matching: use total score on OTHER subjects as matching variable,\\n        avoiding matching variable contamination.\\n      - >-\\n        3.5 Diagnostics: Yen's Q3 for local independence, domain-specificity\\n        analysis (Spearman ρ between C% and accuracy improvement by subject)\\n    dependencies: []\\n    notation_table:\\n      θ: \\\"latent ability (IRT)\\\"\\n      Δ_MH: \\\"Mantel-Haenszel DIF statistic (log-odds ratio)\\\"\\n      p: \\\"exploitation rate in semi-synthetic injection\\\"\\n      \\\"C%\\\": \\\"percentage of items classified ETS C (large DIF)\\\"\\n      ΔTPR: \\\"TPR increase from injection over baseline\\\"\\n      ΔFPR: \\\"FPR change from injection (should be 0 for valid framework)\\\"\\n\\n  - section: experiments\\n    word_budget: 2500\\n    core_bullets:\\n      - >-\\n        4.1 Validation: DIF works under controlled conditions — power\\n        analysis with real MMLU IRT parameters, ETS C TPR=0.68-0.80 at\\n        N≥80 δ≥1.4, FPR=0.036-0.042, AUC 0.93-0.94\\n      - >-\\n        4.2 Temporal comparability concern: 31.3% ETS C (temporal), sanity\\n        random split 0.18%, within-family Llama-2v3 61.3% (ability\\n        confound), ability-quintile 2.9% (well-controlled), domain ρ=0.307\\n        (p=0.02). Within-subject C%=38.1% (31-45% across 5 subjects) —\\n        instability penetrates within every domain\\n      - >-\\n        4.3 Ground truth mismatch: enrichment=0.96 against Li et al.\\n        web-overlap labels; semi-synthetic ΔTPR=+0.508 (p=0.5), +0.674\\n        (p=1.0), clear dose-response; DIF WORKS for differential\\n        contamination but Li et al. labels are the wrong ground truth\\n      - >-\\n        4.4 Structural analysis — empirical observation that three\\n        structural improvements fail: (a) matched-ability enrichment\\n        0.94-1.04, (b) θ-conditioning r=0.9986 FPR unchanged at 31%,\\n        (c) within-subject pre-check C%=38.1% (bifactor not viable).\\n        Frame as: jointly constraining DIF utility, not formal impossibility\\n      - >-\\n        4.5 Semi-synthetic framework validation: cross-subject matching\\n        ΔFPR=0.000 all 5 subjects, 4/5 ΔTPR>0.3 at p=0.5 (cross), vs\\n        within-subject FPR inflation +0.186. Cross-subject matching as\\n        methodological recommendation.\\n      - >-\\n        4.6 Q3 local independence: 11.3% within-subject pairs >0.20 vs\\n        2.2% cross-subject (5x, p=2.3e-9); mild local dependence,\\n        contributing factor but not main FPR driver\\n      - >-\\n        4.7 Downstream impact — four layers: (1) Benchmark redundancy:\\n        ρ≈0.997 full vs stable-only, rankings extremely robust to 31%\\n        removal; (2) DIF items = discriminative signal carriers: DIF\\n        removal disrupts MORE than random (z=-8 to -49σ, 21/21),\\n        DIF items carry 1.09× cross-cohort swing vs 0.96× stable;\\n        (3) DIF as diagnostic lens: identifies which capability\\n        dimensions drive ranking shifts across generations. Model-specific\\n        patterns (phi-3/llama-3 +700-850, mistral merges -400 to -587)\\n        but caveat: top-50 movers 49/50 \\\"unknown\\\" family;\\n        (4) Cross-benchmark validation: GSM1K contamination gap\\n        anti-correlates with DIF advantage (r=−0.478, p=0.005) —\\n        contaminated models perform WORSE on DIF items, confirming DIF\\n        captures capability not contamination (N=33, partial r=−0.385,\\n        permutation p=0.014).\\n      - >-\\n        4.8 Cross-benchmark validation (GSM8K, 1,319 items × 6,702 models):\\n        Three-part analysis. (a) Temporal DIF: C%=18.9% (standard matching),\\n        sanity 0.3% — instability is lower than MMLU (31.3%) but still\\n        substantial for a single-domain benchmark. (b) Semi-synthetic:\\n        ΔTPR=+0.818 (standard, p=0.7), +0.517 (external, p=0.7); dose-\\n        response confirmed; framework generalizes beyond MMLU.\\n        (c) GSM1K contamination gap correlation: DIF-C items anti-correlate\\n        with contamination gap (r=−0.478, p=0.005; partial r=−0.385\\n        controlling accuracy; permutation p=0.014, N=33). Contaminated\\n        models (Phi, Gemma) perform WORSE on DIF items. DIF captures\\n        capability-discriminative items that contamination cannot fake.\\n    dependencies: []\\n    registry_refs:\\n      - mvp_dif_power_sim\\n      - mvp_dif_power_sim_phase2\\n      - plan_001_real_data_dif_mmlu\\n      - plan_001b_matched_ability_dif\\n      - plan_011_semi_synthetic_validation\\n      - plan_012_irt_theta_conditioning\\n      - plan_013_q3_local_independence\\n      - plan_014_within_subject_dif\\n      - plan_016_within_subject_semi_synthetic\\n      - plan_017_downstream_impact\\n      - plan_004_gsm8k_cross_benchmark\\n    tables: [tab_1_temporal_landscape, tab_2_structural_comparison]\\n    figures: [fig_2_dose_response, fig_3_within_subject_matching, fig_4_downstream_impact, fig_5_gsm8k_cross_benchmark]\\n\\n  - section: discussion\\n    word_budget: 1000\\n    core_bullets:\\n      - >-\\n        5.1 Implications for benchmark temporal comparability: 38%\\n        instability means cross-temporal MMLU scores carry uncontrolled\\n        item-level variance; benchmark designers should monitor DIF as\\n        quality diagnostic\\n      - >-\\n        5.2 Ground truth meta-critique — AGGRESSIVE framing per Director:\\n        all work validating item-level detectors against web-overlap/n-gram\\n        labels has the same validation methodology gap. Web-overlap measures\\n        existence, not differential usage. This is a meta-contribution to\\n        the contamination detection field — not just \\\"DIF and Li et al.\\n        measure different things\\\" but \\\"the field's standard validation\\n        approach is fundamentally mismatched for item-level detection.\\\"\\n      - >-\\n        5.3 Empirical observation on DIF applicability: 1D IRT fit\\n        limitations + power requirements + ability confounding jointly\\n        constrain DIF utility in LLM benchmarks. This is a structural\\n        constraint revealed by systematic experimentation, NOT a formal\\n        impossibility — higher-level methods (MIMIC, propensity-score\\n        matching, multidimensional IRT) may address individual constraints.\\n      - >-\\n        5.4 Limitations — MUST BE HONEST, non-negotiable:\\n        (a) ρ=0.307 means item instability correlates with capability\\n        improvement — \\\"unstable items\\\" may mainly reflect \\\"models got\\n        better at those domains\\\" rather than item-intrinsic problems;\\n        (b) 38% C% cannot be decomposed into contamination vs capability;\\n        (c) semi-synthetic injection (incorrect→correct flipping) may\\n        not match real contamination patterns (partial knowledge, format\\n        memorization);\\n        (d) primarily MMLU/METABENCH — GSM8K cross-validation (§4.8)\\n        confirms semi-synthetic framework portability and provides GSM1K\\n        correlation evidence (N=33), but full temporal DIF characterization\\n        on diverse benchmarks not yet done; GSM1K N=33 has wide CI;\\n        (e) cross-subject baseline FPR 33-53% — stable across injection\\n        levels but not low;\\n        (f) RL robustness: theoretically motivated but empirically\\n        unvalidated with adequate sample size (N=13 reasoning-RL models\\n        in METABENCH);\\n        (g) downstream impact family analysis limited to N≥20 families\\n        (llama, mistral, qwen, phi); top-50 rank movers 49/50 are\\n        \\\"unknown\\\" family — family-level conclusions have limited coverage\\n      - >-\\n        5.5 Future work: ensemble fusion (DIF + ConStat + DVD),\\n        broader cross-benchmark generalization (beyond GSM8K — e.g.\\n        ARC, HellaSwag, coding benchmarks), RL model cohorts with\\n        adequate N, item-focused trees (continuous covariate),\\n        SIBTEST/LR-DIF comparison, MIMIC models, GSM1K-style\\n        controlled item sets for more benchmarks\\n    dependencies: [experiments]\\n\\n  - section: conclusion\\n    word_budget: 350\\n    core_bullets:\\n      - >-\\n        Four contributions: (1) 38% MMLU items functionally unstable\\n        across model generations, (2) ground truth meta-critique —\\n        validation methodology gap in contamination detection, (3)\\n        semi-synthetic framework with cross-subject matching (cross-\\n        benchmark replication on GSM8K: ΔTPR=+0.818), (4) DIF as\\n        diagnostic lens — four-layer finding\\n      - >-\\n        Key message: LLM benchmarks need psychometric monitoring, not\\n        just score reporting — DIF reveals benchmark quality as a\\n        benchmark quality tool\\n      - >-\\n        DIF items concentrate discriminative information (removal disrupts\\n        rankings MORE than random, z=-8 to -49σ) and anti-correlate with\\n        contamination (r=−0.478) — DIF captures genuine capability\\n        differences that contamination cannot replicate\\n    dependencies: [experiments, discussion]\\n\\nvisualization_plan:\\n  - fig_id: fig_1_global_vs_differential\\n    type: conceptual\\n    tool: paperbanana\\n    description: >-\\n      Global vs Differential contamination concept diagram with ICC\\n      illustration — global exposure affects all models equally (no DIF),\\n      differential training data inclusion creates group-specific ICC\\n      shifts (DIF detected). Shows why enrichment≈1.0 is expected.\\n    narrative_intent: >-\\n      Web-overlap labels and DIF measure fundamentally different things:\\n      global exposure vs differential item functioning. Low enrichment is\\n      expected, not failure.\\n    design_notes:\\n      - >-\\n        Left panel: \\\"Global Contamination\\\" — item on Common Crawl since\\n        2020, both cohort ICCs overlap (no DIF), Li et al. labels it\\n        contaminated but DIF correctly reports no group difference\\n      - >-\\n        Right panel: \\\"Differential Contamination\\\" — item in focal\\n        cohort's training data only, ICCs diverge (DIF detected), Li\\n        et al. may or may not label it\\n      - >-\\n        Use ICC curves (S-shaped logistic) with shaded area between\\n        curves = DIF magnitude (Δ_MH)\\n      - \\\"Color: reference cohort blue, focal cohort orange (Okabe-Ito)\\\"\\n      - >-\\n        Bottom annotation connecting panels: \\\"Enrichment ≈ 1.0 because\\n        most MMLU items are globally contaminated (left), not\\n        differentially (right)\\\"\\n    placement: introduction\\n    aspect_ratio: \\\"16:9\\\"\\n\\n  - fig_id: fig_2_dose_response\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      Semi-synthetic dose-response: TPR vs exploitation rate p for\\n      temporal cohort with external/cross-subject matching, plus FPR\\n      stability panel\\n    narrative_intent: >-\\n      DIF detection power increases monotonically with contamination\\n      exploitation rate (clear dose-response), and cross-subject matching\\n      maintains perfectly stable FPR (ΔFPR=0.000) — controlled detection\\n      capability confirmed.\\n    design_notes:\\n      - \\\"x-axis: exploitation rate p ∈ {0, 0.3, 0.5, 0.7, 1.0}\\\"\\n      - >-\\n        Top panel: TPR lines — temporal_external (primary, solid blue),\\n        temporal_standard (dashed red, shows FPR inflation problem at\\n        high p)\\n      - >-\\n        Bottom panel (smaller): FPR vs p — external flat at ~0.31\\n        (ΔFPR=0.000), standard inflating from 0.30 to 0.62\\n      - \\\"Pattern A: light regime band at p<0.3 labeled 'below practical detection'\\\"\\n      - \\\"Dashed horizontal lines at baseline TPR (p=0) for reference\\\"\\n      - \\\"Annotate ΔTPR=+0.508 at p=0.5 on the primary line\\\"\\n    data_source: \\\"registry: plan_011_semi_synthetic_validation\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"3:4\\\"\\n\\n  - fig_id: fig_3_within_subject_matching\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      Within-subject semi-synthetic: 5 subjects comparing cross-subject\\n      vs within-subject matching on ΔTPR and ΔFPR\\n    narrative_intent: >-\\n      Cross-subject matching eliminates FPR inflation (ΔFPR=0.000 for\\n      all 5 subjects) while maintaining detection power — a practical\\n      methodological recommendation.\\n    design_notes:\\n      - >-\\n        Paired dot plot or grouped bars: 5 subjects on x-axis, sorted\\n        by cross-subject ΔTPR\\n      - >-\\n        Left panel: ΔTPR at p=0.5 — cross (filled circle) vs within\\n        (open circle), connected by line\\n      - >-\\n        Right panel: ΔFPR — cross all at 0.000 (flat line), within\\n        showing inflation (+0.067 to +0.281)\\n      - \\\"Reference line: ΔTPR=0.3 (success threshold), ΔFPR=0\\\"\\n      - >-\\n        Highlight business_ethics: high baseline FPR (0.53-0.56),\\n        negative within-subject ΔTPR, low cross-subject ΔTPR — the\\n        failure case\\n    data_source: \\\"registry: plan_016_within_subject_semi_synthetic\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"3:2\\\"\\n\\n  - fig_id: fig_4_downstream_impact\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      Model-level rank change scatter: full-benchmark rank vs\\n      stable-only rank, showing that DIF removal systematically\\n      disrupts rankings more than random removal. Annotate key model\\n      clusters (phi-3/llama-3 beneficiaries, mistral merge losers).\\n    narrative_intent: >-\\n      DIF-flagged items concentrate cross-generational discriminative\\n      information — removing them disrupts rankings MORE than random\\n      removal, revealing model-specific evolution patterns rather than\\n      benchmark noise.\\n    design_notes:\\n      - >-\\n        Scatter plot: x = full-benchmark rank, y = stable-only rank.\\n        Diagonal line (y=x) = no change. Points above = gained rank\\n        (benefited from DIF items), below = lost rank.\\n      - >-\\n        Color by model family or cohort (2023 blue, 2024 orange) if\\n        feasible; otherwise uniform gray with key models highlighted\\n      - >-\\n        Annotate clusters: phi-3 / llama-3 derivatives (large positive\\n        rank change, +700-850), mistral merges (large negative, -400\\n        to -587)\\n      - >-\\n        Inset or annotation box: ρ_full_vs_stable = 0.996, z_dif_vs_random\\n        = -14.9 (mean), DIF items 1.09× cross-cohort ratio\\n      - \\\"Reference diagonal dashed line y=x\\\"\\n      - \\\"Alternative: if scatter too dense, use hexbin or contour\\\"\\n    data_source: \\\"registry: plan_017_downstream_impact\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n\\n  - fig_id: fig_5_gsm1k_dif_correlation\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      GSM1K contamination gap vs DIF advantage scatter: 33 matched models,\\n      showing significant negative correlation (r=−0.478, p=0.005).\\n      Models with higher contamination (GSM8K−GSM1K gap) perform WORSE\\n      on DIF-C items — DIF captures capability, not contamination.\\n    narrative_intent: >-\\n      Cross-benchmark validation of Claim 4's \\\"DIF as diagnostic lens\\\":\\n      contaminated models cannot fake performance on DIF items, which\\n      capture genuine capability-discriminative differences. The negative\\n      correlation inverts the contamination narrative.\\n    design_notes:\\n      - >-\\n        Scatter: x = GSM8K−GSM1K contamination gap, y = DIF advantage\\n        (acc_DIF_C − acc_non_DIF). Regression line with 95% CI band.\\n      - >-\\n        Color by model family (Phi green, Gemma orange, Llama blue,\\n        Mixtral purple, DeepSeek red, Other gray)\\n      - \\\"Annotate: r=−0.478, p=0.005 (partial r=−0.385 ctrl accuracy)\\\"\\n      - \\\"Annotate key outlier: Deepseek-math-7b-rl (near zero on both)\\\"\\n      - >-\\n        Dashed horizontal line at DIF advantage = 0; most models below\\n        (DIF items are harder for all, but contaminated models worse)\\n      - \\\"Already generated by Agent Worker — may need style refinement\\\"\\n    data_source: \\\"registry: plan_004_gsm8k_cross_benchmark, artifacts/plan_004/gsm1k_dif_correlation.csv\\\"\\n    placement: experiments\\n    aspect_ratio: \\\"4:3\\\"\\n    source_file: \\\"artifacts/plan_004/fig_gsm1k_dif_correlation.pdf\\\"\\n\\n  - fig_id: fig_A1_subject_heatmap\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      Per-subject ETS C percentage for all 57 MMLU subjects (temporal\\n      cohort), showing pervasiveness of item instability\\n    narrative_intent: >-\\n      Item instability is pervasive across all MMLU subjects, not\\n      concentrated in a few — temporal DIF is a benchmark-wide phenomenon.\\n    design_notes:\\n      - \\\"Horizontal bar chart sorted by C%, all 57 subjects\\\"\\n      - >-\\n        Color-coded by domain group (STEM / humanities / social science\\n        / other) to show whether instability clusters by domain\\n      - \\\"Vertical dashed line at overall mean C% (31.3%)\\\"\\n      - >-\\n        Annotate subjects with known capability jumps (e.g.,\\n        abstract_algebra, college_mathematics)\\n    data_source: \\\"registry: plan_001_real_data_dif_mmlu\\\"\\n    placement: appendix\\n    aspect_ratio: \\\"1:2\\\"\\n\\n  - fig_id: fig_A2_q3_distribution\\n    type: statistical\\n    tool: matplotlib\\n    description: >-\\n      Q3 residual correlation distribution: within-subject vs\\n      cross-subject pairs\\n    narrative_intent: >-\\n      Local dependence exists (11.3% within-subject pairs exceed 0.20)\\n      but is mild — a contributing factor, not the main FPR driver.\\n    design_notes:\\n      - >-\\n        Overlapping density plot: within-subject Q3 (blue) vs\\n        cross-subject Q3 (orange)\\n      - \\\"Vertical dashed line at |Q3|=0.20 threshold\\\"\\n      - \\\"Annotate: 11.3% vs 2.2% above threshold (5x ratio)\\\"\\n      - \\\"Inset text: Mann-Whitney p=2.3e-9\\\"\\n    data_source: \\\"registry: plan_013_q3_local_independence\\\"\\n    placement: appendix\\n    aspect_ratio: \\\"4:3\\\"\\n\\ntable_plan:\\n  - table_id: tab_1_temporal_landscape\\n    caption: >-\\n      DIF detection results across cohort definitions on METABENCH MMLU\\n      (5,227 models × 12,508 items). ETS C = large DIF (|Δ_MH| ≥ 1.5).\\n    placement: experiments\\n    type: comparison\\n    columns:\\n      - Cohort Definition\\n      - N_ref / N_focal\\n      - \\\"ETS C (%)\\\"\\n      - \\\"FPR (Li clean)\\\"\\n      - Enrichment\\n    data_source: \\\"registry: plan_001_real_data_dif_mmlu, plan_014_within_subject_dif\\\"\\n    notes: >-\\n      Rows: temporal (2023 vs 2024), ability-quintile (Q1-2 vs Q4-5),\\n      within-family (Llama-2 vs Llama-3), random split (sanity check),\\n      within-subject average (5 subjects). Highlight contrast: sanity\\n      0.18% vs temporal 31.3%. Within-subject 38.1% proves instability\\n      penetrates within domains.\\n\\n  - table_id: tab_2_structural_comparison\\n    caption: >-\\n      Three structural improvement attempts and their outcomes. None\\n      reduces temporal baseline FPR below 31%.\\n    placement: experiments\\n    type: comparison\\n    columns:\\n      - Approach\\n      - Mechanism\\n      - Temporal FPR\\n      - \\\"TPR (p=0.5)\\\"\\n      - Outcome\\n    data_source: \\\"registry: plan_001b_matched_ability_dif, plan_012_irt_theta_conditioning, plan_014_within_subject_dif\\\"\\n    notes: >-\\n      Rows: baseline (plan_011 external matching), matched-ability\\n      quintiles (plan_001b), IRT θ-conditioning (plan_012), within-subject\\n      pre-check (plan_014). Frame as \\\"empirical observation revealing\\n      structural constraint\\\" not \\\"our method failed.\\\" Note: higher-level\\n      methods (MIMIC, propensity-score) may address individual constraints.\\n    baseline_row: \\\"Baseline (plan_011 external matching, FPR=0.314, TPR=0.834)\\\"\\n\\n  - table_id: tab_3_gsm8k_comparison\\n    caption: >-\\n      Cross-benchmark comparison: MMLU vs GSM8K on temporal DIF and\\n      semi-synthetic detection. GSM8K replicates key findings on a\\n      single-domain math benchmark (1,319 items × 6,702 models).\\n    placement: experiments\\n    type: comparison\\n    columns:\\n      - Metric\\n      - MMLU (plan_001/011)\\n      - GSM8K (plan_004)\\n    data_source: \\\"registry: plan_001_real_data_dif_mmlu, plan_011_semi_synthetic_validation, plan_004_gsm8k_cross_benchmark\\\"\\n    notes: >-\\n      Rows: Items / Models / Temporal C% / Sanity C% / Semi-synthetic\\n      ΔTPR (standard, p=0.7) / ΔTPR (external, p=0.5) / Baseline FPR\\n      (external) / GSM1K gap correlation (GSM8K only). Highlight: GSM8K\\n      standard ΔTPR=+0.818 vs MMLU external ΔTPR=+0.508. Different\\n      matching strategies make direct comparison nuanced — note in caption.\\n\\n  - table_id: tab_A1_power_analysis\\n    caption: >-\\n      DIF power analysis: ETS C classification performance with real\\n      MMLU IRT parameters across sample sizes and effect sizes.\\n    placement: appendix\\n    type: statistics\\n    columns:\\n      - N per group\\n      - \\\"δ (logits)\\\"\\n      - TPR (ETS C)\\n      - FPR (ETS C)\\n      - AUC (MH)\\n      - AUC (LR)\\n    data_source: \\\"registry: mvp_dif_power_sim, mvp_dif_power_sim_phase2\\\"\\n    notes: >-\\n      Grid: N ∈ {50, 80, 100} × δ ∈ {1.0, 1.2, 1.4, 1.6}. Operational\\n      region: N≥80, δ≥1.4 (TPR 0.68-0.80, FPR 0.036-0.042).\\n\\n  - table_id: tab_A2_within_subject_detail\\n    caption: >-\\n      Per-subject semi-synthetic validation with cross-subject vs\\n      within-subject matching at p=0.5.\\n    placement: appendix\\n    type: comparison\\n    columns:\\n      - Subject\\n      - N items\\n      - \\\"Baseline FPR (cross)\\\"\\n      - \\\"ΔTPR (cross)\\\"\\n      - \\\"Baseline FPR (within)\\\"\\n      - \\\"ΔTPR (within)\\\"\\n      - \\\"ΔFPR (cross)\\\"\\n    data_source: \\\"registry: plan_016_within_subject_semi_synthetic\\\"\\n    notes: >-\\n      5 subjects: business_ethics, human_aging, professional_medicine,\\n      formal_logic, high_school_statistics. Cross-subject ΔFPR=0.000 for\\n      all subjects. business_ethics is failure case (baseline FPR>0.53\\n      both methods).\\n\\nliterature_strategy:\\n  citation_budget: 40\\n  macro_context:\\n    - \\\"LLM benchmark contamination detection and validation methodology\\\"\\n    - \\\"psychometric methods (IRT, DIF) applied to LLM evaluation\\\"\\n    - \\\"benchmark temporal comparability and dynamic evaluation design\\\"\\n  micro_clusters:\\n    - cluster_name: \\\"Contamination Detection Methods\\\"\\n      search_queries:\\n        - \\\"benchmark contamination detection LLM 2024 2025 2026\\\"\\n        - \\\"Min-K++ training data detection language model\\\"\\n        - \\\"ConStat perturbation contamination benchmark\\\"\\n        - \\\"n-gram overlap contamination benchmark LLM\\\"\\n      must_cite:\\n        - \\\"Wang et al. 2026 RL fragility (ICLR 2026)\\\"\\n        - \\\"Liang et al. 2026 DVD generation variance\\\"\\n        - \\\"Tao et al. 2026 Self-Critique (ICLR 2026)\\\"\\n        - \\\"Li et al. EMNLP 2024 web-overlap labels\\\"\\n        - \\\"Shi et al. 2024 Min-K++\\\"\\n        - \\\"Balloccu et al. 2024\\\"\\n      target_count: 10\\n\\n    - cluster_name: \\\"IRT in LLM Evaluation\\\"\\n      search_queries:\\n        - \\\"item response theory LLM evaluation 2024 2025 2026\\\"\\n        - \\\"Growing Pains fixed parameter calibration benchmark\\\"\\n        - \\\"psychometric analysis language model benchmark\\\"\\n      must_cite:\\n        - \\\"Polo et al. 2026 Growing Pains\\\"\\n        - \\\"Polo et al. 2026 PSN-IRT (AAAI)\\\"\\n        - \\\"Hardy et al. 2026 scalability coefficients\\\"\\n        - \\\"Lalor et al. 2019 IRT for NLP\\\"\\n        - \\\"Vania et al. 2021\\\"\\n      target_count: 8\\n\\n    - cluster_name: \\\"DIF Methodology & Impact-vs-DIF\\\"\\n      search_queries:\\n        - \\\"differential item functioning Mantel-Haenszel ETS classification\\\"\\n        - \\\"impact versus DIF Shealy Stout SIBTEST\\\"\\n        - \\\"DIF small sample logistic regression\\\"\\n        - \\\"Zumbo 1999 DIF\\\"\\n      must_cite:\\n        - \\\"Holland & Thayer 1988 MH-DIF\\\"\\n        - \\\"Shealy & Stout 1993 SIBTEST\\\"\\n        - \\\"Clauser & Mazor 1998 DIF review\\\"\\n        - \\\"Zumbo 1999 DIF overview\\\"\\n        - \\\"Belzak 2020 small-sample DIF\\\"\\n        - \\\"Kim & Kolen 2019 fixed parameter calibration\\\"\\n      target_count: 8\\n\\n    - cluster_name: \\\"Benchmark Design & Ground Truth\\\"\\n      search_queries:\\n        - \\\"contamination-free benchmark LLM LiveBench 2025\\\"\\n        - \\\"benchmark ground truth contamination labels validation\\\"\\n        - \\\"GSM1K GSM8K contamination evidence\\\"\\n      must_cite:\\n        - \\\"White et al. 2025 LiveBench (ICLR)\\\"\\n        - \\\"Zhang et al. 2024 GSM1K\\\"\\n        - \\\"METABENCH original paper\\\"\\n      target_count: 6\\n\\n    - cluster_name: \\\"LLM Evaluation Methodology\\\"\\n      search_queries:\\n        - \\\"LLM evaluation methodology benchmark design 2025 2026\\\"\\n        - \\\"MMLU benchmark psychometric analysis\\\"\\n        - \\\"language model evaluation survey\\\"\\n      must_cite: []\\n      target_count: 5\\n\\nwriting_order:\\n  - experiments\\n  - method\\n  - introduction\\n  - related_work\\n  - discussion\\n  - abstract\\n  - conclusion\\n\", \"total_chars\": 31764, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db6cef2e-af3d-482c-85bf-d49250345f71",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "48549c11-b1ce-40a3-83d3-2c70fc5e3036",
  "sourceToolAssistantUUID": "db6cef2e-af3d-482c-85bf-d49250345f71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-21T02:17:47.336Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011kKcRXpAh39FhMQBq1JhsK`</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "paper_checklist.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48549c11-b1ce-40a3-83d3-2c70fc5e3036",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEuoQR36vjFvTvr6PaHt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c0f745f1-f1f1-4b18-a59f-c69dcb50dad7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AMCVppybY6m2oN2CPqtFGv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6759,
      "cache_read_input_tokens": 61364,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6759
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 61364,
          "cache_creation_input_tokens": 6759,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6759,
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

_source line 47 · 2026-05-21T02:17:47.343Z_

<details><summary>↩ Tool result · `toolu_011kKcRXpAh39FhMQBq1JhsK`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'irt_equated_bench_regen'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0f745f1-f1f1-4b18-a59f-c69dcb50dad7",
  "isSidechain": true,
  "promptId": "cbf20591-5ec1-4944-9358-f71a0fd8078e",
  "agentId": "ab7cf5d98411afbbc",
  "type": "user",
  "uuid": "07c38230-5296-4b55-a778-a04fa44c7a7b",
  "sourceToolAssistantUUID": "c0f745f1-f1f1-4b18-a59f-c69dcb50dad7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-21T02:19:24.646Z_

Now I have a thorough understanding of all experiments, results, methods, framing, and the decision chain. Let me compose the review.

## R1 Review: Methods and Experiments

### Summary

This paper applies Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis to the METABENCH response matrix (5,227 models x 12,508 MMLU items) and claims that 38% of MMLU items are "functionally unstable" across model generations. After the original contamination-detection hypothesis failed (enrichment ~1.0 against Li et al. labels), the paper pivoted to characterizing benchmark item instability, introducing a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000) and presenting a GSM1K-based cross-benchmark correlation (r=-0.478). The paper is methodologically competent in its application of classical psychometrics to LLM benchmarks, but several core claims rest on weak statistical foundations or conflate inability to falsify with positive evidence.

### Strengths

1. **Scale and thoroughness of the investigation.** 12 experiments forming a coherent decision chain, with each negative result motivating the next analysis, is exemplary scientific practice. The 5,227 x 12,508 response matrix is the largest-scale DIF analysis applied to LLM benchmarks. The exhaustive pursuit of three structural corrections (matched-ability, theta-conditioning, bifactor pre-check) before pivoting adds credibility.

2. **Semi-synthetic validation framework is well-designed.** Injecting known differential contamination (focal-group-only incorrect-to-correct flips) into real response matrices at controlled rates p in {0.3, 0.5, 0.7, 1.0} and measuring ΔTPR provides a rigorous internal validity check. The clear dose-response relationship (monotonically increasing TPR with exploitation rate) and the use of Fisher's exact test with appropriate multiple seed averaging (5 seeds per condition) are sound.

3. **Cross-subject matching as FPR control.** The observation that using total scores on OTHER subjects as the MH matching variable yields ΔFPR=0.000 across all 5 tested subjects while within-subject matching inflates FPR by +0.067 to +0.281 is a clean methodological finding. This addresses the matching variable contamination problem in a principled way and constitutes a practical, reusable recommendation.

4. **Sanity checks are convincing.** Random half-split of the 2023 cohort yielding 0.18% C% (vs. 31.3% temporal) provides strong evidence that the temporal DIF signal is not a statistical artifact of the MH procedure itself.

5. **Honest reporting of negative results.** The paper does not hide its failures: enrichment ~1.0, matched-ability DIF failure, theta-conditioning equivalence to total score (r=0.9986), within-subject C% exceeding global C%. This transparency is commendable and rare.

6. **Downstream impact analysis reveals a non-obvious finding.** The result that DIF removal causes MORE ranking disruption than random removal (z=-8 to -49σ across 21/21 conditions) inverts the naive expectation and supports the "diagnostic lens" reframing.

### Weaknesses

1. **(Major) The 31-38% temporal C% is fundamentally uninterpretable.** The paper's headline finding -- that 38% of MMLU items exhibit "functional instability" -- cannot be decomposed into contamination, genuine capability improvement, or statistical artifacts of the multidimensional ability structure. The authors acknowledge this (ρ=0.307 with domain accuracy improvement), but the paper still frames this as a contribution. A C% of 31% means the MH procedure flags nearly one in three items as exhibiting large DIF -- this is either (a) a staggeringly high true instability rate, or (b) a signal that the unidimensionality assumption is severely violated and the MH procedure is detecting multidimensional ability differences rather than item-level anomalies. The within-subject C% of 38.1% does not resolve this because within-subject DIF could still reflect multidimensional ability differences WITHIN domains (e.g., procedural vs. conceptual knowledge in professional_medicine). The paper cannot distinguish these explanations, which limits the interpretive value of the headline number.

2. **(Major) GSM1K validation is underpowered and the causal interpretation is overreached.** N=33 matched models is small. The leave-one-out analysis shows that removing Deepseek-math-7b-rl cuts the correlation by 22% (from -0.478 to -0.374), and the bootstrap CI reported in the summary [-0.71, -0.12] is extremely wide. The partial correlation (r=-0.385, p=0.027) barely survives at alpha=0.05 with 30 degrees of freedom. More critically, the paper claims DIF captures "capability-discriminative items that contamination cannot fake" -- but the negative correlation could equally reflect that high-contamination models have shallow knowledge that fails on difficult items regardless of their DIF status. The DIF-C items happen to be harder (all models except one show negative DIF advantage), so the correlation may reflect item difficulty confounding rather than a deep property of DIF flags.

3. **(Major) Baseline FPR of 31-53% undermines practical utility.** Across all matching variants and cohort definitions, the baseline FPR never drops below 30% for temporal cohorts. This means that even before any contamination is injected, roughly one-third of items are already flagged. The ΔTPR metric partially addresses this by measuring the incremental detection, but for a practitioner wanting to use DIF to identify problematic items in a real benchmark, the signal-to-noise ratio is extremely poor. The paper's reframing as "diagnostic lens" rather than "detection tool" acknowledges this but does not solve it -- a diagnostic lens that flags one-third of items as anomalous has limited actionable value.

4. **(Moderate) Semi-synthetic injection mechanism is too simplistic.** The incorrect-to-correct flipping mechanism assumes contamination produces uniform performance improvement across all contaminated items in the focal group. Real contamination patterns are more nuanced: partial memorization, format-dependent recall, chain-of-thought interference, and varying exposure levels across items. The ΔTPR=+0.508 at p=0.5 may overestimate detection power for realistic contamination patterns and underestimate it for others. No sensitivity analysis on the injection mechanism (e.g., partial flips, difficulty-dependent flip rates, asymmetric flips) is provided.

5. **(Moderate) Unidimensionality violation is acknowledged but not adequately addressed.** The IRT fit indices reported (RMSEA=0.092, CFI=0.81, TLI=0.78 for the decoder-only subset; RMSEA=0.11, CFI=0.72, TLI=0.68 for bifactor) all fail standard psychometric thresholds (RMSEA < 0.06, CFI > 0.95, TLI > 0.95). MH-DIF is a non-parametric procedure that does not require IRT model fit, but it DOES require that the matching variable adequately captures the latent ability being compared. When the construct is multidimensional (57 MMLU subjects testing distinct knowledge domains), matching on a unidimensional total score conflates between-dimension ability differences with within-dimension item-level DIF. The Q3 analysis (plan_013) shows 11.3% of within-subject item pairs exceed the 0.20 threshold, with moral_scenarios at 34.2% -- this suggests meaningful local dependence that could inflate DIF detection rates.

6. **(Moderate) Architecture stratification analysis (Experiment 2) adds little.** Restricting to decoder-only models (N=3,400) yields C%=33.1% vs. 31.3% for the full population -- a 1.8pp difference that is within noise. The IRT fit analysis confirms what is already known: MMLU is multidimensional. This experiment does not substantively advance any claim.

7. **(Minor) Reporting inconsistencies in the paper summary.** The paper summary mentions experiments (Exp 5-12) with results (graceful degradation, IFT, Bayesian DIF, RL robustness, ConStat comparison, DVD, ensemble fusion, bifactor IRT, item generation) that do not appear in the actual experimental artifacts. If these are "imagined experiments" from a review context rather than actual results, presenting them alongside real results is misleading. If they are real, the experimental reports should be available.

8. **(Minor) Cross-subject matching tested on only 5 subjects.** The ΔFPR=0.000 claim is based on 5 out of 57 MMLU subjects, including one clear failure case (business_ethics, with baseline FPR > 0.53 and negative within-subject ΔTPR at p=0.5). The selection of these 5 subjects (business_ethics, human_aging, professional_medicine, formal_logic, high_school_statistics) appears to be based on having high C% rates in plan_001, which may bias toward subjects where DIF is easiest to detect. Generalization to all 57 subjects is not established.

9. **(Minor) The "ground truth meta-critique" overstates novelty.** The observation that web-overlap labels measure global exposure rather than differential contamination is conceptually straightforward once stated. The contribution is the empirical demonstration (enrichment ~1.0), but the framing as "a fundamental validation methodology gap affecting the entire contamination detection field" is aggressive for what amounts to noting that two different things measure different things.

### Questions for Authors

1. Can you provide a formal argument or simulation showing what temporal C% would be expected under the null hypothesis that 2024 models are simply higher-ability versions of 2023 models on a truly unidimensional test? This would help calibrate whether 31% is "surprisingly high" or "expected given the ability gap."

2. For the GSM1K analysis (N=33): what happens if you restrict to models within the same family (e.g., only Llama variants, only Phi variants)? The between-family confound (different architectures, training data, etc.) could drive the correlation rather than a contamination-specific mechanism.

3. The DIF advantage (acc_DIF_C - acc_non_DIF) is negative for 32 of 33 models. This suggests DIF-C items are systematically harder. Did you control for item difficulty in the DIF-contamination correlation? A partial correlation controlling for mean item difficulty (not just overall model accuracy) would strengthen the causal claim.

4. How sensitive are the temporal C% results to the choice of temporal cutoff? What happens with 2023-Q1 vs 2023-Q2, or 2024-Q1 vs 2024-Q2? If C% scales with the temporal gap, this would support the "genuine capability evolution" interpretation; if it plateaus, it would suggest a more item-intrinsic phenomenon.

5. The within-family analysis (Llama-2 vs Llama-3, C%=61.3%) is presented as evidence of impact-vs-DIF confounding, but could this not also be interpreted as evidence that DIF IS detecting genuine architectural/training differences? What makes this "confounding" rather than "the signal"?

6. You acknowledge SIBTEST and MIMIC as alternative DIF methods that handle multidimensionality better. Given that unidimensionality violation is the central methodological concern, why were these not attempted? Even a preliminary SIBTEST analysis on a subset of subjects would substantially strengthen the paper.

### Missing Experiments or Analyses

1. **Null-model simulation for expected C% under ability differences.** Simulate a unidimensional 2PL model where the focal group has systematically higher theta, and compute the expected C% under MH-DIF. This would establish whether 31% is anomalously high or a predictable artifact of ability differences under the MH procedure.

2. **Item difficulty confounding in GSM1K correlation.** Partial correlation of contamination gap with DIF advantage, controlling for mean item difficulty (proportion correct), not just overall model accuracy.

3. **SIBTEST or logistic regression DIF on a subset.** Apply at least one DIF method that explicitly models multidimensional ability (SIBTEST separates target and suspected dimensions) on the 5 within-subject subjects to see if C% decreases.

4. **Temporal cutoff sensitivity analysis.** Vary the temporal split point to establish the dose-response of C% with temporal distance between cohorts.

5. **Effect of model count imbalance.** The temporal cohort has 1,080 vs 807 models -- check whether subsampling the reference group to equalize N changes C%.

6. **Comparison of DIF flags across difficulty quantiles.** Are DIF-C items concentrated among easy items, hard items, or uniformly distributed? This would inform the "capability improvement" interpretation.

### Preliminary Score: 4/6
### Confidence: 4/5

**Justification:** The paper is a competent, thorough application of classical psychometrics to LLM benchmarks with several valuable contributions: the semi-synthetic validation framework, the cross-subject matching insight, and the empirical characterization of MMLU item instability at scale. However, the headline finding (38% instability) remains fundamentally ambiguous between genuine item-level anomalies and multidimensional ability confounding that the MH procedure cannot resolve. The GSM1K validation is too underpowered to carry the weight placed on it, and the practical utility of a diagnostic tool with 31% baseline FPR is unclear. The paper would benefit substantially from a null-model calibration and at least one multidimensionality-aware DIF method. These are addressable weaknesses, and conditional on adequate responses, this could move to a 5. The score of 4 (Weak Accept) reflects that the contributions, while solid, are incremental rather than transformative -- the core insight (items behave differently across model generations) is expected once stated, and the methodological apparatus, while carefully executed, yields uncertain conclusions about the underlying mechanisms.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07c38230-5296-4b55-a778-a04fa44c7a7b",
  "isSidechain": true,
  "agentId": "ab7cf5d98411afbbc",
  "requestId": "req_011CbEuomrssm1oQZTWmFmLM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d4cc846-c1c6-4fb6-bb20-5e2c14630c1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "f077ac60-b5f3-45fc-82ab-a50de5ad3465",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01915YjiDwA6VuYPFa2Jq9DK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11095,
      "cache_read_input_tokens": 68123,
      "output_tokens": 3339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11095
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3339,
          "cache_read_input_tokens": 68123,
          "cache_creation_input_tokens": 11095,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11095,
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
