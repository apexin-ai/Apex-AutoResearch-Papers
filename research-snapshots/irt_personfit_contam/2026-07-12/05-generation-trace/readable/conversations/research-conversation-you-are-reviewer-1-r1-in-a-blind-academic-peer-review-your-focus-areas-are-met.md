# Research conversation: You are Reviewer 1 (R1) in a blind academic peer review. Your focus areas are **Methods** and **Experiments**. Review th

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a251e1d4dccb70e3e.jsonl`
- **Structured JSON:** [`3b3db1070d2e3ab4477f.json`](../../sessions/3b/3b3db1070d2e3ab4477f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

44 recorded events

### User

_source line 1 · 2026-05-20T10:04:32.530Z_

You are Reviewer 1 (R1) in a blind academic peer review. Your focus areas are **Methods** and **Experiments**. 

Review the following paper and produce a structured review. Use the standard top-ML-venue 6-point scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Acceptance rate ~25%.

## Paper Summary

**Title:** IRT-FIT: Detecting Benchmark Contamination in Large Language Models via Person-Fit Statistics at the Minimal-Information Operating Point

**Core idea:** Repurpose IRT person-fit statistics (lz*) to detect benchmark contamination in LLMs using only binary correct/incorrect response patterns — the "minimal-information operating point." The key innovation is using Δlz* (difference between clean and contaminated conditions) rather than absolute lz* to handle the universal positive misfit problem in LLMs.

**Three claims:**
1. On benchmarks with ≥10K items, AUROC > 0.9 at 15% contamination, within 3-5pp of gray-box methods (ConStat, Min-K%++)
2. Detection power follows a predictable inverted-U curve across contamination levels, with analytically derivable nadir, scaling as a function of benchmark size
3. Leaderboard-wide audit of 1,847 Open LLM Leaderboard models: ~12% flagged, rising from 6% in 2023H2 to 18% in 2024H1 (p=0.003)

**Method (Section 4):**
- Pipeline: Fit 4PL IRT model → estimate θ via MLE → compute lz* → flag via |lz*| threshold or Δlz*
- Calibration gap addressed via relative detection (Δlz* = lz*_test - lz*_clean)
- Analytical power theory: P(detect) = Φ(−z_α + δ√n / σ_lz*), nadir formula π* ≈ (θ_true − θ_low)/(θ_high − θ_low)

**Experiments (Section 5):**
- 5.1 Simulation: 5 benchmarks × contamination 5%-100%, 1000 replications. Table 1 shows inverted-U. Power scales with n_items.
- 5.2 Controlled contamination: Qwen3.5-9B + Gemma-4-31B, QLoRA SFT (rank 16, α=32, lr=2e-4, 3 epochs), 6 levels (0-50%), 5 benchmarks. Tables 3-4. Cohen's d=2.8 (Qwen MMLU 15%), AUROC=0.94. SFT generalization ratio = 4.4%.
- 5.3 Post-RL robustness: GRPO 2000 steps on 15%-contaminated Qwen. IRT-FIT retains 94% AUROC (0.94→0.88), Min-K%++ drops to 64% (0.96→0.61).
- 5.4 Baseline comparison: IRT-FIT vs ConStat vs Min-K%++ on ground-truth. Gap <5pp at 15%, 6-10pp at 5%.
- 5.5 Leaderboard audit: 1,847 models, 6 benchmarks, June 2023-June 2024. 12% overall flagged. Yi-derivatives 31%, Phind-CodeLlama 28%. Temporal trend p=0.003.
- Appendices: A (lz* decomposition), B (4PL vs 3PL ablation: 3-5pp advantage), C (cross-benchmark comparison), D (minimum n_items table), E (BBH, MATH extended), F (domain-level MMLU analysis), G (multiscale lzm)

**Key tables:**
- Table 1: Simulation power across contamination levels (5 benchmarks)
- Table 2: Theory vs simulation vs ctrl-exp power (7 benchmarks, R²≥0.91)
- Tables 3-4: Dose-response lz* (Qwen, Gemma)
- Table 5: Post-RL retention (IRT-FIT 94%, Min-K%++ 64%, ConStat 96%)
- Table 6: Method comparison (AUROC, Type-I, time, archived data applicability)
- Tables 7-8: Leaderboard audit results and temporal trends
- Table 9: lz* power decomposition (negative vs positive)
- Table 10: 4PL vs 3PL ablation
- Tables 11-14: Extended analyses

**Experiment design reference (from review_context.yaml):** The paper was designed to cover 10+ imagined experiments including extended simulation, controlled contamination pilot + full experiment, analytical power theory, leaderboard recon + audit, 4PL vs 3PL ablation, baseline comparison, multiscale lzm, post-RL test, extra benchmarks (BBH/MATH), and domain-level analysis. All appear reflected in the paper.

## Your Review Task

Evaluate specifically:

1. **Methodological soundness**: Is the IRT framework correctly applied? Is lz* the right statistic? Is the 4PL model appropriate? Is the Δlz* approach for handling universal misfit well-justified?

2. **Experimental rigor**: Are the experiments well-controlled? Are the simulation assumptions realistic? Is the controlled contamination protocol (QLoRA SFT) a valid proxy for real-world contamination? Is the SFT generalization analysis (4.4% ratio) convincing? Are there confounds?

3. **Statistical validity**: Is the analytical power theory correctly derived? Is the inverted-U well-characterized? Are the AUROC comparisons fair? Is the leaderboard audit's flagging methodology sound?

4. **Reproducibility**: Are sufficient details provided? Could someone reproduce the controlled experiments and the leaderboard audit?

5. **Limitations and scope**: Are the acknowledged limitations honest and complete? What's missing?

6. **Strengths and weaknesses**: List at least 3 of each.

7. **Questions for authors**: List specific questions you would ask.

8. **Overall score** on the 6-point scale with justification.

Format your review with clear headers: Summary, Strengths, Weaknesses, Questions, Minor Issues, Overall Assessment (score + justification).


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "07bbef2e-43c4-42c3-892f-81ec0a9fb560",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T10:04:32.535Z_

```json
{
  "parentUuid": "07bbef2e-43c4-42c3-892f-81ec0a9fb560",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
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
  "uuid": "eb67298c-04f5-481e-94a9-049ac0d8be1c",
  "timestamp": "2026-05-20T10:04:32.535Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T10:04:41.031Z_



I'll start by reading the paper and related project files to conduct a thorough review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb67298c-04f5-481e-94a9-049ac0d8be1c",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdbEkR5Hpm4SXXqarNQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dbef118b-efa4-4950-b85f-1f6f9be84356",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwGCGQPR5HuDzSXkayj3jh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16116,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16116,
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

_source line 4 · 2026-05-20T10:04:42.059Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SPLa1jJc1t5N5AMSCtRA11`</summary>

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
  "parentUuid": "dbef118b-efa4-4950-b85f-1f6f9be84356",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdbEkR5Hpm4SXXqarNQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "563bc33b-da10-4771-8891-db09ecbe6b85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwGCGQPR5HuDzSXkayj3jh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16116,
      "cache_read_input_tokens": 0,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16116
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 107,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16116,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16116,
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

_source line 5 · 2026-05-20T10:04:42.064Z_

<details><summary>↩ Tool result · `toolu_01SPLa1jJc1t5N5AMSCtRA11`</summary>

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
  "parentUuid": "563bc33b-da10-4771-8891-db09ecbe6b85",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "f8dcc942-b50e-442a-ac72-dba501fa1de8",
  "sourceToolAssistantUUID": "563bc33b-da10-4771-8891-db09ecbe6b85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-20T10:04:44.438Z_



Let me read the paper and all related project files systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8dcc942-b50e-442a-ac72-dba501fa1de8",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdbwiGJdQJUDGFBPdSa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f51d7127-e419-435d-9851-75313ab20e4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01942q9dP7mzHDRPG96uVWsh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 7 · 2026-05-20T10:04:45.389Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Euqg8UPkmgG6MchZFaRF8E`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f51d7127-e419-435d-9851-75313ab20e4a",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdbwiGJdQJUDGFBPdSa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f38001fe-895c-482c-a076-4e95b5deba71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01942q9dP7mzHDRPG96uVWsh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 8 · 2026-05-20T10:04:45.421Z_

<details><summary>↩ Tool result · `toolu_01Euqg8UPkmgG6MchZFaRF8E`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- exp-power-theory: Detection power of lz* follows an analytic function of n_items and contamination level derivable from Snijders (2001) variance formula, and this theoretical curve explains the empirically observed inverted-U shape and n_items dependence with R²>0.95 against simulation data（准备中）\\n\\n## 近期结论\\n- **exp-empirical-null** (negative): Bootstrap empirical null of lz* under 4PL model shows systematic positive bias (mean>>0) and inflated variance (std>>1) for real LLM response data, quantifying the degree to which LLMs violate IRT local independence/unidimensionality assumptions — this bias explains why 95% of cells are flagged with absolute thresholds ← 基于 exp-two-sided\\n- **exp-leaderboard-data-recon** (success): Open LLM Leaderboard v1 results repo on HuggingFace contains per-item binary response logs (not just aggregate scores) for a substantial number of models, enabling large-scale person-fit analysis without running inference ourselves\\n  [Leaderboard Data Recon Report](/api/workspace-files/projects/irt_personfit_contam/artifacts/exp-leaderboard-data-recon/report/report.md)\\n- **exp-extended-sim** (success): Extended simulation with finer contamination levels (60/75/90%) and fixed 100% NaN handling will reveal the precise dual-regime crossover point where lz* flips from negative (aberrant) to positive (over-consistent), and inverted-U power curve shape is confirmed across all benchmarks ← 基于 sim_001\\n\\n## 趋势\\n成功 3 / 负向 3 / 失败 0 / 共 6\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb2-36806: 无 GPU 信息\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1620, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f38001fe-895c-482c-a076-4e95b5deba71",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "47b71fb0-b742-434a-93ce-63388604cc95",
  "sourceToolAssistantUUID": "f38001fe-895c-482c-a076-4e95b5deba71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T10:04:46.972Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01SzqCnUNU69HLN4Gf183S22`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/**/*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47b71fb0-b742-434a-93ce-63388604cc95",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdbwiGJdQJUDGFBPdSa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "90e54199-01d9-422d-89c1-a5cdbb0e8cb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01942q9dP7mzHDRPG96uVWsh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1289,
      "cache_read_input_tokens": 16116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1289,
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

_source line 10 · 2026-05-20T10:04:47.005Z_

<details><summary>↩ Tool result · `toolu_01SzqCnUNU69HLN4Gf183S22`</summary>

```text
artifacts/psn_irt_params/item_parameters_all.csv
artifacts/psn_irt_params/arc_c_params.csv
artifacts/psn_irt_params/gsm8k_params.csv
artifacts/psn_irt_params/hellaswag_params.csv
artifacts/psn_irt_params/humaneval_params.csv
artifacts/psn_irt_params/mmlu_params.csv
artifacts/psn_irt_data_report.md
artifacts/psn_irt_phase_b/combine.csv
artifacts/psn_irt_phase_b/student_abilities.csv
artifacts/code/__pycache__/irt_utils.cpython-314.pyc
artifacts/null_check_mini_test/humaneval_lz_star_hist.png
artifacts/null_check_mini_test/null_check_summary.json
artifacts/sim_001/data/null_check_summary.json
artifacts/simulation_results/simulation_summary.json
artifacts/sim_001/data/simulation_summary.json
artifacts/simulation_results/simulation_detailed.csv
artifacts/simulation_results/power_curves.png
artifacts/sim_001/chart/power_curves.png
artifacts/simulation_results/power_by_benchmark/humaneval_power_detail.png
artifacts/simulation_results/power_by_benchmark/arc_c_power_detail.png
artifacts/simulation_results/power_by_benchmark/gsm8k_power_detail.png
artifacts/simulation_results/power_by_benchmark/hellaswag_power_detail.png
artifacts/simulation_results/power_by_benchmark/mmlu_power_detail.png
artifacts/null_check_results/mmlu_lz_star_hist.png
artifacts/null_check_results/hellaswag_lz_star_hist.png
artifacts/null_check_results/gsm8k_lz_star_hist.png
artifacts/null_check_results/arc_c_lz_star_hist.png
artifacts/null_check_results/humaneval_lz_star_hist.png
artifacts/null_check_results/null_check_summary.json
artifacts/_project/data/personfit_matrix.csv
artifacts/phase_b_results/personfit_matrix.csv
artifacts/_project/report/personfit_summary.json
artifacts/phase_b_results/personfit_summary.json
artifacts/_project/chart/lz_star_MMLU.png
artifacts/phase_b_results/lz_star_MMLU.png
artifacts/phase_b_results/lz_star_HellaSwag.png
artifacts/phase_b_results/lz_star_GSM8K.png
artifacts/phase_b_results/lz_star_ARC-C.png
artifacts/phase_b_results/lz_star_HumanEval.png
artifacts/dream_reports/dream_20260520T082549/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260520T082549/logs/phase2_best_attempt0.log
artifacts/phase_b_two_sided/two_sided_flags.csv
artifacts/phase_b_two_sided/model_anomaly_profile.csv
artifacts/phase_b_two_sided/two_sided_summary.json
artifacts/phase_b_two_sided/two_sided_heatmap.png
artifacts/dream_reports/dream_20260520T082549/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260520T082549/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260520T082549/logs/phase2_worst_attempt1.log
artifacts/dream_reports/dream_20260520T082549/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T082549/best/experiment_data.json
artifacts/dream_reports/dream_20260520T082549/best/paper_framing.md
artifacts/dream_reports/dream_20260520T082549/best/paper.tex
artifacts/dream_reports/dream_20260520T082549/best/paper.aux
artifacts/dream_reports/dream_20260520T082549/best/paper.out
artifacts/dream_reports/dream_20260520T082549/best/paper.pdf
artifacts/dream_reports/dream_20260520T082549/best/paper.log
artifacts/dream_reports/dream_20260520T082549/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260520T082549/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T082549/median/experiment_data.json
artifacts/dream_reports/dream_20260520T082549/median/paper_framing.md
artifacts/dream_reports/dream_20260520T082549/median/paper.tex
artifacts/dream_reports/dream_20260520T082549/median/paper.aux
artifacts/dream_reports/dream_20260520T082549/median/paper.out
artifacts/dream_reports/dream_20260520T082549/median/paper.pdf
artifacts/dream_reports/dream_20260520T082549/median/paper.log
artifacts/dream_reports/dream_20260520T082549/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260520T082549/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T082549/worst/experiment_data.json
artifacts/dream_reports/dream_20260520T082549/worst/paper_framing.md
artifacts/_project/data/two_sided_detection_v2.py
artifacts/_project/data/personfit_matrix_v2.csv
artifacts/phase_b_two_sided_v2/personfit_matrix_v2.csv
artifacts/dream_reports/dream_20260520T082549/worst/paper.tex
artifacts/dream_reports/dream_20260520T082549/worst/paper.aux
artifacts/dream_reports/dream_20260520T082549/worst/paper.out
artifacts/dream_reports/dream_20260520T082549/worst/paper.pdf
artifacts/dream_reports/dream_20260520T082549/worst/paper.log
artifacts/dream_reports/dream_20260520T082549/logs/paper_agent_worst.log
artifacts/dream_reports/dream_20260520T082549/best/review_context.yaml
artifacts/dream_reports/dream_20260520T082549/logs/orchestrator.log
artifacts/_project/data/empirical_pvalues.csv
artifacts/phase_b_two_sided_v2/empirical_pvalues.csv
artifacts/_project/data/two_sided_summary_v2.json
artifacts/phase_b_two_sided_v2/two_sided_summary_v2.json
artifacts/_project/chart/lz_star_heatmap_v2.png
artifacts/phase_b_two_sided_v2/lz_star_heatmap_v2.png
artifacts/_project/report/analysis_report.md
artifacts/phase_b_two_sided_v2/analysis_report.md
artifacts/dream_reports/dream_20260520T082549/best/review_report.md
artifacts/dream_reports/dream_20260520T082549/logs/review_best.log
artifacts/dream_reports/dream_20260520T082549/median/review_context.yaml
artifacts/dream_reports/dream_20260520T082549/median/review_report.md
artifacts/dream_reports/dream_20260520T082549/logs/review_median.log
artifacts/dream_reports/dream_20260520T082549/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T082549/logs/review_worst.log
artifacts/dream_reports/dream_20260520T082549/best/_pdf_images/paper_p3.png
artifacts/dream_reports/dream_20260520T082549/best/_pdf_images/paper_p4.png
artifacts/dream_reports/dream_20260520T082549/best/_pdf_images/paper_p5.png
artifacts/dream_reports/dream_20260520T082549/best/_pdf_images/paper_p8.png
artifacts/dream_reports/dream_20260520T092614/logs/orchestrator.log
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90e54199-01d9-422d-89c1-a5cdbb0e8cb1",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "3072ff12-c1ee-4c50-81dd-ce1d73d6d387",
  "sourceToolAssistantUUID": "90e54199-01d9-422d-89c1-a5cdbb0e8cb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T10:04:50.583Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AKuUYG52YtjT1kYBkKB2XZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3072ff12-c1ee-4c50-81dd-ce1d73d6d387",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdcJvU7bgd6DN6Nd66b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e445d063-36f7-4617-b63e-4141ea54cd73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7YFFkJBf9uqAK5zZfHQfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3020,
      "cache_read_input_tokens": 17405,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3020,
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

_source line 12 · 2026-05-20T10:04:50.589Z_

<details><summary>↩ Tool result · `toolu_01AKuUYG52YtjT1kYBkKB2XZ`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{tabularx}
9	\usepackage[margin=2.5cm]{geometry}
10	\usepackage{natbib}
11	\usepackage{hyperref}
12	\usepackage{xcolor}
13	\usepackage{array}
14	\usepackage{caption}
15	
16	\newcolumntype{R}{>{\raggedleft\arraybackslash}p{1.2cm}}
17	\newcolumntype{L}{>{\raggedright\arraybackslash}p{2.8cm}}
18	
19	\title{IRT-FIT: Detecting Benchmark Contamination in Large Language Models\\via Item Response Theory Person-Fit Statistics}
20	
21	\author{Anonymous}
22	\date{}
23	
24	\begin{document}
25	\maketitle
26	
27	% ============================================================
28	\begin{abstract}
29	Benchmark contamination undermines the reliability of LLM evaluation, yet all existing detection methods require privileged access---training data, token probabilities, model weights, or specially crafted prompts. We establish the \emph{minimal-information operating point} on the contamination detection frontier by repurposing Item Response Theory (IRT) person-fit statistics, which require only binary (correct/incorrect) response patterns. Our framework, \textbf{IRT-FIT}, introduces three contributions: (1) a two-sided detection framework capturing both partial contamination (aberrant patterns, $l_{z}^{*} \ll 0$) and full contamination (over-consistent patterns, $l_{z}^{*} \gg 0$); (2) a theoretical characterization showing detection power is a predictable function of benchmark size ($n_{\text{items}}$) and contamination level, with an analytically derivable inverted-U signal structure ($R^2=0.97$); and (3) a large-scale audit of 2{,}847 Open LLM Leaderboard models revealing a 12\% overall contamination flag rate. In controlled experiments with ground-truth contamination (QLoRA SFT on Qwen3.5-9B and Gemma-4-31B), IRT-FIT achieves AUROC 0.96 at 15\% contamination and 0.82 at 5\%---outperforming ConStat (0.83/0.61) and Min-K\%++ (0.88/0.72) while requiring strictly less information. The person-fit signal survives post-RL training (AUROC 0.92 after GRPO), whereas MIA-based methods degrade to near-chance (AUROC 0.54). IRT-FIT is the only method that simultaneously addresses partial, full, and post-RL contamination at the minimal-information level.
30	\end{abstract}
31	
32	% ============================================================
33	\section{Introduction}
34	\label{sec:intro}
35	
36	Benchmark contamination---the inclusion of evaluation data in training corpora---is a growing threat to LLM evaluation integrity. As training data scales to trillions of tokens and benchmarks proliferate, the probability of inadvertent or intentional overlap increases. This undermines the fundamental assumption that benchmark performance reflects genuine capability.
37	
38	Existing detection methods span a spectrum of information requirements. N-gram overlap methods require access to training data. Membership inference attacks (MIA) and Min-K\%++ \citep{shi2024detecting} require token-level log-probabilities. Time Travel probing \citep{oren2024proving} requires specially crafted prompts. ConStat \citep{dekoninck2024constat} requires the ability to re-test models on rephrased items. \citet{wang2025reassessing} demonstrate that all MIA-based methods fail under post-RL contamination, highlighting the fragility of token-level signals.
39	
40	A contaminated LLM answering benchmark questions is functionally analogous to an examinee with item preknowledge---a problem studied for decades in psychometrics under the rubric of \emph{person-fit analysis}. Person-fit statistics such as $l_z^*$ \citep{snijders2001person} detect aberrant response patterns: examinees who answer difficult items correctly while failing easy ones, or who answer all items correctly including those far beyond their estimated ability. These statistics require only binary response data and a calibrated item bank---precisely the information available from standard LLM benchmark evaluation.
41	
42	We introduce \textbf{IRT-FIT}, a framework that establishes the \emph{minimal-information operating point} on the contamination detection frontier. Our contributions are:
43	
44	\begin{enumerate}
45	    \item \textbf{Minimal-information detection.} We show that IRT person-fit statistics detect benchmark contamination using only binary response patterns, achieving AUROC 0.96 at 15\% contamination---outperforming methods requiring token probabilities or re-testing.
46	    \item \textbf{Theoretical characterization.} We derive an analytic power formula relating detection power to benchmark size and contamination level ($R^2=0.97$), and prove that the inverted-U signal structure has a predictable inflection point determined by item difficulty distributions.
47	    \item \textbf{Large-scale empirical evidence.} We audit 2{,}847 Open LLM Leaderboard models, revealing a 12\% contamination flag rate increasing from 6\% (2023 Q1) to 18\% (2024 Q1). We identify Gemini-1.5's 100\% MMLU accuracy as systematic contamination ($l_z^*=+34.75$, $\hat{\theta}=0.78$).
48	\end{enumerate}
49	
50	% ============================================================
51	\section{Background}
52	\label{sec:background}
53	
54	\subsection{Item Response Theory}
55	
56	IRT models the probability of a correct response as a function of examinee ability $\theta$ and item parameters. We adopt the four-parameter logistic (4PL) model:
57	\begin{equation}
58	P_i(\theta) = c_i + (d_i - c_i) \cdot \frac{1}{1 + e^{-a_i(\theta - b_i)}}
59	\label{eq:4pl}
60	\end{equation}
61	where $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is the guessing parameter, and $d_i$ is the feasibility (upper asymptote) parameter. The 3PL model is the special case $d_i=1$.
62	
63	\subsection{Person-Fit Statistics}
64	
65	The $l_z$ statistic \citep{drasgow1985appropriateness} measures the fit of an individual response pattern to the IRT model:
66	\begin{equation}
67	l_z = \frac{\sum_{i=1}^{n} \left[ x_i \log P_i(\hat{\theta}) + (1-x_i) \log(1-P_i(\hat{\theta})) \right] - E[l_0]}{SD[l_0]}
68	\end{equation}
69	where $x_i \in \{0,1\}$ is the response to item $i$ and $\hat{\theta}$ is the MLE of ability. \citet{snijders2001person} derived the corrected statistic $l_z^*$ that accounts for estimation error in $\hat{\theta}$, yielding $l_z^* \sim N(0,1)$ under the null hypothesis of model fit.
70	
71	% ============================================================
72	\section{Method: IRT-FIT}
73	\label{sec:method}
74	
75	\subsection{Two-Sided Detection Framework}
76	
77	Traditional person-fit analysis tests only $l_z^* < c_{\alpha}$ (aberrant patterns). We extend to two-sided testing because contamination produces two distinct signal regimes:
78	
79	\begin{itemize}
80	    \item \textbf{Partial contamination} ($l_z^* \ll 0$): The model memorizes a subset of items, answering difficult contaminated items correctly while failing easy non-contaminated items---an aberrant pattern.
81	    \item \textbf{Full contamination} ($l_z^* \gg 0$): The model memorizes all items, producing a response pattern that is \emph{over-consistent}---all items correct, including those far beyond estimated ability.
82	\end{itemize}
83	
84	We apply the two-sided test $|l_z^*| > c_{\alpha/2}$ with Benjamini--Hochberg FDR control for multiple comparisons across models and benchmarks.
85	
86	\subsection{Multiscale Aggregation ($l_{zm}$)}
87	
88	Following \citet{hong2021multiscale}, we aggregate per-benchmark $l_z^*$ values into a single model-level index:
89	\begin{equation}
90	l_{zm} = \frac{1}{\sqrt{K}} \sum_{k=1}^{K} |l_{z,k}^*|
91	\end{equation}
92	where $K$ is the number of benchmarks evaluated. Under the null, $l_{zm}$ is approximately standard normal (verified by Kolmogorov--Smirnov test, $p=0.312$).
93	
94	\subsection{Power Theory}
95	
96	Building on Snijders' variance formula, we derive the detection power as:
97	\begin{equation}
98	\text{power} \approx \Phi\!\left(\frac{\delta \sqrt{n}}{\sigma_{l_z^*}} - z_{\alpha}\right)
99	\label{eq:power}
100	\end{equation}
101	where $\delta = E[\log L_{\text{contam}} - \log L_{\text{clean}}]$ per item is the expected log-likelihood shift induced by contamination, and $n$ is the number of items. The inverted-U inflection point $c^*$ satisfies:
102	\begin{equation}
103	c^* = \arg\min_{c} \left| E_\theta\!\left[\sum_i f(x_i, P_i) \mid \text{contam}=c\right] - E_\theta\!\left[\sum_i f(x_i, P_i) \mid \text{contam}=0\right] \right|
104	\end{equation}
105	where $f(x_i, P_i) = x_i \log P_i + (1-x_i)\log(1-P_i)$.
106	
107	% ============================================================
108	\section{Controlled Contamination Experiments}
109	\label{sec:controlled}
110	
111	\subsection{Ground-Truth Contamination}
112	\label{sec:ctrl-contam}
113	
114	We inject known contamination via QLoRA SFT on two base models (Qwen3.5-9B and Gemma-4-31B), training on 0\%/5\%/10\%/15\%/25\%/50\% of MMLU items to establish a ground-truth contamination--$l_z^*$ mapping.
115	
116	\begin{table}[t]
117	\centering
118	\caption{Controlled contamination: $l_z^*$ by model and contamination level (MMLU).}
119	\label{tab:ctrl-contam}
120	\small
121	\begin{tabular}{llrrrr}
122	\toprule
123	\textbf{Model} & \textbf{Contam.} & \textbf{Acc.} & $\hat{\theta}$ & $l_z^*$ & \textbf{Flag} \\
124	\midrule
125	Qwen3.5-9B & 0\% & .721 & 1.42 & 0.08 & .047 \\
126	Qwen3.5-9B & 5\% & .738 & 1.51 & $-$3.72 & .82 \\
127	Qwen3.5-9B & 10\% & .756 & 1.59 & $-$6.45 & .94 \\
128	Qwen3.5-9B & 15\% & .764 & 1.63 & $-$8.91 & .97 \\
129	Qwen3.5-9B & 25\% & .787 & 1.71 & $-$11.34 & .99 \\
130	Qwen3.5-9B & 50\% & .831 & 1.89 & $-$4.82 & .87 \\
131	\midrule
132	Gemma-4-31B & 0\% & .793 & 1.81 & 0.15 & .041 \\
133	Gemma-4-31B & 5\% & .808 & 1.88 & $-$3.21 & .78 \\
134	Gemma-4-31B & 15\% & .831 & 1.97 & $-$7.63 & .95 \\
135	Gemma-4-31B & 50\% & .874 & 2.14 & $-$5.14 & .84 \\
136	\bottomrule
137	\end{tabular}
138	\end{table}
139	
140	\begin{table}[t]
141	\centering
142	\caption{Detection performance (AUROC) by contamination level.}
143	\label{tab:auroc}
144	\small
145	\begin{tabular}{lrrrr}
146	\toprule
147	\textbf{Contam.} & \textbf{Qwen} & \textbf{Gemma} & \textbf{Pooled} & \textbf{Cohen's $d$} \\
148	\midrule
149	5\% & 0.84 & 0.80 & 0.82 & 1.1 \\
150	10\% & 0.93 & 0.91 & 0.92 & 1.8 \\
151	15\% & 0.97 & 0.95 & 0.96 & 2.3 \\
152	25\% & 0.99 & 0.98 & 0.99 & 2.8 \\
153	50\% & 0.94 & 0.91 & 0.93 & 1.6 \\
154	\bottomrule
155	\end{tabular}
156	\end{table}
157	
158	Table~\ref{tab:ctrl-contam} shows a monotonic increase in $|l_z^*|$ from 0\% to 25\% contamination, followed by a decrease at 50\%---the inverted-U pattern. Both models exhibit consistent behavior (effect size difference $<$15\%), ruling out model-specific artifacts. False positive rate at $\alpha=0.05$ is well-calibrated: 0.047 (Qwen) and 0.041 (Gemma). The minimum detectable contamination level is 5\% (AUROC 0.82, Table~\ref{tab:auroc}).
159	
160	\begin{table}[t]
161	\centering
162	\caption{Contamination selectivity: accuracy change on contaminated vs.\ non-contaminated items (Qwen3.5-9B).}
163	\label{tab:selectivity}
164	\small
165	\begin{tabular}{lrrrr}
166	\toprule
167	\textbf{Contam.} & \multicolumn{2}{c}{\textbf{Contam.\ Items}} & \multicolumn{2}{c}{\textbf{Non-Contam.\ Items}} \\
168	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
169	 & Before & Lift & Before & Lift \\
170	\midrule
171	5\% & .56 & +.31 & .73 & +.014 \\
172	15\% & .54 & +.30 & .73 & +.018 \\
173	25\% & .55 & +.31 & .73 & +.024 \\
174	50\% & .57 & +.31 & .73 & +.037 \\
175	\bottomrule
176	\end{tabular}
177	\end{table}
178	
179	Table~\ref{tab:selectivity} confirms that SFT contamination is highly selective: accuracy on contaminated items increases by $\sim$31 percentage points, while non-contaminated items show only 1.4--3.7\% generalization. The generalization ratio is 0.12, far too small to smooth the aberrant pattern.
180	
181	\subsection{Inverted-U Signal Characterization}
182	\label{sec:inverted-u}
183	
184	We extend simulations to 60\%/75\%/90\%/100\% contamination levels, characterizing the complete inverted-U curve across four benchmarks.
185	
186	\begin{table}[t]
187	\centering
188	\caption{$l_z^*$ as a function of contamination level (mean $\pm$ SD, 100 replications).}
189	\label{tab:inverted-u}
190	\small
191	\begin{tabular}{lrrrr}
192	\toprule
193	\textbf{Contam.} & \textbf{MMLU} & \textbf{HSwag} & \textbf{GSM8K} & \textbf{ARC-C} \\
194	\midrule
195	0\% & 0.01 & 0.03 & $-$0.02 & 0.01 \\
196	5\% & $-$3.41 & $-$1.82 & $-$1.34 & $-$0.42 \\
197	10\% & $-$6.12 & $-$3.45 & $-$2.51 & $-$0.78 \\
198	15\% & $-$8.31 & $-$4.72 & $-$3.38 & $-$1.02 \\
199	25\% & $-$12.08 & $-$6.21 & $-$4.53 & $-$1.31 \\
200	50\% & $-$5.73 & $-$2.89 & $-$1.67 & $-$0.43 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e445d063-36f7-4617-b63e-4141ea54cd73",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "fcb82fcc-ca9d-40f7-9d2c-437ae5a58bf9",
  "sourceToolAssistantUUID": "e445d063-36f7-4617-b63e-4141ea54cd73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T10:04:51.377Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VGqPJ5yat8fjXHMHGrMM8u`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcb82fcc-ca9d-40f7-9d2c-437ae5a58bf9",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdcJvU7bgd6DN6Nd66b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6af57a82-57cb-499c-9d6e-4d1f1d0e1d80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7YFFkJBf9uqAK5zZfHQfR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3020,
      "cache_read_input_tokens": 17405,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3020
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 212,
          "cache_read_input_tokens": 17405,
          "cache_creation_input_tokens": 3020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3020,
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

_source line 14 · 2026-05-20T10:04:51.646Z_

<details><summary>↩ Tool result · `toolu_01VGqPJ5yat8fjXHMHGrMM8u`</summary>

```text
1	narrative_guidance: '原始 framing 完全成立。三条 claim 均有 ground-truth 支撑：(1) minimal-information
2	  operating point 经控制实验确认——仅 binary 数据即可在 5% 污染水平检测，AUROC>0.93；(2) power ∝ n_items
3	  有解析公式， inverted-U 从经验观察升级为理论命题，拐点位置可预测；(3) Gemini-1.5 case study + leaderboard audit
4	  构成大规模实证贡献。Post-RL 实验直接回应 Wang et al.，形成"MIA 失效但 person-fit 存活"的对比叙事。 Headline: "IRT-FIT
5	  是唯一在 minimal-information 条件下同时解决 partial/full/post-RL 污染的方法"。 EMNLP 主会议无需调整 claim
6	  强度。
7	
8	  '
9	imagined_experiments:
10	- name: Two-Sided Detection Framework
11	  plan_id: exp-two-sided
12	  description: '基于 Phase B personfit_matrix.csv，实现 |lz*| > threshold 双侧检测框架， 含 bootstrap
13	    CI 和 BH-FDR 控制。验证 Gemini-1.5 case study 中正侧信号。
14	
15	    '
16	  expected_results:
17	    gemini15_mmlu_lz_star: 34.75
18	    gemini15_mmlu_lz_star_bootstrap_95ci: '[32.1, 37.4]'
19	    gemini15_gsm8k_lz_star: -15.71
20	    gemini15_humaneval_lz_star: -12.37
21	    two_sided_flagged_models_at_fdr_0.05: 4
22	    one_sided_flagged_models_at_fdr_0.05: 2
23	    incremental_detection_gain_two_vs_one_sided: 2 additional models flagged (Gemini-1.5
24	      on MMLU, 1 other high-perf model)
25	    optimal_negative_threshold_alpha_0.05: -2.81
26	    optimal_positive_threshold_alpha_0.05: 3.24
27	    positive_regime_models: Gemini-1.5 (MMLU), possibly Yi-34B or similar near-ceiling
28	      model
29	    negative_regime_models: Gemini-1.5 (GSM8K, HumanEval), Llama-2-70B (ARC-C)
30	  result_rationale: 'Gemini-1.5 的 MMLU 100% 正确率对应 θ=0.78（远低于满分所需能力），产生极端正侧 lz*=+34.75。
31	    这是因为 full contamination 导致模型在所有 item 上正确，包括远超其真实能力的难题—— response pattern 过度一致（over-consistent），与真正高能力模型的"偶尔失误"模式不符。
32	    负侧信号来自 partial contamination：模型在已污染的难题上正确、在未污染的易题上错误， 产生 aberrant pattern（lz*
33	    << 0）。双侧框架捕获这两类互补信号， 单侧框架只能捕获负侧（partial），遗漏正侧（full）。Bootstrap CI 窄是因为 MMLU 有 14K
34	    items， lz* 的抽样方差 ∝ 1/n_items。FDR 控制在 12 模型 × 5 benchmarks = 60 次检验下仍能保持 power，
35	    因为真阳性的 lz* 绝对值远超阈值（效应量极大）。
36	
37	    '
38	  tables:
39	  - name: 'Table 1: Two-Sided Detection Results (Phase B, 12 Models × 5 Benchmarks)'
40	    columns:
41	    - model
42	    - benchmark
43	    - accuracy
44	    - theta_hat
45	    - lz_star
46	    - side
47	    - flagged_bh_fdr_005
48	    - bootstrap_95ci
49	    key_rows:
50	    - - Gemini-1.5
51	      - MMLU
52	      - 1.0
53	      - 0.78
54	      - 34.75
55	      - positive
56	      - 'YES'
57	      - '[32.1, 37.4]'
58	    - - Gemini-1.5
59	      - GSM8K
60	      - 0.946
61	      - 2.41
62	      - -15.71
63	      - negative
64	      - 'YES'
65	      - '[-17.2, -14.3]'
66	    - - Gemini-1.5
67	      - HumanEval
68	      - 0.878
69	      - 1.92
70	      - -12.37
71	      - negative
72	      - 'YES'
73	      - '[-14.1, -10.8]'
74	    - - GPT-4
75	      - MMLU
76	      - 0.864
77	      - 2.15
78	      - -1.23
79	      - —
80	      - 'no'
81	      - '[-2.1, -0.4]'
82	    - - Llama-2-70B
83	      - ARC-C
84	      - 0.673
85	      - 1.08
86	      - -3.87
87	      - negative
88	      - 'YES'
89	      - '[-5.2, -2.6]'
90	  - name: 'Table 2: One-Sided vs Two-Sided Detection Comparison'
91	    columns:
92	    - method
93	    - total_flagged
94	    - partial_contam_detected
95	    - full_contam_detected
96	    - FDR_control
97	    key_rows:
98	    - - one-sided (lz* < threshold)
99	      - 2
100	      - 2
101	      - 0
102	      - '0.05'
103	    - - two-sided (|lz*| > threshold)
104	      - 4
105	      - 2
106	      - 2
107	      - '0.05'
108	  figures_description:
109	  - 'Fig 1: lz* heatmap (12 models × 5 benchmarks)，color diverging at 0，标注双侧阈值线。Gemini-1.5
110	    MMLU 为极端红色（正侧），GSM8K/HumanEval 为极端蓝色（负侧）。'
111	  - 'Fig 2: Bootstrap distribution of lz* for Gemini-1.5 MMLU，显示 CI 远离零点，p-value 极小。'
112	  analysis: '双侧框架是论文的关键方法论贡献。Phase B 数据直接证明单侧检测的盲区：Gemini-1.5 在 MMLU 上的 full contamination
113	    产生正侧信号，传统 person-fit（只看负侧 aberrance）完全遗漏。 这不仅是技术改进，而是揭示了污染信号的双重机制——partial contamination
114	    产生 aberrant pattern （答对难题、答错易题），full contamination 产生 over-consistent pattern（所有题都对，包括不该对的）。
115	    Bootstrap CI 和 FDR 控制确保结论在多重比较下依然稳健。
116	
117	    '
118	- name: Extended Simulation (Inverted-U Characterization)
119	  plan_id: exp-extended-sim
120	  description: '扩展 Phase A 模拟至 60%/75%/90%/100% contamination levels， 修复 100% contamination
121	    的 MLE boundary 处理，精确刻画 inverted-U 拐点。
122	
123	    '
124	  expected_results:
125	    inverted_u_inflection_point_mmlu: 0.65
126	    inverted_u_inflection_point_hellaswag: 0.6
127	    inverted_u_inflection_point_gsm8k: 0.7
128	    inverted_u_inflection_ci_range: '[0.55, 0.75]'
129	    lz_star_at_inflection_mmlu: -0.12
130	    lz_star_at_100pct_contam_mmlu: 28.5
131	    lz_star_at_100pct_contam_hellaswag: 18.2
132	    lz_star_at_100pct_contam_gsm8k: 8.7
133	    negative_peak_lz_at_15pct_mmlu: -8.3
134	    negative_peak_lz_at_25pct_mmlu: -12.1
135	    zero_crossing_contam_level_mmlu: 0.63
136	    zero_crossing_contam_level_hellaswag: 0.58
137	    nan_rate_after_boundary_fix: 0.0
138	    power_at_5pct_contam_mmlu: 0.78
139	    power_at_5pct_contam_hellaswag: 0.34
140	  result_rationale: 'Inverted-U 的物理机制：低污染（<15%）时，少量 hard items 被答对产生 aberrant pattern（lz*
141	    < 0）， 信号随污染比例增强；中等污染（~40-60%）时，被污染 items 的 "全部答对" 开始被 IRT 模型解释为 "该模型能力更高"，θ 估计上移，lz*
142	    绝对值开始减小——因为 response pattern 变得可以被高 θ 解释； 拐点（~65% for MMLU）处 lz* ≈ 0，pattern 恰好可被某个
143	    θ 值完美拟合；超过拐点后， 模型在几乎所有 items 上正确但 θ 估计仍有上界（受 non-contaminated items 约束）， 导致 over-consistent
144	    pattern（lz* > 0）。拐点位置取决于 benchmark 的 item difficulty 分布： MMLU 有大量高难度 items（14K
145	    items 中 ~30% difficulty > 2.0），需要更高污染比例才能 让 pattern 显得 "合理"，所以拐点在 0.65。GSM8K 难度更集中，拐点在
146	    0.70。 100% contamination 的 lz* 大小与 n_items 正相关（MMLU > HellaSwag > GSM8K）， 因为 lz*
147	    的分子累加了所有 item 的 log-likelihood 偏差。 MLE boundary fix 后 NaN 消失，因为 θ 被 cap 在 4.0，lz*
148	    仍可计算（只是值更极端）。
149	
150	    '
151	  tables:
152	  - name: 'Table 3: lz* as a Function of Contamination Level (Mean ± SD, 100 Replications)'
153	    columns:
154	    - contam_level
155	    - mmlu_lz_mean
156	    - mmlu_lz_sd
157	    - hellaswag_lz_mean
158	    - gsm8k_lz_mean
159	    - arc_c_lz_mean
160	    key_rows:
161	    - - 0%
162	      - 0.01
163	      - 1.02
164	      - 0.03
165	      - -0.02
166	      - 0.01
167	    - - 5%
168	      - -3.41
169	      - 1.15
170	      - -1.82
171	      - -1.34
172	      - -0.42
173	    - - 10%
174	      - -6.12
175	      - 1.28
176	      - -3.45
177	      - -2.51
178	      - -0.78
179	    - - 15%
180	      - -8.31
181	      - 1.41
182	      - -4.72
183	      - -3.38
184	      - -1.02
185	    - - 25%
186	      - -12.08
187	      - 1.67
188	      - -6.21
189	      - -4.53
190	      - -1.31
191	    - - 50%
192	      - -5.73
193	      - 2.14
194	      - -2.89
195	      - -1.67
196	      - -0.43
197	    - - 60%
198	      - -1.24
199	      - 2.31
200	      - 0.82
201	      - -0.34
202	      - 0.21
203	    - - 75%
204	      - 8.42
205	      - 2.53
206	      - 5.67
207	      - 3.21
208	      - 1.12
209	    - - 90%
210	      - 19.31
211	      - 2.87
212	      - 12.45
213	      - 6.78
214	      - 2.34
215	    - - 100%
216	      - 28.5
217	      - 3.12
218	      - 18.2
219	      - 8.7
220	      - 3.01
221	  - name: 'Table 4: Two-Sided Power at Various Contamination Levels'
222	    columns:
223	    - contam_level
224	    - mmlu_power
225	    - hellaswag_power
226	    - gsm8k_power
227	    - arc_c_power
228	    key_rows:
229	    - - 5%
230	      - 0.78
231	      - 0.34
232	      - 0.22
233	      - 0.06
234	    - - 15%
235	      - 0.979
236	      - 0.733
237	      - 0.578
238	      - 0.129
239	    - - 25%
240	      - 0.998
241	      - 0.891
242	      - 0.743
243	      - 0.201
244	    - - 50%
245	      - 0.872
246	      - 0.514
247	      - 0.298
248	      - 0.08
249	    - - 75%
250	      - 0.991
251	      - 0.934
252	      - 0.712
253	      - 0.187
254	    - - 100%
255	      - 1.0
256	      - 0.998
257	      - 0.962
258	      - 0.478
259	  figures_description:
260	  - 'Fig 3: Inverted-U 曲线——lz* mean vs contamination level，5 benchmarks 分色。标注 zero-crossing
261	    点和拐点位置，shaded area 为 ±1 SD。MMLU 曲线最深、拐点最右。'
262	  - 'Fig 4: Two-sided power vs contamination level，显示 U 型 power 曲线（中间有 dip 但不到 0）。对比
263	    one-sided power 在高污染时 drop to 0。'
264	  analysis: 'Inverted-U 的完整刻画是 Claim 2 的核心证据。拐点位置在 [0.55, 0.75] 范围内与 benchmark difficulty
265	    分布相关——这为后续理论推导提供了经验基准。关键发现：two-sided power 在拐点附近 有 dip 但不跌至零（因为 lz* 的 SD 在拐点处也增大，部分
266	    replications 仍超阈值）， 而 one-sided power 在高污染区完全失效。100% contamination 修复后产生极端正侧 lz*，
267	    与 Phase B Gemini-1.5 的经验数据定量一致（模拟 28.5 vs 实测 34.75，差异来自 Gemini-1.5 的真实 θ 分布与模拟假设不完全匹配）。
268	
269	    '
270	- name: Controlled Contamination Experiment
271	  plan_id: exp-ctrl-contam
272	  description: '在 Qwen3.5-9B 和 Gemma-4-31B 上，QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark
273	    items，建立 ground-truth contamination → lz* 映射。
274	
275	    '
276	  expected_results:
277	    ctrl_contam_auroc_at_15pct: 0.96
278	    ctrl_contam_auroc_at_5pct: 0.82
279	    ctrl_contam_auroc_at_25pct: 0.99
280	    ctrl_contam_min_detectable_level: 0.05
281	    ctrl_contam_lz_effect_size_cohens_d_at_15pct: 2.3
282	    ctrl_contam_lz_effect_size_cohens_d_at_5pct: 1.1
283	    qwen_clean_lz_star_mmlu: 0.08
284	    qwen_5pct_lz_star_mmlu: -3.72
285	    qwen_10pct_lz_star_mmlu: -6.45
286	    qwen_15pct_lz_star_mmlu: -8.91
287	    qwen_25pct_lz_star_mmlu: -11.34
288	    qwen_50pct_lz_star_mmlu: -4.82
289	    gemma_clean_lz_star_mmlu: 0.15
290	    gemma_5pct_lz_star_mmlu: -3.21
291	    gemma_15pct_lz_star_mmlu: -7.63
292	    gemma_50pct_lz_star_mmlu: -5.14
293	    accuracy_lift_at_15pct_contam_qwen: 0.043
294	    accuracy_lift_at_15pct_contam_gemma: 0.038
295	    sft_generalization_ratio: 0.12
296	    contaminated_items_accuracy_lift: 0.31
297	    non_contaminated_items_accuracy_change: 0.014
298	    false_positive_rate_at_alpha_0.05: 0.038
299	  result_rationale: 'SFT contamination 在 binary response 层面产生强 person-misfit 信号的原因：QLoRA
300	    SFT 直接 优化被注入 items 的 loss，导致这些 items 的正确率大幅上升（+31% on contaminated items）， 而未注入
301	    items 仅有微弱泛化（+1.4%）。这种"选择性提升"在 IRT 模型看来是 aberrant—— 模型在某些 hard items 上突然正确，但在同难度的
302	    non-contaminated items 上仍然错误。 泛化效应仅 12% 的原因：QLoRA 只更新 adapter weights（~0.5% 参数），且
303	    benchmark items 的格式高度标准化（MCQA），SFT 学到的是特定 item 的 answer pattern 而非领域知识。 Cohen''s
304	    d = 2.3 at 15% 说明效应量巨大——clean 和 contaminated 的 lz* 分布几乎不重叠。 AUROC 0.96 at 15%
305	    意味着随机抽一对 clean/contaminated 模型，96% 概率能正确区分。 5% contamination 仍可检测（AUROC 0.82）是因为
306	    MMLU 有 14K items，5% = 700 items 被污染， 足以在 lz* 累积中产生显著偏移。FPR 0.038 < 0.05 说明 null
307	    distribution 校准良好。 两个 base model 结果一致（效应量差 <15%）说明信号不依赖于特定模型架构。
308	
309	    '
310	  tables:
311	  - name: 'Table 5: Controlled Contamination — lz* by Model and Contamination Level
312	      (MMLU)'
313	    columns:
314	    - model
315	    - contam_level
316	    - accuracy
317	    - theta_hat
318	    - lz_star_mean
319	    - lz_star_sd
320	    - flagged_rate_alpha005
321	    key_rows:
322	    - - Qwen3.5-9B
323	      - 0%
324	      - 0.721
325	      - 1.42
326	      - 0.08
327	      - 0.97
328	      - 0.047
329	    - - Qwen3.5-9B
330	      - 5%
331	      - 0.738
332	      - 1.51
333	      - -3.72
334	      - 1.21
335	      - 0.82
336	    - - Qwen3.5-9B
337	      - 10%
338	      - 0.756
339	      - 1.59
340	      - -6.45
341	      - 1.34
342	      - 0.94
343	    - - Qwen3.5-9B
344	      - 15%
345	      - 0.764
346	      - 1.63
347	      - -8.91
348	      - 1.42
349	      - 0.97
350	    - - Qwen3.5-9B
351	      - 25%
352	      - 0.787
353	      - 1.71
354	      - -11.34
355	      - 1.58
356	      - 0.99
357	    - - Qwen3.5-9B
358	      - 50%
359	      - 0.831
360	      - 1.89
361	      - -4.82
362	      - 2.08
363	      - 0.87
364	    - - Gemma-4-31B
365	      - 0%
366	      - 0.793
367	      - 1.81
368	      - 0.15
369	      - 0.94
370	      - 0.041
371	    - - Gemma-4-31B
372	      - 5%
373	      - 0.808
374	      - 1.88
375	      - -3.21
376	      - 1.18
377	      - 0.78
378	    - - Gemma-4-31B
379	      - 15%
380	      - 0.831
381	      - 1.97
382	      - -7.63
383	      - 1.38
384	      - 0.95
385	    - - Gemma-4-31B
386	      - 50%
387	      - 0.874
388	      - 2.14
389	      - -5.14
390	      - 2.01
391	      - 0.84
392	  - name: 'Table 6: Detection Performance (AUROC) by Contamination Level'
393	    columns:
394	    - contam_level
395	    - auroc_qwen
396	    - auroc_gemma
397	    - auroc_pooled
398	    - cohens_d_pooled
399	    key_rows:
400	    - - 5%
401	      - 0.84
402	      - 0.8
403	      - 0.82
404	      - 1.1
405	    - - 10%
406	      - 0.93
407	      - 0.91
408	      - 0.92
409	      - 1.8
410	    - - 15%
411	      - 0.97
412	      - 0.95
413	      - 0.96
414	      - 2.3
415	    - - 25%
416	      - 0.99
417	      - 0.98
418	      - 0.99
419	      - 2.8
420	    - - 50%
421	      - 0.94
422	      - 0.91
423	      - 0.93
424	      - 1.6
425	  - name: 'Table 7: Contamination Selectivity — Accuracy Change on Contaminated vs
426	      Non-Contaminated Items'
427	    columns:
428	    - contam_level
429	    - contam_items_acc_before
430	    - contam_items_acc_after
431	    - contam_items_lift
432	    - non_contam_items_acc_before
433	    - non_contam_items_acc_after
434	    - non_contam_items_lift
435	    key_rows:
436	    - - 5%
437	      - 0.56
438	      - 0.87
439	      - 0.31
440	      - 0.73
441	      - 0.74
442	      - 0.014
443	    - - 15%
444	      - 0.54
445	      - 0.84
446	      - 0.3
447	      - 0.73
448	      - 0.75
449	      - 0.018
450	    - - 25%
451	      - 0.55
452	      - 0.86
453	      - 0.31
454	      - 0.73
455	      - 0.76
456	      - 0.024
457	    - - 50%
458	      - 0.57
459	      - 0.88
460	      - 0.31
461	      - 0.73
462	      - 0.77
463	      - 0.037
464	  figures_description:
465	  - 'Fig 5: lz* vs contamination level scatter (Qwen + Gemma, MMLU)，叠加模拟 inverted-U
466	    理论曲线。实测数据点落在理论预测 ±1 SD 内。'
467	  - 'Fig 6: ROC 曲线 at 5%/15%/25% contamination，三条曲线叠在一起，标注 AUROC 值。'
468	  - 'Fig 7: Item-level accuracy heatmap，contaminated items (sorted by difficulty)
469	    vs non-contaminated items，展示 SFT 的选择性提升效应。'
470	  analysis: '控制实验是论文最关键的 ground-truth 证据。核心发现：(1) SFT 污染在 binary response 层面 产生强烈且可检测的
471	    person-misfit 信号，Cohen''s d > 2 at 15% contamination； (2) 泛化效应仅 1-4%，远不足以平滑 aberrant
472	    pattern——这直接回应了 R5 审稿意见； (3) 两个不同架构/规模的 base model 给出一致结果，排除模型特异性； (4) 5% contamination
473	    即可检测（AUROC 0.82），确立 minimal detectable level。 50% contamination 的 lz* 绝对值回落验证了
474	    inverted-U，与扩展模拟定量一致。
475	
476	    '
477	- name: Power Theory Derivation
478	  plan_id: exp-power-theory
479	  description: '推导 power 与 n_items 的解析关系，基于 Snijders (2001) lz* 方差公式， 验证理论曲线与模拟数据的拟合度，将
480	    inverted-U 升级为理论命题。
481	
482	    '
483	  expected_results:
484	    power_theory_r_squared: 0.97
485	    power_formula: power ≈ Φ(δ·√n / σ_lz* − z_α) where δ = E[log L_contam − log L_clean]
486	      per item
487	    inverted_u_inflection_formula: c* = argmin_c |E_θ[Σ_i (x_i·log P_i + (1−x_i)·log(1−P_i))
488	      | contam=c] − E_θ[...| contam=0]|
489	    predicted_inflection_mmlu: 0.64
490	    predicted_inflection_hellaswag: 0.59
491	    predicted_inflection_gsm8k: 0.68
492	    observed_inflection_mmlu: 0.65
493	    observed_inflection_hellaswag: 0.6
494	    observed_inflection_gsm8k: 0.7
495	    inflection_prediction_error: 0.02
496	    power_at_n100_15pct_predicted: 0.089
497	    power_at_n1000_15pct_predicted: 0.491
498	    power_at_n5000_15pct_predicted: 0.862
499	    power_at_n14000_15pct_predicted: 0.981
500	    min_n_for_80pct_power_at_15pct: 3200
501	    min_n_for_80pct_power_at_5pct: 9800
502	  result_rationale: 'Snijders (2001) 证明了在正确指定的 IRT 模型下 lz* ~ N(0,1)。当注入 contamination
503	    时， lz* 的期望偏移量 δ 可以解析计算：每个被污染 item 对 log-likelihood 的贡献偏差为 log P_i(θ_true) − log
504	    P_i(θ_estimated)，其中 θ_estimated 被 contaminated items 上推。 对 n 个 items 中 c·n 个被污染的情况，总偏移
505	    ∝ c·n·δ_per_item，而 lz* 的标准差 ∝ √n。 因此 power ≈ Φ(c·√n·δ_per_item/σ − z_α)，这是一个关于
506	    c 和 n 的可预测函数。 R² = 0.97 的原因：理论假设（IRT 模型正确指定、θ 的 MLE 一致性）在模拟中近似成立， 但现实中参数估计有误差、4PL
507	    模型有轻微 misfit，导致不完美拟合。 Inverted-U 的拐点可以从 item difficulty 分布的分位数推导：当 contaminated
508	    items 的正确率 被提升到 1.0 时，如果这些 items 的 difficulty 覆盖了 IRT scale 的某个区间， θ 的 MLE 会被推到一个特定位置，使得
509	    response pattern 看起来 "最合理" 的 contamination 比例 就是拐点。MMLU difficulty 分布偏宽（SD ≈ 1.8），拐点偏右（0.64）；GSM8K
510	    difficulty 更集中 （SD ≈ 1.2），拐点偏右（0.68）是因为 difficulty 水平更高。 理论预测的拐点与观测值的误差仅 0.02，验证了解析公式的有效性。
511	
512	    '
513	  tables:
514	  - name: 'Table 8: Theoretical vs Simulated Power (15% Contamination)'
515	    columns:
516	    - n_items
517	    - predicted_power
518	    - simulated_power
519	    - absolute_error
520	    key_rows:
521	    - - 100
522	      - 0.089
523	      - 0.092
524	      - 0.003
525	    - - 500
526	      - 0.312
527	      - 0.298
528	      - 0.014
529	    - - 1000
530	      - 0.491
531	      - 0.503
532	      - 0.012
533	    - - 1319
534	      - 0.578
535	      - 0.578
536	      - 0.0
537	    - - 5000
538	      - 0.862
539	      - 0.851
540	      - 0.011
541	    - - 10042
542	      - 0.964
543	      - 0.958
544	      - 0.006
545	    - - 14042
546	      - 0.981
547	      - 0.979
548	      - 0.002
549	  - name: 'Table 9: Inverted-U Inflection Point — Predicted vs Observed'
550	    columns:
551	    - benchmark
552	    - n_items
553	    - difficulty_sd
554	    - predicted_inflection
555	    - observed_inflection
556	    - abs_error
557	    key_rows:
558	    - - MMLU
559	      - 14042
560	      - 1.83
561	      - 0.64
562	      - 0.65
563	      - 0.01
564	    - - HellaSwag
565	      - 10042
566	      - 1.52
567	      - 0.59
568	      - 0.6
569	      - 0.01
570	    - - GSM8K
571	      - 1319
572	      - 1.21
573	      - 0.68
574	      - 0.7
575	      - 0.02
576	    - - ARC-C
577	      - 1172
578	      - 1.45
579	      - 0.62
580	      - 0.64
581	      - 0.02
582	    - - HumanEval
583	      - 164
584	      - 1.67
585	      - 0.61
586	      - 0.63
587	      - 0.02
588	  - name: 'Table 10: Minimum n_items for 80% Power at Various Contamination Levels'
589	    columns:
590	    - contam_level
591	    - min_n_theoretical
592	    - min_n_simulated
593	    key_rows:
594	    - - 5%
595	      - 9800
596	      - 10200
597	    - - 10%
598	      - 4700
599	      - 4900
600	    - - 15%
601	      - 3200
602	      - 3350
603	    - - 25%
604	      - 1800
605	      - 1900
606	  figures_description:
607	  - 'Fig 8: Power vs n_items 理论曲线（连续线）叠加 5 benchmarks 的模拟数据点（散点）。多条曲线对应不同 contamination
608	    levels (5%/10%/15%/25%)。'
609	  - 'Fig 9: Inverted-U 理论预测曲线 vs 模拟数据，标注拐点位置与 CI。'
610	  - 'Fig 10: Power landscape heatmap (n_items × contam_level)，颜色编码 power，标注 80% power
611	    等高线。'
612	  analysis: 'Power 理论将 Claim 2 从经验观察升级为可预测的定量关系。解析公式给出了 practitioner 的 直接指导：要检测 15%
613	    污染需要 ≥3200 items，检测 5% 污染需要 ≥9800 items。 这解释了为什么 ARC-C (1172 items) 的 power 只有
614	    12.9%——不是方法失败，而是信息不足。 Inverted-U 的理论推导是方法论贡献的核心：它不仅解释了为什么存在拐点， 还能从 item difficulty
615	    分布预测拐点位置，误差仅 1-2 个百分点。
616	
617	    '
618	- name: Leaderboard Audit (Large-Scale Scan)
619	  plan_id: exp-leaderboard-audit
620	  description: 'Open LLM Leaderboard v1 大规模扫描，获取 per-item response logs， 对所有可用模型计算
621	    person-fit，绘制 per-benchmark 污染率随时间趋势。
622	
623	    '
624	  expected_results:
625	    leaderboard_models_scanned: 2847
626	    leaderboard_models_with_per_item_logs: 0
627	    leaderboard_models_rerun_inference: 2847
628	    total_gpu_hours_inference: 18.5
629	    leaderboard_flagged_rate_overall: 0.12
630	    leaderboard_flagged_rate_mmlu: 0.15
631	    leaderboard_flagged_rate_hellaswag: 0.09
632	    leaderboard_flagged_rate_arc_c: 0.07
633	    leaderboard_flagged_rate_gsm8k: 0.11
634	    flagged_models_total: 342
635	    flagged_two_sided_positive: 87
636	    flagged_two_sided_negative: 255
637	    contamination_trend_increasing: true
638	    contamination_rate_2023q1: 0.06
639	    contamination_rate_2023q3: 0.11
640	    contamination_rate_2024q1: 0.18
641	    cross_benchmark_consistent_flag_rate: 0.34
642	    top_flagged_model_lz_star: -22.4
643	  result_rationale: 'Per-item response logs 在 HuggingFace 上不直接公开（Leaderboard v1 只存
644	    aggregate scores）， 因此需要对可获取权重的模型重新跑推理。受 GPU 预算限制（20 hrs），选择 <7B 参数模型 优先扫描，覆盖 2847
645	    个模型（占 Leaderboard v1 总量的 ~40%）。 12% flagged rate 的来源：Leaderboard v1 时期（2023-2024）是
646	    benchmark gaming 高峰期， 大量模型通过 SFT 在 benchmark items 上训练以获取高排名。MMLU 受影响最严重（15%）
647	    因为它是 Leaderboard 的核心排名指标且训练数据广泛可获得。 时间趋势显示 2023 Q1 flagged rate 仅 6%，到 2024 Q1
648	    升至 18%—— 与社区对 benchmark contamination 问题认知的时间线一致（Contamination in the wild 2024
649	    等论文）。 正侧 flagged（87 个）主要是 MMLU 上的 "suspicious near-ceiling" 模型， 负侧 flagged（255
650	    个）主要是 partial contamination 的小模型。 跨 benchmark 一致 flag rate 34% 说明约 1/3 的 flagged
651	    模型在多个 benchmark 上同时异常—— 这些是最可信的 contamination 案例。
652	
653	    '
654	  tables:
655	  - name: 'Table 11: Leaderboard Audit Summary'
656	    columns:
657	    - benchmark
658	    - models_scanned
659	    - flagged_negative
660	    - flagged_positive
661	    - flagged_rate
662	    - median_lz_star_flagged
663	    key_rows:
664	    - - MMLU
665	      - 2847
666	      - 312
667	      - 115
668	      - 0.15
669	      - -6.73
670	    - - HellaSwag
671	      - 2847
672	      - 198
673	      - 58
674	      - 0.09
675	      - -4.21
676	    - - ARC-C
677	      - 2847
678	      - 142
679	      - 57
680	      - 0.07
681	      - -3.12
682	    - - GSM8K
683	      - 2182
684	      - 178
685	      - 63
686	      - 0.11
687	      - -5.42
688	    - - Overall (any benchmark)
689	      - 2847
690	      - 255
691	      - 87
692	      - 0.12
693	      - —
694	  - name: 'Table 12: Contamination Rate by Time Period'
695	    columns:
696	    - period
697	    - models_in_period
698	    - flagged_count
699	    - flagged_rate
700	    key_rows:
701	    - - 2023 Q1-Q2
702	      - 487
703	      - 29
704	      - 0.06
705	    - - 2023 Q3-Q4
706	      - 891
707	      - 98
708	      - 0.11
709	    - - 2024 Q1-Q2
710	      - 1103
711	      - 198
712	      - 0.18
713	    - - 2024 Q3+
714	      - 366
715	      - 51
716	      - 0.14
717	  - name: 'Table 13: Top 10 Most Anomalous Models'
718	    columns:
719	    - model
720	    - benchmark
721	    - accuracy
722	    - theta
723	    - lz_star
724	    - side
725	    - params
726	    key_rows:
727	    - - anonymous-7b-v3
728	      - MMLU
729	      - 0.847
730	      - 1.23
731	      - -22.4
732	      - negative
733	      - 7B
734	    - - llm-finetune-2b
735	      - MMLU
736	      - 0.912
737	      - 1.45
738	      - 18.7
739	      - positive
740	      - 2B
741	    - - benchmark-tuned-3b
742	      - GSM8K
743	      - 0.891
744	      - 2.12
745	      - -17.3
746	      - negative
747	      - 3B
748	  figures_description:
749	  - 'Fig 11: 散点图——所有 2847 模型的 (accuracy, lz*) on MMLU。Flagged 模型标红，non-flagged 标灰。显示
750	    flagged 模型不仅是高 accuracy（也有中等 accuracy 但 aberrant pattern 的）。'
751	  - 'Fig 12: 时间趋势——每季度的 flagged rate，按 benchmark 分色。显示逐年上升趋势。'
752	  - 'Fig 13: Cross-benchmark consistency heatmap——flagged 模型在各 benchmark 上的 lz* 值，展示跨
753	    benchmark 污染的关联性。'
754	  analysis: 'Leaderboard audit 是 IRT-FIT 的 "killer app"——唯一只需要 binary response data
755	    的方法 才能做到如此规模的扫描。ConStat 需要 re-test（需要 live model access）， Min-K%++ 需要 token probabilities（需要
756	    logits），MIA 需要 training data reference。 2847 个模型的扫描中 12% flagged rate 意味着约 342
757	    个模型存在可疑的 benchmark 污染， 且这个比例随时间上升。这为社区提供了首个大规模、定量的 benchmark integrity 评估。 尽管未达到
758	    7000 个模型的上限预测，2847 个模型已是同类研究中最大规模。
759	
760	    '
761	- name: 4PL vs 3PL Ablation
762	  plan_id: exp-4pl-ablation
763	  description: '比较 4PL (with feasibility parameter d) 和 3PL(d=1) 下的检测灵敏度差异， 量化 d 参数对
764	    false alarm 和 detection power 的影响。
765	
766	    '
767	  expected_results:
768	    auroc_4pl_15pct: 0.96
769	    auroc_3pl_15pct: 0.91
770	    auroc_difference_15pct: 0.05
771	    false_alarm_rate_4pl: 0.042
772	    false_alarm_rate_3pl: 0.078
773	    power_4pl_15pct_mmlu: 0.979
774	    power_3pl_15pct_mmlu: 0.934
775	    power_difference_15pct_mmlu: 0.045
776	    mean_abs_lz_star_difference_clean: 0.34
777	    mean_abs_lz_star_difference_contam: 0.87
778	    d_parameter_mean_psn_irt: 0.91
779	    d_parameter_sd_psn_irt: 0.08
780	    items_where_d_matters_most: top-difficulty items (difficulty > 2.5) where d <
781	      0.85
782	  result_rationale: '4PL 的 d 参数（upper asymptote / feasibility parameter）建模了即使能力极高的考生
783	    也可能答错某些 items 的现象——在 LLM 场景中对应"某些 items 的表述/格式导致即使知道答案的模型也可能选错"。 当 d < 1 时，3PL(d=1)
784	    会高估高能力模型在这些 items 上的预期正确率， 导致其答错时产生过多的 "aberrant" 信号（false alarm 上升）。 4PL 通过让
785	    d < 1 吸收这种自然变异，减少了 false alarm（0.042 vs 0.078）。 对于 contaminated models，d < 1 的
786	    items 是区分度最高的：contaminated model 在这些 items 上 答对率接近 1.0（因为直接记住了答案），而 clean model
787	    的答对率被 d 压低。 因此 4PL 在 contaminated case 中效应量更大（lz* 偏差多 0.87），综合 AUROC 提升 0.05。
788	    差异主要集中在高难度 items（difficulty > 2.5）——这些 items 的 d 值通常更低， 因为它们的表述更复杂，即使知道正确答案也更容易因格式理解问题出错。
789	
790	    '
791	  tables:
792	  - name: 'Table 14: 4PL vs 3PL Detection Performance Comparison'
793	    columns:
794	    - metric
795	    - 4PL
796	    - 3PL(d=1)
797	    - difference
798	    key_rows:
799	    - - AUROC @ 15%
800	      - 0.96
801	      - 0.91
802	      - '+0.05'
803	    - - False Alarm Rate (α=0.05)
804	      - 0.042
805	      - 0.078
806	      - −0.036
807	    - - Power @ 15% MMLU
808	      - 0.979
809	      - 0.934
810	      - '+0.045'
811	    - - Power @ 5% MMLU
812	      - 0.78
813	      - 0.69
814	      - '+0.09'
815	    - - Mean |lz*| clean models
816	      - 0.83
817	      - 1.17
818	      - −0.34
819	    - - Mean |lz*| contam models (15%)
820	      - 8.91
821	      - 8.04
822	      - '+0.87'
823	  - name: 'Table 15: Impact of d Parameter by Item Difficulty Band'
824	    columns:
825	    - difficulty_band
826	    - n_items
827	    - mean_d
828	    - lz_star_diff_clean
829	    - lz_star_diff_contam
830	    key_rows:
831	    - - < 0.5 (easy)
832	      - 2814
833	      - 0.97
834	      - -0.08
835	      - 0.12
836	    - - 0.5–1.5
837	      - 5621
838	      - 0.93
839	      - -0.21
840	      - 0.43
841	    - - 1.5–2.5
842	      - 3891
843	      - 0.89
844	      - -0.38
845	      - 0.78
846	    - - '> 2.5 (hard)'
847	      - 1716
848	      - 0.82
849	      - -0.67
850	      - 1.45
851	  figures_description:
852	  - 'Fig 14: ROC 曲线对比——4PL vs 3PL at 5%/15% contamination。4PL 曲线始终在 3PL 上方。'
853	  - 'Fig 15: d parameter distribution (histogram) from PSN-IRT，标注 mean 和关键分位数。'
854	  analysis: '4PL vs 3PL 的差异统计显著但不是巨大的——这其实是好消息：它说明 person-fit 方法 对 IRT 模型选择有一定 robustness，3PL
855	    也能工作（AUROC 0.91），但 4PL 更优（AUROC 0.96）。 关键 insight：d 参数的影响集中在高难度 items 上，而这些 items
856	    恰好是 contamination 信号最强的区域（contaminated model 在难题上答对是最 aberrant 的）。因此 4PL 的精确建模
857	    在检测任务中有非平凡的价值。
858	
859	    '
860	- name: Baseline Comparison (ConStat, Min-K%++)
861	  plan_id: exp-baseline-comparison
862	  description: '在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs ConStat vs
863	    Min-K%++ 的 AUROC 和 Type-I error。
864	
865	    '
866	  expected_results:
867	    irt_fit_auroc_15pct: 0.96
868	    constat_auroc_15pct: 0.83
869	    min_k_pp_auroc_15pct: 0.88
870	    irt_fit_auroc_5pct: 0.82
871	    constat_auroc_5pct: 0.61
872	    min_k_pp_auroc_5pct: 0.72
873	    auroc_advantage_vs_constat_15pct: 0.13
874	    auroc_advantage_vs_minkpp_15pct: 0.08
875	    baseline_auroc_advantage_vs_constat: 0.1
876	    type_i_error_irt_fit: 0.042
877	    type_i_error_constat: 0.053
878	    type_i_error_min_k_pp: 0.048
879	    irt_fit_information_required: binary responses only
880	    constat_information_required: binary responses + re-test capability
881	    min_k_pp_information_required: token-level log-probabilities
882	    irt_fit_unique_advantage: operates without model access
883	  result_rationale: 'IRT-FIT 在 AUROC 上优于 ConStat 0.10-0.13 的原因有两方面： (1) Person-fit
884	    statistics 利用了完整的 item-level response pattern 信息——每个 item 的 difficulty、 discrimination、guessing、feasibility
885	    参数都参与 lz* 计算，而 ConStat 基于 aggregate performance 的一致性检验，信息利用效率更低； (2) ConStat 的
886	    re-test design 假设 contaminated model 在 re-test 时表现不一致， 但 SFT contamination 是永久性的（权重已改变），re-test
887	    分数几乎不变，削弱了 ConStat 的信号。 Min-K%++ 在 AUROC 上略低于 IRT-FIT（0.88 vs 0.96）但需要 token-level
888	    probabilities—— 信息需求更高。其信号来自 token-level memorization（contaminated items 的 token
889	    loss 更低）， 但 SFT 后的 token-level 信号会被 RL 和 decoding 过程扰动，不如 binary response 层面的
890	    person-fit 信号稳定。 Type-I error 都接近 nominal 0.05，说明三种方法的 null calibration 都合理。 关键叙事：IRT-FIT
891	    不仅性能更好，而且信息需求最低——这是 detection frontier 的核心论点。
892	
893	    '
894	  tables:
895	  - name: 'Table 16: Baseline Comparison — Detection Performance on Controlled Contamination'
896	    columns:
897	    - method
898	    - info_required
899	    - auroc_5pct
900	    - auroc_15pct
901	    - auroc_25pct
902	    - type_i_error
903	    key_rows:
904	    - - IRT-FIT (lz*, two-sided)
905	      - binary responses
906	      - 0.82
907	      - 0.96
908	      - 0.99
909	      - 0.042
910	    - - ConStat
911	      - binary + re-test
912	      - 0.61
913	      - 0.83
914	      - 0.91
915	      - 0.053
916	    - - Min-K%++
917	      - token log-probs
918	      - 0.72
919	      - 0.88
920	      - 0.95
921	      - 0.048
922	  - name: 'Table 17: Detection Frontier — Information Access vs Detection Power'
923	    columns:
924	    - information_level
925	    - method
926	    - auroc_15pct
927	    - scalability
928	    key_rows:
929	    - - binary responses only
930	      - IRT-FIT
931	      - 0.96
932	      - any model with public scores
933	    - - binary + re-test
934	      - ConStat
935	      - 0.83
936	      - requires live model access
937	    - - token probabilities
938	      - Min-K%++
939	      - 0.88
940	      - requires API with logprobs
941	    - - training data
942	      - n-gram overlap
943	      - —
944	      - requires training data access
945	    - - model weights
946	      - internal probing
947	      - —
948	      - requires open weights
949	  figures_description:
950	  - 'Fig 16: ROC 曲线三方对比，IRT-FIT / ConStat / Min-K%++，at 15% contamination。'
951	  - 'Fig 17: Detection frontier diagram——x 轴为 information access level (ordered)，y
952	    轴为 AUROC，标注各方法位置。IRT-FIT 在最左下角（最少信息，高 AUROC）。'
953	  analysis: 'Baseline comparison 直接支撑 Claim 1（minimal-information operating point）。IRT-FIT
954	    在信息需求最低的条件下取得了最高的 AUROC——这不是因为 person-fit 比 MIA 更好（在等信息条件下 Min-K%++ 可能更强），而是因为
955	    person-fit 从 binary data 中提取了最大信号量。 Detection frontier diagram 是一个有力的可视化，直接展示了方法论贡献的核心。
956	
957	    '
958	- name: Multiscale lzm Statistic
959	  plan_id: exp-multiscale-lzm
960	  description: '实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021），跨 benchmark 聚合 lz*，
961	    在 PSN-IRT 12 模型 + 控制实验模型上验证。
962	
963	    '
964	  expected_results:
965	    lzm_auroc_15pct: 0.98
966	    lzm_vs_single_benchmark_auroc_gain: 0.02
967	    lzm_cross_benchmark_correlation: 0.67
968	    gemini15_lzm: 18.42
969	    gpt4_lzm: -0.87
970	    clean_model_lzm_mean: 0.03
971	    clean_model_lzm_sd: 0.91
972	    contam_model_lzm_mean_15pct: -7.23
973	    lzm_null_ks_p: 0.312
974	    lzm_power_at_15pct_pooled: 0.99
975	  result_rationale: 'lzm 将多个 benchmark 的 lz* 标准化后求和，利用了跨 benchmark 的信息： 如果一个模型在多个
976	    benchmark 上都有 aberrant pattern，lzm 的信号会累积。 AUROC 从单 benchmark 的 0.96 提升到 0.98
977	    是因为： (1) 信息量增加——5 benchmarks 总共 ~27K items，比单 benchmark 多了判别力； (2) 跨 benchmark
978	    一致性——真正 contaminated 的模型在多个 benchmark 上 lz* 都异常， 而 false positive（某个 benchmark
979	    上偶然异常）不会在 lzm 中累积。 Gemini-1.5 的 lzm = 18.42 极端，因为它在 MMLU 上正侧异常、在 GSM8K/HumanEval
980	    上负侧异常， lzm 用绝对值聚合两侧信号。GPT-4 的 lzm = -0.87 接近零，说明 GPT-4 的 response pattern 在所有
981	    benchmark 上都是 "正常" 的。 Null distribution 校准通过（KS p = 0.312），说明 lzm 在 clean models
982	    上确实近似 N(0,1)。
983	
984	    '
985	  tables:
986	  - name: 'Table 18: lzm Results — PSN-IRT 12 Models'
987	    columns:
988	    - model
989	    - lzm_value
990	    - flagged_alpha005
991	    - n_benchmarks_individual_flag
992	    key_rows:
993	    - - Gemini-1.5
994	      - 18.42
995	      - 'YES'
996	      - 3
997	    - - GPT-4
998	      - -0.87
999	      - 'no'
1000	      - 0
1001	    - - Llama-2-70B
1002	      - -3.21
1003	      - 'YES'
1004	      - 1
1005	    - - Claude-3-Opus
1006	      - 0.42
1007	      - 'no'
1008	      - 0
1009	    - - Mistral-7B
1010	      - -2.45
1011	      - 'no'
1012	      - 0
1013	  - name: 'Table 19: lzm vs Single-Benchmark Detection Power'
1014	    columns:
1015	    - method
1016	    - auroc_15pct
1017	    - power_at_15pct
1018	    - false_alarm_rate
1019	    key_rows:
1020	    - - lz* (MMLU only)
1021	      - 0.96
1022	      - 0.979
1023	      - 0.042
1024	    - - lz* (best single benchmark)
1025	      - 0.96
1026	      - 0.979
1027	      - 0.042
1028	    - - lzm (all benchmarks)
1029	      - 0.98
1030	      - 0.99
1031	      - 0.037
1032	  figures_description:
1033	  - 'Fig 18: lzm 分布——clean models (histogram) + contaminated models (overlay)，标注阈值。'
1034	  - 'Fig 19: 散点图——lzm vs max single-benchmark |lz*|，标注各模型。显示 lzm 提供增量信息。'
1035	  analysis: 'lzm 是一个稳健的 "overall contamination index"，特别适合 leaderboard audit 场景——
1036	    单一指标告诉你 "这个模型总体上是否可疑"。AUROC 增益 0.02 看似不大， 但对 leaderboard-scale 扫描（数千模型），2% 的 precision
1037	    提升意味着减少 ~50 个 false flag。 更重要的叙事价值：lzm 展示了 IRT person-fit 框架的可扩展性——可以从单 benchmark
1038	    到多 benchmark 无缝聚合。
1039	
1040	    '
1041	- name: Post-RL Hypothesis Test
1042	  plan_id: exp-post-rl
1043	  description: '在 Qwen3.5-9B 上先 SFT 污染（15% MMLU items）再 GRPO 训练， 测试 person-fit 信号是否在
1044	    RL 后保持检测力。
1045	
1046	    '
1047	  expected_results:
1048	    pre_rl_lz_star: -8.91
1049	    post_rl_lz_star: -7.12
1050	    post_rl_power_retention_ratio: 0.84
1051	    post_rl_auroc: 0.92
1052	    pre_rl_auroc: 0.96
1053	    auroc_drop_after_rl: 0.04
1054	    post_rl_accuracy_change: 0.012
1055	    post_rl_contam_items_accuracy: 0.82
1056	    pre_rl_contam_items_accuracy: 0.84
1057	    post_rl_non_contam_items_accuracy: 0.75
1058	    pre_rl_non_contam_items_accuracy: 0.74
1059	    post_rl_theta_shift: 0.08
1060	    mia_post_rl_auroc: 0.54
1061	    mia_pre_rl_auroc: 0.71
1062	    person_fit_vs_mia_advantage_post_rl: 0.38
1063	  result_rationale: 'GRPO 后 lz* 信号保留 84% 的机制：GRPO 优化 reward（通常是正确率或 format compliance），
1064	    对已经答对的 contaminated items 不会产生"遗忘"梯度——这些 items 已经获得最大 reward， GRPO 的梯度主要推动模型在
1065	    reward 边界附近的 items 上改进。因此 contaminated items 的 正确率几乎不变（0.84 → 0.82，仅微降 2%），而 non-contaminated
1066	    items 略有提升（+1%）。 lz* 从 -8.91 衰减到 -7.12（~20% 衰减）的原因：GRPO 对 non-contaminated items
1067	    的泛化提升 使 θ 估计上移，缩小了 contaminated items 的 "预期外正确" 幅度。但衰减有限，因为 GRPO 的泛化效应弱于 SFT 的直接
1068	    memorization 效应。 对比 MIA：Wang et al. (2025) 发现 MIA 在 post-RL 后 AUROC 接近随机（0.54），
1069	    因为 RL 重新校准了 token-level probability 分布，消除了 memorization 的 token-level 痕迹。 但 binary
1070	    response pattern 不受 probability recalibration 影响——只要 contaminated items 仍然被答对，person-fit
1071	    信号就存在。这是 person-fit "信息层级优势" 的直接体现： binary outcome 比 token probability 更鲁棒，因为
1072	    RL 可以改变 "how confident the model is" 但很难改变 "whether it gets the answer right"
1073	    on memorized items.
1074	
1075	    '
1076	  tables:
1077	  - name: 'Table 20: Pre- vs Post-RL Person-Fit (Qwen3.5-9B, 15% MMLU Contamination)'
1078	    columns:
1079	    - stage
1080	    - accuracy
1081	    - theta
1082	    - lz_star
1083	    - auroc
1084	    - power
1085	    key_rows:
1086	    - - Clean baseline
1087	      - 0.721
1088	      - 1.42
1089	      - 0.08
1090	      - —
1091	      - —
1092	    - - Post-SFT (contaminated)
1093	      - 0.764
1094	      - 1.63
1095	      - -8.91
1096	      - 0.96
1097	      - 0.97
1098	    - - Post-SFT + GRPO
1099	      - 0.776
1100	      - 1.71
1101	      - -7.12
1102	      - 0.92
1103	      - 0.91
1104	  - name: 'Table 21: Person-Fit vs MIA — Post-RL Robustness'
1105	    columns:
1106	    - method
1107	    - pre_rl_auroc
1108	    - post_rl_auroc
1109	    - auroc_retention
1110	    - info_required
1111	    key_rows:
1112	    - - IRT-FIT (lz*)
1113	      - 0.96
1114	      - 0.92
1115	      - 96%
1116	      - binary responses
1117	    - - Min-K%++
1118	      - 0.88
1119	      - 0.62
1120	      - 70%
1121	      - token log-probs
1122	    - - MIA (reference-based)
1123	      - 0.71
1124	      - 0.54
1125	      - 76%
1126	      - token log-probs + ref model
1127	  - name: 'Table 22: Item-Level Analysis — Accuracy Change After GRPO'
1128	    columns:
1129	    - item_type
1130	    - pre_rl_accuracy
1131	    - post_rl_accuracy
1132	    - change
1133	    key_rows:
1134	    - - contaminated items
1135	      - 0.84
1136	      - 0.82
1137	      - -0.02
1138	    - - non-contaminated items
1139	      - 0.74
1140	      - 0.75
1141	      - 0.01
1142	    - - contaminated hard items (diff>2)
1143	      - 0.79
1144	      - 0.76
1145	      - -0.03
1146	    - - non-contaminated hard items (diff>2)
1147	      - 0.41
1148	      - 0.43
1149	      - 0.02
1150	  figures_description:
1151	  - 'Fig 20: lz* trajectory——clean → post-SFT → post-GRPO，三个阶段的 lz* 值 + CI bar。显示信号有衰减但仍显著。'
1152	  - 'Fig 21: AUROC 对比 bar chart——IRT-FIT vs Min-K%++ vs MIA，pre-RL 和 post-RL 两组。IRT-FIT
1153	    post-RL 仍为 0.92，MIA 跌至 0.54。'
1154	  - 'Fig 22: Item-level accuracy scatterplot，pre-RL (x) vs post-RL (y)，contaminated
1155	    items 标红，non-contaminated 标灰。显示 contaminated items 集中在 (high, high) 区域。'
1156	  analysis: 'Post-RL 实验是论文回应 Wang et al. (2025) 的关键证据。形成清晰对比叙事： "MIA 在 post-RL 后失效（AUROC
1157	    0.54）但 person-fit 保留 84% 信号（AUROC 0.92）， 因为 RL recalibrates probabilities but
1158	    does not undo memorization of correct answers。" 这直接支撑 Claim 1：person-fit 不仅在 minimal-information
1159	    条件下工作， 而且对 post-training 流程具有鲁棒性。机制解释简洁有力：binary outcome > token probability in
1160	    robustness to distribution shift。
1161	
1162	    '
1163	- name: Extra Benchmarks (BBH, MATH)
1164	  plan_id: exp-extra-benchmarks
1165	  description: '添加 BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power
1166	    gap。
1167	
1168	    '
1169	  expected_results:
1170	    bbh_n_items: 6511
1171	    math_n_items: 5000
1172	    bbh_power_at_15pct: 0.89
1173	    math_power_at_15pct: 0.84
1174	    bbh_power_at_5pct: 0.52
1175	    math_power_at_5pct: 0.44
1176	    bbh_predicted_power_from_theory: 0.88
1177	    math_predicted_power_from_theory: 0.83
1178	    theory_prediction_error_bbh: 0.01
1179	    theory_prediction_error_math: 0.01
1180	    bbh_inverted_u_inflection: 0.62
1181	    math_inverted_u_inflection: 0.66
1182	    power_gap_1k_10k_filled: true
1183	  result_rationale: 'BBH (6511 items) 和 MATH (5000 items) 精确填充了 GSM8K (1319) 和 HellaSwag
1184	    (10042) 之间的 power gap。根据 power theory 公式 power ≈ Φ(δ·√n/σ − z_α)： BBH: √6511/√14042
1185	    ≈ 0.68 × MMLU power → 预测 power ≈ 0.88，实测 0.89； MATH: √5000/√14042 ≈ 0.60 × MMLU
1186	    power → 预测 power ≈ 0.83，实测 0.84。 理论预测误差 ≤ 1% 进一步验证了 power theory 的准确性。 BBH 和 MATH
1187	    的 item difficulty 分布不同于 MMLU：BBH 难度更高（mean difficulty ≈ 1.8 vs MMLU 1.2）， MATH
1188	    难度分布更宽（SD ≈ 2.1），这些差异体现在 inverted-U 拐点位置和每 item 信号强度 δ 上， 但 power theory 通过 δ
1189	    参数化吸收了这些差异。
1190	
1191	    '
1192	  tables:
1193	  - name: 'Table 23: Power Gap Analysis — All 7 Benchmarks'
1194	    columns:
1195	    - benchmark
1196	    - n_items
1197	    - power_at_15pct_simulated
1198	    - power_at_15pct_predicted
1199	    - power_at_5pct
1200	    key_rows:
1201	    - - HumanEval
1202	      - 164
1203	      - 0.243
1204	      - 0.231
1205	      - 0.07
1206	    - - ARC-C
1207	      - 1172
1208	      - 0.129
1209	      - 0.142
1210	      - 0.04
1211	    - - GSM8K
1212	      - 1319
1213	      - 0.578
1214	      - 0.561
1215	      - 0.22
1216	    - - MATH
1217	      - 5000
1218	      - 0.84
1219	      - 0.83
1220	      - 0.44
1221	    - - BBH
1222	      - 6511
1223	      - 0.89
1224	      - 0.88
1225	      - 0.52
1226	    - - HellaSwag
1227	      - 10042
1228	      - 0.733
1229	      - 0.748
1230	      - 0.34
1231	    - - MMLU
1232	      - 14042
1233	      - 0.979
1234	      - 0.981
1235	      - 0.78
1236	  figures_description:
1237	  - 'Fig 23: Power vs n_items 理论曲线，7 benchmarks 的数据点全部标注。BBH 和 MATH 精确落在曲线上。'
1238	  analysis: 'BBH 和 MATH 的加入使 power 分析从 5 个 benchmark 扩展到 7 个，覆盖了从 164 (HumanEval)
1239	    到 14042 (MMLU) 的完整 n_items 范围。7 个数据点全部落在理论预测 ±1% 内， 将 power theory 的 R² 从 0.97
1240	    推至接近 0.98。更重要的是 ARC-C 的 power 异常低（0.129 at 1172 items vs GSM8K 的 0.578 at 1319
1241	    items），说明除了 n_items 外 item quality（discrimination）也影响 power， 这在理论公式中通过 δ_per_item
1242	    体现。
1243	
1244	    '
1245	- name: Domain-Level Analysis (MMLU)
1246	  plan_id: exp-domain-analysis
1247	  description: '按 MMLU subject category 分别计算 person-fit，识别 Gemini-1.5 的 MMLU 污染模式。
1248	
1249	    '
1250	  expected_results:
1251	    n_domains_analyzed: 57
1252	    domains_with_extreme_lz_star: 57
1253	    gemini15_domain_lz_star_range: '[+0.8, +12.3]'
1254	    gemini15_domain_lz_star_mean: 4.21
1255	    gemini15_domain_lz_star_sd: 2.87
1256	    gemini15_most_aberrant_domain: abstract_algebra
1257	    gemini15_least_aberrant_domain: high_school_mathematics
1258	    contamination_pattern: uniform across all domains
1259	    domain_level_power_mean: 0.34
1260	    domain_level_power_max: 0.72
1261	    domain_level_n_items_range: '[100, 1534]'
1262	    gpt4_domain_lz_star_sd: 0.82
1263	    gpt4_domains_flagged: 0
1264	  result_rationale: 'Gemini-1.5 在所有 57 个 MMLU domains 上都是 100% 正确率，因此每个 domain 的 lz*
1265	    都为正 （over-consistent pattern）。但各 domain 的 lz* 值不同（range [+0.8, +12.3]）是因为： (1)
1266	    各 domain 的 item 数量不同（100-1534），lz* 信号强度 ∝ √n_items； (2) 各 domain 的 item difficulty
1267	    分布不同——abstract_algebra 有更多高难度 items （mean difficulty ≈ 2.4），100% 正确率与其 difficulty
1268	    分布的偏差更大。 "uniform across all domains" 的发现很重要：它排除了 "Gemini-1.5 只是在特定领域特别强" 的 innocent
1269	    explanation——如果是真实能力，应该在某些 domain 偶尔出错，而不是全面 100%。 Domain-level power 平均仅 0.34
1270	    是因为单 domain 只有 100-1534 items，远少于 full MMLU 的 14K。 这为 power theory 提供了额外验证：57
1271	    个 domain 相当于 57 个不同 n_items 的 "实验"。 GPT-4 在所有 domain 上 lz* 都正常（SD 0.82，接近理论标准差
1272	    1.0），0 个 domain flagged， 作为干净的 negative control。
1273	
1274	    '
1275	  tables:
1276	  - name: 'Table 24: MMLU Domain-Level lz* — Gemini-1.5 vs GPT-4 (Top/Bottom 5 Domains)'
1277	    columns:
1278	    - domain
1279	    - n_items
1280	    - gemini15_acc
1281	    - gemini15_lz_star
1282	    - gpt4_acc
1283	    - gpt4_lz_star
1284	    key_rows:
1285	    - - abstract_algebra
1286	      - 100
1287	      - 1.0
1288	      - 0.83
1289	      - 0.73
1290	      - -0.42
1291	    - - professional_medicine
1292	      - 272
1293	      - 1.0
1294	      - 4.21
1295	      - 0.851
1296	      - 0.67
1297	    - - high_school_mathematics
1298	      - 270
1299	      - 1.0
1300	      - 2.14
1301	      - 0.412
1302	      - -1.23
1303	    - - college_chemistry
1304	      - 100
1305	      - 1.0
1306	      - 0.91
1307	      - 0.47
1308	      - 0.31
1309	    - - global_facts
1310	      - 100
1311	      - 1.0
1312	      - 0.8
1313	      - 0.38
1314	      - -0.87
1315	    - - '...'
1316	      - '...'
1317	      - '...'
1318	      - '...'
1319	      - '...'
1320	      - '...'
1321	    - - miscellaneous
1322	      - 783
1323	      - 1.0
1324	      - 7.89
1325	      - 0.872
1326	      - 0.42
1327	    - - clinical_knowledge
1328	      - 265
1329	      - 1.0
1330	      - 3.87
1331	      - 0.792
1332	      - -0.18
1333	  - name: 'Table 25: Domain-Level Power as Function of n_items'
1334	    columns:
1335	    - n_items_bin
1336	    - n_domains
1337	    - mean_power_at_15pct
1338	    - predicted_from_theory
1339	    key_rows:
1340	    - - 100-150
1341	      - 22
1342	      - 0.18
1343	      - 0.17
1344	    - - 150-300
1345	      - 21
1346	      - 0.31
1347	      - 0.33
1348	    - - 300-600
1349	      - 9
1350	      - 0.52
1351	      - 0.5
1352	    - - 600-1000
1353	      - 3
1354	      - 0.64
1355	      - 0.67
1356	    - - '>1000'
1357	      - 2
1358	      - 0.72
1359	      - 0.74
1360	  figures_description:
1361	  - 'Fig 24: MMLU domain-level lz* heatmap for all 12 models × 57 domains。Gemini-1.5
1362	    行全部为正侧红色。GPT-4 行为中性灰色。'
1363	  - 'Fig 25: Gemini-1.5 domain-level lz* vs domain n_items scatter，显示 √n 依赖关系。'
1364	  analysis: Domain analysis 为 Gemini-1.5 case study 提供了 fine-grained 证据："uniform contamination
1365	    across all 57 MMLU domains" 排除了能力解释（没有任何模型在所有领域同等强）， 支持系统性 benchmark memorization
1366	    的结论。与 GPT-4 的对比提供了干净的 negative control。 Domain-level power 分析作为 bonus，为 power
1367	    theory 提供了 57 个额外的 (n_items, power) 数据点。
1368	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6af57a82-57cb-499c-9d6e-4d1f1d0e1d80",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "4105f7d9-a76e-4a32-81fb-a9566a1c06b3",
  "sourceToolAssistantUUID": "6af57a82-57cb-499c-9d6e-4d1f1d0e1d80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T10:04:57.177Z_

<details open><summary>🔧 Tool call — Read · `toolu_015MYdchLAqJnFK52gfm5ZMj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex",
  "offset": 200,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4105f7d9-a76e-4a32-81fb-a9566a1c06b3",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdceUxBdoSab8bj5ML9",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "10033259-ebd2-4c92-bc5d-9c431092c9cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DtShposCtMsS7guRSPR6VZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28166,
      "cache_read_input_tokens": 20425,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 28166
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 20425,
          "cache_creation_input_tokens": 28166,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 28166,
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

_source line 16 · 2026-05-20T10:04:57.184Z_

<details><summary>↩ Tool result · `toolu_015MYdchLAqJnFK52gfm5ZMj`</summary>

```text
200	50\% & $-$5.73 & $-$2.89 & $-$1.67 & $-$0.43 \\
201	60\% & $-$1.24 & 0.82 & $-$0.34 & 0.21 \\
202	75\% & 8.42 & 5.67 & 3.21 & 1.12 \\
203	90\% & 19.31 & 12.45 & 6.78 & 2.34 \\
204	100\% & 28.50 & 18.20 & 8.70 & 3.01 \\
205	\bottomrule
206	\end{tabular}
207	\end{table}
208	
209	\begin{table}[t]
210	\centering
211	\caption{Two-sided detection power at various contamination levels.}
212	\label{tab:two-sided-power}
213	\small
214	\begin{tabular}{lrrrr}
215	\toprule
216	\textbf{Contam.} & \textbf{MMLU} & \textbf{HSwag} & \textbf{GSM8K} & \textbf{ARC-C} \\
217	\midrule
218	5\% & .780 & .340 & .220 & .060 \\
219	15\% & .979 & .733 & .578 & .129 \\
220	25\% & .998 & .891 & .743 & .201 \\
221	50\% & .872 & .514 & .298 & .080 \\
222	75\% & .991 & .934 & .712 & .187 \\
223	100\% & 1.000 & .998 & .962 & .478 \\
224	\bottomrule
225	\end{tabular}
226	\end{table}
227	
228	Tables~\ref{tab:inverted-u} and \ref{tab:two-sided-power} reveal the inverted-U structure. The $l_z^*$ signal peaks negatively around 25\% contamination (MMLU: $-$12.08), crosses zero near 60--65\%, and becomes strongly positive at high contamination (100\%: +28.50). The inflection point varies by benchmark: 0.65 (MMLU), 0.60 (HellaSwag), 0.70 (GSM8K), consistent with differences in item difficulty distributions. Two-sided power dips at the inflection point (50\% contamination) but recovers for higher levels, whereas one-sided testing would have zero power above the inflection.
229	
230	\subsection{Power Theory Derivation}
231	\label{sec:power-theory}
232	
233	Equation~\ref{eq:power} predicts detection power as a function of $n_{\text{items}}$. Table~\ref{tab:power-theory} shows the theory fits simulation data with $R^2=0.97$.
234	
235	\begin{table}[t]
236	\centering
237	\caption{Theoretical vs.\ simulated power at 15\% contamination.}
238	\label{tab:power-theory}
239	\small
240	\begin{tabular}{rrrr}
241	\toprule
242	$n_{\text{items}}$ & \textbf{Predicted} & \textbf{Simulated} & \textbf{$|\Delta|$} \\
243	\midrule
244	100 & .089 & .092 & .003 \\
245	500 & .312 & .298 & .014 \\
246	1{,}000 & .491 & .503 & .012 \\
247	1{,}319 & .578 & .578 & .000 \\
248	5{,}000 & .862 & .851 & .011 \\
249	10{,}042 & .964 & .958 & .006 \\
250	14{,}042 & .981 & .979 & .002 \\
251	\bottomrule
252	\end{tabular}
253	\end{table}
254	
255	\begin{table}[t]
256	\centering
257	\caption{Inverted-U inflection point: predicted vs.\ observed.}
258	\label{tab:inflection}
259	\small
260	\begin{tabular}{lrrrr}
261	\toprule
262	\textbf{Benchmark} & $n$ & \textbf{Pred.} & \textbf{Obs.} & $|\Delta|$ \\
263	\midrule
264	MMLU & 14{,}042 & 0.64 & 0.65 & 0.01 \\
265	HellaSwag & 10{,}042 & 0.59 & 0.60 & 0.01 \\
266	GSM8K & 1{,}319 & 0.68 & 0.70 & 0.02 \\
267	ARC-C & 1{,}172 & 0.62 & 0.64 & 0.02 \\
268	HumanEval & 164 & 0.61 & 0.63 & 0.02 \\
269	\bottomrule
270	\end{tabular}
271	\end{table}
272	
273	\begin{table}[t]
274	\centering
275	\caption{Minimum $n_{\text{items}}$ for 80\% power at various contamination levels.}
276	\label{tab:min-n}
277	\small
278	\begin{tabular}{lrr}
279	\toprule
280	\textbf{Contam.} & \textbf{Theory} & \textbf{Simulation} \\
281	\midrule
282	5\% & 9{,}800 & 10{,}200 \\
283	10\% & 4{,}700 & 4{,}900 \\
284	15\% & 3{,}200 & 3{,}350 \\
285	25\% & 1{,}800 & 1{,}900 \\
286	\bottomrule
287	\end{tabular}
288	\end{table}
289	
290	Table~\ref{tab:inflection} shows the inflection point can be predicted from item difficulty distributions alone, with error $\leq$0.02. Table~\ref{tab:min-n} provides practitioners with concrete guidance: detecting 15\% contamination requires $\geq$3{,}200 items; detecting 5\% contamination requires $\geq$9{,}800 items. This explains why ARC-C (1{,}172 items) yields only 12.9\% power---not a method failure, but insufficient information.
291	
292	% ============================================================
293	\section{Comparisons and Robustness}
294	\label{sec:comparison}
295	
296	\subsection{Baseline Comparison}
297	\label{sec:baselines}
298	
299	\begin{table}[t]
300	\centering
301	\caption{Baseline comparison on controlled contamination ground truth.}
302	\label{tab:baseline}
303	\small
304	\begin{tabular}{llrrrr}
305	\toprule
306	\textbf{Method} & \textbf{Info Required} & \textbf{5\%} & \textbf{15\%} & \textbf{25\%} & \textbf{Type-I} \\
307	\midrule
308	IRT-FIT & binary & .82 & .96 & .99 & .042 \\
309	ConStat & binary + retest & .61 & .83 & .91 & .053 \\
310	Min-K\%++ & token log-probs & .72 & .88 & .95 & .048 \\
311	\bottomrule
312	\end{tabular}
313	\end{table}
314	
315	\begin{table}[t]
316	\centering
317	\caption{Detection frontier: information access vs.\ detection power (AUROC at 15\% contam.).}
318	\label{tab:frontier}
319	\small
320	\begin{tabular}{llrl}
321	\toprule
322	\textbf{Info Level} & \textbf{Method} & \textbf{AUROC} & \textbf{Scalability} \\
323	\midrule
324	Binary only & IRT-FIT & .96 & Any model w/ scores \\
325	Binary + retest & ConStat & .83 & Requires live access \\
326	Token probs & Min-K\%++ & .88 & Requires API logprobs \\
327	Training data & N-gram & --- & Requires training data \\
328	Weights & Probing & --- & Requires open weights \\
329	\bottomrule
330	\end{tabular}
331	\end{table}
332	
333	IRT-FIT achieves the highest AUROC while requiring the least information (Table~\ref{tab:baseline}). The advantage over ConStat (+0.13 at 15\%) stems from IRT-FIT's use of item-level response patterns rather than aggregate performance statistics. The advantage over Min-K\%++ (+0.08) is notable given that Min-K\%++ has access to richer token-level information. Table~\ref{tab:frontier} positions these results on the detection frontier.
334	
335	\subsection{Post-RL Robustness}
336	\label{sec:post-rl}
337	
338	\citet{wang2025reassessing} show that MIA-based methods fail after reinforcement learning. We test whether IRT-FIT survives post-RL by applying GRPO training to a contaminated Qwen3.5-9B (15\% MMLU SFT contamination).
339	
340	\begin{table}[t]
341	\centering
342	\caption{Pre- vs.\ post-RL person-fit (Qwen3.5-9B, 15\% MMLU contamination).}
343	\label{tab:post-rl}
344	\small
345	\begin{tabular}{lrrrrr}
346	\toprule
347	\textbf{Stage} & \textbf{Acc.} & $\hat{\theta}$ & $l_z^*$ & \textbf{AUROC} & \textbf{Power} \\
348	\midrule
349	Clean & .721 & 1.42 & 0.08 & --- & --- \\
350	Post-SFT & .764 & 1.63 & $-$8.91 & .96 & .97 \\
351	Post-SFT+GRPO & .776 & 1.71 & $-$7.12 & .92 & .91 \\
352	\bottomrule
353	\end{tabular}
354	\end{table}
355	
356	\begin{table}[t]
357	\centering
358	\caption{Person-fit vs.\ MIA: post-RL robustness comparison.}
359	\label{tab:post-rl-comparison}
360	\small
361	\begin{tabular}{lrrrl}
362	\toprule
363	\textbf{Method} & \textbf{Pre-RL} & \textbf{Post-RL} & \textbf{Retain.} & \textbf{Info} \\
364	\midrule
365	IRT-FIT & .96 & .92 & 96\% & binary \\
366	Min-K\%++ & .88 & .62 & 70\% & token probs \\
367	MIA (ref.) & .71 & .54 & 76\% & token probs + ref \\
368	\bottomrule
369	\end{tabular}
370	\end{table}
371	
372	GRPO reduces the $l_z^*$ signal by only 20\% ($-$8.91 $\to$ $-$7.12), retaining 96\% of AUROC (Table~\ref{tab:post-rl}). In contrast, MIA degrades to near-chance (0.54) because RL recalibrates token-level probability distributions while leaving binary response patterns largely intact (Table~\ref{tab:post-rl-comparison}). Item-level analysis confirms: contaminated items retain 97.6\% of their accuracy after GRPO (0.84 $\to$ 0.82), while non-contaminated items gain +1\%. RL changes \emph{how confident} the model is, but not \emph{whether it answers correctly} on memorized items.
373	
374	\subsection{4PL vs.\ 3PL Ablation}
375	\label{sec:ablation}
376	
377	\begin{table}[t]
378	\centering
379	\caption{4PL vs.\ 3PL detection performance.}
380	\label{tab:4pl-3pl}
381	\small
382	\begin{tabular}{lrrr}
383	\toprule
384	\textbf{Metric} & \textbf{4PL} & \textbf{3PL} & $\Delta$ \\
385	\midrule
386	AUROC @ 15\% & .960 & .910 & +.050 \\
387	False alarm ($\alpha$=.05) & .042 & .078 & $-$.036 \\
388	Power @ 15\% MMLU & .979 & .934 & +.045 \\
389	Power @ 5\% MMLU & .780 & .690 & +.090 \\
390	Mean $|l_z^*|$ clean & 0.83 & 1.17 & $-$0.34 \\
391	Mean $|l_z^*|$ contam.\ 15\% & 8.91 & 8.04 & +0.87 \\
392	\bottomrule
393	\end{tabular}
394	\end{table}
395	
396	\begin{table}[t]
397	\centering
398	\caption{Impact of $d$ parameter by item difficulty band.}
399	\label{tab:d-param}
400	\small
401	\begin{tabular}{lrrrr}
402	\toprule
403	\textbf{Difficulty} & $n$ & Mean $d$ & $\Delta l_z^*$ clean & $\Delta l_z^*$ contam. \\
404	\midrule
405	$<0.5$ (easy) & 2{,}814 & .97 & $-$0.08 & 0.12 \\
406	0.5--1.5 & 5{,}621 & .93 & $-$0.21 & 0.43 \\
407	1.5--2.5 & 3{,}891 & .89 & $-$0.38 & 0.78 \\
408	$>2.5$ (hard) & 1{,}716 & .82 & $-$0.67 & 1.45 \\
409	\bottomrule
410	\end{tabular}
411	\end{table}
412	
413	The 4PL model improves over 3PL primarily through better calibration on high-difficulty items (Table~\ref{tab:4pl-3pl}). The $d$ parameter absorbs natural variation in ceiling performance, reducing false alarms from 7.8\% to 4.2\%. The improvement concentrates on items with difficulty $>$2.5, where $d<0.85$ (Table~\ref{tab:d-param}). These are precisely the items where contamination signals are strongest, making the 4PL advantage non-trivial for detection despite modest overall improvement.
414	
415	\subsection{Multiscale $l_{zm}$ Statistic}
416	\label{sec:lzm}
417	
418	\begin{table}[t]
419	\centering
420	\caption{$l_{zm}$ results on PSN-IRT 12 models.}
421	\label{tab:lzm}
422	\small
423	\begin{tabular}{lrrl}
424	\toprule
425	\textbf{Model} & $l_{zm}$ & \textbf{Flag} & \textbf{\#Bench.\ Flagged} \\
426	\midrule
427	Gemini-1.5 & 18.42 & YES & 3 \\
428	GPT-4 & $-$0.87 & no & 0 \\
429	Llama-2-70B & $-$3.21 & YES & 1 \\
430	Claude-3-Opus & 0.42 & no & 0 \\
431	Mistral-7B & $-$2.45 & no & 0 \\
432	\bottomrule
433	\end{tabular}
434	\end{table}
435	
436	\begin{table}[t]
437	\centering
438	\caption{$l_{zm}$ vs.\ single-benchmark detection (15\% contamination).}
439	\label{tab:lzm-vs-single}
440	\small
441	\begin{tabular}{lrrr}
442	\toprule
443	\textbf{Method} & \textbf{AUROC} & \textbf{Power} & \textbf{FA Rate} \\
444	\midrule
445	$l_z^*$ (MMLU only) & .96 & .979 & .042 \\
446	$l_z^*$ (best single) & .96 & .979 & .042 \\
447	$l_{zm}$ (all benchmarks) & .98 & .990 & .037 \\
448	\bottomrule
449	\end{tabular}
450	\end{table}
451	
452	Cross-benchmark aggregation via $l_{zm}$ yields a modest but consistent improvement: AUROC increases from 0.96 to 0.98 (Table~\ref{tab:lzm-vs-single}). The gain comes from information pooling across $\sim$27K total items and from the fact that genuine contamination signals are correlated across benchmarks while false positives are not. The null distribution is well-calibrated (KS $p=0.312$). Gemini-1.5 produces the most extreme $l_{zm}=18.42$, aggregating both positive (MMLU) and negative (GSM8K, HumanEval) regime signals.
453	
454	% ============================================================
455	\section{Large-Scale Empirical Study}
456	\label{sec:empirical}
457	
458	\subsection{Two-Sided Detection on PSN-IRT Models}
459	\label{sec:two-sided}
460	
461	We apply the two-sided framework to 12 models from the PSN-IRT dataset across 5 benchmarks (60 model-benchmark pairs).
462	
463	\begin{table}[t]
464	\centering
465	\caption{Two-sided detection results (selected model-benchmark pairs).}
466	\label{tab:two-sided-results}
467	\small
468	\begin{tabular}{llrrl}
469	\toprule
470	\textbf{Model} & \textbf{Bench.} & $l_z^*$ & \textbf{Side} & \textbf{Flag} \\
471	\midrule
472	Gemini-1.5 & MMLU & +34.75 & positive & YES \\
473	Gemini-1.5 & GSM8K & $-$15.71 & negative & YES \\
474	Gemini-1.5 & HumanEval & $-$12.37 & negative & YES \\
475	GPT-4 & MMLU & $-$1.23 & --- & no \\
476	Llama-2-70B & ARC-C & $-$3.87 & negative & YES \\
477	\bottomrule
478	\end{tabular}
479	\end{table}
480	
481	\begin{table}[t]
482	\centering
483	\caption{One-sided vs.\ two-sided detection comparison (FDR = 0.05).}
484	\label{tab:one-vs-two}
485	\small
486	\begin{tabular}{lrrrr}
487	\toprule
488	\textbf{Method} & \textbf{Total} & \textbf{Partial} & \textbf{Full} & \textbf{FDR} \\
489	\midrule
490	One-sided ($l_z^* < c$) & 2 & 2 & 0 & .05 \\
491	Two-sided ($|l_z^*| > c$) & 4 & 2 & 2 & .05 \\
492	\bottomrule
493	\end{tabular}
494	\end{table}
495	
496	Gemini-1.5 on MMLU ($l_z^*=+34.75$, 95\% CI $[32.1, 37.4]$) exemplifies the positive regime: 100\% accuracy with estimated $\hat{\theta}=0.78$ indicates systematic memorization, not extraordinary ability (Table~\ref{tab:two-sided-results}). One-sided testing completely misses this signal and the two additional flagged models at the positive extreme (Table~\ref{tab:one-vs-two}).
497	
498	\subsection{Leaderboard Audit}
499	\label{sec:leaderboard}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10033259-ebd2-4c92-bc5d-9c431092c9cd",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "75ac190a-7526-4e7f-87b2-4e270953b0a6",
  "sourceToolAssistantUUID": "10033259-ebd2-4c92-bc5d-9c431092c9cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T10:05:02.571Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LBzNkbHVMHSKebnzY8Qw4x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex",
  "offset": 500,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75ac190a-7526-4e7f-87b2-4e270953b0a6",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdd4LeSaU7mVvpuWNj4",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5862b32-96d8-45ea-8dd9-d1b556a85679",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CdwRKVw1GTAkr721m26p3b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5834,
      "cache_read_input_tokens": 48591,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5834
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 48591,
          "cache_creation_input_tokens": 5834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5834,
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

_source line 18 · 2026-05-20T10:05:02.578Z_

<details><summary>↩ Tool result · `toolu_01LBzNkbHVMHSKebnzY8Qw4x`</summary>

```text
500	
501	We run inference on 2{,}847 models from Open LLM Leaderboard v1, computing $l_z^*$ for each model-benchmark pair (18.5 GPU-hours total).
502	
503	\begin{table}[t]
504	\centering
505	\caption{Leaderboard audit summary.}
506	\label{tab:leaderboard}
507	\small
508	\begin{tabular}{lrrrrr}
509	\toprule
510	\textbf{Bench.} & $n$ & \textbf{Neg.} & \textbf{Pos.} & \textbf{Rate} & \textbf{Med.\ $l_z^*$} \\
511	\midrule
512	MMLU & 2{,}847 & 312 & 115 & .15 & $-$6.73 \\
513	HSwag & 2{,}847 & 198 & 58 & .09 & $-$4.21 \\
514	ARC-C & 2{,}847 & 142 & 57 & .07 & $-$3.12 \\
515	GSM8K & 2{,}182 & 178 & 63 & .11 & $-$5.42 \\
516	Overall & 2{,}847 & 255 & 87 & .12 & --- \\
517	\bottomrule
518	\end{tabular}
519	\end{table}
520	
521	\begin{table}[t]
522	\centering
523	\caption{Contamination rate by time period.}
524	\label{tab:temporal}
525	\small
526	\begin{tabular}{lrrr}
527	\toprule
528	\textbf{Period} & \textbf{Models} & \textbf{Flagged} & \textbf{Rate} \\
529	\midrule
530	2023 Q1--Q2 & 487 & 29 & .06 \\
531	2023 Q3--Q4 & 891 & 98 & .11 \\
532	2024 Q1--Q2 & 1{,}103 & 198 & .18 \\
533	2024 Q3+ & 366 & 51 & .14 \\
534	\bottomrule
535	\end{tabular}
536	\end{table}
537	
538	\begin{table}[t]
539	\centering
540	\caption{Most anomalous models (top 3 by $|l_z^*|$).}
541	\label{tab:top-anomalous}
542	\small
543	\begin{tabular}{llrrrl}
544	\toprule
545	\textbf{Model} & \textbf{Bench.} & \textbf{Acc.} & $l_z^*$ & \textbf{Side} & \textbf{Params} \\
546	\midrule
547	anon-7b-v3 & MMLU & .847 & $-$22.4 & neg & 7B \\
548	llm-ft-2b & MMLU & .912 & +18.7 & pos & 2B \\
549	bench-tuned-3b & GSM8K & .891 & $-$17.3 & neg & 3B \\
550	\bottomrule
551	\end{tabular}
552	\end{table}
553	
554	The audit reveals 342 flagged models (12\% overall), with MMLU most affected at 15\% (Table~\ref{tab:leaderboard}). Contamination rates increase from 6\% in early 2023 to 18\% in early 2024 (Table~\ref{tab:temporal}), consistent with the proliferation of benchmark-tuned models on the leaderboard. Table~\ref{tab:top-anomalous} shows the most extreme cases, including a 2B-parameter model achieving 91.2\% MMLU accuracy ($l_z^*=+18.7$) and a 7B model with $l_z^*=-22.4$. Cross-benchmark consistency is 34\%: about one-third of flagged models show anomalies on multiple benchmarks.
555	
556	\subsection{Additional Benchmarks: BBH and MATH}
557	\label{sec:extra-bench}
558	
559	\begin{table}[t]
560	\centering
561	\caption{Power analysis across all 7 benchmarks (15\% contamination).}
562	\label{tab:power-all}
563	\small
564	\begin{tabular}{lrrrr}
565	\toprule
566	\textbf{Benchmark} & $n$ & \textbf{Sim.} & \textbf{Pred.} & \textbf{5\%} \\
567	\midrule
568	HumanEval & 164 & .243 & .231 & .07 \\
569	ARC-C & 1{,}172 & .129 & .142 & .04 \\
570	GSM8K & 1{,}319 & .578 & .561 & .22 \\
571	MATH & 5{,}000 & .840 & .830 & .44 \\
572	BBH & 6{,}511 & .890 & .880 & .52 \\
573	HellaSwag & 10{,}042 & .733 & .748 & .34 \\
574	MMLU & 14{,}042 & .979 & .981 & .78 \\
575	\bottomrule
576	\end{tabular}
577	\end{table}
578	
579	Adding BBH (6{,}511 items) and MATH (5{,}000 items) fills the power gap between GSM8K and HellaSwag (Table~\ref{tab:power-all}). All seven benchmarks fall within 1--2\% of theoretical predictions, further validating the power formula. ARC-C is a notable outlier: its power (0.129) is much lower than GSM8K (0.578) despite similar $n_{\text{items}}$ (1{,}172 vs.\ 1{,}319), indicating that item discrimination quality also affects power---a factor captured by the $\delta$ term in Equation~\ref{eq:power}.
580	
581	\subsection{MMLU Domain-Level Analysis}
582	\label{sec:domain}
583	
584	\begin{table}[t]
585	\centering
586	\caption{MMLU domain-level $l_z^*$: Gemini-1.5 vs.\ GPT-4 (selected domains).}
587	\label{tab:domain}
588	\small
589	\begin{tabular}{lrrrrr}
590	\toprule
591	\textbf{Domain} & $n$ & \multicolumn{2}{c}{\textbf{Gemini-1.5}} & \multicolumn{2}{c}{\textbf{GPT-4}} \\
592	\cmidrule(lr){3-4} \cmidrule(lr){5-6}
593	 & & Acc. & $l_z^*$ & Acc. & $l_z^*$ \\
594	\midrule
595	abstract\_algebra & 100 & 1.00 & +0.83 & .73 & $-$0.42 \\
596	prof\_medicine & 272 & 1.00 & +4.21 & .85 & +0.67 \\
597	hs\_mathematics & 270 & 1.00 & +2.14 & .41 & $-$1.23 \\
598	college\_chem & 100 & 1.00 & +0.91 & .47 & +0.31 \\
599	miscellaneous & 783 & 1.00 & +7.89 & .87 & +0.42 \\
600	clinical\_know & 265 & 1.00 & +3.87 & .79 & $-$0.18 \\
601	\bottomrule
602	\end{tabular}
603	\end{table}
604	
605	\begin{table}[t]
606	\centering
607	\caption{Domain-level power as a function of $n_{\text{items}}$.}
608	\label{tab:domain-power}
609	\small
610	\begin{tabular}{lrrr}
611	\toprule
612	$n_{\text{items}}$ \textbf{bin} & \textbf{Domains} & \textbf{Power} & \textbf{Pred.} \\
613	\midrule
614	100--150 & 22 & .18 & .17 \\
615	150--300 & 21 & .31 & .33 \\
616	300--600 & 9 & .52 & .50 \\
617	600--1{,}000 & 3 & .64 & .67 \\
618	$>$1{,}000 & 2 & .72 & .74 \\
619	\bottomrule
620	\end{tabular}
621	\end{table}
622	
623	Gemini-1.5 achieves 100\% accuracy across all 57 MMLU domains, with uniformly positive $l_z^*$ values ranging from +0.8 to +12.3 (Table~\ref{tab:domain}). This uniformity rules out the innocent explanation that Gemini-1.5 is simply exceptionally strong in certain domains---no model genuinely excels equally across abstract algebra, clinical knowledge, and high school mathematics without occasionally erring. GPT-4, by contrast, shows normally distributed $l_z^*$ (SD=0.82) with zero domains flagged. The 57 MMLU domains provide 57 additional validation points for the power theory (Table~\ref{tab:domain-power}), with predicted power matching observed power within 2--3 percentage points across all domain size bins.
624	
625	% ============================================================
626	\section{Related Work}
627	\label{sec:related}
628	
629	\paragraph{Benchmark contamination detection.}
630	\citet{shi2024detecting} introduce Min-K\%++ for membership inference using token-level likelihood. \citet{oren2024proving} propose Time Travel testing via prompting. \citet{dekoninck2024constat} use performance consistency across rephrased items. \citet{dong2024generalization} study generalization-based detection. \citet{wang2025reassessing} show all MIA-based methods fail post-RL. Our work establishes a strictly lower information requirement.
631	
632	\paragraph{IRT for LLMs.}
633	\citet{polo2024tinybenchmarks} use IRT for efficient benchmarking. \citet{gu2024psnirt} calibrate 4PL IRT models on LLM response data (PSN-IRT). We build on PSN-IRT's item parameters but pivot from benchmarking to contamination detection via person-fit analysis.
634	
635	\paragraph{Person-fit in psychometrics.}
636	\citet{drasgow1985appropriateness} introduce $l_z$; \citet{snijders2001person} derive the corrected $l_z^*$. \citet{meijer2001methodology} survey applications including cheating detection. \citet{hong2021multiscale} propose multiscale aggregation. We are the first to apply person-fit statistics to LLM evaluation.
637	
638	% ============================================================
639	\section{Conclusion}
640	\label{sec:conclusion}
641	
642	We introduced IRT-FIT, a framework that detects benchmark contamination using only binary response patterns---the minimal-information operating point on the detection frontier. Three findings stand out: (1) person-fit statistics achieve AUROC 0.96 at 15\% contamination, surpassing methods requiring token probabilities or re-testing; (2) detection power follows a predictable analytic function of benchmark size ($R^2=0.97$), with the inverted-U signal structure theoretically derivable from item difficulty distributions; (3) a leaderboard-scale audit of 2{,}847 models reveals 12\% overall contamination rates, increasing from 6\% to 18\% over 2023--2024.
643	
644	The person-fit signal survives post-RL training (AUROC 0.92 after GRPO) while MIA degrades to near-chance (0.54), because binary response patterns are robust to the probability recalibration that RL induces. IRT-FIT is the only method that simultaneously addresses partial contamination (aberrant patterns), full contamination (over-consistent patterns), and post-RL contamination at the minimal-information level.
645	
646	\paragraph{Limitations.}
647	Detection power depends on benchmark size: benchmarks with fewer than $\sim$3{,}200 items have limited power at 15\% contamination ($<$80\%). The method targets intentional SFT-style contamination and leaderboard gaming; gradual pretraining exposure that yields smooth capability improvement is not in scope. The 4PL IRT model assumes unidimensionality, which may not hold for heterogeneous benchmarks.
648	
649	% ============================================================
650	\bibliographystyle{plainnat}
651	\begin{thebibliography}{20}
652	
653	\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}
654	Jasper Dekoninck, Mark Niklas M{\"u}ller, and Martin Vechev.
655	\newblock ConStat: Performance-based contamination detection in large language models.
656	\newblock In \emph{NeurIPS}, 2024.
657	
658	\bibitem[Dong et~al.(2024)]{dong2024generalization}
659	Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, and Ge Li.
660	\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.
661	\newblock In \emph{ACL}, 2024.
662	
663	\bibitem[Drasgow et~al.(1985)]{drasgow1985appropriateness}
664	Fritz Drasgow, Michael~V. Levine, and Mary~E. Williams.
665	\newblock Appropriateness measurement with polychotomous item response models and standardized indices.
666	\newblock \emph{British Journal of Mathematical and Statistical Psychology}, 38(1):67--86, 1985.
667	
668	\bibitem[Gu et~al.(2024)]{gu2024psnirt}
669	Guanyu Gu, Yixiao Li, and Yun-Fei Liu.
670	\newblock PSN-IRT: A psychometric benchmark calibration framework for large language models.
671	\newblock In \emph{AAAI}, 2024.
672	
673	\bibitem[Hong et~al.(2021)]{hong2021multiscale}
674	Sophia Hong, David~J. Lin, and Ying Cheng.
675	\newblock Multiscale person-fit statistics.
676	\newblock \emph{Applied Psychological Measurement}, 45(6):417--434, 2021.
677	
678	\bibitem[Meijer and Sijtsma(2001)]{meijer2001methodology}
679	Rob~R. Meijer and Klaas Sijtsma.
680	\newblock Methodology review: Evaluating person fit.
681	\newblock \emph{Applied Psychological Measurement}, 25(2):107--135, 2001.
682	
683	\bibitem[Oren et~al.(2024)]{oren2024proving}
684	Yonatan Oren, Nicole Meister, Niladri~S. Chatterji, Faisal Ladhak, and Tatsunori Hashimoto.
685	\newblock Proving test set contamination in black-box language models.
686	\newblock In \emph{ICLR (Spotlight)}, 2024.
687	
688	\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}
689	Felipe~Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and Mikhail Yurochkin.
690	\newblock tinyBenchmarks: evaluating LLMs with fewer examples.
691	\newblock In \emph{ICML}, 2024.
692	
693	\bibitem[Shi et~al.(2024)]{shi2024detecting}
694	Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.
695	\newblock Detecting pretraining data from large language models.
696	\newblock In \emph{ICLR}, 2024.
697	
698	\bibitem[Snijders(2001)]{snijders2001person}
699	Tom~A.B. Snijders.
700	\newblock Asymptotic null distribution of person fit statistics with estimated item parameters.
701	\newblock \emph{Psychometrika}, 66(3):331--342, 2001.
702	
703	\bibitem[Wang et~al.(2025)]{wang2025reassessing}
704	Cheng Wang, Yiwei Wang, Bryan Hooi, and Yujun Cai.
705	\newblock Reassessing contamination detection: MIA fails under post-RL training.
706	\newblock \emph{arXiv preprint arXiv:2501.xxxxx}, 2025.
707	
708	\end{thebibliography}
709	
710	\end{document}
711	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5862b32-96d8-45ea-8dd9-d1b556a85679",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "3f06e5bc-0ceb-479c-88d5-612aa0eabcbb",
  "sourceToolAssistantUUID": "b5862b32-96d8-45ea-8dd9-d1b556a85679",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-20T10:05:06.630Z_

