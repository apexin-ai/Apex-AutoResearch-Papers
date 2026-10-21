# code plan 034 multi subject injection

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 112
- **Recorded user turns:** 1
- **Tool calls:** 34
- **Original source:** `logs/workers/worker_code_plan_034_multi_subject_injection_20260521T154505.log`
- **Structured JSON:** [`d4d624aee1a026fef050.json`](../../sessions/d4/d4d624aee1a026fef050.json)

## Before a recorded user message

7 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
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
  "uuid": "69d160d6-d7cf-4069-9015-0de2e702c468",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/memory/"
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
    "resetsAt": 1779382200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "beaf67a4-4cfe-4541-a62c-e4ae070395ba",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to implement Plan 034: a multi-subject simultaneous injection experiment to test Proposition 1's robustness boundary. Let me start by understanding the existing code and data structures, then write the experiment script.

Let me first read the reference code from plan_016 and plan_011 to understand the MH-DIF implementation and injection framework.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "3c768a9b-9eb0-456e-b548-b402f6e0185c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011UyaYA97z289qH6FoEms7Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13392,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13392
      },
      "output_tokens": 27,
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

_source line 5_

I'll start by reading the reference code and data to understand the existing MH-DIF implementation and data structures.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "ce848291-395b-45bd-b8cc-06f03da93621",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011UyaYA97z289qH6FoEms7Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13392,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13392
      },
      "output_tokens": 27,
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

_source line 6_

<details open><summary>🔧 Tool call — Agent · `toolu_01MR3pkEvJfub3UbUuhSTgUT`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore plan_016 and plan_011 code",
  "prompt": "I need to understand the MH-DIF implementation and semi-synthetic injection framework in two directories:\n\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/` - cross-subject matching implementation\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py` - basic semi-synthetic injection framework\n\nFor each, I need:\n- The MH-DIF function signature and implementation (especially purified MH-DIF with external matching)\n- How injection (incorrect→correct flip) is done\n- How cohorts (ref/foc) are defined\n- How TPR/FPR are calculated\n- ETS classification logic\n- How response matrix and metadata are loaded\n\nBe very thorough - read the full files and report back all relevant code patterns, function signatures, and implementation details. Include line numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "8406e14c-5461-4507-a0ac-3a24ee7be07f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011UyaYA97z289qH6FoEms7Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13392,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13392
      },
      "output_tokens": 27,
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

_source line 7_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "aa73b16fd4338b1af",
  "tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "description": "Explore plan_016 and plan_011 code",
  "task_type": "local_agent",
  "prompt": "I need to understand the MH-DIF implementation and semi-synthetic injection framework in two directories:\n\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/` - cross-subject matching implementation\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py` - basic semi-synthetic injection framework\n\nFor each, I need:\n- The MH-DIF function signature and implementation (especially purified MH-DIF with external matching)\n- How injection (incorrect→correct flip) is done\n- How cohorts (ref/foc) are defined\n- How TPR/FPR are calculated\n- ETS classification logic\n- How response matrix and metadata are loaded\n\nBe very thorough - read the full files and report back all relevant code patterns, function signatures, and implementation details. Include line numbers.",
  "uuid": "e20ab749-8100-43e8-9749-6325357a23c7",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c"
}
```

---

## Round 1

105 recorded events

### User

_source line 8 · 2026-05-21T15:45:28.896Z_

I need to understand the MH-DIF implementation and semi-synthetic injection framework in two directories:

1. `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/` - cross-subject matching implementation
2. `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py` - basic semi-synthetic injection framework

For each, I need:
- The MH-DIF function signature and implementation (especially purified MH-DIF with external matching)
- How injection (incorrect→correct flip) is done
- How cohorts (ref/foc) are defined
- How TPR/FPR are calculated
- ETS classification logic
- How response matrix and metadata are loaded

Be very thorough - read the full files and report back all relevant code patterns, function signatures, and implementation details. Include line numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "f23f2d36-d905-4d16-bc06-5a909f3d8996"
}
```

</details>

---

### System

_source line 9_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa73b16fd4338b1af",
  "tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_052…",
  "usage": {
    "total_tokens": 17065,
    "tool_uses": 1,
    "duration_ms": 1677
  },
  "last_tool_name": "Bash",
  "uuid": "d76d3134-f4e3-41da-8055-e3fe85fa8aa1",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c"
}
```

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Bash · `toolu_01KhPEyixfHVxwxocsQCjw6v`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/ -type f -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "e86e1a2d-d7c3-4c08-93a7-c02e6bad8fd1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015nqME6kGCstZm998Ku7rL3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17056,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17056,
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

_source line 11 · 2026-05-21T15:45:30.758Z_

<details><summary>↩ Tool result · `toolu_01KhPEyixfHVxwxocsQCjw6v`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_within_subject_injection.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "ef6d05d4-a982-4551-b515-ee40295983c6"
}
```

</details>

---

### System

_source line 12_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa73b16fd4338b1af",
  "tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 18108,
    "tool_uses": 2,
    "duration_ms": 3294
  },
  "last_tool_name": "Bash",
  "uuid": "24c202ec-a9f7-40d5-a4a1-d31817de3007",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c"
}
```

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_01LbyJAYqRpFvGYRrKbCTEjX`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "6022a114-8db9-4bcf-b079-f2b93cf46f6b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UU3R5nqeCP7KhQbw2hnUR9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1039,
      "cache_read_input_tokens": 17056,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1039,
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

_source line 14 · 2026-05-21T15:45:32.258Z_

<details><summary>↩ Tool result · `toolu_01LbyJAYqRpFvGYRrKbCTEjX`</summary>

```text
total 2096
drwxr-xr-x  2 ubuntu ubuntu    4096 May 20 21:48 .
drwxr-xr-x 43 ubuntu ubuntu    4096 May 21 15:40 ..
-rw-r--r--  1 ubuntu ubuntu    3587 May 20 21:48 dose_response_summary.csv
-rw-r--r--  1 ubuntu ubuntu   19217 May 20 21:48 injection_results.csv
-rw-r--r--  1 ubuntu ubuntu 2076592 May 20 21:48 per_item_results.csv
-rw-r--r--  1 ubuntu ubuntu   25953 May 20 21:48 plan_011_analysis.py
-rw-r--r--  1 ubuntu ubuntu    7000 May 20 21:48 plan_011_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "672dbb11-e8dc-477e-b083-8e793538a929"
}
```

</details>

---

### System

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa73b16fd4338b1af",
  "tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "description": "Reading artifacts/plan_011/plan_011_analysis.py",
  "usage": {
    "total_tokens": 18464,
    "tool_uses": 3,
    "duration_ms": 4881
  },
  "last_tool_name": "Read",
  "uuid": "681a02f4-fa59-4e7f-8498-baba0cfec889",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c"
}
```

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_011EBAMnG5tKrunK35YycYyW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "fcf2c443-aff1-4171-8da7-b779084a1364",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UBGFqfKugG5agCRXiivG65",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 354,
      "cache_read_input_tokens": 18095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 354,
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

_source line 17 · 2026-05-21T15:45:33.797Z_

<details><summary>↩ Tool result · `toolu_011EBAMnG5tKrunK35YycYyW`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_011_analysis.py — Semi-Synthetic DIF Validation
4	
5	Injects known differential contamination into real MMLU response data and tests
6	whether MH-DIF can detect it. Validates the DIF methodology used in plan_001.
7	
8	Three MH variants:
9	  (1) standard  — total score on 500 items minus current (same as plan_001)
10	  (2) anchor    — total score on 400 known-clean items only
11	  (3) external  — total score on full 12508-item original matrix (best matching)
12	
13	Inputs:
14	  response_matrix.npz, response_matrix_index.npz, model_metadata.csv,
15	  item_metadata.csv, mmlu_li2024_proxy_labels.csv,
16	  plan_001/dif_results_ability.csv
17	
18	Outputs (all in plan_011/):
19	  injection_results.csv, dose_response_summary.csv, per_item_results.csv,
20	  plan_011_report.md
21	"""
22	
23	import numpy as np
24	import pandas as pd
25	from scipy.sparse import load_npz
26	from scipy.stats import chi2 as chi2_dist, fisher_exact
27	from pathlib import Path
28	import time
29	import warnings
30	
31	warnings.filterwarnings("ignore", category=RuntimeWarning)
32	
33	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
34	OUT = BASE / "plan_011"
35	OUT.mkdir(exist_ok=True)
36	
37	INJECTION_PS = [0.0, 0.3, 0.5, 0.7, 1.0]
38	N_SEEDS = 5
39	N_BASELINE = 500
40	N_CONTAMINATED = 100
41	
42	
43	# ════════════════════════════════════════════════════════════════════════════
44	#  MH-DIF CORE
45	# ════════════════════════════════════════════════════════════════════════════
46	def mh_dif_subset(X_ref, X_foc, n_strata=5, anchor_cols=None,
47	                  external_scores_ref=None, external_scores_foc=None):
48	    """
49	    Purified MH-DIF for all columns.
50	
51	    Stratification source (in priority order):
52	      1. external_scores_ref/foc — precomputed ability scores (e.g. full-matrix total)
53	      2. anchor_cols — total score from specified columns only
54	      3. None — standard purified (all cols minus current)
55	    """
56	    J = X_ref.shape[1]
57	    use_external = external_scores_ref is not None
58	
59	    if not use_external:
60	        if anchor_cols is not None:
61	            tot_ref = X_ref[:, anchor_cols].sum(axis=1).astype(np.float64)
62	            tot_foc = X_foc[:, anchor_cols].sum(axis=1).astype(np.float64)
63	            anchor_set = set(anchor_cols.tolist()) if hasattr(anchor_cols, 'tolist') else set(anchor_cols)
64	        else:
65	            tot_ref = X_ref.sum(axis=1).astype(np.float64)
66	            tot_foc = X_foc.sum(axis=1).astype(np.float64)
67	            anchor_set = None
68	
69	    rows = []
70	    for j in range(J):
71	        if use_external:
72	            s_ref = external_scores_ref
73	            s_foc = external_scores_foc
74	        elif anchor_set is not None:
75	            if j in anchor_set:
76	                s_ref = tot_ref - X_ref[:, j].astype(np.float64)
77	                s_foc = tot_foc - X_foc[:, j].astype(np.float64)
78	            else:
79	                s_ref = tot_ref
80	                s_foc = tot_foc
81	        else:
82	            s_ref = tot_ref - X_ref[:, j].astype(np.float64)
83	            s_foc = tot_foc - X_foc[:, j].astype(np.float64)
84	
85	        s_all = np.concatenate([s_ref, s_foc])
86	        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
87	        if len(edges) < 2:
88	            rows.append(_nan_row(j))
89	            continue
90	        n_bins = len(edges) - 1
91	
92	        k_ref = np.digitize(s_ref, edges[1:-1])
93	        k_foc = np.digitize(s_foc, edges[1:-1])
94	
95	        R = S = 0.0
96	        sum_diff = 0.0
97	        sum_var = 0.0
98	        pr = ps_qr = qs = 0.0
99	        n_ok = 0
100	
101	        for k in range(n_bins):
102	            mr = (k_ref == k)
103	            mf = (k_foc == k)
104	            n1 = int(mr.sum())
105	            n0 = int(mf.sum())
106	            if n1 == 0 or n0 == 0:
107	                continue
108	
109	            A = float(X_ref[mr, j].sum())
110	            B = float(n1 - A)
111	            C = float(X_foc[mf, j].sum())
112	            D = float(n0 - C)
113	            Nk = float(n1 + n0)
114	            m1 = A + C
115	            m0 = B + D
116	
117	            if m1 == 0 or m0 == 0 or Nk <= 1:
118	                continue
119	            n_ok += 1
120	
121	            Rk = A * D / Nk
122	            Sk = B * C / Nk
123	            R += Rk
124	            S += Sk
125	
126	            EA = n1 * m1 / Nk
127	            sum_diff += A - EA
128	            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))
129	
130	            Pk = (A + D) / Nk
131	            Qk = (B + C) / Nk
132	            pr += Pk * Rk
133	            ps_qr += Pk * Sk + Qk * Rk
134	            qs += Qk * Sk
135	
136	        if n_ok == 0 or (R == 0 and S == 0):
137	            rows.append(_nan_row(j))
138	            continue
139	
140	        if S == 0:
141	            alpha, delta, se = np.inf, -np.inf, np.nan
142	        elif R == 0:
143	            alpha, delta, se = 0.0, np.inf, np.nan
144	        else:
145	            alpha = R / S
146	            delta = -2.35 * np.log(alpha)
147	            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)
148	            se = 2.35 * np.sqrt(v) if v > 0 else np.nan
149	
150	        if sum_var > 0:
151	            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
152	            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
153	        else:
154	            chi2_stat = pval = np.nan
155	
156	        ad = abs(delta) if np.isfinite(delta) else np.inf
157	        if ad < 1.0:
158	            ets = "A"
159	        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:
160	            ets = "C"
161	        else:
162	            ets = "B"
163	
164	        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,
165	                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))
166	
167	    return pd.DataFrame(rows)
168	
169	
170	def _nan_row(j):
171	    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,
172	                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class="A")
173	
174	
175	# ════════════════════════════════════════════════════════════════════════════
176	#  DATA LOADING
177	# ════════════════════════════════════════════════════════════════════════════
178	print("=== Loading data ===")
179	mat = load_npz(BASE / "response_matrix.npz")
180	idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
181	MODEL_NAMES = idx["model_names"]
182	ITEM_IDS = idx["item_ids"]
183	ITEM2COL = {iid: i for i, iid in enumerate(ITEM_IDS)}
184	
185	model_meta = pd.read_csv(BASE / "model_metadata.csv")
186	li_labels = pd.read_csv(BASE / "mmlu_li2024_proxy_labels.csv")
187	ability_dif = pd.read_csv(BASE / "plan_001" / "dif_results_ability.csv")
188	
189	NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}
190	N_MODELS, J_FULL = mat.shape
191	print(f"  Matrix: {N_MODELS} × {J_FULL}")
192	
193	# Precompute full-matrix total scores (for external matching)
194	print("  Computing full-matrix total scores...")
195	full_totals = np.asarray(mat.sum(axis=1)).ravel().astype(np.float64)  # (5227,)
196	print(f"  Full total scores: mean={full_totals.mean():.1f}, "
197	      f"range=[{full_totals.min():.0f}, {full_totals.max():.0f}]")
198	
199	
200	# ════════════════════════════════════════════════════════════════════════════
201	#  STEP 1: SELECT BASELINE ITEMS
202	# ════════════════════════════════════════════════════════════════════════════
203	print("\n=== Step 1: Selecting baseline items ===")
204	merged = ability_dif.merge(li_labels[["item_id", "contamination_type"]], on="item_id", how="inner")
205	baseline_pool = merged[(merged["contamination_type"] == "clean") & (merged["ets_class"] == "A")]
206	print(f"  Baseline pool (clean + ETS A in ability DIF): {len(baseline_pool)}")
207	
208	baseline_items = baseline_pool.sample(N_BASELINE, random_state=42)
209	baseline_item_ids = baseline_items["item_id"].values
210	baseline_col_indices = np.array([ITEM2COL[iid] for iid in baseline_item_ids])
211	print(f"  Selected {N_BASELINE} baseline items")
212	
213	
214	# ════════════════════════════════════════════════════════════════════════════
215	#  STEP 2: DEFINE COHORTS
216	# ════════════════════════════════════════════════════════════════════════════
217	print("\n=== Step 2: Defining cohorts ===")
218	
219	
220	def get_row_indices(col, values):
221	    names = model_meta.loc[model_meta[col].isin(values), "model_name"]
222	    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])
223	
224	
225	cohort_defs = {}
226	
227	# (a) Ability cohort
228	ref_ability_idx = get_row_indices("cohort_accuracy_quintile", [1, 2])
229	foc_ability_idx = get_row_indices("cohort_accuracy_quintile", [4, 5])
230	
231	ref_acc = model_meta.loc[model_meta["cohort_accuracy_quintile"].isin([1, 2]), "accuracy"]
232	foc_acc = model_meta.loc[model_meta["cohort_accuracy_quintile"].isin([4, 5]), "accuracy"]
233	ab_overlap_min = max(ref_acc.min(), foc_acc.min())
234	ab_overlap_max = min(ref_acc.max(), foc_acc.max())
235	
236	if ab_overlap_min <= ab_overlap_max:
237	    foc_ab_inject_mask = (
238	        model_meta["cohort_accuracy_quintile"].isin([4, 5]) &
239	        (model_meta["accuracy"] >= ab_overlap_min) &
240	        (model_meta["accuracy"] <= ab_overlap_max)
241	    )
242	    foc_ab_inject_idx = np.array([NAME2ROW[n] for n in model_meta.loc[foc_ab_inject_mask, "model_name"] if n in NAME2ROW])
243	else:
244	    foc_ab_inject_idx = foc_ability_idx
245	
246	print(f"  Ability: ref={len(ref_ability_idx)} (Q1-2), foc={len(foc_ability_idx)} (Q4-5)")
247	print(f"    Accuracy overlap: [{ab_overlap_min:.4f}, {ab_overlap_max:.4f}]"
248	      f" → {'EMPTY, injecting all focal' if ab_overlap_min > ab_overlap_max else f'{len(foc_ab_inject_idx)} focal models'}")
249	
250	cohort_defs["ability"] = dict(
251	    ref_idx=ref_ability_idx, foc_idx=foc_ability_idx,
252	    foc_inject_idx=foc_ab_inject_idx
253	)
254	
255	# (b) Temporal cohort
256	ref_temporal_idx = get_row_indices("cohort_temporal", ["2023"])
257	foc_temporal_idx = get_row_indices("cohort_temporal", ["2024"])
258	
259	ref_t_acc = model_meta.loc[model_meta["cohort_temporal"] == "2023", "accuracy"]
260	foc_t_acc = model_meta.loc[model_meta["cohort_temporal"] == "2024", "accuracy"]
261	t_overlap_min = max(ref_t_acc.min(), foc_t_acc.min())
262	t_overlap_max = min(ref_t_acc.max(), foc_t_acc.max())
263	
264	foc_t_inject_mask = (
265	    (model_meta["cohort_temporal"] == "2024") &
266	    (model_meta["accuracy"] >= t_overlap_min) &
267	    (model_meta["accuracy"] <= t_overlap_max)
268	)
269	foc_t_inject_idx = np.array([NAME2ROW[n] for n in model_meta.loc[foc_t_inject_mask, "model_name"] if n in NAME2ROW])
270	
271	print(f"  Temporal: ref={len(ref_temporal_idx)} (2023), foc={len(foc_temporal_idx)} (2024)")
272	print(f"    Accuracy overlap: [{t_overlap_min:.4f}, {t_overlap_max:.4f}]"
273	      f" → {len(foc_t_inject_idx)} focal models for injection")
274	
275	cohort_defs["temporal"] = dict(
276	    ref_idx=ref_temporal_idx, foc_idx=foc_temporal_idx,
277	    foc_inject_idx=foc_t_inject_idx
278	)
279	
280	
281	# ════════════════════════════════════════════════════════════════════════════
282	#  STEP 3-4: INJECTION + MH-DIF
283	# ════════════════════════════════════════════════════════════════════════════
284	print("\n=== Step 3-4: Injection + MH-DIF ===")
285	
286	X_base = mat[:, baseline_col_indices].toarray().astype(np.int8)
287	print(f"  Baseline submatrix: {X_base.shape}, density: {X_base.mean():.4f}")
288	
289	injection_rows = []
290	per_item_rows = []
291	
292	MH_VARIANTS = ["standard", "anchor", "external"]
293	
294	total_runs = len(INJECTION_PS) * N_SEEDS * len(cohort_defs) * len(MH_VARIANTS)
295	run_count = 0
296	t_start = time.time()
297	
298	for cohort_name, cdef in cohort_defs.items():
299	    ref_idx = cdef["ref_idx"]
300	    foc_idx = cdef["foc_idx"]
301	    foc_inject_idx = cdef["foc_inject_idx"]
302	
303	    # External scores for this cohort (from full original matrix)
304	    ext_ref = full_totals[ref_idx]
305	    ext_foc = full_totals[foc_idx]
306	
307	    for p in INJECTION_PS:
308	        for seed in range(1, N_SEEDS + 1):
309	            rng = np.random.RandomState(seed)
310	
311	            contam_local_idx = rng.choice(N_BASELINE, N_CONTAMINATED, replace=False)
312	            contam_set = set(contam_local_idx.tolist())
313	            clean_local_idx = np.array([i for i in range(N_BASELINE) if i not in contam_set])
314	
315	            X_inj = X_base.copy()
316	            n_flipped = 0
317	
318	            if p > 0:
319	                for local_j in contam_local_idx:
320	                    for model_row in foc_inject_idx:
321	                        if X_inj[model_row, local_j] == 0:
322	                            if rng.random() < p:
323	                                X_inj[model_row, local_j] = 1
324	                                n_flipped += 1
325	
326	            orig_density = X_base[np.ix_(foc_inject_idx, contam_local_idx)].mean()
327	            new_density = X_inj[np.ix_(foc_inject_idx, contam_local_idx)].mean()
328	
329	            X_ref = X_inj[ref_idx]
330	            X_foc = X_inj[foc_idx]
331	
332	            for variant in MH_VARIANTS:
333	                run_count += 1
334	
335	                if variant == "anchor":
336	                    dif_results = mh_dif_subset(X_ref, X_foc, n_strata=5,
337	                                                anchor_cols=clean_local_idx)
338	                elif variant == "external":
339	                    dif_results = mh_dif_subset(X_ref, X_foc, n_strata=5,
340	                                                external_scores_ref=ext_ref,
341	                                                external_scores_foc=ext_foc)
342	                else:
343	                    dif_results = mh_dif_subset(X_ref, X_foc, n_strata=5)
344	
345	                contam_mask = dif_results["col_idx"].isin(contam_set)
346	                clean_mask = ~contam_mask
347	
348	                contam_results = dif_results[contam_mask]
349	                clean_results = dif_results[clean_mask]
350	
351	                n_c_contam = (contam_results["ets_class"] == "C").sum()
352	                n_c_clean = (clean_results["ets_class"] == "C").sum()
353	                tpr = n_c_contam / N_CONTAMINATED
354	                fpr = n_c_clean / (N_BASELINE - N_CONTAMINATED)
355	
356	                table = [[n_c_contam, N_CONTAMINATED - n_c_contam],
357	                         [n_c_clean, (N_BASELINE - N_CONTAMINATED) - n_c_clean]]
358	                fisher_or, fisher_p = fisher_exact(table)
359	
360	                injection_rows.append(dict(
361	                    p=p, seed=seed, cohort_type=cohort_name,
362	                    mh_variant=variant,
363	                    n_baseline=N_BASELINE, n_contaminated=N_CONTAMINATED,
364	                    n_clean=N_BASELINE - N_CONTAMINATED,
365	                    n_foc_inject=len(foc_inject_idx),
366	                    tpr=tpr, fpr=fpr,
367	                    fisher_or=fisher_or, fisher_p=fisher_p,
368	                    n_responses_flipped=n_flipped,
369	                    orig_density=orig_density, new_density=new_density,
370	                ))
371	
372	                # Per-item results only for anchor variant (keeps CSV manageable)
373	                if variant == "anchor":
374	                    for _, row in dif_results.iterrows():
375	                        local_j = int(row["col_idx"])
376	                        per_item_rows.append(dict(
377	                            item_id=baseline_item_ids[local_j],
378	                            p=p, seed=seed, cohort_type=cohort_name,
379	                            mh_variant=variant,
380	                            delta_mh=row["delta_mh"], p_value=row["p_value"],
381	                            ets_class=row["ets_class"],
382	                            is_injected=local_j in contam_set,
383	                        ))
384	
385	                elapsed = time.time() - t_start
386	                if variant == "external" or (variant == "standard" and p in [0.0, 1.0]):
387	                    print(f"  [{run_count}/{total_runs}] {cohort_name} {variant:8s} p={p} seed={seed}: "
388	                          f"TPR={tpr:.3f} FPR={fpr:.3f} flipped={n_flipped} "
389	                          f"({elapsed:.0f}s)")
390	
391	
392	# ════════════════════════════════════════════════════════════════════════════
393	#  STEP 5-6: AGGREGATE & SAVE
394	# ════════════════════════════════════════════════════════════════════════════
395	print("\n=== Step 5: Aggregating results ===")
396	
397	inj_df = pd.DataFrame(injection_rows)
398	per_item_df = pd.DataFrame(per_item_rows)
399	
400	summary_rows = []
401	for (p_val, cohort, variant), grp in inj_df.groupby(["p", "cohort_type", "mh_variant"]):
402	    summary_rows.append(dict(
403	        p=p_val, cohort_type=cohort, mh_variant=variant,
404	        tpr_mean=grp["tpr"].mean(), tpr_std=grp["tpr"].std(),
405	        fpr_mean=grp["fpr"].mean(), fpr_std=grp["fpr"].std(),
406	        fisher_or_mean=grp["fisher_or"].mean(),
407	        fisher_p_median=grp["fisher_p"].median(),
408	    ))
409	summary_df = pd.DataFrame(summary_rows)
410	
411	inj_df.to_csv(OUT / "injection_results.csv", index=False)
412	summary_df.to_csv(OUT / "dose_response_summary.csv", index=False)
413	per_item_df.to_csv(OUT / "per_item_results.csv", index=False)
414	print(f"  Saved injection_results.csv ({len(inj_df)} rows)")
415	print(f"  Saved dose_response_summary.csv ({len(summary_df)} rows)")
416	print(f"  Saved per_item_results.csv ({len(per_item_df)} rows)")
417	
418	
419	# ════════════════════════════════════════════════════════════════════════════
420	#  REPORT
421	# ════════════════════════════════════════════════════════════════════════════
422	print("\n=== Generating report ===")
423	
424	L = []
425	def w(s=""):
426	    L.append(s)
427	
428	w("# Plan 011: Semi-Synthetic DIF Validation")
429	w()
430	w("## 1. Objective")
431	w()
432	w("Inject known **differential** contamination into real MMLU response data and test")
433	w("whether MH-DIF can detect it. This validates whether plan_001/001b's failure to find")
434	w("enrichment was due to Li et al. labels being non-differential (global contamination)")
435	w("rather than a fundamental limitation of MH-DIF.")
436	w()
437	
438	w("## 2. Setup")
439	w()
440	w(f"- **Baseline items**: {N_BASELINE} (clean in Li et al. + ETS A in plan_001 ability DIF)")
441	w(f"- **Contaminated per run**: {N_CONTAMINATED} of {N_BASELINE}")
442	w(f"- **Injection probabilities**: {INJECTION_PS}")
443	w(f"- **Seeds per p**: {N_SEEDS}")
444	w()
445	w("### Cohort definitions")
446	w()
447	for cn, cd in cohort_defs.items():
448	    w(f"- **{cn}**: ref N={len(cd['ref_idx'])}, foc N={len(cd['foc_idx'])}, "
449	      f"foc inject N={len(cd['foc_inject_idx'])}")
450	w()
451	
452	if ab_overlap_min > ab_overlap_max:
453	    w("> **Note**: Ability quintiles (Q1-2 vs Q4-5) have no accuracy overlap by construction "
454	      f"(ref max={ref_acc.max():.4f}, foc min={foc_acc.min():.4f}). "
455	      "All focal models used for injection. MH stratification handles ability matching.")
456	    w()
457	
458	w("### MH variants")
459	w()
460	w("| Variant | Matching variable | Rationale |")
461	w("|---------|-------------------|-----------|")
462	w("| standard | sum of 500 items − current | Same as plan_001; susceptible to matching variable contamination when 20% items injected |")
463	w("| anchor | sum of 400 known-clean items | Eliminates matching variable contamination; assumes oracle knowledge of clean items |")
464	w("| external | sum of all 12,508 items (original, pre-injection) | Best matching precision; immune to injection; requires external ability estimate |")
465	w()
466	
467	w("## 3. Results by MH Variant")
468	w()
469	for variant in MH_VARIANTS:
470	    w(f"### {variant.capitalize()} MH")
471	    w()
472	    w("| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |")
473	    w("|--------|---|----------------|----------------|------|-----------|----------|")
474	    sub = summary_df[summary_df["mh_variant"] == variant]
475	    for _, r in sub.sort_values(["cohort_type", "p"]).iterrows():
476	        # ΔTPR = TPR - baseline TPR at p=0
477	        base_tpr = sub[(sub["cohort_type"] == r.cohort_type) & (sub["p"] == 0.0)]["tpr_mean"].values
478	        d_tpr = r.tpr_mean - base_tpr[0] if len(base_tpr) > 0 else 0
479	        w(f"| {r.cohort_type} | {r.p} | {r.tpr_mean:.3f}±{r.tpr_std:.3f} | "
480	          f"{r.fpr_mean:.3f}±{r.fpr_std:.3f} | {d_tpr:+.3f} | "
481	          f"{r.fisher_or_mean:.2f} | {r.fisher_p_median:.4f} |")
482	    w()
483	
484	w("## 4. Key Comparison: Baseline FPR by Variant")
485	w()
486	w("| Cohort | standard | anchor | external |")
487	w("|--------|----------|--------|----------|")
488	for cohort in ["ability", "temporal"]:
489	    vals = []
490	    for variant in MH_VARIANTS:
491	        r = summary_df[(summary_df["p"] == 0.0) & (summary_df["cohort_type"] == cohort) &
492	                       (summary_df["mh_variant"] == variant)]
493	        vals.append(f"{r.iloc[0]['fpr_mean']:.3f}" if len(r) > 0 else "—")
494	    w(f"| {cohort} | {vals[0]} | {vals[1]} | {vals[2]} |")
495	w()
496	w("If external FPR ≪ standard FPR, the high baseline rate is from matching precision,")
497	w("not inherent DIF in the selected items.")
498	w()
499	
500	w("## 5. Sanity Checks")
501	w()
502	w("### Density change (focal × contaminated items)")
503	w()
504	w("| Cohort | p | Orig density | Post density | Responses flipped |")
505	w("|--------|---|--------------|--------------|-------------------|")
506	for (p_val, cohort), grp in inj_df[inj_df["mh_variant"] == "standard"].groupby(["p", "cohort_type"]):
507	    if p_val == 0:
508	        continue
509	    w(f"| {cohort} | {p_val} | {grp['orig_density'].mean():.4f} | "
510	      f"{grp['new_density'].mean():.4f} | {grp['n_responses_flipped'].mean():.0f} |")
511	w()
512	
513	w("## 6. Verdict")
514	w()
515	
516	for variant in MH_VARIANTS:
517	    w(f"### {variant.capitalize()} MH")
518	    w()
519	    sub = summary_df[summary_df["mh_variant"] == variant]
520	
521	    for cohort in ["ability", "temporal"]:
522	        c_sub = sub[sub["cohort_type"] == cohort]
523	        p0 = c_sub[c_sub["p"] == 0.0]
524	        p1 = c_sub[c_sub["p"] == 1.0]
525	        if len(p1) == 0 or len(p0) == 0:
526	            continue
527	
528	        fpr0 = p0.iloc[0]["fpr_mean"]
529	        tpr0 = p0.iloc[0]["tpr_mean"]
530	        tpr1 = p1.iloc[0]["tpr_mean"]
531	        fpr1 = p1.iloc[0]["fpr_mean"]
532	        d_tpr = tpr1 - tpr0
533	
534	        w(f"**{cohort}**: baseline TPR={tpr0:.3f}/FPR={fpr0:.3f}, "
535	          f"p=1.0 TPR={tpr1:.3f}/FPR={fpr1:.3f}, ΔTPR={d_tpr:+.3f}")
536	
537	        if d_tpr > 0.3 and tpr1 > 0.5:
538	            w(f"→ **SUCCESS**: injection raises TPR by {d_tpr:.3f} with clear dose-response")
539	        elif d_tpr > 0.1:
540	            w(f"→ **PARTIAL**: detectable signal (ΔTPR={d_tpr:.3f}) but modest")
541	        else:
542	            w(f"→ **FAIL**: ΔTPR={d_tpr:.3f} too small to indicate detection")
543	        w()
544	
545	w("## 7. Overall Interpretation")
546	w()
547	w("### Does MH-DIF detect differential contamination?")
548	w()
549	
550	# Compute key numbers for conclusion
551	ext_t = summary_df[(summary_df["mh_variant"] == "external") & (summary_df["cohort_type"] == "temporal")]
552	ext_a = summary_df[(summary_df["mh_variant"] == "external") & (summary_df["cohort_type"] == "ability")]
553	
554	if len(ext_t) > 0:
555	    ext_t_p0 = ext_t[ext_t["p"] == 0.0]["tpr_mean"].values[0]
556	    ext_t_p1 = ext_t[ext_t["p"] == 1.0]["tpr_mean"].values[0]
557	    ext_t_fpr0 = ext_t[ext_t["p"] == 0.0]["fpr_mean"].values[0]
558	    ext_t_fpr1 = ext_t[ext_t["p"] == 1.0]["fpr_mean"].values[0]
559	    w(f"- **Temporal + external matching**: TPR rises {ext_t_p0:.3f} → {ext_t_p1:.3f} "
560	      f"(ΔTPR=+{ext_t_p1-ext_t_p0:.3f}), FPR {ext_t_fpr0:.3f} → {ext_t_fpr1:.3f}")
561	
562	if len(ext_a) > 0:
563	    ext_a_p0 = ext_a[ext_a["p"] == 0.0]["tpr_mean"].values[0]
564	    ext_a_p1 = ext_a[ext_a["p"] == 1.0]["tpr_mean"].values[0]
565	    ext_a_fpr0 = ext_a[ext_a["p"] == 0.0]["fpr_mean"].values[0]
566	    ext_a_fpr1 = ext_a[ext_a["p"] == 1.0]["fpr_mean"].values[0]
567	    w(f"- **Ability + external matching**: TPR rises {ext_a_p0:.3f} → {ext_a_p1:.3f} "
568	      f"(ΔTPR=+{ext_a_p1-ext_a_p0:.3f}), FPR {ext_a_fpr0:.3f} → {ext_a_fpr1:.3f}")
569	
570	w()
571	w("### Implications for plan_001")
572	w()
573	w("If semi-synthetic injection is detectable → plan_001's failure to find enrichment")
574	w("against Li et al. labels is because Li et al. contamination is **non-differential**")
575	w("(Common Crawl data available to all models), not because MH-DIF is fundamentally limited.")
576	w()
577	w("### Matching variable contamination")
578	w()
579	w("When 20% of items are injected, standard MH's matching variable (total score) is")
580	w("corrupted by injected items, inflating FPR. This is a known limitation when DIF items")
581	w("constitute a large fraction of the test. In practice, iterative purification (exclude")
582	w("suspected DIF items from matching) or external ability estimates mitigate this.")
583	w()
584	
585	(OUT / "plan_011_report.md").write_text("\n".join(L) + "\n")
586	print("  Report written.")
587	
588	# Console summary
589	print("\n" + "=" * 60)
590	print("SUMMARY")
591	print("=" * 60)
592	for variant in MH_VARIANTS:
593	    print(f"\n--- {variant} MH ---")
594	    sub = summary_df[summary_df["mh_variant"] == variant]
595	    for _, r in sub.sort_values(["cohort_type", "p"]).iterrows():
596	        print(f"  {r.cohort_type:8s} p={r.p}: TPR={r.tpr_mean:.3f}±{r.tpr_std:.3f}  "
597	              f"FPR={r.fpr_mean:.3f}±{r.fpr_std:.3f}")
598	
599	total_elapsed = time.time() - t_start
600	print(f"\nTotal time: {total_elapsed:.0f}s")
601	print(f"All outputs saved to {OUT}")
602	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "ebd2d900-68a5-4606-a0ce-f436e884f44a"
}
```

</details>

---

### System

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa73b16fd4338b1af",
  "tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "description": "Reading artifacts/plan_016/plan_016_within_subject_injection.py",
  "usage": {
    "total_tokens": 28755,
    "tool_uses": 4,
    "duration_ms": 7312
  },
  "last_tool_name": "Read",
  "uuid": "c13a46a1-0776-4a82-8c3a-dec70e065342",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_015D55hJ5mKC8GWxXuVPFMvy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_within_subject_injection.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "35882a73-9856-423a-bc41-bfd236ce4356",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MYMA1PRR6jQS3xSvRqYp3v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 10283,
      "cache_read_input_tokens": 18449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10283,
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

_source line 20 · 2026-05-21T15:45:36.224Z_

<details><summary>↩ Tool result · `toolu_015D55hJ5mKC8GWxXuVPFMvy`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_016: Within-Subject Semi-Synthetic Injection
4	
5	For each of 5 selected MMLU subjects, inject differential contamination into
6	the temporal focal group (2024 models) and test whether within-subject MH-DIF
7	detects the injected signal.
8	
9	Subjects: business_ethics (93), human_aging (203), professional_medicine (248),
10	          formal_logic (109), high_school_statistics (181)
11	Injection: 20% items contaminated, p ∈ {0.0, 0.5, 1.0}, 5 seeds
12	Matching: within-subject purified total score + cross-subject total score
13	"""
14	
15	import numpy as np
16	import pandas as pd
17	from scipy.sparse import load_npz
18	from scipy.stats import chi2 as chi2_dist, fisher_exact
19	from pathlib import Path
20	import time
21	import warnings
22	
23	warnings.filterwarnings("ignore", category=RuntimeWarning)
24	
25	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
26	OUT = BASE / "plan_016"
27	OUT.mkdir(exist_ok=True)
28	
29	SUBJECTS = ["business_ethics", "human_aging", "professional_medicine",
30	            "formal_logic", "high_school_statistics"]
31	INJECTION_PS = [0.0, 0.5, 1.0]
32	N_SEEDS = 5
33	CONTAM_FRAC = 0.20
34	N_STRATA = 5
35	MIN_PER_STRATUM = 5
36	
37	
38	# ════════════════════════════════════════════════════════════════════════════
39	#  MH-DIF CORE (from plan_014 with strata merging + external score support)
40	# ════════════════════════════════════════════════════════════════════════════
41	def purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,
42	                    external_scores_foc=None, min_per_stratum=5):
43	    J = X_ref.shape[1]
44	    use_external = external_scores_ref is not None
45	
46	    if not use_external:
47	        tot_ref = X_ref.sum(axis=1).astype(np.float64)
48	        tot_foc = X_foc.sum(axis=1).astype(np.float64)
49	
50	    rows = []
51	    for j in range(J):
52	        if use_external:
53	            s_ref = external_scores_ref.astype(np.float64)
54	            s_foc = external_scores_foc.astype(np.float64)
55	        else:
56	            s_ref = tot_ref - X_ref[:, j].astype(np.float64)
57	            s_foc = tot_foc - X_foc[:, j].astype(np.float64)
58	
59	        s_all = np.concatenate([s_ref, s_foc])
60	        groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])
61	
62	        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
63	        if len(edges) < 2:
64	            rows.append(_nan_row(j))
65	            continue
66	
67	        n_bins = len(edges) - 1
68	        k_all = np.digitize(s_all, edges[1:-1])
69	        strata_labels = _merge_small_strata(k_all, groups_all, n_bins, min_per_stratum)
70	
71	        R = S = 0.0
72	        sum_diff = 0.0
73	        sum_var = 0.0
74	        pr = ps_qr = qs = 0.0
75	        n_ok = 0
76	
77	        x_all = np.concatenate([X_ref[:, j], X_foc[:, j]])
78	
79	        for k in np.unique(strata_labels):
80	            mask_k = (strata_labels == k)
81	            mask_ref = mask_k & (groups_all == 0)
82	            mask_foc = mask_k & (groups_all == 1)
83	
84	            n1 = int(mask_ref.sum())
85	            n0 = int(mask_foc.sum())
86	            if n1 == 0 or n0 == 0:
87	                continue
88	
89	            A = float(x_all[mask_ref].sum())
90	            B = float(n1 - A)
91	            C = float(x_all[mask_foc].sum())
92	            D = float(n0 - C)
93	            Nk = float(n1 + n0)
94	            m1 = A + C
95	            m0 = B + D
96	
97	            if m1 == 0 or m0 == 0 or Nk <= 1:
98	                continue
99	            n_ok += 1
100	
101	            Rk = A * D / Nk
102	            Sk = B * C / Nk
103	            R += Rk
104	            S += Sk
105	
106	            EA = n1 * m1 / Nk
107	            sum_diff += A - EA
108	            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))
109	
110	            Pk = (A + D) / Nk
111	            Qk = (B + C) / Nk
112	            pr += Pk * Rk
113	            ps_qr += Pk * Sk + Qk * Rk
114	            qs += Qk * Sk
115	
116	        if n_ok == 0 or (R == 0 and S == 0):
117	            rows.append(_nan_row(j))
118	            continue
119	
120	        if S == 0:
121	            alpha, delta, se = np.inf, -np.inf, np.nan
122	        elif R == 0:
123	            alpha, delta, se = 0.0, np.inf, np.nan
124	        else:
125	            alpha = R / S
126	            delta = -2.35 * np.log(alpha)
127	            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)
128	            se = 2.35 * np.sqrt(v) if v > 0 else np.nan
129	
130	        if sum_var > 0:
131	            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
132	            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
133	        else:
134	            chi2_stat = pval = np.nan
135	
136	        ad = abs(delta) if np.isfinite(delta) else np.inf
137	        if ad < 1.0:
138	            ets = "A"
139	        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:
140	            ets = "C"
141	        else:
142	            ets = "B"
143	
144	        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,
145	                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets,
146	                         n_strata_used=n_ok))
147	
148	    return pd.DataFrame(rows)
149	
150	
151	def _nan_row(j):
152	    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,
153	                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class="A",
154	                n_strata_used=0)
155	
156	
157	def _merge_small_strata(k_all, groups_all, n_bins, min_n):
158	    labels = k_all.copy()
159	    merged = True
160	    while merged:
161	        merged = False
162	        unique_strata = sorted(np.unique(labels))
163	        for i, k in enumerate(unique_strata):
164	            mask_k = (labels == k)
165	            n_ref = int((mask_k & (groups_all == 0)).sum())
166	            n_foc = int((mask_k & (groups_all == 1)).sum())
167	            if n_ref < min_n or n_foc < min_n:
168	                if i + 1 < len(unique_strata):
169	                    next_k = unique_strata[i + 1]
170	                    labels[labels == next_k] = k
171	                elif i > 0:
172	                    prev_k = unique_strata[i - 1]
173	                    labels[labels == k] = prev_k
174	                merged = True
175	                break
176	    return labels
177	
178	
179	# ════════════════════════════════════════════════════════════════════════════
180	#  DATA LOADING
181	# ════════════════════════════════════════════════════════════════════════════
182	print("=== Loading data ===")
183	t0 = time.time()
184	
185	mat = load_npz(BASE / "response_matrix.npz")
186	idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
187	MODEL_NAMES = idx["model_names"]
188	ITEM_IDS = idx["item_ids"]
189	ITEM2COL = {iid: i for i, iid in enumerate(ITEM_IDS)}
190	
191	model_meta = pd.read_csv(BASE / "model_metadata.csv")
192	item_meta = pd.read_csv(BASE / "item_metadata.csv")
193	
194	NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}
195	print(f"  Matrix: {mat.shape[0]} x {mat.shape[1]}  ({time.time()-t0:.1f}s)")
196	
197	# Temporal cohorts
198	ref_names = model_meta.loc[model_meta["cohort_temporal"] == "2023", "model_name"]
199	foc_names = model_meta.loc[model_meta["cohort_temporal"] == "2024", "model_name"]
200	ref_rows = np.array([NAME2ROW[n] for n in ref_names if n in NAME2ROW])
201	foc_rows = np.array([NAME2ROW[n] for n in foc_names if n in NAME2ROW])
202	
203	# Focal injection subset: 2024 models in ability overlap with 2023
204	ref_acc = model_meta.loc[model_meta["cohort_temporal"] == "2023", "accuracy"]
205	foc_acc = model_meta.loc[model_meta["cohort_temporal"] == "2024", "accuracy"]
206	t_overlap_min = max(ref_acc.min(), foc_acc.min())
207	t_overlap_max = min(ref_acc.max(), foc_acc.max())
208	
209	foc_inject_mask = (
210	    (model_meta["cohort_temporal"] == "2024") &
211	    (model_meta["accuracy"] >= t_overlap_min) &
212	    (model_meta["accuracy"] <= t_overlap_max)
213	)
214	foc_inject_rows = np.array([NAME2ROW[n] for n in model_meta.loc[foc_inject_mask, "model_name"] if n in NAME2ROW])
215	
216	print(f"  Temporal: ref(2023)={len(ref_rows)}, foc(2024)={len(foc_rows)}, foc_inject={len(foc_inject_rows)}")
217	
218	
219	# ════════════════════════════════════════════════════════════════════════════
220	#  INJECTION + DETECTION
221	# ════════════════════════════════════════════════════════════════════════════
222	print("\n=== Running within-subject injection (within + cross matching) ===")
223	
224	MATCHING_TYPES = ["within", "cross"]
225	injection_rows = []
226	total_runs = len(SUBJECTS) * len(INJECTION_PS) * N_SEEDS * len(MATCHING_TYPES)
227	run_count = 0
228	
229	for subj_name in SUBJECTS:
230	    subj_items = item_meta[item_meta["subject"] == subj_name]["item_id"].values
231	    subj_cols = np.array([ITEM2COL[iid] for iid in subj_items if iid in ITEM2COL])
232	    n_items = len(subj_cols)
233	    n_contam = max(1, int(n_items * CONTAM_FRAC))
234	    n_baseline = n_items - n_contam
235	
236	    n_strata = 3 if n_items < 100 else N_STRATA
237	
238	    # Full subject response submatrix (all models, subject items only)
239	    X_subj = mat[:, subj_cols].toarray().astype(np.int8)
240	
241	    # Cross-subject columns: all items NOT in current subject
242	    subj_items_set = set(subj_items.tolist())
243	    other_cols = np.array([ITEM2COL[iid] for iid in ITEM_IDS
244	                           if iid in ITEM2COL and iid not in subj_items_set])
245	
246	    # Precompute cross-subject base scores from the original (uninjected) matrix
247	    cross_ref_base = np.asarray(mat[ref_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)
248	    cross_foc_base = np.asarray(mat[foc_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)
249	
250	    print(f"\n--- {subj_name}: {n_items} items, {n_contam} contaminated, {n_strata} strata, "
251	          f"{len(other_cols)} cross-items ---")
252	
253	    for p in INJECTION_PS:
254	        for seed in range(1, N_SEEDS + 1):
255	            rng = np.random.RandomState(seed)
256	
257	            # Split: random 20% contaminated
258	            contam_local_idx = rng.choice(n_items, n_contam, replace=False)
259	            contam_set = set(contam_local_idx.tolist())
260	
261	            # Inject: flip incorrect→correct for focal inject models on contaminated items
262	            X_inj = X_subj.copy()
263	            n_flipped = 0
264	
265	            if p > 0:
266	                for local_j in contam_local_idx:
267	                    for model_row in foc_inject_rows:
268	                        if X_inj[model_row, local_j] == 0:
269	                            if rng.random() < p:
270	                                X_inj[model_row, local_j] = 1
271	                                n_flipped += 1
272	
273	            X_ref = X_inj[ref_rows]
274	            X_foc = X_inj[foc_rows]
275	
276	            for matching_type in MATCHING_TYPES:
277	                run_count += 1
278	
279	                if matching_type == "within":
280	                    dif_results = purified_mh_dif(X_ref, X_foc, n_strata=n_strata,
281	                                                  min_per_stratum=MIN_PER_STRATUM)
282	                else:
283	                    dif_results = purified_mh_dif(X_ref, X_foc, n_strata=n_strata,
284	                                                  external_scores_ref=cross_ref_base,
285	                                                  external_scores_foc=cross_foc_base,
286	                                                  min_per_stratum=MIN_PER_STRATUM)
287	
288	                # TPR / FPR
289	                contam_mask = dif_results["col_idx"].isin(contam_set)
290	                contam_results = dif_results[contam_mask]
291	                clean_results = dif_results[~contam_mask]
292	
293	                n_c_contam = (contam_results["ets_class"] == "C").sum()
294	                n_c_clean = (clean_results["ets_class"] == "C").sum()
295	                tpr = n_c_contam / n_contam if n_contam > 0 else 0
296	                fpr = n_c_clean / n_baseline if n_baseline > 0 else 0
297	
298	                table = [[n_c_contam, n_contam - n_c_contam],
299	                         [n_c_clean, n_baseline - n_c_clean]]
300	                fisher_or, fisher_p = fisher_exact(table)
301	
302	                injection_rows.append(dict(
303	                    subject=subj_name, p=p, seed=seed,
304	                    matching_type=matching_type,
305	                    n_items=n_items, n_baseline=n_baseline, n_contaminated=n_contam,
306	                    n_flipped=n_flipped,
307	                    tpr=tpr, fpr=fpr,
308	                    n_c_contam=n_c_contam, n_c_clean=n_c_clean,
309	                    fisher_or=fisher_or, fisher_p=fisher_p,
310	                ))
311	
312	                print(f"  [{run_count}/{total_runs}] {subj_name} p={p} seed={seed} {matching_type}: "
313	                      f"TPR={tpr:.3f} FPR={fpr:.3f} flipped={n_flipped} Fisher p={fisher_p:.4f}")
314	
315	
316	# ════════════════════════════════════════════════════════════════════════════
317	#  AGGREGATE
318	# ════════════════════════════════════════════════════════════════════════════
319	print("\n=== Aggregating ===")
320	
321	inj_df = pd.DataFrame(injection_rows)
322	inj_df.to_csv(OUT / "within_subject_injection_results.csv", index=False)
323	print(f"  Saved within_subject_injection_results.csv ({len(inj_df)} rows)")
324	
325	# Dose-response summary (per subject × p × matching_type)
326	summary_rows = []
327	for (subj, p_val, mt), grp in inj_df.groupby(["subject", "p", "matching_type"]):
328	    base_tpr = inj_df[(inj_df["subject"] == subj) & (inj_df["p"] == 0.0) &
329	                       (inj_df["matching_type"] == mt)]["tpr"].mean()
330	    d_tpr = grp["tpr"].mean() - base_tpr
331	
332	    summary_rows.append(dict(
333	        subject=subj, p=p_val, matching_type=mt,
334	        tpr_mean=grp["tpr"].mean(), tpr_std=grp["tpr"].std(),
335	        fpr_mean=grp["fpr"].mean(), fpr_std=grp["fpr"].std(),
336	        delta_tpr=d_tpr,
337	        fisher_or_mean=grp["fisher_or"].mean(),
338	        fisher_p_median=grp["fisher_p"].median(),
339	    ))
340	
341	summary_df = pd.DataFrame(summary_rows)
342	summary_df.to_csv(OUT / "within_subject_dose_response.csv", index=False)
343	print(f"  Saved within_subject_dose_response.csv ({len(summary_df)} rows)")
344	
345	
346	# ════════════════════════════════════════════════════════════════════════════
347	#  REPORT
348	# ════════════════════════════════════════════════════════════════════════════
349	print("\n=== Generating report ===")
350	
351	L = []
352	def w(s=""):
353	    L.append(s)
354	
355	w("# Plan 016: Within-Subject Semi-Synthetic Injection")
356	w()
357	w("## Objective")
358	w()
359	w("Verify that MH-DIF detects differential contamination **within individual subjects**,")
360	w("not just globally. This validates plan_014's finding that within-subject temporal")
361	w("C% = 38.1% reflects real signal, not method failure.")
362	w()
363	
364	w("## Setup")
365	w()
366	w(f"- **Temporal cohort**: ref=2023 ({len(ref_rows)} models), foc=2024 ({len(foc_rows)} models)")
367	w(f"- **Focal injection subset**: {len(foc_inject_rows)} models (ability overlap with ref)")
368	w(f"- **Contamination fraction**: {CONTAM_FRAC*100:.0f}% of items per subject")
369	w(f"- **Injection probabilities**: {INJECTION_PS}")
370	w(f"- **Seeds per p**: {N_SEEDS}")
371	w(f"- **Matching**: within-subject purified total score + cross-subject total score")
372	w()
373	
374	w("### Subjects")
375	w()
376	w("| Subject | N items | N contaminated | N baseline | Strata |")
377	w("|---------|---------|----------------|------------|--------|")
378	for subj in SUBJECTS:
379	    sub = inj_df[inj_df["subject"] == subj].iloc[0]
380	    n_strata = 3 if sub["n_items"] < 100 else N_STRATA
381	    w(f"| {subj} | {sub['n_items']} | {sub['n_contaminated']} | {sub['n_baseline']} | {n_strata} |")
382	w()
383	
384	# === Within-subject results ===
385	w("## Results: Within-Subject Matching")
386	w()
387	w("Matching variable = purified total score on current subject's items (minus studied item).")
388	w()
389	w("### Per-Subject Dose-Response (Within)")
390	w()
391	w("| Subject | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |")
392	w("|---------|---|----------------|----------------|------|-----------|----------|")
393	within_summary = summary_df[summary_df["matching_type"] == "within"]
394	for _, r in within_summary.sort_values(["subject", "p"]).iterrows():
395	    w(f"| {r.subject} | {r.p} | {r.tpr_mean:.3f}±{r.tpr_std:.3f} | "
396	      f"{r.fpr_mean:.3f}±{r.fpr_std:.3f} | {r.delta_tpr:+.3f} | "
397	      f"{r.fisher_or_mean:.2f} | {r.fisher_p_median:.4f} |")
398	w()
399	
400	# === Cross-subject results ===
401	w("## Results: Cross-Subject Matching")
402	w()
403	w("Matching variable = total score on all other subjects' items (not affected by injection).")
404	w()
405	w("### Per-Subject Dose-Response (Cross)")
406	w()
407	w("| Subject | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |")
408	w("|---------|---|----------------|----------------|------|-----------|----------|")
409	cross_summary = summary_df[summary_df["matching_type"] == "cross"]
410	for _, r in cross_summary.sort_values(["subject", "p"]).iterrows():
411	    w(f"| {r.subject} | {r.p} | {r.tpr_mean:.3f}±{r.tpr_std:.3f} | "
412	      f"{r.fpr_mean:.3f}±{r.fpr_std:.3f} | {r.delta_tpr:+.3f} | "
413	      f"{r.fisher_or_mean:.2f} | {r.fisher_p_median:.4f} |")
414	w()
415	
416	# === Within vs Cross comparison ===
417	w("## Within vs Cross Matching Comparison")
418	w()
419	w("| Subject | p | Within FPR | Cross FPR | Within TPR | Cross TPR |")
420	w("|---------|---|------------|-----------|------------|-----------|")
421	for subj in SUBJECTS:
422	    for p_val in INJECTION_PS:
423	        ws = within_summary[(within_summary["subject"] == subj) & (within_summary["p"] == p_val)]
424	        cs = cross_summary[(cross_summary["subject"] == subj) & (cross_summary["p"] == p_val)]
425	        if len(ws) > 0 and len(cs) > 0:
426	            ws = ws.iloc[0]
427	            cs = cs.iloc[0]
428	            w(f"| {subj} | {p_val} | {ws.fpr_mean:.3f} | {cs.fpr_mean:.3f} | "
429	              f"{ws.tpr_mean:.3f} | {cs.tpr_mean:.3f} |")
430	w()
431	
432	# FPR stability analysis
433	w("### FPR Stability: Within vs Cross")
434	w()
435	w("| Subject | Within FPR(p=0) | Within FPR(p=1) | ΔFPR(within) | Cross FPR(p=0) | Cross FPR(p=1) | ΔFPR(cross) |")
436	w("|---------|-----------------|-----------------|--------------|----------------|----------------|-------------|")
437	for subj in SUBJECTS:
438	    w0 = within_summary[(within_summary["subject"] == subj) & (within_summary["p"] == 0.0)]
439	    w1 = within_summary[(within_summary["subject"] == subj) & (within_summary["p"] == 1.0)]
440	    c0 = cross_summary[(cross_summary["subject"] == subj) & (cross_summary["p"] == 0.0)]
441	    c1 = cross_summary[(cross_summary["subject"] == subj) & (cross_summary["p"] == 1.0)]
442	    if len(w0) > 0 and len(w1) > 0 and len(c0) > 0 and len(c1) > 0:
443	        w0, w1, c0, c1 = w0.iloc[0], w1.iloc[0], c0.iloc[0], c1.iloc[0]
444	        d_within = w1.fpr_mean - w0.fpr_mean
445	        d_cross = c1.fpr_mean - c0.fpr_mean
446	        w(f"| {subj} | {w0.fpr_mean:.3f} | {w1.fpr_mean:.3f} | {d_within:+.3f} | "
447	          f"{c0.fpr_mean:.3f} | {c1.fpr_mean:.3f} | {d_cross:+.3f} |")
448	w()
449	
450	# === Subject-Level Summary ===
451	w("### Subject-Level Summary")
452	w()
453	w("| Subject | Matching | Baseline FPR (p=0) | TPR at p=0.5 | TPR at p=1.0 | ΔTPR(0.5) | ΔTPR(1.0) | Significant? |")
454	w("|---------|----------|--------------------|--------------|--------------|-----------|-----------|-------------|")
455	
456	n_success_within = 0
457	n_success_cross = 0
458	for subj in SUBJECTS:
459	    for mt in MATCHING_TYPES:
460	        s = summary_df[(summary_df["subject"] == subj) & (summary_df["matching_type"] == mt)]
461	        if len(s) < 3:
462	            continue
463	        p0 = s[s["p"] == 0.0].iloc[0]
464	        p05 = s[s["p"] == 0.5].iloc[0]
465	        p10 = s[s["p"] == 1.0].iloc[0]
466	
467	        sig_05 = "Yes" if p05["fisher_p_median"] < 0.05 else "No"
468	        sig_10 = "Yes" if p10["fisher_p_median"] < 0.05 else "No"
469	        sig = f"{sig_05} / {sig_10}"
470	
471	        if p05["delta_tpr"] > 0.3:
472	            if mt == "within":
473	                n_success_within += 1
474	            else:
475	                n_success_cross += 1
476	
477	        w(f"| {subj} | {mt} | {p0['fpr_mean']:.3f} | {p05['tpr_mean']:.3f} | {p10['tpr_mean']:.3f} | "
478	          f"{p05['delta_tpr']:+.3f} | {p10['delta_tpr']:+.3f} | {sig} |")
479	w()
480	
481	w("## Comparison with Plan 011 (Global)")
482	w()
483	w("| Metric | Plan 011 temporal external | Plan 016 within (avg) | Plan 016 cross (avg) |")
484	w("|--------|---------------------------|----------------------|---------------------|")
485	
486	avg_fpr_within = within_summary[within_summary["p"] == 0.0]["fpr_mean"].mean()
487	avg_dtpr_05_within = within_summary[within_summary["p"] == 0.5]["delta_tpr"].mean()
488	avg_dtpr_10_within = within_summary[within_summary["p"] == 1.0]["delta_tpr"].mean()
489	
490	avg_fpr_cross = cross_summary[cross_summary["p"] == 0.0]["fpr_mean"].mean()
491	avg_dtpr_05_cross = cross_summary[cross_summary["p"] == 0.5]["delta_tpr"].mean()
492	avg_dtpr_10_cross = cross_summary[cross_summary["p"] == 1.0]["delta_tpr"].mean()
493	
494	w(f"| Baseline FPR | 0.314 | {avg_fpr_within:.3f} | {avg_fpr_cross:.3f} |")
495	w(f"| ΔTPR at p=0.5 | +0.508 | {avg_dtpr_05_within:+.3f} | {avg_dtpr_05_cross:+.3f} |")
496	w(f"| ΔTPR at p=1.0 | +0.674 | {avg_dtpr_10_within:+.3f} | {avg_dtpr_10_cross:+.3f} |")
497	w()
498	
499	w("## Verdict")
500	w()
501	w(f"**Within-subject matching**: {n_success_within}/{len(SUBJECTS)} subjects with ΔTPR > 0.3 at p=0.5")
502	w(f"**Cross-subject matching**: {n_success_cross}/{len(SUBJECTS)} subjects with ΔTPR > 0.3 at p=0.5")
503	w()
504	
505	w("Within-subject MH-DIF successfully detects injected differential contamination")
506	w("in subjects with sufficient items. Cross-subject matching provides a cleaner")
507	w("baseline FPR (not inflated by injection in the matching variable) while")
508	w("maintaining detection sensitivity.")
509	w()
510	
511	w("Key findings:")
512	w()
513	w("1. The DIF methodology works at the within-subject level")
514	w("2. Plan 014's finding of ~38% within-subject temporal C% is methodologically valid")
515	w("3. Cross-subject matching FPR is more stable across injection levels (not contaminated)")
516	w("4. Within-subject matching FPR inflates with injection (matching variable includes injected items)")
517	w("5. Very small subjects (N<100) have inflated baseline FPR due to limited matching variable precision")
518	w()
519	
520	w("## Implications")
521	w()
522	w("The within-subject injection results, combined with plan_014's finding of ~38%")
523	w("within-subject C%, support the final narrative: temporal DIF is a real, pervasive")
524	w("phenomenon that persists even when ability matching is done within content domains.")
525	w("Cross-subject matching confirms the FPR inflation in within-subject matching is due")
526	w("to contamination of the matching variable, validating the use of external scores")
527	w("for cleaner DIF estimation.")
528	
529	report_text = "\n".join(L) + "\n"
530	(OUT / "plan_016_report.md").write_text(report_text)
531	print("  Report written.")
532	
533	# Console summary
534	print("\n" + "=" * 60)
535	print("SUMMARY")
536	print("=" * 60)
537	for _, r in summary_df.sort_values(["matching_type", "subject", "p"]).iterrows():
538	    print(f"  {r.matching_type:6s} {r.subject:25s} p={r.p}: TPR={r.tpr_mean:.3f}±{r.tpr_std:.3f}  "
539	          f"FPR={r.fpr_mean:.3f}±{r.fpr_std:.3f}  ΔTPR={r.delta_tpr:+.3f}")
540	
541	print(f"\nWithin: {n_success_within}/{len(SUBJECTS)} subjects with ΔTPR > 0.3 at p=0.5")
542	print(f"Cross:  {n_success_cross}/{len(SUBJECTS)} subjects with ΔTPR > 0.3 at p=0.5")
543	print(f"Total time: {time.time()-t0:.0f}s")
544	print(f"All outputs saved to {OUT}")
545	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "771954bb-69cd-4628-8342-e438cb4b8428"
}
```

</details>

---

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa73b16fd4338b1af",
  "tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 38299,
    "tool_uses": 5,
    "duration_ms": 9832
  },
  "last_tool_name": "Bash",
  "uuid": "01dabfee-3bcd-49ac-9772-ab6ddd553bd8",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01HrJv48Cv2BGWvLnujo94gD`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep -E \"plan_001|response|metadata\" | head -15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "e82bbdb4-57b9-4cdf-b725-b791e2ad76dc",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M8RdQD7i9mHhfUbv123fEn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 9542,
      "cache_read_input_tokens": 28732,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9542,
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

_source line 23 · 2026-05-21T15:45:38.800Z_

<details><summary>↩ Tool result · `toolu_01HrJv48Cv2BGWvLnujo94gD`</summary>

```text
-rw-r--r--  1 ubuntu ubuntu    20975 May 20 20:48 build_response_matrix.py
-rw-r--r--  1 ubuntu ubuntu  1528143 May 20 20:57 item_metadata.csv
-rw-r--r--  1 ubuntu ubuntu   399283 May 20 20:51 model_metadata.csv
drwxr-xr-x  2 ubuntu ubuntu     4096 May 20 21:08 plan_001
drwxr-xr-x  5 ubuntu ubuntu     4096 May 20 21:11 plan_001_real_data_dif_mmlu
drwxr-xr-x  4 ubuntu ubuntu     4096 May 20 21:22 plan_001b
-rw-r--r--  1 ubuntu ubuntu 50638630 May 20 20:51 response_matrix.npz
-rw-r--r--  1 ubuntu ubuntu    87445 May 20 20:51 response_matrix_index.npz
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "a005e5fe-378f-4b1a-9183-f538e0838417"
}
```

</details>

---

### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa73b16fd4338b1af",
  "tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "description": "Reading artifacts/plan_011/plan_011_analysis.py",
  "usage": {
    "total_tokens": 38716,
    "tool_uses": 6,
    "duration_ms": 11544
  },
  "last_tool_name": "Read",
  "uuid": "6f57437d-9115-40e2-bd32-d562ea1a7327",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01TwNidtMLzfG3SewYQ9gHEN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py",
  "offset": 1,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "831a133c-a271-44aa-8d9c-e5317052a834",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SnkgJs9vpGsrXFXP9MEkCw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 415,
      "cache_read_input_tokens": 38274,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 415,
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

_source line 26 · 2026-05-21T15:45:40.449Z_

<details><summary>↩ Tool result · `toolu_01TwNidtMLzfG3SewYQ9gHEN`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_011_analysis.py — Semi-Synthetic DIF Validation
4	
5	Injects known differential contamination into real MMLU response data and tests
6	whether MH-DIF can detect it. Validates the DIF methodology used in plan_001.
7	
8	Three MH variants:
9	  (1) standard  — total score on 500 items minus current (same as plan_001)
10	  (2) anchor    — total score on 400 known-clean items only
11	  (3) external  — total score on full 12508-item original matrix (best matching)
12	
13	Inputs:
14	  response_matrix.npz, response_matrix_index.npz, model_metadata.csv,
15	  item_metadata.csv, mmlu_li2024_proxy_labels.csv,
16	  plan_001/dif_results_ability.csv
17	
18	Outputs (all in plan_011/):
19	  injection_results.csv, dose_response_summary.csv, per_item_results.csv,
20	  plan_011_report.md
21	"""
22	
23	import numpy as np
24	import pandas as pd
25	from scipy.sparse import load_npz
26	from scipy.stats import chi2 as chi2_dist, fisher_exact
27	from pathlib import Path
28	import time
29	import warnings
30	
31	warnings.filterwarnings("ignore", category=RuntimeWarning)
32	
33	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
34	OUT = BASE / "plan_011"
35	OUT.mkdir(exist_ok=True)
36	
37	INJECTION_PS = [0.0, 0.3, 0.5, 0.7, 1.0]
38	N_SEEDS = 5
39	N_BASELINE = 500
40	N_CONTAMINATED = 100
41	
42	
43	# ════════════════════════════════════════════════════════════════════════════
44	#  MH-DIF CORE
45	# ════════════════════════════════════════════════════════════════════════════
46	def mh_dif_subset(X_ref, X_foc, n_strata=5, anchor_cols=None,
47	                  external_scores_ref=None, external_scores_foc=None):
48	    """
49	    Purified MH-DIF for all columns.
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "cc0dfd0c-2f5a-41e7-b98e-aa1428851e35"
}
```

</details>

---

### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "aa73b16fd4338b1af",
  "tool_use_id": "toolu_01MR3pkEvJfub3UbUuhSTgUT",
  "status": "completed",
  "output_file": "",
  "summary": "Explore plan_016 and plan_011 code",
  "usage": {
    "total_tokens": 39541,
    "tool_uses": 6,
    "duration_ms": 61674
  },
  "uuid": "6df5a69b-e98d-4b2b-a1c8-25ef326b3c24",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c"
}
```

---

### Tool result

_source line 28 · 2026-05-21T15:46:30.574Z_

<details><summary>↩ Tool result · `toolu_01MR3pkEvJfub3UbUuhSTgUT`</summary>

````text
Perfect! Now I have all the information I need. Let me compile a comprehensive technical report:

## Comprehensive MH-DIF Implementation Report

Based on thorough analysis of both implementations, here's the complete technical breakdown:

---

### **PLAN 011: Semi-Synthetic Global Injection Framework**
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py`

#### **1. MH-DIF Function Signature (Lines 46-167)**

```python
def mh_dif_subset(X_ref, X_foc, n_strata=5, anchor_cols=None,
                  external_scores_ref=None, external_scores_foc=None):
    """
    Purified MH-DIF for all columns.

    Stratification source (in priority order):
      1. external_scores_ref/foc — precomputed ability scores (e.g. full-matrix total)
      2. anchor_cols — total score from specified columns only
      3. None — standard purified (all cols minus current)
    """
```

**Parameters:**
- `X_ref`, `X_foc`: Response matrices (ref group, focal group) - shape (n_people, n_items)
- `n_strata`: Number of ability strata (default 5)
- `anchor_cols`: Column indices for anchor set (if provided, excludes current item when computing total score for anchor items)
- `external_scores_ref/foc`: Precomputed ability scores (bypasses internal total score computation)

#### **2. Stratification Logic (Lines 59-83)**

Three-tier matching variable selection:

```python
if not use_external:
    if anchor_cols is not None:
        # ANCHOR mode: total score on specified clean items only
        tot_ref = X_ref[:, anchor_cols].sum(axis=1).astype(np.float64)
        tot_foc = X_foc[:, anchor_cols].sum(axis=1).astype(np.float64)
        anchor_set = set(anchor_cols.tolist()) if hasattr(anchor_cols, 'tolist') else set(anchor_cols)
    else:
        # STANDARD mode: total score on all items
        tot_ref = X_ref.sum(axis=1).astype(np.float64)
        tot_foc = X_foc.sum(axis=1).astype(np.float64)
        anchor_set = None
```

**For each item j (lines 70-83):**
- If `use_external=True`: Use precomputed `external_scores_ref/foc` directly
- If `anchor_set` exists: For items IN anchor set, compute `total - current item`; for items NOT in anchor, use full total
- If standard mode: Compute `total - current item` for every item (purified)

#### **3. MH-DIF Calculation Core (Lines 95-154)**

**Stratification (Lines 85-93):**
```python
s_all = np.concatenate([s_ref, s_foc])
edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
# Create strata boundaries from ability quantiles
n_bins = len(edges) - 1

# Assign each person to stratum k ∈ [0, n_bins-1]
k_ref = np.digitize(s_ref, edges[1:-1])
k_foc = np.digitize(s_foc, edges[1:-1])
```

**Per-Stratum Contingency Table (Lines 101-134):**

For each stratum k with reference (ref) and focal (foc) responders:

| Category | Correct (1) | Incorrect (0) | Total |
|----------|-------------|---------------|-------|
| Ref (n1) | A           | B = n1 - A    | n1    |
| Foc (n0) | C           | D = n0 - C    | n0    |
| Total    | m1 = A + C  | m0 = B + D    | Nk    |

**Where:**
```python
A = float(X_ref[mr, j].sum())  # Correct responses in ref group, stratum k
B = float(n1 - A)              # Incorrect responses in ref group
C = float(X_foc[mf, j].sum())  # Correct responses in focal group
D = float(n0 - C)              # Incorrect responses in focal group
```

**MH Accumulation (Lines 121-134):**
```python
Rk = A * D / Nk    # "Reverse" product
Sk = B * C / Nk    # "Same" product
R += Rk
S += Sk

# Variance components for chi-square
EA = n1 * m1 / Nk
sum_diff += A - EA
sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))

# Variance components for delta SE
Pk = (A + D) / Nk
Qk = (B + C) / Nk
pr += Pk * Rk
ps_qr += Pk * Sk + Qk * Rk
qs += Qk * Sk
```

#### **4. MH Statistics Computation (Lines 140-154)**

```python
if S == 0:
    alpha, delta, se = np.inf, -np.inf, np.nan
elif R == 0:
    alpha, delta, se = 0.0, np.inf, np.nan
else:
    alpha = R / S                           # Mantel-Haenszel odds ratio
    delta = -2.35 * np.log(alpha)           # Delta parameter (log-scale transformation)
    v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)  # Variance of delta
    se = 2.35 * np.sqrt(v) if v > 0 else np.nan

# Chi-square test (Mantel-Haenszel)
if sum_var > 0:
    chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var  # Continuity correction
    pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
else:
    chi2_stat = pval = np.nan
```

#### **5. ETS Classification (Lines 156-162)**

```python
ad = abs(delta) if np.isfinite(delta) else np.inf
if ad < 1.0:
    ets = "A"  # Negligible DIF: |delta| < 1.0
elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:
    ets = "C"  # Large DIF: |delta| ≥ 1.5 AND p < 0.05
else:
    ets = "B"  # Moderate/inconclusive DIF
```

#### **6. Data Loading (Lines 178-198)**

```python
mat = load_npz(BASE / "response_matrix.npz")  # Sparse binary matrix (models × items)
idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
MODEL_NAMES = idx["model_names"]               # (5227,) array of model names
ITEM_IDS = idx["item_ids"]                     # (12508,) array of item IDs
ITEM2COL = {iid: i for i, iid in enumerate(ITEM_IDS)}  # item_id → column index mapping

model_meta = pd.read_csv(BASE / "model_metadata.csv")
li_labels = pd.read_csv(BASE / "mmlu_li2024_proxy_labels.csv")
ability_dif = pd.read_csv(BASE / "plan_001" / "dif_results_ability.csv")

NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}  # model_name → row index mapping
N_MODELS, J_FULL = mat.shape  # (5227, 12508)

# Precompute full-matrix total scores (for external matching)
full_totals = np.asarray(mat.sum(axis=1)).ravel().astype(np.float64)
```

#### **7. Cohort Definition (Lines 216-278)**

**Ability Cohort (Lines 228-253):**
```python
ref_ability_idx = get_row_indices("cohort_accuracy_quintile", [1, 2])  # Q1-2 (low accuracy)
foc_ability_idx = get_row_indices("cohort_accuracy_quintile", [4, 5])  # Q4-5 (high accuracy)

# Find accuracy overlap for fair comparison
ref_acc = model_meta.loc[model_meta["cohort_accuracy_quintile"].isin([1, 2]), "accuracy"]
foc_acc = model_meta.loc[model_meta["cohort_accuracy_quintile"].isin([4, 5]), "accuracy"]
ab_overlap_min = max(ref_acc.min(), foc_acc.min())
ab_overlap_max = min(ref_acc.max(), foc_acc.max())

# Focal injection subset: focal models within accuracy overlap
if ab_overlap_min <= ab_overlap_max:
    foc_ab_inject_mask = (
        model_meta["cohort_accuracy_quintile"].isin([4, 5]) &
        (model_meta["accuracy"] >= ab_overlap_min) &
        (model_meta["accuracy"] <= ab_overlap_max)
    )
    foc_ab_inject_idx = np.array([...])
else:
    foc_ab_inject_idx = foc_ability_idx  # No overlap → inject all focal
```

**Temporal Cohort (Lines 256-278):**
```python
ref_temporal_idx = get_row_indices("cohort_temporal", ["2023"])  # 2023 models
foc_temporal_idx = get_row_indices("cohort_temporal", ["2024"])  # 2024 models

# Similar overlap logic applied
foc_t_inject_idx = subset of 2024 models with accuracy overlap with 2023 models
```

#### **8. Injection Process (Lines 307-325)**

```python
for p in INJECTION_PS:  # [0.0, 0.3, 0.5, 0.7, 1.0]
    for seed in range(1, N_SEEDS + 1):
        rng = np.random.RandomState(seed)
        
        # Step 1: Select random contamination set (20% of baseline items)
        contam_local_idx = rng.choice(N_BASELINE, N_CONTAMINATED, replace=False)  # 100 of 500
        contam_set = set(contam_local_idx.tolist())
        clean_local_idx = np.array([i for i in range(N_BASELINE) if i not in contam_set])
        
        # Step 2: Copy baseline submatrix and inject
        X_inj = X_base.copy()  # X_base is the 500-baseline-item submatrix
        n_flipped = 0
        
        if p > 0:
            # For each contaminated item column
            for local_j in contam_local_idx:
                # For each focal model marked for injection
                for model_row in foc_inject_idx:
                    # If answer is currently incorrect (0)
                    if X_inj[model_row, local_j] == 0:
                        # Flip to correct with probability p
                        if rng.random() < p:
                            X_inj[model_row, local_j] = 1  # Inject correct answer
                            n_flipped += 1
```

**Key injection details:**
- Only flips 0 → 1 (incorrect → correct)
- Never flips 1 → 0 (preserves existing correct answers)
- Applied only to focal inject subset (ability/temporal overlap)
- Probability p controls flip rate per opportunity

#### **9. TPR/FPR Calculation (Lines 345-354)**

```python
contam_mask = dif_results["col_idx"].isin(contam_set)
clean_mask = ~contam_mask

contam_results = dif_results[contam_mask]
clean_results = dif_results[clean_mask]

n_c_contam = (contam_results["ets_class"] == "C").sum()  # Contaminated items flagged as DIF
n_c_clean = (clean_results["ets_class"] == "C").sum()    # Clean items flagged as DIF

tpr = n_c_contam / N_CONTAMINATED              # True positive rate
fpr = n_c_clean / (N_BASELINE - N_CONTAMINATED)  # False positive rate (on clean items)
```

**Fisher's exact test:**
```python
table = [[n_c_contam, N_CONTAMINATED - n_c_contam],
         [n_c_clean, (N_BASELINE - N_CONTAMINATED) - n_c_clean]]
fisher_or, fisher_p = fisher_exact(table)  # Odds ratio and p-value
```

---

### **PLAN 016: Within-Subject Cross-Subject Injection Framework**
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_within_subject_injection.py`

#### **1. MH-DIF Function Signature with Strata Merging (Lines 41-148)**

```python
def purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,
                    external_scores_foc=None, min_per_stratum=5):
    """
    Purified MH-DIF with automatic strata merging for small sample sizes.
    """
```

**Key differences from plan_011:**
- Includes `min_per_stratum` parameter for automatic merging
- Returns `n_strata_used` field (actual strata count after merging)
- Combines ref/foc into single score vector for quantile computation

#### **2. Strata Merging Logic (Lines 157-176)**

```python
def _merge_small_strata(k_all, groups_all, n_bins, min_n):
    """
    Iteratively merge strata with &lt;min_n observations per group.
    Ensures each stratum has ≥min_n in both ref AND foc groups.
    """
    labels = k_all.copy()
    merged = True
    while merged:
        merged = False
        unique_strata = sorted(np.unique(labels))
        for i, k in enumerate(unique_strata):
            mask_k = (labels == k)
            n_ref = int((mask_k & (groups_all == 0)).sum())
            n_foc = int((mask_k & (groups_all == 1)).sum())
            
            # If either group has &lt;min_n observations
            if n_ref < min_n or n_foc < min_n:
                if i + 1 < len(unique_strata):
                    next_k = unique_strata[i + 1]
                    labels[labels == next_k] = k  # Merge with next stratum
                elif i > 0:
                    prev_k = unique_strata[i - 1]
                    labels[labels == k] = prev_k  # Merge with previous stratum
                merged = True
                break
    return labels
```

**Merging strategy:**
- Performed after stratification but before stratum computation
- Always merges forward (toward higher ability) unless at end, then backward
- Continues iteratively until all strata satisfy min_per_stratum constraint

#### **3. Score Vector Formation (Lines 52-60)**

```python
if use_external:
    s_ref = external_scores_ref.astype(np.float64)
    s_foc = external_scores_foc.astype(np.float64)
else:
    s_ref = tot_ref - X_ref[:, j].astype(np.float64)  # Purified: exclude current item
    s_foc = tot_foc - X_foc[:, j].astype(np.float64)

# Combined for unified quantile boundaries
s_all = np.concatenate([s_ref, s_foc])
groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])
```

#### **4. Data Loading (Lines 182-217)**

```python
mat = load_npz(BASE / "response_matrix.npz")
idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
MODEL_NAMES = idx["model_names"]
ITEM_IDS = idx["item_ids"]
ITEM2COL = {iid: i for i, iid in enumerate(ITEM_IDS)}

model_meta = pd.read_csv(BASE / "model_metadata.csv")
item_meta = pd.read_csv(BASE / "item_metadata.csv")

NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}

# Temporal cohorts
ref_names = model_meta.loc[model_meta["cohort_temporal"] == "2023", "model_name"]
foc_names = model_meta.loc[model_meta["cohort_temporal"] == "2024", "model_name"]
ref_rows = np.array([NAME2ROW[n] for n in ref_names if n in NAME2ROW])
foc_rows = np.array([NAME2ROW[n] for n in foc_names if n in NAME2ROW])

# Focal inject subset (2024 models in ability overlap with 2023)
ref_acc = model_meta.loc[model_meta["cohort_temporal"] == "2023", "accuracy"]
foc_acc = model_meta.loc[model_meta["cohort_temporal"] == "2024", "accuracy"]
t_overlap_min = max(ref_acc.min(), foc_acc.min())
t_overlap_max = min(ref_acc.max(), foc_acc.max())

foc_inject_mask = (
    (model_meta["cohort_temporal"] == "2024") &
    (model_meta["accuracy"] >= t_overlap_min) &
    (model_meta["accuracy"] <= t_overlap_max)
)
foc_inject_rows = np.array([...])
```

#### **5. Within-Subject Processing (Lines 229-251)**

```python
for subj_name in SUBJECTS:
    # Extract items in current subject
    subj_items = item_meta[item_meta["subject"] == subj_name]["item_id"].values
    subj_cols = np.array([ITEM2COL[iid] for iid in subj_items if iid in ITEM2COL])
    n_items = len(subj_cols)
    n_contam = max(1, int(n_items * CONTAM_FRAC))  # 20% of subject items
    n_baseline = n_items - n_contam
    
    # Adaptive strata based on subject size
    n_strata = 3 if n_items < 100 else N_STRATA  # Use 3 strata for small subjects
    
    # Full subject response submatrix
    X_subj = mat[:, subj_cols].toarray().astype(np.int8)  # (5227 models, n_items)
```

#### **6. Cross-Subject Score Precomputation (Lines 242-248)**

```python
# Columns that are NOT in current subject
subj_items_set = set(subj_items.tolist())
other_cols = np.array([ITEM2COL[iid] for iid in ITEM_IDS
                       if iid in ITEM2COL and iid not in subj_items_set])

# Precompute base scores from original (uninjected) matrix
# These scores won't change regardless of within-subject injection
cross_ref_base = np.asarray(mat[ref_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)
cross_foc_base = np.asarray(mat[foc_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)
```

**Critical design choice:**
- Cross-subject scores computed from `other_cols` (all non-current-subject items)
- Precomputed ONCE per subject before injection loop
- Immune to injection since injection only affects current subject items

#### **7. Within-Subject Injection (Lines 253-275)**

```python
for p in INJECTION_PS:  # [0.0, 0.5, 1.0]
    for seed in range(1, N_SEEDS + 1):
        rng = np.random.RandomState(seed)
        
        # Contamination set: random 20% of current subject's items
        contam_local_idx = rng.choice(n_items, n_contam, replace=False)
        contam_set = set(contam_local_idx.tolist())
        
        # Inject
        X_inj = X_subj.copy()
        n_flipped = 0
        
        if p > 0:
            for local_j in contam_local_idx:  # For each contaminated subject item
                for model_row in foc_inject_rows:  # For each focal inject model
                    if X_inj[model_row, local_j] == 0:  # If incorrect
                        if rng.random() < p:
                            X_inj[model_row, local_j] = 1  # Flip to correct
                            n_flipped += 1
        
        X_ref = X_inj[ref_rows]   # Extract reference subset
        X_foc = X_inj[foc_rows]   # Extract focal subset
```

#### **8. Matching Type Variants (Lines 276-286)**

```python
for matching_type in MATCHING_TYPES:  # ["within", "cross"]
    
    if matching_type == "within":
        # Standard purified MH: total score on current subject items (minus current)
        dif_results = purified_mh_dif(X_ref, X_foc, n_strata=n_strata,
                                      min_per_stratum=MIN_PER_STRATUM)
    else:  # "cross"
        # External matching: total score on other subjects (precomputed, uninjected)
        dif_results = purified_mh_dif(X_ref, X_foc, n_strata=n_strata,
                                      external_scores_ref=cross_ref_base,
                                      external_scores_foc=cross_foc_base,
                                      min_per_stratum=MIN_PER_STRATUM)
```

**Key design distinction:**
- **within**: Matching variable = subject total score (contaminated by injection)
- **cross**: Matching variable = other subjects' total score (immune to injection)

#### **9. TPR/FPR Calculation (Lines 288-300)**

```python
contam_mask = dif_results["col_idx"].isin(contam_set)
contam_results = dif_results[contam_mask]
clean_results = dif_results[~contam_mask]

n_c_contam = (contam_results["ets_class"] == "C").sum()
n_c_clean = (clean_results["ets_class"] == "C").sum()
tpr = n_c_contam / n_contam if n_contam > 0 else 0
fpr = n_c_clean / n_baseline if n_baseline > 0 else 0

# Fisher's exact test
table = [[n_c_contam, n_contam - n_c_contam],
         [n_c_clean, n_baseline - n_c_clean]]
fisher_or, fisher_p = fisher_exact(table)
```

#### **10. Results Structure (Lines 302-310)**

```python
injection_rows.append(dict(
    subject=subj_name,
    p=p,                        # Injection probability [0.0, 0.5, 1.0]
    seed=seed,
    matching_type=matching_type,  # "within" or "cross"
    n_items=n_items,            # Total items in subject
    n_baseline=n_baseline,      # Clean items (80% of subject)
    n_contaminated=n_contam,    # Contaminated items (20% of subject)
    n_flipped=n_flipped,        # Actual flips performed
    tpr=tpr,                    # True positive rate
    fpr=fpr,                    # False positive rate
    n_c_contam=n_c_contam,      # Count: contaminated → C
    n_c_clean=n_c_clean,        # Count: clean → C (false positives)
    fisher_or=fisher_or,
    fisher_p=fisher_p,
))
```

---

### **Key Implementation Differences**

| Aspect | Plan 011 (Global) | Plan 016 (Within-Subject) |
|--------|-------------------|--------------------------|
| **Baseline set** | 500 global clean items | Per-subject 80% of items |
| **Contamination** | 100 of 500 items (20%) | 20% of each subject's items |
| **Injection P values** | [0.0, 0.3, 0.5, 0.7, 1.0] | [0.0, 0.5, 1.0] |
| **Matching variants** | standard, anchor, external | within, cross |
| **Strata handling** | Fixed 5 strata | Adaptive (3 for <100 items, 5 otherwise) + merging |
| **External scores** | Full 12508-item total | Cross-subject items total |
| **Scope** | Entire test (500 items) | Individual subjects (81-248 items) |
| **Subjects** | Global ability + temporal | Temporal only, per-subject |

---

### **Key Function Signatures Summary**

**Plan 011 - mh_dif_subset** (lines 46-167):
- Input: X_ref, X_foc matrices + stratification parameters
- Matching modes: standard (purified), anchor (specified cols), external (precomputed)
- Output: DataFrame with col_idx, alpha_mh, delta_mh, se, chi2, p_value, ets_class

**Plan 016 - purified_mh_dif** (lines 41-148):
- Input: X_ref, X_foc matrices + automatic strata merging
- Matching modes: within (purified), external (precomputed)
- Output: DataFrame with col_idx, alpha_mh, delta_mh, se, chi2, p_value, ets_class, n_strata_used

**Both use identical ETS classification** (lines 137-142 in plan_016, similar in plan_011):
- A: |delta| < 1.0
- C: |delta| ≥ 1.5 AND p < 0.05
- B: Otherwise
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "baa30323-8efb-4e66-a793-0aa4e3b5b286",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to understand the MH-DIF implementation and semi-synthetic injection framework in two directories:\n\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/` - cross-subject matching implementation\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py` - basic semi-synthetic injection framework\n\nFor each, I need:\n- The MH-DIF function signature and implementation (especially purified MH-DIF with external matching)\n- How injection (incorrect→correct flip) is done\n- How cohorts (ref/foc) are defined\n- How TPR/FPR are calculated\n- ETS classification logic\n- How response matrix and metadata are loaded\n\nBe very thorough - read the full files and report back all relevant code patterns, function signatures, and implementation details. Include line numbers.",
    "agentId": "aa73b16fd4338b1af",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information I need. Let me compile a comprehensive technical report:\n\n## Comprehensive MH-DIF Implementation Report\n\nBased on thorough analysis of both implementations, here's the complete technical breakdown:\n\n---\n\n### **PLAN 011: Semi-Synthetic Global Injection Framework**\n**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py`\n\n#### **1. MH-DIF Function Signature (Lines 46-167)**\n\n```python\ndef mh_dif_subset(X_ref, X_foc, n_strata=5, anchor_cols=None,\n                  external_scores_ref=None, external_scores_foc=None):\n    \"\"\"\n    Purified MH-DIF for all columns.\n\n    Stratification source (in priority order):\n      1. external_scores_ref/foc — precomputed ability scores (e.g. full-matrix total)\n      2. anchor_cols — total score from specified columns only\n      3. None — standard purified (all cols minus current)\n    \"\"\"\n```\n\n**Parameters:**\n- `X_ref`, `X_foc`: Response matrices (ref group, focal group) - shape (n_people, n_items)\n- `n_strata`: Number of ability strata (default 5)\n- `anchor_cols`: Column indices for anchor set (if provided, excludes current item when computing total score for anchor items)\n- `external_scores_ref/foc`: Precomputed ability scores (bypasses internal total score computation)\n\n#### **2. Stratification Logic (Lines 59-83)**\n\nThree-tier matching variable selection:\n\n```python\nif not use_external:\n    if anchor_cols is not None:\n        # ANCHOR mode: total score on specified clean items only\n        tot_ref = X_ref[:, anchor_cols].sum(axis=1).astype(np.float64)\n        tot_foc = X_foc[:, anchor_cols].sum(axis=1).astype(np.float64)\n        anchor_set = set(anchor_cols.tolist()) if hasattr(anchor_cols, 'tolist') else set(anchor_cols)\n    else:\n        # STANDARD mode: total score on all items\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n        anchor_set = None\n```\n\n**For each item j (lines 70-83):**\n- If `use_external=True`: Use precomputed `external_scores_ref/foc` directly\n- If `anchor_set` exists: For items IN anchor set, compute `total - current item`; for items NOT in anchor, use full total\n- If standard mode: Compute `total - current item` for every item (purified)\n\n#### **3. MH-DIF Calculation Core (Lines 95-154)**\n\n**Stratification (Lines 85-93):**\n```python\ns_all = np.concatenate([s_ref, s_foc])\nedges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n# Create strata boundaries from ability quantiles\nn_bins = len(edges) - 1\n\n# Assign each person to stratum k ∈ [0, n_bins-1]\nk_ref = np.digitize(s_ref, edges[1:-1])\nk_foc = np.digitize(s_foc, edges[1:-1])\n```\n\n**Per-Stratum Contingency Table (Lines 101-134):**\n\nFor each stratum k with reference (ref) and focal (foc) responders:\n\n| Category | Correct (1) | Incorrect (0) | Total |\n|----------|-------------|---------------|-------|\n| Ref (n1) | A           | B = n1 - A    | n1    |\n| Foc (n0) | C           | D = n0 - C    | n0    |\n| Total    | m1 = A + C  | m0 = B + D    | Nk    |\n\n**Where:**\n```python\nA = float(X_ref[mr, j].sum())  # Correct responses in ref group, stratum k\nB = float(n1 - A)              # Incorrect responses in ref group\nC = float(X_foc[mf, j].sum())  # Correct responses in focal group\nD = float(n0 - C)              # Incorrect responses in focal group\n```\n\n**MH Accumulation (Lines 121-134):**\n```python\nRk = A * D / Nk    # \"Reverse\" product\nSk = B * C / Nk    # \"Same\" product\nR += Rk\nS += Sk\n\n# Variance components for chi-square\nEA = n1 * m1 / Nk\nsum_diff += A - EA\nsum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n# Variance components for delta SE\nPk = (A + D) / Nk\nQk = (B + C) / Nk\npr += Pk * Rk\nps_qr += Pk * Sk + Qk * Rk\nqs += Qk * Sk\n```\n\n#### **4. MH Statistics Computation (Lines 140-154)**\n\n```python\nif S == 0:\n    alpha, delta, se = np.inf, -np.inf, np.nan\nelif R == 0:\n    alpha, delta, se = 0.0, np.inf, np.nan\nelse:\n    alpha = R / S                           # Mantel-Haenszel odds ratio\n    delta = -2.35 * np.log(alpha)           # Delta parameter (log-scale transformation)\n    v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)  # Variance of delta\n    se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n# Chi-square test (Mantel-Haenszel)\nif sum_var > 0:\n    chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var  # Continuity correction\n    pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\nelse:\n    chi2_stat = pval = np.nan\n```\n\n#### **5. ETS Classification (Lines 156-162)**\n\n```python\nad = abs(delta) if np.isfinite(delta) else np.inf\nif ad < 1.0:\n    ets = \"A\"  # Negligible DIF: |delta| < 1.0\nelif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n    ets = \"C\"  # Large DIF: |delta| ≥ 1.5 AND p < 0.05\nelse:\n    ets = \"B\"  # Moderate/inconclusive DIF\n```\n\n#### **6. Data Loading (Lines 178-198)**\n\n```python\nmat = load_npz(BASE / \"response_matrix.npz\")  # Sparse binary matrix (models × items)\nidx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\nMODEL_NAMES = idx[\"model_names\"]               # (5227,) array of model names\nITEM_IDS = idx[\"item_ids\"]                     # (12508,) array of item IDs\nITEM2COL = {iid: i for i, iid in enumerate(ITEM_IDS)}  # item_id → column index mapping\n\nmodel_meta = pd.read_csv(BASE / \"model_metadata.csv\")\nli_labels = pd.read_csv(BASE / \"mmlu_li2024_proxy_labels.csv\")\nability_dif = pd.read_csv(BASE / \"plan_001\" / \"dif_results_ability.csv\")\n\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}  # model_name → row index mapping\nN_MODELS, J_FULL = mat.shape  # (5227, 12508)\n\n# Precompute full-matrix total scores (for external matching)\nfull_totals = np.asarray(mat.sum(axis=1)).ravel().astype(np.float64)\n```\n\n#### **7. Cohort Definition (Lines 216-278)**\n\n**Ability Cohort (Lines 228-253):**\n```python\nref_ability_idx = get_row_indices(\"cohort_accuracy_quintile\", [1, 2])  # Q1-2 (low accuracy)\nfoc_ability_idx = get_row_indices(\"cohort_accuracy_quintile\", [4, 5])  # Q4-5 (high accuracy)\n\n# Find accuracy overlap for fair comparison\nref_acc = model_meta.loc[model_meta[\"cohort_accuracy_quintile\"].isin([1, 2]), \"accuracy\"]\nfoc_acc = model_meta.loc[model_meta[\"cohort_accuracy_quintile\"].isin([4, 5]), \"accuracy\"]\nab_overlap_min = max(ref_acc.min(), foc_acc.min())\nab_overlap_max = min(ref_acc.max(), foc_acc.max())\n\n# Focal injection subset: focal models within accuracy overlap\nif ab_overlap_min <= ab_overlap_max:\n    foc_ab_inject_mask = (\n        model_meta[\"cohort_accuracy_quintile\"].isin([4, 5]) &\n        (model_meta[\"accuracy\"] >= ab_overlap_min) &\n        (model_meta[\"accuracy\"] <= ab_overlap_max)\n    )\n    foc_ab_inject_idx = np.array([...])\nelse:\n    foc_ab_inject_idx = foc_ability_idx  # No overlap → inject all focal\n```\n\n**Temporal Cohort (Lines 256-278):**\n```python\nref_temporal_idx = get_row_indices(\"cohort_temporal\", [\"2023\"])  # 2023 models\nfoc_temporal_idx = get_row_indices(\"cohort_temporal\", [\"2024\"])  # 2024 models\n\n# Similar overlap logic applied\nfoc_t_inject_idx = subset of 2024 models with accuracy overlap with 2023 models\n```\n\n#### **8. Injection Process (Lines 307-325)**\n\n```python\nfor p in INJECTION_PS:  # [0.0, 0.3, 0.5, 0.7, 1.0]\n    for seed in range(1, N_SEEDS + 1):\n        rng = np.random.RandomState(seed)\n        \n        # Step 1: Select random contamination set (20% of baseline items)\n        contam_local_idx = rng.choice(N_BASELINE, N_CONTAMINATED, replace=False)  # 100 of 500\n        contam_set = set(contam_local_idx.tolist())\n        clean_local_idx = np.array([i for i in range(N_BASELINE) if i not in contam_set])\n        \n        # Step 2: Copy baseline submatrix and inject\n        X_inj = X_base.copy()  # X_base is the 500-baseline-item submatrix\n        n_flipped = 0\n        \n        if p > 0:\n            # For each contaminated item column\n            for local_j in contam_local_idx:\n                # For each focal model marked for injection\n                for model_row in foc_inject_idx:\n                    # If answer is currently incorrect (0)\n                    if X_inj[model_row, local_j] == 0:\n                        # Flip to correct with probability p\n                        if rng.random() < p:\n                            X_inj[model_row, local_j] = 1  # Inject correct answer\n                            n_flipped += 1\n```\n\n**Key injection details:**\n- Only flips 0 → 1 (incorrect → correct)\n- Never flips 1 → 0 (preserves existing correct answers)\n- Applied only to focal inject subset (ability/temporal overlap)\n- Probability p controls flip rate per opportunity\n\n#### **9. TPR/FPR Calculation (Lines 345-354)**\n\n```python\ncontam_mask = dif_results[\"col_idx\"].isin(contam_set)\nclean_mask = ~contam_mask\n\ncontam_results = dif_results[contam_mask]\nclean_results = dif_results[clean_mask]\n\nn_c_contam = (contam_results[\"ets_class\"] == \"C\").sum()  # Contaminated items flagged as DIF\nn_c_clean = (clean_results[\"ets_class\"] == \"C\").sum()    # Clean items flagged as DIF\n\ntpr = n_c_contam / N_CONTAMINATED              # True positive rate\nfpr = n_c_clean / (N_BASELINE - N_CONTAMINATED)  # False positive rate (on clean items)\n```\n\n**Fisher's exact test:**\n```python\ntable = [[n_c_contam, N_CONTAMINATED - n_c_contam],\n         [n_c_clean, (N_BASELINE - N_CONTAMINATED) - n_c_clean]]\nfisher_or, fisher_p = fisher_exact(table)  # Odds ratio and p-value\n```\n\n---\n\n### **PLAN 016: Within-Subject Cross-Subject Injection Framework**\n**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_within_subject_injection.py`\n\n#### **1. MH-DIF Function Signature with Strata Merging (Lines 41-148)**\n\n```python\ndef purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,\n                    external_scores_foc=None, min_per_stratum=5):\n    \"\"\"\n    Purified MH-DIF with automatic strata merging for small sample sizes.\n    \"\"\"\n```\n\n**Key differences from plan_011:**\n- Includes `min_per_stratum` parameter for automatic merging\n- Returns `n_strata_used` field (actual strata count after merging)\n- Combines ref/foc into single score vector for quantile computation\n\n#### **2. Strata Merging Logic (Lines 157-176)**\n\n```python\ndef _merge_small_strata(k_all, groups_all, n_bins, min_n):\n    \"\"\"\n    Iteratively merge strata with &lt;min_n observations per group.\n    Ensures each stratum has ≥min_n in both ref AND foc groups.\n    \"\"\"\n    labels = k_all.copy()\n    merged = True\n    while merged:\n        merged = False\n        unique_strata = sorted(np.unique(labels))\n        for i, k in enumerate(unique_strata):\n            mask_k = (labels == k)\n            n_ref = int((mask_k & (groups_all == 0)).sum())\n            n_foc = int((mask_k & (groups_all == 1)).sum())\n            \n            # If either group has &lt;min_n observations\n            if n_ref < min_n or n_foc < min_n:\n                if i + 1 < len(unique_strata):\n                    next_k = unique_strata[i + 1]\n                    labels[labels == next_k] = k  # Merge with next stratum\n                elif i > 0:\n                    prev_k = unique_strata[i - 1]\n                    labels[labels == k] = prev_k  # Merge with previous stratum\n                merged = True\n                break\n    return labels\n```\n\n**Merging strategy:**\n- Performed after stratification but before stratum computation\n- Always merges forward (toward higher ability) unless at end, then backward\n- Continues iteratively until all strata satisfy min_per_stratum constraint\n\n#### **3. Score Vector Formation (Lines 52-60)**\n\n```python\nif use_external:\n    s_ref = external_scores_ref.astype(np.float64)\n    s_foc = external_scores_foc.astype(np.float64)\nelse:\n    s_ref = tot_ref - X_ref[:, j].astype(np.float64)  # Purified: exclude current item\n    s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n# Combined for unified quantile boundaries\ns_all = np.concatenate([s_ref, s_foc])\ngroups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])\n```\n\n#### **4. Data Loading (Lines 182-217)**\n\n```python\nmat = load_npz(BASE / \"response_matrix.npz\")\nidx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\nMODEL_NAMES = idx[\"model_names\"]\nITEM_IDS = idx[\"item_ids\"]\nITEM2COL = {iid: i for i, iid in enumerate(ITEM_IDS)}\n\nmodel_meta = pd.read_csv(BASE / \"model_metadata.csv\")\nitem_meta = pd.read_csv(BASE / \"item_metadata.csv\")\n\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}\n\n# Temporal cohorts\nref_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"model_name\"]\nfoc_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"model_name\"]\nref_rows = np.array([NAME2ROW[n] for n in ref_names if n in NAME2ROW])\nfoc_rows = np.array([NAME2ROW[n] for n in foc_names if n in NAME2ROW])\n\n# Focal inject subset (2024 models in ability overlap with 2023)\nref_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\nfoc_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"accuracy\"]\nt_overlap_min = max(ref_acc.min(), foc_acc.min())\nt_overlap_max = min(ref_acc.max(), foc_acc.max())\n\nfoc_inject_mask = (\n    (model_meta[\"cohort_temporal\"] == \"2024\") &\n    (model_meta[\"accuracy\"] >= t_overlap_min) &\n    (model_meta[\"accuracy\"] <= t_overlap_max)\n)\nfoc_inject_rows = np.array([...])\n```\n\n#### **5. Within-Subject Processing (Lines 229-251)**\n\n```python\nfor subj_name in SUBJECTS:\n    # Extract items in current subject\n    subj_items = item_meta[item_meta[\"subject\"] == subj_name][\"item_id\"].values\n    subj_cols = np.array([ITEM2COL[iid] for iid in subj_items if iid in ITEM2COL])\n    n_items = len(subj_cols)\n    n_contam = max(1, int(n_items * CONTAM_FRAC))  # 20% of subject items\n    n_baseline = n_items - n_contam\n    \n    # Adaptive strata based on subject size\n    n_strata = 3 if n_items < 100 else N_STRATA  # Use 3 strata for small subjects\n    \n    # Full subject response submatrix\n    X_subj = mat[:, subj_cols].toarray().astype(np.int8)  # (5227 models, n_items)\n```\n\n#### **6. Cross-Subject Score Precomputation (Lines 242-248)**\n\n```python\n# Columns that are NOT in current subject\nsubj_items_set = set(subj_items.tolist())\nother_cols = np.array([ITEM2COL[iid] for iid in ITEM_IDS\n                       if iid in ITEM2COL and iid not in subj_items_set])\n\n# Precompute base scores from original (uninjected) matrix\n# These scores won't change regardless of within-subject injection\ncross_ref_base = np.asarray(mat[ref_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)\ncross_foc_base = np.asarray(mat[foc_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)\n```\n\n**Critical design choice:**\n- Cross-subject scores computed from `other_cols` (all non-current-subject items)\n- Precomputed ONCE per subject before injection loop\n- Immune to injection since injection only affects current subject items\n\n#### **7. Within-Subject Injection (Lines 253-275)**\n\n```python\nfor p in INJECTION_PS:  # [0.0, 0.5, 1.0]\n    for seed in range(1, N_SEEDS + 1):\n        rng = np.random.RandomState(seed)\n        \n        # Contamination set: random 20% of current subject's items\n        contam_local_idx = rng.choice(n_items, n_contam, replace=False)\n        contam_set = set(contam_local_idx.tolist())\n        \n        # Inject\n        X_inj = X_subj.copy()\n        n_flipped = 0\n        \n        if p > 0:\n            for local_j in contam_local_idx:  # For each contaminated subject item\n                for model_row in foc_inject_rows:  # For each focal inject model\n                    if X_inj[model_row, local_j] == 0:  # If incorrect\n                        if rng.random() < p:\n                            X_inj[model_row, local_j] = 1  # Flip to correct\n                            n_flipped += 1\n        \n        X_ref = X_inj[ref_rows]   # Extract reference subset\n        X_foc = X_inj[foc_rows]   # Extract focal subset\n```\n\n#### **8. Matching Type Variants (Lines 276-286)**\n\n```python\nfor matching_type in MATCHING_TYPES:  # [\"within\", \"cross\"]\n    \n    if matching_type == \"within\":\n        # Standard purified MH: total score on current subject items (minus current)\n        dif_results = purified_mh_dif(X_ref, X_foc, n_strata=n_strata,\n                                      min_per_stratum=MIN_PER_STRATUM)\n    else:  # \"cross\"\n        # External matching: total score on other subjects (precomputed, uninjected)\n        dif_results = purified_mh_dif(X_ref, X_foc, n_strata=n_strata,\n                                      external_scores_ref=cross_ref_base,\n                                      external_scores_foc=cross_foc_base,\n                                      min_per_stratum=MIN_PER_STRATUM)\n```\n\n**Key design distinction:**\n- **within**: Matching variable = subject total score (contaminated by injection)\n- **cross**: Matching variable = other subjects' total score (immune to injection)\n\n#### **9. TPR/FPR Calculation (Lines 288-300)**\n\n```python\ncontam_mask = dif_results[\"col_idx\"].isin(contam_set)\ncontam_results = dif_results[contam_mask]\nclean_results = dif_results[~contam_mask]\n\nn_c_contam = (contam_results[\"ets_class\"] == \"C\").sum()\nn_c_clean = (clean_results[\"ets_class\"] == \"C\").sum()\ntpr = n_c_contam / n_contam if n_contam > 0 else 0\nfpr = n_c_clean / n_baseline if n_baseline > 0 else 0\n\n# Fisher's exact test\ntable = [[n_c_contam, n_contam - n_c_contam],\n         [n_c_clean, n_baseline - n_c_clean]]\nfisher_or, fisher_p = fisher_exact(table)\n```\n\n#### **10. Results Structure (Lines 302-310)**\n\n```python\ninjection_rows.append(dict(\n    subject=subj_name,\n    p=p,                        # Injection probability [0.0, 0.5, 1.0]\n    seed=seed,\n    matching_type=matching_type,  # \"within\" or \"cross\"\n    n_items=n_items,            # Total items in subject\n    n_baseline=n_baseline,      # Clean items (80% of subject)\n    n_contaminated=n_contam,    # Contaminated items (20% of subject)\n    n_flipped=n_flipped,        # Actual flips performed\n    tpr=tpr,                    # True positive rate\n    fpr=fpr,                    # False positive rate\n    n_c_contam=n_c_contam,      # Count: contaminated → C\n    n_c_clean=n_c_clean,        # Count: clean → C (false positives)\n    fisher_or=fisher_or,\n    fisher_p=fisher_p,\n))\n```\n\n---\n\n### **Key Implementation Differences**\n\n| Aspect | Plan 011 (Global) | Plan 016 (Within-Subject) |\n|--------|-------------------|--------------------------|\n| **Baseline set** | 500 global clean items | Per-subject 80% of items |\n| **Contamination** | 100 of 500 items (20%) | 20% of each subject's items |\n| **Injection P values** | [0.0, 0.3, 0.5, 0.7, 1.0] | [0.0, 0.5, 1.0] |\n| **Matching variants** | standard, anchor, external | within, cross |\n| **Strata handling** | Fixed 5 strata | Adaptive (3 for <100 items, 5 otherwise) + merging |\n| **External scores** | Full 12508-item total | Cross-subject items total |\n| **Scope** | Entire test (500 items) | Individual subjects (81-248 items) |\n| **Subjects** | Global ability + temporal | Temporal only, per-subject |\n\n---\n\n### **Key Function Signatures Summary**\n\n**Plan 011 - mh_dif_subset** (lines 46-167):\n- Input: X_ref, X_foc matrices + stratification parameters\n- Matching modes: standard (purified), anchor (specified cols), external (precomputed)\n- Output: DataFrame with col_idx, alpha_mh, delta_mh, se, chi2, p_value, ets_class\n\n**Plan 016 - purified_mh_dif** (lines 41-148):\n- Input: X_ref, X_foc matrices + automatic strata merging\n- Matching modes: within (purified), external (precomputed)\n- Output: DataFrame with col_idx, alpha_mh, delta_mh, se, chi2, p_value, ets_class, n_strata_used\n\n**Both use identical ETS classification** (lines 137-142 in plan_016, similar in plan_011):\n- A: |delta| < 1.0\n- C: |delta| ≥ 1.5 AND p < 0.05\n- B: Otherwise"
      }
    ],
    "totalDurationMs": 61677,
    "totalTokens": 46468,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 824,
      "cache_read_input_tokens": 38689,
      "output_tokens": 6950,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 824
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 6950,
          "cache_read_input_tokens": 38689,
          "cache_creation_input_tokens": 824,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 824,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 3,
      "searchCount": 0,
      "bashCount": 3,
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

_source line 29_

Now let me check the data structures to understand subjects and verify counts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "dad21707-80ba-4cb9-9541-1349a7f0198d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K33JZnqXs6jArdKS5UPJQT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7418,
      "cache_read_input_tokens": 25233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7418
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

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01HMPjoKDbBNHwiEkJMwnwrg`</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np, pandas as pd\nfrom scipy.sparse import load_npz\n\nmat = load_npz('artifacts/response_matrix.npz')\nidx = np.load('artifacts/response_matrix_index.npz', allow_pickle=True)\nmodel_meta = pd.read_csv('artifacts/model_metadata.csv')\nitem_meta = pd.read_csv('artifacts/item_metadata.csv')\n\nprint('Matrix shape:', mat.shape)\nprint('Subjects:', item_meta['subject'].nunique())\nprint('Cohort counts:', model_meta['cohort_temporal'].value_counts().to_dict())\n\n# Check overlap\nref_acc = model_meta.loc[model_meta['cohort_temporal']=='2023','accuracy']\nfoc_acc = model_meta.loc[model_meta['cohort_temporal']=='2024','accuracy']\nt_min = max(ref_acc.min(), foc_acc.min())\nt_max = min(ref_acc.max(), foc_acc.max())\nfoc_inj = model_meta[(model_meta['cohort_temporal']=='2024') & (model_meta['accuracy']>=t_min) & (model_meta['accuracy']<=t_max)]\nprint(f'Overlap: [{t_min:.4f}, {t_max:.4f}], foc_inject: {len(foc_inj)}')\n\n# Subject sizes\nsubj_sizes = item_meta.groupby('subject').size().sort_values()\nprint(f'Subject sizes: min={subj_sizes.min()}, max={subj_sizes.max()}, median={subj_sizes.median()}')\nprint(subj_sizes.to_string())\n\"\n",
  "description": "Check data dimensions and subject info"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "ff5ac47f-66d4-436e-adfc-60cb887d17ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K33JZnqXs6jArdKS5UPJQT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7418,
      "cache_read_input_tokens": 25233,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7418
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

_source line 31 · 2026-05-21T15:46:43.529Z_

<details><summary>↩ Tool result · `toolu_01HMPjoKDbBNHwiEkJMwnwrg`</summary>

```text
Matrix shape: (5227, 12508)
Subjects: 57
Cohort counts: {'other': 3340, '2023': 1080, '2024': 807}
Overlap: [0.2200, 0.8090], foc_inject: 787
Subject sizes: min=72, max=1331, median=161.0
subject
college_mathematics                      72
college_physics                          73
college_chemistry                        81
global_facts                             83
medical_genetics                         85
college_computer_science                 86
machine_learning                         87
computer_security                        87
abstract_algebra                         91
management                               92
business_ethics                          93
high_school_computer_science             96
us_foreign_policy                        96
public_relations                         98
jurisprudence                           101
econometrics                            103
international_law                       104
formal_logic                            109
human_sexuality                         119
high_school_physics                     121
anatomy                                 122
electrical_engineering                  127
college_biology                         133
astronomy                               136
virology                                149
logical_fallacies                       151
high_school_european_history            155
world_religions                         159
college_medicine                        161
high_school_statistics                  181
high_school_chemistry                   181
high_school_geography                   184
sociology                               186
high_school_government_and_politics     189
high_school_us_history                  196
high_school_mathematics                 197
conceptual_physics                      202
human_aging                             203
high_school_microeconomics              220
high_school_world_history               225
marketing                               225
security_studies                        230
clinical_knowledge                      241
professional_accounting                 242
professional_medicine                   248
nutrition                               282
philosophy                              285
high_school_biology                     290
prehistory                              296
moral_disputes                          313
elementary_mathematics                  317
high_school_macroeconomics              358
high_school_psychology                  517
professional_psychology                 562
moral_scenarios                         692
miscellaneous                           745
professional_law                       1331
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "fcfbb6d1-09f1-436c-8829-dfb74a376d13",
  "tool_use_result": {
    "stdout": "Matrix shape: (5227, 12508)\nSubjects: 57\nCohort counts: {'other': 3340, '2023': 1080, '2024': 807}\nOverlap: [0.2200, 0.8090], foc_inject: 787\nSubject sizes: min=72, max=1331, median=161.0\nsubject\ncollege_mathematics                      72\ncollege_physics                          73\ncollege_chemistry                        81\nglobal_facts                             83\nmedical_genetics                         85\ncollege_computer_science                 86\nmachine_learning                         87\ncomputer_security                        87\nabstract_algebra                         91\nmanagement                               92\nbusiness_ethics                          93\nhigh_school_computer_science             96\nus_foreign_policy                        96\npublic_relations                         98\njurisprudence                           101\neconometrics                            103\ninternational_law                       104\nformal_logic                            109\nhuman_sexuality                         119\nhigh_school_physics                     121\nanatomy                                 122\nelectrical_engineering                  127\ncollege_biology                         133\nastronomy                               136\nvirology                                149\nlogical_fallacies                       151\nhigh_school_european_history            155\nworld_religions                         159\ncollege_medicine                        161\nhigh_school_statistics                  181\nhigh_school_chemistry                   181\nhigh_school_geography                   184\nsociology                               186\nhigh_school_government_and_politics     189\nhigh_school_us_history                  196\nhigh_school_mathematics                 197\nconceptual_physics                      202\nhuman_aging                             203\nhigh_school_microeconomics              220\nhigh_school_world_history               225\nmarketing                               225\nsecurity_studies                        230\nclinical_knowledge                      241\nprofessional_accounting                 242\nprofessional_medicine                   248\nnutrition                               282\nphilosophy                              285\nhigh_school_biology                     290\nprehistory                              296\nmoral_disputes                          313\nelementary_mathematics                  317\nhigh_school_macroeconomics              358\nhigh_school_psychology                  517\nprofessional_psychology                 562\nmoral_scenarios                         692\nmiscellaneous                           745\nprofessional_law                       1331",
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

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need to write the experiment script. Let me read the plan_016 code directly to get the exact function implementation I'll adapt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "fd44db66-cd36-468d-9820-0573e0390990",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ChDKREjSixjHgbJWyWrkh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1039,
      "cache_read_input_tokens": 32651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1039
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

_source line 33_

Now I have all the context. Let me read the plan_016 script to get the exact `purified_mh_dif` function implementation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "725d5333-27b4-4824-bab3-d2a8092f7f04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ChDKREjSixjHgbJWyWrkh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1039,
      "cache_read_input_tokens": 32651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1039
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

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_0193UZfbSwnrW959m1ZkE1a1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_within_subject_injection.py",
  "limit": 180
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "6562b152-6325-4e3e-9276-2dad7821a3a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ChDKREjSixjHgbJWyWrkh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1039,
      "cache_read_input_tokens": 32651,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1039
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

_source line 35 · 2026-05-21T15:46:50.046Z_

<details><summary>↩ Tool result · `toolu_0193UZfbSwnrW959m1ZkE1a1`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_016: Within-Subject Semi-Synthetic Injection
4	
5	For each of 5 selected MMLU subjects, inject differential contamination into
6	the temporal focal group (2024 models) and test whether within-subject MH-DIF
7	detects the injected signal.
8	
9	Subjects: business_ethics (93), human_aging (203), professional_medicine (248),
10	          formal_logic (109), high_school_statistics (181)
11	Injection: 20% items contaminated, p ∈ {0.0, 0.5, 1.0}, 5 seeds
12	Matching: within-subject purified total score + cross-subject total score
13	"""
14	
15	import numpy as np
16	import pandas as pd
17	from scipy.sparse import load_npz
18	from scipy.stats import chi2 as chi2_dist, fisher_exact
19	from pathlib import Path
20	import time
21	import warnings
22	
23	warnings.filterwarnings("ignore", category=RuntimeWarning)
24	
25	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
26	OUT = BASE / "plan_016"
27	OUT.mkdir(exist_ok=True)
28	
29	SUBJECTS = ["business_ethics", "human_aging", "professional_medicine",
30	            "formal_logic", "high_school_statistics"]
31	INJECTION_PS = [0.0, 0.5, 1.0]
32	N_SEEDS = 5
33	CONTAM_FRAC = 0.20
34	N_STRATA = 5
35	MIN_PER_STRATUM = 5
36	
37	
38	# ════════════════════════════════════════════════════════════════════════════
39	#  MH-DIF CORE (from plan_014 with strata merging + external score support)
40	# ════════════════════════════════════════════════════════════════════════════
41	def purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,
42	                    external_scores_foc=None, min_per_stratum=5):
43	    J = X_ref.shape[1]
44	    use_external = external_scores_ref is not None
45	
46	    if not use_external:
47	        tot_ref = X_ref.sum(axis=1).astype(np.float64)
48	        tot_foc = X_foc.sum(axis=1).astype(np.float64)
49	
50	    rows = []
51	    for j in range(J):
52	        if use_external:
53	            s_ref = external_scores_ref.astype(np.float64)
54	            s_foc = external_scores_foc.astype(np.float64)
55	        else:
56	            s_ref = tot_ref - X_ref[:, j].astype(np.float64)
57	            s_foc = tot_foc - X_foc[:, j].astype(np.float64)
58	
59	        s_all = np.concatenate([s_ref, s_foc])
60	        groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])
61	
62	        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
63	        if len(edges) < 2:
64	            rows.append(_nan_row(j))
65	            continue
66	
67	        n_bins = len(edges) - 1
68	        k_all = np.digitize(s_all, edges[1:-1])
69	        strata_labels = _merge_small_strata(k_all, groups_all, n_bins, min_per_stratum)
70	
71	        R = S = 0.0
72	        sum_diff = 0.0
73	        sum_var = 0.0
74	        pr = ps_qr = qs = 0.0
75	        n_ok = 0
76	
77	        x_all = np.concatenate([X_ref[:, j], X_foc[:, j]])
78	
79	        for k in np.unique(strata_labels):
80	            mask_k = (strata_labels == k)
81	            mask_ref = mask_k & (groups_all == 0)
82	            mask_foc = mask_k & (groups_all == 1)
83	
84	            n1 = int(mask_ref.sum())
85	            n0 = int(mask_foc.sum())
86	            if n1 == 0 or n0 == 0:
87	                continue
88	
89	            A = float(x_all[mask_ref].sum())
90	            B = float(n1 - A)
91	            C = float(x_all[mask_foc].sum())
92	            D = float(n0 - C)
93	            Nk = float(n1 + n0)
94	            m1 = A + C
95	            m0 = B + D
96	
97	            if m1 == 0 or m0 == 0 or Nk <= 1:
98	                continue
99	            n_ok += 1
100	
101	            Rk = A * D / Nk
102	            Sk = B * C / Nk
103	            R += Rk
104	            S += Sk
105	
106	            EA = n1 * m1 / Nk
107	            sum_diff += A - EA
108	            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))
109	
110	            Pk = (A + D) / Nk
111	            Qk = (B + C) / Nk
112	            pr += Pk * Rk
113	            ps_qr += Pk * Sk + Qk * Rk
114	            qs += Qk * Sk
115	
116	        if n_ok == 0 or (R == 0 and S == 0):
117	            rows.append(_nan_row(j))
118	            continue
119	
120	        if S == 0:
121	            alpha, delta, se = np.inf, -np.inf, np.nan
122	        elif R == 0:
123	            alpha, delta, se = 0.0, np.inf, np.nan
124	        else:
125	            alpha = R / S
126	            delta = -2.35 * np.log(alpha)
127	            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)
128	            se = 2.35 * np.sqrt(v) if v > 0 else np.nan
129	
130	        if sum_var > 0:
131	            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
132	            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
133	        else:
134	            chi2_stat = pval = np.nan
135	
136	        ad = abs(delta) if np.isfinite(delta) else np.inf
137	        if ad < 1.0:
138	            ets = "A"
139	        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:
140	            ets = "C"
141	        else:
142	            ets = "B"
143	
144	        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,
145	                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets,
146	                         n_strata_used=n_ok))
147	
148	    return pd.DataFrame(rows)
149	
150	
151	def _nan_row(j):
152	    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,
153	                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class="A",
154	                n_strata_used=0)
155	
156	
157	def _merge_small_strata(k_all, groups_all, n_bins, min_n):
158	    labels = k_all.copy()
159	    merged = True
160	    while merged:
161	        merged = False
162	        unique_strata = sorted(np.unique(labels))
163	        for i, k in enumerate(unique_strata):
164	            mask_k = (labels == k)
165	            n_ref = int((mask_k & (groups_all == 0)).sum())
166	            n_foc = int((mask_k & (groups_all == 1)).sum())
167	            if n_ref < min_n or n_foc < min_n:
168	                if i + 1 < len(unique_strata):
169	                    next_k = unique_strata[i + 1]
170	                    labels[labels == next_k] = k
171	                elif i > 0:
172	                    prev_k = unique_strata[i - 1]
173	                    labels[labels == k] = prev_k
174	                merged = True
175	                break
176	    return labels
177	
178	
179	# ════════════════════════════════════════════════════════════════════════════
180	#  DATA LOADING
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "f65bf0c4-5f8a-497c-b2b1-63d9c8715079",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_within_subject_injection.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nplan_016: Within-Subject Semi-Synthetic Injection\n\nFor each of 5 selected MMLU subjects, inject differential contamination into\nthe temporal focal group (2024 models) and test whether within-subject MH-DIF\ndetects the injected signal.\n\nSubjects: business_ethics (93), human_aging (203), professional_medicine (248),\n          formal_logic (109), high_school_statistics (181)\nInjection: 20% items contaminated, p ∈ {0.0, 0.5, 1.0}, 5 seeds\nMatching: within-subject purified total score + cross-subject total score\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist, fisher_exact\nfrom pathlib import Path\nimport time\nimport warnings\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_016\"\nOUT.mkdir(exist_ok=True)\n\nSUBJECTS = [\"business_ethics\", \"human_aging\", \"professional_medicine\",\n            \"formal_logic\", \"high_school_statistics\"]\nINJECTION_PS = [0.0, 0.5, 1.0]\nN_SEEDS = 5\nCONTAM_FRAC = 0.20\nN_STRATA = 5\nMIN_PER_STRATUM = 5\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE (from plan_014 with strata merging + external score support)\n# ════════════════════════════════════════════════════════════════════════════\ndef purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,\n                    external_scores_foc=None, min_per_stratum=5):\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])\n\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n\n        n_bins = len(edges) - 1\n        k_all = np.digitize(s_all, edges[1:-1])\n        strata_labels = _merge_small_strata(k_all, groups_all, n_bins, min_per_stratum)\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        x_all = np.concatenate([X_ref[:, j], X_foc[:, j]])\n\n        for k in np.unique(strata_labels):\n            mask_k = (strata_labels == k)\n            mask_ref = mask_k & (groups_all == 0)\n            mask_foc = mask_k & (groups_all == 1)\n\n            n1 = int(mask_ref.sum())\n            n0 = int(mask_foc.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(x_all[mask_ref].sum())\n            B = float(n1 - A)\n            C = float(x_all[mask_foc].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else np.inf\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets,\n                         n_strata_used=n_ok))\n\n    return pd.DataFrame(rows)\n\n\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\",\n                n_strata_used=0)\n\n\ndef _merge_small_strata(k_all, groups_all, n_bins, min_n):\n    labels = k_all.copy()\n    merged = True\n    while merged:\n        merged = False\n        unique_strata = sorted(np.unique(labels))\n        for i, k in enumerate(unique_strata):\n            mask_k = (labels == k)\n            n_ref = int((mask_k & (groups_all == 0)).sum())\n            n_foc = int((mask_k & (groups_all == 1)).sum())\n            if n_ref < min_n or n_foc < min_n:\n                if i + 1 < len(unique_strata):\n                    next_k = unique_strata[i + 1]\n                    labels[labels == next_k] = k\n                elif i > 0:\n                    prev_k = unique_strata[i - 1]\n                    labels[labels == k] = prev_k\n                merged = True\n                break\n    return labels\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING",
      "numLines": 180,
      "startLine": 1,
      "totalLines": 545
    }
  }
}
```

</details>

---

### Assistant

_source line 36_

Good, I have all the pieces. Now let me create the output directory and write the experiment script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "1751100c-399f-4bbc-abf8-5b974f1ef1a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016nStguBt1EvDgK1iqweAzL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2799,
      "cache_read_input_tokens": 33690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2799
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

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01QPuDz7p5ML8Sihc8u2wtgB`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "b26f35f3-e23a-48a4-9656-75b485f6139a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016nStguBt1EvDgK1iqweAzL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2799,
      "cache_read_input_tokens": 33690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2799
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

_source line 38 · 2026-05-21T15:46:55.844Z_

<details><summary>↩ Tool result · `toolu_01QPuDz7p5ML8Sihc8u2wtgB`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "4d7bdac8-2dcc-4b70-bae6-c605ab96d778",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Write · `toolu_017FYT7RLMc7Y7pS7zvksxSq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nplan_034: Multi-Subject Simultaneous Injection Experiment\n\nTests Proposition 1 (ΔFPR=0) robustness under multi-subject contamination.\nWhen k subjects are simultaneously injected, the cross-subject matching variable\n(total score on remaining 57-k uninjected subjects) degrades. ΔFPR(k) on\nnon-target subjects should increase with k, revealing the validity boundary.\n\nInputs:\n  - artifacts/response_matrix.npz         (5227 × 12508 sparse binary)\n  - artifacts/response_matrix_index.npz   (model_names, item_ids)\n  - artifacts/model_metadata.csv          (cohort_temporal, accuracy, ...)\n  - artifacts/item_metadata.csv           (item_id, subject, ...)\n\nOutputs:\n  - multi_subject_injection_results.csv   (per-target-subject DIF results)\n  - non_target_fpr_results.csv            (FPR on uninjected subjects)\n  - summary_by_k.csv                      (aggregated ΔFPR/ΔTPR by k,p)\n  - plan_034_report.md\n\nDependencies: numpy, pandas, scipy\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\nimport warnings\nimport argparse\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_034_multi_subject_injection\"\nOUT.mkdir(exist_ok=True)\n\nKS = [1, 2, 3, 5, 10, 20]\nPS = [0.1, 0.3, 0.5]\nN_SEEDS = 5\nN_STRATA = 5\nMIN_PER_STRATUM = 5\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE (from plan_016 with strata merging + external score support)\n# ════════════════════════════════════════════════════════════════════════════\ndef purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,\n                    external_scores_foc=None, min_per_stratum=5):\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])\n\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n\n        n_bins = len(edges) - 1\n        k_all = np.digitize(s_all, edges[1:-1])\n        strata_labels = _merge_small_strata(k_all, groups_all, n_bins, min_per_stratum)\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        x_all = np.concatenate([X_ref[:, j], X_foc[:, j]])\n\n        for k in np.unique(strata_labels):\n            mask_k = (strata_labels == k)\n            mask_ref = mask_k & (groups_all == 0)\n            mask_foc = mask_k & (groups_all == 1)\n\n            n1 = int(mask_ref.sum())\n            n0 = int(mask_foc.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(x_all[mask_ref].sum())\n            B = float(n1 - A)\n            C = float(x_all[mask_foc].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else np.inf\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets,\n                         n_strata_used=n_ok))\n\n    return pd.DataFrame(rows)\n\n\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\",\n                n_strata_used=0)\n\n\ndef _merge_small_strata(k_all, groups_all, n_bins, min_n):\n    labels = k_all.copy()\n    merged = True\n    while merged:\n        merged = False\n        unique_strata = sorted(np.unique(labels))\n        for i, k in enumerate(unique_strata):\n            mask_k = (labels == k)\n            n_ref = int((mask_k & (groups_all == 0)).sum())\n            n_foc = int((mask_k & (groups_all == 1)).sum())\n            if n_ref < min_n or n_foc < min_n:\n                if i + 1 < len(unique_strata):\n                    next_k = unique_strata[i + 1]\n                    labels[labels == next_k] = k\n                elif i > 0:\n                    prev_k = unique_strata[i - 1]\n                    labels[labels == k] = prev_k\n                merged = True\n                break\n    return labels\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\ndef load_data():\n    mat = load_npz(BASE / \"response_matrix.npz\")\n    idx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n    item2col = {iid: i for i, iid in enumerate(item_ids)}\n\n    model_meta = pd.read_csv(BASE / \"model_metadata.csv\")\n    item_meta = pd.read_csv(BASE / \"item_metadata.csv\")\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    # Temporal cohorts\n    ref_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"model_name\"]\n    foc_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"model_name\"]\n    ref_rows = np.array([name2row[n] for n in ref_names if n in name2row])\n    foc_rows = np.array([name2row[n] for n in foc_names if n in name2row])\n\n    # Focal inject subset: 2024 models in accuracy overlap with 2023\n    ref_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\n    foc_df = model_meta[model_meta[\"cohort_temporal\"] == \"2024\"]\n    t_min = max(ref_acc.min(), foc_df[\"accuracy\"].min())\n    t_max = min(ref_acc.max(), foc_df[\"accuracy\"].max())\n    foc_inject_mask = (foc_df[\"accuracy\"] >= t_min) & (foc_df[\"accuracy\"] <= t_max)\n    foc_inject_rows = np.array([name2row[n] for n in foc_df.loc[foc_inject_mask, \"model_name\"]\n                                if n in name2row])\n\n    # Build subject → column indices mapping\n    subject_cols = {}\n    subjects = sorted(item_meta[\"subject\"].unique())\n    for subj in subjects:\n        ids = item_meta.loc[item_meta[\"subject\"] == subj, \"item_id\"].values\n        cols = np.array([item2col[iid] for iid in ids if iid in item2col])\n        subject_cols[subj] = cols\n\n    return mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MAIN EXPERIMENT\n# ════════════════════════════════════════════════════════════════════════════\ndef run_experiment(ks=KS, ps=PS, n_seeds=N_SEEDS):\n    t0 = time.time()\n    mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols = load_data()\n    print(f\"Data loaded: {len(ref_rows)} ref, {len(foc_rows)} foc, \"\n          f\"{len(foc_inject_rows)} foc_inject, {len(subjects)} subjects\")\n\n    all_cols = np.concatenate([subject_cols[s] for s in subjects])\n    all_cols_set = set(all_cols.tolist())\n\n    # ── Phase 1: baseline (p=0) per-subject FPR with cross-subject matching ──\n    # Baseline uses full uninjected cross-subject scores\n    print(\"Computing baseline FPR (p=0) for all subjects...\")\n    baseline_fpr = {}\n    baseline_n_c = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        other_cols = np.array([c for c in all_cols if c not in set(s_cols.tolist())])\n\n        cross_ref = np.asarray(mat[ref_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)\n        cross_foc = np.asarray(mat[foc_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)\n\n        X_ref = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n        X_foc = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n        n_strata = 3 if len(s_cols) < 100 else N_STRATA\n        dif = purified_mh_dif(X_ref, X_foc, n_strata=n_strata,\n                              external_scores_ref=cross_ref,\n                              external_scores_foc=cross_foc,\n                              min_per_stratum=MIN_PER_STRATUM)\n        n_c = int((dif[\"ets_class\"] == \"C\").sum())\n        fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n        baseline_fpr[subj] = fpr\n        baseline_n_c[subj] = n_c\n\n    print(f\"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}\")\n\n    # ── Phase 2: injection runs ──\n    target_rows_list = []\n    non_target_rows_list = []\n    total_runs = len(ks) * len(ps) * n_seeds\n    run_i = 0\n\n    for k in ks:\n        for p in ps:\n            for seed in range(1, n_seeds + 1):\n                run_i += 1\n                rng = np.random.RandomState(seed)\n                target_subjects = sorted(rng.choice(subjects, size=k, replace=False))\n                non_target_subjects = [s for s in subjects if s not in target_subjects]\n\n                # Build injected matrix columns for target subjects\n                # Collect all target columns for injection\n                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])\n                target_cols_set = set(target_cols_all.tolist())\n                non_target_cols = np.array([c for c in all_cols if c not in target_cols_set])\n\n                # Inject: flip incorrect→correct for focal inject models on target items\n                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    for local_j in range(len(target_cols_all)):\n                        for model_row in foc_inject_rows:\n                            if mat_dense_targets[model_row, local_j] == 0:\n                                if rng.random() < p:\n                                    mat_dense_targets[model_row, local_j] = 1\n                                    n_flipped += 1\n\n                # Cross-subject matching variable = total on uninjected subjects\n                # (from original matrix — non-target subjects are never injected)\n                cross_ref = np.asarray(mat[ref_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n                cross_foc = np.asarray(mat[foc_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                # But for target subjects, the matching variable includes OTHER\n                # target subjects' injected scores too. We need per-subject matching.\n                # For target subject s: matching = non_target_total + injected_other_targets\n                # For non-target subject s: matching = non_target_total_minus_s + all_target_injected\n\n                # Precompute injected target total per model (from injected matrix)\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                # Build local col mapping: target_cols_all[local_idx] → local_idx\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}\n\n                elapsed = time.time() - t0\n                print(f\"  [{run_i}/{total_runs}] k={k} p={p} seed={seed} \"\n                      f\"flipped={n_flipped} ({elapsed:.0f}s)\")\n\n                # ── DIF on each target subject ──\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    # Matching variable for target subject: everything EXCEPT this subject\n                    # = non_target_total + injected scores from OTHER target subjects\n                    this_subj_injected = X_subj_inj.sum(axis=1).astype(np.float64)\n                    other_target_injected = injected_target_total - this_subj_injected\n\n                    match_ref = cross_ref + other_target_injected[ref_rows]\n                    match_foc = cross_foc + other_target_injected[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    # All items in target subject are \"contaminated\" (injected)\n                    tpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_tpr = tpr - baseline_fpr[subj]  # baseline is p=0 rate\n\n                    target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, target_subject=subj,\n                        n_items=len(s_cols), tpr=tpr, fpr=np.nan,\n                        delta_tpr=delta_tpr, delta_fpr=np.nan,\n                        n_target_c=n_c, n_clean_c=np.nan\n                    ))\n\n                # ── DIF on each non-target subject (FPR measurement) ──\n                # Sample non-targets to keep runtime manageable for large k\n                # For k≤5, test all; for k>5, test 20 random non-targets\n                if len(non_target_subjects) <= 20:\n                    test_nontargets = non_target_subjects\n                else:\n                    test_nontargets = sorted(rng.choice(non_target_subjects,\n                                                        size=20, replace=False))\n\n                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n                    s_cols_set = set(s_cols.tolist())\n\n                    X_ref_s = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n                    X_foc_s = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n                    # Matching = everything except this subject\n                    # = non_target_total (minus this subject) + all injected target scores\n                    other_nontarget_cols = np.array([c for c in non_target_cols\n                                                     if c not in s_cols_set])\n                    other_nt_ref = np.asarray(mat[ref_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n                    other_nt_foc = np.asarray(mat[foc_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                    match_ref = other_nt_ref + injected_target_total[ref_rows]\n                    match_foc = other_nt_foc + injected_target_total[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_fpr = fpr - baseline_fpr[subj]\n\n                    non_target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, non_target_subject=subj,\n                        n_items=len(s_cols),\n                        fpr=fpr, baseline_fpr=baseline_fpr[subj],\n                        delta_fpr=delta_fpr\n                    ))\n\n    # ── Save results ──\n    target_df = pd.DataFrame(target_rows_list)\n    target_df.to_csv(OUT / \"multi_subject_injection_results.csv\", index=False)\n\n    nontarget_df = pd.DataFrame(non_target_rows_list)\n    nontarget_df.to_csv(OUT / \"non_target_fpr_results.csv\", index=False)\n\n    # ── Summary by k,p ──\n    summary_rows = []\n    for k in ks:\n        for p_val in ps:\n            t_sub = target_df[(target_df[\"k\"] == k) & (target_df[\"p\"] == p_val)]\n            nt_sub = nontarget_df[(nontarget_df[\"k\"] == k) & (nontarget_df[\"p\"] == p_val)]\n\n            mean_tpr = t_sub[\"tpr\"].mean() if len(t_sub) > 0 else np.nan\n            mean_delta_tpr = t_sub[\"delta_tpr\"].mean() if len(t_sub) > 0 else np.nan\n            std_delta_tpr = t_sub.groupby(\"seed\")[\"delta_tpr\"].mean().std() if len(t_sub) > 0 else np.nan\n\n            mean_fpr_nt = nt_sub[\"fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            mean_delta_fpr_nt = nt_sub[\"delta_fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            std_delta_fpr_nt = nt_sub.groupby(\"seed\")[\"delta_fpr\"].mean().std() if len(nt_sub) > 0 else np.nan\n\n            summary_rows.append(dict(\n                k=k, p=p_val,\n                mean_tpr_target=round(mean_tpr, 4),\n                mean_delta_tpr=round(mean_delta_tpr, 4),\n                std_delta_tpr=round(std_delta_tpr, 4) if not np.isnan(std_delta_tpr) else np.nan,\n                mean_fpr_non_target=round(mean_fpr_nt, 4),\n                mean_delta_fpr_non_target=round(mean_delta_fpr_nt, 4),\n                std_delta_fpr_non_target=round(std_delta_fpr_nt, 4) if not np.isnan(std_delta_fpr_nt) else np.nan,\n            ))\n\n    summary_df = pd.DataFrame(summary_rows)\n    summary_df.to_csv(OUT / \"summary_by_k.csv\", index=False)\n\n    elapsed = time.time() - t0\n    print(f\"\\nDone in {elapsed:.0f}s. Saved to {OUT}\")\n    print(\"\\nSummary:\")\n    print(summary_df.to_string(index=False))\n\n    return target_df, nontarget_df, summary_df\n\n\ndef generate_report(target_df, nontarget_df, summary_df):\n    lines = [\n        \"# Plan 034: Multi-Subject Simultaneous Injection — Report\",\n        \"\",\n        \"## Method\",\n        \"\",\n        \"We test Proposition 1's robustness boundary by simultaneously injecting\",\n        \"differential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).\",\n        \"For each (k, p, seed) combination:\",\n        \"\",\n        \"1. Randomly select k target subjects from 57 MMLU subjects\",\n        \"2. For each item in the k target subjects, flip incorrect→correct responses\",\n        \"   in the focal group (2024 models within accuracy overlap) with probability p\",\n        \"3. Compute cross-subject MH-DIF for each target and non-target subject\",\n        \"   - Matching variable = total score on all subjects EXCEPT the tested one\",\n        \"   - For target subjects: matching includes injected scores from other targets\",\n        \"   - For non-target subjects: matching includes all injected target scores\",\n        \"4. Measure TPR on target subjects and FPR on non-target subjects\",\n        \"\",\n        f\"Grid: k ∈ {{{','.join(map(str, KS))}}}, p ∈ {{{','.join(map(str, PS))}}}, \"\n        f\"5 seeds per combination = {len(KS)*len(PS)*N_SEEDS} runs\",\n        \"\",\n        \"## Core Results: ΔFPR by k and p\",\n        \"\",\n    ]\n\n    # Summary table\n    lines.append(\"### Target Subjects (TPR)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean TPR | Mean ΔTPR | SD(ΔTPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_tpr_target']:.4f} | \"\n                      f\"{row['mean_delta_tpr']:.4f} | \"\n                      f\"{row['std_delta_tpr']:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Non-Target Subjects (FPR — key result)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean FPR | Mean ΔFPR | SD(ΔFPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_fpr_non_target']:.4f} | \"\n                      f\"{row['mean_delta_fpr_non_target']:.4f} | \"\n                      f\"{row['std_delta_fpr_non_target']:.4f} |\")\n    lines.append(\"\")\n\n    # Key findings\n    lines.append(\"## Key Findings\")\n    lines.append(\"\")\n\n    # Find threshold where ΔFPR becomes notable\n    for p_val in PS:\n        sub = summary_df[summary_df[\"p\"] == p_val]\n        significant_k = sub[sub[\"mean_delta_fpr_non_target\"].abs() > 0.01]\n        if len(significant_k) > 0:\n            first_k = int(significant_k.iloc[0][\"k\"])\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR exceeds 0.01 at k={first_k}\")\n        else:\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR stays below 0.01 for all k tested\")\n\n    lines.append(\"\")\n    lines.append(\"## Interpretation\")\n    lines.append(\"\")\n    lines.append(\"Proposition 1 guarantees ΔFPR=0 when the matching variable is uncontaminated.\")\n    lines.append(\"As k increases, more of the cross-subject total score is contaminated,\")\n    lines.append(\"violating the proposition's assumption. The k at which ΔFPR becomes\")\n    lines.append(\"practically significant marks the validity boundary of cross-subject DIF auditing.\")\n    lines.append(\"\")\n\n    report_path = OUT / \"plan_034_report.md\"\n    report_path.write_text(\"\\n\".join(lines))\n    print(f\"Report saved to {report_path}\")\n\n\nif __name__ == \"__main__\":\n    parser = argparse.ArgumentParser(description=\"Plan 034: Multi-Subject Injection\")\n    parser.add_argument(\"--quick\", action=\"store_true\",\n                        help=\"Quick validation: k∈{1,5,20}, p=0.3, seed=1\")\n    args = parser.parse_args()\n\n    if args.quick:\n        target_df, nontarget_df, summary_df = run_experiment(\n            ks=[1, 5, 20], ps=[0.3], n_seeds=1)\n    else:\n        target_df, nontarget_df, summary_df = run_experiment()\n\n    generate_report(target_df, nontarget_df, summary_df)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "96899843-4daf-4880-841f-7437719c8840",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C4qM8AUgagqp3rdXd1XVVw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 157,
      "cache_read_input_tokens": 36489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 157
      },
      "output_tokens": 53,
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

_source line 40 · 2026-05-21T15:48:42.866Z_

<details><summary>↩ Tool result · `toolu_017FYT7RLMc7Y7pS7zvksxSq`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "7f7e8190-8aaf-425d-b565-b88aa1d283ba",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nplan_034: Multi-Subject Simultaneous Injection Experiment\n\nTests Proposition 1 (ΔFPR=0) robustness under multi-subject contamination.\nWhen k subjects are simultaneously injected, the cross-subject matching variable\n(total score on remaining 57-k uninjected subjects) degrades. ΔFPR(k) on\nnon-target subjects should increase with k, revealing the validity boundary.\n\nInputs:\n  - artifacts/response_matrix.npz         (5227 × 12508 sparse binary)\n  - artifacts/response_matrix_index.npz   (model_names, item_ids)\n  - artifacts/model_metadata.csv          (cohort_temporal, accuracy, ...)\n  - artifacts/item_metadata.csv           (item_id, subject, ...)\n\nOutputs:\n  - multi_subject_injection_results.csv   (per-target-subject DIF results)\n  - non_target_fpr_results.csv            (FPR on uninjected subjects)\n  - summary_by_k.csv                      (aggregated ΔFPR/ΔTPR by k,p)\n  - plan_034_report.md\n\nDependencies: numpy, pandas, scipy\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\nimport warnings\nimport argparse\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_034_multi_subject_injection\"\nOUT.mkdir(exist_ok=True)\n\nKS = [1, 2, 3, 5, 10, 20]\nPS = [0.1, 0.3, 0.5]\nN_SEEDS = 5\nN_STRATA = 5\nMIN_PER_STRATUM = 5\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE (from plan_016 with strata merging + external score support)\n# ════════════════════════════════════════════════════════════════════════════\ndef purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,\n                    external_scores_foc=None, min_per_stratum=5):\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])\n\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n\n        n_bins = len(edges) - 1\n        k_all = np.digitize(s_all, edges[1:-1])\n        strata_labels = _merge_small_strata(k_all, groups_all, n_bins, min_per_stratum)\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        x_all = np.concatenate([X_ref[:, j], X_foc[:, j]])\n\n        for k in np.unique(strata_labels):\n            mask_k = (strata_labels == k)\n            mask_ref = mask_k & (groups_all == 0)\n            mask_foc = mask_k & (groups_all == 1)\n\n            n1 = int(mask_ref.sum())\n            n0 = int(mask_foc.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(x_all[mask_ref].sum())\n            B = float(n1 - A)\n            C = float(x_all[mask_foc].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else np.inf\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets,\n                         n_strata_used=n_ok))\n\n    return pd.DataFrame(rows)\n\n\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\",\n                n_strata_used=0)\n\n\ndef _merge_small_strata(k_all, groups_all, n_bins, min_n):\n    labels = k_all.copy()\n    merged = True\n    while merged:\n        merged = False\n        unique_strata = sorted(np.unique(labels))\n        for i, k in enumerate(unique_strata):\n            mask_k = (labels == k)\n            n_ref = int((mask_k & (groups_all == 0)).sum())\n            n_foc = int((mask_k & (groups_all == 1)).sum())\n            if n_ref < min_n or n_foc < min_n:\n                if i + 1 < len(unique_strata):\n                    next_k = unique_strata[i + 1]\n                    labels[labels == next_k] = k\n                elif i > 0:\n                    prev_k = unique_strata[i - 1]\n                    labels[labels == k] = prev_k\n                merged = True\n                break\n    return labels\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\ndef load_data():\n    mat = load_npz(BASE / \"response_matrix.npz\")\n    idx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n    item2col = {iid: i for i, iid in enumerate(item_ids)}\n\n    model_meta = pd.read_csv(BASE / \"model_metadata.csv\")\n    item_meta = pd.read_csv(BASE / \"item_metadata.csv\")\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    # Temporal cohorts\n    ref_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"model_name\"]\n    foc_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"model_name\"]\n    ref_rows = np.array([name2row[n] for n in ref_names if n in name2row])\n    foc_rows = np.array([name2row[n] for n in foc_names if n in name2row])\n\n    # Focal inject subset: 2024 models in accuracy overlap with 2023\n    ref_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\n    foc_df = model_meta[model_meta[\"cohort_temporal\"] == \"2024\"]\n    t_min = max(ref_acc.min(), foc_df[\"accuracy\"].min())\n    t_max = min(ref_acc.max(), foc_df[\"accuracy\"].max())\n    foc_inject_mask = (foc_df[\"accuracy\"] >= t_min) & (foc_df[\"accuracy\"] <= t_max)\n    foc_inject_rows = np.array([name2row[n] for n in foc_df.loc[foc_inject_mask, \"model_name\"]\n                                if n in name2row])\n\n    # Build subject → column indices mapping\n    subject_cols = {}\n    subjects = sorted(item_meta[\"subject\"].unique())\n    for subj in subjects:\n        ids = item_meta.loc[item_meta[\"subject\"] == subj, \"item_id\"].values\n        cols = np.array([item2col[iid] for iid in ids if iid in item2col])\n        subject_cols[subj] = cols\n\n    return mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MAIN EXPERIMENT\n# ════════════════════════════════════════════════════════════════════════════\ndef run_experiment(ks=KS, ps=PS, n_seeds=N_SEEDS):\n    t0 = time.time()\n    mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols = load_data()\n    print(f\"Data loaded: {len(ref_rows)} ref, {len(foc_rows)} foc, \"\n          f\"{len(foc_inject_rows)} foc_inject, {len(subjects)} subjects\")\n\n    all_cols = np.concatenate([subject_cols[s] for s in subjects])\n    all_cols_set = set(all_cols.tolist())\n\n    # ── Phase 1: baseline (p=0) per-subject FPR with cross-subject matching ──\n    # Baseline uses full uninjected cross-subject scores\n    print(\"Computing baseline FPR (p=0) for all subjects...\")\n    baseline_fpr = {}\n    baseline_n_c = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        other_cols = np.array([c for c in all_cols if c not in set(s_cols.tolist())])\n\n        cross_ref = np.asarray(mat[ref_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)\n        cross_foc = np.asarray(mat[foc_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)\n\n        X_ref = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n        X_foc = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n        n_strata = 3 if len(s_cols) < 100 else N_STRATA\n        dif = purified_mh_dif(X_ref, X_foc, n_strata=n_strata,\n                              external_scores_ref=cross_ref,\n                              external_scores_foc=cross_foc,\n                              min_per_stratum=MIN_PER_STRATUM)\n        n_c = int((dif[\"ets_class\"] == \"C\").sum())\n        fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n        baseline_fpr[subj] = fpr\n        baseline_n_c[subj] = n_c\n\n    print(f\"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}\")\n\n    # ── Phase 2: injection runs ──\n    target_rows_list = []\n    non_target_rows_list = []\n    total_runs = len(ks) * len(ps) * n_seeds\n    run_i = 0\n\n    for k in ks:\n        for p in ps:\n            for seed in range(1, n_seeds + 1):\n                run_i += 1\n                rng = np.random.RandomState(seed)\n                target_subjects = sorted(rng.choice(subjects, size=k, replace=False))\n                non_target_subjects = [s for s in subjects if s not in target_subjects]\n\n                # Build injected matrix columns for target subjects\n                # Collect all target columns for injection\n                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])\n                target_cols_set = set(target_cols_all.tolist())\n                non_target_cols = np.array([c for c in all_cols if c not in target_cols_set])\n\n                # Inject: flip incorrect→correct for focal inject models on target items\n                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    for local_j in range(len(target_cols_all)):\n                        for model_row in foc_inject_rows:\n                            if mat_dense_targets[model_row, local_j] == 0:\n                                if rng.random() < p:\n                                    mat_dense_targets[model_row, local_j] = 1\n                                    n_flipped += 1\n\n                # Cross-subject matching variable = total on uninjected subjects\n                # (from original matrix — non-target subjects are never injected)\n                cross_ref = np.asarray(mat[ref_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n                cross_foc = np.asarray(mat[foc_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                # But for target subjects, the matching variable includes OTHER\n                # target subjects' injected scores too. We need per-subject matching.\n                # For target subject s: matching = non_target_total + injected_other_targets\n                # For non-target subject s: matching = non_target_total_minus_s + all_target_injected\n\n                # Precompute injected target total per model (from injected matrix)\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                # Build local col mapping: target_cols_all[local_idx] → local_idx\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}\n\n                elapsed = time.time() - t0\n                print(f\"  [{run_i}/{total_runs}] k={k} p={p} seed={seed} \"\n                      f\"flipped={n_flipped} ({elapsed:.0f}s)\")\n\n                # ── DIF on each target subject ──\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    # Matching variable for target subject: everything EXCEPT this subject\n                    # = non_target_total + injected scores from OTHER target subjects\n                    this_subj_injected = X_subj_inj.sum(axis=1).astype(np.float64)\n                    other_target_injected = injected_target_total - this_subj_injected\n\n                    match_ref = cross_ref + other_target_injected[ref_rows]\n                    match_foc = cross_foc + other_target_injected[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    # All items in target subject are \"contaminated\" (injected)\n                    tpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_tpr = tpr - baseline_fpr[subj]  # baseline is p=0 rate\n\n                    target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, target_subject=subj,\n                        n_items=len(s_cols), tpr=tpr, fpr=np.nan,\n                        delta_tpr=delta_tpr, delta_fpr=np.nan,\n                        n_target_c=n_c, n_clean_c=np.nan\n                    ))\n\n                # ── DIF on each non-target subject (FPR measurement) ──\n                # Sample non-targets to keep runtime manageable for large k\n                # For k≤5, test all; for k>5, test 20 random non-targets\n                if len(non_target_subjects) <= 20:\n                    test_nontargets = non_target_subjects\n                else:\n                    test_nontargets = sorted(rng.choice(non_target_subjects,\n                                                        size=20, replace=False))\n\n                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n                    s_cols_set = set(s_cols.tolist())\n\n                    X_ref_s = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n                    X_foc_s = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n                    # Matching = everything except this subject\n                    # = non_target_total (minus this subject) + all injected target scores\n                    other_nontarget_cols = np.array([c for c in non_target_cols\n                                                     if c not in s_cols_set])\n                    other_nt_ref = np.asarray(mat[ref_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n                    other_nt_foc = np.asarray(mat[foc_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                    match_ref = other_nt_ref + injected_target_total[ref_rows]\n                    match_foc = other_nt_foc + injected_target_total[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_fpr = fpr - baseline_fpr[subj]\n\n                    non_target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, non_target_subject=subj,\n                        n_items=len(s_cols),\n                        fpr=fpr, baseline_fpr=baseline_fpr[subj],\n                        delta_fpr=delta_fpr\n                    ))\n\n    # ── Save results ──\n    target_df = pd.DataFrame(target_rows_list)\n    target_df.to_csv(OUT / \"multi_subject_injection_results.csv\", index=False)\n\n    nontarget_df = pd.DataFrame(non_target_rows_list)\n    nontarget_df.to_csv(OUT / \"non_target_fpr_results.csv\", index=False)\n\n    # ── Summary by k,p ──\n    summary_rows = []\n    for k in ks:\n        for p_val in ps:\n            t_sub = target_df[(target_df[\"k\"] == k) & (target_df[\"p\"] == p_val)]\n            nt_sub = nontarget_df[(nontarget_df[\"k\"] == k) & (nontarget_df[\"p\"] == p_val)]\n\n            mean_tpr = t_sub[\"tpr\"].mean() if len(t_sub) > 0 else np.nan\n            mean_delta_tpr = t_sub[\"delta_tpr\"].mean() if len(t_sub) > 0 else np.nan\n            std_delta_tpr = t_sub.groupby(\"seed\")[\"delta_tpr\"].mean().std() if len(t_sub) > 0 else np.nan\n\n            mean_fpr_nt = nt_sub[\"fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            mean_delta_fpr_nt = nt_sub[\"delta_fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            std_delta_fpr_nt = nt_sub.groupby(\"seed\")[\"delta_fpr\"].mean().std() if len(nt_sub) > 0 else np.nan\n\n            summary_rows.append(dict(\n                k=k, p=p_val,\n                mean_tpr_target=round(mean_tpr, 4),\n                mean_delta_tpr=round(mean_delta_tpr, 4),\n                std_delta_tpr=round(std_delta_tpr, 4) if not np.isnan(std_delta_tpr) else np.nan,\n                mean_fpr_non_target=round(mean_fpr_nt, 4),\n                mean_delta_fpr_non_target=round(mean_delta_fpr_nt, 4),\n                std_delta_fpr_non_target=round(std_delta_fpr_nt, 4) if not np.isnan(std_delta_fpr_nt) else np.nan,\n            ))\n\n    summary_df = pd.DataFrame(summary_rows)\n    summary_df.to_csv(OUT / \"summary_by_k.csv\", index=False)\n\n    elapsed = time.time() - t0\n    print(f\"\\nDone in {elapsed:.0f}s. Saved to {OUT}\")\n    print(\"\\nSummary:\")\n    print(summary_df.to_string(index=False))\n\n    return target_df, nontarget_df, summary_df\n\n\ndef generate_report(target_df, nontarget_df, summary_df):\n    lines = [\n        \"# Plan 034: Multi-Subject Simultaneous Injection — Report\",\n        \"\",\n        \"## Method\",\n        \"\",\n        \"We test Proposition 1's robustness boundary by simultaneously injecting\",\n        \"differential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).\",\n        \"For each (k, p, seed) combination:\",\n        \"\",\n        \"1. Randomly select k target subjects from 57 MMLU subjects\",\n        \"2. For each item in the k target subjects, flip incorrect→correct responses\",\n        \"   in the focal group (2024 models within accuracy overlap) with probability p\",\n        \"3. Compute cross-subject MH-DIF for each target and non-target subject\",\n        \"   - Matching variable = total score on all subjects EXCEPT the tested one\",\n        \"   - For target subjects: matching includes injected scores from other targets\",\n        \"   - For non-target subjects: matching includes all injected target scores\",\n        \"4. Measure TPR on target subjects and FPR on non-target subjects\",\n        \"\",\n        f\"Grid: k ∈ {{{','.join(map(str, KS))}}}, p ∈ {{{','.join(map(str, PS))}}}, \"\n        f\"5 seeds per combination = {len(KS)*len(PS)*N_SEEDS} runs\",\n        \"\",\n        \"## Core Results: ΔFPR by k and p\",\n        \"\",\n    ]\n\n    # Summary table\n    lines.append(\"### Target Subjects (TPR)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean TPR | Mean ΔTPR | SD(ΔTPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_tpr_target']:.4f} | \"\n                      f\"{row['mean_delta_tpr']:.4f} | \"\n                      f\"{row['std_delta_tpr']:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Non-Target Subjects (FPR — key result)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean FPR | Mean ΔFPR | SD(ΔFPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_fpr_non_target']:.4f} | \"\n                      f\"{row['mean_delta_fpr_non_target']:.4f} | \"\n                      f\"{row['std_delta_fpr_non_target']:.4f} |\")\n    lines.append(\"\")\n\n    # Key findings\n    lines.append(\"## Key Findings\")\n    lines.append(\"\")\n\n    # Find threshold where ΔFPR becomes notable\n    for p_val in PS:\n        sub = summary_df[summary_df[\"p\"] == p_val]\n        significant_k = sub[sub[\"mean_delta_fpr_non_target\"].abs() > 0.01]\n        if len(significant_k) > 0:\n            first_k = int(significant_k.iloc[0][\"k\"])\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR exceeds 0.01 at k={first_k}\")\n        else:\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR stays below 0.01 for all k tested\")\n\n    lines.append(\"\")\n    lines.append(\"## Interpretation\")\n    lines.append(\"\")\n    lines.append(\"Proposition 1 guarantees ΔFPR=0 when the matching variable is uncontaminated.\")\n    lines.append(\"As k increases, more of the cross-subject total score is contaminated,\")\n    lines.append(\"violating the proposition's assumption. The k at which ΔFPR becomes\")\n    lines.append(\"practically significant marks the validity boundary of cross-subject DIF auditing.\")\n    lines.append(\"\")\n\n    report_path = OUT / \"plan_034_report.md\"\n    report_path.write_text(\"\\n\".join(lines))\n    print(f\"Report saved to {report_path}\")\n\n\nif __name__ == \"__main__\":\n    parser = argparse.ArgumentParser(description=\"Plan 034: Multi-Subject Injection\")\n    parser.add_argument(\"--quick\", action=\"store_true\",\n                        help=\"Quick validation: k∈{1,5,20}, p=0.3, seed=1\")\n    args = parser.parse_args()\n\n    if args.quick:\n        target_df, nontarget_df, summary_df = run_experiment(\n            ks=[1, 5, 20], ps=[0.3], n_seeds=1)\n    else:\n        target_df, nontarget_df, summary_df = run_experiment()\n\n    generate_report(target_df, nontarget_df, summary_df)\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 41_

Now let me run the quick validation first to verify correctness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "db906b82-7542-44ae-af21-afc3f8f7dc18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CuVL3jt6C5nFFxsmhaXSUc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8040,
      "cache_read_input_tokens": 36646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8040
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

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01F55aisDxkbwDKLBHJNdmcr`</summary>

```json
{
  "command": "python3 artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py --quick 2>&1",
  "description": "Quick validation run (k∈{1,5,20}, p=0.3, seed=1)",
  "timeout": 600000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "7fd54d52-6078-4238-b24d-772e11c6bcde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CuVL3jt6C5nFFxsmhaXSUc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8040,
      "cache_read_input_tokens": 36646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8040
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

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bohf16z64",
  "tool_use_id": "toolu_01F55aisDxkbwDKLBHJNdmcr",
  "description": "Quick validation run (k∈{1,5,20}, p=0.3, seed=1)",
  "task_type": "local_bash",
  "uuid": "99179dfb-7afc-4a0a-9e90-69ce48b631ef",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c"
}
```

---

### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bohf16z64",
  "tool_use_id": "toolu_01F55aisDxkbwDKLBHJNdmcr",
  "status": "completed",
  "output_file": "",
  "summary": "Quick validation run (k∈{1,5,20}, p=0.3, seed=1)",
  "uuid": "e76a6c19-0fe8-4cf4-9655-acfaf6176a3a",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c"
}
```

---

### Tool result

_source line 45 · 2026-05-21T15:49:49.081Z_

<details><summary>↩ Tool result · `toolu_01F55aisDxkbwDKLBHJNdmcr`</summary>

```text
Data loaded: 1080 ref, 807 foc, 787 foc_inject, 57 subjects
Computing baseline FPR (p=0) for all subjects...
Baseline done. Mean FPR = 0.3136
  [1/3] k=1 p=0.3 seed=1 flipped=30238 (31s)
  [2/3] k=5 p=0.3 seed=1 flipped=77534 (40s)
  [3/3] k=20 p=0.3 seed=1 flipped=317129 (51s)

Done in 61s. Saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection

Summary:
 k   p  mean_tpr_target  mean_delta_tpr  std_delta_tpr  mean_fpr_non_target  mean_delta_fpr_non_target  std_delta_fpr_non_target
 1 0.3           0.5744          0.2025            NaN               0.3099                     0.0033                       NaN
 5 0.3           0.4555          0.1269            NaN               0.3130                    -0.0007                       NaN
20 0.3           0.3775          0.0607            NaN               0.3577                     0.0614                       NaN
Report saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "93f85fa1-cdb8-4be4-a915-2525ecc184fd",
  "tool_use_result": {
    "stdout": "Data loaded: 1080 ref, 807 foc, 787 foc_inject, 57 subjects\nComputing baseline FPR (p=0) for all subjects...\nBaseline done. Mean FPR = 0.3136\n  [1/3] k=1 p=0.3 seed=1 flipped=30238 (31s)\n  [2/3] k=5 p=0.3 seed=1 flipped=77534 (40s)\n  [3/3] k=20 p=0.3 seed=1 flipped=317129 (51s)\n\nDone in 61s. Saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection\n\nSummary:\n k   p  mean_tpr_target  mean_delta_tpr  std_delta_tpr  mean_fpr_non_target  mean_delta_fpr_non_target  std_delta_fpr_non_target\n 1 0.3           0.5744          0.2025            NaN               0.3099                     0.0033                       NaN\n 5 0.3           0.4555          0.1269            NaN               0.3130                    -0.0007                       NaN\n20 0.3           0.3775          0.0607            NaN               0.3577                     0.0614                       NaN\nReport saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md",
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
Quick validation results look correct:
- k=1, p=0.3: ΔFPR non-target = 0.0033 ≈ 0 (confirms Proposition 1 — matching variable barely polluted)
- k=5, p=0.3: ΔFPR non-target = -0.0007 ≈ 0 (still robust)
- k=20, p=0.3: ΔFPR non-target = 0.0614 > 0 (matching variable significantly polluted → FPR inflates)

This is exactly the expected pattern. The injection performance looks reasonable.


The full run will take around 30 minutes at the current pace, which fits within the task requirements. The real bottleneck is computing DIF for each non-target subject since it requires separate sparse matrix operations, but I should focus on vectorizing the injection loop with numpy to speed things up first. me look at the runtime breakdown more carefully. The baseline took 31s for 57 subjects. Each run needs ~10s for both target and non-target DIF. With 90 runs, that's ~900s = 15 min plus 31s baseline = ~16 min total. That's fine.

But wait — I should also check if the injection code is correct. Let me verify:

1. For k=1, non-target ΔFPR ≈ 0 ✓ (Proposition 1 holds when matching variable is almost entirely clean)
2. For k=20, non-target ΔFPR = 0.06 ✓ (significant pollution of matching variable)

The injection loop is O(n_target_items × n_foc_inject_models), which for k=20 is ~4400 items × 787 models = ~3.5M iterations. That's slow in pure Python. I need to vectorize the injection logic to speed things up.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "b41f22d8-e6bb-4dfe-89b5-f3bea406d081",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgvCXD6cJnLKf4fuUpx2ii",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 44686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 694
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

Quick run validates correctly: k=1 ΔFPR≈0 (Proposition 1 holds), k=20 ΔFPR=0.06 (matching variable pollution). Let me optimize the injection loop before the full run — the per-element Python loop is slow.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "4575f744-16a7-4c74-b764-539a9b5752f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgvCXD6cJnLKf4fuUpx2ii",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 44686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 694
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

<details open><summary>🔧 Tool call — Read · `toolu_01AnMsB51zqDwZZHvdAUzYMy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
  "offset": 208,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "3e242fe3-4773-4b70-b145-0f69fe5ac662",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SgvCXD6cJnLKf4fuUpx2ii",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 694,
      "cache_read_input_tokens": 44686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 694
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

_source line 49 · 2026-05-21T15:50:10.403Z_

<details><summary>↩ Tool result · `toolu_01AnMsB51zqDwZZHvdAUzYMy`</summary>

```text
208	    # Focal inject subset: 2024 models in accuracy overlap with 2023
209	    ref_acc = model_meta.loc[model_meta["cohort_temporal"] == "2023", "accuracy"]
210	    foc_df = model_meta[model_meta["cohort_temporal"] == "2024"]
211	    t_min = max(ref_acc.min(), foc_df["accuracy"].min())
212	    t_max = min(ref_acc.max(), foc_df["accuracy"].max())
213	    foc_inject_mask = (foc_df["accuracy"] >= t_min) & (foc_df["accuracy"] <= t_max)
214	    foc_inject_rows = np.array([name2row[n] for n in foc_df.loc[foc_inject_mask, "model_name"]
215	                                if n in name2row])
216	
217	    # Build subject → column indices mapping
218	    subject_cols = {}
219	    subjects = sorted(item_meta["subject"].unique())
220	    for subj in subjects:
221	        ids = item_meta.loc[item_meta["subject"] == subj, "item_id"].values
222	        cols = np.array([item2col[iid] for iid in ids if iid in item2col])
223	        subject_cols[subj] = cols
224	
225	    return mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols
226	
227	
228	# ════════════════════════════════════════════════════════════════════════════
229	#  MAIN EXPERIMENT
230	# ════════════════════════════════════════════════════════════════════════════
231	def run_experiment(ks=KS, ps=PS, n_seeds=N_SEEDS):
232	    t0 = time.time()
233	    mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols = load_data()
234	    print(f"Data loaded: {len(ref_rows)} ref, {len(foc_rows)} foc, "
235	          f"{len(foc_inject_rows)} foc_inject, {len(subjects)} subjects")
236	
237	    all_cols = np.concatenate([subject_cols[s] for s in subjects])
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "585300eb-fc87-4f8e-aa9e-6457d1d2ea85",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
      "content": "    # Focal inject subset: 2024 models in accuracy overlap with 2023\n    ref_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\n    foc_df = model_meta[model_meta[\"cohort_temporal\"] == \"2024\"]\n    t_min = max(ref_acc.min(), foc_df[\"accuracy\"].min())\n    t_max = min(ref_acc.max(), foc_df[\"accuracy\"].max())\n    foc_inject_mask = (foc_df[\"accuracy\"] >= t_min) & (foc_df[\"accuracy\"] <= t_max)\n    foc_inject_rows = np.array([name2row[n] for n in foc_df.loc[foc_inject_mask, \"model_name\"]\n                                if n in name2row])\n\n    # Build subject → column indices mapping\n    subject_cols = {}\n    subjects = sorted(item_meta[\"subject\"].unique())\n    for subj in subjects:\n        ids = item_meta.loc[item_meta[\"subject\"] == subj, \"item_id\"].values\n        cols = np.array([item2col[iid] for iid in ids if iid in item2col])\n        subject_cols[subj] = cols\n\n    return mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MAIN EXPERIMENT\n# ════════════════════════════════════════════════════════════════════════════\ndef run_experiment(ks=KS, ps=PS, n_seeds=N_SEEDS):\n    t0 = time.time()\n    mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols = load_data()\n    print(f\"Data loaded: {len(ref_rows)} ref, {len(foc_rows)} foc, \"\n          f\"{len(foc_inject_rows)} foc_inject, {len(subjects)} subjects\")\n\n    all_cols = np.concatenate([subject_cols[s] for s in subjects])",
      "numLines": 30,
      "startLine": 208,
      "totalLines": 527
    }
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_01LjjbGnp841NDUKjPsTr7t5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
  "old_string": "                # Inject: flip incorrect→correct for focal inject models on target items\n                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    for local_j in range(len(target_cols_all)):\n                        for model_row in foc_inject_rows:\n                            if mat_dense_targets[model_row, local_j] == 0:\n                                if rng.random() < p:\n                                    mat_dense_targets[model_row, local_j] = 1\n                                    n_flipped += 1",
  "new_string": "                # Inject: flip incorrect→correct for focal inject models on target items\n                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    block = mat_dense_targets[foc_inject_rows]\n                    zeros = (block == 0)\n                    flip_mask = zeros & (rng.random(block.shape) < p)\n                    n_flipped = int(flip_mask.sum())\n                    mat_dense_targets[foc_inject_rows] = block + flip_mask.astype(np.int8)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "83f37f8a-7669-4d96-bb16-fe02e7b1d83d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAyScgHrAGeTaXuK3qui2u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1373,
      "cache_read_input_tokens": 45380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1373
      },
      "output_tokens": 61,
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

_source line 51 · 2026-05-21T15:50:19.044Z_

<details><summary>↩ Tool result · `toolu_01LjjbGnp841NDUKjPsTr7t5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "2813350e-0ab3-44b2-8ea7-abf69c227bf0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
    "oldString": "                # Inject: flip incorrect→correct for focal inject models on target items\n                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    for local_j in range(len(target_cols_all)):\n                        for model_row in foc_inject_rows:\n                            if mat_dense_targets[model_row, local_j] == 0:\n                                if rng.random() < p:\n                                    mat_dense_targets[model_row, local_j] = 1\n                                    n_flipped += 1",
    "newString": "                # Inject: flip incorrect→correct for focal inject models on target items\n                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    block = mat_dense_targets[foc_inject_rows]\n                    zeros = (block == 0)\n                    flip_mask = zeros & (rng.random(block.shape) < p)\n                    n_flipped = int(flip_mask.sum())\n                    mat_dense_targets[foc_inject_rows] = block + flip_mask.astype(np.int8)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nplan_034: Multi-Subject Simultaneous Injection Experiment\n\nTests Proposition 1 (ΔFPR=0) robustness under multi-subject contamination.\nWhen k subjects are simultaneously injected, the cross-subject matching variable\n(total score on remaining 57-k uninjected subjects) degrades. ΔFPR(k) on\nnon-target subjects should increase with k, revealing the validity boundary.\n\nInputs:\n  - artifacts/response_matrix.npz         (5227 × 12508 sparse binary)\n  - artifacts/response_matrix_index.npz   (model_names, item_ids)\n  - artifacts/model_metadata.csv          (cohort_temporal, accuracy, ...)\n  - artifacts/item_metadata.csv           (item_id, subject, ...)\n\nOutputs:\n  - multi_subject_injection_results.csv   (per-target-subject DIF results)\n  - non_target_fpr_results.csv            (FPR on uninjected subjects)\n  - summary_by_k.csv                      (aggregated ΔFPR/ΔTPR by k,p)\n  - plan_034_report.md\n\nDependencies: numpy, pandas, scipy\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\nimport warnings\nimport argparse\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_034_multi_subject_injection\"\nOUT.mkdir(exist_ok=True)\n\nKS = [1, 2, 3, 5, 10, 20]\nPS = [0.1, 0.3, 0.5]\nN_SEEDS = 5\nN_STRATA = 5\nMIN_PER_STRATUM = 5\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE (from plan_016 with strata merging + external score support)\n# ════════════════════════════════════════════════════════════════════════════\ndef purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,\n                    external_scores_foc=None, min_per_stratum=5):\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])\n\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n\n        n_bins = len(edges) - 1\n        k_all = np.digitize(s_all, edges[1:-1])\n        strata_labels = _merge_small_strata(k_all, groups_all, n_bins, min_per_stratum)\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        x_all = np.concatenate([X_ref[:, j], X_foc[:, j]])\n\n        for k in np.unique(strata_labels):\n            mask_k = (strata_labels == k)\n            mask_ref = mask_k & (groups_all == 0)\n            mask_foc = mask_k & (groups_all == 1)\n\n            n1 = int(mask_ref.sum())\n            n0 = int(mask_foc.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(x_all[mask_ref].sum())\n            B = float(n1 - A)\n            C = float(x_all[mask_foc].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else np.inf\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets,\n                         n_strata_used=n_ok))\n\n    return pd.DataFrame(rows)\n\n\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\",\n                n_strata_used=0)\n\n\ndef _merge_small_strata(k_all, groups_all, n_bins, min_n):\n    labels = k_all.copy()\n    merged = True\n    while merged:\n        merged = False\n        unique_strata = sorted(np.unique(labels))\n        for i, k in enumerate(unique_strata):\n            mask_k = (labels == k)\n            n_ref = int((mask_k & (groups_all == 0)).sum())\n            n_foc = int((mask_k & (groups_all == 1)).sum())\n            if n_ref < min_n or n_foc < min_n:\n                if i + 1 < len(unique_strata):\n                    next_k = unique_strata[i + 1]\n                    labels[labels == next_k] = k\n                elif i > 0:\n                    prev_k = unique_strata[i - 1]\n                    labels[labels == k] = prev_k\n                merged = True\n                break\n    return labels\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\ndef load_data():\n    mat = load_npz(BASE / \"response_matrix.npz\")\n    idx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n    item2col = {iid: i for i, iid in enumerate(item_ids)}\n\n    model_meta = pd.read_csv(BASE / \"model_metadata.csv\")\n    item_meta = pd.read_csv(BASE / \"item_metadata.csv\")\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    # Temporal cohorts\n    ref_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"model_name\"]\n    foc_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"model_name\"]\n    ref_rows = np.array([name2row[n] for n in ref_names if n in name2row])\n    foc_rows = np.array([name2row[n] for n in foc_names if n in name2row])\n\n    # Focal inject subset: 2024 models in accuracy overlap with 2023\n    ref_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\n    foc_df = model_meta[model_meta[\"cohort_temporal\"] == \"2024\"]\n    t_min = max(ref_acc.min(), foc_df[\"accuracy\"].min())\n    t_max = min(ref_acc.max(), foc_df[\"accuracy\"].max())\n    foc_inject_mask = (foc_df[\"accuracy\"] >= t_min) & (foc_df[\"accuracy\"] <= t_max)\n    foc_inject_rows = np.array([name2row[n] for n in foc_df.loc[foc_inject_mask, \"model_name\"]\n                                if n in name2row])\n\n    # Build subject → column indices mapping\n    subject_cols = {}\n    subjects = sorted(item_meta[\"subject\"].unique())\n    for subj in subjects:\n        ids = item_meta.loc[item_meta[\"subject\"] == subj, \"item_id\"].values\n        cols = np.array([item2col[iid] for iid in ids if iid in item2col])\n        subject_cols[subj] = cols\n\n    return mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MAIN EXPERIMENT\n# ════════════════════════════════════════════════════════════════════════════\ndef run_experiment(ks=KS, ps=PS, n_seeds=N_SEEDS):\n    t0 = time.time()\n    mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols = load_data()\n    print(f\"Data loaded: {len(ref_rows)} ref, {len(foc_rows)} foc, \"\n          f\"{len(foc_inject_rows)} foc_inject, {len(subjects)} subjects\")\n\n    all_cols = np.concatenate([subject_cols[s] for s in subjects])\n    all_cols_set = set(all_cols.tolist())\n\n    # ── Phase 1: baseline (p=0) per-subject FPR with cross-subject matching ──\n    # Baseline uses full uninjected cross-subject scores\n    print(\"Computing baseline FPR (p=0) for all subjects...\")\n    baseline_fpr = {}\n    baseline_n_c = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        other_cols = np.array([c for c in all_cols if c not in set(s_cols.tolist())])\n\n        cross_ref = np.asarray(mat[ref_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)\n        cross_foc = np.asarray(mat[foc_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)\n\n        X_ref = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n        X_foc = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n        n_strata = 3 if len(s_cols) < 100 else N_STRATA\n        dif = purified_mh_dif(X_ref, X_foc, n_strata=n_strata,\n                              external_scores_ref=cross_ref,\n                              external_scores_foc=cross_foc,\n                              min_per_stratum=MIN_PER_STRATUM)\n        n_c = int((dif[\"ets_class\"] == \"C\").sum())\n        fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n        baseline_fpr[subj] = fpr\n        baseline_n_c[subj] = n_c\n\n    print(f\"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}\")\n\n    # ── Phase 2: injection runs ──\n    target_rows_list = []\n    non_target_rows_list = []\n    total_runs = len(ks) * len(ps) * n_seeds\n    run_i = 0\n\n    for k in ks:\n        for p in ps:\n            for seed in range(1, n_seeds + 1):\n                run_i += 1\n                rng = np.random.RandomState(seed)\n                target_subjects = sorted(rng.choice(subjects, size=k, replace=False))\n                non_target_subjects = [s for s in subjects if s not in target_subjects]\n\n                # Build injected matrix columns for target subjects\n                # Collect all target columns for injection\n                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])\n                target_cols_set = set(target_cols_all.tolist())\n                non_target_cols = np.array([c for c in all_cols if c not in target_cols_set])\n\n                # Inject: flip incorrect→correct for focal inject models on target items\n                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    for local_j in range(len(target_cols_all)):\n                        for model_row in foc_inject_rows:\n                            if mat_dense_targets[model_row, local_j] == 0:\n                                if rng.random() < p:\n                                    mat_dense_targets[model_row, local_j] = 1\n                                    n_flipped += 1\n\n                # Cross-subject matching variable = total on uninjected subjects\n                # (from original matrix — non-target subjects are never injected)\n                cross_ref = np.asarray(mat[ref_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n                cross_foc = np.asarray(mat[foc_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                # But for target subjects, the matching variable includes OTHER\n                # target subjects' injected scores too. We need per-subject matching.\n                # For target subject s: matching = non_target_total + injected_other_targets\n                # For non-target subject s: matching = non_target_total_minus_s + all_target_injected\n\n                # Precompute injected target total per model (from injected matrix)\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                # Build local col mapping: target_cols_all[local_idx] → local_idx\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}\n\n                elapsed = time.time() - t0\n                print(f\"  [{run_i}/{total_runs}] k={k} p={p} seed={seed} \"\n                      f\"flipped={n_flipped} ({elapsed:.0f}s)\")\n\n                # ── DIF on each target subject ──\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    # Matching variable for target subject: everything EXCEPT this subject\n                    # = non_target_total + injected scores from OTHER target subjects\n                    this_subj_injected = X_subj_inj.sum(axis=1).astype(np.float64)\n                    other_target_injected = injected_target_total - this_subj_injected\n\n                    match_ref = cross_ref + other_target_injected[ref_rows]\n                    match_foc = cross_foc + other_target_injected[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    # All items in target subject are \"contaminated\" (injected)\n                    tpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_tpr = tpr - baseline_fpr[subj]  # baseline is p=0 rate\n\n                    target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, target_subject=subj,\n                        n_items=len(s_cols), tpr=tpr, fpr=np.nan,\n                        delta_tpr=delta_tpr, delta_fpr=np.nan,\n                        n_target_c=n_c, n_clean_c=np.nan\n                    ))\n\n                # ── DIF on each non-target subject (FPR measurement) ──\n                # Sample non-targets to keep runtime manageable for large k\n                # For k≤5, test all; for k>5, test 20 random non-targets\n                if len(non_target_subjects) <= 20:\n                    test_nontargets = non_target_subjects\n                else:\n                    test_nontargets = sorted(rng.choice(non_target_subjects,\n                                                        size=20, replace=False))\n\n                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n                    s_cols_set = set(s_cols.tolist())\n\n                    X_ref_s = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n                    X_foc_s = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n                    # Matching = everything except this subject\n                    # = non_target_total (minus this subject) + all injected target scores\n                    other_nontarget_cols = np.array([c for c in non_target_cols\n                                                     if c not in s_cols_set])\n                    other_nt_ref = np.asarray(mat[ref_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n                    other_nt_foc = np.asarray(mat[foc_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                    match_ref = other_nt_ref + injected_target_total[ref_rows]\n                    match_foc = other_nt_foc + injected_target_total[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_fpr = fpr - baseline_fpr[subj]\n\n                    non_target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, non_target_subject=subj,\n                        n_items=len(s_cols),\n                        fpr=fpr, baseline_fpr=baseline_fpr[subj],\n                        delta_fpr=delta_fpr\n                    ))\n\n    # ── Save results ──\n    target_df = pd.DataFrame(target_rows_list)\n    target_df.to_csv(OUT / \"multi_subject_injection_results.csv\", index=False)\n\n    nontarget_df = pd.DataFrame(non_target_rows_list)\n    nontarget_df.to_csv(OUT / \"non_target_fpr_results.csv\", index=False)\n\n    # ── Summary by k,p ──\n    summary_rows = []\n    for k in ks:\n        for p_val in ps:\n            t_sub = target_df[(target_df[\"k\"] == k) & (target_df[\"p\"] == p_val)]\n            nt_sub = nontarget_df[(nontarget_df[\"k\"] == k) & (nontarget_df[\"p\"] == p_val)]\n\n            mean_tpr = t_sub[\"tpr\"].mean() if len(t_sub) > 0 else np.nan\n            mean_delta_tpr = t_sub[\"delta_tpr\"].mean() if len(t_sub) > 0 else np.nan\n            std_delta_tpr = t_sub.groupby(\"seed\")[\"delta_tpr\"].mean().std() if len(t_sub) > 0 else np.nan\n\n            mean_fpr_nt = nt_sub[\"fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            mean_delta_fpr_nt = nt_sub[\"delta_fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            std_delta_fpr_nt = nt_sub.groupby(\"seed\")[\"delta_fpr\"].mean().std() if len(nt_sub) > 0 else np.nan\n\n            summary_rows.append(dict(\n                k=k, p=p_val,\n                mean_tpr_target=round(mean_tpr, 4),\n                mean_delta_tpr=round(mean_delta_tpr, 4),\n                std_delta_tpr=round(std_delta_tpr, 4) if not np.isnan(std_delta_tpr) else np.nan,\n                mean_fpr_non_target=round(mean_fpr_nt, 4),\n                mean_delta_fpr_non_target=round(mean_delta_fpr_nt, 4),\n                std_delta_fpr_non_target=round(std_delta_fpr_nt, 4) if not np.isnan(std_delta_fpr_nt) else np.nan,\n            ))\n\n    summary_df = pd.DataFrame(summary_rows)\n    summary_df.to_csv(OUT / \"summary_by_k.csv\", index=False)\n\n    elapsed = time.time() - t0\n    print(f\"\\nDone in {elapsed:.0f}s. Saved to {OUT}\")\n    print(\"\\nSummary:\")\n    print(summary_df.to_string(index=False))\n\n    return target_df, nontarget_df, summary_df\n\n\ndef generate_report(target_df, nontarget_df, summary_df):\n    lines = [\n        \"# Plan 034: Multi-Subject Simultaneous Injection — Report\",\n        \"\",\n        \"## Method\",\n        \"\",\n        \"We test Proposition 1's robustness boundary by simultaneously injecting\",\n        \"differential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).\",\n        \"For each (k, p, seed) combination:\",\n        \"\",\n        \"1. Randomly select k target subjects from 57 MMLU subjects\",\n        \"2. For each item in the k target subjects, flip incorrect→correct responses\",\n        \"   in the focal group (2024 models within accuracy overlap) with probability p\",\n        \"3. Compute cross-subject MH-DIF for each target and non-target subject\",\n        \"   - Matching variable = total score on all subjects EXCEPT the tested one\",\n        \"   - For target subjects: matching includes injected scores from other targets\",\n        \"   - For non-target subjects: matching includes all injected target scores\",\n        \"4. Measure TPR on target subjects and FPR on non-target subjects\",\n        \"\",\n        f\"Grid: k ∈ {{{','.join(map(str, KS))}}}, p ∈ {{{','.join(map(str, PS))}}}, \"\n        f\"5 seeds per combination = {len(KS)*len(PS)*N_SEEDS} runs\",\n        \"\",\n        \"## Core Results: ΔFPR by k and p\",\n        \"\",\n    ]\n\n    # Summary table\n    lines.append(\"### Target Subjects (TPR)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean TPR | Mean ΔTPR | SD(ΔTPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_tpr_target']:.4f} | \"\n                      f\"{row['mean_delta_tpr']:.4f} | \"\n                      f\"{row['std_delta_tpr']:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Non-Target Subjects (FPR — key result)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean FPR | Mean ΔFPR | SD(ΔFPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_fpr_non_target']:.4f} | \"\n                      f\"{row['mean_delta_fpr_non_target']:.4f} | \"\n                      f\"{row['std_delta_fpr_non_target']:.4f} |\")\n    lines.append(\"\")\n\n    # Key findings\n    lines.append(\"## Key Findings\")\n    lines.append(\"\")\n\n    # Find threshold where ΔFPR becomes notable\n    for p_val in PS:\n        sub = summary_df[summary_df[\"p\"] == p_val]\n        significant_k = sub[sub[\"mean_delta_fpr_non_target\"].abs() > 0.01]\n        if len(significant_k) > 0:\n            first_k = int(significant_k.iloc[0][\"k\"])\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR exceeds 0.01 at k={first_k}\")\n        else:\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR stays below 0.01 for all k tested\")\n\n    lines.append(\"\")\n    lines.append(\"## Interpretation\")\n    lines.append(\"\")\n    lines.append(\"Proposition 1 guarantees ΔFPR=0 when the matching variable is uncontaminated.\")\n    lines.append(\"As k increases, more of the cross-subject total score is contaminated,\")\n    lines.append(\"violating the proposition's assumption. The k at which ΔFPR becomes\")\n    lines.append(\"practically significant marks the validity boundary of cross-subject DIF auditing.\")\n    lines.append(\"\")\n\n    report_path = OUT / \"plan_034_report.md\"\n    report_path.write_text(\"\\n\".join(lines))\n    print(f\"Report saved to {report_path}\")\n\n\nif __name__ == \"__main__\":\n    parser = argparse.ArgumentParser(description=\"Plan 034: Multi-Subject Injection\")\n    parser.add_argument(\"--quick\", action=\"store_true\",\n                        help=\"Quick validation: k∈{1,5,20}, p=0.3, seed=1\")\n    args = parser.parse_args()\n\n    if args.quick:\n        target_df, nontarget_df, summary_df = run_experiment(\n            ks=[1, 5, 20], ps=[0.3], n_seeds=1)\n    else:\n        target_df, nontarget_df, summary_df = run_experiment()\n\n    generate_report(target_df, nontarget_df, summary_df)\n",
    "structuredPatch": [
      {
        "oldStart": 288,
        "oldLines": 12,
        "newStart": 288,
        "newLines": 11,
        "lines": [
          "                 mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)",
          "                 n_flipped = 0",
          "                 if p > 0:",
          "-                    for local_j in range(len(target_cols_all)):",
          "-                        for model_row in foc_inject_rows:",
          "-                            if mat_dense_targets[model_row, local_j] == 0:",
          "-                                if rng.random() < p:",
          "-                                    mat_dense_targets[model_row, local_j] = 1",
          "-                                    n_flipped += 1",
          "+                    block = mat_dense_targets[foc_inject_rows]",
          "+                    zeros = (block == 0)",
          "+                    flip_mask = zeros & (rng.random(block.shape) < p)",
          "+                    n_flipped = int(flip_mask.sum())",
          "+                    mat_dense_targets[foc_inject_rows] = block + flip_mask.astype(np.int8)",
          " ",
          "                 # Cross-subject matching variable = total on uninjected subjects",
          "                 # (from original matrix — non-target subjects are never injected)"
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

### Assistant

_source line 52_

Now let me also optimize the non-target matching variable computation — currently recomputing sparse slices per non-target subject is expensive. I can precompute the full non-target total and subtract per-subject.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "5361ef26-44ba-4dcf-a20a-93636cb49351",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPaR32aB69UdFDnmbZDhbi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 46753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 555
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

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_01Jxy3WyAbanVzRNtqfmnVKc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
  "offset": 288,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "eacebf0d-5789-4fdd-b1c4-18d47063eef5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPaR32aB69UdFDnmbZDhbi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 46753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 555
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

_source line 54 · 2026-05-21T15:50:24.214Z_

<details><summary>↩ Tool result · `toolu_01Jxy3WyAbanVzRNtqfmnVKc`</summary>

```text
288	                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)
289	                n_flipped = 0
290	                if p > 0:
291	                    block = mat_dense_targets[foc_inject_rows]
292	                    zeros = (block == 0)
293	                    flip_mask = zeros & (rng.random(block.shape) < p)
294	                    n_flipped = int(flip_mask.sum())
295	                    mat_dense_targets[foc_inject_rows] = block + flip_mask.astype(np.int8)
296	
297	                # Cross-subject matching variable = total on uninjected subjects
298	                # (from original matrix — non-target subjects are never injected)
299	                cross_ref = np.asarray(mat[ref_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)
300	                cross_foc = np.asarray(mat[foc_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)
301	
302	                # But for target subjects, the matching variable includes OTHER
303	                # target subjects' injected scores too. We need per-subject matching.
304	                # For target subject s: matching = non_target_total + injected_other_targets
305	                # For non-target subject s: matching = non_target_total_minus_s + all_target_injected
306	
307	                # Precompute injected target total per model (from injected matrix)
308	                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)
309	
310	                # Build local col mapping: target_cols_all[local_idx] → local_idx
311	                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}
312	
313	                elapsed = time.time() - t0
314	                print(f"  [{run_i}/{total_runs}] k={k} p={p} seed={seed} "
315	                      f"flipped={n_flipped} ({elapsed:.0f}s)")
316	
317	                # ── DIF on each target subject ──
318	                for subj in target_subjects:
319	                    s_cols = subject_cols[subj]
320	                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])
321	                    X_subj_inj = mat_dense_targets[:, local_idxs]
322	
323	                    X_ref_s = X_subj_inj[ref_rows]
324	                    X_foc_s = X_subj_inj[foc_rows]
325	
326	                    # Matching variable for target subject: everything EXCEPT this subject
327	                    # = non_target_total + injected scores from OTHER target subjects
328	                    this_subj_injected = X_subj_inj.sum(axis=1).astype(np.float64)
329	                    other_target_injected = injected_target_total - this_subj_injected
330	
331	                    match_ref = cross_ref + other_target_injected[ref_rows]
332	                    match_foc = cross_foc + other_target_injected[foc_rows]
333	
334	                    n_strata = 3 if len(s_cols) < 100 else N_STRATA
335	                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,
336	                                          external_scores_ref=match_ref,
337	                                          external_scores_foc=match_foc,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "8b70de44-2f85-41c4-9e92-dc4a8133ffc1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
      "content": "                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    block = mat_dense_targets[foc_inject_rows]\n                    zeros = (block == 0)\n                    flip_mask = zeros & (rng.random(block.shape) < p)\n                    n_flipped = int(flip_mask.sum())\n                    mat_dense_targets[foc_inject_rows] = block + flip_mask.astype(np.int8)\n\n                # Cross-subject matching variable = total on uninjected subjects\n                # (from original matrix — non-target subjects are never injected)\n                cross_ref = np.asarray(mat[ref_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n                cross_foc = np.asarray(mat[foc_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                # But for target subjects, the matching variable includes OTHER\n                # target subjects' injected scores too. We need per-subject matching.\n                # For target subject s: matching = non_target_total + injected_other_targets\n                # For non-target subject s: matching = non_target_total_minus_s + all_target_injected\n\n                # Precompute injected target total per model (from injected matrix)\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                # Build local col mapping: target_cols_all[local_idx] → local_idx\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}\n\n                elapsed = time.time() - t0\n                print(f\"  [{run_i}/{total_runs}] k={k} p={p} seed={seed} \"\n                      f\"flipped={n_flipped} ({elapsed:.0f}s)\")\n\n                # ── DIF on each target subject ──\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    # Matching variable for target subject: everything EXCEPT this subject\n                    # = non_target_total + injected scores from OTHER target subjects\n                    this_subj_injected = X_subj_inj.sum(axis=1).astype(np.float64)\n                    other_target_injected = injected_target_total - this_subj_injected\n\n                    match_ref = cross_ref + other_target_injected[ref_rows]\n                    match_foc = cross_foc + other_target_injected[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,",
      "numLines": 50,
      "startLine": 288,
      "totalLines": 526
    }
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01Uxg1gxfcffZd38GBfZRd41`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
  "offset": 338,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "ec4a257e-f709-4ee2-a6da-053966533ec0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VDWn7Tr8NfhAAGxdv45bVt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1179,
      "cache_read_input_tokens": 47308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1179
      },
      "output_tokens": 37,
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

_source line 56 · 2026-05-21T15:50:29.538Z_

<details><summary>↩ Tool result · `toolu_01Uxg1gxfcffZd38GBfZRd41`</summary>

```text
338	                                          min_per_stratum=MIN_PER_STRATUM)
339	
340	                    n_c = int((dif["ets_class"] == "C").sum())
341	                    # All items in target subject are "contaminated" (injected)
342	                    tpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0
343	                    delta_tpr = tpr - baseline_fpr[subj]  # baseline is p=0 rate
344	
345	                    target_rows_list.append(dict(
346	                        k=k, p=p, seed=seed, target_subject=subj,
347	                        n_items=len(s_cols), tpr=tpr, fpr=np.nan,
348	                        delta_tpr=delta_tpr, delta_fpr=np.nan,
349	                        n_target_c=n_c, n_clean_c=np.nan
350	                    ))
351	
352	                # ── DIF on each non-target subject (FPR measurement) ──
353	                # Sample non-targets to keep runtime manageable for large k
354	                # For k≤5, test all; for k>5, test 20 random non-targets
355	                if len(non_target_subjects) <= 20:
356	                    test_nontargets = non_target_subjects
357	                else:
358	                    test_nontargets = sorted(rng.choice(non_target_subjects,
359	                                                        size=20, replace=False))
360	
361	                for subj in test_nontargets:
362	                    s_cols = subject_cols[subj]
363	                    s_cols_set = set(s_cols.tolist())
364	
365	                    X_ref_s = mat[ref_rows][:, s_cols].toarray().astype(np.int8)
366	                    X_foc_s = mat[foc_rows][:, s_cols].toarray().astype(np.int8)
367	
368	                    # Matching = everything except this subject
369	                    # = non_target_total (minus this subject) + all injected target scores
370	                    other_nontarget_cols = np.array([c for c in non_target_cols
371	                                                     if c not in s_cols_set])
372	                    other_nt_ref = np.asarray(mat[ref_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)
373	                    other_nt_foc = np.asarray(mat[foc_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)
374	
375	                    match_ref = other_nt_ref + injected_target_total[ref_rows]
376	                    match_foc = other_nt_foc + injected_target_total[foc_rows]
377	
378	                    n_strata = 3 if len(s_cols) < 100 else N_STRATA
379	                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,
380	                                          external_scores_ref=match_ref,
381	                                          external_scores_foc=match_foc,
382	                                          min_per_stratum=MIN_PER_STRATUM)
383	
384	                    n_c = int((dif["ets_class"] == "C").sum())
385	                    fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0
386	                    delta_fpr = fpr - baseline_fpr[subj]
387	
388	                    non_target_rows_list.append(dict(
389	                        k=k, p=p, seed=seed, non_target_subject=subj,
390	                        n_items=len(s_cols),
391	                        fpr=fpr, baseline_fpr=baseline_fpr[subj],
392	                        delta_fpr=delta_fpr
393	                    ))
394	
395	    # ── Save results ──
396	    target_df = pd.DataFrame(target_rows_list)
397	    target_df.to_csv(OUT / "multi_subject_injection_results.csv", index=False)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "d75d6f30-5c44-4516-92de-0ee431702247",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
      "content": "                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    # All items in target subject are \"contaminated\" (injected)\n                    tpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_tpr = tpr - baseline_fpr[subj]  # baseline is p=0 rate\n\n                    target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, target_subject=subj,\n                        n_items=len(s_cols), tpr=tpr, fpr=np.nan,\n                        delta_tpr=delta_tpr, delta_fpr=np.nan,\n                        n_target_c=n_c, n_clean_c=np.nan\n                    ))\n\n                # ── DIF on each non-target subject (FPR measurement) ──\n                # Sample non-targets to keep runtime manageable for large k\n                # For k≤5, test all; for k>5, test 20 random non-targets\n                if len(non_target_subjects) <= 20:\n                    test_nontargets = non_target_subjects\n                else:\n                    test_nontargets = sorted(rng.choice(non_target_subjects,\n                                                        size=20, replace=False))\n\n                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n                    s_cols_set = set(s_cols.tolist())\n\n                    X_ref_s = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n                    X_foc_s = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n                    # Matching = everything except this subject\n                    # = non_target_total (minus this subject) + all injected target scores\n                    other_nontarget_cols = np.array([c for c in non_target_cols\n                                                     if c not in s_cols_set])\n                    other_nt_ref = np.asarray(mat[ref_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n                    other_nt_foc = np.asarray(mat[foc_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                    match_ref = other_nt_ref + injected_target_total[ref_rows]\n                    match_foc = other_nt_foc + injected_target_total[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_fpr = fpr - baseline_fpr[subj]\n\n                    non_target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, non_target_subject=subj,\n                        n_items=len(s_cols),\n                        fpr=fpr, baseline_fpr=baseline_fpr[subj],\n                        delta_fpr=delta_fpr\n                    ))\n\n    # ── Save results ──\n    target_df = pd.DataFrame(target_rows_list)\n    target_df.to_csv(OUT / \"multi_subject_injection_results.csv\", index=False)",
      "numLines": 60,
      "startLine": 338,
      "totalLines": 526
    }
  }
}
```

</details>

---

### Assistant

_source line 57_

<details><summary>Logged reasoning block</summary>

```text
The non-target FPR computation is the bottleneck because for each non-target subject, it's recomputing `other_nontarget_cols` sparse slicing. I can optimize by precomputing per-subject total scores from the original matrix and then doing subtraction.

Let me optimize: precompute total score per model across all non-target subjects, then for each non-target subject s, the matching = (all_nontarget_total - s_total) + injected_target_total.

This avoids the expensive sparse matrix column selection per non-target subject.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "e7e45faa-da98-49ea-8514-18a32d1a9822",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SwS8oGqbFQo2oC83tWUqhm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 48487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1312
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

_source line 58_

Let me optimize the non-target loop by precomputing totals and using subtraction instead of re-slicing sparse matrix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "f2a7fb96-eaf1-41b0-868a-bca37590c84b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SwS8oGqbFQo2oC83tWUqhm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 48487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1312
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

_source line 59_

<details open><summary>🔧 Tool call — Edit · `toolu_013ztKE9tfLx8mwEtW15QTbF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
  "old_string": "    all_cols = np.concatenate([subject_cols[s] for s in subjects])\n    all_cols_set = set(all_cols.tolist())\n\n    # ── Phase 1: baseline (p=0) per-subject FPR with cross-subject matching ──\n    # Baseline uses full uninjected cross-subject scores\n    print(\"Computing baseline FPR (p=0) for all subjects...\")\n    baseline_fpr = {}\n    baseline_n_c = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        other_cols = np.array([c for c in all_cols if c not in set(s_cols.tolist())])\n\n        cross_ref = np.asarray(mat[ref_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)\n        cross_foc = np.asarray(mat[foc_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)\n\n        X_ref = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n        X_foc = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n        n_strata = 3 if len(s_cols) < 100 else N_STRATA\n        dif = purified_mh_dif(X_ref, X_foc, n_strata=n_strata,\n                              external_scores_ref=cross_ref,\n                              external_scores_foc=cross_foc,\n                              min_per_stratum=MIN_PER_STRATUM)\n        n_c = int((dif[\"ets_class\"] == \"C\").sum())\n        fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n        baseline_fpr[subj] = fpr\n        baseline_n_c[subj] = n_c\n\n    print(f\"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}\")",
  "new_string": "    all_cols = np.concatenate([subject_cols[s] for s in subjects])\n\n    # Precompute per-subject total scores (original matrix) for ref/foc\n    # Enables O(1) matching variable via subtraction instead of re-slicing\n    subj_totals_ref = {}\n    subj_totals_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_totals_ref[subj] = np.asarray(mat[ref_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n        subj_totals_foc[subj] = np.asarray(mat[foc_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n\n    # Full total across all subjects\n    full_total_ref = sum(subj_totals_ref.values())\n    full_total_foc = sum(subj_totals_foc.values())\n\n    # Precompute dense submatrices per subject for ref/foc (avoids repeated sparse→dense)\n    subj_X_ref = {}\n    subj_X_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_X_ref[subj] = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n        subj_X_foc[subj] = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n    # ── Phase 1: baseline (p=0) per-subject FPR with cross-subject matching ──\n    print(\"Computing baseline FPR (p=0) for all subjects...\")\n    baseline_fpr = {}\n    baseline_n_c = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        cross_ref = full_total_ref - subj_totals_ref[subj]\n        cross_foc = full_total_foc - subj_totals_foc[subj]\n\n        n_strata = 3 if len(s_cols) < 100 else N_STRATA\n        dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,\n                              external_scores_ref=cross_ref,\n                              external_scores_foc=cross_foc,\n                              min_per_stratum=MIN_PER_STRATUM)\n        n_c = int((dif[\"ets_class\"] == \"C\").sum())\n        fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n        baseline_fpr[subj] = fpr\n        baseline_n_c[subj] = n_c\n\n    print(f\"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "bd665d98-6d91-4597-87f3-1297bbe5e5c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SwS8oGqbFQo2oC83tWUqhm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1312,
      "cache_read_input_tokens": 48487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1312
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

_source line 60 · 2026-05-21T15:50:52.179Z_

<details><summary>↩ Tool result · `toolu_013ztKE9tfLx8mwEtW15QTbF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "deb7780d-834d-40eb-9601-5f7527c02920",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
    "oldString": "    all_cols = np.concatenate([subject_cols[s] for s in subjects])\n    all_cols_set = set(all_cols.tolist())\n\n    # ── Phase 1: baseline (p=0) per-subject FPR with cross-subject matching ──\n    # Baseline uses full uninjected cross-subject scores\n    print(\"Computing baseline FPR (p=0) for all subjects...\")\n    baseline_fpr = {}\n    baseline_n_c = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        other_cols = np.array([c for c in all_cols if c not in set(s_cols.tolist())])\n\n        cross_ref = np.asarray(mat[ref_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)\n        cross_foc = np.asarray(mat[foc_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)\n\n        X_ref = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n        X_foc = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n        n_strata = 3 if len(s_cols) < 100 else N_STRATA\n        dif = purified_mh_dif(X_ref, X_foc, n_strata=n_strata,\n                              external_scores_ref=cross_ref,\n                              external_scores_foc=cross_foc,\n                              min_per_stratum=MIN_PER_STRATUM)\n        n_c = int((dif[\"ets_class\"] == \"C\").sum())\n        fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n        baseline_fpr[subj] = fpr\n        baseline_n_c[subj] = n_c\n\n    print(f\"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}\")",
    "newString": "    all_cols = np.concatenate([subject_cols[s] for s in subjects])\n\n    # Precompute per-subject total scores (original matrix) for ref/foc\n    # Enables O(1) matching variable via subtraction instead of re-slicing\n    subj_totals_ref = {}\n    subj_totals_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_totals_ref[subj] = np.asarray(mat[ref_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n        subj_totals_foc[subj] = np.asarray(mat[foc_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n\n    # Full total across all subjects\n    full_total_ref = sum(subj_totals_ref.values())\n    full_total_foc = sum(subj_totals_foc.values())\n\n    # Precompute dense submatrices per subject for ref/foc (avoids repeated sparse→dense)\n    subj_X_ref = {}\n    subj_X_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_X_ref[subj] = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n        subj_X_foc[subj] = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n    # ── Phase 1: baseline (p=0) per-subject FPR with cross-subject matching ──\n    print(\"Computing baseline FPR (p=0) for all subjects...\")\n    baseline_fpr = {}\n    baseline_n_c = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        cross_ref = full_total_ref - subj_totals_ref[subj]\n        cross_foc = full_total_foc - subj_totals_foc[subj]\n\n        n_strata = 3 if len(s_cols) < 100 else N_STRATA\n        dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,\n                              external_scores_ref=cross_ref,\n                              external_scores_foc=cross_foc,\n                              min_per_stratum=MIN_PER_STRATUM)\n        n_c = int((dif[\"ets_class\"] == \"C\").sum())\n        fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n        baseline_fpr[subj] = fpr\n        baseline_n_c[subj] = n_c\n\n    print(f\"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}\")",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nplan_034: Multi-Subject Simultaneous Injection Experiment\n\nTests Proposition 1 (ΔFPR=0) robustness under multi-subject contamination.\nWhen k subjects are simultaneously injected, the cross-subject matching variable\n(total score on remaining 57-k uninjected subjects) degrades. ΔFPR(k) on\nnon-target subjects should increase with k, revealing the validity boundary.\n\nInputs:\n  - artifacts/response_matrix.npz         (5227 × 12508 sparse binary)\n  - artifacts/response_matrix_index.npz   (model_names, item_ids)\n  - artifacts/model_metadata.csv          (cohort_temporal, accuracy, ...)\n  - artifacts/item_metadata.csv           (item_id, subject, ...)\n\nOutputs:\n  - multi_subject_injection_results.csv   (per-target-subject DIF results)\n  - non_target_fpr_results.csv            (FPR on uninjected subjects)\n  - summary_by_k.csv                      (aggregated ΔFPR/ΔTPR by k,p)\n  - plan_034_report.md\n\nDependencies: numpy, pandas, scipy\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\nimport warnings\nimport argparse\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_034_multi_subject_injection\"\nOUT.mkdir(exist_ok=True)\n\nKS = [1, 2, 3, 5, 10, 20]\nPS = [0.1, 0.3, 0.5]\nN_SEEDS = 5\nN_STRATA = 5\nMIN_PER_STRATUM = 5\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE (from plan_016 with strata merging + external score support)\n# ════════════════════════════════════════════════════════════════════════════\ndef purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,\n                    external_scores_foc=None, min_per_stratum=5):\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])\n\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n\n        n_bins = len(edges) - 1\n        k_all = np.digitize(s_all, edges[1:-1])\n        strata_labels = _merge_small_strata(k_all, groups_all, n_bins, min_per_stratum)\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        x_all = np.concatenate([X_ref[:, j], X_foc[:, j]])\n\n        for k in np.unique(strata_labels):\n            mask_k = (strata_labels == k)\n            mask_ref = mask_k & (groups_all == 0)\n            mask_foc = mask_k & (groups_all == 1)\n\n            n1 = int(mask_ref.sum())\n            n0 = int(mask_foc.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(x_all[mask_ref].sum())\n            B = float(n1 - A)\n            C = float(x_all[mask_foc].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else np.inf\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets,\n                         n_strata_used=n_ok))\n\n    return pd.DataFrame(rows)\n\n\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\",\n                n_strata_used=0)\n\n\ndef _merge_small_strata(k_all, groups_all, n_bins, min_n):\n    labels = k_all.copy()\n    merged = True\n    while merged:\n        merged = False\n        unique_strata = sorted(np.unique(labels))\n        for i, k in enumerate(unique_strata):\n            mask_k = (labels == k)\n            n_ref = int((mask_k & (groups_all == 0)).sum())\n            n_foc = int((mask_k & (groups_all == 1)).sum())\n            if n_ref < min_n or n_foc < min_n:\n                if i + 1 < len(unique_strata):\n                    next_k = unique_strata[i + 1]\n                    labels[labels == next_k] = k\n                elif i > 0:\n                    prev_k = unique_strata[i - 1]\n                    labels[labels == k] = prev_k\n                merged = True\n                break\n    return labels\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\ndef load_data():\n    mat = load_npz(BASE / \"response_matrix.npz\")\n    idx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n    item2col = {iid: i for i, iid in enumerate(item_ids)}\n\n    model_meta = pd.read_csv(BASE / \"model_metadata.csv\")\n    item_meta = pd.read_csv(BASE / \"item_metadata.csv\")\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    # Temporal cohorts\n    ref_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"model_name\"]\n    foc_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"model_name\"]\n    ref_rows = np.array([name2row[n] for n in ref_names if n in name2row])\n    foc_rows = np.array([name2row[n] for n in foc_names if n in name2row])\n\n    # Focal inject subset: 2024 models in accuracy overlap with 2023\n    ref_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\n    foc_df = model_meta[model_meta[\"cohort_temporal\"] == \"2024\"]\n    t_min = max(ref_acc.min(), foc_df[\"accuracy\"].min())\n    t_max = min(ref_acc.max(), foc_df[\"accuracy\"].max())\n    foc_inject_mask = (foc_df[\"accuracy\"] >= t_min) & (foc_df[\"accuracy\"] <= t_max)\n    foc_inject_rows = np.array([name2row[n] for n in foc_df.loc[foc_inject_mask, \"model_name\"]\n                                if n in name2row])\n\n    # Build subject → column indices mapping\n    subject_cols = {}\n    subjects = sorted(item_meta[\"subject\"].unique())\n    for subj in subjects:\n        ids = item_meta.loc[item_meta[\"subject\"] == subj, \"item_id\"].values\n        cols = np.array([item2col[iid] for iid in ids if iid in item2col])\n        subject_cols[subj] = cols\n\n    return mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MAIN EXPERIMENT\n# ════════════════════════════════════════════════════════════════════════════\ndef run_experiment(ks=KS, ps=PS, n_seeds=N_SEEDS):\n    t0 = time.time()\n    mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols = load_data()\n    print(f\"Data loaded: {len(ref_rows)} ref, {len(foc_rows)} foc, \"\n          f\"{len(foc_inject_rows)} foc_inject, {len(subjects)} subjects\")\n\n    all_cols = np.concatenate([subject_cols[s] for s in subjects])\n    all_cols_set = set(all_cols.tolist())\n\n    # ── Phase 1: baseline (p=0) per-subject FPR with cross-subject matching ──\n    # Baseline uses full uninjected cross-subject scores\n    print(\"Computing baseline FPR (p=0) for all subjects...\")\n    baseline_fpr = {}\n    baseline_n_c = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        other_cols = np.array([c for c in all_cols if c not in set(s_cols.tolist())])\n\n        cross_ref = np.asarray(mat[ref_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)\n        cross_foc = np.asarray(mat[foc_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)\n\n        X_ref = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n        X_foc = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n        n_strata = 3 if len(s_cols) < 100 else N_STRATA\n        dif = purified_mh_dif(X_ref, X_foc, n_strata=n_strata,\n                              external_scores_ref=cross_ref,\n                              external_scores_foc=cross_foc,\n                              min_per_stratum=MIN_PER_STRATUM)\n        n_c = int((dif[\"ets_class\"] == \"C\").sum())\n        fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n        baseline_fpr[subj] = fpr\n        baseline_n_c[subj] = n_c\n\n    print(f\"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}\")\n\n    # ── Phase 2: injection runs ──\n    target_rows_list = []\n    non_target_rows_list = []\n    total_runs = len(ks) * len(ps) * n_seeds\n    run_i = 0\n\n    for k in ks:\n        for p in ps:\n            for seed in range(1, n_seeds + 1):\n                run_i += 1\n                rng = np.random.RandomState(seed)\n                target_subjects = sorted(rng.choice(subjects, size=k, replace=False))\n                non_target_subjects = [s for s in subjects if s not in target_subjects]\n\n                # Build injected matrix columns for target subjects\n                # Collect all target columns for injection\n                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])\n                target_cols_set = set(target_cols_all.tolist())\n                non_target_cols = np.array([c for c in all_cols if c not in target_cols_set])\n\n                # Inject: flip incorrect→correct for focal inject models on target items\n                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    block = mat_dense_targets[foc_inject_rows]\n                    zeros = (block == 0)\n                    flip_mask = zeros & (rng.random(block.shape) < p)\n                    n_flipped = int(flip_mask.sum())\n                    mat_dense_targets[foc_inject_rows] = block + flip_mask.astype(np.int8)\n\n                # Cross-subject matching variable = total on uninjected subjects\n                # (from original matrix — non-target subjects are never injected)\n                cross_ref = np.asarray(mat[ref_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n                cross_foc = np.asarray(mat[foc_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                # But for target subjects, the matching variable includes OTHER\n                # target subjects' injected scores too. We need per-subject matching.\n                # For target subject s: matching = non_target_total + injected_other_targets\n                # For non-target subject s: matching = non_target_total_minus_s + all_target_injected\n\n                # Precompute injected target total per model (from injected matrix)\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                # Build local col mapping: target_cols_all[local_idx] → local_idx\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}\n\n                elapsed = time.time() - t0\n                print(f\"  [{run_i}/{total_runs}] k={k} p={p} seed={seed} \"\n                      f\"flipped={n_flipped} ({elapsed:.0f}s)\")\n\n                # ── DIF on each target subject ──\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    # Matching variable for target subject: everything EXCEPT this subject\n                    # = non_target_total + injected scores from OTHER target subjects\n                    this_subj_injected = X_subj_inj.sum(axis=1).astype(np.float64)\n                    other_target_injected = injected_target_total - this_subj_injected\n\n                    match_ref = cross_ref + other_target_injected[ref_rows]\n                    match_foc = cross_foc + other_target_injected[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    # All items in target subject are \"contaminated\" (injected)\n                    tpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_tpr = tpr - baseline_fpr[subj]  # baseline is p=0 rate\n\n                    target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, target_subject=subj,\n                        n_items=len(s_cols), tpr=tpr, fpr=np.nan,\n                        delta_tpr=delta_tpr, delta_fpr=np.nan,\n                        n_target_c=n_c, n_clean_c=np.nan\n                    ))\n\n                # ── DIF on each non-target subject (FPR measurement) ──\n                # Sample non-targets to keep runtime manageable for large k\n                # For k≤5, test all; for k>5, test 20 random non-targets\n                if len(non_target_subjects) <= 20:\n                    test_nontargets = non_target_subjects\n                else:\n                    test_nontargets = sorted(rng.choice(non_target_subjects,\n                                                        size=20, replace=False))\n\n                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n                    s_cols_set = set(s_cols.tolist())\n\n                    X_ref_s = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n                    X_foc_s = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n                    # Matching = everything except this subject\n                    # = non_target_total (minus this subject) + all injected target scores\n                    other_nontarget_cols = np.array([c for c in non_target_cols\n                                                     if c not in s_cols_set])\n                    other_nt_ref = np.asarray(mat[ref_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n                    other_nt_foc = np.asarray(mat[foc_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                    match_ref = other_nt_ref + injected_target_total[ref_rows]\n                    match_foc = other_nt_foc + injected_target_total[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_fpr = fpr - baseline_fpr[subj]\n\n                    non_target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, non_target_subject=subj,\n                        n_items=len(s_cols),\n                        fpr=fpr, baseline_fpr=baseline_fpr[subj],\n                        delta_fpr=delta_fpr\n                    ))\n\n    # ── Save results ──\n    target_df = pd.DataFrame(target_rows_list)\n    target_df.to_csv(OUT / \"multi_subject_injection_results.csv\", index=False)\n\n    nontarget_df = pd.DataFrame(non_target_rows_list)\n    nontarget_df.to_csv(OUT / \"non_target_fpr_results.csv\", index=False)\n\n    # ── Summary by k,p ──\n    summary_rows = []\n    for k in ks:\n        for p_val in ps:\n            t_sub = target_df[(target_df[\"k\"] == k) & (target_df[\"p\"] == p_val)]\n            nt_sub = nontarget_df[(nontarget_df[\"k\"] == k) & (nontarget_df[\"p\"] == p_val)]\n\n            mean_tpr = t_sub[\"tpr\"].mean() if len(t_sub) > 0 else np.nan\n            mean_delta_tpr = t_sub[\"delta_tpr\"].mean() if len(t_sub) > 0 else np.nan\n            std_delta_tpr = t_sub.groupby(\"seed\")[\"delta_tpr\"].mean().std() if len(t_sub) > 0 else np.nan\n\n            mean_fpr_nt = nt_sub[\"fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            mean_delta_fpr_nt = nt_sub[\"delta_fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            std_delta_fpr_nt = nt_sub.groupby(\"seed\")[\"delta_fpr\"].mean().std() if len(nt_sub) > 0 else np.nan\n\n            summary_rows.append(dict(\n                k=k, p=p_val,\n                mean_tpr_target=round(mean_tpr, 4),\n                mean_delta_tpr=round(mean_delta_tpr, 4),\n                std_delta_tpr=round(std_delta_tpr, 4) if not np.isnan(std_delta_tpr) else np.nan,\n                mean_fpr_non_target=round(mean_fpr_nt, 4),\n                mean_delta_fpr_non_target=round(mean_delta_fpr_nt, 4),\n                std_delta_fpr_non_target=round(std_delta_fpr_nt, 4) if not np.isnan(std_delta_fpr_nt) else np.nan,\n            ))\n\n    summary_df = pd.DataFrame(summary_rows)\n    summary_df.to_csv(OUT / \"summary_by_k.csv\", index=False)\n\n    elapsed = time.time() - t0\n    print(f\"\\nDone in {elapsed:.0f}s. Saved to {OUT}\")\n    print(\"\\nSummary:\")\n    print(summary_df.to_string(index=False))\n\n    return target_df, nontarget_df, summary_df\n\n\ndef generate_report(target_df, nontarget_df, summary_df):\n    lines = [\n        \"# Plan 034: Multi-Subject Simultaneous Injection — Report\",\n        \"\",\n        \"## Method\",\n        \"\",\n        \"We test Proposition 1's robustness boundary by simultaneously injecting\",\n        \"differential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).\",\n        \"For each (k, p, seed) combination:\",\n        \"\",\n        \"1. Randomly select k target subjects from 57 MMLU subjects\",\n        \"2. For each item in the k target subjects, flip incorrect→correct responses\",\n        \"   in the focal group (2024 models within accuracy overlap) with probability p\",\n        \"3. Compute cross-subject MH-DIF for each target and non-target subject\",\n        \"   - Matching variable = total score on all subjects EXCEPT the tested one\",\n        \"   - For target subjects: matching includes injected scores from other targets\",\n        \"   - For non-target subjects: matching includes all injected target scores\",\n        \"4. Measure TPR on target subjects and FPR on non-target subjects\",\n        \"\",\n        f\"Grid: k ∈ {{{','.join(map(str, KS))}}}, p ∈ {{{','.join(map(str, PS))}}}, \"\n        f\"5 seeds per combination = {len(KS)*len(PS)*N_SEEDS} runs\",\n        \"\",\n        \"## Core Results: ΔFPR by k and p\",\n        \"\",\n    ]\n\n    # Summary table\n    lines.append(\"### Target Subjects (TPR)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean TPR | Mean ΔTPR | SD(ΔTPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_tpr_target']:.4f} | \"\n                      f\"{row['mean_delta_tpr']:.4f} | \"\n                      f\"{row['std_delta_tpr']:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Non-Target Subjects (FPR — key result)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean FPR | Mean ΔFPR | SD(ΔFPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_fpr_non_target']:.4f} | \"\n                      f\"{row['mean_delta_fpr_non_target']:.4f} | \"\n                      f\"{row['std_delta_fpr_non_target']:.4f} |\")\n    lines.append(\"\")\n\n    # Key findings\n    lines.append(\"## Key Findings\")\n    lines.append(\"\")\n\n    # Find threshold where ΔFPR becomes notable\n    for p_val in PS:\n        sub = summary_df[summary_df[\"p\"] == p_val]\n        significant_k = sub[sub[\"mean_delta_fpr_non_target\"].abs() > 0.01]\n        if len(significant_k) > 0:\n            first_k = int(significant_k.iloc[0][\"k\"])\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR exceeds 0.01 at k={first_k}\")\n        else:\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR stays below 0.01 for all k tested\")\n\n    lines.append(\"\")\n    lines.append(\"## Interpretation\")\n    lines.append(\"\")\n    lines.append(\"Proposition 1 guarantees ΔFPR=0 when the matching variable is uncontaminated.\")\n    lines.append(\"As k increases, more of the cross-subject total score is contaminated,\")\n    lines.append(\"violating the proposition's assumption. The k at which ΔFPR becomes\")\n    lines.append(\"practically significant marks the validity boundary of cross-subject DIF auditing.\")\n    lines.append(\"\")\n\n    report_path = OUT / \"plan_034_report.md\"\n    report_path.write_text(\"\\n\".join(lines))\n    print(f\"Report saved to {report_path}\")\n\n\nif __name__ == \"__main__\":\n    parser = argparse.ArgumentParser(description=\"Plan 034: Multi-Subject Injection\")\n    parser.add_argument(\"--quick\", action=\"store_true\",\n                        help=\"Quick validation: k∈{1,5,20}, p=0.3, seed=1\")\n    args = parser.parse_args()\n\n    if args.quick:\n        target_df, nontarget_df, summary_df = run_experiment(\n            ks=[1, 5, 20], ps=[0.3], n_seeds=1)\n    else:\n        target_df, nontarget_df, summary_df = run_experiment()\n\n    generate_report(target_df, nontarget_df, summary_df)\n",
    "structuredPatch": [
      {
        "oldStart": 235,
        "oldLines": 25,
        "newStart": 235,
        "newLines": 39,
        "lines": [
          "           f\"{len(foc_inject_rows)} foc_inject, {len(subjects)} subjects\")",
          " ",
          "     all_cols = np.concatenate([subject_cols[s] for s in subjects])",
          "-    all_cols_set = set(all_cols.tolist())",
          " ",
          "+    # Precompute per-subject total scores (original matrix) for ref/foc",
          "+    # Enables O(1) matching variable via subtraction instead of re-slicing",
          "+    subj_totals_ref = {}",
          "+    subj_totals_foc = {}",
          "+    for subj in subjects:",
          "+        s_cols = subject_cols[subj]",
          "+        subj_totals_ref[subj] = np.asarray(mat[ref_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)",
          "+        subj_totals_foc[subj] = np.asarray(mat[foc_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)",
          "+",
          "+    # Full total across all subjects",
          "+    full_total_ref = sum(subj_totals_ref.values())",
          "+    full_total_foc = sum(subj_totals_foc.values())",
          "+",
          "+    # Precompute dense submatrices per subject for ref/foc (avoids repeated sparse→dense)",
          "+    subj_X_ref = {}",
          "+    subj_X_foc = {}",
          "+    for subj in subjects:",
          "+        s_cols = subject_cols[subj]",
          "+        subj_X_ref[subj] = mat[ref_rows][:, s_cols].toarray().astype(np.int8)",
          "+        subj_X_foc[subj] = mat[foc_rows][:, s_cols].toarray().astype(np.int8)",
          "+",
          "     # ── Phase 1: baseline (p=0) per-subject FPR with cross-subject matching ──",
          "-    # Baseline uses full uninjected cross-subject scores",
          "     print(\"Computing baseline FPR (p=0) for all subjects...\")",
          "     baseline_fpr = {}",
          "     baseline_n_c = {}",
          "     for subj in subjects:",
          "         s_cols = subject_cols[subj]",
          "-        other_cols = np.array([c for c in all_cols if c not in set(s_cols.tolist())])",
          "+        cross_ref = full_total_ref - subj_totals_ref[subj]",
          "+        cross_foc = full_total_foc - subj_totals_foc[subj]",
          " ",
          "-        cross_ref = np.asarray(mat[ref_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)",
          "-        cross_foc = np.asarray(mat[foc_rows][:, other_cols].sum(axis=1)).ravel().astype(np.float64)",
          "-",
          "-        X_ref = mat[ref_rows][:, s_cols].toarray().astype(np.int8)",
          "-        X_foc = mat[foc_rows][:, s_cols].toarray().astype(np.int8)",
          "-",
          "         n_strata = 3 if len(s_cols) < 100 else N_STRATA",
          "-        dif = purified_mh_dif(X_ref, X_foc, n_strata=n_strata,",
          "+        dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,",
          "                               external_scores_ref=cross_ref,",
          "                               external_scores_foc=cross_foc,",
          "                               min_per_stratum=MIN_PER_STRATUM)"
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

### Assistant

_source line 61_

Now optimize the injection loop's non-target computation to use the precomputed totals.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "e79ee6df-8e54-4619-87df-b905aaa0d127",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0134KNjZeGT5dzPCB1ELa8B7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1704,
      "cache_read_input_tokens": 49799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1704
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

_source line 62_

<details open><summary>🔧 Tool call — Edit · `toolu_01LpRkYokCvUSGaSW4C2FCtS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
  "old_string": "                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])\n                target_cols_set = set(target_cols_all.tolist())\n                non_target_cols = np.array([c for c in all_cols if c not in target_cols_set])",
  "new_string": "                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "669e15ea-1deb-4c20-972c-b23b6655cf65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0134KNjZeGT5dzPCB1ELa8B7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1704,
      "cache_read_input_tokens": 49799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1704
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

_source line 63 · 2026-05-21T15:51:01.513Z_

<details><summary>↩ Tool result · `toolu_01LpRkYokCvUSGaSW4C2FCtS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "80374436-568d-4f28-921d-f7ef0bf3d663",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
    "oldString": "                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])\n                target_cols_set = set(target_cols_all.tolist())\n                non_target_cols = np.array([c for c in all_cols if c not in target_cols_set])",
    "newString": "                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nplan_034: Multi-Subject Simultaneous Injection Experiment\n\nTests Proposition 1 (ΔFPR=0) robustness under multi-subject contamination.\nWhen k subjects are simultaneously injected, the cross-subject matching variable\n(total score on remaining 57-k uninjected subjects) degrades. ΔFPR(k) on\nnon-target subjects should increase with k, revealing the validity boundary.\n\nInputs:\n  - artifacts/response_matrix.npz         (5227 × 12508 sparse binary)\n  - artifacts/response_matrix_index.npz   (model_names, item_ids)\n  - artifacts/model_metadata.csv          (cohort_temporal, accuracy, ...)\n  - artifacts/item_metadata.csv           (item_id, subject, ...)\n\nOutputs:\n  - multi_subject_injection_results.csv   (per-target-subject DIF results)\n  - non_target_fpr_results.csv            (FPR on uninjected subjects)\n  - summary_by_k.csv                      (aggregated ΔFPR/ΔTPR by k,p)\n  - plan_034_report.md\n\nDependencies: numpy, pandas, scipy\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\nimport warnings\nimport argparse\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_034_multi_subject_injection\"\nOUT.mkdir(exist_ok=True)\n\nKS = [1, 2, 3, 5, 10, 20]\nPS = [0.1, 0.3, 0.5]\nN_SEEDS = 5\nN_STRATA = 5\nMIN_PER_STRATUM = 5\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE (from plan_016 with strata merging + external score support)\n# ════════════════════════════════════════════════════════════════════════════\ndef purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,\n                    external_scores_foc=None, min_per_stratum=5):\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])\n\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n\n        n_bins = len(edges) - 1\n        k_all = np.digitize(s_all, edges[1:-1])\n        strata_labels = _merge_small_strata(k_all, groups_all, n_bins, min_per_stratum)\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        x_all = np.concatenate([X_ref[:, j], X_foc[:, j]])\n\n        for k in np.unique(strata_labels):\n            mask_k = (strata_labels == k)\n            mask_ref = mask_k & (groups_all == 0)\n            mask_foc = mask_k & (groups_all == 1)\n\n            n1 = int(mask_ref.sum())\n            n0 = int(mask_foc.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(x_all[mask_ref].sum())\n            B = float(n1 - A)\n            C = float(x_all[mask_foc].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else np.inf\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets,\n                         n_strata_used=n_ok))\n\n    return pd.DataFrame(rows)\n\n\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\",\n                n_strata_used=0)\n\n\ndef _merge_small_strata(k_all, groups_all, n_bins, min_n):\n    labels = k_all.copy()\n    merged = True\n    while merged:\n        merged = False\n        unique_strata = sorted(np.unique(labels))\n        for i, k in enumerate(unique_strata):\n            mask_k = (labels == k)\n            n_ref = int((mask_k & (groups_all == 0)).sum())\n            n_foc = int((mask_k & (groups_all == 1)).sum())\n            if n_ref < min_n or n_foc < min_n:\n                if i + 1 < len(unique_strata):\n                    next_k = unique_strata[i + 1]\n                    labels[labels == next_k] = k\n                elif i > 0:\n                    prev_k = unique_strata[i - 1]\n                    labels[labels == k] = prev_k\n                merged = True\n                break\n    return labels\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\ndef load_data():\n    mat = load_npz(BASE / \"response_matrix.npz\")\n    idx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n    item2col = {iid: i for i, iid in enumerate(item_ids)}\n\n    model_meta = pd.read_csv(BASE / \"model_metadata.csv\")\n    item_meta = pd.read_csv(BASE / \"item_metadata.csv\")\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    # Temporal cohorts\n    ref_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"model_name\"]\n    foc_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"model_name\"]\n    ref_rows = np.array([name2row[n] for n in ref_names if n in name2row])\n    foc_rows = np.array([name2row[n] for n in foc_names if n in name2row])\n\n    # Focal inject subset: 2024 models in accuracy overlap with 2023\n    ref_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\n    foc_df = model_meta[model_meta[\"cohort_temporal\"] == \"2024\"]\n    t_min = max(ref_acc.min(), foc_df[\"accuracy\"].min())\n    t_max = min(ref_acc.max(), foc_df[\"accuracy\"].max())\n    foc_inject_mask = (foc_df[\"accuracy\"] >= t_min) & (foc_df[\"accuracy\"] <= t_max)\n    foc_inject_rows = np.array([name2row[n] for n in foc_df.loc[foc_inject_mask, \"model_name\"]\n                                if n in name2row])\n\n    # Build subject → column indices mapping\n    subject_cols = {}\n    subjects = sorted(item_meta[\"subject\"].unique())\n    for subj in subjects:\n        ids = item_meta.loc[item_meta[\"subject\"] == subj, \"item_id\"].values\n        cols = np.array([item2col[iid] for iid in ids if iid in item2col])\n        subject_cols[subj] = cols\n\n    return mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MAIN EXPERIMENT\n# ════════════════════════════════════════════════════════════════════════════\ndef run_experiment(ks=KS, ps=PS, n_seeds=N_SEEDS):\n    t0 = time.time()\n    mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols = load_data()\n    print(f\"Data loaded: {len(ref_rows)} ref, {len(foc_rows)} foc, \"\n          f\"{len(foc_inject_rows)} foc_inject, {len(subjects)} subjects\")\n\n    all_cols = np.concatenate([subject_cols[s] for s in subjects])\n\n    # Precompute per-subject total scores (original matrix) for ref/foc\n    # Enables O(1) matching variable via subtraction instead of re-slicing\n    subj_totals_ref = {}\n    subj_totals_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_totals_ref[subj] = np.asarray(mat[ref_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n        subj_totals_foc[subj] = np.asarray(mat[foc_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n\n    # Full total across all subjects\n    full_total_ref = sum(subj_totals_ref.values())\n    full_total_foc = sum(subj_totals_foc.values())\n\n    # Precompute dense submatrices per subject for ref/foc (avoids repeated sparse→dense)\n    subj_X_ref = {}\n    subj_X_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_X_ref[subj] = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n        subj_X_foc[subj] = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n    # ── Phase 1: baseline (p=0) per-subject FPR with cross-subject matching ──\n    print(\"Computing baseline FPR (p=0) for all subjects...\")\n    baseline_fpr = {}\n    baseline_n_c = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        cross_ref = full_total_ref - subj_totals_ref[subj]\n        cross_foc = full_total_foc - subj_totals_foc[subj]\n\n        n_strata = 3 if len(s_cols) < 100 else N_STRATA\n        dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,\n                              external_scores_ref=cross_ref,\n                              external_scores_foc=cross_foc,\n                              min_per_stratum=MIN_PER_STRATUM)\n        n_c = int((dif[\"ets_class\"] == \"C\").sum())\n        fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n        baseline_fpr[subj] = fpr\n        baseline_n_c[subj] = n_c\n\n    print(f\"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}\")\n\n    # ── Phase 2: injection runs ──\n    target_rows_list = []\n    non_target_rows_list = []\n    total_runs = len(ks) * len(ps) * n_seeds\n    run_i = 0\n\n    for k in ks:\n        for p in ps:\n            for seed in range(1, n_seeds + 1):\n                run_i += 1\n                rng = np.random.RandomState(seed)\n                target_subjects = sorted(rng.choice(subjects, size=k, replace=False))\n                non_target_subjects = [s for s in subjects if s not in target_subjects]\n\n                # Build injected matrix columns for target subjects\n                # Collect all target columns for injection\n                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])\n                target_cols_set = set(target_cols_all.tolist())\n                non_target_cols = np.array([c for c in all_cols if c not in target_cols_set])\n\n                # Inject: flip incorrect→correct for focal inject models on target items\n                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    block = mat_dense_targets[foc_inject_rows]\n                    zeros = (block == 0)\n                    flip_mask = zeros & (rng.random(block.shape) < p)\n                    n_flipped = int(flip_mask.sum())\n                    mat_dense_targets[foc_inject_rows] = block + flip_mask.astype(np.int8)\n\n                # Cross-subject matching variable = total on uninjected subjects\n                # (from original matrix — non-target subjects are never injected)\n                cross_ref = np.asarray(mat[ref_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n                cross_foc = np.asarray(mat[foc_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                # But for target subjects, the matching variable includes OTHER\n                # target subjects' injected scores too. We need per-subject matching.\n                # For target subject s: matching = non_target_total + injected_other_targets\n                # For non-target subject s: matching = non_target_total_minus_s + all_target_injected\n\n                # Precompute injected target total per model (from injected matrix)\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                # Build local col mapping: target_cols_all[local_idx] → local_idx\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}\n\n                elapsed = time.time() - t0\n                print(f\"  [{run_i}/{total_runs}] k={k} p={p} seed={seed} \"\n                      f\"flipped={n_flipped} ({elapsed:.0f}s)\")\n\n                # ── DIF on each target subject ──\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    # Matching variable for target subject: everything EXCEPT this subject\n                    # = non_target_total + injected scores from OTHER target subjects\n                    this_subj_injected = X_subj_inj.sum(axis=1).astype(np.float64)\n                    other_target_injected = injected_target_total - this_subj_injected\n\n                    match_ref = cross_ref + other_target_injected[ref_rows]\n                    match_foc = cross_foc + other_target_injected[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    # All items in target subject are \"contaminated\" (injected)\n                    tpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_tpr = tpr - baseline_fpr[subj]  # baseline is p=0 rate\n\n                    target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, target_subject=subj,\n                        n_items=len(s_cols), tpr=tpr, fpr=np.nan,\n                        delta_tpr=delta_tpr, delta_fpr=np.nan,\n                        n_target_c=n_c, n_clean_c=np.nan\n                    ))\n\n                # ── DIF on each non-target subject (FPR measurement) ──\n                # Sample non-targets to keep runtime manageable for large k\n                # For k≤5, test all; for k>5, test 20 random non-targets\n                if len(non_target_subjects) <= 20:\n                    test_nontargets = non_target_subjects\n                else:\n                    test_nontargets = sorted(rng.choice(non_target_subjects,\n                                                        size=20, replace=False))\n\n                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n                    s_cols_set = set(s_cols.tolist())\n\n                    X_ref_s = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n                    X_foc_s = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n                    # Matching = everything except this subject\n                    # = non_target_total (minus this subject) + all injected target scores\n                    other_nontarget_cols = np.array([c for c in non_target_cols\n                                                     if c not in s_cols_set])\n                    other_nt_ref = np.asarray(mat[ref_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n                    other_nt_foc = np.asarray(mat[foc_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                    match_ref = other_nt_ref + injected_target_total[ref_rows]\n                    match_foc = other_nt_foc + injected_target_total[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_fpr = fpr - baseline_fpr[subj]\n\n                    non_target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, non_target_subject=subj,\n                        n_items=len(s_cols),\n                        fpr=fpr, baseline_fpr=baseline_fpr[subj],\n                        delta_fpr=delta_fpr\n                    ))\n\n    # ── Save results ──\n    target_df = pd.DataFrame(target_rows_list)\n    target_df.to_csv(OUT / \"multi_subject_injection_results.csv\", index=False)\n\n    nontarget_df = pd.DataFrame(non_target_rows_list)\n    nontarget_df.to_csv(OUT / \"non_target_fpr_results.csv\", index=False)\n\n    # ── Summary by k,p ──\n    summary_rows = []\n    for k in ks:\n        for p_val in ps:\n            t_sub = target_df[(target_df[\"k\"] == k) & (target_df[\"p\"] == p_val)]\n            nt_sub = nontarget_df[(nontarget_df[\"k\"] == k) & (nontarget_df[\"p\"] == p_val)]\n\n            mean_tpr = t_sub[\"tpr\"].mean() if len(t_sub) > 0 else np.nan\n            mean_delta_tpr = t_sub[\"delta_tpr\"].mean() if len(t_sub) > 0 else np.nan\n            std_delta_tpr = t_sub.groupby(\"seed\")[\"delta_tpr\"].mean().std() if len(t_sub) > 0 else np.nan\n\n            mean_fpr_nt = nt_sub[\"fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            mean_delta_fpr_nt = nt_sub[\"delta_fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            std_delta_fpr_nt = nt_sub.groupby(\"seed\")[\"delta_fpr\"].mean().std() if len(nt_sub) > 0 else np.nan\n\n            summary_rows.append(dict(\n                k=k, p=p_val,\n                mean_tpr_target=round(mean_tpr, 4),\n                mean_delta_tpr=round(mean_delta_tpr, 4),\n                std_delta_tpr=round(std_delta_tpr, 4) if not np.isnan(std_delta_tpr) else np.nan,\n                mean_fpr_non_target=round(mean_fpr_nt, 4),\n                mean_delta_fpr_non_target=round(mean_delta_fpr_nt, 4),\n                std_delta_fpr_non_target=round(std_delta_fpr_nt, 4) if not np.isnan(std_delta_fpr_nt) else np.nan,\n            ))\n\n    summary_df = pd.DataFrame(summary_rows)\n    summary_df.to_csv(OUT / \"summary_by_k.csv\", index=False)\n\n    elapsed = time.time() - t0\n    print(f\"\\nDone in {elapsed:.0f}s. Saved to {OUT}\")\n    print(\"\\nSummary:\")\n    print(summary_df.to_string(index=False))\n\n    return target_df, nontarget_df, summary_df\n\n\ndef generate_report(target_df, nontarget_df, summary_df):\n    lines = [\n        \"# Plan 034: Multi-Subject Simultaneous Injection — Report\",\n        \"\",\n        \"## Method\",\n        \"\",\n        \"We test Proposition 1's robustness boundary by simultaneously injecting\",\n        \"differential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).\",\n        \"For each (k, p, seed) combination:\",\n        \"\",\n        \"1. Randomly select k target subjects from 57 MMLU subjects\",\n        \"2. For each item in the k target subjects, flip incorrect→correct responses\",\n        \"   in the focal group (2024 models within accuracy overlap) with probability p\",\n        \"3. Compute cross-subject MH-DIF for each target and non-target subject\",\n        \"   - Matching variable = total score on all subjects EXCEPT the tested one\",\n        \"   - For target subjects: matching includes injected scores from other targets\",\n        \"   - For non-target subjects: matching includes all injected target scores\",\n        \"4. Measure TPR on target subjects and FPR on non-target subjects\",\n        \"\",\n        f\"Grid: k ∈ {{{','.join(map(str, KS))}}}, p ∈ {{{','.join(map(str, PS))}}}, \"\n        f\"5 seeds per combination = {len(KS)*len(PS)*N_SEEDS} runs\",\n        \"\",\n        \"## Core Results: ΔFPR by k and p\",\n        \"\",\n    ]\n\n    # Summary table\n    lines.append(\"### Target Subjects (TPR)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean TPR | Mean ΔTPR | SD(ΔTPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_tpr_target']:.4f} | \"\n                      f\"{row['mean_delta_tpr']:.4f} | \"\n                      f\"{row['std_delta_tpr']:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Non-Target Subjects (FPR — key result)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean FPR | Mean ΔFPR | SD(ΔFPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_fpr_non_target']:.4f} | \"\n                      f\"{row['mean_delta_fpr_non_target']:.4f} | \"\n                      f\"{row['std_delta_fpr_non_target']:.4f} |\")\n    lines.append(\"\")\n\n    # Key findings\n    lines.append(\"## Key Findings\")\n    lines.append(\"\")\n\n    # Find threshold where ΔFPR becomes notable\n    for p_val in PS:\n        sub = summary_df[summary_df[\"p\"] == p_val]\n        significant_k = sub[sub[\"mean_delta_fpr_non_target\"].abs() > 0.01]\n        if len(significant_k) > 0:\n            first_k = int(significant_k.iloc[0][\"k\"])\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR exceeds 0.01 at k={first_k}\")\n        else:\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR stays below 0.01 for all k tested\")\n\n    lines.append(\"\")\n    lines.append(\"## Interpretation\")\n    lines.append(\"\")\n    lines.append(\"Proposition 1 guarantees ΔFPR=0 when the matching variable is uncontaminated.\")\n    lines.append(\"As k increases, more of the cross-subject total score is contaminated,\")\n    lines.append(\"violating the proposition's assumption. The k at which ΔFPR becomes\")\n    lines.append(\"practically significant marks the validity boundary of cross-subject DIF auditing.\")\n    lines.append(\"\")\n\n    report_path = OUT / \"plan_034_report.md\"\n    report_path.write_text(\"\\n\".join(lines))\n    print(f\"Report saved to {report_path}\")\n\n\nif __name__ == \"__main__\":\n    parser = argparse.ArgumentParser(description=\"Plan 034: Multi-Subject Injection\")\n    parser.add_argument(\"--quick\", action=\"store_true\",\n                        help=\"Quick validation: k∈{1,5,20}, p=0.3, seed=1\")\n    args = parser.parse_args()\n\n    if args.quick:\n        target_df, nontarget_df, summary_df = run_experiment(\n            ks=[1, 5, 20], ps=[0.3], n_seeds=1)\n    else:\n        target_df, nontarget_df, summary_df = run_experiment()\n\n    generate_report(target_df, nontarget_df, summary_df)\n",
    "structuredPatch": [
      {
        "oldStart": 295,
        "oldLines": 8,
        "newStart": 295,
        "newLines": 6,
        "lines": [
          "                 # Build injected matrix columns for target subjects",
          "                 # Collect all target columns for injection",
          "                 target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])",
          "-                target_cols_set = set(target_cols_all.tolist())",
          "-                non_target_cols = np.array([c for c in all_cols if c not in target_cols_set])",
          " ",
          "                 # Inject: flip incorrect→correct for focal inject models on target items",
          "                 mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)"
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

_source line 64_

<details open><summary>🔧 Tool call — Edit · `toolu_01EDhB7ktbYqMTSeTLLVi874`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
  "old_string": "                # Cross-subject matching variable = total on uninjected subjects\n                # (from original matrix — non-target subjects are never injected)\n                cross_ref = np.asarray(mat[ref_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n                cross_foc = np.asarray(mat[foc_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                # But for target subjects, the matching variable includes OTHER\n                # target subjects' injected scores too. We need per-subject matching.\n                # For target subject s: matching = non_target_total + injected_other_targets\n                # For non-target subject s: matching = non_target_total_minus_s + all_target_injected\n\n                # Precompute injected target total per model (from injected matrix)\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                # Build local col mapping: target_cols_all[local_idx] → local_idx\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}",
  "new_string": "                # Precompute totals for matching variable construction\n                # non_target_total = full_total - sum(target subject originals)\n                non_target_total_ref = full_total_ref - sum(subj_totals_ref[s] for s in target_subjects)\n                non_target_total_foc = full_total_foc - sum(subj_totals_foc[s] for s in target_subjects)\n\n                # Injected target total (all target subjects combined, after injection)\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                # Per-target-subject injected totals (for leave-one-out matching)\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}\n                target_subj_injected = {}\n                for s in target_subjects:\n                    local_idxs = np.array([target_col_to_local[c] for c in subject_cols[s]])\n                    target_subj_injected[s] = mat_dense_targets[:, local_idxs].sum(axis=1).astype(np.float64)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "b2e678e1-8ce5-4f97-b15d-82c9bc8f60cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SwYG5YYLBfknKzcRn4UFwy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 459,
      "cache_read_input_tokens": 51503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 459
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

_source line 65 · 2026-05-21T15:51:19.533Z_

<details><summary>↩ Tool result · `toolu_01EDhB7ktbYqMTSeTLLVi874`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "2dd356c4-eabf-4d9c-9f49-acf4a028139a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
    "oldString": "                # Cross-subject matching variable = total on uninjected subjects\n                # (from original matrix — non-target subjects are never injected)\n                cross_ref = np.asarray(mat[ref_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n                cross_foc = np.asarray(mat[foc_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                # But for target subjects, the matching variable includes OTHER\n                # target subjects' injected scores too. We need per-subject matching.\n                # For target subject s: matching = non_target_total + injected_other_targets\n                # For non-target subject s: matching = non_target_total_minus_s + all_target_injected\n\n                # Precompute injected target total per model (from injected matrix)\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                # Build local col mapping: target_cols_all[local_idx] → local_idx\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}",
    "newString": "                # Precompute totals for matching variable construction\n                # non_target_total = full_total - sum(target subject originals)\n                non_target_total_ref = full_total_ref - sum(subj_totals_ref[s] for s in target_subjects)\n                non_target_total_foc = full_total_foc - sum(subj_totals_foc[s] for s in target_subjects)\n\n                # Injected target total (all target subjects combined, after injection)\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                # Per-target-subject injected totals (for leave-one-out matching)\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}\n                target_subj_injected = {}\n                for s in target_subjects:\n                    local_idxs = np.array([target_col_to_local[c] for c in subject_cols[s]])\n                    target_subj_injected[s] = mat_dense_targets[:, local_idxs].sum(axis=1).astype(np.float64)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nplan_034: Multi-Subject Simultaneous Injection Experiment\n\nTests Proposition 1 (ΔFPR=0) robustness under multi-subject contamination.\nWhen k subjects are simultaneously injected, the cross-subject matching variable\n(total score on remaining 57-k uninjected subjects) degrades. ΔFPR(k) on\nnon-target subjects should increase with k, revealing the validity boundary.\n\nInputs:\n  - artifacts/response_matrix.npz         (5227 × 12508 sparse binary)\n  - artifacts/response_matrix_index.npz   (model_names, item_ids)\n  - artifacts/model_metadata.csv          (cohort_temporal, accuracy, ...)\n  - artifacts/item_metadata.csv           (item_id, subject, ...)\n\nOutputs:\n  - multi_subject_injection_results.csv   (per-target-subject DIF results)\n  - non_target_fpr_results.csv            (FPR on uninjected subjects)\n  - summary_by_k.csv                      (aggregated ΔFPR/ΔTPR by k,p)\n  - plan_034_report.md\n\nDependencies: numpy, pandas, scipy\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\nimport warnings\nimport argparse\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_034_multi_subject_injection\"\nOUT.mkdir(exist_ok=True)\n\nKS = [1, 2, 3, 5, 10, 20]\nPS = [0.1, 0.3, 0.5]\nN_SEEDS = 5\nN_STRATA = 5\nMIN_PER_STRATUM = 5\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE (from plan_016 with strata merging + external score support)\n# ════════════════════════════════════════════════════════════════════════════\ndef purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,\n                    external_scores_foc=None, min_per_stratum=5):\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])\n\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n\n        n_bins = len(edges) - 1\n        k_all = np.digitize(s_all, edges[1:-1])\n        strata_labels = _merge_small_strata(k_all, groups_all, n_bins, min_per_stratum)\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        x_all = np.concatenate([X_ref[:, j], X_foc[:, j]])\n\n        for k in np.unique(strata_labels):\n            mask_k = (strata_labels == k)\n            mask_ref = mask_k & (groups_all == 0)\n            mask_foc = mask_k & (groups_all == 1)\n\n            n1 = int(mask_ref.sum())\n            n0 = int(mask_foc.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(x_all[mask_ref].sum())\n            B = float(n1 - A)\n            C = float(x_all[mask_foc].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else np.inf\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets,\n                         n_strata_used=n_ok))\n\n    return pd.DataFrame(rows)\n\n\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\",\n                n_strata_used=0)\n\n\ndef _merge_small_strata(k_all, groups_all, n_bins, min_n):\n    labels = k_all.copy()\n    merged = True\n    while merged:\n        merged = False\n        unique_strata = sorted(np.unique(labels))\n        for i, k in enumerate(unique_strata):\n            mask_k = (labels == k)\n            n_ref = int((mask_k & (groups_all == 0)).sum())\n            n_foc = int((mask_k & (groups_all == 1)).sum())\n            if n_ref < min_n or n_foc < min_n:\n                if i + 1 < len(unique_strata):\n                    next_k = unique_strata[i + 1]\n                    labels[labels == next_k] = k\n                elif i > 0:\n                    prev_k = unique_strata[i - 1]\n                    labels[labels == k] = prev_k\n                merged = True\n                break\n    return labels\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\ndef load_data():\n    mat = load_npz(BASE / \"response_matrix.npz\")\n    idx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n    item2col = {iid: i for i, iid in enumerate(item_ids)}\n\n    model_meta = pd.read_csv(BASE / \"model_metadata.csv\")\n    item_meta = pd.read_csv(BASE / \"item_metadata.csv\")\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    # Temporal cohorts\n    ref_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"model_name\"]\n    foc_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"model_name\"]\n    ref_rows = np.array([name2row[n] for n in ref_names if n in name2row])\n    foc_rows = np.array([name2row[n] for n in foc_names if n in name2row])\n\n    # Focal inject subset: 2024 models in accuracy overlap with 2023\n    ref_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\n    foc_df = model_meta[model_meta[\"cohort_temporal\"] == \"2024\"]\n    t_min = max(ref_acc.min(), foc_df[\"accuracy\"].min())\n    t_max = min(ref_acc.max(), foc_df[\"accuracy\"].max())\n    foc_inject_mask = (foc_df[\"accuracy\"] >= t_min) & (foc_df[\"accuracy\"] <= t_max)\n    foc_inject_rows = np.array([name2row[n] for n in foc_df.loc[foc_inject_mask, \"model_name\"]\n                                if n in name2row])\n\n    # Build subject → column indices mapping\n    subject_cols = {}\n    subjects = sorted(item_meta[\"subject\"].unique())\n    for subj in subjects:\n        ids = item_meta.loc[item_meta[\"subject\"] == subj, \"item_id\"].values\n        cols = np.array([item2col[iid] for iid in ids if iid in item2col])\n        subject_cols[subj] = cols\n\n    return mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MAIN EXPERIMENT\n# ════════════════════════════════════════════════════════════════════════════\ndef run_experiment(ks=KS, ps=PS, n_seeds=N_SEEDS):\n    t0 = time.time()\n    mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols = load_data()\n    print(f\"Data loaded: {len(ref_rows)} ref, {len(foc_rows)} foc, \"\n          f\"{len(foc_inject_rows)} foc_inject, {len(subjects)} subjects\")\n\n    all_cols = np.concatenate([subject_cols[s] for s in subjects])\n\n    # Precompute per-subject total scores (original matrix) for ref/foc\n    # Enables O(1) matching variable via subtraction instead of re-slicing\n    subj_totals_ref = {}\n    subj_totals_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_totals_ref[subj] = np.asarray(mat[ref_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n        subj_totals_foc[subj] = np.asarray(mat[foc_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n\n    # Full total across all subjects\n    full_total_ref = sum(subj_totals_ref.values())\n    full_total_foc = sum(subj_totals_foc.values())\n\n    # Precompute dense submatrices per subject for ref/foc (avoids repeated sparse→dense)\n    subj_X_ref = {}\n    subj_X_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_X_ref[subj] = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n        subj_X_foc[subj] = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n    # ── Phase 1: baseline (p=0) per-subject FPR with cross-subject matching ──\n    print(\"Computing baseline FPR (p=0) for all subjects...\")\n    baseline_fpr = {}\n    baseline_n_c = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        cross_ref = full_total_ref - subj_totals_ref[subj]\n        cross_foc = full_total_foc - subj_totals_foc[subj]\n\n        n_strata = 3 if len(s_cols) < 100 else N_STRATA\n        dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,\n                              external_scores_ref=cross_ref,\n                              external_scores_foc=cross_foc,\n                              min_per_stratum=MIN_PER_STRATUM)\n        n_c = int((dif[\"ets_class\"] == \"C\").sum())\n        fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n        baseline_fpr[subj] = fpr\n        baseline_n_c[subj] = n_c\n\n    print(f\"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}\")\n\n    # ── Phase 2: injection runs ──\n    target_rows_list = []\n    non_target_rows_list = []\n    total_runs = len(ks) * len(ps) * n_seeds\n    run_i = 0\n\n    for k in ks:\n        for p in ps:\n            for seed in range(1, n_seeds + 1):\n                run_i += 1\n                rng = np.random.RandomState(seed)\n                target_subjects = sorted(rng.choice(subjects, size=k, replace=False))\n                non_target_subjects = [s for s in subjects if s not in target_subjects]\n\n                # Build injected matrix columns for target subjects\n                # Collect all target columns for injection\n                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])\n\n                # Inject: flip incorrect→correct for focal inject models on target items\n                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    block = mat_dense_targets[foc_inject_rows]\n                    zeros = (block == 0)\n                    flip_mask = zeros & (rng.random(block.shape) < p)\n                    n_flipped = int(flip_mask.sum())\n                    mat_dense_targets[foc_inject_rows] = block + flip_mask.astype(np.int8)\n\n                # Cross-subject matching variable = total on uninjected subjects\n                # (from original matrix — non-target subjects are never injected)\n                cross_ref = np.asarray(mat[ref_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n                cross_foc = np.asarray(mat[foc_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                # But for target subjects, the matching variable includes OTHER\n                # target subjects' injected scores too. We need per-subject matching.\n                # For target subject s: matching = non_target_total + injected_other_targets\n                # For non-target subject s: matching = non_target_total_minus_s + all_target_injected\n\n                # Precompute injected target total per model (from injected matrix)\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                # Build local col mapping: target_cols_all[local_idx] → local_idx\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}\n\n                elapsed = time.time() - t0\n                print(f\"  [{run_i}/{total_runs}] k={k} p={p} seed={seed} \"\n                      f\"flipped={n_flipped} ({elapsed:.0f}s)\")\n\n                # ── DIF on each target subject ──\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    # Matching variable for target subject: everything EXCEPT this subject\n                    # = non_target_total + injected scores from OTHER target subjects\n                    this_subj_injected = X_subj_inj.sum(axis=1).astype(np.float64)\n                    other_target_injected = injected_target_total - this_subj_injected\n\n                    match_ref = cross_ref + other_target_injected[ref_rows]\n                    match_foc = cross_foc + other_target_injected[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    # All items in target subject are \"contaminated\" (injected)\n                    tpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_tpr = tpr - baseline_fpr[subj]  # baseline is p=0 rate\n\n                    target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, target_subject=subj,\n                        n_items=len(s_cols), tpr=tpr, fpr=np.nan,\n                        delta_tpr=delta_tpr, delta_fpr=np.nan,\n                        n_target_c=n_c, n_clean_c=np.nan\n                    ))\n\n                # ── DIF on each non-target subject (FPR measurement) ──\n                # Sample non-targets to keep runtime manageable for large k\n                # For k≤5, test all; for k>5, test 20 random non-targets\n                if len(non_target_subjects) <= 20:\n                    test_nontargets = non_target_subjects\n                else:\n                    test_nontargets = sorted(rng.choice(non_target_subjects,\n                                                        size=20, replace=False))\n\n                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n                    s_cols_set = set(s_cols.tolist())\n\n                    X_ref_s = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n                    X_foc_s = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n                    # Matching = everything except this subject\n                    # = non_target_total (minus this subject) + all injected target scores\n                    other_nontarget_cols = np.array([c for c in non_target_cols\n                                                     if c not in s_cols_set])\n                    other_nt_ref = np.asarray(mat[ref_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n                    other_nt_foc = np.asarray(mat[foc_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                    match_ref = other_nt_ref + injected_target_total[ref_rows]\n                    match_foc = other_nt_foc + injected_target_total[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_fpr = fpr - baseline_fpr[subj]\n\n                    non_target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, non_target_subject=subj,\n                        n_items=len(s_cols),\n                        fpr=fpr, baseline_fpr=baseline_fpr[subj],\n                        delta_fpr=delta_fpr\n                    ))\n\n    # ── Save results ──\n    target_df = pd.DataFrame(target_rows_list)\n    target_df.to_csv(OUT / \"multi_subject_injection_results.csv\", index=False)\n\n    nontarget_df = pd.DataFrame(non_target_rows_list)\n    nontarget_df.to_csv(OUT / \"non_target_fpr_results.csv\", index=False)\n\n    # ── Summary by k,p ──\n    summary_rows = []\n    for k in ks:\n        for p_val in ps:\n            t_sub = target_df[(target_df[\"k\"] == k) & (target_df[\"p\"] == p_val)]\n            nt_sub = nontarget_df[(nontarget_df[\"k\"] == k) & (nontarget_df[\"p\"] == p_val)]\n\n            mean_tpr = t_sub[\"tpr\"].mean() if len(t_sub) > 0 else np.nan\n            mean_delta_tpr = t_sub[\"delta_tpr\"].mean() if len(t_sub) > 0 else np.nan\n            std_delta_tpr = t_sub.groupby(\"seed\")[\"delta_tpr\"].mean().std() if len(t_sub) > 0 else np.nan\n\n            mean_fpr_nt = nt_sub[\"fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            mean_delta_fpr_nt = nt_sub[\"delta_fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            std_delta_fpr_nt = nt_sub.groupby(\"seed\")[\"delta_fpr\"].mean().std() if len(nt_sub) > 0 else np.nan\n\n            summary_rows.append(dict(\n                k=k, p=p_val,\n                mean_tpr_target=round(mean_tpr, 4),\n                mean_delta_tpr=round(mean_delta_tpr, 4),\n                std_delta_tpr=round(std_delta_tpr, 4) if not np.isnan(std_delta_tpr) else np.nan,\n                mean_fpr_non_target=round(mean_fpr_nt, 4),\n                mean_delta_fpr_non_target=round(mean_delta_fpr_nt, 4),\n                std_delta_fpr_non_target=round(std_delta_fpr_nt, 4) if not np.isnan(std_delta_fpr_nt) else np.nan,\n            ))\n\n    summary_df = pd.DataFrame(summary_rows)\n    summary_df.to_csv(OUT / \"summary_by_k.csv\", index=False)\n\n    elapsed = time.time() - t0\n    print(f\"\\nDone in {elapsed:.0f}s. Saved to {OUT}\")\n    print(\"\\nSummary:\")\n    print(summary_df.to_string(index=False))\n\n    return target_df, nontarget_df, summary_df\n\n\ndef generate_report(target_df, nontarget_df, summary_df):\n    lines = [\n        \"# Plan 034: Multi-Subject Simultaneous Injection — Report\",\n        \"\",\n        \"## Method\",\n        \"\",\n        \"We test Proposition 1's robustness boundary by simultaneously injecting\",\n        \"differential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).\",\n        \"For each (k, p, seed) combination:\",\n        \"\",\n        \"1. Randomly select k target subjects from 57 MMLU subjects\",\n        \"2. For each item in the k target subjects, flip incorrect→correct responses\",\n        \"   in the focal group (2024 models within accuracy overlap) with probability p\",\n        \"3. Compute cross-subject MH-DIF for each target and non-target subject\",\n        \"   - Matching variable = total score on all subjects EXCEPT the tested one\",\n        \"   - For target subjects: matching includes injected scores from other targets\",\n        \"   - For non-target subjects: matching includes all injected target scores\",\n        \"4. Measure TPR on target subjects and FPR on non-target subjects\",\n        \"\",\n        f\"Grid: k ∈ {{{','.join(map(str, KS))}}}, p ∈ {{{','.join(map(str, PS))}}}, \"\n        f\"5 seeds per combination = {len(KS)*len(PS)*N_SEEDS} runs\",\n        \"\",\n        \"## Core Results: ΔFPR by k and p\",\n        \"\",\n    ]\n\n    # Summary table\n    lines.append(\"### Target Subjects (TPR)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean TPR | Mean ΔTPR | SD(ΔTPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_tpr_target']:.4f} | \"\n                      f\"{row['mean_delta_tpr']:.4f} | \"\n                      f\"{row['std_delta_tpr']:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Non-Target Subjects (FPR — key result)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean FPR | Mean ΔFPR | SD(ΔFPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_fpr_non_target']:.4f} | \"\n                      f\"{row['mean_delta_fpr_non_target']:.4f} | \"\n                      f\"{row['std_delta_fpr_non_target']:.4f} |\")\n    lines.append(\"\")\n\n    # Key findings\n    lines.append(\"## Key Findings\")\n    lines.append(\"\")\n\n    # Find threshold where ΔFPR becomes notable\n    for p_val in PS:\n        sub = summary_df[summary_df[\"p\"] == p_val]\n        significant_k = sub[sub[\"mean_delta_fpr_non_target\"].abs() > 0.01]\n        if len(significant_k) > 0:\n            first_k = int(significant_k.iloc[0][\"k\"])\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR exceeds 0.01 at k={first_k}\")\n        else:\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR stays below 0.01 for all k tested\")\n\n    lines.append(\"\")\n    lines.append(\"## Interpretation\")\n    lines.append(\"\")\n    lines.append(\"Proposition 1 guarantees ΔFPR=0 when the matching variable is uncontaminated.\")\n    lines.append(\"As k increases, more of the cross-subject total score is contaminated,\")\n    lines.append(\"violating the proposition's assumption. The k at which ΔFPR becomes\")\n    lines.append(\"practically significant marks the validity boundary of cross-subject DIF auditing.\")\n    lines.append(\"\")\n\n    report_path = OUT / \"plan_034_report.md\"\n    report_path.write_text(\"\\n\".join(lines))\n    print(f\"Report saved to {report_path}\")\n\n\nif __name__ == \"__main__\":\n    parser = argparse.ArgumentParser(description=\"Plan 034: Multi-Subject Injection\")\n    parser.add_argument(\"--quick\", action=\"store_true\",\n                        help=\"Quick validation: k∈{1,5,20}, p=0.3, seed=1\")\n    args = parser.parse_args()\n\n    if args.quick:\n        target_df, nontarget_df, summary_df = run_experiment(\n            ks=[1, 5, 20], ps=[0.3], n_seeds=1)\n    else:\n        target_df, nontarget_df, summary_df = run_experiment()\n\n    generate_report(target_df, nontarget_df, summary_df)\n",
    "structuredPatch": [
      {
        "oldStart": 306,
        "oldLines": 21,
        "newStart": 306,
        "newLines": 20,
        "lines": [
          "                     n_flipped = int(flip_mask.sum())",
          "                     mat_dense_targets[foc_inject_rows] = block + flip_mask.astype(np.int8)",
          " ",
          "-                # Cross-subject matching variable = total on uninjected subjects",
          "-                # (from original matrix — non-target subjects are never injected)",
          "-                cross_ref = np.asarray(mat[ref_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)",
          "-                cross_foc = np.asarray(mat[foc_rows][:, non_target_cols].sum(axis=1)).ravel().astype(np.float64)",
          "+                # Precompute totals for matching variable construction",
          "+                # non_target_total = full_total - sum(target subject originals)",
          "+                non_target_total_ref = full_total_ref - sum(subj_totals_ref[s] for s in target_subjects)",
          "+                non_target_total_foc = full_total_foc - sum(subj_totals_foc[s] for s in target_subjects)",
          " ",
          "-                # But for target subjects, the matching variable includes OTHER",
          "-                # target subjects' injected scores too. We need per-subject matching.",
          "-                # For target subject s: matching = non_target_total + injected_other_targets",
          "-                # For non-target subject s: matching = non_target_total_minus_s + all_target_injected",
          "-",
          "-                # Precompute injected target total per model (from injected matrix)",
          "+                # Injected target total (all target subjects combined, after injection)",
          "                 injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)",
          " ",
          "-                # Build local col mapping: target_cols_all[local_idx] → local_idx",
          "+                # Per-target-subject injected totals (for leave-one-out matching)",
          "                 target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}",
          "+                target_subj_injected = {}",
          "+                for s in target_subjects:",
          "+                    local_idxs = np.array([target_col_to_local[c] for c in subject_cols[s]])",
          "+                    target_subj_injected[s] = mat_dense_targets[:, local_idxs].sum(axis=1).astype(np.float64)",
          " ",
          "                 elapsed = time.time() - t0",
          "                 print(f\"  [{run_i}/{total_runs}] k={k} p={p} seed={seed} \""
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

### Assistant

_source line 66_

Now update the target subject DIF computation to use the new precomputed values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "1d880c27-6dde-48c6-8870-f8144e5f8eb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrRZgvdQ4iaWTW5VLAZzqh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 823,
      "cache_read_input_tokens": 51962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 823
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

_source line 67_

<details open><summary>🔧 Tool call — Edit · `toolu_019BMvc7fzM37GHhnYQ4AyPn`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
  "old_string": "                # ── DIF on each target subject ──\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    # Matching variable for target subject: everything EXCEPT this subject\n                    # = non_target_total + injected scores from OTHER target subjects\n                    this_subj_injected = X_subj_inj.sum(axis=1).astype(np.float64)\n                    other_target_injected = injected_target_total - this_subj_injected\n\n                    match_ref = cross_ref + other_target_injected[ref_rows]\n                    match_foc = cross_foc + other_target_injected[foc_rows]",
  "new_string": "                # ── DIF on each target subject ──\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    # Matching = non_target_total + other_target_injected\n                    other_target_inj = injected_target_total - target_subj_injected[subj]\n                    match_ref = non_target_total_ref + other_target_inj[ref_rows]\n                    match_foc = non_target_total_foc + other_target_inj[foc_rows]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "d9b74f19-4438-4f1b-a6ea-a7301f139457",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrRZgvdQ4iaWTW5VLAZzqh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 823,
      "cache_read_input_tokens": 51962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 823
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

_source line 68 · 2026-05-21T15:51:30.287Z_

<details><summary>↩ Tool result · `toolu_019BMvc7fzM37GHhnYQ4AyPn`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "8bab9a0c-c5db-41c7-b156-54287c5f6c7d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
    "oldString": "                # ── DIF on each target subject ──\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    # Matching variable for target subject: everything EXCEPT this subject\n                    # = non_target_total + injected scores from OTHER target subjects\n                    this_subj_injected = X_subj_inj.sum(axis=1).astype(np.float64)\n                    other_target_injected = injected_target_total - this_subj_injected\n\n                    match_ref = cross_ref + other_target_injected[ref_rows]\n                    match_foc = cross_foc + other_target_injected[foc_rows]",
    "newString": "                # ── DIF on each target subject ──\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    # Matching = non_target_total + other_target_injected\n                    other_target_inj = injected_target_total - target_subj_injected[subj]\n                    match_ref = non_target_total_ref + other_target_inj[ref_rows]\n                    match_foc = non_target_total_foc + other_target_inj[foc_rows]",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nplan_034: Multi-Subject Simultaneous Injection Experiment\n\nTests Proposition 1 (ΔFPR=0) robustness under multi-subject contamination.\nWhen k subjects are simultaneously injected, the cross-subject matching variable\n(total score on remaining 57-k uninjected subjects) degrades. ΔFPR(k) on\nnon-target subjects should increase with k, revealing the validity boundary.\n\nInputs:\n  - artifacts/response_matrix.npz         (5227 × 12508 sparse binary)\n  - artifacts/response_matrix_index.npz   (model_names, item_ids)\n  - artifacts/model_metadata.csv          (cohort_temporal, accuracy, ...)\n  - artifacts/item_metadata.csv           (item_id, subject, ...)\n\nOutputs:\n  - multi_subject_injection_results.csv   (per-target-subject DIF results)\n  - non_target_fpr_results.csv            (FPR on uninjected subjects)\n  - summary_by_k.csv                      (aggregated ΔFPR/ΔTPR by k,p)\n  - plan_034_report.md\n\nDependencies: numpy, pandas, scipy\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\nimport warnings\nimport argparse\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_034_multi_subject_injection\"\nOUT.mkdir(exist_ok=True)\n\nKS = [1, 2, 3, 5, 10, 20]\nPS = [0.1, 0.3, 0.5]\nN_SEEDS = 5\nN_STRATA = 5\nMIN_PER_STRATUM = 5\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE (from plan_016 with strata merging + external score support)\n# ════════════════════════════════════════════════════════════════════════════\ndef purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,\n                    external_scores_foc=None, min_per_stratum=5):\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])\n\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n\n        n_bins = len(edges) - 1\n        k_all = np.digitize(s_all, edges[1:-1])\n        strata_labels = _merge_small_strata(k_all, groups_all, n_bins, min_per_stratum)\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        x_all = np.concatenate([X_ref[:, j], X_foc[:, j]])\n\n        for k in np.unique(strata_labels):\n            mask_k = (strata_labels == k)\n            mask_ref = mask_k & (groups_all == 0)\n            mask_foc = mask_k & (groups_all == 1)\n\n            n1 = int(mask_ref.sum())\n            n0 = int(mask_foc.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(x_all[mask_ref].sum())\n            B = float(n1 - A)\n            C = float(x_all[mask_foc].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else np.inf\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets,\n                         n_strata_used=n_ok))\n\n    return pd.DataFrame(rows)\n\n\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\",\n                n_strata_used=0)\n\n\ndef _merge_small_strata(k_all, groups_all, n_bins, min_n):\n    labels = k_all.copy()\n    merged = True\n    while merged:\n        merged = False\n        unique_strata = sorted(np.unique(labels))\n        for i, k in enumerate(unique_strata):\n            mask_k = (labels == k)\n            n_ref = int((mask_k & (groups_all == 0)).sum())\n            n_foc = int((mask_k & (groups_all == 1)).sum())\n            if n_ref < min_n or n_foc < min_n:\n                if i + 1 < len(unique_strata):\n                    next_k = unique_strata[i + 1]\n                    labels[labels == next_k] = k\n                elif i > 0:\n                    prev_k = unique_strata[i - 1]\n                    labels[labels == k] = prev_k\n                merged = True\n                break\n    return labels\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\ndef load_data():\n    mat = load_npz(BASE / \"response_matrix.npz\")\n    idx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n    item2col = {iid: i for i, iid in enumerate(item_ids)}\n\n    model_meta = pd.read_csv(BASE / \"model_metadata.csv\")\n    item_meta = pd.read_csv(BASE / \"item_metadata.csv\")\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    # Temporal cohorts\n    ref_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"model_name\"]\n    foc_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"model_name\"]\n    ref_rows = np.array([name2row[n] for n in ref_names if n in name2row])\n    foc_rows = np.array([name2row[n] for n in foc_names if n in name2row])\n\n    # Focal inject subset: 2024 models in accuracy overlap with 2023\n    ref_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\n    foc_df = model_meta[model_meta[\"cohort_temporal\"] == \"2024\"]\n    t_min = max(ref_acc.min(), foc_df[\"accuracy\"].min())\n    t_max = min(ref_acc.max(), foc_df[\"accuracy\"].max())\n    foc_inject_mask = (foc_df[\"accuracy\"] >= t_min) & (foc_df[\"accuracy\"] <= t_max)\n    foc_inject_rows = np.array([name2row[n] for n in foc_df.loc[foc_inject_mask, \"model_name\"]\n                                if n in name2row])\n\n    # Build subject → column indices mapping\n    subject_cols = {}\n    subjects = sorted(item_meta[\"subject\"].unique())\n    for subj in subjects:\n        ids = item_meta.loc[item_meta[\"subject\"] == subj, \"item_id\"].values\n        cols = np.array([item2col[iid] for iid in ids if iid in item2col])\n        subject_cols[subj] = cols\n\n    return mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MAIN EXPERIMENT\n# ════════════════════════════════════════════════════════════════════════════\ndef run_experiment(ks=KS, ps=PS, n_seeds=N_SEEDS):\n    t0 = time.time()\n    mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols = load_data()\n    print(f\"Data loaded: {len(ref_rows)} ref, {len(foc_rows)} foc, \"\n          f\"{len(foc_inject_rows)} foc_inject, {len(subjects)} subjects\")\n\n    all_cols = np.concatenate([subject_cols[s] for s in subjects])\n\n    # Precompute per-subject total scores (original matrix) for ref/foc\n    # Enables O(1) matching variable via subtraction instead of re-slicing\n    subj_totals_ref = {}\n    subj_totals_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_totals_ref[subj] = np.asarray(mat[ref_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n        subj_totals_foc[subj] = np.asarray(mat[foc_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n\n    # Full total across all subjects\n    full_total_ref = sum(subj_totals_ref.values())\n    full_total_foc = sum(subj_totals_foc.values())\n\n    # Precompute dense submatrices per subject for ref/foc (avoids repeated sparse→dense)\n    subj_X_ref = {}\n    subj_X_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_X_ref[subj] = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n        subj_X_foc[subj] = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n    # ── Phase 1: baseline (p=0) per-subject FPR with cross-subject matching ──\n    print(\"Computing baseline FPR (p=0) for all subjects...\")\n    baseline_fpr = {}\n    baseline_n_c = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        cross_ref = full_total_ref - subj_totals_ref[subj]\n        cross_foc = full_total_foc - subj_totals_foc[subj]\n\n        n_strata = 3 if len(s_cols) < 100 else N_STRATA\n        dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,\n                              external_scores_ref=cross_ref,\n                              external_scores_foc=cross_foc,\n                              min_per_stratum=MIN_PER_STRATUM)\n        n_c = int((dif[\"ets_class\"] == \"C\").sum())\n        fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n        baseline_fpr[subj] = fpr\n        baseline_n_c[subj] = n_c\n\n    print(f\"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}\")\n\n    # ── Phase 2: injection runs ──\n    target_rows_list = []\n    non_target_rows_list = []\n    total_runs = len(ks) * len(ps) * n_seeds\n    run_i = 0\n\n    for k in ks:\n        for p in ps:\n            for seed in range(1, n_seeds + 1):\n                run_i += 1\n                rng = np.random.RandomState(seed)\n                target_subjects = sorted(rng.choice(subjects, size=k, replace=False))\n                non_target_subjects = [s for s in subjects if s not in target_subjects]\n\n                # Build injected matrix columns for target subjects\n                # Collect all target columns for injection\n                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])\n\n                # Inject: flip incorrect→correct for focal inject models on target items\n                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    block = mat_dense_targets[foc_inject_rows]\n                    zeros = (block == 0)\n                    flip_mask = zeros & (rng.random(block.shape) < p)\n                    n_flipped = int(flip_mask.sum())\n                    mat_dense_targets[foc_inject_rows] = block + flip_mask.astype(np.int8)\n\n                # Precompute totals for matching variable construction\n                # non_target_total = full_total - sum(target subject originals)\n                non_target_total_ref = full_total_ref - sum(subj_totals_ref[s] for s in target_subjects)\n                non_target_total_foc = full_total_foc - sum(subj_totals_foc[s] for s in target_subjects)\n\n                # Injected target total (all target subjects combined, after injection)\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                # Per-target-subject injected totals (for leave-one-out matching)\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}\n                target_subj_injected = {}\n                for s in target_subjects:\n                    local_idxs = np.array([target_col_to_local[c] for c in subject_cols[s]])\n                    target_subj_injected[s] = mat_dense_targets[:, local_idxs].sum(axis=1).astype(np.float64)\n\n                elapsed = time.time() - t0\n                print(f\"  [{run_i}/{total_runs}] k={k} p={p} seed={seed} \"\n                      f\"flipped={n_flipped} ({elapsed:.0f}s)\")\n\n                # ── DIF on each target subject ──\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    # Matching variable for target subject: everything EXCEPT this subject\n                    # = non_target_total + injected scores from OTHER target subjects\n                    this_subj_injected = X_subj_inj.sum(axis=1).astype(np.float64)\n                    other_target_injected = injected_target_total - this_subj_injected\n\n                    match_ref = cross_ref + other_target_injected[ref_rows]\n                    match_foc = cross_foc + other_target_injected[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    # All items in target subject are \"contaminated\" (injected)\n                    tpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_tpr = tpr - baseline_fpr[subj]  # baseline is p=0 rate\n\n                    target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, target_subject=subj,\n                        n_items=len(s_cols), tpr=tpr, fpr=np.nan,\n                        delta_tpr=delta_tpr, delta_fpr=np.nan,\n                        n_target_c=n_c, n_clean_c=np.nan\n                    ))\n\n                # ── DIF on each non-target subject (FPR measurement) ──\n                # Sample non-targets to keep runtime manageable for large k\n                # For k≤5, test all; for k>5, test 20 random non-targets\n                if len(non_target_subjects) <= 20:\n                    test_nontargets = non_target_subjects\n                else:\n                    test_nontargets = sorted(rng.choice(non_target_subjects,\n                                                        size=20, replace=False))\n\n                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n                    s_cols_set = set(s_cols.tolist())\n\n                    X_ref_s = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n                    X_foc_s = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n                    # Matching = everything except this subject\n                    # = non_target_total (minus this subject) + all injected target scores\n                    other_nontarget_cols = np.array([c for c in non_target_cols\n                                                     if c not in s_cols_set])\n                    other_nt_ref = np.asarray(mat[ref_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n                    other_nt_foc = np.asarray(mat[foc_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                    match_ref = other_nt_ref + injected_target_total[ref_rows]\n                    match_foc = other_nt_foc + injected_target_total[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_fpr = fpr - baseline_fpr[subj]\n\n                    non_target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, non_target_subject=subj,\n                        n_items=len(s_cols),\n                        fpr=fpr, baseline_fpr=baseline_fpr[subj],\n                        delta_fpr=delta_fpr\n                    ))\n\n    # ── Save results ──\n    target_df = pd.DataFrame(target_rows_list)\n    target_df.to_csv(OUT / \"multi_subject_injection_results.csv\", index=False)\n\n    nontarget_df = pd.DataFrame(non_target_rows_list)\n    nontarget_df.to_csv(OUT / \"non_target_fpr_results.csv\", index=False)\n\n    # ── Summary by k,p ──\n    summary_rows = []\n    for k in ks:\n        for p_val in ps:\n            t_sub = target_df[(target_df[\"k\"] == k) & (target_df[\"p\"] == p_val)]\n            nt_sub = nontarget_df[(nontarget_df[\"k\"] == k) & (nontarget_df[\"p\"] == p_val)]\n\n            mean_tpr = t_sub[\"tpr\"].mean() if len(t_sub) > 0 else np.nan\n            mean_delta_tpr = t_sub[\"delta_tpr\"].mean() if len(t_sub) > 0 else np.nan\n            std_delta_tpr = t_sub.groupby(\"seed\")[\"delta_tpr\"].mean().std() if len(t_sub) > 0 else np.nan\n\n            mean_fpr_nt = nt_sub[\"fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            mean_delta_fpr_nt = nt_sub[\"delta_fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            std_delta_fpr_nt = nt_sub.groupby(\"seed\")[\"delta_fpr\"].mean().std() if len(nt_sub) > 0 else np.nan\n\n            summary_rows.append(dict(\n                k=k, p=p_val,\n                mean_tpr_target=round(mean_tpr, 4),\n                mean_delta_tpr=round(mean_delta_tpr, 4),\n                std_delta_tpr=round(std_delta_tpr, 4) if not np.isnan(std_delta_tpr) else np.nan,\n                mean_fpr_non_target=round(mean_fpr_nt, 4),\n                mean_delta_fpr_non_target=round(mean_delta_fpr_nt, 4),\n                std_delta_fpr_non_target=round(std_delta_fpr_nt, 4) if not np.isnan(std_delta_fpr_nt) else np.nan,\n            ))\n\n    summary_df = pd.DataFrame(summary_rows)\n    summary_df.to_csv(OUT / \"summary_by_k.csv\", index=False)\n\n    elapsed = time.time() - t0\n    print(f\"\\nDone in {elapsed:.0f}s. Saved to {OUT}\")\n    print(\"\\nSummary:\")\n    print(summary_df.to_string(index=False))\n\n    return target_df, nontarget_df, summary_df\n\n\ndef generate_report(target_df, nontarget_df, summary_df):\n    lines = [\n        \"# Plan 034: Multi-Subject Simultaneous Injection — Report\",\n        \"\",\n        \"## Method\",\n        \"\",\n        \"We test Proposition 1's robustness boundary by simultaneously injecting\",\n        \"differential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).\",\n        \"For each (k, p, seed) combination:\",\n        \"\",\n        \"1. Randomly select k target subjects from 57 MMLU subjects\",\n        \"2. For each item in the k target subjects, flip incorrect→correct responses\",\n        \"   in the focal group (2024 models within accuracy overlap) with probability p\",\n        \"3. Compute cross-subject MH-DIF for each target and non-target subject\",\n        \"   - Matching variable = total score on all subjects EXCEPT the tested one\",\n        \"   - For target subjects: matching includes injected scores from other targets\",\n        \"   - For non-target subjects: matching includes all injected target scores\",\n        \"4. Measure TPR on target subjects and FPR on non-target subjects\",\n        \"\",\n        f\"Grid: k ∈ {{{','.join(map(str, KS))}}}, p ∈ {{{','.join(map(str, PS))}}}, \"\n        f\"5 seeds per combination = {len(KS)*len(PS)*N_SEEDS} runs\",\n        \"\",\n        \"## Core Results: ΔFPR by k and p\",\n        \"\",\n    ]\n\n    # Summary table\n    lines.append(\"### Target Subjects (TPR)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean TPR | Mean ΔTPR | SD(ΔTPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_tpr_target']:.4f} | \"\n                      f\"{row['mean_delta_tpr']:.4f} | \"\n                      f\"{row['std_delta_tpr']:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Non-Target Subjects (FPR — key result)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean FPR | Mean ΔFPR | SD(ΔFPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_fpr_non_target']:.4f} | \"\n                      f\"{row['mean_delta_fpr_non_target']:.4f} | \"\n                      f\"{row['std_delta_fpr_non_target']:.4f} |\")\n    lines.append(\"\")\n\n    # Key findings\n    lines.append(\"## Key Findings\")\n    lines.append(\"\")\n\n    # Find threshold where ΔFPR becomes notable\n    for p_val in PS:\n        sub = summary_df[summary_df[\"p\"] == p_val]\n        significant_k = sub[sub[\"mean_delta_fpr_non_target\"].abs() > 0.01]\n        if len(significant_k) > 0:\n            first_k = int(significant_k.iloc[0][\"k\"])\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR exceeds 0.01 at k={first_k}\")\n        else:\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR stays below 0.01 for all k tested\")\n\n    lines.append(\"\")\n    lines.append(\"## Interpretation\")\n    lines.append(\"\")\n    lines.append(\"Proposition 1 guarantees ΔFPR=0 when the matching variable is uncontaminated.\")\n    lines.append(\"As k increases, more of the cross-subject total score is contaminated,\")\n    lines.append(\"violating the proposition's assumption. The k at which ΔFPR becomes\")\n    lines.append(\"practically significant marks the validity boundary of cross-subject DIF auditing.\")\n    lines.append(\"\")\n\n    report_path = OUT / \"plan_034_report.md\"\n    report_path.write_text(\"\\n\".join(lines))\n    print(f\"Report saved to {report_path}\")\n\n\nif __name__ == \"__main__\":\n    parser = argparse.ArgumentParser(description=\"Plan 034: Multi-Subject Injection\")\n    parser.add_argument(\"--quick\", action=\"store_true\",\n                        help=\"Quick validation: k∈{1,5,20}, p=0.3, seed=1\")\n    args = parser.parse_args()\n\n    if args.quick:\n        target_df, nontarget_df, summary_df = run_experiment(\n            ks=[1, 5, 20], ps=[0.3], n_seeds=1)\n    else:\n        target_df, nontarget_df, summary_df = run_experiment()\n\n    generate_report(target_df, nontarget_df, summary_df)\n",
    "structuredPatch": [
      {
        "oldStart": 334,
        "oldLines": 14,
        "newStart": 334,
        "newLines": 11,
        "lines": [
          "                     X_ref_s = X_subj_inj[ref_rows]",
          "                     X_foc_s = X_subj_inj[foc_rows]",
          " ",
          "-                    # Matching variable for target subject: everything EXCEPT this subject",
          "-                    # = non_target_total + injected scores from OTHER target subjects",
          "-                    this_subj_injected = X_subj_inj.sum(axis=1).astype(np.float64)",
          "-                    other_target_injected = injected_target_total - this_subj_injected",
          "+                    # Matching = non_target_total + other_target_injected",
          "+                    other_target_inj = injected_target_total - target_subj_injected[subj]",
          "+                    match_ref = non_target_total_ref + other_target_inj[ref_rows]",
          "+                    match_foc = non_target_total_foc + other_target_inj[foc_rows]",
          " ",
          "-                    match_ref = cross_ref + other_target_injected[ref_rows]",
          "-                    match_foc = cross_foc + other_target_injected[foc_rows]",
          "-",
          "                     n_strata = 3 if len(s_cols) < 100 else N_STRATA",
          "                     dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,",
          "                                           external_scores_ref=match_ref,"
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

### Assistant

_source line 69_

Now optimize the non-target loop to use precomputed totals instead of sparse slicing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "d93deaad-ffe0-4c8c-82ad-d5aaaee84a5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2tbd9CLLzAYaiM8oo9qwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 763,
      "cache_read_input_tokens": 52785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 763
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

_source line 70_

<details open><summary>🔧 Tool call — Edit · `toolu_01AgN2tu35HasKCVYxUTY16R`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
  "old_string": "                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n                    s_cols_set = set(s_cols.tolist())\n\n                    X_ref_s = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n                    X_foc_s = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n                    # Matching = everything except this subject\n                    # = non_target_total (minus this subject) + all injected target scores\n                    other_nontarget_cols = np.array([c for c in non_target_cols\n                                                     if c not in s_cols_set])\n                    other_nt_ref = np.asarray(mat[ref_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n                    other_nt_foc = np.asarray(mat[foc_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                    match_ref = other_nt_ref + injected_target_total[ref_rows]\n                    match_foc = other_nt_foc + injected_target_total[foc_rows]",
  "new_string": "                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n\n                    # Matching = (non_target_total - this subject) + all injected target total\n                    match_ref = (non_target_total_ref - subj_totals_ref[subj]\n                                 + injected_target_total[ref_rows])\n                    match_foc = (non_target_total_foc - subj_totals_foc[subj]\n                                 + injected_target_total[foc_rows])"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "61254abe-f8e5-4f13-b17d-43f25a66ddb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2tbd9CLLzAYaiM8oo9qwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 763,
      "cache_read_input_tokens": 52785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 763
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

_source line 71 · 2026-05-21T15:51:43.631Z_

<details><summary>↩ Tool result · `toolu_01AgN2tu35HasKCVYxUTY16R`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "99e625af-df61-47d0-876d-9505ff124383",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
    "oldString": "                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n                    s_cols_set = set(s_cols.tolist())\n\n                    X_ref_s = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n                    X_foc_s = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n                    # Matching = everything except this subject\n                    # = non_target_total (minus this subject) + all injected target scores\n                    other_nontarget_cols = np.array([c for c in non_target_cols\n                                                     if c not in s_cols_set])\n                    other_nt_ref = np.asarray(mat[ref_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n                    other_nt_foc = np.asarray(mat[foc_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                    match_ref = other_nt_ref + injected_target_total[ref_rows]\n                    match_foc = other_nt_foc + injected_target_total[foc_rows]",
    "newString": "                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n\n                    # Matching = (non_target_total - this subject) + all injected target total\n                    match_ref = (non_target_total_ref - subj_totals_ref[subj]\n                                 + injected_target_total[ref_rows])\n                    match_foc = (non_target_total_foc - subj_totals_foc[subj]\n                                 + injected_target_total[foc_rows])",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nplan_034: Multi-Subject Simultaneous Injection Experiment\n\nTests Proposition 1 (ΔFPR=0) robustness under multi-subject contamination.\nWhen k subjects are simultaneously injected, the cross-subject matching variable\n(total score on remaining 57-k uninjected subjects) degrades. ΔFPR(k) on\nnon-target subjects should increase with k, revealing the validity boundary.\n\nInputs:\n  - artifacts/response_matrix.npz         (5227 × 12508 sparse binary)\n  - artifacts/response_matrix_index.npz   (model_names, item_ids)\n  - artifacts/model_metadata.csv          (cohort_temporal, accuracy, ...)\n  - artifacts/item_metadata.csv           (item_id, subject, ...)\n\nOutputs:\n  - multi_subject_injection_results.csv   (per-target-subject DIF results)\n  - non_target_fpr_results.csv            (FPR on uninjected subjects)\n  - summary_by_k.csv                      (aggregated ΔFPR/ΔTPR by k,p)\n  - plan_034_report.md\n\nDependencies: numpy, pandas, scipy\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\nimport warnings\nimport argparse\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_034_multi_subject_injection\"\nOUT.mkdir(exist_ok=True)\n\nKS = [1, 2, 3, 5, 10, 20]\nPS = [0.1, 0.3, 0.5]\nN_SEEDS = 5\nN_STRATA = 5\nMIN_PER_STRATUM = 5\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE (from plan_016 with strata merging + external score support)\n# ════════════════════════════════════════════════════════════════════════════\ndef purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,\n                    external_scores_foc=None, min_per_stratum=5):\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])\n\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n\n        n_bins = len(edges) - 1\n        k_all = np.digitize(s_all, edges[1:-1])\n        strata_labels = _merge_small_strata(k_all, groups_all, n_bins, min_per_stratum)\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        x_all = np.concatenate([X_ref[:, j], X_foc[:, j]])\n\n        for k in np.unique(strata_labels):\n            mask_k = (strata_labels == k)\n            mask_ref = mask_k & (groups_all == 0)\n            mask_foc = mask_k & (groups_all == 1)\n\n            n1 = int(mask_ref.sum())\n            n0 = int(mask_foc.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(x_all[mask_ref].sum())\n            B = float(n1 - A)\n            C = float(x_all[mask_foc].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else np.inf\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets,\n                         n_strata_used=n_ok))\n\n    return pd.DataFrame(rows)\n\n\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\",\n                n_strata_used=0)\n\n\ndef _merge_small_strata(k_all, groups_all, n_bins, min_n):\n    labels = k_all.copy()\n    merged = True\n    while merged:\n        merged = False\n        unique_strata = sorted(np.unique(labels))\n        for i, k in enumerate(unique_strata):\n            mask_k = (labels == k)\n            n_ref = int((mask_k & (groups_all == 0)).sum())\n            n_foc = int((mask_k & (groups_all == 1)).sum())\n            if n_ref < min_n or n_foc < min_n:\n                if i + 1 < len(unique_strata):\n                    next_k = unique_strata[i + 1]\n                    labels[labels == next_k] = k\n                elif i > 0:\n                    prev_k = unique_strata[i - 1]\n                    labels[labels == k] = prev_k\n                merged = True\n                break\n    return labels\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\ndef load_data():\n    mat = load_npz(BASE / \"response_matrix.npz\")\n    idx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n    item2col = {iid: i for i, iid in enumerate(item_ids)}\n\n    model_meta = pd.read_csv(BASE / \"model_metadata.csv\")\n    item_meta = pd.read_csv(BASE / \"item_metadata.csv\")\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    # Temporal cohorts\n    ref_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"model_name\"]\n    foc_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"model_name\"]\n    ref_rows = np.array([name2row[n] for n in ref_names if n in name2row])\n    foc_rows = np.array([name2row[n] for n in foc_names if n in name2row])\n\n    # Focal inject subset: 2024 models in accuracy overlap with 2023\n    ref_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\n    foc_df = model_meta[model_meta[\"cohort_temporal\"] == \"2024\"]\n    t_min = max(ref_acc.min(), foc_df[\"accuracy\"].min())\n    t_max = min(ref_acc.max(), foc_df[\"accuracy\"].max())\n    foc_inject_mask = (foc_df[\"accuracy\"] >= t_min) & (foc_df[\"accuracy\"] <= t_max)\n    foc_inject_rows = np.array([name2row[n] for n in foc_df.loc[foc_inject_mask, \"model_name\"]\n                                if n in name2row])\n\n    # Build subject → column indices mapping\n    subject_cols = {}\n    subjects = sorted(item_meta[\"subject\"].unique())\n    for subj in subjects:\n        ids = item_meta.loc[item_meta[\"subject\"] == subj, \"item_id\"].values\n        cols = np.array([item2col[iid] for iid in ids if iid in item2col])\n        subject_cols[subj] = cols\n\n    return mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MAIN EXPERIMENT\n# ════════════════════════════════════════════════════════════════════════════\ndef run_experiment(ks=KS, ps=PS, n_seeds=N_SEEDS):\n    t0 = time.time()\n    mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols = load_data()\n    print(f\"Data loaded: {len(ref_rows)} ref, {len(foc_rows)} foc, \"\n          f\"{len(foc_inject_rows)} foc_inject, {len(subjects)} subjects\")\n\n    all_cols = np.concatenate([subject_cols[s] for s in subjects])\n\n    # Precompute per-subject total scores (original matrix) for ref/foc\n    # Enables O(1) matching variable via subtraction instead of re-slicing\n    subj_totals_ref = {}\n    subj_totals_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_totals_ref[subj] = np.asarray(mat[ref_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n        subj_totals_foc[subj] = np.asarray(mat[foc_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n\n    # Full total across all subjects\n    full_total_ref = sum(subj_totals_ref.values())\n    full_total_foc = sum(subj_totals_foc.values())\n\n    # Precompute dense submatrices per subject for ref/foc (avoids repeated sparse→dense)\n    subj_X_ref = {}\n    subj_X_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_X_ref[subj] = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n        subj_X_foc[subj] = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n    # ── Phase 1: baseline (p=0) per-subject FPR with cross-subject matching ──\n    print(\"Computing baseline FPR (p=0) for all subjects...\")\n    baseline_fpr = {}\n    baseline_n_c = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        cross_ref = full_total_ref - subj_totals_ref[subj]\n        cross_foc = full_total_foc - subj_totals_foc[subj]\n\n        n_strata = 3 if len(s_cols) < 100 else N_STRATA\n        dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,\n                              external_scores_ref=cross_ref,\n                              external_scores_foc=cross_foc,\n                              min_per_stratum=MIN_PER_STRATUM)\n        n_c = int((dif[\"ets_class\"] == \"C\").sum())\n        fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n        baseline_fpr[subj] = fpr\n        baseline_n_c[subj] = n_c\n\n    print(f\"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}\")\n\n    # ── Phase 2: injection runs ──\n    target_rows_list = []\n    non_target_rows_list = []\n    total_runs = len(ks) * len(ps) * n_seeds\n    run_i = 0\n\n    for k in ks:\n        for p in ps:\n            for seed in range(1, n_seeds + 1):\n                run_i += 1\n                rng = np.random.RandomState(seed)\n                target_subjects = sorted(rng.choice(subjects, size=k, replace=False))\n                non_target_subjects = [s for s in subjects if s not in target_subjects]\n\n                # Build injected matrix columns for target subjects\n                # Collect all target columns for injection\n                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])\n\n                # Inject: flip incorrect→correct for focal inject models on target items\n                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    block = mat_dense_targets[foc_inject_rows]\n                    zeros = (block == 0)\n                    flip_mask = zeros & (rng.random(block.shape) < p)\n                    n_flipped = int(flip_mask.sum())\n                    mat_dense_targets[foc_inject_rows] = block + flip_mask.astype(np.int8)\n\n                # Precompute totals for matching variable construction\n                # non_target_total = full_total - sum(target subject originals)\n                non_target_total_ref = full_total_ref - sum(subj_totals_ref[s] for s in target_subjects)\n                non_target_total_foc = full_total_foc - sum(subj_totals_foc[s] for s in target_subjects)\n\n                # Injected target total (all target subjects combined, after injection)\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                # Per-target-subject injected totals (for leave-one-out matching)\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}\n                target_subj_injected = {}\n                for s in target_subjects:\n                    local_idxs = np.array([target_col_to_local[c] for c in subject_cols[s]])\n                    target_subj_injected[s] = mat_dense_targets[:, local_idxs].sum(axis=1).astype(np.float64)\n\n                elapsed = time.time() - t0\n                print(f\"  [{run_i}/{total_runs}] k={k} p={p} seed={seed} \"\n                      f\"flipped={n_flipped} ({elapsed:.0f}s)\")\n\n                # ── DIF on each target subject ──\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    # Matching = non_target_total + other_target_injected\n                    other_target_inj = injected_target_total - target_subj_injected[subj]\n                    match_ref = non_target_total_ref + other_target_inj[ref_rows]\n                    match_foc = non_target_total_foc + other_target_inj[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    # All items in target subject are \"contaminated\" (injected)\n                    tpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_tpr = tpr - baseline_fpr[subj]  # baseline is p=0 rate\n\n                    target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, target_subject=subj,\n                        n_items=len(s_cols), tpr=tpr, fpr=np.nan,\n                        delta_tpr=delta_tpr, delta_fpr=np.nan,\n                        n_target_c=n_c, n_clean_c=np.nan\n                    ))\n\n                # ── DIF on each non-target subject (FPR measurement) ──\n                # Sample non-targets to keep runtime manageable for large k\n                # For k≤5, test all; for k>5, test 20 random non-targets\n                if len(non_target_subjects) <= 20:\n                    test_nontargets = non_target_subjects\n                else:\n                    test_nontargets = sorted(rng.choice(non_target_subjects,\n                                                        size=20, replace=False))\n\n                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n                    s_cols_set = set(s_cols.tolist())\n\n                    X_ref_s = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n                    X_foc_s = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n                    # Matching = everything except this subject\n                    # = non_target_total (minus this subject) + all injected target scores\n                    other_nontarget_cols = np.array([c for c in non_target_cols\n                                                     if c not in s_cols_set])\n                    other_nt_ref = np.asarray(mat[ref_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n                    other_nt_foc = np.asarray(mat[foc_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)\n\n                    match_ref = other_nt_ref + injected_target_total[ref_rows]\n                    match_foc = other_nt_foc + injected_target_total[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_fpr = fpr - baseline_fpr[subj]\n\n                    non_target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, non_target_subject=subj,\n                        n_items=len(s_cols),\n                        fpr=fpr, baseline_fpr=baseline_fpr[subj],\n                        delta_fpr=delta_fpr\n                    ))\n\n    # ── Save results ──\n    target_df = pd.DataFrame(target_rows_list)\n    target_df.to_csv(OUT / \"multi_subject_injection_results.csv\", index=False)\n\n    nontarget_df = pd.DataFrame(non_target_rows_list)\n    nontarget_df.to_csv(OUT / \"non_target_fpr_results.csv\", index=False)\n\n    # ── Summary by k,p ──\n    summary_rows = []\n    for k in ks:\n        for p_val in ps:\n            t_sub = target_df[(target_df[\"k\"] == k) & (target_df[\"p\"] == p_val)]\n            nt_sub = nontarget_df[(nontarget_df[\"k\"] == k) & (nontarget_df[\"p\"] == p_val)]\n\n            mean_tpr = t_sub[\"tpr\"].mean() if len(t_sub) > 0 else np.nan\n            mean_delta_tpr = t_sub[\"delta_tpr\"].mean() if len(t_sub) > 0 else np.nan\n            std_delta_tpr = t_sub.groupby(\"seed\")[\"delta_tpr\"].mean().std() if len(t_sub) > 0 else np.nan\n\n            mean_fpr_nt = nt_sub[\"fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            mean_delta_fpr_nt = nt_sub[\"delta_fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            std_delta_fpr_nt = nt_sub.groupby(\"seed\")[\"delta_fpr\"].mean().std() if len(nt_sub) > 0 else np.nan\n\n            summary_rows.append(dict(\n                k=k, p=p_val,\n                mean_tpr_target=round(mean_tpr, 4),\n                mean_delta_tpr=round(mean_delta_tpr, 4),\n                std_delta_tpr=round(std_delta_tpr, 4) if not np.isnan(std_delta_tpr) else np.nan,\n                mean_fpr_non_target=round(mean_fpr_nt, 4),\n                mean_delta_fpr_non_target=round(mean_delta_fpr_nt, 4),\n                std_delta_fpr_non_target=round(std_delta_fpr_nt, 4) if not np.isnan(std_delta_fpr_nt) else np.nan,\n            ))\n\n    summary_df = pd.DataFrame(summary_rows)\n    summary_df.to_csv(OUT / \"summary_by_k.csv\", index=False)\n\n    elapsed = time.time() - t0\n    print(f\"\\nDone in {elapsed:.0f}s. Saved to {OUT}\")\n    print(\"\\nSummary:\")\n    print(summary_df.to_string(index=False))\n\n    return target_df, nontarget_df, summary_df\n\n\ndef generate_report(target_df, nontarget_df, summary_df):\n    lines = [\n        \"# Plan 034: Multi-Subject Simultaneous Injection — Report\",\n        \"\",\n        \"## Method\",\n        \"\",\n        \"We test Proposition 1's robustness boundary by simultaneously injecting\",\n        \"differential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).\",\n        \"For each (k, p, seed) combination:\",\n        \"\",\n        \"1. Randomly select k target subjects from 57 MMLU subjects\",\n        \"2. For each item in the k target subjects, flip incorrect→correct responses\",\n        \"   in the focal group (2024 models within accuracy overlap) with probability p\",\n        \"3. Compute cross-subject MH-DIF for each target and non-target subject\",\n        \"   - Matching variable = total score on all subjects EXCEPT the tested one\",\n        \"   - For target subjects: matching includes injected scores from other targets\",\n        \"   - For non-target subjects: matching includes all injected target scores\",\n        \"4. Measure TPR on target subjects and FPR on non-target subjects\",\n        \"\",\n        f\"Grid: k ∈ {{{','.join(map(str, KS))}}}, p ∈ {{{','.join(map(str, PS))}}}, \"\n        f\"5 seeds per combination = {len(KS)*len(PS)*N_SEEDS} runs\",\n        \"\",\n        \"## Core Results: ΔFPR by k and p\",\n        \"\",\n    ]\n\n    # Summary table\n    lines.append(\"### Target Subjects (TPR)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean TPR | Mean ΔTPR | SD(ΔTPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_tpr_target']:.4f} | \"\n                      f\"{row['mean_delta_tpr']:.4f} | \"\n                      f\"{row['std_delta_tpr']:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Non-Target Subjects (FPR — key result)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean FPR | Mean ΔFPR | SD(ΔFPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_fpr_non_target']:.4f} | \"\n                      f\"{row['mean_delta_fpr_non_target']:.4f} | \"\n                      f\"{row['std_delta_fpr_non_target']:.4f} |\")\n    lines.append(\"\")\n\n    # Key findings\n    lines.append(\"## Key Findings\")\n    lines.append(\"\")\n\n    # Find threshold where ΔFPR becomes notable\n    for p_val in PS:\n        sub = summary_df[summary_df[\"p\"] == p_val]\n        significant_k = sub[sub[\"mean_delta_fpr_non_target\"].abs() > 0.01]\n        if len(significant_k) > 0:\n            first_k = int(significant_k.iloc[0][\"k\"])\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR exceeds 0.01 at k={first_k}\")\n        else:\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR stays below 0.01 for all k tested\")\n\n    lines.append(\"\")\n    lines.append(\"## Interpretation\")\n    lines.append(\"\")\n    lines.append(\"Proposition 1 guarantees ΔFPR=0 when the matching variable is uncontaminated.\")\n    lines.append(\"As k increases, more of the cross-subject total score is contaminated,\")\n    lines.append(\"violating the proposition's assumption. The k at which ΔFPR becomes\")\n    lines.append(\"practically significant marks the validity boundary of cross-subject DIF auditing.\")\n    lines.append(\"\")\n\n    report_path = OUT / \"plan_034_report.md\"\n    report_path.write_text(\"\\n\".join(lines))\n    print(f\"Report saved to {report_path}\")\n\n\nif __name__ == \"__main__\":\n    parser = argparse.ArgumentParser(description=\"Plan 034: Multi-Subject Injection\")\n    parser.add_argument(\"--quick\", action=\"store_true\",\n                        help=\"Quick validation: k∈{1,5,20}, p=0.3, seed=1\")\n    args = parser.parse_args()\n\n    if args.quick:\n        target_df, nontarget_df, summary_df = run_experiment(\n            ks=[1, 5, 20], ps=[0.3], n_seeds=1)\n    else:\n        target_df, nontarget_df, summary_df = run_experiment()\n\n    generate_report(target_df, nontarget_df, summary_df)\n",
    "structuredPatch": [
      {
        "oldStart": 368,
        "oldLines": 21,
        "newStart": 368,
        "newLines": 13,
        "lines": [
          " ",
          "                 for subj in test_nontargets:",
          "                     s_cols = subject_cols[subj]",
          "-                    s_cols_set = set(s_cols.tolist())",
          " ",
          "-                    X_ref_s = mat[ref_rows][:, s_cols].toarray().astype(np.int8)",
          "-                    X_foc_s = mat[foc_rows][:, s_cols].toarray().astype(np.int8)",
          "+                    # Matching = (non_target_total - this subject) + all injected target total",
          "+                    match_ref = (non_target_total_ref - subj_totals_ref[subj]",
          "+                                 + injected_target_total[ref_rows])",
          "+                    match_foc = (non_target_total_foc - subj_totals_foc[subj]",
          "+                                 + injected_target_total[foc_rows])",
          " ",
          "-                    # Matching = everything except this subject",
          "-                    # = non_target_total (minus this subject) + all injected target scores",
          "-                    other_nontarget_cols = np.array([c for c in non_target_cols",
          "-                                                     if c not in s_cols_set])",
          "-                    other_nt_ref = np.asarray(mat[ref_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)",
          "-                    other_nt_foc = np.asarray(mat[foc_rows][:, other_nontarget_cols].sum(axis=1)).ravel().astype(np.float64)",
          "-",
          "-                    match_ref = other_nt_ref + injected_target_total[ref_rows]",
          "-                    match_foc = other_nt_foc + injected_target_total[foc_rows]",
          "-",
          "                     n_strata = 3 if len(s_cols) < 100 else N_STRATA",
          "                     dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,",
          "                                           external_scores_ref=match_ref,"
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

### Assistant

_source line 72_

Also update the non-target loop to use precomputed dense matrices.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "e01ccbd6-22b2-40d9-9223-d87c44bd77d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YVCt5LSr7u5SceUBs6Q9Aj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 53548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 732
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

_source line 73_

<details open><summary>🔧 Tool call — Read · `toolu_01K5nV2xa6fM8mmD99xsF7ag`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
  "offset": 363,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "711343e5-95a1-4536-b826-a28ffb59d3fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YVCt5LSr7u5SceUBs6Q9Aj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 53548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 732
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

_source line 74 · 2026-05-21T15:51:47.753Z_

<details><summary>↩ Tool result · `toolu_01K5nV2xa6fM8mmD99xsF7ag`</summary>

```text
363	                if len(non_target_subjects) <= 20:
364	                    test_nontargets = non_target_subjects
365	                else:
366	                    test_nontargets = sorted(rng.choice(non_target_subjects,
367	                                                        size=20, replace=False))
368	
369	                for subj in test_nontargets:
370	                    s_cols = subject_cols[subj]
371	
372	                    # Matching = (non_target_total - this subject) + all injected target total
373	                    match_ref = (non_target_total_ref - subj_totals_ref[subj]
374	                                 + injected_target_total[ref_rows])
375	                    match_foc = (non_target_total_foc - subj_totals_foc[subj]
376	                                 + injected_target_total[foc_rows])
377	
378	                    n_strata = 3 if len(s_cols) < 100 else N_STRATA
379	                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,
380	                                          external_scores_ref=match_ref,
381	                                          external_scores_foc=match_foc,
382	                                          min_per_stratum=MIN_PER_STRATUM)
383	
384	                    n_c = int((dif["ets_class"] == "C").sum())
385	                    fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0
386	                    delta_fpr = fpr - baseline_fpr[subj]
387	
388	                    non_target_rows_list.append(dict(
389	                        k=k, p=p, seed=seed, non_target_subject=subj,
390	                        n_items=len(s_cols),
391	                        fpr=fpr, baseline_fpr=baseline_fpr[subj],
392	                        delta_fpr=delta_fpr
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "8f0a7e8b-42d4-4280-98d2-07c8c9ed2cc6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
      "content": "                if len(non_target_subjects) <= 20:\n                    test_nontargets = non_target_subjects\n                else:\n                    test_nontargets = sorted(rng.choice(non_target_subjects,\n                                                        size=20, replace=False))\n\n                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n\n                    # Matching = (non_target_total - this subject) + all injected target total\n                    match_ref = (non_target_total_ref - subj_totals_ref[subj]\n                                 + injected_target_total[ref_rows])\n                    match_foc = (non_target_total_foc - subj_totals_foc[subj]\n                                 + injected_target_total[foc_rows])\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_fpr = fpr - baseline_fpr[subj]\n\n                    non_target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, non_target_subject=subj,\n                        n_items=len(s_cols),\n                        fpr=fpr, baseline_fpr=baseline_fpr[subj],\n                        delta_fpr=delta_fpr",
      "numLines": 30,
      "startLine": 363,
      "totalLines": 526
    }
  }
}
```

</details>

---

### Assistant

_source line 75_

I see `X_ref_s` and `X_foc_s` are stale variable references from the target subject loop. Need to fix that to use precomputed dense matrices.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "6b926d6f-74cb-4395-a00b-e32e3f0dd61f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEGLKRi7b5pYAe5NeHRky9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 54280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
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

_source line 76_

<details open><summary>🔧 Tool call — Edit · `toolu_018sSxUnhNW9SKc86ysivdKJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
  "old_string": "                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n\n                    # Matching = (non_target_total - this subject) + all injected target total\n                    match_ref = (non_target_total_ref - subj_totals_ref[subj]\n                                 + injected_target_total[ref_rows])\n                    match_foc = (non_target_total_foc - subj_totals_foc[subj]\n                                 + injected_target_total[foc_rows])\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,",
  "new_string": "                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n\n                    # Matching = (non_target_total - this subject) + all injected target total\n                    match_ref = (non_target_total_ref - subj_totals_ref[subj]\n                                 + injected_target_total[ref_rows])\n                    match_foc = (non_target_total_foc - subj_totals_foc[subj]\n                                 + injected_target_total[foc_rows])\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "ecc72099-1262-4100-93e6-f2c762a93105",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEGLKRi7b5pYAe5NeHRky9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 54280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
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

_source line 77 · 2026-05-21T15:52:01.901Z_

<details><summary>↩ Tool result · `toolu_018sSxUnhNW9SKc86ysivdKJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "951dcc55-3e5b-4080-b14b-0592ce81e412",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
    "oldString": "                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n\n                    # Matching = (non_target_total - this subject) + all injected target total\n                    match_ref = (non_target_total_ref - subj_totals_ref[subj]\n                                 + injected_target_total[ref_rows])\n                    match_foc = (non_target_total_foc - subj_totals_foc[subj]\n                                 + injected_target_total[foc_rows])\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,",
    "newString": "                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n\n                    # Matching = (non_target_total - this subject) + all injected target total\n                    match_ref = (non_target_total_ref - subj_totals_ref[subj]\n                                 + injected_target_total[ref_rows])\n                    match_foc = (non_target_total_foc - subj_totals_foc[subj]\n                                 + injected_target_total[foc_rows])\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nplan_034: Multi-Subject Simultaneous Injection Experiment\n\nTests Proposition 1 (ΔFPR=0) robustness under multi-subject contamination.\nWhen k subjects are simultaneously injected, the cross-subject matching variable\n(total score on remaining 57-k uninjected subjects) degrades. ΔFPR(k) on\nnon-target subjects should increase with k, revealing the validity boundary.\n\nInputs:\n  - artifacts/response_matrix.npz         (5227 × 12508 sparse binary)\n  - artifacts/response_matrix_index.npz   (model_names, item_ids)\n  - artifacts/model_metadata.csv          (cohort_temporal, accuracy, ...)\n  - artifacts/item_metadata.csv           (item_id, subject, ...)\n\nOutputs:\n  - multi_subject_injection_results.csv   (per-target-subject DIF results)\n  - non_target_fpr_results.csv            (FPR on uninjected subjects)\n  - summary_by_k.csv                      (aggregated ΔFPR/ΔTPR by k,p)\n  - plan_034_report.md\n\nDependencies: numpy, pandas, scipy\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\nimport warnings\nimport argparse\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_034_multi_subject_injection\"\nOUT.mkdir(exist_ok=True)\n\nKS = [1, 2, 3, 5, 10, 20]\nPS = [0.1, 0.3, 0.5]\nN_SEEDS = 5\nN_STRATA = 5\nMIN_PER_STRATUM = 5\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE (from plan_016 with strata merging + external score support)\n# ════════════════════════════════════════════════════════════════════════════\ndef purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,\n                    external_scores_foc=None, min_per_stratum=5):\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])\n\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n\n        n_bins = len(edges) - 1\n        k_all = np.digitize(s_all, edges[1:-1])\n        strata_labels = _merge_small_strata(k_all, groups_all, n_bins, min_per_stratum)\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        x_all = np.concatenate([X_ref[:, j], X_foc[:, j]])\n\n        for k in np.unique(strata_labels):\n            mask_k = (strata_labels == k)\n            mask_ref = mask_k & (groups_all == 0)\n            mask_foc = mask_k & (groups_all == 1)\n\n            n1 = int(mask_ref.sum())\n            n0 = int(mask_foc.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(x_all[mask_ref].sum())\n            B = float(n1 - A)\n            C = float(x_all[mask_foc].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else np.inf\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets,\n                         n_strata_used=n_ok))\n\n    return pd.DataFrame(rows)\n\n\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\",\n                n_strata_used=0)\n\n\ndef _merge_small_strata(k_all, groups_all, n_bins, min_n):\n    labels = k_all.copy()\n    merged = True\n    while merged:\n        merged = False\n        unique_strata = sorted(np.unique(labels))\n        for i, k in enumerate(unique_strata):\n            mask_k = (labels == k)\n            n_ref = int((mask_k & (groups_all == 0)).sum())\n            n_foc = int((mask_k & (groups_all == 1)).sum())\n            if n_ref < min_n or n_foc < min_n:\n                if i + 1 < len(unique_strata):\n                    next_k = unique_strata[i + 1]\n                    labels[labels == next_k] = k\n                elif i > 0:\n                    prev_k = unique_strata[i - 1]\n                    labels[labels == k] = prev_k\n                merged = True\n                break\n    return labels\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\ndef load_data():\n    mat = load_npz(BASE / \"response_matrix.npz\")\n    idx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n    item2col = {iid: i for i, iid in enumerate(item_ids)}\n\n    model_meta = pd.read_csv(BASE / \"model_metadata.csv\")\n    item_meta = pd.read_csv(BASE / \"item_metadata.csv\")\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    # Temporal cohorts\n    ref_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"model_name\"]\n    foc_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"model_name\"]\n    ref_rows = np.array([name2row[n] for n in ref_names if n in name2row])\n    foc_rows = np.array([name2row[n] for n in foc_names if n in name2row])\n\n    # Focal inject subset: 2024 models in accuracy overlap with 2023\n    ref_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\n    foc_df = model_meta[model_meta[\"cohort_temporal\"] == \"2024\"]\n    t_min = max(ref_acc.min(), foc_df[\"accuracy\"].min())\n    t_max = min(ref_acc.max(), foc_df[\"accuracy\"].max())\n    foc_inject_mask = (foc_df[\"accuracy\"] >= t_min) & (foc_df[\"accuracy\"] <= t_max)\n    foc_inject_rows = np.array([name2row[n] for n in foc_df.loc[foc_inject_mask, \"model_name\"]\n                                if n in name2row])\n\n    # Build subject → column indices mapping\n    subject_cols = {}\n    subjects = sorted(item_meta[\"subject\"].unique())\n    for subj in subjects:\n        ids = item_meta.loc[item_meta[\"subject\"] == subj, \"item_id\"].values\n        cols = np.array([item2col[iid] for iid in ids if iid in item2col])\n        subject_cols[subj] = cols\n\n    return mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MAIN EXPERIMENT\n# ════════════════════════════════════════════════════════════════════════════\ndef run_experiment(ks=KS, ps=PS, n_seeds=N_SEEDS):\n    t0 = time.time()\n    mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols = load_data()\n    print(f\"Data loaded: {len(ref_rows)} ref, {len(foc_rows)} foc, \"\n          f\"{len(foc_inject_rows)} foc_inject, {len(subjects)} subjects\")\n\n    all_cols = np.concatenate([subject_cols[s] for s in subjects])\n\n    # Precompute per-subject total scores (original matrix) for ref/foc\n    # Enables O(1) matching variable via subtraction instead of re-slicing\n    subj_totals_ref = {}\n    subj_totals_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_totals_ref[subj] = np.asarray(mat[ref_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n        subj_totals_foc[subj] = np.asarray(mat[foc_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n\n    # Full total across all subjects\n    full_total_ref = sum(subj_totals_ref.values())\n    full_total_foc = sum(subj_totals_foc.values())\n\n    # Precompute dense submatrices per subject for ref/foc (avoids repeated sparse→dense)\n    subj_X_ref = {}\n    subj_X_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_X_ref[subj] = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n        subj_X_foc[subj] = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n    # ── Phase 1: baseline (p=0) per-subject FPR with cross-subject matching ──\n    print(\"Computing baseline FPR (p=0) for all subjects...\")\n    baseline_fpr = {}\n    baseline_n_c = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        cross_ref = full_total_ref - subj_totals_ref[subj]\n        cross_foc = full_total_foc - subj_totals_foc[subj]\n\n        n_strata = 3 if len(s_cols) < 100 else N_STRATA\n        dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,\n                              external_scores_ref=cross_ref,\n                              external_scores_foc=cross_foc,\n                              min_per_stratum=MIN_PER_STRATUM)\n        n_c = int((dif[\"ets_class\"] == \"C\").sum())\n        fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n        baseline_fpr[subj] = fpr\n        baseline_n_c[subj] = n_c\n\n    print(f\"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}\")\n\n    # ── Phase 2: injection runs ──\n    target_rows_list = []\n    non_target_rows_list = []\n    total_runs = len(ks) * len(ps) * n_seeds\n    run_i = 0\n\n    for k in ks:\n        for p in ps:\n            for seed in range(1, n_seeds + 1):\n                run_i += 1\n                rng = np.random.RandomState(seed)\n                target_subjects = sorted(rng.choice(subjects, size=k, replace=False))\n                non_target_subjects = [s for s in subjects if s not in target_subjects]\n\n                # Build injected matrix columns for target subjects\n                # Collect all target columns for injection\n                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])\n\n                # Inject: flip incorrect→correct for focal inject models on target items\n                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    block = mat_dense_targets[foc_inject_rows]\n                    zeros = (block == 0)\n                    flip_mask = zeros & (rng.random(block.shape) < p)\n                    n_flipped = int(flip_mask.sum())\n                    mat_dense_targets[foc_inject_rows] = block + flip_mask.astype(np.int8)\n\n                # Precompute totals for matching variable construction\n                # non_target_total = full_total - sum(target subject originals)\n                non_target_total_ref = full_total_ref - sum(subj_totals_ref[s] for s in target_subjects)\n                non_target_total_foc = full_total_foc - sum(subj_totals_foc[s] for s in target_subjects)\n\n                # Injected target total (all target subjects combined, after injection)\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                # Per-target-subject injected totals (for leave-one-out matching)\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}\n                target_subj_injected = {}\n                for s in target_subjects:\n                    local_idxs = np.array([target_col_to_local[c] for c in subject_cols[s]])\n                    target_subj_injected[s] = mat_dense_targets[:, local_idxs].sum(axis=1).astype(np.float64)\n\n                elapsed = time.time() - t0\n                print(f\"  [{run_i}/{total_runs}] k={k} p={p} seed={seed} \"\n                      f\"flipped={n_flipped} ({elapsed:.0f}s)\")\n\n                # ── DIF on each target subject ──\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    # Matching = non_target_total + other_target_injected\n                    other_target_inj = injected_target_total - target_subj_injected[subj]\n                    match_ref = non_target_total_ref + other_target_inj[ref_rows]\n                    match_foc = non_target_total_foc + other_target_inj[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    # All items in target subject are \"contaminated\" (injected)\n                    tpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_tpr = tpr - baseline_fpr[subj]  # baseline is p=0 rate\n\n                    target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, target_subject=subj,\n                        n_items=len(s_cols), tpr=tpr, fpr=np.nan,\n                        delta_tpr=delta_tpr, delta_fpr=np.nan,\n                        n_target_c=n_c, n_clean_c=np.nan\n                    ))\n\n                # ── DIF on each non-target subject (FPR measurement) ──\n                # Sample non-targets to keep runtime manageable for large k\n                # For k≤5, test all; for k>5, test 20 random non-targets\n                if len(non_target_subjects) <= 20:\n                    test_nontargets = non_target_subjects\n                else:\n                    test_nontargets = sorted(rng.choice(non_target_subjects,\n                                                        size=20, replace=False))\n\n                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n\n                    # Matching = (non_target_total - this subject) + all injected target total\n                    match_ref = (non_target_total_ref - subj_totals_ref[subj]\n                                 + injected_target_total[ref_rows])\n                    match_foc = (non_target_total_foc - subj_totals_foc[subj]\n                                 + injected_target_total[foc_rows])\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_fpr = fpr - baseline_fpr[subj]\n\n                    non_target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, non_target_subject=subj,\n                        n_items=len(s_cols),\n                        fpr=fpr, baseline_fpr=baseline_fpr[subj],\n                        delta_fpr=delta_fpr\n                    ))\n\n    # ── Save results ──\n    target_df = pd.DataFrame(target_rows_list)\n    target_df.to_csv(OUT / \"multi_subject_injection_results.csv\", index=False)\n\n    nontarget_df = pd.DataFrame(non_target_rows_list)\n    nontarget_df.to_csv(OUT / \"non_target_fpr_results.csv\", index=False)\n\n    # ── Summary by k,p ──\n    summary_rows = []\n    for k in ks:\n        for p_val in ps:\n            t_sub = target_df[(target_df[\"k\"] == k) & (target_df[\"p\"] == p_val)]\n            nt_sub = nontarget_df[(nontarget_df[\"k\"] == k) & (nontarget_df[\"p\"] == p_val)]\n\n            mean_tpr = t_sub[\"tpr\"].mean() if len(t_sub) > 0 else np.nan\n            mean_delta_tpr = t_sub[\"delta_tpr\"].mean() if len(t_sub) > 0 else np.nan\n            std_delta_tpr = t_sub.groupby(\"seed\")[\"delta_tpr\"].mean().std() if len(t_sub) > 0 else np.nan\n\n            mean_fpr_nt = nt_sub[\"fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            mean_delta_fpr_nt = nt_sub[\"delta_fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            std_delta_fpr_nt = nt_sub.groupby(\"seed\")[\"delta_fpr\"].mean().std() if len(nt_sub) > 0 else np.nan\n\n            summary_rows.append(dict(\n                k=k, p=p_val,\n                mean_tpr_target=round(mean_tpr, 4),\n                mean_delta_tpr=round(mean_delta_tpr, 4),\n                std_delta_tpr=round(std_delta_tpr, 4) if not np.isnan(std_delta_tpr) else np.nan,\n                mean_fpr_non_target=round(mean_fpr_nt, 4),\n                mean_delta_fpr_non_target=round(mean_delta_fpr_nt, 4),\n                std_delta_fpr_non_target=round(std_delta_fpr_nt, 4) if not np.isnan(std_delta_fpr_nt) else np.nan,\n            ))\n\n    summary_df = pd.DataFrame(summary_rows)\n    summary_df.to_csv(OUT / \"summary_by_k.csv\", index=False)\n\n    elapsed = time.time() - t0\n    print(f\"\\nDone in {elapsed:.0f}s. Saved to {OUT}\")\n    print(\"\\nSummary:\")\n    print(summary_df.to_string(index=False))\n\n    return target_df, nontarget_df, summary_df\n\n\ndef generate_report(target_df, nontarget_df, summary_df):\n    lines = [\n        \"# Plan 034: Multi-Subject Simultaneous Injection — Report\",\n        \"\",\n        \"## Method\",\n        \"\",\n        \"We test Proposition 1's robustness boundary by simultaneously injecting\",\n        \"differential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).\",\n        \"For each (k, p, seed) combination:\",\n        \"\",\n        \"1. Randomly select k target subjects from 57 MMLU subjects\",\n        \"2. For each item in the k target subjects, flip incorrect→correct responses\",\n        \"   in the focal group (2024 models within accuracy overlap) with probability p\",\n        \"3. Compute cross-subject MH-DIF for each target and non-target subject\",\n        \"   - Matching variable = total score on all subjects EXCEPT the tested one\",\n        \"   - For target subjects: matching includes injected scores from other targets\",\n        \"   - For non-target subjects: matching includes all injected target scores\",\n        \"4. Measure TPR on target subjects and FPR on non-target subjects\",\n        \"\",\n        f\"Grid: k ∈ {{{','.join(map(str, KS))}}}, p ∈ {{{','.join(map(str, PS))}}}, \"\n        f\"5 seeds per combination = {len(KS)*len(PS)*N_SEEDS} runs\",\n        \"\",\n        \"## Core Results: ΔFPR by k and p\",\n        \"\",\n    ]\n\n    # Summary table\n    lines.append(\"### Target Subjects (TPR)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean TPR | Mean ΔTPR | SD(ΔTPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_tpr_target']:.4f} | \"\n                      f\"{row['mean_delta_tpr']:.4f} | \"\n                      f\"{row['std_delta_tpr']:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Non-Target Subjects (FPR — key result)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean FPR | Mean ΔFPR | SD(ΔFPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_fpr_non_target']:.4f} | \"\n                      f\"{row['mean_delta_fpr_non_target']:.4f} | \"\n                      f\"{row['std_delta_fpr_non_target']:.4f} |\")\n    lines.append(\"\")\n\n    # Key findings\n    lines.append(\"## Key Findings\")\n    lines.append(\"\")\n\n    # Find threshold where ΔFPR becomes notable\n    for p_val in PS:\n        sub = summary_df[summary_df[\"p\"] == p_val]\n        significant_k = sub[sub[\"mean_delta_fpr_non_target\"].abs() > 0.01]\n        if len(significant_k) > 0:\n            first_k = int(significant_k.iloc[0][\"k\"])\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR exceeds 0.01 at k={first_k}\")\n        else:\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR stays below 0.01 for all k tested\")\n\n    lines.append(\"\")\n    lines.append(\"## Interpretation\")\n    lines.append(\"\")\n    lines.append(\"Proposition 1 guarantees ΔFPR=0 when the matching variable is uncontaminated.\")\n    lines.append(\"As k increases, more of the cross-subject total score is contaminated,\")\n    lines.append(\"violating the proposition's assumption. The k at which ΔFPR becomes\")\n    lines.append(\"practically significant marks the validity boundary of cross-subject DIF auditing.\")\n    lines.append(\"\")\n\n    report_path = OUT / \"plan_034_report.md\"\n    report_path.write_text(\"\\n\".join(lines))\n    print(f\"Report saved to {report_path}\")\n\n\nif __name__ == \"__main__\":\n    parser = argparse.ArgumentParser(description=\"Plan 034: Multi-Subject Injection\")\n    parser.add_argument(\"--quick\", action=\"store_true\",\n                        help=\"Quick validation: k∈{1,5,20}, p=0.3, seed=1\")\n    args = parser.parse_args()\n\n    if args.quick:\n        target_df, nontarget_df, summary_df = run_experiment(\n            ks=[1, 5, 20], ps=[0.3], n_seeds=1)\n    else:\n        target_df, nontarget_df, summary_df = run_experiment()\n\n    generate_report(target_df, nontarget_df, summary_df)\n",
    "structuredPatch": [
      {
        "oldStart": 376,
        "oldLines": 7,
        "newStart": 376,
        "newLines": 7,
        "lines": [
          "                                  + injected_target_total[foc_rows])",
          " ",
          "                     n_strata = 3 if len(s_cols) < 100 else N_STRATA",
          "-                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,",
          "+                    dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,",
          "                                           external_scores_ref=match_ref,",
          "                                           external_scores_foc=match_foc,",
          "                                           min_per_stratum=MIN_PER_STRATUM)"
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

### Assistant

_source line 78_

Now re-run the quick validation to confirm the optimized code produces consistent results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "9b52e884-8ffe-4bdd-9660-aea9bc65742e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVWB6nM6YrryYT5wxEcXHc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 55000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 697
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

_source line 79_

<details open><summary>🔧 Tool call — Bash · `toolu_01PFdzWgcetemG1TdcrtjDFH`</summary>

```json
{
  "command": "python3 artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py --quick 2>&1",
  "description": "Quick validation of optimized code",
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
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "e5a2305d-94b3-470a-be09-99fa557eac0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVWB6nM6YrryYT5wxEcXHc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 697,
      "cache_read_input_tokens": 55000,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 697
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

_source line 80_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bivvqo3tv",
  "tool_use_id": "toolu_01PFdzWgcetemG1TdcrtjDFH",
  "description": "Quick validation of optimized code",
  "task_type": "local_bash",
  "uuid": "4a874529-0b5c-474c-9a37-7da3e20ad3e9",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c"
}
```

---

### System

_source line 81_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bivvqo3tv",
  "tool_use_id": "toolu_01PFdzWgcetemG1TdcrtjDFH",
  "status": "completed",
  "output_file": "",
  "summary": "Quick validation of optimized code",
  "uuid": "181b7b8f-3ddf-4771-b2da-afcf68f069ea",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c"
}
```

---

### Tool result

_source line 82 · 2026-05-21T15:52:39.578Z_

<details><summary>↩ Tool result · `toolu_01PFdzWgcetemG1TdcrtjDFH`</summary>

```text
Data loaded: 1080 ref, 807 foc, 787 foc_inject, 57 subjects
Computing baseline FPR (p=0) for all subjects...
Baseline done. Mean FPR = 0.3136
  [1/3] k=1 p=0.3 seed=1 flipped=30159 (16s)
  [2/3] k=5 p=0.3 seed=1 flipped=77002 (19s)
  [3/3] k=20 p=0.3 seed=1 flipped=317731 (23s)

Done in 29s. Saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection

Summary:
 k   p  mean_tpr_target  mean_delta_tpr  std_delta_tpr  mean_fpr_non_target  mean_delta_fpr_non_target  std_delta_fpr_non_target
 1 0.3           0.5785          0.2066            NaN               0.3098                     0.0030                       NaN
 5 0.3           0.4523          0.1236            NaN               0.3083                    -0.0057                       NaN
20 0.3           0.3758          0.0590            NaN               0.3674                     0.0501                       NaN
Report saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "20d48097-ecb6-4a29-a6b8-a612497ca311",
  "tool_use_result": {
    "stdout": "Data loaded: 1080 ref, 807 foc, 787 foc_inject, 57 subjects\nComputing baseline FPR (p=0) for all subjects...\nBaseline done. Mean FPR = 0.3136\n  [1/3] k=1 p=0.3 seed=1 flipped=30159 (16s)\n  [2/3] k=5 p=0.3 seed=1 flipped=77002 (19s)\n  [3/3] k=20 p=0.3 seed=1 flipped=317731 (23s)\n\nDone in 29s. Saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection\n\nSummary:\n k   p  mean_tpr_target  mean_delta_tpr  std_delta_tpr  mean_fpr_non_target  mean_delta_fpr_non_target  std_delta_fpr_non_target\n 1 0.3           0.5785          0.2066            NaN               0.3098                     0.0030                       NaN\n 5 0.3           0.4523          0.1236            NaN               0.3083                    -0.0057                       NaN\n20 0.3           0.3758          0.0590            NaN               0.3674                     0.0501                       NaN\nReport saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md",
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

_source line 83_

<details><summary>Logged reasoning block</summary>

```text
The optimized code runs in 29s (vs 61s before), and produces consistent results:
- k=1: ΔFPR ≈ 0 ✓
- k=20: ΔFPR ≈ 0.05 ✓

Slight differences in n_flipped (30159 vs 30238) are expected since vectorized random differs from per-element random due to RNG state traversal order. But the statistical patterns are consistent.

Now let me estimate the full run time: 29s for 3 runs → ~870s for 90 runs ≈ 15 min. 

I need to think through the actual complexity of the full experiment more carefully. The quick run only tested 3 k values with a single seed, but the full experiment has 90 combinations total. The runtime for each iteration scales with k since larger k means more target subjects and thus more DIF calculations. For k=1, I'm testing 1 target against 20 sampled non-targets, while for k=20, I'm testing 20 targets against 20 sampled non-targets, so the per-iteration cost varies significantly.

Based on the quick run's timing of 3-4 seconds per iteration after precomputation, the full 90 runs should take roughly 5-6 minutes plus the initial 15-second baseline setup, putting the total around 7 minutes. I'll go ahead and run the full experiment now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "b1c77360-b35f-4fae-ac9c-cd084254fadc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9Gx49DmFovEqc75YsotcH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 55697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 681
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

_source line 84_

2x speedup from optimization. Results consistent. Running the full 90-run experiment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "00613e54-353d-43cf-a7e1-67f53f8cf4ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9Gx49DmFovEqc75YsotcH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 55697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 681
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

_source line 85_

<details open><summary>🔧 Tool call — Bash · `toolu_013tKVS3yWcg4ZGi4AuehHGU`</summary>

```json
{
  "command": "python3 artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py 2>&1",
  "description": "Full experiment run (90 combinations)",
  "timeout": 600000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "ed75be90-0e4c-421c-ba90-b0eec410b633",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V9Gx49DmFovEqc75YsotcH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 55697,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 681
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

### System

_source line 86_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b2mszs2qx",
  "tool_use_id": "toolu_013tKVS3yWcg4ZGi4AuehHGU",
  "description": "Full experiment run (90 combinations)",
  "task_type": "local_bash",
  "uuid": "55d1c50b-d65f-4ddb-a850-26e96f4e41ed",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c"
}
```

---

### System

_source line 87_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b2mszs2qx",
  "tool_use_id": "toolu_013tKVS3yWcg4ZGi4AuehHGU",
  "status": "completed",
  "output_file": "",
  "summary": "Full experiment run (90 combinations)",
  "uuid": "2c183c15-4f94-46e6-b823-136472393316",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c"
}
```

---

### Tool result

_source line 88 · 2026-05-21T16:00:13.873Z_

<details><summary>↩ Tool result · `toolu_013tKVS3yWcg4ZGi4AuehHGU`</summary>

```text
Data loaded: 1080 ref, 807 foc, 787 foc_inject, 57 subjects
Computing baseline FPR (p=0) for all subjects...
Baseline done. Mean FPR = 0.3136
  [1/90] k=1 p=0.1 seed=1 flipped=10037 (15s)
  [2/90] k=1 p=0.1 seed=2 flipped=7091 (19s)
  [3/90] k=1 p=0.1 seed=3 flipped=4321 (22s)
  [4/90] k=1 p=0.1 seed=4 flipped=6545 (25s)
  [5/90] k=1 p=0.1 seed=5 flipped=11181 (29s)
  [6/90] k=1 p=0.3 seed=1 flipped=30159 (34s)
  [7/90] k=1 p=0.3 seed=2 flipped=21076 (37s)
  [8/90] k=1 p=0.3 seed=3 flipped=12658 (40s)
  [9/90] k=1 p=0.3 seed=4 flipped=19606 (43s)
  [10/90] k=1 p=0.3 seed=5 flipped=33308 (47s)
  [11/90] k=1 p=0.5 seed=1 flipped=49893 (52s)
  [12/90] k=1 p=0.5 seed=2 flipped=35285 (55s)
  [13/90] k=1 p=0.5 seed=3 flipped=21164 (58s)
  [14/90] k=1 p=0.5 seed=4 flipped=32427 (62s)
  [15/90] k=1 p=0.5 seed=5 flipped=55332 (66s)
  [16/90] k=2 p=0.1 seed=1 flipped=13934 (70s)
  [17/90] k=2 p=0.1 seed=2 flipped=13932 (74s)
  [18/90] k=2 p=0.1 seed=3 flipped=14539 (79s)
  [19/90] k=2 p=0.1 seed=4 flipped=9114 (83s)
  [20/90] k=2 p=0.1 seed=5 flipped=14396 (88s)
  [21/90] k=2 p=0.3 seed=1 flipped=41502 (91s)
  [22/90] k=2 p=0.3 seed=2 flipped=41552 (95s)
  [23/90] k=2 p=0.3 seed=3 flipped=43264 (100s)
  [24/90] k=2 p=0.3 seed=4 flipped=27540 (104s)
  [25/90] k=2 p=0.3 seed=5 flipped=43013 (108s)
  [26/90] k=2 p=0.5 seed=1 flipped=68996 (112s)
  [27/90] k=2 p=0.5 seed=2 flipped=69252 (116s)
  [28/90] k=2 p=0.5 seed=3 flipped=71845 (120s)
  [29/90] k=2 p=0.5 seed=4 flipped=45747 (124s)
  [30/90] k=2 p=0.5 seed=5 flipped=71481 (129s)
  [31/90] k=3 p=0.1 seed=1 flipped=16264 (132s)
  [32/90] k=3 p=0.1 seed=2 flipped=16593 (136s)
  [33/90] k=3 p=0.1 seed=3 flipped=21833 (140s)
  [34/90] k=3 p=0.1 seed=4 flipped=10889 (144s)
  [35/90] k=3 p=0.1 seed=5 flipped=16574 (147s)
  [36/90] k=3 p=0.3 seed=1 flipped=48566 (150s)
  [37/90] k=3 p=0.3 seed=2 flipped=49079 (154s)
  [38/90] k=3 p=0.3 seed=3 flipped=65706 (158s)
  [39/90] k=3 p=0.3 seed=4 flipped=32495 (162s)
  [40/90] k=3 p=0.3 seed=5 flipped=49815 (164s)
  [41/90] k=3 p=0.5 seed=1 flipped=80604 (168s)
  [42/90] k=3 p=0.5 seed=2 flipped=81808 (172s)
  [43/90] k=3 p=0.5 seed=3 flipped=109853 (176s)
  [44/90] k=3 p=0.5 seed=4 flipped=54180 (181s)
  [45/90] k=3 p=0.5 seed=5 flipped=82890 (185s)
  [46/90] k=5 p=0.1 seed=1 flipped=25632 (189s)
  [47/90] k=5 p=0.1 seed=2 flipped=22321 (193s)
  [48/90] k=5 p=0.1 seed=3 flipped=28379 (198s)
  [49/90] k=5 p=0.1 seed=4 flipped=28682 (203s)
  [50/90] k=5 p=0.1 seed=5 flipped=33912 (206s)
  [51/90] k=5 p=0.3 seed=1 flipped=77002 (210s)
  [52/90] k=5 p=0.3 seed=2 flipped=66422 (214s)
  [53/90] k=5 p=0.3 seed=3 flipped=84741 (218s)
  [54/90] k=5 p=0.3 seed=4 flipped=86396 (222s)
  [55/90] k=5 p=0.3 seed=5 flipped=101344 (226s)
  [56/90] k=5 p=0.5 seed=1 flipped=128377 (229s)
  [57/90] k=5 p=0.5 seed=2 flipped=110893 (234s)
  [58/90] k=5 p=0.5 seed=3 flipped=141423 (238s)
  [59/90] k=5 p=0.5 seed=4 flipped=144011 (243s)
  [60/90] k=5 p=0.5 seed=5 flipped=168672 (246s)
  [61/90] k=10 p=0.1 seed=1 flipped=58624 (250s)
  [62/90] k=10 p=0.1 seed=2 flipped=52568 (255s)
  [63/90] k=10 p=0.1 seed=3 flipped=56259 (261s)
  [64/90] k=10 p=0.1 seed=4 flipped=82155 (268s)
  [65/90] k=10 p=0.1 seed=5 flipped=94651 (274s)
  [66/90] k=10 p=0.3 seed=1 flipped=176311 (280s)
  [67/90] k=10 p=0.3 seed=2 flipped=157761 (285s)
  [68/90] k=10 p=0.3 seed=3 flipped=168561 (290s)
  [69/90] k=10 p=0.3 seed=4 flipped=247609 (296s)
  [70/90] k=10 p=0.3 seed=5 flipped=284314 (303s)
  [71/90] k=10 p=0.5 seed=1 flipped=293874 (308s)
  [72/90] k=10 p=0.5 seed=2 flipped=262918 (313s)
  [73/90] k=10 p=0.5 seed=3 flipped=281548 (319s)
  [74/90] k=10 p=0.5 seed=4 flipped=413593 (325s)
  [75/90] k=10 p=0.5 seed=5 flipped=473781 (331s)
  [76/90] k=20 p=0.1 seed=1 flipped=105710 (337s)
  [77/90] k=20 p=0.1 seed=2 flipped=113561 (344s)
  [78/90] k=20 p=0.1 seed=3 flipped=108330 (351s)
  [79/90] k=20 p=0.1 seed=4 flipped=126719 (357s)
  [80/90] k=20 p=0.1 seed=5 flipped=141678 (363s)
  [81/90] k=20 p=0.3 seed=1 flipped=317731 (371s)
  [82/90] k=20 p=0.3 seed=2 flipped=340734 (378s)
  [83/90] k=20 p=0.3 seed=3 flipped=325510 (385s)
  [84/90] k=20 p=0.3 seed=4 flipped=380445 (391s)
  [85/90] k=20 p=0.3 seed=5 flipped=424687 (398s)
  [86/90] k=20 p=0.5 seed=1 flipped=529003 (405s)
  [87/90] k=20 p=0.5 seed=2 flipped=568020 (411s)
  [88/90] k=20 p=0.5 seed=3 flipped=542544 (419s)
  [89/90] k=20 p=0.5 seed=4 flipped=634317 (425s)
  [90/90] k=20 p=0.5 seed=5 flipped=708280 (432s)

Done in 439s. Saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection

Summary:
 k   p  mean_tpr_target  mean_delta_tpr  std_delta_tpr  mean_fpr_non_target  mean_delta_fpr_non_target  std_delta_fpr_non_target
 1 0.1           0.3906          0.0743         0.0531               0.3191                     0.0019                    0.0016
 1 0.3           0.5590          0.2427         0.0456               0.3192                     0.0020                    0.0012
 1 0.5           0.8340          0.5177         0.0497               0.3188                     0.0016                    0.0015
 2 0.1           0.3521          0.0383         0.0292               0.3169                     0.0031                    0.0015
 2 0.3           0.5012          0.1874         0.0493               0.3168                     0.0030                    0.0017
 2 0.5           0.8071          0.4933         0.0324               0.3152                     0.0015                    0.0019
 3 0.1           0.3305          0.0225         0.0208               0.3186                     0.0022                    0.0011
 3 0.3           0.4678          0.1598         0.0662               0.3172                     0.0007                    0.0025
 3 0.5           0.7779          0.4700         0.0934               0.3153                    -0.0011                    0.0032
 5 0.1           0.3135          0.0004         0.0230               0.3198                     0.0038                    0.0023
 5 0.3           0.4345          0.1215         0.0225               0.3157                    -0.0002                    0.0039
 5 0.5           0.7336          0.4205         0.0410               0.3224                     0.0065                    0.0066
10 0.1           0.3176          0.0086         0.0123               0.3164                     0.0012                    0.0027
10 0.3           0.4076          0.0986         0.0152               0.3406                     0.0255                    0.0115
10 0.5           0.6696          0.3606         0.0269               0.3841                     0.0690                    0.0302
20 0.1           0.3332          0.0217         0.0101               0.3223                     0.0013                    0.0039
20 0.3           0.3979          0.0864         0.0182               0.3927                     0.0717                    0.0224
20 0.5           0.6106          0.2992         0.0299               0.4883                     0.1673                    0.0294
Report saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "29431022-8f9d-4a0f-af24-31328ae6fe9b",
  "tool_use_result": {
    "stdout": "Data loaded: 1080 ref, 807 foc, 787 foc_inject, 57 subjects\nComputing baseline FPR (p=0) for all subjects...\nBaseline done. Mean FPR = 0.3136\n  [1/90] k=1 p=0.1 seed=1 flipped=10037 (15s)\n  [2/90] k=1 p=0.1 seed=2 flipped=7091 (19s)\n  [3/90] k=1 p=0.1 seed=3 flipped=4321 (22s)\n  [4/90] k=1 p=0.1 seed=4 flipped=6545 (25s)\n  [5/90] k=1 p=0.1 seed=5 flipped=11181 (29s)\n  [6/90] k=1 p=0.3 seed=1 flipped=30159 (34s)\n  [7/90] k=1 p=0.3 seed=2 flipped=21076 (37s)\n  [8/90] k=1 p=0.3 seed=3 flipped=12658 (40s)\n  [9/90] k=1 p=0.3 seed=4 flipped=19606 (43s)\n  [10/90] k=1 p=0.3 seed=5 flipped=33308 (47s)\n  [11/90] k=1 p=0.5 seed=1 flipped=49893 (52s)\n  [12/90] k=1 p=0.5 seed=2 flipped=35285 (55s)\n  [13/90] k=1 p=0.5 seed=3 flipped=21164 (58s)\n  [14/90] k=1 p=0.5 seed=4 flipped=32427 (62s)\n  [15/90] k=1 p=0.5 seed=5 flipped=55332 (66s)\n  [16/90] k=2 p=0.1 seed=1 flipped=13934 (70s)\n  [17/90] k=2 p=0.1 seed=2 flipped=13932 (74s)\n  [18/90] k=2 p=0.1 seed=3 flipped=14539 (79s)\n  [19/90] k=2 p=0.1 seed=4 flipped=9114 (83s)\n  [20/90] k=2 p=0.1 seed=5 flipped=14396 (88s)\n  [21/90] k=2 p=0.3 seed=1 flipped=41502 (91s)\n  [22/90] k=2 p=0.3 seed=2 flipped=41552 (95s)\n  [23/90] k=2 p=0.3 seed=3 flipped=43264 (100s)\n  [24/90] k=2 p=0.3 seed=4 flipped=27540 (104s)\n  [25/90] k=2 p=0.3 seed=5 flipped=43013 (108s)\n  [26/90] k=2 p=0.5 seed=1 flipped=68996 (112s)\n  [27/90] k=2 p=0.5 seed=2 flipped=69252 (116s)\n  [28/90] k=2 p=0.5 seed=3 flipped=71845 (120s)\n  [29/90] k=2 p=0.5 seed=4 flipped=45747 (124s)\n  [30/90] k=2 p=0.5 seed=5 flipped=71481 (129s)\n  [31/90] k=3 p=0.1 seed=1 flipped=16264 (132s)\n  [32/90] k=3 p=0.1 seed=2 flipped=16593 (136s)\n  [33/90] k=3 p=0.1 seed=3 flipped=21833 (140s)\n  [34/90] k=3 p=0.1 seed=4 flipped=10889 (144s)\n  [35/90] k=3 p=0.1 seed=5 flipped=16574 (147s)\n  [36/90] k=3 p=0.3 seed=1 flipped=48566 (150s)\n  [37/90] k=3 p=0.3 seed=2 flipped=49079 (154s)\n  [38/90] k=3 p=0.3 seed=3 flipped=65706 (158s)\n  [39/90] k=3 p=0.3 seed=4 flipped=32495 (162s)\n  [40/90] k=3 p=0.3 seed=5 flipped=49815 (164s)\n  [41/90] k=3 p=0.5 seed=1 flipped=80604 (168s)\n  [42/90] k=3 p=0.5 seed=2 flipped=81808 (172s)\n  [43/90] k=3 p=0.5 seed=3 flipped=109853 (176s)\n  [44/90] k=3 p=0.5 seed=4 flipped=54180 (181s)\n  [45/90] k=3 p=0.5 seed=5 flipped=82890 (185s)\n  [46/90] k=5 p=0.1 seed=1 flipped=25632 (189s)\n  [47/90] k=5 p=0.1 seed=2 flipped=22321 (193s)\n  [48/90] k=5 p=0.1 seed=3 flipped=28379 (198s)\n  [49/90] k=5 p=0.1 seed=4 flipped=28682 (203s)\n  [50/90] k=5 p=0.1 seed=5 flipped=33912 (206s)\n  [51/90] k=5 p=0.3 seed=1 flipped=77002 (210s)\n  [52/90] k=5 p=0.3 seed=2 flipped=66422 (214s)\n  [53/90] k=5 p=0.3 seed=3 flipped=84741 (218s)\n  [54/90] k=5 p=0.3 seed=4 flipped=86396 (222s)\n  [55/90] k=5 p=0.3 seed=5 flipped=101344 (226s)\n  [56/90] k=5 p=0.5 seed=1 flipped=128377 (229s)\n  [57/90] k=5 p=0.5 seed=2 flipped=110893 (234s)\n  [58/90] k=5 p=0.5 seed=3 flipped=141423 (238s)\n  [59/90] k=5 p=0.5 seed=4 flipped=144011 (243s)\n  [60/90] k=5 p=0.5 seed=5 flipped=168672 (246s)\n  [61/90] k=10 p=0.1 seed=1 flipped=58624 (250s)\n  [62/90] k=10 p=0.1 seed=2 flipped=52568 (255s)\n  [63/90] k=10 p=0.1 seed=3 flipped=56259 (261s)\n  [64/90] k=10 p=0.1 seed=4 flipped=82155 (268s)\n  [65/90] k=10 p=0.1 seed=5 flipped=94651 (274s)\n  [66/90] k=10 p=0.3 seed=1 flipped=176311 (280s)\n  [67/90] k=10 p=0.3 seed=2 flipped=157761 (285s)\n  [68/90] k=10 p=0.3 seed=3 flipped=168561 (290s)\n  [69/90] k=10 p=0.3 seed=4 flipped=247609 (296s)\n  [70/90] k=10 p=0.3 seed=5 flipped=284314 (303s)\n  [71/90] k=10 p=0.5 seed=1 flipped=293874 (308s)\n  [72/90] k=10 p=0.5 seed=2 flipped=262918 (313s)\n  [73/90] k=10 p=0.5 seed=3 flipped=281548 (319s)\n  [74/90] k=10 p=0.5 seed=4 flipped=413593 (325s)\n  [75/90] k=10 p=0.5 seed=5 flipped=473781 (331s)\n  [76/90] k=20 p=0.1 seed=1 flipped=105710 (337s)\n  [77/90] k=20 p=0.1 seed=2 flipped=113561 (344s)\n  [78/90] k=20 p=0.1 seed=3 flipped=108330 (351s)\n  [79/90] k=20 p=0.1 seed=4 flipped=126719 (357s)\n  [80/90] k=20 p=0.1 seed=5 flipped=141678 (363s)\n  [81/90] k=20 p=0.3 seed=1 flipped=317731 (371s)\n  [82/90] k=20 p=0.3 seed=2 flipped=340734 (378s)\n  [83/90] k=20 p=0.3 seed=3 flipped=325510 (385s)\n  [84/90] k=20 p=0.3 seed=4 flipped=380445 (391s)\n  [85/90] k=20 p=0.3 seed=5 flipped=424687 (398s)\n  [86/90] k=20 p=0.5 seed=1 flipped=529003 (405s)\n  [87/90] k=20 p=0.5 seed=2 flipped=568020 (411s)\n  [88/90] k=20 p=0.5 seed=3 flipped=542544 (419s)\n  [89/90] k=20 p=0.5 seed=4 flipped=634317 (425s)\n  [90/90] k=20 p=0.5 seed=5 flipped=708280 (432s)\n\nDone in 439s. Saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection\n\nSummary:\n k   p  mean_tpr_target  mean_delta_tpr  std_delta_tpr  mean_fpr_non_target  mean_delta_fpr_non_target  std_delta_fpr_non_target\n 1 0.1           0.3906          0.0743         0.0531               0.3191                     0.0019                    0.0016\n 1 0.3           0.5590          0.2427         0.0456               0.3192                     0.0020                    0.0012\n 1 0.5           0.8340          0.5177         0.0497               0.3188                     0.0016                    0.0015\n 2 0.1           0.3521          0.0383         0.0292               0.3169                     0.0031                    0.0015\n 2 0.3           0.5012          0.1874         0.0493               0.3168                     0.0030                    0.0017\n 2 0.5           0.8071          0.4933         0.0324               0.3152                     0.0015                    0.0019\n 3 0.1           0.3305          0.0225         0.0208               0.3186                     0.0022                    0.0011\n 3 0.3           0.4678          0.1598         0.0662               0.3172                     0.0007                    0.0025\n 3 0.5           0.7779          0.4700         0.0934               0.3153                    -0.0011                    0.0032\n 5 0.1           0.3135          0.0004         0.0230               0.3198                     0.0038                    0.0023\n 5 0.3           0.4345          0.1215         0.0225               0.3157                    -0.0002                    0.0039\n 5 0.5           0.7336          0.4205         0.0410               0.3224                     0.0065                    0.0066\n10 0.1           0.3176          0.0086         0.0123               0.3164                     0.0012                    0.0027\n10 0.3           0.4076          0.0986         0.0152               0.3406                     0.0255                    0.0115\n10 0.5           0.6696          0.3606         0.0269               0.3841                     0.0690                    0.0302\n20 0.1           0.3332          0.0217         0.0101               0.3223                     0.0013                    0.0039\n20 0.3           0.3979          0.0864         0.0182               0.3927                     0.0717                    0.0224\n20 0.5           0.6106          0.2992         0.0299               0.4883                     0.1673                    0.0294\nReport saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md",
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

_source line 89_

Full run complete in ~7.3 min. Let me verify the output files and check key patterns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "2a7ba2a7-b726-46b7-baf9-cc2694c3fe02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vTvWvaZzvpGBp3T8enM7z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4243,
      "cache_read_input_tokens": 56378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4243
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

_source line 90_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gs6e6rzBS5jDt964pLqfgq`</summary>

```json
{
  "command": "ls -la artifacts/plan_034_multi_subject_injection/ && echo \"---\" && wc -l artifacts/plan_034_multi_subject_injection/*.csv",
  "description": "Check output files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "bfe289fb-7819-4fd6-987c-73043a9856e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vTvWvaZzvpGBp3T8enM7z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4243,
      "cache_read_input_tokens": 56378,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4243
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

_source line 91 · 2026-05-21T16:00:19.484Z_

<details><summary>↩ Tool result · `toolu_01Gs6e6rzBS5jDt964pLqfgq`</summary>

```text
total 240
drwxr-xr-x  2 ubuntu ubuntu   4096 May 21 15:52 .
drwxr-xr-x 45 ubuntu ubuntu   4096 May 21 15:59 ..
-rw-r--r--  1 ubuntu ubuntu  47041 May 21 16:00 multi_subject_injection_results.csv
-rw-r--r--  1 ubuntu ubuntu 154109 May 21 16:00 non_target_fpr_results.csv
-rw-r--r--  1 ubuntu ubuntu  23488 May 21 15:52 plan_034_multi_subject_injection.py
-rw-r--r--  1 ubuntu ubuntu   3205 May 21 16:00 plan_034_report.md
-rw-r--r--  1 ubuntu ubuntu    983 May 21 16:00 summary_by_k.csv
---
   616 artifacts/plan_034_multi_subject_injection/multi_subject_injection_results.csv
  1801 artifacts/plan_034_multi_subject_injection/non_target_fpr_results.csv
    19 artifacts/plan_034_multi_subject_injection/summary_by_k.csv
  2436 total
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "c82e6272-5992-4c64-962a-ab32d5dbd811",
  "tool_use_result": {
    "stdout": "total 240\ndrwxr-xr-x  2 ubuntu ubuntu   4096 May 21 15:52 .\ndrwxr-xr-x 45 ubuntu ubuntu   4096 May 21 15:59 ..\n-rw-r--r--  1 ubuntu ubuntu  47041 May 21 16:00 multi_subject_injection_results.csv\n-rw-r--r--  1 ubuntu ubuntu 154109 May 21 16:00 non_target_fpr_results.csv\n-rw-r--r--  1 ubuntu ubuntu  23488 May 21 15:52 plan_034_multi_subject_injection.py\n-rw-r--r--  1 ubuntu ubuntu   3205 May 21 16:00 plan_034_report.md\n-rw-r--r--  1 ubuntu ubuntu    983 May 21 16:00 summary_by_k.csv\n---\n   616 artifacts/plan_034_multi_subject_injection/multi_subject_injection_results.csv\n  1801 artifacts/plan_034_multi_subject_injection/non_target_fpr_results.csv\n    19 artifacts/plan_034_multi_subject_injection/summary_by_k.csv\n  2436 total",
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

Now let me update the report with the actual findings, including a clearer analysis of the validity boundary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "a6bdb1cb-70d9-47f7-95fa-7ee7738f4259",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HML4wMoAXetKeiftU9rdbg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 60621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 458
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

_source line 93_

<details open><summary>🔧 Tool call — Read · `toolu_01BuLHBJZ7TSUpViEuQMUhQb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "ff8d7ed9-ae4b-44bc-8df6-0d4c3f5703bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HML4wMoAXetKeiftU9rdbg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 458,
      "cache_read_input_tokens": 60621,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 458
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

_source line 94 · 2026-05-21T16:00:23.724Z_

<details><summary>↩ Tool result · `toolu_01BuLHBJZ7TSUpViEuQMUhQb`</summary>

```text
1	# Plan 034: Multi-Subject Simultaneous Injection — Report
2	
3	## Method
4	
5	We test Proposition 1's robustness boundary by simultaneously injecting
6	differential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).
7	For each (k, p, seed) combination:
8	
9	1. Randomly select k target subjects from 57 MMLU subjects
10	2. For each item in the k target subjects, flip incorrect→correct responses
11	   in the focal group (2024 models within accuracy overlap) with probability p
12	3. Compute cross-subject MH-DIF for each target and non-target subject
13	   - Matching variable = total score on all subjects EXCEPT the tested one
14	   - For target subjects: matching includes injected scores from other targets
15	   - For non-target subjects: matching includes all injected target scores
16	4. Measure TPR on target subjects and FPR on non-target subjects
17	
18	Grid: k ∈ {1,2,3,5,10,20}, p ∈ {0.1,0.3,0.5}, 5 seeds per combination = 90 runs
19	
20	## Core Results: ΔFPR by k and p
21	
22	### Target Subjects (TPR)
23	
24	| k | p | Mean TPR | Mean ΔTPR | SD(ΔTPR) |
25	|---|---|----------|-----------|----------|
26	| 1.0 | 0.1 | 0.3906 | 0.0743 | 0.0531 |
27	| 1.0 | 0.3 | 0.5590 | 0.2427 | 0.0456 |
28	| 1.0 | 0.5 | 0.8340 | 0.5177 | 0.0497 |
29	| 2.0 | 0.1 | 0.3521 | 0.0383 | 0.0292 |
30	| 2.0 | 0.3 | 0.5012 | 0.1874 | 0.0493 |
31	| 2.0 | 0.5 | 0.8071 | 0.4933 | 0.0324 |
32	| 3.0 | 0.1 | 0.3305 | 0.0225 | 0.0208 |
33	| 3.0 | 0.3 | 0.4678 | 0.1598 | 0.0662 |
34	| 3.0 | 0.5 | 0.7779 | 0.4700 | 0.0934 |
35	| 5.0 | 0.1 | 0.3135 | 0.0004 | 0.0230 |
36	| 5.0 | 0.3 | 0.4345 | 0.1215 | 0.0225 |
37	| 5.0 | 0.5 | 0.7336 | 0.4205 | 0.0410 |
38	| 10.0 | 0.1 | 0.3176 | 0.0086 | 0.0123 |
39	| 10.0 | 0.3 | 0.4076 | 0.0986 | 0.0152 |
40	| 10.0 | 0.5 | 0.6696 | 0.3606 | 0.0269 |
41	| 20.0 | 0.1 | 0.3332 | 0.0217 | 0.0101 |
42	| 20.0 | 0.3 | 0.3979 | 0.0864 | 0.0182 |
43	| 20.0 | 0.5 | 0.6106 | 0.2992 | 0.0299 |
44	
45	### Non-Target Subjects (FPR — key result)
46	
47	| k | p | Mean FPR | Mean ΔFPR | SD(ΔFPR) |
48	|---|---|----------|-----------|----------|
49	| 1.0 | 0.1 | 0.3191 | 0.0019 | 0.0016 |
50	| 1.0 | 0.3 | 0.3192 | 0.0020 | 0.0012 |
51	| 1.0 | 0.5 | 0.3188 | 0.0016 | 0.0015 |
52	| 2.0 | 0.1 | 0.3169 | 0.0031 | 0.0015 |
53	| 2.0 | 0.3 | 0.3168 | 0.0030 | 0.0017 |
54	| 2.0 | 0.5 | 0.3152 | 0.0015 | 0.0019 |
55	| 3.0 | 0.1 | 0.3186 | 0.0022 | 0.0011 |
56	| 3.0 | 0.3 | 0.3172 | 0.0007 | 0.0025 |
57	| 3.0 | 0.5 | 0.3153 | -0.0011 | 0.0032 |
58	| 5.0 | 0.1 | 0.3198 | 0.0038 | 0.0023 |
59	| 5.0 | 0.3 | 0.3157 | -0.0002 | 0.0039 |
60	| 5.0 | 0.5 | 0.3224 | 0.0065 | 0.0066 |
61	| 10.0 | 0.1 | 0.3164 | 0.0012 | 0.0027 |
62	| 10.0 | 0.3 | 0.3406 | 0.0255 | 0.0115 |
63	| 10.0 | 0.5 | 0.3841 | 0.0690 | 0.0302 |
64	| 20.0 | 0.1 | 0.3223 | 0.0013 | 0.0039 |
65	| 20.0 | 0.3 | 0.3927 | 0.0717 | 0.0224 |
66	| 20.0 | 0.5 | 0.4883 | 0.1673 | 0.0294 |
67	
68	## Key Findings
69	
70	- **p=0.1**: Non-target ΔFPR stays below 0.01 for all k tested
71	- **p=0.3**: Non-target ΔFPR exceeds 0.01 at k=10
72	- **p=0.5**: Non-target ΔFPR exceeds 0.01 at k=10
73	
74	## Interpretation
75	
76	Proposition 1 guarantees ΔFPR=0 when the matching variable is uncontaminated.
77	As k increases, more of the cross-subject total score is contaminated,
78	violating the proposition's assumption. The k at which ΔFPR becomes
79	practically significant marks the validity boundary of cross-subject DIF auditing.
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "968745c6-8421-4dca-b1ab-8ffc3168563d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md",
      "content": "# Plan 034: Multi-Subject Simultaneous Injection — Report\n\n## Method\n\nWe test Proposition 1's robustness boundary by simultaneously injecting\ndifferential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).\nFor each (k, p, seed) combination:\n\n1. Randomly select k target subjects from 57 MMLU subjects\n2. For each item in the k target subjects, flip incorrect→correct responses\n   in the focal group (2024 models within accuracy overlap) with probability p\n3. Compute cross-subject MH-DIF for each target and non-target subject\n   - Matching variable = total score on all subjects EXCEPT the tested one\n   - For target subjects: matching includes injected scores from other targets\n   - For non-target subjects: matching includes all injected target scores\n4. Measure TPR on target subjects and FPR on non-target subjects\n\nGrid: k ∈ {1,2,3,5,10,20}, p ∈ {0.1,0.3,0.5}, 5 seeds per combination = 90 runs\n\n## Core Results: ΔFPR by k and p\n\n### Target Subjects (TPR)\n\n| k | p | Mean TPR | Mean ΔTPR | SD(ΔTPR) |\n|---|---|----------|-----------|----------|\n| 1.0 | 0.1 | 0.3906 | 0.0743 | 0.0531 |\n| 1.0 | 0.3 | 0.5590 | 0.2427 | 0.0456 |\n| 1.0 | 0.5 | 0.8340 | 0.5177 | 0.0497 |\n| 2.0 | 0.1 | 0.3521 | 0.0383 | 0.0292 |\n| 2.0 | 0.3 | 0.5012 | 0.1874 | 0.0493 |\n| 2.0 | 0.5 | 0.8071 | 0.4933 | 0.0324 |\n| 3.0 | 0.1 | 0.3305 | 0.0225 | 0.0208 |\n| 3.0 | 0.3 | 0.4678 | 0.1598 | 0.0662 |\n| 3.0 | 0.5 | 0.7779 | 0.4700 | 0.0934 |\n| 5.0 | 0.1 | 0.3135 | 0.0004 | 0.0230 |\n| 5.0 | 0.3 | 0.4345 | 0.1215 | 0.0225 |\n| 5.0 | 0.5 | 0.7336 | 0.4205 | 0.0410 |\n| 10.0 | 0.1 | 0.3176 | 0.0086 | 0.0123 |\n| 10.0 | 0.3 | 0.4076 | 0.0986 | 0.0152 |\n| 10.0 | 0.5 | 0.6696 | 0.3606 | 0.0269 |\n| 20.0 | 0.1 | 0.3332 | 0.0217 | 0.0101 |\n| 20.0 | 0.3 | 0.3979 | 0.0864 | 0.0182 |\n| 20.0 | 0.5 | 0.6106 | 0.2992 | 0.0299 |\n\n### Non-Target Subjects (FPR — key result)\n\n| k | p | Mean FPR | Mean ΔFPR | SD(ΔFPR) |\n|---|---|----------|-----------|----------|\n| 1.0 | 0.1 | 0.3191 | 0.0019 | 0.0016 |\n| 1.0 | 0.3 | 0.3192 | 0.0020 | 0.0012 |\n| 1.0 | 0.5 | 0.3188 | 0.0016 | 0.0015 |\n| 2.0 | 0.1 | 0.3169 | 0.0031 | 0.0015 |\n| 2.0 | 0.3 | 0.3168 | 0.0030 | 0.0017 |\n| 2.0 | 0.5 | 0.3152 | 0.0015 | 0.0019 |\n| 3.0 | 0.1 | 0.3186 | 0.0022 | 0.0011 |\n| 3.0 | 0.3 | 0.3172 | 0.0007 | 0.0025 |\n| 3.0 | 0.5 | 0.3153 | -0.0011 | 0.0032 |\n| 5.0 | 0.1 | 0.3198 | 0.0038 | 0.0023 |\n| 5.0 | 0.3 | 0.3157 | -0.0002 | 0.0039 |\n| 5.0 | 0.5 | 0.3224 | 0.0065 | 0.0066 |\n| 10.0 | 0.1 | 0.3164 | 0.0012 | 0.0027 |\n| 10.0 | 0.3 | 0.3406 | 0.0255 | 0.0115 |\n| 10.0 | 0.5 | 0.3841 | 0.0690 | 0.0302 |\n| 20.0 | 0.1 | 0.3223 | 0.0013 | 0.0039 |\n| 20.0 | 0.3 | 0.3927 | 0.0717 | 0.0224 |\n| 20.0 | 0.5 | 0.4883 | 0.1673 | 0.0294 |\n\n## Key Findings\n\n- **p=0.1**: Non-target ΔFPR stays below 0.01 for all k tested\n- **p=0.3**: Non-target ΔFPR exceeds 0.01 at k=10\n- **p=0.5**: Non-target ΔFPR exceeds 0.01 at k=10\n\n## Interpretation\n\nProposition 1 guarantees ΔFPR=0 when the matching variable is uncontaminated.\nAs k increases, more of the cross-subject total score is contaminated,\nviolating the proposition's assumption. The k at which ΔFPR becomes\npractically significant marks the validity boundary of cross-subject DIF auditing.\n",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 80
    }
  }
}
```

</details>

---

### Assistant

_source line 95_

The auto-generated report captures the findings but needs a richer analysis. Let me rewrite it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "2088f945-915a-43fa-a498-baaadf0a5627",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrmoGEiMrix9Kgugn1oSVe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2108,
      "cache_read_input_tokens": 61079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2108
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

_source line 96_

<details open><summary>🔧 Tool call — Write · `toolu_01EsxMZPSTcZsmADYJGZQqAZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md",
  "content": "# Plan 034: Multi-Subject Simultaneous Injection — Report\n\n## Method\n\nWe test Proposition 1's robustness boundary by simultaneously injecting\ndifferential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).\nFor each (k, p, seed) combination:\n\n1. Randomly select k target subjects from 57 MMLU subjects\n2. For each item in the k target subjects, flip incorrect→correct responses\n   in the focal group (2024 models within accuracy overlap) with probability p\n3. Compute cross-subject MH-DIF for each target and non-target subject\n   - Matching variable = total score on all subjects EXCEPT the tested one\n   - For target subjects: matching includes injected scores from other targets\n   - For non-target subjects: matching includes all injected target scores\n4. Measure TPR on target subjects and FPR on non-target subjects\n\nGrid: k ∈ {1,2,3,5,10,20}, p ∈ {0.1,0.3,0.5}, 5 seeds per combination = 90 runs.\nCohorts: reference = 2023 models (n=1080), focal = 2024 models (n=807),\nfocal inject subset = 787 models (within accuracy overlap).\n\n## Core Results\n\n### Non-Target Subjects (FPR — key result)\n\n| k | p=0.1 ΔFPR | p=0.3 ΔFPR | p=0.5 ΔFPR |\n|---|-----------|-----------|-----------|\n| 1  | +0.002 ± 0.002 | +0.002 ± 0.001 | +0.002 ± 0.002 |\n| 2  | +0.003 ± 0.002 | +0.003 ± 0.002 | +0.002 ± 0.002 |\n| 3  | +0.002 ± 0.001 | +0.001 ± 0.003 | −0.001 ± 0.003 |\n| 5  | +0.004 ± 0.002 | −0.000 ± 0.004 | +0.007 ± 0.007 |\n| 10 | +0.001 ± 0.003 | **+0.026 ± 0.012** | **+0.069 ± 0.030** |\n| 20 | +0.001 ± 0.004 | **+0.072 ± 0.022** | **+0.167 ± 0.029** |\n\n### Target Subjects (TPR)\n\n| k | p=0.1 TPR | p=0.3 TPR | p=0.5 TPR |\n|---|----------|----------|----------|\n| 1  | 0.391 | 0.559 | 0.834 |\n| 2  | 0.352 | 0.501 | 0.807 |\n| 3  | 0.331 | 0.468 | 0.778 |\n| 5  | 0.314 | 0.435 | 0.734 |\n| 10 | 0.318 | 0.408 | 0.670 |\n| 20 | 0.333 | 0.398 | 0.611 |\n\n## Key Findings\n\n### 1. Proposition 1 validity boundary: k ≈ 5–10\n\n- **k ≤ 5** (≤ 8.8% of subjects contaminated): Non-target ΔFPR remains within\n  noise (|ΔFPR| < 0.007) across all p values. Proposition 1 holds practically.\n\n- **k = 10** (17.5% of subjects): ΔFPR becomes significant at p ≥ 0.3.\n  At p=0.3, ΔFPR = +0.026; at p=0.5, ΔFPR = +0.069. The matching variable\n  is ~17.5% contaminated and MH stratification breaks down.\n\n- **k = 20** (35.1% of subjects): ΔFPR is large and clearly significant.\n  At p=0.3, ΔFPR = +0.072; at p=0.5, ΔFPR = +0.167 (absolute FPR rises\n  from 0.31 to 0.49). Cross-subject DIF auditing is no longer reliable.\n\n### 2. Injection intensity (p) matters only at high k\n\nAt k ≤ 5, ΔFPR is near-zero regardless of p (even p=0.5). The contamination\nfraction of the matching variable is too small to distort stratification.\nAt k ≥ 10, p amplifies the effect: higher p means more flips per subject,\nproducing larger ability shifts that degrade the matching variable further.\n\n### 3. TPR dilution with increasing k\n\nTarget-subject TPR decreases as k grows (e.g., p=0.5: 0.834 → 0.611).\nThis is expected: the matching variable for each target includes OTHER\ninjected target subjects, partially absorbing the DIF signal into the\nstratification variable and reducing detection power.\n\n### 4. Low injection intensity (p=0.1) is robust across all k\n\nEven at k=20, p=0.1 produces ΔFPR ≈ +0.001. When each item has only 10%\nflip probability, the total score shift per model is too small to\nmeaningfully contaminate the matching variable.\n\n## Interpretation for Paper\n\n**Practical implication**: Cross-subject MH-DIF auditing remains valid under\nsimultaneous contamination of up to ~9% of the test (5/57 subjects). This\nprovides a safety margin for real-world benchmark contamination scenarios,\nwhere contamination typically affects a small subset of subjects.\n\n**Theoretical note**: The validity boundary depends on the product k × p —\nthe total contamination load on the matching variable. At k=10, p=0.3, the\nmatching variable has ~17.5% contaminated subjects with moderate injection,\nwhich crosses the threshold. The boundary can be approximately characterized\nas: cross-subject DIF auditing remains reliable when the contaminated fraction\nof the matching variable stays below ~10%.\n\n**For the paper's Proposition 1 discussion**: These results support stating\nthat Proposition 1's ΔFPR=0 guarantee degrades gracefully — it holds in\npractice for isolated or small-scale contamination (the realistic scenario)\nand only breaks under heavy multi-subject contamination (≥10 subjects at p≥0.3).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "75f316b2-b2d1-40f9-8b4e-c3365b31753c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrmoGEiMrix9Kgugn1oSVe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2108,
      "cache_read_input_tokens": 61079,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2108
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

_source line 97 · 2026-05-21T16:01:02.100Z_

<details><summary>↩ Tool result · `toolu_01EsxMZPSTcZsmADYJGZQqAZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "3a15e4f8-5db5-47cf-a1b1-e7dc7a15d9da",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md",
    "content": "# Plan 034: Multi-Subject Simultaneous Injection — Report\n\n## Method\n\nWe test Proposition 1's robustness boundary by simultaneously injecting\ndifferential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).\nFor each (k, p, seed) combination:\n\n1. Randomly select k target subjects from 57 MMLU subjects\n2. For each item in the k target subjects, flip incorrect→correct responses\n   in the focal group (2024 models within accuracy overlap) with probability p\n3. Compute cross-subject MH-DIF for each target and non-target subject\n   - Matching variable = total score on all subjects EXCEPT the tested one\n   - For target subjects: matching includes injected scores from other targets\n   - For non-target subjects: matching includes all injected target scores\n4. Measure TPR on target subjects and FPR on non-target subjects\n\nGrid: k ∈ {1,2,3,5,10,20}, p ∈ {0.1,0.3,0.5}, 5 seeds per combination = 90 runs.\nCohorts: reference = 2023 models (n=1080), focal = 2024 models (n=807),\nfocal inject subset = 787 models (within accuracy overlap).\n\n## Core Results\n\n### Non-Target Subjects (FPR — key result)\n\n| k | p=0.1 ΔFPR | p=0.3 ΔFPR | p=0.5 ΔFPR |\n|---|-----------|-----------|-----------|\n| 1  | +0.002 ± 0.002 | +0.002 ± 0.001 | +0.002 ± 0.002 |\n| 2  | +0.003 ± 0.002 | +0.003 ± 0.002 | +0.002 ± 0.002 |\n| 3  | +0.002 ± 0.001 | +0.001 ± 0.003 | −0.001 ± 0.003 |\n| 5  | +0.004 ± 0.002 | −0.000 ± 0.004 | +0.007 ± 0.007 |\n| 10 | +0.001 ± 0.003 | **+0.026 ± 0.012** | **+0.069 ± 0.030** |\n| 20 | +0.001 ± 0.004 | **+0.072 ± 0.022** | **+0.167 ± 0.029** |\n\n### Target Subjects (TPR)\n\n| k | p=0.1 TPR | p=0.3 TPR | p=0.5 TPR |\n|---|----------|----------|----------|\n| 1  | 0.391 | 0.559 | 0.834 |\n| 2  | 0.352 | 0.501 | 0.807 |\n| 3  | 0.331 | 0.468 | 0.778 |\n| 5  | 0.314 | 0.435 | 0.734 |\n| 10 | 0.318 | 0.408 | 0.670 |\n| 20 | 0.333 | 0.398 | 0.611 |\n\n## Key Findings\n\n### 1. Proposition 1 validity boundary: k ≈ 5–10\n\n- **k ≤ 5** (≤ 8.8% of subjects contaminated): Non-target ΔFPR remains within\n  noise (|ΔFPR| < 0.007) across all p values. Proposition 1 holds practically.\n\n- **k = 10** (17.5% of subjects): ΔFPR becomes significant at p ≥ 0.3.\n  At p=0.3, ΔFPR = +0.026; at p=0.5, ΔFPR = +0.069. The matching variable\n  is ~17.5% contaminated and MH stratification breaks down.\n\n- **k = 20** (35.1% of subjects): ΔFPR is large and clearly significant.\n  At p=0.3, ΔFPR = +0.072; at p=0.5, ΔFPR = +0.167 (absolute FPR rises\n  from 0.31 to 0.49). Cross-subject DIF auditing is no longer reliable.\n\n### 2. Injection intensity (p) matters only at high k\n\nAt k ≤ 5, ΔFPR is near-zero regardless of p (even p=0.5). The contamination\nfraction of the matching variable is too small to distort stratification.\nAt k ≥ 10, p amplifies the effect: higher p means more flips per subject,\nproducing larger ability shifts that degrade the matching variable further.\n\n### 3. TPR dilution with increasing k\n\nTarget-subject TPR decreases as k grows (e.g., p=0.5: 0.834 → 0.611).\nThis is expected: the matching variable for each target includes OTHER\ninjected target subjects, partially absorbing the DIF signal into the\nstratification variable and reducing detection power.\n\n### 4. Low injection intensity (p=0.1) is robust across all k\n\nEven at k=20, p=0.1 produces ΔFPR ≈ +0.001. When each item has only 10%\nflip probability, the total score shift per model is too small to\nmeaningfully contaminate the matching variable.\n\n## Interpretation for Paper\n\n**Practical implication**: Cross-subject MH-DIF auditing remains valid under\nsimultaneous contamination of up to ~9% of the test (5/57 subjects). This\nprovides a safety margin for real-world benchmark contamination scenarios,\nwhere contamination typically affects a small subset of subjects.\n\n**Theoretical note**: The validity boundary depends on the product k × p —\nthe total contamination load on the matching variable. At k=10, p=0.3, the\nmatching variable has ~17.5% contaminated subjects with moderate injection,\nwhich crosses the threshold. The boundary can be approximately characterized\nas: cross-subject DIF auditing remains reliable when the contaminated fraction\nof the matching variable stays below ~10%.\n\n**For the paper's Proposition 1 discussion**: These results support stating\nthat Proposition 1's ΔFPR=0 guarantee degrades gracefully — it holds in\npractice for isolated or small-scale contamination (the realistic scenario)\nand only breaks under heavy multi-subject contamination (≥10 subjects at p≥0.3).\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 65,
        "newStart": 15,
        "newLines": 84,
        "lines": [
          "    - For non-target subjects: matching includes all injected target scores",
          " 4. Measure TPR on target subjects and FPR on non-target subjects",
          " ",
          "-Grid: k ∈ {1,2,3,5,10,20}, p ∈ {0.1,0.3,0.5}, 5 seeds per combination = 90 runs",
          "+Grid: k ∈ {1,2,3,5,10,20}, p ∈ {0.1,0.3,0.5}, 5 seeds per combination = 90 runs.",
          "+Cohorts: reference = 2023 models (n=1080), focal = 2024 models (n=807),",
          "+focal inject subset = 787 models (within accuracy overlap).",
          " ",
          "-## Core Results: ΔFPR by k and p",
          "+## Core Results",
          " ",
          "-### Target Subjects (TPR)",
          "+### Non-Target Subjects (FPR — key result)",
          " ",
          "-| k | p | Mean TPR | Mean ΔTPR | SD(ΔTPR) |",
          "-|---|---|----------|-----------|----------|",
          "-| 1.0 | 0.1 | 0.3906 | 0.0743 | 0.0531 |",
          "-| 1.0 | 0.3 | 0.5590 | 0.2427 | 0.0456 |",
          "-| 1.0 | 0.5 | 0.8340 | 0.5177 | 0.0497 |",
          "-| 2.0 | 0.1 | 0.3521 | 0.0383 | 0.0292 |",
          "-| 2.0 | 0.3 | 0.5012 | 0.1874 | 0.0493 |",
          "-| 2.0 | 0.5 | 0.8071 | 0.4933 | 0.0324 |",
          "-| 3.0 | 0.1 | 0.3305 | 0.0225 | 0.0208 |",
          "-| 3.0 | 0.3 | 0.4678 | 0.1598 | 0.0662 |",
          "-| 3.0 | 0.5 | 0.7779 | 0.4700 | 0.0934 |",
          "-| 5.0 | 0.1 | 0.3135 | 0.0004 | 0.0230 |",
          "-| 5.0 | 0.3 | 0.4345 | 0.1215 | 0.0225 |",
          "-| 5.0 | 0.5 | 0.7336 | 0.4205 | 0.0410 |",
          "-| 10.0 | 0.1 | 0.3176 | 0.0086 | 0.0123 |",
          "-| 10.0 | 0.3 | 0.4076 | 0.0986 | 0.0152 |",
          "-| 10.0 | 0.5 | 0.6696 | 0.3606 | 0.0269 |",
          "-| 20.0 | 0.1 | 0.3332 | 0.0217 | 0.0101 |",
          "-| 20.0 | 0.3 | 0.3979 | 0.0864 | 0.0182 |",
          "-| 20.0 | 0.5 | 0.6106 | 0.2992 | 0.0299 |",
          "+| k | p=0.1 ΔFPR | p=0.3 ΔFPR | p=0.5 ΔFPR |",
          "+|---|-----------|-----------|-----------|",
          "+| 1  | +0.002 ± 0.002 | +0.002 ± 0.001 | +0.002 ± 0.002 |",
          "+| 2  | +0.003 ± 0.002 | +0.003 ± 0.002 | +0.002 ± 0.002 |",
          "+| 3  | +0.002 ± 0.001 | +0.001 ± 0.003 | −0.001 ± 0.003 |",
          "+| 5  | +0.004 ± 0.002 | −0.000 ± 0.004 | +0.007 ± 0.007 |",
          "+| 10 | +0.001 ± 0.003 | **+0.026 ± 0.012** | **+0.069 ± 0.030** |",
          "+| 20 | +0.001 ± 0.004 | **+0.072 ± 0.022** | **+0.167 ± 0.029** |",
          " ",
          "-### Non-Target Subjects (FPR — key result)",
          "+### Target Subjects (TPR)",
          " ",
          "-| k | p | Mean FPR | Mean ΔFPR | SD(ΔFPR) |",
          "-|---|---|----------|-----------|----------|",
          "-| 1.0 | 0.1 | 0.3191 | 0.0019 | 0.0016 |",
          "-| 1.0 | 0.3 | 0.3192 | 0.0020 | 0.0012 |",
          "-| 1.0 | 0.5 | 0.3188 | 0.0016 | 0.0015 |",
          "-| 2.0 | 0.1 | 0.3169 | 0.0031 | 0.0015 |",
          "-| 2.0 | 0.3 | 0.3168 | 0.0030 | 0.0017 |",
          "-| 2.0 | 0.5 | 0.3152 | 0.0015 | 0.0019 |",
          "-| 3.0 | 0.1 | 0.3186 | 0.0022 | 0.0011 |",
          "-| 3.0 | 0.3 | 0.3172 | 0.0007 | 0.0025 |",
          "-| 3.0 | 0.5 | 0.3153 | -0.0011 | 0.0032 |",
          "-| 5.0 | 0.1 | 0.3198 | 0.0038 | 0.0023 |",
          "-| 5.0 | 0.3 | 0.3157 | -0.0002 | 0.0039 |",
          "-| 5.0 | 0.5 | 0.3224 | 0.0065 | 0.0066 |",
          "-| 10.0 | 0.1 | 0.3164 | 0.0012 | 0.0027 |",
          "-| 10.0 | 0.3 | 0.3406 | 0.0255 | 0.0115 |",
          "-| 10.0 | 0.5 | 0.3841 | 0.0690 | 0.0302 |",
          "-| 20.0 | 0.1 | 0.3223 | 0.0013 | 0.0039 |",
          "-| 20.0 | 0.3 | 0.3927 | 0.0717 | 0.0224 |",
          "-| 20.0 | 0.5 | 0.4883 | 0.1673 | 0.0294 |",
          "+| k | p=0.1 TPR | p=0.3 TPR | p=0.5 TPR |",
          "+|---|----------|----------|----------|",
          "+| 1  | 0.391 | 0.559 | 0.834 |",
          "+| 2  | 0.352 | 0.501 | 0.807 |",
          "+| 3  | 0.331 | 0.468 | 0.778 |",
          "+| 5  | 0.314 | 0.435 | 0.734 |",
          "+| 10 | 0.318 | 0.408 | 0.670 |",
          "+| 20 | 0.333 | 0.398 | 0.611 |",
          " ",
          " ## Key Findings",
          " ",
          "-- **p=0.1**: Non-target ΔFPR stays below 0.01 for all k tested",
          "-- **p=0.3**: Non-target ΔFPR exceeds 0.01 at k=10",
          "-- **p=0.5**: Non-target ΔFPR exceeds 0.01 at k=10",
          "+### 1. Proposition 1 validity boundary: k ≈ 5–10",
          " ",
          "-## Interpretation",
          "+- **k ≤ 5** (≤ 8.8% of subjects contaminated): Non-target ΔFPR remains within",
          "+  noise (|ΔFPR| < 0.007) across all p values. Proposition 1 holds practically.",
          " ",
          "-Proposition 1 guarantees ΔFPR=0 when the matching variable is uncontaminated.",
          "-As k increases, more of the cross-subject total score is contaminated,",
          "-violating the proposition's assumption. The k at which ΔFPR becomes",
          "-practically significant marks the validity boundary of cross-subject DIF auditing.",
          "+- **k = 10** (17.5% of subjects): ΔFPR becomes significant at p ≥ 0.3.",
          "+  At p=0.3, ΔFPR = +0.026; at p=0.5, ΔFPR = +0.069. The matching variable",
          "+  is ~17.5% contaminated and MH stratification breaks down.",
          "+",
          "+- **k = 20** (35.1% of subjects): ΔFPR is large and clearly significant.",
          "+  At p=0.3, ΔFPR = +0.072; at p=0.5, ΔFPR = +0.167 (absolute FPR rises",
          "+  from 0.31 to 0.49). Cross-subject DIF auditing is no longer reliable.",
          "+",
          "+### 2. Injection intensity (p) matters only at high k",
          "+",
          "+At k ≤ 5, ΔFPR is near-zero regardless of p (even p=0.5). The contamination",
          "+fraction of the matching variable is too small to distort stratification.",
          "+At k ≥ 10, p amplifies the effect: higher p means more flips per subject,",
          "+producing larger ability shifts that degrade the matching variable further.",
          "+",
          "+### 3. TPR dilution with increasing k",
          "+",
          "+Target-subject TPR decreases as k grows (e.g., p=0.5: 0.834 → 0.611).",
          "+This is expected: the matching variable for each target includes OTHER",
          "+injected target subjects, partially absorbing the DIF signal into the",
          "+stratification variable and reducing detection power.",
          "+",
          "+### 4. Low injection intensity (p=0.1) is robust across all k",
          "+",
          "+Even at k=20, p=0.1 produces ΔFPR ≈ +0.001. When each item has only 10%",
          "+flip probability, the total score shift per model is too small to",
          "+meaningfully contaminate the matching variable.",
          "+",
          "+## Interpretation for Paper",
          "+",
          "+**Practical implication**: Cross-subject MH-DIF auditing remains valid under",
          "+simultaneous contamination of up to ~9% of the test (5/57 subjects). This",
          "+provides a safety margin for real-world benchmark contamination scenarios,",
          "+where contamination typically affects a small subset of subjects.",
          "+",
          "+**Theoretical note**: The validity boundary depends on the product k × p —",
          "+the total contamination load on the matching variable. At k=10, p=0.3, the",
          "+matching variable has ~17.5% contaminated subjects with moderate injection,",
          "+which crosses the threshold. The boundary can be approximately characterized",
          "+as: cross-subject DIF auditing remains reliable when the contaminated fraction",
          "+of the matching variable stays below ~10%.",
          "+",
          "+**For the paper's Proposition 1 discussion**: These results support stating",
          "+that Proposition 1's ΔFPR=0 guarantee degrades gracefully — it holds in",
          "+practice for isolated or small-scale contamination (the realistic scenario)",
          "+and only breaks under heavy multi-subject contamination (≥10 subjects at p≥0.3)."
        ]
      }
    ],
    "originalFile": "# Plan 034: Multi-Subject Simultaneous Injection — Report\n\n## Method\n\nWe test Proposition 1's robustness boundary by simultaneously injecting\ndifferential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).\nFor each (k, p, seed) combination:\n\n1. Randomly select k target subjects from 57 MMLU subjects\n2. For each item in the k target subjects, flip incorrect→correct responses\n   in the focal group (2024 models within accuracy overlap) with probability p\n3. Compute cross-subject MH-DIF for each target and non-target subject\n   - Matching variable = total score on all subjects EXCEPT the tested one\n   - For target subjects: matching includes injected scores from other targets\n   - For non-target subjects: matching includes all injected target scores\n4. Measure TPR on target subjects and FPR on non-target subjects\n\nGrid: k ∈ {1,2,3,5,10,20}, p ∈ {0.1,0.3,0.5}, 5 seeds per combination = 90 runs\n\n## Core Results: ΔFPR by k and p\n\n### Target Subjects (TPR)\n\n| k | p | Mean TPR | Mean ΔTPR | SD(ΔTPR) |\n|---|---|----------|-----------|----------|\n| 1.0 | 0.1 | 0.3906 | 0.0743 | 0.0531 |\n| 1.0 | 0.3 | 0.5590 | 0.2427 | 0.0456 |\n| 1.0 | 0.5 | 0.8340 | 0.5177 | 0.0497 |\n| 2.0 | 0.1 | 0.3521 | 0.0383 | 0.0292 |\n| 2.0 | 0.3 | 0.5012 | 0.1874 | 0.0493 |\n| 2.0 | 0.5 | 0.8071 | 0.4933 | 0.0324 |\n| 3.0 | 0.1 | 0.3305 | 0.0225 | 0.0208 |\n| 3.0 | 0.3 | 0.4678 | 0.1598 | 0.0662 |\n| 3.0 | 0.5 | 0.7779 | 0.4700 | 0.0934 |\n| 5.0 | 0.1 | 0.3135 | 0.0004 | 0.0230 |\n| 5.0 | 0.3 | 0.4345 | 0.1215 | 0.0225 |\n| 5.0 | 0.5 | 0.7336 | 0.4205 | 0.0410 |\n| 10.0 | 0.1 | 0.3176 | 0.0086 | 0.0123 |\n| 10.0 | 0.3 | 0.4076 | 0.0986 | 0.0152 |\n| 10.0 | 0.5 | 0.6696 | 0.3606 | 0.0269 |\n| 20.0 | 0.1 | 0.3332 | 0.0217 | 0.0101 |\n| 20.0 | 0.3 | 0.3979 | 0.0864 | 0.0182 |\n| 20.0 | 0.5 | 0.6106 | 0.2992 | 0.0299 |\n\n### Non-Target Subjects (FPR — key result)\n\n| k | p | Mean FPR | Mean ΔFPR | SD(ΔFPR) |\n|---|---|----------|-----------|----------|\n| 1.0 | 0.1 | 0.3191 | 0.0019 | 0.0016 |\n| 1.0 | 0.3 | 0.3192 | 0.0020 | 0.0012 |\n| 1.0 | 0.5 | 0.3188 | 0.0016 | 0.0015 |\n| 2.0 | 0.1 | 0.3169 | 0.0031 | 0.0015 |\n| 2.0 | 0.3 | 0.3168 | 0.0030 | 0.0017 |\n| 2.0 | 0.5 | 0.3152 | 0.0015 | 0.0019 |\n| 3.0 | 0.1 | 0.3186 | 0.0022 | 0.0011 |\n| 3.0 | 0.3 | 0.3172 | 0.0007 | 0.0025 |\n| 3.0 | 0.5 | 0.3153 | -0.0011 | 0.0032 |\n| 5.0 | 0.1 | 0.3198 | 0.0038 | 0.0023 |\n| 5.0 | 0.3 | 0.3157 | -0.0002 | 0.0039 |\n| 5.0 | 0.5 | 0.3224 | 0.0065 | 0.0066 |\n| 10.0 | 0.1 | 0.3164 | 0.0012 | 0.0027 |\n| 10.0 | 0.3 | 0.3406 | 0.0255 | 0.0115 |\n| 10.0 | 0.5 | 0.3841 | 0.0690 | 0.0302 |\n| 20.0 | 0.1 | 0.3223 | 0.0013 | 0.0039 |\n| 20.0 | 0.3 | 0.3927 | 0.0717 | 0.0224 |\n| 20.0 | 0.5 | 0.4883 | 0.1673 | 0.0294 |\n\n## Key Findings\n\n- **p=0.1**: Non-target ΔFPR stays below 0.01 for all k tested\n- **p=0.3**: Non-target ΔFPR exceeds 0.01 at k=10\n- **p=0.5**: Non-target ΔFPR exceeds 0.01 at k=10\n\n## Interpretation\n\nProposition 1 guarantees ΔFPR=0 when the matching variable is uncontaminated.\nAs k increases, more of the cross-subject total score is contaminated,\nviolating the proposition's assumption. The k at which ΔFPR becomes\npractically significant marks the validity boundary of cross-subject DIF auditing.\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 98_

Now register the artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "93bfd7a4-c522-4855-ba04-2f3b2646257c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GnU9SEhnBK8CXgEdeToe2N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1839,
      "cache_read_input_tokens": 63187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1839
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

_source line 99_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EJZ21BQ4YCWo7LgYzneFwL`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "cb0567a7-da3f-4429-b94a-7a7c9baecf75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GnU9SEhnBK8CXgEdeToe2N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1839,
      "cache_read_input_tokens": 63187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1839
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

_source line 100 · 2026-05-21T16:01:06.716Z_

<details><summary>↩ Tool result · `toolu_01EJZ21BQ4YCWo7LgYzneFwL`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "b9ee2013-e5b1-4d18-9d4c-4a9bdd447b5d",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 101_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01VARrd65XbM7SBLKPTho2Zs`</summary>

```json
{
  "name": "plan_034_multi_subject_injection_script",
  "type": "intermediate",
  "description": "Multi-subject simultaneous injection experiment script — tests Proposition 1 robustness boundary by contaminating k subjects simultaneously and measuring ΔFPR on non-target subjects",
  "project": "irt_equated_bench_regen",
  "exp_id": "plan_034",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
  "tags": [
    "semi-synthetic",
    "mh-dif",
    "proposition-1",
    "robustness"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "b211ba81-f168-466e-844d-aec269b45e28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQqoyQudc6P7XcJ7iFgX3P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 65026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 820
      },
      "output_tokens": 51,
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

_source line 102 · 2026-05-21T16:01:12.593Z_

<details><summary>↩ Tool result · `toolu_01VARrd65XbM7SBLKPTho2Zs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_05eda7\", \"name\": \"plan_034_multi_subject_injection_script\", \"type\": \"intermediate\", \"description\": \"Multi-subject simultaneous injection experiment script — tests Proposition 1 robustness boundary by contaminating k subjects simultaneously and measuring ΔFPR on non-target subjects\", \"path\": \"projects/irt_equated_bench_regen/artifacts/plan_034/intermediate/plan_034_multi_subject_injection.py\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": \"plan_034\", \"skill\": \"\", \"created_at\": \"2026-05-21T16:01:12.191386+00:00\", \"tags\": [\"semi-synthetic\", \"mh-dif\", \"proposition-1\", \"robustness\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "961106c3-d6a7-4353-8b8d-e7efc3b7329a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260521_05eda7\\\", \\\"name\\\": \\\"plan_034_multi_subject_injection_script\\\", \\\"type\\\": \\\"intermediate\\\", \\\"description\\\": \\\"Multi-subject simultaneous injection experiment script — tests Proposition 1 robustness boundary by contaminating k subjects simultaneously and measuring ΔFPR on non-target subjects\\\", \\\"path\\\": \\\"projects/irt_equated_bench_regen/artifacts/plan_034/intermediate/plan_034_multi_subject_injection.py\\\", \\\"url\\\": null, \\\"project\\\": \\\"irt_equated_bench_regen\\\", \\\"exp_id\\\": \\\"plan_034\\\", \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-21T16:01:12.191386+00:00\\\", \\\"tags\\\": [\\\"semi-synthetic\\\", \\\"mh-dif\\\", \\\"proposition-1\\\", \\\"robustness\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_05eda7\", \"name\": \"plan_034_multi_subject_injection_script\", \"type\": \"intermediate\", \"description\": \"Multi-subject simultaneous injection experiment script — tests Proposition 1 robustness boundary by contaminating k subjects simultaneously and measuring ΔFPR on non-target subjects\", \"path\": \"projects/irt_equated_bench_regen/artifacts/plan_034/intermediate/plan_034_multi_subject_injection.py\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": \"plan_034\", \"skill\": \"\", \"created_at\": \"2026-05-21T16:01:12.191386+00:00\", \"tags\": [\"semi-synthetic\", \"mh-dif\", \"proposition-1\", \"robustness\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 103_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01N5LR92vC5tqUPQd6GuVTbz`</summary>

```json
{
  "name": "plan_034_target_results",
  "type": "data",
  "description": "Per-target-subject DIF results (TPR) for multi-subject injection: 615 rows across k∈{1,2,3,5,10,20}, p∈{0.1,0.3,0.5}, 5 seeds",
  "project": "irt_equated_bench_regen",
  "exp_id": "plan_034",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/multi_subject_injection_results.csv",
  "tags": [
    "semi-synthetic",
    "mh-dif",
    "tpr"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "f04a0078-5fe7-4543-bf09-0cf4c6624e71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQqoyQudc6P7XcJ7iFgX3P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 65026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 820
      },
      "output_tokens": 51,
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

_source line 104 · 2026-05-21T16:01:16.376Z_

<details><summary>↩ Tool result · `toolu_01N5LR92vC5tqUPQd6GuVTbz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_d9665b\", \"name\": \"plan_034_target_results\", \"type\": \"data\", \"description\": \"Per-target-subject DIF results (TPR) for multi-subject injection: 615 rows across k∈{1,2,3,5,10,20}, p∈{0.1,0.3,0.5}, 5 seeds\", \"path\": \"projects/irt_equated_bench_regen/artifacts/plan_034/data/multi_subject_injection_results.csv\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": \"plan_034\", \"skill\": \"\", \"created_at\": \"2026-05-21T16:01:16.115790+00:00\", \"tags\": [\"semi-synthetic\", \"mh-dif\", \"tpr\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "18755b7a-e8e1-4082-b46b-4c4fd56768b2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260521_d9665b\\\", \\\"name\\\": \\\"plan_034_target_results\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Per-target-subject DIF results (TPR) for multi-subject injection: 615 rows across k∈{1,2,3,5,10,20}, p∈{0.1,0.3,0.5}, 5 seeds\\\", \\\"path\\\": \\\"projects/irt_equated_bench_regen/artifacts/plan_034/data/multi_subject_injection_results.csv\\\", \\\"url\\\": null, \\\"project\\\": \\\"irt_equated_bench_regen\\\", \\\"exp_id\\\": \\\"plan_034\\\", \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-21T16:01:16.115790+00:00\\\", \\\"tags\\\": [\\\"semi-synthetic\\\", \\\"mh-dif\\\", \\\"tpr\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_d9665b\", \"name\": \"plan_034_target_results\", \"type\": \"data\", \"description\": \"Per-target-subject DIF results (TPR) for multi-subject injection: 615 rows across k∈{1,2,3,5,10,20}, p∈{0.1,0.3,0.5}, 5 seeds\", \"path\": \"projects/irt_equated_bench_regen/artifacts/plan_034/data/multi_subject_injection_results.csv\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": \"plan_034\", \"skill\": \"\", \"created_at\": \"2026-05-21T16:01:16.115790+00:00\", \"tags\": [\"semi-synthetic\", \"mh-dif\", \"tpr\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 105_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01BXFwcTuMruc2K5cBeQzU5m`</summary>

```json
{
  "name": "plan_034_non_target_fpr",
  "type": "data",
  "description": "Non-target subject FPR under multi-subject injection: 1800 rows measuring matching variable pollution effect on uninjected subjects",
  "project": "irt_equated_bench_regen",
  "exp_id": "plan_034",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/non_target_fpr_results.csv",
  "tags": [
    "semi-synthetic",
    "mh-dif",
    "fpr",
    "proposition-1"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "9b75abdf-c85e-4e78-a5c4-6bc06b1ea8c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQqoyQudc6P7XcJ7iFgX3P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 65026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 820
      },
      "output_tokens": 51,
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

_source line 106 · 2026-05-21T16:01:18.769Z_

<details><summary>↩ Tool result · `toolu_01BXFwcTuMruc2K5cBeQzU5m`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_f7efb2\", \"name\": \"plan_034_non_target_fpr\", \"type\": \"data\", \"description\": \"Non-target subject FPR under multi-subject injection: 1800 rows measuring matching variable pollution effect on uninjected subjects\", \"path\": \"projects/irt_equated_bench_regen/artifacts/plan_034/data/non_target_fpr_results.csv\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": \"plan_034\", \"skill\": \"\", \"created_at\": \"2026-05-21T16:01:18.502235+00:00\", \"tags\": [\"semi-synthetic\", \"mh-dif\", \"fpr\", \"proposition-1\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "f172a030-f9ce-445c-8c68-e99fa3a9ea85",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260521_f7efb2\\\", \\\"name\\\": \\\"plan_034_non_target_fpr\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Non-target subject FPR under multi-subject injection: 1800 rows measuring matching variable pollution effect on uninjected subjects\\\", \\\"path\\\": \\\"projects/irt_equated_bench_regen/artifacts/plan_034/data/non_target_fpr_results.csv\\\", \\\"url\\\": null, \\\"project\\\": \\\"irt_equated_bench_regen\\\", \\\"exp_id\\\": \\\"plan_034\\\", \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-21T16:01:18.502235+00:00\\\", \\\"tags\\\": [\\\"semi-synthetic\\\", \\\"mh-dif\\\", \\\"fpr\\\", \\\"proposition-1\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_f7efb2\", \"name\": \"plan_034_non_target_fpr\", \"type\": \"data\", \"description\": \"Non-target subject FPR under multi-subject injection: 1800 rows measuring matching variable pollution effect on uninjected subjects\", \"path\": \"projects/irt_equated_bench_regen/artifacts/plan_034/data/non_target_fpr_results.csv\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": \"plan_034\", \"skill\": \"\", \"created_at\": \"2026-05-21T16:01:18.502235+00:00\", \"tags\": [\"semi-synthetic\", \"mh-dif\", \"fpr\", \"proposition-1\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 107_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01BeGneiuaXq8wum637CGQ5L`</summary>

```json
{
  "name": "plan_034_summary",
  "type": "data",
  "description": "Summary statistics aggregated by (k, p): mean ΔFPR/ΔTPR for target and non-target subjects with cross-seed SD",
  "project": "irt_equated_bench_regen",
  "exp_id": "plan_034",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/summary_by_k.csv",
  "tags": [
    "semi-synthetic",
    "summary"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "7c48bae3-3dc8-400f-8e80-1001591cd158",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQqoyQudc6P7XcJ7iFgX3P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 65026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 820
      },
      "output_tokens": 51,
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

_source line 108 · 2026-05-21T16:01:21.833Z_

<details><summary>↩ Tool result · `toolu_01BeGneiuaXq8wum637CGQ5L`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_d616d2\", \"name\": \"plan_034_summary\", \"type\": \"data\", \"description\": \"Summary statistics aggregated by (k, p): mean ΔFPR/ΔTPR for target and non-target subjects with cross-seed SD\", \"path\": \"projects/irt_equated_bench_regen/artifacts/plan_034/data/summary_by_k.csv\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": \"plan_034\", \"skill\": \"\", \"created_at\": \"2026-05-21T16:01:21.547071+00:00\", \"tags\": [\"semi-synthetic\", \"summary\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "0e8621ab-e37f-4af7-9de9-df4c2603ff99",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260521_d616d2\\\", \\\"name\\\": \\\"plan_034_summary\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Summary statistics aggregated by (k, p): mean ΔFPR/ΔTPR for target and non-target subjects with cross-seed SD\\\", \\\"path\\\": \\\"projects/irt_equated_bench_regen/artifacts/plan_034/data/summary_by_k.csv\\\", \\\"url\\\": null, \\\"project\\\": \\\"irt_equated_bench_regen\\\", \\\"exp_id\\\": \\\"plan_034\\\", \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-21T16:01:21.547071+00:00\\\", \\\"tags\\\": [\\\"semi-synthetic\\\", \\\"summary\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_d616d2\", \"name\": \"plan_034_summary\", \"type\": \"data\", \"description\": \"Summary statistics aggregated by (k, p): mean ΔFPR/ΔTPR for target and non-target subjects with cross-seed SD\", \"path\": \"projects/irt_equated_bench_regen/artifacts/plan_034/data/summary_by_k.csv\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": \"plan_034\", \"skill\": \"\", \"created_at\": \"2026-05-21T16:01:21.547071+00:00\", \"tags\": [\"semi-synthetic\", \"summary\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 109_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01Urrc9E1kPVxQZ6nSHTbFrn`</summary>

```json
{
  "name": "plan_034_report",
  "type": "report",
  "description": "Plan 034 report: Proposition 1 validity boundary at k≈5-10 subjects, ΔFPR remains <0.007 for k≤5, rises to +0.167 at k=20/p=0.5",
  "project": "irt_equated_bench_regen",
  "exp_id": "plan_034",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_report.md",
  "tags": [
    "proposition-1",
    "robustness",
    "validity-boundary"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "91d0b556-d57a-40c7-85fb-6b60c2d00c45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQqoyQudc6P7XcJ7iFgX3P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 65026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 820
      },
      "output_tokens": 51,
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

_source line 110 · 2026-05-21T16:01:25.100Z_

<details><summary>↩ Tool result · `toolu_01Urrc9E1kPVxQZ6nSHTbFrn`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_c0cc74\", \"name\": \"plan_034_report\", \"type\": \"report\", \"description\": \"Plan 034 report: Proposition 1 validity boundary at k≈5-10 subjects, ΔFPR remains <0.007 for k≤5, rises to +0.167 at k=20/p=0.5\", \"path\": \"projects/irt_equated_bench_regen/artifacts/plan_034/report/plan_034_report.md\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": \"plan_034\", \"skill\": \"\", \"created_at\": \"2026-05-21T16:01:24.820161+00:00\", \"tags\": [\"proposition-1\", \"robustness\", \"validity-boundary\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "5d2446d6-e174-4e00-abac-b697591aa3b7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260521_c0cc74\\\", \\\"name\\\": \\\"plan_034_report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Plan 034 report: Proposition 1 validity boundary at k≈5-10 subjects, ΔFPR remains <0.007 for k≤5, rises to +0.167 at k=20/p=0.5\\\", \\\"path\\\": \\\"projects/irt_equated_bench_regen/artifacts/plan_034/report/plan_034_report.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"irt_equated_bench_regen\\\", \\\"exp_id\\\": \\\"plan_034\\\", \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-21T16:01:24.820161+00:00\\\", \\\"tags\\\": [\\\"proposition-1\\\", \\\"robustness\\\", \\\"validity-boundary\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_c0cc74\", \"name\": \"plan_034_report\", \"type\": \"report\", \"description\": \"Plan 034 report: Proposition 1 validity boundary at k≈5-10 subjects, ΔFPR remains <0.007 for k≤5, rises to +0.167 at k=20/p=0.5\", \"path\": \"projects/irt_equated_bench_regen/artifacts/plan_034/report/plan_034_report.md\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": \"plan_034\", \"skill\": \"\", \"created_at\": \"2026-05-21T16:01:24.820161+00:00\", \"tags\": [\"proposition-1\", \"robustness\", \"validity-boundary\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 111_

Plan 034 完成。核心结果：

**Proposition 1 的 validity boundary 在 k ≈ 5–10 个 subjects：**

- **k ≤ 5**（≤ 8.8% subjects 被污染）：non-target ΔFPR < 0.007，与噪声无异。Proposition 1 实际成立。
- **k = 10**（17.5%）：p ≥ 0.3 时 ΔFPR 开始显著（+0.026 ~ +0.069）。
- **k = 20**（35.1%）：ΔFPR 大幅膨胀（p=0.5 时 +0.167，绝对 FPR 从 0.31 升到 0.49）。

其他发现：
- 低注入强度 p=0.1 在所有 k 值下都 robust（ΔFPR ≈ 0）
- Target-subject TPR 随 k 增大而下降（matching variable 吸收了部分 DIF 信号）

所有输出文件已保存并注册：脚本、3 个 CSV（target results / non-target FPR / summary）、report。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "uuid": "4a77d994-df21-401a-a516-e6038226cc30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UNM3oufWtzyUkduQWbjRrF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3085,
      "cache_read_input_tokens": 65846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3085
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

_source line 112_

Plan 034 完成。核心结果：

**Proposition 1 的 validity boundary 在 k ≈ 5–10 个 subjects：**

- **k ≤ 5**（≤ 8.8% subjects 被污染）：non-target ΔFPR < 0.007，与噪声无异。Proposition 1 实际成立。
- **k = 10**（17.5%）：p ≥ 0.3 时 ΔFPR 开始显著（+0.026 ~ +0.069）。
- **k = 20**（35.1%）：ΔFPR 大幅膨胀（p=0.5 时 +0.167，绝对 FPR 从 0.31 升到 0.49）。

其他发现：
- 低注入强度 p=0.1 在所有 k 值下都 robust（ΔFPR ≈ 0）
- Target-subject TPR 随 k 增大而下降（matching variable 吸收了部分 DIF 信号）

所有输出文件已保存并注册：脚本、3 个 CSV（target results / non-target FPR / summary）、report。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 982031,
  "duration_api_ms": 447275,
  "num_turns": 29,
  "stop_reason": "end_turn",
  "session_id": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "total_cost_usd": 1.5747877499999998,
  "usage": {
    "input_tokens": 29,
    "cache_creation_input_tokens": 57090,
    "cache_read_input_tokens": 1205875,
    "output_tokens": 20345,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 57090,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 330,
        "cache_read_input_tokens": 65846,
        "cache_creation_input_tokens": 3085,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3085
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2187,
      "outputTokens": 7752,
      "cacheReadInputTokens": 159295,
      "cacheCreationInputTokens": 39513,
      "webSearchRequests": 0,
      "costUSD": 0.10626775,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 29,
      "outputTokens": 20345,
      "cacheReadInputTokens": 1205875,
      "cacheCreationInputTokens": 57090,
      "webSearchRequests": 0,
      "costUSD": 1.4685199999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6e76437f-11f7-49d8-9be2-31c627f24711"
}
```

</details>

---
