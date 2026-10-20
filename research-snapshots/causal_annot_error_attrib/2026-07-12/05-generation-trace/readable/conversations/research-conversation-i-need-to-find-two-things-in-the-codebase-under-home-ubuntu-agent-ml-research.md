# Research conversation: I need to find two things in the codebase under /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_at

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a8d5f7280dd4c25d0.jsonl`
- **Structured JSON:** [`4ce81c0e5da1b550abfa.json`](../../sessions/4c/4ce81c0e5da1b550abfa.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-23T14:56:54.558Z_

I need to find two things in the codebase under /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/:

1. JSON files in artifacts/ that contain empirical LLM confusion matrices (search for files with "confusion" in the name, or JSON files containing "confusion_matrix" or "confusion_matrices" keys)
2. The bias plim / exposure bias computation code in artifacts/ranking_stability.py or artifacts/compute_all_tasks.py — I need to understand how sign reversal is determined from a confusion matrix and a beta vector under exposure topology.

Search breadth: very thorough. Show me the relevant file paths and code snippets.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "a39553f7-6119-4bf4-95d9-7538c4458778",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T14:56:56.019Z_

I'll conduct a thorough search for these two items. Let me start by exploring the artifacts directory and searching for the relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a39553f7-6119-4bf4-95d9-7538c4458778",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhK5pghGAL6JXjYphyG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8487e82b-886b-4ce9-94d5-8bcffbb00886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012nTTjhkyrZpZiWWFAzS5t9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 17330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 586,
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

_source line 3 · 2026-05-23T14:56:56.617Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HS32CDBYErnM6TshyEGQzD`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/**/*.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8487e82b-886b-4ce9-94d5-8bcffbb00886",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhK5pghGAL6JXjYphyG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "beb43626-474c-491b-8b01-d202088a0602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012nTTjhkyrZpZiWWFAzS5t9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 17330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 586,
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

_source line 4 · 2026-05-23T14:56:56.637Z_

<details><summary>↩ Tool result · `toolu_01HS32CDBYErnM6TshyEGQzD`</summary>

```text
artifacts/dream_reports/dream_20260520T074549/best/experiment_data.json
artifacts/dream_reports/dream_20260520T074549/median/experiment_data.json
artifacts/dream_reports/dream_20260520T074549/worst/experiment_data.json
artifacts/plan006/asv_empirical_results.json
artifacts/plan006_mock/asv_empirical_results.json
artifacts/plan006_asv_empirical/data/plan006_full_filtered_stats.json
artifacts/plan006_full_filtered_stats.json
artifacts/iv_dirichlet_subspace_results.json
artifacts/_project/data/nondiff_stress_test_results.json
artifacts/dream_reports/dream_20260521T054528/best/experiment_data.json
artifacts/_project/data/ppi_empirical_validation.json
artifacts/_project/data/case_study_results.json
artifacts/plan012_case_study/case_study_results.json
artifacts/ppi_empirical_validation.json
artifacts/plan007_fast/correction_guidance_results.json
artifacts/plan007/correction_guidance_results.json
artifacts/plan007_rmse_correction_results.json
artifacts/plan007_correction_guidance/data/plan007_rmse_correction_results.json
artifacts/delta_max_results.json
artifacts/_project/data/plan011_frontier_cms.json
artifacts/_project/data/updated_empirical_results.json
artifacts/plan011_new_cms.json
artifacts/plan011_new_cms_round2.json
artifacts/exp_a_stress_test_results.json
artifacts/plan011_new_cms_vast_qwen3_zs.json
artifacts/plan011_frontier_cms.json
artifacts/updated_empirical_results.json
artifacts/exp_c_bootstrap_results.json
artifacts/exp_d_conjecture_results.json
artifacts/exp_e_asv_stability_results.json
artifacts/exp_d_conjecture_results_v2.json
artifacts/exp_b_logistic_results.json
artifacts/_project/data/exp_d_epsilon_tau_sensitivity.json
artifacts/exp_d_epsilon_tau_sensitivity.json
artifacts/_project/data/verify_lambda_bound_results.json
artifacts/verify_lambda_bound_results.json
artifacts/exp_fwl_logistic_results.json
artifacts/theorem1_direct_proof_results.json
artifacts/theory_empirical_mape.json
artifacts/exp_primary_coeff_breakdown_results.json
artifacts/nondiff_stress_test_results.json
artifacts/exp_proportional_effects_results.json
artifacts/exp_fwl_nonlinear_scaling_results.json
artifacts/exp_realistic_epsilon_results.json
artifacts/exp_proportional_real_matrices_results.json
artifacts/_project/data/nondiff_structured_stress_results.json
artifacts/nondiff_structured_stress_results.json
artifacts/_project/data/bootstrap_ci_convergence_results.json
artifacts/bootstrap_ci_convergence_results.json
artifacts/ppi_gold_ratio_results.json
artifacts/nondiff_topic_stratified_results.json
artifacts/correction_k_sensitivity_results.json
artifacts/ranking_stability_results.json
artifacts/_project/data/e2e_demo_results.json
artifacts/e2e_demo_results.json
artifacts/conjecture_dgp_sensitivity_results.json
artifacts/structured_nondiff_violation_results.json
artifacts/within_topo_f1_bias_results.json
artifacts/c_estimation_robustness_results.json
artifacts/sign_reversal_determinants_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "beb43626-474c-491b-8b01-d202088a0602",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "afac5528-0769-449e-811c-57e02c79026e",
  "sourceToolAssistantUUID": "beb43626-474c-491b-8b01-d202088a0602",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T14:56:56.770Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UjsgETyBSDNcHwDFNFHC8k`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts -type f -name \"*confusion*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afac5528-0769-449e-811c-57e02c79026e",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhK5pghGAL6JXjYphyG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b301da3a-db36-44b6-8754-09e3263b7c41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012nTTjhkyrZpZiWWFAzS5t9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 17330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 586,
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

_source line 6 · 2026-05-23T14:56:56.924Z_

<details><summary>↩ Tool result · `toolu_01UjsgETyBSDNcHwDFNFHC8k`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b301da3a-db36-44b6-8754-09e3263b7c41",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "d28f2859-c726-4831-b96d-ee750f02d2c2",
  "sourceToolAssistantUUID": "b301da3a-db36-44b6-8754-09e3263b7c41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T14:56:57.012Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AYM1PZp4AXuNdfHJ2A5hve`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d28f2859-c726-4831-b96d-ee750f02d2c2",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhK5pghGAL6JXjYphyG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9cfdf32b-cd64-4f69-824e-9f46e0ace19b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012nTTjhkyrZpZiWWFAzS5t9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 17330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 586,
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

_source line 8 · 2026-05-23T14:56:57.071Z_

<details><summary>↩ Tool result · `toolu_01AYM1PZp4AXuNdfHJ2A5hve`</summary>

```text
total 2736
drwxr-xr-x 37 ubuntu ubuntu  12288 May 23 14:56 .
drwxr-xr-x 16 ubuntu ubuntu   4096 May 23 13:41 ..
drwxr-xr-x  2 ubuntu ubuntu   4096 May 23 14:35 __pycache__
drwxr-xr-x  7 ubuntu ubuntu   4096 May 21 10:11 _project
-rw-r--r--  1 ubuntu ubuntu  19684 May 22 14:24 analyze_epsilon_bound.py
-rw-r--r--  1 ubuntu ubuntu   6687 May 22 14:25 analyze_epsilon_sign_structure.py
-rw-r--r--  1 ubuntu ubuntu  25721 May 22 06:30 annotate.py
-rw-r--r--  1 ubuntu ubuntu  16182 May 23 05:06 bootstrap_ci_convergence.py
-rw-r--r--  1 ubuntu ubuntu   3557 May 23 05:10 bootstrap_ci_convergence_results.json
-rw-r--r--  1 ubuntu ubuntu  12020 May 23 14:54 c_estimation_robustness.py
-rw-r--r--  1 ubuntu ubuntu  20032 May 23 14:55 c_estimation_robustness_results.json
-rw-r--r--  1 ubuntu ubuntu  32956 May 21 08:24 compute_all_tasks.py
-rw-r--r--  1 ubuntu ubuntu  18836 May 22 04:00 compute_delta_max.py
-rw-r--r--  1 ubuntu ubuntu  22098 May 21 08:32 compute_ppi_empirical.py
-rw-r--r--  1 ubuntu ubuntu   8003 May 21 08:07 compute_theory_empirical_mape.py
-rw-r--r--  1 ubuntu ubuntu   7475 May 22 19:57 compute_unified_mape.py
-rw-r--r--  1 ubuntu ubuntu  14720 May 22 06:44 compute_updated_empirical.py
-rw-r--r--  1 ubuntu ubuntu  21740 May 23 14:42 conjecture_dgp_sensitivity.py
-rw-r--r--  1 ubuntu ubuntu  45552 May 23 14:45 conjecture_dgp_sensitivity_results.json
-rw-r--r--  1 ubuntu ubuntu   2104 May 23 14:45 conjecture_dgp_sensitivity_table.tex
-rw-r--r--  1 ubuntu ubuntu  17957 May 23 07:02 correction_k_sensitivity.py
-rw-r--r--  1 ubuntu ubuntu   4624 May 23 09:02 correction_k_sensitivity_results.json
-rw-r--r--  1 ubuntu ubuntu  23193 May 22 04:00 delta_max_results.json
drwxr-xr-x 13 ubuntu ubuntu   4096 May 21 08:32 dream_reports
-rw-r--r--  1 ubuntu ubuntu  13795 May 23 14:34 e2e_demo.py
-rw-r--r--  1 ubuntu ubuntu   3590 May 23 14:36 e2e_demo_results.json
-rw-r--r--  1 ubuntu ubuntu    887 May 23 14:36 e2e_demo_table.tex
-rw-r--r--  1 ubuntu ubuntu  15138 May 22 11:23 exp_a_stress_test.py
-rw-r--r--  1 ubuntu ubuntu  39314 May 22 11:24 exp_a_stress_test_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cfdf32b-cd64-4f69-824e-9f46e0ace19b",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "458bea35-1ce3-42eb-baab-af01834a02f2",
  "sourceToolAssistantUUID": "9cfdf32b-cd64-4f69-824e-9f46e0ace19b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-23T14:56:58.654Z_

Now let me search for JSON files with confusion matrix content and examine the two Python files you mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "458bea35-1ce3-42eb-baab-af01834a02f2",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhKH8peYXq1phbo9NGP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "de55cfcc-269f-4f8f-b3a2-fdae6571208f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01A4fEMd5GejZCLGquxFjpsS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3081,
      "cache_read_input_tokens": 17916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3081,
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

_source line 10 · 2026-05-23T14:56:59.510Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01R8Py7rSMJD34CStS44ABVe`</summary>

```json
{
  "pattern": "confusion_matrix|confusion_matrices",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts",
  "type": "json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de55cfcc-269f-4f8f-b3a2-fdae6571208f",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhKH8peYXq1phbo9NGP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8d84cb16-3691-4001-abc6-dfd7ccaef213",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01A4fEMd5GejZCLGquxFjpsS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3081,
      "cache_read_input_tokens": 17916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3081,
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

_source line 11 · 2026-05-23T14:56:59.532Z_

<details><summary>↩ Tool result · `toolu_01R8Py7rSMJD34CStS44ABVe`</summary>

```text
Found 17 files
artifacts/correction_k_sensitivity_results.json
artifacts/nondiff_topic_stratified_results.json
artifacts/ppi_gold_ratio_results.json
artifacts/exp_fwl_nonlinear_scaling_results.json
artifacts/nondiff_stress_test_results.json
artifacts/updated_empirical_results.json
artifacts/plan011_frontier_cms.json
artifacts/plan011_new_cms_vast_qwen3_zs.json
artifacts/plan011_new_cms_round2.json
artifacts/plan011_new_cms.json
artifacts/_project/data/updated_empirical_results.json
artifacts/_project/data/plan011_frontier_cms.json
artifacts/delta_max_results.json
artifacts/dream_reports/dream_20260521T054528/best/experiment_data.json
artifacts/_project/data/nondiff_stress_test_results.json
artifacts/plan006_mock/asv_empirical_results.json
artifacts/plan006/asv_empirical_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d84cb16-3691-4001-abc6-dfd7ccaef213",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "b31bed1b-9c3e-43c7-8af5-6955928a26f4",
  "sourceToolAssistantUUID": "8d84cb16-3691-4001-abc6-dfd7ccaef213",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-23T14:56:59.961Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BupENoYToVorWhy8x8t7hN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ranking_stability.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b31bed1b-9c3e-43c7-8af5-6955928a26f4",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhKH8peYXq1phbo9NGP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d4551d21-939e-428a-b1ff-764c9443fedc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01A4fEMd5GejZCLGquxFjpsS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3081,
      "cache_read_input_tokens": 17916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3081,
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

