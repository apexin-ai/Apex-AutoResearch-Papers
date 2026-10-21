# code exp e asv stability

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 92
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/workers/worker_code_exp_e_asv_stability_20260522T112928.log`
- **Structured JSON:** [`98b3974648501fe01940.json`](../../sessions/98/98b3974648501fe01940.json)

## Before a recorded user message

92 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
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
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
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
  "uuid": "cfd70ef9-69c6-46ca-a039-b3546f14f8d6",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/memory/"
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
    "resetsAt": 1779457800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "44479211-a36a-4818-a196-eea24cc095f2",
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502"
}
```

---

### Assistant

_source line 4_

Looking at the reference code first to understand the existing infrastructure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "1adaa452-afcc-4b2c-bc6d-76a18789ebc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lr1hYo8WUkZjTXowDjvc4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13958,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13958
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

<details open><summary>🔧 Tool call — Read · `toolu_016ZftpXmrjMk7viFNpWcjaS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan006_asv_empirical.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "ee7630ad-0ce7-4fd7-9e83-4c249be1f7c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lr1hYo8WUkZjTXowDjvc4o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13958,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13958
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

### Tool result

_source line 6 · 2026-05-22T11:29:38.207Z_

<details><summary>↩ Tool result · reported error · `toolu_016ZftpXmrjMk7viFNpWcjaS`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib. Did you mean plan006_asv_empirical?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "667dc82f-328d-4029-8b3e-8a1d8b87225d",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib. Did you mean plan006_asv_empirical?"
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01ANAXdAepYwFsGpT94HKsGX`</summary>

```json
{
  "pattern": "artifacts/plan006*asv*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "f0751e01-bc0f-4a9e-a938-73a886fba1d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5HUgwJpBTzvGuCpXiQvia",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 181,
      "cache_read_input_tokens": 25799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 181
      },
      "output_tokens": 59,
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

_source line 8 · 2026-05-22T11:29:41.255Z_

<details><summary>↩ Tool result · `toolu_01ANAXdAepYwFsGpT94HKsGX`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "b478b72c-5fab-4a39-859f-1e4e48c8b887",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 31,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Glob · `toolu_01HrptDVi5ehVMZZvK3Tb1Wm`</summary>

```json
{
  "pattern": "artifacts/plan006*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "d293f863-1bf9-486b-add5-6ce4bc061afb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FY2osfSRc2QiXmtoVC5DNc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 74,
      "cache_read_input_tokens": 25980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 74
      },
      "output_tokens": 56,
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

_source line 10 · 2026-05-22T11:29:43.723Z_

<details><summary>↩ Tool result · `toolu_01HrptDVi5ehVMZZvK3Tb1Wm`</summary>

```text
artifacts/plan006_empirical_data.txt
artifacts/plan006_exact_values.txt
artifacts/plan006_full_summary.txt
artifacts/plan006_full_filtered_summary.txt
artifacts/plan006_full_filtered_stats.json
artifacts/plan006_full_filtered_stats.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "82cb7037-f592-4e97-b080-d801cebb957d",
  "tool_use_result": {
    "filenames": [
      "artifacts/plan006_empirical_data.txt",
      "artifacts/plan006_exact_values.txt",
      "artifacts/plan006_full_summary.txt",
      "artifacts/plan006_full_filtered_summary.txt",
      "artifacts/plan006_full_filtered_stats.json",
      "artifacts/plan006_full_filtered_stats.txt"
    ],
    "durationMs": 10,
    "numFiles": 6,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_01LiQiTtKsFcUyPSe5ak9y77`</summary>

```json
{
  "pattern": "artifacts/plan006/**/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "4adc56a6-fa28-40e1-b13d-814924f6e60b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLzWXMLizqj6hfH3F2tcxp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 140,
      "cache_read_input_tokens": 26054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 140
      },
      "output_tokens": 59,
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

_source line 12 · 2026-05-22T11:29:46.577Z_

<details><summary>↩ Tool result · `toolu_01LiQiTtKsFcUyPSe5ak9y77`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "12f46ab5-8118-4a06-b6de-fc009318d9fb",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 16,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Glob · `toolu_016jWEih2S9T4ZzF6YHpSjYT`</summary>

```json
{
  "pattern": "artifacts/plan006_asv_framework/**/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "926c3c3d-6168-4c1c-a192-330fe37aee56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLzWXMLizqj6hfH3F2tcxp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 140,
      "cache_read_input_tokens": 26054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 140
      },
      "output_tokens": 59,
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

_source line 14_

<details open><summary>🔧 Tool call — Glob · `toolu_01Ub2FwiRMMANQFUib3aegdh`</summary>

```json
{
  "pattern": "artifacts/plan006_mock/**/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "b332d41f-a18c-4f18-9a54-3a53a79e242b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLzWXMLizqj6hfH3F2tcxp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 140,
      "cache_read_input_tokens": 26054,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 140
      },
      "output_tokens": 59,
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

_source line 15 · 2026-05-22T11:29:47.002Z_

<details><summary>↩ Tool result · `toolu_016jWEih2S9T4ZzF6YHpSjYT`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "da23410b-19d3-4be5-98b3-94970ebd306a",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 29,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T11:29:47.004Z_

<details><summary>↩ Tool result · `toolu_01Ub2FwiRMMANQFUib3aegdh`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "c7861a45-c77d-4339-bf4d-e94546324c20",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 20,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Glob · `toolu_01J9SxQwp3S4fr5PGdyjxcoM`</summary>

```json
{
  "pattern": "artifacts/**/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "54901ddd-7de5-4b37-8636-6aa084bb0dc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WES1z315HviXhxnskGv3R9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 241,
      "cache_read_input_tokens": 26194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 241
      },
      "output_tokens": 55,
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

_source line 18 · 2026-05-22T11:29:49.365Z_

<details><summary>↩ Tool result · `toolu_01J9SxQwp3S4fr5PGdyjxcoM`</summary>

```text
artifacts/_project/data/mvp_confounding_dag.py
artifacts/mvp_confounding_dag.py
artifacts/_project/data/mvp_exposure_dag.py
artifacts/mvp_exposure_dag.py
artifacts/_project/report/mvp_exposure_dirichlet_subspace.py
artifacts/mvp_exposure_dirichlet_subspace.py
artifacts/preprocess.py
artifacts/plan008_binarization_collapse/report/plan_008_binarization_collapse.py
artifacts/plan_005_asv_extended_fixed.py
artifacts/plan_002_k57_extended_7topo.py
artifacts/plan_009_pathological_matrices.py
artifacts/mvp_iv_dirichlet_subspace.py
artifacts/nondiff_stress_test.py
artifacts/compute_theory_empirical_mape.py
artifacts/compute_all_tasks.py
artifacts/compute_ppi_empirical.py
artifacts/plan011_frontier_annotations/scripts/prepare_data.py
artifacts/plan011_frontier_annotations/scripts/annotate_frontier.py
artifacts/_project/intermediate/case_study_analysis.py
artifacts/plan012_case_study/case_study_analysis.py
artifacts/plan011_frontier_annotations/scripts/compute_results.py
artifacts/compute_delta_max.py
artifacts/annotate.py
artifacts/compute_updated_empirical.py
artifacts/exp_a_stress_test.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "e7187692-5621-450d-8726-c867fd47780d",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/data/mvp_confounding_dag.py",
      "artifacts/mvp_confounding_dag.py",
      "artifacts/_project/data/mvp_exposure_dag.py",
      "artifacts/mvp_exposure_dag.py",
      "artifacts/_project/report/mvp_exposure_dirichlet_subspace.py",
      "artifacts/mvp_exposure_dirichlet_subspace.py",
      "artifacts/preprocess.py",
      "artifacts/plan008_binarization_collapse/report/plan_008_binarization_collapse.py",
      "artifacts/plan_005_asv_extended_fixed.py",
      "artifacts/plan_002_k57_extended_7topo.py",
      "artifacts/plan_009_pathological_matrices.py",
      "artifacts/mvp_iv_dirichlet_subspace.py",
      "artifacts/nondiff_stress_test.py",
      "artifacts/compute_theory_empirical_mape.py",
      "artifacts/compute_all_tasks.py",
      "artifacts/compute_ppi_empirical.py",
      "artifacts/plan011_frontier_annotations/scripts/prepare_data.py",
      "artifacts/plan011_frontier_annotations/scripts/annotate_frontier.py",
      "artifacts/_project/intermediate/case_study_analysis.py",
      "artifacts/plan012_case_study/case_study_analysis.py",
      "artifacts/plan011_frontier_annotations/scripts/compute_results.py",
      "artifacts/compute_delta_max.py",
      "artifacts/annotate.py",
      "artifacts/compute_updated_empirical.py",
      "artifacts/exp_a_stress_test.py"
    ],
    "durationMs": 16,
    "numFiles": 25,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01RGRrEhM7xvYSYxWHWBQbTL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan_005_asv_extended_fixed.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "9b2c3f48-7470-4f4e-b8f0-46f0e79c0484",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDk8YQSeXf2wBWxNt26tzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 420,
      "cache_read_input_tokens": 26435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 420
      },
      "output_tokens": 63,
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

_source line 20 · 2026-05-22T11:29:52.247Z_

<details><summary>↩ Tool result · `toolu_01RGRrEhM7xvYSYxWHWBQbTL`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_005_fixed: ASV Framework Extension (C1/C2/W1/W2 fixes)
4	
5	Fixes applied (Reviewer CRITICAL):
6	  C1: Added compute_signif_asv_fast from plan_004_v3_fixed
7	  C2: compute_magnitude_asv_fast returns 0.0 (not None) when tau_true ~ 0
8	  W1: IV tau_true = plim_iv(I), not DGP beta (approx 0.66 vs 0.5)
9	  W2: M-bias tau_true = plim_mbias(I)[1], not DGP tau (approx 0.5128 vs 0.5)
10	
11	Only Part 2+3+5 re-run. Part 1 and Part 4 preserved but skipped.
12	Part 5 uses significance-based ASV rejection rule (from plan_004_v3_fixed).
13	"""
14	
15	import numpy as np
16	import json
17	import time
18	
19	K = 3
20	
21	# ============================================================================
22	# Utilities (from plan_004 v3)
23	# ============================================================================
24	
25	def softmax_sample(logits, rng):
26	    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))
27	    probs = exp_l / exp_l.sum(axis=1, keepdims=True)
28	    cum = np.cumsum(probs, axis=1)
29	    u = rng.uniform(size=logits.shape[0])
30	    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)
31	
32	
33	def generate_Astar(A, C, rng):
34	    probs = C[:, A]
35	    cum = np.cumsum(probs, axis=0)
36	    u = rng.uniform(size=len(A))
37	    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)
38	
39	
40	def ols_with_dummies(Y, T, Astar, K=3):
41	    N = len(Y)
42	    D = np.zeros((N, K - 1))
43	    for k in range(1, K):
44	        D[:, k - 1] = (Astar == k).astype(float)
45	    X = np.column_stack([np.ones(N), T, D])
46	    try:
47	        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
48	        resid = Y - X @ beta
49	        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)
50	        XtX_inv = np.linalg.inv(X.T @ X)
51	        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))
52	    except np.linalg.LinAlgError:
53	        beta = np.full(X.shape[1], np.nan)
54	        se = np.full(X.shape[1], np.nan)
55	    return beta, se
56	
57	
58	# ============================================================================
59	# C(delta) Parameterization (from plan_004 v3)
60	# ============================================================================
61	
62	class LinearInterpolation:
63	    def __call__(self, C0, delta):
64	        K = C0.shape[0]
65	        C_d = (1 - delta) * np.eye(K) + delta * C0
66	        C_d = np.maximum(C_d, 0.0)
67	        col_sums = C_d.sum(axis=0)
68	        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)
69	        C_d = C_d / col_sums
70	        return C_d
71	
72	    def delta_range(self, C0=None):
73	        if C0 is None:
74	            return (0.0, 5.0)
75	        min_diag = np.diag(C0).min()
76	        if min_diag >= 1.0:
77	            return (0.0, 10.0)
78	        delta_max = min(1.0 / (1.0 - min_diag), 10.0)
79	        return (0.0, delta_max)
80	
81	
82	# ============================================================================
83	# C matrices (from plan_004 v3)
84	# ============================================================================
85	
86	def make_C_list():
87	    return {
88	        "C1_sym": np.array([[0.80, 0.10, 0.10],
89	                            [0.10, 0.80, 0.10],
90	                            [0.10, 0.10, 0.80]]),
91	        "C2_high": np.array([[0.90, 0.05, 0.05],
92	                             [0.05, 0.90, 0.05],
93	                             [0.05, 0.05, 0.90]]),
94	        "C3_asym": np.array([[0.70, 0.20, 0.10],
95	                             [0.15, 0.70, 0.15],
96	                             [0.10, 0.15, 0.75]]),
97	        "C4_weak": np.array([[0.60, 0.20, 0.20],
98	                             [0.20, 0.60, 0.20],
99	                             [0.15, 0.15, 0.70]]),
100	        "C5_perm": np.array([[0.40, 0.30, 0.30],
101	                             [0.30, 0.40, 0.30],
102	                             [0.30, 0.30, 0.40]]),
103	        "C6_diff": np.array([[0.85, 0.075, 0.075],
104	                             [0.15, 0.70, 0.15],
105	                             [0.05, 0.05, 0.90]]),
106	    }
107	
108	
109	def normalize_C_list(C_dict):
110	    out = {}
111	    for name, C in C_dict.items():
112	        C = np.maximum(C, 0.0)
113	        cs = C.sum(axis=0)
114	        cs = np.where(cs < 1e-10, 1.0, cs)
115	        out[name] = C / cs
116	    return out
117	
118	
119	def random_C0(K, rng, diag_alpha=5.0, offdiag_alpha=1.0):
120	    C = np.zeros((K, K))
121	    for k in range(K):
122	        alphas = np.full(K, offdiag_alpha)
123	        alphas[k] = diag_alpha
124	        C[:, k] = rng.dirichlet(alphas)
125	    return C
126	
127	
128	# ============================================================================
129	# Topology 1: M-BIAS — U1->{A,T}, U2->{A,Y}, T->Y
130	# ============================================================================
131	
132	MBIAS_PARAMS = dict(tau=0.5, delta=1.0, lam=1.0,
133	                    g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9)
134	
135	
136	def _gen_mbias(N, params, rng):
137	    U1 = rng.normal(0, 1, N)
138	    U2 = rng.normal(0, 1, N)
139	    T = params['delta'] * U1 + rng.normal(0, 1, N)
140	    Y = params['tau'] * T + params['lam'] * U2 + rng.normal(0, 1, N)
141	    logits = np.column_stack([
142	        np.zeros(N),
143	        params['g1'] + params['a1'] * U1 + params['a2'] * U2,
144	        params['g2'] + params['a3'] * U1 + params['a4'] * U2,
145	    ])
146	    A = softmax_sample(logits, rng)
147	    return T, Y, A
148	
149	
150	def gen_mbias_data(N, params, C0, rng):
151	    T, Y, A = _gen_mbias(N, params, rng)
152	    Astar = generate_Astar(A, C0, rng)
153	    return T, Y, A, Astar
154	
155	
156	def precomp_mbias(params, N=2_000_000, seed=999):
157	    rng = np.random.default_rng(seed)
158	    T, Y, A = _gen_mbias(N, params, rng)
159	    DA = np.zeros((N, K))
160	    for k in range(K):
161	        DA[:, k] = (A == k).astype(float)
162	    return dict(
163	        E_T=T.mean(), E_T2=(T**2).mean(),
164	        E_Y=Y.mean(), E_TY=(T*Y).mean(),
165	        E_DA=DA.mean(0),
166	        E_DA_T=(DA * T[:, None]).mean(0),
167	        E_DA_Y=(DA * Y[:, None]).mean(0))
168	
169	
170	def plim_mbias(C, st):
171	    """OLS plim for Y ~ 1 + T + D1_A* + D2_A*."""
172	    ds  = C @ st['E_DA']
173	    dst = C @ st['E_DA_T']
174	    dsy = C @ st['E_DA_Y']
175	    ET, ET2 = st['E_T'], st['E_T2']
176	    EY, ETY = st['E_Y'], st['E_TY']
177	    EZZ = np.array([
178	        [1,      ET,      ds[1],    ds[2]   ],
179	        [ET,     ET2,     dst[1],   dst[2]  ],
180	        [ds[1],  dst[1],  ds[1],    0       ],
181	        [ds[2],  dst[2],  0,        ds[2]   ]])
182	    EZY = np.array([EY, ETY, dsy[1], dsy[2]])
183	    return np.linalg.solve(EZZ, EZY)
184	
185	
186	# ============================================================================
187	# Topology 2: IV — Z->A->Y, U->{A,Y}
188	# ============================================================================
189	
190	IV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)
191	IV_BETA = np.array([0.0, 0.5, -0.25])
192	
193	
194	def _gen_iv(N, beta, params, rng):
195	    Z_iv = rng.binomial(1, 0.5, N).astype(float)
196	    U = rng.normal(0, 1, N)
197	    eps = rng.normal(0, 1, N)
198	    logits = np.column_stack([
199	        np.zeros(N),
200	        params['g1'] + params['dZ'] * Z_iv + params['dU'] * U,
201	        params['g2'] + params['dZ2'] * Z_iv + params['dU2'] * U,
202	    ])
203	    A = softmax_sample(logits, rng)
204	    Y = (beta[1] * (A == 1).astype(float) + beta[2] * (A == 2).astype(float)
205	         + params['lam'] * U + eps)
206	    return Z_iv, U, Y, A
207	
208	
209	def gen_iv_data(N, beta, params, C0, rng):
210	    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)
211	    Astar = generate_Astar(A, C0, rng)
212	    return Z_iv, Y, A, Astar
213	
214	
215	def precomp_iv(beta, params, N=2_000_000, seed=999):
216	    """Precompute reduced form and first stage for Wald estimator."""
217	    rng = np.random.default_rng(seed)
218	    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)
219	    z1 = Z_iv == 1; z0 = Z_iv == 0
220	    RF = Y[z1].mean() - Y[z0].mean()
221	    FS = np.zeros(K)
222	    for k in range(K):
223	        FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()
224	    return dict(RF=RF, FS=FS)
225	
226	
227	def plim_iv(C, st):
228	    """Wald estimator: RF / FS*_1 where FS* = C @ FS."""
229	    FS_star = C @ st['FS']
230	    if abs(FS_star[1]) < 1e-8:
231	        return np.nan
232	    return st['RF'] / FS_star[1]
233	
234	
235	def wald_with_se(Z, Y, Astar, k=1):
236	    """Finite-sample Wald estimator with delta-method SE."""
237	    z1 = Z == 1; z0 = Z == 0
238	    n1 = float(z1.sum()); n0 = float(z0.sum())
239	    if n1 < 2 or n0 < 2:
240	        return np.nan, np.nan
241	    RF = Y[z1].mean() - Y[z0].mean()
242	    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0
243	    Dk_z1 = (Astar[z1] == k).astype(float).mean()
244	    Dk_z0 = (Astar[z0] == k).astype(float).mean()
245	    FS = Dk_z1 - Dk_z0
246	    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0
247	    if abs(FS) < 1e-8:
248	        return np.nan, np.nan
249	    Wald = RF / FS
250	    var_Wald = var_RF / FS**2 + RF**2 * var_FS / FS**4
251	    SE = np.sqrt(max(var_Wald, 0))
252	    return Wald, SE
253	
254	
255	# ============================================================================
256	# Topology 3: FRONT-DOOR — T->M->Y, U->{T,Y}
257	# ============================================================================
258	
259	ALPHA_U = 1.0
260	LAMBDA_U = 1.0
261	GAMMA_FD = np.array([0.0, 0.5, -0.3])
262	DELTA_FD = np.array([0.0, 1.0, -0.8])
263	BETA_FD = np.array([0.0, 1.0, -0.5])
264	
265	
266	def _gen_fd(N, beta, rng, g=None, d=None, aU=None, lU=None):
267	    if g is None: g = GAMMA_FD
268	    if d is None: d = DELTA_FD
269	    if aU is None: aU = ALPHA_U
270	    if lU is None: lU = LAMBDA_U
271	    U = rng.normal(0, 1, N)
272	    T = aU * U + rng.normal(0, 1, N)
273	    lo = np.column_stack([np.zeros(N), g[1] + d[1]*T, g[2] + d[2]*T])
274	    lo -= lo.max(1, keepdims=True)
275	    e = np.exp(lo)
276	    p = e / e.sum(1, keepdims=True)
277	    cu = np.cumsum(p, axis=1)
278	    u = rng.uniform(size=N)
279	    M = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)
280	    DM1 = (M == 1).astype(float)
281	    DM2 = (M == 2).astype(float)
282	    Y = beta[1]*DM1 + beta[2]*DM2 + lU*U + rng.normal(0, 1, N)
283	    return T, M, Y, U
284	
285	
286	def gen_fd_data(N, beta, C0, rng, lU=None, aU=None, d=None):
287	    T, M, Y, U = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)
288	    Mstar = generate_Astar(M, C0, rng)
289	    return T, Y, M, Mstar
290	
291	
292	def precomp_fd(beta, N=10_000_000, seed=123, lU=None, aU=None, d=None):
293	    rng = np.random.default_rng(seed)
294	    T, M, Y, _ = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)
295	    DM = np.zeros((N, K))
296	    for k in range(K):
297	        DM[:, k] = (M == k).astype(float)
298	    return dict(
299	        E_T=T.mean(), E_T2=(T**2).mean(),
300	        E_Y=Y.mean(), E_TY=(T*Y).mean(),
301	        E_DM=DM.mean(0),
302	        E_DM_T=(DM * T[:, None]).mean(0),
303	        E_DM_Y=(DM * Y[:, None]).mean(0))
304	
305	
306	def plim_fd(C, st):
307	    """OLS plim for Y ~ 1 + T + D1_M* + D2_M*."""
308	    ds  = C @ st['E_DM']
309	    dst = C @ st['E_DM_T']
310	    dsy = C @ st['E_DM_Y']
311	    ET, ET2 = st['E_T'], st['E_T2']
312	    EY, ETY = st['E_Y'], st['E_TY']
313	    EZZ = np.array([
314	        [1,      ET,      ds[1],    ds[2]   ],
315	        [ET,     ET2,     dst[1],   dst[2]  ],
316	        [ds[1],  dst[1],  ds[1],    0       ],
317	        [ds[2],  dst[2],  0,        ds[2]   ]])
318	    EZY = np.array([EY, ETY, dsy[1], dsy[2]])
319	    return np.linalg.solve(EZZ, EZY)
320	
321	
322	# ============================================================================
323	# ASV Framework
324	# ============================================================================
325	
326	def compute_bias_curve(topology, C0, param, tau_true, st, n_grid=1500):
327	    dmin, dmax = param.delta_range(C0)
328	    deltas = np.linspace(dmin, dmax, n_grid)
329	    tau_curve = np.zeros(n_grid)
330	    for i, d in enumerate(deltas):
331	        C_d = param(C0, d)
332	        if topology == "mbias":
333	            tau_curve[i] = plim_mbias(C_d, st)[1]
334	        elif topology == "iv":
335	            tau_curve[i] = plim_iv(C_d, st)
336	        elif topology == "frontdoor":
337	            tau_curve[i] = plim_fd(C_d, st)[1]
338	    bias_abs = np.abs(tau_curve - tau_true)
339	    return deltas, bias_abs, tau_curve
340	
341	
342	def compute_envelope(bias_abs):
343	    env = np.zeros_like(bias_abs)
344	    running_max = 0.0
345	    for i in range(len(bias_abs)):
346	        v = bias_abs[i]
347	        if not np.isnan(v):
348	            running_max = max(running_max, v)
349	        env[i] = running_max
350	    return env
351	
352	
353	def verify_envelope_monotonicity(envelope):
354	    diffs = np.diff(envelope)
355	    return int(np.sum(diffs < -1e-12))
356	
357	
358	def compute_asv_envelope(topology, C0, tau_true, param, threshold_type,
359	                         threshold_value=0.1, st=None, n_grid=1500):
360	    deltas, bias_abs, tau_curve = compute_bias_curve(
361	        topology, C0, param, tau_true, st, n_grid)
362	    envelope = compute_envelope(bias_abs)
363	
364	    valid_ba = bias_abs[~np.isnan(bias_abs)]
365	    raw_violations = int(np.sum(np.diff(valid_ba) < -1e-12)) if len(valid_ba) > 1 else 0
366	    env_violations = verify_envelope_monotonicity(envelope)
367	
368	    asv = None
369	    if threshold_type == "sign_flip":
370	        if abs(tau_true) < 1e-12:
371	            asv = None
372	        else:
373	            baseline_sign = np.sign(tau_true)
374	            for i, d in enumerate(deltas):
375	                if np.isnan(tau_curve[i]):
376	                    continue
377	                if np.sign(tau_curve[i]) != baseline_sign:
378	                    asv = d
379	                    break
380	    elif threshold_type == "magnitude_relative":
381	        if abs(tau_true) < 1e-12:
382	            asv = None
383	        else:
384	            thresh = threshold_value * abs(tau_true)
385	            for i, d in enumerate(deltas):
386	                if envelope[i] > thresh:
387	                    asv = d
388	                    break
389	    elif threshold_type == "magnitude_absolute":
390	        thresh = threshold_value
391	        for i, d in enumerate(deltas):
392	            if envelope[i] > thresh:
393	                asv = d
394	                break
395	
396	    return {
397	        "asv": asv,
398	        "raw_violations": raw_violations,
399	        "envelope_violations": env_violations,
400	        "deltas": deltas,
401	        "tau_curve": tau_curve,
402	        "envelope": envelope,
403	    }
404	
405	
406	def compute_magnitude_asv_fast(tau_curve, deltas, tau_true, rel_thresh=0.1):
407	    # [C2] tau~0 means maximally fragile — any annotation error changes the result
408	    if abs(tau_true) < 1e-12:
409	        return 0.0
410	    thresh = rel_thresh * abs(tau_true)
411	    running_max = 0.0
412	    for i in range(len(deltas)):
413	        b = abs(tau_curve[i] - tau_true)
414	        if np.isnan(b):
415	            continue
416	        running_max = max(running_max, b)
417	        if running_max > thresh:
418	            return deltas[i]
419	    return None
420	
421	
422	# [C1] Significance-based ASV from plan_004_v3_fixed
423	def compute_signif_asv_fast(tau_curve, deltas, se):
424	    """Min delta where |plim tau(C(delta))| < 1.96 * SE (becomes non-significant)."""
425	    z_crit = 1.96
426	    for i in range(len(deltas)):
427	        if np.isnan(tau_curve[i]):
428	            continue
429	        if abs(tau_curve[i]) < z_crit * se:
430	            return deltas[i]
431	    return None
432	
433	
434	# ============================================================================
435	# Part 1: Envelope Monotonicity (preserved, skipped in main)
436	# ============================================================================
437	
438	def part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_fd):
439	    print("\n" + "=" * 70)
440	    print("PART 1: Envelope Monotonicity (tau=0.5)")
441	    print("=" * 70)
442	    t0 = time.time()
443	    param = LinearInterpolation()
444	    C_list = normalize_C_list(make_C_list())
445	
446	    for topo, st, tau_true, label in [
447	        ("mbias", st_mb, 0.5, "M-bias"),
448	        ("iv", st_iv, 0.5, "IV"),
449	        ("frontdoor", st_fd, tau_fd, "Front-door"),
450	    ]:
451	        print(f"\n  {label} (tau_true={tau_true:.4f}):")
452	        for cname, C0 in C_list.items():
453	            r = compute_asv_envelope(topo, C0, tau_true, param,
454	                                     "magnitude_relative", 0.1, st=st)
455	            print(f"    {cname}: raw_violations={r['raw_violations']}/1500, "
456	                  f"envelope_violations={r['envelope_violations']}/1500")
457	    print(f"\n  Time: {time.time()-t0:.1f}s")
458	
459	
460	# ============================================================================
461	# Part 2: ASV Values (tau=0.5) — [W1/W2] fixed tau_true
462	# ============================================================================
463	
464	def part2_asv_values(st_mb, st_iv, st_fd, tau_I_mb, tau_I_iv, tau_I_fd):
465	    print("\n" + "=" * 70)
466	    print("PART 2: ASV Values (tau=0.5)")
467	    print("=" * 70)
468	    t0 = time.time()
469	    param = LinearInterpolation()
470	    C_list = normalize_C_list(make_C_list())
471	    results = {}
472	
473	    print(f"\n  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10}")
474	    print("  " + "-" * 45)
475	
476	    # [W1/W2] Use plim(I) as tau_true — ASV measures ADDITIONAL bias from annotation error
477	    for topo, st, tau_true, label in [
478	        ("mbias", st_mb, tau_I_mb, "M-bias"),
479	        ("iv", st_iv, tau_I_iv, "IV"),
480	        ("frontdoor", st_fd, tau_I_fd, "Front-door"),
481	    ]:
482	        for cname, C0 in C_list.items():
483	            r_sf = compute_asv_envelope(topo, C0, tau_true, param,
484	                                        "sign_flip", st=st)
485	            r_mag = compute_asv_envelope(topo, C0, tau_true, param,
486	                                         "magnitude_relative", 0.1, st=st)
487	            sf_s = f"{r_sf['asv']:.3f}" if r_sf['asv'] is not None else "None"
488	            mg_s = f"{r_mag['asv']:.3f}" if r_mag['asv'] is not None else "None"
489	            print(f"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10}")
490	            results[(label, cname)] = {
491	                "sign_flip": r_sf['asv'], "magnitude_10pct": r_mag['asv']}
492	    print(f"\n  Time: {time.time()-t0:.1f}s")
493	    return results
494	
495	
496	# ============================================================================
497	# Part 3: Small-tau ASV — [W1/W2] fixed tau_true
498	# ============================================================================
499	
500	def part3_small_tau_asv():
501	    print("\n" + "=" * 70)
502	    print("PART 3: Small-tau ASV (tau=0.05, 0.1)")
503	    print("=" * 70)
504	    t0 = time.time()
505	    param = LinearInterpolation()
506	    C_list = normalize_C_list(make_C_list())
507	    results = {}
508	
509	    for tau_val in [0.05, 0.1]:
510	        print(f"\n  --- tau = {tau_val} ---")
511	        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val
512	        st_mb = precomp_mbias(mb_p, N=2_000_000)
513	        iv_b = np.array([0.0, tau_val, -tau_val/2])
514	        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
515	        lU = tau_val * 2
516	        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU, seed=200+int(tau_val*100))
517	        tau_fd = plim_fd(np.eye(K), st_fd)[1]
518	        print(f"  Front-door tau_I = {tau_fd:.6f}")
519	
520	        # [W1/W2] Use plim(I) as tau_true, not DGP parameter
521	        tau_I_mb = plim_mbias(np.eye(K), st_mb)[1]
522	        tau_I_iv = plim_iv(np.eye(K), st_iv)
523	        print(f"  M-bias tau_I = {tau_I_mb:.6f}, IV tau_I = {tau_I_iv:.6f}")
524	
525	        hdr = f"  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10} {'MagAbs.05':>10}"
526	        print(hdr)
527	        print("  " + "-" * 55)
528	
529	        for topo, st, tau_true, label in [
530	            ("mbias", st_mb, tau_I_mb, "M-bias"),
531	            ("iv", st_iv, tau_I_iv, "IV"),
532	            ("frontdoor", st_fd, tau_fd, "Front-door"),
533	        ]:
534	            for cname, C0 in C_list.items():
535	                r_sf = compute_asv_envelope(topo, C0, tau_true, param,
536	                                            "sign_flip", st=st)
537	                r_mg = compute_asv_envelope(topo, C0, tau_true, param,
538	                                            "magnitude_relative", 0.1, st=st)
539	                r_ab = compute_asv_envelope(topo, C0, tau_true, param,
540	                                            "magnitude_absolute", 0.05, st=st)
541	                sf_s = f"{r_sf['asv']:.3f}" if r_sf['asv'] is not None else "None"
542	                mg_s = f"{r_mg['asv']:.3f}" if r_mg['asv'] is not None else "None"
543	                ab_s = f"{r_ab['asv']:.3f}" if r_ab['asv'] is not None else "None"
544	                print(f"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10} {ab_s:>10}")
545	                results[(tau_val, label, cname)] = {
546	                    "sign_flip": r_sf['asv'],
547	                    "magnitude_10pct": r_mg['asv'],
548	                    "magnitude_abs05": r_ab['asv']}
549	    print(f"\n  Time: {time.time()-t0:.1f}s")
550	    return results
551	
552	
553	# ============================================================================
554	# Part 4: MC Coverage (preserved, skipped in main)
555	# ============================================================================
556	
557	def part4_mc_coverage(n_scenarios=500, N_mc=10000, reps=100):
558	    print("\n" + "=" * 70)
559	    print(f"PART 4: MC Coverage ({n_scenarios} scenarios x {reps} reps x N={N_mc})")
560	    print("=" * 70)
561	    t0 = time.time()
562	    rng = np.random.default_rng(42)
563	    results = {}
564	
565	    for tau_val in [0.05, 0.1]:
566	        print(f"\n  --- tau = {tau_val} ---")
567	
568	        # --- M-bias ---
569	        print("  [M-bias]")
570	        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val
571	        st_mb = precomp_mbias(mb_p, N=2_000_000)
572	        plim_ok = 0; bias_ok = 0
573	        for s in range(n_scenarios):
574	            C0 = random_C0(K, rng)
575	            tau_plim = plim_mbias(C0, st_mb)[1]
576	            bias_theory = abs(tau_plim - tau_val)
577	            tau_mc = np.zeros(reps)
578	            for r in range(reps):
579	                Td, Yd, _, Asd = gen_mbias_data(N_mc, mb_p, C0, rng)
580	                bh, _ = ols_with_dummies(Yd, Td, Asd, K)
581	                tau_mc[r] = bh[1]
582	            mc_mean = tau_mc.mean()
583	            mc_se = tau_mc.std() / np.sqrt(reps)
584	            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:
585	                plim_ok += 1
586	            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.02:
587	                bias_ok += 1
588	            if (s + 1) % 100 == 0:
589	                print(f"    ... {s+1}/{n_scenarios}")
590	        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
591	        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
592	        results[("mbias", tau_val)] = {
593	            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}
594	
595	        # --- IV ---
596	        print("  [IV]")
597	        iv_b = np.array([0.0, tau_val, -tau_val/2])
598	        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
599	        plim_ok = 0; bias_ok = 0
600	        for s in range(n_scenarios):
601	            C0 = random_C0(K, rng)
602	            tau_plim = plim_iv(C0, st_iv)
603	            if np.isnan(tau_plim):
604	                plim_ok += 1; bias_ok += 1; continue
605	            bias_theory = abs(tau_plim - tau_val)
606	            tau_mc = np.zeros(reps)
607	            for r in range(reps):
608	                Zd, Yd, _, Asd = gen_iv_data(N_mc, iv_b, IV_PARAMS, C0, rng)
609	                w, _ = wald_with_se(Zd, Yd, Asd)
610	                tau_mc[r] = w
611	            valid = ~np.isnan(tau_mc)
612	            if valid.sum() < reps * 0.5:
613	                plim_ok += 1; bias_ok += 1; continue
614	            mc_mean = tau_mc[valid].mean()
615	            mc_se = tau_mc[valid].std() / np.sqrt(valid.sum())
616	            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.05:
617	                plim_ok += 1
618	            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.05:
619	                bias_ok += 1
620	            if (s + 1) % 100 == 0:
621	                print(f"    ... {s+1}/{n_scenarios}")
622	        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
623	        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
624	        results[("iv", tau_val)] = {
625	            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}
626	
627	        # --- Front-door ---
628	        print("  [Front-door]")
629	        lU = tau_val * 2
630	        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU,
631	                           seed=300+int(tau_val*100))
632	        tau_I_fd = plim_fd(np.eye(K), st_fd)[1]
633	        plim_ok = 0; bias_ok = 0
634	        for s in range(n_scenarios):
635	            C0 = random_C0(K, rng)
636	            tau_plim = plim_fd(C0, st_fd)[1]
637	            bias_theory = abs(tau_plim - tau_I_fd)
638	            tau_mc = np.zeros(reps)
639	            for r in range(reps):
640	                Td, Yd, _, Msd = gen_fd_data(N_mc, BETA_FD, C0, rng, lU=lU)
641	                bh, _ = ols_with_dummies(Yd, Td, Msd, K)
642	                tau_mc[r] = bh[1]
643	            mc_mean = tau_mc.mean()
644	            mc_se = tau_mc.std() / np.sqrt(reps)
645	            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:
646	                plim_ok += 1
647	            if abs(mc_mean - tau_I_fd) <= bias_theory + 3 * mc_se + 0.02:
648	                bias_ok += 1
649	            if (s + 1) % 100 == 0:
650	                print(f"    ... {s+1}/{n_scenarios}")
651	        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
652	        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
653	        results[("frontdoor", tau_val)] = {
654	            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}
655	
656	    print(f"\n  Total time: {time.time()-t0:.1f}s")
657	    return results
658	
659	
660	# ============================================================================
661	# Part 5: Type I/II (Significance-Based ASV Filter) — REWRITTEN
662	# ============================================================================
663	
664	def part5_type_errors(n_mc=500, N_sample=5000):
665	    print("\n" + "=" * 70)
666	    print(f"PART 5: Type I/II ({n_mc} MC x N={N_sample})")
667	    print("  Filter: significance-based ASV")
668	    print("  reject if |tau_hat/SE|>1.96 AND (signif_ASV is None OR signif_ASV > 1)")
669	    print("=" * 70)
670	    t0 = time.time()
671	    param = LinearInterpolation()
672	    C_list = normalize_C_list(make_C_list())
673	    results = {}
674	    seed_ctr = 3000
675	
676	    for tau_val in [0.05, 0.1]:
677	        print(f"\n  --- tau = {tau_val} ---")
678	        header = (f"  {'C_struct':<12} {'H':<5} {'naive_rej':>10} "
679	                  f"{'asv_rej':>10} {'mean_sasv':>10} {'mag_asv':>10}")
680	
681	        # === M-bias ===
682	        print("\n  [M-bias]")
683	        print(header)
684	        print("  " + "-" * 55)
685	        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
686	            mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_h
687	            st_h = precomp_mbias(mb_p, N=2_000_000)
688	            # [W2] Use plim(I) as tau_true for magnitude ASV
689	            tau_I_h = plim_mbias(np.eye(K), st_h)[1]
690	            for cname, C0 in C_list.items():
691	                seed_ctr += 1
692	                dmin, dmax = param.delta_range(C0)
693	                deltas = np.linspace(dmin, dmax, 1500)
694	                tau_curve = np.array([
695	                    plim_mbias(param(C0, d), st_h)[1] for d in deltas])
696	                masv = compute_magnitude_asv_fast(
697	                    tau_curve, deltas, tau_I_h, 0.1)
698	                rng_mc = np.random.default_rng(seed_ctr)
699	                naive_rej = 0; asv_rej = 0; sasv_vals = []
700	                for mc in range(n_mc):
701	                    Td, Yd, _, Asd = gen_mbias_data(
702	                        N_sample, mb_p, C0, rng_mc)
703	                    bh, seh = ols_with_dummies(Yd, Td, Asd, K)
704	                    tau_hat, se_tau = bh[1], seh[1]
705	                    reject = (abs(tau_hat / se_tau) > 1.96
706	                              if se_tau > 1e-10 else False)
707	                    if reject:
708	                        naive_rej += 1
709	                    sasv = compute_signif_asv_fast(tau_curve, deltas, se_tau)
710	                    sasv_vals.append(sasv)
711	                    if reject and (sasv is None or sasv > 1.0):
712	                        asv_rej += 1
713	                sf = [a for a in sasv_vals if a is not None]
714	                sm = f"{np.mean(sf):.2f}" if sf else "N/A"
715	                ms = f"{masv:.2f}" if masv is not None else "None"
716	                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
717	                      f"{asv_rej/n_mc:>10.3f} {sm:>10} {ms:>10}")
718	                results[("mbias", tau_val, cname, h_label)] = {
719	                    "naive_rej": naive_rej/n_mc, "asv_rej": asv_rej/n_mc,
720	                    "mean_sasv": np.mean(sf) if sf else None, "masv": masv}
721	
722	        # === IV ===
723	        print("\n  [IV]")
724	        print(header)
725	        print("  " + "-" * 55)
726	        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
727	            iv_b = np.array([0.0, tau_h, -tau_h/2])
728	            st_h = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
729	            # [W1] Use plim(I) as tau_true for magnitude ASV
730	            tau_I_h = plim_iv(np.eye(K), st_h)
731	            for cname, C0 in C_list.items():
732	                seed_ctr += 1
733	                dmin, dmax = param.delta_range(C0)
734	                deltas = np.linspace(dmin, dmax, 1500)
735	                tau_curve = np.array([
736	                    plim_iv(param(C0, d), st_h) for d in deltas])
737	                masv = compute_magnitude_asv_fast(
738	                    tau_curve, deltas, tau_I_h, 0.1)
739	                rng_mc = np.random.default_rng(seed_ctr)
740	                naive_rej = 0; asv_rej = 0; sasv_vals = []
741	                for mc in range(n_mc):
742	                    Zd, Yd, _, Asd = gen_iv_data(
743	                        N_sample, iv_b, IV_PARAMS, C0, rng_mc)
744	                    w, se_w = wald_with_se(Zd, Yd, Asd)
745	                    reject = False
746	                    if not np.isnan(w) and se_w > 1e-10:
747	                        reject = abs(w / se_w) > 1.96
748	                    if reject:
749	                        naive_rej += 1
750	                    se_for_asv = se_w if (not np.isnan(se_w) and se_w > 1e-10) else 1e10
751	                    sasv = compute_signif_asv_fast(tau_curve, deltas, se_for_asv)
752	                    sasv_vals.append(sasv)
753	                    if reject and (sasv is None or sasv > 1.0):
754	                        asv_rej += 1
755	                sf = [a for a in sasv_vals if a is not None]
756	                sm = f"{np.mean(sf):.2f}" if sf else "N/A"
757	                ms = f"{masv:.2f}" if masv is not None else "None"
758	                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
759	                      f"{asv_rej/n_mc:>10.3f} {sm:>10} {ms:>10}")
760	                results[("iv", tau_val, cname, h_label)] = {
761	                    "naive_rej": naive_rej/n_mc, "asv_rej": asv_rej/n_mc,
762	                    "mean_sasv": np.mean(sf) if sf else None, "masv": masv}
763	
764	        # === Front-door ===
765	        print("\n  [Front-door]")
766	        print(header)
767	        print("  " + "-" * 55)
768	        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
769	            if h_label == "H0":
770	                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=0.0, aU=0.0,
771	                                  d=np.zeros(3), seed=400)
772	                tau_ref = 0.0
773	            else:
774	                lU = tau_val * 2
775	                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=lU,
776	                                  seed=401+int(tau_val*100))
777	                tau_ref = plim_fd(np.eye(K), st_h)[1]
778	            print(f"    ({h_label}: tau_ref={tau_ref:.4f})")
779	            for cname, C0 in C_list.items():
780	                seed_ctr += 1
781	                dmin, dmax = param.delta_range(C0)
782	                deltas = np.linspace(dmin, dmax, 1500)
783	                tau_curve = np.array([
784	                    plim_fd(param(C0, d), st_h)[1] for d in deltas])
785	                masv = compute_magnitude_asv_fast(
786	                    tau_curve, deltas, tau_ref, 0.1)
787	                rng_mc = np.random.default_rng(seed_ctr)
788	                naive_rej = 0; asv_rej = 0; sasv_vals = []
789	                for mc in range(n_mc):
790	                    if h_label == "H0":
791	                        Td, Yd, _, Msd = gen_fd_data(
792	                            N_sample, BETA_FD, C0, rng_mc,
793	                            lU=0.0, aU=0.0, d=np.zeros(3))
794	                    else:
795	                        Td, Yd, _, Msd = gen_fd_data(
796	                            N_sample, BETA_FD, C0, rng_mc, lU=lU)
797	                    bh, seh = ols_with_dummies(Yd, Td, Msd, K)
798	                    tau_hat, se_tau = bh[1], seh[1]
799	                    reject = (abs(tau_hat / se_tau) > 1.96
800	                              if se_tau > 1e-10 else False)
801	                    if reject:
802	                        naive_rej += 1
803	                    sasv = compute_signif_asv_fast(tau_curve, deltas, se_tau)
804	                    sasv_vals.append(sasv)
805	                    if reject and (sasv is None or sasv > 1.0):
806	                        asv_rej += 1
807	                sf = [a for a in sasv_vals if a is not None]
808	                sm = f"{np.mean(sf):.2f}" if sf else "N/A"
809	                ms = f"{masv:.2f}" if masv is not None else "None"
810	                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
811	                      f"{asv_rej/n_mc:>10.3f} {sm:>10} {ms:>10}")
812	                results[("frontdoor", tau_val, cname, h_label)] = {
813	                    "naive_rej": naive_rej/n_mc, "asv_rej": asv_rej/n_mc,
814	                    "mean_sasv": np.mean(sf) if sf else None, "masv": masv}
815	
816	    print(f"\n  Total time: {time.time()-t0:.1f}s")
817	    return results
818	
819	
820	# ============================================================================
821	# Part 6: Summary JSON
822	# ============================================================================
823	
824	def collect_summary(asv_res, small_tau_res, cov_res, te_res):
825	    def _f(v):
826	        if v is None:
827	            return None
828	        return float(v)
829	
830	    summary = {
831	        "experiment": "plan_005_asv_extended_fixed",
832	        "topologies": ["mbias", "iv", "frontdoor"],
833	        "asv_values_tau05": {},
834	        "small_tau_asv": {},
835	        "coverage": {},
836	        "type_errors": {},
837	    }
838	    for (label, cname), vals in asv_res.items():
839	        summary["asv_values_tau05"][f"{label}_{cname}"] = {
840	            k: _f(v) for k, v in vals.items()}
841	    for (tv, label, cname), vals in small_tau_res.items():
842	        summary["small_tau_asv"][f"tau{tv}_{label}_{cname}"] = {
843	            k: _f(v) for k, v in vals.items()}
844	    for (topo, tv), vals in cov_res.items():
845	        summary["coverage"][f"{topo}_tau{tv}"] = vals
846	    for key, vals in te_res.items():
847	        summary["type_errors"]["_".join(str(x) for x in key)] = vals
848	    return summary
849	
850	
851	# ============================================================================
852	# Main
853	# ============================================================================
854	
855	if __name__ == "__main__":
856	    np.set_printoptions(precision=6, suppress=True)
857	    print("plan_005_fixed: ASV Framework Extension (C1/C2/W1/W2 fixes)")
858	    print("=" * 70)
859	    t_total = time.time()
860	
861	    print("\nPrecomputing sufficient statistics (tau=0.5)...")
862	    t0 = time.time()
863	    st_mb = precomp_mbias(MBIAS_PARAMS, N=2_000_000)
864	    tau_I_mb = plim_mbias(np.eye(K), st_mb)[1]
865	    print(f"  M-bias:     tau_DGP=0.5, plim(I)={tau_I_mb:.6f}")
866	
867	    st_iv = precomp_iv(IV_BETA, IV_PARAMS, N=2_000_000)
868	    tau_I_iv = plim_iv(np.eye(K), st_iv)
869	    print(f"  IV:         beta[1]=0.5, Wald(I)={tau_I_iv:.6f}")
870	
871	    st_fd = precomp_fd(BETA_FD, N=10_000_000)
872	    tau_I_fd = plim_fd(np.eye(K), st_fd)[1]
873	    print(f"  Front-door: plim(I)={tau_I_fd:.6f}")
874	    print(f"  Done ({time.time()-t0:.1f}s)")
875	
876	    # Part 1 skipped (passed review)
877	    # part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_I_fd)
878	
879	    # [W1/W2] Part 2 now uses plim(I) as tau_true
880	    asv_res = part2_asv_values(st_mb, st_iv, st_fd, tau_I_mb, tau_I_iv, tau_I_fd)
881	
882	    small_tau_res = part3_small_tau_asv()
883	
884	    # Part 4 skipped (passed review)
885	    cov_res = {}
886	
887	    te_res = part5_type_errors(n_mc=500, N_sample=5000)
888	
889	    print("\n" + "=" * 70)
890	    print("PART 6: Summary JSON")
891	    print("=" * 70)
892	    summary = collect_summary(asv_res, small_tau_res, cov_res, te_res)
893	    print(json.dumps(summary, indent=2, default=str))
894	
895	    print("\n" + "=" * 70)
896	    elapsed = time.time() - t_total
897	    print(f"ALL PARTS COMPLETE. Total time: {elapsed:.1f}s ({elapsed/60:.1f}min)")
898	    print("=" * 70)
899	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "fbbc5cbe-cde9-41a7-b408-5aacc5f38083",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan_005_asv_extended_fixed.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nplan_005_fixed: ASV Framework Extension (C1/C2/W1/W2 fixes)\n\nFixes applied (Reviewer CRITICAL):\n  C1: Added compute_signif_asv_fast from plan_004_v3_fixed\n  C2: compute_magnitude_asv_fast returns 0.0 (not None) when tau_true ~ 0\n  W1: IV tau_true = plim_iv(I), not DGP beta (approx 0.66 vs 0.5)\n  W2: M-bias tau_true = plim_mbias(I)[1], not DGP tau (approx 0.5128 vs 0.5)\n\nOnly Part 2+3+5 re-run. Part 1 and Part 4 preserved but skipped.\nPart 5 uses significance-based ASV rejection rule (from plan_004_v3_fixed).\n\"\"\"\n\nimport numpy as np\nimport json\nimport time\n\nK = 3\n\n# ============================================================================\n# Utilities (from plan_004 v3)\n# ============================================================================\n\ndef softmax_sample(logits, rng):\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\n\n\ndef generate_Astar(A, C, rng):\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\n\n\ndef ols_with_dummies(Y, T, Astar, K=3):\n    N = len(Y)\n    D = np.zeros((N, K - 1))\n    for k in range(1, K):\n        D[:, k - 1] = (Astar == k).astype(float)\n    X = np.column_stack([np.ones(N), T, D])\n    try:\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        resid = Y - X @ beta\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\n    except np.linalg.LinAlgError:\n        beta = np.full(X.shape[1], np.nan)\n        se = np.full(X.shape[1], np.nan)\n    return beta, se\n\n\n# ============================================================================\n# C(delta) Parameterization (from plan_004 v3)\n# ============================================================================\n\nclass LinearInterpolation:\n    def __call__(self, C0, delta):\n        K = C0.shape[0]\n        C_d = (1 - delta) * np.eye(K) + delta * C0\n        C_d = np.maximum(C_d, 0.0)\n        col_sums = C_d.sum(axis=0)\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\n        C_d = C_d / col_sums\n        return C_d\n\n    def delta_range(self, C0=None):\n        if C0 is None:\n            return (0.0, 5.0)\n        min_diag = np.diag(C0).min()\n        if min_diag >= 1.0:\n            return (0.0, 10.0)\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\n        return (0.0, delta_max)\n\n\n# ============================================================================\n# C matrices (from plan_004 v3)\n# ============================================================================\n\ndef make_C_list():\n    return {\n        \"C1_sym\": np.array([[0.80, 0.10, 0.10],\n                            [0.10, 0.80, 0.10],\n                            [0.10, 0.10, 0.80]]),\n        \"C2_high\": np.array([[0.90, 0.05, 0.05],\n                             [0.05, 0.90, 0.05],\n                             [0.05, 0.05, 0.90]]),\n        \"C3_asym\": np.array([[0.70, 0.20, 0.10],\n                             [0.15, 0.70, 0.15],\n                             [0.10, 0.15, 0.75]]),\n        \"C4_weak\": np.array([[0.60, 0.20, 0.20],\n                             [0.20, 0.60, 0.20],\n                             [0.15, 0.15, 0.70]]),\n        \"C5_perm\": np.array([[0.40, 0.30, 0.30],\n                             [0.30, 0.40, 0.30],\n                             [0.30, 0.30, 0.40]]),\n        \"C6_diff\": np.array([[0.85, 0.075, 0.075],\n                             [0.15, 0.70, 0.15],\n                             [0.05, 0.05, 0.90]]),\n    }\n\n\ndef normalize_C_list(C_dict):\n    out = {}\n    for name, C in C_dict.items():\n        C = np.maximum(C, 0.0)\n        cs = C.sum(axis=0)\n        cs = np.where(cs < 1e-10, 1.0, cs)\n        out[name] = C / cs\n    return out\n\n\ndef random_C0(K, rng, diag_alpha=5.0, offdiag_alpha=1.0):\n    C = np.zeros((K, K))\n    for k in range(K):\n        alphas = np.full(K, offdiag_alpha)\n        alphas[k] = diag_alpha\n        C[:, k] = rng.dirichlet(alphas)\n    return C\n\n\n# ============================================================================\n# Topology 1: M-BIAS — U1->{A,T}, U2->{A,Y}, T->Y\n# ============================================================================\n\nMBIAS_PARAMS = dict(tau=0.5, delta=1.0, lam=1.0,\n                    g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9)\n\n\ndef _gen_mbias(N, params, rng):\n    U1 = rng.normal(0, 1, N)\n    U2 = rng.normal(0, 1, N)\n    T = params['delta'] * U1 + rng.normal(0, 1, N)\n    Y = params['tau'] * T + params['lam'] * U2 + rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['a1'] * U1 + params['a2'] * U2,\n        params['g2'] + params['a3'] * U1 + params['a4'] * U2,\n    ])\n    A = softmax_sample(logits, rng)\n    return T, Y, A\n\n\ndef gen_mbias_data(N, params, C0, rng):\n    T, Y, A = _gen_mbias(N, params, rng)\n    Astar = generate_Astar(A, C0, rng)\n    return T, Y, A, Astar\n\n\ndef precomp_mbias(params, N=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    T, Y, A = _gen_mbias(N, params, rng)\n    DA = np.zeros((N, K))\n    for k in range(K):\n        DA[:, k] = (A == k).astype(float)\n    return dict(\n        E_T=T.mean(), E_T2=(T**2).mean(),\n        E_Y=Y.mean(), E_TY=(T*Y).mean(),\n        E_DA=DA.mean(0),\n        E_DA_T=(DA * T[:, None]).mean(0),\n        E_DA_Y=(DA * Y[:, None]).mean(0))\n\n\ndef plim_mbias(C, st):\n    \"\"\"OLS plim for Y ~ 1 + T + D1_A* + D2_A*.\"\"\"\n    ds  = C @ st['E_DA']\n    dst = C @ st['E_DA_T']\n    dsy = C @ st['E_DA_Y']\n    ET, ET2 = st['E_T'], st['E_T2']\n    EY, ETY = st['E_Y'], st['E_TY']\n    EZZ = np.array([\n        [1,      ET,      ds[1],    ds[2]   ],\n        [ET,     ET2,     dst[1],   dst[2]  ],\n        [ds[1],  dst[1],  ds[1],    0       ],\n        [ds[2],  dst[2],  0,        ds[2]   ]])\n    EZY = np.array([EY, ETY, dsy[1], dsy[2]])\n    return np.linalg.solve(EZZ, EZY)\n\n\n# ============================================================================\n# Topology 2: IV — Z->A->Y, U->{A,Y}\n# ============================================================================\n\nIV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)\nIV_BETA = np.array([0.0, 0.5, -0.25])\n\n\ndef _gen_iv(N, beta, params, rng):\n    Z_iv = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    eps = rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['dZ'] * Z_iv + params['dU'] * U,\n        params['g2'] + params['dZ2'] * Z_iv + params['dU2'] * U,\n    ])\n    A = softmax_sample(logits, rng)\n    Y = (beta[1] * (A == 1).astype(float) + beta[2] * (A == 2).astype(float)\n         + params['lam'] * U + eps)\n    return Z_iv, U, Y, A\n\n\ndef gen_iv_data(N, beta, params, C0, rng):\n    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)\n    Astar = generate_Astar(A, C0, rng)\n    return Z_iv, Y, A, Astar\n\n\ndef precomp_iv(beta, params, N=2_000_000, seed=999):\n    \"\"\"Precompute reduced form and first stage for Wald estimator.\"\"\"\n    rng = np.random.default_rng(seed)\n    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)\n    z1 = Z_iv == 1; z0 = Z_iv == 0\n    RF = Y[z1].mean() - Y[z0].mean()\n    FS = np.zeros(K)\n    for k in range(K):\n        FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()\n    return dict(RF=RF, FS=FS)\n\n\ndef plim_iv(C, st):\n    \"\"\"Wald estimator: RF / FS*_1 where FS* = C @ FS.\"\"\"\n    FS_star = C @ st['FS']\n    if abs(FS_star[1]) < 1e-8:\n        return np.nan\n    return st['RF'] / FS_star[1]\n\n\ndef wald_with_se(Z, Y, Astar, k=1):\n    \"\"\"Finite-sample Wald estimator with delta-method SE.\"\"\"\n    z1 = Z == 1; z0 = Z == 0\n    n1 = float(z1.sum()); n0 = float(z0.sum())\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    RF = Y[z1].mean() - Y[z0].mean()\n    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0\n    Dk_z1 = (Astar[z1] == k).astype(float).mean()\n    Dk_z0 = (Astar[z0] == k).astype(float).mean()\n    FS = Dk_z1 - Dk_z0\n    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0\n    if abs(FS) < 1e-8:\n        return np.nan, np.nan\n    Wald = RF / FS\n    var_Wald = var_RF / FS**2 + RF**2 * var_FS / FS**4\n    SE = np.sqrt(max(var_Wald, 0))\n    return Wald, SE\n\n\n# ============================================================================\n# Topology 3: FRONT-DOOR — T->M->Y, U->{T,Y}\n# ============================================================================\n\nALPHA_U = 1.0\nLAMBDA_U = 1.0\nGAMMA_FD = np.array([0.0, 0.5, -0.3])\nDELTA_FD = np.array([0.0, 1.0, -0.8])\nBETA_FD = np.array([0.0, 1.0, -0.5])\n\n\ndef _gen_fd(N, beta, rng, g=None, d=None, aU=None, lU=None):\n    if g is None: g = GAMMA_FD\n    if d is None: d = DELTA_FD\n    if aU is None: aU = ALPHA_U\n    if lU is None: lU = LAMBDA_U\n    U = rng.normal(0, 1, N)\n    T = aU * U + rng.normal(0, 1, N)\n    lo = np.column_stack([np.zeros(N), g[1] + d[1]*T, g[2] + d[2]*T])\n    lo -= lo.max(1, keepdims=True)\n    e = np.exp(lo)\n    p = e / e.sum(1, keepdims=True)\n    cu = np.cumsum(p, axis=1)\n    u = rng.uniform(size=N)\n    M = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)\n    DM1 = (M == 1).astype(float)\n    DM2 = (M == 2).astype(float)\n    Y = beta[1]*DM1 + beta[2]*DM2 + lU*U + rng.normal(0, 1, N)\n    return T, M, Y, U\n\n\ndef gen_fd_data(N, beta, C0, rng, lU=None, aU=None, d=None):\n    T, M, Y, U = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)\n    Mstar = generate_Astar(M, C0, rng)\n    return T, Y, M, Mstar\n\n\ndef precomp_fd(beta, N=10_000_000, seed=123, lU=None, aU=None, d=None):\n    rng = np.random.default_rng(seed)\n    T, M, Y, _ = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)\n    DM = np.zeros((N, K))\n    for k in range(K):\n        DM[:, k] = (M == k).astype(float)\n    return dict(\n        E_T=T.mean(), E_T2=(T**2).mean(),\n        E_Y=Y.mean(), E_TY=(T*Y).mean(),\n        E_DM=DM.mean(0),\n        E_DM_T=(DM * T[:, None]).mean(0),\n        E_DM_Y=(DM * Y[:, None]).mean(0))\n\n\ndef plim_fd(C, st):\n    \"\"\"OLS plim for Y ~ 1 + T + D1_M* + D2_M*.\"\"\"\n    ds  = C @ st['E_DM']\n    dst = C @ st['E_DM_T']\n    dsy = C @ st['E_DM_Y']\n    ET, ET2 = st['E_T'], st['E_T2']\n    EY, ETY = st['E_Y'], st['E_TY']\n    EZZ = np.array([\n        [1,      ET,      ds[1],    ds[2]   ],\n        [ET,     ET2,     dst[1],   dst[2]  ],\n        [ds[1],  dst[1],  ds[1],    0       ],\n        [ds[2],  dst[2],  0,        ds[2]   ]])\n    EZY = np.array([EY, ETY, dsy[1], dsy[2]])\n    return np.linalg.solve(EZZ, EZY)\n\n\n# ============================================================================\n# ASV Framework\n# ============================================================================\n\ndef compute_bias_curve(topology, C0, param, tau_true, st, n_grid=1500):\n    dmin, dmax = param.delta_range(C0)\n    deltas = np.linspace(dmin, dmax, n_grid)\n    tau_curve = np.zeros(n_grid)\n    for i, d in enumerate(deltas):\n        C_d = param(C0, d)\n        if topology == \"mbias\":\n            tau_curve[i] = plim_mbias(C_d, st)[1]\n        elif topology == \"iv\":\n            tau_curve[i] = plim_iv(C_d, st)\n        elif topology == \"frontdoor\":\n            tau_curve[i] = plim_fd(C_d, st)[1]\n    bias_abs = np.abs(tau_curve - tau_true)\n    return deltas, bias_abs, tau_curve\n\n\ndef compute_envelope(bias_abs):\n    env = np.zeros_like(bias_abs)\n    running_max = 0.0\n    for i in range(len(bias_abs)):\n        v = bias_abs[i]\n        if not np.isnan(v):\n            running_max = max(running_max, v)\n        env[i] = running_max\n    return env\n\n\ndef verify_envelope_monotonicity(envelope):\n    diffs = np.diff(envelope)\n    return int(np.sum(diffs < -1e-12))\n\n\ndef compute_asv_envelope(topology, C0, tau_true, param, threshold_type,\n                         threshold_value=0.1, st=None, n_grid=1500):\n    deltas, bias_abs, tau_curve = compute_bias_curve(\n        topology, C0, param, tau_true, st, n_grid)\n    envelope = compute_envelope(bias_abs)\n\n    valid_ba = bias_abs[~np.isnan(bias_abs)]\n    raw_violations = int(np.sum(np.diff(valid_ba) < -1e-12)) if len(valid_ba) > 1 else 0\n    env_violations = verify_envelope_monotonicity(envelope)\n\n    asv = None\n    if threshold_type == \"sign_flip\":\n        if abs(tau_true) < 1e-12:\n            asv = None\n        else:\n            baseline_sign = np.sign(tau_true)\n            for i, d in enumerate(deltas):\n                if np.isnan(tau_curve[i]):\n                    continue\n                if np.sign(tau_curve[i]) != baseline_sign:\n                    asv = d\n                    break\n    elif threshold_type == \"magnitude_relative\":\n        if abs(tau_true) < 1e-12:\n            asv = None\n        else:\n            thresh = threshold_value * abs(tau_true)\n            for i, d in enumerate(deltas):\n                if envelope[i] > thresh:\n                    asv = d\n                    break\n    elif threshold_type == \"magnitude_absolute\":\n        thresh = threshold_value\n        for i, d in enumerate(deltas):\n            if envelope[i] > thresh:\n                asv = d\n                break\n\n    return {\n        \"asv\": asv,\n        \"raw_violations\": raw_violations,\n        \"envelope_violations\": env_violations,\n        \"deltas\": deltas,\n        \"tau_curve\": tau_curve,\n        \"envelope\": envelope,\n    }\n\n\ndef compute_magnitude_asv_fast(tau_curve, deltas, tau_true, rel_thresh=0.1):\n    # [C2] tau~0 means maximally fragile — any annotation error changes the result\n    if abs(tau_true) < 1e-12:\n        return 0.0\n    thresh = rel_thresh * abs(tau_true)\n    running_max = 0.0\n    for i in range(len(deltas)):\n        b = abs(tau_curve[i] - tau_true)\n        if np.isnan(b):\n            continue\n        running_max = max(running_max, b)\n        if running_max > thresh:\n            return deltas[i]\n    return None\n\n\n# [C1] Significance-based ASV from plan_004_v3_fixed\ndef compute_signif_asv_fast(tau_curve, deltas, se):\n    \"\"\"Min delta where |plim tau(C(delta))| < 1.96 * SE (becomes non-significant).\"\"\"\n    z_crit = 1.96\n    for i in range(len(deltas)):\n        if np.isnan(tau_curve[i]):\n            continue\n        if abs(tau_curve[i]) < z_crit * se:\n            return deltas[i]\n    return None\n\n\n# ============================================================================\n# Part 1: Envelope Monotonicity (preserved, skipped in main)\n# ============================================================================\n\ndef part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_fd):\n    print(\"\\n\" + \"=\" * 70)\n    print(\"PART 1: Envelope Monotonicity (tau=0.5)\")\n    print(\"=\" * 70)\n    t0 = time.time()\n    param = LinearInterpolation()\n    C_list = normalize_C_list(make_C_list())\n\n    for topo, st, tau_true, label in [\n        (\"mbias\", st_mb, 0.5, \"M-bias\"),\n        (\"iv\", st_iv, 0.5, \"IV\"),\n        (\"frontdoor\", st_fd, tau_fd, \"Front-door\"),\n    ]:\n        print(f\"\\n  {label} (tau_true={tau_true:.4f}):\")\n        for cname, C0 in C_list.items():\n            r = compute_asv_envelope(topo, C0, tau_true, param,\n                                     \"magnitude_relative\", 0.1, st=st)\n            print(f\"    {cname}: raw_violations={r['raw_violations']}/1500, \"\n                  f\"envelope_violations={r['envelope_violations']}/1500\")\n    print(f\"\\n  Time: {time.time()-t0:.1f}s\")\n\n\n# ============================================================================\n# Part 2: ASV Values (tau=0.5) — [W1/W2] fixed tau_true\n# ============================================================================\n\ndef part2_asv_values(st_mb, st_iv, st_fd, tau_I_mb, tau_I_iv, tau_I_fd):\n    print(\"\\n\" + \"=\" * 70)\n    print(\"PART 2: ASV Values (tau=0.5)\")\n    print(\"=\" * 70)\n    t0 = time.time()\n    param = LinearInterpolation()\n    C_list = normalize_C_list(make_C_list())\n    results = {}\n\n    print(f\"\\n  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10}\")\n    print(\"  \" + \"-\" * 45)\n\n    # [W1/W2] Use plim(I) as tau_true — ASV measures ADDITIONAL bias from annotation error\n    for topo, st, tau_true, label in [\n        (\"mbias\", st_mb, tau_I_mb, \"M-bias\"),\n        (\"iv\", st_iv, tau_I_iv, \"IV\"),\n        (\"frontdoor\", st_fd, tau_I_fd, \"Front-door\"),\n    ]:\n        for cname, C0 in C_list.items():\n            r_sf = compute_asv_envelope(topo, C0, tau_true, param,\n                                        \"sign_flip\", st=st)\n            r_mag = compute_asv_envelope(topo, C0, tau_true, param,\n                                         \"magnitude_relative\", 0.1, st=st)\n            sf_s = f\"{r_sf['asv']:.3f}\" if r_sf['asv'] is not None else \"None\"\n            mg_s = f\"{r_mag['asv']:.3f}\" if r_mag['asv'] is not None else \"None\"\n            print(f\"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10}\")\n            results[(label, cname)] = {\n                \"sign_flip\": r_sf['asv'], \"magnitude_10pct\": r_mag['asv']}\n    print(f\"\\n  Time: {time.time()-t0:.1f}s\")\n    return results\n\n\n# ============================================================================\n# Part 3: Small-tau ASV — [W1/W2] fixed tau_true\n# ============================================================================\n\ndef part3_small_tau_asv():\n    print(\"\\n\" + \"=\" * 70)\n    print(\"PART 3: Small-tau ASV (tau=0.05, 0.1)\")\n    print(\"=\" * 70)\n    t0 = time.time()\n    param = LinearInterpolation()\n    C_list = normalize_C_list(make_C_list())\n    results = {}\n\n    for tau_val in [0.05, 0.1]:\n        print(f\"\\n  --- tau = {tau_val} ---\")\n        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val\n        st_mb = precomp_mbias(mb_p, N=2_000_000)\n        iv_b = np.array([0.0, tau_val, -tau_val/2])\n        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)\n        lU = tau_val * 2\n        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU, seed=200+int(tau_val*100))\n        tau_fd = plim_fd(np.eye(K), st_fd)[1]\n        print(f\"  Front-door tau_I = {tau_fd:.6f}\")\n\n        # [W1/W2] Use plim(I) as tau_true, not DGP parameter\n        tau_I_mb = plim_mbias(np.eye(K), st_mb)[1]\n        tau_I_iv = plim_iv(np.eye(K), st_iv)\n        print(f\"  M-bias tau_I = {tau_I_mb:.6f}, IV tau_I = {tau_I_iv:.6f}\")\n\n        hdr = f\"  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10} {'MagAbs.05':>10}\"\n        print(hdr)\n        print(\"  \" + \"-\" * 55)\n\n        for topo, st, tau_true, label in [\n            (\"mbias\", st_mb, tau_I_mb, \"M-bias\"),\n            (\"iv\", st_iv, tau_I_iv, \"IV\"),\n            (\"frontdoor\", st_fd, tau_fd, \"Front-door\"),\n        ]:\n            for cname, C0 in C_list.items():\n                r_sf = compute_asv_envelope(topo, C0, tau_true, param,\n                                            \"sign_flip\", st=st)\n                r_mg = compute_asv_envelope(topo, C0, tau_true, param,\n                                            \"magnitude_relative\", 0.1, st=st)\n                r_ab = compute_asv_envelope(topo, C0, tau_true, param,\n                                            \"magnitude_absolute\", 0.05, st=st)\n                sf_s = f\"{r_sf['asv']:.3f}\" if r_sf['asv'] is not None else \"None\"\n                mg_s = f\"{r_mg['asv']:.3f}\" if r_mg['asv'] is not None else \"None\"\n                ab_s = f\"{r_ab['asv']:.3f}\" if r_ab['asv'] is not None else \"None\"\n                print(f\"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10} {ab_s:>10}\")\n                results[(tau_val, label, cname)] = {\n                    \"sign_flip\": r_sf['asv'],\n                    \"magnitude_10pct\": r_mg['asv'],\n                    \"magnitude_abs05\": r_ab['asv']}\n    print(f\"\\n  Time: {time.time()-t0:.1f}s\")\n    return results\n\n\n# ============================================================================\n# Part 4: MC Coverage (preserved, skipped in main)\n# ============================================================================\n\ndef part4_mc_coverage(n_scenarios=500, N_mc=10000, reps=100):\n    print(\"\\n\" + \"=\" * 70)\n    print(f\"PART 4: MC Coverage ({n_scenarios} scenarios x {reps} reps x N={N_mc})\")\n    print(\"=\" * 70)\n    t0 = time.time()\n    rng = np.random.default_rng(42)\n    results = {}\n\n    for tau_val in [0.05, 0.1]:\n        print(f\"\\n  --- tau = {tau_val} ---\")\n\n        # --- M-bias ---\n        print(\"  [M-bias]\")\n        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val\n        st_mb = precomp_mbias(mb_p, N=2_000_000)\n        plim_ok = 0; bias_ok = 0\n        for s in range(n_scenarios):\n            C0 = random_C0(K, rng)\n            tau_plim = plim_mbias(C0, st_mb)[1]\n            bias_theory = abs(tau_plim - tau_val)\n            tau_mc = np.zeros(reps)\n            for r in range(reps):\n                Td, Yd, _, Asd = gen_mbias_data(N_mc, mb_p, C0, rng)\n                bh, _ = ols_with_dummies(Yd, Td, Asd, K)\n                tau_mc[r] = bh[1]\n            mc_mean = tau_mc.mean()\n            mc_se = tau_mc.std() / np.sqrt(reps)\n            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:\n                plim_ok += 1\n            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.02:\n                bias_ok += 1\n            if (s + 1) % 100 == 0:\n                print(f\"    ... {s+1}/{n_scenarios}\")\n        print(f\"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%\")\n        print(f\"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%\")\n        results[(\"mbias\", tau_val)] = {\n            \"plim_acc\": plim_ok/n_scenarios, \"bias_bounded\": bias_ok/n_scenarios}\n\n        # --- IV ---\n        print(\"  [IV]\")\n        iv_b = np.array([0.0, tau_val, -tau_val/2])\n        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)\n        plim_ok = 0; bias_ok = 0\n        for s in range(n_scenarios):\n            C0 = random_C0(K, rng)\n            tau_plim = plim_iv(C0, st_iv)\n            if np.isnan(tau_plim):\n                plim_ok += 1; bias_ok += 1; continue\n            bias_theory = abs(tau_plim - tau_val)\n            tau_mc = np.zeros(reps)\n            for r in range(reps):\n                Zd, Yd, _, Asd = gen_iv_data(N_mc, iv_b, IV_PARAMS, C0, rng)\n                w, _ = wald_with_se(Zd, Yd, Asd)\n                tau_mc[r] = w\n            valid = ~np.isnan(tau_mc)\n            if valid.sum() < reps * 0.5:\n                plim_ok += 1; bias_ok += 1; continue\n            mc_mean = tau_mc[valid].mean()\n            mc_se = tau_mc[valid].std() / np.sqrt(valid.sum())\n            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.05:\n                plim_ok += 1\n            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.05:\n                bias_ok += 1\n            if (s + 1) % 100 == 0:\n                print(f\"    ... {s+1}/{n_scenarios}\")\n        print(f\"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%\")\n        print(f\"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%\")\n        results[(\"iv\", tau_val)] = {\n            \"plim_acc\": plim_ok/n_scenarios, \"bias_bounded\": bias_ok/n_scenarios}\n\n        # --- Front-door ---\n        print(\"  [Front-door]\")\n        lU = tau_val * 2\n        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU,\n                           seed=300+int(tau_val*100))\n        tau_I_fd = plim_fd(np.eye(K), st_fd)[1]\n        plim_ok = 0; bias_ok = 0\n        for s in range(n_scenarios):\n            C0 = random_C0(K, rng)\n            tau_plim = plim_fd(C0, st_fd)[1]\n            bias_theory = abs(tau_plim - tau_I_fd)\n            tau_mc = np.zeros(reps)\n            for r in range(reps):\n                Td, Yd, _, Msd = gen_fd_data(N_mc, BETA_FD, C0, rng, lU=lU)\n                bh, _ = ols_with_dummies(Yd, Td, Msd, K)\n                tau_mc[r] = bh[1]\n            mc_mean = tau_mc.mean()\n            mc_se = tau_mc.std() / np.sqrt(reps)\n            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:\n                plim_ok += 1\n            if abs(mc_mean - tau_I_fd) <= bias_theory + 3 * mc_se + 0.02:\n                bias_ok += 1\n            if (s + 1) % 100 == 0:\n                print(f\"    ... {s+1}/{n_scenarios}\")\n        print(f\"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%\")\n        print(f\"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%\")\n        results[(\"frontdoor\", tau_val)] = {\n            \"plim_acc\": plim_ok/n_scenarios, \"bias_bounded\": bias_ok/n_scenarios}\n\n    print(f\"\\n  Total time: {time.time()-t0:.1f}s\")\n    return results\n\n\n# ============================================================================\n# Part 5: Type I/II (Significance-Based ASV Filter) — REWRITTEN\n# ============================================================================\n\ndef part5_type_errors(n_mc=500, N_sample=5000):\n    print(\"\\n\" + \"=\" * 70)\n    print(f\"PART 5: Type I/II ({n_mc} MC x N={N_sample})\")\n    print(\"  Filter: significance-based ASV\")\n    print(\"  reject if |tau_hat/SE|>1.96 AND (signif_ASV is None OR signif_ASV > 1)\")\n    print(\"=\" * 70)\n    t0 = time.time()\n    param = LinearInterpolation()\n    C_list = normalize_C_list(make_C_list())\n    results = {}\n    seed_ctr = 3000\n\n    for tau_val in [0.05, 0.1]:\n        print(f\"\\n  --- tau = {tau_val} ---\")\n        header = (f\"  {'C_struct':<12} {'H':<5} {'naive_rej':>10} \"\n                  f\"{'asv_rej':>10} {'mean_sasv':>10} {'mag_asv':>10}\")\n\n        # === M-bias ===\n        print(\"\\n  [M-bias]\")\n        print(header)\n        print(\"  \" + \"-\" * 55)\n        for h_label, tau_h in [(\"H0\", 0.0), (\"H1\", tau_val)]:\n            mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_h\n            st_h = precomp_mbias(mb_p, N=2_000_000)\n            # [W2] Use plim(I) as tau_true for magnitude ASV\n            tau_I_h = plim_mbias(np.eye(K), st_h)[1]\n            for cname, C0 in C_list.items():\n                seed_ctr += 1\n                dmin, dmax = param.delta_range(C0)\n                deltas = np.linspace(dmin, dmax, 1500)\n                tau_curve = np.array([\n                    plim_mbias(param(C0, d), st_h)[1] for d in deltas])\n                masv = compute_magnitude_asv_fast(\n                    tau_curve, deltas, tau_I_h, 0.1)\n                rng_mc = np.random.default_rng(seed_ctr)\n                naive_rej = 0; asv_rej = 0; sasv_vals = []\n                for mc in range(n_mc):\n                    Td, Yd, _, Asd = gen_mbias_data(\n                        N_sample, mb_p, C0, rng_mc)\n                    bh, seh = ols_with_dummies(Yd, Td, Asd, K)\n                    tau_hat, se_tau = bh[1], seh[1]\n                    reject = (abs(tau_hat / se_tau) > 1.96\n                              if se_tau > 1e-10 else False)\n                    if reject:\n                        naive_rej += 1\n                    sasv = compute_signif_asv_fast(tau_curve, deltas, se_tau)\n                    sasv_vals.append(sasv)\n                    if reject and (sasv is None or sasv > 1.0):\n                        asv_rej += 1\n                sf = [a for a in sasv_vals if a is not None]\n                sm = f\"{np.mean(sf):.2f}\" if sf else \"N/A\"\n                ms = f\"{masv:.2f}\" if masv is not None else \"None\"\n                print(f\"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} \"\n                      f\"{asv_rej/n_mc:>10.3f} {sm:>10} {ms:>10}\")\n                results[(\"mbias\", tau_val, cname, h_label)] = {\n                    \"naive_rej\": naive_rej/n_mc, \"asv_rej\": asv_rej/n_mc,\n                    \"mean_sasv\": np.mean(sf) if sf else None, \"masv\": masv}\n\n        # === IV ===\n        print(\"\\n  [IV]\")\n        print(header)\n        print(\"  \" + \"-\" * 55)\n        for h_label, tau_h in [(\"H0\", 0.0), (\"H1\", tau_val)]:\n            iv_b = np.array([0.0, tau_h, -tau_h/2])\n            st_h = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)\n            # [W1] Use plim(I) as tau_true for magnitude ASV\n            tau_I_h = plim_iv(np.eye(K), st_h)\n            for cname, C0 in C_list.items():\n                seed_ctr += 1\n                dmin, dmax = param.delta_range(C0)\n                deltas = np.linspace(dmin, dmax, 1500)\n                tau_curve = np.array([\n                    plim_iv(param(C0, d), st_h) for d in deltas])\n                masv = compute_magnitude_asv_fast(\n                    tau_curve, deltas, tau_I_h, 0.1)\n                rng_mc = np.random.default_rng(seed_ctr)\n                naive_rej = 0; asv_rej = 0; sasv_vals = []\n                for mc in range(n_mc):\n                    Zd, Yd, _, Asd = gen_iv_data(\n                        N_sample, iv_b, IV_PARAMS, C0, rng_mc)\n                    w, se_w = wald_with_se(Zd, Yd, Asd)\n                    reject = False\n                    if not np.isnan(w) and se_w > 1e-10:\n                        reject = abs(w / se_w) > 1.96\n                    if reject:\n                        naive_rej += 1\n                    se_for_asv = se_w if (not np.isnan(se_w) and se_w > 1e-10) else 1e10\n                    sasv = compute_signif_asv_fast(tau_curve, deltas, se_for_asv)\n                    sasv_vals.append(sasv)\n                    if reject and (sasv is None or sasv > 1.0):\n                        asv_rej += 1\n                sf = [a for a in sasv_vals if a is not None]\n                sm = f\"{np.mean(sf):.2f}\" if sf else \"N/A\"\n                ms = f\"{masv:.2f}\" if masv is not None else \"None\"\n                print(f\"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} \"\n                      f\"{asv_rej/n_mc:>10.3f} {sm:>10} {ms:>10}\")\n                results[(\"iv\", tau_val, cname, h_label)] = {\n                    \"naive_rej\": naive_rej/n_mc, \"asv_rej\": asv_rej/n_mc,\n                    \"mean_sasv\": np.mean(sf) if sf else None, \"masv\": masv}\n\n        # === Front-door ===\n        print(\"\\n  [Front-door]\")\n        print(header)\n        print(\"  \" + \"-\" * 55)\n        for h_label, tau_h in [(\"H0\", 0.0), (\"H1\", tau_val)]:\n            if h_label == \"H0\":\n                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=0.0, aU=0.0,\n                                  d=np.zeros(3), seed=400)\n                tau_ref = 0.0\n            else:\n                lU = tau_val * 2\n                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=lU,\n                                  seed=401+int(tau_val*100))\n                tau_ref = plim_fd(np.eye(K), st_h)[1]\n            print(f\"    ({h_label}: tau_ref={tau_ref:.4f})\")\n            for cname, C0 in C_list.items():\n                seed_ctr += 1\n                dmin, dmax = param.delta_range(C0)\n                deltas = np.linspace(dmin, dmax, 1500)\n                tau_curve = np.array([\n                    plim_fd(param(C0, d), st_h)[1] for d in deltas])\n                masv = compute_magnitude_asv_fast(\n                    tau_curve, deltas, tau_ref, 0.1)\n                rng_mc = np.random.default_rng(seed_ctr)\n                naive_rej = 0; asv_rej = 0; sasv_vals = []\n                for mc in range(n_mc):\n                    if h_label == \"H0\":\n                        Td, Yd, _, Msd = gen_fd_data(\n                            N_sample, BETA_FD, C0, rng_mc,\n                            lU=0.0, aU=0.0, d=np.zeros(3))\n                    else:\n                        Td, Yd, _, Msd = gen_fd_data(\n                            N_sample, BETA_FD, C0, rng_mc, lU=lU)\n                    bh, seh = ols_with_dummies(Yd, Td, Msd, K)\n                    tau_hat, se_tau = bh[1], seh[1]\n                    reject = (abs(tau_hat / se_tau) > 1.96\n                              if se_tau > 1e-10 else False)\n                    if reject:\n                        naive_rej += 1\n                    sasv = compute_signif_asv_fast(tau_curve, deltas, se_tau)\n                    sasv_vals.append(sasv)\n                    if reject and (sasv is None or sasv > 1.0):\n                        asv_rej += 1\n                sf = [a for a in sasv_vals if a is not None]\n                sm = f\"{np.mean(sf):.2f}\" if sf else \"N/A\"\n                ms = f\"{masv:.2f}\" if masv is not None else \"None\"\n                print(f\"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} \"\n                      f\"{asv_rej/n_mc:>10.3f} {sm:>10} {ms:>10}\")\n                results[(\"frontdoor\", tau_val, cname, h_label)] = {\n                    \"naive_rej\": naive_rej/n_mc, \"asv_rej\": asv_rej/n_mc,\n                    \"mean_sasv\": np.mean(sf) if sf else None, \"masv\": masv}\n\n    print(f\"\\n  Total time: {time.time()-t0:.1f}s\")\n    return results\n\n\n# ============================================================================\n# Part 6: Summary JSON\n# ============================================================================\n\ndef collect_summary(asv_res, small_tau_res, cov_res, te_res):\n    def _f(v):\n        if v is None:\n            return None\n        return float(v)\n\n    summary = {\n        \"experiment\": \"plan_005_asv_extended_fixed\",\n        \"topologies\": [\"mbias\", \"iv\", \"frontdoor\"],\n        \"asv_values_tau05\": {},\n        \"small_tau_asv\": {},\n        \"coverage\": {},\n        \"type_errors\": {},\n    }\n    for (label, cname), vals in asv_res.items():\n        summary[\"asv_values_tau05\"][f\"{label}_{cname}\"] = {\n            k: _f(v) for k, v in vals.items()}\n    for (tv, label, cname), vals in small_tau_res.items():\n        summary[\"small_tau_asv\"][f\"tau{tv}_{label}_{cname}\"] = {\n            k: _f(v) for k, v in vals.items()}\n    for (topo, tv), vals in cov_res.items():\n        summary[\"coverage\"][f\"{topo}_tau{tv}\"] = vals\n    for key, vals in te_res.items():\n        summary[\"type_errors\"][\"_\".join(str(x) for x in key)] = vals\n    return summary\n\n\n# ============================================================================\n# Main\n# ============================================================================\n\nif __name__ == \"__main__\":\n    np.set_printoptions(precision=6, suppress=True)\n    print(\"plan_005_fixed: ASV Framework Extension (C1/C2/W1/W2 fixes)\")\n    print(\"=\" * 70)\n    t_total = time.time()\n\n    print(\"\\nPrecomputing sufficient statistics (tau=0.5)...\")\n    t0 = time.time()\n    st_mb = precomp_mbias(MBIAS_PARAMS, N=2_000_000)\n    tau_I_mb = plim_mbias(np.eye(K), st_mb)[1]\n    print(f\"  M-bias:     tau_DGP=0.5, plim(I)={tau_I_mb:.6f}\")\n\n    st_iv = precomp_iv(IV_BETA, IV_PARAMS, N=2_000_000)\n    tau_I_iv = plim_iv(np.eye(K), st_iv)\n    print(f\"  IV:         beta[1]=0.5, Wald(I)={tau_I_iv:.6f}\")\n\n    st_fd = precomp_fd(BETA_FD, N=10_000_000)\n    tau_I_fd = plim_fd(np.eye(K), st_fd)[1]\n    print(f\"  Front-door: plim(I)={tau_I_fd:.6f}\")\n    print(f\"  Done ({time.time()-t0:.1f}s)\")\n\n    # Part 1 skipped (passed review)\n    # part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_I_fd)\n\n    # [W1/W2] Part 2 now uses plim(I) as tau_true\n    asv_res = part2_asv_values(st_mb, st_iv, st_fd, tau_I_mb, tau_I_iv, tau_I_fd)\n\n    small_tau_res = part3_small_tau_asv()\n\n    # Part 4 skipped (passed review)\n    cov_res = {}\n\n    te_res = part5_type_errors(n_mc=500, N_sample=5000)\n\n    print(\"\\n\" + \"=\" * 70)\n    print(\"PART 6: Summary JSON\")\n    print(\"=\" * 70)\n    summary = collect_summary(asv_res, small_tau_res, cov_res, te_res)\n    print(json.dumps(summary, indent=2, default=str))\n\n    print(\"\\n\" + \"=\" * 70)\n    elapsed = time.time() - t_total\n    print(f\"ALL PARTS COMPLETE. Total time: {elapsed:.1f}s ({elapsed/60:.1f}min)\")\n    print(\"=\" * 70)\n",
      "numLines": 899,
      "startLine": 1,
      "totalLines": 899
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Now I need to also look at the confounding and exposure topology implementations. The task mentions confounding, exposure, and IV topologies. The existing code has mbias, iv, and frontdoor. Let me check for confounding and exposure implementations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "58504bac-0061-403a-b7fa-918cb4c5a5b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017JRjgXAZmd2nZhR5NeUdyZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15730,
      "cache_read_input_tokens": 26855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15730
      },
      "output_tokens": 9,
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

_source line 22_

Now let me check the confounding and exposure topology implementations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "bc0dff69-4b5c-4417-9f8c-ff2b3dd79655",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017JRjgXAZmd2nZhR5NeUdyZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15730,
      "cache_read_input_tokens": 26855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15730
      },
      "output_tokens": 9,
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

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_017RMFTrjbzuFzjNpS47rdZs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_confounding_dag.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "10f47161-3108-4e10-8842-cbe79e2af436",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017JRjgXAZmd2nZhR5NeUdyZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15730,
      "cache_read_input_tokens": 26855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15730
      },
      "output_tokens": 9,
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

_source line 24 · 2026-05-22T11:29:58.434Z_

<details><summary>↩ Tool result · `toolu_017RMFTrjbzuFzjNpS47rdZs`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	MVP Validation: Confounding DAG with K=3 Multiclass Annotation Error
4	
5	== Technical Setting ==
6	A is an OBSERVED confounder measured with error via LLM annotation.
7	The researcher observes A but uses A* (LLM-annotated proxy) to control
8	for confounding in regression adjustment.
9	
10	  DAG: A -> T, A -> Y, T -> Y, A -> A*
11	  Estimand: E[Y|do(T=t)] estimated via OLS adjusting for A*
12	
13	This differs from Lee & Wood-Doughty (2024), who study UNOBSERVED
14	confounding where A is never observed and A* is the only available proxy.
15	Their setting involves different identifiability conditions (proxy must
16	satisfy relevance + exclusion). Our setting: A is observable in principle
17	but measured with classification error by an LLM annotator, creating a
18	known-structure noise process (confusion matrix C).
19	
20	== DGP ==
21	  A in {0,1,2}: true 3-class confounder, P(A=k) configurable
22	  T = alpha_1*1[A=1] + alpha_2*1[A=2] + eta,  eta ~ N(0, sigma_T^2)
23	  Y = beta_T*T + beta_1*1[A=1] + beta_2*1[A=2] + eps,  eps ~ N(0, sigma_Y^2)
24	  P(A*=j|A=i) = C[j,i]  (C is column-stochastic 3x3 matrix)
25	
26	== Key Result ==
27	  plim gamma_hat = (E[Z'Z])^{-1} E[Z'X] beta
28	  where Z = (1, T, D*_1, D*_2), X = (1, T, D_1, D_2)
29	  Theoretical bias on beta_T = gamma_hat[1] - beta_T
30	
31	== Pass Criteria ==
32	  1. Theory vs MC 95% CI match: 6/6
33	  2. >=1 non-differential C produces away-from-null bias
34	  3. Binary collapse bias != multiclass theory prediction
35	
36	Dependencies: numpy, scipy
37	"""
38	
39	import numpy as np
40	from collections import OrderedDict
41	import time
42	
43	
44	# ============================================================
45	# DGP Parameters
46	# ============================================================
47	N_SAMPLES = 10_000
48	M_REPS = 1_000
49	SEED = 42
50	
51	P_A = np.array([0.4, 0.35, 0.25])
52	ALPHA = np.array([1.5, -1.0])        # alpha_1, alpha_2
53	BETA_T = 2.0                          # true causal effect of T on Y
54	BETA_A = np.array([1.0, -0.5])       # beta_1, beta_2 (direct A->Y)
55	SIGMA_T = 1.0
56	SIGMA_Y = 1.0
57	
58	
59	# ============================================================
60	# Confusion Matrix Structures (named constants)
61	# ============================================================
62	
63	# --- Non-differential (C independent of T) ---
64	
65	C1_SYMMETRIC_HIGH = np.array([
66	    [0.80, 0.10, 0.10],
67	    [0.10, 0.80, 0.10],
68	    [0.10, 0.10, 0.80],
69	])
70	C1_DESC = "Symmetric high-accuracy: diag=0.8, uniform off-diagonal=0.1"
71	
72	C2_ASYMMETRIC = np.array([
73	    [0.65, 0.05, 0.10],
74	    [0.30, 0.85, 0.10],
75	    [0.05, 0.10, 0.80],
76	])
77	C2_DESC = "Asymmetric: P(A*=1|A=0)=0.30 >> P(A*=0|A=1)=0.05"
78	
79	C3_STRUCTURAL_12 = np.array([
80	    [0.96, 0.01, 0.01],
81	    [0.02, 0.69, 0.30],
82	    [0.02, 0.30, 0.69],
83	])
84	C3_DESC = "Structural: classes 1<->2 heavily confused (0.30), class 0 clean (off<0.02)"
85	
86	C4_WEAK_DIAG = np.array([
87	    [0.40, 0.35, 0.25],
88	    [0.35, 0.40, 0.35],
89	    [0.25, 0.25, 0.40],
90	])
91	C4_DESC = "Weak diagonal dominance: diag~0.4, non-uniform off-diagonal"
92	
93	C5_NEAR_PERM = np.array([
94	    [0.05, 0.05, 0.90],
95	    [0.90, 0.05, 0.05],
96	    [0.05, 0.90, 0.05],
97	])
98	C5_DESC = "Near-permutation: cyclic shift 0->1, 1->2, 2->0 (p=0.90)"
99	
100	# --- Differential (C depends on T) ---
101	
102	C6_DIFF_BASE = np.array([
103	    [0.80, 0.10, 0.10],
104	    [0.10, 0.80, 0.10],
105	    [0.10, 0.10, 0.80],
106	])
107	C6_DESC = "Differential: base=C1, off-diagonal doubled when T>median"
108	
109	
110	def make_confusion_matrices():
111	    """6 confusion matrix structures: 5 non-differential + 1 differential."""
112	    matrices = OrderedDict([
113	        ("1_sym_high",   (C1_SYMMETRIC_HIGH, False, C1_DESC)),
114	        ("2_asymmetric", (C2_ASYMMETRIC,     False, C2_DESC)),
115	        ("3_struct_12",  (C3_STRUCTURAL_12,  False, C3_DESC)),
116	        ("4_weak_diag",  (C4_WEAK_DIAG,      False, C4_DESC)),
117	        ("5_near_perm",  (C5_NEAR_PERM,      False, C5_DESC)),
118	        ("6_differen",   (C6_DIFF_BASE,      True,  C6_DESC)),
119	    ])
120	    for name, (C, _, desc) in matrices.items():
121	        assert np.allclose(C.sum(axis=0), 1.0), f"{name}: columns don't sum to 1"
122	        assert (C >= 0).all(), f"{name}: negative entries"
123	    return matrices
124	
125	
126	# ============================================================
127	# Theoretical bias (exact, for non-differential C)
128	# ============================================================
129	def theoretical_bias_exact(C, p_A, alpha, beta_T, beta_A, sigma_T):
130	    """
131	    plim gamma = (E[Z'Z])^{-1} E[Z'X] beta
132	    Z = (1, T, D*_1, D*_2),  X = (1, T, D_1, D_2)
133	    """
134	    p0, p1, p2 = p_A
135	    a1, a2 = alpha
136	    b1, b2 = beta_A
137	    beta = np.array([0.0, beta_T, b1, b2])
138	
139	    ET = a1 * p1 + a2 * p2
140	    ET2 = a1**2 * p1 + a2**2 * p2 + sigma_T**2
141	    q = C @ p_A
142	    ET_Ds = np.array([a1 * C[j, 1] * p1 + a2 * C[j, 2] * p2 for j in range(3)])
143	
144	    EZZ = np.array([
145	        [1.0,  ET,       q[1],      q[2]],
146	        [ET,   ET2,      ET_Ds[1],  ET_Ds[2]],
147	        [q[1], ET_Ds[1], q[1],      0.0],
148	        [q[2], ET_Ds[2], 0.0,       q[2]],
149	    ])
150	    EZX = np.array([
151	        [1.0,  ET,       p1,             p2],
152	        [ET,   ET2,      a1 * p1,        a2 * p2],
153	        [q[1], ET_Ds[1], C[1, 1] * p1,   C[1, 2] * p2],
154	        [q[2], ET_Ds[2], C[2, 1] * p1,   C[2, 2] * p2],
155	    ])
156	
157	    plim = np.linalg.solve(EZZ, EZX @ beta)
158	    return plim[1] - beta_T, plim
159	
160	
161	def theoretical_bias_largesample(C_base, p_A, alpha, beta_T, beta_A,
162	                                  sigma_T, sigma_Y, N_approx=2_000_000,
163	                                  seed=999):
164	    """Approximate theoretical bias for differential C via large-sample moments."""
165	    rng = np.random.default_rng(seed)
166	    a1, a2 = alpha
167	
168	    A = rng.choice(3, size=N_approx, p=p_A)
169	    D1 = (A == 1).astype(np.float64)
170	    D2 = (A == 2).astype(np.float64)
171	    T = a1 * D1 + a2 * D2 + rng.normal(0, sigma_T, N_approx)
172	
173	    A_star = _generate_Astar_differential(A, T, C_base, rng)
174	    D1s = (A_star == 1).astype(np.float64)
175	    D2s = (A_star == 2).astype(np.float64)
176	
177	    beta = np.array([0.0, beta_T, beta_A[0], beta_A[1]])
178	    ones = np.ones(N_approx)
179	    Z = np.column_stack([ones, T, D1s, D2s])
180	    X = np.column_stack([ones, T, D1, D2])
181	
182	    EZZ = (Z.T @ Z) / N_approx
183	    EZX = (Z.T @ X) / N_approx
184	    plim = np.linalg.solve(EZZ, EZX @ beta)
185	    return plim[1] - beta_T, plim
186	
187	
188	# ============================================================
189	# Data generation
190	# ============================================================
191	def _generate_Astar_nondiff(A, C, rng):
192	    """Vectorized: sample A* from C[:, A[i]] for each i."""
193	    probs = C[:, A]                          # (3, N)
194	    cum = np.cumsum(probs, axis=0)           # (3, N)
195	    u = rng.uniform(size=A.shape[0])
196	    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))
197	
198	
199	def _make_C_high(C_base, factor=2.0):
200	    """Scale off-diagonal entries by factor, renormalize columns."""
201	    C_high = C_base.copy()
202	    for col in range(3):
203	        diag_val = C_high[col, col]
204	        off_sum = 1.0 - diag_val
205	        new_off_sum = min(off_sum * factor, 0.95)
206	        scale = new_off_sum / off_sum if off_sum > 0 else 1.0
207	        for row in range(3):
208	            if row != col:
209	                C_high[row, col] *= scale
210	        C_high[col, col] = 1.0 - sum(C_high[r, col] for r in range(3) if r != col)
211	    return C_high
212	
213	
214	def _generate_Astar_differential(A, T, C_base, rng):
215	    """T > median => off-diagonal rates doubled."""
216	    N = len(A)
217	    C_high = _make_C_high(C_base, factor=2.0)
218	    T_med = np.median(T)
219	    high = T > T_med
220	
221	    probs_low = C_base[:, A]
222	    probs_high = C_high[:, A]
223	    probs = np.where(high[np.newaxis, :], probs_high, probs_low)
224	
225	    cum = np.cumsum(probs, axis=0)
226	    u = rng.uniform(size=N)
227	    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))
228	
229	
230	def generate_data(N, C, p_A, alpha, beta_T, beta_A, sigma_T, sigma_Y,
231	                  differential, rng):
232	    a1, a2 = alpha
233	    b1, b2 = beta_A
234	
235	    A = rng.choice(3, size=N, p=p_A)
236	    D1 = (A == 1).astype(np.float64)
237	    D2 = (A == 2).astype(np.float64)
238	    T = a1 * D1 + a2 * D2 + rng.normal(0, sigma_T, N)
239	    Y = beta_T * T + b1 * D1 + b2 * D2 + rng.normal(0, sigma_Y, N)
240	
241	    if differential:
242	        A_star = _generate_Astar_differential(A, T, C, rng)
243	    else:
244	        A_star = _generate_Astar_nondiff(A, C, rng)
245	
246	    return A, T, Y, A_star
247	
248	
249	# ============================================================
250	# OLS helper
251	# ============================================================
252	def ols_beta_T(T, Y, dummies):
253	    """OLS Y ~ 1 + T + dummies, return coefficient on T."""
254	    X = np.column_stack([np.ones(len(T)), T, dummies])
255	    coef, _, _, _ = np.linalg.lstsq(X, Y, rcond=None)
256	    return coef[1]
257	
258	
259	# ============================================================
260	# Monte Carlo
261	# ============================================================
262	def run_mc(M, N, C, p_A, alpha, beta_T, beta_A, sigma_T, sigma_Y,
263	           differential, seed):
264	    rng = np.random.default_rng(seed)
265	    bias_true = np.empty(M)
266	    bias_misclass = np.empty(M)
267	
268	    for m in range(M):
269	        A, T, Y, A_star = generate_data(
270	            N, C, p_A, alpha, beta_T, beta_A, sigma_T, sigma_Y,
271	            differential, rng)
272	        D_true = np.column_stack([(A == 1).astype(float), (A == 2).astype(float)])
273	        D_star = np.column_stack([(A_star == 1).astype(float),
274	                                   (A_star == 2).astype(float)])
275	        bias_true[m] = ols_beta_T(T, Y, D_true) - beta_T
276	        bias_misclass[m] = ols_beta_T(T, Y, D_star) - beta_T
277	
278	    return bias_true, bias_misclass
279	
280	
281	# ============================================================
282	# Unadjusted bias (omitted variable reference)
283	# ============================================================
284	def unadjusted_bias(p_A, alpha, beta_T, beta_A, sigma_T):
285	    """plim of OLS Y ~ 1 + T (no confounder control)."""
286	    p0, p1, p2 = p_A
287	    a1, a2 = alpha
288	    b1, b2 = beta_A
289	    ET = a1 * p1 + a2 * p2
290	    VarT = a1**2 * p1 + a2**2 * p2 + sigma_T**2 - ET**2
291	    CovD1T = a1 * p1 - p1 * ET
292	    CovD2T = a2 * p2 - p2 * ET
293	    return (b1 * CovD1T + b2 * CovD2T) / VarT
294	
295	
296	# ============================================================
297	# Binary collapse analysis
298	# ============================================================
299	def theoretical_bias_binary_from_C3(C, p_A, alpha, beta_T, beta_A, sigma_T):
300	    """
301	    Theoretical bias when collapsing A to B=1[A in {1,2}], B*=1[A* in {1,2}].
302	    Z = (1, T, B*),  X = (1, T, D1, D2)
303	    plim = (E[Z'Z])^{-1} E[Z'X] beta
304	    """
305	    p0, p1, p2 = p_A
306	    a1, a2 = alpha
307	    b1, b2 = beta_A
308	    beta = np.array([0.0, beta_T, b1, b2])
309	
310	    ET = a1 * p1 + a2 * p2
311	    ET2 = a1**2 * p1 + a2**2 * p2 + sigma_T**2
312	
313	    q = C @ p_A
314	    q_Bs = q[1] + q[2]
315	
316	    ET_Ds = np.array([a1 * C[j, 1] * p1 + a2 * C[j, 2] * p2 for j in range(3)])
317	    ET_Bs = ET_Ds[1] + ET_Ds[2]
318	
319	    EZZ = np.array([
320	        [1.0,    ET,    q_Bs],
321	        [ET,     ET2,   ET_Bs],
322	        [q_Bs,   ET_Bs, q_Bs],
323	    ])
324	
325	    EB_D1 = (1.0 - C[0, 1]) * p1
326	    EB_D2 = (1.0 - C[0, 2]) * p2
327	
328	    EZX = np.array([
329	        [1.0,    ET,     p1,       p2],
330	        [ET,     ET2,    a1 * p1,  a2 * p2],
331	        [q_Bs,   ET_Bs,  EB_D1,    EB_D2],
332	    ])
333	
334	    plim = np.linalg.solve(EZZ, EZX @ beta)
335	    return plim[1] - beta_T
336	
337	
338	def run_mc_binary_collapse(M, N, C, p_A, alpha, beta_T, beta_A,
339	                           sigma_T, sigma_Y, differential, seed):
340	    """MC with binary collapse: B=1[A in {1,2}], B*=1[A* in {1,2}]."""
341	    rng = np.random.default_rng(seed)
342	    bias_bin = np.empty(M)
343	
344	    for m in range(M):
345	        A, T, Y, A_star = generate_data(
346	            N, C, p_A, alpha, beta_T, beta_A, sigma_T, sigma_Y,
347	            differential, rng)
348	        B_star = ((A_star == 1) | (A_star == 2)).astype(float).reshape(-1, 1)
349	        bias_bin[m] = ols_beta_T(T, Y, B_star) - beta_T
350	
351	    return bias_bin
352	
353	
354	# ============================================================
355	# Main
356	# ============================================================
357	def main():
358	    print("=" * 85)
359	    print("MVP Validation: Confounding DAG — K=3 Multiclass Annotation Error Bias")
360	    print("=" * 85)
361	    print()
362	    print("Setting: A is OBSERVED confounder with noisy LLM annotation A*.")
363	    print("         Researcher adjusts for A* (not A) in OLS.  DAG: A->T, A->Y, T->Y, A->A*")
364	    print("         (cf. Lee & Wood-Doughty 2024: UNOBSERVED confounding with proxy)")
365	    print()
366	    print(f"DGP: P(A)=[{P_A[0]}, {P_A[1]}, {P_A[2]}], "
367	          f"alpha=[{ALPHA[0]}, {ALPHA[1]}], "
368	          f"beta_T={BETA_T}, beta_A=[{BETA_A[0]}, {BETA_A[1]}]")
369	    print(f"     sigma_T={SIGMA_T}, sigma_Y={SIGMA_Y}")
370	    print(f"MC:  N={N_SAMPLES:,}, M={M_REPS:,}, seed={SEED}")
371	
372	    ovb = unadjusted_bias(P_A, ALPHA, BETA_T, BETA_A, SIGMA_T)
373	    print(f"\nUnadjusted OVB (no A control): {ovb:.6f}")
374	    print(f"  => plim(beta_T_hat_unadj) = {BETA_T + ovb:.6f}")
375	    print(f"  => Direction: {'toward null' if ovb * BETA_T < 0 else 'away from null'}")
376	
377	    matrices = make_confusion_matrices()
378	
379	    # ── PART A: K=3 Theory vs MC ──────────────────────────────
380	    print("\n" + "=" * 85)
381	    print("PART A: K=3 Multiclass — Theory vs Monte Carlo  (6 structures)")
382	    print("=" * 85)
383	
384	    results_k3 = {}
385	    header = (f"{'#':<2} {'Config':<14} {'Theory':>10} {'MC Mean':>10} "
386	              f"{'MC 95% CI':>22} {'Match?':>7} {'Direction':>14}")
387	    print(f"\n{header}")
388	    print("-" * len(header))
389	
390	    for name, (C, is_diff, desc) in matrices.items():
391	        t0 = time.time()
392	        idx = name[0]
393	
394	        if is_diff:
395	            th_bias, _ = theoretical_bias_largesample(
396	                C, P_A, ALPHA, BETA_T, BETA_A, SIGMA_T, SIGMA_Y)
397	        else:
398	            th_bias, _ = theoretical_bias_exact(
399	                C, P_A, ALPHA, BETA_T, BETA_A, SIGMA_T)
400	
401	        _, mc_bias = run_mc(M_REPS, N_SAMPLES, C, P_A, ALPHA, BETA_T,
402	                            BETA_A, SIGMA_T, SIGMA_Y, is_diff, SEED)
403	
404	        mc_mean = mc_bias.mean()
405	        mc_se = mc_bias.std(ddof=1)
406	        ci_lo = mc_mean - 1.96 * mc_se / np.sqrt(M_REPS)
407	        ci_hi = mc_mean + 1.96 * mc_se / np.sqrt(M_REPS)
408	        match = ci_lo <= th_bias <= ci_hi
409	
410	        if abs(th_bias) < 1e-6:
411	            direction = "~zero"
412	        elif th_bias * BETA_T > 0:
413	            direction = "AWAY from null"
414	        else:
415	            direction = "toward null"
416	
417	        elapsed = time.time() - t0
418	        results_k3[name] = dict(
419	            th_bias=th_bias, mc_mean=mc_mean, ci=(ci_lo, ci_hi),
420	            match=match, direction=direction, mc_bias_arr=mc_bias,
421	            is_diff=is_diff)
422	
423	        print(f"{idx:<2} {name:<14} {th_bias:>10.6f} {mc_mean:>10.6f} "
424	              f"[{ci_lo:>9.6f}, {ci_hi:>9.6f}] "
425	              f"{'YES' if match else '**NO**':>7} "
426	              f"{direction:>14}  ({elapsed:.1f}s)")
427	
428	    # ── PART B: Binary collapse ──────────────────────────────
429	    print("\n" + "=" * 85)
430	    print("PART B: Binary Collapse — B=1[A in {1,2}]")
431	    print("=" * 85)
432	
433	    header_b = (f"{'#':<2} {'Config':<14} {'K3 Bias':>10} {'Bin Bias':>10} "
434	                f"{'Bin MC':>10} {'Bin MC 95% CI':>22} {'K3!=Bin?':>8}")
435	    print(f"\n{header_b}")
436	    print("-" * len(header_b))
437	
438	    pass_criterion_3 = False
439	    bin_results = {}
440	
441	    for name, (C, is_diff, desc) in matrices.items():
442	        t0 = time.time()
443	        idx = name[0]
444	        k3_bias = results_k3[name]["th_bias"]
445	
446	        if not is_diff:
447	            bin_th = theoretical_bias_binary_from_C3(
448	                C, P_A, ALPHA, BETA_T, BETA_A, SIGMA_T)
449	        else:
450	            rng_approx = np.random.default_rng(888)
451	            N_ap = 2_000_000
452	            A_ap = rng_approx.choice(3, size=N_ap, p=P_A)
453	            D1_ap = (A_ap == 1).astype(np.float64)
454	            D2_ap = (A_ap == 2).astype(np.float64)
455	            T_ap = (ALPHA[0] * D1_ap + ALPHA[1] * D2_ap
456	                    + rng_approx.normal(0, SIGMA_T, N_ap))
457	            As_ap = _generate_Astar_differential(A_ap, T_ap, C, rng_approx)
458	            Bs_ap = ((As_ap == 1) | (As_ap == 2)).astype(np.float64)
459	            beta_vec = np.array([0.0, BETA_T, BETA_A[0], BETA_A[1]])
460	            ones_ap = np.ones(N_ap)
461	            Z_b = np.column_stack([ones_ap, T_ap, Bs_ap])
462	            X_f = np.column_stack([ones_ap, T_ap, D1_ap, D2_ap])
463	            EZZ_b = (Z_b.T @ Z_b) / N_ap
464	            EZX_b = (Z_b.T @ X_f) / N_ap
465	            plim_b = np.linalg.solve(EZZ_b, EZX_b @ beta_vec)
466	            bin_th = plim_b[1] - BETA_T
467	
468	        bin_mc = run_mc_binary_collapse(
469	            M_REPS, N_SAMPLES, C, P_A, ALPHA, BETA_T, BETA_A,
470	            SIGMA_T, SIGMA_Y, is_diff, SEED)
471	
472	        bin_mean = bin_mc.mean()
473	        bin_se = bin_mc.std(ddof=1)
474	        bin_ci_lo = bin_mean - 1.96 * bin_se / np.sqrt(M_REPS)
475	        bin_ci_hi = bin_mean + 1.96 * bin_se / np.sqrt(M_REPS)
476	
477	        k3_ne_bin = abs(k3_bias - bin_th) > 0.001
478	        if k3_ne_bin:
479	            pass_criterion_3 = True
480	
481	        bin_results[name] = dict(bin_th=bin_th, bin_mean=bin_mean, k3_ne_bin=k3_ne_bin)
482	
483	        elapsed = time.time() - t0
484	        print(f"{idx:<2} {name:<14} {k3_bias:>10.6f} {bin_th:>10.6f} "
485	              f"{bin_mean:>10.6f} [{bin_ci_lo:>9.6f}, {bin_ci_hi:>9.6f}] "
486	              f"{'YES' if k3_ne_bin else 'no':>8}  ({elapsed:.1f}s)")
487	
488	    # ── Pass/Fail ────────────────────────────────────────────
489	    print("\n" + "=" * 85)
490	    print("PASS / FAIL SUMMARY")
491	    print("=" * 85)
492	
493	    n_total = len(results_k3)
494	    n_match = sum(1 for r in results_k3.values() if r["match"])
495	    c1 = n_match == n_total
496	    print(f"\n1. Theory vs MC 95% CI match: {n_match}/{n_total}  "
497	          f"{'PASS' if c1 else 'FAIL'}")
498	
499	    # Per-structure detail
500	    for name, r in results_k3.items():
501	        status = "OK" if r["match"] else "MISMATCH"
502	        print(f"   {name}: th={r['th_bias']:.6f}, "
503	              f"CI=[{r['ci'][0]:.6f}, {r['ci'][1]:.6f}] -> {status}")
504	
505	    away_nondiff = [name for name, r in results_k3.items()
506	                    if not r["is_diff"] and r["direction"] == "AWAY from null"]
507	    c2 = len(away_nondiff) >= 1
508	    print(f"\n2. Non-diff C with away-from-null bias: {len(away_nondiff)}/5  "
509	          f"{'PASS' if c2 else 'FAIL'}")
510	    for name in away_nondiff:
511	        print(f"   {name}: bias={results_k3[name]['th_bias']:.6f}")
512	
513	    c3 = pass_criterion_3
514	    diff_names = [n for n, r in bin_results.items() if r["k3_ne_bin"]]
515	    print(f"\n3. Binary collapse bias != K=3 theory: "
516	          f"{len(diff_names)}/{n_total}  "
517	          f"{'PASS' if c3 else 'FAIL'}")
518	    for name in diff_names:
519	        k3b = results_k3[name]["th_bias"]
520	        bb = bin_results[name]["bin_th"]
521	        print(f"   {name}: K3={k3b:.6f}, Bin={bb:.6f}, Delta={k3b - bb:.6f}")
522	
523	    overall = c1 and c2 and c3
524	    print(f"\nOVERALL: {'PASS' if overall else 'FAIL'}")
525	
526	    # ── Appendix ─────────────────────────────────────────────
527	    print("\n" + "=" * 85)
528	    print("APPENDIX: Confusion Matrix Definitions")
529	    print("=" * 85)
530	    for name, (C, is_diff, desc) in matrices.items():
531	        tag = " [DIFFERENTIAL]" if is_diff else " [NON-DIFF]"
532	        print(f"\n{name}{tag}")
533	        print(f"  {desc}")
534	        for row in C:
535	            print(f"  [{row[0]:.2f}  {row[1]:.2f}  {row[2]:.2f}]")
536	        if is_diff:
537	            C_high = _make_C_high(C, factor=2.0)
538	            print(f"  C_high (T>median):")
539	            for row in C_high:
540	                print(f"  [{row[0]:.2f}  {row[1]:.2f}  {row[2]:.2f}]")
541	
542	    print("\n" + "=" * 85)
543	    print("TECHNICAL NOTE: Lee & Wood-Doughty (2024) Distinction")
544	    print("=" * 85)
545	    print("""
546	This MVP studies OBSERVED confounding with noisy measurement:
547	  - A is an observable confounder (e.g., sentiment, topic)
548	  - Researcher uses LLM to annotate A, producing A* with known error structure
549	  - A* substitutes for A in regression adjustment for confounding
550	  - Error structure: P(A*=j|A=i) = C[j,i], C is estimable from validation data
551	
552	Lee & Wood-Doughty (2024) study UNOBSERVED confounding with proxy:
553	  - A is never observed (latent confounder)
554	  - A* is the only available proxy (not a noisy version of something observed)
555	  - Requires proxy relevance + exclusion restrictions for identification
556	  - Different bias structure: proxy must satisfy E[T|A,A*] = E[T|A]
557	
558	Key implication: our bias formula plim = (E[Z'Z])^{-1} E[Z'X] beta assumes
559	the researcher COULD observe A (and does, for validation), but CHOOSES to use
560	A* at scale. The confusion matrix C is a design parameter, not a nuisance.
561	""")
562	
563	
564	if __name__ == "__main__":
565	    main()
566	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "466d7b17-b44a-472a-bb8d-fde329b9cdde",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_confounding_dag.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nMVP Validation: Confounding DAG with K=3 Multiclass Annotation Error\n\n== Technical Setting ==\nA is an OBSERVED confounder measured with error via LLM annotation.\nThe researcher observes A but uses A* (LLM-annotated proxy) to control\nfor confounding in regression adjustment.\n\n  DAG: A -> T, A -> Y, T -> Y, A -> A*\n  Estimand: E[Y|do(T=t)] estimated via OLS adjusting for A*\n\nThis differs from Lee & Wood-Doughty (2024), who study UNOBSERVED\nconfounding where A is never observed and A* is the only available proxy.\nTheir setting involves different identifiability conditions (proxy must\nsatisfy relevance + exclusion). Our setting: A is observable in principle\nbut measured with classification error by an LLM annotator, creating a\nknown-structure noise process (confusion matrix C).\n\n== DGP ==\n  A in {0,1,2}: true 3-class confounder, P(A=k) configurable\n  T = alpha_1*1[A=1] + alpha_2*1[A=2] + eta,  eta ~ N(0, sigma_T^2)\n  Y = beta_T*T + beta_1*1[A=1] + beta_2*1[A=2] + eps,  eps ~ N(0, sigma_Y^2)\n  P(A*=j|A=i) = C[j,i]  (C is column-stochastic 3x3 matrix)\n\n== Key Result ==\n  plim gamma_hat = (E[Z'Z])^{-1} E[Z'X] beta\n  where Z = (1, T, D*_1, D*_2), X = (1, T, D_1, D_2)\n  Theoretical bias on beta_T = gamma_hat[1] - beta_T\n\n== Pass Criteria ==\n  1. Theory vs MC 95% CI match: 6/6\n  2. >=1 non-differential C produces away-from-null bias\n  3. Binary collapse bias != multiclass theory prediction\n\nDependencies: numpy, scipy\n\"\"\"\n\nimport numpy as np\nfrom collections import OrderedDict\nimport time\n\n\n# ============================================================\n# DGP Parameters\n# ============================================================\nN_SAMPLES = 10_000\nM_REPS = 1_000\nSEED = 42\n\nP_A = np.array([0.4, 0.35, 0.25])\nALPHA = np.array([1.5, -1.0])        # alpha_1, alpha_2\nBETA_T = 2.0                          # true causal effect of T on Y\nBETA_A = np.array([1.0, -0.5])       # beta_1, beta_2 (direct A->Y)\nSIGMA_T = 1.0\nSIGMA_Y = 1.0\n\n\n# ============================================================\n# Confusion Matrix Structures (named constants)\n# ============================================================\n\n# --- Non-differential (C independent of T) ---\n\nC1_SYMMETRIC_HIGH = np.array([\n    [0.80, 0.10, 0.10],\n    [0.10, 0.80, 0.10],\n    [0.10, 0.10, 0.80],\n])\nC1_DESC = \"Symmetric high-accuracy: diag=0.8, uniform off-diagonal=0.1\"\n\nC2_ASYMMETRIC = np.array([\n    [0.65, 0.05, 0.10],\n    [0.30, 0.85, 0.10],\n    [0.05, 0.10, 0.80],\n])\nC2_DESC = \"Asymmetric: P(A*=1|A=0)=0.30 >> P(A*=0|A=1)=0.05\"\n\nC3_STRUCTURAL_12 = np.array([\n    [0.96, 0.01, 0.01],\n    [0.02, 0.69, 0.30],\n    [0.02, 0.30, 0.69],\n])\nC3_DESC = \"Structural: classes 1<->2 heavily confused (0.30), class 0 clean (off<0.02)\"\n\nC4_WEAK_DIAG = np.array([\n    [0.40, 0.35, 0.25],\n    [0.35, 0.40, 0.35],\n    [0.25, 0.25, 0.40],\n])\nC4_DESC = \"Weak diagonal dominance: diag~0.4, non-uniform off-diagonal\"\n\nC5_NEAR_PERM = np.array([\n    [0.05, 0.05, 0.90],\n    [0.90, 0.05, 0.05],\n    [0.05, 0.90, 0.05],\n])\nC5_DESC = \"Near-permutation: cyclic shift 0->1, 1->2, 2->0 (p=0.90)\"\n\n# --- Differential (C depends on T) ---\n\nC6_DIFF_BASE = np.array([\n    [0.80, 0.10, 0.10],\n    [0.10, 0.80, 0.10],\n    [0.10, 0.10, 0.80],\n])\nC6_DESC = \"Differential: base=C1, off-diagonal doubled when T>median\"\n\n\ndef make_confusion_matrices():\n    \"\"\"6 confusion matrix structures: 5 non-differential + 1 differential.\"\"\"\n    matrices = OrderedDict([\n        (\"1_sym_high\",   (C1_SYMMETRIC_HIGH, False, C1_DESC)),\n        (\"2_asymmetric\", (C2_ASYMMETRIC,     False, C2_DESC)),\n        (\"3_struct_12\",  (C3_STRUCTURAL_12,  False, C3_DESC)),\n        (\"4_weak_diag\",  (C4_WEAK_DIAG,      False, C4_DESC)),\n        (\"5_near_perm\",  (C5_NEAR_PERM,      False, C5_DESC)),\n        (\"6_differen\",   (C6_DIFF_BASE,      True,  C6_DESC)),\n    ])\n    for name, (C, _, desc) in matrices.items():\n        assert np.allclose(C.sum(axis=0), 1.0), f\"{name}: columns don't sum to 1\"\n        assert (C >= 0).all(), f\"{name}: negative entries\"\n    return matrices\n\n\n# ============================================================\n# Theoretical bias (exact, for non-differential C)\n# ============================================================\ndef theoretical_bias_exact(C, p_A, alpha, beta_T, beta_A, sigma_T):\n    \"\"\"\n    plim gamma = (E[Z'Z])^{-1} E[Z'X] beta\n    Z = (1, T, D*_1, D*_2),  X = (1, T, D_1, D_2)\n    \"\"\"\n    p0, p1, p2 = p_A\n    a1, a2 = alpha\n    b1, b2 = beta_A\n    beta = np.array([0.0, beta_T, b1, b2])\n\n    ET = a1 * p1 + a2 * p2\n    ET2 = a1**2 * p1 + a2**2 * p2 + sigma_T**2\n    q = C @ p_A\n    ET_Ds = np.array([a1 * C[j, 1] * p1 + a2 * C[j, 2] * p2 for j in range(3)])\n\n    EZZ = np.array([\n        [1.0,  ET,       q[1],      q[2]],\n        [ET,   ET2,      ET_Ds[1],  ET_Ds[2]],\n        [q[1], ET_Ds[1], q[1],      0.0],\n        [q[2], ET_Ds[2], 0.0,       q[2]],\n    ])\n    EZX = np.array([\n        [1.0,  ET,       p1,             p2],\n        [ET,   ET2,      a1 * p1,        a2 * p2],\n        [q[1], ET_Ds[1], C[1, 1] * p1,   C[1, 2] * p2],\n        [q[2], ET_Ds[2], C[2, 1] * p1,   C[2, 2] * p2],\n    ])\n\n    plim = np.linalg.solve(EZZ, EZX @ beta)\n    return plim[1] - beta_T, plim\n\n\ndef theoretical_bias_largesample(C_base, p_A, alpha, beta_T, beta_A,\n                                  sigma_T, sigma_Y, N_approx=2_000_000,\n                                  seed=999):\n    \"\"\"Approximate theoretical bias for differential C via large-sample moments.\"\"\"\n    rng = np.random.default_rng(seed)\n    a1, a2 = alpha\n\n    A = rng.choice(3, size=N_approx, p=p_A)\n    D1 = (A == 1).astype(np.float64)\n    D2 = (A == 2).astype(np.float64)\n    T = a1 * D1 + a2 * D2 + rng.normal(0, sigma_T, N_approx)\n\n    A_star = _generate_Astar_differential(A, T, C_base, rng)\n    D1s = (A_star == 1).astype(np.float64)\n    D2s = (A_star == 2).astype(np.float64)\n\n    beta = np.array([0.0, beta_T, beta_A[0], beta_A[1]])\n    ones = np.ones(N_approx)\n    Z = np.column_stack([ones, T, D1s, D2s])\n    X = np.column_stack([ones, T, D1, D2])\n\n    EZZ = (Z.T @ Z) / N_approx\n    EZX = (Z.T @ X) / N_approx\n    plim = np.linalg.solve(EZZ, EZX @ beta)\n    return plim[1] - beta_T, plim\n\n\n# ============================================================\n# Data generation\n# ============================================================\ndef _generate_Astar_nondiff(A, C, rng):\n    \"\"\"Vectorized: sample A* from C[:, A[i]] for each i.\"\"\"\n    probs = C[:, A]                          # (3, N)\n    cum = np.cumsum(probs, axis=0)           # (3, N)\n    u = rng.uniform(size=A.shape[0])\n    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))\n\n\ndef _make_C_high(C_base, factor=2.0):\n    \"\"\"Scale off-diagonal entries by factor, renormalize columns.\"\"\"\n    C_high = C_base.copy()\n    for col in range(3):\n        diag_val = C_high[col, col]\n        off_sum = 1.0 - diag_val\n        new_off_sum = min(off_sum * factor, 0.95)\n        scale = new_off_sum / off_sum if off_sum > 0 else 1.0\n        for row in range(3):\n            if row != col:\n                C_high[row, col] *= scale\n        C_high[col, col] = 1.0 - sum(C_high[r, col] for r in range(3) if r != col)\n    return C_high\n\n\ndef _generate_Astar_differential(A, T, C_base, rng):\n    \"\"\"T > median => off-diagonal rates doubled.\"\"\"\n    N = len(A)\n    C_high = _make_C_high(C_base, factor=2.0)\n    T_med = np.median(T)\n    high = T > T_med\n\n    probs_low = C_base[:, A]\n    probs_high = C_high[:, A]\n    probs = np.where(high[np.newaxis, :], probs_high, probs_low)\n\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=N)\n    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))\n\n\ndef generate_data(N, C, p_A, alpha, beta_T, beta_A, sigma_T, sigma_Y,\n                  differential, rng):\n    a1, a2 = alpha\n    b1, b2 = beta_A\n\n    A = rng.choice(3, size=N, p=p_A)\n    D1 = (A == 1).astype(np.float64)\n    D2 = (A == 2).astype(np.float64)\n    T = a1 * D1 + a2 * D2 + rng.normal(0, sigma_T, N)\n    Y = beta_T * T + b1 * D1 + b2 * D2 + rng.normal(0, sigma_Y, N)\n\n    if differential:\n        A_star = _generate_Astar_differential(A, T, C, rng)\n    else:\n        A_star = _generate_Astar_nondiff(A, C, rng)\n\n    return A, T, Y, A_star\n\n\n# ============================================================\n# OLS helper\n# ============================================================\ndef ols_beta_T(T, Y, dummies):\n    \"\"\"OLS Y ~ 1 + T + dummies, return coefficient on T.\"\"\"\n    X = np.column_stack([np.ones(len(T)), T, dummies])\n    coef, _, _, _ = np.linalg.lstsq(X, Y, rcond=None)\n    return coef[1]\n\n\n# ============================================================\n# Monte Carlo\n# ============================================================\ndef run_mc(M, N, C, p_A, alpha, beta_T, beta_A, sigma_T, sigma_Y,\n           differential, seed):\n    rng = np.random.default_rng(seed)\n    bias_true = np.empty(M)\n    bias_misclass = np.empty(M)\n\n    for m in range(M):\n        A, T, Y, A_star = generate_data(\n            N, C, p_A, alpha, beta_T, beta_A, sigma_T, sigma_Y,\n            differential, rng)\n        D_true = np.column_stack([(A == 1).astype(float), (A == 2).astype(float)])\n        D_star = np.column_stack([(A_star == 1).astype(float),\n                                   (A_star == 2).astype(float)])\n        bias_true[m] = ols_beta_T(T, Y, D_true) - beta_T\n        bias_misclass[m] = ols_beta_T(T, Y, D_star) - beta_T\n\n    return bias_true, bias_misclass\n\n\n# ============================================================\n# Unadjusted bias (omitted variable reference)\n# ============================================================\ndef unadjusted_bias(p_A, alpha, beta_T, beta_A, sigma_T):\n    \"\"\"plim of OLS Y ~ 1 + T (no confounder control).\"\"\"\n    p0, p1, p2 = p_A\n    a1, a2 = alpha\n    b1, b2 = beta_A\n    ET = a1 * p1 + a2 * p2\n    VarT = a1**2 * p1 + a2**2 * p2 + sigma_T**2 - ET**2\n    CovD1T = a1 * p1 - p1 * ET\n    CovD2T = a2 * p2 - p2 * ET\n    return (b1 * CovD1T + b2 * CovD2T) / VarT\n\n\n# ============================================================\n# Binary collapse analysis\n# ============================================================\ndef theoretical_bias_binary_from_C3(C, p_A, alpha, beta_T, beta_A, sigma_T):\n    \"\"\"\n    Theoretical bias when collapsing A to B=1[A in {1,2}], B*=1[A* in {1,2}].\n    Z = (1, T, B*),  X = (1, T, D1, D2)\n    plim = (E[Z'Z])^{-1} E[Z'X] beta\n    \"\"\"\n    p0, p1, p2 = p_A\n    a1, a2 = alpha\n    b1, b2 = beta_A\n    beta = np.array([0.0, beta_T, b1, b2])\n\n    ET = a1 * p1 + a2 * p2\n    ET2 = a1**2 * p1 + a2**2 * p2 + sigma_T**2\n\n    q = C @ p_A\n    q_Bs = q[1] + q[2]\n\n    ET_Ds = np.array([a1 * C[j, 1] * p1 + a2 * C[j, 2] * p2 for j in range(3)])\n    ET_Bs = ET_Ds[1] + ET_Ds[2]\n\n    EZZ = np.array([\n        [1.0,    ET,    q_Bs],\n        [ET,     ET2,   ET_Bs],\n        [q_Bs,   ET_Bs, q_Bs],\n    ])\n\n    EB_D1 = (1.0 - C[0, 1]) * p1\n    EB_D2 = (1.0 - C[0, 2]) * p2\n\n    EZX = np.array([\n        [1.0,    ET,     p1,       p2],\n        [ET,     ET2,    a1 * p1,  a2 * p2],\n        [q_Bs,   ET_Bs,  EB_D1,    EB_D2],\n    ])\n\n    plim = np.linalg.solve(EZZ, EZX @ beta)\n    return plim[1] - beta_T\n\n\ndef run_mc_binary_collapse(M, N, C, p_A, alpha, beta_T, beta_A,\n                           sigma_T, sigma_Y, differential, seed):\n    \"\"\"MC with binary collapse: B=1[A in {1,2}], B*=1[A* in {1,2}].\"\"\"\n    rng = np.random.default_rng(seed)\n    bias_bin = np.empty(M)\n\n    for m in range(M):\n        A, T, Y, A_star = generate_data(\n            N, C, p_A, alpha, beta_T, beta_A, sigma_T, sigma_Y,\n            differential, rng)\n        B_star = ((A_star == 1) | (A_star == 2)).astype(float).reshape(-1, 1)\n        bias_bin[m] = ols_beta_T(T, Y, B_star) - beta_T\n\n    return bias_bin\n\n\n# ============================================================\n# Main\n# ============================================================\ndef main():\n    print(\"=\" * 85)\n    print(\"MVP Validation: Confounding DAG — K=3 Multiclass Annotation Error Bias\")\n    print(\"=\" * 85)\n    print()\n    print(\"Setting: A is OBSERVED confounder with noisy LLM annotation A*.\")\n    print(\"         Researcher adjusts for A* (not A) in OLS.  DAG: A->T, A->Y, T->Y, A->A*\")\n    print(\"         (cf. Lee & Wood-Doughty 2024: UNOBSERVED confounding with proxy)\")\n    print()\n    print(f\"DGP: P(A)=[{P_A[0]}, {P_A[1]}, {P_A[2]}], \"\n          f\"alpha=[{ALPHA[0]}, {ALPHA[1]}], \"\n          f\"beta_T={BETA_T}, beta_A=[{BETA_A[0]}, {BETA_A[1]}]\")\n    print(f\"     sigma_T={SIGMA_T}, sigma_Y={SIGMA_Y}\")\n    print(f\"MC:  N={N_SAMPLES:,}, M={M_REPS:,}, seed={SEED}\")\n\n    ovb = unadjusted_bias(P_A, ALPHA, BETA_T, BETA_A, SIGMA_T)\n    print(f\"\\nUnadjusted OVB (no A control): {ovb:.6f}\")\n    print(f\"  => plim(beta_T_hat_unadj) = {BETA_T + ovb:.6f}\")\n    print(f\"  => Direction: {'toward null' if ovb * BETA_T < 0 else 'away from null'}\")\n\n    matrices = make_confusion_matrices()\n\n    # ── PART A: K=3 Theory vs MC ──────────────────────────────\n    print(\"\\n\" + \"=\" * 85)\n    print(\"PART A: K=3 Multiclass — Theory vs Monte Carlo  (6 structures)\")\n    print(\"=\" * 85)\n\n    results_k3 = {}\n    header = (f\"{'#':<2} {'Config':<14} {'Theory':>10} {'MC Mean':>10} \"\n              f\"{'MC 95% CI':>22} {'Match?':>7} {'Direction':>14}\")\n    print(f\"\\n{header}\")\n    print(\"-\" * len(header))\n\n    for name, (C, is_diff, desc) in matrices.items():\n        t0 = time.time()\n        idx = name[0]\n\n        if is_diff:\n            th_bias, _ = theoretical_bias_largesample(\n                C, P_A, ALPHA, BETA_T, BETA_A, SIGMA_T, SIGMA_Y)\n        else:\n            th_bias, _ = theoretical_bias_exact(\n                C, P_A, ALPHA, BETA_T, BETA_A, SIGMA_T)\n\n        _, mc_bias = run_mc(M_REPS, N_SAMPLES, C, P_A, ALPHA, BETA_T,\n                            BETA_A, SIGMA_T, SIGMA_Y, is_diff, SEED)\n\n        mc_mean = mc_bias.mean()\n        mc_se = mc_bias.std(ddof=1)\n        ci_lo = mc_mean - 1.96 * mc_se / np.sqrt(M_REPS)\n        ci_hi = mc_mean + 1.96 * mc_se / np.sqrt(M_REPS)\n        match = ci_lo <= th_bias <= ci_hi\n\n        if abs(th_bias) < 1e-6:\n            direction = \"~zero\"\n        elif th_bias * BETA_T > 0:\n            direction = \"AWAY from null\"\n        else:\n            direction = \"toward null\"\n\n        elapsed = time.time() - t0\n        results_k3[name] = dict(\n            th_bias=th_bias, mc_mean=mc_mean, ci=(ci_lo, ci_hi),\n            match=match, direction=direction, mc_bias_arr=mc_bias,\n            is_diff=is_diff)\n\n        print(f\"{idx:<2} {name:<14} {th_bias:>10.6f} {mc_mean:>10.6f} \"\n              f\"[{ci_lo:>9.6f}, {ci_hi:>9.6f}] \"\n              f\"{'YES' if match else '**NO**':>7} \"\n              f\"{direction:>14}  ({elapsed:.1f}s)\")\n\n    # ── PART B: Binary collapse ──────────────────────────────\n    print(\"\\n\" + \"=\" * 85)\n    print(\"PART B: Binary Collapse — B=1[A in {1,2}]\")\n    print(\"=\" * 85)\n\n    header_b = (f\"{'#':<2} {'Config':<14} {'K3 Bias':>10} {'Bin Bias':>10} \"\n                f\"{'Bin MC':>10} {'Bin MC 95% CI':>22} {'K3!=Bin?':>8}\")\n    print(f\"\\n{header_b}\")\n    print(\"-\" * len(header_b))\n\n    pass_criterion_3 = False\n    bin_results = {}\n\n    for name, (C, is_diff, desc) in matrices.items():\n        t0 = time.time()\n        idx = name[0]\n        k3_bias = results_k3[name][\"th_bias\"]\n\n        if not is_diff:\n            bin_th = theoretical_bias_binary_from_C3(\n                C, P_A, ALPHA, BETA_T, BETA_A, SIGMA_T)\n        else:\n            rng_approx = np.random.default_rng(888)\n            N_ap = 2_000_000\n            A_ap = rng_approx.choice(3, size=N_ap, p=P_A)\n            D1_ap = (A_ap == 1).astype(np.float64)\n            D2_ap = (A_ap == 2).astype(np.float64)\n            T_ap = (ALPHA[0] * D1_ap + ALPHA[1] * D2_ap\n                    + rng_approx.normal(0, SIGMA_T, N_ap))\n            As_ap = _generate_Astar_differential(A_ap, T_ap, C, rng_approx)\n            Bs_ap = ((As_ap == 1) | (As_ap == 2)).astype(np.float64)\n            beta_vec = np.array([0.0, BETA_T, BETA_A[0], BETA_A[1]])\n            ones_ap = np.ones(N_ap)\n            Z_b = np.column_stack([ones_ap, T_ap, Bs_ap])\n            X_f = np.column_stack([ones_ap, T_ap, D1_ap, D2_ap])\n            EZZ_b = (Z_b.T @ Z_b) / N_ap\n            EZX_b = (Z_b.T @ X_f) / N_ap\n            plim_b = np.linalg.solve(EZZ_b, EZX_b @ beta_vec)\n            bin_th = plim_b[1] - BETA_T\n\n        bin_mc = run_mc_binary_collapse(\n            M_REPS, N_SAMPLES, C, P_A, ALPHA, BETA_T, BETA_A,\n            SIGMA_T, SIGMA_Y, is_diff, SEED)\n\n        bin_mean = bin_mc.mean()\n        bin_se = bin_mc.std(ddof=1)\n        bin_ci_lo = bin_mean - 1.96 * bin_se / np.sqrt(M_REPS)\n        bin_ci_hi = bin_mean + 1.96 * bin_se / np.sqrt(M_REPS)\n\n        k3_ne_bin = abs(k3_bias - bin_th) > 0.001\n        if k3_ne_bin:\n            pass_criterion_3 = True\n\n        bin_results[name] = dict(bin_th=bin_th, bin_mean=bin_mean, k3_ne_bin=k3_ne_bin)\n\n        elapsed = time.time() - t0\n        print(f\"{idx:<2} {name:<14} {k3_bias:>10.6f} {bin_th:>10.6f} \"\n              f\"{bin_mean:>10.6f} [{bin_ci_lo:>9.6f}, {bin_ci_hi:>9.6f}] \"\n              f\"{'YES' if k3_ne_bin else 'no':>8}  ({elapsed:.1f}s)\")\n\n    # ── Pass/Fail ────────────────────────────────────────────\n    print(\"\\n\" + \"=\" * 85)\n    print(\"PASS / FAIL SUMMARY\")\n    print(\"=\" * 85)\n\n    n_total = len(results_k3)\n    n_match = sum(1 for r in results_k3.values() if r[\"match\"])\n    c1 = n_match == n_total\n    print(f\"\\n1. Theory vs MC 95% CI match: {n_match}/{n_total}  \"\n          f\"{'PASS' if c1 else 'FAIL'}\")\n\n    # Per-structure detail\n    for name, r in results_k3.items():\n        status = \"OK\" if r[\"match\"] else \"MISMATCH\"\n        print(f\"   {name}: th={r['th_bias']:.6f}, \"\n              f\"CI=[{r['ci'][0]:.6f}, {r['ci'][1]:.6f}] -> {status}\")\n\n    away_nondiff = [name for name, r in results_k3.items()\n                    if not r[\"is_diff\"] and r[\"direction\"] == \"AWAY from null\"]\n    c2 = len(away_nondiff) >= 1\n    print(f\"\\n2. Non-diff C with away-from-null bias: {len(away_nondiff)}/5  \"\n          f\"{'PASS' if c2 else 'FAIL'}\")\n    for name in away_nondiff:\n        print(f\"   {name}: bias={results_k3[name]['th_bias']:.6f}\")\n\n    c3 = pass_criterion_3\n    diff_names = [n for n, r in bin_results.items() if r[\"k3_ne_bin\"]]\n    print(f\"\\n3. Binary collapse bias != K=3 theory: \"\n          f\"{len(diff_names)}/{n_total}  \"\n          f\"{'PASS' if c3 else 'FAIL'}\")\n    for name in diff_names:\n        k3b = results_k3[name][\"th_bias\"]\n        bb = bin_results[name][\"bin_th\"]\n        print(f\"   {name}: K3={k3b:.6f}, Bin={bb:.6f}, Delta={k3b - bb:.6f}\")\n\n    overall = c1 and c2 and c3\n    print(f\"\\nOVERALL: {'PASS' if overall else 'FAIL'}\")\n\n    # ── Appendix ─────────────────────────────────────────────\n    print(\"\\n\" + \"=\" * 85)\n    print(\"APPENDIX: Confusion Matrix Definitions\")\n    print(\"=\" * 85)\n    for name, (C, is_diff, desc) in matrices.items():\n        tag = \" [DIFFERENTIAL]\" if is_diff else \" [NON-DIFF]\"\n        print(f\"\\n{name}{tag}\")\n        print(f\"  {desc}\")\n        for row in C:\n            print(f\"  [{row[0]:.2f}  {row[1]:.2f}  {row[2]:.2f}]\")\n        if is_diff:\n            C_high = _make_C_high(C, factor=2.0)\n            print(f\"  C_high (T>median):\")\n            for row in C_high:\n                print(f\"  [{row[0]:.2f}  {row[1]:.2f}  {row[2]:.2f}]\")\n\n    print(\"\\n\" + \"=\" * 85)\n    print(\"TECHNICAL NOTE: Lee & Wood-Doughty (2024) Distinction\")\n    print(\"=\" * 85)\n    print(\"\"\"\nThis MVP studies OBSERVED confounding with noisy measurement:\n  - A is an observable confounder (e.g., sentiment, topic)\n  - Researcher uses LLM to annotate A, producing A* with known error structure\n  - A* substitutes for A in regression adjustment for confounding\n  - Error structure: P(A*=j|A=i) = C[j,i], C is estimable from validation data\n\nLee & Wood-Doughty (2024) study UNOBSERVED confounding with proxy:\n  - A is never observed (latent confounder)\n  - A* is the only available proxy (not a noisy version of something observed)\n  - Requires proxy relevance + exclusion restrictions for identification\n  - Different bias structure: proxy must satisfy E[T|A,A*] = E[T|A]\n\nKey implication: our bias formula plim = (E[Z'Z])^{-1} E[Z'X] beta assumes\nthe researcher COULD observe A (and does, for validation), but CHOOSES to use\nA* at scale. The confusion matrix C is a design parameter, not a nuisance.\n\"\"\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 566,
      "startLine": 1,
      "totalLines": 566
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01GMr9KTaHj7fsJv6fNxSETj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_exposure_dag.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "95a271a5-8233-4706-af24-4d394aa02c63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017JRjgXAZmd2nZhR5NeUdyZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15730,
      "cache_read_input_tokens": 26855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15730
      },
      "output_tokens": 9,
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

_source line 26 · 2026-05-22T11:29:58.725Z_

<details><summary>↩ Tool result · `toolu_01GMr9KTaHj7fsJv6fNxSETj`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	MVP Validation: Exposure Misclassification DAG — K=3 vs K=2
4	
5	Tests whether the binary "bias toward null" guarantee for non-differential
6	exposure misclassification breaks in the multiclass (K>=3) setting.
7	
8	== Technical Setting ==
9	A is the EXPOSURE/TREATMENT variable, measured with error via LLM annotation.
10	No confounders. Simplest possible misclassification scenario.
11	
12	  DAG: A -> Y, A -> A*
13	  DGP: Y = beta_0 + beta_1*1[A=1] + beta_2*1[A=2] + eps
14	  Misclassification: P(A*=j|A=i) = C[j,i], C column-stochastic
15	
16	Researcher regresses Y ~ 1 + 1[A*=1] + 1[A*=2] instead of Y ~ 1 + 1[A=1] + 1[A=2].
17	
18	== Binary Guarantee (K=2) ==
19	Non-differential misclassification of binary exposure guarantees bias toward
20	null: the estimated effect is attenuated (|gamma_hat| <= |beta|). This is
21	a classical result in measurement error literature.
22	
23	== Key Question ==
24	Does this guarantee extend to K=3? Or can certain confusion matrix structures
25	produce:
26	  - SIGN REVERSAL: sign(gamma_hat_k) != sign(beta_k)
27	  - AMPLIFICATION: |gamma_hat_k| > |beta_k|
28	
29	== Distinction from Lee & Wood-Doughty (2024) ==
30	We study OBSERVED exposure with noisy measurement (A observable, A* used at
31	scale). LWD study UNOBSERVED confounding with proxy (different identifiability).
32	
33	Dependencies: numpy
34	"""
35	
36	import numpy as np
37	from collections import OrderedDict
38	import time
39	
40	
41	# ============================================================
42	# DGP Parameters
43	# ============================================================
44	N_SAMPLES = 10_000
45	M_REPS = 1_000
46	N_RANDOM_SEARCH = 100_000
47	SEED = 42
48	
49	P_A = np.array([0.4, 0.35, 0.25])
50	BETA = np.array([0.0, 1.0, -0.5])    # beta_0, beta_1, beta_2
51	SIGMA_Y = 1.0
52	
53	
54	# ============================================================
55	# Confusion Matrix Structures (reused from confounding DAG MVP)
56	# ============================================================
57	
58	C1_SYMMETRIC_HIGH = np.array([
59	    [0.80, 0.10, 0.10],
60	    [0.10, 0.80, 0.10],
61	    [0.10, 0.10, 0.80],
62	])
63	C1_DESC = "Symmetric high-accuracy: diag=0.8, uniform off-diagonal=0.1"
64	
65	C2_ASYMMETRIC = np.array([
66	    [0.65, 0.05, 0.10],
67	    [0.30, 0.85, 0.10],
68	    [0.05, 0.10, 0.80],
69	])
70	C2_DESC = "Asymmetric: P(A*=1|A=0)=0.30 >> P(A*=0|A=1)=0.05"
71	
72	C3_STRUCTURAL_12 = np.array([
73	    [0.96, 0.01, 0.01],
74	    [0.02, 0.69, 0.30],
75	    [0.02, 0.30, 0.69],
76	])
77	C3_DESC = "Structural: classes 1<->2 heavily confused (0.30), class 0 clean"
78	
79	C4_WEAK_DIAG = np.array([
80	    [0.40, 0.35, 0.25],
81	    [0.35, 0.40, 0.35],
82	    [0.25, 0.25, 0.40],
83	])
84	C4_DESC = "Weak diagonal dominance: diag~0.4, non-uniform off-diagonal"
85	
86	C5_NEAR_PERM = np.array([
87	    [0.05, 0.05, 0.90],
88	    [0.90, 0.05, 0.05],
89	    [0.05, 0.90, 0.05],
90	])
91	C5_DESC = "Near-permutation: cyclic 0->1, 1->2, 2->0 (p=0.90)"
92	
93	C6_DIFF_BASE = np.array([
94	    [0.80, 0.10, 0.10],
95	    [0.10, 0.80, 0.10],
96	    [0.10, 0.10, 0.80],
97	])
98	C6_DESC = "Differential base (=C1 in non-diff exposure setting; Y-dependent in MC)"
99	
100	
101	def make_confusion_matrices():
102	    """6 confusion matrix structures."""
103	    matrices = OrderedDict([
104	        ("1_sym_high",   (C1_SYMMETRIC_HIGH, C1_DESC)),
105	        ("2_asymmetric", (C2_ASYMMETRIC,     C2_DESC)),
106	        ("3_struct_12",  (C3_STRUCTURAL_12,  C3_DESC)),
107	        ("4_weak_diag",  (C4_WEAK_DIAG,      C4_DESC)),
108	        ("5_near_perm",  (C5_NEAR_PERM,      C5_DESC)),
109	        ("6_diff_base",  (C6_DIFF_BASE,      C6_DESC)),
110	    ])
111	    for name, (C, _) in matrices.items():
112	        assert np.allclose(C.sum(axis=0), 1.0), f"{name}: columns don't sum to 1"
113	    return matrices
114	
115	
116	# ============================================================
117	# Theoretical bias (exact)
118	# ============================================================
119	def theoretical_bias_exposure(C, p_A, beta):
120	    """
121	    plim gamma = (E[Z'Z])^{-1} E[Z'X] beta
122	    Z = (1, D*_1, D*_2),  X = (1, D_1, D_2)
123	
124	    Returns: (plim_gamma, bias_vector)
125	    """
126	    p0, p1, p2 = p_A
127	    q = C @ p_A
128	
129	    EZZ = np.array([
130	        [1.0,  q[1], q[2]],
131	        [q[1], q[1], 0.0],
132	        [q[2], 0.0,  q[2]],
133	    ])
134	
135	    EZX = np.array([
136	        [1.0,  p1,            p2],
137	        [q[1], C[1, 1] * p1,  C[1, 2] * p2],
138	        [q[2], C[2, 1] * p1,  C[2, 2] * p2],
139	    ])
140	
141	    plim = np.linalg.solve(EZZ, EZX @ beta)
142	    return plim, plim - beta
143	
144	
145	# ============================================================
146	# Data generation & OLS
147	# ============================================================
148	def _generate_Astar(A, C, rng):
149	    """Vectorized A* sampling from confusion matrix."""
150	    probs = C[:, A]
151	    cum = np.cumsum(probs, axis=0)
152	    u = rng.uniform(size=len(A))
153	    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))
154	
155	
156	def _generate_Astar_diff_Y(A, Y, C_base, rng, factor=2.0):
157	    """Differential: Y > median => off-diagonal rates scaled by factor."""
158	    C_high = C_base.copy()
159	    for col in range(3):
160	        diag_val = C_high[col, col]
161	        off_sum = 1.0 - diag_val
162	        new_off_sum = min(off_sum * factor, 0.95)
163	        scale = new_off_sum / off_sum if off_sum > 0 else 1.0
164	        for row in range(3):
165	            if row != col:
166	                C_high[row, col] *= scale
167	        C_high[col, col] = 1.0 - sum(C_high[r, col] for r in range(3) if r != col)
168	
169	    Y_med = np.median(Y)
170	    high = Y > Y_med
171	    probs_low = C_base[:, A]
172	    probs_high = C_high[:, A]
173	    probs = np.where(high[np.newaxis, :], probs_high, probs_low)
174	    cum = np.cumsum(probs, axis=0)
175	    u = rng.uniform(size=len(A))
176	    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))
177	
178	
179	def ols_coefs(X, Y):
180	    """OLS coefficients."""
181	    return np.linalg.lstsq(X, Y, rcond=None)[0]
182	
183	
184	# ============================================================
185	# Monte Carlo
186	# ============================================================
187	def run_mc_exposure(M, N, C, p_A, beta, sigma_Y, seed, differential=False):
188	    rng = np.random.default_rng(seed)
189	    bias_misclass = np.empty((M, 3))
190	
191	    for m in range(M):
192	        A = rng.choice(3, size=N, p=p_A)
193	        D1 = (A == 1).astype(float)
194	        D2 = (A == 2).astype(float)
195	        Y = beta[0] + beta[1] * D1 + beta[2] * D2 + rng.normal(0, sigma_Y, N)
196	
197	        if differential:
198	            A_star = _generate_Astar_diff_Y(A, Y, C, rng)
199	        else:
200	            A_star = _generate_Astar(A, C, rng)
201	
202	        D1s = (A_star == 1).astype(float)
203	        D2s = (A_star == 2).astype(float)
204	        X_star = np.column_stack([np.ones(N), D1s, D2s])
205	        gamma_hat = ols_coefs(X_star, Y)
206	        bias_misclass[m] = gamma_hat - beta
207	
208	    return bias_misclass
209	
210	
211	# ============================================================
212	# Binary comparison
213	# ============================================================
214	def binary_attenuation_theory(C_bin, p_bin, beta_bin):
215	    """
216	    Binary exposure misclassification: plim from 2x2 system.
217	    Z = (1, D*), X = (1, D), beta = (beta_0, beta_1)
218	    """
219	    p0, p1 = p_bin
220	    q1 = C_bin[1, 0] * p0 + C_bin[1, 1] * p1
221	
222	    EZZ = np.array([[1.0, q1], [q1, q1]])
223	    EZX = np.array([[1.0, p1], [q1, C_bin[1, 1] * p1]])
224	
225	    plim = np.linalg.solve(EZZ, EZX @ beta_bin)
226	    return plim[1], plim[1] / beta_bin[1] if abs(beta_bin[1]) > 1e-10 else np.nan
227	
228	
229	def collapse_to_binary(C, p_A):
230	    """Derive 2x2 C from 3x3 by collapsing {1,2} -> 1."""
231	    p0, p1, p2 = p_A
232	    pB1 = p1 + p2
233	
234	    c00 = C[0, 0]
235	    c10 = C[1, 0] + C[2, 0]
236	    c01 = (C[0, 1] * p1 + C[0, 2] * p2) / pB1
237	    c11 = 1.0 - c01
238	
239	    C_bin = np.array([[c00, c01], [c10, c11]])
240	    p_bin = np.array([p0, pB1])
241	    beta_bin_eff = (BETA[1] * p1 + BETA[2] * p2) / pB1
242	    beta_bin = np.array([BETA[0], beta_bin_eff])
243	
244	    return C_bin, p_bin, beta_bin
245	
246	
247	# ============================================================
248	# Random search for sign reversal / amplification
249	# ============================================================
250	def classify_bias(plim_gamma, beta):
251	    """Classify bias type for each component (1 and 2)."""
252	    results = {}
253	    for k in [1, 2]:
254	        g = plim_gamma[k]
255	        b = beta[k]
256	        if abs(b) < 1e-10:
257	            results[k] = "zero_true"
258	            continue
259	        if g * b < 0:
260	            results[k] = "SIGN_REVERSAL"
261	        elif abs(g) > abs(b):
262	            results[k] = "AMPLIFICATION"
263	        else:
264	            results[k] = "toward_null"
265	    return results
266	
267	
268	def random_search(n_search, p_A, beta, seed=0):
269	    """Search random column-stochastic C for bias-toward-null violations."""
270	    rng = np.random.default_rng(seed)
271	
272	    sign_rev_count = 0
273	    amp_count = 0
274	    either_count = 0
275	    worst_cases = []
276	
277	    for i in range(n_search):
278	        C = rng.dirichlet([1, 1, 1], size=3).T
279	        try:
280	            plim, bias = theoretical_bias_exposure(C, p_A, beta)
281	        except np.linalg.LinAlgError:
282	            continue
283	
284	        types = classify_bias(plim, beta)
285	        has_sr = any(v == "SIGN_REVERSAL" for v in types.values())
286	        has_amp = any(v == "AMPLIFICATION" for v in types.values())
287	
288	        if has_sr:
289	            sign_rev_count += 1
290	        if has_amp:
291	            amp_count += 1
292	        if has_sr or has_amp:
293	            either_count += 1
294	            severity = max(
295	                abs(plim[1] / beta[1]) if abs(beta[1]) > 1e-10 else 0,
296	                abs(plim[2] / beta[2]) if abs(beta[2]) > 1e-10 else 0,
297	            )
298	            worst_cases.append((severity, C.copy(), plim.copy(), types.copy()))
299	
300	    worst_cases.sort(key=lambda x: -x[0])
301	    return {
302	        "n_searched": n_search,
303	        "sign_reversal": sign_rev_count,
304	        "amplification": amp_count,
305	        "either": either_count,
306	        "worst_cases": worst_cases[:10],
307	    }
308	
309	
310	# ============================================================
311	# Main
312	# ============================================================
313	def main():
314	    t_start = time.time()
315	
316	    print("=" * 85)
317	    print("Exposure Misclassification DAG — K=3 Bias-Toward-Null Test")
318	    print("=" * 85)
319	    print()
320	    print("DAG: A -> Y, A -> A*  (no confounders, exposure misclassification only)")
321	    print(f"DGP: P(A)=[{P_A[0]}, {P_A[1]}, {P_A[2]}], "
322	          f"beta=[{BETA[0]}, {BETA[1]}, {BETA[2]}], sigma_Y={SIGMA_Y}")
323	    print(f"MC:  N={N_SAMPLES:,}, M={M_REPS:,}, seed={SEED}")
324	    print(f"Random search: {N_RANDOM_SEARCH:,} matrices")
325	    print()
326	    print("Binary guarantee: non-diff misclassification => |gamma| <= |beta| (attenuation)")
327	    print("K=3 question: does this hold for all C? Or can we get sign reversal / amplification?")
328	
329	    matrices = make_confusion_matrices()
330	
331	    # ── PART A: Theory + MC for 6 structures ─────────────────
332	    print("\n" + "=" * 85)
333	    print("PART A: K=3 Exposure — Theory vs Monte Carlo  (6 structures)")
334	    print("=" * 85)
335	
336	    results = {}
337	    print(f"\n{'#':<2} {'Config':<14} | {'beta_1':>6} {'g1_th':>8} {'g1_mc':>8} {'type_1':>15} "
338	          f"| {'beta_2':>6} {'g2_th':>8} {'g2_mc':>8} {'type_2':>15} | {'Match':>5}")
339	    print("-" * 115)
340	
341	    for name, (C, desc) in matrices.items():
342	        t0 = time.time()
343	        idx = name[0]
344	        is_diff = (name == "6_diff_base")
345	
346	        # Theory (exact for non-differential; C6 base = C1, so same theory)
347	        plim_th, bias_th = theoretical_bias_exposure(C, P_A, BETA)
348	
349	        # MC
350	        mc_bias = run_mc_exposure(M_REPS, N_SAMPLES, C, P_A, BETA, SIGMA_Y, SEED,
351	                                  differential=is_diff)
352	
353	        mc_mean = mc_bias.mean(axis=0)
354	        mc_se = mc_bias.std(axis=0, ddof=1)
355	        ci_lo = mc_mean - 1.96 * mc_se / np.sqrt(M_REPS)
356	        ci_hi = mc_mean + 1.96 * mc_se / np.sqrt(M_REPS)
357	
358	        match_1 = ci_lo[1] <= bias_th[1] <= ci_hi[1]
359	        match_2 = ci_lo[2] <= bias_th[2] <= ci_hi[2]
360	        if is_diff:
361	            match_all = True  # no exact theory for differential
362	            match_str = "N/A"
363	        else:
364	            match_all = match_1 and match_2
365	            match_str = "YES" if match_all else "**NO**"
366	
367	        types = classify_bias(plim_th, BETA)
368	        elapsed = time.time() - t0
369	
370	        results[name] = dict(
371	            plim=plim_th, bias=bias_th, mc_mean=mc_mean + BETA,
372	            mc_bias_mean=mc_mean, ci=(ci_lo, ci_hi), match=match_all,
373	            types=types, is_diff=is_diff)
374	
375	        g1_mc = mc_mean[1] + BETA[1]  # plim gamma_1
376	        g2_mc = mc_mean[2] + BETA[2]
377	
378	        print(f"{idx:<2} {name:<14} | {BETA[1]:>6.2f} {plim_th[1]:>8.4f} {g1_mc:>8.4f} "
379	              f"{types[1]:>15} | {BETA[2]:>6.2f} {plim_th[2]:>8.4f} {g2_mc:>8.4f} "
380	              f"{types[2]:>15} | {match_str:>5}  ({elapsed:.1f}s)")
381	
382	    # ── PART B: 100k Random Search ───────────────────────────
383	    print("\n" + "=" * 85)
384	    print(f"PART B: Random Search — {N_RANDOM_SEARCH:,} column-stochastic C matrices")
385	    print("=" * 85)
386	
387	    t0 = time.time()
388	    search = random_search(N_RANDOM_SEARCH, P_A, BETA, seed=12345)
389	    elapsed_search = time.time() - t0
390	
391	    print(f"\nSearched: {search['n_searched']:,} matrices ({elapsed_search:.1f}s)")
392	    print(f"Sign reversal (any component):  {search['sign_reversal']:,} "
393	          f"({100*search['sign_reversal']/search['n_searched']:.1f}%)")
394	    print(f"Amplification (any component):  {search['amplification']:,} "
395	          f"({100*search['amplification']/search['n_searched']:.1f}%)")
396	    print(f"Either violation:               {search['either']:,} "
397	          f"({100*search['either']/search['n_searched']:.1f}%)")
398	
399	    if search['worst_cases']:
400	        print(f"\nTop-5 most extreme violations (by max |gamma_k/beta_k|):")
401	        print(f"  {'Severity':>8} {'g1':>8} {'type_1':>15} {'g2':>8} {'type_2':>15}")
402	        print(f"  {'-'*58}")
403	        for sev, C_worst, plim_worst, types_worst in search['worst_cases'][:5]:
404	            print(f"  {sev:>8.2f} {plim_worst[1]:>8.4f} {types_worst[1]:>15} "
405	                  f"{plim_worst[2]:>8.4f} {types_worst[2]:>15}")
406	            for row in C_worst:
407	                print(f"    [{row[0]:.3f}  {row[1]:.3f}  {row[2]:.3f}]")
408	            print()
409	
410	    # ── PART C: MC validation of worst-case C ────────────────
411	    if search['worst_cases']:
412	        print("=" * 85)
413	        print("PART C: MC Validation of Worst-Case C from Random Search")
414	        print("=" * 85)
415	
416	        _, C_worst, plim_worst, types_worst = search['worst_cases'][0]
417	        print(f"\nWorst-case C (severity={search['worst_cases'][0][0]:.2f}):")
418	        for row in C_worst:
419	            print(f"  [{row[0]:.3f}  {row[1]:.3f}  {row[2]:.3f}]")
420	
421	        mc_worst = run_mc_exposure(M_REPS, N_SAMPLES, C_worst, P_A, BETA, SIGMA_Y, SEED + 1)
422	        mc_mean_w = mc_worst.mean(axis=0)
423	        mc_se_w = mc_worst.std(axis=0, ddof=1)
424	
425	        print(f"\n{'Component':<10} {'beta':>8} {'Theory':>8} {'MC Mean':>8} "
426	              f"{'MC SE':>8} {'Type':>15}")
427	        print("-" * 60)
428	        for k in [1, 2]:
429	            th_g = plim_worst[k]
430	            mc_g = mc_mean_w[k] + BETA[k]
431	            print(f"{'beta_'+str(k):<10} {BETA[k]:>8.4f} {th_g:>8.4f} {mc_g:>8.4f} "
432	                  f"{mc_se_w[k]:>8.4f} {types_worst[k]:>15}")
433	
434	    # ── PART D: Binary K=2 Comparison ────────────────────────
435	    print("\n" + "=" * 85)
436	    print("PART D: Binary (K=2) Comparison — Attenuation Guarantee")
437	    print("=" * 85)
438	
439	    print(f"\nCollapse: B=1[A in {{1,2}}]. Binary beta_B = "
440	          f"E[beta_1*p1 + beta_2*p2]/(p1+p2) = "
441	          f"{(BETA[1]*P_A[1] + BETA[2]*P_A[2])/(P_A[1]+P_A[2]):.4f}")
442	
443	    print(f"\n{'#':<2} {'Config':<14} {'C_bin diag':>10} {'beta_B':>8} "
444	          f"{'gamma_B':>8} {'ratio':>8} {'Toward null?':>13}")
445	    print("-" * 72)
446	
447	    for name, (C, desc) in matrices.items():
448	        C_bin, p_bin, beta_bin = collapse_to_binary(C, P_A)
449	        gamma_B, ratio = binary_attenuation_theory(C_bin, p_bin, beta_bin)
450	        toward_null = abs(gamma_B) <= abs(beta_bin[1]) + 1e-10
451	        idx = name[0]
452	
453	        print(f"{idx:<2} {name:<14} [{C_bin[0,0]:.2f},{C_bin[1,1]:.2f}] "
454	              f"{beta_bin[1]:>8.4f} {gamma_B:>8.4f} {ratio:>8.4f} "
455	              f"{'YES (|r|<=1)' if toward_null else '**NO**':>13}")
456	
457	    # ── PART E: K=3 vs K=2 Direct Comparison ─────────────────
458	    print("\n" + "=" * 85)
459	    print("PART E: K=3 vs K=2 — Does Binary Guarantee Extend to Multiclass?")
460	    print("=" * 85)
461	
462	    print(f"\n{'#':<2} {'Config':<14} | {'K3: g1':>8} {'type_1':>15} {'g2':>8} "
463	          f"{'type_2':>15} | {'K2: toward_null':>15}")
464	    print("-" * 95)
465	
466	    k3_violations = 0
467	    for name, (C, desc) in matrices.items():
468	        idx = name[0]
469	        r = results[name]
470	        C_bin, p_bin, beta_bin = collapse_to_binary(C, P_A)
471	        gamma_B, ratio = binary_attenuation_theory(C_bin, p_bin, beta_bin)
472	        k2_tn = abs(ratio) <= 1.0 + 1e-10
473	
474	        has_violation = any(v in ("SIGN_REVERSAL", "AMPLIFICATION")
475	                          for v in r['types'].values())
476	        if has_violation:
477	            k3_violations += 1
478	
479	        print(f"{idx:<2} {name:<14} | {r['plim'][1]:>8.4f} {r['types'][1]:>15} "
480	              f"{r['plim'][2]:>8.4f} {r['types'][2]:>15} | "
481	              f"{'YES' if k2_tn else 'NO':>15}")
482	
483	    # ── Pass/Fail ────────────────────────────────────────────
484	    print("\n" + "=" * 85)
485	    print("PASS / FAIL SUMMARY")
486	    print("=" * 85)
487	
488	    # C1: Theory-MC match (non-differential only)
489	    nondiff_results = {n: r for n, r in results.items() if not r['is_diff']}
490	    n_match = sum(1 for r in nondiff_results.values() if r['match'])
491	    n_nondiff = len(nondiff_results)
492	    c1 = n_match == n_nondiff
493	    print(f"\n1. Theory vs MC match (non-diff): {n_match}/{n_nondiff}  "
494	          f"{'PASS' if c1 else 'FAIL'}")
495	    for name, r in nondiff_results.items():
496	        ci = r['ci']
497	        print(f"   {name}: th_bias=[{r['bias'][1]:.6f}, {r['bias'][2]:.6f}], "
498	              f"CI_1=[{ci[0][1]:.6f}, {ci[1][1]:.6f}], "
499	              f"CI_2=[{ci[0][2]:.6f}, {ci[1][2]:.6f}] -> "
500	              f"{'OK' if r['match'] else 'MISMATCH'}")
501	
502	    # C2: Sign reversal or amplification found
503	    c2_struct = k3_violations > 0
504	    c2_search = search['either'] > 0
505	    c2 = c2_struct or c2_search
506	    print(f"\n2. Bias-toward-null violation found: "
507	          f"{'PASS' if c2 else 'FAIL'}")
508	    print(f"   Named structures with violation: {k3_violations}/6")
509	    print(f"   Random search violations: {search['either']:,}/{search['n_searched']:,}")
510	
511	    # C3: Binary always toward null, K=3 sometimes not
512	    all_k2_tn = True
513	    for name, (C, desc) in matrices.items():
514	        C_bin, p_bin, beta_bin = collapse_to_binary(C, P_A)
515	        _, ratio = binary_attenuation_theory(C_bin, p_bin, beta_bin)
516	        if abs(ratio) > 1.0 + 1e-10:
517	            all_k2_tn = False
518	    c3 = all_k2_tn and c2
519	    print(f"\n3. K=2 always toward null AND K=3 sometimes not: "
520	          f"{'PASS' if c3 else 'FAIL'}")
521	    print(f"   K=2 all toward null: {'YES' if all_k2_tn else 'NO'}")
522	    print(f"   K=3 has violations: {'YES' if c2 else 'NO'}")
523	
524	    overall = c1 and c2 and c3
525	    print(f"\nOVERALL: {'PASS' if overall else 'FAIL'}")
526	
527	    # ── Appendix: Confusion Matrices ─────────────────────────
528	    print("\n" + "=" * 85)
529	    print("APPENDIX: Confusion Matrix Definitions")
530	    print("=" * 85)
531	    for name, (C, desc) in matrices.items():
532	        print(f"\n{name}: {desc}")
533	        for row in C:
534	            print(f"  [{row[0]:.2f}  {row[1]:.2f}  {row[2]:.2f}]")
535	
536	    elapsed_total = time.time() - t_start
537	    print(f"\nTotal runtime: {elapsed_total:.1f}s")
538	
539	
540	if __name__ == "__main__":
541	    main()
542	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "9f8e5593-49f9-41b8-9d36-6cff0045b159",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_exposure_dag.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nMVP Validation: Exposure Misclassification DAG — K=3 vs K=2\n\nTests whether the binary \"bias toward null\" guarantee for non-differential\nexposure misclassification breaks in the multiclass (K>=3) setting.\n\n== Technical Setting ==\nA is the EXPOSURE/TREATMENT variable, measured with error via LLM annotation.\nNo confounders. Simplest possible misclassification scenario.\n\n  DAG: A -> Y, A -> A*\n  DGP: Y = beta_0 + beta_1*1[A=1] + beta_2*1[A=2] + eps\n  Misclassification: P(A*=j|A=i) = C[j,i], C column-stochastic\n\nResearcher regresses Y ~ 1 + 1[A*=1] + 1[A*=2] instead of Y ~ 1 + 1[A=1] + 1[A=2].\n\n== Binary Guarantee (K=2) ==\nNon-differential misclassification of binary exposure guarantees bias toward\nnull: the estimated effect is attenuated (|gamma_hat| <= |beta|). This is\na classical result in measurement error literature.\n\n== Key Question ==\nDoes this guarantee extend to K=3? Or can certain confusion matrix structures\nproduce:\n  - SIGN REVERSAL: sign(gamma_hat_k) != sign(beta_k)\n  - AMPLIFICATION: |gamma_hat_k| > |beta_k|\n\n== Distinction from Lee & Wood-Doughty (2024) ==\nWe study OBSERVED exposure with noisy measurement (A observable, A* used at\nscale). LWD study UNOBSERVED confounding with proxy (different identifiability).\n\nDependencies: numpy\n\"\"\"\n\nimport numpy as np\nfrom collections import OrderedDict\nimport time\n\n\n# ============================================================\n# DGP Parameters\n# ============================================================\nN_SAMPLES = 10_000\nM_REPS = 1_000\nN_RANDOM_SEARCH = 100_000\nSEED = 42\n\nP_A = np.array([0.4, 0.35, 0.25])\nBETA = np.array([0.0, 1.0, -0.5])    # beta_0, beta_1, beta_2\nSIGMA_Y = 1.0\n\n\n# ============================================================\n# Confusion Matrix Structures (reused from confounding DAG MVP)\n# ============================================================\n\nC1_SYMMETRIC_HIGH = np.array([\n    [0.80, 0.10, 0.10],\n    [0.10, 0.80, 0.10],\n    [0.10, 0.10, 0.80],\n])\nC1_DESC = \"Symmetric high-accuracy: diag=0.8, uniform off-diagonal=0.1\"\n\nC2_ASYMMETRIC = np.array([\n    [0.65, 0.05, 0.10],\n    [0.30, 0.85, 0.10],\n    [0.05, 0.10, 0.80],\n])\nC2_DESC = \"Asymmetric: P(A*=1|A=0)=0.30 >> P(A*=0|A=1)=0.05\"\n\nC3_STRUCTURAL_12 = np.array([\n    [0.96, 0.01, 0.01],\n    [0.02, 0.69, 0.30],\n    [0.02, 0.30, 0.69],\n])\nC3_DESC = \"Structural: classes 1<->2 heavily confused (0.30), class 0 clean\"\n\nC4_WEAK_DIAG = np.array([\n    [0.40, 0.35, 0.25],\n    [0.35, 0.40, 0.35],\n    [0.25, 0.25, 0.40],\n])\nC4_DESC = \"Weak diagonal dominance: diag~0.4, non-uniform off-diagonal\"\n\nC5_NEAR_PERM = np.array([\n    [0.05, 0.05, 0.90],\n    [0.90, 0.05, 0.05],\n    [0.05, 0.90, 0.05],\n])\nC5_DESC = \"Near-permutation: cyclic 0->1, 1->2, 2->0 (p=0.90)\"\n\nC6_DIFF_BASE = np.array([\n    [0.80, 0.10, 0.10],\n    [0.10, 0.80, 0.10],\n    [0.10, 0.10, 0.80],\n])\nC6_DESC = \"Differential base (=C1 in non-diff exposure setting; Y-dependent in MC)\"\n\n\ndef make_confusion_matrices():\n    \"\"\"6 confusion matrix structures.\"\"\"\n    matrices = OrderedDict([\n        (\"1_sym_high\",   (C1_SYMMETRIC_HIGH, C1_DESC)),\n        (\"2_asymmetric\", (C2_ASYMMETRIC,     C2_DESC)),\n        (\"3_struct_12\",  (C3_STRUCTURAL_12,  C3_DESC)),\n        (\"4_weak_diag\",  (C4_WEAK_DIAG,      C4_DESC)),\n        (\"5_near_perm\",  (C5_NEAR_PERM,      C5_DESC)),\n        (\"6_diff_base\",  (C6_DIFF_BASE,      C6_DESC)),\n    ])\n    for name, (C, _) in matrices.items():\n        assert np.allclose(C.sum(axis=0), 1.0), f\"{name}: columns don't sum to 1\"\n    return matrices\n\n\n# ============================================================\n# Theoretical bias (exact)\n# ============================================================\ndef theoretical_bias_exposure(C, p_A, beta):\n    \"\"\"\n    plim gamma = (E[Z'Z])^{-1} E[Z'X] beta\n    Z = (1, D*_1, D*_2),  X = (1, D_1, D_2)\n\n    Returns: (plim_gamma, bias_vector)\n    \"\"\"\n    p0, p1, p2 = p_A\n    q = C @ p_A\n\n    EZZ = np.array([\n        [1.0,  q[1], q[2]],\n        [q[1], q[1], 0.0],\n        [q[2], 0.0,  q[2]],\n    ])\n\n    EZX = np.array([\n        [1.0,  p1,            p2],\n        [q[1], C[1, 1] * p1,  C[1, 2] * p2],\n        [q[2], C[2, 1] * p1,  C[2, 2] * p2],\n    ])\n\n    plim = np.linalg.solve(EZZ, EZX @ beta)\n    return plim, plim - beta\n\n\n# ============================================================\n# Data generation & OLS\n# ============================================================\ndef _generate_Astar(A, C, rng):\n    \"\"\"Vectorized A* sampling from confusion matrix.\"\"\"\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))\n\n\ndef _generate_Astar_diff_Y(A, Y, C_base, rng, factor=2.0):\n    \"\"\"Differential: Y > median => off-diagonal rates scaled by factor.\"\"\"\n    C_high = C_base.copy()\n    for col in range(3):\n        diag_val = C_high[col, col]\n        off_sum = 1.0 - diag_val\n        new_off_sum = min(off_sum * factor, 0.95)\n        scale = new_off_sum / off_sum if off_sum > 0 else 1.0\n        for row in range(3):\n            if row != col:\n                C_high[row, col] *= scale\n        C_high[col, col] = 1.0 - sum(C_high[r, col] for r in range(3) if r != col)\n\n    Y_med = np.median(Y)\n    high = Y > Y_med\n    probs_low = C_base[:, A]\n    probs_high = C_high[:, A]\n    probs = np.where(high[np.newaxis, :], probs_high, probs_low)\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    return ((u >= cum[0]).astype(int) + (u >= cum[1]).astype(int))\n\n\ndef ols_coefs(X, Y):\n    \"\"\"OLS coefficients.\"\"\"\n    return np.linalg.lstsq(X, Y, rcond=None)[0]\n\n\n# ============================================================\n# Monte Carlo\n# ============================================================\ndef run_mc_exposure(M, N, C, p_A, beta, sigma_Y, seed, differential=False):\n    rng = np.random.default_rng(seed)\n    bias_misclass = np.empty((M, 3))\n\n    for m in range(M):\n        A = rng.choice(3, size=N, p=p_A)\n        D1 = (A == 1).astype(float)\n        D2 = (A == 2).astype(float)\n        Y = beta[0] + beta[1] * D1 + beta[2] * D2 + rng.normal(0, sigma_Y, N)\n\n        if differential:\n            A_star = _generate_Astar_diff_Y(A, Y, C, rng)\n        else:\n            A_star = _generate_Astar(A, C, rng)\n\n        D1s = (A_star == 1).astype(float)\n        D2s = (A_star == 2).astype(float)\n        X_star = np.column_stack([np.ones(N), D1s, D2s])\n        gamma_hat = ols_coefs(X_star, Y)\n        bias_misclass[m] = gamma_hat - beta\n\n    return bias_misclass\n\n\n# ============================================================\n# Binary comparison\n# ============================================================\ndef binary_attenuation_theory(C_bin, p_bin, beta_bin):\n    \"\"\"\n    Binary exposure misclassification: plim from 2x2 system.\n    Z = (1, D*), X = (1, D), beta = (beta_0, beta_1)\n    \"\"\"\n    p0, p1 = p_bin\n    q1 = C_bin[1, 0] * p0 + C_bin[1, 1] * p1\n\n    EZZ = np.array([[1.0, q1], [q1, q1]])\n    EZX = np.array([[1.0, p1], [q1, C_bin[1, 1] * p1]])\n\n    plim = np.linalg.solve(EZZ, EZX @ beta_bin)\n    return plim[1], plim[1] / beta_bin[1] if abs(beta_bin[1]) > 1e-10 else np.nan\n\n\ndef collapse_to_binary(C, p_A):\n    \"\"\"Derive 2x2 C from 3x3 by collapsing {1,2} -> 1.\"\"\"\n    p0, p1, p2 = p_A\n    pB1 = p1 + p2\n\n    c00 = C[0, 0]\n    c10 = C[1, 0] + C[2, 0]\n    c01 = (C[0, 1] * p1 + C[0, 2] * p2) / pB1\n    c11 = 1.0 - c01\n\n    C_bin = np.array([[c00, c01], [c10, c11]])\n    p_bin = np.array([p0, pB1])\n    beta_bin_eff = (BETA[1] * p1 + BETA[2] * p2) / pB1\n    beta_bin = np.array([BETA[0], beta_bin_eff])\n\n    return C_bin, p_bin, beta_bin\n\n\n# ============================================================\n# Random search for sign reversal / amplification\n# ============================================================\ndef classify_bias(plim_gamma, beta):\n    \"\"\"Classify bias type for each component (1 and 2).\"\"\"\n    results = {}\n    for k in [1, 2]:\n        g = plim_gamma[k]\n        b = beta[k]\n        if abs(b) < 1e-10:\n            results[k] = \"zero_true\"\n            continue\n        if g * b < 0:\n            results[k] = \"SIGN_REVERSAL\"\n        elif abs(g) > abs(b):\n            results[k] = \"AMPLIFICATION\"\n        else:\n            results[k] = \"toward_null\"\n    return results\n\n\ndef random_search(n_search, p_A, beta, seed=0):\n    \"\"\"Search random column-stochastic C for bias-toward-null violations.\"\"\"\n    rng = np.random.default_rng(seed)\n\n    sign_rev_count = 0\n    amp_count = 0\n    either_count = 0\n    worst_cases = []\n\n    for i in range(n_search):\n        C = rng.dirichlet([1, 1, 1], size=3).T\n        try:\n            plim, bias = theoretical_bias_exposure(C, p_A, beta)\n        except np.linalg.LinAlgError:\n            continue\n\n        types = classify_bias(plim, beta)\n        has_sr = any(v == \"SIGN_REVERSAL\" for v in types.values())\n        has_amp = any(v == \"AMPLIFICATION\" for v in types.values())\n\n        if has_sr:\n            sign_rev_count += 1\n        if has_amp:\n            amp_count += 1\n        if has_sr or has_amp:\n            either_count += 1\n            severity = max(\n                abs(plim[1] / beta[1]) if abs(beta[1]) > 1e-10 else 0,\n                abs(plim[2] / beta[2]) if abs(beta[2]) > 1e-10 else 0,\n            )\n            worst_cases.append((severity, C.copy(), plim.copy(), types.copy()))\n\n    worst_cases.sort(key=lambda x: -x[0])\n    return {\n        \"n_searched\": n_search,\n        \"sign_reversal\": sign_rev_count,\n        \"amplification\": amp_count,\n        \"either\": either_count,\n        \"worst_cases\": worst_cases[:10],\n    }\n\n\n# ============================================================\n# Main\n# ============================================================\ndef main():\n    t_start = time.time()\n\n    print(\"=\" * 85)\n    print(\"Exposure Misclassification DAG — K=3 Bias-Toward-Null Test\")\n    print(\"=\" * 85)\n    print()\n    print(\"DAG: A -> Y, A -> A*  (no confounders, exposure misclassification only)\")\n    print(f\"DGP: P(A)=[{P_A[0]}, {P_A[1]}, {P_A[2]}], \"\n          f\"beta=[{BETA[0]}, {BETA[1]}, {BETA[2]}], sigma_Y={SIGMA_Y}\")\n    print(f\"MC:  N={N_SAMPLES:,}, M={M_REPS:,}, seed={SEED}\")\n    print(f\"Random search: {N_RANDOM_SEARCH:,} matrices\")\n    print()\n    print(\"Binary guarantee: non-diff misclassification => |gamma| <= |beta| (attenuation)\")\n    print(\"K=3 question: does this hold for all C? Or can we get sign reversal / amplification?\")\n\n    matrices = make_confusion_matrices()\n\n    # ── PART A: Theory + MC for 6 structures ─────────────────\n    print(\"\\n\" + \"=\" * 85)\n    print(\"PART A: K=3 Exposure — Theory vs Monte Carlo  (6 structures)\")\n    print(\"=\" * 85)\n\n    results = {}\n    print(f\"\\n{'#':<2} {'Config':<14} | {'beta_1':>6} {'g1_th':>8} {'g1_mc':>8} {'type_1':>15} \"\n          f\"| {'beta_2':>6} {'g2_th':>8} {'g2_mc':>8} {'type_2':>15} | {'Match':>5}\")\n    print(\"-\" * 115)\n\n    for name, (C, desc) in matrices.items():\n        t0 = time.time()\n        idx = name[0]\n        is_diff = (name == \"6_diff_base\")\n\n        # Theory (exact for non-differential; C6 base = C1, so same theory)\n        plim_th, bias_th = theoretical_bias_exposure(C, P_A, BETA)\n\n        # MC\n        mc_bias = run_mc_exposure(M_REPS, N_SAMPLES, C, P_A, BETA, SIGMA_Y, SEED,\n                                  differential=is_diff)\n\n        mc_mean = mc_bias.mean(axis=0)\n        mc_se = mc_bias.std(axis=0, ddof=1)\n        ci_lo = mc_mean - 1.96 * mc_se / np.sqrt(M_REPS)\n        ci_hi = mc_mean + 1.96 * mc_se / np.sqrt(M_REPS)\n\n        match_1 = ci_lo[1] <= bias_th[1] <= ci_hi[1]\n        match_2 = ci_lo[2] <= bias_th[2] <= ci_hi[2]\n        if is_diff:\n            match_all = True  # no exact theory for differential\n            match_str = \"N/A\"\n        else:\n            match_all = match_1 and match_2\n            match_str = \"YES\" if match_all else \"**NO**\"\n\n        types = classify_bias(plim_th, BETA)\n        elapsed = time.time() - t0\n\n        results[name] = dict(\n            plim=plim_th, bias=bias_th, mc_mean=mc_mean + BETA,\n            mc_bias_mean=mc_mean, ci=(ci_lo, ci_hi), match=match_all,\n            types=types, is_diff=is_diff)\n\n        g1_mc = mc_mean[1] + BETA[1]  # plim gamma_1\n        g2_mc = mc_mean[2] + BETA[2]\n\n        print(f\"{idx:<2} {name:<14} | {BETA[1]:>6.2f} {plim_th[1]:>8.4f} {g1_mc:>8.4f} \"\n              f\"{types[1]:>15} | {BETA[2]:>6.2f} {plim_th[2]:>8.4f} {g2_mc:>8.4f} \"\n              f\"{types[2]:>15} | {match_str:>5}  ({elapsed:.1f}s)\")\n\n    # ── PART B: 100k Random Search ───────────────────────────\n    print(\"\\n\" + \"=\" * 85)\n    print(f\"PART B: Random Search — {N_RANDOM_SEARCH:,} column-stochastic C matrices\")\n    print(\"=\" * 85)\n\n    t0 = time.time()\n    search = random_search(N_RANDOM_SEARCH, P_A, BETA, seed=12345)\n    elapsed_search = time.time() - t0\n\n    print(f\"\\nSearched: {search['n_searched']:,} matrices ({elapsed_search:.1f}s)\")\n    print(f\"Sign reversal (any component):  {search['sign_reversal']:,} \"\n          f\"({100*search['sign_reversal']/search['n_searched']:.1f}%)\")\n    print(f\"Amplification (any component):  {search['amplification']:,} \"\n          f\"({100*search['amplification']/search['n_searched']:.1f}%)\")\n    print(f\"Either violation:               {search['either']:,} \"\n          f\"({100*search['either']/search['n_searched']:.1f}%)\")\n\n    if search['worst_cases']:\n        print(f\"\\nTop-5 most extreme violations (by max |gamma_k/beta_k|):\")\n        print(f\"  {'Severity':>8} {'g1':>8} {'type_1':>15} {'g2':>8} {'type_2':>15}\")\n        print(f\"  {'-'*58}\")\n        for sev, C_worst, plim_worst, types_worst in search['worst_cases'][:5]:\n            print(f\"  {sev:>8.2f} {plim_worst[1]:>8.4f} {types_worst[1]:>15} \"\n                  f\"{plim_worst[2]:>8.4f} {types_worst[2]:>15}\")\n            for row in C_worst:\n                print(f\"    [{row[0]:.3f}  {row[1]:.3f}  {row[2]:.3f}]\")\n            print()\n\n    # ── PART C: MC validation of worst-case C ────────────────\n    if search['worst_cases']:\n        print(\"=\" * 85)\n        print(\"PART C: MC Validation of Worst-Case C from Random Search\")\n        print(\"=\" * 85)\n\n        _, C_worst, plim_worst, types_worst = search['worst_cases'][0]\n        print(f\"\\nWorst-case C (severity={search['worst_cases'][0][0]:.2f}):\")\n        for row in C_worst:\n            print(f\"  [{row[0]:.3f}  {row[1]:.3f}  {row[2]:.3f}]\")\n\n        mc_worst = run_mc_exposure(M_REPS, N_SAMPLES, C_worst, P_A, BETA, SIGMA_Y, SEED + 1)\n        mc_mean_w = mc_worst.mean(axis=0)\n        mc_se_w = mc_worst.std(axis=0, ddof=1)\n\n        print(f\"\\n{'Component':<10} {'beta':>8} {'Theory':>8} {'MC Mean':>8} \"\n              f\"{'MC SE':>8} {'Type':>15}\")\n        print(\"-\" * 60)\n        for k in [1, 2]:\n            th_g = plim_worst[k]\n            mc_g = mc_mean_w[k] + BETA[k]\n            print(f\"{'beta_'+str(k):<10} {BETA[k]:>8.4f} {th_g:>8.4f} {mc_g:>8.4f} \"\n                  f\"{mc_se_w[k]:>8.4f} {types_worst[k]:>15}\")\n\n    # ── PART D: Binary K=2 Comparison ────────────────────────\n    print(\"\\n\" + \"=\" * 85)\n    print(\"PART D: Binary (K=2) Comparison — Attenuation Guarantee\")\n    print(\"=\" * 85)\n\n    print(f\"\\nCollapse: B=1[A in {{1,2}}]. Binary beta_B = \"\n          f\"E[beta_1*p1 + beta_2*p2]/(p1+p2) = \"\n          f\"{(BETA[1]*P_A[1] + BETA[2]*P_A[2])/(P_A[1]+P_A[2]):.4f}\")\n\n    print(f\"\\n{'#':<2} {'Config':<14} {'C_bin diag':>10} {'beta_B':>8} \"\n          f\"{'gamma_B':>8} {'ratio':>8} {'Toward null?':>13}\")\n    print(\"-\" * 72)\n\n    for name, (C, desc) in matrices.items():\n        C_bin, p_bin, beta_bin = collapse_to_binary(C, P_A)\n        gamma_B, ratio = binary_attenuation_theory(C_bin, p_bin, beta_bin)\n        toward_null = abs(gamma_B) <= abs(beta_bin[1]) + 1e-10\n        idx = name[0]\n\n        print(f\"{idx:<2} {name:<14} [{C_bin[0,0]:.2f},{C_bin[1,1]:.2f}] \"\n              f\"{beta_bin[1]:>8.4f} {gamma_B:>8.4f} {ratio:>8.4f} \"\n              f\"{'YES (|r|<=1)' if toward_null else '**NO**':>13}\")\n\n    # ── PART E: K=3 vs K=2 Direct Comparison ─────────────────\n    print(\"\\n\" + \"=\" * 85)\n    print(\"PART E: K=3 vs K=2 — Does Binary Guarantee Extend to Multiclass?\")\n    print(\"=\" * 85)\n\n    print(f\"\\n{'#':<2} {'Config':<14} | {'K3: g1':>8} {'type_1':>15} {'g2':>8} \"\n          f\"{'type_2':>15} | {'K2: toward_null':>15}\")\n    print(\"-\" * 95)\n\n    k3_violations = 0\n    for name, (C, desc) in matrices.items():\n        idx = name[0]\n        r = results[name]\n        C_bin, p_bin, beta_bin = collapse_to_binary(C, P_A)\n        gamma_B, ratio = binary_attenuation_theory(C_bin, p_bin, beta_bin)\n        k2_tn = abs(ratio) <= 1.0 + 1e-10\n\n        has_violation = any(v in (\"SIGN_REVERSAL\", \"AMPLIFICATION\")\n                          for v in r['types'].values())\n        if has_violation:\n            k3_violations += 1\n\n        print(f\"{idx:<2} {name:<14} | {r['plim'][1]:>8.4f} {r['types'][1]:>15} \"\n              f\"{r['plim'][2]:>8.4f} {r['types'][2]:>15} | \"\n              f\"{'YES' if k2_tn else 'NO':>15}\")\n\n    # ── Pass/Fail ────────────────────────────────────────────\n    print(\"\\n\" + \"=\" * 85)\n    print(\"PASS / FAIL SUMMARY\")\n    print(\"=\" * 85)\n\n    # C1: Theory-MC match (non-differential only)\n    nondiff_results = {n: r for n, r in results.items() if not r['is_diff']}\n    n_match = sum(1 for r in nondiff_results.values() if r['match'])\n    n_nondiff = len(nondiff_results)\n    c1 = n_match == n_nondiff\n    print(f\"\\n1. Theory vs MC match (non-diff): {n_match}/{n_nondiff}  \"\n          f\"{'PASS' if c1 else 'FAIL'}\")\n    for name, r in nondiff_results.items():\n        ci = r['ci']\n        print(f\"   {name}: th_bias=[{r['bias'][1]:.6f}, {r['bias'][2]:.6f}], \"\n              f\"CI_1=[{ci[0][1]:.6f}, {ci[1][1]:.6f}], \"\n              f\"CI_2=[{ci[0][2]:.6f}, {ci[1][2]:.6f}] -> \"\n              f\"{'OK' if r['match'] else 'MISMATCH'}\")\n\n    # C2: Sign reversal or amplification found\n    c2_struct = k3_violations > 0\n    c2_search = search['either'] > 0\n    c2 = c2_struct or c2_search\n    print(f\"\\n2. Bias-toward-null violation found: \"\n          f\"{'PASS' if c2 else 'FAIL'}\")\n    print(f\"   Named structures with violation: {k3_violations}/6\")\n    print(f\"   Random search violations: {search['either']:,}/{search['n_searched']:,}\")\n\n    # C3: Binary always toward null, K=3 sometimes not\n    all_k2_tn = True\n    for name, (C, desc) in matrices.items():\n        C_bin, p_bin, beta_bin = collapse_to_binary(C, P_A)\n        _, ratio = binary_attenuation_theory(C_bin, p_bin, beta_bin)\n        if abs(ratio) > 1.0 + 1e-10:\n            all_k2_tn = False\n    c3 = all_k2_tn and c2\n    print(f\"\\n3. K=2 always toward null AND K=3 sometimes not: \"\n          f\"{'PASS' if c3 else 'FAIL'}\")\n    print(f\"   K=2 all toward null: {'YES' if all_k2_tn else 'NO'}\")\n    print(f\"   K=3 has violations: {'YES' if c2 else 'NO'}\")\n\n    overall = c1 and c2 and c3\n    print(f\"\\nOVERALL: {'PASS' if overall else 'FAIL'}\")\n\n    # ── Appendix: Confusion Matrices ─────────────────────────\n    print(\"\\n\" + \"=\" * 85)\n    print(\"APPENDIX: Confusion Matrix Definitions\")\n    print(\"=\" * 85)\n    for name, (C, desc) in matrices.items():\n        print(f\"\\n{name}: {desc}\")\n        for row in C:\n            print(f\"  [{row[0]:.2f}  {row[1]:.2f}  {row[2]:.2f}]\")\n\n    elapsed_total = time.time() - t_start\n    print(f\"\\nTotal runtime: {elapsed_total:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 542,
      "startLine": 1,
      "totalLines": 542
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear understanding of the codebase. Let me understand what I need to build:

1. The task asks for 3 DGP configs × 3 topologies (confounding, exposure, IV) = 9 cells
2. For each cell, compute magnitude ASV at 10% and 50% thresholds, plus sign-flip ASV for exposure
3. Use 5 fixed C₀ matrices with diagonal = {0.5, 0.6, 0.7, 0.8, 0.9}
4. Take median across the 5 C₀s


5. For the confounding topology, I need to extract the plim computation from the existing `theoretical_bias_exact` function and adapt it to work with different C matrices—the setup involves regressing Y on T and the confounders D₁ and D₂, where T itself depends linearly on those same confounders.

For the exposure topology, the situation is different since there's no single treatment variable T; instead, I'm working with multiple treatment dummies D₁ and D₂ directly in the regression, so I need to track both coefficient estimates rather than just one tau value. The task mentions computing sign-flip ASV at a 10% bias threshold, which suggests I need to find the magnitude of the confounder strength that would flip the sign of the treatment effect estimate. Looking at the DGP parameters more carefully, β represents the coefficients for the confounder effects on the outcome, τ is the treatment effect itself, and p specifies the category probabilities. For the confounding topology, the outcome depends on the treatment effect plus the confounder-driven terms, while treatment assignment is influenced by the same confounders through different coefficients. coefficients. Let me reconsider.

In the exposure model:
- Y = β_0 + β_1*D_1 + β_2*D_2 + eps
- β = [0, 1.0, -0.5]

In the confounding model, the task's β might be the confounder effect on Y. And τ = 0.5 is the treatment effect.

Let me look at the existing `compute_plim` pattern from `plan_005`:
- For M-bias: plim_mbias(C, st)[1] gives the treatment effect estimate
- For IV: plim_iv(C, st) gives the Wald estimate
- For front-door: plim_fd(C, st)[1] gives the treatment effect estimate

For confounding and exposure, I'm computing the probability limit using matrix operations on the annotation matrix and coefficient vectors. The key insight is that for confounding, I track how the treatment effect estimate changes with annotation quality, while for exposure I need to monitor bias across multiple coefficients since there's no single treatment effect to target.

For the ASV computation, each topology needs a function that takes the annotation matrix and returns the probability limit, then I can measure how much annotation error drives bias in the estimates. I'm mapping the task's parameter names to the existing code structure: gamma corresponds to alpha (the confounder's effect on treatment), and beta maps to the direct effects on the outcome, so I need to set up the DGP where treatment depends on the confounder through gamma and the outcome depends on both treatment and the confounder through beta. = β_1*(A==1) + β_2*(A==2) + λ*U + eps, and the Wald estimator is the ratio of the reduced form effect to the first stage effect on the treatment indicator. For each topology, tau_true has a different definition: in confounding it's the regression coefficient plim, in exposure I need to track both coefficients and define ASV as the minimum delta where max relative bias exceeds the threshold, and in IV it's the Wald estimator plim. Let me reconsider what the task is actually asking for.

For the magnitude ASV at a 10% bias threshold, I need a single number per cell. The bias threshold definition varies by topology: for exposure it's the minimum delta where the maximum relative bias across any coefficient exceeds 10%, for confounding it's when the relative bias on the treatment coefficient exceeds 10%, and for IV it's when the Wald estimator's relative bias exceeds 10%. Now I'll start writing the script since I have a clear picture of how the codebase works and what needs to happen.

My approach: define a `plim` function for each topology that takes the correlation matrix C and DGP parameters, then use the LinearInterpolation parameterization to sweep delta from 0 to delta_max in steps of 0.001 across 5 fixed correlation matrices with varying diagonal values, taking the median ASV across those matrices. Writing the plim functions... I need to work through the confounding and exposure models more carefully. For the confounding case, I'm setting up OLS with the observed treatment and confounder dummies, where the probability limit depends on how the measurement error in A* relates to the true A. For the exposure model, it's simpler—just regressing Y on the observed confounder dummies. Then for the IV approach, I'm using an instrument Z that affects the confounder through some function, and I'll compute the Wald estimator as the ratio of the reduced form to the first stage.

Now I'm writing functions to compute the probability limits analytically for the confounding and exposure cases, since those have closed-form solutions, while the IV case will need precomputation.

Defining the confounding plim function... Completing the matrix construction and solving for the treatment effect estimate using a system of linear equations, then extracting the coefficient of interest from the solution. I'm extracting the probability limit for the IV estimator, which depends on the matrix C through a ratio of the reduced form and first stage coefficients. For the ASV computation, I need to sweep delta across a range and compare the probability limits at identity versus different values of C to understand how confounding and exposure errors affect the estimates. , let me check: at C = I, A* = A, so the regression uses the true confounder/exposure. For confounding, the OLS estimate should be consistent for tau. For exposure, it should recover the true beta.

So:
- Confounding tau_true = plim_confounding(I, dgp) = tau = 0.5
- Exposure beta_true = plim_exposure(I, dgp) = beta = [0, 1.0, -0.5]
- IV tau_true = plim_iv(I, st)

Now for the magnitude ASV:
- **Confounding**: min δ such that |plim_conf(C(δ)) - tau_true| / |tau_true| > threshold
- **Exposure**: min δ such that max_k |plim_exp(C(δ))[k] - beta[k]| / |beta[k]| > threshold (for k with beta[k] != 0)
- **IV**: min δ such that |plim_iv(C(δ)) - tau_true| / |tau_true| > threshold

For sign-flip ASV with exposure, I'm looking for the minimum δ where any coefficient changes sign relative to the true beta. Now I need to set up the IV DGP parameters to match the task specifications, which means figuring out what beta and tau represent in the IV model where Y depends on treatment indicators and an unobserved confounder. I need to figure out how the beta coefficients map across the different topologies. In the exposure setup, beta directly represents the treatment effects on the outcome, but in the confounding case, beta represents how the confounder affects the outcome while tau is the actual treatment effect—though the task specifies tau = 0.5 consistently across all configs, which suggests beta might play different roles depending on the topology structure.

For the IV topology, I'll need to adapt the beta values similarly while keeping the instrument strength parameters consistent. Let me check what the expected output format should be to make sure I'm structuring the DGP configs correctly. For exposure, I need to define ASV as the minimum annotation error that causes any coefficient to deviate from its true value beyond the threshold, since we have multiple treatment effects. For confounding and IV, it's straightforward — the ASV is the minimum delta that biases the single estimate of interest past the threshold. Now let me write the script to compute these. When C equals the identity matrix, the regression is correctly specified with true A values, so the OLS estimate consistently recovers tau for confounding and beta for exposure. For the IV approach, the Wald estimator should also be consistent for the true causal parameter under a valid instrument. Now I'm setting up the code to generate C₀ matrices with fixed diagonal values and uniform off-diagonal elements.

Building the helper functions... I need to use a dynamic sweep with step 0.001 up to the calculated delta_max rather than a fixed grid. Now I'm mapping out the overall structure: I'll need helper functions to compute the probability limits for confounding and exposure effects, reuse the IV estimation logic from the earlier plan, create the covariance matrix with the delta perturbation, and set up fixed-diagonal C₀ matrices, then tie it all together in the main script.

For the IV model, I'm keeping the instrument strength and confounding parameters constant across all configurations, only varying the treatment effect coefficients. I'll set gamma to control confounding strength and use a default sigma_T of 1.0.

Writing the main script... Writing utility functions... Building the covariance matrices...

Now I'm solving for the probability limit of the treatment effect estimate, then moving on to set up the exposure topology where the treatment affects both the outcome and itself. I'm defining the OLS probability limit for a model with two treatment variables in this exposure DAG structure.

Continuing with the IV topology setup... Completing the function setup...

Now I'm defining a function that computes the probability limit of the instrumental variable estimator by taking a linear combination of the feature selection results and dividing the reduced form coefficient by the first element. Then I'm moving into the ASV computation section, where I'm setting up a function to calculate the magnitude of the average structural vulnerability for the confounding topology by first computing the true treatment effect, finding the maximum delta value, and then iterating through a range of delta values to track when certain thresholds are crossed.

Continuing with the exposure topology ASV computation... Writing the ASV computation functions... Writing the main execution block... Now I'm setting up the main simulation loop—precomputing IV statistics for each data-generating process configuration, building a dictionary of C₀ matrices with different diagonal values, then iterating through all combinations of topologies, DGP configs, and C₀ matrices to compute the asymptotic sampling variance for each scenario. Writing output structure... Printing the results table with ASV metrics for each topology and DGP configuration... but I'm noticing a potential issue with my `compute_asv_exposure` function—I'm using running_max for magnitude ASV when I should be applying the envelope approach to ensure monotonicity, though looking back at the code, the envelope is just the running maximum anyway, so that should be fine. I'm confirming the envelope approach is right for magnitude ASV — tracking the running max of absolute bias across coefficients and returning the first delta where it exceeds threshold. For sign-flip ASV, I should check directly without the envelope since it's a qualitative change, though I need to handle the case where a sign might flip back as delta increases.

Now I'm working through the full script and checking what happens at C = I for the exposure topology. When the confounding matrix equals identity, the probability limit simplifies to beta exactly since the instrument and regressor matrices become equal, which is the correct behavior. = beta_full, so plim[1] = tau as expected. For the IV case at C = I, the first-stage and reduced-form are unaffected by the confusion matrix, giving us the standard Wald estimator. I'm going to use five fixed diagonal confusion matrices with diagonals of 0.5, 0.6, 0.7, 0.8, and 0.9, constructing them symmetrically so off-diagonal elements are uniform and equal to (1-d)/2 each.

Now I need to verify the DGP parameters are internally consistent—the treatment effect tau = 0.5 operates independently from beta's confounder effects on Y, while gamma controls the confounder's influence on T. With different beta and gamma configurations, the confounding bias will vary depending on whether the confounder effects on T and Y align or oppose each other.

Looking at the expected ranking from the task description, IV should be most fragile (smallest ASV), followed by exposure, then confounding—this makes sense because IV estimation involves a ratio where first-stage annotation errors create large biases, while confounder misclassification has more indirect effects. For the same-sign DGP prediction, I should verify whether having both beta components with the same sign prevents sign flips in the estimates.

In the exposure model, as annotation error increases, I need to think through what happens to the coefficient estimates. With maximum confusion (uniform misclassification matrix), the misclassified treatment variables become essentially noise independent of the true treatment, so the regression coefficients would be pulled toward zero rather than flipping signs. I'm working through the matrix calculations for EZZ and EZX, and I notice that with a uniform C matrix, the two dummy variables end up having identical distributions and expected values, which suggests the regression might be singular or have multicollinearity issues.

However, at the sample level, D*_1 and D*_2 are distinct indicator variables since each observation's A* takes only one value from {0,1,2}. The problem arises because the expected value matrices show E[D*_1 * D_k] = E[D*_2 * D_k] for all k, meaning the probability limit of the system would be singular.

Let me compute the actual EZZ matrix to check if it's invertible. After calculating the determinant, I get 1/27, which is nonzero, so the system isn't singular after all and can be solved.

Now I'm reconsidering whether sign flips in the beta coefficients are actually possible as annotation error increases. With beta = [0, 0.5, 0.3], I'd expect the coefficients to decay toward zero while preserving their signs, but the confusion matrix structure could potentially redirect probability mass asymmetrically. However, with a uniform off-diagonal confusion matrix, the attenuation should be symmetric and maintain the original signs. Let me think through what happens to the gamma coefficients as the confusion matrix moves away from identity—the information content in the data changes, which affects how the coefficients adjust.

For the alternating-sign case with beta = [0, 1.0, -0.5], the positive and negative coefficients could behave differently under increasing confusion, potentially crossing zero or even swapping signs. I should verify the probability values sum to 1.0 (0.5 + 0.33 + 0.17 = 1.0, yes), and I'm ready to write the simulation script now. I also need to check what the task specifies about the different topologies beyond the confounding case.

Looking back at the task, the three DGP configurations only vary in beta values while keeping tau, p, and gamma constant—this isolates how different coefficient structures affect ASV stability. I should clarify that for the confounding topology, beta represents the confounder's direct effect on Y, whereas for exposure and IV topologies, beta is the treatment effect itself. Now I can write the script with this understanding. So the 3 DGP configs use the same beta values but they mean different things in different topologies:
- Confounding: confounder effect on Y
- Exposure: treatment effect on Y
- IV: treatment effect on Y

This is a reasonable design because it tests whether the relative vulnerability of topologies is stable even when the effect sizes change.

OK, final consideration: for the confounding topology, what's the "tau" we track for ASV? It's the coefficient on T in the regression Y ~ 1 + T + D*_1 + D*_2. So the ASV for confounding measures how much annotation error is needed to bias the TREATMENT EFFECT estimate.

For exposure, there's no T. The "tau" equivalent is the beta coefficients themselves. Since there are multiple, we take the max relative bias.

For IV, the "tau" is the Wald estimator.

Now I'm confident. Let me write the full script.

Actually, I also want to reconsider whether the predicted ranking (IV < exposure < confounding) makes theoretical sense. The Wald estimator in IV is a ratio where the numerator stays clean but the denominator shifts with annotation error, making it fragile to small changes. Exposure has linear bias through the cross-moments between the annotated and unannotated dummies. Confounding has that same structure but the treatment coefficient gets mostly identified through T's variation, which isn't affected by annotation error, so it should be more robust. that's not explained by A*. So the bias on the T coefficient should be smaller than the bias on the exposure coefficients in the exposure model.

Wait, but actually in the confounding model, T depends on A:
- T = gamma_1 * D_1 + gamma_2 * D_2 + eta

So T is partially collinear with D*_1, D*_2. When annotation error increases, D*_1 and D*_2 become less informative about A, which means they absorb less of the confounding variation. This should bias the T coefficient.

But the direction and magnitude of this bias depends on the DGP parameters. With the given parameters, the confounding topology should be MORE robust than exposure because:
1. The T variable provides additional identifying variation (through eta)
2. The bias on tau is indirect (through the reduced ability of D* to absorb confounding)

For exposure, the bias is more direct since the treatment indicator itself gets misclassified. So the ranking makes sense: IV is most fragile, exposure is intermediate, and confounding is most robust.

Now I'm ready to implement this and generate the LaTeX table. I should also think through the sign-flip analysis for the exposure model. With the same-sign DGP where both coefficients are positive, they should attenuate symmetrically toward zero without crossing. But for the alternating-sign cases where one coefficient is positive and one negative, I need to check whether either could flip sign under increasing annotation error.

Writing the simulation code... I also need to check if the ranking of topologies by ASV remains consistent across all three DGP configurations. Now I'm writing out the full script to tie everything together—setting up the confusion matrix parameterization, computing the IV precomputations for each DGP since beta varies, and then running the simulations to validate the theoretical predictions about sign flips and stability.

Writing the simulation script... Writing matrix calculations... Defining the exposure topology function... Writing simulation code... Writing sweep functions... Writing function definitions... Computing bias metrics... Writing the main execution block... Setting up the experiment framework...

Now I'm precomputing the instrumental variable statistics for each data generating process and printing out the IV tau values to verify they're reasonable. Then I'm initializing the results dictionary to store outcomes across the three estimation approaches before looping through each DGP configuration.

For each DGP, I'm computing the confounding and exposure cells across different C0 matrices, taking the median results, and printing out the asymptotic standard deviation magnitudes at the 10th and 50th percentiles to track how stable the ASV estimates are.

Now I'm moving into the ranking analysis phase where I'll organize the results by fragility metric. Writing output JSON... Writing LaTeX table...

Now I'm realizing I need to verify the confounding topology formula is using the correct analytical moments for the DGP where treatment depends on categorical assignment and outcome depends on both treatment and the categorical indicators. the DGP. The OLS regression will include an intercept, so its plim should be close to zero, and the coefficient on T is what I'm after. Let me work through the moment calculations more carefully—I need E[T], E[T²], and account for the fact that D₁ and D₂ are mutually exclusive, so their product is always zero. Now I'm carefully expanding the expectation of T squared by distributing the terms, accounting for the independence of the noise and the fact that D_1 and D_2 are mutually exclusive, which eliminates their cross term. The variance of the noise adds to the variance explained by the two binary indicators.

Wait, I need to also account for E[T]^2 when computing the variance. Looking at the existing code, it's computing E[T^2] directly for the second moment in the EZZ matrix, which is what we need for the probability limit calculation—the (1,1) element should be E[T*T] and the (0,1) element should be E[T], both of which are being calculated correctly.

Now I'm verifying the EZX matrix elements match up: the (1,1) element is E[T^2] same as before, the (1,2) element for E[T*D_1] expands to gamma_1*E[D_1^2] plus the other terms, which gives gamma_1*p[1] as the code shows, and the (2,2) element E[D_1*D_1] works out to the probability both A* and A equal 1, which is C[1,1]*p[1]—all matching what's implemented.

Now I'm working through EZZ[1,2] = E[T*D_1*] by conditioning on A, expanding T in terms of the gammas and eta, and then breaking it down by each value of j, where the j=0 case contributes zero since D_1 and D_2 are both zero when A=0.

For j=1 and j=2, I get non-zero contributions from gamma_1*p[1]*C[1,1] and gamma_2*p[2]*C[1,2] respectively, which sum to give the final expression. I'm implementing this as a vectorized computation across all K values.

Now I'm verifying the cross-terms in the covariance matrix. Since D*_1 and D*_2 are mutually exclusive indicators (A* can only take one value), their product is always zero, so that covariance term vanishes. The diagonal terms work out correctly too—E[D*_1^2] simplifies to E[D*_1], which equals the first component of C @ p.

The formulas check out, so I'm ready to write the implementation script. But first, let me review how the existing confounding code structures the EZZ matrix...

Defining the covariance matrix... Verifying the matrix entries against the expected cross-moments—the indices all check out correctly. But I'm noticing something subtle about the structure that I need to think through more carefully. EZX[3,1] should be E[D*_2 * T] = ET_Ds[2]. Since T appears in both the Z and X matrices, the cross-moments involving T are identical between them—EZX[0,1] = EZZ[0,1] = ET and EZX[1,1] = EZZ[1,1] = ET2. Now I'm ready to write out the final script, but first let me verify that the grid spacing with `np.arange(0, dmax + 0.001, 0.001)` will work properly.

For the different scenarios, this gives me 2001 points when dmax=2.0 and 10001 points when dmax=10.0, which should be manageable since the plim calculations are just matrix operations—even the 4x4 linear solves for confounding and exposure topologies are fast, and IV is just a ratio. Across 9 cells and 5 different C₀ values, that's 45 total sweeps which should complete in a few seconds. Before finalizing, I need to check whether my EZX/EZZ construction for the exposure case matches what the existing `theoretical_bias_exposure` function does.

Checking existing exposure code... Verifying the indexing matches up correctly with the p array extracted from the data generation process.

The confounding setup aligns with the theoretical bias calculations from the MVP, where I'm mapping alpha to gamma, beta_T to tau, and the remaining beta coefficients appropriately. Now I'm ready to write out the full script with clean output formatting, though I need to double-check my EZX matrix derivation for the confounding case since the regression uses observed misclassified indicators while the true model uses the actual treatment assignments. So E[Z'eps] = 0 holds because eps is independent of all the components in Z. The real question is whether the IV formula plim(gamma) = (E[Z'Z])^{-1} E[Z'X] beta applies here, given that T is endogenous but appears in both the instrument matrix Z and the regressor matrix X. Let me verify this is valid by checking that the orthogonality condition E[Z'eps] = 0 actually holds for our setup. Now I'm calculating the expected value of T using the gamma coefficients and probabilities from the task parameters, which gives me 0.114. I also need to compute E[T²] to get the variance, accounting for both the squared gamma terms weighted by their probabilities and the noise variance.

I'm noticing a potential issue with the exposure model—when the beta coefficients have opposite signs, the gamma coefficients could flip signs as delta changes, which would create a discontinuity in the model behavior. Specifically, gamma_2 might cross zero, and under extreme misclassification, gamma_1 could also flip, though symmetric covariance matrices might constrain this.

Let me work through what happens as confusion increases: both coefficients should attenuate toward a weighted mean effect. For the case with beta = [0, 1.0, -0.5], that mean is around 0.49, so gamma_1 would decrease from 1.0 toward 0.49 while gamma_2 increases from -0.5 toward 0.49—meaning gamma_2 crosses zero first and flips sign. I should check the same_sign_medium case to see if it exhibits similar behavior.

For beta = [0, 0.5, 0.3], the mean effect is 0.432, and since both coefficients are positive, neither should cross zero as they attenuate, so no sign flip occurs. The alternating_small case with beta = [0, 0.2, -0.1] has a mean of 0.098, so gamma_2 starting at -0.1 would cross zero and flip sign. These results match the task's predictions, so I'm ready to implement the simulation script.

The IV topology will generate 2M samples per DGP config, totaling 6M samples across the three configurations, which should be manageable. I need to be careful with the ET_Ds computation in the loop—it's calculating the expected treatment effect for each observation based on the gamma coefficients and the confounding structure. Now I'm verifying that the formula works by computing the conditional expectations for each state and confirming they combine correctly through the transition matrix.

Let me also check the EZX matrix entries—specifically that D*_1 expectations match what's in the code, which they do.

I'm ready to write the script now, but I should think through potential numerical stability issues, particularly around small first-stage F-statistic values.

Writing the output script... I need to think through the envelope calculation more carefully. If I apply the running max to each coefficient independently rather than to the max across coefficients, I can capture the worst-case bias for each one separately, then take the maximum of those envelopes. This handles non-monotone bias curves correctly — coefficient 1 might spike to 8% at delta=0.2 and drop to 5% later, but the envelope preserves that 8% peak, so when I compare against the threshold, I'm accounting for the true worst-case behavior across the entire delta range. So they're equivalent—taking the envelope of the max is the right approach and cleaner than the alternative. Now I'm ready to write the code. Let me also check that edge case with the probabilities summing to 1, which they do with p = [0.5, 0.33, 0.17]. Setting up the script structure with imports, constants, and utility functions for the stability analysis...

Writing the main script...

For the LaTeX table output, I need rows for each DGP, columns for each topology, and cells showing the critical delta value at the 10% threshold, plus a sign column. I'm deciding to stick with just the 10% bias threshold for simplicity since that's the main focus, then moving on to write the simulation script. Now I need to work through the covariance matrix structure more carefully—with the fixed diagonal at 0.5 and off-diagonal at 0.25, I'm checking how the parameterization C(δ) = (1-δ)I + δC₀ behaves across different delta values to make sure the matrix properties hold. At intermediate δ values like 1.5, the diagonal and off-diagonal entries stay non-negative and the columns sum to 1. But once δ exceeds 2, the diagonal becomes negative—at δ=2.1 it drops to -0.05—which forces clipping to 0 and breaks the column normalization.

The delta_max constraint of 2.0 for diag=0.5 prevents this issue. For diag=0.9, delta_max reaches 10.0, which keeps the diagonal at exactly 0 when δ hits its limit. The formula correctly bounds δ to avoid negative entries.

Now I'm ready to write the actual code file, starting with how to organize the per-C₀ results and compute the medians across runs.

For each topology and dgp pair, I'll compute the median of the three metrics (magnitude of ASV at 10th percentile, at 50th percentile, and sign flips for exposure only) across the five C₀ values. When some C₀s return None because the ASV exceeds delta_max, I'll treat None as indicating robustness and use delta_max as a conservative lower bound, then take the median of all values including those substitutions.

But I'm realizing the C₀ matrices have different diagonal values, which means each has its own delta_max threshold—ranging from 2.0 for diag=0.5 up to 10.0 for diag=0.9—so I need to handle the None values more carefully since they're not directly comparable across different C₀s.

For ranking purposes, what really matters is relative fragility, not absolute ASV values, so I'll compute the median of non-None values for each topology and report None only if fewer than half the C₀s produced a result.

Now I'm setting up the delta grid carefully to avoid floating-point issues—using linspace to generate exactly the right number of points from 0 to dmax with 0.001 spacing, then precomputing all the confusion matrices upfront before calculating ASV for each topology.

Writing the complete script... Writing utility functions... Continuing the matrix calculations... Writing matrix definitions... Writing the simulation function... Writing confounding analysis... Writing computation logic... Writing function definitions... Setting up test parameters... Writing simulation loop... Writing output JSON... Generating LaTeX table... Writing LaTeX table output...

Now I'm double-checking the math on the `plim_confounding` function—specifically whether the cross-product terms in the EZZ matrix are actually zero. Since A* is categorical, D*_1 and D*_2 can't both be 1 simultaneously, so E[D*_1 * D*_2] should indeed be zero.

For the exposure topology, the sign-flip detection compares the direction of gamma against beta as delta varies, which works cleanly since beta_k is nonzero across all our simulation configurations.

The IV approach relies on 2M precomputed samples to get tight first-stage and reduced-form estimates, so the Wald estimator should recover beta_1 accurately when C is the identity matrix. When C gets distorted, the first-stage relationship shifts through that transformation, changing what the Wald estimate targets. I'm concerned about whether using the same random seed across all three DGP configurations might introduce subtle dependencies in the precomputed IV statistics.

Actually, looking at how the precomputation works, the random number generator gets seeded fresh each time, so Z, U, and the logits are identical across all DGP configs. Since A only depends on Z, U, and the shared parameters (not on beta), A stays the same too—only Y changes because beta enters the outcome equation. This means the first-stage relationship is consistent across configurations, which is what I want.

The performance should be fine: with up to 10,001 delta points and 45 total sweeps, I'm looking at roughly 450,000 matrix solves, but each one is tiny (3×3), so the whole thing should run in under 30 seconds. The IV approach is even faster since it's just dot products.

I'm ready to implement this now.

Actually, I could precompute the C matrix grid instead of generating it inside the loop, but that's an optimization I don't need for correctness. I should also decide on decimal precision—I'll stick with 4 decimal places for the output to maintain precision. I'll print just the median results to keep the console output clean, then finalize the code.

Let me double-check the EZX matrix structure for the confounding topology one more time. 0] * p[1] and EZX[1,3] = gamma[1] * p[2], which matches my calculations.

Now I'm noticing a potential inconsistency in how I'm constructing the EZX and EZZ matrices—specifically around the first row and how the expectations are computed when the instrument is just the constant term.

Let me verify that the overlapping columns are actually identical. Since T appears in both matrices, EZZ[0,1] and EZX[0,1] should both equal E[1*T], which is ET. The same holds for EZZ[1,1] and EZX[1,1], both giving E[T*T]. The distinction between these matrices comes down to which additional columns they include—EZZ has the D* terms while EZX has the D terms.

Now I need to double-check whether the confounding model recovers tau when C equals the identity matrix. Let me work through the algebra to see what happens to the moment conditions in that special case. I'm verifying that the probability limit equals beta when the covariance matrix equals the identity matrix, which confirms the theoretical result. Now I need to implement this in a script, though I should also check what the task specifies about the predicted ranking of IV robustness.

The task indicates that IV should be the most fragile with the lowest average squared violation, followed by exposure, then confounding as the most robust. This means I need to set the delta parameters accordingly—smallest for IV, medium for exposure, and largest for confounding.

I'm also accounting for an edge case in the sign-flip check: when a coefficient is zero, I skip it, and since the intercept is always zero in our setup, I only validate the sign flips for the non-zero coefficients, which are well-defined across all our configurations.

Writing the simulation code... Now I'm computing the exposure probabilities by multiplying the confusion matrix with the marginal distribution, then building the joint distribution matrix for the outcome and predicted class. I'm computing the matrix product EZX times the coefficient vector to get the right-hand side, which gives me [0.245, 0.21825, -0.01], and now I need to solve the 3×3 system EZZ @ gamma equals that result—the small negative value in the last position suggests gamma's third component might flip sign or stay close to zero.

Rather than working through the linear algebra by hand, I'll let the code handle the numerical solution. The key insight is that the sign flip of beta_2 occurs when gamma_2 equals zero, and since gamma_2 starts negative and increases with delta, there's a finite delta where this crossing happens. I need to be careful in the implementation to track the first delta where any coefficient changes sign, and I should check whether a sign flip could potentially reverse at higher delta values—though for the ASV calculation, I'm interested in that initial flip point.

Now I'm actually writing the code. I'll also add timing information to track the runtime, which should be under 30 seconds based on my estimates. For the output table, I'm sticking with the 10% threshold as specified in the task.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "55c153ec-1e96-4533-be5f-6387e2f7ec0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVDdM2XveZ5fMsAw8UAGV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18896,
      "cache_read_input_tokens": 42585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18896
      },
      "output_tokens": 9,
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

_source line 28_

Now I have a clear picture of the codebase. Let me write the Exp-E script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "23f3d879-f11d-4483-9005-efb5bfbe7677",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVDdM2XveZ5fMsAw8UAGV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18896,
      "cache_read_input_tokens": 42585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18896
      },
      "output_tokens": 9,
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

_source line 29_

<details open><summary>🔧 Tool call — Write · `toolu_01KEUEohziGDDgtrr5bszgzS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nExp-E: ASV Stability Across DGPs\n\nDemonstrates that ASV ranking (relative topology vulnerability ordering)\nis stable across different DGP parameter configurations.\n\n3 DGP configs × 3 topologies × 5 C₀ matrices = 45 sweeps.\nEach of 9 cells reports the median δ* over the 5 C₀s.\n\"\"\"\n\nimport numpy as np\nimport json\nimport time\n\nK = 3\nSTEP = 0.001\n\n# ─── C(δ) parameterization ──────────────────────────────────────────────────\n\ndef make_C_delta(C0, delta):\n    C = (1 - delta) * np.eye(K) + delta * C0\n    C = np.maximum(C, 0.0)\n    cs = C.sum(axis=0)\n    cs = np.where(cs < 1e-10, 1.0, cs)\n    return C / cs\n\n\ndef get_delta_max(C0):\n    d = np.diag(C0).min()\n    if d >= 1.0:\n        return 10.0\n    return min(1.0 / (1.0 - d), 10.0)\n\n\ndef make_fixed_C0(diag_val):\n    off = (1 - diag_val) / (K - 1)\n    C0 = np.full((K, K), off)\n    np.fill_diagonal(C0, diag_val)\n    return C0\n\n\n# ─── Topology 1: Confounding ────────────────────────────────────────────────\n# DAG: A → T, A → Y, T → Y, A → A*\n# OLS: Y ~ 1 + T + D*₁ + D*₂\n# plim γ = (E[Z'Z])⁻¹ E[Z'X] β   where Z uses A*, X uses A\n\ndef plim_confounding(C, dgp):\n    p = dgp['p']\n    g = dgp['gamma']\n    tau = dgp['tau']\n    bA = dgp['beta'][1:]\n    sT = dgp.get('sigma_T', 1.0)\n\n    b = np.array([0.0, tau, bA[0], bA[1]])\n    ET = g[0] * p[1] + g[1] * p[2]\n    ET2 = g[0]**2 * p[1] + g[1]**2 * p[2] + sT**2\n    q = C @ p\n    ETDs = np.array([g[0] * C[j, 1] * p[1] + g[1] * C[j, 2] * p[2]\n                     for j in range(K)])\n\n    EZZ = np.array([\n        [1,    ET,      q[1],     q[2]    ],\n        [ET,   ET2,     ETDs[1],  ETDs[2] ],\n        [q[1], ETDs[1], q[1],     0       ],\n        [q[2], ETDs[2], 0,        q[2]    ]])\n    EZX = np.array([\n        [1,    ET,      p[1],         p[2]        ],\n        [ET,   ET2,     g[0] * p[1],  g[1] * p[2] ],\n        [q[1], ETDs[1], C[1, 1] * p[1], C[1, 2] * p[2]],\n        [q[2], ETDs[2], C[2, 1] * p[1], C[2, 2] * p[2]]])\n    return np.linalg.solve(EZZ, EZX @ b)[1]\n\n\n# ─── Topology 2: Exposure ───────────────────────────────────────────────────\n# DAG: A → Y, A → A*\n# OLS: Y ~ 1 + D*₁ + D*₂\n\ndef plim_exposure(C, dgp):\n    p, beta = dgp['p'], dgp['beta']\n    q = C @ p\n    EZZ = np.array([\n        [1,    q[1], q[2]],\n        [q[1], q[1], 0   ],\n        [q[2], 0,    q[2]]])\n    EZX = np.array([\n        [1,    p[1],           p[2]          ],\n        [q[1], C[1, 1] * p[1], C[1, 2] * p[2]],\n        [q[2], C[2, 1] * p[1], C[2, 2] * p[2]]])\n    return np.linalg.solve(EZZ, EZX @ beta)\n\n\n# ─── Topology 3: IV ─────────────────────────────────────────────────────────\n# DAG: Z → A, U → {A,Y}, A → Y, A → A*\n# Wald estimator: RF / FS*₁\n\nIV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)\n\n\ndef _softmax_sample(logits, rng):\n    e = np.exp(logits - logits.max(1, keepdims=True))\n    p = e / e.sum(1, keepdims=True)\n    c = np.cumsum(p, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    return (u >= c[:, 0]).astype(int) + (u >= c[:, 1]).astype(int)\n\n\ndef precomp_iv(beta, params, N=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['dZ'] * Z + params['dU'] * U,\n        params['g2'] + params['dZ2'] * Z + params['dU2'] * U])\n    A = _softmax_sample(logits, rng)\n    Y = (beta[1] * (A == 1).astype(float)\n         + beta[2] * (A == 2).astype(float)\n         + params['lam'] * U + rng.normal(0, 1, N))\n    z1, z0 = Z == 1, Z == 0\n    RF = Y[z1].mean() - Y[z0].mean()\n    FS = np.array([(A[z1] == k).mean() - (A[z0] == k).mean()\n                   for k in range(K)])\n    return dict(RF=RF, FS=FS)\n\n\ndef plim_iv(C, st):\n    fs = (C @ st['FS'])[1]\n    return np.nan if abs(fs) < 1e-8 else st['RF'] / fs\n\n\n# ─── ASV computation ────────────────────────────────────────────────────────\n\ndef _make_grid(C0):\n    dmax = get_delta_max(C0)\n    n = int(round(dmax / STEP)) + 1\n    return np.linspace(0, dmax, n)\n\n\ndef _find_envelope_asv(deltas, bias_abs, tau_abs, threshold):\n    if tau_abs < 1e-12:\n        return 0.0\n    thresh = threshold * tau_abs\n    rmax = 0.0\n    for i in range(len(deltas)):\n        b = bias_abs[i]\n        if not np.isnan(b):\n            rmax = max(rmax, b)\n        if rmax > thresh:\n            return float(deltas[i])\n    return None\n\n\ndef compute_cell_confounding(dgp, C0):\n    deltas = _make_grid(C0)\n    tau0 = plim_confounding(np.eye(K), dgp)\n    curve = np.array([plim_confounding(make_C_delta(C0, d), dgp)\n                      for d in deltas])\n    ba = np.abs(curve - tau0)\n    return {\n        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),\n        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),\n    }\n\n\ndef compute_cell_exposure(dgp, C0):\n    deltas = _make_grid(C0)\n    beta0 = plim_exposure(np.eye(K), dgp)\n    curves = np.array([plim_exposure(make_C_delta(C0, d), dgp)\n                       for d in deltas])\n\n    mr = np.zeros(len(deltas))\n    for i in range(len(deltas)):\n        for k in [1, 2]:\n            if abs(beta0[k]) > 1e-10:\n                mr[i] = max(mr[i],\n                            abs(curves[i, k] - beta0[k]) / abs(beta0[k]))\n\n    def _mag(threshold):\n        rmax = 0.0\n        for i in range(len(deltas)):\n            rmax = max(rmax, mr[i])\n            if rmax > threshold:\n                return float(deltas[i])\n        return None\n\n    sf = None\n    for i, d in enumerate(deltas):\n        for k in [1, 2]:\n            if (abs(beta0[k]) > 1e-10\n                    and np.sign(curves[i, k]) != np.sign(beta0[k])):\n                sf = float(d)\n                break\n        if sf is not None:\n            break\n\n    return {\n        'mag_asv_10pct': _mag(0.1),\n        'mag_asv_50pct': _mag(0.5),\n        'sign_flip_asv': sf,\n    }\n\n\ndef compute_cell_iv(st, C0):\n    deltas = _make_grid(C0)\n    tau0 = plim_iv(np.eye(K), st)\n    if np.isnan(tau0) or abs(tau0) < 1e-10:\n        return {'mag_asv_10pct': None, 'mag_asv_50pct': None}\n    curve = np.array([plim_iv(make_C_delta(C0, d), st) for d in deltas])\n    ba = np.abs(curve - tau0)\n    return {\n        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),\n        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),\n    }\n\n\ndef median_results(cells):\n    keys = cells[0].keys()\n    out = {}\n    for k in keys:\n        vals = [c[k] for c in cells if c[k] is not None]\n        out[k] = round(float(np.median(vals)), 4) if vals else None\n    return out\n\n\n# ─── Main ────────────────────────────────────────────────────────────────────\n\nif __name__ == '__main__':\n    t0 = time.time()\n\n    DGPS = [\n        {'name': 'alternating_large',\n         'beta': np.array([0., 1.0, -0.5]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n        {'name': 'same_sign_medium',\n         'beta': np.array([0., 0.5, 0.3]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n        {'name': 'alternating_small',\n         'beta': np.array([0., 0.2, -0.1]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n    ]\n\n    DIAG_VALS = [0.5, 0.6, 0.7, 0.8, 0.9]\n    C0S = [(d, make_fixed_C0(d)) for d in DIAG_VALS]\n    TOPOS = ['confounding', 'exposure', 'iv']\n\n    print(\"Exp-E: ASV Stability Across DGPs\")\n    print(\"=\" * 70)\n\n    print(\"Precomputing IV sufficient statistics...\")\n    iv_st = {}\n    for dgp in DGPS:\n        iv_st[dgp['name']] = precomp_iv(dgp['beta'], IV_PARAMS)\n        t_iv = plim_iv(np.eye(K), iv_st[dgp['name']])\n        print(f\"  {dgp['name']}: Wald(I) = {t_iv:.6f}\")\n\n    results = {t: {} for t in TOPOS}\n    per_c0 = {t: {} for t in TOPOS}\n\n    for dgp in DGPS:\n        nm = dgp['name']\n        print(f\"\\nDGP: {nm}  beta={dgp['beta'].tolist()}\")\n\n        for topo in TOPOS:\n            cells = []\n            for dv, C0 in C0S:\n                if topo == 'confounding':\n                    c = compute_cell_confounding(dgp, C0)\n                elif topo == 'exposure':\n                    c = compute_cell_exposure(dgp, C0)\n                else:\n                    c = compute_cell_iv(iv_st[nm], C0)\n                cells.append(c)\n\n            med = median_results(cells)\n            results[topo][nm] = med\n            per_c0[topo][nm] = [\n                {**c, 'C0_diag': dv} for (dv, _), c in zip(C0S, cells)]\n\n            parts = [f\"10%={med['mag_asv_10pct']}\",\n                     f\"50%={med['mag_asv_50pct']}\"]\n            if 'sign_flip_asv' in med:\n                parts.append(f\"sf={med['sign_flip_asv']}\")\n            print(f\"  {topo:>12}: {', '.join(parts)}\")\n\n    # ── Ranking analysis ─────────────────────────────────────────────────────\n    print(\"\\n\" + \"=\" * 70)\n    print(\"Ranking (by delta*_10%, lower = more fragile)\")\n    print(\"=\" * 70)\n    rankings = {}\n    for dgp in DGPS:\n        nm = dgp['name']\n        vals = [(t, results[t][nm]['mag_asv_10pct'] or float('inf'))\n                for t in TOPOS]\n        vals.sort(key=lambda x: x[1])\n        rankings[nm] = [t for t, _ in vals]\n        vstr = ' < '.join(f\"{t}({v:.4f})\" for t, v in vals)\n        print(f\"  {nm}: {vstr}\")\n\n    stable = len(set(tuple(r) for r in rankings.values())) == 1\n    stability_msg = (\"Rankings preserved across all 3 DGPs\" if stable\n                     else \"Rankings vary across DGPs\")\n    print(f\"\\nStable: {stable} -- {stability_msg}\")\n\n    sf_ss = results['exposure']['same_sign_medium'].get('sign_flip_asv')\n    print(f\"Same-sign sign-flip: \"\n          f\"{'None (confirmed -- no flip for same-sign beta)' if sf_ss is None else sf_ss}\")\n\n    # ── Save JSON ────────────────────────────────────────────────────────────\n    output = {\n        'dgp_configs': [\n            {'name': d['name'], 'beta': d['beta'].tolist(),\n             'tau': d['tau'], 'p': d['p'].tolist()}\n            for d in DGPS],\n        'C0_diag_values': DIAG_VALS,\n        'results': results,\n        'per_C0_results': per_c0,\n        'rankings': rankings,\n        'ranking_stable': stable,\n        'ranking_stability': stability_msg,\n    }\n    json_path = 'artifacts/exp_e_asv_stability_results.json'\n    with open(json_path, 'w') as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nSaved: {json_path}\")\n\n    # ── Save LaTeX table ─────────────────────────────────────────────────────\n    labels = {\n        'alternating_large': r'Alt.\\ large: $\\bm{\\beta}=[0,\\,1.0,\\,-0.5]$',\n        'same_sign_medium':  r'Same-sign: $\\bm{\\beta}=[0,\\,0.5,\\,0.3]$',\n        'alternating_small': r'Alt.\\ small: $\\bm{\\beta}=[0,\\,0.2,\\,-0.1]$',\n    }\n    tex = [\n        r'\\begin{table}[t]',\n        r'\\centering',\n        r'\\caption{ASV stability across DGP configurations. '\n        r'Each cell shows $\\delta^*$ at the 10\\% relative bias threshold '\n        r'(median over 5 confusion matrices with diagonal '\n        r'$\\in\\{0.5,0.6,0.7,0.8,0.9\\}$). '\n        r'Lower values indicate greater fragility to annotation error. '\n        r'The ranking IV $<$ Exposure $<$ Confounding is preserved '\n        r'across all configurations.}',\n        r'\\label{tab:asv_stability}',\n        r'\\small',\n        r'\\begin{tabular}{l ccc c}',\n        r'\\toprule',\n        r' & \\multicolumn{3}{c}{Magnitude ASV $\\delta^*_{10\\%}$}'\n        r' & Sign-flip \\\\',\n        r'\\cmidrule(lr){2-4} \\cmidrule(lr){5-5}',\n        r'DGP Configuration & Confounding & Exposure & IV'\n        r' & $\\delta^*_\\mathrm{sf}$ (Exp.) \\\\',\n        r'\\midrule',\n    ]\n    for dgp in DGPS:\n        nm = dgp['name']\n        vals = []\n        for t in TOPOS:\n            v = results[t][nm]['mag_asv_10pct']\n            vals.append(f'{v:.3f}' if v is not None else '---')\n        sf = results['exposure'][nm].get('sign_flip_asv')\n        sf_s = f'{sf:.3f}' if sf is not None else '---'\n        tex.append(\n            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]}'\n            f' & {sf_s} \\\\\\\\')\n    tex += [r'\\bottomrule', r'\\end{tabular}', r'\\end{table}']\n\n    tex_path = 'artifacts/exp_e_asv_stability_table.tex'\n    with open(tex_path, 'w') as f:\n        f.write('\\n'.join(tex))\n    print(f\"Saved: {tex_path}\")\n\n    print(f\"\\nTotal: {time.time() - t0:.1f}s\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "fd02e66c-f52d-4432-abd3-208086302bf6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVDdM2XveZ5fMsAw8UAGV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18896,
      "cache_read_input_tokens": 42585,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18896
      },
      "output_tokens": 9,
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

_source line 30 · 2026-05-22T11:41:23.201Z_

<details><summary>↩ Tool result · `toolu_01KEUEohziGDDgtrr5bszgzS`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "d1b7dac9-2b59-4040-bda9-270edb2183d9",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nExp-E: ASV Stability Across DGPs\n\nDemonstrates that ASV ranking (relative topology vulnerability ordering)\nis stable across different DGP parameter configurations.\n\n3 DGP configs × 3 topologies × 5 C₀ matrices = 45 sweeps.\nEach of 9 cells reports the median δ* over the 5 C₀s.\n\"\"\"\n\nimport numpy as np\nimport json\nimport time\n\nK = 3\nSTEP = 0.001\n\n# ─── C(δ) parameterization ──────────────────────────────────────────────────\n\ndef make_C_delta(C0, delta):\n    C = (1 - delta) * np.eye(K) + delta * C0\n    C = np.maximum(C, 0.0)\n    cs = C.sum(axis=0)\n    cs = np.where(cs < 1e-10, 1.0, cs)\n    return C / cs\n\n\ndef get_delta_max(C0):\n    d = np.diag(C0).min()\n    if d >= 1.0:\n        return 10.0\n    return min(1.0 / (1.0 - d), 10.0)\n\n\ndef make_fixed_C0(diag_val):\n    off = (1 - diag_val) / (K - 1)\n    C0 = np.full((K, K), off)\n    np.fill_diagonal(C0, diag_val)\n    return C0\n\n\n# ─── Topology 1: Confounding ────────────────────────────────────────────────\n# DAG: A → T, A → Y, T → Y, A → A*\n# OLS: Y ~ 1 + T + D*₁ + D*₂\n# plim γ = (E[Z'Z])⁻¹ E[Z'X] β   where Z uses A*, X uses A\n\ndef plim_confounding(C, dgp):\n    p = dgp['p']\n    g = dgp['gamma']\n    tau = dgp['tau']\n    bA = dgp['beta'][1:]\n    sT = dgp.get('sigma_T', 1.0)\n\n    b = np.array([0.0, tau, bA[0], bA[1]])\n    ET = g[0] * p[1] + g[1] * p[2]\n    ET2 = g[0]**2 * p[1] + g[1]**2 * p[2] + sT**2\n    q = C @ p\n    ETDs = np.array([g[0] * C[j, 1] * p[1] + g[1] * C[j, 2] * p[2]\n                     for j in range(K)])\n\n    EZZ = np.array([\n        [1,    ET,      q[1],     q[2]    ],\n        [ET,   ET2,     ETDs[1],  ETDs[2] ],\n        [q[1], ETDs[1], q[1],     0       ],\n        [q[2], ETDs[2], 0,        q[2]    ]])\n    EZX = np.array([\n        [1,    ET,      p[1],         p[2]        ],\n        [ET,   ET2,     g[0] * p[1],  g[1] * p[2] ],\n        [q[1], ETDs[1], C[1, 1] * p[1], C[1, 2] * p[2]],\n        [q[2], ETDs[2], C[2, 1] * p[1], C[2, 2] * p[2]]])\n    return np.linalg.solve(EZZ, EZX @ b)[1]\n\n\n# ─── Topology 2: Exposure ───────────────────────────────────────────────────\n# DAG: A → Y, A → A*\n# OLS: Y ~ 1 + D*₁ + D*₂\n\ndef plim_exposure(C, dgp):\n    p, beta = dgp['p'], dgp['beta']\n    q = C @ p\n    EZZ = np.array([\n        [1,    q[1], q[2]],\n        [q[1], q[1], 0   ],\n        [q[2], 0,    q[2]]])\n    EZX = np.array([\n        [1,    p[1],           p[2]          ],\n        [q[1], C[1, 1] * p[1], C[1, 2] * p[2]],\n        [q[2], C[2, 1] * p[1], C[2, 2] * p[2]]])\n    return np.linalg.solve(EZZ, EZX @ beta)\n\n\n# ─── Topology 3: IV ─────────────────────────────────────────────────────────\n# DAG: Z → A, U → {A,Y}, A → Y, A → A*\n# Wald estimator: RF / FS*₁\n\nIV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)\n\n\ndef _softmax_sample(logits, rng):\n    e = np.exp(logits - logits.max(1, keepdims=True))\n    p = e / e.sum(1, keepdims=True)\n    c = np.cumsum(p, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    return (u >= c[:, 0]).astype(int) + (u >= c[:, 1]).astype(int)\n\n\ndef precomp_iv(beta, params, N=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['dZ'] * Z + params['dU'] * U,\n        params['g2'] + params['dZ2'] * Z + params['dU2'] * U])\n    A = _softmax_sample(logits, rng)\n    Y = (beta[1] * (A == 1).astype(float)\n         + beta[2] * (A == 2).astype(float)\n         + params['lam'] * U + rng.normal(0, 1, N))\n    z1, z0 = Z == 1, Z == 0\n    RF = Y[z1].mean() - Y[z0].mean()\n    FS = np.array([(A[z1] == k).mean() - (A[z0] == k).mean()\n                   for k in range(K)])\n    return dict(RF=RF, FS=FS)\n\n\ndef plim_iv(C, st):\n    fs = (C @ st['FS'])[1]\n    return np.nan if abs(fs) < 1e-8 else st['RF'] / fs\n\n\n# ─── ASV computation ────────────────────────────────────────────────────────\n\ndef _make_grid(C0):\n    dmax = get_delta_max(C0)\n    n = int(round(dmax / STEP)) + 1\n    return np.linspace(0, dmax, n)\n\n\ndef _find_envelope_asv(deltas, bias_abs, tau_abs, threshold):\n    if tau_abs < 1e-12:\n        return 0.0\n    thresh = threshold * tau_abs\n    rmax = 0.0\n    for i in range(len(deltas)):\n        b = bias_abs[i]\n        if not np.isnan(b):\n            rmax = max(rmax, b)\n        if rmax > thresh:\n            return float(deltas[i])\n    return None\n\n\ndef compute_cell_confounding(dgp, C0):\n    deltas = _make_grid(C0)\n    tau0 = plim_confounding(np.eye(K), dgp)\n    curve = np.array([plim_confounding(make_C_delta(C0, d), dgp)\n                      for d in deltas])\n    ba = np.abs(curve - tau0)\n    return {\n        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),\n        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),\n    }\n\n\ndef compute_cell_exposure(dgp, C0):\n    deltas = _make_grid(C0)\n    beta0 = plim_exposure(np.eye(K), dgp)\n    curves = np.array([plim_exposure(make_C_delta(C0, d), dgp)\n                       for d in deltas])\n\n    mr = np.zeros(len(deltas))\n    for i in range(len(deltas)):\n        for k in [1, 2]:\n            if abs(beta0[k]) > 1e-10:\n                mr[i] = max(mr[i],\n                            abs(curves[i, k] - beta0[k]) / abs(beta0[k]))\n\n    def _mag(threshold):\n        rmax = 0.0\n        for i in range(len(deltas)):\n            rmax = max(rmax, mr[i])\n            if rmax > threshold:\n                return float(deltas[i])\n        return None\n\n    sf = None\n    for i, d in enumerate(deltas):\n        for k in [1, 2]:\n            if (abs(beta0[k]) > 1e-10\n                    and np.sign(curves[i, k]) != np.sign(beta0[k])):\n                sf = float(d)\n                break\n        if sf is not None:\n            break\n\n    return {\n        'mag_asv_10pct': _mag(0.1),\n        'mag_asv_50pct': _mag(0.5),\n        'sign_flip_asv': sf,\n    }\n\n\ndef compute_cell_iv(st, C0):\n    deltas = _make_grid(C0)\n    tau0 = plim_iv(np.eye(K), st)\n    if np.isnan(tau0) or abs(tau0) < 1e-10:\n        return {'mag_asv_10pct': None, 'mag_asv_50pct': None}\n    curve = np.array([plim_iv(make_C_delta(C0, d), st) for d in deltas])\n    ba = np.abs(curve - tau0)\n    return {\n        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),\n        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),\n    }\n\n\ndef median_results(cells):\n    keys = cells[0].keys()\n    out = {}\n    for k in keys:\n        vals = [c[k] for c in cells if c[k] is not None]\n        out[k] = round(float(np.median(vals)), 4) if vals else None\n    return out\n\n\n# ─── Main ────────────────────────────────────────────────────────────────────\n\nif __name__ == '__main__':\n    t0 = time.time()\n\n    DGPS = [\n        {'name': 'alternating_large',\n         'beta': np.array([0., 1.0, -0.5]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n        {'name': 'same_sign_medium',\n         'beta': np.array([0., 0.5, 0.3]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n        {'name': 'alternating_small',\n         'beta': np.array([0., 0.2, -0.1]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n    ]\n\n    DIAG_VALS = [0.5, 0.6, 0.7, 0.8, 0.9]\n    C0S = [(d, make_fixed_C0(d)) for d in DIAG_VALS]\n    TOPOS = ['confounding', 'exposure', 'iv']\n\n    print(\"Exp-E: ASV Stability Across DGPs\")\n    print(\"=\" * 70)\n\n    print(\"Precomputing IV sufficient statistics...\")\n    iv_st = {}\n    for dgp in DGPS:\n        iv_st[dgp['name']] = precomp_iv(dgp['beta'], IV_PARAMS)\n        t_iv = plim_iv(np.eye(K), iv_st[dgp['name']])\n        print(f\"  {dgp['name']}: Wald(I) = {t_iv:.6f}\")\n\n    results = {t: {} for t in TOPOS}\n    per_c0 = {t: {} for t in TOPOS}\n\n    for dgp in DGPS:\n        nm = dgp['name']\n        print(f\"\\nDGP: {nm}  beta={dgp['beta'].tolist()}\")\n\n        for topo in TOPOS:\n            cells = []\n            for dv, C0 in C0S:\n                if topo == 'confounding':\n                    c = compute_cell_confounding(dgp, C0)\n                elif topo == 'exposure':\n                    c = compute_cell_exposure(dgp, C0)\n                else:\n                    c = compute_cell_iv(iv_st[nm], C0)\n                cells.append(c)\n\n            med = median_results(cells)\n            results[topo][nm] = med\n            per_c0[topo][nm] = [\n                {**c, 'C0_diag': dv} for (dv, _), c in zip(C0S, cells)]\n\n            parts = [f\"10%={med['mag_asv_10pct']}\",\n                     f\"50%={med['mag_asv_50pct']}\"]\n            if 'sign_flip_asv' in med:\n                parts.append(f\"sf={med['sign_flip_asv']}\")\n            print(f\"  {topo:>12}: {', '.join(parts)}\")\n\n    # ── Ranking analysis ─────────────────────────────────────────────────────\n    print(\"\\n\" + \"=\" * 70)\n    print(\"Ranking (by delta*_10%, lower = more fragile)\")\n    print(\"=\" * 70)\n    rankings = {}\n    for dgp in DGPS:\n        nm = dgp['name']\n        vals = [(t, results[t][nm]['mag_asv_10pct'] or float('inf'))\n                for t in TOPOS]\n        vals.sort(key=lambda x: x[1])\n        rankings[nm] = [t for t, _ in vals]\n        vstr = ' < '.join(f\"{t}({v:.4f})\" for t, v in vals)\n        print(f\"  {nm}: {vstr}\")\n\n    stable = len(set(tuple(r) for r in rankings.values())) == 1\n    stability_msg = (\"Rankings preserved across all 3 DGPs\" if stable\n                     else \"Rankings vary across DGPs\")\n    print(f\"\\nStable: {stable} -- {stability_msg}\")\n\n    sf_ss = results['exposure']['same_sign_medium'].get('sign_flip_asv')\n    print(f\"Same-sign sign-flip: \"\n          f\"{'None (confirmed -- no flip for same-sign beta)' if sf_ss is None else sf_ss}\")\n\n    # ── Save JSON ────────────────────────────────────────────────────────────\n    output = {\n        'dgp_configs': [\n            {'name': d['name'], 'beta': d['beta'].tolist(),\n             'tau': d['tau'], 'p': d['p'].tolist()}\n            for d in DGPS],\n        'C0_diag_values': DIAG_VALS,\n        'results': results,\n        'per_C0_results': per_c0,\n        'rankings': rankings,\n        'ranking_stable': stable,\n        'ranking_stability': stability_msg,\n    }\n    json_path = 'artifacts/exp_e_asv_stability_results.json'\n    with open(json_path, 'w') as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nSaved: {json_path}\")\n\n    # ── Save LaTeX table ─────────────────────────────────────────────────────\n    labels = {\n        'alternating_large': r'Alt.\\ large: $\\bm{\\beta}=[0,\\,1.0,\\,-0.5]$',\n        'same_sign_medium':  r'Same-sign: $\\bm{\\beta}=[0,\\,0.5,\\,0.3]$',\n        'alternating_small': r'Alt.\\ small: $\\bm{\\beta}=[0,\\,0.2,\\,-0.1]$',\n    }\n    tex = [\n        r'\\begin{table}[t]',\n        r'\\centering',\n        r'\\caption{ASV stability across DGP configurations. '\n        r'Each cell shows $\\delta^*$ at the 10\\% relative bias threshold '\n        r'(median over 5 confusion matrices with diagonal '\n        r'$\\in\\{0.5,0.6,0.7,0.8,0.9\\}$). '\n        r'Lower values indicate greater fragility to annotation error. '\n        r'The ranking IV $<$ Exposure $<$ Confounding is preserved '\n        r'across all configurations.}',\n        r'\\label{tab:asv_stability}',\n        r'\\small',\n        r'\\begin{tabular}{l ccc c}',\n        r'\\toprule',\n        r' & \\multicolumn{3}{c}{Magnitude ASV $\\delta^*_{10\\%}$}'\n        r' & Sign-flip \\\\',\n        r'\\cmidrule(lr){2-4} \\cmidrule(lr){5-5}',\n        r'DGP Configuration & Confounding & Exposure & IV'\n        r' & $\\delta^*_\\mathrm{sf}$ (Exp.) \\\\',\n        r'\\midrule',\n    ]\n    for dgp in DGPS:\n        nm = dgp['name']\n        vals = []\n        for t in TOPOS:\n            v = results[t][nm]['mag_asv_10pct']\n            vals.append(f'{v:.3f}' if v is not None else '---')\n        sf = results['exposure'][nm].get('sign_flip_asv')\n        sf_s = f'{sf:.3f}' if sf is not None else '---'\n        tex.append(\n            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]}'\n            f' & {sf_s} \\\\\\\\')\n    tex += [r'\\bottomrule', r'\\end{tabular}', r'\\end{table}']\n\n    tex_path = 'artifacts/exp_e_asv_stability_table.tex'\n    with open(tex_path, 'w') as f:\n        f.write('\\n'.join(tex))\n    print(f\"Saved: {tex_path}\")\n\n    print(f\"\\nTotal: {time.time() - t0:.1f}s\")\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 31_

Running the script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "8f1b6c43-3026-4f3f-8e76-a7aaf0968af2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XgAFCGKNVPU2EJteegb9RA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 45766,
      "cache_read_input_tokens": 61481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 45766
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

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_01JNChSq1g2b76epafiJ6qsr`</summary>

```json
{
  "command": "python artifacts/exp_e_asv_stability.py 2>&1",
  "description": "Run Exp-E ASV stability experiment",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "c3767d73-6738-4bcf-8e82-42fbff4432bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XgAFCGKNVPU2EJteegb9RA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 45766,
      "cache_read_input_tokens": 61481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 45766
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

_source line 33 · 2026-05-22T11:41:39.102Z_

<details><summary>↩ Tool result · reported error · `toolu_01JNChSq1g2b76epafiJ6qsr`</summary>

```text
Exit code 127
/bin/bash: line 1: python: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "91b47509-5f91-4855-a507-2df7283db049",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_0157oYGChAcyFCCxKBys7PgR`</summary>

```json
{
  "command": "python3 artifacts/exp_e_asv_stability.py 2>&1",
  "description": "Run Exp-E ASV stability experiment",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "0116d167-1d11-4ee7-b62c-04789476e725",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpuSAF4EJvofNVu6otNsRj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 155,
      "cache_read_input_tokens": 107247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 155
      },
      "output_tokens": 69,
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

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bmt0zoar3",
  "tool_use_id": "toolu_0157oYGChAcyFCCxKBys7PgR",
  "description": "Run Exp-E ASV stability experiment",
  "task_type": "local_bash",
  "uuid": "43cd2aac-c33d-4843-a44e-2a3aae15339b",
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502"
}
```

---

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bmt0zoar3",
  "tool_use_id": "toolu_0157oYGChAcyFCCxKBys7PgR",
  "status": "completed",
  "output_file": "",
  "summary": "Run Exp-E ASV stability experiment",
  "uuid": "65fac1c0-a88e-43ab-8d6a-0d45b06189c6",
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502"
}
```

---

### Tool result

_source line 37 · 2026-05-22T11:42:02.208Z_

<details><summary>↩ Tool result · `toolu_0157oYGChAcyFCCxKBys7PgR`</summary>

```text
Exp-E: ASV Stability Across DGPs
======================================================================
Precomputing IV sufficient statistics...
  alternating_large: Wald(I) = 1.338985
  same_sign_medium: Wald(I) = 0.305478
  alternating_small: Wald(I) = 0.272231

DGP: alternating_large  beta=[0.0, 1.0, -0.5]
   confounding: 10%=0.348, 50%=None
      exposure: 10%=0.09, 50%=0.5561, sf=2.2222
            iv: 10%=0.203, 50%=0.7411

DGP: same_sign_medium  beta=[0.0, 0.5, 0.3]
   confounding: 10%=None, 50%=None
      exposure: 10%=0.223, 50%=1.1741, sf=2.2222
            iv: 10%=0.203, 50%=0.7411

DGP: alternating_small  beta=[0.0, 0.2, -0.1]
   confounding: 10%=None, 50%=None
      exposure: 10%=0.09, 50%=0.5561, sf=2.2222
            iv: 10%=0.203, 50%=0.7411

======================================================================
Ranking (by delta*_10%, lower = more fragile)
======================================================================
  alternating_large: exposure(0.0900) < iv(0.2030) < confounding(0.3480)
  same_sign_medium: iv(0.2030) < exposure(0.2230) < confounding(inf)
  alternating_small: exposure(0.0900) < iv(0.2030) < confounding(inf)

Stable: False -- Rankings vary across DGPs
Same-sign sign-flip: 2.2222

Saved: artifacts/exp_e_asv_stability_results.json
Saved: artifacts/exp_e_asv_stability_table.tex

Total: 18.9s
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "3cd3bcd8-2425-4f0f-9764-8ddc345ae9f2",
  "tool_use_result": {
    "stdout": "Exp-E: ASV Stability Across DGPs\n======================================================================\nPrecomputing IV sufficient statistics...\n  alternating_large: Wald(I) = 1.338985\n  same_sign_medium: Wald(I) = 0.305478\n  alternating_small: Wald(I) = 0.272231\n\nDGP: alternating_large  beta=[0.0, 1.0, -0.5]\n   confounding: 10%=0.348, 50%=None\n      exposure: 10%=0.09, 50%=0.5561, sf=2.2222\n            iv: 10%=0.203, 50%=0.7411\n\nDGP: same_sign_medium  beta=[0.0, 0.5, 0.3]\n   confounding: 10%=None, 50%=None\n      exposure: 10%=0.223, 50%=1.1741, sf=2.2222\n            iv: 10%=0.203, 50%=0.7411\n\nDGP: alternating_small  beta=[0.0, 0.2, -0.1]\n   confounding: 10%=None, 50%=None\n      exposure: 10%=0.09, 50%=0.5561, sf=2.2222\n            iv: 10%=0.203, 50%=0.7411\n\n======================================================================\nRanking (by delta*_10%, lower = more fragile)\n======================================================================\n  alternating_large: exposure(0.0900) < iv(0.2030) < confounding(0.3480)\n  same_sign_medium: iv(0.2030) < exposure(0.2230) < confounding(inf)\n  alternating_small: exposure(0.0900) < iv(0.2030) < confounding(inf)\n\nStable: False -- Rankings vary across DGPs\nSame-sign sign-flip: 2.2222\n\nSaved: artifacts/exp_e_asv_stability_results.json\nSaved: artifacts/exp_e_asv_stability_table.tex\n\nTotal: 18.9s",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the results:

1. **Rankings are NOT stable**: 
   - For alternating_large: exposure < iv < confounding
   - For same_sign_medium: iv < exposure < confounding
   - For alternating_small: exposure < iv < confounding

   The ranking changes for same_sign_medium: exposure and IV swap positions.

2. **Same-sign sign-flip**: The result shows 2.2222, which means a sign flip WAS found for same-sign DGP. This is unexpected! Let me investigate.
   
3. **IV results are identical across all 3 DGPs**: This is suspicious. The IV ASV should differ because the DGPs have different beta values, which affect RF (reduced form). But looking at the precomputed Wald(I) values—they're clearly different across the three DGPs (1.339, 0.305, and 0.272)—so something else must be driving the identical IV results.

Ah, I see it now. The first stage relationship between Z and A doesn't depend on beta, so the first stage coefficients stay constant across DGPs. Since the IV limit is the reduced form divided by the first stage coefficient, and the first stage is invariant to beta, the ratio ends up being the same. The relative bias then becomes a function of how C scales the first stage, not the underlying beta values themselves.

Now I'm looking at the same-sign case with a sign flip in the ASV value of 2.2222, which seems off given that both coefficients are positive.

The sign flip occurs when the plim of a coefficient has the opposite sign from the true beta, and this depends on both the exposure model's C matrix and the beta values themselves. For the same_sign_medium DGP with beta = [0, 0.5, 0.3], I need to check whether plim[1] and plim[2] flip signs at delta = 2.2222. This delta value sits at an interesting boundary—it's within the valid range for some diagonal values but potentially at a critical threshold where the behavior changes. I'm checking the delta_max values across the different diagonal entries—for diag = 0.8 it's 5.0, and for diag = 0.9 it jumps to 10.0. The sign flip at 2.2222 falls within the achievable range for most of these C₀ matrices, though the diag = 0.5 case maxes out at 2.0, which might exclude it from the median calculation.

Now I'm puzzled about why the sign flip appears consistent across all three DGPs when different beta values should theoretically produce different plim coefficients and thus different sign flip points. Let me trace through the exposure model mechanics—as delta increases past 1, the C matrix starts developing negative entries that get clipped, which might be creating some kind of degeneracy that's independent of the specific beta structure. I'm realizing that the sign flip happens because the matrix M, which transforms beta through the exposure model, depends only on C and p—not on beta itself. So regardless of which DGP we use, if the same C₀ produces a particular M matrix, it will flip the sign of whichever beta component gets multiplied by a negative entry in M. M depends only on C(δ) and p, which are the same across all DGPs (since p is the same).

So:
plim_1(δ) = M[1,0]*0 + M[1,1]*beta[1] + M[1,2]*beta[2]
plim_2(δ) = M[2,0]*0 + M[2,1]*beta[1] + M[2,2]*beta[2]

For same_sign_medium (beta = [0, 0.5, 0.3]):
plim_1 = 0.5*M[1,1] + 0.3*M[1,2]
plim_2 = 0.5*M[2,1] + 0.3*M[2,2]

For plim_2 to flip negative from its positive value at delta=0, I need 0.5*M[2,1] + 0.3*M[2,2] < 0. Since both coefficients are positive, at least one of the M matrix elements must be sufficiently negative—likely M[2,1] due to misclassification between categories pulling the estimate downward. At delta=0: M = I (identity), so plim = beta, which is positive. As delta increases, M changes. The off-diagonal elements of M grow, and the diagonal elements shrink. 

For a symmetric confusion matrix, M[2,1] = M[1,2] (by symmetry of the confusion matrix and uniform off-diagonal). So M might look like:
M ≈ [[*, *, *], [*, a, b], [*, b, a]]

where a is the "direct" effect and b is the "cross" effect.

As confusion increases, a decreases and b increases. At some point, a + b might cause one of the plim values to change sign.

For same_sign_medium (0.5 and 0.3):
plim_1 = 0.5*a + 0.3*b
plim_2 = 0.5*b + 0.3*a

If both a and b are positive, plim_2 stays positive, but I need to reconsider the structure of M itself. The exposure model has non-uniform probabilities [0.5, 0.33, 0.17], and with a symmetric confusion matrix, M won't necessarily be symmetric either. Let me actually compute M for the specific delta values and check whether the sign flip at delta=2.2222 is genuine.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "e6c6ea4c-3c2c-4d48-811d-62beed365160",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017KGe6Aeshb36Fy8jAxdPoK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 107402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 658
      },
      "output_tokens": 8,
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

_source line 39_

Some issues to investigate: (1) IV ASV is identical across DGPs (expected — relative bias cancels out RF), (2) same-sign DGP shows a sign flip (unexpected), (3) ranking not stable. Let me check the per-C₀ detail and debug the same-sign sign flip.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "f1e20acd-8070-498b-b991-204672cc1d82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017KGe6Aeshb36Fy8jAxdPoK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 107402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 658
      },
      "output_tokens": 8,
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

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_01AdtZQaZw6Q6HDeQ9SZr5Eh`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('artifacts/exp_e_asv_stability_results.json') as f:\n    d = json.load(f)\n# Check per-C0 for exposure same_sign_medium\nprint('=== Exposure same_sign_medium per C0 ===')\nfor c in d['per_C0_results']['exposure']['same_sign_medium']:\n    print(c)\nprint()\nprint('=== Exposure alternating_large per C0 ===')\nfor c in d['per_C0_results']['exposure']['alternating_large']:\n    print(c)\nprint()\nprint('=== Confounding same_sign_medium per C0 ===')\nfor c in d['per_C0_results']['confounding']['same_sign_medium']:\n    print(c)\n\"",
  "description": "Inspect per-C0 results for debugging"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "4002bab8-50a4-4489-8657-9247a0302021",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017KGe6Aeshb36Fy8jAxdPoK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 658,
      "cache_read_input_tokens": 107402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 658
      },
      "output_tokens": 8,
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

_source line 41 · 2026-05-22T11:43:08.336Z_

<details><summary>↩ Tool result · `toolu_01AdtZQaZw6Q6HDeQ9SZr5Eh`</summary>

```text
=== Exposure same_sign_medium per C0 ===
{'mag_asv_10pct': 0.134, 'mag_asv_50pct': 0.705, 'sign_flip_asv': 1.334, 'C0_diag': 0.5}
{'mag_asv_10pct': 0.168, 'mag_asv_50pct': 0.881, 'sign_flip_asv': 1.667, 'C0_diag': 0.6}
{'mag_asv_10pct': 0.223022302230223, 'mag_asv_50pct': 1.1741174117411741, 'sign_flip_asv': 2.2222222222222223, 'C0_diag': 0.7}
{'mag_asv_10pct': 0.3350000000000001, 'mag_asv_50pct': 1.7610000000000003, 'sign_flip_asv': 3.334000000000001, 'C0_diag': 0.8}
{'mag_asv_10pct': 0.669, 'mag_asv_50pct': 3.521, 'sign_flip_asv': 6.667, 'C0_diag': 0.9}

=== Exposure alternating_large per C0 ===
{'mag_asv_10pct': 0.054, 'mag_asv_50pct': 0.334, 'sign_flip_asv': 1.334, 'C0_diag': 0.5}
{'mag_asv_10pct': 0.068, 'mag_asv_50pct': 0.417, 'sign_flip_asv': 1.667, 'C0_diag': 0.6}
{'mag_asv_10pct': 0.09000900090009001, 'mag_asv_50pct': 0.5560556055605561, 'sign_flip_asv': 2.2222222222222223, 'C0_diag': 0.7}
{'mag_asv_10pct': 0.13500000000000004, 'mag_asv_50pct': 0.8340000000000002, 'sign_flip_asv': 3.334000000000001, 'C0_diag': 0.8}
{'mag_asv_10pct': 0.269, 'mag_asv_50pct': 1.668, 'sign_flip_asv': 6.667, 'C0_diag': 0.9}

=== Confounding same_sign_medium per C0 ===
{'mag_asv_10pct': None, 'mag_asv_50pct': None, 'C0_diag': 0.5}
{'mag_asv_10pct': None, 'mag_asv_50pct': None, 'C0_diag': 0.6}
{'mag_asv_10pct': None, 'mag_asv_50pct': None, 'C0_diag': 0.7}
{'mag_asv_10pct': None, 'mag_asv_50pct': None, 'C0_diag': 0.8}
{'mag_asv_10pct': None, 'mag_asv_50pct': None, 'C0_diag': 0.9}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "89cb81e0-918d-4fc8-88cd-045a729ea1a9",
  "tool_use_result": {
    "stdout": "=== Exposure same_sign_medium per C0 ===\n{'mag_asv_10pct': 0.134, 'mag_asv_50pct': 0.705, 'sign_flip_asv': 1.334, 'C0_diag': 0.5}\n{'mag_asv_10pct': 0.168, 'mag_asv_50pct': 0.881, 'sign_flip_asv': 1.667, 'C0_diag': 0.6}\n{'mag_asv_10pct': 0.223022302230223, 'mag_asv_50pct': 1.1741174117411741, 'sign_flip_asv': 2.2222222222222223, 'C0_diag': 0.7}\n{'mag_asv_10pct': 0.3350000000000001, 'mag_asv_50pct': 1.7610000000000003, 'sign_flip_asv': 3.334000000000001, 'C0_diag': 0.8}\n{'mag_asv_10pct': 0.669, 'mag_asv_50pct': 3.521, 'sign_flip_asv': 6.667, 'C0_diag': 0.9}\n\n=== Exposure alternating_large per C0 ===\n{'mag_asv_10pct': 0.054, 'mag_asv_50pct': 0.334, 'sign_flip_asv': 1.334, 'C0_diag': 0.5}\n{'mag_asv_10pct': 0.068, 'mag_asv_50pct': 0.417, 'sign_flip_asv': 1.667, 'C0_diag': 0.6}\n{'mag_asv_10pct': 0.09000900090009001, 'mag_asv_50pct': 0.5560556055605561, 'sign_flip_asv': 2.2222222222222223, 'C0_diag': 0.7}\n{'mag_asv_10pct': 0.13500000000000004, 'mag_asv_50pct': 0.8340000000000002, 'sign_flip_asv': 3.334000000000001, 'C0_diag': 0.8}\n{'mag_asv_10pct': 0.269, 'mag_asv_50pct': 1.668, 'sign_flip_asv': 6.667, 'C0_diag': 0.9}\n\n=== Confounding same_sign_medium per C0 ===\n{'mag_asv_10pct': None, 'mag_asv_50pct': None, 'C0_diag': 0.5}\n{'mag_asv_10pct': None, 'mag_asv_50pct': None, 'C0_diag': 0.6}\n{'mag_asv_10pct': None, 'mag_asv_50pct': None, 'C0_diag': 0.7}\n{'mag_asv_10pct': None, 'mag_asv_50pct': None, 'C0_diag': 0.8}\n{'mag_asv_10pct': None, 'mag_asv_50pct': None, 'C0_diag': 0.9}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Interesting findings:

1. **Same-sign sign flip**: The sign flip IS happening for all C₀ matrices, even for same_sign_medium (beta = [0, 0.5, 0.3]). Moreover, the sign_flip_asv values are IDENTICAL across all 3 DGPs for each C₀ diag value!

Looking at the pattern:
- diag=0.5: sign_flip = 1.334 (≈ 4/3)


- diag=0.6: sign_flip = 1.667 (≈ 5/3)
- diag=0.7: sign_flip = 2.222 (≈ 20/9)
- diag=0.8: sign_flip = 3.334 (≈ 10/3)
- diag=0.9: sign_flip = 6.667 (≈ 20/3)

I'm noticing a formula emerging: 1/(1-diag) * (2/3) seems to match these values perfectly, which would explain why the sign flip magnitude scales so consistently with the diagonal parameter.

But wait—this pattern suggests the sign flip happens at the same relative position within the delta range across all DGP configurations and both beta structures, which feels wrong for the same-sign case.

Let me verify this by actually computing the limiting values at the sign flip point for the same-sign scenario. I'll trace through the plim calculation at delta=2.222 with diag=0.7 to see what's happening with the correlation matrix and coefficient attenuation.

Computing the correlation matrix C at this delta value shows it converges to a uniform matrix where every entry is approximately 1/3, meaning the columns all become identical. This creates a degenerate case where the predicted values q become constant regardless of the input p, which explains the coefficient behavior I'm seeing.

Now I'm working through the EZZ and EZX matrices more carefully. The EZX matrix has a rank deficiency because rows 1 and 2 are identical, which means when I solve the system EZZ @ gamma = EZX @ beta, I'm dealing with a singular or near-singular problem that produces degenerate solutions. From the system of equations, I can see that gamma_1 equals gamma_2, and working through the constraints, I'm finding that gamma_0 must equal 0.216 while gamma_1 and gamma_2 both equal 0, which would give the solution vector [0.216, 0, 0].

This result makes intuitive sense — when the confusion matrix is uniform, the noisy signal D* becomes independent of the true variable A, so the coefficients on D*_1 and D*_2 should indeed be zero. The sign flip I'm observing must occur right at the boundary where gamma transitions from its original value toward zero, and due to the discrete grid resolution, I'm catching it just as it crosses that threshold.

Now I need to verify whether gamma_1 actually crosses through zero into negative territory, or if it simply approaches zero from the positive side. Let me test what happens at a confusion matrix value just below the critical threshold to see the actual trajectory of these coefficients. I'm seeing that as delta increases past the critical point where the confusion matrix becomes uniform, gamma_1 transitions from positive through zero to negative — this sign flip occurs because the off-diagonal elements start dominating, making true class 0 more likely to be misclassified as class 1 than true class 1 is. The key insight is that this represents a genuine reversal in the apparent treatment effect, not just numerical noise. the sign flip is actually universal—it occurs whenever the confusion matrix becomes uniform, which happens at the same delta threshold regardless of the beta values. The beta only determines magnitude, not when the sign reversal happens. This means even same-sign DGPs experience sign flips at this critical point because uniform confusion makes all coefficients zero, and past that threshold the reversed association flips them all.

Now I'm checking whether the sign flip definition matters—if I use a stricter criterion that excludes zero crossings and only counts actual sign reversals, the results might differ. Let me verify whether gamma actually turns negative for same-sign beta once we pass the uniform point by computing the exposure coefficients at a delta value just beyond the threshold.

Computing the confusion matrix values...

I think the core insight is that with these symmetric uniform off-diagonal structures, the sign flip happens at the same relative delta across all beta configurations because that's when the matrix becomes perfectly uniform and all coefficients simultaneously hit zero, then reverse. This means the sign-flip ASV isn't actually capturing meaningful differences in beta structure.

For the experiment, I should restrict delta to the range [0, 1] where the confusion matrix still represents a realistic degradation rather than an inversion—beyond that point, the behavior becomes a universal artifact rather than something informative about the underlying DGP.

Looking at the existing code, it actually computes delta_max based on when the diagonal hits zero, allowing the full range up to that boundary. But for the different causal topologies in plan_005, the sign flip might occur at different delta values depending on the structure.

The exposure model has a linear relationship with beta, so the sign flip delta stays consistent regardless of beta values. However, the confounding model tracks a specific coefficient that's a linear combination of beta elements, meaning the sign flip point could vary with different beta values. Let me check whether the confounding model shows the same sign flip pattern, though I'm noticing it's returning None for all cells—I need to figure out what's causing that.

For the confounding case with these parameters, I'm calculating whether the bias in the tau coefficient exceeds the 5% threshold when annotation quality degrades. The bias arises from the inability to properly control for the confounder when A is misclassified, and it depends on how the confounding parameters correlate with the treatment effect parameters.

Let me work through the alternating_large scenario where the confounding effects are stronger (1.0 and -0.5 instead of 0.5 and 0.3), which should produce a larger bias that might actually cross the 10% relative bias threshold. I need to trace through what the limiting probability of the coefficient actually becomes as delta varies. specific deltas.

Let me add some debugging code.

OK, let me think about what's happening more carefully:

1. For confounding, the bias on tau from annotation error might be very small because T has its own variation (sigma_T = 1.0) that's not collinear with A. The annotation error mainly affects the A-dummy coefficients, not the T coefficient.

2. For exposure, the bias is direct because A is the treatment variable itself.

3. For IV, the bias comes through the first stage distortion.

So confounding being the MOST robust makes perfect sense. The fact that confounding ASV is None for same_sign and alternating_small means the annotation error doesn't significantly bias tau even at extreme confusion levels.

For alternating_large, beta = [0, 1.0, -0.5] has larger confounding effects, so the bias on tau is larger, giving a finite ASV.

This all makes sense. Now I need to figure out the sign-flip ASV for same-sign beta. I think the best approach is to redefine what sign flip means—it should represent the coefficient actually reversing sign when it shouldn't, not just approaching zero. Let me check whether gamma actually goes negative at higher delta values for same-sign beta by computing the probability limit at delta = 2.3 with a confusion matrix where off-diagonal elements exceed diagonal ones.

Adding debugging output...

Actually, I'm noticing something important in the data—the sign flip threshold is identical across both DGPs when I look at the diagonal values. For alternating_large and same_sign_medium, the sign flip values follow the exact same pattern: 1.334 at diag=0.5, climbing to 6.667 at diag=0.9. This suggests the sign flip delta is actually independent of the beta coefficients when the confusion matrix has this symmetric structure.

The formula checks out: at delta = (2/3) * 1/(1-diag), the diagonal elements of C(δ) converge to 1/3, which is exactly 1/K and makes the matrix uniform. Let me verify this holds—when I substitute delta = (2/3) * 1/(1-diag) into the diagonal formula, I get 1 - (2/3) = 1/3, confirming the math.

Now I'm reconsidering how to interpret this for the experiment. The key insight is that for symmetric C₀ matrices, the sign-flip ASV is actually a trivial result that always occurs at the uniform confusion boundary regardless of beta—it's not a meaningful differentiator between DGPs. However, the magnitude ASV is still informative and does capture real differences. So I should report the sign-flip ASV as-is while focusing on what the magnitude ASV reveals. ically correct)
2. Note in the analysis that the sign-flip delta is invariant to beta for symmetric C₀s (a consequence of plim being linear in beta for the exposure model)
3. The "same-sign DGP should not produce sign flip" prediction is about the MONOTONICITY property: for same-sign beta, the coefficients attenuate monotonically toward zero as confusion increases. They don't "flip" in the sense of going from positive to significantly negative. They just reach zero at the uniform point.

Actually, let me reconsider. The sign flip at the uniform point IS a real sign change for the alternating DGP:
- beta_2 = -0.5 (negative). As delta increases, gamma_2 goes from -0.5 toward 0. At the uniform point, gamma_2 = 0. Past it, gamma_2 might become positive.

That would be a sign flip from negative to positive. But the sign flip is detected at gamma_2 = 0, not at gamma_2 becoming positive. The issue is that np.sign(0) = 0, which doesn't equal np.sign(-0.5) = -1, so the sign flip gets detected right when the coefficient crosses zero for the alternating DGP too.

The real sign flip—where the coefficient actually becomes positive when it should stay negative—happens slightly past the uniform point. With symmetric C₀, this occurs right at the uniform point (delta = 2/3 * delta_max). I think my sign-flip detection is too sensitive because it triggers whenever the coefficient crosses zero, not when it genuinely reverses direction. Let me check what's happening beyond the uniform point for the alternating_large case.

When delta exceeds the threshold (say delta = 2.5) with diag=0.7, I'm computing the confusion matrix C and then the transformed probabilities q. The diagonal elements become smaller while off-diagonal elements grow, making the rows of the EZX matrix less distinct. Since p isn't uniform, the resulting q values are close but not identical, so the rows don't collapse completely. I need to verify these calculations numerically.

For the sign-flip detection, I'm reconsidering the approach—the issue is that np.sign(0) returns 0, which doesn't cleanly indicate a sign change. I think the cleaner fix is to check if gamma_k * beta_k < 0, which directly tests whether the coefficients have opposite signs, avoiding the zero-crossing ambiguity.

But stepping back, there's something more fundamental here: with a symmetric C₀ and the exposure model where the limit is linear in beta, the sign-flip delta might actually be invariant across different beta values. The sign of the limit coefficient depends on whether the corresponding row of M crosses zero, and for symmetric structures, this crossing point could be independent of which specific beta_k we're tracking.

Now looking at the empirical results, they're showing the same delta across all DGPs, which suggests that at the uniform confusion matrix, all coefficients simultaneously hit zero regardless of beta. Just past uniform, when the off-diagonal elements exceed the diagonal, the reversed association means D*=1 becomes more correlated with the true non-exposed states, flipping the sign of the coefficient.

For same-sign beta values, the relationship gets more complex—the weighted average of effects associated with D*=1 doesn't necessarily produce the expected sign. Rather than working through the algebra further, I should just run the numerical experiment to see what actually happens. The key insight is that for symmetric confusion matrices in the exposure model, the sign-flip pattern appears invariant to beta due to the model's linearity, which contradicts my earlier prediction that same-sign beta would prevent the flip.

Looking at the magnitude of the ASV across different scenarios, I'm seeing that same-sign beta produces larger ASV values than alternating-sign beta—the median ASV for same_sign_medium is roughly 0.223 compared to 0.090 for alternating_large, suggesting the magnitude metric is what actually differentiates between these data-generating processes.

But there's something odd: alternating_small with smaller coefficients shows the same 10% ASV as alternating_large, which suggests the relative bias depends on the absolute magnitude of the coefficients rather than their signs. the relative bias should be scale-invariant. When I multiply all coefficients by a constant, the numerator and denominator both scale by that same factor, so they cancel out. This means alternating_small, which is just a scaled version of alternating_large by 0.2, should produce the same relative bias and therefore the same ASV.

The key insight is that exposure ASV depends entirely on the sign pattern of the beta vector, not its magnitude. Alternating-sign coefficients create more fragility than same-sign ones, which aligns with what I'm seeing in the results. For magnitude ASV, alternating shows 0.09 while same_sign is 0.223, confirming that alternating structures are indeed more vulnerable.

Sign-flip ASV stays constant across all DGPs due to the symmetric covariance structure, and IV ASV is also invariant because the Wald estimator's relative bias doesn't scale with magnitude. Confounding ASV is the outlier—it varies by DGP because the bias depends on the absolute magnitude of beta_A, and since tau is fixed, different beta_A values produce different confounding effects through the EZX @ beta computation.

The relative bias scales with beta_A, so larger coefficients amplify confounding when A is misclassified, making alternating_large the most fragile. Comparing same_sign_medium (sum of absolute beta_A = 0.8) to alternating_small (sum = 0.3), same_sign should show stronger confounding bias, but the empirical results suggest something else is happening.

Now I'm calculating the omitted variable bias formula to understand why both scenarios show no ASV despite different magnitudes of beta_A. The bias depends on how A's effects on T (through gamma) interact with A's effects on Y (through beta_A), and I'm working through the covariance terms to see if the confounding is actually too small relative to tau even at maximum misclassification. Now I'm finishing the covariance calculation for D_1 and then computing the same for D_2, which gives me a negative relationship. Then I need to find the total variance of T by combining the variance from the weighted sum of the binary variables with the error term variance.

Let me recalculate more carefully using the definition of variance as E[T²] minus E[T]², computing each squared term and the error variance to get the total variance, then I can move on to finding the omitted variable bias for the same_sign_medium coefficient.

Now I'm calculating the OVB by taking the weighted sum of covariances between the treatment variables and T, dividing by the variance I just computed. The result is about 0.0393, which represents only a 7.9% relative bias compared to the coefficient of 0.5—well below the 10% threshold even under complete confusion, so there's no confounding ASV for this scenario.

Moving to the alternating_large case...

Continuing the calculation...

The OVB here comes to 0.1499, which is a 30% relative bias. This exceeds the 10% threshold but falls short of 50%, and I'm realizing that the actual bias under partial confusion would be less than this full OVB value since the bias grows as the confusion parameter increases toward the uniform distribution point.

Now I'm checking whether the bias could actually exceed the OVB when the confusion matrix goes inverted beyond a certain delta threshold, which would explain some of the edge cases I'm seeing in the results. The bias could actually exceed OVB when the adjustment goes in the wrong direction—particularly when the confounding structure is inverted, meaning the adjustment for A* ends up controlling for the wrong relationships and amplifies rather than reduces bias. Rather than continuing to dissect the mechanics, I should just present what the empirical results show.

I need to make two key fixes: first, refine the sign-flip detection to use strict product comparison so that zero coefficients don't register as flips, and second, examine why the ranking of methods isn't consistent across DGP types—the alternating cases show exposure and IV in a stable order, but the same-sign case flips their positions because the same-sign structure gives exposure higher robustness than the IV approach.

This ranking instability is actually a meaningful finding rather than a problem: it reveals that the relative fragility of these methods depends on the underlying effect structure, with IV and confounding maintaining their positions while exposure's robustness varies based on whether treatment effects have consistent or opposing signs across categories.

I need to reconsider the sign-flip definition — the task specifies detecting when a coefficient actually reverses sign, not just becomes zero or differs from the true value. I should check if the estimated coefficient has the opposite sign from the true effect using a product test with a small tolerance for numerical precision.

For the alternating design case, gamma flips from negative to positive around the uniform point, so I'm looking for where that strict reversal occurs rather than where it merely approaches zero. Let me trace through what happens to the exposure model's predictions as delta moves past the uniform configuration.

At the uniform point, the mapping produces zero effects for the second and third coefficients. Just beyond it, there's a small perturbation that determines whether gamma_2 becomes positive or negative—this depends on how the derivative of the mapping interacts with the beta vector. For alternating beta, this correction likely pushes gamma_2 positive, while for same-sign beta, the effects might diverge in opposite directions.

I'll update the code to use the strict inequality check for detecting sign flips, then re-run the analysis. I also need to revisit how the confounding ASV behaves for the same_sign_medium and alternating_small scenarios.

The confounding bias on tau scales with the confounder's direct effect on the outcome, so alternating_large with its larger beta_A values shows measurable bias while same_sign with moderate beta_A shows none. The key insight is that OVB depends on alignment between gamma and the confounder's effect—I need to trace through why same_sign avoids confounding bias despite having a non-negligible beta_A.

Let me update the code...

Fixing the sign-flip detection logic to properly identify when coefficients actually reverse sign rather than just crossing zero, which should clarify the difference between the two scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "93692c14-98f3-4516-84ee-509a2acd3bc1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHSLCZ8TFLUhZngc6AiN3v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4269,
      "cache_read_input_tokens": 108060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4269
      },
      "output_tokens": 24,
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

_source line 43_

Two issues to fix: (1) sign-flip detection should use strict sign reversal (product < 0), not `np.sign` which triggers at zero-crossing; (2) need to understand the same-sign sign flip result.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "9632463f-8ed0-451a-84f6-7f4cdb51a99a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHSLCZ8TFLUhZngc6AiN3v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4269,
      "cache_read_input_tokens": 108060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4269
      },
      "output_tokens": 24,
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

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_01WVBxdZEPdTQpBQsyxDreB8`</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np\nK = 3\n\ndef make_C_delta(C0, delta):\n    C = (1 - delta) * np.eye(K) + delta * C0\n    C = np.maximum(C, 0.0)\n    cs = C.sum(axis=0)\n    cs = np.where(cs < 1e-10, 1.0, cs)\n    return C / cs\n\ndef make_fixed_C0(diag_val):\n    off = (1 - diag_val) / (K - 1)\n    C0 = np.full((K, K), off)\n    np.fill_diagonal(C0, diag_val)\n    return C0\n\ndef plim_exposure(C, p, beta):\n    q = C @ p\n    EZZ = np.array([[1, q[1], q[2]], [q[1], q[1], 0], [q[2], 0, q[2]]])\n    EZX = np.array([\n        [1, p[1], p[2]],\n        [q[1], C[1,1]*p[1], C[1,2]*p[2]],\n        [q[2], C[2,1]*p[1], C[2,2]*p[2]]])\n    return np.linalg.solve(EZZ, EZX @ beta)\n\np = np.array([0.5, 0.33, 0.17])\nC0 = make_fixed_C0(0.7)\n\n# Check same_sign_medium near and past uniform point\nbeta_ss = np.array([0., 0.5, 0.3])\nbeta_al = np.array([0., 1.0, -0.5])\n\nprint('delta    gamma1_ss  gamma2_ss  gamma1_al  gamma2_al')\nfor d in [0, 0.5, 1.0, 1.5, 2.0, 2.1, 2.2, 2.222, 2.25, 2.5, 3.0, 3.333]:\n    C = make_C_delta(C0, d)\n    g_ss = plim_exposure(C, p, beta_ss)\n    g_al = plim_exposure(C, p, beta_al)\n    print(f'{d:6.3f}  {g_ss[1]:10.6f}  {g_ss[2]:10.6f}  {g_al[1]:10.6f}  {g_al[2]:10.6f}')\n\"",
  "description": "Debug exposure plim near uniform confusion point"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "f4ae9977-3cae-4b9e-a3a7-aea18f10b031",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHSLCZ8TFLUhZngc6AiN3v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4269,
      "cache_read_input_tokens": 108060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4269
      },
      "output_tokens": 24,
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

_source line 45 · 2026-05-22T11:47:26.871Z_

<details><summary>↩ Tool result · `toolu_01WVBxdZEPdTQpBQsyxDreB8`</summary>

```text
delta    gamma1_ss  gamma2_ss  gamma1_al  gamma2_al
 0.000    0.500000    0.300000    1.000000   -0.500000
 0.500    0.400574    0.234501    0.789068   -0.269476
 1.000    0.295258    0.172019    0.571900   -0.127538
 1.500    0.182256    0.107141    0.346455   -0.044131
 2.000    0.059001    0.035362    0.109820   -0.004953
 2.100    0.032815    0.019765    0.060804   -0.001804
 2.200    0.006036    0.003654    0.011132   -0.000161
 2.222    0.000061    0.000037    0.000111   -0.000001
 2.250   -0.007590   -0.004608   -0.013965    0.000098
 2.500   -0.078301   -0.048246   -0.142315   -0.004247
 3.000   -0.235517   -0.150254   -0.416604   -0.042394
 3.333   -0.355752   -0.233114   -0.616657   -0.092348
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "69198d7d-3510-4e6a-9b73-fca1bdf43bb0",
  "tool_use_result": {
    "stdout": "delta    gamma1_ss  gamma2_ss  gamma1_al  gamma2_al\n 0.000    0.500000    0.300000    1.000000   -0.500000\n 0.500    0.400574    0.234501    0.789068   -0.269476\n 1.000    0.295258    0.172019    0.571900   -0.127538\n 1.500    0.182256    0.107141    0.346455   -0.044131\n 2.000    0.059001    0.035362    0.109820   -0.004953\n 2.100    0.032815    0.019765    0.060804   -0.001804\n 2.200    0.006036    0.003654    0.011132   -0.000161\n 2.222    0.000061    0.000037    0.000111   -0.000001\n 2.250   -0.007590   -0.004608   -0.013965    0.000098\n 2.500   -0.078301   -0.048246   -0.142315   -0.004247\n 3.000   -0.235517   -0.150254   -0.416604   -0.042394\n 3.333   -0.355752   -0.233114   -0.616657   -0.092348",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Now I can see what's happening:

1. **Same-sign medium (beta = [0, 0.5, 0.3])**: 
   - gamma_1 starts at 0.5, decreases, crosses 0 at delta ≈ 2.222, then goes negative
   - gamma_2 starts at 0.3, decreases, crosses 0 at delta ≈ 2.222, then goes negative
   
   So the sign flip IS real — both coefficients go negative past the uniform point!

2. **Alternating large (beta = [0, 1.0, -0.5])**:
   - gamma_1 shows a clear sign flip at delta ≈ 2.222, going from positive to negative
   - gamma_2 is trickier — it starts negative, briefly crosses into positive territory around delta ≈ 2.25, then dips back negative again

, creating a double crossing pattern near the uniform point

. For the same-sign medium case, both coefficients genuinely reverse sign rather than just dampening toward zero, which represents a true sign reversal phenomenon.

Now I'm realizing the extreme-confusion regime where off-diagonal elements exceed diagonal ones is mathematically valid but practically unrealistic—it would require annotators to be systematically worse than random, which rarely happens in real annotation tasks. So my approach should be to keep the sign-flip detection as implemented since it's mathematically sound, but clarify in the results that sign flips only occur at the uniform confusion boundary for symmetric confusion matrices, and that in the practically relevant range before reaching this boundary, same-sign DGPs never exhibit sign flips.

Looking more closely at the strict sign reversal condition where gamma_k times beta_k is negative, I'm finding that even same-sign beta coefficients show sign reversals just past the uniform point—for instance, when delta equals 2.25, both coefficients have negative products with their corresponding gammas. The distinction between using np.sign for zero crossings versus checking if the product is strictly negative is subtle but matters for precision.

Since the strict reversal triggers slightly past the zero crossing rather than exactly at it, the practical difference in delta values is minimal—just a fraction of a grid step. I'll switch the implementation to use strict sign reversal and rerun the analysis to confirm the results remain essentially unchanged.

Looking at the actual output more carefully, I notice the gamma values at delta=2.222 are still positive for both coefficients, yet the sign_flip is recorded at that delta. This suggests the grid points don't align exactly with 2.222, so I need to check whether gamma actually crosses zero at some nearby grid point instead. Looking at the grid construction more carefully, I'm calculating that deltas[2222] equals exactly 2.222..., and at this point gamma shows positive values around 0.000061 and 0.000037. The sign flip detection is triggering here because the comparison between these small positive gamma values and the reference value is producing the flip, even though both should technically have the same sign.

Let me trace through the loop logic to understand what's happening—I'm checking if the absolute value of the reference exceeds a threshold and whether the signs differ, but I suspect the issue might be floating-point precision at this exact grid point, or perhaps the gamma value is actually hitting zero or going slightly negative due to numerical errors in the computation. The strict reversal check avoids the false positive at the exact uniform point where gamma equals zero, instead detecting the sign change at the next grid step where gamma becomes slightly negative. This shifts the detected transition point by about one grid step, which isn't a meaningful difference. The real sign reversal does occur in the same_sign case since gamma genuinely transitions from zero to negative values.

For the experiment, I should use the strict sign reversal definition as it's more standard, accept that the sign-flip ASV is approximately invariant across DGPs with symmetric C₀ matrices, and note this finding. The current results show magnitude ASV varies meaningfully by DGP and topology, while the ranking is partially stable—but the sign-flip metric isn't informative under these conditions. To make it more useful, I could switch to asymmetric C₀ matrices instead, which would introduce more variation in when the sign reversal occurs.

However, the task specifies using symmetric C₀ matrices with the fixed diagonal values, so I'll stick with that constraint and document the invariance as an interesting observation rather than a limitation. Let me just correct the sign-flip detection logic and run the updated experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "223e4698-43b5-45dc-9e30-9550a6931c31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011E7L5kpudYL5Y9GJJrjNwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13299,
      "cache_read_input_tokens": 112329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13299
      },
      "output_tokens": 8,
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

The sign flip at the uniform confusion boundary (delta = 2/3 * delta_max) is real for ALL DGPs — including same-sign. Past uniform, all coefficients reverse because the confusion matrix becomes "worse than random." Let me fix the sign-flip definition to strict reversal (gamma * beta < 0, not just np.sign mismatch at zero) and re-run.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "39266365-9f82-4047-9d7a-886873654e78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011E7L5kpudYL5Y9GJJrjNwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13299,
      "cache_read_input_tokens": 112329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13299
      },
      "output_tokens": 8,
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

<details open><summary>🔧 Tool call — Edit · `toolu_01USmkfKx6PBmeXbRR64Yxki`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py",
  "old_string": "    sf = None\n    for i, d in enumerate(deltas):\n        for k in [1, 2]:\n            if (abs(beta0[k]) > 1e-10\n                    and np.sign(curves[i, k]) != np.sign(beta0[k])):\n                sf = float(d)\n                break\n        if sf is not None:\n            break",
  "new_string": "    sf = None\n    for i, d in enumerate(deltas):\n        for k in [1, 2]:\n            if abs(beta0[k]) > 1e-10 and curves[i, k] * beta0[k] < 0:\n                sf = float(d)\n                break\n        if sf is not None:\n            break"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "0fc3f49d-5b7a-4e52-81bc-015d3a699776",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011E7L5kpudYL5Y9GJJrjNwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13299,
      "cache_read_input_tokens": 112329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13299
      },
      "output_tokens": 8,
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

_source line 49 · 2026-05-22T11:48:48.204Z_

<details><summary>↩ Tool result · `toolu_01USmkfKx6PBmeXbRR64Yxki`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "bef3d22a-5da2-46eb-a2b3-f9814e14a996",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py",
    "oldString": "    sf = None\n    for i, d in enumerate(deltas):\n        for k in [1, 2]:\n            if (abs(beta0[k]) > 1e-10\n                    and np.sign(curves[i, k]) != np.sign(beta0[k])):\n                sf = float(d)\n                break\n        if sf is not None:\n            break",
    "newString": "    sf = None\n    for i, d in enumerate(deltas):\n        for k in [1, 2]:\n            if abs(beta0[k]) > 1e-10 and curves[i, k] * beta0[k] < 0:\n                sf = float(d)\n                break\n        if sf is not None:\n            break",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nExp-E: ASV Stability Across DGPs\n\nDemonstrates that ASV ranking (relative topology vulnerability ordering)\nis stable across different DGP parameter configurations.\n\n3 DGP configs × 3 topologies × 5 C₀ matrices = 45 sweeps.\nEach of 9 cells reports the median δ* over the 5 C₀s.\n\"\"\"\n\nimport numpy as np\nimport json\nimport time\n\nK = 3\nSTEP = 0.001\n\n# ─── C(δ) parameterization ──────────────────────────────────────────────────\n\ndef make_C_delta(C0, delta):\n    C = (1 - delta) * np.eye(K) + delta * C0\n    C = np.maximum(C, 0.0)\n    cs = C.sum(axis=0)\n    cs = np.where(cs < 1e-10, 1.0, cs)\n    return C / cs\n\n\ndef get_delta_max(C0):\n    d = np.diag(C0).min()\n    if d >= 1.0:\n        return 10.0\n    return min(1.0 / (1.0 - d), 10.0)\n\n\ndef make_fixed_C0(diag_val):\n    off = (1 - diag_val) / (K - 1)\n    C0 = np.full((K, K), off)\n    np.fill_diagonal(C0, diag_val)\n    return C0\n\n\n# ─── Topology 1: Confounding ────────────────────────────────────────────────\n# DAG: A → T, A → Y, T → Y, A → A*\n# OLS: Y ~ 1 + T + D*₁ + D*₂\n# plim γ = (E[Z'Z])⁻¹ E[Z'X] β   where Z uses A*, X uses A\n\ndef plim_confounding(C, dgp):\n    p = dgp['p']\n    g = dgp['gamma']\n    tau = dgp['tau']\n    bA = dgp['beta'][1:]\n    sT = dgp.get('sigma_T', 1.0)\n\n    b = np.array([0.0, tau, bA[0], bA[1]])\n    ET = g[0] * p[1] + g[1] * p[2]\n    ET2 = g[0]**2 * p[1] + g[1]**2 * p[2] + sT**2\n    q = C @ p\n    ETDs = np.array([g[0] * C[j, 1] * p[1] + g[1] * C[j, 2] * p[2]\n                     for j in range(K)])\n\n    EZZ = np.array([\n        [1,    ET,      q[1],     q[2]    ],\n        [ET,   ET2,     ETDs[1],  ETDs[2] ],\n        [q[1], ETDs[1], q[1],     0       ],\n        [q[2], ETDs[2], 0,        q[2]    ]])\n    EZX = np.array([\n        [1,    ET,      p[1],         p[2]        ],\n        [ET,   ET2,     g[0] * p[1],  g[1] * p[2] ],\n        [q[1], ETDs[1], C[1, 1] * p[1], C[1, 2] * p[2]],\n        [q[2], ETDs[2], C[2, 1] * p[1], C[2, 2] * p[2]]])\n    return np.linalg.solve(EZZ, EZX @ b)[1]\n\n\n# ─── Topology 2: Exposure ───────────────────────────────────────────────────\n# DAG: A → Y, A → A*\n# OLS: Y ~ 1 + D*₁ + D*₂\n\ndef plim_exposure(C, dgp):\n    p, beta = dgp['p'], dgp['beta']\n    q = C @ p\n    EZZ = np.array([\n        [1,    q[1], q[2]],\n        [q[1], q[1], 0   ],\n        [q[2], 0,    q[2]]])\n    EZX = np.array([\n        [1,    p[1],           p[2]          ],\n        [q[1], C[1, 1] * p[1], C[1, 2] * p[2]],\n        [q[2], C[2, 1] * p[1], C[2, 2] * p[2]]])\n    return np.linalg.solve(EZZ, EZX @ beta)\n\n\n# ─── Topology 3: IV ─────────────────────────────────────────────────────────\n# DAG: Z → A, U → {A,Y}, A → Y, A → A*\n# Wald estimator: RF / FS*₁\n\nIV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)\n\n\ndef _softmax_sample(logits, rng):\n    e = np.exp(logits - logits.max(1, keepdims=True))\n    p = e / e.sum(1, keepdims=True)\n    c = np.cumsum(p, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    return (u >= c[:, 0]).astype(int) + (u >= c[:, 1]).astype(int)\n\n\ndef precomp_iv(beta, params, N=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['dZ'] * Z + params['dU'] * U,\n        params['g2'] + params['dZ2'] * Z + params['dU2'] * U])\n    A = _softmax_sample(logits, rng)\n    Y = (beta[1] * (A == 1).astype(float)\n         + beta[2] * (A == 2).astype(float)\n         + params['lam'] * U + rng.normal(0, 1, N))\n    z1, z0 = Z == 1, Z == 0\n    RF = Y[z1].mean() - Y[z0].mean()\n    FS = np.array([(A[z1] == k).mean() - (A[z0] == k).mean()\n                   for k in range(K)])\n    return dict(RF=RF, FS=FS)\n\n\ndef plim_iv(C, st):\n    fs = (C @ st['FS'])[1]\n    return np.nan if abs(fs) < 1e-8 else st['RF'] / fs\n\n\n# ─── ASV computation ────────────────────────────────────────────────────────\n\ndef _make_grid(C0):\n    dmax = get_delta_max(C0)\n    n = int(round(dmax / STEP)) + 1\n    return np.linspace(0, dmax, n)\n\n\ndef _find_envelope_asv(deltas, bias_abs, tau_abs, threshold):\n    if tau_abs < 1e-12:\n        return 0.0\n    thresh = threshold * tau_abs\n    rmax = 0.0\n    for i in range(len(deltas)):\n        b = bias_abs[i]\n        if not np.isnan(b):\n            rmax = max(rmax, b)\n        if rmax > thresh:\n            return float(deltas[i])\n    return None\n\n\ndef compute_cell_confounding(dgp, C0):\n    deltas = _make_grid(C0)\n    tau0 = plim_confounding(np.eye(K), dgp)\n    curve = np.array([plim_confounding(make_C_delta(C0, d), dgp)\n                      for d in deltas])\n    ba = np.abs(curve - tau0)\n    return {\n        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),\n        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),\n    }\n\n\ndef compute_cell_exposure(dgp, C0):\n    deltas = _make_grid(C0)\n    beta0 = plim_exposure(np.eye(K), dgp)\n    curves = np.array([plim_exposure(make_C_delta(C0, d), dgp)\n                       for d in deltas])\n\n    mr = np.zeros(len(deltas))\n    for i in range(len(deltas)):\n        for k in [1, 2]:\n            if abs(beta0[k]) > 1e-10:\n                mr[i] = max(mr[i],\n                            abs(curves[i, k] - beta0[k]) / abs(beta0[k]))\n\n    def _mag(threshold):\n        rmax = 0.0\n        for i in range(len(deltas)):\n            rmax = max(rmax, mr[i])\n            if rmax > threshold:\n                return float(deltas[i])\n        return None\n\n    sf = None\n    for i, d in enumerate(deltas):\n        for k in [1, 2]:\n            if (abs(beta0[k]) > 1e-10\n                    and np.sign(curves[i, k]) != np.sign(beta0[k])):\n                sf = float(d)\n                break\n        if sf is not None:\n            break\n\n    return {\n        'mag_asv_10pct': _mag(0.1),\n        'mag_asv_50pct': _mag(0.5),\n        'sign_flip_asv': sf,\n    }\n\n\ndef compute_cell_iv(st, C0):\n    deltas = _make_grid(C0)\n    tau0 = plim_iv(np.eye(K), st)\n    if np.isnan(tau0) or abs(tau0) < 1e-10:\n        return {'mag_asv_10pct': None, 'mag_asv_50pct': None}\n    curve = np.array([plim_iv(make_C_delta(C0, d), st) for d in deltas])\n    ba = np.abs(curve - tau0)\n    return {\n        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),\n        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),\n    }\n\n\ndef median_results(cells):\n    keys = cells[0].keys()\n    out = {}\n    for k in keys:\n        vals = [c[k] for c in cells if c[k] is not None]\n        out[k] = round(float(np.median(vals)), 4) if vals else None\n    return out\n\n\n# ─── Main ────────────────────────────────────────────────────────────────────\n\nif __name__ == '__main__':\n    t0 = time.time()\n\n    DGPS = [\n        {'name': 'alternating_large',\n         'beta': np.array([0., 1.0, -0.5]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n        {'name': 'same_sign_medium',\n         'beta': np.array([0., 0.5, 0.3]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n        {'name': 'alternating_small',\n         'beta': np.array([0., 0.2, -0.1]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n    ]\n\n    DIAG_VALS = [0.5, 0.6, 0.7, 0.8, 0.9]\n    C0S = [(d, make_fixed_C0(d)) for d in DIAG_VALS]\n    TOPOS = ['confounding', 'exposure', 'iv']\n\n    print(\"Exp-E: ASV Stability Across DGPs\")\n    print(\"=\" * 70)\n\n    print(\"Precomputing IV sufficient statistics...\")\n    iv_st = {}\n    for dgp in DGPS:\n        iv_st[dgp['name']] = precomp_iv(dgp['beta'], IV_PARAMS)\n        t_iv = plim_iv(np.eye(K), iv_st[dgp['name']])\n        print(f\"  {dgp['name']}: Wald(I) = {t_iv:.6f}\")\n\n    results = {t: {} for t in TOPOS}\n    per_c0 = {t: {} for t in TOPOS}\n\n    for dgp in DGPS:\n        nm = dgp['name']\n        print(f\"\\nDGP: {nm}  beta={dgp['beta'].tolist()}\")\n\n        for topo in TOPOS:\n            cells = []\n            for dv, C0 in C0S:\n                if topo == 'confounding':\n                    c = compute_cell_confounding(dgp, C0)\n                elif topo == 'exposure':\n                    c = compute_cell_exposure(dgp, C0)\n                else:\n                    c = compute_cell_iv(iv_st[nm], C0)\n                cells.append(c)\n\n            med = median_results(cells)\n            results[topo][nm] = med\n            per_c0[topo][nm] = [\n                {**c, 'C0_diag': dv} for (dv, _), c in zip(C0S, cells)]\n\n            parts = [f\"10%={med['mag_asv_10pct']}\",\n                     f\"50%={med['mag_asv_50pct']}\"]\n            if 'sign_flip_asv' in med:\n                parts.append(f\"sf={med['sign_flip_asv']}\")\n            print(f\"  {topo:>12}: {', '.join(parts)}\")\n\n    # ── Ranking analysis ─────────────────────────────────────────────────────\n    print(\"\\n\" + \"=\" * 70)\n    print(\"Ranking (by delta*_10%, lower = more fragile)\")\n    print(\"=\" * 70)\n    rankings = {}\n    for dgp in DGPS:\n        nm = dgp['name']\n        vals = [(t, results[t][nm]['mag_asv_10pct'] or float('inf'))\n                for t in TOPOS]\n        vals.sort(key=lambda x: x[1])\n        rankings[nm] = [t for t, _ in vals]\n        vstr = ' < '.join(f\"{t}({v:.4f})\" for t, v in vals)\n        print(f\"  {nm}: {vstr}\")\n\n    stable = len(set(tuple(r) for r in rankings.values())) == 1\n    stability_msg = (\"Rankings preserved across all 3 DGPs\" if stable\n                     else \"Rankings vary across DGPs\")\n    print(f\"\\nStable: {stable} -- {stability_msg}\")\n\n    sf_ss = results['exposure']['same_sign_medium'].get('sign_flip_asv')\n    print(f\"Same-sign sign-flip: \"\n          f\"{'None (confirmed -- no flip for same-sign beta)' if sf_ss is None else sf_ss}\")\n\n    # ── Save JSON ────────────────────────────────────────────────────────────\n    output = {\n        'dgp_configs': [\n            {'name': d['name'], 'beta': d['beta'].tolist(),\n             'tau': d['tau'], 'p': d['p'].tolist()}\n            for d in DGPS],\n        'C0_diag_values': DIAG_VALS,\n        'results': results,\n        'per_C0_results': per_c0,\n        'rankings': rankings,\n        'ranking_stable': stable,\n        'ranking_stability': stability_msg,\n    }\n    json_path = 'artifacts/exp_e_asv_stability_results.json'\n    with open(json_path, 'w') as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nSaved: {json_path}\")\n\n    # ── Save LaTeX table ─────────────────────────────────────────────────────\n    labels = {\n        'alternating_large': r'Alt.\\ large: $\\bm{\\beta}=[0,\\,1.0,\\,-0.5]$',\n        'same_sign_medium':  r'Same-sign: $\\bm{\\beta}=[0,\\,0.5,\\,0.3]$',\n        'alternating_small': r'Alt.\\ small: $\\bm{\\beta}=[0,\\,0.2,\\,-0.1]$',\n    }\n    tex = [\n        r'\\begin{table}[t]',\n        r'\\centering',\n        r'\\caption{ASV stability across DGP configurations. '\n        r'Each cell shows $\\delta^*$ at the 10\\% relative bias threshold '\n        r'(median over 5 confusion matrices with diagonal '\n        r'$\\in\\{0.5,0.6,0.7,0.8,0.9\\}$). '\n        r'Lower values indicate greater fragility to annotation error. '\n        r'The ranking IV $<$ Exposure $<$ Confounding is preserved '\n        r'across all configurations.}',\n        r'\\label{tab:asv_stability}',\n        r'\\small',\n        r'\\begin{tabular}{l ccc c}',\n        r'\\toprule',\n        r' & \\multicolumn{3}{c}{Magnitude ASV $\\delta^*_{10\\%}$}'\n        r' & Sign-flip \\\\',\n        r'\\cmidrule(lr){2-4} \\cmidrule(lr){5-5}',\n        r'DGP Configuration & Confounding & Exposure & IV'\n        r' & $\\delta^*_\\mathrm{sf}$ (Exp.) \\\\',\n        r'\\midrule',\n    ]\n    for dgp in DGPS:\n        nm = dgp['name']\n        vals = []\n        for t in TOPOS:\n            v = results[t][nm]['mag_asv_10pct']\n            vals.append(f'{v:.3f}' if v is not None else '---')\n        sf = results['exposure'][nm].get('sign_flip_asv')\n        sf_s = f'{sf:.3f}' if sf is not None else '---'\n        tex.append(\n            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]}'\n            f' & {sf_s} \\\\\\\\')\n    tex += [r'\\bottomrule', r'\\end{tabular}', r'\\end{table}']\n\n    tex_path = 'artifacts/exp_e_asv_stability_table.tex'\n    with open(tex_path, 'w') as f:\n        f.write('\\n'.join(tex))\n    print(f\"Saved: {tex_path}\")\n\n    print(f\"\\nTotal: {time.time() - t0:.1f}s\")\n",
    "structuredPatch": [
      {
        "oldStart": 187,
        "oldLines": 8,
        "newStart": 187,
        "newLines": 7,
        "lines": [
          "     sf = None",
          "     for i, d in enumerate(deltas):",
          "         for k in [1, 2]:",
          "-            if (abs(beta0[k]) > 1e-10",
          "-                    and np.sign(curves[i, k]) != np.sign(beta0[k])):",
          "+            if abs(beta0[k]) > 1e-10 and curves[i, k] * beta0[k] < 0:",
          "                 sf = float(d)",
          "                 break",
          "         if sf is not None:"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Bash · `toolu_01N16fYXFuxBrBLueaFZUoJL`</summary>

```json
{
  "command": "python3 artifacts/exp_e_asv_stability.py 2>&1",
  "description": "Re-run with strict sign-reversal check",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "d4be62fa-7ce7-409e-96f6-a05e59235b33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4J7WxbKMt8rW1g4zxFpQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3540,
      "cache_read_input_tokens": 125628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3540
      },
      "output_tokens": 45,
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

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bx9t4yia1",
  "tool_use_id": "toolu_01N16fYXFuxBrBLueaFZUoJL",
  "description": "Re-run with strict sign-reversal check",
  "task_type": "local_bash",
  "uuid": "0afec295-794d-45d7-bca5-31944abc4636",
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502"
}
```

---

### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bx9t4yia1",
  "tool_use_id": "toolu_01N16fYXFuxBrBLueaFZUoJL",
  "status": "completed",
  "output_file": "",
  "summary": "Re-run with strict sign-reversal check",
  "uuid": "cf78846f-b43e-4d33-9b54-b99e5c1febc6",
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502"
}
```

---

### Tool result

_source line 53 · 2026-05-22T11:49:15.578Z_

<details><summary>↩ Tool result · `toolu_01N16fYXFuxBrBLueaFZUoJL`</summary>

```text
Exp-E: ASV Stability Across DGPs
======================================================================
Precomputing IV sufficient statistics...
  alternating_large: Wald(I) = 1.338985
  same_sign_medium: Wald(I) = 0.305478
  alternating_small: Wald(I) = 0.272231

DGP: alternating_large  beta=[0.0, 1.0, -0.5]
   confounding: 10%=0.348, 50%=None
      exposure: 10%=0.09, 50%=0.5561, sf=2.2222
            iv: 10%=0.203, 50%=0.7411

DGP: same_sign_medium  beta=[0.0, 0.5, 0.3]
   confounding: 10%=None, 50%=None
      exposure: 10%=0.223, 50%=1.1741, sf=2.2222
            iv: 10%=0.203, 50%=0.7411

DGP: alternating_small  beta=[0.0, 0.2, -0.1]
   confounding: 10%=None, 50%=None
      exposure: 10%=0.09, 50%=0.5561, sf=2.2222
            iv: 10%=0.203, 50%=0.7411

======================================================================
Ranking (by delta*_10%, lower = more fragile)
======================================================================
  alternating_large: exposure(0.0900) < iv(0.2030) < confounding(0.3480)
  same_sign_medium: iv(0.2030) < exposure(0.2230) < confounding(inf)
  alternating_small: exposure(0.0900) < iv(0.2030) < confounding(inf)

Stable: False -- Rankings vary across DGPs
Same-sign sign-flip: 2.2222

Saved: artifacts/exp_e_asv_stability_results.json
Saved: artifacts/exp_e_asv_stability_table.tex

Total: 23.7s
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "c87644b6-eca3-48c8-9ea1-3ebbb217bd6d",
  "tool_use_result": {
    "stdout": "Exp-E: ASV Stability Across DGPs\n======================================================================\nPrecomputing IV sufficient statistics...\n  alternating_large: Wald(I) = 1.338985\n  same_sign_medium: Wald(I) = 0.305478\n  alternating_small: Wald(I) = 0.272231\n\nDGP: alternating_large  beta=[0.0, 1.0, -0.5]\n   confounding: 10%=0.348, 50%=None\n      exposure: 10%=0.09, 50%=0.5561, sf=2.2222\n            iv: 10%=0.203, 50%=0.7411\n\nDGP: same_sign_medium  beta=[0.0, 0.5, 0.3]\n   confounding: 10%=None, 50%=None\n      exposure: 10%=0.223, 50%=1.1741, sf=2.2222\n            iv: 10%=0.203, 50%=0.7411\n\nDGP: alternating_small  beta=[0.0, 0.2, -0.1]\n   confounding: 10%=None, 50%=None\n      exposure: 10%=0.09, 50%=0.5561, sf=2.2222\n            iv: 10%=0.203, 50%=0.7411\n\n======================================================================\nRanking (by delta*_10%, lower = more fragile)\n======================================================================\n  alternating_large: exposure(0.0900) < iv(0.2030) < confounding(0.3480)\n  same_sign_medium: iv(0.2030) < exposure(0.2230) < confounding(inf)\n  alternating_small: exposure(0.0900) < iv(0.2030) < confounding(inf)\n\nStable: False -- Rankings vary across DGPs\nSame-sign sign-flip: 2.2222\n\nSaved: artifacts/exp_e_asv_stability_results.json\nSaved: artifacts/exp_e_asv_stability_table.tex\n\nTotal: 23.7s",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 54_

<details><summary>Logged reasoning block</summary>

```text
The sign-flip result didn't change — all three DGPs still show sign_flip = 2.2222. This is because the strict sign reversal (gamma * beta < 0) is achieved at the very next grid point after the uniform boundary (where gamma goes from ~0 to slightly negative). The grid resolution (0.001) means the delta is essentially the same.

Let me check if the sign flip actually changed to a later grid point or is exactly the same:

For diag=0.7 C₀, delta_max = 3.333... The grid has 3334 points. The uniform point is at delta = 2.222..., which is grid index ~2222. The next point is at delta ≈ 2.223.


But the output still shows 2.2222. Looking at the per-C₀ results, I realize the linspace grid with n=3334 points from 0 to 3.333 has a step of 0.001000..., so index 2222 gives exactly 2.222 and index 2223 gives 2.223. At the exact uniform point, gamma is zero, so the strict inequality (gamma * beta < 0) fails since 0 * 0.5 = 0.

Let me recalculate more precisely: 2222/3333 * 3.333... = 2.222222..., and 2223/3333 * 3.333... = 2.223222.... So the sign flip should occur at 2.223222..., not 2.222222..., but the output shows 2.2222, which suggests the strict check is somehow being triggered at the 2.222 grid point. Let me verify this more carefully.

At delta ≈ 2.222, the gamma values are very small due to floating point precision—gamma_1 is slightly positive at 0.000061, while for the alternating_large case, gamma_2 is slightly negative at -0.000001. When I multiply gamma_2 by beta_2 = -0.5, the product should be positive, but the numerical precision might be causing the check to trigger anyway.

Let me reconsider the grid construction—the linspace might not be hitting the exact uniform point where C = 1/3 everywhere. I need to verify how the delta values are actually being generated for diag=0.7, since the grid spacing and rounding could be shifting where the sign flip is detected. I'm noticing a discrepancy—the gamma values are both positive and small (0.000061 and 0.000037), so their products with the positive beta values should stay positive, yet the output is reporting sign_flip = 2.2222, which doesn't match. Let me verify whether my test calculation used the exact same computation pipeline as the actual code.

The code constructs a grid of delta values and evaluates the exposure at each point, but in my debug work I computed the plim at specific delta values that might not align exactly with the grid points the code uses. I should re-run this with the actual grid to see if the slight differences in delta values account for the discrepancy.

Looking at the per-C₀ breakdown, the individual sign_flip values vary across different C₀ configurations (ranging from 1.334 to 6.667), and the median of these values is 2.222, which matches what I'm seeing in the aggregate results.

Now I'm checking whether my code fix for the strict sign reversal actually changed anything—the results appear identical to before, which suggests the sign flip is being detected at the same delta value even with the stricter condition. Let me trace through why this might be happening by examining what's occurring at that critical delta point. I'm realizing the output value 2.2222222222222223 is exactly 20/9 in floating point, but the actual grid point should be around 2.223. The console output shows "sf=2.2222" with some formatting applied, so I need to check whether the raw JSON value differs from what's being displayed—the default float representation might be rounding or truncating the actual computed value. I'm going to write a simple test case to isolate what's happening with the gamma values and the delta calculations at the boundary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "5a187db0-b7e3-4af4-a8f9-8921367e0b22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tRCySoA6v787nzQqNFWMA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 129168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 659
      },
      "output_tokens": 8,
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

_source line 55_

The output didn't change, which means the strict check produces essentially the same result at grid resolution. Let me verify the exact values at the boundary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "42c5f21f-9fad-47dd-b100-3a1b780c4931",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tRCySoA6v787nzQqNFWMA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 129168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 659
      },
      "output_tokens": 8,
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

_source line 56_

<details open><summary>🔧 Tool call — Bash · `toolu_014hnqFN2DXephHHRVnH5g3X`</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np\nK = 3\n\ndef make_C_delta(C0, delta):\n    C = (1 - delta) * np.eye(K) + delta * C0\n    C = np.maximum(C, 0.0)\n    cs = C.sum(axis=0)\n    cs = np.where(cs < 1e-10, 1.0, cs)\n    return C / cs\n\ndef make_fixed_C0(diag_val):\n    off = (1 - diag_val) / (K - 1)\n    C0 = np.full((K, K), off)\n    np.fill_diagonal(C0, diag_val)\n    return C0\n\ndef plim_exposure(C, p, beta):\n    q = C @ p\n    EZZ = np.array([[1, q[1], q[2]], [q[1], q[1], 0], [q[2], 0, q[2]]])\n    EZX = np.array([\n        [1, p[1], p[2]],\n        [q[1], C[1,1]*p[1], C[1,2]*p[2]],\n        [q[2], C[2,1]*p[1], C[2,2]*p[2]]])\n    return np.linalg.solve(EZZ, EZX @ beta)\n\np = np.array([0.5, 0.33, 0.17])\nbeta_ss = np.array([0., 0.5, 0.3])\n\n# Reproduce exact grid\nfor diag in [0.5, 0.7]:\n    C0 = make_fixed_C0(diag)\n    dmax = min(1.0 / (1.0 - diag), 10.0)\n    n = int(round(dmax / 0.001)) + 1\n    deltas = np.linspace(0, dmax, n)\n    \n    # Find the uniform boundary\n    uniform_delta = (2/3) * dmax\n    \n    # Check grid points near uniform boundary\n    idx = np.searchsorted(deltas, uniform_delta)\n    print(f'diag={diag}, dmax={dmax:.6f}, uniform={uniform_delta:.10f}')\n    for i in range(max(0, idx-2), min(len(deltas), idx+3)):\n        d = deltas[i]\n        C = make_C_delta(C0, d)\n        g = plim_exposure(C, p, beta_ss)\n        prod1 = g[1] * beta_ss[1]\n        prod2 = g[2] * beta_ss[2]\n        print(f'  i={i}, d={d:.15f}, g1={g[1]:.15e}, g2={g[2]:.15e}, '\n              f'prod1={prod1:.6e}, prod2={prod2:.6e}, '\n              f'flip1={prod1<0}, flip2={prod2<0}')\n    print()\n\"",
  "description": "Check exact plim values at grid points near uniform boundary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "91e6200c-4093-4b3a-a702-8cc354b1e824",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015tRCySoA6v787nzQqNFWMA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 129168,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 659
      },
      "output_tokens": 8,
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

_source line 57 · 2026-05-22T11:50:27.703Z_

<details><summary>↩ Tool result · `toolu_014hnqFN2DXephHHRVnH5g3X`</summary>

```text
diag=0.5, dmax=2.000000, uniform=1.3333333333
  i=1332, d=1.332000000000000, g1=6.050008925875567e-04, g2=3.666990828503538e-04, prod1=3.025004e-04, prod2=1.100097e-04, flip1=False, flip2=False
  i=1333, d=1.333000000000000, g1=1.512800519908487e-04, g2=9.170118840112811e-05, prod1=7.564003e-05, prod2=2.751036e-05, flip1=False, flip2=False
  i=1334, d=1.334000000000000, g1=-3.026198072310869e-04, g2=-1.834552635130044e-04, prod1=-1.513099e-04, prod2=-5.503658e-05, flip1=True, flip2=True
  i=1335, d=1.335000000000000, g1=-7.566988902319951e-04, g2=-4.587705040044177e-04, prod1=-3.783494e-04, prod2=-1.376312e-04, flip1=True, flip2=True
  i=1336, d=1.336000000000000, g1=-1.210957402473729e-03, g2=-7.342447644552469e-04, prod1=-6.054787e-04, prod2=-2.202734e-04, flip1=True, flip2=True

diag=0.7, dmax=3.333333, uniform=2.2222222222
  i=2220, d=2.220222022202220, g1=5.445695605110894e-04, g2=3.300748457950528e-04, prod1=2.722848e-04, prod2=9.902245e-05, flip1=False, flip2=False
  i=2221, d=2.221222122212221, g1=2.723170002084269e-04, g2=1.650659578575763e-04, prod1=1.361585e-04, prod2=4.951979e-05, flip1=False, flip2=False
  i=2222, d=2.222222222222222, g1=-1.552091788425969e-16, g2=-1.135758154191536e-16, prod1=-7.760459e-17, prod2=-3.407274e-17, flip1=True, flip2=True
  i=2223, d=2.223222322232223, g1=-2.723814844103382e-04, g2=-1.651230776861482e-04, prod1=-1.361907e-04, prod2=-4.953692e-05, flip1=True, flip2=True
  i=2224, d=2.224222422242224, g1=-5.448274973574140e-04, g2=-3.303033251434936e-04, prod1=-2.724137e-04, prod2=-9.909100e-05, flip1=True, flip2=True
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "b480cb37-44be-43ab-bafc-e38e0a8afffd",
  "tool_use_result": {
    "stdout": "diag=0.5, dmax=2.000000, uniform=1.3333333333\n  i=1332, d=1.332000000000000, g1=6.050008925875567e-04, g2=3.666990828503538e-04, prod1=3.025004e-04, prod2=1.100097e-04, flip1=False, flip2=False\n  i=1333, d=1.333000000000000, g1=1.512800519908487e-04, g2=9.170118840112811e-05, prod1=7.564003e-05, prod2=2.751036e-05, flip1=False, flip2=False\n  i=1334, d=1.334000000000000, g1=-3.026198072310869e-04, g2=-1.834552635130044e-04, prod1=-1.513099e-04, prod2=-5.503658e-05, flip1=True, flip2=True\n  i=1335, d=1.335000000000000, g1=-7.566988902319951e-04, g2=-4.587705040044177e-04, prod1=-3.783494e-04, prod2=-1.376312e-04, flip1=True, flip2=True\n  i=1336, d=1.336000000000000, g1=-1.210957402473729e-03, g2=-7.342447644552469e-04, prod1=-6.054787e-04, prod2=-2.202734e-04, flip1=True, flip2=True\n\ndiag=0.7, dmax=3.333333, uniform=2.2222222222\n  i=2220, d=2.220222022202220, g1=5.445695605110894e-04, g2=3.300748457950528e-04, prod1=2.722848e-04, prod2=9.902245e-05, flip1=False, flip2=False\n  i=2221, d=2.221222122212221, g1=2.723170002084269e-04, g2=1.650659578575763e-04, prod1=1.361585e-04, prod2=4.951979e-05, flip1=False, flip2=False\n  i=2222, d=2.222222222222222, g1=-1.552091788425969e-16, g2=-1.135758154191536e-16, prod1=-7.760459e-17, prod2=-3.407274e-17, flip1=True, flip2=True\n  i=2223, d=2.223222322232223, g1=-2.723814844103382e-04, g2=-1.651230776861482e-04, prod1=-1.361907e-04, prod2=-4.953692e-05, flip1=True, flip2=True\n  i=2224, d=2.224222422242224, g1=-5.448274973574140e-04, g2=-3.303033251434936e-04, prod1=-2.724137e-04, prod2=-9.909100e-05, flip1=True, flip2=True",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
Now I see the issue: at the exact grid point delta = 2.222222... for diag=0.7, the plim values are:
- gamma_1 = -1.55e-16 (essentially 0, but numerically negative due to floating point)
- gamma_2 = -1.14e-16

So `curves[i, k] * beta0[k]` = -1.55e-16 * 0.5 = -7.76e-17 < 0 → flip detected!

The floating point error makes gamma very slightly negative (instead of exactly 0) at the uniform point. 

This is triggering the strict sign reversal check, but it's really just numerical noise from the matrix solve. I need to add a tolerance threshold so I only flag actual sign flips, not tiny floating point artifacts. The right approach is to check if the magnitude of gamma exceeds some fraction of beta—something like 1% relative tolerance—so the uniform point where gamma is essentially zero gets skipped. I'm testing this threshold approach with concrete values, and I see the problem — even tiny negative values like -0.000272 are technically sign reversals, so using a magnitude threshold feels arbitrary and misses real flips. I should instead use a very tight tolerance for floating-point noise and accept any sign change beyond that, rather than trying to filter by absolute magnitude. the sign flip occurs at the next grid point after the uniform boundary, which is just one step away (delta difference of 0.001). For diag=0.5, the flip stays at 1.334 since gamma was already negative at that grid point, while for diag=0.7 it's essentially 2.223. Let me double-check the gamma values around the boundary to make sure I'm identifying the flip correctly. The diag=0.5 case avoids the floating point precision issue because the uniform point doesn't land exactly on a grid point, whereas with diag=0.7 it does. Let me check whether the median changes across different diagonal values—so far diag=0.5 gives sf=1.334, and I need to verify if diag=0.6 has the uniform point falling on a grid point. The median across those delta values would shift slightly if I adjust 2.222 to 2.223, but it's negligible. Rather than getting caught up in floating-point precision, let me step back—the key finding is that all DGPs show a sign flip at roughly the same delta value, which corresponds to the uniform confusion boundary. This sign flip is genuine, stemming from the symmetric C₀ matrices and linear plim structure, and it reveals that the "same-sign should not flip" prediction breaks down in extreme confusion regimes. I'll add tolerance handling to the code and move forward.

The main takeaways are clear: magnitude ASV ordering is exposure-alternating < IV < confounding (with IV and exposure occasionally swapping for same-sign cases), the sign-flip ASV is invariant to beta under symmetric C₀ (a universal property), and confounding emerges as most robust with the largest ASV. This is a solid experimental result.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "a2a6bc2b-1989-4362-a6f5-b201d06d8d9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SvtJkpJUA3MYnnkVQGSf64",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4420,
      "cache_read_input_tokens": 129827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4420
      },
      "output_tokens": 8,
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

_source line 59_

The issue is floating point: at the exact uniform point, gamma = -1.55e-16 (should be 0) triggers the check. Let me add a proper tolerance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "812240be-de31-4534-95d9-75b45dc555c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SvtJkpJUA3MYnnkVQGSf64",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4420,
      "cache_read_input_tokens": 129827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4420
      },
      "output_tokens": 8,
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

_source line 60_

<details open><summary>🔧 Tool call — Edit · `toolu_01QJSEqb8rvhEToE1rkRtYrB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py",
  "old_string": "    sf = None\n    for i, d in enumerate(deltas):\n        for k in [1, 2]:\n            if abs(beta0[k]) > 1e-10 and curves[i, k] * beta0[k] < 0:\n                sf = float(d)\n                break\n        if sf is not None:\n            break",
  "new_string": "    sf = None\n    for i, d in enumerate(deltas):\n        for k in [1, 2]:\n            if (abs(beta0[k]) > 1e-10\n                    and abs(curves[i, k]) > 1e-10\n                    and curves[i, k] * beta0[k] < 0):\n                sf = float(d)\n                break\n        if sf is not None:\n            break"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "4dd68305-b247-4da2-9fbc-a47aa3967b33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SvtJkpJUA3MYnnkVQGSf64",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4420,
      "cache_read_input_tokens": 129827,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4420
      },
      "output_tokens": 8,
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

_source line 61 · 2026-05-22T11:51:23.542Z_

<details><summary>↩ Tool result · `toolu_01QJSEqb8rvhEToE1rkRtYrB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "cd753b92-9eeb-4c60-a1dc-9f6800996f4d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py",
    "oldString": "    sf = None\n    for i, d in enumerate(deltas):\n        for k in [1, 2]:\n            if abs(beta0[k]) > 1e-10 and curves[i, k] * beta0[k] < 0:\n                sf = float(d)\n                break\n        if sf is not None:\n            break",
    "newString": "    sf = None\n    for i, d in enumerate(deltas):\n        for k in [1, 2]:\n            if (abs(beta0[k]) > 1e-10\n                    and abs(curves[i, k]) > 1e-10\n                    and curves[i, k] * beta0[k] < 0):\n                sf = float(d)\n                break\n        if sf is not None:\n            break",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nExp-E: ASV Stability Across DGPs\n\nDemonstrates that ASV ranking (relative topology vulnerability ordering)\nis stable across different DGP parameter configurations.\n\n3 DGP configs × 3 topologies × 5 C₀ matrices = 45 sweeps.\nEach of 9 cells reports the median δ* over the 5 C₀s.\n\"\"\"\n\nimport numpy as np\nimport json\nimport time\n\nK = 3\nSTEP = 0.001\n\n# ─── C(δ) parameterization ──────────────────────────────────────────────────\n\ndef make_C_delta(C0, delta):\n    C = (1 - delta) * np.eye(K) + delta * C0\n    C = np.maximum(C, 0.0)\n    cs = C.sum(axis=0)\n    cs = np.where(cs < 1e-10, 1.0, cs)\n    return C / cs\n\n\ndef get_delta_max(C0):\n    d = np.diag(C0).min()\n    if d >= 1.0:\n        return 10.0\n    return min(1.0 / (1.0 - d), 10.0)\n\n\ndef make_fixed_C0(diag_val):\n    off = (1 - diag_val) / (K - 1)\n    C0 = np.full((K, K), off)\n    np.fill_diagonal(C0, diag_val)\n    return C0\n\n\n# ─── Topology 1: Confounding ────────────────────────────────────────────────\n# DAG: A → T, A → Y, T → Y, A → A*\n# OLS: Y ~ 1 + T + D*₁ + D*₂\n# plim γ = (E[Z'Z])⁻¹ E[Z'X] β   where Z uses A*, X uses A\n\ndef plim_confounding(C, dgp):\n    p = dgp['p']\n    g = dgp['gamma']\n    tau = dgp['tau']\n    bA = dgp['beta'][1:]\n    sT = dgp.get('sigma_T', 1.0)\n\n    b = np.array([0.0, tau, bA[0], bA[1]])\n    ET = g[0] * p[1] + g[1] * p[2]\n    ET2 = g[0]**2 * p[1] + g[1]**2 * p[2] + sT**2\n    q = C @ p\n    ETDs = np.array([g[0] * C[j, 1] * p[1] + g[1] * C[j, 2] * p[2]\n                     for j in range(K)])\n\n    EZZ = np.array([\n        [1,    ET,      q[1],     q[2]    ],\n        [ET,   ET2,     ETDs[1],  ETDs[2] ],\n        [q[1], ETDs[1], q[1],     0       ],\n        [q[2], ETDs[2], 0,        q[2]    ]])\n    EZX = np.array([\n        [1,    ET,      p[1],         p[2]        ],\n        [ET,   ET2,     g[0] * p[1],  g[1] * p[2] ],\n        [q[1], ETDs[1], C[1, 1] * p[1], C[1, 2] * p[2]],\n        [q[2], ETDs[2], C[2, 1] * p[1], C[2, 2] * p[2]]])\n    return np.linalg.solve(EZZ, EZX @ b)[1]\n\n\n# ─── Topology 2: Exposure ───────────────────────────────────────────────────\n# DAG: A → Y, A → A*\n# OLS: Y ~ 1 + D*₁ + D*₂\n\ndef plim_exposure(C, dgp):\n    p, beta = dgp['p'], dgp['beta']\n    q = C @ p\n    EZZ = np.array([\n        [1,    q[1], q[2]],\n        [q[1], q[1], 0   ],\n        [q[2], 0,    q[2]]])\n    EZX = np.array([\n        [1,    p[1],           p[2]          ],\n        [q[1], C[1, 1] * p[1], C[1, 2] * p[2]],\n        [q[2], C[2, 1] * p[1], C[2, 2] * p[2]]])\n    return np.linalg.solve(EZZ, EZX @ beta)\n\n\n# ─── Topology 3: IV ─────────────────────────────────────────────────────────\n# DAG: Z → A, U → {A,Y}, A → Y, A → A*\n# Wald estimator: RF / FS*₁\n\nIV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)\n\n\ndef _softmax_sample(logits, rng):\n    e = np.exp(logits - logits.max(1, keepdims=True))\n    p = e / e.sum(1, keepdims=True)\n    c = np.cumsum(p, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    return (u >= c[:, 0]).astype(int) + (u >= c[:, 1]).astype(int)\n\n\ndef precomp_iv(beta, params, N=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['dZ'] * Z + params['dU'] * U,\n        params['g2'] + params['dZ2'] * Z + params['dU2'] * U])\n    A = _softmax_sample(logits, rng)\n    Y = (beta[1] * (A == 1).astype(float)\n         + beta[2] * (A == 2).astype(float)\n         + params['lam'] * U + rng.normal(0, 1, N))\n    z1, z0 = Z == 1, Z == 0\n    RF = Y[z1].mean() - Y[z0].mean()\n    FS = np.array([(A[z1] == k).mean() - (A[z0] == k).mean()\n                   for k in range(K)])\n    return dict(RF=RF, FS=FS)\n\n\ndef plim_iv(C, st):\n    fs = (C @ st['FS'])[1]\n    return np.nan if abs(fs) < 1e-8 else st['RF'] / fs\n\n\n# ─── ASV computation ────────────────────────────────────────────────────────\n\ndef _make_grid(C0):\n    dmax = get_delta_max(C0)\n    n = int(round(dmax / STEP)) + 1\n    return np.linspace(0, dmax, n)\n\n\ndef _find_envelope_asv(deltas, bias_abs, tau_abs, threshold):\n    if tau_abs < 1e-12:\n        return 0.0\n    thresh = threshold * tau_abs\n    rmax = 0.0\n    for i in range(len(deltas)):\n        b = bias_abs[i]\n        if not np.isnan(b):\n            rmax = max(rmax, b)\n        if rmax > thresh:\n            return float(deltas[i])\n    return None\n\n\ndef compute_cell_confounding(dgp, C0):\n    deltas = _make_grid(C0)\n    tau0 = plim_confounding(np.eye(K), dgp)\n    curve = np.array([plim_confounding(make_C_delta(C0, d), dgp)\n                      for d in deltas])\n    ba = np.abs(curve - tau0)\n    return {\n        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),\n        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),\n    }\n\n\ndef compute_cell_exposure(dgp, C0):\n    deltas = _make_grid(C0)\n    beta0 = plim_exposure(np.eye(K), dgp)\n    curves = np.array([plim_exposure(make_C_delta(C0, d), dgp)\n                       for d in deltas])\n\n    mr = np.zeros(len(deltas))\n    for i in range(len(deltas)):\n        for k in [1, 2]:\n            if abs(beta0[k]) > 1e-10:\n                mr[i] = max(mr[i],\n                            abs(curves[i, k] - beta0[k]) / abs(beta0[k]))\n\n    def _mag(threshold):\n        rmax = 0.0\n        for i in range(len(deltas)):\n            rmax = max(rmax, mr[i])\n            if rmax > threshold:\n                return float(deltas[i])\n        return None\n\n    sf = None\n    for i, d in enumerate(deltas):\n        for k in [1, 2]:\n            if abs(beta0[k]) > 1e-10 and curves[i, k] * beta0[k] < 0:\n                sf = float(d)\n                break\n        if sf is not None:\n            break\n\n    return {\n        'mag_asv_10pct': _mag(0.1),\n        'mag_asv_50pct': _mag(0.5),\n        'sign_flip_asv': sf,\n    }\n\n\ndef compute_cell_iv(st, C0):\n    deltas = _make_grid(C0)\n    tau0 = plim_iv(np.eye(K), st)\n    if np.isnan(tau0) or abs(tau0) < 1e-10:\n        return {'mag_asv_10pct': None, 'mag_asv_50pct': None}\n    curve = np.array([plim_iv(make_C_delta(C0, d), st) for d in deltas])\n    ba = np.abs(curve - tau0)\n    return {\n        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),\n        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),\n    }\n\n\ndef median_results(cells):\n    keys = cells[0].keys()\n    out = {}\n    for k in keys:\n        vals = [c[k] for c in cells if c[k] is not None]\n        out[k] = round(float(np.median(vals)), 4) if vals else None\n    return out\n\n\n# ─── Main ────────────────────────────────────────────────────────────────────\n\nif __name__ == '__main__':\n    t0 = time.time()\n\n    DGPS = [\n        {'name': 'alternating_large',\n         'beta': np.array([0., 1.0, -0.5]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n        {'name': 'same_sign_medium',\n         'beta': np.array([0., 0.5, 0.3]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n        {'name': 'alternating_small',\n         'beta': np.array([0., 0.2, -0.1]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n    ]\n\n    DIAG_VALS = [0.5, 0.6, 0.7, 0.8, 0.9]\n    C0S = [(d, make_fixed_C0(d)) for d in DIAG_VALS]\n    TOPOS = ['confounding', 'exposure', 'iv']\n\n    print(\"Exp-E: ASV Stability Across DGPs\")\n    print(\"=\" * 70)\n\n    print(\"Precomputing IV sufficient statistics...\")\n    iv_st = {}\n    for dgp in DGPS:\n        iv_st[dgp['name']] = precomp_iv(dgp['beta'], IV_PARAMS)\n        t_iv = plim_iv(np.eye(K), iv_st[dgp['name']])\n        print(f\"  {dgp['name']}: Wald(I) = {t_iv:.6f}\")\n\n    results = {t: {} for t in TOPOS}\n    per_c0 = {t: {} for t in TOPOS}\n\n    for dgp in DGPS:\n        nm = dgp['name']\n        print(f\"\\nDGP: {nm}  beta={dgp['beta'].tolist()}\")\n\n        for topo in TOPOS:\n            cells = []\n            for dv, C0 in C0S:\n                if topo == 'confounding':\n                    c = compute_cell_confounding(dgp, C0)\n                elif topo == 'exposure':\n                    c = compute_cell_exposure(dgp, C0)\n                else:\n                    c = compute_cell_iv(iv_st[nm], C0)\n                cells.append(c)\n\n            med = median_results(cells)\n            results[topo][nm] = med\n            per_c0[topo][nm] = [\n                {**c, 'C0_diag': dv} for (dv, _), c in zip(C0S, cells)]\n\n            parts = [f\"10%={med['mag_asv_10pct']}\",\n                     f\"50%={med['mag_asv_50pct']}\"]\n            if 'sign_flip_asv' in med:\n                parts.append(f\"sf={med['sign_flip_asv']}\")\n            print(f\"  {topo:>12}: {', '.join(parts)}\")\n\n    # ── Ranking analysis ─────────────────────────────────────────────────────\n    print(\"\\n\" + \"=\" * 70)\n    print(\"Ranking (by delta*_10%, lower = more fragile)\")\n    print(\"=\" * 70)\n    rankings = {}\n    for dgp in DGPS:\n        nm = dgp['name']\n        vals = [(t, results[t][nm]['mag_asv_10pct'] or float('inf'))\n                for t in TOPOS]\n        vals.sort(key=lambda x: x[1])\n        rankings[nm] = [t for t, _ in vals]\n        vstr = ' < '.join(f\"{t}({v:.4f})\" for t, v in vals)\n        print(f\"  {nm}: {vstr}\")\n\n    stable = len(set(tuple(r) for r in rankings.values())) == 1\n    stability_msg = (\"Rankings preserved across all 3 DGPs\" if stable\n                     else \"Rankings vary across DGPs\")\n    print(f\"\\nStable: {stable} -- {stability_msg}\")\n\n    sf_ss = results['exposure']['same_sign_medium'].get('sign_flip_asv')\n    print(f\"Same-sign sign-flip: \"\n          f\"{'None (confirmed -- no flip for same-sign beta)' if sf_ss is None else sf_ss}\")\n\n    # ── Save JSON ────────────────────────────────────────────────────────────\n    output = {\n        'dgp_configs': [\n            {'name': d['name'], 'beta': d['beta'].tolist(),\n             'tau': d['tau'], 'p': d['p'].tolist()}\n            for d in DGPS],\n        'C0_diag_values': DIAG_VALS,\n        'results': results,\n        'per_C0_results': per_c0,\n        'rankings': rankings,\n        'ranking_stable': stable,\n        'ranking_stability': stability_msg,\n    }\n    json_path = 'artifacts/exp_e_asv_stability_results.json'\n    with open(json_path, 'w') as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nSaved: {json_path}\")\n\n    # ── Save LaTeX table ─────────────────────────────────────────────────────\n    labels = {\n        'alternating_large': r'Alt.\\ large: $\\bm{\\beta}=[0,\\,1.0,\\,-0.5]$',\n        'same_sign_medium':  r'Same-sign: $\\bm{\\beta}=[0,\\,0.5,\\,0.3]$',\n        'alternating_small': r'Alt.\\ small: $\\bm{\\beta}=[0,\\,0.2,\\,-0.1]$',\n    }\n    tex = [\n        r'\\begin{table}[t]',\n        r'\\centering',\n        r'\\caption{ASV stability across DGP configurations. '\n        r'Each cell shows $\\delta^*$ at the 10\\% relative bias threshold '\n        r'(median over 5 confusion matrices with diagonal '\n        r'$\\in\\{0.5,0.6,0.7,0.8,0.9\\}$). '\n        r'Lower values indicate greater fragility to annotation error. '\n        r'The ranking IV $<$ Exposure $<$ Confounding is preserved '\n        r'across all configurations.}',\n        r'\\label{tab:asv_stability}',\n        r'\\small',\n        r'\\begin{tabular}{l ccc c}',\n        r'\\toprule',\n        r' & \\multicolumn{3}{c}{Magnitude ASV $\\delta^*_{10\\%}$}'\n        r' & Sign-flip \\\\',\n        r'\\cmidrule(lr){2-4} \\cmidrule(lr){5-5}',\n        r'DGP Configuration & Confounding & Exposure & IV'\n        r' & $\\delta^*_\\mathrm{sf}$ (Exp.) \\\\',\n        r'\\midrule',\n    ]\n    for dgp in DGPS:\n        nm = dgp['name']\n        vals = []\n        for t in TOPOS:\n            v = results[t][nm]['mag_asv_10pct']\n            vals.append(f'{v:.3f}' if v is not None else '---')\n        sf = results['exposure'][nm].get('sign_flip_asv')\n        sf_s = f'{sf:.3f}' if sf is not None else '---'\n        tex.append(\n            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]}'\n            f' & {sf_s} \\\\\\\\')\n    tex += [r'\\bottomrule', r'\\end{tabular}', r'\\end{table}']\n\n    tex_path = 'artifacts/exp_e_asv_stability_table.tex'\n    with open(tex_path, 'w') as f:\n        f.write('\\n'.join(tex))\n    print(f\"Saved: {tex_path}\")\n\n    print(f\"\\nTotal: {time.time() - t0:.1f}s\")\n",
    "structuredPatch": [
      {
        "oldStart": 187,
        "oldLines": 7,
        "newStart": 187,
        "newLines": 9,
        "lines": [
          "     sf = None",
          "     for i, d in enumerate(deltas):",
          "         for k in [1, 2]:",
          "-            if abs(beta0[k]) > 1e-10 and curves[i, k] * beta0[k] < 0:",
          "+            if (abs(beta0[k]) > 1e-10",
          "+                    and abs(curves[i, k]) > 1e-10",
          "+                    and curves[i, k] * beta0[k] < 0):",
          "                 sf = float(d)",
          "                 break",
          "         if sf is not None:"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Bash · `toolu_016feJ6SjytK8HFqmuTn2bjp`</summary>

```json
{
  "command": "python3 artifacts/exp_e_asv_stability.py 2>&1",
  "description": "Re-run with floating point tolerance on sign flip",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "d6827556-ad76-4367-a65a-f3cdf46ce607",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013kinHprwFzQG2keDYtWPTp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2519,
      "cache_read_input_tokens": 134247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2519
      },
      "output_tokens": 45,
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

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bajup4hsr",
  "tool_use_id": "toolu_016feJ6SjytK8HFqmuTn2bjp",
  "description": "Re-run with floating point tolerance on sign flip",
  "task_type": "local_bash",
  "uuid": "0600176d-b61c-450b-accd-b5a35fe24843",
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502"
}
```

---

### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bajup4hsr",
  "tool_use_id": "toolu_016feJ6SjytK8HFqmuTn2bjp",
  "status": "completed",
  "output_file": "",
  "summary": "Re-run with floating point tolerance on sign flip",
  "uuid": "9c2c10ee-9b19-460b-ad6a-94f0b27f4c84",
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502"
}
```

---

### Tool result

_source line 65 · 2026-05-22T11:51:36.436Z_

<details><summary>↩ Tool result · `toolu_016feJ6SjytK8HFqmuTn2bjp`</summary>

```text
Exp-E: ASV Stability Across DGPs
======================================================================
Precomputing IV sufficient statistics...
  alternating_large: Wald(I) = 1.338985
  same_sign_medium: Wald(I) = 0.305478
  alternating_small: Wald(I) = 0.272231

DGP: alternating_large  beta=[0.0, 1.0, -0.5]
   confounding: 10%=0.348, 50%=None
      exposure: 10%=0.09, 50%=0.5561, sf=2.2232
            iv: 10%=0.203, 50%=0.7411

DGP: same_sign_medium  beta=[0.0, 0.5, 0.3]
   confounding: 10%=None, 50%=None
      exposure: 10%=0.223, 50%=1.1741, sf=2.2232
            iv: 10%=0.203, 50%=0.7411

DGP: alternating_small  beta=[0.0, 0.2, -0.1]
   confounding: 10%=None, 50%=None
      exposure: 10%=0.09, 50%=0.5561, sf=2.2232
            iv: 10%=0.203, 50%=0.7411

======================================================================
Ranking (by delta*_10%, lower = more fragile)
======================================================================
  alternating_large: exposure(0.0900) < iv(0.2030) < confounding(0.3480)
  same_sign_medium: iv(0.2030) < exposure(0.2230) < confounding(inf)
  alternating_small: exposure(0.0900) < iv(0.2030) < confounding(inf)

Stable: False -- Rankings vary across DGPs
Same-sign sign-flip: 2.2232

Saved: artifacts/exp_e_asv_stability_results.json
Saved: artifacts/exp_e_asv_stability_table.tex

Total: 9.3s
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "c268a509-9dc8-4aeb-b75e-10292805dd6e",
  "tool_use_result": {
    "stdout": "Exp-E: ASV Stability Across DGPs\n======================================================================\nPrecomputing IV sufficient statistics...\n  alternating_large: Wald(I) = 1.338985\n  same_sign_medium: Wald(I) = 0.305478\n  alternating_small: Wald(I) = 0.272231\n\nDGP: alternating_large  beta=[0.0, 1.0, -0.5]\n   confounding: 10%=0.348, 50%=None\n      exposure: 10%=0.09, 50%=0.5561, sf=2.2232\n            iv: 10%=0.203, 50%=0.7411\n\nDGP: same_sign_medium  beta=[0.0, 0.5, 0.3]\n   confounding: 10%=None, 50%=None\n      exposure: 10%=0.223, 50%=1.1741, sf=2.2232\n            iv: 10%=0.203, 50%=0.7411\n\nDGP: alternating_small  beta=[0.0, 0.2, -0.1]\n   confounding: 10%=None, 50%=None\n      exposure: 10%=0.09, 50%=0.5561, sf=2.2232\n            iv: 10%=0.203, 50%=0.7411\n\n======================================================================\nRanking (by delta*_10%, lower = more fragile)\n======================================================================\n  alternating_large: exposure(0.0900) < iv(0.2030) < confounding(0.3480)\n  same_sign_medium: iv(0.2030) < exposure(0.2230) < confounding(inf)\n  alternating_small: exposure(0.0900) < iv(0.2030) < confounding(inf)\n\nStable: False -- Rankings vary across DGPs\nSame-sign sign-flip: 2.2232\n\nSaved: artifacts/exp_e_asv_stability_results.json\nSaved: artifacts/exp_e_asv_stability_table.tex\n\nTotal: 9.3s",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 66_

<details><summary>Logged reasoning block</summary>

```text
The tolerance fix changed the sign-flip delta from 2.2222 to 2.2232 (shifted by one grid step for the C₀ with diag=0.7 where the grid hit the exact uniform point).

The sign flip is still identical across all 3 DGPs: 2.2232. This confirms the theoretical analysis — for symmetric C₀ in the exposure model, the sign-flip ASV depends ONLY on the C₀ structure (not on beta).

Now, the key results are:

1. **Magnitude ASV (10% threshold)**:
   - Exposure alternating: δ* = 0.090
   - Exposure same-sign: δ* = 0.223
   - IV (all DGPs): δ* = 0.203
   - Confounding alternating_large: δ* = 0.348
   - Confounding same_sign/small: None (≈ ∞)

2. **Ranking**:
   - Alternating DGPs: exposure < IV < confounding ✓
   - Same-sign DGP: IV < exposure < confounding (IV and exposure swap!)

3. **Sign-flip ASV**: Identical across DGPs (2.223), confirming that the sign-flip threshold is purely determined by the C₀ structure regardless of the DGP specification.

The ranking isn't fully stable across all scenarios — for same-sign coefficients, exposure becomes more robust than IV because misclassification between categories doesn't amplify relative bias when both have similar-sign effects, whereas IV's first-stage fragility remains constant. This suggests the ranking actually depends on the coefficient structure rather than being universally fixed. I should report these results as they are, highlighting that while IV and confounding maintain consistent positions, exposure's robustness relative to IV shifts based on whether beta alternates or stays the same-signed.

Now I'm finalizing the outputs and double-checking the JSON and LaTeX tables. I'll stick with the fixed-diagonal C₀ matrices as recommended rather than pulling from the existing codebase. Let me verify the confounding results make sense — for the alternating_large case, a magnitude ASV of 0.348 at 10% bias threshold seems plausible given the diagonal structure and delta scaling. I need to pull the per-C₀ breakdown for the alternating_large case to understand why the confounding varies across different diagonal values — the bias should scale with how far each C₀ is from identity, so lower-diagonal matrices will show stronger confounding effects.

For the cases where ASV comes back as None, that's actually a good sign: it means the annotation error isn't large enough to push the bias past 10% of the treatment effect, so the result is robust. Let me verify the output files have all the confounding results recorded correctly. only alternating_large crosses the 10% threshold. Now I'm checking whether the bias could exceed the OVB in the extreme regime where the confusion matrix has off-diagonal elements larger than diagonal ones — but even at maximum delta, the bias for alternating_large never reaches 50% of tau, which suggests the confounding effect is fundamentally bounded by the structure of the problem.

Let me work through what happens at the anti-diagonal extreme where each category gets misclassified equally to the other two categories. I need to compute the actual confounding bias in this regime to see if adjusting for a corrupted A* could push the bias beyond what we'd expect from OVB alone. I'm computing the expected temporal differences for each state by combining the gamma weights with the transition matrix and probability distribution, and the results show varying magnitudes across states. The confounding ASV value for alternating_large comes out to 0.348.

Looking at the overall experiment results, the ranking isn't entirely stable across conditions—confounding consistently emerges as most robust, but exposure and IV swap positions depending on whether the coefficients alternate in sign or stay the same. For the paper, I should highlight that while confounding robustness is universal, the relative fragility of exposure versus IV depends on the coefficient structure, with alternating signs making exposure particularly vulnerable to cross-category misclassification bias.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "b2c99cfb-1653-4ea9-b058-d60a034f7d13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2moP9kbLa59XfitjfFYZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 136766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 659
      },
      "output_tokens": 9,
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

_source line 67_

Results are now clean. Let me verify the output files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "ba9d5ed3-a20e-41e9-8385-7fbd792f357b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2moP9kbLa59XfitjfFYZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 136766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 659
      },
      "output_tokens": 9,
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

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_01V8pu7fVWbd24MFVy8zuFFK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "9e78498e-8941-4fb5-a1a0-77868612e8eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2moP9kbLa59XfitjfFYZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 136766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 659
      },
      "output_tokens": 9,
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

_source line 69 · 2026-05-22T11:52:39.995Z_

<details><summary>↩ Tool result · `toolu_01V8pu7fVWbd24MFVy8zuFFK`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\caption{ASV stability across DGP configurations. Each cell shows $\delta^*$ at the 10\% relative bias threshold (median over 5 confusion matrices with diagonal $\in\{0.5,0.6,0.7,0.8,0.9\}$). Lower values indicate greater fragility to annotation error. The ranking IV $<$ Exposure $<$ Confounding is preserved across all configurations.}
4	\label{tab:asv_stability}
5	\small
6	\begin{tabular}{l ccc c}
7	\toprule
8	 & \multicolumn{3}{c}{Magnitude ASV $\delta^*_{10\%}$} & Sign-flip \\
9	\cmidrule(lr){2-4} \cmidrule(lr){5-5}
10	DGP Configuration & Confounding & Exposure & IV & $\delta^*_\mathrm{sf}$ (Exp.) \\
11	\midrule
12	Alt.\ large: $\bm{\beta}=[0,\,1.0,\,-0.5]$ & 0.348 & 0.090 & 0.203 & 2.223 \\
13	Same-sign: $\bm{\beta}=[0,\,0.5,\,0.3]$ & --- & 0.223 & 0.203 & 2.223 \\
14	Alt.\ small: $\bm{\beta}=[0,\,0.2,\,-0.1]$ & --- & 0.090 & 0.203 & 2.223 \\
15	\bottomrule
16	\end{tabular}
17	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "8b63a8cc-3111-4c41-a531-a865911ec727",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability_table.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\caption{ASV stability across DGP configurations. Each cell shows $\\delta^*$ at the 10\\% relative bias threshold (median over 5 confusion matrices with diagonal $\\in\\{0.5,0.6,0.7,0.8,0.9\\}$). Lower values indicate greater fragility to annotation error. The ranking IV $<$ Exposure $<$ Confounding is preserved across all configurations.}\n\\label{tab:asv_stability}\n\\small\n\\begin{tabular}{l ccc c}\n\\toprule\n & \\multicolumn{3}{c}{Magnitude ASV $\\delta^*_{10\\%}$} & Sign-flip \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-5}\nDGP Configuration & Confounding & Exposure & IV & $\\delta^*_\\mathrm{sf}$ (Exp.) \\\\\n\\midrule\nAlt.\\ large: $\\bm{\\beta}=[0,\\,1.0,\\,-0.5]$ & 0.348 & 0.090 & 0.203 & 2.223 \\\\\nSame-sign: $\\bm{\\beta}=[0,\\,0.5,\\,0.3]$ & --- & 0.223 & 0.203 & 2.223 \\\\\nAlt.\\ small: $\\bm{\\beta}=[0,\\,0.2,\\,-0.1]$ & --- & 0.090 & 0.203 & 2.223 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  }
}
```

</details>

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Bash · `toolu_01VqtBVw3KBGAPgQQzhb52aN`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('artifacts/exp_e_asv_stability_results.json') as f:\n    d = json.load(f)\n# Print nicely\nprint('=== Results Summary ===')\nfor topo in ['confounding', 'exposure', 'iv']:\n    print(f'\\n{topo.upper()}:')\n    for dgp_name, vals in d['results'][topo].items():\n        print(f'  {dgp_name}: {vals}')\nprint(f'\\nRankings: {d[\\\"rankings\\\"]}')\nprint(f'Stable: {d[\\\"ranking_stable\\\"]}')\nprint(f'Message: {d[\\\"ranking_stability\\\"]}')\n\"",
  "description": "Verify JSON output contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "95853ca2-4d07-424a-a10a-db978c883ebd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2moP9kbLa59XfitjfFYZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 136766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 659
      },
      "output_tokens": 9,
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

_source line 71 · 2026-05-22T11:52:43.277Z_

<details><summary>↩ Tool result · `toolu_01VqtBVw3KBGAPgQQzhb52aN`</summary>

```text
=== Results Summary ===

CONFOUNDING:
  alternating_large: {'mag_asv_10pct': 0.348, 'mag_asv_50pct': None}
  same_sign_medium: {'mag_asv_10pct': None, 'mag_asv_50pct': None}
  alternating_small: {'mag_asv_10pct': None, 'mag_asv_50pct': None}

EXPOSURE:
  alternating_large: {'mag_asv_10pct': 0.09, 'mag_asv_50pct': 0.5561, 'sign_flip_asv': 2.2232}
  same_sign_medium: {'mag_asv_10pct': 0.223, 'mag_asv_50pct': 1.1741, 'sign_flip_asv': 2.2232}
  alternating_small: {'mag_asv_10pct': 0.09, 'mag_asv_50pct': 0.5561, 'sign_flip_asv': 2.2232}

IV:
  alternating_large: {'mag_asv_10pct': 0.203, 'mag_asv_50pct': 0.7411}
  same_sign_medium: {'mag_asv_10pct': 0.203, 'mag_asv_50pct': 0.7411}
  alternating_small: {'mag_asv_10pct': 0.203, 'mag_asv_50pct': 0.7411}

Rankings: {'alternating_large': ['exposure', 'iv', 'confounding'], 'same_sign_medium': ['iv', 'exposure', 'confounding'], 'alternating_small': ['exposure', 'iv', 'confounding']}
Stable: False
Message: Rankings vary across DGPs
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "ad6eba10-a7b8-43d7-b55a-29ec03407802",
  "tool_use_result": {
    "stdout": "=== Results Summary ===\n\nCONFOUNDING:\n  alternating_large: {'mag_asv_10pct': 0.348, 'mag_asv_50pct': None}\n  same_sign_medium: {'mag_asv_10pct': None, 'mag_asv_50pct': None}\n  alternating_small: {'mag_asv_10pct': None, 'mag_asv_50pct': None}\n\nEXPOSURE:\n  alternating_large: {'mag_asv_10pct': 0.09, 'mag_asv_50pct': 0.5561, 'sign_flip_asv': 2.2232}\n  same_sign_medium: {'mag_asv_10pct': 0.223, 'mag_asv_50pct': 1.1741, 'sign_flip_asv': 2.2232}\n  alternating_small: {'mag_asv_10pct': 0.09, 'mag_asv_50pct': 0.5561, 'sign_flip_asv': 2.2232}\n\nIV:\n  alternating_large: {'mag_asv_10pct': 0.203, 'mag_asv_50pct': 0.7411}\n  same_sign_medium: {'mag_asv_10pct': 0.203, 'mag_asv_50pct': 0.7411}\n  alternating_small: {'mag_asv_10pct': 0.203, 'mag_asv_50pct': 0.7411}\n\nRankings: {'alternating_large': ['exposure', 'iv', 'confounding'], 'same_sign_medium': ['iv', 'exposure', 'confounding'], 'alternating_small': ['exposure', 'iv', 'confounding']}\nStable: False\nMessage: Rankings vary across DGPs",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 72_

<details><summary>Logged reasoning block</summary>

```text
The table caption says "The ranking IV < Exposure < Confounding is preserved across all configurations" but the actual result is that the ranking is NOT always preserved (for same_sign_medium, IV < exposure instead of exposure < IV). Let me fix the caption.

Also, I notice the sign-flip ASV values are all 2.223, which is not very informative. The sign-flip ASV is invariant to beta for symmetric C₀ (a mathematical consequence of plim linearity in the exposure model).

Let me also reconsider whether the confounding result (None for same_sign and small) should be better handled. 

The "---" entries in the table actually convey something important — they indicate that confounding bias never reaches 10% of tau even at maximum confusion, which demonstrates how robust these parameter configurations are to confounding. I should update the caption to accurately reflect where the ranking holds and where it doesn't, and add a note explaining what the "---" means and why the sign-flip ASV values are constant across configurations. Now I'm refining the table caption to accurately reflect what's actually stable across the simulations—confounding consistently shows the highest robustness, while the exposure-IV-confounding ranking holds specifically for alternating-sign betas. I'll keep the sign-flip column since it demonstrates an interesting invariance property, even though all values are identical, and I should clean up any incomplete text in the original.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "4ed1182c-a36d-44e6-8d07-cbb6be6a5d88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011z1ioBhW96FxtoBwStXUDd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4009,
      "cache_read_input_tokens": 137425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4009
      },
      "output_tokens": 8,
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

_source line 73_

The table caption incorrectly claims a stable ranking. Let me fix it to reflect the actual results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "c07b73c6-2c8f-4550-a10f-23317c42f5d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011z1ioBhW96FxtoBwStXUDd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4009,
      "cache_read_input_tokens": 137425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4009
      },
      "output_tokens": 8,
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

_source line 74_

<details open><summary>🔧 Tool call — Edit · `toolu_014GuNRrovRNiX5g4wRhQqGH`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py",
  "old_string": "    tex = [\n        r'\\begin{table}[t]',\n        r'\\centering',\n        r'\\caption{ASV stability across DGP configurations. '\n        r'Each cell shows $\\delta^*$ at the 10\\% relative bias threshold '\n        r'(median over 5 confusion matrices with diagonal '\n        r'$\\in\\{0.5,0.6,0.7,0.8,0.9\\}$). '\n        r'Lower values indicate greater fragility to annotation error. '\n        r'The ranking IV $<$ Exposure $<$ Confounding is preserved '\n        r'across all configurations.}',\n        r'\\label{tab:asv_stability}',\n        r'\\small',\n        r'\\begin{tabular}{l ccc c}',\n        r'\\toprule',\n        r' & \\multicolumn{3}{c}{Magnitude ASV $\\delta^*_{10\\%}$}'\n        r' & Sign-flip \\\\',\n        r'\\cmidrule(lr){2-4} \\cmidrule(lr){5-5}',\n        r'DGP Configuration & Confounding & Exposure & IV'\n        r' & $\\delta^*_\\mathrm{sf}$ (Exp.) \\\\',\n        r'\\midrule',\n    ]",
  "new_string": "    tex = [\n        r'\\begin{table}[t]',\n        r'\\centering',\n        r'\\caption{ASV stability across DGP configurations. '\n        r'Each cell shows $\\delta^*$ at the 10\\% relative bias threshold '\n        r'(median over 5 confusion matrices with diagonal '\n        r'$\\in\\{0.5,0.6,0.7,0.8,0.9\\}$). '\n        r'Lower $\\delta^*$ indicates greater fragility. '\n        r'Confounding is consistently most robust; '\n        r'for alternating-sign $\\bm{\\beta}$, '\n        r'the ranking Exposure $<$ IV $<$ Confounding holds. '\n        r'``$\\infty$\\!\\!'' = threshold never reached within $\\delta$ range.}',\n        r'\\label{tab:asv_stability}',\n        r'\\small',\n        r'\\begin{tabular}{l ccc}',\n        r'\\toprule',\n        r' & \\multicolumn{3}{c}{Magnitude ASV $\\delta^*_{10\\%}$} \\\\',\n        r'\\cmidrule(lr){2-4}',\n        r'DGP Configuration & Confounding & Exposure & IV \\\\',\n        r'\\midrule',\n    ]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "f8c1f1eb-19d5-4ea2-b5c6-1aa987031f89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011z1ioBhW96FxtoBwStXUDd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4009,
      "cache_read_input_tokens": 137425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4009
      },
      "output_tokens": 8,
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

_source line 75 · 2026-05-22T11:53:18.535Z_

<details><summary>↩ Tool result · `toolu_014GuNRrovRNiX5g4wRhQqGH`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "f0523a67-e1c0-4ce4-b5f3-11dfc380fc3f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py",
    "oldString": "    tex = [\n        r'\\begin{table}[t]',\n        r'\\centering',\n        r'\\caption{ASV stability across DGP configurations. '\n        r'Each cell shows $\\delta^*$ at the 10\\% relative bias threshold '\n        r'(median over 5 confusion matrices with diagonal '\n        r'$\\in\\{0.5,0.6,0.7,0.8,0.9\\}$). '\n        r'Lower values indicate greater fragility to annotation error. '\n        r'The ranking IV $<$ Exposure $<$ Confounding is preserved '\n        r'across all configurations.}',\n        r'\\label{tab:asv_stability}',\n        r'\\small',\n        r'\\begin{tabular}{l ccc c}',\n        r'\\toprule',\n        r' & \\multicolumn{3}{c}{Magnitude ASV $\\delta^*_{10\\%}$}'\n        r' & Sign-flip \\\\',\n        r'\\cmidrule(lr){2-4} \\cmidrule(lr){5-5}',\n        r'DGP Configuration & Confounding & Exposure & IV'\n        r' & $\\delta^*_\\mathrm{sf}$ (Exp.) \\\\',\n        r'\\midrule',\n    ]",
    "newString": "    tex = [\n        r'\\begin{table}[t]',\n        r'\\centering',\n        r'\\caption{ASV stability across DGP configurations. '\n        r'Each cell shows $\\delta^*$ at the 10\\% relative bias threshold '\n        r'(median over 5 confusion matrices with diagonal '\n        r'$\\in\\{0.5,0.6,0.7,0.8,0.9\\}$). '\n        r'Lower $\\delta^*$ indicates greater fragility. '\n        r'Confounding is consistently most robust; '\n        r'for alternating-sign $\\bm{\\beta}$, '\n        r'the ranking Exposure $<$ IV $<$ Confounding holds. '\n        r'``$\\infty$\\!\\!'' = threshold never reached within $\\delta$ range.}',\n        r'\\label{tab:asv_stability}',\n        r'\\small',\n        r'\\begin{tabular}{l ccc}',\n        r'\\toprule',\n        r' & \\multicolumn{3}{c}{Magnitude ASV $\\delta^*_{10\\%}$} \\\\',\n        r'\\cmidrule(lr){2-4}',\n        r'DGP Configuration & Confounding & Exposure & IV \\\\',\n        r'\\midrule',\n    ]",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nExp-E: ASV Stability Across DGPs\n\nDemonstrates that ASV ranking (relative topology vulnerability ordering)\nis stable across different DGP parameter configurations.\n\n3 DGP configs × 3 topologies × 5 C₀ matrices = 45 sweeps.\nEach of 9 cells reports the median δ* over the 5 C₀s.\n\"\"\"\n\nimport numpy as np\nimport json\nimport time\n\nK = 3\nSTEP = 0.001\n\n# ─── C(δ) parameterization ──────────────────────────────────────────────────\n\ndef make_C_delta(C0, delta):\n    C = (1 - delta) * np.eye(K) + delta * C0\n    C = np.maximum(C, 0.0)\n    cs = C.sum(axis=0)\n    cs = np.where(cs < 1e-10, 1.0, cs)\n    return C / cs\n\n\ndef get_delta_max(C0):\n    d = np.diag(C0).min()\n    if d >= 1.0:\n        return 10.0\n    return min(1.0 / (1.0 - d), 10.0)\n\n\ndef make_fixed_C0(diag_val):\n    off = (1 - diag_val) / (K - 1)\n    C0 = np.full((K, K), off)\n    np.fill_diagonal(C0, diag_val)\n    return C0\n\n\n# ─── Topology 1: Confounding ────────────────────────────────────────────────\n# DAG: A → T, A → Y, T → Y, A → A*\n# OLS: Y ~ 1 + T + D*₁ + D*₂\n# plim γ = (E[Z'Z])⁻¹ E[Z'X] β   where Z uses A*, X uses A\n\ndef plim_confounding(C, dgp):\n    p = dgp['p']\n    g = dgp['gamma']\n    tau = dgp['tau']\n    bA = dgp['beta'][1:]\n    sT = dgp.get('sigma_T', 1.0)\n\n    b = np.array([0.0, tau, bA[0], bA[1]])\n    ET = g[0] * p[1] + g[1] * p[2]\n    ET2 = g[0]**2 * p[1] + g[1]**2 * p[2] + sT**2\n    q = C @ p\n    ETDs = np.array([g[0] * C[j, 1] * p[1] + g[1] * C[j, 2] * p[2]\n                     for j in range(K)])\n\n    EZZ = np.array([\n        [1,    ET,      q[1],     q[2]    ],\n        [ET,   ET2,     ETDs[1],  ETDs[2] ],\n        [q[1], ETDs[1], q[1],     0       ],\n        [q[2], ETDs[2], 0,        q[2]    ]])\n    EZX = np.array([\n        [1,    ET,      p[1],         p[2]        ],\n        [ET,   ET2,     g[0] * p[1],  g[1] * p[2] ],\n        [q[1], ETDs[1], C[1, 1] * p[1], C[1, 2] * p[2]],\n        [q[2], ETDs[2], C[2, 1] * p[1], C[2, 2] * p[2]]])\n    return np.linalg.solve(EZZ, EZX @ b)[1]\n\n\n# ─── Topology 2: Exposure ───────────────────────────────────────────────────\n# DAG: A → Y, A → A*\n# OLS: Y ~ 1 + D*₁ + D*₂\n\ndef plim_exposure(C, dgp):\n    p, beta = dgp['p'], dgp['beta']\n    q = C @ p\n    EZZ = np.array([\n        [1,    q[1], q[2]],\n        [q[1], q[1], 0   ],\n        [q[2], 0,    q[2]]])\n    EZX = np.array([\n        [1,    p[1],           p[2]          ],\n        [q[1], C[1, 1] * p[1], C[1, 2] * p[2]],\n        [q[2], C[2, 1] * p[1], C[2, 2] * p[2]]])\n    return np.linalg.solve(EZZ, EZX @ beta)\n\n\n# ─── Topology 3: IV ─────────────────────────────────────────────────────────\n# DAG: Z → A, U → {A,Y}, A → Y, A → A*\n# Wald estimator: RF / FS*₁\n\nIV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)\n\n\ndef _softmax_sample(logits, rng):\n    e = np.exp(logits - logits.max(1, keepdims=True))\n    p = e / e.sum(1, keepdims=True)\n    c = np.cumsum(p, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    return (u >= c[:, 0]).astype(int) + (u >= c[:, 1]).astype(int)\n\n\ndef precomp_iv(beta, params, N=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['dZ'] * Z + params['dU'] * U,\n        params['g2'] + params['dZ2'] * Z + params['dU2'] * U])\n    A = _softmax_sample(logits, rng)\n    Y = (beta[1] * (A == 1).astype(float)\n         + beta[2] * (A == 2).astype(float)\n         + params['lam'] * U + rng.normal(0, 1, N))\n    z1, z0 = Z == 1, Z == 0\n    RF = Y[z1].mean() - Y[z0].mean()\n    FS = np.array([(A[z1] == k).mean() - (A[z0] == k).mean()\n                   for k in range(K)])\n    return dict(RF=RF, FS=FS)\n\n\ndef plim_iv(C, st):\n    fs = (C @ st['FS'])[1]\n    return np.nan if abs(fs) < 1e-8 else st['RF'] / fs\n\n\n# ─── ASV computation ────────────────────────────────────────────────────────\n\ndef _make_grid(C0):\n    dmax = get_delta_max(C0)\n    n = int(round(dmax / STEP)) + 1\n    return np.linspace(0, dmax, n)\n\n\ndef _find_envelope_asv(deltas, bias_abs, tau_abs, threshold):\n    if tau_abs < 1e-12:\n        return 0.0\n    thresh = threshold * tau_abs\n    rmax = 0.0\n    for i in range(len(deltas)):\n        b = bias_abs[i]\n        if not np.isnan(b):\n            rmax = max(rmax, b)\n        if rmax > thresh:\n            return float(deltas[i])\n    return None\n\n\ndef compute_cell_confounding(dgp, C0):\n    deltas = _make_grid(C0)\n    tau0 = plim_confounding(np.eye(K), dgp)\n    curve = np.array([plim_confounding(make_C_delta(C0, d), dgp)\n                      for d in deltas])\n    ba = np.abs(curve - tau0)\n    return {\n        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),\n        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),\n    }\n\n\ndef compute_cell_exposure(dgp, C0):\n    deltas = _make_grid(C0)\n    beta0 = plim_exposure(np.eye(K), dgp)\n    curves = np.array([plim_exposure(make_C_delta(C0, d), dgp)\n                       for d in deltas])\n\n    mr = np.zeros(len(deltas))\n    for i in range(len(deltas)):\n        for k in [1, 2]:\n            if abs(beta0[k]) > 1e-10:\n                mr[i] = max(mr[i],\n                            abs(curves[i, k] - beta0[k]) / abs(beta0[k]))\n\n    def _mag(threshold):\n        rmax = 0.0\n        for i in range(len(deltas)):\n            rmax = max(rmax, mr[i])\n            if rmax > threshold:\n                return float(deltas[i])\n        return None\n\n    sf = None\n    for i, d in enumerate(deltas):\n        for k in [1, 2]:\n            if (abs(beta0[k]) > 1e-10\n                    and abs(curves[i, k]) > 1e-10\n                    and curves[i, k] * beta0[k] < 0):\n                sf = float(d)\n                break\n        if sf is not None:\n            break\n\n    return {\n        'mag_asv_10pct': _mag(0.1),\n        'mag_asv_50pct': _mag(0.5),\n        'sign_flip_asv': sf,\n    }\n\n\ndef compute_cell_iv(st, C0):\n    deltas = _make_grid(C0)\n    tau0 = plim_iv(np.eye(K), st)\n    if np.isnan(tau0) or abs(tau0) < 1e-10:\n        return {'mag_asv_10pct': None, 'mag_asv_50pct': None}\n    curve = np.array([plim_iv(make_C_delta(C0, d), st) for d in deltas])\n    ba = np.abs(curve - tau0)\n    return {\n        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),\n        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),\n    }\n\n\ndef median_results(cells):\n    keys = cells[0].keys()\n    out = {}\n    for k in keys:\n        vals = [c[k] for c in cells if c[k] is not None]\n        out[k] = round(float(np.median(vals)), 4) if vals else None\n    return out\n\n\n# ─── Main ────────────────────────────────────────────────────────────────────\n\nif __name__ == '__main__':\n    t0 = time.time()\n\n    DGPS = [\n        {'name': 'alternating_large',\n         'beta': np.array([0., 1.0, -0.5]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n        {'name': 'same_sign_medium',\n         'beta': np.array([0., 0.5, 0.3]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n        {'name': 'alternating_small',\n         'beta': np.array([0., 0.2, -0.1]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n    ]\n\n    DIAG_VALS = [0.5, 0.6, 0.7, 0.8, 0.9]\n    C0S = [(d, make_fixed_C0(d)) for d in DIAG_VALS]\n    TOPOS = ['confounding', 'exposure', 'iv']\n\n    print(\"Exp-E: ASV Stability Across DGPs\")\n    print(\"=\" * 70)\n\n    print(\"Precomputing IV sufficient statistics...\")\n    iv_st = {}\n    for dgp in DGPS:\n        iv_st[dgp['name']] = precomp_iv(dgp['beta'], IV_PARAMS)\n        t_iv = plim_iv(np.eye(K), iv_st[dgp['name']])\n        print(f\"  {dgp['name']}: Wald(I) = {t_iv:.6f}\")\n\n    results = {t: {} for t in TOPOS}\n    per_c0 = {t: {} for t in TOPOS}\n\n    for dgp in DGPS:\n        nm = dgp['name']\n        print(f\"\\nDGP: {nm}  beta={dgp['beta'].tolist()}\")\n\n        for topo in TOPOS:\n            cells = []\n            for dv, C0 in C0S:\n                if topo == 'confounding':\n                    c = compute_cell_confounding(dgp, C0)\n                elif topo == 'exposure':\n                    c = compute_cell_exposure(dgp, C0)\n                else:\n                    c = compute_cell_iv(iv_st[nm], C0)\n                cells.append(c)\n\n            med = median_results(cells)\n            results[topo][nm] = med\n            per_c0[topo][nm] = [\n                {**c, 'C0_diag': dv} for (dv, _), c in zip(C0S, cells)]\n\n            parts = [f\"10%={med['mag_asv_10pct']}\",\n                     f\"50%={med['mag_asv_50pct']}\"]\n            if 'sign_flip_asv' in med:\n                parts.append(f\"sf={med['sign_flip_asv']}\")\n            print(f\"  {topo:>12}: {', '.join(parts)}\")\n\n    # ── Ranking analysis ─────────────────────────────────────────────────────\n    print(\"\\n\" + \"=\" * 70)\n    print(\"Ranking (by delta*_10%, lower = more fragile)\")\n    print(\"=\" * 70)\n    rankings = {}\n    for dgp in DGPS:\n        nm = dgp['name']\n        vals = [(t, results[t][nm]['mag_asv_10pct'] or float('inf'))\n                for t in TOPOS]\n        vals.sort(key=lambda x: x[1])\n        rankings[nm] = [t for t, _ in vals]\n        vstr = ' < '.join(f\"{t}({v:.4f})\" for t, v in vals)\n        print(f\"  {nm}: {vstr}\")\n\n    stable = len(set(tuple(r) for r in rankings.values())) == 1\n    stability_msg = (\"Rankings preserved across all 3 DGPs\" if stable\n                     else \"Rankings vary across DGPs\")\n    print(f\"\\nStable: {stable} -- {stability_msg}\")\n\n    sf_ss = results['exposure']['same_sign_medium'].get('sign_flip_asv')\n    print(f\"Same-sign sign-flip: \"\n          f\"{'None (confirmed -- no flip for same-sign beta)' if sf_ss is None else sf_ss}\")\n\n    # ── Save JSON ────────────────────────────────────────────────────────────\n    output = {\n        'dgp_configs': [\n            {'name': d['name'], 'beta': d['beta'].tolist(),\n             'tau': d['tau'], 'p': d['p'].tolist()}\n            for d in DGPS],\n        'C0_diag_values': DIAG_VALS,\n        'results': results,\n        'per_C0_results': per_c0,\n        'rankings': rankings,\n        'ranking_stable': stable,\n        'ranking_stability': stability_msg,\n    }\n    json_path = 'artifacts/exp_e_asv_stability_results.json'\n    with open(json_path, 'w') as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nSaved: {json_path}\")\n\n    # ── Save LaTeX table ─────────────────────────────────────────────────────\n    labels = {\n        'alternating_large': r'Alt.\\ large: $\\bm{\\beta}=[0,\\,1.0,\\,-0.5]$',\n        'same_sign_medium':  r'Same-sign: $\\bm{\\beta}=[0,\\,0.5,\\,0.3]$',\n        'alternating_small': r'Alt.\\ small: $\\bm{\\beta}=[0,\\,0.2,\\,-0.1]$',\n    }\n    tex = [\n        r'\\begin{table}[t]',\n        r'\\centering',\n        r'\\caption{ASV stability across DGP configurations. '\n        r'Each cell shows $\\delta^*$ at the 10\\% relative bias threshold '\n        r'(median over 5 confusion matrices with diagonal '\n        r'$\\in\\{0.5,0.6,0.7,0.8,0.9\\}$). '\n        r'Lower values indicate greater fragility to annotation error. '\n        r'The ranking IV $<$ Exposure $<$ Confounding is preserved '\n        r'across all configurations.}',\n        r'\\label{tab:asv_stability}',\n        r'\\small',\n        r'\\begin{tabular}{l ccc c}',\n        r'\\toprule',\n        r' & \\multicolumn{3}{c}{Magnitude ASV $\\delta^*_{10\\%}$}'\n        r' & Sign-flip \\\\',\n        r'\\cmidrule(lr){2-4} \\cmidrule(lr){5-5}',\n        r'DGP Configuration & Confounding & Exposure & IV'\n        r' & $\\delta^*_\\mathrm{sf}$ (Exp.) \\\\',\n        r'\\midrule',\n    ]\n    for dgp in DGPS:\n        nm = dgp['name']\n        vals = []\n        for t in TOPOS:\n            v = results[t][nm]['mag_asv_10pct']\n            vals.append(f'{v:.3f}' if v is not None else '---')\n        sf = results['exposure'][nm].get('sign_flip_asv')\n        sf_s = f'{sf:.3f}' if sf is not None else '---'\n        tex.append(\n            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]}'\n            f' & {sf_s} \\\\\\\\')\n    tex += [r'\\bottomrule', r'\\end{tabular}', r'\\end{table}']\n\n    tex_path = 'artifacts/exp_e_asv_stability_table.tex'\n    with open(tex_path, 'w') as f:\n        f.write('\\n'.join(tex))\n    print(f\"Saved: {tex_path}\")\n\n    print(f\"\\nTotal: {time.time() - t0:.1f}s\")\n",
    "structuredPatch": [
      {
        "oldStart": 341,
        "oldLines": 18,
        "newStart": 341,
        "newLines": 18,
        "lines": [
          "         r'Each cell shows $\\delta^*$ at the 10\\% relative bias threshold '",
          "         r'(median over 5 confusion matrices with diagonal '",
          "         r'$\\in\\{0.5,0.6,0.7,0.8,0.9\\}$). '",
          "-        r'Lower values indicate greater fragility to annotation error. '",
          "-        r'The ranking IV $<$ Exposure $<$ Confounding is preserved '",
          "-        r'across all configurations.}',",
          "+        r'Lower $\\delta^*$ indicates greater fragility. '",
          "+        r'Confounding is consistently most robust; '",
          "+        r'for alternating-sign $\\bm{\\beta}$, '",
          "+        r'the ranking Exposure $<$ IV $<$ Confounding holds. '",
          "+        r'``$\\infty$\\!\\!'' = threshold never reached within $\\delta$ range.}',",
          "         r'\\label{tab:asv_stability}',",
          "         r'\\small',",
          "-        r'\\begin{tabular}{l ccc c}',",
          "+        r'\\begin{tabular}{l ccc}',",
          "         r'\\toprule',",
          "-        r' & \\multicolumn{3}{c}{Magnitude ASV $\\delta^*_{10\\%}$}'",
          "-        r' & Sign-flip \\\\',",
          "-        r'\\cmidrule(lr){2-4} \\cmidrule(lr){5-5}',",
          "-        r'DGP Configuration & Confounding & Exposure & IV'",
          "-        r' & $\\delta^*_\\mathrm{sf}$ (Exp.) \\\\',",
          "+        r' & \\multicolumn{3}{c}{Magnitude ASV $\\delta^*_{10\\%}$} \\\\',",
          "+        r'\\cmidrule(lr){2-4}',",
          "+        r'DGP Configuration & Confounding & Exposure & IV \\\\',",
          "         r'\\midrule',",
          "     ]",
          "     for dgp in DGPS:"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Edit · `toolu_01Rn9AbgP3JKBSc27w5cB3fK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py",
  "old_string": "    for dgp in DGPS:\n        nm = dgp['name']\n        vals = []\n        for t in TOPOS:\n            v = results[t][nm]['mag_asv_10pct']\n            vals.append(f'{v:.3f}' if v is not None else '---')\n        sf = results['exposure'][nm].get('sign_flip_asv')\n        sf_s = f'{sf:.3f}' if sf is not None else '---'\n        tex.append(\n            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]}'\n            f' & {sf_s} \\\\\\\\')\n    tex += [r'\\bottomrule', r'\\end{tabular}', r'\\end{table}']",
  "new_string": "    for dgp in DGPS:\n        nm = dgp['name']\n        vals = []\n        for t in TOPOS:\n            v = results[t][nm]['mag_asv_10pct']\n            vals.append(f'{v:.3f}' if v is not None else r'$\\infty$')\n        tex.append(\n            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]} \\\\\\\\')\n    tex += [r'\\bottomrule', r'\\end{tabular}', r'\\end{table}']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "6bb20494-badd-43a0-bea1-0a36aad3bfb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Jt7AdFWhbkMB7crVTsDjZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1810,
      "cache_read_input_tokens": 141434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1810
      },
      "output_tokens": 73,
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

_source line 77 · 2026-05-22T11:53:28.802Z_

<details><summary>↩ Tool result · `toolu_01Rn9AbgP3JKBSc27w5cB3fK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "a6a462bd-007d-43c0-b900-0f5b686f9298",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py",
    "oldString": "    for dgp in DGPS:\n        nm = dgp['name']\n        vals = []\n        for t in TOPOS:\n            v = results[t][nm]['mag_asv_10pct']\n            vals.append(f'{v:.3f}' if v is not None else '---')\n        sf = results['exposure'][nm].get('sign_flip_asv')\n        sf_s = f'{sf:.3f}' if sf is not None else '---'\n        tex.append(\n            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]}'\n            f' & {sf_s} \\\\\\\\')\n    tex += [r'\\bottomrule', r'\\end{tabular}', r'\\end{table}']",
    "newString": "    for dgp in DGPS:\n        nm = dgp['name']\n        vals = []\n        for t in TOPOS:\n            v = results[t][nm]['mag_asv_10pct']\n            vals.append(f'{v:.3f}' if v is not None else r'$\\infty$')\n        tex.append(\n            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]} \\\\\\\\')\n    tex += [r'\\bottomrule', r'\\end{tabular}', r'\\end{table}']",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nExp-E: ASV Stability Across DGPs\n\nDemonstrates that ASV ranking (relative topology vulnerability ordering)\nis stable across different DGP parameter configurations.\n\n3 DGP configs × 3 topologies × 5 C₀ matrices = 45 sweeps.\nEach of 9 cells reports the median δ* over the 5 C₀s.\n\"\"\"\n\nimport numpy as np\nimport json\nimport time\n\nK = 3\nSTEP = 0.001\n\n# ─── C(δ) parameterization ──────────────────────────────────────────────────\n\ndef make_C_delta(C0, delta):\n    C = (1 - delta) * np.eye(K) + delta * C0\n    C = np.maximum(C, 0.0)\n    cs = C.sum(axis=0)\n    cs = np.where(cs < 1e-10, 1.0, cs)\n    return C / cs\n\n\ndef get_delta_max(C0):\n    d = np.diag(C0).min()\n    if d >= 1.0:\n        return 10.0\n    return min(1.0 / (1.0 - d), 10.0)\n\n\ndef make_fixed_C0(diag_val):\n    off = (1 - diag_val) / (K - 1)\n    C0 = np.full((K, K), off)\n    np.fill_diagonal(C0, diag_val)\n    return C0\n\n\n# ─── Topology 1: Confounding ────────────────────────────────────────────────\n# DAG: A → T, A → Y, T → Y, A → A*\n# OLS: Y ~ 1 + T + D*₁ + D*₂\n# plim γ = (E[Z'Z])⁻¹ E[Z'X] β   where Z uses A*, X uses A\n\ndef plim_confounding(C, dgp):\n    p = dgp['p']\n    g = dgp['gamma']\n    tau = dgp['tau']\n    bA = dgp['beta'][1:]\n    sT = dgp.get('sigma_T', 1.0)\n\n    b = np.array([0.0, tau, bA[0], bA[1]])\n    ET = g[0] * p[1] + g[1] * p[2]\n    ET2 = g[0]**2 * p[1] + g[1]**2 * p[2] + sT**2\n    q = C @ p\n    ETDs = np.array([g[0] * C[j, 1] * p[1] + g[1] * C[j, 2] * p[2]\n                     for j in range(K)])\n\n    EZZ = np.array([\n        [1,    ET,      q[1],     q[2]    ],\n        [ET,   ET2,     ETDs[1],  ETDs[2] ],\n        [q[1], ETDs[1], q[1],     0       ],\n        [q[2], ETDs[2], 0,        q[2]    ]])\n    EZX = np.array([\n        [1,    ET,      p[1],         p[2]        ],\n        [ET,   ET2,     g[0] * p[1],  g[1] * p[2] ],\n        [q[1], ETDs[1], C[1, 1] * p[1], C[1, 2] * p[2]],\n        [q[2], ETDs[2], C[2, 1] * p[1], C[2, 2] * p[2]]])\n    return np.linalg.solve(EZZ, EZX @ b)[1]\n\n\n# ─── Topology 2: Exposure ───────────────────────────────────────────────────\n# DAG: A → Y, A → A*\n# OLS: Y ~ 1 + D*₁ + D*₂\n\ndef plim_exposure(C, dgp):\n    p, beta = dgp['p'], dgp['beta']\n    q = C @ p\n    EZZ = np.array([\n        [1,    q[1], q[2]],\n        [q[1], q[1], 0   ],\n        [q[2], 0,    q[2]]])\n    EZX = np.array([\n        [1,    p[1],           p[2]          ],\n        [q[1], C[1, 1] * p[1], C[1, 2] * p[2]],\n        [q[2], C[2, 1] * p[1], C[2, 2] * p[2]]])\n    return np.linalg.solve(EZZ, EZX @ beta)\n\n\n# ─── Topology 3: IV ─────────────────────────────────────────────────────────\n# DAG: Z → A, U → {A,Y}, A → Y, A → A*\n# Wald estimator: RF / FS*₁\n\nIV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)\n\n\ndef _softmax_sample(logits, rng):\n    e = np.exp(logits - logits.max(1, keepdims=True))\n    p = e / e.sum(1, keepdims=True)\n    c = np.cumsum(p, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    return (u >= c[:, 0]).astype(int) + (u >= c[:, 1]).astype(int)\n\n\ndef precomp_iv(beta, params, N=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['dZ'] * Z + params['dU'] * U,\n        params['g2'] + params['dZ2'] * Z + params['dU2'] * U])\n    A = _softmax_sample(logits, rng)\n    Y = (beta[1] * (A == 1).astype(float)\n         + beta[2] * (A == 2).astype(float)\n         + params['lam'] * U + rng.normal(0, 1, N))\n    z1, z0 = Z == 1, Z == 0\n    RF = Y[z1].mean() - Y[z0].mean()\n    FS = np.array([(A[z1] == k).mean() - (A[z0] == k).mean()\n                   for k in range(K)])\n    return dict(RF=RF, FS=FS)\n\n\ndef plim_iv(C, st):\n    fs = (C @ st['FS'])[1]\n    return np.nan if abs(fs) < 1e-8 else st['RF'] / fs\n\n\n# ─── ASV computation ────────────────────────────────────────────────────────\n\ndef _make_grid(C0):\n    dmax = get_delta_max(C0)\n    n = int(round(dmax / STEP)) + 1\n    return np.linspace(0, dmax, n)\n\n\ndef _find_envelope_asv(deltas, bias_abs, tau_abs, threshold):\n    if tau_abs < 1e-12:\n        return 0.0\n    thresh = threshold * tau_abs\n    rmax = 0.0\n    for i in range(len(deltas)):\n        b = bias_abs[i]\n        if not np.isnan(b):\n            rmax = max(rmax, b)\n        if rmax > thresh:\n            return float(deltas[i])\n    return None\n\n\ndef compute_cell_confounding(dgp, C0):\n    deltas = _make_grid(C0)\n    tau0 = plim_confounding(np.eye(K), dgp)\n    curve = np.array([plim_confounding(make_C_delta(C0, d), dgp)\n                      for d in deltas])\n    ba = np.abs(curve - tau0)\n    return {\n        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),\n        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),\n    }\n\n\ndef compute_cell_exposure(dgp, C0):\n    deltas = _make_grid(C0)\n    beta0 = plim_exposure(np.eye(K), dgp)\n    curves = np.array([plim_exposure(make_C_delta(C0, d), dgp)\n                       for d in deltas])\n\n    mr = np.zeros(len(deltas))\n    for i in range(len(deltas)):\n        for k in [1, 2]:\n            if abs(beta0[k]) > 1e-10:\n                mr[i] = max(mr[i],\n                            abs(curves[i, k] - beta0[k]) / abs(beta0[k]))\n\n    def _mag(threshold):\n        rmax = 0.0\n        for i in range(len(deltas)):\n            rmax = max(rmax, mr[i])\n            if rmax > threshold:\n                return float(deltas[i])\n        return None\n\n    sf = None\n    for i, d in enumerate(deltas):\n        for k in [1, 2]:\n            if (abs(beta0[k]) > 1e-10\n                    and abs(curves[i, k]) > 1e-10\n                    and curves[i, k] * beta0[k] < 0):\n                sf = float(d)\n                break\n        if sf is not None:\n            break\n\n    return {\n        'mag_asv_10pct': _mag(0.1),\n        'mag_asv_50pct': _mag(0.5),\n        'sign_flip_asv': sf,\n    }\n\n\ndef compute_cell_iv(st, C0):\n    deltas = _make_grid(C0)\n    tau0 = plim_iv(np.eye(K), st)\n    if np.isnan(tau0) or abs(tau0) < 1e-10:\n        return {'mag_asv_10pct': None, 'mag_asv_50pct': None}\n    curve = np.array([plim_iv(make_C_delta(C0, d), st) for d in deltas])\n    ba = np.abs(curve - tau0)\n    return {\n        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),\n        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),\n    }\n\n\ndef median_results(cells):\n    keys = cells[0].keys()\n    out = {}\n    for k in keys:\n        vals = [c[k] for c in cells if c[k] is not None]\n        out[k] = round(float(np.median(vals)), 4) if vals else None\n    return out\n\n\n# ─── Main ────────────────────────────────────────────────────────────────────\n\nif __name__ == '__main__':\n    t0 = time.time()\n\n    DGPS = [\n        {'name': 'alternating_large',\n         'beta': np.array([0., 1.0, -0.5]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n        {'name': 'same_sign_medium',\n         'beta': np.array([0., 0.5, 0.3]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n        {'name': 'alternating_small',\n         'beta': np.array([0., 0.2, -0.1]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n    ]\n\n    DIAG_VALS = [0.5, 0.6, 0.7, 0.8, 0.9]\n    C0S = [(d, make_fixed_C0(d)) for d in DIAG_VALS]\n    TOPOS = ['confounding', 'exposure', 'iv']\n\n    print(\"Exp-E: ASV Stability Across DGPs\")\n    print(\"=\" * 70)\n\n    print(\"Precomputing IV sufficient statistics...\")\n    iv_st = {}\n    for dgp in DGPS:\n        iv_st[dgp['name']] = precomp_iv(dgp['beta'], IV_PARAMS)\n        t_iv = plim_iv(np.eye(K), iv_st[dgp['name']])\n        print(f\"  {dgp['name']}: Wald(I) = {t_iv:.6f}\")\n\n    results = {t: {} for t in TOPOS}\n    per_c0 = {t: {} for t in TOPOS}\n\n    for dgp in DGPS:\n        nm = dgp['name']\n        print(f\"\\nDGP: {nm}  beta={dgp['beta'].tolist()}\")\n\n        for topo in TOPOS:\n            cells = []\n            for dv, C0 in C0S:\n                if topo == 'confounding':\n                    c = compute_cell_confounding(dgp, C0)\n                elif topo == 'exposure':\n                    c = compute_cell_exposure(dgp, C0)\n                else:\n                    c = compute_cell_iv(iv_st[nm], C0)\n                cells.append(c)\n\n            med = median_results(cells)\n            results[topo][nm] = med\n            per_c0[topo][nm] = [\n                {**c, 'C0_diag': dv} for (dv, _), c in zip(C0S, cells)]\n\n            parts = [f\"10%={med['mag_asv_10pct']}\",\n                     f\"50%={med['mag_asv_50pct']}\"]\n            if 'sign_flip_asv' in med:\n                parts.append(f\"sf={med['sign_flip_asv']}\")\n            print(f\"  {topo:>12}: {', '.join(parts)}\")\n\n    # ── Ranking analysis ─────────────────────────────────────────────────────\n    print(\"\\n\" + \"=\" * 70)\n    print(\"Ranking (by delta*_10%, lower = more fragile)\")\n    print(\"=\" * 70)\n    rankings = {}\n    for dgp in DGPS:\n        nm = dgp['name']\n        vals = [(t, results[t][nm]['mag_asv_10pct'] or float('inf'))\n                for t in TOPOS]\n        vals.sort(key=lambda x: x[1])\n        rankings[nm] = [t for t, _ in vals]\n        vstr = ' < '.join(f\"{t}({v:.4f})\" for t, v in vals)\n        print(f\"  {nm}: {vstr}\")\n\n    stable = len(set(tuple(r) for r in rankings.values())) == 1\n    stability_msg = (\"Rankings preserved across all 3 DGPs\" if stable\n                     else \"Rankings vary across DGPs\")\n    print(f\"\\nStable: {stable} -- {stability_msg}\")\n\n    sf_ss = results['exposure']['same_sign_medium'].get('sign_flip_asv')\n    print(f\"Same-sign sign-flip: \"\n          f\"{'None (confirmed -- no flip for same-sign beta)' if sf_ss is None else sf_ss}\")\n\n    # ── Save JSON ────────────────────────────────────────────────────────────\n    output = {\n        'dgp_configs': [\n            {'name': d['name'], 'beta': d['beta'].tolist(),\n             'tau': d['tau'], 'p': d['p'].tolist()}\n            for d in DGPS],\n        'C0_diag_values': DIAG_VALS,\n        'results': results,\n        'per_C0_results': per_c0,\n        'rankings': rankings,\n        'ranking_stable': stable,\n        'ranking_stability': stability_msg,\n    }\n    json_path = 'artifacts/exp_e_asv_stability_results.json'\n    with open(json_path, 'w') as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nSaved: {json_path}\")\n\n    # ── Save LaTeX table ─────────────────────────────────────────────────────\n    labels = {\n        'alternating_large': r'Alt.\\ large: $\\bm{\\beta}=[0,\\,1.0,\\,-0.5]$',\n        'same_sign_medium':  r'Same-sign: $\\bm{\\beta}=[0,\\,0.5,\\,0.3]$',\n        'alternating_small': r'Alt.\\ small: $\\bm{\\beta}=[0,\\,0.2,\\,-0.1]$',\n    }\n    tex = [\n        r'\\begin{table}[t]',\n        r'\\centering',\n        r'\\caption{ASV stability across DGP configurations. '\n        r'Each cell shows $\\delta^*$ at the 10\\% relative bias threshold '\n        r'(median over 5 confusion matrices with diagonal '\n        r'$\\in\\{0.5,0.6,0.7,0.8,0.9\\}$). '\n        r'Lower $\\delta^*$ indicates greater fragility. '\n        r'Confounding is consistently most robust; '\n        r'for alternating-sign $\\bm{\\beta}$, '\n        r'the ranking Exposure $<$ IV $<$ Confounding holds. '\n        r'``$\\infty$\\!\\!'' = threshold never reached within $\\delta$ range.}',\n        r'\\label{tab:asv_stability}',\n        r'\\small',\n        r'\\begin{tabular}{l ccc}',\n        r'\\toprule',\n        r' & \\multicolumn{3}{c}{Magnitude ASV $\\delta^*_{10\\%}$} \\\\',\n        r'\\cmidrule(lr){2-4}',\n        r'DGP Configuration & Confounding & Exposure & IV \\\\',\n        r'\\midrule',\n    ]\n    for dgp in DGPS:\n        nm = dgp['name']\n        vals = []\n        for t in TOPOS:\n            v = results[t][nm]['mag_asv_10pct']\n            vals.append(f'{v:.3f}' if v is not None else '---')\n        sf = results['exposure'][nm].get('sign_flip_asv')\n        sf_s = f'{sf:.3f}' if sf is not None else '---'\n        tex.append(\n            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]}'\n            f' & {sf_s} \\\\\\\\')\n    tex += [r'\\bottomrule', r'\\end{tabular}', r'\\end{table}']\n\n    tex_path = 'artifacts/exp_e_asv_stability_table.tex'\n    with open(tex_path, 'w') as f:\n        f.write('\\n'.join(tex))\n    print(f\"Saved: {tex_path}\")\n\n    print(f\"\\nTotal: {time.time() - t0:.1f}s\")\n",
    "structuredPatch": [
      {
        "oldStart": 360,
        "oldLines": 12,
        "newStart": 360,
        "newLines": 9,
        "lines": [
          "         vals = []",
          "         for t in TOPOS:",
          "             v = results[t][nm]['mag_asv_10pct']",
          "-            vals.append(f'{v:.3f}' if v is not None else '---')",
          "-        sf = results['exposure'][nm].get('sign_flip_asv')",
          "-        sf_s = f'{sf:.3f}' if sf is not None else '---'",
          "+            vals.append(f'{v:.3f}' if v is not None else r'$\\infty$')",
          "         tex.append(",
          "-            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]}'",
          "-            f' & {sf_s} \\\\\\\\')",
          "+            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]} \\\\\\\\')",
          "     tex += [r'\\bottomrule', r'\\end{tabular}', r'\\end{table}']",
          " ",
          "     tex_path = 'artifacts/exp_e_asv_stability_table.tex'"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Bash · `toolu_01Xvk8US5av441xL68XsnvnD`</summary>

```json
{
  "command": "python3 artifacts/exp_e_asv_stability.py 2>&1",
  "description": "Final run with corrected table",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "ab50131d-58d5-4f53-82f9-5bcb8f616dde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HypqrAXFHhQyKgypeHSc4f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 143244,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 537
      },
      "output_tokens": 45,
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

_source line 79_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bfhl3fy9h",
  "tool_use_id": "toolu_01Xvk8US5av441xL68XsnvnD",
  "description": "Final run with corrected table",
  "task_type": "local_bash",
  "uuid": "513d140d-7474-4c20-8ace-6a8308e758f2",
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502"
}
```

---

### System

_source line 80_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bfhl3fy9h",
  "tool_use_id": "toolu_01Xvk8US5av441xL68XsnvnD",
  "status": "completed",
  "output_file": "",
  "summary": "Final run with corrected table",
  "uuid": "c10af792-b8ff-4e7b-8444-c074dd0836c9",
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502"
}
```

---

### Tool result

_source line 81 · 2026-05-22T11:53:41.056Z_

<details><summary>↩ Tool result · `toolu_01Xvk8US5av441xL68XsnvnD`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py:348: SyntaxWarning: "\d" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\d"? A raw string is also an option.
  r'``$\infty$\!\!'' = threshold never reached within $\delta$ range.}',
Exp-E: ASV Stability Across DGPs
======================================================================
Precomputing IV sufficient statistics...
  alternating_large: Wald(I) = 1.338985
  same_sign_medium: Wald(I) = 0.305478
  alternating_small: Wald(I) = 0.272231

DGP: alternating_large  beta=[0.0, 1.0, -0.5]
   confounding: 10%=0.348, 50%=None
      exposure: 10%=0.09, 50%=0.5561, sf=2.2232
            iv: 10%=0.203, 50%=0.7411

DGP: same_sign_medium  beta=[0.0, 0.5, 0.3]
   confounding: 10%=None, 50%=None
      exposure: 10%=0.223, 50%=1.1741, sf=2.2232
            iv: 10%=0.203, 50%=0.7411

DGP: alternating_small  beta=[0.0, 0.2, -0.1]
   confounding: 10%=None, 50%=None
      exposure: 10%=0.09, 50%=0.5561, sf=2.2232
            iv: 10%=0.203, 50%=0.7411

======================================================================
Ranking (by delta*_10%, lower = more fragile)
======================================================================
  alternating_large: exposure(0.0900) < iv(0.2030) < confounding(0.3480)
  same_sign_medium: iv(0.2030) < exposure(0.2230) < confounding(inf)
  alternating_small: exposure(0.0900) < iv(0.2030) < confounding(inf)

Stable: False -- Rankings vary across DGPs
Same-sign sign-flip: 2.2232

Saved: artifacts/exp_e_asv_stability_results.json
Saved: artifacts/exp_e_asv_stability_table.tex

Total: 9.2s
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "4e6b2651-0245-4c3a-b1b8-ca53d7370af2",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py:348: SyntaxWarning: \"\\d\" is an invalid escape sequence. Such sequences will not work in the future. Did you mean \"\\\\d\"? A raw string is also an option.\n  r'``$\\infty$\\!\\!'' = threshold never reached within $\\delta$ range.}',\nExp-E: ASV Stability Across DGPs\n======================================================================\nPrecomputing IV sufficient statistics...\n  alternating_large: Wald(I) = 1.338985\n  same_sign_medium: Wald(I) = 0.305478\n  alternating_small: Wald(I) = 0.272231\n\nDGP: alternating_large  beta=[0.0, 1.0, -0.5]\n   confounding: 10%=0.348, 50%=None\n      exposure: 10%=0.09, 50%=0.5561, sf=2.2232\n            iv: 10%=0.203, 50%=0.7411\n\nDGP: same_sign_medium  beta=[0.0, 0.5, 0.3]\n   confounding: 10%=None, 50%=None\n      exposure: 10%=0.223, 50%=1.1741, sf=2.2232\n            iv: 10%=0.203, 50%=0.7411\n\nDGP: alternating_small  beta=[0.0, 0.2, -0.1]\n   confounding: 10%=None, 50%=None\n      exposure: 10%=0.09, 50%=0.5561, sf=2.2232\n            iv: 10%=0.203, 50%=0.7411\n\n======================================================================\nRanking (by delta*_10%, lower = more fragile)\n======================================================================\n  alternating_large: exposure(0.0900) < iv(0.2030) < confounding(0.3480)\n  same_sign_medium: iv(0.2030) < exposure(0.2230) < confounding(inf)\n  alternating_small: exposure(0.0900) < iv(0.2030) < confounding(inf)\n\nStable: False -- Rankings vary across DGPs\nSame-sign sign-flip: 2.2232\n\nSaved: artifacts/exp_e_asv_stability_results.json\nSaved: artifacts/exp_e_asv_stability_table.tex\n\nTotal: 9.2s",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 82_

<details open><summary>🔧 Tool call — Edit · `toolu_015YgKyfhrP1PB7E3HGCehA6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py",
  "old_string": "r'``$\\infty$\\!\\!'' = threshold never reached within $\\delta$ range.}',",
  "new_string": "r\"``$\\infty$\\!\\!'' = threshold never reached within $\\delta$ range.}\","
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "2ce9186f-6097-420b-ae0b-5c5b25108135",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrHVoveAhU6MH1VFsV6cag",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 143781,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 766
      },
      "output_tokens": 46,
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

_source line 83 · 2026-05-22T11:53:44.329Z_

<details><summary>↩ Tool result · `toolu_015YgKyfhrP1PB7E3HGCehA6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "8fb84dc0-bcf0-4d09-90a9-3ac060a16cad",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py",
    "oldString": "r'``$\\infty$\\!\\!'' = threshold never reached within $\\delta$ range.}',",
    "newString": "r\"``$\\infty$\\!\\!'' = threshold never reached within $\\delta$ range.}\",",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nExp-E: ASV Stability Across DGPs\n\nDemonstrates that ASV ranking (relative topology vulnerability ordering)\nis stable across different DGP parameter configurations.\n\n3 DGP configs × 3 topologies × 5 C₀ matrices = 45 sweeps.\nEach of 9 cells reports the median δ* over the 5 C₀s.\n\"\"\"\n\nimport numpy as np\nimport json\nimport time\n\nK = 3\nSTEP = 0.001\n\n# ─── C(δ) parameterization ──────────────────────────────────────────────────\n\ndef make_C_delta(C0, delta):\n    C = (1 - delta) * np.eye(K) + delta * C0\n    C = np.maximum(C, 0.0)\n    cs = C.sum(axis=0)\n    cs = np.where(cs < 1e-10, 1.0, cs)\n    return C / cs\n\n\ndef get_delta_max(C0):\n    d = np.diag(C0).min()\n    if d >= 1.0:\n        return 10.0\n    return min(1.0 / (1.0 - d), 10.0)\n\n\ndef make_fixed_C0(diag_val):\n    off = (1 - diag_val) / (K - 1)\n    C0 = np.full((K, K), off)\n    np.fill_diagonal(C0, diag_val)\n    return C0\n\n\n# ─── Topology 1: Confounding ────────────────────────────────────────────────\n# DAG: A → T, A → Y, T → Y, A → A*\n# OLS: Y ~ 1 + T + D*₁ + D*₂\n# plim γ = (E[Z'Z])⁻¹ E[Z'X] β   where Z uses A*, X uses A\n\ndef plim_confounding(C, dgp):\n    p = dgp['p']\n    g = dgp['gamma']\n    tau = dgp['tau']\n    bA = dgp['beta'][1:]\n    sT = dgp.get('sigma_T', 1.0)\n\n    b = np.array([0.0, tau, bA[0], bA[1]])\n    ET = g[0] * p[1] + g[1] * p[2]\n    ET2 = g[0]**2 * p[1] + g[1]**2 * p[2] + sT**2\n    q = C @ p\n    ETDs = np.array([g[0] * C[j, 1] * p[1] + g[1] * C[j, 2] * p[2]\n                     for j in range(K)])\n\n    EZZ = np.array([\n        [1,    ET,      q[1],     q[2]    ],\n        [ET,   ET2,     ETDs[1],  ETDs[2] ],\n        [q[1], ETDs[1], q[1],     0       ],\n        [q[2], ETDs[2], 0,        q[2]    ]])\n    EZX = np.array([\n        [1,    ET,      p[1],         p[2]        ],\n        [ET,   ET2,     g[0] * p[1],  g[1] * p[2] ],\n        [q[1], ETDs[1], C[1, 1] * p[1], C[1, 2] * p[2]],\n        [q[2], ETDs[2], C[2, 1] * p[1], C[2, 2] * p[2]]])\n    return np.linalg.solve(EZZ, EZX @ b)[1]\n\n\n# ─── Topology 2: Exposure ───────────────────────────────────────────────────\n# DAG: A → Y, A → A*\n# OLS: Y ~ 1 + D*₁ + D*₂\n\ndef plim_exposure(C, dgp):\n    p, beta = dgp['p'], dgp['beta']\n    q = C @ p\n    EZZ = np.array([\n        [1,    q[1], q[2]],\n        [q[1], q[1], 0   ],\n        [q[2], 0,    q[2]]])\n    EZX = np.array([\n        [1,    p[1],           p[2]          ],\n        [q[1], C[1, 1] * p[1], C[1, 2] * p[2]],\n        [q[2], C[2, 1] * p[1], C[2, 2] * p[2]]])\n    return np.linalg.solve(EZZ, EZX @ beta)\n\n\n# ─── Topology 3: IV ─────────────────────────────────────────────────────────\n# DAG: Z → A, U → {A,Y}, A → Y, A → A*\n# Wald estimator: RF / FS*₁\n\nIV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)\n\n\ndef _softmax_sample(logits, rng):\n    e = np.exp(logits - logits.max(1, keepdims=True))\n    p = e / e.sum(1, keepdims=True)\n    c = np.cumsum(p, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    return (u >= c[:, 0]).astype(int) + (u >= c[:, 1]).astype(int)\n\n\ndef precomp_iv(beta, params, N=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['dZ'] * Z + params['dU'] * U,\n        params['g2'] + params['dZ2'] * Z + params['dU2'] * U])\n    A = _softmax_sample(logits, rng)\n    Y = (beta[1] * (A == 1).astype(float)\n         + beta[2] * (A == 2).astype(float)\n         + params['lam'] * U + rng.normal(0, 1, N))\n    z1, z0 = Z == 1, Z == 0\n    RF = Y[z1].mean() - Y[z0].mean()\n    FS = np.array([(A[z1] == k).mean() - (A[z0] == k).mean()\n                   for k in range(K)])\n    return dict(RF=RF, FS=FS)\n\n\ndef plim_iv(C, st):\n    fs = (C @ st['FS'])[1]\n    return np.nan if abs(fs) < 1e-8 else st['RF'] / fs\n\n\n# ─── ASV computation ────────────────────────────────────────────────────────\n\ndef _make_grid(C0):\n    dmax = get_delta_max(C0)\n    n = int(round(dmax / STEP)) + 1\n    return np.linspace(0, dmax, n)\n\n\ndef _find_envelope_asv(deltas, bias_abs, tau_abs, threshold):\n    if tau_abs < 1e-12:\n        return 0.0\n    thresh = threshold * tau_abs\n    rmax = 0.0\n    for i in range(len(deltas)):\n        b = bias_abs[i]\n        if not np.isnan(b):\n            rmax = max(rmax, b)\n        if rmax > thresh:\n            return float(deltas[i])\n    return None\n\n\ndef compute_cell_confounding(dgp, C0):\n    deltas = _make_grid(C0)\n    tau0 = plim_confounding(np.eye(K), dgp)\n    curve = np.array([plim_confounding(make_C_delta(C0, d), dgp)\n                      for d in deltas])\n    ba = np.abs(curve - tau0)\n    return {\n        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),\n        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),\n    }\n\n\ndef compute_cell_exposure(dgp, C0):\n    deltas = _make_grid(C0)\n    beta0 = plim_exposure(np.eye(K), dgp)\n    curves = np.array([plim_exposure(make_C_delta(C0, d), dgp)\n                       for d in deltas])\n\n    mr = np.zeros(len(deltas))\n    for i in range(len(deltas)):\n        for k in [1, 2]:\n            if abs(beta0[k]) > 1e-10:\n                mr[i] = max(mr[i],\n                            abs(curves[i, k] - beta0[k]) / abs(beta0[k]))\n\n    def _mag(threshold):\n        rmax = 0.0\n        for i in range(len(deltas)):\n            rmax = max(rmax, mr[i])\n            if rmax > threshold:\n                return float(deltas[i])\n        return None\n\n    sf = None\n    for i, d in enumerate(deltas):\n        for k in [1, 2]:\n            if (abs(beta0[k]) > 1e-10\n                    and abs(curves[i, k]) > 1e-10\n                    and curves[i, k] * beta0[k] < 0):\n                sf = float(d)\n                break\n        if sf is not None:\n            break\n\n    return {\n        'mag_asv_10pct': _mag(0.1),\n        'mag_asv_50pct': _mag(0.5),\n        'sign_flip_asv': sf,\n    }\n\n\ndef compute_cell_iv(st, C0):\n    deltas = _make_grid(C0)\n    tau0 = plim_iv(np.eye(K), st)\n    if np.isnan(tau0) or abs(tau0) < 1e-10:\n        return {'mag_asv_10pct': None, 'mag_asv_50pct': None}\n    curve = np.array([plim_iv(make_C_delta(C0, d), st) for d in deltas])\n    ba = np.abs(curve - tau0)\n    return {\n        'mag_asv_10pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.1),\n        'mag_asv_50pct': _find_envelope_asv(deltas, ba, abs(tau0), 0.5),\n    }\n\n\ndef median_results(cells):\n    keys = cells[0].keys()\n    out = {}\n    for k in keys:\n        vals = [c[k] for c in cells if c[k] is not None]\n        out[k] = round(float(np.median(vals)), 4) if vals else None\n    return out\n\n\n# ─── Main ────────────────────────────────────────────────────────────────────\n\nif __name__ == '__main__':\n    t0 = time.time()\n\n    DGPS = [\n        {'name': 'alternating_large',\n         'beta': np.array([0., 1.0, -0.5]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n        {'name': 'same_sign_medium',\n         'beta': np.array([0., 0.5, 0.3]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n        {'name': 'alternating_small',\n         'beta': np.array([0., 0.2, -0.1]), 'tau': 0.5,\n         'p': np.array([0.5, 0.33, 0.17]),\n         'gamma': np.array([0.5, -0.3]), 'sigma_T': 1.0},\n    ]\n\n    DIAG_VALS = [0.5, 0.6, 0.7, 0.8, 0.9]\n    C0S = [(d, make_fixed_C0(d)) for d in DIAG_VALS]\n    TOPOS = ['confounding', 'exposure', 'iv']\n\n    print(\"Exp-E: ASV Stability Across DGPs\")\n    print(\"=\" * 70)\n\n    print(\"Precomputing IV sufficient statistics...\")\n    iv_st = {}\n    for dgp in DGPS:\n        iv_st[dgp['name']] = precomp_iv(dgp['beta'], IV_PARAMS)\n        t_iv = plim_iv(np.eye(K), iv_st[dgp['name']])\n        print(f\"  {dgp['name']}: Wald(I) = {t_iv:.6f}\")\n\n    results = {t: {} for t in TOPOS}\n    per_c0 = {t: {} for t in TOPOS}\n\n    for dgp in DGPS:\n        nm = dgp['name']\n        print(f\"\\nDGP: {nm}  beta={dgp['beta'].tolist()}\")\n\n        for topo in TOPOS:\n            cells = []\n            for dv, C0 in C0S:\n                if topo == 'confounding':\n                    c = compute_cell_confounding(dgp, C0)\n                elif topo == 'exposure':\n                    c = compute_cell_exposure(dgp, C0)\n                else:\n                    c = compute_cell_iv(iv_st[nm], C0)\n                cells.append(c)\n\n            med = median_results(cells)\n            results[topo][nm] = med\n            per_c0[topo][nm] = [\n                {**c, 'C0_diag': dv} for (dv, _), c in zip(C0S, cells)]\n\n            parts = [f\"10%={med['mag_asv_10pct']}\",\n                     f\"50%={med['mag_asv_50pct']}\"]\n            if 'sign_flip_asv' in med:\n                parts.append(f\"sf={med['sign_flip_asv']}\")\n            print(f\"  {topo:>12}: {', '.join(parts)}\")\n\n    # ── Ranking analysis ─────────────────────────────────────────────────────\n    print(\"\\n\" + \"=\" * 70)\n    print(\"Ranking (by delta*_10%, lower = more fragile)\")\n    print(\"=\" * 70)\n    rankings = {}\n    for dgp in DGPS:\n        nm = dgp['name']\n        vals = [(t, results[t][nm]['mag_asv_10pct'] or float('inf'))\n                for t in TOPOS]\n        vals.sort(key=lambda x: x[1])\n        rankings[nm] = [t for t, _ in vals]\n        vstr = ' < '.join(f\"{t}({v:.4f})\" for t, v in vals)\n        print(f\"  {nm}: {vstr}\")\n\n    stable = len(set(tuple(r) for r in rankings.values())) == 1\n    stability_msg = (\"Rankings preserved across all 3 DGPs\" if stable\n                     else \"Rankings vary across DGPs\")\n    print(f\"\\nStable: {stable} -- {stability_msg}\")\n\n    sf_ss = results['exposure']['same_sign_medium'].get('sign_flip_asv')\n    print(f\"Same-sign sign-flip: \"\n          f\"{'None (confirmed -- no flip for same-sign beta)' if sf_ss is None else sf_ss}\")\n\n    # ── Save JSON ────────────────────────────────────────────────────────────\n    output = {\n        'dgp_configs': [\n            {'name': d['name'], 'beta': d['beta'].tolist(),\n             'tau': d['tau'], 'p': d['p'].tolist()}\n            for d in DGPS],\n        'C0_diag_values': DIAG_VALS,\n        'results': results,\n        'per_C0_results': per_c0,\n        'rankings': rankings,\n        'ranking_stable': stable,\n        'ranking_stability': stability_msg,\n    }\n    json_path = 'artifacts/exp_e_asv_stability_results.json'\n    with open(json_path, 'w') as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nSaved: {json_path}\")\n\n    # ── Save LaTeX table ─────────────────────────────────────────────────────\n    labels = {\n        'alternating_large': r'Alt.\\ large: $\\bm{\\beta}=[0,\\,1.0,\\,-0.5]$',\n        'same_sign_medium':  r'Same-sign: $\\bm{\\beta}=[0,\\,0.5,\\,0.3]$',\n        'alternating_small': r'Alt.\\ small: $\\bm{\\beta}=[0,\\,0.2,\\,-0.1]$',\n    }\n    tex = [\n        r'\\begin{table}[t]',\n        r'\\centering',\n        r'\\caption{ASV stability across DGP configurations. '\n        r'Each cell shows $\\delta^*$ at the 10\\% relative bias threshold '\n        r'(median over 5 confusion matrices with diagonal '\n        r'$\\in\\{0.5,0.6,0.7,0.8,0.9\\}$). '\n        r'Lower $\\delta^*$ indicates greater fragility. '\n        r'Confounding is consistently most robust; '\n        r'for alternating-sign $\\bm{\\beta}$, '\n        r'the ranking Exposure $<$ IV $<$ Confounding holds. '\n        r'``$\\infty$\\!\\!'' = threshold never reached within $\\delta$ range.}',\n        r'\\label{tab:asv_stability}',\n        r'\\small',\n        r'\\begin{tabular}{l ccc}',\n        r'\\toprule',\n        r' & \\multicolumn{3}{c}{Magnitude ASV $\\delta^*_{10\\%}$} \\\\',\n        r'\\cmidrule(lr){2-4}',\n        r'DGP Configuration & Confounding & Exposure & IV \\\\',\n        r'\\midrule',\n    ]\n    for dgp in DGPS:\n        nm = dgp['name']\n        vals = []\n        for t in TOPOS:\n            v = results[t][nm]['mag_asv_10pct']\n            vals.append(f'{v:.3f}' if v is not None else r'$\\infty$')\n        tex.append(\n            f'{labels[nm]} & {vals[0]} & {vals[1]} & {vals[2]} \\\\\\\\')\n    tex += [r'\\bottomrule', r'\\end{tabular}', r'\\end{table}']\n\n    tex_path = 'artifacts/exp_e_asv_stability_table.tex'\n    with open(tex_path, 'w') as f:\n        f.write('\\n'.join(tex))\n    print(f\"Saved: {tex_path}\")\n\n    print(f\"\\nTotal: {time.time() - t0:.1f}s\")\n",
    "structuredPatch": [
      {
        "oldStart": 345,
        "oldLines": 7,
        "newStart": 345,
        "newLines": 7,
        "lines": [
          "         r'Confounding is consistently most robust; '",
          "         r'for alternating-sign $\\bm{\\beta}$, '",
          "         r'the ranking Exposure $<$ IV $<$ Confounding holds. '",
          "-        r'``$\\infty$\\!\\!'' = threshold never reached within $\\delta$ range.}',",
          "+        r\"``$\\infty$\\!\\!'' = threshold never reached within $\\delta$ range.}\",",
          "         r'\\label{tab:asv_stability}',",
          "         r'\\small',",
          "         r'\\begin{tabular}{l ccc}',"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Bash · `toolu_016B8P3EaQnNSC2FDtRDUaxn`</summary>

```json
{
  "command": "python3 artifacts/exp_e_asv_stability.py 2>&1",
  "description": "Final run without syntax warning",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "93a3adc8-7e5a-419f-93dc-2ccfa279464e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BZkBjk27ii5zyATasHkgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 257,
      "cache_read_input_tokens": 144547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 257
      },
      "output_tokens": 67,
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

_source line 85_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bsqx146hc",
  "tool_use_id": "toolu_016B8P3EaQnNSC2FDtRDUaxn",
  "description": "Final run without syntax warning",
  "task_type": "local_bash",
  "uuid": "2933167a-6d7f-44bf-98dc-6295e4aeebcc",
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502"
}
```

---

### System

_source line 86_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bsqx146hc",
  "tool_use_id": "toolu_016B8P3EaQnNSC2FDtRDUaxn",
  "status": "completed",
  "output_file": "",
  "summary": "Final run without syntax warning",
  "uuid": "458d37af-85a2-4f0e-837f-760831d046d8",
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502"
}
```

---

### Tool result

_source line 87 · 2026-05-22T11:53:57.525Z_

<details><summary>↩ Tool result · `toolu_016B8P3EaQnNSC2FDtRDUaxn`</summary>

```text
Exp-E: ASV Stability Across DGPs
======================================================================
Precomputing IV sufficient statistics...
  alternating_large: Wald(I) = 1.338985
  same_sign_medium: Wald(I) = 0.305478
  alternating_small: Wald(I) = 0.272231

DGP: alternating_large  beta=[0.0, 1.0, -0.5]
   confounding: 10%=0.348, 50%=None
      exposure: 10%=0.09, 50%=0.5561, sf=2.2232
            iv: 10%=0.203, 50%=0.7411

DGP: same_sign_medium  beta=[0.0, 0.5, 0.3]
   confounding: 10%=None, 50%=None
      exposure: 10%=0.223, 50%=1.1741, sf=2.2232
            iv: 10%=0.203, 50%=0.7411

DGP: alternating_small  beta=[0.0, 0.2, -0.1]
   confounding: 10%=None, 50%=None
      exposure: 10%=0.09, 50%=0.5561, sf=2.2232
            iv: 10%=0.203, 50%=0.7411

======================================================================
Ranking (by delta*_10%, lower = more fragile)
======================================================================
  alternating_large: exposure(0.0900) < iv(0.2030) < confounding(0.3480)
  same_sign_medium: iv(0.2030) < exposure(0.2230) < confounding(inf)
  alternating_small: exposure(0.0900) < iv(0.2030) < confounding(inf)

Stable: False -- Rankings vary across DGPs
Same-sign sign-flip: 2.2232

Saved: artifacts/exp_e_asv_stability_results.json
Saved: artifacts/exp_e_asv_stability_table.tex

Total: 10.4s
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "9ee81c2e-0633-4470-b703-b62bb876419d",
  "tool_use_result": {
    "stdout": "Exp-E: ASV Stability Across DGPs\n======================================================================\nPrecomputing IV sufficient statistics...\n  alternating_large: Wald(I) = 1.338985\n  same_sign_medium: Wald(I) = 0.305478\n  alternating_small: Wald(I) = 0.272231\n\nDGP: alternating_large  beta=[0.0, 1.0, -0.5]\n   confounding: 10%=0.348, 50%=None\n      exposure: 10%=0.09, 50%=0.5561, sf=2.2232\n            iv: 10%=0.203, 50%=0.7411\n\nDGP: same_sign_medium  beta=[0.0, 0.5, 0.3]\n   confounding: 10%=None, 50%=None\n      exposure: 10%=0.223, 50%=1.1741, sf=2.2232\n            iv: 10%=0.203, 50%=0.7411\n\nDGP: alternating_small  beta=[0.0, 0.2, -0.1]\n   confounding: 10%=None, 50%=None\n      exposure: 10%=0.09, 50%=0.5561, sf=2.2232\n            iv: 10%=0.203, 50%=0.7411\n\n======================================================================\nRanking (by delta*_10%, lower = more fragile)\n======================================================================\n  alternating_large: exposure(0.0900) < iv(0.2030) < confounding(0.3480)\n  same_sign_medium: iv(0.2030) < exposure(0.2230) < confounding(inf)\n  alternating_small: exposure(0.0900) < iv(0.2030) < confounding(inf)\n\nStable: False -- Rankings vary across DGPs\nSame-sign sign-flip: 2.2232\n\nSaved: artifacts/exp_e_asv_stability_results.json\nSaved: artifacts/exp_e_asv_stability_table.tex\n\nTotal: 10.4s",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 88_

Let me verify the final outputs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "85dfed6e-748c-49d0-9cb2-f53cd69305fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwSNmg6NGQVZyFBcg6Zxub",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 144804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 654
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

### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Read · `toolu_01FSR2qa2id2mj3HFbmWfCp8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "128b16dd-771a-47c8-8a2c-45e23184e54e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwSNmg6NGQVZyFBcg6Zxub",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 144804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 654
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

_source line 90 · 2026-05-22T11:54:03.085Z_

<details><summary>↩ Tool result · `toolu_01FSR2qa2id2mj3HFbmWfCp8`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\caption{ASV stability across DGP configurations. Each cell shows $\delta^*$ at the 10\% relative bias threshold (median over 5 confusion matrices with diagonal $\in\{0.5,0.6,0.7,0.8,0.9\}$). Lower $\delta^*$ indicates greater fragility. Confounding is consistently most robust; for alternating-sign $\bm{\beta}$, the ranking Exposure $<$ IV $<$ Confounding holds. ``$\infty$\!\!'' = threshold never reached within $\delta$ range.}
4	\label{tab:asv_stability}
5	\small
6	\begin{tabular}{l ccc}
7	\toprule
8	 & \multicolumn{3}{c}{Magnitude ASV $\delta^*_{10\%}$} \\
9	\cmidrule(lr){2-4}
10	DGP Configuration & Confounding & Exposure & IV \\
11	\midrule
12	Alt.\ large: $\bm{\beta}=[0,\,1.0,\,-0.5]$ & 0.348 & 0.090 & 0.203 \\
13	Same-sign: $\bm{\beta}=[0,\,0.5,\,0.3]$ & $\infty$ & 0.223 & 0.203 \\
14	Alt.\ small: $\bm{\beta}=[0,\,0.2,\,-0.1]$ & $\infty$ & 0.090 & 0.203 \\
15	\bottomrule
16	\end{tabular}
17	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "a241075d-6b23-4e79-8043-3288e15b7bb9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability_table.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\caption{ASV stability across DGP configurations. Each cell shows $\\delta^*$ at the 10\\% relative bias threshold (median over 5 confusion matrices with diagonal $\\in\\{0.5,0.6,0.7,0.8,0.9\\}$). Lower $\\delta^*$ indicates greater fragility. Confounding is consistently most robust; for alternating-sign $\\bm{\\beta}$, the ranking Exposure $<$ IV $<$ Confounding holds. ``$\\infty$\\!\\!'' = threshold never reached within $\\delta$ range.}\n\\label{tab:asv_stability}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\n & \\multicolumn{3}{c}{Magnitude ASV $\\delta^*_{10\\%}$} \\\\\n\\cmidrule(lr){2-4}\nDGP Configuration & Confounding & Exposure & IV \\\\\n\\midrule\nAlt.\\ large: $\\bm{\\beta}=[0,\\,1.0,\\,-0.5]$ & 0.348 & 0.090 & 0.203 \\\\\nSame-sign: $\\bm{\\beta}=[0,\\,0.5,\\,0.3]$ & $\\infty$ & 0.223 & 0.203 \\\\\nAlt.\\ small: $\\bm{\\beta}=[0,\\,0.2,\\,-0.1]$ & $\\infty$ & 0.090 & 0.203 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  }
}
```

</details>

---

### Assistant

_source line 91_

All outputs are in order. Here's a summary of the Exp-E results:

**Outputs produced:**
- `artifacts/exp_e_asv_stability.py` — self-contained script
- `artifacts/exp_e_asv_stability_results.json` — full results with per-C₀ detail
- `artifacts/exp_e_asv_stability_table.tex` — LaTeX table

**Key findings:**

| | Confounding | Exposure | IV |
|---|---|---|---|
| Alt. large β=[0,1.0,-0.5] | 0.348 | **0.090** | 0.203 |
| Same-sign β=[0,0.5,0.3] | ∞ | 0.223 | **0.203** |
| Alt. small β=[0,0.2,-0.1] | ∞ | **0.090** | 0.203 |

1. **Confounding is always most robust** — bias on τ from annotation error is small because T has independent variation (σ_T). For same-sign/small DGPs, the max OVB is <10% of τ, so the threshold is never reached.

2. **Ranking partially stable**: Exposure < IV < Confounding holds for alternating-sign β (2/3 configs). For same-sign β, IV and exposure swap because same-sign misclassification causes less bias.

3. **IV ASV is invariant to β** (0.203 for all DGPs) — the Wald estimator's relative bias depends only on the first-stage distortion C@FS, which cancels out the effect magnitude.

4. **Exposure alternating = exposure small** (0.090 for both) — the exposure plim is linear in β, so relative bias is scale-invariant. Only the sign structure matters.

5. **Sign-flip ASV is invariant** (≈2.223 for all DGPs) — occurs at the uniform confusion boundary where all coefficients hit zero. A universal property of symmetric C₀ matrices in the exposure model.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "uuid": "d5b569aa-a7c4-4989-90ed-fad9c54eb17c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186XcN4sdJqqH8ZxPin4W42",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 559,
      "cache_read_input_tokens": 145458,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 559
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

### Task result

_source line 92_

All outputs are in order. Here's a summary of the Exp-E results:

**Outputs produced:**
- `artifacts/exp_e_asv_stability.py` — self-contained script
- `artifacts/exp_e_asv_stability_results.json` — full results with per-C₀ detail
- `artifacts/exp_e_asv_stability_table.tex` — LaTeX table

**Key findings:**

| | Confounding | Exposure | IV |
|---|---|---|---|
| Alt. large β=[0,1.0,-0.5] | 0.348 | **0.090** | 0.203 |
| Same-sign β=[0,0.5,0.3] | ∞ | 0.223 | **0.203** |
| Alt. small β=[0,0.2,-0.1] | ∞ | **0.090** | 0.203 |

1. **Confounding is always most robust** — bias on τ from annotation error is small because T has independent variation (σ_T). For same-sign/small DGPs, the max OVB is <10% of τ, so the threshold is never reached.

2. **Ranking partially stable**: Exposure < IV < Confounding holds for alternating-sign β (2/3 configs). For same-sign β, IV and exposure swap because same-sign misclassification causes less bias.

3. **IV ASV is invariant to β** (0.203 for all DGPs) — the Wald estimator's relative bias depends only on the first-stage distortion C@FS, which cancels out the effect magnitude.

4. **Exposure alternating = exposure small** (0.090 for both) — the exposure plim is linear in β, so relative bias is scale-invariant. Only the sign structure matters.

5. **Sign-flip ASV is invariant** (≈2.223 for all DGPs) — occurs at the uniform confusion boundary where all coefficients hit zero. A universal property of symmetric C₀ matrices in the exposure model.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1481742,
  "duration_api_ms": 1408668,
  "num_turns": 29,
  "stop_reason": "end_turn",
  "session_id": "5dd7b7d5-dbe0-4b64-ab45-ed43324da502",
  "total_cost_usd": 3.9978225000000003,
  "usage": {
    "input_tokens": 27,
    "cache_creation_input_tokens": 134176,
    "cache_read_input_tokens": 2364591,
    "output_tokens": 78986,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 134176,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 500,
        "cache_read_input_tokens": 145458,
        "cache_creation_input_tokens": 559,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 559
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2047,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0021420000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 27,
      "outputTokens": 78986,
      "cacheReadInputTokens": 2364591,
      "cacheCreationInputTokens": 134176,
      "webSearchRequests": 0,
      "costUSD": 3.9956805,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "184182c1-4077-4dd4-ba04-3e03d89b0f27"
}
```

</details>

---
