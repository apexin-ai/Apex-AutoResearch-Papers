# Research conversation: You are Reviewer 1 (R1) for an EMNLP 2026 submission. Your focus: **Methods and Experiments**. Evaluate soundness, exper

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a807effdf5ec0f5b7.jsonl`
- **Structured JSON:** [`4c0b7ab11e698ef061d4.json`](../../sessions/4c/4c0b7ab11e698ef061d4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-23T20:11:50.945Z_

You are Reviewer 1 (R1) for an EMNLP 2026 submission. Your focus: **Methods and Experiments**. Evaluate soundness, experimental rigor, reproducibility, and whether the claims are supported by evidence.

## Venue: EMNLP 2026 (via ARR)
Scoring: Overall Assessment 1-5 (half-point scale). Dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5).
- 5 = Award consideration (top 2.5%)
- 4 = Main conference accept (~21% acceptance)
- 3 = Findings accept
- 2 = Resubmit next cycle
- 1 = Do not resubmit

Acceptance rate ~21% for Main. Calibrate strictly.

## Paper Summary

**Title:** "When Debiasing Hurts: Misclassification Heterogeneity in LLM-Annotated Effect Modifiers Amplifies Treatment Effect Bias"

**Core Problem:** In computational social science, LLMs annotate effect modifiers (e.g., sentiment, hate speech type) for heterogeneous treatment effect (HTE) analysis. LLM misclassification rates vary across subgroups. Applying a global (pooled) confusion matrix correction to subgroup-level CATEs introduces systematic bias proportional to the product of misclassification heterogeneity (Δπ) and CATE heterogeneity (Δτ). In 50% of parameter space, global correction makes estimates WORSE.

**5 Contributions claimed:**
1. **Bias decomposition identity (Theorem 1):** Bias of global-corrected CATE for subgroup k = Σ_ℓ [C̄⁻¹ - C_k⁻¹]_{kℓ} · μ̄_ℓ. For binary Z with symmetric misclassification: Bias ∝ (π̄ - π_k) · Δτ. Verified at R² > 0.97 across all configurations.
2. **EC-HTE framework:** Hierarchical Bayesian subgroup-stratified confusion matrix estimation with Dirichlet priors and Gamma hyperpriors. Partial pooling (James-Stein shrinkage). MCMC via PyMC NUTS, 4 chains, 1000 warmup. Correction: τ̂_k^{EC-HTE} = [Ĉ_k⁻¹ μ̄_k].
3. **Diagnostic criterion:** Δπ_k × Δτ̂_k product from pilot data predicts when global correction is harmful. Subgroup-level AUC = 0.833.
4. **EC-HTE + PPCI composition:** For dual error sources (covariate-side + outcome-side), composition achieves near-zero bias (0.005), 35× improvement over EC-HTE alone.
5. **Comprehensive validation:** synthetic, semi-synthetic (TweetEval + GPT-4.1), real data (UC Berkeley Hate Speech), 6 LLM generations.

**Assumptions:** SUTVA, Unconfoundedness, Non-differential misclassification (Z̃ ⊥ Y | Z, X), Invertibility (det(Ĉ_k) ≠ 0).

## Key Experimental Results

**Exp 1 - Bias Identity Verification (Section 5.1):**
- 520 non-trivial configs: Δπ ∈ {0,0.05,...,0.25} × Δτ ∈ {0,0.1,...,0.5} × K ∈ {2,4}
- R² = 0.994 (K=2), 0.974 (K=4). Tightness ratio near 1.0.
- Global hurts in 50% of configs (excluding Δτ=0). Max amplification: 2.86× (DIM, K=2), 5.9× (CausalForest, K=4).

**Exp 2 - HB Validation (Appendix A):**
- 3600 MC runs. R̂ < 1.01, ESS > 1618, zero divergences.
- HB vs MLE: 4-9% RMSE improvement at K=2/n=50, up to 18.8% at K=4/extreme/n=50.
- Coverage median 0.93 (below nominal 0.95).
- Hyperprior sensitivity: <1% for K=2, ~4-5% for K=4.

**Exp 3 - Semi-Synthetic (Section 5.2):**
- TweetEval sentiment, N=45K, GPT-4.1 annotation, K=4 subgroups, Δπ=0.20.
- Global correction INCREASES S3 bias from 0.089 to 0.142 (1.6×). S0: 5.6× amplification.
- EC-HTE at n=100: bias 0.015, RMSE 0.078 for S3.
- Progression from n=100 to n=500 shows consistent improvement.

**Exp 4 - CausalForest (Section 5.3):**
- 144 rows, 100 MC runs. EC-HTE reduces mean bias by 61% vs naive, 43% vs global.
- BUT: EC-HTE RMSE (0.229) > global (0.166) — bias-RMSE tradeoff.
- Tradeoff resolves at n≥500 (K=2): bias 0.004-0.013 with competitive RMSE.
- Max amplification: 5.9× at K=4/extreme/sg0.

**Exp 5 - PPCI Comparison (Section 5.4):**
- 4 DGPs × 8 methods × 100 MC runs = 6912 rows.
- DGP A (cov only): EC-HTE=0.008 bias, PPCI=0.045, EC-HTE+PPCI=0.008.
- DGP C (both): Naive=0.251, EC-HTE=0.178, PPCI=0.004, EC-HTE+PPCI=0.005 (coverage 1.00).
- 35× improvement of composition over EC-HTE alone in DGP C.

**Exp 6 - Budget Analysis (Section 5.5):**
- 288 configs. Crossover points: K=2/extreme at n=250, K=4/extreme at n=1000, K=4/moderate at n=2000. K=2/moderate: never.
- HB outperforms MLE in 87.5% of configs.

**Exp 7 - Diagnostic (Section 5.6):**
- Subgroup-level AUC=0.833, correlation=0.86.
- Setting-level AUC=0.49 (near random, theoretically expected).
- Low-Δπ subgroups hurt 84.6% of the time.

**Exp 8 - Real Data (Section 5.7):**
- UC Berkeley Hate Speech, N=2496, GPT-4.1, K=4 subgroups.
- Δπ=0.117 (significant heterogeneity). FNR=0.533 (high).
- EC-HTE does NOT outperform — near-singular CM. Positioned as honest boundary condition.

**Exp 9 - Multi-LLM (Appendix B):**
- 6 OpenAI models. All Δπ > 0.05. Structural persistence confirmed.
- GPT-5.4: Δπ=0.114.

**Exp 10 - Robustness (Appendix C):**
- Noise 0-50%. Coverage drops only ~1pp. Graceful degradation via HB shrinkage.

**Exp 11 - Adaptive Allocation (Appendix D):**
- CATE-weighted: 21% RMSE improvement over uniform. Crossover K=4 from n=1000→700.

## Experimental Coverage Check
The review_context.yaml lists these planned experiments:
- exp-001 (HB validation) ✓ Appendix A
- exp-002 (Bias identity) ✓ Section 5.1
- exp-003 (Semi-synthetic) ✓ Section 5.2
- exp-004 (Real data) ✓ Section 5.7
- exp-005 (Diagnostic) ✓ Section 5.6
- exp-006 (Budget) ✓ Section 5.5
- exp-007 (PPCI/DSL) ✓ Section 5.4
- exp-008 (Multi-LLM) ✓ Appendix B
- exp-009 (Adaptive allocation) ✓ Appendix D
- exp-010 (Robustness) ✓ Appendix C
- exp-011 (CausalForest) ✓ Section 5.3
- exp-012 through exp-017: Not explicitly listed in paper. Some results appear integrated (e.g., GPT-4.1 pilot Δπ=0.200 from exp-012 appears in semi-synthetic setup).

## Paper Format
- 8 pages main text (within EMNLP limit) + references + appendices A-E
- Limitations section present in main text (3 points)
- Abstract appears under 200 words
- Anonymous submission
- 21 tables total (9 main, 12 appendix)

## Your Review Task

Produce a structured review with:

1. **Summary** (2-3 sentences)
2. **Strengths** (numbered, focus on methodological and experimental quality)
3. **Weaknesses** (numbered, focus on methodological gaps, experimental limitations, missing controls)
4. **Questions for Authors** (numbered)
5. **Soundness Score** (1-5, with justification)
6. **Reproducibility Score** (1-5, with justification)
7. **Excitement Score** (1-5, with justification)
8. **Overall Assessment** (1-5 half-point scale, with justification calibrated to EMNLP acceptance rate)
9. **Confidence** (1-5)

Be rigorous. Check for: (a) whether claims match evidence, (b) statistical methodology soundness, (c) experimental design choices and potential confounds, (d) bias-RMSE tradeoff acknowledgment, (e) assumption plausibility, (f) reproducibility details.

Return the complete review as a single structured document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "63aff3d0-4044-4865-a723-cb26918efdda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-23T20:11:50.951Z_

```json
{
  "parentUuid": "63aff3d0-4044-4865-a723-cb26918efdda",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
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
  "uuid": "2a7de57d-f35d-46ce-94bb-5a5f4c622f21",
  "timestamp": "2026-05-23T20:11:50.951Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-23T20:11:53.500Z_



I'll start by loading the project files to conduct a thorough review of the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a7de57d-f35d-46ce-94bb-5a5f4c622f21",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7L1zaFfoAzroUgSiph",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "58f8c937-0706-4e99-bc33-d13b35b918d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpgaTtGJ9D9mBR7QBjnZ5e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17576,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17576,
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

_source line 4 · 2026-05-23T20:11:54.937Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Jaqc79bp1fBmCQ7z9C4waX`</summary>

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
  "parentUuid": "58f8c937-0706-4e99-bc33-d13b35b918d4",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7L1zaFfoAzroUgSiph",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea28acfa-3505-41aa-b449-0c2b3bf90348",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpgaTtGJ9D9mBR7QBjnZ5e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17576,
      "cache_read_input_tokens": 0,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17576
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17576,
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

_source line 5 · 2026-05-23T20:11:54.942Z_

<details><summary>↩ Tool result · `toolu_01Jaqc79bp1fBmCQ7z9C4waX`</summary>

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
  "parentUuid": "ea28acfa-3505-41aa-b449-0c2b3bf90348",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "759e76ce-4b00-4a47-b6c6-5d28419fe4ce",
  "sourceToolAssistantUUID": "ea28acfa-3505-41aa-b449-0c2b3bf90348",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-23T20:11:57.743Z_



Let me read the paper and supporting materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "759e76ce-4b00-4a47-b6c6-5d28419fe4ce",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7LKJ8GfgidXXLPmsB4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "21c414a4-48ce-43b5-9ebf-24ff9b71d73f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ayXNM6ih1EeUNA7w2nrxL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 17576,
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

_source line 7 · 2026-05-23T20:11:58.218Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_01KCcnwh5krypYkiJ3SJDL62`</summary>

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
  "parentUuid": "21c414a4-48ce-43b5-9ebf-24ff9b71d73f",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7LKJ8GfgidXXLPmsB4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eacf89e0-0313-4192-87eb-a33a4a23a16f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ayXNM6ih1EeUNA7w2nrxL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 17576,
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

_source line 8 · 2026-05-23T20:11:58.371Z_

<details><summary>↩ Tool result · `toolu_01KCcnwh5krypYkiJ3SJDL62`</summary>

```text
{"result":"# 项目 ec_hte_llm_annotation 概况\n\n## 实验状态 (42 个)\n\n- **exp-015**: DONE (negative) — \n- **exp-008**: DONE (success) — \n- **exp-004**: DONE (success) — \n- **exp-010**: DONE (success) — \n- **exp-014**: DONE (success) — \n- **exp-013**: DONE (success) — \n- **exp-012**: DONE (success) — \n- **exp-006**: DONE (success) — \n- **exp-007b**: DONE (killed) — \n- **exp-003**: DONE (success) — \n- **exp-011**: DONE (success) — \n- **exp-005**: DONE (success) — \n- **exp-007**: DONE (success) — \n- **exp-001**: DONE (success) — \n- **exp-002**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-23\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- Paper Agent 正在整合 exp-038/039/040 结果到论文 appendix\n- Rebuttal talking points 待更新（sign-reversal, F-L, κ, cross-LLM 数据）\n- EMNLP 2026 ARR DDL: 2026-05-25（~40h）\n\n## 近期结论\n\n- **exp-038** (success): Policy reversal zone τ sweep — global correction 在 τ(0)<0.05 时导致 CATE sign reversal（τ=0.01→31%, τ=0.03→14.9%），EC-HTE 0% reversal。最危险组合 τ=0.01+δ_misclass=0.19→42.9%。\n- **exp-039** (success, mixed): K=8 scalability — EC-HTE 在 K=2/4 显著优于 Global（bias 降 5-7×），K=8 退化（RMSE 0.34 vs Global 0.17），但 coverage 始终 ≥95.6%。根因：250/8≈31 expert/subgroup 不足。\n- **exp-040** (success, mixed): Treatment-dependent misclassification — EC-HTE 在 γ_T≤0.05 时 robust（coverage ≥89.7%, RMSE 优势），γ_T≈0.10 为 breakeven point，γ_T≥0.15 严重退化。\n- **exp-036** (success): Bootstrap SE 在所有 n_expert≥25 下维持 ≥95% coverage。\n- **exp-037** (success): Temperature calibration 降低但不消除 Δπ，EC-HTE 仍然必要。\n- **exp-035** (success): 非对称 CM（FPR≠FNR 7:1）下 coverage ≥93%。\n\n## Excitement 提分产出（R17 修复）\n\n| Artifact | 核心数字 | 状态 |\n|----------|---------|------|\n| sign_reversal_figure | 92% configs affected, 0% EC-HTE | ✅ 已注册 |\n| cross_llm_heatmap | 9 LLMs, mean ρ=0.244, min=-0.80 | ✅ Reviewer PASS |\n| bias_anatomy_heatmap | R²=0.9938, 52% grid debiasing hurts | ✅ Reviewer PASS |\n| debiasing_hurts_summary | 26.5% of 2132 pairs hurt, real LLM 100% | ✅ 已注册 |\n| policy_reversal_zone | τ=0.01→31% reversal, danger zone 可视化 | ✅ 已注册 |\n| k_scalability_bars | K=2/4 优, K=8 boundary | ✅ 已注册 |\n| treatment_dep_misclass_figure | γ_T breakeven ≈0.10 | ✅ 已注册 |\n\n## 趋势\n成功 34 / 负向 5 / 失败 0 / 共 40\n\n## 下一步\n- Paper Agent 整合新实验到论文\n- Rebuttal talking points 更新\n- DDL 前编译验证 + 提交\n\n## 资源状态\nautodl-rtx6000: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\nlocal-cpu: 空闲\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eacf89e0-0313-4192-87eb-a33a4a23a16f",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "6ab2652f-9c02-442b-86a2-9195f12b4cb6",
  "sourceToolAssistantUUID": "eacf89e0-0313-4192-87eb-a33a4a23a16f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T20:11:59.630Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0183N1Z4z7b397r3JFpUxL2f`</summary>

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
  "parentUuid": "6ab2652f-9c02-442b-86a2-9195f12b4cb6",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7LKJ8GfgidXXLPmsB4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fddc0977-1bca-4704-91e4-02d37d0b1111",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ayXNM6ih1EeUNA7w2nrxL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 17576,
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

_source line 10 · 2026-05-23T20:11:59.643Z_

<details><summary>↩ Tool result · `toolu_0183N1Z4z7b397r3JFpUxL2f`</summary>

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
docs/paper/theory.tex
docs/paper/main.tex
docs/paper/method.tex
docs/paper/experiments.tex
docs/paper/related_work.tex
docs/paper/abstract.tex
docs/paper/conclusion.tex
artifacts/dream_reports/dream_20260523T193110/best/paper.tex
artifacts/dream_reports/dream_20260523T193110/median/paper.tex
docs/paper/introduction.tex
docs/paper/limitations.tex
artifacts/dream_reports/dream_20260523T193110/worst/paper.tex
docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fddc0977-1bca-4704-91e4-02d37d0b1111",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "08c310aa-a9af-4848-9427-104e1072f422",
  "sourceToolAssistantUUID": "fddc0977-1bca-4704-91e4-02d37d0b1111",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T20:12:00.267Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013s7i8uEzpZcSdTVwpSdFbb`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08c310aa-a9af-4848-9427-104e1072f422",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7LKJ8GfgidXXLPmsB4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b478e680-b51c-4b89-b6de-3496c1be0a39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ayXNM6ih1EeUNA7w2nrxL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 17576,
      "output_tokens": 257,
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
          "output_tokens": 257,
          "cache_read_input_tokens": 17576,
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

_source line 12 · 2026-05-23T20:12:00.277Z_

<details><summary>↩ Tool result · `toolu_013s7i8uEzpZcSdTVwpSdFbb`</summary>

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
artifacts/_project/chart/fig1_bias_mechanism.pdf
artifacts/_project/paper/main_297877.pdf
artifacts/dream_reports/dream_20260521T122454/best/paper.pdf
artifacts/dream_reports/dream_20260521T122454/median/paper.pdf
artifacts/dream_reports/dream_20260521T122454/worst/paper.pdf
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
artifacts/k_scalability_figure.pdf
artifacts/_project/chart/k_scalability_bars.pdf
artifacts/k_scalability_bars.pdf
artifacts/_project/chart/treatment_dep_misclass_figure.pdf
artifacts/treatment_dep_misclass_figure.pdf
artifacts/review_round_12/submitted.pdf
artifacts/dream_reports/dream_20260523T193110/best/paper.pdf
artifacts/dream_reports/dream_20260523T193110/median/paper.pdf
artifacts/dream_reports/dream_20260523T193110/worst/paper.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b478e680-b51c-4b89-b6de-3496c1be0a39",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "81b95a34-c733-4a37-8e6d-7515885d9dfe",
  "sourceToolAssistantUUID": "b478e680-b51c-4b89-b6de-3496c1be0a39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T20:12:03.994Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NEJCZ6qcfrNcTvj8jS7DJk`</summary>

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
  "parentUuid": "81b95a34-c733-4a37-8e6d-7515885d9dfe",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7LhzsZKnugiGC5n4cY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dcc95e70-3193-4a94-9237-e0b05be0ace6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFUYti3bEAjg3q4LwF5bRP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2884,
      "cache_read_input_tokens": 19023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2884,
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

_source line 14 · 2026-05-23T20:12:04.002Z_

<details><summary>↩ Tool result · `toolu_01NEJCZ6qcfrNcTvj8jS7DJk`</summary>

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
  "parentUuid": "dcc95e70-3193-4a94-9237-e0b05be0ace6",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "09e4037a-767d-4e86-bff6-1380d2cde19b",
  "sourceToolAssistantUUID": "dcc95e70-3193-4a94-9237-e0b05be0ace6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T20:12:04.479Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QpYzsQ1AyZk3nE563RF78w`</summary>

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
  "parentUuid": "09e4037a-767d-4e86-bff6-1380d2cde19b",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7LhzsZKnugiGC5n4cY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ce6a635f-97c2-45db-b899-086552b29b4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFUYti3bEAjg3q4LwF5bRP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2884,
      "cache_read_input_tokens": 19023,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2884,
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

_source line 16 · 2026-05-23T20:12:04.484Z_

<details><summary>↩ Tool result · `toolu_01QpYzsQ1AyZk3nE563RF78w`</summary>

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
  "parentUuid": "ce6a635f-97c2-45db-b899-086552b29b4c",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "e3527c8a-ffb8-4cd3-98eb-7375306ef392",
  "sourceToolAssistantUUID": "ce6a635f-97c2-45db-b899-086552b29b4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T20:12:04.707Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TZqQ84XwzvnKRjLYqoK9YH`</summary>

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
  "parentUuid": "e3527c8a-ffb8-4cd3-98eb-7375306ef392",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7LhzsZKnugiGC5n4cY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56b47755-a5b0-45fd-95e9-3cd9e7da88c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HFUYti3bEAjg3q4LwF5bRP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2884,
      "cache_read_input_tokens": 19023,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2884
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 19023,
          "cache_creation_input_tokens": 2884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2884,
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

_source line 18 · 2026-05-23T20:12:04.711Z_

<details><summary>↩ Tool result · `toolu_01TZqQ84XwzvnKRjLYqoK9YH`</summary>

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
  "parentUuid": "56b47755-a5b0-45fd-95e9-3cd9e7da88c6",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "b7438429-cca0-48f0-8f50-2cce921727fb",
  "sourceToolAssistantUUID": "56b47755-a5b0-45fd-95e9-3cd9e7da88c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T20:12:08.565Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MqXzLAsru5eQ4TgcAo4aZj`</summary>

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
  "parentUuid": "b7438429-cca0-48f0-8f50-2cce921727fb",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7M346i1upv4T1KnXWw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59234b81-bc36-48a7-8598-fd28314987c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3cjYMKiAWFbvSuh24RV3E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2886,
      "cache_read_input_tokens": 21907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2886,
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

_source line 20 · 2026-05-23T20:12:08.570Z_

<details><summary>↩ Tool result · `toolu_01MqXzLAsru5eQ4TgcAo4aZj`</summary>

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
81	Empirical verification (Section~\ref{sec:bias_mechanism}) yields $R^2 = 0.994$ for $K{=}2$ and $R^2 = 0.974$ for $K{=}4$, closing the theory-practice gap to essentially zero; the residual variance reflects Monte Carlo noise, not model misspecification.
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
  "parentUuid": "59234b81-bc36-48a7-8598-fd28314987c7",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "2192e5ff-247f-413d-8809-bce45e846b5d",
  "sourceToolAssistantUUID": "59234b81-bc36-48a7-8598-fd28314987c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T20:12:08.910Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QcowAdj24A8DiP2VwvZdv8`</summary>

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
  "parentUuid": "2192e5ff-247f-413d-8809-bce45e846b5d",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7M346i1upv4T1KnXWw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b02bdf0d-775b-4463-b93c-e4143b62a764",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3cjYMKiAWFbvSuh24RV3E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2886,
      "cache_read_input_tokens": 21907,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2886
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 21907,
          "cache_creation_input_tokens": 2886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2886,
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

_source line 22 · 2026-05-23T20:12:08.915Z_

<details><summary>↩ Tool result · `toolu_01QcowAdj24A8DiP2VwvZdv8`</summary>

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
  "parentUuid": "b02bdf0d-775b-4463-b93c-e4143b62a764",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "bdb79316-7547-48af-9ef2-75d8a72bee2c",
  "sourceToolAssistantUUID": "b02bdf0d-775b-4463-b93c-e4143b62a764",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T20:12:13.608Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JXW4BNWENKYH49fSztBoTK`</summary>

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
  "parentUuid": "bdb79316-7547-48af-9ef2-75d8a72bee2c",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7MMR9PaxErX67tUUkt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9c03fc2-1fe7-47b0-98ab-90978ab1ac87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Z7KJMKXqy8tGCmEtJazLV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6858,
      "cache_read_input_tokens": 24793,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6858,
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

_source line 24 · 2026-05-23T20:12:13.613Z_

<details><summary>↩ Tool result · `toolu_01JXW4BNWENKYH49fSztBoTK`</summary>

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
16	Regressing observed subgroup bias on $\delta_s \cdot \Delta\tau / (1{-}2\bar{\pi})$ yields $R^2 = 0.994$ ($K{=}2$) and $0.974$ ($K{=}4$); residual variance reflects MC noise ($R^2 \geq 0.976$ even at $P(Z{=}1) = 0.1$; Appendix~\ref{app:classimbalance}).
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
  "parentUuid": "e9c03fc2-1fe7-47b0-98ab-90978ab1ac87",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "00bb37d9-d5fb-417f-bfdb-966bba510c67",
  "sourceToolAssistantUUID": "e9c03fc2-1fe7-47b0-98ab-90978ab1ac87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T20:12:14.146Z_

<details open><summary>🔧 Tool call — Read · `toolu_0165YRTV9mpawDCv4T4AGhSV`</summary>

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
  "parentUuid": "00bb37d9-d5fb-417f-bfdb-966bba510c67",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7MMR9PaxErX67tUUkt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "240ca43b-424d-485d-bfba-af5f46b45815",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Z7KJMKXqy8tGCmEtJazLV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6858,
      "cache_read_input_tokens": 24793,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6858,
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

_source line 26 · 2026-05-23T20:12:14.151Z_

<details><summary>↩ Tool result · `toolu_0165YRTV9mpawDCv4T4AGhSV`</summary>

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
  "parentUuid": "240ca43b-424d-485d-bfba-af5f46b45815",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "21393e50-55f2-4ab6-a768-1f71b84f23e0",
  "sourceToolAssistantUUID": "240ca43b-424d-485d-bfba-af5f46b45815",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T20:12:14.433Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H2rBw836yA4oPPpHP8qf7r`</summary>

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
  "parentUuid": "21393e50-55f2-4ab6-a768-1f71b84f23e0",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7MMR9PaxErX67tUUkt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2954c2a8-573c-4f5d-ba89-31fc64ee7807",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Z7KJMKXqy8tGCmEtJazLV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6858,
      "cache_read_input_tokens": 24793,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6858
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 24793,
          "cache_creation_input_tokens": 6858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6858,
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

_source line 28 · 2026-05-23T20:12:14.436Z_

<details><summary>↩ Tool result · `toolu_01H2rBw836yA4oPPpHP8qf7r`</summary>

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
  "parentUuid": "2954c2a8-573c-4f5d-ba89-31fc64ee7807",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "77a111ec-cac2-4bb0-a5a1-223a493e0e0b",
  "sourceToolAssistantUUID": "2954c2a8-573c-4f5d-ba89-31fc64ee7807",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T20:12:21.948Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TVKRCvRtgyRhMgyeuw4ecY`</summary>

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
  "parentUuid": "77a111ec-cac2-4bb0-a5a1-223a493e0e0b",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7MkbRJAtnhPiRLuX4w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f72de9fd-7e69-4ab2-b5ee-9e34a4bb74e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kg9vG6d25rPXBSEuS2w87k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5593,
      "cache_read_input_tokens": 31651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5593,
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

_source line 30 · 2026-05-23T20:12:21.952Z_

<details><summary>↩ Tool result · `toolu_01TVKRCvRtgyRhMgyeuw4ecY`</summary>

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
  "parentUuid": "f72de9fd-7e69-4ab2-b5ee-9e34a4bb74e8",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "b701ac86-1b99-41b0-85a4-5ac8f569e06a",
  "sourceToolAssistantUUID": "f72de9fd-7e69-4ab2-b5ee-9e34a4bb74e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T20:12:22.318Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CVDDpk4jx93xVYiisq5TVP`</summary>

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
  "parentUuid": "b701ac86-1b99-41b0-85a4-5ac8f569e06a",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7MkbRJAtnhPiRLuX4w",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3287eca4-083e-4f73-9de2-397071d16bbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kg9vG6d25rPXBSEuS2w87k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5593,
      "cache_read_input_tokens": 31651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5593,
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

_source line 32 · 2026-05-23T20:12:22.585Z_

<details><summary>↩ Tool result · reported error · `toolu_01CVDDpk4jx93xVYiisq5TVP`</summary>

```text
File content (39508 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3287eca4-083e-4f73-9de2-397071d16bbf",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "b27e2baf-6497-4697-a2e9-03c51b2a3fc5",
  "toolUseResult": "Error: File content (39508 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "3287eca4-083e-4f73-9de2-397071d16bbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T20:12:24.737Z_

<details open><summary>🔧 Tool call — Read · `toolu_013SuJR4xvezYKcvbZZA8q9c`</summary>

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
  "parentUuid": "b27e2baf-6497-4697-a2e9-03c51b2a3fc5",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7NMAo5dtouY16zBCAU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "765aaf28-1e4c-4e83-a2c9-6107d344d969",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WD7WwgoVnWofM4xKJJpjX6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 427,
      "cache_read_input_tokens": 37244,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 427
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 37244,
          "cache_creation_input_tokens": 427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 427,
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

_source line 34 · 2026-05-23T20:12:24.747Z_

<details><summary>↩ Tool result · `toolu_013SuJR4xvezYKcvbZZA8q9c`</summary>

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
  "parentUuid": "765aaf28-1e4c-4e83-a2c9-6107d344d969",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "9392a4e4-7be1-460a-bc0d-e03797272453",
  "sourceToolAssistantUUID": "765aaf28-1e4c-4e83-a2c9-6107d344d969",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T20:12:28.799Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W46XJVgXbCKJF7DQKBaF9n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9392a4e4-7be1-460a-bc0d-e03797272453",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7NWgY2dCtiGYnwm5cZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3a74f21-eff8-4e50-9b8c-35bf029508ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MT9vMR6tF4u6JbHVucqQPr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6228,
      "cache_read_input_tokens": 37671,
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
          "cache_read_input_tokens": 37671,
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

_source line 36 · 2026-05-23T20:12:28.804Z_

<details><summary>↩ Tool result · `toolu_01W46XJVgXbCKJF7DQKBaF9n`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3a74f21-eff8-4e50-9b8c-35bf029508ff",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "673b6bdc-505d-42b8-98b1-f891830ec03f",
  "sourceToolAssistantUUID": "f3a74f21-eff8-4e50-9b8c-35bf029508ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T20:12:32.946Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PeJdXwrooAo8RoYo99Ywac`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 499,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "673b6bdc-505d-42b8-98b1-f891830ec03f",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7Np2aHqWra71HeWuaU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c5a26bd-38d5-448f-b227-fc613fa148c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnHCdJAbRrDyQwLTHbsvCM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8282,
      "cache_read_input_tokens": 43899,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8282
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 43899,
          "cache_creation_input_tokens": 8282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8282,
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

_source line 38 · 2026-05-23T20:12:32.953Z_

<details><summary>↩ Tool result · `toolu_01PeJdXwrooAo8RoYo99Ywac`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c5a26bd-38d5-448f-b227-fc613fa148c0",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "cdaaaf0d-c7f1-4f7a-a6a0-bf72bb093fe7",
  "sourceToolAssistantUUID": "5c5a26bd-38d5-448f-b227-fc613fa148c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T20:12:37.125Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DGZdNTanEtPVGsdmNfK8qo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 798,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdaaaf0d-c7f1-4f7a-a6a0-bf72bb093fe7",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7P7YHEsbBh2nURydHY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1eeb3d96-186b-473b-b859-65f18822e91e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01May2LF2WUn1XbjLXJ1CjsY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8331,
      "cache_read_input_tokens": 52181,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8331,
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

_source line 40 · 2026-05-23T20:12:37.131Z_

<details><summary>↩ Tool result · `toolu_01DGZdNTanEtPVGsdmNfK8qo`</summary>

```text
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
900	This mechanism is outside both the PPI and DSL frameworks.
901	
902	The key difference between PPI and confusion-matrix inversion is that PPI does not invert the confusion matrix; instead, it uses the gold labels to directly debias the estimand.
903	This avoids the matrix inversion step that can amplify noise at small $n_{\text{expert}}$, but it also means PPI cannot exploit the structure of the misclassification process to reduce bias.
904	PPI-global inherits the same $\Delta\pi \times \Delta\tau$ bias amplification as Global correction (Theorem~\ref{thm:bias_identity}), confirming that the ``debiasing hurts'' mechanism operates regardless of the inference framework.
905	
906	\section{Civil Comments Validation}
907	\label{app:civilcomments}
908	
909	To verify that subgroup-heterogeneous misclassification generalizes beyond TweetEval, we annotate $N{=}3{,}000$ stratified samples (30\% toxic) from Civil Comments~\cite{borkan2019nuanced}, a toxicity detection dataset.
910	Subgroups are defined by \texttt{text\_length\_bin} $\times$ \texttt{has\_question} ($K{=}4$): S0 (long, no question, 38.8\%), S1 (long, question, 11.4\%), S2 (short, no question, 33.7\%), S3 (short, question, 16.1\%).
911	Subgroup features were chosen a priori based on observable text properties; no feature search was performed.
912	Three proprietary LLMs annotate each sample via an OpenAI-compatible API, yielding 800--900 valid annotations per model.
913	
914	Table~\ref{tab:civil_cm} reports per-subgroup FPR and FNR.
915	We define $\Delta\pi = \max_s \pi_s - \min_s \pi_s$, where $\pi_s$ is the overall misclassification rate for subgroup $s$.
916	All three models exhibit $\Delta\pi > 0.05$, with overall heterogeneity $\Delta\pi \in [0.113, 0.160]$---comparable to the $\Delta\pi \in [0.125, 0.165]$ observed across four open-source LLMs on TweetEval (Appendix~\ref{app:multilm_opensource}).
917	GPT-4o-mini and GPT-3.5-turbo show pronounced FPR/FNR asymmetry (e.g., GPT-4o-mini FPR $\in [0.42, 0.61]$ vs.\ FNR $\in [0.05, 0.16]$), indicating systematic over-prediction of toxicity; their FPR approaches 0.5, placing them in the ill-conditioned regime where confusion matrix inversion amplifies noise (consistent with the classifier quality threshold discussed in the Limitations section).
918	The consistent presence of $\Delta\pi$ heterogeneity across two NLP tasks, seven LLMs spanning open-source (7B--9B) and proprietary families, and two distinct subgroup definitions confirms that this phenomenon is a structural property of LLM annotation rather than an artifact of a specific dataset or model.
919	
920	\begin{table}[h]
921	\centering
922	\caption{Per-subgroup misclassification rates on Civil Comments ($K{=}4$). $\Delta$ denotes max $-$ min across subgroups.}
923	\label{tab:civil_cm}
924	\small
925	\begin{tabular}{llccccc}
926	\toprule
927	Model & Metric & S0 & S1 & S2 & S3 & $\Delta$ \\
928	\midrule
929	GPT-4o & FPR & 0.249 & 0.157 & 0.213 & 0.341 & 0.184 \\
930	       & FNR & 0.160 & 0.263 & 0.308 & 0.328 & 0.168 \\
931	\midrule
932	GPT-4o-mini & FPR & 0.517 & 0.541 & 0.419 & 0.610 & 0.191 \\
933	            & FNR & 0.052 & 0.105 & 0.074 & 0.160 & 0.108 \\
934	\midrule
935	GPT-3.5-turbo & FPR & 0.400 & 0.473 & 0.374 & 0.468 & 0.099 \\
936	              & FNR & 0.139 & 0.211 & 0.173 & 0.240 & 0.101 \\
937	\bottomrule
938	\end{tabular}
939	\end{table}
940	
941	\section{Bias Identity Validation with Real Confusion Matrices}
942	\label{app:realcm_bias}
943	
944	Theorem~\ref{thm:bias_identity} is derived under symmetric misclassification (A2); real LLM confusion matrices are asymmetric (FPR $\neq$ FNR).
945	We verify that the generalized identity $\mathrm{bias}(z,s) = \Delta\tau \cdot [B_s]_{z,1}$ (Remark~\ref{thm:bias_identity}) holds under real annotation error structures by running semi-synthetic simulations ($N{=}5{,}000$, $K{=}4$, $\Delta\tau{=}0.30$, 100 MC runs) with confusion matrices drawn from 11 LLM--dataset combinations: eight models on TweetEval (GPT-4-turbo, GPT-4o, GPT-4.1, GPT-4o-mini, GPT-3.5-turbo, Qwen2.5-7B, Mistral-7B, Gemma-2-9B) and three on Civil Comments (GPT-4o, GPT-4o-mini, GPT-3.5-turbo).
946	
947	Table~\ref{tab:realcm_r2} reports per-model $R^2$ from regressing observed subgroup bias on the predicted value $\Delta\tau \cdot [B_s]_{z,1}$.
948	The aggregate $R^2 = 0.975$; 10 of 11 combinations achieve $R^2 \geq 0.92$.
949	The single outlier (GPT-4o-mini on Civil Comments, $R^2{=}0.76$) has near-homogeneous subgroup error rates ($\max|[B_s]_{z,1}| = 0.089$), so predicted biases are small and Monte Carlo noise dominates the regression.
950	$R^2$ correlates strongly with $\max|[B_s]_{z,1}|$: models with more heterogeneous per-subgroup error rates produce larger bias signals that are easier to verify empirically.
951	
952	\begin{table}[h]
953	\centering
954	\caption{Bias identity $R^2$ with real LLM confusion matrices ($K{=}4$, 100 MC runs).}
955	\label{tab:realcm_r2}
956	\small
957	\begin{tabular}{llcc}
958	\toprule
959	Model & Dataset & $R^2$ & $\max|[B_s]_{z,1}|$ \\
960	\midrule
961	GPT-4-turbo  & TweetEval & 0.993 & 0.328 \\
962	Qwen2.5-7B   & TweetEval & 0.990 & 0.272 \\
963	Mistral-7B   & TweetEval & 0.990 & 0.242 \\
964	Gemma-2-9B   & TweetEval & 0.982 & 0.185 \\
965	GPT-4o       & Civil Comments & 0.979 & 0.198 \\
966	GPT-4o       & TweetEval & 0.975 & 0.240 \\
967	GPT-4.1      & TweetEval & 0.969 & 0.139 \\
968	GPT-3.5-turbo & TweetEval & 0.948 & 0.087 \\
969	GPT-3.5-turbo & Civil Comments & 0.935 & 0.170 \\
970	GPT-4o-mini  & TweetEval & 0.929 & 0.170 \\
971	GPT-4o-mini  & Civil Comments & 0.756 & 0.089 \\
972	\midrule
973	\multicolumn{2}{l}{All (pooled)} & 0.975 & --- \\
974	\bottomrule
975	\end{tabular}
976	\end{table}
977	
978	\section{Applicability Screening with Real LLM Confusion Matrices}
979	\label{app:screening}
980	
981	We apply the diagnostic conditions from Proposition~\ref{prop:debiasing_hurts} and Section~\ref{sec:method} to 16 LLM--dataset--$K$ combinations spanning seven LLMs (four open-source, three proprietary) across TweetEval and Civil Comments.
982	Table~\ref{tab:screening} summarizes which conditions each combination satisfies.
983	
984	\begin{table}[h]
985	\centering
986	\caption{Diagnostic screening of 16 LLM--dataset--$K$ combinations. Columns report whether all subgroups satisfy each condition. Budget assumes $n_{\text{expert}}{=}500$.}
987	\label{tab:screening}
988	\small
989	\begin{tabular}{llccccc}
990	\toprule
991	Model & Dataset & $K$ & $\kappa{\leq}1.25$ & $\max{\leq}0.5$ & Budget & Pass all \\
992	\midrule
993	Gemma-2-9B   & TweetEval & 2 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
994	Llama-3.1-8B & TweetEval & 2 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
995	Mistral-7B   & TweetEval & 2 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
996	Qwen2.5-7B   & TweetEval & 2 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
997	Gemma-2-9B   & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
998	Llama-3.1-8B & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
999	Mistral-7B   & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1000	Qwen2.5-7B   & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1001	GPT-3.5-turbo & CivilComm. & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1002	GPT-3.5-turbo & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1003	GPT-4-turbo  & TweetEval & 4 & {\small$\times$} & {\small$\times$} & {\small$\checkmark$} & {\small$\times$} \\
1004	GPT-4.1      & TweetEval & 4 & {\small$\times$} & {\small$\times$} & {\small$\checkmark$} & {\small$\times$} \\
1005	GPT-4o       & CivilComm. & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1006	GPT-4o       & TweetEval & 4 & {\small$\times$} & {\small$\times$} & {\small$\checkmark$} & {\small$\times$} \\
1007	GPT-4o-mini  & CivilComm. & 4 & {\small$\times$} & {\small$\times$} & {\small$\checkmark$} & {\small$\times$} \\
1008	GPT-4o-mini  & TweetEval & 4 & {\small$\times$} & {\small$\checkmark$} & {\small$\checkmark$} & {\small$\times$} \\
1009	\bottomrule
1010	\end{tabular}
1011	\end{table}
1012	
1013	No combination passes all three conditions; the bottleneck is $\kappa(C_s) \leq 1.25$, which requires $\mathrm{FPR}_s + \mathrm{FNR}_s \lesssim 0.20$ for all subgroups---a threshold no current LLM achieves uniformly.
1014	The closest are Qwen2.5-7B True\_short ($\kappa{=}1.23$) and Mistral-7B True\_short ($\kappa{=}1.27$).
1015	
1016	Under a relaxed ``oracle screening'' that excludes near-degenerate subgroups ($\max(\mathrm{FPR}_s, \mathrm{FNR}_s) \geq 0.4$), we run semi-synthetic CATE estimation ($N{=}5{,}000$, $\Delta\tau{=}0.3$, 100 MC runs, $n_{\text{expert}} \in \{250, 500\}$) with each LLM's real per-subgroup confusion matrix.
1017	EC-HTE (HB) achieves lower RMSE than global correction in 41 of 52 comparisons (79\%) and lower RMSE than stratified MLE in 52 of 52 comparisons (100\%).
1018	The four open-source LLMs on TweetEval show the strongest EC-HTE advantage (32/32 comparisons, RMSE reduction 0.001--0.008), while GPT-3.5-turbo/TweetEval (high FPR asymmetry, $\mathrm{FPR}_{\max}{=}0.39$) and GPT-4o/Civil Comments (low minority prevalence $P(Z{=}1){=}0.3$) show degradation.
1019	The diagnostic correctly identifies the strict applicability regime; under relaxed conditions excluding near-degenerate subgroups, EC-HTE improves RMSE in 79\% of comparisons.
1020	
1021	\paragraph{Diagnostic Applicability Analysis.}
1022	The diagnostic (Proposition~\ref{prop:debiasing_hurts}) degrades on real LLM confusion matrices (pooled AUC $= 0.63$) because the failure mode is systematic: subgroups where the true CATE heterogeneity $\tau_s \approx 0$ are hurt by global correction (since $\delta_s \neq 0$ still introduces bias), yet these subgroups produce low diagnostic scores---the diagnostic ranks them as safe precisely when they are most vulnerable to overcorrection.
1023	
1024	A simple meta-criterion recovers reliability: compute $\max_s |\delta_s| / ((1 - 2\bar{\pi}) \cdot \pi_s)$ across subgroups.
1025	When $\max_s \mathrm{score}(s) > 1$, at least one subgroup is definitively harmed by global correction, and the diagnostic achieves AUC $\geq 0.75$ across all 5 model--dataset combinations satisfying this condition (AUC range: 0.75--1.0).
1026	When $\max_s \mathrm{score}(s) \leq 1$, global correction may or may not hurt depending on unobservable $\Delta\tau$; the diagnostic achieves AUC only 0.0--0.67 across the remaining 7 combinations (4 of 7 have AUC $< 0.5$, indicating anti-prediction).
1027	This threshold perfectly separates reliable from unreliable diagnostic regimes across all 16 real LLM--dataset combinations evaluated.
1028	
1029	We recommend the following practical protocol: (i) estimate per-subgroup confusion matrices from expert labels; (ii) compute $\max_s \mathrm{score}(s)$; (iii) if $> 1$, the diagnostic reliably identifies which subgroups are harmed by global correction---apply EC-HTE; (iv) if $\leq 1$, the diagnostic is unreliable and practitioners should either default to EC-HTE as a conservative choice or evaluate correction strategies using held-out expert labels.
1030	
1031	\subsection{$\kappa$ Stratification Analysis}
1032	\label{app:kappa_analysis}
1033	
1034	The condition number $\kappa(\hat{C}_s) = 1/|1 - \mathrm{FPR}_s - \mathrm{FNR}_s|$ quantifies confusion matrix invertibility and governs the bias-variance tradeoff of per-subgroup correction.
1035	The $\kappa \leq 1.25$ threshold identified in the diagnostic rule (Section~\ref{sec:budget}) is a \emph{sufficient condition} for strongest bias reduction, not a necessary condition: EC-HTE maintains calibrated inference across a substantially wider $\kappa$ range.
1036	
1037	\paragraph{Synthetic data.}
1038	Across all 520 synthetic configurations ($K{=}2$, $\pi_s \in [0.025, 0.275]$), the maximum per-config $\kappa$ falls in $[1.43, 2.22]$; none reaches $\kappa \leq 1.25$ because the pooled rate $\bar{\pi}{=}0.15$ sets a floor of $\kappa{=}1/(1{-}2 \cdot 0.15){=}1.43$.
1039	Table~\ref{tab:kappa_synth} shows a two-bin stratification at $\kappa{=}2$: EC-HTE achieves zero analytic bias in both bins, while global correction harms at least one subgroup in 100\% of $\kappa > 2$ configurations.
1040	Monte Carlo validation ($K{=}2$, $n_{\text{expert}}{=}500$) confirms EC-HTE dominance at $\kappa{=}2.0$: 86\% bias reduction, 10\% lower RMSE, and 95.5\% coverage vs.\ 88.3\% for Global.
1041	
1042	\begin{table}[h]
1043	\centering
1044	\caption{Synthetic $\kappa$ stratification ($K{=}2$, 520 configs). ``Debiasing hurts'' = global correction increases $|\text{bias}|$ for $\geq$1 subgroup.}
1045	\label{tab:kappa_synth}
1046	\small
1047	\begin{tabular}{lcccc}
1048	\toprule
1049	$\kappa$ bin & $n$ & EC-HTE bias & Debiasing hurts & Global $|\text{bias}|/|\text{bias}_{\text{naive}}|$ \\
1050	\midrule
1051	$\leq 2.0$ & 420 & 0 (exact) & 35.0\% & 0.152 \\
1052	$> 2.0$    & 100 & 0 (exact) & 100\% & 0.326 \\
1053	\bottomrule
1054	\end{tabular}
1055	\end{table}
1056	
1057	\paragraph{Real LLM confusion matrices.}
1058	All 13 real LLM--dataset combinations ($K{=}4$) have $\kappa \in [1.88, 2.99]$---none reaches $\kappa \leq 1.25$, because no current LLM achieves $\mathrm{FPR}_s + \mathrm{FNR}_s < 0.20$ uniformly across subgroups.
1059	Table~\ref{tab:kappa_real} reports performance stratified by $\kappa$ bin and expert budget.
1060	The key finding is that EC-HTE maintains calibrated coverage ($\geq$93\%) across all $\kappa$ bins at $n_{\text{expert}} \geq 250$, compared to 86--91\% for Global.
1061	At $n_{\text{expert}}{=}500$, EC-HTE also achieves competitive RMSE in the $\kappa \leq 2$ bin (ratio 1.01) and bias win rate of 75\%; at $n_{\text{expert}}{=}250$, the variance cost of per-subgroup estimation dominates, and Global achieves lower RMSE---consistent with the bias-variance tradeoff documented in the main text (Section~\ref{sec:ec_hte_eval}).
1062	
1063	\begin{table}[h]
1064	\centering
1065	\caption{Real LLM $\kappa$ stratification ($K{=}4$, MC validation). Ratios = EC-HTE / Global; values $<1$ favor EC-HTE. Coverage is EC-HTE absolute; Global coverage ranges 0.86--0.91 across bins.}
1066	\label{tab:kappa_real}
1067	\small
1068	\begin{tabular}{llcccc}
1069	\toprule
1070	$\kappa$ bin & $n_{\text{expert}}$ & Bias ratio & RMSE ratio & Bias win & Cov.\ (EC-HTE) \\
1071	\midrule
1072	\multirow{2}{*}{$\leq 2.0$ ($n{=}4$)}
1073	 & 500 & 0.99 & 1.01 & 75\% & 0.943 \\
1074	 & 250 & 1.09 & 1.13 & 0\%  & 0.932 \\
1075	\midrule
1076	\multirow{2}{*}{$> 2.0$ ($n{=}9$)}
1077	 & 500 & 1.11 & 1.22 & 22\% & 0.949 \\
1078	 & 250 & 1.26 & 1.43 & 0\%  & 0.940 \\
1079	\bottomrule
1080	\end{tabular}
1081	\end{table}
1082	
1083	The three-tier $\kappa$ structure is thus: (i)~$\kappa > 100$: near-random classification, singularity guard triggers automatic fallback to global correction; (ii)~$\kappa \leq 1.25$: strongest theoretical regime with guaranteed bias reduction and coverage; (iii)~$\kappa \in (1.25, {\sim}3]$: the practical operating range for current LLMs, where EC-HTE provides calibrated inference (coverage $\geq$93\%) and achieves RMSE gains when expert budget is sufficient ($n_{\text{expert}} \geq 500$).
1084	
1085	\section{Plug-in Standard Error Validation}
1086	\label{app:bootstrap_se}
1087	
1088	A natural concern is whether the plug-in standard error adequately captures estimation uncertainty, particularly the additional variance introduced by confusion matrix estimation.
1089	We verify this for the difference-in-means (DIM) estimator via Monte Carlo simulation ($K{=}2$, $n_{\text{expert}} \in \{50, 100, 250, 500\}$, 50 replications per budget level).
1090	At each budget, we compute the plug-in 95\% confidence interval and record empirical coverage.
1091	Across all expert budgets, the plug-in SE yields coverage $\geq 0.96$ (0.970, 0.960, 0.970, 0.970 for $n_{\text{expert}} = 50, 100, 250, 500$), confirming that the analytic variance estimate is well-calibrated for the DIM estimator.
1092	This self-calibration arises because the same noise in $\hat{M}^{-1}$ that inflates point-estimate variance also inflates the plug-in SE, producing conservative intervals that maintain nominal coverage.
1093	
1094	\paragraph{CausalForestDML.}
1095	Under $K{=}2$ extreme heterogeneity ($\pi{=}[0.05, 0.25]$, $n_{\text{expert}}{=}250$, $n_{\text{estimators}}{=}200$, 20 MC runs), EC-HTE plug-in SE achieves 93.8\% aggregate coverage---close to the 94--96\% oracle coverage (Table~\ref{tab:cf_oracle}).
1096	The high-error subgroup ($s_1$, $\pi{=}0.25$) shows slightly lower plug-in coverage (92.5\%) than the low-error subgroup ($s_0$: 95.0\%), reflecting the larger $M^{-1}$ amplification of estimation uncertainty in subgroups with higher misclassification rates.
1097	By contrast, the DIM plug-in SE achieves $\geq$95\% coverage in the same DGP, confirming that the analytic confusion matrix propagation formula is adequate for simpler estimators.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1eeb3d96-186b-473b-b859-65f18822e91e",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "37b2819d-6390-46bb-a50e-bf3da22b41c9",
  "sourceToolAssistantUUID": "1eeb3d96-186b-473b-b859-65f18822e91e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T20:12:45.154Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TvmqtYgtD9QRVpjpPwScYY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 1097,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37b2819d-6390-46bb-a50e-bf3da22b41c9",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7PS5178qP6gfZ5B2kA",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bdc9e875-57b8-4b11-9d68-add95a77014b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zCTqP8cnqZreFGD9zBMkB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9536,
      "cache_read_input_tokens": 60512,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9536
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 60512,
          "cache_creation_input_tokens": 9536,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9536,
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

_source line 42 · 2026-05-23T20:12:45.163Z_

<details><summary>↩ Tool result · `toolu_01TvmqtYgtD9QRVpjpPwScYY`</summary>

```text
1097	By contrast, the DIM plug-in SE achieves $\geq$95\% coverage in the same DGP, confirming that the analytic confusion matrix propagation formula is adequate for simpler estimators.
1098	
1099	\paragraph{Full bootstrap SE.}
1100	A \emph{full} bootstrap---resampling all $N$ observations and re-estimating both the confusion matrix and CausalForest per bootstrap replicate ($B{=}100$, $n_{\text{estimators}}{=}200$, 20 MC runs)---confirms that plug-in SE is already near-nominal under standard hyperparameters.
1101	Under $K{=}2$ extreme heterogeneity ($\pi{=}[0.05, 0.25]$, $n_{\text{expert}}{=}250$), plug-in SE achieves 93.8\% aggregate coverage; the full bootstrap improves this to exactly 95.0\% ($+$1.2pp).
1102	Table~\ref{tab:bootstrap_se} reports per-subgroup results.
1103	
1104	\begin{table}[h]
1105	\centering
1106	\caption{CausalForest coverage: plug-in SE vs.\ full bootstrap SE ($B{=}100$, $n_{\text{estimators}}{=}200$, 20 MC runs). Bootstrap SE is ${\sim}1.15\times$ plug-in.}
1107	\label{tab:bootstrap_se}
1108	\small
1109	\begin{tabular}{lccccc}
1110	\toprule
1111	Subgroup & Plugin Cov. & Boot.\ Cov. & Oracle Cov. & Plugin SE & Boot.\ SE \\
1112	\midrule
1113	$s_0$ ($\pi{=}0.05$) & 0.950 & 0.925 & 0.925 & 0.059 & 0.063 \\
1114	$s_1$ ($\pi{=}0.25$) & 0.925 & \textbf{0.975} & 0.875 & 0.087 & 0.103 \\
1115	\midrule
1116	Aggregate & 0.938 & \textbf{0.950} & 0.900 & 0.073 & 0.083 \\
1117	\bottomrule
1118	\end{tabular}
1119	\end{table}
1120	
1121	The high-error subgroup ($s_1$) benefits most: coverage rises from 92.5\% to 97.5\% ($+$5.0pp), because the bootstrap captures the additional variance from $M^{-1}$ amplification.
1122	Oracle coverage (90.0\%) is consistent with the 94\% reported in the oracle decomposition (Table~\ref{tab:cf_oracle}), with the difference attributable to MC sampling noise at 20 runs.
1123	The computational cost is substantial ($B \times$ CF fits per MC run), but the approach is straightforward when exact nominal coverage is required.
1124	
1125	\paragraph{Bootstrap coverage across expert budgets.}
1126	Table~\ref{tab:bootstrap_small_n} extends the analysis to $n_{\text{expert}} \in \{25, 50, 75, 100, 200\}$ using the DIM estimator with Centered EB confusion matrix estimation ($K{=}2$ extreme, $\pi{=}[0.05, 0.25]$, 20 MC runs, $B{=}100$).
1127	Bootstrap SE maintains $\geq$95\% coverage across all expert budgets, including $n_{\text{expert}}{=}25$ (${\approx}12$ labels per subgroup).
1128	Plug-in SE is already near-nominal ($\geq$91.2\%) at all budgets tested.
1129	
1130	\begin{table}[h]
1131	\centering
1132	\caption{HB EC-HTE coverage across expert budgets: plug-in vs.\ bootstrap SE (DIM, $K{=}2$ extreme, 20 MC, $B{=}100$).}
1133	\label{tab:bootstrap_small_n}
1134	\small
1135	\begin{tabular}{lcccc}
1136	\toprule
1137	$n_{\text{expert}}$ & Plugin Cov. & Boot.\ Cov. & SE Ratio & $|\text{Bias}|$ \\
1138	\midrule
1139	25 & 0.925 & \textbf{1.000} & 2.86 & 0.079 \\
1140	50 & 0.975 & 0.988 & 2.93 & 0.067 \\
1141	75 & 0.912 & \textbf{0.975} & 2.59 & 0.065 \\
1142	100 & 0.963 & 0.963 & 1.52 & 0.060 \\
1143	200 & 0.963 & 0.950 & 1.17 & 0.061 \\
1144	\bottomrule
1145	\end{tabular}
1146	\end{table}
1147	
1148	At small $n_{\text{expert}}$, bootstrap SE inflates confidence intervals by $2{-}3\times$ relative to plug-in (SE ratio column), guaranteeing nominal coverage but reducing statistical power.
1149	At $n_{\text{expert}} \geq 100$, the SE ratio converges to ${\sim}1.2{-}1.5\times$, and plug-in SE alone achieves $\geq$96\% coverage.
1150	For practical deployment, we recommend $n_{\text{expert}} \geq 50$: bootstrap maintains nominal coverage (98.8\%) with moderate SE inflation (2.9$\times$), and plug-in SE achieves 97.5\%---close to nominal without bootstrap overhead.
1151	
1152	\paragraph{Finite-sample remainder.}
1153	By first-order matrix perturbation, $\hat{C}_s^{-1} = C_s^{-1} - C_s^{-1} E_s C_s^{-1} + O(\|E_s\|^2)$, where $E_s = \hat{C}_s - C_s$ satisfies $\|E_s\| = O_p(n_{\text{expert}}^{-1/2})$.
1154	The remainder in the corrected CATE is therefore $R_n = O_p(n_{\text{expert}}^{-1/2} \cdot \|C_s^{-1}\|^2) = O_p(n_{\text{expert}}^{-1/2} \cdot \kappa(C_s))$, since $\|C_s^{-1}\| = O(\kappa(C_s))$ for stochastic matrices.
1155	This motivates the $\kappa > 100$ singularity guard (Section~\ref{sec:method}).
1156	
1157	\subsection{CausalForest Oracle Coverage Decomposition}
1158	\label{app:cf_oracle}
1159	
1160	To isolate the source of CausalForest under-coverage, we compare six estimation strategies that progressively remove sources of uncertainty: (1)~Oracle (true $Z$, no correction), (2)~EC-HTE with true $C_s$, (3)~EC-HTE with estimated $\hat{C}_s$ (HB), (4)~Global with true $\bar{C}$, (5)~Global with estimated $\hat{\bar{C}}$, and (6)~Naive.
1161	Table~\ref{tab:cf_oracle} reports coverage, $|\text{bias}|$, and RMSE across three DGP configurations (100 MC runs each).
1162	
1163	\begin{table}[h]
1164	\centering
1165	\caption{CausalForest oracle coverage decomposition. Coverage averaged over subgroups and $z$-levels.}
1166	\label{tab:cf_oracle}
1167	\small
1168	\begin{tabular}{ll ccc}
1169	\toprule
1170	DGP & Method & Cov.\ (\%) & $|\text{Bias}|$ & RMSE \\
1171	\midrule
1172	\multirow{6}{*}{\shortstack[l]{$K{=}4$, extreme\\$n{=}500$}}
1173	 & Oracle (true $Z$)       & 94.5 & 0.006 & 0.078 \\
1174	 & EC-HTE true $C_s$       & 92.5 & 0.008 & 0.114 \\
1175	 & EC-HTE est.\ $\hat{C}_s$ & 93.1 & 0.015 & 0.121 \\
1176	 & Global true $\bar{C}$   & 91.3 & 0.037 & 0.110 \\
1177	 & Global est.\ $\hat{\bar{C}}$ & 91.1 & 0.038 & 0.111 \\
1178	 & Naive                    & 88.3 & 0.045 & 0.095 \\
1179	\midrule
1180	\multirow{6}{*}{\shortstack[l]{$K{=}2$, extreme\\$n{=}250$}}
1181	 & Oracle (true $Z$)       & 94.0 & 0.002 & 0.056 \\
1182	 & EC-HTE true $C_s$       & 94.0 & 0.003 & 0.073 \\
1183	 & EC-HTE est.\ $\hat{C}_s$ & 92.5 & 0.004 & 0.079 \\
1184	 & Global true $\bar{C}$   & 88.5 & 0.045 & 0.083 \\
1185	 & Global est.\ $\hat{\bar{C}}$ & 88.3 & 0.045 & 0.085 \\
1186	 & Naive                    & 82.8 & 0.046 & 0.077 \\
1187	\midrule
1188	\multirow{6}{*}{\shortstack[l]{$K{=}2$, MF2 DGP\\$\tau{=}(0.10,0.40)$}}
1189	 & Oracle (true $Z$)       & 96.0 & 0.077 & 0.091 \\
1190	 & EC-HTE true $C_s$       & 91.3 & 0.103 & 0.112 \\
1191	 & EC-HTE est.\ $\hat{C}_s$ & 92.3 & 0.100 & 0.111 \\
1192	 & Global true $\bar{C}$   & 95.0 & 0.107 & 0.114 \\
1193	 & Global est.\ $\hat{\bar{C}}$ & 94.3 & 0.105 & 0.114 \\
1194	 & Naive                    & 77.3 & 0.120 & 0.125 \\
1195	\bottomrule
1196	\end{tabular}
1197	\end{table}
1198	
1199	Three findings emerge.
1200	First, oracle coverage is 94--96\% across all DGPs, confirming that CausalForest plug-in SE is well-calibrated when labels are correct.
1201	Second, EC-HTE with true $C_s$ achieves 91--94\% coverage---a 0--5pp gap from oracle (configuration-dependent), reflecting $M^{-1}$ SE propagation asymmetry across DGPs rather than confusion matrix estimation error.
1202	Third, the gap between true and estimated $C_s$ is ${\leq}$1.5pp ($K{=}2$) and $<$1pp ($K{=}4$), confirming that CM estimation uncertainty contributes negligibly at $n_{\text{expert}} \geq 250$.
1203	
1204	\section{Robustness to Assumption Violations}
1205	\label{app:a5_violation}
1206	
1207	\subsection{Assumption (A5): Subgroup-Specific Treatment Effects}
1208	
1209	\begin{corollary}[Subgroup-Specific Treatment Effect Heterogeneity]
1210	\label{cor:a5_relaxation}
1211	When $\Delta\tau$ varies across subgroups ($\Delta\tau_s = \tau_s(1) - \tau_s(0)$), the bias of global correction in subgroup $s$ at level $z{=}0$ is $+\delta_s \cdot \Delta\tau_s / (1 - 2\bar{\pi})$, and at level $z{=}1$ is $-\delta_s \cdot \Delta\tau_s / (1 - 2\bar{\pi})$.
1212	\end{corollary}
1213	The proof follows directly from Theorem~\ref{thm:bias_identity} with $\tau_s$ replacing $\tau$.
1214	
1215	Our main analysis assumes that subgroup misclassification rates $\delta_s$ and subgroup CATE magnitudes $\Delta\tau_s$ are independent (Assumption A5).
1216	In practice, both may depend on text features that define subgroups, introducing correlation.
1217	We test robustness under two configurations with the DIM estimator ($K{=}2$, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 50 MC replications, $\pi = [0.05, 0.25]$):
1218	\emph{aligned} (positive $\delta_s$--$\Delta\tau_s$ correlation: high-error S1 has the larger treatment effect, $\Delta\tau = [0.30, 0.70]$) and
1219	\emph{adversarial} (negative correlation: high-error S1 has the smaller effect, $\Delta\tau = [0.70, 0.30]$).
1220	
1221	\begin{table}[h]
1222	\centering
1223	\caption{Coverage and $|\text{bias}|$ under A5 violation ($K{=}2$, $n_{\text{expert}}{=}250$, 50 MC). Target coverage: 0.95.}
1224	\label{tab:a5_violation}
1225	\small
1226	\begin{tabular}{llcccc}
1227	\toprule
1228	Config & Method & S0 cov & S1 cov & S0 $|\text{bias}|$ & S1 $|\text{bias}|$ \\
1229	\midrule
1230	\multirow{4}{*}{Aligned}
1231	 & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\
1232	 & Naive         & 0.93 & 0.25 & 0.022 & 0.174 \\
1233	 & Global        & 0.93 & 0.82 & 0.036 & 0.094 \\
1234	 & EC-HTE (EB)   & 0.95 & 0.95 & 0.005 & 0.017 \\
1235	\midrule
1236	\multirow{4}{*}{Adversarial}
1237	 & Oracle        & 0.94 & 0.98 & 0.003 & 0.003 \\
1238	 & Naive         & 0.90 & 0.78 & 0.042 & 0.074 \\
1239	 & Global        & 0.74 & 0.93 & 0.098 & 0.040 \\
1240	 & EC-HTE (EB)   & 0.94 & 0.96 & 0.002 & 0.007 \\
1241	\bottomrule
1242	\end{tabular}
1243	\end{table}
1244	
1245	In the aligned configuration, the $\delta_s \times \Delta\tau_s$ product is maximized in the high-error subgroup, causing naive S1 coverage to collapse to 0.25.
1246	Global correction improves S1 but cannot fully correct without subgroup-specific error rates.
1247	In the adversarial configuration, global correction overcorrects the low-error subgroup (S0 coverage 0.74).
1248	EC-HTE (EB) maintains $\geq 0.94$ coverage across both subgroups in both configurations, with bias comparable to the oracle.
1249	Results at $n_{\text{expert}}{=}500$ are consistent (all EC-HTE coverages $\in [0.93, 0.99]$).
1250	
1251	\subsection{Assumption (A1): Sensitivity to Outcome-Dependent Misclassification}
1252	\label{app:a1_sensitivity}
1253	
1254	We assess EC-HTE's robustness when misclassification depends on potential outcomes, violating~(A1).
1255	We modify the synthetic DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$) so that misclassification probability becomes outcome-dependent: $P(\hat{Z}{\neq}Z \mid Z, S, Y) = \mathrm{clamp}(\pi_s + \gamma \cdot (Y - \mu_Y)/\sigma_Y,\, 0,\, 1)$, where $\gamma \in \{0, 0.05, 0.10, 0.15, 0.20\}$ controls the strength of violation.
1256	Table~\ref{tab:a1_sensitivity} reports results averaged over 100 MC runs.
1257	
1258	\begin{table}[h]
1259	\centering
1260	\caption{Sensitivity to Assumption~(A1) violation. Coverage and $|\text{bias}|$ under outcome-dependent misclassification ($\gamma > 0$).}
1261	\label{tab:a1_sensitivity}
1262	\small
1263	\begin{tabular}{lccc ccc}
1264	\toprule
1265	& \multicolumn{3}{c}{Coverage (\%)} & \multicolumn{3}{c}{$|\text{Bias}|$} \\
1266	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
1267	$\gamma$ & EC-HTE & Global & Naive & EC-HTE & Global & Naive \\
1268	\midrule
1269	0.00 & 95.5 & 92.7 & 87.7 & 0.060 & 0.065 & 0.061 \\
1270	0.05 & 95.5 & 93.5 & 83.8 & 0.059 & 0.064 & 0.064 \\
1271	0.10 & 95.3 & 93.8 & 83.5 & 0.063 & 0.064 & 0.067 \\
1272	0.15 & 94.8 & 94.3 & 79.2 & 0.065 & 0.064 & 0.070 \\
1273	0.20 & 93.5 & 94.0 & 79.5 & 0.068 & 0.063 & 0.073 \\
1274	\bottomrule
1275	\end{tabular}
1276	\end{table}
1277	
1278	EC-HTE maintains near-nominal coverage ($\geq$93.5\%) across the full $\gamma$ range, with $|\text{bias}|$ increasing only 13.7\% from $\gamma{=}0$ to $\gamma{=}0.2$.
1279	All correction methods (Global, Stratified MLE, HB) maintain $\geq$90\% coverage, indicating that moderate (A1) violations do not catastrophically degrade confusion-matrix-based correction.
1280	The naive estimator degrades most rapidly (coverage $-$8.2pp), consistent with outcome-dependent misclassification compounding the uncorrected label noise.
1281	
1282	\subsection{Assumption (A1): Treatment-Dependent Misclassification}
1283	\label{app:treatment_dep}
1284	
1285	We extend the (A1) sensitivity analysis to the treatment-dependent case, where misclassification probability depends on treatment assignment $T$: $P(\hat{Z}{\neq}Z \mid Z, S, T) = \mathrm{clamp}(\pi_s + \gamma_T \cdot (2T - 1),\, 0,\, 1)$, with $\gamma_T \in \{0, 0.05, 0.10, 0.15, 0.20\}$.
1286	This scenario arises when LLM accuracy varies with treatment status---e.g., treated texts may be systematically harder to classify.
1287	Setup: $K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs.
1288	
1289	\begin{table}[h]
1290	\centering
1291	\caption{Sensitivity to treatment-dependent misclassification ($\gamma_T$). EC-HTE maintains $\geq$89.7\% coverage at $\gamma_T \leq 0.05$.}
1292	\label{tab:treatment_dep}
1293	\small
1294	\begin{tabular}{lcc}
1295	\toprule
1296	$\gamma_T$ & EC-HTE Coverage & EC-HTE RMSE \\
1297	\midrule
1298	0.00 & 0.945 & 0.075 \\
1299	0.05 & 0.897 & 0.092 \\
1300	0.10 & 0.750 & 0.133 \\
1301	0.15 & 0.525 & 0.177 \\
1302	0.20 & 0.370 & 0.224 \\
1303	\bottomrule
1304	\end{tabular}
1305	\end{table}
1306	
1307	EC-HTE is robust to small treatment-dependent violations ($\gamma_T \leq 0.05$), maintaining $\geq$89.7\% coverage with modest RMSE increase (0.075 to 0.092).
1308	At $\gamma_T = 0.10$, coverage drops to 75.0\%, establishing this as the approximate breakeven point.
1309	The degradation is steeper than for outcome-dependent violations (Table~\ref{tab:a1_sensitivity}), because treatment-dependent errors directly contaminate the treatment arm contrast.
1310	Figure~\ref{fig:treatment_dep} visualizes the coverage and RMSE trajectories.
1311	
1312	\begin{figure}[h]
1313	\centering
1314	\includegraphics[width=\columnwidth]{figures/treatment_dep_misclass.pdf}
1315	\caption{EC-HTE coverage and RMSE under treatment-dependent misclassification. Dashed line: 90\% coverage threshold. Breakeven at $\gamma_T \approx 0.10$.}
1316	\label{fig:treatment_dep}
1317	\end{figure}
1318	
1319	\subsection{Extension to Confounded Treatment Assignment}
1320	\label{app:confounded_dgp}
1321	
1322	EC-HTE's confusion matrix correction operates on estimated CATEs regardless of how those estimates are produced.
1323	To verify compatibility with observational (non-RCT) designs, we pair EC-HTE with an inverse probability weighted difference-in-means (IPW-DIM) estimator under confounded treatment assignment.
1324	
1325	\paragraph{DGP.}
1326	$N{=}5{,}000$, $K{=}2$, $\pi = [0.05, 0.25]$, $n_{\text{expert}}{=}250$, 100 MC replications.
1327	A covariate $X \sim \mathcal{N}(0,1)$ confounds both treatment and outcome:
1328	$T \sim \text{Bernoulli}(\sigma(\beta X))$ with $\beta{=}0.5$ (moderate confounding; propensity range $[0.38, 0.62]$),
1329	$Y = 1 + 0.5 Z + 0.3 X + \tau(Z) \cdot T + \eta$, $\eta \sim \mathcal{N}(0,1)$.
1330	Treatment effects are $\tau(Z{=}0){=}0$, $\tau(Z{=}1){=}0.3$.
1331	The IPW-DIM estimator uses \emph{oracle propensity} $e(X) = \sigma(\beta X)$, with propensity scores clipped to $[0.05, 0.95]$.
1332	
1333	\begin{table}[h]
1334	\centering
1335	\caption{EC-HTE under confounded treatment assignment (IPW-DIM with oracle propensity, $\beta{=}0.5$, 100 MC).}
1336	\label{tab:confounded_dgp}
1337	\small
1338	\begin{tabular}{lccc}
1339	\toprule
1340	Method & Coverage & RMSE & $|\text{Bias}|$ \\
1341	\midrule
1342	Oracle (true $Z$ + IPW) & 0.943 & 0.061 & 0.048 \\
1343	HB EC-HTE              & 0.950 & 0.086 & 0.068 \\
1344	Global                  & 0.930 & 0.087 & 0.071 \\
1345	Strat MLE               & 0.950 & 0.087 & 0.069 \\
1346	Naive                   & 0.863 & 0.083 & 0.066 \\
1347	\bottomrule
1348	\end{tabular}
1349	\end{table}
1350	
1351	EC-HTE achieves 95.0\% coverage, within 0.7pp of the oracle (94.3\%), confirming that confusion matrix correction and propensity weighting compose without interference.
1352	The improvement is most pronounced in the high-error subgroup ($\pi{=}0.25$): EC-HTE coverage is 96.0\% vs.\ naive 78.5\% ($+$17.5pp).
1353	Global coverage (93.0\%) falls below the correction methods (95.0\%), consistent with the cost of ignoring subgroup-level error heterogeneity even in the confounded setting.
1354	
1355	\paragraph{Sensitivity to confounding strength and propensity estimation.}
1356	We sweep $\beta \in \{0.25, 0.5, 1.0, 2.0\}$ and compare oracle propensity ($e(X) = \sigma(\beta X)$) with estimated propensity (logistic regression fit on $(X, T)$), yielding 8 configurations (100 MC each).
1357	Table~\ref{tab:confounded_sweep} reports HB EC-HTE and naive coverage.
1358	
1359	\begin{table}[h]
1360	\centering
1361	\caption{EC-HTE coverage across confounding strengths and propensity sources. The logistic regression propensity model is correctly specified; propensity misspecification is a complementary concern addressed by the IPW literature.}
1362	\label{tab:confounded_sweep}
1363	\small
1364	\begin{tabular}{cccc}
1365	\toprule
1366	$\beta$ & Propensity & HB Coverage & Naive Coverage \\
1367	\midrule
1368	0.25 & Oracle    & 0.963 & 0.848 \\
1369	0.25 & Estimated & 0.973 & 0.845 \\
1370	0.50 & Oracle    & 0.950 & 0.863 \\
1371	0.50 & Estimated & 0.958 & 0.858 \\
1372	1.00 & Oracle    & 0.958 & 0.898 \\
1373	1.00 & Estimated & 0.960 & 0.883 \\
1374	2.00 & Oracle    & 0.945 & 0.858 \\
1375	2.00 & Estimated & 0.948 & 0.858 \\
1376	\bottomrule
1377	\end{tabular}
1378	\end{table}
1379	
1380	EC-HTE maintains coverage $\geq$94.5\% across all 8 configurations, including strong confounding ($\beta{=}2.0$, propensity range $[0.12, 0.88]$).
1381	The oracle--estimated gap is $\leq$1pp, confirming that propensity estimation error does not meaningfully degrade EC-HTE when the propensity model is correctly specified.
1382	This validates that EC-HTE is robust to confounded treatment assignment when the propensity model is correctly specified.
1383	
1384	\subsection{Empirical Comparison with Frazis--Loewenstein Correction}
1385	\label{app:fl_comparison}
1386	
1387	We empirically compare EC-HTE's confusion matrix inversion against the scalar attenuation correction of \citet{frazis2003estimating} (F-L).
1388	The F-L correction rescales the observed estimate as $\hat{\tau}_{\text{FL}} = \hat{\tau}_{\text{obs}} / (1 - 2\bar{\pi})$, where $\bar{\pi}$ is the (global or per-subgroup) misclassification rate.
1389	We test two variants: F-L \emph{scalar} (single global $\bar{\pi}$) and F-L \emph{per-subgroup} ($\pi_s$-specific rescaling).
1390	Setup: $K{=}2$, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, $\pi{=}[0.05, 0.25]$ (extreme heterogeneity), $\tau(z{=}0){=}0$, $\tau(z{=}1){=}0.3$, 100 MC runs.
1391	
1392	\begin{table}[h]
1393	\centering
1394	\caption{F-L correction vs.\ EC-HTE under heterogeneous misclassification ($\Delta\pi{=}0.20$). Both F-L variants produce \emph{higher} aggregate bias than the uncorrected estimator.}
1395	\label{tab:fl_comparison}
1396	\small
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdc9e875-57b8-4b11-9d68-add95a77014b",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "d233cafa-1d9c-414f-9c34-3347457905c9",
  "sourceToolAssistantUUID": "bdc9e875-57b8-4b11-9d68-add95a77014b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T20:12:49.933Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G6BSyVsVxSX4ye3GHjPV29`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/docs/paper/appendix.tex",
  "offset": 1396,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d233cafa-1d9c-414f-9c34-3347457905c9",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7Q2A7CuELcUsz6WGtq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6f61adba-4ef9-4b8d-bbe9-a974078fbefd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1GDg3Arc63LFQcnxqQz4C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8397,
      "cache_read_input_tokens": 70048,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8397
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 70048,
          "cache_creation_input_tokens": 8397,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8397,
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

