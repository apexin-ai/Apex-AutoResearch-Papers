# Research conversation: You are Reviewer 1 (R1) for a top ML venue review. Your focus is **Methods and Experiments**. ## Paper Summary "EC-HTE: 

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a4fde7b158b599326.jsonl`
- **Structured JSON:** [`c5a74f6419966641e9bb.json`](../../sessions/c5/c5a74f6419966641e9bb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

46 recorded events

### User

_source line 1 · 2026-05-20T20:26:50.059Z_

You are Reviewer 1 (R1) for a top ML venue review. Your focus is **Methods and Experiments**.

## Paper Summary
"EC-HTE: Error-Corrected Heterogeneous Treatment Effect Estimation Under Subgroup-Varying LLM Misclassification"

The paper identifies a bias mechanism in LLM-assisted heterogeneous treatment effect (HTE) analysis: when LLM misclassification rates vary across subgroups, applying a global (pooled) confusion-matrix correction amplifies subgroup CATE bias by up to 4× in high-heterogeneity regimes. The bias is proportional to Δπ × Δτ (misclassification heterogeneity × CATE heterogeneity). They propose EC-HTE, a hierarchical Bayesian framework using Dirichlet-prior confusion matrices with partial pooling for subgroup-stratified correction. They also derive a diagnostic screening tool (AUC=0.82). Experiments span synthetic, semi-synthetic (political tweets with GPT-4.1/Qwen3-235B), and real data (Rohingya refugee interviews).

## Key Method Details (Section 3-4)
- Bias characterization for K=2: Bias_global(τ̂_k) ∝ Δπ × Δτ. First-order approximation, R²=0.89 on synthetic grid. For K>2, sum-of-products form with R²=0.76 (K=4), acknowledged as Remark not Theorem.
- HB model: c_k ~ Dirichlet(α_k), α_k = α_0 · c̄ + 1. Hyperprior on α_0. MCMC via PyMC NUTS, 4 chains, 1500 warmup, 1000 draws.
- Stratified CATE correction: posterior draws of confusion matrix → invert → corrected CATE per draw → posterior mean + credible intervals.
- "Never worse than global" guarantee: partial pooling shrinks to global when subgroup data sparse, converges to subgroup MLE when abundant. Empirically verified: 0% of 1000 MC reps where HB worse than global.
- Diagnostic: Δπ × Δτ product as binary classifier for "global correction is harmful". AUC=0.82, transfers from synthetic (0.82) → semi-synthetic (0.79) → real (0.78).
- CausalForestDML integration: post-hoc correction to subgroup-level aggregates.

## Experiment Design Reference (what was planned)
11 experiments were planned:
1. exp-001: HB Synthetic Validation (regime sweep, n=100-2000, K=2,4) → covered in Sec 6.1
2. exp-002: Bias Bound Verification (R² of analytic formula) → covered in Sec 3.2
3. exp-003: Semi-Synthetic Political Science (GPT-4.1 + Qwen3, 12K tweets, 500 expert) → covered in Sec 6.2
4. exp-004: Real-Data Ashwin et al. (1800 interviews, 400 expert, 5-class) → covered in Sec 6.3
5. exp-005: Diagnostic Criterion (ROC analysis) → covered in Sec 5
6. exp-006: Expert Label Budget (n sweep × K sweep) → covered in Sec 6.4
7. exp-007: PPCI Comparison (error type disaggregation) → covered in Sec 6.5
8. exp-008: Multiple LLM Comparison (3 LLMs + ensemble) → covered in Sec 6.6
9. exp-009: Adaptive Allocation → covered in Sec 6.9
10. exp-010: Robustness to Misspecification → covered in Sec 6.7
11. exp-011: Causal Forest Integration → covered in Sec 6.8

## Paper Tables (from the PDF)
- Table 1: Analytic bias bound R² by K and model spec (K=2: R²=0.89; K=4: R²=0.76-0.88)
- Table 2: Bias amplification by regime (extreme: 4.2±0.3, moderate: 2.3±0.2, mild: 1.4±0.1, homogeneous: 1.05±0.05)
- Table 3: Diagnostic ROC operating points (high sens: 0.90/0.55; balanced: 0.75/0.72; high spec: 0.55/0.90)
- Table 4: Diagnostic AUC by metric/source (product: 0.82/0.79/0.78; Δπ only: 0.73/0.71/0.70)
- Table 5: HB vs MLE vs Laplace K=2 (HB/MLE ratio 0.72-0.99, HB coverage 0.90-0.94, MLE 0.79-0.93)
- Table 6: HB vs MLE K=4 extreme (ratio 0.65-0.97, HB cov 0.88-0.93, MLE 0.72-0.91)
- Table 7: Semi-synthetic CATE estimation (no corr RMSE 0.145, global 0.198, MLE 0.078, HB 0.072, oracle 0.035)
- Table 8: LLM quality by subgroup (GPT-4.1: 0.82 acc, Δπ=0.09, 2.8× ampl; Qwen3: 0.76, 0.13, 3.6×)
- Table 9: Real data worst-SG bias (no corr 0.09, global 0.22, MLE 0.07, HB 0.05; coverage 0.86→0.74→0.83→0.90)
- Table 10: Crossover budget (K=2 extreme: n=180; K=8 moderate: >1000)
- Table 11: EC-HTE vs PPCI by error type (cov only: EC-HTE 0.04 vs PPCI 0.16; outcome only: 0.14 vs 0.05; both combined: 0.08)
- Table 12: Coverage by error type (cov: EC-HTE 0.91, PPCI 0.80; outcome: 0.82, 0.93; both combined: 0.88)
- Table 13: LLM comparison (3 LLMs + majority vote)
- Table 14: Robustness under misspecification (10% noise: 0.085, 20%: 0.105, 30%: 0.132)
- Table 15: HB vs MLE degradation (10% noise: HB 15% vs MLE 25%)
- Table 16: CausalForestDML results (SG bias: naive 0.12, global 0.17, EC-HTE 0.06)
- Table 17: Allocation strategy comparison (uniform 0.082, uncertainty 0.075, CATE-weighted 0.071, oracle 0.065)

## Your Task
Provide a detailed review focusing on:

1. **Methodological soundness**: Is the bias characterization (Eq 1) correctly derived? Is the HB model well-specified? Is the "never worse than global" claim adequately supported? Are the MCMC diagnostics sufficient?
2. **Experimental rigor**: Are baselines appropriate? Is the evaluation comprehensive? Are the synthetic/semi-synthetic/real experiments well-designed? Any missing controls or ablations?
3. **Statistical concerns**: Undercoverage (88-94% vs nominal 95%) — is this adequately explained? Is the delta-method explanation convincing? Are standard errors properly reported?
4. **Reproducibility**: Are enough details provided? MCMC specs, data sizes, MC replications?
5. **Weaknesses in methods/experiments**: What are the main technical weaknesses?
6. **Experiment coverage**: All 11 planned experiments appear covered. Comment on completeness and depth.

Output format:
```
## R1: Methods & Experiments

### Summary
[2-3 sentences]

### Strengths
[Bulleted list, 4-6 items]

### Weaknesses
[Bulleted list, 4-6 items]

### Questions for Authors
[Bulleted list, 3-5 items]

### Minor Issues
[Bulleted list]

### Scores
- Soundness: [1-4]
- Empirical Rigor: [1-4]
- Reproducibility: [1-3]
- Overall: [1-6, where 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept]
- Confidence: [1-5]
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "ef2069a6-9609-4408-9b24-81250682356e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T20:26:50.078Z_

```json
{
  "parentUuid": "ef2069a6-9609-4408-9b24-81250682356e",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
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
  "uuid": "410aeb36-9904-4c36-a476-0eb5ca2521de",
  "timestamp": "2026-05-20T20:26:50.078Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T20:26:55.145Z_



I'll start by reading the paper and key project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "410aeb36-9904-4c36-a476-0eb5ca2521de",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET3Yu1g54GdVqUuSjrW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15a65265-6a41-49ff-90dc-1991b460d246",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eLqTd37P8R38ehTKRYGvF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16726,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16726,
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

_source line 4 · 2026-05-20T20:26:55.716Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QYcD9S24Y4MSHg93K7Dr3j`</summary>

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
  "parentUuid": "15a65265-6a41-49ff-90dc-1991b460d246",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET3Yu1g54GdVqUuSjrW",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efd3d72f-8a45-48cb-88fa-c8e5504fa16c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eLqTd37P8R38ehTKRYGvF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16726,
      "cache_read_input_tokens": 0,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16726
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 124,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16726,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16726,
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

_source line 5 · 2026-05-20T20:26:55.725Z_

<details><summary>↩ Tool result · `toolu_01QYcD9S24Y4MSHg93K7Dr3j`</summary>

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
  "parentUuid": "efd3d72f-8a45-48cb-88fa-c8e5504fa16c",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "90b9c6ad-fef7-44a9-a980-50e5eae82ff3",
  "sourceToolAssistantUUID": "efd3d72f-8a45-48cb-88fa-c8e5504fa16c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T20:26:58.253Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01BhT1LxKM78M5qQXY4d6EEX`</summary>

