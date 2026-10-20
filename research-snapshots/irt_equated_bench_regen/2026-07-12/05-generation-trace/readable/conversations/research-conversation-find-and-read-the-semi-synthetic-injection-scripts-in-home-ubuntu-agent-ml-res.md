# Research conversation: Find and read the semi-synthetic injection scripts in /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equat

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-af14da85843b71e93.jsonl`
- **Structured JSON:** [`f3027c046472a905e68b.json`](../../sessions/f3/f3027c046472a905e68b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-21T00:52:13.179Z_

Find and read the semi-synthetic injection scripts in /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/. I need to understand:
1. The full injection mechanism (how contaminated items are selected, how ability-overlapping models are identified, how incorrect→correct flipping works)
2. The MH-DIF implementation
3. The dose-response evaluation (TPR, FPR, Fisher exact test)
4. The matching variable computation (standard vs external)
5. How results are summarized

Read ALL python files in that directory thoroughly. Return the complete code of the main semi-synthetic script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "b681718f-ed7e-4c71-ace8-cbf70777063c",
  "agentId": "af14da85843b71e93",
  "type": "user",
  "uuid": "6b91c322-5743-448a-a9a6-7b496e674a58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T00:52:14.414Z_

I'll help you find and analyze the semi-synthetic injection scripts. Let me start by exploring the directory structure and then reading the Python files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b91c322-5743-448a-a9a6-7b496e674a58",
  "isSidechain": true,
  "agentId": "af14da85843b71e93",
  "requestId": "req_011CbEoHJw6rotVR5DwhabMP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "20c39455-3b5a-488e-a9a7-9091d4122306",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Vt15JBKqysGx91JY8DFwCU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19336,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 19336,
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

_source line 3 · 2026-05-21T00:52:14.696Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WNsx1daQBd5tjSfWJjbYvp`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011 -type f -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20c39455-3b5a-488e-a9a7-9091d4122306",
  "isSidechain": true,
  "agentId": "af14da85843b71e93",
  "requestId": "req_011CbEoHJw6rotVR5DwhabMP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9b11012a-06ff-408c-b9d1-c227a971c2fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Vt15JBKqysGx91JY8DFwCU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 19336,
      "cache_read_input_tokens": 0,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 19336
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 134,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 19336,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 19336,
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

_source line 4 · 2026-05-21T00:52:14.903Z_

<details><summary>↩ Tool result · `toolu_01WNsx1daQBd5tjSfWJjbYvp`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b11012a-06ff-408c-b9d1-c227a971c2fc",
  "isSidechain": true,
  "promptId": "b681718f-ed7e-4c71-ace8-cbf70777063c",
  "agentId": "af14da85843b71e93",
  "type": "user",
  "uuid": "86740689-c85b-4110-9f44-71af56d5947f",
  "sourceToolAssistantUUID": "9b11012a-06ff-408c-b9d1-c227a971c2fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-21T00:52:16.088Z_

Let me check the directory structure more thoroughly:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86740689-c85b-4110-9f44-71af56d5947f",
  "isSidechain": true,
  "agentId": "af14da85843b71e93",
  "requestId": "req_011CbEoHSF8gh2Kn6cJRMZHj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ffceea55-dce0-4478-be2f-f5ef88e04ab3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NKr5RFZD9LoFZqUb3Bd5Wn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1026,
      "cache_read_input_tokens": 19336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1026,
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

_source line 6 · 2026-05-21T00:52:16.272Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MvmRdfczBAucRnw71izkQB`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffceea55-dce0-4478-be2f-f5ef88e04ab3",
  "isSidechain": true,
  "agentId": "af14da85843b71e93",
  "requestId": "req_011CbEoHSF8gh2Kn6cJRMZHj",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "078f9d8a-b2d2-43fd-914f-660c9457a008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NKr5RFZD9LoFZqUb3Bd5Wn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1026,
      "cache_read_input_tokens": 19336,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1026
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 103,
          "cache_read_input_tokens": 19336,
          "cache_creation_input_tokens": 1026,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1026,
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

_source line 7 · 2026-05-21T00:52:16.338Z_

<details><summary>↩ Tool result · `toolu_01MvmRdfczBAucRnw71izkQB`</summary>

```text
total 2096
drwxr-xr-x  2 ubuntu ubuntu    4096 May 20 21:48 .
drwxr-xr-x 23 ubuntu ubuntu    4096 May 21 00:32 ..
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
  "parentUuid": "078f9d8a-b2d2-43fd-914f-660c9457a008",
  "isSidechain": true,
  "promptId": "b681718f-ed7e-4c71-ace8-cbf70777063c",
  "agentId": "af14da85843b71e93",
  "type": "user",
  "uuid": "ceb104f9-84c5-4ceb-9471-87dfb6ed4ea8",
  "sourceToolAssistantUUID": "078f9d8a-b2d2-43fd-914f-660c9457a008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-21T00:52:17.584Z_

