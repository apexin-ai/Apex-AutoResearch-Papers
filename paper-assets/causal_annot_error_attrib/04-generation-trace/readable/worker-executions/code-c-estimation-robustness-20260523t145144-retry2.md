# code c estimation robustness 20260523T145144 retry2

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 93
- **Recorded user turns:** 1
- **Tool calls:** 28
- **Original source:** `logs/workers/worker_code_c_estimation_robustness_20260523T145144_retry2.log`
- **Structured JSON:** [`7c17de2623e25f1cd758.json`](../../sessions/7c/7c17de2623e25f1cd758.json)

## Before a recorded user message

5 recorded events

### System

_source line 1_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
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
  "uuid": "3b88d7c0-b5fe-4892-9350-a6affcec9e80",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 2_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779550800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9e4df03e-5257-4da7-b204-edf51398da6e",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Assistant

_source line 3_

I'll start by examining the reference code and data files to understand the existing implementation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "c269e15f-20b7-486a-8eb0-3f48db944dc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWJqhPME28eXs9BLbwGDes",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13253,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13253
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

### Tool call

_source line 4_

<details open><summary>🔧 Tool call — Agent · `toolu_019RAmNXzxRkNsP6Bq4t2qER`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find ASV and bias code",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/, I need to understand:\n\n1. How ASV (magnitude) is computed in `ranking_stability.py` — find the function `compute_asv_magnitude` or similar, and show the full implementation.\n2. How bias plim is computed for the 7 topologies (confounding, mediation, collider, frontdoor, mbias, exposure, IV). Search for bias computation functions across all .py files in artifacts/.\n3. Check if `dream_reports/empirical_confusion_matrices.json` exists, and if not, find any JSON file containing empirical confusion matrices.\n4. Look at any existing `c_estimation_robustness.py` to understand what's already been done.\n\nSearch breadth: very thorough. Show full function bodies for the key functions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "5c2e3b24-b30d-47af-b86b-555ea7c47573",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWJqhPME28eXs9BLbwGDes",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13253,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13253
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

### System

_source line 5_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Find ASV and bias code",
  "task_type": "local_agent",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/, I need to understand:\n\n1. How ASV (magnitude) is computed in `ranking_stability.py` — find the function `compute_asv_magnitude` or similar, and show the full implementation.\n2. How bias plim is computed for the 7 topologies (confounding, mediation, collider, frontdoor, mbias, exposure, IV). Search for bias computation functions across all .py files in artifacts/.\n3. Check if `dream_reports/empirical_confusion_matrices.json` exists, and if not, find any JSON file containing empirical confusion matrices.\n4. Look at any existing `c_estimation_robustness.py` to understand what's already been done.\n\nSearch breadth: very thorough. Show full function bodies for the key functions.",
  "uuid": "0da39d0d-c4d3-42e7-b5c0-a82769442828",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

## Round 1

88 recorded events

### User

_source line 6 · 2026-05-23T14:55:55.544Z_

In the directory /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/, I need to understand:

1. How ASV (magnitude) is computed in `ranking_stability.py` — find the function `compute_asv_magnitude` or similar, and show the full implementation.
2. How bias plim is computed for the 7 topologies (confounding, mediation, collider, frontdoor, mbias, exposure, IV). Search for bias computation functions across all .py files in artifacts/.
3. Check if `dream_reports/empirical_confusion_matrices.json` exists, and if not, find any JSON file containing empirical confusion matrices.
4. Look at any existing `c_estimation_robustness.py` to understand what's already been done.

Search breadth: very thorough. Show full function bodies for the key functions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "c17e9fde-91b2-4c35-927a-33839448a1f5"
}
```

</details>

---

### System

_source line 7_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Running find /home/ubuntu/.agent-ml-research-prod_0510/pr…",
  "usage": {
    "total_tokens": 17973,
    "tool_uses": 1,
    "duration_ms": 1896
  },
  "last_tool_name": "Bash",
  "uuid": "e1a59562-4953-4152-9cec-eb253cb8c22d",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Bash · `toolu_01RqzbDdfaFb4FgCbbzeky1k`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts -type f -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "e2419321-7d75-40e5-9403-7fb25a0c7cda",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EuXs5ukd8xN4oHgBDbtp7X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17964,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17964,
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

_source line 9 · 2026-05-23T14:55:57.736Z_

<details><summary>↩ Tool result · `toolu_01RqzbDdfaFb4FgCbbzeky1k`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/intermediate/verify_lambda_bound.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/intermediate/case_study_analysis.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/mvp_exposure_dag.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/exp_fwl_logistic_breakdown.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/mvp_confounding_dag.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/report/mvp_exposure_dirichlet_subspace.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ppi_gold_ratio_sensitivity.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/analyze_epsilon_bound.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_realistic_epsilon.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_primary_coeff_breakdown.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_annotations/scripts/annotate_frontier.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_annotations/scripts/prepare_data.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_annotations/scripts/compute_results.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/verify_lambda_bound.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan012_case_study/case_study_analysis.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_all_tasks.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/nondiff_stress_test.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_epsilon_tau_sensitivity.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/analyze_epsilon_sign_structure.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/nondiff_topic_stratified.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "e5fa3e1d-7108-4645-84d2-57ec68dd1b3c"
}
```

</details>

---

### System

_source line 10_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Finding /home/ubuntu/.agent-ml-research-prod_0510/project…",
  "usage": {
    "total_tokens": 19817,
    "tool_uses": 2,
    "duration_ms": 3559
  },
  "last_tool_name": "Glob",
  "uuid": "30ef5be0-536b-4876-bc17-4f7a78c45e9d",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_017t3Lfy1wFZMqi6dy228CEY`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/*ranking*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "bd32d356-d232-4ae8-af1a-db58f80e23da",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Gx7jEt9yox9PshFNQJBJoM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1840,
      "cache_read_input_tokens": 17964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1840,
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

_source line 12 · 2026-05-23T14:55:59.133Z_

<details><summary>↩ Tool result · `toolu_017t3Lfy1wFZMqi6dy228CEY`</summary>

```text
artifacts/_project/chart/fig3_asv_ranking.pdf
artifacts/_project/chart/fig3_asv_ranking_d3fbb2.pdf
artifacts/_project/chart/fig3_asv_ranking_8051a6.pdf
artifacts/ranking_stability.py
artifacts/__pycache__/ranking_stability.cpython-314.pyc
artifacts/ranking_stability_results.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "3dbad8de-103d-430a-9b55-9580d4bfd6fd"
}
```

</details>

---

### System

_source line 13_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Running find /home/ubuntu/.agent-ml-research-prod_0510/pr…",
  "usage": {
    "total_tokens": 20023,
    "tool_uses": 3,
    "duration_ms": 5271
  },
  "last_tool_name": "Bash",
  "uuid": "60ff10f0-718d-407b-acbf-a3e45d2c53c8",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_014ZUFi2kYZUNmS1YsEJMg5E`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts -type f -name \"*empirical_confusion*\" -o -name \"*c_estimation_robustness*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "d56d2333-1b27-4daa-b06b-75ed82aa60c1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BR7uLGq3HPYUWfC1Kr1mGC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 19804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 204,
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

_source line 15 · 2026-05-23T14:56:00.880Z_

<details><summary>↩ Tool result · `toolu_014ZUFi2kYZUNmS1YsEJMg5E`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "c85503be-7524-4d17-9376-324676df10c6"
}
```

</details>

---

### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Running find /home/ubuntu/.agent-ml-research-prod_0510/pr…",
  "usage": {
    "total_tokens": 20254,
    "tool_uses": 4,
    "duration_ms": 7207
  },
  "last_tool_name": "Bash",
  "uuid": "2095ea5a-7617-4f91-ba8c-70652b09b34b",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_01UDdbkN2TxBqTpohxLTa4pq`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts -type d -name \"dream_reports\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "6615160f-66dd-4982-9bef-4af8b7a9c8c3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EhJDF8Xu9prWDwzyPajHFm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 223,
      "cache_read_input_tokens": 20008,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 223,
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

_source line 18 · 2026-05-23T14:56:02.878Z_

<details><summary>↩ Tool result · `toolu_01UDdbkN2TxBqTpohxLTa4pq`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "e1f8cefc-765d-4d5b-8885-42f4083fbf9b"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-prod_0510/…",
  "usage": {
    "total_tokens": 20476,
    "tool_uses": 5,
    "duration_ms": 8867
  },
  "last_tool_name": "Bash",
  "uuid": "b011163e-1f10-428e-b853-f8afb94b88df",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_01Qw136goULubu72oNhX7adv`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/ | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "77312d6a-a3ad-481d-a2ba-a050fb9952d7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C6ZKaLuzXsWnxffoH5wFCL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 155,
      "cache_read_input_tokens": 20231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 155,
        "ephemeral_1h_input_tokens": 0
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

### Tool result

_source line 21 · 2026-05-23T14:56:04.496Z_

<details><summary>↩ Tool result · `toolu_01Qw136goULubu72oNhX7adv`</summary>

```text
total 64
drwxr-xr-x 13 ubuntu ubuntu  4096 May 21 08:32 .
drwxr-xr-x 37 ubuntu ubuntu 12288 May 23 14:55 ..
drwxr-xr-x  3 ubuntu ubuntu  4096 May 20 07:29 dream_20260520T072911
drwxr-xr-x  6 ubuntu ubuntu  4096 May 20 09:03 dream_20260520T074549
drwxr-xr-x  3 ubuntu ubuntu  4096 May 21 05:22 dream_20260521T052211
drwxr-xr-x  3 ubuntu ubuntu  4096 May 21 05:23 dream_20260521T052307
drwxr-xr-x  3 ubuntu ubuntu  4096 May 21 05:25 dream_20260521T052449
drwxr-xr-x  3 ubuntu ubuntu  4096 May 21 05:25 dream_20260521T052547
drwxr-xr-x  3 ubuntu ubuntu  4096 May 21 05:28 dream_20260521T052836
drwxr-xr-x  3 ubuntu ubuntu  4096 May 21 05:42 dream_20260521T054240
drwxr-xr-x  3 ubuntu ubuntu  4096 May 21 05:44 dream_20260521T054441
drwxr-xr-x  4 ubuntu ubuntu  4096 May 21 05:55 dream_20260521T054528
drwxr-xr-x  3 ubuntu ubuntu  4096 May 21 08:32 dream_20260521T083151
lrwxrwxrwx  1 ubuntu ubuntu   122 May 21 08:32 latest -> /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260521T083151
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "53a8ea0b-42f5-4488-ac4b-41b7302446e9"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Running find /home/ubuntu/.agent-ml-research-prod_0510/pr…",
  "usage": {
    "total_tokens": 21162,
    "tool_uses": 6,
    "duration_ms": 10451
  },
  "last_tool_name": "Bash",
  "uuid": "963766d3-00d9-41c6-bf36-5b6f6610da7a",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_014aJzDitN8vT11a3cmNxkaD`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports -name \"*empirical_confusion*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "8d1a91d7-d948-4696-b6d7-32504411f01f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AxEpAnfdukndgDT6M32Jmu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 621,
      "cache_read_input_tokens": 20386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 621,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
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

_source line 24 · 2026-05-23T14:56:06.146Z_

<details><summary>↩ Tool result · `toolu_014aJzDitN8vT11a3cmNxkaD`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "3f859a85-06fc-4a2e-9e45-95e6f490db1e"
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Running find /home/ubuntu/.agent-ml-research-prod_0510/pr…",
  "usage": {
    "total_tokens": 21445,
    "tool_uses": 7,
    "duration_ms": 11907
  },
  "last_tool_name": "Bash",
  "uuid": "e4a4be17-2c0d-4559-804e-3611d66263c0",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_01RakdzvhbvxnzuswY7H7SLX`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts -name \"*.json\" | grep -i \"confus\\|matrix\\|empirical\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "8aed7e7a-19a5-407f-8c2e-d32caf98ae2c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Td9ZXakJfH28fW4YQ9dQ6p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 221,
      "cache_read_input_tokens": 21007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 221,
        "ephemeral_1h_input_tokens": 0
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

_source line 27 · 2026-05-23T14:56:07.547Z_