_source line 13 · 2026-05-23T14:57:00.121Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SkBELojKFb5i1pckyoxYim`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_all_tasks.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4551d21-939e-428a-b1ff-764c9443fedc",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhKH8peYXq1phbo9NGP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1ac7a21a-88bf-4c6b-8a13-c6fe72cd8269",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01A4fEMd5GejZCLGquxFjpsS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3081,
      "cache_read_input_tokens": 17916,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3081
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 286,
          "cache_read_input_tokens": 17916,
          "cache_creation_input_tokens": 3081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3081,
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

_source line 14 · 2026-05-23T14:57:00.248Z_

<details><summary>↩ Tool result · `toolu_01BupENoYToVorWhy8x8t7hN`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	ASV topology ranking stability analysis.
4	
5	Computes three things:
6	  1. ASV topology ranking stability: For N random Dirichlet(1,1,1) confusion
7	     matrices C0, compute magnitude ASV delta* for 6 topologies and measure
8	     Kendall tau correlation between empirical and theoretical ranking.
9	     Collider/M-bias are assigned ASV=inf (immune) since annotation error
10	     is protective (|B| non-increasing). IV is included but may produce NaN
11	     due to first-stage singularities.
12	  2. Epsilon-perturbation ranking robustness: At each delta*, check if
13	     perturbing by +/-0.013 would change the relative ranking between any
14	     pair of topologies.
15	  3. Large-scale Conjecture verification: Verify epsilon-approximate
16	     monotonicity of |B(C(delta))| along delta in [0,1] for non-IV topologies.
17	     Report worst-case step deviation across all matrices.
18	
19	Uses analytic plim computation (Gauss-Hermite quadrature for nonlinear
20	topologies) -- zero sampling noise. Fully vectorized over matrices in chunks.
21	
22	Input: Random K=3 Dirichlet(1,1,1) confusion matrices.
23	Output: artifacts/ranking_stability_results.json + console summary.
24	"""
25	
26	import numpy as np
27	import json
28	import time
29	import sys
30	import os
31	from scipy.special import roots_hermite
32	from scipy.stats import kendalltau, rankdata
33	
34	# ====================================================================
35	# Gauss-Hermite quadrature setup
36	# ====================================================================
37	N_GH = 100
38	_gh_x_raw, _gh_w_raw = roots_hermite(N_GH)
39	GH_X = _gh_x_raw * np.sqrt(2)
40	GH_W = _gh_w_raw / np.sqrt(np.pi)
41	
42	GH_X2_a, GH_X2_b = np.meshgrid(GH_X, GH_X, indexing='ij')
43	GH_W2 = np.outer(GH_W, GH_W)
44	GH_X2_a_flat = GH_X2_a.ravel()
45	GH_X2_b_flat = GH_X2_b.ravel()
46	GH_W2_flat = GH_W2.ravel()
47	
48	# ====================================================================
49	# Configuration
50	# ====================================================================
51	K = 3
52	N_MATRICES = 1_000_000
53	CHUNK_SIZE = 10_000          # process this many matrices at once
54	SEED = 42
55	DELTA_STEP = 0.005           # step size for bias curve
56	ASV_EPSILON = 0.05           # magnitude ASV threshold (10% of tau=0.5)
57	PERTURB_EPSILON = 0.013      # perturbation for ranking robustness check
58	MONO_TOL = 1e-12             # tolerance for monotonicity violation detection
59	
60	# Theoretical ranking (most fragile to most robust)
61	THEORETICAL_RANKING_ORDER = [
62	    'iv', 'frontdoor', 'mediation', 'confounding', 'collider', 'mbias'
63	]
64	
65	RANKING_TOPOS = ['iv', 'frontdoor', 'mediation', 'confounding',
66	                 'collider', 'mbias']
67	CONJECTURE_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
68	                    'mbias', 'frontdoor']
69	ALL_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
70	             'mbias', 'iv', 'frontdoor']
71	
72	NON_DECREASING = {'confounding', 'mediation', 'exposure', 'frontdoor', 'iv'}
73	NON_INCREASING = {'collider', 'mbias'}
74	PROTECTIVE = {'collider', 'mbias'}
75	
76	OUT_DIR = os.path.dirname(os.path.abspath(__file__))
77	
78	# Fixed delta grid (delta_max capped at 1.0 for all Dirichlet matrices)
79	DELTAS = np.arange(0, 1.0 + DELTA_STEP / 2, DELTA_STEP)
80	N_DELTA = len(DELTAS)
81	
82	# ====================================================================
83	# DGP parameters (paper defaults, K=3)
84	# ====================================================================
85	DGP_PARAMS = {
86	    'confounding': dict(
87	        p_A=np.array([0.40, 0.35, 0.25]),
88	        alpha=np.array([1.5, -1.0]),
89	        beta_A=np.array([1.0, -0.5]),
90	        beta_T=2.0, sigma_T=1.0),
91	    'mediation': dict(
92	        tau=0.5,
93	        gamma=np.array([0.0, 0.5, -0.3]),
94	        delta=np.array([0.0, 0.8, -0.6]),
95	        beta=np.array([0.0, 1.0, -0.5])),
96	    'collider': dict(
97	        tau=1.0,
98	        g=np.array([0.0, 0.0, 0.0]),
99	        dT=np.array([0.0, 0.5, -0.3]),
100	        dY=np.array([0.0, 0.8, 0.6])),
101	    'exposure': dict(
102	        beta=np.array([0.0, 1.0, -0.5]),
103	        p_A=np.array([0.40, 0.35, 0.25])),
104	    'mbias': dict(
105	        tau=1.0, delta_coef=1.0, lam=1.0,
106	        g=np.array([0.0, 0.0, 0.0]),
107	        a1=np.array([0.0, 0.8, -0.5]),
108	        a2=np.array([0.0, 0.6, 0.9])),
109	    'iv': dict(
110	        lam=1.0,
111	        g=np.array([0.0, 0.0, 0.0]),
112	        dZ=np.array([0.0, 1.0, -0.5]),
113	        dU=np.array([0.0, 0.8, 0.6]),
114	        beta=np.array([0.0, 1.0, -0.5])),
115	    'frontdoor': dict(
116	        alpha_U=1.0, lam_U=1.0,
117	        gamma=np.array([0.0, 0.5, -0.3]),
118	        delta=np.array([0.0, 1.0, -0.8]),
119	        beta=np.array([0.0, 1.0, -0.5])),
120	}
121	
122	
123	# ====================================================================
124	# Stable softmax
125	# ====================================================================
126	def _softmax(logits):
127	    e = np.exp(logits - np.max(logits, axis=-1, keepdims=True))
128	    return e / np.sum(e, axis=-1, keepdims=True)
129	
130	
131	# ====================================================================
132	# Analytic Sufficient Statistics
133	# ====================================================================
134	class SuffStats:
135	    def __init__(self, K, has_T=True):
136	        self.K = K
137	        self.has_T = has_T
138	
139	
140	class IVSuffStats:
141	    def __init__(self, K):
142	        self.K = K
143	
144	
145	def compute_confounding_ss(p):
146	    ss = SuffStats(K, has_T=True)
147	    p_A = p['p_A']
148	    alpha = p['alpha']
149	    beta_A = p['beta_A']
150	    beta_T = p['beta_T']
151	    sigma_T = p['sigma_T']
152	    ss.p_A = p_A.copy()
153	    ss.E_T = sum(alpha[j] * p_A[j + 1] for j in range(K - 1))
154	    ss.E_T2 = sum(alpha[j]**2 * p_A[j + 1] for j in range(K - 1)) + sigma_T**2
155	    ss.E_TD = np.zeros(K)
156	    for k in range(1, K):
157	        ss.E_TD[k] = alpha[k - 1] * p_A[k]
158	    ss.E_Y = beta_T * ss.E_T + sum(beta_A[j] * p_A[j + 1] for j in range(K - 1))
159	    ss.E_YD = np.zeros(K)
160	    for k in range(1, K):
161	        ss.E_YD[k] = beta_T * ss.E_TD[k] + beta_A[k - 1] * p_A[k]
162	    ss.E_TY = beta_T * ss.E_T2 + sum(
163	        beta_A[j] * ss.E_TD[j + 1] for j in range(K - 1))
164	    return ss
165	
166	
167	def compute_exposure_ss(p):
168	    ss = SuffStats(K, has_T=False)
169	    p_A = p['p_A']
170	    beta = p['beta']
171	    ss.p_A = p_A.copy()
172	    ss.E_Y = beta[0] + sum(beta[j] * p_A[j] for j in range(1, K))
173	    ss.E_YD = np.zeros(K)
174	    ss.E_YD[0] = beta[0] * p_A[0]
175	    for k in range(1, K):
176	        ss.E_YD[k] = (beta[0] + beta[k]) * p_A[k]
177	    return ss
178	
179	
180	def compute_mediation_ss(p):
181	    ss = SuffStats(K, has_T=True)
182	    tau = p['tau']
183	    gamma = p['gamma']
184	    delta_coef = p['delta']
185	    beta = p['beta']
186	    probs_T0 = _softmax(gamma)
187	    probs_T1 = _softmax(gamma + delta_coef)
188	    ss.p_A = 0.5 * probs_T0 + 0.5 * probs_T1
189	    ss.E_T = 0.5
190	    ss.E_T2 = 0.5
191	    ss.E_TD = 0.5 * probs_T1
192	    ss.E_Y = (beta[0] + sum(beta[k] * ss.p_A[k] for k in range(1, K))
193	              + tau * 0.5)
194	    ss.E_YD = np.zeros(K)
195	    for k in range(K):
196	        beta_k = beta[k] if k >= 1 else 0.0
197	        ss.E_YD[k] = (beta[0] + beta_k) * ss.p_A[k] + tau * ss.E_TD[k]
198	    ss.E_TY = (beta[0] * 0.5
199	               + sum(beta[k] * ss.E_TD[k] for k in range(1, K))
200	               + tau * 0.5)
201	    return ss
202	
203	
204	def compute_collider_ss(p):
205	    ss = SuffStats(K, has_T=True)
206	    tau = p['tau']
207	    g, dT, dY = p['g'], p['dT'], p['dY']
208	    coeff1 = dT + tau * dY
209	    coeff2 = dY
210	    logits = (g[None, :]
211	              + coeff1[None, :] * GH_X2_a_flat[:, None]
212	              + coeff2[None, :] * GH_X2_b_flat[:, None])
213	    probs = _softmax(logits)
214	    T_vals = GH_X2_a_flat
215	    Y_vals = tau * GH_X2_a_flat + GH_X2_b_flat
216	    w = GH_W2_flat
217	    ss.p_A = (w[:, None] * probs).sum(axis=0)
218	    ss.E_TD = (w[:, None] * T_vals[:, None] * probs).sum(axis=0)
219	    ss.E_YD = (w[:, None] * Y_vals[:, None] * probs).sum(axis=0)
220	    ss.E_T = 0.0
221	    ss.E_T2 = 1.0
222	    ss.E_Y = 0.0
223	    ss.E_TY = tau
224	    return ss
225	
226	
227	def compute_mbias_ss(p):
228	    ss = SuffStats(K, has_T=True)
229	    tau = p['tau']
230	    delta_coef = p['delta_coef']
231	    lam = p['lam']
232	    g, a1, a2 = p['g'], p['a1'], p['a2']
233	    logits = (g[None, :]
234	              + a1[None, :] * GH_X2_a_flat[:, None]
235	              + a2[None, :] * GH_X2_b_flat[:, None])
236	    probs = _softmax(logits)
237	    w = GH_W2_flat
238	    ss.p_A = (w[:, None] * probs).sum(axis=0)
239	    E_U1_Dk = (w[:, None] * GH_X2_a_flat[:, None] * probs).sum(axis=0)
240	    E_U2_Dk = (w[:, None] * GH_X2_b_flat[:, None] * probs).sum(axis=0)
241	    ss.E_TD = delta_coef * E_U1_Dk
242	    ss.E_YD = tau * ss.E_TD + lam * E_U2_Dk
243	    ss.E_T = 0.0
244	    ss.E_T2 = delta_coef**2 + 1.0
245	    ss.E_Y = 0.0
246	    ss.E_TY = tau * ss.E_T2
247	    return ss
248	
249	
250	def compute_frontdoor_ss(p):
251	    ss = SuffStats(K, has_T=True)
252	    alpha_U = p['alpha_U']
253	    lam_U = p['lam_U']
254	    gamma = p['gamma']
255	    delta_coef = p['delta']
256	    beta = p['beta']
257	    sigma_T2 = alpha_U**2 + 1.0
258	    sigma_T = np.sqrt(sigma_T2)
259	    T_nodes = GH_X * sigma_T
260	    T_weights = GH_W
261	    logits = gamma[None, :] + delta_coef[None, :] * T_nodes[:, None]
262	    probs = _softmax(logits)
263	    ss.p_A = (T_weights[:, None] * probs).sum(axis=0)
264	    ss.E_TD = (T_weights[:, None] * T_nodes[:, None] * probs).sum(axis=0)
265	    E_U_given_T = alpha_U / sigma_T2 * T_nodes
266	    E_U_Mk = (T_weights[:, None] * E_U_given_T[:, None] * probs).sum(axis=0)
267	    ss.E_YD = np.zeros(K)
268	    for k in range(K):
269	        beta_k = beta[k] if k >= 1 else 0.0
270	        ss.E_YD[k] = beta_k * ss.p_A[k] + lam_U * E_U_Mk[k]
271	    ss.E_T = 0.0
272	    ss.E_T2 = sigma_T2
273	    ss.E_Y = sum(beta[k] * ss.p_A[k] for k in range(1, K))
274	    ss.E_TY = (sum(beta[k] * ss.E_TD[k] for k in range(1, K))
275	               + lam_U * alpha_U)
276	    return ss
277	
278	
279	def compute_iv_ss(p):
280	    ivss = IVSuffStats(K)
281	    g, dZ, dU = p['g'], p['dZ'], p['dU']
282	    beta = p['beta']
283	    logits_z0 = g[None, :] + dU[None, :] * GH_X[:, None]
284	    probs_z0 = _softmax(logits_z0)
285	    P_A_z0 = (GH_W[:, None] * probs_z0).sum(axis=0)
286	    logits_z1 = g[None, :] + dZ[None, :] + dU[None, :] * GH_X[:, None]
287	    probs_z1 = _softmax(logits_z1)
288	    P_A_z1 = (GH_W[:, None] * probs_z1).sum(axis=0)
289	    ivss.FS = P_A_z1 - P_A_z0
290	    E_Y_z0 = sum(beta[k] * P_A_z0[k] for k in range(1, K))
291	    E_Y_z1 = sum(beta[k] * P_A_z1[k] for k in range(1, K))
292	    ivss.RF = E_Y_z1 - E_Y_z0
293	    return ivss
294	
295	
296	COMPUTE_SS = {
297	    'confounding': compute_confounding_ss,
298	    'mediation': compute_mediation_ss,
299	    'collider': compute_collider_ss,
300	    'exposure': compute_exposure_ss,
301	    'mbias': compute_mbias_ss,
302	    'iv': compute_iv_ss,
303	    'frontdoor': compute_frontdoor_ss,
304	}
305	
306	
307	def get_tau_true(topo, ss):
308	    """True causal parameter."""
309	    p = DGP_PARAMS[topo]
310	    if topo in PROTECTIVE:
311	        return p['tau']
312	    if topo == 'iv':
313	        if abs(ss.FS[1]) < 1e-15:
314	            return np.nan
315	        return ss.RF / ss.FS[1]
316	    elif topo == 'exposure':
317	        q = ss.p_A
318	        EZZ = np.zeros((K, K))
319	        EZZ[0, 0] = 1.0
320	        EZZ[0, 1:] = q[1:]
321	        EZZ[1:, 0] = q[1:]
322	        for j in range(K - 1):
323	            EZZ[j + 1, j + 1] = q[j + 1]
324	        EZY = np.zeros(K)
325	        EZY[0] = ss.E_Y
326	        EZY[1:] = ss.E_YD[1:]
327	        return np.linalg.solve(EZZ, EZY)[1]
328	    else:
329	        q = ss.p_A
330	        ct = ss.E_TD
331	        cy = ss.E_YD
332	        dim = K + 1
333	        EZZ = np.zeros((dim, dim))
334	        EZZ[0, 0] = 1.0
335	        EZZ[0, 1] = ss.E_T
336	        EZZ[1, 0] = ss.E_T
337	        EZZ[1, 1] = ss.E_T2
338	        EZZ[0, 2:] = q[1:]
339	        EZZ[2:, 0] = q[1:]
340	        EZZ[1, 2:] = ct[1:]
341	        EZZ[2:, 1] = ct[1:]
342	        for j in range(K - 1):
343	            EZZ[j + 2, j + 2] = q[j + 1]
344	        EZY = np.zeros(dim)
345	        EZY[0] = ss.E_Y
346	        EZY[1] = ss.E_TY
347	        EZY[2:] = cy[1:]
348	        return np.linalg.solve(EZZ, EZY)[1]
349	
350	
351	# ====================================================================
352	# Batch bias curve + ASV + monotonicity (fully vectorized)
353	# ====================================================================
354	def process_batch_iv(C0_batch, ss, tau_true):
355	    """Process a batch of C0 matrices for IV topology.
356	
357	    Args:
358	        C0_batch: (M, K, K) confusion matrices
359	        ss: IVSuffStats
360	        tau_true: scalar
361	
362	    Returns:
363	        asv_vals: (M,) ASV values (inf if threshold never crossed)
364	    """
365	    M = C0_batch.shape[0]
366	    # FS0[m, k] = sum_j C0[m, k, j] * ss.FS[j]
367	    FS0 = np.einsum('mkj,j->mk', C0_batch, ss.FS)  # (M, K)
368	
369	    # For each delta, FS*(delta) = (1-d)*ss.FS + d*FS0
370	    # Shape: (N_DELTA, M, K)
371	    d = DELTAS[:, None, None]  # (N_DELTA, 1, 1)
372	    fs_star = (1 - d) * ss.FS[None, None, :] + d * FS0[None, :, :]
373	    denom = fs_star[:, :, 1]  # (N_DELTA, M)
374	
375	    # tau(delta) = RF / denom
376	    with np.errstate(divide='ignore', invalid='ignore'):
377	        taus = np.where(np.abs(denom) < 1e-15, np.nan, ss.RF / denom)
378	
379	    bias_abs = np.abs(taus - tau_true)  # (N_DELTA, M)
380	
381	    # ASV: find first delta where running-max envelope > ASV_EPSILON
382	    # Compute running max along delta axis
383	    envelope = np.fmax.accumulate(np.nan_to_num(bias_abs, nan=0.0), axis=0)
384	    # Find first crossing
385	    crossed = envelope > ASV_EPSILON  # (N_DELTA, M)
386	    # For each matrix, find first delta index where crossed
387	    # Use argmax on the crossed array (first True)
388	    any_crossed = crossed.any(axis=0)  # (M,)
389	    first_idx = crossed.argmax(axis=0)  # (M,) — 0 if never crossed
390	    asv_vals = np.where(any_crossed, DELTAS[first_idx], np.inf)
391	
392	    return asv_vals
393	
394	
395	def process_batch_exposure(C0_batch, ss, tau_true):
396	    """Process batch for exposure topology.
397	
398	    Returns:
399	        asv_vals: (M,) ASV values
400	        worst_devs: (M,) worst monotonicity violation per matrix
401	    """
402	    M = C0_batch.shape[0]
403	    # Precompute C0 @ ss.p_A and C0 @ ss.E_YD for all matrices
404	    pA0 = np.einsum('mkj,j->mk', C0_batch, ss.p_A)  # (M, K)
405	    YD0 = np.einsum('mkj,j->mk', C0_batch, ss.E_YD)  # (M, K)
406	
407	    d = DELTAS[:, None, None]  # (N_DELTA, 1, 1)
408	    # q[delta, m, k] = (1-delta)*ss.p_A[k] + delta*pA0[m, k]
409	    q = (1 - d) * ss.p_A[None, None, :] + d * pA0[None, :, :]
410	    cy = (1 - d) * ss.E_YD[None, None, :] + d * YD0[None, :, :]
411	
412	    # Build EZZ: (N_DELTA, M, K, K) — but K=3, so (N_D, M, 3, 3)
413	    dim = K
414	    EZZ = np.zeros((N_DELTA, M, dim, dim))
415	    EZZ[:, :, 0, 0] = 1.0
416	    EZZ[:, :, 0, 1:] = q[:, :, 1:]
417	    EZZ[:, :, 1:, 0] = q[:, :, 1:]
418	    for j in range(K - 1):
419	        EZZ[:, :, j + 1, j + 1] = q[:, :, j + 1]
420	
421	    EZY = np.zeros((N_DELTA, M, dim))
422	    EZY[:, :, 0] = ss.E_Y
423	    EZY[:, :, 1:] = cy[:, :, 1:]
424	
425	    # Solve for all at once: (N_DELTA * M, dim, dim) solve
426	    EZZ_flat = EZZ.reshape(-1, dim, dim)
427	    EZY_flat = EZY.reshape(-1, dim, 1)
428	    try:
429	        coefs_flat = np.linalg.solve(EZZ_flat, EZY_flat)[:, :, 0]
430	    except np.linalg.LinAlgError:
431	        coefs_flat = np.full((N_DELTA * M, dim), np.nan)
432	    taus = coefs_flat[:, 1].reshape(N_DELTA, M)
433	
434	    bias_abs = np.abs(taus - tau_true)
435	
436	    # ASV
437	    envelope = np.fmax.accumulate(np.nan_to_num(bias_abs, nan=0.0), axis=0)
438	    crossed = envelope > ASV_EPSILON
439	    any_crossed = crossed.any(axis=0)
440	    first_idx = crossed.argmax(axis=0)
441	    asv_vals = np.where(any_crossed, DELTAS[first_idx], np.inf)
442	
443	    # Monotonicity: non-decreasing
444	    valid_bias = np.nan_to_num(bias_abs, nan=0.0)
445	    diffs = np.diff(valid_bias, axis=0)  # (N_DELTA-1, M)
446	    violations = np.where(diffs < -MONO_TOL, -diffs, 0.0)
447	    worst_devs = violations.max(axis=0)  # (M,)
448	
449	    return asv_vals, worst_devs
450	
451	
452	def process_batch_with_T(C0_batch, ss, tau_true, topo):
453	    """Process batch for topologies with treatment T.
454	
455	    Returns:
456	        asv_vals: (M,) ASV values (None if protective)
457	        worst_devs: (M,) worst monotonicity violation per matrix
458	    """
459	    M = C0_batch.shape[0]
460	    pA0 = np.einsum('mkj,j->mk', C0_batch, ss.p_A)
461	    TD0 = np.einsum('mkj,j->mk', C0_batch, ss.E_TD)
462	    YD0 = np.einsum('mkj,j->mk', C0_batch, ss.E_YD)
463	
464	    d = DELTAS[:, None, None]
465	    q = (1 - d) * ss.p_A[None, None, :] + d * pA0[None, :, :]
466	    ct = (1 - d) * ss.E_TD[None, None, :] + d * TD0[None, :, :]
467	    cy = (1 - d) * ss.E_YD[None, None, :] + d * YD0[None, :, :]
468	
469	    dim = K + 1
470	    EZZ = np.zeros((N_DELTA, M, dim, dim))
471	    EZZ[:, :, 0, 0] = 1.0
472	    EZZ[:, :, 0, 1] = ss.E_T
473	    EZZ[:, :, 1, 0] = ss.E_T
474	    EZZ[:, :, 1, 1] = ss.E_T2
475	    EZZ[:, :, 0, 2:] = q[:, :, 1:]
476	    EZZ[:, :, 2:, 0] = q[:, :, 1:]
477	    EZZ[:, :, 1, 2:] = ct[:, :, 1:]
478	    EZZ[:, :, 2:, 1] = ct[:, :, 1:]
479	    for j in range(K - 1):
480	        EZZ[:, :, j + 2, j + 2] = q[:, :, j + 1]
481	
482	    EZY = np.zeros((N_DELTA, M, dim))
483	    EZY[:, :, 0] = ss.E_Y
484	    EZY[:, :, 1] = ss.E_TY
485	    EZY[:, :, 2:] = cy[:, :, 1:]
486	
487	    EZZ_flat = EZZ.reshape(-1, dim, dim)
488	    EZY_flat = EZY.reshape(-1, dim, 1)
489	    try:
490	        coefs_flat = np.linalg.solve(EZZ_flat, EZY_flat)[:, :, 0]
491	    except np.linalg.LinAlgError:
492	        coefs_flat = np.full((N_DELTA * M, dim), np.nan)
493	    taus = coefs_flat[:, 1].reshape(N_DELTA, M)
494	
495	    bias_abs = np.abs(taus - tau_true)
496	
497	    # ASV (only for non-protective topologies)
498	    asv_vals = None
499	    if topo not in PROTECTIVE:
500	        envelope = np.fmax.accumulate(
501	            np.nan_to_num(bias_abs, nan=0.0), axis=0)
502	        crossed = envelope > ASV_EPSILON
503	        any_crossed = crossed.any(axis=0)
504	        first_idx = crossed.argmax(axis=0)
505	        asv_vals = np.where(any_crossed, DELTAS[first_idx], np.inf)
506	
507	    # Monotonicity
508	    valid_bias = np.nan_to_num(bias_abs, nan=0.0)
509	    diffs = np.diff(valid_bias, axis=0)
510	    if topo in NON_DECREASING:
511	        violations = np.where(diffs < -MONO_TOL, -diffs, 0.0)
512	    else:
513	        violations = np.where(diffs > MONO_TOL, diffs, 0.0)
514	    worst_devs = violations.max(axis=0)
515	
516	    return asv_vals, worst_devs
517	
518	
519	# ====================================================================
520	# Main
521	# ====================================================================
522	def main():
523	    t_total = time.time()
524	
525	    print("ASV Topology Ranking Stability Analysis")
526	    print(f"  N_matrices = {N_MATRICES:,}")
527	    print(f"  K = {K}, ASV_threshold = {ASV_EPSILON}")
528	    print(f"  Perturbation epsilon = {PERTURB_EPSILON}")
529	    print(f"  delta_step = {DELTA_STEP}, n_delta = {N_DELTA}")
530	    print(f"  GH quadrature: {N_GH} pts/dim")
531	    print(f"  Chunk size: {CHUNK_SIZE:,}")
532	    print(f"  Seed = {SEED}")
533	    print("=" * 70)
534	    sys.stdout.flush()
535	
536	    # ── Precompute sufficient statistics ──────────────────────────────
537	    print("\nPrecomputing analytic sufficient statistics...")
538	    all_ss = {}
539	    all_tau_true = {}
540	    for topo in ALL_TOPOS:
541	        ss = COMPUTE_SS[topo](DGP_PARAMS[topo])
542	        all_ss[topo] = ss
543	        all_tau_true[topo] = get_tau_true(topo, ss)
544	        print(f"  {topo:<14} tau_true = {all_tau_true[topo]:.10f}")
545	    sys.stdout.flush()
546	
547	    # ── Generate random confusion matrices ────────────────────────────
548	    print(f"\nGenerating {N_MATRICES:,} Dirichlet(1,1,1) C0 matrices...")
549	    sys.stdout.flush()
550	    rng = np.random.default_rng(SEED)
551	    all_C0 = np.zeros((N_MATRICES, K, K))
552	    for j in range(K):
553	        all_C0[:, :, j] = rng.dirichlet(np.ones(K), size=N_MATRICES)
554	
555	    # ── Storage ───────────────────────────────────────────────────────
556	    ranking_topo_idx = {t: i for i, t in enumerate(RANKING_TOPOS)}
557	    n_rank = len(RANKING_TOPOS)
558	    asv_matrix = np.full((N_MATRICES, n_rank), np.nan)
559	
560	    # Collider and M-bias: ASV = inf (protective)
561	    asv_matrix[:, ranking_topo_idx['collider']] = np.inf
562	    asv_matrix[:, ranking_topo_idx['mbias']] = np.inf
563	
564	    worst_step_dev = {t: 0.0 for t in CONJECTURE_TOPOS}
565	    violation_count = {t: 0 for t in CONJECTURE_TOPOS}
566	
567	    # ── Process topologies in chunks ──────────────────────────────────
568	    print(f"\nProcessing topologies (chunk_size={CHUNK_SIZE:,})...")
569	    sys.stdout.flush()
570	
571	    n_chunks = (N_MATRICES + CHUNK_SIZE - 1) // CHUNK_SIZE
572	
573	    for topo in ALL_TOPOS:
574	        t0 = time.time()
575	        ss = all_ss[topo]
576	        tau_true = all_tau_true[topo]
577	
578	        need_asv = (topo in ranking_topo_idx and topo not in PROTECTIVE)
579	        need_conj = topo in CONJECTURE_TOPOS
580	
581	        if not need_asv and not need_conj:
582	            continue
583	
584	        topo_worst = 0.0
585	        topo_viol = 0
586	
587	        for c in range(n_chunks):
588	            start = c * CHUNK_SIZE
589	            end = min(start + CHUNK_SIZE, N_MATRICES)
590	            C0_chunk = all_C0[start:end]
591	
592	            if topo == 'iv':
593	                asv_vals = process_batch_iv(C0_chunk, ss, tau_true)
594	                if need_asv:
595	                    asv_matrix[start:end, ranking_topo_idx[topo]] = asv_vals
596	                # No conjecture for IV
597	            elif topo == 'exposure':
598	                asv_vals, w_devs = process_batch_exposure(
599	                    C0_chunk, ss, tau_true)
600	                if need_asv:
601	                    asv_matrix[start:end, ranking_topo_idx[topo]] = asv_vals
602	                if need_conj:
603	                    chunk_worst = float(w_devs.max())
604	                    topo_worst = max(topo_worst, chunk_worst)
605	                    topo_viol += int((w_devs > 0).sum())
606	            else:
607	                asv_vals, w_devs = process_batch_with_T(
608	                    C0_chunk, ss, tau_true, topo)
609	                if need_asv and asv_vals is not None:
610	                    asv_matrix[start:end, ranking_topo_idx[topo]] = asv_vals
611	                if need_conj:
612	                    chunk_worst = float(w_devs.max())
613	                    topo_worst = max(topo_worst, chunk_worst)
614	                    topo_viol += int((w_devs > 0).sum())
615	
616	            if (c + 1) % max(1, n_chunks // 5) == 0:
617	                elapsed = time.time() - t0
618	                frac = (c + 1) / n_chunks
619	                eta = elapsed / frac * (1 - frac)
620	                print(f"    {topo}: chunk {c+1}/{n_chunks} "
621	                      f"({elapsed:.0f}s, ~{eta:.0f}s left)")
622	                sys.stdout.flush()
623	
624	        if need_conj:
625	            worst_step_dev[topo] = topo_worst
626	            violation_count[topo] = topo_viol
627	
628	        elapsed = time.time() - t0
629	        extras = []
630	        if need_conj:
631	            extras.append(f"worst_dev={topo_worst:.2e}")
632	            extras.append(f"viol={topo_viol}")
633	        if need_asv and topo in ranking_topo_idx:
634	            col = asv_matrix[:, ranking_topo_idx[topo]]
635	            finite = col[np.isfinite(col)]
636	            if len(finite) > 0:
637	                extras.append(f"med_ASV={np.median(finite):.4f}")
638	        print(f"  {topo:<14} {elapsed:.1f}s  {', '.join(extras)}")
639	        sys.stdout.flush()
640	
641	    # ── Part 1: Kendall tau ranking analysis ──────────────────────────
642	    print("\n" + "=" * 70)
643	    print("PART 1: ASV Topology Ranking Stability")
644	    print("=" * 70)
645	
646	    theoretical_ranks = np.array([
647	        THEORETICAL_RANKING_ORDER.index(t) + 1 for t in RANKING_TOPOS
648	    ], dtype=float)
649	
650	    # Vectorized Kendall tau for all valid matrices
651	    valid_mask = ~np.any(np.isnan(asv_matrix), axis=1)
652	    n_valid = int(valid_mask.sum())
653	
654	    kendall_taus = np.full(N_MATRICES, np.nan)
655	    exact_match_count = 0
656	
657	    if n_valid > 0:
658	        valid_asv = asv_matrix[valid_mask]
659	        emp_ranks = np.apply_along_axis(
660	            lambda x: rankdata(x, method='average'), 1, valid_asv)
661	
662	        theo_order = np.argsort(theoretical_ranks)
663	
664	        for idx in range(n_valid):
665	            tau_corr, _ = kendalltau(theoretical_ranks, emp_ranks[idx])
666	            orig_idx = np.where(valid_mask)[0][idx]
667	            kendall_taus[orig_idx] = tau_corr
668	
669	            emp_order = np.argsort(emp_ranks[idx])
670	            if np.array_equal(theo_order, emp_order):
671	                exact_match_count += 1
672	
673	    valid_taus = kendall_taus[~np.isnan(kendall_taus)]
674	    mean_tau = float(np.mean(valid_taus)) if len(valid_taus) > 0 else float('nan')
675	    min_tau = float(np.min(valid_taus)) if len(valid_taus) > 0 else float('nan')
676	    median_tau = float(np.median(valid_taus)) if len(valid_taus) > 0 else float('nan')
677	    exact_frac = exact_match_count / n_valid if n_valid > 0 else 0.0
678	
679	    print(f"  Valid rankings: {n_valid:,} / {N_MATRICES:,}")
680	    print(f"  Kendall tau:")
681	    print(f"    Mean:   {mean_tau:.4f}")
682	    print(f"    Median: {median_tau:.4f}")
683	    print(f"    Min:    {min_tau:.4f}")
684	    print(f"  Exact match: {exact_match_count:,}/{n_valid:,} ({exact_frac:.6f})")
685	
686	    tau_dist = {}
687	    for t in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
688	        frac = float(np.mean(valid_taus >= t)) if len(valid_taus) > 0 else 0.0
689	        tau_dist[f"ge_{t:.1f}"] = frac
690	        print(f"    tau >= {t:.1f}: {frac:.4f}")
691	    sys.stdout.flush()
692	
693	    # ── Part 2: epsilon-perturbation ranking robustness ───────────────
694	    print("\n" + "=" * 70)
695	    print(f"PART 2: Perturbation Robustness (eps={PERTURB_EPSILON})")
696	    print("=" * 70)
697	
698	    # Vectorized: for each valid matrix, check all pairs
699	    n_reversals = 0
700	    n_pair_reversals = 0
701	    n_checked = n_valid
702	    n_pairs_per = n_rank * (n_rank - 1) // 2
703	    n_pairs_total = n_checked * n_pairs_per
704	
705	    if n_valid > 0:
706	        valid_asv = asv_matrix[valid_mask]
707	        for a in range(n_rank):
708	            for b in range(a + 1, n_rank):
709	                va = valid_asv[:, a]
710	                vb = valid_asv[:, b]
711	                # Both inf => no reversal
712	                both_inf = np.isinf(va) & np.isinf(vb)
713	                gap = np.abs(va - vb)
714	                pair_rev = (~both_inf) & (gap < 2 * PERTURB_EPSILON)
715	                n_pair_reversals += int(pair_rev.sum())
716	
717	        # Count matrices with any reversal
718	        has_reversal = np.zeros(n_valid, dtype=bool)
719	        for a in range(n_rank):
720	            for b in range(a + 1, n_rank):
721	                va = valid_asv[:, a]
722	                vb = valid_asv[:, b]
723	                both_inf = np.isinf(va) & np.isinf(vb)
724	                gap = np.abs(va - vb)
725	                has_reversal |= (~both_inf) & (gap < 2 * PERTURB_EPSILON)
726	        n_reversals = int(has_reversal.sum())
727	
728	    rev_frac = n_reversals / n_checked if n_checked > 0 else 0.0
729	    pair_rev_frac = (n_pair_reversals / n_pairs_total
730	                     if n_pairs_total > 0 else 0.0)
731	
732	    print(f"  Matrices checked: {n_checked:,}")
733	    print(f"  Any pairwise reversal: {n_reversals:,}/{n_checked:,} "
734	          f"({rev_frac:.4f})")
735	    print(f"  Pairwise reversals: {n_pair_reversals:,}/{n_pairs_total:,} "
736	          f"({pair_rev_frac:.4f})")
737	    sys.stdout.flush()
738	
739	    # ── Part 3: Conjecture verification ───────────────────────────────
740	    print("\n" + "=" * 70)
741	    print("PART 3: Conjecture Verification (non-IV topologies)")
742	    print("=" * 70)
743	
744	    global_worst = 0.0
745	    global_worst_topo = None
746	    total_viol = 0
747	
748	    for topo in CONJECTURE_TOPOS:
749	        dev = worst_step_dev[topo]
750	        viol = violation_count[topo]
751	        direction = "non-dec" if topo in NON_DECREASING else "non-inc"
752	        total_viol += viol
753	        print(f"  {topo:<14} [{direction}]  worst_dev={dev:.6e}  "
754	              f"violations={viol:,}/{N_MATRICES:,}")
755	        if dev > global_worst:
756	            global_worst = dev
757	            global_worst_topo = topo
758	
759	    print(f"\n  Global worst step deviation: {global_worst:.6e} "
760	          f"({global_worst_topo})")
761	    conj_holds = global_worst < 0.06
762	    print(f"  Conjecture holds (worst_dev < 0.06)? {conj_holds}")
763	    sys.stdout.flush()
764	
765	    # ── ASV summary ───────────────────────────────────────────────────
766	    print("\n" + "=" * 70)
767	    print("ASV Summary (per topology)")
768	    print("=" * 70)
769	    asv_summary = {}
770	    for topo in RANKING_TOPOS:
771	        col = asv_matrix[:, ranking_topo_idx[topo]]
772	        finite = col[np.isfinite(col) & ~np.isnan(col)]
773	        pct_inf = float(np.mean(np.isinf(col) & (col > 0)) * 100)
774	        pct_nan = float(np.mean(np.isnan(col)) * 100)
775	        if len(finite) > 0:
776	            med = float(np.median(finite))
777	            mn = float(np.mean(finite))
778	            print(f"  {topo:<14} median={med:.4f}  mean={mn:.4f}  "
779	                  f"immune={pct_inf:.1f}%  NaN={pct_nan:.1f}%")
780	            asv_summary[topo] = {
781	                "median": med, "mean": mn,
782	                "pct_immune": pct_inf, "pct_nan": pct_nan
783	            }
784	        else:
785	            print(f"  {topo:<14} all inf/NaN  immune={pct_inf:.1f}%  "
786	                  f"NaN={pct_nan:.1f}%")
787	            asv_summary[topo] = {
788	                "median": None, "mean": None,
789	                "pct_immune": pct_inf, "pct_nan": pct_nan
790	            }
791	    sys.stdout.flush()
792	
793	    # ── Save results ──────────────────────────────────────────────────
794	    total_time = time.time() - t_total
795	
796	    results = {
797	        "description": "ASV topology ranking stability analysis",
798	        "config": {
799	            "n_matrices": N_MATRICES,
800	            "K": K,
801	            "asv_threshold": ASV_EPSILON,
802	            "perturbation_epsilon": PERTURB_EPSILON,
803	            "delta_step": DELTA_STEP,
804	            "n_delta": N_DELTA,
805	            "gh_quadrature_points": N_GH,
806	            "mono_tol": MONO_TOL,
807	            "seed": SEED,
808	            "theoretical_ranking": THEORETICAL_RANKING_ORDER,
809	        },
810	        "part1_ranking_stability": {
811	            "n_valid_rankings": n_valid,
812	            "kendall_tau_mean": mean_tau,
813	            "kendall_tau_median": median_tau,
814	            "kendall_tau_min": min_tau,
815	            "exact_match_count": exact_match_count,
816	            "exact_match_fraction": exact_frac,
817	            "tau_distribution": tau_dist,
818	        },
819	        "part2_perturbation_robustness": {
820	            "n_checked": n_checked,
821	            "n_reversals": n_reversals,
822	            "reversal_fraction": rev_frac,
823	            "n_pair_reversals": n_pair_reversals,
824	            "n_pairs_total": n_pairs_total,
825	            "pair_reversal_fraction": pair_rev_frac,
826	        },
827	        "part3_conjecture_verification": {
828	            "global_worst_step_deviation": global_worst,
829	            "global_worst_topology": global_worst_topo,
830	            "conjecture_holds_0_06": conj_holds,
831	            "per_topology": {
832	                topo: {
833	                    "worst_step_deviation": worst_step_dev[topo],
834	                    "violation_count": violation_count[topo],
835	                    "direction": ("non-dec" if topo in NON_DECREASING
836	                                  else "non-inc"),
837	                }
838	                for topo in CONJECTURE_TOPOS
839	            },
840	        },
841	        "asv_summary": asv_summary,
842	        "total_time_seconds": total_time,
843	    }
844	
845	    out_path = os.path.join(OUT_DIR, 'ranking_stability_results.json')
846	    with open(out_path, 'w') as f:
847	        json.dump(results, f, indent=2)
848	    print(f"\nJSON saved: {out_path}")
849	
850	    print(f"\n{'=' * 70}")
851	    print("SUMMARY")
852	    print(f"{'=' * 70}")
853	    print(f"  Kendall tau: mean={mean_tau:.4f}, median={median_tau:.4f}, "
854	          f"min={min_tau:.4f}")
855	    print(f"  Exact ranking match: {exact_frac:.6f}")
856	    print(f"  Reversal rate (eps={PERTURB_EPSILON}): {rev_frac:.4f}")
857	    print(f"  Worst |B| step deviation: {global_worst:.6e} "
858	          f"({global_worst_topo})")
859	    print(f"  Conjecture holds: {conj_holds}")
860	    print(f"  Total time: {total_time:.1f}s ({total_time/60:.1f}min)")
861	    print(f"{'=' * 70}")
862	
863	
864	if __name__ == "__main__":
865	    main()
866	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d4551d21-939e-428a-b1ff-764c9443fedc",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "864a44fd-1a61-4015-b79d-c2c2c8683ceb",
  "sourceToolAssistantUUID": "d4551d21-939e-428a-b1ff-764c9443fedc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-23T14:57:00.391Z_

<details><summary>↩ Tool result · `toolu_01SkBELojKFb5i1pckyoxYim`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Three computational tasks for the causal annotation error attribution paper.
4	
5	Task 1: Theory-Empirical MAPE (extend existing humaid-only to all 18 valid configs)
6	Task 2: PPI++ Empirical Validation (simulate gold labels, apply PPI++ correction)
7	Task 3: Dirichlet Subspace Overlay (regenerated with improved styling)
8	
9	Author: auto-generated for paper artifacts
10	"""
11	
12	import json
13	import sys
14	import time
15	import numpy as np
16	from pathlib import Path
17	from collections import defaultdict
18	
19	PROJ = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib")
20	sys.path.insert(0, str(PROJ))
21	
22	# Import the plan_006 module for DGP generators matching the paper's setup
23	import importlib.util
24	spec = importlib.util.spec_from_file_location(
25	    "plan_006",
26	    str(PROJ / "plan_006_asv_empirical.py")
27	)
28	plan_006 = importlib.util.module_from_spec(spec)
29	spec.loader.exec_module(plan_006)
30	
31	from annot_sensitivity.correction import correct_ppi, correct_naive_plugin, correct_mla
32	from annot_sensitivity.utils import misclassify
33	
34	# ============================================================================
35	# Common data loading
36	# ============================================================================
37	
38	TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
39	              'mbias', 'iv', 'frontdoor']
40	HAS_TREATMENT = {'confounding', 'mediation', 'collider', 'mbias', 'frontdoor'}
41	
42	
43	def load_all_data():
44	    """Load confusion matrices and bias records for all 18 valid configs."""
45	    # Load humaid confusion matrices (full 10x10)
46	    with open(PROJ / "artifacts/plan006/asv_empirical_results.json") as f:
47	        plan006 = json.load(f)
48	    humaid_cms = {k: np.array(v) for k, v in plan006["confusion_matrices"].items()}
49	    bias_records = plan006["biases"]
50	
51	    # Load filter info
52	    with open(PROJ / "artifacts/plan006_full_filtered_stats.json") as f:
53	        filter_data = json.load(f)
54	    zero_configs = set(filter_data["zero_configs"])
55	
56	    # Valid humaid configs (8 of 9, excluding qwen3_few-shot-5)
57	    humaid_valid = {k: humaid_cms[k] for k in humaid_cms if k not in zero_configs}
58	
59	    # Build bias lookup for humaid
60	    bias_lookup = {}
61	    for b in bias_records:
62	        ck = f"{b['dataset']}_{b['model']}_{b['prompt']}"
63	        if ck not in zero_configs and b.get('bias') is not None:
64	            bias_lookup[(ck, b['topology'])] = b
65	
66	    # VAST confusion matrices: we only have per-class recall (diagonal).
67	    # For VAST we need to construct approximate confusion matrices from the
68	    # diagonal data. The VAST per-class recall gives us C_kk for each class.
69	    # We distribute off-diagonal mass uniformly (best available approximation).
70	    vast_per_class_recall = filter_data["filtered_stats"]["vast_per_class_recall"]
71	    vast_cms = {}
72	    for key, diag in vast_per_class_recall.items():
73	        # key format: "vast_llama4_zero-shot"
74	        config_key = key  # already has "vast_" prefix
75	        K = 3
76	        C = np.zeros((K, K))
77	        for i in range(K):
78	            C[i, i] = diag[i]
79	            off_diag_mass = 1.0 - diag[i]
80	            for j in range(K):
81	                if j != i:
82	                    C[j, i] = off_diag_mass / (K - 1)
83	        vast_cms[config_key] = C
84	
85	    # CivilComments: we have trace/macro_recall from filtered_stats
86	    # For K=2, trace = C[0,0] + C[1,1], macro_recall = trace/2
87	    # We use the CC diagonal values from gen_fig7.py (extracted from the pipeline)
88	    civil_diag = {
89	        "civil_comments_qwen2.5-7b_zero-shot":  [0.7481536189069424, 0.684931506849315],
90	        "civil_comments_qwen2.5-7b_few-shot-3": [0.6787296898079763, 0.7808219178082192],
91	        "civil_comments_qwen2.5-7b_few-shot-5": [0.7370753323485968, 0.7602739726027398],
92	    }
93	    civil_cms = {}
94	    for key, diag in civil_diag.items():
95	        K = 2
96	        C = np.zeros((K, K))
97	        C[0, 0] = diag[0]
98	        C[1, 1] = diag[1]
99	        C[1, 0] = 1.0 - diag[0]
100	        C[0, 1] = 1.0 - diag[1]
101	        civil_cms[key] = C
102	
103	    # Merge all confusion matrices
104	    all_cms = {}
105	    all_cms.update(humaid_valid)
106	    all_cms.update(vast_cms)
107	    all_cms.update(civil_cms)
108	
109	    # Config metadata
110	    config_meta = {}
111	    for k, C in all_cms.items():
112	        parts = k.split("_", 1)
113	        dataset = parts[0]
114	        if dataset == "civil":
115	            dataset = "civil_comments"
116	            model_prompt = k[len("civil_comments_"):]
117	        elif dataset == "vast":
118	            model_prompt = k[len("vast_"):]
119	        else:
120	            model_prompt = k[len("humaid_"):]
121	        K = C.shape[0]
122	        config_meta[k] = {
123	            "dataset": dataset,
124	            "model_prompt": model_prompt,
125	            "K": K,
126	            "min_diag": float(np.min(np.diag(C))),
127	            "trace": float(np.trace(C)),
128	            "macro_recall": float(np.trace(C) / K),
129	        }
130	
131	    return all_cms, config_meta, bias_lookup, filter_data
132	
133	
134	# ============================================================================
135	# Task 1: Theory-Empirical MAPE
136	# ============================================================================
137	
138	def task1_mape(all_cms, config_meta, bias_lookup):
139	    """Compute MAPE between analytical plim bias and finite-sample MC bias."""
140	    print("=" * 80)
141	    print("TASK 1: Theory-Empirical MAPE")
142	    print("=" * 80)
143	    t0 = time.time()
144	
145	    N_MC = 200
146	    N_SAMPLES = 10_000
147	
148	    # Precompute sufficient stats and tau_true for each K
149	    Ks_used = sorted(set(m["K"] for m in config_meta.values()))
150	    params_by_K = {K: plan_006.make_dgp_params(K) for K in Ks_used}
151	    suff_stats = {}
152	    tau_true_cache = {}
153	
154	    for K in Ks_used:
155	        for topo in TOPOLOGIES:
156	            st = plan_006.precompute_suff_stats(K, topo, params_by_K[K][topo])
157	            suff_stats[(K, topo)] = st
158	            plim_I = plan_006.compute_plim(np.eye(K), st, K)
159	            tau_true_cache[(K, topo)] = plan_006.extract_tau(plim_I, topo)
160	            print(f"  K={K:>2} {topo:<12} tau_true={tau_true_cache[(K, topo)]:.6f}")
161	
162	    per_config = {}
163	    per_topology = defaultdict(list)
164	    grand_records = []
165	
166	    for config_key, C in sorted(all_cms.items()):
167	        meta = config_meta[config_key]
168	        K = meta["K"]
169	        params = params_by_K[K]
170	        per_config[config_key] = {}
171	        print(f"\n[{config_key}] K={K}, min_diag={meta['min_diag']:.4f}")
172	
173	        for topo in TOPOLOGIES:
174	            tau_true = tau_true_cache[(K, topo)]
175	            st = suff_stats[(K, topo)]
176	
177	            # Compute analytical plim (theory bias)
178	            plim_C = plan_006.compute_plim(C, st, K)
179	            tau_biased = plan_006.extract_tau(plim_C, topo)
180	            if not np.isfinite(tau_biased) or not np.isfinite(tau_true):
181	                continue
182	            theory_bias = tau_biased - tau_true
183	
184	            # MC empirical bias
185	            tau_hats = []
186	            for mc_i in range(N_MC):
187	                seed = (hash(config_key + topo) & 0xFFFFFFFF) + mc_i * 7919
188	                try:
189	                    rng = np.random.default_rng(seed)
190	                    first_var, Y, A = plan_006.GEN_FNS[topo](K, N_SAMPLES,
191	                                                              params[topo], rng)
192	                    A_star = plan_006.generate_Astar(A, C, rng)
193	
194	                    if topo == 'iv':
195	                        Z = first_var
196	                        W, _ = plan_006.wald_estimator(Z, Y, A_star, k=1)
197	                        if np.isfinite(W):
198	                            tau_hats.append(float(W))
199	                    elif topo == 'exposure':
200	                        beta, _ = plan_006.ols_no_T(Y, A_star, K)
201	                        if len(beta) > 1 and np.isfinite(beta[1]):
202	                            tau_hats.append(float(beta[1]))
203	                    else:
204	                        T = first_var
205	                        beta, _ = plan_006.ols_with_dummies(Y, T, A_star, K)
206	                        if np.isfinite(beta[1]):
207	                            tau_hats.append(float(beta[1]))
208	                except Exception:
209	                    continue
210	
211	            if len(tau_hats) < N_MC // 2:
212	                print(f"  {topo:<12} MC FAILED ({len(tau_hats)}/{N_MC})")
213	                continue
214	
215	            tau_mean = float(np.mean(tau_hats))
216	            tau_se = float(np.std(tau_hats, ddof=1) / np.sqrt(len(tau_hats)))
217	            mc_bias = tau_mean - tau_true
218	
219	            if abs(theory_bias) > 1e-12:
220	                ape = abs(theory_bias - mc_bias) / abs(theory_bias)
221	            else:
222	                ape = float('nan')
223	
224	            entry = {
225	                'theory_bias': float(theory_bias),
226	                'mc_bias': float(mc_bias),
227	                'mc_tau_mean': tau_mean,
228	                'mc_tau_se': tau_se,
229	                'tau_true': float(tau_true),
230	                'tau_biased_plim': float(tau_biased),
231	                'abs_pct_error': float(ape) if np.isfinite(ape) else None,
232	                'n_mc_used': len(tau_hats),
233	            }
234	            per_config[config_key][topo] = entry
235	            if np.isfinite(ape):
236	                per_topology[topo].append(ape)
237	                grand_records.append(ape)
238	            print(f"  {topo:<12} theory={theory_bias:+.5f}  MC={mc_bias:+.5f}  "
239	                  f"APE={ape:.3%}")
240	
241	    # Aggregate
242	    per_topology_summary = {}
243	    for topo in TOPOLOGIES:
244	        apes = per_topology.get(topo, [])
245	        finite = [a for a in apes if np.isfinite(a)]
246	        per_topology_summary[topo] = {
247	            'mape': float(np.mean(finite)) if finite else None,
248	            'median_ape': float(np.median(finite)) if finite else None,
249	            'max_ape': float(np.max(finite)) if finite else None,
250	            'n': len(finite),
251	        }
252	
253	    grand_mape = float(np.mean(grand_records)) if grand_records else None
254	
255	    output = {
256	        'meta': {
257	            'n_mc': N_MC,
258	            'n_samples': N_SAMPLES,
259	            'scope': f'All {len(all_cms)} valid configs (K=2,3,10)',
260	            'n_valid_configs': len(all_cms),
261	            'n_scenarios_total': len(grand_records),
262	            'topologies': TOPOLOGIES,
263	            'note': (
264	                'VAST and CivilComments use approximate confusion matrices '
265	                '(diagonal from per-class recall, off-diagonal uniform). '
266	                'HumAID uses full empirical confusion matrices.'
267	            ),
268	        },
269	        'grand_mape': grand_mape,
270	        'per_topology': per_topology_summary,
271	        'per_config': per_config,
272	    }
273	
274	    out_path = PROJ / "artifacts/theory_empirical_mape.json"
275	    out_path.write_text(json.dumps(output, indent=2))
276	    print(f"\n=== Task 1 DONE in {time.time()-t0:.1f}s ===")
277	    print(f"Grand MAPE: {grand_mape:.4%}" if grand_mape else "Grand MAPE: N/A")
278	    print(f"Written: {out_path}")
279	
280	    # LaTeX snippet
281	    latex = r"""% Theory-Empirical MAPE (auto-generated)
282	% Grand MAPE across """ + f"{len(grand_records)} scenarios: {grand_mape:.2%}" + r"""
283	\begin{table}[h]\centering\small
284	\caption{Theory vs.\ MC MAPE per topology}
285	\begin{tabular}{lrrr}
286	\toprule
287	Topology & MAPE (\%) & Median APE (\%) & $n$ \\
288	\midrule
289	"""
290	    for topo in TOPOLOGIES:
291	        s = per_topology_summary[topo]
292	        if s['mape'] is not None:
293	            latex += f"{topo} & {100*s['mape']:.2f} & {100*s['median_ape']:.2f} & {s['n']} \\\\\n"
294	    latex += r"""\midrule
295	Grand & """ + f"{100*grand_mape:.2f}" + r""" & -- & """ + f"{len(grand_records)}" + r""" \\
296	\bottomrule
297	\end{tabular}
298	\end{table}
299	"""
300	    latex_path = PROJ / "artifacts/theory_empirical_mape_table.tex"
301	    latex_path.write_text(latex)
302	    print(f"LaTeX: {latex_path}")
303	
304	    return output
305	
306	
307	# ============================================================================
308	# Task 2: PPI++ Empirical Validation
309	# ============================================================================
310	
311	def task2_ppi(all_cms, config_meta):
312	    """PPI++ empirical validation on all configs x topologies."""
313	    print("\n" + "=" * 80)
314	    print("TASK 2: PPI++ Empirical Validation")
315	    print("=" * 80)
316	    t0 = time.time()
317	
318	    N_SAMPLES = 10_000
319	    N_MC = 50  # fewer MC reps since PPI++ itself has internal bootstrap
320	    GOLD_FRACTION = 0.1
321	
322	    Ks_used = sorted(set(m["K"] for m in config_meta.values()))
323	    params_by_K = {K: plan_006.make_dgp_params(K) for K in Ks_used}
324	    suff_stats = {}
325	    tau_true_cache = {}
326	
327	    for K in Ks_used:
328	        for topo in TOPOLOGIES:
329	            st = plan_006.precompute_suff_stats(K, topo, params_by_K[K][topo])
330	            suff_stats[(K, topo)] = st
331	            plim_I = plan_006.compute_plim(np.eye(K), st, K)
332	            tau_true_cache[(K, topo)] = plan_006.extract_tau(plim_I, topo)
333	
334	    results = {}
335	    summary_by_topo = defaultdict(list)
336	    summary_by_K = defaultdict(list)
337	
338	    for config_key, C in sorted(all_cms.items()):
339	        meta = config_meta[config_key]
340	        K = meta["K"]
341	        params = params_by_K[K]
342	        results[config_key] = {}
343	        print(f"\n[{config_key}] K={K}")
344	
345	        for topo in TOPOLOGIES:
346	            tau_true = tau_true_cache[(K, topo)]
347	            st = suff_stats[(K, topo)]
348	
349	            # Skip IV for PPI++ (PPI++ requires OLS, IV uses Wald estimator)
350	            if topo == 'iv':
351	                # For IV, compute theoretical C^{-1} correction effectiveness instead
352	                cond = np.linalg.cond(C)
353	                try:
354	                    C_inv = np.linalg.inv(C)
355	                    # Theoretical: tau_corrected = RF / (C^{-1} C @ FS)[1] = RF / FS[1] = tau_true
356	                    # So C^{-1} correction should theoretically give 100% bias reduction for IV
357	                    # But this is the Wald estimator - C^{-1} on the first stage only
358	                    plim_C = plan_006.compute_plim(C, st, K)
359	                    tau_biased = plan_006.extract_tau(plim_C, topo)
360	                    bias_biased = tau_biased - tau_true
361	                    # C^{-1} correction of first stage: effective C becomes I
362	                    tau_corrected = tau_true  # theoretical perfect correction
363	                    results[config_key][topo] = {
364	                        'method': 'theoretical_Cinv',
365	                        'tau_true': float(tau_true),
366	                        'tau_biased': float(tau_biased),
367	                        'tau_corrected': float(tau_corrected),
368	                        'bias_biased': float(bias_biased),
369	                        'bias_corrected': 0.0,
370	                        'bias_reduction_pct': 100.0 if abs(bias_biased) > 1e-12 else 0.0,
371	                        'cond_C': float(cond),
372	                        'note': 'IV topology: theoretical C^{-1} correction = perfect (by construction)',
373	                    }
374	                    summary_by_topo[topo].append(100.0)
375	                    summary_by_K[K].append(100.0)
376	                except np.linalg.LinAlgError:
377	                    results[config_key][topo] = {'method': 'failed', 'note': 'C not invertible'}
378	                print(f"  {topo:<12} [IV theoretical] bias_reduction=100.0%")
379	                continue
380	
381	            # For non-IV topologies: simulate PPI++ correction
382	            biased_taus = []
383	            ppi_taus = []
384	            naive_plugin_taus = []
385	
386	            for mc_i in range(N_MC):
387	                seed = (hash(config_key + topo + "ppi") & 0xFFFFFFFF) + mc_i * 3571
388	                rng = np.random.default_rng(seed)
389	
390	                try:
391	                    first_var, Y, A = plan_006.GEN_FNS[topo](K, N_SAMPLES,
392	                                                              params[topo], rng)
393	                    A_star = plan_006.generate_Astar(A, C, rng)
394	
395	                    # Build design matrix
396	                    N = len(Y)
397	                    if topo == 'exposure':
398	                        X_other = np.ones((N, 1))
399	                        tau_idx = 1
400	                    else:
401	                        T = first_var
402	                        X_other = np.column_stack([np.ones(N), T])
403	                        tau_idx = 1  # treatment coefficient
404	
405	                    # Gold labels: select GOLD_FRACTION of data
406	                    n_gold = max(int(N * GOLD_FRACTION), 50)
407	                    gold_idx = rng.choice(N, size=n_gold, replace=False)
408	                    gold_mask = np.zeros(N, dtype=bool)
409	                    gold_mask[gold_idx] = True
410	
411	                    # Biased estimate (using A*)
412	                    D_star = np.zeros((N, K - 1))
413	                    for k_idx in range(1, K):
414	                        D_star[:, k_idx - 1] = (A_star == k_idx).astype(float)
415	                    X_biased = np.column_stack([X_other, D_star])
416	                    try:
417	                        beta_biased = np.linalg.lstsq(X_biased, Y, rcond=None)[0]
418	                        biased_taus.append(float(beta_biased[tau_idx]))
419	                    except Exception:
420	                        continue
421	
422	                    # PPI++ correction
423	                    tau_ppi, se_ppi, success = correct_ppi(
424	                        X_other, Y, A_star, A, gold_mask,
425	                        tau_idx=tau_idx, rng=rng
426	                    )
427	                    if success and np.isfinite(tau_ppi):
428	                        ppi_taus.append(float(tau_ppi))
429	
430	                    # Naive plugin (C^{-1}) correction for comparison
431	                    tau_np, se_np, success_np = correct_naive_plugin(
432	                        X_other, Y, A_star, C, tau_idx=tau_idx
433	                    )
434	                    if success_np and np.isfinite(tau_np):
435	                        naive_plugin_taus.append(float(tau_np))
436	
437	                except Exception:
438	                    continue
439	
440	            if len(biased_taus) < N_MC // 4 or len(ppi_taus) < N_MC // 4:
441	                print(f"  {topo:<12} FAILED (biased={len(biased_taus)}, "
442	                      f"ppi={len(ppi_taus)})")
443	                results[config_key][topo] = {
444	                    'method': 'mc_failed',
445	                    'n_biased': len(biased_taus),
446	                    'n_ppi': len(ppi_taus),
447	                }
448	                continue
449	
450	            mean_biased = float(np.mean(biased_taus))
451	            mean_ppi = float(np.mean(ppi_taus))
452	            bias_biased = mean_biased - tau_true
453	            bias_ppi = mean_ppi - tau_true
454	
455	            if abs(bias_biased) > 1e-12:
456	                reduction_pct = 100.0 * (1.0 - abs(bias_ppi) / abs(bias_biased))
457	            else:
458	                reduction_pct = 0.0
459	
460	            # Naive plugin results
461	            mean_naive = float(np.mean(naive_plugin_taus)) if naive_plugin_taus else float('nan')
462	            bias_naive = mean_naive - tau_true if np.isfinite(mean_naive) else float('nan')
463	            if abs(bias_biased) > 1e-12 and np.isfinite(bias_naive):
464	                naive_reduction = 100.0 * (1.0 - abs(bias_naive) / abs(bias_biased))
465	            else:
466	                naive_reduction = float('nan')
467	
468	            entry = {
469	                'method': 'ppi_mc',
470	                'tau_true': float(tau_true),
471	                'tau_biased_mean': mean_biased,
472	                'tau_ppi_mean': mean_ppi,
473	                'tau_naive_mean': mean_naive,
474	                'bias_biased': float(bias_biased),
475	                'bias_ppi': float(bias_ppi),
476	                'bias_naive': float(bias_naive),
477	                'bias_reduction_pct': float(reduction_pct),
478	                'naive_reduction_pct': float(naive_reduction) if np.isfinite(naive_reduction) else None,
479	                'n_mc_biased': len(biased_taus),
480	                'n_mc_ppi': len(ppi_taus),
481	                'n_mc_naive': len(naive_plugin_taus),
482	                'gold_fraction': GOLD_FRACTION,
483	            }
484	            results[config_key][topo] = entry
485	            summary_by_topo[topo].append(reduction_pct)
486	            summary_by_K[K].append(reduction_pct)
487	            print(f"  {topo:<12} bias_biased={bias_biased:+.5f} bias_ppi={bias_ppi:+.5f} "
488	                  f"reduction={reduction_pct:.1f}%")
489	
490	    # Aggregate summaries
491	    topo_summary = {}
492	    for topo in TOPOLOGIES:
493	        vals = summary_by_topo.get(topo, [])
494	        if vals:
495	            topo_summary[topo] = {
496	                'mean_reduction_pct': float(np.mean(vals)),
497	                'median_reduction_pct': float(np.median(vals)),
498	                'min_reduction_pct': float(np.min(vals)),
499	                'max_reduction_pct': float(np.max(vals)),
500	                'n': len(vals),
501	            }
502	
503	    k_summary = {}
504	    for K in sorted(summary_by_K.keys()):
505	        vals = summary_by_K[K]
506	        if vals:
507	            k_summary[str(K)] = {
508	                'mean_reduction_pct': float(np.mean(vals)),
509	                'median_reduction_pct': float(np.median(vals)),
510	                'n': len(vals),
511	            }
512	
513	    all_reductions = []
514	    for topo_vals in summary_by_topo.values():
515	        all_reductions.extend(topo_vals)
516	    grand_mean_reduction = float(np.mean(all_reductions)) if all_reductions else None
517	
518	    output = {
519	        'meta': {
520	            'n_mc': N_MC,
521	            'n_samples': N_SAMPLES,
522	            'gold_fraction': GOLD_FRACTION,
523	            'n_configs': len(all_cms),
524	            'n_topologies': len(TOPOLOGIES),
525	            'correction_methods': ['ppi++', 'naive_plugin (C^{-1})', 'theoretical_Cinv (IV only)'],
526	            'note': (
527	                'PPI++ uses 10% gold labels. For IV topology, theoretical C^{-1} correction '
528	                'is used (100% by construction). Naive plugin shown for comparison. '
529	                'VAST/CC use approximate confusion matrices (diagonal + uniform off-diagonal).'
530	            ),
531	        },
532	        'grand_mean_bias_reduction_pct': grand_mean_reduction,
533	        'per_topology': topo_summary,
534	        'per_K': k_summary,
535	        'per_config': results,
536	    }
537	
538	    out_path = PROJ / "artifacts/ppi_empirical_validation.json"
539	    out_path.write_text(json.dumps(output, indent=2))
540	    print(f"\n=== Task 2 DONE in {time.time()-t0:.1f}s ===")
541	    print(f"Grand mean bias reduction: {grand_mean_reduction:.1f}%"
542	          if grand_mean_reduction else "N/A")
543	    print(f"Written: {out_path}")
544	
545	    # LaTeX snippet
546	    latex = r"""% PPI++ Bias Reduction (auto-generated)
547	\begin{table}[h]\centering\small
548	\caption{PPI++ bias reduction by topology (""" + f"{GOLD_FRACTION:.0%} gold labels" + r""")}
549	\begin{tabular}{lrrrr}
550	\toprule
551	Topology & Mean (\%) & Median (\%) & Min (\%) & $n$ \\
552	\midrule
553	"""
554	    for topo in TOPOLOGIES:
555	        s = topo_summary.get(topo)
556	        if s:
557	            latex += (f"{topo} & {s['mean_reduction_pct']:.1f} & "
558	                      f"{s['median_reduction_pct']:.1f} & "
559	                      f"{s['min_reduction_pct']:.1f} & {s['n']} \\\\\n")
560	    latex += r"""\midrule
561	Grand & """ + f"{grand_mean_reduction:.1f}" + r""" & -- & -- & """ + f"{len(all_reductions)}" + r""" \\
562	\bottomrule
563	\end{tabular}
564	\end{table}
565	"""
566	    latex_path = PROJ / "artifacts/ppi_empirical_validation_table.tex"
567	    latex_path.write_text(latex)
568	    print(f"LaTeX: {latex_path}")
569	
570	    return output
571	
572	
573	# ============================================================================
574	# Task 3: Dirichlet Subspace Overlay Visualization
575	# ============================================================================
576	
577	def task3_dirichlet_overlay(all_cms, config_meta):
578	    """Create fig7 with improved styling and all 18 configs."""
579	    print("\n" + "=" * 80)
580	    print("TASK 3: Dirichlet Subspace Overlay Visualization")
581	    print("=" * 80)
582	
583	    try:
584	        import matplotlib
585	        matplotlib.use("Agg")
586	        import matplotlib.pyplot as plt
587	        import matplotlib.patheffects as pe
588	    except ImportError:
589	        print("ERROR: matplotlib not available")
590	        return
591	
592	    try:
593	        from scipy.interpolate import PchipInterpolator
594	    except ImportError:
595	        print("WARNING: scipy not available, using linear interpolation")
596	        PchipInterpolator = None
597	
598	    # Load theoretical data
599	    EXPOSURE_THEORY = {
600	        "diag_thresh":    [0.0, 0.5, 0.7, 0.9],
601	        "violation_rate": [0.850, 0.325, 0.137, 0.119],
602	        "sign_flip_rate": [0.834, 0.216, 0.021, 0.000],
603	    }
604	
605	    with open(PROJ / "artifacts/iv_dirichlet_subspace_results.json") as f:
606	        iv_raw = json.load(f)
607	    IV_THEORY = {
608	        "diag_thresh":    [],
609	        "violation_rate": [],
610	        "sign_flip_rate": [],
611	    }
612	    for t in ("0.0", "0.5", "0.7", "0.9"):
613	        IV_THEORY["diag_thresh"].append(float(t))
614	        IV_THEORY["violation_rate"].append(iv_raw["thresholds"][t]["violation_rate"])
615	        IV_THEORY["sign_flip_rate"].append(iv_raw["thresholds"][t]["sign_flip_rate"])
616	
617	    # Style
618	    plt.rcParams.update({
619	        "font.family": "serif",
620	        "font.serif": ["Times New Roman", "DejaVu Serif", "Times"],
621	        "font.size": 9,
622	        "axes.titlesize": 10,
623	        "axes.labelsize": 9,
624	        "xtick.labelsize": 8,
625	        "ytick.labelsize": 8,
626	        "legend.fontsize": 7,
627	        "figure.dpi": 300,
628	        "savefig.dpi": 300,
629	        "savefig.bbox": "tight",
630	        "savefig.pad_inches": 0.05,
631	        "axes.spines.top": False,
632	        "axes.spines.right": False,
633	        "lines.linewidth": 1.4,
634	        "mathtext.fontset": "stix",
635	    })
636	
637	    # Marker / color encoding
638	    DATASET_MARKERS = {
639	        "humaid":         {"marker": "o", "size": 40},
640	        "vast":           {"marker": "s", "size": 40},
641	        "civil_comments": {"marker": "^", "size": 50},
642	    }
643	    MODEL_COLORS = {
644	        "llama4":     "#E31A1C",   # red
645	        "qwen3":      "#1F78B4",   # blue
646	        "deepseek":   "#33A02C",   # green
647	        "qwen2.5-7b": "#FF7F00",   # orange
648	    }
649	
650	    # Build config list
651	    configs = []
652	    for key, C in all_cms.items():
653	        meta = config_meta[key]
654	        model = meta["model_prompt"].split("_")[0]
655	        # Handle "qwen2.5-7b" model name
656	        if "qwen2.5" in meta["model_prompt"]:
657	            model = "qwen2.5-7b"
658	            prompt = meta["model_prompt"].replace("qwen2.5-7b_", "")
659	        else:
660	            prompt = meta["model_prompt"][len(model)+1:]
661	        configs.append({
662	            "key": key,
663	            "dataset": meta["dataset"],
664	            "model": model,
665	            "prompt": prompt,
666	            "K": meta["K"],
667	            "min_diag": meta["min_diag"],
668	        })
669	
670	    def smooth_curve(xs, ys, n=200):
671	        xs = np.asarray(xs, dtype=float)
672	        ys = np.asarray(ys, dtype=float)
673	        xx = np.linspace(0.0, 1.0, n)
674	        if PchipInterpolator is not None:
675	            interp = PchipInterpolator(xs, ys, extrapolate=False)
676	            yy = interp(xx)
677	            yy[xx < xs[0]] = ys[0]
678	            yy[xx > xs[-1]] = ys[-1]
679	        else:
680	            yy = np.interp(xx, xs, ys)
681	        return xx, yy
682	
683	    def interp_at(x, xs, ys):
684	        xs = np.asarray(xs, dtype=float)
685	        ys = np.asarray(ys, dtype=float)
686	        if x <= xs[0]:
687	            return float(ys[0])
688	        if x >= xs[-1]:
689	            return float(ys[-1])
690	        if PchipInterpolator is not None:
691	            return float(PchipInterpolator(xs, ys, extrapolate=False)(x))
692	        return float(np.interp(x, xs, ys))
693	
694	    def draw_panel(ax, theory, panel_title, panel_letter, show_violation_fill=True):
695	        xs_t = theory["diag_thresh"]
696	        vr_t = theory["violation_rate"]
697	        sf_t = theory["sign_flip_rate"]
698	
699	        xx, vr_curve = smooth_curve(xs_t, vr_t)
700	        _, sf_curve = smooth_curve(xs_t, sf_t)
701	
702	        # Shading zones
703	        ax.axvspan(0.0, 0.5, color="#FDAE61", alpha=0.12, zorder=0,
704	                   label="_nolegend_")  # danger
705	        ax.axvspan(0.5, 0.7, color="#FEE08B", alpha=0.10, zorder=0,
706	                   label="_nolegend_")  # caution
707	        ax.axvspan(0.9, 1.0, color="#A6D96A", alpha=0.12, zorder=0,
708	                   label="_nolegend_")  # safe
709	
710	        # Theory curves
711	        if show_violation_fill:
712	            ax.fill_between(xx, 0, vr_curve,
713	                            color="#888888", alpha=0.15, zorder=1,
714	                            label="Violation rate (theory)")
715	            ax.plot(xx, vr_curve, color="#555555", linewidth=1.2, zorder=2)
716	        else:
717	            ax.axhline(1.0, color="#888888", linewidth=1.0, alpha=0.5,
718	                       linestyle=":", zorder=1,
719	                       label="Violation rate (theory) $=1$")
720	
721	        ax.plot(xx, sf_curve, color="#B22222", linewidth=1.4,
722	                linestyle="--", zorder=3,
723	                label="Sign-flip rate (theory)")
724	
725	        # Theory anchor points
726	        ax.scatter(xs_t, vr_t, s=15, color="#555555",
727	                   marker="x", linewidth=0.8, zorder=4, label="_nolegend_")
728	        ax.scatter(xs_t, sf_t, s=15, color="#B22222",
729	                   marker="x", linewidth=0.8, zorder=4, label="_nolegend_")
730	
731	        # Empirical points
732	        handled = set()
733	        for cfg in configs:
734	            x = cfg["min_diag"]
735	            y = interp_at(x, xs_t, vr_t)
736	            ds = cfg["dataset"]
737	            style = DATASET_MARKERS[ds]
738	            color = MODEL_COLORS.get(cfg["model"], "#999999")
739	
740	            legend_key = (ds, cfg["model"])
741	            if legend_key not in handled:
742	                handled.add(legend_key)
743	                ds_short = {"humaid": "HumAID", "vast": "VAST",
744	                            "civil_comments": "CC"}[ds]
745	                lbl = f"{ds_short}/{cfg['model']} ($K$={cfg['K']})"
746	            else:
747	                lbl = None
748	
749	            ax.scatter(x, y, marker=style["marker"], s=style["size"],
750	                       facecolor=color, edgecolor="white", linewidth=0.6,
751	                       zorder=6, label=lbl)
752	
753	        # Zone labels
754	        for txt_str, pos, col in [
755	            ("sign-flip\nzone", (0.08, 0.55), "#A53A0C"),
756	            ("safe", (0.95, 0.06), "#2B7A3B"),
757	        ]:
758	            t = ax.text(pos[0], pos[1], txt_str, ha="center", va="center",
759	                        fontsize=7, color=col, fontstyle="italic",
760	                        transform=ax.transAxes)
761	            t.set_path_effects([pe.withStroke(linewidth=2.0, foreground="white")])
762	
763	        ax.set_xlim(0.0, 1.0)
764	        ax.set_ylim(-0.03, 1.15)
765	        ax.set_xlabel(r"Min.\ diagonal dominance $\min_k C_{kk}$")
766	        if panel_letter == "a":
767	            ax.set_ylabel("Violation / sign-flip rate")
768	        ax.set_title(f"({panel_letter}) {panel_title}", loc="left", pad=4,
769	                     fontweight="bold")
770	        ax.grid(True, axis="y", alpha=0.2, linewidth=0.4, zorder=0)
771	
772	    # Build figure (single-column width ~ 3.5 inches, but we use 7.0 for two panels)
773	    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.2), sharey=True)
774	
775	    draw_panel(axes[0], EXPOSURE_THEORY, "Exposure", "a",
776	               show_violation_fill=True)
777	    draw_panel(axes[1], IV_THEORY, "IV", "b",
778	               show_violation_fill=False)
779	
780	    # Unified legend
781	    handles, labels = [], []
782	    for ax in axes:
783	        h, l = ax.get_legend_handles_labels()
784	        for hh, ll in zip(h, l):
785	            if ll and ll not in labels:
786	                handles.append(hh)
787	                labels.append(ll)
788	    fig.legend(handles, labels,
789	               loc="lower center", bbox_to_anchor=(0.5, -0.08),
790	               ncol=4, frameon=False, columnspacing=1.0,
791	               handletextpad=0.4, fontsize=7)
792	
793	    plt.tight_layout(rect=(0, 0.04, 1, 1.0))
794	
795	    out_pdf = PROJ / "figures/paper/fig7_dirichlet_overlay.pdf"
796	    out_png = PROJ / "figures/paper/fig7_dirichlet_overlay.png"
797	    out_pdf.parent.mkdir(parents=True, exist_ok=True)
798	    plt.savefig(out_pdf)
799	    plt.savefig(out_png)
800	    plt.close()
801	
802	    print(f"Saved: {out_pdf}")
803	    print(f"Saved: {out_png}")
804	
805	    # Print empirical positions for reference
806	    print(f"\n{'config':<52} {'K':>3} {'min_diag':>9}")
807	    print("-" * 70)
808	    for cfg in sorted(configs, key=lambda c: c["min_diag"]):
809	        key = f"{cfg['dataset']}_{cfg['model']}_{cfg['prompt']}"
810	        print(f"{key:<52} {cfg['K']:>3} {cfg['min_diag']:>9.4f}")
811	
812	    return {"n_configs": len(configs), "output_files": [str(out_pdf), str(out_png)]}
813	
814	
815	# ============================================================================
816	# Main
817	# ============================================================================
818	
819	def main():
820	    t_start = time.time()
821	    print("Loading all data...")
822	    all_cms, config_meta, bias_lookup, filter_data = load_all_data()
823	    print(f"Loaded {len(all_cms)} confusion matrices")
824	    for k, m in sorted(config_meta.items()):
825	        print(f"  {k:<52} K={m['K']:>2}  min_diag={m['min_diag']:.4f}  "
826	              f"trace={m['trace']:.4f}")
827	
828	    # Task 1
829	    mape_result = task1_mape(all_cms, config_meta, bias_lookup)
830	
831	    # Task 2
832	    ppi_result = task2_ppi(all_cms, config_meta)
833	
834	    # Task 3
835	    fig_result = task3_dirichlet_overlay(all_cms, config_meta)
836	
837	    print(f"\n{'='*80}")
838	    print(f"ALL TASKS COMPLETE in {time.time()-t_start:.1f}s")
839	    print(f"{'='*80}")
840	    print(f"\nTask 1: Grand MAPE = {mape_result['grand_mape']:.4%}")
841	    print(f"Task 2: Grand PPI++ reduction = {ppi_result['grand_mean_bias_reduction_pct']:.1f}%")
842	    if fig_result:
843	        print(f"Task 3: Figure saved with {fig_result['n_configs']} configs")
844	    else:
845	        print("Task 3: SKIPPED (matplotlib not available)")
846	
847	
848	if __name__ == "__main__":
849	    main()
850	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ac7a21a-88bf-4c6b-8a13-c6fe72cd8269",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "e8db9377-1a38-4b6c-87d7-74762eb6c45b",
  "sourceToolAssistantUUID": "1ac7a21a-88bf-4c6b-8a13-c6fe72cd8269",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-23T14:57:02.255Z_

Now let me search more specifically for the exposure bias and sign reversal computation code:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8db9377-1a38-4b6c-87d7-74762eb6c45b",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhKWguPQCQJ4JPi28Wd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c013783d-09b1-4622-b227-eaf4df07ad42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FjLAtNjcyCHho6jhazVTQh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 27839,
      "cache_read_input_tokens": 20997,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27839,
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

_source line 17 · 2026-05-23T14:57:04.497Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01AeiFR8TkYowgtRmvVEJhsE`</summary>

