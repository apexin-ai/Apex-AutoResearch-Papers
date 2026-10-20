# Research conversation: You are Reviewer 1 (R1) for an EMNLP 2026 ARR submission. Your focus: **Methods and Experiments**. ## Venue Calibration 

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ad7f414c5f9981729.jsonl`
- **Structured JSON:** [`ba41d5548535e1bbc115.json`](../../sessions/ba/ba41d5548535e1bbc115.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

56 recorded events

### User

_source line 1 · 2026-05-21T21:30:29.640Z_

You are Reviewer 1 (R1) for an EMNLP 2026 ARR submission. Your focus: **Methods and Experiments**.

## Venue Calibration
EMNLP 2026 ARR Overall Assessment (1–5, half-point scale):
- 5 = Award consideration (top 2.5%)
- 4 = Conference accept
- 3 = Findings accept
- 2 = Resubmit next cycle
- 1 = Do not resubmit
Acceptance rate ~21%. Soundness (1-5), Excitement (1-5), Reproducibility (1-5).

## Paper Summary

**Title**: "G-MFRM: A Diagnostic Framework for Joint Detection of Judge Bias and Benchmark Contamination in LLM Evaluation"

**Problem**: LLM-as-a-judge evaluation faces two entangled threats: inter-judge severity bias and benchmark contamination. Existing methods address these independently. Sequential correction (bias first, then contamination or vice versa) is an omitted variable bias problem when judge severity d_j and contamination term c_n·e_i are non-orthogonal.

**Contributions**:
1. Proposition 1: First-order bias expression for sequential estimators. Bias ≈ ρ·σ_d·c̄·ē·f(N,J,I). Validated by MC simulation across 120 settings (direction correct 97.2%, magnitude relative error 8%). Confounding negligible when c̄ < 0.4.
2. G-MFRM: 3-stage psychometric framework. Stage 1: standard MFRM calibration (θ,b,d). Stage 2: external exposure anchoring via ConStat delta + temporal signal + LogProber, composite e_i with cross-validated weights. Stage 3: Joint gated model with sigmoid gate g(e_i) = σ(α(e_i − e_0)) that activates contamination term only when exposure exceeds threshold. Prior on c_n ~ Half-Normal(0, σ_c²).
3. Empirical diagnostic: On real data (8 judges × 22 models × 3 benchmarks, ~186K evals), c̄_n = 0.14, 78% of posterior 95% CIs cover zero, prior-posterior KL = 0.08. G-MFRM degrades gracefully to MFRM (τ = 0.851 vs 0.843, p = 0.31). Under adversarial injection (5 models fine-tuned on benchmark items), G-MFRM recovers correction advantage (τ = 0.871 vs Sequential 0.831, p = 0.008).

**Key Results (Tables)**:
- Table 1: MC validation of Proposition 1. θ-RMSE degradation >5% only at c̄ ≥ 0.5, ρ ≥ 0.3.
- Table 2: Data collection. MT-Bench 80 items, Arena-Hard 500 items, 8 judges, 22 models, ~186K evals, 1.2% missing.
- Table 3: Exposure indicators. Composite e_i mean=0.07, std=0.10, median=0.03, ~11% significant. Skewness=2.1.
- Table 4: G-MFRM fit. Stage 1: R̂=1.01, ESS=820, τ=0.843. Stage 3: R̂=1.06, ESS=112, τ=0.851.
- Table 5: c_n posterior for top 3 models: model_A (0.38±0.15, CI [0.09,0.67] excludes 0), model_B (0.31±0.17, CI covers 0), model_C (0.27±0.14, CI covers 0). Remaining 19 models: c_n ∈ [0.02, 0.22], mostly cover 0.
- Table 6: Main results. G-MFRM τ=0.851 nominally best but not significantly better than MFRM (0.843, p=0.31) or Sequential (0.845, p=0.28). Bootstrap 95% CI for Δτ: [-0.008, 0.021]. Significant gap only vs Raw Average (0.812, p=0.003), DCR (0.819, p=0.008), Pref Leakage (0.824, p=0.012).
- Table 7: Contamination calibration. Real c̄=0.14 vs synthetic weak 0.50 vs synthetic strong 1.50. Real θ-RMSE degradation only 2.1%.
- Table 8: Facet fit. θ: 1 misfit (4.5%), b: 28 misfit (4.8%), d: 0 misfit (0%), c: 5 misfit (22.7%). c has widest infit range [0.60, 1.82].
- Table 9: Judge count sensitivity. Δ(G-MFRM vs Seq) ∈ [0.003, 0.006], never significant (p > 0.28).
- Table 10: Exposure ablation. Max Δτ from dropping any indicator: 0.003. No exposure (MFRM): Δτ = -0.008.
- Table 11: WildBench replication. Same pattern: MFRM 0.826, Sequential 0.828, G-MFRM 0.832. Cross-benchmark d_j correlation r=0.78, c_n correlation r=0.35.
- Table 12: Adversarial injection. Clean: G-MFRM 0.851 vs Seq 0.845 (p=0.28). Adversarial: G-MFRM 0.871 vs Seq 0.831 (p=0.008). c_n recovery correlation 0.82.

**Method Details**:
- Stage 1 MFRM: ln P(X≥k)/P(X<k) = θ_n − b_i − d_j − τ_k. Estimated via MCMC.
- Stage 2: e_i = w1·Δ_i^CS + w2·Δ_i^temp + w3·Δ_i^LP. 3 reference variants per item, 89% human equivalence pass rate.
- Stage 3: ln P(X≥k)/P(X<k) = θ_n − b_i − d_j + g(e_i)·c_n·e_i − τ_k. Sigmoid gate. c_n ~ Half-Normal. Initialized from Stage 1.
- Runtime: ~5,200 seconds for full pipeline.

**Paper structure**: 7 pages (within 8-page limit). Sections: Abstract, Intro, §2 Confounding theory, §3 Method, §4 Setup, §5 Results (5.1-5.8), §6 Adversarial, §7 Related Work, §8 Conclusion, Limitations. References: 8 entries.

## Your Review Task

Evaluate the following dimensions thoroughly:

### 1. Soundness (1-5)
- Is Proposition 1 mathematically correct? Is the first-order bias approximation valid? Are assumptions stated?
- Is the 3-stage G-MFRM model well-specified? Are priors justified?
- Is the MC validation methodology sound?
- Are the statistical tests appropriate (Wilcoxon, bootstrap CI)?
- Stage 3 convergence: R̂=1.06, ESS=112 — is this acceptable? What does it mean for reliability of c_n estimates?
- Is the "graceful degradation" narrative justified by the evidence, or is it post-hoc rationalization?

### 2. Experimental Rigor
- Are baselines comprehensive and fairly compared?
- Is Chatbot Arena τ the right ground truth? Limitations?
- Is the adversarial injection experiment convincing? Is fine-tuning 5/22 models on benchmark items a realistic threat model?
- Are there missing experiments or ablations?
- Is the exposure indicator construction (ConStat + temporal + LogProber) well-validated? Only 11% of items have significant exposure — does this undermine the framework?
- Facet fit: c has 22.7% misfit rate — what does this imply about model specification?

### 3. Reproducibility (1-5)
- Can the pipeline be reproduced? What details are missing?
- Is code/data availability mentioned?
- Are hyperparameters fully specified?

### 4. Key Strengths (bullet points)

### 5. Key Weaknesses (bullet points, be specific)

### 6. Questions for Authors (numbered list)

### 7. Preliminary Scores
- Soundness: X/5
- Excitement: X/5
- Reproducibility: X/5
- Overall Assessment: X/5 (use the EMNLP scale above)
- Confidence: X/5

Format your response as a structured review. Be rigorous but fair. Calibrate to the 21% acceptance rate.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "2ae5d648-4dc0-4b8e-aa51-26eb26607b2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T21:30:29.646Z_

```json
{
  "parentUuid": "2ae5d648-4dc0-4b8e-aa51-26eb26607b2c",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
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
  "uuid": "b15727d1-015c-4d8c-aa22-69439e94f87c",
  "timestamp": "2026-05-21T21:30:29.646Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T21:30:35.563Z_



I'll start by reading the paper and all relevant project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b15727d1-015c-4d8c-aa22-69439e94f87c",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRi2EA5QBkhdUv9dmic",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9bff37f0-a7c8-4e46-aa48-f97ac2619eca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyMaiTapNeMYqnvUPsPQVH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17081,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17081,
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

_source line 4 · 2026-05-21T21:30:36.991Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QybSXUuBbr8nwgC77gYBkG`</summary>

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
  "parentUuid": "9bff37f0-a7c8-4e46-aa48-f97ac2619eca",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRi2EA5QBkhdUv9dmic",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4476bebf-e288-4b8c-a7fa-7ea44c43878d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyMaiTapNeMYqnvUPsPQVH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17081,
      "cache_read_input_tokens": 0,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17081
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 125,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17081,
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

_source line 5 · 2026-05-21T21:30:36.996Z_

<details><summary>↩ Tool result · `toolu_01QybSXUuBbr8nwgC77gYBkG`</summary>

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
  "parentUuid": "4476bebf-e288-4b8c-a7fa-7ea44c43878d",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "8a656151-9d03-408a-b405-e33a8e9530d2",
  "sourceToolAssistantUUID": "4476bebf-e288-4b8c-a7fa-7ea44c43878d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-21T21:30:43.602Z_



Let me read the paper and project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a656151-9d03-408a-b405-e33a8e9530d2",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRiaFjdSHXq2eMQFMJx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b4ca597a-1e67-4681-88f1-170940331ff8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Powx9pqzj8EvCdn4YEsBxn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 17081,
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

_source line 7 · 2026-05-21T21:30:44.595Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_017qhf1m2a58Qin5ecougDJY`</summary>

```json
{
  "project": "gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4ca597a-1e67-4681-88f1-170940331ff8",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRiaFjdSHXq2eMQFMJx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56501dbb-bc8d-4170-839d-07997bb27913",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Powx9pqzj8EvCdn4YEsBxn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 17081,
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

_source line 8 · 2026-05-21T21:30:44.631Z_

<details><summary>↩ Tool result · `toolu_017qhf1m2a58Qin5ecougDJY`</summary>

```text
{"result":"# 项目 gated_mfrm_judge_bias 概况\n\n## 实验状态 (3 个)\n\n- **mvp_003**: DONE (success) — \n- **mvp_002**: DONE (negative) — \n- **mvp_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **mvp_003** (success): 同 mvp_002 DGP（c~HalfNormal(1.5), bimodal e, s~N(0,0.8), N=50, J=8, ρ=0.6），MCMC 调优（warmup=2000, samples=4000, chains=4, target_accept=0.95, non-centered parameterization）后收敛达标（R̂<1.05, ESS>100）且 joint 显著优于 sequential。 ← 基于 mvp_002\n- **mvp_002** (negative): 放大 contamination 信号（c~HalfNormal(1.5), bimodal e, s~N(0,0.8), N=50, J=8）后，joint G-MFRM 在 item-level + judge-level confounding (ρ=0.6) 下对 θ_true 的恢复精度显著优于 sequential pipeline。 ← 基于 mvp_001\n- **mvp_001** (negative): 当 d_j 与 c_n·e_i 存在 confounding（item-level + judge-level, ρ>0）时，joint G-MFRM 对 θ_true 的恢复精度（RMSE）显著优于 sequential pipeline，因为 joint estimation 避免了 contamination 效应被 d̂_j 和 b̂_i 吸收。\n  [diagnosis_bias_scatter](rtx6000-4x:/root/gated_mfrm_judge_bias/mvp/diagnosis_bias_scatter.png)\n\n## 趋势\n成功 1 / 负向 2 / 失败 0 / 共 3\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nrtx6000-4x: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56501dbb-bc8d-4170-839d-07997bb27913",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "1b1fbf62-e3d8-4b5c-8f50-1366cf45e69d",
  "sourceToolAssistantUUID": "56501dbb-bc8d-4170-839d-07997bb27913",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T21:30:45.127Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QY8fVCNxHXWEEC6WjDWDUM`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b1fbf62-e3d8-4b5c-8f50-1366cf45e69d",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRiaFjdSHXq2eMQFMJx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e897623-841a-4da6-ae44-db8625af67d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Powx9pqzj8EvCdn4YEsBxn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1447,
      "cache_read_input_tokens": 17081,
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

_source line 10 · 2026-05-21T21:30:45.137Z_

<details><summary>↩ Tool result · `toolu_01QY8fVCNxHXWEEC6WjDWDUM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/report.md\", \"content\": \"# Handover — 2026-05-21\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **mvp_003** (success): 同 mvp_002 DGP（c~HalfNormal(1.5), bimodal e, s~N(0,0.8), N=50, J=8, ρ=0.6），MCMC 调优（warmup=2000, samples=4000, chains=4, target_accept=0.95, non-centered parameterization）后收敛达标（R̂<1.05, ESS>100）且 joint 显著优于 sequential。 ← 基于 mvp_002\\n- **mvp_002** (negative): 放大 contamination 信号（c~HalfNormal(1.5), bimodal e, s~N(0,0.8), N=50, J=8）后，joint G-MFRM 在 item-level + judge-level confounding (ρ=0.6) 下对 θ_true 的恢复精度显著优于 sequential pipeline。 ← 基于 mvp_001\\n- **mvp_001** (negative): 当 d_j 与 c_n·e_i 存在 confounding（item-level + judge-level, ρ>0）时，joint G-MFRM 对 θ_true 的恢复精度（RMSE）显著优于 sequential pipeline，因为 joint estimation 避免了 contamination 效应被 d̂_j 和 b̂_i 吸收。\\n  [diagnosis_bias_scatter](rtx6000-4x:/root/gated_mfrm_judge_bias/mvp/diagnosis_bias_scatter.png)\\n\\n## 趋势\\n成功 1 / 负向 2 / 失败 0 / 共 3\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nrtx6000-4x: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 998, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e897623-841a-4da6-ae44-db8625af67d3",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "faeac9bd-1428-4281-9a95-2fe4ef06315a",
  "sourceToolAssistantUUID": "2e897623-841a-4da6-ae44-db8625af67d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T21:30:59.567Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_014Zs8xFSfvvVm9iT6t7FwEv`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faeac9bd-1428-4281-9a95-2fe4ef06315a",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRjAdTA8A27fs8fKWGp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a17cb486-af49-44ce-8335-d07756875100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWtRNKNT9LcpnKBYh657yB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1720,
      "cache_read_input_tokens": 18528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1720,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 12 · 2026-05-21T21:30:59.587Z_

<details><summary>↩ Tool result · `toolu_014Zs8xFSfvvVm9iT6t7FwEv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/memory.md\", \"content\": \"# Memory — gated_mfrm_judge_bias\\n\\n## MVP 验证链 (2026-05-21)\\n\\n### mvp_001: 信号太弱 → FAIL\\nc~HalfNormal(0.5), sigmoid(e), N=20, J=5。joint vs sequential Δ=0.0008, p=0.39。contamination 项仅占 logit ~10-15%。\\n\\n### mvp_002: 方法有效但 MCMC 不收敛 → FAIL (技术性)\\nc~HalfNormal(1.5), bimodal e, s~N(0,0.8), N=50, J=8, ρ=0.6。joint RMSE 降 32.8%, p=1e-6。但 ESS=47<100, R̂=1.05 边界。\\n\\n### mvp_003: MCMC 调优 → **PASS** ✅\\n同 mvp_002 DGP + warmup=2000, samples=4000, chains=4, target_accept=0.95, NCP for c。\\n- joint RMSE=0.1243±0.016 vs sequential=0.2211±0.038 → **降 43.8%, p=1e-6**\\n- joint τ=0.9223±0.010 vs sequential=0.8593±0.029 → +6.3pp\\n- R̂=1.03, ESS=224 → 收敛完全达标\\n- MCMC 调优不仅修复收敛，还提升了估计精度（mvp_002 joint RMSE=0.1486 → mvp_003=0.1243, -16.4%）\\n\\n### 散点图确认 omitted variable bias\\nmvp_001 ρ=0.6: Pearson r=0.6534 (p≈0)。高 c_n 的 model 被 sequential 系统性高估 θ。\\n\\n### 关键经验\\n- contamination 信号需要足够强（c_scale≥1.5, bimodal e）才能暴露 sequential 的缺陷\\n- NCP + target_accept=0.95 对 HalfNormal 约束参数的 MCMC 收敛至关重要\\n- 4 chains 比 2 chains 在 ESS 上提升巨大（47→224），不只是线性翻倍\\n- JAX CPU 模式下 20 seeds × 4 methods × (2000wu+4000s×4chains) 约 73 min\\n\\n## ConStat 调研 (2026-05-21)\\n\\n### 基本信息\\n- **论文**: \\\"ConStat: Performance-Based Contamination Detection in LLMs\\\", NeurIPS 2024 Poster, ETH Zurich SRI Lab\\n- **Repo**: github.com/eth-sri/ConStat, Apache-2.0, 低活跃 (4 commits)\\n- **核心定义**: Contamination = 不泛化的虚高性能（非单纯训练集包含 benchmark 样本）\\n\\n### 接口\\n`ConStat.test(scores_model, scores_model_ref_data, scores_ref_models, scores_ref_models_ref_data)` → p_value, estimated_contamination, delta, min_delta_095, 置信区间。纯黑盒，不需要 logprobs。\\n\\n### ⚠️ 对 G-MFRM 的关键 gap\\nConStat 输出 **per-model 全局污染检测**，不直接输出 **per-item e_i**。G-MFRM 需要 per-item exposure level。\\n- 可利用 `return_functions_test()` 的 spline 拟合函数推导 per-item observed vs expected 偏差作为 e_i proxy\\n- 最简方案：直接用 item-level performance gap (original vs reference benchmark) 作为 e_i proxy，ConStat spline hardness correction 作为精确校正层\\n\\n### 数据需求\\n1. Reference benchmark（与原始 benchmark 同分布但未泄露的变体）— **最大依赖**\\n2. Reference models（一组已知未污染的模型）的 per-item 评测结果（论文用 ~20 个模型）\\n3. 所有数据为 numpy per-item binary scores\\n\\n### 替代 e_i 估计方案\\n| 方法 | per-item? | 需要 logprobs? |\\n|------|-----------|---------------|\\n| ConStat spline 推导 | 间接可得 | 否 |\\n| Performance gap (orig vs ref) | 是 | 否 |\\n| LogProber | 天然 per-item | 是（无官方 repo） |\\n| Min-K% Prob | 天然 per-item | 是 |\\n\\n## Baseline 代码可用性 (2026-05-21)\\n\\n| Baseline | 代码 | License | 重实现难度 |\\n|----------|------|---------|-----------|\\n| CyclicJudge | 无 repo | — | 低 (~100行) |\\n| UDA | 无（anonymous 403） | — | 中 (2-4天) |\\n| DCR | github.com/chengxuphd/dcr | Apache-2.0 | 适配即可 |\\n| Preference Leakage | github.com/David-Li0406/Preference-Leakage | 无 license, 82% notebooks | 需整理 |\\n\\n### 下一步\\nMVP 通过后应：写 paper_framing.md + experiment_plan.yaml → 进入 research 阶段（真实数据实验）\\n\", \"total_chars\": 2712, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a17cb486-af49-44ce-8335-d07756875100",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "2f5204d5-5bc6-40f9-8dac-24b49693caad",
  "sourceToolAssistantUUID": "a17cb486-af49-44ce-8335-d07756875100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T21:31:00.504Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XjWTbucbZxPaW5zBmLeE9g`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f5204d5-5bc6-40f9-8dac-24b49693caad",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRjAdTA8A27fs8fKWGp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af73ab73-f7ea-498d-896d-f4df1982917c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWtRNKNT9LcpnKBYh657yB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1720,
      "cache_read_input_tokens": 18528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1720,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 67,
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

_source line 14 · 2026-05-21T21:31:00.514Z_

<details><summary>↩ Tool result · `toolu_01XjWTbucbZxPaW5zBmLeE9g`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/ROADMAP.md\", \"content\": \"# gated_mfrm_judge_bias — Research Dashboard\\n\\n> 最后更新: 2026-05-21 20:49 UTC | 更新原因: MVP PASS, 进入 research 阶段, 完成 post-MVP kickoff Steps 1-4\\n\\n## 核心方向\\nG-MFRM 统一校正 LLM 评测中的 judge bias 和 contamination。核心 insight: sequential 方法中 judge severity 与 contamination 存在 omitted variable confounding，joint estimation 方法论必要。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-21 通过）\\n- MVP 验证链: mvp_001 (FAIL, 信号弱) → mvp_002 (效应强 p=1e-6, 收敛不达标) → mvp_003 (PASS: RMSE -43.8%, R̂=1.03, ESS=224)\\n- 偏差散点图 Pearson r=0.65 独立确认 omitted variable bias\\n- paper_framing.md ✅ | experiment_plan.yaml ✅ | Dream 模拟中 (dream_20260521T204917)\\n- 文献图谱 12 篇 + 蒸馏完成\\n\\n## 实验计划摘要（详见 experiment_plan.yaml）\\n| 优先级 | 数量 | GPU·h | 关键实验 |\\n|--------|------|-------|---------|\\n| P0 | 5 | 200 | 数据收集(130h) + ConStat(30h) + G-MFRM 拟合(15h) + Baseline(20h) + Contamination 校准(5h) |\\n| P1 | 4 | 35 | Judge 数量敏感性 + 指标消融 + Facet 诊断 + Formal proposition |\\n| P2 | 2 | 55 | WildBench 复制 + 对抗鲁棒性 |\\n| **Total** | **11** | **290** | Critical path: exp-001→002→003→004/005 |\\n\\n## 近期任务\\n- [ ] 等 Dream 模拟完成，审查结果决定是否调整 framing/plan\\n- [ ] Dream 通过后批准 P0 实验，exp-001 + exp-009 可并行启动\\n- [ ] exp-001: 多 judge 数据收集（开源 judge vLLM 推理 + proprietary API）\\n- [ ] exp-009: Formal bias proposition（纯计算，不依赖数据）\\n\\n## GPU 预算\\n4x RTX 6000 96G (rtx6000-4x)，已绑定。\\nP0 实验 ~200 GPU·h，4 卡并行 ~50h wall clock (~2 天)。\\nProprietary API ~$900。\\n\\n## 目标会议\\n- AAAI 2027: July 28, 2026（~68 天）\\n- ACL 2027 ARR: August 3, 2026（~74 天）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D004 | 2026-05-21 | MVP PASS，进入 research 阶段 | mvp_003 |\\n| D003 | 2026-05-21 | mvp_002 核心效应验证成功（Joint RMSE -32.8%, p=1e-6），收敛未达标， | mvp_001, mvp_002 |\\n| D002 | 2026-05-21 | MVP FAIL 但不 kill，启动 DGP 参数诊断 | mvp_001 |\\n| D001 | 2026-05-21 | MVP 采用合成数据恢复实验验证 joint estimation 优势 | — |\\n\\n\\n\", \"total_chars\": 1780, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af73ab73-f7ea-498d-896d-f4df1982917c",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "c0180ea7-7b7e-499f-8a44-21eaaf3f90bf",
  "sourceToolAssistantUUID": "af73ab73-f7ea-498d-896d-f4df1982917c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T21:31:00.681Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01LLoX2hRXDqJG3nhwi2afLT`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0180ea7-7b7e-499f-8a44-21eaaf3f90bf",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRjAdTA8A27fs8fKWGp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d2187245-2597-4464-b1ef-2e55b17fd5eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UWtRNKNT9LcpnKBYh657yB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1720,
      "cache_read_input_tokens": 18528,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1720
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 301,
          "cache_read_input_tokens": 18528,
          "cache_creation_input_tokens": 1720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1720,
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

_source line 16 · 2026-05-21T21:31:00.690Z_

<details><summary>↩ Tool result · `toolu_01LLoX2hRXDqJG3nhwi2afLT`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'gated_mfrm_judge_bias'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2187245-2597-4464-b1ef-2e55b17fd5eb",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "3f88d8a9-d069-4a54-b896-9bb04a7f53a9",
  "sourceToolAssistantUUID": "d2187245-2597-4464-b1ef-2e55b17fd5eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T21:31:03.912Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QJpNjXUc1SNChimAWsYPhX`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f88d8a9-d069-4a54-b896-9bb04a7f53a9",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRkK7Tbo5BC6xnNFe2T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1256a4c-1384-4324-a974-4bd2d794f80e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tr85XwNQLq3JtBqn6goADM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 20248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3351,
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

_source line 18 · 2026-05-21T21:31:03.926Z_

<details><summary>↩ Tool result · `toolu_01QJpNjXUc1SNChimAWsYPhX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/paper_framing.md\", \"content\": \"# Paper Framing — gated_mfrm_judge_bias\\n\\n## Target Venue\\n- Primary: AAAI 2027 (full paper, deadline July 28, 2026)\\n- Backup: ACL 2027 via ARR (submission August 3, 2026)\\n- Timeline: ~68 days from today (2026-05-21)\\n\\n## Core Insight\\nSequential approaches to judge bias correction and contamination adjustment produce biased model ability estimates due to omitted variable confounding. Joint estimation within a single psychometric calibration framework is methodologically necessary, not merely convenient.\\n\\n## Core Claims (3 条，均可证伪)\\n\\n1. **Confounding Claim**: When judge severity (d_j) and contamination susceptibility (c_n·e_i) are both present but only one is modeled, the unmodeled facet's effect is absorbed into other parameter estimates, producing systematic bias in model ability rankings. Sequential pipelines (bias-first or contamination-first) do not resolve this confounding.\\n\\n2. **Framework Claim**: The Gated Many-Facet Rasch Model (G-MFRM) — combining MFRM's multi-facet structure with DG-IRT's gating mechanism and externally-anchored exposure indicators — jointly estimates model ability, item difficulty, judge severity, and contamination susceptibility in a single calibration, yielding bias-and-contamination-corrected \\\"fair scores.\\\"\\n\\n3. **Empirical Claim**: G-MFRM fair scores achieve higher agreement with human rankings (Chatbot Arena votes, Kendall-τ) than all baselines: raw multi-judge averages, bias-only correction (CyclicJudge, UDA), contamination-only adjustment (DCR), and naive sequential pipelines.\\n\\n## Story Spine\\n\\n- **Problem**: LLM-as-a-judge evaluation has bifurcated into two correction silos — judge bias and benchmark contamination — that are addressed independently. But judge severity and contamination effects are confounded: bias-only methods absorb contamination inflation into ability estimates; contamination-only methods misattribute judge effects as contamination signals. Sequential correction cannot resolve this because the first stage's estimates are already biased by the unmodeled facet.\\n\\n- **Existing approaches & gaps**: CyclicJudge eliminates average judge bias via round-robin but ignores contamination. UDA uses neural K-factor adjustment (−63.4% inter-judge std) but is black-box and contamination-unaware. DCR/ConStat quantify contamination effects (r²=0.94) but ignore judge variation. No existing work (0/12 surveyed papers, through May 2026) jointly models both within a single calibration framework.\\n\\n- **Our framing**: Joint estimation is methodologically necessary. We formalize this as an omitted variable bias problem: under non-orthogonality of d_j and c_n·e_i, sequential estimators are asymptotically biased (direction determined by covariance sign). G-MFRM resolves this by estimating all facets simultaneously, with a three-stage procedure ensuring identifiability: (1) standard MFRM for initial estimates, (2) external per-item exposure estimation via item-level performance gap (original vs reference variants) with difficulty correction, supplemented by temporal signals and LogProber where available, (3) joint gated model with e_i fixed and c_n as latent parameters. ConStat per-model delta serves as external validation of fitted c_n.\\n\\n- **Headline result template**: \\\"On MT-Bench/Arena-Hard with 8 LLM judges, G-MFRM fair scores achieve X% higher Kendall-τ with Chatbot Arena human votes than the best sequential baseline, while simultaneously producing interpretable per-model contamination estimates and per-judge severity profiles.\\\"\\n\\n## Narrative Strategy (from distilled writing)\\n\\n- **Type**: \\\"突破局限\\\" (sequential has structural flaw) + \\\"统一框架\\\" (G-MFRM unifies both corrections)\\n- **Opening hook**: Quantitative shock — lead with confounding's θ-RMSE degradation (43.8% in synthetic, to be validated on real data)\\n- **Section 2**: Toy example / formal proposition demonstrating confounding before introducing G-MFRM method\\n- **Figure 1**: Left = sequential pipeline with confounding annotation, Right = joint G-MFRM with gating mechanism highlighted\\n- **Main result table**: rows = methods (7 baselines + G-MFRM), cols = benchmarks × metrics\\n- **Ablation**: Full numbers (not checkmark grid), rows = components on/off\\n\\n## Venue Fit Risks\\n\\n- **AAAI**: Good fit for psychometric methodology applied to AI evaluation. Risk: reviewers may lack MFRM/IRT background — need clear, self-contained exposition with toy examples. Strength: AAAI values formal modeling + practical impact.\\n- **ACL/ARR**: Good fit for LLM evaluation methodology. Risk: may demand stronger NLP-specific contributions beyond the measurement framework. Strength: directly relevant to LLM evaluation community.\\n\\n## Anticipated Reviewer Concerns & Responses\\n\\n1. **\\\"Why not CyclicJudge + discard contaminated items?\\\"** — Item discard wastes information; CyclicJudge doesn't capture item-specific judge effects; neither produces c_n for auditing; G-MFRM degrades gracefully to standard MFRM when contamination ≈ 0.\\n\\n2. **\\\"Is confounding large enough in practice?\\\"** — MVP synthetic: 43.8% RMSE degradation. Real-data calibration (P0 experiment) will establish realistic contamination magnitude. Bias scatter (r=0.65) shows the mechanism exists regardless of magnitude.\\n\\n3. **\\\"Rank-1 assumption (c_n·e_i) too strong\\\"** — Rank-1 is LLTM tradition, good approximation when contamination comes from dominant data source. Person-fit diagnostics (infit/outfit) detect violations. Rank-k extension is future work.\\n\\n4. **\\\"DG-IRT transfer is trivial\\\"** — Three structural differences require non-trivial adaptation: binary→continuous exposure, single-rater→multi-facet, known→unknown exposure status. Stage 2 external anchoring solves a fundamental obstacle (exposure unknown to administrator) absent in educational testing.\\n\\n5. **\\\"Contamination signal realistic?\\\"** — ConStat validated r²=0.94 with true contamination effects. LogProber provides per-item memorization indicators. Multiple indicators combined via weighted composite. P0 experiment calibrates against real benchmarks.\\n\\n## Two-Tier Narrative (contingent on exp-005 contamination magnitude)\\n\\n**Tier A — Strong contamination (c ≈ 1.0-1.5, matching mvp_002/003)**:\\n- Lead with ranking correction as primary contribution\\n- Claim 3 at full strength: \\\"G-MFRM achieves X% higher Kendall-τ\\\"\\n- Headline: joint estimation dramatically outperforms sequential\\n\\n**Tier B — Weak contamination (c ≈ 0.3-0.5, matching mvp_001)**:\\n- Elevate diagnostic interpretability to co-primary contribution (per IDEA_BRIEF optimization A4)\\n- Reframe: \\\"even when ranking improvement is modest, G-MFRM uniquely provides per-model c_n (training audit), per-item e_i (item retirement), per-judge d_j (judge calibration)\\\"\\n- Bias scatter r=0.65 proves the mechanism exists; practical impact scales with contamination magnitude\\n- Claim 3 softened to \\\"comparable or better rankings PLUS interpretable diagnostic outputs\\\"\\n\\nexp-005 determines which tier. Decision point: after exp-005 results, before paper writing.\\n\\n## MVP Evidence Summary\\n\\n- mvp_003: Joint RMSE −43.8% vs Sequential (p=1e-6), Kendall-τ +6.3pp, R̂=1.03, ESS=224\\n- Bias scatter: Pearson r=0.65 (sequential systematically overestimates high-c_n models)\\n- Robustness: method effective even under model misspecification (DGP with s_j, model without)\\n\", \"total_chars\": 7277, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1256a4c-1384-4324-a974-4bd2d794f80e",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "c4b60cd1-ae2e-4dfd-aee2-ad57c0416051",
  "sourceToolAssistantUUID": "a1256a4c-1384-4324-a974-4bd2d794f80e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T21:31:04.265Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01VCQQWmVo3Rd2dwF46YTNyE`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4b60cd1-ae2e-4dfd-aee2-ad57c0416051",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRkK7Tbo5BC6xnNFe2T",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f6227fa-a2ce-469e-9de1-97fa7728f429",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tr85XwNQLq3JtBqn6goADM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3351,
      "cache_read_input_tokens": 20248,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3351
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 20248,
          "cache_creation_input_tokens": 3351,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3351,
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

_source line 20 · 2026-05-21T21:31:04.283Z_

<details><summary>↩ Tool result · `toolu_01VCQQWmVo3Rd2dwF46YTNyE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/decisions.yaml\", \"content\": \"_next_id: 5\\ndecisions:\\n- id: D001\\n  date: 2026-05-21 16:32 UTC\\n  summary: MVP 采用合成数据恢复实验验证 joint estimation 优势\\n  rationale: 合成数据 MVP 直接测试核心方法论主张（confounding 导致 sequential 有偏），无需 GPU/API key，实现快速，pass/fail\\n    标准明确。若合成数据上 joint 都无法胜出，real data 更不可能。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-21 18:40 UTC\\n  summary: MVP FAIL 但不 kill，启动 DGP 参数诊断\\n  rationale: mvp_001 效应方向正确（Joint RMSE < Sequential）但不显著（Δ<0.001, p≈0.37）。Reviewer\\n    诊断根因：contamination 信噪比低（c·e≈0.2 vs θ~1.0）、sequential OLS 在高正交变异下意外有效。数学逻辑成立，需找到暴露偏差的参数区间。\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: primary\\n    result: FAIL (p=0.35/0.39, Δ RMSE<0.001)\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-21 19:22 UTC\\n  summary: mvp_002 核心效应验证成功（Joint RMSE -32.8%, p=1e-6），收敛未达标，批准 mvp_003 调优 MCMC\\n  rationale: mvp_002 证明放大 contamination 后 joint 显著优于 sequential，散点图 r=0.65 直接验证 omitted\\n    variable bias 存在。ESS=47<100 是采样器技术问题（posterior geometry 困难），非理论缺陷。mvp_003 通过增加\\n    warmup/samples/chains + non-centered parameterization 解决。\\n  related_experiments:\\n  - exp_id: mvp_001\\n    role: predecessor\\n    result: FAIL (signal too weak)\\n  - exp_id: mvp_002\\n    role: primary\\n    result: partial PASS (effect strong p=1e-6, convergence FAIL ESS=47)\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-21 20:47 UTC\\n  summary: MVP PASS，进入 research 阶段\\n  rationale: mvp_003 全面达标：Joint RMSE -43.8% (p=1e-6)，R̂=1.03，ESS=224。散点图 r=0.65 独立验证\\n    omitted variable bias。方法在 model misspecification 下仍大幅优于 sequential（DGP 含 s_j，拟合模型不含），提供\\n    robustness 证据。\\n  related_experiments:\\n  - exp_id: mvp_003\\n    role: primary\\n    result: PASS (RMSE -43.8%, p=1e-6, R̂=1.03, ESS=224)\\n  depends_on:\\n  - D003\\n\", \"total_chars\": 1677, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f6227fa-a2ce-469e-9de1-97fa7728f429",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "85345540-50bd-4128-9d6d-f12f43329fb2",
  "sourceToolAssistantUUID": "2f6227fa-a2ce-469e-9de1-97fa7728f429",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T21:31:08.587Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QAjfaamKRVNmTWPRT86Ah5`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85345540-50bd-4128-9d6d-f12f43329fb2",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRkaTwX19oNsxmK6p1x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42509cc1-e558-41e4-8822-2d87445eef31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011AuBhffv3PDfzs4MzAFssK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3586,
      "cache_read_input_tokens": 23599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3586,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 22 · 2026-05-21T21:31:08.614Z_

<details><summary>↩ Tool result · `toolu_01QAjfaamKRVNmTWPRT86Ah5`</summary>

```text
artifacts/dream_reports/dream_20260521T204917/best/paper.tex
artifacts/dream_reports/dream_20260521T204917/median/paper.tex
artifacts/dream_reports/dream_20260521T204917/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42509cc1-e558-41e4-8822-2d87445eef31",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "04d5d8a9-4c69-4704-b2db-f9aa46a99580",
  "sourceToolAssistantUUID": "42509cc1-e558-41e4-8822-2d87445eef31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T21:31:09.076Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01N5Cec8q7zkjHYYVa54r1eh`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04d5d8a9-4c69-4704-b2db-f9aa46a99580",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRkaTwX19oNsxmK6p1x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ef0b5e3-da51-43a1-b032-08c8d093091e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011AuBhffv3PDfzs4MzAFssK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3586,
      "cache_read_input_tokens": 23599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3586,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 47,
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

_source line 24 · 2026-05-21T21:31:09.094Z_

<details><summary>↩ Tool result · `toolu_01N5Cec8q7zkjHYYVa54r1eh`</summary>

```text
artifacts/_project/intermediate/run_mvp.py
artifacts/mvp/models.py
artifacts/mvp/data_gen.py
artifacts/mvp/evaluate.py
artifacts/mvp/run_mvp.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ef0b5e3-da51-43a1-b032-08c8d093091e",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "c213b504-79e8-44c8-9906-71725bf07b74",
  "sourceToolAssistantUUID": "8ef0b5e3-da51-43a1-b032-08c8d093091e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T21:31:09.407Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FC9HPe1nUQAWMUCZvNb1Az`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c213b504-79e8-44c8-9906-71725bf07b74",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRkaTwX19oNsxmK6p1x",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "975a9dd7-74ad-4d18-b735-4d806d0e8427",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011AuBhffv3PDfzs4MzAFssK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3586,
      "cache_read_input_tokens": 23599,
      "output_tokens": 254,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3586
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 254,
          "cache_read_input_tokens": 23599,
          "cache_creation_input_tokens": 3586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3586,
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

_source line 26 · 2026-05-21T21:31:09.426Z_

<details><summary>↩ Tool result · `toolu_01FC9HPe1nUQAWMUCZvNb1Az`</summary>

```text
literature_map.yaml
distill_tmp/wang2025mfrm_llm.yaml
distill_tmp/fiedler2026bias_uncertainty.yaml
distill_tmp/soumik2026judging_judges.yaml
distill_tmp/logprober2024.yaml
distill_tmp/shu2013dgirt.yaml
distill_tmp/preference_leakage2026.yaml
distill_tmp/cyclicjudge2026.yaml
distill_tmp/lin2025psnirt.yaml
distill_tmp/constat2024.yaml
distill_tmp/dcr2025.yaml
distill_tmp/uda2026.yaml
distill_tmp/zheng2023mtbench.yaml
mistakes.yaml
artifacts/manifest.yaml
registry.yaml
decisions.yaml
artifacts/dream_reports/dream_20260521T204917/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T204917/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T204917/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260521T204917/best/review_context.yaml
experiment_plan.yaml
dream_registry.yaml
artifacts/dream_reports/dream_20260521T204917/median/review_context.yaml
artifacts/dream_reports/dream_20260521T204917/worst/review_context.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "975a9dd7-74ad-4d18-b735-4d806d0e8427",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "8f69b945-7fbf-4def-8613-014c58923766",
  "sourceToolAssistantUUID": "975a9dd7-74ad-4d18-b735-4d806d0e8427",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-21T21:31:12.770Z_

Let me read the dream report paper (the "best" scenario version, which likely represents the submitted paper) and the experiment plan.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f69b945-7fbf-4def-8613-014c58923766",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRkxVkXPdynbqY3RWmT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9c34be5e-a9dd-4456-8e97-4780f5800077",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzKFCML76RmgtYZ2XkGKLc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 802,
      "cache_read_input_tokens": 27185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 802,
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

_source line 28 · 2026-05-21T21:31:13.311Z_

<details open><summary>🔧 Tool call — Read · `toolu_01836g5ep5vLjeyR1k1QTRxm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c34be5e-a9dd-4456-8e97-4780f5800077",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRkxVkXPdynbqY3RWmT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dd8f7d9c-3755-4cae-94a8-386aaf7fd2f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzKFCML76RmgtYZ2XkGKLc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 802,
      "cache_read_input_tokens": 27185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 802,
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

_source line 29 · 2026-05-21T21:31:13.603Z_

<details open><summary>🔧 Tool call — Read · `toolu_01995cZhjDsJ6hce7hXXgbu1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd8f7d9c-3755-4cae-94a8-386aaf7fd2f1",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRkxVkXPdynbqY3RWmT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8b2c37f8-e334-40d5-8fda-84c7df195ea6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzKFCML76RmgtYZ2XkGKLc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 802,
      "cache_read_input_tokens": 27185,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 802
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 27185,
          "cache_creation_input_tokens": 802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 802,
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

_source line 30 · 2026-05-21T21:31:13.637Z_

<details><summary>↩ Tool result · `toolu_01836g5ep5vLjeyR1k1QTRxm`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{amsmath,amssymb,amsthm}
6	\usepackage{booktabs}
7	\usepackage{multirow}
8	\usepackage{graphicx}
9	\usepackage{xcolor}
10	\usepackage{hyperref}
11	\usepackage[margin=1in]{geometry}
12	\usepackage{natbib}
13	\usepackage{enumitem}
14	\usepackage{pifont}
15	
16	\newcommand{\cmark}{\ding{51}}
17	\newcommand{\xmark}{\ding{55}}
18	\newtheorem{proposition}{Proposition}
19	
20	\title{Joint Calibration of Judge Bias and Benchmark Contamination\\in LLM-as-a-Judge Evaluation}
21	
22	\author{Anonymous}
23	\date{}
24	
25	\begin{document}
26	\maketitle
27	
28	% ============================================================
29	% ABSTRACT
30	% ============================================================
31	\begin{abstract}
32	LLM-as-a-judge evaluation suffers from two well-documented distortions: inter-judge severity bias and benchmark contamination of target models. Existing methods address these independently---bias correction methods ignore contamination, and contamination adjustment methods ignore judge variation---or apply them sequentially. We show that sequential correction is fundamentally flawed: when judge severity ($d_j$) and contamination susceptibility ($c_n \cdot e_i$) are non-orthogonal, any single-facet estimator absorbs the unmodeled facet into its estimates, producing systematically biased model rankings. We formalize this as a first-order bias result (Proposition~1) and validate it on real data where ignoring confounding degrades ability RMSE by 28.5\%.
33	
34	We propose the \textbf{Gated Many-Facet Rasch Model (G-MFRM)}, a psychometric framework that jointly estimates model ability ($\theta_n$), item difficulty ($b_i$), judge severity ($d_j$), and contamination susceptibility ($c_n$) in a single Bayesian calibration. G-MFRM adapts the gating mechanism from Differential Group-IRT to the multi-facet, continuous-exposure setting, using externally-anchored exposure indicators from ConStat and temporal signals. On MT-Bench and Arena-Hard with 8 LLM judges evaluating 22 target models, G-MFRM fair scores achieve Kendall-$\tau = 0.91$ with Chatbot Arena human votes, significantly outperforming the best baseline (UDA, $\tau = 0.86$; $p < 0.001$) and all six other methods. The advantage holds on WildBench ($\tau = 0.89$), requires as few as 4 judges for significance, and provides interpretable per-model contamination estimates (AUC = 0.94 for detecting adversarially contaminated models).
35	\end{abstract}
36	
37	% ============================================================
38	% 1. INTRODUCTION
39	% ============================================================
40	\section{Introduction}
41	
42	LLM-as-a-judge evaluation has become the dominant paradigm for scalable model assessment \citep{zheng2023judging}, but it introduces two systematic distortions. First, different LLM judges exhibit varying severity: a lenient judge inflates scores while a strict one deflates them. Second, benchmark contamination causes target models that have been exposed to evaluation items during training to receive artificially inflated scores on those items. Both effects corrupt model ability estimates and can alter leaderboard rankings.
43	
44	The research community has attacked these problems in separate silos. Judge bias correction methods---CyclicJudge \citep{lin2025cyclicjudge}, UDA \citep{li2024uda}---model inter-judge variation but ignore contamination. Contamination detection methods---DCR \citep{yang2024dcr}, Preference Leakage \citep{li2024preference}---quantify contamination effects but ignore judge variation. The implicit assumption is that these distortions are separable: correct one, then correct the other.
45	
46	This assumption is wrong. We demonstrate that when judge severity and contamination susceptibility coexist and are correlated---as they are in practice ($|\rho| = 0.37$ in our data)---sequential correction produces biased estimates regardless of ordering. The mechanism is omitted variable confounding: the first correction stage's parameter estimates absorb the unmodeled facet's effects, and these biased estimates propagate to the second stage. In our experiments, ignoring this confounding degrades model ability RMSE by 28.5\% and causes sequential pipelines to systematically overestimate high-contamination models (bias scatter $r = 0.61$).
47	
48	We propose the \textbf{Gated Many-Facet Rasch Model (G-MFRM)}, a joint calibration framework that resolves this confounding by estimating all facets simultaneously. G-MFRM combines the multi-facet structure of the Many-Facet Rasch Model (MFRM) \citep{linacre1989mfrm} with the gating mechanism from Differential Group Item Response Theory (DG-IRT) \citep{robitzsch2020dgirt}, adapted to the LLM evaluation setting through three non-trivial modifications: (1)~binary group membership is replaced with continuous exposure indicators, (2)~single-rater design is extended to multi-facet calibration, and (3)~unknown exposure status is resolved through external anchoring.
49	
50	Our contributions:
51	\begin{enumerate}[nosep]
52	    \item A formal analysis showing sequential correction of judge bias and contamination is asymptotically biased under non-orthogonality (Proposition~1), validated by Monte Carlo simulation ($R^2 = 0.94$) and real data.
53	    \item G-MFRM: the first framework that jointly estimates model ability, item difficulty, judge severity, and contamination susceptibility in a single Bayesian calibration.
54	    \item Comprehensive evaluation on MT-Bench, Arena-Hard, and WildBench with 8 judges and 22 target models, achieving $\tau = 0.91$ with human rankings (vs.\ $\tau = 0.86$ for the best baseline), with ablations, sensitivity analyses, and adversarial robustness tests.
55	\end{enumerate}
56	
57	% ============================================================
58	% 2. WHY SEQUENTIAL CORRECTION FAILS
59	% ============================================================
60	\section{Why Sequential Correction Fails}
61	
62	Before presenting our model, we establish why joint estimation is methodologically necessary rather than merely convenient. We first formalize the confounding mechanism, then illustrate it with real data.
63	
64	\subsection{Problem Setup}
65	
66	Consider $N$ target models evaluated by $J$ LLM judges on $I$ benchmark items. The observed score $X_{nij}$ for model $n$ on item $i$ by judge $j$ depends on:
67	\begin{itemize}[nosep]
68	    \item $\theta_n$: model $n$'s true ability,
69	    \item $b_i$: item $i$'s difficulty,
70	    \item $d_j$: judge $j$'s severity (higher = stricter),
71	    \item $c_n$: model $n$'s contamination susceptibility,
72	    \item $e_i$: item $i$'s exposure level.
73	\end{itemize}
74	
75	A \emph{sequential} pipeline either (a)~corrects for judge severity first, then adjusts for contamination on the severity-corrected scores, or (b)~adjusts for contamination first, then corrects for severity. We show both orderings produce biased $\hat{\theta}_n$ when $d_j$ and $c_n \cdot e_i$ are non-orthogonal.
76	
77	\subsection{Formal Result}
78	
79	\begin{proposition}[Sequential Estimation Bias]
80	Under non-orthogonality $\mathrm{Cov}(d_j, c_n \cdot e_i) \neq 0$, the bias-first sequential estimator $\hat{\theta}_{\mathrm{seq}}$ has first-order bias:
81	\[
82	\mathbb{E}[\hat{\theta}_{\mathrm{seq}} - \theta_n] \approx \gamma \cdot \frac{\mathrm{Cov}(d_j,\; c_n \cdot e_i)}{\mathrm{Var}(d_j)}
83	\]
84	where $\gamma$ is the contamination gating coefficient. When the covariance is positive (strict judges assign more extreme scores to high-contamination models on high-exposure items), sequential estimation overestimates high-contamination models.
85	\end{proposition}
86	
87	\noindent This follows from standard omitted variable bias analysis adapted to the psychometric setting. The key insight is structural: the bias does not vanish with more data---it is a property of the model specification, not estimation noise.
88	
89	\subsection{Monte Carlo Validation}
90	
91	We validate Proposition~1 via 5,000 Monte Carlo simulations across a grid of 50 parameter configurations spanning $\rho(d_j, c_n \cdot e_i) \in [-0.8, 0.8]$. Table~\ref{tab:mc_bias} summarizes the results.
92	
93	\begin{table}[h]
94	\centering
95	\caption{Monte Carlo validation of the first-order bias approximation across correlation ranges.}
96	\label{tab:mc_bias}
97	\small
98	\begin{tabular}{lrrrr}
99	\toprule
100	$\rho$ range & $N_{\mathrm{sim}}$ & True bias & Approx.\ bias & Direction acc.\ (\%) \\
101	\midrule
102	$[-0.8, -0.4]$ & 1000 & $-0.28$ & $-0.26$ & 98.2 \\
103	$[-0.4, 0.0]$ & 1000 & $-0.09$ & $-0.08$ & 97.5 \\
104	$[0.0, 0.4]$ & 1000 & $0.10$ & $0.09$ & 97.8 \\
105	$[0.4, 0.8]$ & 1000 & $0.32$ & $0.30$ & 97.6 \\
106	\midrule
107	Overall & 5000 & --- & --- & 97.8 \\
108	\bottomrule
109	\end{tabular}
110	\end{table}
111	
112	The first-order approximation achieves $R^2 = 0.94$ and correctly predicts bias direction in 97.8\% of cases. On our real data ($\rho = 0.37$), the predicted bias is 0.17 standard units while the observed bias is 0.19 (10.5\% prediction error), confirming the formal result in practice.
113	
114	\subsection{Real-Data Evidence for Confounding}
115	
116	Three lines of evidence establish that confounding is not merely theoretical:
117	\begin{enumerate}[nosep]
118	    \item \textbf{Non-orthogonality}: $|\rho(d_j, c_n \cdot e_i)| = 0.37$ in our data, indicating that judge severity and contamination effects are correlated.
119	    \item \textbf{RMSE degradation}: Ignoring either facet degrades ability RMSE by 28.5\%, exceeding the 20\% threshold for practical significance.
120	    \item \textbf{Systematic overestimation}: The bias scatter correlation between sequential residuals and $c_n$ is $r = 0.61$---sequential pipelines systematically overestimate high-contamination models.
121	\end{enumerate}
122	
123	% ============================================================
124	% 3. THE GATED MANY-FACET RASCH MODEL
125	% ============================================================
126	\section{The Gated Many-Facet Rasch Model}
127	
128	\subsection{Model Specification}
129	
130	G-MFRM extends the standard MFRM by adding a contamination gating term. The expected score for model $n$ on item $i$ by judge $j$ is:
131	\begin{equation}
132	\mathbb{E}[X_{nij}] = \mu + (\theta_n - b_i - d_j) + g(c_n, e_i)
133	\label{eq:gmfrm}
134	\end{equation}
135	where $g(c_n, e_i) = c_n \cdot e_i$ is the gating function that captures the interaction between model $n$'s contamination susceptibility and item $i$'s exposure level. When $c_n = 0$ (clean model) or $e_i = 0$ (unexposed item), the gating term vanishes and G-MFRM reduces to standard MFRM.
136	
137	The full generative model with Gaussian residuals is:
138	\begin{equation}
139	X_{nij} \sim \mathcal{N}\!\left(\mu + \theta_n - b_i - d_j + c_n \cdot e_i,\; \sigma^2\right)
140	\end{equation}
141	with priors:
142	\begin{align}
143	\theta_n &\sim \mathcal{N}(0, \sigma_\theta^2), \quad b_i \sim \mathcal{N}(0, \sigma_b^2) \notag\\
144	d_j &\sim \mathcal{N}(0, \sigma_d^2), \quad c_n \sim \mathcal{N}^+(0, \sigma_c^2) \notag\\
145	\sigma_\theta, \sigma_b, \sigma_d, \sigma_c &\sim \text{Half-Cauchy}(0, 1) \notag
146	\end{align}
147	The half-normal prior on $c_n$ encodes the assumption that contamination inflates (not deflates) scores.
148	
149	\subsection{Three-Stage Estimation Pipeline}
150	
151	Joint estimation of $(\theta, b, d, c)$ faces an identifiability challenge: without knowing which items are exposed ($e_i$), the model cannot distinguish contamination-induced score inflation from genuine ability. We resolve this through a three-stage pipeline:
152	
153	\paragraph{Stage 1: Standard MFRM.} Fit a standard MFRM (without the gating term) to obtain initial estimates $\hat{\theta}^{(0)}, \hat{b}^{(0)}, \hat{d}^{(0)}$. This stage provides reasonable starting estimates and identifies potentially misfitting response patterns.
154	
155	\paragraph{Stage 2: External Exposure Anchoring.} Estimate per-item exposure $e_i$ using external indicators:
156	\begin{itemize}[nosep]
157	    \item \textbf{ConStat} \citep{dekoninck2024constat}: measures performance gap between original and semantically-equivalent rephrased items, providing a behavioral contamination signal.
158	    \item \textbf{Temporal signals}: release date proximity between benchmark publication and model training cutoff.
159	    \item \textbf{LogProber}: per-item memorization indicators from log-probability probing.
160	\end{itemize}
161	These are combined into a composite exposure indicator via weighted averaging, with weights determined by rank correlation with Stage~1 person-fit residuals.
162	
163	\paragraph{Stage 3: Joint Gated Model.} With $e_i$ anchored from Stage~2, fit the full G-MFRM (Eq.~\ref{eq:gmfrm}) using NumPyro MCMC with non-centered parameterization. All facets $(\theta, b, d, c)$ are estimated jointly, resolving the confounding identified in Section~2.
164	
165	\subsection{Adaptation from DG-IRT}
166	
167	G-MFRM adapts the gating mechanism from DG-IRT \citep{robitzsch2020dgirt} with three non-trivial modifications:
168	\begin{enumerate}[nosep]
169	    \item \textbf{Binary $\to$ continuous exposure}: DG-IRT uses known binary group membership; we replace this with continuous $e_i \in [0,1]$ estimated externally.
170	    \item \textbf{Single-rater $\to$ multi-facet}: DG-IRT models a single rater dimension; G-MFRM adds judge severity $d_j$ as an additional facet.
171	    \item \textbf{Known $\to$ unknown exposure}: In educational testing, group membership is observed; in LLM evaluation, exposure is latent and must be anchored externally (Stage~2).
172	\end{enumerate}
173	
174	% ============================================================
175	% 4. EXPERIMENTAL SETUP
176	% ============================================================
177	\section{Experimental Setup}
178	
179	\subsection{Data Collection}
180	\label{sec:data}
181	
182	We collected evaluation scores from 8 LLM judges spanning 4 providers and both API and open-source models: GPT-5.5 (OpenAI), Claude Opus 4.7 and Claude Sonnet 4.6 (Anthropic), DeepSeek-V4-Pro (DeepSeek), Qwen3-235B-A22B and Qwen3.6-27B (Alibaba), Llama~4 Maverick (Meta), and Gemini 2.5 Pro (Google). Each judge evaluated 22 target models on MT-Bench (80 items) and Arena-Hard (500 items) with position swapping, yielding 28,160 and 176,000 judgments respectively.
183	
184	Data quality metrics: missing rate 1.8\% (API timeouts, handled as missing-at-random in MCMC), inter-judge Fleiss $\kappa = 0.41$ (moderate agreement), and judge severity $\mathrm{SD} = 0.82$ (sufficient variation for $d_j$ estimation). Open-source judges (Qwen3.6-27B, Llama~4 Maverick) scored 0.3--0.4 points lower on average than API judges.
185	
186	\subsection{Exposure Estimation}
187	\label{sec:exposure}
188	
189	For each of the 580 items, we generated 3 reference variants via GPT-5.5 rephrasing. Human spot-check on 50 items confirmed 94\% semantic equivalence. ConStat deltas were computed as the performance gap between original and rephrased items. The composite exposure indicator combines ConStat ($\rho = 0.81$ with estimated $c_n$), temporal signals ($\rho = 0.62$), and LogProber ($\rho = 0.59$).
190	
191	MT-Bench items show substantially higher exposure (mean $e_i = 0.68$, 42.5\% high-exposure) compared to Arena-Hard (mean $e_i = 0.49$, 25.2\% high-exposure), consistent with MT-Bench's longer public availability and wider use.
192	
193	\subsection{MCMC Configuration}
194	
195	All models are fit using NumPyro with NUTS sampler: 2,000 warmup steps, 4,000 posterior samples, 4 chains, non-centered parameterization, target acceptance probability 0.95. Runtime: 2.8 hours on a single node.
196	
197	\subsection{Baselines}
198	
199	We compare G-MFRM against 7 methods spanning three categories:
200	
201	\begin{itemize}[nosep]
202	    \item \textbf{No correction}: Raw multi-judge average.
203	    \item \textbf{Bias-only}: MFRM-only (standard MFRM without gating), CyclicJudge \citep{lin2025cyclicjudge}, UDA \citep{li2024uda}.
204	    \item \textbf{Contamination-only}: DCR Factor \citep{yang2024dcr}, Preference Leakage calibration \citep{li2024preference}.
205	    \item \textbf{Both (sequential)}: Sequential pipeline applying MFRM then contamination correction.
206	\end{itemize}
207	
208	The primary evaluation metric is Kendall-$\tau$ between estimated model rankings and Chatbot Arena Elo-based rankings.
209	
210	% ============================================================
211	% 5. RESULTS
212	% ============================================================
213	\section{Results}
214	
215	\subsection{Main Results: G-MFRM vs.\ Baselines}
216	
217	Table~\ref{tab:main} presents the main comparison. G-MFRM achieves $\tau = 0.91$ (combined), significantly outperforming all 7 baselines.
218	
219	\begin{table}[t]
220	\centering
221	\caption{Baseline comparison: Kendall-$\tau$ and Spearman-$\rho$ with Chatbot Arena rankings. \textbf{Bold}: best result. All pairwise differences between G-MFRM and baselines are significant at $p < 0.01$ (Wilcoxon).}
222	\label{tab:main}
223	\small
224	\begin{tabular}{lccccccc}
225	\toprule
226	Method & Bias & Contam. & Joint & MT-B $\tau$ & AH $\tau$ & Comb.\ $\tau$ & Comb.\ $\rho$ \\
227	\midrule
228	Raw Average & \xmark & \xmark & \xmark & 0.80 & 0.83 & 0.82 & 0.89 \\
229	MFRM-only & \cmark & \xmark & --- & 0.83 & 0.85 & 0.84 & 0.91 \\
230	CyclicJudge & \cmark & \xmark & --- & 0.82 & 0.85 & 0.84 & 0.91 \\
231	DCR Factor & \xmark & \cmark & --- & 0.81 & 0.84 & 0.83 & 0.90 \\
232	Pref.\ Leakage & \xmark & \cmark & --- & 0.82 & 0.84 & 0.83 & 0.90 \\
233	Sequential & \cmark & \cmark & \xmark & 0.84 & 0.86 & 0.85 & 0.92 \\
234	UDA & \cmark$^*$ & \xmark & --- & 0.85 & 0.87 & 0.86 & 0.93 \\
235	\midrule
236	\textbf{G-MFRM (ours)} & \cmark & \cmark & \cmark & \textbf{0.90} & \textbf{0.91} & \textbf{0.91} & \textbf{0.96} \\
237	\bottomrule
238	\end{tabular}
239	
240	\vspace{2pt}
241	{\footnotesize $^*$UDA uses neural K-factor (implicit bias correction).}
242	\end{table}
243	
244	Key observations: (1)~Bias-only methods (MFRM, CyclicJudge: $\tau = 0.84$) and contamination-only methods (DCR, Pref.\ Leakage: $\tau = 0.83$) perform comparably---each captures one distortion but absorbs the other. (2)~Sequential ($\tau = 0.85$) improves over single-facet methods but remains limited by confounding. (3)~UDA ($\tau = 0.86$) is the strongest baseline owing to its neural K-factor, but its black-box design cannot address contamination. (4)~Only joint estimation (G-MFRM, $\tau = 0.91$) achieves the quality jump that resolves both distortions simultaneously. The improvement over UDA is significant ($p = 8.7 \times 10^{-4}$, 95\% CI of $\Delta\tau$: $[0.02, 0.08]$).
245	
246	\subsection{Model Ability and Contamination Estimates}
247	
248	Table~\ref{tab:ability} shows ability estimates for selected models. G-MFRM provides both decontaminated ability ($\theta_n$) and contamination susceptibility ($c_n$).
249	
250	\begin{table}[t]
251	\centering
252	\caption{Model ability estimates: G-MFRM vs.\ Sequential (selected models). $c_n$: contamination susceptibility estimated by G-MFRM.}
253	\label{tab:ability}
254	\small
255	\begin{tabular}{lrrrrr}
256	\toprule
257	Model & Arena Elo & G-MFRM $\theta$ & Seq.\ $\theta$ & Raw Avg & $c_n$ \\
258	\midrule
259	GPT-5.5 & 1320 & 1.82 & 1.95 & 8.12 & 1.63 \\
260	Claude Opus 4.7 & 1305 & 1.74 & 1.82 & 7.98 & 1.41 \\
261	DeepSeek-V4-Pro & 1285 & 1.61 & 1.73 & 7.85 & 1.52 \\
262	Gemini 2.5 Pro & 1275 & 1.55 & 1.58 & 7.79 & 0.89 \\
263	Claude Sonnet 4.6 & 1260 & 1.48 & 1.51 & 7.72 & 1.15 \\
264	\multicolumn{6}{c}{\dots} \\
265	Phi-4-mini & 1085 & 0.52 & 0.48 & 6.41 & 0.35 \\
266	Llama-3.3-8B & 1065 & 0.38 & 0.41 & 6.22 & 0.28 \\
267	\bottomrule
268	\end{tabular}
269	\end{table}
270	
271	The most contaminated models (GPT-5.5: $c_n = 1.63$, DeepSeek-V4-Pro: $c_n = 1.52$, Claude Opus 4.7: $c_n = 1.41$) are high-capacity models with the largest training corpora, consistent with higher probability of benchmark exposure. Small models (Phi-4-mini: $c_n = 0.35$, Llama-3.3-8B: $c_n = 0.28$) show minimal contamination.
272	
273	The mean contamination susceptibility $\bar{c}_n = 1.18$ ($\mathrm{SD} = 0.64$) confirms that contamination is not marginal: 45.5\% of models have $c_n > 0.8$, and 18.2\% have $c_n > 1.5$.
274	
275	\subsection{Contamination Magnitude Calibration}
276	
277	To assess whether real-world contamination is large enough to matter, we compare the empirical $c_n$ distribution against synthetic scenarios from our development experiments (Table~\ref{tab:calib}).
278	
279	\begin{table}[h]
280	\centering
281	\caption{Real vs.\ synthetic contamination magnitude. KS $p$: Kolmogorov-Smirnov test against real distribution.}
282	\label{tab:calib}
283	\small
284	\begin{tabular}{lrrrrr}
285	\toprule
286	Distribution & Mean & SD & Median & Q25--Q75 & KS $p$ \\
287	\midrule
288	Real data & 1.18 & 0.64 & 1.05 & 0.62--1.58 & --- \\
289	Synthetic (low) & 0.50 & 0.30 & 0.45 & 0.28--0.68 & 0.001 \\
290	Synthetic (high) & 1.50 & 0.50 & 1.48 & 1.15--1.82 & 0.12 \\
291	Synthetic (matched) & 1.20 & 0.50 & 1.18 & 0.82--1.55 & 0.41 \\
292	\bottomrule
293	\end{tabular}
294	\end{table}
295	
296	The real $c_n$ distribution is statistically indistinguishable from our ``matched'' synthetic scenario (KS $p = 0.41$) and clearly rejects the low-contamination scenario ($p = 0.001$). This validates that real-world contamination operates in a regime where joint correction yields substantial benefits.
297	
298	\subsection{Convergence Diagnostics}
299	
300	Table~\ref{tab:convergence} reports MCMC diagnostics. All parameters achieve $\hat{R} \leq 1.02$ and $\mathrm{ESS} \geq 312$, indicating reliable posterior estimation.
301	
302	\begin{table}[h]
303	\centering
304	\caption{MCMC convergence diagnostics by parameter group.}
305	\label{tab:convergence}
306	\small
307	\begin{tabular}{lrrrrr}
308	\toprule
309	Parameter & $N$ & Max $\hat{R}$ & Min ESS & Med.\ ESS & \% $\hat{R} < 1.01$ \\
310	\midrule
311	$\theta$ (ability) & 22 & 1.01 & 412 & 1850 & 95.5 \\
312	$b$ (difficulty) & 580 & 1.02 & 312 & 890 & 85.2 \\
313	$d$ (severity) & 8 & 1.00 & 2450 & 3100 & 100.0 \\
314	$c$ (contamination) & 22 & 1.02 & 345 & 1620 & 86.4 \\
315	$\sigma$ (priors) & 4 & 1.01 & 1890 & 2340 & 100.0 \\
316	\bottomrule
317	\end{tabular}
318	\end{table}
319	
320	\subsection{Judge Count Sensitivity}
321	
322	A practical question: how many judges does G-MFRM require? We subsample $\{2, 4, 6, 8\}$ judges (20 random draws each) and refit both G-MFRM and the sequential pipeline (Table~\ref{tab:judge_count}).
323	
324	\begin{table}[h]
325	\centering
326	\caption{Sensitivity to number of judges. G-MFRM's advantage grows with judge count; the sequential pipeline's $\tau$ plateaus because its bias is structural, not data-limited.}
327	\label{tab:judge_count}
328	\small
329	\begin{tabular}{rcccccc}
330	\toprule
331	$J$ & G-MFRM $\tau$ & Seq.\ $\tau$ & $\Delta\tau$ & $p$ & Max $\hat{R}$ & Min ESS \\
332	\midrule
333	2 & $0.86 \pm 0.03$ & $0.84 \pm 0.02$ & 0.02 & 0.14 & 1.04 & 185 \\
334	4 & $0.89 \pm 0.02$ & $0.85 \pm 0.02$ & 0.04 & 0.008 & 1.03 & 265 \\
335	6 & $0.90 \pm 0.01$ & $0.85 \pm 0.01$ & 0.05 & 0.001 & 1.02 & 298 \\
336	8 & $0.91 \pm 0.01$ & $0.85 \pm 0.01$ & 0.06 & $3.2 \times 10^{-5}$ & 1.02 & 312 \\
337	\bottomrule
338	\end{tabular}
339	\end{table}
340	
341	G-MFRM achieves significant improvement over sequential with as few as 4 judges ($p = 0.008$). The sequential pipeline's $\tau$ is essentially flat across judge counts (0.84--0.85), confirming that its limitation is structural (confounding) rather than statistical (insufficient data). In contrast, G-MFRM monotonically improves with more judges as cross-judge information better identifies $d_j$ and $c_n$.
342	
343	\subsection{Exposure Indicator Ablation}
344	
345	Table~\ref{tab:ablation} ablates the three exposure indicators used in Stage~2.
346	
347	\begin{table}[h]
348	\centering
349	\caption{Leave-one-out ablation of exposure indicators. ConStat is the dominant contributor; G-MFRM degrades gracefully without any single indicator.}
350	\label{tab:ablation}
351	\small
352	\begin{tabular}{llrrl}
353	\toprule
354	Configuration & Indicators & $\tau$ & $\Delta\tau$ & Rank corr.\ with $c_n$ \\
355	\midrule
356	Full composite & All three & 0.91 & --- & 0.85 \\
357	w/o ConStat & Temp.\ + LogP. & 0.88 & $-0.03$ & 0.68 \\
358	w/o Temporal & ConStat + LogP. & 0.90 & $-0.01$ & 0.82 \\
359	w/o LogProber & ConStat + Temp. & 0.90 & $-0.01$ & 0.83 \\
360	\midrule
361	ConStat only & ConStat & 0.90 & $-0.01$ & 0.81 \\
362	Temporal only & Temporal & 0.87 & $-0.04$ & 0.62 \\
363	LogProber only & LogProber & 0.87 & $-0.04$ & 0.59 \\
364	No exposure & None (MFRM) & 0.84 & $-0.07$ & --- \\
365	\bottomrule
366	\end{tabular}
367	\end{table}
368	
369	ConStat is the most important single indicator (marginal contribution: +0.03). Critically, even without ConStat, G-MFRM ($\tau = 0.88$) still outperforms all baselines including UDA ($\tau = 0.86$), demonstrating that the joint calibration framework provides structural benefits beyond exposure estimation quality. ConStat alone ($\tau = 0.90$) nearly matches the full composite ($\tau = 0.91$), suggesting it captures the dominant contamination signal.
370	
371	\subsection{Facet Fit Diagnostics}
372	
373	Table~\ref{tab:fit} reports infit/outfit mean-square statistics for each facet, assessing whether G-MFRM's assumptions are consistent with the data.
374	
375	\begin{table}[h]
376	\centering
377	\caption{Facet fit statistics. Acceptable range: infit/outfit MNSQ $\in [0.7, 1.3]$.}
378	\label{tab:fit}
379	\small
380	\begin{tabular}{lrccrc}
381	\toprule
382	Facet & $N$ & Infit mean & Infit range & Outfit mean & \% misfit \\
383	\midrule
384	$\theta$ (ability) & 22 & 1.01 & 0.78--1.25 & 1.03 & 4.5 \\
385	$b$ (difficulty) & 580 & 1.00 & 0.65--1.42 & 1.02 & 5.2 \\
386	$d$ (severity) & 8 & 0.98 & 0.82--1.18 & 0.99 & 0.0 \\
387	$c$ (contamination) & 22 & 1.02 & 0.74--1.38 & 1.05 & 9.1 \\
388	\bottomrule
389	\end{tabular}
390	\end{table}
391	
392	Overall fit is good: $\theta$, $b$, and $d$ facets show mean infit/outfit near 1.0 with low misfit rates. The contamination facet $c$ has the highest misfit rate (9.1\%, 2 of 22 models), attributable to the rank-1 assumption ($c_n \cdot e_i$) being an imperfect approximation for models with heterogeneous contamination patterns across items. Traditional person-fit statistics ($l_z$, EMRi) correlate $r = 0.72$ and $r = 0.68$ with G-MFRM's $c_n$ estimates, providing convergent validity for the contamination construct.
393	
394	\subsection{Cross-Benchmark Replication: WildBench}
395	
396	To assess generalization, we replicate the full G-MFRM pipeline on WildBench (1,024 items; Table~\ref{tab:wildbench}).
397	
398	\begin{table}[h]
399	\centering
400	\caption{Cross-benchmark replication. G-MFRM's advantage is consistent across all three benchmarks.}
401	\label{tab:wildbench}
402	\small
403	\begin{tabular}{lccc}
404	\toprule
405	Method & WildBench $\tau$ & MT-Bench $\tau$ & Arena-Hard $\tau$ \\
406	\midrule
407	Raw Average & 0.80 & 0.80 & 0.83 \\
408	Sequential & 0.84 & 0.84 & 0.86 \\
409	UDA & 0.85 & 0.85 & 0.87 \\
410	\textbf{G-MFRM} & \textbf{0.89} & \textbf{0.90} & \textbf{0.91} \\
411	\bottomrule
412	\end{tabular}
413	\end{table}
414	
415	G-MFRM achieves $\tau = 0.89$ on WildBench ($p = 2.1 \times 10^{-4}$ vs.\ sequential), with slightly lower absolute performance than MT-Bench/Arena-Hard due to WildBench's more open-ended items. Contamination estimates are consistent across benchmarks: the rank correlation of per-model $c_n$ between WildBench and MT-Bench+Arena-Hard is $r = 0.82$, indicating that contamination susceptibility is a stable model property rather than a benchmark-specific artifact.
416	
417	\subsection{Adversarial Robustness}
418	
419	Following \citet{wang2026adversarial}, we simulate controlled contamination injection at $\{0\%, 5\%, 10\%, 20\%\}$ of training data and measure both contamination detection and ability estimation robustness (Table~\ref{tab:adversarial}).
420	
421	\begin{table}[h]
422	\centering
423	\caption{Adversarial robustness under controlled contamination injection. Robustness ratio = Sequential $\theta$-bias / G-MFRM $\theta$-bias.}
424	\label{tab:adversarial}
425	\small
426	\begin{tabular}{rcccc}
427	\toprule
428	Injection \% & G-MFRM $c_n$ & G-MFRM $\theta$-bias & Seq.\ $\theta$-bias & Robustness \\
429	\midrule
430	0 & 0.15 & 0.02 & 0.03 & 1.5$\times$ \\
431	5 & 0.82 & 0.05 & 0.18 & 3.6$\times$ \\
432	10 & 1.45 & 0.08 & 0.34 & 4.3$\times$ \\
433	20 & 2.18 & 0.14 & 0.52 & 3.7$\times$ \\
434	\bottomrule
435	\end{tabular}
436	\end{table}
437	
438	G-MFRM's $c_n$ estimates correlate $r = 0.97$ with true injection rates. Under 20\% contamination injection, G-MFRM's ability bias (0.14) is 3.7$\times$ smaller than sequential's (0.52). The gating mechanism absorbs contamination inflation into $c_n$ rather than $\theta$, providing both robust ability estimation and a contamination audit signal (AUC = 0.94 for detecting injected models). This is a controlled validation; real-world contamination involves unknown injection rates, which G-MFRM handles through its Stage~2 external anchoring.
439	
440	% ============================================================
441	% 6. RELATED WORK
442	% ============================================================
443	\section{Related Work}
444	
445	\paragraph{LLM Judge Bias.}
446	\citet{zheng2023judging} document position bias and verbosity bias in GPT-4 judgments. CyclicJudge \citep{lin2025cyclicjudge} eliminates average judge bias via round-robin evaluation but cannot capture item-specific severity variation. UDA \citep{li2024uda} uses a neural K-factor to reduce inter-judge standard deviation by 63.4\%, but operates as a black box without principled contamination handling. These methods assume contamination is absent or negligible.
447	
448	\paragraph{Benchmark Contamination.}
449	ConStat \citep{dekoninck2024constat} detects contamination via performance gaps on original vs.\ rephrased items ($r^2 = 0.94$ with true effects). DCR \citep{yang2024dcr} factors contamination into ranking adjustments. Preference Leakage \citep{li2024preference} shows that LLM judges preferentially score contaminated outputs higher. LogProber provides item-level memorization detection. None of these methods account for judge severity variation.
450	
451	\paragraph{Psychometric Models for LLM Evaluation.}
452	Item Response Theory (IRT) has been applied to benchmark calibration \citep{polo2024tinybenchmarks}. The Many-Facet Rasch Model (MFRM) \citep{linacre1989mfrm} generalizes Rasch models to multiple rater facets and has been used for human evaluation calibration. Differential Group IRT (DG-IRT) \citep{robitzsch2020dgirt} models differential item functioning across known groups. G-MFRM is the first framework to combine multi-facet structure with contamination gating for LLM evaluation.
453	
454	% ============================================================
455	% 7. CONCLUSION
456	% ============================================================
457	\section{Conclusion}
458	
459	We have shown that sequential correction of judge bias and benchmark contamination is fundamentally biased under non-orthogonality of these effects---a condition that holds in practice. G-MFRM resolves this through joint Bayesian calibration, achieving 5--9 points higher Kendall-$\tau$ with human rankings than existing methods across three benchmarks. Beyond ranking correction, G-MFRM produces interpretable per-model contamination estimates that can serve as a post-hoc audit tool ($\text{AUC} = 0.94$).
460	
461	% ============================================================
462	% LIMITATIONS
463	% ============================================================
464	\section*{Limitations}
465	
466	The rank-1 contamination structure ($c_n \cdot e_i$) assumes a single dominant contamination mechanism; models with heterogeneous contamination sources may exhibit misfit (9.1\% of models in our data). Extending to rank-$k$ decomposition is a natural direction. The Stage~2 exposure estimation relies on ConStat's rephrasing pipeline, which assumes semantic equivalence of rephrasings (94\% pass rate in our human validation, but not 100\%). Our evaluation uses Chatbot Arena Elo as the ground truth for model ability, which itself carries biases from user selection effects. Finally, the MCMC inference requires $\sim$3 hours, which may limit real-time deployment; variational alternatives could improve scalability.
467	
468	% ============================================================
469	% REFERENCES
470	% ============================================================
471	\bibliographystyle{plainnat}
472	
473	\begin{thebibliography}{20}
474	
475	\bibitem[Zheng et~al.(2023)]{zheng2023judging}
476	L.~Zheng, W.-L. Chiang, Y.~Sheng, et~al.
477	\newblock Judging {LLM}-as-a-judge with {MT-Bench} and {Chatbot Arena}.
478	\newblock In \emph{NeurIPS}, 2023.
479	
480	\bibitem[Lin et~al.(2025)]{lin2025cyclicjudge}
481	Z.~Lin, S.~Wang, et~al.
482	\newblock {CyclicJudge}: Eliminating judge bias via cyclic evaluation.
483	\newblock In \emph{AAAI}, 2025.
484	
485	\bibitem[Li et~al.(2024a)]{li2024uda}
486	X.~Li et~al.
487	\newblock {UDA}: Unified debiasing approach for {LLM}-as-a-judge.
488	\newblock In \emph{ACL}, 2024.
489	
490	\bibitem[Yang et~al.(2024)]{yang2024dcr}
491	S.~Yang et~al.
492	\newblock {DCR}: Decontaminated ranking for fair {LLM} evaluation.
493	\newblock In \emph{EMNLP}, 2024.
494	
495	\bibitem[Li et~al.(2024b)]{li2024preference}
496	W.~Li et~al.
497	\newblock Preference leakage: How benchmark contamination biases {LLM} judges.
498	\newblock In \emph{NeurIPS}, 2024.
499	
500	\bibitem[De~Koninck et~al.(2024)]{dekoninck2024constat}
501	T.~De~Koninck et~al.
502	\newblock {ConStat}: Performance-based contamination detection in large language models.
503	\newblock In \emph{ICML}, 2024.
504	
505	\bibitem[Linacre(1989)]{linacre1989mfrm}
506	J.~M. Linacre.
507	\newblock \emph{Many-Facet {Rasch} Measurement}.
508	\newblock MESA Press, 1989.
509	
510	\bibitem[Robitzsch(2020)]{robitzsch2020dgirt}
511	A.~Robitzsch.
512	\newblock {DG-IRT}: Differential group item response theory.
513	\newblock \emph{Journal of Educational and Behavioral Statistics}, 45(6), 2020.
514	
515	\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}
516	F.~Polo et~al.
517	\newblock {TinyBenchmarks}: Evaluating {LLMs} with fewer examples via item response theory.
518	\newblock In \emph{ICML}, 2024.
519	
520	\bibitem[Wang et~al.(2026)]{wang2026adversarial}
521	Y.~Wang et~al.
522	\newblock Adversarial contamination attacks on {LLM} benchmarks.
523	\newblock In \emph{ICLR}, 2026.
524	
525	\end{thebibliography}
526	
527	\end{document}
528	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd8f7d9c-3755-4cae-94a8-386aaf7fd2f1",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "e107d58d-a495-4d06-8258-3740b88d65de",
  "sourceToolAssistantUUID": "dd8f7d9c-3755-4cae-94a8-386aaf7fd2f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T21:31:13.608Z_

<details><summary>↩ Tool result · `toolu_01995cZhjDsJ6hce7hXXgbu1`</summary>

```text
1	experiments:
2	  # === P0: Must-run for headline results ===
3	
4	  - id: exp-001
5	    name: multi_judge_data_collection
6	    claim: 3
7	    description: "Collect multi-judge evaluation data on MT-Bench and Arena-Hard using 8+ judges: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick, + 1 additional. Evaluate 20+ target models. Position swap for pairwise."
8	    priority: P0
9	    gpu_budget_hours: 130
10	    deps: []
11	    notes: "Open-source judges via vLLM on RTX 6000. Proprietary judges via API (~$900 budget). Position swap doubles evaluation count."
12	
13	  - id: exp-002
14	    name: item_exposure_estimation
15	    claim: 2
16	    description: "Estimate per-item exposure e_i via three-source pipeline: (1) Primary: item-level performance gap between original items and GPT-5.5/Claude-rephrased reference variants, averaged across reference models, with spline difficulty correction (ConStat-inspired). (2) Temporal: performance gap on pre-cutoff vs post-cutoff item variants where available. (3) LogProber: token logprob memorization scores for models with logprob API. Sources combined via weighted composite (weights tuned on validation split). ConStat per-model delta used as external validation of fitted c_n, not as e_i source."
17	    priority: P0
18	    gpu_budget_hours: 30
19	    deps: [exp-001]
20	    notes: "Main bottleneck: reference benchmark variant construction + quality validation. ConStat per-model delta validates G-MFRM c_n, not used for per-item e_i."
21	
22	  - id: exp-003
23	    name: gmfrm_real_data_fit
24	    claim: [1, 2, 3]
25	    description: "Fit G-MFRM three-stage pipeline on real data from exp-001/002. Stage 1: MFRM (θ,b,d). Stage 2: e_i from exp-002. Stage 3: Joint gated model. Compare fair scores θ̂ with Chatbot Arena human votes (Kendall-τ)."
26	    priority: P0
27	    gpu_budget_hours: 15
28	    deps: [exp-001, exp-002]
29	    notes: "NumPyro MCMC. Use MVP MCMC settings (warmup=2000, samples=4000, chains=4, NCP, target_accept=0.95). Include per-benchmark analysis: if any benchmark has contamination ≈ 0, verify G-MFRM degrades gracefully to MFRM level (real-data graceful degradation check)."
30	
31	  - id: exp-004
32	    name: baseline_comparison
33	    claim: 3
34	    description: "Compare G-MFRM against 8 baselines on same data: (1) raw multi-judge average, (2) MFRM-only, (3) sequential pipeline, (4) CyclicJudge, (5) CyclicJudge + contaminated item discard, (6) DCR Factor, (7) UDA, (8) Preference Leakage calibration. Metrics: Kendall-τ, Spearman-ρ with Chatbot Arena."
35	    priority: P0
36	    gpu_budget_hours: 20
37	    deps: [exp-003]
38	    notes: "Baseline (5) is the strongest trivial alternative — addresses Reviewer Concern #1. CyclicJudge/UDA/DCR/PrefLeakage need public code check. Budget may not include debug time."
39	
40	  - id: exp-005
41	    name: contamination_magnitude_calibration
42	    claim: 1
43	    description: "Estimate real contamination magnitude: compare fitted c_n from exp-003 with synthetic MVP assumptions. Determine if real contamination is closer to mvp_001 (c~0.5, weak) or mvp_002 (c~1.5, strong). Critical for claim strength."
44	    priority: P0
45	    gpu_budget_hours: 5
46	    deps: [exp-003]
47	    notes: "Reviewer flagged: if real c ≈ mvp_001 level, paper impact weakens. This experiment determines claim calibration."
48	
49	  # === P1: Important for robustness ===
50	
51	  - id: exp-006
52	    name: judge_count_sensitivity
53	    claim: 2
54	    description: "Sensitivity analysis: vary number of judges (2, 4, 6, 8+) and measure G-MFRM performance degradation. At what minimum judge count does G-MFRM still outperform sequential?"
55	    priority: P1
56	    gpu_budget_hours: 10
57	    deps: [exp-003]
58	
59	  - id: exp-007
60	    name: exposure_indicator_ablation
61	    claim: 2
62	    description: "Ablation: contribution of each exposure indicator (ConStat delta, temporal signal, LogProber Safe Score) to e_i estimation quality. Leave-one-out analysis."
63	    priority: P1
64	    gpu_budget_hours: 10
65	    deps: [exp-002, exp-003]
66	
67	  - id: exp-008
68	    name: facet_fit_diagnostics
69	    claim: 2
70	    description: "Measurement quality validation: report infit/outfit MNSQ for all facets (θ, b, d, c). Flag misfitting elements. Compare Stage 1 person-fit (lz, EMRi) vs Stage 3 c_n as construct coherence validation."
71	    priority: P1
72	    gpu_budget_hours: 5
73	    deps: [exp-003]
74	
75	  - id: exp-009
76	    name: confounding_formal_proposition
77	    claim: 1
78	    description: "Formal bias analysis: derive first-order bias approximation for sequential estimator under d_j/c_n·e_i non-orthogonality. Validate via Monte Carlo simulation across realistic parameter ranges. For paper Section 2."
79	    priority: P1
80	    gpu_budget_hours: 10
81	    deps: []
82	    notes: "Can run in parallel with data collection. Extends MVP synthetic analysis to formal proposition."
83	
84	  # === P2: Nice-to-have ===
85	
86	  - id: exp-010
87	    name: wildbench_replication
88	    claim: 3
89	    description: "Replicate G-MFRM pipeline on WildBench as third benchmark. Cross-benchmark generalization."
90	    priority: P2
91	    gpu_budget_hours: 40
92	    deps: [exp-003]
93	
94	  - id: exp-011
95	    name: adversarial_robustness
96	    claim: 2
97	    description: "Test G-MFRM robustness against adversarial contamination following Wang et al. (ICLR 2026) fragility findings."
98	    priority: P2
99	    gpu_budget_hours: 15
100	    deps: [exp-003]
101	
102	summary:
103	  total_experiments: 11
104	  p0_count: 5
105	  p1_count: 4
106	  p2_count: 2
107	  total_gpu_hours: 290
108	  p0_gpu_hours: 200
109	  api_budget: "$900 (proprietary judge APIs)"
110	  critical_path: "exp-001 → exp-002 → exp-003 → exp-004/005"
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b2c37f8-e334-40d5-8fda-84c7df195ea6",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "d47cd305-05ee-4ee6-9cde-2528de6d1a16",
  "sourceToolAssistantUUID": "8b2c37f8-e334-40d5-8fda-84c7df195ea6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-21T21:31:17.125Z_

Now let me read the median and worst scenario papers to understand the full range of imagined results, plus the review context and imagined experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d47cd305-05ee-4ee6-9cde-2528de6d1a16",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRmGMYoVRevoTtrdBL2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d2b1f0a-a970-4616-9210-e9e165938739",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q1fpZ7XippD5rrRCdceW7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14947,
      "cache_read_input_tokens": 27987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14947,
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

_source line 33 · 2026-05-21T21:31:19.501Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A94fVK8UyhN7u82v9uQVYQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/median/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d2b1f0a-a970-4616-9210-e9e165938739",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRmGMYoVRevoTtrdBL2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fecfb2be-ef33-4624-a5cf-49fe88436b36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q1fpZ7XippD5rrRCdceW7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14947,
      "cache_read_input_tokens": 27987,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14947,
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

_source line 34 · 2026-05-21T21:31:19.790Z_

<details><summary>↩ Tool result · `toolu_01A94fVK8UyhN7u82v9uQVYQ`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage[margin=1in]{geometry}
6	\usepackage{amsmath,amssymb,amsthm}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{natbib}
10	\usepackage{hyperref}
11	\usepackage{multirow}
12	\usepackage{xcolor}
13	\usepackage{tabularx}
14	
15	\newtheorem{proposition}{Proposition}
16	\newtheorem{definition}{Definition}
17	
18	\title{G-MFRM: Joint Estimation of Judge Bias and Benchmark Contamination\\for Fair LLM Evaluation}
19	
20	\author{Anonymous}
21	\date{}
22	
23	\begin{document}
24	\maketitle
25	
26	%% ============================================================
27	%% ABSTRACT
28	%% ============================================================
29	\begin{abstract}
30	LLM-as-a-judge evaluation faces two well-documented distortions: inter-judge bias (systematic severity differences across judges) and benchmark contamination (inflated scores on memorized items). Existing methods address these independently, but judge severity and contamination susceptibility are confounded: bias-only correction absorbs contamination effects into ability estimates, while contamination-only adjustment misattributes judge variation as contamination signal. We formalize this as an omitted variable bias problem and prove that sequential correction pipelines produce asymptotically biased ability estimates when judge severity and contamination are non-orthogonal. We propose the Gated Many-Facet Rasch Model (G-MFRM), a unified psychometric framework that jointly estimates model ability, item difficulty, judge severity, and per-model contamination susceptibility within a single calibration. G-MFRM uses externally-anchored exposure indicators and a three-stage estimation procedure to ensure identifiability.
31	On MT-Bench and Arena-Hard with 8 Large Language Model (LLM) judges evaluating 22 target models (203,520 evaluations), G-MFRM fair scores achieve Kendall $\tau = 0.86$ and $0.85$ with Chatbot Arena human votes, significantly outperforming the best sequential baseline ($p = 0.008$ and $p = 0.041$). Beyond ranking accuracy, G-MFRM produces interpretable per-model contamination estimates that correlate consistently across benchmarks ($r = 0.68$--$0.71$) and degrade gracefully to standard MFRM when contamination is absent.
32	\end{abstract}
33	
34	%% ============================================================
35	%% 1. INTRODUCTION
36	%% ============================================================
37	\section{Introduction}
38	
39	Automated evaluation with LLM judges has become the dominant paradigm for comparing language models on open-ended generation tasks. Benchmarks such as MT-Bench \citep{zheng2023judging}, Arena-Hard \citep{li2024crowdsourced}, and WildBench \citep{lin2024wildbench} rely on one or more LLM judges to score model outputs, and the resulting rankings drive both research priorities and deployment decisions.
40	
41	Two systematic distortions threaten the validity of these rankings. First, LLM judges exhibit significant inter-judge bias: different judges assign systematically different severity levels, and their agreement is modest (Fleiss' $\kappa \approx 0.41$ in our data). Second, benchmark contamination inflates scores when target models have memorized evaluation items during pre-training, a problem that grows as benchmarks age and training corpora expand.
42	
43	A growing literature addresses each distortion separately. CyclicJudge \citep{cyclicjudge2025} and UDA \citep{uda2025} correct judge bias through round-robin protocols or neural K-factor adjustment. ConStat \citep{constat2024} and DCR \citep{dcr2025} quantify contamination effects via reference variant comparisons. However, no existing work (across 12 surveyed papers through May 2026) jointly models both within a single estimation framework. This separation is not merely incomplete; it is structurally flawed.
44	
45	The core problem is \textit{omitted variable confounding}. When judge severity ($d_j$) and contamination susceptibility ($c_n \cdot e_i$) are both present but only one is modeled, the unmodeled factor is absorbed into other parameter estimates. A bias-only method treats contamination-inflated scores as genuine ability, producing overestimates for contaminated models. A contamination-only method attributes part of the judge-driven variance to contamination, distorting the contamination signal. Sequential pipelines (correct bias first, then contamination, or vice versa) do not resolve this: the first stage's estimates are already biased by the unmodeled facet, and the second stage inherits that bias.
46	
47	We formalize this confounding and prove that under non-orthogonality of $d_j$ and $c_n \cdot e_i$, sequential estimators are asymptotically biased with a predictable direction (Proposition~\ref{prop:bias}). Our Monte Carlo validation confirms that the first-order bias approximation correctly predicts the direction of bias in 97\% of conditions across 540 parameter configurations.
48	
49	We propose the \textbf{Gated Many-Facet Rasch Model (G-MFRM)}, a unified psychometric framework that resolves confounding by jointly estimating all facets. G-MFRM extends the classical Many-Facet Rasch Model (MFRM) with a gating mechanism inspired by DG-IRT \citep{dgirt2024}, incorporating externally-anchored item exposure indicators to model contamination. A three-stage estimation procedure ensures identifiability: (1) standard MFRM for initial parameter estimates, (2) exposure anchoring via ConStat delta scores and temporal signals, (3) joint Bayesian estimation of all parameters including per-model contamination susceptibility $c_n$.
50	
51	Our contributions are:
52	\begin{itemize}
53	    \item We formalize the confounding between judge bias and benchmark contamination as an omitted variable bias problem (Proposition~\ref{prop:bias}) and validate the bias direction empirically (Section~\ref{sec:proposition}).
54	    \item We propose G-MFRM, a joint estimation framework that produces bias-and-contamination-corrected ``fair scores'' along with interpretable per-model contamination estimates (Section~\ref{sec:method}).
55	    \item We evaluate G-MFRM on MT-Bench, Arena-Hard, and WildBench with 8 LLM judges and 22 target models, showing consistent improvements over 7 baselines and graceful degradation when contamination is low (Sections~\ref{sec:main_results}--\ref{sec:wildbench}).
56	\end{itemize}
57	
58	%% ============================================================
59	%% 2. BACKGROUND AND MOTIVATION
60	%% ============================================================
61	\section{Background and Motivation}
62	\label{sec:background}
63	
64	\subsection{Many-Facet Rasch Model}
65	
66	The Many-Facet Rasch Model (MFRM) \citep{linacre1989mfrm} extends item response theory to settings with multiple facets (e.g., examinees, items, raters). In LLM evaluation, we have three facets: model ability $\theta_n$, item difficulty $b_i$, and judge severity $d_j$. The probability of model $n$ receiving a high rating from judge $j$ on item $i$ is:
67	\begin{equation}
68	\label{eq:mfrm}
69	\log \frac{P(X_{nij} \geq k)}{P(X_{nij} < k)} = \theta_n - b_i - d_j - \tau_k
70	\end{equation}
71	where $\tau_k$ are threshold parameters. MFRM produces ``fair scores'' that separate model ability from judge and item effects, but it does not account for contamination.
72	
73	\subsection{Contamination as a Latent Facet}
74	
75	Benchmark contamination occurs when a target model has been exposed to evaluation items during training. Following the DG-IRT framework \citep{dgirt2024}, we model contamination as a multiplicative interaction: a model with contamination susceptibility $c_n$ gains an advantage $c_n \cdot e_i$ on item $i$ with exposure level $e_i$. This rank-1 structure captures the dominant contamination pattern where advantage is proportional to both model memorization tendency and item exposure.
76	
77	\subsection{The Confounding Problem: A Toy Example}
78	\label{sec:toy}
79	
80	Consider two models evaluated by two judges on items with varying exposure levels. Model A has high ability but low contamination ($\theta_A = 2, c_A = 0.1$). Model B has lower ability but high contamination ($\theta_B = 1, c_B = 1.5$). Judge 1 is lenient ($d_1 = -0.5$), Judge 2 is strict ($d_2 = 0.5$).
81	
82	Under a bias-only correction (e.g., standard MFRM), the contamination-inflated scores of Model B are treated as genuine ability. The estimated $\hat{\theta}_B$ absorbs the $c_B \cdot e_i$ term, producing $\hat{\theta}_B > \theta_B$. Conversely, under contamination-only correction, the differing judge severities create phantom contamination signals: if Judge 1 (lenient) happens to evaluate more high-exposure items, the contamination estimator conflates leniency with exposure effects.
83	
84	Sequential correction does not resolve this. If we first correct for judge bias, the resulting ``debiased'' scores still contain contamination inflation, and the subsequent contamination correction inherits these inflated baselines.
85	
86	\subsection{Formal Proposition}
87	\label{sec:proposition}
88	
89	\begin{proposition}
90	\label{prop:bias}
91	Let $\hat{\theta}^{seq}_n$ denote the sequential estimator of model ability (bias correction followed by contamination correction) and $\hat{\theta}^{joint}_n$ the joint estimator. Under non-orthogonality of $d_j$ and $c_n \cdot e_i$ (i.e., $\text{Cov}(d_j, c_n \cdot e_i) \neq 0$), the first-order asymptotic bias of the sequential estimator is:
92	\[
93	\text{Bias}(\hat{\theta}^{seq}_n) \approx \frac{\text{Cov}(d_j, c_n \cdot e_i)}{\text{Var}(d_j)} \cdot d_j + O(n^{-1})
94	\]
95	The direction of bias is determined by the sign of $\text{Cov}(d_j, c_n \cdot e_i)$, and the joint estimator is asymptotically unbiased under standard regularity conditions.
96	\end{proposition}
97	
98	We validate Proposition~\ref{prop:bias} via Monte Carlo simulation across 540 parameter configurations (varying correlation $\rho$ between $d_j$ and $c_n \cdot e_i$, contamination magnitude, and sample size) with 200 replications each.
99	
100	\begin{table}[t]
101	\centering
102	\caption{Monte Carlo validation of the first-order bias approximation. The proposition correctly predicts bias direction in 97\% of conditions. Bias magnitude increases with confounding correlation $\rho$.}
103	\label{tab:proposition}
104	\begin{tabular}{lcccc}
105	\toprule
106	$\rho(d_j, c \cdot e)$ & Bias (median) & Bias 95\% CI & Direction correct (\%) & Approx.\ corr. \\
107	\midrule
108	0.1 & 0.018 & [0.005, 0.038] & 97 & 0.91 \\
109	0.2 & 0.041 & [0.012, 0.079] & 97 & 0.91 \\
110	0.3 & 0.072 & [0.021, 0.134] & 97 & 0.91 \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	Table~\ref{tab:proposition} confirms that (1) the bias direction is correctly predicted in 97\% of conditions, (2) the first-order approximation correlates at $r = 0.91$ with the true bias, and (3) bias magnitude increases monotonically with $\rho$. The proposition holds across 89\% of the realistic parameter range; the 11\% of cases where regularity conditions are violated correspond to near-zero contamination ($c < 0.1$), where the bias itself is negligible.
116	
117	%% ============================================================
118	%% 3. METHOD
119	%% ============================================================
120	\section{The Gated Many-Facet Rasch Model}
121	\label{sec:method}
122	
123	\subsection{Model Formulation}
124	
125	G-MFRM extends the standard MFRM (Eq.~\ref{eq:mfrm}) with a contamination gating term:
126	\begin{equation}
127	\label{eq:gmfrm}
128	\log \frac{P(X_{nij} \geq k)}{P(X_{nij} < k)} = \theta_n + c_n \cdot e_i - b_i - d_j - \tau_k
129	\end{equation}
130	where $c_n \geq 0$ is the contamination susceptibility of model $n$ and $e_i \in [0, 1]$ is the exposure indicator for item $i$. The key design choices are:
131	
132	\textbf{Rank-1 contamination structure.} The interaction $c_n \cdot e_i$ assumes that contamination advantage is separable into a model factor and an item factor. This follows the LLTM tradition and provides a parsimonious first approximation. Person-fit diagnostics (Section~\ref{sec:fit}) can detect violations of this assumption.
133	
134	\textbf{External exposure anchoring.} Unlike educational testing (where exposure status is known to the administrator), benchmark contamination exposure is unknown. We estimate $e_i$ externally via a composite of ConStat delta scores, temporal signals, and memorization indicators (Section~\ref{sec:exposure}), then treat $e_i$ as fixed in Stage 3.
135	
136	\textbf{Non-negative $c_n$.} Contamination can only inflate scores (or have no effect), never deflate them. We enforce $c_n \geq 0$ via a half-normal prior.
137	
138	\subsection{Three-Stage Estimation}
139	
140	\textbf{Stage 1: Standard MFRM.} We fit the standard MFRM without contamination terms to obtain initial estimates $(\hat{\theta}_n^{(0)}, \hat{b}_i^{(0)}, \hat{d}_j^{(0)})$. These serve as informative priors for Stage 3.
141	
142	\textbf{Stage 2: Exposure Estimation.} We construct composite exposure indicators $e_i$ for each item by combining three signals: (a) ConStat delta scores (comparing model performance on original items vs.\ semantically equivalent rephrased variants), (b) temporal signals (benchmark publication date relative to model training cutoff), and (c) LogProber Safe Scores (memorization indicators from probing model internals). The composite reliability is $\alpha = 0.71$ (Section~\ref{sec:exposure}).
143	
144	\textbf{Stage 3: Joint Bayesian Estimation.} We fit the full G-MFRM (Eq.~\ref{eq:gmfrm}) using NumPyro MCMC with non-centered parameterization: 2,000 warmup steps, 4,000 posterior samples, and 4 chains. Stage 1 estimates provide informative priors. The exposure indicators $e_i$ from Stage 2 are treated as fixed, and $c_n$ is estimated as a latent parameter for each target model.
145	
146	\subsection{Graceful Degradation}
147	
148	When contamination is absent ($e_i \approx 0$ for all items or $c_n \approx 0$ for all models), the gating term vanishes and G-MFRM reduces to the standard MFRM. This means G-MFRM incurs no performance penalty on clean benchmarks, eliminating the risk of over-correction.
149	
150	%% ============================================================
151	%% 4. EXPERIMENTAL SETUP
152	%% ============================================================
153	\section{Experimental Setup}
154	\label{sec:setup}
155	
156	\subsection{Data Collection}
157	
158	We evaluate 22 target models using 8 LLM judges spanning 4 model families: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick, and Gemini 2.5 Pro. Each judge evaluates all target models on MT-Bench (80 items) and Arena-Hard (500 items) with position swapping, yielding a total of 203,520 evaluations.
159	
160	\begin{table}[t]
161	\centering
162	\caption{Data collection summary. Position swapping controls for position bias (average rate 12\%). Completion rate exceeds 97\% across all judges.}
163	\label{tab:data}
164	\begin{tabular}{lccccc}
165	\toprule
166	Statistic & Value \\
167	\midrule
168	Judges & 8 (5 open-source, 3 API) \\
169	Target models & 22 \\
170	Items (MT-Bench / Arena-Hard) & 80 / 500 \\
171	Total evaluations & 203,520 \\
172	Avg.\ position bias rate & 12\% \\
173	Inter-judge agreement (Fleiss' $\kappa$) & 0.41 \\
174	Judge completion rate & $\geq$97\% \\
175	Missing data & 2.8\% (MCAR) \\
176	\bottomrule
177	\end{tabular}
178	\end{table}
179	
180	The inter-judge agreement of $\kappa = 0.41$ (Table~\ref{tab:data}) reflects the typical level of LLM judge consistency, above chance but far from perfect. This moderate agreement is precisely the condition under which MFRM-based severity modeling provides value: if judges agreed perfectly, there would be no severity to separate.
181	
182	\subsection{Exposure Indicator Construction}
183	\label{sec:exposure}
184	
185	For each benchmark item, we generate rephrased reference variants and compute ConStat delta scores as the primary exposure signal. We combine these with temporal signals (benchmark release date vs.\ model training cutoff) and LogProber Safe Scores into a composite indicator $e_i$.
186	
187	\begin{table}[t]
188	\centering
189	\caption{Exposure indicator statistics by benchmark. MT-Bench, as an older benchmark, shows higher exposure rates. The composite $e_i$ achieves acceptable reliability ($\alpha = 0.71$).}
190	\label{tab:exposure}
191	\begin{tabular}{lccccc}
192	\toprule
193	Benchmark & $n$ items & Mean $e_i$ & Std $e_i$ & High exposure (\%) & Reliability $\alpha$ \\
194	\midrule
195	MT-Bench & 80 & 0.15 & 0.22 & 35 & 0.71 \\
196	Arena-Hard & 500 & 0.15 & 0.22 & 18 & 0.71 \\
197	\bottomrule
198	\end{tabular}
199	\end{table}
200	
201	MT-Bench has substantially higher exposure (35\% of items classified as high-exposure) compared to Arena-Hard (18\%), consistent with MT-Bench being older and more widely incorporated into training data. The rephrased reference variants pass a human equivalence check ($p = 0.23$), confirming that performance differences between original and rephrased items reflect memorization rather than semantic divergence. The ConStat delta scores correlate at $r = 0.74$ (rank correlation) with ground-truth exposure levels, and the temporal signal adds moderate complementary information ($r = 0.48$ with ConStat).
202	
203	\subsection{Baselines}
204	
205	We compare G-MFRM against 7 baselines:
206	\begin{itemize}
207	\item \textbf{Raw Average}: simple multi-judge average without correction.
208	\item \textbf{MFRM-only}: standard MFRM without contamination modeling.
209	\item \textbf{Sequential (bias-first)}: MFRM for bias correction, then post-hoc contamination adjustment.
210	\item \textbf{Sequential (contam-first)}: contamination adjustment first, then MFRM.
211	\item \textbf{CyclicJudge} \citep{cyclicjudge2025}: round-robin protocol eliminating average judge bias.
212	\item \textbf{DCR} \citep{dcr2025}: contamination-aware scoring via data characterization.
213	\item \textbf{UDA} \citep{uda2025}: neural K-factor adjustment for judge bias.
214	\item \textbf{Preference Leakage} \citep{prefleak2025}: leakage-aware evaluation protocol.
215	\end{itemize}
216	
217	All methods are evaluated by Kendall $\tau$ and Spearman $\rho$ correlation with Chatbot Arena human votes, with bootstrap 95\% confidence intervals.
218	
219	%% ============================================================
220	%% 5. RESULTS
221	%% ============================================================
222	\section{Results}
223	
224	\subsection{G-MFRM Model Fit}
225	\label{sec:fit}
226	
227	\begin{table}[t]
228	\centering
229	\caption{G-MFRM convergence diagnostics. The model achieves acceptable convergence: 92\% of parameters have $\hat{R} < 1.05$.}
230	\label{tab:convergence}
231	\begin{tabular}{lccc}
232	\toprule
233	Metric & Value & Threshold & Status \\
234	\midrule
235	Max $\hat{R}$ & 1.06 & $<$1.10 & Pass \\
236	\% params $\hat{R} > 1.05$ & 8\% & $<$10\% & Pass \\
237	Min ESS & 120 & $>$100 & Pass \\
238	Divergent transitions & 12 (0.075\%) & $<$1\% & Pass \\
239	Runtime & 3.2 hours & -- & -- \\
240	\bottomrule
241	\end{tabular}
242	\end{table}
243	
244	Table~\ref{tab:convergence} shows that G-MFRM converges adequately on real data. The 8\% of parameters with $\hat{R} > 1.05$ are concentrated among high-$c_n$ models where the contamination signal is noisier. We report 12 divergent transitions (0.075\% of total), within the acceptable range for complex hierarchical models.
245	
246	\begin{table}[t]
247	\centering
248	\caption{Facet fit statistics (infit/outfit mean-square). Judge severity shows the best fit; contamination shows the highest misfit rate, reflecting the rank-1 approximation's limitations.}
249	\label{tab:facet_fit}
250	\begin{tabular}{lcccccc}
251	\toprule
252	Facet & $n$ & Infit $\bar{x}$ & Outfit $\bar{x}$ & Misfit (\%) \\
253	\midrule
254	Model ability ($\theta_n$) & 22 & 1.02 & 1.08 & 9 \\
255	Item difficulty ($b_i$) & 580 & 0.99 & 1.05 & 7 \\
256	Judge severity ($d_j$) & 8 & 1.01 & 1.03 & 0 \\
257	Contamination ($c_n$) & 22 & 1.06 & 1.15 & 18 \\
258	\bottomrule
259	\end{tabular}
260	\end{table}
261	
262	Table~\ref{tab:facet_fit} reports fit statistics across all facets. Judge severity parameters show excellent fit (0\% misfit), as expected given relatively stable judge behavior. Contamination parameters show the highest misfit rate (18\%), with outfit mean-square of 1.15. This reflects cases where the rank-1 assumption ($c_n \cdot e_i$) does not fully capture the contamination pattern for individual models. We interpret $c_n$ as a contamination \textit{tendency} rather than a precise quantity and note rank-$k$ extensions as future work. The correlation between Stage 1 person-fit statistics ($l_z$) and Stage 3 contamination estimates is $r = 0.52$, providing moderate construct validity: models that exhibit poor fit under the standard MFRM tend to have higher estimated contamination.
263	
264	\subsection{Main Results}
265	\label{sec:main_results}
266	
267	\begin{table*}[t]
268	\centering
269	\caption{Method comparison across benchmarks. G-MFRM achieves the highest correlation with Chatbot Arena human votes on both MT-Bench and Arena-Hard. $\dagger$: significant at $p < 0.05$ vs.\ G-MFRM (Wilcoxon signed-rank test). Best in \textbf{bold}, second best \underline{underlined}.}
270	\label{tab:main}
271	\begin{tabular}{lcccccc}
272	\toprule
273	\multirow{2}{*}{Method} & \multicolumn{2}{c}{MT-Bench} & \multicolumn{2}{c}{Arena-Hard} & \multicolumn{2}{c}{Average} \\
274	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
275	& $\tau$ & $\rho$ & $\tau$ & $\rho$ & $\tau$ & $\rho$ \\
276	\midrule
277	Raw Average & 0.78$^\dagger$ & 0.82 & 0.76$^\dagger$ & 0.80 & 0.77 & 0.81 \\
278	MFRM-only & 0.83$^\dagger$ & 0.86 & 0.82$^\dagger$ & 0.85 & 0.83 & 0.86 \\
279	Seq.\ (bias-first) & \underline{0.84}$^\dagger$ & \underline{0.87} & \underline{0.83}$^\dagger$ & \underline{0.86} & \underline{0.84} & \underline{0.87} \\
280	Seq.\ (contam-first) & 0.83$^\dagger$ & 0.86 & 0.82$^\dagger$ & 0.85 & 0.83 & 0.86 \\
281	CyclicJudge & 0.82$^\dagger$ & 0.85 & 0.81$^\dagger$ & 0.84 & 0.82 & 0.85 \\
282	DCR & 0.81$^\dagger$ & 0.84 & 0.80$^\dagger$ & 0.83 & 0.81 & 0.84 \\
283	UDA & \underline{0.84}$^\dagger$ & \underline{0.87} & \underline{0.83}$^\dagger$ & \underline{0.86} & \underline{0.84} & \underline{0.87} \\
284	Pref.\ Leakage & 0.80$^\dagger$ & 0.83 & 0.79$^\dagger$ & 0.82 & 0.80 & 0.83 \\
285	\midrule
286	\textbf{G-MFRM} & \textbf{0.86} & \textbf{0.89} & \textbf{0.85} & \textbf{0.88} & \textbf{0.86} & \textbf{0.89} \\
287	\bottomrule
288	\end{tabular}
289	\end{table*}
290	
291	Table~\ref{tab:main} presents the main results. G-MFRM achieves the highest Kendall $\tau$ on both benchmarks: 0.86 on MT-Bench ($p = 0.008$ vs.\ best baseline) and 0.85 on Arena-Hard ($p = 0.041$). The improvement over the best sequential baseline is $\Delta\tau = 0.02$ on both benchmarks.
292	
293	Several patterns are informative. First, all correction methods outperform Raw Average, confirming that both bias and contamination distort rankings. Second, MFRM-only already provides substantial gains over Raw Average ($+0.05$/$+0.06$ in $\tau$), demonstrating the value of judge severity modeling. Third, methods that address only one distortion (CyclicJudge for bias, DCR for contamination) underperform sequential approaches that attempt both, consistent with our confounding analysis. Fourth, UDA matches the sequential (bias-first) baseline despite being a black-box method, but neither provides contamination estimates.
294	
295	The $\Delta\tau = 0.02$ improvement may appear modest in isolation. We emphasize two points. First, Proposition~\ref{prop:bias} establishes that the sequential estimator is \textit{asymptotically biased} regardless of the magnitude of the bias in any finite sample. Joint estimation is the methodologically correct approach. Second, G-MFRM's per-model contamination estimates (Section~\ref{sec:calibration}) constitute an independent contribution with practical value for benchmark auditing, a capability that no baseline provides.
296	
297	\subsection{Contamination Magnitude Calibration}
298	\label{sec:calibration}
299	
300	\begin{table}[t]
301	\centering
302	\caption{Contamination magnitude: real data vs.\ synthetic scenarios. Real contamination falls between the two synthetic settings, closer to the mild scenario (MVP-001).}
303	\label{tab:contamination}
304	\begin{tabular}{lccccc}
305	\toprule
306	Scenario & $\bar{c}$ & Std & \% $c > 1$ & G-MFRM $\tau$ & Seq.\ $\tau$ \\
307	\midrule
308	MVP-001 (mild) & $\sim$0.5 & -- & -- & -- & -- \\
309	Real data & 0.62 & 0.35 & 18 & 0.86 & 0.84 \\
310	MVP-003 (strong) & $\sim$1.5 & -- & -- & -- & -- \\
311	\bottomrule
312	\end{tabular}
313	\end{table}
314	
315	The estimated per-model contamination susceptibility $c_n$ has mean 0.62 (median 0.51, std 0.35), with values ranging from 0.08 to 1.41 across the 22 target models (Table~\ref{tab:contamination}). The distribution is right-skewed: 23\% of models show negligible contamination ($c_n < 0.2$) while 18\% show strong contamination ($c_n > 1.0$). This heterogeneity is the critical finding: average contamination appears moderate, but a substantial tail of heavily contaminated models exists.
316	
317	The distribution is statistically indistinguishable from the mild synthetic scenario MVP-001 ($p = 0.12$, KS test) but significantly different from the strong scenario MVP-003 ($p = 0.003$). This confirms that real-world contamination is less extreme than worst-case assumptions but too prevalent to ignore.
318	
319	Two model-level correlates emerge. Training recency correlates negatively with $c_n$ ($r = -0.43$): newer models tend to have lower contamination, likely because benchmark decontamination has become standard practice. Model size correlates weakly positively with $c_n$ ($r = 0.28$), consistent with larger models having greater memorization capacity.
320	
321	\subsection{Cross-Benchmark Generalization: WildBench}
322	\label{sec:wildbench}
323	
324	To test generalization, we replicate the full G-MFRM pipeline on WildBench (1,024 items) using the same 8 judges.
325	
326	\begin{table}[t]
327	\centering
328	\caption{WildBench replication. With only 12\% high-exposure items, G-MFRM's advantage is small and non-significant, demonstrating graceful degradation.}
329	\label{tab:wildbench}
330	\begin{tabular}{lccc}
331	\toprule
332	Method & WildBench $\tau$ & $\Delta\tau$ & $p$ \\
333	\midrule
334	Sequential & 0.83 & -- & -- \\
335	G-MFRM & 0.84 & +0.01 & 0.062 \\
336	\bottomrule
337	\end{tabular}
338	\end{table}
339	
340	On WildBench, G-MFRM achieves $\tau = 0.84$ compared to the sequential baseline's 0.83 (Table~\ref{tab:wildbench}). The difference ($\Delta\tau = 0.01$) is not statistically significant ($p = 0.062$). This is expected: WildBench has only 12\% high-exposure items, providing minimal signal for contamination correction. The result confirms G-MFRM's graceful degradation property: on clean benchmarks, it performs no worse than the sequential approach, adding no over-correction penalty.
341	
342	The per-model $c_n$ estimates from WildBench correlate at $r = 0.71$ with MT-Bench estimates and $r = 0.68$ with Arena-Hard estimates. This cross-benchmark consistency provides construct validity evidence: $c_n$ captures a genuine model-level property (memorization tendency) rather than benchmark-specific artifacts. Convergence on WildBench is slightly weaker ($\hat{R}_{max} = 1.07$, ESS$_{min} = 95$), reflecting the longer and more complex items that increase judge scoring variance.
343	
344	\subsection{Judge Count Sensitivity}
345	\label{sec:judge_sensitivity}
346	
347	\begin{table}[t]
348	\centering
349	\caption{Sensitivity to the number of judges. G-MFRM requires at least 4 judges to significantly outperform the sequential baseline. Performance saturates at 6 judges.}
350	\label{tab:judge_count}
351	\begin{tabular}{lcccc}
352	\toprule
353	$n$ judges & G-MFRM $\tau$ & Seq.\ $\tau$ & $\Delta\tau$ & Conv.\ rate (\%) \\
354	\midrule
355	2 & 0.80 & 0.80 & 0.00 & 65 \\
356	4 & 0.84 & 0.82 & 0.02 & 85 \\
357	6 & 0.85 & 0.83 & 0.02 & 95 \\
358	8 & 0.86 & 0.84 & 0.02 & 100 \\
359	\bottomrule
360	\end{tabular}
361	\end{table}
362	
363	Table~\ref{tab:judge_count} reports results from subsampling 2, 4, 6, and 8 judges (20 random subsets per configuration). With only 2 judges, G-MFRM cannot separate $d_j$ from $c_n \cdot e_i$, and it degrades to MFRM-equivalent performance. The convergence rate of 65\% at 2 judges reflects fundamental identifiability limitations. Four judges represent the minimum for G-MFRM to show a significant advantage, with performance saturating around 6 judges. This provides a practical guideline: the contamination correction benefit requires moderate multi-judge setups, but 8 judges are sufficient (no need for more).
364	
365	\subsection{Exposure Indicator Ablation}
366	\label{sec:ablation}
367	
368	\begin{table}[t]
369	\centering
370	\caption{Ablation of exposure indicator components. ConStat is the dominant signal (58\% relative importance). Removing it causes the largest $\tau$ drop and severely disrupts $c_n$ ranking.}
371	\label{tab:ablation}
372	\begin{tabular}{lcccc}
373	\toprule
374	Configuration & G-MFRM $\tau$ & $\Delta\tau$ & $c_n$ rank corr. & Rel.\ import. \\
375	\midrule
376	Full composite & \textbf{0.86} & -- & 1.00 & -- \\
377	$-$ ConStat & 0.83 & $-$0.03 & 0.61 & 0.58 \\
378	$-$ Temporal & 0.85 & $-$0.01 & 0.89 & 0.22 \\
379	$-$ LogProber & 0.85 & $-$0.01 & 0.91 & 0.20 \\
380	ConStat only & 0.85 & $-$0.01 & 0.82 & -- \\
381	\bottomrule
382	\end{tabular}
383	\end{table}
384	
385	Table~\ref{tab:ablation} presents leave-one-out ablation results for the composite exposure indicator. ConStat dominates with 58\% relative importance: removing it drops $\tau$ by 0.03 and reduces $c_n$ rank correlation to 0.61. Temporal signals and LogProber each contribute approximately 20\%. ConStat alone achieves $\tau = 0.85$, nearly matching the full composite ($\tau = 0.86$), suggesting it can serve as a practical minimum when other signals are unavailable.
386	
387	The low marginal contribution of temporal signals is somewhat surprising. Training cutoff dates provide only coarse-grained information (quarterly resolution at best), while contamination is an item-level phenomenon. LogProber complements ConStat by distinguishing memorization from generalization, but its contribution is limited in the median contamination regime.
388	
389	\subsection{Adversarial Robustness}
390	\label{sec:adversarial}
391	
392	\begin{table}[t]
393	\centering
394	\caption{Adversarial robustness by attack type. G-MFRM maintains an advantage over sequential under adversarial contamination, though paraphrase attacks are difficult to detect.}
395	\label{tab:adversarial}
396	\begin{tabular}{lcccc}
397	\toprule
398	Attack type & Detection & G-MFRM $\tau$ & Seq.\ $\tau$ & FPR \\
399	\midrule
400	Direct memorization & 0.88 & 0.85 & 0.80 & 0.08 \\
401	Partial memorization & 0.62 & 0.82 & 0.78 & 0.12 \\
402	Paraphrase & 0.45 & 0.79 & 0.76 & 0.16 \\
403	\midrule
404	Overall & 0.68 & 0.82 & 0.78 & 0.12 \\
405	\bottomrule
406	\end{tabular}
407	\end{table}
408	
409	Following the adversarial evaluation protocol of \citet{wang2026adversarial}, we test G-MFRM under three types of constructed contamination (Table~\ref{tab:adversarial}). Direct memorization is detected at 88\%, but paraphrase attacks (where items are memorized in rewritten form) are detected at only 45\%. This is a fundamental limitation: ConStat's reference variant method itself relies on paraphrasing, creating overlap with the attack mechanism.
410	
411	Under adversarial conditions, G-MFRM's advantage over sequential actually increases ($\Delta\tau = 0.04$ vs.\ 0.02 under clean conditions). Adversarial contamination amplifies the confounding between $d_j$ and $c_n \cdot e_i$, making the sequential estimator's bias more pronounced and joint estimation relatively more valuable. The false positive rate of 12\% indicates that approximately 12\% of clean models are incorrectly flagged as contaminated, an acceptable but non-trivial error rate. RMSE degrades by 15\% relative to clean conditions.
412	
413	%% ============================================================
414	%% 6. RELATED WORK
415	%% ============================================================
416	\section{Related Work}
417	
418	\paragraph{LLM Judge Bias.}
419	\citet{zheng2023judging} first documented systematic biases in LLM judges, including position bias, verbosity bias, and self-enhancement. CyclicJudge \citep{cyclicjudge2025} addresses bias via round-robin evaluation, eliminating average bias but not capturing item-specific effects. UDA \citep{uda2025} uses neural K-factor adjustment and achieves substantial bias reduction, but operates as a black box without interpretable parameters. Our work differs by treating judge severity as a facet within a psychometric model, jointly estimated with contamination.
420	
421	\paragraph{Benchmark Contamination.}
422	ConStat \citep{constat2024} introduced reference variant comparison for detecting contamination, achieving $r^2 = 0.94$ with true effects. DCR \citep{dcr2025} factors out contamination via data characterization. Preference Leakage \citep{prefleak2025} formalizes contamination as a form of data leakage in preference-based evaluation. These methods quantify contamination but do not account for judge variation. G-MFRM incorporates ConStat as an exposure signal within a joint framework.
423	
424	\paragraph{Psychometric Models for NLP Evaluation.}
425	Item response theory (IRT) has been applied to NLP benchmarks for calibrated difficulty estimation \citep{irt_nlp2020}. MFRM specifically models rater effects in human evaluation \citep{linacre1989mfrm}. DG-IRT \citep{dgirt2024} introduced gating mechanisms for differential item functioning in educational testing. G-MFRM adapts DG-IRT to the LLM evaluation setting with three structural changes: binary-to-continuous exposure, single-rater-to-multi-facet, and known-to-unknown exposure status.
426	
427	%% ============================================================
428	%% 7. CONCLUSION
429	%% ============================================================
430	\section{Conclusion}
431	
432	We have identified a structural flaw in the dominant approach to LLM evaluation calibration: sequential correction of judge bias and benchmark contamination produces biased estimates due to omitted variable confounding. G-MFRM resolves this by jointly estimating model ability, item difficulty, judge severity, and contamination susceptibility within a single psychometric framework.
433	
434	The empirical gains, while consistent, are moderate ($\Delta\tau = 0.02$ on MT-Bench and Arena-Hard). We argue that the methodological contribution extends beyond these numbers. First, Proposition~\ref{prop:bias} establishes that joint estimation is asymptotically correct regardless of the empirical effect size. Second, per-model contamination estimates provide a new tool for benchmark auditing, with cross-benchmark consistency ($r = 0.68$--$0.71$) validating their meaningfulness. Third, G-MFRM degrades gracefully to standard MFRM when contamination is absent, eliminating the downside risk of adoption.
435	
436	\paragraph{Limitations.}
437	Three limitations deserve attention. First, the rank-1 contamination structure ($c_n \cdot e_i$) does not capture heterogeneous contamination patterns (18\% misfit rate for $c_n$). Rank-$k$ extensions could address this at the cost of additional parameters. Second, exposure estimation depends heavily on ConStat (58\% relative importance), and paraphrase-based attacks reduce detection to 45\%. Improving exposure indicators for adversarial settings is an open problem. Third, G-MFRM requires at least 4 judges for identifiability, limiting applicability in single-judge evaluation setups.
438	
439	\bibliography{references}
440	\bibliographystyle{plainnat}
441	
442	\end{document}
443	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fecfb2be-ef33-4624-a5cf-49fe88436b36",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "e1af4bca-d616-4f6a-a9f0-c95eee413d51",
  "sourceToolAssistantUUID": "fecfb2be-ef33-4624-a5cf-49fe88436b36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T21:31:20.171Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CAfvvPG6VbgueNHKWNmapW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1af4bca-d616-4f6a-a9f0-c95eee413d51",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRmGMYoVRevoTtrdBL2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef415cb8-c6b2-479e-a007-3c9b1303482a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q1fpZ7XippD5rrRCdceW7u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14947,
      "cache_read_input_tokens": 27987,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14947
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 27987,
          "cache_creation_input_tokens": 14947,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14947,
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

_source line 36 · 2026-05-21T21:31:20.436Z_

<details><summary>↩ Tool result · `toolu_01CAfvvPG6VbgueNHKWNmapW`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立。Confounding claim 有真实数据强实证（degradation ≥20%），
2	  framework claim 通过收敛和诊断验证，empirical claim 通过 Kendall-τ 显著提升验证。 论文按 paper_framing
3	  原样推进：Section 2 用形式化命题 + 真实数据 toy example 双重论证 confounding， 主表展示 G-MFRM 全面优于 7 baselines，headline
4	  可写 "X% higher Kendall-τ"。 DG-IRT 迁移的 novelty 通过三阶段 pipeline 的非平凡适配（binary→continuous,
5	  external anchoring）自然建立。 无需降低任何 claim 强度。
6	
7	  '
8	imagined_experiments:
9	- name: multi_judge_data_collection
10	  plan_id: exp-001
11	  description: '8 judges（GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro,
12	    Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick, Gemini 2.5 Pro） 评估 22 个 target
13	    models，MT-Bench 80 items + Arena-Hard 500 items， position swap 产生双向评分。
14	
15	    '
16	  expected_results:
17	    n_judges: 8
18	    n_target_models: 22
19	    n_items_mtbench: 80
20	    n_items_arenahard: 500
21	    total_judgments_mtbench: 28160
22	    total_judgments_arenahard: 176000
23	    missing_rate_pct: 1.8
24	    position_bias_avg_swap_disagreement_pct: 12.5
25	    api_cost_usd: 780
26	    vllm_gpu_hours: 105
27	    inter_judge_agreement_fleiss_kappa: 0.41
28	    judge_severity_range_raw_std: 0.82
29	  result_rationale: 'best 档假设数据收集无重大缺失。8 个 judges 涵盖 4 家厂商 + 3 个开源， 缺失率 <2% 因 API
30	    和 vLLM 基础设施成熟。position swap disagreement ~12.5% 符合已知 LLM positional bias 文献（Zheng
31	    et al. 2023 报告 10-15%）。 inter-judge Fleiss κ≈0.41 处于 "moderate agreement" 范围，这正是
32	    G-MFRM 需要的场景——若 judges 高度一致则无需建模 severity。 judge severity raw std=0.82 表明 judges
33	    间存在可量化的系统性差异， 为后续 MFRM 的 d_j 估计提供充分变异。API 成本低于 $900 预算。
34	
35	    '
36	  tables:
37	  - name: 'Table S1: Data Collection Summary'
38	    columns:
39	    - Judge
40	    - Provider
41	    - Type
42	    - MT-Bench_judgments
43	    - Arena-Hard_judgments
44	    - Missing_pct
45	    - Avg_score
46	    rows:
47	    - - GPT-5.5
48	      - OpenAI
49	      - API
50	      - 3520
51	      - 22000
52	      - 1.2
53	      - 7.84
54	    - - Claude Opus 4.7
55	      - Anthropic
56	      - API
57	      - 3520
58	      - 22000
59	      - 0.8
60	      - 7.52
61	    - - Claude Sonnet 4.6
62	      - Anthropic
63	      - API
64	      - 3520
65	      - 22000
66	      - 1.1
67	      - 7.71
68	    - - DeepSeek-V4-Pro
69	      - DeepSeek
70	      - API
71	      - 3520
72	      - 22000
73	      - 2.0
74	      - 7.63
75	    - - Qwen3-235B-A22B
76	      - Alibaba
77	      - vLLM
78	      - 3520
79	      - 22000
80	      - 2.5
81	      - 7.45
82	    - - Qwen3.6-27B
83	      - Alibaba
84	      - vLLM
85	      - 3520
86	      - 22000
87	      - 3.1
88	      - 7.28
89	    - - Llama 4 Maverick
90	      - Meta
91	      - vLLM
92	      - 3520
93	      - 22000
94	      - 2.8
95	      - 7.39
96	    - - Gemini 2.5 Pro
97	      - Google
98	      - API
99	      - 3520
100	      - 22000
101	      - 1.5
102	      - 7.68
103	  figures_description:
104	  - 'Figure S1: Judge severity heatmap (22 models × 8 judges), 色彩编码 raw score deviation
105	    from item mean, 展示 judges 间系统性差异模式'
106	  analysis: '数据质量充分支撑后续全部实验。缺失率 1.8% 可用 MCMC 内自然处理（missing at random 假设合理， 缺失主要来自
107	    API timeout 而非 systematic）。8 judges 的 severity 分布有足够变异（std=0.82）， 开源 judges（Qwen3.6-27B,
108	    Llama 4 Maverick）系统性偏低 0.3-0.4 分， 为 d_j 估计提供了清晰信号。
109	
110	    '
111	- name: constat_exposure_estimation
112	  plan_id: exp-002
113	  description: '对 MT-Bench 80 + Arena-Hard 500 items 生成 reference variants（GPT-5.5
114	    rephrased）， 人工抽检 50 items 验证语义等价，运行 ConStat pipeline 计算 per-item exposure e_i，
115	    结合 temporal signals（release date proximity）形成 composite exposure indicator。
116	
117	    '
118	  expected_results:
119	    n_items_total: 580
120	    n_reference_variants_per_item: 3
121	    human_equivalence_check_n: 50
122	    human_equivalence_pass_rate_pct: 94.0
123	    constat_delta_mean: 0.38
124	    constat_delta_std: 0.27
125	    constat_rank_corr_with_temporal: 0.72
126	    composite_e_i_mean: 0.55
127	    composite_e_i_std: 0.31
128	    items_high_exposure_pct: 28.4
129	    items_low_exposure_pct: 35.2
130	    mtbench_avg_e_i: 0.68
131	    arenahard_avg_e_i: 0.49
132	  result_rationale: 'best 档假设 ConStat e_i 估计与真实曝光高度一致（rank correlation ≥ 0.85）。 MT-Bench
133	    作为 2023 年发布的广泛使用 benchmark，items 曝光量显著高于 Arena-Hard（动态更新），体现为 MT-Bench avg e_i=0.68
134	    > Arena-Hard 0.49。 ConStat delta 与 temporal signal 相关 r=0.72 表明两个独立信号的一致性， 增强了
135	    composite indicator 的可信度。human equivalence 94% pass rate 表明 reference variants
136	    质量高，未引入语义偏移。28.4% items 高曝光 提供了充足的 contamination signal 变异范围。
137	
138	    '
139	  tables:
140	  - name: 'Table S2: Exposure Estimation Summary by Benchmark'
141	    columns:
142	    - Benchmark
143	    - N_items
144	    - Mean_e_i
145	    - Std_e_i
146	    - High_exposure_pct
147	    - ConStat_delta_mean
148	    rows:
149	    - - MT-Bench
150	      - 80
151	      - 0.68
152	      - 0.24
153	      - 42.5
154	      - 0.51
155	    - - Arena-Hard
156	      - 500
157	      - 0.49
158	      - 0.31
159	      - 25.2
160	      - 0.34
161	    - - Combined
162	      - 580
163	      - 0.52
164	      - 0.3
165	      - 28.4
166	      - 0.36
167	  figures_description:
168	  - 'Figure S2: e_i 分布直方图，MT-Bench vs Arena-Hard 分面，展示 MT-Bench 右偏（高曝光更多）'
169	  - 'Figure S3: ConStat delta vs temporal proximity scatter，r=0.72，展示两个独立信号的一致性'
170	  analysis: 'Exposure estimation 质量足够支撑 Stage 2 anchoring。MT-Bench 的高曝光占比（42.5%） 和
171	    Arena-Hard 的相对低曝光形成了自然对比，有利于 contamination 效应的识别。 Composite indicator 结合了 ConStat
172	    的 behavioral signal 和 temporal 的 prior information， 比单独使用任一信号更鲁棒。这为 exp-003 的
173	    Stage 2 提供了可靠的 external anchor。
174	
175	    '
176	- name: gmfrm_real_data_fit
177	  plan_id: exp-003
178	  description: '三阶段 pipeline 在真实数据上拟合：Stage 1 MFRM 估计 θ,b,d； Stage 2 用 exp-002 的 e_i
179	    作为 external anchor； Stage 3 joint gated model 同时估计所有 facets 含 latent c_n。 NumPyro
180	    MCMC (warmup=2000, samples=4000, chains=4, NCP, target_accept=0.95)。
181	
182	    '
183	  expected_results:
184	    convergence_max_rhat: 1.02
185	    convergence_min_ess: 312
186	    convergence_all_params_rhat_below_1_05: true
187	    convergence_pct_params_rhat_below_1_01: 87.3
188	    real_c_n_mean: 1.18
189	    real_c_n_std: 0.64
190	    real_c_n_median: 1.05
191	    pct_models_c_n_above_0_8: 45.5
192	    pct_models_c_n_above_1_5: 18.2
193	    c_n_range:
194	    - 0.12
195	    - 2.41
196	    kendall_tau_arena_mtbench: 0.91
197	    kendall_tau_arena_arenahard: 0.9
198	    kendall_tau_arena_combined: 0.91
199	    spearman_rho_arena_combined: 0.96
200	    kendall_tau_sequential_combined: 0.85
201	    delta_tau_vs_sequential: 0.06
202	    rmse_theta_vs_sequential_reduction_pct: 34.2
203	    wilcoxon_p_joint_vs_seq: 3.2e-05
204	    scatter_pearson_r_seq_bias: 0.61
205	    confounding_theta_rmse_degradation_pct: 28.5
206	    d_j_c_n_e_i_correlation_abs: 0.37
207	    runtime_hours: 2.8
208	    total_mcmc_samples: 16000
209	  result_rationale: 'best 档核心假设：真实 c̄≥1.0。c_n_mean=1.18 落在 [1.0, 2.0] 范围内， 接近 mvp_003
210	    设定（mvp_003 DGP 中 c_n~N(1.2,0.5)），表明真实污染量级 确实不是边缘现象。45.5% 模型 c_n>0.8（远超 30% 阈值），说明污染在主流模型中普遍存在。
211	    收敛优于 mvp_003（R̂=1.02 < 1.03），因为真实数据的 N=580 items 远多于 合成数据的 100 items，提供了更多信息量。ESS=312
212	    > 200 阈值， real data 的 item 数量和 judge 数量给 MCMC 更充分的似然信号。 Kendall-τ=0.91 vs sequential
213	    0.85，delta=0.06 落在 [0.04, 0.10] 范围中部， 因为真实数据噪声高于合成但 contamination 量级充足。 |ρ(d_j,
214	    c_n·e_i)|=0.37 > 0.3 阈值——严格 judges 倾向于对高污染模型给出更极端分数， confounding 在真实数据上可观测。RMSE
215	    degradation 28.5% < mvp_003 的 43.8% 但仍 >20% 阈值，因为真实数据中 confounding 结构不如合成 DGP
216	    极端但仍显著。
217	
218	    '
219	  tables:
220	  - name: 'Table 1 (Main): Model Ability Estimates — G-MFRM vs Sequential'
221	    columns:
222	    - Model
223	    - Arena_Elo
224	    - G-MFRM_θ
225	    - Sequential_θ
226	    - Raw_Avg
227	    - c_n_estimate
228	    note: 22 rows, top-5 and bottom-5 shown for illustration
229	    rows:
230	    - - GPT-5.5
231	      - 1320
232	      - 1.82
233	      - 1.95
234	      - 8.12
235	      - 1.63
236	    - - Claude Opus 4.7
237	      - 1305
238	      - 1.74
239	      - 1.82
240	      - 7.98
241	      - 1.41
242	    - - DeepSeek-V4-Pro
243	      - 1285
244	      - 1.61
245	      - 1.73
246	      - 7.85
247	      - 1.52
248	    - - Gemini 2.5 Pro
249	      - 1275
250	      - 1.55
251	      - 1.58
252	      - 7.79
253	      - 0.89
254	    - - Claude Sonnet 4.6
255	      - 1260
256	      - 1.48
257	      - 1.51
258	      - 7.72
259	      - 1.15
260	    - - '...'
261	      - '...'
262	      - '...'
263	      - '...'
264	      - '...'
265	      - '...'
266	    - - Phi-4-mini
267	      - 1085
268	      - 0.52
269	      - 0.48
270	      - 6.41
271	      - 0.35
272	    - - Llama-3.3-8B
273	      - 1065
274	      - 0.38
275	      - 0.41
276	      - 6.22
277	      - 0.28
278	  - name: 'Table S3: MCMC Convergence Diagnostics Summary'
279	    columns:
280	    - Parameter_group
281	    - N_params
282	    - Max_Rhat
283	    - Min_ESS
284	    - Median_ESS
285	    - Pct_Rhat_below_1_01
286	    rows:
287	    - - theta (ability)
288	      - 22
289	      - 1.01
290	      - 412
291	      - 1850
292	      - 95.5
293	    - - b (difficulty)
294	      - 580
295	      - 1.02
296	      - 312
297	      - 890
298	      - 85.2
299	    - - d (severity)
300	      - 8
301	      - 1.0
302	      - 2450
303	      - 3100
304	      - 100.0
305	    - - c (contamination)
306	      - 22
307	      - 1.02
308	      - 345
309	      - 1620
310	      - 86.4
311	    - - sigma_priors
312	      - 4
313	      - 1.01
314	      - 1890
315	      - 2340
316	      - 100.0
317	  figures_description:
318	  - 'Figure 2: Bias scatter — x=c_n estimate, y=(θ_sequential − θ_joint), Pearson
319	    r=0.61, 展示 sequential 对高污染模型系统性高估 ability'
320	  - 'Figure 3: c_n posterior distribution ridge plot (22 models), 按 Arena Elo 排序,
321	    展示高 Elo 模型倾向于高 c_n'
322	  - 'Figure S4: Trace plots for representative parameters (θ_1, d_3, c_5), 4 chains
323	    混合良好'
324	  analysis: '核心发现：真实数据上 c̄=1.18 确认污染非边缘现象，G-MFRM 显著优于 sequential（τ +0.06, p=3.2e-5）。
325	    confounding 在真实数据上通过三条证据链确认：(1) |ρ|=0.37 表明 d_j 与 c_n·e_i 非正交， (2) RMSE degradation
326	    28.5% 表明忽略任一 facet 导致显著偏差， (3) bias scatter r=0.61 表明 sequential 对高污染模型系统性高估。
327	    收敛良好（R̂≤1.02, ESS≥312），支撑 framework claim。
328	
329	    '
330	- name: baseline_comparison
331	  plan_id: exp-004
332	  description: '在同一数据上比较 G-MFRM 与 7 个 baselines： (1) Raw multi-judge average, (2)
333	    MFRM-only, (3) Sequential pipeline, (4) CyclicJudge, (5) DCR Factor, (6) UDA,
334	    (7) Preference Leakage calibration。 主指标 Kendall-τ 和 Spearman-ρ with Chatbot Arena
335	    votes， 分 MT-Bench 和 Arena-Hard 两个 benchmark 报告。
336	
337	    '
338	  expected_results:
339	    raw_average_tau: 0.82
340	    mfrm_only_tau: 0.84
341	    sequential_tau: 0.85
342	    cyclicjudge_tau: 0.84
343	    dcr_factor_tau: 0.83
344	    uda_tau: 0.86
345	    pref_leakage_tau: 0.83
346	    gmfrm_tau: 0.91
347	    raw_average_rho: 0.89
348	    mfrm_only_rho: 0.91
349	    sequential_rho: 0.92
350	    cyclicjudge_rho: 0.91
351	    dcr_factor_rho: 0.9
352	    uda_rho: 0.93
353	    pref_leakage_rho: 0.9
354	    gmfrm_rho: 0.96
355	    best_baseline_name: UDA
356	    best_baseline_tau: 0.86
357	    delta_tau_vs_best_baseline: 0.05
358	    wilcoxon_p_gmfrm_vs_uda: 0.00087
359	    wilcoxon_p_gmfrm_vs_sequential: 3.2e-05
360	    wilcoxon_p_gmfrm_vs_raw: 1.4e-06
361	    delta_tau_95ci:
362	    - 0.02
363	    - 0.08
364	  result_rationale: 'best 档下 G-MFRM τ=0.91 落在 [0.88, 0.94] 范围，best baseline τ=0.86
365	    落在 [0.82, 0.87] 范围。 UDA 是最强 baseline（τ=0.86）因为其 neural K-factor 部分捕捉了 judge 间差异，
366	    但它是 black-box 且 contamination-unaware，无法处理 c_n 导致的系统性偏差。 CyclicJudge（τ=0.84）消除了平均
367	    judge bias 但无法捕捉 item-specific severity 差异。 DCR（τ=0.83）仅建模 contamination 而忽略 judge
368	    severity，吸收了部分 d_j 效应。 Sequential（τ=0.85）优于单独 correction 但仍受 confounding bias
369	    影响。 MFRM-only（τ=0.84）与 CyclicJudge 相当，因为两者都只建模 judge 效应。 delta=0.05 vs UDA 在 bootstrap
370	    95% CI [0.02, 0.08] 中显著， Wilcoxon p=8.7e-4 落在 [1e-6, 0.001] 范围内。 G-MFRM 在所有 7
371	    baselines 上显著优于，支撑 headline claim。
372	
373	    '
374	  tables:
375	  - name: 'Table 2 (Main): Baseline Comparison — Kendall-τ with Chatbot Arena'
376	    columns:
377	    - Method
378	    - Bias_Correction
379	    - Contam_Correction
380	    - Joint
381	    - MT-Bench_τ
382	    - Arena-Hard_τ
383	    - Combined_τ
384	    - Combined_ρ
385	    rows:
386	    - - Raw Average
387	      - ✗
388	      - ✗
389	      - ✗
390	      - 0.8
391	      - 0.83
392	      - 0.82
393	      - 0.89
394	    - - MFRM-only
395	      - ✓
396	      - ✗
397	      - —
398	      - 0.83
399	      - 0.85
400	      - 0.84
401	      - 0.91
402	    - - CyclicJudge
403	      - ✓
404	      - ✗
405	      - —
406	      - 0.82
407	      - 0.85
408	      - 0.84
409	      - 0.91
410	    - - DCR Factor
411	      - ✗
412	      - ✓
413	      - —
414	      - 0.81
415	      - 0.84
416	      - 0.83
417	      - 0.9
418	    - - Pref Leakage
419	      - ✗
420	      - ✓
421	      - —
422	      - 0.82
423	      - 0.84
424	      - 0.83
425	      - 0.9
426	    - - Sequential
427	      - ✓
428	      - ✓
429	      - ✗
430	      - 0.84
431	      - 0.86
432	      - 0.85
433	      - 0.92
434	    - - UDA
435	      - ✓(neural)
436	      - ✗
437	      - —
438	      - 0.85
439	      - 0.87
440	      - 0.86
441	      - 0.93
442	    - - '**G-MFRM (ours)**'
443	      - ✓
444	      - ✓
445	      - ✓
446	      - '**0.90**'
447	      - '**0.91**'
448	      - '**0.91**'
449	      - '**0.96**'
450	  - name: 'Table S4: Pairwise Significance (Wilcoxon p-values, G-MFRM vs each baseline)'
451	    columns:
452	    - Baseline
453	    - p_value_tau
454	    - p_value_rho
455	    - Significant_at_0_01
456	    rows:
457	    - - Raw Average
458	      - 1.4e-06
459	      - 2.1e-06
460	      - ✓
461	    - - MFRM-only
462	      - 5.8e-05
463	      - 8.3e-05
464	      - ✓
465	    - - CyclicJudge
466	      - 7.2e-05
467	      - 0.00011
468	      - ✓
469	    - - DCR Factor
470	      - 2.3e-05
471	      - 3.5e-05
472	      - ✓
473	    - - Pref Leakage
474	      - 3.1e-05
475	      - 4.7e-05
476	      - ✓
477	    - - Sequential
478	      - 3.2e-05
479	      - 4.9e-05
480	      - ✓
481	    - - UDA
482	      - 0.00087
483	      - 0.0012
484	      - ✓
485	  figures_description:
486	  - 'Figure 4: Bar chart — Kendall-τ with 95% bootstrap CI for all 8 methods, 按 τ
487	    排序, G-MFRM 显著高于全部 baselines'
488	  - 'Figure S5: Per-model rank comparison heatmap — rows=models, cols=methods, 色彩编码
489	    rank deviation from Arena Elo rank'
490	  analysis: 'G-MFRM 在全部 7 baselines 上显著优于，最强 baseline UDA 的差距也在统计上显著（p<0.001）。 关键观察：bias-only
491	    方法（MFRM, CyclicJudge）和 contam-only 方法（DCR, PrefLeakage） 性能相近（τ=0.83-0.84），sequential
492	    小幅提升至 0.85 但受 confounding 限制， 只有 joint estimation 实现了 τ=0.91 的跳跃。这一模式直接支撑 confounding
493	    claim： sequential 无法完全解决两个 facet 的交互效应。
494	
495	    '
496	- name: contamination_magnitude_calibration
497	  plan_id: exp-005
498	  description: '将 exp-003 估计的真实 c_n 分布与 mvp_001/002/003 的合成 DGP 设定对比， 确定真实污染量级落在哪个区间，评估对论文
499	    claim 强度的影响。
500	
501	    '
502	  expected_results:
503	    real_c_n_mean: 1.18
504	    real_c_n_std: 0.64
505	    real_c_n_median: 1.05
506	    closest_mvp: mvp_003
507	    mvp_001_c_mean: 0.5
508	    mvp_002_c_mean: 1.5
509	    mvp_003_c_mean: 1.2
510	    distance_to_mvp_003: 0.02
511	    distance_to_mvp_001: 0.68
512	    distance_to_mvp_002: 0.32
513	    ks_test_vs_mvp_003_p: 0.41
514	    pct_models_in_mvp_001_regime: 22.7
515	    pct_models_in_mvp_003_regime: 54.5
516	    pct_models_in_mvp_002_regime: 22.7
517	    top3_contaminated_models:
518	    - GPT-5.5
519	    - DeepSeek-V4-Pro
520	    - Claude Opus 4.7
521	    top3_clean_models:
522	    - Phi-4-mini
523	    - Llama-3.3-8B
524	    - Mistral-Small-3.2
525	  result_rationale: 'best 档假设 c̄≥1.0。c_n_mean=1.18 最接近 mvp_003（c̄=1.2）， KS test p=0.41
526	    表明真实分布与 mvp_003 DGP 不可区分。这是 best 档的核心验证： 真实污染量级确实接近 mvp_003 设定而非 mvp_001（弱），论文
527	    story 完全成立。 高 Elo 模型（GPT-5.5, Claude Opus 4.7, DeepSeek-V4-Pro）c_n 最高（1.4-2.4），
528	    因为它们训练数据最多、最可能包含 benchmark items。小模型（Phi-4-mini, Llama-3.3-8B） c_n 低（0.1-0.4），因为训练数据量和质量有限，benchmark
529	    泄漏概率低。 这种结构性模式增强了 c_n 估计的 face validity。
530	
531	    '
532	  tables:
533	  - name: 'Table S5: Real vs Synthetic Contamination Distribution Comparison'
534	    columns:
535	    - Distribution
536	    - Mean
537	    - Std
538	    - Median
539	    - Q25
540	    - Q75
541	    - KS_p_vs_real
542	    rows:
543	    - - Real data
544	      - 1.18
545	      - 0.64
546	      - 1.05
547	      - 0.62
548	      - 1.58
549	      - —
550	    - - mvp_001 DGP
551	      - 0.5
552	      - 0.3
553	      - 0.45
554	      - 0.28
555	      - 0.68
556	      - 0.001
557	    - - mvp_002 DGP
558	      - 1.5
559	      - 0.5
560	      - 1.48
561	      - 1.15
562	      - 1.82
563	      - 0.12
564	    - - mvp_003 DGP
565	      - 1.2
566	      - 0.5
567	      - 1.18
568	      - 0.82
569	      - 1.55
570	      - 0.41
571	  figures_description:
572	  - 'Figure S6: 真实 c_n 分布 vs mvp_001/002/003 DGP 分布叠加密度图，展示真实数据最接近 mvp_003'
573	  - 'Figure S7: 模型 c_n vs Arena Elo scatter (r=0.58), 展示高 Elo 模型更容易被污染'
574	  analysis: '真实污染量级与 mvp_003 高度一致（KS p=0.41），远非 mvp_001 的弱污染场景。 这意味着 mvp_003 的合成结果（RMSE
575	    −43.8%, τ +6.3pp）是对真实场景的合理预测， real data 上观测到的效应量（RMSE −34.2%, τ +0.06）与之一致但略小，
576	    可归因于真实数据中 confounding 结构不如 DGP 极端。 c_n 与 Elo 正相关（r=0.58）提供了额外的 construct validity：
577	    被更多使用的强模型更可能接触 benchmark data。
578	
579	    '
580	- name: judge_count_sensitivity
581	  plan_id: exp-006
582	  description: '从 8 judges 中抽取子集（2, 4, 6 judges），对每个子集重新拟合 G-MFRM， 测量 Kendall-τ 随
583	    judge 数量的变化。每个 judge 数量随机抽取 20 次取均值。 确定 G-MFRM 优于 sequential 的最小 judge 数量。
584	
585	    '
586	  expected_results:
587	    tau_2_judges_gmfrm: 0.86
588	    tau_2_judges_sequential: 0.84
589	    tau_4_judges_gmfrm: 0.89
590	    tau_4_judges_sequential: 0.85
591	    tau_6_judges_gmfrm: 0.9
592	    tau_6_judges_sequential: 0.85
593	    tau_8_judges_gmfrm: 0.91
594	    tau_8_judges_sequential: 0.85
595	    min_judges_for_significant_improvement: 4
596	    delta_tau_2_judges: 0.02
597	    delta_tau_4_judges: 0.04
598	    delta_tau_6_judges: 0.05
599	    delta_tau_8_judges: 0.06
600	    p_value_at_4_judges: 0.008
601	    p_value_at_2_judges: 0.14
602	    convergence_2_judges_max_rhat: 1.04
603	    convergence_4_judges_max_rhat: 1.03
604	  result_rationale: 'G-MFRM 的优势随 judge 数量增加而单调增长，因为更多 judges 提供了更好的 d_j 和 c_n 可辨识性——judge
605	    severity 的 cross-information 帮助分离 confounding。 2 judges 时 G-MFRM 仍优于 sequential（Δτ=0.02），但不显著（p=0.14），
606	    因为 2 judges 的 d_j 估计不稳定，gating mechanism 无法充分发挥。 4 judges 是临界点（p=0.008<0.01），此后优势稳定。
607	    Sequential 的 τ 对 judge 数量不敏感（0.84-0.85），因为它的 confounding bias 不因更多 judges 而消除——这是结构性问题而非数据量问题。
608	    这一对比直接展示了 joint vs sequential 的本质差异。
609	
610	    '
611	  tables:
612	  - name: 'Table 3: Judge Count Sensitivity Analysis'
613	    columns:
614	    - N_judges
615	    - G-MFRM_τ
616	    - Sequential_τ
617	    - Δτ
618	    - p_value
619	    - Max_Rhat
620	    - Min_ESS
621	    rows:
622	    - - 2
623	      - 0.86±0.03
624	      - 0.84±0.02
625	      - 0.02
626	      - 0.14
627	      - 1.04
628	      - 185
629	    - - 4
630	      - 0.89±0.02
631	      - 0.85±0.02
632	      - 0.04
633	      - 0.008
634	      - 1.03
635	      - 265
636	    - - 6
637	      - 0.90±0.01
638	      - 0.85±0.01
639	      - 0.05
640	      - 0.001
641	      - 1.02
642	      - 298
643	    - - 8
644	      - 0.91±0.01
645	      - 0.85±0.01
646	      - 0.06
647	      - 3.2e-05
648	      - 1.02
649	      - 312
650	  figures_description:
651	  - 'Figure 5: Line plot — Kendall-τ vs N_judges for G-MFRM (blue) and Sequential
652	    (red), shaded 95% CI, 展示 G-MFRM 收益递增而 sequential 平坦'
653	  analysis: '实用建议：4 judges 是 G-MFRM 优势显著的最低门槛。 这对 practitioner 有价值：即使只有 4 个 judges，joint
654	    estimation 也值得。 Sequential 的平坦曲线是 confounding claim 的另一个实证支撑—— 增加数据量（更多 judges）不能修复结构性模型误设。
655	
656	    '
657	- name: exposure_indicator_ablation
658	  plan_id: exp-007
659	  description: 'Leave-one-out ablation：依次移除 ConStat delta、temporal signal、LogProber
660	    Safe Score 中的一个 exposure indicator，重新拟合 G-MFRM，比较 Kendall-τ 变化。 同时测试 single-indicator
661	    版本。
662	
663	    '
664	  expected_results:
665	    full_composite_tau: 0.91
666	    without_constat_tau: 0.88
667	    without_temporal_tau: 0.9
668	    without_logprober_tau: 0.9
669	    constat_only_tau: 0.9
670	    temporal_only_tau: 0.87
671	    logprober_only_tau: 0.87
672	    constat_marginal_contribution: 0.03
673	    temporal_marginal_contribution: 0.01
674	    logprober_marginal_contribution: 0.01
675	    constat_rank_corr_with_c_n: 0.81
676	    temporal_rank_corr_with_c_n: 0.62
677	    logprober_rank_corr_with_c_n: 0.59
678	  result_rationale: 'ConStat 是最关键的 exposure indicator（marginal contribution +0.03），
679	    因为它直接测量 behavioral contamination signal（原始 vs rephrased 表现差异）， 与 c_n 的 rank correlation
680	    最高（0.81）。移除 ConStat 后 τ 从 0.91 降至 0.88， 仍优于所有 baselines（best baseline UDA τ=0.86），说明
681	    G-MFRM 的优势 不完全依赖于 exposure estimation 质量——joint calibration 框架本身就有结构性优势。 Temporal
682	    和 LogProber 各贡献 0.01，它们提供的信息与 ConStat 部分重叠。 ConStat-only 版本（τ=0.90）已接近 full composite（0.91），
683	    进一步确认 ConStat 是 Stage 2 的核心。
684	
685	    '
686	  tables:
687	  - name: 'Table 4: Exposure Indicator Ablation'
688	    columns:
689	    - Configuration
690	    - Indicators_used
691	    - Kendall_τ
692	    - Δτ_vs_full
693	    - Rank_corr_with_c_n
694	    rows:
695	    - - Full composite
696	      - ConStat + Temporal + LogProber
697	      - 0.91
698	      - —
699	      - 0.85
700	    - - w/o ConStat
701	      - Temporal + LogProber
702	      - 0.88
703	      - -0.03
704	      - 0.68
705	    - - w/o Temporal
706	      - ConStat + LogProber
707	      - 0.9
708	      - -0.01
709	      - 0.82
710	    - - w/o LogProber
711	      - ConStat + Temporal
712	      - 0.9
713	      - -0.01
714	      - 0.83
715	    - - ConStat only
716	      - ConStat
717	      - 0.9
718	      - -0.01
719	      - 0.81
720	    - - Temporal only
721	      - Temporal
722	      - 0.87
723	      - -0.04
724	      - 0.62
725	    - - LogProber only
726	      - LogProber
727	      - 0.87
728	      - -0.04
729	      - 0.59
730	    - - No exposure (MFRM-only)
731	      - None
732	      - 0.84
733	      - -0.07
734	      - —
735	  figures_description:
736	  - 'Figure S8: Bar chart — leave-one-out Kendall-τ with error bars, 标注每个 indicator
737	    的 marginal contribution'
738	  analysis: 'ConStat 是 Stage 2 的支柱，但 G-MFRM 即使在 ConStat 缺失时仍优于 sequential（0.88 > 0.85），
739	    表明 joint framework 的结构性优势独立于 exposure estimation 质量。 这回应了潜在 reviewer 质疑："如果 ConStat
740	    不准怎么办？"—— 答案是 G-MFRM 优雅退化但不崩溃。
741	
742	    '
743	- name: facet_fit_diagnostics
744	  plan_id: exp-008
745	  description: '报告全部 facets（θ, b, d, c）的 infit/outfit MNSQ， 标记 misfitting elements（MNSQ
746	    > 1.3 或 < 0.7）。 比较 Stage 1 person-fit 指标（lz, EMRi）与 Stage 3 c_n 估计的一致性。
747	
748	    '
749	  expected_results:
750	    theta_infit_mean: 1.01
751	    theta_infit_range:
752	    - 0.78
753	    - 1.25
754	    theta_outfit_mean: 1.03
755	    theta_pct_misfit: 4.5
756	    b_infit_mean: 1.0
757	    b_infit_range:
758	    - 0.65
759	    - 1.42
760	    b_pct_misfit: 5.2
761	    d_infit_mean: 0.98
762	    d_infit_range:
763	    - 0.82
764	    - 1.18
765	    d_pct_misfit: 0.0
766	    c_infit_mean: 1.02
767	    c_pct_misfit: 9.1
768	    lz_c_n_rank_corr: 0.72
769	    emri_c_n_rank_corr: 0.68
770	    pct_agreement_flagged: 78.3
771	  result_rationale: 'best 档下 MFRM 拟合良好：θ 和 d 的 infit/outfit 接近 1.0，misfit 率低。 b (items)
772	    的 misfit 略高（5.2%），因为部分 Arena-Hard items 的难度在 不同 judges 间变异大（某些 items 对某些 judges
773	    "特别难评"）。 c_n 的 misfit 率最高（9.1%=2/22 models），因为 rank-1 c_n·e_i 假设 对极端模型（极高或极低污染）拟合不完美——这正是论文中坦诚讨论
774	    rank-1 局限性的位置。 lz 和 c_n 的 rank correlation 0.72 表明传统 person-fit 指标确实能部分捕捉 contamination（因为
775	    contaminated models 在高曝光 items 上表现异常好）， 但 c_n 提供了更结构化的解释。两者 78.3% 的重叠验证了 construct
776	    coherence。
777	
778	    '
779	  tables:
780	  - name: 'Table S6: Facet Fit Statistics'
781	    columns:
782	    - Facet
783	    - N
784	    - Infit_MNSQ_mean
785	    - Infit_MNSQ_range
786	    - Outfit_MNSQ_mean
787	    - Pct_misfit
788	    rows:
789	    - - θ (ability)
790	      - 22
791	      - 1.01
792	      - 0.78–1.25
793	      - 1.03
794	      - 4.5
795	    - - b (difficulty)
796	      - 580
797	      - 1.0
798	      - 0.65–1.42
799	      - 1.02
800	      - 5.2
801	    - - d (severity)
802	      - 8
803	      - 0.98
804	      - 0.82–1.18
805	      - 0.99
806	      - 0.0
807	    - - c (contamination)
808	      - 22
809	      - 1.02
810	      - 0.74–1.38
811	      - 1.05
812	      - 9.1
813	  - name: 'Table S7: Person-Fit vs c_n Convergent Validity'
814	    columns:
815	    - Metric
816	    - Rank_corr_with_c_n
817	    - p_value
818	    - Pct_overlap_flagged
819	    rows:
820	    - - lz (person-fit)
821	      - 0.72
822	      - 0.0002
823	      - 78.3
824	    - - EMRi (extended)
825	      - 0.68
826	      - 0.0008
827	      - 73.9
828	  figures_description:
829	  - 'Figure S9: Infit/Outfit MNSQ distribution per facet (box plots), 红色虚线标注 0.7/1.3
830	    阈值'
831	  - 'Figure S10: lz vs c_n scatter, r=0.72, 展示 person-fit 与 contamination 的 convergent
832	    validity'
833	  analysis: '整体拟合质量支撑 framework claim：G-MFRM 不是 overfitting 噪声， 而是合理捕捉了数据结构。c_n 的
834	    9.1% misfit 率可在 Limitations 中坦诚报告， 并指向 rank-k extension 的 future work。person-fit/c_n
835	    的 convergent validity (r=0.72) 是 DG-IRT 迁移成功的额外证据。
836	
837	    '
838	- name: confounding_formal_proposition
839	  plan_id: exp-009
840	  description: '推导 sequential estimator 在 d_j/c_n·e_i 非正交条件下的一阶 bias 近似。 形式化为 Proposition
841	    1（Section 2）。Monte Carlo 验证 bias 近似精度。
842	
843	    '
844	  expected_results:
845	    proposition_statement: 'Under non-orthogonality (Cov(d_j, c_n·e_i) ≠ 0), the bias-first
846	      sequential estimator θ̂_seq has first-order bias E[θ̂_seq - θ] ≈ γ·Cov(d_j,
847	      c_n·e_i)/Var(d_j) where γ is the contamination gating coefficient. Direction:
848	      positive covariance → overestimation of high-contamination models.
849	
850	      '
851	    mc_n_simulations: 5000
852	    mc_parameter_grid_size: 50
853	    bias_approximation_r2: 0.94
854	    bias_direction_correct_pct: 97.8
855	    max_bias_at_rho_0_6: 0.31
856	    bias_at_rho_0_3: 0.14
857	    real_data_rho: 0.37
858	    real_data_predicted_bias: 0.17
859	    real_data_observed_bias: 0.19
860	    prediction_error_pct: 10.5
861	  result_rationale: '一阶 bias 近似基于 omitted variable bias 的经典结果（Angrist & Pischke 框架
862	    在 psychometric context 的适配）。R²=0.94 表明一阶近似在实际参数范围内精度高。 关键洞察：bias 方向由 Cov(d_j,
863	    c_n·e_i) 决定——当严格 judges（高 d_j） 与高污染模型×高曝光 items 的交互为正时，sequential 高估高污染模型。 真实数据
864	    ρ=0.37 > 0 预测正向 bias 0.17 std units，观测值 0.19 std units， 预测误差仅 10.5%——形式化命题在真实数据上得到量化验证。
865	    这为 Section 2 提供了理论 + 实证双重论证。
866	
867	    '
868	  tables:
869	  - name: 'Table S8: Monte Carlo Validation of Bias Approximation'
870	    columns:
871	    - rho_range
872	    - N_sims
873	    - Mean_true_bias
874	    - Mean_approx_bias
875	    - Approx_R2
876	    - Direction_accuracy_pct
877	    rows:
878	    - - '[-0.8, -0.4]'
879	      - 1000
880	      - -0.28
881	      - -0.26
882	      - 0.93
883	      - 98.2
884	    - - '[-0.4, 0.0]'
885	      - 1000
886	      - -0.09
887	      - -0.08
888	      - 0.95
889	      - 97.5
890	    - - '[0.0, 0.4]'
891	      - 1000
892	      - 0.1
893	      - 0.09
894	      - 0.94
895	      - 97.8
896	    - - '[0.4, 0.8]'
897	      - 1000
898	      - 0.32
899	      - 0.3
900	      - 0.93
901	      - 97.6
902	    - - Overall
903	      - 5000
904	      - —
905	      - —
906	      - 0.94
907	      - 97.8
908	  figures_description:
909	  - 'Figure 1 (Section 2): Left panel: sequential pipeline diagram with confounding
910	    annotation (red arrows showing omitted variable path); Right panel: G-MFRM joint
911	    estimation DAG with all paths modeled'
912	  - 'Figure S11: MC validation — true bias vs approximate bias scatter (5000 points),
913	    R²=0.94, 按 ρ 色彩编码'
914	  analysis: 'Proposition 1 将 confounding claim 从实证观察提升为理论结果， MC 验证确认近似在实际参数范围内高精度（R²=0.94）。
915	    real data 上 predicted vs observed bias 的一致性（10.5% error） 提供了 "theory predicts,
916	    data confirms" 的强叙事弧线。 Section 2 可以先展示 proposition，再用 exp-003 的 bias scatter 作为实证验证。
917	
918	    '
919	- name: wildbench_replication
920	  plan_id: exp-010
921	  description: '在 WildBench 上复制 G-MFRM pipeline：收集 8 judges × 22 models 评分， ConStat
922	    exposure estimation，三阶段拟合，baseline 比较。 验证跨 benchmark 泛化性。
923	
924	    '
925	  expected_results:
926	    wildbench_n_items: 1024
927	    kendall_tau_gmfrm_wildbench: 0.89
928	    kendall_tau_sequential_wildbench: 0.84
929	    kendall_tau_uda_wildbench: 0.85
930	    delta_tau_vs_best_baseline_wildbench: 0.04
931	    wilcoxon_p_gmfrm_vs_seq_wildbench: 0.00021
932	    c_n_mean_wildbench: 0.95
933	    c_n_rank_corr_cross_benchmark: 0.82
934	    convergence_max_rhat_wildbench: 1.02
935	    convergence_min_ess_wildbench: 278
936	  result_rationale: 'WildBench τ=0.89 略低于 MT-Bench+Arena-Hard 的 0.91， 因为 WildBench
937	    items 更 open-ended、scoring 更主观， 引入了 G-MFRM 无法完全捕捉的 noise。但仍显著优于全部 baselines（Δτ=0.04）。
938	    c_n_mean=0.95 略低于主数据集的 1.18，因为 WildBench 较新（2024）， 部分 items 未被充分泄漏。跨 benchmark
939	    c_n rank correlation 0.82 表明 contamination 是模型属性（不是 benchmark 属性）， 支撑 c_n 作为 meaningful
940	    latent trait 的解读。
941	
942	    '
943	  tables:
944	  - name: 'Table 5: Cross-Benchmark Replication (WildBench)'
945	    columns:
946	    - Method
947	    - WildBench_τ
948	    - MT-Bench_τ
949	    - Arena-Hard_τ
950	    rows:
951	    - - Raw Average
952	      - 0.8
953	      - 0.8
954	      - 0.83
955	    - - Sequential
956	      - 0.84
957	      - 0.84
958	      - 0.86
959	    - - UDA
960	      - 0.85
961	      - 0.85
962	      - 0.87
963	    - - '**G-MFRM**'
964	      - '**0.89**'
965	      - '**0.90**'
966	      - '**0.91**'
967	  figures_description:
968	  - 'Figure 6: Cross-benchmark c_n rank comparison scatter, MT-Bench+Arena-Hard c_n
969	    vs WildBench c_n, r=0.82'
970	  analysis: '跨 benchmark 泛化成功：G-MFRM 在第三个独立 benchmark 上同样显著优于全部 baselines。 c_n 跨 benchmark
971	    一致性（r=0.82）是论文的加分项—— 说明 contamination susceptibility 是模型的稳定属性，G-MFRM 估计的不是 benchmark-specific
972	    噪声。
973	
974	    '
975	- name: adversarial_robustness
976	  plan_id: exp-011
977	  description: '模拟 Wang et al. (ICLR 2026) 的 adversarial contamination 场景： 对 target
978	    model 注入 benchmark items（0%, 5%, 10%, 20% training data）， 测试 G-MFRM c_n 估计是否正确反映注入量，
979	    以及 θ 估计是否对 adversarial contamination 鲁棒。
980	
981	    '
982	  expected_results:
983	    c_n_at_0pct_injection: 0.15
984	    c_n_at_5pct_injection: 0.82
985	    c_n_at_10pct_injection: 1.45
986	    c_n_at_20pct_injection: 2.18
987	    c_n_injection_correlation: 0.97
988	    theta_bias_at_0pct: 0.02
989	    theta_bias_at_5pct: 0.05
990	    theta_bias_at_10pct: 0.08
991	    theta_bias_at_20pct: 0.14
992	    theta_bias_sequential_at_20pct: 0.52
993	    robustness_ratio_20pct: 3.71
994	    auc_detecting_contaminated: 0.94
995	  result_rationale: 'G-MFRM 的 gating mechanism 设计上就是为了 absorb contamination effect
996	    into c_n， 所以 c_n 与 injection rate 高度相关（r=0.97）是预期中的。 θ bias 在 20% injection 时仅
997	    0.14（vs sequential 的 0.52）， 因为 G-MFRM 将 contamination inflation 归因于 c_n 而非 θ。
998	    robustness ratio 3.71× 意味着 G-MFRM 的 θ 偏差仅为 sequential 的 27%。 AUC=0.94 表明 c_n 可以作为
999	    contamination detection 工具， 这为论文的 practical impact 增加了一个维度。 注意：这是在 controlled
1000	    setting（已知注入量）的 validation， 与真实场景的 unknown contamination 有区别，需在论文中说明。
1001	
1002	    '
1003	  tables:
1004	  - name: 'Table S9: Adversarial Robustness — θ Bias Under Controlled Contamination'
1005	    columns:
1006	    - Injection_pct
1007	    - G-MFRM_c_n
1008	    - G-MFRM_θ_bias
1009	    - Sequential_θ_bias
1010	    - Robustness_ratio
1011	    rows:
1012	    - - 0
1013	      - 0.15
1014	      - 0.02
1015	      - 0.03
1016	      - 1.5
1017	    - - 5
1018	      - 0.82
1019	      - 0.05
1020	      - 0.18
1021	      - 3.6
1022	    - - 10
1023	      - 1.45
1024	      - 0.08
1025	      - 0.34
1026	      - 4.25
1027	    - - 20
1028	      - 2.18
1029	      - 0.14
1030	      - 0.52
1031	      - 3.71
1032	  figures_description:
1033	  - 'Figure S12: Left: c_n vs injection rate (near-linear, r=0.97); Right: θ bias
1034	    vs injection rate for G-MFRM (blue, flat) vs Sequential (red, steep)'
1035	  analysis: Adversarial robustness 是 reviewer concern 的预防性回应。 G-MFRM 在极端场景（20% injection）下
1036	    θ bias 仅为 sequential 的 1/4， 且 c_n 可作为 post-hoc contamination audit 工具（AUC=0.94）。
1037	    这将 G-MFRM 从 "evaluation correction method" 提升为 "contamination-aware evaluation
1038	    framework"。
1039	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef415cb8-c6b2-479e-a007-3c9b1303482a",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "96fc851b-2a66-418d-ad5d-9ab9f6bf823d",
  "sourceToolAssistantUUID": "ef415cb8-c6b2-479e-a007-3c9b1303482a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-21T21:31:32.702Z_

Now let me also read the worst-case scenario paper and the MVP experiment code to understand the actual implementation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96fc851b-2a66-418d-ad5d-9ab9f6bf823d",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRmmN4Hh1QPdgeXccvP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "92003f44-5af1-46fc-925b-875dff9952a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zfbXRX6MFAHF9jNH4xt4H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28891,
      "cache_read_input_tokens": 42934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28891,
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

_source line 38 · 2026-05-21T21:31:38.920Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Une87dsin5GyxBRuNotJDV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/worst/paper.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92003f44-5af1-46fc-925b-875dff9952a4",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRmmN4Hh1QPdgeXccvP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5700b031-f28d-4dfc-bed6-d243486876e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zfbXRX6MFAHF9jNH4xt4H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28891,
      "cache_read_input_tokens": 42934,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 28891
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 42934,
          "cache_creation_input_tokens": 28891,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 28891,
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

### Tool call

_source line 39 · 2026-05-21T21:31:38.924Z_

<details open><summary>🔧 Tool call — Read · `toolu_017zH3dRCq6MNAcwh5VcBTZv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/mvp/models.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5700b031-f28d-4dfc-bed6-d243486876e2",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRmmN4Hh1QPdgeXccvP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a5983b0f-d276-43f7-b259-bd9484cb73ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zfbXRX6MFAHF9jNH4xt4H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28891,
      "cache_read_input_tokens": 42934,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 28891
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 42934,
          "cache_creation_input_tokens": 28891,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 28891,
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

_source line 40 · 2026-05-21T21:31:38.930Z_

<details><summary>↩ Tool result · `toolu_017zH3dRCq6MNAcwh5VcBTZv`</summary>

```text
1	"""Fitting methods for the G-MFRM synthetic recovery experiment.
2	
3	Four methods of increasing sophistication:
4	  1. Raw average — naive mean of responses.
5	  2. MFRM-only — standard 3-facet Rasch via NumPyro MCMC.
6	  3. Sequential — MFRM then OLS residual regression on exposure.
7	  4. Joint G-MFRM — full model with contamination term, NumPyro MCMC.
8	
9	Dependencies: numpy, jax, numpyro, arviz, scipy
10	"""
11	
12	import warnings
13	
14	import arviz as az
15	import jax
16	import jax.numpy as jnp
17	import numpy as np
18	import numpyro
19	import numpyro.distributions as dist
20	from numpyro.infer import MCMC, NUTS
21	from scipy.special import expit
22	
23	numpyro.set_host_device_count(2)
24	
25	
26	# ---------------------------------------------------------------------------
27	# Helpers
28	# ---------------------------------------------------------------------------
29	
30	def _mcmc_diagnostics(mcmc: MCMC) -> tuple[float, float]:
31	    """Return (max R-hat, min ESS) across all parameters."""
32	    summary = az.summary(az.from_numpyro(mcmc))
33	    max_rhat = summary["r_hat"].max()
34	    min_ess = summary["ess_bulk"].min()
35	    return float(max_rhat), float(min_ess)
36	
37	
38	# ---------------------------------------------------------------------------
39	# Method 1: Raw average
40	# ---------------------------------------------------------------------------
41	
42	def fit_raw_average(data: dict) -> dict:
43	    """Estimate theta as mean response rate per model.
44	
45	    Args:
46	        data: Output of generate_gated_mfrm_data().
47	
48	    Returns:
49	        Dict with theta_hat (N,), r_hat=NaN, ess=NaN.
50	    """
51	    Y = data["responses"].astype(np.float64)
52	    theta_hat = Y.mean(axis=(1, 2))
53	    # Center to match identification constraint of MCMC methods
54	    theta_hat = theta_hat - theta_hat.mean()
55	    return {"theta_hat": theta_hat, "r_hat": float("nan"), "ess": float("nan")}
56	
57	
58	# ---------------------------------------------------------------------------
59	# Method 2: Standard MFRM (no contamination term)
60	# ---------------------------------------------------------------------------
61	
62	def _mfrm_model(Y: jnp.ndarray, N: int, I: int, J: int) -> None:
63	    theta_raw = numpyro.sample("theta_raw", dist.Normal(0, 1).expand([N]))
64	    theta = numpyro.deterministic("theta", theta_raw - theta_raw.mean())
65	    b = numpyro.sample("b", dist.Normal(0, 1).expand([I]))
66	    d = numpyro.sample("d", dist.Normal(0, 0.5).expand([J]))
67	
68	    logits = theta[:, None, None] - b[None, :, None] - d[None, None, :]
69	    numpyro.sample("obs", dist.Bernoulli(logits=logits), obs=Y)
70	
71	
72	def fit_mfrm_only(data: dict) -> dict:
73	    """Fit standard 3-facet MFRM via NUTS.
74	
75	    Args:
76	        data: Output of generate_gated_mfrm_data().
77	
78	    Returns:
79	        Dict with theta_hat (N,), r_hat (float), ess (float).
80	    """
81	    cfg = data["config"]
82	    Y = jnp.array(data["responses"], dtype=jnp.float32)
83	
84	    kernel = NUTS(_mfrm_model)
85	    mcmc = MCMC(kernel, num_warmup=1000, num_samples=2000, num_chains=2, progress_bar=False)
86	    mcmc.run(jax.random.PRNGKey(cfg["seed"]), Y=Y, N=cfg["N"], I=cfg["I"], J=cfg["J"])
87	
88	    samples = mcmc.get_samples()
89	    theta_hat = np.array(samples["theta"].mean(axis=0))
90	    max_rhat, min_ess = _mcmc_diagnostics(mcmc)
91	
92	    return {"theta_hat": theta_hat, "r_hat": max_rhat, "ess": min_ess}
93	
94	
95	# ---------------------------------------------------------------------------
96	# Method 3: Sequential (MFRM then OLS residual correction)
97	# ---------------------------------------------------------------------------
98	
99	def fit_sequential(data: dict, e_values: np.ndarray) -> dict:
100	    """Two-step approach: fit MFRM, then regress residuals on exposure.
101	
102	    Args:
103	        data: Output of generate_gated_mfrm_data().
104	        e_values: True item exposure values, shape (I,).
105	
106	    Returns:
107	        Dict with theta_hat (N,), r_hat (float), ess (float).
108	    """
109	    cfg = data["config"]
110	    N, I, J = cfg["N"], cfg["I"], cfg["J"]
111	    Y = data["responses"].astype(np.float64)
112	
113	    # Step A: single MFRM MCMC — extract theta, b, d from one run
114	    Y_jnp = jnp.array(data["responses"], dtype=jnp.float32)
115	    kernel = NUTS(_mfrm_model)
116	    mcmc = MCMC(kernel, num_warmup=1000, num_samples=2000, num_chains=2, progress_bar=False)
117	    mcmc.run(jax.random.PRNGKey(cfg["seed"]), Y=Y_jnp, N=N, I=I, J=J)
118	    samples = mcmc.get_samples()
119	    theta_mfrm = np.array(samples["theta"].mean(axis=0))
120	    b_hat = np.array(samples["b"].mean(axis=0))
121	    d_hat = np.array(samples["d"].mean(axis=0))
122	    max_rhat, min_ess = _mcmc_diagnostics(mcmc)
123	
124	    # Step B: residuals
125	    logits_hat = theta_mfrm[:, None, None] - b_hat[None, :, None] - d_hat[None, None, :]
126	    pred = expit(logits_hat)
127	    residuals = Y - pred  # (N, I, J)
128	    r_ni = residuals.mean(axis=2)  # (N, I) — average over judges
129	
130	    # Step C: OLS per model — regress r_ni on e_i to get c_hat_n
131	    c_hat = np.zeros(N)
132	    e_centered = e_values - e_values.mean()
133	    e_var = (e_centered**2).sum()
134	    if e_var > 1e-10:
135	        for n in range(N):
136	            c_hat[n] = (r_ni[n] * e_centered).sum() / e_var
137	
138	    # Step D: adjust theta
139	    mean_e = e_values.mean()
140	    theta_seq = theta_mfrm - c_hat * mean_e
141	    theta_seq = theta_seq - theta_seq.mean()
142	
143	    return {
144	        "theta_hat": theta_seq,
145	        "r_hat": max_rhat,
146	        "ess": min_ess,
147	    }
148	
149	
150	# ---------------------------------------------------------------------------
151	# Method 4: Joint G-MFRM
152	# ---------------------------------------------------------------------------
153	
154	def _gmfrm_model(Y: jnp.ndarray, e: jnp.ndarray, N: int, I: int, J: int) -> None:
155	    theta_raw = numpyro.sample("theta_raw", dist.Normal(0, 1).expand([N]))
156	    theta = numpyro.deterministic("theta", theta_raw - theta_raw.mean())
157	    b = numpyro.sample("b", dist.Normal(0, 1).expand([I]))
158	    d = numpyro.sample("d", dist.Normal(0, 0.5).expand([J]))
159	    c = numpyro.sample("c", dist.HalfNormal(0.5).expand([N]))
160	
161	    logits = (
162	        theta[:, None, None]
163	        - b[None, :, None]
164	        - d[None, None, :]
165	        + c[:, None, None] * e[None, :, None]
166	    )
167	    numpyro.sample("obs", dist.Bernoulli(logits=logits), obs=Y)
168	
169	
170	def fit_joint_gmfrm(data: dict, e_values: np.ndarray) -> dict:
171	    """Fit full G-MFRM with contamination term via NUTS.
172	
173	    Args:
174	        data: Output of generate_gated_mfrm_data().
175	        e_values: True item exposure values, shape (I,).
176	
177	    Returns:
178	        Dict with theta_hat (N,), c_hat (N,), r_hat (float), ess (float).
179	    """
180	    cfg = data["config"]
181	    Y = jnp.array(data["responses"], dtype=jnp.float32)
182	    e = jnp.array(e_values, dtype=jnp.float32)
183	
184	    kernel = NUTS(_gmfrm_model)
185	    mcmc = MCMC(kernel, num_warmup=1000, num_samples=2000, num_chains=2, progress_bar=False)
186	    mcmc.run(jax.random.PRNGKey(cfg["seed"]), Y=Y, e=e, N=cfg["N"], I=cfg["I"], J=cfg["J"])
187	
188	    samples = mcmc.get_samples()
189	    theta_hat = np.array(samples["theta"].mean(axis=0))
190	    c_hat = np.array(samples["c"].mean(axis=0))
191	    max_rhat, min_ess = _mcmc_diagnostics(mcmc)
192	
193	    return {"theta_hat": theta_hat, "c_hat": c_hat, "r_hat": max_rhat, "ess": min_ess}
194	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5983b0f-d276-43f7-b259-bd9484cb73ad",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "1b198b6c-c9ca-4115-8007-415e05290cbc",
  "sourceToolAssistantUUID": "a5983b0f-d276-43f7-b259-bd9484cb73ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-21T21:31:39.183Z_

<details><summary>↩ Tool result · `toolu_01Une87dsin5GyxBRuNotJDV`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata}
9	\usepackage{graphicx}
10	\usepackage{amsmath,amssymb,amsthm}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{url}
15	
16	\newtheorem{proposition}{Proposition}
17	
18	\title{G-MFRM: A Diagnostic Framework for Joint Detection of Judge Bias\\and Benchmark Contamination in LLM Evaluation}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\begin{abstract}
26	LLM-as-a-judge evaluation faces two entangled threats: inter-judge severity bias and benchmark contamination.
27	Existing methods address these independently---bias correction ignores contamination, and contamination detection ignores judge variation---raising the concern that unmodeled effects confound ability estimates when both are present.
28	We formalize this confounding as an omitted variable bias problem and derive a closed-form first-order bias expression for sequential estimators.
29	We then propose the Gated Many-Facet Rasch Model (G-MFRM), a psychometric framework that jointly estimates model ability, item difficulty, judge severity, and contamination susceptibility via a three-stage procedure with external exposure anchoring.
30	Monte Carlo simulations across 120 parameter settings confirm that the theoretical bias predictions are accurate (direction correct 97.2\%, magnitude relative error 8\%) and that confounding becomes practically significant when contamination strength $\bar{c} > 0.6$ and correlation $\rho > 0.15$.
31	On real evaluation data (8 LLM judges $\times$ 22 target models across MT-Bench, Arena-Hard, and WildBench; ${\sim}$186K evaluations), we find that current contamination levels are low ($\bar{c}_n = 0.14$, 78\% of posterior intervals covering zero), and G-MFRM gracefully degrades to standard MFRM without performance loss ($\tau = 0.851$ vs.\ $0.843$, $p = 0.31$).
32	Under controlled adversarial contamination injection, G-MFRM recovers its full correction advantage ($\tau = 0.871$ vs.\ $0.831$, $p = 0.008$), demonstrating monitoring readiness.
33	Our framework provides both a current diagnostic---contamination in major benchmarks is presently mitigated---and a ready-made monitoring tool for future contamination threats.
34	\end{abstract}
35	
36	%---------------------------------------------------------------------
37	\section{Introduction}
38	\label{sec:intro}
39	
40	The widespread adoption of LLM-as-a-judge protocols for evaluating language models \cite{zheng2024judging} has exposed a fundamental tension in evaluation methodology. On one hand, LLM judges exhibit systematic severity biases: different judges produce substantially different scores for the same model-output pair, with inter-judge agreement as low as Fleiss' $\kappa = 0.38$ in multi-judge settings. On the other hand, benchmark contamination---where target models have been exposed to evaluation items during training---can inflate performance estimates in ways that are difficult to distinguish from genuine capability gains.
41	
42	These two problems have been studied largely in isolation. Judge bias correction methods such as CyclicJudge \cite{bai2024cyclicjudge} and UDA \cite{kwon2024uda} focus on harmonizing ratings across judges without considering contamination. Contamination detection tools such as ConStat \cite{dekoninck2024constat} and DCR \cite{xu2024dcr} quantify exposure effects but ignore judge variation. A natural question arises: \emph{can these corrections be composed sequentially, or does their interaction introduce systematic bias?}
43	
44	We formalize this question as an omitted variable bias problem. When judge severity $d_j$ and the contamination term $c_n \cdot e_i$ are non-orthogonal, sequential estimation---correcting one facet then the other---produces asymptotically biased ability estimates. The bias direction depends on the covariance structure, and the magnitude scales with the contamination strength (Proposition~\ref{prop:bias}).
45	
46	To address this, we propose the \textbf{Gated Many-Facet Rasch Model (G-MFRM)}, which integrates MFRM's multi-facet calibration with DG-IRT's gating mechanism \cite{sato2024dg-irt} and externally anchored exposure indicators. G-MFRM estimates model ability ($\theta_n$), item difficulty ($b_i$), judge severity ($d_j$), and contamination susceptibility ($c_n$) in a single joint calibration via a three-stage procedure.
47	
48	Our theoretical analysis, validated through Monte Carlo simulation across 120 parameter settings, establishes precise conditions under which confounding becomes practically significant: $\bar{c} > 0.6$ and $\rho > 0.15$ are needed for $>$5\% $\theta$-RMSE degradation. This leads to a diagnostic framework with two operating modes:
49	
50	\begin{itemize}
51	    \item \textbf{Detection mode}: When contamination is weak ($\bar{c} < 0.4$), G-MFRM degrades gracefully to standard MFRM, producing reliable bias-corrected ability estimates while diagnosing that contamination-induced confounding is negligible.
52	    \item \textbf{Correction mode}: When contamination is strong ($\bar{c} > 0.6$), the gating mechanism activates, and G-MFRM's joint estimation provides significant improvement over sequential approaches.
53	\end{itemize}
54	
55	We validate both modes empirically. On real data from three benchmarks (MT-Bench, Arena-Hard, WildBench) with 8 LLM judges and 22 target models (${\sim}$186K total evaluations), G-MFRM operates in detection mode: contamination levels are low ($\bar{c}_n = 0.14$), the framework produces the diagnostic conclusion that current contamination is mitigated, and performance matches MFRM ($\tau = 0.851$ vs.\ $0.843$, $p = 0.31$). Under adversarial contamination injection, G-MFRM switches to correction mode and achieves significant gains ($\tau = 0.871$ vs.\ $0.831$, $p = 0.008$).
56	
57	Our contributions are:
58	\begin{enumerate}
59	    \item A formal proposition characterizing the first-order confounding bias between judge severity and contamination in sequential estimators, with Monte Carlo validation (Section~\ref{sec:confounding}).
60	    \item The G-MFRM framework for joint estimation and diagnosis of judge bias and contamination (Section~\ref{sec:method}).
61	    \item An empirical diagnostic establishing that benchmark contamination in current major benchmarks is at mitigated levels ($\bar{c}_n = 0.14$), with the framework ready for future monitoring (Sections~\ref{sec:experiments}--\ref{sec:adversarial}).
62	\end{enumerate}
63	
64	%---------------------------------------------------------------------
65	\section{Confounding in Sequential Estimation}
66	\label{sec:confounding}
67	
68	Consider a response $X_{nij}$ from model $n$ to item $i$ scored by judge $j$. The full generative model includes model ability $\theta_n$, item difficulty $b_i$, judge severity $d_j$, and a contamination effect $c_n \cdot e_i$, where $c_n$ is model $n$'s contamination susceptibility and $e_i$ is item $i$'s exposure level:
69	\begin{equation}
70	    X_{nij} = \theta_n - b_i - d_j + c_n \cdot e_i + \varepsilon_{nij}.
71	    \label{eq:full}
72	\end{equation}
73	
74	A \emph{sequential} procedure first estimates $\hat{\theta}_n^{(1)}, \hat{b}_i^{(1)}, \hat{d}_j^{(1)}$ from an MFRM ignoring contamination, then adjusts for contamination using $\hat{\theta}_n^{(1)}$. We show this produces biased ability estimates when $d_j$ and $c_n \cdot e_i$ are non-orthogonal.
75	
76	\begin{proposition}[First-order confounding bias]
77	\label{prop:bias}
78	Let $\rho = \text{corr}(\mathbf{d}, \mathbf{c} \odot \mathbf{e})$ be the empirical correlation between judge severity effects and contamination effects across the observed response matrix. The first-order bias in the sequential ability estimator is:
79	\begin{equation}
80	    \text{Bias}(\hat{\theta}_n^{\text{seq}}) \approx \rho \cdot \sigma_d \cdot \bar{c} \cdot \bar{e} \cdot f(N, J, I),
81	    \label{eq:bias}
82	\end{equation}
83	where $\sigma_d$ is the standard deviation of judge severities, $\bar{c}$ is the mean contamination susceptibility, $\bar{e}$ is the mean exposure, and $f(N, J, I)$ is a design-dependent scaling factor.
84	\end{proposition}
85	
86	\paragraph{Monte Carlo Validation.}
87	We validate Proposition~\ref{prop:bias} through simulation across 120 parameter configurations spanning $\bar{c} \in \{0.2, 0.5, 1.0, 1.5\}$, $\rho \in \{0.3, 0.6\}$, and varying $N$, $J$, $I$. Table~\ref{tab:confounding_mc} summarizes results at representative settings.
88	
89	\begin{table}[t]
90	\centering
91	\small
92	\begin{tabular}{lcccc}
93	\toprule
94	$\bar{c}$ & $\rho$ & Bias$_{\text{theory}}$ & Bias$_{\text{MC}}$ & $\theta$-RMSE $\downarrow$\% \\
95	\midrule
96	0.2 & 0.3 & 0.003 & 0.004$_{\pm.002}$ & 0.8 \\
97	0.2 & 0.6 & 0.007 & 0.008$_{\pm.003}$ & 1.9 \\
98	0.5 & 0.3 & 0.019 & 0.021$_{\pm.006}$ & 5.2 \\
99	0.5 & 0.6 & 0.041 & 0.044$_{\pm.009}$ & 12.7 \\
100	1.0 & 0.3 & 0.078 & 0.082$_{\pm.015}$ & 24.1 \\
101	1.0 & 0.6 & 0.163 & 0.171$_{\pm.028}$ & 43.5 \\
102	1.5 & 0.6 & 0.245 & 0.258$_{\pm.041}$ & 67.2 \\
103	\bottomrule
104	\end{tabular}
105	\caption{Confounding bias: theoretical prediction vs.\ Monte Carlo simulation. Bias direction is correctly predicted in 97.2\% of 120 settings (type I error rate: 0.048). $\theta$-RMSE degradation becomes practically significant ($>$5\%) at $\bar{c} \geq 0.5, \rho \geq 0.3$.}
106	\label{tab:confounding_mc}
107	\end{table}
108	
109	The theoretical approximation accurately tracks the Monte Carlo results: bias direction is correctly predicted 97.2\% of the time, with a mean magnitude relative error of 8\%. The critical finding is that confounding becomes negligible when $\bar{c} < 0.4$---precisely the regime we observe in real evaluation data (Section~\ref{sec:calibration}). This does not invalidate the confounding concern but rather \emph{conditions} it: G-MFRM serves as both a diagnostic tool (measuring where the current data falls in this landscape) and a correction mechanism (activating when contamination rises above the critical threshold).
110	
111	%---------------------------------------------------------------------
112	\section{Method: Gated Many-Facet Rasch Model}
113	\label{sec:method}
114	
115	G-MFRM proceeds in three stages, each building on the previous.
116	
117	\subsection{Stage 1: MFRM Calibration}
118	
119	Standard MFRM models the probability of response level $k$ for model $n$ on item $i$ by judge $j$:
120	\begin{equation}
121	    \ln\frac{P(X_{nij} \geq k)}{P(X_{nij} < k)} = \theta_n - b_i - d_j - \tau_k,
122	    \label{eq:mfrm}
123	\end{equation}
124	where $\tau_k$ are rating scale thresholds. We estimate $\{\hat{\theta}_n, \hat{b}_i, \hat{d}_j, \hat{\tau}_k\}$ via MCMC. This provides well-calibrated ability and severity estimates when contamination is negligible.
125	
126	\subsection{Stage 2: External Exposure Anchoring}
127	
128	Since item exposure status is unknown to the evaluation administrator, we anchor exposure indicators $e_i$ using three external signals:
129	
130	\begin{itemize}
131	    \item \textbf{ConStat delta}: Performance difference between original and rephrased variants ($\Delta_i$), with 3 reference variants per item and 89\% human equivalence pass rate.
132	    \item \textbf{Temporal signal}: Score changes across model release cohorts that correlate with potential training data exposure.
133	    \item \textbf{LogProber}: Per-item memorization indicators from output log-probability analysis.
134	\end{itemize}
135	
136	The composite exposure indicator is: $e_i = w_1 \cdot \Delta_i^{\text{CS}} + w_2 \cdot \Delta_i^{\text{temp}} + w_3 \cdot \Delta_i^{\text{LP}}$, with weights determined via cross-validation.
137	
138	\subsection{Stage 3: Joint Gated Model}
139	
140	The full G-MFRM introduces contamination susceptibility $c_n$ with a gating mechanism:
141	\begin{equation}
142	    \ln\frac{P(X_{nij} \geq k)}{P(X_{nij} < k)} = \theta_n - b_i - d_j + g(e_i) \cdot c_n \cdot e_i - \tau_k,
143	    \label{eq:gmfrm}
144	\end{equation}
145	where $g(e_i) = \sigma(\alpha(e_i - e_0))$ is a sigmoid gate that activates the contamination term only when the exposure indicator exceeds a learned threshold $e_0$. This gating ensures that the contamination channel is effectively closed for low-exposure items, preventing noise injection.
146	
147	The prior on $c_n$ is weakly informative: $c_n \sim \text{Half-Normal}(0, \sigma_c^2)$, allowing the data to determine contamination levels. When exposure is uniformly low, the posterior on $c_n$ concentrates near zero and the model reduces to standard MFRM---a designed graceful degradation.
148	
149	Stage 3 is initialized from Stage 1 estimates, with $c_n$ initialized at the prior mean. MCMC sampling proceeds for all parameters jointly.
150	
151	%---------------------------------------------------------------------
152	\section{Experimental Setup}
153	\label{sec:setup}
154	
155	\paragraph{Data Collection.}
156	We collect multi-judge evaluation data across three benchmarks using 8 LLM judges and 22 target models, with position-swapped evaluations. Table~\ref{tab:data} summarizes the dataset.
157	
158	\begin{table}[t]
159	\centering
160	\small
161	\begin{tabular}{lrrrrr}
162	\toprule
163	Benchmark & Items & Judges & Models & Evals & Miss\% \\
164	\midrule
165	MT-Bench & 80 & 8 & 22 & 28,160 & 0.8 \\
166	Arena-Hard & 500 & 8 & 22 & 176,000 & 1.3 \\
167	\midrule
168	Total & 580 & 8 & 22 & $\sim$186K & 1.2 \\
169	\bottomrule
170	\end{tabular}
171	\caption{Data collection summary. Position swap disagreement: 14.5\%. Inter-judge Fleiss' $\kappa$: 0.38. API cost: \$870; GPU hours: 118.}
172	\label{tab:data}
173	\end{table}
174	
175	\paragraph{External Evaluation Ground Truth.}
176	We use Chatbot Arena human vote rankings as ground truth for ranking agreement, measured via Kendall's $\tau$ correlation.
177	
178	\paragraph{Baselines.}
179	We compare G-MFRM against 7 methods: (1) \textbf{Raw Average}---simple multi-judge mean; (2) \textbf{MFRM-only}---Stage 1 without contamination modeling; (3) \textbf{Sequential}---bias correction then contamination adjustment; (4) \textbf{CyclicJudge}---round-robin judge elimination; (5) \textbf{DCR Factor}---contamination-only adjustment; (6) \textbf{UDA}---neural K-factor judge calibration; (7) \textbf{Pref Leakage}---preference leakage detection and adjustment.
180	
181	%---------------------------------------------------------------------
182	\section{Experiments and Results}
183	\label{sec:experiments}
184	
185	\subsection{Exposure Estimation}
186	\label{sec:exposure}
187	
188	Table~\ref{tab:exposure} shows the distribution of exposure indicators. The composite $e_i$ has a mean of 0.07 with high right skewness (2.1): the vast majority of items show near-zero exposure signals, with only $\sim$11\% reaching statistical significance. The rank correlation between ConStat and temporal signals is modest ($r = 0.31$), indicating that different indicators capture different noise dimensions rather than consistent contamination signals.
189	
190	\begin{table}[t]
191	\centering
192	\small
193	\begin{tabular}{lcccc}
194	\toprule
195	Indicator & Mean & Std & Median & Sig\% \\
196	\midrule
197	ConStat $\Delta$ & 0.08 & 0.12 & 0.04 & 12.0 \\
198	Temporal & 0.05 & 0.09 & 0.02 & 8.5 \\
199	Composite $e_i$ & 0.07 & 0.10 & 0.03 & 11.0 \\
200	\bottomrule
201	\end{tabular}
202	\caption{Exposure indicator statistics across 580 items. Right-skewed distribution (skewness = 2.1): most items show negligible exposure.}
203	\label{tab:exposure}
204	\end{table}
205	
206	\subsection{G-MFRM Model Fit}
207	\label{sec:fit}
208	
209	Table~\ref{tab:gmfrm_fit} compares Stage 1 (MFRM) and Stage 3 (joint G-MFRM) model fits.
210	
211	\begin{table}[t]
212	\centering
213	\small
214	\begin{tabular}{lccccc}
215	\toprule
216	Stage & Model & $\hat{R}$ & ESS & $\tau_{\text{Arena}}$ & Params \\
217	\midrule
218	1 & MFRM & 1.01 & 820 & 0.843 & 110 \\
219	3 & G-MFRM & 1.06 & 112 & 0.851 & 132 \\
220	\bottomrule
221	\end{tabular}
222	\caption{G-MFRM fit summary. Stage 1 converges well. Stage 3 shows degraded MCMC mixing ($\hat{R} = 1.06$, ESS $= 112$) due to weak contamination signal---$c_n$ posteriors are prior-dominated.}
223	\label{tab:gmfrm_fit}
224	\end{table}
225	
226	The $c_n$ posterior mean is 0.14 (std 0.11), with 78\% of models' 95\% credible intervals covering zero. The prior-posterior KL divergence is only 0.08, confirming that the data provide negligible information about contamination beyond the prior. The $\Delta\tau$ between Stage 3 and Stage 1 is 0.008 (Wilcoxon $p = 0.34$): the contamination channel does not contribute to ranking accuracy on this data.
227	
228	\begin{table}[t]
229	\centering
230	\small
231	\begin{tabular}{lcccc}
232	\toprule
233	Model & $\hat{c}_n$ & Std & 95\% CI & $\ni 0$? \\
234	\midrule
235	model\_A & 0.38 & 0.15 & [0.09, 0.67] & No \\
236	model\_B & 0.31 & 0.17 & [$-$0.02, 0.64] & Yes \\
237	model\_C & 0.27 & 0.14 & [0.00, 0.54] & Yes \\
238	\multicolumn{5}{l}{\emph{Remaining 19 models}: $\hat{c}_n \in [0.02, 0.22]$, mostly cover 0} \\
239	\bottomrule
240	\end{tabular}
241	\caption{$c_n$ posterior summary for the top 3 models by estimated contamination. Only 1 of 22 models has a 95\% CI excluding zero.}
242	\label{tab:cn_posterior}
243	\end{table}
244	
245	\subsection{Main Results}
246	\label{sec:main_results}
247	
248	Table~\ref{tab:main} presents the main ranking agreement results.
249	
250	\begin{table}[t]
251	\centering
252	\small
253	\begin{tabular}{lccccr}
254	\toprule
255	Method & MT$\tau$ & AH$\tau$ & Avg$\tau$ & $\rho$ & $p$ \\
256	\midrule
257	Raw Average & .801 & .823 & .812 & .847 & .003 \\
258	DCR Factor & .810 & .828 & .819 & .853 & .008 \\
259	Pref Leakage & .815 & .833 & .824 & .858 & .012 \\
260	CyclicJudge & .831 & .845 & .838 & .866 & .14 \\
261	UDA & .834 & .848 & .841 & .869 & .22 \\
262	MFRM-only & .836 & .850 & .843 & .871 & .31 \\
263	Sequential & .839 & .851 & .845 & .873 & .28 \\
264	\textbf{G-MFRM} & \textbf{.845} & \textbf{.857} & \textbf{.851} & \textbf{.878} & --- \\
265	\bottomrule
266	\end{tabular}
267	\caption{Kendall $\tau$ and Spearman $\rho$ with Chatbot Arena rankings. $p$: Wilcoxon test vs.\ G-MFRM. G-MFRM is nominally highest but not significantly better than MFRM-only or Sequential ($p > 0.28$). Bootstrap 95\% CI for $\Delta\tau$ (G-MFRM $-$ Sequential): [$-$0.008, 0.021].}
268	\label{tab:main}
269	\end{table}
270	
271	The results reveal a clear two-tier structure. Methods that model judge severity (MFRM-only, Sequential, UDA, G-MFRM) cluster at $\tau \in [0.841, 0.851]$, significantly outperforming methods that do not (Raw Average, DCR, Pref Leakage; $\tau \in [0.812, 0.824]$, $p < 0.012$). Within the severity-aware tier, the contamination correction component provides no significant additional benefit: G-MFRM vs.\ MFRM-only has $\Delta\tau = 0.008$ ($p = 0.31$), and the bootstrap 95\% CI spans zero.
272	
273	This is the expected behavior of a diagnostic framework under low contamination: the gating mechanism keeps the contamination channel effectively closed, G-MFRM degrades to MFRM, and the diagnostic output is that contamination-induced confounding is currently negligible.
274	
275	\subsection{Contamination Magnitude Calibration}
276	\label{sec:calibration}
277	
278	Table~\ref{tab:calibration} places the real-data contamination estimates in the context of synthetic scenarios.
279	
280	\begin{table}[t]
281	\centering
282	\small
283	\begin{tabular}{lccccc}
284	\toprule
285	Scenario & $\bar{c}$ & $\sigma_c$ & RMSE$\downarrow$\% & $r_{\text{bias}}$ & $p$ \\
286	\midrule
287	Real data & 0.14 & 0.11 & 2.1 & 0.11 & 0.34 \\
288	Synth.\ weak & 0.50 & 0.25 & --- & 0.05 & 0.48 \\
289	Synth.\ strong & 1.50 & 0.50 & 43.8 & 0.65 & 1e-6 \\
290	\bottomrule
291	\end{tabular}
292	\caption{Contamination magnitude calibration. Real data ($\bar{c} = 0.14$) falls far below the synthetic weak scenario ($\bar{c} = 0.50$). $\theta$-RMSE degradation from confounding is only 2.1\% (vs.\ 43.8\% in the strong synthetic scenario). Sequential bias scatter $r = 0.11$, indicating near-zero systematic bias.}
293	\label{tab:calibration}
294	\end{table}
295	
296	Real contamination levels ($\bar{c} = 0.14$) are approximately 3.5$\times$ lower than even the weak synthetic scenario. Only 2 of 22 models have $c_n > 0.3$, and none reach 0.5. The $\theta$-RMSE degradation from confounding is 2.1\%---well within noise. The sequential bias scatter correlation ($r = 0.11$) indicates that judge severity and contamination effects are empirically near-orthogonal, consistent with the theoretical prediction that confounding is negligible at this contamination magnitude.
297	
298	\subsection{Facet Fit Diagnostics}
299	\label{sec:diagnostics}
300	
301	Table~\ref{tab:fit_diag} reports measurement quality across facets.
302	
303	\begin{table}[t]
304	\centering
305	\small
306	\begin{tabular}{lrcccc}
307	\toprule
308	Facet & $n$ & Infit & Range & Misfit & \% \\
309	\midrule
310	$\theta$ (ability) & 22 & 1.02 & 0.78--1.31 & 1 & 4.5 \\
311	$b$ (difficulty) & 580 & 1.00 & 0.72--1.45 & 28 & 4.8 \\
312	$d$ (severity) & 8 & 0.98 & 0.85--1.12 & 0 & 0.0 \\
313	$c$ (contamination) & 22 & 1.05 & 0.60--1.82 & 5 & 22.7 \\
314	\bottomrule
315	\end{tabular}
316	\caption{Facet fit summary (infit MNSQ). Judge severity ($d$) has excellent fit (0 misfit, narrow range). Contamination ($c$) shows high misfit rate (22.7\%) and wide infit range, consistent with $c_n$ being prior-dominated rather than data-driven.}
317	\label{tab:fit_diag}
318	\end{table}
319	
320	Judge severity achieves the best fit among all facets: zero misfit elements and the narrowest infit range (0.85--1.12). This validates that $d_j$ captures a psychometrically reliable construct. In contrast, $c_n$ has the highest misfit rate (22.7\%) and widest infit range, reflecting inadequate data information for this facet. The correlation between Stage 1 person-fit statistics ($l_z$, EMRi) and Stage 3 $c_n$ estimates is negligible ($r = 0.18$, $0.12$), indicating that Stage 1 misfit signals do not correspond to contamination.
321	
322	\subsection{Judge Count Sensitivity}
323	\label{sec:judge_count}
324	
325	\begin{table}[t]
326	\centering
327	\small
328	\begin{tabular}{rcccccc}
329	\toprule
330	$J$ & Raw & MFRM & Seq. & G-MFRM & $\Delta$ & $p$ \\
331	\midrule
332	2 & .778 & .801 & .798 & .803 & .005 & .61 \\
333	4 & .802 & .829 & .828 & .831 & .003 & .72 \\
334	6 & .810 & .842 & .841 & .844 & .003 & .68 \\
335	8 & .812 & .843 & .845 & .851 & .006 & .28 \\
336	\bottomrule
337	\end{tabular}
338	\caption{Judge count sensitivity ($\tau$). $\Delta$: G-MFRM $-$ Sequential. MFRM-based judge bias correction is the sole driver of improvement; contamination correction adds nothing at any judge count.}
339	\label{tab:judge_count}
340	\end{table}
341	
342	Table~\ref{tab:judge_count} varies the number of judges from 2 to 8. The Raw $\rightarrow$ MFRM improvement is consistent and substantial across all judge counts ($+$0.023 to $+$0.031 $\tau$), with practical benefits observable from as few as 3 judges. The G-MFRM $-$ Sequential gap is never significant ($p > 0.28$), confirming that the contamination channel contributes nothing across the judge count range.
343	
344	\subsection{Exposure Indicator Ablation}
345	\label{sec:ablation}
346	
347	\begin{table}[t]
348	\centering
349	\small
350	\begin{tabular}{lccc}
351	\toprule
352	Configuration & $r_{e_i}$ & $\tau$ & $\Delta\tau$ \\
353	\midrule
354	Full composite & 1.00 & .851 & --- \\
355	Drop ConStat & 0.72 & .849 & $-$.002 \\
356	Drop temporal & 0.88 & .850 & $-$.001 \\
357	Drop LogProber & 0.91 & .851 & .000 \\
358	ConStat only & --- & .850 & $-$.001 \\
359	Temporal only & --- & .848 & $-$.003 \\
360	LogProber only & --- & .849 & $-$.002 \\
361	No exposure (MFRM) & --- & .843 & $-$.008 \\
362	\bottomrule
363	\end{tabular}
364	\caption{Exposure indicator ablation. $r_{e_i}$: rank correlation of $e_i$ with the full composite. No single indicator's removal changes $\tau$ by more than 0.003. The framework is robust to indicator quality.}
365	\label{tab:ablation}
366	\end{table}
367	
368	Table~\ref{tab:ablation} presents leave-one-out ablation of exposure indicators. The maximum $\tau$ drop from removing any single indicator is 0.003---within noise. This reflects the low-contamination regime: when the gating mechanism is effectively closed, the specific composition of $e_i$ is immaterial. Importantly, this also demonstrates robustness: when contamination is genuinely weak, the framework does not overfit to noise in individual indicators.
369	
370	\subsection{Cross-Benchmark Replication}
371	\label{sec:wildbench}
372	
373	We replicate the full G-MFRM pipeline on WildBench (Table~\ref{tab:wildbench}).
374	
375	\begin{table}[t]
376	\centering
377	\small
378	\begin{tabular}{lcccc}
379	\toprule
380	Method & WB $\tau$ & MT $\tau$ & AH $\tau$ & Avg $\tau$ \\
381	\midrule
382	Raw Average & .795 & .801 & .823 & .806 \\
383	MFRM-only & .826 & .836 & .850 & .837 \\
384	Sequential & .828 & .839 & .851 & .839 \\
385	G-MFRM & .832 & .845 & .857 & .845 \\
386	\bottomrule
387	\end{tabular}
388	\caption{Cross-benchmark replication. WildBench confirms the same pattern: MFRM provides the benefit; contamination correction adds noise.}
389	\label{tab:wildbench}
390	\end{table}
391	
392	WildBench shows even lower contamination ($\bar{c}_n = 0.11$, 82\% covering zero), consistent with it being a newer benchmark with less training data exposure. The key cross-benchmark diagnostic: judge severity $d_j$ correlates strongly across benchmarks ($r = 0.78$), confirming it captures a stable judge attribute. In contrast, $c_n$ correlates weakly ($r = 0.35$), consistent with $c_n$ being dominated by noise rather than a stable model property under current contamination levels.
393	
394	%---------------------------------------------------------------------
395	\section{Adversarial Contamination Injection}
396	\label{sec:adversarial}
397	
398	The preceding sections establish that G-MFRM operates in detection mode on current data. A natural question is whether it can operate in correction mode when contamination is genuinely present. We test this via adversarial injection following the fragility attack protocol of Wang et al.\ (ICLR 2026): 5 of 22 target models are fine-tuned on benchmark items to simulate strong contamination ($c_n \approx 1.0$).
399	
400	\begin{table}[t]
401	\centering
402	\small
403	\begin{tabular}{lccccc}
404	\toprule
405	Setting & Raw & MFRM & Seq. & G-MFRM & $p$ \\
406	\midrule
407	Clean & .812 & .843 & .845 & .851 & .28 \\
408	Adversarial & .780 & .821 & .831 & \textbf{.871} & .008 \\
409	\bottomrule
410	\end{tabular}
411	\caption{Clean vs.\ adversarial contamination. Under injection, G-MFRM significantly outperforms all baselines ($p = 0.008$ vs.\ Sequential), recovering a $\Delta\tau$ of 0.040.}
412	\label{tab:adversarial}
413	\end{table}
414	
415	Under adversarial injection (Table~\ref{tab:adversarial}), G-MFRM recovers its full joint estimation advantage: $\tau = 0.871$ vs.\ Sequential's $0.831$ ($p = 0.008$). The $c_n$ recovery correlation reaches 0.82 between injected and estimated contamination levels, and MCMC convergence improves ($\hat{R} = 1.03$, ESS $= 195$) because the data now carry sufficient contamination signal.
416	
417	This validates both the framework's correctness and its monitoring readiness: G-MFRM is a ``thermostat'' that reads low when contamination is absent and activates correction when contamination rises.
418	
419	%---------------------------------------------------------------------
420	\section{Related Work}
421	\label{sec:related}
422	
423	\paragraph{Judge Bias Correction.}
424	CyclicJudge \cite{bai2024cyclicjudge} eliminates average judge bias via round-robin evaluation but discards non-cyclic data and ignores contamination.
425	UDA \cite{kwon2024uda} uses a neural K-factor to harmonize judge scores, achieving $-$63.4\% inter-judge std reduction, but operates as a black box without contamination awareness.
426	Neither method produces per-judge severity profiles or contamination diagnostics.
427	
428	\paragraph{Benchmark Contamination.}
429	ConStat \cite{dekoninck2024constat} detects contamination via rephrase-based $\Delta$-scores ($r^2 = 0.94$ with true contamination in controlled settings).
430	DCR \cite{xu2024dcr} factors contamination effects from ability estimates.
431	Pref Leakage \cite{dong2024prefleakage} targets preference data leakage.
432	All ignore judge variation.
433	
434	\paragraph{Psychometric Models for LLM Evaluation.}
435	Item Response Theory (IRT) has been applied to NLG evaluation \cite{otani2016irt}, and MFRM extends IRT to multi-rater settings.
436	DG-IRT \cite{sato2024dg-irt} introduces gated contamination effects in educational testing, but assumes binary exposure status and single raters.
437	G-MFRM adapts and extends this to the LLM evaluation setting with continuous exposure, multiple judge facets, and external anchoring.
438	
439	\paragraph{Joint Modeling.}
440	To our knowledge, no prior work (0/12 surveyed papers through May 2026) jointly models judge bias and benchmark contamination within a single calibration framework.
441	
442	%---------------------------------------------------------------------
443	\section{Conclusion}
444	\label{sec:conclusion}
445	
446	We present G-MFRM, a diagnostic framework for jointly detecting judge bias and benchmark contamination in LLM evaluation. Our formal analysis establishes that sequential correction introduces confounding bias whose magnitude depends on contamination strength---negligible below $\bar{c} = 0.4$ but severe above $\bar{c} = 0.6$. On real data from three benchmarks with 8 judges and 22 models, G-MFRM diagnoses that current contamination levels ($\bar{c}_n = 0.14$) are well below the critical threshold, and the framework gracefully degrades to standard MFRM. Under adversarial injection, G-MFRM activates its correction mechanism and significantly outperforms sequential approaches.
447	
448	The primary empirical contribution is a diagnostic rather than a correction: benchmark contamination in current major evaluation suites has been mitigated to the point where it does not meaningfully confound judge-based evaluation. The primary methodological contribution---the formal confounding proposition and the G-MFRM framework---is independent of this empirical finding and provides ready-made tools for ongoing monitoring as contamination landscapes evolve.
449	
450	\section*{Limitations}
451	
452	Our study covers 8 LLM judges and 22 target models across 3 benchmarks; the diagnostic conclusion that contamination is currently mitigated may not generalize to other benchmarks or future model generations where training data practices differ.
453	The rank-1 assumption ($c_n \cdot e_i$) may be insufficient when contamination arises from multiple independent sources; person-fit diagnostics can detect but not resolve such violations.
454	The three-stage procedure, while ensuring identifiability, takes $\sim$5,200 seconds on our data, which may limit adoption for rapid evaluation cycles.
455	
456	\bibliographystyle{acl_natbib}
457	\bibliography{references}
458	
459	\end{document}
460	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5700b031-f28d-4dfc-bed6-d243486876e2",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "d453351b-1162-4b3e-b44e-639869abacbb",
  "sourceToolAssistantUUID": "5700b031-f28d-4dfc-bed6-d243486876e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-21T21:31:42.760Z_

Now let me read the data generation and the distilled research skill for deeper context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d453351b-1162-4b3e-b44e-639869abacbb",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRo9WbNJytZWE5bC5c9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65955ed8-f460-47a3-b4ce-c6f9d5c6dbdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013hEQGoXc7mYnTKbFrbNA5C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2917,
      "cache_creation_input_tokens": 11126,
      "cache_read_input_tokens": 71825,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11126,
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

_source line 43 · 2026-05-21T21:31:44.726Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R9okH25DsodBwejmo162n6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/mvp/data_gen.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65955ed8-f460-47a3-b4ce-c6f9d5c6dbdc",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRo9WbNJytZWE5bC5c9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a868446c-26cc-4952-9cdd-fa2a215f0bf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013hEQGoXc7mYnTKbFrbNA5C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2917,
      "cache_creation_input_tokens": 11126,
      "cache_read_input_tokens": 71825,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11126,
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

_source line 44 · 2026-05-21T21:31:44.731Z_

<details><summary>↩ Tool result · `toolu_01R9okH25DsodBwejmo162n6`</summary>

```text
1	"""Synthetic data generation for Gated Multi-Facet Rasch Model (G-MFRM).
2	
3	Generates binary response tensors Y[n,i,j] from the model:
4	    logit(P_nij) = theta_n - b_i - d_j + c_n * e_i * (1 + s_j)
5	
6	Two confounding mechanisms controlled by rho:
7	  A) Item-level: e_i correlated with -b_i (easy items get high exposure).
8	  B) Judge-level: s_j (contamination sensitivity) correlated with -d_j
9	     (strict judges dampen contamination signal), so d̂_j absorbs part of
10	     the c_n·e_i effect when contamination is unmodeled.
11	
12	Dependencies: numpy, scipy
13	"""
14	
15	import numpy as np
16	from scipy.special import expit
17	
18	
19	def generate_gated_mfrm_data(
20	    N: int = 20,
21	    I: int = 100,
22	    J: int = 5,
23	    rho: float = 0.3,
24	    seed: int = 42,
25	) -> dict:
26	    """Generate synthetic G-MFRM data with item-level and judge-level confounding.
27	
28	    Args:
29	        N: Number of models (examinees).
30	        I: Number of items.
31	        J: Number of judges.
32	        rho: Controls both confounding strengths: (A) corr(e_i, -b_i) for
33	             item-level and (B) corr(s_j, -d_j) for judge-level.
34	        seed: Random seed for reproducibility.
35	
36	    Returns:
37	        Dict with keys:
38	            responses: (N, I, J) binary numpy array.
39	            true_params: dict of theta (N,), b (I,), d (J,), c (N,), e (I,), s (J,).
40	            config: dict of N, I, J, rho, seed.
41	    """
42	    rng = np.random.default_rng(seed)
43	
44	    theta = rng.standard_normal(N)
45	    b = rng.standard_normal(I)
46	    d = rng.normal(0, 0.5, size=J)
47	    c = np.abs(rng.normal(0, 0.5, size=N))
48	
49	    # Confounding A (item-level): e_i correlated with -b_i (easy items get high exposure)
50	    b_std = b.std()
51	    if b_std < 1e-8:
52	        b_std = 1.0
53	    z = rng.standard_normal(I)
54	    e_raw = rho * (-b / b_std) + np.sqrt(1 - rho**2) * z
55	    e = expit(e_raw)  # map to [0, 1]
56	
57	    # Confounding B (judge-level): s_j correlated with -d_j
58	    # Strict judges (high d_j) get negative s_j → dampen contamination signal
59	    d_std = d.std()
60	    if d_std < 1e-8:
61	        d_std = 1.0
62	    z_s = rng.standard_normal(J)
63	    s = 0.3 * (-rho * (d / d_std) + np.sqrt(1 - rho**2) * z_s)
64	
65	    # logit(P_nij) = theta_n - b_i - d_j + c_n * e_i * (1 + s_j)
66	    contamination = c[:, None, None] * e[None, :, None] * (1.0 + s[None, None, :])
67	    logits = (
68	        theta[:, None, None]
69	        - b[None, :, None]
70	        - d[None, None, :]
71	        + contamination
72	    )
73	    probs = expit(logits)
74	    responses = rng.binomial(1, probs).astype(np.int8)
75	
76	    return {
77	        "responses": responses,
78	        "true_params": {
79	            "theta": theta,
80	            "b": b,
81	            "d": d,
82	            "c": c,
83	            "e": e,
84	            "s": s,
85	        },
86	        "config": {"N": N, "I": I, "J": J, "rho": rho, "seed": seed},
87	    }
88	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a868446c-26cc-4952-9cdd-fa2a215f0bf0",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "2af6b577-aabb-415a-b626-9a7f1b57fa4d",
  "sourceToolAssistantUUID": "a868446c-26cc-4952-9cdd-fa2a215f0bf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T21:31:46.355Z_

<details open><summary>🔧 Tool call — Read · `toolu_012vYW3CNCmU6Vvc1PtxGnb3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/best/imagined_experiments.yaml",
  "offset": 0,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2af6b577-aabb-415a-b626-9a7f1b57fa4d",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRo9WbNJytZWE5bC5c9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "070491ed-2f6e-48ac-a617-d1085c99a01b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013hEQGoXc7mYnTKbFrbNA5C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2917,
      "cache_creation_input_tokens": 11126,
      "cache_read_input_tokens": 71825,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2917,
          "output_tokens": 226,
          "cache_read_input_tokens": 71825,
          "cache_creation_input_tokens": 11126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11126,
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

_source line 46 · 2026-05-21T21:31:46.372Z_

<details><summary>↩ Tool result · `toolu_012vYW3CNCmU6Vvc1PtxGnb3`</summary>

```text
0	tier: best
1	narrative_guidance: '原始 framing 完全成立。Confounding claim 有真实数据强实证（degradation ≥20%），
2	  framework claim 通过收敛和诊断验证，empirical claim 通过 Kendall-τ 显著提升验证。 论文按 paper_framing
3	  原样推进：Section 2 用形式化命题 + 真实数据 toy example 双重论证 confounding， 主表展示 G-MFRM 全面优于 7 baselines，headline
4	  可写 "X% higher Kendall-τ"。 DG-IRT 迁移的 novelty 通过三阶段 pipeline 的非平凡适配（binary→continuous,
5	  external anchoring）自然建立。 无需降低任何 claim 强度。
6	
7	  '
8	imagined_experiments:
9	- name: multi_judge_data_collection
10	  plan_id: exp-001
11	  description: '8 judges（GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro,
12	    Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick, Gemini 2.5 Pro） 评估 22 个 target
13	    models，MT-Bench 80 items + Arena-Hard 500 items， position swap 产生双向评分。
14	
15	    '
16	  expected_results:
17	    n_judges: 8
18	    n_target_models: 22
19	    n_items_mtbench: 80
20	    n_items_arenahard: 500
21	    total_judgments_mtbench: 28160
22	    total_judgments_arenahard: 176000
23	    missing_rate_pct: 1.8
24	    position_bias_avg_swap_disagreement_pct: 12.5
25	    api_cost_usd: 780
26	    vllm_gpu_hours: 105
27	    inter_judge_agreement_fleiss_kappa: 0.41
28	    judge_severity_range_raw_std: 0.82
29	  result_rationale: 'best 档假设数据收集无重大缺失。8 个 judges 涵盖 4 家厂商 + 3 个开源， 缺失率 <2% 因 API
30	    和 vLLM 基础设施成熟。position swap disagreement ~12.5% 符合已知 LLM positional bias 文献（Zheng
31	    et al. 2023 报告 10-15%）。 inter-judge Fleiss κ≈0.41 处于 "moderate agreement" 范围，这正是
32	    G-MFRM 需要的场景——若 judges 高度一致则无需建模 severity。 judge severity raw std=0.82 表明 judges
33	    间存在可量化的系统性差异， 为后续 MFRM 的 d_j 估计提供充分变异。API 成本低于 $900 预算。
34	
35	    '
36	  tables:
37	  - name: 'Table S1: Data Collection Summary'
38	    columns:
39	    - Judge
40	    - Provider
41	    - Type
42	    - MT-Bench_judgments
43	    - Arena-Hard_judgments
44	    - Missing_pct
45	    - Avg_score
46	    rows:
47	    - - GPT-5.5
48	      - OpenAI
49	      - API
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "070491ed-2f6e-48ac-a617-d1085c99a01b",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "35b96885-0f8a-47be-b83a-71185f017f06",
  "sourceToolAssistantUUID": "070491ed-2f6e-48ac-a617-d1085c99a01b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-21T21:31:51.026Z_

Now I have comprehensive information to write the review. Let me also read the literature map for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35b96885-0f8a-47be-b83a-71185f017f06",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRogSCGddNTPJdPM8AN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d817819e-1538-4162-b14f-c7d0be908f12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V7gScru7VJ83hz8NBHgi5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5463,
      "cache_read_input_tokens": 82951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5463,
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

_source line 48 · 2026-05-21T21:31:52.706Z_

<details open><summary>🔧 Tool call — Read · `toolu_012ycZwPsfkQ1DiNu7QqcV9E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/literature_map.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d817819e-1538-4162-b14f-c7d0be908f12",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRogSCGddNTPJdPM8AN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6732cb29-c70d-42d6-877a-1a724e855b12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V7gScru7VJ83hz8NBHgi5i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5463,
      "cache_read_input_tokens": 82951,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5463
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 82951,
          "cache_creation_input_tokens": 5463,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5463,
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

_source line 49 · 2026-05-21T21:31:52.712Z_

<details><summary>↩ Tool result · `toolu_012ycZwPsfkQ1DiNu7QqcV9E`</summary>

```text
1	meta:
2	  last_updated: "2026-05-21T16:40:00Z"
3	  total_papers: 12
4	categories:
5	  - key: "psychometric_foundation"
6	    name: "Psychometric & IRT Foundation"
7	    narrative: "Core psychometric models: DG-IRT gating mechanism for cheating detection, MFRM applied to LLM raters, and IRT-based LLM evaluation frameworks"
8	  - key: "judge_bias_correction"
9	    name: "Judge Bias Correction"
10	    narrative: "Methods for detecting and correcting systematic biases in LLM-as-a-judge evaluation pipelines"
11	  - key: "contamination_detection"
12	    name: "Contamination Detection & Adjustment"
13	    narrative: "Methods for detecting and quantifying benchmark contamination in LLM evaluation"
14	  - key: "unified_evaluation"
15	    name: "Unified Evaluation Frameworks"
16	    narrative: "Comprehensive LLM evaluation frameworks and benchmarks that combine multiple assessment dimensions"
17	papers:
18	  shu2013dgirt:
19	    title: "Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise"
20	    authors:
21	      - "Shu, Z."
22	      - "Henson, R."
23	      - "Luecht, R."
24	    year: 2013
25	    venue: "Psychometrika"
26	    doi: "10.1007/s11336-012-9311-3"
27	    bibtex_key: "shu2013dgirt"
28	    category: "psychometric_foundation"
29	    role: "foundation"
30	    relevance: "Core methodological inspiration. DG-IRT decomposes observed performance into genuine ability and cheating-inflated components via a gating mechanism. G-MFRM adapts this gating logic from educational cheating to LLM benchmark contamination."
31	    verified: false
32	    added_by: "director"
33	    added_at: "2026-05-21T16:40:00Z"
34	
35	  wang2025mfrm_llm:
36	    title: "Comparing Human and AI Rater Effects Using the Many-Facet Rasch Model"
37	    authors:
38	      - "Wang, Y."
39	    year: 2025
40	    venue: "arXiv"
41	    arxiv_id: "2505.18486"
42	    bibtex_key: "wang2025mfrm_llm"
43	    category: "psychometric_foundation"
44	    role: "foundation"
45	    relevance: "Most direct predecessor. Applies MFRM to compare 10 LLM raters with human experts, demonstrating MFRM's applicability to LLM judge calibration. Does NOT model contamination — the gap G-MFRM fills."
46	    verified: false
47	    added_by: "director"
48	    added_at: "2026-05-21T16:40:00Z"
49	
50	  lin2025psnirt:
51	    title: "Lost in Benchmarks? Rethinking LLM Benchmarking with IRT — PSN-IRT"
52	    authors:
53	      - "Lin, Z."
54	    year: 2026
55	    venue: "AAAI"
56	    bibtex_key: "lin2025psnirt"
57	    category: "psychometric_foundation"
58	    role: "baseline"
59	    relevance: "Neural 4PL IRT for LLM benchmark evaluation. Demonstrates scalability of IRT to LLMs but lacks judge facet and contamination modeling. Serves as IRT-based baseline without multi-facet structure."
60	    verified: false
61	    added_by: "director"
62	    added_at: "2026-05-21T16:40:00Z"
63	
64	  cyclicjudge2026:
65	    title: "CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation"
66	    authors:
67	      - "Unknown"
68	    year: 2026
69	    venue: "arXiv"
70	    bibtex_key: "cyclicjudge2026"
71	    category: "judge_bias_correction"
72	    role: "baseline"
73	    relevance: "Primary bias-only baseline. Eliminates judge bias via round-robin assignment but completely ignores contamination. G-MFRM addresses both jointly."
74	    verified: false
75	    added_by: "director"
76	    added_at: "2026-05-21T16:40:00Z"
77	
78	  fiedler2026bias_uncertainty:
79	    title: "Bias and Uncertainty in LLM-as-a-Judge Estimation"
80	    authors:
81	      - "Fiedler, M."
82	    year: 2026
83	    venue: "arXiv"
84	    arxiv_id: "2605.06939"
85	    bibtex_key: "fiedler2026bias_uncertainty"
86	    category: "judge_bias_correction"
87	    role: "related"
88	    relevance: "Introduces formal J/delta-J diagnostics for judge bias, identifies sign-reversal failure modes in shared-calibration comparisons. Stays within classical test theory. G-MFRM's confounding argument positions Fiedler's sign-reversal as downstream consequence of unmodeled contamination."
89	    verified: false
90	    added_by: "director"
91	    added_at: "2026-05-21T16:40:00Z"
92	
93	  soumik2026judging_judges:
94	    title: "Judging the Judges: Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines"
95	    authors:
96	      - "Soumik, M."
97	    year: 2026
98	    venue: "arXiv"
99	    arxiv_id: "2604.23178"
100	    bibtex_key: "soumik2026judging_judges"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6732cb29-c70d-42d6-877a-1a724e855b12",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "4c80789a-e6c1-4b7d-a1fc-6db46571040c",
  "sourceToolAssistantUUID": "6732cb29-c70d-42d6-877a-1a724e855b12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-21T21:31:56.639Z_

I now have a thorough understanding of the full project. Let me now submit the review via the designated tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c80789a-e6c1-4b7d-a1fc-6db46571040c",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRp9WNh3A3ygGcDj1kr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9af3a59a-6aa2-47b9-8cd0-32b1d67fa782",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3zn9QaTTJgyXGSivNkMbD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1744,
      "cache_read_input_tokens": 88414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1744,
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

_source line 51 · 2026-05-21T21:31:57.419Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013q1MJCZDeBecjCKywxYLaJ`</summary>

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
  "parentUuid": "9af3a59a-6aa2-47b9-8cd0-32b1d67fa782",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRp9WNh3A3ygGcDj1kr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b31eed34-fd0f-4168-b862-59180df44165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3zn9QaTTJgyXGSivNkMbD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1744,
      "cache_read_input_tokens": 88414,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1744
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 113,
          "cache_read_input_tokens": 88414,
          "cache_creation_input_tokens": 1744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1744,
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

_source line 52 · 2026-05-21T21:31:57.421Z_

<details><summary>↩ Tool result · `toolu_013q1MJCZDeBecjCKywxYLaJ`</summary>

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
  "parentUuid": "b31eed34-fd0f-4168-b862-59180df44165",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "772cc4da-2dbe-4e30-a844-fcd9d484be30",
  "sourceToolAssistantUUID": "b31eed34-fd0f-4168-b862-59180df44165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-21T21:32:04.224Z_



Now I have all the information needed. Let me carefully analyze the three paper versions (best/median/worst) and the project internals, then write my review. The task asks me to review the paper as described in the summary — which corresponds to the **worst-case** scenario paper (the one actually matching the tables and results described in the prompt).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "772cc4da-2dbe-4e30-a844-fcd9d484be30",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRpVcbh632BBGkaPbev",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "901e3005-87c4-4caf-ae73-29bf34a44a95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gYkhSquBBYSSvigGaXWyT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 90158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 737,
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

_source line 54 · 2026-05-21T21:34:10.386Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01H4QH4Au7HcxcVVuFn66oda`</summary>

```json
{
  "report": "\n# Reviewer 1 (R1): Methods and Experiments\n\n## Paper Summary\n\nThis paper identifies an omitted variable bias problem when judge severity and benchmark contamination are corrected sequentially in LLM-as-a-judge evaluation. The authors formalize this as Proposition 1 (first-order bias expression), then propose G-MFRM, a three-stage psychometric framework that jointly estimates model ability, item difficulty, judge severity, and contamination susceptibility. On real data (8 judges x 22 models x 3 benchmarks, ~186K evaluations), they find contamination is low (mean c_n = 0.14), G-MFRM degrades gracefully to MFRM (tau = 0.851 vs 0.843, p = 0.31), and only under adversarial injection does G-MFRM show significant advantage (tau = 0.871 vs 0.831, p = 0.008).\n\n---\n\n## 1. Soundness (3/5)\n\n### Proposition 1\n\nThe first-order bias expression (Eq. 2) follows from standard omitted variable bias logic adapted to the psychometric setting. The derivation is conceptually correct: when d_j and c_n * e_i are non-orthogonal and only d_j is modeled, the OLS/MLE estimator absorbs the projection of the omitted term onto the modeled regressors.\n\nHowever, several concerns arise:\n\n- **Regularity conditions are not stated.** The proposition implicitly assumes the standard MFRM is estimated via something approximating OLS on the linearized model. But MFRM is an ordinal logistic model estimated via MCMC. The connection between the linear OVB result and the nonlinear Bayesian estimation needs explicit justification. The \"standard omitted variable bias analysis\" claim glosses over the gap between linear regression OVB and nonlinear psychometric model misspecification.\n\n- **The bias expression involves Cov(d_j, c_n * e_i).** This is a covariance between a J-dimensional quantity and an N x I interaction term. The paper does not clarify over which index this covariance is computed, or how the design matrix structure (the crossed N x I x J design) interacts with the bias formula. The scaling factor f(N, J, I) is introduced but never derived or bounded.\n\n- **MC validation is convincing on direction (97.2%) but the \"magnitude relative error 8%\" claim masks heterogeneity.** Looking at Table 1, the absolute biases at low rho are tiny (0.003-0.004), where measurement noise dominates, and the relative error at these levels is likely much higher. The 8% figure is probably driven by the high-rho, high-c settings where the signal is strong.\n\n- **The proposition is stated for the bias-first sequential estimator but the paper claims \"both orderings produce biased estimates.\"** The contam-first case is not formalized. While the symmetry argument is intuitive, it should be stated explicitly or proven.\n\n### G-MFRM Model Specification\n\n- **The sigmoid gate g(e_i) = sigma(alpha(e_i - e_0)) appears in the model equation (Eq. 3) but the implementation in the MVP code (models.py) uses a simple linear c_n * e_i without any gating.** This is a significant gap between the described method and the validated implementation. The gate parameters alpha and e_0 add model complexity that has not been validated even in simulation.\n\n- **Stage 3 convergence is problematic.** R-hat = 1.06 exceeds the conventional 1.01 threshold (Vehtari et al. 2021 recommend < 1.01 for reliable inference). ESS = 112 is marginal. The paper acknowledges this is due to \"weak contamination signal\" and \"prior-dominated posteriors,\" but this undermines the reliability of c_n estimates. If the data provide negligible information beyond the prior (KL = 0.08), then c_n is essentially the prior, not a data-driven estimate.\n\n- **The Half-Normal prior on c_n is appropriate in principle** (contamination inflates scores), but the choice of sigma_c is not discussed. Given that the posterior is prior-dominated, the prior specification matters enormously and should be subjected to sensitivity analysis.\n\n### \"Graceful Degradation\" Narrative\n\nThe framing of null results as \"graceful degradation\" is a reasonable post-hoc interpretation, but it should be recognized as such. The paper was designed with the expectation of finding significant contamination (the paper_framing.md explicitly plans for \"Tier A: strong contamination\" as the primary narrative and \"Tier B: weak contamination\" as the fallback). The \"diagnostic framework / monitoring tool\" framing emerged after the real-data results showed negligible contamination. This is not inherently wrong — science should report null findings honestly — but the paper should be more transparent that the diagnostic framing was not the original hypothesis.\n\nThe \"thermostat\" metaphor is appealing but somewhat misleading. A thermostat has a known calibration. G-MFRM's ability to \"activate\" under adversarial injection does not prove it would activate at the right threshold for unknown real-world contamination at intermediate levels.\n\n---\n\n## 2. Experimental Rigor\n\n### Baselines\n\nThe baseline selection is comprehensive. Seven methods spanning three categories (no correction, bias-only, contamination-only, and sequential) provide good coverage. The inclusion of both CyclicJudge and UDA as bias-only baselines is appropriate.\n\n**However, the comparison is somewhat misleading in the main results.** G-MFRM is not significantly better than MFRM-only (p = 0.31), Sequential (p = 0.28), or UDA (p = 0.22). The paper correctly reports this, but the framing still positions G-MFRM as \"nominally highest.\" A fairer summary would state: \"judge severity modeling is the primary driver of improvement; the contamination component adds nothing on current data.\"\n\n### Ground Truth\n\nChatbot Arena Elo as ground truth is a reasonable but imperfect choice. Key limitations:\n\n- **User self-selection bias**: Arena users are not representative of general LLM use cases. Models that are popular on Arena may receive more votes, creating a popularity-driven Elo that does not purely reflect ability.\n- **Temporal confounding**: Arena Elo changes over time as new models enter. The snapshot used for ground truth matters but is not specified.\n- **Kendall tau with only 22 models** has limited statistical power. The difference between tau = 0.843 and 0.851 on 22 items is well within noise, as the bootstrap CI [-0.008, 0.021] confirms.\n\n### Adversarial Injection\n\nThe adversarial experiment is the paper's strongest result but raises concerns:\n\n- **Fine-tuning 5/22 models on benchmark items** is a strong intervention. Real-world contamination is typically incidental (benchmark items in training corpora) rather than intentional fine-tuning. The threat model may be unrealistically extreme.\n- **The 5 contaminated models are not named.** Were they chosen randomly? Were they the weaker models (to make contamination effects more visible)? This matters for interpreting c_n recovery.\n- **c_n recovery correlation of 0.82 is good but not 0.97** (as in the best-case dream). This suggests the gating mechanism captures the overall direction but not the precise magnitude of injection.\n- **MCMC convergence improves under adversarial injection** (R-hat = 1.03, ESS = 195 vs R-hat = 1.06, ESS = 112 in clean), confirming that the contamination channel needs strong signal to be identifiable. This is consistent but somewhat undermines the \"monitoring readiness\" claim for moderate contamination levels.\n\n### Missing Experiments and Concerns\n\n1. **No analysis of when G-MFRM activates at intermediate contamination levels.** The paper shows it does nothing at c_bar = 0.14 and works at c_bar ~ 1.0 (adversarial). What about c_bar = 0.3, 0.4, 0.5? The MC simulations give theoretical predictions but no empirical validation in this range.\n\n2. **Exposure indicator quality is poor.** Only 11% of items show significant exposure. Composite e_i mean = 0.07 with skewness 2.1. This means the Stage 2 anchoring provides very little contamination signal to Stage 3. The exposure ablation (Table 10) confirms this: dropping any indicator changes tau by at most 0.003, because the entire exposure signal is negligible.\n\n3. **Facet fit for c_n is concerning.** 22.7% misfit rate (5 of 22 models) with infit range [0.60, 1.82] is well outside acceptable bounds. Values below 0.70 indicate Guttman-like overfit; values above 1.30 indicate noise. This suggests the rank-1 contamination structure is a poor fit for the data — or, more likely, that there is insufficient contamination signal to estimate c_n at all.\n\n4. **Person-fit / c_n correlation is negligible.** In the worst-case paper, r = 0.18 and 0.12 for l_z and EMRi respectively. This contradicts the best-case paper's r = 0.72. The near-zero convergent validity suggests c_n is not measuring a meaningful construct in the real data.\n\n5. **Cross-benchmark c_n correlation is weak.** r = 0.35 between WildBench and MT-Bench+Arena-Hard c_n estimates. If c_n captured a stable model property (memorization tendency), this correlation should be much higher. The weak correlation suggests c_n is noise under current contamination levels.\n\n6. **The paper uses 8 references.** For an EMNLP submission, this is extremely sparse. Key works in the psychometric modeling literature (Rasch, Bond & Fox, de Ayala, etc.), IRT for NLP (Rodriguez et al. 2021, Vania et al. 2021), and recent contamination work (Jacovi et al. 2023, Oren et al. 2023) are missing.\n\n---\n\n## 3. Reproducibility (3/5)\n\n**Strengths:**\n- MCMC configuration is fully specified (NumPyro, NUTS, warmup=2000, samples=4000, chains=4, target_accept=0.95, NCP).\n- Data dimensions are clear (8 judges, 22 models, 580 items, ~186K evaluations).\n- Runtime is reported (~5,200 seconds).\n\n**Weaknesses:**\n- **No code or data release is mentioned.** This is a significant gap for a methods paper.\n- **ConStat reference variant construction is underspecified.** \"3 reference variants per item\" with \"89% human equivalence pass rate\" — but how were the rephrasings generated? What prompts? What human validation protocol?\n- **LogProber is mentioned but no reference is given** and no implementation details are provided. Is this an existing tool or something built for this paper?\n- **Composite exposure weight determination** (\"cross-validated weights\") lacks detail: what cross-validation scheme? What loss function?\n- **The 22 target models are not fully listed.** Only a few are named in Table 5. The full list matters for reproducibility.\n- **The sigmoid gate parameters alpha and e_0** are described but their learned values are not reported.\n\n---\n\n## 4. Key Strengths\n\n- **Well-motivated problem.** The confounding between judge severity and contamination is a genuine methodological concern that has not been addressed in the literature. The omitted variable bias framing is elegant and accessible.\n\n- **Honest reporting of null results.** The paper does not overclaim. The main results table correctly reports non-significant differences, and the \"graceful degradation\" interpretation, while post-hoc, is stated clearly.\n\n- **Comprehensive experimental design.** The coverage of baselines, ablations, sensitivity analyses, cross-benchmark replication, and adversarial testing is thorough for a 7-page paper.\n\n- **Sound psychometric foundation.** The extension of MFRM with DG-IRT-style gating is a principled approach. The three-stage estimation procedure is well-motivated as a solution to the identifiability problem.\n\n- **The adversarial injection experiment provides a convincing proof-of-concept** that joint estimation can outperform sequential when contamination is genuinely present.\n\n---\n\n## 5. Key Weaknesses\n\n- **The primary empirical finding is a null result.** G-MFRM does not significantly outperform MFRM or Sequential on real data. The paper is essentially saying: \"contamination does not confound current LLM evaluation, but here is a tool in case it does in the future.\" While methodologically valuable, this limits the paper's immediate practical impact.\n\n- **Disconnect between theory/simulation and real data.** The MVP experiments validated G-MFRM at c_bar ~ 1.5 with RMSE improvement of 43.8%. The real data has c_bar = 0.14 — an order of magnitude lower. The theoretical framework works but the empirical setting does not require it. This gap undermines the motivation.\n\n- **Stage 3 convergence issues (R-hat = 1.06, ESS = 112) are not adequately addressed.** The paper acknowledges them but does not explore remedies (tighter priors, different parameterizations, variational inference). These diagnostics fall below standard thresholds for reliable Bayesian inference.\n\n- **The sigmoid gating mechanism described in the paper is not validated.** The MVP code implements a simple linear c_n * e_i without the sigmoid gate. The additional parameters (alpha, e_0) introduced by the gate have unknown identifiability properties and are never reported.\n\n- **Only 8 references** is far below expectations for an EMNLP paper. Critical related work is omitted, making it difficult to assess the novelty contribution against the broader IRT/psychometric literature.\n\n- **The exposure estimation pipeline (Stage 2) contributes almost nothing** on real data. With only 11% of items showing significant exposure and prior-posterior KL of 0.08, the entire contamination channel is effectively dormant. This raises the question: is the framework solving a problem that currently does not exist?\n\n- **c_n estimates lack construct validity on real data.** Low person-fit correlation (r = 0.18), low cross-benchmark correlation (r = 0.35), high misfit rate (22.7%), and prior-dominated posteriors collectively suggest c_n does not capture a meaningful latent construct in the current data.\n\n---\n\n## 6. Questions for Authors\n\n1. **The sigmoid gate g(e_i) = sigma(alpha(e_i - e_0)) appears in the paper but not in the MVP code. Was the gate actually used in the real-data experiments? If so, what are the learned values of alpha and e_0? If not, why is it described as part of the method?**\n\n2. **How sensitive are the results to the Half-Normal prior on c_n? Specifically, if you use a more informative prior (e.g., Half-Normal(0, 0.1) reflecting the observed low contamination) or a less informative prior (e.g., Half-Normal(0, 2.0)), how do tau, R-hat, and ESS change?**\n\n3. **In the adversarial injection, how were the 5 contaminated models selected? Were they fine-tuned on MT-Bench items, Arena-Hard items, or both? What was the fine-tuning protocol (epochs, learning rate, data mixing)?**\n\n4. **The Proposition 1 bias expression includes f(N, J, I) described as a \"design-dependent scaling factor\" but never derived. Can you provide the explicit form of f(N, J, I) for the crossed design used in this paper?**\n\n5. **Given that c_n is prior-dominated (KL = 0.08, 78% of CIs covering zero), how do you distinguish between \"contamination is genuinely absent\" and \"the model lacks power to detect contamination\"? What sample size or exposure level would be needed for adequate detection power?**\n\n6. **The cross-benchmark c_n correlation is only r = 0.35. How do you reconcile the claim that G-MFRM provides \"interpretable per-model contamination estimates\" with this evidence that the estimates are unstable across benchmarks?**\n\n7. **Have you considered a model comparison approach (e.g., WAIC, LOO-CV) to formally test whether the contamination parameters improve model fit beyond MFRM? This would be more informative than the tau comparison.**\n\n8. **LogProber is mentioned as an exposure indicator but no citation or implementation details are given. Is this an existing tool? How does it compute per-item memorization scores?**\n\n9. **The paper reports 8 references. Are you planning to expand the related work section? Key missing references include psychometric foundations (Bond & Fox, de Ayala), IRT for NLP (Rodriguez et al. 2021), and recent contamination detection beyond ConStat/DCR.**\n\n10. **Table 8 shows c_n has 22.7% misfit rate with infit range [0.60, 1.82]. Values of 1.82 indicate severe noise. Have you identified which models are misfitting and whether there is a systematic pattern (e.g., model size, provider)?**\n\n---\n\n## 7. Preliminary Scores\n\n- **Soundness: 3/5.** The theoretical framework is conceptually sound but the formalization has gaps (unstated regularity conditions, unvalidated sigmoid gate, convergence issues). The MC validation is adequate but the real-data application does not test the method in its intended operating regime.\n\n- **Excitement: 2.5/5.** The problem is well-motivated and the framework is principled, but the primary empirical finding is that the problem does not currently exist in practice. The paper is essentially a methodology paper validated only on synthetic/adversarial data, with a null result on real data. The \"monitoring tool\" framing is reasonable but not exciting.\n\n- **Reproducibility: 3/5.** Core MCMC configuration is specified, but no code/data release is mentioned, exposure estimation details are sparse, LogProber is undefined, and the sigmoid gate's actual use is unclear.\n\n- **Overall Assessment: 2.5/5 (Borderline Findings).** The paper identifies a real methodological concern (confounding between judge bias and contamination), provides a principled solution (G-MFRM), and validates it theoretically and on synthetic data. However, the primary empirical contribution is a null result — contamination does not currently confound LLM evaluation on major benchmarks. The convergence issues, prior-dominated posteriors, and lack of construct validity for c_n on real data weaken the methodological contribution. The paper would benefit from (a) demonstrating the method on data where contamination is organically present (not artificially injected), (b) resolving the disconnect between the described sigmoid gate and the implemented linear model, (c) expanding the related work, and (d) providing code and data for reproducibility. In its current form, the contribution is below the EMNLP main conference threshold but could reach Findings with revisions.\n\n- **Confidence: 4/5.** I am familiar with IRT/MFRM literature, Bayesian inference diagnostics, and LLM evaluation methodology. I have read the paper carefully and examined the implementation code. My main uncertainty is whether the adversarial injection experiment is sufficient to demonstrate \"monitoring readiness\" for the EMNLP community.\n\n---\n\n## Summary for Authors\n\nThe paper tackles an important and previously unaddressed problem: the confounding between judge severity bias and benchmark contamination in LLM evaluation. The G-MFRM framework is principled, and the theoretical analysis (Proposition 1) is a genuine contribution. However, the paper's empirical story is fundamentally a null result — current contamination levels are too low for the method to provide any benefit over standard MFRM. The adversarial injection experiment demonstrates proof-of-concept but does not address the gap between the theoretical regime where G-MFRM excels (c_bar > 0.6) and the observed reality (c_bar = 0.14). The convergence diagnostics, prior-dominated posteriors, and construct validity evidence collectively suggest that the contamination channel is not identifiable on current data. I recommend the authors either find a setting where contamination is organically present at meaningful levels, or reframe the contribution more explicitly as a theoretical/methodological advance with prospective utility, while acknowledging that the current empirical validation is limited to synthetic and adversarial settings.\n",
  "project": "gated_mfrm_judge_bias",
  "tier": "worst",
  "dream_id": "dream_20260521T204917",
  "overall_score": "2.5 — Borderline Findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "901e3005-87c4-4caf-ae73-29bf34a44a95",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRpVcbh632BBGkaPbev",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cd65697a-8ecd-458f-a490-3d6a3d009a12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011gYkhSquBBYSSvigGaXWyT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 90158,
      "output_tokens": 5115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 737
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5115,
          "cache_read_input_tokens": 90158,
          "cache_creation_input_tokens": 737,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 737,
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

_source line 55 · 2026-05-21T21:34:13.841Z_

<details><summary>↩ Tool result · `toolu_01H4QH4Au7HcxcVVuFn66oda`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/worst/review_report.md\", \"dream_id\": \"dream_20260521T204917\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd65697a-8ecd-458f-a490-3d6a3d009a12",
  "isSidechain": true,
  "promptId": "1237d6e8-1113-48bd-9290-354158e7fcf5",
  "agentId": "ad7f414c5f9981729",
  "type": "user",
  "uuid": "58d37ec4-a699-4bbd-bdc3-b6e6364548e3",
  "sourceToolAssistantUUID": "cd65697a-8ecd-458f-a490-3d6a3d009a12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-21T21:34:28.788Z_

Review submitted successfully. Here is a summary of the review:

**Overall Assessment: 2.5/5 (Borderline Findings)**

The review evaluates the worst-case scenario paper, where real-data contamination is low (c_bar = 0.14) and G-MFRM produces a null result against baselines.

**Core findings of the review:**

1. **Soundness (3/5):** Proposition 1 is conceptually correct but has unstated regularity conditions and an unspecified scaling factor f(N,J,I). The sigmoid gate described in the paper is not present in the MVP implementation code. Stage 3 convergence (R-hat=1.06, ESS=112) falls below standard thresholds.

2. **Excitement (2.5/5):** The problem is well-motivated, but the primary empirical finding is that the problem does not currently exist in practice. The paper is essentially a methodology validated only on synthetic/adversarial data with a null result on real data.

3. **Reproducibility (3/5):** MCMC configuration is specified, but no code/data release is mentioned, LogProber is undefined, and exposure estimation details are sparse.

**Key weaknesses identified:**
- Primary result is null (G-MFRM vs MFRM: p=0.31)
- Disconnect between theory (c_bar~1.5) and practice (c_bar=0.14)
- c_n estimates lack construct validity (cross-benchmark r=0.35, person-fit r=0.18, 22.7% misfit rate, prior-dominated posteriors)
- Sigmoid gate in paper does not match linear implementation in code
- Only 8 references — far below EMNLP expectations

**Key strengths:**
- Genuine gap in the literature (no prior joint modeling of both distortions)
- Honest reporting of null results
- Comprehensive experimental design with ablations, sensitivity, and adversarial testing
- Adversarial injection provides convincing proof-of-concept

The review was saved to `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/artifacts/dream_reports/dream_20260521T204917/worst/review_report.md`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58d37ec4-a699-4bbd-bdc3-b6e6364548e3",
  "isSidechain": true,
  "agentId": "ad7f414c5f9981729",
  "requestId": "req_011CbGRzYm8mtbehSgowEfXy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c11e9d45-375f-4aac-926e-02d46328ddde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "sessionId": "ee81a174-9ebc-470f-bc34-08485e997e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrUfejTMJCyQ7pqa7yh8PV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5243,
      "cache_read_input_tokens": 90895,
      "output_tokens": 529,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5243
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 529,
          "cache_read_input_tokens": 90895,
          "cache_creation_input_tokens": 5243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5243,
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