Now let me read the main analysis script:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ceb104f9-84c5-4ceb-9471-87dfb6ed4ea8",
  "isSidechain": true,
  "agentId": "af14da85843b71e93",
  "requestId": "req_011CbEoHYNEds9gkahUkFoDM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d1398ea9-f18b-431b-97d0-de552e4427b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BEABEUHtgQf2MnktaqkUh3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 339,
      "cache_read_input_tokens": 20362,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 339,
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

_source line 9 · 2026-05-21T00:52:17.905Z_

<details open><summary>🔧 Tool call — Read · `toolu_013NyL7f45cAds94WN7u2vKq`</summary>

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
  "parentUuid": "d1398ea9-f18b-431b-97d0-de552e4427b5",
  "isSidechain": true,
  "agentId": "af14da85843b71e93",
  "requestId": "req_011CbEoHYNEds9gkahUkFoDM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5b5af298-05f0-47ed-95b4-3e9b57ed4d67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BEABEUHtgQf2MnktaqkUh3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 339,
      "cache_read_input_tokens": 20362,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 339
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 108,
          "cache_read_input_tokens": 20362,
          "cache_creation_input_tokens": 339,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 339,
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

_source line 10 · 2026-05-21T00:52:17.929Z_

<details><summary>↩ Tool result · `toolu_013NyL7f45cAds94WN7u2vKq`</summary>

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
  "parentUuid": "5b5af298-05f0-47ed-95b4-3e9b57ed4d67",
  "isSidechain": true,
  "promptId": "b681718f-ed7e-4c71-ace8-cbf70777063c",
  "agentId": "af14da85843b71e93",
  "type": "user",
  "uuid": "28a329d4-e2b4-4c80-8b2f-488c5b966179",
  "sourceToolAssistantUUID": "5b5af298-05f0-47ed-95b4-3e9b57ed4d67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T00:53:34.941Z_

Perfect! I have the complete semi-synthetic injection script. Let me now provide you with a comprehensive analysis of the code:

## Complete Analysis of plan_011_analysis.py

### 1. **Full Injection Mechanism** (Lines 307-330)

The injection process works as follows:

- **Contaminated item selection**: For each seed, `N_CONTAMINATED=100` items are randomly selected from the `N_BASELINE=500` baseline items using `np.random.choice()` without replacement (line 311).
- **Ability-overlapping model identification**: The script identifies focal models that fall within the ability (or temporal) overlap range:
  - For ability cohort: models in Q4-5 (highest accuracy) whose accuracy falls within [min(Q1-2 accuracy), min(Q4-5 accuracy)] (lines 237-242)
  - This ensures contamination is injected into models with similar base abilities as reference models, creating a "differential" contamination scenario
- **Incorrect→Correct flipping** (lines 318-324):
  - For each contaminated item and each focal model to inject into
  - Only flip if current response is 0 (incorrect), with probability `p` (the injection strength)
  - Only incorrect responses can be flipped to correct (never the reverse)
  - Count total flips via `n_flipped`

### 2. **MH-DIF Implementation** (Lines 46-167)

The `mh_dif_subset()` function implements Mantel-Haenszel DIF testing with three matching variable modes:

**Stratification priority**:
1. **External**: Pre-computed ability scores from full 12,508-item matrix (lines 71-73)
2. **Anchor**: Sum of known-clean items only (lines 74-80)
3. **Standard**: Total score minus current item (lines 81-83) - purified approach

**Core MH computation** (lines 101-149):
- Stratifies both reference and focal groups into `n_strata=5` bins based on matching variable (lines 85-93)
- For each stratum k, computes 2×2 contingency table (A, B, C, D) for item j (lines 109-115)
- Accumulates Mantel-Haenszel statistics across strata:
  - R and S: numerator/denominator of alpha (lines 121-124)
  - Variance components for SE calculation (lines 126-134)
- Calculates MH alpha (odds ratio) and delta (log-odds effect size) (lines 145-148)
- Computes chi-square statistic with continuity correction (line 151)

**ETS classification** (lines 156-162):
- Class A: |delta| < 1.0 (negligible)
- Class C: |delta| >= 1.5 AND p-value < 0.05 (significant DIF)
- Class B: everything else (moderate)

### 3. **Dose-Response Evaluation** (Lines 345-370)

For each injection run, the script computes:

**TPR (True Positive Rate)**:
- Number of contaminated items flagged as class C (DIF detected)
- Divided by N_CONTAMINATED (100)
- Formula: `tpr = (contaminated items flagged as C) / 100`

**FPR (False Positive Rate)**:
- Number of clean items flagged as class C
- Divided by N_CLEAN (400)
- Formula: `fpr = (clean items flagged as C) / 400`

**Fisher Exact Test** (lines 356-358):
- Builds contingency table:
  ```
  [[n_c_contam, N_CONTAMINATED - n_c_contam],
   [n_c_clean, (N_BASELINE - N_CONTAMINATED) - n_c_clean]]
  ```
