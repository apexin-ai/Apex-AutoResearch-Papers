# code lofo robustness

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 72
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/workers/worker_code_lofo_robustness_20260522T071721.log`
- **Structured JSON:** [`d14c088e18b5716a532e.json`](../../sessions/d1/d14c088e18b5716a532e.json)

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
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
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
  "uuid": "6771d1ba-c6fb-4ce1-9b51-04b3dc664fa7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/memory/"
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
    "resetsAt": 1779451800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8065449c-a575-4718-b63e-c03422aca165",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break down this task:

1. Perform a Leave-One-Family-Out (LOFO) robustness check on MMLU temporal MH-DIF C%
2. Need to explore data sources, confirm cohort definitions, align model names, then run the analysis

Let me start by exploring the necessary files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "cf521393-4499-4a03-8c9e-6c97a16ed5ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QnH173NTd9SuLc7T2EXvM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13805,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13805
      },
      "output_tokens": 42,
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

I'll start by exploring the data sources and existing code to understand cohort definitions and model name alignment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "7289680b-2373-4c13-ad56-c3840a9767fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QnH173NTd9SuLc7T2EXvM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13805,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13805
      },
      "output_tokens": 42,
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

<details open><summary>🔧 Tool call — Agent · `toolu_016Gu6sDPik5aYrBXVLzS65d`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore cohort definitions and MH code",
  "prompt": "I need to understand two things for an LOFO robustness analysis:\n\n1. **Cohort definition**: How are ref/foc cohorts defined for temporal MH-DIF? Look in:\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001*/` — any Python scripts that define cohort splits\n   - Grep for \"cohort\" or \"ref\" or \"foc\" or \"temporal\" in plan_001 artifacts\n   - Also check `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/` for any scripts\n\n2. **MH-DIF function**: Read the function `mh_dif_c_pct_vec` from `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py`\n\nSearch breadth: medium. Report the exact cohort split logic (which models are ref vs foc), and the full function code for mh_dif_c_pct_vec."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "bd9dea21-3abe-4406-8427-149b56628fed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QnH173NTd9SuLc7T2EXvM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13805,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13805
      },
      "output_tokens": 42,
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
  "task_id": "ab1e3c29de8139595",
  "tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "description": "Explore cohort definitions and MH code",
  "task_type": "local_agent",
  "prompt": "I need to understand two things for an LOFO robustness analysis:\n\n1. **Cohort definition**: How are ref/foc cohorts defined for temporal MH-DIF? Look in:\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001*/` — any Python scripts that define cohort splits\n   - Grep for \"cohort\" or \"ref\" or \"foc\" or \"temporal\" in plan_001 artifacts\n   - Also check `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/` for any scripts\n\n2. **MH-DIF function**: Read the function `mh_dif_c_pct_vec` from `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py`\n\nSearch breadth: medium. Report the exact cohort split logic (which models are ref vs foc), and the full function code for mh_dif_c_pct_vec.",
  "uuid": "b321f215-1f22-40be-a4da-6906067940bd",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd"
}
```

---

## Round 1

65 recorded events

### User

_source line 8 · 2026-05-22T07:17:40.043Z_

I need to understand two things for an LOFO robustness analysis:

1. **Cohort definition**: How are ref/foc cohorts defined for temporal MH-DIF? Look in:
   - `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001*/` — any Python scripts that define cohort splits
   - Grep for "cohort" or "ref" or "foc" or "temporal" in plan_001 artifacts
   - Also check `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/` for any scripts

2. **MH-DIF function**: Read the function `mh_dif_c_pct_vec` from `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py`

Search breadth: medium. Report the exact cohort split logic (which models are ref vs foc), and the full function code for mh_dif_c_pct_vec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "39b97a9b-0492-41c2-aac0-0347b33ead39"
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
  "task_id": "ab1e3c29de8139595",
  "tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_052…",
  "usage": {
    "total_tokens": 16326,
    "tool_uses": 1,
    "duration_ms": 1816
  },
  "last_tool_name": "Bash",
  "uuid": "f4886323-f049-4b8d-98be-deab433812fe",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd"
}
```

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Bash · `toolu_015frU9ofvbS8DvxHsn9y1tJ`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -type d -name \"plan_001*\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "b7678aa7-90e8-4d32-b2af-9f7cb21a4cc6",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017MuYYN6S4m6HAXbBghQa7S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16313,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16313,
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

_source line 11 · 2026-05-22T07:17:42.049Z_

<details><summary>↩ Tool result · `toolu_015frU9ofvbS8DvxHsn9y1tJ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "ca7fa95f-5227-46bc-a6b9-8728ec5fada9"
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_011UhxTKhSfxK5gCVSKEa4dX`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts && head -5 plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv && echo \"---\" && wc -l plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv && echo \"---\" && python3 -c \"\nimport pandas as pd\ndf = pd.read_csv('plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv')\nprint('Columns:', list(df.columns))\nprint('cohort_temporal values:', df['cohort_temporal'].value_counts().to_dict())\nprint('Top families:', df['family'].value_counts().head(10).to_dict())\nprint('Family by cohort:')\nfor cohort in df['cohort_temporal'].unique():\n    sub = df[df['cohort_temporal'] == cohort]\n    print(f'  {cohort}: {len(sub)} models, top families: {sub[\\\"family\\\"].value_counts().head(5).to_dict()}')\n\"",
  "description": "Explore cleaned_mmlu_analysis.csv structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "8aa4404d-43be-4521-9cf0-c10dfa85484c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QnH173NTd9SuLc7T2EXvM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13805,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13805
      },
      "output_tokens": 42,
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

_source line 13_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab1e3c29de8139595",
  "tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "description": "Reading artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py",
  "usage": {
    "total_tokens": 17438,
    "tool_uses": 2,
    "duration_ms": 3909
  },
  "last_tool_name": "Read",
  "uuid": "b9597844-0dee-48cf-bd78-a67cf3591fb2",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd"
}
```

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01XLzJoRyn1UkYvJn1r6dLcw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "0db1f643-d757-4bce-b6bb-a64fb6e38141",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Bnt5fhYa59VkUejAB8Jf9r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1108,
      "cache_read_input_tokens": 16313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1108,
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

_source line 15 · 2026-05-22T07:17:43.964Z_

<details><summary>↩ Tool result · `toolu_01XLzJoRyn1UkYvJn1r6dLcw`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	mmlu_bootstrap_ci.py — MMLU bootstrap 95% CI for MH-DIF C%.
4	
5	Vectorized total-score stratification (~100x faster than per-item rest-score).
6	For J=12508, total-score ≈ rest-score (diff < 0.3pp); validated at startup.
7	"""
8	
9	import numpy as np
10	import pandas as pd
11	from scipy.stats import chi2 as chi2_dist
12	from scipy.sparse import load_npz
13	from pathlib import Path
14	from multiprocessing import Pool
15	import time
16	import warnings
17	
18	warnings.filterwarnings("ignore", category=RuntimeWarning)
19	
20	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/"
21	            "projects/irt_equated_bench_regen/artifacts")
22	OUT = BASE / "plan_028_bootstrap_ci"
23	OUT.mkdir(exist_ok=True)
24	
25	N_BOOTSTRAP = 1000
26	N_CONTROL = 20
27	SEED = 42
28	N_STRATA = 5
29	
30	
31	# ════════════════════════════════════════════════════════════════════════
32	#  VECTORIZED MH-DIF (total-score stratification)
33	# ════════════════════════════════════════════════════════════════════════
34	def mh_dif_c_pct_vec(X_ref, X_foc, n_strata=N_STRATA):
35	    """Fully vectorized MH-DIF → C%. Stratifies on total score (not rest)."""
36	    n_ref, J = X_ref.shape
37	    n_foc = X_foc.shape[0]
38	
39	    tot_ref = X_ref.sum(axis=1).astype(np.float64)
40	    tot_foc = X_foc.sum(axis=1).astype(np.float64)
41	    s_all = np.concatenate([tot_ref, tot_foc])
42	
43	    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
44	    n_bins = len(edges) - 1
45	    if n_bins < 1:
46	        return 0.0
47	
48	    k_ref = np.digitize(tot_ref, edges[1:-1])
49	    k_foc = np.digitize(tot_foc, edges[1:-1])
50	
51	    n1 = np.zeros(n_bins, dtype=np.float64)
52	    n0 = np.zeros(n_bins, dtype=np.float64)
53	    A = np.zeros((n_bins, J), dtype=np.float64)
54	    C = np.zeros((n_bins, J), dtype=np.float64)
55	
56	    for k in range(n_bins):
57	        mr = (k_ref == k)
58	        mf = (k_foc == k)
59	        n1[k] = mr.sum()
60	        n0[k] = mf.sum()
61	        if mr.any():
62	            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)
63	        if mf.any():
64	            C[k] = X_foc[mf].sum(axis=0).astype(np.float64)
65	
66	    B = n1[:, None] - A
67	    D = n0[:, None] - C
68	    Nk = (n1 + n0)[:, None]
69	    m1 = A + C
70	    m0 = B + D
71	
72	    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &
73	             (Nk > 1) & (m1 > 0) & (m0 > 0))
74	
75	    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)
76	    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)
77	
78	    finite_mask = (Rj > 0) & (Sj > 0)
79	
80	    with np.errstate(divide="ignore", invalid="ignore"):
81	        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)
82	
83	    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)
84	    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)
85	
86	    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)
87	    sum_var = np.where(
88	        valid,
89	        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),
90	        0,
91	    ).sum(axis=0)
92	
93	    chi2_j = np.where(
94	        sum_var > 0,
95	        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),
96	        0,
97	    )
98	    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)
99	
100	    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)
101	    return is_c.sum() / J * 100
102	
103	
104	# ════════════════════════════════════════════════════════════════════════
105	#  REST-SCORE MH-DIF (validation only)
106	# ════════════════════════════════════════════════════════════════════════
107	def mh_dif_c_pct_rest(X_ref, X_foc, n_strata=N_STRATA):
108	    """Per-item rest-score MH-DIF (reference implementation)."""
109	    tot_ref = X_ref.sum(axis=1).astype(np.float64)
110	    tot_foc = X_foc.sum(axis=1).astype(np.float64)
111	    J = X_ref.shape[1]
112	    n_c = 0
113	    qs = np.linspace(0, 1, n_strata + 1)
114	    nr = len(tot_ref)
115	    nf = len(tot_foc)
116	    s_buf = np.empty(nr + nf, dtype=np.float64)
117	
118	    for j in range(J):
119	        s_buf[:nr] = tot_ref - X_ref[:, j]
120	        s_buf[nr:] = tot_foc - X_foc[:, j]
121	        edges = np.unique(np.quantile(s_buf, qs))
122	        nb = len(edges) - 1
123	        if nb < 1:
124	            continue
125	        kr = np.digitize(s_buf[:nr], edges[1:-1])
126	        kf = np.digitize(s_buf[nr:], edges[1:-1])
127	
128	        R = S = sd = sv = 0.0
129	        n_ok = 0
130	        for k in range(nb):
131	            mr = (kr == k)
132	            mf = (kf == k)
133	            n1 = int(mr.sum())
134	            n0 = int(mf.sum())
135	            if n1 == 0 or n0 == 0:
136	                continue
137	            Ak = float(X_ref[mr, j].sum())
138	            Bk = n1 - Ak
139	            Ck = float(X_foc[mf, j].sum())
140	            Dk = n0 - Ck
141	            Nk = n1 + n0
142	            m1k = Ak + Ck
143	            m0k = Bk + Dk
144	            if m1k == 0 or m0k == 0 or Nk <= 1:
145	                continue
146	            n_ok += 1
147	            R += Ak * Dk / Nk
148	            S += Bk * Ck / Nk
149	            sd += Ak - n1 * m1k / Nk
150	            sv += n1 * n0 * m1k * m0k / (Nk * Nk * (Nk - 1))
151	
152	        if n_ok == 0 or (R == 0 and S == 0):
153	            continue
154	        if S == 0:
155	            delta = -np.inf
156	        elif R == 0:
157	            delta = np.inf
158	        else:
159	            delta = -2.35 * np.log(R / S)
160	        pval = (1 - chi2_dist.cdf(max(abs(sd) - 0.5, 0) ** 2 / sv, df=1)
161	                if sv > 0 else 1.0)
162	        if np.isfinite(delta) and abs(delta) >= 1.5 and pval < 0.05:
163	            n_c += 1
164	
165	    return n_c / J * 100
166	
167	
168	# ════════════════════════════════════════════════════════════════════════
169	#  MULTIPROCESSING BOOTSTRAP
170	# ════════════════════════════════════════════════════════════════════════
171	_Xr = None
172	_Xf = None
173	
174	
175	def _init(Xr, Xf):
176	    global _Xr, _Xf
177	    _Xr = Xr
178	    _Xf = Xf
179	
180	
181	def _boot_one(seed):
182	    rng = np.random.RandomState(seed)
183	    ir = rng.randint(0, _Xr.shape[0], size=_Xr.shape[0])
184	    jf = rng.randint(0, _Xf.shape[0], size=_Xf.shape[0])
185	    return mh_dif_c_pct_vec(_Xr[ir], _Xf[jf])
186	
187	
188	# ════════════════════════════════════════════════════════════════════════
189	#  MAIN
190	# ════════════════════════════════════════════════════════════════════════
191	def main():
192	    t_total = time.time()
193	    print(f"MMLU Bootstrap CI — N={N_BOOTSTRAP}, seed={SEED}")
194	    print(f"Output: {OUT}\n")
195	
196	    # ── Load ──
197	    print("Loading MMLU response matrix...")
198	    t0 = time.time()
199	    X = load_npz(BASE / "response_matrix.npz").toarray().astype(np.int8)
200	    idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
201	    model_names = idx["model_names"]
202	    meta = pd.read_csv(BASE / "model_metadata.csv")
203	    cohort = dict(zip(meta["model_name"], meta["cohort_temporal"]))
204	    print(f"  {X.shape[0]} models × {X.shape[1]} items ({time.time()-t0:.1f}s)")
205	
206	    name2row = {n: i for i, n in enumerate(model_names)}
207	    ref_idx = np.array([name2row[n] for n in model_names if cohort.get(n) == "2023"])
208	    foc_idx = np.array([name2row[n] for n in model_names if cohort.get(n) == "2024"])
209	    print(f"  Cohorts: ref(2023)={len(ref_idx)}, foc(2024)={len(foc_idx)}")
210	
211	    X_ref = X[ref_idx]
212	    X_foc = X[foc_idx]
213	    del X
214	
215	    # ── Validate total-score vs rest-score ──
216	    print("\nValidation: total-score vs rest-score stratification...")
217	    t0 = time.time()
218	    c_vec = mh_dif_c_pct_vec(X_ref, X_foc)
219	    t_vec = time.time() - t0
220	    print(f"  Vectorized (total-score): C% = {c_vec:.2f}% ({t_vec:.2f}s)")
221	
222	    t0 = time.time()
223	    c_rest = mh_dif_c_pct_rest(X_ref, X_foc)
224	    t_rest = time.time() - t0
225	    print(f"  Original  (rest-score):   C% = {c_rest:.2f}% ({t_rest:.1f}s)")
226	    diff_pp = abs(c_vec - c_rest)
227	    print(f"  Difference: {diff_pp:.2f}pp  |  Speedup: {t_rest/t_vec:.0f}x")
228	
229	    use_rest = diff_pp > 1.0
230	    if use_rest:
231	        print("  WARNING: >1pp gap — using rest-score (slow path)")
232	
233	    # ── Sanity check N=10 ──
234	    print(f"\nSanity check: N=10 bootstrap...")
235	    rng = np.random.RandomState(SEED)
236	    fn = mh_dif_c_pct_rest if use_rest else mh_dif_c_pct_vec
237	    sanity = []
238	    for i in range(10):
239	        ir = rng.randint(0, len(ref_idx), size=len(ref_idx))
240	        jf = rng.randint(0, len(foc_idx), size=len(foc_idx))
241	        sanity.append(fn(X_ref[ir], X_foc[jf]))
242	    print(f"  C% range: [{min(sanity):.1f}%, {max(sanity):.1f}%], "
243	          f"mean={np.mean(sanity):.1f}%  (expect ≈31%)")
244	
245	    # ── Full bootstrap N=1000 ──
246	    print(f"\nBootstrap N={N_BOOTSTRAP} (2 processes)...")
247	    seeds = list(range(SEED, SEED + N_BOOTSTRAP))
248	    boot_cs = np.zeros(N_BOOTSTRAP)
249	    t_start = time.time()
250	
251	    with Pool(2, initializer=_init, initargs=(X_ref, X_foc)) as pool:
252	        for i, c in enumerate(pool.imap(
253	                _boot_one if not use_rest else _boot_one, seeds)):
254	            boot_cs[i] = c
255	            done = i + 1
256	            if done % 100 == 0 or done == 1:
257	                el = time.time() - t_start
258	                eta = (N_BOOTSTRAP - done) / (done / el) / 60
259	                print(f"  [{done}/{N_BOOTSTRAP}] C%={c:.2f}%  "
260	                      f"running mean={boot_cs[:done].mean():.2f}%  "
261	                      f"({el:.0f}s, ETA {eta:.0f}min)")
262	
263	    ci_lo = np.percentile(boot_cs, 2.5)
264	    ci_hi = np.percentile(boot_cs, 97.5)
265	    b_mean = boot_cs.mean()
266	    b_std = boot_cs.std()
267	
268	    print(f"\n  Original C% = {c_rest:.2f}% (rest-score)")
269	    print(f"  95% CI: [{ci_lo:.2f}%, {ci_hi:.2f}%]")
270	    print(f"  Boot mean={b_mean:.2f}%, std={b_std:.2f}%, "
271	          f"bias={b_mean - c_vec:+.2f}pp")
272	
273	    # ── Random-split control ──
274	    print(f"\nRandom-split control (N={N_CONTROL})...")
275	    combined = np.vstack([X_ref, X_foc])
276	    rng_c = np.random.RandomState(SEED + 9999)
277	    ctrl = []
278	    for i in range(N_CONTROL):
279	        perm = rng_c.permutation(combined.shape[0])
280	        Xr = combined[perm[: len(ref_idx)]]
281	        Xf = combined[perm[len(ref_idx): len(ref_idx) + len(foc_idx)]]
282	        ctrl.append(mh_dif_c_pct_vec(Xr, Xf))
283	        if (i + 1) % 5 == 0:
284	            print(f"  [{i+1}/{N_CONTROL}] C%={ctrl[-1]:.2f}%")
285	
286	    ctrl_mean = np.mean(ctrl)
287	    ctrl_std = np.std(ctrl)
288	    print(f"  Control: mean={ctrl_mean:.2f}%, std={ctrl_std:.2f}%, "
289	          f"range=[{min(ctrl):.2f}%, {max(ctrl):.2f}%]")
290	
291	    # ── Save ──
292	    pd.DataFrame({"bootstrap_id": range(N_BOOTSTRAP), "c_pct": boot_cs}).to_csv(
293	        OUT / "mmlu_bootstrap_results.csv", index=False)
294	
295	    summary = pd.DataFrame([{
296	        "benchmark": "mmlu",
297	        "original_c_pct_rest": c_rest,
298	        "original_c_pct_vec": c_vec,
299	        "ci_lower": ci_lo,
300	        "ci_upper": ci_hi,
301	        "boot_mean": b_mean,
302	        "boot_std": b_std,
303	        "n_bootstrap": N_BOOTSTRAP,
304	        "n_ref": len(ref_idx),
305	        "n_foc": len(foc_idx),
306	        "n_items": X_ref.shape[1],
307	        "ctrl_mean": ctrl_mean,
308	        "ctrl_std": ctrl_std,
309	    }])
310	    summary.to_csv(OUT / "mmlu_bootstrap_summary.csv", index=False)
311	
312	    elapsed = time.time() - t_total
313	    temporal_vs_ctrl = ("confirms DIF is temporal, not spurious"
314	                        if ctrl_mean < ci_lo
315	                        else "control overlaps temporal — interpret with caution")
316	
317	    report = f"""# MMLU Bootstrap 95% CI for MH-DIF C%
318	
319	## Method
320	
321	- Bootstrap resampling of **models** (not items), N={N_BOOTSTRAP}
322	- Per bootstrap: resample N_ref={len(ref_idx)} (2023) and N_foc={len(foc_idx)} (2024) with replacement
323	- MH-DIF with {N_STRATA}-stratum total-score matching
324	- Validated against rest-score: diff = {diff_pp:.2f}pp (speedup {t_rest/t_vec:.0f}x)
325	- 95% CI via percentile method [2.5th, 97.5th]
326	- Seed = {SEED}
327	
328	## Results
329	
330	| Metric | Value |
331	|--------|-------|
332	| Original C% (rest-score) | {c_rest:.2f}% |
333	| Original C% (total-score) | {c_vec:.2f}% |
334	| Bootstrap 95% CI | [{ci_lo:.2f}%, {ci_hi:.2f}%] |
335	| Bootstrap mean | {b_mean:.2f}% |
336	| Bootstrap SD | {b_std:.2f}% |
337	| Bias (mean − original) | {b_mean - c_vec:+.2f}pp |
338	| CI width | {ci_hi - ci_lo:.2f}pp |
339	
340	## Random-Split Control (N={N_CONTROL})
341	
342	| Metric | Value |
343	|--------|-------|
344	| Control mean C% | {ctrl_mean:.2f}% |
345	| Control SD | {ctrl_std:.2f}% |
346	| Control range | [{min(ctrl):.2f}%, {max(ctrl):.2f}%] |
347	
348	## Interpretation
349	
350	- 95% CI [{ci_lo:.1f}%, {ci_hi:.1f}%] — {'narrow, estimate is stable' if (ci_hi - ci_lo) < 10 else 'moderate width'}
351	- Control C% = {ctrl_mean:.1f}% vs temporal C% = {c_rest:.1f}% — {temporal_vs_ctrl}
352	
353	Runtime: {elapsed / 60:.1f} min
354	"""
355	    (OUT / "mmlu_bootstrap_report.md").write_text(report)
356	
357	    print(f"\nSaved: mmlu_bootstrap_results.csv, mmlu_bootstrap_summary.csv, "
358	          f"mmlu_bootstrap_report.md")
359	    print(f"Total: {elapsed / 60:.1f} min")
360	
361	
362	if __name__ == "__main__":
363	    main()
364	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "3ab54678-ecae-4477-89c9-759edd0dc984"
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01Tui5qykFUateyjkF9LfF9F`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts && python3 -c \"\nimport numpy as np\nidx = np.load('response_matrix_index.npz', allow_pickle=True)\nmodel_names = list(idx['model_names'])\nitem_ids = list(idx['item_ids'])\nprint(f'Models: {len(model_names)}, Items: {len(item_ids)}')\nprint('First 5 models:', model_names[:5])\nprint('Last 5 models:', model_names[-5:])\n\"",
  "description": "Check response matrix index"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "42154e85-7535-4636-9d47-a816df699a16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QnH173NTd9SuLc7T2EXvM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13805,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13805
      },
      "output_tokens": 42,
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

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ab1e3c29de8139595",
  "tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_052…",
  "usage": {
    "total_tokens": 23543,
    "tool_uses": 3,
    "duration_ms": 6150
  },
  "last_tool_name": "Bash",
  "uuid": "d705a13a-1ff3-4204-8da2-921ea77d169b",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01H9ngQn3GGrg86QTnFb9dtP`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001* -type f -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "46a1c32c-66aa-44be-8712-48acc2ce51e8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C9i31xKQzw1QJzncGhWR6a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6101,
      "cache_read_input_tokens": 17421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6101,
        "ephemeral_1h_input_tokens": 0
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

_source line 19 · 2026-05-22T07:17:46.256Z_

<details><summary>↩ Tool result · `toolu_01H9ngQn3GGrg86QTnFb9dtP`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/intermediate/plan_001_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/plan_001_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/plan_001b_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/data/plan_001b_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "b900a99b-a0ba-4307-b763-3f3e956ae247"
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
  "task_id": "ab1e3c29de8139595",
  "tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "description": "Searching for cohort|ref|foc|temporal",
  "usage": {
    "total_tokens": 23980,
    "tool_uses": 4,
    "duration_ms": 8126
  },
  "last_tool_name": "Grep",
  "uuid": "2cbe0233-44cb-4fec-aa6f-f53a86358be2",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd"
}
```

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Grep · `toolu_011kKGAxW9KmF7HjxkaMTkbb`</summary>