```json
{
  "pattern": "sign.?reversal|sign.?flip|exposure.?topology",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts",
  "type": "py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c013783d-09b1-4622-b227-eaf4df07ad42",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhKWguPQCQJ4JPi28Wd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "58c8c586-b74a-4f68-a6ce-1250795712ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FjLAtNjcyCHho6jhazVTQh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 27839,
      "cache_read_input_tokens": 20997,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27839
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 262,
          "cache_read_input_tokens": 20997,
          "cache_creation_input_tokens": 27839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27839,
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

_source line 18 · 2026-05-23T14:57:04.504Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P4wD2GXypQYZNi9czB5h4V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/sign_reversal_determinants.py",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58c8c586-b74a-4f68-a6ce-1250795712ce",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhKWguPQCQJ4JPi28Wd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "008b0197-e22d-4bf6-8df6-a6fcaf85ee86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FjLAtNjcyCHho6jhazVTQh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 27839,
      "cache_read_input_tokens": 20997,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27839
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 262,
          "cache_read_input_tokens": 20997,
          "cache_creation_input_tokens": 27839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27839,
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

_source line 19 · 2026-05-23T14:57:04.522Z_

<details><summary>↩ Tool result · `toolu_01AeiFR8TkYowgtRmvVEJhsE`</summary>

```text
Found 30 files
artifacts/sign_reversal_determinants.py
artifacts/structured_nondiff_violation.py
artifacts/e2e_demo.py
artifacts/ranking_stability.py
artifacts/nondiff_structured_stress_test.py
artifacts/exp_realistic_epsilon.py
artifacts/exp_proportional_effects.py
artifacts/exp_primary_coeff_breakdown.py
artifacts/nondiff_stress_test.py
artifacts/analyze_epsilon_sign_structure.py
artifacts/exp_b_logistic_dgp.py
artifacts/analyze_epsilon_bound.py
artifacts/exp_d_conjecture_verify_v2.py
artifacts/exp_e_asv_stability.py
artifacts/exp_a_stress_test.py
artifacts/compute_updated_empirical.py
artifacts/compute_delta_max.py
artifacts/plan011_frontier_annotations/scripts/compute_results.py
artifacts/_project/intermediate/case_study_analysis.py
artifacts/plan012_case_study/case_study_analysis.py
artifacts/compute_all_tasks.py
artifacts/mvp_iv_dirichlet_subspace.py
artifacts/plan_009_pathological_matrices.py
artifacts/plan_002_k57_extended_7topo.py
artifacts/plan_005_asv_extended_fixed.py
artifacts/plan008_binarization_collapse/report/plan_008_binarization_collapse.py
artifacts/_project/report/mvp_exposure_dirichlet_subspace.py
artifacts/mvp_exposure_dirichlet_subspace.py
artifacts/_project/data/mvp_exposure_dag.py
artifacts/mvp_exposure_dag.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58c8c586-b74a-4f68-a6ce-1250795712ce",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "5144b05b-8b77-48cb-a7ac-2fd8d54d7deb",
  "sourceToolAssistantUUID": "58c8c586-b74a-4f68-a6ce-1250795712ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T14:57:04.521Z_