_source line 44 · 2026-05-23T20:12:49.939Z_

<details><summary>↩ Tool result · `toolu_01G6BSyVsVxSX4ye3GHjPV29`</summary>

```text
1396	\small
1397	\begin{tabular}{lccc}
1398	\toprule
1399	Method & $|\text{Bias}|$ & RMSE & Coverage \\
1400	\midrule
1401	Oracle         & 0.045 & 0.056 & 0.943 \\
1402	Naive          & 0.062 & 0.077 & 0.858 \\
1403	Global (CM inv)& 0.064 & 0.081 & 0.938 \\
1404	HB EC-HTE      & 0.064 & 0.086 & \textbf{0.953} \\
1405	F-L Scalar     & 0.091 & 0.116 & 0.850 \\
1406	F-L Per-Subgroup & 0.112 & 0.158 & 0.838 \\
1407	\bottomrule
1408	\end{tabular}
1409	\end{table}
1410	
1411	Both F-L variants produce \emph{higher} bias and RMSE than the naive estimator (F-L per-subgroup $|\text{bias}|{=}0.112$ vs.\ naive $0.062$), demonstrating that scalar attenuation cannot substitute for confusion matrix inversion under subgroup-heterogeneous misclassification.
1412	The per-subgroup bias direction reveals the mechanism: F-L scalar over-corrects the low-error subgroup ($s_0$: mean bias ${=}+0.073$ vs.\ naive $+0.005$, a $14.6\times$ amplification), while F-L per-subgroup dramatically over-corrects the high-error subgroup ($s_1$: mean bias ${=}+0.160$).
1413	EC-HTE achieves near-zero per-subgroup bias ($s_0{:}\,{+}0.006$, $s_1{:}\,{+}0.001$) with nominal coverage (95.3\%).
1414	The root cause is structural: F-L's $1/(1{-}2\pi)$ scaling amplifies each $z$-level estimate independently, whereas CM inversion simultaneously redistributes the cross-contamination between misclassified and correctly classified observations.
1415	
1416	\subsection{End-to-End Validation with Asymmetric Confusion Matrices}
1417	\label{app:asymmetric_endtoend}
1418	
1419	We validate EC-HTE under strongly asymmetric confusion matrices ($\text{FPR}/\text{FNR}$ ratio up to $7{:}1$), simulating the error profile of GPT-4.1 on Civil Comments.
1420	Setup: $K{=}2$, $N{=}5{,}000$, $n_{\text{expert}}{=}250$; $s_0$: $\text{FPR}{=}0.05$, $\text{FNR}{=}0.02$ (low error); $s_1$: $\text{FPR}{=}0.38$, $\text{FNR}{=}0.054$ ($7{:}1$ ratio); 100 MC runs.
1421	We compare EC-HTE using the full $2{\times}2$ asymmetric CM (Remark~2) against the symmetric assumption ($\text{FPR}{=}\text{FNR}{=}\pi_s$).
1422	
1423	\begin{table}[h]
1424	\centering
1425	\caption{EC-HTE under asymmetric misclassification ($\text{FPR}/\text{FNR}$ up to $7{:}1$). The asymmetric formula improves coverage by $+1.5$pp and RMSE by $11.5\%$.}
1426	\label{tab:asymmetric_endtoend}
1427	\small
1428	\begin{tabular}{lccc}
1429	\toprule
1430	Method & $|\text{Bias}|$ & RMSE & Coverage \\
1431	\midrule
1432	Oracle              & 0.045 & 0.056 & 0.943 \\
1433	EC-HTE (asymmetric) & 0.057 & 0.074 & \textbf{0.945} \\
1434	Naive               & 0.059 & 0.073 & 0.870 \\
1435	Global (asymmetric) & 0.061 & 0.076 & 0.915 \\
1436	EC-HTE (symmetric)  & 0.062 & 0.083 & 0.930 \\
1437	Global (symmetric)  & 0.063 & 0.078 & 0.915 \\
1438	\bottomrule
1439	\end{tabular}
1440	\end{table}
1441	
1442	EC-HTE with the asymmetric formula achieves 94.5\% coverage versus 93.0\% under the symmetric assumption ($+1.5$pp), with RMSE improved from 0.083 to 0.074 ($-11.5\%$).
1443	The improvement concentrates in the high-error subgroup ($s_1$): asymmetric coverage is 93.0\% vs.\ symmetric 91.0\%.
1444	Practitioners should estimate full $2 \times 2$ confusion matrices rather than assuming symmetric misclassification, particularly when FPR and FNR differ substantially.
1445	
1446	\subsection{Complementarity with LLM Calibration}
1447	\label{app:calibration}
1448	
1449	Temperature or Platt scaling~\cite{guo2017calibration} can reduce per-subgroup misclassification rates, but does not eliminate heterogeneity $\Delta\pi$.
1450	We simulate calibration by shrinking per-subgroup rates from $\pi{=}[0.05, 0.25]$ ($\Delta\pi{=}0.20$) to $\pi{=}[0.08, 0.15]$ ($\Delta\pi{=}0.07$), testing whether EC-HTE remains necessary post-calibration.
1451	Setup: $K{=}2$, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs.
1452	
1453	\begin{table}[h]
1454	\centering
1455	\caption{Calibration reduces $\Delta\pi$ but does not eliminate it; EC-HTE corrects the residual bias. Best coverage is achieved by combining both.}
1456	\label{tab:calibration}
1457	\small
1458	\begin{tabular}{lccc}
1459	\toprule
1460	Method & $|\text{Bias}|$ & RMSE & Coverage \\
1461	\midrule
1462	Oracle                    & 0.043 & 0.053 & 0.963 \\
1463	Calibrated + EC-HTE       & 0.055 & 0.069 & \textbf{0.965} \\
1464	Calibrated + Global       & 0.055 & 0.068 & 0.963 \\
1465	Calibrated + Naive        & 0.051 & 0.064 & 0.913 \\
1466	Uncalibrated + EC-HTE     & 0.064 & 0.084 & 0.938 \\
1467	Uncalibrated + Global     & 0.069 & 0.085 & 0.920 \\
1468	Uncalibrated + Naive      & 0.063 & 0.079 & 0.840 \\
1469	\bottomrule
1470	\end{tabular}
1471	\end{table}
1472	
1473	Calibration alone improves naive coverage from 84.0\% to 91.3\% but does not reach the nominal 95\%.
1474	Calibrated + EC-HTE achieves the highest coverage (96.5\%), demonstrating that calibration and EC-HTE address complementary error sources: calibration reduces per-subgroup $\pi_s$ while EC-HTE corrects the residual $\delta_s$-driven bias from heterogeneity that persists post-calibration.
1475	Propensity estimation robustness under model misspecification is a complementary concern addressed by the IPW literature; EC-HTE as a downstream correction layer does not alter IPW behavior.
1476	
1477	\subsection{Policy Reversal Zone Analysis}
1478	\label{app:policy_reversal}
1479	
1480	When the true treatment effect is small, global correction can reverse the sign of estimated CATE---concluding a beneficial treatment is harmful---creating a \emph{policy reversal zone}.
1481	We sweep $\tau(0) \in \{0.01, 0.02, 0.03, 0.05, 0.07, 0.10\}$ under the standard DGP ($K{=}2$, extreme heterogeneity, $N{=}5{,}000$, $n_{\text{expert}}{=}250$, 100 MC runs; $\Delta\tau{=}0.30$).
1482	
1483	\begin{table}[h]
1484	\centering
1485	\caption{Policy reversal zone: fraction of configurations where global correction reverses the sign of estimated CATE.
1486	The naive estimator produces zero sign reversals across all $\tau(0)$ values; EC-HTE also achieves 0\% reversal.}
1487	\label{tab:policy_reversal}
1488	\small
1489	\begin{tabular}{ccc}
1490	\toprule
1491	$\tau(0)$ & Global reversal \% & Most extreme $\hat{\tau}_{\text{global}}$ \\
1492	\midrule
1493	0.01 & 31.0 & $-0.079$ \\
1494	0.02 & 21.6 & --- \\
1495	0.03 & 14.9 & $-0.059$ \\
1496	0.05 & 6.1  & $-0.039$ \\
1497	0.07 & 1.6  & --- \\
1498	$\geq$0.10 & 0 & --- \\
1499	\bottomrule
1500	\end{tabular}
1501	\end{table}
1502	
1503	The reversal rate increases monotonically as $\tau(0)$ decreases: at $\tau(0) = 0.01$, 31\% of configurations yield sign reversal, with the most extreme case estimating $\hat{\tau} = -0.079$ when the true effect is $\tau = +0.01$.
1504	The critical threshold is $\tau(0) < 0.089$, matching the closed-form prediction from Theorem~\ref{thm:bias_identity}: $|\delta_{\max} \cdot \Delta\tau_{\max}| / (1 - 2\bar{\pi}) = 0.125 \times 0.50 / 0.70 = 0.089$.
1505	The most dangerous combination ($\tau(0) = 0.01$, $\delta_{\text{misclass}} = 0.19$) reaches 42.9\% reversal rate.
1506	The naive estimator produces zero sign reversals across all $\tau(0)$ values, confirming that reversal is an artifact of global correction, not inherent estimation noise.
1507	
1508	Figure~\ref{fig:policy_reversal} visualizes the reversal zone across the $\Delta\pi \times \tau(0)$ parameter space.
1509	
1510	\begin{figure}[h]
1511	\centering
1512	\includegraphics[width=\columnwidth]{figures/policy_reversal_zone.pdf}
1513	\caption{Policy reversal zone: sign-reversal rate as a function of $\tau(0)$ and $\Delta\pi$. Shaded region marks configurations where global correction reverses the CATE sign, directing policy toward the wrong subgroups.}
1514	\label{fig:policy_reversal}
1515	\end{figure}
1516	
1517	\section*{Use of AI Assistants}
1518	\label{app:ai-assistants}
1519	
1520	We used Claude (Anthropic) as an AI coding and writing assistant
1521	throughout this work. Specifically:
1522	\begin{itemize}
1523	    \item \textbf{Code:} drafting experiment scripts, data-processing
1524	    pipelines, and analysis utilities; debugging and refactoring.
1525	    \item \textbf{Writing:} drafting and revising paper sections,
1526	    polishing prose, and reformatting LaTeX.
1527	    \item \textbf{Literature:} summarizing related papers to inform
1528	    the related-work section.
1529	\end{itemize}
1530	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f61adba-4ef9-4b8d-bbe9-a974078fbefd",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "d82d9017-29ff-4ab2-a02c-a8c3c678e707",
  "sourceToolAssistantUUID": "6f61adba-4ef9-4b8d-bbe9-a974078fbefd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-23T20:12:53.625Z_

Now let me also read the review context and any existing review materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d82d9017-29ff-4ab2-a02c-a8c3c678e707",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7QNTF5y81ZZJyArwrx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b50b22a-aee8-44f0-8211-08bcbb94875c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKDQESr7WMhUf83wBRvmz6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3496,
      "cache_read_input_tokens": 78445,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3496,
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

_source line 46 · 2026-05-23T20:12:54.577Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01PFbuoMVEqmZVJrnvYjDDhM`</summary>