```json
{
  "project": "ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90b9c6ad-fef7-44a9-a980-50e5eae82ff3",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET3y73vXAsof4K78ow6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aff4afae-5b75-4997-99a7-fa101a2f9810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CivBgy3JfUJCegLWGW5Sad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 7 · 2026-05-20T20:26:58.344Z_

<details><summary>↩ Tool result · `toolu_01BhT1LxKM78M5qQXY4d6EEX`</summary>

```text
{"result":"# 项目 ec_hte_llm_annotation 概况\n\n## 实验状态 (2 个)\n\n- **exp-002**: PREPARING — \n- **exp-001**: PREPARING — \n\n## 最新报告\n（尚未生成）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aff4afae-5b75-4997-99a7-fa101a2f9810",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "1c3e13a8-3789-4d90-b489-ca8585bf00af",
  "sourceToolAssistantUUID": "aff4afae-5b75-4997-99a7-fa101a2f9810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T20:26:59.641Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FJFZkndMpqFzwzRpLhgUjy`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c3e13a8-3789-4d90-b489-ca8585bf00af",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET3y73vXAsof4K78ow6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f25e600-42c2-495e-b3a3-dad7d535f88b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CivBgy3JfUJCegLWGW5Sad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1446,
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

_source line 9 · 2026-05-20T20:26:59.697Z_

<details><summary>↩ Tool result · `toolu_01FJFZkndMpqFzwzRpLhgUjy`</summary>

```text
artifacts/dream_reports/dream_20260520T185426/best/paper.tex
artifacts/dream_reports/dream_20260520T185426/median/paper.tex
artifacts/dream_reports/dream_20260520T185426/worst/paper.tex
artifacts/dream_reports/dream_20260520T194535/best/paper.tex
artifacts/dream_reports/dream_20260520T194535/median/paper.tex
artifacts/dream_reports/dream_20260520T194535/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f25e600-42c2-495e-b3a3-dad7d535f88b",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "bb4313b6-fc88-4eac-8f32-df64a22880c9",
  "sourceToolAssistantUUID": "1f25e600-42c2-495e-b3a3-dad7d535f88b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T20:27:00.137Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01N8rUebdd3GUkubGcLG2KTY`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb4313b6-fc88-4eac-8f32-df64a22880c9",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET3y73vXAsof4K78ow6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2b3e084-17be-40ce-bb03-2e1376b3cbed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CivBgy3JfUJCegLWGW5Sad",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 16726,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1446
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 239,
          "cache_read_input_tokens": 16726,
          "cache_creation_input_tokens": 1446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1446,
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

_source line 11 · 2026-05-20T20:27:00.199Z_

<details><summary>↩ Tool result · `toolu_01N8rUebdd3GUkubGcLG2KTY`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2b3e084-17be-40ce-bb03-2e1376b3cbed",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "622e429a-b11f-42f0-aec5-a44739cb632b",
  "sourceToolAssistantUUID": "f2b3e084-17be-40ce-bb03-2e1376b3cbed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T20:27:02.704Z_

<details open><summary>🔧 Tool call — Read · `toolu_015nJqPCg2wyyaPd73yf3hYk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "622e429a-b11f-42f0-aec5-a44739cb632b",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET4JBGBkkE2uPXAvTF5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1add8965-2226-4f3f-9610-c5ac930f8cab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016kV5rQAGZG6nDaFncnVu14",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 547,
      "cache_read_input_tokens": 18172,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 547,
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

_source line 13 · 2026-05-20T20:27:02.751Z_

<details><summary>↩ Tool result · `toolu_015nJqPCg2wyyaPd73yf3hYk`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[margin=2.5cm]{geometry}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath,amssymb,amsthm}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{enumitem}
11	\usepackage{microtype}
12	\usepackage{tabularx}
13	\usepackage[T1]{fontenc}
14	\usepackage[utf8]{inputenc}
15	\usepackage{natbib}
16	\usepackage[colorlinks,citecolor=blue,urlcolor=blue,linkcolor=blue]{hyperref}
17	
18	\newtheorem{theorem}{Theorem}
19	\newtheorem{proposition}{Proposition}
20	\newtheorem{remark}{Remark}
21	\newtheorem{definition}{Definition}
22	
23	\newcommand{\CATE}{\mathrm{CATE}}
24	\newcommand{\bias}{\mathrm{bias}}
25	\newcommand{\RMSE}{\mathrm{RMSE}}
26	
27	\title{When Debiasing Backfires: Measurement-Error Heterogeneity\\ in LLM-Annotated Causal Effect Estimation}
28	
29	\author{Anonymous}
30	
31	\begin{document}
32	\maketitle
33	
34	\begin{abstract}
35	Large language models are increasingly used to annotate effect modifiers in heterogeneous treatment effect (HTE) analysis, yet their misclassification rates vary systematically across subgroups. We identify and formalize a previously unrecognized bias mechanism: when a pooled confusion matrix is used to correct subgroup-level conditional average treatment effect (CATE) estimates, the resulting bias is proportional to the product of misclassification heterogeneity ($\Delta\pi$) and CATE heterogeneity ($\Delta\tau$). In realistic settings, this ``debiasing'' worsens CATE bias by up to 7.8$\times$ compared to no correction. We propose EC-HTE, a hierarchical Bayesian framework that estimates subgroup-stratified confusion matrices with Dirichlet partial pooling, eliminating bias while controlling estimation variance. EC-HTE requires as few as 250 expert labels (for $K \le 4$ subgroups) and integrates with any CATE estimator including causal forests. On semi-synthetic political-science benchmarks with GPT-4.1 and Qwen3-235B annotations, EC-HTE reduces subgroup bias by 89--92\% versus global correction, with 93--95\% coverage. We further derive a diagnostic criterion (AUC = 0.953) that predicts when global correction is harmful, providing standalone practical value. Experiments on real interview data from Ashwin et al.\ (2025) confirm these findings, with global correction amplifying bias up to 6.7$\times$ on policy-relevant education subgroups.
36	\end{abstract}
37	
38	\section{Introduction}
39	
40	Researchers in computational social science increasingly rely on LLM annotations as effect modifiers in heterogeneous treatment effect analysis---for instance, classifying whether a political tweet contains ``economic framing'' to study how message framing moderates campaign effectiveness \citep{egami2024dsl,angelopoulos2023ppi}. A growing body of work addresses LLM annotation error by applying correction methods that use a pooled confusion matrix estimated from expert-labeled calibration data \citep{angelopoulos2023ppi,egami2024dsl,mozer2026arm}.
41	
42	However, LLM misclassification is not homogeneous. \citet{ashwin2025refugee} document that GPT-4 annotation errors vary significantly by refugee status, gender, and education level. When such heterogeneous errors interact with heterogeneous treatment effects, the standard pooled correction---designed to remove bias---can instead \emph{amplify} it.
43	
44	We formalize this bias mechanism and show that applying a global confusion matrix correction to subgroup-level CATEs introduces bias proportional to $\Delta\pi \times \Delta\tau$, the product of misclassification heterogeneity and CATE heterogeneity across subgroups. In a constructive example, global correction increases subgroup CATE bias from 0.023 to 0.179---a 7.8$\times$ amplification. This finding has immediate practical consequence: researchers who responsibly apply measurement error correction may obtain \emph{worse} estimates than those who use raw LLM labels.
45	
46	To address this, we propose \textbf{EC-HTE} (Error-Corrected Heterogeneous Treatment Effects), a hierarchical Bayesian framework that:
47	\begin{enumerate}[nosep,leftmargin=*]
48	\item estimates \emph{subgroup-stratified} confusion matrices using Dirichlet partial pooling, borrowing strength across subgroups while respecting heterogeneity;
49	\item corrects CATE estimates at the subgroup level with properly propagated uncertainty;
50	\item integrates with any CATE estimator, including causal forests.
51	\end{enumerate}
52	
53	Our contributions are:
54	\begin{enumerate}[nosep,leftmargin=*]
55	\item \textbf{Bias mechanism identification}: We prove that subgroup CATE bias under global correction equals $\sum_k w_k (\bar{\pi} - \pi_k)\tau_k$, where $\pi_k$ and $\tau_k$ are subgroup-specific misclassification rates and CATEs. For $K=2$, this simplifies to $\bias \propto \Delta\pi \times \Delta\tau$ (\S\ref{sec:theory}).
56	\item \textbf{EC-HTE framework}: Hierarchical Bayesian stratified correction with ``never worse than global'' guarantee via partial pooling (\S\ref{sec:method}).
57	\item \textbf{Diagnostic criterion}: A computable product-based test (AUC = 0.953) that predicts when global correction is harmful, with standalone value (\S\ref{sec:diagnostic}).
58	\item \textbf{Comprehensive validation}: Synthetic, semi-synthetic (political tweets), and real-data (refugee interviews) experiments across three LLMs (\S\ref{sec:experiments}).
59	\end{enumerate}
60	
61	\section{Related Work}
62	
63	\paragraph{Prediction-powered inference.} \citet{angelopoulos2023ppi} introduce PPI for constructing valid confidence intervals using ML predictions and a small labeled set. \citet{egami2024dsl} extend this to design-based social science (DSL). Both apply population-level corrections assuming homogeneous prediction error. \citet{mozer2026arm} proves arm-specific rectifiers fix ATE bias under differential prediction error but explicitly limits analysis to average effects. None address the case where the mismeasured variable \emph{defines} the heterogeneity structure.
64	
65	\paragraph{Conditional correction.} \citet{sui2026ppci} extend PPI to conditional functionals (PPCI) via kernel-based localization, correcting outcome-side measurement error. EC-HTE addresses covariate-side measurement error---the variable defining the conditioning structure---an orthogonal problem (\S\ref{sec:ppci}).
66	
67	\paragraph{Measurement error in causal inference.} Classical measurement error correction \citep{carroll2006measurement} addresses regression covariates; \citet{bu2023forestiv} handle ML-covariate error in regression via instrumental variables. Our contribution is the specific bias characterization for CATE estimation when the mismeasured variable defines heterogeneity. The $\Delta\pi \times \Delta\tau$ product form is new in this context.
68	
69	\paragraph{Bayesian annotation models.} \citet{dawid1979maximum} and \citet{paun2018comparing} model annotator-specific confusion matrices. We adapt this idea to subgroup-stratified estimation with hierarchical Dirichlet priors, connecting annotation modeling to causal inference.
70	
71	\section{Problem Formulation and Theory}
72	\label{sec:theory}
73	
74	\subsection{Setup}
75	
76	Consider a randomized experiment with treatment $T \in \{0,1\}$, outcome $Y$, and a binary effect modifier $X \in \{1,\ldots,K\}$ that defines subgroups for HTE analysis. The subgroup-specific CATE is $\tau_k = \mathbb{E}[Y(1) - Y(0) \mid X = k]$.
77	
78	The true $X$ is unobserved at scale. Instead, an LLM provides $\tilde{X}$, with subgroup-specific misclassification rates $\pi_k = P(\tilde{X} \neq X \mid X = k)$. A researcher estimates confusionmatrix $\hat{C}$ from $n$ expert-labeled instances and applies correction $\hat{\tau}_k^{\mathrm{corr}} = f(\hat{C}, \hat{\tau}_k^{\mathrm{raw}})$.
79	
80	\subsection{Bias Decomposition}
81	
82	\begin{theorem}[Global Correction Bias]
83	\label{thm:bias}
84	Let $\bar{\pi} = \sum_k w_k \pi_k$ be the population-averaged misclassification rate and $\hat{\pi}_{\mathrm{global}} = \bar{\pi}$ the pooled estimator. The bias of the globally-corrected CATE estimator for subgroup $k$ is:
85	\begin{equation}
86	\bias(\hat{\tau}_k^{\mathrm{global}}) = \sum_{j} w_j (\bar{\pi} - \pi_j) \tau_j
87	\end{equation}
88	For $K=2$ with equal subgroup weights:
89	\begin{equation}
90	\bias \propto \Delta\pi \cdot \Delta\tau
91	\label{eq:product}
92	\end{equation}
93	where $\Delta\pi = |\pi_1 - \pi_2|$ and $\Delta\tau = |\tau_1 - \tau_2|$.
94	\end{theorem}
95	
96	This has a natural interpretation: global correction over-corrects low-error subgroups (where $\bar{\pi} > \pi_k$) and under-corrects high-error subgroups (where $\bar{\pi} < \pi_k$). The damage scales with the treatment effect magnitude in affected subgroups.
97	
98	\begin{proposition}[Debiasing Can Hurt]
99	\label{prop:hurt}
100	There exist configurations where $|\bias(\hat{\tau}_k^{\mathrm{global}})| > |\bias(\hat{\tau}_k^{\mathrm{raw}})|$. Specifically, when $\Delta\pi > 0$ and $\Delta\tau > 0$, global correction amplifies subgroup bias.
101	\end{proposition}
102	
103	We verify this analytically and empirically. The analytic bound achieves $R^2 = 0.982$ against Monte Carlo simulations ($K=2$) and $R^2 = 0.971$ for $K=4$ (Table~\ref{tab:bound}).
104	
105	\begin{remark}[General-$K$ Extension]
106	For $K > 2$ subgroups, the bias takes the sum-of-products form $\sum_k w_k(\bar{\pi} - \pi_k)\tau_k$. Empirical verification across balanced and unbalanced configurations confirms this form with absolute errors $\leq 0.005$ (Table~\ref{tab:k4bound}).
107	\end{remark}
108	
109	\subsection{Diagnostic Criterion}
110	\label{sec:diagnostic}
111	
112	The product $\Delta\pi \times \Delta\tau$ serves as a diagnostic score for whether global correction is harmful. We define global correction as ``harmful'' when it amplifies bias relative to no correction, and evaluate this criterion via ROC analysis across 342 experimental settings spanning synthetic, semi-synthetic, and real data.
113	
114	The diagnostic achieves AUC = 0.953 (Table~\ref{tab:diagnostic}), with sensitivity 0.93 and specificity 0.88 at the optimal threshold of 0.008. This means even mild heterogeneity ($\Delta\pi = 0.04, \Delta\tau = 0.20$) triggers a recommendation for stratified correction---consistent with EC-HTE's ``never worse than global'' property.
115	
116	\begin{table}[t]
117	\centering
118	\small
119	\begin{tabular}{lcccc}
120	\toprule
121	Data source & $n$ & AUC & Sens. & Spec. \\
122	\midrule
123	Synthetic & 240 & 0.971 & 0.95 & 0.92 \\
124	Semi-synthetic & 72 & 0.938 & 0.91 & 0.86 \\
125	Real data & 30 & 0.929 & 0.90 & 0.83 \\
126	\midrule
127	Combined & 342 & 0.953 & 0.93 & 0.88 \\
128	\bottomrule
129	\end{tabular}
130	\caption{Diagnostic criterion ROC analysis. The $\Delta\pi \times \Delta\tau$ product reliably predicts when global correction is harmful (optimal threshold = 0.008).}
131	\label{tab:diagnostic}
132	\end{table}
133	
134	\section{The EC-HTE Framework}
135	\label{sec:method}
136	
137	\subsection{Subgroup-Stratified Confusion Matrix}
138	
139	Rather than estimating a single pooled confusion matrix $\hat{C}$, we estimate $K$ subgroup-specific matrices $\hat{C}_k$ from expert-labeled data. The corrected CATE for subgroup $k$ uses only $\hat{C}_k$:
140	\begin{equation}
141	\hat{\tau}_k^{\mathrm{EC\text{-}HTE}} = \hat{C}_k^{-1} \hat{\tau}_k^{\mathrm{raw}}
142	\end{equation}
143	
144	\subsection{Hierarchical Bayesian Estimation}
145	
146	With $K$ subgroups and limited expert labels, per-subgroup MLE of $C_k$ suffers from high variance (especially when $n_k = n/K$ is small). We place a hierarchical Dirichlet prior:
147	\begin{align}
148	C_{k,j} &\sim \mathrm{Dirichlet}(\alpha_j), \quad k = 1,\ldots,K \\
149	\alpha_j &\sim \mathrm{Gamma}(\mu_j, \sigma_j)
150	\end{align}
151	where $C_{k,j}$ is the $j$-th row of confusion matrix $C_k$ and $\alpha_j$ controls cross-subgroup shrinkage. When subgroups share similar error patterns, the posterior shrinks toward the global estimate; when they differ, each subgroup retains its own estimate.
152	
153	We use PyMC with NUTS sampling (4 chains, 1000 warmup). All MCMC diagnostics pass: $\hat{R} \leq 1.004$, ESS $\geq 387$, zero divergences (Table~\ref{tab:mcmc}).
154	
155	\begin{table}[t]
156	\centering
157	\small
158	\begin{tabular}{lcccc}
159	\toprule
160	Metric & Min & Median & Max & Threshold \\
161	\midrule
162	$\hat{R}$ & 1.000 & 1.001 & 1.004 & $<$1.01 \\
163	ESS (bulk) & 387 & 1240 & 4000 & $>$200 \\
164	ESS (tail) & 302 & 980 & 3500 & $>$200 \\
165	Divergences & 0 & 0 & 0 & 0 \\
166	Runtime (s) & 1.1 & 2.3 & 4.7 & --- \\
167	\bottomrule
168	\end{tabular}
169	\caption{MCMC diagnostics (1000 MC replications). All metrics within standard thresholds.}
170	\label{tab:mcmc}
171	\end{table}
172	
173	\subsection{Integration with CATE Estimators}
174	
175	EC-HTE integrates with any CATE estimator. We demonstrate two approaches with CausalForestDML:
176	
177	\textbf{Post-hoc correction.} Train the forest on raw LLM labels, then apply EC-HTE correction to subgroup-level CATE estimates.
178	
179	\textbf{Corrected pseudo-outcomes.} Apply EC-HTE to construct corrected pseudo-outcomes before forest training, with variance-adjusted confidence intervals.
180	
181	\section{Experiments}
182	\label{sec:experiments}
183	
184	We evaluate EC-HTE across three data regimes: synthetic (controlled DGP), semi-synthetic (real text, injected CATE structure), and real data. All experiments use 1000 Monte Carlo replications unless noted.
185	
186	\subsection{Bias Bound Verification}
187	\label{sec:bound}
188	
189	We verify Theorem~\ref{thm:bias} on a systematic parameter grid: $\Delta\pi \in [0, 0.3]$, $\Delta\tau \in [0, 0.5]$.
190	
191	\begin{table}[t]
192	\centering
193	\small
194	\begin{tabular}{cccccc}
195	\toprule
196	$\Delta\pi$ & $\Delta\tau$ & Analytic & MC & SE & Ratio \\
197	\midrule
198	0.05 & 0.10 & 0.006 & 0.006 & 0.001 & 1.01 \\
199	0.10 & 0.30 & 0.038 & 0.037 & 0.002 & 1.03 \\
200	0.20 & 0.20 & 0.050 & 0.049 & 0.002 & 1.02 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1add8965-2226-4f3f-9610-c5ac930f8cab",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "268c0e15-6b06-479f-b5f3-66e246df0abe",
  "sourceToolAssistantUUID": "1add8965-2226-4f3f-9610-c5ac930f8cab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T20:27:03.464Z_

<details open><summary>🔧 Tool call — Read · `toolu_018XyVTQ3uU1CAs4gwoZsBdG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/median/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "268c0e15-6b06-479f-b5f3-66e246df0abe",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET4JBGBkkE2uPXAvTF5",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f2b08b09-95c5-4ad8-9dc8-f3cdb7cc728a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016kV5rQAGZG6nDaFncnVu14",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 547,
      "cache_read_input_tokens": 18172,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 547
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 18172,
          "cache_creation_input_tokens": 547,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 547,
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

_source line 15 · 2026-05-20T20:27:03.499Z_

<details><summary>↩ Tool result · `toolu_018XyVTQ3uU1CAs4gwoZsBdG`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{amsmath,amssymb,amsfonts}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{graphicx}
9	\usepackage{hyperref}
10	\usepackage{natbib}
11	\usepackage[margin=2.5cm]{geometry}
12	\usepackage{xcolor}
13	\usepackage{tabularx}
14	\usepackage{array}
15	
16	\usepackage{amsthm}
17	\newtheorem{remark}{Remark}
18	
19	\newcommand{\CATE}{\mathrm{CATE}}
20	\newcommand{\E}{\mathbb{E}}
21	\newcommand{\Var}{\mathrm{Var}}
22	\newcommand{\RMSE}{\mathrm{RMSE}}
23	
24	\title{EC-HTE: Error-Corrected Heterogeneous Treatment Effect Estimation\\Under Subgroup-Varying LLM Misclassification}
25	
26	\author{Anonymous}
27	
28	\date{}
29	
30	\begin{document}
31	\maketitle
32	
33	%=============================================================================
34	% ABSTRACT
35	%=============================================================================
36	\begin{abstract}
37	Large language models are increasingly used to annotate effect modifiers in heterogeneous treatment effect (HTE) analysis, yet their misclassification rates vary systematically across subgroups.
38	We identify a previously unrecognized bias mechanism: applying a global (pooled) confusion-matrix correction to subgroup-level conditional average treatment effects (CATEs) introduces bias proportional to the product of misclassification heterogeneity ($\Delta\pi$) and CATE heterogeneity ($\Delta\tau$), amplifying subgroup CATE bias by up to $4\times$ in high-heterogeneity regimes.
39	We propose EC-HTE, a hierarchical Bayesian framework that estimates subgroup-specific confusion matrices via Dirichlet-prior partial pooling and applies stratified correction.
40	EC-HTE provides an automatic robustness guarantee---it never performs worse than global correction---because partial pooling degrades gracefully to the global estimator when subgroup structure is weak.
41	We further derive a diagnostic screening tool: the $\Delta\pi \times \Delta\tau$ product (AUC = 0.82) identifies settings where global correction is harmful, with practitioner-chosen operating points balancing sensitivity and specificity.
42	Experiments on synthetic, semi-synthetic (political-science tweets annotated by GPT-4.1 and Qwen3-235B), and real data (Rohingya refugee interviews) validate the bias mechanism and demonstrate that EC-HTE reduces worst-subgroup CATE bias from 0.22 to 0.05 on real data while improving confidence interval coverage from 74\% to 90\%.
43	\end{abstract}
44	
45	%=============================================================================
46	% 1. INTRODUCTION
47	%=============================================================================
48	\section{Introduction}
49	
50	The use of LLM-generated annotations as effect modifiers in causal inference has grown rapidly in computational social science \citep{egami2024using,ziems2024can}.
51	A researcher studying how ``economic framing'' in political tweets moderates campaign effectiveness might annotate thousands of tweets with GPT-4 and estimate conditional average treatment effects (CATEs) for subgroups defined by this LLM-assigned label.
52	Standard practice applies a global confusion-matrix correction estimated from a small expert-labeled calibration set \citep{angelopoulos2023prediction,egami2024using}.
53	
54	This correction assumes homogeneous misclassification---that the LLM errs at the same rate across all subgroups.
55	Empirically, this assumption fails: \citet{ashwin2025using} document that GPT-4 accuracy on refugee interview coding varies from 58\% to 76\% across subgroups defined by refugee status and gender.
56	We show that under such heterogeneity, global correction does not merely fail to help---it actively \emph{worsens} subgroup-level CATE estimates, over-correcting low-error subgroups while under-correcting high-error ones.
57	
58	\paragraph{Contributions.}
59	\begin{enumerate}
60	\item \textbf{Bias mechanism identification.} We formalize a bias proportional to $\Delta\pi \times \Delta\tau$---the product of misclassification heterogeneity and CATE heterogeneity---and show global correction can amplify subgroup CATE bias by up to $4\text{--}5\times$ in high-heterogeneity regimes (Section~\ref{sec:theory}).
61	\item \textbf{EC-HTE framework.} We propose hierarchical Bayesian subgroup-stratified correction with a never-worse-than-global guarantee via partial pooling (Section~\ref{sec:method}).
62	\item \textbf{Diagnostic screening tool.} The $\Delta\pi \times \Delta\tau$ product, computable from pilot data, serves as a screening criterion (AUC = 0.82) with practitioner-chosen operating points (Section~\ref{sec:diagnostic}).
63	\item \textbf{Comprehensive validation.} Synthetic, semi-synthetic, and real-data experiments with three LLMs demonstrate the practical relevance of the bias mechanism and the effectiveness of EC-HTE (Sections~\ref{sec:synthetic}--\ref{sec:real}).
64	\end{enumerate}
65	
66	%=============================================================================
67	% 2. RELATED WORK
68	%=============================================================================
69	\section{Related Work}
70	
71	\paragraph{Prediction-powered inference.}
72	PPI \citep{angelopoulos2023prediction} and DSL \citep{egami2024using} use expert-labeled calibration data to debias LLM annotations for population-level estimands.
73	PPCI \citep{sui2026prediction} extends PPI to conditional functionals via kernel localization but targets \emph{outcome-side} measurement error, not covariate-side misclassification.
74	
75	\paragraph{Measurement error in causal inference.}
76	\citet{carroll2006measurement} develop regression calibration and SIMEX for covariate measurement error.
77	ForestIV \citep{bu2023estimating} instruments ML-assigned covariates in regression.
78	\citet{mozer2026adjusting} proves arm-specific rectifiers fix ATE under differential prediction error but explicitly limits analysis to average treatment effects.
79	None of these works addresses the specific bias arising when the mismeasured variable \emph{defines the heterogeneity structure} for CATE estimation.
80	
81	\paragraph{Bayesian annotation models.}
82	\citet{dawid1979maximum} and \citet{paun2018comparing} model annotator-specific confusion matrices.
83	Our hierarchical Bayesian formulation adapts this idea to subgroup-specific LLM error estimation within a causal inference pipeline.
84	
85	%=============================================================================
86	% 3. BIAS MECHANISM
87	%=============================================================================
88	\section{Bias Mechanism: When Global Correction Backfires}
89	\label{sec:theory}
90	
91	\subsection{Setup}
92	
93	Consider $K$ subgroups defined by an effect modifier $X \in \{1, \ldots, K\}$.
94	Let $\tilde{X}$ denote the LLM-assigned label, $\pi_k = P(\tilde{X} = X \mid X = k)$ the subgroup-specific accuracy, and $\tau_k$ the true CATE for subgroup $k$.
95	A global correction applies the pooled confusion matrix $\bar{C}$ (estimated from calibration data) to adjust CATE estimates.
96	
97	\subsection{Bias Characterization for $K=2$}
98	
99	When subgroup-specific accuracies $\pi_1 \neq \pi_2$, the global confusion matrix $\bar{C}$ misallocates prediction errors across subgroups. The resulting bias in subgroup CATE estimates takes the form:
100	\begin{equation}
101	\text{Bias}_{\text{global}}(\hat{\tau}_k) \propto \Delta\pi \times \Delta\tau,
102	\label{eq:bias}
103	\end{equation}
104	where $\Delta\pi = |\pi_1 - \pi_2|$ measures misclassification heterogeneity and $\Delta\tau = |\tau_1 - \tau_2|$ measures CATE heterogeneity.
105	This first-order approximation explains 89\% of bias variance across a systematic parameter grid ($R^2 = 0.89$, 1000 Monte Carlo replications per grid point; Table~\ref{tab:bias_bound}).
106	
107	\paragraph{Constructive example.}
108	Consider two subgroups with $\pi_1 = 0.9$, $\pi_2 = 0.75$, $\tau_1 = 0.15$, $\tau_2 = 0.35$.
109	Global correction produces subgroup biases of 0.18 and $-0.14$, while the aggregate bias is only 0.02---researchers examining only aggregate metrics would incorrectly conclude the correction works well.
110	
111	\paragraph{Bias amplification.}
112	Table~\ref{tab:amplification} quantifies the amplification factor (ratio of global-correction bias to no-correction bias) across regimes.
113	In extreme heterogeneity settings ($\Delta\pi \in [0.10, 0.25]$, $\Delta\tau \in [0.20, 0.50]$), global correction amplifies subgroup CATE bias by $4.2\times$ on average.
114	
115	\begin{table}[t]
116	\centering
117	\small
118	\caption{Analytic bias bound $R^2$ by $K$ and model specification.}
119	\label{tab:bias_bound}
120	\begin{tabular}{llccc}
121	\toprule
122	$K$ & Model & $R^2$ & Tightness (med.) & Tightness (90th) \\
123	\midrule
124	2 & $\Delta\pi \times \Delta\tau$ & 0.89 & 1.15 & 1.45 \\
125	2 & $+ $ intercept & 0.91 & 1.12 & 1.38 \\
126	4 & $\Sigma(\Delta\pi_k \times \Delta\tau_k)$ & 0.76 & 1.32 & 1.85 \\
127	4 & $+$ pairwise interactions & 0.84 & 1.20 & 1.55 \\
128	4 & $+$ all higher-order & 0.88 & 1.14 & 1.42 \\
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	\begin{table}[t]
134	\centering
135	\small
136	\caption{Bias amplification factor (global correction / no correction) by heterogeneity regime.}
137	\label{tab:amplification}
138	\begin{tabular}{llll}
139	\toprule
140	Regime & $\Delta\pi$ range & $\Delta\tau$ range & Amplification \\
141	\midrule
142	Extreme & 0.10--0.25 & 0.20--0.50 & $4.2 \pm 0.3$ \\
143	Moderate & 0.05--0.12 & 0.10--0.25 & $2.3 \pm 0.2$ \\
144	Mild & 0.02--0.05 & 0.05--0.12 & $1.4 \pm 0.1$ \\
145	Homogeneous & $< 0.02$ & any & $1.05 \pm 0.05$ \\
146	\bottomrule
147	\end{tabular}
148	\end{table}
149	
150	\begin{remark}[Extension to $K > 2$]
151	For $K > 2$ subgroups, the bias takes a sum-of-products form $\sum_k \Delta\pi_k \times \Delta\tau_k$, but cross-subgroup misclassification routing introduces additional structure not captured by marginal heterogeneity measures.
152	Adding pairwise interaction terms recovers $R^2 = 0.84$ for $K=4$ (Table~\ref{tab:bias_bound}).
153	A complete characterization of the $K > 2$ case involving higher-order terms remains an open problem.
154	\end{remark}
155	
156	%=============================================================================
157	% 4. METHOD: EC-HTE
158	%=============================================================================
159	\section{Method: EC-HTE}
160	\label{sec:method}
161	
162	\subsection{Hierarchical Bayesian Confusion Matrix Estimation}
163	
164	For each subgroup $k$, the confusion matrix row $\mathbf{c}_k$ is modeled with a Dirichlet prior:
165	\begin{align}
166	\mathbf{c}_k &\sim \text{Dirichlet}(\boldsymbol{\alpha}_k), \\
167	\boldsymbol{\alpha}_k &= \alpha_0 \cdot \bar{\mathbf{c}} + \mathbf{1},
168	\end{align}
169	where $\bar{\mathbf{c}}$ is the global confusion matrix and $\alpha_0$ controls shrinkage.
170	We place a hyperprior on $\alpha_0$ and estimate the full posterior via MCMC (PyMC NUTS, 4 chains, 1500 warmup, 1000 draws).
171	
172	\paragraph{Automatic robustness guarantee.}
173	When subgroup-level data is sparse, the posterior for $\mathbf{c}_k$ shrinks toward $\bar{\mathbf{c}}$, recovering global correction.
174	When data is abundant, the posterior converges to the subgroup-specific MLE.
175	This ensures EC-HTE is \emph{never worse than global correction}---verified empirically: across all 1000 Monte Carlo replications, the fraction of settings where HB performs worse than global is 0.0\% (Table~\ref{tab:hb_main}).
176	
177	\subsection{Stratified CATE Correction}
178	
179	Given posterior draws $\{\mathbf{C}_k^{(s)}\}_{s=1}^S$ of the subgroup confusion matrix, corrected CATE estimates are obtained by inverting the confusion matrix for each draw and propagating uncertainty:
180	\begin{equation}
181	\hat{\tau}_k^{(s)} = f(\mathbf{C}_k^{(s)}, \hat{\tau}_k^{\text{naive}}),
182	\end{equation}
183	where $f$ denotes the matrix-inversion correction operator.
184	Point estimates and credible intervals are computed from the posterior sample.
185	
186	\subsection{Integration with Causal Forests}
187	
188	EC-HTE correction is estimator-agnostic. We demonstrate integration with both difference-in-means within strata and CausalForestDML \citep{athey2019generalized}.
189	For causal forests, correction is applied post-hoc to subgroup-level CATE aggregates, with variance-adjusted confidence intervals.
190	
191	%=============================================================================
192	% 5. DIAGNOSTIC CRITERION
193	%=============================================================================
194	\section{Diagnostic Screening Tool}
195	\label{sec:diagnostic}
196	
197	The $\Delta\pi \times \Delta\tau$ product, computable from a small pilot study, serves as a screening criterion for whether global correction is harmful.
198	We evaluate this diagnostic as a binary classifier (``global correction increases bias beyond no correction'') via ROC analysis.
199	
200	\begin{table}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2b08b09-95c5-4ad8-9dc8-f3cdb7cc728a",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "ccc5a17c-c6ba-47b1-b6e4-58e78f3eae20",
  "sourceToolAssistantUUID": "f2b08b09-95c5-4ad8-9dc8-f3cdb7cc728a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-20T20:27:05.747Z_

Let me continue reading both papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ccc5a17c-c6ba-47b1-b6e4-58e78f3eae20",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET4Yz1Ak8EQL8w2wPay",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5729cb67-f13d-4237-90ed-781ec3b5ac97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ptBFUfc8qu9TFZHC8nKeq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9224,
      "cache_read_input_tokens": 18719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9224,
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

_source line 17 · 2026-05-20T20:27:08.766Z_

<details open><summary>🔧 Tool call — Read · `toolu_011HqwvnFp35htAzBTfo1tg2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5729cb67-f13d-4237-90ed-781ec3b5ac97",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET4Yz1Ak8EQL8w2wPay",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1252f2c0-989c-4413-be40-4f04c6689cde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ptBFUfc8qu9TFZHC8nKeq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9224,
      "cache_read_input_tokens": 18719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9224,
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

_source line 18 · 2026-05-20T20:27:08.817Z_

<details><summary>↩ Tool result · `toolu_011HqwvnFp35htAzBTfo1tg2`</summary>

```text
200	0.20 & 0.20 & 0.050 & 0.049 & 0.002 & 1.02 \\
201	0.20 & 0.40 & 0.100 & 0.097 & 0.003 & 1.03 \\
202	0.30 & 0.50 & 0.188 & 0.179 & 0.005 & 1.05 \\
203	\bottomrule
204	\end{tabular}
205	\caption{Analytic bound vs.\ MC empirical bias ($K=2$). The product form (Eq.~\ref{eq:product}) achieves $R^2 = 0.982$ across the full grid.}
206	\label{tab:bound}
207	\end{table}
208	
209	Table~\ref{tab:amplification} shows bias amplification---the ratio of global-corrected bias to uncorrected bias. In the extreme regime ($\Delta\pi = 0.25, \Delta\tau = 0.13$), global correction amplifies bias from 0.023 to 0.179, a 7.8$\times$ increase. Even moderate heterogeneity ($\Delta\pi = 0.10, \Delta\tau = 0.10$) produces 3.1$\times$ amplification.
210	
211	\begin{table}[t]
212	\centering
213	\small
214	\begin{tabular}{lcccc}
215	\toprule
216	Regime & $\Delta\pi$ & No corr. & Global & Ampl. \\
217	\midrule
218	Extreme & 0.25 & 0.023 & 0.179 & 7.8$\times$ \\
219	Extreme & 0.20 & 0.019 & 0.118 & 6.2$\times$ \\
220	Extreme & 0.15 & 0.015 & 0.080 & 5.3$\times$ \\
221	Moderate & 0.10 & 0.008 & 0.025 & 3.1$\times$ \\
222	Homogeneous & 0.03 & 0.001 & 0.002 & 1.5$\times$ \\
223	\bottomrule
224	\end{tabular}
225	\caption{Bias amplification: global correction vs.\ no correction.}
226	\label{tab:amplification}
227	\end{table}
228	
229	\begin{table}[t]
230	\centering
231	\small
232	\begin{tabular}{cccccc}
233	\toprule
234	Config & Pred. & MC & Error \\
235	\midrule
236	Balanced, linear $\Delta\pi$ & 0.062 & 0.060 & 0.002 \\
237	Balanced, quadratic $\Delta\pi$ & 0.084 & 0.081 & 0.003 \\
238	Unbalanced, linear $\Delta\pi$ & 0.071 & 0.068 & 0.003 \\
239	Unbalanced, quadratic $\Delta\pi$ & 0.098 & 0.093 & 0.005 \\
240	\bottomrule
241	\end{tabular}
242	\caption{$K=4$ sum-of-products verification ($R^2 = 0.971$).}
243	\label{tab:k4bound}
244	\end{table}
245	
246	\subsection{HB Partial Pooling Validation}
247	\label{sec:hb}
248	
249	We compare HB Dirichlet estimation against MLE and Laplace-smoothed baselines across error regimes (extreme/moderate/homogeneous), expert sample sizes ($n \in \{100, 250, 500, 1000, 2000\}$), and number of subgroups ($K \in \{2, 4\}$).
250	
251	\begin{table}[t]
252	\centering
253	\small
254	\setlength{\tabcolsep}{3.5pt}
255	\begin{tabular}{llccccc}
256	\toprule
257	Regime & $n$ & MLE & Lap. & HB & Ratio & Cov. \\
258	\midrule
259	\multirow{3}{*}{Extreme}
260	 & 100 & .058 & .049 & .042 & .72 & .932 \\
261	 & 250 & .037 & .032 & .027 & .74 & .943 \\
262	 & 1000 & .016 & .015 & .015 & .91 & .952 \\
263	\midrule
264	\multirow{3}{*}{Moderate}
265	 & 100 & .041 & .036 & .031 & .76 & .938 \\
266	 & 250 & .027 & .024 & .021 & .78 & .951 \\
267	 & 1000 & .012 & .012 & .011 & .93 & .954 \\
268	\midrule
269	\multirow{3}{*}{Homog.}
270	 & 100 & .032 & .029 & .027 & .84 & .944 \\
271	 & 250 & .021 & .020 & .019 & .88 & .954 \\
272	 & 1000 & .010 & .010 & .010 & .97 & .954 \\
273	\bottomrule
274	\end{tabular}
275	\caption{RMSE comparison ($K=2$). HB achieves 22--28\% reduction at $n \leq 250$ with near-nominal coverage. Full table in Appendix.}
276	\label{tab:hb_k2}
277	\end{table}
278	
279	Table~\ref{tab:hb_k2} shows that HB partial pooling reduces RMSE by 22--28\% at $n \leq 250$ in the extreme regime, with 95\% CI coverage consistently in $[0.93, 0.96]$. MLE coverage drops to 0.87 under the same conditions. The advantage is more pronounced for $K=4$: at $n=250$, HB achieves a 32\% RMSE reduction (HB/MLE ratio = 0.68) because per-subgroup sample sizes halve (Table~\ref{tab:hb_k4}).
280	
281	\begin{table}[t]
282	\centering
283	\small
284	\begin{tabular}{cccccc}
285	\toprule
286	$n$ & MLE & HB & Ratio & HB Cov. & MLE Cov. \\
287	\midrule
288	100 & .089 & .058 & .65 & .921 & .82 \\
289	250 & .054 & .037 & .68 & .940 & .86 \\
290	500 & .035 & .027 & .77 & .949 & .91 \\
291	1000 & .023 & .020 & .87 & .953 & .94 \\
292	\bottomrule
293	\end{tabular}
294	\caption{$K=4$ subgroups, extreme regime. HB advantage grows with $K$ due to reduced per-subgroup sample size.}
295	\label{tab:hb_k4}
296	\end{table}
297	
298	\subsection{Semi-Synthetic Political Science Benchmark}
299	\label{sec:semisynthetic}
300	
301	We construct a semi-synthetic benchmark from political tweets ($N = 20{,}000$) with injected CATE heterogeneity structure (economic framing moderates campaign effectiveness). Two LLMs annotate effect modifiers; $n = 500$ expert labels calibrate confusion matrices.
302	
303	\paragraph{Misclassification heterogeneity is real.} Table~\ref{tab:misclass} confirms systematic error heterogeneity: GPT-4.1 achieves 93\% accuracy on economic-mainstream tweets but only 78\% on minority-immigration content (error ratio 2.15$\times$). Qwen3-235B shows even larger heterogeneity (error ratio 2.55$\times$).
304	
305	\begin{table}[t]
306	\centering
307	\small
308	\setlength{\tabcolsep}{3pt}
309	\begin{tabular}{llcccc}
310	\toprule
311	LLM & Subgroup & $n$ & Acc. & FPR & FNR \\
312	\midrule
313	\multirow{2}{*}{GPT-4.1}
314	 & Econ-mainstream & 11200 & .93 & .04 & .10 \\
315	 & Minor-immigr. & 8800 & .78 & .12 & .31 \\
316	\midrule
317	\multirow{2}{*}{Qwen3}
318	 & Econ-mainstream & 11200 & .89 & .06 & .16 \\
319	 & Minor-immigr. & 8800 & .72 & .15 & .40 \\
320	\bottomrule
321	\end{tabular}
322	\caption{Subgroup-specific LLM misclassification rates on political tweets.}
323	\label{tab:misclass}
324	\end{table}
325	
326	\paragraph{Global correction amplifies bias.} Table~\ref{tab:semisyn_gpt4} presents CATE estimation results with GPT-4.1. Global correction amplifies bias by 5.4$\times$: for the economic-mainstream subgroup ($\tau = 0.15$), it over-corrects to $\hat{\tau} = 0.188$ (bias = 0.038); for minority-immigration ($\tau = 0.04$), it under-corrects to $\hat{\tau} = 0.009$ (bias = $-0.031$). EC-HTE reduces bias to 0.004--0.006 across subgroups with 94--95\% coverage.
327	
328	\begin{table}[t]
329	\centering
330	\small
331	\setlength{\tabcolsep}{3pt}
332	\begin{tabular}{llcccc}
333	\toprule
334	Method & Subgroup & $\hat{\tau}$ & Bias & RMSE & Cov. \\
335	\midrule
336	\multirow{2}{*}{No corr.}
337	 & Econ-main & .138 & $-.012$ & .018 & .89 \\
338	 & Minor-imm & .058 & .018 & .023 & .85 \\
339	\midrule
340	\multirow{2}{*}{Global}
341	 & Econ-main & .188 & .038 & .042 & .71 \\
342	 & Minor-imm & .009 & $-.031$ & .035 & .76 \\
343	\midrule
344	\multirow{2}{*}{MLE strat.}
345	 & Econ-main & .153 & .003 & .021 & .91 \\
346	 & Minor-imm & .044 & .004 & .019 & .90 \\
347	\midrule
348	\multirow{2}{*}{\textbf{EC-HTE}}
349	 & Econ-main & .154 & .004 & .014 & .94 \\
350	 & Minor-imm & .046 & .006 & .012 & .95 \\
351	\bottomrule
352	\end{tabular}
353	\caption{CATE estimation with GPT-4.1 annotations. True CATEs: economic-mainstream $\tau_1 = 0.15$, minority-immigration $\tau_2 = 0.04$. Global correction amplifies bias 5.4$\times$.}
354	\label{tab:semisyn_gpt4}
355	\end{table}
356	
357	Results with Qwen3-235B are even more pronounced (6.9$\times$ amplification), with EC-HTE achieving 92\% bias reduction and 93\% coverage on both subgroups (Table~\ref{tab:semisyn_qwen3}).
358	
359	\begin{table}[t]
360	\centering
361	\small
362	\setlength{\tabcolsep}{3pt}
363	\begin{tabular}{llcccc}
364	\toprule
365	Method & Subgroup & $\hat{\tau}$ & Bias & RMSE & Cov. \\
366	\midrule
367	\multirow{2}{*}{No corr.}
368	 & Econ-main & .133 & $-.017$ & .023 & .86 \\
369	 & Minor-imm & .065 & .025 & .030 & .81 \\
370	\midrule
371	\multirow{2}{*}{Global}
372	 & Econ-main & .201 & .051 & .055 & .63 \\
373	 & Minor-imm & $-.003$ & $-.043$ & .048 & .68 \\
374	\midrule
375	\multirow{2}{*}{\textbf{EC-HTE}}
376	 & Econ-main & .155 & .005 & .016 & .93 \\
377	 & Minor-imm & .047 & .007 & .014 & .93 \\
378	\bottomrule
379	\end{tabular}
380	\caption{CATE estimation with Qwen3-235B. Global correction produces a \emph{negative} CATE estimate for the minority-immigration subgroup (true $\tau = 0.04$).}
381	\label{tab:semisyn_qwen3}
382	\end{table}
383	
384	\subsection{Real-Data Validation}
385	\label{sec:realdata}
386	
387	We apply EC-HTE to the Rohingya refugee interview dataset of \citet{ashwin2025refugee}, where LLM annotation errors correlate with refugee status, gender, and education. GPT-4.1 annotations are calibrated with 200--500 expert labels.
388	
389	\paragraph{Education dimension.} Table~\ref{tab:realdata} shows the education subgroup results, where misclassification heterogeneity is largest (error ratio 3.0$\times$; high-education: $\pi = 0.08$, low-education: $\pi = 0.24$). Global correction amplifies bias 6.7$\times$, pushing the low-education CATE estimate negative ($-0.012$, implying the intervention is harmful) when the true effect is positive. EC-HTE corrects both subgroups to within 0.003--0.004 of ground truth with 93--94\% coverage.
390	
391	\begin{table}[t]
392	\centering
393	\small
394	\setlength{\tabcolsep}{3pt}
395	\begin{tabular}{llcccc}
396	\toprule
397	Method & Subgroup & $\hat{\tau}$ & Bias & RMSE & Cov. \\
398	\midrule
399	\multirow{2}{*}{No corr.}
400	 & High edu & .082 & $-.008$ & .015 & .90 \\
401	 & Low edu & .031 & .019 & .024 & .83 \\
402	\midrule
403	\multirow{2}{*}{Global}
404	 & High edu & .135 & .045 & .049 & .65 \\
405	 & Low edu & $-.012$ & $-.062$ & .067 & .58 \\
406	\midrule
407	\multirow{2}{*}{\textbf{EC-HTE}}
408	 & High edu & .093 & .003 & .013 & .94 \\
409	 & Low edu & .054 & .004 & .014 & .93 \\
410	\bottomrule
411	\end{tabular}
412	\caption{Real-data validation on Ashwin et al.\ (2025), education subgroups. Global correction produces policy-misleading negative CATE for low-education group.}
413	\label{tab:realdata}
414	\end{table}
415	
416	Across all demographic dimensions, EC-HTE achieves 87--93\% bias reduction with 93--94\% coverage, while global correction amplifies bias 4.2--6.7$\times$ (Table~\ref{tab:realdata_summary}).
417	
418	\begin{table}[t]
419	\centering
420	\small
421	\begin{tabular}{lccc}
422	\toprule
423	Dimension & Error ratio & Ampl. & EC-HTE red. \\
424	\midrule
425	Refugee status & 1.91$\times$ & 4.2$\times$ & 87\% \\
426	Gender & 2.00$\times$ & 5.1$\times$ & 91\% \\
427	Education & 3.00$\times$ & 6.7$\times$ & 93\% \\
428	\bottomrule
429	\end{tabular}
430	\caption{Summary across demographic dimensions. Amplification correlates with error ratio.}
431	\label{tab:realdata_summary}
432	\end{table}
433	
434	\subsection{Orthogonality with PPCI}
435	\label{sec:ppci}
436	
437	We compare EC-HTE with PPCI \citep{sui2026ppci} across three error scenarios: (A) covariate-side error only (effect modifier misclassification), (B) outcome-side error only, and (C) both.
438	
439	\begin{table}[t]
440	\centering
441	\small
442	\setlength{\tabcolsep}{3pt}
443	\begin{tabular}{llccc}
444	\toprule
445	Scenario & Method & Bias & RMSE & Cov. \\
446	\midrule
447	\multirow{4}{*}{\shortstack[l]{A: Covar-\\iate-side}}
448	 & No correction & .021 & .027 & .87 \\
449	 & PPCI & .089 & .094 & .58 \\
450	 & EC-HTE & \textbf{.005} & \textbf{.012} & \textbf{.94} \\
451	\midrule
452	\multirow{4}{*}{\shortstack[l]{B: Out-\\come-side}}
453	 & No correction & .020 & .025 & .88 \\
454	 & PPCI & \textbf{.004} & \textbf{.010} & \textbf{.95} \\
455	 & EC-HTE & .018 & .023 & .89 \\
456	\midrule
457	\multirow{4}{*}{C: Both}
458	 & No correction & .038 & .044 & .82 \\
459	 & PPCI & .082 & .088 & .61 \\
460	 & EC-HTE & .017 & .023 & .89 \\
461	 & \textbf{EC-HTE+PPCI} & \textbf{.006} & \textbf{.012} & \textbf{.94} \\
462	\bottomrule
463	\end{tabular}
464	\caption{EC-HTE and PPCI are orthogonal: each excels on its target error type. Their composition achieves the best result when both errors are present (correlation of correction terms: $r = 0.04$).}
465	\label{tab:ppci}
466	\end{table}
467	
468	Table~\ref{tab:ppci} confirms orthogonality. PPCI is effective for outcome-side error (bias 0.004) but \emph{worsens} covariate-side error (bias 0.089 vs.\ 0.021 uncorrected). EC-HTE shows the reverse pattern. When both error types are present, their composition reduces bias to 0.006---84\% reduction versus no correction and better than either method alone.
469	
470	\subsection{Causal Forest Integration}
471	
472	Table~\ref{tab:forest} demonstrates EC-HTE integration with CausalForestDML. The pseudo-outcome approach achieves near-oracle performance (bias 0.005 vs.\ oracle 0.002) and substantially improves heterogeneity detection power from 0.62 (naive) to 0.89.
473	
474	\begin{table}[t]
475	\centering
476	\small
477	\setlength{\tabcolsep}{3.5pt}
478	\begin{tabular}{lcccc}
479	\toprule
480	Method & Bias & RMSE & Cov. & Power \\
481	\midrule
482	Naive forest & .024 & .029 & .88 & .62 \\
483	Global-corrected & .051 & .056 & .73 & .55 \\
484	EC-HTE post-hoc & .007 & .015 & .93 & .85 \\
485	EC-HTE pseudo-out. & \textbf{.005} & \textbf{.013} & \textbf{.95} & \textbf{.89} \\
486	Oracle (true labels) & .002 & .010 & .95 & .93 \\
487	\bottomrule
488	\end{tabular}
489	\caption{Causal forest integration. EC-HTE pseudo-outcome correction approaches oracle performance and nearly doubles heterogeneity detection power vs.\ naive forest.}
490	\label{tab:forest}
491	\end{table}
492	
493	\section{Conclusion}
494	
495	We identified and formalized a previously unrecognized bias mechanism in LLM-annotated causal effect estimation: when misclassification rates and treatment effects both vary across subgroups, applying a pooled correction amplifies rather than reduces bias. The $\Delta\pi \times \Delta\tau$ product characterization provides both theoretical insight and a practical diagnostic (AUC = 0.953). EC-HTE, our hierarchical Bayesian stratified correction framework, eliminates this bias with as few as 250 expert labels and integrates with modern CATE estimators. On semi-synthetic political-science and real refugee-interview data, it achieves 85--93\% bias reduction across three LLMs.
496	
497	\section*{Limitations}
498	
499	EC-HTE requires subgroup structure to be defined \emph{a priori}. When $K$ is large relative to expert label budget (e.g., $K=8$ with only 50 labels), per-subgroup estimation degrades and EC-HTE may perform worse than global correction (breakeven at $\sim$38\% subgroup label noise; see Appendix~\ref{app:robustness}). The method adds computational cost ($\sim$2.3s per MCMC fit vs.\ 0.008s for MLE), though this is negligible relative to LLM annotation costs. Our semi-synthetic and real-data experiments use binary or small-$K$ subgroups; extension to high-dimensional continuous effect modifiers remains future work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1252f2c0-989c-4413-be40-4f04c6689cde",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "c9a734ec-3b80-44cc-b2c8-050aac4634c2",
  "sourceToolAssistantUUID": "1252f2c0-989c-4413-be40-4f04c6689cde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T20:27:09.457Z_

<details open><summary>🔧 Tool call — Read · `toolu_017VnNZahVEqHmt1HUEWEiRq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/median/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9a734ec-3b80-44cc-b2c8-050aac4634c2",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET4Yz1Ak8EQL8w2wPay",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "532470f2-d653-4e5b-93a5-38ccddbe0887",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ptBFUfc8qu9TFZHC8nKeq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9224,
      "cache_read_input_tokens": 18719,
      "output_tokens": 263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9224
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 263,
          "cache_read_input_tokens": 18719,
          "cache_creation_input_tokens": 9224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9224,
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

_source line 20 · 2026-05-20T20:27:09.503Z_

<details><summary>↩ Tool result · `toolu_017VnNZahVEqHmt1HUEWEiRq`</summary>

```text
200	\begin{table}[t]
201	\centering
202	\small
203	\caption{Diagnostic criterion ROC operating points.}
204	\label{tab:diagnostic_roc}
205	\begin{tabular}{lcccc}
206	\toprule
207	Operating Point & $\Delta\pi \times \Delta\tau$ & Sens. & Spec. & F1 \\
208	\midrule
209	High sensitivity & 0.015 & 0.90 & 0.55 & 0.68 \\
210	Balanced & 0.035 & 0.75 & 0.72 & 0.73 \\
211	High specificity & 0.065 & 0.55 & 0.90 & 0.67 \\
212	\bottomrule
213	\end{tabular}
214	\end{table}
215	
216	\begin{table}[t]
217	\centering
218	\small
219	\caption{Diagnostic AUC by metric and data source.}
220	\label{tab:diagnostic_auc}
221	\begin{tabular}{lccc}
222	\toprule
223	Diagnostic & Synth. & Semi-synth. & Real \\
224	\midrule
225	$\Delta\pi \times \Delta\tau$ product & 0.82 & 0.79 & 0.78 \\
226	$\Delta\pi$ only & 0.73 & 0.71 & 0.70 \\
227	$\Delta\tau$ only & 0.65 & 0.64 & 0.62 \\
228	\bottomrule
229	\end{tabular}
230	\end{table}
231	
232	The overall AUC is 0.82 (95\% CI: [0.77, 0.87]), with the product outperforming either marginal metric by 9+ AUC points (Table~\ref{tab:diagnostic_auc}).
233	Rather than prescribing a single threshold, we recommend practitioners choose an operating point based on their tolerance for false negatives (Table~\ref{tab:diagnostic_roc}):
234	a conservative threshold of 0.015 catches 90\% of harmful settings at the cost of 45\% false positives, while a stringent 0.065 threshold achieves 90\% specificity.
235	Approximately 35\% of realistic settings fall in a gray zone ($\Delta\pi \times \Delta\tau \in [0.02, 0.06]$) where domain knowledge should guide the decision.
236	
237	The diagnostic transfers reasonably across data sources: AUC degrades from 0.82 (synthetic) to 0.79 (semi-synthetic) to 0.78 (real data), suggesting practitioners should calibrate thresholds with a small pilot study rather than relying on pre-set values.
238	
239	%=============================================================================
240	% 6. EXPERIMENTS
241	%=============================================================================
242	\section{Experiments}
243	\label{sec:experiments}
244	
245	\subsection{Synthetic Validation: HB vs.\ MLE vs.\ Laplace}
246	\label{sec:synthetic}
247	
248	We conduct a full regime sweep across heterogeneity levels (extreme, moderate, homogeneous), expert sample sizes ($n \in \{100, 250, 500, 1000\}$), and subgroup counts ($K \in \{2, 4\}$), with 1000 Monte Carlo replications per setting.
249	
250	\begin{table}[t]
251	\centering
252	\small
253	\caption{HB vs.\ MLE vs.\ Laplace: RMSE ratio (HB/MLE) and coverage across regimes ($K=2$). Standard errors in parentheses.}
254	\label{tab:hb_main}
255	\begin{tabular}{llcccc}
256	\toprule
257	Regime & $n$ & HB/MLE & HB Cov. & MLE Cov. & Lap.\ Cov. \\
258	\midrule
259	Extreme & 100 & 0.72 (0.02) & 0.90 & 0.79 & 0.84 \\
260	Extreme & 250 & 0.88 (0.01) & 0.91 & 0.83 & 0.87 \\
261	Extreme & 500 & 0.95 (0.01) & 0.93 & 0.89 & 0.91 \\
262	Extreme & 1000 & 0.98 (0.01) & 0.94 & 0.93 & 0.93 \\
263	Moderate & 250 & 0.93 (0.01) & 0.92 & 0.87 & 0.89 \\
264	Homogeneous & 250 & 0.99 (0.01) & 0.94 & 0.93 & 0.93 \\
265	\bottomrule
266	\end{tabular}
267	\end{table}
268	
269	\begin{table}[t]
270	\centering
271	\small
272	\caption{HB vs.\ MLE: RMSE ratio and coverage ($K=4$, extreme regime).}
273	\label{tab:hb_k4}
274	\begin{tabular}{lcccc}
275	\toprule
276	$n$ & HB/MLE & HB Cov. & MLE Cov. \\
277	\midrule
278	100 & 0.65 (0.02) & 0.88 & 0.72 \\
279	250 & 0.82 (0.01) & 0.89 & 0.80 \\
280	500 & 0.91 (0.01) & 0.91 & 0.86 \\
281	1000 & 0.97 (0.01) & 0.93 & 0.91 \\
282	\bottomrule
283	\end{tabular}
284	\end{table}
285	
286	Tables~\ref{tab:hb_main} and \ref{tab:hb_k4} summarize the results.
287	HB partial pooling provides the largest RMSE advantage at small $n$ and high $K$: at $n=100, K=4$, HB achieves 35\% lower RMSE than MLE (ratio 0.65).
288	The advantage diminishes as $n$ grows---at $n=1000, K=2$, HB and MLE are nearly equivalent (ratio 0.98)---confirming that HB's value lies in the small-sample regime where MLE estimates become unstable.
289	
290	Coverage is consistently closer to nominal 95\% for HB (88--94\%) than for MLE (72--93\%), though mild undercoverage persists due to the delta-method approximation underestimating nonlinear error propagation through matrix inversion.
291	MCMC diagnostics are clean across all settings ($\hat{R}_{\max} = 1.003$, $\text{ESS}_{\text{bulk}} \geq 380$, $\text{ESS}_{\text{tail}} \geq 220$, zero divergences).
292	
293	\paragraph{Runtime.}
294	HB is $\sim$210$\times$ slower than MLE per replication (4.2s vs.\ 0.02s), which is substantial in simulation studies but acceptable in practice where the model is fit once.
295	
296	\subsection{Semi-Synthetic Political Science Benchmark}
297	\label{sec:semisynthetic}
298	
299	We construct a semi-synthetic benchmark from 12{,}000 political-science tweets with injected CATE heterogeneity ($\tau_1 = 0.15$, $\tau_2 = 0.35$, $\Delta\tau = 0.20$), annotated by GPT-4.1 and Qwen3-235B-A22B, with 500 expert labels for calibration.
300	
301	\begin{table}[t]
302	\centering
303	\small
304	\caption{Semi-synthetic benchmark: subgroup CATE estimation ($K=2$, $n_{\text{expert}}=500$). Standard errors in parentheses.}
305	\label{tab:semisynthetic}
306	\begin{tabular}{lcccc}
307	\toprule
308	Method & SG1 Bias & SG2 Bias & RMSE & Cov. \\
309	\midrule
310	No correction & 0.08 (0.02) & $-$0.11 (0.02) & 0.145 & 0.85 \\
311	Global correction & $-$0.14 (0.03) & 0.15 (0.03) & 0.198 & 0.78 \\
312	MLE stratified & 0.02 (0.03) & $-$0.03 (0.03) & 0.078 & 0.87 \\
313	HB stratified (EC-HTE) & 0.01 (0.02) & $-$0.02 (0.02) & 0.072 & 0.91 \\
314	Oracle stratified & 0.00 (0.01) & 0.00 (0.01) & 0.035 & 0.95 \\
315	\bottomrule
316	\end{tabular}
317	\end{table}
318	
319	\begin{table}[t]
320	\centering
321	\small
322	\caption{LLM annotation quality by subgroup.}
323	\label{tab:llm_quality}
324	\begin{tabular}{lcccccc}
325	\toprule
326	LLM & Acc. & SG1 Acc. & SG2 Acc. & $\Delta\pi_{\max}$ & Ampl. \\
327	\midrule
328	GPT-4.1 & 0.82 & 0.88 & 0.75 & 0.09 & 2.8$\times$ \\
329	Qwen3-235B & 0.76 & 0.83 & 0.67 & 0.13 & 3.6$\times$ \\
330	\bottomrule
331	\end{tabular}
332	\end{table}
333	
334	Table~\ref{tab:semisynthetic} demonstrates the core finding: global correction \emph{increases} RMSE from 0.145 to 0.198, while EC-HTE reduces it to 0.072.
335	The bias mechanism is regime-dependent: Qwen3-235B, with larger misclassification heterogeneity ($\Delta\pi_{\max} = 0.13$), exhibits $3.6\times$ bias amplification under global correction versus $2.8\times$ for GPT-4.1 (Table~\ref{tab:llm_quality}).
336	This confirms the theoretical prediction that lower-quality annotators with more heterogeneous errors benefit most from stratified correction.
337	
338	The gap between EC-HTE (0.072) and oracle (0.035) reflects the noise floor from confusion matrix estimation with finite expert labels---more expert labels monotonically improve performance.
339	
340	\subsection{Real-Data Validation: Rohingya Refugee Interviews}
341	\label{sec:real}
342	
343	We apply EC-HTE to the \citet{ashwin2025using} dataset of 1{,}800 Rohingya refugee interviews with 400 expert-coded labels, 5-class annotation, and subgroups defined by refugee status $\times$ gender.
344	
345	\begin{table}[t]
346	\centering
347	\small
348	\caption{Ashwin et al.\ real data: worst-subgroup CATE bias by method.}
349	\label{tab:real}
350	\begin{tabular}{lcccc}
351	\toprule
352	Method & Worst SG bias & Mean $|$bias$|$ & Cov. & CI width \\
353	\midrule
354	No correction & 0.09 & 0.06 & 0.86 & 0.28 \\
355	Global correction & 0.22 & 0.14 & 0.74 & 0.25 \\
356	MLE stratified & 0.07 & 0.05 & 0.83 & 0.35 \\
357	HB stratified (EC-HTE) & 0.05 & 0.03 & 0.90 & 0.32 \\
358	\bottomrule
359	\end{tabular}
360	\end{table}
361	
362	Table~\ref{tab:real} shows that global correction increases worst-subgroup bias from 0.09 to 0.22 ($3.1\times$ amplification), systematically under-correcting female refugees while over-correcting male host community members.
363	EC-HTE reduces worst-subgroup bias to 0.05 and improves coverage from 74\% to 90\%.
364	The difference between EC-HTE and MLE stratified is directionally correct but not statistically significant ($p = 0.18$), consistent with the moderate sample size (400 expert labels across 4 subgroups $\approx$ 100 per cell).
365	
366	The substantive implication is consequential: global correction would lead researchers to \emph{reverse} the subgroup priority ranking, underestimating treatment effects for the most vulnerable population (female refugees) while overestimating effects for the least vulnerable (male host community).
367	
368	\subsection{Expert Label Budget Sensitivity}
369	\label{sec:budget}
370	
371	We sweep $n_{\text{expert}} \in \{50, 100, 250, 500, 1000, 2000\}$ across $K \in \{2, 4, 8\}$ to identify the crossover point where EC-HTE outperforms global correction.
372	
373	\begin{table}[t]
374	\centering
375	\small
376	\caption{Crossover expert budget by $K$ and regime.}
377	\label{tab:crossover}
378	\begin{tabular}{llcc}
379	\toprule
380	$K$ & Regime & Crossover $n$ & HB advantage \\
381	\midrule
382	2 & Extreme & 180 & 15\% \\
383	2 & Moderate & 350 & 10\% \\
384	4 & Extreme & 320 & 22\% \\
385	4 & Moderate & 480 & 16\% \\
386	8 & Extreme & 600 & 28\% \\
387	8 & Moderate & $>$1000 & --- \\
388	\bottomrule
389	\end{tabular}
390	\end{table}
391	
392	For typical NLP-CSS studies ($K = 2\text{--}4$ subgroups, moderate heterogeneity), 250--500 expert labels constitute the minimum viable budget for EC-HTE (Table~\ref{tab:crossover}).
393	At $K = 8$ with moderate heterogeneity, the crossover exceeds $n = 1000$, making EC-HTE impractical unless heterogeneity is extreme.
394	This motivates the diagnostic criterion: practitioners should first assess $\Delta\pi \times \Delta\tau$ and then decide on the granularity of subgroup stratification.
395	
396	A critical safety property: HB is never worse than global correction in any tested setting, while MLE stratified correction \emph{can} be worse than global at $n = 50$ for $K \geq 4$ due to unstable confusion matrix estimates.
397	
398	\subsection{PPCI Baseline Comparison}
399	\label{sec:ppci}
400	
401	We conduct a head-to-head comparison with PPCI \citep{sui2026prediction}, which corrects outcome-side measurement error via kernel localization.
402	Table~\ref{tab:ppci} disaggregates performance by error type: covariate-only, outcome-only, and both.
403	
404	\begin{table}[t]
405	\centering
406	\small
407	\caption{EC-HTE vs.\ PPCI by error type ($K=2$, $n_{\text{expert}}=500$). Values are mean absolute bias.}
408	\label{tab:ppci}
409	\begin{tabular}{lccccc}
410	\toprule
411	Error Type & None & Global & EC-HTE & PPCI & Combined \\
412	\midrule
413	Covariate only & 0.12 & 0.19 & \textbf{0.04} & 0.16 & --- \\
414	Cov.\ (high corr.) & 0.12 & 0.19 & \textbf{0.04} & 0.11 & --- \\
415	Outcome only & 0.13 & 0.15 & 0.14 & \textbf{0.05} & --- \\
416	Both & 0.18 & 0.24 & 0.13 & 0.15 & \textbf{0.08} \\
417	\bottomrule
418	\end{tabular}
419	\end{table}
420	
421	\begin{table}[t]
422	\centering
423	\small
424	\caption{Coverage by error type and correction method.}
425	\label{tab:ppci_coverage}
426	\begin{tabular}{lccc}
427	\toprule
428	Error Type & EC-HTE & PPCI & Combined \\
429	\midrule
430	Covariate only & 0.91 & 0.80 & --- \\
431	Outcome only & 0.82 & 0.93 & --- \\
432	Both & 0.85 & 0.83 & 0.88 \\
433	\bottomrule
434	\end{tabular}
435	\end{table}
436	
437	The methods are complementary but \emph{not} fully orthogonal.
438	EC-HTE dominates on covariate-side error (bias 0.04 vs.\ 0.16), while PPCI dominates on outcome-side error (0.05 vs.\ 0.14).
439	Notably, PPCI provides partial correction for covariate error when covariate and outcome errors are correlated (bias 0.11 vs.\ 0.16 without correlation), because kernel localization indirectly captures some covariate-side heterogeneity---but EC-HTE remains $3\times$ more effective (0.04 vs.\ 0.11).
440	When both error types are present, sequential application (EC-HTE then PPCI) reduces bias to 0.08, outperforming either method alone (Table~\ref{tab:ppci}).
441	Coverage under combination (0.88; Table~\ref{tab:ppci_coverage}) degrades slightly due to compounding uncertainty from two correction stages.
442	
443	\subsection{Multiple LLM Annotator Comparison}
444	\label{sec:multi_llm}
445	
446	We compare three LLMs and a majority-vote ensemble to characterize how annotator quality modulates EC-HTE benefit.
447	
448	\begin{table}[t]
449	\centering
450	\small
451	\caption{LLM annotator comparison: quality, heterogeneity, and EC-HTE benefit.}
452	\label{tab:multi_llm}
453	\begin{tabular}{lccccc}
454	\toprule
455	LLM & Acc. & $\Delta\pi_{\max}$ & Ampl. & RMSE Gain \\
456	\midrule
457	GPT-4.1 & 0.82 & 0.09 & 2.8$\times$ & 0.08 \\
458	Claude Sonnet 4.6 & 0.79 & 0.11 & 3.1$\times$ & 0.11 \\
459	Qwen3-235B & 0.76 & 0.13 & 3.6$\times$ & 0.15 \\
460	Majority Vote & 0.85 & 0.07 & 2.1$\times$ & 0.05 \\
461	\bottomrule
462	\end{tabular}
463	\end{table}
464	
465	EC-HTE benefit is strongly negatively correlated with annotator accuracy ($r = -0.92$) and positively correlated with $\Delta\pi$ ($r = 0.88$; Table~\ref{tab:multi_llm}).
466	Lower-quality annotators with more heterogeneous errors benefit most from stratified correction.
467	Majority-vote ensembling improves accuracy (0.85) and reduces heterogeneity ($\Delta\pi = 0.07$) but does not eliminate it---bias amplification remains $2.1\times$, confirming that ensembling is not a substitute for stratified correction.
468	
469	\subsection{Robustness to Subgroup Misspecification}
470	\label{sec:robustness}
471	
472	A key practical concern is sensitivity to imperfect subgroup definitions.
473	We test three forms of misspecification: (i) noisy subgroup labels (10--30\% noise), (ii) misspecified $K$ (true $K=4$, model uses $K \in \{2, 8\}$), and (iii) incorrect discretization of a continuous moderator.
474	
475	\begin{table}[t]
476	\centering
477	\small
478	\caption{EC-HTE RMSE under subgroup misspecification.}
479	\label{tab:robustness}
480	\begin{tabular}{lcccc}
481	\toprule
482	Scenario & Clean & Mild & Moderate & Severe \\
483	\midrule
484	SG noise & 0.072 & 0.085 (10\%) & 0.105 (20\%) & 0.132 (30\%) \\
485	$K$ misspec. & 0.082 ($K\!=\!4$) & 0.098 ($K\!=\!2$) & 0.095 ($K\!=\!8$) & --- \\
486	Discretization & 0.075 (correct) & 0.092 (coarse) & 0.098 (fine) & --- \\
487	\bottomrule
488	\end{tabular}
489	\end{table}
490	
491	\begin{table}[t]
492	\centering
493	\small
494	\caption{HB vs.\ MLE degradation under misspecification.}
495	\label{tab:robustness_hb_mle}
496	\begin{tabular}{lcc}
497	\toprule
498	Misspecification & HB increase & MLE increase \\
499	\midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "532470f2-d653-4e5b-93a5-38ccddbe0887",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "aa0925cd-8e0f-4589-886d-7ffd3e487882",
  "sourceToolAssistantUUID": "532470f2-d653-4e5b-93a5-38ccddbe0887",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T20:27:15.188Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PZhFi7W655n63X6rvDWrw8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/median/paper.tex",
  "offset": 499,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa0925cd-8e0f-4589-886d-7ffd3e487882",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET4zX9tvVgcGLm7eMPP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3e19de19-6eb2-41d3-b63f-53547e67f655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRRC7hKkJ2CTm1Dz53mF35",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12547,
      "cache_read_input_tokens": 27943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12547,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 37,
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

_source line 22 · 2026-05-20T20:27:15.202Z_

<details><summary>↩ Tool result · `toolu_01PZhFi7W655n63X6rvDWrw8`</summary>

```text
499	\midrule
500	10\% subgroup noise & 15\% & 25\% \\
501	20\% subgroup noise & 30\% & 50\% \\
502	$K\!=\!4 \to K\!=\!2$ & 18\% & 30\% \\
503	\bottomrule
504	\end{tabular}
505	\end{table}
506	
507	EC-HTE degrades gracefully under misspecification (Table~\ref{tab:robustness}).
508	At 10\% subgroup noise, RMSE increases by 18\% (0.072 $\to$ 0.085)---compared to global correction, which becomes harmful at just 5\% misclassification heterogeneity.
509	EC-HTE does not become worse than no correction until noise reaches approximately 35\%.
510	
511	HB consistently degrades less than MLE under all forms of misspecification (Table~\ref{tab:robustness_hb_mle}): 15\% vs.\ 25\% RMSE increase at 10\% noise, 18\% vs.\ 30\% under $K$ misspecification.
512	This is because partial pooling automatically shrinks noisy subgroup estimates toward the global, damping the effect of misspecification rather than fitting to it.
513	
514	\subsection{Causal Forest Integration}
515	\label{sec:cf}
516	
517	We demonstrate that EC-HTE is estimator-agnostic by integrating it with CausalForestDML.
518	
519	\begin{table}[t]
520	\centering
521	\small
522	\caption{EC-HTE with CausalForestDML: subgroup and leaf-level results.}
523	\label{tab:cf}
524	\begin{tabular}{lcccc}
525	\toprule
526	Level & Naive & Global & EC-HTE & Oracle \\
527	\midrule
528	SG CATE bias & 0.12 & 0.17 & 0.06 & 0.03 \\
529	SG coverage & 0.82 & 0.75 & 0.90 & 0.94 \\
530	Leaf RMSE & 0.22 & 0.26 & 0.18 & 0.14 \\
531	Leaf coverage & 0.79 & 0.72 & 0.87 & 0.93 \\
532	\bottomrule
533	\end{tabular}
534	\end{table}
535	
536	The bias mechanism operates identically with causal forests: global correction worsens subgroup CATE bias (0.17 vs.\ 0.12 naive), while EC-HTE halves it (0.06; Table~\ref{tab:cf}).
537	At the leaf level, improvement is more modest (RMSE 0.18 vs.\ 0.22 naive) because leaf granularity exceeds the resolution of subgroup-level confusion matrix estimation.
538	Causal forests provide a modest 10\% advantage over difference-in-means when combined with EC-HTE, confirming that the correction method matters more than the CATE estimator choice.
539	
540	\subsection{Adaptive Expert Annotation Allocation}
541	\label{sec:adaptive}
542	
543	We compare uniform allocation of expert labels across subgroups with uncertainty-weighted and CATE-weighted adaptive allocation strategies.
544	
545	\begin{table}[t]
546	\centering
547	\small
548	\caption{Allocation strategy comparison ($n_{\text{expert}}=250$, $K=4$, extreme regime).}
549	\label{tab:allocation}
550	\begin{tabular}{lcc}
551	\toprule
552	Strategy & RMSE & Improvement \\
553	\midrule
554	Uniform & 0.082 & --- \\
555	Uncertainty-only & 0.075 & 8.5\% \\
556	CATE-weighted & 0.071 & 13.4\% \\
557	Oracle & 0.065 & 20.7\% \\
558	\bottomrule
559	\end{tabular}
560	\end{table}
561	
562	CATE-weighted allocation provides 13.4\% RMSE improvement over uniform allocation (Table~\ref{tab:allocation}), but the marginal gain over simpler uncertainty-based allocation is modest (5.3 percentage points).
563	The CATE-weighted strategy requires a 15\% pilot phase to estimate CATE heterogeneity before allocating the remaining budget, which further reduces the effective sample.
564	We view adaptive allocation as a useful extension for budget-constrained settings but not a primary contribution.
565	
566	%=============================================================================
567	% 7. DISCUSSION & LIMITATIONS
568	%=============================================================================
569	\section{Discussion}
570	
571	\paragraph{When to use EC-HTE.}
572	The diagnostic product $\Delta\pi \times \Delta\tau$ provides a practical screening tool, but 35\% of realistic settings fall in a gray zone where the recommendation is ambiguous.
573	In such cases, we recommend defaulting to EC-HTE given its never-worse-than-global guarantee---the computational overhead (4.2s per fit) is negligible in practice.
574	
575	\paragraph{Limitations.}
576	(1) Coverage remains mildly below nominal (88--94\% vs.\ 95\%) due to the delta-method approximation; posterior predictive checks offer a practical calibration tool.
577	(2) For $K > 4$ with moderate heterogeneity, the required expert budget may exceed practical limits.
578	(3) The $\Delta\pi \times \Delta\tau$ characterization is a first-order approximation; full characterization for $K > 2$ remains open.
579	(4) Real-data validation, while directionally supportive, lacks statistical power to demonstrate significant EC-HTE advantage over MLE stratified correction.
580	(5) HB runtime overhead ($\sim$210$\times$ MLE) is irrelevant for single-fit applications but prohibitive for large-scale simulation.
581	
582	%=============================================================================
583	% 8. CONCLUSION
584	%=============================================================================
585	\section{Conclusion}
586	
587	We identify and formalize a bias mechanism in LLM-assisted heterogeneous treatment effect estimation: global confusion-matrix correction amplifies subgroup CATE bias by up to $4\text{--}5\times$ when misclassification rates vary across subgroups.
588	EC-HTE addresses this via hierarchical Bayesian stratified correction with an automatic robustness guarantee.
589	The $\Delta\pi \times \Delta\tau$ diagnostic provides practitioners a screening tool to assess when stratified correction is needed, with AUC = 0.82 across synthetic, semi-synthetic, and real-data settings.
590	Validation on political-science tweets and refugee interview data demonstrates that the bias mechanism has substantive consequences---incorrectly ranking subgroup treatment effects---and that EC-HTE effectively mitigates it.
591	
592	%=============================================================================
593	% REFERENCES
594	%=============================================================================
595	\bibliographystyle{plainnat}
596	\begin{thebibliography}{20}
597	
598	\bibitem[Angelopoulos et~al.(2023)]{angelopoulos2023prediction}
599	A.~N. Angelopoulos, S.~Bates, C.~Fannjiang, M.~I. Jordan, and T.~Zrnic.
600	\newblock Prediction-powered inference.
601	\newblock \emph{Science}, 382(6671):669--674, 2023.
602	
603	\bibitem[Ashwin et~al.(2025)]{ashwin2025using}
604	A.~Ashwin, M.~Banerjee, and R.~Hanna.
605	\newblock Using {LLM} annotations in social science research: Evidence from a refugee interview study.
606	\newblock Working paper, 2025.
607	
608	\bibitem[Athey et~al.(2019)]{athey2019generalized}
609	S.~Athey, J.~Tibshirani, and S.~Wager.
610	\newblock Generalized random forests.
611	\newblock \emph{Annals of Statistics}, 47(2):1148--1178, 2019.
612	
613	\bibitem[Bu et~al.(2023)]{bu2023estimating}
614	Z.~Bu, D.~Klusowski, and J.~Wu.
615	\newblock Estimating treatment effects using machine learning-generated covariates.
616	\newblock \emph{arXiv preprint arXiv:2310.08724}, 2023.
617	
618	\bibitem[Carroll et~al.(2006)]{carroll2006measurement}
619	R.~J. Carroll, D.~Ruppert, L.~A. Stefanski, and C.~M. Crainiceanu.
620	\newblock \emph{Measurement Error in Nonlinear Models: A Modern Perspective}.
621	\newblock Chapman \& Hall/CRC, 2nd edition, 2006.
622	
623	\bibitem[Dawid and Skene(1979)]{dawid1979maximum}
624	A.~P. Dawid and A.~M. Skene.
625	\newblock Maximum likelihood estimation of observer error-rates using the {EM} algorithm.
626	\newblock \emph{Journal of the Royal Statistical Society: Series C}, 28(1):20--28, 1979.
627	
628	\bibitem[Egami et~al.(2024)]{egami2024using}
629	N.~Egami, M.~Hinck, B.~Stewart, and H.~Wei.
630	\newblock Using imperfect surrogates for downstream inference: Design-based supervised learning for social science applications of large language models.
631	\newblock In \emph{NeurIPS}, 2024.
632	
633	\bibitem[Mozer(2026)]{mozer2026adjusting}
634	R.~Mozer.
635	\newblock Adjusting for differential prediction error in treatment effect estimation.
636	\newblock \emph{Journal of Causal Inference}, 2026.
637	
638	\bibitem[Paun et~al.(2018)]{paun2018comparing}
639	S.~Paun, B.~Carpenter, J.~Curber, and D.~Hovy.
640	\newblock Comparing {B}ayesian models of annotation.
641	\newblock \emph{Transactions of the ACL}, 6:571--585, 2018.
642	
643	\bibitem[Sui et~al.(2026)]{sui2026prediction}
644	Y.~Sui, T.~Chen, and M.~Yang.
645	\newblock Prediction-powered conditional inference.
646	\newblock In \emph{ICML}, 2026.
647	
648	\bibitem[Ziems et~al.(2024)]{ziems2024can}
649	C.~Ziems, W.~Held, O.~Shaikh, J.~Chen, Z.~Zhang, and D.~Yang.
650	\newblock Can large language models transform computational social science?
651	\newblock \emph{Computational Linguistics}, 50(1):237--291, 2024.
652	
653	\end{thebibliography}
654	
655	\end{document}
656	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e19de19-6eb2-41d3-b63f-53547e67f655",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "c025b4cb-7a1b-4d17-9b61-8d5617649d5f",
  "sourceToolAssistantUUID": "3e19de19-6eb2-41d3-b63f-53547e67f655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T20:27:15.652Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Hzr9aF1GDYLU2p2bDZzdVV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper.tex",
  "offset": 497,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c025b4cb-7a1b-4d17-9b61-8d5617649d5f",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET4zX9tvVgcGLm7eMPP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a5d95b3-981b-4d62-b77c-5401855fb44c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRRC7hKkJ2CTm1Dz53mF35",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12547,
      "cache_read_input_tokens": 27943,
      "output_tokens": 255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12547
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 255,
          "cache_read_input_tokens": 27943,
          "cache_creation_input_tokens": 12547,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12547,
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

_source line 24 · 2026-05-20T20:27:15.665Z_

<details><summary>↩ Tool result · `toolu_01Hzr9aF1GDYLU2p2bDZzdVV`</summary>

```text
497	\section*{Limitations}
498	
499	EC-HTE requires subgroup structure to be defined \emph{a priori}. When $K$ is large relative to expert label budget (e.g., $K=8$ with only 50 labels), per-subgroup estimation degrades and EC-HTE may perform worse than global correction (breakeven at $\sim$38\% subgroup label noise; see Appendix~\ref{app:robustness}). The method adds computational cost ($\sim$2.3s per MCMC fit vs.\ 0.008s for MLE), though this is negligible relative to LLM annotation costs. Our semi-synthetic and real-data experiments use binary or small-$K$ subgroups; extension to high-dimensional continuous effect modifiers remains future work.
500	
501	\section*{Ethics Statement}
502	
503	Our method improves the accuracy of causal effect estimates for marginalized subgroups that disproportionately suffer from LLM annotation errors. The refugee interview data are used with appropriate permissions following \citet{ashwin2025refugee}. We note that improved subgroup CATE estimates could be misused to target interventions in harmful ways; responsible deployment requires domain expertise and ethical oversight.
504	
505	\begin{thebibliography}{20}
506	\bibitem[\protect\citeauthoryear{Angelopoulos et al.}{2023}]{angelopoulos2023ppi}
507	Anastasios~N. Angelopoulos, Stephen Bates, Clara Fannjiang, Michael~I. Jordan, and Tijana Zrnic. 2023.
508	\newblock Prediction-powered inference.
509	\newblock \emph{Science}, 382(6671):669--674.
510	
511	\bibitem[\protect\citeauthoryear{Ashwin et al.}{2025}]{ashwin2025refugee}
512	Ashwin, Maaz et al. 2025.
513	\newblock Differential {LLM} annotation errors across demographic subgroups in refugee interview data.
514	\newblock \emph{Working paper}.
515	
516	\bibitem[\protect\citeauthoryear{Bu et al.}{2023}]{bu2023forestiv}
517	Zhixuan Bu, David Simchi-Levi, and Claire Squires. 2023.
518	\newblock {ForestIV}: Instrumental variable estimation using random forests with application to {ML}-generated covariates.
519	\newblock \emph{arXiv preprint arXiv:2310.08709}.
520	
521	\bibitem[\protect\citeauthoryear{Carroll et al.}{2006}]{carroll2006measurement}
522	Raymond~J. Carroll, David Ruppert, Leonard~A. Stefanski, and Ciprian~M. Crainiceanu. 2006.
523	\newblock \emph{Measurement Error in Nonlinear Models: A Modern Perspective}.
524	\newblock Chapman and Hall/CRC, 2nd edition.
525	
526	\bibitem[\protect\citeauthoryear{Dawid and Skene}{1979}]{dawid1979maximum}
527	Alexander~Philip Dawid and Allan~M. Skene. 1979.
528	\newblock Maximum likelihood estimation of observer error-rates using the {EM} algorithm.
529	\newblock \emph{Journal of the Royal Statistical Society: Series C}, 28(1):20--28.
530	
531	\bibitem[\protect\citeauthoryear{Egami et al.}{2024}]{egami2024dsl}
532	Naoki Egami, Musashi Hinck, Brandon Stewart, and Hanying Wei. 2024.
533	\newblock Using imperfect surrogates for downstream inference: Design-based supervised learning for social science applications of large language models.
534	\newblock In \emph{Advances in Neural Information Processing Systems}.
535	
536	\bibitem[\protect\citeauthoryear{Mozer}{2026}]{mozer2026arm}
537	Reagan Mozer. 2026.
538	\newblock Arm-specific rectifiers for causal inference with prediction-derived treatments.
539	\newblock \emph{Journal of Causal Inference}, forthcoming.
540	
541	\bibitem[\protect\citeauthoryear{Paun et al.}{2018}]{paun2018comparing}
542	Silviu Paun, Bob Carpenter, Jon Chamberlain, Dirk Hovy, Udo Kruschwitz, and Massimo Poesio. 2018.
543	\newblock Comparing {Bayesian} models of annotation.
544	\newblock \emph{Transactions of the Association for Computational Linguistics}, 6:571--585.
545	
546	\bibitem[\protect\citeauthoryear{Sui et al.}{2026}]{sui2026ppci}
547	Yi Sui, Congbo Ma, Yifan Zhu, and Lei Zhong. 2026.
548	\newblock Prediction-powered conditional inference.
549	\newblock In \emph{Proceedings of NeurIPS 2026}.
550	\end{thebibliography}
551	
552	\appendix
553	
554	\section{Expert Label Budget Sensitivity}
555	\label{app:budget}
556	
557	\begin{table}[h]
558	\centering
559	\small
560	\begin{tabular}{ccccc}
561	\toprule
562	$n$ & $n/K$ & EC-HTE & Global & Better? \\
563	\midrule
564	50 & 25 & .031 & .042 & \checkmark \\
565	100 & 50 & .022 & .042 & \checkmark \\
566	250 & 125 & .015 & .042 & \checkmark \\
567	500 & 250 & .011 & .042 & \checkmark \\
568	1000 & 500 & .008 & .042 & \checkmark \\
569	2000 & 1000 & .006 & .042 & \checkmark \\
570	\bottomrule
571	\end{tabular}
572	\caption{Crossover analysis ($K=2$, extreme regime). EC-HTE outperforms global correction at all tested budget levels. Crossover occurs at $n \approx 85$ ($\sim$42 labels per subgroup).}
573	\label{tab:budget_k2}
574	\end{table}
575	
576	\begin{table}[h]
577	\centering
578	\small
579	\begin{tabular}{cccc}
580	\toprule
581	$K$ & Crossover $n$ & $n/K$ & EC-HTE RMSE \\
582	\midrule
583	2 & 85 & 42 & .041 \\
584	4 & 140 & 35 & .041 \\
585	8 & 210 & 26 & .041 \\
586	\bottomrule
587	\end{tabular}
588	\caption{Crossover budget scales sub-linearly with $K$ due to HB partial pooling.}
589	\label{tab:budget_crossover}
590	\end{table}
591	
592	For $K=8$ with only 50 labels ($\sim$6 per subgroup), EC-HTE RMSE (0.058) exceeds global RMSE (0.042). HB still outperforms MLE (0.093) by 39\%, but the fundamental sample-size limit prevents reliable stratification. We recommend $n \geq 30K$ as a practical guideline.
593	
594	\section{Multiple LLM Comparison}
595	\label{app:multilm}
596	
597	\begin{table}[h]
598	\centering
599	\small
600	\begin{tabular}{lcccc}
601	\toprule
602	LLM & Acc. & $\Delta\pi$ & Ampl. & EC-HTE \\
603	\midrule
604	GPT-4.1 & .87 & .15 & 5.4$\times$ & 89\% \\
605	Qwen3-235B & .82 & .17 & 6.9$\times$ & 92\% \\
606	Claude Sonnet 4.6 & .89 & .11 & 4.1$\times$ & 85\% \\
607	\bottomrule
608	\end{tabular}
609	\caption{Even the most accurate LLM (Claude Sonnet 4.6) produces 4.1$\times$ bias amplification under global correction. Cross-LLM error pattern correlations range from 0.68 to 0.74, suggesting subgroup heterogeneity is structural rather than model-specific.}
610	\label{tab:multilm}
611	\end{table}
612	
613	\section{Robustness to Misspecified Subgroups}
614	\label{app:robustness}
615	
616	\begin{table}[h]
617	\centering
618	\small
619	\setlength{\tabcolsep}{3.5pt}
620	\begin{tabular}{lcccc}
621	\toprule
622	Scenario & EC-HTE & Global & Better? & Degrad. \\
623	\midrule
624	Oracle ($K=4$) & .014 & .042 & \checkmark & --- \\
625	Coarsened ($K=2$) & .019 & .042 & \checkmark & +36\% \\
626	Noise 10\% & .016 & .042 & \checkmark & +14\% \\
627	Noise 20\% & .021 & .042 & \checkmark & +50\% \\
628	Noise 30\% & .028 & .042 & \checkmark & +100\% \\
629	Noise 38\% & .042 & .042 & --- & breakeven \\
630	Continuous, $K{=}4$ bins & .017 & .042 & \checkmark & +21\% \\
631	\bottomrule
632	\end{tabular}
633	\caption{EC-HTE degrades gracefully under subgroup misspecification. Breakeven occurs at 38\% subgroup label noise, far beyond realistic scenarios. HB shrinkage provides automatic robustness.}
634	\label{tab:robustness}
635	\end{table}
636	
637	\section{Adaptive Expert Allocation}
638	\label{app:adaptive}
639	
640	CATE-weighted allocation assigns more expert labels to high-CATE $\times$ high-error subgroups. With $K=4$ and $n=250$, CATE-weighted allocation achieves RMSE 0.020 (vs.\ 0.027 uniform), equivalent to 340 uniformly-allocated labels---a 36\% efficiency gain.
641	
642	\begin{table}[h]
643	\centering
644	\small
645	\setlength{\tabcolsep}{3pt}
646	\begin{tabular}{lcccc}
647	\toprule
648	Strategy & $n$ & Allocation & RMSE & Cov. \\
649	\midrule
650	Uniform & 250 & [62,63,62,63] & .027 & .940 \\
651	Uncertainty & 250 & [78,72,55,45] & .023 & .945 \\
652	CATE-weighted & 250 & [95,75,50,30] & .020 & .948 \\
653	Uniform (matched) & 340 & [85,85,85,85] & .020 & .949 \\
654	\bottomrule
655	\end{tabular}
656	\caption{Adaptive allocation strategies ($K=4$, extreme regime).}
657	\label{tab:adaptive}
658	\end{table}
659	
660	\end{document}
661	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a5d95b3-981b-4d62-b77c-5401855fb44c",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "6a217053-9d85-43a2-b96d-c7b71ca241ad",
  "sourceToolAssistantUUID": "1a5d95b3-981b-4d62-b77c-5401855fb44c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-20T20:27:19.231Z_

Now let me also read the worst-case paper and check for any additional project files that might inform the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a217053-9d85-43a2-b96d-c7b71ca241ad",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET5SRtK919jTmZMm3J7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1586b01d-de77-4079-8132-fc0be73c4b84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VruNJC3gNd4nEyi93zFdhn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6333,
      "cache_read_input_tokens": 40490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6333,
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

_source line 26 · 2026-05-20T20:27:22.086Z_

<details open><summary>🔧 Tool call — Read · `toolu_0139etH3eoC3FzByqMGwoC2X`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/worst/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1586b01d-de77-4079-8132-fc0be73c4b84",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET5SRtK919jTmZMm3J7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aeb02201-d560-435d-8acf-d91947a6176c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VruNJC3gNd4nEyi93zFdhn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6333,
      "cache_read_input_tokens": 40490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6333,
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

_source line 27 · 2026-05-20T20:27:22.111Z_

<details><summary>↩ Tool result · `toolu_0139etH3eoC3FzByqMGwoC2X`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{amsmath,amssymb,amsfonts,amsthm}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{graphicx}
9	\usepackage{hyperref}
10	\usepackage{natbib}
11	\usepackage[margin=2.5cm]{geometry}
12	\usepackage{caption}
13	\usepackage{subcaption}
14	\usepackage{xcolor}
15	
16	\newtheorem{proposition}{Proposition}
17	
18	\title{When Does Subgroup-Stratified Correction Matter\\for LLM-Annotated Heterogeneous Treatment Effects?}
19	
20	\author{Anonymous}
21	
22	\date{}
23	
24	\begin{document}
25	\maketitle
26	
27	\begin{abstract}
28	LLM annotations are increasingly used as effect modifiers in heterogeneous treatment effect (HTE) analysis, yet LLM misclassification rates vary across subgroups. A natural concern is that applying a global (pooled) confusion-matrix correction to subgroup-level conditional average treatment effects (CATEs) may introduce systematic bias. We formalize this bias mechanism and derive an analytic bound showing that the additional bias from global correction is proportional to the product of misclassification heterogeneity ($\Delta\pi$) and CATE heterogeneity ($\Delta\tau$). We propose EC-HTE, a hierarchical Bayesian subgroup-stratified correction framework, and evaluate it across synthetic, semi-synthetic, and real-data experiments with three frontier LLMs (GPT-4.1, Qwen3-235B, Claude Sonnet 4.6). Our central finding is \emph{negative}: on typical computational social science tasks, current LLMs exhibit limited misclassification heterogeneity (max/min accuracy ratios of 1.10--1.18), and global correction's additional bias is small (amplification factors of 1.05--1.15$\times$). EC-HTE provides a modest improvement (22--38\% subgroup bias reduction) but requires substantial expert labels (crossover at $n \geq 750$ for $K{=}2$ in moderate regimes) and is sensitive to subgroup misspecification. We characterize the conditions under which stratified correction becomes necessary and argue that, for most current LLM annotation pipelines, global correction suffices---a reassuring finding for practitioners, and a formal boundary condition for future work.
29	\end{abstract}
30	
31	\section{Introduction}
32	
33	Researchers in computational social science (CSS) increasingly rely on large language models to annotate text variables that serve as effect modifiers in causal analyses~\citep{egami2024using,ziems2024can}. For example, whether a political tweet contains ``economic framing'' may moderate the effect of a campaign on voter engagement. When LLM annotations replace expert labels, measurement error propagates into treatment effect estimates.
34	
35	Several correction methods address this propagation. Prediction-powered inference~\citep[PPI;][]{angelopoulos2023prediction} and design-based supervised learning~\citep[DSL;][]{egami2024using} correct population-level estimates assuming homogeneous measurement error. \citet{mozer2026arm} extend rectifiers to arm-specific prediction error for average treatment effects (ATEs). PPCI~\citep{sui2026ppci} handles outcome-side measurement error for conditional functionals via kernel localization.
36	
37	A gap remains: none of these methods address the case where the \emph{mismeasured variable defines the heterogeneity structure itself}. When an LLM-annotated effect modifier has subgroup-varying error rates, applying a pooled correction to subgroup-level CATEs could, in principle, over-correct low-error subgroups and under-correct high-error ones. This raises a natural question: \textbf{when does this bias mechanism matter in practice?}
38	
39	We make three contributions:
40	\begin{enumerate}
41	\item We formalize the bias from global correction under heterogeneous misclassification and derive a closed-form bound for $K{=}2$ (tight, $R^2{=}0.92$) and a conservative sufficient condition for $K{>}2$ (\S\ref{sec:theory}).
42	\item We propose EC-HTE, a hierarchical Bayesian subgroup-stratified correction framework that eliminates this bias when subgroups are correctly specified (\S\ref{sec:method}).
43	\item Through comprehensive experiments with three LLMs on synthetic, semi-synthetic, and real data, we show that \emph{current frontier LLMs rarely trigger the conditions where stratified correction is necessary} (\S\ref{sec:experiments}). This negative result itself has practical value: it provides formal reassurance that global correction suffices in most current CSS pipelines, and it delineates when future LLM--domain combinations might require stratified approaches.
44	\end{enumerate}
45	
46	The remainder of this paper proceeds as follows. We formalize the bias mechanism and derive analytic bounds (\S\ref{sec:theory}), describe the EC-HTE framework (\S\ref{sec:method}), present experiments spanning eleven evaluation dimensions (\S\ref{sec:experiments}), and discuss implications and limitations (\S\ref{sec:discussion}).
47	
48	
49	\section{Related Work}
50	
51	\paragraph{Measurement error in causal inference.} Classical measurement error correction~\citep{carroll2006measurement,gustafson2004measurement} addresses mismeasured covariates in regression but does not characterize the specific interaction between misclassification heterogeneity and CATE heterogeneity that arises when the mismeasured variable defines the heterogeneity structure. \citet{hu2008instrumental} and \citet{schennach2016recent} develop nonparametric identification strategies under misclassification but focus on population-level functionals.
52	
53	\paragraph{LLM annotation correction.} PPI~\citep{angelopoulos2023prediction} provides valid inference by combining LLM predictions with a small labeled dataset, assuming the correction applies uniformly. DSL~\citep{egami2024using} offers design-based guarantees for text-as-treatment settings. \citet{mozer2026arm} proves arm-specific rectifiers fix ATE bias under differential prediction error but explicitly limits the analysis to average effects. PPCI~\citep{sui2026ppci} extends PPI to conditional functionals via kernel localization but addresses outcome-side, not covariate-side, measurement error.
54	
55	\paragraph{Heterogeneous treatment effects.} Causal forests~\citep{athey2019generalized,wager2018estimation} and related methods estimate CATEs via data-driven partitioning. ForestIV~\citep{bu2023treatment} handles ML-covariate measurement error in regression forests but does not address the case where the mismeasured variable is the effect modifier.
56	
57	\paragraph{Bayesian annotation models.} \citet{dawid1979maximum}, \citet{paun2018comparing}, and related work model annotator-specific confusion matrices. Our hierarchical Bayesian component builds on this tradition but applies it to causal estimation rather than consensus labeling.
58	
59	
60	\section{Bias Mechanism and Analytic Bounds}
61	\label{sec:theory}
62	
63	\subsection{Setup}
64	
65	Let $Y_i(1), Y_i(0)$ denote potential outcomes and $X_i \in \{1, \ldots, K\}$ a categorical effect modifier annotated by an LLM. The subgroup-specific CATE is $\tau_k = \mathbb{E}[Y_i(1) - Y_i(0) \mid X_i = k]$. Let $\tilde{X}_i$ denote the LLM annotation with subgroup-specific confusion matrix $\Pi^{(k)}$ where $\Pi^{(k)}_{jl} = P(\tilde{X}_i = l \mid X_i = j, \text{subgroup } k)$.
66	
67	A \emph{global} correction applies a pooled confusion matrix $\bar{\Pi} = \sum_k w_k \Pi^{(k)}$ to all subgroups. We seek to characterize the bias:
68	\begin{equation}
69	\text{Bias}_k^{\text{global}} = \hat{\tau}_k^{\text{global}} - \tau_k
70	\end{equation}
71	
72	\subsection{Binary Case ($K{=}2$)}
73	
74	For binary classification, each subgroup-specific confusion matrix has a single free parameter (off-diagonal error rate). Let $\pi_k$ denote the misclassification rate in subgroup $k$, and $\Delta\pi = \max_k \pi_k - \min_k \pi_k$ the misclassification heterogeneity. Let $\Delta\tau = \max_k \tau_k - \min_k \tau_k$ denote CATE heterogeneity.
75	
76	\begin{proposition}[Bias bound, $K{=}2$]
77	Under standard regularity conditions, the additional bias from global vs.\ stratified correction in subgroup $k$ satisfies:
78	\begin{equation}
79	|\text{Bias}_k^{\text{global}}| \leq C \cdot \Delta\pi \cdot \Delta\tau
80	\label{eq:bound}
81	\end{equation}
82	where $C$ depends on subgroup proportions and is $O(1)$.
83	\end{proposition}
84	
85	Monte Carlo verification ($n_{\text{MC}} = 1{,}000$) confirms this bound is tight: the analytic prediction achieves $R^2 = 0.92$ against empirical bias, with a bound-to-actual ratio of 1.15 (Table~\ref{tab:bound_accuracy}).
86	
87	\subsection{Multi-class Case ($K{>}2$)}
88	
89	For $K > 2$, the $K \times K$ confusion matrix has $K(K{-}1)$ off-diagonal elements, and the simple $\Delta\pi \times \Delta\tau$ product becomes a first-order approximation. Monte Carlo verification shows degrading fit: $R^2 = 0.68$ for $K{=}4$ and $R^2 = 0.52$ for $K{=}8$, with bound tightness ratios increasing to 2.3 and 3.8 respectively (Table~\ref{tab:bound_accuracy}). The bound remains valid as a \emph{conservative sufficient condition}: if $\Delta\pi \times \Delta\tau$ is below threshold, global correction is safe; but the converse is not guaranteed.
90	
91	\begin{table}[t]
92	\centering
93	\caption{Analytic bound accuracy by number of categories $K$. $n_{\text{MC}}$: Monte Carlo runs.}
94	\label{tab:bound_accuracy}
95	\begin{tabular}{@{}lccc@{}}
96	\toprule
97	$K$ & $R^2$ & Tightness ratio & $n_{\text{MC}}$ \\
98	\midrule
99	2 & 0.92 & 1.15 & 1{,}000 \\
100	4 & 0.68 & 2.30 & 1{,}000 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aeb02201-d560-435d-8acf-d91947a6176c",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "e7f25926-2c6b-4f1c-9c7c-bb21b9a09666",
  "sourceToolAssistantUUID": "aeb02201-d560-435d-8acf-d91947a6176c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T20:27:23.063Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012LeqVdEPKSVBFNV6PwrGxh`</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "file": "ROADMAP.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7f25926-2c6b-4f1c-9c7c-bb21b9a09666",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET5SRtK919jTmZMm3J7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5198a23-1149-4fac-85b4-ebace2cd1e4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VruNJC3gNd4nEyi93zFdhn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6333,
      "cache_read_input_tokens": 40490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6333,
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

_source line 29 · 2026-05-20T20:27:23.120Z_

<details><summary>↩ Tool result · `toolu_012LeqVdEPKSVBFNV6PwrGxh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/ROADMAP.md\", \"content\": \"# ec_hte_llm_annotation — Research Dashboard\\n\\n> 最后更新: 2026-05-20 19:44 UTC | 更新原因: Dream Round 1 完成，分析结果后更新\\n\\n## 核心方向\\n识别并修正 LLM 标注作为效应修饰变量时的异质性误分类偏差。全局混淆矩阵修正在亚组级 CATE 估计中产生 ∝ Δπ×Δτ 的系统性偏差；EC-HTE 通过层级贝叶斯分层修正消除该偏差。详见 paper_framing.md。\\n\\n## 当前阶段：Research（Post-MVP，Dream Round 1 完成）\\n\\n**MVP**: PASS (2026-05-20)。v3 仿真确认亚组级 EC-HTE 优势（extreme regime: bias 0.003 vs naive 0.063）。\\n\\n**Dream Round 1** (dream_20260520T185426): best=4/6 (Weak Accept), median=3.5/6 (Borderline Conference), worst=2.5/6 (Borderline Reject)。达到启动门槛。\\n\\n**关键发现**（三档一致 = 结构性问题）：\\n1. 文献过薄（11 refs → 需 30-40+）\\n2. MCMC/HB 实现细节缺失（sampler, R̂, ESS）\\n3. 方法新颖性需定位为\\\"问题发现\\\"而非\\\"新技术\\\"\\n4. 信息密度过高，需增加图表、P2 实验移入附录\\n5. K=2 理论 vs K>2 实验 gap\\n6. 真实数据验证缺失\\n\\n**观察项**（待真实实验验证）：coverage 系统性低于 nominal、diagnostic AUROC 灵敏度、PPCI 在 realistic settings 的对比。\\n\\n## 近期任务\\n- [ ] exp-001: HB 合成验证（CPU, 已派 Agent, RUNNING）\\n- [ ] exp-002: Bias bound 验证 + K>2 扩展（CPU, 已派 Agent, RUNNING）\\n- [ ] exp-004: 确认 Ashwin 数据集可及性\\n- [ ] exp-003: 半合成 benchmark（依赖 exp-001, 需 GPU）\\n- [ ] exp-007: PPCI 对比 + 组合实验（升级为 P0, 依赖 exp-001/003）\\n- [ ] 文献扩展：30-40 篇参考文献（Paper Agent 写作阶段处理）\\n- [ ] [Dream 观察] coverage 校准（exp-001 结果出来后评估）\\n- [ ] [Dream 观察] diagnostic AUROC（exp-005 结果出来后评估）\\n\\n## GPU 预算\\n- 本地 CPU：exp-001, exp-002, exp-005, exp-006, exp-007, exp-009, exp-010, exp-011\\n- GPU 需求：exp-003 (~20h), exp-004 (~10h), exp-008 (~15h)。待分配。\\n- GPU 申请已发 Manager，等待回复。\\n\\n## 实验计划\\n详见 experiment_plan.yaml。P0: exp-001, 002, 003, 004, 005, 007(新)。P1: exp-006, 008, 011。P2: exp-009, 010。\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D002 | 2026-05-20 | Dream Round 1 分析完成：best=4 (Weak Accept), median=3. | — |\\n| D001 | 2026-05-20 | MVP PASS：核心假设验证通过，评估框架修正为子群水平 | — |\\n\\n\\n\", \"total_chars\": 1675, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5198a23-1149-4fac-85b4-ebace2cd1e4e",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "9d11b8a5-6afe-4b6d-9337-0f833e98a585",
  "sourceToolAssistantUUID": "f5198a23-1149-4fac-85b4-ebace2cd1e4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T20:27:23.636Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016GfenH6Bt3HAJhpBC2sXM4`</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "file": "ideas.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d11b8a5-6afe-4b6d-9337-0f833e98a585",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET5SRtK919jTmZMm3J7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de09a952-70c5-4be5-ba80-cec9c6b623c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VruNJC3gNd4nEyi93zFdhn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6333,
      "cache_read_input_tokens": 40490,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6333
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 333,
          "cache_read_input_tokens": 40490,
          "cache_creation_input_tokens": 6333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6333,
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

_source line 31 · 2026-05-20T20:27:23.677Z_

<details><summary>↩ Tool result · `toolu_016GfenH6Bt3HAJhpBC2sXM4`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'ec_hte_llm_annotation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de09a952-70c5-4be5-ba80-cec9c6b623c9",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "1f6be874-907f-4ca0-93b8-a14da7fbae70",
  "sourceToolAssistantUUID": "de09a952-70c5-4be5-ba80-cec9c6b623c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T20:27:28.139Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K5iWvY5Cr5Myh7BYzR6tM9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/worst/paper.tex",
  "offset": 100,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f6be874-907f-4ca0-93b8-a14da7fbae70",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET62md2i4fFqfLD6bES",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0470323-3252-4686-b272-77b45e8ebafa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yfYu1NtzT79XJqzLSBNeM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4626,
      "cache_read_input_tokens": 46823,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4626,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 41,
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

_source line 33 · 2026-05-20T20:27:28.176Z_

<details><summary>↩ Tool result · `toolu_01K5iWvY5Cr5Myh7BYzR6tM9`</summary>

```text
100	4 & 0.68 & 2.30 & 1{,}000 \\
101	8 & 0.52 & 3.80 & 500 \\
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	\subsection{Bias Amplification Under Realistic Parameters}
107	
108	Table~\ref{tab:bias_amplification} reports the bias amplification factor (ratio of global-correction bias to no-correction bias) across the $(\Delta\pi, \Delta\tau)$ space. At realistic values for current LLMs ($\Delta\pi \in [0.05, 0.10]$), amplification is modest: 1.08--1.18$\times$ for $K{=}2$. Only at $\Delta\pi \geq 0.20$ does amplification become practically significant ($\geq 1.45\times$), and the ``debiasing can hurt'' regime ($\geq 3\times$) requires $\Delta\pi \geq 0.40$---a level rarely observed in current frontier LLMs.
109	
110	\begin{table}[t]
111	\centering
112	\caption{Bias amplification (global/no-correction) by misclassification heterogeneity $\Delta\pi$ and CATE heterogeneity $\Delta\tau$.}
113	\label{tab:bias_amplification}
114	\begin{tabular}{@{}cccc@{}}
115	\toprule
116	$\Delta\pi$ & $\Delta\tau$ & Amplification ($K{=}2$) & Amplification ($K{=}4$) \\
117	\midrule
118	0.05 & 0.3 & 1.08 & 1.12 \\
119	0.10 & 0.3 & 1.18 & 1.25 \\
120	0.20 & 0.3 & 1.45 & 1.62 \\
121	0.40 & 0.3 & 3.20 & 4.10 \\
122	0.05 & 0.6 & 1.15 & 1.20 \\
123	0.10 & 0.6 & 1.35 & 1.48 \\
124	0.20 & 0.6 & 2.10 & 2.55 \\
125	\bottomrule
126	\end{tabular}
127	\end{table}
128	
129	
130	\section{The EC-HTE Framework}
131	\label{sec:method}
132	
133	\subsection{Subgroup-Stratified Confusion Matrix Estimation}
134	
135	Given $n_{\text{expert}}$ expert-labeled examples, we estimate a per-subgroup confusion matrix $\hat{\Pi}^{(k)}$. Two estimators are considered:
136	
137	\paragraph{MLE stratified.} Maximum likelihood estimation of $\hat{\Pi}^{(k)}$ from the expert-labeled subset within each subgroup. Simple and fast, but high variance when per-subgroup sample sizes are small.
138	
139	\paragraph{Hierarchical Bayesian (HB).} We place a Dirichlet prior on each row of $\Pi^{(k)}$ with a shared hyperprior across subgroups:
140	\begin{align}
141	\Pi^{(k)}_j &\sim \text{Dirichlet}(\alpha_j) \\
142	\alpha_j &\sim \text{Gamma}(\mu_j, \sigma_j)
143	\end{align}
144	This induces partial pooling: subgroups with sparse data shrink toward the global estimate, while subgroups with sufficient data retain their local estimates. MCMC inference via NUTS yields posterior samples of $\Pi^{(k)}$, which propagate uncertainty through to CATE estimates.
145	
146	\subsection{Corrected CATE Estimation}
147	
148	Given estimated $\hat{\Pi}^{(k)}$, we apply the inverse confusion matrix to correct subgroup-level outcome distributions before computing CATEs. For each subgroup $k$:
149	\begin{equation}
150	\hat{p}_{\text{corrected}}^{(k)} = (\hat{\Pi}^{(k)})^{-1} \hat{p}_{\text{observed}}^{(k)}
151	\end{equation}
152	Confidence intervals incorporate both CATE sampling uncertainty and confusion-matrix estimation uncertainty via posterior predictive draws (HB) or bootstrap (MLE).
153	
154	\subsection{Diagnostic Criterion}
155	
156	We propose a diagnostic based on the $\Delta\pi \times \Delta\tau$ product from pilot data. If this product exceeds a threshold (estimated via ROC analysis on synthetic calibration data), stratified correction is recommended. We stress that this serves as a \emph{conservative sufficient condition}: exceeding the threshold warrants stratification, but falling below it does not guarantee safety, especially for $K > 2$.
157	
158	
159	\section{Experiments}
160	\label{sec:experiments}
161	
162	We organize experiments into four groups: (1) synthetic validation of the framework, (2) semi-synthetic and real-data evaluation with actual LLMs, (3) comparison with existing methods, and (4) robustness and sensitivity analyses.
163	
164	\subsection{Synthetic Validation}
165	
166	\subsubsection{HB vs.\ MLE Stratified Correction}
167	
168	We compare HB Dirichlet partial pooling against MLE stratified correction across a full regime sweep: extreme ($5\times$ heterogeneity), moderate ($2\times$), and homogeneous ($1\times$) misclassification regimes, with $n_{\text{expert}} \in \{100, 250, 500, 1000, 2000\}$ and $K \in \{2, 4\}$, over 1{,}000 Monte Carlo runs.
169	
170	\begin{table}[t]
171	\centering
172	\caption{HB vs.\ MLE stratified correction: RMSE and 95\% CI coverage by regime. RMSE differences are modest; HB provides marginal coverage improvement.}
173	\label{tab:hb_vs_mle}
174	\begin{tabular}{@{}llccccc@{}}
175	\toprule
176	Regime & $K$ & $n_{\text{expert}}$ & RMSE (HB) & RMSE (MLE) & Cov.\ (HB) & Cov.\ (MLE) \\
177	\midrule
178	Extreme  & 2 & 250  & 0.041 & 0.042 & 0.86 & 0.82 \\
179	Extreme  & 2 & 1000 & 0.022 & 0.022 & 0.91 & 0.89 \\
180	Extreme  & 4 & 250  & 0.058 & 0.055 & 0.83 & 0.80 \\
181	Moderate & 2 & 250  & 0.035 & 0.035 & 0.84 & 0.83 \\
182	Moderate & 2 & 1000 & 0.019 & 0.019 & 0.90 & 0.89 \\
183	Moderate & 4 & 250  & 0.049 & 0.048 & 0.83 & 0.79 \\
184	Homog.   & 2 & 250  & 0.030 & 0.030 & 0.88 & 0.87 \\
185	Homog.   & 4 & 250  & 0.038 & 0.037 & 0.85 & 0.84 \\
186	\bottomrule
187	\end{tabular}
188	\end{table}
189	
190	Results (Table~\ref{tab:hb_vs_mle}) show that HB and MLE stratified correction perform similarly in RMSE. HB provides modest coverage improvements (2--4 percentage points), attributable to partial pooling's variance reduction. However, for $K{=}4$ with $n_{\text{expert}}{=}250$, HB is slightly \emph{worse} in RMSE (+5.5\% for extreme, +2.1\% for moderate), because the $4 \times 4$ Dirichlet parameter space is large relative to per-cell sample sizes, making prior sensitivity more consequential.
191	
192	MCMC diagnostics are satisfactory: $\hat{R}_{\max} = 1.003$ for $K{=}2$ and $1.005$ for $K{=}4$; minimum bulk ESS $\geq 320$ (Table~\ref{tab:mcmc_diag}). Runtime is 45$\times$ that of MLE, a practical concern for large-scale applications.
193	
194	\begin{table}[t]
195	\centering
196	\caption{MCMC diagnostics for HB estimation.}
197	\label{tab:mcmc_diag}
198	\begin{tabular}{@{}lccccc@{}}
199	\toprule
200	Parameter group & $\hat{R}_{\text{med}}$ & $\hat{R}_{\max}$ & ESS (bulk, min) & ESS (tail, min) & Runtime (s) \\
201	\midrule
202	Confusion matrix ($K{=}2$) & 1.001 & 1.003 & 450 & 280 & 42 \\
203	Confusion matrix ($K{=}4$) & 1.002 & 1.005 & 320 & 210 & 185 \\
204	CATE posterior ($K{=}2$) & 1.001 & 1.002 & 520 & 310 & -- \\
205	CATE posterior ($K{=}4$) & 1.002 & 1.004 & 380 & 240 & -- \\
206	\bottomrule
207	\end{tabular}
208	\end{table}
209	
210	Coverage is systematically below nominal (83--91\% vs.\ 95\%) across all conditions, indicating that the posterior predictive intervals underestimate error propagation through the matrix inversion step. This is a structural limitation that would require bootstrap or sandwich variance corrections to address, at further computational cost.
211	
212	\subsubsection{Expert Label Budget Sensitivity}
213	
214	We sweep $n_{\text{expert}} \in \{50, 100, 250, 500, 1000, 2000\}$ across $K \in \{2, 4, 8\}$ to identify the crossover point where EC-HTE outperforms global correction in RMSE (Table~\ref{tab:budget}).
215	
216	\begin{table}[t]
217	\centering
218	\caption{Expert label budget crossover: minimum $n_{\text{expert}}$ at which EC-HTE RMSE $\leq$ global RMSE.}
219	\label{tab:budget}
220	\begin{tabular}{@{}llccc@{}}
221	\toprule
222	$K$ & Regime & Crossover $n$ & EC-HTE RMSE & Global RMSE \\
223	\midrule
224	2 & Extreme     & 350    & 0.032 & 0.032 \\
225	2 & Moderate    & 750    & 0.024 & 0.024 \\
226	2 & Homogeneous & $>$2000 & --    & --    \\
227	4 & Extreme     & 650    & 0.045 & 0.045 \\
228	4 & Moderate    & $>$2000 & --    & --    \\
229	8 & Extreme     & 1200   & 0.068 & 0.068 \\
230	8 & Moderate    & $>$2000 & --    & --    \\
231	\bottomrule
232	\end{tabular}
233	\end{table}
234	
235	The crossover points are high: $n{=}750$ for $K{=}2$ moderate, and $>2{,}000$ for all $K{\geq}4$ moderate settings. This is because EC-HTE must estimate per-subgroup $K \times K$ confusion matrices, requiring sufficient per-cell expert labels. In moderate heterogeneity regimes---which characterize current LLMs (see \S\ref{sec:semisynthetic})---global correction's bias is small enough that EC-HTE's variance cost dominates until very large expert budgets. Only the extreme regime with $K{=}2$ achieves crossover at a practical sample size ($n{=}350$).
236	
237	
238	\subsection{Semi-Synthetic and Real-Data Evaluation}
239	\label{sec:semisynthetic}
240	
241	\subsubsection{Semi-Synthetic Benchmark}
242	
243	We construct a semi-synthetic benchmark using a real tweet corpus with injected CATE structure, annotated by GPT-4.1 and Qwen3-235B. This enables measuring real misclassification heterogeneity with known ground-truth CATEs.
244	
245	\begin{table}[t]
246	\centering
247	\caption{Misclassification heterogeneity of real LLMs on semi-synthetic data.}
248	\label{tab:misclass_heterogeneity}
249	\begin{tabular}{@{}lcccc@{}}
250	\toprule
251	LLM & Overall acc. & Min subgroup acc. & Max subgroup acc. & Max/min ratio \\
252	\midrule
253	GPT-4.1     & 0.88 & 0.86 & 0.90 & 1.12 \\
254	Qwen3-235B  & 0.82 & 0.78 & 0.86 & 1.18 \\
255	\bottomrule
256	\end{tabular}
257	\end{table}
258	
259	\begin{table}[t]
260	\centering
261	\caption{Subgroup CATE bias (max and mean across subgroups) by correction method on semi-synthetic data.}
262	\label{tab:semisynthetic_bias}
263	\begin{tabular}{@{}lcccc@{}}
264	\toprule
265	Method & \multicolumn{2}{c}{GPT-4.1} & \multicolumn{2}{c}{Qwen3-235B} \\
266	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
267	 & Max bias & Mean bias & Max bias & Mean bias \\
268	\midrule
269	No correction     & 0.025 & 0.018 & 0.042 & 0.030 \\
270	Global correction & 0.015 & 0.010 & 0.028 & 0.019 \\
271	EC-HTE (MLE)      & 0.012 & 0.008 & 0.018 & 0.012 \\
272	EC-HTE (HB)       & 0.011 & 0.008 & 0.017 & 0.011 \\
273	\bottomrule
274	\end{tabular}
275	\end{table}
276	
277	Both LLMs exhibit limited misclassification heterogeneity: max/min accuracy ratios of 1.12 (GPT-4.1) and 1.18 (Qwen3-235B) (Table~\ref{tab:misclass_heterogeneity}). Global correction introduces minimal additional bias: amplification factors of 1.05 (GPT-4.1) and 1.12 (Qwen3-235B) relative to no correction. EC-HTE reduces subgroup bias by 25\% (GPT-4.1) and 40\% (Qwen3-235B) compared to global correction (Table~\ref{tab:semisynthetic_bias}), but the absolute improvements are small: the largest bias difference between global and EC-HTE is 0.011 (Qwen3-235B).
278	
279	Coverage follows the pattern from synthetic experiments: EC-HTE achieves 85--87\%, global 82--85\%, and no correction 74--78\%---all below nominal 95\%.
280	
281	\subsubsection{Ashwin et al.\ Real-Data Validation}
282	
283	We apply EC-HTE to the Rohingya refugee interview dataset of \citet{ashwin2025using}, where LLM annotation error correlates with refugee status, gender, and education level.
284	
285	\begin{table}[t]
286	\centering
287	\caption{LLM accuracy by demographic subgroup on the Ashwin et al.\ dataset.}
288	\label{tab:ashwin_accuracy}
289	\begin{tabular}{@{}lccc@{}}
290	\toprule
291	Subgroup & $n$ & LLM accuracy & SE \\
292	\midrule
293	Female refugee & 420 & 0.78 & 0.020 \\
294	Male refugee   & 380 & 0.82 & 0.020 \\
295	Female host    & 350 & 0.88 & 0.017 \\
296	Male host      & 310 & 0.90 & 0.017 \\
297	\bottomrule
298	\end{tabular}
299	\end{table}
300	
301	\begin{table}[t]
302	\centering
303	\caption{CATE estimates by correction method on Ashwin et al.\ data.}
304	\label{tab:ashwin_cate}
305	\begin{tabular}{@{}lcccc@{}}
306	\toprule
307	Subgroup & No corr. & Global & EC-HTE & Shift (Global$\to$EC-HTE) \\
308	\midrule
309	Female refugee & 0.142 & 0.158 & 0.172 & +0.014 \\
310	Male refugee   & 0.118 & 0.131 & 0.138 & +0.007 \\
311	Female host    & 0.085 & 0.094 & 0.090 & $-$0.004 \\
312	Male host      & 0.062 & 0.069 & 0.065 & $-$0.004 \\
313	\bottomrule
314	\end{tabular}
315	\end{table}
316	
317	This dataset exhibits higher misclassification heterogeneity (max/min ratio 1.22) than the semi-synthetic benchmark, driven by language complexity differences (code-switching, dialect variation) in refugee interviews. EC-HTE shifts CATE estimates by up to 0.035 relative to global correction, with the direction consistent with known error patterns: upward adjustment for high-error refugee subgroups, downward for low-error host subgroups (Table~\ref{tab:ashwin_cate}).
318	
319	However, no qualitative conclusions change: the ranking of subgroups by CATE magnitude is identical across all methods. Without ground-truth CATEs, we cannot determine whether EC-HTE's adjustments represent genuine bias reduction or overcorrection. Global-vs-no-correction bias amplification is 1.15$\times$, confirming that the practical impact of the bias mechanism remains limited even in this dataset with above-average heterogeneity.
320	
321	\subsubsection{Multi-LLM Annotator Comparison}
322	
323	We compare misclassification heterogeneity across three frontier LLMs: GPT-4.1, Qwen3-235B, and Claude Sonnet 4.6 (Table~\ref{tab:multi_llm}).
324	
325	\begin{table}[t]
326	\centering
327	\caption{Cross-LLM misclassification heterogeneity and EC-HTE benefit.}
328	\label{tab:multi_llm}
329	\begin{tabular}{@{}lcccc@{}}
330	\toprule
331	LLM & Overall acc. & Max/min ($K{=}2$) & Max/min ($K{=}4$) & EC-HTE benefit (\%) \\
332	\midrule
333	GPT-4.1          & 0.88 & 1.12 & 1.08 & 22 \\
334	Qwen3-235B       & 0.82 & 1.18 & 1.15 & 38 \\
335	Claude Sonnet 4.6 & 0.90 & 1.10 & 1.07 & 18 \\
336	\bottomrule
337	\end{tabular}
338	\end{table}
339	
340	All three LLMs show modest heterogeneity (max/min ratios 1.07--1.18). A strong negative correlation ($r = -0.85$) between overall accuracy and heterogeneity suggests that as LLMs improve, the problem diminishes further.
341	
342	One notable case: Qwen3-235B on the intersectional subgroup ``refugee $\times$ female $\times$ low education'' achieves only 71\% accuracy (vs.\ 89\% for ``host $\times$ male''), yielding a localized max/min ratio of 1.25 and bias amplification of 1.45$\times$ (Table~\ref{tab:qwen_subgroup}). This illustrates that fine-grained intersectional subgroups with linguistically challenging text can trigger meaningful heterogeneity, even when overall metrics appear benign.
343	
344	\begin{table}[t]
345	\centering
346	\caption{Qwen3-235B accuracy by fine-grained subgroup (best case for heterogeneity).}
347	\label{tab:qwen_subgroup}
348	\begin{tabular}{@{}lccc@{}}
349	\toprule
350	Subgroup & $n$ & Accuracy & SE \\
351	\midrule
352	Refugee, female, low edu  & 85  & 0.71 & 0.049 \\
353	Refugee, female, high edu & 120 & 0.80 & 0.037 \\
354	Refugee, male             & 180 & 0.83 & 0.028 \\
355	Host, female              & 165 & 0.87 & 0.026 \\
356	Host, male                & 150 & 0.89 & 0.026 \\
357	\bottomrule
358	\end{tabular}
359	\end{table}
360	
361	However, this case involves small sample sizes ($n{=}85$, SE $= 0.049$), making the heterogeneity estimate imprecise. It serves as an illustrative example of \emph{when} EC-HTE matters, rather than strong evidence that it is broadly needed.
362	
363	
364	\subsection{Comparison with Existing Methods}
365	
366	\subsubsection{EC-HTE vs.\ PPCI}
367	
368	PPCI~\citep{sui2026ppci} addresses outcome-side measurement error via kernel localization. We compare EC-HTE and PPCI under three error conditions: covariate-only, outcome-only, and both (Table~\ref{tab:ppci}).
369	
370	\begin{table}[t]
371	\centering
372	\caption{EC-HTE vs.\ PPCI: max subgroup bias and coverage under different error types.}
373	\label{tab:ppci}
374	\begin{tabular}{@{}llcccc@{}}
375	\toprule
376	Error type & Metric & PPCI & EC-HTE & Composed & No corr. \\
377	\midrule
378	Covariate-only & Max bias & 0.45 & 0.08 & -- & 1.00 \\
379	Outcome-only   & Max bias & 0.05 & 0.42 & -- & 1.00 \\
380	Both           & Max bias & 0.38 & 0.35 & 0.22 & 1.00 \\
381	\midrule
382	Covariate-only & Coverage & 0.82 & 0.87 & -- & 0.72 \\
383	Outcome-only   & Coverage & 0.91 & 0.78 & -- & 0.72 \\
384	Both           & Coverage & 0.80 & 0.83 & 0.85 & 0.68 \\
385	\bottomrule
386	\end{tabular}
387	\end{table}
388	
389	As expected, EC-HTE excels on covariate-side error (bias 0.08 vs.\ PPCI's 0.45) while PPCI excels on outcome-side error (0.05 vs.\ 0.42). When both error types are present, the methods perform similarly (0.35 vs.\ 0.38). Composing EC-HTE then PPCI yields a modest improvement (combined bias 0.22), but the gain is not additive due to over-adjustment interactions.
390	
391	An important caveat: PPCI achieves \emph{partial} effectiveness on covariate-side error (bias 0.45 vs.\ 1.0 with no correction, a 55\% reduction). This is because kernel localization in covariate space indirectly captures some covariate-side correction when covariate and outcome errors are correlated---common in LLM annotation where the same model annotates both. This partially undercuts EC-HTE's differentiation: the methods are complementary but with meaningful overlap.
392	
393	\subsubsection{Diagnostic Criterion Evaluation}
394	
395	We evaluate the $\Delta\pi \times \Delta\tau$ product as a diagnostic for predicting when global correction is harmful (Table~\ref{tab:diagnostic}).
396	
397	\begin{table}[t]
398	\centering
399	\caption{Diagnostic ROC analysis for predicting ``global correction harmful.''}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0470323-3252-4686-b272-77b45e8ebafa",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "4c30dd58-01f7-41f9-9527-b1262eec74e5",
  "sourceToolAssistantUUID": "f0470323-3252-4686-b272-77b45e8ebafa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T20:27:28.981Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01EvQRjcLDVCsT6vhN7MQVfR`</summary>

```json
{
  "pattern": "**/dream_20260520T194535/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c30dd58-01f7-41f9-9527-b1262eec74e5",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET62md2i4fFqfLD6bES",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6ea1511-153e-4c70-afa9-b7728e930bfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yfYu1NtzT79XJqzLSBNeM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4626,
      "cache_read_input_tokens": 46823,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4626
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 46823,
          "cache_creation_input_tokens": 4626,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4626,
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

_source line 35 · 2026-05-20T20:27:29.025Z_

<details><summary>↩ Tool result · `toolu_01EvQRjcLDVCsT6vhN7MQVfR`</summary>

```text
artifacts/dream_reports/dream_20260520T194535/logs/orchestrator.log
artifacts/dream_reports/dream_20260520T194535/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260520T194535/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260520T194535/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260520T194535/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260520T194535/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T194535/best/experiment_data.json
artifacts/dream_reports/dream_20260520T194535/best/paper_framing.md
artifacts/dream_reports/dream_20260520T194535/best/paper.tex
artifacts/dream_reports/dream_20260520T194535/best/paper.aux
artifacts/dream_reports/dream_20260520T194535/best/paper.out
artifacts/dream_reports/dream_20260520T194535/best/paper.pdf
artifacts/dream_reports/dream_20260520T194535/best/paper.log
artifacts/dream_reports/dream_20260520T194535/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260520T194535/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T194535/median/experiment_data.json
artifacts/dream_reports/dream_20260520T194535/median/paper_framing.md
artifacts/dream_reports/dream_20260520T194535/median/paper.tex
artifacts/dream_reports/dream_20260520T194535/median/paper.aux
artifacts/dream_reports/dream_20260520T194535/median/paper.out
artifacts/dream_reports/dream_20260520T194535/median/paper.pdf
artifacts/dream_reports/dream_20260520T194535/median/paper.log
artifacts/dream_reports/dream_20260520T194535/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260520T194535/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T194535/worst/experiment_data.json
artifacts/dream_reports/dream_20260520T194535/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T194535/worst/paper.tex
artifacts/dream_reports/dream_20260520T194535/worst/paper.aux
artifacts/dream_reports/dream_20260520T194535/worst/paper.out
artifacts/dream_reports/dream_20260520T194535/worst/paper.pdf
artifacts/dream_reports/dream_20260520T194535/worst/paper.log
artifacts/dream_reports/dream_20260520T194535/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260520T194535/best/review_context.yaml
artifacts/dream_reports/dream_20260520T194535/best/review_report.md
artifacts/dream_reports/dream_20260520T194535/logs/review_best.log
artifacts/dream_reports/dream_20260520T194535/median/review_context.yaml
artifacts/dream_reports/dream_20260520T194535/logs/review_median.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6ea1511-153e-4c70-afa9-b7728e930bfe",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "a31fa4ad-adbc-468a-ad0d-2cde7d220394",
  "sourceToolAssistantUUID": "e6ea1511-153e-4c70-afa9-b7728e930bfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-20T20:27:35.469Z_

Let me read the remaining sections of the worst paper and also the experiment data files for all three scenarios.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a31fa4ad-adbc-468a-ad0d-2cde7d220394",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET6Rohv96CVDqY3T3zE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3113f8e0-8de4-44b1-9cd4-c155318582b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwppnaqNg7GWS6LdYxhh4D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7887,
      "cache_read_input_tokens": 51449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7887,
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

_source line 37 · 2026-05-20T20:27:35.921Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KysDGEyhEae7MiF4gdKMie`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/worst/paper.tex",
  "offset": 398,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3113f8e0-8de4-44b1-9cd4-c155318582b5",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET6Rohv96CVDqY3T3zE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "649fda68-9b31-4131-a987-3114b43f2b31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwppnaqNg7GWS6LdYxhh4D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7887,
      "cache_read_input_tokens": 51449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7887,
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

_source line 38 · 2026-05-20T20:27:35.940Z_

<details><summary>↩ Tool result · `toolu_01KysDGEyhEae7MiF4gdKMie`</summary>

```text
398	\centering
399	\caption{Diagnostic ROC analysis for predicting ``global correction harmful.''}
400	\label{tab:diagnostic}
401	\begin{tabular}{@{}lcccc@{}}
402	\toprule
403	Setting & AUC & Sens.\ @FPR=0.10 & Spec.\ @TPR=0.90 & $n$ \\
404	\midrule
405	$K{=}2$ synthetic        & 0.74 & 0.58 & 0.42 & 500 \\
406	$K{=}4$ synthetic        & 0.65 & 0.45 & 0.28 & 500 \\
407	Semi-synth.\ (GPT-4.1)   & 0.71 & 0.50 & 0.33 & 100 \\
408	Semi-synth.\ (Qwen3)     & 0.73 & 0.55 & 0.38 & 100 \\
409	\midrule
410	Overall                  & 0.70 & 0.52 & 0.35 & 1{,}200 \\
411	\bottomrule
412	\end{tabular}
413	\end{table}
414	
415	The diagnostic achieves an overall AUC of 0.70---better than chance but insufficient for reliable decision-making. Two factors limit performance: (1) the base rate of ``global correction harmful'' is only 18\% across settings, making discrimination difficult; (2) for $K > 2$, the $\Delta\pi \times \Delta\tau$ product loses information about cross-subgroup misclassification interactions.
416	
417	We recommend interpreting this diagnostic as a conservative sufficient condition: practitioners should use stratified correction when the product is high, but should not rely on a low product to guarantee that global correction is safe.
418	
419	
420	\subsection{Robustness and Extensions}
421	
422	\subsubsection{Robustness to Subgroup Misspecification}
423	
424	A critical assumption of EC-HTE is correct subgroup specification. We evaluate robustness by introducing noise (random subgroup reassignment) and misalignment (correction along a different dimension than true heterogeneity) (Table~\ref{tab:robustness}).
425	
426	\begin{table}[t]
427	\centering
428	\caption{EC-HTE robustness to subgroup misspecification. EC-HTE becomes worse than global correction at $\geq$25\% noise.}
429	\label{tab:robustness}
430	\begin{tabular}{@{}lcccc@{}}
431	\toprule
432	Condition & RMSE (HB) & RMSE (MLE) & RMSE (Global) & EC-HTE vs.\ Global \\
433	\midrule
434	Correct subgroups  & 0.035 & 0.036 & 0.040 & $-$12.5\% \\
435	10\% noise         & 0.038 & 0.040 & 0.040 & $-$5.0\% \\
436	20\% noise         & 0.042 & 0.046 & 0.040 & +5.0\% \\
437	30\% noise         & 0.048 & 0.054 & 0.040 & +20.0\% \\
438	Misaligned         & 0.055 & 0.062 & 0.042 & +31.0\% \\
439	\bottomrule
440	\end{tabular}
441	\end{table}
442	
443	EC-HTE is not ``never worse than global.'' At 25\% subgroup noise, EC-HTE's RMSE exceeds global correction. With fully misaligned subgroups, EC-HTE is 31\% worse. HB partial pooling provides some protection---at 30\% noise, HB recovers 8\% relative to MLE stratified via adaptive shrinkage toward the global estimate---but this is insufficient to fully mitigate misspecification. Practitioners must validate subgroup definitions using domain knowledge and the diagnostic criterion before applying stratified correction.
444	
445	\subsubsection{Adaptive Expert Annotation Allocation}
446	
447	We evaluate CATE-weighted allocation of expert labels vs.\ uniform and uncertainty-only strategies (Table~\ref{tab:adaptive}).
448	
449	\begin{table}[t]
450	\centering
451	\caption{Adaptive allocation of expert annotation budget.}
452	\label{tab:adaptive}
453	\begin{tabular}{@{}llccc@{}}
454	\toprule
455	$n_{\text{expert}}$ & Method & RMSE & Coverage & Runtime (s) \\
456	\midrule
457	250  & Uniform         & 0.048 & 0.84 & 12 \\
458	250  & Uncertainty-only & 0.045 & 0.85 & 28 \\
459	250  & CATE-weighted    & 0.042 & 0.86 & 34 \\
460	500  & Uniform         & 0.032 & 0.87 & 12 \\
461	500  & CATE-weighted    & 0.029 & 0.88 & 35 \\
462	1000 & Uniform         & 0.021 & 0.90 & 12 \\
463	1000 & CATE-weighted    & 0.020 & 0.90 & 36 \\
464	\bottomrule
465	\end{tabular}
466	\end{table}
467	
468	CATE-weighted allocation improves RMSE by 12\% at $n_{\text{expert}} = 250$ but only 4\% at $n = 1{,}000$. The improvement over uncertainty-only allocation is small (5\% at $n = 250$), because in the moderate heterogeneity regime, CATE heterogeneity and error heterogeneity are weakly correlated. Runtime overhead is 180\%. This is a useful practical tip but not a substantial contribution.
469	
470	\subsubsection{Causal Forest Integration}
471	
472	We evaluate EC-HTE as a post-hoc correction on CausalForestDML leaf-level estimates (Table~\ref{tab:forest}).
473	
474	\begin{table}[t]
475	\centering
476	\caption{Causal forest integration results. Leaf-level EC-HTE correction underperforms global correction.}
477	\label{tab:forest}
478	\begin{tabular}{@{}lccccc@{}}
479	\toprule
480	Method & RMSE & Bias & Coverage & CI width & Conv.\ rate \\
481	\midrule
482	Naive forest              & 0.045 & 0.032 & 0.75 & 0.080 & 1.00 \\
483	Global-corrected forest   & 0.036 & 0.018 & 0.83 & 0.100 & 1.00 \\
484	EC-HTE forest (leaf)      & 0.038 & 0.012 & 0.85 & 0.135 & 0.78 \\
485	EC-HTE forest (subgroup)  & 0.037 & 0.015 & 0.84 & 0.120 & 0.95 \\
486	\bottomrule
487	\end{tabular}
488	\end{table}
489	
490	Leaf-level EC-HTE correction achieves lower bias (0.012 vs.\ 0.018) but higher RMSE (0.038 vs.\ 0.036) than global correction, because per-leaf confusion matrix estimation is noisy (typical leaf sizes of 50--200 observations). CI widths inflate by 35\%, and 22\% of Monte Carlo runs encounter numerical issues in leaf-level matrix inversion (convergence rate 0.78). Subgroup-level correction applied to forest outputs performs marginally better (RMSE 0.037) but still does not clearly outperform global correction. The forest's own adaptive partitioning partially accounts for heterogeneity, reducing the marginal value of stratified correction.
491	
492	
493	\section{Discussion and Conclusion}
494	\label{sec:discussion}
495	
496	\paragraph{Summary of findings.} We formalized the bias mechanism arising from global misclassification correction under heterogeneous LLM error rates and derived an analytic bound (tight for $K{=}2$, conservative for $K{>}2$). Our central empirical finding is that \emph{current frontier LLMs exhibit limited misclassification heterogeneity on typical CSS tasks}: max/min accuracy ratios of 1.10--1.18, bias amplification of 1.05--1.15$\times$, and no qualitative conclusion changes in our real-data application. EC-HTE provides measurable but modest improvements (18--38\% relative bias reduction) at substantial cost (expert labels, computation, sensitivity to subgroup specification).
497	
498	\paragraph{When does stratified correction matter?} Our experiments identify three conditions that jointly trigger meaningful heterogeneity: (1) weaker LLMs ($r = -0.85$ between accuracy and heterogeneity), (2) fine-grained intersectional subgroups with linguistically challenging text (e.g., Qwen3 on refugee $\times$ female $\times$ low education: accuracy 71\% vs.\ 89\% for host $\times$ male), and (3) high CATE heterogeneity. When all three conditions co-occur, bias amplification can reach 1.45$\times$ and EC-HTE's benefit becomes practically significant. We expect these conditions to arise more frequently as CSS researchers move to smaller, domain-specialized LLMs and finer-grained subgroup analyses.
499	
500	\paragraph{Practical recommendations.} For most current LLM annotation pipelines using frontier models, global correction suffices. Practitioners should (1) compute the $\Delta\pi \times \Delta\tau$ diagnostic from pilot data, (2) consider stratified correction only when the product is large or when using weaker LLMs on linguistically diverse populations, and (3) validate subgroup definitions carefully, as misspecified subgroups can make EC-HTE worse than global correction (Table~\ref{tab:robustness}).
501	
502	\paragraph{Limitations.} Coverage is systematically below nominal (83--91\% vs.\ 95\%) across all methods, reflecting insufficient uncertainty propagation through the confusion-matrix inversion. The analytic bound degrades for $K > 2$ (tightness ratio 2.3--3.8). The diagnostic criterion (AUC 0.70) is insufficient for reliable automated decision-making. The real-data evaluation lacks ground-truth CATEs, preventing definitive validation. HB estimation is 45$\times$ slower than MLE with marginal accuracy gains.
503	
504	\paragraph{Conclusion.} This paper asked when subgroup-stratified correction matters for LLM-annotated HTE. The answer, for current frontier LLMs on typical CSS tasks, is: rarely. This negative result has value---it provides formal reassurance to a growing community of CSS researchers using LLM annotations, and it delineates the boundary conditions (weak LLMs, intersectional subgroups, high CATE heterogeneity) under which the problem becomes consequential. As LLMs and CSS analyses continue to evolve, the characterization and diagnostic tools developed here offer a principled framework for deciding when to invest in stratified correction.
505	
506	
507	\bibliographystyle{plainnat}
508	
509	\begin{thebibliography}{20}
510	
511	\bibitem[Angelopoulos et~al.(2023)]{angelopoulos2023prediction}
512	A.~N. Angelopoulos, S.~Bates, C.~Fannjiang, M.~I. Jordan, and T.~Zrnic.
513	\newblock Prediction-powered inference.
514	\newblock \emph{Science}, 382(6671):669--674, 2023.
515	
516	\bibitem[Ashwin et~al.(2025)]{ashwin2025using}
517	J.~Ashwin, M.~Björkman, S.~Gaikwad, M.~Mattsson, and E.~Somanchi.
518	\newblock Using {LLM} annotations in social science research.
519	\newblock Working paper, 2025.
520	
521	\bibitem[Athey et~al.(2019)]{athey2019generalized}
522	S.~Athey, J.~Tibshirani, and S.~Wager.
523	\newblock Generalized random forests.
524	\newblock \emph{The Annals of Statistics}, 47(2):1148--1178, 2019.
525	
526	\bibitem[Bu et~al.(2023)]{bu2023treatment}
527	Z.~Bu, S.~Athey, and J.~Causal.
528	\newblock Treatment effect estimation with {ML}-covariate measurement error.
529	\newblock Working paper, 2023.
530	
531	\bibitem[Carroll et~al.(2006)]{carroll2006measurement}
532	R.~J. Carroll, D.~Ruppert, L.~A. Stefanski, and C.~M. Crainiceanu.
533	\newblock \emph{Measurement Error in Nonlinear Models}.
534	\newblock Chapman and Hall/CRC, 2nd edition, 2006.
535	
536	\bibitem[Dawid and Skene(1979)]{dawid1979maximum}
537	A.~P. Dawid and A.~M. Skene.
538	\newblock Maximum likelihood estimation of observer error-rates using the {EM} algorithm.
539	\newblock \emph{Journal of the Royal Statistical Society: Series C}, 28(1):20--28, 1979.
540	
541	\bibitem[Egami et~al.(2024)]{egami2024using}
542	N.~Egami, M.~Hinck, B.~Stewart, and H.~Wei.
543	\newblock Using imperfect surrogates for downstream inference.
544	\newblock \emph{Advances in Neural Information Processing Systems}, 2024.
545	
546	\bibitem[Gustafson(2004)]{gustafson2004measurement}
547	P.~Gustafson.
548	\newblock \emph{Measurement Error and Misclassification in Statistics and Epidemiology}.
549	\newblock Chapman and Hall/CRC, 2004.
550	
551	\bibitem[Hu and Schennach(2008)]{hu2008instrumental}
552	Y.~Hu and S.~M. Schennach.
553	\newblock Instrumental variable treatment of nonclassical measurement error models.
554	\newblock \emph{Econometrica}, 76(1):195--216, 2008.
555	
556	\bibitem[Mozer(2026)]{mozer2026arm}
557	R.~Mozer.
558	\newblock Arm-specific rectifiers for differential prediction error in treatment effect estimation.
559	\newblock Working paper, 2026.
560	
561	\bibitem[Paun et~al.(2018)]{paun2018comparing}
562	S.~Paun, B.~Carpenter, J.~Curber, D.~Hovy, and M.~Poesio.
563	\newblock Comparing {B}ayesian models of annotation.
564	\newblock \emph{Transactions of the Association for Computational Linguistics}, 6:571--585, 2018.
565	
566	\bibitem[Schennach(2016)]{schennach2016recent}
567	S.~M. Schennach.
568	\newblock Recent advances in the measurement error literature.
569	\newblock \emph{Annual Review of Economics}, 8:341--377, 2016.
570	
571	\bibitem[Sui et~al.(2026)]{sui2026ppci}
572	Y.~Sui, L.~Lei, and S.~Wager.
573	\newblock Prediction-powered conditional inference.
574	\newblock Working paper, 2026.
575	
576	\bibitem[Wager and Athey(2018)]{wager2018estimation}
577	S.~Wager and S.~Athey.
578	\newblock Estimation and inference of heterogeneous treatment effects using random forests.
579	\newblock \emph{Journal of the American Statistical Association}, 113(523):1228--1242, 2018.
580	
581	\bibitem[Ziems et~al.(2024)]{ziems2024can}
582	C.~Ziems, W.~Held, O.~Shaikh, J.~Chen, Z.~Zhang, and D.~Yang.
583	\newblock Can large language models transform computational social science?
584	\newblock \emph{Computational Linguistics}, 50(1):237--291, 2024.
585	
586	\end{thebibliography}
587	
588	\end{document}
589	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "649fda68-9b31-4131-a987-3114b43f2b31",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "62eac9a6-f574-496d-b862-31572b8a64ba",
  "sourceToolAssistantUUID": "649fda68-9b31-4131-a987-3114b43f2b31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T20:27:36.281Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GdrHSkgb1jPcnrNwXxm1fF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/imagined_experiments.yaml",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62eac9a6-f574-496d-b862-31572b8a64ba",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET6Rohv96CVDqY3T3zE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a872fdd0-48b4-4092-a2e4-aadbd4a0e74c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwppnaqNg7GWS6LdYxhh4D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7887,
      "cache_read_input_tokens": 51449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7887,
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

_source line 40 · 2026-05-20T20:27:36.304Z_

<details><summary>↩ Tool result · `toolu_01GdrHSkgb1jPcnrNwXxm1fF`</summary>

```text
1	tier: best
2	narrative_guidance: '原始 framing 完全成立。论文以 problem-discovery 定位：首次识别并形式化 measurement-error
3	  × causal-heterogeneity confounding，Δπ×Δτ product 诊断准则有独立实用价值。Headline result 可直接使用（"global
4	  correction worsens bias by up to 7.8x"）。PPCI 正交性干净，K>2 扩展自然，HB partial pooling 在小样本下优势显著。
5	  论文结构 Theory → Synthetic → Semi-synthetic → Real data 全链条闭合，无需防守性让步。
6	
7	  '
8	imagined_experiments:
9	- name: Hierarchical Bayesian EC-HTE synthetic validation
10	  plan_id: exp-001
11	  description: '在合成数据上实现 HB Dirichlet-prior confusion matrix estimator，与 MLE stratified
12	    和 Laplace smoothed 基线对比。覆盖 extreme/moderate/homogeneous error regimes × n_expert
13	    ∈ {100,250,500,1000,2000} × K ∈ {2,4} subgroups，共 1000 次 MC 重复。PyMC NUTS sampler，4
14	    chains，warmup=1000。
15	
16	    '
17	  expected_results:
18	    hb_rmse_vs_mle_at_n100_k2: 0.72
19	    hb_rmse_vs_mle_at_n250_k2: 0.74
20	    hb_rmse_vs_mle_at_n250_k4: 0.68
21	    hb_rmse_vs_mle_at_n1000_k2: 0.91
22	    hb_rmse_vs_mle_at_n2000_k2: 0.96
23	    hb_coverage_95ci_extreme_n250: 0.943
24	    hb_coverage_95ci_moderate_n250: 0.951
25	    hb_coverage_95ci_homogeneous_n250: 0.954
26	    mle_coverage_95ci_extreme_n250: 0.87
27	    laplace_coverage_95ci_extreme_n250: 0.91
28	    ec_hte_subgroup_bias_extreme: 0.003
29	    global_correction_subgroup_bias_extreme: 0.041
30	    rhat_max: 1.004
31	    ess_min: 387
32	    mcmc_runtime_per_fit_seconds: 2.3
33	    mle_runtime_per_fit_seconds: 0.008
34	    mc_runs: 1000
35	  result_rationale: 'HB Dirichlet partial pooling 在小样本下的优势来自两个机制：(1) 当 n_expert ≤
36	    250 时，per-subgroup confusion matrix 的 MLE 估计面临严重的有限样本方差——K=4 时每个 subgroup 仅 ~62
37	    个标注，2×2 矩阵 4 个参数的 MLE 方差很大，矩阵求逆进一步放大误差；HB 通过向全局先验收缩，借用跨 subgroup 信息， 有效降低估计方差。(2)
38	    Coverage 改善因为 HB 的后验区间自然包含参数不确定性，而 MLE 的 delta-method CI 在小样本下低估方差。随着 n_expert
39	    → 2000，每个 subgroup 有充足数据，MLE 渐近最优性使 HB 优势消失。 Extreme regime 下 HB 优势最大，因为 subgroup
40	    间 error rate 差异大（π₁=0.15 vs π₂=0.35）， MLE 在低频 subgroup 上方差爆炸。MCMC 收敛良好因为 Dirichlet-Multinomial
41	    是共轭结构， posterior geometry 简单，NUTS 无困难。Runtime 比 MLE 慢 ~300x 但绝对值仍可接受。
42	
43	    '
44	  tables:
45	  - title: 'Table 1: RMSE comparison across methods, regimes, and sample sizes (K=2)'
46	    columns:
47	    - regime
48	    - n_expert
49	    - MLE_RMSE
50	    - Laplace_RMSE
51	    - HB_RMSE
52	    - HB/MLE_ratio
53	    - HB_95CI_coverage
54	    rows:
55	    - - extreme
56	      - 100
57	      - 0.058
58	      - 0.049
59	      - 0.042
60	      - 0.72
61	      - 0.932
62	    - - extreme
63	      - 250
64	      - 0.037
65	      - 0.032
66	      - 0.027
67	      - 0.74
68	      - 0.943
69	    - - extreme
70	      - 500
71	      - 0.024
72	      - 0.022
73	      - 0.02
74	      - 0.83
75	      - 0.948
76	    - - extreme
77	      - 1000
78	      - 0.016
79	      - 0.015
80	      - 0.015
81	      - 0.91
82	      - 0.952
83	    - - extreme
84	      - 2000
85	      - 0.011
86	      - 0.011
87	      - 0.011
88	      - 0.96
89	      - 0.953
90	    - - moderate
91	      - 100
92	      - 0.041
93	      - 0.036
94	      - 0.031
95	      - 0.76
96	      - 0.938
97	    - - moderate
98	      - 250
99	      - 0.027
100	      - 0.024
101	      - 0.021
102	      - 0.78
103	      - 0.951
104	    - - moderate
105	      - 500
106	      - 0.018
107	      - 0.017
108	      - 0.016
109	      - 0.87
110	      - 0.953
111	    - - moderate
112	      - 1000
113	      - 0.012
114	      - 0.012
115	      - 0.011
116	      - 0.93
117	      - 0.954
118	    - - moderate
119	      - 2000
120	      - 0.009
121	      - 0.009
122	      - 0.008
123	      - 0.97
124	      - 0.953
125	    - - homogeneous
126	      - 100
127	      - 0.032
128	      - 0.029
129	      - 0.027
130	      - 0.84
131	      - 0.944
132	    - - homogeneous
133	      - 250
134	      - 0.021
135	      - 0.02
136	      - 0.019
137	      - 0.88
138	      - 0.954
139	    - - homogeneous
140	      - 500
141	      - 0.015
142	      - 0.014
143	      - 0.014
144	      - 0.93
145	      - 0.955
146	    - - homogeneous
147	      - 1000
148	      - 0.01
149	      - 0.01
150	      - 0.01
151	      - 0.97
152	      - 0.954
153	    - - homogeneous
154	      - 2000
155	      - 0.007
156	      - 0.007
157	      - 0.007
158	      - 0.99
159	      - 0.953
160	  - title: 'Table 2: K=4 subgroups results (extreme regime)'
161	    columns:
162	    - n_expert
163	    - MLE_RMSE
164	    - HB_RMSE
165	    - HB/MLE_ratio
166	    - HB_coverage
167	    - MLE_coverage
168	    rows:
169	    - - 100
170	      - 0.089
171	      - 0.058
172	      - 0.65
173	      - 0.921
174	      - 0.82
175	    - - 250
176	      - 0.054
177	      - 0.037
178	      - 0.68
179	      - 0.94
180	      - 0.86
181	    - - 500
182	      - 0.035
183	      - 0.027
184	      - 0.77
185	      - 0.949
186	      - 0.91
187	    - - 1000
188	      - 0.023
189	      - 0.02
190	      - 0.87
191	      - 0.953
192	      - 0.94
193	    - - 2000
194	      - 0.016
195	      - 0.015
196	      - 0.94
197	      - 0.954
198	      - 0.95
199	  - title: 'Table 3: MCMC diagnostics summary'
200	    columns:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a872fdd0-48b4-4092-a2e4-aadbd4a0e74c",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "5ce72640-a44e-4632-9921-8041ce82db3e",
  "sourceToolAssistantUUID": "a872fdd0-48b4-4092-a2e4-aadbd4a0e74c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-20T20:27:39.857Z_

Now let me also read the review report that was already generated for the best paper, and the paper_framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ce72640-a44e-4632-9921-8041ce82db3e",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET6zjrpSicdYXJ1n5v1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90acb208-a19b-4570-ade0-229acf93ed8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMJSQfdQWFT3hpBXxVTASH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7394,
      "cache_read_input_tokens": 59336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7394,
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

_source line 42 · 2026-05-20T20:27:42.236Z_

<details open><summary>🔧 Tool call — Read · `toolu_015Dajgm7vSGznNCCepZCtxU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/review_report.md",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90acb208-a19b-4570-ade0-229acf93ed8e",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET6zjrpSicdYXJ1n5v1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2b4a4d3e-7c2e-48f2-8b2a-93dd7b61f86e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMJSQfdQWFT3hpBXxVTASH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7394,
      "cache_read_input_tokens": 59336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7394,
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

_source line 43 · 2026-05-20T20:27:42.262Z_

<details><summary>↩ Tool result · `toolu_015Dajgm7vSGznNCCepZCtxU`</summary>

```text
1	---
2	dream_id: dream_20260520T194535
3	tier: best
4	overall_score: 4/6 Weak Accept
5	timestamp: 2026-05-20T20:24:43.040742+00:00
6	---
7	
8	# Dream Review Report: "When Debiasing Backfires: Measurement-Error Heterogeneity in LLM-Annotated Causal Effect Estimation"
9	
10	**Review Mode**: Full (2 Reviewers, 4-step roundtable)  
11	**Date**: 2026-05-20  
12	**Venue Standard**: Top ML venue, ~25% acceptance rate, 6-point scale
13	
14	---
15	
16	## Step 1: Independent Reviews
17	
18	### Reviewer 1 (R1) — Methods & Experiments
19	
20	**Score: 4 / 6 (Weak Accept)**
21	
22	#### Summary
23	The paper identifies a genuine failure mode where global confusion-matrix correction amplifies subgroup CATE bias, proposes EC-HTE (hierarchical Bayesian stratified correction), and validates across synthetic, semi-synthetic, and real-data experiments. The experimental coverage is comprehensive (11 experiments spanning theory verification, method validation, benchmarking, robustness, and integration).
24	
25	#### Strengths
26	- **S1. Clean problem identification with practical impact.** The Δπ×Δτ product characterization is intuitive, verifiable (R²=0.982), and immediately actionable. The 7.8× amplification headline is striking.
27	- **S2. Comprehensive 11-experiment pipeline.** Theory→Synthetic→Semi-synthetic→Real data chain is fully closed. Budget sensitivity, robustness, multi-LLM, and causal forest integration all included.
28	- **S3. Well-motivated HB estimation.** Dirichlet partial pooling is a principled choice for small-sample confusion matrix estimation. MCMC diagnostics (R̂≤1.004, ESS≥387, zero divergences) are solid.
29	- **S4. Convincing PPCI orthogonality.** Section 5.5 demonstrates that PPCI worsens covariate-side error (bias 0.089 vs 0.021 uncorrected) while EC-HTE worsens outcome-side error, and their composition achieves the best result (bias 0.006). Near-zero correction-term correlation (r=0.04) is clean evidence.
30	- **S5. Honest failure mode reporting.** K=8/n=50 failure, computational overhead, a priori subgroup requirement all acknowledged.
31	
32	#### Weaknesses
33	
34	**Major:**
35	
36	1. **Theorem 1 is an identity, not a bound.** The bias decomposition bias(τ̂_k^global) = Σ_j w_j(π̄−π_j)τ_j is exact at the population level. Calling it a "bias bound" and reporting R²<1.0 as "bound verification" is misleading — the gap is sampling noise from finite MC, not bound looseness. The framing should be corrected to "bias decomposition verification."
37	
38	2. **Semi-synthetic DGP is underspecified.** Section 5.3 describes N=20,000 tweets with "injected CATE heterogeneity structure" but provides no details on: (a) how outcomes are generated, (b) how treatment is assigned, (c) how true CATEs (τ₁=0.15, τ₂=0.04) are injected into the text-based pipeline. Without this, results are not reproducible.
39	
40	3. **Real-data ground truth is opaque.** Table 11 reports bias and RMSE for Ashwin et al. data, implying known true CATEs. But the paper never explains how ground truth CATEs are established in observational refugee interview data. If these are estimated from expert labels alone, they carry their own uncertainty; if from a separate RCT component, this should be stated.
41	
42	4. **Diagnostic AUC (0.953) evaluated on own experiments.** The 342 settings are drawn from the paper's own synthetic/semi-synthetic/real experiments — not a held-out evaluation. The AUC is an in-sample metric. Cross-validation or a separate evaluation set would strengthen this claim.
43	
44	**Minor:**
45	
46	5. Table numbering jumps inconsistently (Tables 1-2 in §3, Tables 3-5 in §5.1, Tables 6-7 in §5.2, etc.) — confusing for readers.
47	6. 1000 MC replications are adequate but the paper should report SE of the reported RMSE values, not just point estimates.
48	7. The K>2 extension (Remark 1) remains informal — it would benefit from a brief proof sketch.
49	8. No discussion of computational scaling: how does MCMC time grow with K and n?
50	9. Gamma hyperprior values (μ_j, σ_j) for the Dirichlet concentration parameters are not specified, nor is sensitivity analysis provided.
51	
52	#### Questions for Authors
53	1. How are true CATEs established in the Ashwin et al. real-data experiment (Table 11)?
54	2. In the semi-synthetic setup, how exactly are outcomes generated and CATEs injected? Is treatment assignment random or observational?
55	3. The semi-synthetic benchmark uses n=500 expert labels, but the abstract and Appendix A claim EC-HTE works with "as few as 250." Are there results at n=250 for the semi-synthetic setting?
56	4. What are the Gamma hyperprior values (μ_j, σ_j) for the Dirichlet concentration, and how sensitive are results to these choices?
57	5. How does the K>2 bias decomposition (sum-of-products) relate to bias for a *specific* subgroup k, versus the aggregated expression?
58	
59	#### Scores (R1)
60	| Dimension | Score |
61	|-----------|-------|
62	| Soundness | 3 / 4 |
63	| Contribution | 3 / 4 |
64	| Presentation | 2.5 / 4 |
65	| Overall | 4 / 6 |
66	| Confidence | 4 / 5 |
67	
68	---
69	
70	### Reviewer 2 (R2) — Novelty & Related Work
71	
72	**Score: 4 / 6 (Weak Accept)**
73	
74	#### Summary
75	The paper identifies a previously unformalized failure mode at the intersection of LLM annotation and HTE estimation, proposes a principled Bayesian correction framework, and validates comprehensively. The problem identification is the primary contribution; the method is competent but not deeply novel. The paper is well-written but suffers from a critically thin bibliography (9 references) that undermines its positioning.
76	
77	#### Strengths
78	- **S1. Novel and well-scoped problem identification.** The specific failure mode — that error correction *amplifies* bias when the mismeasured variable defines the heterogeneity structure — has not been formalized before in the CATE context. Neither PPI, DSL, Mozer, nor PPCI addresses this case.
79	- **S2. PPCI orthogonality is undersold.** The composition result (bias 0.006 with both corrections) is a positive contribution that goes beyond defensive positioning. This deserves elevation in the abstract and contributions list.
80	- **S3. Diagnostic criterion has standalone value.** AUC=0.953 with stable threshold (0.008) across data sources gives practitioners a zero-implementation-cost decision tool.
81	- **S4. Real-data validation closes the key external validity gap.** The 6.7× amplification on education subgroups, producing a misleading negative CATE for the low-education group, is compelling and policy-relevant.
82	
83	#### Weaknesses
84	
85	**Major:**
86	
87	1. **Bibliography critically thin (9 references).** For a paper bridging 5 literatures (measurement error, Bayesian estimation, causal inference, LLM annotation, CSS), 9 references is far below the 25-35 expected. Critical omissions:
88	   - **Classical measurement error**: Fuller (1987), Gustafson (2003), Hu & Schennach (2008). The qualitative insight "misspecified correction can amplify MSE" exists since Fuller 1987. Without engaging this, the novelty claim is vulnerable.
89	   - **LLM-as-annotator CSS**: Tornberg (2024), Gilardi et al. (2023), Pangakis et al. (2023), Ziems et al. (2024) — zero cited, yet these document the heterogeneous error patterns motivating EC-HTE.
90	   - **HTE methods**: Wager & Athey (2018) for causal forests (used but not cited!), Kennedy (2023), Kunzel et al. (2019), Chernozhukov et al. (2018) for DML.
91	   - **Bayesian annotator models**: Passonneau & Carpenter (2014), Hovy et al. (2013), Rodrigues & Pereira (2018).
92	   - **PPI extensions**: PPI++, Zrnic & Candes (2024).
93	   - **Missing baselines**: SIMEX (Cook & Stefanski 1994), multiple imputation for misclassified variables (Blackwell et al. 2017).
94	
95	2. **Novelty positioning needs sharpening against classical measurement error theory.** The Δπ×Δτ product form is new in the CATE context, but the qualitative insight is known. The paper should explicitly state: "It has long been known that misspecified corrections can amplify MSE (Fuller 1987). Our contribution is (a) the specific quantitative characterization for CATE estimation, (b) demonstrating this occurs by default in LLM-annotation workflows, and (c) providing a computable diagnostic and correction framework."
96	
97	3. **Ashwin et al. (2025) reference appears problematic.** Bibliography entry has "Ashwin, Maaz et al." but the actual paper is by "Ashwin, Aditya et al." with a different title. Needs verification.
98	
99	**Moderate:**
100	
101	4. **Missing natural baselines.** SIMEX and multiple imputation for misclassified variables are standard measurement error approaches not compared against.
102	5. **DSL distinction insufficiently crisp.** Egami et al. (2024) DSL is a direct competitor — the key distinction (DSL targets ATE with global correction; EC-HTE targets subgroup CATEs requiring stratified correction) needs a single prominent sentence.
103	6. **Confusion matrix invertibility assumption unstated.** Equation (3) requires det(Ĉ_k)≠0; this should be explicit.
104	7. **"Never worse than global" claim contradicted by own K=8/n=50 results.** Needs qualification in main text, not just appendix.
105	
106	**Minor:**
107	
108	8. Semi-synthetic ground truth CATEs are by construction aligned with binary subgroup structure — may overstate advantage.
109	9. No figures in main text — 13 tables in 8 pages reads more as technical report than conference paper. Mechanism schematic and amplification heatmap should be figures.
110	
111	#### Questions for Authors
112	1. How does Theorem 1 relate to Fuller (1987, Sec. 2.3) on misspecified measurement error corrections amplifying MSE? What specifically is new beyond the CATE-with-effect-modifier application?
113	2. Have you considered framing subgroups as "annotators" in the Dawid-Skene sense? Would existing Bayesian annotator model software directly apply?
114	3. Have you experimented with SIMEX or multiple imputation as baselines?
115	4. Can you reconcile the "never worse than global guarantee" (§1, contribution #2) with the K=8/n=50 counterexample (Appendix A)?
116	5. Can you verify the Ashwin et al. citation (author names and title)?
117	
118	#### Novelty Calibration
119	- **Δπ×Δτ characterization**: Moderately novel. Qualitative insight known in stats; quantitative product form new for CATE.
120	- **EC-HTE framework**: Incremental. HB Dirichlet for confusion matrices is established; application to CATE correction is sensible engineering.
121	- **Diagnostic criterion**: Useful practical contribution (minor but clean).
122	- **Overall**: Novelty is borderline for a top venue. Strength is problem identification + comprehensive validation, not technical depth. Appropriate for CSS-oriented tracks if bibliography adequately contextualizes.
123	
124	#### Scores (R2)
125	| Dimension | Score |
126	|-----------|-------|
127	| Soundness | 3 / 4 |
128	| Contribution | 3 / 4 |
129	| Presentation | 2.5 / 4 |
130	| Overall | 4 / 6 |
131	| Confidence | 4 / 5 |
132	
133	---
134	
135	## Step 2: Cross-Sharing
136	
137	After exchanging reviews, both reviewers note:
138	
139	**R1 → R2**: "R2's bibliography analysis is extremely valuable and I endorse it fully. I had not considered the Fuller (1987) precedent — this does somewhat weaken the novelty of the 'debiasing can backfire' headline. However, the specific CATE product form and the LLM-workflow relevance are genuinely new. I also agree the PPCI composition result is undersold."
140	
141	**R2 → R1**: "R1's point about Theorem 1 being an identity rather than a bound is precisely correct and I should have flagged it. The 'bias bound verification' framing is misleading. R1's concern about real-data ground truth is critical — I took the Ashwin et al. results at face value but the ground truth mechanism is indeed opaque. The semi-synthetic DGP underspecification is also a valid reproducibility concern."
142	
143	**Points of agreement:**
144	- Both give 4/6 (Weak Accept)
145	- Both flag PPCI orthogonality as a strong contribution that could be elevated
146	- Both concerned about bibliography thinness
147	- Both value the honest limitations disclosure
148	- Both note presentation could be improved (tables vs figures)
149	
150	**Points of divergence:**
151	- R1 emphasizes experimental methodology gaps (DGP specification, ground truth opacity)
152	- R2 emphasizes positioning and bibliographic gaps
153	- These are complementary, not conflicting
154	
155	---
156	
157	## Step 3: Convergence
158	
159	After discussion, reviewers converge on the following assessment:
160	
161	### Consensus Score: 4 / 6 (Weak Accept)
162	
163	Both reviewers independently arrived at 4/6 and see no reason to change after cross-sharing. The paper is above the acceptance threshold on problem identification, experimental coverage, and practical value, but below on bibliography depth, novelty contextualization, and certain methodological details.
164	
165	### Consensus on Key Issues
166	
167	**Accept-worthy contributions (agreed):**
168	1. The Δπ×Δτ bias characterization is genuinely new in the CATE context, even if the qualitative insight has precedent in classical measurement error theory
169	2. The PPCI orthogonality + composition demonstration is clean and constructive
170	3. The real-data validation (Ashwin et al., education subgroups) provides compelling external validity
171	4. The diagnostic criterion (AUC=0.953) has standalone practical value
172	5. The experiment pipeline (Theory→Synthetic→Semi-synthetic→Real) is exemplary
173	
174	**Required revisions for acceptance (agreed):**
175	1. **[Critical]** Expand bibliography to 25-35 references covering all five bridged literatures
176	2. **[Critical]** Explicitly contextualize against classical measurement error (Fuller 1987, Carroll Ch. 4)
177	3. **[Critical]** Clarify real-data ground truth mechanism — how are true CATEs established?
178	4. **[High]** Correct "bias bound" framing to "bias decomposition" — Theorem 1 is an identity
179	5. **[High]** Specify semi-synthetic DGP (outcome generation, treatment assignment, CATE injection)
180	6. **[High]** Qualify "never worse than global" in main text given K=8/n=50 counterexample
181	7. **[Medium]** Add 2-3 figures to main text (mechanism schematic, amplification heatmap, ROC curve)
182	8. **[Medium]** Specify Gamma hyperprior values and report sensitivity
183	9. **[Medium]** Evaluate diagnostic AUC on held-out settings or via cross-validation
184	10. **[Low]** Fix Ashwin et al. bibliography entry; verify author names and title
185	
186	---
187	
188	## Step 4: Synthesized Assessment
189	
190	### Overall Score: 4 / 6 (Weak Accept)
191	
192	### Paper Summary
193	This paper identifies and formalizes a previously unrecognized bias mechanism in LLM-annotated causal effect estimation: when a pooled confusion matrix is used to correct subgroup-level CATEs, the resulting bias is proportional to Δπ×Δτ (the product of misclassification heterogeneity and CATE heterogeneity), and this "debiasing" can amplify bias by up to 7.8×. The proposed EC-HTE framework uses hierarchical Bayesian Dirichlet partial pooling to estimate subgroup-stratified confusion matrices, achieving 89-92% bias reduction on semi-synthetic political-science benchmarks with GPT-4.1 and Qwen3-235B annotations. A diagnostic criterion (AUC=0.953) predicts when global correction is harmful. Real-data validation on Rohingya refugee interviews confirms global correction amplifies bias up to 6.7× on education subgroups.
194	
195	### Meta-Strengths
196	1. **Problem identification is the paper's core value proposition and it delivers.** The "debiasing can backfire" insight is immediately actionable for the growing community of CSS researchers using LLM annotations. The constructive example — global correction producing a negative CATE estimate for a low-education group when the true effect is positive — has genuine policy implications.
197	
198	2. **Experimental comprehensiveness is exceptional.** All 11 planned experiments are executed, covering theory verification (§5.1), method validation (§5.2), semi-synthetic benchmarking (§5.3), real-data validation (§5.4), competitor comparison (§5.5), and downstream integration (§5.6), plus 4 appendix extensions (budget sensitivity, multi-LLM, robustness, adaptive allocation). This is among the most thorough experimental pipelines we have seen for a methods paper of this scope.
199	
200	3. **PPCI orthogonality demonstration elevates the paper beyond problem identification.** The composition result (EC-HTE for covariate-side + PPCI for outcome-side = bias 0.006, 84% reduction) is a constructive contribution that opens a research direction on modular error-correction pipelines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b4a4d3e-7c2e-48f2-8b2a-93dd7b61f86e",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "9850cc27-b2a5-438c-a796-533af6967235",
  "sourceToolAssistantUUID": "2b4a4d3e-7c2e-48f2-8b2a-93dd7b61f86e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T20:27:43.049Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JSdNr6qTXEeXNiu6CrwnFi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260520T194535/best/paper_framing.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9850cc27-b2a5-438c-a796-533af6967235",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET6zjrpSicdYXJ1n5v1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e451d0ce-3bc5-424f-94f3-ef5e702fdf69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMJSQfdQWFT3hpBXxVTASH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7394,
      "cache_read_input_tokens": 59336,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7394
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 252,
          "cache_read_input_tokens": 59336,
          "cache_creation_input_tokens": 7394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7394,
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

_source line 45 · 2026-05-20T20:27:43.064Z_

<details><summary>↩ Tool result · `toolu_01JSdNr6qTXEeXNiu6CrwnFi`</summary>

```text
1	# Paper Framing — ec_hte_llm_annotation
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (via ARR)
5	- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026
6	- Format: Long paper, 8 pages + unlimited references
7	
8	## Core Claims (3 条，可证伪)
9	
10	1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this "debiasing" can worsen CATE bias by 5-10x compared to no correction at all.
11	
12	2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) eliminates this bias while controlling estimation variance through partial pooling. MVP demonstrates near-zero subgroup-level bias with simple stratification; HB partial pooling (exp-001) expected to further reduce RMSE by controlling matrix-inversion variance. Applicable to any CATE estimator; demonstrated with difference-in-means and CausalForestDML.
13	
14	3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic: when this product exceeds a threshold, global correction is harmful and stratified correction is needed. This criterion has standalone value independent of EC-HTE.
15	
16	## Story Spine
17	
18	- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis (e.g., "tweet contains economic framing" moderates campaign effectiveness). LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.
19	
20	- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**
21	
22	- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration. **Novelty positioning**: The individual components (HB Dirichlet estimation, confusion matrix correction, causal forests) are established; the contribution is (a) identifying and formalizing the bias mechanism specific to effect-modifier misclassification, (b) the Δπ×Δτ product characterization that predicts when correction backfires, and (c) bridging the measurement error and HTE literatures in a practically consequential way. Frame as "problem identification + principled solution" not "new estimation technique."
23	
24	- **Headline result template**: "On semi-synthetic political-science benchmarks, global correction worsens subgroup CATE bias by up to 7.8x in low-error subgroups; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels."
25	
26	## Key Contributions (ordered for paper)
27	
28	1. **Bias mechanism identification + formal bound**: bias ∝ misclassification heterogeneity × CATE heterogeneity. Includes "debiasing can hurt" proposition with constructive example. (Theory + Empirical)
29	2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)
30	3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)
31	4. **Comprehensive validation**: Synthetic + semi-synthetic + real-data experiments with multiple LLMs. (Empirical)
32	
33	## Anticipated Reviewer Concerns
34	
35	1. **"Why not just use expert labels directly for CATE?"** — Defense: 2000 expert labels / k subgroups / honest forest halving → insufficient power per cell. EC-HTE uses all LLM data for low-variance CATE, expert labels only for calibration. Explicitly quantify in experiments.
36	
37	2. **"How is this different from PPCI (Sui et al., 2026)?"** — PPCI corrects outcome-side measurement error for conditional functionals via kernel localization. We correct covariate-side measurement error in the variable that defines the conditioning structure. Orthogonal problems.
38	
39	3. **"Incremental over Mozer (2026)"** — Mozer addresses ATE under differential prediction error. We address CATE under heterogeneous effect-modifier misclassification — a structurally different problem. The bias mechanism we identify (pooled correction hurting low-error subgroups) has no counterpart in Mozer's framework.
40	
41	4. **"How sensitive to subgroup definition?"** — Hierarchical Bayesian partial pooling makes the method robust: with well-defined subgroups, full stratification; with noisy subgroups, automatic shrinkage toward global. Include robustness analysis.
42	
43	5. **"Real-world expert label cost"** — Address with expert budget sensitivity sweep (n=100 to 2000) and adaptive allocation (Stage 3).
44	
45	6. **"How does this differ from Carroll et al. (2006) / classical measurement error?"** — Carroll et al. addresses measurement error in regression covariates; our contribution is the specific bias characterization for CATE estimation when the mismeasured variable *defines* the heterogeneity structure. The Δπ×Δτ product form is a new result in this context. Engage deeply with measurement error literature (Carroll, Gustafson, Hu & Schennach) and Bayesian annotation models (Dawid & Skene, Paun et al.) to contextualize precisely.
46	
47	7. **"Methodological novelty is modest"** — Acknowledge explicitly. Position contribution as problem discovery + formal characterization + comprehensive validation, not as a new estimation technique. The "never worse than global" guarantee via HB partial pooling is the key methodological property.
48	
49	8. **"Why no figures?"** — Paper MUST include key figures: (1) schematic of bias mechanism (global over/under-correction), (2) bias amplification heatmap (Δπ vs Δτ), (3) diagnostic ROC curve, (4) budget crossover curves. Move P2 experiments (exp-008, exp-009) to appendix to free space.
50	
51	## Venue Fit
52	
53	EMNLP fit is strong: core NLP application (LLM annotation quality), computational social science use case (political messaging, refugee interviews), direct comparison with NeurIPS/EMNLP published methods (DSL, PPI, benchmarking). Methodology is causal inference but framed through NLP lens. Potential reviewer pool: CL+CSS track.
54	
55	Risk: pure statistics reviewers may want stronger theoretical contribution (convergence rates, minimax bounds). Mitigation: emphasize the practical diagnostic criterion and empirical validation breadth.
56	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e451d0ce-3bc5-424f-94f3-ef5e702fdf69",
  "isSidechain": true,
  "promptId": "79a83734-c815-44a7-9a50-60c025d8511b",
  "agentId": "a4fde7b158b599326",
  "type": "user",
  "uuid": "06054c3e-f7e1-430e-9a69-9c008903a7a4",
  "sourceToolAssistantUUID": "e451d0ce-3bc5-424f-94f3-ef5e702fdf69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-20T20:29:00.720Z_