<details><summary>↩ Tool result · `toolu_01RakdzvhbvxnzuswY7H7SLX`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/ppi_empirical_validation.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/updated_empirical_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan006/asv_empirical_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ppi_empirical_validation.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan006_asv_empirical/data/plan006_full_filtered_stats.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan006_mock/asv_empirical_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/theory_empirical_mape.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "006b4485-83c5-450e-923c-178eb93446ae"
}
```

</details>

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Searching for def\\s+compute.*bias|def\\s+bias.*plim|confounding|…",
  "usage": {
    "total_tokens": 21918,
    "tool_uses": 8,
    "duration_ms": 14579
  },
  "last_tool_name": "Grep",
  "uuid": "c014707a-0913-4242-81dd-d0d475b2193b",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Grep · `toolu_01Tx73J63djdtwjmiiDXqZxw`</summary>

```json
{
  "pattern": "def\\s+compute.*bias|def\\s+bias.*plim|confounding|mediation|collider|frontdoor|mbias|exposure|IV",
  "type": "py",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts",
  "head_limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "43ffa906-e7a3-475f-b3fc-5801d1d1415e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012m63DCSyMnqBv8MsPCELS4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 471,
      "cache_read_input_tokens": 21228,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 471,
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

_source line 30 · 2026-05-23T14:56:10.179Z_

<details><summary>↩ Tool result · `toolu_01Tx73J63djdtwjmiiDXqZxw`</summary>

```text
Found 48 files
artifacts/c_estimation_robustness.py
artifacts/sign_reversal_determinants.py
artifacts/within_topo_f1_bias.py
artifacts/structured_nondiff_violation.py
artifacts/conjecture_dgp_sensitivity.py
artifacts/e2e_demo.py
artifacts/ranking_stability.py
artifacts/correction_k_sensitivity.py
artifacts/bootstrap_ci_convergence.py
artifacts/ppi_gold_ratio_sensitivity.py
artifacts/nondiff_structured_stress_test.py
artifacts/exp_proportional_real_matrices.py
artifacts/exp_realistic_epsilon.py
artifacts/exp_fwl_nonlinear_scaling.py
artifacts/exp_proportional_effects.py
artifacts/exp_primary_coeff_breakdown.py
artifacts/nondiff_stress_test.py
artifacts/compute_unified_mape.py
artifacts/_project/data/exp_fwl_logistic_breakdown.py
artifacts/exp_fwl_logistic_breakdown.py
artifacts/verify_lambda_bound.py
artifacts/exp_d_epsilon_tau_sensitivity.py
artifacts/_project/intermediate/verify_lambda_bound.py
artifacts/analyze_epsilon_sign_structure.py
artifacts/exp_b_logistic_dgp.py
artifacts/analyze_epsilon_bound.py
artifacts/exp_d_conjecture_verify_v2.py
artifacts/exp_e_asv_stability.py
artifacts/exp_d_conjecture_verify.py
artifacts/exp_c_bootstrap_asv.py
artifacts/exp_a_stress_test.py
artifacts/compute_updated_empirical.py
artifacts/compute_delta_max.py
artifacts/_project/intermediate/case_study_analysis.py
artifacts/plan012_case_study/case_study_analysis.py
artifacts/compute_ppi_empirical.py
artifacts/compute_all_tasks.py
artifacts/compute_theory_empirical_mape.py
artifacts/mvp_iv_dirichlet_subspace.py
artifacts/plan_009_pathological_matrices.py
artifacts/plan_002_k57_extended_7topo.py
artifacts/plan_005_asv_extended_fixed.py
artifacts/plan008_binarization_collapse/report/plan_008_binarization_collapse.py
artifacts/_project/report/mvp_exposure_dirichlet_subspace.py
artifacts/mvp_exposure_dirichlet_subspace.py
artifacts/_project/data/mvp_exposure_dag.py
artifacts/mvp_exposure_dag.py
artifacts/mvp_confounding_dag.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "27652693-97f9-4fe6-9bd7-aca1fd828322"
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Reading artifacts/ranking_stability.py",
  "usage": {
    "total_tokens": 22757,
    "tool_uses": 9,
    "duration_ms": 16277
  },
  "last_tool_name": "Read",
  "uuid": "96f85145-f836-4d2a-ad4a-23f09947e4d0",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01WQmFioarTtLg8MAfoPkto6`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "fc3ffa4b-dd25-455e-b137-54163d035326",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UC6g7KCgz3QF8v5UGaCD2z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 837,
      "cache_read_input_tokens": 21699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 837,
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

_source line 33 · 2026-05-23T14:56:12.112Z_

<details><summary>↩ Tool result · `toolu_01WQmFioarTtLg8MAfoPkto6`</summary>

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
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "a4f6af77-268f-4fba-9bae-4e646cee808c"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Reading artifacts/c_estimation_robustness.py",
  "usage": {
    "total_tokens": 37274,
    "tool_uses": 10,
    "duration_ms": 18647
  },
  "last_tool_name": "Read",
  "uuid": "5b50a590-2df2-4bab-ba8c-e5675f7c3ec4",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01G9tfruBo1hUue25cyBrGek`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "c8237e44-cc46-41c3-b9f7-a4dae32b1365",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013sNaEdNg8eCyAeK1foW8AR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 14509,
      "cache_read_input_tokens": 22536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14509,
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

_source line 36 · 2026-05-23T14:56:14.200Z_

<details><summary>↩ Tool result · `toolu_01G9tfruBo1hUue25cyBrGek`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Ĉ Estimation Robustness Experiment.
4	
5	Question: With a finite K-class gold-labelled set used to estimate C, does
6	the safe/fragile topology partition (5 vs 2) hold under multinomial bootstrap
7	of Ĉ?
8	
9	For each empirical column-stochastic K=3 confusion matrix C (LLM truth),
10	draw B bootstrap replicates Ĉ ~ multinomial(C[:,k] · n_gold) / n_gold for
11	each class k. For each Ĉ, recompute the magnitude ASV δ* for the 7
12	topologies (confounding, mediation, collider, exposure, mbias, IV,
13	frontdoor) and report:
14	
15	  • Partition stability rate vs n_gold: fraction of bootstraps where the
16	    two lowest-ASV topologies equal {exposure, IV}.
17	  • Spearman ρ vs n_gold: rank correlation between ASV ranking from Ĉ and
18	    from true C (averaged over bootstraps and source matrices).
19	
20	Empirical Cs come from artifacts/updated_empirical_results.json (23 LLM
21	matrices; 8 are K=3 vast/stance — the K=3 framework subset).
22	
23	Output: c_estimation_robustness_results.json next to this script.
24	"""
25	
26	import json
27	import os
28	import sys
29	import time
30	from collections import defaultdict
31	
32	import numpy as np
33	from scipy.stats import rankdata, spearmanr
34	
35	sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
36	
37	from ranking_stability import (  # noqa: E402
38	    ALL_TOPOS, COMPUTE_SS, DGP_PARAMS, K, N_DELTA, DELTAS, ASV_EPSILON,
39	    PROTECTIVE, get_tau_true, process_batch_iv, process_batch_exposure,
40	    process_batch_with_T,
41	)
42	
43	# ──────────────────────────────────────────────────────────────────────────
44	EMP_PATH = '/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json'
45	OUT_DIR = os.path.dirname(os.path.abspath(__file__))
46	OUT_PATH = os.path.join(OUT_DIR, 'c_estimation_robustness_results.json')
47	
48	N_GOLD_GRID = [50, 100, 200, 500]
49	B_BOOT = 200
50	SEED = 20260523
51	SAFE = {'confounding', 'mediation', 'collider', 'frontdoor', 'mbias'}
52	FRAGILE = {'exposure', 'iv'}
53	RANK_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
54	              'mbias', 'iv', 'frontdoor']
55	TOPO_IDX = {t: i for i, t in enumerate(RANK_TOPOS)}
56	
57	
58	def load_k3_matrices():
59	    with open(EMP_PATH) as f:
60	        d = json.load(f)
61	    out = {}
62	    for name, cm in d['confusion_matrices'].items():
63	        arr = np.asarray(cm, dtype=float)
64	        if arr.shape == (K, K):
65	            # Re-normalise columns just in case
66	            cs = arr.sum(axis=0, keepdims=True)
67	            cs = np.where(cs < 1e-12, 1.0, cs)
68	            out[name] = arr / cs
69	    return out
70	
71	
72	def bootstrap_chats(C_true, n_gold, B, rng):
73	    """Multinomial bootstrap of Ĉ.
74	
75	    For each class k, draw n_gold predictions from C_true[:, k] then
76	    normalise. Returns (B, K, K) array of column-stochastic matrices.
77	    """
78	    out = np.empty((B, K, K))
79	    for k in range(K):
80	        # rng.multinomial returns (B, K) with each row summing to n_gold
81	        counts = rng.multinomial(n_gold, C_true[:, k], size=B)
82	        out[:, :, k] = counts / float(n_gold)
83	    return out
84	
85	
86	def compute_asv_for_matrices(C0_batch, all_ss, all_tau_true):
87	    """Compute magnitude ASV per topology for a batch of C0 matrices.
88	
89	    Returns asv: (M, n_topo) ndarray. Collider/M-bias get +inf (protective).
90	    """
91	    M = C0_batch.shape[0]
92	    n_topo = len(RANK_TOPOS)
93	    asv = np.full((M, n_topo), np.nan)
94	    # Protective topologies: always inf
95	    asv[:, TOPO_IDX['collider']] = np.inf
96	    asv[:, TOPO_IDX['mbias']] = np.inf
97	
98	    for topo in RANK_TOPOS:
99	        if topo in PROTECTIVE:
100	            continue
101	        ss = all_ss[topo]
102	        tau_true = all_tau_true[topo]
103	        if topo == 'iv':
104	            vals = process_batch_iv(C0_batch, ss, tau_true)
105	        elif topo == 'exposure':
106	            vals, _ = process_batch_exposure(C0_batch, ss, tau_true)
107	        else:
108	            vals, _ = process_batch_with_T(C0_batch, ss, tau_true, topo)
109	        asv[:, TOPO_IDX[topo]] = vals
110	    return asv
111	
112	
113	def partition_from_asv(asv_row):
114	    """Bottom-2 topologies (smallest ASV) form the fragile set."""
115	    order = np.argsort(asv_row, kind='stable')
116	    return frozenset(RANK_TOPOS[i] for i in order[:2])
117	
118	
119	def spearman_versus_truth(asv_boot, asv_true):
120	    """Spearman rho between bootstrap ASV ranking and truth ranking."""
121	    # Handle infinities: replace +inf with large finite via rank ordering.
122	    # scipy.spearmanr is OK with finite inputs; rankdata handles infinities.
123	    r_true = rankdata(asv_true)
124	    r_boot = rankdata(asv_boot)
125	    # If all values are identical (or all inf), correlation undefined → NaN
126	    if np.all(r_true == r_true[0]) or np.all(r_boot == r_boot[0]):
127	        return np.nan
128	    rho, _ = spearmanr(r_true, r_boot)
129	    return rho
130	
131	
132	def main():
133	    t_total = time.time()
134	    print('Ĉ Estimation Robustness Experiment')
135	    print(f'  K={K}, B={B_BOOT}, n_gold ∈ {N_GOLD_GRID}')
136	    print(f'  Topologies: {RANK_TOPOS}')
137	    print(f'  ASV threshold (magnitude): {ASV_EPSILON}')
138	    print(f'  n_delta = {N_DELTA}')
139	    print('=' * 70)
140	    sys.stdout.flush()
141	
142	    # Precompute analytic sufficient statistics + tau_true
143	    print('\nPrecomputing sufficient statistics & tau_true...')
144	    all_ss = {}
145	    all_tau_true = {}
146	    for topo in ALL_TOPOS:
147	        ss = COMPUTE_SS[topo](DGP_PARAMS[topo])
148	        all_ss[topo] = ss
149	        all_tau_true[topo] = get_tau_true(topo, ss)
150	        print(f'  {topo:<12} tau_true = {all_tau_true[topo]:.6f}')
151	    sys.stdout.flush()
152	
153	    # Load empirical K=3 matrices
154	    print('\nLoading empirical K=3 confusion matrices...')
155	    Cs = load_k3_matrices()
156	    print(f'  Loaded {len(Cs)} K=3 matrices')
157	    for name in Cs:
158	        print(f'    {name}  diag={np.diag(Cs[name]).round(3).tolist()}')
159	    sys.stdout.flush()
160	
161	    # Truth ASV per source C
162	    print('\nComputing ASV for the truth Cs...')
163	    truth_C_batch = np.stack(list(Cs.values()))
164	    truth_asv = compute_asv_for_matrices(truth_C_batch, all_ss, all_tau_true)
165	    truth_partition = {}
166	    truth_asv_dict = {}
167	    for i, name in enumerate(Cs):
168	        truth_partition[name] = partition_from_asv(truth_asv[i])
169	        truth_asv_dict[name] = {
170	            RANK_TOPOS[j]: (None if np.isinf(truth_asv[i, j])
171	                            else float(truth_asv[i, j]))
172	            for j in range(len(RANK_TOPOS))
173	        }
174	        eq = 'YES' if truth_partition[name] == FRAGILE else 'NO'
175	        print(f'  {name}  fragile-set={sorted(truth_partition[name])}  '
176	              f'matches canonical: {eq}')
177	    sys.stdout.flush()
178	
179	    # Bootstrap loop
180	    print(f'\nBootstrapping (B={B_BOOT})...')
181	    rng = np.random.default_rng(SEED)
182	
183	    results_per_n = {}
184	    for n_gold in N_GOLD_GRID:
185	        t0 = time.time()
186	        partition_match_total = 0   # vs canonical {exposure,iv}
187	        partition_match_truth = 0   # vs source-C truth partition
188	        n_bootstraps_total = 0
189	        rho_values_vs_truth = []
190	        rho_values_vs_theoretical_safe = []
191	
192	        # Per-source-C aggregates
193	        per_C = {}
194	
195	        for name, C_true in Cs.items():
196	            boot = bootstrap_chats(C_true, n_gold, B_BOOT, rng)
197	            asv_boot = compute_asv_for_matrices(
198	                boot, all_ss, all_tau_true)  # (B, n_topo)
199	
200	            truth_row = truth_asv[list(Cs).index(name)]
201	
202	            n_match_canon = 0
203	            n_match_truth = 0
204	            rho_vs_truth = []
205	            for b in range(B_BOOT):
206	                part = partition_from_asv(asv_boot[b])
207	                if part == FRAGILE:
208	                    n_match_canon += 1
209	                if part == truth_partition[name]:
210	                    n_match_truth += 1
211	                rho_vs_truth.append(
212	                    spearman_versus_truth(asv_boot[b], truth_row))
213	
214	            rho_vs_truth = np.array(rho_vs_truth, dtype=float)
215	            rho_clean = rho_vs_truth[~np.isnan(rho_vs_truth)]
216	
217	            per_C[name] = {
218	                'partition_match_canonical': n_match_canon / B_BOOT,
219	                'partition_match_truth_C': n_match_truth / B_BOOT,
220	                'spearman_rho_mean_vs_truth':
221	                    float(rho_clean.mean()) if rho_clean.size else float('nan'),
222	                'spearman_rho_median_vs_truth':
223	                    float(np.median(rho_clean)) if rho_clean.size else float('nan'),
224	                'spearman_rho_q25_vs_truth':
225	                    float(np.quantile(rho_clean, 0.25)) if rho_clean.size else float('nan'),
226	                'truth_partition_matches_canonical':
227	                    truth_partition[name] == FRAGILE,
228	            }
229	
230	            partition_match_total += n_match_canon
231	            partition_match_truth += n_match_truth
232	            n_bootstraps_total += B_BOOT
233	            rho_values_vs_truth.extend(rho_clean.tolist())
234	
235	        results_per_n[n_gold] = {
236	            'n_bootstraps_total': n_bootstraps_total,
237	            'partition_stability_rate_vs_canonical':
238	                partition_match_total / n_bootstraps_total,
239	            'partition_stability_rate_vs_truth_C':
240	                partition_match_truth / n_bootstraps_total,
241	            'spearman_rho_mean':
242	                float(np.mean(rho_values_vs_truth)) if rho_values_vs_truth
243	                else float('nan'),
244	            'spearman_rho_median':
245	                float(np.median(rho_values_vs_truth)) if rho_values_vs_truth
246	                else float('nan'),
247	            'spearman_rho_q25':
248	                float(np.quantile(rho_values_vs_truth, 0.25))
249	                if rho_values_vs_truth else float('nan'),
250	            'spearman_rho_q75':
251	                float(np.quantile(rho_values_vs_truth, 0.75))
252	                if rho_values_vs_truth else float('nan'),
253	            'per_source_C': per_C,
254	        }
255	        elapsed = time.time() - t0
256	        r = results_per_n[n_gold]
257	        print(f'  n_gold={n_gold:<4}  '
258	              f'partition_rate_canonical={r["partition_stability_rate_vs_canonical"]:.4f}  '
259	              f'partition_rate_truth={r["partition_stability_rate_vs_truth_C"]:.4f}  '
260	              f'rho_mean={r["spearman_rho_mean"]:.4f}  '
261	              f'({elapsed:.1f}s)')
262	        sys.stdout.flush()
263	
264	    # Summary
265	    print('\n' + '=' * 70)
266	    print('Summary')
267	    print('=' * 70)
268	    print(f'{"n_gold":<8}{"part_canon":<14}{"part_truth":<14}'
269	          f'{"rho_mean":<12}{"rho_median":<12}')
270	    for n_gold in N_GOLD_GRID:
271	        r = results_per_n[n_gold]
272	        print(f'{n_gold:<8}'
273	              f'{r["partition_stability_rate_vs_canonical"]:<14.4f}'
274	              f'{r["partition_stability_rate_vs_truth_C"]:<14.4f}'
275	              f'{r["spearman_rho_mean"]:<12.4f}'
276	              f'{r["spearman_rho_median"]:<12.4f}')
277	
278	    # Save
279	    total_time = time.time() - t_total
280	    out = {
281	        'description': ('Ĉ estimation robustness under multinomial bootstrap'
282	                        ' from finite gold set'),
283	        'config': {
284	            'K': K,
285	            'n_gold_grid': N_GOLD_GRID,
286	            'B_bootstrap': B_BOOT,
287	            'seed': SEED,
288	            'asv_threshold': ASV_EPSILON,
289	            'n_delta': N_DELTA,
290	            'topologies': RANK_TOPOS,
291	            'canonical_safe': sorted(SAFE),
292	            'canonical_fragile': sorted(FRAGILE),
293	            'empirical_path': EMP_PATH,
294	        },
295	        'source_matrices': {
296	            name: {
297	                'C': Cs[name].tolist(),
298	                'diag': np.diag(Cs[name]).tolist(),
299	                'truth_asv': truth_asv_dict[name],
300	                'truth_fragile_set': sorted(truth_partition[name]),
301	                'truth_matches_canonical':
302	                    truth_partition[name] == FRAGILE,
303	            }
304	            for name in Cs
305	        },
306	        'results_per_n_gold': {
307	            str(n): results_per_n[n] for n in N_GOLD_GRID
308	        },
309	        'total_time_seconds': total_time,
310	    }
311	    with open(OUT_PATH, 'w') as f:
312	        json.dump(out, f, indent=2)
313	    print(f'\nJSON saved: {OUT_PATH}')
314	    print(f'Total: {total_time:.1f}s')
315	
316	
317	if __name__ == '__main__':
318	    main()
319	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "4f370b26-e2d2-4658-9300-547360946563"
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Running grep -l \"confounding\\|mediation\\|collider\\|frontd…",
  "usage": {
    "total_tokens": 42240,
    "tool_uses": 11,
    "duration_ms": 21067
  },
  "last_tool_name": "Bash",
  "uuid": "d382ab0e-5f93-4db3-bfde-29242ab13103",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01JkKDDfgyH8uWXKqM8hwV3E`</summary>

```json
{
  "command": "grep -l \"confounding\\|mediation\\|collider\\|frontdoor\\|mbias\\|exposure\\|IV\" /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/*.py | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "4c3b9c15-b46b-4741-ab1c-98a7b4492ceb",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01B1iUxRqAeBHRhUdt4Khewt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 4964,
      "cache_read_input_tokens": 37045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4964,
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

_source line 39 · 2026-05-23T14:56:16.669Z_

<details><summary>↩ Tool result · `toolu_01JkKDDfgyH8uWXKqM8hwV3E`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/analyze_epsilon_bound.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/analyze_epsilon_sign_structure.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/bootstrap_ci_convergence.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_all_tasks.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_delta_max.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_ppi_empirical.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_theory_empirical_mape.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_unified_mape.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_updated_empirical.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture_dgp_sensitivity.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/correction_k_sensitivity.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_b_logistic_dgp.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_c_bootstrap_asv.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify_v2.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_epsilon_tau_sensitivity.py
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_e_asv_stability.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "29d757de-6d87-4633-868b-0ed61200c6c6"
}
```

</details>

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Searching for def.*bias.*plim|def compute.*bias",
  "usage": {
    "total_tokens": 43204,
    "tool_uses": 12,
    "duration_ms": 22952
  },
  "last_tool_name": "Grep",
  "uuid": "4f4cfd59-4506-4105-af0c-50bc4d517bcb",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Grep · `toolu_014CYRsFYLJ2Hg8u2XoBrs3F`</summary>

```json
{
  "pattern": "def.*bias.*plim|def compute.*bias",
  "type": "py",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "6dfa4669-666f-424a-8bc6-8d5f7b01087d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013tWLFgPuMkEMN6j89jGC8g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 962,
      "cache_read_input_tokens": 42009,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 962,
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

_source line 42 · 2026-05-23T14:56:18.519Z_

<details><summary>↩ Tool result · `toolu_014CYRsFYLJ2Hg8u2XoBrs3F`</summary>

```text
Found 10 files
artifacts/conjecture_dgp_sensitivity.py
artifacts/ranking_stability.py
artifacts/analyze_epsilon_sign_structure.py
artifacts/analyze_epsilon_bound.py
artifacts/exp_d_conjecture_verify_v2.py
artifacts/exp_d_conjecture_verify.py
artifacts/compute_updated_empirical.py
artifacts/plan_005_asv_extended_fixed.py
artifacts/_project/data/mvp_exposure_dag.py
artifacts/mvp_exposure_dag.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "2c68b460-1add-40d7-915b-81b641526daf"
}
```

</details>

---

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Reading artifacts/compute_updated_empirical.py",
  "usage": {
    "total_tokens": 43615,
    "tool_uses": 13,
    "duration_ms": 24357
  },
  "last_tool_name": "Read",
  "uuid": "b70dac98-a7db-4a68-a9f9-e02b58b7bfcf",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01VymwweYni6sK7NxbkThfAn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_updated_empirical.py",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "62fd6607-4a77-4d7a-a6b7-ff69a71ecff2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01S1ygzq166tkVfwMspMxpfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 42971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 402,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 45 · 2026-05-23T14:56:19.910Z_

<details><summary>↩ Tool result · `toolu_01VymwweYni6sK7NxbkThfAn`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Compute bias for all available confusion matrices (plan006 + plan011 frontier).
4	Merges HumAID K=10 (from plan006), VAST K=3 and CivilComments K=2 (from plan011
5	frontier extractions + existing 7B data) and computes 7-topology biases.
6	
7	Fixes applied (Reviewer CRITICAL):
8	  1. Label consistency validation: all CMs for same (dataset, K) must share label order
9	  2. Exclude vast_deepseek_zero-shot (1000 samples, near-degenerate neutral recall)
10	  3. Exposure sign flip checks ALL K-1 coefficients (not just coefs[1])
11	  4. Per-coefficient sign flip details recorded for exposure topology
12	
13	Output: artifacts/updated_empirical_results.json
14	"""
15	
16	import json
17	import sys
18	import numpy as np
19	from pathlib import Path
20	from collections import defaultdict
21	
22	PROJ = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib")
23	sys.path.insert(0, str(PROJ))
24	
25	import importlib.util
26	spec = importlib.util.spec_from_file_location(
27	    "plan_006",
28	    str(PROJ / "plan_006_asv_empirical.py")
29	)
30	plan_006 = importlib.util.module_from_spec(spec)
31	spec.loader.exec_module(plan_006)
32	
33	TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
34	              'mbias', 'iv', 'frontdoor']
35	
36	MIN_SAMPLES = 500
37	
38	EXCLUDE_CONFIGS = {
39	    "vast/deepseek_zero-shot",
40	}
41	
42	
43	def validate_label_consistency(frontier_data):
44	    """Assert all CMs for same (dataset, K) have identical label ordering."""
45	    by_group = defaultdict(list)
46	    for raw_key, entry in frontier_data.items():
47	        labels = entry.get("labels", [])
48	        K = np.array(entry["confusion_matrix_normalized"]).shape[0]
49	        dataset = raw_key.split("/")[0] if "/" in raw_key else "unknown"
50	        by_group[(dataset, K)].append((raw_key, labels))
51	
52	    for (dataset, K), items in by_group.items():
53	        ref_labels = items[0][1]
54	        for raw_key, labels in items[1:]:
55	            if labels != ref_labels:
56	                raise ValueError(
57	                    f"Label mismatch in ({dataset}, K={K}): "
58	                    f"{items[0][0]} has {ref_labels}, {raw_key} has {labels}"
59	                )
60	        if ref_labels:
61	            print(f"  Label check OK: ({dataset}, K={K}) → {ref_labels} ({len(items)} CMs)")
62	
63	
64	def load_all_cms():
65	    """Load confusion matrices from plan006 (HumAID) + plan011 frontier extractions."""
66	    all_cms = {}
67	    meta = {}
68	
69	    # 1. HumAID K=10 from plan006 (authoritative, full matrices)
70	    with open(PROJ / "artifacts/plan006/asv_empirical_results.json") as f:
71	        plan006 = json.load(f)
72	    for key, cm in plan006["confusion_matrices"].items():
73	        C = np.array(cm)
74	        if np.min(np.diag(C)) > 0:
75	            all_cms[key] = C
76	            parts = key.split("_", 1)
77	            model_prompt = parts[1] if len(parts) > 1 else key
78	            meta[key] = {"dataset": "humaid", "model_prompt": model_prompt, "K": 10,
79	                         "source": "plan006"}
80	
81	    # 2. Plan011 frontier extractions (VAST + CivilComments + any new)
82	    with open(PROJ / "artifacts/plan011_frontier_cms.json") as f:
83	        frontier = json.load(f)
84	
85	    validate_label_consistency(frontier)
86	
87	    for raw_key, entry in frontier.items():
88	        if raw_key in EXCLUDE_CONFIGS:
89	            print(f"  EXCLUDE {raw_key}: in exclusion list (degenerate)")
90	            continue
91	
92	        C = np.array(entry["confusion_matrix_normalized"])
93	        n_valid = entry.get("n_valid", entry.get("n_samples", 0))
94	        labels = entry.get("labels", [])
95	        K = C.shape[0]
96	
97	        if n_valid < MIN_SAMPLES:
98	            print(f"  SKIP {raw_key}: n_valid={n_valid} < {MIN_SAMPLES}")
99	            continue
100	
101	        norm_key = raw_key.replace("/", "_")
102	
103	        col_sums = C.sum(axis=0)
104	        if not np.allclose(col_sums, 1.0, atol=0.05):
105	            row_sums = C.sum(axis=1)
106	            if np.allclose(row_sums, 1.0, atol=0.05):
107	                C = C.T
108	            else:
109	                print(f"  WARN {raw_key}: neither row nor col stochastic, normalizing columns")
110	                C = C / C.sum(axis=0, keepdims=True)
111	
112	        if norm_key in all_cms:
113	            print(f"  SKIP {norm_key}: already in plan006")
114	            continue
115	
116	        if raw_key.startswith("civil_comments/"):
117	            dataset = "civil_comments"
118	            model_prompt = raw_key[len("civil_comments/"):]
119	        elif raw_key.startswith("vast/"):
120	            dataset = "vast"
121	            model_prompt = raw_key[len("vast/"):]
122	        elif raw_key.startswith("humaid/"):
123	            dataset = "humaid"
124	            model_prompt = raw_key[len("humaid/"):]
125	        else:
126	            dataset = "unknown"
127	            model_prompt = raw_key
128	
129	        all_cms[norm_key] = C
130	        meta[norm_key] = {
131	            "dataset": dataset, "model_prompt": model_prompt, "K": K,
132	            "source": "plan011_frontier", "n_valid": n_valid,
133	            "labels": labels,
134	            "accuracy": entry.get("accuracy", None),
135	        }
136	
137	    return all_cms, meta
138	
139	
140	def check_exposure_sign_flips(plim_true, plim_biased, K):
141	    """Check ALL K-1 exposure coefficients for sign reversal.
142	
143	    Returns (any_flip: bool, details: list of per-coefficient results).
144	    Coefficients are at indices 1..K-1 (index 0 is the intercept).
145	    """
146	    details = []
147	    any_flip = False
148	    for i in range(1, K):
149	        true_val = float(plim_true[i])
150	        biased_val = float(plim_biased[i])
151	        if not (np.isfinite(true_val) and np.isfinite(biased_val)):
152	            details.append({"coef_idx": i, "true": true_val, "biased": biased_val,
153	                            "sign_flip": False, "note": "non-finite"})
154	            continue
155	        sf = bool(np.sign(biased_val) != np.sign(true_val)) if abs(true_val) > 1e-10 else False
156	        if sf:
157	            any_flip = True
158	        details.append({
159	            "coef_idx": i,
160	            "true": round(true_val, 6),
161	            "biased": round(biased_val, 6),
162	            "sign_flip": sf,
163	        })
164	    return any_flip, details
165	
166	
167	def compute_biases(all_cms, config_meta):
168	    """Compute plim bias for all (config, topology) pairs.
169	
170	    For exposure topology: checks ALL K-1 coefficients for sign flips.
171	    For IV: scalar Wald estimator (sign flip on tau).
172	    For others: tau = plim_result[1] (treatment coefficient).
173	    """
174	    Ks_used = sorted(set(m["K"] for m in config_meta.values()))
175	    params_by_K = {K: plan_006.make_dgp_params(K) for K in Ks_used}
176	    suff_stats = {}
177	    tau_true_cache = {}
178	    plim_true_cache = {}
179	
180	    for K in Ks_used:
181	        for topo in TOPOLOGIES:
182	            st = plan_006.precompute_suff_stats(K, topo, params_by_K[K][topo])
183	            suff_stats[(K, topo)] = st
184	            plim_I = plan_006.compute_plim(np.eye(K), st, K)
185	            tau_true_cache[(K, topo)] = plan_006.extract_tau(plim_I, topo)
186	            plim_true_cache[(K, topo)] = plim_I
187	
188	    bias_records = []
189	    sign_flips = 0
190	    exposure_coef_sign_flips = 0
191	    total = 0
192	
193	    for config_key, C in sorted(all_cms.items()):
194	        m = config_meta[config_key]
195	        K = m["K"]
196	        dataset = m["dataset"]
197	        model_prompt = m["model_prompt"]
198	
199	        parts = model_prompt.rsplit("_", 1)
200	        if len(parts) == 2 and parts[1] in ["zero-shot", "few-shot-3", "few-shot-5"]:
201	            model, prompt = parts
202	        else:
203	            for p in ["zero-shot", "few-shot-3", "few-shot-5"]:
204	                if model_prompt.endswith(p):
205	                    model = model_prompt[:-(len(p)+1)]
206	                    prompt = p
207	                    break
208	            else:
209	                model = model_prompt
210	                prompt = "unknown"
211	
212	        for topo in TOPOLOGIES:
213	            tau_true = tau_true_cache[(K, topo)]
214	            st = suff_stats[(K, topo)]
215	
216	            try:
217	                plim_C = plan_006.compute_plim(C, st, K)
218	            except Exception:
219	                continue
220	
221	            if topo == 'exposure':
222	                plim_I = plim_true_cache[(K, topo)]
223	                if isinstance(plim_C, np.ndarray) and isinstance(plim_I, np.ndarray):
224	                    any_flip, coef_details = check_exposure_sign_flips(plim_I, plim_C, K)
225	                    tau_biased = plan_006.extract_tau(plim_C, topo)
226	                    if not np.isfinite(tau_biased) or not np.isfinite(tau_true):
227	                        continue
228	                    bias = tau_biased - tau_true
229	                    bias_pct = abs(bias / tau_true) if abs(tau_true) > 1e-10 else float('inf')
230	                    if any_flip:
231	                        sign_flips += 1
232	                        exposure_coef_sign_flips += sum(1 for d in coef_details if d["sign_flip"])
233	                    total += 1
234	                    bias_records.append({
235	                        "dataset": dataset, "model": model, "prompt": prompt,
236	                        "K": K, "topology": topo,
237	                        "tau_true": float(tau_true), "tau_hat": float(tau_biased),
238	                        "bias": float(bias), "bias_pct": float(bias_pct),
239	                        "sign_flip": any_flip,
240	                        "exposure_coef_details": coef_details,
241	                        "source": m.get("source", "unknown"),
242	                    })
243	                    continue
244	
245	            tau_biased = plan_006.extract_tau(plim_C, topo)
246	            if not np.isfinite(tau_biased) or not np.isfinite(tau_true):
247	                continue
248	
249	            bias = tau_biased - tau_true
250	            bias_pct = abs(bias / tau_true) if abs(tau_true) > 1e-10 else float('inf')
251	            sf = bool(np.sign(tau_biased) != np.sign(tau_true)) if abs(tau_true) > 1e-10 else False
252	
253	            if sf:
254	                sign_flips += 1
255	            total += 1
256	
257	            bias_records.append({
258	                "dataset": dataset, "model": model, "prompt": prompt,
259	                "K": K, "topology": topo,
260	                "tau_true": float(tau_true), "tau_hat": float(tau_biased),
261	                "bias": float(bias), "bias_pct": float(bias_pct),
262	                "sign_flip": sf,
263	                "source": m.get("source", "unknown"),
264	            })
265	
266	    return bias_records, sign_flips, total, exposure_coef_sign_flips
267	
268	
269	def main():
270	    print("Loading confusion matrices...")
271	    all_cms, config_meta = load_all_cms()
272	    print(f"\nTotal configs: {len(all_cms)}")
273	    for k, m in sorted(config_meta.items()):
274	        C = all_cms[k]
275	        print(f"  {k}: K={m['K']}, diag_mean={np.diag(C).mean():.3f}, src={m.get('source', '?')}")
276	
277	    print(f"\nComputing biases across {len(TOPOLOGIES)} topologies...")
278	    bias_records, sign_flips, total, exposure_coef_sf = compute_biases(all_cms, config_meta)
279	
280	    datasets = set(r["dataset"] for r in bias_records)
281	    models = set(r["model"] for r in bias_records)
282	    n_configs = len(all_cms)
283	
284	    by_dataset = defaultdict(list)
285	    by_topology = defaultdict(list)
286	    for r in bias_records:
287	        by_dataset[r["dataset"]].append(r)
288	        by_topology[r["topology"]].append(r)
289	
290	    print(f"\n{'='*70}")
291	    print(f"RESULTS SUMMARY")
292	    print(f"{'='*70}")
293	    print(f"Total configs: {n_configs}")
294	    print(f"Total scenarios: {total}")
295	    print(f"Sign flips (any coef): {sign_flips}")
296	    print(f"Exposure coefficient-level sign flips: {exposure_coef_sf}")
297	    print(f"Datasets: {sorted(datasets)}")
298	    print(f"Models: {sorted(models)}")
299	
300	    # Exposure coefficient details
301	    print(f"\nExposure coefficient-level details:")
302	    for r in bias_records:
303	        if r["topology"] == "exposure" and "exposure_coef_details" in r:
304	            details = r["exposure_coef_details"]
305	            flipped = [d for d in details if d["sign_flip"]]
306	            if flipped:
307	                print(f"  ⚠️ {r['dataset']}/{r['model']}_{r['prompt']}: "
308	                      f"{len(flipped)}/{len(details)} coefs flipped: {flipped}")
309	            else:
310	                vals = [(d["coef_idx"], d["true"], d["biased"]) for d in details]
311	                print(f"  ✓ {r['dataset']}/{r['model']}_{r['prompt']}: no flip {vals}")
312	
313	    print(f"\nPer-dataset:")
314	    for ds in sorted(datasets):
315	        recs = by_dataset[ds]
316	        n_cfg = len(set(f"{r['model']}_{r['prompt']}" for r in recs))
317	        mean_bias = np.mean([r['bias_pct'] for r in recs])
318	        sf = sum(r['sign_flip'] for r in recs)
319	        print(f"  {ds}: {n_cfg} configs, {len(recs)} scenarios, mean_abs_bias={mean_bias:.3f}, sign_flips={sf}")
320	
321	    print(f"\nPer-topology:")
322	    for topo in TOPOLOGIES:
323	        recs = by_topology[topo]
324	        mean_bias = np.mean([r['bias_pct'] for r in recs])
325	        max_bias = max([r['bias_pct'] for r in recs])
326	        sf = sum(r['sign_flip'] for r in recs)
327	        print(f"  {topo}: mean_bias_pct={mean_bias:.3f}, max={max_bias:.3f}, sign_flips={sf}")
328	
329	    # Model tier comparison
330	    print(f"\nFrontier vs 7B comparison:")
331	    frontier_biases = [r['bias_pct'] for r in bias_records if 'qwen2.5-7b' not in r['model']]
332	    sevb_biases = [r['bias_pct'] for r in bias_records if 'qwen2.5-7b' in r['model']]
333	    if frontier_biases and sevb_biases:
334	        print(f"  Frontier mean abs bias: {np.mean(frontier_biases):.3f}")
335	        print(f"  7B mean abs bias: {np.mean(sevb_biases):.3f}")
336	        print(f"  Ratio 7B/frontier: {np.mean(sevb_biases)/np.mean(frontier_biases):.2f}")
337	
338	    output = {
339	        "confusion_matrices": {k: all_cms[k].tolist() for k in sorted(all_cms.keys())},
340	        "config_meta": {k: v for k, v in config_meta.items()},
341	        "biases": bias_records,
342	        "summary": {
343	            "total_configs": n_configs,
344	            "total_scenarios": total,
345	            "sign_flips": sign_flips,
346	            "exposure_coef_level_sign_flips": exposure_coef_sf,
347	            "datasets": sorted(datasets),
348	            "models": sorted(models),
349	            "excluded_configs": list(EXCLUDE_CONFIGS),
350	            "per_dataset": {
351	                ds: {
352	                    "n_configs": len(set(f"{r['model']}_{r['prompt']}" for r in recs)),
353	                    "n_scenarios": len(recs),
354	                    "mean_abs_bias_pct": float(np.mean([r['bias_pct'] for r in recs])),
355	                    "sign_flips": sum(r['sign_flip'] for r in recs),
356	                }
357	                for ds, recs in by_dataset.items()
358	            },
359	            "per_topology": {
360	                topo: {
361	                    "mean_abs_bias_pct": float(np.mean([r['bias_pct'] for r in recs])),
362	                    "max_abs_bias_pct": float(max(r['bias_pct'] for r in recs)),
363	                    "sign_flips": sum(r['sign_flip'] for r in recs),
364	                }
365	                for topo, recs in by_topology.items()
366	            },
367	        }
368	    }
369	
370	    out_path = PROJ / "artifacts/updated_empirical_results.json"
371	    with open(out_path, "w") as f:
372	        json.dump(output, f, indent=2)
373	    print(f"\nSaved: {out_path}")
374	
375	
376	if __name__ == "__main__":
377	    main()
378	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "4487380f-04fe-488b-a656-8edbc52d7787"
}
```

