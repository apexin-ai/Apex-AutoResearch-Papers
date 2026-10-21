# code exp 029 a1 sensitivity

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_code_exp-029-a1-sensitivity_20260522T161509.log`
- **Structured JSON:** [`b32d089f5567a018d823.json`](../../sessions/b3/b32d089f5567a018d823.json)

## Before a recorded user message

6 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__update_registry"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "1b90ec40-dab9-4502-8619-3a73377111bc",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-ec-hte-llm-annotation/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779474000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "01648509-799b-4803-b04a-cde8d7e7a31e",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a"
}
```

---

### Assistant

_source line 4_

I'll start by reading the reference implementations to understand the existing code structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "01613294-5af3-4211-96ee-8dd679f418ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhEZgf9Di7AtVRdgGDB2sB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7078,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7078
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Agent · `toolu_01ViC7keEW7s5eZikifsAL3g`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find reference implementations",
  "prompt": "In the project at /home/ubuntu/ec_hte_llm_annotation, I need to find and read the following files to understand existing code patterns:\n\n1. `exp_mf2_cf_bootstrap_se.py` - has DIM estimator implementation\n2. `exp027b_cf_oracle_k2.py` - has DIM estimator implementation\n3. Any other exp*.py files that show the pattern for MC simulation, confusion matrix estimation, and CATE estimation\n\nSearch broadly: check root, src/, experiments/, scripts/, etc.\n\nFor each file found, read it fully and report:\n- The DGP (data generating process) setup\n- How confusion matrices are estimated (global, stratified, HB)\n- How CATE is estimated using DIM\n- How MC runs are structured\n- How results are saved\n\nBe very thorough - read the complete files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "be626722-bb9b-4d80-98e8-e4f295f51083",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhEZgf9Di7AtVRdgGDB2sB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7078,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7078
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### System

_source line 6_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a8238e369993613e3",
  "tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "description": "Find reference implementations",
  "task_type": "local_agent",
  "prompt": "In the project at /home/ubuntu/ec_hte_llm_annotation, I need to find and read the following files to understand existing code patterns:\n\n1. `exp_mf2_cf_bootstrap_se.py` - has DIM estimator implementation\n2. `exp027b_cf_oracle_k2.py` - has DIM estimator implementation\n3. Any other exp*.py files that show the pattern for MC simulation, confusion matrix estimation, and CATE estimation\n\nSearch broadly: check root, src/, experiments/, scripts/, etc.\n\nFor each file found, read it fully and report:\n- The DGP (data generating process) setup\n- How confusion matrices are estimated (global, stratified, HB)\n- How CATE is estimated using DIM\n- How MC runs are structured\n- How results are saved\n\nBe very thorough - read the complete files.",
  "uuid": "56a6b03f-3c5b-46d4-b666-4186fa14b263",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a"
}
```

---

## Round 1

59 recorded events

### User

_source line 7 · 2026-05-22T16:15:28.413Z_

In the project at /home/ubuntu/ec_hte_llm_annotation, I need to find and read the following files to understand existing code patterns:

1. `exp_mf2_cf_bootstrap_se.py` - has DIM estimator implementation
2. `exp027b_cf_oracle_k2.py` - has DIM estimator implementation
3. Any other exp*.py files that show the pattern for MC simulation, confusion matrix estimation, and CATE estimation

Search broadly: check root, src/, experiments/, scripts/, etc.

For each file found, read it fully and report:
- The DGP (data generating process) setup
- How confusion matrices are estimated (global, stratified, HB)
- How CATE is estimated using DIM
- How MC runs are structured
- How results are saved

Be very thorough - read the complete files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "c5381dc3-a201-42be-9b60-c93d5bf302a0"
}
```

</details>

---

### System

_source line 8_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8238e369993613e3",
  "tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "description": "Running find /home/ubuntu/ec_hte_llm_annotation -type f -…",
  "usage": {
    "total_tokens": 18562,
    "tool_uses": 1,
    "duration_ms": 1966
  },
  "last_tool_name": "Bash",
  "uuid": "a973f5e0-f7e2-4848-b104-901f5ffd76aa",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a"
}
```

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Bash · `toolu_017JGrCyvprRsuhQicL5HsQj`</summary>

```json
{
  "command": "find /home/ubuntu/ec_hte_llm_annotation -type f -name \"*.py\" | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "c3d8c506-58ab-49a2-9877-7e3295207955",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CVHsixEGMwEpThX8ijUh3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18553,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18553,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T16:15:30.553Z_

<details><summary>↩ Tool result · `toolu_017JGrCyvprRsuhQicL5HsQj`</summary>

```text
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py
/home/ubuntu/ec_hte_llm_annotation/exp027b_cf_oracle_k2.py
/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py
/home/ubuntu/ec_hte_llm_annotation/scripts/explore_tweeteval.py
/home/ubuntu/ec_hte_llm_annotation/scripts/fig1_bias_mechanism.py
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp004_hate_speech.py
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py
/home/ubuntu/ec_hte_llm_annotation/exp025_positive_scenario.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/utils.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/impl.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/_staggered.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/__init__.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/types.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/_multiprocess/__init__.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/annotated_doc/main.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/annotated_doc/__init__.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plot_collection.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/utils.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/bf_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/ess_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/forest_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/utils_plot_types.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/convergence_dist_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/ppc_rootogram_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/ppc_tstat.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/rank_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/pair_focus_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/loo_interval_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/ecdf_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/pair_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/combine.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/pava_residual_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/ppc_censored_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/pava_calibration_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/parallel_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/mcse_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/ppc_pit_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/trace_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/ppc_interval_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/psense_quantities_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/compare_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/psense_dist_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/loo_pit_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/autocorr_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/rank_dist_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/trace_dist_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/ppc_dist_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/energy_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/prior_posterior_plot.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "4b0efcf3-8b0b-42ad-a0a8-a0cf725b8f96"
}
```

</details>

---

### System

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8238e369993613e3",
  "tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "description": "Finding **/exp*.py",
  "usage": {
    "total_tokens": 21498,
    "tool_uses": 2,
    "duration_ms": 3898
  },
  "last_tool_name": "Glob",
  "uuid": "c6f28612-b144-4914-8ece-89e5bbf959d6",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a"
}
```

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_01MP2RJdZNPsGpDuG1kcQ2Uj`</summary>

```json
{
  "pattern": "**/exp*.py",
  "path": "/home/ubuntu/ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "cb1d9fbf-589a-4bc4-bf76-d79385874e00",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R1ksD6epAbgQwJ152rqdVL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2932,
      "cache_read_input_tokens": 18553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2932,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T16:15:32.374Z_

<details><summary>↩ Tool result · `toolu_01MP2RJdZNPsGpDuG1kcQ2Uj`</summary>

```text
.venv/lib/python3.14/site-packages/scipy/special/_precompute/expn_asy.py
.venv/lib/python3.14/site-packages/pandas/core/computation/expr.py
.venv/lib/python3.14/site-packages/pandas/core/computation/expressions.py
.venv/lib/python3.14/site-packages/pandas/core/window/expanding.py
.venv/lib/python3.14/site-packages/statsmodels/tsa/statespace/exponential_smoothing.py
.venv/lib/python3.14/site-packages/shap/benchmark/experiments.py
.venv/lib/python3.14/site-packages/setuptools/config/expand.py
exp002_bias_bound.py
scripts/explore_tweeteval.py
exp001_regularize.py
exp001_hyperprior_sensitivity.py
exp001_hb_synthetic.py
exp005_diagnostic_criterion.py
exp003_tweeteval.py
exp006_budget_sensitivity.py
exp011_causal_forest.py
exp007_ppci_dsl.py
.venv/lib/python3.14/site-packages/datasets/utils/experimental.py
exp013_boundary_condition.py
exp014_asymmetric.py
exp008_multi_llm.py
exp004_hate_speech.py
exp010_misspecified_subgroups.py
exp008_gpt55_annotate.py
exp008_gpt5x_annotate.py
exp008_filter_analysis.py
exp015_semi_real_cm.py
exp016_semi_real_better_cm.py
exp017_rlearner.py
exp018_multiplicative_dgp.py
exp019_pz1_sweep.py
exp020_kappa_sweep.py
exp021_seeds_supplement.py
exp022_ppi_dsl_baseline.py
exp023_ppi_dsl_baseline.py
exp023_civil_comments_prepare.py
exp023_civil_comments_semisynthetic.py
exp023_annotate_parallel.py
exp023_civil_comments_semisynthetic_v2.py
exp023_ppi_dsl_k2.py
exp023_civil_comments_symmetric.py
exp023_civil_comments_semisynthetic_v3.py
exp_w4_bootstrap_se.py
exp_w8_a5_violation.py
exp_mf2_cf_bootstrap_se.py
exp024_realcm_bias_identity.py
exp025_positive_scenario.py
exp026_low_budget_hb.py
exp027_cf_oracle_coverage.py
exp027b_cf_oracle_k2.py
exp027c_cf_oracle_mf2dgp.py
exp028_asymmetric_diagnostic_auc.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "ae82aa03-e9be-49db-b840-bb7a3c2a6ba6"
}
```

</details>

---

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8238e369993613e3",
  "tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "description": "Reading exp_mf2_cf_bootstrap_se.py",
  "usage": {
    "total_tokens": 22324,
    "tool_uses": 3,
    "duration_ms": 5646
  },
  "last_tool_name": "Read",
  "uuid": "c614f649-d597-4c99-8cec-362bcb000ce4",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a"
}
```

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01KWqyky6zfvWAD9B5JmtExy`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp_mf2_cf_bootstrap_se.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "0337c680-fc23-461a-a8ac-8fab0bef5b09",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01K3cjFbE89rsaPDM11cDWnZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 824,
      "cache_read_input_tokens": 21485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 824,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T16:15:34.069Z_

<details><summary>↩ Tool result · `toolu_01KWqyky6zfvWAD9B5JmtExy`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	exp_mf2_cf_bootstrap_se.py — CausalForestDML: Bootstrap SE vs Plug-in SE Coverage (MF2)
4	
5	Validates whether CausalForestDML's plug-in SE captures confusion matrix
6	estimation uncertainty. Compares:
7	  1. Plug-in SE: forest effect_inference SE propagated through M⁻¹ (delta method)
8	  2. CM-Bootstrap SE: resample experts → re-estimate CM → re-apply M⁻¹ → SD of corrected CATEs
9	  3. Combined SE: sqrt(plugin² + bootstrap²)
10	
11	DGP: K=2, π=[0.05, 0.25], τ(z=0)=0.10, τ(z=1)=0.40
12	N=5000, n_expert ∈ {100, 250, 500}, 50 MC runs, 100 CM-bootstrap resamples
13	"""
14	
15	import argparse
16	import os
17	import time
18	import warnings
19	
20	import numpy as np
21	import pandas as pd
22	from econml.dml import CausalForestDML
23	from sklearn.linear_model import LinearRegression, LogisticRegression
24	
25	warnings.filterwarnings('ignore')
26	
27	N = 5000
28	MISCLASS = [0.05, 0.25]
29	TAU_Z0 = 0.10
30	TAU_Z1 = 0.40
31	TAU_TRUE = np.array([TAU_Z0, TAU_Z1])
32	LABELS = ['A', 'B']
33	
34	
35	def generate_data(n_expert, seed):
36	    rng = np.random.RandomState(seed)
37	    T = rng.binomial(1, 0.5, N)
38	    Z = rng.binomial(1, 0.5, N)
39	    S = rng.choice(LABELS, N, p=[0.5, 0.5])
40	    X = rng.randn(N, 5)
41	    tau = np.where(Z == 1, TAU_Z1, TAU_Z0)
42	    Y = 1.0 + tau * T + 0.5 * X[:, 0] + rng.randn(N)
43	    mc_rates = np.where(S == 'A', MISCLASS[0], MISCLASS[1])
44	    Z_tilde = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)
45	    idx = rng.choice(N, min(n_expert, N), replace=False)
46	    expert_mask = np.zeros(N, dtype=bool)
47	    expert_mask[idx] = True
48	    return dict(T=T, Z=Z, Z_tilde=Z_tilde, S=S, X=X, Y=Y, expert_mask=expert_mask)
49	
50	
51	def estimate_cm(z_true, z_hat):
52	    C = np.zeros((2, 2))
53	    for z in [0, 1]:
54	        mask = z_true == z
55	        n = mask.sum()
56	        for zh in [0, 1]:
57	            C[z, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
58	    return C
59	
60	
61	def build_mixing_matrix(C):
62	    M = np.zeros((2, 2))
63	    for zh in [0, 1]:
64	        cs = C[0, zh] + C[1, zh]
65	        M[zh, 0] = C[0, zh] / cs if cs > 0 else 0.5
66	        M[zh, 1] = C[1, zh] / cs if cs > 0 else 0.5
67	    return M
68	
69	
70	def invert_mixing(M, tau_obs, se_obs):
71	    if np.linalg.cond(M) > 100 or abs(np.linalg.det(M)) < 1e-10:
72	        return tau_obs.copy(), se_obs.copy(), True
73	    Mi = np.linalg.inv(M)
74	    tau_c = Mi @ tau_obs
75	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
76	    return tau_c, se_c, False
77	
78	
79	def run_one_mc(n_expert, seed, n_bootstrap):
80	    data = generate_data(n_expert, seed)
81	    Y, T, Z, Z_tilde, S, X = (
82	        data['Y'], data['T'], data['Z'], data['Z_tilde'], data['S'], data['X']
83	    )
84	    em = data['expert_mask']
85	
86	    z_exp = Z[em]
87	    zt_exp = Z_tilde[em]
88	    s_exp = S[em]
89	    n_exp = em.sum()
90	
91	    # Per-subgroup CM from expert sample
92	    M_sub = {}
93	    for s in LABELS:
94	        sm = s_exp == s
95	        if sm.sum() >= 4:
96	            C_s = estimate_cm(z_exp[sm], zt_exp[sm])
97	        else:
98	            C_s = estimate_cm(z_exp, zt_exp)
99	        M_sub[s] = build_mixing_matrix(C_s)
100	
101	    # ── Fit CausalForestDML ──
102	    X_features = np.column_stack([Z_tilde, X]).astype(float)
103	    cf = CausalForestDML(
104	        model_y=LinearRegression(),
105	        model_t=LogisticRegression(solver='lbfgs'),
106	        discrete_treatment=True,
107	        n_estimators=200,
108	        min_samples_leaf=20,
109	        random_state=seed,
110	    )
111	    cf.fit(Y, T, X=X_features)
112	
113	    # Individual CATEs
114	    cate_all = cf.effect(X_features).flatten()
115	
116	    # Per-subgroup observed CATEs: mean(τ̂ᵢ | Z_tilde=z, S=s)
117	    sub_obs = {}
118	    for s in LABELS:
119	        sm = S == s
120	        vals = []
121	        for z in [0, 1]:
122	            mask = sm & (Z_tilde == z)
123	            if mask.sum() == 0:
124	                return None
125	            vals.append(cate_all[mask].mean())
126	        sub_obs[s] = np.array(vals)
127	
128	    # Plug-in SE from effect_inference at representative points
129	    X_mean = X.mean(axis=0)
130	    X_eval = np.array([
131	        np.concatenate([[0], X_mean]),
132	        np.concatenate([[1], X_mean]),
133	    ])
134	    try:
135	        inf = cf.effect_inference(X_eval)
136	        se_raw = np.asarray(inf.stderr).flatten()
137	        if np.any(np.isnan(se_raw)) or np.any(se_raw <= 0):
138	            se_raw = np.full(2, np.nan)
139	    except Exception:
140	        se_raw = np.full(2, np.nan)
141	
142	    sub_se_obs = {s: se_raw.copy() for s in LABELS}
143	
144	    # ── Plug-in: M⁻¹ corrected ──
145	    plugin_tau_sub, plugin_se_sub = {}, {}
146	    for s in LABELS:
147	        tau_c, se_c, _ = invert_mixing(M_sub[s], sub_obs[s], sub_se_obs[s])
148	        plugin_tau_sub[s] = tau_c
149	        plugin_se_sub[s] = se_c
150	
151	    sub_w = {s: (S == s).sum() / N for s in LABELS}
152	    plugin_tau = sum(sub_w[s] * plugin_tau_sub[s] for s in LABELS)
153	    plugin_se = np.sqrt(sum((sub_w[s] * plugin_se_sub[s]) ** 2 for s in LABELS))
154	
155	    # ── CM Bootstrap ──
156	    boot_taus = np.zeros((n_bootstrap, 2))
157	    rng_boot = np.random.RandomState(seed * 1000 + 7)
158	
159	    for b in range(n_bootstrap):
160	        boot_idx = rng_boot.choice(n_exp, n_exp, replace=True)
161	        z_b, zt_b, s_b = z_exp[boot_idx], zt_exp[boot_idx], s_exp[boot_idx]
162	
163	        b_tau = np.zeros(2)
164	        for s in LABELS:
165	            sm_b = s_b == s
166	            if sm_b.sum() >= 4:
167	                C_b = estimate_cm(z_b[sm_b], zt_b[sm_b])
168	            else:
169	                C_b = estimate_cm(z_b, zt_b)
170	            M_b = build_mixing_matrix(C_b)
171	            tau_c_b, _, _ = invert_mixing(M_b, sub_obs[s], sub_se_obs[s])
172	            b_tau += sub_w[s] * tau_c_b
173	        boot_taus[b] = b_tau
174	
175	    boot_se = np.nanstd(boot_taus, axis=0)
176	
177	    # ── Results ──
178	    result = {'n_expert': n_expert, 'seed': seed}
179	    for z in [0, 1]:
180	        zl = f'z{z}'
181	        # Plug-in CI
182	        pi_lo = plugin_tau[z] - 1.96 * plugin_se[z]
183	        pi_hi = plugin_tau[z] + 1.96 * plugin_se[z]
184	        result[f'plugin_covers_{zl}'] = int(pi_lo <= TAU_TRUE[z] <= pi_hi)
185	        result[f'plugin_se_{zl}'] = plugin_se[z]
186	        result[f'plugin_width_{zl}'] = pi_hi - pi_lo
187	        result[f'tau_hat_{zl}'] = plugin_tau[z]
188	
189	        # CM-Bootstrap CI (uses same point estimate, different SE)
190	        bs_lo = plugin_tau[z] - 1.96 * boot_se[z]
191	        bs_hi = plugin_tau[z] + 1.96 * boot_se[z]
192	        result[f'bootstrap_covers_{zl}'] = int(bs_lo <= TAU_TRUE[z] <= bs_hi)
193	        result[f'bootstrap_se_{zl}'] = boot_se[z]
194	        result[f'bootstrap_width_{zl}'] = bs_hi - bs_lo
195	
196	        # Combined CI
197	        comb_se = np.sqrt(plugin_se[z] ** 2 + boot_se[z] ** 2)
198	        cb_lo = plugin_tau[z] - 1.96 * comb_se
199	        cb_hi = plugin_tau[z] + 1.96 * comb_se
200	        result[f'combined_covers_{zl}'] = int(cb_lo <= TAU_TRUE[z] <= cb_hi)
201	        result[f'combined_se_{zl}'] = comb_se
202	        result[f'combined_width_{zl}'] = cb_hi - cb_lo
203	
204	    return result
205	
206	
207	def aggregate(df_raw):
208	    rows = []
209	    for ne, grp in df_raw.groupby('n_expert'):
210	        for method, col_prefix in [
211	            ('plugin', 'plugin'),
212	            ('cm_bootstrap', 'bootstrap'),
213	            ('combined', 'combined'),
214	        ]:
215	            row = {'n_expert': int(ne), 'se_method': method}
216	            for z in [0, 1]:
217	                zl = f'z{z}'
218	                row[f'coverage_{zl}'] = grp[f'{col_prefix}_covers_{zl}'].mean()
219	                row[f'mean_se_{zl}'] = grp[f'{col_prefix}_se_{zl}'].mean()
220	                row[f'mean_width_{zl}'] = grp[f'{col_prefix}_width_{zl}'].mean()
221	            row['coverage_avg'] = (row['coverage_z0'] + row['coverage_z1']) / 2
222	            rows.append(row)
223	    return pd.DataFrame(rows)
224	
225	
226	def main():
227	    parser = argparse.ArgumentParser()
228	    parser.add_argument('--dry-run', action='store_true')
229	    args = parser.parse_args()
230	
231	    n_mc = 2 if args.dry_run else 50
232	    n_bootstrap = 5 if args.dry_run else 100
233	    n_experts = [100, 250, 500]
234	    seeds = list(range(42, 42 + n_mc))
235	
236	    print(f"MF2: CausalForestDML Bootstrap SE vs Plug-in SE Coverage")
237	    print(f"N={N}, n_expert={n_experts}, N_MC={n_mc}, N_boot={n_bootstrap}")
238	    print(f"DGP: K=2, pi={MISCLASS}, tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}")
239	    if args.dry_run:
240	        print("** DRY RUN **")
241	    print()
242	
243	    all_rows = []
244	    total = len(n_experts) * n_mc
245	    count = 0
246	    t0 = time.time()
247	
248	    for ne in n_experts:
249	        for seed in seeds:
250	            result = run_one_mc(ne, seed, n_bootstrap)
251	            if result is not None:
252	                all_rows.append(result)
253	            count += 1
254	            if count % max(1, total // 10) == 0:
255	                el = time.time() - t0
256	                eta = el / count * (total - count)
257	                print(f"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s")
258	
259	    elapsed = time.time() - t0
260	    print(f"\nDone in {elapsed:.1f}s ({len(all_rows)} successful MC runs)\n")
261	
262	    df_raw = pd.DataFrame(all_rows)
263	    df_agg = aggregate(df_raw)
264	
265	    # ── Print summary ──
266	    print("=" * 115)
267	    print("SUMMARY: CausalForestDML SE Coverage")
268	    print("=" * 115)
269	    header = (f"{'n_exp':>5} {'method':>14} | {'cov_z0':>7} {'cov_z1':>7} "
270	              f"{'cov_avg':>7} | {'SE_z0':>8} {'SE_z1':>8} | "
271	              f"{'width_z0':>9} {'width_z1':>9}")
272	    print(header)
273	    print("-" * len(header))
274	    for _, r in df_agg.iterrows():
275	        print(f"{int(r['n_expert']):5d} {r['se_method']:>14s} | "
276	              f"{r['coverage_z0']:7.3f} {r['coverage_z1']:7.3f} "
277	              f"{r['coverage_avg']:7.3f} | "
278	              f"{r['mean_se_z0']:8.4f} {r['mean_se_z1']:8.4f} | "
279	              f"{r['mean_width_z0']:9.4f} {r['mean_width_z1']:9.4f}")
280	
281	    # ── Save ──
282	    proj = '/home/ubuntu/ec_hte_llm_annotation'
283	    os.makedirs(f'{proj}/results', exist_ok=True)
284	    csv_path = f'{proj}/results/exp_mf2_cf_bootstrap_se.csv'
285	    raw_path = f'{proj}/results/exp_mf2_cf_bootstrap_se_raw.csv'
286	    df_agg.to_csv(csv_path, index=False)
287	    df_raw.to_csv(raw_path, index=False)
288	    print(f"\nSaved: {csv_path} ({len(df_agg)} rows)")
289	    print(f"Saved: {raw_path} ({len(df_raw)} rows)")
290	
291	    artifacts_dir = os.path.expanduser(
292	        '~/.agent-ml-research-idea_gen_0520/projects/'
293	        'ec_hte_llm_annotation/artifacts/mf2/data/')
294	    os.makedirs(artifacts_dir, exist_ok=True)
295	    art_path = os.path.join(artifacts_dir, 'exp_mf2_cf_bootstrap_se.csv')
296	    df_agg.to_csv(art_path, index=False)
297	    print(f"Saved: {art_path}")
298	
299	    # ── Interpretation ──
300	    print(f"\n{'=' * 80}")
301	    print("INTERPRETATION")
302	    print(f"{'=' * 80}")
303	    for ne in n_experts:
304	        sub = df_agg[df_agg['n_expert'] == ne]
305	        pi_cov = sub[sub['se_method'] == 'plugin']['coverage_avg'].values[0]
306	        bs_cov = sub[sub['se_method'] == 'cm_bootstrap']['coverage_avg'].values[0]
307	        cb_cov = sub[sub['se_method'] == 'combined']['coverage_avg'].values[0]
308	        if pi_cov >= 0.90:
309	            verdict = "plug-in SE sufficient"
310	        elif bs_cov >= 0.90:
311	            verdict = "plug-in insufficient, CM-bootstrap recommended"
312	        else:
313	            verdict = "both insufficient — possible CF SE calibration issue"
314	        print(f"  n_expert={ne:3d}: plugin={pi_cov:.2f}, bootstrap={bs_cov:.2f}, "
315	              f"combined={cb_cov:.2f} -> {verdict}")
316	
317	
318	if __name__ == '__main__':
319	    main()
320	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "9bcf4e9c-7381-410a-9b77-22716a7e8cb0"
}
```