I now have a thorough understanding of all three paper variants (best, median, worst) and the project context. Let me now produce the R1 review focused on Methods and Experiments, synthesizing my analysis across all materials.

## R1: Methods & Experiments

### Summary
The paper formalizes a bias mechanism in LLM-annotated HTE analysis where global confusion-matrix correction amplifies subgroup CATE bias proportionally to the product of misclassification heterogeneity and CATE heterogeneity. EC-HTE addresses this via hierarchical Bayesian Dirichlet partial pooling for subgroup-stratified confusion matrices. Eleven experiments span synthetic, semi-synthetic (political tweets with GPT-4.1/Qwen3-235B), and real data (Rohingya refugee interviews), covering theory verification, method validation, competitor comparison, robustness, and downstream integration with causal forests.

### Strengths

- **S1. Bias decomposition is analytically correct and well-verified.** The identity bias(tau_k^global) = sum_j w_j(pi_bar - pi_j)tau_j is algebraically exact for the K=2 case. Empirical verification with R^2 = 0.89-0.98 (depending on the paper variant) across a systematic parameter grid with 1000 MC replications per point is thorough. The gap between analytic prediction and MC estimate is appropriately small (ratio 1.01-1.05), consistent with finite-sample noise rather than bound looseness.

- **S2. Comprehensive experimental pipeline covering all 11 planned experiments.** The Theory -> Synthetic -> Semi-synthetic -> Real data chain is fully closed. Budget sensitivity (exp-006), robustness to misspecification (exp-010), PPCI comparison (exp-007), multi-LLM (exp-008), adaptive allocation (exp-009), and CausalForestDML integration (exp-011) are all addressed. This is unusually thorough for a methods paper.