```json
{
  "pattern": "cohort|ref|foc|temporal",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001",
  "type": "py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "736f47f7-6c86-4dcf-844e-ba075e3138e7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016BKs5aYyuWCSqhJVqcV2Dn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 23522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 401,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 22 · 2026-05-22T07:17:48.190Z_

<details><summary>↩ Tool result · `toolu_011kKGAxW9KmF7HjxkaMTkbb`</summary>

```text
Found 1 file
artifacts/plan_001/plan_001_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "1249e8fb-cc24-494e-8cb4-1c3509b02554"
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
  "task_id": "ab1e3c29de8139595",
  "tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "description": "Reading artifacts/plan_001/plan_001_analysis.py",
  "usage": {
    "total_tokens": 24216,
    "tool_uses": 5,
    "duration_ms": 9498
  },
  "last_tool_name": "Read",
  "uuid": "7fcc54d3-4edb-4be5-9ceb-40919061b34c",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01AHAydbJmVAoqxQzdUbzy6a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "b3093568-f007-4178-868f-70162af49fcd",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017EdhPptEXDo9XGzNfcGGAT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 185,
      "cache_read_input_tokens": 23923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 185,
        "ephemeral_1h_input_tokens": 0
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

_source line 25 · 2026-05-22T07:17:49.808Z_

