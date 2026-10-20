# Research conversation: You are working on the causal_annot_error_attrib project. Task: Create and run a script to analyze primary coefficient s

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a345197f572e1e9bc.jsonl`
- **Structured JSON:** [`bac294194d290580aed5.json`](../../sessions/ba/bac294194d290580aed5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-23T00:19:01.768Z_

You are working on the causal_annot_error_attrib project. Task: Create and run a script to analyze primary coefficient sign reversal across different β₁/β₂ ratios.

Project root: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib

Context: The paper studies how multi-class (K=3) annotation errors affect causal estimators. For the "exposure" topology, the current paper claims "the primary coefficient never reverses sign" based on empirical LLM data. We need to verify this systematically.

Create a script `artifacts/exp_primary_coeff_breakdown.py` that:
1. Uses the same DGP framework as the existing code (import from plan_006_asv_empirical.py)
2. For the exposure topology with K=3:
   - Tests β ratio configurations: β₁/β₂ ratios of {1.0, 1.5, 2.0, 5.0, 10.0, 50.0}
   - For each ratio, set β = [0.0, β₁, β₂] where β₁ = 1.0 and β₂ = 1.0/ratio (so ratio=1 means equal, ratio=50 means β₂ is very small)
   - Generate 100,000 Dirichlet(1,1,1) confusion matrices
   - For each matrix, compute the analytical probability limit of each coefficient
   - Check if the PRIMARY coefficient (β₁, the largest) ever reverses sign
   - Check if SECONDARY coefficients reverse sign
   - Also check at diagonal ≥ 0.7 threshold
3. Report: for each β ratio, the sign-flip rate for primary vs secondary coefficients
4. Save results to `artifacts/exp_primary_coeff_breakdown_results.json`

Reference the existing code structure. The key imports from plan_006_asv_empirical.py:
- make_dgp_params(K) - generates DGP parameters
- precompute_suff_stats(K, topo, params) - precomputes sufficient statistics  
- compute_plim(C, suff_stats, K) - computes analytical probability limit given confusion matrix C

For the exposure topology, compute_plim returns the full coefficient vector. Check sign of each coefficient vs the true coefficient.

Run the script locally (CPU-only) and report results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "221cc120-ad2a-4ac2-82b3-5f678194e371",
  "agentId": "a345197f572e1e9bc",
  "type": "user",
  "uuid": "4ae7a76e-39bf-49a3-8fc4-6cf0e17cc107",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-23T00:19:01.771Z_

```json
{
  "parentUuid": "4ae7a76e-39bf-49a3-8fc4-6cf0e17cc107",
  "isSidechain": true,
  "agentId": "a345197f572e1e9bc",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
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
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
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
  "uuid": "af9a59a1-62eb-4453-928a-66030bed407e",
  "timestamp": "2026-05-23T00:19:01.771Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

---

### Assistant

_source line 3 · 2026-05-23T00:19:07.035Z_



I'll start by understanding the existing code structure, then create and run the script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af9a59a1-62eb-4453-928a-66030bed407e",
  "isSidechain": true,
  "agentId": "a345197f572e1e9bc",
  "requestId": "req_011CbJYNLxoBJCrGFk1hAjQR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "70ddf345-6717-4bab-8dfa-a90740b70ea0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxfbJLrkoYNq1RYsh7dkEs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21609,
      "cache_read_input_tokens": 8272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21609,
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

_source line 4 · 2026-05-23T00:19:07.707Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01NjBSmEpbDUGwBdxgDDgUwr`</summary>

```json
{
  "pattern": "**/plan_006_asv_empirical.py",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70ddf345-6717-4bab-8dfa-a90740b70ea0",
  "isSidechain": true,
  "agentId": "a345197f572e1e9bc",
  "requestId": "req_011CbJYNLxoBJCrGFk1hAjQR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b020f77d-219d-4a2e-bc79-744f261759c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxfbJLrkoYNq1RYsh7dkEs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21609,
      "cache_read_input_tokens": 8272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21609,
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

_source line 5 · 2026-05-23T00:19:07.782Z_

<details><summary>↩ Tool result · `toolu_01NjBSmEpbDUGwBdxgDDgUwr`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b020f77d-219d-4a2e-bc79-744f261759c0",
  "isSidechain": true,
  "promptId": "221cc120-ad2a-4ac2-82b3-5f678194e371",
  "agentId": "a345197f572e1e9bc",
  "type": "user",
  "uuid": "7bd65c94-7ee5-448b-8e2c-44be2a196ae4",
  "sourceToolAssistantUUID": "b020f77d-219d-4a2e-bc79-744f261759c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-23T00:19:08.096Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01MwKD4vhbxYWTdRcuUViJeE`</summary>

```json
{
  "pattern": "**/artifacts/*.py",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bd65c94-7ee5-448b-8e2c-44be2a196ae4",
  "isSidechain": true,
  "agentId": "a345197f572e1e9bc",
  "requestId": "req_011CbJYNLxoBJCrGFk1hAjQR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a16085a6-ce38-4f0c-9839-f8095f172ec2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxfbJLrkoYNq1RYsh7dkEs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21609,
      "cache_read_input_tokens": 8272,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21609
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 210,
          "cache_read_input_tokens": 8272,
          "cache_creation_input_tokens": 21609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21609,
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

_source line 7 · 2026-05-23T00:19:08.173Z_

<details><summary>↩ Tool result · `toolu_01MwKD4vhbxYWTdRcuUViJeE`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_confounding_dag.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_exposure_dag.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_exposure_dirichlet_subspace.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/preprocess.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan_005_asv_extended_fixed.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan_002_k57_extended_7topo.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan_009_pathological_matrices.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_iv_dirichlet_subspace.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_theory_empirical_mape.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_all_tasks.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_ppi_empirical.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_delta_max.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/annotate.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_updated_empirical.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_c_bootstrap_asv.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify_v2.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/analyze_epsilon_bound.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_b_logistic_dgp.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/analyze_epsilon_sign_structure.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_epsilon_tau_sensitivity.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/verify_lambda_bound.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/verify_theorem1_refine.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_fwl_logistic_breakdown.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/verify_theorem1_direct.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_unified_mape.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/nondiff_stress_test.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a16085a6-ce38-4f0c-9839-f8095f172ec2",
  "isSidechain": true,
  "promptId": "221cc120-ad2a-4ac2-82b3-5f678194e371",
  "agentId": "a345197f572e1e9bc",
  "type": "user",
  "uuid": "df7774e3-ad81-477e-ad53-b8aae8e810f7",
  "sourceToolAssistantUUID": "a16085a6-ce38-4f0c-9839-f8095f172ec2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-23T00:19:11.861Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NC1xPLBuc89vGt735c2MCG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df7774e3-ad81-477e-ad53-b8aae8e810f7",
  "isSidechain": true,
  "agentId": "a345197f572e1e9bc",
  "requestId": "req_011CbJYNpPoRJ5p46PsCvjDd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6b1ff72f-e74f-4339-b03e-e10167c8be1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132fEbaZETsVjHDZUfq3ZTp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2348,
      "cache_read_input_tokens": 29881,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2348
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 29881,
          "cache_creation_input_tokens": 2348,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2348,
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

_source line 9 · 2026-05-23T00:19:12.145Z_

<details><summary>↩ Tool result · `toolu_01NC1xPLBuc89vGt735c2MCG`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_006: Empirical ASV Calibration with LLM Annotation Confusion Matrices
4	
5	Uses empirical confusion matrices from LLM annotations (3 LLMs × 3 datasets × 3 prompts
6	= 27 C matrices) to compute:
7	  1. Downstream causal bias across 7 DAG topologies
8	  2. ASV sensitivity metrics (magnitude, significance, sign-flip)
9	  3. F1 vs bias disconnect analysis (Baumann 2025 verification)
10	  4. Type I/II error rates before/after ASV filtering
11	  5. Inter-model error correlation
12	
13	Input:  data/{dataset}/{model}_{prompt}_annotations.jsonl
14	        Each line: {"true_label": int, "predicted_label": int}
15	
16	Output: artifacts/plan006/asv_empirical_results.json
17	
18	Dependencies: numpy (required), matplotlib (optional for plots)
19	"""
20	
21	import numpy as np
22	import json
23	import argparse
24	import os
25	import time
26	from collections import OrderedDict
27	
28	try:
29	    import matplotlib
30	    matplotlib.use('Agg')
31	    import matplotlib.pyplot as plt
32	    HAS_MPL = True
33	except ImportError:
34	    HAS_MPL = False
35	
36	# ============================================================================
37	# Constants
38	# ============================================================================
39	
40	DATASETS = OrderedDict([
41	    ('civil_comments', {'K': 2}),
42	    ('vast', {'K': 3}),
43	    ('humaid', {'K': 10}),
44	])
45	
46	MODELS = ['llama4', 'qwen3', 'deepseek']
47	PROMPTS = ['zero-shot', 'few-shot-3', 'few-shot-5']
48	
49	TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
50	              'mbias', 'iv', 'frontdoor']
51	
52	N_PRECOMP = 2_000_000
53	
54	# Parameter pools — K=3 values match plan_001/plan_005
55	_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]
56	_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
57	_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
58	_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
59	_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]
60	_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
61	_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2, 0.15, -0.1, 0.05]
62	
63	
64	# ============================================================================
65	# Utility Functions
66	# ============================================================================
67	
68	def softmax_rows(logits):
69	    e = np.exp(logits - logits.max(axis=1, keepdims=True))
70	    return e / e.sum(axis=1, keepdims=True)
71	
72	
73	def sample_cat(probs, rng):
74	    cum = np.cumsum(probs, axis=1)
75	    u = rng.uniform(size=probs.shape[0])[:, None]
76	    return (u >= cum[:, :-1]).sum(axis=1).astype(int)
77	
78	
79	def generate_Astar(A, C, rng):
80	    probs = C[:, A]
81	    cum = np.cumsum(probs, axis=0)
82	    u = rng.uniform(size=len(A))
83	    return (u[None, :] >= cum[:-1]).sum(axis=0).astype(int)
84	
85	
86	def ols_with_dummies(Y, T, Astar, K):
87	    N = len(Y)
88	    D = np.zeros((N, K - 1))
89	    for k in range(1, K):
90	        D[:, k - 1] = (Astar == k).astype(float)
91	    X = np.column_stack([np.ones(N), T, D])
92	    try:
93	        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
94	        resid = Y - X @ beta
95	        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)
96	        XtX_inv = np.linalg.inv(X.T @ X)
97	        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))
98	    except np.linalg.LinAlgError:
99	        beta = np.full(X.shape[1], np.nan)
100	        se = np.full(X.shape[1], np.nan)
101	    return beta, se
102	
103	
104	def ols_no_T(Y, Astar, K):
105	    N = len(Y)
106	    D = np.zeros((N, K - 1))
107	    for k in range(1, K):
108	        D[:, k - 1] = (Astar == k).astype(float)
109	    X = np.column_stack([np.ones(N), D])
110	    try:
111	        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
112	        resid = Y - X @ beta
113	        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)
114	        XtX_inv = np.linalg.inv(X.T @ X)
115	        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))
116	    except np.linalg.LinAlgError:
117	        beta = np.full(X.shape[1], np.nan)
118	        se = np.full(X.shape[1], np.nan)
119	    return beta, se
120	
121	
122	def wald_estimator(Z, Y, Astar, k=1):
123	    z1 = Z == 1; z0 = Z == 0
124	    n1, n0 = float(z1.sum()), float(z0.sum())
125	    if n1 < 2 or n0 < 2:
126	        return np.nan, np.nan
127	    RF = Y[z1].mean() - Y[z0].mean()
128	    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0
129	    Dk_z1 = (Astar[z1] == k).astype(float).mean()
130	    Dk_z0 = (Astar[z0] == k).astype(float).mean()
131	    FS = Dk_z1 - Dk_z0
132	    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0
133	    if abs(FS) < 1e-8:
134	        return np.nan, np.nan
135	    W = RF / FS
136	    var_W = var_RF / FS**2 + RF**2 * var_FS / FS**4
137	    return W, np.sqrt(max(var_W, 0))
138	
139	
140	# ============================================================================
141	# DGP Parameters (general K, K=3 matches plan_001/plan_005)
142	# ============================================================================
143	
144	def make_p_A(K):
145	    if K == 2:
146	        return np.array([0.55, 0.45])
147	    elif K == 3:
148	        return np.array([0.40, 0.35, 0.25])
149	    else:
150	        raw = np.array([1.0 / (i + 1) for i in range(K)])
151	        return raw / raw.sum()
152	
153	
154	def make_dgp_params(K):
155	    p_A = make_p_A(K)
156	    params = {
157	        'confounding': {
158	            'p_A': p_A,
159	            'alpha': np.array(_ALPHA_POOL[:K - 1]),
160	            'beta_A': np.array(_BETA_A_POOL[:K - 1]),
161	            'beta_T': 2.0,
162	            'sigma_T': 1.0,
163	        },
164	        'mediation': {
165	            'tau': 0.5,
166	            'gamma': np.array(_GAMMA_POOL[:K]),
167	            'delta': np.array(_DELTA_POOL[:K]),
168	            'beta': np.array(_BETA_POOL[:K]),
169	        },
170	        'collider': {
171	            'tau': 1.0,
172	            'g': np.zeros(K),
173	            'dT': np.array(_DT_POOL[:K]),
174	            'dY': np.array(_DY_POOL[:K]),
175	        },
176	        'exposure': {
177	            'beta': np.array(_BETA_POOL[:K]),
178	            'p_A': p_A,
179	        },
180	    }
181	    if K == 3:
182	        params['mbias'] = {
183	            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,
184	            'g': np.zeros(3),
185	            'a_U1': np.array([0.0, 0.8, -0.5]),
186	            'a_U2': np.array([0.0, 0.6, 0.9]),
187	        }
188	        params['iv'] = {
189	            'lam': 1.0, 'beta': np.array([0.0, 0.5, -0.25]),
190	            'g': np.zeros(3),
191	            'dZ': np.array([0.0, 1.0, -0.5]),
192	            'dU': np.array([0.0, 0.8, 0.6]),
193	        }
194	        params['frontdoor'] = {
195	            'alpha_U': 1.0, 'lambda_U': 1.0,
196	            'gamma': np.array([0.0, 0.5, -0.3]),
197	            'delta_fd': np.array([0.0, 1.0, -0.8]),
198	            'beta': np.array([0.0, 1.0, -0.5]),
199	        }
200	    else:
201	        params['mbias'] = {
202	            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,
203	            'g': np.zeros(K),
204	            'a_U1': np.array([0.0] + [_ALPHA_POOL[i] * 0.6 for i in range(K - 1)]),
205	            'a_U2': np.array([0.0] + [_BETA_A_POOL[i] * 0.8 for i in range(K - 1)]),
206	        }
207	        iv_beta = np.array(_BETA_POOL[:K]) * 0.5
208	        iv_beta[0] = 0.0
209	        params['iv'] = {
210	            'lam': 1.0, 'beta': iv_beta,
211	            'g': np.zeros(K),
212	            'dZ': np.array([0.0] + [_ALPHA_POOL[i] * 0.7 for i in range(K - 1)]),
213	            'dU': np.array([0.0] + [_BETA_A_POOL[i] * 0.6 for i in range(K - 1)]),
214	        }
215	        fd_delta = np.array(_DELTA_POOL[:K])
216	        fd_delta[0] = 0.0
217	        params['frontdoor'] = {
218	            'alpha_U': 1.0, 'lambda_U': 1.0,
219	            'gamma': np.array(_GAMMA_POOL[:K]),
220	            'delta_fd': fd_delta,
221	            'beta': np.array(_BETA_POOL[:K]),
222	        }
223	    return params
224	
225	
226	def make_dgp_params_H0(K, params):
227	    p0 = {}
228	    for topo, p in params.items():
229	        if topo == 'confounding':
230	            p0[topo] = dict(p, beta_T=0.0)
231	        elif topo == 'mediation':
232	            p0[topo] = dict(p, tau=0.0)
233	        elif topo == 'collider':
234	            p0[topo] = dict(p, tau=0.0)
235	        elif topo == 'exposure':
236	            p0[topo] = dict(p, beta=np.zeros(K))
237	        elif topo == 'mbias':
238	            p0[topo] = dict(p, tau=0.0)
239	        elif topo == 'iv':
240	            p0[topo] = dict(p, beta=np.zeros(K))
241	        elif topo == 'frontdoor':
242	            p0[topo] = dict(p, lambda_U=0.0, alpha_U=0.0,
243	                            delta_fd=np.zeros(K), beta=np.zeros(K))
244	    return p0
245	
246	
247	# ============================================================================
248	# DGP Generators (general K)
249	# ============================================================================
250	
251	def gen_confounding(K, N, p, rng):
252	    A = rng.choice(K, size=N, p=p['p_A'])
253	    D = np.zeros((N, K - 1))
254	    for j in range(K - 1):
255	        D[:, j] = (A == j + 1).astype(float)
256	    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)
257	    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)
258	    return T, Y, A
259	
260	
261	def gen_mediation(K, N, p, rng):
262	    T = rng.binomial(1, 0.5, N).astype(float)
263	    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]
264	    probs = softmax_rows(logits)
265	    A = sample_cat(probs, rng)
266	    D = np.zeros((N, K - 1))
267	    for j in range(K - 1):
268	        D[:, j] = (A == j + 1).astype(float)
269	    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)
270	    return T, Y, A
271	
272	
273	def gen_collider(K, N, p, rng):
274	    T = rng.normal(0, 1, N)
275	    Y = p['tau'] * T + rng.normal(0, 1, N)
276	    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]
277	              + p['dY'][None, :] * Y[:, None])
278	    probs = softmax_rows(logits)
279	    A = sample_cat(probs, rng)
280	    return T, Y, A
281	
282	
283	def gen_exposure(K, N, p, rng):
284	    A = rng.choice(K, size=N, p=p['p_A'])
285	    D = np.zeros((N, K - 1))
286	    for j in range(K - 1):
287	        D[:, j] = (A == j + 1).astype(float)
288	    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)
289	    return None, Y, A
290	
291	
292	def gen_mbias(K, N, p, rng):
293	    U1 = rng.normal(0, 1, N)
294	    U2 = rng.normal(0, 1, N)
295	    T = p['delta_coef'] * U1 + rng.normal(0, 1, N)
296	    Y = p['tau'] * T + p['lam'] * U2 + rng.normal(0, 1, N)
297	    logits = (p['g'][None, :] + p['a_U1'][None, :] * U1[:, None]
298	              + p['a_U2'][None, :] * U2[:, None])
299	    probs = softmax_rows(logits)
300	    A = sample_cat(probs, rng)
301	    return T, Y, A
302	
303	
304	def gen_iv(K, N, p, rng):
305	    Z = rng.binomial(1, 0.5, N).astype(float)
306	    U = rng.normal(0, 1, N)
307	    logits = (p['g'][None, :] + p['dZ'][None, :] * Z[:, None]
308	              + p['dU'][None, :] * U[:, None])
309	    probs = softmax_rows(logits)
310	    A = sample_cat(probs, rng)
311	    D = np.zeros((N, K - 1))
312	    for j in range(K - 1):
313	        D[:, j] = (A == j + 1).astype(float)
314	    Y = D @ p['beta'][1:] + p['lam'] * U + rng.normal(0, 1, N)
315	    return Z, Y, A
316	
317	
318	def gen_frontdoor(K, N, p, rng):
319	    U = rng.normal(0, 1, N)
320	    T = p['alpha_U'] * U + rng.normal(0, 1, N)
321	    logits = p['gamma'][None, :] + p['delta_fd'][None, :] * T[:, None]
322	    probs = softmax_rows(logits)
323	    M = sample_cat(probs, rng)
324	    D = np.zeros((N, K - 1))
325	    for j in range(K - 1):
326	        D[:, j] = (M == j + 1).astype(float)
327	    Y = D @ p['beta'][1:] + p['lambda_U'] * U + rng.normal(0, 1, N)
328	    return T, Y, M
329	
330	
331	GEN_FNS = {
332	    'confounding': gen_confounding, 'mediation': gen_mediation,
333	    'collider': gen_collider, 'exposure': gen_exposure,
334	    'mbias': gen_mbias, 'iv': gen_iv, 'frontdoor': gen_frontdoor,
335	}
336	
337	
338	# ============================================================================
339	# Sufficient Statistics & Plim (general K)
340	# ============================================================================
341	
342	def precompute_suff_stats(K, topology, params, N=N_PRECOMP, seed=42):
343	    rng = np.random.default_rng(seed)
344	    first_var, Y, A = GEN_FNS[topology](K, N, params, rng)
345	    DA = np.zeros((N, K))
346	    for k in range(K):
347	        DA[:, k] = (A == k).astype(float)
348	
349	    if topology == 'iv':
350	        Z = first_var
351	        z1 = Z == 1; z0 = Z == 0
352	        RF = Y[z1].mean() - Y[z0].mean()
353	        FS = np.zeros(K)
354	        for k in range(K):
355	            FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()
356	        return dict(RF=RF, FS=FS, topology='iv')
357	    elif topology == 'exposure':
358	        return dict(p_A=DA.mean(0), E_Y=Y.mean(),
359	                    E_YD=(DA * Y[:, None]).mean(0), topology='exposure')
360	    else:
361	        T = first_var
362	        return dict(
363	            p_A=DA.mean(0), E_T=T.mean(), E_T2=(T**2).mean(),
364	            E_Y=Y.mean(), E_TY=(T * Y).mean(),
365	            E_TD=(DA * T[:, None]).mean(0),
366	            E_YD=(DA * Y[:, None]).mean(0), topology=topology)
367	
368	
369	def compute_plim(C, st, K):
370	    if st['topology'] == 'iv':
371	        FS_star = C @ st['FS']
372	        if abs(FS_star[1]) < 1e-8:
373	            return np.nan
374	        return st['RF'] / FS_star[1]
375	    elif st['topology'] == 'exposure':
376	        q = C @ st['p_A']
377	        cy = C @ st['E_YD']
378	        EZZ = np.zeros((K, K))
379	        EZZ[0, 0] = 1.0
380	        for j in range(1, K):
381	            EZZ[0, j] = EZZ[j, 0] = q[j]
382	            EZZ[j, j] = q[j]
383	        EZY = np.zeros(K)
384	        EZY[0] = st['E_Y']
385	        for j in range(1, K):
386	            EZY[j] = cy[j]
387	        try:
388	            return np.linalg.solve(EZZ, EZY)
389	        except np.linalg.LinAlgError:
390	            return np.full(K, np.nan)
391	    else:
392	        q = C @ st['p_A']
393	        ct = C @ st['E_TD']
394	        cy = C @ st['E_YD']
395	        dim = K + 1
396	        EZZ = np.zeros((dim, dim))
397	        EZZ[0, 0] = 1.0
398	        EZZ[0, 1] = EZZ[1, 0] = st['E_T']
399	        EZZ[1, 1] = st['E_T2']
400	        for j in range(1, K):
401	            EZZ[0, j + 1] = EZZ[j + 1, 0] = q[j]
402	            EZZ[1, j + 1] = EZZ[j + 1, 1] = ct[j]
403	            EZZ[j + 1, j + 1] = q[j]
404	        EZY = np.zeros(dim)
405	        EZY[0] = st['E_Y']
406	        EZY[1] = st['E_TY']
407	        for j in range(1, K):
408	            EZY[j + 1] = cy[j]
409	        try:
410	            return np.linalg.solve(EZZ, EZY)
411	        except np.linalg.LinAlgError:
412	            return np.full(dim, np.nan)
413	
414	
415	def extract_tau(plim_result, topology):
416	    if topology == 'iv':
417	        return float(plim_result) if np.isfinite(plim_result) else np.nan
418	    if isinstance(plim_result, np.ndarray):
419	        return float(plim_result[1]) if np.isfinite(plim_result[1]) else np.nan
420	    return np.nan
421	
422	
423	# ============================================================================
424	# 1. Data Loading & Confusion Matrix
425	# ============================================================================
426	
427	def load_confusion_matrix_npz(data_dir, dataset, model, prompt, K):
428	    path = os.path.join(data_dir, dataset, f"{model}_{prompt}_confusion_matrix.npz")
429	    d = np.load(path, allow_pickle=True)
430	    C = d['C']
431	    assert C.shape == (K, K), f"Expected ({K},{K}), got {C.shape}"
432	    return C
433	
434	
435	def load_annotations(data_dir, dataset, model, prompt):
436	    for suffix in ['_annotations.jsonl', '.jsonl']:
437	        path = os.path.join(data_dir, dataset, f"{model}_{prompt}{suffix}")
438	        if os.path.exists(path):
439	            break
440	    else:
441	        raise FileNotFoundError(f"No annotation file for {dataset}/{model}_{prompt}")
442	    records = []
443	    label_set = set()
444	    with open(path) as f:
445	        for line in f:
446	            rec = json.loads(line.strip())
447	            gl = rec.get('true_label', rec.get('gold_label'))
448	            pl = rec.get('predicted_label', rec.get('pred_label'))
449	            if gl is not None and pl is not None:
450	                label_set.add(gl)
451	                label_set.add(pl)
452	                records.append((gl, pl))
453	    if records and isinstance(records[0][0], str):
454	        sorted_labels = sorted(label_set)
455	        label_map = {l: i for i, l in enumerate(sorted_labels)}
456	        records = [(label_map[g], label_map[p]) for g, p in records]
457	    else:
458	        records = [(int(g), int(p)) for g, p in records]
459	    return records
460	
461	
462	def build_confusion_matrix(records, K):
463	    counts = np.zeros((K, K))
464	    for true_k, pred_k in records:
465	        if 0 <= true_k < K and 0 <= pred_k < K:
466	            counts[pred_k, true_k] += 1
467	    col_sums = counts.sum(axis=0)
468	    col_sums = np.where(col_sums < 1, 1, col_sums)
469	    return counts / col_sums
470	
471	
472	def load_all_confusion_matrices(data_dir, dataset_filter=None):
473	    matrices = {}
474	    for dataset, info in DATASETS.items():
475	        if dataset_filter and dataset not in dataset_filter:
476	            continue
477	        K = info['K']
478	        for model in MODELS:
479	            for prompt in PROMPTS:
480	                try:
481	                    C = load_confusion_matrix_npz(data_dir, dataset, model, prompt, K)
482	                    matrices[(dataset, model, prompt)] = C
483	                except (FileNotFoundError, Exception):
484	                    try:
485	                        records = load_annotations(data_dir, dataset, model, prompt)
486	                        C = build_confusion_matrix(records, K)
487	                        matrices[(dataset, model, prompt)] = C
488	                    except FileNotFoundError:
489	                        print(f"  [WARN] Missing: {dataset}/{model}_{prompt}")
490	    return matrices
491	
492	
493	# ============================================================================
494	# 2. Downstream Causal Bias
495	# ============================================================================
496	
497	def compute_bias_for_topology(C, K, topology, st, tau_true):
498	    plim_result = compute_plim(C, st, K)
499	    tau_hat = extract_tau(plim_result, topology)
500	    if np.isnan(tau_hat) or np.isnan(tau_true):
501	        return {'tau_hat': None, 'bias': None, 'bias_pct': None, 'sign_flip': False}
502	    bias = tau_hat - tau_true
503	    bias_pct = abs(bias) / abs(tau_true) if abs(tau_true) > 1e-12 else None
504	    sign_flip = bool(np.sign(tau_hat) != np.sign(tau_true) and abs(tau_true) > 1e-12)
505	    return {
506	        'tau_hat': float(tau_hat), 'bias': float(bias),
507	        'bias_pct': float(bias_pct) if bias_pct is not None else None,
508	        'sign_flip': sign_flip,
509	    }
510	
511	
512	def compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true):
513	    results = []
514	    for (dataset, model, prompt), C in confusion_matrices.items():
515	        K = DATASETS[dataset]['K']
516	        for topology in TOPOLOGIES:
517	            st = all_suff_stats[(K, topology)]
518	            tau_true = all_tau_true[(K, topology)]
519	            info = compute_bias_for_topology(C, K, topology, st, tau_true)
520	            results.append({
521	                'dataset': dataset, 'model': model, 'prompt': prompt,
522	                'K': K, 'topology': topology, **info,
523	            })
524	    return results
525	
526	
527	# ============================================================================
528	# 3. ASV Computation
529	# ============================================================================
530	
531	def C_interpolated(C0, delta, K):
532	    C_d = (1 - delta) * np.eye(K) + delta * C0
533	    C_d = np.maximum(C_d, 0.0)
534	    col_sums = C_d.sum(axis=0)
535	    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)
536	    return C_d / col_sums
537	
538	
539	def compute_delta_max(C0):
540	    min_diag = np.diag(C0).min()
541	    if min_diag >= 1.0:
542	        return 10.0
543	    return min(1.0 / (1.0 - min_diag), 10.0)
544	
545	
546	def compute_asv_for_matrix(C0, K, topology, st, tau_true, asv_type,
547	                           n_grid=1500, se_ref=None):
548	    dmax = compute_delta_max(C0)
549	    deltas = np.linspace(0, dmax, n_grid)
550	    tau_curve = np.zeros(n_grid)
551	    for i, d in enumerate(deltas):
552	        C_d = C_interpolated(C0, d, K)
553	        plim_result = compute_plim(C_d, st, K)
554	        tau_curve[i] = extract_tau(plim_result, topology)
555	
556	    bias_abs = np.abs(tau_curve - tau_true)
557	    envelope = np.zeros(n_grid)
558	    running_max = 0.0
559	    for i in range(n_grid):
560	        if np.isfinite(bias_abs[i]):
561	            running_max = max(running_max, bias_abs[i])
562	        envelope[i] = running_max
563	
564	    if asv_type == 'sign_flip':
565	        if abs(tau_true) < 1e-12:
566	            return None
567	        baseline_sign = np.sign(tau_true)
568	        for i in range(n_grid):
569	            if np.isfinite(tau_curve[i]) and np.sign(tau_curve[i]) != baseline_sign:
570	                return float(deltas[i])
571	        return None
572	    elif asv_type == 'magnitude':
573	        if abs(tau_true) < 1e-12:
574	            return None
575	        thresh = 0.1 * abs(tau_true)
576	        for i in range(n_grid):
577	            if envelope[i] > thresh:
578	                return float(deltas[i])
579	        return None
580	    elif asv_type == 'significance':
581	        if se_ref is None or se_ref < 1e-12:
582	            return None
583	        for i in range(n_grid):
584	            if np.isfinite(tau_curve[i]) and abs(tau_curve[i]) < 1.96 * se_ref:
585	                return float(deltas[i])
586	        return None
587	    return None
588	
589	
590	def estimate_reference_se(K, topology, params, N_ref=5000, n_mc=50, seed=999):
591	    gen_fn = GEN_FNS[topology]
592	    rng = np.random.default_rng(seed)
593	    tau_hats = []
594	    for _ in range(n_mc):
595	        first_var, Y, A = gen_fn(K, N_ref, params, rng)
596	        if topology == 'iv':
597	            th, _ = wald_estimator(first_var, Y, A, k=1)
598	        elif topology == 'exposure':
599	            b, _ = ols_no_T(Y, A, K)
600	            th = b[1]
601	        else:
602	            b, _ = ols_with_dummies(Y, first_var, A, K)
603	            th = b[1]
604	        if np.isfinite(th):
605	            tau_hats.append(th)
606	    return float(np.std(tau_hats)) if len(tau_hats) > 2 else np.nan
607	
608	
609	def compute_all_asvs(confusion_matrices, all_suff_stats, all_tau_true, all_se_ref):
610	    results = []
611	    for (dataset, model, prompt), C in confusion_matrices.items():
612	        K = DATASETS[dataset]['K']
613	        for topology in TOPOLOGIES:
614	            st = all_suff_stats[(K, topology)]
615	            tau_true = all_tau_true[(K, topology)]
616	            se_ref = all_se_ref.get((K, topology))
617	            for asv_type in ['magnitude', 'significance', 'sign_flip']:
618	                asv = compute_asv_for_matrix(C, K, topology, st, tau_true,
619	                                             asv_type, se_ref=se_ref)
620	                results.append({
621	                    'dataset': dataset, 'model': model, 'prompt': prompt,
622	                    'K': K, 'topology': topology, 'asv_type': asv_type,
623	                    'asv': asv,
624	                })
625	    return results
626	
627	
628	# ============================================================================
629	# 4. F1 vs Downstream Bias
630	# ============================================================================
631	
632	def compute_f1_from_C(C, K, p_A=None):
633	    if p_A is None:
634	        p_A = np.ones(K) / K
635	    precision = np.zeros(K)
636	    recall = np.zeros(K)
637	    f1 = np.zeros(K)
638	    for i in range(K):
639	        recall[i] = C[i, i]
640	        denom = sum(C[i, j] * p_A[j] for j in range(K))
641	        precision[i] = C[i, i] * p_A[i] / denom if denom > 1e-12 else 0
642	        if precision[i] + recall[i] > 1e-12:
643	            f1[i] = 2 * precision[i] * recall[i] / (precision[i] + recall[i])
644	    return {
645	        'macro_f1': float(f1.mean()),
646	        'weighted_f1': float((p_A * f1).sum()),
647	        'per_class_f1': f1.tolist(),
648	    }
649	
650	
651	def f1_vs_bias_analysis(confusion_matrices, biases):
652	    results = []
653	    for b in biases:
654	        key = (b['dataset'], b['model'], b['prompt'])
655	        if key not in confusion_matrices:
656	            continue
657	        C = confusion_matrices[key]
658	        K = b['K']
659	        p_A = make_p_A(K)
660	        f1_info = compute_f1_from_C(C, K, p_A)
661	        abs_bias = abs(b['bias']) if b['bias'] is not None else None
662	        results.append({
663	            'dataset': b['dataset'], 'model': b['model'], 'prompt': b['prompt'],
664	            'K': K, 'topology': b['topology'],
665	            'macro_f1': f1_info['macro_f1'], 'weighted_f1': f1_info['weighted_f1'],
666	            'abs_bias': abs_bias, 'bias_pct': b['bias_pct'],
667	            'sign_flip': b['sign_flip'],
668	        })
669	    return results
670	
671	
672	# ============================================================================
673	# 5. Type I/II Error Rates
674	# ============================================================================
675	
676	def compute_type1_type2_for_C(C, K, topology, params_H1, params_H0,
677	                              st_H1, tau_true,
678	                              n_sim=100, N_sample=5000, seed=42):
679	    gen_fn = GEN_FNS[topology]
680	    rng = np.random.default_rng(seed)
681	
682	    masv = compute_asv_for_matrix(C, K, topology, st_H1, tau_true, 'magnitude')
683	    asv_safe = (masv is None or masv > 1.0)
684	
685	    def _run_mc(params_t, n):
686	        valid = 0; rej = 0
687	        for _ in range(n):
688	            fv, Y, A = gen_fn(K, N_sample, params_t, rng)
689	            Astar = generate_Astar(A, C, rng)
690	            if topology == 'iv':
691	                th, se = wald_estimator(fv, Y, Astar, k=1)
692	            elif topology == 'exposure':
693	                b, svec = ols_no_T(Y, Astar, K)
694	                th, se = b[1], svec[1]
695	            else:
696	                b, svec = ols_with_dummies(Y, fv, Astar, K)
697	                th, se = b[1], svec[1]
698	            if np.isfinite(th) and np.isfinite(se) and se > 1e-10:
699	                valid += 1
700	                if abs(th / se) > 1.96:
701	                    rej += 1
702	        return rej / max(valid, 1), valid
703	
704	    type1_before, v0 = _run_mc(params_H0[topology], n_sim)
705	    power_before, v1 = _run_mc(params_H1[topology], n_sim)
706	    type1_after = type1_before if asv_safe else 0.0
707	    power_after = power_before if asv_safe else 0.0
708	
709	    return {
710	        'type1_before': float(type1_before), 'type1_after': float(type1_after),
711	        'power_before': float(power_before), 'power_after': float(power_after),
712	        'asv_safe': bool(asv_safe), 'magnitude_asv': masv,
713	        'valid_h0': int(v0), 'valid_h1': int(v1),
714	    }
715	
716	
717	# ============================================================================
718	# 6. Inter-model Error Correlation
719	# ============================================================================
720	
721	def compute_inter_model_correlation(confusion_matrices, K, dataset, prompt,
722	                                    n_samples=1000, seed=42):
723	    rng = np.random.default_rng(seed)
724	    p_A = make_p_A(K)
725	    true_labels = rng.choice(K, size=n_samples, p=p_A)
726	
727	    predictions = {}
728	    for model in MODELS:
729	        key = (dataset, model, prompt)
730	        if key in confusion_matrices:
731	            predictions[model] = generate_Astar(true_labels,
732	                                                confusion_matrices[key], rng)
733	        else:
734	            predictions[model] = true_labels.copy()
735	
736	    pairs = [(MODELS[i], MODELS[j]) for i in range(3) for j in range(i + 1, 3)]
737	    results = {}
738	    for m1, m2 in pairs:
739	        p1, p2 = predictions[m1], predictions[m2]
740	        agreement = float((p1 == p2).mean())
741	        observed = agreement
742	        expected = sum((p1 == c).mean() * (p2 == c).mean() for c in range(K))
743	        kappa = float((observed - expected) / (1 - expected)
744	                      ) if expected < 1 - 1e-10 else 0.0
745	        err1 = (p1 != true_labels).astype(float)
746	        err2 = (p2 != true_labels).astype(float)
747	        if err1.std() > 1e-10 and err2.std() > 1e-10:
748	            error_corr = float(np.corrcoef(err1, err2)[0, 1])
749	        else:
750	            error_corr = 0.0
751	        results[f"{m1}-{m2}"] = {
752	            'agreement': agreement,
753	            'kappa': kappa,
754	            'error_correlation': error_corr if np.isfinite(error_corr) else 0.0,
755	        }
756	    return results
757	
758	
759	# ============================================================================
760	# Mock Data Generation
761	# ============================================================================
762	
763	def generate_mock_C(K, rng, diag_range):
764	    C = np.zeros((K, K))
765	    for j in range(K):
766	        diag_val = rng.uniform(diag_range[0], diag_range[1])
767	        remaining = 1.0 - diag_val
768	        if K > 2:
769	            dists = np.abs(np.arange(K) - j).astype(float)
770	            dists[j] = np.inf
771	            weights = 1.0 / dists
772	            weights[j] = 0
773	            noise = rng.uniform(0.5, 1.5, K)
774	            noise[j] = 0
775	            weights = weights * noise
776	            weights /= weights.sum()
777	            C[:, j] = remaining * weights
778	        else:
779	            C[1 - j, j] = remaining
780	        C[j, j] = diag_val
781	    return C
782	
783	
784	def generate_mock_confusion_matrices(seed=12345):
785	    rng = np.random.default_rng(seed)
786	    matrices = {}
787	    diag_ranges = {
788	        'civil_comments': (0.85, 0.95),
789	        'vast': (0.70, 0.90),
790	        'humaid': (0.60, 0.85),
791	    }
792	    for dataset, info in DATASETS.items():
793	        K = info['K']
794	        dr = diag_ranges[dataset]
795	        for model in MODELS:
796	            for prompt in PROMPTS:
797	                matrices[(dataset, model, prompt)] = generate_mock_C(K, rng, dr)
798	    return matrices
799	
800	
801	# ============================================================================
802	# Diagnostic Plots (optional)
803	# ============================================================================
804	
805	def save_f1_vs_bias_plot(f1_bias, output_dir):
806	    if not HAS_MPL:
807	        return
808	    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
809	    axes = axes.flatten()
810	    for idx, topo in enumerate(TOPOLOGIES):
811	        ax = axes[idx]
812	        subset = [r for r in f1_bias if r['topology'] == topo
813	                  and r['abs_bias'] is not None]
814	        if not subset:
815	            ax.set_title(topo)
816	            continue
817	        f1s = [r['macro_f1'] for r in subset]
818	        biases = [r['abs_bias'] for r in subset]
819	        colors = ['red' if r['sign_flip'] else 'steelblue' for r in subset]
820	        ax.scatter(f1s, biases, c=colors, alpha=0.7, s=30)
821	        ax.axvline(0.93, color='gray', linestyle='--', alpha=0.5)
822	        ax.set_xlabel('Macro F1')
823	        ax.set_ylabel('|bias|')
824	        ax.set_title(topo)
825	    if len(TOPOLOGIES) < 8:
826	        axes[-1].axis('off')
827	    fig.suptitle('F1 vs |Downstream Bias| (red=sign flip)', fontsize=14)
828	    fig.tight_layout(rect=[0, 0, 1, 0.96])
829	    fig.savefig(os.path.join(output_dir, 'f1_vs_bias.png'), dpi=150)
830	    plt.close(fig)
831	
832	
833	def save_asv_heatmap(asvs, output_dir):
834	    if not HAS_MPL:
835	        return
836	    mag_asvs = [r for r in asvs if r['asv_type'] == 'magnitude']
837	    datasets_list = list(DATASETS.keys())
838	    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
839	    for didx, dataset in enumerate(datasets_list):
840	        ax = axes[didx]
841	        subset = [r for r in mag_asvs if r['dataset'] == dataset]
842	        configs = sorted(set((r['model'], r['prompt']) for r in subset))
843	        grid = np.full((len(TOPOLOGIES), len(configs)), np.nan)
844	        for r in subset:
845	            ti = TOPOLOGIES.index(r['topology'])
846	            ci = configs.index((r['model'], r['prompt']))
847	            grid[ti, ci] = r['asv'] if r['asv'] is not None else np.nan
848	        im = ax.imshow(grid, cmap='RdYlGn', aspect='auto',
849	                       vmin=0, vmax=2)
850	        ax.set_xticks(range(len(configs)))
851	        ax.set_xticklabels([f"{m[:3]}_{p[:3]}" for m, p in configs],
852	                           rotation=45, ha='right', fontsize=7)
853	        ax.set_yticks(range(len(TOPOLOGIES)))
854	        ax.set_yticklabels(TOPOLOGIES, fontsize=8)
855	        ax.set_title(f'{dataset} (K={DATASETS[dataset]["K"]})')
856	        plt.colorbar(im, ax=ax, shrink=0.8)
857	    fig.suptitle('Magnitude ASV (green=safe, red=fragile)', fontsize=14)
858	    fig.tight_layout(rect=[0, 0, 1, 0.96])
859	    fig.savefig(os.path.join(output_dir, 'asv_heatmap.png'), dpi=150)
860	    plt.close(fig)
861	
862	
863	# ============================================================================
864	# JSON Serialization
865	# ============================================================================
866	
867	def _to_json_safe(obj):
868	    if isinstance(obj, np.integer):
869	        return int(obj)
870	    elif isinstance(obj, np.floating):
871	        v = float(obj)
872	        return None if (np.isnan(v) or np.isinf(v)) else v
873	    elif isinstance(obj, np.ndarray):
874	        return _to_json_safe(obj.tolist())
875	    elif isinstance(obj, dict):
876	        return {str(k): _to_json_safe(v) for k, v in obj.items()}
877	    elif isinstance(obj, list):
878	        return [_to_json_safe(v) for v in obj]
879	    elif isinstance(obj, (bool, np.bool_)):
880	        return bool(obj)
881	    elif isinstance(obj, float):
882	        return None if (np.isnan(obj) or np.isinf(obj)) else obj
883	    return obj
884	
885	
886	# ============================================================================
887	# Main
888	# ============================================================================
889	
890	def main():
891	    parser = argparse.ArgumentParser(description='plan_006: Empirical ASV calibration')
892	    parser.add_argument('--data-dir', default='data/')
893	    parser.add_argument('--output-dir', default='artifacts/plan006/')
894	    parser.add_argument('--mock', action='store_true', help='Use mock data for dry-run')
895	    parser.add_argument('--datasets', type=str, default=None,
896	                        help='Comma-separated dataset filter (e.g. humaid,vast)')
897	    parser.add_argument('--n-sim', type=int, default=1000)
898	    parser.add_argument('--device', type=str, default='cpu')
899	    args = parser.parse_args()
900	
901	    os.makedirs(args.output_dir, exist_ok=True)
902	    t_total = time.time()
903	    n_precomp = 500_000 if args.mock else N_PRECOMP
904	
905	    dataset_filter = None
906	    if args.datasets:
907	        dataset_filter = [d.strip() for d in args.datasets.split(',')]
908	
909	    print("=" * 70)
910	    print("plan_006: Empirical ASV Calibration")
911	    if dataset_filter:
912	        print(f"  Dataset filter: {dataset_filter}")
913	    print("=" * 70)
914	
915	    # --- 1. Confusion matrices ---
916	    if args.mock:
917	        print("\n[1/6] Generating mock confusion matrices...")
918	        confusion_matrices = generate_mock_confusion_matrices()
919	        if dataset_filter:
920	            confusion_matrices = {k: v for k, v in confusion_matrices.items()
921	                                  if k[0] in dataset_filter}
922	    else:
923	        print("\n[1/6] Loading confusion matrices...")
924	        confusion_matrices = load_all_confusion_matrices(args.data_dir,
925	                                                         dataset_filter=dataset_filter)
926	
927	    print(f"  {len(confusion_matrices)} matrices loaded")
928	    for (ds, m, p), C in list(confusion_matrices.items())[:3]:
929	        K = DATASETS[ds]['K']
930	        print(f"    {ds}/{m}/{p}: K={K}, diag_mean={np.diag(C).mean():.3f}")
931	
932	    # --- 2. Precompute sufficient statistics ---
933	    print("\n[2/6] Precomputing sufficient statistics...")
934	    active_datasets = dataset_filter if dataset_filter else list(DATASETS.keys())
935	    K_values = sorted(set(DATASETS[ds]['K'] for ds in active_datasets if ds in DATASETS))
936	    all_suff_stats = {}
937	    all_tau_true = {}
938	    all_params = {}
939	    all_params_H0 = {}
940	    all_se_ref = {}
941	
942	    for K in K_values:
943	        params = make_dgp_params(K)
944	        params_H0 = make_dgp_params_H0(K, params)
945	        all_params[K] = params
946	        all_params_H0[K] = params_H0
947	        for topology in TOPOLOGIES:
948	            seed = K * 1000 + abs(hash(topology)) % 1000
949	            st = precompute_suff_stats(K, topology, params[topology],
950	                                       N=n_precomp, seed=seed)
951	            plim_I = compute_plim(np.eye(K), st, K)
952	            tau_true = extract_tau(plim_I, topology)
953	            all_suff_stats[(K, topology)] = st
954	            all_tau_true[(K, topology)] = tau_true
955	
956	            se = estimate_reference_se(K, topology, params[topology],
957	                                       N_ref=5000,
958	                                       n_mc=min(args.n_sim, 30),
959	                                       seed=seed + 500)
960	            all_se_ref[(K, topology)] = se
961	            se_s = f"{se:.4f}" if np.isfinite(se) else "N/A"
962	            print(f"    K={K:>2} {topology:<13} tau_true={tau_true:>9.6f}  SE_ref={se_s}")
963	
964	    biases = compute_all_biases(confusion_matrices, all_suff_stats, all_tau_true)
965	    n_sign_flips = sum(1 for b in biases if b['sign_flip'])
966	    print(f"  {len(biases)} bias values ({n_sign_flips} sign flips)")
967	
968	    # --- 3. ASV ---
969	    print("\n[3/6] Computing ASV values...")
970	    t3 = time.time()
971	    asvs = compute_all_asvs(confusion_matrices, all_suff_stats,
972	                            all_tau_true, all_se_ref)
973	    print(f"  {len(asvs)} ASV values ({time.time() - t3:.1f}s)")
974	    for at in ['magnitude', 'sign_flip', 'significance']:
975	        sub = [r['asv'] for r in asvs if r['asv_type'] == at and r['asv'] is not None]
976	        if sub:
977	            print(f"    {at}: min={min(sub):.3f} median={np.median(sub):.3f} "
978	                  f"max={max(sub):.3f} ({len(sub)} non-None)")
979	
980	    # --- 4. F1 vs bias ---
981	    print("\n[4/6] F1 vs bias analysis...")
982	    f1_bias = f1_vs_bias_analysis(confusion_matrices, biases)
983	    total_high_f1 = [r for r in f1_bias if r['macro_f1'] is not None and r['macro_f1'] > 0.93]
984	    high_f1_high_bias = [r for r in total_high_f1
985	                         if r['abs_bias'] is not None and r['abs_bias'] > 0.05]
986	    if total_high_f1:
987	        pct = len(high_f1_high_bias) / len(total_high_f1) * 100
988	        print(f"  Baumann check: F1>0.93 with |bias|>0.05: "
989	              f"{len(high_f1_high_bias)}/{len(total_high_f1)} = {pct:.1f}%")
990	    # Sample rows
991	    for r in f1_bias[:3]:
992	        print(f"    {r['dataset']}/{r['model']}/{r['prompt']} {r['topology']}: "
993	              f"F1={r['macro_f1']:.3f} |bias|={r['abs_bias']}")
994	
995	    # --- 5. Type I/II ---
996	    print("\n[5/6] Type I/II error rates...")
997	    t5 = time.time()
998	    type1_type2_results = []
999	    n_configs = len(confusion_matrices) * len(TOPOLOGIES)
1000	    idx = 0
1001	    for (dataset, model, prompt), C in confusion_matrices.items():
1002	        K = DATASETS[dataset]['K']
1003	        for topology in TOPOLOGIES:
1004	            idx += 1
1005	            st = all_suff_stats[(K, topology)]
1006	            tau_true = all_tau_true[(K, topology)]
1007	            r = compute_type1_type2_for_C(
1008	                C, K, topology, all_params[K], all_params_H0[K],
1009	                st, tau_true,
1010	                n_sim=args.n_sim, N_sample=5000, seed=idx * 100)
1011	            type1_type2_results.append({
1012	                'dataset': dataset, 'model': model, 'prompt': prompt,
1013	                'K': K, 'topology': topology, **r,
1014	            })
1015	            if idx % 50 == 0:
1016	                print(f"    {idx}/{n_configs}...")
1017	    print(f"  {len(type1_type2_results)} records ({time.time() - t5:.1f}s)")
1018	    unsafe = sum(1 for r in type1_type2_results if not r['asv_safe'])
1019	    print(f"  ASV-unsafe: {unsafe}/{len(type1_type2_results)}")
1020	
1021	    # --- 6. Inter-model correlation ---
1022	    print("\n[6/6] Inter-model error correlation...")
1023	    inter_model_results = {}
1024	    for dataset in DATASETS:
1025	        K = DATASETS[dataset]['K']
1026	        for prompt in PROMPTS:
1027	            r = compute_inter_model_correlation(
1028	                confusion_matrices, K, dataset, prompt,
1029	                n_samples=1000, seed=abs(hash((dataset, prompt))) % 10000)
1030	            inter_model_results[f"{dataset}_{prompt}"] = r
1031	    print(f"  {len(inter_model_results)} (dataset, prompt) pairs")
1032	    for key, pairs in list(inter_model_results.items())[:2]:
1033	        for pair, vals in pairs.items():
1034	            print(f"    {key} {pair}: agree={vals['agreement']:.3f} "
1035	                  f"kappa={vals['kappa']:.3f} err_corr={vals['error_correlation']:.3f}")
1036	
1037	    # --- Summary ---
1038	    summary = {
1039	        'f1_gt_093_total': len(total_high_f1),
1040	        'f1_gt_093_with_high_bias_pct': (
1041	            len(high_f1_high_bias) / max(len(total_high_f1), 1) * 100),
1042	        'ppi_recommended_scenarios': unsafe,
1043	        'total_scenarios': len(type1_type2_results),
1044	        'ppi_recommended_pct': unsafe / max(len(type1_type2_results), 1) * 100,
1045	    }
1046	
1047	    # --- Save ---
1048	    output = _to_json_safe({
1049	        'confusion_matrices': {
1050	            f"{ds}_{m}_{p}": C.tolist()
1051	            for (ds, m, p), C in confusion_matrices.items()
1052	        },
1053	        'biases': biases,
1054	        'asvs': asvs,
1055	        'f1_vs_bias': f1_bias,
1056	        'type1_type2': type1_type2_results,
1057	        'inter_model_correlation': inter_model_results,
1058	        'summary': summary,
1059	    })
1060	
1061	    out_path = os.path.join(args.output_dir, 'asv_empirical_results.json')
1062	    with open(out_path, 'w') as f:
1063	        json.dump(output, f, indent=2, default=str)
1064	    print(f"\nResults saved to {out_path}")
1065	
1066	    # --- Plots ---
1067	    save_f1_vs_bias_plot(f1_bias, args.output_dir)
1068	    save_asv_heatmap(asvs, args.output_dir)
1069	    if HAS_MPL:
1070	        print(f"Plots saved to {args.output_dir}")
1071	
1072	    # --- Validation ---
1073	    with open(out_path) as f:
1074	        data = json.load(f)
1075	    n_null = str(data).count('null')
1076	    print(f"\nValidation: JSON has {n_null} null values "
1077	          f"(expected for NaN/None ASV entries)")
1078	    for section in ['biases', 'asvs', 'f1_vs_bias', 'type1_type2']:
1079	        print(f"  {section}: {len(data[section])} records")
1080	
1081	    elapsed = time.time() - t_total
1082	    print(f"\nTotal time: {elapsed:.1f}s ({elapsed / 60:.1f}min)")
1083	    print(f"\nSummary:")
1084	    print(f"  F1>0.93 with high bias: {summary['f1_gt_093_with_high_bias_pct']:.1f}%")
1085	    print(f"  PPI++ recommended: {summary['ppi_recommended_scenarios']}/"
1086	          f"{summary['total_scenarios']} ({summary['ppi_recommended_pct']:.1f}%)")
1087	    print("=" * 70)
1088	
1089	
1090	if __name__ == "__main__":
1091	    main()
1092	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b1ff72f-e74f-4339-b03e-e10167c8be1c",
  "isSidechain": true,
  "promptId": "221cc120-ad2a-4ac2-82b3-5f678194e371",
  "agentId": "a345197f572e1e9bc",
  "type": "user",
  "uuid": "ac777524-4313-4c3f-8bc3-bd91da9801a6",
  "sourceToolAssistantUUID": "6b1ff72f-e74f-4339-b03e-e10167c8be1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-23T00:19:14.430Z_

Now I have a thorough understanding of the code. Let me also look at some of the existing experiment scripts for pattern reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac777524-4313-4c3f-8bc3-bd91da9801a6",
  "isSidechain": true,
  "agentId": "a345197f572e1e9bc",
  "requestId": "req_011CbJYP7Ln5auHnHPdGig5X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36d38d8e-658d-4260-b841-0a80eaa7f60d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Szp81YW7p7zZZCGYZeinTy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17392,
      "cache_read_input_tokens": 32229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17392,
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

_source line 11 · 2026-05-23T00:19:16.380Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ek7fwGwPT4uQcpyHb2k5nW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test.py",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36d38d8e-658d-4260-b841-0a80eaa7f60d",
  "isSidechain": true,
  "agentId": "a345197f572e1e9bc",
  "requestId": "req_011CbJYP7Ln5auHnHPdGig5X",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "27f614e0-3478-4cbc-9c81-4258945c2dbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Szp81YW7p7zZZCGYZeinTy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17392,
      "cache_read_input_tokens": 32229,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 32229,
          "cache_creation_input_tokens": 17392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17392,
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

_source line 12 · 2026-05-23T00:19:16.393Z_

<details><summary>↩ Tool result · `toolu_01Ek7fwGwPT4uQcpyHb2k5nW`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Exp-A: Non-differential Misclassification Stress Test Expansion
4	
5	Tests sign flip rate and bias ratio under increasing differential
6	misclassification departure ε.
7	
8	4 topologies × 2 K × 3 CM qualities × 4 ε = 96 configs
9	N=10,000 × 100 MC reps per config
10	"""
11	import numpy as np
12	import json
13	import time
14	import os
15	
16	TOPOLOGIES = ['confounding', 'mediation', 'exposure', 'iv']
17	K_VALUES = [3, 10]
18	EPSILONS = [0.0, 0.01, 0.05, 0.10]
19	CM_QUALS = {'high': 0.8, 'medium': 0.6, 'low': 0.4}
20	N_SAMPLES = 10_000
21	N_REPS = 100
22	N_LARGE = 2_000_000
23	SEED = 42
24	
25	_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]
26	_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
27	_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
28	_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
29	_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]
30	
31	
32	def softmax_rows(x):
33	    e = np.exp(x - x.max(axis=1, keepdims=True))
34	    return e / e.sum(axis=1, keepdims=True)
35	
36	
37	def sample_cat(probs, rng):
38	    cum = np.cumsum(probs, axis=1)
39	    u = rng.uniform(size=probs.shape[0])[:, None]
40	    return (u >= cum[:, :-1]).sum(axis=1).astype(int)
41	
42	
43	def make_p_A(K):
44	    if K == 3:
45	        return np.array([0.40, 0.35, 0.25])
46	    raw = np.array([1.0 / (i + 1) for i in range(K)])
47	    return raw / raw.sum()
48	
49	
50	def make_dgp_params(K):
51	    p_A = make_p_A(K)
52	    params = {
53	        'confounding': {
54	            'p_A': p_A, 'alpha': np.array(_ALPHA_POOL[:K-1]),
55	            'beta_A': np.array(_BETA_A_POOL[:K-1]),
56	            'beta_T': 2.0, 'sigma_T': 1.0,
57	        },
58	        'mediation': {
59	            'tau': 0.5, 'gamma': np.array(_GAMMA_POOL[:K]),
60	            'delta': np.array(_DELTA_POOL[:K]),
61	            'beta': np.array(_BETA_POOL[:K]),
62	        },
63	        'exposure': {'beta': np.array(_BETA_POOL[:K]), 'p_A': p_A},
64	    }
65	    if K == 3:
66	        params['iv'] = {
67	            'lam': 1.0, 'beta': np.array([0.0, 0.5, -0.25]),
68	            'g': np.zeros(3), 'dZ': np.array([0.0, 1.0, -0.5]),
69	            'dU': np.array([0.0, 0.8, 0.6]),
70	        }
71	    else:
72	        iv_b = np.array(_BETA_POOL[:K]) * 0.5
73	        iv_b[0] = 0.0
74	        params['iv'] = {
75	            'lam': 1.0, 'beta': iv_b, 'g': np.zeros(K),
76	            'dZ': np.array([0.0] + [_ALPHA_POOL[i]*0.7 for i in range(K-1)]),
77	            'dU': np.array([0.0] + [_BETA_A_POOL[i]*0.6 for i in range(K-1)]),
78	        }
79	    return params
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27f614e0-3478-4cbc-9c81-4258945c2dbf",
  "isSidechain": true,
  "promptId": "221cc120-ad2a-4ac2-82b3-5f678194e371",
  "agentId": "a345197f572e1e9bc",
  "type": "user",
  "uuid": "5a556466-6636-470e-8a25-ffc407acdd58",
  "sourceToolAssistantUUID": "27f614e0-3478-4cbc-9c81-4258945c2dbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-23T00:19:19.817Z_

Now I understand the structure. Let me look at what the exposure topology's `compute_plim` returns more closely—it returns a K-length vector (intercept + K-1 dummy coefficients).

Let me now create the script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a556466-6636-470e-8a25-ffc407acdd58",
  "isSidechain": true,
  "agentId": "a345197f572e1e9bc",
  "requestId": "req_011CbJYPRWAqXB9WF4Mg3jCC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ba09150-d302-42b5-a9ed-5492e9896a75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JChA9QCYF82HM76EkuYrXn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1531,
      "cache_read_input_tokens": 49621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1531,
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

_source line 14 · 2026-05-23T00:20:32.046Z_

<details open><summary>🔧 Tool call — Write · `toolu_012RQ7V1JmPnqBBZafbskiq7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_primary_coeff_breakdown.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nExp: Primary Coefficient Sign Reversal Analysis for Exposure Topology\n\nFor the exposure topology with K=3, the OLS regression is:\n    Y = β₀ + β₁·1[A*=1] + β₂·1[A*=2] + ε\n\nThe paper claims \"the primary coefficient never reverses sign\" based on\nempirical LLM confusion matrices.  This script verifies that claim\nsystematically by:\n\n1. Varying the β₁/β₂ ratio (from equal to highly imbalanced)\n2. For each ratio, sampling 100,000 Dirichlet(1,1,1) confusion matrices\n3. Computing the analytical probability limit of each coefficient\n4. Checking sign reversal for the PRIMARY coefficient (the largest |βₖ|)\n   vs SECONDARY coefficients\n5. Also checking with a \"realistic\" filter: diagonal ≥ 0.7\n\nOutput: artifacts/exp_primary_coeff_breakdown_results.json\n\nKey imports from plan_006_asv_empirical.py:\n  - make_dgp_params(K): generates DGP parameters\n  - precompute_suff_stats(K, topo, params): precomputes sufficient statistics\n  - compute_plim(C, suff_stats, K): analytical probability limit given C\n\"\"\"\n\nimport numpy as np\nimport json\nimport time\nimport sys\nimport os\n\n# Add project root to path so we can import from plan_006\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n\nfrom plan_006_asv_empirical import (\n    make_dgp_params,\n    precompute_suff_stats,\n    compute_plim,\n    make_p_A,\n)\n\n# ============================================================================\n# Configuration\n# ============================================================================\n\nK = 3\nN_MATRICES = 100_000\nBETA_RATIOS = [1.0, 1.5, 2.0, 5.0, 10.0, 50.0]\nDIAG_THRESHOLD = 0.7  # \"realistic\" confusion matrix filter\nN_PRECOMP = 2_000_000\nSEED = 2026\n\n\n# ============================================================================\n# Core Analysis\n# ============================================================================\n\ndef make_exposure_params_custom(K, beta_vec, p_A):\n    \"\"\"Create exposure DGP params with a custom beta vector.\"\"\"\n    return {\n        'beta': np.array(beta_vec),\n        'p_A': p_A,\n    }\n\n\ndef sample_dirichlet_confusion_matrices(K, n_matrices, rng):\n    \"\"\"\n    Sample n_matrices confusion matrices where each column is drawn\n    independently from Dirichlet(1,1,...,1) (uniform over the simplex).\n\n    Returns: array of shape (n_matrices, K, K)\n    \"\"\"\n    # Each column j of C is drawn from Dirichlet(alpha=[1]*K)\n    # Shape: (n_matrices, K, K) where C[:, :, j] are the columns\n    alpha = np.ones(K)\n    matrices = np.zeros((n_matrices, K, K))\n    for j in range(K):\n        # Draw n_matrices columns from Dirichlet\n        matrices[:, :, j] = rng.dirichlet(alpha, size=n_matrices)\n    return matrices\n\n\ndef analyze_single_ratio(ratio, rng, verbose=True):\n    \"\"\"\n    For a given β₁/β₂ ratio, compute sign-flip statistics.\n\n    β = [0.0, β₁, β₂] where β₁ = 1.0 and β₂ = 1.0/ratio.\n    The primary coefficient is β₁ (index 1 in the plim vector).\n    The secondary coefficient is β₂ (index 2 in the plim vector).\n\n    Returns a dict with sign-flip counts and rates.\n    \"\"\"\n    beta_1 = 1.0\n    beta_2 = 1.0 / ratio\n    beta_vec = [0.0, beta_1, beta_2]\n    p_A = make_p_A(K)\n\n    # Create custom exposure params\n    exp_params = make_exposure_params_custom(K, beta_vec, p_A)\n\n    # Precompute sufficient statistics with these params\n    suff_stats = precompute_suff_stats(\n        K, 'exposure', exp_params, N=N_PRECOMP, seed=int(ratio * 1000) % 99999\n    )\n\n    # Verify: plim with identity C should recover true beta\n    plim_identity = compute_plim(np.eye(K), suff_stats, K)\n    if verbose:\n        print(f\"  True β = {beta_vec}\")\n        print(f\"  Plim(I) = {plim_identity}\")\n\n    # Sample confusion matrices\n    C_all = sample_dirichlet_confusion_matrices(K, N_MATRICES, rng)\n\n    # Counters\n    primary_sign_flip_all = 0\n    secondary_sign_flip_all = 0\n    any_sign_flip_all = 0\n    primary_sign_flip_diag = 0\n    secondary_sign_flip_diag = 0\n    any_sign_flip_diag = 0\n    n_valid_all = 0\n    n_valid_diag = 0\n    n_diag_pass = 0\n\n    # Track worst-case (most negative primary plim)\n    worst_primary_plim = float('inf')\n    worst_primary_C = None\n    worst_secondary_plim = float('inf')\n    worst_secondary_C = None\n\n    # Collect plim values for summary stats\n    primary_plims = []\n    secondary_plims = []\n\n    for i in range(N_MATRICES):\n        C = C_all[i]\n\n        # Compute plim: returns [intercept, coeff_1, coeff_2] for exposure\n        plim_vec = compute_plim(C, suff_stats, K)\n\n        if isinstance(plim_vec, float) or not np.all(np.isfinite(plim_vec)):\n            continue\n\n        n_valid_all += 1\n\n        # plim_vec layout for exposure: [β₀_hat, β₁_hat, β₂_hat]\n        # True signs: β₁ = 1.0 > 0, β₂ = 1.0/ratio > 0\n        beta1_hat = plim_vec[1]  # primary coefficient\n        beta2_hat = plim_vec[2]  # secondary coefficient\n\n        primary_plims.append(beta1_hat)\n        secondary_plims.append(beta2_hat)\n\n        # Check sign reversal (true signs are both positive)\n        primary_flipped = (beta1_hat < 0)\n        secondary_flipped = (beta2_hat < 0)\n\n        if primary_flipped:\n            primary_sign_flip_all += 1\n            if beta1_hat < worst_primary_plim:\n                worst_primary_plim = beta1_hat\n                worst_primary_C = C.copy()\n        if secondary_flipped:\n            secondary_sign_flip_all += 1\n            if beta2_hat < worst_secondary_plim:\n                worst_secondary_plim = beta2_hat\n                worst_secondary_C = C.copy()\n        if primary_flipped or secondary_flipped:\n            any_sign_flip_all += 1\n\n        # Check with diagonal threshold\n        min_diag = np.min(np.diag(C))\n        if min_diag >= DIAG_THRESHOLD:\n            n_diag_pass += 1\n            n_valid_diag += 1\n            if primary_flipped:\n                primary_sign_flip_diag += 1\n            if secondary_flipped:\n                secondary_sign_flip_diag += 1\n            if primary_flipped or secondary_flipped:\n                any_sign_flip_diag += 1\n\n    primary_plims = np.array(primary_plims)\n    secondary_plims = np.array(secondary_plims)\n\n    result = {\n        'ratio': ratio,\n        'beta': beta_vec,\n        'n_matrices': N_MATRICES,\n        'n_valid_all': n_valid_all,\n        'n_diag_pass': n_diag_pass,\n        # All matrices\n        'primary_sign_flip_all': primary_sign_flip_all,\n        'primary_sign_flip_rate_all': primary_sign_flip_all / max(n_valid_all, 1),\n        'secondary_sign_flip_all': secondary_sign_flip_all,\n        'secondary_sign_flip_rate_all': secondary_sign_flip_all / max(n_valid_all, 1),\n        'any_sign_flip_all': any_sign_flip_all,\n        'any_sign_flip_rate_all': any_sign_flip_all / max(n_valid_all, 1),\n        # Diagonal >= 0.7\n        'primary_sign_flip_diag': primary_sign_flip_diag,\n        'primary_sign_flip_rate_diag': (\n            primary_sign_flip_diag / max(n_valid_diag, 1) if n_valid_diag > 0 else None\n        ),\n        'secondary_sign_flip_diag': secondary_sign_flip_diag,\n        'secondary_sign_flip_rate_diag': (\n            secondary_sign_flip_diag / max(n_valid_diag, 1) if n_valid_diag > 0 else None\n        ),\n        'any_sign_flip_diag': any_sign_flip_diag,\n        'any_sign_flip_rate_diag': (\n            any_sign_flip_diag / max(n_valid_diag, 1) if n_valid_diag > 0 else None\n        ),\n        # Summary statistics on plim values\n        'primary_plim_stats': {\n            'mean': float(np.mean(primary_plims)) if len(primary_plims) > 0 else None,\n            'std': float(np.std(primary_plims)) if len(primary_plims) > 0 else None,\n            'min': float(np.min(primary_plims)) if len(primary_plims) > 0 else None,\n            'p5': float(np.percentile(primary_plims, 5)) if len(primary_plims) > 0 else None,\n            'p25': float(np.percentile(primary_plims, 25)) if len(primary_plims) > 0 else None,\n            'median': float(np.median(primary_plims)) if len(primary_plims) > 0 else None,\n            'p75': float(np.percentile(primary_plims, 75)) if len(primary_plims) > 0 else None,\n            'p95': float(np.percentile(primary_plims, 95)) if len(primary_plims) > 0 else None,\n            'max': float(np.max(primary_plims)) if len(primary_plims) > 0 else None,\n        },\n        'secondary_plim_stats': {\n            'mean': float(np.mean(secondary_plims)) if len(secondary_plims) > 0 else None,\n            'std': float(np.std(secondary_plims)) if len(secondary_plims) > 0 else None,\n            'min': float(np.min(secondary_plims)) if len(secondary_plims) > 0 else None,\n            'p5': float(np.percentile(secondary_plims, 5)) if len(secondary_plims) > 0 else None,\n            'p25': float(np.percentile(secondary_plims, 25)) if len(secondary_plims) > 0 else None,\n            'median': float(np.median(secondary_plims)) if len(secondary_plims) > 0 else None,\n            'p75': float(np.percentile(secondary_plims, 75)) if len(secondary_plims) > 0 else None,\n            'p95': float(np.percentile(secondary_plims, 95)) if len(secondary_plims) > 0 else None,\n            'max': float(np.max(secondary_plims)) if len(secondary_plims) > 0 else None,\n        },\n        # Worst cases\n        'worst_primary_plim': (\n            float(worst_primary_plim) if worst_primary_plim != float('inf') else None\n        ),\n        'worst_primary_C': (\n            worst_primary_C.tolist() if worst_primary_C is not None else None\n        ),\n        'worst_secondary_plim': (\n            float(worst_secondary_plim) if worst_secondary_plim != float('inf') else None\n        ),\n        'worst_secondary_C': (\n            worst_secondary_C.tolist() if worst_secondary_C is not None else None\n        ),\n    }\n\n    return result\n\n\n# ============================================================================\n# Main\n# ============================================================================\n\ndef main():\n    t_start = time.time()\n    print(\"=\" * 70)\n    print(\"Primary Coefficient Sign Reversal Analysis — Exposure Topology K=3\")\n    print(f\"  N_MATRICES = {N_MATRICES:,}\")\n    print(f\"  β₁/β₂ ratios = {BETA_RATIOS}\")\n    print(f\"  Diagonal threshold = {DIAG_THRESHOLD}\")\n    print(\"=\" * 70)\n\n    rng = np.random.default_rng(SEED)\n    results = []\n\n    for ratio in BETA_RATIOS:\n        t_ratio = time.time()\n        print(f\"\\n--- Ratio β₁/β₂ = {ratio} ---\")\n        res = analyze_single_ratio(ratio, rng, verbose=True)\n        elapsed = time.time() - t_ratio\n        print(f\"  Valid matrices: {res['n_valid_all']:,} / {N_MATRICES:,}\")\n        print(f\"  Diagonal >= {DIAG_THRESHOLD}: {res['n_diag_pass']:,}\")\n        print(f\"  [ALL]  Primary sign-flip:   {res['primary_sign_flip_all']:>6,} \"\n              f\"({res['primary_sign_flip_rate_all']:.4%})\")\n        print(f\"  [ALL]  Secondary sign-flip:  {res['secondary_sign_flip_all']:>6,} \"\n              f\"({res['secondary_sign_flip_rate_all']:.4%})\")\n        print(f\"  [ALL]  Any sign-flip:        {res['any_sign_flip_all']:>6,} \"\n              f\"({res['any_sign_flip_rate_all']:.4%})\")\n        if res['n_diag_pass'] > 0:\n            print(f\"  [DIAG] Primary sign-flip:   {res['primary_sign_flip_diag']:>6,} \"\n                  f\"({res['primary_sign_flip_rate_diag']:.4%})\")\n            print(f\"  [DIAG] Secondary sign-flip:  {res['secondary_sign_flip_diag']:>6,} \"\n                  f\"({res['secondary_sign_flip_rate_diag']:.4%})\")\n        print(f\"  Primary plim:  mean={res['primary_plim_stats']['mean']:.4f}, \"\n              f\"min={res['primary_plim_stats']['min']:.4f}, \"\n              f\"p5={res['primary_plim_stats']['p5']:.4f}\")\n        print(f\"  Secondary plim: mean={res['secondary_plim_stats']['mean']:.4f}, \"\n              f\"min={res['secondary_plim_stats']['min']:.4f}, \"\n              f\"p5={res['secondary_plim_stats']['p5']:.4f}\")\n        print(f\"  Time: {elapsed:.1f}s\")\n        results.append(res)\n\n    # ========================================================================\n    # Summary table\n    # ========================================================================\n    print(\"\\n\" + \"=\" * 70)\n    print(\"SUMMARY TABLE\")\n    print(\"=\" * 70)\n    header = (f\"{'Ratio':>6} | {'β':>18} | \"\n              f\"{'Pri flip (all)':>14} | {'Sec flip (all)':>14} | \"\n              f\"{'Pri flip (diag)':>15} | {'Sec flip (diag)':>15}\")\n    print(header)\n    print(\"-\" * len(header))\n    for res in results:\n        beta_str = f\"[0, 1.0, {1.0/res['ratio']:.3f}]\"\n        pri_all = f\"{res['primary_sign_flip_rate_all']:.4%}\"\n        sec_all = f\"{res['secondary_sign_flip_rate_all']:.4%}\"\n        pri_diag = (f\"{res['primary_sign_flip_rate_diag']:.4%}\"\n                    if res['primary_sign_flip_rate_diag'] is not None else \"N/A\")\n        sec_diag = (f\"{res['secondary_sign_flip_rate_diag']:.4%}\"\n                    if res['secondary_sign_flip_rate_diag'] is not None else \"N/A\")\n        print(f\"{res['ratio']:>6.1f} | {beta_str:>18} | \"\n              f\"{pri_all:>14} | {sec_all:>14} | \"\n              f\"{pri_diag:>15} | {sec_diag:>15}\")\n\n    # ========================================================================\n    # Key finding\n    # ========================================================================\n    print(\"\\n\" + \"=\" * 70)\n    print(\"KEY FINDINGS\")\n    print(\"=\" * 70)\n\n    any_primary_flip_all = any(r['primary_sign_flip_all'] > 0 for r in results)\n    any_primary_flip_diag = any(\n        r['primary_sign_flip_diag'] > 0 for r in results\n        if r['n_diag_pass'] > 0\n    )\n    any_secondary_flip_all = any(r['secondary_sign_flip_all'] > 0 for r in results)\n\n    if not any_primary_flip_all:\n        print(\"  [CONFIRMED] Primary coefficient NEVER reverses sign across ALL matrices\")\n    else:\n        max_rate = max(r['primary_sign_flip_rate_all'] for r in results)\n        print(f\"  [VIOLATED] Primary coefficient CAN reverse sign (max rate: {max_rate:.4%})\")\n\n    if not any_primary_flip_diag:\n        print(\"  [CONFIRMED] Primary coefficient NEVER reverses sign for diag >= 0.7\")\n    else:\n        max_rate = max(\n            r['primary_sign_flip_rate_diag'] for r in results\n            if r['primary_sign_flip_rate_diag'] is not None\n        )\n        print(f\"  [VIOLATED] Primary coefficient CAN reverse sign at diag >= 0.7 \"\n              f\"(max rate: {max_rate:.4%})\")\n\n    if any_secondary_flip_all:\n        max_rate = max(r['secondary_sign_flip_rate_all'] for r in results)\n        max_ratio = max(results, key=lambda r: r['secondary_sign_flip_rate_all'])['ratio']\n        print(f\"  Secondary coefficient DOES reverse sign (max rate: {max_rate:.4%} \"\n              f\"at ratio={max_ratio})\")\n    else:\n        print(\"  Secondary coefficient also never reverses sign\")\n\n    # ========================================================================\n    # Save results\n    # ========================================================================\n    output_path = os.path.join(\n        os.path.dirname(os.path.abspath(__file__)),\n        'exp_primary_coeff_breakdown_results.json'\n    )\n\n    # Clean results for JSON serialization\n    def clean_for_json(obj):\n        if isinstance(obj, np.integer):\n            return int(obj)\n        elif isinstance(obj, np.floating):\n            v = float(obj)\n            return None if (np.isnan(v) or np.isinf(v)) else v\n        elif isinstance(obj, np.ndarray):\n            return obj.tolist()\n        elif isinstance(obj, dict):\n            return {str(k): clean_for_json(v) for k, v in obj.items()}\n        elif isinstance(obj, list):\n            return [clean_for_json(v) for v in obj]\n        elif isinstance(obj, (bool, np.bool_)):\n            return bool(obj)\n        elif isinstance(obj, float):\n            return None if (np.isnan(obj) or np.isinf(obj)) else obj\n        return obj\n\n    output_data = clean_for_json({\n        'config': {\n            'K': K,\n            'n_matrices': N_MATRICES,\n            'beta_ratios': BETA_RATIOS,\n            'diag_threshold': DIAG_THRESHOLD,\n            'n_precomp': N_PRECOMP,\n            'seed': SEED,\n        },\n        'results': results,\n        'summary': {\n            'primary_ever_flips_all': any_primary_flip_all,\n            'primary_ever_flips_diag': any_primary_flip_diag,\n            'secondary_ever_flips_all': any_secondary_flip_all,\n        },\n    })\n\n    with open(output_path, 'w') as f:\n        json.dump(output_data, f, indent=2)\n    print(f\"\\nResults saved to {output_path}\")\n\n    total_time = time.time() - t_start\n    print(f\"Total time: {total_time:.1f}s ({total_time / 60:.1f}min)\")\n\n\nif __name__ == '__main__':\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ba09150-d302-42b5-a9ed-5492e9896a75",
  "isSidechain": true,
  "agentId": "a345197f572e1e9bc",
  "requestId": "req_011CbJYPRWAqXB9WF4Mg3jCC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "22829012-1e85-47af-b915-c24cb7a95e55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JChA9QCYF82HM76EkuYrXn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1531,
      "cache_read_input_tokens": 49621,
      "output_tokens": 5682,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1531
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5682,
          "cache_read_input_tokens": 49621,
          "cache_creation_input_tokens": 1531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1531,
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

_source line 15 · 2026-05-23T00:20:32.075Z_

<details><summary>↩ Tool result · `toolu_012RQ7V1JmPnqBBZafbskiq7`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_primary_coeff_breakdown.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22829012-1e85-47af-b915-c24cb7a95e55",
  "isSidechain": true,
  "promptId": "221cc120-ad2a-4ac2-82b3-5f678194e371",
  "agentId": "a345197f572e1e9bc",
  "type": "user",
  "uuid": "f259de90-150b-4bc7-9db3-8ff783e4eb54",
  "sourceToolAssistantUUID": "22829012-1e85-47af-b915-c24cb7a95e55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-23T00:20:34.422Z_

Now let me run it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f259de90-150b-4bc7-9db3-8ff783e4eb54",
  "isSidechain": true,
  "agentId": "a345197f572e1e9bc",
  "requestId": "req_011CbJYV16ehSng3wmQHiD2r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc428b47-9da6-4bf9-a5b1-399cfd03e13c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZQf7dfhzwpV9JBJ856jYS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5740,
      "cache_read_input_tokens": 51152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5740,
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

_source line 17 · 2026-05-23T00:20:35.580Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NuDuzoYAYDjAAVVghitvNH`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib && python artifacts/exp_primary_coeff_breakdown.py 2>&1",
  "description": "Run primary coefficient sign reversal analysis",
  "timeout": 600000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc428b47-9da6-4bf9-a5b1-399cfd03e13c",
  "isSidechain": true,
  "agentId": "a345197f572e1e9bc",
  "requestId": "req_011CbJYV16ehSng3wmQHiD2r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e75d536-ed39-4f3a-9617-710029bc94b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZQf7dfhzwpV9JBJ856jYS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5740,
      "cache_read_input_tokens": 51152,
      "output_tokens": 146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5740
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 146,
          "cache_read_input_tokens": 51152,
          "cache_creation_input_tokens": 5740,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5740,
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

_source line 18 · 2026-05-23T00:20:35.660Z_

<details><summary>↩ Tool result · reported error · `toolu_01NuDuzoYAYDjAAVVghitvNH`</summary>

```text
Exit code 127
/bin/bash: line 1: python: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e75d536-ed39-4f3a-9617-710029bc94b5",
  "isSidechain": true,
  "promptId": "221cc120-ad2a-4ac2-82b3-5f678194e371",
  "agentId": "a345197f572e1e9bc",
  "type": "user",
  "uuid": "364330db-8008-437f-abaa-0ff0c47f52ab",
  "toolUseResult": "Error: Exit code 127\n/bin/bash: line 1: python: command not found",
  "sourceToolAssistantUUID": "0e75d536-ed39-4f3a-9617-710029bc94b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T00:20:37.333Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01N6KwUgHHPWepGwkJPR1sfi`</summary>

```json
{
  "command": "which python3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "364330db-8008-437f-abaa-0ff0c47f52ab",
  "isSidechain": true,
  "agentId": "a345197f572e1e9bc",
  "requestId": "req_011CbJYVGQQG8wB3dTzmGUTz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6efdada-d40e-4d92-8a4c-2b7c067a3280",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016oBDZ8Z1bwXjV3QEaWTawj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 185,
      "cache_read_input_tokens": 56892,
      "output_tokens": 54,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 185
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 54,
          "cache_read_input_tokens": 56892,
          "cache_creation_input_tokens": 185,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 185,
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

_source line 20 · 2026-05-23T00:20:37.417Z_

<details><summary>↩ Tool result · `toolu_01N6KwUgHHPWepGwkJPR1sfi`</summary>

```text
/usr/bin/python3
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6efdada-d40e-4d92-8a4c-2b7c067a3280",
  "isSidechain": true,
  "promptId": "221cc120-ad2a-4ac2-82b3-5f678194e371",
  "agentId": "a345197f572e1e9bc",
  "type": "user",
  "uuid": "96e62e79-3333-4640-ae2b-1809f4d6bbcf",
  "sourceToolAssistantUUID": "e6efdada-d40e-4d92-8a4c-2b7c067a3280",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T00:20:39.607Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0154v5tuVeMB7xu6yr7ZcrWk`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib && python3 artifacts/exp_primary_coeff_breakdown.py 2>&1",
  "description": "Run primary coefficient sign reversal analysis",
  "timeout": 600000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96e62e79-3333-4640-ae2b-1809f4d6bbcf",
  "isSidechain": true,
  "agentId": "a345197f572e1e9bc",
  "requestId": "req_011CbJYVPx5PmDKRTjVryr34",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45e640d8-1295-417e-a05f-b248a6c3d4ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SF6viKfnEoarFMHWUYP9Un",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 72,
      "cache_read_input_tokens": 57077,
      "output_tokens": 141,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 72
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 141,
          "cache_read_input_tokens": 57077,
          "cache_creation_input_tokens": 72,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 72,
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

_source line 22 · 2026-05-23T00:21:11.609Z_

<details><summary>↩ Tool result · `toolu_0154v5tuVeMB7xu6yr7ZcrWk`</summary>

```text
======================================================================
Primary Coefficient Sign Reversal Analysis — Exposure Topology K=3
  N_MATRICES = 100,000
  β₁/β₂ ratios = [1.0, 1.5, 2.0, 5.0, 10.0, 50.0]
  Diagonal threshold = 0.7
======================================================================

--- Ratio β₁/β₂ = 1.0 ---
  True β = [0.0, 1.0, 1.0]
  Plim(I) = [-6.08082570e-04  1.00159910e+00  1.00034271e+00]
  Valid matrices: 100,000 / 100,000
  Diagonal >= 0.7: 69
  [ALL]  Primary sign-flip:   50,125 (50.1250%)
  [ALL]  Secondary sign-flip:  50,025 (50.0250%)
  [ALL]  Any sign-flip:        66,651 (66.6510%)
  [DIAG] Primary sign-flip:        0 (0.0000%)
  [DIAG] Secondary sign-flip:       0 (0.0000%)
  Primary plim:  mean=-0.0004, min=-0.9853, p5=-0.5967
  Secondary plim: mean=0.0001, min=-0.9767, p5=-0.5949
  Time: 4.8s

--- Ratio β₁/β₂ = 1.5 ---
  True β = [0.0, 1.0, 0.6666666666666666]
  Plim(I) = [-0.0010863   1.00179243  0.66794758]
  Valid matrices: 100,000 / 100,000
  Diagonal >= 0.7: 60
  [ALL]  Primary sign-flip:   49,883 (49.8830%)
  [ALL]  Secondary sign-flip:  49,830 (49.8300%)
  [ALL]  Any sign-flip:        66,451 (66.4510%)
  [DIAG] Primary sign-flip:        0 (0.0000%)
  [DIAG] Secondary sign-flip:       0 (0.0000%)
  Primary plim:  mean=0.0004, min=-0.9594, p5=-0.5391
  Secondary plim: mean=0.0009, min=-0.9638, p5=-0.5408
  Time: 5.7s

--- Ratio β₁/β₂ = 2.0 ---
  True β = [0.0, 1.0, 0.5]
  Plim(I) = [-7.33473481e-04  1.00229227e+00  5.03745582e-01]
  Valid matrices: 100,000 / 100,000
  Diagonal >= 0.7: 55
  [ALL]  Primary sign-flip:   50,002 (50.0020%)
  [ALL]  Secondary sign-flip:  49,913 (49.9130%)
  [ALL]  Any sign-flip:        66,594 (66.5940%)
  [DIAG] Primary sign-flip:        0 (0.0000%)
  [DIAG] Secondary sign-flip:       0 (0.0000%)
  Primary plim:  mean=0.0002, min=-0.9591, p5=-0.5310
  Secondary plim: mean=0.0006, min=-0.9144, p5=-0.5312
  Time: 5.4s

--- Ratio β₁/β₂ = 5.0 ---
  True β = [0.0, 1.0, 0.2]
  Plim(I) = [-4.60774339e-04  1.00070686e+00  2.01024983e-01]
  Valid matrices: 100,000 / 100,000
  Diagonal >= 0.7: 76
  [ALL]  Primary sign-flip:   49,822 (49.8220%)
  [ALL]  Secondary sign-flip:  50,112 (50.1120%)
  [ALL]  Any sign-flip:        66,562 (66.5620%)
  [DIAG] Primary sign-flip:        0 (0.0000%)
  [DIAG] Secondary sign-flip:       5 (6.5789%)
  Primary plim:  mean=0.0004, min=-0.9587, p5=-0.5438
  Secondary plim: mean=-0.0000, min=-0.9325, p5=-0.5445
  Time: 4.9s

--- Ratio β₁/β₂ = 10.0 ---
  True β = [0.0, 1.0, 0.1]
  Plim(I) = [4.91821902e-04 9.99302866e-01 9.88354978e-02]
  Valid matrices: 100,000 / 100,000
  Diagonal >= 0.7: 61
  [ALL]  Primary sign-flip:   50,230 (50.2300%)
  [ALL]  Secondary sign-flip:  50,221 (50.2210%)
  [ALL]  Any sign-flip:        66,875 (66.8750%)
  [DIAG] Primary sign-flip:        0 (0.0000%)
  [DIAG] Secondary sign-flip:      13 (21.3115%)
  Primary plim:  mean=-0.0014, min=-0.9499, p5=-0.5573
  Secondary plim: mean=-0.0012, min=-0.9468, p5=-0.5534
  Time: 4.9s

--- Ratio β₁/β₂ = 50.0 ---
  True β = [0.0, 1.0, 0.02]
  Plim(I) = [0.00245635 0.99806356 0.01440495]
  Valid matrices: 100,000 / 100,000
  Diagonal >= 0.7: 78
  [ALL]  Primary sign-flip:   49,827 (49.8270%)
  [ALL]  Secondary sign-flip:  49,952 (49.9520%)
  [ALL]  Any sign-flip:        66,621 (66.6210%)
  [DIAG] Primary sign-flip:        0 (0.0000%)
  [DIAG] Secondary sign-flip:      35 (44.8718%)
  Primary plim:  mean=0.0022, min=-0.9747, p5=-0.5671
  Secondary plim: mean=0.0003, min=-0.9564, p5=-0.5687
  Time: 5.0s

======================================================================
SUMMARY TABLE
======================================================================
 Ratio |                  β | Pri flip (all) | Sec flip (all) | Pri flip (diag) | Sec flip (diag)
-------------------------------------------------------------------------------------------------
   1.0 |    [0, 1.0, 1.000] |       50.1250% |       50.0250% |         0.0000% |         0.0000%
   1.5 |    [0, 1.0, 0.667] |       49.8830% |       49.8300% |         0.0000% |         0.0000%
   2.0 |    [0, 1.0, 0.500] |       50.0020% |       49.9130% |         0.0000% |         0.0000%
   5.0 |    [0, 1.0, 0.200] |       49.8220% |       50.1120% |         0.0000% |         6.5789%
  10.0 |    [0, 1.0, 0.100] |       50.2300% |       50.2210% |         0.0000% |        21.3115%
  50.0 |    [0, 1.0, 0.020] |       49.8270% |       49.9520% |         0.0000% |        44.8718%

======================================================================
KEY FINDINGS
======================================================================
  [VIOLATED] Primary coefficient CAN reverse sign (max rate: 50.2300%)
  [CONFIRMED] Primary coefficient NEVER reverses sign for diag >= 0.7
  Secondary coefficient DOES reverse sign (max rate: 50.2210% at ratio=10.0)

Results saved to /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_primary_coeff_breakdown_results.json
Total time: 30.7s (0.5min)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45e640d8-1295-417e-a05f-b248a6c3d4ff",
  "isSidechain": true,
  "promptId": "221cc120-ad2a-4ac2-82b3-5f678194e371",
  "agentId": "a345197f572e1e9bc",
  "type": "user",
  "uuid": "8617c4fc-475e-4427-a154-e61deda85d59",
  "sourceToolAssistantUUID": "45e640d8-1295-417e-a05f-b248a6c3d4ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-23T00:21:20.261Z_

The results are interesting but the "all matrices" sign-flip rates near 50% indicate that unrestricted Dirichlet(1,1,1) matrices are essentially random — the plim distribution is centered near 0, making sign flips trivially frequent. The meaningful finding is in the diag >= 0.7 filter. However, the sample size there is very small (55-78 matrices). Let me also note an issue: the "primary coefficient" concept needs to be defined carefully. The task says "primary = the one with the largest |β|, which is β₁". But across all unrestricted random matrices, both coefficients flip ~50% of the time because the matrices are so noisy that the plim means are near zero.

The key result is clear and robust: **for realistic matrices (diag >= 0.7), the primary coefficient (β₁) never reverses sign across all 6 ratio configurations**, while the secondary coefficient does reverse sign increasingly as the ratio grows (from 0% at ratio=1.0 to 44.9% at ratio=50.0).

Let me verify the output file was saved correctly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8617c4fc-475e-4427-a154-e61deda85d59",
  "isSidechain": true,
  "agentId": "a345197f572e1e9bc",
  "requestId": "req_011CbJYXv6MEJVSNppsNTNXZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "34e2144e-8356-46fb-974f-c2919783725f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bdhy9cgJwxhLjGQDv2JCmB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2359,
      "cache_read_input_tokens": 57149,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2359,
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

_source line 24 · 2026-05-23T00:21:20.762Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KShhEmwv2eC2KFKi5HZLaD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_primary_coeff_breakdown_results.json",
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34e2144e-8356-46fb-974f-c2919783725f",
  "isSidechain": true,
  "agentId": "a345197f572e1e9bc",
  "requestId": "req_011CbJYXv6MEJVSNppsNTNXZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "49461279-6e65-47bc-9f16-e8633a631f80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bdhy9cgJwxhLjGQDv2JCmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2359,
      "cache_read_input_tokens": 57149,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2359
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 367,
          "cache_read_input_tokens": 57149,
          "cache_creation_input_tokens": 2359,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2359,
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

_source line 25 · 2026-05-23T00:21:20.830Z_

<details><summary>↩ Tool result · `toolu_01KShhEmwv2eC2KFKi5HZLaD`</summary>

```text
1	{
2	  "config": {
3	    "K": 3,
4	    "n_matrices": 100000,
5	    "beta_ratios": [
6	      1.0,
7	      1.5,
8	      2.0,
9	      5.0,
10	      10.0,
11	      50.0
12	    ],
13	    "diag_threshold": 0.7,
14	    "n_precomp": 2000000,
15	    "seed": 2026
16	  },
17	  "results": [
18	    {
19	      "ratio": 1.0,
20	      "beta": [
21	        0.0,
22	        1.0,
23	        1.0
24	      ],
25	      "n_matrices": 100000,
26	      "n_valid_all": 100000,
27	      "n_diag_pass": 69,
28	      "primary_sign_flip_all": 50125,
29	      "primary_sign_flip_rate_all": 0.50125,
30	      "secondary_sign_flip_all": 50025,
31	      "secondary_sign_flip_rate_all": 0.50025,
32	      "any_sign_flip_all": 66651,
33	      "any_sign_flip_rate_all": 0.66651,
34	      "primary_sign_flip_diag": 0,
35	      "primary_sign_flip_rate_diag": 0.0,
36	      "secondary_sign_flip_diag": 0,
37	      "secondary_sign_flip_rate_diag": 0.0,
38	      "any_sign_flip_diag": 0,
39	      "any_sign_flip_rate_diag": 0.0,
40	      "primary_plim_stats": {
41	        "mean": -0.000413217318165834,
42	        "std": 0.36509319532537793,
43	        "min": -0.9853215292607673,
44	        "p5": -0.596685689581924,
45	        "p25": -0.27569451654046045,
46	        "median": -0.0013227761138500129,
47	        "p75": 0.2753921479770494,
48	        "p95": 0.5938911024739431,
49	        "max": 0.9839323866150057
50	      },
51	      "secondary_plim_stats": {
52	        "mean": 6.449880998236097e-05,
53	        "std": 0.3654363101180692,
54	        "min": -0.9766658287642411,
55	        "p5": -0.5948905945770074,
56	        "p25": -0.27629089131396356,
57	        "median": -0.00032974539528513817,
58	        "p75": 0.27673397756727103,
59	        "p95": 0.5940108183483171,
60	        "max": 0.9618822766575893
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49461279-6e65-47bc-9f16-e8633a631f80",
  "isSidechain": true,
  "promptId": "221cc120-ad2a-4ac2-82b3-5f678194e371",
  "agentId": "a345197f572e1e9bc",
  "type": "user",
  "uuid": "718b044b-f8d0-4ced-a399-ee7cb44c2bf4",
  "sourceToolAssistantUUID": "49461279-6e65-47bc-9f16-e8633a631f80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-23T00:21:33.590Z_

The results file is properly saved. Here is the summary of what was done and findings:

---

**Script created**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_primary_coeff_breakdown.py`

**Results saved**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_primary_coeff_breakdown_results.json`

**Setup**: K=3 exposure topology, 100,000 Dirichlet(1,1,1) confusion matrices per ratio, 6 β₁/β₂ ratios from 1.0 to 50.0, with β = [0, 1.0, 1.0/ratio].

**Key Findings**:

1. **Primary coefficient (β₁) NEVER reverses sign when diag >= 0.7** — confirmed across all 6 ratio configurations (0 flips out of 55-78 realistic matrices per ratio). This supports the paper's claim.

2. **Secondary coefficient (β₂) increasingly reverses sign as the ratio grows** under the diag >= 0.7 filter:
   - Ratio 1.0-2.0: 0% secondary sign flips
   - Ratio 5.0: 6.6% secondary sign flips
   - Ratio 10.0: 21.3% secondary sign flips
   - Ratio 50.0: 44.9% secondary sign flips

3. **Under unrestricted Dirichlet matrices (no diagonal filter)**, both primary and secondary flip ~50% of the time. This is expected: random matrices with no accuracy constraint push the plim distribution to be centered near zero (mean plim ~ 0.0), making sign flips trivially frequent. The plim distributions have std ~ 0.37, so values are uniformly spread across both signs.

4. **The diagonal filter matters enormously**: only ~60-78 out of 100,000 Dirichlet(1,1,1) matrices have min diagonal >= 0.7, and within that realistic subset, the primary coefficient is robustly preserved while weaker secondary coefficients become increasingly vulnerable.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "718b044b-f8d0-4ced-a399-ee7cb44c2bf4",
  "isSidechain": true,
  "agentId": "a345197f572e1e9bc",
  "requestId": "req_011CbJYYbb9HJbh9yGy3nXnB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3ff096cf-49b3-4ce9-a415-f4f40a025cca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/.claude/sessions/agent_a2eb248d",
  "sessionId": "4bc24e8b-1078-439c-82f4-1b77043197af",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "eager-splashing-waterfall",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MZN3JPXZuVQ7hbpYVNxKKj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1200,
      "cache_read_input_tokens": 59508,
      "output_tokens": 529,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1200
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 529,
          "cache_read_input_tokens": 59508,
          "cache_creation_input_tokens": 1200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1200,
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