- **S3. MCMC diagnostics are adequately reported.** R-hat <= 1.004, bulk ESS >= 387, tail ESS >= 302, zero divergences across 1000 MC replications. These meet standard thresholds (R-hat < 1.01, ESS > 200). The diagnostics table (Table in Section 4) is well-structured.

- **S4. PPCI orthogonality demonstration is convincing and constructive.** The disaggregation by error type (covariate-only, outcome-only, both) with the composition result (bias 0.006 in best variant, 0.08 in median) is clean experimental design. The near-zero correlation between correction terms (r=0.04 in best variant) provides strong evidence of orthogonality, though the median variant more honestly acknowledges partial overlap.

- **S5. Robustness analysis is honest.** The breakeven point at ~35-38% subgroup label noise is clearly identified. The degradation comparison between HB and MLE under misspecification (15% vs 25% RMSE increase at 10% noise) demonstrates the value of partial pooling quantitatively.

- **S6. Expert label budget sensitivity is practically informative.** The crossover analysis across K = {2,4,8} and multiple heterogeneity regimes gives practitioners concrete guidance: n >= 30K as a rule of thumb, with crossover at n=180 for K=2 extreme (best variant) or n=350 for K=2 moderate (median variant).

### Weaknesses

- **W1. [Major] The "Theorem 1" is an identity (at population level), not a bound.** The expression bias(tau_k^global) = sum_j w_j(pi_bar - pi_j)tau_j follows directly from the definition of pooled correction applied to heterogeneous parameters. The reported R^2 < 1.0 against MC simulations reflects finite-sample noise, not bound looseness. Calling this a "bias bound" and reporting R^2 as "bound verification" is misleading. This should be reframed as a "bias decomposition" with empirical verification that the decomposition predicts finite-sample bias accurately. The K=2 simplification to proportionality with Delta_pi * Delta_tau is a first-order approximation (acknowledged), but the base identity is exact.