Now let me also read the experiment data and the paper framing to understand the full context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f06e5bc-0ceb-479c-88d5-612aa0eabcbb",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDddTD4vojUVH7gqUoP6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31dd0fbc-8d8e-4e08-9cc0-f3dba39a14c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXAEhMdk4YS9Lfp8744chD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4798,
      "cache_read_input_tokens": 54425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4798,
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

_source line 20 · 2026-05-20T10:05:09.587Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V4kQ59nUWa8HF67KxLk7zo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31dd0fbc-8d8e-4e08-9cc0-f3dba39a14c3",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDddTD4vojUVH7gqUoP6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "392ddda8-4a61-429c-b41c-71bbcbab15a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXAEhMdk4YS9Lfp8744chD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4798,
      "cache_read_input_tokens": 54425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4798,
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

_source line 21 · 2026-05-20T10:05:09.606Z_

<details><summary>↩ Tool result · `toolu_01V4kQ59nUWa8HF67KxLk7zo`</summary>

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
10	**Claim 1 (Minimal-Information Detection)**:
11	IRT person-fit statistics detect benchmark contamination at the minimal-information operating point on the detection frontier — requiring only binary (correct/incorrect) response patterns, without access to model logits, weights, or training data.
12	
13	**Claim 2 (Detection Characterization)**:
14	Detection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.
15	
16	**Claim 3 (Empirical Prevalence)**:
17	Applying IRT-FIT to publicly available LLM benchmark data reveals previously undocumented contamination patterns — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence, and cross-benchmark anomaly consistency across 12 models from PSN-IRT.
18	
19	## Story Spine
20	
21	**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.
22	
23	**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.
24	
25	**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics (lz*, outfit, infit) — developed over decades for detecting exam cheating — we answer: "What can be detected from binary response patterns alone?" This is a foundational question, not just another detector. We show the method works (97.9% power on MMLU), characterize its limits (power ∝ n_items), and reveal its dual-regime signal structure (partial vs. full contamination).
26	
27	**Headline result template**: "Using only binary response patterns, IRT-FIT detects benchmark contamination with 97.9% power on MMLU (14K items) and identifies Gemini-1.5's 100% MMLU accuracy as contamination (lz*=+34.75) — a signal invisible to existing detectors that require model internals."
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
44	| R6 | "Single-sided test misses full contamination" | Two-sided detection framework is a core contribution. Gemini-1.5 case study demonstrates. | exp-two-sided |
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
55	## MVP Evidence Summary
56	
57	- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed.
58	- **Phase B (real data)**: Gemini-1.5 (student_id=3) MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark: GSM8K lz*=-15.71, HumanEval lz*=-12.37. All benchmarks SD >> 0.5.
59	- **Key insight from MVP**: Two-sided detection is essential — full contamination produces lz* >> 0 (over-consistent), not lz* << 0 (aberrant).
60	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "392ddda8-4a61-429c-b41c-71bbcbab15a0",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "3485d152-8198-4c75-a208-b6335045ef9b",
  "sourceToolAssistantUUID": "392ddda8-4a61-429c-b41c-71bbcbab15a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T10:05:10.083Z_

