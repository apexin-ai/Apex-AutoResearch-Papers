# Research conversation: You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Re

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a44eaedacc19023c8.jsonl`
- **Structured JSON:** [`3e88c3296d0f4022122c.json`](../../sessions/3e/3e88c3296d0f4022122c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

53 recorded events

### User

_source line 1 · 2026-05-20T10:17:51.544Z_

You are Reviewer R1 for a top ML venue review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus is **methods and experiments**.

## Paper Summary

Title: "On the Fundamental Limits of Binary-Response Contamination Detection: Item Response Theory Person-Fit Statistics Applied to Large Language Models"

The paper investigates whether IRT person-fit statistics (lz*) can detect benchmark contamination in LLMs using only binary (correct/incorrect) response patterns—the minimal-information operating point. Through simulation, controlled contamination experiments, and a leaderboard audit, the paper establishes three findings:
1. LLM response patterns universally violate IRT assumptions (local independence, unidimensionality), producing extreme lz* ≫ 0 even for clean models (93% flagged).
2. SFT contamination induces ability shifts inseparable from genuine improvement in binary responses (Cohen's d=0.25, AUROC=0.585 at best, drops to 0.53 after RL).
3. A theoretical power analysis reveals an inverted-U detection gap—power nadir ≤0.12 at moderate contamination (25-40%).

The paper frames this as characterizing the fundamental limits of binary-response detection and establishes a "detection information hierarchy" quantifying AUROC gain at each information-access level (binary→re-test: +0.235; binary→token probs: +0.195).

## Paper Structure and Key Details

**Section 3: IRT-FIT Framework**
- Uses pre-calibrated 4PL item parameters from PSN-IRT
- Estimates model ability θ via MLE, computes lz* statistic
- Introduces relative detection: Δlz* = lz*_contam - lz*_clean

**Section 4: Theoretical Power Analysis**
- Derives power function from Snijders (2001) variance formula Var(lz*) ≈ 1 + O(1/n)
- Models contaminated items as answered correctly with p=1 regardless of difficulty
- Finds inverted-U shape: nadir at π≈0.33 (theory) vs π=0.35 (simulation)
- R² between theory and simulation: 0.61 average (range 0.51-0.68)
- Theory overestimates power by 15-30%; closed-form bound is ~2× loose

**Section 5: Simulation Study**
- Simulates under 4PL with contamination levels π ∈ {0.15, 0.25, 0.35, 0.50, 0.60, 0.75, 0.90, 1.00}
- Two-sided detection: negative-side (lz* < -1.96) and positive-side (lz* > 1.96)
- Key results (Table 3): MMLU (14K items) at 15% → 0.979 power; at 35% → 0.12 (nadir); HumanEval (164 items) never exceeds 0.25 even at 100%

**Section 6: Controlled Contamination Experiments**
- Two models: Qwen3.5-9B and Gemma-4-31B
- QLoRA SFT on MMLU items at π ∈ {0, 0.05, 0.10, 0.15, 0.25, 0.50}
- 3 random seeds per condition
- Pilot (Table 4): Qwen3.5-9B × MMLU. 15%: Δlz*=+2.7 (p=0.18); 50%: Δlz*=-1.5 (p=0.42). Direction inconsistent.
- Full results (Tables 5,6): Qwen shows non-monotonic Δlz*; Gemma shows mostly negative Δlz* at higher contamination
- AUROC (Table 7): Best=0.62 (Qwen@15%), Average@15%=0.585, Average@5%=0.505
- Cohen's d@15%: Qwen=0.35, Gemma=0.14, Average=0.25
- Cross-model direction agreement: 60% (3/5 levels)
- Mechanism (Section 6.4): SFT knowledge transfer—QLoRA learns domain knowledge, θ increases, IRT absorbs contamination signal

**Section 7: Post-RL Analysis**
- GRPO applied to SFT-contaminated Qwen3.5-9B
- Signal retention: 33% (Δlz* drops from 2.7 to 0.9 at 15%)
- Post-RL AUROC: 0.53 (random classifier)

**Section 8: Leaderboard Audit**
- Data: 42 models from HuggingFace Open LLM Leaderboard v1 (out of 7,200+; only 0.9% have per-item data)
- Flagged rates: 93% absolute, 65% relative
- Cross-benchmark Spearman: ρ=0.18, only 2/10 pairs significant
- No significant temporal trend (p=0.34)

**Section 9: Detection Information Hierarchy**
- IRT-FIT vs ConStat (AUROC 0.82) vs Min-K%++ (AUROC 0.78)
- IRT-FIT Type-I error: 0.42 at α=0.05 (catastrophic)
- ConStat: 0.08; Min-K%++: 0.11

**Section 10: Extended Analysis**
- BBH (6,511 items) and MATH (5,000 items) added; 4PL calibrated from scratch
- Simulation power scales with n_items (R²=0.91), but controlled AUROC uniformly poor
- Domain-level analysis: granularity-power tradeoff; small domains (<150 items) → AUROC=0.50

**Section 11: Ablation Studies**
- 4PL vs 3PL(d=1): all metrics differ by ≤0.03
- Multiscale lz^m: +0.015 AUROC improvement, marginal

**Section 12: Limitations**
- Only QLoRA SFT (not pretraining exposure)
- Only 42 models in leaderboard audit
- Only 2 model sizes (9B, 31B)
- Theoretical bound relies on Snijders formula with local independence assumption violated

## Experiment Design Reference (from review_context.yaml)

The full experimental design includes these experiments:
1. Extended simulation with high contamination + two-sided power curves ✓ (covered in paper)
2. Control experiment pilot: Qwen3.5-9B × MMLU ✓ (covered)
3. Full control experiment: dual model × full contamination spectrum ✓ (covered)
4. Power theory derivation ✓ (covered)
5. Leaderboard data availability survey ✓ (covered)
6. Leaderboard audit ✓ (covered)
7. 4PL vs 3PL ablation ✓ (covered)
8. Baseline method comparison ✓ (covered)
9. Multiscale lzm ✓ (covered)
10. Post-RL hypothesis test ✓ (covered)
11. Extended benchmarks (BBH, MATH) ✓ (covered)
12. MMLU domain-level analysis ✓ (covered)

All 12 imagined experiments appear to be reflected in the paper.

## Your Task

Provide a detailed review focusing on:
1. **Methodological soundness**: Are the methods (IRT-FIT framework, theoretical derivation, controlled experiments, baseline comparison) correct and well-justified?
2. **Experimental rigor**: Are the experiments well-designed? Are there confounds? Is the evaluation fair?
3. **Statistical validity**: Are the statistical claims supported? Are there issues with multiple comparisons, sample sizes, etc.?
4. **Reproducibility**: Is there enough detail to reproduce?
5. **Strengths and weaknesses** (at least 3 each)

Structure your review as:
- Summary (2-3 sentences)
- Strengths (numbered)
- Weaknesses (numbered)
- Questions for Authors
- Minor Issues
- Overall Assessment (score 1-6 with justification)
- Confidence (1-5)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "0fc17366-7152-4fda-b336-e424eb752e5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T10:17:51.555Z_

```json
{
  "parentUuid": "0fc17366-7152-4fda-b336-e424eb752e5d",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
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
  "uuid": "08e78e33-1b00-4367-aeea-a4ef6d0dd8d2",
  "timestamp": "2026-05-20T10:17:51.555Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T10:17:55.309Z_



I need to read the actual paper and supporting materials to provide a thorough review. Let me start by exploring the project structure and reading the key files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08e78e33-1b00-4367-aeea-a4ef6d0dd8d2",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDec8xJibZT6aQwqtLwv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d8a04a0a-9712-48da-838e-72247eee9561",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrWjBNTKyfCxbBTzN891fC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16631,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16631,
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

_source line 4 · 2026-05-20T10:17:56.350Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PxDSD7sPJ3rkWnCEsKzqg9`</summary>

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
  "parentUuid": "d8a04a0a-9712-48da-838e-72247eee9561",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDec8xJibZT6aQwqtLwv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d0d05c9-f8cf-49e9-aced-58384b42880e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrWjBNTKyfCxbBTzN891fC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16631,
      "cache_read_input_tokens": 0,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16631
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 137,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16631,
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

_source line 5 · 2026-05-20T10:17:56.355Z_

<details><summary>↩ Tool result · `toolu_01PxDSD7sPJ3rkWnCEsKzqg9`</summary>

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
  "parentUuid": "6d0d05c9-f8cf-49e9-aced-58384b42880e",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "476953f0-0fd3-47d8-b55c-2e673c8d555d",
  "sourceToolAssistantUUID": "6d0d05c9-f8cf-49e9-aced-58384b42880e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-20T10:17:58.970Z_



Let me read the paper and supporting materials to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "476953f0-0fd3-47d8-b55c-2e673c8d555d",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDecVxrHDb2mNa7Bi8yw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc820b83-a27e-4a2f-b112-c6b9ae951b7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGXgaMjddDRxx92o9DBZWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 16631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1459,
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

_source line 7 · 2026-05-20T10:18:00.058Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview · `toolu_013DCc5YFibtTx6QWujY1jxU`</summary>

```json
{
  "project": "irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc820b83-a27e-4a2f-b112-c6b9ae951b7a",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDecVxrHDb2mNa7Bi8yw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ab8e978-8e6c-405e-9e85-cbf7a937015f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGXgaMjddDRxx92o9DBZWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 16631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1459,
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

_source line 8 · 2026-05-20T10:18:00.112Z_

<details><summary>↩ Tool result · `toolu_013DCc5YFibtTx6QWujY1jxU`</summary>

```text
{"result":"# 项目 irt_personfit_contam 概况\n\n## 实验状态 (8 个)\n\n- **exp-item-alignment-check**: PREPARING — \n- **exp-empirical-null**: DONE (negative) — \n- **exp-leaderboard-data-recon**: DONE (success) — \n- **exp-power-theory**: PREPARING — \n- **exp-extended-sim**: DONE (success) — \n- **exp-two-sided**: DONE (negative) — \n- **phase_b_personfit**: DONE (success) — \n- **sim_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exp-item-alignment-check（准备中）\n- exp-power-theory: Detection power of lz* follows an analytic function of n_items and contamination level derivable from Snijders (2001) variance formula, and this theoretical curve explains the empirically observed inverted-U shape and n_items dependence with R²>0.95 against simulation data（准备中）\n\n## 近期结论\n- **exp-empirical-null** (negative): Bootstrap empirical null of lz* under 4PL model shows systematic positive bias (mean>>0) and inflated variance (std>>1) for real LLM response data, quantifying the degree to which LLMs violate IRT local independence/unidimensionality assumptions — this bias explains why 95% of cells are flagged with absolute thresholds ← 基于 exp-two-sided\n  [Empirical Null Q-Q Plots](/api/workspace-files/projects/irt_personfit_contam/artifacts/exp-empirical-null/chart/qq_plots_by_benchmark.png) | [Empirical Null Distributions](/api/workspace-files/projects/irt_personfit_contam/artifacts/exp-empirical-null/chart/null_distributions.png) | [KS Test Results](/api/workspace-files/projects/irt_personfit_contam/artifacts/exp-empirical-null/data/ks_test_results.csv) | [Null Bias Table](/api/workspace-files/projects/irt_personfit_contam/artifacts/exp-empirical-null/data/null_bias_table.csv) | [Unflagged Cells Analysis](/api/workspace-files/projects/irt_personfit_contam/artifacts/exp-empirical-null/report/unflagged_analysis.md) | [Empirical Null Summary](/api/workspace-files/projects/irt_personfit_contam/artifacts/exp-empirical-null/data/empirical_null_summary.json)\n- **exp-leaderboard-data-recon** (success): Open LLM Leaderboard v1 results repo on HuggingFace contains per-item binary response logs (not just aggregate scores) for a substantial number of models, enabling large-scale person-fit analysis without running inference ourselves\n  [Leaderboard Data Recon Report](/api/workspace-files/projects/irt_personfit_contam/artifacts/exp-leaderboard-data-recon/report/report.md)\n- **exp-extended-sim** (success): Extended simulation with finer contamination levels (60/75/90%) and fixed 100% NaN handling will reveal the precise dual-regime crossover point where lz* flips from negative (aberrant) to positive (over-consistent), and inverted-U power curve shape is confirmed across all benchmarks ← 基于 sim_001\n\n## 趋势\n成功 3 / 负向 3 / 失败 0 / 共 6\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nbjb2-36806: 无 GPU 信息\n\n## 告警\n（无）"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ab8e978-8e6c-405e-9e85-cbf7a937015f",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "96530b68-d616-46c6-bcc8-498e9c13dd68",
  "sourceToolAssistantUUID": "5ab8e978-8e6c-405e-9e85-cbf7a937015f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T10:18:00.865Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FaR7GSdahs9Sh3gZHgpzB6`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96530b68-d616-46c6-bcc8-498e9c13dd68",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDecVxrHDb2mNa7Bi8yw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "14bf9e7f-1d5f-41ce-ba75-958352a07d04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGXgaMjddDRxx92o9DBZWr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 16631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1459,
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

_source line 10 · 2026-05-20T10:18:00.901Z_

<details><summary>↩ Tool result · `toolu_01FaR7GSdahs9Sh3gZHgpzB6`</summary>

```text
artifacts/dream_reports/dream_20260520T082549/best/paper.tex
artifacts/dream_reports/dream_20260520T082549/median/paper.tex
artifacts/dream_reports/dream_20260520T082549/worst/paper.tex
artifacts/dream_reports/dream_20260520T092614/best/paper.tex
artifacts/dream_reports/dream_20260520T092614/median/paper.tex
artifacts/dream_reports/dream_20260520T092614/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14bf9e7f-1d5f-41ce-ba75-958352a07d04",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "6c13f847-15d0-4289-b5bc-02880ab04d16",
  "sourceToolAssistantUUID": "14bf9e7f-1d5f-41ce-ba75-958352a07d04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T10:18:01.463Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01XanpkcygEYpcfX7chPnCXf`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c13f847-15d0-4289-b5bc-02880ab04d16",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDecVxrHDb2mNa7Bi8yw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9b73f56f-314b-45fa-8a7d-70ad5e62fb31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EGXgaMjddDRxx92o9DBZWr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1459,
      "cache_read_input_tokens": 16631,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1459
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 260,
          "cache_read_input_tokens": 16631,
          "cache_creation_input_tokens": 1459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1459,
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

_source line 12 · 2026-05-20T10:18:01.519Z_

<details><summary>↩ Tool result · `toolu_01XanpkcygEYpcfX7chPnCXf`</summary>

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
  "parentUuid": "9b73f56f-314b-45fa-8a7d-70ad5e62fb31",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "9e7ebe52-4bda-4047-a588-5e69f33d6519",
  "sourceToolAssistantUUID": "9b73f56f-314b-45fa-8a7d-70ad5e62fb31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T10:18:06.793Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QVB1GsRzizLPpBxhh2XoNA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e7ebe52-4bda-4047-a588-5e69f33d6519",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDecsSRmRfx3J8d2kK6u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb9c0bc7-6243-4543-90b6-d9390e0744c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1TWkVgRCcCQr2X41YWMJR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4121,
      "cache_read_input_tokens": 18090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4121,
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

_source line 14 · 2026-05-20T10:18:06.801Z_

<details><summary>↩ Tool result · `toolu_01QVB1GsRzizLPpBxhh2XoNA`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{xcolor}
9	\usepackage{hyperref}
10	\usepackage[margin=2.5cm]{geometry}
11	\usepackage{natbib}
12	\usepackage{tabularx}
13	\usepackage{array}
14	
15	\title{IRT-FIT: Detecting Benchmark Contamination in Large Language Models\\via Person-Fit Statistics at the Minimal-Information Operating Point}
16	
17	\author{Anonymous}
18	\date{}
19	
20	\begin{document}
21	\maketitle
22	
23	% ============================================================
24	% ABSTRACT
25	% ============================================================
26	\begin{abstract}
27	Benchmark contamination threatens the reliability of Large Language Model (LLM) evaluation, yet all existing detection methods require privileged access beyond binary response patterns---token probabilities, rephrased test items, or training data.
28	We introduce \textbf{IRT-FIT}, a framework that repurposes Item Response Theory (IRT) person-fit statistics to detect contamination at the \emph{minimal-information operating point}, requiring only binary (correct/incorrect) response logs.
29	Through simulation, controlled contamination experiments on two models (Qwen3.5-9B and Gemma-4-31B), and analytical derivation, we establish three results:
30	(1)~on benchmarks with $\geq$10K items, IRT-FIT achieves AUROC~$>$~0.9 at 15\% contamination using only binary responses, narrowing the gap to gray-box methods (ConStat, Min-K\%++) to $<$5 percentage points;
31	(2)~detection power follows a predictable inverted-U curve across contamination levels with a theoretically derivable nadir, and scales as a closed-form function of benchmark size;
32	(3)~a leaderboard-wide audit of 1{,}847 Open LLM Leaderboard models reveals that ${\sim}$12\% exhibit contamination-consistent misfit, with flagging rates rising from 6\% in 2023\,H2 to 18\% in 2024\,H1 ($p{=}0.003$).
33	IRT-FIT is the only method capable of retrospective auditing on archived evaluation data, enabling ecosystem-scale contamination surveillance that is infeasible with existing approaches.
34	\end{abstract}
35	
36	% ============================================================
37	% 1  INTRODUCTION
38	% ============================================================
39	\section{Introduction}
40	
41	As LLM benchmarks proliferate and training corpora expand, the risk that models are trained on evaluation data---benchmark contamination---grows accordingly.
42	Contaminated scores inflate perceived capability, mislead downstream adoption decisions, and erode trust in community leaderboards.
43	The problem is compounded by the opacity of training pipelines: most frontier models disclose neither data composition nor contamination auditing procedures.
44	
45	Existing detection methods span five families: time-based partition analysis, membership inference attacks (Min-K\%++; \citealt{shi2024detecting}), probing-based detection (Time Travel; \citealt{oren2024proving}), performance-consistency testing (ConStat; \citealt{li2024constat}), and in-context learning effects (CoDeC; \citealt{wu2026codec}).
46	All require \emph{more} than binary response patterns: token-level probabilities, rephrased test items, model weights, or specially crafted prompts.
47	Moreover, \citet{wang2025mia} demonstrate that MIA-based methods fail under post-reinforcement-learning (RL) contamination, highlighting fragility tied to token-level signals.
48	Critically, \textbf{no existing method operates at the minimal-information level}---binary correct/incorrect outcomes---which is the only signal universally available in archived evaluation logs.
49	
50	A contaminated LLM is functionally analogous to an examinee with item preknowledge, a scenario studied for decades in psychometrics under the rubric of \emph{person-fit} analysis.
51	IRT person-fit statistics such as $l_z^*$ \citep{snijders2001} quantify whether an individual's response pattern is consistent with the estimated ability level: aberrant patterns (e.g., answering difficult items correctly while missing easy ones) yield extreme $l_z^*$ values.
52	Despite this conceptual alignment, no prior work has connected IRT person-fit to LLM contamination detection.
53	
54	We introduce \textbf{IRT-FIT}, a framework that establishes the \emph{minimal-information operating point} on the contamination detection frontier.
55	Our approach fits a 4-parameter logistic (4PL) IRT model to binary response matrices across many LLMs, computes standardized person-fit statistics ($l_z^*$), and detects contamination through the misfit delta ($\Delta l_z^*$) between clean and contaminated conditions.
56	
57	\paragraph{Contributions.}
58	\begin{enumerate}
59	\item We demonstrate that IRT person-fit statistics provide effective contamination detection using only binary responses, achieving AUROC~$>$~0.9 at 15\% contamination on large benchmarks ($\geq$10K items), within 3--5 percentage points of methods requiring richer information.
60	\item We characterize detection power as a closed-form function of benchmark size and contamination level, derive the inverted-U power curve analytically, and provide minimum benchmark-size thresholds for target power levels.
61	\item We conduct the first leaderboard-scale contamination audit (1{,}847 models, 6 benchmarks), revealing ecosystem-level contamination trends and identifying model families with systematically elevated misfit.
62	\end{enumerate}
63	
64	% ============================================================
65	% 2  RELATED WORK
66	% ============================================================
67	\section{Related Work}
68	
69	\paragraph{Contamination detection.}
70	\citet{shi2024detecting} introduce Min-K\%++, a membership inference approach using token-level log-probabilities.
71	\citet{oren2024proving} propose Time Travel, probing models with temporally shifted variants of test items.
72	\citet{li2024constat} develop ConStat, comparing performance on original vs.\ rephrased items.
73	\citet{wu2026codec} leverage in-context learning dynamics via CoDeC.
74	All require access beyond binary responses.
75	\citet{wang2025mia} show that post-RL training erases the token-probability signals that MIA methods rely on.
76	Our work is complementary: IRT-FIT occupies the minimal-information end of the detection frontier, trading modest accuracy for universal applicability.
77	
78	\paragraph{IRT for LLMs.}
79	PSN-IRT \citep{polo2024psnirt} calibrates 4PL item parameters from LLM response matrices and demonstrates that IRT-based scoring improves benchmark reliability.
80	\citet{zhuang2024irtllm} show that IRT-derived ability estimates are more robust to item sampling than raw accuracy.
81	Neither addresses contamination.
82	Our work builds on PSN-IRT's item calibration infrastructure and extends it to person-fit analysis.
83	
84	\paragraph{Person-fit statistics.}
85	The $l_z$ statistic \citep{drasgow1985} and its standardized variant $l_z^*$ \citep{snijders2001} are the workhorse tools for detecting aberrant response patterns in educational testing.
86	Applications include detecting cheating, item preknowledge, and random responding.
87	We adapt this framework to LLM evaluation, addressing the unique challenge of universal model misfit.
88	
89	% ============================================================
90	% 3  BACKGROUND
91	% ============================================================
92	\section{IRT and Person-Fit Background}
93	
94	\paragraph{4PL IRT model.}
95	Given a response matrix $\mathbf{U} \in \{0,1\}^{N \times J}$ with $N$ respondents (LLMs) and $J$ items, the 4PL model specifies:
96	\begin{equation}
97	P(U_{ij}=1 \mid \theta_i) = c_j + (d_j - c_j) \cdot \frac{1}{1 + e^{-a_j(\theta_i - b_j)}}
98	\end{equation}
99	where $\theta_i$ is the ability of respondent $i$; $a_j$, $b_j$, $c_j$, $d_j$ are the discrimination, difficulty, guessing, and upper-asymptote parameters of item $j$.
100	
101	\paragraph{Person-fit statistic $l_z^*$.}
102	The log-likelihood of respondent $i$'s pattern is $l_i = \sum_j [u_{ij} \log P_{ij} + (1{-}u_{ij})\log(1{-}P_{ij})]$, where $P_{ij} = P(U_{ij}{=}1\mid\theta_i)$.
103	The standardized person-fit statistic is:
104	\begin{equation}
105	l_z^* = \frac{l_i - E[l_i]}{\sqrt{\text{Var}(l_i)}}
106	\end{equation}
107	Under a well-fitting model, $l_z^* \sim \mathcal{N}(0,1)$.
108	Negative values ($l_z^* \ll 0$) indicate aberrant patterns (unexpected correct responses on hard items); positive values ($l_z^* \gg 0$) indicate over-consistent patterns.
109	
110	\paragraph{Contamination signatures.}
111	Benchmark contamination introduces item preknowledge: the model answers contaminated items correctly regardless of their difficulty, creating a mismatch between observed and expected response patterns.
112	At \emph{low-to-moderate} contamination ($\lesssim$50\%), the aberrant correct responses produce $l_z^* \ll 0$.
113	At \emph{high} contamination ($\gtrsim$75\%), nearly all items are answered correctly, pushing the MLE ability estimate $\hat{\theta}$ upward; the resulting pattern appears over-consistent ($l_z^* \gg 0$).
114	This creates an \emph{inverted-U} in detection power when using one-sided tests, which we resolve with two-sided testing.
115	
116	% ============================================================
117	% 4  IRT-FIT FRAMEWORK
118	% ============================================================
119	\section{IRT-FIT Framework}
120	
121	\subsection{Pipeline}
122	
123	Given binary response logs from multiple LLMs on a benchmark:
124	\textbf{(1)}~Fit a 4PL IRT model to the response matrix using PSN-IRT calibration, obtaining item parameters $(a_j, b_j, c_j, d_j)$ for each item.
125	\textbf{(2)}~Estimate each model's ability $\hat{\theta}_i$ via maximum likelihood.
126	\textbf{(3)}~Compute $l_z^*$ for each model.
127	\textbf{(4)}~Flag models with $|l_z^*|$ exceeding a calibrated threshold, or compare $\Delta l_z^* = l_{z,\text{test}}^* - l_{z,\text{clean}}^*$ against the clean baseline distribution.
128	
129	\subsection{Calibration Gap and $\Delta l_z^*$}
130	
131	Real LLM responses violate IRT's local independence assumption: knowledge is clustered by domain, items within a topic are correlated, and response strategies vary across question types.
132	This produces universal positive misfit ($l_z^* \gg 0$) even in clean models---e.g., clean Qwen3.5-9B has $l_z^* = +18.3$ on MMLU.
133	Absolute thresholds therefore flag nearly all models indiscriminately.
134	
135	We resolve this via \emph{relative detection}: the contamination-induced misfit delta $\Delta l_z^*$ between clean and contaminated conditions.
136	This approach requires either (a)~a controlled experiment establishing clean baselines, or (b)~a large population of models providing an empirical baseline distribution (as in our leaderboard audit).
137	
138	\subsection{Analytical Power Theory}
139	\label{sec:power-theory}
140	
141	Building on the variance formula from \citet{snijders2001}, we derive the detection power as a function of benchmark size $n$ and contamination fraction $\pi$:
142	\begin{equation}
143	P(\text{detect}) = \Phi\!\left(-z_\alpha + \frac{\delta \sqrt{n}}{\sigma_{l_z^*}}\right)
144	\end{equation}
145	where $\delta = E[l_{z,\text{contam}}^* - l_{z,\text{clean}}^*]/n$ is the per-item effect size and $\sigma_{l_z^*}$ is derived from the Snijders variance formula.
146	
147	The inverted-U emerges analytically: as $\pi$ increases, the MLE $\hat{\theta}$ rises, and the expected log-likelihood crosses zero at a nadir contamination fraction:
148	\begin{equation}
149	\pi^* \approx \frac{\theta_{\text{true}} - \theta_{\text{low}}}{\theta_{\text{high}} - \theta_{\text{low}}}
150	\end{equation}
151	At $\pi^*$, $|E[l_z^*]|$ is minimized, producing minimal detection power.
152	Two-sided testing ($|l_z^*| > z_{\alpha/2}$) mitigates this by capturing both negative (aberrant) and positive (over-consistent) signals.
153	
154	% ============================================================
155	% 5  EXPERIMENTS
156	% ============================================================
157	\section{Experiments}
158	
159	\subsection{Simulation Study}
160	\label{sec:simulation}
161	
162	We simulate binary response matrices under the 4PL model across five benchmarks (MMLU, HellaSwag, GSM8K, ARC-C, HumanEval), injecting contamination at levels from 5\% to 100\%.
163	Contaminated items are set to $P(\text{correct})=1$ regardless of ability.
164	For each condition, 1{,}000 replications are run.
165	
166	\paragraph{Results.}
167	Table~\ref{tab:sim-power} reports two-sided detection power ($|l_z^*| > 1.96$, $\alpha=0.05$).
168	On MMLU (14{,}042 items), power reaches 0.979 at 15\% contamination and remains above 0.85 at all levels except the inverted-U nadir.
169	The nadir occurs at $\sim$72\% contamination for MMLU (power\,=\,0.50) and $\sim$68\% for HellaSwag (power\,=\,0.38), consistent with the analytical prediction.
170	
171	Detection power scales with benchmark size: MMLU (14K) achieves 0.979 at 15\%, HellaSwag (10K) achieves 0.733, GSM8K (1.3K) achieves 0.578, and ARC-C (1.2K) only 0.129.
172	HumanEval (164 items) yields power\,$\leq$\,0.31 across all conditions, establishing a clear lower bound on benchmark size for feasible detection.
173	
174	\begin{table}[t]
175	\centering
176	\small
177	\caption{Two-sided detection power across contamination levels (simulation, $\alpha{=}0.05$).}
178	\label{tab:sim-power}
179	\begin{tabular}{lrcccccccc}
180	\toprule
181	\textbf{Benchmark} & $n$ & \textbf{5\%} & \textbf{15\%} & \textbf{25\%} & \textbf{50\%} & \textbf{60\%} & \textbf{75\%} & \textbf{90\%} & \textbf{100\%} \\
182	\midrule
183	MMLU & 14042 & .42 & .979 & .998 & .89 & .54 & .50 & .85 & .97 \\
184	HellaSwag & 10042 & .28 & .733 & .94 & .62 & .35 & .38 & .71 & .89 \\
185	GSM8K & 1319 & .10 & .578 & .72 & .41 & .22 & .18 & .52 & .68 \\
186	ARC-C & 1172 & .04 & .129 & .28 & .09 & .05 & .04 & .11 & .22 \\
187	HumanEval & 164 & .02 & .243 & .31 & .08 & .04 & .03 & .06 & .09 \\
188	\bottomrule
189	\end{tabular}
190	\end{table}
191	
192	\paragraph{Inverted-U mechanism.}
193	At low contamination, correct responses on hard items conflict with estimated ability, producing $l_z^* \ll 0$ (aberrant misfit).
194	As contamination increases past $\sim$60\%, the MLE $\hat{\theta}$ is driven upward by near-universal correct responding, and $l_z^*$ crosses zero into the positive regime.
195	In the transition zone ($\sim$60--75\%), $|l_z^*|$ is minimized, creating a detection power dip.
196	At extreme contamination ($\geq$90\%), over-consistency ($l_z^* \gg 0$) provides strong signal again.
197	Table~\ref{tab:lz-decomposition} (Appendix~\ref{app:decomposition}) decomposes negative vs.\ positive $l_z^*$ contributions on MMLU, confirming the dual-regime structure.
198	
199	\paragraph{Theory--simulation agreement.}
200	Table~\ref{tab:theory-vs-empirical} compares analytical power predictions with simulation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb9c0bc7-6243-4543-90b6-d9390e0744c9",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "f0a7dae2-4a19-438a-bb97-623c24c8d895",
  "sourceToolAssistantUUID": "bb9c0bc7-6243-4543-90b6-d9390e0744c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T10:18:07.213Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012aEcGaie1QSFK6fVq5C3if`</summary>

```json
{
  "pattern": "artifacts/dream_reports/dream_20260520T092614/**/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0a7dae2-4a19-438a-bb97-623c24c8d895",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDecsSRmRfx3J8d2kK6u",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91bd77b0-a364-4d5f-84b1-ca3efbc40b7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C1TWkVgRCcCQr2X41YWMJR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4121,
      "cache_read_input_tokens": 18090,
      "output_tokens": 220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4121
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 220,
          "cache_read_input_tokens": 18090,
          "cache_creation_input_tokens": 4121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4121,
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

_source line 16 · 2026-05-20T10:18:07.251Z_

<details><summary>↩ Tool result · `toolu_012aEcGaie1QSFK6fVq5C3if`</summary>

```text
artifacts/dream_reports/dream_20260520T092614/logs/orchestrator.log
artifacts/dream_reports/dream_20260520T092614/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260520T092614/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260520T092614/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260520T092614/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260520T092614/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T092614/best/experiment_data.json
artifacts/dream_reports/dream_20260520T092614/best/paper_framing.md
artifacts/dream_reports/dream_20260520T092614/best/paper.tex
artifacts/dream_reports/dream_20260520T092614/best/paper.aux
artifacts/dream_reports/dream_20260520T092614/best/paper.out
artifacts/dream_reports/dream_20260520T092614/best/paper.pdf
artifacts/dream_reports/dream_20260520T092614/best/paper.log
artifacts/dream_reports/dream_20260520T092614/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260520T092614/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T092614/median/experiment_data.json
artifacts/dream_reports/dream_20260520T092614/median/paper_framing.md
artifacts/dream_reports/dream_20260520T092614/median/paper.tex
artifacts/dream_reports/dream_20260520T092614/median/paper.aux
artifacts/dream_reports/dream_20260520T092614/median/paper.out
artifacts/dream_reports/dream_20260520T092614/median/paper.pdf
artifacts/dream_reports/dream_20260520T092614/median/paper.log
artifacts/dream_reports/dream_20260520T092614/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260520T092614/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T092614/worst/experiment_data.json
artifacts/dream_reports/dream_20260520T092614/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T092614/worst/paper.tex
artifacts/dream_reports/dream_20260520T092614/worst/paper.aux
artifacts/dream_reports/dream_20260520T092614/worst/paper.out
artifacts/dream_reports/dream_20260520T092614/worst/paper.pdf
artifacts/dream_reports/dream_20260520T092614/worst/paper.log
artifacts/dream_reports/dream_20260520T092614/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260520T092614/best/review_context.yaml
artifacts/dream_reports/dream_20260520T092614/best/review_report.md
artifacts/dream_reports/dream_20260520T092614/logs/review_best.log
artifacts/dream_reports/dream_20260520T092614/median/review_context.yaml
artifacts/dream_reports/dream_20260520T092614/median/review_report.md
artifacts/dream_reports/dream_20260520T092614/logs/review_median.log
artifacts/dream_reports/dream_20260520T092614/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T092614/logs/review_worst.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91bd77b0-a364-4d5f-84b1-ca3efbc40b7a",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "3aa2aa6d-77c0-475e-8c35-d66c3df59cb1",
  "sourceToolAssistantUUID": "91bd77b0-a364-4d5f-84b1-ca3efbc40b7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-20T10:18:10.324Z_

Let me continue reading the full paper and review the supporting materials.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3aa2aa6d-77c0-475e-8c35-d66c3df59cb1",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDedJ235ixLDavM8fJ8i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1dab6c8c-7207-4e88-85d5-f66e7852d1ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjvDfgvUkzV41qWdMcK9tL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5991,
      "cache_read_input_tokens": 22211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5991,
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

_source line 18 · 2026-05-20T10:18:12.205Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LaxMgMN6XEybMbS6U3s958`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/best/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dab6c8c-7207-4e88-85d5-f66e7852d1ab",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDedJ235ixLDavM8fJ8i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b15b0c99-18ad-44a2-b059-ef73fc8d55ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjvDfgvUkzV41qWdMcK9tL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5991,
      "cache_read_input_tokens": 22211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5991,
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

_source line 19 · 2026-05-20T10:18:12.211Z_

<details><summary>↩ Tool result · `toolu_01LaxMgMN6XEybMbS6U3s958`</summary>

```text
200	Table~\ref{tab:theory-vs-empirical} compares analytical power predictions with simulation.
201	Across all benchmarks, $R^2 \geq 0.91$, confirming that the closed-form expression captures the essential behavior.
202	The minimum benchmark sizes for 80\% power at 15\% contamination is $n \geq 4{,}200$; at 5\% contamination, $n \geq 11{,}800$ (Appendix~\ref{app:min-n}).
203	
204	\begin{table}[t]
205	\centering
206	\small
207	\caption{Theoretical vs.\ empirical detection power at 15\% contamination.}
208	\label{tab:theory-vs-empirical}
209	\begin{tabular}{lrcccr}
210	\toprule
211	\textbf{Benchmark} & $n$ & \textbf{Theory} & \textbf{Simulation} & \textbf{Ctrl-Exp} & $R^2$ \\
212	\midrule
213	MMLU & 14042 & .973 & .979 & .94 & .96 \\
214	HellaSwag & 10042 & .748 & .733 & .91 & .94 \\
215	BBH & 6511 & .85 & .87 & .89 & --- \\
216	MATH & 5000 & .80 & .82 & .85 & --- \\
217	GSM8K & 1319 & .561 & .578 & .82 & .92 \\
218	ARC-C & 1172 & .138 & .129 & .74 & .91 \\
219	HumanEval & 164 & .225 & .243 & .63 & .90 \\
220	\bottomrule
221	\end{tabular}
222	\end{table}
223	
224	\subsection{Controlled Contamination Experiment}
225	\label{sec:ctrl-contam}
226	
227	To bridge the calibration gap between simulation and real LLMs, we conduct controlled contamination experiments with ground-truth labels.
228	
229	\paragraph{Setup.}
230	We fine-tune two base models---Qwen3.5-9B and Gemma-4-31B---on known subsets of benchmark items via QLoRA SFT (rank 16, $\alpha$=32, lr=2e-4, 3 epochs).
231	Six contamination levels are tested: 0\% (clean), 5\%, 10\%, 15\%, 25\%, 50\%.
232	Five benchmarks are evaluated: MMLU, HellaSwag, GSM8K, ARC-C, and HumanEval.
233	At 15\% on MMLU, this corresponds to 2{,}106 training samples per run.
234	
235	\paragraph{Results.}
236	Tables~\ref{tab:dose-qwen} and \ref{tab:dose-gemma} show the full dose-response curves.
237	The key findings:
238	
239	\emph{Strong detection on large benchmarks.}
240	At 15\% contamination on MMLU, Qwen3.5-9B shows $\Delta l_z^* = -27.0$ (Cohen's $d = 2.8$, AUROC = 0.94) and Gemma-4-31B shows $\Delta l_z^* = -27.8$ ($d = 2.5$, AUROC = 0.92).
241	The mean AUROC across models is 0.93 at 15\%.
242	
243	\emph{Strict monotonicity.}
244	$l_z^*$ decreases monotonically with contamination level in the 0--50\% range ($R^2 > 0.96$ for both models on MMLU), consistent with the aberrant-misfit regime below the inverted-U nadir.
245	
246	\emph{Cross-model consistency.}
247	The Spearman correlation of $\Delta l_z^*$ between the two models is 0.94 on MMLU and 0.89 on HellaSwag, confirming that the signal is not model-specific.
248	
249	\emph{Benchmark size dependence.}
250	AUROC at 15\% ranges from 0.94 (MMLU, 14K) to 0.63 (HumanEval, 164), consistent with the power-theoretic prediction that $n_{\text{items}}$ is the dominant factor.
251	
252	\begin{table}[t]
253	\centering
254	\small
255	\caption{Dose-response: $l_z^*$ across contamination levels (Qwen3.5-9B).}
256	\label{tab:dose-qwen}
257	\begin{tabular}{lrcccccccr}
258	\toprule
259	\textbf{BM} & $n$ & \textbf{0\%} & \textbf{5\%} & \textbf{10\%} & \textbf{15\%} & \textbf{25\%} & \textbf{50\%} & $d$\textbf{@15} & \textbf{AUC@15} \\
260	\midrule
261	MMLU & 14042 & 18.3 & 8.1 & $-$2.4 & $-$8.7 & $-$22.5 & $-$42.1 & 2.8 & .94 \\
262	HSwag & 10042 & 14.7 & 6.2 & $-$0.8 & $-$4.2 & $-$14.1 & $-$28.6 & 2.2 & .91 \\
263	GSM8K & 1319 & 6.8 & 4.1 & 1.9 & 0.3 & $-$4.8 & $-$12.3 & 1.4 & .82 \\
264	ARC-C & 1172 & 5.2 & 3.8 & 2.1 & 1.0 & $-$2.7 & $-$8.9 & 1.1 & .74 \\
265	HEval & 164 & 1.8 & 1.4 & 0.8 & 0.2 & $-$1.1 & $-$3.2 & 0.6 & .63 \\
266	\bottomrule
267	\end{tabular}
268	\end{table}
269	
270	\begin{table}[t]
271	\centering
272	\small
273	\caption{Dose-response: $l_z^*$ across contamination levels (Gemma-4-31B).}
274	\label{tab:dose-gemma}
275	\begin{tabular}{lrcccccccr}
276	\toprule
277	\textbf{BM} & $n$ & \textbf{0\%} & \textbf{5\%} & \textbf{10\%} & \textbf{15\%} & \textbf{25\%} & \textbf{50\%} & $d$\textbf{@15} & \textbf{AUC@15} \\
278	\midrule
279	MMLU & 14042 & 22.6 & 11.4 & 1.8 & $-$5.2 & $-$18.7 & $-$35.8 & 2.5 & .92 \\
280	HSwag & 10042 & 17.1 & 8.9 & 1.2 & $-$3.1 & $-$11.8 & $-$24.2 & 2.0 & .90 \\
281	GSM8K & 1319 & 8.4 & 5.7 & 3.2 & 1.6 & $-$3.1 & $-$10.5 & 1.2 & .79 \\
282	ARC-C & 1172 & 6.9 & 5.1 & 3.4 & 2.0 & $-$1.8 & $-$7.4 & 0.9 & .71 \\
283	HEval & 164 & 2.4 & 1.9 & 1.2 & 0.6 & $-$0.7 & $-$2.6 & 0.5 & .60 \\
284	\bottomrule
285	\end{tabular}
286	\end{table}
287	
288	\paragraph{SFT generalization analysis.}
289	A key concern is whether SFT generalization---performance improvement on non-contaminated items---might mask the contamination signal.
290	On Qwen3.5-9B at 15\% MMLU contamination, accuracy on contaminated items jumps from 0.52 to 0.97 ($+$0.45), while non-contaminated items improve only from 0.74 to 0.76 ($+$0.02), yielding a generalization ratio of 4.4\%.
291	The SFT injection is highly item-specific.
292	
293	\subsection{Post-RL Robustness}
294	\label{sec:post-rl}
295	
296	Modern LLMs undergo RL fine-tuning (RLHF, GRPO, DPO) after SFT, which reshapes the output distribution.
297	\citet{wang2025mia} show this degrades MIA-based detection.
298	We test IRT-FIT's robustness by applying GRPO training (2{,}000 steps, lr=1e-5, rule-based reward) to the 15\%-contaminated Qwen3.5-9B model.
299	
300	\begin{table}[t]
301	\centering
302	\small
303	\caption{Post-RL detection robustness (Qwen3.5-9B, 15\% MMLU).}
304	\label{tab:post-rl}
305	\begin{tabular}{llccc}
306	\toprule
307	\textbf{Method} & \textbf{Info Required} & \textbf{AUC (SFT)} & \textbf{AUC (SFT+RL)} & \textbf{Retention} \\
308	\midrule
309	IRT-FIT (ours) & Binary responses & .94 & .88 & 94\% \\
310	Min-K\%++ & Token log-probs & .96 & .61 & 64\% \\
311	ConStat & Rephrased test & .97 & .93 & 96\% \\
312	\bottomrule
313	\end{tabular}
314	\end{table}
315	
316	Results (Table~\ref{tab:post-rl}): IRT-FIT retains 94\% of its AUROC after RL (0.94\,$\to$\,0.88), while Min-K\%++ drops to 0.61 (64\% retention).
317	The post-RL $l_z^*$ shifts from $-$8.7 to $-$5.1 (58\% signal retention), but $\Delta l_z^*$ vs.\ clean remains $-$23.4 ($d = 2.1$, $p < 10^{-8}$).
318	ConStat retains 96\% because it also does not depend on token-level signals; however, it requires live model access for retesting, unlike IRT-FIT.
319	The property that limits IRT-FIT's absolute power---operating on binary signals only---also insulates it from RL-induced signal erosion affecting token-level methods.
320	
321	\subsection{Baseline Method Comparison}
322	\label{sec:baselines}
323	
324	Table~\ref{tab:baselines} compares IRT-FIT against ConStat and Min-K\%++ on the controlled contamination models with ground-truth labels.
325	
326	\begin{table}[t]
327	\centering
328	\small
329	\caption{Detection method comparison (Qwen3.5-9B $\times$ MMLU, ground-truth labels).}
330	\label{tab:baselines}
331	\begin{tabular}{llccccc}
332	\toprule
333	\textbf{Method} & \textbf{Info Required} & \textbf{AUC@15\%} & \textbf{AUC@5\%} & \textbf{Type-I} & \textbf{Time} & \textbf{Archived?} \\
334	\midrule
335	IRT-FIT (ours) & Binary responses & .94 & .78 & .048 & 12s & Yes \\
336	ConStat & Rephrased test & .97 & .84 & .052 & 60min & No \\
337	Min-K\%++ & Token log-probs & .96 & .88 & .044 & 3min & No \\
338	\bottomrule
339	\end{tabular}
340	\end{table}
341	
342	At 15\% contamination on MMLU, IRT-FIT achieves AUROC\,=\,0.94, trailing ConStat (0.97) by 3 and Min-K\%++ (0.96) by 2 percentage points.
343	At 5\%, the gap widens to 6--10 percentage points---the genuine cost of minimal information.
344	The critical differentiator is applicability to archived data: IRT-FIT is the only method that works on historical evaluation logs where models may be offline and token probabilities unavailable.
345	Processing time per model is 12 seconds (IRT-FIT) vs.\ 3 minutes (Min-K\%++) vs.\ 60 minutes (ConStat).
346	
347	Table~\ref{tab:baselines-cross} (Appendix~\ref{app:baselines-cross}) extends the comparison across benchmarks, confirming that the gap grows for smaller benchmarks (ARC-C: 0.74 vs.\ 0.86) but remains practical for large ones.
348	
349	\subsection{Leaderboard-Wide Audit}
350	\label{sec:leaderboard}
351	
352	We apply IRT-FIT to 1{,}847 models from the HuggingFace Open LLM Leaderboard v1 that have complete per-item binary response logs across 6 benchmarks (MMLU, HellaSwag, ARC-C, GSM8K, Winogrande, TruthfulQA), spanning June 2023 to June 2024.
353	Flagging uses the $\Delta l_z^*$ baseline calibrated from the controlled experiment.
354	
355	\begin{table}[t]
356	\centering
357	\small
358	\caption{Leaderboard-wide contamination audit (1{,}847 models).}
359	\label{tab:leaderboard}
360	\begin{tabular}{lrccc}
361	\toprule
362	\textbf{Benchmark} & $n_{\text{models}}$ & \textbf{Flagged} & \textbf{Flagged \%} & \textbf{Mean $l_z^*$ (flagged / unflagged)} \\
363	\midrule
364	MMLU & 1847 & 259 & 14.0\% & $-$12.4~/~16.8 \\
365	HellaSwag & 1847 & 203 & 11.0\% & $-$8.7~/~13.2 \\
366	GSM8K & 1847 & 166 & 9.0\% & $-$4.5~/~6.2 \\
367	ARC-C & 1847 & 148 & 8.0\% & $-$3.1~/~4.8 \\
368	TruthfulQA & 1847 & 129 & 7.0\% & $-$3.9~/~5.1 \\
369	Winogrande & 1847 & 111 & 6.0\% & $-$2.8~/~3.4 \\
370	\midrule
371	\textbf{Overall} & & & \textbf{12.0\%} & \\
372	\bottomrule
373	\end{tabular}
374	\end{table}
375	
376	\paragraph{Key findings} (Table~\ref{tab:leaderboard}).
377	Overall, 12\% of models exhibit contamination-consistent misfit.
378	MMLU has the highest flagging rate (14\%), consistent with its prominence as the primary leaderboard metric and consequent incentive for gaming.
379	Flagged models have strongly negative mean $l_z^*$ ($-$12.4 on MMLU), while unflagged models show the expected positive misfit ($+$16.8).
380	
381	\paragraph{Temporal trend.}
382	Flagging rates rise significantly over time: 4.2\% in 2023\,Q3, 7.8\% in 2023\,Q4, 15.3\% in 2024\,Q1, and 20.1\% in 2024\,Q2 (Table~\ref{tab:temporal}).
383	The linear trend of $+$1.2 percentage points per month is significant ($p = 0.003$), consistent with the public timeline of leaderboard gaming discussions.
384	
385	\begin{table}[t]
386	\centering
387	\small
388	\caption{Temporal trend in contamination flagging rate.}
389	\label{tab:temporal}
390	\begin{tabular}{lccc}
391	\toprule
392	\textbf{Period} & $n_{\text{models}}$ & \textbf{Overall Flagged} & \textbf{MMLU Flagged} \\
393	\midrule
394	2023 Q3 & 312 & 4.2\% & 5.1\% \\
395	2023 Q4 & 487 & 7.8\% & 9.6\% \\
396	2024 Q1 & 623 & 15.3\% & 18.7\% \\
397	2024 Q2 & 425 & 20.1\% & 24.2\% \\
398	\bottomrule
399	\end{tabular}
400	\end{table}
401	
402	\paragraph{Model family analysis.}
403	Yi-derivatives show the highest flagging rate (31\% of 95 models), followed by Phind-CodeLlama variants (28\% of 42) and unofficial Mistral fine-tunes (22\% of 280).
404	Official Llama-2 models have a flagging rate of only 3\%.
405	Models flagged on $\geq$3 benchmarks (4.2\% of total) have an odds ratio of 4.2 for being flagged on additional benchmarks, supporting systematic rather than random misfit.
406	
407	\paragraph{Case study: Gemini-1.5-Pro.}
408	Gemini-1.5-Pro achieves 100\% MMLU accuracy with $\theta = 0.78$ and $l_z^* = +34.75$, placing it at the 99.8th percentile of the leaderboard distribution.
409	Only 3 of 1{,}847 models have more extreme $l_z^*$.
410	Domain-level analysis (Appendix~\ref{app:domain}) reveals uniformly high $l_z^*$ across all MMLU domains (STEM: 36.2, Humanities: 33.8, Social Sciences: 30.1, Other: 28.4; CV\,=\,0.09), consistent with uniform contamination rather than genuine domain-specific expertise.
411	
412	% ============================================================
413	% 6  DISCUSSION
414	% ============================================================
415	\section{Discussion}
416	
417	\paragraph{The detection frontier.}
418	IRT-FIT establishes the minimal-information operating point on the contamination detection frontier.
419	The 3--5 percentage point AUROC gap relative to gray-box methods (Table~\ref{tab:baselines}) is the quantified cost of requiring only binary responses.
420	This cost is justified when (a)~token probabilities are unavailable (archived data, API-only models), (b)~retesting is infeasible (offline models), or (c)~computational efficiency matters (12 seconds vs.\ 60 minutes per model for leaderboard-scale audits).
421	
422	\paragraph{When IRT-FIT fails.}
423	Detection power drops below practical thresholds ($<$0.80) for benchmarks with fewer than $\sim$4{,}200 items at 15\% contamination (Table~\ref{tab:min-n}, Appendix~\ref{app:min-n}).
424	HumanEval (164 items) and ARC-C (1{,}172 items) remain largely undetectable.
425	Very low contamination ($<$5\%) on any benchmark also falls below detection limits.
426	These are fundamental constraints of the binary-information operating point, not limitations of the specific method.
427	
428	\paragraph{The inverted-U.}
429	The inverted-U in detection power is not a limitation but a \emph{predictable physical property} of person-fit statistics under contamination.
430	Its analytical derivation (Section~\ref{sec:power-theory}) makes it anticipatable: practitioners can compute the nadir for any benchmark using the formula in Eq.~4.
431	Two-sided testing raises nadir power from near-zero to $\sim$0.50 on MMLU, and above 0.85 at all non-nadir contamination levels.
432	
433	\paragraph{Scope.}
434	IRT-FIT targets \emph{item-level memorization} (e.g., SFT on benchmark items, leaderboard gaming).
435	Pretraining-stage exposure produces smooth distributional improvement---higher $\theta$ without aberrant patterns---which is not in scope for person-fit detection.
436	This scope limitation is shared with all contamination detection methods that do not access training data.
437	
438	% ============================================================
439	% 7  CONCLUSION
440	% ============================================================
441	\section{Conclusion}
442	
443	We introduced IRT-FIT, a framework for detecting benchmark contamination in LLMs using only binary response patterns.
444	Through simulation, controlled experiments on two model families, analytical derivation, and a leaderboard-wide audit of 1{,}847 models, we showed that person-fit statistics provide effective contamination detection at the minimal-information operating point.
445	On large benchmarks ($\geq$10K items), IRT-FIT achieves AUROC~$>$~0.9 at 15\% contamination, within 3--5 percentage points of methods requiring token probabilities or retesting.
446	The leaderboard audit revealed that $\sim$12\% of Open LLM Leaderboard models exhibit contamination-consistent misfit, with rates doubling over the June 2023 -- June 2024 period.
447	IRT-FIT is the only detection method applicable to archived evaluation data, enabling retrospective contamination surveillance at ecosystem scale.
448	
449	\section*{Limitations}
450	
451	Detection power is fundamentally bounded by benchmark size: benchmarks with fewer than $\sim$4{,}200 items have $<$80\% power at 15\% contamination.
452	The controlled experiments use QLoRA SFT to simulate contamination, which may not capture all contamination pathways (e.g., pretraining exposure, continued pretraining).
453	The leaderboard audit uses relative thresholds calibrated on two model architectures; generalization to models with very different response characteristics is an open question.
454	The 4PL IRT model assumes unidimensionality, which real benchmark data violates; our $\Delta l_z^*$ approach mitigates but does not eliminate this model misspecification.
455	
456	% ============================================================
457	% REFERENCES
458	% ============================================================
459	\bibliographystyle{plainnat}
460	
461	\begin{thebibliography}{20}
462	
463	\bibitem[Drasgow et~al.(1985)]{drasgow1985}
464	Fritz Drasgow, Michael~V. Levine, and Mary~E. Williams.
465	\newblock Appropriateness measurement with polychotomous item response models and standardized indices.
466	\newblock \emph{British Journal of Mathematical and Statistical Psychology}, 38(1):67--86, 1985.
467	
468	\bibitem[Li et~al.(2024)]{li2024constat}
469	Jasper Li, Pengfei Liu, and Diyi Yang.
470	\newblock Con{S}tat: Performance-based contamination detection in large language models.
471	\newblock In \emph{Advances in Neural Information Processing Systems}, 2024.
472	
473	\bibitem[Oren et~al.(2024)]{oren2024proving}
474	Yonatan Oren, Nicole Meister, Niladri Chatterji, Faisal Ladhak, and Tatsunori~B. Hashimoto.
475	\newblock Proving test set contamination in black box language models.
476	\newblock In \emph{International Conference on Learning Representations}, 2024.
477	
478	\bibitem[Polo et~al.(2024)]{polo2024psnirt}
479	Felipe~Maia Polo, Lucas Weber, Lesi\'{n}skas Raphenya, Onkar Bhardwaj, Leshem Choshen, Allysson Flavio~Melo de~Oliveira, Yuekai Sun, and Mikhail Yurochkin.
480	\newblock t{IRT}: A next-generation framework for computational psychometrics.
481	\newblock In \emph{AAAI Conference on Artificial Intelligence}, 2024.
482	
483	\bibitem[Shi et~al.(2024)]{shi2024detecting}
484	Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.
485	\newblock Detecting pretraining data from large language models.
486	\newblock In \emph{International Conference on Learning Representations}, 2024.
487	
488	\bibitem[Snijders(2001)]{snijders2001}
489	Tom~A.B. Snijders.
490	\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.
491	\newblock \emph{Psychometrika}, 66(3):331--342, 2001.
492	
493	\bibitem[Wang et~al.(2025)]{wang2025mia}
494	Yiwen Wang, Jiayi Pan, and Diyi Yang.
495	\newblock Do membership inference attacks fail against large language models with reinforcement learning?
496	\newblock \emph{arXiv preprint arXiv:2502.xxxxx}, 2025.
497	
498	\bibitem[Wu et~al.(2026)]{wu2026codec}
499	Tongfei Wu, et~al.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b15b0c99-18ad-44a2-b059-ef73fc8d55ad",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "5bc570fe-b597-4050-81f2-a050c825b64b",
  "sourceToolAssistantUUID": "b15b0c99-18ad-44a2-b059-ef73fc8d55ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T10:18:13.160Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YDgXqV3N3y8hkApnWGrmWJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bc570fe-b597-4050-81f2-a050c825b64b",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDedJ235ixLDavM8fJ8i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "577054bf-a495-4a3f-b698-59316217815e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjvDfgvUkzV41qWdMcK9tL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5991,
      "cache_read_input_tokens": 22211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5991,
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

_source line 21 · 2026-05-20T10:18:13.391Z_

<details open><summary>🔧 Tool call — Read · `toolu_013ScP1FujYZNimGxy21Qmcd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "577054bf-a495-4a3f-b698-59316217815e",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDedJ235ixLDavM8fJ8i",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1328a895-fe26-455a-a9f2-dc0637654906",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjvDfgvUkzV41qWdMcK9tL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5991,
      "cache_read_input_tokens": 22211,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5991
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 333,
          "cache_read_input_tokens": 22211,
          "cache_creation_input_tokens": 5991,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5991,
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

_source line 22 · 2026-05-20T10:18:13.486Z_

<details><summary>↩ Tool result · `toolu_01YDgXqV3N3y8hkApnWGrmWJ`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立。Claim 1: minimal-information detection 经控制实验验证，Δlz*
2	  提供 可靠的相对检测信号，calibration gap 被 bridged。Claim 2: inverted-U 从经验升级为理论命题， dose-response
3	  曲线在两个模型上复现。Claim 3: leaderboard 大规模审计揭示生态系统级污染趋势， Gemini-1.5 case study 由控制实验的 Δlz*
4	  基线提供定量支撑。 Headline: "IRT-FIT achieves AUROC>0.9 at 15% contamination using only
5	  binary responses, and a leaderboard-wide audit reveals ~12% of models exhibit contamination-consistent
6	  misfit."
7	
8	  '
9	imagined_experiments:
10	- name: Extended Simulation — Inverted-U Full Characterization
11	  plan_id: exp-extended-sim
12	  description: '在 Phase A 模拟基础上添加 60%/75%/90%/100% contamination levels， 修复 100% contamination
13	    时 MLE boundary θ=4.0 的 lz* 计算， 精确刻画 inverted-U 拐点位置，计算 two-sided power curves。
14	
15	    '
16	  expected_results:
17	    power_negative_at_5pct_mmlu: 0.42
18	    power_negative_at_15pct_mmlu: 0.979
19	    power_negative_at_25pct_mmlu: 0.998
20	    power_negative_at_50pct_mmlu: 0.87
21	    power_negative_at_60pct_mmlu: 0.54
22	    power_negative_at_75pct_mmlu: 0.12
23	    power_negative_at_90pct_mmlu: 0.03
24	    power_negative_at_100pct_mmlu: 0.01
25	    power_positive_at_5pct_mmlu: 0.0
26	    power_positive_at_15pct_mmlu: 0.0
27	    power_positive_at_50pct_mmlu: 0.02
28	    power_positive_at_60pct_mmlu: 0.08
29	    power_positive_at_75pct_mmlu: 0.38
30	    power_positive_at_90pct_mmlu: 0.82
31	    power_positive_at_100pct_mmlu: 0.96
32	    power_twosided_at_15pct_mmlu: 0.979
33	    power_twosided_at_50pct_mmlu: 0.89
34	    power_twosided_at_75pct_mmlu: 0.5
35	    power_twosided_at_90pct_mmlu: 0.85
36	    power_twosided_at_100pct_mmlu: 0.97
37	    inverted_u_nadir_contamination_pct_mmlu: 72
38	    inverted_u_nadir_power_mmlu: 0.45
39	    inverted_u_nadir_contamination_pct_hellaswag: 68
40	    inverted_u_nadir_power_hellaswag: 0.38
41	    power_twosided_at_15pct_hellaswag: 0.733
42	    power_twosided_at_50pct_hellaswag: 0.62
43	    power_twosided_at_90pct_hellaswag: 0.71
44	    power_twosided_at_15pct_gsm8k: 0.578
45	    power_twosided_at_50pct_gsm8k: 0.41
46	    power_twosided_at_90pct_gsm8k: 0.52
47	    power_twosided_at_15pct_arc_c: 0.129
48	    power_twosided_at_50pct_arc_c: 0.09
49	    power_twosided_at_90pct_arc_c: 0.11
50	    pct_100_nan_rate_after_fix: 0.0
51	    pct_100_mean_lz_star_mmlu: 28.4
52	    pct_100_mean_theta_mmlu: 4.0
53	  result_rationale: '在 best 档下，inverted-U 拐点清晰可见且位于 ~70% contamination 附近。 机制：低污染(5-50%)时，被污染
54	    item 上的正确作答与模型能力不匹配→aberrant pattern→lz*<<0， 检测力随污染量单调上升。但超过~60%后，模型在绝大部分 item
55	    上都答对，MLE θ 被推高， lz* 从负值穿越零点转向正值——此时处于"过渡区"，|lz*| 最小，power 最低。 继续到 90-100%，over-consistency
56	    信号 (lz*>>0) 变强，双侧检测再次有效。 MMLU (14K items) 由于 n_items 最大，在所有 contamination levels
57	    上 power 最高， nadir 点也最浅。小 benchmark (ARC-C 1.2K) 全程 power 低，nadir 更深， 符合 power∝n_items
58	    的理论预测。 100% contamination 修复后 θ=4.0 (boundary)，lz*=+28.4 反映极端 over-consistency。
59	
60	    '
61	  tables:
62	  - title: 'Table 2: Two-Sided Detection Power Across Contamination Levels (Simulation)'
63	    columns:
64	    - Benchmark
65	    - n_items
66	    - 5%
67	    - 15%
68	    - 25%
69	    - 50%
70	    - 60%
71	    - 75%
72	    - 90%
73	    - 100%
74	    rows:
75	    - - MMLU
76	      - 14042
77	      - 0.42
78	      - 0.979
79	      - 0.998
80	      - 0.89
81	      - 0.54
82	      - 0.5
83	      - 0.85
84	      - 0.97
85	    - - HellaSwag
86	      - 10042
87	      - 0.28
88	      - 0.733
89	      - 0.94
90	      - 0.62
91	      - 0.35
92	      - 0.38
93	      - 0.71
94	      - 0.89
95	    - - GSM8K
96	      - 1319
97	      - 0.1
98	      - 0.578
99	      - 0.72
100	      - 0.41
101	      - 0.22
102	      - 0.18
103	      - 0.52
104	      - 0.68
105	    - - ARC-C
106	      - 1172
107	      - 0.04
108	      - 0.129
109	      - 0.28
110	      - 0.09
111	      - 0.05
112	      - 0.04
113	      - 0.11
114	      - 0.22
115	    - - HumanEval
116	      - 164
117	      - 0.02
118	      - 0.243
119	      - 0.31
120	      - 0.08
121	      - 0.04
122	      - 0.03
123	      - 0.06
124	      - 0.09
125	  - title: 'Table S1: Negative vs Positive lz* Power Decomposition (MMLU)'
126	    columns:
127	    - Contamination
128	    - P(lz*<-1.96)
129	    - P(lz*>1.96)
130	    - P(|lz*|>1.96)
131	    - Mean lz*
132	    - SD lz*
133	    rows:
134	    - - 5%
135	      - 0.42
136	      - 0.0
137	      - 0.42
138	      - -3.1
139	      - 2.8
140	    - - 15%
141	      - 0.979
142	      - 0.0
143	      - 0.979
144	      - -12.7
145	      - 4.2
146	    - - 50%
147	      - 0.87
148	      - 0.02
149	      - 0.89
150	      - -8.4
151	      - 6.1
152	    - - 75%
153	      - 0.12
154	      - 0.38
155	      - 0.5
156	      - 2.8
157	      - 9.3
158	    - - 90%
159	      - 0.03
160	      - 0.82
161	      - 0.85
162	      - 18.6
163	      - 7.5
164	    - - 100%
165	      - 0.01
166	      - 0.96
167	      - 0.97
168	      - 28.4
169	      - 5.2
170	  figures_description:
171	  - 'Figure 2: Inverted-U power curve — x-axis contamination %, y-axis two-sided power,
172	    5 benchmarks 分色，vertical dashed line at nadir (~72% for MMLU). 清晰展示 negative→positive
173	    regime transition.'
174	  - 'Figure S1: lz* distribution heatmap — x-axis contamination level, y-axis lz*
175	    value, color=density. 显示 lz* 分布从负到正的 shift。'
176	  analysis: '关键发现：(1) 双侧框架消除了 inverted-U 的 blind spot——nadir 从 power≈0 提升到 ~0.5， 但在
177	    60-75% contamination 区间仍有检测力下降。(2) 对 MMLU 这种大 benchmark， 除 nadir 外全程 power>0.85，实用性强。(3)
178	    小 benchmark 即使双侧也不够：ARC-C 峰值 仅 0.28，这支持"power 是 n_items 的函数"这一 claim。 叙事价值：inverted-U
179	    是可预测的物理现象而非 limitation，dual-regime 结构是新贡献。
180	
181	    '
182	- name: Controlled Contamination Pilot — Go/No-Go
183	  plan_id: exp-ctrl-contam-pilot
184	  description: 'Qwen3.5-9B × 3 levels (0%/15%/50%) × MMLU。QLoRA SFT 注入已知 benchmark
185	    items， 测量 Δlz*(clean→contaminated) 作为论文 go/no-go 信号。
186	
187	    '
188	  expected_results:
189	    qwen_clean_mmlu_accuracy: 0.71
190	    qwen_clean_mmlu_theta: 1.24
191	    qwen_clean_mmlu_lz_star: 18.3
192	    qwen_15pct_mmlu_accuracy: 0.78
193	    qwen_15pct_mmlu_theta: 1.62
194	    qwen_15pct_mmlu_lz_star: -8.7
195	    qwen_15pct_delta_lz_star: -27.0
196	    qwen_15pct_delta_lz_star_se: 3.2
197	    qwen_15pct_delta_lz_star_z: -8.44
198	    qwen_15pct_delta_lz_star_p: <1e-16
199	    qwen_50pct_mmlu_accuracy: 0.91
200	    qwen_50pct_mmlu_theta: 2.85
201	    qwen_50pct_mmlu_lz_star: -42.1
202	    qwen_50pct_delta_lz_star: -60.4
203	    qwen_50pct_delta_lz_star_se: 4.1
204	    qwen_50pct_delta_lz_star_z: -14.73
205	    qwen_50pct_delta_lz_star_p: <1e-48
206	    go_nogo_signal: GO
207	    cohen_d_15pct: 2.8
208	    cohen_d_50pct: 6.1
209	    accuracy_uplift_15pct: 0.07
210	    accuracy_uplift_50pct: 0.2
211	    sft_epochs: 3
212	    sft_lr: 2e-4
213	    lora_rank: 16
214	    lora_alpha: 32
215	    training_samples_15pct: 2106
216	    training_samples_50pct: 7021
217	    training_time_per_run_hrs: 2.8
218	  result_rationale: '在 best 档下，Δlz* 效应极其显著。原因：(1) MMLU 有 14K items，信噪比极高—— 即使 SFT
219	    generalization 让部分非污染 item 也受益，15% 直接污染的 2100+ items 已足以产生强 aberrant pattern。(2)
220	    Qwen3.5-9B 是中等能力模型（clean acc~0.71）， 污染后能力-表现不匹配最明显——在它本不该答对的难题上答对了。 (3) Clean
221	    baseline lz*=+18.3 (已知的 universal misfit) 在污染后急剧下降到 -8.7， 说明 SFT 注入不仅改变了 accuracy，还改变了
222	    response pattern 的结构—— 打破了原有的 over-consistency (正 lz*) 转为 aberrant (负 lz*)。 (4)
223	    50% 时效应更强 (d=6.1)，但 lz* 仍为负（未越过 inverted-U nadir）， 因为 50% 在 MMLU 14K items 上仍只是
224	    7K items， 模型在剩余 7K 上的表现仍产生 mismatch。 这个 pilot 给出明确 GO 信号。
225	
226	    '
227	  tables:
228	  - title: 'Table 3: Controlled Contamination Pilot Results (Qwen3.5-9B × MMLU)'
229	    columns:
230	    - Contamination
231	    - Accuracy
232	    - θ
233	    - lz*
234	    - Δlz*
235	    - Cohen's d
236	    - p-value
237	    rows:
238	    - - 0% (clean)
239	      - 0.71
240	      - 1.24
241	      - 18.3
242	      - —
243	      - —
244	      - —
245	    - - 15%
246	      - 0.78
247	      - 1.62
248	      - -8.7
249	      - -27.0
250	      - 2.8
251	      - <1e-16
252	    - - 50%
253	      - 0.91
254	      - 2.85
255	      - -42.1
256	      - -60.4
257	      - 6.1
258	      - <1e-48
259	  figures_description:
260	  - 'Figure 3a: Bar chart — lz* at 0%/15%/50% with bootstrap 95% CI. 清晰展示从 +18 到 -8
261	    到 -42 的单调下降。'
262	  - 'Figure 3b: MMLU item-level accuracy heatmap — rows=items sorted by difficulty,
263	    columns=0%/15%/50%. 显示污染 items 上 accuracy spike。'
264	  analysis: 'Pilot 结果明确支持 GO。Cohen''s d=2.8 at 15% 远超预设阈值 2.0。 关键洞察：clean model 已有正
265	    lz*(universal misfit)，污染后 lz* 逆转为负值， 说明 Δlz* 的信号不是从零出发而是从正值出发—— 这反而增大了效应量，因为正负逆转
266	    = 更大的 delta。 Calibration gap 被 bridge：不需要绝对 lz* 阈值，只需 Δlz* 即可区分 clean vs contaminated。
267	
268	    '
269	- name: Full Controlled Contamination Experiment
270	  plan_id: exp-ctrl-contam
271	  description: '完整控制实验：Qwen3.5-9B + Gemma-4-31B × 6 contamination levels (0%/5%/10%/15%/25%/50%)
272	    × 5 benchmarks。建立 ground-truth contamination → Δlz* 映射。
273	
274	    '
275	  expected_results:
276	    qwen_mmlu_lz_star_0pct: 18.3
277	    qwen_mmlu_lz_star_5pct: 8.1
278	    qwen_mmlu_lz_star_10pct: -2.4
279	    qwen_mmlu_lz_star_15pct: -8.7
280	    qwen_mmlu_lz_star_25pct: -22.5
281	    qwen_mmlu_lz_star_50pct: -42.1
282	    qwen_mmlu_delta_lz_star_15pct: -27.0
283	    qwen_mmlu_cohen_d_15pct: 2.8
284	    qwen_mmlu_auroc_15pct: 0.94
285	    qwen_mmlu_auroc_5pct: 0.78
286	    gemma_mmlu_lz_star_0pct: 22.6
287	    gemma_mmlu_lz_star_5pct: 11.4
288	    gemma_mmlu_lz_star_10pct: 1.8
289	    gemma_mmlu_lz_star_15pct: -5.2
290	    gemma_mmlu_lz_star_25pct: -18.7
291	    gemma_mmlu_lz_star_50pct: -35.8
292	    gemma_mmlu_delta_lz_star_15pct: -27.8
293	    gemma_mmlu_cohen_d_15pct: 2.5
294	    gemma_mmlu_auroc_15pct: 0.92
295	    gemma_mmlu_auroc_5pct: 0.76
296	    cross_model_spearman_delta_lz_mmlu: 0.94
297	    cross_model_spearman_delta_lz_hellaswag: 0.89
298	    qwen_hellaswag_lz_star_0pct: 14.7
299	    qwen_hellaswag_lz_star_15pct: -4.2
300	    qwen_hellaswag_delta_lz_star_15pct: -18.9
301	    qwen_hellaswag_cohen_d_15pct: 2.2
302	    qwen_hellaswag_auroc_15pct: 0.91
303	    qwen_gsm8k_lz_star_0pct: 6.8
304	    qwen_gsm8k_lz_star_15pct: 0.3
305	    qwen_gsm8k_delta_lz_star_15pct: -6.5
306	    qwen_gsm8k_cohen_d_15pct: 1.4
307	    qwen_gsm8k_auroc_15pct: 0.82
308	    dose_response_monotonic_qwen_mmlu: true
309	    dose_response_monotonic_gemma_mmlu: true
310	    dose_response_monotonic_qwen_hellaswag: true
311	    dose_response_r2_qwen_mmlu: 0.97
312	    dose_response_r2_gemma_mmlu: 0.96
313	    inverted_u_visible_qwen_mmlu: not yet — need 60%+ levels to see nadir
314	    inverted_u_visible_qwen_hellaswag: not yet
315	    mean_cohen_d_at_15pct_across_models_mmlu: 2.65
316	    mean_auroc_at_15pct_across_models_mmlu: 0.93
317	    mean_auroc_at_5pct_across_models_mmlu: 0.77
318	    accuracy_uplift_on_non_contaminated_items_15pct_qwen: 0.02
319	    accuracy_uplift_on_contaminated_items_15pct_qwen: 0.45
320	    generalization_ratio: 0.044
321	    cross_benchmark_spearman_ctrl_models: 0.74
322	    cross_benchmark_spearman_ctrl_p: 0.008
323	  result_rationale: 'Best 档下，两个模型在 MMLU 上都展示 Cohen''s d > 2.0 且 AUROC > 0.9 at 15%。
324	    机制解释： (1) SFT 注入的关键效应不是提升 overall accuracy（虽然也提升）， 而是创造 aberrant response pattern：模型在难题上答对（因为见过），
325	    在本应答对的简单题上偶尔答错（SFT 微调略微扰动了非目标知识）。 这种 pattern mismatch 正是 lz* 捕捉的信号。 (2) Gemma-4-31B
326	    (31B) 比 Qwen3.5-9B (9B) 能力更强，clean baseline lz* 更高 (22.6 vs 18.3)， 但污染效应略弱 (d=2.5
327	    vs 2.8)——因为更强的模型原本就能答对更多题， contamination 带来的额外"不该答对却答对"信号相对更小。 (3) GSM8K (1.3K
328	    items) 的 d=1.4 < 2.0 因为 n_items 小， 但 AUROC=0.82 仍实用——这与 simulation power curve
329	    一致。 (4) Dose-response 严格单调（在 0-50% 范围内），R²>0.96， 因为 0-50% 完全处于 negative lz* regime，远未到达
330	    inverted-U nadir。 (5) SFT generalization ratio 仅 4.4%——被污染 items 上 accuracy 提升
331	    45pp， 非污染 items 仅 2pp——说明 QLoRA SFT 注入是高度 item-specific 的， 不会 smooth out signal。这直接回应
332	    R5 审稿意见。 (6) 跨 benchmark Spearman=0.74 (p=0.008) 在控制实验中显著， 因为同一模型在多个 benchmark
333	    上受到同等比例污染， lz* shift 高度相关——与 Phase B 的 n=12 观察性数据 (p>0.05) 形成对比。
334	
335	    '
336	  tables:
337	  - title: 'Table 4: Δlz* Dose-Response (Qwen3.5-9B)'
338	    columns:
339	    - Benchmark
340	    - n_items
341	    - 0%
342	    - 5%
343	    - 10%
344	    - 15%
345	    - 25%
346	    - 50%
347	    - Cohen's d @15%
348	    - AUROC @15%
349	    rows:
350	    - - MMLU
351	      - 14042
352	      - 18.3
353	      - 8.1
354	      - -2.4
355	      - -8.7
356	      - -22.5
357	      - -42.1
358	      - 2.8
359	      - 0.94
360	    - - HellaSwag
361	      - 10042
362	      - 14.7
363	      - 6.2
364	      - -0.8
365	      - -4.2
366	      - -14.1
367	      - -28.6
368	      - 2.2
369	      - 0.91
370	    - - GSM8K
371	      - 1319
372	      - 6.8
373	      - 4.1
374	      - 1.9
375	      - 0.3
376	      - -4.8
377	      - -12.3
378	      - 1.4
379	      - 0.82
380	    - - ARC-C
381	      - 1172
382	      - 5.2
383	      - 3.8
384	      - 2.1
385	      - 1.0
386	      - -2.7
387	      - -8.9
388	      - 1.1
389	      - 0.74
390	    - - HumanEval
391	      - 164
392	      - 1.8
393	      - 1.4
394	      - 0.8
395	      - 0.2
396	      - -1.1
397	      - -3.2
398	      - 0.6
399	      - 0.63
400	  - title: 'Table 5: Δlz* Dose-Response (Gemma-4-31B)'
401	    columns:
402	    - Benchmark
403	    - n_items
404	    - 0%
405	    - 5%
406	    - 10%
407	    - 15%
408	    - 25%
409	    - 50%
410	    - Cohen's d @15%
411	    - AUROC @15%
412	    rows:
413	    - - MMLU
414	      - 14042
415	      - 22.6
416	      - 11.4
417	      - 1.8
418	      - -5.2
419	      - -18.7
420	      - -35.8
421	      - 2.5
422	      - 0.92
423	    - - HellaSwag
424	      - 10042
425	      - 17.1
426	      - 8.9
427	      - 1.2
428	      - -3.1
429	      - -11.8
430	      - -24.2
431	      - 2.0
432	      - 0.9
433	    - - GSM8K
434	      - 1319
435	      - 8.4
436	      - 5.7
437	      - 3.2
438	      - 1.6
439	      - -3.1
440	      - -10.5
441	      - 1.2
442	      - 0.79
443	    - - ARC-C
444	      - 1172
445	      - 6.9
446	      - 5.1
447	      - 3.4
448	      - 2.0
449	      - -1.8
450	      - -7.4
451	      - 0.9
452	      - 0.71
453	    - - HumanEval
454	      - 164
455	      - 2.4
456	      - 1.9
457	      - 1.2
458	      - 0.6
459	      - -0.7
460	      - -2.6
461	      - 0.5
462	      - 0.6
463	  - title: 'Table 6: SFT Generalization Analysis (Qwen3.5-9B, 15% MMLU)'
464	    columns:
465	    - Item Set
466	    - n_items
467	    - Acc (clean)
468	    - Acc (15%)
469	    - Δ Acc
470	    rows:
471	    - - Contaminated items
472	      - 2106
473	      - 0.52
474	      - 0.97
475	      - '+0.45'
476	    - - Non-contaminated items
477	      - 11936
478	      - 0.74
479	      - 0.76
480	      - '+0.02'
481	    - - Overall
482	      - 14042
483	      - 0.71
484	      - 0.78
485	      - '+0.07'
486	  figures_description:
487	  - 'Figure 4: Dose-response curves — x-axis contamination %, y-axis lz*. Two panels
488	    (Qwen / Gemma), 5 benchmarks per panel. 两个模型趋势平行，MMLU/HellaSwag 斜率最陡。'
489	  - 'Figure 5: ROC curves at 15% contamination — one curve per (model, benchmark)
490	    pair. MMLU curves 明显优于小 benchmark。AUC 标注在图例中。'
491	  - 'Figure 6: Item-level analysis — scatter plot of item difficulty vs accuracy change
492	    (clean→15%). 被污染 items 在高难度区出现 accuracy spike，non-contaminated items 变化极小。'
493	  analysis: '这是论文的核心表格。关键 takeaway： (1) MMLU 和 HellaSwag (n>10K) 上 AUROC>0.9，confirmed
494	    large benchmark 上 minimal-information detection 可行。 (2) 两个模型趋势一致，排除 model-specific
495	    artifact。 (3) n_items 是决定性因素——HumanEval (164 items) 即使在 best 档也不可用 (AUROC=0.63)，
496	    这是诚实的 scope limitation 而非 failure。 (4) Generalization ratio 4.4% 证明 SFT 注入足够 surgical，
497	    不会导致 "general capability improvement masking contamination signal" 的 confound。
498	
499	    '
500	- name: Analytical Power Theory
501	  plan_id: exp-power-theory
502	  description: '基于 Snijders (2001) lz* 方差公式推导 power 与 n_items 的解析关系。 将 inverted-U
503	    从经验观察升级为理论命题，验证理论曲线与模拟/控制实验拟合度。
504	
505	    '
506	  expected_results:
507	    theoretical_power_formula: P(detect) = Φ(−z_α + δ·√n / σ_lz) where δ = E[lz*_contam
508	      − lz*_clean]/n, σ_lz from Snijders variance
509	    inverted_u_theoretical_derivation: 'contamination fraction π ∈ [0,1] 时，E[lz*]
510	      = n·{π·f_contam(θ) + (1−π)·f_clean(θ) − f_expected(θ)}, 其中 f_contam 在高污染时驱动
511	      θ_MLE 上升，使 f_expected(θ) 接近 f_observed， 产生 lz*→0 的 identifiability collapse。拐点
512	      π* 可解析求解。
513	
514	      '
515	    inverted_u_nadir_formula: π* = argmin |E[lz*(π)]| ≈ (θ_true − θ_low)/(θ_high −
516	      θ_low) — model ability dependent
517	    theory_vs_simulation_r2_mmlu: 0.96
518	    theory_vs_simulation_r2_hellaswag: 0.94
519	    theory_vs_simulation_r2_gsm8k: 0.92
520	    theory_vs_simulation_r2_arc_c: 0.91
521	    theory_vs_ctrl_experiment_r2_mmlu: 0.93
522	    theory_vs_ctrl_experiment_r2_hellaswag: 0.9
523	    n_min_for_80pct_power_at_15pct_contam: 4200
524	    n_min_for_80pct_power_at_5pct_contam: 11800
525	    n_min_for_80pct_power_at_25pct_contam: 1900
526	  result_rationale: 'Best 档下，理论与经验高度吻合 (R²>0.9)。原因： (1) Snijders (2001) 的 lz* 方差公式在
527	    n>100 时已非常精确， 我们的 benchmark n 远超 100，所以渐近近似几乎精确。 (2) 4PL model 在 simulation 中是
528	    ground truth，理论推导基于同一模型， 所以 theory-simulation 拟合自然极高 (R²=0.96)。 (3) Theory-control_experiment
529	    拟合略低 (R²=0.93) 因为真实 SFT 注入 并非理论假设的 "item 独立翻转"——有 generalization spillover (4.4%)
530	    和 item 间的 correlation (local dependence violation)。 (4) Inverted-U 的解析拐点公式使其从"奇怪的经验现象"变为
531	    "可预测的理论必然"——审稿人可以代入自己的 benchmark 参数验证。 (5) 最低 n_items 阈值直接给出实操建议：检测 15% 污染需要 ≥4200
532	    items， 这解释了为什么 MMLU/HellaSwag 可行而 ARC-C/HumanEval 不行。
533	
534	    '
535	  tables:
536	  - title: 'Table 7: Theoretical vs Empirical Power Comparison'
537	    columns:
538	    - Benchmark
539	    - n_items
540	    - Power (theory)
541	    - Power (simulation)
542	    - Power (ctrl-exp)
543	    - Theory-Sim R²
544	    rows:
545	    - - MMLU
546	      - 14042
547	      - 0.973
548	      - 0.979
549	      - 0.94
550	      - 0.96
551	    - - HellaSwag
552	      - 10042
553	      - 0.748
554	      - 0.733
555	      - 0.91
556	      - 0.94
557	    - - GSM8K
558	      - 1319
559	      - 0.561
560	      - 0.578
561	      - 0.82
562	      - 0.92
563	    - - ARC-C
564	      - 1172
565	      - 0.138
566	      - 0.129
567	      - 0.74
568	      - 0.91
569	    - - HumanEval
570	      - 164
571	      - 0.225
572	      - 0.243
573	      - 0.63
574	      - 0.9
575	  - title: 'Table S2: Minimum n_items for Target Power (Theoretical)'
576	    columns:
577	    - Contamination %
578	    - Power=0.80
579	    - Power=0.90
580	    - Power=0.95
581	    rows:
582	    - - 5%
583	      - 11800
584	      - 15200
585	      - 18500
586	    - - 10%
587	      - 6100
588	      - 7900
589	      - 9600
590	    - - 15%
591	      - 4200
592	      - 5400
593	      - 6600
594	    - - 25%
595	      - 1900
596	      - 2500
597	      - 3000
598	    - - 50%
599	      - 800
600	      - 1000
601	      - 1200
602	  figures_description:
603	  - 'Figure 7: Power surface — 3D plot with x=n_items, y=contamination%, z=power.
604	    理论曲面 (mesh) 叠加 simulation 点 (dots) 和 ctrl-exp 点 (stars). R² annotated per benchmark.'
605	  - 'Figure 8: Inverted-U theoretical decomposition — 负向 power + 正向 power + combined
606	    power, 理论曲线 vs simulation dots. Nadir 位置 marked.'
607	  analysis: '理论贡献使论文从"IRT applied to LLMs"升级为"principled detection theory"。 审稿人可以用
608	    Table S2 直接查询任意 benchmark 的检测可行性。 R² 全部 >0.9 的关键前提是 best 档下 SFT 注入高度 item-specific
609	    (generalization ratio 低)。 如果 generalization 更强，theory-ctrl R² 会下降。
610	
611	    '
612	- name: Leaderboard Data Reconnaissance
613	  plan_id: exp-leaderboard-data-recon
614	  description: '调研 HuggingFace Open LLM Leaderboard v1 的 per-item binary response
615	    logs 可用性。
616	
617	    '
618	  expected_results:
619	    per_item_data_available: true
620	    data_source: HuggingFace open-llm-leaderboard-old/results
621	    total_models_with_results: 6842
622	    models_with_per_item_binary_logs: 2184
623	    benchmarks_with_per_item:
624	    - MMLU (14042)
625	    - HellaSwag (10042)
626	    - ARC-C (1172)
627	    - TruthfulQA (817)
628	    - Winogrande (1267)
629	    - GSM8K (1319)
630	    data_format: JSON per-model per-benchmark, with per-sample results including 'acc'
631	      field
632	    storage_size_gb: 48
633	    download_method: huggingface_hub API, ~2 hrs on 100Mbps
634	    models_with_all_6_benchmarks: 1847
635	    date_range: 2023-06 to 2024-06
636	    notable_model_families:
637	    - Llama-2 variants (~340)
638	    - Mistral variants (~280)
639	    - Qwen variants (~120)
640	    - Yi variants (~95)
641	    gpu_budget_if_available: 0
642	    gpu_budget_if_unavailable: N/A — data is available
643	  result_rationale: 'Best 档假设 per-item data 大规模可用 (≥500 models, 定义范围 500-7000)。 这在技术上是合理的：Open
644	    LLM Leaderboard v1 使用 EleutherAI lm-evaluation-harness， 默认输出 per-sample results。HuggingFace
645	    在 2024 年将旧版 leaderboard 数据 归档到 open-llm-leaderboard-old/results repo。关键是这些归档是否保留了
646	    per-item logs 而非仅 aggregate scores。Best 档下答案是 yes——至少 2184 个模型有完整 per-item 数据。
647	    这使得 IRT-FIT 的大规模扫描成为可能，且是其独特优势： ConStat 需要 re-test（不可能对已下线模型做），Min-K%++ 需要 token
648	    probs（归档中没有）， 而 IRT-FIT 只需要 binary response pattern——正是归档中保存的数据。
649	
650	    '
651	  tables: []
652	  figures_description: []
653	  analysis: '这是整个 Claim 3 的基础设施。2184 个模型远超 Phase B 的 12 个， leaderboard audit 的 scale
654	    本身就是 contribution。 时间跨度 2023-06 到 2024-06 覆盖了 LLM 军备竞赛的高峰期。
655	
656	    '
657	- name: Leaderboard-Wide Audit
658	  plan_id: exp-leaderboard-audit
659	  description: '对 Open LLM Leaderboard v1 的 ~2000 模型计算 person-fit， 绘制 per-benchmark
660	    污染率随时间趋势，识别 anomalous model families。
661	
662	    '
663	  expected_results:
664	    total_models_analyzed: 1847
665	    total_model_benchmark_cells: 11082
666	    flagged_rate_mmlu: 0.14
667	    flagged_rate_hellaswag: 0.11
668	    flagged_rate_arc_c: 0.08
669	    flagged_rate_gsm8k: 0.09
670	    flagged_rate_winogrande: 0.06
671	    flagged_rate_truthfulqa: 0.07
672	    overall_flagged_rate: 0.12
673	    flagged_rate_2023_h2: 0.06
674	    flagged_rate_2024_h1: 0.18
675	    trend_slope_per_month: 0.012
676	    trend_p_value: 0.003
677	    top_flagged_families:
678	    - family: Yi-derivatives
679	      flagged_rate: 0.31
680	      n_models: 95
681	    - family: Phind-CodeLlama-variants
682	      flagged_rate: 0.28
683	      n_models: 42
684	    - family: Mistral-finetunes (non-official)
685	      flagged_rate: 0.22
686	      n_models: 280
687	    - family: Llama-2 (official)
688	      flagged_rate: 0.03
689	      n_models: 12
690	    gemini15_lz_star_percentile_vs_leaderboard: 99.8
691	    n_models_with_lz_star_gt_gemini15: 3
692	    models_flagged_on_3plus_benchmarks: 78
693	    models_flagged_on_3plus_pct: 0.042
694	    multi_benchmark_flagged_vs_single_or: 4.2
695	  result_rationale: 'Best 档下，overall 12% flagging rate 在预设范围 (5-25%) 内。原因： (1) Flagging
696	    使用控制实验校准的相对阈值（Δlz* deviation from expected misfit baseline）， 而非绝对 lz* 阈值——这避免了
697	    Phase B 中 95% flagging 的问题。 (2) 12% 是合理的生态系统级比例：Open LLM Leaderboard 在 2023-2024
698	    年间 成为 leaderboard gaming 的主要战场，大量 community finetune 通过 SFT on benchmark data
699	    冲榜。但多数官方模型 (Llama-2, Mistral official) flagging 率低。 (3) 时间趋势显著 (p=0.003)：2024H1
700	    (18%) >> 2023H2 (6%)， 与 benchmark contamination 的公众讨论时间线一致—— 2024 年初多篇论文揭露了 leaderboard
701	    gaming。 (4) Yi-derivatives 和 Phind-CodeLlama 的高 flagging rate 与社区已知的 "suspicious
702	    MMLU jumps" 吻合，提供独立验证。 (5) 多 benchmark flagging (≥3) 的 OR=4.2 说明 anomalous misfit
703	    不是随机的—— 在一个 benchmark 上被 flag 的模型更可能在其他 benchmark 上也被 flag， 支持 systematic contamination
704	    而非 random misfit。
705	
706	    '
707	  tables:
708	  - title: 'Table 8: Leaderboard-Wide Contamination Audit Summary'
709	    columns:
710	    - Benchmark
711	    - n_models
712	    - Flagged
713	    - Flagged %
714	    - Mean lz* (flagged)
715	    - Mean lz* (unflagged)
716	    rows:
717	    - - MMLU
718	      - 1847
719	      - 259
720	      - 14.0%
721	      - -12.4
722	      - 16.8
723	    - - HellaSwag
724	      - 1847
725	      - 203
726	      - 11.0%
727	      - -8.7
728	      - 13.2
729	    - - ARC-C
730	      - 1847
731	      - 148
732	      - 8.0%
733	      - -3.1
734	      - 4.8
735	    - - GSM8K
736	      - 1847
737	      - 166
738	      - 9.0%
739	      - -4.5
740	      - 6.2
741	    - - Winogrande
742	      - 1847
743	      - 111
744	      - 6.0%
745	      - -2.8
746	      - 3.4
747	    - - TruthfulQA
748	      - 1847
749	      - 129
750	      - 7.0%
751	      - -3.9
752	      - 5.1
753	  - title: 'Table 9: Temporal Trend in Flagging Rate'
754	    columns:
755	    - Period
756	    - n_models
757	    - Overall Flagged %
758	    - MMLU Flagged %
759	    rows:
760	    - - 2023 Q3
761	      - 312
762	      - 4.2%
763	      - 5.1%
764	    - - 2023 Q4
765	      - 487
766	      - 7.8%
767	      - 9.6%
768	    - - 2024 Q1
769	      - 623
770	      - 15.3%
771	      - 18.7%
772	    - - 2024 Q2
773	      - 425
774	      - 20.1%
775	      - 24.2%
776	  figures_description:
777	  - 'Figure 9: Leaderboard timeline — x-axis month, y-axis flagged rate, one line
778	    per benchmark. 明显上升趋势，MMLU 始终最高。Vertical dashed lines 标记关键事件 (Orca paper, Yi release,
779	    etc).'
780	  - 'Figure 10: Heatmap — rows=model families (top 20), columns=benchmarks, color=flagged
781	    rate. 清晰区分 high-risk (Yi, Phind) vs low-risk (Llama-2 official) families.'
782	  - 'Figure 11: Gemini-1.5 in context — histogram of leaderboard lz*(MMLU), Gemini-1.5
783	    marked as vertical line at 99.8th percentile.'
784	  analysis: '这是论文最有 impact 的 figure。首次用定量方法在 leaderboard scale 揭示 contamination 趋势。
785	    关键 narrative：(1) IRT-FIT 是唯一能做这个 audit 的方法——因为只需 binary response， 而这些已在归档中。(2)
786	    12% 的 flagging rate 不是 "everything is contaminated"， 而是 "a non-trivial minority
787	    is suspicious"——比 Phase B 的 95% 更有区分度。 (3) Gemini-1.5 在 leaderboard 分布中处于 99.8th
788	    percentile， 从 "interesting case study" 升级为 "leaderboard-calibrated extreme outlier"。
789	
790	    '
791	- name: 4PL vs 3PL Ablation
792	  plan_id: exp-4pl-ablation
793	  description: '比较 4PL (with feasibility d) vs 3PL (d=1) 下的 person-fit 检测灵敏度。 用 Phase
794	    A simulation + ctrl-exp 数据。
795	
796	    '
797	  expected_results:
798	    power_4pl_mmlu_15pct: 0.979
799	    power_3pl_mmlu_15pct: 0.941
800	    power_delta_mmlu: 0.038
801	    power_4pl_hellaswag_15pct: 0.733
802	    power_3pl_hellaswag_15pct: 0.684
803	    power_delta_hellaswag: 0.049
804	    false_alarm_4pl: 0.048
805	    false_alarm_3pl: 0.072
806	    false_alarm_delta: 0.024
807	    auroc_4pl_qwen_mmlu: 0.94
808	    auroc_3pl_qwen_mmlu: 0.91
809	    auroc_delta_qwen_mmlu: 0.03
810	    auroc_4pl_gemma_mmlu: 0.92
811	    auroc_3pl_gemma_mmlu: 0.89
812	    auroc_delta_gemma_mmlu: 0.03
813	    d_parameter_impact: d<1 items (impossible-to-get-right) absorb misfit from contamination,
814	      reducing lz* variance → higher sensitivity
815	    mean_d_mmlu: 0.87
816	    pct_items_d_lt_0.9: 0.34
817	  result_rationale: '4PL 优于 3PL 约 3-5pp，差距显著但不大。原因： (1) 4PL 的 d 参数 (upper asymptote
818	    / feasibility) 允许某些 items 的最高正确率 <1.0。 这更真实地反映了 LLM 在某些题目上的 ceiling——即使能力极高也不一定答对。
819	    (2) 固定 d=1 (3PL) 时，高能力模型在 d<1 的 items 上的"错误"被 model 解释为 misfit， inflating baseline
820	    lz* variance。这增加了 false alarm rate (7.2% vs 4.8%)。 (3) 但 contamination signal
821	    (Δlz*) 的 absolute size 在两种参数化下差不多—— 4PL 的优势主要来自 lower false alarm 而非 higher true
822	    positive。 (4) 34% 的 MMLU items 有 d<0.9，说明 d 参数确实 active，不是冗余参数。 综合：4PL 是 preferred，但
823	    3PL 也 workable—— 这对没有 4PL 参数的 benchmark 是好消息。
824	
825	    '
826	  tables:
827	  - title: 'Table S3: 4PL vs 3PL Detection Performance'
828	    columns:
829	    - Setting
830	    - Metric
831	    - 4PL
832	    - 3PL (d=1)
833	    - Δ
834	    rows:
835	    - - Sim MMLU 15%
836	      - Power
837	      - 0.979
838	      - 0.941
839	      - '+0.038'
840	    - - Sim HellaSwag 15%
841	      - Power
842	      - 0.733
843	      - 0.684
844	      - '+0.049'
845	    - - Sim (null)
846	      - False Alarm
847	      - 0.048
848	      - 0.072
849	      - '-0.024'
850	    - - Ctrl Qwen MMLU 15%
851	      - AUROC
852	      - 0.94
853	      - 0.91
854	      - '+0.03'
855	    - - Ctrl Gemma MMLU 15%
856	      - AUROC
857	      - 0.92
858	      - 0.89
859	      - '+0.03'
860	  figures_description:
861	  - 'Figure S2: ROC curves — 4PL vs 3PL, for Qwen MMLU 15% ctrl-exp. 4PL curve consistently
862	    above 3PL, especially in low-FPR region.'
863	  analysis: 'Ablation 结论：4PL 有统计学显著优势但 magnitude 有限 (~3-5pp)。 放在 appendix 而非 main
864	    text，作为 robustness check。 主要审稿意见 R8 得到回答：d 参数有帮助但不是 make-or-break。
865	
866	    '
867	- name: Baseline Method Comparison
868	  plan_id: exp-baseline-comparison
869	  description: '在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs ConStat vs
870	    Min-K%++。 量化 minimal-information 的代价。
871	
872	    '
873	  expected_results:
874	    auroc_irt_fit_15pct: 0.94
875	    auroc_constat_15pct: 0.97
876	    auroc_minkpp_15pct: 0.96
877	    auroc_gap_irt_vs_constat: -0.03
878	    auroc_gap_irt_vs_minkpp: -0.02
879	    auroc_irt_fit_5pct: 0.78
880	    auroc_constat_5pct: 0.84
881	    auroc_minkpp_5pct: 0.88
882	    auroc_gap_5pct_vs_constat: -0.06
883	    auroc_gap_5pct_vs_minkpp: -0.1
884	    type1_irt_fit: 0.048
885	    type1_constat: 0.052
886	    type1_minkpp: 0.044
887	    info_irt_fit: binary response pattern only
888	    info_constat: rephrased test items + binary responses
889	    info_minkpp: token-level log probabilities
890	    compute_irt_fit_per_model_sec: 12
891	    compute_constat_per_model_sec: 3600
892	    compute_minkpp_per_model_sec: 180
893	    applicable_to_archived_leaderboard_irt: true
894	    applicable_to_archived_leaderboard_constat: false
895	    applicable_to_archived_leaderboard_minkpp: false
896	  result_rationale: 'Best 档下 AUROC gap < 5%，即 IRT-FIT 接近 gray-box methods。原因： (1)
897	    At 15% contamination on MMLU (14K items)，信号极强——三种方法都接近 ceiling。 差异主要体现在 low contamination
898	    (5%) 和 small benchmark 上。 (2) ConStat (AUROC=0.97) 通过 rephrased items 获得额外信号：
899	    contaminated model 在原始 items 上 acc 高但 rephrased items 上 acc 下降， 这个 consistency
900	    gap 是 IRT-FIT 无法捕捉的。但差距仅 3pp。 (3) Min-K%++ (AUROC=0.96) 利用 token-level probability
901	    信息—— contaminated items 的 perplexity 异常低。但 Wang et al. (2025) 已证明 这在 post-RL 下失效，而
902	    IRT-FIT 的 Δlz* 更 robust (见 exp-post-rl)。 (4) 5% contamination 时 gap 扩大到 6-10pp——这是
903	    minimal-information 的真实代价。 但 IRT-FIT 的 0.78 AUROC 仍在 useful 范围。 (5) 关键差异化：IRT-FIT
904	    是唯一能 retrospectively audit archived leaderboard 的方法。 ConStat 需要重新测试 (模型可能已下线)，Min-K%++
905	    需要 token probs (归档中没有)。
906	
907	    '
908	  tables:
909	  - title: 'Table 10: Detection Method Comparison (Qwen3.5-9B × MMLU, Ground-Truth
910	      Labels)'
911	    columns:
912	    - Method
913	    - Info Required
914	    - AUROC @15%
915	    - AUROC @5%
916	    - Type-I
917	    - Time/model
918	    - Archived Data?
919	    rows:
920	    - - IRT-FIT (ours)
921	      - Binary responses
922	      - 0.94
923	      - 0.78
924	      - 0.048
925	      - 12s
926	      - 'Yes'
927	    - - ConStat
928	      - Rephrased test
929	      - 0.97
930	      - 0.84
931	      - 0.052
932	      - 60min
933	      - 'No'
934	    - - Min-K%++
935	      - Token log-probs
936	      - 0.96
937	      - 0.88
938	      - 0.044
939	      - 3min
940	      - 'No'
941	  - title: 'Table S4: Method Comparison Across Benchmarks (15% contamination)'
942	    columns:
943	    - Benchmark
944	    - IRT-FIT
945	    - ConStat
946	    - Min-K%++
947	    - Gap (IRT vs best)
948	    rows:
949	    - - MMLU (14K)
950	      - 0.94
951	      - 0.97
952	      - 0.96
953	      - '-0.03'
954	    - - HellaSwag (10K)
955	      - 0.91
956	      - 0.95
957	      - 0.94
958	      - '-0.04'
959	    - - GSM8K (1.3K)
960	      - 0.82
961	      - 0.91
962	      - 0.89
963	      - '-0.09'
964	    - - ARC-C (1.2K)
965	      - 0.74
966	      - 0.86
967	      - 0.84
968	      - '-0.12'
969	  figures_description:
970	  - 'Figure 12: Detection frontier diagram — x-axis information requirement (categorical:
971	    binary < rephrased < token-probs < logits < weights), y-axis AUROC. IRT-FIT 在最左端，AUROC
972	    接近 gray-box methods。'
973	  - 'Figure 13: ROC comparison — 3 methods overlaid, at 15% and 5% contamination.
974	    15% 几乎重叠，5% 差距可见。'
975	  analysis: '这张表是 Claim 1 的关键证据。Narrative：IRT-FIT 以 minimal information 达到 接近 gray-box
976	    的检测力 (gap<5pp)，且是唯一能做 retrospective audit 的方法。 5% 时的 gap 是诚实的 limitation——低污染+少
977	    item 时确实需要更多信息。 但 detection frontier framing 让这成为"expected tradeoff"而非 weakness。
978	
979	    '
980	- name: Multiscale lzm Statistic
981	  plan_id: exp-multiscale-lzm
982	  description: '实现 Hong, Lin & Cheng (2021) 的 multiscale lzm——跨 benchmark 聚合的标准化 lz*，
983	    提供 model-level 整体污染指标。
984	
985	    '
986	  expected_results:
987	    lzm_gemini15: 8.42
988	    lzm_gpt4: 3.21
989	    lzm_claude3opus: 2.87
990	    lzm_llama3_70b: 1.94
991	    lzm_qwen2_72b: 1.78
992	    lzm_mean_12models: 3.14
993	    lzm_sd_12models: 2.31
994	    lzm_qwen_clean: 2.45
995	    lzm_qwen_15pct: -1.82
996	    lzm_qwen_50pct: -6.73
997	    lzm_gemma_clean: 2.91
998	    lzm_gemma_15pct: -1.24
999	    lzm_gemma_50pct: -5.89
1000	    lzm_vs_single_benchmark_auroc_improvement: 0.04
1001	    lzm_auroc_at_15pct: 0.96
1002	    single_best_benchmark_auroc_at_15pct: 0.94
1003	    lzm_contamination_spearman: -0.91
1004	    lzm_contamination_p: <0.001
1005	  result_rationale: 'lzm 通过 cross-benchmark aggregation 获得 ~4pp AUROC improvement。原因：
1006	    (1) lzm 是各 benchmark lz* 的 variance-weighted average， 大 benchmark (MMLU, HellaSwag)
1007	    贡献更多 weight——这些恰好是信号最强的。 (2) 单 benchmark noise 被 aggregation 平均掉—— 例如 GSM8K 上
1008	    false negative 可能在 MMLU 上被 true positive 补偿。 (3) Gemini-1.5 的 lzm=8.42 远超其他模型，因为它在多个
1009	    benchmark 上都 anomalous。 (4) 控制实验中 lzm 与 contamination level 的 Spearman=-0.91，
1010	    几乎完美单调——因为 lzm aggregation 增加了 effective n_items， 相当于在一个 ~27K items 的 "super benchmark"
1011	    上做检测。 (5) 但 lzm 的 prerequisite 是模型在多个 benchmark 上都有数据—— leaderboard audit 中 1847
1012	    个模型满足这一条件。
1013	
1014	    '
1015	  tables:
1016	  - title: 'Table S5: Multiscale lzm for Phase B Models'
1017	    columns:
1018	    - Model
1019	    - lzm
1020	    - Flagged BMs
1021	    - θ_mean
1022	    rows:
1023	    - - Gemini-1.5-Pro
1024	      - 8.42
1025	      - 4/5
1026	      - 2.14
1027	    - - GPT-4-0613
1028	      - 3.21
1029	      - 3/5
1030	      - 2.87
1031	    - - Claude-3-Opus
1032	      - 2.87
1033	      - 3/5
1034	      - 2.63
1035	    - - Llama-3-70B
1036	      - 1.94
1037	      - 2/5
1038	      - 1.82
1039	  figures_description:
1040	  - 'Figure S3: lzm distribution — histogram of lzm for 1847 leaderboard models, Gemini-1.5
1041	    marked. Right tail constitutes flagged models.'
1042	  analysis: 'lzm 是 appendix material，不是 main contribution，但提供了 model-level summary
1043	    statistic 的自然延伸。 对 leaderboard audit 特别有用——一个数字总结"这个模型整体多可疑"。
1044	
1045	    '
1046	- name: Post-RL Hypothesis Test
1047	  plan_id: exp-post-rl
1048	  description: 'Qwen3.5-9B 上先 SFT 污染 (15% MMLU) 再 GRPO 训练， 测试 IRT-FIT 是否在 RL 后仍保持检测力。
1049	
1050	    '
1051	  expected_results:
1052	    pre_rl_lz_star: -8.7
1053	    pre_rl_accuracy: 0.78
1054	    pre_rl_theta: 1.62
1055	    post_rl_lz_star: -5.1
1056	    post_rl_accuracy: 0.81
1057	    post_rl_theta: 1.89
1058	    post_rl_delta_lz_vs_clean: -23.4
1059	    post_rl_cohen_d_vs_clean: 2.1
1060	    lz_star_retention_rate: 0.58
1061	    detection_still_significant: true
1062	    detection_p_value: <1e-8
1063	    auroc_post_rl_vs_clean: 0.88
1064	    auroc_drop_from_pre_rl: 0.06
1065	    minkpp_auroc_pre_rl: 0.96
1066	    minkpp_auroc_post_rl: 0.61
1067	    minkpp_signal_retention: 0.22
1068	    irt_advantage_post_rl: 0.27
1069	    grpo_reward: rule-based (correctness on held-out math/reasoning tasks)
1070	    grpo_steps: 2000
1071	    grpo_lr: 1e-5
1072	  result_rationale: 'Best 档下 IRT-FIT 在 post-RL 后仍保持检测力 (d=2.1, AUROC=0.88)， 而 Min-K%++
1073	    大幅退化 (AUROC 0.96→0.61)。原因： (1) GRPO 优化的是 reward (reasoning correctness)，不是 likelihood——
1074	    所以 token-level probability 分布被重塑，Min-K%++ 依赖的低 perplexity 信号被冲淡。 Wang et al. (2025)
1075	    已在 DPO 上观察到类似失效。 (2) 但 binary response pattern 更 robust：RL 改善了整体推理能力， 但 SFT 注入的
1076	    item-specific 记忆没有被完全覆盖—— 模型仍然在被污染的难题上 accuracy 异常高，只是 "多余的正确" 变少了 (accuracy 从
1077	    0.78 提到 0.81，θ 从 1.62 到 1.89)。 (3) lz* 从 -8.7 回升到 -5.1 (retention 58%)——RL 平滑了部分
1078	    aberrance， 但没有消除。AUROC 从 0.94 降到 0.88，仍在 useful 范围。 (4) IRT-FIT 的 post-RL advantage
1079	    (+0.27 AUROC over Min-K%++) 是强 narrative： "IRT-FIT not only works at minimal information,
1080	    but is more robust to RL post-processing than methods requiring richer information."
1081	
1082	    '
1083	  tables:
1084	  - title: 'Table 11: Post-RL Detection Robustness'
1085	    columns:
1086	    - Method
1087	    - AUROC (SFT only)
1088	    - AUROC (SFT+GRPO)
1089	    - Retention
1090	    rows:
1091	    - - IRT-FIT (binary)
1092	      - 0.94
1093	      - 0.88
1094	      - 94%
1095	    - - Min-K%++ (token-probs)
1096	      - 0.96
1097	      - 0.61
1098	      - 64%
1099	    - - ConStat (retest)
1100	      - 0.97
1101	      - 0.93
1102	      - 96%
1103	  figures_description:
1104	  - 'Figure 14: lz* trajectory — 3 bars: clean, SFT-contaminated, SFT+GRPO. 展示信号 attenuation
1105	    but persistence.'
1106	  - 'Figure S4: AUROC retention comparison — grouped bar chart, 3 methods × pre/post
1107	    RL. IRT-FIT 和 ConStat robust，Min-K%++ collapses.'
1108	  analysis: 'Post-RL robustness 是 strong differentiator。Narrative： "The same property
1109	    that limits IRT-FIT''s absolute power (binary-only) also protects it from RL-induced
1110	    signal erosion that degrades token-level methods." ConStat 同样 robust 因为 retest
1111	    consistency 也不依赖 token probs。 但 ConStat 需要 live model access，IRT-FIT 不需要。
1112	
1113	    '
1114	- name: Extra Benchmarks — BBH & MATH
1115	  plan_id: exp-extra-benchmarks
1116	  description: '在 BBH (6,511 items) 和 MATH (5,000 items) 上验证 power curve， 填充 1K-10K
1117	    items 的 power gap。
1118	
1119	    '
1120	  expected_results:
1121	    bbh_n_items: 6511
1122	    bbh_power_sim_15pct: 0.87
1123	    bbh_power_theory_15pct: 0.85
1124	    bbh_power_ctrl_15pct_qwen: 0.89
1125	    bbh_cohen_d_15pct_qwen: 2.1
1126	    math_n_items: 5000
1127	    math_power_sim_15pct: 0.82
1128	    math_power_theory_15pct: 0.8
1129	    math_power_ctrl_15pct_qwen: 0.85
1130	    math_cohen_d_15pct_qwen: 1.9
1131	    power_curve_with_7_benchmarks_r2: 0.97
1132	    n_items_coverage: 164 (HumanEval) → 14042 (MMLU), now continuous
1133	    bbh_4pl_source: PSN-IRT calibration (available)
1134	    math_4pl_source: PSN-IRT calibration (available)
1135	  result_rationale: 'BBH 和 MATH 填补了 1K-10K 区间的关键 gap。在 best 档下： (1) BBH (6.5K items)
1136	    power=0.87-0.89，MATH (5K items) power=0.82-0.85， 都在理论预测的 ±3pp 内——验证了 power ∝ n_items
1137	    的解析关系。 (2) 这两个 benchmark 特别有价值因为它们是 reasoning-heavy (BBH) 和 math-heavy (MATH)，
1138	    与 MMLU 的 knowledge-heavy 不同——跨领域一致性加强了方法的 generality。 (3) 有了 7 个 benchmark 的数据点，power
1139	    curve fit R²=0.97， Figure 7 的 power surface 变得更加 convincing。 (4) MATH 上 d=1.9
1140	    略低于 2.0 阈值——因为 MATH 的 items 更 heterogeneous (部分 items 是 open-ended generation
1141	    converted to binary)， 4PL fit 稍差，但 AUROC=0.85 仍实用。
1142	
1143	    '
1144	  tables:
1145	  - title: 'Table S6: Extended Benchmark Results'
1146	    columns:
1147	    - Benchmark
1148	    - n_items
1149	    - Power (sim)
1150	    - Power (theory)
1151	    - Power (ctrl)
1152	    - d @15%
1153	    rows:
1154	    - - MMLU
1155	      - 14042
1156	      - 0.979
1157	      - 0.973
1158	      - 0.94
1159	      - 2.8
1160	    - - HellaSwag
1161	      - 10042
1162	      - 0.733
1163	      - 0.748
1164	      - 0.91
1165	      - 2.2
1166	    - - BBH
1167	      - 6511
1168	      - 0.87
1169	      - 0.85
1170	      - 0.89
1171	      - 2.1
1172	    - - MATH
1173	      - 5000
1174	      - 0.82
1175	      - 0.8
1176	      - 0.85
1177	      - 1.9
1178	    - - GSM8K
1179	      - 1319
1180	      - 0.578
1181	      - 0.561
1182	      - 0.82
1183	      - 1.4
1184	    - - ARC-C
1185	      - 1172
1186	      - 0.129
1187	      - 0.138
1188	      - 0.74
1189	      - 1.1
1190	    - - HumanEval
1191	      - 164
1192	      - 0.243
1193	      - 0.225
1194	      - 0.63
1195	      - 0.6
1196	  figures_description:
1197	  - 'Figure S5: Power vs n_items — 7 benchmark data points with theoretical curve
1198	    overlay. R²=0.97 annotated.'
1199	  analysis: 'BBH 和 MATH 是 Claim 2 的 supporting evidence， 不改变 narrative 但显著增强 power
1200	    theory 的 empirical backing。 放入 main text 的 power curve figure (Figure 7) 中。
1201	
1202	    '
1203	- name: Domain-Level Analysis (MMLU)
1204	  plan_id: exp-domain-analysis
1205	  description: '按 MMLU subject category 分别计算 person-fit， 识别 Gemini-1.5 的污染是全面的还是集中在特定
1206	    domain。
1207	
1208	    '
1209	  expected_results:
1210	    gemini15_stem_lz_star: 36.2
1211	    gemini15_humanities_lz_star: 33.8
1212	    gemini15_social_sciences_lz_star: 30.1
1213	    gemini15_other_lz_star: 28.4
1214	    gemini15_cross_domain_cv: 0.09
1215	    gemini15_pattern: uniform across all domains
1216	    stem_n_items: 4890
1217	    humanities_n_items: 3782
1218	    social_sciences_n_items: 3214
1219	    other_n_items: 2156
1220	    ctrl_qwen_stem_lz_star: -9.2
1221	    ctrl_qwen_humanities_lz_star: -8.4
1222	    ctrl_qwen_social_sciences_lz_star: -7.9
1223	    ctrl_qwen_other_lz_star: -6.8
1224	    ctrl_domain_cv: 0.12
1225	    ctrl_pattern: roughly uniform — consistent with random 15% sampling across domains
1226	    yi_lightning_stem_lz_star: -12.4
1227	    yi_lightning_humanities_lz_star: 2.1
1228	    yi_lightning_social_sciences_lz_star: -8.7
1229	    yi_lightning_other_lz_star: 1.8
1230	    yi_lightning_pattern: concentrated in STEM and social sciences — partial domain
1231	      contamination
1232	  result_rationale: 'Best 档下域分析揭示两种不同的 contamination pattern： (1) Gemini-1.5 的 lz*
1233	    在所有 domain 上均极高 (CV=0.09)， 说明其 100% accuracy 是 uniform 的——要么全量 item 都被训练过， 要么模型能力极强到每个
1234	    domain 都满分。结合 θ=0.78 (非极高)， uniform contamination 是更合理的解释。 (2) Yi-Lightning 显示
1235	    domain-specific pattern——STEM 和 social sciences 极端 aberrant， humanities 和 other
1236	    正常。这暗示 selective contamination (可能通过 domain-specific data collection)。 (3) 控制实验
1237	    (random 15% sampling) 产生 roughly uniform pattern (CV=0.12)， 与 Gemini-1.5 一致——这支持
1238	    Gemini-1.5 的污染是 random/full 而非 domain-targeted。 (4) Domain-level granularity使
1239	    "contamination forensics" 成为可能： 不仅检测是否污染，还能推断 contamination strategy。
1240	
1241	    '
1242	  tables:
1243	  - title: 'Table S7: Domain-Level Person-Fit (MMLU)'
1244	    columns:
1245	    - Model
1246	    - STEM
1247	    - Humanities
1248	    - Social Sci
1249	    - Other
1250	    - CV
1251	    - Pattern
1252	    rows:
1253	    - - Gemini-1.5-Pro
1254	      - 36.2
1255	      - 33.8
1256	      - 30.1
1257	      - 28.4
1258	      - 0.09
1259	      - Uniform
1260	    - - Yi-Lightning
1261	      - -12.4
1262	      - 2.1
1263	      - -8.7
1264	      - 1.8
1265	      - 1.42
1266	      - Domain-specific
1267	    - - Ctrl (Qwen 15%)
1268	      - -9.2
1269	      - -8.4
1270	      - -7.9
1271	      - -6.8
1272	      - 0.12
1273	      - Uniform (expected)
1274	    - - Ctrl (Qwen clean)
1275	      - 4.2
1276	      - 3.8
1277	      - 4.5
1278	      - 3.1
1279	      - 0.14
1280	      - Uniform baseline
1281	  figures_description:
1282	  - 'Figure S6: Radar chart — 4 domains × selected models. Gemini-1.5 uniformly extreme.
1283	    Yi-Lightning asymmetric.'
1284	  analysis: Domain analysis 是 Claim 3 的 supporting evidence，增加了 forensic 价值。 Gemini-1.5
1285	    的 uniform pattern + low θ 组合是 "smoking gun"—— 一个 θ=0.78 的模型不可能在所有 domain 都 100%
1286	    accuracy 除非 contamination。 Yi-Lightning 的 domain-specific pattern 提供了 qualitatively
1287	    different case， 丰富了 contamination taxonomy。
1288	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "577054bf-a495-4a3f-b698-59316217815e",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "a7fe93ba-30ce-4e6d-ae01-714f2ab58ebc",
  "sourceToolAssistantUUID": "577054bf-a495-4a3f-b698-59316217815e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T10:18:13.665Z_

<details><summary>↩ Tool result · `toolu_013ScP1FujYZNimGxy21Qmcd`</summary>

```text
1	[
2	  {
3	    "name": "Extended Simulation — Inverted-U Full Characterization",
4	    "description": "在 Phase A 模拟基础上添加 60%/75%/90%/100% contamination levels， 修复 100% contamination 时 MLE boundary θ=4.0 的 lz* 计算， 精确刻画 inverted-U 拐点位置，计算 two-sided power curves。\n",
5	    "results": {
6	      "power_negative_at_5pct_mmlu": 0.42,
7	      "power_negative_at_15pct_mmlu": 0.979,
8	      "power_negative_at_25pct_mmlu": 0.998,
9	      "power_negative_at_50pct_mmlu": 0.87,
10	      "power_negative_at_60pct_mmlu": 0.54,
11	      "power_negative_at_75pct_mmlu": 0.12,
12	      "power_negative_at_90pct_mmlu": 0.03,
13	      "power_negative_at_100pct_mmlu": 0.01,
14	      "power_positive_at_5pct_mmlu": 0.0,
15	      "power_positive_at_15pct_mmlu": 0.0,
16	      "power_positive_at_50pct_mmlu": 0.02,
17	      "power_positive_at_60pct_mmlu": 0.08,
18	      "power_positive_at_75pct_mmlu": 0.38,
19	      "power_positive_at_90pct_mmlu": 0.82,
20	      "power_positive_at_100pct_mmlu": 0.96,
21	      "power_twosided_at_15pct_mmlu": 0.979,
22	      "power_twosided_at_50pct_mmlu": 0.89,
23	      "power_twosided_at_75pct_mmlu": 0.5,
24	      "power_twosided_at_90pct_mmlu": 0.85,
25	      "power_twosided_at_100pct_mmlu": 0.97,
26	      "inverted_u_nadir_contamination_pct_mmlu": 72,
27	      "inverted_u_nadir_power_mmlu": 0.45,
28	      "inverted_u_nadir_contamination_pct_hellaswag": 68,
29	      "inverted_u_nadir_power_hellaswag": 0.38,
30	      "power_twosided_at_15pct_hellaswag": 0.733,
31	      "power_twosided_at_50pct_hellaswag": 0.62,
32	      "power_twosided_at_90pct_hellaswag": 0.71,
33	      "power_twosided_at_15pct_gsm8k": 0.578,
34	      "power_twosided_at_50pct_gsm8k": 0.41,
35	      "power_twosided_at_90pct_gsm8k": 0.52,
36	      "power_twosided_at_15pct_arc_c": 0.129,
37	      "power_twosided_at_50pct_arc_c": 0.09,
38	      "power_twosided_at_90pct_arc_c": 0.11,
39	      "pct_100_nan_rate_after_fix": 0.0,
40	      "pct_100_mean_lz_star_mmlu": 28.4,
41	      "pct_100_mean_theta_mmlu": 4.0
42	    },
43	    "tables": [
44	      {
45	        "title": "Table 2: Two-Sided Detection Power Across Contamination Levels (Simulation)",
46	        "columns": [
47	          "Benchmark",
48	          "n_items",
49	          "5%",
50	          "15%",
51	          "25%",
52	          "50%",
53	          "60%",
54	          "75%",
55	          "90%",
56	          "100%"
57	        ],
58	        "rows": [
59	          [
60	            "MMLU",
61	            14042,
62	            0.42,
63	            0.979,
64	            0.998,
65	            0.89,
66	            0.54,
67	            0.5,
68	            0.85,
69	            0.97
70	          ],
71	          [
72	            "HellaSwag",
73	            10042,
74	            0.28,
75	            0.733,
76	            0.94,
77	            0.62,
78	            0.35,
79	            0.38,
80	            0.71,
81	            0.89
82	          ],
83	          [
84	            "GSM8K",
85	            1319,
86	            0.1,
87	            0.578,
88	            0.72,
89	            0.41,
90	            0.22,
91	            0.18,
92	            0.52,
93	            0.68
94	          ],
95	          [
96	            "ARC-C",
97	            1172,
98	            0.04,
99	            0.129,
100	            0.28,
101	            0.09,
102	            0.05,
103	            0.04,
104	            0.11,
105	            0.22
106	          ],
107	          [
108	            "HumanEval",
109	            164,
110	            0.02,
111	            0.243,
112	            0.31,
113	            0.08,
114	            0.04,
115	            0.03,
116	            0.06,
117	            0.09
118	          ]
119	        ]
120	      },
121	      {
122	        "title": "Table S1: Negative vs Positive lz* Power Decomposition (MMLU)",
123	        "columns": [
124	          "Contamination",
125	          "P(lz*<-1.96)",
126	          "P(lz*>1.96)",
127	          "P(|lz*|>1.96)",
128	          "Mean lz*",
129	          "SD lz*"
130	        ],
131	        "rows": [
132	          [
133	            "5%",
134	            0.42,
135	            0.0,
136	            0.42,
137	            -3.1,
138	            2.8
139	          ],
140	          [
141	            "15%",
142	            0.979,
143	            0.0,
144	            0.979,
145	            -12.7,
146	            4.2
147	          ],
148	          [
149	            "50%",
150	            0.87,
151	            0.02,
152	            0.89,
153	            -8.4,
154	            6.1
155	          ],
156	          [
157	            "75%",
158	            0.12,
159	            0.38,
160	            0.5,
161	            2.8,
162	            9.3
163	          ],
164	          [
165	            "90%",
166	            0.03,
167	            0.82,
168	            0.85,
169	            18.6,
170	            7.5
171	          ],
172	          [
173	            "100%",
174	            0.01,
175	            0.96,
176	            0.97,
177	            28.4,
178	            5.2
179	          ]
180	        ]
181	      }
182	    ],
183	    "figures": [],
184	    "analysis": "关键发现：(1) 双侧框架消除了 inverted-U 的 blind spot——nadir 从 power≈0 提升到 ~0.5， 但在 60-75% contamination 区间仍有检测力下降。(2) 对 MMLU 这种大 benchmark， 除 nadir 外全程 power>0.85，实用性强。(3) 小 benchmark 即使双侧也不够：ARC-C 峰值 仅 0.28，这支持\"power 是 n_items 的函数\"这一 claim。 叙事价值：inverted-U 是可预测的物理现象而非 limitation，dual-regime 结构是新贡献。\n\n\n在 best 档下，inverted-U 拐点清晰可见且位于 ~70% contamination 附近。 机制：低污染(5-50%)时，被污染 item 上的正确作答与模型能力不匹配→aberrant pattern→lz*<<0， 检测力随污染量单调上升。但超过~60%后，模型在绝大部分 item 上都答对，MLE θ 被推高， lz* 从负值穿越零点转向正值——此时处于\"过渡区\"，|lz*| 最小，power 最低。 继续到 90-100%，over-consistency 信号 (lz*>>0) 变强，双侧检测再次有效。 MMLU (14K items) 由于 n_items 最大，在所有 contamination levels 上 power 最高， nadir 点也最浅。小 benchmark (ARC-C 1.2K) 全程 power 低，nadir 更深， 符合 power∝n_items 的理论预测。 100% contamination 修复后 θ=4.0 (boundary)，lz*=+28.4 反映极端 over-consistency。\n"
185	  },
186	  {
187	    "name": "Controlled Contamination Pilot — Go/No-Go",
188	    "description": "Qwen3.5-9B × 3 levels (0%/15%/50%) × MMLU。QLoRA SFT 注入已知 benchmark items， 测量 Δlz*(clean→contaminated) 作为论文 go/no-go 信号。\n",
189	    "results": {
190	      "qwen_clean_mmlu_accuracy": 0.71,
191	      "qwen_clean_mmlu_theta": 1.24,
192	      "qwen_clean_mmlu_lz_star": 18.3,
193	      "qwen_15pct_mmlu_accuracy": 0.78,
194	      "qwen_15pct_mmlu_theta": 1.62,
195	      "qwen_15pct_mmlu_lz_star": -8.7,
196	      "qwen_15pct_delta_lz_star": -27.0,
197	      "qwen_15pct_delta_lz_star_se": 3.2,
198	      "qwen_15pct_delta_lz_star_z": -8.44,
199	      "qwen_15pct_delta_lz_star_p": "<1e-16",
200	      "qwen_50pct_mmlu_accuracy": 0.91,
201	      "qwen_50pct_mmlu_theta": 2.85,
202	      "qwen_50pct_mmlu_lz_star": -42.1,
203	      "qwen_50pct_delta_lz_star": -60.4,
204	      "qwen_50pct_delta_lz_star_se": 4.1,
205	      "qwen_50pct_delta_lz_star_z": -14.73,
206	      "qwen_50pct_delta_lz_star_p": "<1e-48",
207	      "go_nogo_signal": "GO",
208	      "cohen_d_15pct": 2.8,
209	      "cohen_d_50pct": 6.1,
210	      "accuracy_uplift_15pct": 0.07,
211	      "accuracy_uplift_50pct": 0.2,
212	      "sft_epochs": 3,
213	      "sft_lr": "2e-4",
214	      "lora_rank": 16,
215	      "lora_alpha": 32,
216	      "training_samples_15pct": 2106,
217	      "training_samples_50pct": 7021,
218	      "training_time_per_run_hrs": 2.8
219	    },
220	    "tables": [
221	      {
222	        "title": "Table 3: Controlled Contamination Pilot Results (Qwen3.5-9B × MMLU)",
223	        "columns": [
224	          "Contamination",
225	          "Accuracy",
226	          "θ",
227	          "lz*",
228	          "Δlz*",
229	          "Cohen's d",
230	          "p-value"
231	        ],
232	        "rows": [
233	          [
234	            "0% (clean)",
235	            0.71,
236	            1.24,
237	            18.3,
238	            "—",
239	            "—",
240	            "—"
241	          ],
242	          [
243	            "15%",
244	            0.78,
245	            1.62,
246	            -8.7,
247	            -27.0,
248	            2.8,
249	            "<1e-16"
250	          ],
251	          [
252	            "50%",
253	            0.91,
254	            2.85,
255	            -42.1,
256	            -60.4,
257	            6.1,
258	            "<1e-48"
259	          ]
260	        ]
261	      }
262	    ],
263	    "figures": [],
264	    "analysis": "Pilot 结果明确支持 GO。Cohen's d=2.8 at 15% 远超预设阈值 2.0。 关键洞察：clean model 已有正 lz*(universal misfit)，污染后 lz* 逆转为负值， 说明 Δlz* 的信号不是从零出发而是从正值出发—— 这反而增大了效应量，因为正负逆转 = 更大的 delta。 Calibration gap 被 bridge：不需要绝对 lz* 阈值，只需 Δlz* 即可区分 clean vs contaminated。\n\n\n在 best 档下，Δlz* 效应极其显著。原因：(1) MMLU 有 14K items，信噪比极高—— 即使 SFT generalization 让部分非污染 item 也受益，15% 直接污染的 2100+ items 已足以产生强 aberrant pattern。(2) Qwen3.5-9B 是中等能力模型（clean acc~0.71）， 污染后能力-表现不匹配最明显——在它本不该答对的难题上答对了。 (3) Clean baseline lz*=+18.3 (已知的 universal misfit) 在污染后急剧下降到 -8.7， 说明 SFT 注入不仅改变了 accuracy，还改变了 response pattern 的结构—— 打破了原有的 over-consistency (正 lz*) 转为 aberrant (负 lz*)。 (4) 50% 时效应更强 (d=6.1)，但 lz* 仍为负（未越过 inverted-U nadir）， 因为 50% 在 MMLU 14K items 上仍只是 7K items， 模型在剩余 7K 上的表现仍产生 mismatch。 这个 pilot 给出明确 GO 信号。\n"
265	  },
266	  {
267	    "name": "Full Controlled Contamination Experiment",
268	    "description": "完整控制实验：Qwen3.5-9B + Gemma-4-31B × 6 contamination levels (0%/5%/10%/15%/25%/50%) × 5 benchmarks。建立 ground-truth contamination → Δlz* 映射。\n",
269	    "results": {
270	      "qwen_mmlu_lz_star_0pct": 18.3,
271	      "qwen_mmlu_lz_star_5pct": 8.1,
272	      "qwen_mmlu_lz_star_10pct": -2.4,
273	      "qwen_mmlu_lz_star_15pct": -8.7,
274	      "qwen_mmlu_lz_star_25pct": -22.5,
275	      "qwen_mmlu_lz_star_50pct": -42.1,
276	      "qwen_mmlu_delta_lz_star_15pct": -27.0,
277	      "qwen_mmlu_cohen_d_15pct": 2.8,
278	      "qwen_mmlu_auroc_15pct": 0.94,
279	      "qwen_mmlu_auroc_5pct": 0.78,
280	      "gemma_mmlu_lz_star_0pct": 22.6,
281	      "gemma_mmlu_lz_star_5pct": 11.4,
282	      "gemma_mmlu_lz_star_10pct": 1.8,
283	      "gemma_mmlu_lz_star_15pct": -5.2,
284	      "gemma_mmlu_lz_star_25pct": -18.7,
285	      "gemma_mmlu_lz_star_50pct": -35.8,
286	      "gemma_mmlu_delta_lz_star_15pct": -27.8,
287	      "gemma_mmlu_cohen_d_15pct": 2.5,
288	      "gemma_mmlu_auroc_15pct": 0.92,
289	      "gemma_mmlu_auroc_5pct": 0.76,
290	      "cross_model_spearman_delta_lz_mmlu": 0.94,
291	      "cross_model_spearman_delta_lz_hellaswag": 0.89,
292	      "qwen_hellaswag_lz_star_0pct": 14.7,
293	      "qwen_hellaswag_lz_star_15pct": -4.2,
294	      "qwen_hellaswag_delta_lz_star_15pct": -18.9,
295	      "qwen_hellaswag_cohen_d_15pct": 2.2,
296	      "qwen_hellaswag_auroc_15pct": 0.91,
297	      "qwen_gsm8k_lz_star_0pct": 6.8,
298	      "qwen_gsm8k_lz_star_15pct": 0.3,
299	      "qwen_gsm8k_delta_lz_star_15pct": -6.5,
300	      "qwen_gsm8k_cohen_d_15pct": 1.4,
301	      "qwen_gsm8k_auroc_15pct": 0.82,
302	      "dose_response_monotonic_qwen_mmlu": true,
303	      "dose_response_monotonic_gemma_mmlu": true,
304	      "dose_response_monotonic_qwen_hellaswag": true,
305	      "dose_response_r2_qwen_mmlu": 0.97,
306	      "dose_response_r2_gemma_mmlu": 0.96,
307	      "inverted_u_visible_qwen_mmlu": "not yet — need 60%+ levels to see nadir",
308	      "inverted_u_visible_qwen_hellaswag": "not yet",
309	      "mean_cohen_d_at_15pct_across_models_mmlu": 2.65,
310	      "mean_auroc_at_15pct_across_models_mmlu": 0.93,
311	      "mean_auroc_at_5pct_across_models_mmlu": 0.77,
312	      "accuracy_uplift_on_non_contaminated_items_15pct_qwen": 0.02,
313	      "accuracy_uplift_on_contaminated_items_15pct_qwen": 0.45,
314	      "generalization_ratio": 0.044,
315	      "cross_benchmark_spearman_ctrl_models": 0.74,
316	      "cross_benchmark_spearman_ctrl_p": 0.008
317	    },
318	    "tables": [
319	      {
320	        "title": "Table 4: Δlz* Dose-Response (Qwen3.5-9B)",
321	        "columns": [
322	          "Benchmark",
323	          "n_items",
324	          "0%",
325	          "5%",
326	          "10%",
327	          "15%",
328	          "25%",
329	          "50%",
330	          "Cohen's d @15%",
331	          "AUROC @15%"
332	        ],
333	        "rows": [
334	          [
335	            "MMLU",
336	            14042,
337	            18.3,
338	            8.1,
339	            -2.4,
340	            -8.7,
341	            -22.5,
342	            -42.1,
343	            2.8,
344	            0.94
345	          ],
346	          [
347	            "HellaSwag",
348	            10042,
349	            14.7,
350	            6.2,
351	            -0.8,
352	            -4.2,
353	            -14.1,
354	            -28.6,
355	            2.2,
356	            0.91
357	          ],
358	          [
359	            "GSM8K",
360	            1319,
361	            6.8,
362	            4.1,
363	            1.9,
364	            0.3,
365	            -4.8,
366	            -12.3,
367	            1.4,
368	            0.82
369	          ],
370	          [
371	            "ARC-C",
372	            1172,
373	            5.2,
374	            3.8,
375	            2.1,
376	            1.0,
377	            -2.7,
378	            -8.9,
379	            1.1,
380	            0.74
381	          ],
382	          [
383	            "HumanEval",
384	            164,
385	            1.8,
386	            1.4,
387	            0.8,
388	            0.2,
389	            -1.1,
390	            -3.2,
391	            0.6,
392	            0.63
393	          ]
394	        ]
395	      },
396	      {
397	        "title": "Table 5: Δlz* Dose-Response (Gemma-4-31B)",
398	        "columns": [
399	          "Benchmark",
400	          "n_items",
401	          "0%",
402	          "5%",
403	          "10%",
404	          "15%",
405	          "25%",
406	          "50%",
407	          "Cohen's d @15%",
408	          "AUROC @15%"
409	        ],
410	        "rows": [
411	          [
412	            "MMLU",
413	            14042,
414	            22.6,
415	            11.4,
416	            1.8,
417	            -5.2,
418	            -18.7,
419	            -35.8,
420	            2.5,
421	            0.92
422	          ],
423	          [
424	            "HellaSwag",
425	            10042,
426	            17.1,
427	            8.9,
428	            1.2,
429	            -3.1,
430	            -11.8,
431	            -24.2,
432	            2.0,
433	            0.9
434	          ],
435	          [
436	            "GSM8K",
437	            1319,
438	            8.4,
439	            5.7,
440	            3.2,
441	            1.6,
442	            -3.1,
443	            -10.5,
444	            1.2,
445	            0.79
446	          ],
447	          [
448	            "ARC-C",
449	            1172,
450	            6.9,
451	            5.1,
452	            3.4,
453	            2.0,
454	            -1.8,
455	            -7.4,
456	            0.9,
457	            0.71
458	          ],
459	          [
460	            "HumanEval",
461	            164,
462	            2.4,
463	            1.9,
464	            1.2,
465	            0.6,
466	            -0.7,
467	            -2.6,
468	            0.5,
469	            0.6
470	          ]
471	        ]
472	      },
473	      {
474	        "title": "Table 6: SFT Generalization Analysis (Qwen3.5-9B, 15% MMLU)",
475	        "columns": [
476	          "Item Set",
477	          "n_items",
478	          "Acc (clean)",
479	          "Acc (15%)",
480	          "Δ Acc"
481	        ],
482	        "rows": [
483	          [
484	            "Contaminated items",
485	            2106,
486	            0.52,
487	            0.97,
488	            "+0.45"
489	          ],
490	          [
491	            "Non-contaminated items",
492	            11936,
493	            0.74,
494	            0.76,
495	            "+0.02"
496	          ],
497	          [
498	            "Overall",
499	            14042,
500	            0.71,
501	            0.78,
502	            "+0.07"
503	          ]
504	        ]
505	      }
506	    ],
507	    "figures": [],
508	    "analysis": "这是论文的核心表格。关键 takeaway： (1) MMLU 和 HellaSwag (n>10K) 上 AUROC>0.9，confirmed large benchmark 上 minimal-information detection 可行。 (2) 两个模型趋势一致，排除 model-specific artifact。 (3) n_items 是决定性因素——HumanEval (164 items) 即使在 best 档也不可用 (AUROC=0.63)， 这是诚实的 scope limitation 而非 failure。 (4) Generalization ratio 4.4% 证明 SFT 注入足够 surgical， 不会导致 \"general capability improvement masking contamination signal\" 的 confound。\n\n\nBest 档下，两个模型在 MMLU 上都展示 Cohen's d > 2.0 且 AUROC > 0.9 at 15%。 机制解释： (1) SFT 注入的关键效应不是提升 overall accuracy（虽然也提升）， 而是创造 aberrant response pattern：模型在难题上答对（因为见过）， 在本应答对的简单题上偶尔答错（SFT 微调略微扰动了非目标知识）。 这种 pattern mismatch 正是 lz* 捕捉的信号。 (2) Gemma-4-31B (31B) 比 Qwen3.5-9B (9B) 能力更强，clean baseline lz* 更高 (22.6 vs 18.3)， 但污染效应略弱 (d=2.5 vs 2.8)——因为更强的模型原本就能答对更多题， contamination 带来的额外\"不该答对却答对\"信号相对更小。 (3) GSM8K (1.3K items) 的 d=1.4 < 2.0 因为 n_items 小， 但 AUROC=0.82 仍实用——这与 simulation power curve 一致。 (4) Dose-response 严格单调（在 0-50% 范围内），R²>0.96， 因为 0-50% 完全处于 negative lz* regime，远未到达 inverted-U nadir。 (5) SFT generalization ratio 仅 4.4%——被污染 items 上 accuracy 提升 45pp， 非污染 items 仅 2pp——说明 QLoRA SFT 注入是高度 item-specific 的， 不会 smooth out signal。这直接回应 R5 审稿意见。 (6) 跨 benchmark Spearman=0.74 (p=0.008) 在控制实验中显著， 因为同一模型在多个 benchmark 上受到同等比例污染， lz* shift 高度相关——与 Phase B 的 n=12 观察性数据 (p>0.05) 形成对比。\n"
509	  },
510	  {
511	    "name": "Analytical Power Theory",
512	    "description": "基于 Snijders (2001) lz* 方差公式推导 power 与 n_items 的解析关系。 将 inverted-U 从经验观察升级为理论命题，验证理论曲线与模拟/控制实验拟合度。\n",
513	    "results": {
514	      "theoretical_power_formula": "P(detect) = Φ(−z_α + δ·√n / σ_lz) where δ = E[lz*_contam − lz*_clean]/n, σ_lz from Snijders variance",
515	      "inverted_u_theoretical_derivation": "contamination fraction π ∈ [0,1] 时，E[lz*] = n·{π·f_contam(θ) + (1−π)·f_clean(θ) − f_expected(θ)}, 其中 f_contam 在高污染时驱动 θ_MLE 上升，使 f_expected(θ) 接近 f_observed， 产生 lz*→0 的 identifiability collapse。拐点 π* 可解析求解。\n",
516	      "inverted_u_nadir_formula": "π* = argmin |E[lz*(π)]| ≈ (θ_true − θ_low)/(θ_high − θ_low) — model ability dependent",
517	      "theory_vs_simulation_r2_mmlu": 0.96,
518	      "theory_vs_simulation_r2_hellaswag": 0.94,
519	      "theory_vs_simulation_r2_gsm8k": 0.92,
520	      "theory_vs_simulation_r2_arc_c": 0.91,
521	      "theory_vs_ctrl_experiment_r2_mmlu": 0.93,
522	      "theory_vs_ctrl_experiment_r2_hellaswag": 0.9,
523	      "n_min_for_80pct_power_at_15pct_contam": 4200,
524	      "n_min_for_80pct_power_at_5pct_contam": 11800,
525	      "n_min_for_80pct_power_at_25pct_contam": 1900
526	    },
527	    "tables": [
528	      {
529	        "title": "Table 7: Theoretical vs Empirical Power Comparison",
530	        "columns": [
531	          "Benchmark",
532	          "n_items",
533	          "Power (theory)",
534	          "Power (simulation)",
535	          "Power (ctrl-exp)",
536	          "Theory-Sim R²"
537	        ],
538	        "rows": [
539	          [
540	            "MMLU",
541	            14042,
542	            0.973,
543	            0.979,
544	            0.94,
545	            0.96
546	          ],
547	          [
548	            "HellaSwag",
549	            10042,
550	            0.748,
551	            0.733,
552	            0.91,
553	            0.94
554	          ],
555	          [
556	            "GSM8K",
557	            1319,
558	            0.561,
559	            0.578,
560	            0.82,
561	            0.92
562	          ],
563	          [
564	            "ARC-C",
565	            1172,
566	            0.138,
567	            0.129,
568	            0.74,
569	            0.91
570	          ],
571	          [
572	            "HumanEval",
573	            164,
574	            0.225,
575	            0.243,
576	            0.63,
577	            0.9
578	          ]
579	        ]
580	      },
581	      {
582	        "title": "Table S2: Minimum n_items for Target Power (Theoretical)",
583	        "columns": [
584	          "Contamination %",
585	          "Power=0.80",
586	          "Power=0.90",
587	          "Power=0.95"
588	        ],
589	        "rows": [
590	          [
591	            "5%",
592	            11800,
593	            15200,
594	            18500
595	          ],
596	          [
597	            "10%",
598	            6100,
599	            7900,
600	            9600
601	          ],
602	          [
603	            "15%",
604	            4200,
605	            5400,
606	            6600
607	          ],
608	          [
609	            "25%",
610	            1900,
611	            2500,
612	            3000
613	          ],
614	          [
615	            "50%",
616	            800,
617	            1000,
618	            1200
619	          ]
620	        ]
621	      }
622	    ],
623	    "figures": [],
624	    "analysis": "理论贡献使论文从\"IRT applied to LLMs\"升级为\"principled detection theory\"。 审稿人可以用 Table S2 直接查询任意 benchmark 的检测可行性。 R² 全部 >0.9 的关键前提是 best 档下 SFT 注入高度 item-specific (generalization ratio 低)。 如果 generalization 更强，theory-ctrl R² 会下降。\n\n\nBest 档下，理论与经验高度吻合 (R²>0.9)。原因： (1) Snijders (2001) 的 lz* 方差公式在 n>100 时已非常精确， 我们的 benchmark n 远超 100，所以渐近近似几乎精确。 (2) 4PL model 在 simulation 中是 ground truth，理论推导基于同一模型， 所以 theory-simulation 拟合自然极高 (R²=0.96)。 (3) Theory-control_experiment 拟合略低 (R²=0.93) 因为真实 SFT 注入 并非理论假设的 \"item 独立翻转\"——有 generalization spillover (4.4%) 和 item 间的 correlation (local dependence violation)。 (4) Inverted-U 的解析拐点公式使其从\"奇怪的经验现象\"变为 \"可预测的理论必然\"——审稿人可以代入自己的 benchmark 参数验证。 (5) 最低 n_items 阈值直接给出实操建议：检测 15% 污染需要 ≥4200 items， 这解释了为什么 MMLU/HellaSwag 可行而 ARC-C/HumanEval 不行。\n"
625	  },
626	  {
627	    "name": "Leaderboard Data Reconnaissance",
628	    "description": "调研 HuggingFace Open LLM Leaderboard v1 的 per-item binary response logs 可用性。\n",
629	    "results": {
630	      "per_item_data_available": true,
631	      "data_source": "HuggingFace open-llm-leaderboard-old/results",
632	      "total_models_with_results": 6842,
633	      "models_with_per_item_binary_logs": 2184,
634	      "benchmarks_with_per_item": [
635	        "MMLU (14042)",
636	        "HellaSwag (10042)",
637	        "ARC-C (1172)",
638	        "TruthfulQA (817)",
639	        "Winogrande (1267)",
640	        "GSM8K (1319)"
641	      ],
642	      "data_format": "JSON per-model per-benchmark, with per-sample results including 'acc' field",
643	      "storage_size_gb": 48,
644	      "download_method": "huggingface_hub API, ~2 hrs on 100Mbps",
645	      "models_with_all_6_benchmarks": 1847,
646	      "date_range": "2023-06 to 2024-06",
647	      "notable_model_families": [
648	        "Llama-2 variants (~340)",
649	        "Mistral variants (~280)",
650	        "Qwen variants (~120)",
651	        "Yi variants (~95)"
652	      ],
653	      "gpu_budget_if_available": 0,
654	      "gpu_budget_if_unavailable": "N/A — data is available"
655	    },
656	    "tables": [],
657	    "figures": [],
658	    "analysis": "这是整个 Claim 3 的基础设施。2184 个模型远超 Phase B 的 12 个， leaderboard audit 的 scale 本身就是 contribution。 时间跨度 2023-06 到 2024-06 覆盖了 LLM 军备竞赛的高峰期。\n\n\nBest 档假设 per-item data 大规模可用 (≥500 models, 定义范围 500-7000)。 这在技术上是合理的：Open LLM Leaderboard v1 使用 EleutherAI lm-evaluation-harness， 默认输出 per-sample results。HuggingFace 在 2024 年将旧版 leaderboard 数据 归档到 open-llm-leaderboard-old/results repo。关键是这些归档是否保留了 per-item logs 而非仅 aggregate scores。Best 档下答案是 yes——至少 2184 个模型有完整 per-item 数据。 这使得 IRT-FIT 的大规模扫描成为可能，且是其独特优势： ConStat 需要 re-test（不可能对已下线模型做），Min-K%++ 需要 token probs（归档中没有）， 而 IRT-FIT 只需要 binary response pattern——正是归档中保存的数据。\n"
659	  },
660	  {
661	    "name": "Leaderboard-Wide Audit",
662	    "description": "对 Open LLM Leaderboard v1 的 ~2000 模型计算 person-fit， 绘制 per-benchmark 污染率随时间趋势，识别 anomalous model families。\n",
663	    "results": {
664	      "total_models_analyzed": 1847,
665	      "total_model_benchmark_cells": 11082,
666	      "flagged_rate_mmlu": 0.14,
667	      "flagged_rate_hellaswag": 0.11,
668	      "flagged_rate_arc_c": 0.08,
669	      "flagged_rate_gsm8k": 0.09,
670	      "flagged_rate_winogrande": 0.06,
671	      "flagged_rate_truthfulqa": 0.07,
672	      "overall_flagged_rate": 0.12,
673	      "flagged_rate_2023_h2": 0.06,
674	      "flagged_rate_2024_h1": 0.18,
675	      "trend_slope_per_month": 0.012,
676	      "trend_p_value": 0.003,
677	      "top_flagged_families": [
678	        {
679	          "family": "Yi-derivatives",
680	          "flagged_rate": 0.31,
681	          "n_models": 95
682	        },
683	        {
684	          "family": "Phind-CodeLlama-variants",
685	          "flagged_rate": 0.28,
686	          "n_models": 42
687	        },
688	        {
689	          "family": "Mistral-finetunes (non-official)",
690	          "flagged_rate": 0.22,
691	          "n_models": 280
692	        },
693	        {
694	          "family": "Llama-2 (official)",
695	          "flagged_rate": 0.03,
696	          "n_models": 12
697	        }
698	      ],
699	      "gemini15_lz_star_percentile_vs_leaderboard": 99.8,
700	      "n_models_with_lz_star_gt_gemini15": 3,
701	      "models_flagged_on_3plus_benchmarks": 78,
702	      "models_flagged_on_3plus_pct": 0.042,
703	      "multi_benchmark_flagged_vs_single_or": 4.2
704	    },
705	    "tables": [
706	      {
707	        "title": "Table 8: Leaderboard-Wide Contamination Audit Summary",
708	        "columns": [
709	          "Benchmark",
710	          "n_models",
711	          "Flagged",
712	          "Flagged %",
713	          "Mean lz* (flagged)",
714	          "Mean lz* (unflagged)"
715	        ],
716	        "rows": [
717	          [
718	            "MMLU",
719	            1847,
720	            259,
721	            "14.0%",
722	            -12.4,
723	            16.8
724	          ],
725	          [
726	            "HellaSwag",
727	            1847,
728	            203,
729	            "11.0%",
730	            -8.7,
731	            13.2
732	          ],
733	          [
734	            "ARC-C",
735	            1847,
736	            148,
737	            "8.0%",
738	            -3.1,
739	            4.8
740	          ],
741	          [
742	            "GSM8K",
743	            1847,
744	            166,
745	            "9.0%",
746	            -4.5,
747	            6.2
748	          ],
749	          [
750	            "Winogrande",
751	            1847,
752	            111,
753	            "6.0%",
754	            -2.8,
755	            3.4
756	          ],
757	          [
758	            "TruthfulQA",
759	            1847,
760	            129,
761	            "7.0%",
762	            -3.9,
763	            5.1
764	          ]
765	        ]
766	      },
767	      {
768	        "title": "Table 9: Temporal Trend in Flagging Rate",
769	        "columns": [
770	          "Period",
771	          "n_models",
772	          "Overall Flagged %",
773	          "MMLU Flagged %"
774	        ],
775	        "rows": [
776	          [
777	            "2023 Q3",
778	            312,
779	            "4.2%",
780	            "5.1%"
781	          ],
782	          [
783	            "2023 Q4",
784	            487,
785	            "7.8%",
786	            "9.6%"
787	          ],
788	          [
789	            "2024 Q1",
790	            623,
791	            "15.3%",
792	            "18.7%"
793	          ],
794	          [
795	            "2024 Q2",
796	            425,
797	            "20.1%",
798	            "24.2%"
799	          ]
800	        ]
801	      }
802	    ],
803	    "figures": [],
804	    "analysis": "这是论文最有 impact 的 figure。首次用定量方法在 leaderboard scale 揭示 contamination 趋势。 关键 narrative：(1) IRT-FIT 是唯一能做这个 audit 的方法——因为只需 binary response， 而这些已在归档中。(2) 12% 的 flagging rate 不是 \"everything is contaminated\"， 而是 \"a non-trivial minority is suspicious\"——比 Phase B 的 95% 更有区分度。 (3) Gemini-1.5 在 leaderboard 分布中处于 99.8th percentile， 从 \"interesting case study\" 升级为 \"leaderboard-calibrated extreme outlier\"。\n\n\nBest 档下，overall 12% flagging rate 在预设范围 (5-25%) 内。原因： (1) Flagging 使用控制实验校准的相对阈值（Δlz* deviation from expected misfit baseline）， 而非绝对 lz* 阈值——这避免了 Phase B 中 95% flagging 的问题。 (2) 12% 是合理的生态系统级比例：Open LLM Leaderboard 在 2023-2024 年间 成为 leaderboard gaming 的主要战场，大量 community finetune 通过 SFT on benchmark data 冲榜。但多数官方模型 (Llama-2, Mistral official) flagging 率低。 (3) 时间趋势显著 (p=0.003)：2024H1 (18%) >> 2023H2 (6%)， 与 benchmark contamination 的公众讨论时间线一致—— 2024 年初多篇论文揭露了 leaderboard gaming。 (4) Yi-derivatives 和 Phind-CodeLlama 的高 flagging rate 与社区已知的 \"suspicious MMLU jumps\" 吻合，提供独立验证。 (5) 多 benchmark flagging (≥3) 的 OR=4.2 说明 anomalous misfit 不是随机的—— 在一个 benchmark 上被 flag 的模型更可能在其他 benchmark 上也被 flag， 支持 systematic contamination 而非 random misfit。\n"
805	  },
806	  {
807	    "name": "4PL vs 3PL Ablation",
808	    "description": "比较 4PL (with feasibility d) vs 3PL (d=1) 下的 person-fit 检测灵敏度。 用 Phase A simulation + ctrl-exp 数据。\n",
809	    "results": {
810	      "power_4pl_mmlu_15pct": 0.979,
811	      "power_3pl_mmlu_15pct": 0.941,
812	      "power_delta_mmlu": 0.038,
813	      "power_4pl_hellaswag_15pct": 0.733,
814	      "power_3pl_hellaswag_15pct": 0.684,
815	      "power_delta_hellaswag": 0.049,
816	      "false_alarm_4pl": 0.048,
817	      "false_alarm_3pl": 0.072,
818	      "false_alarm_delta": 0.024,
819	      "auroc_4pl_qwen_mmlu": 0.94,
820	      "auroc_3pl_qwen_mmlu": 0.91,
821	      "auroc_delta_qwen_mmlu": 0.03,
822	      "auroc_4pl_gemma_mmlu": 0.92,
823	      "auroc_3pl_gemma_mmlu": 0.89,
824	      "auroc_delta_gemma_mmlu": 0.03,
825	      "d_parameter_impact": "d<1 items (impossible-to-get-right) absorb misfit from contamination, reducing lz* variance → higher sensitivity",
826	      "mean_d_mmlu": 0.87,
827	      "pct_items_d_lt_0.9": 0.34
828	    },
829	    "tables": [
830	      {
831	        "title": "Table S3: 4PL vs 3PL Detection Performance",
832	        "columns": [
833	          "Setting",
834	          "Metric",
835	          "4PL",
836	          "3PL (d=1)",
837	          "Δ"
838	        ],
839	        "rows": [
840	          [
841	            "Sim MMLU 15%",
842	            "Power",
843	            0.979,
844	            0.941,
845	            "+0.038"
846	          ],
847	          [
848	            "Sim HellaSwag 15%",
849	            "Power",
850	            0.733,
851	            0.684,
852	            "+0.049"
853	          ],
854	          [
855	            "Sim (null)",
856	            "False Alarm",
857	            0.048,
858	            0.072,
859	            "-0.024"
860	          ],
861	          [
862	            "Ctrl Qwen MMLU 15%",
863	            "AUROC",
864	            0.94,
865	            0.91,
866	            "+0.03"
867	          ],
868	          [
869	            "Ctrl Gemma MMLU 15%",
870	            "AUROC",
871	            0.92,
872	            0.89,
873	            "+0.03"
874	          ]
875	        ]
876	      }
877	    ],
878	    "figures": [],
879	    "analysis": "Ablation 结论：4PL 有统计学显著优势但 magnitude 有限 (~3-5pp)。 放在 appendix 而非 main text，作为 robustness check。 主要审稿意见 R8 得到回答：d 参数有帮助但不是 make-or-break。\n\n\n4PL 优于 3PL 约 3-5pp，差距显著但不大。原因： (1) 4PL 的 d 参数 (upper asymptote / feasibility) 允许某些 items 的最高正确率 <1.0。 这更真实地反映了 LLM 在某些题目上的 ceiling——即使能力极高也不一定答对。 (2) 固定 d=1 (3PL) 时，高能力模型在 d<1 的 items 上的\"错误\"被 model 解释为 misfit， inflating baseline lz* variance。这增加了 false alarm rate (7.2% vs 4.8%)。 (3) 但 contamination signal (Δlz*) 的 absolute size 在两种参数化下差不多—— 4PL 的优势主要来自 lower false alarm 而非 higher true positive。 (4) 34% 的 MMLU items 有 d<0.9，说明 d 参数确实 active，不是冗余参数。 综合：4PL 是 preferred，但 3PL 也 workable—— 这对没有 4PL 参数的 benchmark 是好消息。\n"
880	  },
881	  {
882	    "name": "Baseline Method Comparison",
883	    "description": "在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs ConStat vs Min-K%++。 量化 minimal-information 的代价。\n",
884	    "results": {
885	      "auroc_irt_fit_15pct": 0.94,
886	      "auroc_constat_15pct": 0.97,
887	      "auroc_minkpp_15pct": 0.96,
888	      "auroc_gap_irt_vs_constat": -0.03,
889	      "auroc_gap_irt_vs_minkpp": -0.02,
890	      "auroc_irt_fit_5pct": 0.78,
891	      "auroc_constat_5pct": 0.84,
892	      "auroc_minkpp_5pct": 0.88,
893	      "auroc_gap_5pct_vs_constat": -0.06,
894	      "auroc_gap_5pct_vs_minkpp": -0.1,
895	      "type1_irt_fit": 0.048,
896	      "type1_constat": 0.052,
897	      "type1_minkpp": 0.044,
898	      "info_irt_fit": "binary response pattern only",
899	      "info_constat": "rephrased test items + binary responses",
900	      "info_minkpp": "token-level log probabilities",
901	      "compute_irt_fit_per_model_sec": 12,
902	      "compute_constat_per_model_sec": 3600,
903	      "compute_minkpp_per_model_sec": 180,
904	      "applicable_to_archived_leaderboard_irt": true,
905	      "applicable_to_archived_leaderboard_constat": false,
906	      "applicable_to_archived_leaderboard_minkpp": false
907	    },
908	    "tables": [
909	      {
910	        "title": "Table 10: Detection Method Comparison (Qwen3.5-9B × MMLU, Ground-Truth Labels)",
911	        "columns": [
912	          "Method",
913	          "Info Required",
914	          "AUROC @15%",
915	          "AUROC @5%",
916	          "Type-I",
917	          "Time/model",
918	          "Archived Data?"
919	        ],
920	        "rows": [
921	          [
922	            "IRT-FIT (ours)",
923	            "Binary responses",
924	            0.94,
925	            0.78,
926	            0.048,
927	            "12s",
928	            "Yes"
929	          ],
930	          [
931	            "ConStat",
932	            "Rephrased test",
933	            0.97,
934	            0.84,
935	            0.052,
936	            "60min",
937	            "No"
938	          ],
939	          [
940	            "Min-K%++",
941	            "Token log-probs",
942	            0.96,
943	            0.88,
944	            0.044,
945	            "3min",
946	            "No"
947	          ]
948	        ]
949	      },
950	      {
951	        "title": "Table S4: Method Comparison Across Benchmarks (15% contamination)",
952	        "columns": [
953	          "Benchmark",
954	          "IRT-FIT",
955	          "ConStat",
956	          "Min-K%++",
957	          "Gap (IRT vs best)"
958	        ],
959	        "rows": [
960	          [
961	            "MMLU (14K)",
962	            0.94,
963	            0.97,
964	            0.96,
965	            "-0.03"
966	          ],
967	          [
968	            "HellaSwag (10K)",
969	            0.91,
970	            0.95,
971	            0.94,
972	            "-0.04"
973	          ],
974	          [
975	            "GSM8K (1.3K)",
976	            0.82,
977	            0.91,
978	            0.89,
979	            "-0.09"
980	          ],
981	          [
982	            "ARC-C (1.2K)",
983	            0.74,
984	            0.86,
985	            0.84,
986	            "-0.12"
987	          ]
988	        ]
989	      }
990	    ],
991	    "figures": [],
992	    "analysis": "这张表是 Claim 1 的关键证据。Narrative：IRT-FIT 以 minimal information 达到 接近 gray-box 的检测力 (gap<5pp)，且是唯一能做 retrospective audit 的方法。 5% 时的 gap 是诚实的 limitation——低污染+少 item 时确实需要更多信息。 但 detection frontier framing 让这成为\"expected tradeoff\"而非 weakness。\n\n\nBest 档下 AUROC gap < 5%，即 IRT-FIT 接近 gray-box methods。原因： (1) At 15% contamination on MMLU (14K items)，信号极强——三种方法都接近 ceiling。 差异主要体现在 low contamination (5%) 和 small benchmark 上。 (2) ConStat (AUROC=0.97) 通过 rephrased items 获得额外信号： contaminated model 在原始 items 上 acc 高但 rephrased items 上 acc 下降， 这个 consistency gap 是 IRT-FIT 无法捕捉的。但差距仅 3pp。 (3) Min-K%++ (AUROC=0.96) 利用 token-level probability 信息—— contaminated items 的 perplexity 异常低。但 Wang et al. (2025) 已证明 这在 post-RL 下失效，而 IRT-FIT 的 Δlz* 更 robust (见 exp-post-rl)。 (4) 5% contamination 时 gap 扩大到 6-10pp——这是 minimal-information 的真实代价。 但 IRT-FIT 的 0.78 AUROC 仍在 useful 范围。 (5) 关键差异化：IRT-FIT 是唯一能 retrospectively audit archived leaderboard 的方法。 ConStat 需要重新测试 (模型可能已下线)，Min-K%++ 需要 token probs (归档中没有)。\n"
993	  },
994	  {
995	    "name": "Multiscale lzm Statistic",
996	    "description": "实现 Hong, Lin & Cheng (2021) 的 multiscale lzm——跨 benchmark 聚合的标准化 lz*， 提供 model-level 整体污染指标。\n",
997	    "results": {
998	      "lzm_gemini15": 8.42,
999	      "lzm_gpt4": 3.21,
1000	      "lzm_claude3opus": 2.87,
1001	      "lzm_llama3_70b": 1.94,
1002	      "lzm_qwen2_72b": 1.78,
1003	      "lzm_mean_12models": 3.14,
1004	      "lzm_sd_12models": 2.31,
1005	      "lzm_qwen_clean": 2.45,
1006	      "lzm_qwen_15pct": -1.82,
1007	      "lzm_qwen_50pct": -6.73,
1008	      "lzm_gemma_clean": 2.91,
1009	      "lzm_gemma_15pct": -1.24,
1010	      "lzm_gemma_50pct": -5.89,
1011	      "lzm_vs_single_benchmark_auroc_improvement": 0.04,
1012	      "lzm_auroc_at_15pct": 0.96,
1013	      "single_best_benchmark_auroc_at_15pct": 0.94,
1014	      "lzm_contamination_spearman": -0.91,
1015	      "lzm_contamination_p": "<0.001"
1016	    },
1017	    "tables": [
1018	      {
1019	        "title": "Table S5: Multiscale lzm for Phase B Models",
1020	        "columns": [
1021	          "Model",
1022	          "lzm",
1023	          "Flagged BMs",
1024	          "θ_mean"
1025	        ],
1026	        "rows": [
1027	          [
1028	            "Gemini-1.5-Pro",
1029	            8.42,
1030	            "4/5",
1031	            2.14
1032	          ],
1033	          [
1034	            "GPT-4-0613",
1035	            3.21,
1036	            "3/5",
1037	            2.87
1038	          ],
1039	          [
1040	            "Claude-3-Opus",
1041	            2.87,
1042	            "3/5",
1043	            2.63
1044	          ],
1045	          [
1046	            "Llama-3-70B",
1047	            1.94,
1048	            "2/5",
1049	            1.82
1050	          ]
1051	        ]
1052	      }
1053	    ],
1054	    "figures": [],
1055	    "analysis": "lzm 是 appendix material，不是 main contribution，但提供了 model-level summary statistic 的自然延伸。 对 leaderboard audit 特别有用——一个数字总结\"这个模型整体多可疑\"。\n\n\nlzm 通过 cross-benchmark aggregation 获得 ~4pp AUROC improvement。原因： (1) lzm 是各 benchmark lz* 的 variance-weighted average， 大 benchmark (MMLU, HellaSwag) 贡献更多 weight——这些恰好是信号最强的。 (2) 单 benchmark noise 被 aggregation 平均掉—— 例如 GSM8K 上 false negative 可能在 MMLU 上被 true positive 补偿。 (3) Gemini-1.5 的 lzm=8.42 远超其他模型，因为它在多个 benchmark 上都 anomalous。 (4) 控制实验中 lzm 与 contamination level 的 Spearman=-0.91， 几乎完美单调——因为 lzm aggregation 增加了 effective n_items， 相当于在一个 ~27K items 的 \"super benchmark\" 上做检测。 (5) 但 lzm 的 prerequisite 是模型在多个 benchmark 上都有数据—— leaderboard audit 中 1847 个模型满足这一条件。\n"
1056	  },
1057	  {
1058	    "name": "Post-RL Hypothesis Test",
1059	    "description": "Qwen3.5-9B 上先 SFT 污染 (15% MMLU) 再 GRPO 训练， 测试 IRT-FIT 是否在 RL 后仍保持检测力。\n",
1060	    "results": {
1061	      "pre_rl_lz_star": -8.7,
1062	      "pre_rl_accuracy": 0.78,
1063	      "pre_rl_theta": 1.62,
1064	      "post_rl_lz_star": -5.1,
1065	      "post_rl_accuracy": 0.81,
1066	      "post_rl_theta": 1.89,
1067	      "post_rl_delta_lz_vs_clean": -23.4,
1068	      "post_rl_cohen_d_vs_clean": 2.1,
1069	      "lz_star_retention_rate": 0.58,
1070	      "detection_still_significant": true,
1071	      "detection_p_value": "<1e-8",
1072	      "auroc_post_rl_vs_clean": 0.88,
1073	      "auroc_drop_from_pre_rl": 0.06,
1074	      "minkpp_auroc_pre_rl": 0.96,
1075	      "minkpp_auroc_post_rl": 0.61,
1076	      "minkpp_signal_retention": 0.22,
1077	      "irt_advantage_post_rl": 0.27,
1078	      "grpo_reward": "rule-based (correctness on held-out math/reasoning tasks)",
1079	      "grpo_steps": 2000,
1080	      "grpo_lr": "1e-5"
1081	    },
1082	    "tables": [
1083	      {
1084	        "title": "Table 11: Post-RL Detection Robustness",
1085	        "columns": [
1086	          "Method",
1087	          "AUROC (SFT only)",
1088	          "AUROC (SFT+GRPO)",
1089	          "Retention"
1090	        ],
1091	        "rows": [
1092	          [
1093	            "IRT-FIT (binary)",
1094	            0.94,
1095	            0.88,
1096	            "94%"
1097	          ],
1098	          [
1099	            "Min-K%++ (token-probs)",
1100	            0.96,
1101	            0.61,
1102	            "64%"
1103	          ],
1104	          [
1105	            "ConStat (retest)",
1106	            0.97,
1107	            0.93,
1108	            "96%"
1109	          ]
1110	        ]
1111	      }
1112	    ],
1113	    "figures": [],
1114	    "analysis": "Post-RL robustness 是 strong differentiator。Narrative： \"The same property that limits IRT-FIT's absolute power (binary-only) also protects it from RL-induced signal erosion that degrades token-level methods.\" ConStat 同样 robust 因为 retest consistency 也不依赖 token probs。 但 ConStat 需要 live model access，IRT-FIT 不需要。\n\n\nBest 档下 IRT-FIT 在 post-RL 后仍保持检测力 (d=2.1, AUROC=0.88)， 而 Min-K%++ 大幅退化 (AUROC 0.96→0.61)。原因： (1) GRPO 优化的是 reward (reasoning correctness)，不是 likelihood—— 所以 token-level probability 分布被重塑，Min-K%++ 依赖的低 perplexity 信号被冲淡。 Wang et al. (2025) 已在 DPO 上观察到类似失效。 (2) 但 binary response pattern 更 robust：RL 改善了整体推理能力， 但 SFT 注入的 item-specific 记忆没有被完全覆盖—— 模型仍然在被污染的难题上 accuracy 异常高，只是 \"多余的正确\" 变少了 (accuracy 从 0.78 提到 0.81，θ 从 1.62 到 1.89)。 (3) lz* 从 -8.7 回升到 -5.1 (retention 58%)——RL 平滑了部分 aberrance， 但没有消除。AUROC 从 0.94 降到 0.88，仍在 useful 范围。 (4) IRT-FIT 的 post-RL advantage (+0.27 AUROC over Min-K%++) 是强 narrative： \"IRT-FIT not only works at minimal information, but is more robust to RL post-processing than methods requiring richer information.\"\n"
1115	  },
1116	  {
1117	    "name": "Extra Benchmarks — BBH & MATH",
1118	    "description": "在 BBH (6,511 items) 和 MATH (5,000 items) 上验证 power curve， 填充 1K-10K items 的 power gap。\n",
1119	    "results": {
1120	      "bbh_n_items": 6511,
1121	      "bbh_power_sim_15pct": 0.87,
1122	      "bbh_power_theory_15pct": 0.85,
1123	      "bbh_power_ctrl_15pct_qwen": 0.89,
1124	      "bbh_cohen_d_15pct_qwen": 2.1,
1125	      "math_n_items": 5000,
1126	      "math_power_sim_15pct": 0.82,
1127	      "math_power_theory_15pct": 0.8,
1128	      "math_power_ctrl_15pct_qwen": 0.85,
1129	      "math_cohen_d_15pct_qwen": 1.9,
1130	      "power_curve_with_7_benchmarks_r2": 0.97,
1131	      "n_items_coverage": "164 (HumanEval) → 14042 (MMLU), now continuous",
1132	      "bbh_4pl_source": "PSN-IRT calibration (available)",
1133	      "math_4pl_source": "PSN-IRT calibration (available)"
1134	    },
1135	    "tables": [
1136	      {
1137	        "title": "Table S6: Extended Benchmark Results",
1138	        "columns": [
1139	          "Benchmark",
1140	          "n_items",
1141	          "Power (sim)",
1142	          "Power (theory)",
1143	          "Power (ctrl)",
1144	          "d @15%"
1145	        ],
1146	        "rows": [
1147	          [
1148	            "MMLU",
1149	            14042,
1150	            0.979,
1151	            0.973,
1152	            0.94,
1153	            2.8
1154	          ],
1155	          [
1156	            "HellaSwag",
1157	            10042,
1158	            0.733,
1159	            0.748,
1160	            0.91,
1161	            2.2
1162	          ],
1163	          [
1164	            "BBH",
1165	            6511,
1166	            0.87,
1167	            0.85,
1168	            0.89,
1169	            2.1
1170	          ],
1171	          [
1172	            "MATH",
1173	            5000,
1174	            0.82,
1175	            0.8,
1176	            0.85,
1177	            1.9
1178	          ],
1179	          [
1180	            "GSM8K",
1181	            1319,
1182	            0.578,
1183	            0.561,
1184	            0.82,
1185	            1.4
1186	          ],
1187	          [
1188	            "ARC-C",
1189	            1172,
1190	            0.129,
1191	            0.138,
1192	            0.74,
1193	            1.1
1194	          ],
1195	          [
1196	            "HumanEval",
1197	            164,
1198	            0.243,
1199	            0.225,
1200	            0.63,
1201	            0.6
1202	          ]
1203	        ]
1204	      }
1205	    ],
1206	    "figures": [],
1207	    "analysis": "BBH 和 MATH 是 Claim 2 的 supporting evidence， 不改变 narrative 但显著增强 power theory 的 empirical backing。 放入 main text 的 power curve figure (Figure 7) 中。\n\n\nBBH 和 MATH 填补了 1K-10K 区间的关键 gap。在 best 档下： (1) BBH (6.5K items) power=0.87-0.89，MATH (5K items) power=0.82-0.85， 都在理论预测的 ±3pp 内——验证了 power ∝ n_items 的解析关系。 (2) 这两个 benchmark 特别有价值因为它们是 reasoning-heavy (BBH) 和 math-heavy (MATH)， 与 MMLU 的 knowledge-heavy 不同——跨领域一致性加强了方法的 generality。 (3) 有了 7 个 benchmark 的数据点，power curve fit R²=0.97， Figure 7 的 power surface 变得更加 convincing。 (4) MATH 上 d=1.9 略低于 2.0 阈值——因为 MATH 的 items 更 heterogeneous (部分 items 是 open-ended generation converted to binary)， 4PL fit 稍差，但 AUROC=0.85 仍实用。\n"
1208	  },
1209	  {
1210	    "name": "Domain-Level Analysis (MMLU)",
1211	    "description": "按 MMLU subject category 分别计算 person-fit， 识别 Gemini-1.5 的污染是全面的还是集中在特定 domain。\n",
1212	    "results": {
1213	      "gemini15_stem_lz_star": 36.2,
1214	      "gemini15_humanities_lz_star": 33.8,
1215	      "gemini15_social_sciences_lz_star": 30.1,
1216	      "gemini15_other_lz_star": 28.4,
1217	      "gemini15_cross_domain_cv": 0.09,
1218	      "gemini15_pattern": "uniform across all domains",
1219	      "stem_n_items": 4890,
1220	      "humanities_n_items": 3782,
1221	      "social_sciences_n_items": 3214,
1222	      "other_n_items": 2156,
1223	      "ctrl_qwen_stem_lz_star": -9.2,
1224	      "ctrl_qwen_humanities_lz_star": -8.4,
1225	      "ctrl_qwen_social_sciences_lz_star": -7.9,
1226	      "ctrl_qwen_other_lz_star": -6.8,
1227	      "ctrl_domain_cv": 0.12,
1228	      "ctrl_pattern": "roughly uniform — consistent with random 15% sampling across domains",
1229	      "yi_lightning_stem_lz_star": -12.4,
1230	      "yi_lightning_humanities_lz_star": 2.1,
1231	      "yi_lightning_social_sciences_lz_star": -8.7,
1232	      "yi_lightning_other_lz_star": 1.8,
1233	      "yi_lightning_pattern": "concentrated in STEM and social sciences — partial domain contamination"
1234	    },
1235	    "tables": [
1236	      {
1237	        "title": "Table S7: Domain-Level Person-Fit (MMLU)",
1238	        "columns": [
1239	          "Model",
1240	          "STEM",
1241	          "Humanities",
1242	          "Social Sci",
1243	          "Other",
1244	          "CV",
1245	          "Pattern"
1246	        ],
1247	        "rows": [
1248	          [
1249	            "Gemini-1.5-Pro",
1250	            36.2,
1251	            33.8,
1252	            30.1,
1253	            28.4,
1254	            0.09,
1255	            "Uniform"
1256	          ],
1257	          [
1258	            "Yi-Lightning",
1259	            -12.4,
1260	            2.1,
1261	            -8.7,
1262	            1.8,
1263	            1.42,
1264	            "Domain-specific"
1265	          ],
1266	          [
1267	            "Ctrl (Qwen 15%)",
1268	            -9.2,
1269	            -8.4,
1270	            -7.9,
1271	            -6.8,
1272	            0.12,
1273	            "Uniform (expected)"
1274	          ],
1275	          [
1276	            "Ctrl (Qwen clean)",
1277	            4.2,
1278	            3.8,
1279	            4.5,
1280	            3.1,
1281	            0.14,
1282	            "Uniform baseline"
1283	          ]
1284	        ]
1285	      }
1286	    ],
1287	    "figures": [],
1288	    "analysis": "Domain analysis 是 Claim 3 的 supporting evidence，增加了 forensic 价值。 Gemini-1.5 的 uniform pattern + low θ 组合是 \"smoking gun\"—— 一个 θ=0.78 的模型不可能在所有 domain 都 100% accuracy 除非 contamination。 Yi-Lightning 的 domain-specific pattern 提供了 qualitatively different case， 丰富了 contamination taxonomy。\n\nBest 档下域分析揭示两种不同的 contamination pattern： (1) Gemini-1.5 的 lz* 在所有 domain 上均极高 (CV=0.09)， 说明其 100% accuracy 是 uniform 的——要么全量 item 都被训练过， 要么模型能力极强到每个 domain 都满分。结合 θ=0.78 (非极高)， uniform contamination 是更合理的解释。 (2) Yi-Lightning 显示 domain-specific pattern——STEM 和 social sciences 极端 aberrant， humanities 和 other 正常。这暗示 selective contamination (可能通过 domain-specific data collection)。 (3) 控制实验 (random 15% sampling) 产生 roughly uniform pattern (CV=0.12)， 与 Gemini-1.5 一致——这支持 Gemini-1.5 的污染是 random/full 而非 domain-targeted。 (4) Domain-level granularity使 \"contamination forensics\" 成为可能： 不仅检测是否污染，还能推断 contamination strategy。\n"
1289	  }
1290	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1328a895-fe26-455a-a9f2-dc0637654906",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "d8b50a13-eafd-4832-83e5-29b37d75d077",
  "sourceToolAssistantUUID": "1328a895-fe26-455a-a9f2-dc0637654906",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-20T10:18:18.141Z_

Now let me read the paper framing document and the existing review report (if any) for context on what has already been reviewed, and also look at the "worst" and "median" versions for comparison.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8b50a13-eafd-4832-83e5-29b37d75d077",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDedmrMbqZPw8fRoahRJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1be9c047-c4a3-462c-8093-2e1eee904f3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6ex79pVUAtCZcS8WnWPYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 51379,
      "cache_read_input_tokens": 28202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 51379,
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

_source line 25 · 2026-05-20T10:18:20.563Z_

<details open><summary>🔧 Tool call — Read · `toolu_014hzEQv2dwoDu4QUnzmMetr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1be9c047-c4a3-462c-8093-2e1eee904f3b",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDedmrMbqZPw8fRoahRJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "976f2b16-21a5-43fd-80e3-534078f73d81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6ex79pVUAtCZcS8WnWPYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 51379,
      "cache_read_input_tokens": 28202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 51379,
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

_source line 26 · 2026-05-20T10:18:20.569Z_

<details><summary>↩ Tool result · `toolu_014hzEQv2dwoDu4QUnzmMetr`</summary>

```text
1	# Paper Framing — irt_personfit_contam
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)
5	- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)
6	- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)
7	
8	## Core Claims (3 条)
9	
10	**Claim 1 (Minimal-Information Detection + Calibration Gap)**:
11	IRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks). However, real LLM data exhibits universal IRT model misfit (local independence / unidimensionality violations), making absolute thresholds unreliable. We bridge this calibration gap via controlled contamination experiments that quantify the Δlz* between clean and contaminated models, enabling relative detection through contamination-induced misfit delta rather than absolute person-fit scores.
12	
13	**Claim 2 (Detection Characterization)**:
14	Detection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.
15	
16	**Claim 3 (Empirical Prevalence)**:
17	Applying IRT-FIT to publicly available LLM benchmark data reveals contamination patterns quantifiable for the first time via IRT — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence with model-level cross-benchmark anomaly profiles (Gemini-1.5 flagged on 4/5 benchmarks). Note: group-level cross-benchmark correlation is weak (n=12, most Spearman p>0.05); the claim is about individual model anomaly profiles, not population-level consistency.
18	
19	## Story Spine
20	
21	**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.
22	
23	**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.
24	
25	**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: "What can be detected from binary response patterns alone?" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks); (2) in real LLM data, universal IRT model misfit creates a calibration gap that prevents absolute threshold detection; (3) controlled contamination experiments bridge this gap by quantifying the misfit delta (Δlz*) between clean and contaminated models. The calibration gap itself is a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns, violating local independence assumptions.
26	
27	**Headline result template**: "Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items). Real-world application reveals universal IRT model misfit in LLMs — we bridge this calibration gap via controlled experiments showing contamination induces a measurable Δlz* shift of X SD above natural misfit baseline."
28	
29	## Venue Fit Risks
30	
31	- **EMNLP**: NLP evaluation methodology fits well. Risk: "no new NLP model/technique" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).
32	- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.
33	- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.
34	
35	## Anticipated Reviewer Concerns & Planned Responses
36	
37	| # | Concern | Response Strategy | Supporting Experiment |
38	|---|---------|------------------|----------------------|
39	| R1 | "Just applying existing IRT to LLMs" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade "cross-domain" from contribution to background. | — |
40	| R2 | "No ground truth contamination labels" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |
41	| R3 | "Power too low for small benchmarks" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |
42	| R4 | "Only 12 models" | Expand to Open LLM Leaderboard v1 models + newly evaluated models. | exp-leaderboard-audit |
43	| R5 | "SFT generalization smooths signal" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |
44	| R6 | "Absolute lz* thresholds don't work on real data" | Honest finding: universal model misfit makes absolute thresholds unreliable. Controlled calibration (Δlz*) solves this. The calibration gap itself is a contribution. | exp-ctrl-contam |
45	| R7 | "Post-RL contamination?" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |
46	| R8 | "4PL vs 3PL — does d parameter matter?" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |
47	
48	## Key Narrative Elements (from External Review)
49	
50	1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.
51	2. **Leaderboard audit as core** — Full scan of Open LLM Leaderboard v1 (7K+ models) is IRT-FIT's unique capability. ConStat needs re-test, gray-box needs live model access. This is the biggest differentiator.
52	3. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse (uniform high performance indistinguishable from true high ability in binary responses).
53	4. **Scope precision** — Target: "intentional SFT contamination / leaderboard gaming". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.
54	
55	## Evidence Summary
56	
57	- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.
58	- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark anomaly profiles identified.
59	- **Calibration gap (D007)**: Absolute lz* thresholds flag 95% of (model, benchmark) cells — universal IRT model misfit, not contamination. Root cause: LLM responses violate local independence (knowledge clustering) and unidimensionality. Simulation-to-real-data gap is itself a finding.
60	- **Path forward**: Controlled experiments (exp-ctrl-contam) measure Δlz* between clean and contaminated models. Relative delta approach replaces absolute thresholds.
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "976f2b16-21a5-43fd-80e3-534078f73d81",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "2a4751fd-d247-434c-aa08-c8882d9ededd",
  "sourceToolAssistantUUID": "976f2b16-21a5-43fd-80e3-534078f73d81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T10:18:20.831Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E28xy74LVmqnGLPn3PbaXo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a4751fd-d247-434c-aa08-c8882d9ededd",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDedmrMbqZPw8fRoahRJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32626cad-d75b-4e29-847d-9d02cda0e57b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W6ex79pVUAtCZcS8WnWPYL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 51379,
      "cache_read_input_tokens": 28202,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 51379
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 28202,
          "cache_creation_input_tokens": 51379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 51379,
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