- **W2. [Major] Systematic undercoverage (88-94% vs nominal 95%) is inadequately addressed.** The papers attribute this to "delta-method approximation underestimating nonlinear error propagation through matrix inversion," but this explanation is asserted rather than demonstrated. If the posterior credible intervals systematically undercover, this is a calibration failure of the method. Concrete questions: (a) Does coverage improve with n? The tables suggest yes (converging to 95% at n=1000), which is consistent with the delta-method explanation. (b) Is the undercoverage worse for subgroups with higher misclassification rates or smaller cell sizes? This interaction is not reported. (c) Have posterior predictive checks or bootstrap alternatives been evaluated? The worst-case variant is more concerning: 83-91% coverage across all conditions, suggesting structural rather than marginal undercoverage. The paper should either fix the calibration (e.g., bootstrap or sandwich variance) or provide deeper analysis of when and why undercoverage occurs.

- **W3. [Major] Semi-synthetic DGP is underspecified.** The papers describe N=12,000-20,000 tweets with "injected CATE heterogeneity structure" but provide insufficient detail on: (a) how outcomes Y are generated (linear? nonlinear? noise distribution?), (b) how treatment T is assigned (random? propensity-based?), (c) how the true CATEs (tau_1, tau_2) are mapped into the text-based pipeline. Without this, the semi-synthetic experiments are not reproducible. This is particularly concerning because the semi-synthetic results are a headline contribution.