</details>

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8238e369993613e3",
  "tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "description": "Reading exp027b_cf_oracle_k2.py",
  "usage": {
    "total_tokens": 22325,
    "tool_uses": 4,
    "duration_ms": 5916
  },
  "last_tool_name": "Read",
  "uuid": "fcfbee4e-5a90-481d-93c8-b4501111568a",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01J5N8Q66K9wmg6rspPRNget`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp027b_cf_oracle_k2.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "2198ea7b-d6e1-449a-a2d6-7945c3a0f7dc",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01K3cjFbE89rsaPDM11cDWnZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 824,
      "cache_read_input_tokens": 21485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 824,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T16:15:34.337Z_

<details><summary>↩ Tool result · `toolu_01J5N8Q66K9wmg6rspPRNget`</summary>

```text
1	#!/usr/bin/env python3
2	"""exp027b_cf_oracle_k2.py — CausalForest Oracle Coverage, K=2 extreme (exp-027b)
3	
4	K=2 variant of exp-027 to match the paper's DGP for the 83-85% coverage gap analysis.
5	
6	Six methods compared:
7	  1. Oracle (true Z): CausalForestDML with Z_true, no correction
8	  2. EC-HTE true CM: Z_hat forest + per-subgroup correction with true C_s
9	  3. EC-HTE estimated CM: Z_hat forest + per-subgroup correction with estimated C_s (HB)
10	  4. Global true CM: Z_hat forest + global correction with true C_bar
11	  5. Global estimated CM: Z_hat forest + global correction with estimated C_bar
12	  6. Naive: Z_hat forest, no correction
13	
14	DGP: K=2, pi=[0.05,0.25], weights=[0.5,0.5], tau(0)=0, tau(1)=0.3, N=5000, n_expert=250
15	Output: results/exp_cf_oracle_coverage_k2.csv
16	"""
17	
18	import os
19	import time
20	import warnings
21	
22	import numpy as np
23	import pandas as pd
24	from econml.dml import CausalForestDML
25	from sklearn.linear_model import LinearRegression, LogisticRegression
26	
27	warnings.filterwarnings('ignore')
28	
29	N = 5000
30	K = 2
31	N_EXPERT = 250
32	PI = [0.05, 0.25]
33	TAU_TRUE = {0: 0.0, 1: 0.3}
34	SUB_WEIGHTS = [0.5, 0.5]
35	N_MC = 100
36	BASE_SEED = 42
37	
38	
39	def generate_data(seed):
40	    rng = np.random.RandomState(seed)
41	    S = rng.randint(0, K, N)
42	    T = rng.binomial(1, 0.5, N)
43	    Z_true = rng.binomial(1, 0.5, N)
44	
45	    Z_hat = Z_true.copy()
46	    for s in range(K):
47	        mask_s = S == s
48	        flip = rng.binomial(1, PI[s], mask_s.sum())
49	        Z_hat[mask_s] = np.where(flip, 1 - Z_true[mask_s], Z_true[mask_s])
50	
51	    tau = np.where(Z_true == 1, TAU_TRUE[1], TAU_TRUE[0])
52	    baseline = 1.0 + 0.5 * Z_true
53	    Y = baseline + tau * T + rng.normal(0, 1, N)
54	
55	    expert_idx = rng.choice(N, N_EXPERT, replace=False)
56	    expert_mask = np.zeros(N, dtype=bool)
57	    expert_mask[expert_idx] = True
58	
59	    return Y, T, Z_true, Z_hat, S, expert_mask
60	
61	
62	def compute_confusion_matrix(z_true, z_hat):
63	    C = np.zeros((2, 2))
64	    for z in [0, 1]:
65	        mz = z_true == z
66	        C[z, 0] = (z_hat[mz] == 0).sum() + 1
67	        C[z, 1] = (z_hat[mz] == 1).sum() + 1
68	    return C / C.sum(axis=1, keepdims=True)
69	
70	
71	def build_mixing_matrix(C):
72	    M = np.zeros((2, 2))
73	    for zh in [0, 1]:
74	        cs = C[0, zh] + C[1, zh]
75	        if cs > 0:
76	            M[zh, 0] = C[0, zh] / cs
77	            M[zh, 1] = C[1, zh] / cs
78	        else:
79	            M[zh, :] = 0.5
80	    return M
81	
82	
83	def invert_mixing(M, tau_obs, se_obs, cond_threshold=100):
84	    cond = np.linalg.cond(M)
85	    if cond > cond_threshold or abs(np.linalg.det(M)) < 1e-10:
86	        return tau_obs.copy(), se_obs.copy()
87	    Mi = np.linalg.inv(M)
88	    tau_c = Mi @ tau_obs
89	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
90	    return tau_c, se_c
91	
92	
93	def true_confusion_matrix(pi_s):
94	    return np.array([[1 - pi_s, pi_s],
95	                     [pi_s, 1 - pi_s]])
96	
97	
98	def fit_cf_and_predict(Y, T, X_features, X_eval):
99	    cf = CausalForestDML(
100	        model_y=LinearRegression(),
101	        model_t=LogisticRegression(solver='lbfgs'),
102	        discrete_treatment=True,
103	        n_estimators=200,
104	        min_samples_leaf=20,
105	        random_state=42,
106	    )
107	    cf.fit(Y, T, X=X_features, W=None)
108	
109	    cate_vals = cf.effect(X_eval).flatten()
110	    try:
111	        inf = cf.effect_inference(X_eval)
112	        se_raw = inf.stderr
113	        if hasattr(se_raw, 'values'):
114	            se_raw = se_raw.values
115	        se_vals = np.asarray(se_raw).flatten()
116	    except Exception:
117	        se_vals = np.full(len(X_eval), np.nan)
118	
119	    return cate_vals, se_vals
120	
121	
122	def run_one_mc(seed):
123	    Y, T, Z_true, Z_hat, S, expert_mask = generate_data(seed)
124	
125	    X_eval = np.array([[z, s] for s in range(K) for z in [0, 1]], dtype=float)
126	
127	    X_oracle = np.column_stack([Z_true, S]).astype(float)
128	    oracle_cate, oracle_se = fit_cf_and_predict(Y, T, X_oracle, X_eval)
129	
130	    X_zhat = np.column_stack([Z_hat, S]).astype(float)
131	    zhat_cate, zhat_se = fit_cf_and_predict(Y, T, X_zhat, X_eval)
132	
133	    M_true_sub = {}
134	    for s in range(K):
135	        C_s_true = true_confusion_matrix(PI[s])
136	        M_true_sub[s] = build_mixing_matrix(C_s_true)
137	
138	    C_global_true = sum(SUB_WEIGHTS[s] * true_confusion_matrix(PI[s]) for s in range(K))
139	    M_global_true = build_mixing_matrix(C_global_true)
140	
141	    M_est_sub = {}
142	    for s in range(K):
143	        mask_s = expert_mask & (S == s)
144	        if mask_s.sum() >= 4:
145	            C_s = compute_confusion_matrix(Z_true[mask_s], Z_hat[mask_s])
146	        else:
147	            C_s = np.array([[0.5, 0.5], [0.5, 0.5]])
148	        M_est_sub[s] = build_mixing_matrix(C_s)
149	
150	    C_global_est = compute_confusion_matrix(Z_true[expert_mask], Z_hat[expert_mask])
151	    M_global_est = build_mixing_matrix(C_global_est)
152	
153	    rows = []
154	    for s in range(K):
155	        idx_z0 = s * 2
156	        idx_z1 = s * 2 + 1
157	
158	        o_tau = np.array([oracle_cate[idx_z0], oracle_cate[idx_z1]])
159	        o_se = np.array([oracle_se[idx_z0], oracle_se[idx_z1]])
160	
161	        tau_obs = np.array([zhat_cate[idx_z0], zhat_cate[idx_z1]])
162	        se_obs = np.array([zhat_se[idx_z0], zhat_se[idx_z1]])
163	
164	        tau_ec_true, se_ec_true = invert_mixing(M_true_sub[s], tau_obs, se_obs)
165	        tau_ec_est, se_ec_est = invert_mixing(M_est_sub[s], tau_obs, se_obs)
166	        tau_gl_true, se_gl_true = invert_mixing(M_global_true, tau_obs, se_obs)
167	        tau_gl_est, se_gl_est = invert_mixing(M_global_est, tau_obs, se_obs)
168	
169	        methods = [
170	            ('Oracle', o_tau, o_se),
171	            ('EC-HTE true CM', tau_ec_true, se_ec_true),
172	            ('EC-HTE estimated CM', tau_ec_est, se_ec_est),
173	            ('Global true CM', tau_gl_true, se_gl_true),
174	            ('Global estimated CM', tau_gl_est, se_gl_est),
175	            ('Naive', tau_obs, se_obs),
176	        ]
177	
178	        for method_name, tau_hat, se_hat in methods:
179	            for zi, z in enumerate([0, 1]):
180	                th = tau_hat[zi]
181	                se = se_hat[zi]
182	                if np.isnan(se) or np.isnan(th):
183	                    covers = np.nan
184	                else:
185	                    ci_lo = th - 1.96 * se
186	                    ci_hi = th + 1.96 * se
187	                    covers = int(ci_lo <= TAU_TRUE[z] <= ci_hi)
188	                rows.append({
189	                    'method': method_name,
190	                    'subgroup': s,
191	                    'z': z,
192	                    'tau_hat': th,
193	                    'se': se,
194	                    'tau_true': TAU_TRUE[z],
195	                    'covers': covers,
196	                    'mc_run': seed,
197	                })
198	
199	    return rows
200	
201	
202	def aggregate_results(df):
203	    grp_cols = ['method', 'subgroup', 'z']
204	    rows = []
205	    for keys, g in df.groupby(grp_cols):
206	        method, subgroup, z = keys
207	        err = g['tau_hat'].values - g['tau_true'].values
208	        bias = err.mean()
209	        rmse = np.sqrt((err ** 2).mean())
210	        cov = g['covers'].mean()
211	        se_mean = g['se'].mean()
212	        n_mc = len(g)
213	        rows.append({
214	            'method': method,
215	            'subgroup': int(subgroup),
216	            'z': int(z),
217	            'bias': bias,
218	            'rmse': rmse,
219	            'coverage': cov,
220	            'se_mean': se_mean,
221	            'mc_run_count': n_mc,
222	        })
223	    return pd.DataFrame(rows)
224	
225	
226	def print_summary(df_agg):
227	    method_order = [
228	        'Oracle', 'EC-HTE true CM', 'EC-HTE estimated CM',
229	        'Global true CM', 'Global estimated CM', 'Naive',
230	    ]
231	
232	    print("\n" + "=" * 80)
233	    print("exp-027b CausalForest Oracle Coverage (K=2, extreme)")
234	    print("=" * 80)
235	
236	    print(f"\n{'Method':<28s} | {'|Bias|':>7s} | {'RMSE':>7s} | {'Coverage':>8s} | {'Mean SE':>7s}")
237	    print(f"{'-'*28}-+-{'-'*7}-+-{'-'*7}-+-{'-'*8}-+-{'-'*7}")
238	
239	    for method in method_order:
240	        sub = df_agg[df_agg['method'] == method]
241	        abs_bias = sub['bias'].abs().mean()
242	        rmse = sub['rmse'].mean()
243	        cov = sub['coverage'].mean()
244	        se_mean = sub['se_mean'].mean()
245	        print(f"{method:<28s} | {abs_bias:7.4f} | {rmse:7.4f} | {cov:8.4f} | {se_mean:7.4f}")
246	
247	    print(f"\n\nPer-subgroup detail:")
248	    print(f"{'Method':<28s} | {'Sub':>3s} | {'z':>1s} | {'Bias':>8s} | {'RMSE':>7s} | {'Coverage':>8s} | {'Mean SE':>7s}")
249	    print(f"{'-'*28}-+-{'-'*3}-+-{'-'*1}-+-{'-'*8}-+-{'-'*7}-+-{'-'*8}-+-{'-'*7}")
250	
251	    for method in method_order:
252	        for s in range(K):
253	            for z in [0, 1]:
254	                r = df_agg[(df_agg['method'] == method) &
255	                           (df_agg['subgroup'] == s) &
256	                           (df_agg['z'] == z)]
257	                if r.empty:
258	                    continue
259	                r = r.iloc[0]
260	                print(f"{method:<28s} | {s:>3d} | {z:>1d} | {r['bias']:8.4f} | {r['rmse']:7.4f} | {r['coverage']:8.4f} | {r['se_mean']:7.4f}")
261	        print()
262	
263	    print("\n" + "=" * 80)
264	    print("INTERPRETATION")
265	    print("=" * 80)
266	    oracle_cov = df_agg[df_agg['method'] == 'Oracle']['coverage'].mean()
267	    ec_true_cov = df_agg[df_agg['method'] == 'EC-HTE true CM']['coverage'].mean()
268	    ec_est_cov = df_agg[df_agg['method'] == 'EC-HTE estimated CM']['coverage'].mean()
269	    print(f"  Oracle coverage:           {oracle_cov:.4f}")
270	    print(f"  EC-HTE true CM coverage:   {ec_true_cov:.4f}")
271	    print(f"  EC-HTE estimated coverage: {ec_est_cov:.4f}")
272	    print()
273	    if oracle_cov < 0.90:
274	        print("  -> Oracle < 90%: CF SE is inherently under-calibrated")
275	    else:
276	        print("  -> Oracle >= 90%: CF SE is reasonably calibrated")
277	    if abs(ec_true_cov - ec_est_cov) < 0.03:
278	        print("  -> EC-HTE true CM ~ estimated CM: gap is NOT from CM estimation error")
279	        print("     Coverage gap comes from CF inherent SE under-calibration")
280	    elif ec_true_cov > ec_est_cov + 0.05:
281	        print("  -> EC-HTE true CM >> estimated CM: CM estimation error contributes to gap")
282	    else:
283	        print("  -> Mixed signal: both CF SE calibration and CM estimation may contribute")
284	
285	
286	if __name__ == '__main__':
287	    print(f"exp-027b CausalForest Oracle Coverage (K=2, extreme)")
288	    print(f"N={N}, K={K}, pi={PI}, weights={SUB_WEIGHTS}")
289	    print(f"tau(0)={TAU_TRUE[0]}, tau(1)={TAU_TRUE[1]}")
290	    print(f"n_expert={N_EXPERT}, N_MC={N_MC}, seed_base={BASE_SEED}")
291	
292	    print("\nTiming single run...")
293	    t_test = time.time()
294	    _ = run_one_mc(seed=9999)
295	    t_per = time.time() - t_test
296	    print(f"  {t_per:.2f}s/run (2 forest fits per run)")
297	    print(f"  Estimated total: {t_per * N_MC:.0f}s ({t_per * N_MC / 60:.1f} min)\n")
298	
299	    all_rows = []
300	    t0 = time.time()
301	
302	    for mc in range(N_MC):
303	        seed = BASE_SEED + mc
304	        try:
305	            rows = run_one_mc(seed)
306	            all_rows.extend(rows)
307	        except Exception as e:
308	            print(f"  WARN: mc={mc} seed={seed} failed: {e}")
309	
310	        if (mc + 1) % 10 == 0:
311	            el = time.time() - t0
312	            eta = el / (mc + 1) * (N_MC - mc - 1)
313	            print(f"  [{mc+1}/{N_MC}] {el:.0f}s elapsed, ETA {eta:.0f}s")
314	
315	    elapsed = time.time() - t0
316	    print(f"\nDone: {elapsed:.1f}s ({N_MC} runs, {elapsed/N_MC:.1f}s/run)")
317	
318	    df_raw = pd.DataFrame(all_rows)
319	    df_agg = aggregate_results(df_raw)
320	
321	    os.makedirs('results', exist_ok=True)
322	    df_agg.to_csv('results/exp_cf_oracle_coverage_k2.csv', index=False)
323	    print(f"Saved: results/exp_cf_oracle_coverage_k2.csv ({len(df_agg)} rows)")
324	
325	    print_summary(df_agg)
326	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "d7828eb5-827a-4278-bfa7-972abf8614ed"
}
```

</details>

---

### System

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8238e369993613e3",
  "tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "description": "Reading exp027_cf_oracle_coverage.py",
  "usage": {
    "total_tokens": 32876,
    "tool_uses": 5,
    "duration_ms": 9025
  },
  "last_tool_name": "Read",
  "uuid": "2c7d4b11-7a06-4fc0-8caa-3ea0f01e5e18",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a"
}
```

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01WKH6RDRFX1hVdbSPzn2b3y`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp027_cf_oracle_coverage.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "b16421a9-c571-430d-92ae-cc5e7bf9eb0f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y1yd7AhepLcaNeWJZDMNdM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10542,
      "cache_read_input_tokens": 22309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10542,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T16:15:37.446Z_

<details><summary>↩ Tool result · `toolu_01WKH6RDRFX1hVdbSPzn2b3y`</summary>

```text
1	#!/usr/bin/env python3
2	"""exp027_cf_oracle_coverage.py — CausalForest Oracle Coverage experiment (exp-027)
3	
4	Isolates source of CausalForest coverage gap (83-85% vs nominal 95%):
5	  CM estimation error vs CF inherent SE calibration.
6	
7	Six methods compared:
8	  1. Oracle (true Z): CausalForestDML with Z_true, no correction
9	  2. EC-HTE true CM: Z_hat forest + per-subgroup correction with true C_s
10	  3. EC-HTE estimated CM: Z_hat forest + per-subgroup correction with estimated C_s (HB)
11	  4. Global true CM: Z_hat forest + global correction with true C_bar
12	  5. Global estimated CM: Z_hat forest + global correction with estimated C_bar
13	  6. Naive: Z_hat forest, no correction
14	
15	DGP: K=4, pi=[0.05,0.10,0.20,0.30], tau(0)=0, tau(1)=0.3, N=5000, n_expert=500
16	Output: results/exp_cf_oracle_coverage.csv
17	"""
18	
19	import os
20	import time
21	import warnings
22	
23	import numpy as np
24	import pandas as pd
25	from econml.dml import CausalForestDML
26	from sklearn.linear_model import LinearRegression, LogisticRegression
27	
28	warnings.filterwarnings('ignore')
29	
30	N = 5000
31	K = 4
32	N_EXPERT = 500
33	PI = [0.05, 0.10, 0.20, 0.30]
34	TAU_TRUE = {0: 0.0, 1: 0.3}
35	SUB_WEIGHTS = [0.25, 0.25, 0.25, 0.25]
36	N_MC = 100
37	BASE_SEED = 42
38	
39	
40	def generate_data(seed):
41	    rng = np.random.RandomState(seed)
42	    S = rng.randint(0, K, N)
43	    T = rng.binomial(1, 0.5, N)
44	    Z_true = rng.binomial(1, 0.5, N)
45	
46	    Z_hat = Z_true.copy()
47	    for s in range(K):
48	        mask_s = S == s
49	        flip = rng.binomial(1, PI[s], mask_s.sum())
50	        Z_hat[mask_s] = np.where(flip, 1 - Z_true[mask_s], Z_true[mask_s])
51	
52	    tau = np.where(Z_true == 1, TAU_TRUE[1], TAU_TRUE[0])
53	    baseline = 1.0 + 0.5 * Z_true
54	    Y = baseline + tau * T + rng.normal(0, 1, N)
55	
56	    expert_idx = rng.choice(N, N_EXPERT, replace=False)
57	    expert_mask = np.zeros(N, dtype=bool)
58	    expert_mask[expert_idx] = True
59	
60	    return Y, T, Z_true, Z_hat, S, expert_mask
61	
62	
63	def compute_confusion_matrix(z_true, z_hat):
64	    C = np.zeros((2, 2))
65	    for z in [0, 1]:
66	        mz = z_true == z
67	        C[z, 0] = (z_hat[mz] == 0).sum() + 1
68	        C[z, 1] = (z_hat[mz] == 1).sum() + 1
69	    return C / C.sum(axis=1, keepdims=True)
70	
71	
72	def build_mixing_matrix(C):
73	    M = np.zeros((2, 2))
74	    for zh in [0, 1]:
75	        cs = C[0, zh] + C[1, zh]
76	        if cs > 0:
77	            M[zh, 0] = C[0, zh] / cs
78	            M[zh, 1] = C[1, zh] / cs
79	        else:
80	            M[zh, :] = 0.5
81	    return M
82	
83	
84	def invert_mixing(M, tau_obs, se_obs, cond_threshold=100):
85	    cond = np.linalg.cond(M)
86	    if cond > cond_threshold or abs(np.linalg.det(M)) < 1e-10:
87	        return tau_obs.copy(), se_obs.copy()
88	    Mi = np.linalg.inv(M)
89	    tau_c = Mi @ tau_obs
90	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
91	    return tau_c, se_c
92	
93	
94	def true_confusion_matrix(pi_s):
95	    return np.array([[1 - pi_s, pi_s],
96	                     [pi_s, 1 - pi_s]])
97	
98	
99	def fit_cf_and_predict(Y, T, X_features, X_eval):
100	    cf = CausalForestDML(
101	        model_y=LinearRegression(),
102	        model_t=LogisticRegression(solver='lbfgs'),
103	        discrete_treatment=True,
104	        n_estimators=200,
105	        min_samples_leaf=20,
106	        random_state=42,
107	    )
108	    cf.fit(Y, T, X=X_features, W=None)
109	
110	    cate_vals = cf.effect(X_eval).flatten()
111	    try:
112	        inf = cf.effect_inference(X_eval)
113	        se_raw = inf.stderr
114	        if hasattr(se_raw, 'values'):
115	            se_raw = se_raw.values
116	        se_vals = np.asarray(se_raw).flatten()
117	    except Exception:
118	        se_vals = np.full(len(X_eval), np.nan)
119	
120	    return cate_vals, se_vals
121	
122	
123	def run_one_mc(seed):
124	    Y, T, Z_true, Z_hat, S, expert_mask = generate_data(seed)
125	
126	    X_eval = np.array([[z, s] for s in range(K) for z in [0, 1]], dtype=float)
127	
128	    # Oracle forest: fit with true Z
129	    X_oracle = np.column_stack([Z_true, S]).astype(float)
130	    oracle_cate, oracle_se = fit_cf_and_predict(Y, T, X_oracle, X_eval)
131	
132	    # Z_hat forest: fit with misclassified Z (shared by methods 2-6)
133	    X_zhat = np.column_stack([Z_hat, S]).astype(float)
134	    zhat_cate, zhat_se = fit_cf_and_predict(Y, T, X_zhat, X_eval)
135	
136	    # True CMs from DGP parameters
137	    M_true_sub = {}
138	    for s in range(K):
139	        C_s_true = true_confusion_matrix(PI[s])
140	        M_true_sub[s] = build_mixing_matrix(C_s_true)
141	
142	    C_global_true = sum(SUB_WEIGHTS[s] * true_confusion_matrix(PI[s]) for s in range(K))
143	    M_global_true = build_mixing_matrix(C_global_true)
144	
145	    # Estimated CMs from expert labels
146	    M_est_sub = {}
147	    for s in range(K):
148	        mask_s = expert_mask & (S == s)
149	        if mask_s.sum() >= 4:
150	            C_s = compute_confusion_matrix(Z_true[mask_s], Z_hat[mask_s])
151	        else:
152	            C_s = np.array([[0.5, 0.5], [0.5, 0.5]])
153	        M_est_sub[s] = build_mixing_matrix(C_s)
154	
155	    C_global_est = compute_confusion_matrix(Z_true[expert_mask], Z_hat[expert_mask])
156	    M_global_est = build_mixing_matrix(C_global_est)
157	
158	    rows = []
159	    for s in range(K):
160	        idx_z0 = s * 2
161	        idx_z1 = s * 2 + 1
162	
163	        o_tau = np.array([oracle_cate[idx_z0], oracle_cate[idx_z1]])
164	        o_se = np.array([oracle_se[idx_z0], oracle_se[idx_z1]])
165	
166	        tau_obs = np.array([zhat_cate[idx_z0], zhat_cate[idx_z1]])
167	        se_obs = np.array([zhat_se[idx_z0], zhat_se[idx_z1]])
168	
169	        tau_ec_true, se_ec_true = invert_mixing(M_true_sub[s], tau_obs, se_obs)
170	        tau_ec_est, se_ec_est = invert_mixing(M_est_sub[s], tau_obs, se_obs)
171	        tau_gl_true, se_gl_true = invert_mixing(M_global_true, tau_obs, se_obs)
172	        tau_gl_est, se_gl_est = invert_mixing(M_global_est, tau_obs, se_obs)
173	
174	        methods = [
175	            ('Oracle', o_tau, o_se),
176	            ('EC-HTE true CM', tau_ec_true, se_ec_true),
177	            ('EC-HTE estimated CM', tau_ec_est, se_ec_est),
178	            ('Global true CM', tau_gl_true, se_gl_true),
179	            ('Global estimated CM', tau_gl_est, se_gl_est),
180	            ('Naive', tau_obs, se_obs),
181	        ]
182	
183	        for method_name, tau_hat, se_hat in methods:
184	            for zi, z in enumerate([0, 1]):
185	                th = tau_hat[zi]
186	                se = se_hat[zi]
187	                if np.isnan(se) or np.isnan(th):
188	                    covers = np.nan
189	                else:
190	                    ci_lo = th - 1.96 * se
191	                    ci_hi = th + 1.96 * se
192	                    covers = int(ci_lo <= TAU_TRUE[z] <= ci_hi)
193	                rows.append({
194	                    'method': method_name,
195	                    'subgroup': s,
196	                    'z': z,
197	                    'tau_hat': th,
198	                    'se': se,
199	                    'tau_true': TAU_TRUE[z],
200	                    'covers': covers,
201	                    'mc_run': seed,
202	                })
203	
204	    return rows
205	
206	
207	def aggregate_results(df):
208	    grp_cols = ['method', 'subgroup', 'z']
209	    rows = []
210	    for keys, g in df.groupby(grp_cols):
211	        method, subgroup, z = keys
212	        err = g['tau_hat'].values - g['tau_true'].values
213	        bias = err.mean()
214	        rmse = np.sqrt((err ** 2).mean())
215	        cov = g['covers'].mean()
216	        se_mean = g['se'].mean()
217	        n_mc = len(g)
218	        rows.append({
219	            'method': method,
220	            'subgroup': int(subgroup),
221	            'z': int(z),
222	            'bias': bias,
223	            'rmse': rmse,
224	            'coverage': cov,
225	            'se_mean': se_mean,
226	            'mc_run_count': n_mc,
227	        })
228	    return pd.DataFrame(rows)
229	
230	
231	def print_summary(df_agg):
232	    method_order = [
233	        'Oracle', 'EC-HTE true CM', 'EC-HTE estimated CM',
234	        'Global true CM', 'Global estimated CM', 'Naive',
235	    ]
236	
237	    print("\n" + "=" * 80)
238	    print("exp-027 CausalForest Oracle Coverage")
239	    print("=" * 80)
240	
241	    print(f"\n{'Method':<28s} | {'|Bias|':>7s} | {'RMSE':>7s} | {'Coverage':>8s} | {'Mean SE':>7s}")
242	    print(f"{'-'*28}-+-{'-'*7}-+-{'-'*7}-+-{'-'*8}-+-{'-'*7}")
243	
244	    for method in method_order:
245	        sub = df_agg[df_agg['method'] == method]
246	        abs_bias = sub['bias'].abs().mean()
247	        rmse = sub['rmse'].mean()
248	        cov = sub['coverage'].mean()
249	        se_mean = sub['se_mean'].mean()
250	        print(f"{method:<28s} | {abs_bias:7.4f} | {rmse:7.4f} | {cov:8.4f} | {se_mean:7.4f}")
251	
252	    print(f"\n\nPer-subgroup detail:")
253	    print(f"{'Method':<28s} | {'Sub':>3s} | {'z':>1s} | {'Bias':>8s} | {'RMSE':>7s} | {'Coverage':>8s} | {'Mean SE':>7s}")
254	    print(f"{'-'*28}-+-{'-'*3}-+-{'-'*1}-+-{'-'*8}-+-{'-'*7}-+-{'-'*8}-+-{'-'*7}")
255	
256	    for method in method_order:
257	        for s in range(K):
258	            for z in [0, 1]:
259	                r = df_agg[(df_agg['method'] == method) &
260	                           (df_agg['subgroup'] == s) &
261	                           (df_agg['z'] == z)]
262	                if r.empty:
263	                    continue
264	                r = r.iloc[0]
265	                print(f"{method:<28s} | {s:>3d} | {z:>1d} | {r['bias']:8.4f} | {r['rmse']:7.4f} | {r['coverage']:8.4f} | {r['se_mean']:7.4f}")
266	        print()
267	
268	    print("\n" + "=" * 80)
269	    print("INTERPRETATION")
270	    print("=" * 80)
271	    oracle_cov = df_agg[df_agg['method'] == 'Oracle']['coverage'].mean()
272	    ec_true_cov = df_agg[df_agg['method'] == 'EC-HTE true CM']['coverage'].mean()
273	    ec_est_cov = df_agg[df_agg['method'] == 'EC-HTE estimated CM']['coverage'].mean()
274	    print(f"  Oracle coverage:           {oracle_cov:.4f}")
275	    print(f"  EC-HTE true CM coverage:   {ec_true_cov:.4f}")
276	    print(f"  EC-HTE estimated coverage: {ec_est_cov:.4f}")
277	    print()
278	    if oracle_cov < 0.90:
279	        print("  -> Oracle < 90%: CF SE is inherently under-calibrated")
280	    else:
281	        print("  -> Oracle >= 90%: CF SE is reasonably calibrated")
282	    if abs(ec_true_cov - ec_est_cov) < 0.03:
283	        print("  -> EC-HTE true CM ~ estimated CM: gap is NOT from CM estimation error")
284	        print("     Coverage gap comes from CF inherent SE under-calibration")
285	    elif ec_true_cov > ec_est_cov + 0.05:
286	        print("  -> EC-HTE true CM >> estimated CM: CM estimation error contributes to gap")
287	    else:
288	        print("  -> Mixed signal: both CF SE calibration and CM estimation may contribute")
289	
290	
291	if __name__ == '__main__':
292	    print(f"exp-027 CausalForest Oracle Coverage")
293	    print(f"N={N}, K={K}, pi={PI}, tau(0)={TAU_TRUE[0]}, tau(1)={TAU_TRUE[1]}")
294	    print(f"n_expert={N_EXPERT}, N_MC={N_MC}, seed_base={BASE_SEED}")
295	
296	    print("\nTiming single run...")
297	    t_test = time.time()
298	    _ = run_one_mc(seed=9999)
299	    t_per = time.time() - t_test
300	    print(f"  {t_per:.2f}s/run (2 forest fits per run)")
301	    print(f"  Estimated total: {t_per * N_MC:.0f}s ({t_per * N_MC / 60:.1f} min)\n")
302	
303	    all_rows = []
304	    t0 = time.time()
305	
306	    for mc in range(N_MC):
307	        seed = BASE_SEED + mc
308	        try:
309	            rows = run_one_mc(seed)
310	            all_rows.extend(rows)
311	        except Exception as e:
312	            print(f"  WARN: mc={mc} seed={seed} failed: {e}")
313	
314	        if (mc + 1) % 10 == 0:
315	            el = time.time() - t0
316	            eta = el / (mc + 1) * (N_MC - mc - 1)
317	            print(f"  [{mc+1}/{N_MC}] {el:.0f}s elapsed, ETA {eta:.0f}s")
318	
319	    elapsed = time.time() - t0
320	    print(f"\nDone: {elapsed:.1f}s ({N_MC} runs, {elapsed/N_MC:.1f}s/run)")
321	
322	    df_raw = pd.DataFrame(all_rows)
323	    df_agg = aggregate_results(df_raw)
324	
325	    os.makedirs('results', exist_ok=True)
326	    df_agg.to_csv('results/exp_cf_oracle_coverage.csv', index=False)
327	    print(f"Saved: results/exp_cf_oracle_coverage.csv ({len(df_agg)} rows)")
328	
329	    print_summary(df_agg)
330	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "601b9b39-3a39-4435-827f-b4a29e9abfe1"
}
```

</details>

---

### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8238e369993613e3",
  "tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "description": "Reading exp027c_cf_oracle_mf2dgp.py",
  "usage": {
    "total_tokens": 32880,
    "tool_uses": 6,
    "duration_ms": 9266
  },
  "last_tool_name": "Read",
  "uuid": "eb4bfd20-efdd-4482-8baa-23efb9bf8a44",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_0183Fwcud2mfJKMhuEJfrcCT`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp027c_cf_oracle_mf2dgp.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "3b74ffee-05c5-4bad-95e3-baae9f45b06d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y1yd7AhepLcaNeWJZDMNdM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10542,
      "cache_read_input_tokens": 22309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10542,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-22T16:15:37.686Z_

<details><summary>↩ Tool result · `toolu_0183Fwcud2mfJKMhuEJfrcCT`</summary>

```text
1	#!/usr/bin/env python3
2	"""exp027c_cf_oracle_mf2dgp.py — CausalForest Oracle Coverage under MF2 DGP (exp-027c)
3	
4	Replicates the exact DGP from exp_mf2_cf_bootstrap_se.py and runs 6 methods:
5	  1. Oracle (true Z): CausalForestDML with Z_true
6	  2. EC-HTE true CM: Z_hat forest + per-subgroup correction with true C_s
7	  3. EC-HTE estimated CM (HB): Z_hat forest + per-subgroup correction with estimated C_s
8	  4. Global true CM: Z_hat forest + global correction with true C_bar
9	  5. Global estimated CM: Z_hat forest + global correction with estimated C_bar
10	  6. Naive: Z_hat forest, no correction
11	
12	DGP (matching MF2 exactly):
13	  K=2, π=[0.05, 0.25], τ(z=0)=0.10, τ(z=1)=0.40
14	  N=5000, n_expert=250, X∈R^5
15	  Y = 1.0 + τ(Z)*T + 0.5*X₀ + ε, ε~N(0,1)
16	"""
17	
18	import os
19	import time
20	import warnings
21	
22	import numpy as np
23	import pandas as pd
24	from econml.dml import CausalForestDML
25	from sklearn.linear_model import LinearRegression, LogisticRegression
26	
27	warnings.filterwarnings('ignore')
28	
29	# ── MF2 DGP Parameters (exact copy) ──
30	N = 5000
31	K = 2
32	N_EXPERT = 250
33	MISCLASS = [0.05, 0.25]
34	TAU_Z0 = 0.10
35	TAU_Z1 = 0.40
36	TAU_TRUE = np.array([TAU_Z0, TAU_Z1])
37	SUB_WEIGHTS = [0.5, 0.5]
38	N_MC = 100
39	BASE_SEED = 42
40	
41	
42	def generate_data(seed):
43	    """MF2-identical data generation (same RNG draw order)."""
44	    rng = np.random.RandomState(seed)
45	    T = rng.binomial(1, 0.5, N)
46	    Z = rng.binomial(1, 0.5, N)
47	    S = rng.choice(K, N, p=SUB_WEIGHTS)
48	    X = rng.randn(N, 5)
49	    tau = np.where(Z == 1, TAU_Z1, TAU_Z0)
50	    Y = 1.0 + tau * T + 0.5 * X[:, 0] + rng.randn(N)
51	
52	    mc_rates = np.where(S == 0, MISCLASS[0], MISCLASS[1])
53	    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)
54	
55	    idx = rng.choice(N, N_EXPERT, replace=False)
56	    expert_mask = np.zeros(N, dtype=bool)
57	    expert_mask[idx] = True
58	
59	    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, expert_mask=expert_mask)
60	
61	
62	def estimate_cm(z_true, z_hat):
63	    """MF2-identical CM estimation with Laplace smoothing."""
64	    C = np.zeros((2, 2))
65	    for z in [0, 1]:
66	        mask = z_true == z
67	        n = mask.sum()
68	        for zh in [0, 1]:
69	            C[z, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
70	    return C
71	
72	
73	def build_mixing_matrix(C):
74	    M = np.zeros((2, 2))
75	    for zh in [0, 1]:
76	        cs = C[0, zh] + C[1, zh]
77	        M[zh, 0] = C[0, zh] / cs if cs > 0 else 0.5
78	        M[zh, 1] = C[1, zh] / cs if cs > 0 else 0.5
79	    return M
80	
81	
82	def invert_mixing(M, tau_obs, se_obs):
83	    if np.linalg.cond(M) > 100 or abs(np.linalg.det(M)) < 1e-10:
84	        return tau_obs.copy(), se_obs.copy()
85	    Mi = np.linalg.inv(M)
86	    tau_c = Mi @ tau_obs
87	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
88	    return tau_c, se_c
89	
90	
91	def true_confusion_matrix(pi_s):
92	    return np.array([[1 - pi_s, pi_s],
93	                     [pi_s, 1 - pi_s]])
94	
95	
96	def fit_cf(Y, T, X_features, seed):
97	    """CausalForestDML with MF2-identical hyperparameters."""
98	    cf = CausalForestDML(
99	        model_y=LinearRegression(),
100	        model_t=LogisticRegression(solver='lbfgs'),
101	        discrete_treatment=True,
102	        n_estimators=200,
103	        min_samples_leaf=20,
104	        random_state=seed,
105	    )
106	    cf.fit(Y, T, X=X_features)
107	    return cf
108	
109	
110	def get_subgroup_cates_and_se(cf, X_features, S, Z_col, X):
111	    """Per-(subgroup, z) CATEs and SEs following MF2 approach."""
112	    cate_all = cf.effect(X_features).flatten()
113	
114	    sub_tau = {}
115	    for s in range(K):
116	        sm = S == s
117	        vals = []
118	        for z in [0, 1]:
119	            mask = sm & (Z_col == z)
120	            if mask.sum() == 0:
121	                vals.append(np.nan)
122	            else:
123	                vals.append(cate_all[mask].mean())
124	        sub_tau[s] = np.array(vals)
125	
126	    X_mean = X.mean(axis=0)
127	    X_eval = np.array([
128	        np.concatenate([[0], X_mean]),
129	        np.concatenate([[1], X_mean]),
130	    ])
131	    try:
132	        inf = cf.effect_inference(X_eval)
133	        se_raw = np.asarray(inf.stderr).flatten()
134	        if np.any(np.isnan(se_raw)) or np.any(se_raw <= 0):
135	            se_raw = np.full(2, np.nan)
136	    except Exception:
137	        se_raw = np.full(2, np.nan)
138	
139	    sub_se = {s: se_raw.copy() for s in range(K)}
140	    return sub_tau, sub_se
141	
142	
143	def run_one_mc(seed):
144	    data = generate_data(seed)
145	    Y, T, Z, Z_hat, S, X = (
146	        data['Y'], data['T'], data['Z'], data['Z_hat'], data['S'], data['X']
147	    )
148	    em = data['expert_mask']
149	
150	    # ── Fit two forests ──
151	    X_oracle = np.column_stack([Z, X]).astype(float)
152	    X_zhat = np.column_stack([Z_hat, X]).astype(float)
153	
154	    cf_oracle = fit_cf(Y, T, X_oracle, seed)
155	    cf_zhat = fit_cf(Y, T, X_zhat, seed)
156	
157	    # ── CATEs and SEs ──
158	    oracle_tau, oracle_se = get_subgroup_cates_and_se(cf_oracle, X_oracle, S, Z, X)
159	    zhat_tau, zhat_se = get_subgroup_cates_and_se(cf_zhat, X_zhat, S, Z_hat, X)
160	
161	    # ── Confusion matrices ──
162	    M_true_sub = {}
163	    for s in range(K):
164	        C_s_true = true_confusion_matrix(MISCLASS[s])
165	        M_true_sub[s] = build_mixing_matrix(C_s_true)
166	
167	    C_global_true = sum(SUB_WEIGHTS[s] * true_confusion_matrix(MISCLASS[s])
168	                        for s in range(K))
169	    M_global_true = build_mixing_matrix(C_global_true)
170	
171	    M_est_sub = {}
172	    for s in range(K):
173	        mask_s = em & (S == s)
174	        if mask_s.sum() >= 4:
175	            C_s = estimate_cm(Z[mask_s], Z_hat[mask_s])
176	        else:
177	            C_s = estimate_cm(Z[em], Z_hat[em])
178	        M_est_sub[s] = build_mixing_matrix(C_s)
179	
180	    C_global_est = estimate_cm(Z[em], Z_hat[em])
181	    M_global_est = build_mixing_matrix(C_global_est)
182	
183	    # ── Per-subgroup corrections and coverage ──
184	    rows = []
185	    for s in range(K):
186	        tau_obs = zhat_tau[s]
187	        se_obs = zhat_se[s]
188	
189	        tau_ec_true, se_ec_true = invert_mixing(M_true_sub[s], tau_obs, se_obs)
190	        tau_ec_est, se_ec_est = invert_mixing(M_est_sub[s], tau_obs, se_obs)
191	        tau_gl_true, se_gl_true = invert_mixing(M_global_true, tau_obs, se_obs)
192	        tau_gl_est, se_gl_est = invert_mixing(M_global_est, tau_obs, se_obs)
193	
194	        methods = [
195	            ('Oracle', oracle_tau[s], oracle_se[s]),
196	            ('EC-HTE true CM', tau_ec_true, se_ec_true),
197	            ('EC-HTE estimated CM', tau_ec_est, se_ec_est),
198	            ('Global true CM', tau_gl_true, se_gl_true),
199	            ('Global estimated CM', tau_gl_est, se_gl_est),
200	            ('Naive', tau_obs, se_obs),
201	        ]
202	
203	        for method_name, tau_hat, se_hat in methods:
204	            for zi, z in enumerate([0, 1]):
205	                th = tau_hat[zi]
206	                se = se_hat[zi]
207	                if np.isnan(se) or np.isnan(th):
208	                    covers = np.nan
209	                else:
210	                    ci_lo = th - 1.96 * se
211	                    ci_hi = th + 1.96 * se
212	                    covers = int(ci_lo <= TAU_TRUE[z] <= ci_hi)
213	                rows.append({
214	                    'method': method_name,
215	                    'subgroup': s,
216	                    'z': z,
217	                    'tau_hat': th,
218	                    'se': se,
219	                    'tau_true': TAU_TRUE[z],
220	                    'covers': covers,
221	                    'mc_run': seed,
222	                })
223	
224	    return rows
225	
226	
227	def aggregate_results(df):
228	    grp_cols = ['method', 'subgroup', 'z']
229	    rows = []
230	    for keys, g in df.groupby(grp_cols):
231	        method, subgroup, z = keys
232	        err = g['tau_hat'].values - g['tau_true'].values
233	        bias = err.mean()
234	        rmse = np.sqrt((err ** 2).mean())
235	        cov = g['covers'].mean()
236	        se_mean = g['se'].mean()
237	        n_mc = len(g)
238	        rows.append({
239	            'method': method,
240	            'subgroup': int(subgroup),
241	            'z': int(z),
242	            'bias': bias,
243	            'rmse': rmse,
244	            'coverage': cov,
245	            'se_mean': se_mean,
246	            'mc_run_count': n_mc,
247	        })
248	    return pd.DataFrame(rows)
249	
250	
251	def print_summary(df_agg):
252	    method_order = [
253	        'Oracle', 'EC-HTE true CM', 'EC-HTE estimated CM',
254	        'Global true CM', 'Global estimated CM', 'Naive',
255	    ]
256	
257	    print("\n" + "=" * 80)
258	    print("=== exp-027c: MF2 DGP (τ(0)=0.10, τ(1)=0.40) ===")
259	    print("=" * 80)
260	
261	    print(f"\n{'Method':<28s} | {'Coverage':>8s} | {'|Bias|':>7s} | {'RMSE':>7s} | {'Mean SE':>7s}")
262	    print(f"{'-' * 28}-+-{'-' * 8}-+-{'-' * 7}-+-{'-' * 7}-+-{'-' * 7}")
263	
264	    for method in method_order:
265	        sub = df_agg[df_agg['method'] == method]
266	        cov = sub['coverage'].mean()
267	        abs_bias = sub['bias'].abs().mean()
268	        rmse = sub['rmse'].mean()
269	        se_mean = sub['se_mean'].mean()
270	        print(f"{method:<28s} | {cov:8.4f} | {abs_bias:7.4f} | {rmse:7.4f} | {se_mean:7.4f}")
271	
272	    print(f"\nPer-subgroup detail:")
273	    hdr = (f"{'Method':<28s} | {'Sub':>3s} | {'z':>1s} | "
274	           f"{'Bias':>8s} | {'RMSE':>7s} | {'Coverage':>8s} | {'Mean SE':>7s}")
275	    print(hdr)
276	    print("-" * len(hdr))
277	
278	    for method in method_order:
279	        for s in range(K):
280	            for z in [0, 1]:
281	                r = df_agg[(df_agg['method'] == method) &
282	                           (df_agg['subgroup'] == s) &
283	                           (df_agg['z'] == z)]
284	                if r.empty:
285	                    continue
286	                r = r.iloc[0]
287	                print(f"{method:<28s} | {s:>3d} | {z:>1d} | "
288	                      f"{r['bias']:8.4f} | {r['rmse']:7.4f} | "
289	                      f"{r['coverage']:8.4f} | {r['se_mean']:7.4f}")
290	        print()
291	
292	
293	def print_diagnostics(df_agg):
294	    print("\n" + "=" * 80)
295	    print("DIAGNOSTIC COMPARISON")
296	    print("=" * 80)
297	
298	    oracle_cov_c = df_agg[df_agg['method'] == 'Oracle']['coverage'].mean()
299	    ec_est_cov_c = df_agg[df_agg['method'] == 'EC-HTE estimated CM']['coverage'].mean()
300	
301	    b_path = 'results/exp_cf_oracle_coverage_k2.csv'
302	    if os.path.exists(b_path):
303	        df_b = pd.read_csv(b_path)
304	        oracle_cov_b = df_b[df_b['method'] == 'Oracle']['coverage'].mean()
305	        ec_est_cov_b = df_b[df_b['method'] == 'EC-HTE estimated CM']['coverage'].mean()
306	
307	        print(f"\n1. Oracle coverage:")
308	        print(f"   exp-027b (τ(0)=0.00, τ(1)=0.30): {oracle_cov_b:.4f}")
309	        print(f"   exp-027c (τ(0)=0.10, τ(1)=0.40): {oracle_cov_c:.4f}")
310	
311	        print(f"\n2. EC-HTE estimated CM coverage:")
312	        print(f"   exp-027b (τ(0)=0.00, τ(1)=0.30): {ec_est_cov_b:.4f}")
313	        print(f"   exp-027c (τ(0)=0.10, τ(1)=0.40): {ec_est_cov_c:.4f}")
314	    else:
315	        print(f"\n  exp-027b results not found at {b_path}")
316	        print(f"  exp-027c Oracle coverage: {oracle_cov_c:.4f}")
317	        print(f"  exp-027c EC-HTE est CM coverage: {ec_est_cov_c:.4f}")
318	
319	    mf2_path = 'results/exp_mf2_cf_bootstrap_se.csv'
320	    if os.path.exists(mf2_path):
321	        df_mf2 = pd.read_csv(mf2_path)
322	        mf2_250 = df_mf2[(df_mf2['n_expert'] == 250) & (df_mf2['se_method'] == 'plugin')]
323	        if not mf2_250.empty:
324	            mf2_cov = mf2_250['coverage_avg'].values[0]
325	            mf2_z0 = mf2_250['coverage_z0'].values[0]
326	            mf2_z1 = mf2_250['coverage_z1'].values[0]
327	            print(f"\n3. MF2 original EC-HTE plugin coverage (n_expert=250):")
328	            print(f"   z0={mf2_z0:.2f}, z1={mf2_z1:.2f}, avg={mf2_cov:.2f}")
329	    else:
330	        print(f"\n3. MF2 results not found")
331	        print(f"   (Reference: MF2 reported EC-HTE plugin coverage ≈ 0.83)")
332	
333	
334	if __name__ == '__main__':
335	    print(f"exp-027c CausalForest Oracle Coverage — MF2 DGP")
336	    print(f"N={N}, K={K}, pi={MISCLASS}, weights={SUB_WEIGHTS}")
337	    print(f"tau(0)={TAU_Z0}, tau(1)={TAU_Z1}")
338	    print(f"n_expert={N_EXPERT}, N_MC={N_MC}, seed_base={BASE_SEED}")
339	    print(f"Y = 1.0 + tau*T + 0.5*X0 + N(0,1)")
340	    print(f"X_features = [Z, X] (6 columns)")
341	
342	    print("\nTiming single run...")
343	    t_test = time.time()
344	    _ = run_one_mc(seed=9999)
345	    t_per = time.time() - t_test
346	    print(f"  {t_per:.2f}s/run (2 forest fits per run)")
347	    print(f"  Estimated total: {t_per * N_MC:.0f}s ({t_per * N_MC / 60:.1f} min)\n")
348	
349	    all_rows = []
350	    t0 = time.time()
351	
352	    for mc in range(N_MC):
353	        seed = BASE_SEED + mc
354	        try:
355	            rows = run_one_mc(seed)
356	            all_rows.extend(rows)
357	        except Exception as e:
358	            print(f"  WARN: mc={mc} seed={seed} failed: {e}")
359	
360	        if (mc + 1) % 10 == 0:
361	            el = time.time() - t0
362	            eta = el / (mc + 1) * (N_MC - mc - 1)
363	            print(f"  [{mc + 1}/{N_MC}] {el:.0f}s elapsed, ETA {eta:.0f}s")
364	
365	    elapsed = time.time() - t0
366	    print(f"\nDone: {elapsed:.1f}s ({N_MC} runs, {elapsed / N_MC:.1f}s/run)")
367	
368	    df_raw = pd.DataFrame(all_rows)
369	    df_agg = aggregate_results(df_raw)
370	
371	    os.makedirs('results', exist_ok=True)
372	    csv_path = 'results/exp_cf_oracle_coverage_mf2dgp.csv'
373	    df_agg.to_csv(csv_path, index=False)
374	    print(f"Saved: {csv_path} ({len(df_agg)} rows)")
375	
376	    print_summary(df_agg)
377	    print_diagnostics(df_agg)
378	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "f41c6120-9e79-4de9-84e7-5389402ece44"
}
```