```json
{
  "project": "ec_hte_llm_annotation",
  "file": "paper_checklist.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b50b22a-aee8-44f0-8211-08bcbb94875c",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7QNTF5y81ZZJyArwrx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9b90397-c8c2-4314-a719-1eef21edf272",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKDQESr7WMhUf83wBRvmz6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3496,
      "cache_read_input_tokens": 78445,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3496,
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

_source line 47 · 2026-05-23T20:12:54.599Z_

<details><summary>↩ Tool result · `toolu_01PFbuoMVEqmZVJrnvYjDDhM`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'ec_hte_llm_annotation'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9b90397-c8c2-4314-a719-1eef21edf272",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "1b3b728a-29bc-4640-99cc-b15a43b361f7",
  "sourceToolAssistantUUID": "e9b90397-c8c2-4314-a719-1eef21edf272",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-23T20:12:55.995Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Dp6pYob6zAbR8GmwucVqpu`</summary>

```json
{
  "pattern": "**/review_context*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b3b728a-29bc-4640-99cc-b15a43b361f7",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7QNTF5y81ZZJyArwrx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1240ebf5-3cb3-4d27-88c8-be178aca1a52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKDQESr7WMhUf83wBRvmz6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3496,
      "cache_read_input_tokens": 78445,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3496
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 78445,
          "cache_creation_input_tokens": 3496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3496,
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

_source line 49 · 2026-05-23T20:12:56.018Z_

<details><summary>↩ Tool result · `toolu_01Dp6pYob6zAbR8GmwucVqpu`</summary>

```text
artifacts/dream_reports/dream_20260520T185426/best/review_context.yaml
artifacts/dream_reports/dream_20260520T185426/median/review_context.yaml
artifacts/dream_reports/dream_20260520T185426/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T194535/best/review_context.yaml
artifacts/dream_reports/dream_20260520T194535/median/review_context.yaml
artifacts/dream_reports/dream_20260520T194535/worst/review_context.yaml
artifacts/dream_reports/dream_20260521T032758/best/review_context.yaml
artifacts/dream_reports/dream_20260521T032758/median/review_context.yaml
artifacts/dream_reports/dream_20260521T032758/worst/review_context.yaml
artifacts/dream_reports/dream_20260521T122454/best/review_context.yaml
artifacts/dream_reports/dream_20260521T122454/median/review_context.yaml
artifacts/dream_reports/dream_20260521T122454/worst/review_context.yaml
artifacts/dream_reports/dream_20260523T193110/best/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1240ebf5-3cb3-4d27-88c8-be178aca1a52",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "5b421c16-4323-41c1-aeac-0d1124553b93",
  "sourceToolAssistantUUID": "1240ebf5-3cb3-4d27-88c8-be178aca1a52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-23T20:14:24.089Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XuxY13oBRY1wBx66wXo4p2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/dream_reports/dream_20260523T193110/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b421c16-4323-41c1-aeac-0d1124553b93",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7Wxak9qZ5WGFBjsd7S",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "818c3972-976c-470e-a73f-bac82492ea68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015gePvPHYxXj9u6S6JTbFb5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 82576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 0
      },
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 82576,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "output_tokens": 104,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": {
      "applied_edits": []
    }
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-23T20:14:24.325Z_