- Tests association between DIF detection (C-class) and contamination status
- Reports OR (odds ratio) and p-value

### 4. **Matching Variable Computation** (Lines 59-83)

**Standard** (purified):
```python
tot_ref = X_ref.sum(axis=1)  # total across all 500 items
tot_foc = X_foc.sum(axis=1)
# For item j: score = total - response[j]
s_ref = tot_ref - X_ref[:, j]
```

**Anchor**:
```python
anchor_cols = clean_local_idx  # the 400 known-clean items
tot_ref = X_ref[:, anchor_cols].sum(axis=1)
tot_foc = X_foc[:, anchor_cols].sum(axis=1)
# score = total of clean items only (never adjusted per-item)
```

**External**:
```python
# Pre-computed from full 12,508-item matrix
ext_ref = full_totals[ref_idx]  # shape: (N_ref,)
ext_foc = full_totals[foc_idx]  # shape: (N_foc,)
# score = pre-injection full-matrix total (immune to any injection)
```

### 5. **Results Summarization** (Lines 400-416)

**Injection results** (one row per condition):
- Groupby: (p, cohort_type, mh_variant)
- Saved to `injection_results.csv` with:
  - Raw counts and rates (TPR, FPR, Fisher stats)
  - Density metrics (orig_density, new_density, n_responses_flipped)

**Dose-response summary** (lines 401-408):
- Aggregated across 5 seeds
- Computed mean/std for TPR and FPR
- Median Fisher p-value (more robust to outliers than mean)

**Per-item results** (lines 372-383):
- Only for anchor variant (to keep CSV manageable)
- Saved to `per_item_results.csv` with:
  - Individual item delta_mh, p_value, ets_class
  - Whether item was in contamination set

---

## Complete Main Script Code

Here is the full, uninterrupted code of the main semi-synthetic analysis script:

```python
#!/usr/bin/env python3
"""
plan_011_analysis.py — Semi-Synthetic DIF Validation

Injects known differential contamination into real MMLU response data and tests
whether MH-DIF can detect it. Validates the DIF methodology used in plan_001.

Three MH variants:
  (1) standard  — total score on 500 items minus current (same as plan_001)
  (2) anchor    — total score on 400 known-clean items only
  (3) external  — total score on full 12508-item original matrix (best matching)

Inputs:
  response_matrix.npz, response_matrix_index.npz, model_metadata.csv,
  item_metadata.csv, mmlu_li2024_proxy_labels.csv,
  plan_001/dif_results_ability.csv

Outputs (all in plan_011/):
  injection_results.csv, dose_response_summary.csv, per_item_results.csv,
  plan_011_report.md
"""

import numpy as np
import pandas as pd
from scipy.sparse import load_npz
from scipy.stats import chi2 as chi2_dist, fisher_exact
from pathlib import Path
import time
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
OUT = BASE / "plan_011"
OUT.mkdir(exist_ok=True)

INJECTION_PS = [0.0, 0.3, 0.5, 0.7, 1.0]
N_SEEDS = 5
N_BASELINE = 500
N_CONTAMINATED = 100


# ════════════════════════════════════════════════════════════════════════════
#  MH-DIF CORE
# ════════════════════════════════════════════════════════════════════════════
def mh_dif_subset(X_ref, X_foc, n_strata=5, anchor_cols=None,
                  external_scores_ref=None, external_scores_foc=None):
    """
    Purified MH-DIF for all columns.

    Stratification source (in priority order):
      1. external_scores_ref/foc — precomputed ability scores (e.g. full-matrix total)
      2. anchor_cols — total score from specified columns only
      3. None — standard purified (all cols minus current)
    """
    J = X_ref.shape[1]
    use_external = external_scores_ref is not None

    if not use_external:
        if anchor_cols is not None:
            tot_ref = X_ref[:, anchor_cols].sum(axis=1).astype(np.float64)
            tot_foc = X_foc[:, anchor_cols].sum(axis=1).astype(np.float64)
            anchor_set = set(anchor_cols.tolist()) if hasattr(anchor_cols, 'tolist') else set(anchor_cols)
        else:
            tot_ref = X_ref.sum(axis=1).astype(np.float64)
            tot_foc = X_foc.sum(axis=1).astype(np.float64)
            anchor_set = None

    rows = []
    for j in range(J):
        if use_external:
            s_ref = external_scores_ref
            s_foc = external_scores_foc
        elif anchor_set is not None:
            if j in anchor_set:
                s_ref = tot_ref - X_ref[:, j].astype(np.float64)
                s_foc = tot_foc - X_foc[:, j].astype(np.float64)
            else:
                s_ref = tot_ref
                s_foc = tot_foc
        else:
            s_ref = tot_ref - X_ref[:, j].astype(np.float64)
            s_foc = tot_foc - X_foc[:, j].astype(np.float64)

        s_all = np.concatenate([s_ref, s_foc])
        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
        if len(edges) < 2:
            rows.append(_nan_row(j))
            continue
        n_bins = len(edges) - 1

        k_ref = np.digitize(s_ref, edges[1:-1])
        k_foc = np.digitize(s_foc, edges[1:-1])

        R = S = 0.0
        sum_diff = 0.0
        sum_var = 0.0
        pr = ps_qr = qs = 0.0
        n_ok = 0

        for k in range(n_bins):
            mr = (k_ref == k)
            mf = (k_foc == k)
            n1 = int(mr.sum())
            n0 = int(mf.sum())
            if n1 == 0 or n0 == 0:
                continue

            A = float(X_ref[mr, j].sum())
            B = float(n1 - A)
            C = float(X_foc[mf, j].sum())
            D = float(n0 - C)
            Nk = float(n1 + n0)
            m1 = A + C
            m0 = B + D

            if m1 == 0 or m0 == 0 or Nk <= 1:
                continue
            n_ok += 1

            Rk = A * D / Nk
            Sk = B * C / Nk
            R += Rk
            S += Sk

            EA = n1 * m1 / Nk
            sum_diff += A - EA
            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))

            Pk = (A + D) / Nk
            Qk = (B + C) / Nk
            pr += Pk * Rk
            ps_qr += Pk * Sk + Qk * Rk
            qs += Qk * Sk

        if n_ok == 0 or (R == 0 and S == 0):
            rows.append(_nan_row(j))
            continue

        if S == 0:
            alpha, delta, se = np.inf, -np.inf, np.nan
        elif R == 0:
            alpha, delta, se = 0.0, np.inf, np.nan
        else:
            alpha = R / S
            delta = -2.35 * np.log(alpha)
            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)
            se = 2.35 * np.sqrt(v) if v > 0 else np.nan

        if sum_var > 0:
            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
        else:
            chi2_stat = pval = np.nan

        ad = abs(delta) if np.isfinite(delta) else np.inf
        if ad < 1.0:
            ets = "A"
        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:
            ets = "C"
        else:
            ets = "B"

        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,
                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))

    return pd.DataFrame(rows)


def _nan_row(j):
    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,
                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class="A")


# ════════════════════════════════════════════════════════════════════════════
#  DATA LOADING
# ════════════════════════════════════════════════════════════════════════════
print("=== Loading data ===")
mat = load_npz(BASE / "response_matrix.npz")
idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
MODEL_NAMES = idx["model_names"]
ITEM_IDS = idx["item_ids"]
ITEM2COL = {iid: i for i, iid in enumerate(ITEM_IDS)}

model_meta = pd.read_csv(BASE / "model_metadata.csv")
li_labels = pd.read_csv(BASE / "mmlu_li2024_proxy_labels.csv")
ability_dif = pd.read_csv(BASE / "plan_001" / "dif_results_ability.csv")

NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}
N_MODELS, J_FULL = mat.shape
print(f"  Matrix: {N_MODELS} × {J_FULL}")

# Precompute full-matrix total scores (for external matching)
print("  Computing full-matrix total scores...")
full_totals = np.asarray(mat.sum(axis=1)).ravel().astype(np.float64)  # (5227,)
print(f"  Full total scores: mean={full_totals.mean():.1f}, "
      f"range=[{full_totals.min():.0f}, {full_totals.max():.0f}]")


# ════════════════════════════════════════════════════════════════════════════
#  STEP 1: SELECT BASELINE ITEMS
# ════════════════════════════════════════════════════════════════════════════
print("\n=== Step 1: Selecting baseline items ===")
merged = ability_dif.merge(li_labels[["item_id", "contamination_type"]], on="item_id", how="inner")
baseline_pool = merged[(merged["contamination_type"] == "clean") & (merged["ets_class"] == "A")]
print(f"  Baseline pool (clean + ETS A in ability DIF): {len(baseline_pool)}")

baseline_items = baseline_pool.sample(N_BASELINE, random_state=42)
baseline_item_ids = baseline_items["item_id"].values
baseline_col_indices = np.array([ITEM2COL[iid] for iid in baseline_item_ids])
print(f"  Selected {N_BASELINE} baseline items")


# ════════════════════════════════════════════════════════════════════════════
#  STEP 2: DEFINE COHORTS
# ════════════════════════════════════════════════════════════════════════════
print("\n=== Step 2: Defining cohorts ===")


def get_row_indices(col, values):
    names = model_meta.loc[model_meta[col].isin(values), "model_name"]
    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])


cohort_defs = {}

# (a) Ability cohort
ref_ability_idx = get_row_indices("cohort_accuracy_quintile", [1, 2])
foc_ability_idx = get_row_indices("cohort_accuracy_quintile", [4, 5])

ref_acc = model_meta.loc[model_meta["cohort_accuracy_quintile"].isin([1, 2]), "accuracy"]
foc_acc = model_meta.loc[model_meta["cohort_accuracy_quintile"].isin([4, 5]), "accuracy"]
ab_overlap_min = max(ref_acc.min(), foc_acc.min())
ab_overlap_max = min(ref_acc.max(), foc_acc.max())

if ab_overlap_min <= ab_overlap_max:
    foc_ab_inject_mask = (
        model_meta["cohort_accuracy_quintile"].isin([4, 5]) &
        (model_meta["accuracy"] >= ab_overlap_min) &
        (model_meta["accuracy"] <= ab_overlap_max)
    )
    foc_ab_inject_idx = np.array([NAME2ROW[n] for n in model_meta.loc[foc_ab_inject_mask, "model_name"] if n in NAME2ROW])
else:
    foc_ab_inject_idx = foc_ability_idx

print(f"  Ability: ref={len(ref_ability_idx)} (Q1-2), foc={len(foc_ability_idx)} (Q4-5)")
print(f"    Accuracy overlap: [{ab_overlap_min:.4f}, {ab_overlap_max:.4f}]"
      f" → {'EMPTY, injecting all focal' if ab_overlap_min > ab_overlap_max else f'{len(foc_ab_inject_idx)} focal models'}")

cohort_defs["ability"] = dict(
    ref_idx=ref_ability_idx, foc_idx=foc_ability_idx,
    foc_inject_idx=foc_ab_inject_idx
)

# (b) Temporal cohort
ref_temporal_idx = get_row_indices("cohort_temporal", ["2023"])
foc_temporal_idx = get_row_indices("cohort_temporal", ["2024"])

ref_t_acc = model_meta.loc[model_meta["cohort_temporal"] == "2023", "accuracy"]
foc_t_acc = model_meta.loc[model_meta["cohort_temporal"] == "2024", "accuracy"]
t_overlap_min = max(ref_t_acc.min(), foc_t_acc.min())
t_overlap_max = min(ref_t_acc.max(), foc_t_acc.max())

foc_t_inject_mask = (
    (model_meta["cohort_temporal"] == "2024") &
    (model_meta["accuracy"] >= t_overlap_min) &
    (model_meta["accuracy"] <= t_overlap_max)
)
foc_t_inject_idx = np.array([NAME2ROW[n] for n in model_meta.loc[foc_t_inject_mask, "model_name"] if n in NAME2ROW])

print(f"  Temporal: ref={len(ref_temporal_idx)} (2023), foc={len(foc_temporal_idx)} (2024)")
print(f"    Accuracy overlap: [{t_overlap_min:.4f}, {t_overlap_max:.4f}]"
      f" → {len(foc_t_inject_idx)} focal models for injection")

cohort_defs["temporal"] = dict(
    ref_idx=ref_temporal_idx, foc_idx=foc_temporal_idx,
    foc_inject_idx=foc_t_inject_idx
)


# ════════════════════════════════════════════════════════════════════════════
#  STEP 3-4: INJECTION + MH-DIF
# ════════════════════════════════════════════════════════════════════════════
print("\n=== Step 3-4: Injection + MH-DIF ===")

X_base = mat[:, baseline_col_indices].toarray().astype(np.int8)
print(f"  Baseline submatrix: {X_base.shape}, density: {X_base.mean():.4f}")

injection_rows = []
per_item_rows = []

MH_VARIANTS = ["standard", "anchor", "external"]

total_runs = len(INJECTION_PS) * N_SEEDS * len(cohort_defs) * len(MH_VARIANTS)
run_count = 0
t_start = time.time()

for cohort_name, cdef in cohort_defs.items():
    ref_idx = cdef["ref_idx"]
    foc_idx = cdef["foc_idx"]
    foc_inject_idx = cdef["foc_inject_idx"]

    # External scores for this cohort (from full original matrix)
    ext_ref = full_totals[ref_idx]
    ext_foc = full_totals[foc_idx]

    for p in INJECTION_PS:
        for seed in range(1, N_SEEDS + 1):
            rng = np.random.RandomState(seed)

            contam_local_idx = rng.choice(N_BASELINE, N_CONTAMINATED, replace=False)
            contam_set = set(contam_local_idx.tolist())
            clean_local_idx = np.array([i for i in range(N_BASELINE) if i not in contam_set])

            X_inj = X_base.copy()
            n_flipped = 0

            if p > 0:
                for local_j in contam_local_idx:
                    for model_row in foc_inject_idx:
                        if X_inj[model_row, local_j] == 0:
                            if rng.random() < p:
                                X_inj[model_row, local_j] = 1
                                n_flipped += 1

            orig_density = X_base[np.ix_(foc_inject_idx, contam_local_idx)].mean()
            new_density = X_inj[np.ix_(foc_inject_idx, contam_local_idx)].mean()

            X_ref = X_inj[ref_idx]
            X_foc = X_inj[foc_idx]

            for variant in MH_VARIANTS:
                run_count += 1

                if variant == "anchor":
                    dif_results = mh_dif_subset(X_ref, X_foc, n_strata=5,
                                                anchor_cols=clean_local_idx)
                elif variant == "external":
                    dif_results = mh_dif_subset(X_ref, X_foc, n_strata=5,
                                                external_scores_ref=ext_ref,
                                                external_scores_foc=ext_foc)
                else:
                    dif_results = mh_dif_subset(X_ref, X_foc, n_strata=5)

                contam_mask = dif_results["col_idx"].isin(contam_set)
                clean_mask = ~contam_mask

                contam_results = dif_results[contam_mask]
                clean_results = dif_results[clean_mask]

                n_c_contam = (contam_results["ets_class"] == "C").sum()
                n_c_clean = (clean_results["ets_class"] == "C").sum()
                tpr = n_c_contam / N_CONTAMINATED
                fpr = n_c_clean / (N_BASELINE - N_CONTAMINATED)

                table = [[n_c_contam, N_CONTAMINATED - n_c_contam],
                         [n_c_clean, (N_BASELINE - N_CONTAMINATED) - n_c_clean]]
                fisher_or, fisher_p = fisher_exact(table)

                injection_rows.append(dict(
                    p=p, seed=seed, cohort_type=cohort_name,
                    mh_variant=variant,
                    n_baseline=N_BASELINE, n_contaminated=N_CONTAMINATED,
                    n_clean=N_BASELINE - N_CONTAMINATED,
                    n_foc_inject=len(foc_inject_idx),
                    tpr=tpr, fpr=fpr,
                    fisher_or=fisher_or, fisher_p=fisher_p,
                    n_responses_flipped=n_flipped,
                    orig_density=orig_density, new_density=new_density,
                ))

                # Per-item results only for anchor variant (keeps CSV manageable)
                if variant == "anchor":
                    for _, row in dif_results.iterrows():
                        local_j = int(row["col_idx"])
                        per_item_rows.append(dict(
                            item_id=baseline_item_ids[local_j],
                            p=p, seed=seed, cohort_type=cohort_name,
                            mh_variant=variant,
                            delta_mh=row["delta_mh"], p_value=row["p_value"],
                            ets_class=row["ets_class"],
                            is_injected=local_j in contam_set,
                        ))

                elapsed = time.time() - t_start
                if variant == "external" or (variant == "standard" and p in [0.0, 1.0]):
                    print(f"  [{run_count}/{total_runs}] {cohort_name} {variant:8s} p={p} seed={seed}: "
                          f"TPR={tpr:.3f} FPR={fpr:.3f} flipped={n_flipped} "
                          f"({elapsed:.0f}s)")


# ════════════════════════════════════════════════════════════════════════════
#  STEP 5-6: AGGREGATE & SAVE
# ════════════════════════════════════════════════════════════════════════════
print("\n=== Step 5: Aggregating results ===")

inj_df = pd.DataFrame(injection_rows)
per_item_df = pd.DataFrame(per_item_rows)

summary_rows = []
for (p_val, cohort, variant), grp in inj_df.groupby(["p", "cohort_type", "mh_variant"]):
    summary_rows.append(dict(
        p=p_val, cohort_type=cohort, mh_variant=variant,
        tpr_mean=grp["tpr"].mean(), tpr_std=grp["tpr"].std(),
        fpr_mean=grp["fpr"].mean(), fpr_std=grp["fpr"].std(),
        fisher_or_mean=grp["fisher_or"].mean(),
        fisher_p_median=grp["fisher_p"].median(),
    ))
summary_df = pd.DataFrame(summary_rows)

inj_df.to_csv(OUT / "injection_results.csv", index=False)
summary_df.to_csv(OUT / "dose_response_summary.csv", index=False)
per_item_df.to_csv(OUT / "per_item_results.csv", index=False)
print(f"  Saved injection_results.csv ({len(inj_df)} rows)")
print(f"  Saved dose_response_summary.csv ({len(summary_df)} rows)")
print(f"  Saved per_item_results.csv ({len(per_item_df)} rows)")


# ════════════════════════════════════════════════════════════════════════════
#  REPORT
# ════════════════════════════════════════════════════════════════════════════
print("\n=== Generating report ===")

L = []
def w(s=""):
    L.append(s)

w("# Plan 011: Semi-Synthetic DIF Validation")
w()
w("## 1. Objective")
w()
w("Inject known **differential** contamination into real MMLU response data and test")
w("whether MH-DIF can detect it. This validates whether plan_001/001b's failure to find")
w("enrichment was due to Li et al. labels being non-differential (global contamination)")
w("rather than a fundamental limitation of MH-DIF.")
w()

w("## 2. Setup")
w()
w(f"- **Baseline items**: {N_BASELINE} (clean in Li et al. + ETS A in plan_001 ability DIF)")
w(f"- **Contaminated per run**: {N_CONTAMINATED} of {N_BASELINE}")
w(f"- **Injection probabilities**: {INJECTION_PS}")
w(f"- **Seeds per p**: {N_SEEDS}")
w()
w("### Cohort definitions")
w()
for cn, cd in cohort_defs.items():
    w(f"- **{cn}**: ref N={len(cd['ref_idx'])}, foc N={len(cd['foc_idx'])}, "
      f"foc inject N={len(cd['foc_inject_idx'])}")
w()

if ab_overlap_min > ab_overlap_max:
    w("> **Note**: Ability quintiles (Q1-2 vs Q4-5) have no accuracy overlap by construction "
      f"(ref max={ref_acc.max():.4f}, foc min={foc_acc.min():.4f}). "
      "All focal models used for injection. MH stratification handles ability matching.")
    w()

w("### MH variants")
w()
w("| Variant | Matching variable | Rationale |")
w("|---------|-------------------|-----------|")
w("| standard | sum of 500 items − current | Same as plan_001; susceptible to matching variable contamination when 20% items injected |")
w("| anchor | sum of 400 known-clean items | Eliminates matching variable contamination; assumes oracle knowledge of clean items |")
w("| external | sum of all 12,508 items (original, pre-injection) | Best matching precision; immune to injection; requires external ability estimate |")
w()

w("## 3. Results by MH Variant")
w()
for variant in MH_VARIANTS:
    w(f"### {variant.capitalize()} MH")
    w()
    w("| Cohort | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |")
    w("|--------|---|----------------|----------------|------|-----------|----------|")
    sub = summary_df[summary_df["mh_variant"] == variant]
    for _, r in sub.sort_values(["cohort_type", "p"]).iterrows():
        # ΔTPR = TPR - baseline TPR at p=0
        base_tpr = sub[(sub["cohort_type"] == r.cohort_type) & (sub["p"] == 0.0)]["tpr_mean"].values
        d_tpr = r.tpr_mean - base_tpr[0] if len(base_tpr) > 0 else 0
        w(f"| {r.cohort_type} | {r.p} | {r.tpr_mean:.3f}±{r.tpr_std:.3f} | "
          f"{r.fpr_mean:.3f}±{r.fpr_std:.3f} | {d_tpr:+.3f} | "
          f"{r.fisher_or_mean:.2f} | {r.fisher_p_median:.4f} |")
    w()

w("## 4. Key Comparison: Baseline FPR by Variant")
w()
w("| Cohort | standard | anchor | external |")
w("|--------|----------|--------|----------|")
for cohort in ["ability", "temporal"]:
    vals = []
    for variant in MH_VARIANTS:
        r = summary_df[(summary_df["p"] == 0.0) & (summary_df["cohort_type"] == cohort) &
                       (summary_df["mh_variant"] == variant)]
        vals.append(f"{r.iloc[0]['fpr_mean']:.3f}" if len(r) > 0 else "—")
    w(f"| {cohort} | {vals[0]} | {vals[1]} | {vals[2]} |")
w()
w("If external FPR ≪ standard FPR, the high baseline rate is from matching precision,")
w("not inherent DIF in the selected items.")
w()

w("## 5. Sanity Checks")
w()
w("### Density change (focal × contaminated items)")
w()
w("| Cohort | p | Orig density | Post density | Responses flipped |")
w("|--------|---|--------------|--------------|-------------------|")
for (p_val, cohort), grp in inj_df[inj_df["mh_variant"] == "standard"].groupby(["p", "cohort_type"]):
    if p_val == 0:
        continue
    w(f"| {cohort} | {p_val} | {grp['orig_density'].mean():.4f} | "
      f"{grp['new_density'].mean():.4f} | {grp['n_responses_flipped'].mean():.0f} |")
w()

w("## 6. Verdict")
w()

for variant in MH_VARIANTS:
    w(f"### {variant.capitalize()} MH")
    w()
    sub = summary_df[summary_df["mh_variant"] == variant]

    for cohort in ["ability", "temporal"]:
        c_sub = sub[sub["cohort_type"] == cohort]
        p0 = c_sub[c_sub["p"] == 0.0]
        p1 = c_sub[c_sub["p"] == 1.0]
        if len(p1) == 0 or len(p0) == 0:
            continue

        fpr0 = p0.iloc[0]["fpr_mean"]
        tpr0 = p0.iloc[0]["tpr_mean"]
        tpr1 = p1.iloc[0]["tpr_mean"]
        fpr1 = p1.iloc[0]["fpr_mean"]
        d_tpr = tpr1 - tpr0

        w(f"**{cohort}**: baseline TPR={tpr0:.3f}/FPR={fpr0:.3f}, "
          f"p=1.0 TPR={tpr1:.3f}/FPR={fpr1:.3f}, ΔTPR={d_tpr:+.3f}")

        if d_tpr > 0.3 and tpr1 > 0.5:
            w(f"→ **SUCCESS**: injection raises TPR by {d_tpr:.3f} with clear dose-response")
        elif d_tpr > 0.1:
            w(f"→ **PARTIAL**: detectable signal (ΔTPR={d_tpr:.3f}) but modest")
        else:
            w(f"→ **FAIL**: ΔTPR={d_tpr:.3f} too small to indicate detection")
        w()

w("## 7. Overall Interpretation")
w()
w("### Does MH-DIF detect differential contamination?")
w()

# Compute key numbers for conclusion
ext_t = summary_df[(summary_df["mh_variant"] == "external") & (summary_df["cohort_type"] == "temporal")]
ext_a = summary_df[(summary_df["mh_variant"] == "external") & (summary_df["cohort_type"] == "ability")]

if len(ext_t) > 0:
    ext_t_p0 = ext_t[ext_t["p"] == 0.0]["tpr_mean"].values[0]
    ext_t_p1 = ext_t[ext_t["p"] == 1.0]["tpr_mean"].values[0]
    ext_t_fpr0 = ext_t[ext_t["p"] == 0.0]["fpr_mean"].values[0]
    ext_t_fpr1 = ext_t[ext_t["p"] == 1.0]["fpr_mean"].values[0]
    w(f"- **Temporal + external matching**: TPR rises {ext_t_p0:.3f} → {ext_t_p1:.3f} "
      f"(ΔTPR=+{ext_t_p1-ext_t_p0:.3f}), FPR {ext_t_fpr0:.3f} → {ext_t_fpr1:.3f}")

if len(ext_a) > 0:
    ext_a_p0 = ext_a[ext_a["p"] == 0.0]["tpr_mean"].values[0]
    ext_a_p1 = ext_a[ext_a["p"] == 1.0]["tpr_mean"].values[0]
    ext_a_fpr0 = ext_a[ext_a["p"] == 0.0]["fpr_mean"].values[0]
    ext_a_fpr1 = ext_a[ext_a["p"] == 1.0]["fpr_mean"].values[0]
    w(f"- **Ability + external matching**: TPR rises {ext_a_p0:.3f} → {ext_a_p1:.3f} "
      f"(ΔTPR=+{ext_a_p1-ext_a_p0:.3f}), FPR {ext_a_fpr0:.3f} → {ext_a_fpr1:.3f}")

w()
w("### Implications for plan_001")
w()
w("If semi-synthetic injection is detectable → plan_001's failure to find enrichment")
w("against Li et al. labels is because Li et al. contamination is **non-differential**")
w("(Common Crawl data available to all models), not because MH-DIF is fundamentally limited.")
w()
w("### Matching variable contamination")
w()
w("When 20% of items are injected, standard MH's matching variable (total score) is")
w("corrupted by injected items, inflating FPR. This is a known limitation when DIF items")
w("constitute a large fraction of the test. In practice, iterative purification (exclude")
w("suspected DIF items from matching) or external ability estimates mitigate this.")
w()

(OUT / "plan_011_report.md").write_text("\n".join(L) + "\n")
print("  Report written.")

# Console summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
for variant in MH_VARIANTS:
    print(f"\n--- {variant} MH ---")
    sub = summary_df[summary_df["mh_variant"] == variant]
    for _, r in sub.sort_values(["cohort_type", "p"]).iterrows():
        print(f"  {r.cohort_type:8s} p={r.p}: TPR={r.tpr_mean:.3f}±{r.tpr_std:.3f}  "
              f"FPR={r.fpr_mean:.3f}±{r.fpr_std:.3f}")

total_elapsed = time.time() - t_start
print(f"\nTotal time: {total_elapsed:.0f}s")
print(f"All outputs saved to {OUT}")
```