</details>

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8238e369993613e3",
  "tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "description": "Reading exp_w4_bootstrap_se.py",
  "usage": {
    "total_tokens": 32884,
    "tool_uses": 7,
    "duration_ms": 9510
  },
  "last_tool_name": "Read",
  "uuid": "e8727c1a-7b75-4f09-b5e8-4808aeab4823",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01HtD56oWqwgznxGzZQePfEY`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp_w4_bootstrap_se.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "44dc45a8-a8eb-43c3-b1bf-d467bbcf33dc",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y1yd7AhepLcaNeWJZDMNdM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10542,
      "cache_read_input_tokens": 22309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10542,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T16:15:37.929Z_

<details><summary>↩ Tool result · `toolu_01HtD56oWqwgznxGzZQePfEY`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	exp_w4_bootstrap_se.py — Bootstrap SE vs Plug-in SE Coverage Comparison (W4)
4	
5	Quantifies the coverage gap of plug-in SE (delta method) at small expert budgets,
6	compared to bootstrap SE that accounts for confusion matrix estimation uncertainty.
7	
8	DGP: K=2, π=[0.05, 0.25], τ(z=0)=0.10, τ(z=1)=0.40
9	N=5000, n_expert ∈ {50, 100, 250, 500}, 50 MC runs, 100 bootstrap resamples
10	"""
11	
12	import os
13	import time
14	import numpy as np
15	import pandas as pd
16	
17	N = 5000
18	N_BOOTSTRAP = 100
19	N_MC = 50
20	SEEDS = list(range(42, 42 + N_MC))
21	N_EXPERTS = [50, 100, 250, 500]
22	MISCLASS = [0.05, 0.25]
23	TAU_Z0 = 0.10
24	TAU_Z1 = 0.40
25	LABELS = ['A', 'B']
26	
27	
28	def generate_data(n_expert, seed):
29	    rng = np.random.RandomState(seed)
30	    T = rng.binomial(1, 0.5, N)
31	    Z = rng.binomial(1, 0.5, N)
32	    S = rng.choice(LABELS, N, p=[0.5, 0.5])
33	    X = rng.randn(N, 5)
34	    tau = np.where(Z == 1, TAU_Z1, TAU_Z0)
35	    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)
36	    mc_rates = np.where(S == 'A', MISCLASS[0], MISCLASS[1])
37	    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)
38	    idx = rng.choice(N, min(n_expert, N), replace=False)
39	    expert_mask = np.zeros(N, dtype=bool)
40	    expert_mask[idx] = True
41	    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, Y=Y, expert_mask=expert_mask)
42	
43	
44	def diff_in_means(Y, T, mask):
45	    t1, t0 = mask & (T == 1), mask & (T == 0)
46	    n1, n0 = t1.sum(), t0.sum()
47	    if n1 < 2 or n0 < 2:
48	        return np.nan, np.nan
49	    y1, y0 = Y[t1], Y[t0]
50	    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
51	
52	
53	def estimate_cm(z_true, z_hat):
54	    C = np.zeros((2, 2))
55	    for z in [0, 1]:
56	        mask = z_true == z
57	        n = mask.sum()
58	        for zh in [0, 1]:
59	            C[z, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
60	    return C
61	
62	
63	def build_mixing_matrix(C):
64	    M = np.zeros((2, 2))
65	    for zh in [0, 1]:
66	        cs = C[0, zh] + C[1, zh]
67	        M[zh, 0] = C[0, zh] / cs if cs > 0 else 0.5
68	        M[zh, 1] = C[1, zh] / cs if cs > 0 else 0.5
69	    return M
70	
71	
72	def invert_mixing(M, tau_obs, se_obs):
73	    if np.linalg.cond(M) > 100 or abs(np.linalg.det(M)) < 1e-10:
74	        return tau_obs.copy(), se_obs.copy(), True
75	    Mi = np.linalg.inv(M)
76	    tau_c = Mi @ tau_obs
77	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
78	    return tau_c, se_c, False
79	
80	
81	def run_one_mc(n_expert, seed):
82	    data = generate_data(n_expert, seed)
83	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
84	    em = data['expert_mask']
85	    tau_true = np.array([TAU_Z0, TAU_Z1])
86	
87	    z_exp = Z[em]
88	    zh_exp = Z_hat[em]
89	    s_exp = S[em]
90	    n_exp = em.sum()
91	
92	    sub_obs, sub_se_obs, sub_w = {}, {}, {}
93	    for s in LABELS:
94	        sm = S == s
95	        sub_w[s] = sm.sum() / N
96	        th0, se0 = diff_in_means(Y, T, sm & (Z_hat == 0))
97	        th1, se1 = diff_in_means(Y, T, sm & (Z_hat == 1))
98	        sub_obs[s] = np.array([th0, th1])
99	        sub_se_obs[s] = np.array([se0, se1])
100	
101	    for s in LABELS:
102	        if np.any(np.isnan(sub_obs[s])):
103	            return []
104	
105	    # ── Plug-in path ──
106	    plugin_tau_sub, plugin_se_sub = {}, {}
107	    for s in LABELS:
108	        s_mask_exp = s_exp == s
109	        if s_mask_exp.sum() < 4:
110	            C_s = estimate_cm(z_exp, zh_exp)
111	        else:
112	            C_s = estimate_cm(z_exp[s_mask_exp], zh_exp[s_mask_exp])
113	        M_s = build_mixing_matrix(C_s)
114	        tau_c, se_c, _ = invert_mixing(M_s, sub_obs[s], sub_se_obs[s])
115	        plugin_tau_sub[s] = tau_c
116	        plugin_se_sub[s] = se_c
117	
118	    plugin_tau_marg = sum(sub_w[s] * plugin_tau_sub[s] for s in LABELS)
119	    plugin_se_marg = np.sqrt(sum((sub_w[s] * plugin_se_sub[s]) ** 2 for s in LABELS))
120	
121	    # ── Bootstrap path ──
122	    boot_taus_sub = {s: np.zeros((N_BOOTSTRAP, 2)) for s in LABELS}
123	    boot_taus_marg = np.zeros((N_BOOTSTRAP, 2))
124	    rng_boot = np.random.RandomState(seed * 1000 + 7)
125	
126	    for b in range(N_BOOTSTRAP):
127	        boot_idx = rng_boot.choice(n_exp, n_exp, replace=True)
128	        z_b, zh_b, s_b = z_exp[boot_idx], zh_exp[boot_idx], s_exp[boot_idx]
129	
130	        b_tau_marg = np.zeros(2)
131	        for s in LABELS:
132	            sm_b = s_b == s
133	            if sm_b.sum() < 4:
134	                C_s_b = estimate_cm(z_b, zh_b)
135	            else:
136	                C_s_b = estimate_cm(z_b[sm_b], zh_b[sm_b])
137	            M_s_b = build_mixing_matrix(C_s_b)
138	            tau_c_b, _, _ = invert_mixing(M_s_b, sub_obs[s], sub_se_obs[s])
139	            boot_taus_sub[s][b] = tau_c_b
140	            b_tau_marg += sub_w[s] * tau_c_b
141	
142	        boot_taus_marg[b] = b_tau_marg
143	
144	    boot_se_sub = {s: np.nanstd(boot_taus_sub[s], axis=0) for s in LABELS}
145	    boot_se_marg = np.nanstd(boot_taus_marg, axis=0)
146	
147	    # ── Collect results ──
148	    rows = []
149	
150	    def add_result(level, tau_hat, plugin_se, bootstrap_se):
151	        combined_se = np.sqrt(plugin_se ** 2 + bootstrap_se ** 2)
152	        for z_idx in [0, 1]:
153	            z_label = f'z{z_idx}'
154	            pi_lo = tau_hat[z_idx] - 1.96 * plugin_se[z_idx]
155	            pi_hi = tau_hat[z_idx] + 1.96 * plugin_se[z_idx]
156	            bs_lo = tau_hat[z_idx] - 1.96 * bootstrap_se[z_idx]
157	            bs_hi = tau_hat[z_idx] + 1.96 * bootstrap_se[z_idx]
158	            cb_lo = tau_hat[z_idx] - 1.96 * combined_se[z_idx]
159	            cb_hi = tau_hat[z_idx] + 1.96 * combined_se[z_idx]
160	            rows.append({
161	                'n_expert': n_expert, 'seed': seed, 'level': level, 'z': z_label,
162	                'tau_hat': tau_hat[z_idx], 'tau_true': tau_true[z_idx],
163	                'plugin_se': plugin_se[z_idx],
164	                'bootstrap_se': bootstrap_se[z_idx],
165	                'combined_se': combined_se[z_idx],
166	                'plugin_covers': int(pi_lo <= tau_true[z_idx] <= pi_hi),
167	                'bootstrap_covers': int(bs_lo <= tau_true[z_idx] <= bs_hi),
168	                'combined_covers': int(cb_lo <= tau_true[z_idx] <= cb_hi),
169	            })
170	
171	    add_result('marginal', plugin_tau_marg, plugin_se_marg, boot_se_marg)
172	    for s in LABELS:
173	        add_result(f'subgroup_{s}', plugin_tau_sub[s], plugin_se_sub[s], boot_se_sub[s])
174	
175	    return rows
176	
177	
178	def aggregate(df):
179	    agg_rows = []
180	    for (ne, level), grp in df.groupby(['n_expert', 'level']):
181	        row = {'n_expert': int(ne), 'level': level}
182	        for z in ['z0', 'z1']:
183	            zg = grp[grp['z'] == z]
184	            row[f'plugin_cov_{z}'] = zg['plugin_covers'].mean()
185	            row[f'boot_cov_{z}'] = zg['bootstrap_covers'].mean()
186	            row[f'combined_cov_{z}'] = zg['combined_covers'].mean()
187	            row[f'plugin_se_{z}'] = zg['plugin_se'].mean()
188	            row[f'boot_se_{z}'] = zg['bootstrap_se'].mean()
189	            row[f'combined_se_{z}'] = zg['combined_se'].mean()
190	            err = zg['tau_hat'].values - zg['tau_true'].values
191	            row[f'bias_{z}'] = err.mean()
192	            row[f'rmse_{z}'] = np.sqrt((err ** 2).mean())
193	        row['plugin_cov'] = (row['plugin_cov_z0'] + row['plugin_cov_z1']) / 2
194	        row['boot_cov'] = (row['boot_cov_z0'] + row['boot_cov_z1']) / 2
195	        row['combined_cov'] = (row['combined_cov_z0'] + row['combined_cov_z1']) / 2
196	        row['plugin_se_avg'] = (row['plugin_se_z0'] + row['plugin_se_z1']) / 2
197	        row['boot_se_avg'] = (row['boot_se_z0'] + row['boot_se_z1']) / 2
198	        row['combined_se_avg'] = (row['combined_se_z0'] + row['combined_se_z1']) / 2
199	        row['abs_bias'] = (abs(row['bias_z0']) + abs(row['bias_z1'])) / 2
200	        row['rmse'] = (row['rmse_z0'] + row['rmse_z1']) / 2
201	        agg_rows.append(row)
202	    return pd.DataFrame(agg_rows)
203	
204	
205	def main():
206	    print(f"W4: Bootstrap SE vs Plug-in SE Coverage")
207	    print(f"N={N}, n_expert={N_EXPERTS}, N_MC={N_MC}, N_boot={N_BOOTSTRAP}")
208	    print(f"DGP: K=2, pi={MISCLASS}, tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}\n")
209	
210	    all_rows = []
211	    total = len(N_EXPERTS) * N_MC
212	    count = 0
213	    t0 = time.time()
214	
215	    for ne in N_EXPERTS:
216	        for seed in SEEDS:
217	            rows = run_one_mc(ne, seed)
218	            all_rows.extend(rows)
219	            count += 1
220	            if count % max(1, total // 10) == 0:
221	                el = time.time() - t0
222	                eta = el / count * (total - count)
223	                print(f"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s")
224	
225	    elapsed = time.time() - t0
226	    print(f"\nDone in {elapsed:.1f}s\n")
227	
228	    df = pd.DataFrame(all_rows)
229	    df_agg = aggregate(df)
230	
231	    # ── Marginal table ──
232	    print("=" * 100)
233	    print("MARGINAL (EC-HTE stratified)")
234	    print("=" * 100)
235	    marg = df_agg[df_agg['level'] == 'marginal'].sort_values('n_expert')
236	    header = f"{'n_exp':>5} | {'Plug Cov':>8} {'Boot Cov':>8} {'Comb Cov':>8} | {'Plug SE':>8} {'Boot SE':>8} {'Comb SE':>8} | {'|bias|':>7} {'RMSE':>7}"
237	    print(header)
238	    print("-" * len(header))
239	    for _, r in marg.iterrows():
240	        print(f"{int(r['n_expert']):5d} | {r['plugin_cov']:8.3f} {r['boot_cov']:8.3f} {r['combined_cov']:8.3f} | "
241	              f"{r['plugin_se_avg']:8.4f} {r['boot_se_avg']:8.4f} {r['combined_se_avg']:8.4f} | "
242	              f"{r['abs_bias']:7.4f} {r['rmse']:7.4f}")
243	
244	    # ── Per-z breakdown ──
245	    print(f"\n{'=' * 90}")
246	    print("MARGINAL — per Z breakdown")
247	    print(f"{'=' * 90}")
248	    header2 = f"{'n_exp':>5} {'z':>3} | {'Plug Cov':>8} {'Boot Cov':>8} {'Comb Cov':>8} | {'Plug SE':>8} {'Boot SE':>8}"
249	    print(header2)
250	    print("-" * len(header2))
251	    for _, r in marg.iterrows():
252	        for z in ['z0', 'z1']:
253	            print(f"{int(r['n_expert']):5d}  {z:>2} | {r[f'plugin_cov_{z}']:8.3f} {r[f'boot_cov_{z}']:8.3f} {r[f'combined_cov_{z}']:8.3f} | "
254	                  f"{r[f'plugin_se_{z}']:8.4f} {r[f'boot_se_{z}']:8.4f}")
255	
256	    # ── Subgroup table ──
257	    print(f"\n{'=' * 100}")
258	    print("SUBGROUP-LEVEL (averaged over A, B)")
259	    print(f"{'=' * 100}")
260	    sub = df_agg[df_agg['level'].str.startswith('subgroup')].copy()
261	    sub_avg = sub.groupby('n_expert').agg({
262	        'plugin_cov': 'mean', 'boot_cov': 'mean', 'combined_cov': 'mean',
263	        'plugin_se_avg': 'mean', 'boot_se_avg': 'mean', 'combined_se_avg': 'mean',
264	        'abs_bias': 'mean', 'rmse': 'mean',
265	    }).reset_index().sort_values('n_expert')
266	    print(header)
267	    print("-" * len(header))
268	    for _, r in sub_avg.iterrows():
269	        print(f"{int(r['n_expert']):5d} | {r['plugin_cov']:8.3f} {r['boot_cov']:8.3f} {r['combined_cov']:8.3f} | "
270	              f"{r['plugin_se_avg']:8.4f} {r['boot_se_avg']:8.4f} {r['combined_se_avg']:8.4f} | "
271	              f"{r['abs_bias']:7.4f} {r['rmse']:7.4f}")
272	
273	    # ── Save ──
274	    os.makedirs('results', exist_ok=True)
275	    csv_path = 'results/exp_w4_bootstrap_se.csv'
276	    raw_path = 'results/exp_w4_bootstrap_se_raw.csv'
277	    df_agg.to_csv(csv_path, index=False)
278	    df.to_csv(raw_path, index=False)
279	    print(f"\nSaved: {csv_path} ({len(df_agg)} rows)")
280	    print(f"Saved: {raw_path} ({len(df)} rows)")
281	
282	    # ── LaTeX paragraph ──
283	    m50 = marg[marg['n_expert'] == 50].iloc[0]
284	    m500 = marg[marg['n_expert'] == 500].iloc[0]
285	
286	    latex = rf"""\paragraph{{Plug-in vs.\ Bootstrap Standard Errors}}
287	A natural concern is whether the plug-in (delta method) standard errors
288	underestimate uncertainty when the confusion matrix is estimated from a small
289	expert sample. We investigate this via a Monte Carlo study with $K=2$
290	subgroups, heterogeneous misclassification rates $\pi=(0.05, 0.25)$, true
291	CATEs $\tau(z{{=}}0)=0.10$, $\tau(z{{=}}1)=0.40$, and expert budgets
292	$n_{{\text{{expert}}}} \in \{{50, 100, 250, 500\}}$ ({N_MC} replications,
293	{N_BOOTSTRAP} bootstrap resamples each). The plug-in 95\% CI achieves
294	{m50['plugin_cov']:.0%} coverage at $n_{{\text{{expert}}}}=50$ and
295	{m500['plugin_cov']:.0%} at $n_{{\text{{expert}}}}=500$---both at or above the
296	nominal 95\% level. The slight over-coverage at small budgets arises because
297	noisy $\hat{{M}}^{{-1}}$ estimates tend to inflate both the correction error
298	and the propagated SE in tandem, preserving calibration. A bootstrap that
299	resamples only the expert labels captures confusion-matrix estimation
300	uncertainty but misses the dominant outcome-variance component, yielding a
301	standalone coverage of {m50['boot_cov']:.0%}--{m500['boot_cov']:.0%};
302	combining both sources ($\text{{SE}}_{{\text{{combined}}}} =
303	\sqrt{{\text{{SE}}_{{\text{{plugin}}}}^2 + \text{{SE}}_{{\text{{boot}}}}^2}}$)
304	maintains {m50['combined_cov']:.0%}--{m500['combined_cov']:.0%} coverage.
305	These results confirm that the plug-in SE provides adequate inference across
306	the expert budget range considered in our experiments."""
307	
308	    print(f"\n{'=' * 100}")
309	    print("LaTeX paragraph:")
310	    print(f"{'=' * 100}")
311	    print(latex)
312	
313	
314	if __name__ == '__main__':
315	    main()
316	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "38eeeb9e-121a-425d-900d-82886bd828ee"
}
```

</details>

---

### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8238e369993613e3",
  "tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "description": "Reading exp_w8_a5_violation.py",
  "usage": {
    "total_tokens": 50470,
    "tool_uses": 8,
    "duration_ms": 11375
  },
  "last_tool_name": "Read",
  "uuid": "ab3819de-c2eb-4712-99c4-4c7ad912c060",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a"
}
```

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01DUNaLrDNrEyfAZuz7cq4ps`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp_w8_a5_violation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "e08eee5e-a12b-4fdd-b0e4-2acade77b5b2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AsyEREciGnpmGz2TvAYbBv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17580,
      "cache_read_input_tokens": 32851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17580,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-22T16:15:39.796Z_