<details><summary>↩ Tool result · `toolu_01P4wD2GXypQYZNi9czB5h4V`</summary>

```text
1	#!/usr/bin/env python3
2	"""Sign-reversal determinants on the 23 empirical LLM confusion matrices.
3	
4	For each CM:
5	  * extract simple matrix features
6	  * compute exposure-topology sign-reversal under default beta and several alt betas
7	  * search for a simple decision rule that separates flip / no-flip groups
8	"""
9	
10	import json
11	import sys
12	import itertools
13	import numpy as np
14	from pathlib import Path
15	from collections import defaultdict
16	
17	PROJ = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib")
18	sys.path.insert(0, str(PROJ))
19	
20	import importlib.util
21	spec = importlib.util.spec_from_file_location(
22	    "plan_006", str(PROJ / "plan_006_asv_empirical.py"))
23	plan_006 = importlib.util.module_from_spec(spec)
24	spec.loader.exec_module(plan_006)
25	
26	EMPIRICAL_FILE = PROJ / "artifacts/updated_empirical_results.json"
27	OUT_FILE = PROJ / "artifacts/sign_reversal_determinants_results.json"
28	
29	
30	# ----------------------------------------------------------------------
31	# Matrix features
32	# ----------------------------------------------------------------------
33	
34	def matrix_features(C):
35	    """Compute scalar features of a column-stochastic K x K confusion matrix."""
36	    K = C.shape[0]
37	    diag = np.diag(C)
38	    off = C - np.diag(diag)
39	
40	    min_diag = float(np.min(diag))
41	    mean_diag = float(np.mean(diag))
42	
43	    # max off-diagonal element across the matrix
44	    max_off = float(off.max())
45	    # max ratio of off-diagonal element to the diagonal of its column
46	    safe_diag = np.where(diag > 1e-12, diag, np.nan)
47	    # off[i,j] / diag[j]
48	    ratio = off / safe_diag[None, :]
49	    max_off_ratio = float(np.nanmax(ratio))
50	
51	    # condition number
52	    try:
53	        cond = float(np.linalg.cond(C))
54	    except np.linalg.LinAlgError:
55	        cond = float("inf")
56	    if not np.isfinite(cond):
57	        cond = 1e12
58	
59	    # per-column entropy (normalized to [0,1])
60	    H = []
61	    log_K = np.log(K) if K > 1 else 1.0
62	    for j in range(K):
63	        col = C[:, j]
64	        col = col / col.sum() if col.sum() > 0 else col
65	        col = np.clip(col, 1e-12, 1.0)
66	        H.append(-(col * np.log(col)).sum() / log_K)
67	    mean_entropy = float(np.mean(H))
68	    max_entropy = float(np.max(H))
69	
70	    # spectral gap of |eigenvalues|
71	    eigvals = np.linalg.eigvals(C)
72	    abs_eig = np.sort(np.abs(eigvals))[::-1]
73	    if len(abs_eig) >= 2:
74	        spectral_gap = float(abs_eig[0] - abs_eig[1])
75	    else:
76	        spectral_gap = float(abs_eig[0])
77	
78	    # determinant (sign and magnitude indicator)
79	    det = float(np.linalg.det(C))
80	
81	    # minimum singular value (closer to 0 => closer to singular)
82	    sv = np.linalg.svd(C, compute_uv=False)
83	    min_sv = float(sv.min())
84	    sv_ratio = float(sv.max() / sv.min()) if sv.min() > 0 else float("inf")
85	    if not np.isfinite(sv_ratio):
86	        sv_ratio = 1e12
87	
88	    return {
89	        "K": K,
90	        "min_diag": min_diag,
91	        "mean_diag": mean_diag,
92	        "max_off": max_off,
93	        "max_off_ratio": max_off_ratio,
94	        "cond": cond,
95	        "log_cond": float(np.log10(max(cond, 1.0))),
96	        "mean_entropy": mean_entropy,
97	        "max_entropy": max_entropy,
98	        "spectral_gap": spectral_gap,
99	        "det": det,
100	        "min_sv": min_sv,
101	        "sv_ratio": sv_ratio,
102	    }
103	
104	
105	# ----------------------------------------------------------------------
106	# Exposure sign-reversal evaluation
107	# ----------------------------------------------------------------------
108	
109	def exposure_outcome(C, beta, p_A=None, seed=42):
110	    """Run the exposure DGP with custom beta and return sign-flip details."""
111	    K = C.shape[0]
112	    if p_A is None:
113	        p_A = plan_006.make_p_A(K)
114	    params = {"beta": np.asarray(beta, dtype=float), "p_A": p_A}
115	    st = plan_006.precompute_suff_stats(K, "exposure", params, seed=seed)
116	    plim_true = plan_006.compute_plim(np.eye(K), st, K)
117	    plim_biased = plan_006.compute_plim(C, st, K)
118	
119	    if not isinstance(plim_biased, np.ndarray):
120	        return {
121	            "any_flip": None,
122	            "per_coef": None,
123	            "max_relbias": float("inf"),
124	            "tau_true": None,
125	            "tau_hat": None,
126	        }
127	
128	    per = []
129	    any_flip = False
130	    max_relbias = 0.0
131	    for i in range(1, K):
132	        tv = float(plim_true[i])
133	        bv = float(plim_biased[i])
134	        sf = bool(np.sign(bv) != np.sign(tv)) if abs(tv) > 1e-10 else False
135	        rel = abs(bv - tv) / max(abs(tv), 1e-10)
136	        max_relbias = max(max_relbias, rel)
137	        if sf:
138	            any_flip = True
139	        per.append({"coef_idx": i, "true": tv, "biased": bv, "sign_flip": sf})
140	
141	    return {
142	        "any_flip": any_flip,
143	        "per_coef": per,
144	        "max_relbias": float(max_relbias),
145	        "tau_true": float(plim_true[1]),
146	        "tau_hat": float(plim_biased[1]),
147	    }
148	
149	
150	# ----------------------------------------------------------------------
151	# Beta configurations
152	# ----------------------------------------------------------------------
153	
154	DEFAULT_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
155	
156	
157	def beta_default(K):
158	    return DEFAULT_POOL[:K]
159	
160	
161	def beta_uniform_pos(K):
162	    return [0.0] + [1.0] * (K - 1)
163	
164	
165	def beta_alt_signs(K):
166	    """Alternating signs of magnitude 1.0 starting positive at index 1."""
167	    v = [0.0]
168	    for j in range(K - 1):
169	        v.append(1.0 if j % 2 == 0 else -1.0)
170	    return v
171	
172	
173	def beta_only_first(K):
174	    """Only coefficient at index 1 is nonzero."""
175	    v = [0.0] * K
176	    if K >= 2:
177	        v[1] = 1.0
178	    return v
179	
180	
181	def beta_small(K):
182	    """Default vector scaled by 0.3 (smaller effect sizes — sign flips easier)."""
183	    return [0.3 * x for x in DEFAULT_POOL[:K]]
184	
185	
186	def beta_large(K):
187	    """Default vector scaled by 3.0 (larger effect sizes — flips harder)."""
188	    return [3.0 * x for x in DEFAULT_POOL[:K]]
189	
190	
191	BETA_CONFIGS = {
192	    "default": beta_default,
193	    "uniform_pos": beta_uniform_pos,
194	    "alt_signs": beta_alt_signs,
195	    "only_first": beta_only_first,
196	    "scale_0p3": beta_small,
197	    "scale_3p0": beta_large,
198	}
199	
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "008b0197-e22d-4bf6-8df6-a6fcaf85ee86",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "87f994c8-59c6-4ae6-ae51-f41b29264745",
  "sourceToolAssistantUUID": "008b0197-e22d-4bf6-8df6-a6fcaf85ee86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-23T14:57:05.944Z_

Let me continue reading the sign_reversal_determinants.py file and search for more detail on the computation:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87f994c8-59c6-4ae6-ae51-f41b29264745",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhKpR1df2a6f7DFgPSs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3a3f342f-8848-4946-be94-8a31b1d41b45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BZc3vccPkxEbWduWSt2t5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3383,
      "cache_read_input_tokens": 48836,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3383,
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

_source line 22 · 2026-05-23T14:57:06.785Z_

<details open><summary>🔧 Tool call — Read · `toolu_01McnPX9Ws86icLXGhQC2ddJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/sign_reversal_determinants.py",
  "limit": 500,
  "offset": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a3f342f-8848-4946-be94-8a31b1d41b45",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhKpR1df2a6f7DFgPSs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cca89d53-5b98-40f2-aa1b-c68565cb140a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BZc3vccPkxEbWduWSt2t5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3383,
      "cache_read_input_tokens": 48836,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3383,
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

