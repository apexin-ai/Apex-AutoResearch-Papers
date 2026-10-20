# Research conversation: You are auditing every number in an academic paper for data integrity. Read all the .tex files in `/home/ubuntu/.agent-m

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a92bd2628d8113da1.jsonl`
- **Structured JSON:** [`21b5cc9ecf5478e3c593.json`](../../sessions/21/21b5cc9ecf5478e3c593.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-25T19:43:07.036Z_

You are auditing every number in an academic paper for data integrity. Read all the .tex files in `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/` and extract EVERY quantitative claim (numbers, percentages, statistics). 

For each number, record: the number, the file and line number, and what it claims to measure.

Files to scan: abstract.tex, introduction.tex, background.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex

Here are the ground truth values from the experiment registry to compare against:

**exp-003b (N=8 pilot, 9 judges)**:
- n_observations: 5661, n_models: 8, n_items: 176, n_judges: 9
- raw_average: τ=0.786, ρ=0.905
- joint_gmfrm: τ=0.857, ρ=0.952, p_tau=0.002, p_rho=0.0003
- c_n: GPT-3.5=5.587 (CI [4.4, 6.8]), GPT-4-0613=4.168 (CI [3.1, 5.3]), Qwen2.5-72B=2.961 (CI [1.4, 4.6]), LLaMA-3.3-70B=2.478 (CI [1.1, 3.9]), Gemma-2-9B=1.654 (CI [0.36, 2.9]), Qwen3-8B=1.178 (CI [0.14, 2.5]), GPT-4o-mini=0.934 (CI [0.059, 2.2]), GPT-4o=0.880 (CI [0.052, 2.2])
- d_j: Claude-Opus-4.7=0.60, GPT-5.5=0.53, DeepSeek-V4-Pro=0.31, Claude-Sonnet-4.6=0.14, Gemini-2.5-Pro=-0.036, Qwen3-235B=-0.038, Qwen2.5-72B=-0.35, LLaMA-3.3-70B=-0.42, Mistral-Large-2=-0.74
- R̂ max: 1.03, ESS min: 174 (but paper may cite 1.003 and 1240 from exp-020)
- sigma_c: mean=2.4
- LOO: ΔELPD=-55.7, SE=9.4, |Δ/SE|=5.9 (need to verify source)

**exp-019 (bias absorption)**:
- Δθ: GPT-3.5=+0.786, GPT-4-0613=+0.431, Qwen2.5-72B=+0.035, LLaMA-3.3-70B=-0.022, Gemma-2-9B=-0.161, Qwen3-8B=-0.305, GPT-4o-mini=-0.368, GPT-4o=-0.397
- Spearman ρ between Δθ and c_n: 1.0

**exp-020 (N=17, 6 judges)**:
- joint_gmfrm: τ=0.794, ρ=0.926; raw_average: τ=0.838, ρ=0.949; Δτ=-0.044
- v3 (filtered 317 items): τ=0.809, raw=0.824, Δτ=-0.015, R̂=1.009, ESS=1677
- v4 (MFRM-only): τ=0.824, Δτ=0.000
- v5 (contamination-only): τ=0.706, Δτ=-0.118
- v7 (e_i>0 only, 231 items): τ=0.779, raw=0.779, Δτ=0.000
- R̂ max: 1.0023, ESS min: 1240
- bootstrap Δτ CI: [-0.141, 0]

**exp-004 (baselines)**:
- N=8: all baselines τ=0.8095 (except UDA quantile=0.7807)
- N=17: raw=0.8382, CyclicJudge=0.8382, CyclicJudge_discard=0.8235, DCR=0.8235, PrefLeakage=0.8382

**exp-w7-ablation (synthetic N=50, 20 seeds)**:
- full_gmfrm: θ_RMSE=0.1243±0.0164, τ=0.9224±0.0097, c_RMSE=0.5933±0.2242
- staged: θ_RMSE=0.2539±0.0448, τ=0.8393±0.0349, c_RMSE=1.3823±0.1635
- binary_gating: θ_RMSE=0.1371±0.0161, c_RMSE=0.8326±0.2257, τ=0.9093±0.0140
- no_judge_severity: θ_RMSE=0.1266±0.0160, c_RMSE=0.6292±0.2425, τ=0.9216±0.0097
- Wilcoxon p: full_vs_staged θ=1.91e-6, full_vs_binary θ=3.81e-6

**mvp_003 (synthetic N=50, 20 seeds, same DGP as ablation)**:
- joint τ=0.9223, sequential τ=0.8593
- joint RMSE=0.1243, sequential RMSE=0.2211 → reduction ~43.8%
- mfrm_only RMSE=0.2539

**exp-018 (synthetic N=20, 20 seeds)**:
- joint: θ_RMSE=0.094, τ=0.9432; sequential: θ_RMSE=0.1714, τ=0.8911
- θ_RMSE reduction: -45.2%, c_RMSE reduction: -54.5%
- Δτ=+0.0521, Wilcoxon p=0.000181, 18 wins/1 tie/1 loss
- c_pearson: joint=0.8424, seq=0.8167

**exp-015 (synthetic N=8, 20 seeds)**:
- joint: θ_RMSE=0.0827, τ=0.9536; sequential: θ_RMSE=0.1664, τ=0.8821
- θ_RMSE reduction: -50.3%, c_RMSE reduction: -60.5%
- Δτ=+0.0715, Wilcoxon p=0.002, 10 wins/10 ties/0 losses

**exp-009 (OVB simulation, N=50, 50 seeds)**:
- Sequential bias slope: ~0.19 across all ρ; Joint bias slope: ~0.06 across all ρ
- Joint reduces bias slope by ~69% (0.06/0.19 = 0.31, reduction = 69%)
- c_n recovery: coverage=0.71, RMSE=0.6484, correlation=0.8114
- Part A: 200 fits (4 rho × 50 seeds), Part B: 50 seeds

**exp-012 (error propagation, N=50, 20 seeds)**:
- σ=0.0: θ_RMSE=0.1277, c_n RMSE=0.533, c_n corr=0.8599
- σ=0.1: θ_RMSE +1.4%, c_n RMSE +2.3%
- σ=0.2: θ_RMSE +5.9%, c_n RMSE +7.9%
- σ=0.5: θ_RMSE +36.9%, c_n RMSE +57.9%

**exp-013 (weight sensitivity)**:
- All weight configs give identical τ=0.7857
- Spearman ρ between exposure rankings ≥ 0.992 (min 0.9978)

**exp-006 (judge count)**:
- k=9: joint τ=0.857, raw=0.786, advantage=+0.071
- k=6 mean: joint τ=0.821±0.051
- k=4 mean: joint τ=0.800±0.045
- k=2 mean: joint τ=0.771±0.081

**Specific things to verify**:
1. "51%" RMSE reduction — from which experiment? mvp_003 says 43.8%, exp-015 says 50.3%, exp-018 says 45.2%. Paper may cite 51% which may come from a different calculation.
2. τ=0.922 vs 0.839 — ablation staged baseline. Registry: joint τ=0.9224, staged τ=0.8393. Check paper.
3. "4-6×" higher susceptibility — GPT-3.5 c_n=5.587, GPT-4o c_n=0.880. Ratio = 6.35×. GPT-4-0613=4.168/0.880=4.74×. So "4-6×" is approximately correct but should be checked.
4. r=0.81 — from exp-009 Part B: correlation=0.8114. Paper says 0.81 which is rounded.
5. 5,661 observations — from exp-003b spec.data_count and exp-003 data_summary.n_observations.
6. LOO ΔELPD=-55.7, SE=9.4, |Δ/SE|=5.9 — need to find source artifact.
7. c_n values in text: 5.60 (registry: 5.587→rounds to 5.59), 4.20 (registry: 4.168→rounds to 4.17). Check if paper rounds differently.
8. N=8 pilot τ=0.857 — from exp-003b, confirmed.
9. Fill rate "~58%" — paper says this but needs verification.
10. "69%" bias slope reduction — from exp-009.

Output a complete structured audit table. For each number found, state:
- The number and its location (file:line)
- What it claims
- Source experiment
- Registry value
- Match status (OK / MISMATCH / UNVERIFIED)
- If mismatch, what the correct value should be

Be thorough — don't skip any numbers. Group by file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ee9bcf2f-84d2-4322-aa38-fb576f70d6d8",
  "agentId": "a92bd2628d8113da1",
  "type": "user",
  "uuid": "78698cdb-f1f2-4a4b-a1b1-5d09e56785fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T19:43:07.042Z_

```json
{
  "parentUuid": "78698cdb-f1f2-4a4b-a1b1-5d09e56785fe",
  "isSidechain": true,
  "agentId": "a92bd2628d8113da1",
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
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
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
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "acde4bf2-1df1-4715-9bbb-1fe58db13eb5",
  "timestamp": "2026-05-25T19:43:07.042Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango"
}
```

---

### Assistant

_source line 3 · 2026-05-25T19:43:09.516Z_

I'll systematically read all the tex files and extract every quantitative claim, then compare against the ground truth values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acde4bf2-1df1-4715-9bbb-1fe58db13eb5",
  "isSidechain": true,
  "agentId": "a92bd2628d8113da1",
  "requestId": "req_011CbPrkmjYRNnDaKmbw8Rwn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5429bae-dd32-47a5-9178-5e554704297d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CefKxyhX3Eaa9iTufjArC8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31871,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31871,
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

_source line 4 · 2026-05-25T19:43:10.799Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BRYJA13mRevwBCGfTUmhDB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5429bae-dd32-47a5-9178-5e554704297d",
  "isSidechain": true,
  "agentId": "a92bd2628d8113da1",
  "requestId": "req_011CbPrkmjYRNnDaKmbw8Rwn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60d28966-b469-4abc-8396-5a9d9de581c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CefKxyhX3Eaa9iTufjArC8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31871,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 31871,
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

_source line 5 · 2026-05-25T19:43:10.814Z_

<details><summary>↩ Tool result · `toolu_01BRYJA13mRevwBCGfTUmhDB`</summary>

```text
1	\begin{abstract}
2	When an LLM judge scores a model response on a benchmark item, the result conflates genuine ability, the judge's scoring tendency, and any advantage from training data exposure. Current evaluation pipelines correct for judge bias and contamination independently, but we show that separate correction is structurally flawed. We formalize this as an omitted variable bias (OVB) problem: any estimator that models one distortion while omitting the other produces systematically biased ability estimates, regardless of correction order. We propose the Gated Many-Facet Rasch Model (G-MFRM), a Bayesian framework that jointly estimates model ability, judge severity, and contamination susceptibility with formal identifiability guarantees. In synthetic experiments ($N = 50$), G-MFRM reduces ability RMSE by 51\% over sequential pipelines ($p < 0.001$) and recovers contamination susceptibility with Pearson $r = 0.81$. On Arena-Hard, G-MFRM provides interpretable per-model contamination diagnostics (in an 8-model pilot, older models exhibit 4--6$\times$ higher susceptibility), and a controlled coverage ablation demonstrates that over-correction decreases from $\Delta\tau = -0.044$ at 46\% coverage to $\Delta\tau = 0$ at full coverage, quantifying exposure estimation requirements for contamination-aware evaluation. Leave-one-out cross-validation confirms improved predictive fit ($|\Delta\mathrm{ELPD}/\mathrm{SE}| = 5.9$)\footnote{Code and data are available at \url{https://anonymous.4open.science/r/gated_mfrm_judge_bias-43CC/}.}.
3	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60d28966-b469-4abc-8396-5a9d9de581c2",
  "isSidechain": true,
  "promptId": "ee9bcf2f-84d2-4322-aa38-fb576f70d6d8",
  "agentId": "a92bd2628d8113da1",
  "type": "user",
  "uuid": "e5707213-2506-45a6-bb59-aa579e44174b",
  "sourceToolAssistantUUID": "60d28966-b469-4abc-8396-5a9d9de581c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T19:43:11.257Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BrFucvT5ovaQX43Y328Vgw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5707213-2506-45a6-bb59-aa579e44174b",
  "isSidechain": true,
  "agentId": "a92bd2628d8113da1",
  "requestId": "req_011CbPrkmjYRNnDaKmbw8Rwn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "84bbbffd-578f-4e19-8d20-b88a147521e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CefKxyhX3Eaa9iTufjArC8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31871,
      "cache_read_input_tokens": 0,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 31871
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 180,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 31871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 31871,
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

_source line 7 · 2026-05-25T19:43:11.264Z_

<details><summary>↩ Tool result · `toolu_01BrFucvT5ovaQX43Y328Vgw`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When multiple LLM judges evaluate model responses on a benchmark, their scores are shaped by at least three forces: the model's genuine ability, the judge's own scoring tendency, and any advantage the model gained from encountering benchmark items during training. These three signals are entangled in every observation. The evaluation community has developed separate tools for the latter two distortions: judge bias correction methods calibrate inter-judge differences \citep{cyclicjudge2026, uda2026}, while contamination detection tools flag or adjust for memorized items \citep{constat2024, dcr2025, logprober2024}. A practitioner who faces both problems must apply these corrections sequentially. This paper shows that sequential correction produces systematically biased rankings, not merely noisy ones.
5	
6	\begin{figure*}[t]
7	\centering
8	\includegraphics[width=\textwidth]{fig1_framework_v2}
9	\caption{(a)~Sequential pipelines address judge bias and contamination independently; omitted variable bias confounds the unmodeled facet into ability estimates. (b)~G-MFRM three-stage joint calibration: Stage~1 fits a standard MFRM for initial estimates $(\hat{\theta}, \hat{b}, \hat{d})$; Stage~2 estimates per-item exposure $e_i$ from external evidence (reference model anchoring, cross-model agreement, and optionally LogProber); Stage~3 performs joint MCMC inference with $e_i$ fixed, recovering contamination-corrected ability $\hat{\theta}_n$, contamination susceptibility $c_n$, and judge severity $d_j$.}
10	\label{fig:framework}
11	\end{figure*}
12	
13	We formalize this failure as an omitted variable bias (OVB) problem \citep{angrist2009mostly}. Consider a model that has memorized some benchmark items and a judge that scores more strictly than average. A bias-only correction adjusts for the strict judge but leaves the contamination signal untouched; the inflated scores on memorized items get absorbed into the model's estimated ability. Conversely, a contamination-only adjustment removes the memorization signal but conflates systematic scoring differences with contamination variation. In both cases, the omitted facet biases the modeled one. Within the Many-Facet Rasch Model (MFRM) framework \citep{linacre1989mfrm}, we show this bias is directional: contaminated models are systematically overestimated under bias-only correction, and the bias persists regardless of which correction comes first (Section~\ref{sec:confounding}).
14	
15	Resolving this confounding requires joint estimation. We propose the Gated Many-Facet Rasch Model (G-MFRM), which extends MFRM with a multiplicative gating term $c_n \cdot e_i$ for contamination susceptibility, inspired by Doubly-Gated Item Response Theory \citep{shu2013dgirt}. Through a three-stage calibration procedure with externally anchored per-item exposure indicators (Figure~\ref{fig:framework}), G-MFRM simultaneously recovers model ability, item difficulty, judge severity, and contamination susceptibility. We prove that external anchoring of exposure is both necessary and sufficient for parameter identification under standard multi-judge designs (Theorem~\ref{thm:sufficient}), and derive error propagation bounds for the staged estimation.
16	
17	In synthetic experiments ($N = 50$ models, 20 seeds), G-MFRM reduces ability RMSE by 51\% relative to sequential estimation ($p < 0.001$) and recovers contamination susceptibility with Pearson $r = 0.81$. On Arena-Hard \citep{li2024arenahard}, G-MFRM produces interpretable per-model contamination diagnostics (in an 8-model pilot, older models such as GPT-3.5-Turbo and GPT-4-0613 exhibit 4--6$\times$ higher susceptibility than recent models such as GPT-4o), and a controlled coverage ablation with 17 models and 6 judges traces over-correction to incomplete exposure estimation ($\Delta\tau$: $-0.044 \to -0.015 \to 0.000$ as coverage increases from 46\% to 100\%). Leave-one-out cross-validation strongly favors joint estimation ($|\Delta\mathrm{ELPD}/\mathrm{SE}| = 5.9$; stacking weight 1.0). Our contributions are:
18	\begin{enumerate}
19	    \item A formal analysis of judge-contamination confounding as omitted variable bias, proving that sequential correction cannot resolve the confounding under non-orthogonality (Section~\ref{sec:confounding}).
20	    \item The G-MFRM framework with identifiability guarantees and error propagation bounds for staged estimation (Section~\ref{sec:method}).
21	    \item Empirical validation on Arena-Hard yielding interpretable contamination diagnostics, with a controlled coverage ablation tracing over-correction to incomplete exposure estimation (Section~\ref{sec:experiments}).
22	\end{enumerate}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84bbbffd-578f-4e19-8d20-b88a147521e1",
  "isSidechain": true,
  "promptId": "ee9bcf2f-84d2-4322-aa38-fb576f70d6d8",
  "agentId": "a92bd2628d8113da1",
  "type": "user",
  "uuid": "37ad0469-fa5c-4b9b-8bc8-a97bfb29bc36",
  "sourceToolAssistantUUID": "84bbbffd-578f-4e19-8d20-b88a147521e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T19:43:14.455Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QZLUrGDHJBcxf7TRA1QJ3V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37ad0469-fa5c-4b9b-8bc8-a97bfb29bc36",
  "isSidechain": true,
  "agentId": "a92bd2628d8113da1",
  "requestId": "req_011CbPrm5yeUgfnUEg5KXtWn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1321161e-b5fc-4264-9f17-77f4bbd33a3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FRDQFSiQSApNRS8KNPWJjm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2750,
      "cache_read_input_tokens": 31871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2750,
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

_source line 9 · 2026-05-25T19:43:14.461Z_

<details><summary>↩ Tool result · `toolu_01QZLUrGDHJBcxf7TRA1QJ3V`</summary>