</details>

---

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Running ls -lh /home/ubuntu/.agent-ml-research-prod_0510/…",
  "usage": {
    "total_tokens": 49420,
    "tool_uses": 14,
    "duration_ms": 27161
  },
  "last_tool_name": "Bash",
  "uuid": "c9c28545-e5b8-4ada-ac99-ffc34320d155",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gi8n31XMS4AtcsiEMiBQ1v`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/latest/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "94980bd0-7db6-44ad-8705-9e9f7300dd28",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019oru9a3iRFgY2qqvzR58r6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5803,
      "cache_read_input_tokens": 43373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5803,
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

_source line 48 · 2026-05-23T14:56:22.764Z_

<details><summary>↩ Tool result · `toolu_01Gi8n31XMS4AtcsiEMiBQ1v`</summary>

```text
total 12K
drwxr-xr-x 2 ubuntu ubuntu 4.0K May 21 08:32 logs
-rw-r--r-- 1 ubuntu ubuntu 4.4K May 21 08:32 meta.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "d4535c48-b2bc-4942-9efe-cb33d6c2e629"
}
```

</details>

---

### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Running find /home/ubuntu/.agent-ml-research-prod_0510/pr…",
  "usage": {
    "total_tokens": 49672,
    "tool_uses": 15,
    "duration_ms": 28585
  },
  "last_tool_name": "Bash",
  "uuid": "0b40a249-3dd8-4bef-89b2-e74ee19b7b4e",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Bash · `toolu_0169Q8mmrEx4n3Rzp7ZnZuPe`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts -name \"*.json\" -type f | wc -l"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "e8b80414-3580-4770-8613-98ba2b0e5c62",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EVvbj2BX97vhaByxi6JTR1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 189,
      "cache_read_input_tokens": 49176,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 189,
        "ephemeral_1h_input_tokens": 0
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

_source line 51 · 2026-05-23T14:56:24.175Z_

<details><summary>↩ Tool result · `toolu_0169Q8mmrEx4n3Rzp7ZnZuPe`</summary>

```text
60
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "eab9626c-5bdb-4070-bf5f-ca09f4811dd1"
}
```

</details>

---

### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Running find /home/ubuntu/.agent-ml-research-prod_0510/pr…",
  "usage": {
    "total_tokens": 49783,
    "tool_uses": 16,
    "duration_ms": 30284
  },
  "last_tool_name": "Bash",
  "uuid": "bcd81884-1476-4abd-b6a9-642aee5dd54b",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_013VfrKJ95GwgHeast8uwhmi`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib -name \"plan_006*.py\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "f668bf8e-dad2-4a75-9d72-29ffef6d6f9c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JjWeqgQef9mDJmZLWivdpt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 109,
      "cache_read_input_tokens": 49365,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 109,
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

_source line 54 · 2026-05-23T14:56:25.893Z_

<details><summary>↩ Tool result · `toolu_013VfrKJ95GwgHeast8uwhmi`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "0ca30cc2-a7b4-4e69-b8e8-bc42d0e5368f"
}
```

</details>

---

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Reading plan_006_asv_empirical.py",
  "usage": {
    "total_tokens": 49990,
    "tool_uses": 17,
    "duration_ms": 31759
  },
  "last_tool_name": "Read",
  "uuid": "d1525cc5-10c3-4de5-83a0-ae4c164c2bd1",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Read · `toolu_01PZTNTWuXgsphMxt2Hwd9VB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "limit": 800
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "fce87718-8657-44a5-96f3-4c10dafb609d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011eN97CJmV4PWEYmN9hajZ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 162,
      "cache_read_input_tokens": 49474,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 162,
        "ephemeral_1h_input_tokens": 0
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

### Tool result

_source line 57 · 2026-05-23T14:56:27.583Z_

<details><summary>↩ Tool result · `toolu_01PZTNTWuXgsphMxt2Hwd9VB`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "7c59e29a-7871-471b-a672-7334e9dff4a9"
}
```

</details>

---

### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Reading plan_006_asv_empirical.py",
  "usage": {
    "total_tokens": 62456,
    "tool_uses": 18,
    "duration_ms": 34571
  },
  "last_tool_name": "Read",
  "uuid": "39abb01f-3a72-4646-bf57-ae3688910489",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Read · `toolu_01BZWSbWNsiTPS6XfqiV36rS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py",
  "limit": 400,
  "offset": 800
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "172e1ca9-78f7-4e42-a3d0-66e0b24bda56",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018SeNFcFGJmV8QGFsQdUyNw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12460,
      "cache_read_input_tokens": 49636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12460,
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

_source line 60 · 2026-05-23T14:56:30.127Z_

<details><summary>↩ Tool result · `toolu_01BZWSbWNsiTPS6XfqiV36rS`</summary>

```text
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
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "4b00f151-2a30-4602-87a0-95721624d56b"
}
```

</details>

---

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Running find /home/ubuntu/.agent-ml-research-prod_0510/pr…",
  "usage": {
    "total_tokens": 67662,
    "tool_uses": 19,
    "duration_ms": 36820
  },
  "last_tool_name": "Bash",
  "uuid": "b4debc4e-4fc0-47f7-acd3-b6796507ddec",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Bash · `toolu_012byKYxZew9oXzqhtT1xj9d`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts -name \"*.json\" | xargs grep -l \"confusion\" 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "9dc330bf-75f7-4ee0-97f9-20470ea3b5d7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SSd4SCykfdSME2VercgKiA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5205,
      "cache_read_input_tokens": 62096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5205,
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

_source line 63 · 2026-05-23T14:56:32.425Z_

<details><summary>↩ Tool result · `toolu_012byKYxZew9oXzqhtT1xj9d`</summary>

```text
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/plan011_frontier_cms.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/updated_empirical_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/_project/data/nondiff_stress_test_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/delta_max_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/nondiff_topic_stratified_results.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_cms.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/median/experiment_data.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/worst/experiment_data.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260520T074549/best/experiment_data.json
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/dream_reports/dream_20260521T054528/best/experiment_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "9520c6b1-1af0-4ef0-9473-1f09d501dfae"
}
```

</details>

---

### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Running head -100 /home/ubuntu/.agent-ml-research-prod_05…",
  "usage": {
    "total_tokens": 68267,
    "tool_uses": 20,
    "duration_ms": 38507
  },
  "last_tool_name": "Bash",
  "uuid": "8e6418f3-fbb7-49ff-865c-d5dde4004155",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_01SokGrRHVWTcfdS1YcrwQVP`</summary>

```json
{
  "command": "head -100 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "63ad9f28-354d-4655-8472-94ef1d6f456a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BTnNAhTSHuy3Rz2Pn5iwBd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 603,
      "cache_read_input_tokens": 67301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 603,
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

_source line 66 · 2026-05-23T14:56:34.089Z_

<details><summary>↩ Tool result · `toolu_01SokGrRHVWTcfdS1YcrwQVP`</summary>

```text
{
  "confusion_matrices": {
    "civil_comments_deepseek_few-shot-5": [
      [
        0.7341211225997046,
        0.19863013698630136
      ],
      [
        0.2658788774002954,
        0.8013698630136986
      ]
    ],
    "civil_comments_qwen2.5-7b_few-shot-3": [
      [
        0.6787296898079763,
        0.2191780821917808
      ],
      [
        0.3212703101920236,
        0.7808219178082192
      ]
    ],
    "civil_comments_qwen2.5-7b_few-shot-5": [
      [
        0.7370753323485968,
        0.23972602739726026
      ],
      [
        0.26292466765140327,
        0.7602739726027398
      ]
    ],
    "civil_comments_qwen2.5-7b_zero-shot": [
      [
        0.7481536189069424,
        0.3150684931506849
      ],
      [
        0.2518463810930576,
        0.684931506849315
      ]
    ],
    "civil_comments_qwen3_few-shot-3": [
      [
        0.8179126572908957,
        0.25517241379310346
      ],
      [
        0.18208734270910437,
        0.7448275862068966
      ]
    ],
    "civil_comments_qwen3_few-shot-5": [
      [
        0.8240534521158129,
        0.20689655172413793
      ],
      [
        0.1759465478841871,
        0.7931034482758621
      ]
    ],
    "civil_comments_qwen3_zero-shot": [
      [
        0.778118609406953,
        0.25742574257425743
      ],
      [
        0.22188139059304704,
        0.7425742574257426
      ]
    ],
    "humaid_deepseek_few-shot-3": [
      [
        0.5795454545454546,
        0.15,
        0.050955414012738856,
        0.0,
        0.0,
        0.011363636363636364,
        0.1297071129707113,
        0.0,
        0.008287292817679558,
        0.043478260869565216
      ],
      [
        0.0,
        0.7,
        0.03184713375796178,
        0.024,
        0.0,
        0.056818181818181816,
        0.03347280334728033,
        0.018867924528301886,
        0.008287292817679558,
        0.006211180124223602
      ],
      [
        0.07954545454545454,
        0.0,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "ee572d96-02e3-4826-9d40-fbc73cb0dec7"
}
```

</details>

---

### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Searching for def.*compute.*plim|def.*bias_plim|def.*tau.*true|…",
  "usage": {
    "total_tokens": 69169,
    "tool_uses": 21,
    "duration_ms": 45125
  },
  "last_tool_name": "Grep",
  "uuid": "ffded70f-deed-439e-bdc8-68ca8b0215a5",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Grep · `toolu_0131r6JGPjGyrPaE5wiQxkor`</summary>

```json
{
  "pattern": "def.*compute.*plim|def.*bias_plim|def.*tau.*true|Extract.*tau|def.*FS|def.*RF",
  "type": "py",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts",
  "output_mode": "content",
  "head_limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "049a0855-1112-4f68-870a-438f7fe40695",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Gf8E1DRnviFjLQehFLsbkb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 67904,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 896,
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

_source line 69 · 2026-05-23T14:56:40.703Z_

<details><summary>↩ Tool result · `toolu_0131r6JGPjGyrPaE5wiQxkor`</summary>

```text
artifacts/exp_d_conjecture_verify.py:285:def get_tau_true(topo, K, params, ss):
artifacts/exp_d_conjecture_verify.py:304:def compute_bias_curve(topo, C0, ss, tau_true, delta_step=DELTA_STEP):
artifacts/exp_d_conjecture_verify.py:433:def part1_random(all_ss, all_tau_true):
artifacts/exp_d_conjecture_verify.py:507:def part2_adversarial(all_ss, all_tau_true):
artifacts/exp_d_conjecture_verify.py:537:                    def objective(theta, _topo=topo, _ss=ss, _tt=tau_true,
artifacts/plan008_binarization_collapse/report/plan_008_binarization_collapse.py:177:    def __init__(self, T, Y, A, tau_true, has_T=True):
artifacts/conjecture_dgp_sensitivity.py:284:def get_tau_true(topo, params, ss):
artifacts/mvp_iv_dirichlet_subspace.py:72:def analyze(C_batch, FS, RF, tau_true):
artifacts/compute_ppi_empirical.py:277:def compute_tau_true(K, topology, params, N_large=500_000, seed=99):
artifacts/compute_ppi_empirical.py:374:def run_single_rep(K, topology, params, C, tau_true, rng, gold_frac):
artifacts/plan_002_k57_extended_7topo.py:292:def compute_metrics(plim_batch, plim_true, tau_idx=None):
artifacts/plan_005_asv_extended_fixed.py:326:def compute_bias_curve(topology, C0, param, tau_true, st, n_grid=1500):
artifacts/plan_005_asv_extended_fixed.py:358:def compute_asv_envelope(topology, C0, tau_true, param, threshold_type,
artifacts/plan_005_asv_extended_fixed.py:406:def compute_magnitude_asv_fast(tau_curve, deltas, tau_true, rel_thresh=0.1):
artifacts/exp_d_conjecture_verify_v2.py:647:def get_tau_true(topo, K, params, ss):
artifacts/exp_d_conjecture_verify_v2.py:666:def compute_bias_curve(topo, C0, ss, tau_true, delta_step=DELTA_STEP):
artifacts/exp_d_conjecture_verify_v2.py:792:def part1_random(all_ss, all_tau_true):
artifacts/exp_d_conjecture_verify_v2.py:867:def part2_adversarial(all_ss, all_tau_true):
artifacts/exp_d_conjecture_verify_v2.py:897:                    def objective(theta, _topo=topo, _ss=ss, _tt=tau_true,
artifacts/ranking_stability.py:307:def get_tau_true(topo, ss):
artifacts/ranking_stability.py:354:def process_batch_iv(C0_batch, ss, tau_true):
artifacts/ranking_stability.py:395:def process_batch_exposure(C0_batch, ss, tau_true):
artifacts/ranking_stability.py:452:def process_batch_with_T(C0_batch, ss, tau_true, topo):
artifacts/correction_k_sensitivity.py:110:def run_single_rep(K, topology, params, C, tau_true, rng):
artifacts/e2e_demo.py:105:def run_confounding_rep(rng, tau_true):
artifacts/e2e_demo.py:130:def run_exposure_rep(rng, tau_true):
artifacts/e2e_demo.py:153:def compute_summary(reps, method_keys, tau_true):
artifacts/c_estimation_robustness.py:86:def compute_asv_for_matrices(C0_batch, all_ss, all_tau_true):
artifacts/exp_c_bootstrap_asv.py:136:def compute_plim(C, st, K):
artifacts/exp_c_bootstrap_asv.py:207:def compute_magnitude_delta_star(C0, K, topology, st, tau_true):
artifacts/bootstrap_ci_convergence.py:158:def compute_plim(C, st, K):
artifacts/bootstrap_ci_convergence.py:228:def compute_magnitude_delta_star(C0, K, topology, st, tau_true):
artifacts/analyze_epsilon_sign_structure.py:64:def compute_bias_curve_exposure(C0, ss, tau_true, delta_step=0.01):
artifacts/ppi_gold_ratio_sensitivity.py:111:def run_one_rep(topology, params, C, tau_true, gold_frac, rng):
artifacts/analyze_epsilon_bound.py:305:def compute_bias_curve_exposure(C0, ss, tau_true, delta_step=0.01):
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "568bc5f1-de89-4fd4-8376-3cadb5715f67"
}
```

</details>

---

### System

_source line 70_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Running head -50 /home/ubuntu/.agent-ml-research-prod_051…",
  "usage": {
    "total_tokens": 70678,
    "tool_uses": 22,
    "duration_ms": 47771
  },
  "last_tool_name": "Bash",
  "uuid": "3dae1f5f-b11c-489a-b522-ad479d3b22e9",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Bash · `toolu_01XTFGaeyzYgvdVnDxe2yffH`</summary>

```json
{
  "command": "head -50 /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "8d7f4894-c96a-4911-ac78-a897d56090aa",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012od9LSx5maUe5f8TMdmRb4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 1495,
      "cache_read_input_tokens": 68800,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1495,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 72 · 2026-05-23T14:56:43.358Z_

<details><summary>↩ Tool result · `toolu_01XTFGaeyzYgvdVnDxe2yffH`</summary>

```text
{
  "description": "\u0108 estimation robustness under multinomial bootstrap from finite gold set",
  "config": {
    "K": 3,
    "n_gold_grid": [
      50,
      100,
      200,
      500
    ],
    "B_bootstrap": 200,
    "seed": 20260523,
    "asv_threshold": 0.05,
    "n_delta": 201,
    "topologies": [
      "confounding",
      "mediation",
      "collider",
      "exposure",
      "mbias",
      "iv",
      "frontdoor"
    ],
    "canonical_safe": [
      "collider",
      "confounding",
      "frontdoor",
      "mbias",
      "mediation"
    ],
    "canonical_fragile": [
      "exposure",
      "iv"
    ],
    "empirical_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json"
  },
  "source_matrices": {
    "vast_deepseek_few-shot-3": {
      "C": [
        [
          0.5139,
          0.1017,
          0.2888
        ],
        [
          0.3212,
          0.7985,
          0.5498
        ],
        [
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "fb528608-99a4-43cf-b177-070af69cafb8"
}
```

</details>

---

### System

_source line 73_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "description": "Reading artifacts/ranking_stability.py",
  "usage": {
    "total_tokens": 71176,
    "tool_uses": 23,
    "duration_ms": 49646
  },
  "last_tool_name": "Read",
  "uuid": "b77073b9-ffa8-468d-a0cb-86e059cb38a5",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Read · `toolu_01XJnK7fqNmDwsRvaJqz2rxa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ranking_stability.py",
  "offset": 350,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "9406e900-f346-44b2-8b39-71cc8261531a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TnKWBKoNan46cV5MBSvqUF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 70295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 496,
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

_source line 75 · 2026-05-23T14:56:45.200Z_

<details><summary>↩ Tool result · `toolu_01XJnK7fqNmDwsRvaJqz2rxa`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "15850d0e-0cb4-467c-917f-7144d3ceeacc"
}
```

</details>

---

### System

_source line 76_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a8b9c307d53e36cc9",
  "tool_use_id": "toolu_019RAmNXzxRkNsP6Bq4t2qER",
  "status": "completed",
  "output_file": "",
  "summary": "Find ASV and bias code",
  "usage": {
    "total_tokens": 73260,
    "tool_uses": 23,
    "duration_ms": 74475
  },
  "uuid": "af15167e-1fc9-4f89-b979-22b5b7c90a28",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool result

_source line 77 · 2026-05-23T14:57:10.023Z_

<details><summary>↩ Tool result · `toolu_019RAmNXzxRkNsP6Bq4t2qER`</summary>

````text
Excellent! Now I have all the information needed. Let me provide a comprehensive report.

## Summary of Findings

Based on my thorough search of the artifacts directory, here are the answers to your four questions:

---

### 1. **ASV (Magnitude) Computation in `ranking_stability.py`**

The ASV (Annotated Sensitivity Value) magnitude is computed through **vectorized batch processing** across three topologies. There's no single `compute_asv_magnitude` function, but rather three topology-specific batch processors that all implement the same magnitude ASV algorithm:

**Core Algorithm (used by all three functions):**
```python
# Lines 381-390 from ranking_stability.py (IV case, same logic for others)
# Compute running max envelope of absolute bias along delta dimension
envelope = np.fmax.accumulate(np.nan_to_num(bias_abs, nan=0.0), axis=0)
# Find first delta where envelope exceeds threshold
crossed = envelope > ASV_EPSILON  # ASV_EPSILON = 0.05 (10% of tau=0.5)
any_crossed = crossed.any(axis=0)
first_idx = crossed.argmax(axis=0)
asv_vals = np.where(any_crossed, DELTAS[first_idx], np.inf)
```

**The three batch processors are:**

1. **`process_batch_iv()`** (lines 354-392): For IV topology
   - Computes first-stage `FS(delta) = (1-d)*FS_true + d*FS_empirical`
   - Calculates tau as `tau = RF / FS[1]` for each delta
   - Returns ASV as first delta crossing the threshold, or inf if never crossed

2. **`process_batch_exposure()`** (lines 395-449): For exposure topology (no treatment T)
   - Constructs K×K moment matrix EZZ and solves for reduced-form coefficients
   - Extracts tau from coefficient[1]
   - Also computes monotonicity violations (non-decreasing check)

3. **`process_batch_with_T()`** (lines 452-516): For confounding, mediation, collider, mbias, frontdoor
   - Constructs (K+1)×(K+1) moment matrix with treatment T included
   - Extracts tau from coefficient[1]
   - Handles both non-decreasing (confounding, mediation, exposure, frontdoor, iv) and non-increasing (collider, mbias) topologies

**Key Configuration:**
- `ASV_EPSILON = 0.05` (threshold: 10% of tau_true)
- `DELTAS = np.arange(0, 1.0 + 0.005/2, 0.005)` — 201 delta points
- Protective topologies (collider, mbias) always assigned `ASV = inf` (immune to annotation error)

---

### 2. **Bias Plim Computation for 7 Topologies**

Bias computation is centralized in **`plan_006_asv_empirical.py`** and uses **`compute_plim()`** (lines 369-412) as the core function. This is the authoritative implementation used across experiments.

**Core bias computation flow (in `compute_updated_empirical.py`, lines 212-266):**

```python
for topo in TOPOLOGIES:  # 7 topologies: confounding, mediation, collider, exposure, mbias, iv, frontdoor
    plim_C = plan_006.compute_plim(C, st, K)  # C = empirical confusion matrix
    tau_biased = plan_006.extract_tau(plim_C, topo)
    tau_true = tau_true_cache[(K, topo)]  # from identity matrix C=I
    bias = tau_biased - tau_true
    bias_pct = abs(bias / tau_true)
    sign_flip = np.sign(tau_biased) != np.sign(tau_true)
```

**`compute_plim()` implementation for each topology (lines 369-412):**

- **IV**: Returns `RF / FS_star[1]` where FS_star = C @ FS vector
- **Exposure**: Solves K×K system: `EZZ @ coefs = EZY` (no T term)
  - EZZ[0,0]=1, EZZ[0,j]=q[j], EZZ[j,j]=q[j]
  - Returns full coefficient vector (tau at index 1)
- **Other 5 topologies** (confounding, mediation, collider, mbias, frontdoor): Solve (K+1)×(K+1) system
  - EZZ includes full treatment T covariance structure
  - `EZZ[1,1] = E[T²]`, `EZZ[0,1] = E[T]`, etc.
  - Returns coefficient vector (tau at index 1)

**Sufficient statistics precomputation (lines 342-366):**
- Generated via Monte Carlo with N=500,000 samples per topology/K pair
- Stores: `p_A` (label prior), `E_T`, `E_T²`, `E_Y`, `E_TY`, `E_TD`, `E_YD` (moment vectors)
- For IV: stores `RF` (reduced form) and `FS` (first-stage) vectors

---

### 3. **Empirical Confusion Matrices Location**

**Does NOT exist** at `dream_reports/empirical_confusion_matrices.json`

**Actual locations:**
- **Primary source**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json`
  - Contains 23 empirical K×K confusion matrices (8 VAST K=3, plus VAST/CivilComments K=2, plus HumAID K=10)
  - Structure: `confusion_matrices[key]` = column-stochastic normalized matrix
  - Also includes: biases, ASV values, F1 scores, source metadata per configuration

- **Frontier source** (intermediate): `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_cms.json`
  - Contains frontier extraction results (VAST + CivilComments)

- **Plan006 historical**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan006/asv_empirical_results.json`
  - Contains HumAID K=10 matrices and their comprehensive analysis

---

### 4. **Existing `c_estimation_robustness.py` Analysis**

The file **does exist** and is fully implemented at `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness.py`.

**What it does (lines 1-24):**
- Tests robustness of the "safe vs. fragile" topology partition under finite-sample estimation of C
- Draws B=200 multinomial bootstrap replicates of Ĉ for each n_gold ∈ {50, 100, 200, 500}
- For each bootstrap sample, recomputes magnitude ASV for all 7 topologies
- Reports:
  1. **Partition stability rate**: Fraction of bootstraps where bottom-2 ASV topologies = {exposure, IV} (canonical fragile set)
  2. **Spearman ρ rank correlation**: Between bootstrap ASV ranking and true C ranking
  3. Per-source-matrix stability across bootstrap replicates

**Key functions:**
- `load_k3_matrices()` (lines 58-69): Loads K=3 matrices from `updated_empirical_results.json`
- `bootstrap_chats()` (lines 72-83): Multinomial bootstrap: for each class k, draw n_gold predictions from C[:, k]
- `compute_asv_for_matrices()` (lines 86-110): Batch ASV computation (reuses ranking_stability functions)
- `partition_from_asv()` (lines 113-116): Identifies bottom-2 topologies by ASV
- `spearman_versus_truth()` (lines 119-129): Robust rank correlation handling infinities

**Output structure** (in `c_estimation_robustness_results.json`):
```json
{
  "config": { "K": 3, "n_gold_grid": [50, 100, 200, 500], "B_bootstrap": 200, ... },
  "source_matrices": { "vast_deepseek_few-shot-3": { "C": [...], "truth_asv": {...}, ...}, ... },
  "results_per_n_gold": {
    "50": { "partition_stability_rate_vs_canonical": 0.XX, "spearman_rho_mean": 0.XX, ... },
    "100": { ... }, ...
  }
}
```

---

### **File Paths Summary:**

1. **Ranking stability + ASV computation**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ranking_stability.py`
2. **Bias plim core functions**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py` (lines 369-420)
3. **Empirical confusion matrices**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json`
4. **C estimation robustness**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness.py`
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "6d65f20b-d318-436d-9c14-efe89135e4b7",
  "tool_use_result": {
    "status": "completed",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/, I need to understand:\n\n1. How ASV (magnitude) is computed in `ranking_stability.py` — find the function `compute_asv_magnitude` or similar, and show the full implementation.\n2. How bias plim is computed for the 7 topologies (confounding, mediation, collider, frontdoor, mbias, exposure, IV). Search for bias computation functions across all .py files in artifacts/.\n3. Check if `dream_reports/empirical_confusion_matrices.json` exists, and if not, find any JSON file containing empirical confusion matrices.\n4. Look at any existing `c_estimation_robustness.py` to understand what's already been done.\n\nSearch breadth: very thorough. Show full function bodies for the key functions.",
    "agentId": "a8b9c307d53e36cc9",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Now I have all the information needed. Let me provide a comprehensive report.\n\n## Summary of Findings\n\nBased on my thorough search of the artifacts directory, here are the answers to your four questions:\n\n---\n\n### 1. **ASV (Magnitude) Computation in `ranking_stability.py`**\n\nThe ASV (Annotated Sensitivity Value) magnitude is computed through **vectorized batch processing** across three topologies. There's no single `compute_asv_magnitude` function, but rather three topology-specific batch processors that all implement the same magnitude ASV algorithm:\n\n**Core Algorithm (used by all three functions):**\n```python\n# Lines 381-390 from ranking_stability.py (IV case, same logic for others)\n# Compute running max envelope of absolute bias along delta dimension\nenvelope = np.fmax.accumulate(np.nan_to_num(bias_abs, nan=0.0), axis=0)\n# Find first delta where envelope exceeds threshold\ncrossed = envelope > ASV_EPSILON  # ASV_EPSILON = 0.05 (10% of tau=0.5)\nany_crossed = crossed.any(axis=0)\nfirst_idx = crossed.argmax(axis=0)\nasv_vals = np.where(any_crossed, DELTAS[first_idx], np.inf)\n```\n\n**The three batch processors are:**\n\n1. **`process_batch_iv()`** (lines 354-392): For IV topology\n   - Computes first-stage `FS(delta) = (1-d)*FS_true + d*FS_empirical`\n   - Calculates tau as `tau = RF / FS[1]` for each delta\n   - Returns ASV as first delta crossing the threshold, or inf if never crossed\n\n2. **`process_batch_exposure()`** (lines 395-449): For exposure topology (no treatment T)\n   - Constructs K×K moment matrix EZZ and solves for reduced-form coefficients\n   - Extracts tau from coefficient[1]\n   - Also computes monotonicity violations (non-decreasing check)\n\n3. **`process_batch_with_T()`** (lines 452-516): For confounding, mediation, collider, mbias, frontdoor\n   - Constructs (K+1)×(K+1) moment matrix with treatment T included\n   - Extracts tau from coefficient[1]\n   - Handles both non-decreasing (confounding, mediation, exposure, frontdoor, iv) and non-increasing (collider, mbias) topologies\n\n**Key Configuration:**\n- `ASV_EPSILON = 0.05` (threshold: 10% of tau_true)\n- `DELTAS = np.arange(0, 1.0 + 0.005/2, 0.005)` — 201 delta points\n- Protective topologies (collider, mbias) always assigned `ASV = inf` (immune to annotation error)\n\n---\n\n### 2. **Bias Plim Computation for 7 Topologies**\n\nBias computation is centralized in **`plan_006_asv_empirical.py`** and uses **`compute_plim()`** (lines 369-412) as the core function. This is the authoritative implementation used across experiments.\n\n**Core bias computation flow (in `compute_updated_empirical.py`, lines 212-266):**\n\n```python\nfor topo in TOPOLOGIES:  # 7 topologies: confounding, mediation, collider, exposure, mbias, iv, frontdoor\n    plim_C = plan_006.compute_plim(C, st, K)  # C = empirical confusion matrix\n    tau_biased = plan_006.extract_tau(plim_C, topo)\n    tau_true = tau_true_cache[(K, topo)]  # from identity matrix C=I\n    bias = tau_biased - tau_true\n    bias_pct = abs(bias / tau_true)\n    sign_flip = np.sign(tau_biased) != np.sign(tau_true)\n```\n\n**`compute_plim()` implementation for each topology (lines 369-412):**\n\n- **IV**: Returns `RF / FS_star[1]` where FS_star = C @ FS vector\n- **Exposure**: Solves K×K system: `EZZ @ coefs = EZY` (no T term)\n  - EZZ[0,0]=1, EZZ[0,j]=q[j], EZZ[j,j]=q[j]\n  - Returns full coefficient vector (tau at index 1)\n- **Other 5 topologies** (confounding, mediation, collider, mbias, frontdoor): Solve (K+1)×(K+1) system\n  - EZZ includes full treatment T covariance structure\n  - `EZZ[1,1] = E[T²]`, `EZZ[0,1] = E[T]`, etc.\n  - Returns coefficient vector (tau at index 1)\n\n**Sufficient statistics precomputation (lines 342-366):**\n- Generated via Monte Carlo with N=500,000 samples per topology/K pair\n- Stores: `p_A` (label prior), `E_T`, `E_T²`, `E_Y`, `E_TY`, `E_TD`, `E_YD` (moment vectors)\n- For IV: stores `RF` (reduced form) and `FS` (first-stage) vectors\n\n---\n\n### 3. **Empirical Confusion Matrices Location**\n\n**Does NOT exist** at `dream_reports/empirical_confusion_matrices.json`\n\n**Actual locations:**\n- **Primary source**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json`\n  - Contains 23 empirical K×K confusion matrices (8 VAST K=3, plus VAST/CivilComments K=2, plus HumAID K=10)\n  - Structure: `confusion_matrices[key]` = column-stochastic normalized matrix\n  - Also includes: biases, ASV values, F1 scores, source metadata per configuration\n\n- **Frontier source** (intermediate): `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan011_frontier_cms.json`\n  - Contains frontier extraction results (VAST + CivilComments)\n\n- **Plan006 historical**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan006/asv_empirical_results.json`\n  - Contains HumAID K=10 matrices and their comprehensive analysis\n\n---\n\n### 4. **Existing `c_estimation_robustness.py` Analysis**\n\nThe file **does exist** and is fully implemented at `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness.py`.\n\n**What it does (lines 1-24):**\n- Tests robustness of the \"safe vs. fragile\" topology partition under finite-sample estimation of C\n- Draws B=200 multinomial bootstrap replicates of Ĉ for each n_gold ∈ {50, 100, 200, 500}\n- For each bootstrap sample, recomputes magnitude ASV for all 7 topologies\n- Reports:\n  1. **Partition stability rate**: Fraction of bootstraps where bottom-2 ASV topologies = {exposure, IV} (canonical fragile set)\n  2. **Spearman ρ rank correlation**: Between bootstrap ASV ranking and true C ranking\n  3. Per-source-matrix stability across bootstrap replicates\n\n**Key functions:**\n- `load_k3_matrices()` (lines 58-69): Loads K=3 matrices from `updated_empirical_results.json`\n- `bootstrap_chats()` (lines 72-83): Multinomial bootstrap: for each class k, draw n_gold predictions from C[:, k]\n- `compute_asv_for_matrices()` (lines 86-110): Batch ASV computation (reuses ranking_stability functions)\n- `partition_from_asv()` (lines 113-116): Identifies bottom-2 topologies by ASV\n- `spearman_versus_truth()` (lines 119-129): Robust rank correlation handling infinities\n\n**Output structure** (in `c_estimation_robustness_results.json`):\n```json\n{\n  \"config\": { \"K\": 3, \"n_gold_grid\": [50, 100, 200, 500], \"B_bootstrap\": 200, ... },\n  \"source_matrices\": { \"vast_deepseek_few-shot-3\": { \"C\": [...], \"truth_asv\": {...}, ...}, ... },\n  \"results_per_n_gold\": {\n    \"50\": { \"partition_stability_rate_vs_canonical\": 0.XX, \"spearman_rho_mean\": 0.XX, ... },\n    \"100\": { ... }, ...\n  }\n}\n```\n\n---\n\n### **File Paths Summary:**\n\n1. **Ranking stability + ASV computation**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/ranking_stability.py`\n2. **Bias plim core functions**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py` (lines 369-420)\n3. **Empirical confusion matrices**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json`\n4. **C estimation robustness**: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness.py`"
      }
    ],
    "totalDurationMs": 74478,
    "totalTokens": 75323,
    "totalToolUseCount": 23,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2081,
      "cache_read_input_tokens": 70791,
      "output_tokens": 2450,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2081
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2450,
          "cache_read_input_tokens": 70791,
          "cache_creation_input_tokens": 2081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2081,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 6,
      "searchCount": 4,
      "bashCount": 13,
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

_source line 78_

<details><summary>Logged reasoning block</summary>

```text
The existing `c_estimation_robustness.py` already exists and is fully implemented. Let me read it and the results JSON to understand what's already been done, then check if it needs to be run or modified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "a388c99d-12d4-46e0-b20d-040fe4eb5a6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Adke9yHNvpD8fcttq5w23j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2780,
      "cache_read_input_tokens": 25094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2780
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

_source line 79_

The script and results already exist. Let me check the current state of both files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "8c685ddf-cf4e-4b8d-a771-98add04ce608",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Adke9yHNvpD8fcttq5w23j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2780,
      "cache_read_input_tokens": 25094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2780
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

_source line 80_

<details open><summary>🔧 Tool call — Read · `toolu_01YNpeek2uUDCy3DnNBBnnmB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "a9dfea9c-3ab3-4119-ad0b-44f5827629b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Adke9yHNvpD8fcttq5w23j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2780,
      "cache_read_input_tokens": 25094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2780
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

_source line 81 · 2026-05-23T14:57:15.446Z_

<details><summary>↩ Tool result · `toolu_01YNpeek2uUDCy3DnNBBnnmB`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Ĉ Estimation Robustness Experiment.
4	
5	Question: With a finite K-class gold-labelled set used to estimate C, does
6	the safe/fragile topology partition (5 vs 2) hold under multinomial bootstrap
7	of Ĉ?
8	
9	For each empirical column-stochastic K=3 confusion matrix C (LLM truth),
10	draw B bootstrap replicates Ĉ ~ multinomial(C[:,k] · n_gold) / n_gold for
11	each class k. For each Ĉ, recompute the magnitude ASV δ* for the 7
12	topologies (confounding, mediation, collider, exposure, mbias, IV,
13	frontdoor) and report:
14	
15	  • Partition stability rate vs n_gold: fraction of bootstraps where the
16	    two lowest-ASV topologies equal {exposure, IV}.
17	  • Spearman ρ vs n_gold: rank correlation between ASV ranking from Ĉ and
18	    from true C (averaged over bootstraps and source matrices).
19	
20	Empirical Cs come from artifacts/updated_empirical_results.json (23 LLM
21	matrices; 8 are K=3 vast/stance — the K=3 framework subset).
22	
23	Output: c_estimation_robustness_results.json next to this script.
24	"""
25	
26	import json
27	import os
28	import sys
29	import time
30	from collections import defaultdict
31	
32	import numpy as np
33	from scipy.stats import rankdata, spearmanr
34	
35	sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
36	
37	from ranking_stability import (  # noqa: E402
38	    ALL_TOPOS, COMPUTE_SS, DGP_PARAMS, K, N_DELTA, DELTAS, ASV_EPSILON,
39	    PROTECTIVE, get_tau_true, process_batch_iv, process_batch_exposure,
40	    process_batch_with_T,
41	)
42	
43	# ──────────────────────────────────────────────────────────────────────────
44	EMP_PATH = '/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json'
45	OUT_DIR = os.path.dirname(os.path.abspath(__file__))
46	OUT_PATH = os.path.join(OUT_DIR, 'c_estimation_robustness_results.json')
47	
48	N_GOLD_GRID = [50, 100, 200, 500]
49	B_BOOT = 200
50	SEED = 20260523
51	SAFE = {'confounding', 'mediation', 'collider', 'frontdoor', 'mbias'}
52	FRAGILE = {'exposure', 'iv'}
53	RANK_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
54	              'mbias', 'iv', 'frontdoor']
55	TOPO_IDX = {t: i for i, t in enumerate(RANK_TOPOS)}
56	
57	
58	def load_k3_matrices():
59	    with open(EMP_PATH) as f:
60	        d = json.load(f)
61	    out = {}
62	    for name, cm in d['confusion_matrices'].items():
63	        arr = np.asarray(cm, dtype=float)
64	        if arr.shape == (K, K):
65	            # Re-normalise columns just in case
66	            cs = arr.sum(axis=0, keepdims=True)
67	            cs = np.where(cs < 1e-12, 1.0, cs)
68	            out[name] = arr / cs
69	    return out
70	
71	
72	def bootstrap_chats(C_true, n_gold, B, rng):
73	    """Multinomial bootstrap of Ĉ.
74	
75	    For each class k, draw n_gold predictions from C_true[:, k] then
76	    normalise. Returns (B, K, K) array of column-stochastic matrices.
77	    """
78	    out = np.empty((B, K, K))
79	    for k in range(K):
80	        # rng.multinomial returns (B, K) with each row summing to n_gold
81	        counts = rng.multinomial(n_gold, C_true[:, k], size=B)
82	        out[:, :, k] = counts / float(n_gold)
83	    return out
84	
85	
86	def compute_asv_for_matrices(C0_batch, all_ss, all_tau_true):
87	    """Compute magnitude ASV per topology for a batch of C0 matrices.
88	
89	    Returns asv: (M, n_topo) ndarray. Collider/M-bias get +inf (protective).
90	    """
91	    M = C0_batch.shape[0]
92	    n_topo = len(RANK_TOPOS)
93	    asv = np.full((M, n_topo), np.nan)
94	    # Protective topologies: always inf
95	    asv[:, TOPO_IDX['collider']] = np.inf
96	    asv[:, TOPO_IDX['mbias']] = np.inf
97	
98	    for topo in RANK_TOPOS:
99	        if topo in PROTECTIVE:
100	            continue
101	        ss = all_ss[topo]
102	        tau_true = all_tau_true[topo]
103	        if topo == 'iv':
104	            vals = process_batch_iv(C0_batch, ss, tau_true)
105	        elif topo == 'exposure':
106	            vals, _ = process_batch_exposure(C0_batch, ss, tau_true)
107	        else:
108	            vals, _ = process_batch_with_T(C0_batch, ss, tau_true, topo)
109	        asv[:, TOPO_IDX[topo]] = vals
110	    return asv
111	
112	
113	def partition_from_asv(asv_row):
114	    """Bottom-2 topologies (smallest ASV) form the fragile set."""
115	    order = np.argsort(asv_row, kind='stable')
116	    return frozenset(RANK_TOPOS[i] for i in order[:2])
117	
118	
119	def spearman_versus_truth(asv_boot, asv_true):
120	    """Spearman rho between bootstrap ASV ranking and truth ranking."""
121	    # Handle infinities: replace +inf with large finite via rank ordering.
122	    # scipy.spearmanr is OK with finite inputs; rankdata handles infinities.
123	    r_true = rankdata(asv_true)
124	    r_boot = rankdata(asv_boot)
125	    # If all values are identical (or all inf), correlation undefined → NaN
126	    if np.all(r_true == r_true[0]) or np.all(r_boot == r_boot[0]):
127	        return np.nan
128	    rho, _ = spearmanr(r_true, r_boot)
129	    return rho
130	
131	
132	def main():
133	    t_total = time.time()
134	    print('Ĉ Estimation Robustness Experiment')
135	    print(f'  K={K}, B={B_BOOT}, n_gold ∈ {N_GOLD_GRID}')
136	    print(f'  Topologies: {RANK_TOPOS}')
137	    print(f'  ASV threshold (magnitude): {ASV_EPSILON}')
138	    print(f'  n_delta = {N_DELTA}')
139	    print('=' * 70)
140	    sys.stdout.flush()
141	
142	    # Precompute analytic sufficient statistics + tau_true
143	    print('\nPrecomputing sufficient statistics & tau_true...')
144	    all_ss = {}
145	    all_tau_true = {}
146	    for topo in ALL_TOPOS:
147	        ss = COMPUTE_SS[topo](DGP_PARAMS[topo])
148	        all_ss[topo] = ss
149	        all_tau_true[topo] = get_tau_true(topo, ss)
150	        print(f'  {topo:<12} tau_true = {all_tau_true[topo]:.6f}')
151	    sys.stdout.flush()
152	
153	    # Load empirical K=3 matrices
154	    print('\nLoading empirical K=3 confusion matrices...')
155	    Cs = load_k3_matrices()
156	    print(f'  Loaded {len(Cs)} K=3 matrices')
157	    for name in Cs:
158	        print(f'    {name}  diag={np.diag(Cs[name]).round(3).tolist()}')
159	    sys.stdout.flush()
160	
161	    # Truth ASV per source C
162	    print('\nComputing ASV for the truth Cs...')
163	    truth_C_batch = np.stack(list(Cs.values()))
164	    truth_asv = compute_asv_for_matrices(truth_C_batch, all_ss, all_tau_true)
165	    truth_partition = {}
166	    truth_asv_dict = {}
167	    for i, name in enumerate(Cs):
168	        truth_partition[name] = partition_from_asv(truth_asv[i])
169	        truth_asv_dict[name] = {
170	            RANK_TOPOS[j]: (None if np.isinf(truth_asv[i, j])
171	                            else float(truth_asv[i, j]))
172	            for j in range(len(RANK_TOPOS))
173	        }
174	        eq = 'YES' if truth_partition[name] == FRAGILE else 'NO'
175	        print(f'  {name}  fragile-set={sorted(truth_partition[name])}  '
176	              f'matches canonical: {eq}')
177	    sys.stdout.flush()
178	
179	    # Bootstrap loop
180	    print(f'\nBootstrapping (B={B_BOOT})...')
181	    rng = np.random.default_rng(SEED)
182	
183	    results_per_n = {}
184	    for n_gold in N_GOLD_GRID:
185	        t0 = time.time()
186	        partition_match_total = 0   # vs canonical {exposure,iv}
187	        partition_match_truth = 0   # vs source-C truth partition
188	        n_bootstraps_total = 0
189	        rho_values_vs_truth = []
190	        rho_values_vs_theoretical_safe = []
191	
192	        # Per-source-C aggregates
193	        per_C = {}
194	
195	        for name, C_true in Cs.items():
196	            boot = bootstrap_chats(C_true, n_gold, B_BOOT, rng)
197	            asv_boot = compute_asv_for_matrices(
198	                boot, all_ss, all_tau_true)  # (B, n_topo)
199	
200	            truth_row = truth_asv[list(Cs).index(name)]
201	
202	            n_match_canon = 0
203	            n_match_truth = 0
204	            rho_vs_truth = []
205	            for b in range(B_BOOT):
206	                part = partition_from_asv(asv_boot[b])
207	                if part == FRAGILE:
208	                    n_match_canon += 1
209	                if part == truth_partition[name]:
210	                    n_match_truth += 1
211	                rho_vs_truth.append(
212	                    spearman_versus_truth(asv_boot[b], truth_row))
213	
214	            rho_vs_truth = np.array(rho_vs_truth, dtype=float)
215	            rho_clean = rho_vs_truth[~np.isnan(rho_vs_truth)]
216	
217	            per_C[name] = {
218	                'partition_match_canonical': n_match_canon / B_BOOT,
219	                'partition_match_truth_C': n_match_truth / B_BOOT,
220	                'spearman_rho_mean_vs_truth':
221	                    float(rho_clean.mean()) if rho_clean.size else float('nan'),
222	                'spearman_rho_median_vs_truth':
223	                    float(np.median(rho_clean)) if rho_clean.size else float('nan'),
224	                'spearman_rho_q25_vs_truth':
225	                    float(np.quantile(rho_clean, 0.25)) if rho_clean.size else float('nan'),
226	                'truth_partition_matches_canonical':
227	                    truth_partition[name] == FRAGILE,
228	            }
229	
230	            partition_match_total += n_match_canon
231	            partition_match_truth += n_match_truth
232	            n_bootstraps_total += B_BOOT
233	            rho_values_vs_truth.extend(rho_clean.tolist())
234	
235	        results_per_n[n_gold] = {
236	            'n_bootstraps_total': n_bootstraps_total,
237	            'partition_stability_rate_vs_canonical':
238	                partition_match_total / n_bootstraps_total,
239	            'partition_stability_rate_vs_truth_C':
240	                partition_match_truth / n_bootstraps_total,
241	            'spearman_rho_mean':
242	                float(np.mean(rho_values_vs_truth)) if rho_values_vs_truth
243	                else float('nan'),
244	            'spearman_rho_median':
245	                float(np.median(rho_values_vs_truth)) if rho_values_vs_truth
246	                else float('nan'),
247	            'spearman_rho_q25':
248	                float(np.quantile(rho_values_vs_truth, 0.25))
249	                if rho_values_vs_truth else float('nan'),
250	            'spearman_rho_q75':
251	                float(np.quantile(rho_values_vs_truth, 0.75))
252	                if rho_values_vs_truth else float('nan'),
253	            'per_source_C': per_C,
254	        }
255	        elapsed = time.time() - t0
256	        r = results_per_n[n_gold]
257	        print(f'  n_gold={n_gold:<4}  '
258	              f'partition_rate_canonical={r["partition_stability_rate_vs_canonical"]:.4f}  '
259	              f'partition_rate_truth={r["partition_stability_rate_vs_truth_C"]:.4f}  '
260	              f'rho_mean={r["spearman_rho_mean"]:.4f}  '
261	              f'({elapsed:.1f}s)')
262	        sys.stdout.flush()
263	
264	    # Summary
265	    print('\n' + '=' * 70)
266	    print('Summary')
267	    print('=' * 70)
268	    print(f'{"n_gold":<8}{"part_canon":<14}{"part_truth":<14}'
269	          f'{"rho_mean":<12}{"rho_median":<12}')
270	    for n_gold in N_GOLD_GRID:
271	        r = results_per_n[n_gold]
272	        print(f'{n_gold:<8}'
273	              f'{r["partition_stability_rate_vs_canonical"]:<14.4f}'
274	              f'{r["partition_stability_rate_vs_truth_C"]:<14.4f}'
275	              f'{r["spearman_rho_mean"]:<12.4f}'
276	              f'{r["spearman_rho_median"]:<12.4f}')
277	
278	    # Save
279	    total_time = time.time() - t_total
280	    out = {
281	        'description': ('Ĉ estimation robustness under multinomial bootstrap'
282	                        ' from finite gold set'),
283	        'config': {
284	            'K': K,
285	            'n_gold_grid': N_GOLD_GRID,
286	            'B_bootstrap': B_BOOT,
287	            'seed': SEED,
288	            'asv_threshold': ASV_EPSILON,
289	            'n_delta': N_DELTA,
290	            'topologies': RANK_TOPOS,
291	            'canonical_safe': sorted(SAFE),
292	            'canonical_fragile': sorted(FRAGILE),
293	            'empirical_path': EMP_PATH,
294	        },
295	        'source_matrices': {
296	            name: {
297	                'C': Cs[name].tolist(),
298	                'diag': np.diag(Cs[name]).tolist(),
299	                'truth_asv': truth_asv_dict[name],
300	                'truth_fragile_set': sorted(truth_partition[name]),
301	                'truth_matches_canonical':
302	                    truth_partition[name] == FRAGILE,
303	            }
304	            for name in Cs
305	        },
306	        'results_per_n_gold': {
307	            str(n): results_per_n[n] for n in N_GOLD_GRID
308	        },
309	        'total_time_seconds': total_time,
310	    }
311	    with open(OUT_PATH, 'w') as f:
312	        json.dump(out, f, indent=2)
313	    print(f'\nJSON saved: {OUT_PATH}')
314	    print(f'Total: {total_time:.1f}s')
315	
316	
317	if __name__ == '__main__':
318	    main()
319	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "05ff957c-6bf5-40db-8e25-26266bbad73d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nĈ Estimation Robustness Experiment.\n\nQuestion: With a finite K-class gold-labelled set used to estimate C, does\nthe safe/fragile topology partition (5 vs 2) hold under multinomial bootstrap\nof Ĉ?\n\nFor each empirical column-stochastic K=3 confusion matrix C (LLM truth),\ndraw B bootstrap replicates Ĉ ~ multinomial(C[:,k] · n_gold) / n_gold for\neach class k. For each Ĉ, recompute the magnitude ASV δ* for the 7\ntopologies (confounding, mediation, collider, exposure, mbias, IV,\nfrontdoor) and report:\n\n  • Partition stability rate vs n_gold: fraction of bootstraps where the\n    two lowest-ASV topologies equal {exposure, IV}.\n  • Spearman ρ vs n_gold: rank correlation between ASV ranking from Ĉ and\n    from true C (averaged over bootstraps and source matrices).\n\nEmpirical Cs come from artifacts/updated_empirical_results.json (23 LLM\nmatrices; 8 are K=3 vast/stance — the K=3 framework subset).\n\nOutput: c_estimation_robustness_results.json next to this script.\n\"\"\"\n\nimport json\nimport os\nimport sys\nimport time\nfrom collections import defaultdict\n\nimport numpy as np\nfrom scipy.stats import rankdata, spearmanr\n\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\n\nfrom ranking_stability import (  # noqa: E402\n    ALL_TOPOS, COMPUTE_SS, DGP_PARAMS, K, N_DELTA, DELTAS, ASV_EPSILON,\n    PROTECTIVE, get_tau_true, process_batch_iv, process_batch_exposure,\n    process_batch_with_T,\n)\n\n# ──────────────────────────────────────────────────────────────────────────\nEMP_PATH = '/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json'\nOUT_DIR = os.path.dirname(os.path.abspath(__file__))\nOUT_PATH = os.path.join(OUT_DIR, 'c_estimation_robustness_results.json')\n\nN_GOLD_GRID = [50, 100, 200, 500]\nB_BOOT = 200\nSEED = 20260523\nSAFE = {'confounding', 'mediation', 'collider', 'frontdoor', 'mbias'}\nFRAGILE = {'exposure', 'iv'}\nRANK_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',\n              'mbias', 'iv', 'frontdoor']\nTOPO_IDX = {t: i for i, t in enumerate(RANK_TOPOS)}\n\n\ndef load_k3_matrices():\n    with open(EMP_PATH) as f:\n        d = json.load(f)\n    out = {}\n    for name, cm in d['confusion_matrices'].items():\n        arr = np.asarray(cm, dtype=float)\n        if arr.shape == (K, K):\n            # Re-normalise columns just in case\n            cs = arr.sum(axis=0, keepdims=True)\n            cs = np.where(cs < 1e-12, 1.0, cs)\n            out[name] = arr / cs\n    return out\n\n\ndef bootstrap_chats(C_true, n_gold, B, rng):\n    \"\"\"Multinomial bootstrap of Ĉ.\n\n    For each class k, draw n_gold predictions from C_true[:, k] then\n    normalise. Returns (B, K, K) array of column-stochastic matrices.\n    \"\"\"\n    out = np.empty((B, K, K))\n    for k in range(K):\n        # rng.multinomial returns (B, K) with each row summing to n_gold\n        counts = rng.multinomial(n_gold, C_true[:, k], size=B)\n        out[:, :, k] = counts / float(n_gold)\n    return out\n\n\ndef compute_asv_for_matrices(C0_batch, all_ss, all_tau_true):\n    \"\"\"Compute magnitude ASV per topology for a batch of C0 matrices.\n\n    Returns asv: (M, n_topo) ndarray. Collider/M-bias get +inf (protective).\n    \"\"\"\n    M = C0_batch.shape[0]\n    n_topo = len(RANK_TOPOS)\n    asv = np.full((M, n_topo), np.nan)\n    # Protective topologies: always inf\n    asv[:, TOPO_IDX['collider']] = np.inf\n    asv[:, TOPO_IDX['mbias']] = np.inf\n\n    for topo in RANK_TOPOS:\n        if topo in PROTECTIVE:\n            continue\n        ss = all_ss[topo]\n        tau_true = all_tau_true[topo]\n        if topo == 'iv':\n            vals = process_batch_iv(C0_batch, ss, tau_true)\n        elif topo == 'exposure':\n            vals, _ = process_batch_exposure(C0_batch, ss, tau_true)\n        else:\n            vals, _ = process_batch_with_T(C0_batch, ss, tau_true, topo)\n        asv[:, TOPO_IDX[topo]] = vals\n    return asv\n\n\ndef partition_from_asv(asv_row):\n    \"\"\"Bottom-2 topologies (smallest ASV) form the fragile set.\"\"\"\n    order = np.argsort(asv_row, kind='stable')\n    return frozenset(RANK_TOPOS[i] for i in order[:2])\n\n\ndef spearman_versus_truth(asv_boot, asv_true):\n    \"\"\"Spearman rho between bootstrap ASV ranking and truth ranking.\"\"\"\n    # Handle infinities: replace +inf with large finite via rank ordering.\n    # scipy.spearmanr is OK with finite inputs; rankdata handles infinities.\n    r_true = rankdata(asv_true)\n    r_boot = rankdata(asv_boot)\n    # If all values are identical (or all inf), correlation undefined → NaN\n    if np.all(r_true == r_true[0]) or np.all(r_boot == r_boot[0]):\n        return np.nan\n    rho, _ = spearmanr(r_true, r_boot)\n    return rho\n\n\ndef main():\n    t_total = time.time()\n    print('Ĉ Estimation Robustness Experiment')\n    print(f'  K={K}, B={B_BOOT}, n_gold ∈ {N_GOLD_GRID}')\n    print(f'  Topologies: {RANK_TOPOS}')\n    print(f'  ASV threshold (magnitude): {ASV_EPSILON}')\n    print(f'  n_delta = {N_DELTA}')\n    print('=' * 70)\n    sys.stdout.flush()\n\n    # Precompute analytic sufficient statistics + tau_true\n    print('\\nPrecomputing sufficient statistics & tau_true...')\n    all_ss = {}\n    all_tau_true = {}\n    for topo in ALL_TOPOS:\n        ss = COMPUTE_SS[topo](DGP_PARAMS[topo])\n        all_ss[topo] = ss\n        all_tau_true[topo] = get_tau_true(topo, ss)\n        print(f'  {topo:<12} tau_true = {all_tau_true[topo]:.6f}')\n    sys.stdout.flush()\n\n    # Load empirical K=3 matrices\n    print('\\nLoading empirical K=3 confusion matrices...')\n    Cs = load_k3_matrices()\n    print(f'  Loaded {len(Cs)} K=3 matrices')\n    for name in Cs:\n        print(f'    {name}  diag={np.diag(Cs[name]).round(3).tolist()}')\n    sys.stdout.flush()\n\n    # Truth ASV per source C\n    print('\\nComputing ASV for the truth Cs...')\n    truth_C_batch = np.stack(list(Cs.values()))\n    truth_asv = compute_asv_for_matrices(truth_C_batch, all_ss, all_tau_true)\n    truth_partition = {}\n    truth_asv_dict = {}\n    for i, name in enumerate(Cs):\n        truth_partition[name] = partition_from_asv(truth_asv[i])\n        truth_asv_dict[name] = {\n            RANK_TOPOS[j]: (None if np.isinf(truth_asv[i, j])\n                            else float(truth_asv[i, j]))\n            for j in range(len(RANK_TOPOS))\n        }\n        eq = 'YES' if truth_partition[name] == FRAGILE else 'NO'\n        print(f'  {name}  fragile-set={sorted(truth_partition[name])}  '\n              f'matches canonical: {eq}')\n    sys.stdout.flush()\n\n    # Bootstrap loop\n    print(f'\\nBootstrapping (B={B_BOOT})...')\n    rng = np.random.default_rng(SEED)\n\n    results_per_n = {}\n    for n_gold in N_GOLD_GRID:\n        t0 = time.time()\n        partition_match_total = 0   # vs canonical {exposure,iv}\n        partition_match_truth = 0   # vs source-C truth partition\n        n_bootstraps_total = 0\n        rho_values_vs_truth = []\n        rho_values_vs_theoretical_safe = []\n\n        # Per-source-C aggregates\n        per_C = {}\n\n        for name, C_true in Cs.items():\n            boot = bootstrap_chats(C_true, n_gold, B_BOOT, rng)\n            asv_boot = compute_asv_for_matrices(\n                boot, all_ss, all_tau_true)  # (B, n_topo)\n\n            truth_row = truth_asv[list(Cs).index(name)]\n\n            n_match_canon = 0\n            n_match_truth = 0\n            rho_vs_truth = []\n            for b in range(B_BOOT):\n                part = partition_from_asv(asv_boot[b])\n                if part == FRAGILE:\n                    n_match_canon += 1\n                if part == truth_partition[name]:\n                    n_match_truth += 1\n                rho_vs_truth.append(\n                    spearman_versus_truth(asv_boot[b], truth_row))\n\n            rho_vs_truth = np.array(rho_vs_truth, dtype=float)\n            rho_clean = rho_vs_truth[~np.isnan(rho_vs_truth)]\n\n            per_C[name] = {\n                'partition_match_canonical': n_match_canon / B_BOOT,\n                'partition_match_truth_C': n_match_truth / B_BOOT,\n                'spearman_rho_mean_vs_truth':\n                    float(rho_clean.mean()) if rho_clean.size else float('nan'),\n                'spearman_rho_median_vs_truth':\n                    float(np.median(rho_clean)) if rho_clean.size else float('nan'),\n                'spearman_rho_q25_vs_truth':\n                    float(np.quantile(rho_clean, 0.25)) if rho_clean.size else float('nan'),\n                'truth_partition_matches_canonical':\n                    truth_partition[name] == FRAGILE,\n            }\n\n            partition_match_total += n_match_canon\n            partition_match_truth += n_match_truth\n            n_bootstraps_total += B_BOOT\n            rho_values_vs_truth.extend(rho_clean.tolist())\n\n        results_per_n[n_gold] = {\n            'n_bootstraps_total': n_bootstraps_total,\n            'partition_stability_rate_vs_canonical':\n                partition_match_total / n_bootstraps_total,\n            'partition_stability_rate_vs_truth_C':\n                partition_match_truth / n_bootstraps_total,\n            'spearman_rho_mean':\n                float(np.mean(rho_values_vs_truth)) if rho_values_vs_truth\n                else float('nan'),\n            'spearman_rho_median':\n                float(np.median(rho_values_vs_truth)) if rho_values_vs_truth\n                else float('nan'),\n            'spearman_rho_q25':\n                float(np.quantile(rho_values_vs_truth, 0.25))\n                if rho_values_vs_truth else float('nan'),\n            'spearman_rho_q75':\n                float(np.quantile(rho_values_vs_truth, 0.75))\n                if rho_values_vs_truth else float('nan'),\n            'per_source_C': per_C,\n        }\n        elapsed = time.time() - t0\n        r = results_per_n[n_gold]\n        print(f'  n_gold={n_gold:<4}  '\n              f'partition_rate_canonical={r[\"partition_stability_rate_vs_canonical\"]:.4f}  '\n              f'partition_rate_truth={r[\"partition_stability_rate_vs_truth_C\"]:.4f}  '\n              f'rho_mean={r[\"spearman_rho_mean\"]:.4f}  '\n              f'({elapsed:.1f}s)')\n        sys.stdout.flush()\n\n    # Summary\n    print('\\n' + '=' * 70)\n    print('Summary')\n    print('=' * 70)\n    print(f'{\"n_gold\":<8}{\"part_canon\":<14}{\"part_truth\":<14}'\n          f'{\"rho_mean\":<12}{\"rho_median\":<12}')\n    for n_gold in N_GOLD_GRID:\n        r = results_per_n[n_gold]\n        print(f'{n_gold:<8}'\n              f'{r[\"partition_stability_rate_vs_canonical\"]:<14.4f}'\n              f'{r[\"partition_stability_rate_vs_truth_C\"]:<14.4f}'\n              f'{r[\"spearman_rho_mean\"]:<12.4f}'\n              f'{r[\"spearman_rho_median\"]:<12.4f}')\n\n    # Save\n    total_time = time.time() - t_total\n    out = {\n        'description': ('Ĉ estimation robustness under multinomial bootstrap'\n                        ' from finite gold set'),\n        'config': {\n            'K': K,\n            'n_gold_grid': N_GOLD_GRID,\n            'B_bootstrap': B_BOOT,\n            'seed': SEED,\n            'asv_threshold': ASV_EPSILON,\n            'n_delta': N_DELTA,\n            'topologies': RANK_TOPOS,\n            'canonical_safe': sorted(SAFE),\n            'canonical_fragile': sorted(FRAGILE),\n            'empirical_path': EMP_PATH,\n        },\n        'source_matrices': {\n            name: {\n                'C': Cs[name].tolist(),\n                'diag': np.diag(Cs[name]).tolist(),\n                'truth_asv': truth_asv_dict[name],\n                'truth_fragile_set': sorted(truth_partition[name]),\n                'truth_matches_canonical':\n                    truth_partition[name] == FRAGILE,\n            }\n            for name in Cs\n        },\n        'results_per_n_gold': {\n            str(n): results_per_n[n] for n in N_GOLD_GRID\n        },\n        'total_time_seconds': total_time,\n    }\n    with open(OUT_PATH, 'w') as f:\n        json.dump(out, f, indent=2)\n    print(f'\\nJSON saved: {OUT_PATH}')\n    print(f'Total: {total_time:.1f}s')\n\n\nif __name__ == '__main__':\n    main()\n",
      "numLines": 319,
      "startLine": 1,
      "totalLines": 319
    }
  }
}
```

</details>

---

### Tool call

_source line 82_

<details open><summary>🔧 Tool call — Read · `toolu_017kC5zm4JNhCaayuBbMKudr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "61099bc6-c303-46cf-954f-07d92037f497",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Adke9yHNvpD8fcttq5w23j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2780,
      "cache_read_input_tokens": 25094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2780
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

_source line 83 · 2026-05-23T14:57:15.737Z_

<details><summary>↩ Tool result · `toolu_017kC5zm4JNhCaayuBbMKudr`</summary>

```text
1	{
2	  "description": "\u0108 estimation robustness under multinomial bootstrap from finite gold set",
3	  "config": {
4	    "K": 3,
5	    "n_gold_grid": [
6	      50,
7	      100,
8	      200,
9	      500
10	    ],
11	    "B_bootstrap": 200,
12	    "seed": 20260523,
13	    "asv_threshold": 0.05,
14	    "n_delta": 201,
15	    "topologies": [
16	      "confounding",
17	      "mediation",
18	      "collider",
19	      "exposure",
20	      "mbias",
21	      "iv",
22	      "frontdoor"
23	    ],
24	    "canonical_safe": [
25	      "collider",
26	      "confounding",
27	      "frontdoor",
28	      "mbias",
29	      "mediation"
30	    ],
31	    "canonical_fragile": [
32	      "exposure",
33	      "iv"
34	    ],
35	    "empirical_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json"
36	  },
37	  "source_matrices": {
38	    "vast_deepseek_few-shot-3": {
39	      "C": [
40	        [
41	          0.5139,
42	          0.1017,
43	          0.2888
44	        ],
45	        [
46	          0.3212,
47	          0.7985,
48	          0.5498
49	        ],
50	        [
51	          0.1649,
52	          0.0998,
53	          0.1614
54	        ]
55	      ],
56	      "diag": [
57	        0.5139,
58	        0.7985,
59	        0.1614
60	      ],
61	      "truth_asv": {
62	        "confounding": 0.06,
63	        "mediation": 0.12,
64	        "collider": null,
65	        "exposure": 0.055,
66	        "mbias": null,
67	        "iv": 0.055,
68	        "frontdoor": 0.08
69	      },
70	      "truth_fragile_set": [
71	        "exposure",
72	        "iv"
73	      ],
74	      "truth_matches_canonical": true
75	    },
76	    "vast_deepseek_few-shot-5": {
77	      "C": [
78	        [
79	          0.5268,
80	          0.1149,
81	          0.3068
82	        ],
83	        [
84	          0.3105,
85	          0.7853,
86	          0.5398
87	        ],
88	        [
89	          0.1627,
90	          0.0998,
91	          0.1534
92	        ]
93	      ],
94	      "diag": [
95	        0.5268,
96	        0.7853,
97	        0.1534
98	      ],
99	      "truth_asv": {
100	        "confounding": 0.06,
101	        "mediation": 0.12,
102	        "collider": null,
103	        "exposure": 0.055,
104	        "mbias": null,
105	        "iv": 0.055,
106	        "frontdoor": 0.08
107	      },
108	      "truth_fragile_set": [
109	        "exposure",
110	        "iv"
111	      ],
112	      "truth_matches_canonical": true
113	    },
114	    "vast_llama4_few-shot-3": {
115	      "C": [
116	        [
117	          0.6595289079229122,
118	          0.1807909604519774,
119	          0.40438247011952194
120	        ],
121	        [
122	          0.31263383297644537,
123	          0.800376647834275,
124	          0.5597609561752989
125	        ],
126	        [
127	          0.027837259100642397,
128	          0.018832391713747645,
129	          0.03585657370517929
130	        ]
131	      ],
132	      "diag": [
133	        0.6595289079229122,
134	        0.800376647834275,
135	        0.03585657370517929
136	      ],
137	      "truth_asv": {
138	        "confounding": 0.065,
139	        "mediation": 0.14,
140	        "collider": null,
141	        "exposure": 0.055,
142	        "mbias": null,
143	        "iv": 0.055,
144	        "frontdoor": 0.09
145	      },
146	      "truth_fragile_set": [
147	        "exposure",
148	        "iv"
149	      ],
150	      "truth_matches_canonical": true
151	    },
152	    "vast_llama4_zero-shot": {
153	      "C": [
154	        [
155	          0.6781115879828327,
156	          0.14393939393939395,
157	          0.3964143426294821
158	        ],
159	        [
160	          0.2982832618025751,
161	          0.8409090909090909,
162	          0.5577689243027889
163	        ],
164	        [
165	          0.023605150214592276,
166	          0.015151515151515152,
167	          0.04581673306772909
168	        ]
169	      ],
170	      "diag": [
171	        0.6781115879828327,
172	        0.8409090909090909,
173	        0.04581673306772909
174	      ],
175	      "truth_asv": {
176	        "confounding": 0.07,
177	        "mediation": 0.15,
178	        "collider": null,
179	        "exposure": 0.055,
180	        "mbias": null,
181	        "iv": 0.06,
182	        "frontdoor": 0.09
183	      },
184	      "truth_fragile_set": [
185	        "exposure",
186	        "iv"
187	      ],
188	      "truth_matches_canonical": true
189	    },
190	    "vast_qwen2.5-7b_few-shot-3": {
191	      "C": [
192	        [
193	          0.4132762312633833,
194	          0.08662900188323917,
195	          0.22310756972111553
196	        ],
197	        [
198	          0.44539614561027835,
199	          0.8210922787193974,
200	          0.651394422310757
201	        ],
202	        [
203	          0.14132762312633834,
204	          0.09227871939736347,
205	          0.1254980079681275
206	        ]
207	      ],
208	      "diag": [
209	        0.4132762312633833,
210	        0.8210922787193974,
211	        0.1254980079681275
212	      ],
213	      "truth_asv": {
214	        "confounding": 0.055,
215	        "mediation": 0.11,
216	        "collider": null,
217	        "exposure": 0.045,
218	        "mbias": null,
219	        "iv": 0.05,
220	        "frontdoor": 0.075
221	      },
222	      "truth_fragile_set": [
223	        "exposure",
224	        "iv"
225	      ],
226	      "truth_matches_canonical": true
227	    },
228	    "vast_qwen2.5-7b_few-shot-5": {
229	      "C": [
230	        [
231	          0.4753747323340471,
232	          0.11111111111111112,
233	          0.2589641434262948
234	        ],
235	        [
236	          0.39186295503211993,
237	          0.7758945386064031,
238	          0.6155378486055777
239	        ],
240	        [
241	          0.13276231263383298,
242	          0.11299435028248589,
243	          0.1254980079681275
244	        ]
245	      ],
246	      "diag": [
247	        0.4753747323340471,
248	        0.7758945386064031,
249	        0.1254980079681275
250	      ],
251	      "truth_asv": {
252	        "confounding": 0.055,
253	        "mediation": 0.11,
254	        "collider": null,
255	        "exposure": 0.05,
256	        "mbias": null,
257	        "iv": 0.05,
258	        "frontdoor": 0.075
259	      },
260	      "truth_fragile_set": [
261	        "exposure",
262	        "iv"
263	      ],
264	      "truth_matches_canonical": true
265	    },
266	    "vast_qwen2.5-7b_zero-shot": {
267	      "C": [
268	        [
269	          0.4613733905579399,
270	          0.07909604519774012,
271	          0.2410358565737052
272	        ],
273	        [
274	          0.4313304721030043,
275	          0.847457627118644,
276	          0.649402390438247
277	        ],
278	        [
279	          0.1072961373390558,
280	          0.07344632768361582,
281	          0.10956175298804781
282	        ]
283	      ],
284	      "diag": [
285	        0.4613733905579399,
286	        0.847457627118644,
287	        0.10956175298804781
288	      ],
289	      "truth_asv": {
290	        "confounding": 0.055,
291	        "mediation": 0.12,
292	        "collider": null,
293	        "exposure": 0.045,
294	        "mbias": null,
295	        "iv": 0.05,
296	        "frontdoor": 0.075
297	      },
298	      "truth_fragile_set": [
299	        "exposure",
300	        "iv"
301	      ],
302	      "truth_matches_canonical": true
303	    },
304	    "vast_qwen3_zero-shot": {
305	      "C": [
306	        [
307	          0.6858974358974359,
308	          0.16666666666666666,
309	          0.40357852882703776
310	        ],
311	        [
312	          0.23504273504273504,
313	          0.7746212121212122,
314	          0.5228628230616302
315	        ],
316	        [
317	          0.07905982905982906,
318	          0.058712121212121215,
319	          0.073558648111332
320	        ]
321	      ],
322	      "diag": [
323	        0.6858974358974359,
324	        0.7746212121212122,
325	        0.073558648111332
326	      ],
327	      "truth_asv": {
328	        "confounding": 0.07,
329	        "mediation": 0.135,
330	        "collider": null,
331	        "exposure": 0.065,
332	        "mbias": null,
333	        "iv": 0.06,
334	        "frontdoor": 0.085
335	      },
336	      "truth_fragile_set": [
337	        "exposure",
338	        "iv"
339	      ],
340	      "truth_matches_canonical": true
341	    }
342	  },
343	  "results_per_n_gold": {
344	    "50": {
345	      "n_bootstraps_total": 1600,
346	      "partition_stability_rate_vs_canonical": 0.504375,
347	      "partition_stability_rate_vs_truth_C": 0.504375,
348	      "spearman_rho_mean": 0.8572827199901789,
349	      "spearman_rho_median": 0.9908673886137246,
350	      "spearman_rho_q25": 0.7888259403211363,
351	      "spearman_rho_q75": 1.0,
352	      "per_source_C": {
353	        "vast_deepseek_few-shot-3": {
354	          "partition_match_canonical": 0.595,
355	          "partition_match_truth_C": 0.595,
356	          "spearman_rho_mean_vs_truth": 0.9819596831408367,
357	          "spearman_rho_median_vs_truth": 0.9908673886137246,
358	          "spearman_rho_q25_vs_truth": 0.9722222222222223,
359	          "truth_partition_matches_canonical": true
360	        },
361	        "vast_deepseek_few-shot-5": {
362	          "partition_match_canonical": 0.575,
363	          "partition_match_truth_C": 0.575,
364	          "spearman_rho_mean_vs_truth": 0.9787887597148264,
365	          "spearman_rho_median_vs_truth": 0.9908673886137246,
366	          "spearman_rho_q25_vs_truth": 0.9722222222222223,
367	          "truth_partition_matches_canonical": true
368	        },
369	        "vast_llama4_few-shot-3": {
370	          "partition_match_canonical": 0.0,
371	          "partition_match_truth_C": 0.0,
372	          "spearman_rho_mean_vs_truth": 0.5196746370519365,
373	          "spearman_rho_median_vs_truth": 0.5196746370519364,
374	          "spearman_rho_q25_vs_truth": 0.5196746370519364,
375	          "truth_partition_matches_canonical": true
376	        },
377	        "vast_llama4_zero-shot": {
378	          "partition_match_canonical": 0.0,
379	          "partition_match_truth_C": 0.0,
380	          "spearman_rho_mean_vs_truth": 0.41194292043554975,
381	          "spearman_rho_median_vs_truth": 0.41194292043554975,
382	          "spearman_rho_q25_vs_truth": 0.41194292043554975,
383	          "truth_partition_matches_canonical": true
384	        },
385	        "vast_qwen2.5-7b_few-shot-3": {
386	          "partition_match_canonical": 0.69,
387	          "partition_match_truth_C": 0.69,
388	          "spearman_rho_mean_vs_truth": 0.9929838599193943,
389	          "spearman_rho_median_vs_truth": 1.0,
390	          "spearman_rho_q25_vs_truth": 0.9908673886137247,
391	          "truth_partition_matches_canonical": true
392	        },
393	        "vast_qwen2.5-7b_few-shot-5": {
394	          "partition_match_canonical": 0.75,
395	          "partition_match_truth_C": 0.75,
396	          "spearman_rho_mean_vs_truth": 0.9882814040526984,
397	          "spearman_rho_median_vs_truth": 0.9908673886137246,
398	          "spearman_rho_q25_vs_truth": 0.986206097015849,
399	          "truth_partition_matches_canonical": true
400	        },
401	        "vast_qwen2.5-7b_zero-shot": {
402	          "partition_match_canonical": 0.74,
403	          "partition_match_truth_C": 0.74,
404	          "spearman_rho_mean_vs_truth": 0.9952898185666692,
405	          "spearman_rho_median_vs_truth": 1.0,
406	          "spearman_rho_q25_vs_truth": 0.9908673886137247,
407	          "truth_partition_matches_canonical": true
408	        },
409	        "vast_qwen3_zero-shot": {
410	          "partition_match_canonical": 0.685,
411	          "partition_match_truth_C": 0.685,
412	          "spearman_rho_mean_vs_truth": 0.9893406770395201,
413	          "spearman_rho_median_vs_truth": 0.9908673886137247,
414	          "spearman_rho_q25_vs_truth": 0.9908673886137247,
415	          "truth_partition_matches_canonical": true
416	        }
417	      }
418	    },
419	    "100": {
420	      "n_bootstraps_total": 1600,
421	      "partition_stability_rate_vs_canonical": 0.82,
422	      "partition_stability_rate_vs_truth_C": 0.82,
423	      "spearman_rho_mean": 0.9931707831917691,
424	      "spearman_rho_median": 1.0,
425	      "spearman_rho_q25": 0.9908673886137247,
426	      "spearman_rho_q75": 1.0,
427	      "per_source_C": {
428	        "vast_deepseek_few-shot-3": {
429	          "partition_match_canonical": 0.745,
430	          "partition_match_truth_C": 0.745,
431	          "spearman_rho_mean_vs_truth": 0.9890941383494765,
432	          "spearman_rho_median_vs_truth": 1.0,
433	          "spearman_rho_q25_vs_truth": 0.9722222222222223,
434	          "truth_partition_matches_canonical": true
435	        },
436	        "vast_deepseek_few-shot-5": {
437	          "partition_match_canonical": 0.665,
438	          "partition_match_truth_C": 0.665,
439	          "spearman_rho_mean_vs_truth": 0.9870726538292578,
440	          "spearman_rho_median_vs_truth": 0.9908673886137246,
441	          "spearman_rho_q25_vs_truth": 0.9722222222222223,
442	          "truth_partition_matches_canonical": true
443	        },
444	        "vast_llama4_few-shot-3": {
445	          "partition_match_canonical": 1.0,
446	          "partition_match_truth_C": 1.0,
447	          "spearman_rho_mean_vs_truth": 0.9963469554454898,
448	          "spearman_rho_median_vs_truth": 1.0,
449	          "spearman_rho_q25_vs_truth": 0.9908673886137246,
450	          "truth_partition_matches_canonical": true
451	        },
452	        "vast_llama4_zero-shot": {
453	          "partition_match_canonical": 0.995,
454	          "partition_match_truth_C": 0.995,
455	          "spearman_rho_mean_vs_truth": 0.9935245918669391,
456	          "spearman_rho_median_vs_truth": 0.9954336943068623,
457	          "spearman_rho_q25_vs_truth": 0.9908673886137247,
458	          "truth_partition_matches_canonical": true
459	        },
460	        "vast_qwen2.5-7b_few-shot-3": {
461	          "partition_match_canonical": 0.79,
462	          "partition_match_truth_C": 0.79,
463	          "spearman_rho_mean_vs_truth": 0.9957456150900756,
464	          "spearman_rho_median_vs_truth": 1.0,
465	          "spearman_rho_q25_vs_truth": 0.9908673886137247,
466	          "truth_partition_matches_canonical": true
467	        },
468	        "vast_qwen2.5-7b_few-shot-5": {
469	          "partition_match_canonical": 0.835,
470	          "partition_match_truth_C": 0.835,
471	          "spearman_rho_mean_vs_truth": 0.9924372978920885,
472	          "spearman_rho_median_vs_truth": 1.0,
473	          "spearman_rho_q25_vs_truth": 0.9908673886137246,
474	          "truth_partition_matches_canonical": true
475	        },
476	        "vast_qwen2.5-7b_zero-shot": {
477	          "partition_match_canonical": 0.795,
478	          "partition_match_truth_C": 0.795,
479	          "spearman_rho_mean_vs_truth": 0.9969367148779447,
480	          "spearman_rho_median_vs_truth": 1.0,
481	          "spearman_rho_q25_vs_truth": 0.9908673886137247,
482	          "truth_partition_matches_canonical": true
483	        },
484	        "vast_qwen3_zero-shot": {
485	          "partition_match_canonical": 0.735,
486	          "partition_match_truth_C": 0.735,
487	          "spearman_rho_mean_vs_truth": 0.994208298182881,
488	          "spearman_rho_median_vs_truth": 0.9954336943068623,
489	          "spearman_rho_q25_vs_truth": 0.9908673886137247,
490	          "truth_partition_matches_canonical": true
491	        }
492	      }
493	    },
494	    "200": {
495	      "n_bootstraps_total": 1600,
496	      "partition_stability_rate_vs_canonical": 0.855625,
497	      "partition_stability_rate_vs_truth_C": 0.855625,
498	      "spearman_rho_mean": 0.9949540950273014,
499	      "spearman_rho_median": 1.0,
500	      "spearman_rho_q25": 0.9908673886137247,
501	      "spearman_rho_q75": 1.0,
502	      "per_source_C": {
503	        "vast_deepseek_few-shot-3": {
504	          "partition_match_canonical": 0.79,
505	          "partition_match_truth_C": 0.79,
506	          "spearman_rho_mean_vs_truth": 0.9926500327555217,
507	          "spearman_rho_median_vs_truth": 1.0,
508	          "spearman_rho_q25_vs_truth": 0.9908673886137246,
509	          "truth_partition_matches_canonical": true
510	        },
511	        "vast_deepseek_few-shot-5": {
512	          "partition_match_canonical": 0.715,
513	          "partition_match_truth_C": 0.715,
514	          "spearman_rho_mean_vs_truth": 0.9900204844662588,
515	          "spearman_rho_median_vs_truth": 1.0,
516	          "spearman_rho_q25_vs_truth": 0.9722222222222223,
517	          "truth_partition_matches_canonical": true
518	        },
519	        "vast_llama4_few-shot-3": {
520	          "partition_match_canonical": 1.0,
521	          "partition_match_truth_C": 1.0,
522	          "spearman_rho_mean_vs_truth": 0.9964382815593525,
523	          "spearman_rho_median_vs_truth": 1.0,
524	          "spearman_rho_q25_vs_truth": 0.9908673886137246,
525	          "truth_partition_matches_canonical": true
526	        },
527	        "vast_llama4_zero-shot": {
528	          "partition_match_canonical": 1.0,
529	          "partition_match_truth_C": 1.0,
530	          "spearman_rho_mean_vs_truth": 0.9953448703307215,
531	          "spearman_rho_median_vs_truth": 1.0,
532	          "spearman_rho_q25_vs_truth": 0.9908673886137247,
533	          "truth_partition_matches_canonical": true
534	        },
535	        "vast_qwen2.5-7b_few-shot-3": {
536	          "partition_match_canonical": 0.78,
537	          "partition_match_truth_C": 0.78,
538	          "spearman_rho_mean_vs_truth": 0.9965752707301467,
539	          "spearman_rho_median_vs_truth": 1.0,
540	          "spearman_rho_q25_vs_truth": 0.9908673886137247,
541	          "truth_partition_matches_canonical": true
542	        },
543	        "vast_qwen2.5-7b_few-shot-5": {
544	          "partition_match_canonical": 0.93,
545	          "partition_match_truth_C": 0.93,
546	          "spearman_rho_mean_vs_truth": 0.9950398092660113,
547	          "spearman_rho_median_vs_truth": 1.0,
548	          "spearman_rho_q25_vs_truth": 0.9908673886137246,
549	          "truth_partition_matches_canonical": true
550	        },
551	        "vast_qwen2.5-7b_zero-shot": {
552	          "partition_match_canonical": 0.845,
553	          "partition_match_truth_C": 0.845,
554	          "spearman_rho_mean_vs_truth": 0.9978538363242254,
555	          "spearman_rho_median_vs_truth": 1.0,
556	          "spearman_rho_q25_vs_truth": 1.0,
557	          "truth_partition_matches_canonical": true
558	        },
559	        "vast_qwen3_zero-shot": {
560	          "partition_match_canonical": 0.785,
561	          "partition_match_truth_C": 0.785,
562	          "spearman_rho_mean_vs_truth": 0.9957101747861725,
563	          "spearman_rho_median_vs_truth": 1.0,
564	          "spearman_rho_q25_vs_truth": 0.9908673886137247,
565	          "truth_partition_matches_canonical": true
566	        }
567	      }
568	    },
569	    "500": {
570	      "n_bootstraps_total": 1600,
571	      "partition_stability_rate_vs_canonical": 0.885,
572	      "partition_stability_rate_vs_truth_C": 0.885,
573	      "spearman_rho_mean": 0.996150999681536,
574	      "spearman_rho_median": 1.0,
575	      "spearman_rho_q25": 0.9908673886137247,
576	      "spearman_rho_q75": 1.0,
577	      "per_source_C": {
578	        "vast_deepseek_few-shot-3": {
579	          "partition_match_canonical": 0.81,
580	          "partition_match_truth_C": 0.81,
581	          "spearman_rho_mean_vs_truth": 0.9938804418767238,
582	          "spearman_rho_median_vs_truth": 1.0,
583	          "spearman_rho_q25_vs_truth": 0.9908673886137246,
584	          "truth_partition_matches_canonical": true
585	        },
586	        "vast_deepseek_few-shot-5": {
587	          "partition_match_canonical": 0.76,
588	          "partition_match_truth_C": 0.76,
589	          "spearman_rho_mean_vs_truth": 0.9923704400736278,
590	          "spearman_rho_median_vs_truth": 1.0,
591	          "spearman_rho_q25_vs_truth": 0.9908673886137246,
592	          "truth_partition_matches_canonical": true
593	        },
594	        "vast_llama4_few-shot-3": {
595	          "partition_match_canonical": 1.0,
596	          "partition_match_truth_C": 1.0,
597	          "spearman_rho_mean_vs_truth": 0.9972602165841176,
598	          "spearman_rho_median_vs_truth": 1.0,
599	          "spearman_rho_q25_vs_truth": 0.9908673886137246,
600	          "truth_partition_matches_canonical": true
601	        },
602	        "vast_llama4_zero-shot": {
603	          "partition_match_canonical": 1.0,
604	          "partition_match_truth_C": 1.0,
605	          "spearman_rho_mean_vs_truth": 0.9952062130681127,
606	          "spearman_rho_median_vs_truth": 0.9908673886137247,
607	          "spearman_rho_q25_vs_truth": 0.9908673886137247,
608	          "truth_partition_matches_canonical": true
609	        },
610	        "vast_qwen2.5-7b_few-shot-3": {
611	          "partition_match_canonical": 0.91,
612	          "partition_match_truth_C": 0.91,
613	          "spearman_rho_mean_vs_truth": 0.9989040866336469,
614	          "spearman_rho_median_vs_truth": 1.0,
615	          "spearman_rho_q25_vs_truth": 1.0,
616	          "truth_partition_matches_canonical": true
617	        },
618	        "vast_qwen2.5-7b_few-shot-5": {
619	          "partition_match_canonical": 0.97,
620	          "partition_match_truth_C": 0.97,
621	          "spearman_rho_mean_vs_truth": 0.996426883250784,
622	          "spearman_rho_median_vs_truth": 1.0,
623	          "spearman_rho_q25_vs_truth": 0.9908673886137246,
624	          "truth_partition_matches_canonical": true
625	        },
626	        "vast_qwen2.5-7b_zero-shot": {
627	          "partition_match_canonical": 0.775,
628	          "partition_match_truth_C": 0.775,
629	          "spearman_rho_mean_vs_truth": 0.9978081732672939,
630	          "spearman_rho_median_vs_truth": 1.0,
631	          "spearman_rho_q25_vs_truth": 1.0,
632	          "truth_partition_matches_canonical": true
633	        },
634	        "vast_qwen3_zero-shot": {
635	          "partition_match_canonical": 0.855,
636	          "partition_match_truth_C": 0.855,
637	          "spearman_rho_mean_vs_truth": 0.9973515426979802,
638	          "spearman_rho_median_vs_truth": 1.0,
639	          "spearman_rho_q25_vs_truth": 0.9908673886137247,
640	          "truth_partition_matches_canonical": true
641	        }
642	      }
643	    }
644	  },
645	  "total_time_seconds": 15.90272331237793
646	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "0ae23a31-597b-432c-9e98-8a21566f35e5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness_results.json",
      "content": "{\n  \"description\": \"\\u0108 estimation robustness under multinomial bootstrap from finite gold set\",\n  \"config\": {\n    \"K\": 3,\n    \"n_gold_grid\": [\n      50,\n      100,\n      200,\n      500\n    ],\n    \"B_bootstrap\": 200,\n    \"seed\": 20260523,\n    \"asv_threshold\": 0.05,\n    \"n_delta\": 201,\n    \"topologies\": [\n      \"confounding\",\n      \"mediation\",\n      \"collider\",\n      \"exposure\",\n      \"mbias\",\n      \"iv\",\n      \"frontdoor\"\n    ],\n    \"canonical_safe\": [\n      \"collider\",\n      \"confounding\",\n      \"frontdoor\",\n      \"mbias\",\n      \"mediation\"\n    ],\n    \"canonical_fragile\": [\n      \"exposure\",\n      \"iv\"\n    ],\n    \"empirical_path\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json\"\n  },\n  \"source_matrices\": {\n    \"vast_deepseek_few-shot-3\": {\n      \"C\": [\n        [\n          0.5139,\n          0.1017,\n          0.2888\n        ],\n        [\n          0.3212,\n          0.7985,\n          0.5498\n        ],\n        [\n          0.1649,\n          0.0998,\n          0.1614\n        ]\n      ],\n      \"diag\": [\n        0.5139,\n        0.7985,\n        0.1614\n      ],\n      \"truth_asv\": {\n        \"confounding\": 0.06,\n        \"mediation\": 0.12,\n        \"collider\": null,\n        \"exposure\": 0.055,\n        \"mbias\": null,\n        \"iv\": 0.055,\n        \"frontdoor\": 0.08\n      },\n      \"truth_fragile_set\": [\n        \"exposure\",\n        \"iv\"\n      ],\n      \"truth_matches_canonical\": true\n    },\n    \"vast_deepseek_few-shot-5\": {\n      \"C\": [\n        [\n          0.5268,\n          0.1149,\n          0.3068\n        ],\n        [\n          0.3105,\n          0.7853,\n          0.5398\n        ],\n        [\n          0.1627,\n          0.0998,\n          0.1534\n        ]\n      ],\n      \"diag\": [\n        0.5268,\n        0.7853,\n        0.1534\n      ],\n      \"truth_asv\": {\n        \"confounding\": 0.06,\n        \"mediation\": 0.12,\n        \"collider\": null,\n        \"exposure\": 0.055,\n        \"mbias\": null,\n        \"iv\": 0.055,\n        \"frontdoor\": 0.08\n      },\n      \"truth_fragile_set\": [\n        \"exposure\",\n        \"iv\"\n      ],\n      \"truth_matches_canonical\": true\n    },\n    \"vast_llama4_few-shot-3\": {\n      \"C\": [\n        [\n          0.6595289079229122,\n          0.1807909604519774,\n          0.40438247011952194\n        ],\n        [\n          0.31263383297644537,\n          0.800376647834275,\n          0.5597609561752989\n        ],\n        [\n          0.027837259100642397,\n          0.018832391713747645,\n          0.03585657370517929\n        ]\n      ],\n      \"diag\": [\n        0.6595289079229122,\n        0.800376647834275,\n        0.03585657370517929\n      ],\n      \"truth_asv\": {\n        \"confounding\": 0.065,\n        \"mediation\": 0.14,\n        \"collider\": null,\n        \"exposure\": 0.055,\n        \"mbias\": null,\n        \"iv\": 0.055,\n        \"frontdoor\": 0.09\n      },\n      \"truth_fragile_set\": [\n        \"exposure\",\n        \"iv\"\n      ],\n      \"truth_matches_canonical\": true\n    },\n    \"vast_llama4_zero-shot\": {\n      \"C\": [\n        [\n          0.6781115879828327,\n          0.14393939393939395,\n          0.3964143426294821\n        ],\n        [\n          0.2982832618025751,\n          0.8409090909090909,\n          0.5577689243027889\n        ],\n        [\n          0.023605150214592276,\n          0.015151515151515152,\n          0.04581673306772909\n        ]\n      ],\n      \"diag\": [\n        0.6781115879828327,\n        0.8409090909090909,\n        0.04581673306772909\n      ],\n      \"truth_asv\": {\n        \"confounding\": 0.07,\n        \"mediation\": 0.15,\n        \"collider\": null,\n        \"exposure\": 0.055,\n        \"mbias\": null,\n        \"iv\": 0.06,\n        \"frontdoor\": 0.09\n      },\n      \"truth_fragile_set\": [\n        \"exposure\",\n        \"iv\"\n      ],\n      \"truth_matches_canonical\": true\n    },\n    \"vast_qwen2.5-7b_few-shot-3\": {\n      \"C\": [\n        [\n          0.4132762312633833,\n          0.08662900188323917,\n          0.22310756972111553\n        ],\n        [\n          0.44539614561027835,\n          0.8210922787193974,\n          0.651394422310757\n        ],\n        [\n          0.14132762312633834,\n          0.09227871939736347,\n          0.1254980079681275\n        ]\n      ],\n      \"diag\": [\n        0.4132762312633833,\n        0.8210922787193974,\n        0.1254980079681275\n      ],\n      \"truth_asv\": {\n        \"confounding\": 0.055,\n        \"mediation\": 0.11,\n        \"collider\": null,\n        \"exposure\": 0.045,\n        \"mbias\": null,\n        \"iv\": 0.05,\n        \"frontdoor\": 0.075\n      },\n      \"truth_fragile_set\": [\n        \"exposure\",\n        \"iv\"\n      ],\n      \"truth_matches_canonical\": true\n    },\n    \"vast_qwen2.5-7b_few-shot-5\": {\n      \"C\": [\n        [\n          0.4753747323340471,\n          0.11111111111111112,\n          0.2589641434262948\n        ],\n        [\n          0.39186295503211993,\n          0.7758945386064031,\n          0.6155378486055777\n        ],\n        [\n          0.13276231263383298,\n          0.11299435028248589,\n          0.1254980079681275\n        ]\n      ],\n      \"diag\": [\n        0.4753747323340471,\n        0.7758945386064031,\n        0.1254980079681275\n      ],\n      \"truth_asv\": {\n        \"confounding\": 0.055,\n        \"mediation\": 0.11,\n        \"collider\": null,\n        \"exposure\": 0.05,\n        \"mbias\": null,\n        \"iv\": 0.05,\n        \"frontdoor\": 0.075\n      },\n      \"truth_fragile_set\": [\n        \"exposure\",\n        \"iv\"\n      ],\n      \"truth_matches_canonical\": true\n    },\n    \"vast_qwen2.5-7b_zero-shot\": {\n      \"C\": [\n        [\n          0.4613733905579399,\n          0.07909604519774012,\n          0.2410358565737052\n        ],\n        [\n          0.4313304721030043,\n          0.847457627118644,\n          0.649402390438247\n        ],\n        [\n          0.1072961373390558,\n          0.07344632768361582,\n          0.10956175298804781\n        ]\n      ],\n      \"diag\": [\n        0.4613733905579399,\n        0.847457627118644,\n        0.10956175298804781\n      ],\n      \"truth_asv\": {\n        \"confounding\": 0.055,\n        \"mediation\": 0.12,\n        \"collider\": null,\n        \"exposure\": 0.045,\n        \"mbias\": null,\n        \"iv\": 0.05,\n        \"frontdoor\": 0.075\n      },\n      \"truth_fragile_set\": [\n        \"exposure\",\n        \"iv\"\n      ],\n      \"truth_matches_canonical\": true\n    },\n    \"vast_qwen3_zero-shot\": {\n      \"C\": [\n        [\n          0.6858974358974359,\n          0.16666666666666666,\n          0.40357852882703776\n        ],\n        [\n          0.23504273504273504,\n          0.7746212121212122,\n          0.5228628230616302\n        ],\n        [\n          0.07905982905982906,\n          0.058712121212121215,\n          0.073558648111332\n        ]\n      ],\n      \"diag\": [\n        0.6858974358974359,\n        0.7746212121212122,\n        0.073558648111332\n      ],\n      \"truth_asv\": {\n        \"confounding\": 0.07,\n        \"mediation\": 0.135,\n        \"collider\": null,\n        \"exposure\": 0.065,\n        \"mbias\": null,\n        \"iv\": 0.06,\n        \"frontdoor\": 0.085\n      },\n      \"truth_fragile_set\": [\n        \"exposure\",\n        \"iv\"\n      ],\n      \"truth_matches_canonical\": true\n    }\n  },\n  \"results_per_n_gold\": {\n    \"50\": {\n      \"n_bootstraps_total\": 1600,\n      \"partition_stability_rate_vs_canonical\": 0.504375,\n      \"partition_stability_rate_vs_truth_C\": 0.504375,\n      \"spearman_rho_mean\": 0.8572827199901789,\n      \"spearman_rho_median\": 0.9908673886137246,\n      \"spearman_rho_q25\": 0.7888259403211363,\n      \"spearman_rho_q75\": 1.0,\n      \"per_source_C\": {\n        \"vast_deepseek_few-shot-3\": {\n          \"partition_match_canonical\": 0.595,\n          \"partition_match_truth_C\": 0.595,\n          \"spearman_rho_mean_vs_truth\": 0.9819596831408367,\n          \"spearman_rho_median_vs_truth\": 0.9908673886137246,\n          \"spearman_rho_q25_vs_truth\": 0.9722222222222223,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_deepseek_few-shot-5\": {\n          \"partition_match_canonical\": 0.575,\n          \"partition_match_truth_C\": 0.575,\n          \"spearman_rho_mean_vs_truth\": 0.9787887597148264,\n          \"spearman_rho_median_vs_truth\": 0.9908673886137246,\n          \"spearman_rho_q25_vs_truth\": 0.9722222222222223,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_llama4_few-shot-3\": {\n          \"partition_match_canonical\": 0.0,\n          \"partition_match_truth_C\": 0.0,\n          \"spearman_rho_mean_vs_truth\": 0.5196746370519365,\n          \"spearman_rho_median_vs_truth\": 0.5196746370519364,\n          \"spearman_rho_q25_vs_truth\": 0.5196746370519364,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_llama4_zero-shot\": {\n          \"partition_match_canonical\": 0.0,\n          \"partition_match_truth_C\": 0.0,\n          \"spearman_rho_mean_vs_truth\": 0.41194292043554975,\n          \"spearman_rho_median_vs_truth\": 0.41194292043554975,\n          \"spearman_rho_q25_vs_truth\": 0.41194292043554975,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_qwen2.5-7b_few-shot-3\": {\n          \"partition_match_canonical\": 0.69,\n          \"partition_match_truth_C\": 0.69,\n          \"spearman_rho_mean_vs_truth\": 0.9929838599193943,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137247,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_qwen2.5-7b_few-shot-5\": {\n          \"partition_match_canonical\": 0.75,\n          \"partition_match_truth_C\": 0.75,\n          \"spearman_rho_mean_vs_truth\": 0.9882814040526984,\n          \"spearman_rho_median_vs_truth\": 0.9908673886137246,\n          \"spearman_rho_q25_vs_truth\": 0.986206097015849,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_qwen2.5-7b_zero-shot\": {\n          \"partition_match_canonical\": 0.74,\n          \"partition_match_truth_C\": 0.74,\n          \"spearman_rho_mean_vs_truth\": 0.9952898185666692,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137247,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_qwen3_zero-shot\": {\n          \"partition_match_canonical\": 0.685,\n          \"partition_match_truth_C\": 0.685,\n          \"spearman_rho_mean_vs_truth\": 0.9893406770395201,\n          \"spearman_rho_median_vs_truth\": 0.9908673886137247,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137247,\n          \"truth_partition_matches_canonical\": true\n        }\n      }\n    },\n    \"100\": {\n      \"n_bootstraps_total\": 1600,\n      \"partition_stability_rate_vs_canonical\": 0.82,\n      \"partition_stability_rate_vs_truth_C\": 0.82,\n      \"spearman_rho_mean\": 0.9931707831917691,\n      \"spearman_rho_median\": 1.0,\n      \"spearman_rho_q25\": 0.9908673886137247,\n      \"spearman_rho_q75\": 1.0,\n      \"per_source_C\": {\n        \"vast_deepseek_few-shot-3\": {\n          \"partition_match_canonical\": 0.745,\n          \"partition_match_truth_C\": 0.745,\n          \"spearman_rho_mean_vs_truth\": 0.9890941383494765,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9722222222222223,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_deepseek_few-shot-5\": {\n          \"partition_match_canonical\": 0.665,\n          \"partition_match_truth_C\": 0.665,\n          \"spearman_rho_mean_vs_truth\": 0.9870726538292578,\n          \"spearman_rho_median_vs_truth\": 0.9908673886137246,\n          \"spearman_rho_q25_vs_truth\": 0.9722222222222223,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_llama4_few-shot-3\": {\n          \"partition_match_canonical\": 1.0,\n          \"partition_match_truth_C\": 1.0,\n          \"spearman_rho_mean_vs_truth\": 0.9963469554454898,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137246,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_llama4_zero-shot\": {\n          \"partition_match_canonical\": 0.995,\n          \"partition_match_truth_C\": 0.995,\n          \"spearman_rho_mean_vs_truth\": 0.9935245918669391,\n          \"spearman_rho_median_vs_truth\": 0.9954336943068623,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137247,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_qwen2.5-7b_few-shot-3\": {\n          \"partition_match_canonical\": 0.79,\n          \"partition_match_truth_C\": 0.79,\n          \"spearman_rho_mean_vs_truth\": 0.9957456150900756,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137247,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_qwen2.5-7b_few-shot-5\": {\n          \"partition_match_canonical\": 0.835,\n          \"partition_match_truth_C\": 0.835,\n          \"spearman_rho_mean_vs_truth\": 0.9924372978920885,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137246,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_qwen2.5-7b_zero-shot\": {\n          \"partition_match_canonical\": 0.795,\n          \"partition_match_truth_C\": 0.795,\n          \"spearman_rho_mean_vs_truth\": 0.9969367148779447,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137247,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_qwen3_zero-shot\": {\n          \"partition_match_canonical\": 0.735,\n          \"partition_match_truth_C\": 0.735,\n          \"spearman_rho_mean_vs_truth\": 0.994208298182881,\n          \"spearman_rho_median_vs_truth\": 0.9954336943068623,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137247,\n          \"truth_partition_matches_canonical\": true\n        }\n      }\n    },\n    \"200\": {\n      \"n_bootstraps_total\": 1600,\n      \"partition_stability_rate_vs_canonical\": 0.855625,\n      \"partition_stability_rate_vs_truth_C\": 0.855625,\n      \"spearman_rho_mean\": 0.9949540950273014,\n      \"spearman_rho_median\": 1.0,\n      \"spearman_rho_q25\": 0.9908673886137247,\n      \"spearman_rho_q75\": 1.0,\n      \"per_source_C\": {\n        \"vast_deepseek_few-shot-3\": {\n          \"partition_match_canonical\": 0.79,\n          \"partition_match_truth_C\": 0.79,\n          \"spearman_rho_mean_vs_truth\": 0.9926500327555217,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137246,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_deepseek_few-shot-5\": {\n          \"partition_match_canonical\": 0.715,\n          \"partition_match_truth_C\": 0.715,\n          \"spearman_rho_mean_vs_truth\": 0.9900204844662588,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9722222222222223,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_llama4_few-shot-3\": {\n          \"partition_match_canonical\": 1.0,\n          \"partition_match_truth_C\": 1.0,\n          \"spearman_rho_mean_vs_truth\": 0.9964382815593525,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137246,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_llama4_zero-shot\": {\n          \"partition_match_canonical\": 1.0,\n          \"partition_match_truth_C\": 1.0,\n          \"spearman_rho_mean_vs_truth\": 0.9953448703307215,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137247,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_qwen2.5-7b_few-shot-3\": {\n          \"partition_match_canonical\": 0.78,\n          \"partition_match_truth_C\": 0.78,\n          \"spearman_rho_mean_vs_truth\": 0.9965752707301467,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137247,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_qwen2.5-7b_few-shot-5\": {\n          \"partition_match_canonical\": 0.93,\n          \"partition_match_truth_C\": 0.93,\n          \"spearman_rho_mean_vs_truth\": 0.9950398092660113,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137246,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_qwen2.5-7b_zero-shot\": {\n          \"partition_match_canonical\": 0.845,\n          \"partition_match_truth_C\": 0.845,\n          \"spearman_rho_mean_vs_truth\": 0.9978538363242254,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 1.0,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_qwen3_zero-shot\": {\n          \"partition_match_canonical\": 0.785,\n          \"partition_match_truth_C\": 0.785,\n          \"spearman_rho_mean_vs_truth\": 0.9957101747861725,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137247,\n          \"truth_partition_matches_canonical\": true\n        }\n      }\n    },\n    \"500\": {\n      \"n_bootstraps_total\": 1600,\n      \"partition_stability_rate_vs_canonical\": 0.885,\n      \"partition_stability_rate_vs_truth_C\": 0.885,\n      \"spearman_rho_mean\": 0.996150999681536,\n      \"spearman_rho_median\": 1.0,\n      \"spearman_rho_q25\": 0.9908673886137247,\n      \"spearman_rho_q75\": 1.0,\n      \"per_source_C\": {\n        \"vast_deepseek_few-shot-3\": {\n          \"partition_match_canonical\": 0.81,\n          \"partition_match_truth_C\": 0.81,\n          \"spearman_rho_mean_vs_truth\": 0.9938804418767238,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137246,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_deepseek_few-shot-5\": {\n          \"partition_match_canonical\": 0.76,\n          \"partition_match_truth_C\": 0.76,\n          \"spearman_rho_mean_vs_truth\": 0.9923704400736278,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137246,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_llama4_few-shot-3\": {\n          \"partition_match_canonical\": 1.0,\n          \"partition_match_truth_C\": 1.0,\n          \"spearman_rho_mean_vs_truth\": 0.9972602165841176,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137246,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_llama4_zero-shot\": {\n          \"partition_match_canonical\": 1.0,\n          \"partition_match_truth_C\": 1.0,\n          \"spearman_rho_mean_vs_truth\": 0.9952062130681127,\n          \"spearman_rho_median_vs_truth\": 0.9908673886137247,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137247,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_qwen2.5-7b_few-shot-3\": {\n          \"partition_match_canonical\": 0.91,\n          \"partition_match_truth_C\": 0.91,\n          \"spearman_rho_mean_vs_truth\": 0.9989040866336469,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 1.0,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_qwen2.5-7b_few-shot-5\": {\n          \"partition_match_canonical\": 0.97,\n          \"partition_match_truth_C\": 0.97,\n          \"spearman_rho_mean_vs_truth\": 0.996426883250784,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137246,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_qwen2.5-7b_zero-shot\": {\n          \"partition_match_canonical\": 0.775,\n          \"partition_match_truth_C\": 0.775,\n          \"spearman_rho_mean_vs_truth\": 0.9978081732672939,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 1.0,\n          \"truth_partition_matches_canonical\": true\n        },\n        \"vast_qwen3_zero-shot\": {\n          \"partition_match_canonical\": 0.855,\n          \"partition_match_truth_C\": 0.855,\n          \"spearman_rho_mean_vs_truth\": 0.9973515426979802,\n          \"spearman_rho_median_vs_truth\": 1.0,\n          \"spearman_rho_q25_vs_truth\": 0.9908673886137247,\n          \"truth_partition_matches_canonical\": true\n        }\n      }\n    }\n  },\n  \"total_time_seconds\": 15.90272331237793\n}",
      "numLines": 646,
      "startLine": 1,
      "totalLines": 646
    }
  }
}
```

</details>

---

### Assistant

_source line 84_

<details><summary>Logged reasoning block</summary>

```text
The script and results JSON both already exist and look complete. Let me verify the results are consistent and reasonable:

Summary from the JSON:
- n_gold=50: partition stability = 50.4%, rho_mean = 0.857
- n_gold=100: partition stability = 82.0%, rho_mean = 0.993
- n_gold=200: partition stability = 85.6%, rho_mean = 0.995
- n_gold=500: partition stability = 88.5%, rho_mean = 0.996


The low partition stability at n_gold=50 makes sense—the llama4 matrices show 0% stability there because bootstrap noise dominates at that sample size, but they recover dramatically to 99.5-100% by n_gold=100. The Spearman correlations are impressively high across the board, hitting perfect 1.0 medians once we reach n_gold=100, which confirms the implementation is solid.

I need to re-run the script to verify the results are current and that everything writes to JSON as expected before wrapping up.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "5dcd7dfe-3107-499a-8a01-f3bac83c2c9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APs5Zhx4YncPUX2LPQa7Yw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14071,
      "cache_read_input_tokens": 27874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14071
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

_source line 85_

脚本和结果 JSON 都已存在且完整。重新运行脚本确认可复现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "9e7d27d9-fd30-4381-a12f-175a3d258630",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APs5Zhx4YncPUX2LPQa7Yw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14071,
      "cache_read_input_tokens": 27874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14071
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

_source line 86_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q5EzwCmiwcwXCUSBoLxdiZ`</summary>

```json
{
  "command": "python artifacts/c_estimation_robustness.py",
  "description": "Run Ĉ estimation robustness experiment",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "f3fc2bd6-2cfd-49dd-97e5-9c86b2700c97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APs5Zhx4YncPUX2LPQa7Yw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14071,
      "cache_read_input_tokens": 27874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14071
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

_source line 87 · 2026-05-23T14:57:30.552Z_

<details><summary>↩ Tool result · reported error · `toolu_01Q5EzwCmiwcwXCUSBoLxdiZ`</summary>

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
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "364daa42-96d7-4b62-b132-c587c736cced",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---

### Tool call

_source line 88_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gf8eifgx2PsBP4wW4c9ReN`</summary>

```json
{
  "command": "python3 artifacts/c_estimation_robustness.py",
  "description": "Run Ĉ estimation robustness experiment",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "eaa5ab31-4287-4c2c-8582-b86fee854b60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NvSUbYxwhHCkjLp9XfQnHF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 41945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 585
      },
      "output_tokens": 38,
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

_source line 89_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b5h1it3z5",
  "tool_use_id": "toolu_01Gf8eifgx2PsBP4wW4c9ReN",
  "description": "Run Ĉ estimation robustness experiment",
  "task_type": "local_bash",
  "uuid": "e37d86a3-b390-448e-9dac-5be27b8f5ccf",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### System

_source line 90_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b5h1it3z5",
  "tool_use_id": "toolu_01Gf8eifgx2PsBP4wW4c9ReN",
  "status": "completed",
  "output_file": "",
  "summary": "Run Ĉ estimation robustness experiment",
  "uuid": "3805c09a-6c67-496d-a022-c55d0fd23f09",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af"
}
```

---

### Tool result

_source line 91 · 2026-05-23T14:57:43.661Z_

<details><summary>↩ Tool result · `toolu_01Gf8eifgx2PsBP4wW4c9ReN`</summary>

```text
Ĉ Estimation Robustness Experiment
  K=3, B=200, n_gold ∈ [50, 100, 200, 500]
  Topologies: ['confounding', 'mediation', 'collider', 'exposure', 'mbias', 'iv', 'frontdoor']
  ASV threshold (magnitude): 0.05
  n_delta = 201
======================================================================

Precomputing sufficient statistics & tau_true...
  confounding  tau_true = 2.000000
  mediation    tau_true = 0.500000
  collider     tau_true = 1.000000
  exposure     tau_true = 1.000000
  mbias        tau_true = 1.000000
  iv           tau_true = 1.333121
  frontdoor    tau_true = 0.500000

Loading empirical K=3 confusion matrices...
  Loaded 8 K=3 matrices
    vast_deepseek_few-shot-3  diag=[0.514, 0.798, 0.161]
    vast_deepseek_few-shot-5  diag=[0.527, 0.785, 0.153]
    vast_llama4_few-shot-3  diag=[0.66, 0.8, 0.036]
    vast_llama4_zero-shot  diag=[0.678, 0.841, 0.046]
    vast_qwen2.5-7b_few-shot-3  diag=[0.413, 0.821, 0.125]
    vast_qwen2.5-7b_few-shot-5  diag=[0.475, 0.776, 0.125]
    vast_qwen2.5-7b_zero-shot  diag=[0.461, 0.847, 0.11]
    vast_qwen3_zero-shot  diag=[0.686, 0.775, 0.074]

Computing ASV for the truth Cs...
  vast_deepseek_few-shot-3  fragile-set=['exposure', 'iv']  matches canonical: YES
  vast_deepseek_few-shot-5  fragile-set=['exposure', 'iv']  matches canonical: YES
  vast_llama4_few-shot-3  fragile-set=['exposure', 'iv']  matches canonical: YES
  vast_llama4_zero-shot  fragile-set=['exposure', 'iv']  matches canonical: YES
  vast_qwen2.5-7b_few-shot-3  fragile-set=['exposure', 'iv']  matches canonical: YES
  vast_qwen2.5-7b_few-shot-5  fragile-set=['exposure', 'iv']  matches canonical: YES
  vast_qwen2.5-7b_zero-shot  fragile-set=['exposure', 'iv']  matches canonical: YES
  vast_qwen3_zero-shot  fragile-set=['exposure', 'iv']  matches canonical: YES

Bootstrapping (B=200)...
  n_gold=50    partition_rate_canonical=0.5044  partition_rate_truth=0.5044  rho_mean=0.8573  (2.8s)
  n_gold=100   partition_rate_canonical=0.8200  partition_rate_truth=0.8200  rho_mean=0.9932  (1.9s)
  n_gold=200   partition_rate_canonical=0.8556  partition_rate_truth=0.8556  rho_mean=0.9950  (1.9s)
  n_gold=500   partition_rate_canonical=0.8850  partition_rate_truth=0.8850  rho_mean=0.9962  (1.9s)

======================================================================
Summary
======================================================================
n_gold  part_canon    part_truth    rho_mean    rho_median  
50      0.5044        0.5044        0.8573      0.9909      
100     0.8200        0.8200        0.9932      1.0000      
200     0.8556        0.8556        0.9950      1.0000      
500     0.8850        0.8850        0.9962      1.0000      

JSON saved: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness_results.json
Total: 8.4s
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "9171d85d-eae8-419f-970f-be73eb6e2fa6",
  "tool_use_result": {
    "stdout": "Ĉ Estimation Robustness Experiment\n  K=3, B=200, n_gold ∈ [50, 100, 200, 500]\n  Topologies: ['confounding', 'mediation', 'collider', 'exposure', 'mbias', 'iv', 'frontdoor']\n  ASV threshold (magnitude): 0.05\n  n_delta = 201\n======================================================================\n\nPrecomputing sufficient statistics & tau_true...\n  confounding  tau_true = 2.000000\n  mediation    tau_true = 0.500000\n  collider     tau_true = 1.000000\n  exposure     tau_true = 1.000000\n  mbias        tau_true = 1.000000\n  iv           tau_true = 1.333121\n  frontdoor    tau_true = 0.500000\n\nLoading empirical K=3 confusion matrices...\n  Loaded 8 K=3 matrices\n    vast_deepseek_few-shot-3  diag=[0.514, 0.798, 0.161]\n    vast_deepseek_few-shot-5  diag=[0.527, 0.785, 0.153]\n    vast_llama4_few-shot-3  diag=[0.66, 0.8, 0.036]\n    vast_llama4_zero-shot  diag=[0.678, 0.841, 0.046]\n    vast_qwen2.5-7b_few-shot-3  diag=[0.413, 0.821, 0.125]\n    vast_qwen2.5-7b_few-shot-5  diag=[0.475, 0.776, 0.125]\n    vast_qwen2.5-7b_zero-shot  diag=[0.461, 0.847, 0.11]\n    vast_qwen3_zero-shot  diag=[0.686, 0.775, 0.074]\n\nComputing ASV for the truth Cs...\n  vast_deepseek_few-shot-3  fragile-set=['exposure', 'iv']  matches canonical: YES\n  vast_deepseek_few-shot-5  fragile-set=['exposure', 'iv']  matches canonical: YES\n  vast_llama4_few-shot-3  fragile-set=['exposure', 'iv']  matches canonical: YES\n  vast_llama4_zero-shot  fragile-set=['exposure', 'iv']  matches canonical: YES\n  vast_qwen2.5-7b_few-shot-3  fragile-set=['exposure', 'iv']  matches canonical: YES\n  vast_qwen2.5-7b_few-shot-5  fragile-set=['exposure', 'iv']  matches canonical: YES\n  vast_qwen2.5-7b_zero-shot  fragile-set=['exposure', 'iv']  matches canonical: YES\n  vast_qwen3_zero-shot  fragile-set=['exposure', 'iv']  matches canonical: YES\n\nBootstrapping (B=200)...\n  n_gold=50    partition_rate_canonical=0.5044  partition_rate_truth=0.5044  rho_mean=0.8573  (2.8s)\n  n_gold=100   partition_rate_canonical=0.8200  partition_rate_truth=0.8200  rho_mean=0.9932  (1.9s)\n  n_gold=200   partition_rate_canonical=0.8556  partition_rate_truth=0.8556  rho_mean=0.9950  (1.9s)\n  n_gold=500   partition_rate_canonical=0.8850  partition_rate_truth=0.8850  rho_mean=0.9962  (1.9s)\n\n======================================================================\nSummary\n======================================================================\nn_gold  part_canon    part_truth    rho_mean    rho_median  \n50      0.5044        0.5044        0.8573      0.9909      \n100     0.8200        0.8200        0.9932      1.0000      \n200     0.8556        0.8556        0.9950      1.0000      \n500     0.8850        0.8850        0.9962      1.0000      \n\nJSON saved: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/c_estimation_robustness_results.json\nTotal: 8.4s",
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

_source line 92_

脚本运行成功，结果已写入 JSON。

**结果摘要：**

| n_gold | Partition 稳定率 | Spearman ρ (mean) | Spearman ρ (median) |
|--------|-----------------|-------------------|---------------------|
| 50     | 50.4%           | 0.857             | 0.991               |
| 100    | 82.0%           | 0.993             | 1.000               |
| 200    | 85.6%           | 0.995             | 1.000               |
| 500    | 88.5%           | 0.996             | 1.000               |

所有 8 个源矩阵的 truth partition 都匹配 canonical fragile set {exposure, iv}。n_gold=50 时 partition 稳定率较低主要是 llama4 两个矩阵拖累（0%），但这两个矩阵在 n_gold=100 时跳至 99.5-100%。ASV 排名相关性（ρ）从 n_gold≥100 起即达 >0.99，说明有限 gold set 下 Ĉ 估计对 safe/fragile 划分是鲁棒的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "uuid": "6b5f8195-d19c-40eb-b34b-0680c8fb9522",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMSob3HSj7KZ6y2GiRPQLs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1245,
      "cache_read_input_tokens": 42530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1245
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

### Task result

_source line 93_

脚本运行成功，结果已写入 JSON。

**结果摘要：**

| n_gold | Partition 稳定率 | Spearman ρ (mean) | Spearman ρ (median) |
|--------|-----------------|-------------------|---------------------|
| 50     | 50.4%           | 0.857             | 0.991               |
| 100    | 82.0%           | 0.993             | 1.000               |
| 200    | 85.6%           | 0.995             | 1.000               |
| 500    | 88.5%           | 0.996             | 1.000               |

所有 8 个源矩阵的 truth partition 都匹配 canonical fragile set {exposure, iv}。n_gold=50 时 partition 稳定率较低主要是 llama4 两个矩阵拖累（0%），但这两个矩阵在 n_gold=100 时跳至 99.5-100%。ASV 排名相关性（ρ）从 n_gold≥100 起即达 >0.99，说明有限 gold set 下 Ĉ 估计对 safe/fragile 划分是鲁棒的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 124821,
  "duration_api_ms": 115743,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "98f46da3-172a-491a-aaa0-531aa22cc5af",
  "total_cost_usd": 0.5295664000000001,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 31934,
    "cache_read_input_tokens": 149284,
    "output_tokens": 1625,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 31934,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 339,
        "cache_read_input_tokens": 42530,
        "cache_creation_input_tokens": 1245,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1245
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1357,
      "outputTokens": 5344,
      "cacheReadInputTokens": 955099,
      "cacheCreationInputTokens": 72872,
      "webSearchRequests": 0,
      "costUSD": 0.2146769,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 1625,
      "cacheReadInputTokens": 149284,
      "cacheCreationInputTokens": 31934,
      "webSearchRequests": 0,
      "costUSD": 0.3148895,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "96359a39-fe43-4d7f-9db6-13a9919949d0"
}
```

</details>

---