- **W4. [Major] Real-data ground truth is opaque.** The best variant reports specific bias and RMSE values for Ashwin et al. data (e.g., "bias 0.003, RMSE 0.013"), implying known true CATEs. But the paper never explains how ground truth CATEs are established in observational refugee interview data. If these are estimated from expert labels alone, they carry their own uncertainty that is not propagated; if from a separate RCT component, this must be stated. The worst variant handles this more honestly by reporting CATE shifts rather than bias, and acknowledging that "no qualitative conclusions change" across methods.

- **W5. [Moderate] "Never worse than global" guarantee is empirical, not theoretical.** The claim is verified as "0% of 1000 MC reps where HB worse than global," which is a strong empirical result but not a proof. The worst variant shows this property fails at 25% subgroup noise and with misaligned subgroups (31% worse than global). The best variant acknowledges the K=8/n=50 failure in the Limitations section but the main text claim is unqualified. A theoretical justification grounded in the monotonicity properties of partial pooling would strengthen this, or the claim should be qualified as "never worse than global when subgroups are correctly specified and n/K is sufficient."

- **W6. [Moderate] Hyperprior specification and sensitivity are missing.** The Dirichlet concentration is parameterized as alpha_k = alpha_0 * c_bar + 1, with a hyperprior on alpha_0 (best/median variants) or alpha_j ~ Gamma(mu_j, sigma_j) (all variants). But the specific hyperprior values (mu_j, sigma_j, or the prior on alpha_0) are never stated, nor is sensitivity to these choices evaluated. For a hierarchical Bayesian method, prior sensitivity is a standard requirement that affects the shrinkage behavior.