<details><summary>↩ Tool result · `toolu_01XuxY13oBRY1wBx66wXo4p2`</summary>

```text
1	narrative_guidance: 'Reframed ''When Debiasing Hurts'' narrative fully lands. Reviewers
2	  (NLP/CSS-oriented, not deep measurement-error specialists) accept the bias identity
3	  as novel formalization in the LLM annotation context. Three-layer contribution structure
4	  — (1) exact bias identity, (2) EC-HTE as identity-prescribed correction, (3) Δπ×Δτ
5	  diagnostic — reads as coherent and complete. Honest disclosure of RMSE tradeoffs,
6	  K≥8 boundary, and real-CM negative results (exp-015/016) is perceived as mature
7	  scholarship, not weakness. Excitement 4.0-4.5 driven by ''debiasing can hurt'' surprise
8	  factor for NLP audience. Soundness 3.5-4.0 reflects minor concern about lack of
9	  convergence rates but acceptance of empirical thoroughness. No reviewer demands
10	  minimax bounds; ''problem identification + exact identity + diagnostic'' accepted
11	  as complete contribution package.
12	
13	  '
14	imagined_experiments:
15	- name: HB EC-HTE Synthetic Validation
16	  plan_id: exp-001
17	  description: 'Hierarchical Bayesian Dirichlet-prior confusion matrix estimator with
18	    partial pooling. Full regime sweep: extreme/moderate/homogeneous × n_expert={100,250,500,1000,2000}
19	    × K={2,4}. 3600 MC runs total. MCMC diagnostics: PyMC NUTS, 4 chains, 1000 warmup.
20	
21	    '
22	  expected_results:
23	    mcmc_rhat_max: 1.004
24	    mcmc_ess_min: 1618
25	    mcmc_divergent: 0
26	    total_mc_runs: 3600
27	    runtime_min: 69
28	    hb_vs_mle_rmse_improvement_k2_n50: 4-9%
29	    hb_vs_mle_rmse_improvement_k4_n50_moderate: 6-9%
30	    hb_coverage_median: 0.93
31	    hb_coverage_min: 0.87
32	    hyperprior_sensitivity_k2_variation: <1%
33	    hyperprior_sensitivity_k4_variation: ~4-5%
34	    singularity_guard_triggers: extreme/n=50 only
35	  result_rationale: 'Best tier assumes reviewers accept HB partial pooling as well-motivated
36	    James-Stein shrinkage. R̂<1.01 and ESS>200 (actual: ESS>1618 with 4-chain fix)
37	    satisfy standard MCMC convergence criteria — NLP reviewers without deep Bayesian
38	    background will see these as reassuring checkboxes. 4-9% RMSE improvement over
39	    MLE at small n is modest but directionally correct; reviewers accept this as ''partial
40	    pooling helps when data is scarce'' (classical result, applied to new setting).
41	    Coverage median 0.93 (below nominal 0.95) is disclosed honestly — reviewer sees
42	    this as boundary condition acknowledgment, not flaw. Hyperprior sensitivity <5%
43	    for K=4 confirms robustness without requiring exhaustive sensitivity analysis
44	    — one table in appendix suffices.
45	
46	    '
47	  tables:
48	  - name: 'Table A1: MCMC Diagnostics Summary'
49	    columns:
50	    - Config
51	    - R-hat (max)
52	    - ESS (min)
53	    - Divergences
54	    - Runtime (s)
55	    rows:
56	    - - K=2/extreme/n=100
57	      - '1.003'
58	      - '1842'
59	      - '0'
60	      - '68'
61	    - - K=2/moderate/n=100
62	      - '1.002'
63	      - '2105'
64	      - '0'
65	      - '65'
66	    - - K=4/extreme/n=100
67	      - '1.004'
68	      - '1618'
69	      - '0'
70	      - '82'
71	    - - K=4/moderate/n=100
72	      - '1.003'
73	      - '1790'
74	      - '0'
75	      - '79'
76	    - - K=4/extreme/n=50 (guard)
77	      - '1.003'
78	      - '1650'
79	      - '0'
80	      - '85'
81	  - name: 'Table A2: HB vs MLE RMSE Comparison'
82	    columns:
83	    - Config
84	    - HB RMSE
85	    - MLE RMSE
86	    - Improvement (%)
87	    - HB Coverage
88	    rows:
89	    - - K=2/extreme/n=50
90	      - '0.228'
91	      - '0.248'
92	      - +8.1%
93	      - '0.91'
94	    - - K=2/extreme/n=100
95	      - '0.142'
96	      - '0.145'
97	      - +2.1%
98	      - '0.93'
99	    - - K=2/extreme/n=250
100	      - '0.091'
101	      - '0.093'
102	      - +2.2%
103	      - '0.94'
104	    - - K=4/moderate/n=50
105	      - '0.195'
106	      - '0.213'
107	      - +8.5%
108	      - '0.89'
109	    - - K=4/extreme/n=50
110	      - '0.310'
111	      - '0.382'
112	      - +18.8%
113	      - '0.87'
114	    - - K=4/extreme/n=100
115	      - '0.210'
116	      - '0.225'
117	      - +6.7%
118	      - '0.92'
119	  - name: 'Table A3: Hyperprior Sensitivity (Gamma scale)'
120	    columns:
121	    - Scale
122	    - K=2 RMSE
123	    - K=4 RMSE
124	    - Coverage
125	    rows:
126	    - - 0.5x
127	      - '0.091'
128	      - '0.208'
129	      - '0.93'
130	    - - 1.0x (base)
131	      - '0.091'
132	      - '0.210'
133	      - '0.93'
134	    - - 2.0x
135	      - '0.091'
136	      - '0.219'
137	      - '0.93'
138	  figures_description:
139	  - 'Appendix figure: HB vs MLE RMSE ratio across n_expert, colored by regime. Shows
140	    convergence at n≥500.'
141	  analysis: 'Reviewers in best tier see this as thorough validation infrastructure.
142	    The 4-chain MCMC fix (resolving initial K=4/extreme/n=50 blowup) is disclosed
143	    as methodological due diligence. Key narrative: HB provides meaningful but modest
144	    improvement over MLE — the contribution is NOT ''HB is dramatically better'' but
145	    rather ''stratified correction with principled shrinkage enables reliable per-subgroup
146	    CM estimation.'' This framing aligns with the paper''s positioning as problem-identification
147	    rather than method-innovation. Reviewer concern about computational cost (69 min
148	    for full sweep) is preempted by noting this is a one-time calibration, not per-prediction
149	    cost.
150	
151	    '
152	- name: Bias Identity Verification
153	  plan_id: exp-002
154	  description: 'Formal derivation and empirical verification of bias = f(Δπ, Δτ) identity.
155	    Systematic parameter grid: Δπ ∈ {0, 0.05, ..., 0.25} × Δτ ∈ {0, 0.1, ..., 0.5}
156	    × K ∈ {2,4}. ''Debiasing can hurt'' proposition with constructive two-subgroup
157	    example. 520 non-trivial configs.
158	
159	    '
160	  expected_results:
161	    r2_k2: 0.994
162	    r2_k4: 0.974
163	    tightness_ratio_k2_median: 1.003
164	    tightness_ratio_k4_median: 1.023
165	    debiasing_hurts_pct: 50
166	    debiasing_hurts_pct_detail: 260/520 configs (excluding Δτ=0)
167	    max_bias_ratio_k2: 2.86
168	    max_bias_ratio_k4: 2.41
169	    coverage_2se_k2: 0.951
170	    coverage_2se_k4: 0.94
171	    headline_median_amplification: 2-3x
172	    headline_max_amplification: 5.9x (K=4, CausalForest, from exp-011)
173	  result_rationale: 'This is THE core contribution for best tier. R²=0.994 (K=2) and
174	    0.974 (K=4) confirm the identity is exact at population level — finite-sample
175	    noise explains remaining variance, NOT bound looseness. Best-tier reviewers accept
176	    this framing because: (1) ''bias decomposition identity'' language (not ''bound'')
177	    is technically precise, (2) tightness ratio ~1.0 means MC estimate matches analytic
178	    prediction almost exactly, (3) the 50% ''debiasing hurts'' rate is striking —
179	    it means global correction is a coin flip in terms of whether it helps or hurts
180	    across the parameter space. The ''2-3x median, up to 5.9x'' headline is calibrated:
181	    median is robust (not cherry-picked extreme), 5.9x is from CausalForest (exp-011)
182	    which amplifies via nonlinear estimation. NLP reviewers unfamiliar with Fuller/Carroll
183	    see the Δπ×Δτ product form as novel; the explicit ''this is classical in spirit
184	    but new in this specific context'' framing preempts the one reviewer who might
185	    know measurement error literature. K=2 max 2.86× vs K=4 max 2.41× (DIM) is counter-intuitive
186	    and strengthens novelty — NOT monotonic in K, demonstrating the identity captures
187	    non-trivial structure.
188	
189	    '
190	  tables:
191	  - name: 'Table 1: Bias Amplification Under Global Correction (Main Paper)'
192	    columns:
193	    - K
194	    - Δπ
195	    - Δτ
196	    - Analytic Bias
197	    - MC Bias (SE)
198	    - Ratio MC/Analytic
199	    - Global Hurts?
200	    rows:
201	    - - '2'
202	      - '0.05'
203	      - '0.1'
204	      - '0.005'
205	      - 0.005 (0.001)
206	      - '1.00'
207	      - 'No'
208	    - - '2'
209	      - '0.10'
210	      - '0.2'
211	      - '0.020'
212	      - 0.020 (0.002)
213	      - '1.00'
214	      - 'Yes'
215	    - - '2'
216	      - '0.15'
217	      - '0.3'
218	      - '0.045'
219	      - 0.046 (0.003)
220	      - '1.02'
221	      - 'Yes'
222	    - - '2'
223	      - '0.20'
224	      - '0.5'
225	      - '0.100'
226	      - 0.101 (0.005)
227	      - '1.01'
228	      - 'Yes'
229	    - - '2'
230	      - '0.25'
231	      - '0.5'
232	      - '0.125'
233	      - 0.127 (0.006)
234	      - '1.02'
235	      - 'Yes'
236	    - - '4'
237	      - '0.10'
238	      - '0.2'
239	      - '0.020'
240	      - 0.021 (0.003)
241	      - '1.05'
242	      - 'Yes'
243	    - - '4'
244	      - '0.20'
245	      - '0.5'
246	      - '0.100'
247	      - 0.103 (0.008)
248	      - '1.03'
249	      - 'Yes'
250	  - name: 'Table 2: Debiasing-Hurts Summary Statistics'
251	    columns:
252	    - Estimator
253	    - K
254	    - Max Amplification
255	    - Median Amplification
256	    - Hurts Rate (%)
257	    rows:
258	    - - DIM
259	      - '2'
260	      - 2.86x
261	      - 2.1x
262	      - 50%
263	    - - DIM
264	      - '4'
265	      - 2.41x
266	      - 1.8x
267	      - 50%
268	    - - CausalForest
269	      - '2'
270	      - 3.2x
271	      - 2.3x
272	      - 50%
273	    - - CausalForest
274	      - '4'
275	      - 5.9x
276	      - 3.1x
277	      - 50%
278	  figures_description:
279	  - 'Figure 1 (Main): Bias amplification heatmap — Δπ (x-axis) vs Δτ (y-axis), color
280	    = amplification ratio. Clear product-structure gradient. White diagonal = amplification
281	    = 1.0 boundary.'
282	  - 'Figure 2 (Main): Constructive ''debiasing hurts'' example — two-subgroup case
283	    showing over-correction in low-error subgroup, under-correction in high-error
284	    subgroup. Schematic + MC verification overlay.'
285	  analysis: 'Best tier reviewers rate this 4.0-4.5 excitement because the ''debiasing
286	    can hurt'' framing is genuinely surprising to NLP audience. Most NLP papers assume
287	    correction monotonically improves estimates; showing 50% failure rate across parameter
288	    space is a ''stop and think'' result. The exact identity (not a bound) is clean
289	    enough to be stated as Theorem 1 in under 5 lines. R² > 0.97 across all K values
290	    makes the empirical verification convincing without requiring formal convergence
291	    rate proofs. One reviewer may note the classical measurement error parallel (Fuller
292	    1987 Sec 2.3) — the explicit citation and ''new in LLM context'' framing deflects
293	    this to a minor comment rather than a novelty objection.
294	
295	    '
296	- name: Semi-Synthetic CSS Benchmark
297	  plan_id: exp-003
298	  description: 'TweetEval sentiment (N=45K). Inject known CATE heterogeneity, annotate
299	    with GPT-4.1. K=4 subgroups (text features: has_hashtag × text_length). 100 MC
300	    runs with HB integration. Methods: oracle, naive, global_corrected, stratified_mle,
301	    hb_ec_hte.
302	
303	    '
304	  expected_results:
305	    n_subgroups: 4
306	    misclass_rates: S0=0.05, S1=0.10, S2=0.15, S3=0.25
307	    delta_pi: 0.2
308	    debiasing_hurts_confirmed: true
309	    mc_runs: 100
310	    hb_vs_mle_n100_S3_extreme: +60% RMSE improvement (HB dramatically better)
311	    hb_vs_mle_n100_S2: +5-8% RMSE improvement
312	    hb_vs_mle_n250_S3: +5-17% RMSE improvement
313	    hb_vs_mle_n500: converged (<1.6% difference)
314	    boundary_condition: n=50 with extreme heterogeneity in tiny subgroups (S3=12%)
315	      shows moderate degradation
316	    hb_n50_S3_degradation: -57% RMSE (HB worse but not catastrophic)
317	  result_rationale: 'Semi-synthetic design validates the bias identity in a realistic
318	    annotation pipeline: GPT-4.1 on TweetEval sentiment produces genuine subgroup-varying
319	    misclassification (Δπ=0.20), not synthetic noise injection. Best-tier reviewers
320	    accept this because: (1) the DGP is fully specified (outcome generation + treatment
321	    assignment + CATE injection), satisfying the ''semi-synthetic transparency'' requirement,
322	    (2) Δπ=0.20 matches the exp-012 pilot finding (Δπ=0.200 from GPT-4.1), confirming
323	    the heterogeneity is real, not assumed, (3) the +60% RMSE improvement at n=100/S3
324	    demonstrates HB''s value precisely where it matters most — the high-error minority
325	    subgroup. The n=50 degradation is disclosed honestly and positioned as a boundary
326	    condition, not a failure. NLP reviewers see ''real LLM + real corpus'' as strong
327	    validation even though CATEs are injected. The 12% minority subgroup size (S2,
328	    S3) maps to realistic CSS scenarios (e.g., minority demographic groups in survey
329	    data).
330	
331	    '
332	  tables:
333	  - name: 'Table 3: Semi-Synthetic Benchmark Results (Main Paper)'
334	    columns:
335	    - Method
336	    - Subgroup
337	    - n_expert
338	    - '|Bias|'
339	    - RMSE
340	    - Coverage
341	    rows:
342	    - - Oracle
343	      - All
344	      - '-'
345	      - '0.003'
346	      - '0.045'
347	      - '0.96'
348	    - - Naive
349	      - S3 (high-error)
350	      - '-'
351	      - '0.089'
352	      - '0.109'
353	      - '0.82'
354	    - - Global Corrected
355	      - S3 (high-error)
356	      - '-'
357	      - '0.142'
358	      - '0.165'
359	      - '0.78'
360	    - - Stratified MLE
361	      - S3 (high-error)
362	      - '100'
363	      - '0.038'
364	      - '0.195'
365	      - '0.91'
366	    - - HB EC-HTE
367	      - S3 (high-error)
368	      - '100'
369	      - '0.015'
370	      - '0.078'
371	      - '0.93'
372	    - - HB EC-HTE
373	      - S3 (high-error)
374	      - '250'
375	      - '0.008'
376	      - '0.062'
377	      - '0.94'
378	    - - HB EC-HTE
379	      - S3 (high-error)
380	      - '500'
381	      - '0.004'
382	      - '0.051'
383	      - '0.95'
384	    - - Global Corrected
385	      - S0 (low-error)
386	      - '-'
387	      - '0.067'
388	      - '0.082'
389	      - '0.85'
390	    - - HB EC-HTE
391	      - S0 (low-error)
392	      - '100'
393	      - '0.005'
394	      - '0.048'
395	      - '0.94'
396	  - name: 'Table A4: Debiasing Hurts in Semi-Synthetic Setting'
397	    columns:
398	    - Subgroup
399	    - Naive |Bias|
400	    - Global |Bias|
401	    - Amplification
402	    - Direction
403	    rows:
404	    - - S0 (π=0.05)
405	      - '0.012'
406	      - '0.067'
407	      - 5.6x
408	      - Over-corrected
409	    - - S1 (π=0.10)
410	      - '0.035'
411	      - '0.048'
412	      - 1.4x
413	      - Over-corrected
414	    - - S2 (π=0.15)
415	      - '0.058'
416	      - '0.052'
417	      - 0.9x
418	      - Slight improvement
419	    - - S3 (π=0.25)
420	      - '0.089'
421	      - '0.142'
422	      - 1.6x
423	      - Under-corrected
424	  figures_description:
425	  - 'Figure 3 (Main): Per-subgroup bias comparison — grouped bar chart, naive vs global
426	    vs EC-HTE, showing over/under-correction pattern in global, near-zero in EC-HTE.'
427	  analysis: 'The semi-synthetic benchmark is the paper''s empirical centerpiece. Best-tier
428	    reviewers see the ''global hurts S0 by 5.6×'' result as the most compelling instantiation
429	    of the bias identity — a low-error subgroup gets WORSE after correction, which
430	    is exactly the failure mode the paper identifies. The progression from n=50 (HB
431	    struggles) to n=100 (HB wins) to n=500 (converged) maps cleanly to the budget
432	    guidance in exp-006. Honest disclosure of n=50 boundary makes the n≥100 recommendation
433	    credible.
434	
435	    '
436	- name: Real-Data Case Study (Pattern Consistency)
437	  plan_id: exp-004
438	  description: 'UC Berkeley Measuring Hate Speech corpus. N=2496 comments. GPT-4.1
439	    annotation. Subgroups: platform_group × text_length (K=4). Pattern consistency
440	    analysis, NOT ground-truth CATE benchmark. Bootstrap CIs on point estimate differences.
441	
442	    '
443	  expected_results:
444	    dataset: UC Berkeley Measuring Hate Speech
445	    n_comments: 2496
446	    delta_pi: 0.117
447	    global_FPR: 0.139
448	    global_FNR: 0.533
449	    misclass_range: 0.266 - 0.383
450	    echte_vs_global_avg_bias: EC-HTE does not outperform global (high FNR limits correction)
451	    key_pattern: Δπ=0.117 confirms real-world heterogeneity exists
452	    honest_limitation: High FNR (53%) makes CM near-singular for positive class
453	  result_rationale: 'This is a negative/mixed result that STRENGTHENS the best-tier
454	    narrative. The real-data case shows: (1) misclassification heterogeneity exists
455	    in real LLM annotation (Δπ=0.117, statistically significant), validating the premise
456	    that global correction is mis-specified in practice, (2) EC-HTE does NOT outperform
457	    when FNR≈53% (near-random for positive class) — this connects to the honest boundary
458	    condition from exp-015/016 and the ''classifier quality threshold'' limitation.
459	    Best-tier reviewers see this as mature scholarship: the authors don''t cherry-pick
460	    favorable datasets, they show where the method works AND where it doesn''t, and
461	    explain WHY (near-singular CM). The ''pattern consistency, not ground-truth benchmark''
462	    framing is accepted because reviewers agree no ground-truth CATE exists for observational
463	    data.
464	
465	    '
466	  tables:
467	  - name: 'Table 4: Real-Data Misclassification Heterogeneity (Main Paper)'
468	    columns:
469	    - Subgroup
470	    - n
471	    - FPR
472	    - FNR
473	    - Overall Misclass Rate
474	    rows:
475	    - - plat0_long
476	      - '624'
477	      - '0.08'
478	      - '0.58'
479	      - '0.266'
480	    - - plat0_short
481	      - '624'
482	      - '0.12'
483	      - '0.62'
484	      - '0.337'
485	    - - plat23_long
486	      - '624'
487	      - '0.10'
488	      - '0.55'
489	      - '0.303'
490	    - - plat23_short
491	      - '624'
492	      - '0.15'
493	      - '0.59'
494	      - '0.383'
495	    - - Global (pooled)
496	      - '2496'
497	      - '0.139'
498	      - '0.533'
499	      - '0.322'
500	  - name: 'Table A5: Real-Data CATE Comparison'
501	    columns:
502	    - Method
503	    - Avg |Bias|
504	    - Bootstrap 95% CI Width
505	    - Note
506	    rows:
507	    - - Naive
508	      - '0.210'
509	      - '0.18'
510	      - Baseline
511	    - - Global Corrected
512	      - '0.273'
513	      - '0.22'
514	      - FNR=53% amplifies noise
515	    - - EC-HTE
516	      - '0.313'
517	      - '0.31'
518	      - Wide CIs due to near-singular CM
519	    - - Note
520	      - '-'
521	      - '-'
522	      - No ground-truth CATE; pattern comparison only
523	  figures_description:
524	  - 'Appendix figure: Per-subgroup misclassification rate bar chart with 95% bootstrap
525	    CIs, showing statistically significant heterogeneity.'
526	  analysis: 'Best-tier reviewers (70-85% accept EC-HTE as useful) interpret this correctly:
527	    the negative real-data result is a feature, not a bug. It demonstrates the diagnostic
528	    criterion''s value — a practitioner would compute Δπ=0.117 and FNR=0.533, conclude
529	    the classifier quality is insufficient for stratified correction, and stick with
530	    global correction or improve the classifier. This directly validates Claim 3 (diagnostic)
531	    by showing a real scenario where the diagnostic would correctly advise AGAINST
532	    EC-HTE. Reviewers note the honest framing approvingly: ''the authors show both
533	    success and failure cases.'' Revision request: one reviewer asks for a second
534	    real dataset with lower FNR to show EC-HTE working — this is classified as minor
535	    revision.
536	
537	    '
538	- name: Diagnostic Criterion Validation
539	  plan_id: exp-005
540	  description: 'Compute Δπ × Δτ product from pilot data across all experimental settings.
541	    ROC analysis of threshold for predicting when global correction fails. Cross-validated
542	    (NOT in-sample) AUC.
543	
544	    '
545	  expected_results:
546	    subgroup_level_auc: 0.833
547	    subgroup_correlation: 0.86
548	    setting_level_auc: 0.49
549	    low_pi_hurt_pct: 84.6
550	    high_pi_hurt_pct: 15.4
551	    theory_alignment: consistent with exp-002 formula
552	  result_rationale: 'Subgroup-level AUC=0.833 is strong for a zero-cost diagnostic.
553	    Best-tier reviewers accept this as ''useful practical tool'' (65-80% acceptance
554	    range). The setting-level AUC=0.49 (near random) is an honest disclosure — the
555	    diagnostic works at the subgroup level (predicting WHICH subgroups get hurt) but
556	    not at the setting level (predicting WHETHER any subgroup gets hurt). This is
557	    theoretically consistent: the bias identity is a per-subgroup statement (each
558	    subgroup has its own Δπ_k × Δτ_k), not a global statement. Reviewers see this
559	    distinction as demonstrating understanding of the theory''s scope. The 84.6% hurt
560	    rate for low-Δπ subgroups vs 15.4% for high-Δπ subgroups confirms the asymmetry
561	    predicted by the identity: low-error subgroups are over-corrected by global pooling.
562	    This is the ''debiasing hurts'' mechanism in action.
563	
564	    '
565	  tables:
566	  - name: 'Table 5: Diagnostic Criterion Performance (Main Paper)'
567	    columns:
568	    - Level
569	    - AUC
570	    - Correlation
571	    - Precision@80%Recall
572	    - Note
573	    rows:
574	    - - Subgroup-level
575	      - '0.833'
576	      - '0.86'
577	      - '0.79'
578	      - Primary diagnostic
579	    - - Setting-level
580	      - '0.49'
581	      - '0.12'
582	      - '0.51'
583	      - Near random (expected)
584	  - name: 'Table A6: Diagnostic by Subgroup Δπ Quartile'
585	    columns:
586	    - Δπ Quartile
587	    - Hurt Rate (%)
588	    - Mean Amplification
589	    - Diagnostic Recommendation
590	    rows:
591	    - - Q1 (lowest Δπ)
592	      - 84.6%
593	      - 2.8x
594	      - 'Flag: likely over-corrected'
595	    - - Q2
596	      - 62.3%
597	      - 1.6x
598	      - 'Caution: mixed'
599	    - - Q3
600	      - 38.1%
601	      - 0.9x
602	      - 'OK: near breakeven'
603	    - - Q4 (highest Δπ)
604	      - 15.4%
605	      - 0.5x
606	      - 'Safe: under-corrected, global helps'
607	  figures_description:
608	  - 'Figure 4 (Main): Diagnostic ROC curve at subgroup level with AUC=0.833. Annotated
609	    operating point at 80% recall.'
610	  - 'Appendix figure: Scatter plot of Δπ×Δτ product vs actual bias amplification,
611	    showing strong subgroup-level correlation (r=0.86).'
612	  analysis: 'Best-tier reviewers (65-80% acceptance for diagnostic) see AUC=0.833
613	    as ''good enough for practical use.'' The key selling point is zero cost — the
614	    diagnostic requires only a pilot confusion matrix, which practitioners already
615	    compute. Even without adopting EC-HTE, knowing when global correction backfires
616	    has standalone value. The setting-level AUC=0.49 is a limitation that reviewers
617	    note but don''t penalize heavily, because the subgroup-level diagnostic is what
618	    matters for the ''which subgroups to worry about'' decision. One reviewer may
619	    request cross-validation details — this is a minor revision request.
620	
621	    '
622	- name: Expert Label Budget Sensitivity
623	  plan_id: exp-006
624	  description: 'Systematic sweep: n_expert ∈ {50,100,250,500,1000,2000} × K ∈ {2,4}
625	    × regime ∈ {extreme,moderate}. Find RMSE crossover where EC-HTE beats global.
626	    288 total configs, 100 MC runs each.
627	
628	    '
629	  expected_results:
630	    total_configs: 288
631	    runtime_min: 110
632	    crossover_K2_extreme: 250
633	    crossover_K2_moderate: never (global always better on RMSE)
634	    crossover_K4_extreme: 1000
635	    crossover_K4_moderate: 2000
636	    hb_beats_mle_pct: 87.5% (21/24 configs)
637	    convergence_threshold: 'n≥1000: HB ≈ MLE (<0.5%)'
638	    best_hb_improvement: 'K=4/moderate/n=50/sgC: +42.4% RMSE over MLE'
639	  result_rationale: 'Budget sensitivity is critical for Claim 2 acceptance (70-85%
640	    in best tier). The crossover points provide actionable guidance: K=2/extreme at
641	    n=250 is practical (typical CSS study can afford 250 expert labels), K=4/extreme
642	    at n=1000 is feasible but expensive. The ''K=2/moderate never crosses'' result
643	    is an honest limitation that HELPS the narrative — it connects directly to Claim
644	    3 (diagnostic): when heterogeneity is moderate, the diagnostic correctly advises
645	    against EC-HTE. Best-tier reviewers see this as ''the method knows when to use
646	    itself.'' The 87.5% HB≥MLE rate confirms partial pooling rarely hurts (James-Stein
647	    guarantee in symmetric DGP). Convergence at n≥1000 shows HB advantage is most
648	    valuable in the data-scarce regime where it matters most.
649	
650	    '
651	  tables:
652	  - name: 'Table 6: Expert Budget Crossover Points (Main Paper)'
653	    columns:
654	    - K
655	    - Regime
656	    - Crossover n_expert
657	    - HB RMSE at Crossover
658	    - Global RMSE at Crossover
659	    rows:
660	    - - '2'
661	      - Extreme
662	      - '250'
663	      - '0.091'
664	      - '0.095'
665	    - - '2'
666	      - Moderate
667	      - Never
668	      - '-'
669	      - '-'
670	    - - '4'
671	      - Extreme
672	      - '1000'
673	      - '0.068'
674	      - '0.072'
675	    - - '4'
676	      - Moderate
677	      - '2000'
678	      - '0.055'
679	      - '0.058'
680	  - name: 'Table A7: Full Budget Sweep'
681	    columns:
682	    - n_expert
683	    - K
684	    - Regime
685	    - HB RMSE
686	    - MLE RMSE
687	    - Global RMSE
688	    - HB Wins?
689	    rows:
690	    - - '50'
691	      - '2'
692	      - extreme
693	      - '0.228'
694	      - '0.248'
695	      - '0.105'
696	      - vs MLE yes, vs Global no
697	    - - '100'
698	      - '2'
699	      - extreme
700	      - '0.142'
701	      - '0.145'
702	      - '0.098'
703	      - vs MLE yes, vs Global no
704	    - - '250'
705	      - '2'
706	      - extreme
707	      - '0.091'
708	      - '0.093'
709	      - '0.095'
710	      - Both
711	    - - '500'
712	      - '2'
713	      - extreme
714	      - '0.072'
715	      - '0.073'
716	      - '0.092'
717	      - Both
718	    - - '50'
719	      - '4'
720	      - extreme
721	      - '0.310'
722	      - '0.382'
723	      - '0.128'
724	      - vs MLE yes
725	    - - '250'
726	      - '4'
727	      - extreme
728	      - '0.135'
729	      - '0.140'
730	      - '0.110'
731	      - vs MLE yes
732	    - - '1000'
733	      - '4'
734	      - extreme
735	      - '0.068'
736	      - '0.069'
737	      - '0.072'
738	      - Both
739	  figures_description:
740	  - 'Figure 5 (Main): Budget crossover curves — RMSE (y-axis) vs n_expert (x-axis),
741	    separate lines for HB/MLE/Global, faceted by K×regime. Crossover points annotated.'
742	  analysis: 'Best-tier reviewers want actionable budget guidance. The ''Expert Budget
743	    Recommendation'' subsection distills this: ''For K=2 with high heterogeneity,
744	    250 expert labels suffice. For K=4, budget 1000. When diagnostic indicates moderate
745	    heterogeneity, global correction is the safer choice.'' This connects Claims 2
746	    and 3 into a coherent decision framework. The HB vs MLE comparison (87.5% HB wins)
747	    is a secondary but reassuring result — it justifies the Bayesian machinery over
748	    simpler alternatives.
749	
750	    '
751	- name: PPCI + DSL Baseline Comparison
752	  plan_id: exp-007
753	  description: 'Four DGPs: A (covariate-only error), B (outcome-only error), C (both
754	    errors), D (no error). 8 methods including EC-HTE, PPCI, EC-HTE+PPCI composition,
755	    DSL per-subgroup. 6912 total rows, 100 MC runs per config.
756	
757	    '
758	  expected_results:
759	    total_rows: 6912
760	    dgps:
761	    - A_covariate_only
762	    - B_outcome_only
763	    - C_both_errors
764	    - D_no_error
765	    methods: 8
766	    dgp_c_extreme_n250_k2_ec_hte_ppci_bias: 0.005
767	    dgp_c_extreme_n250_k2_ec_hte_bias: 0.178
768	    dgp_c_extreme_n250_k2_ppci_bias: 0.004
769	    dgp_c_extreme_n250_k2_naive_bias: 0.251
770	    bias_reduction_composition_vs_echte: 35x
771	    coverage_ec_hte_ppci: 1.0
772	    dgp_a_ec_hte_ppci_equals_ec_hte: true
773	  result_rationale: 'The PPCI composition result is the paper''s strongest empirical
774	    finding for best tier. EC-HTE+PPCI achieves near-zero bias (0.005) in DGP C —
775	    a 35× improvement over EC-HTE alone. This proves ''necessary and sufficient in
776	    composition'': EC-HTE handles structured covariate error, PPCI rectifier handles
777	    outcome error, composition handles both. Best-tier reviewers (NLP-oriented) see
778	    this as a complete pipeline solution: LLM annotation introduces BOTH error types,
779	    and the composition addresses both. The DGP A control (EC-HTE+PPCI = EC-HTE) confirms
780	    no double-correction — PPCI correctly contributes nothing when there''s no outcome
781	    error. DGP D (no error) confirms all methods reduce to oracle. The ''pure covariate-error''
782	    control (DGP A) demonstrates EC-HTE''s structural advantage: PPCI alone has higher
783	    variance because it treats covariate error as a generic black-box correction,
784	    while EC-HTE exploits the mixing matrix structure.
785	
786	    '
787	  tables:
788	  - name: 'Table 7: Method Comparison Across Error Types (Main Paper)'
789	    columns:
790	    - DGP
791	    - Method
792	    - '|Bias| (z0)'
793	    - RMSE (z0)
794	    - Coverage
795	    rows:
796	    - - A (cov only)
797	      - EC-HTE
798	      - '0.008'
799	      - '0.089'
800	      - '0.94'
801	    - - A (cov only)
802	      - PPCI
803	      - '0.045'
804	      - '0.132'
805	      - '0.88'
806	    - - A (cov only)
807	      - EC-HTE+PPCI
808	      - '0.008'
809	      - '0.089'
810	      - '0.94'
811	    - - B (out only)
812	      - EC-HTE
813	      - '0.085'
814	      - '0.112'
815	      - '0.87'
816	    - - B (out only)
817	      - PPCI
818	      - '0.006'
819	      - '0.098'
820	      - '0.95'
821	    - - B (out only)
822	      - EC-HTE+PPCI
823	      - '0.005'
824	      - '0.095'
825	      - '0.96'
826	    - - C (both)
827	      - Naive
828	      - '0.251'
829	      - '0.269'
830	      - '0.72'
831	    - - C (both)
832	      - EC-HTE
833	      - '0.178'
834	      - '0.226'
835	      - '0.83'
836	    - - C (both)
837	      - PPCI
838	      - '0.004'
839	      - '0.261'
840	      - '0.91'
841	    - - C (both)
842	      - EC-HTE+PPCI
843	      - '0.005'
844	      - '0.225'
845	      - '1.00'
846	    - - D (none)
847	      - All methods
848	      - ~0.002
849	      - ~0.045
850	      - ~0.95
851	  - name: 'Table A8: DSL Per-Subgroup Baseline'
852	    columns:
853	    - Config
854	    - DSL |Bias|
855	    - EC-HTE |Bias|
856	    - DSL RMSE
857	    - EC-HTE RMSE
858	    rows:
859	    - - K=2/extreme/n=250
860	      - '0.015'
861	      - '0.008'
862	      - '0.115'
863	      - '0.089'
864	    - - K=2/extreme/n=500
865	      - '0.010'
866	      - '0.005'
867	      - '0.085'
868	      - '0.072'
869	    - - K=4/extreme/n=500
870	      - '0.022'
871	      - '0.012'
872	      - '0.142'
873	      - '0.120'
874	  figures_description:
875	  - 'Appendix figure: 2×2 grid of DGP panels showing method performance. Highlights
876	    EC-HTE+PPCI dominance in DGP C.'
877	  analysis: 'Best-tier reviewers see the composition result as elevating the contribution
878	    from ''yet another correction method'' to ''principled framework for LLM annotation
879	    pipelines.'' The EC-HTE+PPCI composition addresses the realistic scenario where
880	    both covariate and outcome errors coexist — which is the default in LLM annotation.
881	    The DSL comparison shows EC-HTE''s structural advantage (mixing matrix exploitation
882	    + shrinkage) over generic per-subgroup correction. Reviewer concern about ''just
883	    use PPCI'' is preempted by DGP A results: PPCI alone has higher variance when
884	    error is purely covariate-side.
885	
886	    '
887	- name: Multiple LLM Annotator Comparison
888	  plan_id: exp-008
889	  description: 'Six OpenAI models: GPT-3.5-turbo, GPT-4-turbo, GPT-4o, GPT-4o-mini,
890	    GPT-4.1, GPT-5.4. TweetEval sentiment. Measure per-subgroup misclassification
891	    heterogeneity across models. Test structural persistence of heterogeneity.
892	
893	    '
894	  expected_results:
895	    models_completed: 6
896	    all_delta_pi_above_005: true
897	    effective_delta_pi_range: 0.080 - 0.198
898	    worst_subgroup_consensus: True_medium (5/6 models)
899	    spearman_significant_pairs: 4
900	    gpt35_delta_pi: 0.198
901	    gpt41_delta_pi: 0.098
902	    gpt4o_delta_pi: 0.08
903	    gpt5x_delta_pi: 0.114
904	  result_rationale: 'This experiment validates the paper''s core premise: misclassification
905	    heterogeneity is STRUCTURAL, not model-specific. All 6 models across 3 generations
906	    (GPT-3.5 through GPT-5.4) show Δπ > 0.05 — the threshold where the bias identity
907	    predicts meaningful amplification. Best-tier reviewers see this as strong evidence
908	    that the problem won''t ''go away with better models.'' The worst-subgroup consensus
909	    (True_medium, 5/6 models) suggests text features driving misclassification are
910	    stable across architectures. The Spearman correlations (4 significant pairs) show
911	    error patterns are correlated across models — the same subgroups are hard for
912	    all LLMs. This is a P1 experiment that moves to appendix but provides crucial
913	    evidence for the ''this matters in practice'' argument. Best-tier reviewers cite
914	    this as supporting evidence when rating practical significance.
915	
916	    '
917	  tables:
918	  - name: 'Table A9: Cross-Model Misclassification Heterogeneity (Appendix)'
919	    columns:
920	    - Model
921	    - Overall Accuracy
922	    - Effective Δπ
923	    - Worst Subgroup
924	    - Best Subgroup
925	    rows:
926	    - - GPT-3.5-turbo
927	      - '0.78'
928	      - '0.198'
929	      - True_medium (0.39)
930	      - False_medium (0.10)
931	    - - GPT-4-turbo
932	      - '0.83'
933	      - '0.149'
934	      - True_medium (0.28)
935	      - False_medium (0.08)
936	    - - GPT-4o
937	      - '0.85'
938	      - '0.080'
939	      - True_medium (0.22)
940	      - False_medium (0.07)
941	    - - GPT-4o-mini
942	      - '0.82'
943	      - '0.136'
944	      - True_medium (0.30)
945	      - False_medium (0.09)
946	    - - GPT-4.1
947	      - '0.86'
948	      - '0.098'
949	      - True_medium (0.24)
950	      - False_short (0.07)
951	    - - GPT-5.4
952	      - '0.84'
953	      - '0.114'
954	      - True_medium (0.26)
955	      - False_medium (0.08)
956	  figures_description:
957	  - 'Appendix figure: Grouped bar chart of Δπ across 6 models, with horizontal line
958	    at Δπ=0.05 threshold. All bars above threshold.'
959	  analysis: 'Moved to appendix per paper framing guidelines. But best-tier reviewers
960	    reference it in reviews: ''The multi-model analysis convincingly demonstrates
961	    that heterogeneity is structural.'' The fact that even GPT-5.4 shows Δπ=0.114
962	    preempts the ''future models will fix this'' objection.
963	
964	    '
965	- name: Adaptive Expert Annotation Allocation
966	  plan_id: exp-009
967	  description: 'CATE-weighted allocation targeting high-CATE × high-error subgroups.
968	    Compare against uniform and uncertainty-only allocation. Stage 3 experiment —
969	    builds on exp-001 infrastructure and exp-006 budget analysis.
970	
971	    '
972	  expected_results:
973	    allocation_strategies:
974	    - uniform
975	    - uncertainty_only
976	    - cate_weighted
977	    uniform_rmse_k4_n500: 0.12
978	    uncertainty_rmse_k4_n500: 0.105
979	    cate_weighted_rmse_k4_n500: 0.095
980	    cate_weighted_improvement_vs_uniform: ~21%
981	    cate_weighted_improvement_vs_uncertainty: ~10%
982	    effective_crossover_reduction: Reduces K=4 crossover from n=1000 to ~700
983	    coverage_all_strategies: 0.92-0.95
984	  result_rationale: 'P2 experiment — appendix material. Under best tier, reviewers
985	    see adaptive allocation as a nice-to-have extension that demonstrates the framework''s
986	    practical flexibility. The 21% RMSE improvement over uniform allocation is meaningful
987	    but not dramatic — it confirms that allocation matters but doesn''t change the
988	    paper''s main conclusions. The ''reduces crossover from n=1000 to ~700'' result
989	    tightens the budget guidance from exp-006 but is incremental. Best-tier reviewers
990	    mention this favorably in ''additional contributions'' but don''t weight it heavily
991	    in their overall assessment. The CATE-weighted strategy''s advantage comes from
992	    concentrating expert labels where both error and effect heterogeneity are highest
993	    — this is a direct application of the Δπ×Δτ diagnostic (Claim 3) to allocation,
994	    creating a nice conceptual link.
995	
996	    '
997	  tables:
998	  - name: 'Table A10: Allocation Strategy Comparison (Appendix)'
999	    columns:
1000	    - Strategy
1001	    - K
1002	    - n_expert
1003	    - RMSE
1004	    - Coverage
1005	    - Crossover n
1006	    rows:
1007	    - - Uniform
1008	      - '4'
1009	      - '500'
1010	      - '0.120'
1011	      - '0.93'
1012	      - '1000'
1013	    - - Uncertainty-only
1014	      - '4'
1015	      - '500'
1016	      - '0.105'
1017	      - '0.93'
1018	      - '850'
1019	    - - CATE-weighted
1020	      - '4'
1021	      - '500'
1022	      - '0.095'
1023	      - '0.94'
1024	      - '700'
1025	    - - Uniform
1026	      - '2'
1027	      - '250'
1028	      - '0.091'
1029	      - '0.94'
1030	      - '250'
1031	    - - CATE-weighted
1032	      - '2'
1033	      - '250'
1034	      - '0.082'
1035	      - '0.94'
1036	      - '180'
1037	  figures_description:
1038	  - 'Appendix figure: Budget crossover curves under different allocation strategies,
1039	    showing leftward shift with CATE-weighted allocation.'
1040	  analysis: 'P2 experiment positioned as ''practical extension.'' Best-tier reviewers
1041	    note it approvingly but don''t consider it a core contribution. One reviewer may
1042	    suggest this as future work rather than appendix material — minor framing decision,
1043	    not a weakness.
1044	
1045	    '
1046	- name: Robustness to Misspecified Subgroup Structure
1047	  plan_id: exp-010
1048	  description: 'Test EC-HTE when subgroups are noisy/overlapping. Noise levels: 0%,
1049	    10%, 25%, 50% subgroup misassignment. K={2,4}. Coverage as decisive metric.
1050	
1051	    '
1052	  expected_results:
1053	    noise_levels:
1054	    - 0
1055	    - 0.1
1056	    - 0.25
1057	    - 0.5
1058	    total_runs: 800
1059	    k2_coverage_hb_range: 0.945 - 0.958
1060	    k4_coverage_hb_range: 0.946 - 0.960
1061	    k2_coverage_naive_range: 0.875 - 0.897
1062	    hb_beats_mle_all_configs: true
1063	    graceful_convergence_at_50pct: true
1064	    coverage_drop_0_to_50_noise: -1.3pp (K=2), -1.0pp (K=4)
1065	  result_rationale: 'Robustness is essential for reviewer acceptance of Claim 2 (70-85%
1066	    range). The key result is graceful degradation: EC-HTE coverage drops only ~1pp
1067	    from 0% to 50% noise, while maintaining nominal coverage (>94.5%) at all noise
1068	    levels. This directly addresses reviewer concern #4 (''how sensitive to subgroup
1069	    definition?'') with a quantitative answer: ''not very.'' The mechanism is HB partial
1070	    pooling — at 50% noise, subgroups are essentially random, and HB automatically
1071	    shrinks toward global (its prior), recovering global correction''s behavior. This
1072	    is the James-Stein guarantee in action: ''never much worse than the shrinkage
1073	    target.'' Naive coverage (87-90%) is consistently below nominal, confirming that
1074	    misclassification bias — not subgroup misspecification — is the dominant source
1075	    of coverage failure. Best-tier reviewers see this robustness analysis as demonstrating
1076	    methodological maturity.
1077	
1078	    '
1079	  tables:
1080	  - name: 'Table A11: Robustness to Subgroup Noise (Appendix)'
1081	    columns:
1082	    - Noise (%)
1083	    - K
1084	    - HB Coverage
1085	    - Global Coverage
1086	    - Naive Coverage
1087	    - HB RMSE
1088	    rows:
1089	    - - 0%
1090	      - '2'
1091	      - '0.958'
1092	      - '0.925'
1093	      - '0.875'
1094	      - '0.089'
1095	    - - 10%
1096	      - '2'
1097	      - '0.948'
1098	      - '0.935'
1099	      - '0.877'
1100	      - '0.092'
1101	    - - 25%
1102	      - '2'
1103	      - '0.950'
1104	      - '0.932'
1105	      - '0.890'
1106	      - '0.094'
1107	    - - 50%
1108	      - '2'
1109	      - '0.945'
1110	      - '0.945'
1111	      - '0.897'
1112	      - '0.096'
1113	    - - 0%
1114	      - '4'
1115	      - '0.956'
1116	      - '0.930'
1117	      - '0.904'
1118	      - '0.120'
1119	    - - 10%
1120	      - '4'
1121	      - '0.958'
1122	      - '0.953'
1123	      - '0.916'
1124	      - '0.122'
1125	    - - 25%
1126	      - '4'
1127	      - '0.960'
1128	      - '0.948'
1129	      - '0.909'
1130	      - '0.125'
1131	    - - 50%
1132	      - '4'
1133	      - '0.946'
1134	      - '0.944'
1135	      - '0.919'
1136	      - '0.128'
1137	  figures_description:
1138	  - 'Appendix figure: Coverage vs noise level, showing EC-HTE flat near 95% while
1139	    naive degrades. HB converges to global at 50% noise.'
1140	  analysis: 'Best-tier reviewers use this to rebut their own concern about subgroup
1141	    sensitivity. The ''automatic shrinkage to global at high noise'' property is intellectually
1142	    satisfying — it means EC-HTE is a strict generalization of global correction,
1143	    not a fragile alternative. Coverage as the decisive metric (not RMSE) is the right
1144	    framing: practitioners care about interval validity more than point estimate precision.
1145	
1146	    '
1147	- name: Causal Forest Integration
1148	  plan_id: exp-011
1149	  description: 'EC-HTE correction applied to CausalForestDML subgroup estimates. Compare
1150	    naive_forest, global_forest, ec_hte_forest. K={2,4} × regime × n_expert. 144 total
1151	    rows, 100 MC runs.
1152	
1153	    '
1154	  expected_results:
1155	    n_mc: 100
1156	    n_configs: 8
1157	    total_rows: 144
1158	    mean_abs_bias_naive_forest: 0.156
1159	    mean_abs_bias_global_forest: 0.107
1160	    mean_abs_bias_ec_hte_forest: 0.061
1161	    mean_rmse_naive_forest: 0.178
1162	    mean_rmse_global_forest: 0.166
1163	    mean_rmse_ec_hte_forest: 0.229
1164	    debiasing_hurts_max_ratio: 5.9x (K=4/extreme/sg0)
1165	    debiasing_hurts_cases: 9
1166	    k2_n500_ec_hte_bias_range: 0.004-0.013 (near zero)
1167	    pattern_consistent_with_dim: true
1168	  result_rationale: 'CausalForest integration is P0 because Claim 2 explicitly mentions
1169	    CausalForestDML — without this experiment, there''s a claim-evidence gap that
1170	    reviewers would flag as a killshot. The results show two key patterns: (1) EC-HTE
1171	    achieves 61% bias reduction vs naive and 43% vs global, confirming the correction
1172	    generalizes beyond DIM to nonlinear CATE estimators, (2) the ''debiasing hurts''
1173	    effect is AMPLIFIED with CausalForest (5.9× for K=4/extreme vs 2.41× for DIM)
1174	    — nonlinear estimation compounds the misclassification-induced bias. This amplification
1175	    is the headline ''5.9×'' number in the abstract. Best-tier reviewers accept the
1176	    RMSE tradeoff (EC-HTE RMSE 0.229 > global 0.166) because it''s disclosed honestly
1177	    and explained: variance-bias tradeoff from per-subgroup CM estimation. At n=500/K=2,
1178	    EC-HTE bias is near-zero (0.004-0.013) with competitive RMSE, showing the tradeoff
1179	    resolves with sufficient expert labels. The ''5.9× amplification with CausalForest''
1180	    result is particularly impactful for NLP audience — many CSS researchers use causal
1181	    forests, so this directly threatens their existing workflows.
1182	
1183	    '
1184	  tables:
1185	  - name: 'Table 8: CausalForest Integration Results (Main Paper)'
1186	    columns:
1187	    - Method
1188	    - Mean |Bias|
1189	    - Mean RMSE
1190	    - Max Amplification
1191	    - K=2/n=500 |Bias|
1192	    rows:
1193	    - - Naive Forest
1194	      - '0.156'
1195	      - '0.178'
1196	      - '-'
1197	      - '0.125'
1198	    - - Global Forest
1199	      - '0.107'
1200	      - '0.166'
1201	      - 5.9x (K=4/extreme/sg0)
1202	      - 0.033-0.109
1203	    - - EC-HTE Forest
1204	      - '0.061'
1205	      - '0.229'
1206	      - '-'
1207	      - 0.004-0.013
1208	  - name: 'Table 9: Debiasing-Hurts Cases in CausalForest (Main Paper)'
1209	    columns:
1210	    - Config
1211	    - Subgroup
1212	    - Naive |Bias|
1213	    - Global |Bias|
1214	    - Amplification
1215	    rows:
1216	    - - K=4/extreme
1217	      - sg0 (lowest π)
1218	      - '0.018'
1219	      - '0.106'
1220	      - 5.9x
1221	    - - K=4/extreme
1222	      - sg1
1223	      - '0.045'
1224	      - '0.078'
1225	      - 1.7x
1226	    - - K=2/extreme
1227	      - sg0 (lowest π)
1228	      - '0.022'
1229	      - '0.063'
1230	      - 2.9x
1231	    - - K=2/moderate
1232	      - sg0
1233	      - '0.015'
1234	      - '0.031'
1235	      - 2.1x
1236	  - name: 'Table A12: Bias-RMSE Tradeoff by Budget'
1237	    columns:
1238	    - n_expert
1239	    - K
1240	    - EC-HTE |Bias|
1241	    - EC-HTE RMSE
1242	    - Global |Bias|
1243	    - Global RMSE
1244	    rows:
1245	    - - '100'
1246	      - '2'
1247	      - '0.025'
1248	      - '0.185'
1249	      - '0.071'
1250	      - '0.112'
1251	    - - '250'
1252	      - '2'
1253	      - '0.012'
1254	      - '0.128'
1255	      - '0.065'
1256	      - '0.108'
1257	    - - '500'
1258	      - '2'
1259	      - '0.006'
1260	      - '0.095'
1261	      - '0.059'
1262	      - '0.105'
1263	    - - '250'
1264	      - '4'
1265	      - '0.032'
1266	      - '0.265'
1267	      - '0.095'
1268	      - '0.145'
1269	    - - '500'
1270	      - '4'
1271	      - '0.018'
1272	      - '0.195'
1273	      - '0.088'
1274	      - '0.140'
1275	  figures_description:
1276	  - 'Figure 6 (Main): Side-by-side comparison of DIM vs CausalForest debiasing-hurts
1277	    effect. Shows amplification increases with nonlinear estimator, especially at
1278	    K=4.'
1279	  analysis: Best-tier reviewers see CausalForest results as the strongest evidence
1280	    for practical relevance. The 5.9× amplification headline number comes from this
1281	    experiment and is the paper's most eye-catching finding. The RMSE tradeoff is
1282	    disclosed in a dedicated 'Bias-RMSE Tradeoff' subsection — reviewers appreciate
1283	    the transparency and note that at n≥500, the tradeoff largely resolves. The pattern
1284	    consistency between DIM and CausalForest ('same direction, amplified magnitude')
1285	    strengthens the theoretical claim that the bias identity captures a fundamental
1286	    mechanism, not an estimator-specific artifact. Combined with exp-017 (R-learner
1287	    replication), this establishes estimator-agnosticism as a validated property.
1288	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "818c3972-976c-470e-a73f-bac82492ea68",
  "isSidechain": true,
  "promptId": "4ea5449b-44db-4907-acec-481354666130",
  "agentId": "a807effdf5ec0f5b7",
  "type": "user",
  "uuid": "290ab14b-2144-4230-b3b9-02dd39dad9f0",
  "sourceToolAssistantUUID": "818c3972-976c-470e-a73f-bac82492ea68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-23T20:16:01.666Z_

I have now thoroughly read the paper's main text (abstract, introduction, theory, method, experiments, related work, limitations, conclusion) and all appendices, as well as the review context. I have sufficient information to write a comprehensive review.

---

## EMNLP 2026 Review -- Reviewer 1 (Methods and Experiments)

**Paper:** "When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects"

---

### 1. Summary

This paper identifies a systematic failure mode of standard confusion-matrix correction for LLM-annotated effect modifiers in heterogeneous treatment effect analysis. The authors derive an exact bias identity (Theorem 1) showing that global correction introduces subgroup-level bias proportional to the product of each subgroup's deviation from the pooled error rate and the CATE heterogeneity, divided by an amplification factor from matrix inversion. They propose EC-HTE, a hierarchical Bayesian per-subgroup confusion matrix estimator that eliminates this bias when expert labels and classifier quality are sufficient. Validation spans synthetic grids, semi-synthetic experiments with real LLM annotations, a real hate speech dataset, and multiple LLM generations.

---

### 2. Strengths

**S1. The bias identity is clean, exact, and well-verified.** Theorem 1 is a genuine population-level identity (not a bound or approximation), stated in under five lines, with interpretable components. The empirical verification at R^2 >= 0.974 across hundreds of configurations and 11 real LLM-dataset combinations is thorough and convincing.

**S2. The "debiasing hurts" finding is non-obvious and practically important.** Demonstrating that global correction worsens estimates in 50% of configurations and can reverse CATE sign in 14.9-31% of configurations is a striking result that should prompt the NLP/CSS community to reconsider default correction practices.

**S3. Exceptional experimental breadth and honest boundary reporting.** The paper covers synthetic (520+ configs), semi-synthetic (TweetEval), real data (UC Berkeley Hate Speech, Civil Comments), CausalForest integration, R-learner compatibility, PPCI composition, 11 LLM-dataset combinations, asymmetric confusion matrices, class imbalance, confounded treatment, outcome-dependent and treatment-dependent misclassification, and subgroup misspecification. Critically, the paper honestly reports where EC-HTE fails (K=8 with fixed budget, high-FNR real data, moderate heterogeneity), which strengthens rather than weakens the contribution.

**S4. Actionable diagnostic with standalone value.** Proposition 2 provides a treatment-effect-free condition for detecting when global correction harms specific subgroups, computable from a pilot confusion matrix alone. This breaks a circular dependency and is independently useful even without adopting EC-HTE.

**S5. Strong reproducibility infrastructure.** MCMC convergence diagnostics (R-hat < 1.0034, ESS > 1618, zero divergences), Monte Carlo standard errors with paired statistical tests, per-subgroup decomposition tables, hyperprior sensitivity analysis, bootstrap SE validation across budgets, and oracle coverage decomposition all exceed what is typical in the NLP literature.

**S6. The PPCI composition is well-motivated.** Demonstrating that EC-HTE and PPCI address algebraically independent error sources, with the orthogonal 4-DGP design cleanly isolating each error type, is methodologically sound.

**S7. Multi-LLM persistence result is strategically important.** Showing that all tested LLMs (including GPT-5.4) exhibit Delta-pi > 0.05 preempts the "future models will fix this" objection. The cross-architecture consistency (shared worst subgroups) suggests the heterogeneity is structural.

---

### 3. Weaknesses

**W1. The symmetric misclassification assumption (A2) is heavily load-bearing in the main text but routinely violated in practice.** While Remark 1 and Appendix E acknowledge asymmetric confusion matrices, the main presentation (Theorem 1, Proposition 2, the diagnostic criterion) is built entirely on A2. Real LLM confusion matrices in this very paper show FPR/FNR ratios up to 7:1. The diagnostic AUC drops from 0.86 to 0.66 under asymmetry. The paper should be more explicit in the main text about how practitioners should handle the common asymmetric case, rather than deferring to appendix remarks.

**W2. The RMSE tradeoff is substantial and insufficiently discussed in the main text.** EC-HTE's mean RMSE (0.229) exceeds Global's (0.166) for CausalForest (Table 1). At K=4 with n=250, HB RMSE is 1.43x Global's (Table in Appendix kappa analysis). At K=8, HB RMSE is 2.03x Global's. For a method paper, this is a significant limitation. The main text mentions the tradeoff but underemphasizes its magnitude. A practitioner reading only the main text could come away thinking EC-HTE is uniformly superior, when in fact it requires careful budget-heterogeneity calibration.

**W3. The subgroup definition is assumed known and discrete, which limits applicability.** The paper requires pre-specified subgroups mapping text features to categories. In many CSS applications, the relevant subgroup structure is unknown a priori, and effect modifier heterogeneity may be continuous. The Limitations section mentions this but does not explore it. Data-driven subgroup discovery combined with EC-HTE would create a double-dipping concern (using data to both define subgroups and estimate per-subgroup confusion matrices) that is unaddressed.

**W4. The diagnostic's real-world performance is weaker than synthetic performance.** The subgroup-level AUC is 0.86 on synthetic data but drops to 0.63 on real LLM confusion matrices (Appendix, Section on Screening). The meta-criterion (max_s score > 1) achieves AUC >= 0.75 only for 5 of 16 combinations. For the remaining 11, the diagnostic is unreliable (4 of 7 have AUC < 0.5, indicating anti-prediction). This substantially weakens the practical value of Contribution 3 as stated in the abstract and introduction.

**W5. Assumption (A1)---conditional independence of misclassification and potential outcomes---is not testable and may be violated in the setting of interest.** The sensitivity analysis shows robustness to outcome-dependent violations up to gamma=0.2, but treatment-dependent misclassification degrades coverage to 75% at gamma_T=0.10 and 37% at gamma_T=0.20. In CSS applications where LLM annotation quality depends on treatment context (e.g., post-intervention text being harder to classify), this is a real concern. The paper's defense---"sensitivity analysis frameworks can bound the degradation"---is programmatic rather than demonstrated.

**W6. Semi-synthetic design raises construct validity concerns.** All CATE validation relies on synthetically injected treatment effects onto real text features. Ground-truth CATEs do not exist in any experiment. While this is acknowledged in the Limitations section and is a common constraint in causal inference work, it means we cannot evaluate whether the bias identity holds under naturally occurring treatment effect heterogeneity with naturally occurring confounds, interactions, and non-linearities.

**W7. Coverage below nominal in several configurations.** The HB coverage median is 0.93 (below the nominal 0.95). In the semi-real GPT-4.1 experiment (Appendix Table 9), HB coverage is 0.744 at n=100 and 0.834 at n=250. In the asymmetric end-to-end experiment, coverage is 0.930 under the symmetric assumption. While the paper discloses these, a method whose main selling point includes "calibrated inference" should more prominently discuss when calibration fails.

**W8. No comparison with multiple-annotator aggregation methods.** The related work cites Dawid-Skene and extensions for multi-annotator settings. If one uses multiple LLMs as annotators (which is increasingly standard practice), aggregation approaches might reduce Delta-pi without requiring expert labels. This natural baseline is not discussed or compared.

---

### 4. Questions for Authors

**Q1.** Table 1 (main results, K=2 extreme): Global |Bias| = 0.059 vs. Naive |Bias| = 0.058. This is a difference of 0.001. How sensitive is the "global correction increases bias" claim to this specific parameterization? What fraction of the K=2 extreme configurations show a statistically significant increase (not just any increase)?

**Q2.** The diagnostic AUC drops from 0.86 (synthetic) to 0.63 (real LLMs). Can you provide a practical decision rule for when the diagnostic itself is trustworthy? The meta-criterion (max_s score > 1) is a partial answer but leaves 11 of 16 real-world combinations unresolved.

**Q3.** The paper reports empirical Bayes optimization for alpha_0 in under 5ms. How sensitive are results to the alpha_0 selection method? What happens if alpha_0 is fixed at a small value (e.g., 1) versus a large value (e.g., 100)?

**Q4.** In the K=8 experiment (Appendix Table), HB RMSE (0.340) exceeds even Naive RMSE (0.133). This means EC-HTE is strictly worse than doing nothing on RMSE. At what K does EC-HTE reliably outperform Naive on both bias and RMSE simultaneously, given realistic expert budgets?

**Q5.** The paper claims composition with PPCI is "complementary." But in DGP C (Table in Appendix), PPCI alone achieves |Bias| = 0.017/0.007, while EC-HTE+PPCI achieves 0.007/0.008. The marginal improvement of adding EC-HTE to PPCI is small. Could you more precisely characterize when EC-HTE adds meaningful value over PPCI alone?

**Q6.** Have you considered or experimented with using multiple LLM annotators (not just one) to reduce Delta-pi through ensemble averaging, as an alternative to expert-label-based correction?

**Q7.** The treatment-dependent misclassification breakeven is at gamma_T approximately 0.10. Do you have empirical estimates of typical gamma_T values in real CSS applications? Without this, it is hard to assess whether the robustness range is sufficient.

---

### 5. Soundness Score: 3.5 / 5

**Justification:** The theoretical contribution (Theorem 1, Proposition 2) is mathematically correct and well-verified empirically. The proof is complete and the identity is exact under stated assumptions. However, several concerns limit the score: (a) the symmetric misclassification assumption is violated in practice but the main text presentation does not adequately address this; (b) the RMSE tradeoff means EC-HTE can be strictly worse than alternatives on an MSE criterion in realistic regimes (K>=4, moderate budgets); (c) Assumption A1 is untestable and the sensitivity to treatment-dependent violations is concerning (coverage drops to 75% at gamma_T=0.10); (d) the diagnostic degrades substantially on real data (AUC 0.63 vs. 0.86 synthetic). The contribution is sound in the sense that the identity is correct and the experiments are well-executed, but the gap between theoretical cleanness and practical applicability is not fully bridged.

---

### 6. Reproducibility Score: 4.5 / 5

**Justification:** The paper provides exceptional detail for reproducibility: full DGP specifications (synthetic, semi-synthetic, PPCI); explicit hyperparameters for CausalForest (n_estimators=48, min_samples_leaf=20); MCMC specifications (4 chains, 4000 iterations, 2000 warmup); convergence diagnostics; Monte Carlo standard errors; bootstrap validation; oracle decomposition. Algorithm 1 is fully specified. The code release promise ("upon acceptance") is standard. The only gap is that the LLM annotation prompts and API parameters are not provided (temperature, system prompt, etc.), which could affect the misclassification rates used in semi-synthetic experiments. The AI assistant disclosure is transparent.

---

### 7. Excitement Score: 3.5 / 5

**Justification:** The "debiasing can hurt" insight is genuinely surprising and important for the NLP/CSS community. The sign reversal result (14.9-31%) is particularly striking and should change practice. However, the technical contribution is incremental relative to classical measurement error theory---the bias identity is a matrix-algebra exercise that follows from known structures once you write down the right question. The hierarchical Bayesian estimator is standard (Dirichlet-Multinomial with empirical Bayes). The paper's contribution is more "important problem identification + careful formalization" than "novel methodology." This is valuable but places the work in the "solid contribution" rather than "highly exciting" category. The practical applicability constraints (requires known discrete subgroups, sufficient expert budget, adequate classifier quality, symmetric or near-symmetric errors) narrow the impact.

---

### 8. Overall Assessment: 3.5 / 5 (Borderline Conference)

**Justification:** This is a well-executed paper that identifies a real and important problem, provides a clean theoretical characterization, and validates it thoroughly across many experimental conditions. The honest reporting of negative results and boundary conditions is commendable. The paper would benefit from: (1) more prominent discussion of the RMSE tradeoff and practical applicability constraints in the main text, (2) better treatment of the asymmetric case in the main presentation, (3) acknowledgment that the diagnostic has limited real-world reliability (AUC 0.63), and (4) comparison with multi-annotator ensemble approaches. The gap between the theoretical elegance (exact identity) and practical utility (EC-HTE often loses on RMSE, diagnostic often unreliable) keeps this at the conference borderline. The "problem identification" aspect is strong enough for the main conference, but the proposed solution has narrower applicability than the framing suggests. The paper is above Findings quality but needs the practical story to be tightened for a confident main conference recommendation.

---

### 9. Confidence: 4 / 5

I have expertise in causal inference, measurement error models, and Bayesian estimation. I have less expertise in the specific NLP annotation pipelines discussed but have carefully evaluated the statistical methodology and experimental design. I am confident in my assessment of the theoretical contribution and the experimental rigor but acknowledge that NLP-specific domain considerations may alter the practical significance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "290ab14b-2144-4230-b3b9-02dd39dad9f0",
  "isSidechain": true,
  "agentId": "a807effdf5ec0f5b7",
  "requestId": "req_011CbL7XKmTXxMQ6g53SfruK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "96b0ce1c-c28e-4928-8c89-c39f9e3a059a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation",
  "sessionId": "5a7fea04-88c6-4f40-a7d8-de32a19d47e7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CABhUE1TqbUvbE21Nk55R",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17847,
      "cache_read_input_tokens": 82576,
      "output_tokens": 3505,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17847
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3505,
          "cache_read_input_tokens": 82576,
          "cache_creation_input_tokens": 17847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17847,
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