<details><summary>↩ Tool result · `toolu_01DUNaLrDNrEyfAZuz7cq4ps`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	exp_w8_a5_violation.py — A5 Violation Test: Correlated Δτ and δ (W8)
4	
5	Tests EC-HTE robustness when CATE heterogeneity Δτ_s correlates with
6	misclassification rate δ_s, violating Assumption A5 (independence).
7	
8	Two configs:
9	  aligned:     high-error subgroup has large Δτ  (positive correlation)
10	  adversarial: high-error subgroup has small Δτ  (negative correlation)
11	
12	K=2, N=5000, n_expert ∈ {250, 500}, 50 MC runs, EB estimator.
13	"""
14	
15	import os
16	import time
17	import numpy as np
18	import pandas as pd
19	from scipy.special import gammaln
20	from scipy.optimize import minimize_scalar
21	
22	N = 5000
23	N_MC = 50
24	SEEDS = list(range(42, 42 + N_MC))
25	N_EXPERTS = [250, 500]
26	LABELS = ['S0', 'S1']
27	
28	CONFIGS = {
29	    'aligned': {
30	        'misclass': [0.05, 0.25],
31	        'tau_z0':   [0.10, 0.10],
32	        'tau_z1':   [0.40, 0.80],
33	    },
34	    'adversarial': {
35	        'misclass': [0.05, 0.25],
36	        'tau_z0':   [0.10, 0.10],
37	        'tau_z1':   [0.80, 0.40],
38	    },
39	}
40	
41	
42	def generate_data(config, n_expert, seed):
43	    rng = np.random.RandomState(seed)
44	    T = rng.binomial(1, 0.5, N)
45	    Z = rng.binomial(1, 0.5, N)
46	    S = rng.choice(LABELS, N, p=[0.5, 0.5])
47	    X = rng.randn(N, 5)
48	
49	    tau = np.zeros(N)
50	    mc_rates = np.zeros(N)
51	    for i, s in enumerate(LABELS):
52	        mask_s = S == s
53	        tau[mask_s] = np.where(Z[mask_s] == 1, config['tau_z1'][i], config['tau_z0'][i])
54	        mc_rates[mask_s] = config['misclass'][i]
55	
56	    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)
57	    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)
58	
59	    idx = rng.choice(N, min(n_expert, N), replace=False)
60	    expert_mask = np.zeros(N, dtype=bool)
61	    expert_mask[idx] = True
62	    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, Y=Y, tau=tau, expert_mask=expert_mask)
63	
64	
65	def diff_in_means(Y, T, mask):
66	    t1, t0 = mask & (T == 1), mask & (T == 0)
67	    n1, n0 = t1.sum(), t0.sum()
68	    if n1 < 2 or n0 < 2:
69	        return np.nan, np.nan
70	    y1, y0 = Y[t1], Y[t0]
71	    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
72	
73	
74	def estimate_cm(z_true, z_hat):
75	    C = np.zeros((2, 2))
76	    for z in [0, 1]:
77	        mask = z_true == z
78	        n = mask.sum()
79	        for zh in [0, 1]:
80	            C[z, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
81	    return C
82	
83	
84	def _dirmult_neg_ll(alpha, counts_z):
85	    a = alpha / 2.0
86	    if a < 1e-10:
87	        return 1e10
88	    ll = 0.0
89	    for c0, c1 in counts_z:
90	        n = c0 + c1
91	        if n == 0:
92	            continue
93	        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)
94	        ll -= 2 * gammaln(a) - gammaln(2 * a)
95	    return -ll
96	
97	
98	def estimate_cm_eb(counts):
99	    """Empirical Bayes: optimize shared Dirichlet concentration, return per-subgroup posterior mean."""
100	    k = len(LABELS)
101	    alpha_opt = np.zeros(2)
102	    for z in [0, 1]:
103	        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
104	        total = sum(c0 + c1 for c0, c1 in cl)
105	        if total == 0:
106	            alpha_opt[z] = 2.0
107	            continue
108	        res = minimize_scalar(
109	            lambda a, cz=cl: _dirmult_neg_ll(a, cz), bounds=(0.01, 500), method='bounded')
110	        alpha_opt[z] = res.x
111	
112	    C = {}
113	    for i, s in enumerate(LABELS):
114	        C_s = np.zeros((2, 2))
115	        for z in [0, 1]:
116	            a = alpha_opt[z] / 2.0
117	            n = counts[i, z, :].sum()
118	            d = n + 2 * a
119	            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5
120	            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5
121	        C[s] = C_s
122	    return C
123	
124	
125	def get_counts(z_true, z_hat, subgroups):
126	    k = len(LABELS)
127	    counts = np.zeros((k, 2, 2), dtype=int)
128	    for i, s in enumerate(LABELS):
129	        ms = subgroups == s
130	        for z in [0, 1]:
131	            mz = ms & (z_true == z)
132	            counts[i, z, 0] = (z_hat[mz] == 0).sum()
133	            counts[i, z, 1] = (z_hat[mz] == 1).sum()
134	    return counts
135	
136	
137	def build_mixing_matrix(C):
138	    M = np.zeros((2, 2))
139	    for zh in [0, 1]:
140	        cs = C[0, zh] + C[1, zh]
141	        M[zh, 0] = C[0, zh] / cs if cs > 0 else 0.5
142	        M[zh, 1] = C[1, zh] / cs if cs > 0 else 0.5
143	    return M
144	
145	
146	def invert_mixing(M, tau_obs, se_obs):
147	    if np.linalg.cond(M) > 100 or abs(np.linalg.det(M)) < 1e-10:
148	        return tau_obs.copy(), se_obs.copy(), True
149	    Mi = np.linalg.inv(M)
150	    tau_c = Mi @ tau_obs
151	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
152	    return tau_c, se_c, False
153	
154	
155	def run_one_mc(config, n_expert, seed):
156	    data = generate_data(config, n_expert, seed)
157	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
158	    em = data['expert_mask']
159	
160	    z_exp, zh_exp, s_exp = Z[em], Z_hat[em], S[em]
161	
162	    # True per-subgroup CATEs
163	    tau_true = {}
164	    for i, s in enumerate(LABELS):
165	        tau_true[s] = np.array([config['tau_z0'][i], config['tau_z1'][i]])
166	
167	    # Observed CATEs per subgroup (using Z_hat)
168	    sub_obs, sub_se = {}, {}
169	    for s in LABELS:
170	        sm = S == s
171	        th0, se0 = diff_in_means(Y, T, sm & (Z_hat == 0))
172	        th1, se1 = diff_in_means(Y, T, sm & (Z_hat == 1))
173	        sub_obs[s] = np.array([th0, th1])
174	        sub_se[s] = np.array([se0, se1])
175	
176	    for s in LABELS:
177	        if np.any(np.isnan(sub_obs[s])):
178	            return []
179	
180	    # Oracle: use true Z
181	    oracle_tau, oracle_se = {}, {}
182	    for s in LABELS:
183	        sm = S == s
184	        th0, se0 = diff_in_means(Y, T, sm & (Z == 0))
185	        th1, se1 = diff_in_means(Y, T, sm & (Z == 1))
186	        oracle_tau[s] = np.array([th0, th1])
187	        oracle_se[s] = np.array([se0, se1])
188	
189	    # Global confusion matrix (pooled expert data)
190	    C_global = estimate_cm(z_exp, zh_exp)
191	    M_global = build_mixing_matrix(C_global)
192	
193	    # Per-subgroup confusion matrices
194	    counts = get_counts(z_exp, zh_exp, s_exp)
195	
196	    # MLE per-subgroup
197	    C_mle = {}
198	    for i, s in enumerate(LABELS):
199	        sm = s_exp == s
200	        if sm.sum() < 4:
201	            C_mle[s] = C_global.copy()
202	        else:
203	            C_mle[s] = estimate_cm(z_exp[sm], zh_exp[sm])
204	
205	    # EB per-subgroup
206	    C_eb = estimate_cm_eb(counts)
207	
208	    rows = []
209	
210	    def make_row(method, s, tau_hat, se_hat):
211	        tt = tau_true[s]
212	        for z_idx in [0, 1]:
213	            ci_lo = tau_hat[z_idx] - 1.96 * se_hat[z_idx]
214	            ci_hi = tau_hat[z_idx] + 1.96 * se_hat[z_idx]
215	            rows.append({
216	                'n_expert': n_expert, 'seed': seed, 'method': method,
217	                'subgroup': s, 'z': f'z{z_idx}',
218	                'tau_hat': tau_hat[z_idx], 'tau_true': tt[z_idx],
219	                'se': se_hat[z_idx],
220	                'ci_lower': ci_lo, 'ci_upper': ci_hi,
221	                'covers': int(ci_lo <= tt[z_idx] <= ci_hi),
222	            })
223	
224	    for s in LABELS:
225	        # Oracle
226	        make_row('oracle', s, oracle_tau[s], oracle_se[s])
227	
228	        # Naive
229	        make_row('naive', s, sub_obs[s], sub_se[s])
230	
231	        # Global corrected
232	        tau_gc, se_gc, _ = invert_mixing(M_global, sub_obs[s], sub_se[s])
233	        make_row('global_corrected', s, tau_gc, se_gc)
234	
235	        # EC-HTE (MLE)
236	        M_mle_s = build_mixing_matrix(C_mle[s])
237	        tau_mle, se_mle, _ = invert_mixing(M_mle_s, sub_obs[s], sub_se[s])
238	        make_row('ec_hte_mle', s, tau_mle, se_mle)
239	
240	        # EC-HTE (EB)
241	        M_eb_s = build_mixing_matrix(C_eb[s])
242	        tau_eb, se_eb, _ = invert_mixing(M_eb_s, sub_obs[s], sub_se[s])
243	        make_row('ec_hte_eb', s, tau_eb, se_eb)
244	
245	    return rows
246	
247	
248	def aggregate(df):
249	    agg_rows = []
250	    for (ne, method, subgroup), grp in df.groupby(['n_expert', 'method', 'subgroup']):
251	        row = {'n_expert': int(ne), 'method': method, 'subgroup': subgroup}
252	        for z in ['z0', 'z1']:
253	            zg = grp[grp['z'] == z]
254	            err = zg['tau_hat'].values - zg['tau_true'].values
255	            row[f'bias_{z}'] = err.mean()
256	            row[f'abs_bias_{z}'] = abs(err.mean())
257	            row[f'rmse_{z}'] = np.sqrt((err ** 2).mean())
258	            row[f'coverage_{z}'] = zg['covers'].mean()
259	            row[f'mean_se_{z}'] = zg['se'].mean()
260	        row['abs_bias'] = (row['abs_bias_z0'] + row['abs_bias_z1']) / 2
261	        row['rmse'] = (row['rmse_z0'] + row['rmse_z1']) / 2
262	        row['coverage'] = (row['coverage_z0'] + row['coverage_z1']) / 2
263	        agg_rows.append(row)
264	    return pd.DataFrame(agg_rows)
265	
266	
267	def print_table(df_agg, config_name):
268	    print(f"\n{'=' * 120}")
269	    print(f"  Config: {config_name}")
270	    print(f"{'=' * 120}")
271	    header = (f"{'n_exp':>5} {'Method':>18} {'Subgrp':>6} | "
272	              f"{'|Bias| z0':>9} {'|Bias| z1':>9} | "
273	              f"{'RMSE z0':>8} {'RMSE z1':>8} | "
274	              f"{'Cov z0':>7} {'Cov z1':>7} | "
275	              f"{'RMSE':>7} {'Cov':>5}")
276	    print(header)
277	    print("-" * len(header))
278	    for ne in N_EXPERTS:
279	        for method in ['oracle', 'naive', 'global_corrected', 'ec_hte_mle', 'ec_hte_eb']:
280	            for s in LABELS:
281	                r = df_agg[(df_agg['n_expert'] == ne) &
282	                           (df_agg['method'] == method) &
283	                           (df_agg['subgroup'] == s)]
284	                if r.empty:
285	                    continue
286	                r = r.iloc[0]
287	                print(f"{ne:5d} {method:>18} {s:>6} | "
288	                      f"{r['abs_bias_z0']:9.4f} {r['abs_bias_z1']:9.4f} | "
289	                      f"{r['rmse_z0']:8.4f} {r['rmse_z1']:8.4f} | "
290	                      f"{r['coverage_z0']:7.3f} {r['coverage_z1']:7.3f} | "
291	                      f"{r['rmse']:7.4f} {r['coverage']:5.3f}")
292	        print("-" * len(header))
293	
294	
295	def main():
296	    print(f"W8: A5 Violation — Correlated Δτ and δ")
297	    print(f"N={N}, n_expert={N_EXPERTS}, N_MC={N_MC}")
298	    print(f"Configs: aligned (positive corr), adversarial (negative corr)\n")
299	
300	    all_dfs = {}
301	    t0_total = time.time()
302	
303	    for cfg_name, cfg in CONFIGS.items():
304	        print(f"\n--- Running config: {cfg_name} ---")
305	        delta_tau = [cfg['tau_z1'][i] - cfg['tau_z0'][i] for i in range(len(LABELS))]
306	        for i, s in enumerate(LABELS):
307	            print(f"  {s}: π={cfg['misclass'][i]:.2f}, "
308	                  f"τ(z=0)={cfg['tau_z0'][i]:.2f}, τ(z=1)={cfg['tau_z1'][i]:.2f}, "
309	                  f"Δτ={delta_tau[i]:.2f}")
310	
311	        all_rows = []
312	        total = len(N_EXPERTS) * N_MC
313	        count = 0
314	        t0 = time.time()
315	
316	        for ne in N_EXPERTS:
317	            for seed in SEEDS:
318	                rows = run_one_mc(cfg, ne, seed)
319	                all_rows.extend(rows)
320	                count += 1
321	                if count % max(1, total // 5) == 0:
322	                    el = time.time() - t0
323	                    eta = el / count * (total - count)
324	                    print(f"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s")
325	
326	        elapsed = time.time() - t0
327	        print(f"  Done in {elapsed:.1f}s")
328	
329	        df_raw = pd.DataFrame(all_rows)
330	        df_raw['config'] = cfg_name
331	        df_agg = aggregate(df_raw)
332	        df_agg['config'] = cfg_name
333	        all_dfs[cfg_name] = (df_raw, df_agg)
334	
335	        print_table(df_agg, cfg_name)
336	
337	    total_elapsed = time.time() - t0_total
338	    print(f"\nTotal runtime: {total_elapsed:.1f}s")
339	
340	    # Combine and save
341	    os.makedirs('results', exist_ok=True)
342	    raw_all = pd.concat([v[0] for v in all_dfs.values()], ignore_index=True)
343	    agg_all = pd.concat([v[1] for v in all_dfs.values()], ignore_index=True)
344	
345	    raw_path = 'results/exp_w8_a5_violation_raw.csv'
346	    agg_path = 'results/exp_w8_a5_violation.csv'
347	    raw_all.to_csv(raw_path, index=False)
348	    agg_all.to_csv(agg_path, index=False)
349	    print(f"\nSaved: {agg_path} ({len(agg_all)} rows)")
350	    print(f"Saved: {raw_path} ({len(raw_all)} rows)")
351	
352	    # Overall summary table (for paper)
353	    print(f"\n{'=' * 120}")
354	    print("SUMMARY TABLE (for paper)")
355	    print(f"{'=' * 120}")
356	    header = (f"{'Config':>12} {'n_exp':>5} {'Method':>18} | "
357	              f"{'S0 |Bias|':>9} {'S1 |Bias|':>9} | "
358	              f"{'S0 RMSE':>8} {'S1 RMSE':>8} | "
359	              f"{'S0 Cov':>7} {'S1 Cov':>7} | "
360	              f"{'Overall RMSE':>12}")
361	    print(header)
362	    print("-" * len(header))
363	
364	    for cfg_name in ['aligned', 'adversarial']:
365	        df_agg = all_dfs[cfg_name][1]
366	        for ne in N_EXPERTS:
367	            for method in ['naive', 'global_corrected', 'ec_hte_eb']:
368	                s0 = df_agg[(df_agg['n_expert'] == ne) &
369	                            (df_agg['method'] == method) &
370	                            (df_agg['subgroup'] == 'S0')]
371	                s1 = df_agg[(df_agg['n_expert'] == ne) &
372	                            (df_agg['method'] == method) &
373	                            (df_agg['subgroup'] == 'S1')]
374	                if s0.empty or s1.empty:
375	                    continue
376	                s0, s1 = s0.iloc[0], s1.iloc[0]
377	                overall_rmse = (s0['rmse'] + s1['rmse']) / 2
378	                print(f"{cfg_name:>12} {ne:5d} {method:>18} | "
379	                      f"{s0['abs_bias']:9.4f} {s1['abs_bias']:9.4f} | "
380	                      f"{s0['rmse']:8.4f} {s1['rmse']:8.4f} | "
381	                      f"{s0['coverage']:7.3f} {s1['coverage']:7.3f} | "
382	                      f"{overall_rmse:12.4f}")
383	            print("-" * len(header))
384	
385	    # LaTeX paragraph
386	    a_agg = all_dfs['aligned'][1]
387	    d_agg = all_dfs['adversarial'][1]
388	
389	    def get_cov(df, ne, method):
390	        sub = df[(df['n_expert'] == ne) & (df['method'] == method)]
391	        return sub['coverage'].mean()
392	
393	    def get_rmse(df, ne, method):
394	        sub = df[(df['n_expert'] == ne) & (df['method'] == method)]
395	        return sub['rmse'].mean()
396	
397	    ne_main = 500
398	
399	    naive_cov_a = get_cov(a_agg, ne_main, 'naive')
400	    gc_cov_a = get_cov(a_agg, ne_main, 'global_corrected')
401	    eb_cov_a = get_cov(a_agg, ne_main, 'ec_hte_eb')
402	    naive_cov_d = get_cov(d_agg, ne_main, 'naive')
403	    gc_cov_d = get_cov(d_agg, ne_main, 'global_corrected')
404	    eb_cov_d = get_cov(d_agg, ne_main, 'ec_hte_eb')
405	
406	    naive_rmse_a = get_rmse(a_agg, ne_main, 'naive')
407	    eb_rmse_a = get_rmse(a_agg, ne_main, 'ec_hte_eb')
408	    naive_rmse_d = get_rmse(d_agg, ne_main, 'naive')
409	    eb_rmse_d = get_rmse(d_agg, ne_main, 'ec_hte_eb')
410	
411	    latex = rf"""\paragraph{{Robustness to Correlated Heterogeneity (A5 Violation)}}
412	Assumption~(A5) posits that CATE heterogeneity $\Delta\tau_s = \tau_s(z{{=}}1) - \tau_s(z{{=}}0)$
413	is independent of the subgroup misclassification rate $\delta_s$. We test two
414	structured violations with $K=2$ subgroups and
415	$\delta \in \{{0.05, 0.25\}}$: (i)~\emph{{aligned}}, where the high-error
416	subgroup also has large $\Delta\tau$ ($0.70$ vs.\ $0.30$), and
417	(ii)~\emph{{adversarial}}, the reverse assignment. Under the aligned
418	configuration, the naive estimator's bias is amplified by the $\delta_s
419	\times \Delta\tau_s$ product, yielding RMSE $={naive_rmse_a:.3f}$
420	and coverage $={naive_cov_a:.0%}$ ($n_{{\text{{expert}}}}={ne_main}$).
421	EC-HTE reduces RMSE to ${eb_rmse_a:.3f}$ with ${eb_cov_a:.0%}$ coverage.
422	In the adversarial case the bias product is attenuated, so the global
423	correction appears adequate (coverage ${gc_cov_d:.0%}$); however,
424	EC-HTE still achieves ${eb_cov_d:.0%}$ coverage with RMSE ${eb_rmse_d:.3f}$,
425	matching or improving the global baseline. Across both correlation
426	structures, EC-HTE maintains near-nominal coverage, confirming that
427	the estimator does not rely on Assumption~(A5) for practical validity."""
428	
429	    print(f"\n{'=' * 120}")
430	    print("LaTeX paragraph:")
431	    print(f"{'=' * 120}")
432	    print(latex)
433	
434	
435	if __name__ == '__main__':
436	    main()
437	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "eb54b95b-8075-4363-a9c8-c1cfa9a34cb1"
}
```

</details>

---

### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8238e369993613e3",
  "tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "description": "Reading exp001_regularize.py",
  "usage": {
    "total_tokens": 50473,
    "tool_uses": 9,
    "duration_ms": 11659
  },
  "last_tool_name": "Read",
  "uuid": "8d73a26c-184d-47f3-afed-7be6f1fc37b7",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a"
}
```

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_012BecspFhKXMvY6DsWXsLBr`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "2aca5953-5ef5-4dd1-996f-bf94a33c0589",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AsyEREciGnpmGz2TvAYbBv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 17580,
      "cache_read_input_tokens": 32851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17580,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T16:15:40.078Z_

<details><summary>↩ Tool result · `toolu_012BecspFhKXMvY6DsWXsLBr`</summary>

```text
1	#!/usr/bin/env python3
2	"""exp001_regularize.py - Rerun affected cells with condition-number-guarded inversion."""
3	
4	import argparse
5	import time
6	import numpy as np
7	import pandas as pd
8	
9	from exp001_hb_synthetic import (
10	    REGIMES, SUBGROUP_LABELS,
11	    generate_data, get_counts, build_mixing_matrix, diff_in_means,
12	    estimate_cm_mle, estimate_cm_hb_eb, estimate_cm_hb_gibbs,
13	    invert_mixing_safe, aggregate_results,
14	)
15	
16	AFFECTED_CELLS = [
17	    (4, 'extreme', 50),
18	    (4, 'extreme', 100),
19	    (4, 'moderate', 50),
20	    (4, 'moderate', 100),
21	    (4, 'homogeneous', 50),
22	    (4, 'homogeneous', 100),
23	]
24	
25	
26	def run_one_mc_reg(regime_name, regime_params, n_expert, k, seed,
27	                   cond_threshold=100, n_chains=4, n_iter=4000, n_warmup=2000):
28	    data = generate_data(regime_params, n_expert, k, seed)
29	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
30	    em = data['expert_mask']
31	    labels = SUBGROUP_LABELS[k]
32	    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']
33	
34	    counts = get_counts(Z[em], Z_hat[em], S[em], labels)
35	    C_mle = estimate_cm_mle(counts, labels)
36	    C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed,
37	                                          n_chains=n_chains, n_iter=n_iter,
38	                                          n_warmup=n_warmup)
39	
40	    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}
41	    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}
42	
43	    base = {'regime': regime_name, 'n_expert': n_expert,
44	            'k_subgroups': k, 'mc_run': seed}
45	    rows = []
46	    guard_hb = 0
47	    guard_mle = 0
48	
49	    for s in labels:
50	        sm = S == s
51	        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))
52	        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))
53	
54	        tau_obs = np.array([th0_n, th1_n])
55	        se_obs = np.array([se0_n, se1_n])
56	        if np.any(np.isnan(tau_obs)):
57	            continue
58	
59	        cond_mle = np.linalg.cond(M_mle[s])
60	        cond_hb = np.linalg.cond(M_hb[s])
61	        if cond_mle > cond_threshold:
62	            guard_mle += 1
63	        if cond_hb > cond_threshold:
64	            guard_hb += 1
65	
66	        tml_r, sml_r = invert_mixing_safe(M_mle[s], tau_obs, se_obs, cond_threshold)
67	        thb_r, shb_r = invert_mixing_safe(M_hb[s], tau_obs, se_obs, cond_threshold)
68	
69	        def mr(method, th0, th1, se0, se1):
70	            return {**base, 'subgroup': s, 'method': method,
71	                    'tau_hat_z0': th0, 'tau_hat_z1': th1,
72	                    'se_z0': se0, 'se_z1': se1,
73	                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}
74	
75	        rows.append(mr('mle_laplace_reg', tml_r[0], tml_r[1], sml_r[0], sml_r[1]))
76	        rows.append(mr('hb_dirichlet_reg', thb_r[0], thb_r[1], shb_r[0], shb_r[1]))
77	
78	    return rows, hb_diag, guard_hb, guard_mle
79	
80	
81	if __name__ == '__main__':
82	    parser = argparse.ArgumentParser()
83	    parser.add_argument('--n-mc', type=int, default=100)
84	    parser.add_argument('--cond-threshold', type=float, default=100)
85	    args = parser.parse_args()
86	
87	    print(f"exp-001 Regularization fix v2 | cond_threshold={args.cond_threshold}")
88	    print(f"Affected cells: {AFFECTED_CELLS}")
89	    print(f"n_mc={args.n_mc}")
90	    print(f"MCMC config: n_chains=4, n_iter=4000, n_warmup=2000\n")
91	
92	    # ── MCMC diagnostic comparison (before/after) ────────────────────────────
93	    print("Running MCMC diagnostic comparison (seed=0, per config)...")
94	    diag_rows = []
95	    for k, regime, n_expert in AFFECTED_CELLS:
96	        rp = REGIMES[k][regime]
97	        d = generate_data(rp, n_expert, k, seed=0)
98	        em = d['expert_mask']
99	        labels = SUBGROUP_LABELS[k]
100	        counts = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], labels)
101	
102	        _, diag_before = estimate_cm_hb_gibbs(counts, labels, seed=0,
103	                                               n_chains=2, n_iter=2000, n_warmup=1000)
104	        _, diag_after = estimate_cm_hb_gibbs(counts, labels, seed=0,
105	                                              n_chains=4, n_iter=4000, n_warmup=2000)
106	        diag_rows.append({
107	            'config': f"K={k}/{regime}/n={n_expert}",
108	            'rhat_before': diag_before['rhat_max'],
109	            'rhat_after': diag_after['rhat_max'],
110	            'ess_before': diag_before['ess_min'],
111	            'ess_after': diag_after['ess_min'],
112	        })
113	
114	    print("\n" + "=" * 100)
115	    print("MCMC Diagnostic Comparison (seed=0)")
116	    print(f"{'Config':>30s} | {'Rhat_max (2ch)':>14s} | {'Rhat_max (4ch)':>14s} | "
117	          f"{'ESS_min (2ch)':>14s} | {'ESS_min (4ch)':>14s}")
118	    print("-" * 100)
119	    for r in diag_rows:
120	        print(f"{r['config']:>30s} | {r['rhat_before']:14.4f} | {r['rhat_after']:14.4f} | "
121	              f"{r['ess_before']:14.1f} | {r['ess_after']:14.1f}")
122	    print("=" * 100 + "\n")
123	
124	    # ── Main MC loop ─────────────────────────────────────────────────────────
125	    all_rows = []
126	    guard_stats = {}
127	    diag_agg = {}
128	    total = len(AFFECTED_CELLS) * args.n_mc
129	    count = 0
130	    t0 = time.time()
131	
132	    for k, regime, n_expert in AFFECTED_CELLS:
133	        key = (k, regime, n_expert)
134	        guard_stats[key] = {'total': 0, 'guard_hb': 0, 'guard_mle': 0}
135	        diag_agg[key] = {'rhat_max': [], 'ess_min': []}
136	        rp = REGIMES[k][regime]
137	        for mc in range(args.n_mc):
138	            rows, hb_diag, g_hb, g_mle = run_one_mc_reg(
139	                regime, rp, n_expert, k, seed=mc,
140	                cond_threshold=args.cond_threshold,
141	                n_chains=4, n_iter=4000, n_warmup=2000)
142	            all_rows.extend(rows)
143	            guard_stats[key]['total'] += 1
144	            guard_stats[key]['guard_hb'] += g_hb
145	            guard_stats[key]['guard_mle'] += g_mle
146	            diag_agg[key]['rhat_max'].append(hb_diag['rhat_max'])
147	            diag_agg[key]['ess_min'].append(hb_diag['ess_min'])
148	            count += 1
149	            if count % 50 == 0:
150	                el = time.time() - t0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "95ca2a08-c2e0-41d0-aaa2-0332383ac0df"
}
```

</details>

---

### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8238e369993613e3",
  "tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "description": "Reading exp001_hb_synthetic.py",
  "usage": {
    "total_tokens": 60631,
    "tool_uses": 10,
    "duration_ms": 13514
  },
  "last_tool_name": "Read",
  "uuid": "95840149-7969-4a7f-a385-1b197ad56680",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a"
}
```

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_013cVmHsoZRX7cpFRt2A2jTj`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "6ded71b1-5190-4e12-ab62-7079b5fbdc92",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E9ieaDwrMgUfCdHWHbgbYY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10152,
      "cache_read_input_tokens": 50431,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10152,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-22T16:15:41.960Z_

<details><summary>↩ Tool result · `toolu_013cVmHsoZRX7cpFRt2A2jTj`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	exp001_hb_synthetic.py - Hierarchical Bayesian EC-HTE Synthetic Validation (exp-001)
4	
5	Compares confusion matrix estimators for CATE correction under heterogeneous
6	misclassification across subgroups:
7	  Oracle, Naive, Global-corrected, MLE (Laplace), HB Dirichlet (partial pooling)
8	
9	Input: Synthetic DGP parameters (regimes, expert budgets, subgroup counts)
10	Output: results/exp001_hb_results.csv, results/exp001_hb_diagnostics.csv
11	"""
12	
13	import argparse
14	import os
15	import sys
16	import time
17	import warnings
18	import numpy as np
19	import pandas as pd
20	from scipy.special import gammaln
21	from scipy.optimize import minimize_scalar
22	
23	warnings.filterwarnings('ignore')
24	
25	try:
26	    import pymc as pm
27	    import pytensor.tensor as pt
28	    import arviz as az
29	    HAS_PYMC = True
30	except ImportError:
31	    HAS_PYMC = False
32	
33	N = 5000
34	SUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}
35	
36	REGIMES = {
37	    2: {
38	        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},
39	        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},
40	        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
41	    },
42	    4: {
43	        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},
44	        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},
45	        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
46	    },
47	}
48	
49	DEFAULT_N_EXPERTS = [50, 100, 250, 500, 1000, 2000]
50	DEFAULT_K_LIST = [2, 4]
51	
52	
53	# ── DGP ───────────────────────────────────────────────────────────────────────
54	
55	def generate_data(regime_params, n_expert, k, seed):
56	    rng = np.random.RandomState(seed)
57	    labels = SUBGROUP_LABELS[k]
58	    T = rng.binomial(1, 0.5, N)
59	    Z = rng.binomial(1, 0.5, N)
60	    S = rng.choice(labels, N, p=[1.0 / k] * k)
61	    X = rng.randn(N, 5)
62	    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])
63	    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)
64	    mc_rates = np.zeros(N)
65	    for i, s in enumerate(labels):
66	        mc_rates[S == s] = regime_params['misclass'][i]
67	    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)
68	    idx = rng.choice(N, min(n_expert, N), replace=False)
69	    expert_mask = np.zeros(N, dtype=bool)
70	    expert_mask[idx] = True
71	    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, tau=tau, expert_mask=expert_mask)
72	
73	
74	# ── Helpers ───────────────────────────────────────────────────────────────────
75	
76	def diff_in_means(Y, T, mask):
77	    t1, t0 = mask & (T == 1), mask & (T == 0)
78	    n1, n0 = t1.sum(), t0.sum()
79	    if n1 < 2 or n0 < 2:
80	        return np.nan, np.nan
81	    y1, y0 = Y[t1], Y[t0]
82	    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
83	
84	
85	def get_counts(z_true, z_hat, subgroups, labels):
86	    """Confusion matrix counts per subgroup: (k, 2, 2) = [subgroup, true_z, z_hat]."""
87	    k = len(labels)
88	    counts = np.zeros((k, 2, 2), dtype=int)
89	    for i, s in enumerate(labels):
90	        ms = subgroups == s
91	        for z in [0, 1]:
92	            mz = ms & (z_true == z)
93	            counts[i, z, 0] = (z_hat[mz] == 0).sum()
94	            counts[i, z, 1] = (z_hat[mz] == 1).sum()
95	    return counts
96	
97	
98	def build_mixing_matrix(C):
99	    """C[z, z_hat] → M[z_hat, z] via Bayes rule (assuming P(Z=0)=P(Z=1)=0.5).
100	
101	    NOTE: This assumes P(Z=0)=P(Z=1)=0.5, which is correct for this experiment's
102	    DGP. For general P(Z), use the version in exp007 that takes p_z and p_z_hat.
103	    """
104	    M = np.zeros((2, 2))
105	    for zh in [0, 1]:
106	        cs = C[0, zh] + C[1, zh]
107	        if cs > 0:
108	            M[zh, 0] = C[0, zh] / cs
109	            M[zh, 1] = C[1, zh] / cs
110	        else:
111	            M[zh, :] = 0.5
112	    return M
113	
114	
115	def invert_mixing(M, tau_obs, se_obs):
116	    det = np.linalg.det(M)
117	    if abs(det) < 1e-10:
118	        return tau_obs.copy(), se_obs.copy()
119	    Mi = np.linalg.inv(M)
120	    tau_c = Mi @ tau_obs
121	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
122	    return tau_c, se_c
123	
124	
125	def safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):
126	    """Invert mixing matrix with condition number guard.
127	
128	    When cond(M_s) > threshold, matrix inversion is numerically unstable.
129	    Falls back to naive (no correction) to avoid catastrophic amplification.
130	    """
131	    cond = np.linalg.cond(M_s)
132	    if cond > cond_threshold:
133	        return tau_obs.copy()
134	    return np.linalg.solve(M_s, tau_obs)
135	
136	
137	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
138	    """Like invert_mixing but with condition number guard."""
139	    cond = np.linalg.cond(M)
140	    if cond > cond_threshold:
141	        return tau_obs.copy(), se_obs.copy()
142	    det = np.linalg.det(M)
143	    if abs(det) < 1e-10:
144	        return tau_obs.copy(), se_obs.copy()
145	    Mi = np.linalg.inv(M)
146	    tau_c = Mi @ tau_obs
147	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
148	    return tau_c, se_c
149	
150	
151	# ── Confusion Matrix Estimators ───────────────────────────────────────────────
152	
153	def estimate_cm_mle(counts, labels):
154	    """Per-subgroup MLE with Laplace smoothing (add-1)."""
155	    C = {}
156	    for i, s in enumerate(labels):
157	        C_s = np.zeros((2, 2))
158	        for z in [0, 1]:
159	            n = counts[i, z, :].sum()
160	            for zh in [0, 1]:
161	                C_s[z, zh] = (counts[i, z, zh] + 1) / (n + 2) if n > 0 else 0.5
162	        C[s] = C_s
163	    return C
164	
165	
166	def _dirmult_neg_ll(alpha, counts_z):
167	    """Negative log marginal likelihood for Dirichlet-Multinomial."""
168	    a = alpha / 2.0
169	    if a < 1e-10:
170	        return 1e10
171	    ll = 0.0
172	    for c0, c1 in counts_z:
173	        n = c0 + c1
174	        if n == 0:
175	            continue
176	        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)
177	        ll -= 2 * gammaln(a) - gammaln(2 * a)
178	    return -ll
179	
180	
181	def estimate_cm_hb_eb(counts, labels):
182	    """Empirical Bayes HB: optimize shared Dirichlet concentration, posterior mean."""
183	    k = len(labels)
184	    alpha_opt = np.zeros(2)
185	    for z in [0, 1]:
186	        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
187	        total = sum(c0 + c1 for c0, c1 in cl)
188	        if total == 0:
189	            alpha_opt[z] = 2.0
190	            continue
191	        res = minimize_scalar(
192	            lambda a: _dirmult_neg_ll(a, cl), bounds=(0.01, 500), method='bounded')
193	        alpha_opt[z] = res.x
194	
195	    C = {}
196	    for i, s in enumerate(labels):
197	        C_s = np.zeros((2, 2))
198	        for z in [0, 1]:
199	            a = alpha_opt[z] / 2.0
200	            n = counts[i, z, :].sum()
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "6d3f1b5c-0543-4c8e-aaa4-f30c81003c29"
}
```

</details>

---

### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8238e369993613e3",
  "tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "description": "Reading exp015_semi_real_cm.py",
  "usage": {
    "total_tokens": 63920,
    "tool_uses": 11,
    "duration_ms": 15805
  },
  "last_tool_name": "Read",
  "uuid": "06c2cbf6-a1a0-4cb0-9aa5-50274587325b",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a"
}
```

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01PrH7b2EF5k9deTRbuHU34t`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "bba12fe5-8e4b-4248-a2de-dc2745872f35",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016dXULskFwiec2MZFDU8uVc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3288,
      "cache_read_input_tokens": 60583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3288,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-22T16:15:44.228Z_

<details><summary>↩ Tool result · `toolu_01PrH7b2EF5k9deTRbuHU34t`</summary>

```text
1	"""
2	exp-015: Semi-Real Confusion Matrix EC-HTE Experiment.
3	
4	Uses real asymmetric confusion matrices from GPT-4.1 TweetEval pilot annotations.
5	Ground truth CATE is synthetic, but CMs come from real LLM pilot data.
6	
7	4 subgroups with real asymmetric CMs (from pilot GPT-4.1 annotations, n>=10 only):
8	  S0 (False_medium): FPR=0.054, FNR=0.526, weight=0.38
9	  S1 (False_short):  FPR=0.101, FNR=0.300, weight=0.22
10	  S2 (True_short):   FPR=0.143, FNR=0.308, weight=0.14
11	  S3 (True_medium):  FPR=0.194, FNR=0.222, weight=0.25
12	
13	Output:
14	  results/exp015_semi_real_raw.csv
15	  results/exp015_semi_real_summary.csv
16	  results/exp015_semi_real_analysis.md
17	
18	Usage: python3 exp015_semi_real_cm.py --n-mc 100
19	"""
20	
21	import argparse
22	import time
23	import warnings
24	import numpy as np
25	import pandas as pd
26	from scipy.special import gammaln
27	
28	warnings.filterwarnings('ignore')
29	
30	# === Config ===
31	
32	N = 5000
33	N_EXPERTS = [100, 250, 500]
34	SEED_BASE = 0
35	
36	SUBGROUP_LABELS = ['S0', 'S1', 'S2', 'S3']
37	SUBGROUP_WEIGHTS = np.array([0.38, 0.22, 0.14, 0.25])
38	SUBGROUP_WEIGHTS = SUBGROUP_WEIGHTS / SUBGROUP_WEIGHTS.sum()
39	
40	# Real asymmetric CMs from GPT-4.1 pilot (FPR, FNR per subgroup)
41	SUBGROUP_CM = {
42	    'S0': {'fpr': 0.054, 'fnr': 0.526},
43	    'S1': {'fpr': 0.101, 'fnr': 0.300},
44	    'S2': {'fpr': 0.143, 'fnr': 0.308},
45	    'S3': {'fpr': 0.194, 'fnr': 0.222},
46	}
47	
48	P_Z1 = 0.18  # P(Z=1) from pilot overall
49	P_T1 = 0.5
50	
51	
52	def get_cm_matrix(fpr, fnr):
53	    """Build 2x2 confusion matrix: M[z_true, z_obs]."""
54	    return np.array([[1 - fpr, fpr],
55	                     [fnr, 1 - fnr]])
56	
57	
58	# True CATE by (z, subgroup)
59	def true_tau(z, s_idx):
60	    if z == 0:
61	        return 0.3 + 0.1 * s_idx
62	    else:
63	        return 0.8 - 0.15 * s_idx
64	
65	
66	# === Core Estimators ===
67	
68	def diff_in_means(Y, T, mask):
69	    t1 = mask & (T == 1)
70	    t0 = mask & (T == 0)
71	    n1, n0 = t1.sum(), t0.sum()
72	    if n1 < 2 or n0 < 2:
73	        return np.nan, np.nan
74	    y1, y0 = Y[t1], Y[t0]
75	    tau_hat = y1.mean() - y0.mean()
76	    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
77	    return tau_hat, se
78	
79	
80	def estimate_confusion_matrix(z_true, z_hat):
81	    C = np.zeros((2, 2))
82	    for zt in [0, 1]:
83	        mask = z_true == zt
84	        n = mask.sum()
85	        for zh in [0, 1]:
86	            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
87	    return C
88	
89	
90	def build_mixing_matrix(C, p_z, p_z_hat):
91	    """M[z_hat, z] = P(Z=z | Z_hat=z_hat) via Bayes' rule."""
92	    M = np.zeros((2, 2))
93	    for zh in [0, 1]:
94	        for z in [0, 1]:
95	            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5
96	    return M
97	
98	
99	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
100	    cond = np.linalg.cond(M)
101	    if cond > cond_threshold:
102	        return tau_obs.copy(), se_obs.copy()
103	    det = np.linalg.det(M)
104	    if abs(det) < 1e-10:
105	        return tau_obs.copy(), se_obs.copy()
106	    Mi = np.linalg.inv(M)
107	    tau_c = Mi @ tau_obs
108	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
109	    return tau_c, se_c
110	
111	
112	# === HB Gibbs Sampler ===
113	
114	def get_counts(z_true, z_hat, subgroups, labels):
115	    k = len(labels)
116	    counts = np.zeros((k, 2, 2), dtype=int)
117	    for i, s in enumerate(labels):
118	        ms = subgroups == s
119	        for z in [0, 1]:
120	            mz = ms & (z_true == z)
121	            counts[i, z, 0] = (z_hat[mz] == 0).sum()
122	            counts[i, z, 1] = (z_hat[mz] == 1).sum()
123	    return counts
124	
125	
126	def _split_rhat(chains):
127	    parts = []
128	    for c in range(chains.shape[0]):
129	        half = chains.shape[1] // 2
130	        parts.append(chains[c, :half])
131	        parts.append(chains[c, half:2 * half])
132	    parts = np.array(parts)
133	    m = parts.shape[0]
134	    n = parts.shape[1]
135	    chain_means = parts.mean(axis=1)
136	    W = np.mean(np.var(parts, axis=1, ddof=1))
137	    B = n * np.var(chain_means, ddof=1)
138	    if W < 1e-20:
139	        return 1.0
140	    var_hat = (1 - 1.0 / n) * W + B / n
141	    return float(np.sqrt(var_hat / W))
142	
143	
144	def _bulk_ess(chains):
145	    x = chains.ravel()
146	    n = len(x)
147	    mu = x.mean()
148	    xc = x - mu
149	    max_lag = min(n // 2, 300)
150	    c0 = np.dot(xc, xc)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "d942f7c7-1b47-4bfc-aefc-a8e2e33b5267"
}
```

</details>

---

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8238e369993613e3",
  "tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "description": "Reading exp017_rlearner.py",
  "usage": {
    "total_tokens": 63921,
    "tool_uses": 12,
    "duration_ms": 15932
  },
  "last_tool_name": "Read",
  "uuid": "c4cda280-1a14-461b-acb8-045cf9a03a52",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a"
}
```

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01Egf6R79rWbhTtza5NhYWty`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "e618bc3e-8198-4219-bcb6-ab05561e6f9d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016dXULskFwiec2MZFDU8uVc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3288,
      "cache_read_input_tokens": 60583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3288,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-22T16:15:44.352Z_

<details><summary>↩ Tool result · `toolu_01Egf6R79rWbhTtza5NhYWty`</summary>

```text
1	#!/usr/bin/env python3
2	"""exp017_rlearner.py - R-learner EC-HTE compatibility (exp-017)
3	
4	Validates EC-HTE correction with R-learner (Nie & Wager 2021) as CATE estimator.
5	Four methods: oracle (Z_true), naive (Z_hat), global (global M^-1),
6	ec_hte (per-subgroup M_s^-1).
7	
8	Config: K=2, extreme (pi=[0.05, 0.20]), n_expert=500, 50 MC seeds.
9	DGP matches exp-011 for direct comparability.
10	"""
11	
12	import argparse
13	import os
14	import time
15	import warnings
16	import numpy as np
17	import pandas as pd
18	from sklearn.ensemble import RandomForestRegressor
19	from sklearn.model_selection import KFold
20	
21	warnings.filterwarnings('ignore')
22	
23	N = 5000
24	K = 2
25	REGIME = 'extreme'
26	N_EXPERT = 500
27	TAU_TRUE = {0: 0.5, 1: 1.5}
28	MISCLASS_RATES = [0.05, 0.20]
29	
30	
31	def generate_data(seed):
32	    rng = np.random.RandomState(seed)
33	    S = rng.randint(0, K, N)
34	    T = rng.binomial(1, 0.5, N)
35	    Z_true = rng.binomial(1, 0.5, N)
36	
37	    Z_hat = Z_true.copy()
38	    for s in range(K):
39	        mask_s = S == s
40	        flip = rng.binomial(1, MISCLASS_RATES[s], mask_s.sum())
41	        Z_hat[mask_s] = np.where(flip, 1 - Z_true[mask_s], Z_true[mask_s])
42	
43	    tau = np.where(Z_true == 1, TAU_TRUE[1], TAU_TRUE[0])
44	    baseline = 1.0 + 0.5 * Z_true
45	    Y = baseline + tau * T + rng.normal(0, 1, N)
46	
47	    expert_idx = rng.choice(N, N_EXPERT, replace=False)
48	    expert_mask = np.zeros(N, dtype=bool)
49	    expert_mask[expert_idx] = True
50	
51	    return Y, T, Z_true, Z_hat, S, expert_mask
52	
53	
54	def compute_confusion_matrix(z_true, z_hat):
55	    C = np.zeros((2, 2))
56	    for z in [0, 1]:
57	        mz = z_true == z
58	        C[z, 0] = (z_hat[mz] == 0).sum() + 1
59	        C[z, 1] = (z_hat[mz] == 1).sum() + 1
60	    return C / C.sum(axis=1, keepdims=True)
61	
62	
63	def build_mixing_matrix(C):
64	    M = np.zeros((2, 2))
65	    for zh in [0, 1]:
66	        cs = C[0, zh] + C[1, zh]
67	        if cs > 0:
68	            M[zh, 0] = C[0, zh] / cs
69	            M[zh, 1] = C[1, zh] / cs
70	        else:
71	            M[zh, :] = 0.5
72	    return M
73	
74	
75	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
76	    cond = np.linalg.cond(M)
77	    if cond > cond_threshold:
78	        return tau_obs.copy(), se_obs.copy()
79	    det = np.linalg.det(M)
80	    if abs(det) < 1e-10:
81	        return tau_obs.copy(), se_obs.copy()
82	    Mi = np.linalg.inv(M)
83	    tau_c = Mi @ tau_obs
84	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
85	    return tau_c, se_c
86	
87	
88	def rlearner_cate(Y, T, Z_feat, S):
89	    """R-learner CATE estimation with cross-fitted nuisance.
90	
91	    Steps (Nie & Wager 2021):
92	    1. Cross-fit m(X) = E[Y|X] via RandomForest
93	    2. e(X) = 0.5 (known RCT)
94	    3. Pseudo-outcome: tilde_Y = (Y - m_hat) / (T - 0.5)
95	    4. Group-average CATE per (z, s)
96	
97	    Returns {(z, s): (cate_estimate, standard_error)}.
98	    """
99	    n = len(Y)
100	    X = np.column_stack([Z_feat, S]).astype(float)
101	
102	    m_hat = np.zeros(n)
103	    kf = KFold(n_splits=5, shuffle=True, random_state=42)
104	    for train_idx, test_idx in kf.split(X):
105	        rf = RandomForestRegressor(
106	            n_estimators=200, min_samples_leaf=20, random_state=42)
107	        rf.fit(X[train_idx], Y[train_idx])
108	        m_hat[test_idx] = rf.predict(X[test_idx])
109	
110	    T_res = T - 0.5
111	    Y_res = Y - m_hat
112	    pseudo = Y_res / T_res
113	
114	    results = {}
115	    for s in range(K):
116	        for z in [0, 1]:
117	            mask = (Z_feat == z) & (S == s)
118	            n_group = mask.sum()
119	            if n_group > 1:
120	                po = pseudo[mask]
121	                results[(z, s)] = (po.mean(), po.std(ddof=1) / np.sqrt(n_group))
122	            else:
123	                results[(z, s)] = (np.nan, np.nan)
124	
125	    return results
126	
127	
128	def run_one_mc(seed):
129	    Y, T, Z_true, Z_hat, S, expert_mask = generate_data(seed)
130	
131	    cate_hat = rlearner_cate(Y, T, Z_hat, S)
132	    cate_oracle = rlearner_cate(Y, T, Z_true, S)
133	
134	    C_global = compute_confusion_matrix(Z_true[expert_mask], Z_hat[expert_mask])
135	    M_global = build_mixing_matrix(C_global)
136	
137	    M_sub = {}
138	    for s in range(K):
139	        mask_s = expert_mask & (S == s)
140	        if mask_s.sum() >= 4:
141	            C_s = compute_confusion_matrix(Z_true[mask_s], Z_hat[mask_s])
142	        else:
143	            C_s = np.array([[0.5, 0.5], [0.5, 0.5]])
144	        M_sub[s] = build_mixing_matrix(C_s)
145	
146	    rows = []
147	    for s in range(K):
148	        tau_obs = np.array([cate_hat[(0, s)][0], cate_hat[(1, s)][0]])
149	        se_obs = np.array([cate_hat[(0, s)][1], cate_hat[(1, s)][1]])
150	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "9b13d558-60c1-466c-8809-fab43756c85b"
}
```

</details>

---

### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a8238e369993613e3",
  "tool_use_id": "toolu_01ViC7keEW7s5eZikifsAL3g",
  "status": "completed",
  "output_file": "",
  "summary": "Find reference implementations",
  "usage": {
    "total_tokens": 68494,
    "tool_uses": 12,
    "duration_ms": 53063
  },
  "uuid": "68bb1ae3-7cf6-418f-8c51-cc567f2cbf23",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a"
}
```

---

### Tool result

_source line 45 · 2026-05-22T16:16:21.479Z_

<details><summary>↩ Tool result · `toolu_01ViC7keEW7s5eZikifsAL3g`</summary>

````text
Perfect! I have enough material to provide a comprehensive summary. Let me compile all the findings:

## Summary: EC-HTE Code Patterns Analysis

I've found and analyzed the requested files plus several related experiments. Here's a comprehensive report of the patterns:

### **File Locations**

1. **exp_mf2_cf_bootstrap_se.py** - `/home/ubuntu/ec_hte_llm_annotation/exp_mf2_cf_bootstrap_se.py`
2. **exp027b_cf_oracle_k2.py** - `/home/ubuntu/ec_hte_llm_annotation/exp027b_cf_oracle_k2.py`
3. **Related experiments**: exp027_cf_oracle_coverage.py, exp027c_cf_oracle_mf2dgp.py, exp_w4_bootstrap_se.py, exp_w8_a5_violation.py, exp001_hb_synthetic.py, exp015_semi_real_cm.py, exp017_rlearner.py

---

## **1. DATA GENERATING PROCESS (DGP) SETUP**

### Common DGP Components:
- **N = 5000** (sample size, constant across all files)
- **K = 2 or 4** (number of subgroups)
- **Binary treatment T**: `T ~ Bernoulli(0.5)`
- **Binary confounder/variable Z**: `Z ~ Bernoulli(0.5)` (true)
- **Subgroup assignment S**: Either categorical (0 to K-1) or string labels (A/B/C/D or S0/S1...)
- **Covariates X**: `X ~ N(0, 1)` with shape (N, 5) or similar

### Outcome Generation:
```python
tau = np.where(Z == 1, TAU_Z1, TAU_Z0)  # Treatment effect depends on Z
baseline = 1.0 + 0.5 * Z  # or similar offset
Y = baseline + tau * T + 0.5 * X[:, 0] + N(0, 1)  # outcome with treatment effect
```

### Misclassification of Z:
- **Per-subgroup misclassification rates**: π_s varies by subgroup s
  - exp_mf2: π = [0.05, 0.25]
  - exp027b: π = [0.05, 0.25]
  - exp001: K=2 has π = [0.25, 0.05] (extreme), [0.15, 0.10] (moderate), [0.12, 0.12] (homogeneous)
  
```python
Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)  # flip with probability π_s
```

### Expert Sample:
- **n_expert** ∈ {50, 100, 250, 500, 1000, 2000} (varies by experiment)
- Random subset: `expert_mask = np.zeros(N, dtype=bool); expert_mask[idx] = True`

---

## **2. CONFUSION MATRIX ESTIMATION**

### Three estimation strategies shown:

#### **A. Laplace-Smoothed MLE (Empirical)**
```python
def estimate_cm(z_true, z_hat):
    C = np.zeros((2, 2))
    for z in [0, 1]:
        mask = z_true == z
        n = mask.sum()
        for zh in [0, 1]:
            C[z, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
    return C
```
- **Format**: C[z_true, z_hat] = P(Z_hat = zh | Z = z)
- **Smoothing**: Add 1 to numerator, add 2 to denominator (Laplace)

#### **B. Hierarchical Bayesian (Empirical Bayes + Gibbs)**
- Used in exp001_hb_synthetic.py, exp015_semi_real_cm.py
- Dirichlet priors with shared hyperparameter α
- Gibbs sampler or empirical Bayes optimization
- Better for small expert budgets

#### **C. Three estimation levels:**

1. **Global** (pooled across all subgroups):
   ```python
   C_global = estimate_cm(Z_true[expert_mask], Z_hat[expert_mask])
   ```

2. **Stratified/Per-subgroup** (HB approach):
   ```python
   for s in range(K):
       mask_s = expert_mask & (S == s)
       if mask_s.sum() >= 4:
           C_s = estimate_cm(Z_true[mask_s], Z_hat[mask_s])
       else:
           C_s = estimate_cm(Z_true[expert_mask], Z_hat[expert_mask])  # fallback
   ```

3. **Oracle** (known true parameters from DGP):
   ```python
   def true_confusion_matrix(pi_s):
       return np.array([[1 - pi_s, pi_s],
                        [pi_s, 1 - pi_s]])
   ```

---

## **3. CATE ESTIMATION USING DIMENSION INVERSION (DIM)**

### A. Mixing Matrix Construction
```python
def build_mixing_matrix(C):
    M = np.zeros((2, 2))
    for zh in [0, 1]:
        cs = C[0, zh] + C[1, zh]
        M[zh, 0] = C[0, zh] / cs if cs > 0 else 0.5
        M[zh, 1] = C[1, zh] / cs if cs > 0 else 0.5
    return M
```
- **M[z_hat, z]** = P(Z = z | Z_hat = z_hat) via Bayes rule
- Assumes P(Z=0) = P(Z=1) = 0.5

### B. Observed CATE (from Z_hat):
- **Difference-in-means**: τ̂(z_hat) = E[Y | T=1, Z_hat=z] - E[Y | T=0, Z_hat=z]
- Or **CausalForestDML** directly on Z_hat:
  ```python
  cf = CausalForestDML(
      model_y=LinearRegression(),
      model_t=LogisticRegression(solver='lbfgs'),
      discrete_treatment=True,
      n_estimators=200,
      min_samples_leaf=20,
      random_state=seed,
  )
  cf.fit(Y, T, X=X_features)
  cate_vals = cf.effect(X_features).flatten()
  ```

### C. Correction via M⁻¹ (DIM Estimator)
```python
def invert_mixing(M, tau_obs, se_obs, cond_threshold=100):
    cond = np.linalg.cond(M)
    if cond > cond_threshold or abs(np.linalg.det(M)) < 1e-10:
        return tau_obs.copy(), se_obs.copy()  # fallback to naive if ill-conditioned
    Mi = np.linalg.inv(M)
    tau_c = Mi @ tau_obs  # corrected CATE
    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))  # propagated SE
    return tau_c, se_c
```

### D. Per-Subgroup vs Global:
- **Per-subgroup (EC-HTE stratified)**: 
  ```python
  for s in LABELS:
      tau_c_s, se_c_s = invert_mixing(M_sub[s], tau_obs[s], se_obs[s])
  ```
- **Global**:
  ```python
  tau_c_global, se_c_global = invert_mixing(M_global, tau_obs_pooled, se_obs_pooled)
  ```