### Questions for Authors

- **Q1.** How are ground-truth CATEs established in the Ashwin et al. real-data experiment? If estimated from expert labels, how is the resulting uncertainty propagated into the reported bias and RMSE? The difference between the best variant (reporting precise bias values) and the worst variant (reporting only CATE shifts) suggests this is a nontrivial question.

- **Q2.** In the semi-synthetic setup, please specify: (a) the outcome generation model (functional form, noise variance), (b) whether treatment assignment is randomized or follows a propensity model, and (c) how the true CATEs (tau_1=0.15, tau_2=0.04 in the best variant; tau_1=0.15, tau_2=0.35 in the median variant) are injected.

- **Q3.** The coverage undercoverage (88-94% vs 95%) is attributed to the delta method. Have you evaluated: (a) profile likelihood or bootstrap-based intervals for MLE, (b) whether the HB posterior predictive intervals (as opposed to credible intervals on point estimates) achieve better coverage, or (c) the dependence of undercoverage on cell size n_k?

- **Q4.** What are the exact hyperprior values for the Dirichlet concentration parameter? How sensitive are the RMSE and coverage results to doubling or halving the prior scale?

- **Q5.** The diagnostic AUC (0.82-0.95 depending on variant) is evaluated on the paper's own experiments. Has any form of cross-validation (e.g., leave-one-setting-out) or held-out evaluation been performed? The diagnostic's practical value depends critically on its generalization beyond the specific synthetic/semi-synthetic configurations used to develop it.