_source line 23 · 2026-05-23T14:57:06.791Z_

<details><summary>↩ Tool result · `toolu_01McnPX9Ws86icLXGhQC2ddJ`</summary>

```text
200	
201	# ----------------------------------------------------------------------
202	# Simple rule search
203	# ----------------------------------------------------------------------
204	
205	def evaluate_rule(rows, feat_a, op_a, thr_a, feat_b=None, op_b=None, thr_b=None,
206	                  combine="AND"):
207	    def predict(row):
208	        fa = row["features"][feat_a]
209	        ok_a = (fa < thr_a) if op_a == "<" else (fa > thr_a)
210	        if feat_b is None:
211	            return ok_a
212	        fb = row["features"][feat_b]
213	        ok_b = (fb < thr_b) if op_b == "<" else (fb > thr_b)
214	        return (ok_a and ok_b) if combine == "AND" else (ok_a or ok_b)
215	
216	    tp = fp = tn = fn = 0
217	    for r in rows:
218	        truth = r["sign_flip"]
219	        pred = predict(r)
220	        if pred and truth:
221	            tp += 1
222	        elif pred and not truth:
223	            fp += 1
224	        elif (not pred) and truth:
225	            fn += 1
226	        else:
227	            tn += 1
228	    n = tp + fp + tn + fn
229	    acc = (tp + tn) / n if n else 0.0
230	    sens = tp / (tp + fn) if (tp + fn) else 0.0
231	    spec = tn / (tn + fp) if (tn + fp) else 0.0
232	    return {
233	        "tp": tp, "fp": fp, "tn": tn, "fn": fn,
234	        "accuracy": acc, "sensitivity": sens, "specificity": spec,
235	    }
236	
237	
238	def search_simple_rules(rows, features):
239	    """Brute-force search over single-feature thresholds and 2-feature AND."""
240	    # quantile thresholds per feature
241	    candidates = {}
242	    for f in features:
243	        vals = sorted({row["features"][f] for row in rows})
244	        # midpoints between sorted unique values
245	        thrs = []
246	        for i in range(len(vals) - 1):
247	            thrs.append(0.5 * (vals[i] + vals[i + 1]))
248	        candidates[f] = thrs
249	
250	    # single-feature rules
251	    best_single = None
252	    for f in features:
253	        for thr in candidates[f]:
254	            for op in ("<", ">"):
255	                m = evaluate_rule(rows, f, op, thr)
256	                key = (m["accuracy"], m["sensitivity"] + m["specificity"])
257	                if best_single is None or key > best_single["key"]:
258	                    best_single = {
259	                        "rule": f"{f} {op} {thr:.4f} -> sign_flip",
260	                        "feature": f, "op": op, "thr": thr,
261	                        "metrics": m, "key": key,
262	                    }
263	
264	    # AND-of-2 rules
265	    best_and = None
266	    for fa, fb in itertools.combinations(features, 2):
267	        for ta in candidates[fa]:
268	            for oa in ("<", ">"):
269	                for tb in candidates[fb]:
270	                    for ob in ("<", ">"):
271	                        m = evaluate_rule(rows, fa, oa, ta, fb, ob, tb, "AND")
272	                        key = (m["accuracy"], m["sensitivity"] + m["specificity"])
273	                        if best_and is None or key > best_and["key"]:
274	                            best_and = {
275	                                "rule": (f"({fa} {oa} {ta:.4f}) AND "
276	                                         f"({fb} {ob} {tb:.4f}) -> sign_flip"),
277	                                "feat_a": fa, "op_a": oa, "thr_a": ta,
278	                                "feat_b": fb, "op_b": ob, "thr_b": tb,
279	                                "metrics": m, "key": key,
280	                            }
281	    for d in (best_single, best_and):
282	        if d is not None:
283	            d.pop("key", None)
284	    return best_single, best_and
285	
286	
287	# ----------------------------------------------------------------------
288	# Descriptive comparisons
289	# ----------------------------------------------------------------------
290	
291	def group_compare(rows, features):
292	    flip = [r for r in rows if r["sign_flip"]]
293	    no_flip = [r for r in rows if not r["sign_flip"]]
294	    out = {}
295	    for f in features:
296	        vf = np.array([r["features"][f] for r in flip], dtype=float)
297	        vn = np.array([r["features"][f] for r in no_flip], dtype=float)
298	        out[f] = {
299	            "n_flip": int(vf.size),
300	            "n_no_flip": int(vn.size),
301	            "mean_flip": float(np.nanmean(vf)) if vf.size else None,
302	            "mean_no_flip": float(np.nanmean(vn)) if vn.size else None,
303	            "median_flip": float(np.nanmedian(vf)) if vf.size else None,
304	            "median_no_flip": float(np.nanmedian(vn)) if vn.size else None,
305	            "min_flip": float(np.nanmin(vf)) if vf.size else None,
306	            "min_no_flip": float(np.nanmin(vn)) if vn.size else None,
307	            "max_flip": float(np.nanmax(vf)) if vf.size else None,
308	            "max_no_flip": float(np.nanmax(vn)) if vn.size else None,
309	        }
310	    return out
311	
312	
313	# ----------------------------------------------------------------------
314	# Main
315	# ----------------------------------------------------------------------
316	
317	def main():
318	    with open(EMPIRICAL_FILE) as f:
319	        emp = json.load(f)
320	    cms = {k: np.array(v) for k, v in emp["confusion_matrices"].items()}
321	    print(f"Loaded {len(cms)} confusion matrices")
322	
323	    # 1. features for each matrix
324	    feat_table = {}
325	    for name, C in cms.items():
326	        feat_table[name] = matrix_features(C)
327	
328	    # 2. exposure outcomes per beta config
329	    per_beta_results = {}
330	    for beta_name, beta_fn in BETA_CONFIGS.items():
331	        rows = []
332	        for name, C in cms.items():
333	            K = C.shape[0]
334	            beta = beta_fn(K)
335	            res = exposure_outcome(C, beta)
336	            row = {
337	                "config": name,
338	                "K": K,
339	                "beta": beta,
340	                "sign_flip": bool(res["any_flip"]) if res["any_flip"] is not None else False,
341	                "tau_true": res["tau_true"],
342	                "tau_hat": res["tau_hat"],
343	                "max_relbias": res["max_relbias"],
344	                "per_coef": res["per_coef"],
345	                "features": feat_table[name],
346	            }
347	            rows.append(row)
348	        n_flip = sum(1 for r in rows if r["sign_flip"])
349	        per_beta_results[beta_name] = {
350	            "beta_label": beta_name,
351	            "n_total": len(rows),
352	            "n_flip": n_flip,
353	            "rows": rows,
354	        }
355	        print(f"  beta={beta_name}: {n_flip}/{len(rows)} sign_flips")
356	
357	    # 3. descriptive analysis under default beta
358	    feature_names = [
359	        "min_diag", "mean_diag", "max_off", "max_off_ratio",
360	        "log_cond", "mean_entropy", "max_entropy",
361	        "spectral_gap", "det", "min_sv",
362	    ]
363	    default_rows = per_beta_results["default"]["rows"]
364	    group_stats = group_compare(default_rows, feature_names)
365	
366	    # 4. simple-rule search (default beta)
367	    best_single, best_and = search_simple_rules(default_rows, feature_names)
368	
369	    # 5. robustness: best single-feature rule under default re-evaluated on
370	    #    every other beta configuration
371	    robustness = {}
372	    if best_single is not None:
373	        for beta_name, payload in per_beta_results.items():
374	            m = evaluate_rule(
375	                payload["rows"],
376	                best_single["feature"], best_single["op"], best_single["thr"])
377	            robustness[beta_name] = m
378	
379	    # 6. K-stratified
380	    by_K = defaultdict(list)
381	    for r in default_rows:
382	        by_K[r["K"]].append(r)
383	    k_stratified = {}
384	    for K, rs in by_K.items():
385	        n_flip = sum(1 for r in rs if r["sign_flip"])
386	        k_stratified[str(K)] = {
387	            "n": len(rs),
388	            "n_flip": n_flip,
389	            "configs": [r["config"] for r in rs],
390	            "flips": [r["config"] for r in rs if r["sign_flip"]],
391	        }
392	
393	    # ------------------------------------------------------------------
394	    # write JSON
395	    # ------------------------------------------------------------------
396	    out = {
397	        "n_matrices": len(cms),
398	        "beta_configs_tested": list(BETA_CONFIGS.keys()),
399	        "feature_names": feature_names,
400	        "features_per_config": feat_table,
401	        "per_beta_results": per_beta_results,
402	        "default_beta_descriptive": {
403	            "group_compare": group_stats,
404	            "best_single_rule": best_single,
405	            "best_AND_rule": best_and,
406	            "k_stratified": k_stratified,
407	        },
408	        "rule_robustness_across_betas": robustness,
409	    }
410	    with open(OUT_FILE, "w") as f:
411	        json.dump(out, f, indent=2, default=float)
412	    print(f"\nWrote {OUT_FILE}")
413	    print(f"Best single rule (default beta): {best_single['rule'] if best_single else None}")
414	    if best_single:
415	        print(f"  metrics: {best_single['metrics']}")
416	    print(f"Best AND rule (default beta): {best_and['rule'] if best_and else None}")
417	    if best_and:
418	        print(f"  metrics: {best_and['metrics']}")
419	    print("Rule robustness across betas:")
420	    for k, v in robustness.items():
421	        print(f"  {k}: acc={v['accuracy']:.3f} sens={v['sensitivity']:.3f} spec={v['specificity']:.3f}")
422	
423	
424	if __name__ == "__main__":
425	    main()
426	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cca89d53-5b98-40f2-aa1b-c68565cb140a",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "0d7e4733-fc7e-43fe-9fba-614addba254c",
  "sourceToolAssistantUUID": "cca89d53-5b98-40f2-aa1b-c68565cb140a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-23T14:57:07.441Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01TmcVRLHS1ADeq8vpWrXcNJ`</summary>