### E. Six Methods Compared (exp027b, exp027, exp027c pattern):
1. **Oracle**: Use true Z, no correction
2. **EC-HTE true CM**: Z_hat forest + per-subgroup correction with true C_s
3. **EC-HTE estimated CM**: Z_hat forest + per-subgroup correction with estimated Ĉ_s
4. **Global true CM**: Z_hat forest + global correction with true C_bar
5. **Global estimated CM**: Z_hat forest + global correction with estimated Ĉ_bar
6. **Naive**: Z_hat forest, no correction

---

## **4. MONTE CARLO RUN STRUCTURE**

### Pattern across all exp*.py files:

```python
# Setup
N_MC = 50 or 100  # number of Monte Carlo replications
seeds = list(range(42, 42 + N_MC))
n_experts = [50, 100, 250, 500]
k_subgroups = [2, 4]

# Main loop
all_rows = []
t0 = time.time()

for ne in n_experts:
    for seed in seeds:
        result = run_one_mc(ne, seed)
        if result is not None:
            all_rows.extend(result)
        
        if count % max(1, total // 10) == 0:
            el = time.time() - t0
            eta = el / count * (total - count)
            print(f"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s")

elapsed = time.time() - t0
print(f"\nDone in {elapsed:.1f}s ({len(all_rows)} successful MC runs)\n")

df_raw = pd.DataFrame(all_rows)
df_agg = aggregate(df_raw)
```

### Per-MC run structure (example from exp027b):
```python
def run_one_mc(seed):
    Y, T, Z_true, Z_hat, S, expert_mask = generate_data(seed)
    
    # Fit two forests: oracle (Z_true) and Z_hat
    X_oracle = np.column_stack([Z_true, S])
    X_zhat = np.column_stack([Z_hat, S])
    
    oracle_cate, oracle_se = fit_cf_and_predict(Y, T, X_oracle, X_eval)
    zhat_cate, zhat_se = fit_cf_and_predict(Y, T, X_zhat, X_eval)
    
    # Estimate CMs (true and estimated)
    M_true_sub = {s: build_mixing_matrix(true_confusion_matrix(PI[s])) for s in range(K)}
    M_est_sub = {s: ... for s in range(K)}
    
    # Per-subgroup corrections
    rows = []
    for s in range(K):
        for method_name, tau_hat, se_hat in methods:
            for z in [0, 1]:
                covers = 1 if ci_lo <= TAU_TRUE[z] <= ci_hi else 0
                rows.append({'method': method_name, 'subgroup': s, 'z': z, 
                            'tau_hat': tau_hat[z], 'se': se_hat[z], 
                            'covers': covers, 'mc_run': seed})
    return rows
```

---

## **5. RESULTS AGGREGATION AND SAVING**

### A. Aggregation Pattern:
```python
def aggregate_results(df):
    grp_cols = ['method', 'subgroup', 'z']
    rows = []
    for keys, g in df.groupby(grp_cols):
        method, subgroup, z = keys
        err = g['tau_hat'].values - g['tau_true'].values
        bias = err.mean()
        rmse = np.sqrt((err ** 2).mean())
        cov = g['covers'].mean()  # coverage of 95% CI
        se_mean = g['se'].mean()
        n_mc = len(g)
        rows.append({
            'method': method,
            'subgroup': int(subgroup),
            'z': int(z),
            'bias': bias,
            'rmse': rmse,
            'coverage': cov,
            'se_mean': se_mean,
            'mc_run_count': n_mc,
        })
    return pd.DataFrame(rows)
```

### B. Metrics Computed:
- **Bias**: mean(τ̂ - τ_true)
- **RMSE**: sqrt(mean((τ̂ - τ_true)²))
- **Coverage**: fraction of 95% CIs that contain true τ (1.96 * SE)
- **Mean SE**: average standard error across MC runs

### C. Output Files:
```python
os.makedirs('results', exist_ok=True)
df_agg.to_csv('results/exp_cf_oracle_coverage.csv', index=False)
df_raw.to_csv('results/exp_cf_oracle_coverage_raw.csv', index=False)

# Also artifact directory for ML research registry
artifacts_dir = os.path.expanduser('~/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/')
os.makedirs(artifacts_dir, exist_ok=True)
df_agg.to_csv(os.path.join(artifacts_dir, 'exp_name.csv'), index=False)
```

### D. Display Output:
```python
# Print summary tables
print("=" * 80)
print(f"{'Method':<28s} | {'Coverage':>8s} | {'|Bias|':>7s} | {'RMSE':>7s}")
print("-" * 80)
for method in method_order:
    sub = df_agg[df_agg['method'] == method]
    cov = sub['coverage'].mean()
    abs_bias = sub['bias'].abs().mean()
    rmse = sub['rmse'].mean()
    print(f"{method:<28s} | {cov:8.4f} | {abs_bias:7.4f} | {rmse:7.4f}")
```

---

## **6. SPECIAL PATTERNS**

### Bootstrap SE Analysis (exp_mf2_cf_bootstrap_se.py, exp_w4_bootstrap_se.py):
```python
# Resample expert labels to quantify CM estimation uncertainty
boot_taus = np.zeros((n_bootstrap, 2))
rng_boot = np.random.RandomState(seed * 1000 + 7)

for b in range(n_bootstrap):
    boot_idx = rng_boot.choice(n_exp, n_exp, replace=True)
    z_b, zh_b = z_exp[boot_idx], zt_exp[boot_idx]
    
    # Re-estimate CM from bootstrap sample
    C_b = estimate_cm(z_b, zh_b)
    M_b = build_mixing_matrix(C_b)
    tau_c_b, _, _ = invert_mixing(M_b, sub_obs[s], sub_se_obs[s])
    boot_taus[b] = tau_c_b

boot_se = np.nanstd(boot_taus, axis=0)  # SD across bootstrap samples
```

### Condition Number Guard:
```python
# All files check condition number to avoid ill-posed inversions
cond = np.linalg.cond(M)
if cond > 100:  # or cond_threshold parameter
    return tau_obs.copy(), se_obs.copy()  # fallback to naive
```

### Assumption A5 Violation Testing (exp_w8_a5_violation.py):
- Tests correlated heterogeneity: Δτ_s ⊥ δ_s or not
- Two configs: aligned (positive correlation), adversarial (negative)
- Methods: oracle, naive, global_corrected, ec_hte_mle, ec_hte_eb

---

## **7. KEY IMPLEMENTATION FILES BY PURPOSE**

| File | Purpose | DGP | K | n_expert | N_MC | Methods |
|------|---------|-----|---|----------|------|---------|
| exp_mf2_cf_bootstrap_se.py | Bootstrap SE vs plug-in | [0.05, 0.25] | 2 | [100, 250, 500] | 50 | Plugin, Bootstrap, Combined |
| exp027b_cf_oracle_k2.py | Oracle coverage (K=2) | [0.05, 0.25] | 2 | 250 | 100 | Oracle + 5 methods |
| exp027_cf_oracle_coverage.py | Oracle coverage (K=4) | [0.05, 0.10, 0.20, 0.30] | 4 | 500 | 100 | Oracle + 5 methods |
| exp027c_cf_oracle_mf2dgp.py | Oracle (MF2 DGP) | [0.05, 0.25] | 2 | 250 | 100 | Oracle + 5 methods |
| exp_w4_bootstrap_se.py | Bootstrap SE (W4) | [0.05, 0.25] | 2 | [50, 100, 250, 500] | 50 | Plugin, Bootstrap, Combined |
| exp_w8_a5_violation.py | A5 robustness | [0.05, 0.25] aligned/adversarial | 2 | [250, 500] | 50 | Oracle, Naive, Global, MLE, EB |
| exp001_hb_synthetic.py | HB estimation | Multiple regimes | [2, 4] | [50, 100, 250, 500, 1000, 2000] | 100 | Oracle, Naive, Global, MLE, HB |
| exp015_semi_real_cm.py | Real confusion matrices | From GPT-4.1 pilot | 4 | [100, 250, 500] | 100 | Oracle, Naive, Global, HB |
| exp017_rlearner.py | R-learner compatibility | [0.05, 0.20] | 2 | 500 | 50 | Oracle, Naive, Global, EC-HTE |

All files follow the same structural pattern: generate data → estimate CMs → apply DIM correction → evaluate coverage/bias/RMSE → save results.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "b609a588-2a98-4378-b1b6-c02e163949c2",
  "tool_use_result": {
    "status": "completed",
    "prompt": "In the project at /home/ubuntu/ec_hte_llm_annotation, I need to find and read the following files to understand existing code patterns:\n\n1. `exp_mf2_cf_bootstrap_se.py` - has DIM estimator implementation\n2. `exp027b_cf_oracle_k2.py` - has DIM estimator implementation\n3. Any other exp*.py files that show the pattern for MC simulation, confusion matrix estimation, and CATE estimation\n\nSearch broadly: check root, src/, experiments/, scripts/, etc.\n\nFor each file found, read it fully and report:\n- The DGP (data generating process) setup\n- How confusion matrices are estimated (global, stratified, HB)\n- How CATE is estimated using DIM\n- How MC runs are structured\n- How results are saved\n\nBe very thorough - read the complete files.",
    "agentId": "a8238e369993613e3",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I have enough material to provide a comprehensive summary. Let me compile all the findings:\n\n## Summary: EC-HTE Code Patterns Analysis\n\nI've found and analyzed the requested files plus several related experiments. Here's a comprehensive report of the patterns:\n\n### **File Locations**\n\n1. **exp_mf2_cf_bootstrap_se.py** - `/home/ubuntu/ec_hte_llm_annotation/exp_mf2_cf_bootstrap_se.py`\n2. **exp027b_cf_oracle_k2.py** - `/home/ubuntu/ec_hte_llm_annotation/exp027b_cf_oracle_k2.py`\n3. **Related experiments**: exp027_cf_oracle_coverage.py, exp027c_cf_oracle_mf2dgp.py, exp_w4_bootstrap_se.py, exp_w8_a5_violation.py, exp001_hb_synthetic.py, exp015_semi_real_cm.py, exp017_rlearner.py\n\n---\n\n## **1. DATA GENERATING PROCESS (DGP) SETUP**\n\n### Common DGP Components:\n- **N = 5000** (sample size, constant across all files)\n- **K = 2 or 4** (number of subgroups)\n- **Binary treatment T**: `T ~ Bernoulli(0.5)`\n- **Binary confounder/variable Z**: `Z ~ Bernoulli(0.5)` (true)\n- **Subgroup assignment S**: Either categorical (0 to K-1) or string labels (A/B/C/D or S0/S1...)\n- **Covariates X**: `X ~ N(0, 1)` with shape (N, 5) or similar\n\n### Outcome Generation:\n```python\ntau = np.where(Z == 1, TAU_Z1, TAU_Z0)  # Treatment effect depends on Z\nbaseline = 1.0 + 0.5 * Z  # or similar offset\nY = baseline + tau * T + 0.5 * X[:, 0] + N(0, 1)  # outcome with treatment effect\n```\n\n### Misclassification of Z:\n- **Per-subgroup misclassification rates**: π_s varies by subgroup s\n  - exp_mf2: π = [0.05, 0.25]\n  - exp027b: π = [0.05, 0.25]\n  - exp001: K=2 has π = [0.25, 0.05] (extreme), [0.15, 0.10] (moderate), [0.12, 0.12] (homogeneous)\n  \n```python\nZ_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)  # flip with probability π_s\n```\n\n### Expert Sample:\n- **n_expert** ∈ {50, 100, 250, 500, 1000, 2000} (varies by experiment)\n- Random subset: `expert_mask = np.zeros(N, dtype=bool); expert_mask[idx] = True`\n\n---\n\n## **2. CONFUSION MATRIX ESTIMATION**\n\n### Three estimation strategies shown:\n\n#### **A. Laplace-Smoothed MLE (Empirical)**\n```python\ndef estimate_cm(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for z in [0, 1]:\n        mask = z_true == z\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[z, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n```\n- **Format**: C[z_true, z_hat] = P(Z_hat = zh | Z = z)\n- **Smoothing**: Add 1 to numerator, add 2 to denominator (Laplace)\n\n#### **B. Hierarchical Bayesian (Empirical Bayes + Gibbs)**\n- Used in exp001_hb_synthetic.py, exp015_semi_real_cm.py\n- Dirichlet priors with shared hyperparameter α\n- Gibbs sampler or empirical Bayes optimization\n- Better for small expert budgets\n\n#### **C. Three estimation levels:**\n\n1. **Global** (pooled across all subgroups):\n   ```python\n   C_global = estimate_cm(Z_true[expert_mask], Z_hat[expert_mask])\n   ```\n\n2. **Stratified/Per-subgroup** (HB approach):\n   ```python\n   for s in range(K):\n       mask_s = expert_mask & (S == s)\n       if mask_s.sum() >= 4:\n           C_s = estimate_cm(Z_true[mask_s], Z_hat[mask_s])\n       else:\n           C_s = estimate_cm(Z_true[expert_mask], Z_hat[expert_mask])  # fallback\n   ```\n\n3. **Oracle** (known true parameters from DGP):\n   ```python\n   def true_confusion_matrix(pi_s):\n       return np.array([[1 - pi_s, pi_s],\n                        [pi_s, 1 - pi_s]])\n   ```\n\n---\n\n## **3. CATE ESTIMATION USING DIMENSION INVERSION (DIM)**\n\n### A. Mixing Matrix Construction\n```python\ndef build_mixing_matrix(C):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        cs = C[0, zh] + C[1, zh]\n        M[zh, 0] = C[0, zh] / cs if cs > 0 else 0.5\n        M[zh, 1] = C[1, zh] / cs if cs > 0 else 0.5\n    return M\n```\n- **M[z_hat, z]** = P(Z = z | Z_hat = z_hat) via Bayes rule\n- Assumes P(Z=0) = P(Z=1) = 0.5\n\n### B. Observed CATE (from Z_hat):\n- **Difference-in-means**: τ̂(z_hat) = E[Y | T=1, Z_hat=z] - E[Y | T=0, Z_hat=z]\n- Or **CausalForestDML** directly on Z_hat:\n  ```python\n  cf = CausalForestDML(\n      model_y=LinearRegression(),\n      model_t=LogisticRegression(solver='lbfgs'),\n      discrete_treatment=True,\n      n_estimators=200,\n      min_samples_leaf=20,\n      random_state=seed,\n  )\n  cf.fit(Y, T, X=X_features)\n  cate_vals = cf.effect(X_features).flatten()\n  ```\n\n### C. Correction via M⁻¹ (DIM Estimator)\n```python\ndef invert_mixing(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold or abs(np.linalg.det(M)) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()  # fallback to naive if ill-conditioned\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs  # corrected CATE\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))  # propagated SE\n    return tau_c, se_c\n```\n\n### D. Per-Subgroup vs Global:\n- **Per-subgroup (EC-HTE stratified)**: \n  ```python\n  for s in LABELS:\n      tau_c_s, se_c_s = invert_mixing(M_sub[s], tau_obs[s], se_obs[s])\n  ```\n- **Global**:\n  ```python\n  tau_c_global, se_c_global = invert_mixing(M_global, tau_obs_pooled, se_obs_pooled)\n  ```\n\n### E. Six Methods Compared (exp027b, exp027, exp027c pattern):\n1. **Oracle**: Use true Z, no correction\n2. **EC-HTE true CM**: Z_hat forest + per-subgroup correction with true C_s\n3. **EC-HTE estimated CM**: Z_hat forest + per-subgroup correction with estimated Ĉ_s\n4. **Global true CM**: Z_hat forest + global correction with true C_bar\n5. **Global estimated CM**: Z_hat forest + global correction with estimated Ĉ_bar\n6. **Naive**: Z_hat forest, no correction\n\n---\n\n## **4. MONTE CARLO RUN STRUCTURE**\n\n### Pattern across all exp*.py files:\n\n```python\n# Setup\nN_MC = 50 or 100  # number of Monte Carlo replications\nseeds = list(range(42, 42 + N_MC))\nn_experts = [50, 100, 250, 500]\nk_subgroups = [2, 4]\n\n# Main loop\nall_rows = []\nt0 = time.time()\n\nfor ne in n_experts:\n    for seed in seeds:\n        result = run_one_mc(ne, seed)\n        if result is not None:\n            all_rows.extend(result)\n        \n        if count % max(1, total // 10) == 0:\n            el = time.time() - t0\n            eta = el / count * (total - count)\n            print(f\"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s\")\n\nelapsed = time.time() - t0\nprint(f\"\\nDone in {elapsed:.1f}s ({len(all_rows)} successful MC runs)\\n\")\n\ndf_raw = pd.DataFrame(all_rows)\ndf_agg = aggregate(df_raw)\n```\n\n### Per-MC run structure (example from exp027b):\n```python\ndef run_one_mc(seed):\n    Y, T, Z_true, Z_hat, S, expert_mask = generate_data(seed)\n    \n    # Fit two forests: oracle (Z_true) and Z_hat\n    X_oracle = np.column_stack([Z_true, S])\n    X_zhat = np.column_stack([Z_hat, S])\n    \n    oracle_cate, oracle_se = fit_cf_and_predict(Y, T, X_oracle, X_eval)\n    zhat_cate, zhat_se = fit_cf_and_predict(Y, T, X_zhat, X_eval)\n    \n    # Estimate CMs (true and estimated)\n    M_true_sub = {s: build_mixing_matrix(true_confusion_matrix(PI[s])) for s in range(K)}\n    M_est_sub = {s: ... for s in range(K)}\n    \n    # Per-subgroup corrections\n    rows = []\n    for s in range(K):\n        for method_name, tau_hat, se_hat in methods:\n            for z in [0, 1]:\n                covers = 1 if ci_lo <= TAU_TRUE[z] <= ci_hi else 0\n                rows.append({'method': method_name, 'subgroup': s, 'z': z, \n                            'tau_hat': tau_hat[z], 'se': se_hat[z], \n                            'covers': covers, 'mc_run': seed})\n    return rows\n```\n\n---\n\n## **5. RESULTS AGGREGATION AND SAVING**\n\n### A. Aggregation Pattern:\n```python\ndef aggregate_results(df):\n    grp_cols = ['method', 'subgroup', 'z']\n    rows = []\n    for keys, g in df.groupby(grp_cols):\n        method, subgroup, z = keys\n        err = g['tau_hat'].values - g['tau_true'].values\n        bias = err.mean()\n        rmse = np.sqrt((err ** 2).mean())\n        cov = g['covers'].mean()  # coverage of 95% CI\n        se_mean = g['se'].mean()\n        n_mc = len(g)\n        rows.append({\n            'method': method,\n            'subgroup': int(subgroup),\n            'z': int(z),\n            'bias': bias,\n            'rmse': rmse,\n            'coverage': cov,\n            'se_mean': se_mean,\n            'mc_run_count': n_mc,\n        })\n    return pd.DataFrame(rows)\n```\n\n### B. Metrics Computed:\n- **Bias**: mean(τ̂ - τ_true)\n- **RMSE**: sqrt(mean((τ̂ - τ_true)²))\n- **Coverage**: fraction of 95% CIs that contain true τ (1.96 * SE)\n- **Mean SE**: average standard error across MC runs\n\n### C. Output Files:\n```python\nos.makedirs('results', exist_ok=True)\ndf_agg.to_csv('results/exp_cf_oracle_coverage.csv', index=False)\ndf_raw.to_csv('results/exp_cf_oracle_coverage_raw.csv', index=False)\n\n# Also artifact directory for ML research registry\nartifacts_dir = os.path.expanduser('~/.agent-ml-research-idea_gen_0520/projects/ec_hte_llm_annotation/artifacts/')\nos.makedirs(artifacts_dir, exist_ok=True)\ndf_agg.to_csv(os.path.join(artifacts_dir, 'exp_name.csv'), index=False)\n```\n\n### D. Display Output:\n```python\n# Print summary tables\nprint(\"=\" * 80)\nprint(f\"{'Method':<28s} | {'Coverage':>8s} | {'|Bias|':>7s} | {'RMSE':>7s}\")\nprint(\"-\" * 80)\nfor method in method_order:\n    sub = df_agg[df_agg['method'] == method]\n    cov = sub['coverage'].mean()\n    abs_bias = sub['bias'].abs().mean()\n    rmse = sub['rmse'].mean()\n    print(f\"{method:<28s} | {cov:8.4f} | {abs_bias:7.4f} | {rmse:7.4f}\")\n```\n\n---\n\n## **6. SPECIAL PATTERNS**\n\n### Bootstrap SE Analysis (exp_mf2_cf_bootstrap_se.py, exp_w4_bootstrap_se.py):\n```python\n# Resample expert labels to quantify CM estimation uncertainty\nboot_taus = np.zeros((n_bootstrap, 2))\nrng_boot = np.random.RandomState(seed * 1000 + 7)\n\nfor b in range(n_bootstrap):\n    boot_idx = rng_boot.choice(n_exp, n_exp, replace=True)\n    z_b, zh_b = z_exp[boot_idx], zt_exp[boot_idx]\n    \n    # Re-estimate CM from bootstrap sample\n    C_b = estimate_cm(z_b, zh_b)\n    M_b = build_mixing_matrix(C_b)\n    tau_c_b, _, _ = invert_mixing(M_b, sub_obs[s], sub_se_obs[s])\n    boot_taus[b] = tau_c_b\n\nboot_se = np.nanstd(boot_taus, axis=0)  # SD across bootstrap samples\n```\n\n### Condition Number Guard:\n```python\n# All files check condition number to avoid ill-posed inversions\ncond = np.linalg.cond(M)\nif cond > 100:  # or cond_threshold parameter\n    return tau_obs.copy(), se_obs.copy()  # fallback to naive\n```\n\n### Assumption A5 Violation Testing (exp_w8_a5_violation.py):\n- Tests correlated heterogeneity: Δτ_s ⊥ δ_s or not\n- Two configs: aligned (positive correlation), adversarial (negative)\n- Methods: oracle, naive, global_corrected, ec_hte_mle, ec_hte_eb\n\n---\n\n## **7. KEY IMPLEMENTATION FILES BY PURPOSE**\n\n| File | Purpose | DGP | K | n_expert | N_MC | Methods |\n|------|---------|-----|---|----------|------|---------|\n| exp_mf2_cf_bootstrap_se.py | Bootstrap SE vs plug-in | [0.05, 0.25] | 2 | [100, 250, 500] | 50 | Plugin, Bootstrap, Combined |\n| exp027b_cf_oracle_k2.py | Oracle coverage (K=2) | [0.05, 0.25] | 2 | 250 | 100 | Oracle + 5 methods |\n| exp027_cf_oracle_coverage.py | Oracle coverage (K=4) | [0.05, 0.10, 0.20, 0.30] | 4 | 500 | 100 | Oracle + 5 methods |\n| exp027c_cf_oracle_mf2dgp.py | Oracle (MF2 DGP) | [0.05, 0.25] | 2 | 250 | 100 | Oracle + 5 methods |\n| exp_w4_bootstrap_se.py | Bootstrap SE (W4) | [0.05, 0.25] | 2 | [50, 100, 250, 500] | 50 | Plugin, Bootstrap, Combined |\n| exp_w8_a5_violation.py | A5 robustness | [0.05, 0.25] aligned/adversarial | 2 | [250, 500] | 50 | Oracle, Naive, Global, MLE, EB |\n| exp001_hb_synthetic.py | HB estimation | Multiple regimes | [2, 4] | [50, 100, 250, 500, 1000, 2000] | 100 | Oracle, Naive, Global, MLE, HB |\n| exp015_semi_real_cm.py | Real confusion matrices | From GPT-4.1 pilot | 4 | [100, 250, 500] | 100 | Oracle, Naive, Global, HB |\n| exp017_rlearner.py | R-learner compatibility | [0.05, 0.20] | 2 | 500 | 50 | Oracle, Naive, Global, EC-HTE |\n\nAll files follow the same structural pattern: generate data → estimate CMs → apply DIM correction → evaluate coverage/bias/RMSE → save results."
      }
    ],
    "totalDurationMs": 53064,
    "totalTokens": 73122,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4571,
      "cache_read_input_tokens": 63871,
      "output_tokens": 4674,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4571
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 4674,
          "cache_read_input_tokens": 63871,
          "cache_creation_input_tokens": 4571,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4571,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 10,
      "searchCount": 1,
      "bashCount": 1,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Excellent, I have a comprehensive understanding of the existing codebase. Now let me read one of the key reference files directly to get the exact code patterns, especially `exp027b_cf_oracle_k2.py` and `exp_w8_a5_violation.py` (since A5 violation testing is closest to what we need for A1 sensitivity).

Let me also read `exp_mf2_cf_bootstrap_se.py` for the DIM estimator details.

Actually, I have enough from the agent's summary. Let me now write the exp029 script. Let me think through the design:


I'm setting up a data generating process with 5000 observations and 2 subgroups, where treatment is randomly assigned and outcomes follow a normal distribution with heterogeneous treatment effects across subgroups (0.0 and 0.3 respectively). Then I'm introducing misclassification of the subgroup assignment with A1 violation, using base misclassification rates of 5% and 25% that I'll vary across different sensitivity parameters.

For estimation, I'm collecting 250 expert labels through stratified sampling and comparing four methods—naive, global, stratified MLE, and hierarchical Bayes—using a simple difference-in-means estimator that computes treatment effects within each misclassified subgroup and applies confusion matrix corrections.

Now I'm clarifying the setup: the true treatment effect τ_s varies by subgroup S, while Z is a separate binary variable that gets misclassified. I need to make sure I'm computing the conditional average treatment effect E[Y(1) - Y(0) | Z=z] correctly for each subgroup, accounting for how the misclassification affects the estimation. Looking at the DGP setup more carefully now—there are two subgroups with equal weight, true treatment effects that differ dramatically between them (zero effect in subgroup 0 versus 0.3 in subgroup 1), and the misclassification rates are asymmetric, with subgroup 1 having much higher error rates than subgroup 0. So Z is actually the subgroup itself, not some separate variable—it's what determines the heterogeneous treatment effects, with τ(Z=0) = 0.0 and τ(Z=1) = 0.3. The misclassification rates π_s are indexed by Z, and when we observe Z_hat instead of true Z, we're seeing a mixture of the true treatment effects that gets distorted by the confusion matrix relating observed to true classifications.

The DIM estimator works by computing the observed conditional average treatment effects for each observed subgroup, then applying the inverse confusion matrix to correct back to the true effects. Now I need to implement the script with all four methods: naive estimation using Z_hat directly, a global correction approach, and presumably two others.

Looking at the reference implementation, the hierarchical Bayes method uses Dirichlet priors with a shared hyperparameter and either Gibbs sampling or empirical Bayes optimization to estimate the confusion matrices per subgroup. Let me examine the actual code to understand the exact implementation details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "e8048426-fb93-4e7a-bb93-0901e3641d76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHTeSUyGujzyme2Ve8ZfUy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4988,
      "cache_read_input_tokens": 18919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4988
      },
      "output_tokens": 29,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 47_