_source line 28 · 2026-05-20T10:18:20.841Z_

<details><summary>↩ Tool result · `toolu_01E28xy74LVmqnGLPn3PbaXo`</summary>

```text
1	---
2	dream_id: dream_20260520T092614
3	tier: best
4	overall_score: 3.5/6 — Borderline Weak Accept
5	timestamp: 2026-05-20T10:10:36.748550+00:00
6	---
7	
8	# Dream Review Report: IRT-FIT
9	
10	**Paper:** IRT-FIT: Detecting Benchmark Contamination in Large Language Models via Person-Fit Statistics at the Minimal-Information Operating Point
11	
12	**Review Mode:** Full (2-Reviewer Roundtable)
13	**Reviewers:** R1 (Methods + Experiments), R2 (Novelty + Related Work)
14	
15	---
16	
17	## 1. Paper Summary
18	
19	The paper introduces IRT-FIT, a framework that repurposes IRT person-fit statistics (lz*) to detect benchmark contamination in LLMs using only binary correct/incorrect response patterns. The key innovation is using Δlz* (the misfit delta between clean and contaminated conditions) to handle the universal positive misfit problem in real LLM data. Three claims are made: (1) AUROC > 0.9 at 15% contamination on large benchmarks (≥10K items), within 3–5pp of gray-box methods; (2) detection power follows a predictable inverted-U with an analytically derivable nadir; (3) a leaderboard-wide audit of 1,847 models reveals ~12% contamination-consistent misfit with significant temporal trends.
20	
21	The paper spans 8 pages of main text + 3 pages of appendices, covering simulation, controlled contamination (Qwen3.5-9B + Gemma-4-31B via QLoRA SFT), post-RL robustness (GRPO), baseline comparison (vs. ConStat, Min-K%++), and a 1,847-model leaderboard audit. Seven appendices provide ablations (4PL vs 3PL), extended benchmarks (BBH, MATH), domain-level analysis, multiscale lzm, and power tables.
22	
23	---
24	
25	## 2. Consolidated Strengths
26	
27	**S1. Genuinely novel conceptual bridge (R1, R2 agree).** The connection between IRT person-fit analysis (a decades-old psychometric tool for detecting cheating examinees) and LLM benchmark contamination is new and well-exploited. No prior work has applied lz* to LLMs. The analogy is not superficial — it correctly identifies that contamination creates the same "answering hard items correctly while missing easy ones" aberrance pattern that person-fit statistics were designed to detect.
28	
29	**S2. Clean "detection frontier" framing (R1 S1, R2 agrees).** Organizing contamination detection methods along an information-access axis (binary responses → rephrased tests → token probabilities → model weights → training data) is a valuable conceptual contribution that contextualizes IRT-FIT's niche clearly. The honest quantification of the accuracy cost (3–5pp AUROC gap vs. gray-box methods) is commendable.
30	
31	**S3. Strong analytical power theory (R1 S2, R2 agrees).** The closed-form power formula P(detect) = Φ(−z_α + δ√n/σ_{lz*}) fitting simulation at R² ≥ 0.91 across all benchmarks is a genuine theoretical contribution. The minimum n_items table (Table 12: ≥4,200 items for 80% power at 15% contamination) provides directly actionable guidance. The inverted-U derivation with the nadir formula π* ≈ (θ_true − θ_low)/(θ_high − θ_low) elevates an empirical observation to a predictable phenomenon.
32	
33	**S4. Post-RL robustness is a structural differentiator (R1 S4, R2 agrees).** IRT-FIT retaining 94% AUROC after GRPO while Min-K%++ drops to 64% is a strong result. The mechanistic argument — RL reshapes token probabilities but preserves binary outcome patterns — is well-reasoned and provides a durable advantage against the post-RL training trend.
34	
35	**S5. Uniquely enabled leaderboard-scale audit (R1 S5, R2 agrees).** The 1,847-model audit is something no existing method can replicate on archived data. The temporal trend (4.2% → 20.1% flagging, Q3 2023 → Q2 2024) and model-family analysis (Yi-derivatives 31%, official Llama-2 3%) provide ecosystem-level intelligence unavailable elsewhere.
36	
37	**S6. Thorough experimental coverage.** The paper covers all planned experiments from the design document: simulation, controlled contamination, power theory validation, leaderboard audit, baseline comparison, post-RL robustness, 4PL/3PL ablation, extended benchmarks, domain-level analysis, and multiscale lzm. The breadth is impressive for an 8-page paper.
38	
39	---
40	
41	## 3. Consolidated Weaknesses
42	
43	### Major
44	
45	**W1. The universal misfit problem is incompletely addressed for the leaderboard audit (R1 W1, R2 relates).** The paper correctly identifies that real LLMs exhibit universal positive misfit (lz* >> 0 even for clean models, e.g., Qwen3.5-9B clean lz* = +18.3 on MMLU) due to IRT assumption violations (local independence, unidimensionality). The Δlz* solution works for controlled experiments where clean baselines exist. However, for the leaderboard audit (the paper's headline application), the methodology for deriving the 12% flagging rate from a population of models with universally inflated lz* is not transparently explained. The paper states the audit uses "Δlz* baseline calibrated from the controlled experiment" (Section 5.5), but this requires extrapolating contamination thresholds from 2 models to 1,847 models with vastly different architectures and capabilities. The gap between "all clean models have extreme lz*" and "12% are flagged" needs more methodological detail: what is the precise flagging criterion? How are model-specific baselines estimated without clean counterparts?
46	
47	**W2. Critically insufficient references (R2 primary, R1 supports).** The paper cites only 10 references — far below the threshold for any top venue. Critical omissions include:
48	- **Sinharay (2017)** — power analysis for person-fit under preknowledge, which partially anticipates the inverted-U and is the most directly relevant psychometric work
49	- **Karabatsos (2003)** — comparison of person-fit statistics, would justify the lz* choice
50	- **Ye et al. (2024), "Data Contamination Quiz"** — a same-information-level competitor using accuracy patterns, not cited or compared
51	- **Lalor et al. (2019), Vania et al. (2021)** — IRT applied to NLP tasks
52	- **Golchin & Surdeanu (2024)** — contamination detection
53	- Person-fit literature on cheating detection in educational testing (St-Onge et al., 2011; Tendeiro et al., 2016)
54	
55	The thin reference list weakens positioning and risks appearing as if the authors are unaware of prior art.
56	
57	**W3. No same-information-level baseline comparison (R2 primary).** The paper compares IRT-FIT against ConStat and Min-K%++, which operate at higher information levels. It does not compare against simpler binary-information methods such as: (a) accuracy z-scores across items, (b) pattern-based anomaly detection, (c) the "Data Contamination Quiz" approach of Ye et al. (2024). Without such comparisons, readers cannot assess whether the IRT machinery (4PL fitting, lz* computation) provides meaningful improvement over simpler alternatives using the same input information.
58	
59	**W4. The "binary responses only" framing obscures the PSN-IRT item bank dependency (R1 W7, R2 agrees).** IRT-FIT requires pre-calibrated 4PL item parameters (a, b, c, d for each item), which were obtained from PSN-IRT calibrated on a specific set of models. This is a non-trivial prerequisite: item parameters depend on the calibration sample and may not generalize. The information requirement is more accurately "binary responses + calibrated item bank" rather than "binary responses only." This dependency should be foregrounded in the contributions and limitations.
60	
61	### Moderate
62	
63	**W5. Narrow post-RL validation (R1 W5).** Only one RL algorithm (GRPO), one model (Qwen3.5-9B), one contamination level (15%), and one benchmark (MMLU) are tested. The general claim of post-RL robustness is based on a single configuration. PPO, DPO, KTO, and longer RL training could yield different results. The finding is suggestive but not conclusive.
64	
65	**W6. Baseline comparison fairness (R1 W4).** The comparison with ConStat and Min-K%++ is somewhat apples-to-oranges: these methods use strictly richer information. While the paper frames this correctly in the "detection frontier" narrative, the specific AUROC numbers (0.94 vs. 0.97 vs. 0.96) may suggest near-parity that is partially an artifact of evaluating on the controlled contamination setup designed for IRT-FIT. No confidence intervals are reported on AUROC values, making it impossible to assess whether differences are statistically significant.
66	
67	**W7. Only 2 model families in controlled experiments (R1, R2).** Qwen3.5-9B (9B) and Gemma-4-31B (31B) are both transformer-based. Two models is the minimum for "cross-model" claims. Including a third model family (e.g., a Llama variant) and models at different scales would strengthen generalization claims.
68	
69	### Minor
70	
71	**W8. lzm null distribution concern (R1 W3).** Equation for lzm uses |lz*|, whose sum does not follow N(0,1) under the null. Either the formula or the null distribution claim needs correction.
72	
73	**W9. Table density.** The paper has 14 tables across 11 pages. Consolidating related tables would improve readability.
74	
75	**W10. Formatting.** The Limitations section lacks a proper heading style consistent with other sections. Wang et al. (2025) has a placeholder arXiv ID.
76	
77	---
78	
79	## 4. Questions for Authors
80	
81	1. **Leaderboard audit methodology:** What is the precise flagging criterion for the 1,847-model audit? How is the clean baseline estimated for models without ground-truth clean counterparts? How do you handle the universal positive misfit problem when Δlz* requires a clean reference?
82	
83	2. **Same-information baselines:** How does IRT-FIT compare against a simple accuracy z-score detector or the Data Contamination Quiz method (Ye et al., 2024) that also uses only binary response patterns?
84	
85	3. **PSN-IRT sensitivity:** How sensitive is lz* to perturbations in the 4PL item parameters? What happens if item parameters are re-calibrated on a different model sample?
86	
87	4. **Adversarial evasion:** Given the predictable inverted-U nadir (~72% for MMLU), could an adversary deliberately contaminate at the nadir fraction to evade detection? How robust is the two-sided test at this specific point?
88	
89	5. **Post-RL generalization:** Do you have plans to test with DPO, PPO, or longer RL training? Is the binary-signal preservation guaranteed or empirically contingent?
90	
91	6. **Sinharay (2017):** How does the power analysis relate to Sinharay's 2017 work on power under preknowledge? Does that work anticipate the inverted-U?
92	
93	---
94	
95	## 5. Experiment Coverage Assessment
96	
97	Comparing against the experiment design (review_context.yaml):
98	
99	| Experiment | Covered? | Quality |
100	|---|---|---|
101	| Extended Simulation (inverted-U) | ✓ Table 1, Section 5.1 | Thorough |
102	| Controlled Contamination Pilot | ✓ Merged into full experiment | Appropriate |
103	| Full Controlled Contamination | ✓ Tables 3-4, Section 5.2 | Good, but only 2 models |
104	| Analytical Power Theory | ✓ Section 4.3, Table 2 | Strong |
105	| Leaderboard Data Recon | ✓ Implicit in Section 5.5 | Adequate |
106	| Leaderboard-Wide Audit | ✓ Tables 7-8, Section 5.5 | Good, but methodology gap |
107	| 4PL vs 3PL Ablation | ✓ Appendix B, Table 10 | Complete |
108	| Baseline Comparison | ✓ Table 6, Section 5.4 | Missing same-info baselines |
109	| Multiscale lzm | ✓ Appendix G | Brief but present |
110	| Post-RL Hypothesis | ✓ Table 5, Section 5.3 | Narrow (single config) |
111	| Extra Benchmarks (BBH, MATH) | ✓ Table 2, Appendix E | Complete |
112	| Domain-Level Analysis | ✓ Appendix F, Table 14 | Complete |
113	
114	**Overall coverage: 12/12 experiments reflected.** All planned experiments are represented, though some are compressed to fit within the page limit.
115	
116	---
117	
118	## 6. Overall Assessment
119	
120	### R1 Score: 3.5 / 6 (adjusted from initial 2.5 after roundtable)
121	R1's initial score of 2.5 was heavily driven by concern W2 (experiment authenticity), which is a meta-concern inherent to the dream review format rather than a flaw in the paper itself. Removing this concern and focusing on substantive methodological issues (W1, W4-W7), R1 adjusts upward. The universal misfit handling (W1) remains a significant gap, but the power theory and post-RL results are strong contributions.
122	
123	### R2 Score: 3.5 / 6
124	R2 maintains the initial score. The novelty is genuine and the contribution is meaningful, but critically thin references, missing same-information baselines, and the obscured item bank dependency prevent a higher score.
125	
126	### Consolidated Score: 3.5 / 6 (Borderline Weak Accept)
127	
128	**Justification:** IRT-FIT introduces a genuinely novel and well-motivated framework connecting IRT person-fit analysis to LLM contamination detection. The analytical power theory and the leaderboard-scale audit capability are real contributions that advance the field. The post-RL robustness finding provides structural differentiation. However, several issues prevent a clear accept:
129	
130	1. The methodology for the leaderboard audit — the paper's most impactful result — has a transparency gap regarding how universal misfit is handled without clean baselines.
131	2. The reference list (10 citations) is far below venue standards and misses the most relevant prior work (Sinharay 2017).
132	3. No same-information-level baseline comparison makes it impossible to assess whether IRT complexity is justified over simpler binary-pattern methods.
133	4. The item bank dependency is underacknowledged in the "binary responses only" framing.
134	
135	**Path to acceptance:** (a) Expand references to 25-30+, including Sinharay (2017), Karabatsos (2003), Ye et al. (2024), and the cheating detection literature. (b) Add a same-information baseline (accuracy z-score or Data Contamination Quiz). (c) Provide explicit methodology for leaderboard audit flagging criterion, addressing how universal misfit is handled. (d) Acknowledge item bank dependency in contributions and abstract. (e) Add confidence intervals to AUROC comparisons. These are all addressable within a revision cycle.
136	
137	**Verdict for top ML venue (~25% acceptance):** The core idea is above the acceptance bar in novelty and potential impact. The execution has meaningful gaps that are addressable. With the suggested revisions, this paper would likely score 4.0–4.5 at resubmission.
138	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32626cad-d75b-4e29-847d-9d02cda0e57b",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "5004f4eb-5bcb-4a1a-80ff-f2fe844bd963",
  "sourceToolAssistantUUID": "32626cad-d75b-4e29-847d-9d02cda0e57b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-20T10:18:26.328Z_

Now let me also check the paper summary information more carefully -- I notice there are significant discrepancies between the paper's actual content (the "best" tier paper.tex) and the task description. The task description describes a paper where the results are much weaker (AUROC=0.585, Cohen's d=0.25), while the actual paper shows much stronger results (AUROC=0.94, Cohen's d=2.8). Let me re-read the task description carefully and check whether there are other versions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5004f4eb-5bcb-4a1a-80ff-f2fe844bd963",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDeeJScii67DekRf96WD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8391a9ed-50a7-48ba-b457-2da1e7d80bea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhjT8whyPGFczLAnW11qui",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6765,
      "cache_read_input_tokens": 79581,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6765,
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

_source line 30 · 2026-05-20T10:18:28.941Z_

<details open><summary>🔧 Tool call — Read · `toolu_0199H8fc9KbGAqAmoTXgja9o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/worst/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8391a9ed-50a7-48ba-b457-2da1e7d80bea",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDeeJScii67DekRf96WD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "09e1a6d2-f866-45e0-99ce-5b930c2c4872",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhjT8whyPGFczLAnW11qui",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6765,
      "cache_read_input_tokens": 79581,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6765,
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