```json
{
  "pattern": "compute_plim|extract_tau",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "type": "py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d7e4733-fc7e-43fe-9fba-614addba254c",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhKpR1df2a6f7DFgPSs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6fec90ca-0097-42c3-96e6-bb9b0d80134d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BZc3vccPkxEbWduWSt2t5R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3383,
      "cache_read_input_tokens": 48836,
      "output_tokens": 277,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3383
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 277,
          "cache_read_input_tokens": 48836,
          "cache_creation_input_tokens": 3383,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3383,
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

_source line 25 · 2026-05-23T14:57:07.461Z_

<details><summary>↩ Tool result · `toolu_01TmcVRLHS1ADeq8vpWrXcNJ`</summary>

```text
Found 14 files
artifacts/sign_reversal_determinants.py
artifacts/bootstrap_ci_convergence.py
artifacts/nondiff_structured_stress_test.py
artifacts/exp_proportional_real_matrices.py
artifacts/exp_realistic_epsilon.py
artifacts/exp_proportional_effects.py
artifacts/exp_primary_coeff_breakdown.py
artifacts/compute_unified_mape.py
artifacts/exp_c_bootstrap_asv.py
artifacts/compute_updated_empirical.py
artifacts/plan011_frontier_annotations/scripts/compute_results.py
artifacts/compute_all_tasks.py
artifacts/compute_theory_empirical_mape.py
plan_006_asv_empirical.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fec90ca-0097-42c3-96e6-bb9b0d80134d",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "f7348338-25bd-4955-bbd7-3630ef98b1c6",
  "sourceToolAssistantUUID": "6fec90ca-0097-42c3-96e6-bb9b0d80134d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-23T14:57:09.055Z_