```text
1	\section{Confounding in LLM Evaluation}
2	\label{sec:confounding}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{fig2_ovb_bias}
7	\caption{Sequential estimation bias ($\hat{\theta}_{\mathrm{seq}} - \theta_{\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.86$ ($p < 0.001$) confirms systematic overestimation of contaminated models. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}
8	\label{fig:ovb_bias}
9	\end{figure}
10	
11	The Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies
12	%
13	\begin{equation}
14	\label{eq:mfrm}
15	\log \frac{P(Y_{nij} \geq k \mid \theta_n, b_i, d_j, \gamma_k)}{P(Y_{nij} < k \mid \theta_n, b_i, d_j, \gamma_k)} = \theta_n - b_i - d_j - \gamma_k,
16	\end{equation}
17	%
18	where $Y_{nij}$ is the ordinal rating by judge $j$ for model $n$ on item $i$, $\theta_n$ is the ability of model $n$ ($n = 1, \ldots, N$), $b_i$ is the difficulty of item $i$ ($i = 1, \ldots, I$), $d_j$ is the severity of judge $j$ ($j = 1, \ldots, J$), and $\gamma_k$ is the threshold for category $k$. All facets reside on a common logit scale, so model ability is directly comparable after adjustment for item difficulty and judge severity. \citet{jiao2025mfrm_llm} applied this framework to compare ten LLM raters with human experts and showed that MFRM separates genuine ability from systematic judge effects in multi-judge panels.
19	
20	However, standard MFRM assumes that all systematic sources of score variation are captured by the modeled facets. This assumption breaks down when some models have been exposed to benchmark items during training \citep{dcr2025}. Such contamination inflates scores on exposed items through memorization rather than genuine ability. We represent this effect as an interaction $c_n \cdot e_i$, where $c_n \geq 0$ is the contamination susceptibility of model $n$ and $e_i \in [0, 1]$ is the exposure level of item $i$. The complete data-generating process becomes
21	%
22	\begin{equation}
23	\label{eq:full}
24	\eta_{nijk} = \theta_n - b_i - d_j - \gamma_k + c_n \cdot e_i.
25	\end{equation}
26	
27	
28	When a practitioner fits the standard MFRM (Eq.~\ref{eq:mfrm}) to data generated by Eq.~\ref{eq:full}, the contamination term is absent from the estimated model. Its influence does not vanish but is absorbed into the estimated parameters $\tilde{\theta}_n$, $\tilde{b}_i$, and $\tilde{d}_j$, which distorts all downstream inferences.
29	
30	The consequence of this omission can be stated precisely.
31	
32	\begin{observation}[Omitted Variable Bias in MFRM]
33	\label{obs:ovb}
34	Let the full model be $\eta_{nijk} = \theta_n - b_i - d_j - \gamma_k + c_n \cdot e_i$ and the short model omit the contamination term: $\tilde{\eta}_{nijk} = \tilde{\theta}_n - \tilde{b}_i - \tilde{d}_j - \gamma_k$. Under a linear approximation to the ordinal logit link \citep{wooldridge2010, angrist2009mostly},\footnote{The OVB formula is exact for linear models. We apply it to the MFRM linear predictor $\eta$, which is an approximation. Synthetic validation confirms the approximation quality: the Pearson correlation between the predicted bias direction and empirical bias reaches $r = 0.86$ ($p < 0.001$); the linear result accurately characterizes bias direction and relative magnitude.}
35	\begin{equation}
36	\label{eq:ovb}
37	\mathrm{plim}(\tilde{\theta}_n - \theta_n) = \delta_n \cdot c_n,
38	\end{equation}
39	where $\delta_n$ depends on the projection of the exposure vector $(e_i)$ onto the design matrix of the short model (explicit form in Appendix~\ref{app:gamma}). The bias is non-zero whenever $\mathrm{Cov}(d_j,\, c_n \cdot e_i) \neq 0$. This captures the confounding component; in the nonlinear MFRM, a specification bias from omitting $c_n \cdot e_i$ persists even at zero covariance (Section~\ref{sec:experiments}).
40	\end{observation}
41	
42	While the OVB framework provides the analytical lens for understanding \emph{why} omitting contamination biases ability estimates, our empirical results (Section~\ref{sec:experiments}) reveal that the bias magnitude is driven primarily by the specification error itself rather than the exposure-severity covariance term---a finding that strengthens the case for joint modeling regardless of the covariance structure. G-MFRM uses the full nonlinear likelihood; the linear approximation serves only as directional motivation. Monte Carlo simulation confirms that bias magnitude is approximately constant across confounding levels $\rho$ (Figure~\ref{fig:bias_vs_rho}): omission of $c_n \cdot e_i$, not its correlation with $d_j$, is the primary driver. Joint estimation reduces the bias slope by ${\sim}$69\% at all $\rho$ levels. Neither sequential ordering resolves this: bias-first approaches \citep{cyclicjudge2026} absorb contamination into $\hat{\theta}$, while contamination-first approaches \citep{dcr2025} misattribute judge severity as contamination ($r = 0.86$, $p < 0.001$; Figure~\ref{fig:ovb_bias}).
43	
44	\begin{figure}[t]
45	\centering
46	\includegraphics[width=\columnwidth]{fig4_bias_vs_rho}
47	\caption{Sequential estimation bias is approximately constant across confounding levels $\rho$, confirming that omission of the contamination term, not its correlation with judge severity, drives the bias. Joint G-MFRM reduces the bias slope by ${\sim}$69\% at all $\rho$ levels. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}
48	\label{fig:bias_vs_rho}
49	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1321161e-b5fc-4264-9f17-77f4bbd33a3e",
  "isSidechain": true,
  "promptId": "ee9bcf2f-84d2-4322-aa38-fb576f70d6d8",
  "agentId": "a92bd2628d8113da1",
  "type": "user",
  "uuid": "4c74840c-c0a0-4c13-9175-c26c52f57e7e",
  "sourceToolAssistantUUID": "1321161e-b5fc-4264-9f17-77f4bbd33a3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T19:43:14.565Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PY948wjKQ2k2GqBsgzCVk7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c74840c-c0a0-4c13-9175-c26c52f57e7e",
  "isSidechain": true,
  "agentId": "a92bd2628d8113da1",
  "requestId": "req_011CbPrm5yeUgfnUEg5KXtWn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f322d15f-4c69-4ad4-834e-c2def3fe1159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FRDQFSiQSApNRS8KNPWJjm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2750,
      "cache_read_input_tokens": 31871,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2750
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 155,
          "cache_read_input_tokens": 31871,
          "cache_creation_input_tokens": 2750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2750,
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

_source line 11 · 2026-05-25T19:43:14.570Z_

<details><summary>↩ Tool result · `toolu_01PY948wjKQ2k2GqBsgzCVk7`</summary>

```text
1	\section{The G-MFRM Framework}
2	\label{sec:method}
3	
4	Section~\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and a hierarchical HalfNormal prior for the contamination term, are motivated by the identifiability analysis in \S\ref{sec:identifiability} and the error propagation bounds in \S\ref{sec:error_prop}.
5	
6	\subsection{Model Specification}
7	\label{sec:model_spec}
8	
9	G-MFRM extends the standard MFRM \citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\ref{eq:mfrm}):
10	%
11	\begin{equation}
12	\label{eq:gmfrm}
13	\log \frac{P(Y_{nij} \geq k)}{P(Y_{nij} < k)} = \theta_n - b_i - d_j - \gamma_k + c_n \cdot e_i,
14	\end{equation}
15	%
16	where all terms carry the definitions from Section~\ref{sec:confounding}. The gating structure $c_n \cdot e_i$ separates model-specific contamination susceptibility ($c_n \geq 0$) from item-specific exposure ($e_i \in [0,1]$). When $c_n = 0$ or $e_i = 0$, the gating term vanishes and Eq.~\ref{eq:gmfrm} reduces to the standard MFRM.
17	
18	We enforce non-negativity and sparsity through a hierarchical HalfNormal prior: $\sigma_c \sim \text{HalfNormal}(1.0)$, $c^{\mathrm{raw}}_n \sim \text{HalfNormal}(1.0)$, $c_n = c^{\mathrm{raw}}_n \cdot \sigma_c$. The hierarchical structure provides adaptive shrinkage: when data support low contamination, $\sigma_c$ contracts toward zero. The remaining priors are $\theta_n \sim \mathcal{N}(0, 1)$, $b_i \sim \mathcal{N}(0, 1)$, $d_j \sim \mathcal{N}(0, 0.5)$, and uniform on $\gamma_k$.
19	
20	G-MFRM extends the Doubly-Gated IRT model of \citet{shu2013dgirt} from binary gating to continuous exposure and multi-rater designs, and contributes the first formal identifiability conditions for gated IRT parameters (Propositions~\ref{prop:no_new}--\ref{prop:exposure_variation}, Theorem~\ref{thm:sufficient}) and error propagation bounds for staged estimation (\S\ref{sec:error_prop}).
21	
22	\subsection{Staged Estimation}
23	\label{sec:staged}
24	
25	Joint estimation of all parameters in Eq.~\ref{eq:gmfrm}, including $e_i$, would require identifying the bilinear product $c_n \cdot e_i$ from response data alone. This creates a fundamental non-identifiability (Proposition~\ref{prop:exposure_variation}). We resolve this through a three-stage procedure that fixes exposure externally before estimating the contamination parameters.
26	
27	\paragraph{Stage 1: Standard MFRM.} We fit the standard MFRM (Eq.~\ref{eq:mfrm}) via MCMC (NUTS) to obtain initial estimates $(\hat{\theta}, \hat{b}, \hat{d})$. These serve as warm-start values for the sampler in Stage~3 and improve convergence.
28	
29	\paragraph{Stage 2: Exposure estimation.} Per-item exposure $e_i$ is estimated from external evidence independent of the response data. The primary signal is \emph{reference model anchoring} (75\% weight): win-rate residuals against a fixed anchor (gpt-4-0314) flag items where target models outperform difficulty-adjusted expectations. The secondary signal is \emph{cross-model agreement} (25\%): uniformly high scores across diverse architectures suggest exposure rather than easiness. The composite is clipped to $[0, 1]$ and fixed in Stage~3. Estimation is non-circular: $e_i$ is item-level while $c_n$ is model-level, and ablation with 100\% anchoring yields $\rho = 0.998$ (Appendix~\ref{app:weight_robustness}).
30	
31	\paragraph{Stage 3: Joint MCMC.} With $e_i$ fixed, we sample $(\theta_n, b_i, d_j, c_n)$ jointly via the No-U-Turn Sampler (NUTS) \citep{betancourt2015}. The priors are as specified in \S\ref{sec:model_spec}. The hierarchical contamination prior decomposes as
32	%
33	\begin{align}
34	\label{eq:contam_prior}
35	\sigma_c &\sim \text{HalfNormal}(1.0), \quad c^{\mathrm{raw}}_n \sim \text{HalfNormal}(1.0), \nonumber \\
36	c_n &= c^{\mathrm{raw}}_n \cdot \sigma_c,
37	\end{align}
38	%
39	where $\sigma_c$ is a shared global scale that governs the overall contamination magnitude. This non-centered parameterization improves sampler geometry by decoupling the global scale from the per-model effects.
40	
41	Convergence is assessed via rank-normalized split-$\hat{R}$ \citep{vehtari2021rhat} and bulk effective sample size (ESS), with thresholds $\hat{R} < 1.05$ and ESS$_{\mathrm{bulk}} > 100$ following standard practice \citep{gelman2013bda}.\footnote{Synthetic validation with $N = 50$, $I = 100$, $J = 8$ yields satisfactory convergence across all parameters. Full diagnostic tables are reported in Section~\ref{sec:experiments}.}
42	
43	
44	\begin{figure}[t]
45	\centering
46	\includegraphics[width=\columnwidth]{forest_dj}
47	\caption{Judge severity estimates ($d_j$) with 95\% credible intervals for the full 9-judge panel ($N = 8$ analysis). Positive values indicate stricter scoring; the severity range spans 1.34 logits. The $N = 17$ analysis (\S\ref{sec:setup}) uses a 6-judge subset selected for item coverage.}
48	\label{fig:judge_severity}
49	\end{figure}
50	
51	\subsection{Identifiability}
52	\label{sec:identifiability}
53	
54	We establish that fixing $e_i$ externally is both necessary and sufficient for identifying the contamination parameters. All proofs assume $\sum_n \theta_n = 0$.
55	
56	\begin{proposition}[No New Indeterminacy]
57	\label{prop:no_new}
58	When $e_i$ is fixed externally, $c_n \cdot e_i$ introduces no additional location or scale indeterminacy beyond the standard MFRM.
59	\end{proposition}
60	
61	\begin{proposition}[Exposure Variation Necessary]
62	\label{prop:exposure_variation}
63	If $e_i = e$ for all $i$ (constant exposure), then $c_n$ and $\theta_n$ are not separately identifiable; hence $\mathrm{Var}(e_i) > 0$ is necessary.
64	\end{proposition}
65	
66	Proofs are in Appendix~\ref{app:prop_proofs}.
67	
68	\begin{theorem}[Sufficient Conditions for Local Identifiability]
69	\label{thm:sufficient}
70	G-MFRM is locally identifiable if: (i) a connected observation design, (ii) $J \geq 2$ judges, (iii) each model observes items with at least two distinct exposure values, and (iv) $\sum_n \theta_n = 0$.
71	\end{theorem}
72	
73	The proof (Appendix~\ref{app:proof}) follows \citet{rothenberg1971} and establishes Fisher information non-singularity via the Cauchy--Schwarz inequality on the $(\theta_n, c_n)$ submatrix. Monte Carlo validation confirms successful $c_n$ recovery (Appendix~\ref{app:cn_recovery}).
74	
75	\subsection{Error Propagation}
76	\label{sec:error_prop}
77	
78	Treating Stage~2 estimates $\hat{e}_i$ as fixed creates a generated regressors problem \citep{pagan1984}. Let $\hat{e}_i = e_i + \epsilon_i$ with $\epsilon_i \sim \mathcal{N}(0, \sigma^2)$. The attenuation factor is $\lambda(\sigma) = \mathrm{Var}(e_i) / [\mathrm{Var}(e_i) + \sigma^2]$, reaching 50\% at $\sigma \approx 0.2$ in our setting ($\mathrm{Var}(e_i) \approx 0.04$). Empirically, $\theta$-RMSE increases by only 5.9\% and $c_n$-RMSE by 7.9\% below this threshold; beyond it ($\sigma = 0.5$), degradation becomes severe (Table~\ref{tab:error_prop}, Appendix~\ref{app:error_prop}). We apply the Murphy--Topel correction \citep{murphy1985} for honest credible intervals (Appendix~\ref{app:murphy_topel}).
79	
80	\subsection{Fair Scores and Diagnostics}
81	\label{sec:fair_scores}
82	
83	The Stage~3 posterior mean of $\theta_n$ provides a bias-and-contamination-corrected ``fair score'' for each model. The remaining parameters serve complementary diagnostic roles: per-model $c_n$ flags candidates for training data audit, per-judge $d_j$ informs judge calibration, and per-item $e_i$ identifies items for retirement or replacement.
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f322d15f-4c69-4ad4-834e-c2def3fe1159",
  "isSidechain": true,
  "promptId": "ee9bcf2f-84d2-4322-aa38-fb576f70d6d8",
  "agentId": "a92bd2628d8113da1",
  "type": "user",
  "uuid": "b1f75664-4191-4b06-be37-4c491191d6aa",
  "sourceToolAssistantUUID": "f322d15f-4c69-4ad4-834e-c2def3fe1159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T19:43:17.850Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NeCeg9k352SCEPgu9nqehb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1f75664-4191-4b06-be37-4c491191d6aa",
  "isSidechain": true,
  "agentId": "a92bd2628d8113da1",
  "requestId": "req_011CbPrmLCQz6wJbo69E9SHP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71e9d3ed-dac4-47e4-8fea-ee3b0f5e449e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HwZXZtHt9YQ3RNL9dobZiY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4883,
      "cache_read_input_tokens": 34621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4883,
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

_source line 13 · 2026-05-25T19:43:17.869Z_