---

## Key Insights

1. **Contaminated Item Selection**: Randomly samples 100 items per run (seeded), ensuring stochastic replication.

2. **Ability-Overlapping Models**: Uses accuracy ranges to find models in the focal cohort that fall within the reference accuracy range. This ensures that injected contamination affects ability-matched focal models only.

3. **Flipping Mechanism**: Only flips incorrect responses (0 → 1) with probability p per focal model per item. Never flips correct responses back to incorrect.

4. **Three-Variant MH Approach**:
   - **Standard**: Most realistic but vulnerable to matching variable contamination
   - **Anchor**: Oracle-clean validation (20% of items not contaminated)
   - **External**: Immune to all injection effects, measures best-case DIF detection

5. **Dose-Response Design**: By varying p ∈ [0.0, 0.3, 0.5, 0.7, 1.0], the script validates whether MH-DIF shows monotonic increase in TPR with injection strength.

6. **Fisher Exact Test**: Validates that the association between DIF detection (class C) and contamination status is significant, accounting for small-cell counts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28a329d4-e2b4-4c80-8b2f-488c5b966179",
  "isSidechain": true,
  "agentId": "af14da85843b71e93",
  "requestId": "req_011CbEoHfC1JARfCViarHc3N",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9240dd0b-f697-4d43-bcb4-0091c544fa23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "c9888f1d-7b39-4f56-88ab-428b671b99c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LkyGZQ1xJG72EPEDoPbVxy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 10278,
      "cache_read_input_tokens": 20701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10278,
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