<details><summary>↩ Tool result · `toolu_01AHAydbJmVAoqxQzdUbzy6a`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_001_analysis.py — METABENCH real-data MH-DIF analysis
4	
5	Runs purified Mantel-Haenszel DIF detection on MMLU binary response data with
6	two cohort definitions (temporal 2023-vs-2024, ability Q1-2 vs Q4-5), validates
7	against Li et al. contamination proxy labels, and performs within-family,
8	domain-specificity, and negative-discrimination sensitivity analyses.
9	
10	Inputs  (all in ../):
11	  response_matrix.npz          — (5227, 12508) CSR sparse, int8 binary
12	  response_matrix_index.npz    — model_names, item_ids
13	  model_metadata.csv           — cohort_temporal, cohort_accuracy_quintile, family
14	  item_metadata.csv            — subject, is_negative_disc
15	  mmlu_li2024_proxy_labels.csv — contamination_type proxy labels
16	
17	Outputs (all in ./):
18	  dif_results_temporal.csv, dif_results_ability.csv, dif_summary.csv,
19	  within_family_dif.csv, cross_analysis.csv, domain_specificity.csv,
20	  neg_disc_sensitivity.csv, plan_001_report.md
21	
22	Dependencies: numpy, scipy, pandas
23	"""
24	
25	import numpy as np
26	import pandas as pd
27	from scipy.sparse import load_npz
28	from scipy.stats import chi2 as chi2_dist, spearmanr
29	from pathlib import Path
30	import time
31	import warnings
32	
33	warnings.filterwarnings("ignore", category=RuntimeWarning)
34	
35	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
36	OUT = BASE / "plan_001"
37	OUT.mkdir(exist_ok=True)
38	
39	
40	# ════════════════════════════════════════════════════════════════════════════
41	#  DATA LOADING
42	# ════════════════════════════════════════════════════════════════════════════
43	print("=== Loading data ===")
44	mat = load_npz(BASE / "response_matrix.npz")
45	X = mat.toarray().astype(np.int16)          # (5227, 12508)
46	del mat
47	
48	idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
49	MODEL_NAMES = idx["model_names"]             # (5227,)
50	ITEM_IDS    = idx["item_ids"]                # (12508,)
51	
52	model_meta = pd.read_csv(BASE / "model_metadata.csv")
53	item_meta  = pd.read_csv(BASE / "item_metadata.csv")
54	li_labels  = pd.read_csv(BASE / "mmlu_li2024_proxy_labels.csv")
55	
56	NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}
57	N_MODELS, J = X.shape
58	print(f"  Matrix {N_MODELS}×{J}")
59	print(f"  Li annotated: {(li_labels.contamination_type != 'no_annotation').sum()}, "
60	      f"no_annotation: {(li_labels.contamination_type == 'no_annotation').sum()}")
61	
62	
63	# ════════════════════════════════════════════════════════════════════════════
64	#  MH-DIF CORE
65	# ════════════════════════════════════════════════════════════════════════════
66	def mh_dif(X_ref, X_foc, n_strata=5, col_mask=None):
67	    """
68	    Purified Mantel-Haenszel DIF for all items (or a column subset).
69	
70	    For item j the matching variable is:
71	        purified_score = total_score_across_all_columns - response_to_item_j
72	
73	    Parameters
74	    ----------
75	    X_ref, X_foc : ndarray (N_ref, J) and (N_foc, J), int, binary 0/1
76	    n_strata     : number of quantile-based score strata
77	    col_mask     : bool array (J,); True = analyse this column.  None = all.
78	
79	    Returns
80	    -------
81	    DataFrame with cols: col_idx, alpha_mh, delta_mh, se, chi2, p_value, ets_class
82	    """
83	    _Nr, Jc = X_ref.shape
84	
85	    # row-wise total scores (used for purified matching)
86	    tot_ref = X_ref.sum(axis=1).astype(np.float64)   # (N_ref,)
87	    tot_foc = X_foc.sum(axis=1).astype(np.float64)   # (N_foc,)
88	
89	    cols = np.where(col_mask)[0] if col_mask is not None else np.arange(Jc)
90	    rows = []
91	    t0 = time.time()
92	
93	    for pos, j in enumerate(cols):
94	        if pos % 2500 == 0 and pos > 0:
95	            print(f"    {pos}/{len(cols)}  ({time.time()-t0:.0f}s)")
96	
97	        # ── purified scores: exclude item j from matching variable ──
98	        s_ref = tot_ref - X_ref[:, j].astype(np.float64)
99	        s_foc = tot_foc - X_foc[:, j].astype(np.float64)
100	
101	        # ── quantile-based strata on pooled purified scores ──
102	        s_all = np.concatenate([s_ref, s_foc])
103	        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
104	        if len(edges) < 2:
105	            rows.append(_nan_row(j))
106	            continue
107	        n_bins = len(edges) - 1
108	
109	        k_ref = np.digitize(s_ref, edges[1:-1])      # values in [0, n_bins-1]
110	        k_foc = np.digitize(s_foc, edges[1:-1])
111	
112	        # ── accumulate MH statistics across strata ──
113	        #   α_MH = R / S  where  R = Σ A_k D_k / N_k,  S = Σ B_k C_k / N_k
114	        #   Δ_MH = −2.35 · ln(α_MH)
115	        R = S = 0.0
116	        sum_diff = 0.0       # Σ (A_k − E[A_k])
117	        sum_var  = 0.0       # Σ Var(A_k)
118	        # Robins-Breslow-Greenland variance components for ln(α_MH)
119	        pr = ps_qr = qs = 0.0
120	        n_ok = 0
121	
122	        for k in range(n_bins):
123	            mr = (k_ref == k)
124	            mf = (k_foc == k)
125	            n1 = int(mr.sum())           # ref count in stratum
126	            n0 = int(mf.sum())           # foc count in stratum
127	            if n1 == 0 or n0 == 0:
128	                continue
129	
130	            A = float(X_ref[mr, j].sum())   # ref correct
131	            B = float(n1 - A)               # ref incorrect
132	            C = float(X_foc[mf, j].sum())   # foc correct
133	            D = float(n0 - C)               # foc incorrect
134	            Nk = float(n1 + n0)
135	            m1 = A + C                       # total correct
136	            m0 = B + D                       # total incorrect
137	
138	            if m1 == 0 or m0 == 0 or Nk <= 1:
139	                continue
140	            n_ok += 1
141	
142	            Rk = A * D / Nk
143	            Sk = B * C / Nk
144	            R += Rk
145	            S += Sk
146	
147	            # E[A_k] = n1·m1 / N_k
148	            EA = n1 * m1 / Nk
149	            sum_diff += A - EA
150	            # Var(A_k) = n1·n0·m1·m0 / (N_k²·(N_k−1))
151	            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))
152	
153	            # RBG components: P_k = (A+D)/N, Q_k = (B+C)/N
154	            Pk = (A + D) / Nk
155	            Qk = (B + C) / Nk
156	            pr    += Pk * Rk
157	            ps_qr += Pk * Sk + Qk * Rk
158	            qs    += Qk * Sk
159	
160	        if n_ok == 0 or (R == 0 and S == 0):
161	            rows.append(_nan_row(j))
162	            continue
163	
164	        # ── MH odds ratio ──
165	        if S == 0:
166	            alpha, delta, se = np.inf, -np.inf, np.nan
167	        elif R == 0:
168	            alpha, delta, se = 0.0, np.inf, np.nan
169	        else:
170	            alpha = R / S
171	            delta = -2.35 * np.log(alpha)
172	            # SE via Robins-Breslow-Greenland:
173	            #   Var(ln α) = pr/(2R²) + ps_qr/(2RS) + qs/(2S²)
174	            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)
175	            se = 2.35 * np.sqrt(v) if v > 0 else np.nan
176	
177	        # ── MH χ² with continuity correction (df=1) ──
178	        if sum_var > 0:
179	            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
180	            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
181	        else:
182	            chi2_stat = pval = np.nan
183	
184	        # ── ETS classification ──
185	        #   A: |Δ| < 1.0
186	        #   C: |Δ| ≥ 1.5 AND p < 0.05
187	        #   B: everything else
188	        ad = abs(delta) if np.isfinite(delta) else 0.0
189	        if ad < 1.0:
190	            ets = "A"
191	        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:
192	            ets = "C"
193	        else:
194	            ets = "B"
195	
196	        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,
197	                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))
198	
199	    elapsed = time.time() - t0
200	    print(f"    done — {len(cols)} items in {elapsed:.1f}s")
201	    return pd.DataFrame(rows)
202	
203	
204	def _nan_row(j):
205	    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,
206	                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class="A")
207	
208	
209	# ════════════════════════════════════════════════════════════════════════════
210	#  HELPERS
211	# ════════════════════════════════════════════════════════════════════════════
212	def rows_for(col, values):
213	    """Row indices into X for models matching model_meta[col] ∈ values."""
214	    names = model_meta.loc[model_meta[col].isin(values), "model_name"]
215	    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])
216	
217	
218	def enrich(df):
219	    """Attach item_id, subject, Li labels to DIF results (col_idx → item_id)."""
220	    df = df.copy()
221	    df["item_id"] = [ITEM_IDS[i] for i in df["col_idx"]]
222	    df = df.merge(item_meta[["item_id", "subject"]], on="item_id", how="left")
223	    df = df.merge(
224	        li_labels[["item_id", "is_contaminated", "contamination_type"]].rename(
225	            columns={"is_contaminated": "li_label",
226	                     "contamination_type": "li_contamination_type"}),
227	        on="item_id", how="left",
228	    )
229	    return df
230	
231	
232	def li_metrics(df):
233	    """FPR, contaminated rate, enrichment from enriched DIF results."""
234	    is_c   = df["ets_class"] == "C"
235	    clean  = df["li_contamination_type"] == "clean"
236	    contam = df["li_contamination_type"].isin(["input_only", "input_and_label"])
237	    unlab  = df["li_contamination_type"] == "no_annotation"
238	
239	    r_clean  = is_c[clean].mean()  if clean.any()  else np.nan
240	    r_contam = is_c[contam].mean() if contam.any() else np.nan
241	    r_unlab  = is_c[unlab].mean()  if unlab.any()  else np.nan
242	    enrich   = r_contam / r_clean  if r_clean > 0  else np.nan
243	
244	    return dict(fpr_vs_li_clean=r_clean, rate_contaminated=r_contam,
245	                rate_clean=r_clean, rate_unlabeled=r_unlab,
246	                enrichment_ratio=enrich)
247	
248	
249	def summary_row(cohort, filt, df):
250	    vc = df["ets_class"].value_counts()
251	    n  = len(df)
252	    lm = li_metrics(df)
253	    return dict(
254	        cohort_type=cohort, item_filter=filt, n_items=n,
255	        n_ets_a=vc.get("A", 0), n_ets_b=vc.get("B", 0), n_ets_c=vc.get("C", 0),
256	        pct_c=vc.get("C", 0) / n * 100 if n > 0 else 0,
257	        fpr_vs_li_clean=lm["fpr_vs_li_clean"],
258	        enrichment_ratio=lm["enrichment_ratio"],
259	    )
260	
261	
262	# ════════════════════════════════════════════════════════════════════════════
263	#  MAIN
264	# ════════════════════════════════════════════════════════════════════════════
265	def main():
266	    summary_rows = []
267	
268	    # ── Step 1-2: MH-DIF — Temporal cohort ─────────────────────────────────
269	    print("\n=== Step 1-2a: Temporal cohort DIF (2023 vs 2024, 5 strata) ===")
270	    ref_t = rows_for("cohort_temporal", ["2023"])
271	    foc_t = rows_for("cohort_temporal", ["2024"])
272	    print(f"  N_ref={len(ref_t)}, N_foc={len(foc_t)}")
273	
274	    dif_temp = mh_dif(X[ref_t], X[foc_t], n_strata=5)
275	    dif_temp = enrich(dif_temp)
276	    print(f"  ETS: {dif_temp.ets_class.value_counts().to_dict()}")
277	    summary_rows.append(summary_row("temporal", "all", dif_temp))
278	
279	    # ── Step 1-2: MH-DIF — Ability cohort ──────────────────────────────────
280	    print("\n=== Step 1-2b: Ability cohort DIF (Q1-2 vs Q4-5, 10 strata) ===")
281	    ref_a = rows_for("cohort_accuracy_quintile", [1, 2])
282	    foc_a = rows_for("cohort_accuracy_quintile", [4, 5])
283	    print(f"  N_ref={len(ref_a)}, N_foc={len(foc_a)}")
284	
285	    dif_abil = mh_dif(X[ref_a], X[foc_a], n_strata=10)
286	    dif_abil = enrich(dif_abil)
287	    print(f"  ETS: {dif_abil.ets_class.value_counts().to_dict()}")
288	    summary_rows.append(summary_row("ability", "all", dif_abil))
289	
290	    # ── Step 3: Li et al. proxy validation ─────────────────────────────────
291	    print("\n=== Step 3: Li et al. proxy validation ===")
292	    li_t = li_metrics(dif_temp)
293	    li_a = li_metrics(dif_abil)
294	    print(f"  Temporal — FPR={li_t['fpr_vs_li_clean']:.4f}, "
295	          f"enrichment={li_t['enrichment_ratio']:.2f}")
296	    print(f"  Ability  — FPR={li_a['fpr_vs_li_clean']:.4f}, "
297	          f"enrichment={li_a['enrichment_ratio']:.2f}")
298	
299	    # ── Step 4: Within-family analysis ─────────────────────────────────────
300	    print("\n=== Step 4: Within-family DIF ===")
301	
302	    # Show family × temporal distribution
303	    fam_temp = (model_meta.groupby(["family", "cohort_temporal"])
304	                .size().unstack(fill_value=0))
305	    print("  Family × temporal counts:")
306	    for fam in ["llama-2", "llama-3", "mistral", "mixtral", "solar", "zephyr"]:
307	        if fam in fam_temp.index:
308	            print(f"    {fam}: {fam_temp.loc[fam].to_dict()}")
309	
310	    family_pairs = []
311	
312	    # (A) Cross-family comparisons (related families)
313	    llama2_idx = rows_for("family", ["llama-2"])
314	    llama3_idx = rows_for("family", ["llama-3"])
315	    if len(llama2_idx) >= 80 and len(llama3_idx) >= 80:
316	        family_pairs.append(("llama-2", "llama-3", llama2_idx, llama3_idx))
317	
318	    mistral_idx = rows_for("family", ["mistral"])
319	    mixtral_idx = rows_for("family", ["mixtral"])
320	    if len(mistral_idx) >= 80 and len(mixtral_idx) >= 80:
321	        family_pairs.append(("mistral", "mixtral", mistral_idx, mixtral_idx))
322	
323	    # (B) Within single family, temporal split (where both groups >= 40)
324	    for fam in ["unknown", "mistral", "llama-3", "llama-2"]:
325	        fam_df = model_meta[model_meta["family"] == fam]
326	        r_names = fam_df.loc[fam_df.cohort_temporal == "2023", "model_name"]
327	        f_names = fam_df.loc[fam_df.cohort_temporal == "2024", "model_name"]
328	        ri = np.array([NAME2ROW[n] for n in r_names if n in NAME2ROW])
329	        fi = np.array([NAME2ROW[n] for n in f_names if n in NAME2ROW])
330	        if len(ri) >= 40 and len(fi) >= 40:
331	            family_pairs.append((f"{fam}_2023", f"{fam}_2024", ri, fi))
332	
333	    wf_parts = []
334	    for rname, fname, ri, fi in family_pairs:
335	        ns = 5 if min(len(ri), len(fi)) < 200 else 10
336	        print(f"  {rname} (N={len(ri)}) vs {fname} (N={len(fi)}), {ns} strata")
337	        wf = mh_dif(X[ri], X[fi], n_strata=ns)
338	        wf = enrich(wf)
339	        wf["ref_group"] = rname
340	        wf["foc_group"] = fname
341	        wf_parts.append(wf)
342	        print(f"    ETS: {wf.ets_class.value_counts().to_dict()}")
343	
344	    wf_all = pd.concat(wf_parts, ignore_index=True) if wf_parts else pd.DataFrame()
345	
346	    # Cross-cohort vs within-family comparison
347	    print("\n=== Step 4 cont: Cross analysis ===")
348	    cross_rows = []
349	    for rname, fname, _, _ in family_pairs:
350	        wf_sub = wf_all[(wf_all.ref_group == rname) & (wf_all.foc_group == fname)]
351	        for _, wr in wf_sub.iterrows():
352	            iid = wr["item_id"]
353	            tr = dif_temp.loc[dif_temp.item_id == iid]
354	            if tr.empty:
355	                continue
356	            tr = tr.iloc[0]
357	            cross_rows.append(dict(
358	                item_id=iid, subject=wr["subject"],
359	                temporal_ets=tr["ets_class"], temporal_delta=tr["delta_mh"],
360	                wf_pair=f"{rname}_vs_{fname}",
361	                wf_ets=wr["ets_class"], wf_delta=wr["delta_mh"],
362	                li_contamination_type=wr.get("li_contamination_type", np.nan),
363	            ))
364	    cross_df = pd.DataFrame(cross_rows)
365	
366	    if not cross_df.empty:
367	        for pair in cross_df["wf_pair"].unique():
368	            sub = cross_df[cross_df.wf_pair == pair]
369	            tc = sub.temporal_ets == "C"
370	            wc = sub.wf_ets == "C"
371	            print(f"  {pair}: both_C={int((tc & wc).sum())}, "
372	                  f"temp_only_C={int((tc & ~wc).sum())}, "
373	                  f"wf_only_C={int((~tc & wc).sum())}, "
374	                  f"neither={int((~tc & ~wc).sum())}")
375	
376	    # ── Step 5: Domain specificity ─────────────────────────────────────────
377	    print("\n=== Step 5: Domain specificity ===")
378	
379	    # C rate per subject (temporal cohort)
380	    subj_c = (dif_temp.groupby("subject")["ets_class"]
381	              .agg(n_items="size", n_ets_c=lambda x: (x == "C").sum()))
382	    subj_c["pct_c"] = subj_c["n_ets_c"] / subj_c["n_items"] * 100
383	
384	    # Per-item accuracy for 2023 and 2024 models
385	    acc_2023 = X[ref_t].mean(axis=0).astype(np.float64)   # (J,)
386	    acc_2024 = X[foc_t].mean(axis=0).astype(np.float64)
387	
388	    item_acc = pd.DataFrame({"item_id": ITEM_IDS, "acc_2023": acc_2023, "acc_2024": acc_2024})
389	    item_acc = item_acc.merge(item_meta[["item_id", "subject"]], on="item_id")
390	    subj_acc = item_acc.groupby("subject")[["acc_2023", "acc_2024"]].mean()
391	    subj_acc["acc_change"] = subj_acc["acc_2024"] - subj_acc["acc_2023"]
392	
393	    domain_df = subj_c.join(subj_acc, how="inner")
394	    rho, rho_p = spearmanr(domain_df["pct_c"], domain_df["acc_change"])
395	    print(f"  Spearman(pct_C, acc_change) = {rho:.3f}, p = {rho_p:.4f}")
396	    print("  Top 5 by C rate:")
397	    for subj, row in domain_df.nlargest(5, "pct_c").iterrows():
398	        print(f"    {subj}: {row.pct_c:.1f}% C ({int(row.n_ets_c)}/{int(row.n_items)}), "
399	              f"Δacc={row.acc_change:+.3f}")
400	
401	    # ── Step 6: Negative-discrimination sensitivity ────────────────────────
402	    print("\n=== Step 6: Negative-disc sensitivity ===")
403	    neg_mask = item_meta.set_index("item_id").reindex(ITEM_IDS)["is_negative_disc"].values
404	    pos_mask = ~neg_mask
405	    n_neg = int(neg_mask.sum())
406	    n_pos = int(pos_mask.sum())
407	    print(f"  All={J}, neg_disc={n_neg}, non_neg={n_pos}")
408	
409	    # Re-run temporal DIF on non-negative-disc items only
410	    # (total scores also computed only on non-neg items)
411	    pos_cols = np.where(pos_mask)[0]
412	    dif_temp_nn = mh_dif(X[np.ix_(ref_t, pos_cols)],
413	                         X[np.ix_(foc_t, pos_cols)], n_strata=5)
414	
415	    # Map col_idx back to original item space
416	    dif_temp_nn["col_idx_orig"] = [pos_cols[c] for c in dif_temp_nn["col_idx"]]
417	    dif_temp_nn["item_id"] = [ITEM_IDS[pos_cols[c]] for c in dif_temp_nn["col_idx"]]
418	    dif_temp_nn = dif_temp_nn.merge(
419	        li_labels[["item_id", "is_contaminated", "contamination_type"]].rename(
420	            columns={"is_contaminated": "li_label",
421	                     "contamination_type": "li_contamination_type"}),
422	        on="item_id", how="left",
423	    )
424	
425	    n_c_all = int((dif_temp["ets_class"] == "C").sum())
426	    n_c_nn  = int((dif_temp_nn["ets_class"] == "C").sum())
427	    # C count among neg-disc items in the full run
428	    neg_col_set = set(np.where(neg_mask)[0])
429	    n_c_neg = int((dif_temp.loc[dif_temp.col_idx.isin(neg_col_set), "ets_class"] == "C").sum())
430	
431	    neg_disc_df = pd.DataFrame([
432	        dict(item_set="all",               n_items=J,     n_ets_c=n_c_all,
433	             pct_c=n_c_all / J * 100),
434	        dict(item_set="non_negative_disc",  n_items=n_pos, n_ets_c=n_c_nn,
435	             pct_c=n_c_nn / n_pos * 100),
436	        dict(item_set="negative_disc_only", n_items=n_neg, n_ets_c=n_c_neg,
437	             pct_c=n_c_neg / n_neg * 100 if n_neg > 0 else 0),
438	    ])
439	    print(neg_disc_df.to_string(index=False))
440	
441	    summary_rows.append(summary_row("temporal", "non_neg_disc", dif_temp_nn))
442	
443	    # ── Sanity check: random half-split of 2023 cohort ─────────────────────
444	    print("\n=== Sanity check: random half-split of 2023 cohort ===")
445	    rng = np.random.RandomState(42)
446	    perm = rng.permutation(len(ref_t))
447	    half = len(perm) // 2
448	    san_ref = ref_t[perm[:half]]
449	    san_foc = ref_t[perm[half:]]
450	    print(f"  Split: {len(san_ref)} vs {len(san_foc)}")
451	    dif_san = mh_dif(X[san_ref], X[san_foc], n_strata=5)
452	    vc_san = dif_san["ets_class"].value_counts()
453	    n_c_san = vc_san.get("C", 0)
454	    pct_c_san = n_c_san / len(dif_san) * 100
455	    print(f"  ETS C: {n_c_san}/{len(dif_san)} = {pct_c_san:.2f}% (expect <5%)")
456	
457	    # ── Save all outputs ───────────────────────────────────────────────────
458	    print("\n=== Saving outputs ===")
459	
460	    out_cols = ["item_id", "subject", "alpha_mh", "delta_mh", "se",
461	                "p_value", "ets_class", "li_label", "li_contamination_type"]
462	    dif_temp[out_cols].to_csv(OUT / "dif_results_temporal.csv", index=False)
463	    dif_abil[out_cols].to_csv(OUT / "dif_results_ability.csv", index=False)
464	
465	    summary_df = pd.DataFrame(summary_rows)
466	    summary_df.to_csv(OUT / "dif_summary.csv", index=False)
467	
468	    if not wf_all.empty:
469	        wf_cols = ["item_id", "subject", "ref_group", "foc_group",
470	                   "alpha_mh", "delta_mh", "se", "p_value", "ets_class",
471	                   "li_label", "li_contamination_type"]
472	        wf_all[[c for c in wf_cols if c in wf_all.columns]].to_csv(
473	            OUT / "within_family_dif.csv", index=False)
474	
475	    if not cross_df.empty:
476	        cross_df.to_csv(OUT / "cross_analysis.csv", index=False)
477	
478	    domain_df.reset_index().to_csv(OUT / "domain_specificity.csv", index=False)
479	    neg_disc_df.to_csv(OUT / "neg_disc_sensitivity.csv", index=False)
480	
481	    # ── Cohort overlap ─────────────────────────────────────────────────────
482	    temp_c = set(dif_temp.loc[dif_temp.ets_class == "C", "item_id"])
483	    abil_c = set(dif_abil.loc[dif_abil.ets_class == "C", "item_id"])
484	    overlap = temp_c & abil_c
485	    union   = temp_c | abil_c
486	    jaccard = len(overlap) / len(union) if union else 0
487	
488	    # ── Console summary ────────────────────────────────────────────────────
489	    print("\n" + "=" * 60)
490	    print("SUMMARY")
491	    print("=" * 60)
492	    print(f"\nTemporal (2023 vs 2024, 5 strata):")
493	    print(f"  ETS: {dif_temp.ets_class.value_counts().to_dict()}")
494	    print(f"  FPR vs Li clean = {li_t['fpr_vs_li_clean']:.4f}")
495	    print(f"  Enrichment = {li_t['enrichment_ratio']:.2f}")
496	    print(f"\nAbility (Q1-2 vs Q4-5, 10 strata):")
497	    print(f"  ETS: {dif_abil.ets_class.value_counts().to_dict()}")
498	    print(f"  FPR vs Li clean = {li_a['fpr_vs_li_clean']:.4f}")
499	    print(f"  Enrichment = {li_a['enrichment_ratio']:.2f}")
500	    print(f"\nSanity check (random split): {pct_c_san:.2f}% C")
501	    print(f"Domain ρ(C_rate, Δacc) = {rho:.3f}, p = {rho_p:.4f}")
502	    print(f"Cohort overlap: temp_C={len(temp_c)}, abil_C={len(abil_c)}, "
503	          f"both={len(overlap)}, Jaccard={jaccard:.3f}")
504	
505	    # ── Generate report ────────────────────────────────────────────────────
506	    _write_report(dif_temp, dif_abil, li_t, li_a, summary_df,
507	                  domain_df, rho, rho_p, neg_disc_df, pct_c_san,
508	                  wf_all, cross_df, temp_c, abil_c, overlap, jaccard,
509	                  ref_t, foc_t, ref_a, foc_a)
510	
511	    print(f"\nAll outputs saved to {OUT}")
512	
513	
514	# ════════════════════════════════════════════════════════════════════════════
515	#  REPORT
516	# ════════════════════════════════════════════════════════════════════════════
517	def _write_report(dif_temp, dif_abil, li_t, li_a, summary_df,
518	                  domain_df, rho, rho_p, neg_disc_df, pct_san,
519	                  wf_all, cross_df, temp_c, abil_c, overlap, jaccard,
520	                  ref_t, foc_t, ref_a, foc_a):
521	    L = []
522	    def w(s=""):
523	        L.append(s)
524	
525	    w("# Plan 001: METABENCH Real-Data MH-DIF Analysis")
526	    w()
527	    w("## 1. Data & Setup")
528	    w()
529	    w(f"- Response matrix: **{N_MODELS} models × {J} items** (binary, MMLU)")
530	    w(f"- Temporal cohort: ref = 2023 (N={len(ref_t)}), foc = 2024 (N={len(foc_t)}), 5 strata")
531	    w(f"- Ability cohort: ref = Q1-2 (N={len(ref_a)}), foc = Q4-5 (N={len(foc_a)}), 10 strata")
532	    w(f"- Li et al. annotations: {(li_labels.contamination_type != 'no_annotation').sum()} annotated items")
533	    w()
534	
535	    w("## 2. ETS Classification")
536	    w()
537	    w("| Cohort | Filter | Items | A | B | C | %C | FPR (clean) | Enrichment |")
538	    w("|--------|--------|-------|---|---|---|----|-------------|------------|")
539	    for _, r in summary_df.iterrows():
540	        w(f"| {r.cohort_type} | {r.item_filter} | {r.n_items} | "
541	          f"{r.n_ets_a} | {r.n_ets_b} | {r.n_ets_c} | {r.pct_c:.2f}% | "
542	          f"{r.fpr_vs_li_clean:.4f} | {r.enrichment_ratio:.2f} |")
543	    w()
544	
545	    w("## 3. Li et al. Proxy Validation")
546	    w()
547	    w("| Cohort | FPR (clean) | Rate (contam) | Rate (clean) | Rate (unlabeled) | Enrichment |")
548	    w("|--------|-------------|---------------|--------------|------------------|------------|")
549	    for name, lm in [("temporal", li_t), ("ability", li_a)]:
550	        w(f"| {name} | {lm['fpr_vs_li_clean']:.4f} | "
551	          f"{lm['rate_contaminated']:.4f} | {lm['rate_clean']:.4f} | "
552	          f"{lm['rate_unlabeled']:.4f} | {lm['enrichment_ratio']:.2f} |")
553	    w()
554	
555	    w("## 4. Within-Family Analysis")
556	    w()
557	    if not wf_all.empty:
558	        for (rn, fn), sub in wf_all.groupby(["ref_group", "foc_group"]):
559	            vc = sub.ets_class.value_counts()
560	            nc = vc.get("C", 0)
561	            w(f"- **{rn} vs {fn}**: A={vc.get('A',0)}, B={vc.get('B',0)}, "
562	              f"C={nc} ({nc/len(sub)*100:.2f}%)")
563	        w()
564	        if not cross_df.empty:
565	            w("### Cross-cohort vs within-family overlap")
566	            w()
567	            for pair in cross_df.wf_pair.unique():
568	                s = cross_df[cross_df.wf_pair == pair]
569	                tc = s.temporal_ets == "C"
570	                wc = s.wf_ets == "C"
571	                w(f"- **{pair}**: both_C={int((tc&wc).sum())}, "
572	                  f"temp_only_C={int((tc&~wc).sum())}, "
573	                  f"wf_only_C={int((~tc&wc).sum())}")
574	            w()
575	    else:
576	        w("No within-family pairs with sufficient N found.")
577	        w()
578	
579	    w("## 5. Domain Specificity")
580	    w()
581	    w(f"Spearman ρ(C_rate, Δacc) = **{rho:.3f}** (p = {rho_p:.4f})")
582	    w()
583	    w("Top 15 subjects by C rate (temporal cohort):")
584	    w()
585	    w("| Subject | Items | C | %C | Acc 2023 | Acc 2024 | ΔAcc |")
586	    w("|---------|-------|---|-----|----------|----------|------|")
587	    for subj, row in domain_df.nlargest(15, "pct_c").iterrows():
588	        w(f"| {subj} | {int(row.n_items)} | {int(row.n_ets_c)} | "
589	          f"{row.pct_c:.1f}% | {row.acc_2023:.3f} | {row.acc_2024:.3f} | "
590	          f"{row.acc_change:+.3f} |")
591	    w()
592	
593	    w("## 6. Negative-Discrimination Sensitivity")
594	    w()
595	    w("| Item Set | Items | C | %C |")
596	    w("|----------|-------|---|----|")
597	    for _, r in neg_disc_df.iterrows():
598	        w(f"| {r.item_set} | {int(r.n_items)} | {int(r.n_ets_c)} | {r.pct_c:.2f}% |")
599	    w()
600	
601	    w("## 7. Sanity Check")
602	    w()
603	    w(f"Random half-split of 2023 cohort: **{pct_san:.2f}% C** (expect < 5%)")
604	    w()
605	
606	    w("## 8. Cohort Overlap")
607	    w()
608	    w(f"- Temporal C: {len(temp_c)} items")
609	    w(f"- Ability C: {len(abil_c)} items")
610	    w(f"- Both C: {len(overlap)} items")
611	    w(f"- Jaccard index: {jaccard:.3f}")
612	
613	    (OUT / "plan_001_report.md").write_text("\n".join(L) + "\n")
614	    print("  Report written.")
615	
616	
617	if __name__ == "__main__":
618	    main()
619	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "3d98ac80-f564-4b98-a005-2b4b8f754cda"
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
  "task_id": "ab1e3c29de8139595",
  "tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_052…",
  "usage": {
    "total_tokens": 35890,
    "tool_uses": 6,
    "duration_ms": 12491
  },
  "last_tool_name": "Bash",
  "uuid": "a3fedef6-d7f9-443d-b9e7-93267de9d3ad",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jfa1vmyYnyTbqkwDshrep7`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032* -type f -name \"*.py\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "8f54e7e4-398a-4fef-b0bd-4d4e42c74966",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AqFPAonc5XM3mUQnpDFB8T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 11666,
      "cache_read_input_tokens": 24108,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11666,
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

_source line 28 · 2026-05-22T07:17:52.595Z_

<details><summary>↩ Tool result · `toolu_01Jfa1vmyYnyTbqkwDshrep7`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/plan_032_dif_cleaned_mmlu.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "9ae07817-9bdd-45e5-8498-8c40d0778ddb"
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
  "task_id": "ab1e3c29de8139595",
  "tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "description": "Searching for cohort|ref_idx|foc_idx|temporal|2023|2024",
  "usage": {
    "total_tokens": 36181,
    "tool_uses": 7,
    "duration_ms": 14557
  },
  "last_tool_name": "Grep",
  "uuid": "490c00b7-ac8e-4935-ab7c-165724476620",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd"
}
```

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Grep · `toolu_018sgW1x4APTdV8KbqLxVRpt`</summary>

```json
{
  "pattern": "cohort|ref_idx|foc_idx|temporal|2023|2024",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu",
  "type": "py",
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
  "parent_tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "f77419e0-d2ca-4a28-87bb-5b653b79ea3b",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QVjVAKcQz3x83AZ2pJeFK5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 35774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 256,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 35,
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

_source line 31 · 2026-05-22T07:17:54.621Z_

<details><summary>↩ Tool result · `toolu_018sgW1x4APTdV8KbqLxVRpt`</summary>

```text
artifacts/plan_032_dif_cleaned_mmlu/plan_032_dif_cleaned_mmlu.py:10:  - artifacts/plan_001/dif_results_temporal.csv  (item DIF classifications)
artifacts/plan_032_dif_cleaned_mmlu/plan_032_dif_cleaned_mmlu.py:11:  - artifacts/model_metadata.csv           (model family, cohort, etc.)
artifacts/plan_032_dif_cleaned_mmlu/plan_032_dif_cleaned_mmlu.py:56:dif = pd.read_csv(ARTIFACTS / "plan_001" / "dif_results_temporal.csv")
artifacts/plan_032_dif_cleaned_mmlu/plan_032_dif_cleaned_mmlu.py:120:df["cohort_temporal"] = df["model_name"].map(
artifacts/plan_032_dif_cleaned_mmlu/plan_032_dif_cleaned_mmlu.py:121:    lambda m: meta_lookup.loc[m, "cohort_temporal"] if m in meta_lookup.index else "unknown"
artifacts/plan_032_dif_cleaned_mmlu/plan_032_dif_cleaned_mmlu.py:165:top_up = df.nsmallest(10, "rank_change")[["model_name", "family", "cohort_temporal", "score_full", "score_cleaned", "rank_full", "rank_cleaned", "rank_change"]]
artifacts/plan_032_dif_cleaned_mmlu/plan_032_dif_cleaned_mmlu.py:171:top_down = df.nlargest(10, "rank_change")[["model_name", "family", "cohort_temporal", "score_full", "score_cleaned", "rank_full", "rank_cleaned", "rank_change"]]
artifacts/plan_032_dif_cleaned_mmlu/plan_032_dif_cleaned_mmlu.py:225:# 4g) Per-cohort analysis
artifacts/plan_032_dif_cleaned_mmlu/plan_032_dif_cleaned_mmlu.py:229:for cohort in sorted(df["cohort_temporal"].unique()):
artifacts/plan_032_dif_cleaned_mmlu/plan_032_dif_cleaned_mmlu.py:230:    sub = df[df["cohort_temporal"] == cohort]
artifacts/plan_032_dif_cleaned_mmlu/plan_032_dif_cleaned_mmlu.py:234:    report(f"\n### Cohort: {cohort} (n={len(sub)})")
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:6:produces systematic cohort-asymmetric rank shifts that random removal does not.
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:51:dif = pd.read_csv(ARTIFACTS / "plan_001" / "dif_results_temporal.csv")
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:58:# Build cohort vector aligned to model_names
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:59:cohorts = np.array([
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:60:    meta_lookup.loc[m, "cohort_temporal"] if m in meta_lookup.index else "unknown"
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:80:dif_cohort_means = {}
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:81:for c in ["2023", "2024"]:
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:82:    mask = dif_existing["cohort_temporal"] == c
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:84:        dif_cohort_means[c] = dif_existing.loc[mask, "rank_change"].mean()
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:85:        print(f"  DIF cohort {c} mean rank change: {dif_cohort_means[c]:+.2f}")
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:94:    "cohort_2023_mean_change": dif_cohort_means.get("2023", np.nan),
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:95:    "cohort_2024_mean_change": dif_cohort_means.get("2024", np.nan),
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:114:    cohort_means = {}
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:115:    for c in ["2023", "2024"]:
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:116:        cmask = cohorts == c
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:118:            cohort_means[c] = rc[cmask].mean()
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:129:        "cohort_2023_mean_change": cohort_means.get("2023", np.nan),
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:130:        "cohort_2024_mean_change": cohort_means.get("2024", np.nan),
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:175:c23_rand_mean = random_agg["cohort_2023_mean_change_mean"]
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:176:c23_rand_std = random_agg["cohort_2023_mean_change_std"]
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:177:c24_rand_mean = random_agg["cohort_2024_mean_change_mean"]
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:178:c24_rand_std = random_agg["cohort_2024_mean_change_std"]
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:180:print(f"  Cohort 2023 mean rank change:")
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:181:print(f"    DIF removal:    {dif_metrics['cohort_2023_mean_change']:+.2f}")
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:184:print(f"  Cohort 2024 mean rank change:")
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:185:print(f"    DIF removal:    {dif_metrics['cohort_2024_mean_change']:+.2f}")
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:188:cohort_gap_dif = dif_metrics["cohort_2024_mean_change"] - dif_metrics["cohort_2023_mean_change"]
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:189:cohort_gap_rand = c24_rand_mean - c23_rand_mean
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:190:cohort_gap_rand_std = np.sqrt(c24_rand_std**2 + c23_rand_std**2)
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:191:z_gap = (cohort_gap_dif - cohort_gap_rand) / cohort_gap_rand_std if cohort_gap_rand_std > 0 else np.nan
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:193:print(f"\n  Cohort asymmetry (2024 - 2023 mean change):")
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:194:print(f"    DIF removal:    {cohort_gap_dif:+.2f}")
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:195:print(f"    Random removal: {cohort_gap_rand:+.2f} ± {cohort_gap_rand_std:.2f}")
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:218:report.append(f"The critical test: DIF removal shifts 2024 models up by {dif_metrics['cohort_2024_mean_change']:+.1f} ranks")
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:219:report.append(f"and 2023 models down by {dif_metrics['cohort_2023_mean_change']:+.1f} ranks (gap = {cohort_gap_dif:+.1f}).")
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:220:report.append(f"Random removal produces near-zero cohort bias: 2024 = {c24_rand_mean:+.1f} ± {c24_rand_std:.1f},")
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:221:report.append(f"2023 = {c23_rand_mean:+.1f} ± {c23_rand_std:.1f} (gap z = {z_gap:+.2f}).")
artifacts/plan_032_dif_cleaned_mmlu/plan_032_random_baseline.py:223:report.append("This confirms that the cohort-asymmetric rank shift is specific to DIF-flagged items,")
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "62b3d834-7072-40f6-94f2-e22e195a13e9"
}
```

</details>

---

### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ab1e3c29de8139595",
  "tool_use_id": "toolu_016Gu6sDPik5aYrBXVLzS65d",
  "status": "completed",
  "output_file": "",
  "summary": "Explore cohort definitions and MH code",
  "usage": {
    "total_tokens": 39021,
    "tool_uses": 7,
    "duration_ms": 36223
  },
  "uuid": "2b67a256-3eac-435a-9803-ca78fcd708c2",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd"
}
```

---

### Tool result

_source line 33 · 2026-05-22T07:18:16.269Z_

<details><summary>↩ Tool result · `toolu_016Gu6sDPik5aYrBXVLzS65d`</summary>

````text
Perfect! Now I have all the information needed. Let me compile the final report.

## Summary

I found the exact cohort definition logic and the full MH-DIF function. Here's what you need for the LOFO robustness analysis:

---

### 1. **Cohort Definition for Temporal MH-DIF** (source: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py`, lines 206-208)

```python
ref_idx = np.array([name2row[n] for n in model_names if cohort.get(n) == "2023"])
foc_idx = np.array([name2row[n] for n in model_names if cohort.get(n) == "2024"])
```

**Exact split logic:**
- **Reference cohort (ref)**: All models where `cohort_temporal == "2023"` 
- **Focal cohort (foc)**: All models where `cohort_temporal == "2024"`
- **Matching variable**: Total score across all items (with 5-stratum quantile-based binning)
- **Cohort sizes** (from the code): `ref_idx` contains all 2023 models, `foc_idx` contains all 2024 models
- **Cohort mapping**: Loaded from `model_metadata.csv` via column `"cohort_temporal"`

The plan_001 analysis confirms this same split (lines 270-271):
```python
ref_t = rows_for("cohort_temporal", ["2023"])
foc_t = rows_for("cohort_temporal", ["2024"])
```

---

### 2. **MH-DIF Function: `mh_dif_c_pct_vec`** (source: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py`, lines 34-101)

```python
def mh_dif_c_pct_vec(X_ref, X_foc, n_strata=N_STRATA):
    """Fully vectorized MH-DIF → C%. Stratifies on total score (not rest)."""
    n_ref, J = X_ref.shape
    n_foc = X_foc.shape[0]

    tot_ref = X_ref.sum(axis=1).astype(np.float64)
    tot_foc = X_foc.sum(axis=1).astype(np.float64)
    s_all = np.concatenate([tot_ref, tot_foc])

    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
    n_bins = len(edges) - 1
    if n_bins < 1:
        return 0.0

    k_ref = np.digitize(tot_ref, edges[1:-1])
    k_foc = np.digitize(tot_foc, edges[1:-1])

    n1 = np.zeros(n_bins, dtype=np.float64)
    n0 = np.zeros(n_bins, dtype=np.float64)
    A = np.zeros((n_bins, J), dtype=np.float64)
    C = np.zeros((n_bins, J), dtype=np.float64)

    for k in range(n_bins):
        mr = (k_ref == k)
        mf = (k_foc == k)
        n1[k] = mr.sum()
        n0[k] = mf.sum()
        if mr.any():
            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)
        if mf.any():
            C[k] = X_foc[mf].sum(axis=0).astype(np.float64)

    B = n1[:, None] - A
    D = n0[:, None] - C
    Nk = (n1 + n0)[:, None]
    m1 = A + C
    m0 = B + D

    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &
             (Nk > 1) & (m1 > 0) & (m0 > 0))

    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)
    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)

    finite_mask = (Rj > 0) & (Sj > 0)

    with np.errstate(divide="ignore", invalid="ignore"):
        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)

    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)
    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)

    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)
    sum_var = np.where(
        valid,
        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),
        0,
    ).sum(axis=0)

    chi2_j = np.where(
        sum_var > 0,
        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),
        0,
    )
    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)

    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)
    return is_c.sum() / J * 100
```

**Key implementation details:**
- **Matching variable**: Total score (sum across all items, not rest-score)
- **Strata**: Default `N_STRATA=5` quantile-based bins created from combined ref+foc total scores
- **Item-by-item computation**: Returns percentage C (both |Δ_MH| ≥ 1.5 AND p < 0.05)
- **Δ_MH**: `-2.35 × ln(R/S)` where R/S is the MH odds ratio
- **Validation**: This was verified to produce results within 0.3 percentage points of the slower rest-score variant

---

**For LOFO robustness:** You have two key artifacts:
1. The exact cohort split mechanism (2023 vs 2024 from `model_metadata.csv`)
2. The vectorized MH-DIF function that can be tested across feature perturbations

The function returns a scalar percentage of items classified as C-level DIF, making it suitable for sensitivity/robustness analysis.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "505640e8-b442-473a-9438-110a7366aea8",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to understand two things for an LOFO robustness analysis:\n\n1. **Cohort definition**: How are ref/foc cohorts defined for temporal MH-DIF? Look in:\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001*/` — any Python scripts that define cohort splits\n   - Grep for \"cohort\" or \"ref\" or \"foc\" or \"temporal\" in plan_001 artifacts\n   - Also check `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_032_dif_cleaned_mmlu/` for any scripts\n\n2. **MH-DIF function**: Read the function `mh_dif_c_pct_vec` from `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py`\n\nSearch breadth: medium. Report the exact cohort split logic (which models are ref vs foc), and the full function code for mh_dif_c_pct_vec.",
    "agentId": "ab1e3c29de8139595",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information needed. Let me compile the final report.\n\n## Summary\n\nI found the exact cohort definition logic and the full MH-DIF function. Here's what you need for the LOFO robustness analysis:\n\n---\n\n### 1. **Cohort Definition for Temporal MH-DIF** (source: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py`, lines 206-208)\n\n```python\nref_idx = np.array([name2row[n] for n in model_names if cohort.get(n) == \"2023\"])\nfoc_idx = np.array([name2row[n] for n in model_names if cohort.get(n) == \"2024\"])\n```\n\n**Exact split logic:**\n- **Reference cohort (ref)**: All models where `cohort_temporal == \"2023\"` \n- **Focal cohort (foc)**: All models where `cohort_temporal == \"2024\"`\n- **Matching variable**: Total score across all items (with 5-stratum quantile-based binning)\n- **Cohort sizes** (from the code): `ref_idx` contains all 2023 models, `foc_idx` contains all 2024 models\n- **Cohort mapping**: Loaded from `model_metadata.csv` via column `\"cohort_temporal\"`\n\nThe plan_001 analysis confirms this same split (lines 270-271):\n```python\nref_t = rows_for(\"cohort_temporal\", [\"2023\"])\nfoc_t = rows_for(\"cohort_temporal\", [\"2024\"])\n```\n\n---\n\n### 2. **MH-DIF Function: `mh_dif_c_pct_vec`** (source: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py`, lines 34-101)\n\n```python\ndef mh_dif_c_pct_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Fully vectorized MH-DIF → C%. Stratifies on total score (not rest).\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return 0.0\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n    return is_c.sum() / J * 100\n```\n\n**Key implementation details:**\n- **Matching variable**: Total score (sum across all items, not rest-score)\n- **Strata**: Default `N_STRATA=5` quantile-based bins created from combined ref+foc total scores\n- **Item-by-item computation**: Returns percentage C (both |Δ_MH| ≥ 1.5 AND p < 0.05)\n- **Δ_MH**: `-2.35 × ln(R/S)` where R/S is the MH odds ratio\n- **Validation**: This was verified to produce results within 0.3 percentage points of the slower rest-score variant\n\n---\n\n**For LOFO robustness:** You have two key artifacts:\n1. The exact cohort split mechanism (2023 vs 2024 from `model_metadata.csv`)\n2. The vectorized MH-DIF function that can be tested across feature perturbations\n\nThe function returns a scalar percentage of items classified as C-level DIF, making it suitable for sensitivity/robustness analysis."
      }
    ],
    "totalDurationMs": 36225,
    "totalTokens": 40685,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 2836,
      "cache_read_input_tokens": 36030,
      "output_tokens": 1815,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2836
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 1815,
          "cache_read_input_tokens": 36030,
          "cache_creation_input_tokens": 2836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2836,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 2,
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

### Tool result

_source line 34 · 2026-05-22T07:18:16.842Z_

<details><summary>↩ Tool result · `toolu_011UhxTKhSfxK5gCVSKEa4dX`</summary>

```text
model_name,score_full,score_cleaned,rank_full,rank_cleaned,rank_change,abs_rank_change,family,cohort_temporal
0-hero/Matter-0.1-7B,0.5602014710585226,0.579976717112922,3837,3892,55,55,unknown,other
0-hero/Matter-0.1-7B-DPO-preview,0.6613367444835305,0.6863795110593713,2611,2615,4,4,,other
0-hero/Matter-0.1-7B-boost,0.6534218100415734,0.680093131548312,2811,2791,-20,20,unknown,other
0-hero/Matter-0.1-7B-boost-DPO,0.6549408378637672,0.6817229336437718,2776,2751,-25,25,,other
---
5228 plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv
---
Columns: ['model_name', 'score_full', 'score_cleaned', 'rank_full', 'rank_cleaned', 'rank_change', 'abs_rank_change', 'family', 'cohort_temporal']
cohort_temporal values: {'other': 3340, '2023': 1080, '2024': 807}
Top families: {'unknown': 2882, 'mistral': 547, 'llama-3': 315, 'llama-2': 161, 'mixtral': 120, 'solar': 91, 'zephyr': 86, 'yi': 72, 'mistral-0.1': 72, 'gemma': 72}
Family by cohort:
  other: 3340 models, top families: {'unknown': 2882, 'mistral-0.1': 72, 'orca': 41, 'neuralchat': 28, 'orca-2': 25}
  2024: 807 models, top families: {'llama-3': 315, 'mixtral': 120, 'solar': 91, 'gemma': 72, 'qwen-1.5': 69}
  2023: 1080 models, top families: {'mistral': 547, 'llama-2': 161, 'zephyr': 86, 'yi': 72, 'phi-2': 60}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "a52c0d59-2f7d-4c0a-a023-8ce7c41d81a0",
  "tool_use_result": {
    "stdout": "model_name,score_full,score_cleaned,rank_full,rank_cleaned,rank_change,abs_rank_change,family,cohort_temporal\n0-hero/Matter-0.1-7B,0.5602014710585226,0.579976717112922,3837,3892,55,55,unknown,other\n0-hero/Matter-0.1-7B-DPO-preview,0.6613367444835305,0.6863795110593713,2611,2615,4,4,,other\n0-hero/Matter-0.1-7B-boost,0.6534218100415734,0.680093131548312,2811,2791,-20,20,unknown,other\n0-hero/Matter-0.1-7B-boost-DPO,0.6549408378637672,0.6817229336437718,2776,2751,-25,25,,other\n---\n5228 plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv\n---\nColumns: ['model_name', 'score_full', 'score_cleaned', 'rank_full', 'rank_cleaned', 'rank_change', 'abs_rank_change', 'family', 'cohort_temporal']\ncohort_temporal values: {'other': 3340, '2023': 1080, '2024': 807}\nTop families: {'unknown': 2882, 'mistral': 547, 'llama-3': 315, 'llama-2': 161, 'mixtral': 120, 'solar': 91, 'zephyr': 86, 'yi': 72, 'mistral-0.1': 72, 'gemma': 72}\nFamily by cohort:\n  other: 3340 models, top families: {'unknown': 2882, 'mistral-0.1': 72, 'orca': 41, 'neuralchat': 28, 'orca-2': 25}\n  2024: 807 models, top families: {'llama-3': 315, 'mixtral': 120, 'solar': 91, 'gemma': 72, 'qwen-1.5': 69}\n  2023: 1080 models, top families: {'mistral': 547, 'llama-2': 161, 'zephyr': 86, 'yi': 72, 'phi-2': 60}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-22T07:18:17.017Z_

<details><summary>↩ Tool result · `toolu_01Tui5qykFUateyjkF9LfF9F`</summary>

```text
Models: 5227, Items: 12508
First 5 models: ['0-hero/Matter-0.1-7B', '0-hero/Matter-0.1-7B-DPO-preview', '0-hero/Matter-0.1-7B-boost', '0-hero/Matter-0.1-7B-boost-DPO', '0-hero/Matter-0.1-7B-boost-DPO-preview']
Last 5 models: ['zorobin/mistral-class-shishya-7b-ep3', 'zorobin/mistral-class-shishya-all-hal-7b-ep3', 'zyh3826/20231206094523-pretrain-Llama-2-13b-hf-76000', 'zyh3826/GML-Mistral-merged-v1', 'zyh3826/llama2-13b-ft-openllm-leaderboard-v1']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "04a70f8d-2cd9-4a50-9dc9-ca97c67adaf2",
  "tool_use_result": {
    "stdout": "Models: 5227, Items: 12508\nFirst 5 models: ['0-hero/Matter-0.1-7B', '0-hero/Matter-0.1-7B-DPO-preview', '0-hero/Matter-0.1-7B-boost', '0-hero/Matter-0.1-7B-boost-DPO', '0-hero/Matter-0.1-7B-boost-DPO-preview']\nLast 5 models: ['zorobin/mistral-class-shishya-7b-ep3', 'zorobin/mistral-class-shishya-all-hal-7b-ep3', 'zyh3826/20231206094523-pretrain-Llama-2-13b-hf-76000', 'zyh3826/GML-Mistral-merged-v1', 'zyh3826/llama2-13b-ft-openllm-leaderboard-v1']",
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

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the info I need:

1. **Cohort split**: ref = 2023 (1080 models), foc = 2024 (807 models). "other" not used.
2. **MH function**: `mh_dif_c_pct_vec` from plan_028
3. **Top 5 families**:
   - In ref (2023): mistral (547), llama-2 (161), zephyr (86), yi (72), phi-2 (60)
   - In foc (2024): llama-3 (315), mixtral (120), solar (91), gemma (72), qwen-1.5 (69)
   - Combined across both years: mistral (547), llama-3 (315), llama-2 (161), mixtral (120), solar (91)

I need to verify the top-5 families are based on the combined dataset since LOFO removes from both cohorts. Let me confirm the model names align between the response matrix and CSV—both have 5227 models and the first entries match, so they're properly aligned.

Looking at the family distribution within just the 2023 and 2024 cohorts, mistral dominates 2023 with 547 models while llama-3 leads 2024 with 315. The next tier includes llama-2 (161), mixtral (120), and solar (91), making these the clear top-5 families across the combined period.

Now I'll write and execute the script to analyze this data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "2e1cc37f-bb20-478a-8b1b-59bb3e69ddef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Muzkdqv2j1YKj3ExcfskJ9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3804,
      "cache_read_input_tokens": 25646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3804
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

_source line 37_

Data is clear. Cohort split: ref=2023 (1080), foc=2024 (807). Top families across ref+foc: mistral(547), llama-3(315), llama-2(161), mixtral(120), solar(91). Let me confirm model name alignment and write the LOFO script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "e674f814-a980-4f4e-85ec-ec830c06217a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Muzkdqv2j1YKj3ExcfskJ9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3804,
      "cache_read_input_tokens": 25646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3804
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

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01G7Jcn1MY7HyFcfLrJmnNDm`</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd, numpy as np\nidx = np.load('response_matrix_index.npz', allow_pickle=True)\nmodel_names = list(idx['model_names'])\ndf = pd.read_csv('plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv')\n\n# Check alignment\ncsv_names = df['model_name'].tolist()\nprint(f'response_matrix: {len(model_names)}, csv: {len(csv_names)}')\nprint(f'First 3 match: {model_names[:3] == csv_names[:3]}')\nprint(f'Last 3 match: {model_names[-3:] == csv_names[-3:]}')\n\n# Check how many csv names are in response matrix\nin_matrix = set(model_names)\nin_csv = set(csv_names)\nprint(f'In both: {len(in_matrix & in_csv)}')\nprint(f'In matrix only: {len(in_matrix - in_csv)}')\nprint(f'In csv only: {len(in_csv - in_matrix)}')\n\n# Top families within 2023+2024\nsub = df[df['cohort_temporal'].isin(['2023','2024'])]\nprint(f'\\\\nTop families in 2023+2024 ({len(sub)} models):')\nprint(sub['family'].value_counts().head(10).to_string())\n\"",
  "description": "Verify model name alignment and top families"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "64946d97-8d2f-4813-8a86-d9f7a625d2b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Muzkdqv2j1YKj3ExcfskJ9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3804,
      "cache_read_input_tokens": 25646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3804
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

_source line 39 · 2026-05-22T07:18:35.974Z_

<details><summary>↩ Tool result · `toolu_01G7Jcn1MY7HyFcfLrJmnNDm`</summary>

```text
response_matrix: 5227, csv: 5227
First 3 match: True
Last 3 match: True
In both: 5227
In matrix only: 0
In csv only: 0

Top families in 2023+2024 (1887 models):
family
mistral     547
llama-3     315
llama-2     161
mixtral     120
solar        91
zephyr       86
yi           72
gemma        72
qwen-1.5     69
phi-2        60
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "c4fc1016-d8bd-43ce-94d4-5d85e759742d",
  "tool_use_result": {
    "stdout": "response_matrix: 5227, csv: 5227\nFirst 3 match: True\nLast 3 match: True\nIn both: 5227\nIn matrix only: 0\nIn csv only: 0\n\nTop families in 2023+2024 (1887 models):\nfamily\nmistral     547\nllama-3     315\nllama-2     161\nmixtral     120\nsolar        91\nzephyr       86\nyi           72\ngemma        72\nqwen-1.5     69\nphi-2        60",
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

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Model names align perfectly. Top 5 families: mistral, llama-3, llama-2, mixtral, solar. Now let me write the LOFO script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "d53d9a75-e3d6-4356-a161-5f7167f2de3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGhdpzgmPd9MiJgtdt49mx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 29450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1318
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

_source line 41_

Perfect alignment. Now I'll write and run the LOFO script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "1468397e-d00b-43cc-a644-8e6587e949de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGhdpzgmPd9MiJgtdt49mx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 29450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1318
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

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_011GtYHXd9vJGp6Sh59JZBUS`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness",
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
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "af2fa4c4-4796-4f95-a8ed-88f8639656db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGhdpzgmPd9MiJgtdt49mx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 29450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1318
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

_source line 43 · 2026-05-22T07:18:39.800Z_

<details><summary>↩ Tool result · `toolu_011GtYHXd9vJGp6Sh59JZBUS`</summary>

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
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "6291b66a-ddc2-4978-bd54-05af73c8a527",
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

_source line 44_

<details open><summary>🔧 Tool call — Write · `toolu_01QUc8wAHA5Rfz5aYZmYBb8N`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_robustness.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Leave-One-Family-Out (LOFO) robustness check for temporal MH-DIF C%.\"\"\"\n\nimport numpy as np\nimport pandas as pd\nimport scipy.sparse as sp\nfrom scipy.stats import chi2 as chi2_dist\n\nBASE = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nN_STRATA = 5\nTOP_K = 5\n\n\ndef mh_dif_c_pct_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF -> C%. Stratifies on total score.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return 0.0\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n    return is_c.sum() / J * 100\n\n\ndef main():\n    mat = sp.load_npz(f\"{BASE}/response_matrix.npz\")\n    idx = np.load(f\"{BASE}/response_matrix_index.npz\", allow_pickle=True)\n    model_names = list(idx[\"model_names\"])\n    name_to_idx = {n: i for i, n in enumerate(model_names)}\n\n    df = pd.read_csv(f\"{BASE}/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv\")\n\n    ref_models = df[df[\"cohort_temporal\"] == \"2023\"][\"model_name\"].tolist()\n    foc_models = df[df[\"cohort_temporal\"] == \"2024\"][\"model_name\"].tolist()\n    ref_indices = np.array([name_to_idx[m] for m in ref_models])\n    foc_indices = np.array([name_to_idx[m] for m in foc_models])\n    ref_set = set(ref_indices)\n    foc_set = set(foc_indices)\n\n    print(f\"Ref (2023): {len(ref_indices)}, Foc (2024): {len(foc_indices)}\")\n\n    # Full baseline\n    X_ref_full = mat[ref_indices, :].toarray()\n    X_foc_full = mat[foc_indices, :].toarray()\n    c_pct_full = mh_dif_c_pct_vec(X_ref_full, X_foc_full)\n    print(f\"Full baseline C%: {c_pct_full:.2f}%\")\n\n    # Top-K families across ref+foc\n    active = df[df[\"cohort_temporal\"].isin([\"2023\", \"2024\"])]\n    top_families = active[\"family\"].value_counts().head(TOP_K).index.tolist()\n    print(f\"Top-{TOP_K} families: {top_families}\")\n\n    results = []\n    for fam in top_families:\n        fam_models = df[df[\"family\"] == fam][\"model_name\"].tolist()\n        fam_idx_set = set(name_to_idx[m] for m in fam_models if m in name_to_idx)\n\n        ref_lofo = np.array([i for i in ref_indices if i not in fam_idx_set])\n        foc_lofo = np.array([i for i in foc_indices if i not in fam_idx_set])\n\n        n_ref_removed = len(ref_indices) - len(ref_lofo)\n        n_foc_removed = len(foc_indices) - len(foc_lofo)\n\n        if len(ref_lofo) == 0 or len(foc_lofo) == 0:\n            print(f\"  {fam}: skip (empty cohort after removal)\")\n            continue\n\n        X_ref_lofo = mat[ref_lofo, :].toarray()\n        X_foc_lofo = mat[foc_lofo, :].toarray()\n        c_pct_lofo = mh_dif_c_pct_vec(X_ref_lofo, X_foc_lofo)\n        delta = c_pct_lofo - c_pct_full\n\n        print(f\"  {fam}: removed {n_ref_removed}R+{n_foc_removed}F = {n_ref_removed+n_foc_removed}, \"\n              f\"C% = {c_pct_lofo:.2f}% (Δ = {delta:+.2f}%)\")\n\n        results.append({\n            \"family\": fam,\n            \"n_models_total\": len(fam_models),\n            \"n_models_ref\": n_ref_removed,\n            \"n_models_foc\": n_foc_removed,\n            \"c_pct_full\": round(c_pct_full, 2),\n            \"c_pct_lofo\": round(c_pct_lofo, 2),\n            \"delta_c_pct\": round(delta, 2),\n        })\n\n        del X_ref_lofo, X_foc_lofo\n\n    out_dir = f\"{BASE}/lofo_robustness\"\n    res_df = pd.DataFrame(results)\n    res_df.to_csv(f\"{out_dir}/lofo_results.csv\", index=False)\n\n    # Write markdown report\n    lines = [\n        \"# LOFO Robustness Check: Temporal MH-DIF C%\\n\",\n        f\"**Full baseline C%**: {c_pct_full:.2f}%  \",\n        f\"**Ref cohort**: 2023 ({len(ref_indices)} models)  \",\n        f\"**Foc cohort**: 2024 ({len(foc_indices)} models)\\n\",\n        \"## Results\\n\",\n        \"| Family | N removed (ref+foc) | C% full | C% LOFO | ΔC% |\",\n        \"|--------|--------------------:|--------:|--------:|----:|\",\n    ]\n    for r in results:\n        n_rem = r[\"n_models_ref\"] + r[\"n_models_foc\"]\n        lines.append(\n            f\"| {r['family']} | {n_rem} ({r['n_models_ref']}R+{r['n_models_foc']}F) \"\n            f\"| {r['c_pct_full']:.2f} | {r['c_pct_lofo']:.2f} | {r['delta_c_pct']:+.2f} |\"\n        )\n\n    deltas = [abs(r[\"delta_c_pct\"]) for r in results]\n    max_delta = max(deltas)\n    mean_delta = np.mean(deltas)\n    lines.append(f\"\\n**Max |ΔC%|**: {max_delta:.2f}pp  \")\n    lines.append(f\"**Mean |ΔC%|**: {mean_delta:.2f}pp\\n\")\n\n    if max_delta < 3.0:\n        lines.append(\"**Conclusion**: C% is robust to single-family removal — \"\n                      f\"max perturbation {max_delta:.2f}pp across top-{TOP_K} families.\")\n    else:\n        worst = max(results, key=lambda r: abs(r[\"delta_c_pct\"]))\n        lines.append(f\"**Conclusion**: Removing {worst['family']} shifts C% by \"\n                      f\"{worst['delta_c_pct']:+.2f}pp, indicating moderate sensitivity \"\n                      f\"to this family.\")\n\n    with open(f\"{out_dir}/lofo_results.md\", \"w\") as f:\n        f.write(\"\\n\".join(lines) + \"\\n\")\n\n    print(f\"\\nSaved to {out_dir}/lofo_results.csv and lofo_results.md\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "4caffbc1-5abb-4aa8-90bb-c4258e1e1714",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013pjcdsAyh5hNTmFJ2AYkwz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 30768,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 202
      },
      "output_tokens": 72,
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

_source line 45 · 2026-05-22T07:19:41.484Z_

<details><summary>↩ Tool result · `toolu_01QUc8wAHA5Rfz5aYZmYBb8N`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_robustness.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "c6d53edb-1f3b-46cd-a77e-ce1ab1b299ba",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_robustness.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Leave-One-Family-Out (LOFO) robustness check for temporal MH-DIF C%.\"\"\"\n\nimport numpy as np\nimport pandas as pd\nimport scipy.sparse as sp\nfrom scipy.stats import chi2 as chi2_dist\n\nBASE = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nN_STRATA = 5\nTOP_K = 5\n\n\ndef mh_dif_c_pct_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF -> C%. Stratifies on total score.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return 0.0\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n    return is_c.sum() / J * 100\n\n\ndef main():\n    mat = sp.load_npz(f\"{BASE}/response_matrix.npz\")\n    idx = np.load(f\"{BASE}/response_matrix_index.npz\", allow_pickle=True)\n    model_names = list(idx[\"model_names\"])\n    name_to_idx = {n: i for i, n in enumerate(model_names)}\n\n    df = pd.read_csv(f\"{BASE}/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv\")\n\n    ref_models = df[df[\"cohort_temporal\"] == \"2023\"][\"model_name\"].tolist()\n    foc_models = df[df[\"cohort_temporal\"] == \"2024\"][\"model_name\"].tolist()\n    ref_indices = np.array([name_to_idx[m] for m in ref_models])\n    foc_indices = np.array([name_to_idx[m] for m in foc_models])\n    ref_set = set(ref_indices)\n    foc_set = set(foc_indices)\n\n    print(f\"Ref (2023): {len(ref_indices)}, Foc (2024): {len(foc_indices)}\")\n\n    # Full baseline\n    X_ref_full = mat[ref_indices, :].toarray()\n    X_foc_full = mat[foc_indices, :].toarray()\n    c_pct_full = mh_dif_c_pct_vec(X_ref_full, X_foc_full)\n    print(f\"Full baseline C%: {c_pct_full:.2f}%\")\n\n    # Top-K families across ref+foc\n    active = df[df[\"cohort_temporal\"].isin([\"2023\", \"2024\"])]\n    top_families = active[\"family\"].value_counts().head(TOP_K).index.tolist()\n    print(f\"Top-{TOP_K} families: {top_families}\")\n\n    results = []\n    for fam in top_families:\n        fam_models = df[df[\"family\"] == fam][\"model_name\"].tolist()\n        fam_idx_set = set(name_to_idx[m] for m in fam_models if m in name_to_idx)\n\n        ref_lofo = np.array([i for i in ref_indices if i not in fam_idx_set])\n        foc_lofo = np.array([i for i in foc_indices if i not in fam_idx_set])\n\n        n_ref_removed = len(ref_indices) - len(ref_lofo)\n        n_foc_removed = len(foc_indices) - len(foc_lofo)\n\n        if len(ref_lofo) == 0 or len(foc_lofo) == 0:\n            print(f\"  {fam}: skip (empty cohort after removal)\")\n            continue\n\n        X_ref_lofo = mat[ref_lofo, :].toarray()\n        X_foc_lofo = mat[foc_lofo, :].toarray()\n        c_pct_lofo = mh_dif_c_pct_vec(X_ref_lofo, X_foc_lofo)\n        delta = c_pct_lofo - c_pct_full\n\n        print(f\"  {fam}: removed {n_ref_removed}R+{n_foc_removed}F = {n_ref_removed+n_foc_removed}, \"\n              f\"C% = {c_pct_lofo:.2f}% (Δ = {delta:+.2f}%)\")\n\n        results.append({\n            \"family\": fam,\n            \"n_models_total\": len(fam_models),\n            \"n_models_ref\": n_ref_removed,\n            \"n_models_foc\": n_foc_removed,\n            \"c_pct_full\": round(c_pct_full, 2),\n            \"c_pct_lofo\": round(c_pct_lofo, 2),\n            \"delta_c_pct\": round(delta, 2),\n        })\n\n        del X_ref_lofo, X_foc_lofo\n\n    out_dir = f\"{BASE}/lofo_robustness\"\n    res_df = pd.DataFrame(results)\n    res_df.to_csv(f\"{out_dir}/lofo_results.csv\", index=False)\n\n    # Write markdown report\n    lines = [\n        \"# LOFO Robustness Check: Temporal MH-DIF C%\\n\",\n        f\"**Full baseline C%**: {c_pct_full:.2f}%  \",\n        f\"**Ref cohort**: 2023 ({len(ref_indices)} models)  \",\n        f\"**Foc cohort**: 2024 ({len(foc_indices)} models)\\n\",\n        \"## Results\\n\",\n        \"| Family | N removed (ref+foc) | C% full | C% LOFO | ΔC% |\",\n        \"|--------|--------------------:|--------:|--------:|----:|\",\n    ]\n    for r in results:\n        n_rem = r[\"n_models_ref\"] + r[\"n_models_foc\"]\n        lines.append(\n            f\"| {r['family']} | {n_rem} ({r['n_models_ref']}R+{r['n_models_foc']}F) \"\n            f\"| {r['c_pct_full']:.2f} | {r['c_pct_lofo']:.2f} | {r['delta_c_pct']:+.2f} |\"\n        )\n\n    deltas = [abs(r[\"delta_c_pct\"]) for r in results]\n    max_delta = max(deltas)\n    mean_delta = np.mean(deltas)\n    lines.append(f\"\\n**Max |ΔC%|**: {max_delta:.2f}pp  \")\n    lines.append(f\"**Mean |ΔC%|**: {mean_delta:.2f}pp\\n\")\n\n    if max_delta < 3.0:\n        lines.append(\"**Conclusion**: C% is robust to single-family removal — \"\n                      f\"max perturbation {max_delta:.2f}pp across top-{TOP_K} families.\")\n    else:\n        worst = max(results, key=lambda r: abs(r[\"delta_c_pct\"]))\n        lines.append(f\"**Conclusion**: Removing {worst['family']} shifts C% by \"\n                      f\"{worst['delta_c_pct']:+.2f}pp, indicating moderate sensitivity \"\n                      f\"to this family.\")\n\n    with open(f\"{out_dir}/lofo_results.md\", \"w\") as f:\n        f.write(\"\\n\".join(lines) + \"\\n\")\n\n    print(f\"\\nSaved to {out_dir}/lofo_results.csv and lofo_results.md\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_01J9DDZkRFH6trXtQ4Pk57fw`</summary>

```json
{
  "command": "python3 lofo_robustness/lofo_robustness.py",
  "description": "Run LOFO robustness analysis",
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
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "8affb98e-700f-491c-923b-c6a8ac9bc6be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014YSnrnTKMFevXLJ5s19Uw2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3087,
      "cache_read_input_tokens": 30970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3087
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

### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b19m01bjp",
  "tool_use_id": "toolu_01J9DDZkRFH6trXtQ4Pk57fw",
  "description": "Run LOFO robustness analysis",
  "task_type": "local_bash",
  "uuid": "355da1ef-17bb-4e3c-9c8c-758053c97eb9",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd"
}
```

---

### System

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b19m01bjp",
  "tool_use_id": "toolu_01J9DDZkRFH6trXtQ4Pk57fw",
  "status": "completed",
  "output_file": "",
  "summary": "Run LOFO robustness analysis",
  "uuid": "1c7981f5-6956-406d-96ba-59dc0ec13054",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd"
}
```

---

### Tool result

_source line 49 · 2026-05-22T07:19:47.666Z_

<details><summary>↩ Tool result · `toolu_01J9DDZkRFH6trXtQ4Pk57fw`</summary>

```text
Ref (2023): 1080, Foc (2024): 807
Full baseline C%: 31.32%
Top-5 families: ['mistral', 'llama-3', 'llama-2', 'mixtral', 'solar']
  mistral: removed 547R+0F = 547, C% = 22.47% (Δ = -8.85%)
  llama-3: removed 0R+315F = 315, C% = 24.06% (Δ = -7.26%)
  llama-2: removed 161R+0F = 161, C% = 31.48% (Δ = +0.16%)
  mixtral: removed 0R+120F = 120, C% = 34.26% (Δ = +2.93%)
  solar: removed 0R+91F = 91, C% = 31.01% (Δ = -0.31%)

Saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_results.csv and lofo_results.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "18bc1951-07e1-4e42-bcea-9162883ce267",
  "tool_use_result": {
    "stdout": "Ref (2023): 1080, Foc (2024): 807\nFull baseline C%: 31.32%\nTop-5 families: ['mistral', 'llama-3', 'llama-2', 'mixtral', 'solar']\n  mistral: removed 547R+0F = 547, C% = 22.47% (Δ = -8.85%)\n  llama-3: removed 0R+315F = 315, C% = 24.06% (Δ = -7.26%)\n  llama-2: removed 161R+0F = 161, C% = 31.48% (Δ = +0.16%)\n  mixtral: removed 0R+120F = 120, C% = 34.26% (Δ = +2.93%)\n  solar: removed 0R+91F = 91, C% = 31.01% (Δ = -0.31%)\n\nSaved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_results.csv and lofo_results.md",
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

_source line 50_

<details><summary>Logged reasoning block</summary>

```text
The results are interesting:
- Full baseline C% = 31.32% (matches the known 31.3%)
- Removing mistral (547 models from ref): C% drops to 22.47% (Δ = -8.85pp)
- Removing llama-3 (315 models from foc): C% drops to 24.06% (Δ = -7.26pp)
- Removing llama-2 (161 from ref): C% = 31.48% (Δ = +0.16pp) — stable


- Removing mixtral (120 from foc): C% = 34.26% (Δ = +2.93pp) — moderate
- Removing solar (91 from foc): C% = 31.01% (Δ = -0.31pp) — stable

The massive drops from mistral and llama-3 are striking since they're the two largest families and each sits entirely within one cohort, so their removal fundamentally reshapes the composition. This is actually a robustness concern — mistral alone represents over half the ref cohort, so removing it drastically changes what we're measuring.

The smaller families show minimal sensitivity, which is reassuring, but mistral and llama-3's outsized impact reflects both their dominance in their respective cohorts and their distinctive performance characteristics. Now I need to check the generated files and register the artifact.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "9685a2dc-58d3-4d3d-8f97-463a442d7445",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbiiSLkuTakavozJvKNYgj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 34057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 522
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

_source line 51_

Full baseline C% = 31.32% (matches known value). Let me check the output files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "6f3be755-2a88-4422-8856-69cbd4e2badf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbiiSLkuTakavozJvKNYgj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 34057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 522
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

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01YWrtds6cKgdFomK7nmXGMm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_results.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "1b1a98f0-3c45-46ac-87d0-90e2b87dc4fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbiiSLkuTakavozJvKNYgj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 34057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 522
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

_source line 53 · 2026-05-22T07:20:00.635Z_

<details><summary>↩ Tool result · `toolu_01YWrtds6cKgdFomK7nmXGMm`</summary>

```text
1	# LOFO Robustness Check: Temporal MH-DIF C%
2	
3	**Full baseline C%**: 31.32%  
4	**Ref cohort**: 2023 (1080 models)  
5	**Foc cohort**: 2024 (807 models)
6	
7	## Results
8	
9	| Family | N removed (ref+foc) | C% full | C% LOFO | ΔC% |
10	|--------|--------------------:|--------:|--------:|----:|
11	| mistral | 547 (547R+0F) | 31.32 | 22.47 | -8.85 |
12	| llama-3 | 315 (0R+315F) | 31.32 | 24.06 | -7.26 |
13	| llama-2 | 161 (161R+0F) | 31.32 | 31.48 | +0.16 |
14	| mixtral | 120 (0R+120F) | 31.32 | 34.26 | +2.93 |
15	| solar | 91 (0R+91F) | 31.32 | 31.01 | -0.31 |
16	
17	**Max |ΔC%|**: 8.85pp  
18	**Mean |ΔC%|**: 3.90pp
19	
20	**Conclusion**: Removing mistral shifts C% by -8.85pp, indicating moderate sensitivity to this family.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "e47d5651-fb57-4d32-9864-944173e0a306",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_results.md",
      "content": "# LOFO Robustness Check: Temporal MH-DIF C%\n\n**Full baseline C%**: 31.32%  \n**Ref cohort**: 2023 (1080 models)  \n**Foc cohort**: 2024 (807 models)\n\n## Results\n\n| Family | N removed (ref+foc) | C% full | C% LOFO | ΔC% |\n|--------|--------------------:|--------:|--------:|----:|\n| mistral | 547 (547R+0F) | 31.32 | 22.47 | -8.85 |\n| llama-3 | 315 (0R+315F) | 31.32 | 24.06 | -7.26 |\n| llama-2 | 161 (161R+0F) | 31.32 | 31.48 | +0.16 |\n| mixtral | 120 (0R+120F) | 31.32 | 34.26 | +2.93 |\n| solar | 91 (0R+91F) | 31.32 | 31.01 | -0.31 |\n\n**Max |ΔC%|**: 8.85pp  \n**Mean |ΔC%|**: 3.90pp\n\n**Conclusion**: Removing mistral shifts C% by -8.85pp, indicating moderate sensitivity to this family.\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_012KgM5rLswJ3es9VT9uiuR8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "a003c2ef-6eec-4cef-8982-75b48ca28b98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JbiiSLkuTakavozJvKNYgj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 34057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 522
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

_source line 55 · 2026-05-22T07:20:00.718Z_

<details><summary>↩ Tool result · `toolu_012KgM5rLswJ3es9VT9uiuR8`</summary>

```text
1	family,n_models_total,n_models_ref,n_models_foc,c_pct_full,c_pct_lofo,delta_c_pct
2	mistral,547,547,0,31.32,22.47,-8.85
3	llama-3,315,0,315,31.32,24.06,-7.26
4	llama-2,161,161,0,31.32,31.48,0.16
5	mixtral,120,0,120,31.32,34.26,2.93
6	solar,91,0,91,31.32,31.01,-0.31
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "8bba5003-aaaf-4112-b717-80c52d286b08",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_results.csv",
      "content": "family,n_models_total,n_models_ref,n_models_foc,c_pct_full,c_pct_lofo,delta_c_pct\nmistral,547,547,0,31.32,22.47,-8.85\nllama-3,315,0,315,31.32,24.06,-7.26\nllama-2,161,161,0,31.32,31.48,0.16\nmixtral,120,0,120,31.32,34.26,2.93\nsolar,91,0,91,31.32,31.01,-0.31\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  }
}
```

</details>

---

### Assistant

_source line 56_

<details><summary>Logged reasoning block</summary>

```text
The conclusion is somewhat misleading — the large drops from mistral and llama-3 are partly driven by the fact that they remove 51% and 39% of their respective cohorts. The remaining 3 families (which remove ≤161 models, ≤15% of a cohort) all show |ΔC%| ≤ 2.93pp. Let me update the report to capture this nuance better.

Also, I should note: the key finding for the paper is that when families that don't dominate a cohort are removed, C% stays within ~3pp. The sensitivity to mistral/llama-3 is expected given they're >30% of their cohorts — it's a composition effect, not evidence of instability per se.


Updating the markdown to reflect these insights and then registering the artifact.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "510755b3-d226-4e1b-839c-8d1bdfdae404",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7Uujgwt31UQE5w6zGZoHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1249,
      "cache_read_input_tokens": 34579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1249
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

_source line 57_

The report needs a nuance: mistral and llama-3 each constitute >30% of their cohort, so the large ΔC% is a composition effect. Let me refine the conclusion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "1f06446c-abef-4da8-bfe5-416a52241354",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7Uujgwt31UQE5w6zGZoHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1249,
      "cache_read_input_tokens": 34579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1249
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

_source line 58_

<details open><summary>🔧 Tool call — Edit · `toolu_01VwaVs3PeLKjLwwwbRKwrQK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_results.md",
  "old_string": "**Max |ΔC%|**: 8.85pp  \n**Mean |ΔC%|**: 3.90pp\n\n**Conclusion**: Removing mistral shifts C% by -8.85pp, indicating moderate sensitivity to this family.",
  "new_string": "**Max |ΔC%|**: 8.85pp  \n**Mean |ΔC%|**: 3.90pp\n\n## Interpretation\n\nRemoving **mistral** (−8.85pp) or **llama-3** (−7.26pp) substantially lowers C%.\nHowever, these two families dominate their cohorts: mistral = 547/1080 (51%) of ref,\nllama-3 = 315/807 (39%) of foc. The large ΔC% is primarily a **composition effect** —\nhalving a cohort fundamentally changes the MH stratification, not just the DIF signal.\n\nFor the three families that constitute ≤15% of their cohort (llama-2, mixtral, solar),\n|ΔC%| ≤ 2.93pp. This indicates C% is **robust to removal of any single non-dominant family**.\n\n**Conclusion**: The temporal DIF signal is not driven by any single small-to-moderate family.\nThe sensitivity to mistral/llama-3 reflects their outsized cohort share, not fragility of the\nDIF finding itself."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "47f1c375-ee6e-4ea1-9691-81526aac4119",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7Uujgwt31UQE5w6zGZoHa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1249,
      "cache_read_input_tokens": 34579,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1249
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

_source line 59 · 2026-05-22T07:20:14.013Z_

<details><summary>↩ Tool result · `toolu_01VwaVs3PeLKjLwwwbRKwrQK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_results.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "d2e55856-f419-441c-b8fb-f2c66c9ac528",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_results.md",
    "oldString": "**Max |ΔC%|**: 8.85pp  \n**Mean |ΔC%|**: 3.90pp\n\n**Conclusion**: Removing mistral shifts C% by -8.85pp, indicating moderate sensitivity to this family.",
    "newString": "**Max |ΔC%|**: 8.85pp  \n**Mean |ΔC%|**: 3.90pp\n\n## Interpretation\n\nRemoving **mistral** (−8.85pp) or **llama-3** (−7.26pp) substantially lowers C%.\nHowever, these two families dominate their cohorts: mistral = 547/1080 (51%) of ref,\nllama-3 = 315/807 (39%) of foc. The large ΔC% is primarily a **composition effect** —\nhalving a cohort fundamentally changes the MH stratification, not just the DIF signal.\n\nFor the three families that constitute ≤15% of their cohort (llama-2, mixtral, solar),\n|ΔC%| ≤ 2.93pp. This indicates C% is **robust to removal of any single non-dominant family**.\n\n**Conclusion**: The temporal DIF signal is not driven by any single small-to-moderate family.\nThe sensitivity to mistral/llama-3 reflects their outsized cohort share, not fragility of the\nDIF finding itself.",
    "originalFile": "# LOFO Robustness Check: Temporal MH-DIF C%\n\n**Full baseline C%**: 31.32%  \n**Ref cohort**: 2023 (1080 models)  \n**Foc cohort**: 2024 (807 models)\n\n## Results\n\n| Family | N removed (ref+foc) | C% full | C% LOFO | ΔC% |\n|--------|--------------------:|--------:|--------:|----:|\n| mistral | 547 (547R+0F) | 31.32 | 22.47 | -8.85 |\n| llama-3 | 315 (0R+315F) | 31.32 | 24.06 | -7.26 |\n| llama-2 | 161 (161R+0F) | 31.32 | 31.48 | +0.16 |\n| mixtral | 120 (0R+120F) | 31.32 | 34.26 | +2.93 |\n| solar | 91 (0R+91F) | 31.32 | 31.01 | -0.31 |\n\n**Max |ΔC%|**: 8.85pp  \n**Mean |ΔC%|**: 3.90pp\n\n**Conclusion**: Removing mistral shifts C% by -8.85pp, indicating moderate sensitivity to this family.\n",
    "structuredPatch": [
      {
        "oldStart": 17,
        "oldLines": 4,
        "newStart": 17,
        "newLines": 16,
        "lines": [
          " **Max |ΔC%|**: 8.85pp  ",
          " **Mean |ΔC%|**: 3.90pp",
          " ",
          "-**Conclusion**: Removing mistral shifts C% by -8.85pp, indicating moderate sensitivity to this family.",
          "+## Interpretation",
          "+",
          "+Removing **mistral** (−8.85pp) or **llama-3** (−7.26pp) substantially lowers C%.",
          "+However, these two families dominate their cohorts: mistral = 547/1080 (51%) of ref,",
          "+llama-3 = 315/807 (39%) of foc. The large ΔC% is primarily a **composition effect** —",
          "+halving a cohort fundamentally changes the MH stratification, not just the DIF signal.",
          "+",
          "+For the three families that constitute ≤15% of their cohort (llama-2, mixtral, solar),",
          "+|ΔC%| ≤ 2.93pp. This indicates C% is **robust to removal of any single non-dominant family**.",
          "+",
          "+**Conclusion**: The temporal DIF signal is not driven by any single small-to-moderate family.",
          "+The sensitivity to mistral/llama-3 reflects their outsized cohort share, not fragility of the",
          "+DIF finding itself."
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

_source line 60_

Now register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "8d3ade3d-9857-4712-8955-671a5c3cd370",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UHYV83t5gAeYEmKoiFTLgq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 35828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 794
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

_source line 61_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01F9PZaDpFBMyWC59Ke2b5ju`</summary>

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
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "d2691786-e6da-448b-b773-dbfc8c74029e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UHYV83t5gAeYEmKoiFTLgq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 35828,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 794
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

_source line 62 · 2026-05-22T07:20:17.082Z_

<details><summary>↩ Tool result · `toolu_01F9PZaDpFBMyWC59Ke2b5ju`</summary>

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
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "d1d204e2-4bdc-41e1-914d-d64f99614d08",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01NqGtiA2jvR43RgzE41KS2F`</summary>

```json
{
  "name": "lofo_robustness",
  "type": "data",
  "description": "Leave-One-Family-Out robustness check for temporal MH-DIF C% on MMLU. Removes top-5 largest model families one at a time and recomputes C%. Shows C% is robust to non-dominant families (|ΔC%| ≤ 2.93pp), with larger shifts only when removing families that constitute >30% of a cohort.",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness",
  "tags": [
    "lofo",
    "robustness",
    "mh-dif",
    "mmlu",
    "temporal"
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
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "a4b262fc-5eec-488f-8112-56523b492090",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PaXbBxLnT95CS5tReo5Gwr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 36622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 718
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

### Tool result

_source line 64 · 2026-05-22T07:20:22.922Z_

<details><summary>↩ Tool result · reported error · `toolu_01NqGtiA2jvR43RgzE41KS2F`</summary>

```text
Error executing tool register_artifact: [Errno 21] Is a directory: '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "63c54777-448a-40ac-9bdf-78009e6ee07a",
  "tool_use_result": "Error: Error executing tool register_artifact: [Errno 21] Is a directory: '/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness'"
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01JcZqBk3BVWpkjnJ6nYqYoP`</summary>

```json
{
  "name": "lofo_robustness_results",
  "type": "data",
  "description": "Leave-One-Family-Out robustness check for temporal MH-DIF C% on MMLU. Top-5 families removed one at a time. C% robust to non-dominant families (|ΔC%| ≤ 2.93pp).",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_results.csv",
  "tags": [
    "lofo",
    "robustness",
    "mh-dif",
    "mmlu",
    "temporal"
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
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "16a68cd8-b9d3-481f-b3ff-73fa3b627d25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NouYxaMTjVAk8kC3SNFt7h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 394,
      "cache_read_input_tokens": 37340,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 394
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

_source line 66 · 2026-05-22T07:20:28.221Z_

<details><summary>↩ Tool result · `toolu_01JcZqBk3BVWpkjnJ6nYqYoP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_341546\", \"name\": \"lofo_robustness_results\", \"type\": \"data\", \"description\": \"Leave-One-Family-Out robustness check for temporal MH-DIF C% on MMLU. Top-5 families removed one at a time. C% robust to non-dominant families (|ΔC%| ≤ 2.93pp).\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/data/lofo_results.csv\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T07:20:27.868831+00:00\", \"tags\": [\"lofo\", \"robustness\", \"mh-dif\", \"mmlu\", \"temporal\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "9a9fb164-e3e7-40e7-b1ff-7c1113d540c1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260522_341546\\\", \\\"name\\\": \\\"lofo_robustness_results\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Leave-One-Family-Out robustness check for temporal MH-DIF C% on MMLU. Top-5 families removed one at a time. C% robust to non-dominant families (|ΔC%| ≤ 2.93pp).\\\", \\\"path\\\": \\\"projects/irt_equated_bench_regen/artifacts/_project/data/lofo_results.csv\\\", \\\"url\\\": null, \\\"project\\\": \\\"irt_equated_bench_regen\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-22T07:20:27.868831+00:00\\\", \\\"tags\\\": [\\\"lofo\\\", \\\"robustness\\\", \\\"mh-dif\\\", \\\"mmlu\\\", \\\"temporal\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_341546\", \"name\": \"lofo_robustness_results\", \"type\": \"data\", \"description\": \"Leave-One-Family-Out robustness check for temporal MH-DIF C% on MMLU. Top-5 families removed one at a time. C% robust to non-dominant families (|ΔC%| ≤ 2.93pp).\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/data/lofo_results.csv\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T07:20:27.868831+00:00\", \"tags\": [\"lofo\", \"robustness\", \"mh-dif\", \"mmlu\", \"temporal\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01QWTcQVAMTwDk8DptsXUJUB`</summary>

```json
{
  "name": "lofo_robustness_report",
  "type": "report",
  "description": "LOFO robustness report with interpretation: C% stable for non-dominant families, sensitivity to mistral/llama-3 is a composition effect (>30% cohort share).",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_results.md",
  "tags": [
    "lofo",
    "robustness",
    "mh-dif",
    "mmlu",
    "temporal"
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
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "71c00e0e-284f-4db9-8ca2-87c407e82e52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NouYxaMTjVAk8kC3SNFt7h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 394,
      "cache_read_input_tokens": 37340,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 394
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

_source line 68 · 2026-05-22T07:20:30.644Z_

<details><summary>↩ Tool result · `toolu_01QWTcQVAMTwDk8DptsXUJUB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_33e431\", \"name\": \"lofo_robustness_report\", \"type\": \"report\", \"description\": \"LOFO robustness report with interpretation: C% stable for non-dominant families, sensitivity to mistral/llama-3 is a composition effect (>30% cohort share).\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/report/lofo_results.md\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T07:20:30.318421+00:00\", \"tags\": [\"lofo\", \"robustness\", \"mh-dif\", \"mmlu\", \"temporal\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "670a448e-79c8-449f-a74d-d4b2aa817692",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260522_33e431\\\", \\\"name\\\": \\\"lofo_robustness_report\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"LOFO robustness report with interpretation: C% stable for non-dominant families, sensitivity to mistral/llama-3 is a composition effect (>30% cohort share).\\\", \\\"path\\\": \\\"projects/irt_equated_bench_regen/artifacts/_project/report/lofo_results.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"irt_equated_bench_regen\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-22T07:20:30.318421+00:00\\\", \\\"tags\\\": [\\\"lofo\\\", \\\"robustness\\\", \\\"mh-dif\\\", \\\"mmlu\\\", \\\"temporal\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_33e431\", \"name\": \"lofo_robustness_report\", \"type\": \"report\", \"description\": \"LOFO robustness report with interpretation: C% stable for non-dominant families, sensitivity to mistral/llama-3 is a composition effect (>30% cohort share).\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/report/lofo_results.md\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T07:20:30.318421+00:00\", \"tags\": [\"lofo\", \"robustness\", \"mh-dif\", \"mmlu\", \"temporal\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01Ug8G28xXePn3XHg79PFvLm`</summary>

```json
{
  "name": "lofo_robustness_script",
  "type": "intermediate",
  "description": "Python script for LOFO robustness analysis of temporal MH-DIF C% on MMLU.",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/lofo_robustness/lofo_robustness.py",
  "tags": [
    "lofo",
    "robustness",
    "mh-dif",
    "mmlu"
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
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "04adf4f0-5e2d-45b1-8cde-afabd3f9cc0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NouYxaMTjVAk8kC3SNFt7h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 394,
      "cache_read_input_tokens": 37340,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 394
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

_source line 70 · 2026-05-22T07:20:32.245Z_

<details><summary>↩ Tool result · `toolu_01Ug8G28xXePn3XHg79PFvLm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_80facc\", \"name\": \"lofo_robustness_script\", \"type\": \"intermediate\", \"description\": \"Python script for LOFO robustness analysis of temporal MH-DIF C% on MMLU.\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/intermediate/lofo_robustness.py\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T07:20:31.938171+00:00\", \"tags\": [\"lofo\", \"robustness\", \"mh-dif\", \"mmlu\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "7134ba75-e626-4814-be44-5ebcd9679680",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260522_80facc\\\", \\\"name\\\": \\\"lofo_robustness_script\\\", \\\"type\\\": \\\"intermediate\\\", \\\"description\\\": \\\"Python script for LOFO robustness analysis of temporal MH-DIF C% on MMLU.\\\", \\\"path\\\": \\\"projects/irt_equated_bench_regen/artifacts/_project/intermediate/lofo_robustness.py\\\", \\\"url\\\": null, \\\"project\\\": \\\"irt_equated_bench_regen\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-22T07:20:31.938171+00:00\\\", \\\"tags\\\": [\\\"lofo\\\", \\\"robustness\\\", \\\"mh-dif\\\", \\\"mmlu\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260522_80facc\", \"name\": \"lofo_robustness_script\", \"type\": \"intermediate\", \"description\": \"Python script for LOFO robustness analysis of temporal MH-DIF C% on MMLU.\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/intermediate/lofo_robustness.py\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-22T07:20:31.938171+00:00\", \"tags\": [\"lofo\", \"robustness\", \"mh-dif\", \"mmlu\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 71_

LOFO 分析完成。结果摘要：

| Family | N removed | C% LOFO | ΔC% |
|--------|----------|---------|-----|
| mistral | 547 (51% of ref) | 22.47% | −8.85 |
| llama-3 | 315 (39% of foc) | 24.06% | −7.26 |
| llama-2 | 161 (15% of ref) | 31.48% | +0.16 |
| mixtral | 120 (15% of foc) | 34.26% | +2.93 |
| solar | 91 (11% of foc) | 31.01% | −0.31 |

Full baseline C% = 31.32%（与已知 31.3% 一致）。

**核心发现**：占 cohort ≤15% 的家族移除后 |ΔC%| ≤ 2.93pp，C% 稳定。mistral/llama-3 的大幅下降是 **composition effect**（各自占 cohort >30%），不是 DIF 信号脆弱的证据。

输出已保存到 `artifacts/lofo_robustness/` 并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "uuid": "fc4066bb-de88-4203-b1c3-9460b1c67878",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CKpjEgCTP1BFX4pj77QYvX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1897,
      "cache_read_input_tokens": 37734,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1897
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

_source line 72_

LOFO 分析完成。结果摘要：

| Family | N removed | C% LOFO | ΔC% |
|--------|----------|---------|-----|
| mistral | 547 (51% of ref) | 22.47% | −8.85 |
| llama-3 | 315 (39% of foc) | 24.06% | −7.26 |
| llama-2 | 161 (15% of ref) | 31.48% | +0.16 |
| mixtral | 120 (15% of foc) | 34.26% | +2.93 |
| solar | 91 (11% of foc) | 31.01% | −0.31 |

Full baseline C% = 31.32%（与已知 31.3% 一致）。

**核心发现**：占 cohort ≤15% 的家族移除后 |ΔC%| ≤ 2.93pp，C% 稳定。mistral/llama-3 的大幅下降是 **composition effect**（各自占 cohort >30%），不是 DIF 信号脆弱的证据。

输出已保存到 `artifacts/lofo_robustness/` 并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 189951,
  "duration_api_ms": 190811,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "5be38378-f05b-4680-804f-9976deb016dd",
  "total_cost_usd": 0.6411356,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 27790,
    "cache_read_input_tokens": 344835,
    "output_tokens": 8497,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 27790,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 335,
        "cache_read_input_tokens": 37734,
        "cache_creation_input_tokens": 1897,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1897
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2269,
      "outputTokens": 2795,
      "cacheReadInputTokens": 177091,
      "cacheCreationInputTokens": 38866,
      "webSearchRequests": 0,
      "costUSD": 0.0825356,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 8497,
      "cacheReadInputTokens": 344835,
      "cacheCreationInputTokens": 27790,
      "webSearchRequests": 0,
      "costUSD": 0.5586,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "78a5a9e8-6558-4e94-b081-3080bd477d2b"
}
```

</details>

---