Now let me read the key reference files for exact implementation details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "21faaa44-fbb7-430b-b5bc-7c924513b39e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHTeSUyGujzyme2Ve8ZfUy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4988,
      "cache_read_input_tokens": 18919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4988
      },
      "output_tokens": 29,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_018ZaUAFrDc9xYPwKBrXQx5e`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp027b_cf_oracle_k2.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "2e027483-ea4c-45d1-b52f-8d7056c96605",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHTeSUyGujzyme2Ve8ZfUy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4988,
      "cache_read_input_tokens": 18919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4988
      },
      "output_tokens": 29,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-22T16:17:09.177Z_

<details><summary>↩ Tool result · `toolu_018ZaUAFrDc9xYPwKBrXQx5e`</summary>

```text
1	#!/usr/bin/env python3
2	"""exp027b_cf_oracle_k2.py — CausalForest Oracle Coverage, K=2 extreme (exp-027b)
3	
4	K=2 variant of exp-027 to match the paper's DGP for the 83-85% coverage gap analysis.
5	
6	Six methods compared:
7	  1. Oracle (true Z): CausalForestDML with Z_true, no correction
8	  2. EC-HTE true CM: Z_hat forest + per-subgroup correction with true C_s
9	  3. EC-HTE estimated CM: Z_hat forest + per-subgroup correction with estimated C_s (HB)
10	  4. Global true CM: Z_hat forest + global correction with true C_bar
11	  5. Global estimated CM: Z_hat forest + global correction with estimated C_bar
12	  6. Naive: Z_hat forest, no correction
13	
14	DGP: K=2, pi=[0.05,0.25], weights=[0.5,0.5], tau(0)=0, tau(1)=0.3, N=5000, n_expert=250
15	Output: results/exp_cf_oracle_coverage_k2.csv
16	"""
17	
18	import os
19	import time
20	import warnings
21	
22	import numpy as np
23	import pandas as pd
24	from econml.dml import CausalForestDML
25	from sklearn.linear_model import LinearRegression, LogisticRegression
26	
27	warnings.filterwarnings('ignore')
28	
29	N = 5000
30	K = 2
31	N_EXPERT = 250
32	PI = [0.05, 0.25]
33	TAU_TRUE = {0: 0.0, 1: 0.3}
34	SUB_WEIGHTS = [0.5, 0.5]
35	N_MC = 100
36	BASE_SEED = 42
37	
38	
39	def generate_data(seed):
40	    rng = np.random.RandomState(seed)
41	    S = rng.randint(0, K, N)
42	    T = rng.binomial(1, 0.5, N)
43	    Z_true = rng.binomial(1, 0.5, N)
44	
45	    Z_hat = Z_true.copy()
46	    for s in range(K):
47	        mask_s = S == s
48	        flip = rng.binomial(1, PI[s], mask_s.sum())
49	        Z_hat[mask_s] = np.where(flip, 1 - Z_true[mask_s], Z_true[mask_s])
50	
51	    tau = np.where(Z_true == 1, TAU_TRUE[1], TAU_TRUE[0])
52	    baseline = 1.0 + 0.5 * Z_true
53	    Y = baseline + tau * T + rng.normal(0, 1, N)
54	
55	    expert_idx = rng.choice(N, N_EXPERT, replace=False)
56	    expert_mask = np.zeros(N, dtype=bool)
57	    expert_mask[expert_idx] = True
58	
59	    return Y, T, Z_true, Z_hat, S, expert_mask
60	
61	
62	def compute_confusion_matrix(z_true, z_hat):
63	    C = np.zeros((2, 2))
64	    for z in [0, 1]:
65	        mz = z_true == z
66	        C[z, 0] = (z_hat[mz] == 0).sum() + 1
67	        C[z, 1] = (z_hat[mz] == 1).sum() + 1
68	    return C / C.sum(axis=1, keepdims=True)
69	
70	
71	def build_mixing_matrix(C):
72	    M = np.zeros((2, 2))
73	    for zh in [0, 1]:
74	        cs = C[0, zh] + C[1, zh]
75	        if cs > 0:
76	            M[zh, 0] = C[0, zh] / cs
77	            M[zh, 1] = C[1, zh] / cs
78	        else:
79	            M[zh, :] = 0.5
80	    return M
81	
82	
83	def invert_mixing(M, tau_obs, se_obs, cond_threshold=100):
84	    cond = np.linalg.cond(M)
85	    if cond > cond_threshold or abs(np.linalg.det(M)) < 1e-10:
86	        return tau_obs.copy(), se_obs.copy()
87	    Mi = np.linalg.inv(M)
88	    tau_c = Mi @ tau_obs
89	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
90	    return tau_c, se_c
91	
92	
93	def true_confusion_matrix(pi_s):
94	    return np.array([[1 - pi_s, pi_s],
95	                     [pi_s, 1 - pi_s]])
96	
97	
98	def fit_cf_and_predict(Y, T, X_features, X_eval):
99	    cf = CausalForestDML(
100	        model_y=LinearRegression(),
101	        model_t=LogisticRegression(solver='lbfgs'),
102	        discrete_treatment=True,
103	        n_estimators=200,
104	        min_samples_leaf=20,
105	        random_state=42,
106	    )
107	    cf.fit(Y, T, X=X_features, W=None)
108	
109	    cate_vals = cf.effect(X_eval).flatten()
110	    try:
111	        inf = cf.effect_inference(X_eval)
112	        se_raw = inf.stderr
113	        if hasattr(se_raw, 'values'):
114	            se_raw = se_raw.values
115	        se_vals = np.asarray(se_raw).flatten()
116	    except Exception:
117	        se_vals = np.full(len(X_eval), np.nan)
118	
119	    return cate_vals, se_vals
120	
121	
122	def run_one_mc(seed):
123	    Y, T, Z_true, Z_hat, S, expert_mask = generate_data(seed)
124	
125	    X_eval = np.array([[z, s] for s in range(K) for z in [0, 1]], dtype=float)
126	
127	    X_oracle = np.column_stack([Z_true, S]).astype(float)
128	    oracle_cate, oracle_se = fit_cf_and_predict(Y, T, X_oracle, X_eval)
129	
130	    X_zhat = np.column_stack([Z_hat, S]).astype(float)
131	    zhat_cate, zhat_se = fit_cf_and_predict(Y, T, X_zhat, X_eval)
132	
133	    M_true_sub = {}
134	    for s in range(K):
135	        C_s_true = true_confusion_matrix(PI[s])
136	        M_true_sub[s] = build_mixing_matrix(C_s_true)
137	
138	    C_global_true = sum(SUB_WEIGHTS[s] * true_confusion_matrix(PI[s]) for s in range(K))
139	    M_global_true = build_mixing_matrix(C_global_true)
140	
141	    M_est_sub = {}
142	    for s in range(K):
143	        mask_s = expert_mask & (S == s)
144	        if mask_s.sum() >= 4:
145	            C_s = compute_confusion_matrix(Z_true[mask_s], Z_hat[mask_s])
146	        else:
147	            C_s = np.array([[0.5, 0.5], [0.5, 0.5]])
148	        M_est_sub[s] = build_mixing_matrix(C_s)
149	
150	    C_global_est = compute_confusion_matrix(Z_true[expert_mask], Z_hat[expert_mask])
151	    M_global_est = build_mixing_matrix(C_global_est)
152	
153	    rows = []
154	    for s in range(K):
155	        idx_z0 = s * 2
156	        idx_z1 = s * 2 + 1
157	
158	        o_tau = np.array([oracle_cate[idx_z0], oracle_cate[idx_z1]])
159	        o_se = np.array([oracle_se[idx_z0], oracle_se[idx_z1]])
160	
161	        tau_obs = np.array([zhat_cate[idx_z0], zhat_cate[idx_z1]])
162	        se_obs = np.array([zhat_se[idx_z0], zhat_se[idx_z1]])
163	
164	        tau_ec_true, se_ec_true = invert_mixing(M_true_sub[s], tau_obs, se_obs)
165	        tau_ec_est, se_ec_est = invert_mixing(M_est_sub[s], tau_obs, se_obs)
166	        tau_gl_true, se_gl_true = invert_mixing(M_global_true, tau_obs, se_obs)
167	        tau_gl_est, se_gl_est = invert_mixing(M_global_est, tau_obs, se_obs)
168	
169	        methods = [
170	            ('Oracle', o_tau, o_se),
171	            ('EC-HTE true CM', tau_ec_true, se_ec_true),
172	            ('EC-HTE estimated CM', tau_ec_est, se_ec_est),
173	            ('Global true CM', tau_gl_true, se_gl_true),
174	            ('Global estimated CM', tau_gl_est, se_gl_est),
175	            ('Naive', tau_obs, se_obs),
176	        ]
177	
178	        for method_name, tau_hat, se_hat in methods:
179	            for zi, z in enumerate([0, 1]):
180	                th = tau_hat[zi]
181	                se = se_hat[zi]
182	                if np.isnan(se) or np.isnan(th):
183	                    covers = np.nan
184	                else:
185	                    ci_lo = th - 1.96 * se
186	                    ci_hi = th + 1.96 * se
187	                    covers = int(ci_lo <= TAU_TRUE[z] <= ci_hi)
188	                rows.append({
189	                    'method': method_name,
190	                    'subgroup': s,
191	                    'z': z,
192	                    'tau_hat': th,
193	                    'se': se,
194	                    'tau_true': TAU_TRUE[z],
195	                    'covers': covers,
196	                    'mc_run': seed,
197	                })
198	
199	    return rows
200	
201	
202	def aggregate_results(df):
203	    grp_cols = ['method', 'subgroup', 'z']
204	    rows = []
205	    for keys, g in df.groupby(grp_cols):
206	        method, subgroup, z = keys
207	        err = g['tau_hat'].values - g['tau_true'].values
208	        bias = err.mean()
209	        rmse = np.sqrt((err ** 2).mean())
210	        cov = g['covers'].mean()
211	        se_mean = g['se'].mean()
212	        n_mc = len(g)
213	        rows.append({
214	            'method': method,
215	            'subgroup': int(subgroup),
216	            'z': int(z),
217	            'bias': bias,
218	            'rmse': rmse,
219	            'coverage': cov,
220	            'se_mean': se_mean,
221	            'mc_run_count': n_mc,
222	        })
223	    return pd.DataFrame(rows)
224	
225	
226	def print_summary(df_agg):
227	    method_order = [
228	        'Oracle', 'EC-HTE true CM', 'EC-HTE estimated CM',
229	        'Global true CM', 'Global estimated CM', 'Naive',
230	    ]
231	
232	    print("\n" + "=" * 80)
233	    print("exp-027b CausalForest Oracle Coverage (K=2, extreme)")
234	    print("=" * 80)
235	
236	    print(f"\n{'Method':<28s} | {'|Bias|':>7s} | {'RMSE':>7s} | {'Coverage':>8s} | {'Mean SE':>7s}")
237	    print(f"{'-'*28}-+-{'-'*7}-+-{'-'*7}-+-{'-'*8}-+-{'-'*7}")
238	
239	    for method in method_order:
240	        sub = df_agg[df_agg['method'] == method]
241	        abs_bias = sub['bias'].abs().mean()
242	        rmse = sub['rmse'].mean()
243	        cov = sub['coverage'].mean()
244	        se_mean = sub['se_mean'].mean()
245	        print(f"{method:<28s} | {abs_bias:7.4f} | {rmse:7.4f} | {cov:8.4f} | {se_mean:7.4f}")
246	
247	    print(f"\n\nPer-subgroup detail:")
248	    print(f"{'Method':<28s} | {'Sub':>3s} | {'z':>1s} | {'Bias':>8s} | {'RMSE':>7s} | {'Coverage':>8s} | {'Mean SE':>7s}")
249	    print(f"{'-'*28}-+-{'-'*3}-+-{'-'*1}-+-{'-'*8}-+-{'-'*7}-+-{'-'*8}-+-{'-'*7}")
250	
251	    for method in method_order:
252	        for s in range(K):
253	            for z in [0, 1]:
254	                r = df_agg[(df_agg['method'] == method) &
255	                           (df_agg['subgroup'] == s) &
256	                           (df_agg['z'] == z)]
257	                if r.empty:
258	                    continue
259	                r = r.iloc[0]
260	                print(f"{method:<28s} | {s:>3d} | {z:>1d} | {r['bias']:8.4f} | {r['rmse']:7.4f} | {r['coverage']:8.4f} | {r['se_mean']:7.4f}")
261	        print()
262	
263	    print("\n" + "=" * 80)
264	    print("INTERPRETATION")
265	    print("=" * 80)
266	    oracle_cov = df_agg[df_agg['method'] == 'Oracle']['coverage'].mean()
267	    ec_true_cov = df_agg[df_agg['method'] == 'EC-HTE true CM']['coverage'].mean()
268	    ec_est_cov = df_agg[df_agg['method'] == 'EC-HTE estimated CM']['coverage'].mean()
269	    print(f"  Oracle coverage:           {oracle_cov:.4f}")
270	    print(f"  EC-HTE true CM coverage:   {ec_true_cov:.4f}")
271	    print(f"  EC-HTE estimated coverage: {ec_est_cov:.4f}")
272	    print()
273	    if oracle_cov < 0.90:
274	        print("  -> Oracle < 90%: CF SE is inherently under-calibrated")
275	    else:
276	        print("  -> Oracle >= 90%: CF SE is reasonably calibrated")
277	    if abs(ec_true_cov - ec_est_cov) < 0.03:
278	        print("  -> EC-HTE true CM ~ estimated CM: gap is NOT from CM estimation error")
279	        print("     Coverage gap comes from CF inherent SE under-calibration")
280	    elif ec_true_cov > ec_est_cov + 0.05:
281	        print("  -> EC-HTE true CM >> estimated CM: CM estimation error contributes to gap")
282	    else:
283	        print("  -> Mixed signal: both CF SE calibration and CM estimation may contribute")
284	
285	
286	if __name__ == '__main__':
287	    print(f"exp-027b CausalForest Oracle Coverage (K=2, extreme)")
288	    print(f"N={N}, K={K}, pi={PI}, weights={SUB_WEIGHTS}")
289	    print(f"tau(0)={TAU_TRUE[0]}, tau(1)={TAU_TRUE[1]}")
290	    print(f"n_expert={N_EXPERT}, N_MC={N_MC}, seed_base={BASE_SEED}")
291	
292	    print("\nTiming single run...")
293	    t_test = time.time()
294	    _ = run_one_mc(seed=9999)
295	    t_per = time.time() - t_test
296	    print(f"  {t_per:.2f}s/run (2 forest fits per run)")
297	    print(f"  Estimated total: {t_per * N_MC:.0f}s ({t_per * N_MC / 60:.1f} min)\n")
298	
299	    all_rows = []
300	    t0 = time.time()
301	
302	    for mc in range(N_MC):
303	        seed = BASE_SEED + mc
304	        try:
305	            rows = run_one_mc(seed)
306	            all_rows.extend(rows)
307	        except Exception as e:
308	            print(f"  WARN: mc={mc} seed={seed} failed: {e}")
309	
310	        if (mc + 1) % 10 == 0:
311	            el = time.time() - t0
312	            eta = el / (mc + 1) * (N_MC - mc - 1)
313	            print(f"  [{mc+1}/{N_MC}] {el:.0f}s elapsed, ETA {eta:.0f}s")
314	
315	    elapsed = time.time() - t0
316	    print(f"\nDone: {elapsed:.1f}s ({N_MC} runs, {elapsed/N_MC:.1f}s/run)")
317	
318	    df_raw = pd.DataFrame(all_rows)
319	    df_agg = aggregate_results(df_raw)
320	
321	    os.makedirs('results', exist_ok=True)
322	    df_agg.to_csv('results/exp_cf_oracle_coverage_k2.csv', index=False)
323	    print(f"Saved: results/exp_cf_oracle_coverage_k2.csv ({len(df_agg)} rows)")
324	
325	    print_summary(df_agg)
326	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "d9a62b31-bc2e-4a32-bae0-225721e5589b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp027b_cf_oracle_k2.py",
      "content": "#!/usr/bin/env python3\n\"\"\"exp027b_cf_oracle_k2.py — CausalForest Oracle Coverage, K=2 extreme (exp-027b)\n\nK=2 variant of exp-027 to match the paper's DGP for the 83-85% coverage gap analysis.\n\nSix methods compared:\n  1. Oracle (true Z): CausalForestDML with Z_true, no correction\n  2. EC-HTE true CM: Z_hat forest + per-subgroup correction with true C_s\n  3. EC-HTE estimated CM: Z_hat forest + per-subgroup correction with estimated C_s (HB)\n  4. Global true CM: Z_hat forest + global correction with true C_bar\n  5. Global estimated CM: Z_hat forest + global correction with estimated C_bar\n  6. Naive: Z_hat forest, no correction\n\nDGP: K=2, pi=[0.05,0.25], weights=[0.5,0.5], tau(0)=0, tau(1)=0.3, N=5000, n_expert=250\nOutput: results/exp_cf_oracle_coverage_k2.csv\n\"\"\"\n\nimport os\nimport time\nimport warnings\n\nimport numpy as np\nimport pandas as pd\nfrom econml.dml import CausalForestDML\nfrom sklearn.linear_model import LinearRegression, LogisticRegression\n\nwarnings.filterwarnings('ignore')\n\nN = 5000\nK = 2\nN_EXPERT = 250\nPI = [0.05, 0.25]\nTAU_TRUE = {0: 0.0, 1: 0.3}\nSUB_WEIGHTS = [0.5, 0.5]\nN_MC = 100\nBASE_SEED = 42\n\n\ndef generate_data(seed):\n    rng = np.random.RandomState(seed)\n    S = rng.randint(0, K, N)\n    T = rng.binomial(1, 0.5, N)\n    Z_true = rng.binomial(1, 0.5, N)\n\n    Z_hat = Z_true.copy()\n    for s in range(K):\n        mask_s = S == s\n        flip = rng.binomial(1, PI[s], mask_s.sum())\n        Z_hat[mask_s] = np.where(flip, 1 - Z_true[mask_s], Z_true[mask_s])\n\n    tau = np.where(Z_true == 1, TAU_TRUE[1], TAU_TRUE[0])\n    baseline = 1.0 + 0.5 * Z_true\n    Y = baseline + tau * T + rng.normal(0, 1, N)\n\n    expert_idx = rng.choice(N, N_EXPERT, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return Y, T, Z_true, Z_hat, S, expert_mask\n\n\ndef compute_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for z in [0, 1]:\n        mz = z_true == z\n        C[z, 0] = (z_hat[mz] == 0).sum() + 1\n        C[z, 1] = (z_hat[mz] == 1).sum() + 1\n    return C / C.sum(axis=1, keepdims=True)\n\n\ndef build_mixing_matrix(C):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        cs = C[0, zh] + C[1, zh]\n        if cs > 0:\n            M[zh, 0] = C[0, zh] / cs\n            M[zh, 1] = C[1, zh] / cs\n        else:\n            M[zh, :] = 0.5\n    return M\n\n\ndef invert_mixing(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold or abs(np.linalg.det(M)) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\ndef true_confusion_matrix(pi_s):\n    return np.array([[1 - pi_s, pi_s],\n                     [pi_s, 1 - pi_s]])\n\n\ndef fit_cf_and_predict(Y, T, X_features, X_eval):\n    cf = CausalForestDML(\n        model_y=LinearRegression(),\n        model_t=LogisticRegression(solver='lbfgs'),\n        discrete_treatment=True,\n        n_estimators=200,\n        min_samples_leaf=20,\n        random_state=42,\n    )\n    cf.fit(Y, T, X=X_features, W=None)\n\n    cate_vals = cf.effect(X_eval).flatten()\n    try:\n        inf = cf.effect_inference(X_eval)\n        se_raw = inf.stderr\n        if hasattr(se_raw, 'values'):\n            se_raw = se_raw.values\n        se_vals = np.asarray(se_raw).flatten()\n    except Exception:\n        se_vals = np.full(len(X_eval), np.nan)\n\n    return cate_vals, se_vals\n\n\ndef run_one_mc(seed):\n    Y, T, Z_true, Z_hat, S, expert_mask = generate_data(seed)\n\n    X_eval = np.array([[z, s] for s in range(K) for z in [0, 1]], dtype=float)\n\n    X_oracle = np.column_stack([Z_true, S]).astype(float)\n    oracle_cate, oracle_se = fit_cf_and_predict(Y, T, X_oracle, X_eval)\n\n    X_zhat = np.column_stack([Z_hat, S]).astype(float)\n    zhat_cate, zhat_se = fit_cf_and_predict(Y, T, X_zhat, X_eval)\n\n    M_true_sub = {}\n    for s in range(K):\n        C_s_true = true_confusion_matrix(PI[s])\n        M_true_sub[s] = build_mixing_matrix(C_s_true)\n\n    C_global_true = sum(SUB_WEIGHTS[s] * true_confusion_matrix(PI[s]) for s in range(K))\n    M_global_true = build_mixing_matrix(C_global_true)\n\n    M_est_sub = {}\n    for s in range(K):\n        mask_s = expert_mask & (S == s)\n        if mask_s.sum() >= 4:\n            C_s = compute_confusion_matrix(Z_true[mask_s], Z_hat[mask_s])\n        else:\n            C_s = np.array([[0.5, 0.5], [0.5, 0.5]])\n        M_est_sub[s] = build_mixing_matrix(C_s)\n\n    C_global_est = compute_confusion_matrix(Z_true[expert_mask], Z_hat[expert_mask])\n    M_global_est = build_mixing_matrix(C_global_est)\n\n    rows = []\n    for s in range(K):\n        idx_z0 = s * 2\n        idx_z1 = s * 2 + 1\n\n        o_tau = np.array([oracle_cate[idx_z0], oracle_cate[idx_z1]])\n        o_se = np.array([oracle_se[idx_z0], oracle_se[idx_z1]])\n\n        tau_obs = np.array([zhat_cate[idx_z0], zhat_cate[idx_z1]])\n        se_obs = np.array([zhat_se[idx_z0], zhat_se[idx_z1]])\n\n        tau_ec_true, se_ec_true = invert_mixing(M_true_sub[s], tau_obs, se_obs)\n        tau_ec_est, se_ec_est = invert_mixing(M_est_sub[s], tau_obs, se_obs)\n        tau_gl_true, se_gl_true = invert_mixing(M_global_true, tau_obs, se_obs)\n        tau_gl_est, se_gl_est = invert_mixing(M_global_est, tau_obs, se_obs)\n\n        methods = [\n            ('Oracle', o_tau, o_se),\n            ('EC-HTE true CM', tau_ec_true, se_ec_true),\n            ('EC-HTE estimated CM', tau_ec_est, se_ec_est),\n            ('Global true CM', tau_gl_true, se_gl_true),\n            ('Global estimated CM', tau_gl_est, se_gl_est),\n            ('Naive', tau_obs, se_obs),\n        ]\n\n        for method_name, tau_hat, se_hat in methods:\n            for zi, z in enumerate([0, 1]):\n                th = tau_hat[zi]\n                se = se_hat[zi]\n                if np.isnan(se) or np.isnan(th):\n                    covers = np.nan\n                else:\n                    ci_lo = th - 1.96 * se\n                    ci_hi = th + 1.96 * se\n                    covers = int(ci_lo <= TAU_TRUE[z] <= ci_hi)\n                rows.append({\n                    'method': method_name,\n                    'subgroup': s,\n                    'z': z,\n                    'tau_hat': th,\n                    'se': se,\n                    'tau_true': TAU_TRUE[z],\n                    'covers': covers,\n                    'mc_run': seed,\n                })\n\n    return rows\n\n\ndef aggregate_results(df):\n    grp_cols = ['method', 'subgroup', 'z']\n    rows = []\n    for keys, g in df.groupby(grp_cols):\n        method, subgroup, z = keys\n        err = g['tau_hat'].values - g['tau_true'].values\n        bias = err.mean()\n        rmse = np.sqrt((err ** 2).mean())\n        cov = g['covers'].mean()\n        se_mean = g['se'].mean()\n        n_mc = len(g)\n        rows.append({\n            'method': method,\n            'subgroup': int(subgroup),\n            'z': int(z),\n            'bias': bias,\n            'rmse': rmse,\n            'coverage': cov,\n            'se_mean': se_mean,\n            'mc_run_count': n_mc,\n        })\n    return pd.DataFrame(rows)\n\n\ndef print_summary(df_agg):\n    method_order = [\n        'Oracle', 'EC-HTE true CM', 'EC-HTE estimated CM',\n        'Global true CM', 'Global estimated CM', 'Naive',\n    ]\n\n    print(\"\\n\" + \"=\" * 80)\n    print(\"exp-027b CausalForest Oracle Coverage (K=2, extreme)\")\n    print(\"=\" * 80)\n\n    print(f\"\\n{'Method':<28s} | {'|Bias|':>7s} | {'RMSE':>7s} | {'Coverage':>8s} | {'Mean SE':>7s}\")\n    print(f\"{'-'*28}-+-{'-'*7}-+-{'-'*7}-+-{'-'*8}-+-{'-'*7}\")\n\n    for method in method_order:\n        sub = df_agg[df_agg['method'] == method]\n        abs_bias = sub['bias'].abs().mean()\n        rmse = sub['rmse'].mean()\n        cov = sub['coverage'].mean()\n        se_mean = sub['se_mean'].mean()\n        print(f\"{method:<28s} | {abs_bias:7.4f} | {rmse:7.4f} | {cov:8.4f} | {se_mean:7.4f}\")\n\n    print(f\"\\n\\nPer-subgroup detail:\")\n    print(f\"{'Method':<28s} | {'Sub':>3s} | {'z':>1s} | {'Bias':>8s} | {'RMSE':>7s} | {'Coverage':>8s} | {'Mean SE':>7s}\")\n    print(f\"{'-'*28}-+-{'-'*3}-+-{'-'*1}-+-{'-'*8}-+-{'-'*7}-+-{'-'*8}-+-{'-'*7}\")\n\n    for method in method_order:\n        for s in range(K):\n            for z in [0, 1]:\n                r = df_agg[(df_agg['method'] == method) &\n                           (df_agg['subgroup'] == s) &\n                           (df_agg['z'] == z)]\n                if r.empty:\n                    continue\n                r = r.iloc[0]\n                print(f\"{method:<28s} | {s:>3d} | {z:>1d} | {r['bias']:8.4f} | {r['rmse']:7.4f} | {r['coverage']:8.4f} | {r['se_mean']:7.4f}\")\n        print()\n\n    print(\"\\n\" + \"=\" * 80)\n    print(\"INTERPRETATION\")\n    print(\"=\" * 80)\n    oracle_cov = df_agg[df_agg['method'] == 'Oracle']['coverage'].mean()\n    ec_true_cov = df_agg[df_agg['method'] == 'EC-HTE true CM']['coverage'].mean()\n    ec_est_cov = df_agg[df_agg['method'] == 'EC-HTE estimated CM']['coverage'].mean()\n    print(f\"  Oracle coverage:           {oracle_cov:.4f}\")\n    print(f\"  EC-HTE true CM coverage:   {ec_true_cov:.4f}\")\n    print(f\"  EC-HTE estimated coverage: {ec_est_cov:.4f}\")\n    print()\n    if oracle_cov < 0.90:\n        print(\"  -> Oracle < 90%: CF SE is inherently under-calibrated\")\n    else:\n        print(\"  -> Oracle >= 90%: CF SE is reasonably calibrated\")\n    if abs(ec_true_cov - ec_est_cov) < 0.03:\n        print(\"  -> EC-HTE true CM ~ estimated CM: gap is NOT from CM estimation error\")\n        print(\"     Coverage gap comes from CF inherent SE under-calibration\")\n    elif ec_true_cov > ec_est_cov + 0.05:\n        print(\"  -> EC-HTE true CM >> estimated CM: CM estimation error contributes to gap\")\n    else:\n        print(\"  -> Mixed signal: both CF SE calibration and CM estimation may contribute\")\n\n\nif __name__ == '__main__':\n    print(f\"exp-027b CausalForest Oracle Coverage (K=2, extreme)\")\n    print(f\"N={N}, K={K}, pi={PI}, weights={SUB_WEIGHTS}\")\n    print(f\"tau(0)={TAU_TRUE[0]}, tau(1)={TAU_TRUE[1]}\")\n    print(f\"n_expert={N_EXPERT}, N_MC={N_MC}, seed_base={BASE_SEED}\")\n\n    print(\"\\nTiming single run...\")\n    t_test = time.time()\n    _ = run_one_mc(seed=9999)\n    t_per = time.time() - t_test\n    print(f\"  {t_per:.2f}s/run (2 forest fits per run)\")\n    print(f\"  Estimated total: {t_per * N_MC:.0f}s ({t_per * N_MC / 60:.1f} min)\\n\")\n\n    all_rows = []\n    t0 = time.time()\n\n    for mc in range(N_MC):\n        seed = BASE_SEED + mc\n        try:\n            rows = run_one_mc(seed)\n            all_rows.extend(rows)\n        except Exception as e:\n            print(f\"  WARN: mc={mc} seed={seed} failed: {e}\")\n\n        if (mc + 1) % 10 == 0:\n            el = time.time() - t0\n            eta = el / (mc + 1) * (N_MC - mc - 1)\n            print(f\"  [{mc+1}/{N_MC}] {el:.0f}s elapsed, ETA {eta:.0f}s\")\n\n    elapsed = time.time() - t0\n    print(f\"\\nDone: {elapsed:.1f}s ({N_MC} runs, {elapsed/N_MC:.1f}s/run)\")\n\n    df_raw = pd.DataFrame(all_rows)\n    df_agg = aggregate_results(df_raw)\n\n    os.makedirs('results', exist_ok=True)\n    df_agg.to_csv('results/exp_cf_oracle_coverage_k2.csv', index=False)\n    print(f\"Saved: results/exp_cf_oracle_coverage_k2.csv ({len(df_agg)} rows)\")\n\n    print_summary(df_agg)\n",
      "numLines": 326,
      "startLine": 1,
      "totalLines": 326
    }
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_014276scVnt3Cjj91TZN1TFa`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp_w8_a5_violation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "43b464e9-1255-44f8-91a4-53afe71af94d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHTeSUyGujzyme2Ve8ZfUy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4988,
      "cache_read_input_tokens": 18919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4988
      },
      "output_tokens": 29,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-22T16:17:09.645Z_

<details><summary>↩ Tool result · `toolu_014276scVnt3Cjj91TZN1TFa`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	exp_w8_a5_violation.py — A5 Violation Test: Correlated Δτ and δ (W8)
4	
5	Tests EC-HTE robustness when CATE heterogeneity Δτ_s correlates with
6	misclassification rate δ_s, violating Assumption A5 (independence).
7	
8	Two configs:
9	  aligned:     high-error subgroup has large Δτ  (positive correlation)
10	  adversarial: high-error subgroup has small Δτ  (negative correlation)
11	
12	K=2, N=5000, n_expert ∈ {250, 500}, 50 MC runs, EB estimator.
13	"""
14	
15	import os
16	import time
17	import numpy as np
18	import pandas as pd
19	from scipy.special import gammaln
20	from scipy.optimize import minimize_scalar
21	
22	N = 5000
23	N_MC = 50
24	SEEDS = list(range(42, 42 + N_MC))
25	N_EXPERTS = [250, 500]
26	LABELS = ['S0', 'S1']
27	
28	CONFIGS = {
29	    'aligned': {
30	        'misclass': [0.05, 0.25],
31	        'tau_z0':   [0.10, 0.10],
32	        'tau_z1':   [0.40, 0.80],
33	    },
34	    'adversarial': {
35	        'misclass': [0.05, 0.25],
36	        'tau_z0':   [0.10, 0.10],
37	        'tau_z1':   [0.80, 0.40],
38	    },
39	}
40	
41	
42	def generate_data(config, n_expert, seed):
43	    rng = np.random.RandomState(seed)
44	    T = rng.binomial(1, 0.5, N)
45	    Z = rng.binomial(1, 0.5, N)
46	    S = rng.choice(LABELS, N, p=[0.5, 0.5])
47	    X = rng.randn(N, 5)
48	
49	    tau = np.zeros(N)
50	    mc_rates = np.zeros(N)
51	    for i, s in enumerate(LABELS):
52	        mask_s = S == s
53	        tau[mask_s] = np.where(Z[mask_s] == 1, config['tau_z1'][i], config['tau_z0'][i])
54	        mc_rates[mask_s] = config['misclass'][i]
55	
56	    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)
57	    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)
58	
59	    idx = rng.choice(N, min(n_expert, N), replace=False)
60	    expert_mask = np.zeros(N, dtype=bool)
61	    expert_mask[idx] = True
62	    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, Y=Y, tau=tau, expert_mask=expert_mask)
63	
64	
65	def diff_in_means(Y, T, mask):
66	    t1, t0 = mask & (T == 1), mask & (T == 0)
67	    n1, n0 = t1.sum(), t0.sum()
68	    if n1 < 2 or n0 < 2:
69	        return np.nan, np.nan
70	    y1, y0 = Y[t1], Y[t0]
71	    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
72	
73	
74	def estimate_cm(z_true, z_hat):
75	    C = np.zeros((2, 2))
76	    for z in [0, 1]:
77	        mask = z_true == z
78	        n = mask.sum()
79	        for zh in [0, 1]:
80	            C[z, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
81	    return C
82	
83	
84	def _dirmult_neg_ll(alpha, counts_z):
85	    a = alpha / 2.0
86	    if a < 1e-10:
87	        return 1e10
88	    ll = 0.0
89	    for c0, c1 in counts_z:
90	        n = c0 + c1
91	        if n == 0:
92	            continue
93	        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)
94	        ll -= 2 * gammaln(a) - gammaln(2 * a)
95	    return -ll
96	
97	
98	def estimate_cm_eb(counts):
99	    """Empirical Bayes: optimize shared Dirichlet concentration, return per-subgroup posterior mean."""
100	    k = len(LABELS)
101	    alpha_opt = np.zeros(2)
102	    for z in [0, 1]:
103	        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
104	        total = sum(c0 + c1 for c0, c1 in cl)
105	        if total == 0:
106	            alpha_opt[z] = 2.0
107	            continue
108	        res = minimize_scalar(
109	            lambda a, cz=cl: _dirmult_neg_ll(a, cz), bounds=(0.01, 500), method='bounded')
110	        alpha_opt[z] = res.x
111	
112	    C = {}
113	    for i, s in enumerate(LABELS):
114	        C_s = np.zeros((2, 2))
115	        for z in [0, 1]:
116	            a = alpha_opt[z] / 2.0
117	            n = counts[i, z, :].sum()
118	            d = n + 2 * a
119	            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5
120	            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5
121	        C[s] = C_s
122	    return C
123	
124	
125	def get_counts(z_true, z_hat, subgroups):
126	    k = len(LABELS)
127	    counts = np.zeros((k, 2, 2), dtype=int)
128	    for i, s in enumerate(LABELS):
129	        ms = subgroups == s
130	        for z in [0, 1]:
131	            mz = ms & (z_true == z)
132	            counts[i, z, 0] = (z_hat[mz] == 0).sum()
133	            counts[i, z, 1] = (z_hat[mz] == 1).sum()
134	    return counts
135	
136	
137	def build_mixing_matrix(C):
138	    M = np.zeros((2, 2))
139	    for zh in [0, 1]:
140	        cs = C[0, zh] + C[1, zh]
141	        M[zh, 0] = C[0, zh] / cs if cs > 0 else 0.5
142	        M[zh, 1] = C[1, zh] / cs if cs > 0 else 0.5
143	    return M
144	
145	
146	def invert_mixing(M, tau_obs, se_obs):
147	    if np.linalg.cond(M) > 100 or abs(np.linalg.det(M)) < 1e-10:
148	        return tau_obs.copy(), se_obs.copy(), True
149	    Mi = np.linalg.inv(M)
150	    tau_c = Mi @ tau_obs
151	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
152	    return tau_c, se_c, False
153	
154	
155	def run_one_mc(config, n_expert, seed):
156	    data = generate_data(config, n_expert, seed)
157	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
158	    em = data['expert_mask']
159	
160	    z_exp, zh_exp, s_exp = Z[em], Z_hat[em], S[em]
161	
162	    # True per-subgroup CATEs
163	    tau_true = {}
164	    for i, s in enumerate(LABELS):
165	        tau_true[s] = np.array([config['tau_z0'][i], config['tau_z1'][i]])
166	
167	    # Observed CATEs per subgroup (using Z_hat)
168	    sub_obs, sub_se = {}, {}
169	    for s in LABELS:
170	        sm = S == s
171	        th0, se0 = diff_in_means(Y, T, sm & (Z_hat == 0))
172	        th1, se1 = diff_in_means(Y, T, sm & (Z_hat == 1))
173	        sub_obs[s] = np.array([th0, th1])
174	        sub_se[s] = np.array([se0, se1])
175	
176	    for s in LABELS:
177	        if np.any(np.isnan(sub_obs[s])):
178	            return []
179	
180	    # Oracle: use true Z
181	    oracle_tau, oracle_se = {}, {}
182	    for s in LABELS:
183	        sm = S == s
184	        th0, se0 = diff_in_means(Y, T, sm & (Z == 0))
185	        th1, se1 = diff_in_means(Y, T, sm & (Z == 1))
186	        oracle_tau[s] = np.array([th0, th1])
187	        oracle_se[s] = np.array([se0, se1])
188	
189	    # Global confusion matrix (pooled expert data)
190	    C_global = estimate_cm(z_exp, zh_exp)
191	    M_global = build_mixing_matrix(C_global)
192	
193	    # Per-subgroup confusion matrices
194	    counts = get_counts(z_exp, zh_exp, s_exp)
195	
196	    # MLE per-subgroup
197	    C_mle = {}
198	    for i, s in enumerate(LABELS):
199	        sm = s_exp == s
200	        if sm.sum() < 4:
201	            C_mle[s] = C_global.copy()
202	        else:
203	            C_mle[s] = estimate_cm(z_exp[sm], zh_exp[sm])
204	
205	    # EB per-subgroup
206	    C_eb = estimate_cm_eb(counts)
207	
208	    rows = []
209	
210	    def make_row(method, s, tau_hat, se_hat):
211	        tt = tau_true[s]
212	        for z_idx in [0, 1]:
213	            ci_lo = tau_hat[z_idx] - 1.96 * se_hat[z_idx]
214	            ci_hi = tau_hat[z_idx] + 1.96 * se_hat[z_idx]
215	            rows.append({
216	                'n_expert': n_expert, 'seed': seed, 'method': method,
217	                'subgroup': s, 'z': f'z{z_idx}',
218	                'tau_hat': tau_hat[z_idx], 'tau_true': tt[z_idx],
219	                'se': se_hat[z_idx],
220	                'ci_lower': ci_lo, 'ci_upper': ci_hi,
221	                'covers': int(ci_lo <= tt[z_idx] <= ci_hi),
222	            })
223	
224	    for s in LABELS:
225	        # Oracle
226	        make_row('oracle', s, oracle_tau[s], oracle_se[s])
227	
228	        # Naive
229	        make_row('naive', s, sub_obs[s], sub_se[s])
230	
231	        # Global corrected
232	        tau_gc, se_gc, _ = invert_mixing(M_global, sub_obs[s], sub_se[s])
233	        make_row('global_corrected', s, tau_gc, se_gc)
234	
235	        # EC-HTE (MLE)
236	        M_mle_s = build_mixing_matrix(C_mle[s])
237	        tau_mle, se_mle, _ = invert_mixing(M_mle_s, sub_obs[s], sub_se[s])
238	        make_row('ec_hte_mle', s, tau_mle, se_mle)
239	
240	        # EC-HTE (EB)
241	        M_eb_s = build_mixing_matrix(C_eb[s])
242	        tau_eb, se_eb, _ = invert_mixing(M_eb_s, sub_obs[s], sub_se[s])
243	        make_row('ec_hte_eb', s, tau_eb, se_eb)
244	
245	    return rows
246	
247	
248	def aggregate(df):
249	    agg_rows = []
250	    for (ne, method, subgroup), grp in df.groupby(['n_expert', 'method', 'subgroup']):
251	        row = {'n_expert': int(ne), 'method': method, 'subgroup': subgroup}
252	        for z in ['z0', 'z1']:
253	            zg = grp[grp['z'] == z]
254	            err = zg['tau_hat'].values - zg['tau_true'].values
255	            row[f'bias_{z}'] = err.mean()
256	            row[f'abs_bias_{z}'] = abs(err.mean())
257	            row[f'rmse_{z}'] = np.sqrt((err ** 2).mean())
258	            row[f'coverage_{z}'] = zg['covers'].mean()
259	            row[f'mean_se_{z}'] = zg['se'].mean()
260	        row['abs_bias'] = (row['abs_bias_z0'] + row['abs_bias_z1']) / 2
261	        row['rmse'] = (row['rmse_z0'] + row['rmse_z1']) / 2
262	        row['coverage'] = (row['coverage_z0'] + row['coverage_z1']) / 2
263	        agg_rows.append(row)
264	    return pd.DataFrame(agg_rows)
265	
266	
267	def print_table(df_agg, config_name):
268	    print(f"\n{'=' * 120}")
269	    print(f"  Config: {config_name}")
270	    print(f"{'=' * 120}")
271	    header = (f"{'n_exp':>5} {'Method':>18} {'Subgrp':>6} | "
272	              f"{'|Bias| z0':>9} {'|Bias| z1':>9} | "
273	              f"{'RMSE z0':>8} {'RMSE z1':>8} | "
274	              f"{'Cov z0':>7} {'Cov z1':>7} | "
275	              f"{'RMSE':>7} {'Cov':>5}")
276	    print(header)
277	    print("-" * len(header))
278	    for ne in N_EXPERTS:
279	        for method in ['oracle', 'naive', 'global_corrected', 'ec_hte_mle', 'ec_hte_eb']:
280	            for s in LABELS:
281	                r = df_agg[(df_agg['n_expert'] == ne) &
282	                           (df_agg['method'] == method) &
283	                           (df_agg['subgroup'] == s)]
284	                if r.empty:
285	                    continue
286	                r = r.iloc[0]
287	                print(f"{ne:5d} {method:>18} {s:>6} | "
288	                      f"{r['abs_bias_z0']:9.4f} {r['abs_bias_z1']:9.4f} | "
289	                      f"{r['rmse_z0']:8.4f} {r['rmse_z1']:8.4f} | "
290	                      f"{r['coverage_z0']:7.3f} {r['coverage_z1']:7.3f} | "
291	                      f"{r['rmse']:7.4f} {r['coverage']:5.3f}")
292	        print("-" * len(header))
293	
294	
295	def main():
296	    print(f"W8: A5 Violation — Correlated Δτ and δ")
297	    print(f"N={N}, n_expert={N_EXPERTS}, N_MC={N_MC}")
298	    print(f"Configs: aligned (positive corr), adversarial (negative corr)\n")
299	
300	    all_dfs = {}
301	    t0_total = time.time()
302	
303	    for cfg_name, cfg in CONFIGS.items():
304	        print(f"\n--- Running config: {cfg_name} ---")
305	        delta_tau = [cfg['tau_z1'][i] - cfg['tau_z0'][i] for i in range(len(LABELS))]
306	        for i, s in enumerate(LABELS):
307	            print(f"  {s}: π={cfg['misclass'][i]:.2f}, "
308	                  f"τ(z=0)={cfg['tau_z0'][i]:.2f}, τ(z=1)={cfg['tau_z1'][i]:.2f}, "
309	                  f"Δτ={delta_tau[i]:.2f}")
310	
311	        all_rows = []
312	        total = len(N_EXPERTS) * N_MC
313	        count = 0
314	        t0 = time.time()
315	
316	        for ne in N_EXPERTS:
317	            for seed in SEEDS:
318	                rows = run_one_mc(cfg, ne, seed)
319	                all_rows.extend(rows)
320	                count += 1
321	                if count % max(1, total // 5) == 0:
322	                    el = time.time() - t0
323	                    eta = el / count * (total - count)
324	                    print(f"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s")
325	
326	        elapsed = time.time() - t0
327	        print(f"  Done in {elapsed:.1f}s")
328	
329	        df_raw = pd.DataFrame(all_rows)
330	        df_raw['config'] = cfg_name
331	        df_agg = aggregate(df_raw)
332	        df_agg['config'] = cfg_name
333	        all_dfs[cfg_name] = (df_raw, df_agg)
334	
335	        print_table(df_agg, cfg_name)
336	
337	    total_elapsed = time.time() - t0_total
338	    print(f"\nTotal runtime: {total_elapsed:.1f}s")
339	
340	    # Combine and save
341	    os.makedirs('results', exist_ok=True)
342	    raw_all = pd.concat([v[0] for v in all_dfs.values()], ignore_index=True)
343	    agg_all = pd.concat([v[1] for v in all_dfs.values()], ignore_index=True)
344	
345	    raw_path = 'results/exp_w8_a5_violation_raw.csv'
346	    agg_path = 'results/exp_w8_a5_violation.csv'
347	    raw_all.to_csv(raw_path, index=False)
348	    agg_all.to_csv(agg_path, index=False)
349	    print(f"\nSaved: {agg_path} ({len(agg_all)} rows)")
350	    print(f"Saved: {raw_path} ({len(raw_all)} rows)")
351	
352	    # Overall summary table (for paper)
353	    print(f"\n{'=' * 120}")
354	    print("SUMMARY TABLE (for paper)")
355	    print(f"{'=' * 120}")
356	    header = (f"{'Config':>12} {'n_exp':>5} {'Method':>18} | "
357	              f"{'S0 |Bias|':>9} {'S1 |Bias|':>9} | "
358	              f"{'S0 RMSE':>8} {'S1 RMSE':>8} | "
359	              f"{'S0 Cov':>7} {'S1 Cov':>7} | "
360	              f"{'Overall RMSE':>12}")
361	    print(header)
362	    print("-" * len(header))
363	
364	    for cfg_name in ['aligned', 'adversarial']:
365	        df_agg = all_dfs[cfg_name][1]
366	        for ne in N_EXPERTS:
367	            for method in ['naive', 'global_corrected', 'ec_hte_eb']:
368	                s0 = df_agg[(df_agg['n_expert'] == ne) &
369	                            (df_agg['method'] == method) &
370	                            (df_agg['subgroup'] == 'S0')]
371	                s1 = df_agg[(df_agg['n_expert'] == ne) &
372	                            (df_agg['method'] == method) &
373	                            (df_agg['subgroup'] == 'S1')]
374	                if s0.empty or s1.empty:
375	                    continue
376	                s0, s1 = s0.iloc[0], s1.iloc[0]
377	                overall_rmse = (s0['rmse'] + s1['rmse']) / 2
378	                print(f"{cfg_name:>12} {ne:5d} {method:>18} | "
379	                      f"{s0['abs_bias']:9.4f} {s1['abs_bias']:9.4f} | "
380	                      f"{s0['rmse']:8.4f} {s1['rmse']:8.4f} | "
381	                      f"{s0['coverage']:7.3f} {s1['coverage']:7.3f} | "
382	                      f"{overall_rmse:12.4f}")
383	            print("-" * len(header))
384	
385	    # LaTeX paragraph
386	    a_agg = all_dfs['aligned'][1]
387	    d_agg = all_dfs['adversarial'][1]
388	
389	    def get_cov(df, ne, method):
390	        sub = df[(df['n_expert'] == ne) & (df['method'] == method)]
391	        return sub['coverage'].mean()
392	
393	    def get_rmse(df, ne, method):
394	        sub = df[(df['n_expert'] == ne) & (df['method'] == method)]
395	        return sub['rmse'].mean()
396	
397	    ne_main = 500
398	
399	    naive_cov_a = get_cov(a_agg, ne_main, 'naive')
400	    gc_cov_a = get_cov(a_agg, ne_main, 'global_corrected')
401	    eb_cov_a = get_cov(a_agg, ne_main, 'ec_hte_eb')
402	    naive_cov_d = get_cov(d_agg, ne_main, 'naive')
403	    gc_cov_d = get_cov(d_agg, ne_main, 'global_corrected')
404	    eb_cov_d = get_cov(d_agg, ne_main, 'ec_hte_eb')
405	
406	    naive_rmse_a = get_rmse(a_agg, ne_main, 'naive')
407	    eb_rmse_a = get_rmse(a_agg, ne_main, 'ec_hte_eb')
408	    naive_rmse_d = get_rmse(d_agg, ne_main, 'naive')
409	    eb_rmse_d = get_rmse(d_agg, ne_main, 'ec_hte_eb')
410	
411	    latex = rf"""\paragraph{{Robustness to Correlated Heterogeneity (A5 Violation)}}
412	Assumption~(A5) posits that CATE heterogeneity $\Delta\tau_s = \tau_s(z{{=}}1) - \tau_s(z{{=}}0)$
413	is independent of the subgroup misclassification rate $\delta_s$. We test two
414	structured violations with $K=2$ subgroups and
415	$\delta \in \{{0.05, 0.25\}}$: (i)~\emph{{aligned}}, where the high-error
416	subgroup also has large $\Delta\tau$ ($0.70$ vs.\ $0.30$), and
417	(ii)~\emph{{adversarial}}, the reverse assignment. Under the aligned
418	configuration, the naive estimator's bias is amplified by the $\delta_s
419	\times \Delta\tau_s$ product, yielding RMSE $={naive_rmse_a:.3f}$
420	and coverage $={naive_cov_a:.0%}$ ($n_{{\text{{expert}}}}={ne_main}$).
421	EC-HTE reduces RMSE to ${eb_rmse_a:.3f}$ with ${eb_cov_a:.0%}$ coverage.
422	In the adversarial case the bias product is attenuated, so the global
423	correction appears adequate (coverage ${gc_cov_d:.0%}$); however,
424	EC-HTE still achieves ${eb_cov_d:.0%}$ coverage with RMSE ${eb_rmse_d:.3f}$,
425	matching or improving the global baseline. Across both correlation
426	structures, EC-HTE maintains near-nominal coverage, confirming that
427	the estimator does not rely on Assumption~(A5) for practical validity."""
428	
429	    print(f"\n{'=' * 120}")
430	    print("LaTeX paragraph:")
431	    print(f"{'=' * 120}")
432	    print(latex)
433	
434	
435	if __name__ == '__main__':
436	    main()
437	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "5c855cc2-10ec-4aba-9c4d-e2e49c0d455d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp_w8_a5_violation.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nexp_w8_a5_violation.py — A5 Violation Test: Correlated Δτ and δ (W8)\n\nTests EC-HTE robustness when CATE heterogeneity Δτ_s correlates with\nmisclassification rate δ_s, violating Assumption A5 (independence).\n\nTwo configs:\n  aligned:     high-error subgroup has large Δτ  (positive correlation)\n  adversarial: high-error subgroup has small Δτ  (negative correlation)\n\nK=2, N=5000, n_expert ∈ {250, 500}, 50 MC runs, EB estimator.\n\"\"\"\n\nimport os\nimport time\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\nfrom scipy.optimize import minimize_scalar\n\nN = 5000\nN_MC = 50\nSEEDS = list(range(42, 42 + N_MC))\nN_EXPERTS = [250, 500]\nLABELS = ['S0', 'S1']\n\nCONFIGS = {\n    'aligned': {\n        'misclass': [0.05, 0.25],\n        'tau_z0':   [0.10, 0.10],\n        'tau_z1':   [0.40, 0.80],\n    },\n    'adversarial': {\n        'misclass': [0.05, 0.25],\n        'tau_z0':   [0.10, 0.10],\n        'tau_z1':   [0.80, 0.40],\n    },\n}\n\n\ndef generate_data(config, n_expert, seed):\n    rng = np.random.RandomState(seed)\n    T = rng.binomial(1, 0.5, N)\n    Z = rng.binomial(1, 0.5, N)\n    S = rng.choice(LABELS, N, p=[0.5, 0.5])\n    X = rng.randn(N, 5)\n\n    tau = np.zeros(N)\n    mc_rates = np.zeros(N)\n    for i, s in enumerate(LABELS):\n        mask_s = S == s\n        tau[mask_s] = np.where(Z[mask_s] == 1, config['tau_z1'][i], config['tau_z0'][i])\n        mc_rates[mask_s] = config['misclass'][i]\n\n    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)\n    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)\n\n    idx = rng.choice(N, min(n_expert, N), replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[idx] = True\n    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, Y=Y, tau=tau, expert_mask=expert_mask)\n\n\ndef diff_in_means(Y, T, mask):\n    t1, t0 = mask & (T == 1), mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n\n\ndef estimate_cm(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for z in [0, 1]:\n        mask = z_true == z\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[z, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_eb(counts):\n    \"\"\"Empirical Bayes: optimize shared Dirichlet concentration, return per-subgroup posterior mean.\"\"\"\n    k = len(LABELS)\n    alpha_opt = np.zeros(2)\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = 2.0\n            continue\n        res = minimize_scalar(\n            lambda a, cz=cl: _dirmult_neg_ll(a, cz), bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(LABELS):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n = counts[i, z, :].sum()\n            d = n + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef get_counts(z_true, z_hat, subgroups):\n    k = len(LABELS)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(LABELS):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef build_mixing_matrix(C):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        cs = C[0, zh] + C[1, zh]\n        M[zh, 0] = C[0, zh] / cs if cs > 0 else 0.5\n        M[zh, 1] = C[1, zh] / cs if cs > 0 else 0.5\n    return M\n\n\ndef invert_mixing(M, tau_obs, se_obs):\n    if np.linalg.cond(M) > 100 or abs(np.linalg.det(M)) < 1e-10:\n        return tau_obs.copy(), se_obs.copy(), True\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c, False\n\n\ndef run_one_mc(config, n_expert, seed):\n    data = generate_data(config, n_expert, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n\n    z_exp, zh_exp, s_exp = Z[em], Z_hat[em], S[em]\n\n    # True per-subgroup CATEs\n    tau_true = {}\n    for i, s in enumerate(LABELS):\n        tau_true[s] = np.array([config['tau_z0'][i], config['tau_z1'][i]])\n\n    # Observed CATEs per subgroup (using Z_hat)\n    sub_obs, sub_se = {}, {}\n    for s in LABELS:\n        sm = S == s\n        th0, se0 = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1, se1 = diff_in_means(Y, T, sm & (Z_hat == 1))\n        sub_obs[s] = np.array([th0, th1])\n        sub_se[s] = np.array([se0, se1])\n\n    for s in LABELS:\n        if np.any(np.isnan(sub_obs[s])):\n            return []\n\n    # Oracle: use true Z\n    oracle_tau, oracle_se = {}, {}\n    for s in LABELS:\n        sm = S == s\n        th0, se0 = diff_in_means(Y, T, sm & (Z == 0))\n        th1, se1 = diff_in_means(Y, T, sm & (Z == 1))\n        oracle_tau[s] = np.array([th0, th1])\n        oracle_se[s] = np.array([se0, se1])\n\n    # Global confusion matrix (pooled expert data)\n    C_global = estimate_cm(z_exp, zh_exp)\n    M_global = build_mixing_matrix(C_global)\n\n    # Per-subgroup confusion matrices\n    counts = get_counts(z_exp, zh_exp, s_exp)\n\n    # MLE per-subgroup\n    C_mle = {}\n    for i, s in enumerate(LABELS):\n        sm = s_exp == s\n        if sm.sum() < 4:\n            C_mle[s] = C_global.copy()\n        else:\n            C_mle[s] = estimate_cm(z_exp[sm], zh_exp[sm])\n\n    # EB per-subgroup\n    C_eb = estimate_cm_eb(counts)\n\n    rows = []\n\n    def make_row(method, s, tau_hat, se_hat):\n        tt = tau_true[s]\n        for z_idx in [0, 1]:\n            ci_lo = tau_hat[z_idx] - 1.96 * se_hat[z_idx]\n            ci_hi = tau_hat[z_idx] + 1.96 * se_hat[z_idx]\n            rows.append({\n                'n_expert': n_expert, 'seed': seed, 'method': method,\n                'subgroup': s, 'z': f'z{z_idx}',\n                'tau_hat': tau_hat[z_idx], 'tau_true': tt[z_idx],\n                'se': se_hat[z_idx],\n                'ci_lower': ci_lo, 'ci_upper': ci_hi,\n                'covers': int(ci_lo <= tt[z_idx] <= ci_hi),\n            })\n\n    for s in LABELS:\n        # Oracle\n        make_row('oracle', s, oracle_tau[s], oracle_se[s])\n\n        # Naive\n        make_row('naive', s, sub_obs[s], sub_se[s])\n\n        # Global corrected\n        tau_gc, se_gc, _ = invert_mixing(M_global, sub_obs[s], sub_se[s])\n        make_row('global_corrected', s, tau_gc, se_gc)\n\n        # EC-HTE (MLE)\n        M_mle_s = build_mixing_matrix(C_mle[s])\n        tau_mle, se_mle, _ = invert_mixing(M_mle_s, sub_obs[s], sub_se[s])\n        make_row('ec_hte_mle', s, tau_mle, se_mle)\n\n        # EC-HTE (EB)\n        M_eb_s = build_mixing_matrix(C_eb[s])\n        tau_eb, se_eb, _ = invert_mixing(M_eb_s, sub_obs[s], sub_se[s])\n        make_row('ec_hte_eb', s, tau_eb, se_eb)\n\n    return rows\n\n\ndef aggregate(df):\n    agg_rows = []\n    for (ne, method, subgroup), grp in df.groupby(['n_expert', 'method', 'subgroup']):\n        row = {'n_expert': int(ne), 'method': method, 'subgroup': subgroup}\n        for z in ['z0', 'z1']:\n            zg = grp[grp['z'] == z]\n            err = zg['tau_hat'].values - zg['tau_true'].values\n            row[f'bias_{z}'] = err.mean()\n            row[f'abs_bias_{z}'] = abs(err.mean())\n            row[f'rmse_{z}'] = np.sqrt((err ** 2).mean())\n            row[f'coverage_{z}'] = zg['covers'].mean()\n            row[f'mean_se_{z}'] = zg['se'].mean()\n        row['abs_bias'] = (row['abs_bias_z0'] + row['abs_bias_z1']) / 2\n        row['rmse'] = (row['rmse_z0'] + row['rmse_z1']) / 2\n        row['coverage'] = (row['coverage_z0'] + row['coverage_z1']) / 2\n        agg_rows.append(row)\n    return pd.DataFrame(agg_rows)\n\n\ndef print_table(df_agg, config_name):\n    print(f\"\\n{'=' * 120}\")\n    print(f\"  Config: {config_name}\")\n    print(f\"{'=' * 120}\")\n    header = (f\"{'n_exp':>5} {'Method':>18} {'Subgrp':>6} | \"\n              f\"{'|Bias| z0':>9} {'|Bias| z1':>9} | \"\n              f\"{'RMSE z0':>8} {'RMSE z1':>8} | \"\n              f\"{'Cov z0':>7} {'Cov z1':>7} | \"\n              f\"{'RMSE':>7} {'Cov':>5}\")\n    print(header)\n    print(\"-\" * len(header))\n    for ne in N_EXPERTS:\n        for method in ['oracle', 'naive', 'global_corrected', 'ec_hte_mle', 'ec_hte_eb']:\n            for s in LABELS:\n                r = df_agg[(df_agg['n_expert'] == ne) &\n                           (df_agg['method'] == method) &\n                           (df_agg['subgroup'] == s)]\n                if r.empty:\n                    continue\n                r = r.iloc[0]\n                print(f\"{ne:5d} {method:>18} {s:>6} | \"\n                      f\"{r['abs_bias_z0']:9.4f} {r['abs_bias_z1']:9.4f} | \"\n                      f\"{r['rmse_z0']:8.4f} {r['rmse_z1']:8.4f} | \"\n                      f\"{r['coverage_z0']:7.3f} {r['coverage_z1']:7.3f} | \"\n                      f\"{r['rmse']:7.4f} {r['coverage']:5.3f}\")\n        print(\"-\" * len(header))\n\n\ndef main():\n    print(f\"W8: A5 Violation — Correlated Δτ and δ\")\n    print(f\"N={N}, n_expert={N_EXPERTS}, N_MC={N_MC}\")\n    print(f\"Configs: aligned (positive corr), adversarial (negative corr)\\n\")\n\n    all_dfs = {}\n    t0_total = time.time()\n\n    for cfg_name, cfg in CONFIGS.items():\n        print(f\"\\n--- Running config: {cfg_name} ---\")\n        delta_tau = [cfg['tau_z1'][i] - cfg['tau_z0'][i] for i in range(len(LABELS))]\n        for i, s in enumerate(LABELS):\n            print(f\"  {s}: π={cfg['misclass'][i]:.2f}, \"\n                  f\"τ(z=0)={cfg['tau_z0'][i]:.2f}, τ(z=1)={cfg['tau_z1'][i]:.2f}, \"\n                  f\"Δτ={delta_tau[i]:.2f}\")\n\n        all_rows = []\n        total = len(N_EXPERTS) * N_MC\n        count = 0\n        t0 = time.time()\n\n        for ne in N_EXPERTS:\n            for seed in SEEDS:\n                rows = run_one_mc(cfg, ne, seed)\n                all_rows.extend(rows)\n                count += 1\n                if count % max(1, total // 5) == 0:\n                    el = time.time() - t0\n                    eta = el / count * (total - count)\n                    print(f\"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s\")\n\n        elapsed = time.time() - t0\n        print(f\"  Done in {elapsed:.1f}s\")\n\n        df_raw = pd.DataFrame(all_rows)\n        df_raw['config'] = cfg_name\n        df_agg = aggregate(df_raw)\n        df_agg['config'] = cfg_name\n        all_dfs[cfg_name] = (df_raw, df_agg)\n\n        print_table(df_agg, cfg_name)\n\n    total_elapsed = time.time() - t0_total\n    print(f\"\\nTotal runtime: {total_elapsed:.1f}s\")\n\n    # Combine and save\n    os.makedirs('results', exist_ok=True)\n    raw_all = pd.concat([v[0] for v in all_dfs.values()], ignore_index=True)\n    agg_all = pd.concat([v[1] for v in all_dfs.values()], ignore_index=True)\n\n    raw_path = 'results/exp_w8_a5_violation_raw.csv'\n    agg_path = 'results/exp_w8_a5_violation.csv'\n    raw_all.to_csv(raw_path, index=False)\n    agg_all.to_csv(agg_path, index=False)\n    print(f\"\\nSaved: {agg_path} ({len(agg_all)} rows)\")\n    print(f\"Saved: {raw_path} ({len(raw_all)} rows)\")\n\n    # Overall summary table (for paper)\n    print(f\"\\n{'=' * 120}\")\n    print(\"SUMMARY TABLE (for paper)\")\n    print(f\"{'=' * 120}\")\n    header = (f\"{'Config':>12} {'n_exp':>5} {'Method':>18} | \"\n              f\"{'S0 |Bias|':>9} {'S1 |Bias|':>9} | \"\n              f\"{'S0 RMSE':>8} {'S1 RMSE':>8} | \"\n              f\"{'S0 Cov':>7} {'S1 Cov':>7} | \"\n              f\"{'Overall RMSE':>12}\")\n    print(header)\n    print(\"-\" * len(header))\n\n    for cfg_name in ['aligned', 'adversarial']:\n        df_agg = all_dfs[cfg_name][1]\n        for ne in N_EXPERTS:\n            for method in ['naive', 'global_corrected', 'ec_hte_eb']:\n                s0 = df_agg[(df_agg['n_expert'] == ne) &\n                            (df_agg['method'] == method) &\n                            (df_agg['subgroup'] == 'S0')]\n                s1 = df_agg[(df_agg['n_expert'] == ne) &\n                            (df_agg['method'] == method) &\n                            (df_agg['subgroup'] == 'S1')]\n                if s0.empty or s1.empty:\n                    continue\n                s0, s1 = s0.iloc[0], s1.iloc[0]\n                overall_rmse = (s0['rmse'] + s1['rmse']) / 2\n                print(f\"{cfg_name:>12} {ne:5d} {method:>18} | \"\n                      f\"{s0['abs_bias']:9.4f} {s1['abs_bias']:9.4f} | \"\n                      f\"{s0['rmse']:8.4f} {s1['rmse']:8.4f} | \"\n                      f\"{s0['coverage']:7.3f} {s1['coverage']:7.3f} | \"\n                      f\"{overall_rmse:12.4f}\")\n            print(\"-\" * len(header))\n\n    # LaTeX paragraph\n    a_agg = all_dfs['aligned'][1]\n    d_agg = all_dfs['adversarial'][1]\n\n    def get_cov(df, ne, method):\n        sub = df[(df['n_expert'] == ne) & (df['method'] == method)]\n        return sub['coverage'].mean()\n\n    def get_rmse(df, ne, method):\n        sub = df[(df['n_expert'] == ne) & (df['method'] == method)]\n        return sub['rmse'].mean()\n\n    ne_main = 500\n\n    naive_cov_a = get_cov(a_agg, ne_main, 'naive')\n    gc_cov_a = get_cov(a_agg, ne_main, 'global_corrected')\n    eb_cov_a = get_cov(a_agg, ne_main, 'ec_hte_eb')\n    naive_cov_d = get_cov(d_agg, ne_main, 'naive')\n    gc_cov_d = get_cov(d_agg, ne_main, 'global_corrected')\n    eb_cov_d = get_cov(d_agg, ne_main, 'ec_hte_eb')\n\n    naive_rmse_a = get_rmse(a_agg, ne_main, 'naive')\n    eb_rmse_a = get_rmse(a_agg, ne_main, 'ec_hte_eb')\n    naive_rmse_d = get_rmse(d_agg, ne_main, 'naive')\n    eb_rmse_d = get_rmse(d_agg, ne_main, 'ec_hte_eb')\n\n    latex = rf\"\"\"\\paragraph{{Robustness to Correlated Heterogeneity (A5 Violation)}}\nAssumption~(A5) posits that CATE heterogeneity $\\Delta\\tau_s = \\tau_s(z{{=}}1) - \\tau_s(z{{=}}0)$\nis independent of the subgroup misclassification rate $\\delta_s$. We test two\nstructured violations with $K=2$ subgroups and\n$\\delta \\in \\{{0.05, 0.25\\}}$: (i)~\\emph{{aligned}}, where the high-error\nsubgroup also has large $\\Delta\\tau$ ($0.70$ vs.\\ $0.30$), and\n(ii)~\\emph{{adversarial}}, the reverse assignment. Under the aligned\nconfiguration, the naive estimator's bias is amplified by the $\\delta_s\n\\times \\Delta\\tau_s$ product, yielding RMSE $={naive_rmse_a:.3f}$\nand coverage $={naive_cov_a:.0%}$ ($n_{{\\text{{expert}}}}={ne_main}$).\nEC-HTE reduces RMSE to ${eb_rmse_a:.3f}$ with ${eb_cov_a:.0%}$ coverage.\nIn the adversarial case the bias product is attenuated, so the global\ncorrection appears adequate (coverage ${gc_cov_d:.0%}$); however,\nEC-HTE still achieves ${eb_cov_d:.0%}$ coverage with RMSE ${eb_rmse_d:.3f}$,\nmatching or improving the global baseline. Across both correlation\nstructures, EC-HTE maintains near-nominal coverage, confirming that\nthe estimator does not rely on Assumption~(A5) for practical validity.\"\"\"\n\n    print(f\"\\n{'=' * 120}\")\n    print(\"LaTeX paragraph:\")\n    print(f\"{'=' * 120}\")\n    print(latex)\n\n\nif __name__ == '__main__':\n    main()\n",
      "numLines": 437,
      "startLine": 1,
      "totalLines": 437
    }
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_012f9w1ou2AwV8LkTNuTyP9Q`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "1f10101d-3da7-4b91-8993-36128dcb3731",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JHTeSUyGujzyme2Ve8ZfUy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4988,
      "cache_read_input_tokens": 18919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4988
      },
      "output_tokens": 29,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-22T16:17:10.285Z_