<details open><summary>🔧 Tool call — Read · `toolu_018uXWUNjwkpVmaxTwPBLrri`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/experiment_data.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3485d152-8198-4c75-a208-b6335045ef9b",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDddTD4vojUVH7gqUoP6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c6b9cba-2c29-4755-8e43-353c9c1120b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXAEhMdk4YS9Lfp8744chD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4798,
      "cache_read_input_tokens": 54425,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4798
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 54425,
          "cache_creation_input_tokens": 4798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4798,
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

_source line 23 · 2026-05-20T10:05:10.096Z_

<details><summary>↩ Tool result · `toolu_018uXWUNjwkpVmaxTwPBLrri`</summary>

```text
1	[
2	  {
3	    "name": "Two-Sided Detection Framework",
4	    "description": "基于 Phase B personfit_matrix.csv，实现 |lz*| > threshold 双侧检测框架， 含 bootstrap CI 和 BH-FDR 控制。验证 Gemini-1.5 case study 中正侧信号。\n",
5	    "results": {
6	      "gemini15_mmlu_lz_star": 34.75,
7	      "gemini15_mmlu_lz_star_bootstrap_95ci": "[32.1, 37.4]",
8	      "gemini15_gsm8k_lz_star": -15.71,
9	      "gemini15_humaneval_lz_star": -12.37,
10	      "two_sided_flagged_models_at_fdr_0.05": 4,
11	      "one_sided_flagged_models_at_fdr_0.05": 2,
12	      "incremental_detection_gain_two_vs_one_sided": "2 additional models flagged (Gemini-1.5 on MMLU, 1 other high-perf model)",
13	      "optimal_negative_threshold_alpha_0.05": -2.81,
14	      "optimal_positive_threshold_alpha_0.05": 3.24,
15	      "positive_regime_models": "Gemini-1.5 (MMLU), possibly Yi-34B or similar near-ceiling model",
16	      "negative_regime_models": "Gemini-1.5 (GSM8K, HumanEval), Llama-2-70B (ARC-C)"
17	    },
18	    "tables": [
19	      {
20	        "name": "Table 1: Two-Sided Detection Results (Phase B, 12 Models × 5 Benchmarks)",
21	        "columns": [
22	          "model",
23	          "benchmark",
24	          "accuracy",
25	          "theta_hat",
26	          "lz_star",
27	          "side",
28	          "flagged_bh_fdr_005",
29	          "bootstrap_95ci"
30	        ],
31	        "key_rows": [
32	          [
33	            "Gemini-1.5",
34	            "MMLU",
35	            1.0,
36	            0.78,
37	            34.75,
38	            "positive",
39	            "YES",
40	            "[32.1, 37.4]"
41	          ],
42	          [
43	            "Gemini-1.5",
44	            "GSM8K",
45	            0.946,
46	            2.41,
47	            -15.71,
48	            "negative",
49	            "YES",
50	            "[-17.2, -14.3]"
51	          ],
52	          [
53	            "Gemini-1.5",
54	            "HumanEval",
55	            0.878,
56	            1.92,
57	            -12.37,
58	            "negative",
59	            "YES",
60	            "[-14.1, -10.8]"
61	          ],
62	          [
63	            "GPT-4",
64	            "MMLU",
65	            0.864,
66	            2.15,
67	            -1.23,
68	            "—",
69	            "no",
70	            "[-2.1, -0.4]"
71	          ],
72	          [
73	            "Llama-2-70B",
74	            "ARC-C",
75	            0.673,
76	            1.08,
77	            -3.87,
78	            "negative",
79	            "YES",
80	            "[-5.2, -2.6]"
81	          ]
82	        ]
83	      },
84	      {
85	        "name": "Table 2: One-Sided vs Two-Sided Detection Comparison",
86	        "columns": [
87	          "method",
88	          "total_flagged",
89	          "partial_contam_detected",
90	          "full_contam_detected",
91	          "FDR_control"
92	        ],
93	        "key_rows": [
94	          [
95	            "one-sided (lz* < threshold)",
96	            2,
97	            2,
98	            0,
99	            "0.05"
100	          ],
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c6b9cba-2c29-4755-8e43-353c9c1120b8",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "480bbf38-0bb4-4f58-842c-74dac0e9458f",
  "sourceToolAssistantUUID": "1c6b9cba-2c29-4755-8e43-353c9c1120b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-20T10:05:14.661Z_

Now let me check whether there is actual experimental code or real experiment results vs. the "imagined" results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "480bbf38-0bb4-4f58-842c-74dac0e9458f",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDde1XGKK77mrvrqZTmm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ea213ba-ffbf-4c35-aae7-c1d25596dff9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YFYmEf4NGL1zfdhBHAvhi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3476,
      "cache_read_input_tokens": 59223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3476,
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

_source line 25 · 2026-05-20T10:05:17.952Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PnJkJFqLmTqEknVkRoouCM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/imagined_experiments.yaml",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ea213ba-ffbf-4c35-aae7-c1d25596dff9",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDde1XGKK77mrvrqZTmm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9db8d845-0303-4784-bf2c-262815b6a134",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YFYmEf4NGL1zfdhBHAvhi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3476,
      "cache_read_input_tokens": 59223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3476,
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

_source line 26 · 2026-05-20T10:05:17.963Z_

<details><summary>↩ Tool result · `toolu_01PnJkJFqLmTqEknVkRoouCM`</summary>

```text
1	tier: best
2	narrative_guidance: '原始 framing 完全成立。三条 claim 均有 ground-truth 支撑：(1) minimal-information
3	  operating point 经控制实验确认——仅 binary 数据即可在 5% 污染水平检测，AUROC>0.93；(2) power ∝ n_items
4	  有解析公式， inverted-U 从经验观察升级为理论命题，拐点位置可预测；(3) Gemini-1.5 case study + leaderboard audit
5	  构成大规模实证贡献。Post-RL 实验直接回应 Wang et al.，形成"MIA 失效但 person-fit 存活"的对比叙事。 Headline: "IRT-FIT
6	  是唯一在 minimal-information 条件下同时解决 partial/full/post-RL 污染的方法"。 EMNLP 主会议无需调整 claim
7	  强度。
8	
9	  '
10	imagined_experiments:
11	- name: Two-Sided Detection Framework
12	  plan_id: exp-two-sided
13	  description: '基于 Phase B personfit_matrix.csv，实现 |lz*| > threshold 双侧检测框架， 含 bootstrap
14	    CI 和 BH-FDR 控制。验证 Gemini-1.5 case study 中正侧信号。
15	
16	    '
17	  expected_results:
18	    gemini15_mmlu_lz_star: 34.75
19	    gemini15_mmlu_lz_star_bootstrap_95ci: '[32.1, 37.4]'
20	    gemini15_gsm8k_lz_star: -15.71
21	    gemini15_humaneval_lz_star: -12.37
22	    two_sided_flagged_models_at_fdr_0.05: 4
23	    one_sided_flagged_models_at_fdr_0.05: 2
24	    incremental_detection_gain_two_vs_one_sided: 2 additional models flagged (Gemini-1.5
25	      on MMLU, 1 other high-perf model)
26	    optimal_negative_threshold_alpha_0.05: -2.81
27	    optimal_positive_threshold_alpha_0.05: 3.24
28	    positive_regime_models: Gemini-1.5 (MMLU), possibly Yi-34B or similar near-ceiling
29	      model
30	    negative_regime_models: Gemini-1.5 (GSM8K, HumanEval), Llama-2-70B (ARC-C)
31	  result_rationale: 'Gemini-1.5 的 MMLU 100% 正确率对应 θ=0.78（远低于满分所需能力），产生极端正侧 lz*=+34.75。
32	    这是因为 full contamination 导致模型在所有 item 上正确，包括远超其真实能力的难题—— response pattern 过度一致（over-consistent），与真正高能力模型的"偶尔失误"模式不符。
33	    负侧信号来自 partial contamination：模型在已污染的难题上正确、在未污染的易题上错误， 产生 aberrant pattern（lz*
34	    << 0）。双侧框架捕获这两类互补信号， 单侧框架只能捕获负侧（partial），遗漏正侧（full）。Bootstrap CI 窄是因为 MMLU 有 14K
35	    items， lz* 的抽样方差 ∝ 1/n_items。FDR 控制在 12 模型 × 5 benchmarks = 60 次检验下仍能保持 power，
36	    因为真阳性的 lz* 绝对值远超阈值（效应量极大）。
37	
38	    '
39	  tables:
40	  - name: 'Table 1: Two-Sided Detection Results (Phase B, 12 Models × 5 Benchmarks)'
41	    columns:
42	    - model
43	    - benchmark
44	    - accuracy
45	    - theta_hat
46	    - lz_star
47	    - side
48	    - flagged_bh_fdr_005
49	    - bootstrap_95ci
50	    key_rows:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9db8d845-0303-4784-bf2c-262815b6a134",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "07ee4a37-6b09-4751-a58f-c4eade0b8e0a",
  "sourceToolAssistantUUID": "9db8d845-0303-4784-bf2c-262815b6a134",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T10:05:18.594Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NDZBgYTpfzCbE45s5gNRnS`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07ee4a37-6b09-4751-a58f-c4eade0b8e0a",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDde1XGKK77mrvrqZTmm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02110b81-05fc-455d-b8df-9c635118c463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019YFYmEf4NGL1zfdhBHAvhi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3476,
      "cache_read_input_tokens": 59223,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3476
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 59223,
          "cache_creation_input_tokens": 3476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3476,
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

_source line 28 · 2026-05-20T10:05:18.606Z_

<details><summary>↩ Tool result · `toolu_01NDZBgYTpfzCbE45s5gNRnS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/memory.md\", \"content\": \"# Memory — irt_personfit_contam\\n\\n## OOM 教训 (2026-05-20)\\n- 7.6GB RAM 机器上，N_SIM×n_items float64 矩阵不能一次性分配。MMLU 10K×14042×8B ≈ 1.07GB 单个矩阵，compute_lz_star 内部创建 ~7 个同尺寸中间数组 → OOM\\n- 解决方案：BATCH_SIZE=500 分批计算 + N_SIM 降至 2000（统计效力足够）\\n- generate_response 和 compute_lz_star 都需要分批\\n\\n## sim_001 关键发现 (2026-05-20)\\n- **Null check 全通过**：PSN-IRT 神经网络估计的 4PL 参数与经典 IRT 兼容，lz* ≈ N(0,1)\\n  - 大 benchmark（GSM8K/HellaSwag/MMLU）KS p 全部 > 0.01\\n  - 小 benchmark（HumanEval/ARC-C）KS p < 0.01，但属预期（items 太少，CLT 近似弱）\\n- **检测力与 n_items 强正相关**：MMLU(14042)=97.9% >> HellaSwag(10042)=73.3% >> GSM8K(1319)=57.8% >> ARC-C(295)=12.9%\\n- **Inverted-U 所有 benchmark 可观测**：power 在 25-50% contamination 达峰，100% 全部 NaN（全答对 → MLE 不收敛）\\n- **Hypothesis 部分证伪**：\\\">80% power at 15% contamination\\\" 仅 MMLU 达标，HellaSwag/GSM8K 未达标。但方法确实 work，只是 power 阈值设得太激进\\n\\n## PSN-IRT 12 模型身份 (2026-05-20)\\n\\n**来源**：arXiv:2505.15055 (AAAI 2026 Oral)，GitHub repo `Joe-Hall-Lee/PSN-IRT`\\n**识别方法**：论文 Section 4.1 列出全部 12 个模型名；`data/combine.csv` 行序 = student_id，经验证为字母序排列。DeepSeek-V3 = student_id=1 由论文 Section 5.2 确认（\\\"ability well above 3.0\\\"）。\\n\\n| student_id | θ | 正确率 | 模型名称 | 类型 | 置信度 |\\n|---|---|---|---|---|---|\\n| 0 | 1.46 | 80.6% | 360GPT2-Pro | API 强模型 | ✅ 确定 |\\n| 1 | 3.77 | 85.7% | DeepSeek-V3 | API 强模型 | ✅ 确定（论文确认） |\\n| 2 | 1.14 | 78.9% | Doubao-pro | API 强模型 | ✅ 确定 |\\n| 3 | 0.78 | 84.5% | Gemini-1.5 | API 强模型 | ✅ 确定 |\\n| 4 | -3.38 | 23.1% | Gemma-2B-it | 开源弱模型(2B) | ✅ 确定 |\\n| 5 | 1.73 | 82.1% | Hunyuan-Turbo | API 强模型 | ✅ 确定 |\\n| 6 | -1.37 | 40.0% | Mistral-7B-Instruct-v0.1 | 开源弱模型(7B) | ✅ 确定 |\\n| 7 | 0.93 | 77.0% | Moonshot-v1 | API 强模型 | ✅ 确定 |\\n| 8 | 0.96 | 76.3% | Qwen-Plus | API 强模型 | ✅ 确定 |\\n| 9 | -0.13 | 60.4% | Qwen2.5-3B-Instruct | 开源弱模型(3B) | ✅ 确定 |\\n| 10 | -1.89 | 31.6% | Vicuna-7B-v1.3 | 开源弱模型(7B) | ✅ 确定 |\\n| 11 | 0.77 | 75.2% | Yi-Lightning | API 强模型 | ✅ 确定 |\\n\\n### 异常 response pattern 观察\\n\\nGemini-1.5 (id=3) 有显著的 raw accuracy 与 IRT ability 不一致：\\n- 正确率排名 #2 (84.5%)，但 θ 排名仅 #7 (0.78)\\n- 这意味着 4PL IRT 模型检测到 Gemini-1.5 的 response pattern 异常（如：容易题答错、难题答对）\\n\\n## Gemini-1.5 × 100% contamination 精确匹配 (2026-05-20)\\n\\n**核心发现**：Gemini-1.5 MMLU lz*(benchmark-specific θ) = +31.815，与 100% contamination 模拟的 lz* = +31.815 **完全一致**（std=0.0, deterministic）。\\n\\n**机制**：100% accuracy → θ_bench MLE = 4.0 (boundary) → lz* 完全由 item parameters 决定。Gemini-1.5 MMLU 100% accuracy 等价于模拟中 100% contamination。\\n\\n**跨 benchmark 对比** (Gemini-1.5 observed lz* vs 100% contamination sim lz*):\\n\\n| Benchmark | Gemini-1.5 lz* (v2) | 100% sim lz* | 匹配？ |\\n|---|---|---|---|\\n| MMLU | +31.815 | +31.815 | ✅ 完全一致 (100% acc → boundary θ) |\\n| HellaSwag | -15.303 | +26.297 | ❌ 方向相反 (87.4% acc, 非全对) |\\n| GSM8K | -7.773 | +8.253 | ❌ 方向相反 (77.9% acc, 非全对) |\\n| ARC-C | +2.050 | +4.339 | 同向但幅度不同 (89.8% acc) |\\n| HumanEval | -3.128 | +3.529 | ❌ 方向相反 (54.3% acc) |\\n\\n**论文意义**：Gemini-1.5 MMLU 的 lz* 与 100% contamination simulation 数值完全匹配，是统计意义上的 \\\"smoking gun\\\"。在其他 benchmark 上 Gemini-1.5 表现正常甚至低于预期（negative lz*），说明 MMLU 上的异常不是模型整体能力导致而是 benchmark-specific 的——符合选择性污染的特征。\\n\\n## exp-extended-sim 关键发现 (2026-05-20)\\n\\n- **100% contamination 不再 NaN**：修复后 n_excluded=0，所有 2000 个模拟均产生有效 lz*\\n- **Dual-regime crossover**：所有 5 个 benchmark 在 75-90% contamination 处 lz* 从负翻正\\n  - 75%: mean lz* 仍为负（MMLU: -7.66, HellaSwag: -4.57）\\n  - 90%: mean lz* 翻正（MMLU: +15.02, HellaSwag: +10.86）\\n- **100% contamination lz* 是 deterministic**（std=0.0）：所有模拟 examinee 100% correct → θ=4.0 → 同一 lz*\\n- **Inverted-U 在所有 5 个 benchmark 确认**\\n- **Left-tail power 在 >75% contamination 急剧下降**：因为 lz* 变正，left-tail (lz* < -1.6449) 无法检测\\n\\n## exp-two-sided 关键教训 (2026-05-20)\\n\\n**发现**：Benchmark-specific θ MLE + parametric bootstrap (N=1000) + BH-FDR (α=0.05) 仍然 flag 57/60 cells (95%)。**LLM response patterns 系统性违反 4PL IRT 假设**，不是少数模型的异常。\\n\\n**根因分析**：\\n- 4PL 假设单维能力 + 局部独立，但 LLM 有知识聚类（correlated item responses）+ 多维能力\\n- Phase A null check 通过是因为模拟数据本身从 4PL 生成，自洽但不代表 real data 符合\\n- lz* 值在 real data 上极端（|lz*|=2-36），1000 次 bootstrap 从未复现，说明偏离是系统性的\\n\\n**方向性判断**：\\n- 绝对阈值检测（|lz*| > 1.96 或 bootstrap p < 0.05）对 real LLM data 无意义——所有模型都 misfit\\n- 可行方向：(1) relative ranking across models, (2) contamination-induced misfit vs natural misfit 对比（需控制实验）, (3) lz* 的方向/幅度差异仍携带信号（正向=over-consistent, 负向=aberrant）\\n- Gemini-1.5 仍是最强 case study：MMLU lz*=+31.8 (100% acc, θ_bench=4.0) vs HellaSwag lz*=-15.3（方向翻转）\\n\\n**对 paper framing 的影响**：\\n- Claim 3 (Empirical Prevalence) 需要重新定义 \\\"flagged\\\"——不能用绝对阈值，需要相对度量\\n- exp-ctrl-contam（控制实验）变得更关键：建立 ground-truth 的 \\\"contaminated misfit\\\" vs \\\"natural misfit\\\" 区分\\n\", \"total_chars\": 4411, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02110b81-05fc-455d-b8df-9c635118c463",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "9422dfa2-1026-47f9-b199-a2a95c3d454a",
  "sourceToolAssistantUUID": "02110b81-05fc-455d-b8df-9c635118c463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-20T10:05:21.457Z_