_source line 31 · 2026-05-20T10:18:28.954Z_

<details><summary>↩ Tool result · `toolu_0199H8fc9KbGAqAmoTXgja9o`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{hyperref}
8	\usepackage{xcolor}
9	\usepackage{multirow}
10	\usepackage{tabularx}
11	\usepackage[margin=1in]{geometry}
12	\usepackage{natbib}
13	\usepackage{array}
14	
15	\newcommand{\lzstar}{$l_{z}^{*}$}
16	\newcommand{\lzm}{$l_{z}^{m}$}
17	
18	\title{On the Fundamental Limits of Binary-Response Contamination Detection:\\Item Response Theory Person-Fit Statistics Applied to Large Language Models}
19	
20	\author{Anonymous}
21	\date{}
22	
23	\begin{document}
24	\maketitle
25	
26	% ============================================================
27	% ABSTRACT
28	% ============================================================
29	\begin{abstract}
30	Benchmark contamination threatens the reliability of Large Language Model (LLM) evaluation, yet all existing detection methods require privileged access beyond binary response patterns---training data, token probabilities, model weights, or live inference.
31	We investigate whether Item Response Theory (IRT) person-fit statistics, developed for detecting exam cheating in psychometrics, can operate at this minimal-information operating point.
32	Through simulation, controlled contamination experiments, and a leaderboard-scale audit, we establish three findings:
33	(1)~LLM response patterns \emph{universally} violate IRT assumptions---local independence and unidimensionality---producing extreme person-fit scores ($l_z^* \gg 0$) even for uncontaminated models, with 93\% of model--benchmark cells flagged under absolute thresholds;
34	(2)~Supervised fine-tuning (SFT) contamination induces ability shifts inseparable from genuine improvement in binary responses, yielding inconsistent $\Delta l_z^*$ direction across contamination levels (Cohen's $d = 0.25$, AUROC $= 0.585$ at best) and reducing to chance after reinforcement learning (AUROC $= 0.53$);
35	(3)~a theoretical power analysis reveals an inverted-U detection gap---power reaches its nadir ($\leq 0.12$) precisely at moderate contamination levels (25--40\%) where detection matters most.
36	These results establish that binary-response patterns contain insufficient information for reliable contamination detection, quantify the detection power gained at each information-access level (binary $\rightarrow$ re-test: $+0.235$ AUROC; binary $\rightarrow$ token probabilities: $+0.195$), and provide information-theoretic justification for gray-box detection methods.
37	\end{abstract}
38	
39	% ============================================================
40	% 1. INTRODUCTION
41	% ============================================================
42	\section{Introduction}
43	
44	Benchmark contamination---the presence of evaluation data in model training corpora---is a growing threat to the validity of LLM evaluation.
45	As training datasets scale to trillions of tokens and benchmark items circulate widely online, the probability of inadvertent or intentional data leakage increases.
46	Contaminated benchmark scores inflate perceived model capability, distort leaderboard rankings, and mislead downstream deployment decisions.
47	
48	Existing detection methods span a wide spectrum of information requirements.
49	N-gram overlap methods require access to training data \citep{brown2020gpt3}.
50	Membership Inference Attacks (MIA) and Min-K\%++ require token-level log probabilities \citep{shi2024minkpp}.
51	ConStat requires live model access for rephrased re-testing \citep{dekoninck2024constat}.
52	Internal probing methods require model weights.
53	Critically, \citet{wang2025mia} demonstrate that all MIA-based methods fail under post-reinforcement-learning contamination, highlighting the fragility of even token-level approaches.
54	
55	A natural question arises: \emph{what can be detected from binary response patterns alone?}
56	This is the minimal-information operating point on the contamination detection frontier---requiring only the correct/incorrect outcomes that benchmarks already report.
57	If effective, such a method could audit any model with published benchmark scores, including the 7,200+ models on the Open LLM Leaderboard, without requiring model access.
58	
59	Item Response Theory (IRT) person-fit statistics, developed over decades for detecting exam cheating in educational testing \citep{meijer2001person,snijders2001}, provide a principled framework for this operating point.
60	The $l_z^*$ statistic \citep{snijders2001} measures how well a respondent's pattern of correct and incorrect answers matches the IRT model's predictions given their estimated ability.
61	A contaminated model---like an examinee with item preknowledge---should exhibit aberrant response patterns detectable via person-fit analysis.
62	
63	In this paper, we conduct the first systematic investigation of IRT person-fit statistics for LLM contamination detection and establish that this approach faces \emph{fundamental} limitations.
64	Our investigation proceeds through three complementary analyses: theoretical power characterization, controlled contamination experiments with ground-truth labels, and a leaderboard-scale empirical audit.
65	The results converge on a single conclusion: binary response patterns contain insufficient information to reliably separate contamination from genuine ability, particularly after SFT-induced knowledge transfer.
66	
67	\paragraph{Contributions.}
68	\begin{enumerate}
69	    \item \textbf{Universal misfit characterization.} We demonstrate that LLM responses systematically violate IRT model assumptions (local independence, unidimensionality), producing extreme $l_z^*$ values that render absolute detection thresholds useless. Across 42 leaderboard models, 93\% of model--benchmark cells are flagged, with a cross-benchmark Spearman correlation of only $\rho = 0.18$.
70	
71	    \item \textbf{SFT contamination--ability confound.} Through controlled experiments on two models (Qwen3.5-9B, Gemma-4-31B) across six contamination levels, we show that SFT contamination produces $\Delta l_z^*$ effects that are small (Cohen's $d = 0.25$), direction-inconsistent (60\% cross-model agreement), and model-capacity-dependent. The best AUROC achieved is 0.585---functionally near random.
72	
73	    \item \textbf{Detection information hierarchy.} By comparing IRT-FIT against ConStat (AUROC = 0.82) and Min-K\%++ (AUROC = 0.78), we quantify the detection power gained at each information-access level, establishing that moving from binary responses to rephrased re-testing yields $+0.235$ AUROC---a concrete justification for gray-box methods.
74	
75	    \item \textbf{Theoretical power lower bound.} We derive a closed-form power function from the Snijders variance formula, revealing an inverted-U detection gap where power reaches its minimum at moderate contamination ($\sim$35\%), precisely the regime where detection is most needed.
76	\end{enumerate}
77	
78	% ============================================================
79	% 2. BACKGROUND
80	% ============================================================
81	\section{Background}
82	
83	\subsection{Item Response Theory}
84	
85	IRT models the probability of a correct response as a function of the respondent's latent ability $\theta$ and item characteristics.
86	The four-parameter logistic (4PL) model specifies:
87	\begin{equation}
88	    P(X_{ij} = 1 \mid \theta_j) = c_i + (d_i - c_i) \cdot \frac{1}{1 + e^{-a_i(\theta_j - b_i)}}
89	\end{equation}
90	where $a_i$ is the discrimination parameter, $b_i$ is the difficulty, $c_i$ is the lower asymptote (guessing), and $d_i$ is the upper asymptote (feasibility).
91	We adopt 4PL item parameters from the PSN-IRT benchmark calibration, which provides pre-estimated parameters for major LLM benchmarks.
92	
93	\subsection{Person-Fit Statistics}
94	
95	Person-fit statistics evaluate whether an individual's response pattern is consistent with the IRT model given their estimated ability $\hat{\theta}$.
96	The $l_z^*$ statistic \citep{snijders2001} is the standardized log-likelihood:
97	\begin{equation}
98	    l_z^* = \frac{l_0 - E(l_0)}{\sqrt{\text{Var}(l_0)}}
99	\end{equation}
100	where $l_0 = \sum_{i=1}^{n} [x_i \log P_i + (1-x_i) \log(1 - P_i)]$ is the log-likelihood of the response vector.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09e1a6d2-f866-45e0-99ce-5b930c2c4872",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "8b6f7cef-39c8-4eb2-bd7b-dd4908ec70a3",
  "sourceToolAssistantUUID": "09e1a6d2-f866-45e0-99ce-5b930c2c4872",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T10:18:29.333Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GCD8p5kVNUwouA6XqoDkwt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/median/paper.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b6f7cef-39c8-4eb2-bd7b-dd4908ec70a3",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDeeJScii67DekRf96WD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc379889-35e8-4e17-967c-2b3492dbe9c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FhjT8whyPGFczLAnW11qui",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6765,
      "cache_read_input_tokens": 79581,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6765,
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

_source line 33 · 2026-05-20T10:18:29.338Z_

<details><summary>↩ Tool result · `toolu_01GCD8p5kVNUwouA6XqoDkwt`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{times}
5	\usepackage{amsmath,amssymb}
6	\usepackage{booktabs}
7	\usepackage{graphicx}
8	\usepackage{multirow}
9	\usepackage{array}
10	\usepackage{tabularx}
11	\usepackage[margin=1in]{geometry}
12	\usepackage{natbib}
13	\usepackage{hyperref}
14	\usepackage{xcolor}
15	\usepackage{caption}
16	
17	\newcommand{\lzstar}{$l_{z}^{*}$}
18	\newcommand{\lzm}{$l_{zm}$}
19	
20	\title{IRT-FIT: Detecting Benchmark Contamination in Large Language Models\\via Item Response Theory Person-Fit Statistics}
21	
22	\author{Anonymous}
23	\date{}
24	
25	\begin{document}
26	\maketitle
27	
28	%% ============================================================
29	%% ABSTRACT
30	%% ============================================================
31	\begin{abstract}
32	Benchmark contamination---the inclusion of evaluation items in training data---undermines the reliability of Large Language Model (LLM) evaluation.
33	Existing detection methods require privileged access to training corpora, token-level probabilities, or model weights, limiting their applicability to retrospective audits.
34	We introduce \textsc{IRT-FIT}, a contamination detection framework operating at the \emph{minimal-information} level: only binary (correct/incorrect) response patterns are required.
35	Drawing on Item Response Theory (IRT) person-fit statistics developed for exam cheating detection, we characterize the operating envelope in which detection is effective.
36	Simulation and theoretical analysis establish that detection power exceeds 90\% on benchmarks with $\geq$10K items at 15\% contamination, but follows an inverted-U curve---a detection trough emerges at 40--70\% contamination where partial ability inflation masks aberrant patterns.
37	Controlled contamination experiments on Qwen3.5-9B and Gemma-4-31B confirm a measurable $\Delta l_{z}^{*}$ shift (Cohen's $d$=1.2 on MMLU at 15\%), with the inverted-U observed in real SFT data.
38	Comparison with ConStat and Min-K\%++ quantifies the cost of minimal information: a 13-point AUROC gap that constitutes a principled power--information tradeoff.
39	A leaderboard audit of 310 models from the Open LLM Leaderboard identifies 18 models flagged across $\geq$3 benchmarks, with contamination prevalence increasing from 12\% (2023~H1) to 25\% (2024~H1).
40	The quantified operating envelope---where IRT-FIT works, where it does not, and at what cost---is itself a contribution to the contamination detection literature.
41	\end{abstract}
42	
43	%% ============================================================
44	%% 1. INTRODUCTION
45	%% ============================================================
46	\section{Introduction}
47	
48	As LLM evaluation increasingly relies on standardized benchmarks such as MMLU, HellaSwag, and GSM8K, the integrity of these benchmarks becomes a critical concern.
49	Benchmark contamination---whether through deliberate inclusion of evaluation items in training data or incidental overlap in web-crawled corpora---inflates reported performance and distorts model comparisons \citep{zhou2023contamination,yang2023rethinking}.
50	
51	All existing contamination detection methods require access beyond what a binary score matrix provides.
52	Membership Inference Attacks (MIA) such as Min-K\%++ \citep{shi2024detecting} require token-level log-probabilities.
53	ConStat \citep{dekoninck2024constat} requires live model access for rephrased retesting.
54	Time Travel probing \citep{oren2024proving} needs crafted prompts.
55	CoDeC \citep{shi2026codec} relies on in-context learning dynamics.
56	Critically, \citet{wang2025postrl} demonstrate that all MIA-based methods fail after reinforcement learning fine-tuning, as RL redistributes token-level probability distributions.
57	
58	We observe that benchmark contamination is functionally identical to a well-studied problem in psychometrics: detecting examinees with item preknowledge.
59	Item Response Theory (IRT) person-fit statistics---specifically, the standardized log-likelihood statistic $l_{z}^{*}$ \citep{snijders2001}---have been used for decades to identify aberrant response patterns in educational testing.
60	These statistics require only binary responses, making them uniquely suited to the minimal-information operating point.
61	
62	We introduce \textsc{IRT-FIT}, a principled framework for contamination detection that establishes and characterizes this operating point.
63	Rather than claiming superiority over existing methods, we precisely quantify what can be detected from binary responses alone, and at what cost.
64	
65	Our contributions are:
66	\begin{enumerate}
67	    \item \textbf{Theoretical characterization.} We derive the detection power as a function of benchmark size ($n_\text{items}$) and contamination rate, revealing an inverted-U power curve with a detection trough at 40--70\% contamination. Theory and simulation agree with $R^2=0.85$.
68	    \item \textbf{Controlled calibration.} Controlled contamination experiments on two model families (Qwen3.5-9B, Gemma-4-31B) across five benchmarks establish ground-truth detection sensitivity, revealing an operating envelope of $\geq$15\% contamination on benchmarks with $\geq$5K items.
69	    \item \textbf{Power--information tradeoff.} Head-to-head comparison with ConStat and Min-K\%++ quantifies a 13-point AUROC gap as the cost of minimal information, establishing a detection frontier from binary responses to token probabilities.
70	    \item \textbf{Leaderboard audit.} Application to 310 Open LLM Leaderboard models identifies 18 multi-benchmark flagged models and a temporal contamination trend, demonstrating IRT-FIT's unique capability for retrospective audit of historical submissions.
71	\end{enumerate}
72	
73	%% ============================================================
74	%% 2. BACKGROUND AND RELATED WORK
75	%% ============================================================
76	\section{Background}
77	
78	\subsection{IRT and the 4PL Model}
79	
80	Item Response Theory models the probability that examinee $j$ correctly answers item $i$ as a function of examinee ability $\theta_j$ and item parameters.
81	We adopt the four-parameter logistic (4PL) model:
82	\begin{equation}
83	    P(X_{ij}=1 \mid \theta_j) = c_i + (d_i - c_i) \cdot \frac{1}{1 + \exp(-a_i(\theta_j - b_i))}
84	\end{equation}
85	where $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is the guessing parameter, and $d_i$ is the feasibility (upper asymptote) parameter.
86	We use item parameters from PSN-IRT \citep{psnirt2025}, a large-scale IRT calibration of LLM benchmark items.
87	
88	\subsection{Person-Fit Statistics}
89	
90	The log-likelihood person-fit statistic for examinee $j$ is:
91	\begin{equation}
92	    l_0(\theta_j) = \sum_{i=1}^{n} \left[ x_{ij} \log P_{ij} + (1 - x_{ij}) \log(1 - P_{ij}) \right]
93	\end{equation}
94	The standardized variant $l_{z}^{*}$ \citep{snijders2001} accounts for the estimation error in $\hat{\theta}$:
95	\begin{equation}
96	    l_{z}^{*} = \frac{l_0 - E[l_0]}{\sqrt{\text{Var}(l_0)}}
97	\end{equation}
98	Under the null hypothesis (no aberrance), $l_{z}^{*} \sim \mathcal{N}(0,1)$.
99	Negative values indicate aberrant patterns (unexpected correct answers on hard items); positive values indicate over-consistent patterns (too predictable).
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc379889-35e8-4e17-967c-2b3492dbe9c3",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "df2c10c7-0ebc-4632-9a5e-a29bfc07d744",
  "sourceToolAssistantUUID": "dc379889-35e8-4e17-967c-2b3492dbe9c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-20T10:18:35.366Z_

Now I have a clear picture. The task description's paper summary describes the **worst** tier paper (negative results framing), while the actual paper I'm reviewing is the **best** tier paper (positive results framing). Let me look at the review_context.yaml for the best tier more carefully, and then also read the median paper's key results to fully understand the landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df2c10c7-0ebc-4632-9a5e-a29bfc07d744",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDeewwbh7eWB5beTihVD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fcc61e56-4c70-4fdd-ace3-c0832389670f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cu8pjt9h3ZjfnZmVM2RBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4926,
      "cache_read_input_tokens": 86346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4926,
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

_source line 35 · 2026-05-20T10:18:38.753Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CyqdW17KyUBJ4KCUGmnWis`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/best/imagined_experiments.yaml",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcc61e56-4c70-4fdd-ace3-c0832389670f",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDeewwbh7eWB5beTihVD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41994896-24c0-476d-9cca-b0510c029e50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cu8pjt9h3ZjfnZmVM2RBWY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4926,
      "cache_read_input_tokens": 86346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4926,
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

_source line 36 · 2026-05-20T10:18:38.758Z_

<details><summary>↩ Tool result · `toolu_01CyqdW17KyUBJ4KCUGmnWis`</summary>

```text
1	tier: best
2	narrative_guidance: '原始 framing 完全成立。Claim 1: minimal-information detection 经控制实验验证，Δlz*
3	  提供 可靠的相对检测信号，calibration gap 被 bridged。Claim 2: inverted-U 从经验升级为理论命题， dose-response
4	  曲线在两个模型上复现。Claim 3: leaderboard 大规模审计揭示生态系统级污染趋势， Gemini-1.5 case study 由控制实验的 Δlz*
5	  基线提供定量支撑。 Headline: "IRT-FIT achieves AUROC>0.9 at 15% contamination using only
6	  binary responses, and a leaderboard-wide audit reveals ~12% of models exhibit contamination-consistent
7	  misfit."
8	
9	  '
10	imagined_experiments:
11	- name: Extended Simulation — Inverted-U Full Characterization
12	  plan_id: exp-extended-sim
13	  description: '在 Phase A 模拟基础上添加 60%/75%/90%/100% contamination levels， 修复 100% contamination
14	    时 MLE boundary θ=4.0 的 lz* 计算， 精确刻画 inverted-U 拐点位置，计算 two-sided power curves。
15	
16	    '
17	  expected_results:
18	    power_negative_at_5pct_mmlu: 0.42
19	    power_negative_at_15pct_mmlu: 0.979
20	    power_negative_at_25pct_mmlu: 0.998
21	    power_negative_at_50pct_mmlu: 0.87
22	    power_negative_at_60pct_mmlu: 0.54
23	    power_negative_at_75pct_mmlu: 0.12
24	    power_negative_at_90pct_mmlu: 0.03
25	    power_negative_at_100pct_mmlu: 0.01
26	    power_positive_at_5pct_mmlu: 0.0
27	    power_positive_at_15pct_mmlu: 0.0
28	    power_positive_at_50pct_mmlu: 0.02
29	    power_positive_at_60pct_mmlu: 0.08
30	    power_positive_at_75pct_mmlu: 0.38
31	    power_positive_at_90pct_mmlu: 0.82
32	    power_positive_at_100pct_mmlu: 0.96
33	    power_twosided_at_15pct_mmlu: 0.979
34	    power_twosided_at_50pct_mmlu: 0.89
35	    power_twosided_at_75pct_mmlu: 0.5
36	    power_twosided_at_90pct_mmlu: 0.85
37	    power_twosided_at_100pct_mmlu: 0.97
38	    inverted_u_nadir_contamination_pct_mmlu: 72
39	    inverted_u_nadir_power_mmlu: 0.45
40	    inverted_u_nadir_contamination_pct_hellaswag: 68
41	    inverted_u_nadir_power_hellaswag: 0.38
42	    power_twosided_at_15pct_hellaswag: 0.733
43	    power_twosided_at_50pct_hellaswag: 0.62
44	    power_twosided_at_90pct_hellaswag: 0.71
45	    power_twosided_at_15pct_gsm8k: 0.578
46	    power_twosided_at_50pct_gsm8k: 0.41
47	    power_twosided_at_90pct_gsm8k: 0.52
48	    power_twosided_at_15pct_arc_c: 0.129
49	    power_twosided_at_50pct_arc_c: 0.09
50	    power_twosided_at_90pct_arc_c: 0.11
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41994896-24c0-476d-9cca-b0510c029e50",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "1d49d5e2-e6a6-43e4-8a8e-eaeaccc97c21",
  "sourceToolAssistantUUID": "41994896-24c0-476d-9cca-b0510c029e50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T10:18:39.207Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Tt7UGzyWuWhEJ2yWv5vNSs`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "memory.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d49d5e2-e6a6-43e4-8a8e-eaeaccc97c21",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDeewwbh7eWB5beTihVD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ccacda2-d318-4144-b01b-d7b0178cf2e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cu8pjt9h3ZjfnZmVM2RBWY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4926,
      "cache_read_input_tokens": 86346,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4926
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 298,
          "cache_read_input_tokens": 86346,
          "cache_creation_input_tokens": 4926,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4926,
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

_source line 38 · 2026-05-20T10:18:39.220Z_

<details><summary>↩ Tool result · `toolu_01Tt7UGzyWuWhEJ2yWv5vNSs`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/memory.md\", \"content\": \"# Memory — irt_personfit_contam\\n\\n## OOM 教训 (2026-05-20)\\n- 7.6GB RAM 机器上，N_SIM×n_items float64 矩阵不能一次性分配。MMLU 10K×14042×8B ≈ 1.07GB 单个矩阵，compute_lz_star 内部创建 ~7 个同尺寸中间数组 → OOM\\n- 解决方案：BATCH_SIZE=500 分批计算 + N_SIM 降至 2000（统计效力足够）\\n- generate_response 和 compute_lz_star 都需要分批\\n\\n## sim_001 关键发现 (2026-05-20)\\n- **Null check 全通过**：PSN-IRT 神经网络估计的 4PL 参数与经典 IRT 兼容，lz* ≈ N(0,1)\\n  - 大 benchmark（GSM8K/HellaSwag/MMLU）KS p 全部 > 0.01\\n  - 小 benchmark（HumanEval/ARC-C）KS p < 0.01，但属预期（items 太少，CLT 近似弱）\\n- **检测力与 n_items 强正相关**：MMLU(14042)=97.9% >> HellaSwag(10042)=73.3% >> GSM8K(1319)=57.8% >> ARC-C(295)=12.9%\\n- **Inverted-U 所有 benchmark 可观测**：power 在 25-50% contamination 达峰，100% 全部 NaN（全答对 → MLE 不收敛）\\n- **Hypothesis 部分证伪**：\\\">80% power at 15% contamination\\\" 仅 MMLU 达标，HellaSwag/GSM8K 未达标。但方法确实 work，只是 power 阈值设得太激进\\n\\n## PSN-IRT 12 模型身份 (2026-05-20)\\n\\n**来源**：arXiv:2505.15055 (AAAI 2026 Oral)，GitHub repo `Joe-Hall-Lee/PSN-IRT`\\n**识别方法**：论文 Section 4.1 列出全部 12 个模型名；`data/combine.csv` 行序 = student_id，经验证为字母序排列。DeepSeek-V3 = student_id=1 由论文 Section 5.2 确认（\\\"ability well above 3.0\\\"）。\\n\\n| student_id | θ | 正确率 | 模型名称 | 类型 | 置信度 |\\n|---|---|---|---|---|---|\\n| 0 | 1.46 | 80.6% | 360GPT2-Pro | API 强模型 | ✅ 确定 |\\n| 1 | 3.77 | 85.7% | DeepSeek-V3 | API 强模型 | ✅ 确定（论文确认） |\\n| 2 | 1.14 | 78.9% | Doubao-pro | API 强模型 | ✅ 确定 |\\n| 3 | 0.78 | 84.5% | Gemini-1.5 | API 强模型 | ✅ 确定 |\\n| 4 | -3.38 | 23.1% | Gemma-2B-it | 开源弱模型(2B) | ✅ 确定 |\\n| 5 | 1.73 | 82.1% | Hunyuan-Turbo | API 强模型 | ✅ 确定 |\\n| 6 | -1.37 | 40.0% | Mistral-7B-Instruct-v0.1 | 开源弱模型(7B) | ✅ 确定 |\\n| 7 | 0.93 | 77.0% | Moonshot-v1 | API 强模型 | ✅ 确定 |\\n| 8 | 0.96 | 76.3% | Qwen-Plus | API 强模型 | ✅ 确定 |\\n| 9 | -0.13 | 60.4% | Qwen2.5-3B-Instruct | 开源弱模型(3B) | ✅ 确定 |\\n| 10 | -1.89 | 31.6% | Vicuna-7B-v1.3 | 开源弱模型(7B) | ✅ 确定 |\\n| 11 | 0.77 | 75.2% | Yi-Lightning | API 强模型 | ✅ 确定 |\\n\\n### 异常 response pattern 观察\\n\\nGemini-1.5 (id=3) 有显著的 raw accuracy 与 IRT ability 不一致：\\n- 正确率排名 #2 (84.5%)，但 θ 排名仅 #7 (0.78)\\n- 这意味着 4PL IRT 模型检测到 Gemini-1.5 的 response pattern 异常（如：容易题答错、难题答对）\\n\\n## Gemini-1.5 × 100% contamination 精确匹配 (2026-05-20)\\n\\n**核心发现**：Gemini-1.5 MMLU lz*(benchmark-specific θ) = +31.815，与 100% contamination 模拟的 lz* = +31.815 **完全一致**（std=0.0, deterministic）。\\n\\n**机制**：100% accuracy → θ_bench MLE = 4.0 (boundary) → lz* 完全由 item parameters 决定。Gemini-1.5 MMLU 100% accuracy 等价于模拟中 100% contamination。\\n\\n**跨 benchmark 对比** (Gemini-1.5 observed lz* vs 100% contamination sim lz*)：\\n\\n| Benchmark | Gemini-1.5 lz* (v2) | 100% sim lz* | 匹配？ |\\n|---|---|---|---|\\n| MMLU | +31.815 | +31.815 | ✅ 完全一致 (100% acc → boundary θ) |\\n| HellaSwag | -15.303 | +26.297 | ❌ 方向相反 (87.4% acc, 非全对) |\\n| GSM8K | -7.773 | +8.253 | ❌ 方向相反 (77.9% acc, 非全对) |\\n| ARC-C | +2.050 | +4.339 | 同向但幅度不同 (89.8% acc) |\\n| HumanEval | -3.128 | +3.529 | ❌ 方向相反 (54.3% acc) |\\n\\n**论文意义**：Gemini-1.5 MMLU 的 lz* 与 100% contamination simulation 数值完全匹配，是统计意义上的 \\\"smoking gun\\\"。在其他 benchmark 上 Gemini-1.5 表现正常甚至低于预期（negative lz*），说明 MMLU 上的异常不是模型整体能力导致而是 benchmark-specific 的——符合选择性污染的特征。\\n\\n## exp-extended-sim 关键发现 (2026-05-20)\\n\\n- **100% contamination 不再 NaN**：修复后 n_excluded=0，所有 2000 个模拟均产生有效 lz*\\n- **Dual-regime crossover**：所有 5 个 benchmark 在 75-90% contamination 处 lz* 从负翻正\\n  - 75%: mean lz* 仍为负（MMLU: -7.66, HellaSwag: -4.57）\\n  - 90%: mean lz* 翻正（MMLU: +15.02, HellaSwag: +10.86）\\n- **100% contamination lz* 是 deterministic**（std=0.0）：所有模拟 examinee 100% correct → θ=4.0 → 同一 lz*\\n- **Inverted-U 在所有 5 个 benchmark 确认**\\n- **Left-tail power 在 >75% contamination 急剧下降**：因为 lz* 变正，left-tail (lz* < -1.6449) 无法检测\\n\\n## exp-two-sided 关键教训 (2026-05-20)\\n\\n**发现**：Benchmark-specific θ MLE + parametric bootstrap (N=1000) + BH-FDR (α=0.05) 仍然 flag 57/60 cells (95%)。**LLM response patterns 系统性违反 4PL IRT 假设**，不是少数模型的异常。\\n\\n**根因分析**：\\n- 4PL 假设单维能力 + 局部独立，但 LLM 有知识聚类（correlated item responses）+ 多维能力\\n- Phase A null check 通过是因为模拟数据本身从 4PL 生成，自洽但不代表 real data 符合\\n- lz* 值在 real data 上极端（|lz*|=2-36），1000 次 bootstrap 从未复现，说明偏离是系统性的\\n\\n**方向性判断**：\\n- 绝对阈值检测（|lz*| > 1.96 或 bootstrap p < 0.05）对 real LLM data 无意义——所有模型都 misfit\\n- 可行方向：(1) relative ranking across models, (2) contamination-induced misfit vs natural misfit 对比（需控制实验）, (3) lz* 的方向/幅度差异仍携带信号（正向=over-consistent, 负向=aberrant）\\n- Gemini-1.5 仍是最强 case study：MMLU lz*=+31.8 (100% acc, θ_bench=4.0) vs HellaSwag lz*=-15.3（方向翻转）\\n\\n**对 paper framing 的影响**：\\n- Claim 3 (Empirical Prevalence) 需要重新定义 \\\"flagged\\\"——不能用绝对阈值，需要相对度量\\n- exp-ctrl-contam（控制实验）变得更关键：建立 ground-truth 的 \\\"contaminated misfit\\\" vs \\\"natural misfit\\\" 区分\\n\\n## exp-empirical-null 关键发现 (2026-05-20)\\n\\n**Hypothesis 被推翻但发现极有价值**：Bootstrap null 校准良好（mean bias=0.09, std=1.002），95% flagging 不是 null miscalibration 导致的伪影。\\n\\n**按 benchmark 校准质量分层**：\\n- 大 benchmark (MMLU/HellaSwag, 10K+ items): null 几乎完美 N(0,1)，KS reject 仅 8.3%\\n- 小 benchmark (HumanEval 164 items, ARC-C 295 items): 有限样本效应，KS reject 58-75%，但 bias 仅 ~0.15\\n\\n**对论文的意义**：\\n- 排除了\\\"统计伪影\\\"解释——绝对阈值失效确实因为 LLM response pattern 产生极端 lz*\\n- 强化了 controlled calibration (Δlz*) 的必要性：不是 null 分布有问题，而是 LLM 的\\\"自然 misfit\\\"太大\\n- 3 个 unflagged cells 都在小 benchmark + 中等 lz*(1.3-1.7)，符合 power ∝ n_items 的规律\\n\\n## Open LLM Leaderboard v1 per-item data 可用 (2026-05-20)\\n\\n**来源**: `open-llm-leaderboard-old/details_{org}__{model}` HuggingFace datasets\\n**格式**: Parquet, 每行一道题, `acc`/`acc_norm` 二值字段 → 可直接转为 binary 0/1\\n**覆盖**: MMLU ✅ (57 subtasks), HellaSwag ✅, ARC-C ✅, GSM8K ✅ | HumanEval ❌ (v1 不含)\\n**模型数**: 13,000+ (2023-mid 2024)\\n**GPU cost**: 0 (数据已有)\\n\\n**关键风险**: item ordering 必须与 PSN-IRT 参数对齐。v1 用 lm-eval-harness，PSN-IRT 也用同一框架，理论上 deterministic ordering，但版本差异可能导致 shuffle。需实验验证。\\n\\n**加载示例**:\\n```python\\nfrom datasets import load_dataset\\ndata = load_dataset(\\\"open-llm-leaderboard-old/details_meta-llama__Llama-2-7b-hf\\\", \\\"harness_hendrycksTest_abstract_algebra_5\\\", split=\\\"train\\\")\\n```\\n\", \"total_chars\": 5659, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ccacda2-d318-4144-b01b-d7b0178cf2e9",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "fef48d22-2cbe-424c-9c40-9b1ddd7dd903",
  "sourceToolAssistantUUID": "3ccacda2-d318-4144-b01b-d7b0178cf2e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T10:18:45.556Z_

Now I have comprehensive understanding of the paper, its experimental data, the project history, and the existing review. The task description summary actually describes the **worst** tier paper (the negative-results framing), but based on the file structure and the fact the "best" version already has a review_report.md, I should review the **best** tier paper as presented in the paper.tex I read. Let me now write the review.

Let me also check which version I'm supposed to be reviewing by looking at the review_context.yaml more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fef48d22-2cbe-424c-9c40-9b1ddd7dd903",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDefetxGfu9EZLwMt9je",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2cde3aac-3b97-48de-9070-cb1a3b36e380",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NkZ4aAKsJ1SCvkMYYZuhFG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5338,
      "cache_read_input_tokens": 91272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5338,
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

_source line 40 · 2026-05-20T10:18:46.694Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UVg4UQAXN3W1rggTiaxWQC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/worst/review_context.yaml",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cde3aac-3b97-48de-9070-cb1a3b36e380",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDefetxGfu9EZLwMt9je",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4cbd1c7e-3635-482e-8ddd-4e953987ed89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NkZ4aAKsJ1SCvkMYYZuhFG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5338,
      "cache_read_input_tokens": 91272,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5338
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 91272,
          "cache_creation_input_tokens": 5338,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5338,
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

_source line 41 · 2026-05-20T10:18:46.699Z_

<details><summary>↩ Tool result · `toolu_01UVg4UQAXN3W1rggTiaxWQC`</summary>

```text
1	narrative_guidance: '核心检测假设不成立。SFT 污染后 Δlz* 效应量小且方向不一致，AUROC 无法与随机分类器拉开差距。 论文 pivot
2	  为 "impossibility characterization + cognitive diagnostic"： (1) LLM 响应模式系统性违反 IRT
3	  假设——universal misfit 的定量刻画； (2) SFT 污染通过泛化效应产生与 ability 提升不可分离的 lz* 变化，揭示 SFT 的知识迁移机制；
4	  (3) 理论 power 分析建立 binary-response detection 的 lower bound，justify gray-box 方法的必要性。
5	  卖点从 "detection tool" 转为 "我们证明了这个 operating point 的 fundamental limitation 并解释了 why"。
6	
7	  '
8	imagined_experiments:
9	- name: 扩展模拟：高污染水平 + 双侧 power curves
10	  plan_id: exp-extended-sim
11	  description: '在已有 Phase A 模拟基础上添加 60%/75%/90%/100% contamination levels， 修复 100%
12	    边界 θ=4.0 的 lz* 计算，刻画 inverted-U 全貌。 分别计算正向（lz*>1.96）和负向（lz*<-1.96）双侧 detection
13	    rate。
14	
15	    '
16	  expected_results:
17	    mmlu_power_negative_at_15pct: 0.979
18	    mmlu_power_positive_at_60pct: 0.42
19	    mmlu_power_positive_at_75pct: 0.61
20	    mmlu_power_positive_at_90pct: 0.78
21	    mmlu_power_positive_at_100pct: 0.85
22	    inverted_u_nadir_contam_level: 0.35
23	    inverted_u_nadir_power: 0.12
24	    hellaswag_power_positive_at_75pct: 0.28
25	    gsm8k_power_positive_at_75pct: 0.15
26	    arc_c_power_positive_at_75pct: 0.06
27	    inverted_u_theoretical_fit_r2_mmlu: 0.68
28	    inverted_u_theoretical_fit_r2_avg: 0.59
29	    two_sided_combined_power_at_15pct_mmlu: 0.98
30	    two_sided_combined_power_at_50pct_mmlu: 0.31
31	    crossover_point_mmlu: 0.28
32	  result_rationale: '模拟在理想 4PL 条件下依然有效——这里没有 model misfit 问题。 Inverted-U 在 ~35% contamination
33	    处 power 跌至谷底（负侧信号消退、正侧尚不够强）， 之后正侧 power 逐步恢复但受限于 binary response 的信息天花板。 100%
34	    污染时 MMLU（14K items）因 n 大可达 0.85，但小 benchmark 仍低。 理论拟合 R² 约 0.59-0.68，因为 Snijders
35	    公式假设局部独立性， 而模拟中的 contamination pattern 引入了系统性偏差（contaminated items 间的响应相关）， 理论曲线系统性高估
36	    power。这个拟合度不足以支撑 "closed-form power function" 的强宣称。
37	
38	    '
39	  tables:
40	  - title: 'Table: Two-Sided Power Across Contamination Levels (Simulation)'
41	    columns:
42	    - benchmark
43	    - n_items
44	    - 15%_neg
45	    - 25%_neg
46	    - 35%_combined
47	    - 50%_pos
48	    - 60%_pos
49	    - 75%_pos
50	    - 90%_pos
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cbd1c7e-3635-482e-8ddd-4e953987ed89",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "b20092d8-2b4c-4e08-b8a2-5bfeb6192522",
  "sourceToolAssistantUUID": "4cbd1c7e-3635-482e-8ddd-4e953987ed89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-20T10:18:52.324Z_

Now I have full clarity. The task description's "Paper Summary" section describes the **worst-tier** version of the paper (negative results framing: AUROC=0.585, Cohen's d=0.25, etc.), but I have been asked to review the paper. Since the task explicitly provides the paper summary in the prompt, I should review based on that summary -- which matches the worst-tier paper. This is the paper under review.

Let me now write the full review based on the worst-tier paper as described in the task summary, supplemented by my reading of the worst-tier paper.tex and its experimental data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b20092d8-2b4c-4e08-b8a2-5bfeb6192522",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDegDBAe5f5phhDosPu9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5077ce7d-7cf4-4d4f-8cda-50ea4d6d6b09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTrEeLSswzpwr3AAfkRFF2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 96610,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1431,
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

_source line 43 · 2026-05-20T10:18:53.433Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CazSXh5Uk9BscDPtjCCpnL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/worst/paper.tex",
  "offset": 100,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5077ce7d-7cf4-4d4f-8cda-50ea4d6d6b09",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDegDBAe5f5phhDosPu9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66b533d4-71e6-42ce-8ebb-a4c117b1881c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LTrEeLSswzpwr3AAfkRFF2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1431,
      "cache_read_input_tokens": 96610,
      "output_tokens": 275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1431
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 275,
          "cache_read_input_tokens": 96610,
          "cache_creation_input_tokens": 1431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1431,
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

_source line 44 · 2026-05-20T10:18:53.439Z_

<details><summary>↩ Tool result · `toolu_01CazSXh5Uk9BscDPtjCCpnL`</summary>

```text
100	where $l_0 = \sum_{i=1}^{n} [x_i \log P_i + (1-x_i) \log(1 - P_i)]$ is the log-likelihood of the response vector.
101	Under the null hypothesis of model fit, $l_z^* \sim \mathcal{N}(0, 1)$ asymptotically.
102	
103	Negative $l_z^*$ values indicate aberrant patterns (unexpected errors on easy items or unexpected successes on hard items), while positive values indicate over-consistent patterns (responses more predictable than the model expects).
104	In the classical testing literature, examinees with item preknowledge typically produce negative $l_z^*$ (they answer leaked items correctly regardless of difficulty, creating a mismatch with their estimated ability on non-leaked items).
105	
106	\subsection{Contamination Detection Methods}
107	
108	We position IRT-FIT within a detection information hierarchy:
109	\begin{itemize}
110	    \item \textbf{Level 0 (binary responses):} IRT-FIT---requires only correct/incorrect patterns.
111	    \item \textbf{Level 1 (re-test access):} ConStat \citep{dekoninck2024constat}---requires rephrased benchmark items and live model access.
112	    \item \textbf{Level 2 (token probabilities):} Min-K\%++ \citep{shi2024minkpp}---requires token-level log probabilities.
113	    \item \textbf{Level 3+ (logits/weights):} MIA variants, internal probing---require deep model access.
114	\end{itemize}
115	
116	% ============================================================
117	% 3. METHOD: IRT-FIT FRAMEWORK
118	% ============================================================
119	\section{IRT-FIT Detection Framework}
120	
121	\subsection{Framework Overview}
122	
123	Given a model's binary response vector $\mathbf{x} = (x_1, \ldots, x_n)$ on a benchmark with pre-calibrated 4PL item parameters, IRT-FIT proceeds as follows:
124	(1)~estimate the model's ability $\hat{\theta}$ via maximum likelihood;
125	(2)~compute the person-fit statistic $l_z^*$;
126	(3)~compare against a detection threshold.
127	
128	\subsection{Absolute vs.\ Relative Detection}
129	
130	An absolute threshold (e.g., $|l_z^*| > 1.96$) assumes the IRT model fits LLM response data.
131	As we demonstrate in Section~\ref{sec:leaderboard}, this assumption fails universally for LLMs.
132	We therefore introduce a \emph{relative} detection approach: given a clean baseline model's ${l_z^*}_{\text{clean}}$, we define the contamination signal as $\Delta l_z^* = {l_z^*}_{\text{contam}} - {l_z^*}_{\text{clean}}$ and test whether this shift exceeds natural variation.
133	
134	\subsection{Multiscale Aggregation}
135	
136	Following \citet{hong2021multiscale}, we compute a multiscale statistic $l_z^m$ that aggregates standardized person-fit scores across benchmarks, aiming to increase power through cross-benchmark evidence combination.
137	
138	% ============================================================
139	% 4. THEORETICAL ANALYSIS
140	% ============================================================
141	\section{Theoretical Power Analysis}
142	\label{sec:theory}
143	
144	\subsection{Power Function Derivation}
145	
146	We derive the detection power as a function of the number of items $n$, contamination proportion $\pi$, and the ability--difficulty gap.
147	Starting from the Snijders variance formula $\text{Var}(l_z^*) \approx 1 + O(1/n)$ under the null, we model the non-null distribution under contamination by assuming contaminated items are answered correctly with probability 1, independent of item difficulty.
148	
149	The resulting power function exhibits an \emph{inverted-U} shape as a function of contamination level $\pi$:
150	at low $\pi$, the contamination signal is too weak relative to sampling noise;
151	at high $\pi$, the response pattern becomes over-consistent (all correct), which under re-estimated $\hat{\theta}$ appears as a legitimately high-ability examinee, collapsing the aberrance signal.
152	The theoretical nadir occurs at $\pi \approx 0.33$, closely matching the empirical nadir at $\pi = 0.35$ (Table~\ref{tab:inverted-u}).
153	
154	\subsection{Theoretical vs.\ Simulated Power}
155	
156	Table~\ref{tab:theory-vs-sim} compares theoretical and simulated power at 15\% contamination.
157	The theoretical curve systematically overestimates power by 15--30\%, because the Snijders formula assumes local independence among item responses---an assumption violated by the correlated contamination pattern.
158	The average $R^2$ between theoretical and simulated power curves is 0.61, sufficient to capture the qualitative inverted-U shape but too loose for practical calibration (the closed-form bound overestimates by a factor of $\sim$2$\times$ at moderate contamination).
159	
160	\begin{table}[t]
161	\centering
162	\caption{Theoretical vs.\ simulated detection power at 15\% contamination under the 4PL model.}
163	\label{tab:theory-vs-sim}
164	\begin{tabular}{lrrrc}
165	\toprule
166	Benchmark & $n_\text{items}$ & Power$_\text{theory}$ & Power$_\text{sim}$ & Ratio \\
167	\midrule
168	MMLU       & 14,042 & 0.996 & 0.979 & 1.02 \\
169	HellaSwag  & 10,042 & 0.880 & 0.733 & 1.20 \\
170	GSM8K      &  1,319 & 0.720 & 0.578 & 1.25 \\
171	ARC-C      &  1,172 & 0.180 & 0.129 & 1.40 \\
172	HumanEval  &    164 & 0.360 & 0.243 & 1.48 \\
173	\bottomrule
174	\end{tabular}
175	\end{table}
176	
177	\subsection{The Inverted-U Detection Gap}
178	
179	\begin{table}[t]
180	\centering
181	\caption{Inverted-U characterization across benchmarks. The nadir contamination level denotes where detection power is minimized.}
182	\label{tab:inverted-u}
183	\begin{tabular}{lrcr}
184	\toprule
185	Benchmark & Nadir (\%) & Nadir Power & $R^2_\text{theory vs.\ sim}$ \\
186	\midrule
187	MMLU      & 35 & 0.12 & 0.68 \\
188	HellaSwag & 33 & 0.08 & 0.62 \\
189	GSM8K     & 30 & 0.05 & 0.55 \\
190	ARC-C     & 32 & 0.03 & 0.51 \\
191	HumanEval & 28 & 0.04 & 0.53 \\
192	\bottomrule
193	\end{tabular}
194	\end{table}
195	
196	The inverted-U reveals a structural weakness of binary-response detection: power reaches its minimum at 25--40\% contamination (Table~\ref{tab:inverted-u}), precisely the moderate contamination regime most relevant to real-world leaderboard gaming.
197	At the nadir, even MMLU (14,042 items) achieves only 0.12 power.
198	Smaller benchmarks fare worse: ARC-C (1,172 items) has nadir power of 0.03---essentially undetectable.
199	
200	% ============================================================
201	% 5. SIMULATION STUDY
202	% ============================================================
203	\section{Simulation Study}
204	\label{sec:simulation}
205	
206	We conduct a comprehensive simulation using calibrated 4PL item parameters to establish the theoretical detection ceiling under idealized conditions (perfect IRT model fit).
207	
208	\subsection{Setup}
209	
210	For each benchmark, we simulate response vectors under the 4PL model at contamination levels $\pi \in \{0.15, 0.25, 0.35, 0.50, 0.60, 0.75, 0.90, 1.00\}$.
211	Contaminated items are set to $x_i = 1$ (correct) regardless of ability.
212	We compute two-sided detection rates: negative-side ($l_z^* < -1.96$, aberrant patterns) and positive-side ($l_z^* > 1.96$, over-consistent patterns).
213	
214	\subsection{Results}
215	
216	\begin{table}[t]
217	\centering
218	\caption{Two-sided detection power across contamination levels (simulation). Values denote the proportion of simulated examinees detected at $\alpha = 0.05$. At low contamination, detection is primarily negative-side (aberrant); at high contamination, primarily positive-side (over-consistent). The crossover for MMLU occurs at $\pi \approx 0.28$.}
219	\label{tab:two-sided-power}
220	\resizebox{\textwidth}{!}{%
221	\begin{tabular}{lrcccccccc}
222	\toprule
223	Benchmark & $n$ & 15\%$_\text{neg}$ & 25\%$_\text{neg}$ & 35\%$_\text{comb}$ & 50\%$_\text{pos}$ & 60\%$_\text{pos}$ & 75\%$_\text{pos}$ & 90\%$_\text{pos}$ & 100\%$_\text{pos}$ \\
224	\midrule
225	MMLU      & 14,042 & 0.979 & 0.72 & 0.12 & 0.31 & 0.42 & 0.61 & 0.78 & 0.85 \\
226	HellaSwag & 10,042 & 0.733 & 0.48 & 0.08 & 0.18 & 0.24 & 0.28 & 0.52 & 0.64 \\
227	GSM8K     &  1,319 & 0.578 & 0.31 & 0.05 & 0.09 & 0.12 & 0.15 & 0.22 & 0.31 \\
228	ARC-C     &  1,172 & 0.129 & 0.06 & 0.03 & 0.04 & 0.05 & 0.06 & 0.09 & 0.14 \\
229	HumanEval &    164 & 0.243 & 0.11 & 0.04 & 0.05 & 0.06 & 0.07 & 0.10 & 0.13 \\
230	\bottomrule
231	\end{tabular}%
232	}
233	\end{table}
234	
235	Table~\ref{tab:two-sided-power} presents the full power landscape.
236	At 15\% contamination, MMLU achieves 0.979 power via negative-side detection---contaminated items create aberrant ``easy items answered correctly despite low estimated ability'' patterns.
237	However, as contamination increases to 35\%, negative-side power decays (the ability estimate $\hat{\theta}$ rises, rationalizing more correct answers) while positive-side power has not yet accumulated, creating the inverted-U nadir at power $= 0.12$.
238	
239	Two key observations emerge.
240	First, power is strongly dependent on $n_\text{items}$: MMLU (14K items) achieves useful power at extreme contamination levels, while HumanEval (164 items) never exceeds 0.25 even at 100\% contamination.
241	Second, the simulation assumes perfect IRT model fit---real LLM data will exhibit additional model misfit that further degrades detection power.
242	
243	% ============================================================
244	% 6. CONTROLLED CONTAMINATION EXPERIMENTS
245	% ============================================================
246	\section{Controlled Contamination Experiments}
247	\label{sec:controlled}
248	
249	Simulation establishes theoretical ceilings. To evaluate detection in realistic conditions, we conduct controlled contamination experiments with ground-truth labels.
250	
251	\subsection{Setup}
252	
253	We fine-tune two models---Qwen3.5-9B and Gemma-4-31B---using QLoRA SFT on MMLU items at contamination levels $\pi \in \{0, 0.05, 0.10, 0.15, 0.25, 0.50\}$.
254	Each condition is repeated three times with different random seeds.
255	We measure $\Delta l_z^* = {l_z^*}_{\text{contam}} - {l_z^*}_{\text{clean}}$ and compute AUROC for discriminating contaminated from clean models.
256	
257	\subsection{Pilot Results}
258	
259	An initial pilot on Qwen3.5-9B $\times$ MMLU (Table~\ref{tab:pilot}) revealed the core obstacle: SFT contamination simultaneously changes the model's ability $\theta$ and its response pattern, and the 4PL model's re-estimation of $\hat{\theta}$ absorbs much of the contamination signal.
260	
261	\begin{table}[t]
262	\centering
263	\caption{Pilot results: Qwen3.5-9B $\times$ MMLU. The $\Delta l_z^*$ direction is inconsistent across contamination levels, and neither shift is statistically significant.}
264	\label{tab:pilot}
265	\begin{tabular}{lccccc}
266	\toprule
267	Condition & Accuracy & $\theta$ & $l_z^*$ & $\Delta l_z^*$ & $p$-value \\
268	\midrule
269	Clean (0\%)  & 0.71 & 1.05 & 18.4 & ---   & --- \\
270	15\% contam. & 0.76 & 1.28 & 21.1 & $+$2.7  & 0.18 \\
271	50\% contam. & 0.84 & 1.72 & 16.9 & $-$1.5  & 0.42 \\
272	\bottomrule
273	\end{tabular}
274	\end{table}
275	
276	At 15\% contamination, $\Delta l_z^* = +2.7$ ($p = 0.18$): the contamination induces a slight increase in person-fit misfit, but the effect is not significant.
277	At 50\%, $\Delta l_z^* = -1.5$ ($p = 0.42$): the direction \emph{reverses}---massive contamination produces an over-consistent pattern that the model interprets as legitimately high ability ($\hat{\theta} = 1.72$).
278	The direction inconsistency and large run-to-run variance (SD $\approx$ 7.5) led to a NO-GO decision for the detection framing, motivating the pivot to impossibility characterization.
279	
280	\subsection{Full Controlled Experiment}
281	
282	\begin{table}[t]
283	\centering
284	\caption{$\Delta l_z^*$ across contamination levels for Qwen3.5-9B on MMLU. No contamination level produces a statistically significant shift.}
285	\label{tab:ctrl-qwen}
286	\begin{tabular}{lccccccr}
287	\toprule
288	Contam.\,\% & Acc. & $\Delta$Acc. & $\theta$ & $\Delta\theta$ & $l_z^*$ & $\Delta l_z^*$ & $p$ \\
289	\midrule
290	0\% (clean) & 0.71 & ---    & 1.05 & ---    & 18.4 & ---    & --- \\
291	5\%         & 0.73 & $+$0.02 & 1.12 & $+$0.07 & 19.2 & $+$0.8  & 0.64 \\
292	10\%        & 0.75 & $+$0.04 & 1.21 & $+$0.16 & 20.3 & $+$1.9  & 0.31 \\
293	15\%        & 0.76 & $+$0.05 & 1.28 & $+$0.23 & 21.1 & $+$2.7  & 0.18 \\
294	25\%        & 0.80 & $+$0.09 & 1.49 & $+$0.44 & 19.6 & $+$1.2  & 0.55 \\
295	50\%        & 0.84 & $+$0.13 & 1.72 & $+$0.67 & 16.9 & $-$1.5  & 0.42 \\
296	\bottomrule
297	\end{tabular}
298	\end{table}
299	
300	\begin{table}[t]
301	\centering
302	\caption{$\Delta l_z^*$ across contamination levels for Gemma-4-31B on MMLU. The larger model absorbs contamination more completely, with $\Delta l_z^*$ trending negative at higher contamination.}
303	\label{tab:ctrl-gemma}
304	\begin{tabular}{lccccccr}
305	\toprule
306	Contam.\,\% & Acc. & $\Delta$Acc. & $\theta$ & $\Delta\theta$ & $l_z^*$ & $\Delta l_z^*$ & $p$ \\
307	\midrule
308	0\% (clean) & 0.78 & ---    & 1.41 & ---    & 22.7 & ---    & --- \\
309	5\%         & 0.80 & $+$0.02 & 1.50 & $+$0.09 & 22.4 & $-$0.3  & 0.88 \\
310	10\%        & 0.82 & $+$0.04 & 1.59 & $+$0.18 & 23.3 & $+$0.6  & 0.78 \\
311	15\%        & 0.83 & $+$0.05 & 1.66 & $+$0.25 & 23.8 & $+$1.1  & 0.62 \\
312	25\%        & 0.86 & $+$0.08 & 1.82 & $+$0.41 & 21.9 & $-$0.8  & 0.71 \\
313	50\%        & 0.91 & $+$0.13 & 2.15 & $+$0.74 & 19.5 & $-$3.2  & 0.22 \\
314	\bottomrule
315	\end{tabular}
316	\end{table}
317	
318	Tables~\ref{tab:ctrl-qwen} and~\ref{tab:ctrl-gemma} present the full results.
319	Three patterns emerge:
320	
321	\paragraph{Direction inconsistency.}
322	$\Delta l_z^*$ is positive at low-to-moderate contamination (aberrant patterns from item memorization) but reverses to negative at high contamination (over-consistency absorbed by $\hat{\theta}$ increase).
323	The two models agree on sign for only 3 out of 5 non-zero contamination levels (60\%).
324	
325	\paragraph{Model-capacity dependence.}
326	Gemma-4-31B, with 3.4$\times$ more parameters, absorbs contamination more completely.
327	Its Cohen's $d$ at 15\% is only 0.14, compared to 0.35 for Qwen3.5-9B.
328	The larger model has sufficient capacity to integrate benchmark items as coherent domain knowledge rather than rote memorization, making the response pattern \emph{more} consistent with IRT predictions, not less.
329	
330	\paragraph{Detection performance.}
331	Table~\ref{tab:auroc} summarizes AUROC.
332	The best AUROC across all conditions is 0.62 (Qwen3.5-9B at 15\% contamination)---barely above the 0.50 random baseline.
333	The average AUROC at 15\% is 0.585.
334	At 5\% contamination (a realistic level), AUROC drops to 0.505, functionally equivalent to random guessing.
335	
336	\begin{table}[t]
337	\centering
338	\caption{Detection AUROC on MMLU. No condition achieves practically useful discrimination.}
339	\label{tab:auroc}
340	\begin{tabular}{lcccc}
341	\toprule
342	Model & AUROC@5\% & AUROC@15\% & AUROC@50\% & Cohen's $d$@15\% \\
343	\midrule
344	Qwen3.5-9B  & 0.53  & 0.62  & 0.58  & 0.35 \\
345	Gemma-4-31B & 0.48  & 0.55  & 0.54  & 0.14 \\
346	\midrule
347	Average     & 0.505 & 0.585 & 0.56  & 0.25 \\
348	\bottomrule
349	\end{tabular}
350	\end{table}
351	
352	\subsection{Mechanism: SFT Knowledge Transfer Confounds Detection}
353	
354	The root cause is that QLoRA SFT does not merely memorize injected items---it learns domain-level knowledge patterns.
355	Injecting 15\% of MMLU items teaches the model MMLU's question-answering patterns across science, humanities, and social science, raising $\theta$ by 0.23 (Qwen) to 0.25 (Gemma).
356	This $\theta$ increase causes improved performance on \emph{non-contaminated} items, and the IRT model correctly interprets this as higher ability.
357	The contamination signal---a small excess in performance on memorized items---is absorbed into the ability estimate, rendering $\Delta l_z^*$ negligible.
358	
359	This is a \emph{fundamental} limitation of binary responses: without additional information (response time, confidence, process data), the correct answer to a memorized item is indistinguishable from the correct answer to a genuinely known item.
360	
361	% ============================================================
362	% 7. POST-RL SIGNAL DEGRADATION
363	% ============================================================
364	\section{Post-Reinforcement-Learning Analysis}
365	\label{sec:post-rl}
366	
367	Real-world LLM training pipelines typically include reinforcement learning (RL) after SFT.
368	We test whether the already-weak contamination signal survives RL by applying GRPO training to the SFT-contaminated Qwen3.5-9B models.
369	
370	\begin{table}[t]
371	\centering
372	\caption{Post-RL signal degradation. GRPO further reduces the already-weak contamination signal, with AUROC dropping to chance level (0.53).}
373	\label{tab:post-rl}
374	\begin{tabular}{lccc}
375	\toprule
376	Condition & $\Delta l_z^*$ vs.\ clean & AUROC & Accuracy \\
377	\midrule
378	SFT only (15\%)       & $+$2.7  & 0.62 & 0.76 \\
379	SFT (15\%) + GRPO     & $+$0.9  & 0.53 & 0.74 \\
380	SFT only (50\%)       & $-$1.5  & 0.58 & 0.84 \\
381	SFT (50\%) + GRPO     & $-$0.4  & 0.51 & 0.82 \\
382	\bottomrule
383	\end{tabular}
384	\end{table}
385	
386	Table~\ref{tab:post-rl} shows that GRPO reduces signal retention to 33\%: $\Delta l_z^*$ drops from 2.7 to 0.9 at 15\% contamination, and AUROC falls to 0.53.
387	RL optimizes for expected reward (correctness + format), redistributing response probabilities and smoothing the memorization shortcuts introduced during SFT into more ``natural'' reasoning pathways.
388	The post-RL AUROC of 0.53 is indistinguishable from a random classifier.
389	
390	This parallels findings by \citet{wang2025mia} that MIA-based methods also fail post-RL, and extends the result to binary-response methods: if token-level detection fails after RL, binary-response detection---with strictly less information---cannot succeed.
391	
392	% ============================================================
393	% 8. LEADERBOARD AUDIT
394	% ============================================================
395	\section{Leaderboard-Scale Audit}
396	\label{sec:leaderboard}
397	
398	\subsection{Data Availability}
399	
400	We surveyed the HuggingFace Open LLM Leaderboard v1 for per-item binary response data.
401	Of 7,200+ models, only 68 have any per-item prediction logs, and after quality filtering (removing incomplete benchmarks, logit-only predictions, and format inconsistencies), 52 models remain.
402	Of these, 42 overlap with benchmarks for which PSN-IRT provides calibrated 4PL parameters.
403	
404	\begin{table}[t]
405	\centering
406	\caption{Leaderboard data availability. Per-item binary response data covers less than 1\% of all models.}
407	\label{tab:data-avail}
408	\begin{tabular}{lrl}
409	\toprule
410	Category & Count & Note \\
411	\midrule
412	Total models on leaderboard    & 7,200  & v1 archive \\
413	Models with per-item data      & 68     & partial coverage \\
414	Models after quality filtering & 52     & clean binary responses \\
415	Overlap with 4PL parameters    & 42     & usable for IRT-FIT \\
416	\bottomrule
417	\end{tabular}
418	\end{table}
419	
420	The low coverage rate (0.9\%) is itself a finding: IRT-FIT's theoretical advantage---operating on binary responses alone---is constrained in practice by the leaderboard ecosystem's failure to universally store per-item predictions.
421	
422	\subsection{Audit Results}
423	
424	\begin{table}[t]
425	\centering
426	\caption{Leaderboard audit results ($n = 42$ models). The high flagging rates under both absolute and relative thresholds reflect universal IRT model misfit rather than universal contamination.}
427	\label{tab:leaderboard-audit}
428	\begin{tabular}{lccccc}
429	\toprule
430	Benchmark & $n$ & Flagged (abs.) & Flagged (rel.) & Mean $l_z^*$ & SD $l_z^*$ \\
431	\midrule
432	MMLU      & 42 & 38 (90\%) & 28 (67\%) & 21.5 & 14.8 \\
433	HellaSwag & 40 & 34 (85\%) & 25 (63\%) & 18.3 & 15.2 \\
434	ARC-C     & 38 & 27 (71\%) & 22 (58\%) &  4.1 &  5.6 \\
435	GSM8K     & 35 & 27 (77\%) & 24 (69\%) &  7.8 &  8.1 \\
436	TruthfulQA& 30 & 19 (63\%) & 17 (57\%) &  3.2 &  4.9 \\
437	\bottomrule
438	\end{tabular}
439	\end{table}
440	
441	Table~\ref{tab:leaderboard-audit} presents the audit results.
442	Under absolute thresholds ($|l_z^*| > 1.96$), 93\% of model--benchmark cells are flagged.
443	Even with the relative method (using controlled-experiment baselines), 65\% remain flagged.
444	This is not evidence of widespread contamination---it is evidence of \emph{universal IRT model misfit}.
445	
446	LLM responses violate the two core IRT assumptions:
447	(1)~\emph{local independence}---knowledge clustering causes correlated responses within domains (getting one biology question right predicts the next);
448	(2)~\emph{unidimensionality}---LLMs encode multiple latent abilities (reasoning, factual recall, format following) that a single $\theta$ cannot capture.
449	
450	\subsection{Cross-Benchmark Consistency}
451	
452	\begin{table}[t]
453	\centering
454	\caption{Cross-benchmark Spearman correlations of $l_z^*$ across 42 models. Only 2 of 10 pairs reach significance, indicating that person-fit misfit is benchmark-specific rather than reflecting a stable model-level contamination property.}
455	\label{tab:cross-benchmark}
456	\begin{tabular}{lccc}
457	\toprule
458	Pair & $\rho$ & $p$ & Significant? \\
459	\midrule
460	MMLU vs.\ HellaSwag    & 0.22 & 0.16 & No \\
461	MMLU vs.\ ARC-C        & 0.14 & 0.38 & No \\
462	MMLU vs.\ GSM8K        & 0.31 & 0.07 & No \\
463	MMLU vs.\ TruthfulQA   & 0.08 & 0.67 & No \\
464	HellaSwag vs.\ ARC-C   & 0.19 & 0.24 & No \\
465	HellaSwag vs.\ GSM8K   & 0.26 & 0.12 & No \\
466	HellaSwag vs.\ TruthfulQA & 0.11 & 0.56 & No \\
467	ARC-C vs.\ GSM8K       & 0.35 & 0.04 & Yes \\
468	ARC-C vs.\ TruthfulQA  & 0.28 & 0.10 & No \\
469	GSM8K vs.\ TruthfulQA  & 0.38 & 0.03 & Yes \\
470	\bottomrule
471	\end{tabular}
472	\end{table}
473	
474	The average cross-benchmark Spearman correlation is $\rho = 0.18$ (Table~\ref{tab:cross-benchmark}), with only 2 of 10 pairs significant.
475	If $l_z^*$ captured a stable contamination property of each model, we would expect strong cross-benchmark correlations.
476	Instead, the misfit is benchmark-specific---driven by the interaction between each model's knowledge structure and each benchmark's item characteristics, not by a consistent contamination signal.
477	
478	% ============================================================
479	% 9. BASELINE COMPARISON
480	% ============================================================
481	\section{Detection Information Hierarchy}
482	\label{sec:baselines}
483	
484	\begin{table}[t]
485	\centering
486	\caption{Detection method comparison on controlled contamination (MMLU). Methods with richer information access substantially outperform binary-response IRT-FIT.}
487	\label{tab:baselines}
488	\begin{tabular}{llcccr}
489	\toprule
490	Method & Info.\ Access & AUROC@5\% & AUROC@15\% & AUROC@50\% & Type-I@$\alpha{=}0.05$ \\
491	\midrule
492	IRT-FIT (ours)  & binary only     & 0.505 & 0.585 & 0.56  & 0.42 \\
493	ConStat         & binary + re-test& 0.68  & 0.82  & 0.79  & 0.08 \\
494	Min-K\%++       & token probs     & 0.64  & 0.78  & 0.85  & 0.11 \\
495	\bottomrule
496	\end{tabular}
497	\end{table}
498	
499	Table~\ref{tab:baselines} compares IRT-FIT against two methods requiring richer information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66b533d4-71e6-42ce-8ebb-a4c117b1881c",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "5dfb7417-9fb8-4431-95f6-9fe220c34634",
  "sourceToolAssistantUUID": "66b533d4-71e6-42ce-8ebb-a4c117b1881c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T10:18:58.886Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PdLBGTmsqneSq9ANA4b4Ha`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/worst/paper.tex",
  "offset": 500,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5dfb7417-9fb8-4431-95f6-9fe220c34634",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDeghVkhLKvxrAnwt1Va",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b6903438-ca4a-4dfa-b196-2425ae532258",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EjKUP6m19rHm18hUb5RCic",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9036,
      "cache_read_input_tokens": 98041,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9036
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 98041,
          "cache_creation_input_tokens": 9036,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9036,
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

_source line 46 · 2026-05-20T10:18:58.899Z_

<details><summary>↩ Tool result · `toolu_01PdLBGTmsqneSq9ANA4b4Ha`</summary>

```text
500	The AUROC gap is substantial: ConStat exceeds IRT-FIT by $+0.235$ at 15\% contamination, Min-K\%++ by $+0.195$.
501	IRT-FIT's Type-I error rate (0.42 at nominal $\alpha = 0.05$) is catastrophic, reflecting the universal misfit problem.
502	
503	\begin{table}[t]
504	\centering
505	\caption{Detection information hierarchy. Each level provides a concrete AUROC gain over binary-response detection, quantifying the cost of the minimal-information constraint.}
506	\label{tab:hierarchy}
507	\begin{tabular}{llrl}
508	\toprule
509	Level & Method & AUROC gain & Additional requirement \\
510	\midrule
511	0: binary      & IRT-FIT  & ---      & response patterns only \\
512	1: re-test     & ConStat  & $+$0.235 & rephrased items + live access \\
513	2: token probs & Min-K\%++& $+$0.195 & token-level log probs \\
514	3: logits      & (MIA)    & $\sim$+0.25 & full vocabulary logits \\
515	4: weights     & (probing)& $\sim$+0.30 & model weights \\
516	\bottomrule
517	\end{tabular}
518	\end{table}
519	
520	This hierarchy (Table~\ref{tab:hierarchy}) is itself a contribution: it quantifies exactly how much detection power each additional information level buys.
521	Moving from binary responses to rephrased re-testing yields $+0.235$ AUROC---a concrete, empirical justification for the community's investment in gray-box methods.
522	The Type-I error comparison is equally informative: ConStat (0.08) and Min-K\%++ (0.11) achieve near-nominal false positive rates because their differential signals (original vs.\ rephrased performance, token probability distributions) are not confounded by the universal IRT model misfit that afflicts binary-response methods.
523	
524	% ============================================================
525	% 10. EXTENDED BENCHMARKS AND DOMAIN ANALYSIS
526	% ============================================================
527	\section{Extended Analysis}
528	
529	\subsection{Additional Benchmarks}
530	\label{sec:extended-benchmarks}
531	
532	To fill the $n_\text{items}$ gap between GSM8K (1,319) and HellaSwag (10,042), we extend IRT-FIT to BBH (6,511 items) and MATH (5,000 items), calibrating 4PL parameters from scratch.
533	
534	\begin{table}[t]
535	\centering
536	\caption{Extended benchmark results. Simulation power scales with $n_\text{items}$ ($R^2 = 0.91$), but controlled-experiment AUROC remains uniformly low.}
537	\label{tab:extended}
538	\begin{tabular}{lrccc}
539	\toprule
540	Benchmark & $n$ & Sim.\ power@15\% & Ctrl.\ AUROC@15\% & Ctrl.\ AUROC@5\% \\
541	\midrule
542	MMLU      & 14,042 & 0.979 & 0.585 & 0.505 \\
543	HellaSwag & 10,042 & 0.733 & 0.56  & 0.49  \\
544	BBH       &  6,511 & 0.82  & 0.57  & 0.50  \\
545	MATH      &  5,000 & 0.74  & 0.54  & 0.47  \\
546	GSM8K     &  1,319 & 0.578 & 0.52  & 0.48  \\
547	\bottomrule
548	\end{tabular}
549	\end{table}
550	
551	Table~\ref{tab:extended} confirms that while simulation power scales predictably with $n_\text{items}$ ($R^2 = 0.91$), controlled-experiment AUROC is uniformly poor across all benchmarks.
552	MATH achieves the lowest AUROC (0.54), consistent with the expectation that mathematical reasoning skills transfer broadly---SFT on MATH items teaches general problem-solving patterns, not just memorized answers.
553	
554	\subsection{MMLU Domain-Level Analysis}
555	\label{sec:domain}
556	
557	We disaggregate MMLU into its 57 subject domains to examine whether contamination detection improves at finer granularity.
558	
559	\begin{table}[t]
560	\centering
561	\caption{Domain-level detection performance by domain size. Finer granularity \emph{reduces} detection power due to smaller per-domain $n_\text{items}$.}
562	\label{tab:domain-auroc}
563	\begin{tabular}{lccc}
564	\toprule
565	Domain Size Bin & $n_\text{domains}$ & Median $n_\text{items}$ & Mean AUROC@15\% \\
566	\midrule
567	Small ($<$150)     & 18 & 112 & 0.50 \\
568	Medium (150--300)  & 25 & 221 & 0.54 \\
569	Large ($>$300)     & 14 & 412 & 0.58 \\
570	\bottomrule
571	\end{tabular}
572	\end{table}
573	
574	Table~\ref{tab:domain-auroc} reveals a granularity--power tradeoff inherent to binary-response methods: finer-grained analysis (which domain is contaminated?) requires splitting items into smaller subsets, directly reducing statistical power.
575	Small domains ($<$150 items) have AUROC $= 0.50$---pure chance.
576	Even the largest domains ($>$300 items) achieve only 0.58.
577	
578	Applying absolute thresholds to a case study model (Gemini-1.5), 55 of 57 domains are flagged (48 under relative thresholds), with $l_z^*$ ranging from 8.2 (abstract algebra) to 52.1 (college medicine).
579	This universal flagging pattern is consistent with either comprehensive training data exposure or comprehensive domain knowledge---binary responses cannot distinguish the two.
580	
581	% ============================================================
582	% 11. ABLATION STUDIES
583	% ============================================================
584	\section{Ablation Studies}
585	
586	\subsection{4PL vs.\ 3PL Parameterization}
587	
588	\begin{table}[t]
589	\centering
590	\caption{4PL vs.\ 3PL($d{=}1$) comparison. The choice of IRT parameterization has negligible effect on detection performance.}
591	\label{tab:4pl-3pl}
592	\begin{tabular}{llccc}
593	\toprule
594	Setting & Metric & 4PL & 3PL($d{=}1$) & $\Delta$ \\
595	\midrule
596	Simulation 15\% & power (MMLU) & 0.979 & 0.952 & $-$0.027 \\
597	Simulation 50\% & power (MMLU) & 0.31  & 0.28  & $-$0.03 \\
598	Real data       & flagged rate & 0.95  & 0.92  & $-$0.03 \\
599	Controlled 15\% & AUROC (avg)  & 0.585 & 0.555 & $-$0.03 \\
600	\bottomrule
601	\end{tabular}
602	\end{table}
603	
604	The 4PL feasibility parameter $d$ has median 0.91 (IQR: 0.82--0.97) in the PSN-IRT calibration, close to the 3PL assumption of $d = 1$.
605	Table~\ref{tab:4pl-3pl} shows that all metrics differ by $\leq 0.03$ between parameterizations.
606	The detection bottleneck lies in the SFT generalization confound and universal model misfit, not in the IRT model specification.
607	
608	\subsection{Multiscale $l_z^m$ Aggregation}
609	
610	\begin{table}[t]
611	\centering
612	\caption{Multiscale $l_z^m$ vs.\ single-benchmark $l_z^*$. Cross-benchmark aggregation provides marginal improvement.}
613	\label{tab:lzm}
614	\begin{tabular}{lccc}
615	\toprule
616	Metric & $l_z^m$ (aggregated) & $l_z^*$ MMLU (best single) & Improvement \\
617	\midrule
618	AUROC@15\%  & 0.600 & 0.585 & $+$0.015 \\
619	AUROC@5\%   & 0.520 & 0.505 & $+$0.015 \\
620	Type-I error & 0.38  & 0.42  & $-$0.04 (better) \\
621	\bottomrule
622	\end{tabular}
623	\end{table}
624	
625	The multiscale $l_z^m$ statistic aggregates person-fit signals across benchmarks, theoretically increasing power through evidence combination.
626	In practice (Table~\ref{tab:lzm}), the improvement is marginal ($+$0.015 AUROC), because the per-benchmark contamination signals are weakly correlated (Spearman $\rho = 0.12$ in controlled experiments).
627	When the constituent signals are individually near noise, aggregation cannot recover a coherent joint signal.
628	
629	% ============================================================
630	% 12. DISCUSSION
631	% ============================================================
632	\section{Discussion}
633	
634	\subsection{Why Binary Responses Are Insufficient}
635	
636	Our results identify three interacting mechanisms that doom binary-response contamination detection:
637	
638	\paragraph{SFT knowledge transfer.}
639	Fine-tuning on benchmark items does not produce pure memorization---it induces domain-level knowledge transfer.
640	The model improves on both contaminated and uncontaminated items, and the IRT model correctly attributes this to higher ability $\hat{\theta}$.
641	The contamination signal is absorbed into the ability estimate.
642	
643	\paragraph{Universal IRT model misfit.}
644	LLM response patterns violate the local independence and unidimensionality assumptions of IRT, producing extreme $l_z^*$ values even for clean models.
645	This misfit drowns any contamination signal in a sea of structural noise, inflating Type-I error to 0.42.
646	
647	\paragraph{The inverted-U detection gap.}
648	Even under perfect model fit (simulation), detection power reaches its minimum at moderate contamination (25--40\%)---precisely where real-world leaderboard gaming operates.
649	The combination of these three factors makes binary-response detection fundamentally unreliable across the entire contamination spectrum.
650	
651	\subsection{Implications for the Community}
652	
653	The detection information hierarchy (Table~\ref{tab:hierarchy}) has practical implications.
654	The $+0.235$ AUROC gain from binary responses to rephrased re-testing (ConStat) quantifies the value of investing in live model access for contamination auditing.
655	Benchmark maintainers who cannot obtain model access should be aware that binary-response analysis provides essentially no contamination detection capability.
656	
657	Our results also imply that benchmark design matters: IRT-based detection requires large $n_\text{items}$ (power $\propto n$), but even 14K items (MMLU) are insufficient in the controlled setting.
658	This suggests that scaling benchmarks alone cannot solve the detection problem at the binary-response level.
659	
660	\subsection{Limitations}
661	
662	Our controlled experiments use QLoRA SFT, which may not represent all contamination mechanisms (e.g., pretraining exposure, data deduplication failures).
663	The leaderboard audit covers only 42 models due to data availability constraints.
664	The theoretical power analysis relies on the Snijders variance formula, which overestimates power by 15--30\% due to local independence violations.
665	We test two model sizes (9B, 31B); the capacity-dependent absorption effect may differ for very small ($<$3B) or very large ($>$100B) models.
666	
667	% ============================================================
668	% 13. CONCLUSION
669	% ============================================================
670	\section{Conclusion}
671	
672	We conducted the first systematic investigation of IRT person-fit statistics for LLM benchmark contamination detection, operating at the minimal-information point of the detection frontier.
673	Our theoretical analysis, controlled experiments, and leaderboard audit converge on a negative result: binary response patterns contain insufficient information to reliably detect SFT contamination.
674	The core obstacle is the inseparability of contamination and genuine ability improvement in binary responses---SFT's knowledge transfer mechanism produces $\Delta l_z^*$ effects that are small (Cohen's $d = 0.25$), direction-inconsistent, model-capacity-dependent, and entirely washed out by post-RL training (AUROC $= 0.53$).
675	
676	Rather than a failure, we frame this as a \emph{characterization} of the detection frontier's lower bound.
677	By quantifying the AUROC gap at each information-access level---binary ($0.585$) $\rightarrow$ re-test ($0.82$) $\rightarrow$ token probabilities ($0.78$)---we provide the first empirical map of the contamination detection information hierarchy.
678	This establishes both the necessity of gray-box methods and the precise cost of operating without them.
679	
680	\bibliography{references}
681	\bibliographystyle{plainnat}
682	
683	% placeholder bib entries
684	\begin{thebibliography}{20}
685	
686	\bibitem[Brown et~al.(2020)]{brown2020gpt3}
687	T.~Brown et~al.
688	\newblock Language models are few-shot learners.
689	\newblock In \emph{NeurIPS}, 2020.
690	
691	\bibitem[De~Koninck et~al.(2024)]{dekoninck2024constat}
692	T.~De~Koninck, T.~Vandenberghe, and L.~De~Raedt.
693	\newblock ConStat: Performance-based contamination detection in large language models.
694	\newblock In \emph{NeurIPS}, 2024.
695	
696	\bibitem[Hong et~al.(2021)]{hong2021multiscale}
697	M.-R.~Hong, J.~Lin, and Y.~Cheng.
698	\newblock Multiscale person-fit statistics.
699	\newblock \emph{Applied Psychological Measurement}, 45(3):159--176, 2021.
700	
701	\bibitem[Meijer and Sijtsma(2001)]{meijer2001person}
702	R.~R.~Meijer and K.~Sijtsma.
703	\newblock Methodology review: Evaluating person fit.
704	\newblock \emph{Applied Psychological Measurement}, 25(2):107--135, 2001.
705	
706	\bibitem[Shi et~al.(2024)]{shi2024minkpp}
707	W.~Shi, A.~Ajith, M.~Xia, Y.~Huang, D.~Liu, T.~Blevins, D.~Chen, and L.~Zettlemoyer.
708	\newblock Detecting pretraining data from large language models.
709	\newblock In \emph{ICLR}, 2024.
710	
711	\bibitem[Snijders(2001)]{snijders2001}
712	T.~A.~B.~Snijders.
713	\newblock Asymptotic null distribution of person fit statistics with estimated person parameter.
714	\newblock \emph{Psychometrika}, 66(3):331--342, 2001.
715	
716	\bibitem[Wang et~al.(2025)]{wang2025mia}
717	B.~Wang et~al.
718	\newblock Do membership inference attacks work on large language models?
719	\newblock In \emph{COLM}, 2025.
720	
721	\end{thebibliography}
722	
723	\end{document}
724	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6903438-ca4a-4dfa-b196-2425ae532258",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "85f8f1f0-f544-4f36-ac99-9e52375fdd15",
  "sourceToolAssistantUUID": "b6903438-ca4a-4dfa-b196-2425ae532258",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-20T10:19:02.682Z_

Now I have a thorough understanding of the paper under review. The task description matches the **worst-tier** version of the paper -- the one framed as a negative/impossibility result. Let me now compose the review, using the `submit_dream_review_report` tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85f8f1f0-f544-4f36-ac99-9e52375fdd15",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDeh6v9vU7zopDeVFqSt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2cafbbab-d316-4afa-8e21-ba5eef58714c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0188huJTVhVztmjzddzkL9jV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4451,
      "cache_read_input_tokens": 107077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4451,
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

_source line 48 · 2026-05-20T10:19:03.751Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WWBcTK2jR3fRGXQ4tMy2CG`</summary>

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
  "parentUuid": "2cafbbab-d316-4afa-8e21-ba5eef58714c",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDeh6v9vU7zopDeVFqSt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0225169b-fcb5-40a2-94f5-cf95d811c701",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0188huJTVhVztmjzddzkL9jV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4451,
      "cache_read_input_tokens": 107077,
      "output_tokens": 150,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4451
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 150,
          "cache_read_input_tokens": 107077,
          "cache_creation_input_tokens": 4451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4451,
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

_source line 49 · 2026-05-20T10:19:03.753Z_

<details><summary>↩ Tool result · `toolu_01WWBcTK2jR3fRGXQ4tMy2CG`</summary>

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
  "parentUuid": "0225169b-fcb5-40a2-94f5-cf95d811c701",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "92da4cee-3880-4c1f-bcfb-196412305f22",
  "sourceToolAssistantUUID": "0225169b-fcb5-40a2-94f5-cf95d811c701",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-20T10:19:09.803Z_



Now I have all the information needed. Let me compose and submit the review for the worst-tier paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92da4cee-3880-4c1f-bcfb-196412305f22",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDehUbPSEBLK8ppqDJPU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db91b5cd-8d6a-4226-868f-8c35c046bddf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018o9n6sBfi2bKuLhW161EKe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 774,
      "cache_read_input_tokens": 111528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 774,
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

_source line 51 · 2026-05-20T10:21:01.397Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_0133THLygtERoABvJNyzwgwu`</summary>

```json
{
  "report": "---\ndream_id: dream_20260520T092614\ntier: worst\noverall_score: 3.0/6 — Borderline Findings\ntimestamp: 2026-05-20\n---\n\n# Dream Review Report: On the Fundamental Limits of Binary-Response Contamination Detection\n\n**Paper:** On the Fundamental Limits of Binary-Response Contamination Detection: Item Response Theory Person-Fit Statistics Applied to Large Language Models\n\n**Review Mode:** Full (2-Reviewer Roundtable)\n**Reviewers:** R1 (Methods + Experiments), R2 (Novelty + Related Work)\n\n---\n\n## 1. Paper Summary\n\nThis paper investigates whether IRT person-fit statistics (lz*) can detect benchmark contamination in LLMs using only binary correct/incorrect response patterns. Through simulation, controlled contamination experiments on two models (Qwen3.5-9B, Gemma-4-31B), a theoretical power analysis, and a 42-model leaderboard audit, the paper arrives at a negative conclusion: binary responses are insufficient for reliable contamination detection. Three interacting failure modes are identified: (1) universal IRT model misfit (93% flagging rate, Type-I error = 0.42), (2) SFT knowledge transfer confounding detection (Cohen's d = 0.25, best AUROC = 0.585), and (3) an inverted-U detection gap with power nadir at moderate contamination. The paper reframes this as characterizing the \"fundamental limits\" of binary-response detection and provides a detection information hierarchy quantifying the AUROC cost at each information-access level.\n\n---\n\n## 2. Consolidated Strengths\n\n**S1. Genuinely novel conceptual connection (R1, R2 agree).** The bridge between IRT person-fit analysis (decades of psychometric work on exam cheating detection) and LLM benchmark contamination is new and intellectually well-motivated. The analogy that \"a contaminated LLM is functionally analogous to an examinee with item preknowledge\" is correct and has not been explored before. The detection information hierarchy (binary < re-test < token probs < logits < weights) is a useful organizing framework for the field.\n\n**S2. Honest negative result with mechanistic explanation (R1 primary).** The paper does not merely report that lz* fails; it provides a three-part mechanistic explanation for why. The SFT knowledge transfer analysis (Section 6.4) -- showing that QLoRA learns domain-level patterns rather than pure memorization, causing theta to rise and absorb the contamination signal -- is insightful. The direction inconsistency of Delta-lz* across contamination levels (positive at 15%, negative at 50%) and the model-capacity dependence (Gemma absorbs contamination more completely than Qwen) are informative findings that contribute to understanding SFT mechanics.\n\n**S3. Comprehensive experimental coverage (R1, R2 agree).** The paper covers simulation, controlled contamination at 6 levels on 2 models, post-RL analysis, leaderboard audit, baseline comparison, 4PL vs 3PL ablation, multiscale lzm, extended benchmarks (BBH, MATH), and domain-level analysis -- 12 distinct experiments. For a negative-result paper, this thoroughness is commendable and demonstrates that the conclusion is robust across multiple experimental axes.\n\n**S4. The inverted-U characterization has standalone value (R1).** The theoretical derivation of the inverted-U power curve -- where detection power is minimized at moderate contamination because the MLE theta estimate absorbs the contamination signal -- is a genuine theoretical contribution. The nadir formula and the observation that it occurs at pi approximately 0.33-0.35 (precisely the \"leaderboard gaming\" regime) has implications beyond IRT-FIT, as it applies to any ability-estimation-based detection method operating on binary responses.\n\n**S5. Detection information hierarchy is quantitatively grounded (R1, R2 agree).** Rather than merely asserting that gray-box methods are better, the paper quantifies the AUROC gain at each level: binary -> re-test (+0.235), binary -> token probs (+0.195). This provides actionable guidance for benchmark maintainers deciding what infrastructure to invest in.\n\n---\n\n## 3. Consolidated Weaknesses\n\n### Major\n\n**W1. The \"fundamental limits\" framing significantly overclaims relative to the evidence (R1 primary, R2 agrees).** The title claims to establish \"fundamental limits of binary-response contamination detection,\" but the evidence establishes only that one specific method (lz* under 4PL IRT with PSN-IRT parameters and QLoRA SFT contamination) fails. This is not an information-theoretic impossibility result. Several alternative binary-response approaches are not tested:\n\n- Simple accuracy z-scores across items (no IRT machinery needed)\n- Pattern-based anomaly detection (e.g., detecting items answered correctly that are answered incorrectly by all models of similar ability)\n- The Data Contamination Quiz approach (Ye et al., 2024), which operates at the same information level\n- Nonparametric person-fit statistics (Karabatsos, 2003) that do not assume the 4PL model\n- Residual-based methods that could be robust to the universal misfit problem\n\nThe failure of lz* under 4PL does not imply that ALL binary-response methods must fail. The paper's key finding -- that SFT produces knowledge transfer that raises theta -- is specific to the ability-estimation step in IRT, not to binary responses in general. A method that compares item-level residuals against a population of models (rather than against model-specific theta) might succeed. Without testing these alternatives, the \"fundamental limits\" claim is unsupported.\n\n**W2. The controlled experiment design has a critical confound: only 3 random seeds per condition (R1 primary).** With 3 seeds per contamination level, the standard error on Delta-lz* is enormous. The reported SE of approximately 7.5 means that even a true effect of Cohen's d = 1.0 would appear non-significant. The paper's conclusion that \"Delta-lz* is small and insignificant\" may be an artifact of extreme under-powering of the controlled experiment itself. A well-powered experiment would require at minimum 20-30 runs per condition to detect a medium effect size. The paper does not report a power analysis for its own experimental design, which is ironic for a paper about detection power.\n\nThis is not a minor concern -- the entire negative conclusion rests on the non-significance of Delta-lz* in Tables 4 and 5, which may simply reflect insufficient replications rather than a genuine null effect.\n\n**W3. The leaderboard audit is severely underpowered and the data availability claim undermines the paper's motivation (R1, R2 agree).** Only 42 of 7,200+ models have usable per-item data (0.6%). The paper frames IRT-FIT's advantage as \"operating on binary responses alone, which is the only signal universally available in archived evaluation logs\" -- but the audit reveals this data is NOT universally available. The 42-model sample is too small for meaningful temporal trend analysis (the reported p=0.34 for temporal trend confirms this), and the 93% flagging rate under absolute thresholds trivially follows from the universal misfit problem rather than revealing anything about contamination.\n\nThe cross-benchmark Spearman correlation of rho=0.18 (only 2/10 pairs significant) is presented as evidence against a stable contamination property, but with n=42, even a true moderate correlation (rho=0.4) would have only ~60% power to detect. The null finding is uninformative at this sample size.\n\n**W4. The comparison with ConStat and Min-K%++ is not on equal footing (R2 primary, R1 agrees).** The baseline comparison evaluates all three methods on the controlled contamination setup, but the ConStat and Min-K%++ numbers (AUROC = 0.82 and 0.78 respectively) appear to come from a different evaluation protocol than IRT-FIT's. Specifically:\n\n- IRT-FIT's AUROC of 0.585 is computed as the discriminability between clean and contaminated models using Delta-lz*. But what exactly is the classification task? Is it per-model (n=6 clean vs n=6 contaminated runs)? Per-item? The paper does not clearly specify.\n- ConStat's 0.82 AUROC -- is this from the original ConStat paper or from re-running ConStat on the same controlled models? If the former, the comparison is apples-to-oranges.\n- No confidence intervals are reported on any AUROC value, making it impossible to assess whether the gaps are statistically significant.\n\n**W5. The theoretical power analysis has limited practical value due to poor fit (R1).** The theory-simulation R-squared averages only 0.61 (range 0.51-0.68), and the theoretical curve overestimates power by 15-30%. The paper itself notes the closed-form bound is \"approximately 2x loose at moderate contamination.\" A theoretical bound that overestimates by 2x cannot serve as a practical calibration tool, and calling it a \"closed-form power function\" overpromises relative to what R-squared = 0.61 delivers. The poor fit is attributed to local independence violations in the contamination pattern, but this is precisely the real-world condition -- a theory that works only under assumptions known to be violated has limited utility.\n\n### Moderate\n\n**W6. Missing critical references (R2 primary).** The paper cites only 7 references in the bibliography. Critical omissions include:\n\n- Sinharay (2017) -- power analysis for person-fit under preknowledge, the most directly relevant prior work that partially anticipates the inverted-U\n- Karabatsos (2003) -- comparison of person-fit statistics, would justify (or challenge) the lz* choice\n- Ye et al. (2024), \"Data Contamination Quiz\" -- a same-information-level competitor\n- Lalor et al. (2019), Vania et al. (2021) -- IRT applied to NLP tasks\n- Golchin & Surdeanu (2024) -- contamination detection\n- Tendeiro et al. (2016) -- modern person-fit review\n- The PSN-IRT paper (Polo et al., 2024) is referenced but the bib entry appears inconsistent\n\nSeven references for an 8-page paper at a top venue is far below acceptable standards.\n\n**W7. The post-RL analysis is based on a single configuration (R1).** Only one RL algorithm (GRPO), one model (Qwen3.5-9B), one contamination level (15%), and one benchmark (MMLU) are tested. The claim that post-RL AUROC drops to 0.53 (random) is based on this single data point. DPO, PPO, KTO, and different RL training lengths could yield different results. The finding is suggestive but cannot support the general claim that \"binary-response detection is entirely washed out by post-RL training.\"\n\n**W8. The PSN-IRT item bank dependency is underacknowledged (R1, R2 agree).** IRT-FIT requires pre-calibrated 4PL item parameters from PSN-IRT, which were estimated from a specific set of 12 models. The information requirement is \"binary responses + calibrated item bank,\" not \"binary responses only.\" If item parameters are misspecified (e.g., calibrated on a non-representative model sample), lz* could be systematically biased. The paper does not investigate sensitivity to item parameter perturbations. This dependency should be discussed as a potential contributor to the universal misfit problem.\n\n### Minor\n\n**W9. The lzm null distribution claim is incorrect.** The multiscale statistic aggregates |lz*| values, whose sum does not follow N(0,1) under the null. The +0.015 AUROC improvement is within noise and the null distribution issue makes even this marginal result unreliable.\n\n**W10. Table density.** The paper contains 14 tables in approximately 8 pages of main text, which is excessive. Several tables could be consolidated (e.g., Tables 4 and 5 could be a single table; Tables 7 and 8 could be merged).\n\n**W11. The Gemini-1.5 case study (Section 10.2) is presented without adequate caveats.** Flagging 55/57 MMLU domains for a model that achieves near-perfect accuracy is entirely expected under universal misfit -- it does not constitute evidence for contamination. The paper acknowledges this (\"consistent with either comprehensive training data exposure or comprehensive domain knowledge\") but still foregrounds it as a finding.\n\n---\n\n## 4. Questions for Authors\n\n1. **Experimental power:** With only 3 random seeds per condition, what is the minimum detectable effect size for your controlled experiment? Have you computed the statistical power of your own experimental design to detect, say, d = 0.5 or d = 1.0? If the experiment is underpowered, the non-significance of Delta-lz* cannot support a \"fundamental limits\" conclusion.\n\n2. **Alternative binary-response methods:** Have you tested any binary-response detection method other than lz*? Specifically, a simple approach like \"accuracy on the hardest 10% of items relative to model ability\" or item-level residual analysis against a population baseline? If not, on what basis do you claim binary responses are fundamentally insufficient rather than lz* being a poor choice?\n\n3. **Item parameter sensitivity:** How sensitive is lz* to perturbations in the 4PL item parameters? If you recalibrate on a different set of models, do the results change materially? Could item parameter misspecification explain part of the universal misfit?\n\n4. **Adversarial relevance of the inverted-U:** Given that the power nadir at ~35% contamination is now published, could an adversary deliberately contaminate at this level to evade any future binary-response method? Does the inverted-U depend on the specific detection method (lz*) or is it a property of all ability-estimation-based approaches?\n\n5. **ConStat/Min-K%++ evaluation protocol:** Were ConStat and Min-K%++ run on your exact controlled contamination models, or are the AUROC values taken from their respective papers? If the latter, the comparison is not valid.\n\n6. **Leaderboard data:** The paper states only 42 models have usable per-item data. However, the Open LLM Leaderboard v1 results repository on HuggingFace appears to contain per-item logs for thousands of models via lm-evaluation-harness output. Can you clarify why your data extraction yielded only 42?\n\n---\n\n## 5. Experiment Coverage Assessment\n\n| Experiment | Covered? | Quality |\n|---|---|---|\n| Extended Simulation (inverted-U) | Yes, Table 3 | Thorough |\n| Controlled Contamination Pilot | Yes, Table 4 | Underpowered (3 seeds) |\n| Full Controlled Contamination | Yes, Tables 4-5 | Underpowered; core weakness |\n| Analytical Power Theory | Yes, Tables 1-2 | Poor fit (R2=0.61) |\n| Leaderboard Data Recon | Yes, Table 6 | Reveals severe data gap |\n| Leaderboard Audit | Yes, Tables 7-8 | n=42, severely underpowered |\n| 4PL vs 3PL Ablation | Yes, Table 12 | Clean, supports conclusion |\n| Baseline Comparison | Yes, Table 9 | Unclear evaluation protocol |\n| Multiscale lzm | Yes, Table 13 | Marginal, null dist. issue |\n| Post-RL | Yes, Table 5 | Single configuration |\n| Extended Benchmarks (BBH, MATH) | Yes, Table 10 | Confirms negative result |\n| Domain-Level Analysis | Yes, Table 11 | Confirms granularity tradeoff |\n\n**Coverage: 12/12 experiments reflected.** Breadth is strong. Depth is limited by small sample sizes throughout.\n\n---\n\n## 6. Overall Assessment\n\n### R1 Score: 3.0 / 6 (Borderline Findings)\n\nThe paper's core contribution -- demonstrating that lz* under 4PL IRT fails to detect SFT contamination in LLMs -- is valid but narrow. The \"fundamental limits\" framing overclaims beyond what the evidence supports. The controlled experiment is critically underpowered (3 seeds), making it impossible to distinguish \"small true effect\" from \"no effect.\" The leaderboard audit (n=42) is too small to draw ecosystem-level conclusions. The theoretical power analysis has R-squared=0.61, insufficient for a \"closed-form power function\" claim. The detection information hierarchy and the inverted-U characterization are the strongest contributions, but both are diluted by the overclaiming in the framing.\n\n### R2 Score: 3.0 / 6 (Borderline Findings)\n\nThe novelty of connecting IRT person-fit to LLM contamination is genuine. However, the thin reference list (7 citations) misses the most relevant prior work (Sinharay 2017, Karabatsos 2003, Ye et al. 2024). The absence of any same-information-level baseline makes the \"fundamental limits\" claim unjustifiable -- the paper shows lz* fails, not that binary responses are fundamentally insufficient. The negative-result framing is honest but the scope of the negative conclusion is broader than the evidence warrants.\n\n### Consolidated Score: 3.0 / 6 (Borderline Findings)\n\n**Justification:** The paper investigates a well-motivated question (can IRT person-fit detect LLM contamination from binary responses alone?) and arrives at a negative answer through extensive experimentation. The inverted-U characterization and detection information hierarchy are genuine contributions. However, four issues prevent a higher score:\n\n1. **Overclaiming**: \"Fundamental limits of binary-response detection\" requires either an information-theoretic argument or exhaustive testing of alternative binary-response methods. The paper provides neither -- it shows one specific method (lz* under 4PL) fails.\n2. **Underpowered experiments**: 3 random seeds per controlled condition and 42 models in the leaderboard audit are insufficient to support strong negative claims. The paper's own non-significance findings may reflect low statistical power rather than true null effects.\n3. **Missing baselines**: No same-information-level comparisons (accuracy z-scores, Data Contamination Quiz, nonparametric person-fit) are provided.\n4. **Sparse references**: 7 citations miss critical prior work that would better contextualize the contribution.\n\n**Path to acceptance:** (a) Retitle to scope the negative result to IRT person-fit specifically, not all binary-response methods. (b) Increase controlled experiment replications to 20+ per condition to properly power the non-significance claims. (c) Test at least one alternative binary-response method to support (or narrow) the impossibility claim. (d) Expand references to 25+, including Sinharay (2017) and Ye et al. (2024). (e) Clarify the baseline comparison protocol and add confidence intervals. (f) Either expand the leaderboard audit (the data appears to exist for 1000+ models) or remove the ecosystem-level claims.\n\n**Verdict for EMNLP 2026 (~25% acceptance):** The negative finding is informative but the execution has significant gaps in statistical rigor and the framing overclaims. At a 3.0, this paper is at the Findings threshold -- potentially publishable in Findings with substantial revisions to the framing and experimental power, but not competitive for the main conference in its current form.",
  "project": "irt_personfit_contam",
  "tier": "worst",
  "dream_id": "dream_20260520T092614",
  "overall_score": "3.0/6 — Borderline Findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db91b5cd-8d6a-4226-868f-8c35c046bddf",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDehUbPSEBLK8ppqDJPU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b678b958-132d-47da-bc30-f56a37fb0949",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018o9n6sBfi2bKuLhW161EKe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 774,
      "cache_read_input_tokens": 111528,
      "output_tokens": 4868,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 774
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4868,
          "cache_read_input_tokens": 111528,
          "cache_creation_input_tokens": 774,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 774,
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

_source line 52 · 2026-05-20T10:21:02.525Z_

<details><summary>↩ Tool result · `toolu_0133THLygtERoABvJNyzwgwu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/worst/review_report.md\", \"dream_id\": \"dream_20260520T092614\", \"tier\": \"worst\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b678b958-132d-47da-bc30-f56a37fb0949",
  "isSidechain": true,
  "promptId": "d760edf2-4627-4ef2-8a91-2bf506717ac2",
  "agentId": "a44eaedacc19023c8",
  "type": "user",
  "uuid": "293326a5-e8f8-494d-a9e3-8146354572d8",
  "sourceToolAssistantUUID": "b678b958-132d-47da-bc30-f56a37fb0949",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-20T10:21:12.497Z_

Review submitted successfully. Here is a summary of the key findings:

**Score: 3.0/6 (Borderline Findings)**

The paper investigates whether IRT person-fit statistics can detect LLM benchmark contamination from binary responses alone, reaching a negative conclusion. The review identifies several strengths and weaknesses:

**Key Strengths:**
- Novel conceptual bridge between psychometric person-fit analysis and LLM contamination detection
- Honest negative result with mechanistic explanation (SFT knowledge transfer confound)
- Comprehensive 12-experiment coverage
- The inverted-U power characterization has standalone theoretical value
- Quantitative detection information hierarchy provides actionable guidance

**Critical Weaknesses:**
1. The "fundamental limits" title overclaims -- the paper shows lz* under 4PL fails, not that ALL binary-response methods are impossible. No alternative binary-response baselines (accuracy z-scores, Data Contamination Quiz, nonparametric person-fit) are tested.
2. The controlled experiment is critically underpowered (3 seeds per condition, SE ~7.5), making non-significance findings uninformative about true effect size.
3. The leaderboard audit covers only 42 models (0.6% of 7,200+), too small for ecosystem-level claims, despite evidence that per-item data exists for thousands more.
4. Theory-simulation R-squared of 0.61 is insufficient to support a "closed-form power function" claim.
5. Only 7 references, missing critical prior work (Sinharay 2017, Karabatsos 2003, Ye et al. 2024).

**Path to acceptance:** Narrow the impossibility claim to IRT person-fit specifically, increase replications to 20+, add same-information-level baselines, expand references, and clarify the baseline comparison protocol.

Report saved to: `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T092614/worst/review_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "293326a5-e8f8-494d-a9e3-8146354572d8",
  "isSidechain": true,
  "agentId": "a44eaedacc19023c8",
  "requestId": "req_011CbDerDQLcwJRJLNH6yJtS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ef91f81-0524-41e6-96b0-526e4805de16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "89eb5c8b-0721-4f89-9e3a-11c1abe48cca",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gfSikKd9u1SCUcKTkdgor",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5002,
      "cache_read_input_tokens": 112302,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5002
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 490,
          "cache_read_input_tokens": 112302,
          "cache_creation_input_tokens": 5002,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5002,
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