<details><summary>↩ Tool result · `toolu_012f9w1ou2AwV8LkTNuTyP9Q`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	exp001_hb_synthetic.py - Hierarchical Bayesian EC-HTE Synthetic Validation (exp-001)
4	
5	Compares confusion matrix estimators for CATE correction under heterogeneous
6	misclassification across subgroups:
7	  Oracle, Naive, Global-corrected, MLE (Laplace), HB Dirichlet (partial pooling)
8	
9	Input: Synthetic DGP parameters (regimes, expert budgets, subgroup counts)
10	Output: results/exp001_hb_results.csv, results/exp001_hb_diagnostics.csv
11	"""
12	
13	import argparse
14	import os
15	import sys
16	import time
17	import warnings
18	import numpy as np
19	import pandas as pd
20	from scipy.special import gammaln
21	from scipy.optimize import minimize_scalar
22	
23	warnings.filterwarnings('ignore')
24	
25	try:
26	    import pymc as pm
27	    import pytensor.tensor as pt
28	    import arviz as az
29	    HAS_PYMC = True
30	except ImportError:
31	    HAS_PYMC = False
32	
33	N = 5000
34	SUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}
35	
36	REGIMES = {
37	    2: {
38	        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},
39	        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},
40	        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
41	    },
42	    4: {
43	        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},
44	        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},
45	        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
46	    },
47	}
48	
49	DEFAULT_N_EXPERTS = [50, 100, 250, 500, 1000, 2000]
50	DEFAULT_K_LIST = [2, 4]
51	
52	
53	# ── DGP ───────────────────────────────────────────────────────────────────────
54	
55	def generate_data(regime_params, n_expert, k, seed):
56	    rng = np.random.RandomState(seed)
57	    labels = SUBGROUP_LABELS[k]
58	    T = rng.binomial(1, 0.5, N)
59	    Z = rng.binomial(1, 0.5, N)
60	    S = rng.choice(labels, N, p=[1.0 / k] * k)
61	    X = rng.randn(N, 5)
62	    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])
63	    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)
64	    mc_rates = np.zeros(N)
65	    for i, s in enumerate(labels):
66	        mc_rates[S == s] = regime_params['misclass'][i]
67	    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)
68	    idx = rng.choice(N, min(n_expert, N), replace=False)
69	    expert_mask = np.zeros(N, dtype=bool)
70	    expert_mask[idx] = True
71	    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, tau=tau, expert_mask=expert_mask)
72	
73	
74	# ── Helpers ───────────────────────────────────────────────────────────────────
75	
76	def diff_in_means(Y, T, mask):
77	    t1, t0 = mask & (T == 1), mask & (T == 0)
78	    n1, n0 = t1.sum(), t0.sum()
79	    if n1 < 2 or n0 < 2:
80	        return np.nan, np.nan
81	    y1, y0 = Y[t1], Y[t0]
82	    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
83	
84	
85	def get_counts(z_true, z_hat, subgroups, labels):
86	    """Confusion matrix counts per subgroup: (k, 2, 2) = [subgroup, true_z, z_hat]."""
87	    k = len(labels)
88	    counts = np.zeros((k, 2, 2), dtype=int)
89	    for i, s in enumerate(labels):
90	        ms = subgroups == s
91	        for z in [0, 1]:
92	            mz = ms & (z_true == z)
93	            counts[i, z, 0] = (z_hat[mz] == 0).sum()
94	            counts[i, z, 1] = (z_hat[mz] == 1).sum()
95	    return counts
96	
97	
98	def build_mixing_matrix(C):
99	    """C[z, z_hat] → M[z_hat, z] via Bayes rule (assuming P(Z=0)=P(Z=1)=0.5).
100	
101	    NOTE: This assumes P(Z=0)=P(Z=1)=0.5, which is correct for this experiment's
102	    DGP. For general P(Z), use the version in exp007 that takes p_z and p_z_hat.
103	    """
104	    M = np.zeros((2, 2))
105	    for zh in [0, 1]:
106	        cs = C[0, zh] + C[1, zh]
107	        if cs > 0:
108	            M[zh, 0] = C[0, zh] / cs
109	            M[zh, 1] = C[1, zh] / cs
110	        else:
111	            M[zh, :] = 0.5
112	    return M
113	
114	
115	def invert_mixing(M, tau_obs, se_obs):
116	    det = np.linalg.det(M)
117	    if abs(det) < 1e-10:
118	        return tau_obs.copy(), se_obs.copy()
119	    Mi = np.linalg.inv(M)
120	    tau_c = Mi @ tau_obs
121	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
122	    return tau_c, se_c
123	
124	
125	def safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):
126	    """Invert mixing matrix with condition number guard.
127	
128	    When cond(M_s) > threshold, matrix inversion is numerically unstable.
129	    Falls back to naive (no correction) to avoid catastrophic amplification.
130	    """
131	    cond = np.linalg.cond(M_s)
132	    if cond > cond_threshold:
133	        return tau_obs.copy()
134	    return np.linalg.solve(M_s, tau_obs)
135	
136	
137	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
138	    """Like invert_mixing but with condition number guard."""
139	    cond = np.linalg.cond(M)
140	    if cond > cond_threshold:
141	        return tau_obs.copy(), se_obs.copy()
142	    det = np.linalg.det(M)
143	    if abs(det) < 1e-10:
144	        return tau_obs.copy(), se_obs.copy()
145	    Mi = np.linalg.inv(M)
146	    tau_c = Mi @ tau_obs
147	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
148	    return tau_c, se_c
149	
150	
151	# ── Confusion Matrix Estimators ───────────────────────────────────────────────
152	
153	def estimate_cm_mle(counts, labels):
154	    """Per-subgroup MLE with Laplace smoothing (add-1)."""
155	    C = {}
156	    for i, s in enumerate(labels):
157	        C_s = np.zeros((2, 2))
158	        for z in [0, 1]:
159	            n = counts[i, z, :].sum()
160	            for zh in [0, 1]:
161	                C_s[z, zh] = (counts[i, z, zh] + 1) / (n + 2) if n > 0 else 0.5
162	        C[s] = C_s
163	    return C
164	
165	
166	def _dirmult_neg_ll(alpha, counts_z):
167	    """Negative log marginal likelihood for Dirichlet-Multinomial."""
168	    a = alpha / 2.0
169	    if a < 1e-10:
170	        return 1e10
171	    ll = 0.0
172	    for c0, c1 in counts_z:
173	        n = c0 + c1
174	        if n == 0:
175	            continue
176	        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)
177	        ll -= 2 * gammaln(a) - gammaln(2 * a)
178	    return -ll
179	
180	
181	def estimate_cm_hb_eb(counts, labels):
182	    """Empirical Bayes HB: optimize shared Dirichlet concentration, posterior mean."""
183	    k = len(labels)
184	    alpha_opt = np.zeros(2)
185	    for z in [0, 1]:
186	        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
187	        total = sum(c0 + c1 for c0, c1 in cl)
188	        if total == 0:
189	            alpha_opt[z] = 2.0
190	            continue
191	        res = minimize_scalar(
192	            lambda a: _dirmult_neg_ll(a, cl), bounds=(0.01, 500), method='bounded')
193	        alpha_opt[z] = res.x
194	
195	    C = {}
196	    for i, s in enumerate(labels):
197	        C_s = np.zeros((2, 2))
198	        for z in [0, 1]:
199	            a = alpha_opt[z] / 2.0
200	            n = counts[i, z, :].sum()
201	            d = n + 2 * a
202	            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5
203	            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5
204	        C[s] = C_s
205	
206	    diag = {'rhat_max': np.nan, 'ess_min': np.nan, 'divergent_count': 0,
207	            'runtime_seconds': 0.0, 'hb_method': 'eb',
208	            'alpha_0_z0': alpha_opt[0], 'alpha_0_z1': alpha_opt[1]}
209	    return C, diag
210	
211	
212	def _split_rhat(chains):
213	    """Split R-hat for a scalar parameter. chains: (n_chains, n_draws)."""
214	    parts = []
215	    for c in range(chains.shape[0]):
216	        half = chains.shape[1] // 2
217	        parts.append(chains[c, :half])
218	        parts.append(chains[c, half:2 * half])
219	    parts = np.array(parts)
220	    m = parts.shape[0]
221	    n = parts.shape[1]
222	    chain_means = parts.mean(axis=1)
223	    W = np.mean(np.var(parts, axis=1, ddof=1))
224	    B = n * np.var(chain_means, ddof=1)
225	    if W < 1e-20:
226	        return 1.0
227	    var_hat = (1 - 1.0 / n) * W + B / n
228	    return float(np.sqrt(var_hat / W))
229	
230	
231	def _bulk_ess(chains):
232	    """Approximate bulk ESS via initial positive sequence. chains: (n_chains, n_draws)."""
233	    x = chains.ravel()
234	    n = len(x)
235	    mu = x.mean()
236	    xc = x - mu
237	    max_lag = min(n // 2, 300)
238	    c0 = np.dot(xc, xc)
239	    if c0 < 1e-20:
240	        return float(n)
241	    tau = 1.0
242	    for lag in range(1, max_lag - 1, 2):
243	        r1 = np.dot(xc[:n - lag], xc[lag:]) / c0
244	        r2 = np.dot(xc[:n - lag - 1], xc[lag + 1:]) / c0 if lag + 1 < n else 0
245	        pair = r1 + r2
246	        if pair < 0:
247	            break
248	        tau += 2 * pair
249	    return float(n / tau)
250	
251	
252	def _fast_diagnostics(alpha_arr, theta_arr, labels):
253	    """Compute R-hat and ESS over all parameters without arviz."""
254	    rhats, esss = [], []
255	    for d in range(alpha_arr.shape[2]):
256	        rhats.append(_split_rhat(alpha_arr[:, :, d]))
257	        esss.append(_bulk_ess(alpha_arr[:, :, d]))
258	    k = len(labels)
259	    for i in range(k):
260	        for z in [0, 1]:
261	            for zh in range(theta_arr.shape[4]):
262	                ch = theta_arr[:, :, i, z, zh]
263	                rhats.append(_split_rhat(ch))
264	                esss.append(_bulk_ess(ch))
265	    return max(rhats), min(esss)
266	
267	
268	def _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):
269	    """Log posterior for alpha_0[z] in log-alpha space (includes Jacobian)."""
270	    if alpha < 1e-10:
271	        return -1e10
272	    a = alpha / 2.0
273	    k = theta_z.shape[0]
274	    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha
275	    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))
276	    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))
277	    return lp
278	
279	
280	def estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=4000, n_warmup=2000, n_chains=4,
281	                         hp_a0=3.0, hp_b0=1.0):
282	    """Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).
283	
284	    hp_a0, hp_b0: Gamma hyperprior shape/rate on alpha_0 (default Gamma(3,1)).
285	    """
286	    k = len(labels)
287	    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),
288	                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]
289	    chain_inits = chain_inits_pool[:n_chains]
290	    all_alpha, all_theta = [], []
291	    t0 = time.time()
292	
293	    for chain in range(n_chains):
294	        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)
295	        alpha = chain_inits[chain].copy()
296	        theta = np.ones((k, 2, 2)) * 0.5
297	        mh_scale = np.array([0.3, 0.3])
298	        accept_ct = np.array([0, 0])
299	        attempt_ct = np.array([0, 0])
300	
301	        alpha_samples = np.zeros((n_iter, 2))
302	        theta_samples = np.zeros((n_iter, k, 2, 2))
303	
304	        for it in range(n_warmup + n_iter):
305	            for z in [0, 1]:
306	                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0
307	                post_a = np.maximum(post_a, 1e-6)
308	                g = rng.gamma(post_a)
309	                g_sum = g.sum(axis=1, keepdims=True)
310	                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)
311	
312	            for z in [0, 1]:
313	                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])
314	                a_prop = np.exp(x_prop)
315	                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -
316	                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))
317	                accepted = np.log(rng.rand()) < log_r
318	                if accepted:
319	                    alpha[z] = a_prop
320	                if it < n_warmup:
321	                    accept_ct[z] += int(accepted)
322	                    attempt_ct[z] += 1
323	
324	            if it < n_warmup and it > 0 and it % 100 == 0:
325	                for z in [0, 1]:
326	                    rate = accept_ct[z] / max(attempt_ct[z], 1)
327	                    if rate < 0.2:
328	                        mh_scale[z] *= 0.7
329	                    elif rate > 0.5:
330	                        mh_scale[z] *= 1.3
331	                    accept_ct[z] = 0
332	                    attempt_ct[z] = 0
333	
334	            if it >= n_warmup:
335	                idx = it - n_warmup
336	                alpha_samples[idx] = alpha.copy()
337	                theta_samples[idx] = theta.copy()
338	
339	        all_alpha.append(alpha_samples)
340	        all_theta.append(theta_samples)
341	
342	    runtime = time.time() - t0
343	    alpha_arr = np.stack(all_alpha)
344	    theta_arr = np.stack(all_theta)
345	
346	    C = {}
347	    for i, s in enumerate(labels):
348	        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))
349	
350	    rhat_max, ess_min = _fast_diagnostics(alpha_arr, theta_arr, labels)
351	
352	    diag = {'rhat_max': rhat_max, 'ess_min': ess_min, 'divergent_count': 0,
353	            'runtime_seconds': runtime, 'hb_method': 'gibbs'}
354	    return C, diag
355	
356	
357	def estimate_cm_hb_mcmc(counts, labels, seed=42, draws=1000, tune=500, chains=2):
358	    """Full Bayesian HB with PyMC MCMC."""
359	    k = len(labels)
360	    n_per_sz = counts.sum(axis=2)
361	
362	    with pm.Model():
363	        alpha_0 = pm.Gamma('alpha_0', alpha=2, beta=1, shape=2)
364	        for z in [0, 1]:
365	            for i, s in enumerate(labels):
366	                nsz = int(n_per_sz[i, z])
367	                if nsz == 0:
368	                    continue
369	                a = pt.stack([alpha_0[z] / 2, alpha_0[z] / 2])
370	                theta = pm.Dirichlet(f'theta_{s}_z{z}', a=a)
371	                pm.Multinomial(f'obs_{s}_z{z}', n=nsz, p=theta,
372	                               observed=counts[i, z, :].astype('int32'))
373	        t0 = time.time()
374	        trace = pm.sample(draws=draws, tune=tune, chains=chains,
375	                          random_seed=seed, progressbar=False)
376	        runtime = time.time() - t0
377	
378	    C = {}
379	    for i, s in enumerate(labels):
380	        C_s = np.zeros((2, 2))
381	        for z in [0, 1]:
382	            vn = f'theta_{s}_z{z}'
383	            if vn in trace.posterior:
384	                C_s[z, :] = trace.posterior[vn].values.mean(axis=(0, 1))
385	            else:
386	                C_s[z, :] = 0.5
387	        C[s] = C_s
388	
389	    all_vars = list(trace.posterior.data_vars)
390	    try:
391	        summ = az.summary(trace, var_names=all_vars)
392	        rhat_max = float(summ['r_hat'].max())
393	        ess_min = float(summ['ess_bulk'].min())
394	    except Exception:
395	        rhat_max = ess_min = np.nan
396	    try:
397	        divergent = int(trace.sample_stats['diverging'].values.sum())
398	    except Exception:
399	        divergent = -1
400	
401	    diag = {'rhat_max': rhat_max, 'ess_min': ess_min,
402	            'divergent_count': divergent, 'runtime_seconds': runtime,
403	            'hb_method': 'mcmc'}
404	    return C, diag
405	
406	
407	# ── Single MC Run ─────────────────────────────────────────────────────────────
408	
409	def run_one_mc(regime_name, regime_params, n_expert, k, seed, hb_method='eb'):
410	    data = generate_data(regime_params, n_expert, k, seed)
411	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
412	    em = data['expert_mask']
413	    labels = SUBGROUP_LABELS[k]
414	    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']
415	
416	    counts = get_counts(Z[em], Z_hat[em], S[em], labels)
417	
418	    C_mle = estimate_cm_mle(counts, labels)
419	
420	    if hb_method == 'gibbs':
421	        C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed)
422	    elif hb_method == 'mcmc' and HAS_PYMC:
423	        try:
424	            C_hb, hb_diag = estimate_cm_hb_mcmc(counts, labels, seed=seed)
425	        except Exception:
426	            C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)
427	            hb_diag['hb_method'] = 'eb_fallback'
428	    else:
429	        C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)
430	
431	    # Global CM (pool all expert labels, Laplace)
432	    cg = counts.sum(axis=0)
433	    C_gl = np.zeros((2, 2))
434	    for z in [0, 1]:
435	        n = cg[z, :].sum()
436	        for zh in [0, 1]:
437	            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5
438	
439	    M_gl = build_mixing_matrix(C_gl)
440	    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}
441	    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}
442	
443	    base = {'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k, 'mc_run': seed}
444	    rows = []
445	
446	    for s in labels:
447	        sm = S == s
448	        th0_or, se0_or = diff_in_means(Y, T, sm & (Z == 0))
449	        th1_or, se1_or = diff_in_means(Y, T, sm & (Z == 1))
450	        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))
451	        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))
452	
453	        tau_obs = np.array([th0_n, th1_n])
454	        se_obs = np.array([se0_n, se1_n])
455	        if np.any(np.isnan(tau_obs)):
456	            continue
457	
458	        tgc, sgc = invert_mixing(M_gl, tau_obs, se_obs)
459	        tml, sml = invert_mixing(M_mle[s], tau_obs, se_obs)
460	        thb, shb = invert_mixing(M_hb[s], tau_obs, se_obs)
461	
462	        def mr(method, th0, th1, se0, se1):
463	            return {**base, 'subgroup': s, 'method': method,
464	                    'tau_hat_z0': th0, 'tau_hat_z1': th1,
465	                    'se_z0': se0, 'se_z1': se1,
466	                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}
467	
468	        rows.append(mr('oracle', th0_or, th1_or, se0_or, se1_or))
469	        rows.append(mr('naive', th0_n, th1_n, se0_n, se1_n))
470	        rows.append(mr('global_corrected', tgc[0], tgc[1], sgc[0], sgc[1]))
471	        rows.append(mr('mle_laplace', tml[0], tml[1], sml[0], sml[1]))
472	        rows.append(mr('hb_dirichlet', thb[0], thb[1], shb[0], shb[1]))
473	
474	    return rows, {**base, **hb_diag}
475	
476	
477	# ── Aggregation ───────────────────────────────────────────────────────────────
478	
479	def aggregate_results(df):
480	    rows = []
481	    grp_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method']
482	    for keys, grp in df.groupby(grp_cols):
483	        regime, n_expert, k, subgroup, method = keys
484	        row = {'regime': regime, 'n_expert': int(n_expert), 'k_subgroups': int(k),
485	               'subgroup': subgroup, 'method': method}
486	        n_mc = len(grp)
487	        for z in ['z0', 'z1']:
488	            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values
489	            bias = err.mean()
490	            mse = (err ** 2).mean()
491	            rmse = np.sqrt(mse)
492	            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values
493	            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values
494	            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &
495	                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()
496	            row[f'bias_{z}'] = bias
497	            row[f'rmse_{z}'] = rmse
498	            row[f'coverage_{z}'] = cov
499	            row[f'bias_{z}_se'] = err.std() / np.sqrt(n_mc)
500	            mse_se = (err ** 2).std() / np.sqrt(n_mc)
501	            row[f'rmse_{z}_se'] = mse_se / (2 * rmse) if rmse > 1e-10 else np.nan
502	        rows.append(row)
503	    return pd.DataFrame(rows)
504	
505	
506	# ── Output ────────────────────────────────────────────────────────────────────
507	
508	def print_summary(df_agg, df_diag):
509	    pd.set_option('display.float_format', '{:.4f}'.format)
510	
511	    # MCMC / Gibbs diagnostics
512	    if 'hb_method' in df_diag.columns:
513	        for method_label in ['gibbs', 'mcmc']:
514	            mrows = df_diag[df_diag['hb_method'] == method_label]
515	            if mrows.empty:
516	                continue
517	            print(f"\n── {method_label.upper()} Diagnostics ──────────────────────────────")
518	            print(f"  Runs:           {len(mrows)}")
519	            rh = mrows['rhat_max'].dropna()
520	            es = mrows['ess_min'].dropna()
521	            if not rh.empty:
522	                print(f"  R-hat max:      {rh.max():.4f} (target < 1.01)")
523	            if not es.empty:
524	                print(f"  ESS min:        {es.min():.0f} (target > 200)")
525	            print(f"  Divergent total:{int(mrows['divergent_count'].sum())}")
526	            print(f"  Runtime median: {mrows['runtime_seconds'].median():.2f}s")
527	
528	    # Per-config HB vs MLE comparison
529	    print("\n── HB vs MLE RMSE Comparison (subgroup-level, averaged) ──")
530	    for k in sorted(df_agg['k_subgroups'].unique()):
531	        print(f"\n  K = {int(k)} subgroups")
532	        for regime in ['extreme', 'moderate', 'homogeneous']:
533	            sub = df_agg[(df_agg['k_subgroups'] == k) & (df_agg['regime'] == regime)]
534	            if sub.empty:
535	                continue
536	            print(f"    {regime}:")
537	            print(f"    {'n_exp':>6s}  {'oracle':>8s}  {'naive':>8s}  {'global':>8s}  "
538	                  f"{'mle':>8s}  {'hb':>8s}  {'HB vs MLE':>10s}")
539	            for ne in sorted(sub['n_expert'].unique()):
540	                vals = {}
541	                for m in ['oracle', 'naive', 'global_corrected', 'mle_laplace', 'hb_dirichlet']:
542	                    ms = sub[(sub['method'] == m) & (sub['n_expert'] == ne)]
543	                    if ms.empty:
544	                        vals[m] = np.nan
545	                    else:
546	                        vals[m] = np.sqrt((ms['rmse_z0'].values ** 2 +
547	                                           ms['rmse_z1'].values ** 2).mean())
548	                mle_v, hb_v = vals['mle_laplace'], vals['hb_dirichlet']
549	                pct = (mle_v - hb_v) / mle_v * 100 if mle_v > 1e-10 else 0
550	                tag = f"{pct:+.1f}%"
551	                print(f"    {int(ne):6d}  {vals['oracle']:8.4f}  {vals['naive']:8.4f}  "
552	                      f"{vals['global_corrected']:8.4f}  {mle_v:8.4f}  {hb_v:8.4f}  {tag:>10s}")
553	
554	
555	# ── Sweep ─────────────────────────────────────────────────────────────────────
556	
557	def run_sweep(regime_names, n_experts, k_list, n_mc,
558	              hb_method='eb', mcmc_diag_runs=5, verbose=True):
559	    all_rows, all_diag = [], []
560	    total = sum(1 for k in k_list for r in regime_names if r in REGIMES[k]) * len(n_experts) * n_mc
561	    count = 0
562	    t0 = time.time()
563	
564	    for k in k_list:
565	        for rn in regime_names:
566	            if rn not in REGIMES[k]:
567	                continue
568	            rp = REGIMES[k][rn]
569	            for ne in n_experts:
570	                for mc in range(n_mc):
571	                    use = hb_method
572	                    if hb_method == 'auto':
573	                        use = 'mcmc' if mc < mcmc_diag_runs else 'eb'
574	                    try:
575	                        rows, diag = run_one_mc(rn, rp, ne, k, seed=mc, hb_method=use)
576	                        all_rows.extend(rows)
577	                        all_diag.append(diag)
578	                    except Exception as e:
579	                        if verbose:
580	                            print(f"  WARN: k={k} {rn} ne={ne} mc={mc} failed: {e}")
581	                        all_diag.append({
582	                            'regime': rn, 'n_expert': ne, 'k_subgroups': k,
583	                            'mc_run': mc, 'hb_method': 'error',
584	                            'rhat_max': np.nan, 'ess_min': np.nan,
585	                            'divergent_count': -1, 'runtime_seconds': 0.0})
586	                    count += 1
587	                    if verbose and count % max(1, total // 20) == 0:
588	                        el = time.time() - t0
589	                        eta = el / count * (total - count)
590	                        print(f"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s | "
591	                              f"k={k} {rn} ne={ne} mc={mc}")
592	
593	    if verbose:
594	        print(f"  Sweep done: {time.time() - t0:.1f}s ({count} runs)")
595	    return pd.DataFrame(all_rows), pd.DataFrame(all_diag)
596	
597	
598	# ── Main ──────────────────────────────────────────────────────────────────────
599	
600	if __name__ == '__main__':
601	    parser = argparse.ArgumentParser()
602	    parser.add_argument('--n-mc', type=int, default=100)
603	    parser.add_argument('--dry-run', action='store_true')
604	    parser.add_argument('--hb-method', choices=['auto', 'mcmc', 'gibbs', 'eb'], default='auto')
605	    parser.add_argument('--mcmc-diag-runs', type=int, default=5)
606	    args = parser.parse_args()
607	
608	    n_mc = 5 if args.dry_run else args.n_mc
609	    regime_names = ['moderate'] if args.dry_run else ['extreme', 'moderate', 'homogeneous']
610	    n_experts = [100] if args.dry_run else DEFAULT_N_EXPERTS
611	    k_list = [2] if args.dry_run else DEFAULT_K_LIST
612	
613	    print(f"exp-001 HB Synthetic Validation | PyMC={HAS_PYMC}")
614	    print(f"N={N} n_mc={n_mc} hb={args.hb_method}")
615	    print(f"Regimes={regime_names} n_experts={n_experts} K={k_list}\n")
616	
617	    # Timing test
618	    effective_method = args.hb_method
619	    d = generate_data(REGIMES[2]['moderate'], 100, 2, seed=9999)
620	    em = d['expert_mask']
621	    tc = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], ['A', 'B'])
622	
623	    if args.hb_method == 'auto':
624	        print("Timing Gibbs sampler...")
625	        t0 = time.time()
626	        _, dg = estimate_cm_hb_gibbs(tc, ['A', 'B'], seed=9999)
627	        gt = time.time() - t0
628	        print(f"  Gibbs: {gt:.2f}s | rhat={dg['rhat_max']:.3f} "
629	              f"ess={dg['ess_min']:.0f}")
630	        if gt < 5:
631	            effective_method = 'gibbs'
632	            print(f"  Fast enough → using Gibbs for all runs")
633	        else:
634	            effective_method = 'eb'
635	            print(f"  Slow → using EB")
636	    elif args.hb_method == 'mcmc' and HAS_PYMC:
637	        print("Timing PyMC MCMC...")
638	        t0 = time.time()
639	        try:
640	            _, dg = estimate_cm_hb_mcmc(tc, ['A', 'B'], seed=9999)
641	            mt = time.time() - t0
642	            print(f"  MCMC: {mt:.1f}s | rhat={dg['rhat_max']:.3f} "
643	                  f"ess={dg['ess_min']:.0f} div={dg['divergent_count']}")
644	        except Exception as e:
645	            print(f"  MCMC failed: {e} → falling back to Gibbs")
646	            effective_method = 'gibbs'
647	
648	    print(f"\nEffective method: {effective_method}\n")
649	
650	    df_raw, df_diag = run_sweep(
651	        regime_names, n_experts, k_list, n_mc,
652	        hb_method=effective_method, mcmc_diag_runs=args.mcmc_diag_runs)
653	
654	    df_agg = aggregate_results(df_raw)
655	
656	    os.makedirs('results', exist_ok=True)
657	    agg_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method',
658	                'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1',
659	                'bias_z0_se', 'rmse_z0_se', 'bias_z1_se', 'rmse_z1_se']
660	    df_agg[agg_cols].to_csv('results/exp001_hb_results.csv', index=False)
661	
662	    diag_cols = ['regime', 'n_expert', 'k_subgroups', 'mc_run',
663	                 'rhat_max', 'ess_min', 'divergent_count', 'runtime_seconds']
664	    save_cols = [c for c in diag_cols if c in df_diag.columns]
665	    if 'hb_method' in df_diag.columns:
666	        save_cols.insert(4, 'hb_method')
667	    df_diag[save_cols].to_csv('results/exp001_hb_diagnostics.csv', index=False)
668	
669	    print_summary(df_agg, df_diag)
670	
671	    print(f"\nSaved: results/exp001_hb_results.csv ({len(df_agg)} rows)")
672	    print(f"Saved: results/exp001_hb_diagnostics.csv ({len(df_diag)} rows)")
673	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "5bb92788-8d90-4d53-bd22-dd21d9f31b33",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nexp001_hb_synthetic.py - Hierarchical Bayesian EC-HTE Synthetic Validation (exp-001)\n\nCompares confusion matrix estimators for CATE correction under heterogeneous\nmisclassification across subgroups:\n  Oracle, Naive, Global-corrected, MLE (Laplace), HB Dirichlet (partial pooling)\n\nInput: Synthetic DGP parameters (regimes, expert budgets, subgroup counts)\nOutput: results/exp001_hb_results.csv, results/exp001_hb_diagnostics.csv\n\"\"\"\n\nimport argparse\nimport os\nimport sys\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\nfrom scipy.optimize import minimize_scalar\n\nwarnings.filterwarnings('ignore')\n\ntry:\n    import pymc as pm\n    import pytensor.tensor as pt\n    import arviz as az\n    HAS_PYMC = True\nexcept ImportError:\n    HAS_PYMC = False\n\nN = 5000\nSUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}\n\nREGIMES = {\n    2: {\n        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},\n        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},\n        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},\n    },\n    4: {\n        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},\n        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},\n        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},\n    },\n}\n\nDEFAULT_N_EXPERTS = [50, 100, 250, 500, 1000, 2000]\nDEFAULT_K_LIST = [2, 4]\n\n\n# ── DGP ───────────────────────────────────────────────────────────────────────\n\ndef generate_data(regime_params, n_expert, k, seed):\n    rng = np.random.RandomState(seed)\n    labels = SUBGROUP_LABELS[k]\n    T = rng.binomial(1, 0.5, N)\n    Z = rng.binomial(1, 0.5, N)\n    S = rng.choice(labels, N, p=[1.0 / k] * k)\n    X = rng.randn(N, 5)\n    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])\n    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)\n    mc_rates = np.zeros(N)\n    for i, s in enumerate(labels):\n        mc_rates[S == s] = regime_params['misclass'][i]\n    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)\n    idx = rng.choice(N, min(n_expert, N), replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[idx] = True\n    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, tau=tau, expert_mask=expert_mask)\n\n\n# ── Helpers ───────────────────────────────────────────────────────────────────\n\ndef diff_in_means(Y, T, mask):\n    t1, t0 = mask & (T == 1), mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    \"\"\"Confusion matrix counts per subgroup: (k, 2, 2) = [subgroup, true_z, z_hat].\"\"\"\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef build_mixing_matrix(C):\n    \"\"\"C[z, z_hat] → M[z_hat, z] via Bayes rule (assuming P(Z=0)=P(Z=1)=0.5).\n\n    NOTE: This assumes P(Z=0)=P(Z=1)=0.5, which is correct for this experiment's\n    DGP. For general P(Z), use the version in exp007 that takes p_z and p_z_hat.\n    \"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        cs = C[0, zh] + C[1, zh]\n        if cs > 0:\n            M[zh, 0] = C[0, zh] / cs\n            M[zh, 1] = C[1, zh] / cs\n        else:\n            M[zh, :] = 0.5\n    return M\n\n\ndef invert_mixing(M, tau_obs, se_obs):\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\ndef safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):\n    \"\"\"Invert mixing matrix with condition number guard.\n\n    When cond(M_s) > threshold, matrix inversion is numerically unstable.\n    Falls back to naive (no correction) to avoid catastrophic amplification.\n    \"\"\"\n    cond = np.linalg.cond(M_s)\n    if cond > cond_threshold:\n        return tau_obs.copy()\n    return np.linalg.solve(M_s, tau_obs)\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    \"\"\"Like invert_mixing but with condition number guard.\"\"\"\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# ── Confusion Matrix Estimators ───────────────────────────────────────────────\n\ndef estimate_cm_mle(counts, labels):\n    \"\"\"Per-subgroup MLE with Laplace smoothing (add-1).\"\"\"\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            n = counts[i, z, :].sum()\n            for zh in [0, 1]:\n                C_s[z, zh] = (counts[i, z, zh] + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    \"\"\"Negative log marginal likelihood for Dirichlet-Multinomial.\"\"\"\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_eb(counts, labels):\n    \"\"\"Empirical Bayes HB: optimize shared Dirichlet concentration, posterior mean.\"\"\"\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = 2.0\n            continue\n        res = minimize_scalar(\n            lambda a: _dirmult_neg_ll(a, cl), bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n = counts[i, z, :].sum()\n            d = n + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    diag = {'rhat_max': np.nan, 'ess_min': np.nan, 'divergent_count': 0,\n            'runtime_seconds': 0.0, 'hb_method': 'eb',\n            'alpha_0_z0': alpha_opt[0], 'alpha_0_z1': alpha_opt[1]}\n    return C, diag\n\n\ndef _split_rhat(chains):\n    \"\"\"Split R-hat for a scalar parameter. chains: (n_chains, n_draws).\"\"\"\n    parts = []\n    for c in range(chains.shape[0]):\n        half = chains.shape[1] // 2\n        parts.append(chains[c, :half])\n        parts.append(chains[c, half:2 * half])\n    parts = np.array(parts)\n    m = parts.shape[0]\n    n = parts.shape[1]\n    chain_means = parts.mean(axis=1)\n    W = np.mean(np.var(parts, axis=1, ddof=1))\n    B = n * np.var(chain_means, ddof=1)\n    if W < 1e-20:\n        return 1.0\n    var_hat = (1 - 1.0 / n) * W + B / n\n    return float(np.sqrt(var_hat / W))\n\n\ndef _bulk_ess(chains):\n    \"\"\"Approximate bulk ESS via initial positive sequence. chains: (n_chains, n_draws).\"\"\"\n    x = chains.ravel()\n    n = len(x)\n    mu = x.mean()\n    xc = x - mu\n    max_lag = min(n // 2, 300)\n    c0 = np.dot(xc, xc)\n    if c0 < 1e-20:\n        return float(n)\n    tau = 1.0\n    for lag in range(1, max_lag - 1, 2):\n        r1 = np.dot(xc[:n - lag], xc[lag:]) / c0\n        r2 = np.dot(xc[:n - lag - 1], xc[lag + 1:]) / c0 if lag + 1 < n else 0\n        pair = r1 + r2\n        if pair < 0:\n            break\n        tau += 2 * pair\n    return float(n / tau)\n\n\ndef _fast_diagnostics(alpha_arr, theta_arr, labels):\n    \"\"\"Compute R-hat and ESS over all parameters without arviz.\"\"\"\n    rhats, esss = [], []\n    for d in range(alpha_arr.shape[2]):\n        rhats.append(_split_rhat(alpha_arr[:, :, d]))\n        esss.append(_bulk_ess(alpha_arr[:, :, d]))\n    k = len(labels)\n    for i in range(k):\n        for z in [0, 1]:\n            for zh in range(theta_arr.shape[4]):\n                ch = theta_arr[:, :, i, z, zh]\n                rhats.append(_split_rhat(ch))\n                esss.append(_bulk_ess(ch))\n    return max(rhats), min(esss)\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    \"\"\"Log posterior for alpha_0[z] in log-alpha space (includes Jacobian).\"\"\"\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=4000, n_warmup=2000, n_chains=4,\n                         hp_a0=3.0, hp_b0=1.0):\n    \"\"\"Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).\n\n    hp_a0, hp_b0: Gamma hyperprior shape/rate on alpha_0 (default Gamma(3,1)).\n    \"\"\"\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_alpha, all_theta = [], []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        alpha_samples = np.zeros((n_iter, 2))\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                accepted = np.log(rng.rand()) < log_r\n                if accepted:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(accepted)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                idx = it - n_warmup\n                alpha_samples[idx] = alpha.copy()\n                theta_samples[idx] = theta.copy()\n\n        all_alpha.append(alpha_samples)\n        all_theta.append(theta_samples)\n\n    runtime = time.time() - t0\n    alpha_arr = np.stack(all_alpha)\n    theta_arr = np.stack(all_theta)\n\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n\n    rhat_max, ess_min = _fast_diagnostics(alpha_arr, theta_arr, labels)\n\n    diag = {'rhat_max': rhat_max, 'ess_min': ess_min, 'divergent_count': 0,\n            'runtime_seconds': runtime, 'hb_method': 'gibbs'}\n    return C, diag\n\n\ndef estimate_cm_hb_mcmc(counts, labels, seed=42, draws=1000, tune=500, chains=2):\n    \"\"\"Full Bayesian HB with PyMC MCMC.\"\"\"\n    k = len(labels)\n    n_per_sz = counts.sum(axis=2)\n\n    with pm.Model():\n        alpha_0 = pm.Gamma('alpha_0', alpha=2, beta=1, shape=2)\n        for z in [0, 1]:\n            for i, s in enumerate(labels):\n                nsz = int(n_per_sz[i, z])\n                if nsz == 0:\n                    continue\n                a = pt.stack([alpha_0[z] / 2, alpha_0[z] / 2])\n                theta = pm.Dirichlet(f'theta_{s}_z{z}', a=a)\n                pm.Multinomial(f'obs_{s}_z{z}', n=nsz, p=theta,\n                               observed=counts[i, z, :].astype('int32'))\n        t0 = time.time()\n        trace = pm.sample(draws=draws, tune=tune, chains=chains,\n                          random_seed=seed, progressbar=False)\n        runtime = time.time() - t0\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            vn = f'theta_{s}_z{z}'\n            if vn in trace.posterior:\n                C_s[z, :] = trace.posterior[vn].values.mean(axis=(0, 1))\n            else:\n                C_s[z, :] = 0.5\n        C[s] = C_s\n\n    all_vars = list(trace.posterior.data_vars)\n    try:\n        summ = az.summary(trace, var_names=all_vars)\n        rhat_max = float(summ['r_hat'].max())\n        ess_min = float(summ['ess_bulk'].min())\n    except Exception:\n        rhat_max = ess_min = np.nan\n    try:\n        divergent = int(trace.sample_stats['diverging'].values.sum())\n    except Exception:\n        divergent = -1\n\n    diag = {'rhat_max': rhat_max, 'ess_min': ess_min,\n            'divergent_count': divergent, 'runtime_seconds': runtime,\n            'hb_method': 'mcmc'}\n    return C, diag\n\n\n# ── Single MC Run ─────────────────────────────────────────────────────────────\n\ndef run_one_mc(regime_name, regime_params, n_expert, k, seed, hb_method='eb'):\n    data = generate_data(regime_params, n_expert, k, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n    labels = SUBGROUP_LABELS[k]\n    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']\n\n    counts = get_counts(Z[em], Z_hat[em], S[em], labels)\n\n    C_mle = estimate_cm_mle(counts, labels)\n\n    if hb_method == 'gibbs':\n        C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed)\n    elif hb_method == 'mcmc' and HAS_PYMC:\n        try:\n            C_hb, hb_diag = estimate_cm_hb_mcmc(counts, labels, seed=seed)\n        except Exception:\n            C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)\n            hb_diag['hb_method'] = 'eb_fallback'\n    else:\n        C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)\n\n    # Global CM (pool all expert labels, Laplace)\n    cg = counts.sum(axis=0)\n    C_gl = np.zeros((2, 2))\n    for z in [0, 1]:\n        n = cg[z, :].sum()\n        for zh in [0, 1]:\n            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5\n\n    M_gl = build_mixing_matrix(C_gl)\n    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}\n    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}\n\n    base = {'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k, 'mc_run': seed}\n    rows = []\n\n    for s in labels:\n        sm = S == s\n        th0_or, se0_or = diff_in_means(Y, T, sm & (Z == 0))\n        th1_or, se1_or = diff_in_means(Y, T, sm & (Z == 1))\n        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))\n\n        tau_obs = np.array([th0_n, th1_n])\n        se_obs = np.array([se0_n, se1_n])\n        if np.any(np.isnan(tau_obs)):\n            continue\n\n        tgc, sgc = invert_mixing(M_gl, tau_obs, se_obs)\n        tml, sml = invert_mixing(M_mle[s], tau_obs, se_obs)\n        thb, shb = invert_mixing(M_hb[s], tau_obs, se_obs)\n\n        def mr(method, th0, th1, se0, se1):\n            return {**base, 'subgroup': s, 'method': method,\n                    'tau_hat_z0': th0, 'tau_hat_z1': th1,\n                    'se_z0': se0, 'se_z1': se1,\n                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}\n\n        rows.append(mr('oracle', th0_or, th1_or, se0_or, se1_or))\n        rows.append(mr('naive', th0_n, th1_n, se0_n, se1_n))\n        rows.append(mr('global_corrected', tgc[0], tgc[1], sgc[0], sgc[1]))\n        rows.append(mr('mle_laplace', tml[0], tml[1], sml[0], sml[1]))\n        rows.append(mr('hb_dirichlet', thb[0], thb[1], shb[0], shb[1]))\n\n    return rows, {**base, **hb_diag}\n\n\n# ── Aggregation ───────────────────────────────────────────────────────────────\n\ndef aggregate_results(df):\n    rows = []\n    grp_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method']\n    for keys, grp in df.groupby(grp_cols):\n        regime, n_expert, k, subgroup, method = keys\n        row = {'regime': regime, 'n_expert': int(n_expert), 'k_subgroups': int(k),\n               'subgroup': subgroup, 'method': method}\n        n_mc = len(grp)\n        for z in ['z0', 'z1']:\n            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values\n            bias = err.mean()\n            mse = (err ** 2).mean()\n            rmse = np.sqrt(mse)\n            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values\n            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values\n            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &\n                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()\n            row[f'bias_{z}'] = bias\n            row[f'rmse_{z}'] = rmse\n            row[f'coverage_{z}'] = cov\n            row[f'bias_{z}_se'] = err.std() / np.sqrt(n_mc)\n            mse_se = (err ** 2).std() / np.sqrt(n_mc)\n            row[f'rmse_{z}_se'] = mse_se / (2 * rmse) if rmse > 1e-10 else np.nan\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# ── Output ────────────────────────────────────────────────────────────────────\n\ndef print_summary(df_agg, df_diag):\n    pd.set_option('display.float_format', '{:.4f}'.format)\n\n    # MCMC / Gibbs diagnostics\n    if 'hb_method' in df_diag.columns:\n        for method_label in ['gibbs', 'mcmc']:\n            mrows = df_diag[df_diag['hb_method'] == method_label]\n            if mrows.empty:\n                continue\n            print(f\"\\n── {method_label.upper()} Diagnostics ──────────────────────────────\")\n            print(f\"  Runs:           {len(mrows)}\")\n            rh = mrows['rhat_max'].dropna()\n            es = mrows['ess_min'].dropna()\n            if not rh.empty:\n                print(f\"  R-hat max:      {rh.max():.4f} (target < 1.01)\")\n            if not es.empty:\n                print(f\"  ESS min:        {es.min():.0f} (target > 200)\")\n            print(f\"  Divergent total:{int(mrows['divergent_count'].sum())}\")\n            print(f\"  Runtime median: {mrows['runtime_seconds'].median():.2f}s\")\n\n    # Per-config HB vs MLE comparison\n    print(\"\\n── HB vs MLE RMSE Comparison (subgroup-level, averaged) ──\")\n    for k in sorted(df_agg['k_subgroups'].unique()):\n        print(f\"\\n  K = {int(k)} subgroups\")\n        for regime in ['extreme', 'moderate', 'homogeneous']:\n            sub = df_agg[(df_agg['k_subgroups'] == k) & (df_agg['regime'] == regime)]\n            if sub.empty:\n                continue\n            print(f\"    {regime}:\")\n            print(f\"    {'n_exp':>6s}  {'oracle':>8s}  {'naive':>8s}  {'global':>8s}  \"\n                  f\"{'mle':>8s}  {'hb':>8s}  {'HB vs MLE':>10s}\")\n            for ne in sorted(sub['n_expert'].unique()):\n                vals = {}\n                for m in ['oracle', 'naive', 'global_corrected', 'mle_laplace', 'hb_dirichlet']:\n                    ms = sub[(sub['method'] == m) & (sub['n_expert'] == ne)]\n                    if ms.empty:\n                        vals[m] = np.nan\n                    else:\n                        vals[m] = np.sqrt((ms['rmse_z0'].values ** 2 +\n                                           ms['rmse_z1'].values ** 2).mean())\n                mle_v, hb_v = vals['mle_laplace'], vals['hb_dirichlet']\n                pct = (mle_v - hb_v) / mle_v * 100 if mle_v > 1e-10 else 0\n                tag = f\"{pct:+.1f}%\"\n                print(f\"    {int(ne):6d}  {vals['oracle']:8.4f}  {vals['naive']:8.4f}  \"\n                      f\"{vals['global_corrected']:8.4f}  {mle_v:8.4f}  {hb_v:8.4f}  {tag:>10s}\")\n\n\n# ── Sweep ─────────────────────────────────────────────────────────────────────\n\ndef run_sweep(regime_names, n_experts, k_list, n_mc,\n              hb_method='eb', mcmc_diag_runs=5, verbose=True):\n    all_rows, all_diag = [], []\n    total = sum(1 for k in k_list for r in regime_names if r in REGIMES[k]) * len(n_experts) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for k in k_list:\n        for rn in regime_names:\n            if rn not in REGIMES[k]:\n                continue\n            rp = REGIMES[k][rn]\n            for ne in n_experts:\n                for mc in range(n_mc):\n                    use = hb_method\n                    if hb_method == 'auto':\n                        use = 'mcmc' if mc < mcmc_diag_runs else 'eb'\n                    try:\n                        rows, diag = run_one_mc(rn, rp, ne, k, seed=mc, hb_method=use)\n                        all_rows.extend(rows)\n                        all_diag.append(diag)\n                    except Exception as e:\n                        if verbose:\n                            print(f\"  WARN: k={k} {rn} ne={ne} mc={mc} failed: {e}\")\n                        all_diag.append({\n                            'regime': rn, 'n_expert': ne, 'k_subgroups': k,\n                            'mc_run': mc, 'hb_method': 'error',\n                            'rhat_max': np.nan, 'ess_min': np.nan,\n                            'divergent_count': -1, 'runtime_seconds': 0.0})\n                    count += 1\n                    if verbose and count % max(1, total // 20) == 0:\n                        el = time.time() - t0\n                        eta = el / count * (total - count)\n                        print(f\"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s | \"\n                              f\"k={k} {rn} ne={ne} mc={mc}\")\n\n    if verbose:\n        print(f\"  Sweep done: {time.time() - t0:.1f}s ({count} runs)\")\n    return pd.DataFrame(all_rows), pd.DataFrame(all_diag)\n\n\n# ── Main ──────────────────────────────────────────────────────────────────────\n\nif __name__ == '__main__':\n    parser = argparse.ArgumentParser()\n    parser.add_argument('--n-mc', type=int, default=100)\n    parser.add_argument('--dry-run', action='store_true')\n    parser.add_argument('--hb-method', choices=['auto', 'mcmc', 'gibbs', 'eb'], default='auto')\n    parser.add_argument('--mcmc-diag-runs', type=int, default=5)\n    args = parser.parse_args()\n\n    n_mc = 5 if args.dry_run else args.n_mc\n    regime_names = ['moderate'] if args.dry_run else ['extreme', 'moderate', 'homogeneous']\n    n_experts = [100] if args.dry_run else DEFAULT_N_EXPERTS\n    k_list = [2] if args.dry_run else DEFAULT_K_LIST\n\n    print(f\"exp-001 HB Synthetic Validation | PyMC={HAS_PYMC}\")\n    print(f\"N={N} n_mc={n_mc} hb={args.hb_method}\")\n    print(f\"Regimes={regime_names} n_experts={n_experts} K={k_list}\\n\")\n\n    # Timing test\n    effective_method = args.hb_method\n    d = generate_data(REGIMES[2]['moderate'], 100, 2, seed=9999)\n    em = d['expert_mask']\n    tc = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], ['A', 'B'])\n\n    if args.hb_method == 'auto':\n        print(\"Timing Gibbs sampler...\")\n        t0 = time.time()\n        _, dg = estimate_cm_hb_gibbs(tc, ['A', 'B'], seed=9999)\n        gt = time.time() - t0\n        print(f\"  Gibbs: {gt:.2f}s | rhat={dg['rhat_max']:.3f} \"\n              f\"ess={dg['ess_min']:.0f}\")\n        if gt < 5:\n            effective_method = 'gibbs'\n            print(f\"  Fast enough → using Gibbs for all runs\")\n        else:\n            effective_method = 'eb'\n            print(f\"  Slow → using EB\")\n    elif args.hb_method == 'mcmc' and HAS_PYMC:\n        print(\"Timing PyMC MCMC...\")\n        t0 = time.time()\n        try:\n            _, dg = estimate_cm_hb_mcmc(tc, ['A', 'B'], seed=9999)\n            mt = time.time() - t0\n            print(f\"  MCMC: {mt:.1f}s | rhat={dg['rhat_max']:.3f} \"\n                  f\"ess={dg['ess_min']:.0f} div={dg['divergent_count']}\")\n        except Exception as e:\n            print(f\"  MCMC failed: {e} → falling back to Gibbs\")\n            effective_method = 'gibbs'\n\n    print(f\"\\nEffective method: {effective_method}\\n\")\n\n    df_raw, df_diag = run_sweep(\n        regime_names, n_experts, k_list, n_mc,\n        hb_method=effective_method, mcmc_diag_runs=args.mcmc_diag_runs)\n\n    df_agg = aggregate_results(df_raw)\n\n    os.makedirs('results', exist_ok=True)\n    agg_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method',\n                'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1',\n                'bias_z0_se', 'rmse_z0_se', 'bias_z1_se', 'rmse_z1_se']\n    df_agg[agg_cols].to_csv('results/exp001_hb_results.csv', index=False)\n\n    diag_cols = ['regime', 'n_expert', 'k_subgroups', 'mc_run',\n                 'rhat_max', 'ess_min', 'divergent_count', 'runtime_seconds']\n    save_cols = [c for c in diag_cols if c in df_diag.columns]\n    if 'hb_method' in df_diag.columns:\n        save_cols.insert(4, 'hb_method')\n    df_diag[save_cols].to_csv('results/exp001_hb_diagnostics.csv', index=False)\n\n    print_summary(df_agg, df_diag)\n\n    print(f\"\\nSaved: results/exp001_hb_results.csv ({len(df_agg)} rows)\")\n    print(f\"Saved: results/exp001_hb_diagnostics.csv ({len(df_diag)} rows)\")\n",
      "numLines": 673,
      "startLine": 1,
      "totalLines": 673
    }
  }
}
```

</details>

---

### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "api_retry",
  "attempt": 1,
  "max_retries": 10,
  "retry_delay_ms": 562.4751197170173,
  "error_status": null,
  "error": "unknown",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "383d4dcb-5988-452d-8d78-c1603e896c19"
}
```

---

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "api_retry",
  "attempt": 2,
  "max_retries": 10,
  "retry_delay_ms": 1212.1375058451458,
  "error_status": null,
  "error": "unknown",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "fa20659d-de5a-4b20-9f09-51dcc095b604"
}
```

---

### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "api_retry",
  "attempt": 3,
  "max_retries": 10,
  "retry_delay_ms": 2336.339585906863,
  "error_status": null,
  "error": "unknown",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "539f8e03-d5d0-46d9-ba63-f305ae0c4a85"
}
```

---

### System

_source line 57_

```json
{
  "type": "system",
  "subtype": "api_retry",
  "attempt": 4,
  "max_retries": 10,
  "retry_delay_ms": 4263.6814394523735,
  "error_status": null,
  "error": "unknown",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "5900c08c-4092-4908-9295-c68d0d9dd940"
}
```

---

### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "api_retry",
  "attempt": 5,
  "max_retries": 10,
  "retry_delay_ms": 8241.52872132213,
  "error_status": null,
  "error": "unknown",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "1f0442ca-06a2-4fd2-b8f4-cc9a5f7f74af"
}
```

---

### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "api_retry",
  "attempt": 6,
  "max_retries": 10,
  "retry_delay_ms": 16647.342379089674,
  "error_status": null,
  "error": "unknown",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "1c13d625-e469-43a6-88f1-2e914779d53c"
}
```

---

### System

_source line 60_

```json
{
  "type": "system",
  "subtype": "api_retry",
  "attempt": 7,
  "max_retries": 10,
  "retry_delay_ms": 37266.301148215556,
  "error_status": null,
  "error": "unknown",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "bf163d44-3509-42da-bfec-d63123cb0d0c"
}
```

---

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "api_retry",
  "attempt": 8,
  "max_retries": 10,
  "retry_delay_ms": 38840.59679055462,
  "error_status": null,
  "error": "unknown",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "94b42a6a-3eaf-4e6b-a5db-6fe1b4b1d005"
}
```

---

### System

_source line 62_

```json
{
  "type": "system",
  "subtype": "api_retry",
  "attempt": 9,
  "max_retries": 10,
  "retry_delay_ms": 35201.05437520397,
  "error_status": null,
  "error": "unknown",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "3a402837-ce90-4ed3-b00d-fe066a60189f"
}
```

---

### System

_source line 63_

```json
{
  "type": "system",
  "subtype": "api_retry",
  "attempt": 10,
  "max_retries": 10,
  "retry_delay_ms": 36801.46182743234,
  "error_status": null,
  "error": "unknown",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "ea900df9-05ee-4086-93c2-c029453817d7"
}
```

---

### Assistant

_source line 64_

Request timed out

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "uuid": "1fca80ac-9bf5-4e52-8b9f-ec98b3242d25",
  "error": "unknown",
  "message": {
    "id": "6d802b3a-adf1-4118-a3ae-c3eab8142325",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 65_

Request timed out

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": true,
  "api_error_status": null,
  "duration_ms": 4097481,
  "duration_api_ms": 115098,
  "num_turns": 5,
  "stop_reason": "stop_sequence",
  "session_id": "4bf3e1e5-5595-4dba-a7f1-93c53c64093a",
  "total_cost_usd": 0.2968093,
  "usage": {
    "input_tokens": 3,
    "cache_creation_input_tokens": 12066,
    "cache_read_input_tokens": 30760,
    "output_tokens": 2493,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 12066,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2187,
        "cache_read_input_tokens": 18919,
        "cache_creation_input_tokens": 4988,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4988
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2216,
      "outputTokens": 5780,
      "cacheReadInputTokens": 270083,
      "cacheCreationInputTokens": 68442,
      "webSearchRequests": 0,
      "costUSD": 0.14367680000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 3,
      "outputTokens": 2493,
      "cacheReadInputTokens": 30760,
      "cacheCreationInputTokens": 12066,
      "webSearchRequests": 0,
      "costUSD": 0.1531325,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9ce3f012-2d18-49b2-ad23-4c866c517e01"
}
```

</details>

---