This is extremely revealing. Let me also check the actual simulation results and the existing review report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9422dfa2-1026-47f9-b199-a2a95c3d454a",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdedxkSrzMJroRxHTva",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2afef108-e163-4ff0-bb11-b1cb8deb261f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jf2NmRtFEp2iou7EW23ehN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4601,
      "cache_read_input_tokens": 62699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4601,
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

_source line 30 · 2026-05-20T10:05:23.823Z_

<details open><summary>🔧 Tool call — Read · `toolu_018zfWdS2dMdwewTN1W82v4k`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2afef108-e163-4ff0-bb11-b1cb8deb261f",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdedxkSrzMJroRxHTva",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd8e21ee-b6fb-49f8-b5bf-dc824a2db27f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jf2NmRtFEp2iou7EW23ehN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4601,
      "cache_read_input_tokens": 62699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4601,
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

_source line 31 · 2026-05-20T10:05:23.828Z_

<details><summary>↩ Tool result · `toolu_018zfWdS2dMdwewTN1W82v4k`</summary>

```text
1	---
2	dream_id: dream_20260520T082549
3	tier: best
4	overall_score: 4/6 Weak Accept
5	timestamp: 2026-05-20T09:14:10.147818+00:00
6	---
7	
8	# Dream Review Report: IRT-FIT
9	
10	**Paper:** IRT-FIT: Detecting Benchmark Contamination in Large Language Models via Item Response Theory Person-Fit Statistics
11	
12	**Review Mode:** Full (2-Reviewer Roundtable)
13	
14	---
15	
16	## Overall Assessment
17	
18	**Score: 4 / 6 (Weak Accept)**
19	
20	The paper presents a well-motivated cross-domain transfer of psychometric person-fit statistics to LLM benchmark contamination detection. The core insight — that a contaminated LLM answering benchmark questions is functionally analogous to an examinee with item preknowledge — is clean and enables a novel "minimal-information operating point" on the contamination detection frontier. The controlled experiments are solid, the power theory provides lasting practical value, and the 2,847-model leaderboard audit is a unique capability no competing method can match. However, several technical issues (lzm null distribution, unidimensionality assumption, narrow post-RL validation) and a critically thin reference list (11 entries) prevent a strong accept. With targeted revisions, this paper would be competitive at a top ML venue.
21	
22	---
23	
24	## Reviewer Scores
25	
26	| Reviewer | Focus | Score | Confidence |
27	|----------|-------|-------|------------|
28	| R1 | Methods + Experiments | 4.0 | 4/5 |
29	| R2 | Novelty + Related Work | 3.5 | 4/5 |
30	| **Consensus** | | **4.0** | **4/5** |
31	
32	---
33	
34	## Strengths
35	
36	### S1. Compelling Framing and Real Gap (R1, R2)
37	The "minimal-information operating point" and "detection frontier" concepts provide a clear organizing principle. The paper precisely identifies where IRT-FIT sits: it requires only binary response data (the least privileged information level), yet achieves AUROC 0.96 at 15% contamination — higher than methods requiring token-level probabilities (Min-K%++ 0.88) or re-testing capabilities (ConStat 0.83). This framing is both intellectually honest and practically important: binary response data is the only information available for retrospective audits of historical leaderboard submissions.
38	
39	### S2. Solid Controlled Experiments (R1)
40	The ground-truth contamination setup via QLoRA SFT on two architectures (Qwen3.5-9B, Gemma-4-31B) across six contamination levels is well-designed. Key findings are convincing:
41	- Cohen's d = 2.3 at 15% contamination (near-complete separation of clean vs. contaminated distributions)
42	- False positive rates well-calibrated (0.042/0.041 at α=0.05)
43	- Contamination selectivity: +31pp on contaminated items, only +1.4-3.7% generalization to non-contaminated items
44	- Cross-architecture consistency (effect sizes differ <15%) rules out model-specific artifacts
45	
46	### S3. Power Theory with Practical Value (R1, R2)
47	The power formula (Eq. 4) fits simulation data with R²=0.97. The inverted-U inflection point prediction (within 0.02 of observed) from item difficulty distributions alone is the paper's strongest theoretical contribution. Table 8 (minimum n_items for 80% power) provides actionable guidance: ≥3,200 items for 15% contamination, ≥9,800 for 5%. This directly explains why ARC-C (1,172 items) yields only 12.9% power — a benchmark-size limitation, not a method failure.
48	
49	### S4. Unique Leaderboard-Scale Audit (R1, R2)
50	The 2,847-model audit is something no other method can replicate at this scale on historical data. The temporal trend (6% → 18% flagged rate from 2023Q1 to 2024Q1) is newsworthy. The Gemini-1.5 case study — 100% MMLU accuracy with θ̂=0.78 yielding lz*=+34.75 — vividly demonstrates the two-sided framework's value: one-sided testing would completely miss this full-contamination signal.
51	
52	### S5. Two-Sided Framework is a Genuine Observation (R2)
53	The identification of two contamination regimes (partial: lz* << 0 from aberrant patterns; full: lz* >> 0 from over-consistent patterns) is non-obvious from the psychometrics literature. The inverted-U empirical structure connecting these regimes is a new finding. While the statistical test (|lz*| > c_{α/2}) is straightforward, the observation motivating it is substantive.
54	
55	---
56	
57	## Weaknesses
58	
59	### W1. lzm Null Distribution Error (R1) — **Major**
60	Equation 3 defines lzm = (1/√K) Σ|lz*_k|. Under the null, each lz* ~ N(0,1), so |lz*| follows a half-normal distribution (mean ≈ 0.798, SD ≈ 0.603). The sum of half-normals is NOT N(0,1). The paper claims lzm is "approximately standard normal" verified by KS test (p=0.312), but this cannot be correct for the formula as written. Either: (a) the actual implementation uses signed lz* values (which would make lzm ~ N(0,1) by CLT), contradicting the absolute-value formula; or (b) the KS test was performed against the wrong null distribution. This is a correctness issue that must be resolved.
61	
62	### W2. Critically Thin Reference List (R2) — **Major**
63	11 references is far below the expected density for a top ML venue (typically 30-50+). Critical omissions include:
64	- **Contamination detection:** Golchin & Surdeanu (2024), Sainz et al. (2023), Yang et al. (2023); no survey/position papers on contamination
65	- **IRT for NLP/AI:** Lalor et al. (2019), Vania et al. (2021), Martinez-Plumed et al. (2019)
66	- **Person-fit:** Karabatsos (2003) comparing 36 person-fit statistics (why lz* over alternatives?), Sinharay (2017) on preknowledge detection power (the most directly relevant psychometric precedent)
67	- **Test security:** Wollack & Schoenig (2018) and CAT-based cheating detection literature
68	
69	This gap undermines the novelty claim — without surveying the full person-fit literature, reviewers cannot assess what is genuinely new.
70	
71	### W3. Unfair Baseline Comparison (R1, R2) — **Moderate**
72	ConStat is designed to detect contamination via performance inconsistency on rephrased items. SFT contamination permanently alters model weights, making re-test scores nearly identical — this inherently disadvantages ConStat. The comparison is valid in the sense that IRT-FIT works where ConStat cannot, but calling it "outperformance" without acknowledging the threat-model mismatch is misleading. Additionally:
73	- Min-K%++ operates on raw text, not MCQA binary responses. The information hierarchy (binary < token probs) is not a strict difficulty ordering.
74	- IRT-FIT requires pre-calibrated 4PL item parameters (from PSN-IRT), which is itself a substantial prerequisite. This dependency should be explicitly listed alongside the "binary responses only" claim.
75	- No confidence intervals on AUROC values. The 0.96 vs 0.88 difference may not be statistically significant given sample sizes.
76	
77	### W4. Narrow Post-RL Validation (R1) — **Moderate**
78	The post-RL experiment tests only GRPO on one model (Qwen3.5-9B) at one contamination level (15% MMLU). The claim that "person-fit survives post-RL training" is stated broadly but tested narrowly. Missing:
79	- Other RL algorithms (PPO, DPO, KTO)
80	- Other base models
81	- Other contamination levels
82	- Multiple RL training durations (does signal degrade with more RL steps?)
83	
84	The AUROC retention (96%) is impressive but could be an artifact of the specific GRPO configuration tested.
85	
86	### W5. Unidimensionality Assumption (R1) — **Moderate**
87	The 4PL IRT model assumes unidimensional ability (single θ). MMLU spans 57 diverse domains. Snijders' N(0,1) null distribution guarantee requires correct model specification. If the IRT model is misspecified, lz* under the null may deviate from N(0,1), inflating false positives. The paper's FPR of 0.042 at α=0.05 is slightly below nominal, suggesting the calibration is adequate empirically, but the theoretical justification is incomplete. This is acknowledged in the Limitations section but deserves deeper analysis — particularly for the leaderboard audit where models may have genuinely multidimensional ability profiles.
88	
89	### W6. Leaderboard Audit Lacks Ground Truth (R1) — **Minor**
90	The 12% flagged rate is not 12% contamination rate. Without external validation (e.g., correlation with known contaminated models, independent contamination audits), the audit results are suggestive but not confirmatory. The paper should distinguish "statistically anomalous response pattern" from "confirmed contamination." The time trend could also reflect model architecture/size trends rather than increasing contamination.
91	
92	### W7. QLoRA-Specific Contamination (R2) — **Minor**
93	Controlled experiments use QLoRA SFT exclusively. The generalization ratio (0.12) and selectivity pattern may differ under full-parameter SFT, continued pretraining with benchmark items mixed into other data, or paraphrased benchmark items. These alternative contamination pathways should be discussed.
94	
95	---
96	
97	## Questions for Authors
98	
99	1. **lzm formula vs. implementation:** Does the actual code compute lzm using |lz*| (absolute values as in Eq. 3) or signed lz* values? If absolute values, what is the correct null distribution? The claimed KS test against N(0,1) appears inconsistent with the formula.
100	
101	2. **PSN-IRT parameter sensitivity:** How robust are the results to perturbations in the IRT item parameters? If the 4PL parameters from PSN-IRT have estimation error (calibrated on only 12 models), how much does lz* drift? A sensitivity analysis would strengthen the method's credibility.
102	
103	3. **Pretraining contamination:** The Limitations section acknowledges this is out of scope. Can you provide even a rough estimate of what happens when contamination comes via pretraining exposure (which produces smoother generalization) rather than SFT memorization?
104	
105	4. **Adversarial inflection-point targeting:** Given that the inverted-U inflection point is predictable from item difficulty distributions, could a sophisticated adversary deliberately contaminate at exactly the inflection fraction to evade detection? How would you defend against this?
106	
107	5. **Missing baselines:** Why were CoDeC and recent post-RL-aware contamination detection methods not compared? Would you be willing to add these in a revision?
108	
109	---
110	
111	## Experiment Coverage Assessment
112	
113	Compared to the full experiment design (review_context.yaml), the paper covers all 11 planned experiments:
114	
115	| Experiment | Status | Tables |
116	|-----------|--------|--------|
117	| Two-Sided Detection | ✅ Fully covered | 17, 18 |
118	| Extended Simulation | ✅ Fully covered | 4, 5 |
119	| Controlled Contamination | ✅ Fully covered | 1, 2, 3 |
120	| Power Theory | ✅ Fully covered | 6, 7, 8 |
121	| Leaderboard Audit | ✅ Fully covered | 19, 20, 21 |
122	| 4PL vs 3PL Ablation | ✅ Fully covered | 13, 14 |
123	| Baseline Comparison | ✅ Fully covered | 9, 10 |
124	| Multiscale lzm | ✅ Fully covered | 15, 16 |
125	| Post-RL Hypothesis | ✅ Fully covered | 11, 12 |
126	| Extra Benchmarks | ✅ Fully covered | 22 |
127	| Domain Analysis | ✅ Fully covered | 23, 24 |
128	
129	All planned experiments are present. The paper's experimental scope is comprehensive and matches the design specification.
130	
131	---
132	
133	## Recommendations for Revision
134	
135	**Must-fix (for acceptance):**
136	1. Correct lzm null distribution — either fix the formula or provide the correct null
137	2. Expand reference list to 30+ entries covering contamination detection, IRT-for-NLP, person-fit literature
138	3. Add AUROC confidence intervals throughout
139	4. Acknowledge PSN-IRT item bank as an explicit dependency in the "information requirements" framing
140	
141	**Strongly recommended:**
142	5. Broaden post-RL validation (at minimum, one additional RL algorithm or model)
143	6. Discuss ConStat comparison fairness: acknowledge different threat models
144	7. Add discussion of unidimensionality violation and its empirical impact
145	8. Distinguish "flagged" from "contaminated" in leaderboard audit language
146	
147	**Nice to have:**
148	9. Add CoDeC / Self-Critique baselines
149	10. Discuss pretraining contamination pathway even if out of scope
150	11. Consolidate some tables to reduce density (24 tables in 11 pages is heavy)
151	
152	---
153	
154	## Final Verdict
155	
156	**Score: 4 / 6 (Weak Accept)**
157	
158	The paper makes a genuine contribution: it identifies a new operating point on the contamination detection frontier, provides a theoretically grounded power analysis, and demonstrates unique large-scale audit capability. The core methodology is sound modulo the lzm issue. The controlled experiments are well-designed and convincing. The main barriers to a strong accept are: (1) a fixable but non-trivial technical error in the lzm statistic, (2) a critically thin reference list that obscures the novelty claim, and (3) insufficient discussion of method dependencies and comparison fairness. These are all addressable in revision. The paper is above the acceptance threshold for a top ML venue but needs the revisions listed above to be convincing.
159	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd8e21ee-b6fb-49f8-b5bf-dc824a2db27f",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "e24de6ec-ffc5-46d0-baac-ac16d83a11f1",
  "sourceToolAssistantUUID": "bd8e21ee-b6fb-49f8-b5bf-dc824a2db27f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T10:05:24.474Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K7nsi8uLY1nn4x23NSpJfL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/phase_b_two_sided_v2/analysis_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e24de6ec-ffc5-46d0-baac-ac16d83a11f1",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdedxkSrzMJroRxHTva",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb13a32e-1997-4174-9d07-d03ef15a7be7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jf2NmRtFEp2iou7EW23ehN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4601,
      "cache_read_input_tokens": 62699,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4601
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 62699,
          "cache_creation_input_tokens": 4601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4601,
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

_source line 33 · 2026-05-20T10:05:24.479Z_

<details><summary>↩ Tool result · `toolu_01K7nsi8uLY1nn4x23NSpJfL`</summary>

```text
1	# Two-sided Detection v2 — Analysis Report
2	
3	## Method
4	- **θ estimation**: Benchmark-specific MLE (not global PSN-IRT θ)
5	- **Null distribution**: Parametric bootstrap (N=1000) per cell
6	- **Multiple testing**: Benjamini-Hochberg FDR at α=0.05
7	
8	## Key Results
9	
10	### Flagging rate: 57/60 (95.0%)
11	
12	v1 flagged 56/60 (93.3%) using global θ + |lz*|>1.96 threshold.
13	v2 flags 57/60 (95.0%) after correcting θ estimation and using empirical null with BH-FDR.
14	
15	The flagged rate remains high (95.0%) even after correcting θ estimation. This means the v1 over-flagging was NOT primarily due to global θ bias — the 4PL IRT model genuinely does not fit LLM response patterns at the item level.
16	
17	The lz* values are extreme (|lz*| >> 2 for most cells), and even 1000 bootstrap replicates under the 4PL model cannot reproduce such deviations. This is strong evidence that LLM responses violate 4PL assumptions:
18	  - Local independence: LLMs have correlated item responses (knowledge clusters)
19	  - Unidimensionality: even within a single benchmark, LLM abilities are multi-faceted
20	  - Monotonicity: LLMs may exhibit non-monotonic response patterns on certain items
21	
22	### Gemini-1.5 on MMLU
23	- Accuracy: 100% (θ_bench = 4.0, boundary value)
24	- lz*: 31.815
25	- Empirical p-value: 0.0
26	- Flagged (BH): True
27	
28	Gemini-1.5 achieves 100% on MMLU, pushing θ_bench to the boundary (4.0). At boundary θ, lz* may be unreliable because the MLE is constrained — the Fisher information correction in lz* assumes an interior optimum. The bootstrap null appropriately handles this: bootstrap replicates can also hit the boundary, so the empirical p-value remains valid even when the asymptotic N(0,1) approximation breaks down.
29	
30	### Calibration gap: global θ vs benchmark-specific θ
31	
32	| Benchmark | Mean gap (θ_bench − θ_global) | Std | Min | Max |
33	|-----------|-------------------------------|-----|-----|-----|
34	| arc_c | +0.430 | 1.259 | -2.106 | +2.541 |
35	| gsm8k | +0.227 | 1.004 | -1.136 | +2.860 |
36	| hellaswag | +0.405 | 1.054 | -1.150 | +2.571 |
37	| humaneval | +0.230 | 1.294 | -2.106 | +3.043 |
38	| mmlu | +0.361 | 0.911 | -0.350 | +3.223 |
39	
40	The gap between global and benchmark-specific θ varies substantially across benchmarks, confirming that a single global θ misrepresents model ability on individual benchmarks. However, the high flagging rate persists even with benchmark-specific θ, meaning the calibration gap is a secondary issue — the primary issue is 4PL model misfit.
41	
42	### Per-benchmark detail
43	
44	**arc_c** (n_items=295)
45	  - 360GPT2-Pro: θ_global=1.459, θ_bench=4.000, acc=0.963, lz*=2.898, p_emp=0.0080, p_adj=0.0092 **FLAGGED**
46	  - DeepSeek-V3: θ_global=3.772, θ_bench=2.460, acc=0.925, lz*=3.022, p_emp=0.0020, p_adj=0.0026 **FLAGGED**
47	  - Doubao-pro: θ_global=1.140, θ_bench=1.098, acc=0.885, lz*=2.324, p_emp=0.0250, p_adj=0.0268 **FLAGGED**
48	  - Gemini-1.5: θ_global=0.777, θ_bench=1.261, acc=0.898, lz*=2.050, p_emp=0.0460, p_adj=0.0484 **FLAGGED**
49	  - Gemma-2B-it: θ_global=-3.378, θ_bench=-2.374, acc=0.451, lz*=6.214, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
50	  - Hunyuan-Turbo: θ_global=1.732, θ_bench=4.000, acc=0.966, lz*=3.569, p_emp=0.0010, p_adj=0.0014 **FLAGGED**
51	  - Mistral-7B-Instruct-v0.1: θ_global=-1.365, θ_bench=-0.878, acc=0.702, lz*=5.597, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
52	  - Moonshot-v1: θ_global=0.926, θ_bench=1.621, acc=0.915, lz*=2.746, p_emp=0.0070, p_adj=0.0082 **FLAGGED**
53	  - Qwen-Plus: θ_global=0.957, θ_bench=2.121, acc=0.925, lz*=2.851, p_emp=0.0070, p_adj=0.0082 **FLAGGED**
54	  - Qwen2.5-3B-Instruct: θ_global=-0.125, θ_bench=0.155, acc=0.844, lz*=3.434, p_emp=0.0010, p_adj=0.0014 **FLAGGED**
55	  - Vicuna-7B-v1.3: θ_global=-1.894, θ_bench=-4.000, acc=0.237, lz*=2.979, p_emp=0.0020, p_adj=0.0026 **FLAGGED**
56	  - Yi-Lightning: θ_global=0.772, θ_bench=0.466, acc=0.841, lz*=1.664, p_emp=0.0950, p_adj=0.0983
57	
58	**gsm8k** (n_items=1319)
59	  - 360GPT2-Pro: θ_global=1.459, θ_bench=2.184, acc=0.901, lz*=7.216, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
60	  - DeepSeek-V3: θ_global=3.772, θ_bench=4.000, acc=0.951, lz*=7.894, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
61	  - Doubao-pro: θ_global=1.140, θ_bench=4.000, acc=0.914, lz*=2.650, p_emp=0.0120, p_adj=0.0131 **FLAGGED**
62	  - Gemini-1.5: θ_global=0.777, θ_bench=0.386, acc=0.779, lz*=-7.773, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
63	  - Gemma-2B-it: θ_global=-3.378, θ_bench=-4.000, acc=0.132, lz*=10.019, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
64	  - Hunyuan-Turbo: θ_global=1.732, θ_bench=0.780, acc=0.814, lz*=6.749, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
65	  - Mistral-7B-Instruct-v0.1: θ_global=-1.365, θ_bench=-1.364, acc=0.423, lz*=11.658, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
66	  - Moonshot-v1: θ_global=0.926, θ_bench=1.250, acc=0.861, lz*=7.799, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
67	  - Qwen-Plus: θ_global=0.957, θ_bench=1.708, acc=0.882, lz*=7.174, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
68	  - Qwen2.5-3B-Instruct: θ_global=-0.125, θ_bench=0.115, acc=0.739, lz*=10.821, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
69	  - Vicuna-7B-v1.3: θ_global=-1.894, θ_bench=-3.030, acc=0.175, lz*=8.630, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
70	  - Yi-Lightning: θ_global=0.772, θ_bench=1.471, acc=0.875, lz*=6.030, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
71	
72	**hellaswag** (n_items=10042)
73	  - 360GPT2-Pro: θ_global=1.459, θ_bench=2.734, acc=0.913, lz*=16.040, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
74	  - DeepSeek-V3: θ_global=3.772, θ_bench=2.622, acc=0.905, lz*=14.808, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
75	  - Doubao-pro: θ_global=1.140, θ_bench=1.074, acc=0.861, lz*=17.739, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
76	  - Gemini-1.5: θ_global=0.777, θ_bench=1.144, acc=0.874, lz*=-15.303, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
77	  - Gemma-2B-it: θ_global=-3.378, θ_bench=-3.613, acc=0.291, lz*=23.931, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
78	  - Hunyuan-Turbo: θ_global=1.732, θ_bench=4.000, acc=0.952, lz*=20.420, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
79	  - Mistral-7B-Instruct-v0.1: θ_global=-1.365, θ_bench=-1.362, acc=0.530, lz*=31.855, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
80	  - Moonshot-v1: θ_global=0.926, θ_bench=3.497, acc=0.930, lz*=13.234, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
81	  - Qwen-Plus: θ_global=0.957, θ_bench=0.382, acc=0.794, lz*=8.241, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
82	  - Qwen2.5-3B-Instruct: θ_global=-0.125, θ_bench=0.007, acc=0.766, lz*=18.862, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
83	  - Vicuna-7B-v1.3: θ_global=-1.894, θ_bench=-1.679, acc=0.476, lz*=28.378, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
84	  - Yi-Lightning: θ_global=0.772, θ_bench=0.829, acc=0.848, lz*=18.010, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
85	
86	**humaneval** (n_items=164)
87	  - 360GPT2-Pro: θ_global=1.459, θ_bench=1.806, acc=0.860, lz*=1.504, p_emp=0.1320, p_adj=0.1342
88	  - DeepSeek-V3: θ_global=3.772, θ_bench=4.000, acc=0.915, lz*=2.348, p_emp=0.0120, p_adj=0.0131 **FLAGGED**
89	  - Doubao-pro: θ_global=1.140, θ_bench=0.554, acc=0.750, lz*=2.529, p_emp=0.0100, p_adj=0.0113 **FLAGGED**
90	  - Gemini-1.5: θ_global=0.777, θ_bench=-0.244, acc=0.543, lz*=-3.128, p_emp=0.0020, p_adj=0.0026 **FLAGGED**
91	  - Gemma-2B-it: θ_global=-3.378, θ_bench=-3.350, acc=0.183, lz*=3.823, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
92	  - Hunyuan-Turbo: θ_global=1.732, θ_bench=4.000, acc=0.939, lz*=2.831, p_emp=0.0050, p_adj=0.0062 **FLAGGED**
93	  - Mistral-7B-Instruct-v0.1: θ_global=-1.365, θ_bench=-1.644, acc=0.341, lz*=4.231, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
94	  - Moonshot-v1: θ_global=0.926, θ_bench=1.171, acc=0.823, lz*=3.808, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
95	  - Qwen-Plus: θ_global=0.957, θ_bench=4.000, acc=0.927, lz*=2.813, p_emp=0.0060, p_adj=0.0073 **FLAGGED**
96	  - Qwen2.5-3B-Instruct: θ_global=-0.125, θ_bench=0.134, acc=0.726, lz*=3.523, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
97	  - Vicuna-7B-v1.3: θ_global=-1.894, θ_bench=-4.000, acc=0.140, lz*=3.063, p_emp=0.0020, p_adj=0.0026 **FLAGGED**
98	  - Yi-Lightning: θ_global=0.772, θ_bench=1.110, acc=0.823, lz*=1.354, p_emp=0.1810, p_adj=0.1810
99	
100	**mmlu** (n_items=14042)
101	  - 360GPT2-Pro: θ_global=1.459, θ_bench=1.748, acc=0.831, lz*=19.789, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
102	  - DeepSeek-V3: θ_global=3.772, θ_bench=3.422, acc=0.867, lz*=18.236, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
103	  - Doubao-pro: θ_global=1.140, θ_bench=1.410, acc=0.844, lz*=-21.333, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
104	  - Gemini-1.5: θ_global=0.777, θ_bench=4.000, acc=1.000, lz*=31.815, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
105	  - Gemma-2B-it: θ_global=-3.378, θ_bench=-3.077, acc=0.335, lz*=24.701, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
106	  - Hunyuan-Turbo: θ_global=1.732, θ_bench=1.505, acc=0.821, lz*=16.565, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
107	  - Mistral-7B-Instruct-v0.1: θ_global=-1.365, θ_bench=-1.168, acc=0.533, lz*=34.901, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
108	  - Moonshot-v1: θ_global=0.926, θ_bench=0.873, acc=0.779, lz*=20.216, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
109	  - Qwen-Plus: θ_global=0.957, θ_bench=1.399, acc=0.819, lz*=36.154, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
110	  - Qwen2.5-3B-Instruct: θ_global=-0.125, θ_bench=-0.303, acc=0.653, lz*=26.193, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
111	  - Vicuna-7B-v1.3: θ_global=-1.894, θ_bench=-2.109, acc=0.391, lz*=27.390, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
112	  - Yi-Lightning: θ_global=0.772, θ_bench=1.401, acc=0.819, lz*=36.128, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
113	
114	## Methodological finding
115	
116	Switching from global to benchmark-specific θ corrects the ability estimation bias but does NOT resolve the high flagging rate. This reveals a deeper issue: the 4PL IRT model is fundamentally inadequate for modeling LLM response patterns.
117	
118	LLM responses violate core IRT assumptions even within homogeneous benchmarks. The massive lz* values (often 10-30+) indicate systematic, not marginal, misfit. This has implications for any IRT-based contamination detection method — the signal-to-noise ratio of person-fit statistics is dominated by model misfit, making it difficult to isolate genuine contamination signals.
119	
120	The parametric bootstrap with benchmark-specific θ provides the most rigorous calibration available within the 4PL framework. The persistent flagging is therefore a property of the LLM-IRT interaction, not a statistical artifact.
121	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb13a32e-1997-4174-9d07-d03ef15a7be7",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "15962e52-96da-49ec-b570-a96d7f6aaf9b",
  "sourceToolAssistantUUID": "bb13a32e-1997-4174-9d07-d03ef15a7be7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-20T10:05:26.943Z_

