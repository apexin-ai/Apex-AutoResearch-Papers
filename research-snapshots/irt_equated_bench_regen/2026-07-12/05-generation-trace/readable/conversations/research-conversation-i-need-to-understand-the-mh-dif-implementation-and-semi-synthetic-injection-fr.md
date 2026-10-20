# Research conversation: I need to understand the MH-DIF implementation and semi-synthetic injection framework in two directories: 1. `/home/ubun

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aa73b16fd4338b1af.jsonl`
- **Structured JSON:** [`41602947891df7d4ef44.json`](../../sessions/41/41602947891df7d4ef44.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

20 recorded events

### User

_source line 1 · 2026-05-21T15:45:28.896Z_

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
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6acb2fc6-c913-4bb6-a525-f82390cb809d",
  "agentId": "aa73b16fd4338b1af",
  "type": "user",
  "uuid": "f23f2d36-d905-4d16-bc06-5a909f3d8996",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T15:45:30.300Z_

I'll systematically explore both directories to understand the MH-DIF implementation and semi-synthetic injection framework. Let me start by examining the structure and then dive into the specific files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f23f2d36-d905-4d16-bc06-5a909f3d8996",
  "isSidechain": true,
  "agentId": "aa73b16fd4338b1af",
  "requestId": "req_011CbFyQ5fFCU3AzSRkmBD7o",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6fa0f604-de74-4ffc-9ff1-8394aaaa75e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master",
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
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T15:45:30.570Z_

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
  "parentUuid": "6fa0f604-de74-4ffc-9ff1-8394aaaa75e9",
  "isSidechain": true,
  "agentId": "aa73b16fd4338b1af",
  "requestId": "req_011CbFyQ5fFCU3AzSRkmBD7o",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e86e1a2d-d7c3-4c08-93a7-c02e6bad8fd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015nqME6kGCstZm998Ku7rL3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17056,
      "cache_read_input_tokens": 0,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17056
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 143,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17056,
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

_source line 4 · 2026-05-21T15:45:30.758Z_

<details><summary>↩ Tool result · `toolu_01KhPEyixfHVxwxocsQCjw6v`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_within_subject_injection.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e86e1a2d-d7c3-4c08-93a7-c02e6bad8fd1",
  "isSidechain": true,
  "promptId": "6acb2fc6-c913-4bb6-a525-f82390cb809d",
  "agentId": "aa73b16fd4338b1af",
  "type": "user",
  "uuid": "ef6d05d4-a982-4551-b515-ee40295983c6",
  "sourceToolAssistantUUID": "e86e1a2d-d7c3-4c08-93a7-c02e6bad8fd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-21T15:45:32.063Z_

Now let me check plan_011 and examine the full structure:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef6d05d4-a982-4551-b515-ee40295983c6",
  "isSidechain": true,
  "agentId": "aa73b16fd4338b1af",
  "requestId": "req_011CbFyQDeiHgjWwk5zQLCNK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cd5582ad-6a34-49cf-8d8a-1525bb9c17c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master",
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
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T15:45:32.189Z_

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
  "parentUuid": "cd5582ad-6a34-49cf-8d8a-1525bb9c17c4",
  "isSidechain": true,
  "agentId": "aa73b16fd4338b1af",
  "requestId": "req_011CbFyQDeiHgjWwk5zQLCNK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6022a114-8db9-4bcf-b079-f2b93cf46f6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UU3R5nqeCP7KhQbw2hnUR9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1039,
      "cache_read_input_tokens": 17056,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1039
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 118,
          "cache_read_input_tokens": 17056,
          "cache_creation_input_tokens": 1039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1039,
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

_source line 7 · 2026-05-21T15:45:32.258Z_

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
  "parentUuid": "6022a114-8db9-4bcf-b079-f2b93cf46f6b",
  "isSidechain": true,
  "promptId": "6acb2fc6-c913-4bb6-a525-f82390cb809d",
  "agentId": "aa73b16fd4338b1af",
  "type": "user",
  "uuid": "672dbb11-e8dc-477e-b083-8e793538a929",
  "sourceToolAssistantUUID": "6022a114-8db9-4bcf-b079-f2b93cf46f6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-21T15:45:33.427Z_

Good. Now let me read both Python files to understand the implementations:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "672dbb11-e8dc-477e-b083-8e793538a929",
  "isSidechain": true,
  "agentId": "aa73b16fd4338b1af",
  "requestId": "req_011CbFyQKxEKwqqf3NeXmL33",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4cc7811c-e1c2-4050-a390-f9d266b76aa3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master",
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
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T15:45:33.778Z_

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
  "parentUuid": "4cc7811c-e1c2-4050-a390-f9d266b76aa3",
  "isSidechain": true,
  "agentId": "aa73b16fd4338b1af",
  "requestId": "req_011CbFyQKxEKwqqf3NeXmL33",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fcf2c443-aff1-4171-8da7-b779084a1364",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UBGFqfKugG5agCRXiivG65",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 354,
      "cache_read_input_tokens": 18095,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 354
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 113,
          "cache_read_input_tokens": 18095,
          "cache_creation_input_tokens": 354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 354,
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

_source line 10 · 2026-05-21T15:45:33.797Z_

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
  "parentUuid": "fcf2c443-aff1-4171-8da7-b779084a1364",
  "isSidechain": true,
  "promptId": "6acb2fc6-c913-4bb6-a525-f82390cb809d",
  "agentId": "aa73b16fd4338b1af",
  "type": "user",
  "uuid": "ebd2d900-68a5-4606-a0ce-f436e884f44a",
  "sourceToolAssistantUUID": "fcf2c443-aff1-4171-8da7-b779084a1364",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T15:45:35.209Z_

Excellent! Now let me read the plan_016 file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebd2d900-68a5-4606-a0ce-f436e884f44a",
  "isSidechain": true,
  "agentId": "aa73b16fd4338b1af",
  "requestId": "req_011CbFyQSYraentQeLjXiZGb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a77e9d77-ae08-4383-a8e6-14ca8e3ebb78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master",
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
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T15:45:36.208Z_

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
  "parentUuid": "a77e9d77-ae08-4383-a8e6-14ca8e3ebb78",
  "isSidechain": true,
  "agentId": "aa73b16fd4338b1af",
  "requestId": "req_011CbFyQSYraentQeLjXiZGb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "35882a73-9856-423a-bc41-bfd236ce4356",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MYMA1PRR6jQS3xSvRqYp3v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 10283,
      "cache_read_input_tokens": 18449,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10283
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 117,
          "cache_read_input_tokens": 18449,
          "cache_creation_input_tokens": 10283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10283,
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

_source line 13 · 2026-05-21T15:45:36.224Z_

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
  "parentUuid": "35882a73-9856-423a-bc41-bfd236ce4356",
  "isSidechain": true,
  "promptId": "6acb2fc6-c913-4bb6-a525-f82390cb809d",
  "agentId": "aa73b16fd4338b1af",
  "type": "user",
  "uuid": "771954bb-69cd-4628-8342-e438cb4b8428",
  "sourceToolAssistantUUID": "35882a73-9856-423a-bc41-bfd236ce4356",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-21T15:45:37.817Z_

Perfect! Now I have both files. Let me create a comprehensive report of the implementations. Let me also check if there are any related configuration or data loading files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "771954bb-69cd-4628-8342-e438cb4b8428",
  "isSidechain": true,
  "agentId": "aa73b16fd4338b1af",
  "requestId": "req_011CbFyQd1tmfjDnAAbCco1a",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c28e5d6a-baf0-48f6-94ab-828c450eb178",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master",
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
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T15:45:38.729Z_

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
  "parentUuid": "c28e5d6a-baf0-48f6-94ab-828c450eb178",
  "isSidechain": true,
  "agentId": "aa73b16fd4338b1af",
  "requestId": "req_011CbFyQd1tmfjDnAAbCco1a",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e82bbdb4-57b9-4cdf-b725-b791e2ad76dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M8RdQD7i9mHhfUbv123fEn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 9542,
      "cache_read_input_tokens": 28732,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9542
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 140,
          "cache_read_input_tokens": 28732,
          "cache_creation_input_tokens": 9542,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9542,
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

_source line 16 · 2026-05-21T15:45:38.800Z_

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
  "parentUuid": "e82bbdb4-57b9-4cdf-b725-b791e2ad76dc",
  "isSidechain": true,
  "promptId": "6acb2fc6-c913-4bb6-a525-f82390cb809d",
  "agentId": "aa73b16fd4338b1af",
  "type": "user",
  "uuid": "a005e5fe-378f-4b1a-9183-f538e0838417",
  "sourceToolAssistantUUID": "e82bbdb4-57b9-4cdf-b725-b791e2ad76dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-21T15:45:40.053Z_

Now let me create a comprehensive technical summary document based on what I've read:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a005e5fe-378f-4b1a-9183-f538e0838417",
  "isSidechain": true,
  "agentId": "aa73b16fd4338b1af",
  "requestId": "req_011CbFyQovyQqCpE9EnL6ozy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "04c93a2f-56ea-4796-9ae8-a352d2b46c03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master",
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
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T15:45:40.440Z_

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
  "parentUuid": "04c93a2f-56ea-4796-9ae8-a352d2b46c03",
  "isSidechain": true,
  "agentId": "aa73b16fd4338b1af",
  "requestId": "req_011CbFyQovyQqCpE9EnL6ozy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "831a133c-a271-44aa-8d9c-e5317052a834",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SnkgJs9vpGsrXFXP9MEkCw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 415,
      "cache_read_input_tokens": 38274,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 415
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 149,
          "cache_read_input_tokens": 38274,
          "cache_creation_input_tokens": 415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 415,
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

_source line 19 · 2026-05-21T15:45:40.449Z_

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
  "parentUuid": "831a133c-a271-44aa-8d9c-e5317052a834",
  "isSidechain": true,
  "promptId": "6acb2fc6-c913-4bb6-a525-f82390cb809d",
  "agentId": "aa73b16fd4338b1af",
  "type": "user",
  "uuid": "cc0dfd0c-2f5a-41e7-b98e-aa1428851e35",
  "sourceToolAssistantUUID": "831a133c-a271-44aa-8d9c-e5317052a834",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-21T15:46:30.523Z_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc0dfd0c-2f5a-41e7-b98e-aa1428851e35",
  "isSidechain": true,
  "agentId": "aa73b16fd4338b1af",
  "requestId": "req_011CbFyQwA42X8WddSU3Ugap",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2195ef01-2962-4c95-9c3e-e2e1e9f36a09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "10ffa11d-40e4-471e-8ae3-67988538bc6c",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012zH3ebULfTBLQUsgv2uss3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
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
    "diagnostics": null
  }
}
```

</details>

---
