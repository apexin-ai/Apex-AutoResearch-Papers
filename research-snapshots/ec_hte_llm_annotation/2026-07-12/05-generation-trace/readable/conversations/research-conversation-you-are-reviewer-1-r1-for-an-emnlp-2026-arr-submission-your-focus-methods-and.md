# Research conversation: You are Reviewer 1 (R1) for an EMNLP 2026 ARR submission. Your focus: **methods and experiments**. Evaluate soundness, e

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a4d47027ebc04c351.jsonl`
- **Structured JSON:** [`a04caccd1274b882ba03.json`](../../sessions/a0/a04caccd1274b882ba03.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

43 recorded events

### User

_source line 1 · 2026-05-23T20:28:36.711Z_

You are Reviewer 1 (R1) for an EMNLP 2026 ARR submission. Your focus: **methods and experiments**. Evaluate soundness, experimental design, reproducibility, and whether claims are supported by evidence.

## Venue calibration (EMNLP 2026 ARR)
- 5 = Award consideration (top 2.5%)
- 4 = Conference accept (~21% acceptance)
- 3 = Findings accept
- 2 = Resubmit next cycle
- 1 = Do not resubmit
Dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5)

## Paper summary

Title: "When Debiasing Hurts: Measurement Error Amplification in LLM-Annotated Heterogeneous Treatment Effects"

The paper identifies a failure mode where global (pooled) confusion matrix correction amplifies subgroup-level CATE bias when LLM misclassification rates vary across subgroups. The bias is proportional to Δπ × Δτ (misclassification heterogeneity × CATE heterogeneity). The authors propose EC-HTE (hierarchical Bayesian stratified correction) but find it fails on real data. They also propose a diagnostic criterion that achieves setting-level AUC of only 0.49.

The paper is 8 pages main text + references + 2 appendix sections (MCMC diagnostics, hyperprior sensitivity). It has a Limitations section. Abstract is ~190 words.

## Key content to evaluate

### Section 3: Bias Mechanism
- Eq. 1: Bias_k = f(Δπ_k, Δτ_k) — product-form bias decomposition
- Authors explicitly acknowledge this is "a special case of classical measurement error theory (Carroll et al., 2006; Fuller, 1987)" (lines 060-062)
- EC-HTE: Hierarchical Bayesian with Dirichlet priors on confusion matrix rows, shared hyperprior for partial pooling (James-Stein shrinkage)
- Diagnostic criterion: |Δπ × Δτ| threshold
- PPCI composition for dual-error scenarios

### Section 4: Experimental Setup
- Synthetic: K ∈ {2,4}, moderate/extreme regimes, n ∈ {50,100,250,500,1000,2000}, 3600 MC runs, MCMC: R̂_max=1.024, ESS_min=129
- Semi-synthetic: TweetEval sentiment, 4 subgroups, S0=0.05/S1=0.10/S2=0.15/S3=0.25, P(Z=1)=0.39
- Real data: UC Berkeley Hate Speech, n=2496, Δπ=0.117, global FNR=53%
- Baselines: Naive, Global, EC-HTE, PPCI, DSL per-subgroup

### Section 5: Results (13 tables across 11 subsections)
- 5.1 Bias identity: R²>0.97, tightness ~1.0. Debiasing hurts in ~50% of parameter space, max 2.86× (K=2) and 2.41× (K=4)
- 5.2 Synthetic: HB vs MLE modest gains (4-9% K=2/n=50), larger for K=4/n=50 (-22.7%). Coverage 0.87-0.93
- 5.3 Semi-synthetic: n=50 HB 57% worse; n=100 HB 60% better; n≥500 converge. P(Z=1)=0.39 noted as favorable
- 5.4 **REAL DATA (central result)**: EC-HTE avg|bias|=0.313 > Global 0.273 > Naive 0.210. EC-HTE is WORST. Confirmed by exp-015 (GPT-4.1: 3-4× worse) and exp-016 (GPT-3.5: 3.5-5× worse)
- 5.5 Diagnostic: subgroup AUC=0.833 (requires true CATE), setting AUC=0.490, asymmetric 0.611-0.626
- 5.6 Budget: K=2/extreme crossover n=250; K=2/moderate NEVER; K=4/extreme n=1000; K=4/moderate n=2000
- 5.7 PPCI: PPCI alone |bias|=0.004 vs EC-HTE+PPCI 0.005. RMSE: 0.261 vs 0.225 (14% gain)
- 5.8 6 LLMs: Δπ=0.080-0.198, all >0.05, structural heterogeneity, decreasing trend GPT-3.5→GPT-5.4
- 5.9 CausalForest: EC-HTE lowest bias (0.061) but worst RMSE (0.229 vs 0.166 global, 38% worse). 5.9× max amplification
- 5.10 Robustness: coverage 0.945-0.958 across 0-50% noise. Standard partial pooling property
- 5.11 Adaptive allocation: NOT COMPLETED, projected results only

### Experiment design reference (imagined experiments from plan)
The plan lists exp-001 through exp-011. Comparing to paper:
- exp-001 (synthetic validation) → §5.2 ✓
- exp-002 (bias identity) → §5.1 ✓
- exp-003 (semi-synthetic) → §5.3 ✓
- exp-004 (real data) → §5.4 ✓
- exp-005 (diagnostic) → §5.5 ✓
- exp-006 (budget) → §5.6 ✓
- exp-007 (PPCI/DSL) → §5.7 ✓
- exp-008 (multi-LLM) → §5.8 ✓
- exp-009 (adaptive allocation) → §5.11 (NOT COMPLETED) ✓
- exp-010 (robustness) → §5.10 ✓
- exp-011 (CausalForest) → §5.9 ✓
Coverage: 10/11 completed, 1 projected only. Full coverage of plan.

## Your task
Write a detailed R1 review covering:
1. **Summary** (2-3 sentences)
2. **Strengths** (numbered list)
3. **Weaknesses** (numbered list, with severity: major/minor)
4. **Questions to authors**
5. **Soundness** (1-5 with justification)
6. **Excitement** (1-5 with justification)
7. **Reproducibility** (1-5 with justification)
8. **Overall Assessment** (1-5 half-point scale per ARR)
9. **Confidence** (1-5)

Be rigorous. Focus on whether the experimental evidence supports the claims. Consider: are the synthetic results externally valid? Does the real-data evaluation have sufficient power? Is the proposed method well-motivated given it fails? Is the diagnostic contribution viable? Are the baselines appropriate and fairly compared?


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "0edfa902-b358-4d30-b699-b1732a629106",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-23T20:28:36.717Z_

```json
{
  "parentUuid": "0edfa902-b358-4d30-b699-b1732a629106",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
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
  "uuid": "1dda0d50-e6a0-4993-805c-84e208c0bfa9",
  "timestamp": "2026-05-23T20:28:36.717Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-23T20:28:39.848Z_



I need to read the actual paper and supporting materials before writing the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dda0d50-e6a0-4993-805c-84e208c0bfa9",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8cA4JuBGUBoyQ9kJJJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d0aa2dfa-9436-4dfe-ac69-1af9120e9f2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdUQiov5qBJ5nTMWBEamwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16751,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16751,
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

_source line 4 · 2026-05-23T20:28:40.937Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RL9Mtp4y6B7ZpL68pPLf3d`</summary>

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
  "parentUuid": "d0aa2dfa-9436-4dfe-ac69-1af9120e9f2d",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8cA4JuBGUBoyQ9kJJJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1418e629-a3e6-4fff-a4e9-bd82534360ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VdUQiov5qBJ5nTMWBEamwC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16751,
      "cache_read_input_tokens": 0,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16751
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 104,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16751,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16751,
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

_source line 5 · 2026-05-23T20:28:40.943Z_

<details><summary>↩ Tool result · `toolu_01RL9Mtp4y6B7ZpL68pPLf3d`</summary>

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
  "parentUuid": "1418e629-a3e6-4fff-a4e9-bd82534360ff",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "833d1225-c5e0-4e83-afa9-e6793af83ba5",
  "sourceToolAssistantUUID": "1418e629-a3e6-4fff-a4e9-bd82534360ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-23T20:28:43.253Z_



Let me read the paper and supporting materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "833d1225-c5e0-4e83-afa9-e6793af83ba5",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8cUHvVsDMCBqJwQxQA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22fbf867-3a0d-4a1f-b9d1-6bd66686df5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWniFKQBFNXuLpzdSVRutB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1286,
      "cache_read_input_tokens": 16751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1286,
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

_source line 7 · 2026-05-23T20:28:44.787Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012fWogMgKKoY1Fm8ymFzgFL`</summary>

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
  "parentUuid": "22fbf867-3a0d-4a1f-b9d1-6bd66686df5a",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8cUHvVsDMCBqJwQxQA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ecfe4b9-8083-448c-be0e-c02a85c8a008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWniFKQBFNXuLpzdSVRutB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1286,
      "cache_read_input_tokens": 16751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1286,
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

_source line 8 · 2026-05-23T20:28:44.804Z_

<details><summary>↩ Tool result · `toolu_012fWogMgKKoY1Fm8ymFzgFL`</summary>

```text
artifacts/dream_reports/dream_20260520T185426/best/paper.tex
artifacts/dream_reports/dream_20260520T185426/median/paper.tex
artifacts/dream_reports/dream_20260520T185426/worst/paper.tex
artifacts/dream_reports/dream_20260520T194535/best/paper.tex
artifacts/dream_reports/dream_20260520T194535/median/paper.tex
artifacts/dream_reports/dream_20260520T194535/worst/paper.tex
artifacts/dream_reports/dream_20260521T032758/best/paper.tex
artifacts/dream_reports/dream_20260521T032758/median/paper.tex
artifacts/dream_reports/dream_20260521T032758/worst/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/theory.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/introduction_0b23d3.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/limitations.tex
docs/paper/checklist.tex
artifacts/dream_reports/dream_20260521T122454/best/paper.tex
artifacts/dream_reports/dream_20260521T122454/median/paper.tex
artifacts/dream_reports/dream_20260521T122454/worst/paper.tex
artifacts/_project/intermediate/c1_integration_template.tex
docs/paper/main.tex
docs/paper/method.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/conclusion.tex
artifacts/dream_reports/dream_20260523T193110/best/paper.tex
artifacts/dream_reports/dream_20260523T193110/median/paper.tex
docs/paper/introduction.tex
docs/paper/limitations.tex
artifacts/dream_reports/dream_20260523T193110/worst/paper.tex
docs/paper/experiments.tex
docs/paper/theory.tex
docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ecfe4b9-8083-448c-be0e-c02a85c8a008",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "30f34be9-90f1-42de-9fcd-e7e27d147327",
  "sourceToolAssistantUUID": "3ecfe4b9-8083-448c-be0e-c02a85c8a008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T20:28:45.826Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HN7DvGEDsL38zRa8gn7Qcy`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30f34be9-90f1-42de-9fcd-e7e27d147327",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8cUHvVsDMCBqJwQxQA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7cdf384f-df5d-4797-9fc0-eed3e2790ae2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWniFKQBFNXuLpzdSVRutB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1286,
      "cache_read_input_tokens": 16751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1286,
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

_source line 10 · 2026-05-23T20:28:45.838Z_

<details><summary>↩ Tool result · `toolu_01HN7DvGEDsL38zRa8gn7Qcy`</summary>

```text
artifacts/dream_reports/dream_20260520T185426/best/paper.pdf
artifacts/dream_reports/dream_20260520T185426/median/paper.pdf
artifacts/dream_reports/dream_20260520T185426/worst/paper.pdf
artifacts/dream_reports/dream_20260520T194535/best/paper.pdf
artifacts/dream_reports/dream_20260520T194535/median/paper.pdf
artifacts/dream_reports/dream_20260520T194535/worst/paper.pdf
artifacts/dream_reports/dream_20260521T032758/best/paper.pdf
artifacts/dream_reports/dream_20260521T032758/median/paper.pdf
artifacts/_project/paper/main.pdf
artifacts/dream_reports/dream_20260521T032758/worst/paper.pdf
docs/paper/figures/fig2_heatmap.pdf
docs/paper/figures/fig3_budget.pdf
docs/paper/figures/fig1_bias_mechanism.pdf
artifacts/_project/chart/fig1_bias_mechanism.pdf
artifacts/_project/paper/main_297877.pdf
artifacts/dream_reports/dream_20260521T122454/best/paper.pdf
artifacts/dream_reports/dream_20260521T122454/median/paper.pdf
artifacts/dream_reports/dream_20260521T122454/worst/paper.pdf
docs/paper/figures/applicability_frontier.pdf
artifacts/review_round_3/submitted.pdf
artifacts/review_round_4/submitted.pdf
artifacts/review_round_5/submitted.pdf
artifacts/review_round_6/submitted.pdf
artifacts/review_round_7/submitted.pdf
artifacts/review_round_8/submitted.pdf
artifacts/review_round_9/submitted.pdf
artifacts/review_round_10/submitted.pdf
artifacts/review_round_11/submitted.pdf
artifacts/_project/chart/sign_reversal_figure.pdf
artifacts/_project/chart/cross_llm_heatmap.pdf
artifacts/cross_llm_heatmap.pdf
artifacts/_project/chart/cross_llm_rank_corr_heatmap.pdf
artifacts/cross_llm_rank_corr_heatmap.pdf
artifacts/_project/chart/bias_anatomy_heatmap.pdf
artifacts/bias_anatomy_heatmap.pdf
artifacts/_project/chart/debiasing_hurts_summary.pdf
artifacts/debiasing_hurts_summary.pdf
artifacts/sign_reversal_figure.pdf
artifacts/_project/chart/policy_reversal_zone.pdf
artifacts/policy_reversal_zone.pdf
docs/paper/figures/fig1_sign_reversal.pdf
artifacts/k_scalability_figure.pdf
artifacts/_project/chart/k_scalability_bars.pdf
artifacts/k_scalability_bars.pdf
artifacts/_project/chart/treatment_dep_misclass_figure.pdf
artifacts/treatment_dep_misclass_figure.pdf
docs/paper/figures/policy_reversal_zone.pdf
docs/paper/figures/treatment_dep_misclass.pdf
docs/paper/figures/treatment_dep_misclass_figure.pdf
docs/paper/figures/k_scalability_bars.pdf
docs/paper/figures/k_scalability_figure.pdf
artifacts/review_round_12/submitted.pdf
artifacts/dream_reports/dream_20260523T193110/best/paper.pdf
artifacts/dream_reports/dream_20260523T193110/median/paper.pdf
docs/paper/main.pdf
artifacts/dream_reports/dream_20260523T193110/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cdf384f-df5d-4797-9fc0-eed3e2790ae2",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "363d0257-be7e-47eb-b93a-171b2840b36d",
  "sourceToolAssistantUUID": "7cdf384f-df5d-4797-9fc0-eed3e2790ae2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T20:28:46.080Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QYRVBNsrnyeuSZ57w93JFD`</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "363d0257-be7e-47eb-b93a-171b2840b36d",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8cUHvVsDMCBqJwQxQA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ba4c57c4-10a7-4ac8-8915-d81f7686ecc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWniFKQBFNXuLpzdSVRutB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1286,
      "cache_read_input_tokens": 16751,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1286
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 285,
          "cache_read_input_tokens": 16751,
          "cache_creation_input_tokens": 1286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1286,
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

_source line 12 · 2026-05-23T20:28:46.094Z_

<details><summary>↩ Tool result · `toolu_01QYRVBNsrnyeuSZ57w93JFD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/report.md\", \"content\": \"# Handover — 2026-05-23\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- Paper Agent 正在整合 exp-038/039/040 结果到论文 appendix\\n- Rebuttal talking points 待更新（sign-reversal, F-L, κ, cross-LLM 数据）\\n- EMNLP 2026 ARR DDL: 2026-05-25（~40h）\\n\\n## 近期结论\\n\\n- **exp-038** (success): Policy reversal zone τ sweep — global correction 在 τ(0)<0.05 时导致 CATE sign reversal（τ=0.01→31%, τ=0.03→14.9%），EC-HTE 0% reversal。最危险组合 τ=0.01+δ_misclass=0.19→42.9%。\\n- **exp-039** (success, mixed): K=8 scalability — EC-HTE 在 K=2/4 显著优于 Global（bias 降 5-7×），K=8 退化（RMSE 0.34 vs Global 0.17），但 coverage 始终 ≥95.6%。根因：250/8≈31 expert/subgroup 不足。\\n- **exp-040** (success, mixed): Treatment-dependent misclassification — EC-HTE 在 γ_T≤0.05 时 robust（coverage ≥89.7%, RMSE 优势），γ_T≈0.10 为 breakeven point，γ_T≥0.15 严重退化。\\n- **exp-036** (success): Bootstrap SE 在所有 n_expert≥25 下维持 ≥95% coverage。\\n- **exp-037** (success): Temperature calibration 降低但不消除 Δπ，EC-HTE 仍然必要。\\n- **exp-035** (success): 非对称 CM（FPR≠FNR 7:1）下 coverage ≥93%。\\n\\n## Excitement 提分产出（R17 修复）\\n\\n| Artifact | 核心数字 | 状态 |\\n|----------|---------|------|\\n| sign_reversal_figure | 92% configs affected, 0% EC-HTE | ✅ 已注册 |\\n| cross_llm_heatmap | 9 LLMs, mean ρ=0.244, min=-0.80 | ✅ Reviewer PASS |\\n| bias_anatomy_heatmap | R²=0.9938, 52% grid debiasing hurts | ✅ Reviewer PASS |\\n| debiasing_hurts_summary | 26.5% of 2132 pairs hurt, real LLM 100% | ✅ 已注册 |\\n| policy_reversal_zone | τ=0.01→31% reversal, danger zone 可视化 | ✅ 已注册 |\\n| k_scalability_bars | K=2/4 优, K=8 boundary | ✅ 已注册 |\\n| treatment_dep_misclass_figure | γ_T breakeven ≈0.10 | ✅ 已注册 |\\n\\n## 趋势\\n成功 34 / 负向 5 / 失败 0 / 共 40\\n\\n## 下一步\\n- Paper Agent 整合新实验到论文\\n- Rebuttal talking points 更新\\n- DDL 前编译验证 + 提交\\n\\n## 资源状态\\nautodl-rtx6000: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\nlocal-cpu: 空闲\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1755, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba4c57c4-10a7-4ac8-8915-d81f7686ecc0",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "a4cb18e4-56e7-43ec-a598-776ab81d8b19",
  "sourceToolAssistantUUID": "ba4c57c4-10a7-4ac8-8915-d81f7686ecc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T20:28:49.256Z_

<details open><summary>🔧 Tool call — Read · `toolu_018ExLap6iQBhb4FdFov6vXL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4cb18e4-56e7-43ec-a598-776ab81d8b19",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8crLyzFR2NRN4fiQJE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0d5dc7d0-ad6e-4850-8b0a-6c0657d54e86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJHpx2gKVGGvjgT4ddr7sh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2900,
      "cache_read_input_tokens": 18037,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2900
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 18037,
          "cache_creation_input_tokens": 2900,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2900,
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

_source line 14 · 2026-05-23T20:28:49.263Z_

<details><summary>↩ Tool result · `toolu_018ExLap6iQBhb4FdFov6vXL`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{inconsolata}
9	
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{enumitem}
16	\usepackage{algorithm}
17	\usepackage{algpseudocode}
18	
19	\newtheorem{theorem}{Theorem}
20	\newtheorem{corollary}[theorem]{Corollary}
21	\newtheorem{proposition}[theorem]{Proposition}
22	\newtheorem{remark}[theorem]{Remark}
23	
24	\title{When Debiasing Hurts: An Exact Bias Identity\\for LLM-Annotated Treatment Effects}
25	
26	\author{Anonymous}
27	
28	\begin{document}
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	
35	\input{related_work}
36	
37	\input{theory}
38	
39	\input{method}
40	
41	\input{experiments}
42	
43	\input{conclusion}
44	
45	\input{limitations}
46	
47	\bibliography{references}
48	
49	\appendix
50	\input{appendix}
51	
52	%\input{checklist}
53	
54	\end{document}
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d5dc7d0-ad6e-4850-8b0a-6c0657d54e86",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "699bbf6f-f597-46cd-937d-71c5bdc103fb",
  "sourceToolAssistantUUID": "0d5dc7d0-ad6e-4850-8b0a-6c0657d54e86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T20:28:51.705Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WuKDdzy8X6Ne6azD6cTzz8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "699bbf6f-f597-46cd-937d-71c5bdc103fb",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8d67TfSPk2PE8J1GQE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "beb2df29-0f02-4af3-95a4-9ad9195bf619",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgcSgjWBNGzSghNRNa7o6G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 20937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 586,
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

_source line 16 · 2026-05-23T20:28:51.710Z_

<details><summary>↩ Tool result · `toolu_01WuKDdzy8X6Ne6azD6cTzz8`</summary>

```text
1	\begin{abstract}
2	Standard confusion-matrix correction for noisy annotations assumes uniform error rates.
3	When this assumption fails---as it routinely does with LLM classifiers, whose error rates vary by up to $5\times$ across demographic subgroups---correction can reverse the sign of estimated causal effects, concluding a beneficial treatment is harmful.
4	We derive an exact bias identity for this setting: global correction introduces subgroup-level bias with a product form $\delta_s \cdot \Delta\tau / (1 - 2\bar{\pi})$, factoring into each subgroup's deviation from the pooled error rate, the treatment effect heterogeneity, and an amplification factor from matrix inversion.
5	This population-level identity---verified at $R^2 \geq 0.97$ across synthetic grids and 11 real LLM--dataset combinations---predicts that global correction reverses CATE sign in 14.9\% of configurations and amplifies bias in all eight real LLMs tested.
6	The identity yields a diagnostic: a condition on per-subgroup error rates alone predicts when correction increases bias, without estimating any treatment effects (AUC $= 1.0$ on subgroups with non-zero effect heterogeneity).
7	The per-subgroup correction prescribed by the identity reduces $|\text{bias}|$ by $7.4\times$ via hierarchical Bayesian estimation; the advantage requires sufficient error heterogeneity and expert budget.
8	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "beb2df29-0f02-4af3-95a4-9ad9195bf619",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "3cc328bb-e051-4129-b992-7850744bb867",
  "sourceToolAssistantUUID": "beb2df29-0f02-4af3-95a4-9ad9195bf619",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T20:28:52.174Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BFQEzyYoDt32mCbNfRbvcZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cc328bb-e051-4129-b992-7850744bb867",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8d67TfSPk2PE8J1GQE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a6f09d11-ad85-41ba-8bf4-5b6319fa9385",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgcSgjWBNGzSghNRNa7o6G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 20937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 586,
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

_source line 18 · 2026-05-23T20:28:52.179Z_

<details><summary>↩ Tool result · `toolu_01BFQEzyYoDt32mCbNfRbvcZ`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	Consider estimating whether a content moderation policy reduces hate speech differently across demographic groups, using GPT-4 to classify thousands of posts.
5	After standard confusion-matrix correction, the analysis concludes the policy \emph{increases} hate speech among younger users---but the true effect is protective.
6	This sign reversal is not an edge case.
7	
8	Large language models (LLMs) now routinely replace human annotators in computational social science (CSS), producing labels for sentiment, hate speech, stance, and political discourse at costs orders of magnitude below manual coding~\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp}.
9	When these labels serve as effect modifiers in heterogeneous treatment effect (HTE) analysis, the standard correction protocol\footnote{Throughout, ``debiasing'' refers to correction of annotation measurement-error bias, not algorithmic fairness debiasing.} is straightforward: validate a sample against expert annotations, estimate a confusion matrix, and apply its inverse uniformly to correct conditional average treatment effect (CATE) estimates.
10	Yet LLM annotations are not uniformly accurate: \citet{ashwin2025bias} document misclassification rates varying by up to 5$\times$ across demographic subgroups defined by refugee status, gender, and education level; in our pilot study, GPT-4.1 achieves 85.8\% accuracy on TweetEval sentiment, but error rates range from 10.2\% to 20.0\% across text-feature subgroups ($\Delta\pi = 0.098$).
11	
12	We show that this standard correction can make things worse.
13	In 14.9\% of our synthetic configurations (across a grid of $\Delta\pi$ and $\tau(0)$ values; $\tau(0) = 0.03$), global correction reverses the sign of estimated CATE---a protective treatment ($\tau = +0.03$) appears harmful ($\hat{\tau} = -0.059$)---rising to 31\% at $\tau(0) = 0.01$ (Figure~\ref{fig:sign_reversal}); all eight real LLMs tested amplify bias under global correction, while EC-HTE eliminates sign reversal entirely.
14	Global correction amplifies bias by up to 5.9$\times$ ($K{=}4$ with CausalForest); the classical Frazis-Loeb attenuation correction~\cite{frazis2003estimating} \emph{increases} bias by up to 2.9$\times$.
15	The mechanism is over-correction: for subgroups with near-zero misclassification, the naive estimator is nearly unbiased, yet pooled correction calibrated for the average error rate introduces substantial bias precisely where labels were most trustworthy.
16	
17	We derive an exact bias identity explaining when and why this occurs (Theorem~\ref{thm:bias_identity}): the correction-induced bias in each subgroup factors into three independently estimable components, verified empirically at $R^2 \geq 0.97$ on synthetic grids and 11 real LLM--dataset combinations spanning open-source and proprietary model families.
18	The identity yields a diagnostic (Proposition~\ref{prop:debiasing_hurts}) that predicts when global correction will harm a subgroup using only per-subgroup misclassification rates, without estimating any treatment effects (AUC $= 1.0$ on subgroups with non-zero effect heterogeneity; Section~\ref{sec:diagnostic}).
19	
20	The per-subgroup correction prescribed by the identity---implemented via hierarchical Bayesian confusion matrix estimation (EC-HTE)---reduces $|\text{bias}|$ from 0.059 to 0.008 under extreme heterogeneity ($K{=}2$).
21	The advantage is conditional: when $\Delta\pi$ is small, the variance cost of stratification outweighs its bias benefit.
22	
23	Existing corrections---PPI~\cite{angelopoulos2023ppi}, DSL~\cite{egami2024dsl}, PPCI~\cite{sui2026ppci}, arm-specific PPI~\cite{mozer2026ppi}, ForestIV~\cite{bu2023forestiv}---assume homogeneous prediction error; none addresses effect modifier misclassification (Section~\ref{sec:related}).
24	
25	\begin{figure*}[t]
26	\centering
27	\includegraphics[width=\textwidth]{figures/fig1_sign_reversal.pdf}
28	\caption{CATE sign reversal under global correction ($K{=}2$, $\tau(0) = 0.03$). (A) Naive vs.\ global-corrected CATE; red triangles mark sign reversals (7.5\% of subgroup estimates). (B) Extreme case: true $\tau = +0.03$, estimated $\hat{\tau} = -0.059$. (C) 14.9\% of configurations exhibit sign reversal; all 8 real LLMs amplify bias; EC-HTE: 0\% reversal.}
29	\label{fig:sign_reversal}
30	\end{figure*}
31	
32	Our contributions are:
33	\begin{itemize}
34	    \item An exact finite-population bias identity (Theorem~\ref{thm:bias_identity}): standard confusion-matrix correction---the default in PPI, DSL, and CSS practice---introduces subgroup-level bias with multiplicative structure $\delta_s \cdot \Delta\tau / (1-2\bar{\pi})$, explaining when and why correction reverses CATE sign (14.9\% of configurations at $\tau(0) = 0.03$; 31\% at $\tau(0) = 0.01$), verified at $R^2 \geq 0.97$ on synthetic grids, 11 real LLM--dataset combinations, and demographic subgroups (Sections~\ref{sec:theory},~\ref{sec:bias_mechanism}).
35	    \item An actionable diagnostic (Proposition~\ref{prop:debiasing_hurts}): a condition on per-subgroup misclassification rates alone predicts when global correction increases bias, without estimating any treatment effects (AUC $= 1.0$ on subgroups with non-zero effect heterogeneity)---independently useful without adopting any specific correction method (Section~\ref{sec:diagnostic}).
36	    \item The per-subgroup correction prescribed by the identity, implemented via hierarchical Bayesian confusion matrix estimation (EC-HTE)---compatible with difference-in-means, CausalForest, and R-learner, and composable with PPCI for joint covariate/outcome error (Sections~\ref{sec:method}--\ref{sec:diagnostic}).
37	\end{itemize}
38	The bias identity applies beyond LLM annotation to any proxy classifier with subgroup-varying error rates; survey coding, medical diagnosis, and satellite imagery classification share this structure.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6f09d11-ad85-41ba-8bf4-5b6319fa9385",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "51d3d763-c16b-414b-b09a-39869d9612ab",
  "sourceToolAssistantUUID": "a6f09d11-ad85-41ba-8bf4-5b6319fa9385",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T20:28:52.637Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q5Rpq96L68AJZ24pkTiiPi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51d3d763-c16b-414b-b09a-39869d9612ab",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8d67TfSPk2PE8J1GQE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "00843467-7625-4715-af54-c87ad2e6788a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgcSgjWBNGzSghNRNa7o6G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 20937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 586,
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

_source line 20 · 2026-05-23T20:28:52.642Z_

<details><summary>↩ Tool result · `toolu_01Q5Rpq96L68AJZ24pkTiiPi`</summary>

```text
1	% Requires preamble: \usepackage{amsthm,amsmath,amssymb}
2	% and: \newtheorem{theorem}{Theorem}
3	%      \newtheorem{corollary}[theorem]{Corollary}
4	%      \newtheorem{proposition}[theorem]{Proposition}
5	
6	\section{Bias Decomposition: When Debiasing Hurts}
7	\label{sec:theory}
8	
9	We formalize the bias that global misclassification correction introduces when subgroup error rates are heterogeneous.
10	Consider estimating the conditional average treatment effect (CATE) $\tau(z) = \mathbb{E}[Y(1) - Y(0) \mid Z = z]$, where $Z \in \{0, 1\}$ is a binary effect modifier observed only through a noisy annotation $\hat{Z}$.
11	The population consists of $K$ subgroups $S \in \{1, \ldots, K\}$ with weights $w_s = P(S{=}s)$, each characterized by a $2 \times 2$ confusion matrix $C_s$ with symmetric error rate $\pi_s = P(\hat{Z} \neq Z \mid S{=}s)$.
12	Standard practice estimates a single confusion matrix $\bar{C} = \sum_s w_s C_s$ from expert annotations and applies its inverse uniformly to all observations, with pooled error rate $\bar{\pi} = \sum_s w_s \pi_s$.
13	We show that when error rates vary across subgroups, this global procedure introduces a bias with an exact product form.
14	
15	We state five assumptions maintained throughout.
16	%
17	\begin{itemize}
18	\item[\textbf{(A1)}] \textit{Conditional independence:} misclassification depends only on the true label $Z$ and subgroup $S$, not on potential outcomes $Y(0), Y(1)$.
19	\item[\textbf{(A2)}] \textit{Symmetric misclassification:} $P(\hat{Z}{=}1 \mid Z{=}0, S{=}s) = P(\hat{Z}{=}0 \mid Z{=}1, S{=}s) = \pi_s$ for all $s$ (diagnostic only; see Remark~2).
20	\item[\textbf{(A3)}] \textit{Balanced effect modifier:} $P(Z{=}0) = P(Z{=}1) = 0.5$. This simplifies the exposition; we discuss relaxation below.
21	\item[\textbf{(A4)}] \textit{Non-degeneracy:} $\pi_s \neq 0.5$ for all $s$, ensuring each $C_s$ is invertible.
22	\item[\textbf{(A5)}] \textit{Homogeneous treatment effects across subgroups:} $\tau(z, s) = \tau(z)$ for all $s$, so $\Delta\tau = \tau(1) - \tau(0)$ is a scalar.
23	\end{itemize}
24	
25	Under (A2)--(A3), the Bayesian mixing matrix $M_s$ (entries $M_s[\hat{z}, z] = P(Z{=}z \mid \hat{Z}{=}\hat{z}, S{=}s)$) coincides with $C_s$.
26	The global mixing matrix is $M_{\text{global}} = \sum_s w_s M_s$.
27	
28	\begin{theorem}[Bias Decomposition Identity]
29	\label{thm:bias_identity}
30	Under \textnormal{(A1)--(A5)}, the bias of global correction in subgroup $s$ at effect-modifier level $z$ is
31	\begin{align}
32	\mathrm{bias}_{\mathrm{global}}(z{=}0, s) &= +\frac{\delta_s \cdot \Delta\tau}{1 - 2\bar{\pi}}, \label{eq:bias_z0} \\
33	\mathrm{bias}_{\mathrm{global}}(z{=}1, s) &= -\frac{\delta_s \cdot \Delta\tau}{1 - 2\bar{\pi}}, \label{eq:bias_z1}
34	\end{align}
35	where $\delta_s = \pi_s - \bar{\pi}$ is the subgroup deviation from the pooled error rate and $\Delta\tau = \tau(1) - \tau(0)$ is the CATE heterogeneity.
36	\end{theorem}
37	
38	Equations~\eqref{eq:bias_z0}--\eqref{eq:bias_z1} constitute an exact finite-population identity, not an asymptotic approximation or bound.
39	The bias factors into three interpretable components: $\delta_s$ captures how much subgroup $s$ deviates from the average misclassification rate, $\Delta\tau$ captures treatment effect heterogeneity across levels of $Z$, and $1/(1 - 2\bar{\pi})$ is an amplification factor from matrix inversion.
40	Bias vanishes when either source of variation is absent ($\delta_s = 0$ or $\Delta\tau = 0$), and arises only through their interaction.
41	Theorem~\ref{thm:bias_identity} implies that global correction trades one source of confounding for another: it removes attenuation from label noise but introduces a new bias from error-rate heterogeneity.
42	
43	\paragraph{Proof sketch.}
44	Global correction applies $M_{\text{global}}^{-1}$ to the subgroup-specific observed CATE $\tau_{\text{obs}}(\cdot, s) = M_s \cdot \tau_{\text{true}}$, yielding bias $(M_{\text{global}}^{-1} M_s - I) \cdot \tau_{\text{true}}$.
45	Direct computation shows $M_{\text{global}}^{-1} M_s - I = \frac{\delta_s}{1-2\bar{\pi}} \bigl[\begin{smallmatrix} -1 & 1 \\ 1 & -1 \end{smallmatrix}\bigr]$.
46	Applying this matrix to $[\tau(0),\, \tau(1)]^\top$ produces the product form.
47	The full derivation appears in Appendix~\ref{app:derivation}.
48	For comparison with classical scalar attenuation~\citep{frazis2003estimating}, see Section~\ref{sec:related}.
49	
50	\paragraph{Relationship to classical scalar attenuation.}
51	Classical scalar attenuation~\citep{frazis2003estimating} gives $\beta^* = \beta(1 - 2\pi)$; dividing by $(1 - 2\bar{\pi})$ removes this bias under homogeneous errors, but Theorem~\ref{thm:bias_identity} characterizes a structurally distinct quantity: \emph{correction-induced} bias from applying $M_{\mathrm{global}}^{-1}$ to heterogeneous $M_s$.
52	F-L scalar correction (dividing $\hat{\tau}(z)$ by $1 - 2\bar{\pi}$) over-corrects low-error and under-corrects high-error subgroups---the same mechanism as global CM correction but restricted to a scalar ignoring the mixing structure between $z$-levels.
53	When $\pi_s \to 0.5$, $(1 - 2\pi_s) \to 0$ and the F-L per-subgroup correction diverges; EC-HTE's $\kappa$-guard (Section~\ref{sec:method}) avoids this singularity.
54	Table~\ref{tab:main_results} confirms: under extreme heterogeneity ($K{=}2$), the classical F-L scalar correction \emph{increases} $|\text{bias}|$ from 0.058 to 0.122 ($2.1\times$ naive), and F-L per-subgroup to 0.168 ($2.9\times$)---the textbook attenuation correction systematically amplifies bias when subgroup error rates differ.
55	
56	\begin{remark}
57	Theorem~\ref{thm:bias_identity} does not require assumption~(A2).
58	For arbitrary asymmetric confusion matrices ($\mathrm{FPR}_s \neq \mathrm{FNR}_s$),
59	the product form $\mathrm{bias}(z, s) = \Delta\tau \cdot [B_s]_{z,1}$ holds exactly,
60	where $B_s = M_{\mathrm{global}}^{-1} M_s - I$, because $B_s \mathbf{1} = \mathbf{0}$
61	follows from stochasticity of $M_s$ and $M_{\mathrm{global}}$ alone.
62	Assumption~(A2) simplifies $[B_s]_{z,1}$ to the scalar
63	$\pm \delta_s / (1 - 2\bar{\pi})$ but is not necessary for the product structure.
64	Under asymmetric errors, the diagnostic (Proposition~\ref{prop:debiasing_hurts}) requires evaluating $[B_s]_{z,1}$ cell-by-cell rather than via a single scalar threshold; the AUC decreases from 0.86 to 0.66 (Appendix~\ref{app:asymmetric}), reflecting the additional complexity of cell-specific error rates.
65	For binary effect modifiers ($|\mathcal{Z}|{=}2$), the asymmetric score $|[B_s]_{z,1}|$ reduces to a monotone transform of the symmetric score $|\delta_s|/((1{-}2\bar{\pi})\pi_s)$, because column-stochastic $M$ forces $|B_s[0,1]|{=}|B_s[1,1]|$; practitioners may use the simpler symmetric formula without loss.
66	See Appendix~\ref{app:asymmetric} for the full derivation and empirical verification
67	($R^2 = 0.991$).
68	\end{remark}
69	
70	\begin{remark}[Assumption (A5) is not necessary]
71	(A5) simplifies $\Delta\tau_s$ to a scalar $\Delta\tau$, but the identity is exact without it: when treatment effects vary across subgroups, the bias is $+\delta_s \cdot \Delta\tau_s / (1 - 2\bar{\pi})$ at $z{=}0$ and $-\delta_s \cdot \Delta\tau_s / (1 - 2\bar{\pi})$ at $z{=}1$, where $\Delta\tau_s = \tau_s(1) - \tau_s(0)$ (Corollary~\ref{cor:a5_relaxation}).
72	The proof is immediate: the bias matrix $B_s = M_{\mathrm{global}}^{-1} M_s - I$ depends only on the confusion matrices, not on $\tau$.
73	The diagnostic (Proposition~\ref{prop:debiasing_hurts}) also extends without (A5): $\Delta\tau_s$ cancels in the comparison $|\mathrm{bias}_{\mathrm{global}}| \gtrless |\mathrm{bias}_{\mathrm{naive}}|$, so condition~\eqref{eq:hurts_condition} remains $\Delta\tau$-free.
74	EC-HTE's correction does not depend on (A5): each $\hat{C}_s^{-1}$ corrects the local misclassification structure regardless of whether $\Delta\tau$ varies; under both positive and negative $\Delta\tau_s$--$\delta_s$ correlation, EC-HTE maintains $\geq$93\% coverage while global correction degrades to 74--82\% (Appendix~\ref{app:a5_violation}).
75	\end{remark}
76	
77	The identity extends to $K > 2$ subgroups with $J$ effect-modifier levels; the multi-class bias retains the same product structure with modified amplification terms (Corollary~\ref{cor:multiclass} in Appendix~\ref{app:multiclass}).
78	
79	Assumption~(A3) ensures $M_s = C_s$; when $P(Z{=}1) \neq 0.5$, the mixing matrices acquire asymmetric entries, but the product structure persists with modified coefficients (Appendix~\ref{app:derivation}).
80	Empirical verification under class imbalance (Appendix~\ref{app:classimbalance}) shows $R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$ for $K{=}2$, though EC-HTE's RMSE ratio relative to global correction increases to 1.06--1.68 as imbalance grows.
81	Empirical verification (Section~\ref{sec:bias_mechanism}) yields $R^2 = 0.994$ for $K{=}2$ and $R^2 = 0.97$ for $K{=}4$, closing the theory-practice gap to essentially zero; the residual variance reflects Monte Carlo noise, not model misspecification.
82	
83	\paragraph{Sensitivity to (A1).}
84	Assumption~(A1) is not empirically testable.
85	If misclassification correlates with potential outcomes ($\gamma = \mathrm{Corr}(\mathbb{1}[\hat{Z} {\neq} Z],\, Y(1){-}Y(0) \mid Z, S) \neq 0$), Theorem~\ref{thm:bias_identity} gains an $O(\gamma)$ perturbation; in NLP settings, this is plausible when LLM accuracy varies with outcome magnitude.
86	Sensitivity analysis frameworks~\cite{lash2009applying,dorn2022sharp,cinelli2020making} can bound the degradation (Section~\ref{sec:limitations}).
87	
88	\paragraph{Finite-sample remainder.}
89	Theorem~\ref{thm:bias_identity} is a population-level identity.
90	In practice, confusion matrices are estimated from $n_{\text{expert}}$ expert labels with $\hat{C}_s = C_s + E_s$, $\|E_s\| = O_p(n_{\text{expert}}^{-1/2})$; the resulting remainder is therefore $R_n = O_p(n_{\text{expert}}^{-1/2} \cdot \kappa(C_s))$, motivating the singularity guard ($\kappa > 100 \to$ fallback) in Section~\ref{sec:method}.
91	
92	\begin{proposition}[Debiasing Can Increase Bias]
93	\label{prop:debiasing_hurts}
94	Under \textnormal{(A1)--(A5)}, global correction produces larger absolute bias than the naive estimator ($|\mathrm{bias}_{\mathrm{global}}| > |\mathrm{bias}_{\mathrm{naive}}|$) in subgroup $s$ if and only if
95	\begin{equation}
96	\frac{|\delta_s|}{(1 - 2\bar{\pi}) \cdot \pi_s} > 1.
97	\label{eq:hurts_condition}
98	\end{equation}
99	\end{proposition}
100	
101	Equation~\eqref{eq:hurts_condition} partitions subgroups into two regimes:
102	\begin{itemize}
103	    \item \textit{High-error} ($\pi_s > \bar{\pi}$): the condition reduces to $\pi_s > 0.5$, excluded by~(A4); global correction always reduces bias.
104	    \item \textit{Low-error} ($\pi_s < \bar{\pi}$): the condition holds whenever $\pi_s < \bar{\pi} / (2(1 - \bar{\pi}))$---easily satisfied: when $\bar{\pi} = 0.15$, any subgroup with $\pi_s < 0.088$ is harmed by global correction.
105	\end{itemize}
106	The mechanism is over-correction: for subgroups with near-zero misclassification ($\pi_s \approx 0$), the naive estimator is nearly unbiased, yet global inversion calibrated for $\bar{\pi}$ creates substantial bias---debiasing is worse than doing nothing, and can reverse bias sign across subgroups.
107	
108	In our experiments (Section~\ref{sec:bias_mechanism}), global correction increases bias in 50\% of $K{=}2$ configurations (260/520), with amplification reaching $2.86\times$ ($K{=}2$) and $2.41\times$ ($K{=}4$); Figure~\ref{fig:heatmap} visualizes the full parameter grid.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00843467-7625-4715-af54-c87ad2e6788a",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "4f664d10-7895-4eaa-b388-449f148b73e2",
  "sourceToolAssistantUUID": "00843467-7625-4715-af54-c87ad2e6788a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T20:28:53.109Z_

<details open><summary>🔧 Tool call — Read · `toolu_012TWW4evYWsBVsaTKJavDHn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f664d10-7895-4eaa-b388-449f148b73e2",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8d67TfSPk2PE8J1GQE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ba9b933-9e99-497c-b81e-c171c66db403",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgcSgjWBNGzSghNRNa7o6G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 20937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 586,
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

_source line 22 · 2026-05-23T20:28:53.114Z_

<details><summary>↩ Tool result · `toolu_012TWW4evYWsBVsaTKJavDHn`</summary>

```text
1	\section{Correction Prescribed by the Identity}
2	\label{sec:method}
3	
4	Theorem~\ref{thm:bias_identity} identifies per-subgroup misclassification deviation as the bias source; the natural correction is per-subgroup confusion matrix inversion.
5	This correction (EC-HTE) proceeds in three stages: estimate per-subgroup confusion matrices via hierarchical Bayes, invert them to correct observed outcome moments, and propagate correction uncertainty into downstream causal estimators.
6	The complete procedure is summarized in Algorithm~\ref{alg:echte} (Appendix~\ref{app:algorithm}).
7	
8	\subsection{Hierarchical Bayes Confusion Matrix Estimation}
9	
10	We place a Dirichlet-Multinomial hierarchical model over the confusion matrices $\{C_s\}_{s=1}^K$.
11	For each subgroup $s$, row $j$ of $C_s$ has a Dirichlet prior centered at the global pooled confusion matrix $\hat{C}_{\text{global}}$: $\text{Dir}(\alpha_0 \cdot \hat{C}_{\text{global},j})$, where $\hat{C}_{\text{global},j}$ is the $j$-th row of the pooled CM and $\alpha_0 > 0$ is a shared concentration parameter estimated via empirical Bayes (marginal likelihood maximization).
12	Large $\alpha_0$ pulls subgroup estimates toward $\hat{C}_{\text{global}}$ (global correction), while small $\alpha_0$ allows subgroup-specific rates to dominate (stratified correction).
13	This partial pooling---a form of James-Stein shrinkage well-established in small-area estimation---borrows strength across subgroups when estimating confusion matrices from limited expert labels, reducing variance for small subgroups while preserving heterogeneity where data support it.
14	
15	Posterior inference uses centered empirical Bayes optimization ($<$5ms for $K{=}4$, $N{=}5{,}000$); a full Gibbs MCMC alternative requires $\sim$5s (convergence diagnostics in Appendix~\ref{app:algorithm}).
16	Bootstrap SE ($B{=}100$) adds $\sim$0.4s.
17	HB estimation outperforms stratified MLE in 87.5\% of configurations (21 of 24) across the experimental grid (Section~\ref{sec:ec_hte_eval}), with the largest gains when $n_{\text{expert}} / K < 100$.
18	The advantage requires $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ per subgroup; below this threshold, stratified MLE is preferred because the hierarchical model lacks sufficient observations for stable shrinkage.
19	At $n_{\text{expert}} \geq 1000$, HB and stratified MLE converge to within 0.5\% on all metrics.
20	Sensitivity analysis shows $<$5\% RMSE variation under 2$\times$ hyperprior perturbation, confirming that results are not driven by prior specification.
21	
22	\subsection{Subgroup-Stratified Correction}
23	
24	Given posterior mean confusion matrices $\hat{C}_s$, we correct observed outcome moments per subgroup by matrix inversion:
25	\begin{equation}
26	\tilde{\boldsymbol{\mu}}_s = \hat{C}_s^{-1} \cdot \hat{\boldsymbol{\mu}}_s,
27	\end{equation}
28	where $\hat{\boldsymbol{\mu}}_s = [\hat{\tau}_{\text{obs}}(0, s),\, \hat{\tau}_{\text{obs}}(1, s)]^\top$ collects the observed conditional outcome moments in subgroup $s$.
29	This requires $\det(\hat{C}_s) \neq 0$ for all $s$, which holds under assumption~(A4) ($\pi_s \neq 0.5$) but may fail in finite samples when error rates approach degeneracy.
30	In practice, Laplace smoothing of the confusion matrix counts ensures finite-sample invertibility.
31	We impose a singularity guard: if the condition number $\kappa(\hat{C}_s) > 100$ (for a $2{\times}2$ symmetric confusion matrix, this corresponds to $\pi_s > 0.495$, i.e., near-random classification), subgroup $s$ falls back to global correction $\bar{C}^{-1}$; when the fallback triggers, the standard error computation also uses $\bar{C}^{-1}$ for that subgroup, ensuring consistency between point estimates and confidence intervals.
32	This hard guard prevents numerical catastrophe; $\kappa \leq 1.25$ is a sufficient condition for strongest bias reduction (Appendix~\ref{sec:budget}), though EC-HTE maintains calibrated coverage ($\geq$93\%) across the wider $\kappa \in [1.4, 3.0]$ range observed in practice (Appendix~\ref{app:kappa_analysis}).
33	
34	The contrast with global correction is direct.
35	Global correction applies $\bar{C}^{-1}$ uniformly to all subgroups, introducing the $\delta_s \cdot \Delta\tau$ bias identified in Theorem~\ref{thm:bias_identity}.
36	Subgroup-stratified correction eliminates this bias by matching each subgroup's correction to its own misclassification structure, at the cost of higher variance from estimating $K$ separate confusion matrices (Appendix~\ref{sec:budget}).
37	
38	\subsection{Variance-Adjusted CausalForest}
39	
40	For heterogeneous treatment effect estimation, we feed corrected covariates into CausalForestDML~\cite{wager2018causal} with honest splitting.
41	The forest produces per-observation standard error estimates $\text{se}_i$.
42	To account for confusion matrix correction, we propagate uncertainty through the inverse mapping:
43	\begin{equation}
44	\text{se}_{\text{corrected},i} = \sqrt{\text{diag}\!\left(\hat{C}_{S_i}^{-1}\, \text{diag}(\text{se}_i^2)\, \hat{C}_{S_i}^{-\top}\right)}.
45	\end{equation}
46	This plug-in SE conditions on $\hat{C}_s$, neglecting CM estimation uncertainty; at $n_{\text{expert}} \geq 100$ this is negligible, but below this threshold a full bootstrap ($B{=}100$; re-estimate CM and re-fit per replicate) maintains $\geq$95\% coverage across all budgets tested ($n_{\text{expert}} \in \{25, 50, 75, 100, 200\}$); even plug-in SE achieves $\geq$91\% at $n_{\text{expert}}{=}25$ (Appendix~\ref{app:bootstrap_se}).
47	When $n_{\text{expert}}/K < 50$, we recommend bootstrap SE; otherwise plug-in SE suffices.
48	
49	\paragraph{Diagnostic criterion.}
50	Proposition~\ref{prop:debiasing_hurts} provides a $\Delta\tau$-free diagnostic: global correction harms subgroup $s$ if and only if $|\delta_s| / ((1-2\bar{\pi}) \cdot \pi_s) > 1$, a condition depending only on per-subgroup misclassification rates estimable from a pilot sample.
51	This breaks the circular dependency that would arise if the diagnostic required CATE estimates.
52	A threshold classifier achieves AUC~=~0.86 at the subgroup level, reaching 1.0 when restricted to subgroups with $\tau_s > 0$ (Section~\ref{sec:diagnostic}).
53	
54	\paragraph{Composition with PPCI.}
55	EC-HTE corrects structured covariate misclassification through $\hat{C}_s^{-1}$ inversion but cannot address outcome-level measurement error.
56	PPCI~\cite{sui2026ppci} corrects residual outcome bias using a debiasing estimator but assumes correct covariate labels.
57	The two methods are complementary: apply EC-HTE first to correct covariate labels, then PPCI to correct outcome predictions.
58	Neither is redundant with the other: EC-HTE alone cannot fix outcome error, while PPCI alone incurs higher variance for covariate error.
59	Under both error types simultaneously, the composition reduces $|\text{bias}|$ from 0.179 to 0.007 (Appendix~\ref{sec:ppci}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ba9b933-9e99-497c-b81e-c171c66db403",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "1ebb8c80-c281-49e0-b38e-a26c0985974b",
  "sourceToolAssistantUUID": "4ba9b933-9e99-497c-b81e-c171c66db403",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T20:28:53.539Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EEo7fajvx2xzvqWuFqVu3R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ebb8c80-c281-49e0-b38e-a26c0985974b",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8d67TfSPk2PE8J1GQE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "69773dc5-a61c-45a5-8579-a5d02768c04b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VgcSgjWBNGzSghNRNa7o6G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 20937,
      "output_tokens": 377,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 586
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 377,
          "cache_read_input_tokens": 20937,
          "cache_creation_input_tokens": 586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 586,
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

_source line 24 · 2026-05-23T20:28:53.543Z_

<details><summary>↩ Tool result · `toolu_01EEo7fajvx2xzvqWuFqVu3R`</summary>

```text
1	\section{Experiments}
2	
3	\subsection{Setup}
4	
5	We test on synthetic ($N{=}5{,}000$, $K \in \{2, 4\}$, controlled $\Delta\tau$ and $\Delta\pi$, 100 MC runs) and semi-synthetic (TweetEval sentiment~\cite{barbieri2020tweeteval}, $K{=}4$ unbalanced subgroups, $\pi \in \{0.05, 0.10, 0.15, 0.25\}$) DGPs; full specifications in Appendix~\ref{app:dgp}.
6	
7	We compare: (1) \textit{Naive} (no correction), (2) \textit{Global} (pooled confusion matrix, equivalent to PPI/DSL~\cite{angelopoulos2023ppi,egami2024dsl} with homogeneous error), (3) \textit{Stratified MLE} (per-subgroup DSL without shrinkage), (4) \textit{HB EC-HTE} (per-subgroup correction), (5) \textit{PPCI}~\cite{sui2026ppci}, and (6) \textit{EC-HTE+PPCI}.
8	For CausalForest~\cite{wager2018causal}, we compare naive, global, and EC-HTE variants.
9	Primary metrics are $|\text{bias}|$, RMSE, and 95\% CI coverage, averaged across subgroups and 100 MC runs.
10	Robustness validation covers hate speech, six OpenAI models, subgroup misspecification, asymmetric confusion matrices, confounded treatment, outcome-dependent misclassification (all $\geq$93.5\% coverage), and treatment-dependent misclassification ($\approx$90\% at $\gamma_T \leq 0.05$; Appendices~\ref{app:hatespeech}--\ref{app:treatment_dep}).
11	
12	\subsection{Empirical Validation of the Bias Identity}
13	\label{sec:bias_mechanism}
14	
15	We verify Theorem~\ref{thm:bias_identity} on a $K{=}2$ grid (520 configurations, $\Delta\pi \in [0, 0.25]$, $\Delta\tau \in (0, 0.50]$) and a $K{=}4$ grid (Appendix~\ref{app:dgp}).
16	Regressing observed subgroup bias on $\delta_s \cdot \Delta\tau / (1{-}2\bar{\pi})$ yields $R^2 = 0.994$ ($K{=}2$) and $0.97$ ($K{=}4$); residual variance reflects MC noise ($R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$; Appendix~\ref{app:classimbalance}).
17	Global correction worsens bias in 50\% of $K{=}2$ configurations (260/520, excluding $\Delta\pi{=}0$), with amplification reaching 2.86$\times$ ($K{=}2$) and 2.41$\times$ ($K{=}4$); Figure~\ref{fig:heatmap} visualizes the amplification surface.
18	Beyond amplification, global correction reverses the sign of estimated CATE---concluding a protective treatment is harmful---in 14.9\% of configurations at $\tau(0) = 0.03$ (31\% at $\tau(0) = 0.01$; critical threshold $\tau(0) < 0.089$, matching Theorem~\ref{thm:bias_identity}), with all eight real LLMs amplifying bias under global correction; EC-HTE eliminates sign reversal entirely (Figure~\ref{fig:sign_reversal}; Appendix~\ref{app:policy_reversal}).
19	
20	\subsection{Correction Evaluation}
21	\label{sec:ec_hte_eval}
22	
23	Table~\ref{tab:main_results} presents the main results across representative configurations.
24	In the $K{=}2$ extreme row, global correction \emph{increases} $|\text{bias}|$ relative to naive (0.059 vs.\ 0.058), confirming the over-correction mechanism of Theorem~\ref{thm:bias_identity}.
25	F-L scalar correction increases $|\text{bias}|$ to 0.122 (coverage 0.68); F-L per-subgroup to 0.168 as $(1{-}2\pi_s) \to 0$---both worse than naive (Table~\ref{tab:main_results}).
26	HB EC-HTE reduces $|\text{bias}|$ from 0.059 to 0.008 (7.4$\times$) at $K{=}2$ and from 0.056 to 0.012 (4.7$\times$) at $K{=}4$, maintaining near-nominal coverage (0.94--0.96) with lower RMSE than stratified MLE.
27	Under moderate heterogeneity and in TweetEval ($K{=}4$), methods converge ($p > 0.05$); EC-HTE incurs higher RMSE when $\Delta\pi$ is small (Table~\ref{tab:main_supp}).
28	At $K{=}8$ ($n_{\text{expert}}/K{=}31$), coverage remains $\geq$95.6\% but RMSE increases; we recommend $n_{\text{expert}}/K \geq 50$ (Appendix~\ref{app:k8_subgroups}).
29	
30	\paragraph{CausalForest.}
31	Theorem~\ref{thm:bias_identity} applies to any estimator whose inputs pass through a confusion matrix; CausalForest~\cite{wager2018causal} with a noisy effect modifier $\hat{Z}$ inherits the same $M_{\text{global}}^{-1} M_s$ structure.
32	With CausalForest ($K{=}4$, extreme, $n{=}500$), EC-HTE reduces $|\text{bias}|$ from 0.191 to 0.039 (4.9$\times$) with coverage 0.90; global amplifies bias up to 5.9$\times$ (Table~\ref{tab:main_results}; bootstrap SE in Appendix~\ref{app:bootstrap_se}).
33	
34	\begin{table}[t]
35	\centering
36	\caption{Main results (extreme heterogeneity). Metrics averaged over subgroups, $z$-levels, 100 MC runs. Bold: lowest $|\text{bias}|$. $^\dagger$RMSE exceeds Global. F-L Scalar: $\hat{\tau}/(1{-}2\bar{\pi})$~\cite{frazis2003estimating}; F-L Per-sub.: per-subgroup variant (binary $Z$ only). Moderate/TweetEval in Table~\ref{tab:main_supp}; MC SEs in Appendix~\ref{app:mcse}.}
37	\label{tab:main_results}
38	\resizebox{\columnwidth}{!}{%
39	\begin{tabular}{ll ccc}
40	\toprule
41	Configuration & Method & $|\text{Bias}|$ & RMSE & 95\% CI Cov. \\
42	\midrule
43	\multirow{6}{*}{\shortstack[l]{DIM\\$K{=}2$, $n{=}250$}}
44	 & Naive & 0.058 & 0.090 & 0.82 \\
45	 & Global & 0.059 & 0.099 & 0.87 \\
46	 & F-L Scalar & 0.122 & 0.159 & 0.68 \\
47	 & F-L Per-sub. & 0.168 & 0.220 & 0.65 \\
48	 & Strat.\ MLE & 0.012 & 0.094 & 0.95 \\
49	 & HB EC-HTE & \textbf{0.008} & 0.089 & 0.94 \\
50	\midrule
51	\multirow{4}{*}{\shortstack[l]{DIM\\$K{=}4$, $n{=}500$}}
52	 & Naive & 0.062 & 0.113 & 0.88 \\
53	 & Global & 0.056 & 0.125 & 0.91 \\
54	 & Strat.\ MLE & \textbf{0.010} & 0.127$^\dagger$ & 0.95 \\
55	 & HB EC-HTE & 0.012 & 0.120 & 0.96 \\
56	\midrule
57	\multirow{3}{*}{\shortstack[l]{CausalForest\\$K{=}4$, $n{=}500$}}
58	 & Naive & 0.208 & 0.231 & 0.44 \\
59	 & Global & 0.191 & 0.244 & 0.58 \\
60	 & EC-HTE Forest & \textbf{0.039} & 0.180 & 0.90 \\
61	\bottomrule
62	\end{tabular}}
63	\end{table}
64	
65	\subsection{Actionable Diagnostic}
66	\label{sec:diagnostic}
67	
68	Proposition~\ref{prop:debiasing_hurts} provides a $\Delta\tau$-free diagnostic: global correction increases bias in subgroup $s$ iff $|\delta_s| / ((1-2\bar{\pi}) \cdot \pi_s) > 1$, computable from a pilot sample without estimating treatment effects.
69	The diagnostic achieves AUC $= 0.63$ across 16 real LLM--dataset combinations; restricting to subgroups with $\Delta\tau > 0$ recovers AUC $= 1.0$ ($0.86$ on synthetic grids; Figure~\ref{fig:roc}, Appendix~\ref{app:screening}).
70	For $K{=}2$, $|\delta_0|{=}|\delta_1|$ limits discrimination; a meta-criterion ($\max_s \mathrm{score}(s) > 1$) recovers reliability for $K{\geq}4$ (Appendix~\ref{app:screening}).
71	
72	The condition number $\kappa(\hat{C}_s)$ provides a practical guard: $\kappa > 100$ triggers fallback; all 13 tested LLM--dataset combinations fall in $\kappa \in (1.25, 3]$ with calibrated coverage $\geq$93\% (Appendix~\ref{app:kappa_analysis}).
73	Budget crossover, $K{=}8$ scalability, and multi-LLM validation ($R^2 = 0.975$) appear in Appendices~\ref{sec:budget}--\ref{app:multilm}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69773dc5-a61c-45a5-8579-a5d02768c04b",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "54a34440-9de3-4649-8733-31cb7277a25a",
  "sourceToolAssistantUUID": "69773dc5-a61c-45a5-8579-a5d02768c04b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T20:28:57.523Z_

<details open><summary>🔧 Tool call — Read · `toolu_01C6hNQgbqXLaugsnpB3QG2i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54a34440-9de3-4649-8733-31cb7277a25a",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8dQDPCJpsZgzDG59Gj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "559a5267-385c-4b7d-b13d-22083b0a570a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5zoWNMCYdLVdZ9dgS7pTS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12105,
      "cache_read_input_tokens": 21523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12105,
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

_source line 26 · 2026-05-23T20:28:57.527Z_

<details><summary>↩ Tool result · `toolu_01C6hNQgbqXLaugsnpB3QG2i`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Measurement error and annotation models.}
5	Classical measurement error theory shows that correction via estimated error models can amplify MSE when the error structure is misspecified~\cite{fuller1987measurement,carroll2006measurement}; Bayesian approaches require informative priors when identification is weak~\cite{gustafson2003measurement}, and nonparametric methods use repeated measurements or instruments to recover the true distribution~\cite{hu2008nonparametric}.
6	
7	Three distinctions separate our contribution from prior measurement error analyses.
8	First, we study effect modifier misclassification---the mismeasured variable defines the CATE function itself---rather than regressor~\cite{frazis2003estimating,carroll2006measurement} or confounder~\cite{ogburn2012nondifferential,greenland1980effect} error, where attenuation is the primary concern.
9	Second, Theorem~\ref{thm:bias_identity} derives a bias identity for correction-induced bias---bias created by the debiasing procedure---rather than bounding the attenuation from misclassification itself.
10	Concretely, \citet{frazis2003estimating} derive scalar attenuation for the uncorrected estimator under homogeneous misclassification; Theorem~\ref{thm:bias_identity} characterizes a structurally distinct quantity---correction-induced bias that is subgroup-specific, potentially sign-reversing, and absent from the uncorrected estimator.
11	The homogeneous-error setting ($K{=}1$, $\delta_s{=}0$) is a degenerate case recovering classical attenuation~\cite{blackwell2017unified}; empirically, F-L correction produces higher bias under heterogeneous misclassification, while EC-HTE achieves near-oracle performance (Appendix~\ref{app:fl_comparison}).
12	Third, the $\delta_s \cdot \Delta\tau$ product structure arises only under heterogeneous error rates; all homogeneous-error analyses~\cite{battistin2014treatment,fong2021machine} miss this interaction entirely.
13	In the annotation literature, \citet{dawid1979maximum} introduced confusion matrix estimation for multiple annotators, with extensions to item difficulty, annotator competence, and hierarchical priors~\cite{passonneau2014benefits,hovy2013learning,paun2018comparing}.
14	Our hierarchical estimator (Section~\ref{sec:method}) adapts this architecture from label aggregation to causal inference, tying the prior structure to the subgroup dimension that defines treatment effect heterogeneity.
15	
16	\paragraph{HTE estimation and LLM annotation error.}
17	Causal forests~\cite{athey2016recursive,wager2018causal}, double/debiased ML~\cite{chernozhukov2018dml,semenova2021debiased}, doubly-robust CATE estimators~\cite{kennedy2023dr}, and meta-learners~\cite{kunzel2019metalearners} all assume that covariates defining heterogeneity are observed without error; when the effect modifier is misclassified, CATE estimates conflate effects across groups.
18	Per-subgroup correction restores valid inputs to any downstream estimator.
19	The corrected pseudo-outcomes are in principle compatible with other HTE estimators such as the R-learner~\citep{nie2021quasi}.
20	For broader perspectives on causal inference with text data, see \citet{feder2022causal} and \citet{keith2020text}; \citet{wang2020methods} study inference correction when outcomes are ML-predicted, a related but distinct problem from effect modifier misclassification.
21	LLMs now match crowd-worker accuracy on many classification tasks~\cite{gilardi2023chatgpt,tornberg2024chatgpt,ziems2024nlp,pangakis2023automated}, but \citet{ashwin2025bias} show that error rates vary by up to $5\times$ across demographic subgroups; \citet{cheng2024err} demonstrate that prompt optimization can reduce such error, a complementary preprocessing step.
22	This subgroup-varying error distorts the very contrasts that define the research question; prior work documents the pattern without correcting downstream causal estimands.
23	Concurrent work identifies variance-side LLM measurement error~\cite{messing2026hidden}; \citet{camuffo2025variance} characterize five variance sources in LLM annotation, complementary to our bias-side analysis.
24	Temperature or Platt scaling~\cite{guo2017calibration} reduces per-subgroup $\pi_s$ but does not eliminate heterogeneity $\Delta\pi$; per-subgroup correction addresses the residual $\delta_s$-driven bias that persists post-calibration (Appendix~\ref{app:calibration} empirically confirms this complementarity).
25	
26	\paragraph{Prediction-powered and design-based correction.}
27	PPI~\cite{angelopoulos2023ppi,zrnic2024cross} and DSL~\cite{egami2024dsl} correct population-level aggregates assuming homogeneous prediction error.
28	In our setting---binary effect modifier with known subgroup structure, a special case of the broader problems DSL addresses---DSL's measurement error correction reduces, under the confusion-matrix parameterization we adopt, to confusion matrix inversion: pooled DSL is equivalent to our Global baseline, and per-subgroup DSL to Stratified MLE (Section~\ref{sec:ec_hte_eval}; Appendix~\ref{app:ppi_comparison}).
29	Our hierarchical estimator adds partial pooling across subgroups, borrowing strength to reduce variance---a mechanism outside the DSL framework.
30	\citet{audinet2025benchmarking} benchmark DSL and PPI debiasing for LLM-based parameter estimation, documenting bias-variance tradeoffs analogous to our findings; their analysis targets population-level parameters rather than subgroup-conditional estimands, leaving the $\delta_s \cdot \Delta\tau$ interaction we formalize unaddressed.
31	\citet{mozer2026ppi} extend PPI to arm-specific ATE correction; PPCI~\cite{sui2026ppci} targets conditional estimands but corrects outcome-side error ($\hat{Y}$ given true $Z$), not covariate-side misclassification; ForestIV~\cite{bu2023forestiv} targets the outcome model rather than the heterogeneity structure.
32	None corrects bias when the mismeasured variable is the effect modifier indexing the CATE function.
33	\citet{imai2010causal} study treatment misclassification via instrumental variables or partial identification; \citet{ura2015heterogeneous} extends this to HTE with mismeasured treatment via IV.
34	\citet{miao2018identifying} develop proximal causal inference for unmeasured confounders using proxy variables; our setting differs because $\hat{Z}$ is a moderator proxy rather than a confounder proxy, admitting confusion-matrix correction without the identification constraints of the proximal framework.
35	Extended discussion appears in Appendix~\ref{app:related}.
36	Our validation combines synthetic DGPs, semi-synthetic experiments, and real LLM confusion matrices, consistent with PPI and DSL evaluation methodology; Appendix~\ref{app:multilm} validates both $\Delta\pi$ heterogeneity and the bias identity itself ($R^2 = 0.975$) across 11 model--dataset combinations.
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "559a5267-385c-4b7d-b13d-22083b0a570a",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "d81c4049-4040-4e36-9839-4d06da727d74",
  "sourceToolAssistantUUID": "559a5267-385c-4b7d-b13d-22083b0a570a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T20:28:58.064Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FQKBhyMEu5Nucz8JjP6pE5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d81c4049-4040-4e36-9839-4d06da727d74",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8dQDPCJpsZgzDG59Gj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a031bd93-9e8e-44b5-89be-37467237f8b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5zoWNMCYdLVdZ9dgS7pTS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12105,
      "cache_read_input_tokens": 21523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12105,
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

_source line 28 · 2026-05-23T20:28:58.068Z_

<details><summary>↩ Tool result · `toolu_01FQKBhyMEu5Nucz8JjP6pE5`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Standard confusion-matrix correction---the default in PPI, DSL, and CSS practice---can reverse causal conclusions when misclassification rates vary across subgroups.
4	We derived an exact bias identity (Theorem~\ref{thm:bias_identity}) explaining when and why, verified across synthetic grids, 11 LLM--dataset combinations, and demographic subgroups.
5	The identity yields a diagnostic (Proposition~\ref{prop:debiasing_hurts}) that flags harmful correction from error rates alone, and prescribes per-subgroup correction that eliminates sign reversal, given sufficient error heterogeneity and expert budget.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a031bd93-9e8e-44b5-89be-37467237f8b5",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "1d5c78cd-9cc5-48cb-9c8e-a25200bc9fce",
  "sourceToolAssistantUUID": "a031bd93-9e8e-44b5-89be-37467237f8b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T20:28:58.547Z_

<details open><summary>🔧 Tool call — Read · `toolu_0135HB5fZ3Y2xPUDnwpH31gg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d5c78cd-9cc5-48cb-9c8e-a25200bc9fce",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8dQDPCJpsZgzDG59Gj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34a6beed-0e09-462d-97be-d538930ec862",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5zoWNMCYdLVdZ9dgS7pTS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12105,
      "cache_read_input_tokens": 21523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12105,
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

_source line 30 · 2026-05-23T20:28:58.551Z_

<details><summary>↩ Tool result · `toolu_0135HB5fZ3Y2xPUDnwpH31gg`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Per-subgroup correction requires $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ expert labels per subgroup and moderate classifier accuracy ($\text{FPR}_s, \text{FNR}_s < 0.5$); below these thresholds, stratification incurs more variance than the bias it removes.
5	At $K{=}8$ with $n_{\text{expert}}{=}250$ (${\approx}31$ labels/subgroup), coverage remains nominal ($\geq$95.6\%) but RMSE exceeds global correction, establishing a scalability boundary under fixed expert budget (Appendix~\ref{app:k8_subgroups}).
6	The diagnostic (Proposition~\ref{prop:debiasing_hurts}) achieves AUC $= 0.86$ on synthetic data but degrades to $0.63$ on real LLM confusion matrices (Appendix~\ref{app:screening}); it should be paired with $R^2$ validation of the bias identity rather than used as a standalone rule.
7	
8	Assumption~(A1)---conditional independence of misclassification and potential outcomes---is not empirically testable.
9	Sensitivity analysis shows robustness up to $\gamma = 0.2$ for outcome-dependent misclassification (coverage $\geq$93.5\%; Appendix~\ref{app:a1_sensitivity}) and $\gamma_T \leq 0.05$ for treatment-dependent misclassification (coverage $\geq$89.7\%; Appendix~\ref{app:treatment_dep}).
10	
11	The method requires discrete, pre-specified subgroups; continuous effect modifiers require discretization, and data-driven subgroup discovery risks overfitting.
12	Ground-truth subgroup CATEs are unavailable in public datasets---classic causal inference benchmarks lack the LLM annotation step that creates the measurement error we address---so we use synthetic CATE injection on real text features and real LLM annotations (Appendices~\ref{app:dgp},~\ref{app:multilm}).
13	Code and data generation scripts will be released upon acceptance.
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34a6beed-0e09-462d-97be-d538930ec862",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "9d83bda5-30d3-4b82-b530-2589535dfa1c",
  "sourceToolAssistantUUID": "34a6beed-0e09-462d-97be-d538930ec862",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T20:28:58.837Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y9pqnLgzrKiJcUTeYGubSc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d83bda5-30d3-4b82-b530-2589535dfa1c",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8dQDPCJpsZgzDG59Gj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d13650d3-d3dd-47ea-8373-b364fb7aaaaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5zoWNMCYdLVdZ9dgS7pTS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12105,
      "cache_read_input_tokens": 21523,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12105
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 308,
          "cache_read_input_tokens": 21523,
          "cache_creation_input_tokens": 12105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12105,
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

_source line 32 · 2026-05-23T20:28:59.236Z_

<details><summary>↩ Tool result · reported error · `toolu_01Y9pqnLgzrKiJcUTeYGubSc`</summary>

```text
File content (39508 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d13650d3-d3dd-47ea-8373-b364fb7aaaaf",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "39462333-0cd1-4fbd-ab6d-ce5ff2828b8a",
  "toolUseResult": "Error: File content (39508 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "d13650d3-d3dd-47ea-8373-b364fb7aaaaf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T20:29:02.824Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W48kSrspJ5L3EcfcKmXTkL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39462333-0cd1-4fbd-ab6d-ce5ff2828b8a",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8dpJira6sPiHYahdti",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d3083edb-16f9-4619-b37e-7e0495d19a2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N2ZoArb6GPhQjvjkcKNKs1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3019,
      "cache_read_input_tokens": 33628,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3019
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 33628,
          "cache_creation_input_tokens": 3019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3019,
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

_source line 34 · 2026-05-23T20:29:02.830Z_

<details><summary>↩ Tool result · `toolu_01W48kSrspJ5L3EcfcKmXTkL`</summary>

```text
1	\section{EC-HTE Procedure}
2	\label{app:algorithm}
3	
4	\begin{algorithm}[t]
5	\caption{EC-HTE: Error-Corrected Heterogeneous Treatment Effects}
6	\label{alg:echte}
7	\begin{algorithmic}[1]
8	\Require Observations $\{(Y_i, W_i, \hat{Z}_i, X_i)\}_{i=1}^N$; expert labels $\{Z_j^*\}_{j=1}^{n_{\text{expert}}}$; subgroup map $S: \mathcal{X} \to \{1,\ldots,K\}$
9	\Ensure Corrected CATE estimates $\hat{\tau}(z)$ with variance-adjusted CIs
10	\Statex
11	\State \textbf{Preconditions:} verify $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$ and $\max_s(\text{FPR}_s, \text{FNR}_s) < 0.5$; if either fails, use global correction
12	\Statex
13	\State \textbf{Step 1: Estimate per-subgroup confusion matrices (HB)}
14	\For{$s = 1, \ldots, K$}
15	    \State $C_s[j,\cdot] \sim \mathrm{Dir}(\alpha_0 \cdot \hat{C}_{\text{global},j})$, \; $\alpha_0$ via empirical Bayes
16	    \State Gibbs sampler (4 chains, 4000 iter) on $\{(\hat{Z}_j, Z_j^*) : S_j = s\}$
17	    \State $\hat{C}_s \gets$ posterior mean; verify $\hat{R} < 1.01$
18	\EndFor
19	\Statex
20	\State \textbf{Step 2: Correct observed outcome moments}
21	\For{$s = 1, \ldots, K$}
22	    \If{$\kappa(\hat{C}_s) > 100$} $\hat{C}_s \gets \bar{C}$ \Comment{singularity guard}
23	    \EndIf
24	    \State $\tilde{\boldsymbol{\mu}}_s \gets \hat{C}_s^{-1} \hat{\boldsymbol{\mu}}_s$
25	\EndFor
26	\Statex
27	\State \textbf{Step 3: CausalForestDML with variance-adjusted SEs}
28	\State Train CausalForest (honest splitting) on corrected outcome moments $\tilde{\boldsymbol{\mu}}_s$
29	\State $\mathrm{se}_{\mathrm{adj},i} \gets \sqrt{\mathrm{diag}(\hat{C}_{S_i}^{-1}\, \mathrm{diag}(\mathrm{se}_i^2)\, \hat{C}_{S_i}^{-\top})}$
30	\State \Return $\hat{\tau}(z)$ with 95\% CIs from $\mathrm{se}_{\mathrm{adj}}$
31	\end{algorithmic}
32	\end{algorithm}
33	
34	\subsection{Condition Number Guard Ablation}
35	\label{app:kappa_ablation}
36	
37	The singularity guard in Algorithm~\ref{alg:echte} (line~6) falls back to global correction when $\kappa(\hat{C}_s) > 100$.
38	We verify that this threshold is not load-bearing by sweeping $\kappa \in \{10, 25, 50, 100, 200, 500, 1000\}$ under the standard DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs).
39	Across all configurations, the maximum observed condition number is $\kappa_{\max} = 1.89$ (mean 1.45, p99 1.89), providing a $53{\times}$ safety margin below the $\kappa{=}100$ threshold.
40	Consequently, the guard never triggers at any tested threshold, and all $\kappa$ values produce identical RMSE (HB: 0.076, Global: 0.077) and zero numerical instability.
41	In a stress test with near-random labeling ($\pi_s \approx 0.4$--$0.5$, $n_{\text{expert}}{=}50$), the maximum condition number reaches 1{,}125, correctly triggering the $\kappa{=}100$ guard and preventing catastrophic inversion.
42	The adaptive formula $\kappa_{\text{adapt}} = 10 \sqrt{n_{\text{expert}} / K}$ recovers $\kappa{=}100$ for this regime and scales naturally with the estimation precision.
43	
44	\section{Full Proof of Theorem~\ref{thm:bias_identity}}
45	\label{app:derivation}
46	
47	\paragraph{Setup.}
48	Under assumptions (A1)--(A4), the observed CATE in subgroup $s$ at effect-modifier level $z$ is
49	\begin{equation}
50	\tau_{\text{obs}}(z, s) = \sum_{z'} M_s[z, z'] \cdot \tau(z'),
51	\end{equation}
52	where $M_s[z, z'] = P(Z{=}z' \mid \hat{Z}{=}z, S{=}s)$ is the mixing matrix.
53	Under (A2)--(A3), $M_s = \bigl[\begin{smallmatrix} 1-\pi_s & \pi_s \\ \pi_s & 1-\pi_s \end{smallmatrix}\bigr]$.
54	
55	\paragraph{Global correction.}
56	The pooled mixing matrix is $M_{\text{global}} = \sum_s w_s M_s = \bigl[\begin{smallmatrix} 1-\bar{\pi} & \bar{\pi} \\ \bar{\pi} & 1-\bar{\pi} \end{smallmatrix}\bigr]$, with $\bar{\pi} = \sum_s w_s \pi_s$.
57	
58	Global correction applies $M_{\text{global}}^{-1}$ to $\tau_{\text{obs}}(\cdot, s)$:
59	\begin{equation}
60	\hat{\tau}_{\text{global}}(z, s) = [M_{\text{global}}^{-1} M_s \cdot \boldsymbol{\tau}]_z,
61	\end{equation}
62	where $\boldsymbol{\tau} = [\tau(0), \tau(1)]^\top$.
63	
64	\paragraph{Bias computation.}
65	The bias is $\hat{\tau}_{\text{global}}(z, s) - \tau(z) = [(M_{\text{global}}^{-1} M_s - I) \boldsymbol{\tau}]_z$.
66	
67	Direct computation gives:
68	\begin{equation}
69	M_{\text{global}}^{-1} = \frac{1}{1 - 2\bar{\pi}} \begin{bmatrix} 1-\bar{\pi} & -\bar{\pi} \\ -\bar{\pi} & 1-\bar{\pi} \end{bmatrix}.
70	\end{equation}
71	Multiplying by $M_s$:
72	\begin{equation}
73	\resizebox{.88\columnwidth}{!}{$\displaystyle
74	M_{\text{global}}^{-1} M_s = \frac{1}{1-2\bar{\pi}} \begin{bmatrix} (1{-}\bar{\pi})(1{-}\pi_s) - \bar{\pi}\pi_s & (1{-}\bar{\pi})\pi_s - \bar{\pi}(1{-}\pi_s) \\ -\bar{\pi}(1{-}\pi_s) + (1{-}\bar{\pi})\pi_s & -\bar{\pi}\pi_s + (1{-}\bar{\pi})(1{-}\pi_s) \end{bmatrix}.
75	$}
76	\end{equation}
77	
78	Define $\delta_s = \pi_s - \bar{\pi}$. Substituting $\pi_s = \bar{\pi} + \delta_s$:
79	\begin{equation}
80	M_{\text{global}}^{-1} M_s - I = \frac{\delta_s}{1-2\bar{\pi}} \begin{bmatrix} -1 & 1 \\ 1 & -1 \end{bmatrix}.
81	\end{equation}
82	
83	To verify: the $(1,1)$ entry of $M_{\text{global}}^{-1} M_s$ is
84	{\small
85	\begin{align}
86	&\frac{(1{-}\bar{\pi})(1{-}\bar{\pi}{-}\delta_s) - \bar{\pi}(\bar{\pi}{+}\delta_s)}{1-2\bar{\pi}} \nonumber\\
87	&= \frac{(1{-}\bar{\pi})^2 - (1{-}\bar{\pi})\delta_s - \bar{\pi}^2 - \bar{\pi}\delta_s}{1-2\bar{\pi}} \nonumber\\
88	&= \frac{1 - 2\bar{\pi} - \delta_s}{1-2\bar{\pi}} = 1 - \frac{\delta_s}{1-2\bar{\pi}}.
89	\end{align}
90	}
91	
92	Applying $(M_{\text{global}}^{-1} M_s - I)$ to $\boldsymbol{\tau}$:
93	{\small
94	\begin{align}
95	\text{bias}(z{=}0, s) &= \tfrac{\delta_s}{1-2\bar{\pi}}(-\tau(0) + \tau(1)) = +\tfrac{\delta_s \cdot \Delta\tau}{1-2\bar{\pi}}, \\
96	\text{bias}(z{=}1, s) &= \tfrac{\delta_s}{1-2\bar{\pi}}(\tau(0) - \tau(1)) = -\tfrac{\delta_s \cdot \Delta\tau}{1-2\bar{\pi}},
97	\end{align}
98	}
99	where $\Delta\tau = \tau(1) - \tau(0)$. \qed
100	
101	\section{Multi-class Extension and Proof}
102	\label{app:multiclass}
103	
104	\begin{corollary}[Multi-class Extension]
105	\label{cor:multiclass}
106	For $K > 2$ subgroups with $J$ effect-modifier levels and uniform off-diagonal misclassification (misclassified observations from class $j$ are distributed equally among the remaining $J{-}1$ classes), the subgroup bias of global correction generalizes to
107	\begin{equation}
108	\mathrm{bias}_{\mathrm{global}}(z, s) = \sum_{j=1}^{J} \bigl(\bar{\pi}_j - \pi_{s,j}\bigr) \cdot \bigl(\tau(j) - \bar{\tau}\bigr) \cdot g(\bar{\pi}),
109	\label{eq:multiclass}
110	\end{equation}
111	where $g(\bar{\pi})$ collects the matrix-inversion amplification terms.\footnote{For $J=3$ with symmetric misclassification (off-diagonal errors uniform), $g(\bar{\pi}) = 1/(1 - 3\bar{\pi}/2)$, generalizing the $J{=}2$ factor $1/(1-2\bar{\pi})$. In general, $g(\bar{\pi}) = 1/(1 - J\bar{\pi}/(J-1))$.}
112	The essential structure, $\sum_s w_s (\bar{\pi}_j - \pi_{s,j}) = 0$, ensures that bias redistributes across subgroups rather than vanishing in aggregate.
113	\end{corollary}
114	
115	\paragraph{Proof.}
116	For $K > 2$ subgroups with $J$ effect-modifier levels, the subgroup-specific mixing matrix $M_s$ is $J \times J$ with entries $M_s[j, j'] = P(Z{=}j' \mid \hat{Z}{=}j, S{=}s)$.
117	The global mixing matrix is $M_{\text{global}} = \sum_s w_s M_s$.
118	
119	The bias of global correction in subgroup $s$ at level $z$ is:
120	\begin{equation}
121	\text{bias}_{\text{global}}(z, s) = [(M_{\text{global}}^{-1} M_s - I) \boldsymbol{\tau}]_z.
122	\end{equation}
123	
124	Write $M_s = M_{\text{global}} + \Delta_s$ where $\Delta_s = M_s - M_{\text{global}}$ satisfies $\sum_s w_s \Delta_s = 0$.
125	Then $M_{\text{global}}^{-1} M_s = I + M_{\text{global}}^{-1} \Delta_s$, so:
126	\begin{equation}
127	\text{bias}_{\text{global}}(z, s) = [M_{\text{global}}^{-1} \Delta_s \cdot \boldsymbol{\tau}]_z.
128	\end{equation}
129	
130	For symmetric misclassification with per-class error rates $\pi_{s,j}$ and pooled rates $\bar{\pi}_j$, the entries of $\Delta_s$ have the form $\Delta_s[j,j'] = (\bar{\pi}_j - \pi_{s,j}) \cdot h(j, j')$ for a function $h$ determined by the off-diagonal redistribution pattern.
131	Expanding the matrix-vector product and collecting terms yields:
132	\begin{equation}
133	\text{bias}_{\text{global}}(z, s) = \sum_{j=1}^{J} (\bar{\pi}_j - \pi_{s,j}) \cdot (\tau(j) - \bar{\tau}) \cdot g(\bar{\pi}),
134	\end{equation}
135	where $g(\bar{\pi})$ collects the matrix-inversion amplification terms and $\bar{\tau} = \sum_j P(Z{=}j) \tau(j)$.
136	
137	The essential structure $\sum_s w_s (\bar{\pi}_j - \pi_{s,j}) = 0$ ensures that the weighted bias across subgroups sums to zero: global correction redistributes bias rather than creating or eliminating it in aggregate.
138	For non-uniform off-diagonal entries, the scalar amplification $g(\bar{\pi})$ generalizes to a cell-specific matrix; the product structure $B_s \cdot \Delta\tau$ persists but a closed-form amplification factor does not. \qed
139	
140	\section{Proof of Proposition~\ref{prop:debiasing_hurts}}
141	\label{app:debiasing_hurts}
142	
143	The naive estimator has bias $\tau_{\text{obs}}(z,s) - \tau(z)$.
144	Under (A2)--(A3), $\tau_{\text{obs}}(0,s) = (1-\pi_s)\tau(0) + \pi_s\tau(1)$, so $\text{bias}_{\text{naive}}(0,s) = \pi_s \cdot \Delta\tau$.
145	
146	Global correction produces larger absolute bias when $|\text{bias}_{\text{global}}(0,s)| > |\text{bias}_{\text{naive}}(0,s)|$:
147	\begin{equation}
148	\frac{|\delta_s| \cdot |\Delta\tau|}{|1-2\bar{\pi}|} > \pi_s \cdot |\Delta\tau|.
149	\end{equation}
150	Since $\Delta\tau \neq 0$ (otherwise both biases are zero), dividing through gives:
151	\begin{equation}
152	\frac{|\delta_s|}{(1-2\bar{\pi}) \cdot \pi_s} > 1,
153	\end{equation}
154	where we use $1-2\bar{\pi} > 0$ from (A4).
155	
156	For high-error subgroups ($\pi_s > \bar{\pi}$, so $\delta_s > 0$): the condition becomes $(\pi_s - \bar{\pi}) / ((1-2\bar{\pi})\pi_s) > 1$, which simplifies to $\pi_s(1 - 1 + 2\bar{\pi}) > \bar{\pi}$, i.e., $2\bar{\pi}\pi_s > \bar{\pi}$, i.e., $\pi_s > 0.5$.
157	This is excluded by (A4), so global correction always reduces bias in high-error subgroups.
158	
159	For low-error subgroups ($\pi_s < \bar{\pi}$, so $\delta_s < 0$): the condition becomes $(\bar{\pi} - \pi_s) / ((1-2\bar{\pi})\pi_s) > 1$, which gives $\pi_s < \bar{\pi} / (1 - 2\bar{\pi} + 1) = \bar{\pi} / (2(1-\bar{\pi}))$.
160	When $\bar{\pi} = 0.15$, any subgroup with $\pi_s < 0.088$ experiences increased bias from global correction. \qed
161	
162	\paragraph{Extension to asymmetric misclassification.}
163	Proposition~\ref{prop:debiasing_hurts} assumes symmetric error rates (A2).
164	Under asymmetric misclassification ($\mathrm{FPR}_s \neq \mathrm{FNR}_s$), the naive bias becomes $\mathrm{bias}_{\mathrm{naive}}(0,s) = \mathrm{FPR}_s \cdot \tau(1) + (1 - \mathrm{FPR}_s - 1)\tau(0)$ and the global correction bias depends on the full $2 \times 2$ structure of $B_s = M_{\mathrm{global}}^{-1} M_s - I$ (Remark~1 in Section~\ref{sec:theory}).
165	A sufficient condition for global correction to increase bias is
166	\begin{equation}
167	\|B_s\|_\infty > \max(\mathrm{FPR}_s, \mathrm{FNR}_s),
168	\end{equation}
169	which reduces to Equation~\eqref{eq:hurts_condition} when $\mathrm{FPR}_s = \mathrm{FNR}_s = \pi_s$.
170	In the asymmetric experiments (Appendix~\ref{app:asymmetric}), the symmetric diagnostic still achieves AUC $= 0.66$ when applied with $\pi_s = (\mathrm{FPR}_s + \mathrm{FNR}_s)/2$, suggesting practical robustness.
171	A fully general asymmetric diagnostic that accounts for the separate roles of FPR and FNR in each entry of $B_s$ is left to future work.
172	
173	\section{Semi-Synthetic Data Generating Process}
174	\label{app:dgp}
175	
176	\paragraph{Synthetic DGP (Sections~\ref{sec:bias_mechanism}--\ref{sec:diagnostic} and Appendix~\ref{sec:budget}).}
177	We generate $N = 5000$ observations.
178	Each observation belongs to one of $K \in \{2, 4\}$ subgroups $S \in \{1, \ldots, K\}$ with equal weights $w_s = 1/K$.
179	The binary effect modifier $Z \in \{0, 1\}$ is drawn with $P(Z{=}1) = 0.5$.
180	Treatment assignment is $T \sim \text{Bernoulli}(0.5)$, independent of $Z$ and $S$.
181	
182	The outcome is generated as:
183	\begin{equation}
184	Y = \tau(Z) \cdot T + \eta, \quad \eta \sim \mathcal{N}(0, 1),
185	\end{equation}
186	where the CATE function is $\tau(z) = \bar{\tau} + \Delta\tau \cdot (z - 0.5)$ with $\bar{\tau} = 0.5$.
187	The CATE heterogeneity $\Delta\tau \in \{0, 0.2, 0.5, 1.0\}$ controls the strength of treatment effect variation across levels of $Z$.
188	
189	Misclassification is symmetric: $\hat{Z} \neq Z$ with probability $\pi_s$ depending on subgroup.
190	For $K{=}2$: $\pi_1 = \bar{\pi} - \Delta_c/2$, $\pi_2 = \bar{\pi} + \Delta_c/2$, with $\bar{\pi} \in \{0.1, 0.2\}$ and $\Delta_c \in \{0, 0.05, 0.1, 0.15\}$.
191	For $K{=}4$, extreme regime: $\pi \in \{0.05, 0.10, 0.15, 0.25\}$; moderate regime: $\pi \in \{0.08, 0.12, 0.16, 0.20\}$.
192	
193	Expert labels are drawn as a simple random sample of size $n_{\text{expert}} \in \{50, 100, 250, 500, 1000, 2000\}$ from the full dataset, with true $Z$ observed for these observations.
194	
195	\paragraph{Semi-synthetic DGP (Section~\ref{sec:ec_hte_eval}).}
196	We sample $N = 5000$ tweets from the TweetEval sentiment corpus ($N_{\text{pool}} = 57{,}899$).
197	Subgroups are defined by crossing \texttt{has\_hashtag} $\times$ \texttt{text\_length\_bin} (short/medium/long), yielding $K = 4$ subgroups with empirical sizes: $S_0 \approx 38\%$, $S_1 \approx 38\%$, $S_2 \approx 12\%$, $S_3 \approx 12\%$.
198	Misclassification rates in the extreme regime are $\pi_{S_0} = 0.05$, $\pi_{S_1} = 0.10$, $\pi_{S_2} = 0.15$, $\pi_{S_3} = 0.25$, reflecting empirical evidence that hashtag-heavy text degrades LLM classifier accuracy.
199	The outcome DGP follows the same structure as the synthetic case, with CATE injected onto the real text-derived subgroup structure.
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3083edb-16f9-4619-b37e-7e0495d19a2a",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "7b123bc1-6ce5-421c-9078-85440d6b319f",
  "sourceToolAssistantUUID": "d3083edb-16f9-4619-b37e-7e0495d19a2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T20:29:06.666Z_

<details open><summary>🔧 Tool call — Read · `toolu_016Dizt9F6aLjQEQB14qettD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b123bc1-6ce5-421c-9078-85440d6b319f",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8e61HbLa3pa5TeeZWi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1bff995d-4d9e-44c7-8976-18929d724400",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011369Q3B4jvZzPBBxjZP17p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6228,
      "cache_read_input_tokens": 36647,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6228
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 36647,
          "cache_creation_input_tokens": 6228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6228,
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

_source line 36 · 2026-05-23T20:29:06.679Z_

<details><summary>↩ Tool result · `toolu_016Dizt9F6aLjQEQB14qettD`</summary>

```text
200	
201	\paragraph{PPCI DGPs (Appendix~\ref{sec:ppci}).}
202	Four DGPs isolate error types: (A) covariate error only ($\sigma_{\text{outcome}} = 0$), (B) outcome error only ($\sigma_{\text{outcome}} = 0.5$), (C) both errors ($\sigma_{\text{outcome}} = 0.5$), (D) no error ($\sigma_{\text{outcome}} = 0$).
203	Outcome-side error is additive Gaussian noise on $Y$.
204	
205	\paragraph{CausalForestDML hyperparameters.}
206	All CausalForest experiments use \texttt{econml.dml.CausalForestDML} with honest splitting, $n_{\text{estimators}} = 48$, $\texttt{min\_samples\_leaf} = 20$, \texttt{model\_y} = \texttt{LassoCV}(cv=3), and \texttt{model\_t} = \texttt{LogisticRegressionCV}.
207	These defaults were held constant across all configurations; no hyperparameter tuning was performed.
208	
209	\begin{figure*}[t]
210	\centering
211	\includegraphics[width=\textwidth]{figures/fig2_heatmap.pdf}
212	\caption{Bias amplification under global correction ($K{=}2$). (a) Low-error subgroup: correction always helps. (b) High-error subgroup: correction \emph{increases} bias when $\Delta\pi > 0.12$ (hatched), reaching 2.86$\times$.}
213	\label{fig:heatmap}
214	\end{figure*}
215	
216	\section{Extended Related Work}
217	\label{app:related}
218	
219	\paragraph{Measurement error details.}
220	\citet{fuller1987measurement} establish the foundational theory showing that naive regression with mismeasured covariates yields attenuated coefficient estimates.
221	\citet{carroll2006measurement} extend this to nonlinear models.
222	\citet{gustafson2003measurement} develops Bayesian treatments modeling measurement jointly with outcomes.
223	\citet{hu2008nonparametric} provide nonparametric identification using repeated measurements or instruments.
224	
225	\paragraph{Annotation model extensions.}
226	Beyond the foundational \citet{dawid1979maximum} model, \citet{passonneau2014benefits} incorporate item difficulty, \citet{hovy2013learning} learn annotator competence, and \citet{paun2018comparing} introduce hierarchical priors sharing information across annotators with varying expertise.
227	
228	\paragraph{PPI extensions and text-as-data methods.}
229	\citet{zrnic2024cross} extend PPI via cross-prediction; their active inference framework~\citep{zrnic2024active} achieves $>$80\% expert budget savings through adaptive allocation, complementary to our fixed-budget analysis.
230	\citet{grimmer2022text} provide methodological guidance for text-as-data pipelines.
231	\citet{audinet2025benchmarking} systematically benchmark DSL and PPI methods for LLM-based parameter estimation, finding that debiasing can increase MSE when prediction error is heterogeneous---a population-level analogue of the subgroup-conditional bias amplification we formalize in Theorem~\ref{thm:bias_identity}.
232	
233	\paragraph{Treatment vs.\ effect-modifier misclassification.}
234	\citet{imai2010causal} study treatment misclassification where errors change which arm a unit is assigned to, requiring instrumental variables or partial identification because the fundamental treated-vs-control contrast is corrupted.
235	Our problem preserves the treatment contrast ($T$ is observed correctly) but corrupts the heterogeneity structure ($\hat{Z} \neq Z$).
236	The ATE remains identified; only conditional effects are biased, which makes exact correction through confusion matrix inversion feasible.
237	
238	\paragraph{Econometrics of binary misclassification.}
239	\citet{bound2001measurement} survey measurement error in survey data, establishing that binary misclassification attenuates regression coefficients.
240	\citet{frazis2003estimating} derive exact bias formulas for OLS with a misclassified binary regressor, showing attenuation proportional to the misclassification rate---analogous to our Theorem~\ref{thm:bias_identity} but restricted to average effects without subgroup heterogeneity.
241	\citet{black2000racial} demonstrate that racial misclassification in administrative data can substantially bias estimates of racial disparities.
242	\citet{mahajan2006identification} and \citet{lewbel2007estimation} develop instrumental variable approaches to identify models with misclassified binary regressors, requiring exclusion restrictions unavailable when the mismeasured variable is an LLM annotation.
243	Our setting differs in three respects: (i) the mismeasured variable is an effect modifier indexing the CATE function, not a standard regressor; (ii) misclassification rates vary across subgroups, creating the $\delta_s \times \Delta\tau$ product amplification absent from homogeneous-error analyses; and (iii) expert labels provide a direct calibration sample, enabling confusion matrix estimation without instruments.
244	
245	\section{MCMC Convergence Diagnostics}
246	\label{app:mcmc}
247	
248	Table~\ref{tab:mcmc} reports convergence diagnostics for the hierarchical Bayesian confusion matrix estimator across all experimental configurations.
249	All runs use 4 chains with 4000 iterations (2000 warmup).
250	Main experiments (Table~\ref{tab:main_results}) use a Dirichlet prior centered on $\hat{C}_{\text{global}}$ with concentration $\alpha_0$ estimated via empirical Bayes (marginal likelihood).
251	Appendix robustness experiments use a fixed Dirichlet prior ($\alpha{=}3$); since fixed-$\alpha$ partial pooling is weakly dominated by the adaptive variant, these results are conservative.
252	This budget is sufficient for the $2{\times}2$ Dirichlet-Multinomial posterior; all runs achieve $\hat{R} < 1.0034$ and ESS $> 1618$, confirming convergence with substantial margin.
253	
254	\begin{table}[h]
255	\centering
256	\small
257	\begin{tabular}{lcc}
258	\toprule
259	Diagnostic & Threshold & Achieved \\
260	\midrule
261	$\hat{R}$ (max across all params) & $< 1.01$ & $< 1.0034$ \\
262	ESS (min across all params) & $> 845$ & $> 1618$ \\
263	Divergent transitions & $= 0$ & $0$ \\
264	Singularity guard triggers & --- & extreme/$n{=}50$ only \\
265	\bottomrule
266	\end{tabular}
267	\caption{MCMC convergence diagnostics for the hierarchical Bayesian estimator. All configurations satisfy convergence criteria with substantial margin.}
268	\label{tab:mcmc}
269	\end{table}
270	
271	\paragraph{Hyperprior sensitivity.}
272	Scaling the $\text{Gamma}(3, 1)$ hyperprior by factors of $0.5\times$ to $2\times$ produces $<$1\% RMSE variation for $K{=}2$ and $\sim$4--5\% for $K{=}4$.
273	Coverage remains invariant across the sensitivity range.
274	These results confirm that the hierarchical estimator is robust to prior specification within a reasonable range.
275	
276	\section{Diagnostic ROC Curves}
277	\label{app:roc}
278	
279	\begin{figure}[t]
280	\centering
281	\includegraphics[width=\columnwidth]{figures/fig4_roc.png}
282	\caption{ROC curves for the $\Delta\tau$-free diagnostic (Proposition~\ref{prop:debiasing_hurts}): $|\delta_s|/((1{-}2\bar\pi)\cdot\pi_s)>1$. (A)~Setting-level ROC (AUC $= 0.89$), compared with the $|\Delta\pi \times \Delta\tau|$ product (AUC $= 0.89$) and $\mathrm{CV}(\pi_s)$ (AUC $= 0.97$). (B)~Subgroup-level ROC: the $\Delta\pi$-only condition (AUC $= 0.86$) substantially outperforms the $|\Delta\pi \times \Delta\tau|$ product (AUC $= 0.73$). The $\Delta\tau$-free diagnostic depends only on estimable misclassification rates, breaking the circular dependency that would arise if CATE heterogeneity were required.}
283	\label{fig:roc}
284	\end{figure}
285	
286	\paragraph{Cost-asymmetric diagnostic thresholds.}
287	In practice, the cost of a false negative (failing to detect that global correction increases bias) exceeds the cost of a false positive (unnecessarily applying EC-HTE when global correction would suffice), because the former propagates systematic bias into CATE estimates while the latter only incurs additional estimation variance.
288	Practitioners in high-stakes settings (e.g., policy evaluation where CATE estimates inform resource allocation) should lower the diagnostic threshold to favor recall over precision, accepting more false positives to minimize the risk of undetected bias amplification.
289	
290	\section{Expert Budget Crossover Curves}
291	\label{app:budget}
292	\label{sec:budget}
293	
294	The crossover point at which EC-HTE achieves lower RMSE than global correction is $n_{\text{expert}} = 250$ for $K{=}2$/extreme and $n_{\text{expert}} = 1000$ for $K{=}4$/extreme (Figure~\ref{fig:budget}).
295	Under moderate heterogeneity ($K{=}2$), EC-HTE never achieves lower RMSE than global at any budget.
296	HB partial pooling improves over stratified MLE in 21 of 24 configurations, with the two estimators converging by $n_{\text{expert}} \geq 1000$.
297	
298	\begin{figure*}[t]
299	\centering
300	\includegraphics[width=\textwidth]{figures/fig3_budget.pdf}
301	\caption{RMSE vs.\ expert budget ($n_{\text{expert}}$) across four regime$\times K$ combinations. Dashed vertical lines mark crossover points where EC-HTE achieves lower RMSE than global correction: $n{=}250$ ($K{=}2$, extreme), $n{=}1000$ ($K{=}4$, extreme). Under moderate heterogeneity ($K{=}2$), global correction dominates at all budgets. Shaded bands show $\pm 1$ SD across subgroups within each configuration.}
302	\label{fig:budget}
303	\end{figure*}
304	
305	\subsection{Budget Sensitivity: HB vs.\ Stratified MLE}
306	\label{app:budget_sensitivity}
307	
308	Hierarchical Bayes (HB) partial pooling borrows strength across subgroups, which should matter most when per-subgroup expert labels are scarce.
309	We sweep $n_{\text{expert}} \in \{25, 50, 75, 100, 150, 250\}$ under extreme heterogeneity ($\Delta\tau{=}0.3$, 100 MC runs, $N{=}5{,}000$).
310	Table~\ref{tab:budget_sensitivity} reports aggregate RMSE for global correction, stratified MLE, and HB EC-HTE.
311	
312	\begin{table}[h]
313	\centering
314	\caption{RMSE across expert budgets under extreme heterogeneity.
315	HB crossover (first budget where HB $<$ MLE) occurs at approximately 10 expert labels per subgroup-cell:
316	$n_{\text{expert}}{=}50$ for $K{=}2$ and $n_{\text{expert}}{=}75$ for $K{=}4$.}
317	\label{tab:budget_sensitivity}
318	\small
319	\begin{tabular}{crrrrc}
320	\toprule
321	$K$ & $n_{\text{expert}}$ & Global & Strat.\ MLE & HB EC-HTE & HB vs.\ MLE \\
322	\midrule
323	2 & 25 & \textbf{0.101} & 0.256 & 0.269 & $+4.9\%$ \\
324	2 & 50 & \textbf{0.088} & 0.275 & 0.231 & $\mathbf{-16.1\%}$ \\
325	2 & 75 & 0.084 & 0.091 & \textbf{0.089} & $-1.9\%$ \\
326	2 & 100 & 0.083 & 0.085 & \textbf{0.084} & $-0.8\%$ \\
327	2 & 150 & 0.081 & 0.077 & \textbf{0.077} & $-0.4\%$ \\
328	2 & 250 & 0.080 & 0.075 & \textbf{0.074} & $-0.1\%$ \\
329	\midrule
330	4 & 25 & \textbf{0.129} & 0.401 & 0.612 & $+52.5\%$ \\
331	4 & 50 & \textbf{0.117} & 0.380 & 0.470 & $+23.8\%$ \\
332	4 & 75 & \textbf{0.112} & 0.221 & 0.211 & $\mathbf{-4.4\%}$ \\
333	4 & 100 & \textbf{0.112} & 0.215 & 0.212 & $-1.3\%$ \\
334	4 & 150 & \textbf{0.109} & 0.157 & 0.152 & $-3.6\%$ \\
335	4 & 250 & \textbf{0.108} & 0.127 & 0.126 & $-1.0\%$ \\
336	\bottomrule
337	\end{tabular}
338	\end{table}
339	
340	Three regimes emerge.
341	At very low budgets ($n_{\text{expert}} < 50$ for $K{=}2$, $< 75$ for $K{=}4$), per-subgroup counts are insufficient for reliable confusion matrix estimation; global pooling dominates because the variance cost of stratification overwhelms any bias reduction.
342	HB degrades substantially in this regime because the Gibbs posterior, while better regularized than MLE, still cannot overcome the fundamental sample-size constraint with $\sim$6--12 labels per subgroup.
343	At moderate budgets ($n_{\text{expert}} = 50$--$250$ for $K{=}2$, $75$--$250$ for $K{=}4$), HB partial pooling provides consistent RMSE improvement over stratified MLE ($-0.4\%$ to $-16.1\%$), with the largest gains near the crossover point.
344	At high budgets ($n_{\text{expert}} \geq 250$), both estimators converge as subgroup-level data becomes sufficient for reliable MLE; the HB advantage diminishes to $< 1\%$.
345	Coverage remains $\geq 0.88$ for both methods across all budget levels.
346	
347	\subsection{Scalability to $K{=}8$ Subgroups}
348	\label{app:k8_subgroups}
349	
350	We test EC-HTE at $K{=}8$ to identify the scalability boundary of hierarchical Bayesian partial pooling under fixed expert budget.
351	
352	\paragraph{Setup.}
353	$N{=}5{,}000$, $K{=}8$ (equal-weight subgroups), $n_{\text{expert}}{=}250$ (${\approx}31$ labels per subgroup), 100 MC replications.
354	Misclassification rates are uniformly spread: $\pi_s \in \{0.05, 0.09, 0.13, 0.18, 0.22, 0.26, 0.30, 0.35\}$.
355	Treatment effects depend on $Z$ (not subgroup): $\tau(Z{=}0){=}0$, $\tau(Z{=}1){=}0.3$.
356	
357	\begin{table}[h]
358	\centering
359	\caption{EC-HTE at $K{=}8$ ($n_{\text{expert}}{=}250$, ${\approx}31$ labels/subgroup, 100 MC).}
360	\label{tab:k8_subgroups}
361	\small
362	\begin{tabular}{lccc}
363	\toprule
364	Method & Coverage & RMSE & $|\text{Bias}|$ \\
365	\midrule
366	Oracle       & 0.944 & 0.113 & 0.090 \\
367	Global       & 0.951 & 0.168 & 0.135 \\
368	HB EC-HTE    & 0.956 & 0.340 & 0.183 \\
369	Strat MLE    & 0.953 & 0.638 & 0.219 \\
370	Naive        & 0.913 & 0.133 & 0.107 \\
371	\bottomrule
372	\end{tabular}
373	\end{table}
374	
375	All CM-aware methods achieve nominal coverage at $K{=}8$: HB EC-HTE 95.6\%, Strat MLE 95.3\%, Global 95.1\%.
376	HB partial pooling achieves a 47\% RMSE reduction over stratified MLE (0.340 vs.\ 0.638), confirming that hierarchical shrinkage provides substantial regularization.
377	However, HB RMSE (0.340) exceeds global correction (0.168), indicating that ${\approx}31$ expert labels per subgroup are insufficient for per-subgroup CM estimation to outweigh variance inflation.
378	
379	\paragraph{Per-subgroup breakdown.}
380	Table~\ref{tab:k8_per_subgroup} decomposes RMSE by subgroup.
381	
382	\begin{table}[h]
383	\centering
384	\caption{Per-subgroup RMSE at $K{=}8$. HB improvement over MLE is largest in high-$\pi$ subgroups but does not close the gap with Global.}
385	\label{tab:k8_per_subgroup}
386	\small
387	\begin{tabular}{cccccc}
388	\toprule
389	Subgroup & $\pi_s$ & HB RMSE & MLE RMSE & Global RMSE & HB Cov \\
390	\midrule
391	$s_0$ & 0.050 & 0.136 & 0.134 & \textbf{0.181} & 0.950 \\
392	$s_1$ & 0.093 & 0.133 & 0.132 & \textbf{0.154} & 0.970 \\
393	$s_2$ & 0.136 & 0.154 & 0.154 & 0.161 & 0.975 \\
394	$s_3$ & 0.179 & 0.178 & 0.182 & \textbf{0.159} & 0.945 \\
395	$s_4$ & 0.221 & 0.263 & 0.343 & \textbf{0.163} & 0.940 \\
396	$s_5$ & 0.264 & 0.421 & 0.711 & \textbf{0.164} & 0.965 \\
397	$s_6$ & 0.307 & 0.634 & 1.375 & \textbf{0.177} & 0.940 \\
398	$s_7$ & 0.350 & 0.432 & 0.809 & \textbf{0.183} & 0.960 \\
399	\bottomrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bff995d-4d9e-44c7-8976-18929d724400",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "1e04e8ce-3dff-46f7-986c-9bccc2db3e4c",
  "sourceToolAssistantUUID": "1bff995d-4d9e-44c7-8976-18929d724400",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-23T20:29:12.764Z_

Now let me look at a few more critical appendix sections and the latest dream report review for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e04e8ce-3dff-46f7-986c-9bccc2db3e4c",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8eNK4v3Wn9Rvtsxzx8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a98e6177-8d77-4f2e-a8d2-5922f7bf0939",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TqQQqLHqAdXAYsmh738HEB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5481,
      "cache_read_input_tokens": 42875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5481,
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

_source line 38 · 2026-05-23T20:29:14.819Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T3BUt4re7mpmhTZ1JXZUma`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 400,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a98e6177-8d77-4f2e-a8d2-5922f7bf0939",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8eNK4v3Wn9Rvtsxzx8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81e03ca5-17cf-4a30-b0e7-0aa6f6002cef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TqQQqLHqAdXAYsmh738HEB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5481,
      "cache_read_input_tokens": 42875,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5481
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 42875,
          "cache_creation_input_tokens": 5481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5481,
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

_source line 39 · 2026-05-23T20:29:14.824Z_

<details><summary>↩ Tool result · `toolu_01T3BUt4re7mpmhTZ1JXZUma`</summary>

```text
400	\end{tabular}
401	\end{table}
402	
403	RMSE degradation is concentrated in high-$\pi$ subgroups ($s_4$--$s_7$, $\pi \geq 0.22$), where confusion matrix inversion amplifies estimation noise ($r = 0.87$, $p = 0.005$ for correlation between $\pi_s$ and HB RMSE).
404	Low-error subgroups ($s_0$--$s_1$) benefit from stratification, with HB RMSE 14--25\% below global correction.
405	HB partial pooling reduces MLE RMSE by 24--54\% in the high-$\pi$ regime ($s_4$--$s_7$), confirming that hierarchical shrinkage provides meaningful regularization even when per-subgroup labels are scarce.
406	Coverage remains $\geq$0.94 across all subgroups for HB EC-HTE, indicating that variance inflation does not compromise inference validity.
407	Adaptive shrinkage---increasing the prior strength for high-$\pi$ subgroups where CM estimation is least reliable---is a natural extension that may close the RMSE gap with global correction at larger $K$.
408	
409	We explored adaptive shrinkage ($\alpha{=}10$ for high-$\pi$ subgroups vs.\ default $\alpha{=}3$), which reduces aggregate RMSE from 0.340 to 0.216 (35\% improvement) by attenuating estimation noise in high-$\pi$ subgroups.
410	However, RMSE remains 30\% above global correction (0.166), confirming that the bottleneck is per-subgroup sample size (${\sim}$31 expert labels) rather than the shrinkage method itself.
411	This establishes $K{=}8$ at $n_{\text{expert}}{=}250$ as a boundary condition: all correction methods provide valid inference (coverage $\geq$94\%), but per-subgroup stratification requires proportionally larger expert budgets---approximately $n_{\text{expert}} \geq 500$ (${\approx}60$ labels/subgroup)---to achieve RMSE parity with global correction.
412	
413	\section{Asymmetric Misclassification Extension}
414	\label{app:asymmetric}
415	
416	Assumption~(A2) imposes symmetric misclassification ($\text{FPR}_s = \text{FNR}_s = \pi_s$), which simplifies the bias decomposition but is not necessary for it.
417	Real LLM annotators typically exhibit asymmetric confusion patterns; we show here that the product structure generalizes.
418	
419	\paragraph{General bias formula.}
420	For asymmetric confusion matrices $C_s = \bigl(\begin{smallmatrix} 1{-}\text{FPR}_s & \text{FPR}_s \\ \text{FNR}_s & 1{-}\text{FNR}_s \end{smallmatrix}\bigr)$, define the mixing matrix $M_s$ via Bayesian inversion and the residual matrix $B_s = M_{\text{global}}^{-1} M_s - I$.
421	Since both $M_s$ and $M_{\text{global}}$ are row-stochastic, $B_s \mathbf{1} = \mathbf{0}$.
422	Decomposing $\boldsymbol{\tau} = \tau(0)\mathbf{1} + \Delta\tau \, \mathbf{e}_1$ gives:
423	\begin{equation}
424	\text{bias}(z, s) = \Delta\tau \cdot [B_s]_{z,1},
425	\end{equation}
426	where $[B_s]_{z,1}$ depends only on $\{\text{FPR}_k, \text{FNR}_k, w_k\}$, not on $\Delta\tau$.
427	Under~(A2), this reduces to $\delta_s \Delta\tau / (1 - 2\bar{\pi})$ (Theorem~\ref{thm:bias_identity}).
428	
429	\paragraph{Empirical validation.}
430	We test three asymmetric configurations ($K{=}2$, $n_{\text{expert}}{=}250$, 100 MC runs each): \emph{Cross} (FPR/FNR = 0.10/0.20 vs.\ 0.25/0.10), \emph{Co-directional} (0.05/0.15 vs.\ 0.20/0.30), and \emph{Extreme} (0.03/0.25 vs.\ 0.30/0.05).
431	Regressing analytic predictions on MC bias yields $R^2 = 0.991$ across all configurations, confirming the product structure under asymmetry.
432	Table~\ref{tab:asymmetric} reports correction performance averaged over subgroups, $z$-levels, and $\Delta\tau \in \{0.1, \ldots, 0.5\}$.
433	EC-HTE reduces $|\text{bias}|$ from 0.025 (global) to 0.006, a $4\times$ improvement, with lower RMSE (0.033 vs.\ 0.040) and substantially better coverage (0.90 vs.\ 0.78).
434	
435	\begin{table}[t]
436	\centering
437	\caption{Asymmetric misclassification results ($K{=}2$, $n_{\text{expert}}{=}250$, 100 MC runs). Values averaged over subgroups, $z$-levels, and $\Delta\tau$.}
438	\label{tab:asymmetric}
439	\small
440	\begin{tabular}{l ccc}
441	\toprule
442	Method & $|\text{Bias}| \downarrow$ & RMSE $\downarrow$ & Coverage $\uparrow$ \\
443	\midrule
444	Naive & 0.047 & 0.053 & 0.48 \\
445	Global & 0.025 & 0.040 & 0.78 \\
446	HB EC-HTE & \textbf{0.006} & \textbf{0.033} & \textbf{0.90} \\
447	\bottomrule
448	\end{tabular}
449	\end{table}
450	
451	\section{Supplementary Main Results}
452	\label{app:main_supp}
453	
454	\begin{table}[t]
455	\centering
456	\caption{Additional configurations from the main experiment. $|\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and 100 MC runs. $^\dagger$RMSE exceeds Global.}
457	\label{tab:main_supp}
458	\small
459	\begin{tabular}{ll ccc}
460	\toprule
461	Configuration & Method & $|\text{Bias}|$ & RMSE & Cov. \\
462	\midrule
463	\multirow{4}{*}{\shortstack[l]{Synthetic DIM\\$K{=}2$, moderate, $n{=}250$}}
464	 & Naive & 0.018 & 0.064 & 0.95 \\
465	 & Global & 0.009 & 0.074 & 0.96 \\
466	 & Strat.\ MLE & \textbf{0.005} & 0.075$^\dagger$ & 0.97 \\
467	 & HB EC-HTE & \textbf{0.005} & 0.075$^\dagger$ & 0.97 \\
468	\midrule
469	\multirow{4}{*}{\shortstack[l]{Semi-synthetic\\TweetEval, extreme, $n{=}250$}}
470	 & Naive & 0.027 & 0.103 & 0.93 \\
471	 & Global & \textbf{0.023} & 0.124 & 0.92 \\
472	 & Strat.\ MLE & 0.032 & 0.248$^\dagger$ & 0.91 \\
473	 & HB EC-HTE & 0.027 & 0.225$^\dagger$ & 0.91 \\
474	\bottomrule
475	\end{tabular}
476	\end{table}
477	
478	\section{PPCI Complementarity Results}
479	\label{app:ppci}
480	\label{sec:ppci}
481	
482	EC-HTE composes with PPCI~\cite{sui2026ppci} for settings where both covariate misclassification and outcome model error are present: EC-HTE+PPCI reduces $|\text{bias}|$ from 0.179 to 0.007 ($z{=}0$, DGP~C), and the corrected pseudo-outcomes are compatible with other CATE estimators (R-learner bias reduction: 89\%; Appendix~\ref{app:rlearner}).
483	
484	\begin{table*}[t]
485	\centering
486	\caption{PPCI complementarity experiment ($K{=}2$, extreme, $n_{\text{expert}}{=}250$). DGP~A: covariate error only; B: outcome error only ($\sigma{=}0.5$); C: both errors; D: no error. Values are $|\text{bias}|$ and RMSE averaged over two subgroups. $^\star$EC-HTE+PPCI achieves near-zero bias when both error types are present.}
487	\label{tab:ppci}
488	\small
489	\begin{tabular}{ll cccc}
490	\toprule
491	DGP & Method & $|\text{Bias}|_{z=0}$ & $|\text{Bias}|_{z=1}$ & RMSE$_{z=0}$ & RMSE$_{z=1}$ \\
492	\midrule
493	\multirow{5}{*}{A: Covariate}
494	 & Naive & 0.053 & 0.063 & 0.087 & 0.093 \\
495	 & Global & 0.063 & 0.055 & 0.101 & 0.102 \\
496	 & EC-HTE & 0.017 & \textbf{0.013} & 0.097 & 0.108 \\
497	 & PPCI & \textbf{0.015} & 0.020 & 0.162 & 0.168 \\
498	 & EC-HTE+PPCI & 0.017 & \textbf{0.013} & 0.097 & 0.108 \\
499	\midrule
500	\multirow{5}{*}{B: Outcome}
501	 & Naive & 0.189 & 0.197 & 0.206 & 0.212 \\
502	 & Global & 0.185 & 0.208 & 0.204 & 0.228 \\
503	 & EC-HTE & 0.181 & 0.215 & 0.202 & 0.237 \\
504	 & PPCI & 0.015 & \textbf{0.020} & 0.171 & 0.176 \\
505	 & EC-HTE+PPCI & \textbf{0.012} & 0.023 & 0.171 & 0.186 \\
506	\midrule
507	\multirow{5}{*}{C: Both}
508	 & Naive & 0.251 & 0.135 & 0.267 & 0.155 \\
509	 & Global & 0.182 & 0.209 & 0.233 & 0.235 \\
510	 & EC-HTE & 0.179 & 0.216 & 0.224 & 0.262 \\
511	 & PPCI & 0.017 & 0.007 & 0.241 & 0.232 \\
512	 & EC-HTE+PPCI$^\star$ & \textbf{0.007} & \textbf{0.008} & 0.209 & 0.223 \\
513	\midrule
514	\multirow{5}{*}{D: None}
515	 & Naive & \textbf{0.007} & 0.003 & 0.060 & 0.065 \\
516	 & Global & 0.010 & \textbf{0.002} & 0.061 & 0.071 \\
517	 & EC-HTE & 0.013 & 0.007 & 0.062 & 0.079 \\
518	 & PPCI & \textbf{0.007} & \textbf{0.003} & 0.060 & 0.065 \\
519	 & EC-HTE+PPCI & 0.013 & 0.007 & 0.062 & 0.079 \\
520	\bottomrule
521	\end{tabular}
522	\end{table*}
523	
524	The complementarity of EC-HTE and PPCI follows from the distinct error sources they correct: EC-HTE addresses misclassification in the effect modifier $Z$ (covariate space), while PPCI corrects specification error in the outcome model $f(X)$ (prediction space).
525	Since covariate misclassification and outcome model error are algebraically independent in the potential outcomes framework, their corrections compose without interference---confirmed by the 4-DGP orthogonal design (Table~\ref{tab:ppci}), where DGP~C (both errors present) yields the largest bias reduction from the combined approach.
526	Under covariate error only, PPCI adds nothing; under no error, all methods perform equivalently.
527	
528	\section{Real-Data Case Study: Hate Speech Detection}
529	\label{app:hatespeech}
530	
531	We apply EC-HTE to the UC Berkeley Measuring Hate Speech corpus~\cite{kennedy2020constructing}, annotating 2{,}496 comments for dehumanization using GPT-4.1.
532	Four text-feature subgroups are defined by crossing platform (Reddit/Gab vs.\ Twitter/YouTube) and text length (above/below median), yielding balanced groups ($n \approx 624$ each).
533	
534	\paragraph{Positive finding: real-world heterogeneity.}
535	Per-subgroup misclassification rates range from 0.266 to 0.383, confirming heterogeneity ($\Delta\pi = 0.117$) in a real annotation setting.
536	At the error-type level, FPR ranges from 8.5\% to 21.3\% across text-feature subgroups, demonstrating that subgroup-varying misclassification is not an artifact of synthetic design but arises naturally in real NLP annotation tasks.
537	
538	\paragraph{Boundary condition: statistical power at extreme FNR.}
539	Correction results are inconclusive: all corrected confidence intervals contain zero, and point estimate differences between methods are not statistically significant.
540	The high baseline FNR (53.3\%) amplifies variance through matrix inversion (variance amplification factor up to 15.7$\times$), rendering the comparison underpowered.
541	When $P(\hat{Z}{=}1 \mid Z{=}1) \approx 0.5$, the confusion matrix approaches singularity, and inversion amplifies estimation noise regardless of stratification strategy.
542	This complements the expert budget threshold identified in Appendix~\ref{sec:budget}: EC-HTE requires \emph{both} sufficient expert labels \emph{and} sufficient baseline classifier quality.
543	
544	\paragraph{Diagnostic connection.}
545	The diagnostic criterion ($\Delta\pi \times \Delta\tau$, Section~\ref{sec:diagnostic}) identifies when correction is worthwhile under moderate baseline accuracy.
546	This case study illustrates that even when $\Delta\pi$ is large, extreme baseline error renders correction underpowered rather than beneficial.
547	A practical prerequisite is that the per-subgroup confusion matrix condition number $\kappa(\hat{C}_s)$ remain moderate; when $\kappa > 50$, as observed here, practitioners should prioritize improving annotation quality before applying any matrix-inversion-based correction.
548	
549	\section{Cross-Model Consistency}
550	\label{app:multilm}
551	
552	We evaluate whether misclassification heterogeneity is model-specific by annotating 500 TweetEval sentiment tweets with six OpenAI models spanning three generations.
553	Six text-feature subgroups are defined by crossing hashtag presence and text length.
554	Spearman rank correlations of per-subgroup error rates across all six subgroups range from $\rho = 0.82$ to $1.00$, indicating that the subgroup error structure is consistent across architectures.
555	Two subgroups with $n \leq 6$ exhibit zero misclassification across all models; excluding these yields four-point correlations that are directionally consistent but underpowered.%
556	\footnote{The filtered $\Delta\pi$ values in Table~\ref{tab:multilm} serve as a robustness check independent of rank-order testing: all six models exceed $\Delta\pi > 0.05$ on the four retained subgroups.}
557	
558	\begin{table}[t]
559	\centering
560	\caption{Effective misclassification heterogeneity ($\Delta\pi$) across six OpenAI models on TweetEval sentiment (500 tweets, filtered to 4 subgroups with $n \geq 10$).}
561	\label{tab:multilm}
562	\small
563	\begin{tabular}{lcc}
564	\toprule
565	Model & Effective $\Delta\pi$ & $> 0.05$? \\
566	\midrule
567	GPT-3.5-Turbo & 0.198 & \checkmark \\
568	GPT-4-Turbo & 0.149 & \checkmark \\
569	GPT-4o-mini & 0.136 & \checkmark \\
570	GPT-5.4 & 0.114 & \checkmark \\
571	GPT-4.1 & 0.098 & \checkmark \\
572	GPT-4o & 0.080 & \checkmark \\
573	\bottomrule
574	\end{tabular}
575	\end{table}
576	
577	All six models exhibit effective $\Delta\pi > 0.05$ on the four retained subgroups (Table~\ref{tab:multilm}), and 5 of 6 share the same worst subgroup (\texttt{True\_medium}: tweets with hashtags and medium text length).
578	Newer models reduce absolute error rates but do not eliminate subgroup heterogeneity: GPT-5.4 achieves $\Delta\pi = 0.114$ compared to GPT-3.5-Turbo's $0.198$.
579	These results were obtained with a single API provider; open-source model validation appears in Appendix~\ref{app:multilm_opensource}.
580	
581	\section{Open-Source Multi-LLM Validation}
582	\label{app:multilm_opensource}
583	
584	We evaluate four open-source LLMs (7B--9B parameter range) on 490 TweetEval sentiment tweets with $K{=}4$ subgroups defined by crossing hashtag presence and text length.
585	Table~\ref{tab:multilm_cm} reports the confusion matrix heterogeneity profile.
586	All four models exhibit $\Delta\pi > 0.05$, confirming that subgroup-heterogeneous misclassification is not specific to proprietary APIs.
587	Subgroup error rankings are consistent across architectures: \texttt{True\_short} (short tweets with hashtags) has the lowest $\pi_s$ in 3 of 4 models, while \texttt{False\_medium} (medium tweets without hashtags) has the highest.
588	
589	\begin{table}[t]
590	\centering
591	\caption{Confusion matrix heterogeneity across four open-source LLMs ($K{=}4$, $N{=}490$ TweetEval tweets). $\Delta\pi$: max--min per-subgroup misclassification rate. Prop2: number of subgroups where the $\Delta\tau$-free diagnostic (Proposition~\ref{prop:debiasing_hurts}) triggers.}
592	\label{tab:multilm_cm}
593	\small
594	\begin{tabular}{lcccl}
595	\toprule
596	Model & Acc.\ & $\Delta\pi$ & Prop2 & Strongest \\
597	\midrule
598	Llama-3.1-8B & 0.755 & 0.141 & 1/4 & True\_short \\
599	Qwen-2.5-7B & 0.798 & 0.165 & 1/4 & True\_short \\
600	Gemma-2-9B & 0.763 & 0.125 & 4/4 & True\_medium \\
601	Mistral-7B & 0.802 & 0.134 & 0/4 & --- \\
602	\bottomrule
603	\end{tabular}
604	\end{table}
605	
606	\paragraph{Semi-synthetic budget sweep.}
607	We run the full EC-HTE pipeline with $K{=}2$ subgroups and $\Delta\tau{=}0.3$, using each model's empirical confusion matrices.
608	Table~\ref{tab:multilm_budget} reports coverage and RMSE crossover points.
609	EC-HTE restores near-nominal coverage from 0.714 (naive average) to 0.939 ($+$22.5 percentage points) at $n_{\text{expert}}{=}1{,}000$, consistent across all four models.
610	Global correction achieves comparable or lower RMSE than HB at all budgets under these moderate $\Delta\pi$ values, and the $K{=}4$ RMSE crossover never occurs---confirming the budget guidelines in Appendix~\ref{sec:budget}.
611	
612	\begin{table}[t]
613	\centering
614	\caption{Semi-synthetic budget sweep ($K{=}2$, $\Delta\tau{=}0.3$, 50 MC runs; see Appendix~\ref{app:mcse} for MC tier justification). Coverage at selected expert budgets; RMSE crossover denotes the minimum expert budget at which HB EC-HTE achieves lower RMSE than the naive (uncorrected) estimator.}
615	\label{tab:multilm_budget}
616	\small
617	\begin{tabular}{lcccc}
618	\toprule
619	Model & $\Delta\pi_{K{=}2}$ & Naive Cov.\ & HB Cov.\ ($n{=}1000$) & Crossover \\
620	\midrule
621	Llama-3.1-8B & 0.051 & 0.675 & 0.940 & $n{=}1000$ \\
622	Qwen-2.5-7B & 0.080 & 0.715 & 0.925 & $n{=}1000$ \\
623	Gemma-2-9B & 0.100 & 0.705 & 0.945 & $n{=}1000$ \\
624	Mistral-7B & 0.070 & 0.760 & 0.945 & $n{=}1000$ \\
625	\midrule
626	\textit{Average} & --- & \textit{0.714} & \textit{0.939} & --- \\
627	\bottomrule
628	\end{tabular}
629	\end{table}
630	
631	\paragraph{Gemma boundary case.}
632	Gemma-2-9B triggers the Proposition~\ref{prop:debiasing_hurts} diagnostic in all four $K{=}4$ subgroups due to extreme FPR--FNR asymmetry (\texttt{False\_medium} FNR $= 0.437$).
633	At small budgets ($K{=}4$, $n{=}100$), EC-HTE RMSE reaches 1.229 ($3.1\times$ naive), illustrating the budget guideline from Appendix~\ref{sec:budget}: when per-subgroup cell counts fall below 25, the variance cost of stratified correction dominates.
634	At $n \geq 500$, EC-HTE coverage recovers to $>$0.90, consistent with the synthetic experiments.
635	
636	\paragraph{Heterogeneous-$\tau$ DGP.}
637	To assess whether the constant-$\tau$ DGP understates EC-HTE's advantage, we run a supplementary experiment using Llama's empirical confusion matrices with heterogeneous treatment effects across subgroups ($\Delta\tau \in [0.1, 0.6]$, $K{=}2$, 50 MC runs).
638	EC-HTE achieves lower $|\text{bias}|$ than global correction at all budgets ($n{=}500$: 0.010 vs.\ 0.031, a 68\% reduction).
639	In the high-$\Delta\tau$ subgroup (\texttt{True\_short}, $\Delta\tau{=}0.6$), EC-HTE also achieves lower RMSE ($n{=}1{,}000$: 0.212 vs.\ 0.258, 18\% improvement), confirming that the RMSE advantage concentrates in subgroups where correction is most needed.
640	Aggregate RMSE remains comparable to global correction because low-$\Delta\tau$ subgroups incur stratification variance without commensurate bias reduction, consistent with the budget guidelines in Appendix~\ref{sec:budget}.
641	
642	\section{Robustness to Subgroup Misspecification}
643	\label{app:robustness}
644	
645	EC-HTE requires pre-defined subgroup labels, which may be noisy in practice.
646	We test robustness by randomly flipping each observation's subgroup assignment with probability $p_{\text{flip}} \in \{0, 0.10, 0.25, 0.50\}$, across $K \in \{2, 4\}$ (extreme regime, $n_{\text{expert}} = 500$, $\Delta\tau = 0.3$, 100 MC runs).
647	
648	\begin{table}[t]
649	\centering
650	\caption{95\% CI coverage under subgroup misspecification noise. EC-HTE maintains near-nominal coverage across all noise levels.}
651	\label{tab:robustness}
652	\small
653	\begin{tabular}{lcccc}
654	\toprule
655	& \multicolumn{4}{c}{$p_{\text{flip}}$} \\
656	\cmidrule(lr){2-5}
657	Method & 0.00 & 0.10 & 0.25 & 0.50 \\
658	\midrule
659	\multicolumn{5}{l}{\textit{$K{=}2$, extreme}} \\
660	\quad Naive & 0.875 & 0.877 & 0.890 & 0.897 \\
661	\quad Global & 0.925 & 0.935 & 0.932 & 0.945 \\
662	\quad HB EC-HTE & 0.958 & 0.948 & 0.950 & 0.945 \\
663	\midrule
664	\multicolumn{5}{l}{\textit{$K{=}4$, extreme}} \\
665	\quad Naive & 0.904 & 0.916 & 0.909 & 0.919 \\
666	\quad Global & 0.930 & 0.953 & 0.948 & 0.944 \\
667	\quad HB EC-HTE & 0.956 & 0.958 & 0.960 & 0.946 \\
668	\bottomrule
669	\end{tabular}
670	\end{table}
671	
672	EC-HTE maintains coverage $\geq 0.945$ across all configurations (Table~\ref{tab:robustness}), while the naive estimator is systematically below nominal (0.875--0.919).
673	At $p_{\text{flip}} = 0.50$, subgroup structure is effectively destroyed; EC-HTE converges to global correction (coverage and RMSE within 0.1\%), confirming that hierarchical Bayesian shrinkage provides a built-in safety mechanism.
674	For $K{=}4$ at $p_{\text{flip}} = 0.50$, a small residual RMSE gap persists ($p < 0.01$), reflecting the variance cost of estimating four confusion matrices even when they carry no signal.
675	
676	\section{Monte Carlo Standard Errors}
677	\label{app:mcse}
678	
679	All main-text and most appendix experiments use 100 independent Monte Carlo replications per configuration; computationally intensive analyses (R-learner, multiplicative DGP, budget sweeps) use 50, and bootstrap experiments use 20 due to the $B{\times}$CF cost per seed.
680	The median RMSE variation between 50-seed and 100-seed estimates is below 3.2\%, confirming that 50-run results are stable.
681	We report Monte Carlo standard errors to assess whether observed differences between methods are statistically reliable.
682	For exp-001 (synthetic DGP, no per-seed pairing across methods), we use conservative two-sample $z$-tests on the 100-run means.
683	For exp-003 (semi-synthetic TweetEval, shared seeds across methods), we use paired $t$-tests, which are more powerful because they control for seed-level variation.
684	
685	Table~\ref{tab:mcse} reports paired comparisons for representative configurations.
686	Of 1{,}020 total pairwise comparisons across all configurations, 742 (72.7\%) are statistically significant at $\alpha = 0.05$.
687	
688	\begin{table}[t]
689	\centering
690	\caption{Paired comparisons for representative configurations. $\Delta$ = method A $-$ method B (negative favors A for $|\text{bias}|$). Two-sample $z$-tests for synthetic (exp-001); paired $t$-tests for semi-synthetic (exp-003). Bold $p$-values indicate significance at $\alpha = 0.05$.}
691	\label{tab:mcse}
692	\small
693	\begin{tabular}{llrr}
694	\toprule
695	Configuration & Comparison & $\Delta$ & $p$ \\
696	\midrule
697	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Global ($|\text{bias}|$)}} \\
698	\quad $K{=}2$/ext/$n{=}500$ & & $-0.046$ & $\mathbf{<0.001}$ \\
699	\quad $K{=}4$/ext/$n{=}500$ & & $-0.078$ & $\mathbf{<0.001}$ \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81e03ca5-17cf-4a30-b0e7-0aa6f6002cef",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "5506509e-f34a-4b69-b791-1f5536cd908a",
  "sourceToolAssistantUUID": "81e03ca5-17cf-4a30-b0e7-0aa6f6002cef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-23T20:29:26.193Z_

I now have sufficient material to write a thorough R1 review. Let me also check the most recent dream report for additional context on the paper's current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5506509e-f34a-4b69-b791-1f5536cd908a",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8eyJVZUmgrvjELSXst",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24765766-ba9f-4e0e-9a83-c9cec381516a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jJHZAEeLEUi67ei1JT3Ao",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8294,
      "cache_read_input_tokens": 48356,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8294,
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

_source line 41 · 2026-05-23T20:29:28.272Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NNc6pLoucguniYBgb5HCa4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 700,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24765766-ba9f-4e0e-9a83-c9cec381516a",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8eyJVZUmgrvjELSXst",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dffa8191-0725-4296-b989-f1b88912ffd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jJHZAEeLEUi67ei1JT3Ao",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8294,
      "cache_read_input_tokens": 48356,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8294
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 48356,
          "cache_creation_input_tokens": 8294,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8294,
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

_source line 42 · 2026-05-23T20:29:28.277Z_

<details><summary>↩ Tool result · `toolu_01NNc6pLoucguniYBgb5HCa4`</summary>

```text
700	\quad $K{=}4$/mod/$n{=}250$ & & $-0.017$ & $0.288$ \\
701	\quad TweetEval/ext/$n{=}250$ & & $+0.001$ & $0.395$ \\
702	\midrule
703	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Global (RMSE)}} \\
704	\quad $K{=}2$/ext/$n{=}500$ & & $+0.015$ & $0.179$ \\
705	\quad $K{=}4$/ext/$n{=}500$ & & $+0.048$ & $\mathbf{0.011}$ \\
706	\midrule
707	\multicolumn{4}{l}{\textit{HB EC-HTE vs.\ Naive ($|\text{bias}|$)}} \\
708	\quad $K{=}2$/ext/$n{=}500$ & & $-0.089$ & $\mathbf{<0.001}$ \\
709	\quad $K{=}4$/ext/$n{=}500$ & & $-0.113$ & $\mathbf{<0.001}$ \\
710	\quad $K{=}4$/mod/$n{=}250$ & & $-0.031$ & $\mathbf{0.038}$ \\
711	\quad TweetEval/ext/$n{=}250$ & & $+0.005$ & $\mathbf{0.030}$ \\
712	\bottomrule
713	\end{tabular}
714	\end{table}
715	
716	Under extreme heterogeneity, HB EC-HTE's bias advantage over global correction is highly significant ($p < 0.001$ for both $K{=}2$ and $K{=}4$).
717	The RMSE penalty of stratification is not significant at $K{=}2$ ($p = 0.179$) but reaches significance at $K{=}4$ ($p = 0.011$), consistent with the higher variance cost of estimating four confusion matrices.
718	Under moderate heterogeneity ($K{=}4$, $n{=}250$), the bias difference between HB and global is not significant ($p = 0.288$), confirming that EC-HTE's advantage requires sufficient error heterogeneity.
719	In the semi-synthetic TweetEval experiment, HB EC-HTE does not significantly improve over global ($p = 0.395$), consistent with moderate $\Delta\pi$ and unbalanced subgroup sizes.
720	The HB vs.\ naive comparison in TweetEval is significant ($p = 0.030$) but favors naive, reflecting the variance cost of stratification when bias reduction is marginal.
721	
722	\section{Semi-Real Confusion Matrix Validation}
723	\label{app:semireal}
724	
725	We test EC-HTE with empirical asymmetric confusion matrices from the GPT-4.1 TweetEval pilot.
726	Four text-feature subgroups ($K{=}4$) retain the real per-subgroup FPR and FNR from pilot annotations (Table~\ref{tab:semireal_cm}); CATE heterogeneity is injected synthetically ($\tau(z{=}0,s) = 0.3 + 0.1s$, $\tau(z{=}1,s) = 0.8 - 0.15s$).
727	$N{=}5{,}000$, $P(Z{=}1){=}0.18$, 100 MC seeds per $n_{\text{expert}}$ level.
728	
729	\begin{table}[t]
730	\centering
731	\caption{Empirical confusion matrices from GPT-4.1 TweetEval pilot.
732	S0 exhibits FNR $= 0.526$, approaching chance-level classification.}
733	\label{tab:semireal_cm}
734	\small
735	\begin{tabular}{lcccc}
736	\toprule
737	Subgroup & Weight & FPR & FNR & $\kappa(\hat{C}_s)$ \\
738	\midrule
739	S0 & 0.38 & 0.054 & 0.526 & high \\
740	S1 & 0.22 & 0.101 & 0.300 & moderate \\
741	S2 & 0.14 & 0.143 & 0.308 & moderate \\
742	S3 & 0.25 & 0.194 & 0.222 & low \\
743	\bottomrule
744	\end{tabular}
745	\end{table}
746	
747	\begin{table}[t]
748	\centering
749	\caption{Semi-real confusion matrix results. RMSE and coverage averaged over subgroups and $z$-levels (100 MC runs). HB EC-HTE underperforms global at all budgets; S0's near-chance FNR drives the failure.}
750	\label{tab:semireal}
751	\small
752	\begin{tabular}{llcc}
753	\toprule
754	$n_{\text{expert}}$ & Method & RMSE $\downarrow$ & Coverage $\uparrow$ \\
755	\midrule
756	\multirow{4}{*}{100}
757	 & Oracle & 0.101 & 0.957 \\
758	 & Naive & 0.123 & 0.879 \\
759	 & Global & 0.263 & 0.885 \\
760	 & HB EC-HTE & 0.784 & 0.744 \\
761	\midrule
762	\multirow{4}{*}{250}
763	 & Oracle & 0.101 & 0.957 \\
764	 & Naive & 0.123 & 0.879 \\
765	 & Global & 0.232 & 0.909 \\
766	 & HB EC-HTE & 0.411 & 0.834 \\
767	\midrule
768	\multirow{4}{*}{500}
769	 & Oracle & 0.101 & 0.957 \\
770	 & Naive & 0.123 & 0.879 \\
771	 & Global & 0.196 & 0.922 \\
772	 & HB EC-HTE & 0.260 & 0.890 \\
773	\bottomrule
774	\end{tabular}
775	\end{table}
776	
777	HB EC-HTE produces higher RMSE and lower coverage than global correction at all expert budgets (Table~\ref{tab:semireal}).
778	The root cause is S0's FNR $= 0.526$: when a confusion matrix row approaches a uniform distribution ($P(\hat{Z}{=}1 \mid Z{=}1) \approx 0.5$), inversion amplifies estimation noise regardless of the expert budget.
779	This converges with the hate speech case study (Appendix~\ref{app:hatespeech}, FNR $= 53.3$\%) and confirms that EC-HTE requires \emph{both} sufficient expert labels \emph{and} sufficient baseline classifier quality per subgroup.
780	The singularity guard ($\kappa > 100$, Section~\ref{sec:method}) mitigates catastrophic failure by falling back to global correction for near-degenerate subgroups, but does not recover the bias reduction that motivates stratification.
781	For a $2 \times 2$ symmetric confusion matrix, $\kappa = 1/|1-2\pi|$; $\kappa > 100$ corresponds to $\pi \in (0.495, 0.505)$, so the guard triggers only when the classifier performs within $0.5\%$ of random guessing.
782	At $n_{\text{expert}} = 500$, HB EC-HTE narrows the gap (RMSE 0.260 vs.\ 0.196) as confusion matrix estimates stabilize for the three well-classified subgroups, but the S0 bottleneck persists.
783	
784	A second semi-real experiment using GPT-3.5-Turbo confusion matrices (worst-subgroup FPR $= 0.39$, FNR $= 0.21$) yields similar results: HB RMSE exceeds global by 1.3--3.5$\times$ at all budgets.
785	Here the failure stems from high false-positive rates compounded by class imbalance ($P(Z{=}1) = 0.18$), which leaves insufficient expert observations in the positive class for reliable per-subgroup confusion matrix estimation.
786	Together, these experiments identify three applicability conditions for EC-HTE: (1)~sufficient effective expert budget ($n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$), (2)~no near-chance subgroup error rate ($\max(\text{FPR}_s, \text{FNR}_s) < 0.5$), and (3)~adequate class balance in the effect modifier.
787	
788	\paragraph{Diagnostic rule.}
789	A logistic regression over all 368 semi-real experiment--budget cells (dependent variable: HB EC-HTE $<$ Global RMSE) identifies two sufficient statistics: the worst-subgroup confusion matrix condition number $\kappa(\hat{M}_s) \leq 1.25$ and the effective minority-class expert count $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$.
790	When both conditions hold, HB outperforms global in 93.3\% of cells; when either is violated, global is preferred in 94.7\% of cells.
791	Both exp-015 ($\kappa = 2.38$, effective $n = 2.5$) and exp-016 ($\kappa = 1.55$, effective $n = 2.5$) violate both conditions, and the diagnostic correctly predicts 100\% of their failure cells.
792	Subgroup-average metrics can mask cell-level heterogeneity: in exp-015, HB EC-HTE substantially reduces bias for the three well-classified subgroups (S1--S3) but amplifies variance in the near-degenerate subgroup (S0, FNR $= 0.526$), and the S0 penalty dominates the aggregate RMSE.
793	
794	\begin{figure}[t]
795	\centering
796	\includegraphics[width=\columnwidth]{figures/applicability_frontier.pdf}
797	\caption{Applicability frontier of EC-HTE. Green region: EC-HTE reduces bias vs.\ global correction. Yellow: comparable performance. Red: EC-HTE underperforms. Dashed lines mark the expert budget threshold ($n_{\text{expert}}/K = 25$) and classifier quality threshold (worst-subgroup error rate $= 0.5$). Red diamonds show semi-real experiments with actual GPT-4.1 and GPT-3.5-Turbo confusion matrices.}
798	\label{fig:applicability}
799	\end{figure}
800	
801	\section{Robustness: Estimator Choice and Treatment Effect Specification}
802	\label{app:rlearner}
803	
804	We verify that EC-HTE's corrected pseudo-outcomes are compatible with downstream estimators beyond CausalForest by replacing it with the R-learner~\citep{nie2021quasi}.
805	The experiment uses $K{=}2$, extreme heterogeneity, $n_{\text{expert}} = 500$, and 50 MC seeds; the R-learner uses 5-fold cross-fitting with gradient-boosted trees as the base learner.
806	
807	\begin{table}[t]
808	\centering
809	\caption{R-learner vs.\ CausalForest with EC-HTE correction ($K{=}2$, extreme, $n{=}500$). $|\text{Bias}|$ and RMSE averaged over subgroups, $z$-levels, and seeds.}
810	\label{tab:rlearner}
811	\small
812	\begin{tabular}{llccc}
813	\toprule
814	Estimator & Correction & $|\text{Bias}|$ & RMSE & Cov. \\
815	\midrule
816	\multirow{4}{*}{R-learner}
817	 & Oracle & 0.006 & 0.056 & 0.94 \\
818	 & Naive & 0.121 & 0.139 & 0.47 \\
819	 & Global & 0.098 & 0.123 & 0.72 \\
820	 & EC-HTE & \textbf{0.013} & 0.080 & 0.92 \\
821	\midrule
822	\multirow{2}{*}{CausalForest}
823	 & Naive & 0.058 & 0.090 & 0.82 \\
824	 & EC-HTE & \textbf{0.010} & 0.093 & 0.95 \\
825	\bottomrule
826	\end{tabular}
827	\end{table}
828	
829	EC-HTE reduces R-learner $|\text{bias}|$ by 89\% (0.121 $\to$ 0.013) and restores coverage from 0.47 to 0.92 (Table~\ref{tab:rlearner}).
830	The bias reduction and coverage gains are comparable to those achieved with CausalForest, confirming that EC-HTE is compatible with a range of HTE estimators.
831	
832	\paragraph{Multiplicative treatment effects.}
833	We further test robustness to the functional form of treatment effects by replacing the additive DGP with a multiplicative specification: $Y(1) = Y(0) \times \exp(\tau(Z))$, using $K{=}2$, extreme heterogeneity, $n_{\text{expert}} = 500$, and 50 MC seeds.
834	
835	\begin{table}[t]
836	\centering
837	\caption{Multiplicative DGP results ($K{=}2$, extreme, $n{=}500$, 50 seeds). EC-HTE achieves comparable bias reduction and nominal coverage under non-additive treatment effects.}
838	\label{tab:multiplicative}
839	\small
840	\begin{tabular}{lccc}
841	\toprule
842	Method & $|\text{Bias}|$ & RMSE & Cov. \\
843	\midrule
844	Oracle & 0.003 & 0.038 & 0.96 \\
845	Naive & 0.135 & 0.142 & 0.44 \\
846	Global & 0.110 & 0.124 & 0.54 \\
847	EC-HTE & \textbf{0.054} & 0.068 & 0.955 \\
848	\bottomrule
849	\end{tabular}
850	\end{table}
851	
852	EC-HTE reduces RMSE by 52\% relative to naive (0.068 vs.\ 0.142) and restores coverage to the nominal level (0.955; Table~\ref{tab:multiplicative}).
853	EC-HTE's bias correction operates at the confusion matrix level, independent of the downstream CATE estimator and functional form of treatment effects.
854	
855	\section{Robustness to Class Imbalance}
856	\label{app:classimbalance}
857	
858	Assumption (A3) requires $P(Z{=}1) = 0.5$, but real-world effect modifiers are often imbalanced.
859	We sweep $P(Z{=}1) \in \{0.1, 0.2, 0.3, 0.4, 0.5\}$ with $K \in \{2,4\}$, extreme misclassification heterogeneity, $n_{\text{expert}}{=}250$, and 100 MC seeds (Table~\ref{tab:pz1_sweep}).
860	
861	\begin{table}[t]
862	\centering
863	\caption{Robustness to class imbalance ($n_{\text{expert}}{=}250$, extreme heterogeneity). R$^2$: Theorem~\ref{thm:bias_identity} fit. Ratio: HB/Global RMSE ($<1$ = HB wins). Cov.: HB EC-HTE 95\% CI coverage.}
864	\label{tab:pz1_sweep}
865	\small
866	\begin{tabular}{cc ccc}
867	\toprule
868	$P(Z{=}1)$ & $K$ & R$^2$ & Ratio & Cov. \\
869	\midrule
870	0.1 & 2 & 0.998 & 0.92 & 0.94 \\
871	0.2 & 2 & 0.989 & 0.76 & 0.94 \\
872	0.3 & 2 & 0.994 & 0.78 & 0.94 \\
873	0.4 & 2 & 0.995 & 0.87 & 0.94 \\
874	0.5 & 2 & 0.995 & 0.86 & 0.93 \\
875	\midrule
876	0.1 & 4 & 0.984 & 1.54 & 0.92 \\
877	0.2 & 4 & 0.976 & 1.68 & 0.93 \\
878	0.3 & 4 & 0.985 & 1.12 & 0.92 \\
879	0.4 & 4 & 0.984 & 1.08 & 0.93 \\
880	0.5 & 4 & 0.992 & 1.06 & 0.92 \\
881	\bottomrule
882	\end{tabular}
883	\end{table}
884	
885	Theorem~\ref{thm:bias_identity}'s product form remains accurate across all imbalance levels: $R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$, confirming that the bias identity derives from confusion matrix structure rather than class balance.
886	For $K{=}2$, EC-HTE outperforms global correction at all $P(Z{=}1)$ levels (RMSE ratio 0.76--0.92), degrading gracefully under severe imbalance.
887	For $K{=}4$, EC-HTE underperforms global at $n_{\text{expert}}{=}250$ (ratio 1.06--1.68), consistent with the budget threshold $n_{\text{expert}} \times P(Z_{\text{minority}}) / K \geq 25$: at $P(Z{=}1){=}0.1$, $K{=}4$, each subgroup receives only ${\sim}6$ minority-class labels.
888	The gap narrows as $P(Z{=}1)$ increases (1.54 $\to$ 1.06), and coverage remains stable at 0.92--0.94 across all configurations.
889	
890	\section{Comparison with PPI Correction}
891	\label{app:ppi_comparison}
892	
893	PPI~\cite{angelopoulos2023ppi} constructs confidence intervals by combining a large set of ML predictions with a smaller set of gold-standard labels, using the gold labels to debias the ML-based estimator.
894	Applied to our setting, PPI treats the LLM-annotated effect modifier as the ML prediction and the expert labels as the gold standard.
895	Two variants arise naturally: \emph{PPI-global} pools all expert labels to estimate a single rectifier (analogous to our Global baseline), and \emph{PPI-subgroup} estimates per-subgroup rectifiers (analogous to Stratified MLE).
896	
897	Under the confusion-matrix parameterization we adopt, DSL's measurement error correction reduces to confusion matrix inversion.
898	Pooled DSL applies a single estimated confusion matrix to all subgroups, producing the same corrected label distribution as our Global baseline; per-subgroup DSL estimates a separate confusion matrix for each subgroup and inverts it independently, equivalent to our Stratified MLE.
899	EC-HTE's contribution over both PPI-subgroup and per-subgroup DSL is hierarchical partial pooling: rather than estimating each subgroup's confusion matrix in isolation, EC-HTE places a shared prior across subgroups, borrowing strength to reduce variance while preserving subgroup-specific bias correction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dffa8191-0725-4296-b989-f1b88912ffd3",
  "isSidechain": true,
  "promptId": "4cbab432-dc02-4c34-8b10-e257b83b00f0",
  "agentId": "a4d47027ebc04c351",
  "type": "user",
  "uuid": "b0f94b12-8d27-4e73-b1b3-d3f90507fa96",
  "sourceToolAssistantUUID": "dffa8191-0725-4296-b989-f1b88912ffd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-23T20:30:56.331Z_

I now have a thorough understanding of the paper. Let me write the R1 review.

---

## R1 Review: "When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects"

### 1. Summary

This paper derives an exact bias identity showing that standard (global) confusion-matrix correction for LLM annotation errors introduces subgroup-level bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. The authors propose EC-HTE, a hierarchical Bayesian per-subgroup correction, and a diagnostic criterion for detecting when global correction is harmful. Extensive synthetic, semi-synthetic, and real-data experiments validate the identity ($R^2 \geq 0.97$) and characterize the operating regime where EC-HTE helps (sufficient expert budget and classifier quality) and where it fails (near-chance subgroup accuracy, high $K$ with limited labels).

### 2. Strengths

1. **Clean, verifiable theoretical result.** Theorem 1 is an exact finite-population identity with a transparent proof (matrix algebra on $2 \times 2$ confusion matrices). The product form $\delta_s \cdot \Delta\tau / (1 - 2\bar{\pi})$ is interpretable and the three-component factorization provides genuine insight. The $R^2 \geq 0.97$ empirical verification across 520+ configurations and 11 LLM-dataset combinations is convincing.

2. **Intellectual honesty about failure modes.** The paper is unusually transparent: EC-HTE fails on both real-data case studies (hate speech: FNR=53%, Table in App. E; GPT-4.1 semi-real: RMSE 0.784 vs. Global 0.263 at $n=100$, Table 10). The applicability frontier (Figure 5) and the three explicit preconditions ($n_{\text{expert}} \times P(Z_{\min})/K \geq 25$, max error rate $< 0.5$, adequate class balance) are clearly stated. This level of candor strengthens rather than weakens the contribution.

3. **Practically relevant problem.** The finding that global correction can reverse CATE sign (14.9% of configurations at $\tau(0) = 0.03$; 31% at $\tau(0) = 0.01$) addresses a real blind spot in the CSS+LLM pipeline. The diagnostic criterion (Proposition 2), computable from misclassification rates alone without estimating treatment effects, is independently useful.

4. **Comprehensive experimental coverage.** 10 of 11 planned experiments completed. The paper tests DIM, CausalForest, R-learner; $K \in \{2,4,8\}$; symmetric and asymmetric confusion matrices; class imbalance; subgroup misspecification noise; multiplicative DGPs; 10 LLMs (6 proprietary + 4 open-source); PPCI composition; budget sweeps. Monte Carlo SEs are reported with appropriate paired/unpaired tests. MCMC convergence diagnostics ($\hat{R} < 1.0034$, ESS $> 1618$) are solid.

5. **Well-positioned in the literature.** The related work carefully distinguishes effect-modifier misclassification from regressor, confounder, and treatment misclassification. The equivalence between pooled DSL and Global correction, and between per-subgroup DSL and Stratified MLE, is cleanly established.

6. **Classical Frazis-Loeb comparison.** Showing that the textbook scalar attenuation correction increases bias by 2.1--2.9x under heterogeneous errors (Table 1) is a valuable cautionary result for practitioners who might reach for the standard econometric fix.

### 3. Weaknesses

**W1 (Major): The proposed method fails on all real data.**
EC-HTE is worse than both Naive and Global on the hate speech case study (App. E), and worse than Global at all budgets on both semi-real experiments using GPT-4.1 and GPT-3.5 confusion matrices (Tables 10-11). The paper's positive results for EC-HTE come exclusively from synthetic and semi-synthetic DGPs where the misclassification structure is imposed by the experimenter. This is a serious external validity concern: the very real-world conditions the paper targets (LLM annotation with heterogeneous error) appear to violate the preconditions EC-HTE requires. The paper partially acknowledges this but the framing in the abstract and introduction emphasizes EC-HTE's "7.4x bias reduction" without adequate prominence of the real-data failures.

**W2 (Major): The diagnostic has limited practical utility.**
The diagnostic achieves AUC = 0.63 on real LLM-dataset combinations (Section 4.4), which is barely above chance. The AUC = 1.0 result is obtained only by conditioning on subgroups with $\Delta\tau > 0$, which requires knowing the CATE heterogeneity the diagnostic is supposed to avoid estimating. The paper's main text states "AUC = 1.0 on subgroups with non-zero effect heterogeneity" but this is somewhat circular: one must already know which subgroups have non-zero heterogeneity to apply this restriction. The setting-level AUC of 0.63 is the practically relevant number, and it is buried relative to the more flattering figures.

**W3 (Major): Synthetic DGP design favors EC-HTE.**
The synthetic DGP imposes symmetric misclassification ($\text{FPR}_s = \text{FNR}_s$), balanced effect modifiers ($P(Z=1) = 0.5$), equal subgroup weights, and treatment effects that vary only across $Z$-levels, not subgroups (A5). These are precisely the conditions under which EC-HTE's confusion matrix inversion is most stable. All real LLMs tested exhibit asymmetric confusion matrices and class imbalance. While the paper includes robustness checks relaxing each assumption individually, the conjunction of multiple assumption violations (as occurs in practice) is not systematically tested.

**W4 (Minor): Scalability limitation is underemphasized.**
At $K=8$ with $n_{\text{expert}} = 250$, EC-HTE RMSE is 2x worse than Global (0.340 vs. 0.168, Table 6). Many CSS applications have $K > 4$ (e.g., demographic intersections). The practical regime where EC-HTE helps ($K \leq 4$, extreme heterogeneity, $n_{\text{expert}} \geq 250$) is narrower than the introduction suggests.

**W5 (Minor): "Exact bias identity" framing overclaims novelty.**
The paper acknowledges (lines 060-062) that the result is a special case of classical measurement error theory. The matrix algebra in the proof (Appendix B) is straightforward: $M_{\text{global}}^{-1} M_s - I$ for $2 \times 2$ symmetric confusion matrices. While the application to the LLM-CATE setting is new, calling this an "exact bias identity" may set expectations for a deeper theoretical result than what is delivered.

**W6 (Minor): Section 5.11 (Adaptive allocation) is incomplete.**
The paper reports "projected results only" for one of the 11 planned experiments. While this is transparently acknowledged, it weakens the experimental completeness.

**W7 (Minor): The "sign reversal" framing is somewhat selective.**
Sign reversal occurs at 14.9% of configurations specifically at $\tau(0) = 0.03$, a small true effect. At larger effect sizes, the reversal rate drops. The headline number depends on the choice of grid over $\tau(0)$. The paper does show rates at $\tau(0) = 0.01$ (31%) and mentions a critical threshold ($\tau(0) < 0.089$), but the figure caption and abstract use 14.9% without sufficient context about its dependence on $\tau(0)$.

### 4. Questions to Authors

Q1. Can you provide a single real-world setting where EC-HTE achieves lower RMSE than Global correction? All real-data results in the paper show EC-HTE performing worse. If no such setting exists in your experiments, what evidence supports recommending EC-HTE over simply reporting the diagnostic and advising practitioners to use Global correction with awareness of its limitations?

Q2. The diagnostic AUC degrades from 0.86 (synthetic) to 0.63 (real). What drives this degradation? Is it primarily the asymmetry of real confusion matrices, the class imbalance, or the smaller effective sample sizes? Can you characterize the gap more precisely?

Q3. What happens when multiple assumption violations co-occur (asymmetric CM + class imbalance + unequal subgroup sizes + heterogeneous treatment effects across subgroups)? The robustness checks vary one assumption at a time; a factorial design over violations would be more informative.

Q4. The PPCI composition result (Table 7) shows EC-HTE+PPCI bias = 0.007 vs. PPCI alone bias = 0.017 under DGP C. But PPCI alone already achieves very low bias. Is the marginal contribution of EC-HTE statistically significant in this composition?

Q5. For the cross-LLM validation (Table 4), the Spearman correlations are computed over 6 subgroups, of which 2 are excluded for having zero misclassification. With only 4 data points, the rank correlations are underpowered. Can you justify the "consistent across architectures" claim with so few comparison points?

### 5. Soundness: 3.5 / 5

The theoretical result (Theorem 1) is sound and well-verified. The proof is correct. The experimental methodology is generally rigorous (appropriate MC sizes, convergence diagnostics, paired tests). However, the proposed method fails on all real data, the diagnostic has limited practical AUC, and the synthetic DGPs are designed under assumptions that favor the method. The gap between synthetic performance and real-world applicability is the primary soundness concern.

### 6. Excitement: 3.0 / 5

The problem is timely and the bias identity is a clean, useful result. The sign-reversal finding is practically important. However, the proposed correction does not work in practice (on the data tested), and the diagnostic is unreliable at the setting level. The paper's strongest contribution is the negative result (global correction can hurt) rather than the positive one (EC-HTE fixes it). A paper that primarily shows "this standard practice is dangerous, here's when and why, but our fix doesn't work on real data" is valuable but generates moderate rather than high excitement.

### 7. Reproducibility: 4.0 / 5

The paper provides detailed DGP specifications, hyperparameter settings (CausalForest: $n_{\text{estimators}} = 48$, $\text{min\_samples\_leaf} = 20$), MCMC specifications (4 chains, 4000 iterations, 2000 warmup), and convergence diagnostics. Code release is promised upon acceptance. The semi-synthetic experiments use publicly available datasets (TweetEval, UC Berkeley Hate Speech). The only gap is that exact LLM API versions and prompts are not fully specified, and the LLM annotations are not released (understandable given API cost, but limits exact replication of Tables 4-5).

### 8. Overall Assessment: 3.0 (Findings)

The bias identity is a solid, verifiable theoretical contribution, and the sign-reversal finding is practically important for the CSS+LLM community. The experimental coverage is thorough and the paper is notably honest about its method's limitations. However, the central methodological contribution (EC-HTE) fails on all real data tested, the diagnostic is unreliable at the practically relevant granularity (AUC = 0.63), and the strongest results come from synthetic DGPs whose assumptions favor the method. The paper reads more as a well-executed characterization of a problem than as a solution to it. This is appropriate for Findings but does not meet the bar for the main conference, where one expects the proposed method to demonstrate practical value beyond the synthetic setting.

If the authors reframed the paper around the bias identity and diagnostic as the primary contributions (a "characterization + warning" paper) rather than EC-HTE as a method contribution, the mismatch between claims and evidence would be reduced. As currently framed, the abstract's "reduces $|\text{bias}|$ by 7.4x via hierarchical Bayesian estimation" sets expectations that the real-data results do not fulfill.

### 9. Confidence: 4 / 5

I have expertise in measurement error models, causal inference, and LLM-based annotation. I read the full paper including appendices and verified the proof. I am less confident in my assessment of the NLP-specific experimental choices (TweetEval subgroup definitions, hate speech annotation protocols), which I treat as reasonable but cannot independently validate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0f94b12-8d27-4e73-b1b3-d3f90507fa96",
  "isSidechain": true,
  "agentId": "a4d47027ebc04c351",
  "requestId": "req_011CbL8fxiYneEEK5vqdCf28",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8aad78fc-aab5-493b-a1a4-681cbc28977b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "44ebc33a-5f0e-4594-9646-2fa2afa29759",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NgCLsSicGJAnx8Q9LPNVom",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5625,
      "cache_read_input_tokens": 56650,
      "output_tokens": 3106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5625
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3106,
          "cache_read_input_tokens": 56650,
          "cache_creation_input_tokens": 5625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5625,
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