Now let me check the simulation results to compare against what the paper claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15962e52-96da-49ec-b570-a96d7f6aaf9b",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdf52dVpBBt8TmstBzT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "279e2bfd-1961-4c6f-93f0-fe65f4f8cfd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012R1vVPsdymDm42Gsm5ZCLo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9450,
      "cache_read_input_tokens": 67300,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9450,
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

_source line 35 · 2026-05-20T10:05:28.829Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EAZujyZGmYnAzBgWUWta3P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/sim_001/data/simulation_summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "279e2bfd-1961-4c6f-93f0-fe65f4f8cfd3",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdf52dVpBBt8TmstBzT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bb5f7044-837b-485e-96e8-0bd10511cc47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012R1vVPsdymDm42Gsm5ZCLo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9450,
      "cache_read_input_tokens": 67300,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9450,
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

_source line 36 · 2026-05-20T10:05:28.836Z_

<details><summary>↩ Tool result · `toolu_01EAZujyZGmYnAzBgWUWta3P`</summary>

```text
1	{
2	  "global_pass": false,
3	  "all_large_benchmarks_pass": false,
4	  "inverted_u_observable": true,
5	  "benchmarks": {
6	    "humaneval": {
7	      "n_items": 164,
8	      "tier": "small",
9	      "contamination_levels": {
10	        "0": {
11	          "n_sims": 1000,
12	          "n_excluded": 0,
13	          "detection_rate": 0.061,
14	          "mean_lz_star": 0.043,
15	          "std_lz_star": 1.0031
16	        },
17	        "3": {
18	          "n_sims": 1000,
19	          "n_excluded": 0,
20	          "detection_rate": 0.082,
21	          "mean_lz_star": -0.1729,
22	          "std_lz_star": 1.0071
23	        },
24	        "5": {
25	          "n_sims": 1000,
26	          "n_excluded": 0,
27	          "detection_rate": 0.09,
28	          "mean_lz_star": -0.2925,
29	          "std_lz_star": 1.0325
30	        },
31	        "10": {
32	          "n_sims": 1000,
33	          "n_excluded": 0,
34	          "detection_rate": 0.151,
35	          "mean_lz_star": -0.5381,
36	          "std_lz_star": 1.1302
37	        },
38	        "15": {
39	          "n_sims": 1000,
40	          "n_excluded": 0,
41	          "detection_rate": 0.243,
42	          "mean_lz_star": -0.898,
43	          "std_lz_star": 1.2317
44	        },
45	        "25": {
46	          "n_sims": 1000,
47	          "n_excluded": 0,
48	          "detection_rate": 0.409,
49	          "mean_lz_star": -1.4074,
50	          "std_lz_star": 1.4328
51	        },
52	        "50": {
53	          "n_sims": 1000,
54	          "n_excluded": 0,
55	          "detection_rate": 0.571,
56	          "mean_lz_star": -1.8677,
57	          "std_lz_star": 2.0444
58	        },
59	        "100": {
60	          "n_sims": 0,
61	          "n_excluded": 1000,
62	          "detection_rate": 0.0,
63	          "mean_lz_star": NaN,
64	          "std_lz_star": NaN
65	        }
66	      },
67	      "pass_15pct": false,
68	      "threshold": 0.5,
69	      "inverted_u_detected": true
70	    },
71	    "arc_c": {
72	      "n_items": 295,
73	      "tier": "small",
74	      "contamination_levels": {
75	        "0": {
76	          "n_sims": 1000,
77	          "n_excluded": 0,
78	          "detection_rate": 0.062,
79	          "mean_lz_star": 0.0292,
80	          "std_lz_star": 1.0108
81	        },
82	        "3": {
83	          "n_sims": 1000,
84	          "n_excluded": 0,
85	          "detection_rate": 0.063,
86	          "mean_lz_star": -0.0347,
87	          "std_lz_star": 1.0032
88	        },
89	        "5": {
90	          "n_sims": 1000,
91	          "n_excluded": 0,
92	          "detection_rate": 0.075,
93	          "mean_lz_star": -0.1202,
94	          "std_lz_star": 1.0035
95	        },
96	        "10": {
97	          "n_sims": 1000,
98	          "n_excluded": 0,
99	          "detection_rate": 0.085,
100	          "mean_lz_star": -0.2306,
101	          "std_lz_star": 1.0201
102	        },
103	        "15": {
104	          "n_sims": 1000,
105	          "n_excluded": 0,
106	          "detection_rate": 0.129,
107	          "mean_lz_star": -0.3566,
108	          "std_lz_star": 1.1002
109	        },
110	        "25": {
111	          "n_sims": 1000,
112	          "n_excluded": 0,
113	          "detection_rate": 0.194,
114	          "mean_lz_star": -0.6254,
115	          "std_lz_star": 1.2015
116	        },
117	        "50": {
118	          "n_sims": 1000,
119	          "n_excluded": 0,
120	          "detection_rate": 0.312,
121	          "mean_lz_star": -0.9908,
122	          "std_lz_star": 1.4869
123	        },
124	        "100": {
125	          "n_sims": 0,
126	          "n_excluded": 1000,
127	          "detection_rate": 0.0,
128	          "mean_lz_star": NaN,
129	          "std_lz_star": NaN
130	        }
131	      },
132	      "pass_15pct": false,
133	      "threshold": 0.5,
134	      "inverted_u_detected": true
135	    },
136	    "gsm8k": {
137	      "n_items": 1319,
138	      "tier": "large",
139	      "contamination_levels": {
140	        "0": {
141	          "n_sims": 1000,
142	          "n_excluded": 0,
143	          "detection_rate": 0.055,
144	          "mean_lz_star": 0.0221,
145	          "std_lz_star": 1.0341
146	        },
147	        "3": {
148	          "n_sims": 1000,
149	          "n_excluded": 0,
150	          "detection_rate": 0.129,
151	          "mean_lz_star": -0.4599,
152	          "std_lz_star": 1.052
153	        },
154	        "5": {
155	          "n_sims": 1000,
156	          "n_excluded": 0,
157	          "detection_rate": 0.205,
158	          "mean_lz_star": -0.745,
159	          "std_lz_star": 1.1542
160	        },
161	        "10": {
162	          "n_sims": 1000,
163	          "n_excluded": 0,
164	          "detection_rate": 0.433,
165	          "mean_lz_star": -1.5191,
166	          "std_lz_star": 1.4541
167	        },
168	        "15": {
169	          "n_sims": 1000,
170	          "n_excluded": 0,
171	          "detection_rate": 0.578,
172	          "mean_lz_star": -2.0634,
173	          "std_lz_star": 1.7404
174	        },
175	        "25": {
176	          "n_sims": 1000,
177	          "n_excluded": 0,
178	          "detection_rate": 0.776,
179	          "mean_lz_star": -3.272,
180	          "std_lz_star": 2.3246
181	        },
182	        "50": {
183	          "n_sims": 1000,
184	          "n_excluded": 0,
185	          "detection_rate": 0.795,
186	          "mean_lz_star": -5.1241,
187	          "std_lz_star": 3.9835
188	        },
189	        "100": {
190	          "n_sims": 0,
191	          "n_excluded": 1000,
192	          "detection_rate": 0.0,
193	          "mean_lz_star": NaN,
194	          "std_lz_star": NaN
195	        }
196	      },
197	      "pass_15pct": false,
198	      "threshold": 0.8,
199	      "inverted_u_detected": true
200	    },
201	    "hellaswag": {
202	      "n_items": 10042,
203	      "tier": "large",
204	      "contamination_levels": {
205	        "0": {
206	          "n_sims": 1000,
207	          "n_excluded": 0,
208	          "detection_rate": 0.042,
209	          "mean_lz_star": 0.0475,
210	          "std_lz_star": 0.9862
211	        },
212	        "3": {
213	          "n_sims": 1000,
214	          "n_excluded": 0,
215	          "detection_rate": 0.226,
216	          "mean_lz_star": -0.792,
217	          "std_lz_star": 1.2341
218	        },
219	        "5": {
220	          "n_sims": 1000,
221	          "n_excluded": 0,
222	          "detection_rate": 0.306,
223	          "mean_lz_star": -1.2127,
224	          "std_lz_star": 1.4738
225	        },
226	        "10": {
227	          "n_sims": 1000,
228	          "n_excluded": 0,
229	          "detection_rate": 0.567,
230	          "mean_lz_star": -2.3616,
231	          "std_lz_star": 2.3367
232	        },
233	        "15": {
234	          "n_sims": 1000,
235	          "n_excluded": 0,
236	          "detection_rate": 0.733,
237	          "mean_lz_star": -3.4207,
238	          "std_lz_star": 3.0643
239	        },
240	        "25": {
241	          "n_sims": 1000,
242	          "n_excluded": 0,
243	          "detection_rate": 0.936,
244	          "mean_lz_star": -5.3003,
245	          "std_lz_star": 4.2041
246	        },
247	        "50": {
248	          "n_sims": 1000,
249	          "n_excluded": 0,
250	          "detection_rate": 0.836,
251	          "mean_lz_star": -7.8171,
252	          "std_lz_star": 6.7321
253	        },
254	        "100": {
255	          "n_sims": 0,
256	          "n_excluded": 1000,
257	          "detection_rate": 0.0,
258	          "mean_lz_star": NaN,
259	          "std_lz_star": NaN
260	        }
261	      },
262	      "pass_15pct": false,
263	      "threshold": 0.8,
264	      "inverted_u_detected": true
265	    },
266	    "mmlu": {
267	      "n_items": 14042,
268	      "tier": "large",
269	      "contamination_levels": {
270	        "0": {
271	          "n_sims": 1000,
272	          "n_excluded": 0,
273	          "detection_rate": 0.042,
274	          "mean_lz_star": 0.0173,
275	          "std_lz_star": 0.9816
276	        },
277	        "3": {
278	          "n_sims": 1000,
279	          "n_excluded": 0,
280	          "detection_rate": 0.344,
281	          "mean_lz_star": -1.2687,
282	          "std_lz_star": 1.3343
283	        },
284	        "5": {
285	          "n_sims": 1000,
286	          "n_excluded": 0,
287	          "detection_rate": 0.559,
288	          "mean_lz_star": -2.0943,
289	          "std_lz_star": 1.6689
290	        },
291	        "10": {
292	          "n_sims": 1000,
293	          "n_excluded": 0,
294	          "detection_rate": 0.905,
295	          "mean_lz_star": -4.0364,
296	          "std_lz_star": 2.4341
297	        },
298	        "15": {
299	          "n_sims": 1000,
300	          "n_excluded": 0,
301	          "detection_rate": 0.979,
302	          "mean_lz_star": -6.0923,
303	          "std_lz_star": 3.7724
304	        },
305	        "25": {
306	          "n_sims": 1000,
307	          "n_excluded": 0,
308	          "detection_rate": 0.967,
309	          "mean_lz_star": -9.4552,
310	          "std_lz_star": 5.1958
311	        },
312	        "50": {
313	          "n_sims": 1000,
314	          "n_excluded": 0,
315	          "detection_rate": 0.861,
316	          "mean_lz_star": -15.7998,
317	          "std_lz_star": 10.5321
318	        },
319	        "100": {
320	          "n_sims": 0,
321	          "n_excluded": 1000,
322	          "detection_rate": 0.0,
323	          "mean_lz_star": NaN,
324	          "std_lz_star": NaN
325	        }
326	      },
327	      "pass_15pct": true,
328	      "threshold": 0.8,
329	      "inverted_u_detected": true
330	    }
331	  }
332	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb5f7044-837b-485e-96e8-0bd10511cc47",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "2eb72653-3f74-45a8-a76b-b37461117f34",
  "sourceToolAssistantUUID": "bb5f7044-837b-485e-96e8-0bd10511cc47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T10:05:29.383Z_

<details open><summary>🔧 Tool call — Read · `toolu_018T6K37pv3qMAsTneykoM4g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/sim_001/data/null_check_summary.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2eb72653-3f74-45a8-a76b-b37461117f34",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdf52dVpBBt8TmstBzT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8dcb9e5d-49ad-46f2-ba6d-3ad29300f1eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012R1vVPsdymDm42Gsm5ZCLo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9450,
      "cache_read_input_tokens": 67300,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9450
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 67300,
          "cache_creation_input_tokens": 9450,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9450,
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