Now let me examine the plan_006_asv_empirical.py file since it contains the core compute_plim and extract_tau functions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7348338-25bd-4955-bbd7-3630ef98b1c6",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhL35WrwcGbxJSxVCXB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d6d43d76-fbf7-4923-9468-9c9ba9dd3433",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UHxJQ2Y3h2q5thZiDLGcYU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3677,
      "cache_read_input_tokens": 52219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3677,
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

_source line 27 · 2026-05-23T14:57:09.814Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WoLPG4gSnktBt6BErrMpMC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6d43d76-fbf7-4923-9468-9c9ba9dd3433",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhL35WrwcGbxJSxVCXB",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b00ccaec-935e-4b6b-a473-8bd178287ef1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UHxJQ2Y3h2q5thZiDLGcYU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3677,
      "cache_read_input_tokens": 52219,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3677
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 142,
          "cache_read_input_tokens": 52219,
          "cache_creation_input_tokens": 3677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3677,
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

_source line 28 · 2026-05-23T14:57:09.833Z_

<details><summary>↩ Tool result · `toolu_01WoLPG4gSnktBt6BErrMpMC`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b00ccaec-935e-4b6b-a473-8bd178287ef1",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "aec8e5e9-715c-4e51-b612-0ef5537130ac",
  "sourceToolAssistantUUID": "b00ccaec-935e-4b6b-a473-8bd178287ef1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-23T14:57:11.318Z_

Let me continue reading to find compute_plim and extract_tau:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aec8e5e9-715c-4e51-b612-0ef5537130ac",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhLD7kyJgYnh5qEnhzM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "837ff638-d66d-4f84-bcf5-9e7b3a140ff8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ELbwCni3N89zRJBih8q6Dw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 5073,
      "cache_read_input_tokens": 55896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5073,
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

_source line 30 · 2026-05-23T14:57:12.286Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W7XwKuNMC4nTUWFpha4Phf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "limit": 600,
  "offset": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "837ff638-d66d-4f84-bcf5-9e7b3a140ff8",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhLD7kyJgYnh5qEnhzM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9d273a5f-dfec-474d-80fe-6231773d1719",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ELbwCni3N89zRJBih8q6Dw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 5073,
      "cache_read_input_tokens": 55896,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5073,
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

_source line 31 · 2026-05-23T14:57:12.293Z_

<details><summary>↩ Tool result · `toolu_01W7XwKuNMC4nTUWFpha4Phf`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d273a5f-dfec-474d-80fe-6231773d1719",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "3ea9b721-9325-405e-a45a-671f6686f7c8",
  "sourceToolAssistantUUID": "9d273a5f-dfec-474d-80fe-6231773d1719",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-23T14:57:14.139Z_

Perfect! Now let me look for JSON files with "confusion" in the name to get specific empirical examples:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ea9b721-9325-405e-a45a-671f6686f7c8",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhLQvud995gb4n1btjY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8291ef8d-8f98-44ac-9c77-e3de12da3a52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012h6iLCjzUtGj3KEgK4ujpC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 9189,
      "cache_read_input_tokens": 60969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9189,
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

_source line 33 · 2026-05-23T14:57:15.371Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GVSEPc5kSYcJgBvmGhFy6q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_new_cms.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8291ef8d-8f98-44ac-9c77-e3de12da3a52",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhLQvud995gb4n1btjY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "77640fff-afb9-4e10-a324-9c638e399161",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012h6iLCjzUtGj3KEgK4ujpC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 9189,
      "cache_read_input_tokens": 60969,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9189,
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

_source line 34 · 2026-05-23T14:57:15.376Z_

<details><summary>↩ Tool result · `toolu_01GVSEPc5kSYcJgBvmGhFy6q`</summary>

```text
1	{
2	  "vast/deepseek_few-shot-3": {
3	    "confusion_matrix_normalized": [
4	      [0.5139, 0.1017, 0.2888],
5	      [0.3212, 0.7985, 0.5498],
6	      [0.1649, 0.0998, 0.1614]
7	    ],
8	    "labels": ["pro", "con", "neutral"],
9	    "n_valid": 1500,
10	    "source": "npz",
11	    "accuracy": 0.4967,
12	    "confusion_matrix_counts": [
13	      [240, 54, 145],
14	      [150, 424, 276],
15	      [77, 53, 81]
16	    ]
17	  },
18	  "vast/deepseek_few-shot-5": {
19	    "confusion_matrix_normalized": [
20	      [0.5268, 0.1149, 0.3068],
21	      [0.3105, 0.7853, 0.5398],
22	      [0.1627, 0.0998, 0.1534]
23	    ],
24	    "labels": ["pro", "con", "neutral"],
25	    "n_valid": 1500,
26	    "source": "npz",
27	    "accuracy": 0.4933,
28	    "confusion_matrix_counts": [
29	      [246, 61, 154],
30	      [145, 417, 271],
31	      [76, 53, 77]
32	    ]
33	  }
34	}
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77640fff-afb9-4e10-a324-9c638e399161",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "8669b7af-c3ba-4324-b5b7-37b83fb069f7",
  "sourceToolAssistantUUID": "77640fff-afb9-4e10-a324-9c638e399161",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T14:57:15.734Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01T5hqZDXw826WyRbwb7vPEe`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts -name \"*confusion*\" -o -name \"*new_cms*\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8669b7af-c3ba-4324-b5b7-37b83fb069f7",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhLQvud995gb4n1btjY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c1236f34-4a22-42a6-bf6b-5d06482ea3e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012h6iLCjzUtGj3KEgK4ujpC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 9189,
      "cache_read_input_tokens": 60969,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9189
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 223,
          "cache_read_input_tokens": 60969,
          "cache_creation_input_tokens": 9189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9189,
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

_source line 36 · 2026-05-23T14:57:15.797Z_

<details><summary>↩ Tool result · `toolu_01T5hqZDXw826WyRbwb7vPEe`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_new_cms_round2.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_new_cms.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_new_cms_vast_qwen3_zs.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1236f34-4a22-42a6-bf6b-5d06482ea3e4",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "d5a42f25-6e81-4103-941d-fd3b1dd86de3",
  "sourceToolAssistantUUID": "c1236f34-4a22-42a6-bf6b-5d06482ea3e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-23T14:57:17.055Z_

Great! Let me also check the updated_empirical_results.json to see its structure:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5a42f25-6e81-4103-941d-fd3b1dd86de3",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhLeaSmWi4diUp7PL3M",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7f1780e7-8213-4403-85d8-f523814f7b3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DXT7AZg4CMWTQBvyV1yWdP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 70158,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 955,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 38 · 2026-05-23T14:57:17.182Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GQ6u9ZL3oxXmdWRjxfunKY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f1780e7-8213-4403-85d8-f523814f7b3a",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhLeaSmWi4diUp7PL3M",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7cd4780f-bff1-4281-8d13-ddaaa4c9a336",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DXT7AZg4CMWTQBvyV1yWdP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 70158,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 955
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 129,
          "cache_read_input_tokens": 70158,
          "cache_creation_input_tokens": 955,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 955,
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

_source line 39 · 2026-05-23T14:57:17.191Z_

<details><summary>↩ Tool result · `toolu_01GQ6u9ZL3oxXmdWRjxfunKY`</summary>

```text
1	{
2	  "confusion_matrices": {
3	    "civil_comments_deepseek_few-shot-5": [
4	      [
5	        0.7341211225997046,
6	        0.19863013698630136
7	      ],
8	      [
9	        0.2658788774002954,
10	        0.8013698630136986
11	      ]
12	    ],
13	    "civil_comments_qwen2.5-7b_few-shot-3": [
14	      [
15	        0.6787296898079763,
16	        0.2191780821917808
17	      ],
18	      [
19	        0.3212703101920236,
20	        0.7808219178082192
21	      ]
22	    ],
23	    "civil_comments_qwen2.5-7b_few-shot-5": [
24	      [
25	        0.7370753323485968,
26	        0.23972602739726026
27	      ],
28	      [
29	        0.26292466765140327,
30	        0.7602739726027398
31	      ]
32	    ],
33	    "civil_comments_qwen2.5-7b_zero-shot": [
34	      [
35	        0.7481536189069424,
36	        0.3150684931506849
37	      ],
38	      [
39	        0.2518463810930576,
40	        0.684931506849315
41	      ]
42	    ],
43	    "civil_comments_qwen3_few-shot-3": [
44	      [
45	        0.8179126572908957,
46	        0.25517241379310346
47	      ],
48	      [
49	        0.18208734270910437,
50	        0.7448275862068966
51	      ]
52	    ],
53	    "civil_comments_qwen3_few-shot-5": [
54	      [
55	        0.8240534521158129,
56	        0.20689655172413793
57	      ],
58	      [
59	        0.1759465478841871,
60	        0.7931034482758621
61	      ]
62	    ],
63	    "civil_comments_qwen3_zero-shot": [
64	      [
65	        0.778118609406953,
66	        0.25742574257425743
67	      ],
68	      [
69	        0.22188139059304704,
70	        0.7425742574257426
71	      ]
72	    ],
73	    "humaid_deepseek_few-shot-3": [
74	      [
75	        0.5795454545454546,
76	        0.15,
77	        0.050955414012738856,
78	        0.0,
79	        0.0,
80	        0.011363636363636364,
81	        0.1297071129707113,
82	        0.0,
83	        0.008287292817679558,
84	        0.043478260869565216
85	      ],
86	      [
87	        0.0,
88	        0.7,
89	        0.03184713375796178,
90	        0.024,
91	        0.0,
92	        0.056818181818181816,
93	        0.03347280334728033,
94	        0.018867924528301886,
95	        0.008287292817679558,
96	        0.006211180124223602
97	      ],
98	      [
99	        0.07954545454545454,
100	        0.0,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cd4780f-bff1-4281-8d13-ddaaa4c9a336",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "e2dbb63d-a483-48fd-90bd-226cc581a246",
  "sourceToolAssistantUUID": "7cd4780f-bff1-4281-8d13-ddaaa4c9a336",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-23T14:57:18.452Z_

Perfect! Now let me create a comprehensive summary. Let me also check for the exposure-specific sign reversal computation:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2dbb63d-a483-48fd-90bd-226cc581a246",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhLkcb1EQButBj98GuV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1ee23948-1352-4864-a55f-86955807847c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DW4syBoBEuHU9JRhHPtbWA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1112,
      "cache_read_input_tokens": 71113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1112,
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

_source line 41 · 2026-05-23T14:57:19.809Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01RR9r56eQjxCvcfnhuQkYRR`</summary>

```json
{
  "pattern": "exposure.*sign|sign.*flip.*exposure",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts",
  "type": "py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ee23948-1352-4864-a55f-86955807847c",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhLkcb1EQButBj98GuV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c8975435-5195-4de6-9baa-3e0505b5013f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DW4syBoBEuHU9JRhHPtbWA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1112,
      "cache_read_input_tokens": 71113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1112,
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

_source line 42 · 2026-05-23T14:57:19.830Z_

<details><summary>↩ Tool result · `toolu_01RR9r56eQjxCvcfnhuQkYRR`</summary>

```text
Found 7 files
artifacts/sign_reversal_determinants.py
artifacts/exp_realistic_epsilon.py
artifacts/exp_e_asv_stability.py
artifacts/compute_updated_empirical.py
artifacts/compute_delta_max.py
artifacts/_project/intermediate/case_study_analysis.py
artifacts/plan012_case_study/case_study_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8975435-5195-4de6-9baa-3e0505b5013f",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "854ae5dd-e86f-449e-85ec-439b98386ea7",
  "sourceToolAssistantUUID": "c8975435-5195-4de6-9baa-3e0505b5013f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T14:57:20.184Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MBKM5mcwkFB5dgeH6XY2eu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_exposure_dirichlet_subspace.py",
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "854ae5dd-e86f-449e-85ec-439b98386ea7",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhLkcb1EQButBj98GuV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b87a298c-efae-4527-84b1-3875e728c259",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DW4syBoBEuHU9JRhHPtbWA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1112,
      "cache_read_input_tokens": 71113,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1112
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 267,
          "cache_read_input_tokens": 71113,
          "cache_creation_input_tokens": 1112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1112,
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

_source line 44 · 2026-05-23T14:57:20.189Z_