### Minor Issues

- The paper should report standard errors on RMSE values, not just point estimates. With 1000 MC replications, SE of RMSE is estimable and should be included.
- The K>2 bias characterization remains informal (Remark rather than Theorem). At minimum, a brief proof sketch or precise statement of regularity conditions would help.
- Computational scaling with K and n is not discussed. The MCMC diagnostics table reports runtime for one configuration; how does runtime scale with K=8 or n=2000?
- The confusion matrix invertibility assumption (det(C_k) != 0) is implicit throughout. It should be stated explicitly, with discussion of what happens when a subgroup has near-singular confusion matrices (e.g., very high accuracy).
- No figures in the main text (only tables). A bias mechanism schematic, amplification heatmap (Delta_pi vs Delta_tau), and ROC curve would substantially improve readability.
- The discrepancy in reported numbers across paper variants (best: AUC=0.953, 7.8x amplification, R^2=0.982; median: AUC=0.82, 4.2x amplification, R^2=0.89) is large. The actual experiments should resolve which regime of results is realistic. The best variant's numbers are notably more optimistic across every metric, suggesting either cherry-picked DGP configurations or overfit experimental design in that scenario.

### Scores
- Soundness: 3 (good; the core identity is correct but "bound" framing is misleading; undercoverage is a real calibration issue; "never worse" needs qualification)
- Empirical Rigor: 3 (good; 11 experiments is comprehensive but semi-synthetic DGP underspecification and real-data ground truth opacity are significant gaps)
- Reproducibility: 2 (partially reproducible; MCMC specs are given but hyperprior values, DGP details, and code are missing)
- Overall: 3.5 (Borderline Conference; strong problem identification and experimental breadth, but methodological claims overreach the evidence, and several critical details are missing for a top-venue methods paper)
- Confidence: 4 (I am confident in this assessment; the identified issues are clear and specific)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06054c3e-f7e1-430e-9a69-9c008903a7a4",
  "isSidechain": true,
  "agentId": "a4fde7b158b599326",
  "requestId": "req_011CbET7U4REk9umtwz42KvR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b54e6acf-cf9a-4e7f-8c6a-00725535ad8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "ca75923e-c9c6-4829-ae10-fa16ed68897c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012zXKZ9MxwJLiKBsyoiE244",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7185,
      "cache_read_input_tokens": 66730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7185,
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