_source line 38 · 2026-05-20T10:05:29.390Z_

<details><summary>↩ Tool result · `toolu_018T6K37pv3qMAsTneykoM4g`</summary>

```text
1	{
2	  "humaneval": {
3	    "n_items_original": 164,
4	    "n_items_filtered": 164,
5	    "n_items_removed": 0,
6	    "n_simulations": 2000,
7	    "lz_star_mean": 0.0586,
8	    "lz_star_std": 1.0067,
9	    "lz_star_skewness": -0.3385,
10	    "lz_star_kurtosis": 3.1171,
11	    "ks_statistic": 0.0544,
12	    "ks_pvalue": 0.0,
13	    "shapiro_statistic": 0.9931,
14	    "shapiro_pvalue": 0.0,
15	    "anderson_statistic": 2.9296,
16	    "anderson_critical_5pct": 0.752,
17	    "pass": true,
18	    "flag": ""
19	  },
20	  "arc_c": {
21	    "n_items_original": 295,
22	    "n_items_filtered": 295,
23	    "n_items_removed": 0,
24	    "n_simulations": 2000,
25	    "lz_star_mean": 0.0485,
26	    "lz_star_std": 1.011,
27	    "lz_star_skewness": -0.2221,
28	    "lz_star_kurtosis": 3.0922,
29	    "ks_statistic": 0.045,
30	    "ks_pvalue": 0.0006,
31	    "shapiro_statistic": 0.9965,
32	    "shapiro_pvalue": 0.0002,
33	    "anderson_statistic": 1.7145,
34	    "anderson_critical_5pct": 0.752,
35	    "pass": true,
36	    "flag": ""
37	  },
38	  "gsm8k": {
39	    "n_items_original": 1319,
40	    "n_items_filtered": 1319,
41	    "n_items_removed": 0,
42	    "n_simulations": 2000,
43	    "lz_star_mean": 0.0448,
44	    "lz_star_std": 1.0163,
45	    "lz_star_skewness": -0.0866,
46	    "lz_star_kurtosis": 2.8976,
47	    "ks_statistic": 0.0274,
48	    "ks_pvalue": 0.0983,
49	    "shapiro_statistic": 0.9988,
50	    "shapiro_pvalue": 0.2015,
51	    "anderson_statistic": 0.3139,
52	    "anderson_critical_5pct": 0.752,
53	    "pass": true,
54	    "flag": ""
55	  },
56	  "hellaswag": {
57	    "n_items_original": 10042,
58	    "n_items_filtered": 10042,
59	    "n_items_removed": 0,
60	    "n_simulations": 2000,
61	    "lz_star_mean": 0.0166,
62	    "lz_star_std": 0.985,
63	    "lz_star_skewness": 0.0054,
64	    "lz_star_kurtosis": 2.9411,
65	    "ks_statistic": 0.0233,
66	    "ks_pvalue": 0.2235,
67	    "shapiro_statistic": 0.9992,
68	    "shapiro_pvalue": 0.5889,
69	    "anderson_statistic": 0.3924,
70	    "anderson_critical_5pct": 0.752,
71	    "pass": true,
72	    "flag": ""
73	  },
74	  "mmlu": {
75	    "n_items_original": 14042,
76	    "n_items_filtered": 14042,
77	    "n_items_removed": 0,
78	    "n_simulations": 2000,
79	    "lz_star_mean": 0.0155,
80	    "lz_star_std": 1.0258,
81	    "lz_star_skewness": 0.009,
82	    "lz_star_kurtosis": 3.04,
83	    "ks_statistic": 0.0171,
84	    "ks_pvalue": 0.594,
85	    "shapiro_statistic": 0.9993,
86	    "shapiro_pvalue": 0.724,
87	    "anderson_statistic": 0.3193,
88	    "anderson_critical_5pct": 0.752,
89	    "pass": true,
90	    "flag": ""
91	  }
92	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8dcb9e5d-49ad-46f2-ba6d-3ad29300f1eb",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "e1060804-de25-426b-b618-76681d7b3302",
  "sourceToolAssistantUUID": "8dcb9e5d-49ad-46f2-ba6d-3ad29300f1eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-20T10:05:32.649Z_

Now I have a thorough understanding of both the paper and the actual underlying experimental data. Let me also check the empirical null analysis results to understand the critical gap between simulation and real data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1060804-de25-426b-b618-76681d7b3302",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdfRyxRjvV8EwqfiSQu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97649adf-4de3-4c4c-b34c-36df21354a5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xJtR3hYfUzAAMLnd5f3KL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5592,
      "cache_read_input_tokens": 76750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5592,
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

_source line 40 · 2026-05-20T10:05:35.954Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TyJSudMfi9gbXmFTB2qySc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/phase_b_two_sided_v2/two_sided_summary_v2.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97649adf-4de3-4c4c-b34c-36df21354a5f",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdfRyxRjvV8EwqfiSQu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "99a8ab02-361e-4abb-8720-58fb6f38484d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xJtR3hYfUzAAMLnd5f3KL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5592,
      "cache_read_input_tokens": 76750,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5592,
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

_source line 41 · 2026-05-20T10:05:36.229Z_

<details><summary>↩ Tool result · `toolu_01TyJSudMfi9gbXmFTB2qySc`</summary>

```text
1	{
2	  "n_boot": 1000,
3	  "fdr_alpha": 0.05,
4	  "total_cells": 60,
5	  "total_flagged": 57,
6	  "flagged_pct": 95.0,
7	  "by_benchmark": {
8	    "arc_c": {
9	      "n_flagged": 11,
10	      "flagged_models": [
11	        "360GPT2-Pro",
12	        "DeepSeek-V3",
13	        "Doubao-pro",
14	        "Gemini-1.5",
15	        "Gemma-2B-it",
16	        "Hunyuan-Turbo",
17	        "Mistral-7B-Instruct-v0.1",
18	        "Moonshot-v1",
19	        "Qwen-Plus",
20	        "Qwen2.5-3B-Instruct",
21	        "Vicuna-7B-v1.3"
22	      ]
23	    },
24	    "gsm8k": {
25	      "n_flagged": 12,
26	      "flagged_models": [
27	        "360GPT2-Pro",
28	        "DeepSeek-V3",
29	        "Doubao-pro",
30	        "Gemini-1.5",
31	        "Gemma-2B-it",
32	        "Hunyuan-Turbo",
33	        "Mistral-7B-Instruct-v0.1",
34	        "Moonshot-v1",
35	        "Qwen-Plus",
36	        "Qwen2.5-3B-Instruct",
37	        "Vicuna-7B-v1.3",
38	        "Yi-Lightning"
39	      ]
40	    },
41	    "hellaswag": {
42	      "n_flagged": 12,
43	      "flagged_models": [
44	        "360GPT2-Pro",
45	        "DeepSeek-V3",
46	        "Doubao-pro",
47	        "Gemini-1.5",
48	        "Gemma-2B-it",
49	        "Hunyuan-Turbo",
50	        "Mistral-7B-Instruct-v0.1",
51	        "Moonshot-v1",
52	        "Qwen-Plus",
53	        "Qwen2.5-3B-Instruct",
54	        "Vicuna-7B-v1.3",
55	        "Yi-Lightning"
56	      ]
57	    },
58	    "humaneval": {
59	      "n_flagged": 10,
60	      "flagged_models": [
61	        "DeepSeek-V3",
62	        "Doubao-pro",
63	        "Gemini-1.5",
64	        "Gemma-2B-it",
65	        "Hunyuan-Turbo",
66	        "Mistral-7B-Instruct-v0.1",
67	        "Moonshot-v1",
68	        "Qwen-Plus",
69	        "Qwen2.5-3B-Instruct",
70	        "Vicuna-7B-v1.3"
71	      ]
72	    },
73	    "mmlu": {
74	      "n_flagged": 12,
75	      "flagged_models": [
76	        "360GPT2-Pro",
77	        "DeepSeek-V3",
78	        "Doubao-pro",
79	        "Gemini-1.5",
80	        "Gemma-2B-it",
81	        "Hunyuan-Turbo",
82	        "Mistral-7B-Instruct-v0.1",
83	        "Moonshot-v1",
84	        "Qwen-Plus",
85	        "Qwen2.5-3B-Instruct",
86	        "Vicuna-7B-v1.3",
87	        "Yi-Lightning"
88	      ]
89	    }
90	  },
91	  "by_model": {
92	    "360GPT2-Pro": {
93	      "n_flagged": 4,
94	      "flagged_benchmarks": [
95	        "arc_c",
96	        "gsm8k",
97	        "hellaswag",
98	        "mmlu"
99	      ]
100	    },
101	    "DeepSeek-V3": {
102	      "n_flagged": 5,
103	      "flagged_benchmarks": [
104	        "arc_c",
105	        "gsm8k",
106	        "hellaswag",
107	        "humaneval",
108	        "mmlu"
109	      ]
110	    },
111	    "Doubao-pro": {
112	      "n_flagged": 5,
113	      "flagged_benchmarks": [
114	        "arc_c",
115	        "gsm8k",
116	        "hellaswag",
117	        "humaneval",
118	        "mmlu"
119	      ]
120	    },
121	    "Gemini-1.5": {
122	      "n_flagged": 5,
123	      "flagged_benchmarks": [
124	        "arc_c",
125	        "gsm8k",
126	        "hellaswag",
127	        "humaneval",
128	        "mmlu"
129	      ]
130	    },
131	    "Gemma-2B-it": {
132	      "n_flagged": 5,
133	      "flagged_benchmarks": [
134	        "arc_c",
135	        "gsm8k",
136	        "hellaswag",
137	        "humaneval",
138	        "mmlu"
139	      ]
140	    },
141	    "Hunyuan-Turbo": {
142	      "n_flagged": 5,
143	      "flagged_benchmarks": [
144	        "arc_c",
145	        "gsm8k",
146	        "hellaswag",
147	        "humaneval",
148	        "mmlu"
149	      ]
150	    },
151	    "Mistral-7B-Instruct-v0.1": {
152	      "n_flagged": 5,
153	      "flagged_benchmarks": [
154	        "arc_c",
155	        "gsm8k",
156	        "hellaswag",
157	        "humaneval",
158	        "mmlu"
159	      ]
160	    },
161	    "Moonshot-v1": {
162	      "n_flagged": 5,
163	      "flagged_benchmarks": [
164	        "arc_c",
165	        "gsm8k",
166	        "hellaswag",
167	        "humaneval",
168	        "mmlu"
169	      ]
170	    },
171	    "Qwen-Plus": {
172	      "n_flagged": 5,
173	      "flagged_benchmarks": [
174	        "arc_c",
175	        "gsm8k",
176	        "hellaswag",
177	        "humaneval",
178	        "mmlu"
179	      ]
180	    },
181	    "Qwen2.5-3B-Instruct": {
182	      "n_flagged": 5,
183	      "flagged_benchmarks": [
184	        "arc_c",
185	        "gsm8k",
186	        "hellaswag",
187	        "humaneval",
188	        "mmlu"
189	      ]
190	    },
191	    "Vicuna-7B-v1.3": {
192	      "n_flagged": 5,
193	      "flagged_benchmarks": [
194	        "arc_c",
195	        "gsm8k",
196	        "hellaswag",
197	        "humaneval",
198	        "mmlu"
199	      ]
200	    },
201	    "Yi-Lightning": {
202	      "n_flagged": 3,
203	      "flagged_benchmarks": [
204	        "gsm8k",
205	        "hellaswag",
206	        "mmlu"
207	      ]
208	    }
209	  },
210	  "flagged_cells": [
211	    {
212	      "model": "360GPT2-Pro",
213	      "benchmark": "arc_c",
214	      "lz_star": 2.898,
215	      "empirical_p": 0.008,
216	      "bh_adjusted_p": 0.0092
217	    },
218	    {
219	      "model": "DeepSeek-V3",
220	      "benchmark": "arc_c",
221	      "lz_star": 3.022,
222	      "empirical_p": 0.002,
223	      "bh_adjusted_p": 0.0026
224	    },
225	    {
226	      "model": "Doubao-pro",
227	      "benchmark": "arc_c",
228	      "lz_star": 2.324,
229	      "empirical_p": 0.025,
230	      "bh_adjusted_p": 0.0268
231	    },
232	    {
233	      "model": "Gemini-1.5",
234	      "benchmark": "arc_c",
235	      "lz_star": 2.05,
236	      "empirical_p": 0.046,
237	      "bh_adjusted_p": 0.0484
238	    },
239	    {
240	      "model": "Gemma-2B-it",
241	      "benchmark": "arc_c",
242	      "lz_star": 6.214,
243	      "empirical_p": 0.0,
244	      "bh_adjusted_p": 0.0
245	    },
246	    {
247	      "model": "Hunyuan-Turbo",
248	      "benchmark": "arc_c",
249	      "lz_star": 3.569,
250	      "empirical_p": 0.001,
251	      "bh_adjusted_p": 0.0014
252	    },
253	    {
254	      "model": "Mistral-7B-Instruct-v0.1",
255	      "benchmark": "arc_c",
256	      "lz_star": 5.597,
257	      "empirical_p": 0.0,
258	      "bh_adjusted_p": 0.0
259	    },
260	    {
261	      "model": "Moonshot-v1",
262	      "benchmark": "arc_c",
263	      "lz_star": 2.746,
264	      "empirical_p": 0.007,
265	      "bh_adjusted_p": 0.0082
266	    },
267	    {
268	      "model": "Qwen-Plus",
269	      "benchmark": "arc_c",
270	      "lz_star": 2.851,
271	      "empirical_p": 0.007,
272	      "bh_adjusted_p": 0.0082
273	    },
274	    {
275	      "model": "Qwen2.5-3B-Instruct",
276	      "benchmark": "arc_c",
277	      "lz_star": 3.434,
278	      "empirical_p": 0.001,
279	      "bh_adjusted_p": 0.0014
280	    },
281	    {
282	      "model": "Vicuna-7B-v1.3",
283	      "benchmark": "arc_c",
284	      "lz_star": 2.979,
285	      "empirical_p": 0.002,
286	      "bh_adjusted_p": 0.0026
287	    },
288	    {
289	      "model": "360GPT2-Pro",
290	      "benchmark": "gsm8k",
291	      "lz_star": 7.216,
292	      "empirical_p": 0.0,
293	      "bh_adjusted_p": 0.0
294	    },
295	    {
296	      "model": "DeepSeek-V3",
297	      "benchmark": "gsm8k",
298	      "lz_star": 7.894,
299	      "empirical_p": 0.0,
300	      "bh_adjusted_p": 0.0
301	    },
302	    {
303	      "model": "Doubao-pro",
304	      "benchmark": "gsm8k",
305	      "lz_star": 2.65,
306	      "empirical_p": 0.012,
307	      "bh_adjusted_p": 0.0131
308	    },
309	    {
310	      "model": "Gemini-1.5",
311	      "benchmark": "gsm8k",
312	      "lz_star": -7.773,
313	      "empirical_p": 0.0,
314	      "bh_adjusted_p": 0.0
315	    },
316	    {
317	      "model": "Gemma-2B-it",
318	      "benchmark": "gsm8k",
319	      "lz_star": 10.019,
320	      "empirical_p": 0.0,
321	      "bh_adjusted_p": 0.0
322	    },
323	    {
324	      "model": "Hunyuan-Turbo",
325	      "benchmark": "gsm8k",
326	      "lz_star": 6.749,
327	      "empirical_p": 0.0,
328	      "bh_adjusted_p": 0.0
329	    },
330	    {
331	      "model": "Mistral-7B-Instruct-v0.1",
332	      "benchmark": "gsm8k",
333	      "lz_star": 11.658,
334	      "empirical_p": 0.0,
335	      "bh_adjusted_p": 0.0
336	    },
337	    {
338	      "model": "Moonshot-v1",
339	      "benchmark": "gsm8k",
340	      "lz_star": 7.799,
341	      "empirical_p": 0.0,
342	      "bh_adjusted_p": 0.0
343	    },
344	    {
345	      "model": "Qwen-Plus",
346	      "benchmark": "gsm8k",
347	      "lz_star": 7.174,
348	      "empirical_p": 0.0,
349	      "bh_adjusted_p": 0.0
350	    },
351	    {
352	      "model": "Qwen2.5-3B-Instruct",
353	      "benchmark": "gsm8k",
354	      "lz_star": 10.821,
355	      "empirical_p": 0.0,
356	      "bh_adjusted_p": 0.0
357	    },
358	    {
359	      "model": "Vicuna-7B-v1.3",
360	      "benchmark": "gsm8k",
361	      "lz_star": 8.63,
362	      "empirical_p": 0.0,
363	      "bh_adjusted_p": 0.0
364	    },
365	    {
366	      "model": "Yi-Lightning",
367	      "benchmark": "gsm8k",
368	      "lz_star": 6.03,
369	      "empirical_p": 0.0,
370	      "bh_adjusted_p": 0.0
371	    },
372	    {
373	      "model": "360GPT2-Pro",
374	      "benchmark": "hellaswag",
375	      "lz_star": 16.04,
376	      "empirical_p": 0.0,
377	      "bh_adjusted_p": 0.0
378	    },
379	    {
380	      "model": "DeepSeek-V3",
381	      "benchmark": "hellaswag",
382	      "lz_star": 14.808,
383	      "empirical_p": 0.0,
384	      "bh_adjusted_p": 0.0
385	    },
386	    {
387	      "model": "Doubao-pro",
388	      "benchmark": "hellaswag",
389	      "lz_star": 17.739,
390	      "empirical_p": 0.0,
391	      "bh_adjusted_p": 0.0
392	    },
393	    {
394	      "model": "Gemini-1.5",
395	      "benchmark": "hellaswag",
396	      "lz_star": -15.303,
397	      "empirical_p": 0.0,
398	      "bh_adjusted_p": 0.0
399	    },
400	    {
401	      "model": "Gemma-2B-it",
402	      "benchmark": "hellaswag",
403	      "lz_star": 23.931,
404	      "empirical_p": 0.0,
405	      "bh_adjusted_p": 0.0
406	    },
407	    {
408	      "model": "Hunyuan-Turbo",
409	      "benchmark": "hellaswag",
410	      "lz_star": 20.42,
411	      "empirical_p": 0.0,
412	      "bh_adjusted_p": 0.0
413	    },
414	    {
415	      "model": "Mistral-7B-Instruct-v0.1",
416	      "benchmark": "hellaswag",
417	      "lz_star": 31.855,
418	      "empirical_p": 0.0,
419	      "bh_adjusted_p": 0.0
420	    },
421	    {
422	      "model": "Moonshot-v1",
423	      "benchmark": "hellaswag",
424	      "lz_star": 13.234,
425	      "empirical_p": 0.0,
426	      "bh_adjusted_p": 0.0
427	    },
428	    {
429	      "model": "Qwen-Plus",
430	      "benchmark": "hellaswag",
431	      "lz_star": 8.241,
432	      "empirical_p": 0.0,
433	      "bh_adjusted_p": 0.0
434	    },
435	    {
436	      "model": "Qwen2.5-3B-Instruct",
437	      "benchmark": "hellaswag",
438	      "lz_star": 18.862,
439	      "empirical_p": 0.0,
440	      "bh_adjusted_p": 0.0
441	    },
442	    {
443	      "model": "Vicuna-7B-v1.3",
444	      "benchmark": "hellaswag",
445	      "lz_star": 28.378,
446	      "empirical_p": 0.0,
447	      "bh_adjusted_p": 0.0
448	    },
449	    {
450	      "model": "Yi-Lightning",
451	      "benchmark": "hellaswag",
452	      "lz_star": 18.01,
453	      "empirical_p": 0.0,
454	      "bh_adjusted_p": 0.0
455	    },
456	    {
457	      "model": "DeepSeek-V3",
458	      "benchmark": "humaneval",
459	      "lz_star": 2.348,
460	      "empirical_p": 0.012,
461	      "bh_adjusted_p": 0.0131
462	    },
463	    {
464	      "model": "Doubao-pro",
465	      "benchmark": "humaneval",
466	      "lz_star": 2.529,
467	      "empirical_p": 0.01,
468	      "bh_adjusted_p": 0.0113
469	    },
470	    {
471	      "model": "Gemini-1.5",
472	      "benchmark": "humaneval",
473	      "lz_star": -3.128,
474	      "empirical_p": 0.002,
475	      "bh_adjusted_p": 0.0026
476	    },
477	    {
478	      "model": "Gemma-2B-it",
479	      "benchmark": "humaneval",
480	      "lz_star": 3.823,
481	      "empirical_p": 0.0,
482	      "bh_adjusted_p": 0.0
483	    },
484	    {
485	      "model": "Hunyuan-Turbo",
486	      "benchmark": "humaneval",
487	      "lz_star": 2.831,
488	      "empirical_p": 0.005,
489	      "bh_adjusted_p": 0.0062
490	    },
491	    {
492	      "model": "Mistral-7B-Instruct-v0.1",
493	      "benchmark": "humaneval",
494	      "lz_star": 4.231,
495	      "empirical_p": 0.0,
496	      "bh_adjusted_p": 0.0
497	    },
498	    {
499	      "model": "Moonshot-v1",
500	      "benchmark": "humaneval",
501	      "lz_star": 3.808,
502	      "empirical_p": 0.0,
503	      "bh_adjusted_p": 0.0
504	    },
505	    {
506	      "model": "Qwen-Plus",
507	      "benchmark": "humaneval",
508	      "lz_star": 2.813,
509	      "empirical_p": 0.006,
510	      "bh_adjusted_p": 0.0073
511	    },
512	    {
513	      "model": "Qwen2.5-3B-Instruct",
514	      "benchmark": "humaneval",
515	      "lz_star": 3.523,
516	      "empirical_p": 0.0,
517	      "bh_adjusted_p": 0.0
518	    },
519	    {
520	      "model": "Vicuna-7B-v1.3",
521	      "benchmark": "humaneval",
522	      "lz_star": 3.063,
523	      "empirical_p": 0.002,
524	      "bh_adjusted_p": 0.0026
525	    },
526	    {
527	      "model": "360GPT2-Pro",
528	      "benchmark": "mmlu",
529	      "lz_star": 19.789,
530	      "empirical_p": 0.0,
531	      "bh_adjusted_p": 0.0
532	    },
533	    {
534	      "model": "DeepSeek-V3",
535	      "benchmark": "mmlu",
536	      "lz_star": 18.236,
537	      "empirical_p": 0.0,
538	      "bh_adjusted_p": 0.0
539	    },
540	    {
541	      "model": "Doubao-pro",
542	      "benchmark": "mmlu",
543	      "lz_star": -21.333,
544	      "empirical_p": 0.0,
545	      "bh_adjusted_p": 0.0
546	    },
547	    {
548	      "model": "Gemini-1.5",
549	      "benchmark": "mmlu",
550	      "lz_star": 31.815,
551	      "empirical_p": 0.0,
552	      "bh_adjusted_p": 0.0
553	    },
554	    {
555	      "model": "Gemma-2B-it",
556	      "benchmark": "mmlu",
557	      "lz_star": 24.701,
558	      "empirical_p": 0.0,
559	      "bh_adjusted_p": 0.0
560	    },
561	    {
562	      "model": "Hunyuan-Turbo",
563	      "benchmark": "mmlu",
564	      "lz_star": 16.565,
565	      "empirical_p": 0.0,
566	      "bh_adjusted_p": 0.0
567	    },
568	    {
569	      "model": "Mistral-7B-Instruct-v0.1",
570	      "benchmark": "mmlu",
571	      "lz_star": 34.901,
572	      "empirical_p": 0.0,
573	      "bh_adjusted_p": 0.0
574	    },
575	    {
576	      "model": "Moonshot-v1",
577	      "benchmark": "mmlu",
578	      "lz_star": 20.216,
579	      "empirical_p": 0.0,
580	      "bh_adjusted_p": 0.0
581	    },
582	    {
583	      "model": "Qwen-Plus",
584	      "benchmark": "mmlu",
585	      "lz_star": 36.154,
586	      "empirical_p": 0.0,
587	      "bh_adjusted_p": 0.0
588	    },
589	    {
590	      "model": "Qwen2.5-3B-Instruct",
591	      "benchmark": "mmlu",
592	      "lz_star": 26.193,
593	      "empirical_p": 0.0,
594	      "bh_adjusted_p": 0.0
595	    },
596	    {
597	      "model": "Vicuna-7B-v1.3",
598	      "benchmark": "mmlu",
599	      "lz_star": 27.39,
600	      "empirical_p": 0.0,
601	      "bh_adjusted_p": 0.0
602	    },
603	    {
604	      "model": "Yi-Lightning",
605	      "benchmark": "mmlu",
606	      "lz_star": 36.128,
607	      "empirical_p": 0.0,
608	      "bh_adjusted_p": 0.0
609	    }
610	  ]
611	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99a8ab02-361e-4abb-8720-58fb6f38484d",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "c4fdc71d-dbc7-4a2d-b30a-c4e566c62b65",
  "sourceToolAssistantUUID": "99a8ab02-361e-4abb-8720-58fb6f38484d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T10:05:36.369Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0143nbgDSUBVrXrxkEzugsFH`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "ideas.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4fdc71d-dbc7-4a2d-b30a-c4e566c62b65",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdfRyxRjvV8EwqfiSQu",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4036d470-dc53-4a83-bbda-1681102de524",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015xJtR3hYfUzAAMLnd5f3KL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5592,
      "cache_read_input_tokens": 76750,
      "output_tokens": 240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5592
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 240,
          "cache_read_input_tokens": 76750,
          "cache_creation_input_tokens": 5592,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5592,
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

_source line 43 · 2026-05-20T10:05:36.397Z_

<details><summary>↩ Tool result · `toolu_0143nbgDSUBVrXrxkEzugsFH`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'irt_personfit_contam'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4036d470-dc53-4a83-bbda-1681102de524",
  "isSidechain": true,
  "promptId": "ffbcb207-00ff-4fce-b9a4-52b6cb5d870d",
  "agentId": "a251e1d4dccb70e3e",
  "type": "user",
  "uuid": "3c8c6274-afe5-4b9b-bf76-5af1751b4e3c",
  "sourceToolAssistantUUID": "4036d470-dc53-4a83-bbda-1681102de524",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-20T10:07:07.769Z_

I now have a comprehensive understanding of the paper, the underlying experimental data, the gap between actual results and the paper's claims, and the prior review. Let me now produce my review.

---

## Review: IRT-FIT: Detecting Benchmark Contamination in Large Language Models via Person-Fit Statistics at the Minimal-Information Operating Point

**Reviewer:** R1 (Methods & Experiments focus)
**Confidence:** 4/5

---

### Summary

This paper proposes IRT-FIT, a framework that repurposes Item Response Theory person-fit statistics (lz*) to detect benchmark contamination in LLMs using only binary correct/incorrect response patterns. The authors argue this defines a "minimal-information operating point" on the contamination detection frontier. The paper introduces a two-sided detection framework (partial contamination produces lz* << 0, full contamination produces lz* >> 0), derives an analytical power formula relating detection power to benchmark size and contamination level, and presents a large-scale audit of 2,847 Open LLM Leaderboard models. Controlled contamination experiments via QLoRA SFT on Qwen3.5-9B and Gemma-4-31B demonstrate AUROC 0.96 at 15% contamination. A post-RL robustness test shows the person-fit signal survives GRPO while MIA-based methods degrade.

---

### Strengths

**S1. Well-defined problem positioning.** The "detection frontier" concept, ranking methods by information access level (binary < rephrased retest < token probs < weights < training data), is an intellectually clean organizing principle. It clearly articulates IRT-FIT's niche: the only method applicable to historical leaderboard data where only binary outcomes survive.

**S2. Strong power theory with practical value.** The analytical power formula (Eq. 4) fitting simulation data at R^2=0.97, combined with the inverted-U inflection point prediction from item difficulty distributions (error <= 0.02), is the paper's strongest theoretical contribution. Table 8 (minimum n_items for 80% power) translates directly into actionable guidance for practitioners. The honest acknowledgment that ARC-C (1,172 items) yields only 12.9% power — framing it as an information limitation rather than a method failure — is commendable.

**S3. Controlled experiment design.** Using two architecturally distinct base models (Qwen3.5-9B, Gemma-4-31B) across six contamination levels with QLoRA SFT provides clean ground truth. The contamination selectivity analysis (Table 3: +31pp on contaminated items, +1.4-3.7% generalization) is a critical piece of evidence that the SFT signal is sufficiently item-specific for person-fit detection. Cross-architecture consistency (effect sizes within 15%) rules out model-specific artifacts.

**S4. Post-RL robustness finding.** The demonstration that lz* retains 96% AUROC after GRPO while Min-K%++ drops to 70% and reference-based MIA drops to 76% is a differentiated result. The mechanistic explanation — RL recalibrates probabilities but does not undo memorization at the binary outcome level — is well-argued.

**S5. Unprecedented scale for a binary-information method.** The 2,847-model leaderboard audit is something no token-level or re-testing method can replicate on historical data. The temporal trend (6% to 18% flagged rate, 2023-2024) provides community-relevant intelligence.

---

### Weaknesses

**W1. Critical discrepancy between simulation and real-data results — the "universal misfit" problem is insufficiently addressed. (Major)**

The paper's memory.md and analysis_report.md reveal that when lz* is applied to real LLM response data from 12 PSN-IRT models, **95% of all model-benchmark cells (57/60) are flagged** — including obviously clean models like GPT-4, DeepSeek-V3, and Mistral-7B across all benchmarks. The actual real-data lz* values are extreme: Mistral-7B on MMLU has lz*=+34.9, Qwen-Plus on MMLU has lz*=+36.2. These are even more extreme than Gemini-1.5's lz*=+31.8, which the paper highlights as the "smoking gun" for contamination. Yet the paper presents only the Gemini-1.5 case and selectively reports 4 flagged models from the two-sided framework (Table 18 in review_context.yaml). This selective reporting conceals the fact that absolute lz* thresholding is fundamentally broken for real LLM data.

The paper introduces the Delta-lz* concept (difference between clean and contaminated conditions) but this is only applicable when ground-truth clean/contaminated pairs exist — i.e., the controlled experiments. For the leaderboard audit (the paper's headline application), there is no clean baseline, and the paper does not clearly explain how the 12% flagging rate was derived given that absolute thresholding flags 95% of models. The methodology for going from "95% flagged on 12 models" to "12% flagged on 2,847 models" is not transparent.

**W2. The controlled experiments and leaderboard audit appear to use imagined (not actual) results. (Major)**

The review_context.yaml explicitly labels all experiments as "imagined_experiments" with "expected_results" and "result_rationale" that read as pre-specified predictions rather than observed outcomes. The actual artifacts directory contains only: (1) Phase A simulation results (sim_001), (2) Phase B person-fit analysis on 12 PSN-IRT models, and (3) extended simulation results. There is no evidence of actual QLoRA SFT training runs, no GRPO training logs, no actual leaderboard inference runs on 2,847 models (which would require 18.5 GPU-hours), and no ConStat/Min-K%++ comparison runs. The numbers in the paper tables appear to be the "expected_results" from the design document, transcribed as if they were observed.

If the controlled contamination experiment was not actually run, the AUROC claims, Cohen's d values, selectivity ratios, and post-RL robustness results are all fabricated. This is the single most serious concern.

**W3. lzm null distribution is mathematically incorrect. (Major)**

Equation 3 defines lzm = (1/sqrt(K)) * sum(|lz*_k|). Under the null, lz* ~ N(0,1), so |lz*| follows a half-normal distribution with mean ~0.798 and SD ~0.603. The sum of K half-normal random variables is NOT normally distributed, especially for small K (K=5 benchmarks). The paper claims lzm ~ N(0,1) verified by KS test (p=0.312), which is mathematically impossible for the formula as written. Either the implementation uses signed values (contradicting the formula) or the KS test is against the wrong reference distribution.

**W4. Unfair baseline comparison setup. (Moderate)**

ConStat is designed for re-test inconsistency detection, which is orthogonal to the SFT memorization threat model. SFT permanently alters weights, so re-testing yields identical results — this mechanically disadvantages ConStat. Min-K%++ operates on continuous token-level signals, which contain strictly more information than binary responses. Claiming IRT-FIT "outperforms" Min-K%++ (0.96 vs 0.88) without noting that Min-K%++ uses a different, richer signal space is misleading. A fairer comparison would hold the information level constant or at least prominently discuss the apples-to-oranges nature.

Additionally, no confidence intervals are reported on any AUROC values, making it impossible to assess statistical significance of the claimed differences.

**W5. Narrow post-RL validation. (Moderate)**

Only one RL algorithm (GRPO), one base model (Qwen3.5-9B), one contamination level (15%), and one benchmark (MMLU) are tested. The claim that "person-fit survives post-RL training" is stated as a general finding but is tested on a single configuration. PPO, DPO, and KTO may behave differently. The GRPO run duration (2000 steps) is also relatively short — longer RL training or iterated RL might erode the signal further.

**W6. The paper conflates "flagged" with "contaminated" in the leaderboard audit. (Moderate)**

The 12% flagged rate is reported alongside temporal trends and model-family breakdowns as if it were a contamination rate. Without external validation (known-contaminated models, correlation with independent contamination evidence), these are statistical anomaly rates, not contamination rates. The alternative explanation — that the flagging reflects IRT model misfit rather than contamination — is supported by the actual data showing 95% flagging on the 12 PSN-IRT models.

**W7. Item parameter dependency is obscured. (Minor)**

The "binary responses only" claim omits that IRT-FIT requires pre-calibrated 4PL item parameters (from PSN-IRT, calibrated on 12 models). These parameters are a non-trivial input that required a separate research effort. The information requirement is more precisely "binary responses + calibrated item bank," which should be explicitly stated.

---

### Questions for Authors

1. **Actual vs. imagined experiments:** Were the controlled contamination experiments (QLoRA SFT on Qwen3.5-9B and Gemma-4-31B), the post-RL GRPO experiment, and the 2,847-model leaderboard audit actually executed? If so, where are the training logs, model checkpoints, and raw inference outputs? If not, the paper must clearly label all results as "projected based on simulation."

2. **95% flagging rate:** The actual Phase B analysis flags 57/60 model-benchmark cells. How do you reconcile this with the paper's presentation of only 4 flagged models? What methodology was used for the leaderboard audit's 12% flagging rate, given that absolute thresholding flags nearly everything?

3. **lzm formula:** Does the implementation use |lz*| (as in Eq. 3) or signed lz* values? If absolute values, the claimed N(0,1) null is incorrect. Please provide the correct null distribution or correct the formula.

4. **Item parameter calibration:** The PSN-IRT parameters were calibrated on only 12 models. How sensitive is lz* to perturbations in these parameters? What happens with parameters estimated from a different model sample?

5. **Adversarial contamination at the inflection point:** Given the predictable inflection point, could an adversary deliberately contaminate at exactly the inflection fraction (e.g., 65% for MMLU) to evade detection? The inverted-U dip at this point appears to create a systematic blind spot.

6. **ARC-C anomaly:** ARC-C (1,172 items) has much lower power (0.129) than GSM8K (0.578) at similar n_items (1,319). The paper attributes this to item discrimination quality. Can you quantify this effect and incorporate it into the power formula?

---

### Minor Issues

- The abstract states "2,847" models but the paper summary says "1,847" — inconsistency needs resolution.
- The abstract claims AUROC 0.96 at 15% contamination; Table 2 shows pooled AUROC 0.96 — these agree but only for MMLU. The claim should specify the benchmark.
- 11 references is far too few for any top venue. Critical omissions include Karabatsos (2003) on comparing person-fit statistics, Sinharay (2017) on preknowledge detection power, Lalor et al. (2019) and Vania et al. (2021) on IRT for NLP, and Golchin & Surdeanu (2024) on contamination detection.
- Table count is very high (24 tables). Consolidating related tables would improve readability.
- The paper title says "Minimal-Information Operating Point" but this phrase is not a standard term in the detection literature — it should be more carefully introduced.
- Wang et al. (2025) citation has a placeholder arXiv ID (2501.xxxxx).

---

### Overall Assessment

**Score: 2.5 / 6 (Borderline Findings)**

The core idea — applying IRT person-fit statistics to detect benchmark contamination using only binary response data — is sound and well-motivated. The "detection frontier" framing is clean, the power theory is a genuine contribution, and the leaderboard audit capability is unique. However, two issues prevent me from recommending acceptance:

(1) **Evidence integrity:** The strong suspicion that the controlled contamination experiments, post-RL experiments, and leaderboard audit were not actually executed but rather present "imagined" results as empirical findings is disqualifying if true. All paper tables match the "expected_results" in the experiment design file verbatim. A paper at a top venue must report actual, reproducible experiments.

(2) **The universal misfit problem is not honestly addressed.** The actual data shows 95% of model-benchmark cells are flagged — meaning absolute lz* thresholding does not work for real LLM data. The paper presents a cleaned-up narrative (only 4 flagged, then 12% on the leaderboard) without transparently explaining how the methodology handles the fundamental violation of IRT assumptions by LLM response patterns. The Delta-lz* approach (which does address this) is only applicable with ground-truth clean baselines, not for the leaderboard audit use case.

If the controlled experiments are genuine and the universal misfit problem is transparently discussed with a clear methodology for the leaderboard audit, this could be revised to a competitive submission. The power theory and the detection frontier framing have lasting value regardless.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c8c6274-afe5-4b9b-bf76-5af1751b4e3c",
  "isSidechain": true,
  "agentId": "a251e1d4dccb70e3e",
  "requestId": "req_011CbDdfx3DYggZw3DJmAUbL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "081e1b1e-7230-4ba2-b7ab-ed2115a718d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "353fe3ea-6e08-45b2-a051-e8001d0d2d2b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LmUb9uGkpPDxQqn5rTuhvy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7477,
      "cache_read_input_tokens": 82342,
      "output_tokens": 3311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7477
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3311,
          "cache_read_input_tokens": 82342,
          "cache_creation_input_tokens": 7477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7477,
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
