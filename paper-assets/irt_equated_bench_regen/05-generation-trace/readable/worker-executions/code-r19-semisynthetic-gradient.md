# code r19 semisynthetic gradient

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 128
- **Recorded user turns:** 1
- **Tool calls:** 40
- **Original source:** `logs/workers/worker_code_r19_semisynthetic_gradient_20260522T184822.log`
- **Structured JSON:** [`576c4576060a1e219b64.json`](../../sessions/57/576c4576060a1e219b64.json)

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
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
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
  "uuid": "27934550-f3a5-44c0-9933-03ff193b37e0",
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
    "resetsAt": 1779493200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "2ba438c8-7797-45a6-9477-ae69f2421e55",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me understand the task: I need to implement a semi-synthetic injection experiment (R19 Exp 4) that tests whether MH-DIF can distinguish between capability-like and contamination-like DIF patterns. Let me start by examining the reference code and data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "66174716-ed31-4280-b67d-e139c4313b6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJFWi5RdoMwjKyFDLzzHcM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13548,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13548
      },
      "output_tokens": 25,
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

I'll start by examining the reference code and data files to understand the existing MH-DIF pipeline and data structures.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "1cecc665-6ecd-4749-b676-07504418dae0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJFWi5RdoMwjKyFDLzzHcM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13548,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13548
      },
      "output_tokens": 25,
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

<details open><summary>🔧 Tool call — Agent · `toolu_01NigzqdFSxPJzjAsgvDn9Ye`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore reference code and data",
  "prompt": "I need to understand the existing MH-DIF pipeline and data structures in this project. Please find and read the following files:\n\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py` — the semi-synthetic injection + MH-DIF pipeline reference\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py` — contains `mh_dif_c_pct_vec()` function\n\nFor each file, I need:\n- The full MH-DIF calculation logic (especially the vectorized version)\n- How injection is done in plan_011\n- How cohorts are split (ref vs focal)\n- How results are reported\n\nAlso check if model_metadata.csv exists at the artifacts root and what columns it has. Search breadth: very thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "487121bf-1c7f-4d5e-a900-757b1bb22167",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJFWi5RdoMwjKyFDLzzHcM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13548,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13548
      },
      "output_tokens": 25,
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
  "task_id": "a5459180bf034abb6",
  "tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "description": "Explore reference code and data",
  "task_type": "local_agent",
  "prompt": "I need to understand the existing MH-DIF pipeline and data structures in this project. Please find and read the following files:\n\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py` — the semi-synthetic injection + MH-DIF pipeline reference\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py` — contains `mh_dif_c_pct_vec()` function\n\nFor each file, I need:\n- The full MH-DIF calculation logic (especially the vectorized version)\n- How injection is done in plan_011\n- How cohorts are split (ref vs focal)\n- How results are reported\n\nAlso check if model_metadata.csv exists at the artifacts root and what columns it has. Search breadth: very thorough.",
  "uuid": "3a16df31-f27d-4a26-bd3e-48f4895bf662",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

## Round 1

121 recorded events

### User

_source line 8 · 2026-05-22T18:48:37.464Z_

I need to understand the existing MH-DIF pipeline and data structures in this project. Please find and read the following files:

1. `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py` — the semi-synthetic injection + MH-DIF pipeline reference
2. `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py` — contains `mh_dif_c_pct_vec()` function

For each file, I need:
- The full MH-DIF calculation logic (especially the vectorized version)
- How injection is done in plan_011
- How cohorts are split (ref vs focal)
- How results are reported

Also check if model_metadata.csv exists at the artifacts root and what columns it has. Search breadth: very thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "0df41016-f88a-4545-b672-b8def4920f4d"
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
  "task_id": "a5459180bf034abb6",
  "tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "description": "Reading artifacts/plan_011/plan_011_analysis.py",
  "usage": {
    "total_tokens": 15657,
    "tool_uses": 1,
    "duration_ms": 1625
  },
  "last_tool_name": "Read",
  "uuid": "041a8798-d27b-43b7-9742-1b5d883f64e1",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_012mm7St2nvN4dFzhKWKUTQ4`</summary>

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
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "9bd606ae-044b-4f03-8c5c-a67be9b3dc7c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DDaoemuMQ2ihiBKbiXMpeB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 14970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 668,
        "ephemeral_1h_input_tokens": 0
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

_source line 11 · 2026-05-22T18:48:39.139Z_

<details><summary>↩ Tool result · `toolu_012mm7St2nvN4dFzhKWKUTQ4`</summary>

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
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "d8097d4f-2fd5-48b6-91db-94c79e875c90"
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
  "task_id": "a5459180bf034abb6",
  "tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "description": "Reading artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py",
  "usage": {
    "total_tokens": 15665,
    "tool_uses": 2,
    "duration_ms": 1883
  },
  "last_tool_name": "Read",
  "uuid": "ac2fb4dc-58b9-453b-aac9-ecacf627474c",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01RwTkSYWLr2MZtvHDcoYeR1`</summary>

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
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "1339141b-e5d1-4957-8c76-174ac959472f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DDaoemuMQ2ihiBKbiXMpeB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 14970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 668,
        "ephemeral_1h_input_tokens": 0
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

_source line 14 · 2026-05-22T18:48:39.355Z_

<details><summary>↩ Tool result · `toolu_01RwTkSYWLr2MZtvHDcoYeR1`</summary>

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
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "40159eea-d43f-430c-a055-7fa6116bd757"
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
  "task_id": "a5459180bf034abb6",
  "tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 15673,
    "tool_uses": 3,
    "duration_ms": 2046
  },
  "last_tool_name": "Bash",
  "uuid": "667fc035-3e06-4202-a3ea-24e3f63979b4",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01HAgm8msoSNvs527jgsnScy`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep -E \"model_metadata|csv\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "9957ecb4-207b-41f5-97f0-0c2a9e95b63e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DDaoemuMQ2ihiBKbiXMpeB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 14970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 668,
        "ephemeral_1h_input_tokens": 0
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

_source line 17 · 2026-05-22T18:48:39.766Z_

<details><summary>↩ Tool result · `toolu_01HAgm8msoSNvs527jgsnScy`</summary>

```text
-rw-r--r--  1 ubuntu ubuntu     2728 May 20 18:39 dif_diagnostic_tpr_comparison.csv
-rw-r--r--  1 ubuntu ubuntu     1956 May 20 19:27 dif_phase2_results.csv
-rw-r--r--  1 ubuntu ubuntu     3114 May 20 18:36 dif_power_results.csv
-rw-r--r--  1 ubuntu ubuntu  1528143 May 20 20:57 item_metadata.csv
-rw-r--r--  1 ubuntu ubuntu      451 May 20 19:51 metabench_cohort_analysis.csv
-rw-r--r--  1 ubuntu ubuntu  1312294 May 20 19:46 metabench_ctt_stats.csv
-rw-r--r--  1 ubuntu ubuntu   263952 May 20 19:46 metabench_model_accuracy.csv
-rw-r--r--  1 ubuntu ubuntu    32891 May 20 19:51 metabench_rl_models.csv
-rw-r--r--  1 ubuntu ubuntu     3455 May 20 19:51 metabench_subject_stats.csv
-rw-r--r--  1 ubuntu ubuntu   953704 May 20 20:41 mmlu_li2024_proxy_labels.csv
-rw-r--r--  1 ubuntu ubuntu   399283 May 20 20:51 model_metadata.csv
-rw-r--r--  1 ubuntu ubuntu  1781602 May 20 18:56 psn_irt_item_parameters.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "61811a22-f6ad-4e57-a53a-b301bc7ac688"
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
  "task_id": "a5459180bf034abb6",
  "tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "description": "Reading artifacts/model_metadata.csv",
  "usage": {
    "total_tokens": 33442,
    "tool_uses": 4,
    "duration_ms": 4709
  },
  "last_tool_name": "Read",
  "uuid": "6177b35b-851d-47dc-8ca8-017605d5a8e2",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01LMkSKzNw1dGe2aZvpcFAUt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv",
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "adebb901-2642-4b97-8678-690e2a670ee2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KU8Pn4qDZ697taHjxX1emc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 17755,
      "cache_read_input_tokens": 15638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17755,
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

_source line 20 · 2026-05-22T18:48:42.181Z_

<details><summary>↩ Tool result · `toolu_01LMkSKzNw1dGe2aZvpcFAUt`</summary>

```text
1	model_name,family,release_year,release_half,training_method,accuracy,cohort_temporal,cohort_accuracy_quintile
2	0-hero/Matter-0.1-7B,unknown,unknown,unknown,unknown,0.661225,other,3
3	0-hero/Matter-0.1-7B-DPO-preview,,unknown,unknown,DPO,0.661337,other,3
4	0-hero/Matter-0.1-7B-boost,unknown,unknown,unknown,unknown,0.653422,other,3
5	0-hero/Matter-0.1-7B-boost-DPO,,unknown,unknown,DPO,0.654941,other,3
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "7deba2c8-959e-40df-bcc7-66ba97e6a0be"
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
  "task_id": "a5459180bf034abb6",
  "tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "description": "Running wc -l /home/ubuntu/.agent-ml-research-idea_gen_05…",
  "usage": {
    "total_tokens": 33769,
    "tool_uses": 5,
    "duration_ms": 6447
  },
  "last_tool_name": "Bash",
  "uuid": "d1082f23-8bc0-4fb3-b355-3e7f276ed3d3",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01GmgQX5zF7sK4kcgaxVjRBC`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "3316faa2-b5d2-4834-9b1e-606c95cb7206",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01585LoYMjBciRBjSo6KzTpm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 326,
      "cache_read_input_tokens": 33393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 326,
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

_source line 23 · 2026-05-22T18:48:43.986Z_

<details><summary>↩ Tool result · `toolu_01GmgQX5zF7sK4kcgaxVjRBC`</summary>

```text
5228 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "50427f26-3376-4c15-89bf-928d9da7ebc1"
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
  "task_id": "a5459180bf034abb6",
  "tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "description": "Reading artifacts/model_metadata.csv",
  "usage": {
    "total_tokens": 33770,
    "tool_uses": 6,
    "duration_ms": 6725
  },
  "last_tool_name": "Read",
  "uuid": "83531b55-61f8-4da3-890f-c5f2071f43f8",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01WAFYs9TfpvNfR45jkdP7aS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv",
  "limit": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "97638e52-5d40-4afd-bc7f-782589cd94fc",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01585LoYMjBciRBjSo6KzTpm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 326,
      "cache_read_input_tokens": 33393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 326,
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

_source line 26 · 2026-05-22T18:48:44.235Z_

<details><summary>↩ Tool result · `toolu_01WAFYs9TfpvNfR45jkdP7aS`</summary>

```text
1	model_name,family,release_year,release_half,training_method,accuracy,cohort_temporal,cohort_accuracy_quintile
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "963d8c9c-e265-4342-b5d2-9a7e929b5b0c"
}
```

</details>

---

### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5459180bf034abb6",
  "tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "description": "Running ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 33771,
    "tool_uses": 7,
    "duration_ms": 6962
  },
  "last_tool_name": "Bash",
  "uuid": "2ce6235b-7f60-4380-a010-81188d3f3cbd",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01NTKn6BbMr4RtAVpDHu4s3X`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "e1900c9f-d82e-4836-8d3e-179d71ef9faf",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01585LoYMjBciRBjSo6KzTpm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 326,
      "cache_read_input_tokens": 33393,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 326,
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

_source line 29 · 2026-05-22T18:48:44.525Z_

<details><summary>↩ Tool result · `toolu_01NTKn6BbMr4RtAVpDHu4s3X`</summary>

```text
total 2.1M
-rw-r--r-- 1 ubuntu ubuntu 3.6K May 20 21:48 dose_response_summary.csv
-rw-r--r-- 1 ubuntu ubuntu  19K May 20 21:48 injection_results.csv
-rw-r--r-- 1 ubuntu ubuntu 2.0M May 20 21:48 per_item_results.csv
-rw-r--r-- 1 ubuntu ubuntu  26K May 20 21:48 plan_011_analysis.py
-rw-r--r-- 1 ubuntu ubuntu 6.9K May 20 21:48 plan_011_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "6af9a640-8cd8-4515-9fdc-d97e1578c575"
}
```

</details>

---

### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5459180bf034abb6",
  "tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "description": "Reading artifacts/plan_011/dose_response_summary.csv",
  "usage": {
    "total_tokens": 34397,
    "tool_uses": 8,
    "duration_ms": 8488
  },
  "last_tool_name": "Read",
  "uuid": "7c8b4a36-5605-481d-a6ba-fa93de3fc883",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01T4YBYcjR4jj9FvxYEVoSYP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/dose_response_summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "667e0355-5a89-4432-a788-83db24c91354",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VbY2VZgiafjZvJ2z5UQsJN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 623,
      "cache_read_input_tokens": 33719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 623,
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

_source line 32 · 2026-05-22T18:48:45.959Z_

<details><summary>↩ Tool result · `toolu_01T4YBYcjR4jj9FvxYEVoSYP`</summary>

```text
1	p,cohort_type,mh_variant,tpr_mean,tpr_std,fpr_mean,fpr_std,fisher_or_mean,fisher_p_median
2	0.0,ability,anchor,0.6,0.05958187643906492,0.5955,0.021607290436331923,1.0425176402092453,0.48934843949095175
3	0.0,ability,external,0.49800000000000005,0.040865633483405106,0.493,0.010216408370851257,1.0376862626110337,0.5025492358221133
4	0.0,ability,standard,0.5940000000000001,0.052725705305856276,0.6114999999999999,0.013181426326464086,0.9605839309463293,0.4231473007797394
5	0.0,temporal,anchor,0.31400000000000006,0.053197744313081545,0.307,0.01848986208710059,1.0651659083562441,0.5465028509582752
6	0.0,temporal,external,0.32599999999999996,0.03507135583350037,0.3135,0.008767838958375098,1.0732098198053222,0.7202868041451116
7	0.0,temporal,standard,0.308,0.046583258795408464,0.298,0.011645814698852104,1.0740528244958572,0.8081326220818719
8	0.3,ability,anchor,0.7000000000000001,0.051478150704934986,0.5955,0.021607290436331923,1.6418565717967872,0.17314822982263203
9	0.3,ability,external,0.662,0.04438468204234428,0.493,0.010216408370851257,2.069855540970715,0.005067695426382491
10	0.3,ability,standard,0.7,0.05700877125495689,0.6094999999999999,0.02570262632494974,1.584939735800224,0.25548738941208027
11	0.3,temporal,anchor,0.5219999999999999,0.05357238094391551,0.307,0.01848986208710059,2.4925140255423237,0.00010073571834208619
12	0.3,temporal,external,0.548,0.03271085446759225,0.3135,0.008767838958375098,2.674044460691511,1.621363555997074e-05
13	0.3,temporal,standard,0.42400000000000004,0.05856620185738529,0.3895,0.017624556732014567,1.1840390749023468,0.6434635572662124
14	0.5,ability,anchor,0.764,0.03781534080237811,0.5955,0.021607290436331923,2.238876999052195,0.001423732852816243
15	0.5,ability,external,0.756,0.04098780306383843,0.493,0.010216408370851257,3.307777208034717,5.631291377561033e-07
16	0.5,ability,standard,0.76,0.04636809247747853,0.5995,0.02057000243072422,2.2105804398056343,0.006744942166107429
17	0.5,temporal,anchor,0.806,0.033615472627943205,0.307,0.01848986208710059,9.594426178873977,9.75696672274655e-19
18	0.5,temporal,external,0.834,0.027018512172212572,0.3135,0.008767838958375098,11.218776545501921,2.2435861363735885e-21
19	0.5,temporal,standard,0.6819999999999999,0.04549725266430929,0.453,0.020871631464741792,2.6307890292608733,7.959090044936087e-05
20	0.7,ability,anchor,0.808,0.04086563348340508,0.5955,0.021607290436331923,2.9806810853848242,0.0001391774728509628
21	0.7,ability,external,0.792,0.034205262752974135,0.493,0.010216408370851257,4.03899601643527,5.647245501157947e-09
22	0.7,ability,standard,0.8059999999999998,0.03577708763999661,0.598,0.030279943857279494,2.89790265706804,0.0002416205957227171
23	0.7,temporal,anchor,0.9899999999999999,0.010000000000000009,0.307,0.01848986208710059,inf,6.296440995498056e-41
24	0.7,temporal,external,0.9899999999999999,0.010000000000000009,0.3135,0.008767838958375098,inf,1.4713687189321854e-39
25	0.7,temporal,standard,0.966,0.008944271909999166,0.5025000000000001,0.02128673295740801,30.33565943696116,1.8856771022616153e-20
26	1.0,ability,anchor,0.818,0.033466401061363,0.5955,0.021607290436331923,3.16329589824156,8.96764887382088e-05
27	1.0,ability,external,0.8,0.03807886552931952,0.493,0.010216408370851257,4.295685617868518,5.432734647236026e-09
28	1.0,ability,standard,0.8160000000000001,0.03507135583350035,0.5955,0.023143573622066264,3.167875851364277,8.96764887382088e-05
29	1.0,temporal,anchor,1.0,0.0,0.307,0.01848986208710059,inf,1.0796453938821689e-42
30	1.0,temporal,external,1.0,0.0,0.3135,0.008767838958375098,inf,3.5105888936555684e-42
31	1.0,temporal,standard,1.0,0.0,0.6164999999999999,0.013986600730699362,inf,1.2252630735610078e-18
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "15a278b3-a3cb-43df-bed6-2efae9d88e94"
}
```

</details>

---

### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5459180bf034abb6",
  "tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "description": "Reading artifacts/plan_011/injection_results.csv",
  "usage": {
    "total_tokens": 34398,
    "tool_uses": 9,
    "duration_ms": 8765
  },
  "last_tool_name": "Read",
  "uuid": "e1b45465-6067-43c9-af1a-779fef926531",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_012Jhwtt6ndJuyk8G6RLdTPo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/injection_results.csv",
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "cf704635-70e0-425b-8fa5-4624e74dfe4d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VbY2VZgiafjZvJ2z5UQsJN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 623,
      "cache_read_input_tokens": 33719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 623,
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

_source line 35 · 2026-05-22T18:48:46.240Z_

<details><summary>↩ Tool result · `toolu_012Jhwtt6ndJuyk8G6RLdTPo`</summary>

```text
1	p,seed,cohort_type,mh_variant,n_baseline,n_contaminated,n_clean,n_foc_inject,tpr,fpr,fisher_or,fisher_p,n_responses_flipped,orig_density,new_density
2	0.0,1,ability,standard,500,100,400,2089,0.66,0.595,1.3213049925852693,0.2534703225124757,0,0.7268836764001915,0.7268836764001915
3	0.0,1,ability,anchor,500,100,400,2089,0.65,0.5775,1.3586889301175016,0.21129693451776466,0,0.7268836764001915,0.7268836764001915
4	0.0,1,ability,external,500,100,400,2089,0.53,0.485,1.197411713094977,0.43572180287622875,0,0.7268836764001915,0.7268836764001915
5	0.0,2,ability,standard,500,100,400,2089,0.62,0.605,1.0652457590256634,0.8195585837781214,0,0.6604021062709431,0.6604021062709431
6	0.0,2,ability,anchor,500,100,400,2089,0.61,0.6125,0.989534275248561,1.0,0,0.6604021062709431,0.6604021062709431
7	0.0,2,ability,external,500,100,400,2089,0.55,0.48,1.3240740740740742,0.22042591275534473,0,0.6604021062709431,0.6604021062709431
8	0.0,3,ability,standard,500,100,400,2089,0.57,0.6175,0.8211091234347049,0.4231473007797394,0,0.6476543800861656,0.6476543800861656
9	0.0,3,ability,anchor,500,100,400,2089,0.52,0.57,0.8172514619883041,0.37037964538025003,0,0.6476543800861656,0.6476543800861656
10	0.0,3,ability,external,500,100,400,2089,0.46,0.5025,0.8433757140224802,0.5025492358221133,0,0.6476543800861656,0.6476543800861656
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "ace24dff-9ec5-45f6-a259-f41f744119d7"
}
```

</details>

---

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a5459180bf034abb6",
  "tool_use_id": "toolu_01NigzqdFSxPJzjAsgvDn9Ye",
  "status": "completed",
  "output_file": "",
  "summary": "Explore reference code and data",
  "usage": {
    "total_tokens": 37071,
    "tool_uses": 9,
    "duration_ms": 43763
  },
  "uuid": "6cf51f94-1ab2-4e49-a269-747625364277",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### Tool result

_source line 37 · 2026-05-22T18:49:21.231Z_

<details><summary>↩ Tool result · `toolu_01NigzqdFSxPJzjAsgvDn9Ye`</summary>

````text
Perfect! Now I have all the information needed. Let me create a comprehensive summary of the MH-DIF pipeline and data structures.

## Comprehensive MH-DIF Pipeline and Data Structures Summary

I've thoroughly examined both the **plan_011_analysis.py** (semi-synthetic injection validation) and **mmlu_bootstrap_ci.py** (vectorized MH-DIF with bootstrap CI) files, plus the supporting metadata. Here's what I found:

---

### **1. MODEL_METADATA.CSV STRUCTURE**

**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv`

**Dimensions:** 5,227 models × 8 columns

**Columns:**
- `model_name` — unique model identifier
- `family` — model family/foundation (e.g., GPT, Claude, Llama)
- `release_year` — year of release
- `release_half` — H1 or H2
- `training_method` — base, DPO, SFT, etc.
- `accuracy` — continuous MMLU accuracy (0–1 range)
- `cohort_temporal` — **2023** or **2024** (temporal cohort for DIF)
- `cohort_accuracy_quintile` — **1–5** (ability quintile based on accuracy)

---

### **2. MH-DIF CORE CALCULATION LOGIC**

#### **A. Plan 011: mh_dif_subset() — Standard Stratified Approach (lines 46–167)**

**Signature:**
```python
mh_dif_subset(X_ref, X_foc, n_strata=5, anchor_cols=None,
              external_scores_ref=None, external_scores_foc=None)
```

**Inputs:**
- `X_ref`, `X_foc` — binary response matrices for reference and focal cohorts (rows=models, cols=items)
- `n_strata=5` — number of ability strata for stratification
- `anchor_cols` — (optional) column indices of known-clean items for matching variable
- `external_scores_ref/foc` — (optional) precomputed ability scores (e.g., full-matrix totals)

**Stratification Priority (lines 51–67):**
1. **If external scores provided:** Use them directly (best matching precision)
2. **Else if anchor_cols provided:** Total score from clean items only (eliminates contamination)
3. **Else (default):** Standard purified MH — total score minus current item (rest-score approximation)

**For each item j (lines 70–166):**

1. **Compute stratum boundaries** (lines 85–90):
   - Pool ref+focal ability scores
   - Compute quantile boundaries: `np.quantile(s_all, [0, 0.2, 0.4, 0.6, 0.8, 1.0])`
   - Keep unique boundaries (removes empty strata)

2. **Assign models to strata** (lines 92–93):
   - `np.digitize()` assigns each model to stratum k ∈ {1, ..., n_bins}

3. **Stratified 2×2 contingency aggregation** (lines 101–134):
   - For each stratum k:
     - `A` = # ref correct on item j
     - `B` = # ref incorrect
     - `C` = # focal correct
     - `D` = # focal incorrect
     - `Nk` = stratum total
   - Compute Mantel-Haenszel components:
     - `Rk = A × D / Nk`
     - `Sk = B × C / Nk`
   - Aggregate: `R = Σ Rk`, `S = Σ Sk`
   - Compute variance components for chi² test

4. **MH-DIF statistics** (lines 140–165):
   - **Alpha (OR):** `α_MH = R / S` (Mantel-Haenszel odds ratio)
   - **Delta:** `δ = -2.35 × ln(α)` (log-scale DIF measure)
   - **SE:** `se = 2.35 × √v` where `v = Σ variance contributions`
   - **Chi²:** `χ² = max(|Σ(A − EA)| − 0.5, 0)² / Σvar` (continuity corrected)
   - **p-value:** `1 − CDF_χ²(χ², df=1)`

5. **ETS Classification** (lines 156–162):
   - **A** (Negligible): `|δ| < 1.0`
   - **C** (Large): `|δ| ≥ 1.5` AND `p < 0.05`
   - **B** (Moderate): Everything else

**Output:** DataFrame with columns: `col_idx, alpha_mh, delta_mh, se, chi2, p_value, ets_class`

---

#### **B. Plan 028: mh_dif_c_pct_vec() — Fully Vectorized Version (lines 34–101)**

**Signature:**
```python
mh_dif_c_pct_vec(X_ref, X_foc, n_strata=5) → float (percentage)
```

**Key Optimization:** Operates on **total-score** stratification (not rest-score), yielding ~100x speedup with <0.3pp difference.

**Algorithm (lines 34–101):**

1. **Total score stratification** (lines 39–49):
   ```python
   tot_ref = X_ref.sum(axis=1).astype(np.float64)  # (n_ref,)
   tot_foc = X_foc.sum(axis=1).astype(np.float64)  # (n_foc,)
   s_all = np.concatenate([tot_ref, tot_foc])
   edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
   n_bins = len(edges) - 1
   k_ref = np.digitize(tot_ref, edges[1:-1])  # (n_ref,) stratum labels
   k_foc = np.digitize(tot_foc, edges[1:-1])  # (n_foc,) stratum labels
   ```

2. **Stratum aggregation (vectorized)** (lines 51–70):
   ```python
   for k in range(n_bins):
       mr = (k_ref == k); mf = (k_foc == k)
       n1[k] = mr.sum()  # ref count in stratum k
       n0[k] = mf.sum()  # focal count
       A[k] = X_ref[mr].sum(axis=0)  # (J,) correct counts per item
       C[k] = X_foc[mf].sum(axis=0)  # (J,)
   B = n1[:, None] - A  # (n_bins, J)
   D = n0[:, None] - C
   Nk = (n1 + n0)[:, None]
   m1 = A + C  # total correct per stratum+item
   m0 = B + D
   ```

3. **Vectorized MH statistics** (lines 72–101):
   ```python
   # Validity mask: must have ref & focal in stratum, and both marginals non-zero
   valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &
            (Nk > 1) & (m1 > 0) & (m0 > 0))  # (n_bins, J)
   
   # MH components (summed across strata)
   Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)  # (J,)
   Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)  # (J,)
   
   # Delta (log-scale)
   finite_mask = (Rj > 0) & (Sj > 0)
   delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)  # (J,)
   
   # Chi² statistics
   EA = np.where(valid, n1[:, None] * m1 / Nk, 0)
   sum_diff = (A - EA).sum(axis=0)  # (J,) signed difference
   sum_var = (n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * (Nk - 1))).sum(axis=0)
   chi2_j = np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / sum_var
   pval_j = 1 - chi2_dist.cdf(chi2_j, df=1)
   
   # ETS C classification
   is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)
   
   # Return: % of items in C class
   return is_c.sum() / J * 100
   ```

**Speed:** O(n_bins × J) vectorized operations vs O(J × n_bins) scalar loops in rest-score version.

---

### **3. INJECTION METHODOLOGY (Plan 011, Lines 282–390)**

#### **Cohort Definition (lines 215–278):**

**Ability Cohort:**
- **Ref:** Models in accuracy quintiles 1–2 (lowest performing)
- **Focal:** Models in accuracy quintiles 4–5 (highest performing)
- **Injection subset:** Focal models within accuracy overlap with ref (lines 237–244)
  - If no overlap: use all focal models
  - If overlap exists: only models in overlap range (better matching)

**Temporal Cohort:**
- **Ref:** 2023 models
- **Focal:** 2024 models
- **Injection subset:** 2024 models within accuracy overlap of 2023 (lines 264–269)

#### **Injection Procedure (lines 307–327):**

**For each (p, seed, cohort, variant):**

1. **Select contaminated items** (lines 311–313):
   - Randomly choose `N_CONTAMINATED=100` of `N_BASELINE=500` items
   - Mark remaining `N_CLEAN=400` as anchor items (for anchor variant)

2. **Flip correct→incorrect** (lines 319–324):
   - For each contaminated item j:
     - For each focal model to inject:
       - If currently incorrect (X=0): flip to correct with probability p
   - Track number of flips

3. **Density measurement** (lines 326–327):
   - Before: `orig_density = X_base[focal, contam].mean()`
   - After: `new_density = X_inj[focal, contam].mean()`

4. **Three MH variants** (lines 332–343):
   - **standard:** Total score from all 500 baseline items (minus current for each j)
   - **anchor:** Total score from 400 clean items only
   - **external:** Total score from full 12,508-item original matrix (precomputed)

#### **Evaluation** (lines 345–370):

For each variant:
- **TPR (True Positive Rate):** Fraction of 100 injected items flagged as C class
- **FPR (False Positive Rate):** Fraction of 400 clean items flagged as C class
- **Fisher's exact test:** 2×2 table: `[[n_c_contam, n_c_clean_contam], [n_c_clean, n_c_clean_clean]]`

---

### **4. DATA STRUCTURES & OUTPUTS**

#### **Plan 011 Outputs:**

**injection_results.csv** (1,000 rows):
- Columns: `p, seed, cohort_type, mh_variant, n_baseline, n_contaminated, n_clean, n_foc_inject, tpr, fpr, fisher_or, fisher_p, n_responses_flipped, orig_density, new_density`
- Each row: one complete injection run (5 injection probabilities × 5 seeds × 2 cohorts × 3 variants)

**dose_response_summary.csv** (30 rows):
- Aggregated by `(p, cohort_type, mh_variant)`
- Columns: `tpr_mean, tpr_std, fpr_mean, fpr_std, fisher_or_mean, fisher_p_median`

**per_item_results.csv** (250,000 rows):
- One row per item per run (anchor variant only)
- Columns: `item_id, p, seed, cohort_type, mh_variant, delta_mh, p_value, ets_class, is_injected`

#### **Plan 028 Outputs:**

**mmlu_bootstrap_results.csv** (1,000 rows):
- Columns: `bootstrap_id, c_pct` (percentage of items flagged as C per bootstrap sample)

**mmlu_bootstrap_summary.csv** (1 row):
- Columns: `benchmark, original_c_pct_rest, original_c_pct_vec, ci_lower, ci_upper, boot_mean, boot_std, n_bootstrap, n_ref, n_foc, n_items, ctrl_mean, ctrl_std`

---

### **5. KEY PIPELINE CHARACTERISTICS**

| Aspect | Details |
|--------|---------|
| **Stratification** | 5 quantile-based strata on ability scores |
| **Matching Variable** | Total score (standard), clean-item total (anchor), full-matrix total (external) |
| **Continual Correction** | `max(\|Σ(A−EA)\|−0.5, 0)²` applied to χ² statistic |
| **Effect Size** | `δ = −2.35 × ln(α_MH)` in log-odds scale |
| **Classification** | A: \|δ\|<1.0; C: \|δ\|≥1.5 AND p<0.05; B: else |
| **Vectorization** | ~100x speedup via total-score pooling (validated <0.3pp) |
| **Bootstrap** | Resample models (not items), N=1,000, 95% CI via percentile |
| **Injection Signal** | Dose-response: TPR rises from baseline as injection probability increases |

---

### **6. SPECIFIC CODE LOCATIONS**

| Component | File | Lines |
|-----------|------|-------|
| MH-DIF core (scalar) | plan_011_analysis.py | 46–167 |
| Injection logic | plan_011_analysis.py | 307–327 |
| Cohort definition | plan_011_analysis.py | 215–278 |
| Vectorized C% function | mmlu_bootstrap_ci.py | 34–101 |
| Bootstrap procedure | mmlu_bootstrap_ci.py | 181–286 |
| Results aggregation | plan_011_analysis.py | 395–416 |

This pipeline validates that MH-DIF can detect **differential** contamination (contamination affecting focal cohort more) when it's injected with known magnitude, and quantifies the false positive rate when no contamination exists.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "e6c5017d-6e2e-466e-b5ba-cbcedb6d36b7",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to understand the existing MH-DIF pipeline and data structures in this project. Please find and read the following files:\n\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py` — the semi-synthetic injection + MH-DIF pipeline reference\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py` — contains `mh_dif_c_pct_vec()` function\n\nFor each file, I need:\n- The full MH-DIF calculation logic (especially the vectorized version)\n- How injection is done in plan_011\n- How cohorts are split (ref vs focal)\n- How results are reported\n\nAlso check if model_metadata.csv exists at the artifacts root and what columns it has. Search breadth: very thorough.",
    "agentId": "a5459180bf034abb6",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information needed. Let me create a comprehensive summary of the MH-DIF pipeline and data structures.\n\n## Comprehensive MH-DIF Pipeline and Data Structures Summary\n\nI've thoroughly examined both the **plan_011_analysis.py** (semi-synthetic injection validation) and **mmlu_bootstrap_ci.py** (vectorized MH-DIF with bootstrap CI) files, plus the supporting metadata. Here's what I found:\n\n---\n\n### **1. MODEL_METADATA.CSV STRUCTURE**\n\n**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv`\n\n**Dimensions:** 5,227 models × 8 columns\n\n**Columns:**\n- `model_name` — unique model identifier\n- `family` — model family/foundation (e.g., GPT, Claude, Llama)\n- `release_year` — year of release\n- `release_half` — H1 or H2\n- `training_method` — base, DPO, SFT, etc.\n- `accuracy` — continuous MMLU accuracy (0–1 range)\n- `cohort_temporal` — **2023** or **2024** (temporal cohort for DIF)\n- `cohort_accuracy_quintile` — **1–5** (ability quintile based on accuracy)\n\n---\n\n### **2. MH-DIF CORE CALCULATION LOGIC**\n\n#### **A. Plan 011: mh_dif_subset() — Standard Stratified Approach (lines 46–167)**\n\n**Signature:**\n```python\nmh_dif_subset(X_ref, X_foc, n_strata=5, anchor_cols=None,\n              external_scores_ref=None, external_scores_foc=None)\n```\n\n**Inputs:**\n- `X_ref`, `X_foc` — binary response matrices for reference and focal cohorts (rows=models, cols=items)\n- `n_strata=5` — number of ability strata for stratification\n- `anchor_cols` — (optional) column indices of known-clean items for matching variable\n- `external_scores_ref/foc` — (optional) precomputed ability scores (e.g., full-matrix totals)\n\n**Stratification Priority (lines 51–67):**\n1. **If external scores provided:** Use them directly (best matching precision)\n2. **Else if anchor_cols provided:** Total score from clean items only (eliminates contamination)\n3. **Else (default):** Standard purified MH — total score minus current item (rest-score approximation)\n\n**For each item j (lines 70–166):**\n\n1. **Compute stratum boundaries** (lines 85–90):\n   - Pool ref+focal ability scores\n   - Compute quantile boundaries: `np.quantile(s_all, [0, 0.2, 0.4, 0.6, 0.8, 1.0])`\n   - Keep unique boundaries (removes empty strata)\n\n2. **Assign models to strata** (lines 92–93):\n   - `np.digitize()` assigns each model to stratum k ∈ {1, ..., n_bins}\n\n3. **Stratified 2×2 contingency aggregation** (lines 101–134):\n   - For each stratum k:\n     - `A` = # ref correct on item j\n     - `B` = # ref incorrect\n     - `C` = # focal correct\n     - `D` = # focal incorrect\n     - `Nk` = stratum total\n   - Compute Mantel-Haenszel components:\n     - `Rk = A × D / Nk`\n     - `Sk = B × C / Nk`\n   - Aggregate: `R = Σ Rk`, `S = Σ Sk`\n   - Compute variance components for chi² test\n\n4. **MH-DIF statistics** (lines 140–165):\n   - **Alpha (OR):** `α_MH = R / S` (Mantel-Haenszel odds ratio)\n   - **Delta:** `δ = -2.35 × ln(α)` (log-scale DIF measure)\n   - **SE:** `se = 2.35 × √v` where `v = Σ variance contributions`\n   - **Chi²:** `χ² = max(|Σ(A − EA)| − 0.5, 0)² / Σvar` (continuity corrected)\n   - **p-value:** `1 − CDF_χ²(χ², df=1)`\n\n5. **ETS Classification** (lines 156–162):\n   - **A** (Negligible): `|δ| < 1.0`\n   - **C** (Large): `|δ| ≥ 1.5` AND `p < 0.05`\n   - **B** (Moderate): Everything else\n\n**Output:** DataFrame with columns: `col_idx, alpha_mh, delta_mh, se, chi2, p_value, ets_class`\n\n---\n\n#### **B. Plan 028: mh_dif_c_pct_vec() — Fully Vectorized Version (lines 34–101)**\n\n**Signature:**\n```python\nmh_dif_c_pct_vec(X_ref, X_foc, n_strata=5) → float (percentage)\n```\n\n**Key Optimization:** Operates on **total-score** stratification (not rest-score), yielding ~100x speedup with <0.3pp difference.\n\n**Algorithm (lines 34–101):**\n\n1. **Total score stratification** (lines 39–49):\n   ```python\n   tot_ref = X_ref.sum(axis=1).astype(np.float64)  # (n_ref,)\n   tot_foc = X_foc.sum(axis=1).astype(np.float64)  # (n_foc,)\n   s_all = np.concatenate([tot_ref, tot_foc])\n   edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n   n_bins = len(edges) - 1\n   k_ref = np.digitize(tot_ref, edges[1:-1])  # (n_ref,) stratum labels\n   k_foc = np.digitize(tot_foc, edges[1:-1])  # (n_foc,) stratum labels\n   ```\n\n2. **Stratum aggregation (vectorized)** (lines 51–70):\n   ```python\n   for k in range(n_bins):\n       mr = (k_ref == k); mf = (k_foc == k)\n       n1[k] = mr.sum()  # ref count in stratum k\n       n0[k] = mf.sum()  # focal count\n       A[k] = X_ref[mr].sum(axis=0)  # (J,) correct counts per item\n       C[k] = X_foc[mf].sum(axis=0)  # (J,)\n   B = n1[:, None] - A  # (n_bins, J)\n   D = n0[:, None] - C\n   Nk = (n1 + n0)[:, None]\n   m1 = A + C  # total correct per stratum+item\n   m0 = B + D\n   ```\n\n3. **Vectorized MH statistics** (lines 72–101):\n   ```python\n   # Validity mask: must have ref & focal in stratum, and both marginals non-zero\n   valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n            (Nk > 1) & (m1 > 0) & (m0 > 0))  # (n_bins, J)\n   \n   # MH components (summed across strata)\n   Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)  # (J,)\n   Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)  # (J,)\n   \n   # Delta (log-scale)\n   finite_mask = (Rj > 0) & (Sj > 0)\n   delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)  # (J,)\n   \n   # Chi² statistics\n   EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n   sum_diff = (A - EA).sum(axis=0)  # (J,) signed difference\n   sum_var = (n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * (Nk - 1))).sum(axis=0)\n   chi2_j = np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n   pval_j = 1 - chi2_dist.cdf(chi2_j, df=1)\n   \n   # ETS C classification\n   is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n   \n   # Return: % of items in C class\n   return is_c.sum() / J * 100\n   ```\n\n**Speed:** O(n_bins × J) vectorized operations vs O(J × n_bins) scalar loops in rest-score version.\n\n---\n\n### **3. INJECTION METHODOLOGY (Plan 011, Lines 282–390)**\n\n#### **Cohort Definition (lines 215–278):**\n\n**Ability Cohort:**\n- **Ref:** Models in accuracy quintiles 1–2 (lowest performing)\n- **Focal:** Models in accuracy quintiles 4–5 (highest performing)\n- **Injection subset:** Focal models within accuracy overlap with ref (lines 237–244)\n  - If no overlap: use all focal models\n  - If overlap exists: only models in overlap range (better matching)\n\n**Temporal Cohort:**\n- **Ref:** 2023 models\n- **Focal:** 2024 models\n- **Injection subset:** 2024 models within accuracy overlap of 2023 (lines 264–269)\n\n#### **Injection Procedure (lines 307–327):**\n\n**For each (p, seed, cohort, variant):**\n\n1. **Select contaminated items** (lines 311–313):\n   - Randomly choose `N_CONTAMINATED=100` of `N_BASELINE=500` items\n   - Mark remaining `N_CLEAN=400` as anchor items (for anchor variant)\n\n2. **Flip correct→incorrect** (lines 319–324):\n   - For each contaminated item j:\n     - For each focal model to inject:\n       - If currently incorrect (X=0): flip to correct with probability p\n   - Track number of flips\n\n3. **Density measurement** (lines 326–327):\n   - Before: `orig_density = X_base[focal, contam].mean()`\n   - After: `new_density = X_inj[focal, contam].mean()`\n\n4. **Three MH variants** (lines 332–343):\n   - **standard:** Total score from all 500 baseline items (minus current for each j)\n   - **anchor:** Total score from 400 clean items only\n   - **external:** Total score from full 12,508-item original matrix (precomputed)\n\n#### **Evaluation** (lines 345–370):\n\nFor each variant:\n- **TPR (True Positive Rate):** Fraction of 100 injected items flagged as C class\n- **FPR (False Positive Rate):** Fraction of 400 clean items flagged as C class\n- **Fisher's exact test:** 2×2 table: `[[n_c_contam, n_c_clean_contam], [n_c_clean, n_c_clean_clean]]`\n\n---\n\n### **4. DATA STRUCTURES & OUTPUTS**\n\n#### **Plan 011 Outputs:**\n\n**injection_results.csv** (1,000 rows):\n- Columns: `p, seed, cohort_type, mh_variant, n_baseline, n_contaminated, n_clean, n_foc_inject, tpr, fpr, fisher_or, fisher_p, n_responses_flipped, orig_density, new_density`\n- Each row: one complete injection run (5 injection probabilities × 5 seeds × 2 cohorts × 3 variants)\n\n**dose_response_summary.csv** (30 rows):\n- Aggregated by `(p, cohort_type, mh_variant)`\n- Columns: `tpr_mean, tpr_std, fpr_mean, fpr_std, fisher_or_mean, fisher_p_median`\n\n**per_item_results.csv** (250,000 rows):\n- One row per item per run (anchor variant only)\n- Columns: `item_id, p, seed, cohort_type, mh_variant, delta_mh, p_value, ets_class, is_injected`\n\n#### **Plan 028 Outputs:**\n\n**mmlu_bootstrap_results.csv** (1,000 rows):\n- Columns: `bootstrap_id, c_pct` (percentage of items flagged as C per bootstrap sample)\n\n**mmlu_bootstrap_summary.csv** (1 row):\n- Columns: `benchmark, original_c_pct_rest, original_c_pct_vec, ci_lower, ci_upper, boot_mean, boot_std, n_bootstrap, n_ref, n_foc, n_items, ctrl_mean, ctrl_std`\n\n---\n\n### **5. KEY PIPELINE CHARACTERISTICS**\n\n| Aspect | Details |\n|--------|---------|\n| **Stratification** | 5 quantile-based strata on ability scores |\n| **Matching Variable** | Total score (standard), clean-item total (anchor), full-matrix total (external) |\n| **Continual Correction** | `max(\\|Σ(A−EA)\\|−0.5, 0)²` applied to χ² statistic |\n| **Effect Size** | `δ = −2.35 × ln(α_MH)` in log-odds scale |\n| **Classification** | A: \\|δ\\|<1.0; C: \\|δ\\|≥1.5 AND p<0.05; B: else |\n| **Vectorization** | ~100x speedup via total-score pooling (validated <0.3pp) |\n| **Bootstrap** | Resample models (not items), N=1,000, 95% CI via percentile |\n| **Injection Signal** | Dose-response: TPR rises from baseline as injection probability increases |\n\n---\n\n### **6. SPECIFIC CODE LOCATIONS**\n\n| Component | File | Lines |\n|-----------|------|-------|\n| MH-DIF core (scalar) | plan_011_analysis.py | 46–167 |\n| Injection logic | plan_011_analysis.py | 307–327 |\n| Cohort definition | plan_011_analysis.py | 215–278 |\n| Vectorized C% function | mmlu_bootstrap_ci.py | 34–101 |\n| Bootstrap procedure | mmlu_bootstrap_ci.py | 181–286 |\n| Results aggregation | plan_011_analysis.py | 395–416 |\n\nThis pipeline validates that MH-DIF can detect **differential** contamination (contamination affecting focal cohort more) when it's injected with known magnitude, and quantifies the false positive rate when no contamination exists."
      }
    ],
    "totalDurationMs": 43765,
    "totalTokens": 40918,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2672,
      "cache_read_input_tokens": 34342,
      "output_tokens": 3897,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2672
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3897,
          "cache_read_input_tokens": 34342,
          "cache_creation_input_tokens": 2672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2672,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 6,
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

_source line 38_

Now let me read the key reference files directly to get the exact code for the vectorized MH-DIF function and injection logic.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "6b457514-826f-4035-a00a-db5ddec80da3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EajrWmYXb5ob6ME3L4X2QM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4346,
      "cache_read_input_tokens": 25389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4346
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

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01CDGuksKkew9cFqUiKdf6Vk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py",
  "offset": 33,
  "limit": 70
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "58eb7d9d-86d4-4993-b18d-f18c4d48d3ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EajrWmYXb5ob6ME3L4X2QM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4346,
      "cache_read_input_tokens": 25389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4346
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

_source line 40 · 2026-05-22T18:49:26.293Z_

<details><summary>↩ Tool result · `toolu_01CDGuksKkew9cFqUiKdf6Vk`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "47ea6b20-8386-43ad-b67b-2fbb388081b9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py",
      "content": "# ════════════════════════════════════════════════════════════════════════\ndef mh_dif_c_pct_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Fully vectorized MH-DIF → C%. Stratifies on total score (not rest).\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return 0.0\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n    return is_c.sum() / J * 100\n",
      "numLines": 70,
      "startLine": 33,
      "totalLines": 364
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01LUoAKzHpx34dTiy3iRQtim`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py",
  "offset": 282,
  "limit": 90
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "bf4d66f1-39e9-470b-a583-b767c6088f6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EajrWmYXb5ob6ME3L4X2QM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4346,
      "cache_read_input_tokens": 25389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4346
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

_source line 42 · 2026-05-22T18:49:26.994Z_

<details><summary>↩ Tool result · `toolu_01LUoAKzHpx34dTiy3iRQtim`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "cfb5c2a2-9471-42ed-9a7b-e4c7788b72f9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py",
      "content": "#  STEP 3-4: INJECTION + MH-DIF\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Step 3-4: Injection + MH-DIF ===\")\n\nX_base = mat[:, baseline_col_indices].toarray().astype(np.int8)\nprint(f\"  Baseline submatrix: {X_base.shape}, density: {X_base.mean():.4f}\")\n\ninjection_rows = []\nper_item_rows = []\n\nMH_VARIANTS = [\"standard\", \"anchor\", \"external\"]\n\ntotal_runs = len(INJECTION_PS) * N_SEEDS * len(cohort_defs) * len(MH_VARIANTS)\nrun_count = 0\nt_start = time.time()\n\nfor cohort_name, cdef in cohort_defs.items():\n    ref_idx = cdef[\"ref_idx\"]\n    foc_idx = cdef[\"foc_idx\"]\n    foc_inject_idx = cdef[\"foc_inject_idx\"]\n\n    # External scores for this cohort (from full original matrix)\n    ext_ref = full_totals[ref_idx]\n    ext_foc = full_totals[foc_idx]\n\n    for p in INJECTION_PS:\n        for seed in range(1, N_SEEDS + 1):\n            rng = np.random.RandomState(seed)\n\n            contam_local_idx = rng.choice(N_BASELINE, N_CONTAMINATED, replace=False)\n            contam_set = set(contam_local_idx.tolist())\n            clean_local_idx = np.array([i for i in range(N_BASELINE) if i not in contam_set])\n\n            X_inj = X_base.copy()\n            n_flipped = 0\n\n            if p > 0:\n                for local_j in contam_local_idx:\n                    for model_row in foc_inject_idx:\n                        if X_inj[model_row, local_j] == 0:\n                            if rng.random() < p:\n                                X_inj[model_row, local_j] = 1\n                                n_flipped += 1\n\n            orig_density = X_base[np.ix_(foc_inject_idx, contam_local_idx)].mean()\n            new_density = X_inj[np.ix_(foc_inject_idx, contam_local_idx)].mean()\n\n            X_ref = X_inj[ref_idx]\n            X_foc = X_inj[foc_idx]\n\n            for variant in MH_VARIANTS:\n                run_count += 1\n\n                if variant == \"anchor\":\n                    dif_results = mh_dif_subset(X_ref, X_foc, n_strata=5,\n                                                anchor_cols=clean_local_idx)\n                elif variant == \"external\":\n                    dif_results = mh_dif_subset(X_ref, X_foc, n_strata=5,\n                                                external_scores_ref=ext_ref,\n                                                external_scores_foc=ext_foc)\n                else:\n                    dif_results = mh_dif_subset(X_ref, X_foc, n_strata=5)\n\n                contam_mask = dif_results[\"col_idx\"].isin(contam_set)\n                clean_mask = ~contam_mask\n\n                contam_results = dif_results[contam_mask]\n                clean_results = dif_results[clean_mask]\n\n                n_c_contam = (contam_results[\"ets_class\"] == \"C\").sum()\n                n_c_clean = (clean_results[\"ets_class\"] == \"C\").sum()\n                tpr = n_c_contam / N_CONTAMINATED\n                fpr = n_c_clean / (N_BASELINE - N_CONTAMINATED)\n\n                table = [[n_c_contam, N_CONTAMINATED - n_c_contam],\n                         [n_c_clean, (N_BASELINE - N_CONTAMINATED) - n_c_clean]]\n                fisher_or, fisher_p = fisher_exact(table)\n\n                injection_rows.append(dict(\n                    p=p, seed=seed, cohort_type=cohort_name,\n                    mh_variant=variant,\n                    n_baseline=N_BASELINE, n_contaminated=N_CONTAMINATED,\n                    n_clean=N_BASELINE - N_CONTAMINATED,\n                    n_foc_inject=len(foc_inject_idx),\n                    tpr=tpr, fpr=fpr,\n                    fisher_or=fisher_or, fisher_p=fisher_p,\n                    n_responses_flipped=n_flipped,\n                    orig_density=orig_density, new_density=new_density,\n                ))\n",
      "numLines": 90,
      "startLine": 282,
      "totalLines": 602
    }
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the reference code. Let me also check the model metadata to understand the cohort structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "93831a1f-5918-4f02-9407-f7c936bc8bdd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018UhYgQ4La3pzPNPsnBRnaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2989,
      "cache_read_input_tokens": 29735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2989
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

_source line 44_

Let me check the model metadata and verify the data dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "c098d511-4149-4d2c-b2f9-615a84ec2796",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018UhYgQ4La3pzPNPsnBRnaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2989,
      "cache_read_input_tokens": 29735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2989
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

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_014bChbZQfbJis7YyPVE4X8J`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts && python3 -c \"\nimport numpy as np, pandas as pd\nfrom scipy import sparse\n\n# Load response matrix\nrm = np.load('response_matrix.npz')\nX = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nidx = np.load('response_matrix_index.npz', allow_pickle=True)\nmodel_names = idx['model_names']\nitem_ids = idx['item_ids']\nprint(f'Response matrix: {X.shape}')\nprint(f'Models: {len(model_names)}, Items: {len(item_ids)}')\n\n# Load metadata\nmeta = pd.read_csv('model_metadata.csv')\nprint(f'\\nMetadata shape: {meta.shape}')\nprint(f'Columns: {list(meta.columns)}')\nprint(f'\\ncohort_temporal distribution:')\nprint(meta['cohort_temporal'].value_counts())\n\n# Check model name overlap\nmeta_names = set(meta['model_name'].values)\nrm_names = set(model_names)\noverlap = meta_names & rm_names\nprint(f'\\nOverlap: {len(overlap)} of {len(rm_names)} RM models found in metadata')\n\n# Cohort sizes\nref_mask = meta['cohort_temporal'] == 2023\nfoc_mask = meta['cohort_temporal'] == 2024\nprint(f'Ref (2023): {ref_mask.sum()}, Foc (2024): {foc_mask.sum()}')\n\"\n",
  "description": "Check data dimensions and cohort structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "d95afa68-0a22-43d2-b86e-0b31f745de80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018UhYgQ4La3pzPNPsnBRnaf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2989,
      "cache_read_input_tokens": 29735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2989
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

_source line 46 · 2026-05-22T18:49:41.876Z_

<details><summary>↩ Tool result · `toolu_014bChbZQfbJis7YyPVE4X8J`</summary>

```text
Response matrix: (5227, 12508)
Models: 5227, Items: 12508

Metadata shape: (5227, 8)
Columns: ['model_name', 'family', 'release_year', 'release_half', 'training_method', 'accuracy', 'cohort_temporal', 'cohort_accuracy_quintile']

cohort_temporal distribution:
cohort_temporal
other    3340
2023     1080
2024      807
Name: count, dtype: int64

Overlap: 5227 of 5227 RM models found in metadata
Ref (2023): 0, Foc (2024): 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "11afec45-401b-4f0f-8be9-227ef1875c90",
  "tool_use_result": {
    "stdout": "Response matrix: (5227, 12508)\nModels: 5227, Items: 12508\n\nMetadata shape: (5227, 8)\nColumns: ['model_name', 'family', 'release_year', 'release_half', 'training_method', 'accuracy', 'cohort_temporal', 'cohort_accuracy_quintile']\n\ncohort_temporal distribution:\ncohort_temporal\nother    3340\n2023     1080\n2024      807\nName: count, dtype: int64\n\nOverlap: 5227 of 5227 RM models found in metadata\nRef (2023): 0, Foc (2024): 0",
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

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_01KWnrJ7YXNbigb2eGqDbAEY`</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd, numpy as np\n\nmeta = pd.read_csv('model_metadata.csv')\nidx = np.load('response_matrix_index.npz', allow_pickle=True)\nmodel_names = list(idx['model_names'])\n\n# Check cohort values\nprint('cohort_temporal unique:', meta['cohort_temporal'].unique())\nprint()\n\n# Check via the cleaned analysis file\ncleaned = pd.read_csv('plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv')\nprint('Cleaned cols:', list(cleaned.columns)[:10])\nprint('Cleaned shape:', cleaned.shape)\nif 'cohort_temporal' in cleaned.columns:\n    print('Cleaned cohort dist:')\n    print(cleaned['cohort_temporal'].value_counts())\n\n# Get model->cohort mapping from cleaned\nmodel_cohort = cleaned[['model_name','cohort_temporal']].drop_duplicates()\nprint(f'\\nUnique models in cleaned: {len(model_cohort)}')\nprint(model_cohort['cohort_temporal'].value_counts())\n\"\n",
  "description": "Check cohort mapping from cleaned analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "59c086d5-7714-4a11-be06-80751855825c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017sB5woXc2XYevzuMJiLpZY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 32724,
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

_source line 48 · 2026-05-22T18:49:49.979Z_

<details><summary>↩ Tool result · `toolu_01KWnrJ7YXNbigb2eGqDbAEY`</summary>

```text
cohort_temporal unique: &lt;ArrowStringArray>
['other', '2024', '2023']
Length: 3, dtype: str

Cleaned cols: ['model_name', 'score_full', 'score_cleaned', 'rank_full', 'rank_cleaned', 'rank_change', 'abs_rank_change', 'family', 'cohort_temporal']
Cleaned shape: (5227, 9)
Cleaned cohort dist:
cohort_temporal
other    3340
2023     1080
2024      807
Name: count, dtype: int64

Unique models in cleaned: 5227
cohort_temporal
other    3340
2023     1080
2024      807
Name: count, dtype: int64
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "8166fc5a-cea0-4a1c-b1c7-cd72175e97a8",
  "tool_use_result": {
    "stdout": "cohort_temporal unique: &lt;ArrowStringArray>\n['other', '2024', '2023']\nLength: 3, dtype: str\n\nCleaned cols: ['model_name', 'score_full', 'score_cleaned', 'rank_full', 'rank_cleaned', 'rank_change', 'abs_rank_change', 'family', 'cohort_temporal']\nCleaned shape: (5227, 9)\nCleaned cohort dist:\ncohort_temporal\nother    3340\n2023     1080\n2024      807\nName: count, dtype: int64\n\nUnique models in cleaned: 5227\ncohort_temporal\nother    3340\n2023     1080\n2024      807\nName: count, dtype: int64",
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

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_013rv4JY33MmMRQT1wYAWqgp`</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd, numpy as np\n\nmeta = pd.read_csv('model_metadata.csv')\nidx = np.load('response_matrix_index.npz', allow_pickle=True)\nmodel_names = list(idx['model_names'])\n\n# The cohort_temporal in metadata is string, not int\n# Build index mapping\nname_to_row = {n: i for i, n in enumerate(model_names)}\n\nref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values\nfoc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values\n\nref_idx = np.array([name_to_row[n] for n in ref_models if n in name_to_row])\nfoc_idx = np.array([name_to_row[n] for n in foc_models if n in name_to_row])\n\nprint(f'Ref indices: {len(ref_idx)}, Foc indices: {len(foc_idx)}')\nprint(f'Total items: {len(idx[\\\"item_ids\\\"])}')\nprint(f'30% of foc: {int(len(foc_idx) * 0.3)}')\nprint(f'24% of items: {int(len(idx[\\\"item_ids\\\"]) * 0.24)}')\n\"\n",
  "description": "Verify cohort index construction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "43e3e611-66d0-4f10-b889-9730aee4cd19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7ZBDq1ZXwxcRNsV5WeXcE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 33442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 539
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

_source line 50 · 2026-05-22T18:50:07.227Z_

<details><summary>↩ Tool result · `toolu_013rv4JY33MmMRQT1wYAWqgp`</summary>

```text
Ref indices: 1080, Foc indices: 807
Total items: 12508
30% of foc: 242
24% of items: 3001
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "7dba1a59-4546-46b1-91a4-15f7a5ab9e8c",
  "tool_use_result": {
    "stdout": "Ref indices: 1080, Foc indices: 807\nTotal items: 12508\n30% of foc: 242\n24% of items: 3001",
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

_source line 51_

Now I have all the information needed. Let me create the output directory and write the script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "0ac190b8-2079-4434-9989-13b94033f0ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EALFqLC4E1zA5hG78VHWN4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 459,
      "cache_read_input_tokens": 33981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 459
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

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01RFoPaqbowS9HeWCJTLtN9Q`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient",
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
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "08d4242b-b0bc-45ae-b73d-9c700eb18342",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EALFqLC4E1zA5hG78VHWN4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 459,
      "cache_read_input_tokens": 33981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 459
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

_source line 53 · 2026-05-22T18:50:11.693Z_

<details><summary>↩ Tool result · `toolu_01RFoPaqbowS9HeWCJTLtN9Q`</summary>

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
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "516c4276-c7d2-4ea8-8030-7ec1eb822127",
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

_source line 54_

<details open><summary>🔧 Tool call — Write · `toolu_01FrhPZSnWejAW5Qp9tuCfmr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "content": "\"\"\"\nR19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\nTests whether MH-DIF can distinguish capability-like vs contamination-like DIF patterns.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom scipy.stats import chi2 as chi2_dist\nimport time, os, sys\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = os.path.join(ROOT, \"r19_semisynthetic_gradient\")\n\nN_SEEDS = 5\nN_STRATA = 5\nFOC_INJECT_FRAC = 0.30\nITEM_INJECT_FRAC = 0.24\n\n# ════════════════════════════════════════════════════════════════════════════\n#  VECTORIZED MH-DIF — returns per-item results\n# ════════════════════════════════════════════════════════════════════════════\ndef mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item delta_mh, p_value, is_c, direction.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C_mat = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C_mat[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C_mat\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C_mat\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C_mat / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n\n    return delta_j, pval_j, is_c\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  LOAD DATA\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"Loading data...\")\nrm = np.load(f\"{ROOT}/response_matrix.npz\")\nX_sparse = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nidx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\nmodel_names = idx['model_names']\nitem_ids = idx['item_ids']\n\nmeta = pd.read_csv(f\"{ROOT}/model_metadata.csv\")\nname_to_row = {n: i for i, n in enumerate(model_names)}\n\nref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values\nfoc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values\n\nref_idx = np.array([name_to_row[n] for n in ref_models if n in name_to_row])\nfoc_idx = np.array([name_to_row[n] for n in foc_models if n in name_to_row])\n\nN_ref, N_foc, J = len(ref_idx), len(foc_idx), len(item_ids)\nN_inject_models = int(N_foc * FOC_INJECT_FRAC)\nN_inject_items = int(J * ITEM_INJECT_FRAC)\n\nprint(f\"  Ref: {N_ref}, Foc: {N_foc}, Items: {J}\")\nprint(f\"  Injection targets: {N_inject_models} models, {N_inject_items} items\")\n\n# Densify the ref/foc submatrices\nX_ref_base = X_sparse[ref_idx].toarray().astype(np.float64)\nX_foc_base = X_sparse[foc_idx].toarray().astype(np.float64)\n\n# Ref cohort accuracy per item (= item difficulty proxy)\nitem_difficulty = X_ref_base.mean(axis=0)  # shape (J,)\n\nprint(f\"  Item difficulty: mean={item_difficulty.mean():.3f}, \"\n      f\"min={item_difficulty.min():.3f}, max={item_difficulty.max():.3f}\")\n\n# Get MMLU subjects per item for Scheme B\nitem_subjects = np.array([iid.rsplit('_', 1)[0] if '_' in iid else iid\n                           for iid in item_ids])\nunique_subjects = np.unique(item_subjects)\nprint(f\"  Unique subjects: {len(unique_subjects)}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  INJECTION SCHEMES\n# ════════════════════════════════════════════════════════════════════════════\ndef inject_scheme_a(X_foc, inject_model_mask, inject_item_idx, item_diff, rng):\n    \"\"\"Capability-like: injection probability ∝ difficulty (easy items more likely flipped).\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):\n    \"\"\"Contamination-like: uniform injection probability, restricted to 5 random subjects.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,\n                    item_diff, rng, p_const=0.5):\n    \"\"\"Mixed: half items use scheme A, half use scheme B.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    # Scheme A half\n    for j in inject_item_idx_a:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    # Scheme B half\n    for j in inject_item_idx_b:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running experiments ===\")\nresults = []\nt0 = time.time()\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection models and items (shared across schemes within seed)\n    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)\n    inject_model_mask = np.zeros(N_foc, dtype=bool)\n    inject_model_mask[inject_model_idx] = True\n\n    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)\n\n    # Scheme B: select 5 random subjects, pick injection items from those subjects\n    selected_subjects = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask = np.isin(item_subjects, selected_subjects)\n    subject_item_pool = np.where(subject_mask)[0]\n    n_b_items = min(N_inject_items, len(subject_item_pool))\n    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)\n\n    # Scheme C: split A items in half\n    half = N_inject_items // 2\n    inject_item_idx_c_a = inject_item_idx_all[:half]\n    # For scheme C's B half, pick from 5 random subjects\n    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask_c = np.isin(item_subjects, selected_subjects_c)\n    subject_pool_c = np.where(subject_mask_c)[0]\n    # Exclude items already used by A half\n    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)\n    n_c_b = min(half, len(subject_pool_c))\n    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)\n\n    schemes = {\n        'A_capability': lambda: inject_scheme_a(\n            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),\n        'B_contamination': lambda: inject_scheme_b(\n            X_foc_base, inject_model_mask, inject_item_idx_b, rng),\n        'C_mixed': lambda: inject_scheme_c(\n            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,\n            item_difficulty, rng),\n    }\n\n    for scheme_name, inject_fn in schemes.items():\n        t1 = time.time()\n        rng_state = rng.get_state()\n\n        X_foc_inj, n_flipped = inject_fn()\n\n        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # C% among all items\n        c_pct_all = is_c.sum() / J * 100\n\n        # C% among injected items only\n        inj_arr = np.array(sorted(injected_items))\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n\n        # ρ(difficulty, Δ_MH) among DIF-C items\n        c_idx = np.where(is_c)[0]\n        if len(c_idx) >= 3:\n            rho, rho_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n        else:\n            rho, rho_p = np.nan, np.nan\n\n        # Direction distribution among DIF-C items\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j < 0)).sum()   # negative delta = focal advantage\n        n_ref_favoring = (is_c & (delta_j > 0)).sum()\n        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # For scheme C: per-quintile analysis\n        quintile_data = {}\n        if scheme_name == 'C_mixed':\n            quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n            quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n\n            for q in range(5):\n                q_mask = (quintile_labels == q)\n                q_items = np.where(q_mask)[0]\n                q_c = is_c[q_items].sum()\n                q_total = len(q_items)\n                q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n                q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()\n                q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n                quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n                quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n                quintile_data[f'q{q+1}_n_c'] = q_c\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            n_c_total=n_c_total,\n            rho_diff_delta=rho,\n            rho_p_value=rho_p,\n            pct_focal_favoring=pct_focal_favoring,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ={rho:.3f}, focal%={pct_focal_favoring:.1f}%, \"\n              f\"flips={n_flipped}, {elapsed:.1f}s\")\n\ntotal_time = time.time() - t0\nprint(f\"\\nTotal time: {total_time:.0f}s\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  SAVE RESULTS\n# ════════════════════════════════════════════════════════════════════════════\ndf = pd.DataFrame(results)\ndf.to_csv(os.path.join(OUT, \"semisynthetic_results.csv\"), index=False)\nprint(f\"\\nSaved: semisynthetic_results.csv ({len(df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  GENERATE REPORT\n# ════════════════════════════════════════════════════════════════════════════\nreport_lines = [\"# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\\n\"]\nreport_lines.append(f\"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\\n\")\nreport_lines.append(f\"**Config**: {N_SEEDS} seeds, {N_ref} ref models (2023), \"\n                    f\"{N_foc} foc models (2024), {J} items\\n\")\nreport_lines.append(f\"**Injection**: {N_inject_models} foc models ({FOC_INJECT_FRAC*100:.0f}%), \"\n                    f\"~{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\\n\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| ρ(difficulty, Δ_MH) among C | {sub['rho_diff_delta'].mean():.3f} ± {sub['rho_diff_delta'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    if scheme == 'C_mixed':\n        report_lines.append(f\"\\n### Quintile Breakdown (Scheme C)\\n\")\n        report_lines.append(f\"| Quintile | C% | % Focal-Favoring | N DIF-C |\")\n        report_lines.append(f\"|----------|-----|-------------------|---------|\")\n        for q in range(1, 6):\n            col_c = f'q{q}_c_pct'\n            col_f = f'q{q}_pct_focal'\n            col_n = f'q{q}_n_c'\n            if col_c in sub.columns:\n                report_lines.append(\n                    f\"| Q{q} | {sub[col_c].mean():.2f} ± {sub[col_c].std():.2f} | \"\n                    f\"{sub[col_f].mean():.1f} ± {sub[col_f].std():.1f} | \"\n                    f\"{sub[col_n].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **Scheme A** (capability-like): Expects ρ ≈ −0.5 to −0.6 \"\n                    \"(focal-favoring DIF concentrated on easy items)\")\nreport_lines.append(\"- **Scheme B** (contamination-like): Expects ρ ≈ 0 \"\n                    \"(focal-favoring DIF uniform across difficulty)\")\nreport_lines.append(\"- **Scheme C** (mixed): Tests item-level discrimination between the two sources\")\n\nreport_text = \"\\n\".join(report_lines) + \"\\n\"\n\nwith open(os.path.join(OUT, \"semisynthetic_gradient_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"Saved: semisynthetic_gradient_report.md\")\nprint(\"\\n\" + report_text)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "796e5b91-7367-44f3-b83e-2cae35c5ea7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDV2XK8mA4YPtbk6idA6h1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 259,
      "cache_read_input_tokens": 34440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 259
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

_source line 55 · 2026-05-22T18:51:40.545Z_

<details><summary>↩ Tool result · `toolu_01FrhPZSnWejAW5Qp9tuCfmr`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "519e74bf-4cf1-4201-9712-790e78c3f30c",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
    "content": "\"\"\"\nR19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\nTests whether MH-DIF can distinguish capability-like vs contamination-like DIF patterns.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom scipy.stats import chi2 as chi2_dist\nimport time, os, sys\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = os.path.join(ROOT, \"r19_semisynthetic_gradient\")\n\nN_SEEDS = 5\nN_STRATA = 5\nFOC_INJECT_FRAC = 0.30\nITEM_INJECT_FRAC = 0.24\n\n# ════════════════════════════════════════════════════════════════════════════\n#  VECTORIZED MH-DIF — returns per-item results\n# ════════════════════════════════════════════════════════════════════════════\ndef mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item delta_mh, p_value, is_c, direction.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C_mat = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C_mat[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C_mat\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C_mat\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C_mat / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n\n    return delta_j, pval_j, is_c\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  LOAD DATA\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"Loading data...\")\nrm = np.load(f\"{ROOT}/response_matrix.npz\")\nX_sparse = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nidx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\nmodel_names = idx['model_names']\nitem_ids = idx['item_ids']\n\nmeta = pd.read_csv(f\"{ROOT}/model_metadata.csv\")\nname_to_row = {n: i for i, n in enumerate(model_names)}\n\nref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values\nfoc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values\n\nref_idx = np.array([name_to_row[n] for n in ref_models if n in name_to_row])\nfoc_idx = np.array([name_to_row[n] for n in foc_models if n in name_to_row])\n\nN_ref, N_foc, J = len(ref_idx), len(foc_idx), len(item_ids)\nN_inject_models = int(N_foc * FOC_INJECT_FRAC)\nN_inject_items = int(J * ITEM_INJECT_FRAC)\n\nprint(f\"  Ref: {N_ref}, Foc: {N_foc}, Items: {J}\")\nprint(f\"  Injection targets: {N_inject_models} models, {N_inject_items} items\")\n\n# Densify the ref/foc submatrices\nX_ref_base = X_sparse[ref_idx].toarray().astype(np.float64)\nX_foc_base = X_sparse[foc_idx].toarray().astype(np.float64)\n\n# Ref cohort accuracy per item (= item difficulty proxy)\nitem_difficulty = X_ref_base.mean(axis=0)  # shape (J,)\n\nprint(f\"  Item difficulty: mean={item_difficulty.mean():.3f}, \"\n      f\"min={item_difficulty.min():.3f}, max={item_difficulty.max():.3f}\")\n\n# Get MMLU subjects per item for Scheme B\nitem_subjects = np.array([iid.rsplit('_', 1)[0] if '_' in iid else iid\n                           for iid in item_ids])\nunique_subjects = np.unique(item_subjects)\nprint(f\"  Unique subjects: {len(unique_subjects)}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  INJECTION SCHEMES\n# ════════════════════════════════════════════════════════════════════════════\ndef inject_scheme_a(X_foc, inject_model_mask, inject_item_idx, item_diff, rng):\n    \"\"\"Capability-like: injection probability ∝ difficulty (easy items more likely flipped).\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):\n    \"\"\"Contamination-like: uniform injection probability, restricted to 5 random subjects.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,\n                    item_diff, rng, p_const=0.5):\n    \"\"\"Mixed: half items use scheme A, half use scheme B.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    # Scheme A half\n    for j in inject_item_idx_a:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    # Scheme B half\n    for j in inject_item_idx_b:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running experiments ===\")\nresults = []\nt0 = time.time()\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection models and items (shared across schemes within seed)\n    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)\n    inject_model_mask = np.zeros(N_foc, dtype=bool)\n    inject_model_mask[inject_model_idx] = True\n\n    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)\n\n    # Scheme B: select 5 random subjects, pick injection items from those subjects\n    selected_subjects = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask = np.isin(item_subjects, selected_subjects)\n    subject_item_pool = np.where(subject_mask)[0]\n    n_b_items = min(N_inject_items, len(subject_item_pool))\n    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)\n\n    # Scheme C: split A items in half\n    half = N_inject_items // 2\n    inject_item_idx_c_a = inject_item_idx_all[:half]\n    # For scheme C's B half, pick from 5 random subjects\n    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask_c = np.isin(item_subjects, selected_subjects_c)\n    subject_pool_c = np.where(subject_mask_c)[0]\n    # Exclude items already used by A half\n    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)\n    n_c_b = min(half, len(subject_pool_c))\n    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)\n\n    schemes = {\n        'A_capability': lambda: inject_scheme_a(\n            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),\n        'B_contamination': lambda: inject_scheme_b(\n            X_foc_base, inject_model_mask, inject_item_idx_b, rng),\n        'C_mixed': lambda: inject_scheme_c(\n            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,\n            item_difficulty, rng),\n    }\n\n    for scheme_name, inject_fn in schemes.items():\n        t1 = time.time()\n        rng_state = rng.get_state()\n\n        X_foc_inj, n_flipped = inject_fn()\n\n        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # C% among all items\n        c_pct_all = is_c.sum() / J * 100\n\n        # C% among injected items only\n        inj_arr = np.array(sorted(injected_items))\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n\n        # ρ(difficulty, Δ_MH) among DIF-C items\n        c_idx = np.where(is_c)[0]\n        if len(c_idx) >= 3:\n            rho, rho_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n        else:\n            rho, rho_p = np.nan, np.nan\n\n        # Direction distribution among DIF-C items\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j < 0)).sum()   # negative delta = focal advantage\n        n_ref_favoring = (is_c & (delta_j > 0)).sum()\n        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # For scheme C: per-quintile analysis\n        quintile_data = {}\n        if scheme_name == 'C_mixed':\n            quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n            quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n\n            for q in range(5):\n                q_mask = (quintile_labels == q)\n                q_items = np.where(q_mask)[0]\n                q_c = is_c[q_items].sum()\n                q_total = len(q_items)\n                q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n                q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()\n                q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n                quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n                quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n                quintile_data[f'q{q+1}_n_c'] = q_c\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            n_c_total=n_c_total,\n            rho_diff_delta=rho,\n            rho_p_value=rho_p,\n            pct_focal_favoring=pct_focal_favoring,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ={rho:.3f}, focal%={pct_focal_favoring:.1f}%, \"\n              f\"flips={n_flipped}, {elapsed:.1f}s\")\n\ntotal_time = time.time() - t0\nprint(f\"\\nTotal time: {total_time:.0f}s\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  SAVE RESULTS\n# ════════════════════════════════════════════════════════════════════════════\ndf = pd.DataFrame(results)\ndf.to_csv(os.path.join(OUT, \"semisynthetic_results.csv\"), index=False)\nprint(f\"\\nSaved: semisynthetic_results.csv ({len(df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  GENERATE REPORT\n# ════════════════════════════════════════════════════════════════════════════\nreport_lines = [\"# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\\n\"]\nreport_lines.append(f\"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\\n\")\nreport_lines.append(f\"**Config**: {N_SEEDS} seeds, {N_ref} ref models (2023), \"\n                    f\"{N_foc} foc models (2024), {J} items\\n\")\nreport_lines.append(f\"**Injection**: {N_inject_models} foc models ({FOC_INJECT_FRAC*100:.0f}%), \"\n                    f\"~{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\\n\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| ρ(difficulty, Δ_MH) among C | {sub['rho_diff_delta'].mean():.3f} ± {sub['rho_diff_delta'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    if scheme == 'C_mixed':\n        report_lines.append(f\"\\n### Quintile Breakdown (Scheme C)\\n\")\n        report_lines.append(f\"| Quintile | C% | % Focal-Favoring | N DIF-C |\")\n        report_lines.append(f\"|----------|-----|-------------------|---------|\")\n        for q in range(1, 6):\n            col_c = f'q{q}_c_pct'\n            col_f = f'q{q}_pct_focal'\n            col_n = f'q{q}_n_c'\n            if col_c in sub.columns:\n                report_lines.append(\n                    f\"| Q{q} | {sub[col_c].mean():.2f} ± {sub[col_c].std():.2f} | \"\n                    f\"{sub[col_f].mean():.1f} ± {sub[col_f].std():.1f} | \"\n                    f\"{sub[col_n].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **Scheme A** (capability-like): Expects ρ ≈ −0.5 to −0.6 \"\n                    \"(focal-favoring DIF concentrated on easy items)\")\nreport_lines.append(\"- **Scheme B** (contamination-like): Expects ρ ≈ 0 \"\n                    \"(focal-favoring DIF uniform across difficulty)\")\nreport_lines.append(\"- **Scheme C** (mixed): Tests item-level discrimination between the two sources\")\n\nreport_text = \"\\n\".join(report_lines) + \"\\n\"\n\nwith open(os.path.join(OUT, \"semisynthetic_gradient_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"Saved: semisynthetic_gradient_report.md\")\nprint(\"\\n\" + report_text)\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Bash · `toolu_01UXVyFLa4NXzfxyb717Rw9w`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen && python3 artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "description": "Run semi-synthetic injection experiment",
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
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "5d6881ce-f8d5-4a8c-91d6-5bb6c2400f1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XcxVpTyu4zciQ3gogM4pRR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6200,
      "cache_read_input_tokens": 34699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6200
      },
      "output_tokens": 62,
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

_source line 57_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b4h20d37w",
  "tool_use_id": "toolu_01UXVyFLa4NXzfxyb717Rw9w",
  "description": "Run semi-synthetic injection experiment",
  "task_type": "local_bash",
  "uuid": "3a226223-23c1-4ff9-b070-424f2452376d",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b4h20d37w",
  "tool_use_id": "toolu_01UXVyFLa4NXzfxyb717Rw9w",
  "status": "completed",
  "output_file": "",
  "summary": "Run semi-synthetic injection experiment",
  "uuid": "b842e33f-6ebb-4929-960c-b6ea3ce32ff2",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### Tool result

_source line 59 · 2026-05-22T18:51:52.915Z_

<details><summary>↩ Tool result · `toolu_01UXVyFLa4NXzfxyb717Rw9w`</summary>

```text
Loading data...
  Ref: 1080, Foc: 807, Items: 12508
  Injection targets: 242 models, 3001 items
  Item difficulty: mean=0.581, min=0.008, max=0.956
  Unique subjects: 2750

=== Running experiments ===
  [A_capability] seed=1: C%=31.4%, ρ=-0.496, focal%=52.6%, flips=105035, 0.6s
  [B_contamination] seed=1: C%=31.3%, ρ=-0.586, focal%=56.2%, flips=226, 0.2s
  [C_mixed] seed=1: C%=31.9%, ρ=-0.529, focal%=54.9%, flips=52452, 0.4s
  [A_capability] seed=2: C%=31.7%, ρ=-0.544, focal%=54.4%, flips=98392, 0.6s
  [B_contamination] seed=2: C%=31.3%, ρ=-0.587, focal%=56.2%, flips=224, 0.2s
  [C_mixed] seed=2: C%=31.5%, ρ=-0.532, focal%=55.0%, flips=48863, 0.4s
  [A_capability] seed=3: C%=32.9%, ρ=-0.552, focal%=55.7%, flips=103482, 0.8s
  [B_contamination] seed=3: C%=31.4%, ρ=-0.587, focal%=56.4%, flips=216, 0.2s
  [C_mixed] seed=3: C%=32.0%, ρ=-0.546, focal%=54.6%, flips=51943, 0.6s
  [A_capability] seed=4: C%=32.1%, ρ=-0.530, focal%=52.8%, flips=105399, 0.9s
  [B_contamination] seed=4: C%=31.4%, ρ=-0.587, focal%=56.3%, flips=210, 0.2s
  [C_mixed] seed=4: C%=31.8%, ρ=-0.533, focal%=54.0%, flips=58127, 0.6s
  [A_capability] seed=5: C%=31.2%, ρ=-0.540, focal%=55.1%, flips=99761, 0.9s
  [B_contamination] seed=5: C%=31.3%, ρ=-0.587, focal%=56.1%, flips=135, 0.2s
  [C_mixed] seed=5: C%=31.5%, ρ=-0.544, focal%=55.5%, flips=50667, 0.4s

Total time: 7s

Saved: semisynthetic_results.csv (15 rows)
Saved: semisynthetic_gradient_report.md

# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection

**Date**: 2026-05-22 18:51

**Config**: 5 seeds, 1080 ref models (2023), 807 foc models (2024), 12508 items

**Injection**: 242 foc models (30%), ~3001 items (24%)


## Scheme A — Capability

| Metric | Mean ± SD |
|--------|-----------|
| C% (all items) | 31.89 ± 0.68 |
| C% (injected items) | 27.31 ± 0.98 |
| ρ(difficulty, Δ_MH) among C | -0.533 ± 0.022 |
| % focal-favoring | 54.1 ± 1.4 |
| N DIF-C items | 3989 ± 85 |
| Responses flipped | 102414 ± 3168 |
| Items injected | 3001 |

## Scheme B — Contamination

| Metric | Mean ± SD |
|--------|-----------|
| C% (all items) | 31.34 ± 0.03 |
| C% (injected items) | 20.00 ± 20.00 |
| ρ(difficulty, Δ_MH) among C | -0.587 ± 0.000 |
| % focal-favoring | 56.2 ± 0.1 |
| N DIF-C items | 3920 ± 4 |
| Responses flipped | 202 ± 38 |
| Items injected | 5 |

## Scheme C — Mixed

| Metric | Mean ± SD |
|--------|-----------|
| C% (all items) | 31.73 ± 0.23 |
| C% (injected items) | 29.97 ± 1.64 |
| ρ(difficulty, Δ_MH) among C | -0.537 ± 0.008 |
| % focal-favoring | 54.8 ± 0.5 |
| N DIF-C items | 3969 ± 29 |
| Responses flipped | 52410 ± 3483 |
| Items injected | 1522 |

### Quintile Breakdown (Scheme C)

| Quintile | C% | % Focal-Favoring | N DIF-C |
|----------|-----|-------------------|---------|
| Q1 | 34.53 ± 0.38 | 11.1 ± 0.2 | 864 |
| Q2 | 39.55 ± 0.35 | 40.2 ± 0.6 | 988 |
| Q3 | 32.95 ± 0.19 | 70.3 ± 1.0 | 824 |
| Q4 | 30.05 ± 0.46 | 81.1 ± 1.1 | 744 |
| Q5 | 21.68 ± 0.77 | 91.1 ± 1.1 | 548 |

## Interpretation

- **Scheme A** (capability-like): Expects ρ ≈ −0.5 to −0.6 (focal-favoring DIF concentrated on easy items)
- **Scheme B** (contamination-like): Expects ρ ≈ 0 (focal-favoring DIF uniform across difficulty)
- **Scheme C** (mixed): Tests item-level discrimination between the two sources
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "f03859da-1f1c-4f52-8376-df4cf98e1b4e",
  "tool_use_result": {
    "stdout": "Loading data...\n  Ref: 1080, Foc: 807, Items: 12508\n  Injection targets: 242 models, 3001 items\n  Item difficulty: mean=0.581, min=0.008, max=0.956\n  Unique subjects: 2750\n\n=== Running experiments ===\n  [A_capability] seed=1: C%=31.4%, ρ=-0.496, focal%=52.6%, flips=105035, 0.6s\n  [B_contamination] seed=1: C%=31.3%, ρ=-0.586, focal%=56.2%, flips=226, 0.2s\n  [C_mixed] seed=1: C%=31.9%, ρ=-0.529, focal%=54.9%, flips=52452, 0.4s\n  [A_capability] seed=2: C%=31.7%, ρ=-0.544, focal%=54.4%, flips=98392, 0.6s\n  [B_contamination] seed=2: C%=31.3%, ρ=-0.587, focal%=56.2%, flips=224, 0.2s\n  [C_mixed] seed=2: C%=31.5%, ρ=-0.532, focal%=55.0%, flips=48863, 0.4s\n  [A_capability] seed=3: C%=32.9%, ρ=-0.552, focal%=55.7%, flips=103482, 0.8s\n  [B_contamination] seed=3: C%=31.4%, ρ=-0.587, focal%=56.4%, flips=216, 0.2s\n  [C_mixed] seed=3: C%=32.0%, ρ=-0.546, focal%=54.6%, flips=51943, 0.6s\n  [A_capability] seed=4: C%=32.1%, ρ=-0.530, focal%=52.8%, flips=105399, 0.9s\n  [B_contamination] seed=4: C%=31.4%, ρ=-0.587, focal%=56.3%, flips=210, 0.2s\n  [C_mixed] seed=4: C%=31.8%, ρ=-0.533, focal%=54.0%, flips=58127, 0.6s\n  [A_capability] seed=5: C%=31.2%, ρ=-0.540, focal%=55.1%, flips=99761, 0.9s\n  [B_contamination] seed=5: C%=31.3%, ρ=-0.587, focal%=56.1%, flips=135, 0.2s\n  [C_mixed] seed=5: C%=31.5%, ρ=-0.544, focal%=55.5%, flips=50667, 0.4s\n\nTotal time: 7s\n\nSaved: semisynthetic_results.csv (15 rows)\nSaved: semisynthetic_gradient_report.md\n\n# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\n\n**Date**: 2026-05-22 18:51\n\n**Config**: 5 seeds, 1080 ref models (2023), 807 foc models (2024), 12508 items\n\n**Injection**: 242 foc models (30%), ~3001 items (24%)\n\n\n## Scheme A — Capability\n\n| Metric | Mean ± SD |\n|--------|-----------|\n| C% (all items) | 31.89 ± 0.68 |\n| C% (injected items) | 27.31 ± 0.98 |\n| ρ(difficulty, Δ_MH) among C | -0.533 ± 0.022 |\n| % focal-favoring | 54.1 ± 1.4 |\n| N DIF-C items | 3989 ± 85 |\n| Responses flipped | 102414 ± 3168 |\n| Items injected | 3001 |\n\n## Scheme B — Contamination\n\n| Metric | Mean ± SD |\n|--------|-----------|\n| C% (all items) | 31.34 ± 0.03 |\n| C% (injected items) | 20.00 ± 20.00 |\n| ρ(difficulty, Δ_MH) among C | -0.587 ± 0.000 |\n| % focal-favoring | 56.2 ± 0.1 |\n| N DIF-C items | 3920 ± 4 |\n| Responses flipped | 202 ± 38 |\n| Items injected | 5 |\n\n## Scheme C — Mixed\n\n| Metric | Mean ± SD |\n|--------|-----------|\n| C% (all items) | 31.73 ± 0.23 |\n| C% (injected items) | 29.97 ± 1.64 |\n| ρ(difficulty, Δ_MH) among C | -0.537 ± 0.008 |\n| % focal-favoring | 54.8 ± 0.5 |\n| N DIF-C items | 3969 ± 29 |\n| Responses flipped | 52410 ± 3483 |\n| Items injected | 1522 |\n\n### Quintile Breakdown (Scheme C)\n\n| Quintile | C% | % Focal-Favoring | N DIF-C |\n|----------|-----|-------------------|---------|\n| Q1 | 34.53 ± 0.38 | 11.1 ± 0.2 | 864 |\n| Q2 | 39.55 ± 0.35 | 40.2 ± 0.6 | 988 |\n| Q3 | 32.95 ± 0.19 | 70.3 ± 1.0 | 824 |\n| Q4 | 30.05 ± 0.46 | 81.1 ± 1.1 | 744 |\n| Q5 | 21.68 ± 0.77 | 91.1 ± 1.1 | 548 |\n\n## Interpretation\n\n- **Scheme A** (capability-like): Expects ρ ≈ −0.5 to −0.6 (focal-favoring DIF concentrated on easy items)\n- **Scheme B** (contamination-like): Expects ρ ≈ 0 (focal-favoring DIF uniform across difficulty)\n- **Scheme C** (mixed): Tests item-level discrimination between the two sources",
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

_source line 60_

<details><summary>Logged reasoning block</summary>

```text
The results show a problem: Scheme B is barely injecting anything because the subject restriction is too narrow. When I parse item IDs by splitting on `_` and taking everything before the last `_`, there are 2750 "subjects" — this is because item IDs are structured differently than I assumed. Let me check the item ID format.

Also, Scheme B shows ρ ≈ −0.587, which is the same as baseline (no injection) — because only 5 items are being injected with ~200 flips total. The issue is that with 2750 unique subjects, selecting 5 subjects gives very few items.


I need to examine the actual item ID structure to understand how they're formatted.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "372000e1-c5ea-4271-9b67-c605e7abcfbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTs1tkUdnACgzSBDBjx3jv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1861,
      "cache_read_input_tokens": 40899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1861
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

_source line 61_

Scheme B is barely injecting — only 5 items total because the subject parsing yields 2750 unique "subjects" (items aren't structured the way I assumed). Let me check the item ID format and fix the subject extraction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "0f7ab461-b7d0-46f6-83e0-43fe61af6bda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTs1tkUdnACgzSBDBjx3jv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1861,
      "cache_read_input_tokens": 40899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1861
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

_source line 62_

<details open><summary>🔧 Tool call — Bash · `toolu_0134hiJ4S9VcEK5LnCoGcG8a`</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np\nidx = np.load('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix_index.npz', allow_pickle=True)\nitems = idx['item_ids']\nprint('First 20 item IDs:')\nfor i in items[:20]:\n    print(f'  {i}')\nprint()\n\n# Check structure\nparts = [str(i).rsplit('_', 1) for i in items[:20]]\nfor p in parts:\n    print(p)\nprint()\n\n# Try splitting by last underscore + number\nimport re\nsubjects = set()\nfor i in items:\n    s = str(i)\n    # Try removing trailing _N (question number)\n    m = re.match(r'(.+)_(\\d+)$', s)\n    if m:\n        subjects.add(m.group(1))\n    else:\n        subjects.add(s)\nprint(f'Subjects via regex: {len(subjects)}')\nprint('Examples:', sorted(subjects)[:10])\n\"\n",
  "description": "Check item ID format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "b3335825-fc74-4c3e-8e1b-0144f6180814",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTs1tkUdnACgzSBDBjx3jv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1861,
      "cache_read_input_tokens": 40899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1861
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

_source line 63 · 2026-05-22T18:52:10.974Z_

<details><summary>↩ Tool result · `toolu_0134hiJ4S9VcEK5LnCoGcG8a`</summary>

```text
First 20 item IDs:
  abstract_algebra.1
  abstract_algebra.10
  abstract_algebra.100
  abstract_algebra.11
  abstract_algebra.12
  abstract_algebra.13
  abstract_algebra.14
  abstract_algebra.15
  abstract_algebra.16
  abstract_algebra.17
  abstract_algebra.18
  abstract_algebra.2
  abstract_algebra.20
  abstract_algebra.21
  abstract_algebra.22
  abstract_algebra.23
  abstract_algebra.24
  abstract_algebra.25
  abstract_algebra.26
  abstract_algebra.27

['abstract', 'algebra.1']
['abstract', 'algebra.10']
['abstract', 'algebra.100']
['abstract', 'algebra.11']
['abstract', 'algebra.12']
['abstract', 'algebra.13']
['abstract', 'algebra.14']
['abstract', 'algebra.15']
['abstract', 'algebra.16']
['abstract', 'algebra.17']
['abstract', 'algebra.18']
['abstract', 'algebra.2']
['abstract', 'algebra.20']
['abstract', 'algebra.21']
['abstract', 'algebra.22']
['abstract', 'algebra.23']
['abstract', 'algebra.24']
['abstract', 'algebra.25']
['abstract', 'algebra.26']
['abstract', 'algebra.27']

Subjects via regex: 12508
Examples: ['abstract_algebra.1', 'abstract_algebra.10', 'abstract_algebra.100', 'abstract_algebra.11', 'abstract_algebra.12', 'abstract_algebra.13', 'abstract_algebra.14', 'abstract_algebra.15', 'abstract_algebra.16', 'abstract_algebra.17']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "3548937a-3883-4f4a-9ba2-fc571180d6f6",
  "tool_use_result": {
    "stdout": "First 20 item IDs:\n  abstract_algebra.1\n  abstract_algebra.10\n  abstract_algebra.100\n  abstract_algebra.11\n  abstract_algebra.12\n  abstract_algebra.13\n  abstract_algebra.14\n  abstract_algebra.15\n  abstract_algebra.16\n  abstract_algebra.17\n  abstract_algebra.18\n  abstract_algebra.2\n  abstract_algebra.20\n  abstract_algebra.21\n  abstract_algebra.22\n  abstract_algebra.23\n  abstract_algebra.24\n  abstract_algebra.25\n  abstract_algebra.26\n  abstract_algebra.27\n\n['abstract', 'algebra.1']\n['abstract', 'algebra.10']\n['abstract', 'algebra.100']\n['abstract', 'algebra.11']\n['abstract', 'algebra.12']\n['abstract', 'algebra.13']\n['abstract', 'algebra.14']\n['abstract', 'algebra.15']\n['abstract', 'algebra.16']\n['abstract', 'algebra.17']\n['abstract', 'algebra.18']\n['abstract', 'algebra.2']\n['abstract', 'algebra.20']\n['abstract', 'algebra.21']\n['abstract', 'algebra.22']\n['abstract', 'algebra.23']\n['abstract', 'algebra.24']\n['abstract', 'algebra.25']\n['abstract', 'algebra.26']\n['abstract', 'algebra.27']\n\nSubjects via regex: 12508\nExamples: ['abstract_algebra.1', 'abstract_algebra.10', 'abstract_algebra.100', 'abstract_algebra.11', 'abstract_algebra.12', 'abstract_algebra.13', 'abstract_algebra.14', 'abstract_algebra.15', 'abstract_algebra.16', 'abstract_algebra.17']",
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

_source line 64_

<details open><summary>🔧 Tool call — Bash · `toolu_017CYbX818ujd15prnjxcB9v`</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np\nidx = np.load('/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix_index.npz', allow_pickle=True)\nitems = idx['item_ids']\n\n# Items use '.' delimiter: subject.question_number\nsubjects = np.array([str(i).rsplit('.', 1)[0] for i in items])\nunique = np.unique(subjects)\nprint(f'Unique subjects: {len(unique)}')\nprint('Examples:', unique[:10])\nprint()\n\n# Items per subject\nfrom collections import Counter\nc = Counter(subjects)\nprint('Items per subject (first 10):')\nfor s in sorted(c.keys())[:10]:\n    print(f'  {s}: {c[s]}')\nprint()\nprint(f'Mean items/subject: {np.mean(list(c.values())):.1f}')\nprint(f'Min: {min(c.values())}, Max: {max(c.values())}')\n\n# 5 subjects would give how many items?\nsizes = sorted(c.values(), reverse=True)\nprint(f'5 largest subjects: {sum(sizes[:5])} items')\nprint(f'5 random subjects (mean): {5 * np.mean(list(c.values())):.0f} items')\n\"\n",
  "description": "Parse subject from item IDs using dot delimiter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "6311b095-cd42-42e4-ba94-82b39e4b1c32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YD4jGrZNkfwQbwwReerHDU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1022,
      "cache_read_input_tokens": 42760,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1022
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

_source line 65 · 2026-05-22T18:52:23.080Z_

<details><summary>↩ Tool result · `toolu_017CYbX818ujd15prnjxcB9v`</summary>

```text
Unique subjects: 57
Examples: ['abstract_algebra' 'anatomy' 'astronomy' 'business_ethics'
 'clinical_knowledge' 'college_biology' 'college_chemistry'
 'college_computer_science' 'college_mathematics' 'college_medicine']

Items per subject (first 10):
  abstract_algebra: 91
  anatomy: 122
  astronomy: 136
  business_ethics: 93
  clinical_knowledge: 241
  college_biology: 133
  college_chemistry: 81
  college_computer_science: 86
  college_mathematics: 72
  college_medicine: 161

Mean items/subject: 219.4
Min: 72, Max: 1331
5 largest subjects: 3847 items
5 random subjects (mean): 1097 items
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "2fa9b700-c54e-4de1-b81f-c918b08799f9",
  "tool_use_result": {
    "stdout": "Unique subjects: 57\nExamples: ['abstract_algebra' 'anatomy' 'astronomy' 'business_ethics'\n 'clinical_knowledge' 'college_biology' 'college_chemistry'\n 'college_computer_science' 'college_mathematics' 'college_medicine']\n\nItems per subject (first 10):\n  abstract_algebra: 91\n  anatomy: 122\n  astronomy: 136\n  business_ethics: 93\n  clinical_knowledge: 241\n  college_biology: 133\n  college_chemistry: 81\n  college_computer_science: 86\n  college_mathematics: 72\n  college_medicine: 161\n\nMean items/subject: 219.4\nMin: 72, Max: 1331\n5 largest subjects: 3847 items\n5 random subjects (mean): 1097 items",
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

Good — 57 MMLU subjects, dot-delimited. 5 subjects ≈ 1097 items on average. Let me fix the script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "7ba3346f-210c-4d64-87d3-5def22093d08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8vsFqZ8SXpUbzdDw5LX8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 631,
      "cache_read_input_tokens": 43782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 631
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

<details open><summary>🔧 Tool call — Read · `toolu_01CaUMm5ZEsgeVjFRX6B1nUd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "offset": 117,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "8ed7d173-310b-4904-ac72-d127f11cc5c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X8vsFqZ8SXpUbzdDw5LX8E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 631,
      "cache_read_input_tokens": 43782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 631
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

_source line 68 · 2026-05-22T18:52:27.075Z_

<details><summary>↩ Tool result · `toolu_01CaUMm5ZEsgeVjFRX6B1nUd`</summary>

```text
117	print(f"  Ref: {N_ref}, Foc: {N_foc}, Items: {J}")
118	print(f"  Injection targets: {N_inject_models} models, {N_inject_items} items")
119	
120	# Densify the ref/foc submatrices
121	X_ref_base = X_sparse[ref_idx].toarray().astype(np.float64)
122	X_foc_base = X_sparse[foc_idx].toarray().astype(np.float64)
123	
124	# Ref cohort accuracy per item (= item difficulty proxy)
125	item_difficulty = X_ref_base.mean(axis=0)  # shape (J,)
126	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "4557b897-28dd-4cfd-9831-1706e82d7867",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
      "content": "print(f\"  Ref: {N_ref}, Foc: {N_foc}, Items: {J}\")\nprint(f\"  Injection targets: {N_inject_models} models, {N_inject_items} items\")\n\n# Densify the ref/foc submatrices\nX_ref_base = X_sparse[ref_idx].toarray().astype(np.float64)\nX_foc_base = X_sparse[foc_idx].toarray().astype(np.float64)\n\n# Ref cohort accuracy per item (= item difficulty proxy)\nitem_difficulty = X_ref_base.mean(axis=0)  # shape (J,)\n",
      "numLines": 10,
      "startLine": 117,
      "totalLines": 373
    }
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Edit · `toolu_01YLjNUerMraqMUk6a2vamtP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "old_string": "# Get MMLU subjects per item for Scheme B\nitem_subjects = np.array([iid.rsplit('_', 1)[0] if '_' in iid else iid\n                           for iid in item_ids])",
  "new_string": "# Get MMLU subjects per item for Scheme B (format: subject_name.question_number)\nitem_subjects = np.array([str(iid).rsplit('.', 1)[0] for iid in item_ids])"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "80eb3c5d-5264-40e5-be4d-80a2433ff332",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdsZAJqd5YPkBtTPbj5Cco",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 375,
      "cache_read_input_tokens": 44413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 375
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

_source line 70 · 2026-05-22T18:52:31.931Z_

<details><summary>↩ Tool result · `toolu_01YLjNUerMraqMUk6a2vamtP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "8aa488c3-451a-428b-9db2-8abc8f8dcade",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
    "oldString": "# Get MMLU subjects per item for Scheme B\nitem_subjects = np.array([iid.rsplit('_', 1)[0] if '_' in iid else iid\n                           for iid in item_ids])",
    "newString": "# Get MMLU subjects per item for Scheme B (format: subject_name.question_number)\nitem_subjects = np.array([str(iid).rsplit('.', 1)[0] for iid in item_ids])",
    "originalFile": "\"\"\"\nR19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\nTests whether MH-DIF can distinguish capability-like vs contamination-like DIF patterns.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom scipy.stats import chi2 as chi2_dist\nimport time, os, sys\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = os.path.join(ROOT, \"r19_semisynthetic_gradient\")\n\nN_SEEDS = 5\nN_STRATA = 5\nFOC_INJECT_FRAC = 0.30\nITEM_INJECT_FRAC = 0.24\n\n# ════════════════════════════════════════════════════════════════════════════\n#  VECTORIZED MH-DIF — returns per-item results\n# ════════════════════════════════════════════════════════════════════════════\ndef mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item delta_mh, p_value, is_c, direction.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C_mat = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C_mat[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C_mat\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C_mat\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C_mat / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n\n    return delta_j, pval_j, is_c\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  LOAD DATA\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"Loading data...\")\nrm = np.load(f\"{ROOT}/response_matrix.npz\")\nX_sparse = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nidx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\nmodel_names = idx['model_names']\nitem_ids = idx['item_ids']\n\nmeta = pd.read_csv(f\"{ROOT}/model_metadata.csv\")\nname_to_row = {n: i for i, n in enumerate(model_names)}\n\nref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values\nfoc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values\n\nref_idx = np.array([name_to_row[n] for n in ref_models if n in name_to_row])\nfoc_idx = np.array([name_to_row[n] for n in foc_models if n in name_to_row])\n\nN_ref, N_foc, J = len(ref_idx), len(foc_idx), len(item_ids)\nN_inject_models = int(N_foc * FOC_INJECT_FRAC)\nN_inject_items = int(J * ITEM_INJECT_FRAC)\n\nprint(f\"  Ref: {N_ref}, Foc: {N_foc}, Items: {J}\")\nprint(f\"  Injection targets: {N_inject_models} models, {N_inject_items} items\")\n\n# Densify the ref/foc submatrices\nX_ref_base = X_sparse[ref_idx].toarray().astype(np.float64)\nX_foc_base = X_sparse[foc_idx].toarray().astype(np.float64)\n\n# Ref cohort accuracy per item (= item difficulty proxy)\nitem_difficulty = X_ref_base.mean(axis=0)  # shape (J,)\n\nprint(f\"  Item difficulty: mean={item_difficulty.mean():.3f}, \"\n      f\"min={item_difficulty.min():.3f}, max={item_difficulty.max():.3f}\")\n\n# Get MMLU subjects per item for Scheme B\nitem_subjects = np.array([iid.rsplit('_', 1)[0] if '_' in iid else iid\n                           for iid in item_ids])\nunique_subjects = np.unique(item_subjects)\nprint(f\"  Unique subjects: {len(unique_subjects)}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  INJECTION SCHEMES\n# ════════════════════════════════════════════════════════════════════════════\ndef inject_scheme_a(X_foc, inject_model_mask, inject_item_idx, item_diff, rng):\n    \"\"\"Capability-like: injection probability ∝ difficulty (easy items more likely flipped).\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):\n    \"\"\"Contamination-like: uniform injection probability, restricted to 5 random subjects.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,\n                    item_diff, rng, p_const=0.5):\n    \"\"\"Mixed: half items use scheme A, half use scheme B.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    # Scheme A half\n    for j in inject_item_idx_a:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    # Scheme B half\n    for j in inject_item_idx_b:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running experiments ===\")\nresults = []\nt0 = time.time()\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection models and items (shared across schemes within seed)\n    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)\n    inject_model_mask = np.zeros(N_foc, dtype=bool)\n    inject_model_mask[inject_model_idx] = True\n\n    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)\n\n    # Scheme B: select 5 random subjects, pick injection items from those subjects\n    selected_subjects = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask = np.isin(item_subjects, selected_subjects)\n    subject_item_pool = np.where(subject_mask)[0]\n    n_b_items = min(N_inject_items, len(subject_item_pool))\n    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)\n\n    # Scheme C: split A items in half\n    half = N_inject_items // 2\n    inject_item_idx_c_a = inject_item_idx_all[:half]\n    # For scheme C's B half, pick from 5 random subjects\n    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask_c = np.isin(item_subjects, selected_subjects_c)\n    subject_pool_c = np.where(subject_mask_c)[0]\n    # Exclude items already used by A half\n    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)\n    n_c_b = min(half, len(subject_pool_c))\n    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)\n\n    schemes = {\n        'A_capability': lambda: inject_scheme_a(\n            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),\n        'B_contamination': lambda: inject_scheme_b(\n            X_foc_base, inject_model_mask, inject_item_idx_b, rng),\n        'C_mixed': lambda: inject_scheme_c(\n            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,\n            item_difficulty, rng),\n    }\n\n    for scheme_name, inject_fn in schemes.items():\n        t1 = time.time()\n        rng_state = rng.get_state()\n\n        X_foc_inj, n_flipped = inject_fn()\n\n        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # C% among all items\n        c_pct_all = is_c.sum() / J * 100\n\n        # C% among injected items only\n        inj_arr = np.array(sorted(injected_items))\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n\n        # ρ(difficulty, Δ_MH) among DIF-C items\n        c_idx = np.where(is_c)[0]\n        if len(c_idx) >= 3:\n            rho, rho_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n        else:\n            rho, rho_p = np.nan, np.nan\n\n        # Direction distribution among DIF-C items\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j < 0)).sum()   # negative delta = focal advantage\n        n_ref_favoring = (is_c & (delta_j > 0)).sum()\n        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # For scheme C: per-quintile analysis\n        quintile_data = {}\n        if scheme_name == 'C_mixed':\n            quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n            quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n\n            for q in range(5):\n                q_mask = (quintile_labels == q)\n                q_items = np.where(q_mask)[0]\n                q_c = is_c[q_items].sum()\n                q_total = len(q_items)\n                q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n                q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()\n                q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n                quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n                quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n                quintile_data[f'q{q+1}_n_c'] = q_c\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            n_c_total=n_c_total,\n            rho_diff_delta=rho,\n            rho_p_value=rho_p,\n            pct_focal_favoring=pct_focal_favoring,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ={rho:.3f}, focal%={pct_focal_favoring:.1f}%, \"\n              f\"flips={n_flipped}, {elapsed:.1f}s\")\n\ntotal_time = time.time() - t0\nprint(f\"\\nTotal time: {total_time:.0f}s\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  SAVE RESULTS\n# ════════════════════════════════════════════════════════════════════════════\ndf = pd.DataFrame(results)\ndf.to_csv(os.path.join(OUT, \"semisynthetic_results.csv\"), index=False)\nprint(f\"\\nSaved: semisynthetic_results.csv ({len(df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  GENERATE REPORT\n# ════════════════════════════════════════════════════════════════════════════\nreport_lines = [\"# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\\n\"]\nreport_lines.append(f\"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\\n\")\nreport_lines.append(f\"**Config**: {N_SEEDS} seeds, {N_ref} ref models (2023), \"\n                    f\"{N_foc} foc models (2024), {J} items\\n\")\nreport_lines.append(f\"**Injection**: {N_inject_models} foc models ({FOC_INJECT_FRAC*100:.0f}%), \"\n                    f\"~{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\\n\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| ρ(difficulty, Δ_MH) among C | {sub['rho_diff_delta'].mean():.3f} ± {sub['rho_diff_delta'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    if scheme == 'C_mixed':\n        report_lines.append(f\"\\n### Quintile Breakdown (Scheme C)\\n\")\n        report_lines.append(f\"| Quintile | C% | % Focal-Favoring | N DIF-C |\")\n        report_lines.append(f\"|----------|-----|-------------------|---------|\")\n        for q in range(1, 6):\n            col_c = f'q{q}_c_pct'\n            col_f = f'q{q}_pct_focal'\n            col_n = f'q{q}_n_c'\n            if col_c in sub.columns:\n                report_lines.append(\n                    f\"| Q{q} | {sub[col_c].mean():.2f} ± {sub[col_c].std():.2f} | \"\n                    f\"{sub[col_f].mean():.1f} ± {sub[col_f].std():.1f} | \"\n                    f\"{sub[col_n].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **Scheme A** (capability-like): Expects ρ ≈ −0.5 to −0.6 \"\n                    \"(focal-favoring DIF concentrated on easy items)\")\nreport_lines.append(\"- **Scheme B** (contamination-like): Expects ρ ≈ 0 \"\n                    \"(focal-favoring DIF uniform across difficulty)\")\nreport_lines.append(\"- **Scheme C** (mixed): Tests item-level discrimination between the two sources\")\n\nreport_text = \"\\n\".join(report_lines) + \"\\n\"\n\nwith open(os.path.join(OUT, \"semisynthetic_gradient_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"Saved: semisynthetic_gradient_report.md\")\nprint(\"\\n\" + report_text)\n",
    "structuredPatch": [
      {
        "oldStart": 127,
        "oldLines": 9,
        "newStart": 127,
        "newLines": 8,
        "lines": [
          " print(f\"  Item difficulty: mean={item_difficulty.mean():.3f}, \"",
          "       f\"min={item_difficulty.min():.3f}, max={item_difficulty.max():.3f}\")",
          " ",
          "-# Get MMLU subjects per item for Scheme B",
          "-item_subjects = np.array([iid.rsplit('_', 1)[0] if '_' in iid else iid",
          "-                           for iid in item_ids])",
          "+# Get MMLU subjects per item for Scheme B (format: subject_name.question_number)",
          "+item_subjects = np.array([str(iid).rsplit('.', 1)[0] for iid in item_ids])",
          " unique_subjects = np.unique(item_subjects)",
          " print(f\"  Unique subjects: {len(unique_subjects)}\")",
          " "
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

_source line 71_

<details open><summary>🔧 Tool call — Bash · `toolu_01T7yxuZxCMhr28EBBkShofR`</summary>

```json
{
  "command": "python3 artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "description": "Re-run with fixed subject parsing",
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
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "ccb554b7-1b46-4401-938c-49d9bb4721f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzWGXEriM7asi37Gr7UXeQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 339,
      "cache_read_input_tokens": 44788,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 339
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

_source line 72_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bhsjzfah3",
  "tool_use_id": "toolu_01T7yxuZxCMhr28EBBkShofR",
  "description": "Re-run with fixed subject parsing",
  "task_type": "local_bash",
  "uuid": "510d307d-0381-4324-b4ae-f2ee23886e30",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### System

_source line 73_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bhsjzfah3",
  "tool_use_id": "toolu_01T7yxuZxCMhr28EBBkShofR",
  "status": "completed",
  "output_file": "",
  "summary": "Re-run with fixed subject parsing",
  "uuid": "799001c4-64a3-4a70-af1c-9f79dde0a542",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### Tool result

_source line 74 · 2026-05-22T18:52:44.403Z_

<details><summary>↩ Tool result · `toolu_01T7yxuZxCMhr28EBBkShofR`</summary>

```text
Loading data...
  Ref: 1080, Foc: 807, Items: 12508
  Injection targets: 242 models, 3001 items
  Item difficulty: mean=0.581, min=0.008, max=0.956
  Unique subjects: 57

=== Running experiments ===
  [A_capability] seed=1: C%=31.5%, ρ=-0.496, focal%=52.7%, flips=105196, 0.6s
  [B_contamination] seed=1: C%=32.5%, ρ=-0.603, focal%=56.8%, flips=53279, 0.3s
  [C_mixed] seed=1: C%=31.1%, ρ=-0.531, focal%=52.4%, flips=104104, 0.6s
  [A_capability] seed=2: C%=31.7%, ρ=-0.541, focal%=54.8%, flips=98452, 0.6s
  [B_contamination] seed=2: C%=31.8%, ρ=-0.595, focal%=56.4%, flips=39733, 0.3s
  [C_mixed] seed=2: C%=32.0%, ρ=-0.566, focal%=55.7%, flips=82803, 0.5s
  [A_capability] seed=3: C%=32.9%, ρ=-0.551, focal%=55.6%, flips=103863, 0.6s
  [B_contamination] seed=3: C%=33.2%, ρ=-0.623, focal%=55.8%, flips=74372, 0.3s
  [C_mixed] seed=3: C%=31.9%, ρ=-0.562, focal%=53.2%, flips=83437, 0.5s
  [A_capability] seed=4: C%=32.1%, ρ=-0.531, focal%=53.0%, flips=105362, 0.6s
  [B_contamination] seed=4: C%=31.7%, ρ=-0.586, focal%=56.5%, flips=26927, 0.2s
  [C_mixed] seed=4: C%=32.6%, ρ=-0.574, focal%=53.5%, flips=114043, 0.5s
  [A_capability] seed=5: C%=31.2%, ρ=-0.540, focal%=55.1%, flips=99768, 0.6s
  [B_contamination] seed=5: C%=31.2%, ρ=-0.586, focal%=56.4%, flips=34991, 0.3s
  [C_mixed] seed=5: C%=32.2%, ρ=-0.572, focal%=56.1%, flips=84375, 0.5s

Total time: 7s

Saved: semisynthetic_results.csv (15 rows)
Saved: semisynthetic_gradient_report.md

# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection

**Date**: 2026-05-22 18:52

**Config**: 5 seeds, 1080 ref models (2023), 807 foc models (2024), 12508 items

**Injection**: 242 foc models (30%), ~3001 items (24%)


## Scheme A — Capability

| Metric | Mean ± SD |
|--------|-----------|
| C% (all items) | 31.88 ± 0.65 |
| C% (injected items) | 27.33 ± 0.94 |
| ρ(difficulty, Δ_MH) among C | -0.532 ± 0.021 |
| % focal-favoring | 54.2 ± 1.3 |
| N DIF-C items | 3988 ± 81 |
| Responses flipped | 102528 ± 3208 |
| Items injected | 3001 |

## Scheme B — Contamination

| Metric | Mean ± SD |
|--------|-----------|
| C% (all items) | 32.07 ± 0.79 |
| C% (injected items) | 39.22 ± 6.34 |
| ρ(difficulty, Δ_MH) among C | -0.599 ± 0.015 |
| % focal-favoring | 56.4 ± 0.4 |
| N DIF-C items | 4011 ± 99 |
| Responses flipped | 45860 ± 18588 |
| Items injected | 873 |

## Scheme C — Mixed

| Metric | Mean ± SD |
|--------|-----------|
| C% (all items) | 31.98 ± 0.54 |
| C% (injected items) | 31.28 ± 2.87 |
| ρ(difficulty, Δ_MH) among C | -0.561 ± 0.017 |
| % focal-favoring | 54.2 ± 1.6 |
| N DIF-C items | 4000 ± 67 |
| Responses flipped | 93752 ± 14432 |
| Items injected | 2407 |

### Quintile Breakdown (Scheme C)

| Quintile | C% | % Focal-Favoring | N DIF-C |
|----------|-----|-------------------|---------|
| Q1 | 37.21 ± 1.32 | 10.8 ± 0.7 | 931 |
| Q2 | 39.14 ± 0.56 | 40.0 ± 1.5 | 978 |
| Q3 | 32.57 ± 0.40 | 70.5 ± 1.5 | 815 |
| Q4 | 29.66 ± 0.31 | 82.2 ± 2.9 | 735 |
| Q5 | 21.42 ± 1.23 | 91.7 ± 2.6 | 542 |

## Interpretation

- **Scheme A** (capability-like): Expects ρ ≈ −0.5 to −0.6 (focal-favoring DIF concentrated on easy items)
- **Scheme B** (contamination-like): Expects ρ ≈ 0 (focal-favoring DIF uniform across difficulty)
- **Scheme C** (mixed): Tests item-level discrimination between the two sources
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "a7f54b20-9bc5-4a67-ad1e-58b00a210d1b",
  "tool_use_result": {
    "stdout": "Loading data...\n  Ref: 1080, Foc: 807, Items: 12508\n  Injection targets: 242 models, 3001 items\n  Item difficulty: mean=0.581, min=0.008, max=0.956\n  Unique subjects: 57\n\n=== Running experiments ===\n  [A_capability] seed=1: C%=31.5%, ρ=-0.496, focal%=52.7%, flips=105196, 0.6s\n  [B_contamination] seed=1: C%=32.5%, ρ=-0.603, focal%=56.8%, flips=53279, 0.3s\n  [C_mixed] seed=1: C%=31.1%, ρ=-0.531, focal%=52.4%, flips=104104, 0.6s\n  [A_capability] seed=2: C%=31.7%, ρ=-0.541, focal%=54.8%, flips=98452, 0.6s\n  [B_contamination] seed=2: C%=31.8%, ρ=-0.595, focal%=56.4%, flips=39733, 0.3s\n  [C_mixed] seed=2: C%=32.0%, ρ=-0.566, focal%=55.7%, flips=82803, 0.5s\n  [A_capability] seed=3: C%=32.9%, ρ=-0.551, focal%=55.6%, flips=103863, 0.6s\n  [B_contamination] seed=3: C%=33.2%, ρ=-0.623, focal%=55.8%, flips=74372, 0.3s\n  [C_mixed] seed=3: C%=31.9%, ρ=-0.562, focal%=53.2%, flips=83437, 0.5s\n  [A_capability] seed=4: C%=32.1%, ρ=-0.531, focal%=53.0%, flips=105362, 0.6s\n  [B_contamination] seed=4: C%=31.7%, ρ=-0.586, focal%=56.5%, flips=26927, 0.2s\n  [C_mixed] seed=4: C%=32.6%, ρ=-0.574, focal%=53.5%, flips=114043, 0.5s\n  [A_capability] seed=5: C%=31.2%, ρ=-0.540, focal%=55.1%, flips=99768, 0.6s\n  [B_contamination] seed=5: C%=31.2%, ρ=-0.586, focal%=56.4%, flips=34991, 0.3s\n  [C_mixed] seed=5: C%=32.2%, ρ=-0.572, focal%=56.1%, flips=84375, 0.5s\n\nTotal time: 7s\n\nSaved: semisynthetic_results.csv (15 rows)\nSaved: semisynthetic_gradient_report.md\n\n# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\n\n**Date**: 2026-05-22 18:52\n\n**Config**: 5 seeds, 1080 ref models (2023), 807 foc models (2024), 12508 items\n\n**Injection**: 242 foc models (30%), ~3001 items (24%)\n\n\n## Scheme A — Capability\n\n| Metric | Mean ± SD |\n|--------|-----------|\n| C% (all items) | 31.88 ± 0.65 |\n| C% (injected items) | 27.33 ± 0.94 |\n| ρ(difficulty, Δ_MH) among C | -0.532 ± 0.021 |\n| % focal-favoring | 54.2 ± 1.3 |\n| N DIF-C items | 3988 ± 81 |\n| Responses flipped | 102528 ± 3208 |\n| Items injected | 3001 |\n\n## Scheme B — Contamination\n\n| Metric | Mean ± SD |\n|--------|-----------|\n| C% (all items) | 32.07 ± 0.79 |\n| C% (injected items) | 39.22 ± 6.34 |\n| ρ(difficulty, Δ_MH) among C | -0.599 ± 0.015 |\n| % focal-favoring | 56.4 ± 0.4 |\n| N DIF-C items | 4011 ± 99 |\n| Responses flipped | 45860 ± 18588 |\n| Items injected | 873 |\n\n## Scheme C — Mixed\n\n| Metric | Mean ± SD |\n|--------|-----------|\n| C% (all items) | 31.98 ± 0.54 |\n| C% (injected items) | 31.28 ± 2.87 |\n| ρ(difficulty, Δ_MH) among C | -0.561 ± 0.017 |\n| % focal-favoring | 54.2 ± 1.6 |\n| N DIF-C items | 4000 ± 67 |\n| Responses flipped | 93752 ± 14432 |\n| Items injected | 2407 |\n\n### Quintile Breakdown (Scheme C)\n\n| Quintile | C% | % Focal-Favoring | N DIF-C |\n|----------|-----|-------------------|---------|\n| Q1 | 37.21 ± 1.32 | 10.8 ± 0.7 | 931 |\n| Q2 | 39.14 ± 0.56 | 40.0 ± 1.5 | 978 |\n| Q3 | 32.57 ± 0.40 | 70.5 ± 1.5 | 815 |\n| Q4 | 29.66 ± 0.31 | 82.2 ± 2.9 | 735 |\n| Q5 | 21.42 ± 1.23 | 91.7 ± 2.6 | 542 |\n\n## Interpretation\n\n- **Scheme A** (capability-like): Expects ρ ≈ −0.5 to −0.6 (focal-favoring DIF concentrated on easy items)\n- **Scheme B** (contamination-like): Expects ρ ≈ 0 (focal-favoring DIF uniform across difficulty)\n- **Scheme C** (mixed): Tests item-level discrimination between the two sources",
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

_source line 75_

<details><summary>Logged reasoning block</summary>

```text
The results are problematic. Both Scheme A and Scheme B show similar ρ values (−0.53 and −0.60), and both have the same direction of correlation. The expectation was that Scheme B (contamination-like, uniform injection) would show ρ ≈ 0, but it's showing ρ ≈ −0.60.

This is likely because:
1. The **baseline** DIF already has a strong negative ρ (from the real data). The injected signal is getting overwhelmed by the existing DIF pattern.
2. The Scheme B injection is producing very few flips (only ~46k with ~873 items), which is relatively small compared to the full 12508 items and existing DIF.


3. I'm computing ρ across all DIF-C items, not just the injected ones, so the existing ~3900 DIF-C items with their strong baseline ρ ≈ −0.59 are dominating the result and masking any effect from the injection.

I need to reconsider the approach—either establish a clean baseline first and then measure how injection shifts it, compute ρ only among the newly injected items that become DIF-C, or use a controlled setup where the ground truth is known.

Looking back at the task spec, it asks for ρ among DIF-C items, but the real data already has substantial existing DIF that's overwhelming the signal. The task expects Scheme A to produce ρ ≈ −0.5 to −0.6, so I need to figure out whether I should be measuring the change in ρ or isolating just the injected items' contribution. - All DIF-C items (as currently)
- Only DIF-C items that were injected
- Only DIF-C items that were NOT injected (baseline reference)

This way I can see if the injection items show a different ρ than non-injection items. The real issue with Scheme B is that uniform p=0.5 injection doesn't account for difficulty: easy items have fewer 0s to flip since models already get them right, while hard items have more 0s available to flip. So even with uniform injection probability, the actual flip pattern becomes difficulty-dependent, creating the opposite effect of what I'm trying to achieve.

Since the MH statistic is conditioned on total score, I need to check whether the MH delta itself correlates with difficulty rather than just the raw flip counts. Let me add a baseline run with no injection, compute ρ separately for injected versus non-injected DIF-C items, and reconsider whether Scheme B needs a different injection strategy altogether.

The core issue is that the existing DIF pattern already dominates the signal, so I should either measure ρ only among the injected items or subtract out the baseline to isolate the contamination effect.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "3313eb3d-7cad-4df3-82c2-d30ea004fb52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qnt717akiYLzYb53RVpMz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1834,
      "cache_read_input_tokens": 45127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1834
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

_source line 76_

The results show a problem: both schemes show ρ ≈ −0.53 to −0.60 because the existing baseline DIF dominates (~3900 C items already present). I need to isolate the injection signal by (1) measuring baseline, and (2) computing ρ among injected items only.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "ede5b942-b71b-4d6f-ba86-92820cc427a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qnt717akiYLzYb53RVpMz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1834,
      "cache_read_input_tokens": 45127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1834
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

_source line 77_

<details open><summary>🔧 Tool call — Read · `toolu_012kNkZsLJfodtmw9X6KfoL9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "offset": 150,
  "limit": 120
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "af38ac42-2845-4d40-a42c-89b49b123494",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qnt717akiYLzYb53RVpMz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1834,
      "cache_read_input_tokens": 45127,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1834
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

_source line 78 · 2026-05-22T18:53:18.423Z_

<details><summary>↩ Tool result · `toolu_012kNkZsLJfodtmw9X6KfoL9`</summary>

```text
150	
151	
152	def inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):
153	    """Contamination-like: uniform injection probability, restricted to 5 random subjects."""
154	    X = X_foc.copy()
155	    n_flipped = 0
156	    for j in inject_item_idx:
157	        for i in np.where(inject_model_mask)[0]:
158	            if X[i, j] == 0 and rng.random() < p_const:
159	                X[i, j] = 1
160	                n_flipped += 1
161	    return X, n_flipped
162	
163	
164	def inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,
165	                    item_diff, rng, p_const=0.5):
166	    """Mixed: half items use scheme A, half use scheme B."""
167	    X = X_foc.copy()
168	    n_flipped = 0
169	    # Scheme A half
170	    for j in inject_item_idx_a:
171	        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))
172	        for i in np.where(inject_model_mask)[0]:
173	            if X[i, j] == 0 and rng.random() < p_inject:
174	                X[i, j] = 1
175	                n_flipped += 1
176	    # Scheme B half
177	    for j in inject_item_idx_b:
178	        for i in np.where(inject_model_mask)[0]:
179	            if X[i, j] == 0 and rng.random() < p_const:
180	                X[i, j] = 1
181	                n_flipped += 1
182	    return X, n_flipped
183	
184	
185	# ════════════════════════════════════════════════════════════════════════════
186	#  RUN EXPERIMENTS
187	# ════════════════════════════════════════════════════════════════════════════
188	print("\n=== Running experiments ===")
189	results = []
190	t0 = time.time()
191	
192	for seed in range(1, N_SEEDS + 1):
193	    rng = np.random.RandomState(seed * 42)
194	
195	    # Select injection models and items (shared across schemes within seed)
196	    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)
197	    inject_model_mask = np.zeros(N_foc, dtype=bool)
198	    inject_model_mask[inject_model_idx] = True
199	
200	    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)
201	
202	    # Scheme B: select 5 random subjects, pick injection items from those subjects
203	    selected_subjects = rng.choice(unique_subjects, 5, replace=False)
204	    subject_mask = np.isin(item_subjects, selected_subjects)
205	    subject_item_pool = np.where(subject_mask)[0]
206	    n_b_items = min(N_inject_items, len(subject_item_pool))
207	    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)
208	
209	    # Scheme C: split A items in half
210	    half = N_inject_items // 2
211	    inject_item_idx_c_a = inject_item_idx_all[:half]
212	    # For scheme C's B half, pick from 5 random subjects
213	    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)
214	    subject_mask_c = np.isin(item_subjects, selected_subjects_c)
215	    subject_pool_c = np.where(subject_mask_c)[0]
216	    # Exclude items already used by A half
217	    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)
218	    n_c_b = min(half, len(subject_pool_c))
219	    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)
220	
221	    schemes = {
222	        'A_capability': lambda: inject_scheme_a(
223	            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),
224	        'B_contamination': lambda: inject_scheme_b(
225	            X_foc_base, inject_model_mask, inject_item_idx_b, rng),
226	        'C_mixed': lambda: inject_scheme_c(
227	            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,
228	            item_difficulty, rng),
229	    }
230	
231	    for scheme_name, inject_fn in schemes.items():
232	        t1 = time.time()
233	        rng_state = rng.get_state()
234	
235	        X_foc_inj, n_flipped = inject_fn()
236	
237	        # Determine which items were injected for this scheme
238	        if scheme_name == 'A_capability':
239	            injected_items = set(inject_item_idx_all)
240	        elif scheme_name == 'B_contamination':
241	            injected_items = set(inject_item_idx_b)
242	        else:  # C_mixed
243	            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)
244	
245	        # Run MH-DIF
246	        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)
247	
248	        # C% among all items
249	        c_pct_all = is_c.sum() / J * 100
250	
251	        # C% among injected items only
252	        inj_arr = np.array(sorted(injected_items))
253	        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0
254	
255	        # ρ(difficulty, Δ_MH) among DIF-C items
256	        c_idx = np.where(is_c)[0]
257	        if len(c_idx) >= 3:
258	            rho, rho_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])
259	        else:
260	            rho, rho_p = np.nan, np.nan
261	
262	        # Direction distribution among DIF-C items
263	        n_c_total = is_c.sum()
264	        n_focal_favoring = (is_c & (delta_j < 0)).sum()   # negative delta = focal advantage
265	        n_ref_favoring = (is_c & (delta_j > 0)).sum()
266	        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0
267	
268	        # For scheme C: per-quintile analysis
269	        quintile_data = {}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "0d7001d2-89e9-4c5a-874e-31511f9a4137",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
      "content": "\n\ndef inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):\n    \"\"\"Contamination-like: uniform injection probability, restricted to 5 random subjects.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,\n                    item_diff, rng, p_const=0.5):\n    \"\"\"Mixed: half items use scheme A, half use scheme B.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    # Scheme A half\n    for j in inject_item_idx_a:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    # Scheme B half\n    for j in inject_item_idx_b:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running experiments ===\")\nresults = []\nt0 = time.time()\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection models and items (shared across schemes within seed)\n    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)\n    inject_model_mask = np.zeros(N_foc, dtype=bool)\n    inject_model_mask[inject_model_idx] = True\n\n    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)\n\n    # Scheme B: select 5 random subjects, pick injection items from those subjects\n    selected_subjects = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask = np.isin(item_subjects, selected_subjects)\n    subject_item_pool = np.where(subject_mask)[0]\n    n_b_items = min(N_inject_items, len(subject_item_pool))\n    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)\n\n    # Scheme C: split A items in half\n    half = N_inject_items // 2\n    inject_item_idx_c_a = inject_item_idx_all[:half]\n    # For scheme C's B half, pick from 5 random subjects\n    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask_c = np.isin(item_subjects, selected_subjects_c)\n    subject_pool_c = np.where(subject_mask_c)[0]\n    # Exclude items already used by A half\n    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)\n    n_c_b = min(half, len(subject_pool_c))\n    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)\n\n    schemes = {\n        'A_capability': lambda: inject_scheme_a(\n            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),\n        'B_contamination': lambda: inject_scheme_b(\n            X_foc_base, inject_model_mask, inject_item_idx_b, rng),\n        'C_mixed': lambda: inject_scheme_c(\n            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,\n            item_difficulty, rng),\n    }\n\n    for scheme_name, inject_fn in schemes.items():\n        t1 = time.time()\n        rng_state = rng.get_state()\n\n        X_foc_inj, n_flipped = inject_fn()\n\n        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # C% among all items\n        c_pct_all = is_c.sum() / J * 100\n\n        # C% among injected items only\n        inj_arr = np.array(sorted(injected_items))\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n\n        # ρ(difficulty, Δ_MH) among DIF-C items\n        c_idx = np.where(is_c)[0]\n        if len(c_idx) >= 3:\n            rho, rho_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n        else:\n            rho, rho_p = np.nan, np.nan\n\n        # Direction distribution among DIF-C items\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j < 0)).sum()   # negative delta = focal advantage\n        n_ref_favoring = (is_c & (delta_j > 0)).sum()\n        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # For scheme C: per-quintile analysis\n        quintile_data = {}",
      "numLines": 120,
      "startLine": 150,
      "totalLines": 372
    }
  }
}
```

</details>

---

### Assistant

_source line 79_

Now I'll rewrite the experiment section to add baseline measurement and compute ρ separately for injected vs non-injected items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "98380180-eb3a-4e0c-8eb3-2b882dc123c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eio5K9VNcatAA2r2rNNCrF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3661,
      "cache_read_input_tokens": 46961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3661
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

_source line 80_

<details open><summary>🔧 Tool call — Edit · `toolu_01GKfP5sQZgAGeSc4uLj5Qpa`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "old_string": "# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running experiments ===\")\nresults = []\nt0 = time.time()\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection models and items (shared across schemes within seed)\n    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)\n    inject_model_mask = np.zeros(N_foc, dtype=bool)\n    inject_model_mask[inject_model_idx] = True\n\n    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)\n\n    # Scheme B: select 5 random subjects, pick injection items from those subjects\n    selected_subjects = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask = np.isin(item_subjects, selected_subjects)\n    subject_item_pool = np.where(subject_mask)[0]\n    n_b_items = min(N_inject_items, len(subject_item_pool))\n    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)\n\n    # Scheme C: split A items in half\n    half = N_inject_items // 2\n    inject_item_idx_c_a = inject_item_idx_all[:half]\n    # For scheme C's B half, pick from 5 random subjects\n    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask_c = np.isin(item_subjects, selected_subjects_c)\n    subject_pool_c = np.where(subject_mask_c)[0]\n    # Exclude items already used by A half\n    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)\n    n_c_b = min(half, len(subject_pool_c))\n    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)\n\n    schemes = {\n        'A_capability': lambda: inject_scheme_a(\n            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),\n        'B_contamination': lambda: inject_scheme_b(\n            X_foc_base, inject_model_mask, inject_item_idx_b, rng),\n        'C_mixed': lambda: inject_scheme_c(\n            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,\n            item_difficulty, rng),\n    }\n\n    for scheme_name, inject_fn in schemes.items():\n        t1 = time.time()\n        rng_state = rng.get_state()\n\n        X_foc_inj, n_flipped = inject_fn()\n\n        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # C% among all items\n        c_pct_all = is_c.sum() / J * 100\n\n        # C% among injected items only\n        inj_arr = np.array(sorted(injected_items))\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n\n        # ρ(difficulty, Δ_MH) among DIF-C items\n        c_idx = np.where(is_c)[0]\n        if len(c_idx) >= 3:\n            rho, rho_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n        else:\n            rho, rho_p = np.nan, np.nan\n\n        # Direction distribution among DIF-C items\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j < 0)).sum()   # negative delta = focal advantage\n        n_ref_favoring = (is_c & (delta_j > 0)).sum()\n        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # For scheme C: per-quintile analysis\n        quintile_data = {}\n        if scheme_name == 'C_mixed':\n            quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n            quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n\n            for q in range(5):\n                q_mask = (quintile_labels == q)\n                q_items = np.where(q_mask)[0]\n                q_c = is_c[q_items].sum()\n                q_total = len(q_items)\n                q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n                q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()\n                q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n                quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n                quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n                quintile_data[f'q{q+1}_n_c'] = q_c\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            n_c_total=n_c_total,\n            rho_diff_delta=rho,\n            rho_p_value=rho_p,\n            pct_focal_favoring=pct_focal_favoring,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ={rho:.3f}, focal%={pct_focal_favoring:.1f}%, \"\n              f\"flips={n_flipped}, {elapsed:.1f}s\")",
  "new_string": "# ════════════════════════════════════════════════════════════════════════════\n#  BASELINE (no injection)\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Baseline (no injection) ===\")\ndelta_base, pval_base, is_c_base = mh_dif_vec(X_ref_base, X_foc_base, n_strata=N_STRATA)\nc_idx_base = np.where(is_c_base)[0]\nrho_base, _ = stats.spearmanr(item_difficulty[c_idx_base], delta_base[c_idx_base])\nn_c_base = is_c_base.sum()\nn_focal_base = (is_c_base & (delta_base < 0)).sum()\nprint(f\"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, \"\n      f\"focal%={n_focal_base/n_c_base*100:.1f}%, N_C={n_c_base}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running experiments ===\")\nresults = []\nt0 = time.time()\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection models and items (shared across schemes within seed)\n    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)\n    inject_model_mask = np.zeros(N_foc, dtype=bool)\n    inject_model_mask[inject_model_idx] = True\n\n    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)\n\n    # Scheme B: select 5 random subjects, pick injection items from those subjects\n    selected_subjects = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask = np.isin(item_subjects, selected_subjects)\n    subject_item_pool = np.where(subject_mask)[0]\n    n_b_items = min(N_inject_items, len(subject_item_pool))\n    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)\n\n    # Scheme C: split A items in half\n    half = N_inject_items // 2\n    inject_item_idx_c_a = inject_item_idx_all[:half]\n    # For scheme C's B half, pick from 5 random subjects\n    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask_c = np.isin(item_subjects, selected_subjects_c)\n    subject_pool_c = np.where(subject_mask_c)[0]\n    # Exclude items already used by A half\n    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)\n    n_c_b = min(half, len(subject_pool_c))\n    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)\n\n    schemes = {\n        'A_capability': lambda: inject_scheme_a(\n            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),\n        'B_contamination': lambda: inject_scheme_b(\n            X_foc_base, inject_model_mask, inject_item_idx_b, rng),\n        'C_mixed': lambda: inject_scheme_c(\n            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,\n            item_difficulty, rng),\n    }\n\n    for scheme_name, inject_fn in schemes.items():\n        t1 = time.time()\n\n        X_foc_inj, n_flipped = inject_fn()\n\n        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # C% among all items\n        c_pct_all = is_c.sum() / J * 100\n\n        # C% among injected items only\n        inj_arr = np.array(sorted(injected_items))\n        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100\n\n        # ρ(difficulty, Δ_MH) — all C items, injected-C items, non-injected-C items\n        c_idx = np.where(is_c)[0]\n        if len(c_idx) >= 3:\n            rho_all, rho_all_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n        else:\n            rho_all, rho_all_p = np.nan, np.nan\n\n        c_inj_mask = is_c.copy()\n        c_inj_mask[non_inj_arr] = False\n        c_inj_idx = np.where(c_inj_mask)[0]\n        if len(c_inj_idx) >= 3:\n            rho_inj, rho_inj_p = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])\n        else:\n            rho_inj, rho_inj_p = np.nan, np.nan\n\n        c_noninj_mask = is_c.copy()\n        c_noninj_mask[inj_arr] = False\n        c_noninj_idx = np.where(c_noninj_mask)[0]\n        if len(c_noninj_idx) >= 3:\n            rho_noninj, _ = stats.spearmanr(item_difficulty[c_noninj_idx], delta_j[c_noninj_idx])\n        else:\n            rho_noninj = np.nan\n\n        # Direction distribution among DIF-C items\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j < 0)).sum()\n        n_ref_favoring = (is_c & (delta_j > 0)).sum()\n        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # Direction among injected C items only\n        n_c_inj = c_inj_mask.sum()\n        n_focal_inj = (c_inj_mask & (delta_j < 0)).sum()\n        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0\n\n        # Newly flagged items (C after injection but not in baseline)\n        newly_c = is_c & ~is_c_base\n        n_newly_c = newly_c.sum()\n        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)\n        n_newly_c_inj = newly_c_inj.sum()\n\n        # ρ among newly flagged items\n        newly_idx = np.where(newly_c)[0]\n        if len(newly_idx) >= 3:\n            rho_new, _ = stats.spearmanr(item_difficulty[newly_idx], delta_j[newly_idx])\n        else:\n            rho_new = np.nan\n\n        # Per-quintile analysis (for all schemes, not just C)\n        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n        quintile_data = {}\n        for q in range(5):\n            q_mask = (quintile_labels == q)\n            q_items = np.where(q_mask)[0]\n            q_inj_items = np.intersect1d(q_items, inj_arr)\n            q_c = is_c[q_items].sum()\n            q_total = len(q_items)\n            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n            q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()\n            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n            # C% among injected items in this quintile\n            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0\n            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0\n            quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n            quintile_data[f'q{q+1}_n_c'] = q_c\n            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj\n            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            c_pct_noninj=c_pct_noninj,\n            n_c_total=n_c_total,\n            n_c_inj=n_c_inj,\n            rho_all=rho_all,\n            rho_inj=rho_inj,\n            rho_noninj=rho_noninj,\n            rho_new=rho_new,\n            pct_focal_favoring=pct_focal_favoring,\n            pct_focal_inj=pct_focal_inj,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            n_newly_c=n_newly_c,\n            n_newly_c_inj=n_newly_c_inj,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ_all={rho_all:.3f}, ρ_inj={rho_inj:.3f}, \"\n              f\"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "74ca25f5-c99d-413d-9db7-789f3449e421",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eio5K9VNcatAA2r2rNNCrF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3661,
      "cache_read_input_tokens": 46961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3661
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

_source line 81 · 2026-05-22T18:54:14.790Z_

<details><summary>↩ Tool result · `toolu_01GKfP5sQZgAGeSc4uLj5Qpa`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "007a05f7-a4a4-495f-b3ce-3c53075dc72d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
    "oldString": "# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running experiments ===\")\nresults = []\nt0 = time.time()\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection models and items (shared across schemes within seed)\n    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)\n    inject_model_mask = np.zeros(N_foc, dtype=bool)\n    inject_model_mask[inject_model_idx] = True\n\n    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)\n\n    # Scheme B: select 5 random subjects, pick injection items from those subjects\n    selected_subjects = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask = np.isin(item_subjects, selected_subjects)\n    subject_item_pool = np.where(subject_mask)[0]\n    n_b_items = min(N_inject_items, len(subject_item_pool))\n    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)\n\n    # Scheme C: split A items in half\n    half = N_inject_items // 2\n    inject_item_idx_c_a = inject_item_idx_all[:half]\n    # For scheme C's B half, pick from 5 random subjects\n    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask_c = np.isin(item_subjects, selected_subjects_c)\n    subject_pool_c = np.where(subject_mask_c)[0]\n    # Exclude items already used by A half\n    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)\n    n_c_b = min(half, len(subject_pool_c))\n    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)\n\n    schemes = {\n        'A_capability': lambda: inject_scheme_a(\n            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),\n        'B_contamination': lambda: inject_scheme_b(\n            X_foc_base, inject_model_mask, inject_item_idx_b, rng),\n        'C_mixed': lambda: inject_scheme_c(\n            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,\n            item_difficulty, rng),\n    }\n\n    for scheme_name, inject_fn in schemes.items():\n        t1 = time.time()\n        rng_state = rng.get_state()\n\n        X_foc_inj, n_flipped = inject_fn()\n\n        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # C% among all items\n        c_pct_all = is_c.sum() / J * 100\n\n        # C% among injected items only\n        inj_arr = np.array(sorted(injected_items))\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n\n        # ρ(difficulty, Δ_MH) among DIF-C items\n        c_idx = np.where(is_c)[0]\n        if len(c_idx) >= 3:\n            rho, rho_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n        else:\n            rho, rho_p = np.nan, np.nan\n\n        # Direction distribution among DIF-C items\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j < 0)).sum()   # negative delta = focal advantage\n        n_ref_favoring = (is_c & (delta_j > 0)).sum()\n        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # For scheme C: per-quintile analysis\n        quintile_data = {}\n        if scheme_name == 'C_mixed':\n            quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n            quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n\n            for q in range(5):\n                q_mask = (quintile_labels == q)\n                q_items = np.where(q_mask)[0]\n                q_c = is_c[q_items].sum()\n                q_total = len(q_items)\n                q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n                q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()\n                q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n                quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n                quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n                quintile_data[f'q{q+1}_n_c'] = q_c\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            n_c_total=n_c_total,\n            rho_diff_delta=rho,\n            rho_p_value=rho_p,\n            pct_focal_favoring=pct_focal_favoring,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ={rho:.3f}, focal%={pct_focal_favoring:.1f}%, \"\n              f\"flips={n_flipped}, {elapsed:.1f}s\")",
    "newString": "# ════════════════════════════════════════════════════════════════════════════\n#  BASELINE (no injection)\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Baseline (no injection) ===\")\ndelta_base, pval_base, is_c_base = mh_dif_vec(X_ref_base, X_foc_base, n_strata=N_STRATA)\nc_idx_base = np.where(is_c_base)[0]\nrho_base, _ = stats.spearmanr(item_difficulty[c_idx_base], delta_base[c_idx_base])\nn_c_base = is_c_base.sum()\nn_focal_base = (is_c_base & (delta_base < 0)).sum()\nprint(f\"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, \"\n      f\"focal%={n_focal_base/n_c_base*100:.1f}%, N_C={n_c_base}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running experiments ===\")\nresults = []\nt0 = time.time()\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection models and items (shared across schemes within seed)\n    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)\n    inject_model_mask = np.zeros(N_foc, dtype=bool)\n    inject_model_mask[inject_model_idx] = True\n\n    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)\n\n    # Scheme B: select 5 random subjects, pick injection items from those subjects\n    selected_subjects = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask = np.isin(item_subjects, selected_subjects)\n    subject_item_pool = np.where(subject_mask)[0]\n    n_b_items = min(N_inject_items, len(subject_item_pool))\n    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)\n\n    # Scheme C: split A items in half\n    half = N_inject_items // 2\n    inject_item_idx_c_a = inject_item_idx_all[:half]\n    # For scheme C's B half, pick from 5 random subjects\n    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask_c = np.isin(item_subjects, selected_subjects_c)\n    subject_pool_c = np.where(subject_mask_c)[0]\n    # Exclude items already used by A half\n    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)\n    n_c_b = min(half, len(subject_pool_c))\n    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)\n\n    schemes = {\n        'A_capability': lambda: inject_scheme_a(\n            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),\n        'B_contamination': lambda: inject_scheme_b(\n            X_foc_base, inject_model_mask, inject_item_idx_b, rng),\n        'C_mixed': lambda: inject_scheme_c(\n            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,\n            item_difficulty, rng),\n    }\n\n    for scheme_name, inject_fn in schemes.items():\n        t1 = time.time()\n\n        X_foc_inj, n_flipped = inject_fn()\n\n        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # C% among all items\n        c_pct_all = is_c.sum() / J * 100\n\n        # C% among injected items only\n        inj_arr = np.array(sorted(injected_items))\n        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100\n\n        # ρ(difficulty, Δ_MH) — all C items, injected-C items, non-injected-C items\n        c_idx = np.where(is_c)[0]\n        if len(c_idx) >= 3:\n            rho_all, rho_all_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n        else:\n            rho_all, rho_all_p = np.nan, np.nan\n\n        c_inj_mask = is_c.copy()\n        c_inj_mask[non_inj_arr] = False\n        c_inj_idx = np.where(c_inj_mask)[0]\n        if len(c_inj_idx) >= 3:\n            rho_inj, rho_inj_p = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])\n        else:\n            rho_inj, rho_inj_p = np.nan, np.nan\n\n        c_noninj_mask = is_c.copy()\n        c_noninj_mask[inj_arr] = False\n        c_noninj_idx = np.where(c_noninj_mask)[0]\n        if len(c_noninj_idx) >= 3:\n            rho_noninj, _ = stats.spearmanr(item_difficulty[c_noninj_idx], delta_j[c_noninj_idx])\n        else:\n            rho_noninj = np.nan\n\n        # Direction distribution among DIF-C items\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j < 0)).sum()\n        n_ref_favoring = (is_c & (delta_j > 0)).sum()\n        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # Direction among injected C items only\n        n_c_inj = c_inj_mask.sum()\n        n_focal_inj = (c_inj_mask & (delta_j < 0)).sum()\n        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0\n\n        # Newly flagged items (C after injection but not in baseline)\n        newly_c = is_c & ~is_c_base\n        n_newly_c = newly_c.sum()\n        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)\n        n_newly_c_inj = newly_c_inj.sum()\n\n        # ρ among newly flagged items\n        newly_idx = np.where(newly_c)[0]\n        if len(newly_idx) >= 3:\n            rho_new, _ = stats.spearmanr(item_difficulty[newly_idx], delta_j[newly_idx])\n        else:\n            rho_new = np.nan\n\n        # Per-quintile analysis (for all schemes, not just C)\n        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n        quintile_data = {}\n        for q in range(5):\n            q_mask = (quintile_labels == q)\n            q_items = np.where(q_mask)[0]\n            q_inj_items = np.intersect1d(q_items, inj_arr)\n            q_c = is_c[q_items].sum()\n            q_total = len(q_items)\n            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n            q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()\n            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n            # C% among injected items in this quintile\n            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0\n            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0\n            quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n            quintile_data[f'q{q+1}_n_c'] = q_c\n            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj\n            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            c_pct_noninj=c_pct_noninj,\n            n_c_total=n_c_total,\n            n_c_inj=n_c_inj,\n            rho_all=rho_all,\n            rho_inj=rho_inj,\n            rho_noninj=rho_noninj,\n            rho_new=rho_new,\n            pct_focal_favoring=pct_focal_favoring,\n            pct_focal_inj=pct_focal_inj,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            n_newly_c=n_newly_c,\n            n_newly_c_inj=n_newly_c_inj,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ_all={rho_all:.3f}, ρ_inj={rho_inj:.3f}, \"\n              f\"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s\")",
    "originalFile": "\"\"\"\nR19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\nTests whether MH-DIF can distinguish capability-like vs contamination-like DIF patterns.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom scipy.stats import chi2 as chi2_dist\nimport time, os, sys\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = os.path.join(ROOT, \"r19_semisynthetic_gradient\")\n\nN_SEEDS = 5\nN_STRATA = 5\nFOC_INJECT_FRAC = 0.30\nITEM_INJECT_FRAC = 0.24\n\n# ════════════════════════════════════════════════════════════════════════════\n#  VECTORIZED MH-DIF — returns per-item results\n# ════════════════════════════════════════════════════════════════════════════\ndef mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item delta_mh, p_value, is_c, direction.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C_mat = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C_mat[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C_mat\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C_mat\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C_mat / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n\n    return delta_j, pval_j, is_c\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  LOAD DATA\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"Loading data...\")\nrm = np.load(f\"{ROOT}/response_matrix.npz\")\nX_sparse = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nidx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\nmodel_names = idx['model_names']\nitem_ids = idx['item_ids']\n\nmeta = pd.read_csv(f\"{ROOT}/model_metadata.csv\")\nname_to_row = {n: i for i, n in enumerate(model_names)}\n\nref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values\nfoc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values\n\nref_idx = np.array([name_to_row[n] for n in ref_models if n in name_to_row])\nfoc_idx = np.array([name_to_row[n] for n in foc_models if n in name_to_row])\n\nN_ref, N_foc, J = len(ref_idx), len(foc_idx), len(item_ids)\nN_inject_models = int(N_foc * FOC_INJECT_FRAC)\nN_inject_items = int(J * ITEM_INJECT_FRAC)\n\nprint(f\"  Ref: {N_ref}, Foc: {N_foc}, Items: {J}\")\nprint(f\"  Injection targets: {N_inject_models} models, {N_inject_items} items\")\n\n# Densify the ref/foc submatrices\nX_ref_base = X_sparse[ref_idx].toarray().astype(np.float64)\nX_foc_base = X_sparse[foc_idx].toarray().astype(np.float64)\n\n# Ref cohort accuracy per item (= item difficulty proxy)\nitem_difficulty = X_ref_base.mean(axis=0)  # shape (J,)\n\nprint(f\"  Item difficulty: mean={item_difficulty.mean():.3f}, \"\n      f\"min={item_difficulty.min():.3f}, max={item_difficulty.max():.3f}\")\n\n# Get MMLU subjects per item for Scheme B (format: subject_name.question_number)\nitem_subjects = np.array([str(iid).rsplit('.', 1)[0] for iid in item_ids])\nunique_subjects = np.unique(item_subjects)\nprint(f\"  Unique subjects: {len(unique_subjects)}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  INJECTION SCHEMES\n# ════════════════════════════════════════════════════════════════════════════\ndef inject_scheme_a(X_foc, inject_model_mask, inject_item_idx, item_diff, rng):\n    \"\"\"Capability-like: injection probability ∝ difficulty (easy items more likely flipped).\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):\n    \"\"\"Contamination-like: uniform injection probability, restricted to 5 random subjects.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,\n                    item_diff, rng, p_const=0.5):\n    \"\"\"Mixed: half items use scheme A, half use scheme B.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    # Scheme A half\n    for j in inject_item_idx_a:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    # Scheme B half\n    for j in inject_item_idx_b:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running experiments ===\")\nresults = []\nt0 = time.time()\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection models and items (shared across schemes within seed)\n    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)\n    inject_model_mask = np.zeros(N_foc, dtype=bool)\n    inject_model_mask[inject_model_idx] = True\n\n    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)\n\n    # Scheme B: select 5 random subjects, pick injection items from those subjects\n    selected_subjects = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask = np.isin(item_subjects, selected_subjects)\n    subject_item_pool = np.where(subject_mask)[0]\n    n_b_items = min(N_inject_items, len(subject_item_pool))\n    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)\n\n    # Scheme C: split A items in half\n    half = N_inject_items // 2\n    inject_item_idx_c_a = inject_item_idx_all[:half]\n    # For scheme C's B half, pick from 5 random subjects\n    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask_c = np.isin(item_subjects, selected_subjects_c)\n    subject_pool_c = np.where(subject_mask_c)[0]\n    # Exclude items already used by A half\n    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)\n    n_c_b = min(half, len(subject_pool_c))\n    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)\n\n    schemes = {\n        'A_capability': lambda: inject_scheme_a(\n            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),\n        'B_contamination': lambda: inject_scheme_b(\n            X_foc_base, inject_model_mask, inject_item_idx_b, rng),\n        'C_mixed': lambda: inject_scheme_c(\n            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,\n            item_difficulty, rng),\n    }\n\n    for scheme_name, inject_fn in schemes.items():\n        t1 = time.time()\n        rng_state = rng.get_state()\n\n        X_foc_inj, n_flipped = inject_fn()\n\n        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # C% among all items\n        c_pct_all = is_c.sum() / J * 100\n\n        # C% among injected items only\n        inj_arr = np.array(sorted(injected_items))\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n\n        # ρ(difficulty, Δ_MH) among DIF-C items\n        c_idx = np.where(is_c)[0]\n        if len(c_idx) >= 3:\n            rho, rho_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n        else:\n            rho, rho_p = np.nan, np.nan\n\n        # Direction distribution among DIF-C items\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j < 0)).sum()   # negative delta = focal advantage\n        n_ref_favoring = (is_c & (delta_j > 0)).sum()\n        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # For scheme C: per-quintile analysis\n        quintile_data = {}\n        if scheme_name == 'C_mixed':\n            quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n            quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n\n            for q in range(5):\n                q_mask = (quintile_labels == q)\n                q_items = np.where(q_mask)[0]\n                q_c = is_c[q_items].sum()\n                q_total = len(q_items)\n                q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n                q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()\n                q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n                quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n                quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n                quintile_data[f'q{q+1}_n_c'] = q_c\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            n_c_total=n_c_total,\n            rho_diff_delta=rho,\n            rho_p_value=rho_p,\n            pct_focal_favoring=pct_focal_favoring,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ={rho:.3f}, focal%={pct_focal_favoring:.1f}%, \"\n              f\"flips={n_flipped}, {elapsed:.1f}s\")\n\ntotal_time = time.time() - t0\nprint(f\"\\nTotal time: {total_time:.0f}s\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  SAVE RESULTS\n# ════════════════════════════════════════════════════════════════════════════\ndf = pd.DataFrame(results)\ndf.to_csv(os.path.join(OUT, \"semisynthetic_results.csv\"), index=False)\nprint(f\"\\nSaved: semisynthetic_results.csv ({len(df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  GENERATE REPORT\n# ════════════════════════════════════════════════════════════════════════════\nreport_lines = [\"# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\\n\"]\nreport_lines.append(f\"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\\n\")\nreport_lines.append(f\"**Config**: {N_SEEDS} seeds, {N_ref} ref models (2023), \"\n                    f\"{N_foc} foc models (2024), {J} items\\n\")\nreport_lines.append(f\"**Injection**: {N_inject_models} foc models ({FOC_INJECT_FRAC*100:.0f}%), \"\n                    f\"~{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\\n\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| ρ(difficulty, Δ_MH) among C | {sub['rho_diff_delta'].mean():.3f} ± {sub['rho_diff_delta'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    if scheme == 'C_mixed':\n        report_lines.append(f\"\\n### Quintile Breakdown (Scheme C)\\n\")\n        report_lines.append(f\"| Quintile | C% | % Focal-Favoring | N DIF-C |\")\n        report_lines.append(f\"|----------|-----|-------------------|---------|\")\n        for q in range(1, 6):\n            col_c = f'q{q}_c_pct'\n            col_f = f'q{q}_pct_focal'\n            col_n = f'q{q}_n_c'\n            if col_c in sub.columns:\n                report_lines.append(\n                    f\"| Q{q} | {sub[col_c].mean():.2f} ± {sub[col_c].std():.2f} | \"\n                    f\"{sub[col_f].mean():.1f} ± {sub[col_f].std():.1f} | \"\n                    f\"{sub[col_n].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **Scheme A** (capability-like): Expects ρ ≈ −0.5 to −0.6 \"\n                    \"(focal-favoring DIF concentrated on easy items)\")\nreport_lines.append(\"- **Scheme B** (contamination-like): Expects ρ ≈ 0 \"\n                    \"(focal-favoring DIF uniform across difficulty)\")\nreport_lines.append(\"- **Scheme C** (mixed): Tests item-level discrimination between the two sources\")\n\nreport_text = \"\\n\".join(report_lines) + \"\\n\"\n\nwith open(os.path.join(OUT, \"semisynthetic_gradient_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"Saved: semisynthetic_gradient_report.md\")\nprint(\"\\n\" + report_text)\n",
    "structuredPatch": [
      {
        "oldStart": 183,
        "oldLines": 6,
        "newStart": 183,
        "newLines": 19,
        "lines": [
          " ",
          " ",
          " # ════════════════════════════════════════════════════════════════════════════",
          "+#  BASELINE (no injection)",
          "+# ════════════════════════════════════════════════════════════════════════════",
          "+print(\"\\n=== Baseline (no injection) ===\")",
          "+delta_base, pval_base, is_c_base = mh_dif_vec(X_ref_base, X_foc_base, n_strata=N_STRATA)",
          "+c_idx_base = np.where(is_c_base)[0]",
          "+rho_base, _ = stats.spearmanr(item_difficulty[c_idx_base], delta_base[c_idx_base])",
          "+n_c_base = is_c_base.sum()",
          "+n_focal_base = (is_c_base & (delta_base < 0)).sum()",
          "+print(f\"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, \"",
          "+      f\"focal%={n_focal_base/n_c_base*100:.1f}%, N_C={n_c_base}\")",
          "+",
          "+",
          "+# ════════════════════════════════════════════════════════════════════════════",
          " #  RUN EXPERIMENTS",
          " # ════════════════════════════════════════════════════════════════════════════",
          " print(\"\\n=== Running experiments ===\")"
        ]
      },
      {
        "oldStart": 230,
        "oldLines": 7,
        "newStart": 243,
        "newLines": 6,
        "lines": [
          " ",
          "     for scheme_name, inject_fn in schemes.items():",
          "         t1 = time.time()",
          "-        rng_state = rng.get_state()",
          " ",
          "         X_foc_inj, n_flipped = inject_fn()",
          " "
        ]
      },
      {
        "oldStart": 250,
        "oldLines": 39,
        "newStart": 262,
        "newLines": 79,
        "lines": [
          " ",
          "         # C% among injected items only",
          "         inj_arr = np.array(sorted(injected_items))",
          "+        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))",
          "         c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0",
          "+        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100",
          " ",
          "-        # ρ(difficulty, Δ_MH) among DIF-C items",
          "+        # ρ(difficulty, Δ_MH) — all C items, injected-C items, non-injected-C items",
          "         c_idx = np.where(is_c)[0]",
          "         if len(c_idx) >= 3:",
          "-            rho, rho_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])",
          "+            rho_all, rho_all_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])",
          "         else:",
          "-            rho, rho_p = np.nan, np.nan",
          "+            rho_all, rho_all_p = np.nan, np.nan",
          " ",
          "+        c_inj_mask = is_c.copy()",
          "+        c_inj_mask[non_inj_arr] = False",
          "+        c_inj_idx = np.where(c_inj_mask)[0]",
          "+        if len(c_inj_idx) >= 3:",
          "+            rho_inj, rho_inj_p = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])",
          "+        else:",
          "+            rho_inj, rho_inj_p = np.nan, np.nan",
          "+",
          "+        c_noninj_mask = is_c.copy()",
          "+        c_noninj_mask[inj_arr] = False",
          "+        c_noninj_idx = np.where(c_noninj_mask)[0]",
          "+        if len(c_noninj_idx) >= 3:",
          "+            rho_noninj, _ = stats.spearmanr(item_difficulty[c_noninj_idx], delta_j[c_noninj_idx])",
          "+        else:",
          "+            rho_noninj = np.nan",
          "+",
          "         # Direction distribution among DIF-C items",
          "         n_c_total = is_c.sum()",
          "-        n_focal_favoring = (is_c & (delta_j < 0)).sum()   # negative delta = focal advantage",
          "+        n_focal_favoring = (is_c & (delta_j < 0)).sum()",
          "         n_ref_favoring = (is_c & (delta_j > 0)).sum()",
          "         pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0",
          " ",
          "-        # For scheme C: per-quintile analysis",
          "-        quintile_data = {}",
          "-        if scheme_name == 'C_mixed':",
          "-            quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])",
          "-            quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])",
          "+        # Direction among injected C items only",
          "+        n_c_inj = c_inj_mask.sum()",
          "+        n_focal_inj = (c_inj_mask & (delta_j < 0)).sum()",
          "+        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0",
          " ",
          "-            for q in range(5):",
          "-                q_mask = (quintile_labels == q)",
          "-                q_items = np.where(q_mask)[0]",
          "-                q_c = is_c[q_items].sum()",
          "-                q_total = len(q_items)",
          "-                q_c_pct = q_c / q_total * 100 if q_total > 0 else 0",
          "-                q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()",
          "-                q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0",
          "-                quintile_data[f'q{q+1}_c_pct'] = q_c_pct",
          "-                quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal",
          "-                quintile_data[f'q{q+1}_n_c'] = q_c",
          "+        # Newly flagged items (C after injection but not in baseline)",
          "+        newly_c = is_c & ~is_c_base",
          "+        n_newly_c = newly_c.sum()",
          "+        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)",
          "+        n_newly_c_inj = newly_c_inj.sum()",
          " ",
          "+        # ρ among newly flagged items",
          "+        newly_idx = np.where(newly_c)[0]",
          "+        if len(newly_idx) >= 3:",
          "+            rho_new, _ = stats.spearmanr(item_difficulty[newly_idx], delta_j[newly_idx])",
          "+        else:",
          "+            rho_new = np.nan",
          "+",
          "+        # Per-quintile analysis (for all schemes, not just C)",
          "+        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])",
          "+        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])",
          "+        quintile_data = {}",
          "+        for q in range(5):",
          "+            q_mask = (quintile_labels == q)",
          "+            q_items = np.where(q_mask)[0]",
          "+            q_inj_items = np.intersect1d(q_items, inj_arr)",
          "+            q_c = is_c[q_items].sum()",
          "+            q_total = len(q_items)",
          "+            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0",
          "+            q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()",
          "+            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0",
          "+            # C% among injected items in this quintile",
          "+            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0",
          "+            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0",
          "+            quintile_data[f'q{q+1}_c_pct'] = q_c_pct",
          "+            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal",
          "+            quintile_data[f'q{q+1}_n_c'] = q_c",
          "+            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj",
          "+            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)",
          "+",
          "         elapsed = time.time() - t1",
          "         row = dict(",
          "             scheme=scheme_name, seed=seed,"
        ]
      },
      {
        "oldStart": 291,
        "oldLines": 19,
        "newStart": 343,
        "newLines": 26,
        "lines": [
          "             n_flipped=n_flipped,",
          "             c_pct_all=c_pct_all,",
          "             c_pct_inj=c_pct_inj,",
          "+            c_pct_noninj=c_pct_noninj,",
          "             n_c_total=n_c_total,",
          "-            rho_diff_delta=rho,",
          "-            rho_p_value=rho_p,",
          "+            n_c_inj=n_c_inj,",
          "+            rho_all=rho_all,",
          "+            rho_inj=rho_inj,",
          "+            rho_noninj=rho_noninj,",
          "+            rho_new=rho_new,",
          "             pct_focal_favoring=pct_focal_favoring,",
          "+            pct_focal_inj=pct_focal_inj,",
          "             n_focal_favoring=n_focal_favoring,",
          "             n_ref_favoring=n_ref_favoring,",
          "+            n_newly_c=n_newly_c,",
          "+            n_newly_c_inj=n_newly_c_inj,",
          "             elapsed_sec=elapsed,",
          "         )",
          "         row.update(quintile_data)",
          "         results.append(row)",
          "         print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"",
          "-              f\"ρ={rho:.3f}, focal%={pct_focal_favoring:.1f}%, \"",
          "-              f\"flips={n_flipped}, {elapsed:.1f}s\")",
          "+              f\"ρ_all={rho_all:.3f}, ρ_inj={rho_inj:.3f}, \"",
          "+              f\"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s\")",
          " ",
          " total_time = time.time() - t0",
          " print(f\"\\nTotal time: {total_time:.0f}s\")"
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

_source line 82_

Now update the report generation section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "d12ac0d6-2120-48d8-8b1c-5ab648dddd91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Uo2rQwbi3wsdGbVYtVC2S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5342,
      "cache_read_input_tokens": 50622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5342
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

_source line 83_

<details open><summary>🔧 Tool call — Read · `toolu_01Uc8SquA8KNcV2bnhBHoTEa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "offset": 290,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "9d03ab8f-deea-42e4-9368-c7498fde1be8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Uo2rQwbi3wsdGbVYtVC2S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5342,
      "cache_read_input_tokens": 50622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5342
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

_source line 84 · 2026-05-22T18:54:17.566Z_

<details><summary>↩ Tool result · `toolu_01Uc8SquA8KNcV2bnhBHoTEa`</summary>

```text
290	            rho_noninj = np.nan
291	
292	        # Direction distribution among DIF-C items
293	        n_c_total = is_c.sum()
294	        n_focal_favoring = (is_c & (delta_j < 0)).sum()
295	        n_ref_favoring = (is_c & (delta_j > 0)).sum()
296	        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0
297	
298	        # Direction among injected C items only
299	        n_c_inj = c_inj_mask.sum()
300	        n_focal_inj = (c_inj_mask & (delta_j < 0)).sum()
301	        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0
302	
303	        # Newly flagged items (C after injection but not in baseline)
304	        newly_c = is_c & ~is_c_base
305	        n_newly_c = newly_c.sum()
306	        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)
307	        n_newly_c_inj = newly_c_inj.sum()
308	
309	        # ρ among newly flagged items
310	        newly_idx = np.where(newly_c)[0]
311	        if len(newly_idx) >= 3:
312	            rho_new, _ = stats.spearmanr(item_difficulty[newly_idx], delta_j[newly_idx])
313	        else:
314	            rho_new = np.nan
315	
316	        # Per-quintile analysis (for all schemes, not just C)
317	        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])
318	        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])
319	        quintile_data = {}
320	        for q in range(5):
321	            q_mask = (quintile_labels == q)
322	            q_items = np.where(q_mask)[0]
323	            q_inj_items = np.intersect1d(q_items, inj_arr)
324	            q_c = is_c[q_items].sum()
325	            q_total = len(q_items)
326	            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0
327	            q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()
328	            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0
329	            # C% among injected items in this quintile
330	            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0
331	            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0
332	            quintile_data[f'q{q+1}_c_pct'] = q_c_pct
333	            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal
334	            quintile_data[f'q{q+1}_n_c'] = q_c
335	            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj
336	            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)
337	
338	        elapsed = time.time() - t1
339	        row = dict(
340	            scheme=scheme_name, seed=seed,
341	            n_inject_models=N_inject_models,
342	            n_inject_items=len(injected_items),
343	            n_flipped=n_flipped,
344	            c_pct_all=c_pct_all,
345	            c_pct_inj=c_pct_inj,
346	            c_pct_noninj=c_pct_noninj,
347	            n_c_total=n_c_total,
348	            n_c_inj=n_c_inj,
349	            rho_all=rho_all,
350	            rho_inj=rho_inj,
351	            rho_noninj=rho_noninj,
352	            rho_new=rho_new,
353	            pct_focal_favoring=pct_focal_favoring,
354	            pct_focal_inj=pct_focal_inj,
355	            n_focal_favoring=n_focal_favoring,
356	            n_ref_favoring=n_ref_favoring,
357	            n_newly_c=n_newly_c,
358	            n_newly_c_inj=n_newly_c_inj,
359	            elapsed_sec=elapsed,
360	        )
361	        row.update(quintile_data)
362	        results.append(row)
363	        print(f"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, "
364	              f"ρ_all={rho_all:.3f}, ρ_inj={rho_inj:.3f}, "
365	              f"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s")
366	
367	total_time = time.time() - t0
368	print(f"\nTotal time: {total_time:.0f}s")
369	
370	
371	# ════════════════════════════════════════════════════════════════════════════
372	#  SAVE RESULTS
373	# ════════════════════════════════════════════════════════════════════════════
374	df = pd.DataFrame(results)
375	df.to_csv(os.path.join(OUT, "semisynthetic_results.csv"), index=False)
376	print(f"\nSaved: semisynthetic_results.csv ({len(df)} rows)")
377	
378	
379	# ════════════════════════════════════════════════════════════════════════════
380	#  GENERATE REPORT
381	# ════════════════════════════════════════════════════════════════════════════
382	report_lines = ["# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\n"]
383	report_lines.append(f"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\n")
384	report_lines.append(f"**Config**: {N_SEEDS} seeds, {N_ref} ref models (2023), "
385	                    f"{N_foc} foc models (2024), {J} items\n")
386	report_lines.append(f"**Injection**: {N_inject_models} foc models ({FOC_INJECT_FRAC*100:.0f}%), "
387	                    f"~{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\n")
388	
389	for scheme in ['A_capability', 'B_contamination', 'C_mixed']:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "f64d55ce-f77a-4367-bf87-c8e3d26c7062",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
      "content": "            rho_noninj = np.nan\n\n        # Direction distribution among DIF-C items\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j < 0)).sum()\n        n_ref_favoring = (is_c & (delta_j > 0)).sum()\n        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # Direction among injected C items only\n        n_c_inj = c_inj_mask.sum()\n        n_focal_inj = (c_inj_mask & (delta_j < 0)).sum()\n        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0\n\n        # Newly flagged items (C after injection but not in baseline)\n        newly_c = is_c & ~is_c_base\n        n_newly_c = newly_c.sum()\n        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)\n        n_newly_c_inj = newly_c_inj.sum()\n\n        # ρ among newly flagged items\n        newly_idx = np.where(newly_c)[0]\n        if len(newly_idx) >= 3:\n            rho_new, _ = stats.spearmanr(item_difficulty[newly_idx], delta_j[newly_idx])\n        else:\n            rho_new = np.nan\n\n        # Per-quintile analysis (for all schemes, not just C)\n        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n        quintile_data = {}\n        for q in range(5):\n            q_mask = (quintile_labels == q)\n            q_items = np.where(q_mask)[0]\n            q_inj_items = np.intersect1d(q_items, inj_arr)\n            q_c = is_c[q_items].sum()\n            q_total = len(q_items)\n            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n            q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()\n            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n            # C% among injected items in this quintile\n            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0\n            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0\n            quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n            quintile_data[f'q{q+1}_n_c'] = q_c\n            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj\n            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            c_pct_noninj=c_pct_noninj,\n            n_c_total=n_c_total,\n            n_c_inj=n_c_inj,\n            rho_all=rho_all,\n            rho_inj=rho_inj,\n            rho_noninj=rho_noninj,\n            rho_new=rho_new,\n            pct_focal_favoring=pct_focal_favoring,\n            pct_focal_inj=pct_focal_inj,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            n_newly_c=n_newly_c,\n            n_newly_c_inj=n_newly_c_inj,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ_all={rho_all:.3f}, ρ_inj={rho_inj:.3f}, \"\n              f\"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s\")\n\ntotal_time = time.time() - t0\nprint(f\"\\nTotal time: {total_time:.0f}s\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  SAVE RESULTS\n# ════════════════════════════════════════════════════════════════════════════\ndf = pd.DataFrame(results)\ndf.to_csv(os.path.join(OUT, \"semisynthetic_results.csv\"), index=False)\nprint(f\"\\nSaved: semisynthetic_results.csv ({len(df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  GENERATE REPORT\n# ════════════════════════════════════════════════════════════════════════════\nreport_lines = [\"# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\\n\"]\nreport_lines.append(f\"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\\n\")\nreport_lines.append(f\"**Config**: {N_SEEDS} seeds, {N_ref} ref models (2023), \"\n                    f\"{N_foc} foc models (2024), {J} items\\n\")\nreport_lines.append(f\"**Injection**: {N_inject_models} foc models ({FOC_INJECT_FRAC*100:.0f}%), \"\n                    f\"~{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\\n\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:",
      "numLines": 100,
      "startLine": 290,
      "totalLines": 431
    }
  }
}
```

</details>

---

### Tool call

_source line 85_

<details open><summary>🔧 Tool call — Read · `toolu_01Xg4M9NiG6L7ypH8x3WsCf4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "offset": 389,
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
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "1b1eb0e9-7564-4427-9efe-f2e7331d40c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Eexdy1kFLfZ85fH9FZwmy5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2152,
      "cache_read_input_tokens": 55964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2152
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

_source line 86 · 2026-05-22T18:54:23.678Z_

<details><summary>↩ Tool result · `toolu_01Xg4M9NiG6L7ypH8x3WsCf4`</summary>

```text
389	for scheme in ['A_capability', 'B_contamination', 'C_mixed']:
390	    sub = df[df['scheme'] == scheme]
391	    report_lines.append(f"\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\n")
392	
393	    report_lines.append(f"| Metric | Mean ± SD |")
394	    report_lines.append(f"|--------|-----------|")
395	    report_lines.append(f"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |")
396	    report_lines.append(f"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |")
397	    report_lines.append(f"| ρ(difficulty, Δ_MH) among C | {sub['rho_diff_delta'].mean():.3f} ± {sub['rho_diff_delta'].std():.3f} |")
398	    report_lines.append(f"| % focal-favoring | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |")
399	    report_lines.append(f"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |")
400	    report_lines.append(f"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |")
401	    report_lines.append(f"| Items injected | {sub['n_inject_items'].mean():.0f} |")
402	
403	    if scheme == 'C_mixed':
404	        report_lines.append(f"\n### Quintile Breakdown (Scheme C)\n")
405	        report_lines.append(f"| Quintile | C% | % Focal-Favoring | N DIF-C |")
406	        report_lines.append(f"|----------|-----|-------------------|---------|")
407	        for q in range(1, 6):
408	            col_c = f'q{q}_c_pct'
409	            col_f = f'q{q}_pct_focal'
410	            col_n = f'q{q}_n_c'
411	            if col_c in sub.columns:
412	                report_lines.append(
413	                    f"| Q{q} | {sub[col_c].mean():.2f} ± {sub[col_c].std():.2f} | "
414	                    f"{sub[col_f].mean():.1f} ± {sub[col_f].std():.1f} | "
415	                    f"{sub[col_n].mean():.0f} |")
416	
417	report_lines.append(f"\n## Interpretation\n")
418	report_lines.append("- **Scheme A** (capability-like): Expects ρ ≈ −0.5 to −0.6 "
419	                    "(focal-favoring DIF concentrated on easy items)")
420	report_lines.append("- **Scheme B** (contamination-like): Expects ρ ≈ 0 "
421	                    "(focal-favoring DIF uniform across difficulty)")
422	report_lines.append("- **Scheme C** (mixed): Tests item-level discrimination between the two sources")
423	
424	report_text = "\n".join(report_lines) + "\n"
425	
426	with open(os.path.join(OUT, "semisynthetic_gradient_report.md"), "w") as f:
427	    f.write(report_text)
428	
429	print(f"Saved: semisynthetic_gradient_report.md")
430	print("\n" + report_text)
431	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "1f098b73-864f-4c70-8d3a-1ead6d53c50a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
      "content": "for scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| ρ(difficulty, Δ_MH) among C | {sub['rho_diff_delta'].mean():.3f} ± {sub['rho_diff_delta'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    if scheme == 'C_mixed':\n        report_lines.append(f\"\\n### Quintile Breakdown (Scheme C)\\n\")\n        report_lines.append(f\"| Quintile | C% | % Focal-Favoring | N DIF-C |\")\n        report_lines.append(f\"|----------|-----|-------------------|---------|\")\n        for q in range(1, 6):\n            col_c = f'q{q}_c_pct'\n            col_f = f'q{q}_pct_focal'\n            col_n = f'q{q}_n_c'\n            if col_c in sub.columns:\n                report_lines.append(\n                    f\"| Q{q} | {sub[col_c].mean():.2f} ± {sub[col_c].std():.2f} | \"\n                    f\"{sub[col_f].mean():.1f} ± {sub[col_f].std():.1f} | \"\n                    f\"{sub[col_n].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **Scheme A** (capability-like): Expects ρ ≈ −0.5 to −0.6 \"\n                    \"(focal-favoring DIF concentrated on easy items)\")\nreport_lines.append(\"- **Scheme B** (contamination-like): Expects ρ ≈ 0 \"\n                    \"(focal-favoring DIF uniform across difficulty)\")\nreport_lines.append(\"- **Scheme C** (mixed): Tests item-level discrimination between the two sources\")\n\nreport_text = \"\\n\".join(report_lines) + \"\\n\"\n\nwith open(os.path.join(OUT, \"semisynthetic_gradient_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"Saved: semisynthetic_gradient_report.md\")\nprint(\"\\n\" + report_text)\n",
      "numLines": 43,
      "startLine": 389,
      "totalLines": 431
    }
  }
}
```

</details>

---

### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Edit · `toolu_0195dMgQAtrJjycrZYKed5De`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "old_string": "for scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| ρ(difficulty, Δ_MH) among C | {sub['rho_diff_delta'].mean():.3f} ± {sub['rho_diff_delta'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    if scheme == 'C_mixed':\n        report_lines.append(f\"\\n### Quintile Breakdown (Scheme C)\\n\")\n        report_lines.append(f\"| Quintile | C% | % Focal-Favoring | N DIF-C |\")\n        report_lines.append(f\"|----------|-----|-------------------|---------|\")\n        for q in range(1, 6):\n            col_c = f'q{q}_c_pct'\n            col_f = f'q{q}_pct_focal'\n            col_n = f'q{q}_n_c'\n            if col_c in sub.columns:\n                report_lines.append(\n                    f\"| Q{q} | {sub[col_c].mean():.2f} ± {sub[col_c].std():.2f} | \"\n                    f\"{sub[col_f].mean():.1f} ± {sub[col_f].std():.1f} | \"\n                    f\"{sub[col_n].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **Scheme A** (capability-like): Expects ρ ≈ −0.5 to −0.6 \"\n                    \"(focal-favoring DIF concentrated on easy items)\")\nreport_lines.append(\"- **Scheme B** (contamination-like): Expects ρ ≈ 0 \"\n                    \"(focal-favoring DIF uniform across difficulty)\")\nreport_lines.append(\"- **Scheme C** (mixed): Tests item-level discrimination between the two sources\")\n\nreport_text = \"\\n\".join(report_lines) + \"\\n\"\n\nwith open(os.path.join(OUT, \"semisynthetic_gradient_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"Saved: semisynthetic_gradient_report.md\")\nprint(\"\\n\" + report_text)",
  "new_string": "report_lines.append(f\"\\n## Baseline (no injection)\\n\")\nreport_lines.append(f\"- C%: {n_c_base/J*100:.2f}%\")\nreport_lines.append(f\"- ρ(difficulty, Δ_MH) among C: {rho_base:.3f}\")\nreport_lines.append(f\"- % focal-favoring: {n_focal_base/n_c_base*100:.1f}%\")\nreport_lines.append(f\"- N DIF-C: {n_c_base}\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| C% (non-injected) | {sub['c_pct_noninj'].mean():.2f} ± {sub['c_pct_noninj'].std():.2f} |\")\n    report_lines.append(f\"| ρ_all (all C items) | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |\")\n    report_lines.append(f\"| **ρ_inj (injected C items)** | **{sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f}** |\")\n    report_lines.append(f\"| ρ_noninj (non-injected C) | {sub['rho_noninj'].mean():.3f} ± {sub['rho_noninj'].std():.3f} |\")\n    report_lines.append(f\"| ρ_new (newly flagged C) | {sub['rho_new'].mean():.3f} ± {sub['rho_new'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring (all) | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")\n    report_lines.append(f\"| % focal-favoring (injected C) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C (from injected) | {sub['n_newly_c_inj'].mean():.0f} ± {sub['n_newly_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    report_lines.append(f\"\\n### Quintile Breakdown\\n\")\n    report_lines.append(f\"| Quintile | C% (all) | C% (injected) | % Focal (all) | N_C | N_inj |\")\n    report_lines.append(f\"|----------|----------|---------------|---------------|-----|-------|\")\n    for q in range(1, 6):\n        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'n_c', 'n_inj']}\n        if cols['c_pct'] in sub.columns:\n            report_lines.append(\n                f\"| Q{q} | {sub[cols['c_pct']].mean():.1f} ± {sub[cols['c_pct']].std():.1f} | \"\n                f\"{sub[cols['c_pct_inj']].mean():.1f} ± {sub[cols['c_pct_inj']].std():.1f} | \"\n                f\"{sub[cols['pct_focal']].mean():.1f} ± {sub[cols['pct_focal']].std():.1f} | \"\n                f\"{sub[cols['n_c']].mean():.0f} | \"\n                f\"{sub[cols['n_inj']].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Key Comparison: ρ_inj across Schemes\\n\")\nreport_lines.append(f\"| Scheme | ρ_inj (mean ± SD) | Expected |\")\nreport_lines.append(f\"|--------|-------------------|----------|\")\nfor scheme, expected in [('A_capability', '≈ −0.5 to −0.6'), ('B_contamination', '≈ 0'), ('C_mixed', 'intermediate')]:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"| {scheme} | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} | {expected} |\")\nreport_lines.append(f\"| Baseline | {rho_base:.3f} | — |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **ρ_inj** is the key metric: ρ computed ONLY among injected items that are DIF-C.\")\nreport_lines.append(\"- **Scheme A** (capability-like): injection ∝ difficulty → focal-favoring DIF on easy items → ρ_inj ≈ −0.5 to −0.6\")\nreport_lines.append(\"- **Scheme B** (contamination-like): uniform p=0.5 injection → DIF uniform across difficulty → ρ_inj ≈ 0\")\nreport_lines.append(\"- **ρ_all** is dominated by ~3900 baseline C items and changes little across schemes.\")\n\nreport_text = \"\\n\".join(report_lines) + \"\\n\"\n\nwith open(os.path.join(OUT, \"semisynthetic_gradient_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"Saved: semisynthetic_gradient_report.md\")\nprint(\"\\n\" + report_text)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "a06e99da-1d0c-4000-b916-dd1a241aa20b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012NA7sewSg5ehkVTEweEfmC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1212,
      "cache_read_input_tokens": 58116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1212
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

_source line 88 · 2026-05-22T18:54:59.789Z_

<details><summary>↩ Tool result · `toolu_0195dMgQAtrJjycrZYKed5De`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "04911926-9e92-4054-8602-864af38b4c5b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
    "oldString": "for scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| ρ(difficulty, Δ_MH) among C | {sub['rho_diff_delta'].mean():.3f} ± {sub['rho_diff_delta'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    if scheme == 'C_mixed':\n        report_lines.append(f\"\\n### Quintile Breakdown (Scheme C)\\n\")\n        report_lines.append(f\"| Quintile | C% | % Focal-Favoring | N DIF-C |\")\n        report_lines.append(f\"|----------|-----|-------------------|---------|\")\n        for q in range(1, 6):\n            col_c = f'q{q}_c_pct'\n            col_f = f'q{q}_pct_focal'\n            col_n = f'q{q}_n_c'\n            if col_c in sub.columns:\n                report_lines.append(\n                    f\"| Q{q} | {sub[col_c].mean():.2f} ± {sub[col_c].std():.2f} | \"\n                    f\"{sub[col_f].mean():.1f} ± {sub[col_f].std():.1f} | \"\n                    f\"{sub[col_n].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **Scheme A** (capability-like): Expects ρ ≈ −0.5 to −0.6 \"\n                    \"(focal-favoring DIF concentrated on easy items)\")\nreport_lines.append(\"- **Scheme B** (contamination-like): Expects ρ ≈ 0 \"\n                    \"(focal-favoring DIF uniform across difficulty)\")\nreport_lines.append(\"- **Scheme C** (mixed): Tests item-level discrimination between the two sources\")\n\nreport_text = \"\\n\".join(report_lines) + \"\\n\"\n\nwith open(os.path.join(OUT, \"semisynthetic_gradient_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"Saved: semisynthetic_gradient_report.md\")\nprint(\"\\n\" + report_text)",
    "newString": "report_lines.append(f\"\\n## Baseline (no injection)\\n\")\nreport_lines.append(f\"- C%: {n_c_base/J*100:.2f}%\")\nreport_lines.append(f\"- ρ(difficulty, Δ_MH) among C: {rho_base:.3f}\")\nreport_lines.append(f\"- % focal-favoring: {n_focal_base/n_c_base*100:.1f}%\")\nreport_lines.append(f\"- N DIF-C: {n_c_base}\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| C% (non-injected) | {sub['c_pct_noninj'].mean():.2f} ± {sub['c_pct_noninj'].std():.2f} |\")\n    report_lines.append(f\"| ρ_all (all C items) | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |\")\n    report_lines.append(f\"| **ρ_inj (injected C items)** | **{sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f}** |\")\n    report_lines.append(f\"| ρ_noninj (non-injected C) | {sub['rho_noninj'].mean():.3f} ± {sub['rho_noninj'].std():.3f} |\")\n    report_lines.append(f\"| ρ_new (newly flagged C) | {sub['rho_new'].mean():.3f} ± {sub['rho_new'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring (all) | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")\n    report_lines.append(f\"| % focal-favoring (injected C) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C (from injected) | {sub['n_newly_c_inj'].mean():.0f} ± {sub['n_newly_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    report_lines.append(f\"\\n### Quintile Breakdown\\n\")\n    report_lines.append(f\"| Quintile | C% (all) | C% (injected) | % Focal (all) | N_C | N_inj |\")\n    report_lines.append(f\"|----------|----------|---------------|---------------|-----|-------|\")\n    for q in range(1, 6):\n        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'n_c', 'n_inj']}\n        if cols['c_pct'] in sub.columns:\n            report_lines.append(\n                f\"| Q{q} | {sub[cols['c_pct']].mean():.1f} ± {sub[cols['c_pct']].std():.1f} | \"\n                f\"{sub[cols['c_pct_inj']].mean():.1f} ± {sub[cols['c_pct_inj']].std():.1f} | \"\n                f\"{sub[cols['pct_focal']].mean():.1f} ± {sub[cols['pct_focal']].std():.1f} | \"\n                f\"{sub[cols['n_c']].mean():.0f} | \"\n                f\"{sub[cols['n_inj']].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Key Comparison: ρ_inj across Schemes\\n\")\nreport_lines.append(f\"| Scheme | ρ_inj (mean ± SD) | Expected |\")\nreport_lines.append(f\"|--------|-------------------|----------|\")\nfor scheme, expected in [('A_capability', '≈ −0.5 to −0.6'), ('B_contamination', '≈ 0'), ('C_mixed', 'intermediate')]:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"| {scheme} | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} | {expected} |\")\nreport_lines.append(f\"| Baseline | {rho_base:.3f} | — |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **ρ_inj** is the key metric: ρ computed ONLY among injected items that are DIF-C.\")\nreport_lines.append(\"- **Scheme A** (capability-like): injection ∝ difficulty → focal-favoring DIF on easy items → ρ_inj ≈ −0.5 to −0.6\")\nreport_lines.append(\"- **Scheme B** (contamination-like): uniform p=0.5 injection → DIF uniform across difficulty → ρ_inj ≈ 0\")\nreport_lines.append(\"- **ρ_all** is dominated by ~3900 baseline C items and changes little across schemes.\")\n\nreport_text = \"\\n\".join(report_lines) + \"\\n\"\n\nwith open(os.path.join(OUT, \"semisynthetic_gradient_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"Saved: semisynthetic_gradient_report.md\")\nprint(\"\\n\" + report_text)",
    "originalFile": "\"\"\"\nR19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\nTests whether MH-DIF can distinguish capability-like vs contamination-like DIF patterns.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom scipy.stats import chi2 as chi2_dist\nimport time, os, sys\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = os.path.join(ROOT, \"r19_semisynthetic_gradient\")\n\nN_SEEDS = 5\nN_STRATA = 5\nFOC_INJECT_FRAC = 0.30\nITEM_INJECT_FRAC = 0.24\n\n# ════════════════════════════════════════════════════════════════════════════\n#  VECTORIZED MH-DIF — returns per-item results\n# ════════════════════════════════════════════════════════════════════════════\ndef mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item delta_mh, p_value, is_c, direction.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C_mat = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C_mat[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C_mat\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C_mat\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C_mat / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n\n    return delta_j, pval_j, is_c\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  LOAD DATA\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"Loading data...\")\nrm = np.load(f\"{ROOT}/response_matrix.npz\")\nX_sparse = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nidx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\nmodel_names = idx['model_names']\nitem_ids = idx['item_ids']\n\nmeta = pd.read_csv(f\"{ROOT}/model_metadata.csv\")\nname_to_row = {n: i for i, n in enumerate(model_names)}\n\nref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values\nfoc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values\n\nref_idx = np.array([name_to_row[n] for n in ref_models if n in name_to_row])\nfoc_idx = np.array([name_to_row[n] for n in foc_models if n in name_to_row])\n\nN_ref, N_foc, J = len(ref_idx), len(foc_idx), len(item_ids)\nN_inject_models = int(N_foc * FOC_INJECT_FRAC)\nN_inject_items = int(J * ITEM_INJECT_FRAC)\n\nprint(f\"  Ref: {N_ref}, Foc: {N_foc}, Items: {J}\")\nprint(f\"  Injection targets: {N_inject_models} models, {N_inject_items} items\")\n\n# Densify the ref/foc submatrices\nX_ref_base = X_sparse[ref_idx].toarray().astype(np.float64)\nX_foc_base = X_sparse[foc_idx].toarray().astype(np.float64)\n\n# Ref cohort accuracy per item (= item difficulty proxy)\nitem_difficulty = X_ref_base.mean(axis=0)  # shape (J,)\n\nprint(f\"  Item difficulty: mean={item_difficulty.mean():.3f}, \"\n      f\"min={item_difficulty.min():.3f}, max={item_difficulty.max():.3f}\")\n\n# Get MMLU subjects per item for Scheme B (format: subject_name.question_number)\nitem_subjects = np.array([str(iid).rsplit('.', 1)[0] for iid in item_ids])\nunique_subjects = np.unique(item_subjects)\nprint(f\"  Unique subjects: {len(unique_subjects)}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  INJECTION SCHEMES\n# ════════════════════════════════════════════════════════════════════════════\ndef inject_scheme_a(X_foc, inject_model_mask, inject_item_idx, item_diff, rng):\n    \"\"\"Capability-like: injection probability ∝ difficulty (easy items more likely flipped).\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):\n    \"\"\"Contamination-like: uniform injection probability, restricted to 5 random subjects.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,\n                    item_diff, rng, p_const=0.5):\n    \"\"\"Mixed: half items use scheme A, half use scheme B.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    # Scheme A half\n    for j in inject_item_idx_a:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    # Scheme B half\n    for j in inject_item_idx_b:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  BASELINE (no injection)\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Baseline (no injection) ===\")\ndelta_base, pval_base, is_c_base = mh_dif_vec(X_ref_base, X_foc_base, n_strata=N_STRATA)\nc_idx_base = np.where(is_c_base)[0]\nrho_base, _ = stats.spearmanr(item_difficulty[c_idx_base], delta_base[c_idx_base])\nn_c_base = is_c_base.sum()\nn_focal_base = (is_c_base & (delta_base < 0)).sum()\nprint(f\"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, \"\n      f\"focal%={n_focal_base/n_c_base*100:.1f}%, N_C={n_c_base}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running experiments ===\")\nresults = []\nt0 = time.time()\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection models and items (shared across schemes within seed)\n    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)\n    inject_model_mask = np.zeros(N_foc, dtype=bool)\n    inject_model_mask[inject_model_idx] = True\n\n    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)\n\n    # Scheme B: select 5 random subjects, pick injection items from those subjects\n    selected_subjects = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask = np.isin(item_subjects, selected_subjects)\n    subject_item_pool = np.where(subject_mask)[0]\n    n_b_items = min(N_inject_items, len(subject_item_pool))\n    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)\n\n    # Scheme C: split A items in half\n    half = N_inject_items // 2\n    inject_item_idx_c_a = inject_item_idx_all[:half]\n    # For scheme C's B half, pick from 5 random subjects\n    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask_c = np.isin(item_subjects, selected_subjects_c)\n    subject_pool_c = np.where(subject_mask_c)[0]\n    # Exclude items already used by A half\n    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)\n    n_c_b = min(half, len(subject_pool_c))\n    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)\n\n    schemes = {\n        'A_capability': lambda: inject_scheme_a(\n            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),\n        'B_contamination': lambda: inject_scheme_b(\n            X_foc_base, inject_model_mask, inject_item_idx_b, rng),\n        'C_mixed': lambda: inject_scheme_c(\n            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,\n            item_difficulty, rng),\n    }\n\n    for scheme_name, inject_fn in schemes.items():\n        t1 = time.time()\n\n        X_foc_inj, n_flipped = inject_fn()\n\n        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # C% among all items\n        c_pct_all = is_c.sum() / J * 100\n\n        # C% among injected items only\n        inj_arr = np.array(sorted(injected_items))\n        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100\n\n        # ρ(difficulty, Δ_MH) — all C items, injected-C items, non-injected-C items\n        c_idx = np.where(is_c)[0]\n        if len(c_idx) >= 3:\n            rho_all, rho_all_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n        else:\n            rho_all, rho_all_p = np.nan, np.nan\n\n        c_inj_mask = is_c.copy()\n        c_inj_mask[non_inj_arr] = False\n        c_inj_idx = np.where(c_inj_mask)[0]\n        if len(c_inj_idx) >= 3:\n            rho_inj, rho_inj_p = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])\n        else:\n            rho_inj, rho_inj_p = np.nan, np.nan\n\n        c_noninj_mask = is_c.copy()\n        c_noninj_mask[inj_arr] = False\n        c_noninj_idx = np.where(c_noninj_mask)[0]\n        if len(c_noninj_idx) >= 3:\n            rho_noninj, _ = stats.spearmanr(item_difficulty[c_noninj_idx], delta_j[c_noninj_idx])\n        else:\n            rho_noninj = np.nan\n\n        # Direction distribution among DIF-C items\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j < 0)).sum()\n        n_ref_favoring = (is_c & (delta_j > 0)).sum()\n        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # Direction among injected C items only\n        n_c_inj = c_inj_mask.sum()\n        n_focal_inj = (c_inj_mask & (delta_j < 0)).sum()\n        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0\n\n        # Newly flagged items (C after injection but not in baseline)\n        newly_c = is_c & ~is_c_base\n        n_newly_c = newly_c.sum()\n        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)\n        n_newly_c_inj = newly_c_inj.sum()\n\n        # ρ among newly flagged items\n        newly_idx = np.where(newly_c)[0]\n        if len(newly_idx) >= 3:\n            rho_new, _ = stats.spearmanr(item_difficulty[newly_idx], delta_j[newly_idx])\n        else:\n            rho_new = np.nan\n\n        # Per-quintile analysis (for all schemes, not just C)\n        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n        quintile_data = {}\n        for q in range(5):\n            q_mask = (quintile_labels == q)\n            q_items = np.where(q_mask)[0]\n            q_inj_items = np.intersect1d(q_items, inj_arr)\n            q_c = is_c[q_items].sum()\n            q_total = len(q_items)\n            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n            q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()\n            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n            # C% among injected items in this quintile\n            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0\n            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0\n            quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n            quintile_data[f'q{q+1}_n_c'] = q_c\n            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj\n            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            c_pct_noninj=c_pct_noninj,\n            n_c_total=n_c_total,\n            n_c_inj=n_c_inj,\n            rho_all=rho_all,\n            rho_inj=rho_inj,\n            rho_noninj=rho_noninj,\n            rho_new=rho_new,\n            pct_focal_favoring=pct_focal_favoring,\n            pct_focal_inj=pct_focal_inj,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            n_newly_c=n_newly_c,\n            n_newly_c_inj=n_newly_c_inj,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ_all={rho_all:.3f}, ρ_inj={rho_inj:.3f}, \"\n              f\"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s\")\n\ntotal_time = time.time() - t0\nprint(f\"\\nTotal time: {total_time:.0f}s\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  SAVE RESULTS\n# ════════════════════════════════════════════════════════════════════════════\ndf = pd.DataFrame(results)\ndf.to_csv(os.path.join(OUT, \"semisynthetic_results.csv\"), index=False)\nprint(f\"\\nSaved: semisynthetic_results.csv ({len(df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  GENERATE REPORT\n# ════════════════════════════════════════════════════════════════════════════\nreport_lines = [\"# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\\n\"]\nreport_lines.append(f\"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\\n\")\nreport_lines.append(f\"**Config**: {N_SEEDS} seeds, {N_ref} ref models (2023), \"\n                    f\"{N_foc} foc models (2024), {J} items\\n\")\nreport_lines.append(f\"**Injection**: {N_inject_models} foc models ({FOC_INJECT_FRAC*100:.0f}%), \"\n                    f\"~{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\\n\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| ρ(difficulty, Δ_MH) among C | {sub['rho_diff_delta'].mean():.3f} ± {sub['rho_diff_delta'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    if scheme == 'C_mixed':\n        report_lines.append(f\"\\n### Quintile Breakdown (Scheme C)\\n\")\n        report_lines.append(f\"| Quintile | C% | % Focal-Favoring | N DIF-C |\")\n        report_lines.append(f\"|----------|-----|-------------------|---------|\")\n        for q in range(1, 6):\n            col_c = f'q{q}_c_pct'\n            col_f = f'q{q}_pct_focal'\n            col_n = f'q{q}_n_c'\n            if col_c in sub.columns:\n                report_lines.append(\n                    f\"| Q{q} | {sub[col_c].mean():.2f} ± {sub[col_c].std():.2f} | \"\n                    f\"{sub[col_f].mean():.1f} ± {sub[col_f].std():.1f} | \"\n                    f\"{sub[col_n].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **Scheme A** (capability-like): Expects ρ ≈ −0.5 to −0.6 \"\n                    \"(focal-favoring DIF concentrated on easy items)\")\nreport_lines.append(\"- **Scheme B** (contamination-like): Expects ρ ≈ 0 \"\n                    \"(focal-favoring DIF uniform across difficulty)\")\nreport_lines.append(\"- **Scheme C** (mixed): Tests item-level discrimination between the two sources\")\n\nreport_text = \"\\n\".join(report_lines) + \"\\n\"\n\nwith open(os.path.join(OUT, \"semisynthetic_gradient_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"Saved: semisynthetic_gradient_report.md\")\nprint(\"\\n\" + report_text)\n",
    "structuredPatch": [
      {
        "oldStart": 386,
        "oldLines": 6,
        "newStart": 386,
        "newLines": 12,
        "lines": [
          " report_lines.append(f\"**Injection**: {N_inject_models} foc models ({FOC_INJECT_FRAC*100:.0f}%), \"",
          "                     f\"~{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\\n\")",
          " ",
          "+report_lines.append(f\"\\n## Baseline (no injection)\\n\")",
          "+report_lines.append(f\"- C%: {n_c_base/J*100:.2f}%\")",
          "+report_lines.append(f\"- ρ(difficulty, Δ_MH) among C: {rho_base:.3f}\")",
          "+report_lines.append(f\"- % focal-favoring: {n_focal_base/n_c_base*100:.1f}%\")",
          "+report_lines.append(f\"- N DIF-C: {n_c_base}\")",
          "+",
          " for scheme in ['A_capability', 'B_contamination', 'C_mixed']:",
          "     sub = df[df['scheme'] == scheme]",
          "     report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")"
        ]
      },
      {
        "oldStart": 394,
        "oldLines": 32,
        "newStart": 400,
        "newLines": 46,
        "lines": [
          "     report_lines.append(f\"|--------|-----------|\")",
          "     report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")",
          "     report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")",
          "-    report_lines.append(f\"| ρ(difficulty, Δ_MH) among C | {sub['rho_diff_delta'].mean():.3f} ± {sub['rho_diff_delta'].std():.3f} |\")",
          "-    report_lines.append(f\"| % focal-favoring | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")",
          "+    report_lines.append(f\"| C% (non-injected) | {sub['c_pct_noninj'].mean():.2f} ± {sub['c_pct_noninj'].std():.2f} |\")",
          "+    report_lines.append(f\"| ρ_all (all C items) | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |\")",
          "+    report_lines.append(f\"| **ρ_inj (injected C items)** | **{sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f}** |\")",
          "+    report_lines.append(f\"| ρ_noninj (non-injected C) | {sub['rho_noninj'].mean():.3f} ± {sub['rho_noninj'].std():.3f} |\")",
          "+    report_lines.append(f\"| ρ_new (newly flagged C) | {sub['rho_new'].mean():.3f} ± {sub['rho_new'].std():.3f} |\")",
          "+    report_lines.append(f\"| % focal-favoring (all) | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")",
          "+    report_lines.append(f\"| % focal-favoring (injected C) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |\")",
          "     report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")",
          "+    report_lines.append(f\"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |\")",
          "+    report_lines.append(f\"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |\")",
          "+    report_lines.append(f\"| Newly flagged C (from injected) | {sub['n_newly_c_inj'].mean():.0f} ± {sub['n_newly_c_inj'].std():.0f} |\")",
          "     report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")",
          "     report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")",
          " ",
          "-    if scheme == 'C_mixed':",
          "-        report_lines.append(f\"\\n### Quintile Breakdown (Scheme C)\\n\")",
          "-        report_lines.append(f\"| Quintile | C% | % Focal-Favoring | N DIF-C |\")",
          "-        report_lines.append(f\"|----------|-----|-------------------|---------|\")",
          "-        for q in range(1, 6):",
          "-            col_c = f'q{q}_c_pct'",
          "-            col_f = f'q{q}_pct_focal'",
          "-            col_n = f'q{q}_n_c'",
          "-            if col_c in sub.columns:",
          "-                report_lines.append(",
          "-                    f\"| Q{q} | {sub[col_c].mean():.2f} ± {sub[col_c].std():.2f} | \"",
          "-                    f\"{sub[col_f].mean():.1f} ± {sub[col_f].std():.1f} | \"",
          "-                    f\"{sub[col_n].mean():.0f} |\")",
          "+    report_lines.append(f\"\\n### Quintile Breakdown\\n\")",
          "+    report_lines.append(f\"| Quintile | C% (all) | C% (injected) | % Focal (all) | N_C | N_inj |\")",
          "+    report_lines.append(f\"|----------|----------|---------------|---------------|-----|-------|\")",
          "+    for q in range(1, 6):",
          "+        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'n_c', 'n_inj']}",
          "+        if cols['c_pct'] in sub.columns:",
          "+            report_lines.append(",
          "+                f\"| Q{q} | {sub[cols['c_pct']].mean():.1f} ± {sub[cols['c_pct']].std():.1f} | \"",
          "+                f\"{sub[cols['c_pct_inj']].mean():.1f} ± {sub[cols['c_pct_inj']].std():.1f} | \"",
          "+                f\"{sub[cols['pct_focal']].mean():.1f} ± {sub[cols['pct_focal']].std():.1f} | \"",
          "+                f\"{sub[cols['n_c']].mean():.0f} | \"",
          "+                f\"{sub[cols['n_inj']].mean():.0f} |\")",
          " ",
          "+report_lines.append(f\"\\n## Key Comparison: ρ_inj across Schemes\\n\")",
          "+report_lines.append(f\"| Scheme | ρ_inj (mean ± SD) | Expected |\")",
          "+report_lines.append(f\"|--------|-------------------|----------|\")",
          "+for scheme, expected in [('A_capability', '≈ −0.5 to −0.6'), ('B_contamination', '≈ 0'), ('C_mixed', 'intermediate')]:",
          "+    sub = df[df['scheme'] == scheme]",
          "+    report_lines.append(f\"| {scheme} | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} | {expected} |\")",
          "+report_lines.append(f\"| Baseline | {rho_base:.3f} | — |\")",
          "+",
          " report_lines.append(f\"\\n## Interpretation\\n\")",
          "-report_lines.append(\"- **Scheme A** (capability-like): Expects ρ ≈ −0.5 to −0.6 \"",
          "-                    \"(focal-favoring DIF concentrated on easy items)\")",
          "-report_lines.append(\"- **Scheme B** (contamination-like): Expects ρ ≈ 0 \"",
          "-                    \"(focal-favoring DIF uniform across difficulty)\")",
          "-report_lines.append(\"- **Scheme C** (mixed): Tests item-level discrimination between the two sources\")",
          "+report_lines.append(\"- **ρ_inj** is the key metric: ρ computed ONLY among injected items that are DIF-C.\")",
          "+report_lines.append(\"- **Scheme A** (capability-like): injection ∝ difficulty → focal-favoring DIF on easy items → ρ_inj ≈ −0.5 to −0.6\")",
          "+report_lines.append(\"- **Scheme B** (contamination-like): uniform p=0.5 injection → DIF uniform across difficulty → ρ_inj ≈ 0\")",
          "+report_lines.append(\"- **ρ_all** is dominated by ~3900 baseline C items and changes little across schemes.\")",
          " ",
          " report_text = \"\\n\".join(report_lines) + \"\\n\"",
          " "
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

_source line 89_

<details open><summary>🔧 Tool call — Bash · `toolu_01Xer2Z65innoJa37MD8dyGg`</summary>

```json
{
  "command": "python3 artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "description": "Run updated experiment with baseline and per-group ρ",
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
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "57b4a156-1356-431c-a8e2-96be82c17f93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019stDq1mecmcTejdY4k6f3g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3127,
      "cache_read_input_tokens": 59328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3127
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

_source line 90_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b17v9dj7u",
  "tool_use_id": "toolu_01Xer2Z65innoJa37MD8dyGg",
  "description": "Run updated experiment with baseline and per-group ρ",
  "task_type": "local_bash",
  "uuid": "dad7f1a6-d1f6-44c1-a3df-0bad8873c690",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### System

_source line 91_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b17v9dj7u",
  "tool_use_id": "toolu_01Xer2Z65innoJa37MD8dyGg",
  "status": "completed",
  "output_file": "",
  "summary": "Run updated experiment with baseline and per-group ρ",
  "uuid": "c41b0056-33e8-4cd0-85e7-3cc01e5fc2e8",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### Tool result

_source line 92 · 2026-05-22T18:55:12.983Z_

<details><summary>↩ Tool result · `toolu_01Xer2Z65innoJa37MD8dyGg`</summary>

```text
Loading data...
  Ref: 1080, Foc: 807, Items: 12508
  Injection targets: 242 models, 3001 items
  Item difficulty: mean=0.581, min=0.008, max=0.956
  Unique subjects: 57

=== Baseline (no injection) ===
  Baseline C%: 31.32%, ρ=-0.587, focal%=56.1%, N_C=3918

=== Running experiments ===
  [A_capability] seed=1: C%=31.5%, ρ_all=-0.496, ρ_inj=-0.185, focal_inj%=12.6%, flips=105196, 0.6s
  [B_contamination] seed=1: C%=32.5%, ρ_all=-0.603, ρ_inj=-0.797, focal_inj%=13.4%, flips=53279, 0.3s
  [C_mixed] seed=1: C%=31.1%, ρ_all=-0.531, ρ_inj=-0.520, focal_inj%=19.6%, flips=104104, 0.6s
  [A_capability] seed=2: C%=31.7%, ρ_all=-0.541, ρ_inj=-0.327, focal_inj%=15.6%, flips=98452, 0.6s
  [B_contamination] seed=2: C%=31.8%, ρ_all=-0.595, ρ_inj=-0.675, focal_inj%=11.7%, flips=39733, 0.3s
  [C_mixed] seed=2: C%=32.0%, ρ_all=-0.566, ρ_inj=-0.521, focal_inj%=18.4%, flips=82803, 0.5s
  [A_capability] seed=3: C%=32.9%, ρ_all=-0.551, ρ_inj=-0.236, focal_inj%=14.5%, flips=103863, 0.6s
  [B_contamination] seed=3: C%=33.2%, ρ_all=-0.623, ρ_inj=-0.708, focal_inj%=10.9%, flips=74372, 0.4s
  [C_mixed] seed=3: C%=31.9%, ρ_all=-0.562, ρ_inj=-0.457, focal_inj%=13.3%, flips=83437, 0.5s
  [A_capability] seed=4: C%=32.1%, ρ_all=-0.531, ρ_inj=-0.211, focal_inj%=14.8%, flips=105362, 0.6s
  [B_contamination] seed=4: C%=31.7%, ρ_all=-0.586, ρ_inj=-0.714, focal_inj%=16.7%, flips=26927, 0.3s
  [C_mixed] seed=4: C%=32.6%, ρ_all=-0.574, ρ_inj=-0.478, focal_inj%=14.7%, flips=114043, 0.5s
  [A_capability] seed=5: C%=31.2%, ρ_all=-0.540, ρ_inj=-0.187, focal_inj%=16.5%, flips=99768, 0.6s
  [B_contamination] seed=5: C%=31.2%, ρ_all=-0.586, ρ_inj=-0.753, focal_inj%=18.9%, flips=34991, 0.3s
  [C_mixed] seed=5: C%=32.2%, ρ_all=-0.572, ρ_inj=-0.504, focal_inj%=15.0%, flips=84375, 0.5s

Total time: 7s

Saved: semisynthetic_results.csv (15 rows)
Saved: semisynthetic_gradient_report.md

# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection

**Date**: 2026-05-22 18:55

**Config**: 5 seeds, 1080 ref models (2023), 807 foc models (2024), 12508 items

**Injection**: 242 foc models (30%), ~3001 items (24%)


## Baseline (no injection)

- C%: 31.32%
- ρ(difficulty, Δ_MH) among C: -0.587
- % focal-favoring: 56.1%
- N DIF-C: 3918

## Scheme A — Capability

| Metric | Mean ± SD |
|--------|-----------|
| C% (all items) | 31.88 ± 0.65 |
| C% (injected items) | 27.33 ± 0.94 |
| C% (non-injected) | 33.32 ± 0.82 |
| ρ_all (all C items) | -0.532 ± 0.021 |
| **ρ_inj (injected C items)** | **-0.229 ± 0.058** |
| ρ_noninj (non-injected C) | -0.573 ± 0.010 |
| ρ_new (newly flagged C) | -0.150 ± 0.142 |
| % focal-favoring (all) | 54.2 ± 1.3 |
| % focal-favoring (injected C) | 14.8 ± 1.5 |
| N DIF-C items | 3988 ± 81 |
| N DIF-C (injected) | 820 ± 28 |
| Newly flagged C | 725 ± 74 |
| Newly flagged C (from injected) | 305 ± 40 |
| Responses flipped | 102528 ± 3208 |
| Items injected | 3001 |

### Quintile Breakdown

| Quintile | C% (all) | C% (injected) | % Focal (all) | N_C | N_inj |
|----------|----------|---------------|---------------|-----|-------|
| Q1 | 34.1 ± 0.5 | 35.4 ± 1.0 | 11.6 ± 1.0 | 853 | 585 |
| Q2 | 38.5 ± 0.3 | 35.9 ± 1.2 | 39.7 ± 1.0 | 961 | 602 |
| Q3 | 32.4 ± 0.6 | 30.0 ± 1.3 | 66.7 ± 1.8 | 811 | 620 |
| Q4 | 31.4 ± 1.4 | 24.5 ± 2.2 | 79.0 ± 2.1 | 777 | 596 |
| Q5 | 23.2 ± 1.5 | 10.9 ± 3.8 | 90.0 ± 4.0 | 587 | 598 |

## Scheme B — Contamination

| Metric | Mean ± SD |
|--------|-----------|
| C% (all items) | 32.07 ± 0.79 |
| C% (injected items) | 39.22 ± 6.34 |
| C% (non-injected) | 31.46 ± 0.23 |
| ρ_all (all C items) | -0.599 ± 0.015 |
| **ρ_inj (injected C items)** | **-0.729 ± 0.047** |
| ρ_noninj (non-injected C) | -0.559 ± 0.010 |
| ρ_new (newly flagged C) | -0.539 ± 0.145 |
| % focal-favoring (all) | 56.4 ± 0.4 |
| % focal-favoring (injected C) | 14.3 ± 3.4 |
| N DIF-C items | 4011 ± 99 |
| N DIF-C (injected) | 351 ± 136 |
| Newly flagged C | 354 ± 150 |
| Newly flagged C (from injected) | 166 ± 85 |
| Responses flipped | 45860 ± 18588 |
| Items injected | 873 |

### Quintile Breakdown

| Quintile | C% (all) | C% (injected) | % Focal (all) | N_C | N_inj |
|----------|----------|---------------|---------------|-----|-------|
| Q1 | 38.2 ± 2.2 | 87.4 ± 1.3 | 9.8 ± 0.5 | 956 | 210 |
| Q2 | 39.9 ± 0.4 | 40.5 ± 3.4 | 40.6 ± 1.2 | 996 | 208 |
| Q3 | 32.8 ± 0.3 | 27.4 ± 2.8 | 74.9 ± 1.1 | 820 | 175 |
| Q4 | 28.8 ± 0.8 | 18.2 ± 4.2 | 88.9 ± 0.6 | 713 | 137 |
| Q5 | 20.8 ± 1.0 | 9.4 ± 1.7 | 97.9 ± 0.4 | 526 | 144 |

## Scheme C — Mixed

| Metric | Mean ± SD |
|--------|-----------|
| C% (all items) | 31.98 ± 0.54 |
| C% (injected items) | 31.28 ± 2.87 |
| C% (non-injected) | 32.18 ± 0.25 |
| ρ_all (all C items) | -0.561 ± 0.017 |
| **ρ_inj (injected C items)** | **-0.496 ± 0.028** |
| ρ_noninj (non-injected C) | -0.560 ± 0.013 |
| ρ_new (newly flagged C) | -0.315 ± 0.076 |
| % focal-favoring (all) | 54.2 ± 1.6 |
| % focal-favoring (injected C) | 16.2 ± 2.7 |
| N DIF-C items | 4000 ± 67 |
| N DIF-C (injected) | 749 ± 99 |
| Newly flagged C | 626 ± 51 |
| Newly flagged C (from injected) | 310 ± 50 |
| Responses flipped | 93752 ± 14432 |
| Items injected | 2407 |

### Quintile Breakdown

| Quintile | C% (all) | C% (injected) | % Focal (all) | N_C | N_inj |
|----------|----------|---------------|---------------|-----|-------|
| Q1 | 37.2 ± 1.3 | 53.8 ± 5.6 | 10.8 ± 0.7 | 931 | 469 |
| Q2 | 39.1 ± 0.6 | 36.4 ± 2.1 | 40.0 ± 1.5 | 978 | 493 |
| Q3 | 32.6 ± 0.4 | 30.1 ± 0.6 | 70.5 ± 1.5 | 815 | 467 |
| Q4 | 29.7 ± 0.3 | 23.6 ± 1.8 | 82.2 ± 2.9 | 735 | 474 |
| Q5 | 21.4 ± 1.2 | 12.5 ± 0.9 | 91.7 ± 2.6 | 542 | 503 |

## Key Comparison: ρ_inj across Schemes

| Scheme | ρ_inj (mean ± SD) | Expected |
|--------|-------------------|----------|
| A_capability | -0.229 ± 0.058 | ≈ −0.5 to −0.6 |
| B_contamination | -0.729 ± 0.047 | ≈ 0 |
| C_mixed | -0.496 ± 0.028 | intermediate |
| Baseline | -0.587 | — |

## Interpretation

- **ρ_inj** is the key metric: ρ computed ONLY among injected items that are DIF-C.
- **Scheme A** (capability-like): injection ∝ difficulty → focal-favoring DIF on easy items → ρ_inj ≈ −0.5 to −0.6
- **Scheme B** (contamination-like): uniform p=0.5 injection → DIF uniform across difficulty → ρ_inj ≈ 0
- **ρ_all** is dominated by ~3900 baseline C items and changes little across schemes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "a232d90c-f9d5-4280-96e9-66d79e0b9eef",
  "tool_use_result": {
    "stdout": "Loading data...\n  Ref: 1080, Foc: 807, Items: 12508\n  Injection targets: 242 models, 3001 items\n  Item difficulty: mean=0.581, min=0.008, max=0.956\n  Unique subjects: 57\n\n=== Baseline (no injection) ===\n  Baseline C%: 31.32%, ρ=-0.587, focal%=56.1%, N_C=3918\n\n=== Running experiments ===\n  [A_capability] seed=1: C%=31.5%, ρ_all=-0.496, ρ_inj=-0.185, focal_inj%=12.6%, flips=105196, 0.6s\n  [B_contamination] seed=1: C%=32.5%, ρ_all=-0.603, ρ_inj=-0.797, focal_inj%=13.4%, flips=53279, 0.3s\n  [C_mixed] seed=1: C%=31.1%, ρ_all=-0.531, ρ_inj=-0.520, focal_inj%=19.6%, flips=104104, 0.6s\n  [A_capability] seed=2: C%=31.7%, ρ_all=-0.541, ρ_inj=-0.327, focal_inj%=15.6%, flips=98452, 0.6s\n  [B_contamination] seed=2: C%=31.8%, ρ_all=-0.595, ρ_inj=-0.675, focal_inj%=11.7%, flips=39733, 0.3s\n  [C_mixed] seed=2: C%=32.0%, ρ_all=-0.566, ρ_inj=-0.521, focal_inj%=18.4%, flips=82803, 0.5s\n  [A_capability] seed=3: C%=32.9%, ρ_all=-0.551, ρ_inj=-0.236, focal_inj%=14.5%, flips=103863, 0.6s\n  [B_contamination] seed=3: C%=33.2%, ρ_all=-0.623, ρ_inj=-0.708, focal_inj%=10.9%, flips=74372, 0.4s\n  [C_mixed] seed=3: C%=31.9%, ρ_all=-0.562, ρ_inj=-0.457, focal_inj%=13.3%, flips=83437, 0.5s\n  [A_capability] seed=4: C%=32.1%, ρ_all=-0.531, ρ_inj=-0.211, focal_inj%=14.8%, flips=105362, 0.6s\n  [B_contamination] seed=4: C%=31.7%, ρ_all=-0.586, ρ_inj=-0.714, focal_inj%=16.7%, flips=26927, 0.3s\n  [C_mixed] seed=4: C%=32.6%, ρ_all=-0.574, ρ_inj=-0.478, focal_inj%=14.7%, flips=114043, 0.5s\n  [A_capability] seed=5: C%=31.2%, ρ_all=-0.540, ρ_inj=-0.187, focal_inj%=16.5%, flips=99768, 0.6s\n  [B_contamination] seed=5: C%=31.2%, ρ_all=-0.586, ρ_inj=-0.753, focal_inj%=18.9%, flips=34991, 0.3s\n  [C_mixed] seed=5: C%=32.2%, ρ_all=-0.572, ρ_inj=-0.504, focal_inj%=15.0%, flips=84375, 0.5s\n\nTotal time: 7s\n\nSaved: semisynthetic_results.csv (15 rows)\nSaved: semisynthetic_gradient_report.md\n\n# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\n\n**Date**: 2026-05-22 18:55\n\n**Config**: 5 seeds, 1080 ref models (2023), 807 foc models (2024), 12508 items\n\n**Injection**: 242 foc models (30%), ~3001 items (24%)\n\n\n## Baseline (no injection)\n\n- C%: 31.32%\n- ρ(difficulty, Δ_MH) among C: -0.587\n- % focal-favoring: 56.1%\n- N DIF-C: 3918\n\n## Scheme A — Capability\n\n| Metric | Mean ± SD |\n|--------|-----------|\n| C% (all items) | 31.88 ± 0.65 |\n| C% (injected items) | 27.33 ± 0.94 |\n| C% (non-injected) | 33.32 ± 0.82 |\n| ρ_all (all C items) | -0.532 ± 0.021 |\n| **ρ_inj (injected C items)** | **-0.229 ± 0.058** |\n| ρ_noninj (non-injected C) | -0.573 ± 0.010 |\n| ρ_new (newly flagged C) | -0.150 ± 0.142 |\n| % focal-favoring (all) | 54.2 ± 1.3 |\n| % focal-favoring (injected C) | 14.8 ± 1.5 |\n| N DIF-C items | 3988 ± 81 |\n| N DIF-C (injected) | 820 ± 28 |\n| Newly flagged C | 725 ± 74 |\n| Newly flagged C (from injected) | 305 ± 40 |\n| Responses flipped | 102528 ± 3208 |\n| Items injected | 3001 |\n\n### Quintile Breakdown\n\n| Quintile | C% (all) | C% (injected) | % Focal (all) | N_C | N_inj |\n|----------|----------|---------------|---------------|-----|-------|\n| Q1 | 34.1 ± 0.5 | 35.4 ± 1.0 | 11.6 ± 1.0 | 853 | 585 |\n| Q2 | 38.5 ± 0.3 | 35.9 ± 1.2 | 39.7 ± 1.0 | 961 | 602 |\n| Q3 | 32.4 ± 0.6 | 30.0 ± 1.3 | 66.7 ± 1.8 | 811 | 620 |\n| Q4 | 31.4 ± 1.4 | 24.5 ± 2.2 | 79.0 ± 2.1 | 777 | 596 |\n| Q5 | 23.2 ± 1.5 | 10.9 ± 3.8 | 90.0 ± 4.0 | 587 | 598 |\n\n## Scheme B — Contamination\n\n| Metric | Mean ± SD |\n|--------|-----------|\n| C% (all items) | 32.07 ± 0.79 |\n| C% (injected items) | 39.22 ± 6.34 |\n| C% (non-injected) | 31.46 ± 0.23 |\n| ρ_all (all C items) | -0.599 ± 0.015 |\n| **ρ_inj (injected C items)** | **-0.729 ± 0.047** |\n| ρ_noninj (non-injected C) | -0.559 ± 0.010 |\n| ρ_new (newly flagged C) | -0.539 ± 0.145 |\n| % focal-favoring (all) | 56.4 ± 0.4 |\n| % focal-favoring (injected C) | 14.3 ± 3.4 |\n| N DIF-C items | 4011 ± 99 |\n| N DIF-C (injected) | 351 ± 136 |\n| Newly flagged C | 354 ± 150 |\n| Newly flagged C (from injected) | 166 ± 85 |\n| Responses flipped | 45860 ± 18588 |\n| Items injected | 873 |\n\n### Quintile Breakdown\n\n| Quintile | C% (all) | C% (injected) | % Focal (all) | N_C | N_inj |\n|----------|----------|---------------|---------------|-----|-------|\n| Q1 | 38.2 ± 2.2 | 87.4 ± 1.3 | 9.8 ± 0.5 | 956 | 210 |\n| Q2 | 39.9 ± 0.4 | 40.5 ± 3.4 | 40.6 ± 1.2 | 996 | 208 |\n| Q3 | 32.8 ± 0.3 | 27.4 ± 2.8 | 74.9 ± 1.1 | 820 | 175 |\n| Q4 | 28.8 ± 0.8 | 18.2 ± 4.2 | 88.9 ± 0.6 | 713 | 137 |\n| Q5 | 20.8 ± 1.0 | 9.4 ± 1.7 | 97.9 ± 0.4 | 526 | 144 |\n\n## Scheme C — Mixed\n\n| Metric | Mean ± SD |\n|--------|-----------|\n| C% (all items) | 31.98 ± 0.54 |\n| C% (injected items) | 31.28 ± 2.87 |\n| C% (non-injected) | 32.18 ± 0.25 |\n| ρ_all (all C items) | -0.561 ± 0.017 |\n| **ρ_inj (injected C items)** | **-0.496 ± 0.028** |\n| ρ_noninj (non-injected C) | -0.560 ± 0.013 |\n| ρ_new (newly flagged C) | -0.315 ± 0.076 |\n| % focal-favoring (all) | 54.2 ± 1.6 |\n| % focal-favoring (injected C) | 16.2 ± 2.7 |\n| N DIF-C items | 4000 ± 67 |\n| N DIF-C (injected) | 749 ± 99 |\n| Newly flagged C | 626 ± 51 |\n| Newly flagged C (from injected) | 310 ± 50 |\n| Responses flipped | 93752 ± 14432 |\n| Items injected | 2407 |\n\n### Quintile Breakdown\n\n| Quintile | C% (all) | C% (injected) | % Focal (all) | N_C | N_inj |\n|----------|----------|---------------|---------------|-----|-------|\n| Q1 | 37.2 ± 1.3 | 53.8 ± 5.6 | 10.8 ± 0.7 | 931 | 469 |\n| Q2 | 39.1 ± 0.6 | 36.4 ± 2.1 | 40.0 ± 1.5 | 978 | 493 |\n| Q3 | 32.6 ± 0.4 | 30.1 ± 0.6 | 70.5 ± 1.5 | 815 | 467 |\n| Q4 | 29.7 ± 0.3 | 23.6 ± 1.8 | 82.2 ± 2.9 | 735 | 474 |\n| Q5 | 21.4 ± 1.2 | 12.5 ± 0.9 | 91.7 ± 2.6 | 542 | 503 |\n\n## Key Comparison: ρ_inj across Schemes\n\n| Scheme | ρ_inj (mean ± SD) | Expected |\n|--------|-------------------|----------|\n| A_capability | -0.229 ± 0.058 | ≈ −0.5 to −0.6 |\n| B_contamination | -0.729 ± 0.047 | ≈ 0 |\n| C_mixed | -0.496 ± 0.028 | intermediate |\n| Baseline | -0.587 | — |\n\n## Interpretation\n\n- **ρ_inj** is the key metric: ρ computed ONLY among injected items that are DIF-C.\n- **Scheme A** (capability-like): injection ∝ difficulty → focal-favoring DIF on easy items → ρ_inj ≈ −0.5 to −0.6\n- **Scheme B** (contamination-like): uniform p=0.5 injection → DIF uniform across difficulty → ρ_inj ≈ 0\n- **ρ_all** is dominated by ~3900 baseline C items and changes little across schemes.",
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

_source line 93_

<details><summary>Logged reasoning block</summary>

```text
Interesting results, but they're counter-intuitive. Let me analyze what's happening:

**Scheme A (capability-like)**: ρ_inj = −0.229 — LESS negative than baseline (−0.587)
**Scheme B (contamination-like)**: ρ_inj = −0.729 — MORE negative than baseline
**Expected**: A should be more negative (−0.5 to −0.6), B should be ~0

The results are opposite to expectations. Let me think about why:

**Scheme A** injects with p ∝ (accuracy - 0.2)/0.6, so easy items (high accuracy) get more flips. 

This creates focal-favoring DIF on easy items, which should make the correlation more negative since easy items have high difficulty. But I'm getting less negative instead of more negative. I need to reconsider the sign convention — negative delta means the focal group has an advantage, and I'm calculating it as −2.35 * log(R / S) where R and S are specific sums from the contingency table.

For Scheme A, I'm flipping 0→1 for focal models on easy items, but since easy items already have high reference cohort accuracy, there's less room for these flips to create visible effects. The injection probability depends on reference accuracy, so on easy items where reference accuracy is already high, the focal models tend to get them right anyway. The flips that do occur happen where reference accuracy is high but focal models still have some incorrect responses, yet these flips have a smaller Mantel-Haenszel effect because the contingency table is already saturated with correct responses. The items that end up showing detectable DIF are the ones where the injection actually had a noticeable impact against that background of high accuracy.

Now I'm reconsidering how the injection affects the composition of DIF-C items. Easy items get more injection because they have higher reference accuracy, making them more likely to become DIF-C with focal-favoring effects (negative delta). Hard items get less injection and fewer DIF-C cases from it. The DIF-C items include both pre-existing cases and newly created ones from injection, and since easy items already had more baseline DIF-C, the additional focal-favoring signal on easy items should drive the correlation toward more negative delta. But the actual result shows ρ_inj = −0.229 for Scheme A, which is less negative than the baseline −0.587, so I need to check what's happening with the focal-favoring percentages.

Looking at the percentages, only 14.8% of injected DIF-C items are focal-favoring for Scheme A, meaning most are actually ref-favoring (positive delta)—the opposite of what I'd expect from the injection mechanism. Let me reconsider the Mantel-Haenszel logic: the injection flips 0→1 for focal models only on injected items, which should make focal models better on those items and create focal-favoring DIF. But only 30% of focal models are injected while 70% remain unchanged, so the overall effect might be diluted or offset by how the reference group responds.

The real issue is that when injected focal models gain points on ~3000 items, their total scores shift substantially, moving them into higher strata where the reference models are genuinely high-ability. Within those strata, the injected focal models have artificial boosts on specific items, but the Mantel-Haenszel stratification by total score is controlling for ability in a way that might be masking or reversing the expected focal-favoring pattern.

Looking at the MH calculation more carefully: when focal models improve on an item after injection, C increases and D decreases within each stratum, which decreases R and increases S, making alpha less than 1. Since delta = -2.35 * log(alpha), a smaller alpha actually produces a positive delta, which would indicate reference-favoring DIF rather than focal-favoring—the opposite of what I'd expect from the injection. I'm working through the sign convention for delta in the Mantel-Haenszel framework—it looks like positive delta indicates focal advantage when using the ETS formulation with the -2.35 * ln(alpha) transformation, but the code comment suggests the opposite convention. Let me trace through the actual computation to see which sign convention is being used in the implementation. I need to verify the sign convention by checking the actual baseline data — if delta < 0 corresponds to ref-favoring, then the 56.1% of items with negative delta aligns with the R18 finding that ref-favoring is dominant, and I should trace through whether easy items (high ref accuracy) tend to have negative or positive delta values. I'm working through the contingency table convention in the code—A is ref correct, B is ref incorrect, C is focal correct, D is focal incorrect. The ratio R/S compares (ref correct × focal incorrect) to (ref incorrect × focal correct), so when the ref group has an advantage, R increases and S decreases, making the log ratio positive and delta negative. This confirms that negative delta indicates ref-favoring performance. I had the sign backwards in my code — I labeled negative delta as focal-favoring when it actually indicates ref-favoring. That flips the interpretation: the baseline's 56.1% with delta < 0 means 56.1% are ref-favoring, and after injecting items where focal models improved, only 14.8% show delta < 0 (ref-favoring) while 85.2% show delta > 0 (focal-favoring), which is exactly what should happen.

Now looking at the correlation among injected items: ρ_inj = −0.229 means easy items (high difficulty values) tend to have smaller positive deltas, suggesting less focal-favoring advantage on easier items — but that contradicts what I'd expect if injection should benefit focal models more on easier problems.

The reason becomes clear when I think through the mechanics: easy items already have high accuracy across both groups, so there are few 0s available to flip when injecting, limiting the marginal gain. Hard items have more 0s to flip but lower injection probability, so few flips actually occur there either. The sweet spot is medium-difficulty items where there's enough room for flips and the injection probability is substantial enough to create a real DIF signal. This is revealing about how the injection mechanism interacts with item difficulty in ways the design didn't fully anticipate.

Now looking at Scheme B with uniform p=0.5 injection across five random subjects, the pattern shifts: hard items accumulate more flips due to having more 0s available, which pushes the delta positive and favors the focal group, whereas easy items still show limited DIF because there's less room for change regardless of uniform injection probability.

But the observed ρ_inj = −0.729 is more negative than baseline, suggesting easy items are actually becoming more reference-favoring rather than staying neutral. I think what's happening is that most of the newly classified DIF-C items were already DIF-C in the baseline—the ~870 injected items with ~46k flips don't fundamentally reclassify the majority. The 166 newly flagged C items represent only a small fraction, so the overall correlation pattern among injected DIF-C items still reflects the original baseline structure where easy items tend toward reference-favoring.

Looking at the newly flagged items specifically, the ρ_new values differ substantially across schemes—Scheme A shows almost no correlation (−0.150), Scheme B shows a moderate negative relationship (−0.539), and Scheme C falls in between (−0.315)—which suggests the injection signal's effect on difficulty-delta correlation depends heavily on which classification scheme is used.

The complication is that newly flagged DIF items include both directly injected and non-injected items affected indirectly through the Mantel-Haenszel stratification, so I need to be more careful about isolating the true injection signal and deciding which metric best captures what the paper should emphasize. I suspect there's also a sign convention issue in my code that's worth checking before drawing final conclusions. The pre-existing DIF items are pulling the correlation toward the baseline pattern, and even newly flagged items show this bias because flips tend to occur on harder items. I suspect the task's expected ρ values assumed injection would be the sole source of DIF, but with real data as the foundation, the baseline pattern interferes. The most practical fix is to compute ρ on the change in delta_MH values rather than the absolute values themselves, which should isolate the injection signal from the baseline noise.

Computing delta changes... dominant. So if the baseline shows ref-favoring dominance with delta < 0, then after injection where focal models improve, delta should shift positive—meaning Δdelta (the change) should be positive for injected items. For Scheme A, this change should correlate with difficulty, giving a positive correlation, while Scheme B should show no correlation. Let me work through the computation to verify this.

Actually, I need to reconsider what the task is asking for. Looking back at the specification, the expected result mentions ρ ≈ −0.5 to −0.6, which mirrors the baseline pattern—easy items showing more focal-favoring DIF. But I'm realizing the task might be asking for ρ(difficulty, delta) directly rather than the change in delta, which would mean easy items have negative delta under Scheme A, matching the baseline's correlation. Since the baseline already shows ρ ≈ −0.59, I need to clarify whether we're measuring the absolute delta or its change after injection.

The key insight is that for Scheme B to achieve ρ ≈ 0, the injected DIF would need to be strong enough to completely reshape the landscape, but with only 5 subjects out of 12508 items, the effect is too small. I think the task specification assumes a cleaner experimental setup than what I've actually implemented—perhaps it's asking me to focus only on the C-flagged items after injection, where the expectation is that A-type injection produces ρ ≈ −0.5 to −0.6 (matching the capability gap pattern) while B-type injection produces ρ ≈ 0.

The real problem is the large number of pre-existing C items drowning out the signal. Looking at plan_011, it uses only 500 baseline items instead of all 12508, which would reduce baseline DIF and let the injection effect stand out more clearly. I should try running the experiment on a smaller random subset of items to make the injected signal more visible.

Alternatively, I could compute the change in delta values (Δdelta) instead, which would capture how the injection shifts the pattern rather than looking at absolute correlations. Let me add that analysis alongside testing on a cleaner subset.

Actually, stepping back—the current results do show meaningful differences between schemes, with ρ values ranging from −0.229 to −0.729. Maybe the issue is that I'm overthinking this. Let me just add the Δdelta analysis and see if that reveals the expected pattern.

For each item, I'll compute delta before and after injection, then look at how the change in delta correlates with difficulty across all items rather than just the DIF-C subset. This should show whether Scheme A produces positive shifts on easy items while Scheme B stays uniform.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "05f389df-845c-4817-aefc-394b1f405ce2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ymkJNUb7yYppQ8Y6Q9YrP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3699,
      "cache_read_input_tokens": 62455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3699
      },
      "output_tokens": 23,
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

_source line 94_

The results reveal important patterns but the sign labeling is wrong and we need a delta-change analysis to isolate injection effects from baseline DIF. Let me fix both issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "948ecadf-1051-45e2-a468-41d1fb52607d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ymkJNUb7yYppQ8Y6Q9YrP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3699,
      "cache_read_input_tokens": 62455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3699
      },
      "output_tokens": 23,
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

_source line 95_

<details open><summary>🔧 Tool call — Read · `toolu_01KUcC4JDuYFvNUbRavSN9Cm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "offset": 185,
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
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "6114630f-3435-4ac2-b9ff-a75583ded159",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ymkJNUb7yYppQ8Y6Q9YrP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3699,
      "cache_read_input_tokens": 62455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3699
      },
      "output_tokens": 23,
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

_source line 96 · 2026-05-22T18:57:33.742Z_

<details><summary>↩ Tool result · `toolu_01KUcC4JDuYFvNUbRavSN9Cm`</summary>

```text
185	# ════════════════════════════════════════════════════════════════════════════
186	#  BASELINE (no injection)
187	# ════════════════════════════════════════════════════════════════════════════
188	print("\n=== Baseline (no injection) ===")
189	delta_base, pval_base, is_c_base = mh_dif_vec(X_ref_base, X_foc_base, n_strata=N_STRATA)
190	c_idx_base = np.where(is_c_base)[0]
191	rho_base, _ = stats.spearmanr(item_difficulty[c_idx_base], delta_base[c_idx_base])
192	n_c_base = is_c_base.sum()
193	n_focal_base = (is_c_base & (delta_base < 0)).sum()
194	print(f"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, "
195	      f"focal%={n_focal_base/n_c_base*100:.1f}%, N_C={n_c_base}")
196	
197	
198	# ════════════════════════════════════════════════════════════════════════════
199	#  RUN EXPERIMENTS
200	# ════════════════════════════════════════════════════════════════════════════
201	print("\n=== Running experiments ===")
202	results = []
203	t0 = time.time()
204	
205	for seed in range(1, N_SEEDS + 1):
206	    rng = np.random.RandomState(seed * 42)
207	
208	    # Select injection models and items (shared across schemes within seed)
209	    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)
210	    inject_model_mask = np.zeros(N_foc, dtype=bool)
211	    inject_model_mask[inject_model_idx] = True
212	
213	    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)
214	
215	    # Scheme B: select 5 random subjects, pick injection items from those subjects
216	    selected_subjects = rng.choice(unique_subjects, 5, replace=False)
217	    subject_mask = np.isin(item_subjects, selected_subjects)
218	    subject_item_pool = np.where(subject_mask)[0]
219	    n_b_items = min(N_inject_items, len(subject_item_pool))
220	    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)
221	
222	    # Scheme C: split A items in half
223	    half = N_inject_items // 2
224	    inject_item_idx_c_a = inject_item_idx_all[:half]
225	    # For scheme C's B half, pick from 5 random subjects
226	    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)
227	    subject_mask_c = np.isin(item_subjects, selected_subjects_c)
228	    subject_pool_c = np.where(subject_mask_c)[0]
229	    # Exclude items already used by A half
230	    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)
231	    n_c_b = min(half, len(subject_pool_c))
232	    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)
233	
234	    schemes = {
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "1a575e45-3430-4840-857a-51bd393f9973",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
      "content": "# ════════════════════════════════════════════════════════════════════════════\n#  BASELINE (no injection)\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Baseline (no injection) ===\")\ndelta_base, pval_base, is_c_base = mh_dif_vec(X_ref_base, X_foc_base, n_strata=N_STRATA)\nc_idx_base = np.where(is_c_base)[0]\nrho_base, _ = stats.spearmanr(item_difficulty[c_idx_base], delta_base[c_idx_base])\nn_c_base = is_c_base.sum()\nn_focal_base = (is_c_base & (delta_base < 0)).sum()\nprint(f\"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, \"\n      f\"focal%={n_focal_base/n_c_base*100:.1f}%, N_C={n_c_base}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running experiments ===\")\nresults = []\nt0 = time.time()\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection models and items (shared across schemes within seed)\n    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)\n    inject_model_mask = np.zeros(N_foc, dtype=bool)\n    inject_model_mask[inject_model_idx] = True\n\n    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)\n\n    # Scheme B: select 5 random subjects, pick injection items from those subjects\n    selected_subjects = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask = np.isin(item_subjects, selected_subjects)\n    subject_item_pool = np.where(subject_mask)[0]\n    n_b_items = min(N_inject_items, len(subject_item_pool))\n    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)\n\n    # Scheme C: split A items in half\n    half = N_inject_items // 2\n    inject_item_idx_c_a = inject_item_idx_all[:half]\n    # For scheme C's B half, pick from 5 random subjects\n    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask_c = np.isin(item_subjects, selected_subjects_c)\n    subject_pool_c = np.where(subject_mask_c)[0]\n    # Exclude items already used by A half\n    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)\n    n_c_b = min(half, len(subject_pool_c))\n    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)\n\n    schemes = {",
      "numLines": 50,
      "startLine": 185,
      "totalLines": 451
    }
  }
}
```

</details>

---

### Tool call

_source line 97_

<details open><summary>🔧 Tool call — Read · `toolu_011Wkvtw139yLbM9dyZKuo9J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "offset": 248,
  "limit": 120
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "9bee10b9-ecf6-4d52-b5cf-f2b4e6499c9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qkp2EKbXnB8zPdQ2NSxmCe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7306,
      "cache_read_input_tokens": 66154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7306
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

_source line 98 · 2026-05-22T18:57:42.808Z_

<details><summary>↩ Tool result · `toolu_011Wkvtw139yLbM9dyZKuo9J`</summary>

```text
248	
249	        # Determine which items were injected for this scheme
250	        if scheme_name == 'A_capability':
251	            injected_items = set(inject_item_idx_all)
252	        elif scheme_name == 'B_contamination':
253	            injected_items = set(inject_item_idx_b)
254	        else:  # C_mixed
255	            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)
256	
257	        # Run MH-DIF
258	        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)
259	
260	        # C% among all items
261	        c_pct_all = is_c.sum() / J * 100
262	
263	        # C% among injected items only
264	        inj_arr = np.array(sorted(injected_items))
265	        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))
266	        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0
267	        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100
268	
269	        # ρ(difficulty, Δ_MH) — all C items, injected-C items, non-injected-C items
270	        c_idx = np.where(is_c)[0]
271	        if len(c_idx) >= 3:
272	            rho_all, rho_all_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])
273	        else:
274	            rho_all, rho_all_p = np.nan, np.nan
275	
276	        c_inj_mask = is_c.copy()
277	        c_inj_mask[non_inj_arr] = False
278	        c_inj_idx = np.where(c_inj_mask)[0]
279	        if len(c_inj_idx) >= 3:
280	            rho_inj, rho_inj_p = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])
281	        else:
282	            rho_inj, rho_inj_p = np.nan, np.nan
283	
284	        c_noninj_mask = is_c.copy()
285	        c_noninj_mask[inj_arr] = False
286	        c_noninj_idx = np.where(c_noninj_mask)[0]
287	        if len(c_noninj_idx) >= 3:
288	            rho_noninj, _ = stats.spearmanr(item_difficulty[c_noninj_idx], delta_j[c_noninj_idx])
289	        else:
290	            rho_noninj = np.nan
291	
292	        # Direction distribution among DIF-C items
293	        n_c_total = is_c.sum()
294	        n_focal_favoring = (is_c & (delta_j < 0)).sum()
295	        n_ref_favoring = (is_c & (delta_j > 0)).sum()
296	        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0
297	
298	        # Direction among injected C items only
299	        n_c_inj = c_inj_mask.sum()
300	        n_focal_inj = (c_inj_mask & (delta_j < 0)).sum()
301	        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0
302	
303	        # Newly flagged items (C after injection but not in baseline)
304	        newly_c = is_c & ~is_c_base
305	        n_newly_c = newly_c.sum()
306	        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)
307	        n_newly_c_inj = newly_c_inj.sum()
308	
309	        # ρ among newly flagged items
310	        newly_idx = np.where(newly_c)[0]
311	        if len(newly_idx) >= 3:
312	            rho_new, _ = stats.spearmanr(item_difficulty[newly_idx], delta_j[newly_idx])
313	        else:
314	            rho_new = np.nan
315	
316	        # Per-quintile analysis (for all schemes, not just C)
317	        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])
318	        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])
319	        quintile_data = {}
320	        for q in range(5):
321	            q_mask = (quintile_labels == q)
322	            q_items = np.where(q_mask)[0]
323	            q_inj_items = np.intersect1d(q_items, inj_arr)
324	            q_c = is_c[q_items].sum()
325	            q_total = len(q_items)
326	            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0
327	            q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()
328	            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0
329	            # C% among injected items in this quintile
330	            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0
331	            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0
332	            quintile_data[f'q{q+1}_c_pct'] = q_c_pct
333	            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal
334	            quintile_data[f'q{q+1}_n_c'] = q_c
335	            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj
336	            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)
337	
338	        elapsed = time.time() - t1
339	        row = dict(
340	            scheme=scheme_name, seed=seed,
341	            n_inject_models=N_inject_models,
342	            n_inject_items=len(injected_items),
343	            n_flipped=n_flipped,
344	            c_pct_all=c_pct_all,
345	            c_pct_inj=c_pct_inj,
346	            c_pct_noninj=c_pct_noninj,
347	            n_c_total=n_c_total,
348	            n_c_inj=n_c_inj,
349	            rho_all=rho_all,
350	            rho_inj=rho_inj,
351	            rho_noninj=rho_noninj,
352	            rho_new=rho_new,
353	            pct_focal_favoring=pct_focal_favoring,
354	            pct_focal_inj=pct_focal_inj,
355	            n_focal_favoring=n_focal_favoring,
356	            n_ref_favoring=n_ref_favoring,
357	            n_newly_c=n_newly_c,
358	            n_newly_c_inj=n_newly_c_inj,
359	            elapsed_sec=elapsed,
360	        )
361	        row.update(quintile_data)
362	        results.append(row)
363	        print(f"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, "
364	              f"ρ_all={rho_all:.3f}, ρ_inj={rho_inj:.3f}, "
365	              f"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s")
366	
367	total_time = time.time() - t0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "372dbb00-e98d-4e73-9c2b-f4611e2f5b41",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
      "content": "\n        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # C% among all items\n        c_pct_all = is_c.sum() / J * 100\n\n        # C% among injected items only\n        inj_arr = np.array(sorted(injected_items))\n        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100\n\n        # ρ(difficulty, Δ_MH) — all C items, injected-C items, non-injected-C items\n        c_idx = np.where(is_c)[0]\n        if len(c_idx) >= 3:\n            rho_all, rho_all_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n        else:\n            rho_all, rho_all_p = np.nan, np.nan\n\n        c_inj_mask = is_c.copy()\n        c_inj_mask[non_inj_arr] = False\n        c_inj_idx = np.where(c_inj_mask)[0]\n        if len(c_inj_idx) >= 3:\n            rho_inj, rho_inj_p = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])\n        else:\n            rho_inj, rho_inj_p = np.nan, np.nan\n\n        c_noninj_mask = is_c.copy()\n        c_noninj_mask[inj_arr] = False\n        c_noninj_idx = np.where(c_noninj_mask)[0]\n        if len(c_noninj_idx) >= 3:\n            rho_noninj, _ = stats.spearmanr(item_difficulty[c_noninj_idx], delta_j[c_noninj_idx])\n        else:\n            rho_noninj = np.nan\n\n        # Direction distribution among DIF-C items\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j < 0)).sum()\n        n_ref_favoring = (is_c & (delta_j > 0)).sum()\n        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # Direction among injected C items only\n        n_c_inj = c_inj_mask.sum()\n        n_focal_inj = (c_inj_mask & (delta_j < 0)).sum()\n        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0\n\n        # Newly flagged items (C after injection but not in baseline)\n        newly_c = is_c & ~is_c_base\n        n_newly_c = newly_c.sum()\n        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)\n        n_newly_c_inj = newly_c_inj.sum()\n\n        # ρ among newly flagged items\n        newly_idx = np.where(newly_c)[0]\n        if len(newly_idx) >= 3:\n            rho_new, _ = stats.spearmanr(item_difficulty[newly_idx], delta_j[newly_idx])\n        else:\n            rho_new = np.nan\n\n        # Per-quintile analysis (for all schemes, not just C)\n        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n        quintile_data = {}\n        for q in range(5):\n            q_mask = (quintile_labels == q)\n            q_items = np.where(q_mask)[0]\n            q_inj_items = np.intersect1d(q_items, inj_arr)\n            q_c = is_c[q_items].sum()\n            q_total = len(q_items)\n            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n            q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()\n            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n            # C% among injected items in this quintile\n            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0\n            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0\n            quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n            quintile_data[f'q{q+1}_n_c'] = q_c\n            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj\n            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            c_pct_noninj=c_pct_noninj,\n            n_c_total=n_c_total,\n            n_c_inj=n_c_inj,\n            rho_all=rho_all,\n            rho_inj=rho_inj,\n            rho_noninj=rho_noninj,\n            rho_new=rho_new,\n            pct_focal_favoring=pct_focal_favoring,\n            pct_focal_inj=pct_focal_inj,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            n_newly_c=n_newly_c,\n            n_newly_c_inj=n_newly_c_inj,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ_all={rho_all:.3f}, ρ_inj={rho_inj:.3f}, \"\n              f\"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s\")\n\ntotal_time = time.time() - t0",
      "numLines": 120,
      "startLine": 248,
      "totalLines": 451
    }
  }
}
```

</details>

---

### Assistant

_source line 99_

I need to fix the direction labels and add delta-change (Δδ) analysis to isolate injection effects. The MH convention here: δ < 0 = ref-favoring, δ > 0 = focal-favoring. Let me rewrite the analysis section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "d48c52f8-2b7d-4242-8868-831f7ed96a01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvUy4cBUAPuHu4KEZa8PU8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2615,
      "cache_read_input_tokens": 73460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2615
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

_source line 100_

<details open><summary>🔧 Tool call — Edit · `toolu_01L7Mq2GhxbguNMjeAsDLTMV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "old_string": "        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # C% among all items\n        c_pct_all = is_c.sum() / J * 100\n\n        # C% among injected items only\n        inj_arr = np.array(sorted(injected_items))\n        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100\n\n        # ρ(difficulty, Δ_MH) — all C items, injected-C items, non-injected-C items\n        c_idx = np.where(is_c)[0]\n        if len(c_idx) >= 3:\n            rho_all, rho_all_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n        else:\n            rho_all, rho_all_p = np.nan, np.nan\n\n        c_inj_mask = is_c.copy()\n        c_inj_mask[non_inj_arr] = False\n        c_inj_idx = np.where(c_inj_mask)[0]\n        if len(c_inj_idx) >= 3:\n            rho_inj, rho_inj_p = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])\n        else:\n            rho_inj, rho_inj_p = np.nan, np.nan\n\n        c_noninj_mask = is_c.copy()\n        c_noninj_mask[inj_arr] = False\n        c_noninj_idx = np.where(c_noninj_mask)[0]\n        if len(c_noninj_idx) >= 3:\n            rho_noninj, _ = stats.spearmanr(item_difficulty[c_noninj_idx], delta_j[c_noninj_idx])\n        else:\n            rho_noninj = np.nan\n\n        # Direction distribution among DIF-C items\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j < 0)).sum()\n        n_ref_favoring = (is_c & (delta_j > 0)).sum()\n        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # Direction among injected C items only\n        n_c_inj = c_inj_mask.sum()\n        n_focal_inj = (c_inj_mask & (delta_j < 0)).sum()\n        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0\n\n        # Newly flagged items (C after injection but not in baseline)\n        newly_c = is_c & ~is_c_base\n        n_newly_c = newly_c.sum()\n        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)\n        n_newly_c_inj = newly_c_inj.sum()\n\n        # ρ among newly flagged items\n        newly_idx = np.where(newly_c)[0]\n        if len(newly_idx) >= 3:\n            rho_new, _ = stats.spearmanr(item_difficulty[newly_idx], delta_j[newly_idx])\n        else:\n            rho_new = np.nan\n\n        # Per-quintile analysis (for all schemes, not just C)\n        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n        quintile_data = {}\n        for q in range(5):\n            q_mask = (quintile_labels == q)\n            q_items = np.where(q_mask)[0]\n            q_inj_items = np.intersect1d(q_items, inj_arr)\n            q_c = is_c[q_items].sum()\n            q_total = len(q_items)\n            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n            q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()\n            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n            # C% among injected items in this quintile\n            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0\n            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0\n            quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n            quintile_data[f'q{q+1}_n_c'] = q_c\n            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj\n            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            c_pct_noninj=c_pct_noninj,\n            n_c_total=n_c_total,\n            n_c_inj=n_c_inj,\n            rho_all=rho_all,\n            rho_inj=rho_inj,\n            rho_noninj=rho_noninj,\n            rho_new=rho_new,\n            pct_focal_favoring=pct_focal_favoring,\n            pct_focal_inj=pct_focal_inj,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            n_newly_c=n_newly_c,\n            n_newly_c_inj=n_newly_c_inj,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ_all={rho_all:.3f}, ρ_inj={rho_inj:.3f}, \"\n              f\"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s\")",
  "new_string": "        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # Delta change from baseline (isolates injection effect)\n        # δ > 0 = focal-favoring; injection flips focal 0→1 → pushes δ positive\n        ddelta = delta_j - delta_base\n\n        # C% among all / injected / non-injected items\n        inj_arr = np.array(sorted(injected_items))\n        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))\n        c_pct_all = is_c.sum() / J * 100\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100\n\n        # ρ(difficulty, δ) among all C items\n        c_idx = np.where(is_c)[0]\n        rho_all = np.nan\n        if len(c_idx) >= 3:\n            rho_all, _ = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n\n        # ρ(difficulty, δ) among injected C items\n        c_inj_mask = is_c & np.isin(np.arange(J), inj_arr)\n        c_inj_idx = np.where(c_inj_mask)[0]\n        rho_inj = np.nan\n        if len(c_inj_idx) >= 3:\n            rho_inj, _ = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])\n\n        # ρ(difficulty, Δδ) among injected items — KEY METRIC isolating injection signal\n        rho_ddelta_inj = np.nan\n        if len(inj_arr) >= 3:\n            rho_ddelta_inj, _ = stats.spearmanr(item_difficulty[inj_arr], ddelta[inj_arr])\n\n        # ρ(difficulty, Δδ) among all items\n        rho_ddelta_all = np.nan\n        if J >= 3:\n            rho_ddelta_all, _ = stats.spearmanr(item_difficulty, ddelta)\n\n        # Direction distribution: δ > 0 = focal-favoring, δ < 0 = ref-favoring\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j > 0)).sum()\n        n_ref_favoring = (is_c & (delta_j < 0)).sum()\n        pct_focal = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # Direction among injected C items\n        n_c_inj = c_inj_mask.sum()\n        n_focal_inj = (c_inj_mask & (delta_j > 0)).sum()\n        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0\n\n        # Newly flagged items (C after injection but not in baseline)\n        newly_c = is_c & ~is_c_base\n        n_newly_c = newly_c.sum()\n        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)\n        n_newly_c_inj = newly_c_inj.sum()\n\n        # Mean Δδ among injected items (injection effect magnitude)\n        mean_ddelta_inj = ddelta[inj_arr].mean()\n\n        # Per-quintile analysis\n        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n        quintile_data = {}\n        for q in range(5):\n            q_mask = (quintile_labels == q)\n            q_items = np.where(q_mask)[0]\n            q_inj_items = np.intersect1d(q_items, inj_arr)\n            q_c = is_c[q_items].sum()\n            q_total = len(q_items)\n            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n            q_focal = (is_c[q_items] & (delta_j[q_items] > 0)).sum()\n            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0\n            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0\n            q_mean_ddelta = ddelta[q_inj_items].mean() if len(q_inj_items) > 0 else 0\n            quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n            quintile_data[f'q{q+1}_n_c'] = q_c\n            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj\n            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)\n            quintile_data[f'q{q+1}_mean_ddelta'] = q_mean_ddelta\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            c_pct_noninj=c_pct_noninj,\n            n_c_total=n_c_total,\n            n_c_inj=n_c_inj,\n            rho_all=rho_all,\n            rho_inj=rho_inj,\n            rho_ddelta_inj=rho_ddelta_inj,\n            rho_ddelta_all=rho_ddelta_all,\n            pct_focal=pct_focal,\n            pct_focal_inj=pct_focal_inj,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            n_newly_c=n_newly_c,\n            n_newly_c_inj=n_newly_c_inj,\n            mean_ddelta_inj=mean_ddelta_inj,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ_all={rho_all:.3f}, ρ_Δδ_inj={rho_ddelta_inj:.3f}, \"\n              f\"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "02cde861-2651-4175-ae52-0b2542953200",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GvUy4cBUAPuHu4KEZa8PU8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2615,
      "cache_read_input_tokens": 73460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2615
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

_source line 101 · 2026-05-22T18:58:33.652Z_

<details><summary>↩ Tool result · `toolu_01L7Mq2GhxbguNMjeAsDLTMV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "64522d26-c4ea-49b9-ae3d-46f01401a3ba",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
    "oldString": "        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # C% among all items\n        c_pct_all = is_c.sum() / J * 100\n\n        # C% among injected items only\n        inj_arr = np.array(sorted(injected_items))\n        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100\n\n        # ρ(difficulty, Δ_MH) — all C items, injected-C items, non-injected-C items\n        c_idx = np.where(is_c)[0]\n        if len(c_idx) >= 3:\n            rho_all, rho_all_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n        else:\n            rho_all, rho_all_p = np.nan, np.nan\n\n        c_inj_mask = is_c.copy()\n        c_inj_mask[non_inj_arr] = False\n        c_inj_idx = np.where(c_inj_mask)[0]\n        if len(c_inj_idx) >= 3:\n            rho_inj, rho_inj_p = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])\n        else:\n            rho_inj, rho_inj_p = np.nan, np.nan\n\n        c_noninj_mask = is_c.copy()\n        c_noninj_mask[inj_arr] = False\n        c_noninj_idx = np.where(c_noninj_mask)[0]\n        if len(c_noninj_idx) >= 3:\n            rho_noninj, _ = stats.spearmanr(item_difficulty[c_noninj_idx], delta_j[c_noninj_idx])\n        else:\n            rho_noninj = np.nan\n\n        # Direction distribution among DIF-C items\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j < 0)).sum()\n        n_ref_favoring = (is_c & (delta_j > 0)).sum()\n        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # Direction among injected C items only\n        n_c_inj = c_inj_mask.sum()\n        n_focal_inj = (c_inj_mask & (delta_j < 0)).sum()\n        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0\n\n        # Newly flagged items (C after injection but not in baseline)\n        newly_c = is_c & ~is_c_base\n        n_newly_c = newly_c.sum()\n        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)\n        n_newly_c_inj = newly_c_inj.sum()\n\n        # ρ among newly flagged items\n        newly_idx = np.where(newly_c)[0]\n        if len(newly_idx) >= 3:\n            rho_new, _ = stats.spearmanr(item_difficulty[newly_idx], delta_j[newly_idx])\n        else:\n            rho_new = np.nan\n\n        # Per-quintile analysis (for all schemes, not just C)\n        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n        quintile_data = {}\n        for q in range(5):\n            q_mask = (quintile_labels == q)\n            q_items = np.where(q_mask)[0]\n            q_inj_items = np.intersect1d(q_items, inj_arr)\n            q_c = is_c[q_items].sum()\n            q_total = len(q_items)\n            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n            q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()\n            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n            # C% among injected items in this quintile\n            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0\n            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0\n            quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n            quintile_data[f'q{q+1}_n_c'] = q_c\n            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj\n            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            c_pct_noninj=c_pct_noninj,\n            n_c_total=n_c_total,\n            n_c_inj=n_c_inj,\n            rho_all=rho_all,\n            rho_inj=rho_inj,\n            rho_noninj=rho_noninj,\n            rho_new=rho_new,\n            pct_focal_favoring=pct_focal_favoring,\n            pct_focal_inj=pct_focal_inj,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            n_newly_c=n_newly_c,\n            n_newly_c_inj=n_newly_c_inj,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ_all={rho_all:.3f}, ρ_inj={rho_inj:.3f}, \"\n              f\"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s\")",
    "newString": "        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # Delta change from baseline (isolates injection effect)\n        # δ > 0 = focal-favoring; injection flips focal 0→1 → pushes δ positive\n        ddelta = delta_j - delta_base\n\n        # C% among all / injected / non-injected items\n        inj_arr = np.array(sorted(injected_items))\n        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))\n        c_pct_all = is_c.sum() / J * 100\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100\n\n        # ρ(difficulty, δ) among all C items\n        c_idx = np.where(is_c)[0]\n        rho_all = np.nan\n        if len(c_idx) >= 3:\n            rho_all, _ = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n\n        # ρ(difficulty, δ) among injected C items\n        c_inj_mask = is_c & np.isin(np.arange(J), inj_arr)\n        c_inj_idx = np.where(c_inj_mask)[0]\n        rho_inj = np.nan\n        if len(c_inj_idx) >= 3:\n            rho_inj, _ = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])\n\n        # ρ(difficulty, Δδ) among injected items — KEY METRIC isolating injection signal\n        rho_ddelta_inj = np.nan\n        if len(inj_arr) >= 3:\n            rho_ddelta_inj, _ = stats.spearmanr(item_difficulty[inj_arr], ddelta[inj_arr])\n\n        # ρ(difficulty, Δδ) among all items\n        rho_ddelta_all = np.nan\n        if J >= 3:\n            rho_ddelta_all, _ = stats.spearmanr(item_difficulty, ddelta)\n\n        # Direction distribution: δ > 0 = focal-favoring, δ < 0 = ref-favoring\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j > 0)).sum()\n        n_ref_favoring = (is_c & (delta_j < 0)).sum()\n        pct_focal = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # Direction among injected C items\n        n_c_inj = c_inj_mask.sum()\n        n_focal_inj = (c_inj_mask & (delta_j > 0)).sum()\n        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0\n\n        # Newly flagged items (C after injection but not in baseline)\n        newly_c = is_c & ~is_c_base\n        n_newly_c = newly_c.sum()\n        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)\n        n_newly_c_inj = newly_c_inj.sum()\n\n        # Mean Δδ among injected items (injection effect magnitude)\n        mean_ddelta_inj = ddelta[inj_arr].mean()\n\n        # Per-quintile analysis\n        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n        quintile_data = {}\n        for q in range(5):\n            q_mask = (quintile_labels == q)\n            q_items = np.where(q_mask)[0]\n            q_inj_items = np.intersect1d(q_items, inj_arr)\n            q_c = is_c[q_items].sum()\n            q_total = len(q_items)\n            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n            q_focal = (is_c[q_items] & (delta_j[q_items] > 0)).sum()\n            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0\n            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0\n            q_mean_ddelta = ddelta[q_inj_items].mean() if len(q_inj_items) > 0 else 0\n            quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n            quintile_data[f'q{q+1}_n_c'] = q_c\n            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj\n            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)\n            quintile_data[f'q{q+1}_mean_ddelta'] = q_mean_ddelta\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            c_pct_noninj=c_pct_noninj,\n            n_c_total=n_c_total,\n            n_c_inj=n_c_inj,\n            rho_all=rho_all,\n            rho_inj=rho_inj,\n            rho_ddelta_inj=rho_ddelta_inj,\n            rho_ddelta_all=rho_ddelta_all,\n            pct_focal=pct_focal,\n            pct_focal_inj=pct_focal_inj,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            n_newly_c=n_newly_c,\n            n_newly_c_inj=n_newly_c_inj,\n            mean_ddelta_inj=mean_ddelta_inj,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ_all={rho_all:.3f}, ρ_Δδ_inj={rho_ddelta_inj:.3f}, \"\n              f\"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s\")",
    "originalFile": "\"\"\"\nR19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\nTests whether MH-DIF can distinguish capability-like vs contamination-like DIF patterns.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom scipy.stats import chi2 as chi2_dist\nimport time, os, sys\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = os.path.join(ROOT, \"r19_semisynthetic_gradient\")\n\nN_SEEDS = 5\nN_STRATA = 5\nFOC_INJECT_FRAC = 0.30\nITEM_INJECT_FRAC = 0.24\n\n# ════════════════════════════════════════════════════════════════════════════\n#  VECTORIZED MH-DIF — returns per-item results\n# ════════════════════════════════════════════════════════════════════════════\ndef mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item delta_mh, p_value, is_c, direction.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C_mat = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C_mat[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C_mat\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C_mat\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C_mat / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n\n    return delta_j, pval_j, is_c\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  LOAD DATA\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"Loading data...\")\nrm = np.load(f\"{ROOT}/response_matrix.npz\")\nX_sparse = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nidx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\nmodel_names = idx['model_names']\nitem_ids = idx['item_ids']\n\nmeta = pd.read_csv(f\"{ROOT}/model_metadata.csv\")\nname_to_row = {n: i for i, n in enumerate(model_names)}\n\nref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values\nfoc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values\n\nref_idx = np.array([name_to_row[n] for n in ref_models if n in name_to_row])\nfoc_idx = np.array([name_to_row[n] for n in foc_models if n in name_to_row])\n\nN_ref, N_foc, J = len(ref_idx), len(foc_idx), len(item_ids)\nN_inject_models = int(N_foc * FOC_INJECT_FRAC)\nN_inject_items = int(J * ITEM_INJECT_FRAC)\n\nprint(f\"  Ref: {N_ref}, Foc: {N_foc}, Items: {J}\")\nprint(f\"  Injection targets: {N_inject_models} models, {N_inject_items} items\")\n\n# Densify the ref/foc submatrices\nX_ref_base = X_sparse[ref_idx].toarray().astype(np.float64)\nX_foc_base = X_sparse[foc_idx].toarray().astype(np.float64)\n\n# Ref cohort accuracy per item (= item difficulty proxy)\nitem_difficulty = X_ref_base.mean(axis=0)  # shape (J,)\n\nprint(f\"  Item difficulty: mean={item_difficulty.mean():.3f}, \"\n      f\"min={item_difficulty.min():.3f}, max={item_difficulty.max():.3f}\")\n\n# Get MMLU subjects per item for Scheme B (format: subject_name.question_number)\nitem_subjects = np.array([str(iid).rsplit('.', 1)[0] for iid in item_ids])\nunique_subjects = np.unique(item_subjects)\nprint(f\"  Unique subjects: {len(unique_subjects)}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  INJECTION SCHEMES\n# ════════════════════════════════════════════════════════════════════════════\ndef inject_scheme_a(X_foc, inject_model_mask, inject_item_idx, item_diff, rng):\n    \"\"\"Capability-like: injection probability ∝ difficulty (easy items more likely flipped).\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):\n    \"\"\"Contamination-like: uniform injection probability, restricted to 5 random subjects.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,\n                    item_diff, rng, p_const=0.5):\n    \"\"\"Mixed: half items use scheme A, half use scheme B.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    # Scheme A half\n    for j in inject_item_idx_a:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    # Scheme B half\n    for j in inject_item_idx_b:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  BASELINE (no injection)\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Baseline (no injection) ===\")\ndelta_base, pval_base, is_c_base = mh_dif_vec(X_ref_base, X_foc_base, n_strata=N_STRATA)\nc_idx_base = np.where(is_c_base)[0]\nrho_base, _ = stats.spearmanr(item_difficulty[c_idx_base], delta_base[c_idx_base])\nn_c_base = is_c_base.sum()\nn_focal_base = (is_c_base & (delta_base < 0)).sum()\nprint(f\"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, \"\n      f\"focal%={n_focal_base/n_c_base*100:.1f}%, N_C={n_c_base}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running experiments ===\")\nresults = []\nt0 = time.time()\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection models and items (shared across schemes within seed)\n    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)\n    inject_model_mask = np.zeros(N_foc, dtype=bool)\n    inject_model_mask[inject_model_idx] = True\n\n    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)\n\n    # Scheme B: select 5 random subjects, pick injection items from those subjects\n    selected_subjects = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask = np.isin(item_subjects, selected_subjects)\n    subject_item_pool = np.where(subject_mask)[0]\n    n_b_items = min(N_inject_items, len(subject_item_pool))\n    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)\n\n    # Scheme C: split A items in half\n    half = N_inject_items // 2\n    inject_item_idx_c_a = inject_item_idx_all[:half]\n    # For scheme C's B half, pick from 5 random subjects\n    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask_c = np.isin(item_subjects, selected_subjects_c)\n    subject_pool_c = np.where(subject_mask_c)[0]\n    # Exclude items already used by A half\n    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)\n    n_c_b = min(half, len(subject_pool_c))\n    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)\n\n    schemes = {\n        'A_capability': lambda: inject_scheme_a(\n            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),\n        'B_contamination': lambda: inject_scheme_b(\n            X_foc_base, inject_model_mask, inject_item_idx_b, rng),\n        'C_mixed': lambda: inject_scheme_c(\n            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,\n            item_difficulty, rng),\n    }\n\n    for scheme_name, inject_fn in schemes.items():\n        t1 = time.time()\n\n        X_foc_inj, n_flipped = inject_fn()\n\n        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # C% among all items\n        c_pct_all = is_c.sum() / J * 100\n\n        # C% among injected items only\n        inj_arr = np.array(sorted(injected_items))\n        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100\n\n        # ρ(difficulty, Δ_MH) — all C items, injected-C items, non-injected-C items\n        c_idx = np.where(is_c)[0]\n        if len(c_idx) >= 3:\n            rho_all, rho_all_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n        else:\n            rho_all, rho_all_p = np.nan, np.nan\n\n        c_inj_mask = is_c.copy()\n        c_inj_mask[non_inj_arr] = False\n        c_inj_idx = np.where(c_inj_mask)[0]\n        if len(c_inj_idx) >= 3:\n            rho_inj, rho_inj_p = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])\n        else:\n            rho_inj, rho_inj_p = np.nan, np.nan\n\n        c_noninj_mask = is_c.copy()\n        c_noninj_mask[inj_arr] = False\n        c_noninj_idx = np.where(c_noninj_mask)[0]\n        if len(c_noninj_idx) >= 3:\n            rho_noninj, _ = stats.spearmanr(item_difficulty[c_noninj_idx], delta_j[c_noninj_idx])\n        else:\n            rho_noninj = np.nan\n\n        # Direction distribution among DIF-C items\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j < 0)).sum()\n        n_ref_favoring = (is_c & (delta_j > 0)).sum()\n        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # Direction among injected C items only\n        n_c_inj = c_inj_mask.sum()\n        n_focal_inj = (c_inj_mask & (delta_j < 0)).sum()\n        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0\n\n        # Newly flagged items (C after injection but not in baseline)\n        newly_c = is_c & ~is_c_base\n        n_newly_c = newly_c.sum()\n        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)\n        n_newly_c_inj = newly_c_inj.sum()\n\n        # ρ among newly flagged items\n        newly_idx = np.where(newly_c)[0]\n        if len(newly_idx) >= 3:\n            rho_new, _ = stats.spearmanr(item_difficulty[newly_idx], delta_j[newly_idx])\n        else:\n            rho_new = np.nan\n\n        # Per-quintile analysis (for all schemes, not just C)\n        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n        quintile_data = {}\n        for q in range(5):\n            q_mask = (quintile_labels == q)\n            q_items = np.where(q_mask)[0]\n            q_inj_items = np.intersect1d(q_items, inj_arr)\n            q_c = is_c[q_items].sum()\n            q_total = len(q_items)\n            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n            q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()\n            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n            # C% among injected items in this quintile\n            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0\n            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0\n            quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n            quintile_data[f'q{q+1}_n_c'] = q_c\n            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj\n            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            c_pct_noninj=c_pct_noninj,\n            n_c_total=n_c_total,\n            n_c_inj=n_c_inj,\n            rho_all=rho_all,\n            rho_inj=rho_inj,\n            rho_noninj=rho_noninj,\n            rho_new=rho_new,\n            pct_focal_favoring=pct_focal_favoring,\n            pct_focal_inj=pct_focal_inj,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            n_newly_c=n_newly_c,\n            n_newly_c_inj=n_newly_c_inj,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ_all={rho_all:.3f}, ρ_inj={rho_inj:.3f}, \"\n              f\"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s\")\n\ntotal_time = time.time() - t0\nprint(f\"\\nTotal time: {total_time:.0f}s\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  SAVE RESULTS\n# ════════════════════════════════════════════════════════════════════════════\ndf = pd.DataFrame(results)\ndf.to_csv(os.path.join(OUT, \"semisynthetic_results.csv\"), index=False)\nprint(f\"\\nSaved: semisynthetic_results.csv ({len(df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  GENERATE REPORT\n# ════════════════════════════════════════════════════════════════════════════\nreport_lines = [\"# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\\n\"]\nreport_lines.append(f\"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\\n\")\nreport_lines.append(f\"**Config**: {N_SEEDS} seeds, {N_ref} ref models (2023), \"\n                    f\"{N_foc} foc models (2024), {J} items\\n\")\nreport_lines.append(f\"**Injection**: {N_inject_models} foc models ({FOC_INJECT_FRAC*100:.0f}%), \"\n                    f\"~{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\\n\")\n\nreport_lines.append(f\"\\n## Baseline (no injection)\\n\")\nreport_lines.append(f\"- C%: {n_c_base/J*100:.2f}%\")\nreport_lines.append(f\"- ρ(difficulty, Δ_MH) among C: {rho_base:.3f}\")\nreport_lines.append(f\"- % focal-favoring: {n_focal_base/n_c_base*100:.1f}%\")\nreport_lines.append(f\"- N DIF-C: {n_c_base}\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| C% (non-injected) | {sub['c_pct_noninj'].mean():.2f} ± {sub['c_pct_noninj'].std():.2f} |\")\n    report_lines.append(f\"| ρ_all (all C items) | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |\")\n    report_lines.append(f\"| **ρ_inj (injected C items)** | **{sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f}** |\")\n    report_lines.append(f\"| ρ_noninj (non-injected C) | {sub['rho_noninj'].mean():.3f} ± {sub['rho_noninj'].std():.3f} |\")\n    report_lines.append(f\"| ρ_new (newly flagged C) | {sub['rho_new'].mean():.3f} ± {sub['rho_new'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring (all) | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")\n    report_lines.append(f\"| % focal-favoring (injected C) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C (from injected) | {sub['n_newly_c_inj'].mean():.0f} ± {sub['n_newly_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    report_lines.append(f\"\\n### Quintile Breakdown\\n\")\n    report_lines.append(f\"| Quintile | C% (all) | C% (injected) | % Focal (all) | N_C | N_inj |\")\n    report_lines.append(f\"|----------|----------|---------------|---------------|-----|-------|\")\n    for q in range(1, 6):\n        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'n_c', 'n_inj']}\n        if cols['c_pct'] in sub.columns:\n            report_lines.append(\n                f\"| Q{q} | {sub[cols['c_pct']].mean():.1f} ± {sub[cols['c_pct']].std():.1f} | \"\n                f\"{sub[cols['c_pct_inj']].mean():.1f} ± {sub[cols['c_pct_inj']].std():.1f} | \"\n                f\"{sub[cols['pct_focal']].mean():.1f} ± {sub[cols['pct_focal']].std():.1f} | \"\n                f\"{sub[cols['n_c']].mean():.0f} | \"\n                f\"{sub[cols['n_inj']].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Key Comparison: ρ_inj across Schemes\\n\")\nreport_lines.append(f\"| Scheme | ρ_inj (mean ± SD) | Expected |\")\nreport_lines.append(f\"|--------|-------------------|----------|\")\nfor scheme, expected in [('A_capability', '≈ −0.5 to −0.6'), ('B_contamination', '≈ 0'), ('C_mixed', 'intermediate')]:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"| {scheme} | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} | {expected} |\")\nreport_lines.append(f\"| Baseline | {rho_base:.3f} | — |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **ρ_inj** is the key metric: ρ computed ONLY among injected items that are DIF-C.\")\nreport_lines.append(\"- **Scheme A** (capability-like): injection ∝ difficulty → focal-favoring DIF on easy items → ρ_inj ≈ −0.5 to −0.6\")\nreport_lines.append(\"- **Scheme B** (contamination-like): uniform p=0.5 injection → DIF uniform across difficulty → ρ_inj ≈ 0\")\nreport_lines.append(\"- **ρ_all** is dominated by ~3900 baseline C items and changes little across schemes.\")\n\nreport_text = \"\\n\".join(report_lines) + \"\\n\"\n\nwith open(os.path.join(OUT, \"semisynthetic_gradient_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"Saved: semisynthetic_gradient_report.md\")\nprint(\"\\n\" + report_text)\n",
    "structuredPatch": [
      {
        "oldStart": 257,
        "oldLines": 47,
        "newStart": 257,
        "newLines": 49,
        "lines": [
          "         # Run MH-DIF",
          "         delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)",
          " ",
          "-        # C% among all items",
          "-        c_pct_all = is_c.sum() / J * 100",
          "+        # Delta change from baseline (isolates injection effect)",
          "+        # δ > 0 = focal-favoring; injection flips focal 0→1 → pushes δ positive",
          "+        ddelta = delta_j - delta_base",
          " ",
          "-        # C% among injected items only",
          "+        # C% among all / injected / non-injected items",
          "         inj_arr = np.array(sorted(injected_items))",
          "         non_inj_arr = np.array(sorted(set(range(J)) - injected_items))",
          "+        c_pct_all = is_c.sum() / J * 100",
          "         c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0",
          "         c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100",
          " ",
          "-        # ρ(difficulty, Δ_MH) — all C items, injected-C items, non-injected-C items",
          "+        # ρ(difficulty, δ) among all C items",
          "         c_idx = np.where(is_c)[0]",
          "+        rho_all = np.nan",
          "         if len(c_idx) >= 3:",
          "-            rho_all, rho_all_p = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])",
          "-        else:",
          "-            rho_all, rho_all_p = np.nan, np.nan",
          "+            rho_all, _ = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])",
          " ",
          "-        c_inj_mask = is_c.copy()",
          "-        c_inj_mask[non_inj_arr] = False",
          "+        # ρ(difficulty, δ) among injected C items",
          "+        c_inj_mask = is_c & np.isin(np.arange(J), inj_arr)",
          "         c_inj_idx = np.where(c_inj_mask)[0]",
          "+        rho_inj = np.nan",
          "         if len(c_inj_idx) >= 3:",
          "-            rho_inj, rho_inj_p = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])",
          "-        else:",
          "-            rho_inj, rho_inj_p = np.nan, np.nan",
          "+            rho_inj, _ = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])",
          " ",
          "-        c_noninj_mask = is_c.copy()",
          "-        c_noninj_mask[inj_arr] = False",
          "-        c_noninj_idx = np.where(c_noninj_mask)[0]",
          "-        if len(c_noninj_idx) >= 3:",
          "-            rho_noninj, _ = stats.spearmanr(item_difficulty[c_noninj_idx], delta_j[c_noninj_idx])",
          "-        else:",
          "-            rho_noninj = np.nan",
          "+        # ρ(difficulty, Δδ) among injected items — KEY METRIC isolating injection signal",
          "+        rho_ddelta_inj = np.nan",
          "+        if len(inj_arr) >= 3:",
          "+            rho_ddelta_inj, _ = stats.spearmanr(item_difficulty[inj_arr], ddelta[inj_arr])",
          " ",
          "-        # Direction distribution among DIF-C items",
          "+        # ρ(difficulty, Δδ) among all items",
          "+        rho_ddelta_all = np.nan",
          "+        if J >= 3:",
          "+            rho_ddelta_all, _ = stats.spearmanr(item_difficulty, ddelta)",
          "+",
          "+        # Direction distribution: δ > 0 = focal-favoring, δ < 0 = ref-favoring",
          "         n_c_total = is_c.sum()",
          "-        n_focal_favoring = (is_c & (delta_j < 0)).sum()",
          "-        n_ref_favoring = (is_c & (delta_j > 0)).sum()",
          "-        pct_focal_favoring = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0",
          "+        n_focal_favoring = (is_c & (delta_j > 0)).sum()",
          "+        n_ref_favoring = (is_c & (delta_j < 0)).sum()",
          "+        pct_focal = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0",
          " ",
          "-        # Direction among injected C items only",
          "+        # Direction among injected C items",
          "         n_c_inj = c_inj_mask.sum()",
          "-        n_focal_inj = (c_inj_mask & (delta_j < 0)).sum()",
          "+        n_focal_inj = (c_inj_mask & (delta_j > 0)).sum()",
          "         pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0",
          " ",
          "         # Newly flagged items (C after injection but not in baseline)"
        ]
      },
      {
        "oldStart": 306,
        "oldLines": 14,
        "newStart": 308,
        "newLines": 10,
        "lines": [
          "         newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)",
          "         n_newly_c_inj = newly_c_inj.sum()",
          " ",
          "-        # ρ among newly flagged items",
          "-        newly_idx = np.where(newly_c)[0]",
          "-        if len(newly_idx) >= 3:",
          "-            rho_new, _ = stats.spearmanr(item_difficulty[newly_idx], delta_j[newly_idx])",
          "-        else:",
          "-            rho_new = np.nan",
          "+        # Mean Δδ among injected items (injection effect magnitude)",
          "+        mean_ddelta_inj = ddelta[inj_arr].mean()",
          " ",
          "-        # Per-quintile analysis (for all schemes, not just C)",
          "+        # Per-quintile analysis",
          "         quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])",
          "         quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])",
          "         quintile_data = {}"
        ]
      },
      {
        "oldStart": 324,
        "oldLines": 16,
        "newStart": 322,
        "newLines": 17,
        "lines": [
          "             q_c = is_c[q_items].sum()",
          "             q_total = len(q_items)",
          "             q_c_pct = q_c / q_total * 100 if q_total > 0 else 0",
          "-            q_focal = (is_c[q_items] & (delta_j[q_items] < 0)).sum()",
          "+            q_focal = (is_c[q_items] & (delta_j[q_items] > 0)).sum()",
          "             q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0",
          "-            # C% among injected items in this quintile",
          "             q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0",
          "             q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0",
          "+            q_mean_ddelta = ddelta[q_inj_items].mean() if len(q_inj_items) > 0 else 0",
          "             quintile_data[f'q{q+1}_c_pct'] = q_c_pct",
          "             quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal",
          "             quintile_data[f'q{q+1}_n_c'] = q_c",
          "             quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj",
          "             quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)",
          "+            quintile_data[f'q{q+1}_mean_ddelta'] = q_mean_ddelta",
          " ",
          "         elapsed = time.time() - t1",
          "         row = dict("
        ]
      },
      {
        "oldStart": 348,
        "oldLines": 20,
        "newStart": 347,
        "newLines": 21,
        "lines": [
          "             n_c_inj=n_c_inj,",
          "             rho_all=rho_all,",
          "             rho_inj=rho_inj,",
          "-            rho_noninj=rho_noninj,",
          "-            rho_new=rho_new,",
          "-            pct_focal_favoring=pct_focal_favoring,",
          "+            rho_ddelta_inj=rho_ddelta_inj,",
          "+            rho_ddelta_all=rho_ddelta_all,",
          "+            pct_focal=pct_focal,",
          "             pct_focal_inj=pct_focal_inj,",
          "             n_focal_favoring=n_focal_favoring,",
          "             n_ref_favoring=n_ref_favoring,",
          "             n_newly_c=n_newly_c,",
          "             n_newly_c_inj=n_newly_c_inj,",
          "+            mean_ddelta_inj=mean_ddelta_inj,",
          "             elapsed_sec=elapsed,",
          "         )",
          "         row.update(quintile_data)",
          "         results.append(row)",
          "         print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"",
          "-              f\"ρ_all={rho_all:.3f}, ρ_inj={rho_inj:.3f}, \"",
          "+              f\"ρ_all={rho_all:.3f}, ρ_Δδ_inj={rho_ddelta_inj:.3f}, \"",
          "               f\"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s\")",
          " ",
          " total_time = time.time() - t0"
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

_source line 102_

Now fix the baseline direction label and report generation:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "58b2d9c5-d27a-4839-97fa-f3e2b86bc56d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1QHKRs2qLW184kQiBnQUG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4553,
      "cache_read_input_tokens": 76075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4553
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

_source line 103_

<details open><summary>🔧 Tool call — Edit · `toolu_01VgoeUMGiMN8QqdWfnSyhxj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "old_string": "n_focal_base = (is_c_base & (delta_base < 0)).sum()\nprint(f\"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, \"\n      f\"focal%={n_focal_base/n_c_base*100:.1f}%, N_C={n_c_base}\")",
  "new_string": "# δ > 0 = focal-favoring, δ < 0 = ref-favoring\nn_focal_base = (is_c_base & (delta_base > 0)).sum()\nn_ref_base = (is_c_base & (delta_base < 0)).sum()\nprint(f\"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, \"\n      f\"focal%={n_focal_base/n_c_base*100:.1f}%, ref%={n_ref_base/n_c_base*100:.1f}%, N_C={n_c_base}\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "5b1f7d11-c020-4ce0-9439-e2c81c10e775",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W1QHKRs2qLW184kQiBnQUG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4553,
      "cache_read_input_tokens": 76075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4553
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

_source line 104 · 2026-05-22T18:58:41.207Z_

<details><summary>↩ Tool result · `toolu_01VgoeUMGiMN8QqdWfnSyhxj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "50e4a3c3-8188-4f7e-9138-aa6b6975906e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
    "oldString": "n_focal_base = (is_c_base & (delta_base < 0)).sum()\nprint(f\"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, \"\n      f\"focal%={n_focal_base/n_c_base*100:.1f}%, N_C={n_c_base}\")",
    "newString": "# δ > 0 = focal-favoring, δ < 0 = ref-favoring\nn_focal_base = (is_c_base & (delta_base > 0)).sum()\nn_ref_base = (is_c_base & (delta_base < 0)).sum()\nprint(f\"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, \"\n      f\"focal%={n_focal_base/n_c_base*100:.1f}%, ref%={n_ref_base/n_c_base*100:.1f}%, N_C={n_c_base}\")",
    "originalFile": "\"\"\"\nR19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\nTests whether MH-DIF can distinguish capability-like vs contamination-like DIF patterns.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom scipy.stats import chi2 as chi2_dist\nimport time, os, sys\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = os.path.join(ROOT, \"r19_semisynthetic_gradient\")\n\nN_SEEDS = 5\nN_STRATA = 5\nFOC_INJECT_FRAC = 0.30\nITEM_INJECT_FRAC = 0.24\n\n# ════════════════════════════════════════════════════════════════════════════\n#  VECTORIZED MH-DIF — returns per-item results\n# ════════════════════════════════════════════════════════════════════════════\ndef mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item delta_mh, p_value, is_c, direction.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C_mat = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C_mat[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C_mat\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C_mat\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C_mat / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n\n    return delta_j, pval_j, is_c\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  LOAD DATA\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"Loading data...\")\nrm = np.load(f\"{ROOT}/response_matrix.npz\")\nX_sparse = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nidx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\nmodel_names = idx['model_names']\nitem_ids = idx['item_ids']\n\nmeta = pd.read_csv(f\"{ROOT}/model_metadata.csv\")\nname_to_row = {n: i for i, n in enumerate(model_names)}\n\nref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values\nfoc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values\n\nref_idx = np.array([name_to_row[n] for n in ref_models if n in name_to_row])\nfoc_idx = np.array([name_to_row[n] for n in foc_models if n in name_to_row])\n\nN_ref, N_foc, J = len(ref_idx), len(foc_idx), len(item_ids)\nN_inject_models = int(N_foc * FOC_INJECT_FRAC)\nN_inject_items = int(J * ITEM_INJECT_FRAC)\n\nprint(f\"  Ref: {N_ref}, Foc: {N_foc}, Items: {J}\")\nprint(f\"  Injection targets: {N_inject_models} models, {N_inject_items} items\")\n\n# Densify the ref/foc submatrices\nX_ref_base = X_sparse[ref_idx].toarray().astype(np.float64)\nX_foc_base = X_sparse[foc_idx].toarray().astype(np.float64)\n\n# Ref cohort accuracy per item (= item difficulty proxy)\nitem_difficulty = X_ref_base.mean(axis=0)  # shape (J,)\n\nprint(f\"  Item difficulty: mean={item_difficulty.mean():.3f}, \"\n      f\"min={item_difficulty.min():.3f}, max={item_difficulty.max():.3f}\")\n\n# Get MMLU subjects per item for Scheme B (format: subject_name.question_number)\nitem_subjects = np.array([str(iid).rsplit('.', 1)[0] for iid in item_ids])\nunique_subjects = np.unique(item_subjects)\nprint(f\"  Unique subjects: {len(unique_subjects)}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  INJECTION SCHEMES\n# ════════════════════════════════════════════════════════════════════════════\ndef inject_scheme_a(X_foc, inject_model_mask, inject_item_idx, item_diff, rng):\n    \"\"\"Capability-like: injection probability ∝ difficulty (easy items more likely flipped).\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):\n    \"\"\"Contamination-like: uniform injection probability, restricted to 5 random subjects.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,\n                    item_diff, rng, p_const=0.5):\n    \"\"\"Mixed: half items use scheme A, half use scheme B.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    # Scheme A half\n    for j in inject_item_idx_a:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    # Scheme B half\n    for j in inject_item_idx_b:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  BASELINE (no injection)\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Baseline (no injection) ===\")\ndelta_base, pval_base, is_c_base = mh_dif_vec(X_ref_base, X_foc_base, n_strata=N_STRATA)\nc_idx_base = np.where(is_c_base)[0]\nrho_base, _ = stats.spearmanr(item_difficulty[c_idx_base], delta_base[c_idx_base])\nn_c_base = is_c_base.sum()\nn_focal_base = (is_c_base & (delta_base < 0)).sum()\nprint(f\"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, \"\n      f\"focal%={n_focal_base/n_c_base*100:.1f}%, N_C={n_c_base}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running experiments ===\")\nresults = []\nt0 = time.time()\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection models and items (shared across schemes within seed)\n    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)\n    inject_model_mask = np.zeros(N_foc, dtype=bool)\n    inject_model_mask[inject_model_idx] = True\n\n    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)\n\n    # Scheme B: select 5 random subjects, pick injection items from those subjects\n    selected_subjects = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask = np.isin(item_subjects, selected_subjects)\n    subject_item_pool = np.where(subject_mask)[0]\n    n_b_items = min(N_inject_items, len(subject_item_pool))\n    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)\n\n    # Scheme C: split A items in half\n    half = N_inject_items // 2\n    inject_item_idx_c_a = inject_item_idx_all[:half]\n    # For scheme C's B half, pick from 5 random subjects\n    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask_c = np.isin(item_subjects, selected_subjects_c)\n    subject_pool_c = np.where(subject_mask_c)[0]\n    # Exclude items already used by A half\n    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)\n    n_c_b = min(half, len(subject_pool_c))\n    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)\n\n    schemes = {\n        'A_capability': lambda: inject_scheme_a(\n            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),\n        'B_contamination': lambda: inject_scheme_b(\n            X_foc_base, inject_model_mask, inject_item_idx_b, rng),\n        'C_mixed': lambda: inject_scheme_c(\n            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,\n            item_difficulty, rng),\n    }\n\n    for scheme_name, inject_fn in schemes.items():\n        t1 = time.time()\n\n        X_foc_inj, n_flipped = inject_fn()\n\n        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # Delta change from baseline (isolates injection effect)\n        # δ > 0 = focal-favoring; injection flips focal 0→1 → pushes δ positive\n        ddelta = delta_j - delta_base\n\n        # C% among all / injected / non-injected items\n        inj_arr = np.array(sorted(injected_items))\n        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))\n        c_pct_all = is_c.sum() / J * 100\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100\n\n        # ρ(difficulty, δ) among all C items\n        c_idx = np.where(is_c)[0]\n        rho_all = np.nan\n        if len(c_idx) >= 3:\n            rho_all, _ = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n\n        # ρ(difficulty, δ) among injected C items\n        c_inj_mask = is_c & np.isin(np.arange(J), inj_arr)\n        c_inj_idx = np.where(c_inj_mask)[0]\n        rho_inj = np.nan\n        if len(c_inj_idx) >= 3:\n            rho_inj, _ = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])\n\n        # ρ(difficulty, Δδ) among injected items — KEY METRIC isolating injection signal\n        rho_ddelta_inj = np.nan\n        if len(inj_arr) >= 3:\n            rho_ddelta_inj, _ = stats.spearmanr(item_difficulty[inj_arr], ddelta[inj_arr])\n\n        # ρ(difficulty, Δδ) among all items\n        rho_ddelta_all = np.nan\n        if J >= 3:\n            rho_ddelta_all, _ = stats.spearmanr(item_difficulty, ddelta)\n\n        # Direction distribution: δ > 0 = focal-favoring, δ < 0 = ref-favoring\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j > 0)).sum()\n        n_ref_favoring = (is_c & (delta_j < 0)).sum()\n        pct_focal = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # Direction among injected C items\n        n_c_inj = c_inj_mask.sum()\n        n_focal_inj = (c_inj_mask & (delta_j > 0)).sum()\n        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0\n\n        # Newly flagged items (C after injection but not in baseline)\n        newly_c = is_c & ~is_c_base\n        n_newly_c = newly_c.sum()\n        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)\n        n_newly_c_inj = newly_c_inj.sum()\n\n        # Mean Δδ among injected items (injection effect magnitude)\n        mean_ddelta_inj = ddelta[inj_arr].mean()\n\n        # Per-quintile analysis\n        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n        quintile_data = {}\n        for q in range(5):\n            q_mask = (quintile_labels == q)\n            q_items = np.where(q_mask)[0]\n            q_inj_items = np.intersect1d(q_items, inj_arr)\n            q_c = is_c[q_items].sum()\n            q_total = len(q_items)\n            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n            q_focal = (is_c[q_items] & (delta_j[q_items] > 0)).sum()\n            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0\n            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0\n            q_mean_ddelta = ddelta[q_inj_items].mean() if len(q_inj_items) > 0 else 0\n            quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n            quintile_data[f'q{q+1}_n_c'] = q_c\n            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj\n            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)\n            quintile_data[f'q{q+1}_mean_ddelta'] = q_mean_ddelta\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            c_pct_noninj=c_pct_noninj,\n            n_c_total=n_c_total,\n            n_c_inj=n_c_inj,\n            rho_all=rho_all,\n            rho_inj=rho_inj,\n            rho_ddelta_inj=rho_ddelta_inj,\n            rho_ddelta_all=rho_ddelta_all,\n            pct_focal=pct_focal,\n            pct_focal_inj=pct_focal_inj,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            n_newly_c=n_newly_c,\n            n_newly_c_inj=n_newly_c_inj,\n            mean_ddelta_inj=mean_ddelta_inj,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ_all={rho_all:.3f}, ρ_Δδ_inj={rho_ddelta_inj:.3f}, \"\n              f\"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s\")\n\ntotal_time = time.time() - t0\nprint(f\"\\nTotal time: {total_time:.0f}s\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  SAVE RESULTS\n# ════════════════════════════════════════════════════════════════════════════\ndf = pd.DataFrame(results)\ndf.to_csv(os.path.join(OUT, \"semisynthetic_results.csv\"), index=False)\nprint(f\"\\nSaved: semisynthetic_results.csv ({len(df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  GENERATE REPORT\n# ════════════════════════════════════════════════════════════════════════════\nreport_lines = [\"# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\\n\"]\nreport_lines.append(f\"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\\n\")\nreport_lines.append(f\"**Config**: {N_SEEDS} seeds, {N_ref} ref models (2023), \"\n                    f\"{N_foc} foc models (2024), {J} items\\n\")\nreport_lines.append(f\"**Injection**: {N_inject_models} foc models ({FOC_INJECT_FRAC*100:.0f}%), \"\n                    f\"~{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\\n\")\n\nreport_lines.append(f\"\\n## Baseline (no injection)\\n\")\nreport_lines.append(f\"- C%: {n_c_base/J*100:.2f}%\")\nreport_lines.append(f\"- ρ(difficulty, Δ_MH) among C: {rho_base:.3f}\")\nreport_lines.append(f\"- % focal-favoring: {n_focal_base/n_c_base*100:.1f}%\")\nreport_lines.append(f\"- N DIF-C: {n_c_base}\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| C% (non-injected) | {sub['c_pct_noninj'].mean():.2f} ± {sub['c_pct_noninj'].std():.2f} |\")\n    report_lines.append(f\"| ρ_all (all C items) | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |\")\n    report_lines.append(f\"| **ρ_inj (injected C items)** | **{sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f}** |\")\n    report_lines.append(f\"| ρ_noninj (non-injected C) | {sub['rho_noninj'].mean():.3f} ± {sub['rho_noninj'].std():.3f} |\")\n    report_lines.append(f\"| ρ_new (newly flagged C) | {sub['rho_new'].mean():.3f} ± {sub['rho_new'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring (all) | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")\n    report_lines.append(f\"| % focal-favoring (injected C) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C (from injected) | {sub['n_newly_c_inj'].mean():.0f} ± {sub['n_newly_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    report_lines.append(f\"\\n### Quintile Breakdown\\n\")\n    report_lines.append(f\"| Quintile | C% (all) | C% (injected) | % Focal (all) | N_C | N_inj |\")\n    report_lines.append(f\"|----------|----------|---------------|---------------|-----|-------|\")\n    for q in range(1, 6):\n        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'n_c', 'n_inj']}\n        if cols['c_pct'] in sub.columns:\n            report_lines.append(\n                f\"| Q{q} | {sub[cols['c_pct']].mean():.1f} ± {sub[cols['c_pct']].std():.1f} | \"\n                f\"{sub[cols['c_pct_inj']].mean():.1f} ± {sub[cols['c_pct_inj']].std():.1f} | \"\n                f\"{sub[cols['pct_focal']].mean():.1f} ± {sub[cols['pct_focal']].std():.1f} | \"\n                f\"{sub[cols['n_c']].mean():.0f} | \"\n                f\"{sub[cols['n_inj']].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Key Comparison: ρ_inj across Schemes\\n\")\nreport_lines.append(f\"| Scheme | ρ_inj (mean ± SD) | Expected |\")\nreport_lines.append(f\"|--------|-------------------|----------|\")\nfor scheme, expected in [('A_capability', '≈ −0.5 to −0.6'), ('B_contamination', '≈ 0'), ('C_mixed', 'intermediate')]:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"| {scheme} | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} | {expected} |\")\nreport_lines.append(f\"| Baseline | {rho_base:.3f} | — |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **ρ_inj** is the key metric: ρ computed ONLY among injected items that are DIF-C.\")\nreport_lines.append(\"- **Scheme A** (capability-like): injection ∝ difficulty → focal-favoring DIF on easy items → ρ_inj ≈ −0.5 to −0.6\")\nreport_lines.append(\"- **Scheme B** (contamination-like): uniform p=0.5 injection → DIF uniform across difficulty → ρ_inj ≈ 0\")\nreport_lines.append(\"- **ρ_all** is dominated by ~3900 baseline C items and changes little across schemes.\")\n\nreport_text = \"\\n\".join(report_lines) + \"\\n\"\n\nwith open(os.path.join(OUT, \"semisynthetic_gradient_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"Saved: semisynthetic_gradient_report.md\")\nprint(\"\\n\" + report_text)\n",
    "structuredPatch": [
      {
        "oldStart": 190,
        "oldLines": 9,
        "newStart": 190,
        "newLines": 11,
        "lines": [
          " c_idx_base = np.where(is_c_base)[0]",
          " rho_base, _ = stats.spearmanr(item_difficulty[c_idx_base], delta_base[c_idx_base])",
          " n_c_base = is_c_base.sum()",
          "-n_focal_base = (is_c_base & (delta_base < 0)).sum()",
          "+# δ > 0 = focal-favoring, δ < 0 = ref-favoring",
          "+n_focal_base = (is_c_base & (delta_base > 0)).sum()",
          "+n_ref_base = (is_c_base & (delta_base < 0)).sum()",
          " print(f\"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, \"",
          "-      f\"focal%={n_focal_base/n_c_base*100:.1f}%, N_C={n_c_base}\")",
          "+      f\"focal%={n_focal_base/n_c_base*100:.1f}%, ref%={n_ref_base/n_c_base*100:.1f}%, N_C={n_c_base}\")",
          " ",
          " ",
          " # ════════════════════════════════════════════════════════════════════════════"
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

_source line 105_

Now update the report generation:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "02301d60-d76f-4de3-bc9c-7a2f423929e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdghcyDizaHnCkCSYtgKaZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 80628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 506
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

_source line 106_

<details open><summary>🔧 Tool call — Edit · `toolu_01GgaaXvTSAXYnuQebfqz7DW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "old_string": "report_lines.append(f\"\\n## Baseline (no injection)\\n\")\nreport_lines.append(f\"- C%: {n_c_base/J*100:.2f}%\")\nreport_lines.append(f\"- ρ(difficulty, Δ_MH) among C: {rho_base:.3f}\")\nreport_lines.append(f\"- % focal-favoring: {n_focal_base/n_c_base*100:.1f}%\")\nreport_lines.append(f\"- N DIF-C: {n_c_base}\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| C% (non-injected) | {sub['c_pct_noninj'].mean():.2f} ± {sub['c_pct_noninj'].std():.2f} |\")\n    report_lines.append(f\"| ρ_all (all C items) | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |\")\n    report_lines.append(f\"| **ρ_inj (injected C items)** | **{sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f}** |\")\n    report_lines.append(f\"| ρ_noninj (non-injected C) | {sub['rho_noninj'].mean():.3f} ± {sub['rho_noninj'].std():.3f} |\")\n    report_lines.append(f\"| ρ_new (newly flagged C) | {sub['rho_new'].mean():.3f} ± {sub['rho_new'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring (all) | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")\n    report_lines.append(f\"| % focal-favoring (injected C) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C (from injected) | {sub['n_newly_c_inj'].mean():.0f} ± {sub['n_newly_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    report_lines.append(f\"\\n### Quintile Breakdown\\n\")\n    report_lines.append(f\"| Quintile | C% (all) | C% (injected) | % Focal (all) | N_C | N_inj |\")\n    report_lines.append(f\"|----------|----------|---------------|---------------|-----|-------|\")\n    for q in range(1, 6):\n        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'n_c', 'n_inj']}\n        if cols['c_pct'] in sub.columns:\n            report_lines.append(\n                f\"| Q{q} | {sub[cols['c_pct']].mean():.1f} ± {sub[cols['c_pct']].std():.1f} | \"\n                f\"{sub[cols['c_pct_inj']].mean():.1f} ± {sub[cols['c_pct_inj']].std():.1f} | \"\n                f\"{sub[cols['pct_focal']].mean():.1f} ± {sub[cols['pct_focal']].std():.1f} | \"\n                f\"{sub[cols['n_c']].mean():.0f} | \"\n                f\"{sub[cols['n_inj']].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Key Comparison: ρ_inj across Schemes\\n\")\nreport_lines.append(f\"| Scheme | ρ_inj (mean ± SD) | Expected |\")\nreport_lines.append(f\"|--------|-------------------|----------|\")\nfor scheme, expected in [('A_capability', '≈ −0.5 to −0.6'), ('B_contamination', '≈ 0'), ('C_mixed', 'intermediate')]:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"| {scheme} | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} | {expected} |\")\nreport_lines.append(f\"| Baseline | {rho_base:.3f} | — |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **ρ_inj** is the key metric: ρ computed ONLY among injected items that are DIF-C.\")\nreport_lines.append(\"- **Scheme A** (capability-like): injection ∝ difficulty → focal-favoring DIF on easy items → ρ_inj ≈ −0.5 to −0.6\")\nreport_lines.append(\"- **Scheme B** (contamination-like): uniform p=0.5 injection → DIF uniform across difficulty → ρ_inj ≈ 0\")\nreport_lines.append(\"- **ρ_all** is dominated by ~3900 baseline C items and changes little across schemes.\")",
  "new_string": "report_lines.append(f\"\\n## Baseline (no injection)\\n\")\nreport_lines.append(f\"- C%: {n_c_base/J*100:.2f}%\")\nreport_lines.append(f\"- ρ(difficulty, δ_MH) among C: {rho_base:.3f}\")\nreport_lines.append(f\"- % focal-favoring (δ>0): {n_focal_base/n_c_base*100:.1f}%\")\nreport_lines.append(f\"- % ref-favoring (δ<0): {n_ref_base/n_c_base*100:.1f}%\")\nreport_lines.append(f\"- N DIF-C: {n_c_base}\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| C% (non-injected) | {sub['c_pct_noninj'].mean():.2f} ± {sub['c_pct_noninj'].std():.2f} |\")\n    report_lines.append(f\"| ρ(diff, δ) all C | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |\")\n    report_lines.append(f\"| ρ(diff, δ) injected C | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} |\")\n    report_lines.append(f\"| **ρ(diff, Δδ) injected items** | **{sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f}** |\")\n    report_lines.append(f\"| ρ(diff, Δδ) all items | {sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring (all C, δ>0) | {sub['pct_focal'].mean():.1f} ± {sub['pct_focal'].std():.1f} |\")\n    report_lines.append(f\"| % focal-favoring (inj C, δ>0) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |\")\n    report_lines.append(f\"| Mean Δδ (injected items) | {sub['mean_ddelta_inj'].mean():.3f} ± {sub['mean_ddelta_inj'].std():.3f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    report_lines.append(f\"\\n### Quintile Breakdown\\n\")\n    report_lines.append(f\"| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |\")\n    report_lines.append(f\"|----------|----------|----------|---------|---------------|-----|-------|\")\n    for q in range(1, 6):\n        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'mean_ddelta', 'n_c', 'n_inj']}\n        if cols['c_pct'] in sub.columns:\n            report_lines.append(\n                f\"| Q{q} | {sub[cols['c_pct']].mean():.1f} | \"\n                f\"{sub[cols['c_pct_inj']].mean():.1f} | \"\n                f\"{sub[cols['pct_focal']].mean():.1f} | \"\n                f\"{sub[cols['mean_ddelta']].mean():.3f} | \"\n                f\"{sub[cols['n_c']].mean():.0f} | \"\n                f\"{sub[cols['n_inj']].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated\\n\")\nreport_lines.append(\"Δδ = δ_after − δ_baseline isolates the injection-induced DIF shift.\\n\")\nreport_lines.append(f\"| Scheme | ρ(diff, Δδ) injected | ρ(diff, Δδ) all | Expected |\")\nreport_lines.append(f\"|--------|---------------------|-----------------|----------|\")\nfor scheme, expected in [('A_capability', 'positive (easy→more focal DIF)'),\n                         ('B_contamination', '≈ 0 (uniform)'),\n                         ('C_mixed', 'intermediate')]:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"| {scheme} | {sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f} | \"\n                       f\"{sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} | {expected} |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring\")\nreport_lines.append(\"- **Δδ = δ_after − δ_before**: positive Δδ means injection shifted item toward focal-favoring\")\nreport_lines.append(\"- **ρ(diff, Δδ)** is the key metric: isolates whether injection-induced DIF shift correlates with difficulty\")\nreport_lines.append(\"- **Scheme A**: injection ∝ difficulty → easy items get larger Δδ → ρ(diff, Δδ) > 0\")\nreport_lines.append(\"- **Scheme B**: uniform p=0.5 injection → Δδ independent of difficulty → ρ(diff, Δδ) ≈ 0\")\nreport_lines.append(\"- **ρ(diff, δ)**: dominated by ~3900 baseline C items, less sensitive to injection\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "b450f6b6-5804-4f61-b2b7-f43b80c182d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdghcyDizaHnCkCSYtgKaZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 80628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 506
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

_source line 107 · 2026-05-22T18:59:29.130Z_

<details><summary>↩ Tool result · `toolu_01GgaaXvTSAXYnuQebfqz7DW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "65a011e2-d1cd-441c-85b6-f6890eff3dd5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
    "oldString": "report_lines.append(f\"\\n## Baseline (no injection)\\n\")\nreport_lines.append(f\"- C%: {n_c_base/J*100:.2f}%\")\nreport_lines.append(f\"- ρ(difficulty, Δ_MH) among C: {rho_base:.3f}\")\nreport_lines.append(f\"- % focal-favoring: {n_focal_base/n_c_base*100:.1f}%\")\nreport_lines.append(f\"- N DIF-C: {n_c_base}\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| C% (non-injected) | {sub['c_pct_noninj'].mean():.2f} ± {sub['c_pct_noninj'].std():.2f} |\")\n    report_lines.append(f\"| ρ_all (all C items) | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |\")\n    report_lines.append(f\"| **ρ_inj (injected C items)** | **{sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f}** |\")\n    report_lines.append(f\"| ρ_noninj (non-injected C) | {sub['rho_noninj'].mean():.3f} ± {sub['rho_noninj'].std():.3f} |\")\n    report_lines.append(f\"| ρ_new (newly flagged C) | {sub['rho_new'].mean():.3f} ± {sub['rho_new'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring (all) | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")\n    report_lines.append(f\"| % focal-favoring (injected C) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C (from injected) | {sub['n_newly_c_inj'].mean():.0f} ± {sub['n_newly_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    report_lines.append(f\"\\n### Quintile Breakdown\\n\")\n    report_lines.append(f\"| Quintile | C% (all) | C% (injected) | % Focal (all) | N_C | N_inj |\")\n    report_lines.append(f\"|----------|----------|---------------|---------------|-----|-------|\")\n    for q in range(1, 6):\n        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'n_c', 'n_inj']}\n        if cols['c_pct'] in sub.columns:\n            report_lines.append(\n                f\"| Q{q} | {sub[cols['c_pct']].mean():.1f} ± {sub[cols['c_pct']].std():.1f} | \"\n                f\"{sub[cols['c_pct_inj']].mean():.1f} ± {sub[cols['c_pct_inj']].std():.1f} | \"\n                f\"{sub[cols['pct_focal']].mean():.1f} ± {sub[cols['pct_focal']].std():.1f} | \"\n                f\"{sub[cols['n_c']].mean():.0f} | \"\n                f\"{sub[cols['n_inj']].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Key Comparison: ρ_inj across Schemes\\n\")\nreport_lines.append(f\"| Scheme | ρ_inj (mean ± SD) | Expected |\")\nreport_lines.append(f\"|--------|-------------------|----------|\")\nfor scheme, expected in [('A_capability', '≈ −0.5 to −0.6'), ('B_contamination', '≈ 0'), ('C_mixed', 'intermediate')]:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"| {scheme} | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} | {expected} |\")\nreport_lines.append(f\"| Baseline | {rho_base:.3f} | — |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **ρ_inj** is the key metric: ρ computed ONLY among injected items that are DIF-C.\")\nreport_lines.append(\"- **Scheme A** (capability-like): injection ∝ difficulty → focal-favoring DIF on easy items → ρ_inj ≈ −0.5 to −0.6\")\nreport_lines.append(\"- **Scheme B** (contamination-like): uniform p=0.5 injection → DIF uniform across difficulty → ρ_inj ≈ 0\")\nreport_lines.append(\"- **ρ_all** is dominated by ~3900 baseline C items and changes little across schemes.\")",
    "newString": "report_lines.append(f\"\\n## Baseline (no injection)\\n\")\nreport_lines.append(f\"- C%: {n_c_base/J*100:.2f}%\")\nreport_lines.append(f\"- ρ(difficulty, δ_MH) among C: {rho_base:.3f}\")\nreport_lines.append(f\"- % focal-favoring (δ>0): {n_focal_base/n_c_base*100:.1f}%\")\nreport_lines.append(f\"- % ref-favoring (δ<0): {n_ref_base/n_c_base*100:.1f}%\")\nreport_lines.append(f\"- N DIF-C: {n_c_base}\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| C% (non-injected) | {sub['c_pct_noninj'].mean():.2f} ± {sub['c_pct_noninj'].std():.2f} |\")\n    report_lines.append(f\"| ρ(diff, δ) all C | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |\")\n    report_lines.append(f\"| ρ(diff, δ) injected C | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} |\")\n    report_lines.append(f\"| **ρ(diff, Δδ) injected items** | **{sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f}** |\")\n    report_lines.append(f\"| ρ(diff, Δδ) all items | {sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring (all C, δ>0) | {sub['pct_focal'].mean():.1f} ± {sub['pct_focal'].std():.1f} |\")\n    report_lines.append(f\"| % focal-favoring (inj C, δ>0) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |\")\n    report_lines.append(f\"| Mean Δδ (injected items) | {sub['mean_ddelta_inj'].mean():.3f} ± {sub['mean_ddelta_inj'].std():.3f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    report_lines.append(f\"\\n### Quintile Breakdown\\n\")\n    report_lines.append(f\"| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |\")\n    report_lines.append(f\"|----------|----------|----------|---------|---------------|-----|-------|\")\n    for q in range(1, 6):\n        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'mean_ddelta', 'n_c', 'n_inj']}\n        if cols['c_pct'] in sub.columns:\n            report_lines.append(\n                f\"| Q{q} | {sub[cols['c_pct']].mean():.1f} | \"\n                f\"{sub[cols['c_pct_inj']].mean():.1f} | \"\n                f\"{sub[cols['pct_focal']].mean():.1f} | \"\n                f\"{sub[cols['mean_ddelta']].mean():.3f} | \"\n                f\"{sub[cols['n_c']].mean():.0f} | \"\n                f\"{sub[cols['n_inj']].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated\\n\")\nreport_lines.append(\"Δδ = δ_after − δ_baseline isolates the injection-induced DIF shift.\\n\")\nreport_lines.append(f\"| Scheme | ρ(diff, Δδ) injected | ρ(diff, Δδ) all | Expected |\")\nreport_lines.append(f\"|--------|---------------------|-----------------|----------|\")\nfor scheme, expected in [('A_capability', 'positive (easy→more focal DIF)'),\n                         ('B_contamination', '≈ 0 (uniform)'),\n                         ('C_mixed', 'intermediate')]:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"| {scheme} | {sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f} | \"\n                       f\"{sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} | {expected} |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring\")\nreport_lines.append(\"- **Δδ = δ_after − δ_before**: positive Δδ means injection shifted item toward focal-favoring\")\nreport_lines.append(\"- **ρ(diff, Δδ)** is the key metric: isolates whether injection-induced DIF shift correlates with difficulty\")\nreport_lines.append(\"- **Scheme A**: injection ∝ difficulty → easy items get larger Δδ → ρ(diff, Δδ) > 0\")\nreport_lines.append(\"- **Scheme B**: uniform p=0.5 injection → Δδ independent of difficulty → ρ(diff, Δδ) ≈ 0\")\nreport_lines.append(\"- **ρ(diff, δ)**: dominated by ~3900 baseline C items, less sensitive to injection\")",
    "originalFile": "\"\"\"\nR19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\nTests whether MH-DIF can distinguish capability-like vs contamination-like DIF patterns.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom scipy.stats import chi2 as chi2_dist\nimport time, os, sys\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = os.path.join(ROOT, \"r19_semisynthetic_gradient\")\n\nN_SEEDS = 5\nN_STRATA = 5\nFOC_INJECT_FRAC = 0.30\nITEM_INJECT_FRAC = 0.24\n\n# ════════════════════════════════════════════════════════════════════════════\n#  VECTORIZED MH-DIF — returns per-item results\n# ════════════════════════════════════════════════════════════════════════════\ndef mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item delta_mh, p_value, is_c, direction.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C_mat = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C_mat[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C_mat\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C_mat\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C_mat / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n\n    return delta_j, pval_j, is_c\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  LOAD DATA\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"Loading data...\")\nrm = np.load(f\"{ROOT}/response_matrix.npz\")\nX_sparse = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nidx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\nmodel_names = idx['model_names']\nitem_ids = idx['item_ids']\n\nmeta = pd.read_csv(f\"{ROOT}/model_metadata.csv\")\nname_to_row = {n: i for i, n in enumerate(model_names)}\n\nref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values\nfoc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values\n\nref_idx = np.array([name_to_row[n] for n in ref_models if n in name_to_row])\nfoc_idx = np.array([name_to_row[n] for n in foc_models if n in name_to_row])\n\nN_ref, N_foc, J = len(ref_idx), len(foc_idx), len(item_ids)\nN_inject_models = int(N_foc * FOC_INJECT_FRAC)\nN_inject_items = int(J * ITEM_INJECT_FRAC)\n\nprint(f\"  Ref: {N_ref}, Foc: {N_foc}, Items: {J}\")\nprint(f\"  Injection targets: {N_inject_models} models, {N_inject_items} items\")\n\n# Densify the ref/foc submatrices\nX_ref_base = X_sparse[ref_idx].toarray().astype(np.float64)\nX_foc_base = X_sparse[foc_idx].toarray().astype(np.float64)\n\n# Ref cohort accuracy per item (= item difficulty proxy)\nitem_difficulty = X_ref_base.mean(axis=0)  # shape (J,)\n\nprint(f\"  Item difficulty: mean={item_difficulty.mean():.3f}, \"\n      f\"min={item_difficulty.min():.3f}, max={item_difficulty.max():.3f}\")\n\n# Get MMLU subjects per item for Scheme B (format: subject_name.question_number)\nitem_subjects = np.array([str(iid).rsplit('.', 1)[0] for iid in item_ids])\nunique_subjects = np.unique(item_subjects)\nprint(f\"  Unique subjects: {len(unique_subjects)}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  INJECTION SCHEMES\n# ════════════════════════════════════════════════════════════════════════════\ndef inject_scheme_a(X_foc, inject_model_mask, inject_item_idx, item_diff, rng):\n    \"\"\"Capability-like: injection probability ∝ difficulty (easy items more likely flipped).\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):\n    \"\"\"Contamination-like: uniform injection probability, restricted to 5 random subjects.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,\n                    item_diff, rng, p_const=0.5):\n    \"\"\"Mixed: half items use scheme A, half use scheme B.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    # Scheme A half\n    for j in inject_item_idx_a:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    # Scheme B half\n    for j in inject_item_idx_b:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  BASELINE (no injection)\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Baseline (no injection) ===\")\ndelta_base, pval_base, is_c_base = mh_dif_vec(X_ref_base, X_foc_base, n_strata=N_STRATA)\nc_idx_base = np.where(is_c_base)[0]\nrho_base, _ = stats.spearmanr(item_difficulty[c_idx_base], delta_base[c_idx_base])\nn_c_base = is_c_base.sum()\n# δ > 0 = focal-favoring, δ < 0 = ref-favoring\nn_focal_base = (is_c_base & (delta_base > 0)).sum()\nn_ref_base = (is_c_base & (delta_base < 0)).sum()\nprint(f\"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, \"\n      f\"focal%={n_focal_base/n_c_base*100:.1f}%, ref%={n_ref_base/n_c_base*100:.1f}%, N_C={n_c_base}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running experiments ===\")\nresults = []\nt0 = time.time()\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection models and items (shared across schemes within seed)\n    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)\n    inject_model_mask = np.zeros(N_foc, dtype=bool)\n    inject_model_mask[inject_model_idx] = True\n\n    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)\n\n    # Scheme B: select 5 random subjects, pick injection items from those subjects\n    selected_subjects = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask = np.isin(item_subjects, selected_subjects)\n    subject_item_pool = np.where(subject_mask)[0]\n    n_b_items = min(N_inject_items, len(subject_item_pool))\n    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)\n\n    # Scheme C: split A items in half\n    half = N_inject_items // 2\n    inject_item_idx_c_a = inject_item_idx_all[:half]\n    # For scheme C's B half, pick from 5 random subjects\n    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask_c = np.isin(item_subjects, selected_subjects_c)\n    subject_pool_c = np.where(subject_mask_c)[0]\n    # Exclude items already used by A half\n    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)\n    n_c_b = min(half, len(subject_pool_c))\n    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)\n\n    schemes = {\n        'A_capability': lambda: inject_scheme_a(\n            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),\n        'B_contamination': lambda: inject_scheme_b(\n            X_foc_base, inject_model_mask, inject_item_idx_b, rng),\n        'C_mixed': lambda: inject_scheme_c(\n            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,\n            item_difficulty, rng),\n    }\n\n    for scheme_name, inject_fn in schemes.items():\n        t1 = time.time()\n\n        X_foc_inj, n_flipped = inject_fn()\n\n        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # Delta change from baseline (isolates injection effect)\n        # δ > 0 = focal-favoring; injection flips focal 0→1 → pushes δ positive\n        ddelta = delta_j - delta_base\n\n        # C% among all / injected / non-injected items\n        inj_arr = np.array(sorted(injected_items))\n        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))\n        c_pct_all = is_c.sum() / J * 100\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100\n\n        # ρ(difficulty, δ) among all C items\n        c_idx = np.where(is_c)[0]\n        rho_all = np.nan\n        if len(c_idx) >= 3:\n            rho_all, _ = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n\n        # ρ(difficulty, δ) among injected C items\n        c_inj_mask = is_c & np.isin(np.arange(J), inj_arr)\n        c_inj_idx = np.where(c_inj_mask)[0]\n        rho_inj = np.nan\n        if len(c_inj_idx) >= 3:\n            rho_inj, _ = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])\n\n        # ρ(difficulty, Δδ) among injected items — KEY METRIC isolating injection signal\n        rho_ddelta_inj = np.nan\n        if len(inj_arr) >= 3:\n            rho_ddelta_inj, _ = stats.spearmanr(item_difficulty[inj_arr], ddelta[inj_arr])\n\n        # ρ(difficulty, Δδ) among all items\n        rho_ddelta_all = np.nan\n        if J >= 3:\n            rho_ddelta_all, _ = stats.spearmanr(item_difficulty, ddelta)\n\n        # Direction distribution: δ > 0 = focal-favoring, δ < 0 = ref-favoring\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j > 0)).sum()\n        n_ref_favoring = (is_c & (delta_j < 0)).sum()\n        pct_focal = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # Direction among injected C items\n        n_c_inj = c_inj_mask.sum()\n        n_focal_inj = (c_inj_mask & (delta_j > 0)).sum()\n        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0\n\n        # Newly flagged items (C after injection but not in baseline)\n        newly_c = is_c & ~is_c_base\n        n_newly_c = newly_c.sum()\n        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)\n        n_newly_c_inj = newly_c_inj.sum()\n\n        # Mean Δδ among injected items (injection effect magnitude)\n        mean_ddelta_inj = ddelta[inj_arr].mean()\n\n        # Per-quintile analysis\n        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n        quintile_data = {}\n        for q in range(5):\n            q_mask = (quintile_labels == q)\n            q_items = np.where(q_mask)[0]\n            q_inj_items = np.intersect1d(q_items, inj_arr)\n            q_c = is_c[q_items].sum()\n            q_total = len(q_items)\n            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n            q_focal = (is_c[q_items] & (delta_j[q_items] > 0)).sum()\n            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0\n            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0\n            q_mean_ddelta = ddelta[q_inj_items].mean() if len(q_inj_items) > 0 else 0\n            quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n            quintile_data[f'q{q+1}_n_c'] = q_c\n            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj\n            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)\n            quintile_data[f'q{q+1}_mean_ddelta'] = q_mean_ddelta\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            c_pct_noninj=c_pct_noninj,\n            n_c_total=n_c_total,\n            n_c_inj=n_c_inj,\n            rho_all=rho_all,\n            rho_inj=rho_inj,\n            rho_ddelta_inj=rho_ddelta_inj,\n            rho_ddelta_all=rho_ddelta_all,\n            pct_focal=pct_focal,\n            pct_focal_inj=pct_focal_inj,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            n_newly_c=n_newly_c,\n            n_newly_c_inj=n_newly_c_inj,\n            mean_ddelta_inj=mean_ddelta_inj,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ_all={rho_all:.3f}, ρ_Δδ_inj={rho_ddelta_inj:.3f}, \"\n              f\"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s\")\n\ntotal_time = time.time() - t0\nprint(f\"\\nTotal time: {total_time:.0f}s\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  SAVE RESULTS\n# ════════════════════════════════════════════════════════════════════════════\ndf = pd.DataFrame(results)\ndf.to_csv(os.path.join(OUT, \"semisynthetic_results.csv\"), index=False)\nprint(f\"\\nSaved: semisynthetic_results.csv ({len(df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  GENERATE REPORT\n# ════════════════════════════════════════════════════════════════════════════\nreport_lines = [\"# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\\n\"]\nreport_lines.append(f\"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\\n\")\nreport_lines.append(f\"**Config**: {N_SEEDS} seeds, {N_ref} ref models (2023), \"\n                    f\"{N_foc} foc models (2024), {J} items\\n\")\nreport_lines.append(f\"**Injection**: {N_inject_models} foc models ({FOC_INJECT_FRAC*100:.0f}%), \"\n                    f\"~{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\\n\")\n\nreport_lines.append(f\"\\n## Baseline (no injection)\\n\")\nreport_lines.append(f\"- C%: {n_c_base/J*100:.2f}%\")\nreport_lines.append(f\"- ρ(difficulty, Δ_MH) among C: {rho_base:.3f}\")\nreport_lines.append(f\"- % focal-favoring: {n_focal_base/n_c_base*100:.1f}%\")\nreport_lines.append(f\"- N DIF-C: {n_c_base}\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| C% (non-injected) | {sub['c_pct_noninj'].mean():.2f} ± {sub['c_pct_noninj'].std():.2f} |\")\n    report_lines.append(f\"| ρ_all (all C items) | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |\")\n    report_lines.append(f\"| **ρ_inj (injected C items)** | **{sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f}** |\")\n    report_lines.append(f\"| ρ_noninj (non-injected C) | {sub['rho_noninj'].mean():.3f} ± {sub['rho_noninj'].std():.3f} |\")\n    report_lines.append(f\"| ρ_new (newly flagged C) | {sub['rho_new'].mean():.3f} ± {sub['rho_new'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring (all) | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")\n    report_lines.append(f\"| % focal-favoring (injected C) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C (from injected) | {sub['n_newly_c_inj'].mean():.0f} ± {sub['n_newly_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    report_lines.append(f\"\\n### Quintile Breakdown\\n\")\n    report_lines.append(f\"| Quintile | C% (all) | C% (injected) | % Focal (all) | N_C | N_inj |\")\n    report_lines.append(f\"|----------|----------|---------------|---------------|-----|-------|\")\n    for q in range(1, 6):\n        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'n_c', 'n_inj']}\n        if cols['c_pct'] in sub.columns:\n            report_lines.append(\n                f\"| Q{q} | {sub[cols['c_pct']].mean():.1f} ± {sub[cols['c_pct']].std():.1f} | \"\n                f\"{sub[cols['c_pct_inj']].mean():.1f} ± {sub[cols['c_pct_inj']].std():.1f} | \"\n                f\"{sub[cols['pct_focal']].mean():.1f} ± {sub[cols['pct_focal']].std():.1f} | \"\n                f\"{sub[cols['n_c']].mean():.0f} | \"\n                f\"{sub[cols['n_inj']].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Key Comparison: ρ_inj across Schemes\\n\")\nreport_lines.append(f\"| Scheme | ρ_inj (mean ± SD) | Expected |\")\nreport_lines.append(f\"|--------|-------------------|----------|\")\nfor scheme, expected in [('A_capability', '≈ −0.5 to −0.6'), ('B_contamination', '≈ 0'), ('C_mixed', 'intermediate')]:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"| {scheme} | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} | {expected} |\")\nreport_lines.append(f\"| Baseline | {rho_base:.3f} | — |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **ρ_inj** is the key metric: ρ computed ONLY among injected items that are DIF-C.\")\nreport_lines.append(\"- **Scheme A** (capability-like): injection ∝ difficulty → focal-favoring DIF on easy items → ρ_inj ≈ −0.5 to −0.6\")\nreport_lines.append(\"- **Scheme B** (contamination-like): uniform p=0.5 injection → DIF uniform across difficulty → ρ_inj ≈ 0\")\nreport_lines.append(\"- **ρ_all** is dominated by ~3900 baseline C items and changes little across schemes.\")\n\nreport_text = \"\\n\".join(report_lines) + \"\\n\"\n\nwith open(os.path.join(OUT, \"semisynthetic_gradient_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"Saved: semisynthetic_gradient_report.md\")\nprint(\"\\n\" + report_text)\n",
    "structuredPatch": [
      {
        "oldStart": 390,
        "oldLines": 8,
        "newStart": 390,
        "newLines": 9,
        "lines": [
          " ",
          " report_lines.append(f\"\\n## Baseline (no injection)\\n\")",
          " report_lines.append(f\"- C%: {n_c_base/J*100:.2f}%\")",
          "-report_lines.append(f\"- ρ(difficulty, Δ_MH) among C: {rho_base:.3f}\")",
          "-report_lines.append(f\"- % focal-favoring: {n_focal_base/n_c_base*100:.1f}%\")",
          "+report_lines.append(f\"- ρ(difficulty, δ_MH) among C: {rho_base:.3f}\")",
          "+report_lines.append(f\"- % focal-favoring (δ>0): {n_focal_base/n_c_base*100:.1f}%\")",
          "+report_lines.append(f\"- % ref-favoring (δ<0): {n_ref_base/n_c_base*100:.1f}%\")",
          " report_lines.append(f\"- N DIF-C: {n_c_base}\")",
          " ",
          " for scheme in ['A_capability', 'B_contamination', 'C_mixed']:"
        ]
      },
      {
        "oldStart": 403,
        "oldLines": 45,
        "newStart": 404,
        "newLines": 51,
        "lines": [
          "     report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")",
          "     report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")",
          "     report_lines.append(f\"| C% (non-injected) | {sub['c_pct_noninj'].mean():.2f} ± {sub['c_pct_noninj'].std():.2f} |\")",
          "-    report_lines.append(f\"| ρ_all (all C items) | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |\")",
          "-    report_lines.append(f\"| **ρ_inj (injected C items)** | **{sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f}** |\")",
          "-    report_lines.append(f\"| ρ_noninj (non-injected C) | {sub['rho_noninj'].mean():.3f} ± {sub['rho_noninj'].std():.3f} |\")",
          "-    report_lines.append(f\"| ρ_new (newly flagged C) | {sub['rho_new'].mean():.3f} ± {sub['rho_new'].std():.3f} |\")",
          "-    report_lines.append(f\"| % focal-favoring (all) | {sub['pct_focal_favoring'].mean():.1f} ± {sub['pct_focal_favoring'].std():.1f} |\")",
          "-    report_lines.append(f\"| % focal-favoring (injected C) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |\")",
          "+    report_lines.append(f\"| ρ(diff, δ) all C | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |\")",
          "+    report_lines.append(f\"| ρ(diff, δ) injected C | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} |\")",
          "+    report_lines.append(f\"| **ρ(diff, Δδ) injected items** | **{sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f}** |\")",
          "+    report_lines.append(f\"| ρ(diff, Δδ) all items | {sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} |\")",
          "+    report_lines.append(f\"| % focal-favoring (all C, δ>0) | {sub['pct_focal'].mean():.1f} ± {sub['pct_focal'].std():.1f} |\")",
          "+    report_lines.append(f\"| % focal-favoring (inj C, δ>0) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |\")",
          "     report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")",
          "     report_lines.append(f\"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |\")",
          "     report_lines.append(f\"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |\")",
          "-    report_lines.append(f\"| Newly flagged C (from injected) | {sub['n_newly_c_inj'].mean():.0f} ± {sub['n_newly_c_inj'].std():.0f} |\")",
          "+    report_lines.append(f\"| Mean Δδ (injected items) | {sub['mean_ddelta_inj'].mean():.3f} ± {sub['mean_ddelta_inj'].std():.3f} |\")",
          "     report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")",
          "     report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")",
          " ",
          "     report_lines.append(f\"\\n### Quintile Breakdown\\n\")",
          "-    report_lines.append(f\"| Quintile | C% (all) | C% (injected) | % Focal (all) | N_C | N_inj |\")",
          "-    report_lines.append(f\"|----------|----------|---------------|---------------|-----|-------|\")",
          "+    report_lines.append(f\"| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |\")",
          "+    report_lines.append(f\"|----------|----------|----------|---------|---------------|-----|-------|\")",
          "     for q in range(1, 6):",
          "-        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'n_c', 'n_inj']}",
          "+        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'mean_ddelta', 'n_c', 'n_inj']}",
          "         if cols['c_pct'] in sub.columns:",
          "             report_lines.append(",
          "-                f\"| Q{q} | {sub[cols['c_pct']].mean():.1f} ± {sub[cols['c_pct']].std():.1f} | \"",
          "-                f\"{sub[cols['c_pct_inj']].mean():.1f} ± {sub[cols['c_pct_inj']].std():.1f} | \"",
          "-                f\"{sub[cols['pct_focal']].mean():.1f} ± {sub[cols['pct_focal']].std():.1f} | \"",
          "+                f\"| Q{q} | {sub[cols['c_pct']].mean():.1f} | \"",
          "+                f\"{sub[cols['c_pct_inj']].mean():.1f} | \"",
          "+                f\"{sub[cols['pct_focal']].mean():.1f} | \"",
          "+                f\"{sub[cols['mean_ddelta']].mean():.3f} | \"",
          "                 f\"{sub[cols['n_c']].mean():.0f} | \"",
          "                 f\"{sub[cols['n_inj']].mean():.0f} |\")",
          " ",
          "-report_lines.append(f\"\\n## Key Comparison: ρ_inj across Schemes\\n\")",
          "-report_lines.append(f\"| Scheme | ρ_inj (mean ± SD) | Expected |\")",
          "-report_lines.append(f\"|--------|-------------------|----------|\")",
          "-for scheme, expected in [('A_capability', '≈ −0.5 to −0.6'), ('B_contamination', '≈ 0'), ('C_mixed', 'intermediate')]:",
          "+report_lines.append(f\"\\n## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated\\n\")",
          "+report_lines.append(\"Δδ = δ_after − δ_baseline isolates the injection-induced DIF shift.\\n\")",
          "+report_lines.append(f\"| Scheme | ρ(diff, Δδ) injected | ρ(diff, Δδ) all | Expected |\")",
          "+report_lines.append(f\"|--------|---------------------|-----------------|----------|\")",
          "+for scheme, expected in [('A_capability', 'positive (easy→more focal DIF)'),",
          "+                         ('B_contamination', '≈ 0 (uniform)'),",
          "+                         ('C_mixed', 'intermediate')]:",
          "     sub = df[df['scheme'] == scheme]",
          "-    report_lines.append(f\"| {scheme} | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} | {expected} |\")",
          "-report_lines.append(f\"| Baseline | {rho_base:.3f} | — |\")",
          "+    report_lines.append(f\"| {scheme} | {sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f} | \"",
          "+                       f\"{sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} | {expected} |\")",
          " ",
          " report_lines.append(f\"\\n## Interpretation\\n\")",
          "-report_lines.append(\"- **ρ_inj** is the key metric: ρ computed ONLY among injected items that are DIF-C.\")",
          "-report_lines.append(\"- **Scheme A** (capability-like): injection ∝ difficulty → focal-favoring DIF on easy items → ρ_inj ≈ −0.5 to −0.6\")",
          "-report_lines.append(\"- **Scheme B** (contamination-like): uniform p=0.5 injection → DIF uniform across difficulty → ρ_inj ≈ 0\")",
          "-report_lines.append(\"- **ρ_all** is dominated by ~3900 baseline C items and changes little across schemes.\")",
          "+report_lines.append(\"- **Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring\")",
          "+report_lines.append(\"- **Δδ = δ_after − δ_before**: positive Δδ means injection shifted item toward focal-favoring\")",
          "+report_lines.append(\"- **ρ(diff, Δδ)** is the key metric: isolates whether injection-induced DIF shift correlates with difficulty\")",
          "+report_lines.append(\"- **Scheme A**: injection ∝ difficulty → easy items get larger Δδ → ρ(diff, Δδ) > 0\")",
          "+report_lines.append(\"- **Scheme B**: uniform p=0.5 injection → Δδ independent of difficulty → ρ(diff, Δδ) ≈ 0\")",
          "+report_lines.append(\"- **ρ(diff, δ)**: dominated by ~3900 baseline C items, less sensitive to injection\")",
          " ",
          " report_text = \"\\n\".join(report_lines) + \"\\n\"",
          " "
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

_source line 108_

<details open><summary>🔧 Tool call — Bash · `toolu_01NcZrZUEJDWoPW8Fi8U7GAX`</summary>

```json
{
  "command": "python3 artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "description": "Run experiment with delta-change analysis",
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
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "a2a4d18b-cfa0-438e-9f36-f1da6c916f79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BVRg4mFDneHwEhbTQhbbf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4117,
      "cache_read_input_tokens": 81134,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4117
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

### System

_source line 109_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b5ceqoym8",
  "tool_use_id": "toolu_01NcZrZUEJDWoPW8Fi8U7GAX",
  "description": "Run experiment with delta-change analysis",
  "task_type": "local_bash",
  "uuid": "fc1a68bc-e047-4527-9511-7b3df068f933",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### System

_source line 110_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b5ceqoym8",
  "tool_use_id": "toolu_01NcZrZUEJDWoPW8Fi8U7GAX",
  "status": "completed",
  "output_file": "",
  "summary": "Run experiment with delta-change analysis",
  "uuid": "bcd460bb-5fef-43ac-b524-7a8564db4047",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### Tool result

_source line 111 · 2026-05-22T18:59:42.532Z_

<details><summary>↩ Tool result · `toolu_01NcZrZUEJDWoPW8Fi8U7GAX`</summary>

```text
Loading data...
  Ref: 1080, Foc: 807, Items: 12508
  Injection targets: 242 models, 3001 items
  Item difficulty: mean=0.581, min=0.008, max=0.956
  Unique subjects: 57

=== Baseline (no injection) ===
  Baseline C%: 31.32%, ρ=-0.587, focal%=43.9%, ref%=56.1%, N_C=3918

=== Running experiments ===
  [A_capability] seed=1: C%=31.5%, ρ_all=-0.496, ρ_Δδ_inj=0.816, focal_inj%=87.4%, flips=105196, 0.6s
  [B_contamination] seed=1: C%=32.5%, ρ_all=-0.603, ρ_Δδ_inj=-0.591, focal_inj%=86.6%, flips=53279, 0.3s
  [C_mixed] seed=1: C%=31.1%, ρ_all=-0.531, ρ_Δδ_inj=0.310, focal_inj%=80.4%, flips=104104, 0.6s
  [A_capability] seed=2: C%=31.7%, ρ_all=-0.541, ρ_Δδ_inj=0.742, focal_inj%=84.4%, flips=98452, 0.6s
  [B_contamination] seed=2: C%=31.8%, ρ_all=-0.595, ρ_Δδ_inj=-0.553, focal_inj%=88.3%, flips=39733, 0.3s
  [C_mixed] seed=2: C%=32.0%, ρ_all=-0.566, ρ_Δδ_inj=0.384, focal_inj%=81.6%, flips=82803, 0.5s
  [A_capability] seed=3: C%=32.9%, ρ_all=-0.551, ρ_Δδ_inj=0.747, focal_inj%=85.5%, flips=103863, 0.6s
  [B_contamination] seed=3: C%=33.2%, ρ_all=-0.623, ρ_Δδ_inj=-0.629, focal_inj%=89.1%, flips=74372, 0.4s
  [C_mixed] seed=3: C%=31.9%, ρ_all=-0.562, ρ_Δδ_inj=0.441, focal_inj%=86.7%, flips=83437, 0.5s
  [A_capability] seed=4: C%=32.1%, ρ_all=-0.531, ρ_Δδ_inj=0.774, focal_inj%=85.2%, flips=105362, 0.6s
  [B_contamination] seed=4: C%=31.7%, ρ_all=-0.586, ρ_Δδ_inj=-0.435, focal_inj%=83.3%, flips=26927, 0.3s
  [C_mixed] seed=4: C%=32.6%, ρ_all=-0.574, ρ_Δδ_inj=0.438, focal_inj%=85.3%, flips=114043, 0.6s
  [A_capability] seed=5: C%=31.2%, ρ_all=-0.540, ρ_Δδ_inj=0.776, focal_inj%=83.5%, flips=99768, 0.6s
  [B_contamination] seed=5: C%=31.2%, ρ_all=-0.586, ρ_Δδ_inj=-0.377, focal_inj%=81.1%, flips=34991, 0.3s
  [C_mixed] seed=5: C%=32.2%, ρ_all=-0.572, ρ_Δδ_inj=0.397, focal_inj%=85.0%, flips=84375, 0.5s

Total time: 7s

Saved: semisynthetic_results.csv (15 rows)
Saved: semisynthetic_gradient_report.md

# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection

**Date**: 2026-05-22 18:59

**Config**: 5 seeds, 1080 ref models (2023), 807 foc models (2024), 12508 items

**Injection**: 242 foc models (30%), ~3001 items (24%)


## Baseline (no injection)

- C%: 31.32%
- ρ(difficulty, δ_MH) among C: -0.587
- % focal-favoring (δ>0): 43.9%
- % ref-favoring (δ<0): 56.1%
- N DIF-C: 3918

## Scheme A — Capability

| Metric | Mean ± SD |
|--------|-----------|
| C% (all items) | 31.88 ± 0.65 |
| C% (injected items) | 27.33 ± 0.94 |
| C% (non-injected) | 33.32 ± 0.82 |
| ρ(diff, δ) all C | -0.532 ± 0.021 |
| ρ(diff, δ) injected C | -0.229 ± 0.058 |
| **ρ(diff, Δδ) injected items** | **0.771 ± 0.029** |
| ρ(diff, Δδ) all items | -0.160 ± 0.131 |
| % focal-favoring (all C, δ>0) | 45.8 ± 1.3 |
| % focal-favoring (inj C, δ>0) | 85.2 ± 1.5 |
| N DIF-C items | 3988 ± 81 |
| N DIF-C (injected) | 820 ± 28 |
| Newly flagged C | 725 ± 74 |
| Mean Δδ (injected items) | 0.796 ± 0.049 |
| Responses flipped | 102528 ± 3208 |
| Items injected | 3001 |

### Quintile Breakdown

| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |
|----------|----------|----------|---------|---------------|-----|-------|
| Q1 | 34.1 | 35.4 | 88.4 | -0.080 | 853 | 585 |
| Q2 | 38.5 | 35.9 | 60.3 | 0.426 | 961 | 602 |
| Q3 | 32.4 | 30.0 | 33.3 | 1.045 | 811 | 620 |
| Q4 | 31.4 | 24.5 | 21.0 | 1.378 | 777 | 596 |
| Q5 | 23.2 | 10.9 | 10.0 | 1.188 | 587 | 598 |

## Scheme B — Contamination

| Metric | Mean ± SD |
|--------|-----------|
| C% (all items) | 32.07 ± 0.79 |
| C% (injected items) | 39.22 ± 6.34 |
| C% (non-injected) | 31.46 ± 0.23 |
| ρ(diff, δ) all C | -0.599 ± 0.015 |
| ρ(diff, δ) injected C | -0.729 ± 0.047 |
| **ρ(diff, Δδ) injected items** | **-0.517 ± 0.107** |
| ρ(diff, Δδ) all items | 0.181 ± 0.136 |
| % focal-favoring (all C, δ>0) | 43.6 ± 0.4 |
| % focal-favoring (inj C, δ>0) | 85.7 ± 3.4 |
| N DIF-C items | 4011 ± 99 |
| N DIF-C (injected) | 351 ± 136 |
| Newly flagged C | 354 ± 150 |
| Mean Δδ (injected items) | 1.018 ± 0.108 |
| Responses flipped | 45860 ± 18588 |
| Items injected | 873 |

### Quintile Breakdown

| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |
|----------|----------|----------|---------|---------------|-----|-------|
| Q1 | 38.2 | 87.4 | 90.2 | 1.938 | 956 | 210 |
| Q2 | 39.9 | 40.5 | 59.4 | 0.829 | 996 | 208 |
| Q3 | 32.8 | 27.4 | 25.1 | 0.698 | 820 | 175 |
| Q4 | 28.8 | 18.2 | 11.1 | 0.744 | 713 | 137 |
| Q5 | 20.8 | 9.4 | 2.1 | 0.682 | 526 | 144 |

## Scheme C — Mixed

| Metric | Mean ± SD |
|--------|-----------|
| C% (all items) | 31.98 ± 0.54 |
| C% (injected items) | 31.28 ± 2.87 |
| C% (non-injected) | 32.18 ± 0.25 |
| ρ(diff, δ) all C | -0.561 ± 0.017 |
| ρ(diff, δ) injected C | -0.496 ± 0.028 |
| **ρ(diff, Δδ) injected items** | **0.394 ± 0.053** |
| ρ(diff, Δδ) all items | -0.008 ± 0.101 |
| % focal-favoring (all C, δ>0) | 45.8 ± 1.6 |
| % focal-favoring (inj C, δ>0) | 83.8 ± 2.7 |
| N DIF-C items | 4000 ± 67 |
| N DIF-C (injected) | 749 ± 99 |
| Newly flagged C | 626 ± 51 |
| Mean Δδ (injected items) | 0.850 ± 0.039 |
| Responses flipped | 93752 ± 14432 |
| Items injected | 2407 |

### Quintile Breakdown

| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |
|----------|----------|----------|---------|---------------|-----|-------|
| Q1 | 37.2 | 53.8 | 89.2 | 0.600 | 931 | 469 |
| Q2 | 39.1 | 36.4 | 60.0 | 0.554 | 978 | 493 |
| Q3 | 32.6 | 30.1 | 29.5 | 0.926 | 815 | 467 |
| Q4 | 29.7 | 23.6 | 17.8 | 1.169 | 735 | 474 |
| Q5 | 21.4 | 12.5 | 8.3 | 1.029 | 542 | 503 |

## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated

Δδ = δ_after − δ_baseline isolates the injection-induced DIF shift.

| Scheme | ρ(diff, Δδ) injected | ρ(diff, Δδ) all | Expected |
|--------|---------------------|-----------------|----------|
| A_capability | 0.771 ± 0.029 | -0.160 ± 0.131 | positive (easy→more focal DIF) |
| B_contamination | -0.517 ± 0.107 | 0.181 ± 0.136 | ≈ 0 (uniform) |
| C_mixed | 0.394 ± 0.053 | -0.008 ± 0.101 | intermediate |

## Interpretation

- **Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring
- **Δδ = δ_after − δ_before**: positive Δδ means injection shifted item toward focal-favoring
- **ρ(diff, Δδ)** is the key metric: isolates whether injection-induced DIF shift correlates with difficulty
- **Scheme A**: injection ∝ difficulty → easy items get larger Δδ → ρ(diff, Δδ) > 0
- **Scheme B**: uniform p=0.5 injection → Δδ independent of difficulty → ρ(diff, Δδ) ≈ 0
- **ρ(diff, δ)**: dominated by ~3900 baseline C items, less sensitive to injection
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "7bbe4e36-fa2c-4652-a0fc-81e533df1a46",
  "tool_use_result": {
    "stdout": "Loading data...\n  Ref: 1080, Foc: 807, Items: 12508\n  Injection targets: 242 models, 3001 items\n  Item difficulty: mean=0.581, min=0.008, max=0.956\n  Unique subjects: 57\n\n=== Baseline (no injection) ===\n  Baseline C%: 31.32%, ρ=-0.587, focal%=43.9%, ref%=56.1%, N_C=3918\n\n=== Running experiments ===\n  [A_capability] seed=1: C%=31.5%, ρ_all=-0.496, ρ_Δδ_inj=0.816, focal_inj%=87.4%, flips=105196, 0.6s\n  [B_contamination] seed=1: C%=32.5%, ρ_all=-0.603, ρ_Δδ_inj=-0.591, focal_inj%=86.6%, flips=53279, 0.3s\n  [C_mixed] seed=1: C%=31.1%, ρ_all=-0.531, ρ_Δδ_inj=0.310, focal_inj%=80.4%, flips=104104, 0.6s\n  [A_capability] seed=2: C%=31.7%, ρ_all=-0.541, ρ_Δδ_inj=0.742, focal_inj%=84.4%, flips=98452, 0.6s\n  [B_contamination] seed=2: C%=31.8%, ρ_all=-0.595, ρ_Δδ_inj=-0.553, focal_inj%=88.3%, flips=39733, 0.3s\n  [C_mixed] seed=2: C%=32.0%, ρ_all=-0.566, ρ_Δδ_inj=0.384, focal_inj%=81.6%, flips=82803, 0.5s\n  [A_capability] seed=3: C%=32.9%, ρ_all=-0.551, ρ_Δδ_inj=0.747, focal_inj%=85.5%, flips=103863, 0.6s\n  [B_contamination] seed=3: C%=33.2%, ρ_all=-0.623, ρ_Δδ_inj=-0.629, focal_inj%=89.1%, flips=74372, 0.4s\n  [C_mixed] seed=3: C%=31.9%, ρ_all=-0.562, ρ_Δδ_inj=0.441, focal_inj%=86.7%, flips=83437, 0.5s\n  [A_capability] seed=4: C%=32.1%, ρ_all=-0.531, ρ_Δδ_inj=0.774, focal_inj%=85.2%, flips=105362, 0.6s\n  [B_contamination] seed=4: C%=31.7%, ρ_all=-0.586, ρ_Δδ_inj=-0.435, focal_inj%=83.3%, flips=26927, 0.3s\n  [C_mixed] seed=4: C%=32.6%, ρ_all=-0.574, ρ_Δδ_inj=0.438, focal_inj%=85.3%, flips=114043, 0.6s\n  [A_capability] seed=5: C%=31.2%, ρ_all=-0.540, ρ_Δδ_inj=0.776, focal_inj%=83.5%, flips=99768, 0.6s\n  [B_contamination] seed=5: C%=31.2%, ρ_all=-0.586, ρ_Δδ_inj=-0.377, focal_inj%=81.1%, flips=34991, 0.3s\n  [C_mixed] seed=5: C%=32.2%, ρ_all=-0.572, ρ_Δδ_inj=0.397, focal_inj%=85.0%, flips=84375, 0.5s\n\nTotal time: 7s\n\nSaved: semisynthetic_results.csv (15 rows)\nSaved: semisynthetic_gradient_report.md\n\n# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\n\n**Date**: 2026-05-22 18:59\n\n**Config**: 5 seeds, 1080 ref models (2023), 807 foc models (2024), 12508 items\n\n**Injection**: 242 foc models (30%), ~3001 items (24%)\n\n\n## Baseline (no injection)\n\n- C%: 31.32%\n- ρ(difficulty, δ_MH) among C: -0.587\n- % focal-favoring (δ>0): 43.9%\n- % ref-favoring (δ<0): 56.1%\n- N DIF-C: 3918\n\n## Scheme A — Capability\n\n| Metric | Mean ± SD |\n|--------|-----------|\n| C% (all items) | 31.88 ± 0.65 |\n| C% (injected items) | 27.33 ± 0.94 |\n| C% (non-injected) | 33.32 ± 0.82 |\n| ρ(diff, δ) all C | -0.532 ± 0.021 |\n| ρ(diff, δ) injected C | -0.229 ± 0.058 |\n| **ρ(diff, Δδ) injected items** | **0.771 ± 0.029** |\n| ρ(diff, Δδ) all items | -0.160 ± 0.131 |\n| % focal-favoring (all C, δ>0) | 45.8 ± 1.3 |\n| % focal-favoring (inj C, δ>0) | 85.2 ± 1.5 |\n| N DIF-C items | 3988 ± 81 |\n| N DIF-C (injected) | 820 ± 28 |\n| Newly flagged C | 725 ± 74 |\n| Mean Δδ (injected items) | 0.796 ± 0.049 |\n| Responses flipped | 102528 ± 3208 |\n| Items injected | 3001 |\n\n### Quintile Breakdown\n\n| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |\n|----------|----------|----------|---------|---------------|-----|-------|\n| Q1 | 34.1 | 35.4 | 88.4 | -0.080 | 853 | 585 |\n| Q2 | 38.5 | 35.9 | 60.3 | 0.426 | 961 | 602 |\n| Q3 | 32.4 | 30.0 | 33.3 | 1.045 | 811 | 620 |\n| Q4 | 31.4 | 24.5 | 21.0 | 1.378 | 777 | 596 |\n| Q5 | 23.2 | 10.9 | 10.0 | 1.188 | 587 | 598 |\n\n## Scheme B — Contamination\n\n| Metric | Mean ± SD |\n|--------|-----------|\n| C% (all items) | 32.07 ± 0.79 |\n| C% (injected items) | 39.22 ± 6.34 |\n| C% (non-injected) | 31.46 ± 0.23 |\n| ρ(diff, δ) all C | -0.599 ± 0.015 |\n| ρ(diff, δ) injected C | -0.729 ± 0.047 |\n| **ρ(diff, Δδ) injected items** | **-0.517 ± 0.107** |\n| ρ(diff, Δδ) all items | 0.181 ± 0.136 |\n| % focal-favoring (all C, δ>0) | 43.6 ± 0.4 |\n| % focal-favoring (inj C, δ>0) | 85.7 ± 3.4 |\n| N DIF-C items | 4011 ± 99 |\n| N DIF-C (injected) | 351 ± 136 |\n| Newly flagged C | 354 ± 150 |\n| Mean Δδ (injected items) | 1.018 ± 0.108 |\n| Responses flipped | 45860 ± 18588 |\n| Items injected | 873 |\n\n### Quintile Breakdown\n\n| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |\n|----------|----------|----------|---------|---------------|-----|-------|\n| Q1 | 38.2 | 87.4 | 90.2 | 1.938 | 956 | 210 |\n| Q2 | 39.9 | 40.5 | 59.4 | 0.829 | 996 | 208 |\n| Q3 | 32.8 | 27.4 | 25.1 | 0.698 | 820 | 175 |\n| Q4 | 28.8 | 18.2 | 11.1 | 0.744 | 713 | 137 |\n| Q5 | 20.8 | 9.4 | 2.1 | 0.682 | 526 | 144 |\n\n## Scheme C — Mixed\n\n| Metric | Mean ± SD |\n|--------|-----------|\n| C% (all items) | 31.98 ± 0.54 |\n| C% (injected items) | 31.28 ± 2.87 |\n| C% (non-injected) | 32.18 ± 0.25 |\n| ρ(diff, δ) all C | -0.561 ± 0.017 |\n| ρ(diff, δ) injected C | -0.496 ± 0.028 |\n| **ρ(diff, Δδ) injected items** | **0.394 ± 0.053** |\n| ρ(diff, Δδ) all items | -0.008 ± 0.101 |\n| % focal-favoring (all C, δ>0) | 45.8 ± 1.6 |\n| % focal-favoring (inj C, δ>0) | 83.8 ± 2.7 |\n| N DIF-C items | 4000 ± 67 |\n| N DIF-C (injected) | 749 ± 99 |\n| Newly flagged C | 626 ± 51 |\n| Mean Δδ (injected items) | 0.850 ± 0.039 |\n| Responses flipped | 93752 ± 14432 |\n| Items injected | 2407 |\n\n### Quintile Breakdown\n\n| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |\n|----------|----------|----------|---------|---------------|-----|-------|\n| Q1 | 37.2 | 53.8 | 89.2 | 0.600 | 931 | 469 |\n| Q2 | 39.1 | 36.4 | 60.0 | 0.554 | 978 | 493 |\n| Q3 | 32.6 | 30.1 | 29.5 | 0.926 | 815 | 467 |\n| Q4 | 29.7 | 23.6 | 17.8 | 1.169 | 735 | 474 |\n| Q5 | 21.4 | 12.5 | 8.3 | 1.029 | 542 | 503 |\n\n## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated\n\nΔδ = δ_after − δ_baseline isolates the injection-induced DIF shift.\n\n| Scheme | ρ(diff, Δδ) injected | ρ(diff, Δδ) all | Expected |\n|--------|---------------------|-----------------|----------|\n| A_capability | 0.771 ± 0.029 | -0.160 ± 0.131 | positive (easy→more focal DIF) |\n| B_contamination | -0.517 ± 0.107 | 0.181 ± 0.136 | ≈ 0 (uniform) |\n| C_mixed | 0.394 ± 0.053 | -0.008 ± 0.101 | intermediate |\n\n## Interpretation\n\n- **Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring\n- **Δδ = δ_after − δ_before**: positive Δδ means injection shifted item toward focal-favoring\n- **ρ(diff, Δδ)** is the key metric: isolates whether injection-induced DIF shift correlates with difficulty\n- **Scheme A**: injection ∝ difficulty → easy items get larger Δδ → ρ(diff, Δδ) > 0\n- **Scheme B**: uniform p=0.5 injection → Δδ independent of difficulty → ρ(diff, Δδ) ≈ 0\n- **ρ(diff, δ)**: dominated by ~3900 baseline C items, less sensitive to injection",
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

_source line 112_

<details><summary>Logged reasoning block</summary>

```text
The results are interesting:

**Scheme A** (capability-like): ρ(diff, Δδ) = **+0.771** — strong positive, as expected. Easy items (high difficulty) get more Δδ shift toward focal-favoring.

**Scheme B** (contamination-like): ρ(diff, Δδ) = **−0.517** — NOT ≈ 0 as expected. Instead, it's strongly negative, meaning hard items get MORE Δδ shift.

This makes sense: with uniform p=0.5 injection, HARD items have more 0s to flip (lower accuracy → more incorrect responses), so they get more actual flips → larger Δδ. 

The key insight is that uniform injection probability doesn't translate to uniform DIF shift across difficulty levels—hard items have more 0s available to flip, so the same injection probability produces more actual flips and larger changes. To make Scheme B truly produce ρ ≈ 0, I'd need to adjust the injection probability inversely with the number of 0s available, ensuring the expected number of flips stays constant regardless of item difficulty.

This finding actually reveals something important: even uniform contamination creates difficulty-dependent DIF patterns because of ceiling effects on easy items, which challenges the simple assumption that contamination should be uniform while capability is difficulty-dependent. I should document this clearly in the report—the expected ρ ≈ 0 was based on flawed assumptions, and the actual ρ ≈ −0.52 shows that uniform contamination still produces systematic difficulty-dependent effects.

Now I need to verify whether Scheme B should use the same 3000 randomly selected items as Scheme A or if the 5-subject restriction is intentional. Looking back at the specification, Scheme B is indeed limited to 5 subjects (~870 items) as part of the contamination simulation, which represents memorizing specific test sets rather than uniform contamination across all subjects. So the restriction is by design, not an oversight.

The core finding seems valid despite the unexpected direction: the correlation for Scheme B is −0.52 rather than the expected ≈0, which appears driven by ceiling and floor effects since harder items within those 5 subjects have more capacity for flips. I could normalize by the expected flip rate to correct for this, but the real insight is that MH-DIF successfully distinguishes between the two patterns—Scheme A shows ρ = +0.77 while Scheme B shows ρ = −0.52, which are clearly different even if B's direction is counterintuitive. I'm wrapping up the interpretation section to clarify why Scheme B shows a negative correlation rather than zero—the ceiling effect creates a systematic pattern where difficulty influences the relationship between contamination and performance differences, even with uniform injection probability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "2b2b4a51-d1dd-41b7-a72f-c2eca2c3747c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013u5XTtQGtSF3unELbF4QoT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3777,
      "cache_read_input_tokens": 85251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3777
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

_source line 113_

The Δδ analysis cleanly separates the schemes:
- **Scheme A**: ρ(diff, Δδ) = **+0.77** (strong positive, as expected)  
- **Scheme B**: ρ(diff, Δδ) = **−0.52** (not 0 — ceiling effect: hard items have more 0s to flip, so uniform p produces more flips on hard items)
- **Scheme C**: ρ(diff, Δδ) = **+0.39** (intermediate)

The expected ρ ≈ 0 for Scheme B doesn't hold because of the ceiling effect — an important finding. Let me update the interpretation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "5020f9b0-8564-48a3-b7f9-3baf8dc8e1ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013u5XTtQGtSF3unELbF4QoT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3777,
      "cache_read_input_tokens": 85251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3777
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

_source line 114_

<details open><summary>🔧 Tool call — Read · `toolu_0149Qf21yB7HnMTFLgFwC4y9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "offset": 410,
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
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "fcd19b1d-26c0-4c88-b661-83773b55a66a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013u5XTtQGtSF3unELbF4QoT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3777,
      "cache_read_input_tokens": 85251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3777
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

_source line 115 · 2026-05-22T19:00:21.091Z_

<details><summary>↩ Tool result · `toolu_0149Qf21yB7HnMTFLgFwC4y9`</summary>

```text
410	    report_lines.append(f"| ρ(diff, Δδ) all items | {sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} |")
411	    report_lines.append(f"| % focal-favoring (all C, δ>0) | {sub['pct_focal'].mean():.1f} ± {sub['pct_focal'].std():.1f} |")
412	    report_lines.append(f"| % focal-favoring (inj C, δ>0) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |")
413	    report_lines.append(f"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |")
414	    report_lines.append(f"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |")
415	    report_lines.append(f"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |")
416	    report_lines.append(f"| Mean Δδ (injected items) | {sub['mean_ddelta_inj'].mean():.3f} ± {sub['mean_ddelta_inj'].std():.3f} |")
417	    report_lines.append(f"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |")
418	    report_lines.append(f"| Items injected | {sub['n_inject_items'].mean():.0f} |")
419	
420	    report_lines.append(f"\n### Quintile Breakdown\n")
421	    report_lines.append(f"| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |")
422	    report_lines.append(f"|----------|----------|----------|---------|---------------|-----|-------|")
423	    for q in range(1, 6):
424	        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'mean_ddelta', 'n_c', 'n_inj']}
425	        if cols['c_pct'] in sub.columns:
426	            report_lines.append(
427	                f"| Q{q} | {sub[cols['c_pct']].mean():.1f} | "
428	                f"{sub[cols['c_pct_inj']].mean():.1f} | "
429	                f"{sub[cols['pct_focal']].mean():.1f} | "
430	                f"{sub[cols['mean_ddelta']].mean():.3f} | "
431	                f"{sub[cols['n_c']].mean():.0f} | "
432	                f"{sub[cols['n_inj']].mean():.0f} |")
433	
434	report_lines.append(f"\n## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated\n")
435	report_lines.append("Δδ = δ_after − δ_baseline isolates the injection-induced DIF shift.\n")
436	report_lines.append(f"| Scheme | ρ(diff, Δδ) injected | ρ(diff, Δδ) all | Expected |")
437	report_lines.append(f"|--------|---------------------|-----------------|----------|")
438	for scheme, expected in [('A_capability', 'positive (easy→more focal DIF)'),
439	                         ('B_contamination', '≈ 0 (uniform)'),
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "ca55d2be-d2d5-4103-92c3-4771a2baabfd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
      "content": "    report_lines.append(f\"| ρ(diff, Δδ) all items | {sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring (all C, δ>0) | {sub['pct_focal'].mean():.1f} ± {sub['pct_focal'].std():.1f} |\")\n    report_lines.append(f\"| % focal-favoring (inj C, δ>0) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |\")\n    report_lines.append(f\"| Mean Δδ (injected items) | {sub['mean_ddelta_inj'].mean():.3f} ± {sub['mean_ddelta_inj'].std():.3f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    report_lines.append(f\"\\n### Quintile Breakdown\\n\")\n    report_lines.append(f\"| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |\")\n    report_lines.append(f\"|----------|----------|----------|---------|---------------|-----|-------|\")\n    for q in range(1, 6):\n        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'mean_ddelta', 'n_c', 'n_inj']}\n        if cols['c_pct'] in sub.columns:\n            report_lines.append(\n                f\"| Q{q} | {sub[cols['c_pct']].mean():.1f} | \"\n                f\"{sub[cols['c_pct_inj']].mean():.1f} | \"\n                f\"{sub[cols['pct_focal']].mean():.1f} | \"\n                f\"{sub[cols['mean_ddelta']].mean():.3f} | \"\n                f\"{sub[cols['n_c']].mean():.0f} | \"\n                f\"{sub[cols['n_inj']].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated\\n\")\nreport_lines.append(\"Δδ = δ_after − δ_baseline isolates the injection-induced DIF shift.\\n\")\nreport_lines.append(f\"| Scheme | ρ(diff, Δδ) injected | ρ(diff, Δδ) all | Expected |\")\nreport_lines.append(f\"|--------|---------------------|-----------------|----------|\")\nfor scheme, expected in [('A_capability', 'positive (easy→more focal DIF)'),\n                         ('B_contamination', '≈ 0 (uniform)'),",
      "numLines": 30,
      "startLine": 410,
      "totalLines": 460
    }
  }
}
```

</details>

---

### Tool call

_source line 116_

<details open><summary>🔧 Tool call — Read · `toolu_01M9ckWM2iTCe16egEBPkLsW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "offset": 439,
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
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "9fa2ed55-6198-42d2-951a-883ffd7088a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CLSX58Q7aeinrGDQTZLcgx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2554,
      "cache_read_input_tokens": 89028,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2554
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

_source line 117 · 2026-05-22T19:00:30.399Z_

<details><summary>↩ Tool result · `toolu_01M9ckWM2iTCe16egEBPkLsW`</summary>

```text
439	                         ('B_contamination', '≈ 0 (uniform)'),
440	                         ('C_mixed', 'intermediate')]:
441	    sub = df[df['scheme'] == scheme]
442	    report_lines.append(f"| {scheme} | {sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f} | "
443	                       f"{sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} | {expected} |")
444	
445	report_lines.append(f"\n## Interpretation\n")
446	report_lines.append("- **Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring")
447	report_lines.append("- **Δδ = δ_after − δ_before**: positive Δδ means injection shifted item toward focal-favoring")
448	report_lines.append("- **ρ(diff, Δδ)** is the key metric: isolates whether injection-induced DIF shift correlates with difficulty")
449	report_lines.append("- **Scheme A**: injection ∝ difficulty → easy items get larger Δδ → ρ(diff, Δδ) > 0")
450	report_lines.append("- **Scheme B**: uniform p=0.5 injection → Δδ independent of difficulty → ρ(diff, Δδ) ≈ 0")
451	report_lines.append("- **ρ(diff, δ)**: dominated by ~3900 baseline C items, less sensitive to injection")
452	
453	report_text = "\n".join(report_lines) + "\n"
454	
455	with open(os.path.join(OUT, "semisynthetic_gradient_report.md"), "w") as f:
456	    f.write(report_text)
457	
458	print(f"Saved: semisynthetic_gradient_report.md")
459	print("\n" + report_text)
460	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "2f4d0a13-5f61-44a5-8f1b-6df038bf1a19",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
      "content": "                         ('B_contamination', '≈ 0 (uniform)'),\n                         ('C_mixed', 'intermediate')]:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"| {scheme} | {sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f} | \"\n                       f\"{sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} | {expected} |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring\")\nreport_lines.append(\"- **Δδ = δ_after − δ_before**: positive Δδ means injection shifted item toward focal-favoring\")\nreport_lines.append(\"- **ρ(diff, Δδ)** is the key metric: isolates whether injection-induced DIF shift correlates with difficulty\")\nreport_lines.append(\"- **Scheme A**: injection ∝ difficulty → easy items get larger Δδ → ρ(diff, Δδ) > 0\")\nreport_lines.append(\"- **Scheme B**: uniform p=0.5 injection → Δδ independent of difficulty → ρ(diff, Δδ) ≈ 0\")\nreport_lines.append(\"- **ρ(diff, δ)**: dominated by ~3900 baseline C items, less sensitive to injection\")\n\nreport_text = \"\\n\".join(report_lines) + \"\\n\"\n\nwith open(os.path.join(OUT, \"semisynthetic_gradient_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"Saved: semisynthetic_gradient_report.md\")\nprint(\"\\n\" + report_text)\n",
      "numLines": 22,
      "startLine": 439,
      "totalLines": 460
    }
  }
}
```

</details>

---

### Tool call

_source line 118_

<details open><summary>🔧 Tool call — Edit · `toolu_018o4tcavKoLHwJ7FtHy7Vxz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "old_string": "report_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring\")\nreport_lines.append(\"- **Δδ = δ_after − δ_before**: positive Δδ means injection shifted item toward focal-favoring\")\nreport_lines.append(\"- **ρ(diff, Δδ)** is the key metric: isolates whether injection-induced DIF shift correlates with difficulty\")\nreport_lines.append(\"- **Scheme A**: injection ∝ difficulty → easy items get larger Δδ → ρ(diff, Δδ) > 0\")\nreport_lines.append(\"- **Scheme B**: uniform p=0.5 injection → Δδ independent of difficulty → ρ(diff, Δδ) ≈ 0\")\nreport_lines.append(\"- **ρ(diff, δ)**: dominated by ~3900 baseline C items, less sensitive to injection\")",
  "new_string": "report_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"**Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring. \"\n                    \"Δδ = δ_after − δ_before; positive Δδ = injection shifted item toward focal-favoring.\\n\")\nreport_lines.append(\"### Key finding: three schemes produce cleanly separable ρ(diff, Δδ) signatures\\n\")\nreport_lines.append(\"1. **Scheme A** (capability-like): ρ(diff, Δδ) ≈ **+0.77**. \"\n                    \"Injection probability ∝ item accuracy → easy items receive more flips → \"\n                    \"larger focal-favoring Δδ on easy items. Strong positive correlation.\")\nreport_lines.append(\"2. **Scheme B** (contamination-like): ρ(diff, Δδ) ≈ **−0.52** (NOT ≈ 0 as naively expected). \"\n                    \"Uniform p=0.5 injection gives equal probability per response, but hard items \"\n                    \"have more 0→1 flippable responses (ceiling effect). \"\n                    \"Result: hard items accumulate more flips → larger Δδ on hard items → negative ρ.\")\nreport_lines.append(\"3. **Scheme C** (mixed): ρ(diff, Δδ) ≈ **+0.39**, intermediate between A and B, \"\n                    \"as expected from mixing both injection mechanisms.\\n\")\nreport_lines.append(\"### Ceiling effect insight\\n\")\nreport_lines.append(\"The Scheme B result (ρ ≈ −0.5 instead of 0) reveals that **uniform memorization probability \"\n                    \"does NOT produce uniform DIF**. Easy items have high baseline accuracy → few 0s to flip → \"\n                    \"small Δδ even at p=0.5. Hard items have low accuracy → many 0s → large Δδ. \"\n                    \"This ceiling effect is an inherent property of binary response matrices and means \"\n                    \"the capability vs. contamination distinction is NOT simply 'correlated vs. uncorrelated with difficulty,' \"\n                    \"but rather the SIGN and MAGNITUDE of the difficulty-DIF gradient.\\n\")\nreport_lines.append(\"### Discriminability\\n\")\nreport_lines.append(\"- A vs B separation: Δρ ≈ 1.29 (0.77 − (−0.52)), massive and non-overlapping across all seeds\")\nreport_lines.append(\"- A vs C separation: Δρ ≈ 0.38, clear but smaller\")\nreport_lines.append(\"- The three patterns are unambiguously distinguishable by ρ(diff, Δδ) alone\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "2995a25b-c31f-44a5-a535-57909555f7a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013cfDQvSHipiAqf8k4dsTwF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 91582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 792
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

_source line 119 · 2026-05-22T19:00:56.364Z_

<details><summary>↩ Tool result · `toolu_018o4tcavKoLHwJ7FtHy7Vxz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "3b32a86e-13ac-4479-8852-17acfbf48a95",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
    "oldString": "report_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring\")\nreport_lines.append(\"- **Δδ = δ_after − δ_before**: positive Δδ means injection shifted item toward focal-favoring\")\nreport_lines.append(\"- **ρ(diff, Δδ)** is the key metric: isolates whether injection-induced DIF shift correlates with difficulty\")\nreport_lines.append(\"- **Scheme A**: injection ∝ difficulty → easy items get larger Δδ → ρ(diff, Δδ) > 0\")\nreport_lines.append(\"- **Scheme B**: uniform p=0.5 injection → Δδ independent of difficulty → ρ(diff, Δδ) ≈ 0\")\nreport_lines.append(\"- **ρ(diff, δ)**: dominated by ~3900 baseline C items, less sensitive to injection\")",
    "newString": "report_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"**Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring. \"\n                    \"Δδ = δ_after − δ_before; positive Δδ = injection shifted item toward focal-favoring.\\n\")\nreport_lines.append(\"### Key finding: three schemes produce cleanly separable ρ(diff, Δδ) signatures\\n\")\nreport_lines.append(\"1. **Scheme A** (capability-like): ρ(diff, Δδ) ≈ **+0.77**. \"\n                    \"Injection probability ∝ item accuracy → easy items receive more flips → \"\n                    \"larger focal-favoring Δδ on easy items. Strong positive correlation.\")\nreport_lines.append(\"2. **Scheme B** (contamination-like): ρ(diff, Δδ) ≈ **−0.52** (NOT ≈ 0 as naively expected). \"\n                    \"Uniform p=0.5 injection gives equal probability per response, but hard items \"\n                    \"have more 0→1 flippable responses (ceiling effect). \"\n                    \"Result: hard items accumulate more flips → larger Δδ on hard items → negative ρ.\")\nreport_lines.append(\"3. **Scheme C** (mixed): ρ(diff, Δδ) ≈ **+0.39**, intermediate between A and B, \"\n                    \"as expected from mixing both injection mechanisms.\\n\")\nreport_lines.append(\"### Ceiling effect insight\\n\")\nreport_lines.append(\"The Scheme B result (ρ ≈ −0.5 instead of 0) reveals that **uniform memorization probability \"\n                    \"does NOT produce uniform DIF**. Easy items have high baseline accuracy → few 0s to flip → \"\n                    \"small Δδ even at p=0.5. Hard items have low accuracy → many 0s → large Δδ. \"\n                    \"This ceiling effect is an inherent property of binary response matrices and means \"\n                    \"the capability vs. contamination distinction is NOT simply 'correlated vs. uncorrelated with difficulty,' \"\n                    \"but rather the SIGN and MAGNITUDE of the difficulty-DIF gradient.\\n\")\nreport_lines.append(\"### Discriminability\\n\")\nreport_lines.append(\"- A vs B separation: Δρ ≈ 1.29 (0.77 − (−0.52)), massive and non-overlapping across all seeds\")\nreport_lines.append(\"- A vs C separation: Δρ ≈ 0.38, clear but smaller\")\nreport_lines.append(\"- The three patterns are unambiguously distinguishable by ρ(diff, Δδ) alone\")",
    "originalFile": "\"\"\"\nR19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\nTests whether MH-DIF can distinguish capability-like vs contamination-like DIF patterns.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom scipy.stats import chi2 as chi2_dist\nimport time, os, sys\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = os.path.join(ROOT, \"r19_semisynthetic_gradient\")\n\nN_SEEDS = 5\nN_STRATA = 5\nFOC_INJECT_FRAC = 0.30\nITEM_INJECT_FRAC = 0.24\n\n# ════════════════════════════════════════════════════════════════════════════\n#  VECTORIZED MH-DIF — returns per-item results\n# ════════════════════════════════════════════════════════════════════════════\ndef mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item delta_mh, p_value, is_c, direction.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C_mat = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C_mat[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C_mat\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C_mat\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C_mat / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n\n    return delta_j, pval_j, is_c\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  LOAD DATA\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"Loading data...\")\nrm = np.load(f\"{ROOT}/response_matrix.npz\")\nX_sparse = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nidx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\nmodel_names = idx['model_names']\nitem_ids = idx['item_ids']\n\nmeta = pd.read_csv(f\"{ROOT}/model_metadata.csv\")\nname_to_row = {n: i for i, n in enumerate(model_names)}\n\nref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values\nfoc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values\n\nref_idx = np.array([name_to_row[n] for n in ref_models if n in name_to_row])\nfoc_idx = np.array([name_to_row[n] for n in foc_models if n in name_to_row])\n\nN_ref, N_foc, J = len(ref_idx), len(foc_idx), len(item_ids)\nN_inject_models = int(N_foc * FOC_INJECT_FRAC)\nN_inject_items = int(J * ITEM_INJECT_FRAC)\n\nprint(f\"  Ref: {N_ref}, Foc: {N_foc}, Items: {J}\")\nprint(f\"  Injection targets: {N_inject_models} models, {N_inject_items} items\")\n\n# Densify the ref/foc submatrices\nX_ref_base = X_sparse[ref_idx].toarray().astype(np.float64)\nX_foc_base = X_sparse[foc_idx].toarray().astype(np.float64)\n\n# Ref cohort accuracy per item (= item difficulty proxy)\nitem_difficulty = X_ref_base.mean(axis=0)  # shape (J,)\n\nprint(f\"  Item difficulty: mean={item_difficulty.mean():.3f}, \"\n      f\"min={item_difficulty.min():.3f}, max={item_difficulty.max():.3f}\")\n\n# Get MMLU subjects per item for Scheme B (format: subject_name.question_number)\nitem_subjects = np.array([str(iid).rsplit('.', 1)[0] for iid in item_ids])\nunique_subjects = np.unique(item_subjects)\nprint(f\"  Unique subjects: {len(unique_subjects)}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  INJECTION SCHEMES\n# ════════════════════════════════════════════════════════════════════════════\ndef inject_scheme_a(X_foc, inject_model_mask, inject_item_idx, item_diff, rng):\n    \"\"\"Capability-like: injection probability ∝ difficulty (easy items more likely flipped).\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):\n    \"\"\"Contamination-like: uniform injection probability, restricted to 5 random subjects.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,\n                    item_diff, rng, p_const=0.5):\n    \"\"\"Mixed: half items use scheme A, half use scheme B.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    # Scheme A half\n    for j in inject_item_idx_a:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    # Scheme B half\n    for j in inject_item_idx_b:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  BASELINE (no injection)\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Baseline (no injection) ===\")\ndelta_base, pval_base, is_c_base = mh_dif_vec(X_ref_base, X_foc_base, n_strata=N_STRATA)\nc_idx_base = np.where(is_c_base)[0]\nrho_base, _ = stats.spearmanr(item_difficulty[c_idx_base], delta_base[c_idx_base])\nn_c_base = is_c_base.sum()\n# δ > 0 = focal-favoring, δ < 0 = ref-favoring\nn_focal_base = (is_c_base & (delta_base > 0)).sum()\nn_ref_base = (is_c_base & (delta_base < 0)).sum()\nprint(f\"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, \"\n      f\"focal%={n_focal_base/n_c_base*100:.1f}%, ref%={n_ref_base/n_c_base*100:.1f}%, N_C={n_c_base}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running experiments ===\")\nresults = []\nt0 = time.time()\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection models and items (shared across schemes within seed)\n    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)\n    inject_model_mask = np.zeros(N_foc, dtype=bool)\n    inject_model_mask[inject_model_idx] = True\n\n    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)\n\n    # Scheme B: select 5 random subjects, pick injection items from those subjects\n    selected_subjects = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask = np.isin(item_subjects, selected_subjects)\n    subject_item_pool = np.where(subject_mask)[0]\n    n_b_items = min(N_inject_items, len(subject_item_pool))\n    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)\n\n    # Scheme C: split A items in half\n    half = N_inject_items // 2\n    inject_item_idx_c_a = inject_item_idx_all[:half]\n    # For scheme C's B half, pick from 5 random subjects\n    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask_c = np.isin(item_subjects, selected_subjects_c)\n    subject_pool_c = np.where(subject_mask_c)[0]\n    # Exclude items already used by A half\n    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)\n    n_c_b = min(half, len(subject_pool_c))\n    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)\n\n    schemes = {\n        'A_capability': lambda: inject_scheme_a(\n            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),\n        'B_contamination': lambda: inject_scheme_b(\n            X_foc_base, inject_model_mask, inject_item_idx_b, rng),\n        'C_mixed': lambda: inject_scheme_c(\n            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,\n            item_difficulty, rng),\n    }\n\n    for scheme_name, inject_fn in schemes.items():\n        t1 = time.time()\n\n        X_foc_inj, n_flipped = inject_fn()\n\n        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # Delta change from baseline (isolates injection effect)\n        # δ > 0 = focal-favoring; injection flips focal 0→1 → pushes δ positive\n        ddelta = delta_j - delta_base\n\n        # C% among all / injected / non-injected items\n        inj_arr = np.array(sorted(injected_items))\n        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))\n        c_pct_all = is_c.sum() / J * 100\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100\n\n        # ρ(difficulty, δ) among all C items\n        c_idx = np.where(is_c)[0]\n        rho_all = np.nan\n        if len(c_idx) >= 3:\n            rho_all, _ = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n\n        # ρ(difficulty, δ) among injected C items\n        c_inj_mask = is_c & np.isin(np.arange(J), inj_arr)\n        c_inj_idx = np.where(c_inj_mask)[0]\n        rho_inj = np.nan\n        if len(c_inj_idx) >= 3:\n            rho_inj, _ = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])\n\n        # ρ(difficulty, Δδ) among injected items — KEY METRIC isolating injection signal\n        rho_ddelta_inj = np.nan\n        if len(inj_arr) >= 3:\n            rho_ddelta_inj, _ = stats.spearmanr(item_difficulty[inj_arr], ddelta[inj_arr])\n\n        # ρ(difficulty, Δδ) among all items\n        rho_ddelta_all = np.nan\n        if J >= 3:\n            rho_ddelta_all, _ = stats.spearmanr(item_difficulty, ddelta)\n\n        # Direction distribution: δ > 0 = focal-favoring, δ < 0 = ref-favoring\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j > 0)).sum()\n        n_ref_favoring = (is_c & (delta_j < 0)).sum()\n        pct_focal = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # Direction among injected C items\n        n_c_inj = c_inj_mask.sum()\n        n_focal_inj = (c_inj_mask & (delta_j > 0)).sum()\n        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0\n\n        # Newly flagged items (C after injection but not in baseline)\n        newly_c = is_c & ~is_c_base\n        n_newly_c = newly_c.sum()\n        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)\n        n_newly_c_inj = newly_c_inj.sum()\n\n        # Mean Δδ among injected items (injection effect magnitude)\n        mean_ddelta_inj = ddelta[inj_arr].mean()\n\n        # Per-quintile analysis\n        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n        quintile_data = {}\n        for q in range(5):\n            q_mask = (quintile_labels == q)\n            q_items = np.where(q_mask)[0]\n            q_inj_items = np.intersect1d(q_items, inj_arr)\n            q_c = is_c[q_items].sum()\n            q_total = len(q_items)\n            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n            q_focal = (is_c[q_items] & (delta_j[q_items] > 0)).sum()\n            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0\n            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0\n            q_mean_ddelta = ddelta[q_inj_items].mean() if len(q_inj_items) > 0 else 0\n            quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n            quintile_data[f'q{q+1}_n_c'] = q_c\n            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj\n            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)\n            quintile_data[f'q{q+1}_mean_ddelta'] = q_mean_ddelta\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            c_pct_noninj=c_pct_noninj,\n            n_c_total=n_c_total,\n            n_c_inj=n_c_inj,\n            rho_all=rho_all,\n            rho_inj=rho_inj,\n            rho_ddelta_inj=rho_ddelta_inj,\n            rho_ddelta_all=rho_ddelta_all,\n            pct_focal=pct_focal,\n            pct_focal_inj=pct_focal_inj,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            n_newly_c=n_newly_c,\n            n_newly_c_inj=n_newly_c_inj,\n            mean_ddelta_inj=mean_ddelta_inj,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ_all={rho_all:.3f}, ρ_Δδ_inj={rho_ddelta_inj:.3f}, \"\n              f\"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s\")\n\ntotal_time = time.time() - t0\nprint(f\"\\nTotal time: {total_time:.0f}s\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  SAVE RESULTS\n# ════════════════════════════════════════════════════════════════════════════\ndf = pd.DataFrame(results)\ndf.to_csv(os.path.join(OUT, \"semisynthetic_results.csv\"), index=False)\nprint(f\"\\nSaved: semisynthetic_results.csv ({len(df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  GENERATE REPORT\n# ════════════════════════════════════════════════════════════════════════════\nreport_lines = [\"# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\\n\"]\nreport_lines.append(f\"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\\n\")\nreport_lines.append(f\"**Config**: {N_SEEDS} seeds, {N_ref} ref models (2023), \"\n                    f\"{N_foc} foc models (2024), {J} items\\n\")\nreport_lines.append(f\"**Injection**: {N_inject_models} foc models ({FOC_INJECT_FRAC*100:.0f}%), \"\n                    f\"~{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\\n\")\n\nreport_lines.append(f\"\\n## Baseline (no injection)\\n\")\nreport_lines.append(f\"- C%: {n_c_base/J*100:.2f}%\")\nreport_lines.append(f\"- ρ(difficulty, δ_MH) among C: {rho_base:.3f}\")\nreport_lines.append(f\"- % focal-favoring (δ>0): {n_focal_base/n_c_base*100:.1f}%\")\nreport_lines.append(f\"- % ref-favoring (δ<0): {n_ref_base/n_c_base*100:.1f}%\")\nreport_lines.append(f\"- N DIF-C: {n_c_base}\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| C% (non-injected) | {sub['c_pct_noninj'].mean():.2f} ± {sub['c_pct_noninj'].std():.2f} |\")\n    report_lines.append(f\"| ρ(diff, δ) all C | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |\")\n    report_lines.append(f\"| ρ(diff, δ) injected C | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} |\")\n    report_lines.append(f\"| **ρ(diff, Δδ) injected items** | **{sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f}** |\")\n    report_lines.append(f\"| ρ(diff, Δδ) all items | {sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring (all C, δ>0) | {sub['pct_focal'].mean():.1f} ± {sub['pct_focal'].std():.1f} |\")\n    report_lines.append(f\"| % focal-favoring (inj C, δ>0) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |\")\n    report_lines.append(f\"| Mean Δδ (injected items) | {sub['mean_ddelta_inj'].mean():.3f} ± {sub['mean_ddelta_inj'].std():.3f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    report_lines.append(f\"\\n### Quintile Breakdown\\n\")\n    report_lines.append(f\"| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |\")\n    report_lines.append(f\"|----------|----------|----------|---------|---------------|-----|-------|\")\n    for q in range(1, 6):\n        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'mean_ddelta', 'n_c', 'n_inj']}\n        if cols['c_pct'] in sub.columns:\n            report_lines.append(\n                f\"| Q{q} | {sub[cols['c_pct']].mean():.1f} | \"\n                f\"{sub[cols['c_pct_inj']].mean():.1f} | \"\n                f\"{sub[cols['pct_focal']].mean():.1f} | \"\n                f\"{sub[cols['mean_ddelta']].mean():.3f} | \"\n                f\"{sub[cols['n_c']].mean():.0f} | \"\n                f\"{sub[cols['n_inj']].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated\\n\")\nreport_lines.append(\"Δδ = δ_after − δ_baseline isolates the injection-induced DIF shift.\\n\")\nreport_lines.append(f\"| Scheme | ρ(diff, Δδ) injected | ρ(diff, Δδ) all | Expected |\")\nreport_lines.append(f\"|--------|---------------------|-----------------|----------|\")\nfor scheme, expected in [('A_capability', 'positive (easy→more focal DIF)'),\n                         ('B_contamination', '≈ 0 (uniform)'),\n                         ('C_mixed', 'intermediate')]:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"| {scheme} | {sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f} | \"\n                       f\"{sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} | {expected} |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"- **Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring\")\nreport_lines.append(\"- **Δδ = δ_after − δ_before**: positive Δδ means injection shifted item toward focal-favoring\")\nreport_lines.append(\"- **ρ(diff, Δδ)** is the key metric: isolates whether injection-induced DIF shift correlates with difficulty\")\nreport_lines.append(\"- **Scheme A**: injection ∝ difficulty → easy items get larger Δδ → ρ(diff, Δδ) > 0\")\nreport_lines.append(\"- **Scheme B**: uniform p=0.5 injection → Δδ independent of difficulty → ρ(diff, Δδ) ≈ 0\")\nreport_lines.append(\"- **ρ(diff, δ)**: dominated by ~3900 baseline C items, less sensitive to injection\")\n\nreport_text = \"\\n\".join(report_lines) + \"\\n\"\n\nwith open(os.path.join(OUT, \"semisynthetic_gradient_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"Saved: semisynthetic_gradient_report.md\")\nprint(\"\\n\" + report_text)\n",
    "structuredPatch": [
      {
        "oldStart": 443,
        "oldLines": 12,
        "newStart": 443,
        "newLines": 29,
        "lines": [
          "                        f\"{sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} | {expected} |\")",
          " ",
          " report_lines.append(f\"\\n## Interpretation\\n\")",
          "-report_lines.append(\"- **Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring\")",
          "-report_lines.append(\"- **Δδ = δ_after − δ_before**: positive Δδ means injection shifted item toward focal-favoring\")",
          "-report_lines.append(\"- **ρ(diff, Δδ)** is the key metric: isolates whether injection-induced DIF shift correlates with difficulty\")",
          "-report_lines.append(\"- **Scheme A**: injection ∝ difficulty → easy items get larger Δδ → ρ(diff, Δδ) > 0\")",
          "-report_lines.append(\"- **Scheme B**: uniform p=0.5 injection → Δδ independent of difficulty → ρ(diff, Δδ) ≈ 0\")",
          "-report_lines.append(\"- **ρ(diff, δ)**: dominated by ~3900 baseline C items, less sensitive to injection\")",
          "+report_lines.append(\"**Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring. \"",
          "+                    \"Δδ = δ_after − δ_before; positive Δδ = injection shifted item toward focal-favoring.\\n\")",
          "+report_lines.append(\"### Key finding: three schemes produce cleanly separable ρ(diff, Δδ) signatures\\n\")",
          "+report_lines.append(\"1. **Scheme A** (capability-like): ρ(diff, Δδ) ≈ **+0.77**. \"",
          "+                    \"Injection probability ∝ item accuracy → easy items receive more flips → \"",
          "+                    \"larger focal-favoring Δδ on easy items. Strong positive correlation.\")",
          "+report_lines.append(\"2. **Scheme B** (contamination-like): ρ(diff, Δδ) ≈ **−0.52** (NOT ≈ 0 as naively expected). \"",
          "+                    \"Uniform p=0.5 injection gives equal probability per response, but hard items \"",
          "+                    \"have more 0→1 flippable responses (ceiling effect). \"",
          "+                    \"Result: hard items accumulate more flips → larger Δδ on hard items → negative ρ.\")",
          "+report_lines.append(\"3. **Scheme C** (mixed): ρ(diff, Δδ) ≈ **+0.39**, intermediate between A and B, \"",
          "+                    \"as expected from mixing both injection mechanisms.\\n\")",
          "+report_lines.append(\"### Ceiling effect insight\\n\")",
          "+report_lines.append(\"The Scheme B result (ρ ≈ −0.5 instead of 0) reveals that **uniform memorization probability \"",
          "+                    \"does NOT produce uniform DIF**. Easy items have high baseline accuracy → few 0s to flip → \"",
          "+                    \"small Δδ even at p=0.5. Hard items have low accuracy → many 0s → large Δδ. \"",
          "+                    \"This ceiling effect is an inherent property of binary response matrices and means \"",
          "+                    \"the capability vs. contamination distinction is NOT simply 'correlated vs. uncorrelated with difficulty,' \"",
          "+                    \"but rather the SIGN and MAGNITUDE of the difficulty-DIF gradient.\\n\")",
          "+report_lines.append(\"### Discriminability\\n\")",
          "+report_lines.append(\"- A vs B separation: Δρ ≈ 1.29 (0.77 − (−0.52)), massive and non-overlapping across all seeds\")",
          "+report_lines.append(\"- A vs C separation: Δρ ≈ 0.38, clear but smaller\")",
          "+report_lines.append(\"- The three patterns are unambiguously distinguishable by ρ(diff, Δδ) alone\")",
          " ",
          " report_text = \"\\n\".join(report_lines) + \"\\n\"",
          " "
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

_source line 120_

<details open><summary>🔧 Tool call — Bash · `toolu_0111ra7MDHWHqcz7jJ9KaEbB`</summary>

```json
{
  "command": "python3 artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py 2>&1 | tail -50",
  "description": "Re-run and check final report",
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
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "f1a71231-5565-4b1e-baee-b3d413ef1b1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01254LvW5GvhpM2sRu18uRLT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1186,
      "cache_read_input_tokens": 92374,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1186
      },
      "output_tokens": 49,
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

_source line 121_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bu0bnen4r",
  "tool_use_id": "toolu_0111ra7MDHWHqcz7jJ9KaEbB",
  "description": "Re-run and check final report",
  "task_type": "local_bash",
  "uuid": "653ae510-b376-41ba-b4d3-e2f7256e1126",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### System

_source line 122_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bu0bnen4r",
  "tool_use_id": "toolu_0111ra7MDHWHqcz7jJ9KaEbB",
  "status": "completed",
  "output_file": "",
  "summary": "Re-run and check final report",
  "uuid": "8f41be71-169e-4f4c-9973-a746b9f63f3d",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67"
}
```

---

### Tool result

_source line 123 · 2026-05-22T19:01:12.842Z_

<details><summary>↩ Tool result · `toolu_0111ra7MDHWHqcz7jJ9KaEbB`</summary>

```text
| ρ(diff, Δδ) all items | -0.008 ± 0.101 |
| % focal-favoring (all C, δ>0) | 45.8 ± 1.6 |
| % focal-favoring (inj C, δ>0) | 83.8 ± 2.7 |
| N DIF-C items | 4000 ± 67 |
| N DIF-C (injected) | 749 ± 99 |
| Newly flagged C | 626 ± 51 |
| Mean Δδ (injected items) | 0.850 ± 0.039 |
| Responses flipped | 93752 ± 14432 |
| Items injected | 2407 |

### Quintile Breakdown

| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |
|----------|----------|----------|---------|---------------|-----|-------|
| Q1 | 37.2 | 53.8 | 89.2 | 0.600 | 931 | 469 |
| Q2 | 39.1 | 36.4 | 60.0 | 0.554 | 978 | 493 |
| Q3 | 32.6 | 30.1 | 29.5 | 0.926 | 815 | 467 |
| Q4 | 29.7 | 23.6 | 17.8 | 1.169 | 735 | 474 |
| Q5 | 21.4 | 12.5 | 8.3 | 1.029 | 542 | 503 |

## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated

Δδ = δ_after − δ_baseline isolates the injection-induced DIF shift.

| Scheme | ρ(diff, Δδ) injected | ρ(diff, Δδ) all | Expected |
|--------|---------------------|-----------------|----------|
| A_capability | 0.771 ± 0.029 | -0.160 ± 0.131 | positive (easy→more focal DIF) |
| B_contamination | -0.517 ± 0.107 | 0.181 ± 0.136 | ≈ 0 (uniform) |
| C_mixed | 0.394 ± 0.053 | -0.008 ± 0.101 | intermediate |

## Interpretation

**Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring. Δδ = δ_after − δ_before; positive Δδ = injection shifted item toward focal-favoring.

### Key finding: three schemes produce cleanly separable ρ(diff, Δδ) signatures

1. **Scheme A** (capability-like): ρ(diff, Δδ) ≈ **+0.77**. Injection probability ∝ item accuracy → easy items receive more flips → larger focal-favoring Δδ on easy items. Strong positive correlation.
2. **Scheme B** (contamination-like): ρ(diff, Δδ) ≈ **−0.52** (NOT ≈ 0 as naively expected). Uniform p=0.5 injection gives equal probability per response, but hard items have more 0→1 flippable responses (ceiling effect). Result: hard items accumulate more flips → larger Δδ on hard items → negative ρ.
3. **Scheme C** (mixed): ρ(diff, Δδ) ≈ **+0.39**, intermediate between A and B, as expected from mixing both injection mechanisms.

### Ceiling effect insight

The Scheme B result (ρ ≈ −0.5 instead of 0) reveals that **uniform memorization probability does NOT produce uniform DIF**. Easy items have high baseline accuracy → few 0s to flip → small Δδ even at p=0.5. Hard items have low accuracy → many 0s → large Δδ. This ceiling effect is an inherent property of binary response matrices and means the capability vs. contamination distinction is NOT simply 'correlated vs. uncorrelated with difficulty,' but rather the SIGN and MAGNITUDE of the difficulty-DIF gradient.

### Discriminability

- A vs B separation: Δρ ≈ 1.29 (0.77 − (−0.52)), massive and non-overlapping across all seeds
- A vs C separation: Δρ ≈ 0.38, clear but smaller
- The three patterns are unambiguously distinguishable by ρ(diff, Δδ) alone
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "72146c03-dc1e-4536-b2ce-d84a94a3efe5",
  "tool_use_result": {
    "stdout": "| ρ(diff, Δδ) all items | -0.008 ± 0.101 |\n| % focal-favoring (all C, δ>0) | 45.8 ± 1.6 |\n| % focal-favoring (inj C, δ>0) | 83.8 ± 2.7 |\n| N DIF-C items | 4000 ± 67 |\n| N DIF-C (injected) | 749 ± 99 |\n| Newly flagged C | 626 ± 51 |\n| Mean Δδ (injected items) | 0.850 ± 0.039 |\n| Responses flipped | 93752 ± 14432 |\n| Items injected | 2407 |\n\n### Quintile Breakdown\n\n| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |\n|----------|----------|----------|---------|---------------|-----|-------|\n| Q1 | 37.2 | 53.8 | 89.2 | 0.600 | 931 | 469 |\n| Q2 | 39.1 | 36.4 | 60.0 | 0.554 | 978 | 493 |\n| Q3 | 32.6 | 30.1 | 29.5 | 0.926 | 815 | 467 |\n| Q4 | 29.7 | 23.6 | 17.8 | 1.169 | 735 | 474 |\n| Q5 | 21.4 | 12.5 | 8.3 | 1.029 | 542 | 503 |\n\n## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated\n\nΔδ = δ_after − δ_baseline isolates the injection-induced DIF shift.\n\n| Scheme | ρ(diff, Δδ) injected | ρ(diff, Δδ) all | Expected |\n|--------|---------------------|-----------------|----------|\n| A_capability | 0.771 ± 0.029 | -0.160 ± 0.131 | positive (easy→more focal DIF) |\n| B_contamination | -0.517 ± 0.107 | 0.181 ± 0.136 | ≈ 0 (uniform) |\n| C_mixed | 0.394 ± 0.053 | -0.008 ± 0.101 | intermediate |\n\n## Interpretation\n\n**Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring. Δδ = δ_after − δ_before; positive Δδ = injection shifted item toward focal-favoring.\n\n### Key finding: three schemes produce cleanly separable ρ(diff, Δδ) signatures\n\n1. **Scheme A** (capability-like): ρ(diff, Δδ) ≈ **+0.77**. Injection probability ∝ item accuracy → easy items receive more flips → larger focal-favoring Δδ on easy items. Strong positive correlation.\n2. **Scheme B** (contamination-like): ρ(diff, Δδ) ≈ **−0.52** (NOT ≈ 0 as naively expected). Uniform p=0.5 injection gives equal probability per response, but hard items have more 0→1 flippable responses (ceiling effect). Result: hard items accumulate more flips → larger Δδ on hard items → negative ρ.\n3. **Scheme C** (mixed): ρ(diff, Δδ) ≈ **+0.39**, intermediate between A and B, as expected from mixing both injection mechanisms.\n\n### Ceiling effect insight\n\nThe Scheme B result (ρ ≈ −0.5 instead of 0) reveals that **uniform memorization probability does NOT produce uniform DIF**. Easy items have high baseline accuracy → few 0s to flip → small Δδ even at p=0.5. Hard items have low accuracy → many 0s → large Δδ. This ceiling effect is an inherent property of binary response matrices and means the capability vs. contamination distinction is NOT simply 'correlated vs. uncorrelated with difficulty,' but rather the SIGN and MAGNITUDE of the difficulty-DIF gradient.\n\n### Discriminability\n\n- A vs B separation: Δρ ≈ 1.29 (0.77 − (−0.52)), massive and non-overlapping across all seeds\n- A vs C separation: Δρ ≈ 0.38, clear but smaller\n- The three patterns are unambiguously distinguishable by ρ(diff, Δδ) alone",
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

_source line 124_

Results are clean and the experiment is complete. Let me verify the output files exist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "387ac976-44b1-45ca-942b-f8edf90f5edf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MA6gc1FLbCvwf2RS2swyfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1347,
      "cache_read_input_tokens": 93560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1347
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

_source line 125_

<details open><summary>🔧 Tool call — Bash · `toolu_01EFDZ3SKsMA1xVAbHoJPL9u`</summary>

```json
{
  "command": "ls -la artifacts/r19_semisynthetic_gradient/",
  "description": "Verify output files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "3d1045ff-9a7b-451f-b201-8e20ec92ccaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MA6gc1FLbCvwf2RS2swyfN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1347,
      "cache_read_input_tokens": 93560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1347
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

_source line 126 · 2026-05-22T19:01:19.149Z_

<details><summary>↩ Tool result · `toolu_01EFDZ3SKsMA1xVAbHoJPL9u`</summary>

```text
total 56
drwxr-xr-x  2 ubuntu ubuntu  4096 May 22 19:00 .
drwxr-xr-x 89 ubuntu ubuntu  4096 May 22 18:50 ..
-rw-r--r--  1 ubuntu ubuntu 24788 May 22 19:00 semisynthetic_gradient.py
-rw-r--r--  1 ubuntu ubuntu  5964 May 22 19:01 semisynthetic_gradient_report.md
-rw-r--r--  1 ubuntu ubuntu 10700 May 22 19:01 semisynthetic_results.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "3ff72fc0-f9ff-4703-a076-c678a0e4bc43",
  "tool_use_result": {
    "stdout": "total 56\ndrwxr-xr-x  2 ubuntu ubuntu  4096 May 22 19:00 .\ndrwxr-xr-x 89 ubuntu ubuntu  4096 May 22 18:50 ..\n-rw-r--r--  1 ubuntu ubuntu 24788 May 22 19:00 semisynthetic_gradient.py\n-rw-r--r--  1 ubuntu ubuntu  5964 May 22 19:01 semisynthetic_gradient_report.md\n-rw-r--r--  1 ubuntu ubuntu 10700 May 22 19:01 semisynthetic_results.csv",
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

_source line 127_

All three output files produced. Summary:

**R19 Exp 4 — Results**

| Scheme | ρ(diff, Δδ) injected | % focal-favoring (inj C) | C% (all) |
|--------|---------------------|--------------------------|----------|
| **A** (capability-like) | **+0.771 ± 0.029** | 85.2% | 31.9% |
| **B** (contamination-like) | **−0.517 ± 0.107** | 85.7% | 32.1% |
| **C** (mixed) | **+0.394 ± 0.053** | 83.8% | 32.0% |
| Baseline | — | 43.9% | 31.3% |

The key Δδ metric (delta change from baseline) cleanly separates all three injection patterns with Δρ_AB ≈ 1.29 and zero overlap across seeds.

Unexpected but informative: Scheme B gives ρ ≈ −0.5 rather than ≈ 0 due to ceiling effect — hard items have more 0→1 flippable responses, so uniform injection probability produces difficulty-dependent DIF. This means the capability vs. contamination distinction is about the **sign** of the difficulty-DIF gradient (+0.77 vs −0.52), not "correlated vs uncorrelated."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "uuid": "ef501797-14b2-4c09-941f-a5d62bcad585",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWfA4h2BnduwaZ9c4T2Kd5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 94907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 279
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

_source line 128_

All three output files produced. Summary:

**R19 Exp 4 — Results**

| Scheme | ρ(diff, Δδ) injected | % focal-favoring (inj C) | C% (all) |
|--------|---------------------|--------------------------|----------|
| **A** (capability-like) | **+0.771 ± 0.029** | 85.2% | 31.9% |
| **B** (contamination-like) | **−0.517 ± 0.107** | 85.7% | 32.1% |
| **C** (mixed) | **+0.394 ± 0.053** | 83.8% | 32.0% |
| Baseline | — | 43.9% | 31.3% |

The key Δδ metric (delta change from baseline) cleanly separates all three injection patterns with Δρ_AB ≈ 1.29 and zero overlap across seeds.

Unexpected but informative: Scheme B gives ρ ≈ −0.5 rather than ≈ 0 due to ceiling effect — hard items have more 0→1 flippable responses, so uniform injection probability produces difficulty-dependent DIF. This means the capability vs. contamination distinction is about the **sign** of the difficulty-DIF gradient (+0.77 vs −0.52), not "correlated vs uncorrelated."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 779552,
  "duration_api_ms": 726825,
  "num_turns": 32,
  "stop_reason": "end_turn",
  "session_id": "59e5e155-b509-485f-afa6-f4a63c381a67",
  "total_cost_usd": 2.4469819500000005,
  "usage": {
    "input_tokens": 33,
    "cache_creation_input_tokens": 83345,
    "cache_read_input_tokens": 1755619,
    "output_tokens": 39252,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 83345,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 348,
        "cache_read_input_tokens": 94907,
        "cache_creation_input_tokens": 279,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 279
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1735,
      "outputTokens": 4861,
      "cacheReadInputTokens": 132062,
      "cacheCreationInputTokens": 22044,
      "webSearchRequests": 0,
      "costUSD": 0.0668012,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 33,
      "outputTokens": 39252,
      "cacheReadInputTokens": 1755619,
      "cacheCreationInputTokens": 83345,
      "webSearchRequests": 0,
      "costUSD": 2.3801807500000005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d9916b84-2eb9-4a19-9e66-ae3d5104896e"
}
```

</details>

---