<details><summary>↩ Tool result · `toolu_01NeCeg9k352SCEPgu9nqehb`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{fig5_6_combined}
7	\caption{Contamination diagnostics ($N = 8$ pilot, 9 judges). (a)~Contamination susceptibility $\hat{c}_n$ (posterior mean $\pm$ 95\% CI), ordered by magnitude. Older models (GPT-3.5-Turbo, GPT-4-0613) show 4--6$\times$ higher susceptibility than recent models (GPT-4o). (b)~Ability bias absorbed by MFRM-only estimation: $\Delta\theta = \hat{\theta}_{\mathrm{MFRM}} - \hat{\theta}_{\mathrm{G\text{-}MFRM}}$. The monotonic relationship (Spearman $\rho = 1.0$; $N = 8$, interpret with caution) confirms that contamination inflates MFRM ability estimates for high-$c_n$ models, as predicted by the OVB analysis (Section~\ref{sec:confounding}).}
8	\label{fig:contamination_and_bias}
9	\end{figure*}
10	
11	\subsection{Setup}
12	\label{sec:setup}
13	
14	Our main experiment uses $N = 17$ target models evaluated by 6 LLM judges; a smaller $N = 8$ pilot with 9 judges validates sample-size effects. Table~\ref{tab:main_results} reports both configurations as part of the coverage analysis.
15	
16	\paragraph{Data and models.} We evaluate on Arena-Hard \citep{li2024arenahard}, a benchmark of 500 multi-turn conversational items selected for high separability among frontier models. The evaluation uses all 500 items in a connected incomplete design (${\sim}$58\% fill rate of the $N \times I \times J$ tensor). Seventeen target models spanning proprietary and open-source families are evaluated: GPT-4o, GPT-4o-mini, Qwen2.5-72B, LLaMA-3.3-70B, Qwen3-8B, Gemma-2-9B, GPT-4-0613, GPT-3.5-Turbo, Claude-3.5-Sonnet, GPT-4-Turbo, LLaMA-3.1-70B, Gemma-2-27B, Claude-3-Opus, LLaMA-3-70B, Mixtral-8x22B, Claude-3-Haiku, and LLaMA-3-8B. Ground-truth rankings are derived from Chatbot Arena human preference data \citep{zheng2023mtbench}.
17	
18	\paragraph{Judges.} Six LLM judges score responses in position-swapped pairwise mode: Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini-2.5-Pro, LLaMA-3.3-70B, Qwen2.5-72B, and Qwen3-235B. Four provide complete item coverage; two (Gemini, Sonnet) cover ${\sim}$63--79\% of items; this yields an incomplete connected design. Two models serve as both judge and target; $d_j$ absorbs self-evaluation bias ($\tau$ unchanged when excluding self-judging; Appendix~\ref{app:self_eval}).
19	
20	\paragraph{Exposure estimation.} Per-item $e_i$ follows the two-source pipeline in \S\ref{sec:staged} (75\% reference anchoring, 25\% cross-model agreement; robust to weight configuration, $\rho \geq 0.998$; Appendix~\ref{app:weight_robustness}).
21	
22	\paragraph{MCMC.} NumPyro NUTS, 6{,}000 warmup $+$ 4{,}000 samples $\times$ 4 chains (target acceptance 0.95). Convergence: $\hat{R} < 1.05$, ESS $> 100$ \citep{vehtari2021rhat, gelman2013bda}.
23	
24	\subsection{Main Results}
25	\label{sec:main_results}
26	
27	\begin{table}[t]
28	\centering
29	\footnotesize
30	\setlength{\tabcolsep}{3.5pt}
31	\begin{tabular}{lccccc}
32	\toprule
33	\textbf{Item Set} & \textbf{Items} & \textbf{Cov.} & $\tau_{\mathrm{raw}}$ & $\tau_{\mathrm{G\text{-}MFRM}}$ & $\Delta\tau$ \\
34	\midrule
35	\multicolumn{6}{l}{\textit{$N = 17$, 6 judges (main experiment)}} \\
36	Full set & 500 & 46\% & 0.838 & 0.794 & $-$0.044 \\
37	Filtered & 317 & 73\% & 0.824 & 0.809 & $-$0.015 \\
38	Exposed-only & 231 & 100\% & 0.779 & 0.779 & \phantom{$-$}0.000 \\
39	\midrule
40	\multicolumn{6}{l}{\textit{$N = 8$, 9 judges (pilot)}} \\
41	Full set & 176 & -- & 0.786 & 0.857$^{\dagger}$ & $+$0.071 \\
42	\bottomrule
43	\end{tabular}
44	\caption{Ranking accuracy (Kendall $\tau$ against Chatbot Arena) as a function of exposure coverage. G-MFRM over-correction decreases across all three coverage levels ($\Delta\tau$: $-0.044 \to -0.015 \to 0.000$). At full coverage, G-MFRM matches the raw average exactly; the pilot ($N = 8$) suggests positive $\Delta\tau$ when coverage is adequate. All seven baselines (MFRM-only, Sequential, CyclicJudge, DCR Factor, Pref.\ Leakage) produce $\tau$ within 0.014 of the raw average at both panel sizes. $^{\dagger}$Bootstrap $\Delta\tau$ CI includes zero.}
45	\label{tab:main_results}
46	\end{table}
47	
48	We compare G-MFRM against seven baselines that address judge bias or contamination separately (Table~\ref{tab:main_results}): Raw Average, MFRM-only (Eq.~\ref{eq:mfrm}), Sequential (MFRM then contamination adjustment), CyclicJudge \citep{cyclicjudge2026}, CyclicJudge+discard, DCR Factor \citep{dcr2025}, and Preference Leakage calibration \citep{preference_leakage2026}. All methods are evaluated by Kendall $\tau$ and Spearman $\rho$ against Chatbot Arena human rankings.
49	
50	\paragraph{Synthetic validation.} On synthetic data ($N = 50$, 20 seeds), G-MFRM reduces ability RMSE by 51\% relative to sequential estimation ($p < 10^{-6}$) and improves ranking accuracy ($\tau$: $0.922$ vs.\ $0.839$, Wilcoxon $p < 0.001$). Contamination susceptibility is recovered with Pearson $r = 0.81$.
51	
52	\paragraph{Predictive fit.} In the $N = 8$ pilot, LOO cross-validation strongly favors G-MFRM over MFRM-only (Expected Log Pointwise Predictive Density difference $\Delta\mathrm{ELPD}_{\mathrm{LOO}} = -55.7$, SE $= 9.4$, $|\Delta/\mathrm{SE}| = 5.9$; \citealp{vehtari2017loo}), with stacking weight 1.0 and all Pareto $\hat{k} < 0.7$ (Appendix~\ref{app:loo_comparison}).
53	
54	\paragraph{Reconciling predictive fit and ranking accuracy.} The LOO improvement and the ranking degradation are not contradictory: they measure different quantities. LOO-ELPD evaluates observation-level predictive accuracy across all $(n, i, j)$ triples: it rewards the model for capturing contamination structure in individual responses. Kendall $\tau$ evaluates aggregate system-level rankings, which are sensitive to the accuracy of per-item exposure estimates $e_i$. The separation indicates that the contamination signal is real (the model fits better), but incomplete exposure coverage causes the correction to over-correct when aggregated to rankings. The coverage ablation below confirms this interpretation.
55	
56	\paragraph{Exposure coverage and ranking accuracy.} G-MFRM's ranking accuracy on real data depends on exposure estimation quality. At $N = 17$, the full item set (500 items) has only 46\% of items with non-zero exposure estimates; G-MFRM over-corrects on the remaining items, and the result is $\Delta\tau = -0.044$ relative to the raw average ($\tau = 0.794$ vs.\ $0.838$). We trace this degradation through three item subsets with increasing exposure coverage:
57	%
58	\begin{itemize}
59	    \item Full set (500 items, 46\% $e_i > 0$): $\Delta\tau = -0.044$
60	    \item Filtered set (317 items, 73\% $e_i > 0$): $\Delta\tau = -0.015$
61	    \item Exposed-only (231 items, 100\% $e_i > 0$): $\Delta\tau = 0.000$
62	\end{itemize}
63	%
64	This controlled ablation ($-0.044 \to -0.015 \to 0.000$) demonstrates that over-correction is attributable to incomplete exposure coverage. Two additional variants confirm the mechanism: MFRM-only on the filtered set yields $\Delta\tau = 0.000$, which isolates the degradation to the contamination gating term; a contamination-only variant without severity modeling yields $\Delta\tau = -0.118$, evidence that naive linear contamination deduction without joint calibration is catastrophically harmful.
65	
66	\paragraph{Contamination diagnostics.} G-MFRM's primary real-data contribution is interpretable per-model contamination estimation. In the $N = 8$ pilot, the contamination susceptibility profile (Figure~\ref{fig:contamination_and_bias}a) reveals a clear gradient by model age: older models show $\hat{c}_n > 4$ (GPT-3.5-Turbo: $5.60$; GPT-4-0613: $4.20$), while recent models show near-zero susceptibility (GPT-4o: $0.88$; GPT-4o-mini: $0.93$). MFRM-only estimation absorbs this contamination signal into ability estimates, inflating $\hat{\theta}$ for the most contaminated models by up to 0.79 logits (Figure~\ref{fig:contamination_and_bias}b; Spearman $\rho = 1.0$ between $\hat{c}_n$ and $\Delta\theta$, though with only $N = 8$ data points, perfect rank correlation is not statistically remarkable and should not be interpreted as a robust finding). The $N = 17$ analysis preserves the same age gradient at lower absolute scale (GPT-3.5-Turbo: $2.57$; GPT-4-0613: $3.78$), consistent with shrinkage from the larger model population. All parameters achieve $\hat{R} \leq 1.003$ with ESS $\geq 1{,}240$ in the $N = 8$ pilot (Appendices~\ref{app:item_diagnostics} and~\ref{app:ppc}).
67	
68	\paragraph{Judge severity and panel design.} Judge severity profiles vary across the panel (Figure~\ref{fig:judge_severity}), and contamination--ability separation improves with severity diversity: panels with $k \geq 4$ judges covering the severity extremes provide the most reliable diagnostic output (Appendix~\ref{app:judge_count}). Leave-one-judge-out analysis identifies three individually necessary judges---those at the strict and lenient extremes of the $d_j$ distribution---whose removal reduces G-MFRM $\tau$ to the baseline. This finding suggests that judge panels should prioritize scoring tendency diversity over judge count alone.
69	
70	
71	\subsection{Error Propagation and Ablation}
72	\label{sec:error_prop_results}
73	
74	\begin{figure}[t]
75	\centering
76	\includegraphics[width=\columnwidth]{fig_ablation_rmse}
77	\caption{Ablation on synthetic data ($N = 50$, 20 seeds). Joint estimation drives the improvement: staged estimation doubles $\theta$-RMSE ($p < 0.001$). Continuous gating provides a moderate gain over binary ($p < 0.001$); removing judge severity $d_j$ has negligible effect on ability recovery (n.s.).}
78	\label{fig:ablation}
79	\end{figure}
80	
81	Table~\ref{tab:error_prop} validates the theoretical prediction (\S\ref{sec:error_prop}): below $\sigma = 0.2$, ability RMSE increases by 5.9\% and contamination RMSE by 7.9\%; beyond the threshold ($\sigma = 0.5$), degradation becomes substantial. Ablation (Figure~\ref{fig:ablation}; full results in Table~\ref{tab:ablation}, Appendix~\ref{app:ablation}) confirms joint estimation as the dominant contributor ($2.0\times$ $\theta$-RMSE increase under staged estimation, $p < 0.001$) and continuous gating over binary ($c_n$-RMSE $-$40\%, $p < 0.001$).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71e9d3ed-dac4-47e4-8fea-ee3b0f5e449e",
  "isSidechain": true,
  "promptId": "ee9bcf2f-84d2-4322-aa38-fb576f70d6d8",
  "agentId": "a92bd2628d8113da1",
  "type": "user",
  "uuid": "ff28efdd-b246-4a4b-836c-57905dcf0f65",
  "sourceToolAssistantUUID": "71e9d3ed-dac4-47e4-8fea-ee3b0f5e449e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T19:43:22.375Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QDMfWQZABZ3ZkhgKhdJjL7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff28efdd-b246-4a4b-836c-57905dcf0f65",
  "isSidechain": true,
  "agentId": "a92bd2628d8113da1",
  "requestId": "req_011CbPrmb8LtDuZkccNarsTe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a2d2808-a8e6-4ba3-92a1-9d8eff97c7c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Y3keM51s41u3iwEvETTab8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3727,
      "cache_read_input_tokens": 39504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3727,
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

_source line 15 · 2026-05-25T19:43:22.388Z_

<details><summary>↩ Tool result · `toolu_01QDMfWQZABZ3ZkhgKhdJjL7`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced G-MFRM, a Bayesian measurement model that jointly estimates model ability, judge severity, and contamination susceptibility within a single inferential framework. The key theoretical contribution is formalizing the confounding between judge bias and benchmark contamination as omitted variable bias: omitting the contamination facet produces systematic bias in ability estimates, driven primarily by the specification error itself rather than the exposure-severity covariance (Section~\ref{sec:confounding}).
5	
6	On Arena-Hard, G-MFRM provides interpretable per-model contamination diagnostics unavailable from existing methods: older models exhibit 4--6$\times$ higher susceptibility, and MFRM-only estimation inflates ability for the most contaminated models by up to 0.79 logits. A controlled coverage ablation ($\Delta\tau$: $-0.044 \to -0.015 \to 0.000$ as coverage increases to 100\%) demonstrates that over-correction is attributable to incomplete exposure estimation, and complete coverage eliminates the over-correction observed in partial-coverage settings. Ablation confirms joint estimation as the dominant contributor: staged estimation doubles ability RMSE.
7	
8	Two practical implications emerge. First, evaluation frameworks that treat judge bias and contamination as independent incur systematic errors; future LLM evaluation should model these facets jointly. Second, the coverage--degradation finding provides an actionable quality requirement for contamination-aware evaluation. For practitioners operating Arena-style evaluations, G-MFRM can serve as a post-hoc calibration layer: given pairwise judgments and exposure estimates, the model produces contamination-adjusted rankings and flags models warranting training data audits. The exposure estimation pipeline (\S\ref{sec:staged}) is modular, so improved contamination detectors can substitute for reference anchoring without modifying the measurement model.
9	
10	Several directions remain open: higher-rank contamination decompositions for domain-specific effects, simulation-based recalibration \citep{talts2018sbc} of $c_n$ credible intervals (71\% coverage at nominal 95\%), and scaling to larger model populations and diverse benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a2d2808-a8e6-4ba3-92a1-9d8eff97c7c5",
  "isSidechain": true,
  "promptId": "ee9bcf2f-84d2-4322-aa38-fb576f70d6d8",
  "agentId": "a92bd2628d8113da1",
  "type": "user",
  "uuid": "f5127394-85a0-45a8-890a-6a258a5152f7",
  "sourceToolAssistantUUID": "4a2d2808-a8e6-4ba3-92a1-9d8eff97c7c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T19:43:22.430Z_

<details open><summary>🔧 Tool call — Read · `toolu_014shwuTYP9z1VxoaTJdvcQg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5127394-85a0-45a8-890a-6a258a5152f7",
  "isSidechain": true,
  "agentId": "a92bd2628d8113da1",
  "requestId": "req_011CbPrmb8LtDuZkccNarsTe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "30971551-2a5f-4b06-8479-9652dc7df13d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Y3keM51s41u3iwEvETTab8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3727,
      "cache_read_input_tokens": 39504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3727,
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

_source line 17 · 2026-05-25T19:43:22.441Z_

<details><summary>↩ Tool result · `toolu_014shwuTYP9z1VxoaTJdvcQg`</summary>

```text
1	The evaluation uses a single benchmark (Arena-Hard) with an incomplete observation design (${\sim}$58\% fill rate); generalization to other benchmarks and larger model populations remains to be verified. Posterior credible intervals for contamination susceptibility $c_n$ exhibit systematic overconfidence (71\% coverage at nominal 95\%; Appendix~\ref{app:ci_coverage}), a structural issue from the multiplicative coupling and HalfNormal boundary at $c_n = 0$ that warrants simulation-based recalibration. The rank-1 contamination structure assumes a single $c_n$ per model, whereas contamination may be domain-specific (e.g., coding vs.\ reasoning), motivating higher-rank decompositions in future work. The judge panel comprises six models from four provider families; generalization to more homogeneous panels is untested.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30971551-2a5f-4b06-8479-9652dc7df13d",
  "isSidechain": true,
  "promptId": "ee9bcf2f-84d2-4322-aa38-fb576f70d6d8",
  "agentId": "a92bd2628d8113da1",
  "type": "user",
  "uuid": "ffe2749d-6158-4ccc-8058-6e0f827c9be3",
  "sourceToolAssistantUUID": "30971551-2a5f-4b06-8479-9652dc7df13d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-25T19:43:24.966Z_

Now let me also check for any remaining quantitative details in experiments.tex that I may have missed, specifically around the convergence diagnostics and contamination values:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffe2749d-6158-4ccc-8058-6e0f827c9be3",
  "isSidechain": true,
  "agentId": "a92bd2628d8113da1",
  "requestId": "req_011CbPrmupExiEEdrhsbCATU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d8899cb-9af4-47dc-a187-1fce3eb460f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BKXUJuXSVYJY62F38UEeMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 930,
      "cache_read_input_tokens": 43231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 930,
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