<details><summary>↩ Tool result · `toolu_01MBKM5mcwkFB5dgeH6XY2eu`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Dirichlet Prior Subspace Analysis for Exposure Misclassification
4	
5	The 85% violation rate from mvp_exposure_dag.py uses Dirichlet(1,1,1) uniform
6	prior over column-stochastic matrices. Actual LLM confusion matrices are far
7	more diagonal-dominant. This script stratifies the violation rate by minimum
8	diagonal value of C to assess practical relevance.
9	
10	Subspaces:
11	  - Full space (no diagonal constraint, equiv. Dirichlet(1,1,1))
12	  - min(diag(C)) >= 0.5
13	  - min(diag(C)) >= 0.7  (realistic LLM accuracy)
14	  - min(diag(C)) >= 0.9  (high-accuracy LLM)
15	
16	Method: direct sampling via truncated Beta(1,2) for diagonal entries +
17	uniform simplex split for off-diagonal. Equivalent to uniform distribution
18	on the constrained space, but O(n) time/memory vs rejection sampling.
19	
20	For K=3, each column's diagonal entry d ~ Beta(1,2) truncated to [thresh,1],
21	density f(d) = 2(1-d)/(1-thresh)^2. Inverse CDF: d = 1-(1-thresh)*sqrt(1-U).
22	
23	Dependencies: numpy
24	"""
25	
26	import numpy as np
27	import time
28	
29	P_A = np.array([0.4, 0.35, 0.25])
30	BETA = np.array([0.0, 1.0, -0.5])
31	
32	DIAG_THRESHOLDS = [0.0, 0.5, 0.7, 0.9]
33	N_SAMPLES = 50_000
34	
35	
36	def theoretical_plim(C, p_A, beta):
37	    """plim gamma = (E[Z'Z])^{-1} E[Z'X] beta for exposure DAG."""
38	    p0, p1, p2 = p_A
39	    q = C @ p_A
40	    EZZ = np.array([
41	        [1.0,  q[1], q[2]],
42	        [q[1], q[1], 0.0],
43	        [q[2], 0.0,  q[2]],
44	    ])
45	    EZX = np.array([
46	        [1.0,  p1,            p2],
47	        [q[1], C[1, 1] * p1,  C[1, 2] * p2],
48	        [q[2], C[2, 1] * p1,  C[2, 2] * p2],
49	    ])
50	    return np.linalg.solve(EZZ, EZX @ beta)
51	
52	
53	def sample_and_analyze(n, diag_thresh, p_A, beta, rng):
54	    """
55	    Sample n column-stochastic 3x3 C with min(diag) >= diag_thresh,
56	    compute plim for each, return statistics. No large array stored.
57	    """
58	    n_sr = 0       # sign reversal (any component)
59	    n_amp = 0      # amplification (any component)
60	    n_either = 0   # any violation
61	    n_valid = 0
62	
63	    worst_sev = 0.0
64	    worst_C = None
65	    worst_plim = None
66	
67	    # Process in manageable chunks
68	    chunk = min(n, 5000)
69	    remaining = n
70	
71	    while remaining > 0:
72	        batch = min(chunk, remaining)
73	        remaining -= batch
74	
75	        # Direct sampling: each column independently
76	        C_batch = np.empty((batch, 3, 3))
77	        for col in range(3):
78	            U = rng.uniform(size=batch)
79	            d = 1.0 - (1.0 - diag_thresh) * np.sqrt(1.0 - U)
80	            V = rng.uniform(size=batch)
81	            rem = 1.0 - d
82	
83	            off = [r for r in range(3) if r != col]
84	            C_batch[:, col, col] = d
85	            C_batch[:, off[0], col] = rem * V
86	            C_batch[:, off[1], col] = rem * (1.0 - V)
87	
88	        # Analyze each C
89	        for i in range(batch):
90	            C = C_batch[i]
91	            try:
92	                plim = theoretical_plim(C, p_A, beta)
93	            except np.linalg.LinAlgError:
94	                continue
95	
96	            n_valid += 1
97	            sr = False
98	            amp = False
99	            for k in [1, 2]:
100	                if abs(beta[k]) < 1e-10:
101	                    continue
102	                if plim[k] * beta[k] < 0:
103	                    sr = True
104	                if abs(plim[k]) > abs(beta[k]):
105	                    amp = True
106	
107	            if sr:
108	                n_sr += 1
109	            if amp:
110	                n_amp += 1
111	            if sr or amp:
112	                n_either += 1
113	                sev = max(
114	                    abs(plim[1] / beta[1]) if abs(beta[1]) > 1e-10 else 0,
115	                    abs(plim[2] / beta[2]) if abs(beta[2]) > 1e-10 else 0,
116	                )
117	                if sev > worst_sev:
118	                    worst_sev = sev
119	                    worst_C = C.copy()
120	                    worst_plim = plim.copy()
121	
122	    return {
123	        "n_valid": n_valid,
124	        "n_violation": n_either,
125	        "n_sign_rev": n_sr,
126	        "n_amp": n_amp,
127	        "violation_rate": n_either / n_valid if n_valid > 0 else 0,
128	        "sign_rev_rate": n_sr / n_valid if n_valid > 0 else 0,
129	        "amp_rate": n_amp / n_valid if n_valid > 0 else 0,
130	        "worst_severity": worst_sev,
131	        "worst_C": worst_C,
132	        "worst_plim": worst_plim,
133	    }
134	
135	
136	def main():
137	    t_start = time.time()
138	    rng = np.random.default_rng(42)
139	
140	    print("=" * 85)
141	    print("Dirichlet Subspace Analysis: Exposure Misclassification Violation Rates")
142	    print("=" * 85)
143	    print()
144	    print(f"DGP: P(A)=[{P_A[0]}, {P_A[1]}, {P_A[2]}], "
145	          f"beta=[{BETA[0]}, {BETA[1]}, {BETA[2]}]")
146	    print(f"Samples per subspace: {N_SAMPLES:,}")
147	    print(f"Method: direct sampling (truncated Beta(1,2) diagonal + uniform split)")
148	
149	    # ── Main table ───────────────────────────────────────────
150	    print(f"\n{'Subspace':>12} {'N':>8} {'Violation%':>11} "
151	          f"{'SignRev%':>10} {'Amplif%':>10} {'Worst':>8} {'Time':>7}")
152	    print("-" * 70)
153	
154	    all_results = {}
155	
156	    for thresh in DIAG_THRESHOLDS:
157	        t0 = time.time()
158	        label = f"diag>={thresh:.1f}" if thresh > 0 else "full"
159	
160	        res = sample_and_analyze(N_SAMPLES, thresh, P_A, BETA, rng)
161	        elapsed = time.time() - t0
162	
163	        all_results[thresh] = res
164	
165	        print(f"{label:>12} {res['n_valid']:>8,} {100*res['violation_rate']:>10.1f}% "
166	              f"{100*res['sign_rev_rate']:>9.1f}% {100*res['amp_rate']:>9.1f}% "
167	              f"{res['worst_severity']:>8.2f} {elapsed:>6.1f}s")
168	
169	    # ── Worst-case per subspace ──────────────────────────────
170	    print("\n" + "=" * 85)
171	    print("Worst-Case C per Subspace")
172	    print("=" * 85)
173	
174	    for thresh, res in all_results.items():
175	        label = f"diag>={thresh:.1f}" if thresh > 0 else "full"
176	        if res['worst_C'] is None:
177	            print(f"\n{label}: no violations found")
178	            continue
179	
180	        C_w = res['worst_C']
181	        p_w = res['worst_plim']
182	        print(f"\n{label} (severity={res['worst_severity']:.2f}, "
183	              f"diag=[{C_w[0,0]:.3f}, {C_w[1,1]:.3f}, {C_w[2,2]:.3f}]):")
184	        for row in C_w:
185	            print(f"  [{row[0]:.3f}  {row[1]:.3f}  {row[2]:.3f}]")
186	
187	        for k in [1, 2]:
188	            if abs(BETA[k]) > 1e-10:
189	                ratio = p_w[k] / BETA[k]
190	                if p_w[k] * BETA[k] < 0:
191	                    tag = "SIGN REVERSAL"
192	                elif abs(p_w[k]) > abs(BETA[k]):
193	                    tag = "AMPLIFICATION"
194	                else:
195	                    tag = "toward null"
196	                print(f"  beta_{k}={BETA[k]:.2f} -> gamma_{k}={p_w[k]:.4f} "
197	                      f"(ratio={ratio:.2f}, {tag})")
198	
199	    # ── Paper framing guidance ───────────────────────────────
200	    print("\n" + "=" * 85)
201	    print("PAPER FRAMING GUIDANCE")
202	    print("=" * 85)
203	
204	    print(f"\n{'Subspace':<15} {'Violation':>10} {'SignRev':>10} {'Amplif':>10} {'Assessment':>25}")
205	    print("-" * 73)
206	    for thresh, res in all_results.items():
207	        label = f"diag>={thresh:.1f}" if thresh > 0 else "full space"
208	        vr = res['violation_rate']
209	        if vr > 0.10:
210	            assess = "STRONG argument"
211	        elif vr > 0.01:
212	            assess = "moderate (note scope)"
213	        elif vr > 0.001:
214	            assess = "weak (flag in paper)"
215	        elif vr > 0:
216	            assess = "rare (theoretical only)"
217	        else:
218	            assess = "no violations"
219	        print(f"{label:<15} {100*vr:>9.1f}% {100*res['sign_rev_rate']:>9.1f}% "
220	              f"{100*res['amp_rate']:>9.1f}% {assess:>25}")
221	
222	    elapsed_total = time.time() - t_start
223	    print(f"\nTotal runtime: {elapsed_total:.1f}s")
224	
225	
226	if __name__ == "__main__":
227	    main()
228	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b87a298c-efae-4527-84b1-3875e728c259",
  "isSidechain": true,
  "promptId": "cda5cfc5-1136-4ede-bcf5-df8462bcccbd",
  "agentId": "a8d5f7280dd4c25d0",
  "type": "user",
  "uuid": "d1bfbc3e-af24-4cbd-bf15-a9d12e2fdb47",
  "sourceToolAssistantUUID": "b87a298c-efae-4527-84b1-3875e728c259",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-23T14:57:44.728Z_

Perfect! Now I have all the information needed. Let me compile the comprehensive report.

## Summary: Empirical LLM Confusion Matrices and Bias/Sign Reversal Computation

### Part 1: Empirical LLM Confusion Matrices (JSON Files)

I found multiple JSON files containing empirical LLM confusion matrices:

**Main empirical confusion matrix files:**

1. **/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json**
   - Structure: `"confusion_matrices"` key containing 23 empirical LLM confusion matrices
   - Coverage: 3 datasets × models/prompts combinations
   - Example keys: `"civil_comments_qwen3_zero-shot"`, `"humaid_deepseek_few-shot-3"`, `"vast/llama4_few-shot-5"`
   - Format: Column-stochastic K×K matrices (K=2 for civil_comments, K=3 for vast, K=10 for humaid)

2. **/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_new_cms.json**
   - Structure: Config-level confusion matrices with metadata (labels, n_valid, accuracy, normalized and count versions)
   - Example structure shows both normalized column-stochastic form and raw counts
   - Contains fields: `confusion_matrix_normalized`, `confusion_matrix_counts`, `labels`, `n_valid`, `accuracy`, `source`

3. **/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_new_cms_round2.json** and **plan011_new_cms_vast_qwen3_zs.json**
   - Additional variants with similar structure

**Other files containing confusion matrix data:**
- `plan006/asv_empirical_results.json` - Contains `"confusion_matrices"` key with 10×10 HumAID matrices
- `plan006_mock/asv_empirical_results.json` - Mock versions for testing
- Various results JSON files from different experiments that reference confusion matrices

---

### Part 2: Exposure Bias and Sign Reversal Computation

The core computational pipeline is in **plan_006_asv_empirical.py** with specialized implementations in other scripts. Here's the detailed flow:

#### **Core Functions (plan_006_asv_empirical.py, lines 369-420):**

**1. compute_plim(C, st, K) — Main bias computation under exposure topology:**

```python
def compute_plim(C, st, K):
    if st['topology'] == 'exposure':
        q = C @ st['p_A']                    # q = C * p_A (Eq: E[D_k])
        cy = C @ st['E_YD']                  # cy = C * E[Y*D] (Eq: E[Y*D_k])
        
        # Build EZZ = E[Z'Z] where Z = [1, D_1, D_2, ..., D_{K-1}]
        EZZ = np.zeros((K, K))
        EZZ[0, 0] = 1.0
        for j in range(1, K):
            EZZ[0, j] = EZZ[j, 0] = q[j]
            EZZ[j, j] = q[j]
        
        # Build EZY = E[Z'Y]
        EZY = np.zeros(K)
        EZY[0] = st['E_Y']                  # E[Y]
        for j in range(1, K):
            EZY[j] = cy[j]                  # E[Y*D_j]
        
        return np.linalg.solve(EZZ, EZY)    # Solve for plim coefficients
```

**Key insight:** Under exposure, the observed confound is C (confusion matrix), which transforms:
- True group probabilities **p_A** → biased group probabilities **q = C @ p_A**
- True moment E[Y·D_k] → biased moment cy = C @ E[Y·D_k]

The plim is then `(E[Z'Z])^{-1} E[Z'Y]` where the moments are all computed under C.

**2. extract_tau(plim_result, topology) — Extract treatment effect:**

```python
def extract_tau(plim_result, topology):
    if isinstance(plim_result, np.ndarray):
        return float(plim_result[1])         # Return second element (treatment coefficient)
    return np.nan
```

#### **Sign Reversal Detection (sign_reversal_determinants.py, lines 109-147):**

```python
def exposure_outcome(C, beta, p_A=None, seed=42):
    """Run exposure DGP with custom beta and return sign-flip details."""
    K = C.shape[0]
    if p_A is None:
        p_A = plan_006.make_p_A(K)
    
    params = {"beta": np.asarray(beta), "p_A": p_A}
    st = plan_006.precompute_suff_stats(K, "exposure", params, seed=seed)
    
    # Compute plim under identity matrix (true params)
    plim_true = plan_006.compute_plim(np.eye(K), st, K)
    tau_true = plan_006.extract_tau(plim_true, "exposure")
    
    # Compute plim under confusion matrix C (biased)
    plim_biased = plan_006.compute_plim(C, st, K)
    tau_hat = plan_006.extract_tau(plim_biased, "exposure")
    
    # Detect sign flip for each coefficient k ∈ {1, ..., K-1}
    any_flip = False
    for i in range(1, K):
        tv = float(plim_true[i])
        bv = float(plim_biased[i])
        sign_flip = bool(np.sign(bv) != np.sign(tv)) if abs(tv) > 1e-10 else False
        if sign_flip:
            any_flip = True
    
    return {
        "any_flip": any_flip,
        "per_coef": [...],
        "tau_true": float(tau_true),
        "tau_hat": float(tau_hat),
    }
```

#### **Direct Exposure Violation Analysis (mvp_exposure_dirichlet_subspace.py, lines 36-51):**

This provides a clearer view of how sign reversal is determined:

```python
def theoretical_plim(C, p_A, beta):
    """Compute plim gamma under exposure for column-stochastic C."""
    q = C @ p_A                            # Biased marginal: E[D_k]
    
    # EZZ = E[Z'Z] with Z = [1, D_1, D_2]
    EZZ = np.array([
        [1.0,  q[1], q[2]],
        [q[1], q[1], 0.0],
        [q[2], 0.0,  q[2]],
    ])
    
    # EZX = E[Z'X·diag] where X represents treatment assignment
    EZX = np.array([
        [1.0,  p[1],        p[2]],
        [q[1], C[1,1]*p[1], C[1,2]*p[2]],
        [q[2], C[2,1]*p[1], C[2,2]*p[2]],
    ])
    
    return np.linalg.solve(EZZ, EZX @ beta)

# Sign reversal detection (lines 99-105):
for k in [1, 2]:
    if abs(beta[k]) < 1e-10:
        continue
    if plim[k] * beta[k] < 0:      # <-- SIGN REVERSAL CONDITION
        sr = True                   # True beta and plim have opposite signs
    if abs(plim[k]) > abs(beta[k]):
        amp = True                  # Amplification (magnitude increases)
```

#### **Insufficient Statistics Precomputation (plan_006_asv_empirical.py, lines 342-366):**

```python
def precompute_suff_stats(K, topology, params, N=N_PRECOMP, seed=42):
    rng = np.random.default_rng(seed)
    first_var, Y, A = GEN_FNS[topology](K, N, params, rng)
    
    elif topology == 'exposure':
        DA = np.zeros((N, K))
        for k in range(K):
            DA[:, k] = (A == k).astype(float)
        return dict(
            p_A=DA.mean(0),              # P(A=k)
            E_Y=Y.mean(),                # E[Y]
            E_YD=(DA * Y[:, None]).mean(0),  # E[Y·D_k]
            topology='exposure'
        )
```

---

### Part 3: How Sign Reversal is Determined Under Exposure

**The process:**

1. **Input:** Confusion matrix C (K×K column-stochastic), beta vector (K-dim causal effects), p_A (marginal probabilities)

2. **Transform via C:**
   - Compute biased marginals: **q = C @ p_A**
   - Compute biased moments: **cy = C @ E[Y·D]**
   - Build moment matrix: **EZZ** with elements q[j], **EZY** with elements cy[j]

3. **Solve for plim:**
   - **plim = EZZ^{-1} @ EZY**
   - Extract treatment coefficient: **gamma_true = plim[1]** (true) vs **gamma_biased = plim[1]** (under C)

4. **Detect sign reversal:**
   - For each coefficient k ∈ {1, ..., K-1}:
     - **Sign flips if: sign(plim[k]) ≠ sign(beta[k])** and |beta[k]| > 1e-10
   - Any flip → overall `any_flip = True`

**Key files implementing this:**
- `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/sign_reversal_determinants.py` (lines 109-147)
- `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_exposure_dirichlet_subspace.py` (lines 36-134)
- `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py` (lines 369-510)

**Results:** The analysis found that at min_diag ≥ 0.9 (realistic LLM confusion matrices), the sign reversal rate drops to near zero, while at min_diag < 0.5, violation rates exceed 83%.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1bfbc3e-af24-4cbd-bf15-a9d12e2fdb47",
  "isSidechain": true,
  "agentId": "a8d5f7280dd4c25d0",
  "requestId": "req_011CbKhLyeuwXBaqmYQiyD5F",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "459527d7-23db-473b-b3f0-debc367335d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "bda960fb-f645-4405-a119-332fbfa4589a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C5ARfnEKaVBbVhsGzfrxu7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3733,
      "cache_read_input_tokens": 72225,
      "output_tokens": 2829,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3733
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2829,
          "cache_read_input_tokens": 72225,
          "cache_creation_input_tokens": 3733,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3733,
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