_source line 19 · 2026-05-25T19:43:28.262Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LnRAXSrsaT4CHWu2osdp9v`</summary>

```json
{
  "pattern": "\\d+\\.?\\d*[%×xτρ]|\\d+\\.\\d+|\\d+,\\d+|[0-9]+\\s*\\\\times|p\\s*[<=<>]\\s*[0-9]|\\\\hat\\{R\\}|\\\\tau|ESS|RMSE|\\\\rho|\\\\Delta",
  "path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex",
  "output_mode": "content",
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d8899cb-9af4-47dc-a187-1fce3eb460f3",
  "isSidechain": true,
  "agentId": "a92bd2628d8113da1",
  "requestId": "req_011CbPrmupExiEEdrhsbCATU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e92fe53-bdc9-4ff9-81a3-6390b15c9967",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BKXUJuXSVYJY62F38UEeMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 930,
      "cache_read_input_tokens": 43231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 930,
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

_source line 20 · 2026-05-25T19:43:28.284Z_

<details><summary>↩ Tool result · `toolu_01LnRAXSrsaT4CHWu2osdp9v`</summary>

```text
7:[Omitted long matching line]
16:[Omitted long matching line]
18:\paragraph{Judges.} Six LLM judges score responses in position-swapped pairwise mode: Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini-2.5-Pro, LLaMA-3.3-70B, Qwen2.5-72B, and Qwen3-235B. Four provide complete item coverage; two (Gemini, Sonnet) cover ${\sim}$63--79\% of items; this yields an incomplete connected design. Two models serve as both judge and target; $d_j$ absorbs self-evaluation bias ($\tau$ unchanged when excluding self-judging; Appendix~\ref{app:self_eval}).
20:\paragraph{Exposure estimation.} Per-item $e_i$ follows the two-source pipeline in \S\ref{sec:staged} (75\% reference anchoring, 25\% cross-model agreement; robust to weight configuration, $\rho \geq 0.998$; Appendix~\ref{app:weight_robustness}).
22:\paragraph{MCMC.} NumPyro NUTS, 6{,}000 warmup $+$ 4{,}000 samples $\times$ 4 chains (target acceptance 0.95). Convergence: $\hat{R} < 1.05$, ESS $> 100$ \citep{vehtari2021rhat, gelman2013bda}.
30:\setlength{\tabcolsep}{3.5pt}
33:\textbf{Item Set} & \textbf{Items} & \textbf{Cov.} & $\tau_{\mathrm{raw}}$ & $\tau_{\mathrm{G\text{-}MFRM}}$ & $\Delta\tau$ \\
36:Full set & 500 & 46\% & 0.838 & 0.794 & $-$0.044 \\
37:Filtered & 317 & 73\% & 0.824 & 0.809 & $-$0.015 \\
38:Exposed-only & 231 & 100\% & 0.779 & 0.779 & \phantom{$-$}0.000 \\
41:Full set & 176 & -- & 0.786 & 0.857$^{\dagger}$ & $+$0.071 \\
44:[Omitted long matching line]
48:We compare G-MFRM against seven baselines that address judge bias or contamination separately (Table~\ref{tab:main_results}): Raw Average, MFRM-only (Eq.~\ref{eq:mfrm}), Sequential (MFRM then contamination adjustment), CyclicJudge \citep{cyclicjudge2026}, CyclicJudge+discard, DCR Factor \citep{dcr2025}, and Preference Leakage calibration \citep{preference_leakage2026}. All methods are evaluated by Kendall $\tau$ and Spearman $\rho$ against Chatbot Arena human rankings.
50:\paragraph{Synthetic validation.} On synthetic data ($N = 50$, 20 seeds), G-MFRM reduces ability RMSE by 51\% relative to sequential estimation ($p < 10^{-6}$) and improves ranking accuracy ($\tau$: $0.922$ vs.\ $0.839$, Wilcoxon $p < 0.001$). Contamination susceptibility is recovered with Pearson $r = 0.81$.
52:\paragraph{Predictive fit.} In the $N = 8$ pilot, LOO cross-validation strongly favors G-MFRM over MFRM-only (Expected Log Pointwise Predictive Density difference $\Delta\mathrm{ELPD}_{\mathrm{LOO}} = -55.7$, SE $= 9.4$, $|\Delta/\mathrm{SE}| = 5.9$; \citealp{vehtari2017loo}), with stacking weight 1.0 and all Pareto $\hat{k} < 0.7$ (Appendix~\ref{app:loo_comparison}).
54:[Omitted long matching line]
56:\paragraph{Exposure coverage and ranking accuracy.} G-MFRM's ranking accuracy on real data depends on exposure estimation quality. At $N = 17$, the full item set (500 items) has only 46\% of items with non-zero exposure estimates; G-MFRM over-corrects on the remaining items, and the result is $\Delta\tau = -0.044$ relative to the raw average ($\tau = 0.794$ vs.\ $0.838$). We trace this degradation through three item subsets with increasing exposure coverage:
59:    \item Full set (500 items, 46\% $e_i > 0$): $\Delta\tau = -0.044$
60:    \item Filtered set (317 items, 73\% $e_i > 0$): $\Delta\tau = -0.015$
61:    \item Exposed-only (231 items, 100\% $e_i > 0$): $\Delta\tau = 0.000$
64:[Omitted long matching line]
66:[Omitted long matching line]
68:[Omitted long matching line]
77:\caption{Ablation on synthetic data ($N = 50$, 20 seeds). Joint estimation drives the improvement: staged estimation doubles $\theta$-RMSE ($p < 0.001$). Continuous gating provides a moderate gain over binary ($p < 0.001$); removing judge severity $d_j$ has negligible effect on ability recovery (n.s.).}
81:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e92fe53-bdc9-4ff9-81a3-6390b15c9967",
  "isSidechain": true,
  "promptId": "ee9bcf2f-84d2-4322-aa38-fb576f70d6d8",
  "agentId": "a92bd2628d8113da1",
  "type": "user",
  "uuid": "10d2699f-7a5d-4ff7-b2f1-b3da65fda46f",
  "sourceToolAssistantUUID": "7e92fe53-bdc9-4ff9-81a3-6390b15c9967",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T19:43:28.357Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TMq1eUiBM6tAWnGbsDBbow`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10d2699f-7a5d-4ff7-b2f1-b3da65fda46f",
  "isSidechain": true,
  "agentId": "a92bd2628d8113da1",
  "requestId": "req_011CbPrmupExiEEdrhsbCATU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a3789bd-975b-419c-978d-52aa42240778",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01BKXUJuXSVYJY62F38UEeMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 930,
      "cache_read_input_tokens": 43231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 930,
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

_source line 22 · 2026-05-25T19:43:28.374Z_

<details><summary>↩ Tool result · `toolu_01TMq1eUiBM6tAWnGbsDBbow`</summary>

```text
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a3789bd-975b-419c-978d-52aa42240778",
  "isSidechain": true,
  "promptId": "ee9bcf2f-84d2-4322-aa38-fb576f70d6d8",
  "agentId": "a92bd2628d8113da1",
  "type": "user",
  "uuid": "2426589a-ac47-4c09-9ee7-da8f9867c6f8",
  "sourceToolAssistantUUID": "2a3789bd-975b-419c-978d-52aa42240778",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T19:43:31.217Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UeDy6LYS7QgbD7wgzSmhPL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2426589a-ac47-4c09-9ee7-da8f9867c6f8",
  "isSidechain": true,
  "agentId": "a92bd2628d8113da1",
  "requestId": "req_011CbPrnM6GU4CysE5R7aAqB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89c00106-a3ed-4ee7-bf11-a1e6f0c61f50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MDFvmbD4Qt35SG8dy2Jo5q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2179,
      "cache_read_input_tokens": 44161,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2179,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
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

_source line 24 · 2026-05-25T19:43:31.283Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EuZPQdkcPjEHW5sATW2RjY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89c00106-a3ed-4ee7-bf11-a1e6f0c61f50",
  "isSidechain": true,
  "agentId": "a92bd2628d8113da1",
  "requestId": "req_011CbPrnM6GU4CysE5R7aAqB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "608be7bd-12e0-4782-8f4b-0d47971aec9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MDFvmbD4Qt35SG8dy2Jo5q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2179,
      "cache_read_input_tokens": 44161,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2179,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
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

_source line 25 · 2026-05-25T19:43:31.309Z_

<details><summary>↩ Tool result · `toolu_01EuZPQdkcPjEHW5sATW2RjY`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Judge Bias in LLM Evaluation.}
5	LLM-as-a-judge evaluations exhibit position bias \citep{wang2024positionbias}, self-preference \citep{panickssery2024selffavor}, and other cognitive biases \citep{koo2024cobbler, ye2024justice, bavaresco2025judgebench}; see also \citet{li2024splitmerge} and \citet{fiedler2026bias_uncertainty}. On the correction side, CyclicJudge \citep{cyclicjudge2026} eliminates average bias via round-robin assignment, and UDA \citep{uda2026} learns a neural K-factor reducing inter-judge deviation by 63.4\%. All of these methods model only the judge facet, absorbing contamination effects into ability estimates (Section~\ref{sec:confounding}).
6	
7	\paragraph{Benchmark Contamination Detection and Avoidance.}
8	Detection methods include performance-based tests \citep{constat2024}, unified contamination metrics \citep{dcr2025}, token-level log-probability probes \citep{logprober2024, mink2024}, and guided prompting \citep{golchin2024timetravel, oren2024proving}; see also \citet{deng2024contamination, sainz2023contamination}. \citet{preference_leakage2026} identify judge-side preference leakage, complementary to G-MFRM's examinee-side focus. Avoidance strategies include dynamic benchmarks \citep{livebench2025}, private evaluation \citep{truce2024}, and subset selection \citep{polo2024tinybenchmarks}. G-MFRM instead corrects for residual contamination while simultaneously modeling judge effects.
9	
10	\paragraph{Item Response Theory (IRT) and MFRM for LLM Evaluation.}
11	IRT has been applied to NLP leaderboards for ranking and benchmark analysis \citep{lalor2019irt, rodriguez2021irt, vania2021irt}. The Many-Facet Rasch Model (MFRM) \citep{linacre1989mfrm, linacre1994mfrm} extends IRT to multi-rater settings; \citet{jiao2025mfrm_llm} apply it to LLM judge panels, and \citet{uto2020generalized} and \citet{choi2026irt_judge} propose Bayesian variants; see also \citet{zhou2025psnirt}. The Doubly-Gated IRT (DG-IRT) model of \citet{shu2013dgirt} is the closest antecedent, introducing binary gating for item preknowledge; G-MFRM extends this to continuous exposure, multi-rater designs, and formal identifiability analysis (Section~\ref{sec:model_spec}).
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "608be7bd-12e0-4782-8f4b-0d47971aec9f",
  "isSidechain": true,
  "promptId": "ee9bcf2f-84d2-4322-aa38-fb576f70d6d8",
  "agentId": "a92bd2628d8113da1",
  "type": "user",
  "uuid": "08342e0b-a2c8-4273-852d-03067803e56f",
  "sourceToolAssistantUUID": "608be7bd-12e0-4782-8f4b-0d47971aec9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T19:43:31.530Z_

<details><summary>↩ Tool result · `toolu_01UeDy6LYS7QgbD7wgzSmhPL`</summary>

```text
1	\section{Proofs of Propositions~\ref{prop:no_new} and~\ref{prop:exposure_variation}}
2	\label{app:prop_proofs}
3	
4	\begin{proof}[Proof of Proposition~\ref{prop:no_new}]
5	Suppose $c_n' = c_n + \delta$ preserves all response probabilities. Then $\delta \cdot e_i = 0$ for all items. Since $e_i \neq 0$ for at least one item by assumption, $\delta = 0$. Fixing $e_i$ externally eliminates the bilinear ambiguity $c_n \cdot e_i = (\lambda c_n)(\lambda^{-1} e_i)$ that would otherwise render the decomposition non-unique.
6	\end{proof}
7	
8	\begin{proof}[Proof of Proposition~\ref{prop:exposure_variation}]
9	When exposure is constant, the linear predictor becomes $(\theta_n + c_n \cdot e) - b_i - d_j - \gamma_k$, equivalent to a standard MFRM with reparameterized ability $\theta^*_n = \theta_n + c_n \cdot e$. No configuration of response data can distinguish $(\theta_n, c_n)$ from $(\theta_n + \epsilon, c_n - \epsilon/e)$ for any $\epsilon$.
10	\end{proof}
11	
12	
13	\section{Proof of Theorem~\ref{thm:sufficient}}
14	\label{app:proof}
15	
16	We prove that the G-MFRM is locally identifiable under the conditions of Theorem~\ref{thm:sufficient}. Following \citet{rothenberg1971}, a parametric model is locally identifiable at the true parameter vector $\boldsymbol{\psi}_0$ if and only if the Fisher information matrix $\mathbf{F}(\boldsymbol{\psi}_0)$ is non-singular.
17	
18	\paragraph{Setup.} The G-MFRM parameter vector is $\boldsymbol{\psi} = (\boldsymbol{\theta}, \mathbf{c}, \mathbf{b}, \mathbf{d}, \boldsymbol{\gamma})$, where $\boldsymbol{\theta} \in \mathbb{R}^{N-1}$ (after the location constraint $\sum_n \theta_n = 0$), $\mathbf{c} \in \mathbb{R}_{\geq 0}^N$, $\mathbf{b} \in \mathbb{R}^I$, $\mathbf{d} \in \mathbb{R}^J$, and $\boldsymbol{\gamma} \in \mathbb{R}^{K-1}$. The exposure vector $\mathbf{e} = (e_1, \ldots, e_I)$ is fixed externally and treated as known. The linear predictor is $\eta_{nijk} = \theta_n - b_i - d_j - \gamma_k + c_n \cdot e_i$, with partial derivatives:
19	%
20	\begin{align*}
21	\frac{\partial \eta_{nijk}}{\partial \theta_n} &= 1, \quad
22	\frac{\partial \eta_{nijk}}{\partial c_n} = e_i, \quad
23	\frac{\partial \eta_{nijk}}{\partial b_i} = -1, \\
24	\frac{\partial \eta_{nijk}}{\partial d_j} &= -1, \quad
25	\frac{\partial \eta_{nijk}}{\partial \gamma_k} = -1.
26	\end{align*}
27	
28	\paragraph{Fisher information weights.} For each observation cell $(n,i,j)$, the Fisher information weight under the cumulative logit model is
29	%
30	\begin{equation}
31	\label{eq:fisher_weight}
32	w_{nij} = \sum_{k=1}^{K} \frac{\bigl[\sigma'(\eta_{nijk}) - \sigma'(\eta_{nij,k+1})\bigr]^2}{P(Y_{nij} = k)},
33	\end{equation}
34	%
35	where $\sigma(x) = (1 + e^{-x})^{-1}$, $\sigma'(x) = \sigma(x)(1 - \sigma(x))$, and we set $\sigma'(\eta_{nij,0}) = \sigma'(\eta_{nij,K+1}) = 0$ at the boundaries. Since $P(Y_{nij} = k) > 0$ for all categories and $\sigma'(\cdot) > 0$, we have $w_{nij} > 0$ for all $(n,i,j)$.
36	
37	\paragraph{Step 1: The $(\theta_n, c_n)$ submatrix.} For each model $n$, the $2 \times 2$ Fisher information submatrix is
38	%
39	\begin{equation}
40	\label{eq:fisher_block}
41	\mathbf{F}_n = \sum_{i=1}^{I} \sum_{j=1}^{J} w_{nij}
42	\begin{pmatrix} 1 & e_i \\ e_i & e_i^2 \end{pmatrix}.
43	\end{equation}
44	%
45	Its determinant is
46	%
47	\begin{multline}
48	\det \mathbf{F}_n = \Bigl(\textstyle\sum_{i,j} w_{nij}\Bigr)\Bigl(\textstyle\sum_{i,j} w_{nij}\, e_i^2\Bigr) \\
49	- \Bigl(\textstyle\sum_{i,j} w_{nij}\, e_i\Bigr)^2 = W_n^2 \cdot \mathrm{Var}_w(e_i),
50	\end{multline}
51	%
52	where $W_n = \sum_{i,j} w_{nij}$ and $\mathrm{Var}_w(e_i) = \overline{e^2}_n - \bar{e}_n^2$ is the weighted variance of exposure with weights $w_{nij}$. By the Cauchy--Schwarz inequality, $\mathrm{Var}_w(e_i) \geq 0$, with equality if and only if $e_i$ is constant across all items with $w_{nij} > 0$. Under conditions~(i) and~(iii), the observed items for model $n$ include at least two distinct exposure values with $w_{nij} > 0$ for the corresponding cells. Therefore $\mathrm{Var}_w(e_i) > 0$, $\det \mathbf{F}_n > 0$, and each $\mathbf{F}_n$ is positive definite.
53	
54	\paragraph{Step 2: Item and judge blocks.} Under the connected design (condition~i), each item $i$ is observed by at least one $(n,j)$ pair, so the item difficulty block has positive diagonal entries $[\mathbf{F}_{bb}]_{ii} = \sum_{n,j} w_{nij} > 0$ (summing over observed cells). Similarly, each judge $j$ observes at least one $(n,i)$ pair, giving $[\mathbf{F}_{dd}]_{jj} = \sum_{n,i} w_{nij} > 0$. Condition~(ii) ($J \geq 2$) ensures the judge block has sufficient dimension to separate judge effects from the intercept. Both blocks are positive definite.
55	
56	\paragraph{Step 3: Schur complement argument.} The full Fisher information matrix $\mathbf{F}$ contains off-diagonal blocks coupling the parameter groups. Partition as
57	%
58	\begin{equation*}
59	\mathbf{F} = \begin{pmatrix} \mathbf{A} & \mathbf{B} \\ \mathbf{B}^\top & \mathbf{D} \end{pmatrix},
60	\end{equation*}
61	%
62	where $\mathbf{A} = \mathrm{blockdiag}(\mathbf{F}_1, \ldots, \mathbf{F}_N)$ collects all $(\theta_n, c_n)$ submatrices and $\mathbf{D}$ collects the $(\mathbf{b}, \mathbf{d}, \boldsymbol{\gamma})$ blocks. From Step~1, $\mathbf{A}$ is positive definite. The Schur complement
63	%
64	\begin{equation}
65	\label{eq:schur}
66	\mathbf{S} = \mathbf{D} - \mathbf{B}^\top \mathbf{A}^{-1} \mathbf{B}
67	\end{equation}
68	%
69	equals the conditional Fisher information for $(\mathbf{b}, \mathbf{d}, \boldsymbol{\gamma})$ given $(\boldsymbol{\theta}, \mathbf{c})$. Conditioning on $(\boldsymbol{\theta}, \mathbf{c})$ with fixed $\mathbf{e}$ reduces the model to a standard MFRM with known offsets $c_n \cdot e_i$, whose identifiability is established by \citet[Chapter~5]{sanmartin2016} under conditions~(i), (ii), and~(iv). Therefore $\mathbf{S}$ is positive definite.
70	
71	Since both $\mathbf{A}$ and $\mathbf{S}$ are positive definite:
72	%
73	\begin{equation*}
74	\det \mathbf{F} = \det \mathbf{A} \cdot \det \mathbf{S} > 0,
75	\end{equation*}
76	%
77	establishing non-singularity of $\mathbf{F}$ and hence local identifiability. \qed
78	
79	\paragraph{Local vs.\ global identifiability.} Theorem~\ref{thm:sufficient} establishes \emph{local} identifiability: the Fisher information matrix is non-singular at the true parameter value, guaranteeing that no infinitesimally close parameter vector produces the same likelihood. This does not rule out discrete global non-identifiabilities (i.e., isolated points in parameter space with identical likelihood). However, the HalfNormal prior on $c_n$ restricts the parameter space to $c_n \geq 0$, eliminating the sign ambiguity that would otherwise create a global reflection $(\theta_n + \delta,\, c_n - \delta/e_i)$. Combined with the location constraint $\sum_n \theta_n = 0$ and the empirical observation that the posterior is unimodal across all chains (no mode-switching detected), the local result provides a practical guarantee of unique parameter recovery.
80	
81	\paragraph{Role of the Cauchy--Schwarz inequality.} The key step in Step~1 is the decomposition $\det \mathbf{F}_n = W_n^2 \cdot \mathrm{Var}_w(e_i)$, where the weighted variance $\mathrm{Var}_w(e_i) = \mathbb{E}_w[e_i^2] - (\mathbb{E}_w[e_i])^2 \geq 0$ by the Cauchy--Schwarz inequality applied to the vectors $(\sqrt{w_{nij}})$ and $(\sqrt{w_{nij}}\, e_i)$. Strict positivity follows from the requirement that $e_i$ takes at least two distinct values over observed items (condition~iii): if $e_i = e$ for all $i$ with $w_{nij} > 0$, then $\mathrm{Var}_w(e_i) = 0$ and the $(\theta_n, c_n)$ block becomes singular, recovering Proposition~\ref{prop:exposure_variation}. The Cauchy--Schwarz bound is tight only in this degenerate case, so any non-trivial exposure variation suffices for identification.
82	
83	
84	\section{Explicit Form of the OVB Coefficient $\delta_n$}
85	\label{app:gamma}
86	
87	Under the MFRM logistic link, a first-order Taylor expansion of Observation~\ref{obs:ovb} yields an explicit approximation for the bias coefficient $\delta_n$:
88	%
89	\begin{equation}
90	\label{eq:gamma_explicit}
91	\delta_n \approx \frac{\sum_{i} w_{ni} \cdot e_i \cdot p_{ni}(1 - p_{ni})}{\sum_{i} w_{ni} \cdot p_{ni}(1 - p_{ni})},
92	\end{equation}
93	%
94	where $p_{ni} = \sigma(\theta_n - b_i - \bar{d})$ is the MFRM predicted probability averaged over judges and $w_{ni}$ is the effective item weight (number of judge observations for item $i$ on model $n$). Eq.~\ref{eq:gamma_explicit} is a weighted mean of the exposure values $e_i$, with weights proportional to the Fisher information $p_{ni}(1 - p_{ni})$. Items near the boundary ($p_{ni} \approx 0.5$) contribute more to the bias than items at the extremes, because the logistic link is most sensitive at these points. This approximation is accurate to first order in $(c_n \cdot e_i)$; the synthetic validation in Section~\ref{sec:confounding} ($r = 0.86$) confirms that the linear approximation captures the dominant bias structure.
95	
96	
97	\section{Murphy--Topel Variance Correction}
98	\label{app:murphy_topel}
99	
100	The three-stage G-MFRM procedure treats Stage~2 exposure estimates $\hat{e}_i$ as fixed in Stage~3, understating posterior uncertainty by ignoring estimation error in $\hat{e}_i$. We derive the Murphy--Topel correction \citep{murphy1985} adapted to the G-MFRM setting.
101	
102	\paragraph{Setup.} Let $\boldsymbol{\alpha} = (e_1, \ldots, e_I)$ denote the Stage~2 parameters estimated from an independent dataset with log-likelihood $\ell_2(\boldsymbol{\alpha})$, and let $\boldsymbol{\psi} = (\boldsymbol{\theta}, \mathbf{c}, \mathbf{b}, \mathbf{d}, \boldsymbol{\gamma})$ denote the Stage~3 parameters estimated with log-likelihood $\ell_3(\boldsymbol{\psi}; \hat{\boldsymbol{\alpha}})$, where $\hat{\boldsymbol{\alpha}}$ is plugged in as known.
103	
104	\paragraph{Naive and Stage~2 variances.} The naive (uncorrected) variance of $\hat{\boldsymbol{\psi}}$ is
105	%
106	\begin{equation}
107	\mathbf{V}_3 = \left[-\frac{\partial^2 \ell_3}{\partial \boldsymbol{\psi}\, \partial \boldsymbol{\psi}^\top}\bigg|_{\hat{\boldsymbol{\psi}},\, \hat{\boldsymbol{\alpha}}}\right]^{-1},
108	\end{equation}
109	%
110	and the Stage~2 variance is
111	%
112	\begin{equation}
113	\mathbf{V}_2 = \left[-\frac{\partial^2 \ell_2}{\partial \boldsymbol{\alpha}\, \partial \boldsymbol{\alpha}^\top}\bigg|_{\hat{\boldsymbol{\alpha}}}\right]^{-1}.
114	\end{equation}
115	
116	\paragraph{Cross-derivative matrix.} The coupling between stages is captured by the cross-derivative
117	%
118	\begin{equation}
119	\mathbf{C} = \frac{\partial^2 \ell_3}{\partial \boldsymbol{\psi}\, \partial \boldsymbol{\alpha}^\top}\bigg|_{\hat{\boldsymbol{\psi}},\, \hat{\boldsymbol{\alpha}}}.
120	\end{equation}
121	%
122	In the G-MFRM, non-zero entries of $\mathbf{C}$ arise from the contamination gating term $c_n \cdot e_i$. The key entry is
123	%
124	\begin{equation}
125	\frac{\partial^2 \ell_3}{\partial c_n\, \partial e_i} = \sum_{j=1}^{J} \frac{\partial^2 \ell_{nij}}{\partial \eta_{nij}^2} \cdot c_n,
126	\end{equation}
127	%
128	which is proportional to $c_n$: models with zero contamination contribute no cross-derivative. Similarly, $\partial^2 \ell_3 / (\partial \theta_n\, \partial e_i)$ involves only indirect coupling through the shared item observations. The correction is therefore concentrated on the contamination parameters of models with $c_n > 0$.
129	
130	\paragraph{Corrected variance.} The Murphy--Topel corrected variance is
131	%
132	\begin{equation}
133	\label{eq:murphy_topel}
134	\mathbf{V}_{\mathrm{MT}} = \mathbf{V}_3 + \mathbf{V}_3\, \mathbf{C}\, \mathbf{V}_2\, \mathbf{C}^\top\, \mathbf{V}_3.
135	\end{equation}
136	%
137	The correction term $\mathbf{V}_3 \mathbf{C} \mathbf{V}_2 \mathbf{C}^\top \mathbf{V}_3$ is positive semi-definite, so $\mathbf{V}_{\mathrm{MT}} \succeq \mathbf{V}_3$: the corrected variance is always at least as large as the naive variance. The inflation is concentrated on $c_n$ for contaminated models and is negligible for $\theta_n$ when contamination is sparse, consistent with the empirical pattern in Table~\ref{tab:error_prop}.
138	
139	\paragraph{Implementation.} We estimate $\mathbf{V}_2$ from the Stage~2 bootstrap and compute $\mathbf{C}$ via finite differences of the Stage~3 log-likelihood evaluated at perturbed $\hat{\boldsymbol{\alpha}}$ values. Corrected credible intervals are obtained by inflating Stage~3 posterior samples by $\sqrt{\mathrm{diag}(\mathbf{V}_{\mathrm{MT}}) / \mathrm{diag}(\mathbf{V}_3)}$.
140	
141	
142	\section{Ablation Study}
143	\label{app:ablation}
144	
145	\begin{table}[h]
146	\centering
147	\scriptsize
148	\setlength{\tabcolsep}{3pt}
149	\begin{tabular}{lccc}
150	\toprule
151	\textbf{Variant} & $\theta$-RMSE & $\tau$ & $c_n$-RMSE \\
152	\midrule
153	Full G-MFRM & 0.124 $\pm$ 0.016 & 0.922 $\pm$ 0.010 & 0.593 $\pm$ 0.224 \\
154	$-$ Judge severity ($d_j$) & 0.127 $\pm$ 0.016 & 0.922 $\pm$ 0.010 & 0.629 $\pm$ 0.243 \\
155	Binary gating & 0.137 $\pm$ 0.016 & 0.909 $\pm$ 0.014 & 0.833 $\pm$ 0.226 \\
156	Staged estimation & 0.254 $\pm$ 0.045 & 0.839 $\pm$ 0.035 & 1.382 $\pm$ 0.164 \\
157	\bottomrule
158	\end{tabular}
159	\caption{Ablation study on synthetic data ($N = 50$, $I = 100$, $J = 8$, 20 seeds). Each row removes or modifies one component of the full G-MFRM. Staged estimation refers to fitting MFRM and contamination sequentially rather than jointly. All differences from Full G-MFRM are significant at $p < 0.001$ (Wilcoxon) except $-d_j$ on $\theta$-RMSE ($p = 0.245$) and $\tau$ ($p = 0.344$).}
160	\label{tab:ablation}
161	\end{table}
162	
163	The ablation confirms that joint estimation is the primary contributor to G-MFRM's advantage: staged estimation increases $\theta$-RMSE by $2.0\times$ (from 0.124 to 0.254, $p < 0.001$) and $c_n$-RMSE by $2.3\times$ (from 0.593 to 1.382, $p < 0.001$), with $\tau$ dropping from 0.922 to 0.839. This degradation directly reflects the omitted variable bias characterized in Section~\ref{sec:confounding}: when contamination and judge effects are estimated sequentially, the first-stage estimates absorb the unmodeled facet.
164	
165	Replacing continuous exposure $e_i \in [0,1]$ with binary gating ($e_i \in \{0, 1\}$) increases $c_n$-RMSE by 40\% (from 0.593 to 0.833, $p < 0.001$), indicating that graded exposure modeling captures contamination magnitude more precisely than a binary flag. The effect on $\theta$-RMSE is moderate ($+$10\%, $p < 0.001$), suggesting that the binary approximation still captures the dominant contamination signal but loses precision on partially exposed items.
166	
167	Removing judge severity $d_j$ does not significantly affect ability estimates ($\theta$-RMSE $+$2.4\%, $p = 0.245$; $\tau$ identical, $p = 0.344$) but significantly degrades contamination recovery ($c_n$-RMSE $+$6.1\%, $p < 0.001$). This confirms that $d_j$ serves as a diagnostic component that improves contamination estimation precision rather than ranking accuracy: without explicit judge severity modeling, judge-induced score variation is partially absorbed into the contamination estimates, inflating $c_n$-RMSE. The $d_j$ profile also provides independent diagnostic value for judge calibration (e.g., Claude Opus $d_j = +0.60$ vs.\ Mistral $-0.74$ in the real-data evaluation).
168	
169	\begin{figure}[h]
170	\centering
171	\includegraphics[width=\columnwidth]{theta_tau_boxplot}
172	\caption{Ranking accuracy (Kendall $\tau$ with ground truth) across ablation variants. Full G-MFRM achieves the highest and most consistent $\tau$; staged estimation shows the largest degradation and highest variance. Synthetic data: $N = 50$, $I = 100$, $J = 8$, 20 seeds.}
173	\label{fig:ablation_tau}
174	\end{figure}
175	
176	
177	\section{Posterior Predictive Check}
178	\label{app:ppc}
179	
180	Figure~\ref{fig:ppc} shows the posterior predictive distribution from 1{,}000 posterior draws over 5{,}661 observations. The predicted and observed response distributions are well-aligned (predicted mean win rate $0.593$ vs.\ observed $0.599$), with no systematic discrepancy across item difficulty or model ability levels.
181	
182	\begin{figure}[h]
183	\centering
184	\includegraphics[width=\columnwidth]{fig_ppc}
185	\caption{Posterior predictive check ($N = 8$ pilot). Distribution of predicted (gray) and observed (black) response rates across all model--item--judge triplets. Mean predicted $= 0.593$, mean observed $= 0.599$.}
186	\label{fig:ppc}
187	\end{figure}
188	
189	
190	\section{LOO Model Comparison}
191	\label{app:loo_comparison}
192	
193	Figure~\ref{fig:model_comparison} visualizes the LOO-ELPD difference between G-MFRM and MFRM-only. G-MFRM is the reference model ($\Delta\mathrm{ELPD} = 0$); MFRM-only shows a deficit of $-55.7$ (SE $= 9.4$), confirming that the contamination gating term substantially improves held-out predictive fit.
194	
195	\begin{figure}[h]
196	\centering
197	\includegraphics[width=\columnwidth]{model_comparison}
198	\caption{LOO-ELPD model comparison ($N = 8$ pilot). G-MFRM (reference) versus MFRM-only. Error bars show $\pm$1 SE. The $|\Delta/\mathrm{SE}| = 5.9$ strongly favors G-MFRM.}
199	\label{fig:model_comparison}
200	\end{figure}
201	
202	Figure~\ref{fig:pareto_k} shows the Pareto $\hat{k}$ diagnostic values for both models. All observations have $\hat{k} < 0.7$, confirming that the LOO approximation is reliable for both models.
203	
204	\begin{figure}[h]
205	\centering
206	\includegraphics[width=\columnwidth]{pareto_k_plot}
207	\caption{Pareto $\hat{k}$ diagnostics for G-MFRM (left) and MFRM-only (right), $N = 8$ pilot. All 5{,}661 observations fall below the $\hat{k} = 0.7$ threshold, confirming reliable LOO estimates.}
208	\label{fig:pareto_k}
209	\end{figure}
210	
211	
212	\section{Self-Evaluation Robustness}
213	\label{app:self_eval}
214	
215	Two models (Qwen2.5-72B and LLaMA-3.3-70B) appear as both judge and target in our evaluation. Self-judging introduces a potential confound: a model may score its own responses more favorably. We examine the empirical magnitude of this effect and its impact on rankings.
216	
217	Qwen2.5-72B achieves a perfect self-judging win rate of 1.000 (42/42 items), compared to a cross-judge mean win rate of 0.714 for the same model. LLaMA-3.3-70B shows a self-judging win rate of 0.912, compared to a cross-judge mean of 0.823. Both values are elevated relative to cross-judge baselines, consistent with same-family preference leakage \citep{preference_leakage2026}.
218	
219	To assess sensitivity, we re-fit G-MFRM excluding all 99 self-judging observations (Qwen2.5-72B and LLaMA-3.3-70B judging their own responses). The resulting ranking yields $\tau = 0.857$, identical to the full-data G-MFRM point estimate, with a swap at ranks 2--3. Contamination susceptibility estimates $c_n$ shift by less than 0.15 for all models. This confirms that $d_j$ absorbs the bulk of self-evaluation bias and that rankings are robust to excluding self-judging pairs.
220	
221	
222	\section{Judge Severity Profiles}
223	\label{app:judge_severity}
224	
225	Table~\ref{tab:judge_severity} reports posterior estimates of judge severity $d_j$ for all nine judges. Positive values indicate stricter scoring (lower win rates); negative values indicate more lenient scoring. Proprietary models cluster at the strict end, while open-source models tend to be more lenient.
226	
227	\begin{table}[h]
228	\centering
229	\small
230	\begin{tabular}{lcc}
231	\toprule
232	\textbf{Judge} & $\hat{d}_j$ & 95\% CI \\
233	\midrule
234	Claude Opus 4.7 & $+0.60$ & [$+0.43$, $+0.76$] \\
235	GPT-5.5 & $+0.53$ & [$+0.37$, $+0.70$] \\
236	DeepSeek-V4-Pro & $+0.31$ & [$+0.07$, $+0.54$] \\
237	Claude Sonnet 4.6 & $+0.14$ & [$-0.04$, $+0.31$] \\
238	Gemini-2.5-Pro & $-0.04$ & [$-0.27$, $+0.19$] \\
239	Qwen3-235B & $-0.04$ & [$-0.24$, $+0.16$] \\
240	Qwen2.5-72B & $-0.35$ & [$-0.64$, $-0.07$] \\
241	LLaMA-3.3-70B & $-0.42$ & [$-0.66$, $-0.18$] \\
242	Mistral-Large-2 & $-0.74$ & [$-1.10$, $-0.37$] \\
243	\bottomrule
244	\end{tabular}
245	\caption{Judge severity estimates ($d_j$) for all nine judges. Positive = stricter scoring. The severity range spans 1.34 logits (Claude Opus to Mistral), comparable to $\sim$1 standard deviation of model ability.}
246	\label{tab:judge_severity}
247	\end{table}
248	
249	
250	\section{Judge Count Sensitivity}
251	\label{app:judge_count}
252	
253	Table~\ref{tab:judge_count} reports ranking accuracy as a function of the number of judges $k$, obtained by subsampling from the full 9-judge panel (10 random subsets per $k$; $k = 9$ uses the full panel). G-MFRM outperforms both raw averaging and sequential estimation at all judge counts. Rank agreement increases monotonically with $k$ ($\tau = 0.771 \to 0.857$), and variance contracts as additional judges improve $d_j$ and $c_n$ estimation. At $k \geq 4$, G-MFRM exceeds the full-panel baseline $\tau = 0.786$, suggesting that four diverse judges suffice for practical deployment.
254	
255	\begin{table}[h]
256	\centering
257	\small
258	\begin{tabular}{lcccc}
259	\toprule
260	$k$ & Raw Avg & Sequential & G-MFRM & $\Delta\tau$ \\
261	\midrule
262	2 & $.755 \pm .088$ & $.764 \pm .096$ & $.771 \pm .081$ & $+.017$ \\
263	4 & $.779 \pm .041$ & $.786 \pm .048$ & $.800 \pm .045$ & $+.021$ \\
264	6 & $.800 \pm .030$ & $.807 \pm .048$ & $.821 \pm .051$ & $+.021$ \\
265	9 & $.786$ & $.786$ & $.857$ & $+.071$ \\
266	\bottomrule
267	\end{tabular}
268	\caption{Kendall $\tau$ with Chatbot Arena rankings as a function of judge count $k$. $\Delta\tau$ = G-MFRM $-$ Raw Average. Values for $k < 9$ are mean $\pm$ std over 10 random judge subsets.}
269	\label{tab:judge_count}
270	\end{table}
271	
272	Leave-one-judge-out analysis reveals that three judges (Claude Opus 4.7, $d_j = +0.60$; GPT-5.5, $+0.53$; LLaMA-3.3-70B, $-0.42$) are individually necessary for the ranking improvement: removing any one of these reduces G-MFRM $\tau$ to the baseline ($0.786$), while removing any of the other six judges preserves $\tau = 0.857$. These three judges span the severity spectrum (the two strictest and the second-most lenient), suggesting that contamination$\times$judge interaction identification requires sufficient severity diversity. This provides practical guidance: judge panels should include models with diverse scoring tendencies rather than homogeneous judges.
273	
274	G-MFRM requires $\geq 4$ MCMC chains for reliable contamination estimation; reduced chain counts attenuate $c_n$ estimates toward the prior mean, compressing inter-model differences.
275	
276	
277	\section{Stage~2 Weight Robustness}
278	\label{app:weight_robustness}
279	
280	All four weight configurations produce identical model rankings and near-perfect exposure score agreement (Spearman $\rho \geq 0.998$; Table~\ref{tab:weight_robustness}), confirming that the default 75/25 split is not a sensitive hyperparameter choice.
281	
282	\begin{table}[h]
283	\centering
284	\small
285	\begin{tabular}{lc}
286	\toprule
287	\textbf{Weight Config} & \textbf{Exposure} $\rho$ \\
288	\midrule
289	50 / 50 & 0.998 \\
290	75 / 25 (default) & 1.000 \\
291	90 / 10 & 0.999 \\
292	100 / 0 & 0.998 \\
293	\bottomrule
294	\end{tabular}
295	\caption{Stage~2 weight robustness. Weight Config denotes the percentage assigned to reference model anchoring vs.\ cross-model agreement. All configurations produce identical model rankings. Exposure $\rho$ is the Spearman correlation of per-item $e_i$ scores relative to the default 75/25 configuration.}
296	\label{tab:weight_robustness}
297	\end{table}
298	
299	
300	\section{Power Analysis}
301	\label{app:power}
302	
303	The observed effect size in the real-data evaluation is $\Delta\tau = 0.071$ (G-MFRM $\tau = 0.857$ vs.\ baseline $\tau = 0.786$). We conduct a permutation-based power analysis to determine the sample sizes required to detect this effect at $\alpha = 0.05$.
304	
305	We simulate ranking comparisons under the alternative hypothesis $H_1\!: \Delta\tau = 0.071$ by bootstrapping from the observed posterior distribution of G-MFRM ability estimates and recomputing $\tau$ against ground truth at varying model counts $N$. For each $N$, we draw 10{,}000 permutation replicates and compute the rejection rate at $\alpha = 0.05$ (two-sided).
306	
307	At $N = 8$ (our evaluation), power is approximately 50\%, explaining the non-significant bootstrap result ($\Delta\tau$ 95\% CI $[-0.071, 0.071]$). Achieving 80\% power requires $N \approx 17$ models, and 95\% power requires $N \approx 25$. These estimates inform the scope of future evaluations: detecting ranking improvements of the magnitude observed here requires at minimum doubling the number of target models.
308	
309	
310	\section{Per-Model Estimates}
311	\label{app:raw_scores}
312	
313	Table~\ref{tab:raw_scores} reports G-MFRM posterior estimates for all eight target models. All seven baselines produce identical rankings (Table~\ref{tab:main_results}), with ability scores differing by $< 0.03$ logits across methods; G-MFRM is the only method that alters the ranking, swapping gpt-4o-mini and Qwen2.5-72B at ranks 2--3.
314	
315	\begin{table}[h]
316	\centering
317	\scriptsize
318	\setlength{\tabcolsep}{3pt}
319	\resizebox{\linewidth}{!}{%
320	\begin{tabular}{lcccc}
321	\toprule
322	\textbf{Model} & $\hat{\theta}$ [95\% CI] & $\hat{c}_n$ [95\% CI] & \textbf{Base} & \textbf{G-MFRM} \\
323	\midrule
324	GPT-4o & $+2.00$ [$1.70$, $2.30$] & $0.88$ [$0.05$, $2.20$] & 1 & 1 \\
325	GPT-4o-mini & $+1.40$ [$1.10$, $1.70$] & $0.93$ [$0.06$, $2.20$] & 3 & 2 \\
326	Qwen2.5-72B & $+1.20$ [$0.85$, $1.50$] & $3.00$ [$1.40$, $4.60$] & 2 & 3 \\
327	LLaMA-3.3-70B & $+0.54$ [$0.23$, $0.85$] & $2.50$ [$1.10$, $3.90$] & 4 & 4 \\
328	Qwen3-8B & $+0.51$ [$0.22$, $0.79$] & $1.20$ [$0.14$, $2.50$] & 5 & 5 \\
329	Gemma-2-9B & $-0.50$ [$-0.79$, $-0.21$] & $1.70$ [$0.36$, $2.90$] & 6 & 6 \\
330	GPT-4-0613 & $-1.90$ [$-2.20$, $-1.60$] & $4.20$ [$3.10$, $5.30$] & 7 & 7 \\
331	GPT-3.5-Turbo & $-3.30$ [$-3.60$, $-3.00$] & $5.60$ [$4.40$, $6.80$] & 8 & 8 \\
332	\bottomrule
333	\end{tabular}}
334	\caption{G-MFRM posterior estimates for ability ($\hat{\theta}$) and contamination susceptibility ($\hat{c}_n$) with approximate 95\% credible intervals (empirical coverage ${\sim}$71\%; see Limitations). Point estimates and rank orderings are the primary results. ``Base'' and ``G-MFRM'' columns show model rankings; the only rank change is the swap at positions 2--3.}
335	\label{tab:raw_scores}
336	\end{table}
337	
338	
339	\section{Contamination Bias Absorption}
340	\label{app:bias_absorption}
341	
342	Table~\ref{tab:bias_absorption} compares per-model ability estimates from MFRM-only and G-MFRM. The difference $\Delta\theta = \hat{\theta}_{\text{MFRM}} - \hat{\theta}_{\text{G-MFRM}}$ is perfectly rank-correlated with contamination susceptibility $c_n$ (Spearman $\rho = 1.0$), providing direct empirical evidence that MFRM-only absorbs the omitted contamination term into ability estimates.
343	
344	\begin{table}[h]
345	\centering
346	\scriptsize
347	\setlength{\tabcolsep}{3pt}
348	\begin{tabular}{lcccc}
349	\toprule
350	\textbf{Model} & $\hat{\theta}_{\text{MFRM}}$ & $\hat{\theta}_{\text{G-MFRM}}$ & $\Delta\theta$ & $\hat{c}_n$ \\
351	\midrule
352	GPT-3.5-Turbo & $-2.487$ & $-3.274$ & $+0.786$ & $5.587$ \\
353	GPT-4-0613 & $-1.446$ & $-1.877$ & $+0.431$ & $4.168$ \\
354	Qwen2.5-72B & $+1.213$ & $+1.178$ & $+0.035$ & $2.961$ \\
355	LLaMA-3.3-70B & $+0.518$ & $+0.539$ & $-0.022$ & $2.478$ \\
356	Gemma-2-9B & $-0.661$ & $-0.500$ & $-0.161$ & $1.654$ \\
357	Qwen3-8B & $+0.208$ & $+0.513$ & $-0.305$ & $1.178$ \\
358	GPT-4o-mini & $+1.064$ & $+1.432$ & $-0.368$ & $0.934$ \\
359	GPT-4o & $+1.591$ & $+1.988$ & $-0.397$ & $0.880$ \\
360	\bottomrule
361	\end{tabular}
362	\caption{Contamination bias absorption in MFRM-only estimation. $\Delta\theta = \hat{\theta}_{\text{MFRM}} - \hat{\theta}_{\text{G-MFRM}}$. Models with high contamination susceptibility ($c_n$) have inflated ability estimates under MFRM-only; models with low $c_n$ are relatively deflated. The perfect rank correlation (Spearman $\rho = 1.0$) between $\Delta\theta$ and $c_n$ empirically confirms the omitted variable bias predicted in Section~\ref{sec:confounding}.}
363	\label{tab:bias_absorption}
364	\end{table}
365	
366	
367	\section{Synthetic Calibration at Matched Scale}
368	\label{app:synthetic_calibration}
369	
370	We generate synthetic data at matched scale ($N = 8$ models, $I = 176$ items, $J = 9$ judges) with known ground-truth parameters across 20 random seeds. Joint G-MFRM consistently outperforms sequential estimation: $\theta$-RMSE is halved ($0.083$ vs.\ $0.166$), and ranking agreement improves by 7.2 percentage points (mean $\tau = 0.954$ vs.\ $0.882$). Across 20 seeds, joint estimation improves or matches sequential in all cases (10 wins, 0 losses, 10 ties; Wilcoxon signed-rank $p < 0.002$). The synthetic effect size ($\Delta\tau = +0.072$) closely matches the observed real-data effect ($\Delta\tau = +0.071$). All 40 MCMC fits converge ($\hat{R} = 1.0$, ESS $\geq 1{,}678$).
371	
372	\begin{table}[h]
373	\centering
374	\small
375	\begin{tabular}{lccc}
376	\toprule
377	\textbf{Metric} & \textbf{Sequential} & \textbf{Joint G-MFRM} & \textbf{Improv.} \\
378	\midrule
379	$\theta$ RMSE & $0.166 \pm 0.050$ & $0.083 \pm 0.024$ & $-50.3\%$ \\
380	$\theta$ $\tau$ & $0.882 \pm 0.112$ & $0.954 \pm 0.048$ & $+7.2$pp \\
381	$c_n$ RMSE & $1.399 \pm 0.358$ & $0.552 \pm 0.328$ & $-60.5\%$ \\
382	$c_n$ Pearson & $0.850 \pm 0.141$ & $0.866 \pm 0.151$ & $+1.9$\% \\
383	\bottomrule
384	\end{tabular}
385	\caption{Synthetic calibration at $N = 8$ ($I = 176$, $J = 9$, 20 seeds). Joint G-MFRM halves $\theta$-RMSE and reduces $c_n$-RMSE by 61\% relative to sequential estimation.}
386	\label{tab:synthetic_calibration}
387	\end{table}
388	
389	At $N = 20$ (20 seeds), the ranking improvement becomes individually significant: joint G-MFRM achieves $\Delta\tau = +0.052$ over sequential estimation (Wilcoxon $p = 1.81 \times 10^{-4}$, 18 wins / 1 loss / 1 tie), directly validating the power analysis prediction that $N \approx 17$ suffices for 80\% power. The effect size is stable across scales ($\Delta\tau = +0.072$ at $N = 8$, $+0.052$ at $N = 20$).
390	
391	\begin{table}[h]
392	\centering
393	\small
394	\begin{tabular}{lccc}
395	\toprule
396	\textbf{Metric} & \textbf{Sequential} & \textbf{Joint G-MFRM} & \textbf{Improv.} \\
397	\midrule
398	$\theta$ RMSE & $0.171 \pm 0.049$ & $0.094 \pm 0.019$ & $-45.2\%$ \\
399	$\theta$ $\tau$ & $0.891 \pm 0.038$ & $0.943 \pm 0.036$ & $+5.2$pp \\
400	$c_n$ RMSE & $1.375 \pm 0.278$ & $0.626 \pm 0.263$ & $-54.5\%$ \\
401	$c_n$ Pearson & $0.817 \pm 0.096$ & $0.842 \pm 0.106$ & $+2.5\%$ \\
402	\bottomrule
403	\end{tabular}
404	\caption{Synthetic calibration at $N = 20$ ($I = 176$, $J = 9$, 20 seeds). Ranking improvement is individually significant (Wilcoxon $p = 1.81 \times 10^{-4}$), validating the power analysis prediction.}
405	\label{tab:synthetic_calibration_n20}
406	\end{table}
407	
408	
409	\section{Prior Specification Robustness}
410	\label{app:prior_robustness}
411	
412	We compare posterior estimates under two contamination priors: Horseshoe \citep{piironen2017horseshoe} and hierarchical HalfNormal (Eq.~\ref{eq:contam_prior}). Table~\ref{tab:prior_robustness} reports $\hat{c}_n$ and $\hat{\theta}$ posterior means for all eight target models under both specifications.
413	
414	\begin{table}[h]
415	\centering
416	\small
417	\begin{tabular}{lcccc}
418	\toprule
419	\textbf{Model} & $\hat{c}_n$ (HS) & $\hat{c}_n$ (HN) & $\hat{\theta}$ (HS) & $\hat{\theta}$ (HN) \\
420	\midrule
421	Gemma-2-9B & 1.61 & 1.65 & $-0.49$ & $-0.50$ \\
422	GPT-3.5-Turbo & 5.69 & 5.57 & $-3.30$ & $-3.27$ \\
423	GPT-4-0613 & 4.25 & 4.15 & $-1.89$ & $-1.88$ \\
424	GPT-4o & 0.79 & 0.88 & $+2.01$ & $+1.99$ \\
425	GPT-4o-mini & 0.84 & 0.92 & $+1.45$ & $+1.43$ \\
426	LLaMA-3.3-70B & 2.50 & 2.46 & $+0.53$ & $+0.54$ \\
427	Qwen2.5-72B & 3.02 & 2.94 & $+1.17$ & $+1.18$ \\
428	Qwen3-8B & 1.11 & 1.15 & $+0.53$ & $+0.52$ \\
429	\bottomrule
430	\end{tabular}
431	\caption{Posterior estimates under Horseshoe (HS) and HalfNormal (HN) contamination priors. Both priors produce virtually identical estimates: Pearson $r = 1.000$ for $\hat{\theta}$ and $r = 0.9999$ for $\hat{c}_n$.}
432	\label{tab:prior_robustness}
433	\end{table}
434	
435	Posterior estimates are virtually identical across the two prior specifications (Pearson $r = 1.000$ for $\hat{\theta}$, $r > 0.999$ for $\hat{c}_n$), indicating that results are not sensitive to the choice of contamination prior.
436	
437	
438	\section{Item-Level Fit Diagnostics}
439	\label{app:item_diagnostics}
440	
441	We report item-level infit and outfit MNSQ statistics for all 176 items. Items with MNSQ outside $[0.5, 1.5]$ are flagged as potentially misfitting.
442	
443	\begin{table}[h]
444	\centering
445	\small
446	\begin{tabular}{lccccc}
447	\toprule
448	\textbf{Statistic} & \textbf{Mean} & \textbf{SD} & \textbf{Median} & \textbf{Min} & \textbf{Max} \\
449	\midrule
450	Infit MNSQ & 0.78 & 0.41 & 0.76 & 0.05 & 1.95 \\
451	Outfit MNSQ & 0.73 & 0.57 & 0.58 & 0.04 & 3.17 \\
452	\bottomrule
453	\end{tabular}
454	\caption{Item-level fit statistics across 176 items.}
455	\label{tab:item_fit_summary}
456	\end{table}
457	
458	Of the 176 items, 92 are flagged: 18 overfit (MNSQ $> 1.5$) and 74 underfit (MNSQ $< 0.5$). The majority of flagged items are underfit, reflecting sparse low-observation items where the model's predicted variance exceeds the observed variance, a consequence of limited data per item rather than a structural model deficiency. The 18 overfit items exhibit more erratic response patterns than the model predicts. No model-level or judge-level facets are flagged (all MNSQ within $[0.63, 1.07]$), confirming that the G-MFRM captures the systematic structure in model ability, judge severity, and contamination.
459	
460	
461	\section{CI Coverage Analysis}
462	\label{app:ci_coverage}
463	
464	We assess empirical coverage of 95\% posterior credible intervals across synthetic replications. At $N=8$ (49 seeds), ability parameter $\theta$ achieves 90.1\% coverage, approaching the nominal level, while contamination susceptibility $c_n$ achieves only 67.9\%. At $N=50$ (50 seeds), $c_n$ coverage improves to 71\%. The coverage gap between $\theta$ and $c_n$ reflects the multiplicative coupling $c_n \cdot e_i$: contamination parameters enter the likelihood through an interaction term, making posterior inference more sensitive to exposure estimation noise and the HalfNormal prior's boundary constraint at $c_n = 0$. These results support treating $c_n$ point estimates and rank orderings as reliable diagnostics, while noting that $c_n$ credible intervals are systematically too narrow.
465	
466	\section{Bias vs.\ Confounding Level}
467	\label{app:bias_vs_rho}
468	
469	See Figure~\ref{fig:bias_vs_rho} in the main text.
470	
471	
472	\section{Error Propagation Details}
473	\label{app:error_prop}
474	
475	\begin{table}[h]
476	\centering
477	\small
478	\begin{tabular}{lcccc}
479	\toprule
480	$\sigma$ & $\theta$-RMSE & $\Delta\theta$\% & $c_n$-RMSE & $\Delta c_n$\% \\
481	\midrule
482	0.0 & 0.128 $\pm$ 0.018 & --- & 0.533 $\pm$ 0.187 & --- \\
483	0.1 & 0.130 $\pm$ 0.018 & +1.4 & 0.545 $\pm$ 0.192 & +2.3 \\
484	0.2 & 0.135 $\pm$ 0.018 & +5.9 & 0.575 $\pm$ 0.198 & +7.9 \\
485	0.5 & 0.175 $\pm$ 0.027 & +36.9 & 0.842 $\pm$ 0.281 & +57.9 \\
486	\bottomrule
487	\end{tabular}
488	\caption{Error propagation robustness. Ability RMSE degrades by less than 6\% when exposure noise $\sigma \leq 0.2$, matching the theoretical prediction. Contamination estimates are more sensitive due to multiplicative coupling with $e_i$.}
489	\label{tab:error_prop}
490	\end{table}
491	
492	\begin{figure}[h]
493	\centering
494	\includegraphics[width=\columnwidth]{fig3_error_propagation}
495	\caption{Error propagation from Stage~2 exposure noise to Stage~3 parameter estimates. Ability RMSE ($\theta$, left) and contamination RMSE ($c_n$, right) as a function of exposure noise $\sigma_e$. The dashed line marks $\sigma_{\mathrm{crit}} \approx 0.2$, below which degradation remains mild ($\theta$-RMSE $+$5.9\%, $c_n$-RMSE $+$7.9\%). Error bars: $\pm$1 std over 20 seeds.}
496	\label{fig:error_prop_app}
497	\end{figure}
498	
499	
500	\section{Contamination Recovery}
501	\label{app:cn_recovery}
502	
503	\begin{figure}[h]
504	\centering
505	\includegraphics[width=\columnwidth]{fig5_cn_recovery}
506	\caption{Contamination susceptibility recovery ($c_n$: true vs.\ estimated) from 50 Monte Carlo seeds. Empirical CI coverage is 71\% (below nominal 95\%), indicating moderate posterior overconfidence (see Limitations).}
507	\label{fig:cn_recovery_app}
508	\end{figure}
509	
510	
511	\section{Compute Resources}
512	\label{app:compute}
513	
514	All MCMC inference was performed using NumPyro NUTS on a single GPU (NVIDIA RTX 6000 Ada). The $N = 8$ configuration (4 chains $\times$ 10{,}000 iterations) completed in approximately 10 minutes; the $N = 17$ configuration in approximately 45 minutes. Total GPU usage for all experiments was under 5 GPU-hours.
515	
516	
517	\section{Use of AI Assistants}
518	\label{app:ai_assistants}
519	
520	We used Claude (Anthropic) as an AI coding and writing assistant
521	throughout this work. Specifically:
522	\begin{itemize}
523	    \item \textbf{Code:} drafting experiment scripts, data-processing
524	    pipelines, and analysis utilities; debugging and refactoring.
525	    \item \textbf{Writing:} drafting and revising paper sections,
526	    polishing prose, and reformatting LaTeX.
527	    \item \textbf{Literature:} summarizing related papers to inform
528	    the related-work section.
529	\end{itemize}
530	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89c00106-a3ed-4ee7-bf11-a1e6f0c61f50",
  "isSidechain": true,
  "promptId": "ee9bcf2f-84d2-4322-aa38-fb576f70d6d8",
  "agentId": "a92bd2628d8113da1",
  "type": "user",
  "uuid": "fefd9b7f-4b19-4344-b946-1bbd7c2d731c",
  "sourceToolAssistantUUID": "89c00106-a3ed-4ee7-bf11-a1e6f0c61f50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-25T19:47:20.740Z_

Now I have all the data I need. Let me compile the complete audit table with precise line-by-line analysis.

---

## Complete Data Integrity Audit

### FILE: abstract.tex

| # | Number | Location | Claim | Source Exp | Registry Value | Status | Notes |
|---|--------|----------|-------|-----------|----------------|--------|-------|
| A1 | N=50 | abstract.tex:2 | Synthetic experiment size | exp-w7-ablation / mvp_003 | N=50, 20 seeds | **OK** | |
| A2 | 51% | abstract.tex:2 | RMSE reduction over sequential pipelines | Claimed from mvp_003 / exp-015 / exp-018 | mvp_003: 43.8%, exp-015: 50.3%, exp-018: 45.2% | **MISMATCH** | No experiment yields 51% RMSE reduction. The closest is exp-015 (N=8 scale, 50.3%), but the abstract does not specify N=8 scale. The primary synthetic experiment (N=50, exp-w7-ablation) gives (0.2539−0.1243)/0.2539 = **51.0%** exactly. This is correct when computed from the ablation table: (0.254−0.124)/0.254 = 51.2%. **Actually OK** — computed from exp-w7-ablation staged (0.2539) vs full (0.1243): reduction = (0.2539−0.1243)/0.2539 = 51.0%. |
| A3 | p < 0.001 | abstract.tex:2 | Significance of RMSE reduction | exp-w7-ablation | Wilcoxon p=1.91e-6 (full_vs_staged θ) | **OK** | p < 0.001 is a correct characterization of 1.91e-6 |
| A4 | r=0.81 | abstract.tex:2 | Pearson r for contamination susceptibility recovery | exp-009 Part B | correlation=0.8114 | **OK** | Rounded to 0.81 |
| A5 | 8-model pilot | abstract.tex:2 | Number of models in pilot | exp-003b | n_models=8 | **OK** | |
| A6 | 4–6× | abstract.tex:2 | Higher susceptibility of older models | exp-003b | GPT-3.5 c_n=5.587, GPT-4o c_n=0.880; ratio=6.35×; GPT-4-0613/GPT-4o=4.74× | **OK** | Range "4–6×" covers the two ratio bounds (4.74× and 6.35×). Acceptable approximation. |
| A7 | Δτ = −0.044 | abstract.tex:2 | Over-correction at 46% coverage | exp-020 | Δτ=−0.044 | **OK** | |
| A8 | Δτ = 0 | abstract.tex:2 | Over-correction at full coverage | exp-020 v7 | Δτ=0.000 | **OK** | |
| A9 | \|ΔELPD/SE\| = 5.9 | abstract.tex:2 | LOO cross-validation ratio | LOO result | ΔELPD=−55.7, SE=9.4 → 55.7/9.4=5.93 | **OK** | Rounds to 5.9 |

---

### FILE: introduction.tex

| # | Number | Location | Claim | Source Exp | Registry Value | Status | Notes |
|---|--------|----------|-------|-----------|----------------|--------|-------|
| I1 | N=50 models, 20 seeds | intro:17 | Synthetic experiment parameters | exp-w7-ablation | N=50, 20 seeds | **OK** | |
| I2 | 51% | intro:17 | RMSE reduction over sequential | exp-w7-ablation | (0.2539−0.1243)/0.2539 = 51.0% | **OK** | |
| I3 | p < 0.001 | intro:17 | Significance of RMSE reduction | exp-w7-ablation | p=1.91e-6 | **OK** | |
| I4 | r=0.81 | intro:17 | Pearson r for c_n recovery | exp-009 Part B | 0.8114 | **OK** | |
| I5 | 8-model pilot | intro:17 | Pilot size | exp-003b | n_models=8 | **OK** | |
| I6 | GPT-3.5-Turbo and GPT-4-0613 exhibit 4–6× higher susceptibility than recent models such as GPT-4o | intro:17 | Contamination ratio claim | exp-003b | GPT-3.5: 5.587, GPT-4-0613: 4.168, GPT-4o: 0.880. Ratios: 5.587/0.880=6.35×; 4.168/0.880=4.74× | **OK** | "4–6×" correctly brackets both ratios |
| I7 | 17 models and 6 judges | intro:17 | N=17 configuration | exp-020 | n_models=17, n_judges=6 | **OK** | |
| I8 | Δτ: −0.044 → −0.015 → 0.000 | intro:17 | Coverage ablation progression | exp-020 | Full: −0.044, filtered v3: −0.015, v4 MFRM-only or v7 exposed-only: 0.000 | **OK** | |
| I9 | coverage from 46% to 100% | intro:17 | Coverage range | exp-020 | Full set 46% coverage, exposed-only 100% | **OK** | |
| I10 | \|ΔELPD/SE\| = 5.9 | intro:17 | LOO ratio | LOO (attributed to exp-003b) | 55.7/9.4=5.93 | **OK** | |
| I11 | stacking weight 1.0 | intro:17 | Stacking weight | LOO comparison | Stated in paper as 1.0 | **UNVERIFIED** | Not in provided registry values; stated in experiments section and repeated here |

---

### FILE: background.tex

| # | Number | Location | Claim | Source Exp | Registry Value | Status | Notes |
|---|--------|----------|-------|-----------|----------------|--------|-------|
| B1 | r=0.86 (p < 0.001) | background:7 (figure caption) | Pearson r of sequential bias vs c_n; validation of OVB direction | exp-009 (OVB simulation) | Registry states sequential bias slope ~0.19, but no r=0.86 value provided | **UNVERIFIED** | The provided registry for exp-009 gives bias slope and coverage/RMSE/correlation values, but r=0.86 specifically refers to a different metric — correlation between predicted OVB direction and empirical bias. No registry entry with this value. Needs artifact verification. |
| B2 | N=50, I=100, J=8 | background:7 (figure caption) | Synthetic data parameters for OVB figure | exp-009 | exp-009 spec: N=50, 50 seeds. I=100, J=8 not confirmed in registry summary | **UNVERIFIED** | Registry states N=50, 50 seeds for exp-009; I=100 and J=8 are standard DGP parameters consistent with ablation but not explicitly confirmed for exp-009 in the provided ground truth. |
| B3 | r=0.86 (p < 0.001) | background:34 (footnote) | Pearson r confirming OVB approximation quality | exp-009 | See B1 | **UNVERIFIED** | Same value appears twice; unverified against registry. |
| B4 | ~69% | background:42 | Joint estimation reduces bias slope | exp-009 | bias slope reduction: 0.06/0.19 = 31.6% residual → 68.4% reduction ≈ 69% | **OK** | 1 − (0.06/0.19) = 68.4% ≈ 69%. Correct. |
| B5 | N=50, I=100, J=8 | background:47 (figure caption) | Synthetic data for bias_vs_rho figure | exp-009 | N=50, 50 seeds confirmed; I=100, J=8 unconfirmed in registry | **UNVERIFIED** | Same caveat as B2. |
| B6 | ~69% (bias slope reduction) | background:47 (figure caption) | Second mention in figure caption | exp-009 | Same as B4 | **OK** | |

---

### FILE: method.tex

| # | Number | Location | Claim | Source Exp | Registry Value | Status | Notes |
|---|--------|----------|-------|-----------|----------------|--------|-------|
| M1 | 75% weight (reference anchoring), 25% (cross-model agreement) | method:29 | Exposure pipeline weights | exp-013 (weight sensitivity) | All weight configs give identical τ=0.7857 | **OK** | |
| M2 | ρ=0.998 (100% anchoring ablation) | method:29 | Weight robustness | exp-013 | Spearman ρ ≥ 0.992, min 0.9978 | **MISMATCH** | Registry says min ρ=0.9978 (rounds to 0.998 for the 100/0 config in appendix Table). Paper says "100% anchoring yields ρ=0.998" — appendix table shows 100/0 → 0.998. **OK** (registry min is 0.9978, the 100/0 config specifically is 0.998 as shown in appendix Table app:weight_robustness) |
| M3 | σ≈0.2 (50% attenuation) | method:78 | Attenuation threshold | exp-012 | σ=0.2 threshold given | **OK** | |
| M4 | Var(e_i) ≈ 0.04 | method:78 | Variance of exposure | exp-012 | Not in provided registry | **UNVERIFIED** | |
| M5 | θ-RMSE increases by only 5.9% | method:78 | Error propagation below σ=0.2 | exp-012 | σ=0.2: θ-RMSE +5.9% | **OK** | |
| M6 | c_n-RMSE by 7.9% | method:78 | Error propagation below σ=0.2 | exp-012 | σ=0.2: c_n RMSE +7.9% | **OK** | |
| M7 | N=50, I=100, J=8 | method:41 (footnote) | Synthetic validation parameters | exp-w7-ablation | N=50, 20 seeds; I=100, J=8 consistent with ablation DGP | **OK** | |
| M8 | severity range spans 1.34 logits | method:47 (fig caption) | Judge severity range | exp-003b | d_j: Claude-Opus=0.60, Mistral=-0.74; range=0.60−(−0.74)=1.34 | **OK** | |
| M9 | J≥2 judges | method:70 | Identifiability condition | Theory | Theoretical condition | N/A | |

---

### FILE: experiments.tex

| # | Number | Location | Claim | Source Exp | Registry Value | Status | Notes |
|---|--------|----------|-------|-----------|----------------|--------|-------|
| E1 | N=17 target models, 6 LLM judges | exp:14 | Main experiment setup | exp-020 | n_models=17, n_judges=6 | **OK** | |
| E2 | N=8 pilot, 9 judges | exp:14 | Pilot setup | exp-003b | n_models=8, n_judges=9 | **OK** | |
| E3 | 500 multi-turn conversational items | exp:16 | Arena-Hard benchmark size | exp-020 | n_items=500 (full set) | **OK** | |
| E4 | ~58% fill rate | exp:16 | Fill rate of N×I×J tensor | exp-003b / exp-020 | exp-003b: n_observations=5661; 8×176×9=12672; 5661/12672=44.7%. For exp-020: N=17, I=500, J=6 → full tensor=51000; fill rate=~58% would imply ~29,580 obs | **UNVERIFIED** | Fill rate ~58% stated for the N=17/500-item design. Registry doesn't give n_observations for exp-020 directly. The 58% figure cannot be confirmed from provided registry values. |
| E5 | 63–79% of items (Gemini, Sonnet) | exp:18 | Coverage of two partial judges | exp-020 | Not in provided registry values | **UNVERIFIED** | |
| E6 | 75% reference anchoring, 25% cross-model agreement | exp:20 | Exposure pipeline weights | exp-013 | Confirmed robust | **OK** | |
| E7 | ρ≥0.998 (weight robustness) | exp:20 | Spearman ρ for weight configs | exp-013 | min ρ=0.9978; registry says "≥0.992 (min 0.9978)" | **MISMATCH (minor)** | Paper says ρ≥0.998, registry ground truth says min=0.9978 (rounds to 0.998). The appendix Table shows 50/50→0.998, 100/0→0.998. So ρ≥0.998 is consistent with all configs being ≥0.998. But registry separately states "min 0.9978" which rounds to 0.998. **OK** effectively. |
| E8 | 6,000 warmup + 4,000 samples × 4 chains | exp:22 | MCMC configuration | exp-020/003b | Not in provided registry summary | **UNVERIFIED** | Consistent with standard practice but not in provided ground truth. |
| E9 | target acceptance 0.95 | exp:22 | MCMC acceptance | — | Not in provided registry | **UNVERIFIED** | |
| E10 | R̂ < 1.05, ESS > 100 | exp:22 | Convergence thresholds | Standard (Vehtari 2021) | Thresholds are methodological standards | **OK** | |
| E11 | 500 items, 46% coverage | exp:36, table | Full set, N=17 | exp-020 | τ_raw=0.838, τ_gmfrm=0.794, Δτ=−0.044 | **OK** | |
| E12 | 317 items, 73% coverage | exp:37, table | Filtered set, N=17 | exp-020 v3 | filtered 317 items: τ=0.809, raw=0.824, Δτ=−0.015; coverage 73% | **OK** | exp-020 v3 R̂=1.009, ESS=1677 |
| E13 | 231 items, 100% coverage | exp:38, table | Exposed-only, N=17 | exp-020 v7 | 231 items, τ=0.779, raw=0.779, Δτ=0.000 | **OK** | |
| E14 | N=8 pilot, 176 items, τ_raw=0.786, τ_gmfrm=0.857, Δτ=+0.071 | exp:41, table | Pilot results | exp-003b | τ=0.857 (joint), τ=0.786 (raw), confirmed | **OK** | |
| E15 | Seven baselines, τ within 0.014 of raw average | exp:44 (table caption) | Baseline spread | exp-004 | N=8: all baselines τ=0.8095 (raw=0.786, diff=0.0235 for N=8); N=17: baselines within 0.0147 of raw | **MISMATCH (minor)** | For N=8: raw=0.786, all baselines=0.8095, diff=0.0235 > 0.014. For N=17: raw=0.838, CyclicJudge=0.838 (0.000), DCR=0.823 (0.015), CyclicJudge_discard=0.823 (0.015) — so "within 0.014" is off by 0.001. The caption says "within 0.014 of the raw average at **both** panel sizes" which appears false for N=8 (diff=0.023). **MISMATCH**: at N=8, baselines differ by 0.023 from raw, not within 0.014. |
| E16 | N=50, 20 seeds (synthetic validation) | exp:50 | Synthetic parameters | exp-w7-ablation | N=50, 20 seeds | **OK** | |
| E17 | 51% RMSE reduction | exp:50 | RMSE reduction, sequential vs joint | exp-w7-ablation | (0.2539−0.1243)/0.2539 = 51.0% | **OK** | |
| E18 | p < 10^{−6} | exp:50 | Significance of RMSE reduction | exp-w7-ablation | Wilcoxon p=1.91e-6 | **OK** | 1.91e-6 < 10^{-6}? **MISMATCH**: 1.91e-6 > 1e-6. Paper claims p < 10^{-6} but registry gives p=1.91×10^{-6}. The correct statement would be p < 10^{-5} or p=1.91×10^{-6}. **MISMATCH** |
| E19 | τ: 0.922 vs 0.839 | exp:50 | Ranking accuracy comparison | exp-w7-ablation | joint τ=0.9224, staged τ=0.8393 | **OK** | Paper rounds 0.9224→0.922, 0.8393→0.839. OK. |
| E20 | Wilcoxon p < 0.001 | exp:50 | Significance of τ improvement | exp-w7-ablation | Wilcoxon p for full_vs_staged: p=1.91e-6 (θ); the τ Wilcoxon p not separately listed in registry but p for θ RMSE is 1.91e-6 | **OK** | p < 0.001 is conservatively correct for p=1.91e-6 |
| E21 | Pearson r=0.81 | exp:50 | c_n recovery | exp-009 Part B | correlation=0.8114 | **OK** | |
| E22 | ΔELPD_LOO = −55.7, SE=9.4, \|Δ/SE\|=5.9 | exp:52 | LOO predictive fit | LOO (N=8 pilot) | ΔELPD=−55.7, SE=9.4, ratio=5.93 | **OK** | Stated as from N=8 pilot. Registry says to verify source artifact but values are provided in ground truth. |
| E23 | stacking weight 1.0, Pareto k̂ < 0.7 | exp:52 | LOO diagnostics | LOO | Not in registry summary | **UNVERIFIED** | |
| E24 | Δτ=−0.044 (46% coverage) | exp:59 | Coverage ablation bullet | exp-020 | Δτ=−0.044 | **OK** | |
| E25 | Δτ=−0.015 (73% coverage) | exp:60 | Coverage ablation bullet | exp-020 v3 | Δτ=−0.015 | **OK** | |
| E26 | Δτ=0.000 (100% coverage) | exp:61 | Coverage ablation bullet | exp-020 v7 | Δτ=0.000 | **OK** | |
| E27 | contamination-only variant Δτ=−0.118 | exp:64 | Contamination-only naive correction | exp-020 v5 | τ=0.706, Δτ=−0.118 (raw=0.824, gmfrm=0.706) | **OK** | |
| E28 | MFRM-only filtered set Δτ=0.000 | exp:64 | MFRM-only on filtered items | exp-020 v4 | v4 (MFRM-only): τ=0.824, Δτ=0.000 | **OK** | |
| E29 | GPT-3.5-Turbo: ĉ_n=5.60 | exp:66 | Contamination susceptibility (pilot) | exp-003b | c_n=5.587 → rounds to 5.59, not 5.60 | **MISMATCH** | 5.587 rounds to 5.59 at 2 decimal places. Paper reports 5.60. Discrepancy of 0.01. |
| E30 | GPT-4-0613: ĉ_n=4.20 | exp:66 | Contamination susceptibility (pilot) | exp-003b | c_n=4.168 → rounds to 4.17, not 4.20 | **MISMATCH** | 4.168 rounds to 4.17. Paper reports 4.20. Discrepancy of 0.03. |
| E31 | GPT-4o: ĉ_n=0.88 | exp:66 | Contamination susceptibility (pilot) | exp-003b | c_n=0.880 | **OK** | |
| E32 | GPT-4o-mini: ĉ_n=0.93 | exp:66 | Contamination susceptibility (pilot) | exp-003b | c_n=0.934 → rounds to 0.93 | **OK** | |
| E33 | ĉ_n > 4 for older models | exp:66 | Threshold claim | exp-003b | GPT-3.5: 5.587>4 ✓, GPT-4-0613: 4.168>4 ✓ | **OK** | |
| E34 | Δθ up to 0.79 logits (bias inflation) | exp:66 | Max bias absorption | exp-019 | GPT-3.5 Δθ=+0.786 → rounds to 0.79 | **OK** | |
| E35 | Spearman ρ=1.0 between ĉ_n and Δθ | exp:66 | Rank correlation | exp-019 | ρ=1.0 | **OK** | |
| E36 | R̂ ≤ 1.003, ESS ≥ 1,240 (N=8 pilot) | exp:66 | Convergence diagnostics | exp-020 | R̂ max=1.0023, ESS min=1240 | **MISMATCH (minor)** | Paper attributes R̂≤1.003 and ESS≥1,240 to "N=8 pilot" but the registry values R̂=1.0023 and ESS=1240 are from **exp-020 (N=17)**. The registry states: "R̂ max: 1.03, ESS min: 174 (but paper may cite 1.003 and 1240 from exp-020)." For exp-003b: R̂ max=1.03, ESS min=174. **MISMATCH**: These convergence diagnostics belong to exp-020 (N=17), not the N=8 pilot. |
| E37 | GPT-3.5-Turbo: 2.57 (N=17 analysis) | exp:66 | c_n at N=17 scale | exp-020 | Not in provided registry for exp-020 c_n values | **UNVERIFIED** | |
| E38 | GPT-4-0613: 3.78 (N=17 analysis) | exp:66 | c_n at N=17 scale | exp-020 | Not in provided registry for exp-020 c_n values | **UNVERIFIED** | |
| E39 | k≥4 judges for reliable diagnostics | exp:68 | Judge count recommendation | exp-006 | k=4: τ=0.800±0.045, exceeds raw baseline 0.786 | **OK** | |
| E40 | N=50, 20 seeds (ablation section) | exp:77 (fig caption) | Ablation parameters | exp-w7-ablation | N=50, 20 seeds | **OK** | |
| E41 | staged estimation doubles θ-RMSE | exp:77 (fig caption) and exp:81 | Ablation finding | exp-w7-ablation | Full: 0.1243, staged: 0.2539; ratio=2.04× | **OK** | |
| E42 | p < 0.001 (staged vs full) | exp:77 (fig caption) | Significance | exp-w7-ablation | p=1.91e-6 | **OK** | |
| E43 | continuous vs binary c_n-RMSE −40% | exp:81 | Gating ablation | exp-w7-ablation | binary: 0.8326, full: 0.5933; reduction=(0.8326−0.5933)/0.8326=28.7% — **OR** (0.8326−0.5933)/0.5933=40.3% increase in binary direction | **MISMATCH** | Paper says "c_n-RMSE −40% (from 0.593 to 0.833)". This is actually a +40% **increase** going from full to binary (0.5933→0.8326 = +40.3%). The paper states it correctly as "continuous gating over binary (c_n-RMSE −40%)" meaning binary is 40% worse than continuous — this is correct in framing: binary has 40% higher c_n-RMSE. **OK** — the 40% is computed as (0.8326−0.5933)/0.5933 = +40.3%, so saying binary is "40% worse" is correct. |
| E44 | 5.9% (θ-RMSE) and 7.9% (c_n-RMSE) below σ=0.2 | exp:81 | Error propagation table reference | exp-012 | σ=0.2: θ-RMSE +5.9%, c_n-RMSE +7.9% | **OK** | |
| E45 | 2.0× θ-RMSE increase under staged estimation | exp:81 | Ablation result | exp-w7-ablation | 0.2539/0.1243=2.04× | **OK** | |

---

### FILE: conclusion.tex

| # | Number | Location | Claim | Source Exp | Registry Value | Status | Notes |
|---|--------|----------|-------|-----------|----------------|--------|-------|
| C1 | 4–6× higher susceptibility | conc:6 | Contamination ratio | exp-003b | GPT-3.5: 5.587/0.880=6.35×; GPT-4-0613: 4.168/0.880=4.74× | **OK** | |
| C2 | up to 0.79 logits | conc:6 | Max bias inflation | exp-019 | GPT-3.5 Δθ=+0.786 | **OK** | Rounds to 0.79 |
| C3 | Δτ: −0.044 → −0.015 → 0.000 as coverage increases to 100% | conc:6 | Coverage ablation summary | exp-020 | Confirmed | **OK** | |
| C4 | staged estimation doubles ability RMSE | conc:6 | Ablation finding | exp-w7-ablation | 0.2539/0.1243=2.04× | **OK** | |
| C5 | 71% coverage at nominal 95% | conc:9 | CI coverage for c_n | exp-009 / CI analysis | exp-009: coverage=0.71 | **OK** | |

---

### FILE: limitations.tex

| # | Number | Location | Claim | Source Exp | Registry Value | Status | Notes |
|---|--------|----------|-------|-----------|----------------|--------|-------|
| L1 | ~58% fill rate | lim:1 | Observation fill rate | exp-003b / exp-020 | exp-003b: 5661/(8×176×9)=44.7%; exp-020 fill rate unconfirmed | **UNVERIFIED** | Same issue as E4. The 58% is claimed for the N=17/500-item design; cannot be verified from provided registry values. |
| L2 | 71% coverage at nominal 95% | lim:1 | CI overconfidence for c_n | exp-009 | coverage=0.71 | **OK** | |

---

### FILE: appendix.tex (key quantitative claims)

| # | Number | Location | Claim | Source Exp | Registry Value | Status | Notes |
|---|--------|----------|-------|-----------|----------------|--------|-------|
| AP1 | Full G-MFRM: 0.124±0.016 (θ-RMSE), 0.922±0.010 (τ), 0.593±0.224 (c_n-RMSE) | app:153 | Ablation table, full model | exp-w7-ablation | θ_RMSE=0.1243±0.0164, τ=0.9224±0.0097, c_RMSE=0.5933±0.2242 | **OK** | Rounded appropriately (e.g., 0.0097→0.010) |
| AP2 | −Judge severity: 0.127±0.016, 0.922±0.010, 0.629±0.243 | app:154 | Ablation, no d_j | exp-w7-ablation | no_judge_severity: θ_RMSE=0.1266±0.0160, c_RMSE=0.6292±0.2425, τ=0.9216±0.0097 | **MISMATCH** | Paper shows 0.127 (registry: 0.1266→rounds to 0.127 OK), c_n-RMSE 0.629 (registry: 0.6292→rounds to 0.629 OK), τ 0.922 (registry: 0.9216→rounds to 0.922 OK). **OK** |
| AP3 | Binary gating: 0.137±0.016, 0.909±0.014, 0.833±0.226 | app:155 | Ablation, binary | exp-w7-ablation | binary_gating: θ_RMSE=0.1371±0.0161, τ=0.9093±0.0140, c_RMSE=0.8326±0.2257 | **OK** | 0.1371→0.137, 0.9093→0.909, 0.8326→0.833, ±0.0161→0.016, ±0.0140→0.014, ±0.2257→0.226. OK. |
| AP4 | Staged: 0.254±0.045, 0.839±0.035, 1.382±0.164 | app:156 | Ablation, staged | exp-w7-ablation | staged: θ_RMSE=0.2539±0.0448, τ=0.8393±0.0349, c_RMSE=1.3823±0.1635 | **OK** | 0.2539→0.254, 0.8393→0.839, 1.3823→1.382, ±0.0448→0.045, ±0.0349→0.035, ±0.1635→0.164. OK. |
| AP5 | staged increases θ-RMSE by 2.0× | app:163 | Ablation narrative | exp-w7-ablation | 0.2539/0.1243=2.04× | **OK** | |
| AP6 | c_n-RMSE 2.3× (staged vs full) | app:163 | Ablation narrative | exp-w7-ablation | 1.3823/0.5933=2.33× | **OK** | |
| AP7 | binary c_n-RMSE +40% | app:165 | Gating ablation | exp-w7-ablation | (0.8326−0.5933)/0.5933=40.3% | **OK** | |
| AP8 | binary θ-RMSE +10% | app:165 | Gating ablation | exp-w7-ablation | (0.1371−0.1243)/0.1243=10.3% | **OK** | |
| AP9 | −d_j: θ-RMSE +2.4%, p=0.245; τ identical, p=0.344; c_n-RMSE +6.1%, p<0.001 | app:167 | Ablation significance | exp-w7-ablation | no_judge_severity: θ_RMSE diff=(0.1266−0.1243)/0.1243=1.85% ≈ not 2.4%; c_n diff=(0.6292−0.5933)/0.5933=6.1% | **MISMATCH** | θ-RMSE increase: (0.1266−0.1243)/0.1243 = 1.85%, paper says 2.4%. **MISMATCH** of 0.55pp. |
| AP10 | Claude Opus d_j=+0.60 vs Mistral −0.74 | app:167 | Judge severity contrast | exp-003b | d_j: Claude-Opus-4.7=0.60, Mistral-Large-2=−0.74 | **OK** | |
| AP11 | 1,000 posterior draws, 5,661 observations (PPC) | app:180–181 | PPC parameters | exp-003b | n_observations=5661 | **OK** | |
| AP12 | predicted mean win rate 0.593 vs observed 0.599 | app:180 | PPC win rates | exp-003b | Not in provided registry values | **UNVERIFIED** | |
| AP13 | ΔELPD=−55.7, SE=9.4 (LOO appendix) | app:193 | LOO model comparison | LOO (N=8) | ΔELPD=−55.7, SE=9.4 | **OK** | |
| AP14 | \|Δ/SE\|=5.9 | app:198 (fig caption) | LOO ratio | — | 55.7/9.4=5.93 | **OK** | |
| AP15 | 5,661 observations (Pareto k̂ fig caption) | app:207 | N=8 pilot observation count | exp-003b | n_observations=5661 | **OK** | |
| AP16 | Qwen2.5-72B self-judging win rate 1.000 (42/42) | app:217 | Self-evaluation | exp-003b / exp-020 | Not in registry | **UNVERIFIED** | |
| AP17 | LLaMA-3.3-70B self-judging win rate 0.912, cross-judge mean 0.823 | app:217 | Self-evaluation | exp-020 | Not in registry | **UNVERIFIED** | |
| AP18 | Qwen2.5-72B cross-judge mean 0.714 | app:217 | Self-evaluation | exp-020 | Not in registry | **UNVERIFIED** | |
| AP19 | τ=0.857 (excluding 99 self-judging obs) | app:219 | Robustness check | exp-003b variant | exp-003b joint_gmfrm τ=0.857 | **OK** | |
| AP20 | c_n shift < 0.15 | app:219 | Self-eval robustness | exp-003b variant | Not in registry | **UNVERIFIED** | |
| AP21 | Severity range spans 1.34 logits | app:245 (table caption) | Judge severity range | exp-003b | 0.60−(−0.74)=1.34 | **OK** | |
| AP22 | k=2: G-MFRM 0.771±0.081 | app:262 | Judge count table | exp-006 | k=2: τ=0.771±0.081 | **OK** | |
| AP23 | k=4: G-MFRM 0.800±0.045 | app:263 | Judge count table | exp-006 | k=4: τ=0.800±0.045 | **OK** | |
| AP24 | k=6: G-MFRM 0.821±0.051 | app:264 | Judge count table | exp-006 | k=6 mean: τ=0.821±0.051 | **OK** | |
| AP25 | k=9: G-MFRM 0.857 | app:265 | Judge count table | exp-003b | τ=0.857 | **OK** | |
| AP26 | k≥4 exceeds full-panel baseline τ=0.786 | app:253 | Judge count recommendation | exp-006 / exp-003b | k=4: 0.800>0.786 ✓ | **OK** | |
| AP27 | τ=0.771→0.857 monotone | app:253 | Monotone increase | exp-006 | k=2: 0.771, k=4: 0.800, k=6: 0.821, k=9: 0.857 | **OK** | |
| AP28 | Three individually necessary judges: Claude Opus (+0.60), GPT-5.5 (+0.53), LLaMA-3.3-70B (−0.42) | app:272 | Leave-one-judge-out | exp-003b | d_j: Claude-Opus-4.7=0.60, GPT-5.5=0.53, LLaMA-3.3-70B=−0.42 | **OK** | |
| AP29 | ρ≥0.998 (weight configs, all four) | app:280 | Weight robustness | exp-013 | min ρ=0.9978; appendix Table shows 50/50=0.998, 75/25=1.000, 90/10=0.999, 100/0=0.998 | **OK** | All ≥0.998 | |
| AP30 | Δτ=0.071, G-MFRM τ=0.857 vs baseline τ=0.786 | app:303 | Power analysis effect size | exp-003b | Δτ=0.071, confirmed | **OK** | |
| AP31 | power ~50% at N=8 | app:307 | Power analysis | Simulation | Not in registry | **UNVERIFIED** | |
| AP32 | 80% power at N≈17 | app:307 | Power analysis | Simulation | Not in registry | **UNVERIFIED** | |
| AP33 | 95% power at N≈25 | app:307 | Power analysis | Simulation | Not in registry | **UNVERIFIED** | |
| AP34 | bootstrap Δτ CI [−0.071, 0.071] at N=8 | app:307 | Bootstrap CI | exp-020 | exp-020 bootstrap Δτ CI: [−0.141, 0] | **MISMATCH** | Registry: bootstrap Δτ CI=[-0.141, 0]. Paper appendix says [−0.071, 0.071]. These are different ranges. The table caption in experiments.tex says "$^\dagger$Bootstrap Δτ CI includes zero" without giving exact bounds. The power analysis appendix (app:307) gives CI [−0.071, 0.071] while registry gives [−0.141, 0]. **MISMATCH**. |
| AP35 | ability scores differing by <0.03 logits across baselines | app:313 | Baseline comparison | exp-004 | N=8: all baselines τ=0.8095; N=17: baselines within 0.015 of raw | **UNVERIFIED** | Ability score differences (<0.03 logits) not in registry |
| AP36 | GPT-4o: θ̂=+2.00 [1.70, 2.30], ĉ_n=0.88 [0.05, 2.20] | app:324 | Per-model table | exp-003b | c_n=0.880 (CI [0.052, 2.2]); CI lower: 0.052 vs paper 0.05 | **OK** | 0.052→0.05 acceptable rounding |
| AP37 | GPT-4o-mini: ĉ_n=0.93 [0.06, 2.20] | app:325 | Per-model table | exp-003b | c_n=0.934 (CI [0.059, 2.2]); CI lower: 0.059 vs paper 0.06 | **OK** | |
| AP38 | Qwen2.5-72B: ĉ_n=3.00 [1.40, 4.60] | app:326 | Per-model table | exp-003b | c_n=2.961 (CI [1.4, 4.6]); 2.961 vs paper 3.00 | **MISMATCH** | 2.961 rounds to 2.96, not 3.00. Paper reports 3.00. |
| AP39 | LLaMA-3.3-70B: ĉ_n=2.50 [1.10, 3.90] | app:327 | Per-model table | exp-003b | c_n=2.478 (CI [1.1, 3.9]); 2.478 vs paper 2.50 | **MISMATCH** | 2.478 rounds to 2.48, not 2.50. |
| AP40 | Qwen3-8B: ĉ_n=1.20 [0.14, 2.50] | app:328 | Per-model table | exp-003b | c_n=1.178 (CI [0.14, 2.5]); 1.178 vs paper 1.20 | **MISMATCH** | 1.178 rounds to 1.18, not 1.20. |
| AP41 | Gemma-2-9B: ĉ_n=1.70 [0.36, 2.90] | app:329 | Per-model table | exp-003b | c_n=1.654 (CI [0.36, 2.9]); 1.654 vs paper 1.70 | **MISMATCH** | 1.654 rounds to 1.65, not 1.70. |
| AP42 | GPT-4-0613: ĉ_n=4.20 [3.10, 5.30] | app:330 | Per-model table | exp-003b | c_n=4.168 (CI [3.1, 5.3]); 4.168 vs paper 4.20 | **MISMATCH** | 4.168 rounds to 4.17, not 4.20. Same issue as E30. |
| AP43 | GPT-3.5-Turbo: ĉ_n=5.60 [4.40, 6.80] | app:331 | Per-model table | exp-003b | c_n=5.587 (CI [4.4, 6.8]); 5.587 vs paper 5.60 | **MISMATCH** | 5.587 rounds to 5.59, not 5.60. Same issue as E29. |
| AP44 | ~71% CI coverage (table caption) | app:334 | c_n credible interval coverage | exp-009 | coverage=0.71 | **OK** | |
| AP45 | Δθ values in bias absorption table (GPT-3.5: +0.786, GPT-4-0613: +0.431, etc.) | app:352–359 | Bias absorption | exp-019 | All Δθ values match exactly | **OK** | All values match registry exactly |
| AP46 | ĉ_n values in bias table: 5.587, 4.168, 2.961, 2.478, 1.654, 1.178, 0.934, 0.880 | app:352–359 | c_n in bias absorption table | exp-003b | Exact match | **OK** | Uses exact registry values (not rounded) |
| AP47 | N=8 synthetic calibration: θ-RMSE halved (0.083 vs 0.166), τ=0.954 vs 0.882, Δτ=+0.072, all 10 wins 0 losses 10 ties, p<0.002 | app:370 | Synthetic calibration, N=8 | exp-015 | θ_RMSE joint=0.0827, sequential=0.1664; τ joint=0.9536, seq=0.8821; Wilcoxon p=0.002, 10 wins/10 ties/0 losses | **OK** | 0.0827→0.083, 0.1664→0.166, 0.9536→0.954, 0.8821→0.882 — all consistent. Δτ=0.9536−0.8821=0.0715→0.072 ✓ |
| AP48 | θ-RMSE reduced by −50.3% | app:379 (table) | Synthetic N=8 calibration | exp-015 | θ_RMSE reduction: −50.3% | **OK** | |
| AP49 | τ improvement +7.2pp | app:380 | Synthetic N=8 | exp-015 | Δτ=0.0715≈7.2pp | **OK** (minor rounding) | 0.0715→7.2pp is slightly generous; exactly 7.15pp. Acceptable. |
| AP50 | c_n-RMSE −60.5% | app:381 | Synthetic N=8 | exp-015 | c_RMSE reduction: −60.5% | **OK** | |
| AP51 | R̂=1.0, ESS≥1,678 (synthetic N=8) | app:370 | Convergence, synthetic N=8 | exp-015 | Not in exp-015 registry values | **UNVERIFIED** | exp-015 registry does not include R̂ and ESS values in provided ground truth |
| AP52 | N=20 calibration: Δτ=+0.052, p=1.81×10^{−4}, 18 wins/1 loss/1 tie | app:389 | Synthetic N=20 | exp-018 | Δτ=+0.0521, Wilcoxon p=0.000181=1.81×10^{−4}, 18 wins/1 tie/1 loss | **OK** | Registry says "1 tie/1 loss" — paper says "1 loss/1 tie" same thing |
| AP53 | N=20 θ-RMSE −45.2% | app:398 | Synthetic N=20 | exp-018 | θ_RMSE reduction: −45.2% | **OK** | |
| AP54 | N=20 τ +5.2pp | app:399 | Synthetic N=20 | exp-018 | Δτ=+0.0521≈5.2pp | **OK** | |
| AP55 | N=20 c_n-RMSE −54.5% | app:400 | Synthetic N=20 | exp-018 | c_RMSE reduction: −54.5% | **OK** | |
| AP56 | N=20 sequential θ-RMSE: 0.171±0.049 | app:398 | N=20 table | exp-018 | sequential: θ_RMSE=0.1714 | **OK** | |
| AP57 | N=20 joint θ-RMSE: 0.094±0.019 | app:398 | N=20 table | exp-018 | joint: θ_RMSE=0.094 | **OK** | |
| AP58 | Prior robustness: Pearson r=1.000 for θ̂, r>0.999 for ĉ_n | app:435 | Prior sensitivity | — | Not in registry | **UNVERIFIED** | |
| AP59 | Item fit: 176 items, 92 flagged (18 overfit >1.5, 74 underfit <0.5) | app:441–458 | Item-level diagnostics | exp-003b | n_items=176 | **OK** (partial) | Item count matches; 92 flagged/18 overfit/74 underfit are UNVERIFIED in registry |
| AP60 | Error propagation: σ=0.0 θ-RMSE=0.128±0.018, c_n-RMSE=0.533±0.187 | app:482 | Error prop table | exp-012 | σ=0.0: θ_RMSE=0.1277, c_n RMSE=0.533 | **OK** | 0.1277→0.128 |
| AP61 | σ=0.1: θ-RMSE=0.130±0.018, Δ+1.4%; c_n-RMSE=0.545±0.192, Δ+2.3% | app:483 | Error prop table | exp-012 | σ=0.1: θ_RMSE +1.4%, c_n RMSE +2.3% | **OK** | |
| AP62 | σ=0.2: θ-RMSE=0.135±0.018, Δ+5.9%; c_n-RMSE=0.575±0.198, Δ+7.9% | app:484 | Error prop table | exp-012 | σ=0.2: θ_RMSE +5.9%, c_n RMSE +7.9% | **OK** | |
| AP63 | σ=0.5: θ-RMSE=0.175±0.027, Δ+36.9%; c_n-RMSE=0.842±0.281, Δ+57.9% | app:485 | Error prop table | exp-012 | σ=0.5: θ_RMSE +36.9%, c_n RMSE +57.9% | **OK** | |
| AP64 | CI coverage: θ=90.1% at N=8 (49 seeds), c_n=67.9%; c_n=71% at N=50 | app:464 | CI coverage analysis | exp-009 / CI analysis | exp-009: coverage=0.71 (for c_n at N=50) | **OK** | The 71% matches; 67.9% at N=8 and 90.1% for θ are **UNVERIFIED** in provided registry |
| AP65 | N=8 config: ~10 min; N=17: ~45 min; total <5 GPU-hours | app:514 | Compute resources | — | Not in registry | **UNVERIFIED** | |
| AP66 | exp-003b: 4 chains × 10,000 iterations | app:514 | MCMC configuration | exp-003b | Not in provided registry | **UNVERIFIED** | |

---

## Summary of Issues Requiring Correction

### DEFINITIVE MISMATCHES (must fix):

| ID | Location | Paper Says | Registry Says | Action |
|----|----------|-----------|---------------|--------|
| **E18** | experiments.tex:50 | p < 10^{−6} | p = 1.91×10^{−6} (i.e., > 10^{-6}) | Change to "p < 10^{−5}" or "p = 1.91 × 10^{−6}" |
| **E29/AP43** | experiments.tex:66; appendix.tex:331 | GPT-3.5-Turbo ĉ_n = 5.60 | 5.587 → rounds to 5.59 | Change to 5.59 |
| **E30/AP42** | experiments.tex:66; appendix.tex:330 | GPT-4-0613 ĉ_n = 4.20 | 4.168 → rounds to 4.17 | Change to 4.17 |
| **AP38** | appendix.tex:326 | Qwen2.5-72B ĉ_n = 3.00 | 2.961 → rounds to 2.96 | Change to 2.96 |
| **AP39** | appendix.tex:327 | LLaMA-3.3-70B ĉ_n = 2.50 | 2.478 → rounds to 2.48 | Change to 2.48 |
| **AP40** | appendix.tex:328 | Qwen3-8B ĉ_n = 1.20 | 1.178 → rounds to 1.18 | Change to 1.18 |
| **AP41** | appendix.tex:329 | Gemma-2-9B ĉ_n = 1.70 | 1.654 → rounds to 1.65 | Change to 1.65 |
| **E36** | experiments.tex:66 | R̂ ≤ 1.003, ESS ≥ 1,240 attributed to "N=8 pilot" | These values are from exp-020 (N=17); exp-003b has R̂=1.03, ESS=174 | Attribute to "N=17 analysis" or correct values |
| **AP34** | appendix.tex:307 | Bootstrap Δτ CI [−0.071, 0.071] | Registry: [−0.141, 0] | Verify artifact and correct if needed |
| **E15** | experiments.tex:44 (table caption) | All 7 baselines τ within 0.014 of raw at both panel sizes | N=8: baselines at 0.8095, raw=0.786, diff=0.0235 > 0.014 | Change "0.014" to "0.024" or restrict claim to N=17 only |
| **AP9** | appendix.tex:167 | −d_j: θ-RMSE +2.4% | (0.1266−0.1243)/0.1243 = 1.85% | Change to "+1.9%" or "+2%" |

### UNVERIFIED (cannot confirm or deny from provided registry):
- r=0.86 (background.tex:7, 34) — OVB validation correlation
- ~58% fill rate (experiments.tex:16, limitations.tex:1) — needs obs count for N=17 design
- Var(e_i) ≈ 0.04 (method.tex:78)
- Bootstrap CI [−0.071, 0.071] in power analysis (appendix.tex:307) — contradicts registry [−0.141, 0]
- Self-evaluation win rates (appendix.tex:217–218)
- Power analysis percentages (50%, 80% at N=17, 95% at N=25)
- Predicted PPC win rate 0.593 vs observed 0.599

### CONFIRMED OK (all other numbers):
All main experimental results (τ values, RMSE values, ELPD, SE, the 51% reduction, 4–6× ratio, Δτ progression, judge severity values, judge count table) are consistent with the registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fefd9b7f-4b19-4344-b946-1bbd7c2d731c",
  "isSidechain": true,
  "agentId": "a92bd2628d8113da1",
  "requestId": "req_011CbPrnaWumjtxeT6iLuNK6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cc6bca6b-1650-459f-9788-6b8f5c5e0be1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/agent_41260ada",
  "sessionId": "39f64d8a-146f-412d-ae9a-7526e093921c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "jolly-launching-mango",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01V42W7NP2cf3UBjnkTqfDTP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 773,
      "cache_creation_input_tokens": 15143,
      "cache_read_input_tokens": 46340,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15143,
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
