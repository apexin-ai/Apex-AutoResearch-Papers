# code r19w2 k30 40 50 injection

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_code_r19w2_k30_40_50_injection_20260523T170454.log`
- **Structured JSON:** [`12d983cb024da67851d0.json`](../../sessions/12/12d983cb024da67851d0.json)

## Before a recorded user message

29 recorded events

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
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
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
  "uuid": "02ff8548-55b0-4418-b18d-530eb1e47f2e",
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
    "resetsAt": 1779570000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ebc41862-7840-40a8-8ee1-3dccfba28ee2",
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825"
}
```

---

### Assistant

_source line 4_

I'll start by reading the existing script to understand its logic, then create the extended version.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "0c0a3529-6c5f-42a3-910a-10cbe5e00342",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPCjGveF7PHPbrjb1XKDBu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13292,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13292
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_0199XRwNXrmwddj84mQxUXtc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "0129a45e-fc7f-4a01-94a9-b34012754a20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPCjGveF7PHPbrjb1XKDBu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13292,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13292
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

_source line 6 · 2026-05-23T17:05:07.563Z_

<details><summary>↩ Tool result · `toolu_0199XRwNXrmwddj84mQxUXtc`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_034: Multi-Subject Simultaneous Injection Experiment
4	
5	Tests Proposition 1 (ΔFPR=0) robustness under multi-subject contamination.
6	When k subjects are simultaneously injected, the cross-subject matching variable
7	(total score on remaining 57-k uninjected subjects) degrades. ΔFPR(k) on
8	non-target subjects should increase with k, revealing the validity boundary.
9	
10	Inputs:
11	  - artifacts/response_matrix.npz         (5227 × 12508 sparse binary)
12	  - artifacts/response_matrix_index.npz   (model_names, item_ids)
13	  - artifacts/model_metadata.csv          (cohort_temporal, accuracy, ...)
14	  - artifacts/item_metadata.csv           (item_id, subject, ...)
15	
16	Outputs:
17	  - multi_subject_injection_results.csv   (per-target-subject DIF results)
18	  - non_target_fpr_results.csv            (FPR on uninjected subjects)
19	  - summary_by_k.csv                      (aggregated ΔFPR/ΔTPR by k,p)
20	  - plan_034_report.md
21	
22	Dependencies: numpy, pandas, scipy
23	"""
24	
25	import numpy as np
26	import pandas as pd
27	from scipy.sparse import load_npz
28	from scipy.stats import chi2 as chi2_dist
29	from pathlib import Path
30	import time
31	import warnings
32	import argparse
33	
34	warnings.filterwarnings("ignore", category=RuntimeWarning)
35	
36	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
37	OUT = BASE / "plan_034_multi_subject_injection"
38	OUT.mkdir(exist_ok=True)
39	
40	KS = [1, 2, 3, 5, 10, 20]
41	PS = [0.1, 0.3, 0.5]
42	N_SEEDS = 5
43	N_STRATA = 5
44	MIN_PER_STRATUM = 5
45	
46	
47	# ════════════════════════════════════════════════════════════════════════════
48	#  MH-DIF CORE (from plan_016 with strata merging + external score support)
49	# ════════════════════════════════════════════════════════════════════════════
50	def purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,
51	                    external_scores_foc=None, min_per_stratum=5):
52	    J = X_ref.shape[1]
53	    use_external = external_scores_ref is not None
54	
55	    if not use_external:
56	        tot_ref = X_ref.sum(axis=1).astype(np.float64)
57	        tot_foc = X_foc.sum(axis=1).astype(np.float64)
58	
59	    rows = []
60	    for j in range(J):
61	        if use_external:
62	            s_ref = external_scores_ref.astype(np.float64)
63	            s_foc = external_scores_foc.astype(np.float64)
64	        else:
65	            s_ref = tot_ref - X_ref[:, j].astype(np.float64)
66	            s_foc = tot_foc - X_foc[:, j].astype(np.float64)
67	
68	        s_all = np.concatenate([s_ref, s_foc])
69	        groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])
70	
71	        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
72	        if len(edges) < 2:
73	            rows.append(_nan_row(j))
74	            continue
75	
76	        n_bins = len(edges) - 1
77	        k_all = np.digitize(s_all, edges[1:-1])
78	        strata_labels = _merge_small_strata(k_all, groups_all, n_bins, min_per_stratum)
79	
80	        R = S = 0.0
81	        sum_diff = 0.0
82	        sum_var = 0.0
83	        pr = ps_qr = qs = 0.0
84	        n_ok = 0
85	
86	        x_all = np.concatenate([X_ref[:, j], X_foc[:, j]])
87	
88	        for k in np.unique(strata_labels):
89	            mask_k = (strata_labels == k)
90	            mask_ref = mask_k & (groups_all == 0)
91	            mask_foc = mask_k & (groups_all == 1)
92	
93	            n1 = int(mask_ref.sum())
94	            n0 = int(mask_foc.sum())
95	            if n1 == 0 or n0 == 0:
96	                continue
97	
98	            A = float(x_all[mask_ref].sum())
99	            B = float(n1 - A)
100	            C = float(x_all[mask_foc].sum())
101	            D = float(n0 - C)
102	            Nk = float(n1 + n0)
103	            m1 = A + C
104	            m0 = B + D
105	
106	            if m1 == 0 or m0 == 0 or Nk <= 1:
107	                continue
108	            n_ok += 1
109	
110	            Rk = A * D / Nk
111	            Sk = B * C / Nk
112	            R += Rk
113	            S += Sk
114	
115	            EA = n1 * m1 / Nk
116	            sum_diff += A - EA
117	            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))
118	
119	            Pk = (A + D) / Nk
120	            Qk = (B + C) / Nk
121	            pr += Pk * Rk
122	            ps_qr += Pk * Sk + Qk * Rk
123	            qs += Qk * Sk
124	
125	        if n_ok == 0 or (R == 0 and S == 0):
126	            rows.append(_nan_row(j))
127	            continue
128	
129	        if S == 0:
130	            alpha, delta, se = np.inf, -np.inf, np.nan
131	        elif R == 0:
132	            alpha, delta, se = 0.0, np.inf, np.nan
133	        else:
134	            alpha = R / S
135	            delta = -2.35 * np.log(alpha)
136	            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)
137	            se = 2.35 * np.sqrt(v) if v > 0 else np.nan
138	
139	        if sum_var > 0:
140	            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
141	            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
142	        else:
143	            chi2_stat = pval = np.nan
144	
145	        ad = abs(delta) if np.isfinite(delta) else np.inf
146	        if ad < 1.0:
147	            ets = "A"
148	        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:
149	            ets = "C"
150	        else:
151	            ets = "B"
152	
153	        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,
154	                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets,
155	                         n_strata_used=n_ok))
156	
157	    return pd.DataFrame(rows)
158	
159	
160	def _nan_row(j):
161	    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,
162	                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class="A",
163	                n_strata_used=0)
164	
165	
166	def _merge_small_strata(k_all, groups_all, n_bins, min_n):
167	    labels = k_all.copy()
168	    merged = True
169	    while merged:
170	        merged = False
171	        unique_strata = sorted(np.unique(labels))
172	        for i, k in enumerate(unique_strata):
173	            mask_k = (labels == k)
174	            n_ref = int((mask_k & (groups_all == 0)).sum())
175	            n_foc = int((mask_k & (groups_all == 1)).sum())
176	            if n_ref < min_n or n_foc < min_n:
177	                if i + 1 < len(unique_strata):
178	                    next_k = unique_strata[i + 1]
179	                    labels[labels == next_k] = k
180	                elif i > 0:
181	                    prev_k = unique_strata[i - 1]
182	                    labels[labels == k] = prev_k
183	                merged = True
184	                break
185	    return labels
186	
187	
188	# ════════════════════════════════════════════════════════════════════════════
189	#  DATA LOADING
190	# ════════════════════════════════════════════════════════════════════════════
191	def load_data():
192	    mat = load_npz(BASE / "response_matrix.npz")
193	    idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
194	    model_names = idx["model_names"]
195	    item_ids = idx["item_ids"]
196	    item2col = {iid: i for i, iid in enumerate(item_ids)}
197	
198	    model_meta = pd.read_csv(BASE / "model_metadata.csv")
199	    item_meta = pd.read_csv(BASE / "item_metadata.csv")
200	    name2row = {n: i for i, n in enumerate(model_names)}
201	
202	    # Temporal cohorts
203	    ref_names = model_meta.loc[model_meta["cohort_temporal"] == "2023", "model_name"]
204	    foc_names = model_meta.loc[model_meta["cohort_temporal"] == "2024", "model_name"]
205	    ref_rows = np.array([name2row[n] for n in ref_names if n in name2row])
206	    foc_rows = np.array([name2row[n] for n in foc_names if n in name2row])
207	
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
238	
239	    # Precompute per-subject total scores (original matrix) for ref/foc
240	    # Enables O(1) matching variable via subtraction instead of re-slicing
241	    subj_totals_ref = {}
242	    subj_totals_foc = {}
243	    for subj in subjects:
244	        s_cols = subject_cols[subj]
245	        subj_totals_ref[subj] = np.asarray(mat[ref_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)
246	        subj_totals_foc[subj] = np.asarray(mat[foc_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)
247	
248	    # Full total across all subjects
249	    full_total_ref = sum(subj_totals_ref.values())
250	    full_total_foc = sum(subj_totals_foc.values())
251	
252	    # Precompute dense submatrices per subject for ref/foc (avoids repeated sparse→dense)
253	    subj_X_ref = {}
254	    subj_X_foc = {}
255	    for subj in subjects:
256	        s_cols = subject_cols[subj]
257	        subj_X_ref[subj] = mat[ref_rows][:, s_cols].toarray().astype(np.int8)
258	        subj_X_foc[subj] = mat[foc_rows][:, s_cols].toarray().astype(np.int8)
259	
260	    # ── Phase 1: baseline (p=0) per-subject FPR with cross-subject matching ──
261	    print("Computing baseline FPR (p=0) for all subjects...")
262	    baseline_fpr = {}
263	    baseline_n_c = {}
264	    for subj in subjects:
265	        s_cols = subject_cols[subj]
266	        cross_ref = full_total_ref - subj_totals_ref[subj]
267	        cross_foc = full_total_foc - subj_totals_foc[subj]
268	
269	        n_strata = 3 if len(s_cols) < 100 else N_STRATA
270	        dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,
271	                              external_scores_ref=cross_ref,
272	                              external_scores_foc=cross_foc,
273	                              min_per_stratum=MIN_PER_STRATUM)
274	        n_c = int((dif["ets_class"] == "C").sum())
275	        fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0
276	        baseline_fpr[subj] = fpr
277	        baseline_n_c[subj] = n_c
278	
279	    print(f"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}")
280	
281	    # ── Phase 2: injection runs ──
282	    target_rows_list = []
283	    non_target_rows_list = []
284	    total_runs = len(ks) * len(ps) * n_seeds
285	    run_i = 0
286	
287	    for k in ks:
288	        for p in ps:
289	            for seed in range(1, n_seeds + 1):
290	                run_i += 1
291	                rng = np.random.RandomState(seed)
292	                target_subjects = sorted(rng.choice(subjects, size=k, replace=False))
293	                non_target_subjects = [s for s in subjects if s not in target_subjects]
294	
295	                # Build injected matrix columns for target subjects
296	                # Collect all target columns for injection
297	                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])
298	
299	                # Inject: flip incorrect→correct for focal inject models on target items
300	                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)
301	                n_flipped = 0
302	                if p > 0:
303	                    block = mat_dense_targets[foc_inject_rows]
304	                    zeros = (block == 0)
305	                    flip_mask = zeros & (rng.random(block.shape) < p)
306	                    n_flipped = int(flip_mask.sum())
307	                    mat_dense_targets[foc_inject_rows] = block + flip_mask.astype(np.int8)
308	
309	                # Precompute totals for matching variable construction
310	                # non_target_total = full_total - sum(target subject originals)
311	                non_target_total_ref = full_total_ref - sum(subj_totals_ref[s] for s in target_subjects)
312	                non_target_total_foc = full_total_foc - sum(subj_totals_foc[s] for s in target_subjects)
313	
314	                # Injected target total (all target subjects combined, after injection)
315	                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)
316	
317	                # Per-target-subject injected totals (for leave-one-out matching)
318	                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}
319	                target_subj_injected = {}
320	                for s in target_subjects:
321	                    local_idxs = np.array([target_col_to_local[c] for c in subject_cols[s]])
322	                    target_subj_injected[s] = mat_dense_targets[:, local_idxs].sum(axis=1).astype(np.float64)
323	
324	                elapsed = time.time() - t0
325	                print(f"  [{run_i}/{total_runs}] k={k} p={p} seed={seed} "
326	                      f"flipped={n_flipped} ({elapsed:.0f}s)")
327	
328	                # ── DIF on each target subject ──
329	                for subj in target_subjects:
330	                    s_cols = subject_cols[subj]
331	                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])
332	                    X_subj_inj = mat_dense_targets[:, local_idxs]
333	
334	                    X_ref_s = X_subj_inj[ref_rows]
335	                    X_foc_s = X_subj_inj[foc_rows]
336	
337	                    # Matching = non_target_total + other_target_injected
338	                    other_target_inj = injected_target_total - target_subj_injected[subj]
339	                    match_ref = non_target_total_ref + other_target_inj[ref_rows]
340	                    match_foc = non_target_total_foc + other_target_inj[foc_rows]
341	
342	                    n_strata = 3 if len(s_cols) < 100 else N_STRATA
343	                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,
344	                                          external_scores_ref=match_ref,
345	                                          external_scores_foc=match_foc,
346	                                          min_per_stratum=MIN_PER_STRATUM)
347	
348	                    n_c = int((dif["ets_class"] == "C").sum())
349	                    # All items in target subject are "contaminated" (injected)
350	                    tpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0
351	                    delta_tpr = tpr - baseline_fpr[subj]  # baseline is p=0 rate
352	
353	                    target_rows_list.append(dict(
354	                        k=k, p=p, seed=seed, target_subject=subj,
355	                        n_items=len(s_cols), tpr=tpr, fpr=np.nan,
356	                        delta_tpr=delta_tpr, delta_fpr=np.nan,
357	                        n_target_c=n_c, n_clean_c=np.nan
358	                    ))
359	
360	                # ── DIF on each non-target subject (FPR measurement) ──
361	                # Sample non-targets to keep runtime manageable for large k
362	                # For k≤5, test all; for k>5, test 20 random non-targets
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
379	                    dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,
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
398	
399	    nontarget_df = pd.DataFrame(non_target_rows_list)
400	    nontarget_df.to_csv(OUT / "non_target_fpr_results.csv", index=False)
401	
402	    # ── Summary by k,p ──
403	    summary_rows = []
404	    for k in ks:
405	        for p_val in ps:
406	            t_sub = target_df[(target_df["k"] == k) & (target_df["p"] == p_val)]
407	            nt_sub = nontarget_df[(nontarget_df["k"] == k) & (nontarget_df["p"] == p_val)]
408	
409	            mean_tpr = t_sub["tpr"].mean() if len(t_sub) > 0 else np.nan
410	            mean_delta_tpr = t_sub["delta_tpr"].mean() if len(t_sub) > 0 else np.nan
411	            std_delta_tpr = t_sub.groupby("seed")["delta_tpr"].mean().std() if len(t_sub) > 0 else np.nan
412	
413	            mean_fpr_nt = nt_sub["fpr"].mean() if len(nt_sub) > 0 else np.nan
414	            mean_delta_fpr_nt = nt_sub["delta_fpr"].mean() if len(nt_sub) > 0 else np.nan
415	            std_delta_fpr_nt = nt_sub.groupby("seed")["delta_fpr"].mean().std() if len(nt_sub) > 0 else np.nan
416	
417	            summary_rows.append(dict(
418	                k=k, p=p_val,
419	                mean_tpr_target=round(mean_tpr, 4),
420	                mean_delta_tpr=round(mean_delta_tpr, 4),
421	                std_delta_tpr=round(std_delta_tpr, 4) if not np.isnan(std_delta_tpr) else np.nan,
422	                mean_fpr_non_target=round(mean_fpr_nt, 4),
423	                mean_delta_fpr_non_target=round(mean_delta_fpr_nt, 4),
424	                std_delta_fpr_non_target=round(std_delta_fpr_nt, 4) if not np.isnan(std_delta_fpr_nt) else np.nan,
425	            ))
426	
427	    summary_df = pd.DataFrame(summary_rows)
428	    summary_df.to_csv(OUT / "summary_by_k.csv", index=False)
429	
430	    elapsed = time.time() - t0
431	    print(f"\nDone in {elapsed:.0f}s. Saved to {OUT}")
432	    print("\nSummary:")
433	    print(summary_df.to_string(index=False))
434	
435	    return target_df, nontarget_df, summary_df
436	
437	
438	def generate_report(target_df, nontarget_df, summary_df):
439	    lines = [
440	        "# Plan 034: Multi-Subject Simultaneous Injection — Report",
441	        "",
442	        "## Method",
443	        "",
444	        "We test Proposition 1's robustness boundary by simultaneously injecting",
445	        "differential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).",
446	        "For each (k, p, seed) combination:",
447	        "",
448	        "1. Randomly select k target subjects from 57 MMLU subjects",
449	        "2. For each item in the k target subjects, flip incorrect→correct responses",
450	        "   in the focal group (2024 models within accuracy overlap) with probability p",
451	        "3. Compute cross-subject MH-DIF for each target and non-target subject",
452	        "   - Matching variable = total score on all subjects EXCEPT the tested one",
453	        "   - For target subjects: matching includes injected scores from other targets",
454	        "   - For non-target subjects: matching includes all injected target scores",
455	        "4. Measure TPR on target subjects and FPR on non-target subjects",
456	        "",
457	        f"Grid: k ∈ {{{','.join(map(str, KS))}}}, p ∈ {{{','.join(map(str, PS))}}}, "
458	        f"5 seeds per combination = {len(KS)*len(PS)*N_SEEDS} runs",
459	        "",
460	        "## Core Results: ΔFPR by k and p",
461	        "",
462	    ]
463	
464	    # Summary table
465	    lines.append("### Target Subjects (TPR)")
466	    lines.append("")
467	    lines.append("| k | p | Mean TPR | Mean ΔTPR | SD(ΔTPR) |")
468	    lines.append("|---|---|----------|-----------|----------|")
469	    for _, row in summary_df.iterrows():
470	        lines.append(f"| {row['k']} | {row['p']} | {row['mean_tpr_target']:.4f} | "
471	                      f"{row['mean_delta_tpr']:.4f} | "
472	                      f"{row['std_delta_tpr']:.4f} |")
473	    lines.append("")
474	
475	    lines.append("### Non-Target Subjects (FPR — key result)")
476	    lines.append("")
477	    lines.append("| k | p | Mean FPR | Mean ΔFPR | SD(ΔFPR) |")
478	    lines.append("|---|---|----------|-----------|----------|")
479	    for _, row in summary_df.iterrows():
480	        lines.append(f"| {row['k']} | {row['p']} | {row['mean_fpr_non_target']:.4f} | "
481	                      f"{row['mean_delta_fpr_non_target']:.4f} | "
482	                      f"{row['std_delta_fpr_non_target']:.4f} |")
483	    lines.append("")
484	
485	    # Key findings
486	    lines.append("## Key Findings")
487	    lines.append("")
488	
489	    # Find threshold where ΔFPR becomes notable
490	    for p_val in PS:
491	        sub = summary_df[summary_df["p"] == p_val]
492	        significant_k = sub[sub["mean_delta_fpr_non_target"].abs() > 0.01]
493	        if len(significant_k) > 0:
494	            first_k = int(significant_k.iloc[0]["k"])
495	            lines.append(f"- **p={p_val}**: Non-target ΔFPR exceeds 0.01 at k={first_k}")
496	        else:
497	            lines.append(f"- **p={p_val}**: Non-target ΔFPR stays below 0.01 for all k tested")
498	
499	    lines.append("")
500	    lines.append("## Interpretation")
501	    lines.append("")
502	    lines.append("Proposition 1 guarantees ΔFPR=0 when the matching variable is uncontaminated.")
503	    lines.append("As k increases, more of the cross-subject total score is contaminated,")
504	    lines.append("violating the proposition's assumption. The k at which ΔFPR becomes")
505	    lines.append("practically significant marks the validity boundary of cross-subject DIF auditing.")
506	    lines.append("")
507	
508	    report_path = OUT / "plan_034_report.md"
509	    report_path.write_text("\n".join(lines))
510	    print(f"Report saved to {report_path}")
511	
512	
513	if __name__ == "__main__":
514	    parser = argparse.ArgumentParser(description="Plan 034: Multi-Subject Injection")
515	    parser.add_argument("--quick", action="store_true",
516	                        help="Quick validation: k∈{1,5,20}, p=0.3, seed=1")
517	    args = parser.parse_args()
518	
519	    if args.quick:
520	        target_df, nontarget_df, summary_df = run_experiment(
521	            ks=[1, 5, 20], ps=[0.3], n_seeds=1)
522	    else:
523	        target_df, nontarget_df, summary_df = run_experiment()
524	
525	    generate_report(target_df, nontarget_df, summary_df)
526	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "c4d3dc05-4ef1-4296-8dff-14d9384c7eec",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nplan_034: Multi-Subject Simultaneous Injection Experiment\n\nTests Proposition 1 (ΔFPR=0) robustness under multi-subject contamination.\nWhen k subjects are simultaneously injected, the cross-subject matching variable\n(total score on remaining 57-k uninjected subjects) degrades. ΔFPR(k) on\nnon-target subjects should increase with k, revealing the validity boundary.\n\nInputs:\n  - artifacts/response_matrix.npz         (5227 × 12508 sparse binary)\n  - artifacts/response_matrix_index.npz   (model_names, item_ids)\n  - artifacts/model_metadata.csv          (cohort_temporal, accuracy, ...)\n  - artifacts/item_metadata.csv           (item_id, subject, ...)\n\nOutputs:\n  - multi_subject_injection_results.csv   (per-target-subject DIF results)\n  - non_target_fpr_results.csv            (FPR on uninjected subjects)\n  - summary_by_k.csv                      (aggregated ΔFPR/ΔTPR by k,p)\n  - plan_034_report.md\n\nDependencies: numpy, pandas, scipy\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\nimport warnings\nimport argparse\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_034_multi_subject_injection\"\nOUT.mkdir(exist_ok=True)\n\nKS = [1, 2, 3, 5, 10, 20]\nPS = [0.1, 0.3, 0.5]\nN_SEEDS = 5\nN_STRATA = 5\nMIN_PER_STRATUM = 5\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE (from plan_016 with strata merging + external score support)\n# ════════════════════════════════════════════════════════════════════════════\ndef purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,\n                    external_scores_foc=None, min_per_stratum=5):\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])\n\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n\n        n_bins = len(edges) - 1\n        k_all = np.digitize(s_all, edges[1:-1])\n        strata_labels = _merge_small_strata(k_all, groups_all, n_bins, min_per_stratum)\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        x_all = np.concatenate([X_ref[:, j], X_foc[:, j]])\n\n        for k in np.unique(strata_labels):\n            mask_k = (strata_labels == k)\n            mask_ref = mask_k & (groups_all == 0)\n            mask_foc = mask_k & (groups_all == 1)\n\n            n1 = int(mask_ref.sum())\n            n0 = int(mask_foc.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(x_all[mask_ref].sum())\n            B = float(n1 - A)\n            C = float(x_all[mask_foc].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else np.inf\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets,\n                         n_strata_used=n_ok))\n\n    return pd.DataFrame(rows)\n\n\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\",\n                n_strata_used=0)\n\n\ndef _merge_small_strata(k_all, groups_all, n_bins, min_n):\n    labels = k_all.copy()\n    merged = True\n    while merged:\n        merged = False\n        unique_strata = sorted(np.unique(labels))\n        for i, k in enumerate(unique_strata):\n            mask_k = (labels == k)\n            n_ref = int((mask_k & (groups_all == 0)).sum())\n            n_foc = int((mask_k & (groups_all == 1)).sum())\n            if n_ref < min_n or n_foc < min_n:\n                if i + 1 < len(unique_strata):\n                    next_k = unique_strata[i + 1]\n                    labels[labels == next_k] = k\n                elif i > 0:\n                    prev_k = unique_strata[i - 1]\n                    labels[labels == k] = prev_k\n                merged = True\n                break\n    return labels\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\ndef load_data():\n    mat = load_npz(BASE / \"response_matrix.npz\")\n    idx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n    item2col = {iid: i for i, iid in enumerate(item_ids)}\n\n    model_meta = pd.read_csv(BASE / \"model_metadata.csv\")\n    item_meta = pd.read_csv(BASE / \"item_metadata.csv\")\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    # Temporal cohorts\n    ref_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"model_name\"]\n    foc_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"model_name\"]\n    ref_rows = np.array([name2row[n] for n in ref_names if n in name2row])\n    foc_rows = np.array([name2row[n] for n in foc_names if n in name2row])\n\n    # Focal inject subset: 2024 models in accuracy overlap with 2023\n    ref_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\n    foc_df = model_meta[model_meta[\"cohort_temporal\"] == \"2024\"]\n    t_min = max(ref_acc.min(), foc_df[\"accuracy\"].min())\n    t_max = min(ref_acc.max(), foc_df[\"accuracy\"].max())\n    foc_inject_mask = (foc_df[\"accuracy\"] >= t_min) & (foc_df[\"accuracy\"] <= t_max)\n    foc_inject_rows = np.array([name2row[n] for n in foc_df.loc[foc_inject_mask, \"model_name\"]\n                                if n in name2row])\n\n    # Build subject → column indices mapping\n    subject_cols = {}\n    subjects = sorted(item_meta[\"subject\"].unique())\n    for subj in subjects:\n        ids = item_meta.loc[item_meta[\"subject\"] == subj, \"item_id\"].values\n        cols = np.array([item2col[iid] for iid in ids if iid in item2col])\n        subject_cols[subj] = cols\n\n    return mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MAIN EXPERIMENT\n# ════════════════════════════════════════════════════════════════════════════\ndef run_experiment(ks=KS, ps=PS, n_seeds=N_SEEDS):\n    t0 = time.time()\n    mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols = load_data()\n    print(f\"Data loaded: {len(ref_rows)} ref, {len(foc_rows)} foc, \"\n          f\"{len(foc_inject_rows)} foc_inject, {len(subjects)} subjects\")\n\n    all_cols = np.concatenate([subject_cols[s] for s in subjects])\n\n    # Precompute per-subject total scores (original matrix) for ref/foc\n    # Enables O(1) matching variable via subtraction instead of re-slicing\n    subj_totals_ref = {}\n    subj_totals_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_totals_ref[subj] = np.asarray(mat[ref_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n        subj_totals_foc[subj] = np.asarray(mat[foc_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n\n    # Full total across all subjects\n    full_total_ref = sum(subj_totals_ref.values())\n    full_total_foc = sum(subj_totals_foc.values())\n\n    # Precompute dense submatrices per subject for ref/foc (avoids repeated sparse→dense)\n    subj_X_ref = {}\n    subj_X_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_X_ref[subj] = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n        subj_X_foc[subj] = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n    # ── Phase 1: baseline (p=0) per-subject FPR with cross-subject matching ──\n    print(\"Computing baseline FPR (p=0) for all subjects...\")\n    baseline_fpr = {}\n    baseline_n_c = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        cross_ref = full_total_ref - subj_totals_ref[subj]\n        cross_foc = full_total_foc - subj_totals_foc[subj]\n\n        n_strata = 3 if len(s_cols) < 100 else N_STRATA\n        dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,\n                              external_scores_ref=cross_ref,\n                              external_scores_foc=cross_foc,\n                              min_per_stratum=MIN_PER_STRATUM)\n        n_c = int((dif[\"ets_class\"] == \"C\").sum())\n        fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n        baseline_fpr[subj] = fpr\n        baseline_n_c[subj] = n_c\n\n    print(f\"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}\")\n\n    # ── Phase 2: injection runs ──\n    target_rows_list = []\n    non_target_rows_list = []\n    total_runs = len(ks) * len(ps) * n_seeds\n    run_i = 0\n\n    for k in ks:\n        for p in ps:\n            for seed in range(1, n_seeds + 1):\n                run_i += 1\n                rng = np.random.RandomState(seed)\n                target_subjects = sorted(rng.choice(subjects, size=k, replace=False))\n                non_target_subjects = [s for s in subjects if s not in target_subjects]\n\n                # Build injected matrix columns for target subjects\n                # Collect all target columns for injection\n                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])\n\n                # Inject: flip incorrect→correct for focal inject models on target items\n                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    block = mat_dense_targets[foc_inject_rows]\n                    zeros = (block == 0)\n                    flip_mask = zeros & (rng.random(block.shape) < p)\n                    n_flipped = int(flip_mask.sum())\n                    mat_dense_targets[foc_inject_rows] = block + flip_mask.astype(np.int8)\n\n                # Precompute totals for matching variable construction\n                # non_target_total = full_total - sum(target subject originals)\n                non_target_total_ref = full_total_ref - sum(subj_totals_ref[s] for s in target_subjects)\n                non_target_total_foc = full_total_foc - sum(subj_totals_foc[s] for s in target_subjects)\n\n                # Injected target total (all target subjects combined, after injection)\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                # Per-target-subject injected totals (for leave-one-out matching)\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}\n                target_subj_injected = {}\n                for s in target_subjects:\n                    local_idxs = np.array([target_col_to_local[c] for c in subject_cols[s]])\n                    target_subj_injected[s] = mat_dense_targets[:, local_idxs].sum(axis=1).astype(np.float64)\n\n                elapsed = time.time() - t0\n                print(f\"  [{run_i}/{total_runs}] k={k} p={p} seed={seed} \"\n                      f\"flipped={n_flipped} ({elapsed:.0f}s)\")\n\n                # ── DIF on each target subject ──\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    # Matching = non_target_total + other_target_injected\n                    other_target_inj = injected_target_total - target_subj_injected[subj]\n                    match_ref = non_target_total_ref + other_target_inj[ref_rows]\n                    match_foc = non_target_total_foc + other_target_inj[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    # All items in target subject are \"contaminated\" (injected)\n                    tpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_tpr = tpr - baseline_fpr[subj]  # baseline is p=0 rate\n\n                    target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, target_subject=subj,\n                        n_items=len(s_cols), tpr=tpr, fpr=np.nan,\n                        delta_tpr=delta_tpr, delta_fpr=np.nan,\n                        n_target_c=n_c, n_clean_c=np.nan\n                    ))\n\n                # ── DIF on each non-target subject (FPR measurement) ──\n                # Sample non-targets to keep runtime manageable for large k\n                # For k≤5, test all; for k>5, test 20 random non-targets\n                if len(non_target_subjects) <= 20:\n                    test_nontargets = non_target_subjects\n                else:\n                    test_nontargets = sorted(rng.choice(non_target_subjects,\n                                                        size=20, replace=False))\n\n                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n\n                    # Matching = (non_target_total - this subject) + all injected target total\n                    match_ref = (non_target_total_ref - subj_totals_ref[subj]\n                                 + injected_target_total[ref_rows])\n                    match_foc = (non_target_total_foc - subj_totals_foc[subj]\n                                 + injected_target_total[foc_rows])\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_fpr = fpr - baseline_fpr[subj]\n\n                    non_target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, non_target_subject=subj,\n                        n_items=len(s_cols),\n                        fpr=fpr, baseline_fpr=baseline_fpr[subj],\n                        delta_fpr=delta_fpr\n                    ))\n\n    # ── Save results ──\n    target_df = pd.DataFrame(target_rows_list)\n    target_df.to_csv(OUT / \"multi_subject_injection_results.csv\", index=False)\n\n    nontarget_df = pd.DataFrame(non_target_rows_list)\n    nontarget_df.to_csv(OUT / \"non_target_fpr_results.csv\", index=False)\n\n    # ── Summary by k,p ──\n    summary_rows = []\n    for k in ks:\n        for p_val in ps:\n            t_sub = target_df[(target_df[\"k\"] == k) & (target_df[\"p\"] == p_val)]\n            nt_sub = nontarget_df[(nontarget_df[\"k\"] == k) & (nontarget_df[\"p\"] == p_val)]\n\n            mean_tpr = t_sub[\"tpr\"].mean() if len(t_sub) > 0 else np.nan\n            mean_delta_tpr = t_sub[\"delta_tpr\"].mean() if len(t_sub) > 0 else np.nan\n            std_delta_tpr = t_sub.groupby(\"seed\")[\"delta_tpr\"].mean().std() if len(t_sub) > 0 else np.nan\n\n            mean_fpr_nt = nt_sub[\"fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            mean_delta_fpr_nt = nt_sub[\"delta_fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            std_delta_fpr_nt = nt_sub.groupby(\"seed\")[\"delta_fpr\"].mean().std() if len(nt_sub) > 0 else np.nan\n\n            summary_rows.append(dict(\n                k=k, p=p_val,\n                mean_tpr_target=round(mean_tpr, 4),\n                mean_delta_tpr=round(mean_delta_tpr, 4),\n                std_delta_tpr=round(std_delta_tpr, 4) if not np.isnan(std_delta_tpr) else np.nan,\n                mean_fpr_non_target=round(mean_fpr_nt, 4),\n                mean_delta_fpr_non_target=round(mean_delta_fpr_nt, 4),\n                std_delta_fpr_non_target=round(std_delta_fpr_nt, 4) if not np.isnan(std_delta_fpr_nt) else np.nan,\n            ))\n\n    summary_df = pd.DataFrame(summary_rows)\n    summary_df.to_csv(OUT / \"summary_by_k.csv\", index=False)\n\n    elapsed = time.time() - t0\n    print(f\"\\nDone in {elapsed:.0f}s. Saved to {OUT}\")\n    print(\"\\nSummary:\")\n    print(summary_df.to_string(index=False))\n\n    return target_df, nontarget_df, summary_df\n\n\ndef generate_report(target_df, nontarget_df, summary_df):\n    lines = [\n        \"# Plan 034: Multi-Subject Simultaneous Injection — Report\",\n        \"\",\n        \"## Method\",\n        \"\",\n        \"We test Proposition 1's robustness boundary by simultaneously injecting\",\n        \"differential contamination into k MMLU subjects (k ∈ {1,2,3,5,10,20}).\",\n        \"For each (k, p, seed) combination:\",\n        \"\",\n        \"1. Randomly select k target subjects from 57 MMLU subjects\",\n        \"2. For each item in the k target subjects, flip incorrect→correct responses\",\n        \"   in the focal group (2024 models within accuracy overlap) with probability p\",\n        \"3. Compute cross-subject MH-DIF for each target and non-target subject\",\n        \"   - Matching variable = total score on all subjects EXCEPT the tested one\",\n        \"   - For target subjects: matching includes injected scores from other targets\",\n        \"   - For non-target subjects: matching includes all injected target scores\",\n        \"4. Measure TPR on target subjects and FPR on non-target subjects\",\n        \"\",\n        f\"Grid: k ∈ {{{','.join(map(str, KS))}}}, p ∈ {{{','.join(map(str, PS))}}}, \"\n        f\"5 seeds per combination = {len(KS)*len(PS)*N_SEEDS} runs\",\n        \"\",\n        \"## Core Results: ΔFPR by k and p\",\n        \"\",\n    ]\n\n    # Summary table\n    lines.append(\"### Target Subjects (TPR)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean TPR | Mean ΔTPR | SD(ΔTPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_tpr_target']:.4f} | \"\n                      f\"{row['mean_delta_tpr']:.4f} | \"\n                      f\"{row['std_delta_tpr']:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Non-Target Subjects (FPR — key result)\")\n    lines.append(\"\")\n    lines.append(\"| k | p | Mean FPR | Mean ΔFPR | SD(ΔFPR) |\")\n    lines.append(\"|---|---|----------|-----------|----------|\")\n    for _, row in summary_df.iterrows():\n        lines.append(f\"| {row['k']} | {row['p']} | {row['mean_fpr_non_target']:.4f} | \"\n                      f\"{row['mean_delta_fpr_non_target']:.4f} | \"\n                      f\"{row['std_delta_fpr_non_target']:.4f} |\")\n    lines.append(\"\")\n\n    # Key findings\n    lines.append(\"## Key Findings\")\n    lines.append(\"\")\n\n    # Find threshold where ΔFPR becomes notable\n    for p_val in PS:\n        sub = summary_df[summary_df[\"p\"] == p_val]\n        significant_k = sub[sub[\"mean_delta_fpr_non_target\"].abs() > 0.01]\n        if len(significant_k) > 0:\n            first_k = int(significant_k.iloc[0][\"k\"])\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR exceeds 0.01 at k={first_k}\")\n        else:\n            lines.append(f\"- **p={p_val}**: Non-target ΔFPR stays below 0.01 for all k tested\")\n\n    lines.append(\"\")\n    lines.append(\"## Interpretation\")\n    lines.append(\"\")\n    lines.append(\"Proposition 1 guarantees ΔFPR=0 when the matching variable is uncontaminated.\")\n    lines.append(\"As k increases, more of the cross-subject total score is contaminated,\")\n    lines.append(\"violating the proposition's assumption. The k at which ΔFPR becomes\")\n    lines.append(\"practically significant marks the validity boundary of cross-subject DIF auditing.\")\n    lines.append(\"\")\n\n    report_path = OUT / \"plan_034_report.md\"\n    report_path.write_text(\"\\n\".join(lines))\n    print(f\"Report saved to {report_path}\")\n\n\nif __name__ == \"__main__\":\n    parser = argparse.ArgumentParser(description=\"Plan 034: Multi-Subject Injection\")\n    parser.add_argument(\"--quick\", action=\"store_true\",\n                        help=\"Quick validation: k∈{1,5,20}, p=0.3, seed=1\")\n    args = parser.parse_args()\n\n    if args.quick:\n        target_df, nontarget_df, summary_df = run_experiment(\n            ks=[1, 5, 20], ps=[0.3], n_seeds=1)\n    else:\n        target_df, nontarget_df, summary_df = run_experiment()\n\n    generate_report(target_df, nontarget_df, summary_df)\n",
      "numLines": 526,
      "startLine": 1,
      "totalLines": 526
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Bash · `toolu_01EVdjBSb826J3bKJ1mZSAJc`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/",
  "description": "List existing files in plan_034 directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "88ca5c80-e27a-4784-be6e-83d66946dc67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPCjGveF7PHPbrjb1XKDBu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13292,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13292
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

_source line 8 · 2026-05-23T17:05:08.496Z_

<details><summary>↩ Tool result · `toolu_01EVdjBSb826J3bKJ1mZSAJc`</summary>

```text
data
multi_subject_injection_results.csv
non_target_fpr_results.csv
plan_034_multi_subject_injection.py
plan_034_report.md
report
summary_by_k.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "0d9b43b7-cd3f-40f8-a80b-c5a6a9ea1ae0",
  "tool_use_result": {
    "stdout": "data\nmulti_subject_injection_results.csv\nnon_target_fpr_results.csv\nplan_034_multi_subject_injection.py\nplan_034_report.md\nreport\nsummary_by_k.csv",
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

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Let me read the existing summary_by_k.csv to understand the format and existing results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "b381b621-3a82-4245-bc93-feea4e28f5c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPXJLHFEguAcEdELa6Ao2a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9290,
      "cache_read_input_tokens": 25133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9290
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

_source line 10_

Let me check the existing results and verify the data files exist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "45762556-111e-49d2-a728-f5e1e57aa255",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPXJLHFEguAcEdELa6Ao2a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9290,
      "cache_read_input_tokens": 25133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9290
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

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01PVnjQQczNA7JBXWBV3FGxR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/summary_by_k.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "9667c140-c407-43bd-b8de-e9871cb59429",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPXJLHFEguAcEdELa6Ao2a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9290,
      "cache_read_input_tokens": 25133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9290
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

_source line 12 · 2026-05-23T17:05:13.771Z_

<details><summary>↩ Tool result · `toolu_01PVnjQQczNA7JBXWBV3FGxR`</summary>

```text
1	k,p,mean_tpr_target,mean_delta_tpr,std_delta_tpr,mean_fpr_non_target,mean_delta_fpr_non_target,std_delta_fpr_non_target
2	1,0.1,0.3906,0.0743,0.0531,0.3191,0.0019,0.0016
3	1,0.3,0.559,0.2427,0.0456,0.3192,0.002,0.0012
4	1,0.5,0.834,0.5177,0.0497,0.3188,0.0016,0.0015
5	2,0.1,0.3521,0.0383,0.0292,0.3169,0.0031,0.0015
6	2,0.3,0.5012,0.1874,0.0493,0.3168,0.003,0.0017
7	2,0.5,0.8071,0.4933,0.0324,0.3152,0.0015,0.0019
8	3,0.1,0.3305,0.0225,0.0208,0.3186,0.0022,0.0011
9	3,0.3,0.4678,0.1598,0.0662,0.3172,0.0007,0.0025
10	3,0.5,0.7779,0.47,0.0934,0.3153,-0.0011,0.0032
11	5,0.1,0.3135,0.0004,0.023,0.3198,0.0038,0.0023
12	5,0.3,0.4345,0.1215,0.0225,0.3157,-0.0002,0.0039
13	5,0.5,0.7336,0.4205,0.041,0.3224,0.0065,0.0066
14	10,0.1,0.3176,0.0086,0.0123,0.3164,0.0012,0.0027
15	10,0.3,0.4076,0.0986,0.0152,0.3406,0.0255,0.0115
16	10,0.5,0.6696,0.3606,0.0269,0.3841,0.069,0.0302
17	20,0.1,0.3332,0.0217,0.0101,0.3223,0.0013,0.0039
18	20,0.3,0.3979,0.0864,0.0182,0.3927,0.0717,0.0224
19	20,0.5,0.6106,0.2992,0.0299,0.4883,0.1673,0.0294
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "a564f412-9962-4daa-b4d4-0647f6436716",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/summary_by_k.csv",
      "content": "k,p,mean_tpr_target,mean_delta_tpr,std_delta_tpr,mean_fpr_non_target,mean_delta_fpr_non_target,std_delta_fpr_non_target\n1,0.1,0.3906,0.0743,0.0531,0.3191,0.0019,0.0016\n1,0.3,0.559,0.2427,0.0456,0.3192,0.002,0.0012\n1,0.5,0.834,0.5177,0.0497,0.3188,0.0016,0.0015\n2,0.1,0.3521,0.0383,0.0292,0.3169,0.0031,0.0015\n2,0.3,0.5012,0.1874,0.0493,0.3168,0.003,0.0017\n2,0.5,0.8071,0.4933,0.0324,0.3152,0.0015,0.0019\n3,0.1,0.3305,0.0225,0.0208,0.3186,0.0022,0.0011\n3,0.3,0.4678,0.1598,0.0662,0.3172,0.0007,0.0025\n3,0.5,0.7779,0.47,0.0934,0.3153,-0.0011,0.0032\n5,0.1,0.3135,0.0004,0.023,0.3198,0.0038,0.0023\n5,0.3,0.4345,0.1215,0.0225,0.3157,-0.0002,0.0039\n5,0.5,0.7336,0.4205,0.041,0.3224,0.0065,0.0066\n10,0.1,0.3176,0.0086,0.0123,0.3164,0.0012,0.0027\n10,0.3,0.4076,0.0986,0.0152,0.3406,0.0255,0.0115\n10,0.5,0.6696,0.3606,0.0269,0.3841,0.069,0.0302\n20,0.1,0.3332,0.0217,0.0101,0.3223,0.0013,0.0039\n20,0.3,0.3979,0.0864,0.0182,0.3927,0.0717,0.0224\n20,0.5,0.6106,0.2992,0.0299,0.4883,0.1673,0.0294\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_01LCSx8QJp63DBNF25m5EB1Z`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix.npz /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix_index.npz /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/item_metadata.csv",
  "description": "Check data file existence and sizes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "b1c69c8d-aeff-45f2-99ba-7f7d6cc76a6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EPXJLHFEguAcEdELa6Ao2a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9290,
      "cache_read_input_tokens": 25133,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9290
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

_source line 14 · 2026-05-23T17:05:16.123Z_

<details><summary>↩ Tool result · `toolu_01LCSx8QJp63DBNF25m5EB1Z`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 1.5M May 20 20:57 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/item_metadata.csv
-rw-r--r-- 1 ubuntu ubuntu 390K May 20 20:51 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv
-rw-r--r-- 1 ubuntu ubuntu  49M May 20 20:51 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix.npz
-rw-r--r-- 1 ubuntu ubuntu  86K May 20 20:51 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix_index.npz
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "87ef215a-266f-4e66-81f4-305eb5becfdd",
  "tool_use_result": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 1.5M May 20 20:57 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/item_metadata.csv\n-rw-r--r-- 1 ubuntu ubuntu 390K May 20 20:51 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv\n-rw-r--r-- 1 ubuntu ubuntu  49M May 20 20:51 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix.npz\n-rw-r--r-- 1 ubuntu ubuntu  86K May 20 20:51 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix_index.npz",
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

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the info I need. The existing script runs k=[1,2,3,5,10,20] with p=[0.1,0.3,0.5] and 5 seeds. I need to create a new script for k=[30,40,50] with the same parameters.

Key observations from the existing results:
- Format: k, p, mean_tpr_target, mean_delta_tpr, std_delta_tpr, mean_fpr_non_target, mean_delta_fpr_non_target, std_delta_fpr_non_target


- The FPR gap is widening as k increases — at k=20 with p=0.5 it's already at 0.1673, well above the 0.05 threshold
- I'll modify the script to test the higher k values with minimal changes, just swapping the k list and updating the output filenames. The new run will be 45 iterations instead of 90, so it should complete in reasonable time.
- At k=30 there are 27 non-targets to test, k=40 has 17, and k=50 has only 7, so the non-target testing gets progressively faster as k increases while the data loading stays constant.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "1f7a189b-88c3-4bba-9d72-29298e31cef0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VTeagsQXQuji1S7GR9pdKH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1438,
      "cache_read_input_tokens": 34423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1438
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

_source line 16_

Data files exist, existing results have k=1..20. Now I'll create the k=30,40,50 script with minimal changes from the original.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "67535b60-3728-4e16-af77-f5a00e87345e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VTeagsQXQuji1S7GR9pdKH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1438,
      "cache_read_input_tokens": 34423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1438
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

_source line 17_

<details open><summary>🔧 Tool call — Write · `toolu_01LYxmE3MMvYjJuNk7QymNT6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_k30_40_50.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nplan_034 extension: k=30,40,50 multi-subject simultaneous injection.\nSame logic as plan_034_multi_subject_injection.py but only for KS=[30,40,50].\nOutputs k30_40_50_results.csv, k30_40_50_nontarget.csv, k30_40_50_summary.csv.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\nimport warnings\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_034_multi_subject_injection\"\nOUT.mkdir(exist_ok=True)\n\nKS = [30, 40, 50]\nPS = [0.1, 0.3, 0.5]\nN_SEEDS = 5\nN_STRATA = 5\nMIN_PER_STRATUM = 5\n\n\ndef purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,\n                    external_scores_foc=None, min_per_stratum=5):\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])\n\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n\n        n_bins = len(edges) - 1\n        k_all = np.digitize(s_all, edges[1:-1])\n        strata_labels = _merge_small_strata(k_all, groups_all, n_bins, min_per_stratum)\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        x_all = np.concatenate([X_ref[:, j], X_foc[:, j]])\n\n        for k in np.unique(strata_labels):\n            mask_k = (strata_labels == k)\n            mask_ref = mask_k & (groups_all == 0)\n            mask_foc = mask_k & (groups_all == 1)\n\n            n1 = int(mask_ref.sum())\n            n0 = int(mask_foc.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(x_all[mask_ref].sum())\n            B = float(n1 - A)\n            C = float(x_all[mask_foc].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else np.inf\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets,\n                         n_strata_used=n_ok))\n\n    return pd.DataFrame(rows)\n\n\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\",\n                n_strata_used=0)\n\n\ndef _merge_small_strata(k_all, groups_all, n_bins, min_n):\n    labels = k_all.copy()\n    merged = True\n    while merged:\n        merged = False\n        unique_strata = sorted(np.unique(labels))\n        for i, k in enumerate(unique_strata):\n            mask_k = (labels == k)\n            n_ref = int((mask_k & (groups_all == 0)).sum())\n            n_foc = int((mask_k & (groups_all == 1)).sum())\n            if n_ref < min_n or n_foc < min_n:\n                if i + 1 < len(unique_strata):\n                    next_k = unique_strata[i + 1]\n                    labels[labels == next_k] = k\n                elif i > 0:\n                    prev_k = unique_strata[i - 1]\n                    labels[labels == k] = prev_k\n                merged = True\n                break\n    return labels\n\n\ndef load_data():\n    mat = load_npz(BASE / \"response_matrix.npz\")\n    idx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n    item2col = {iid: i for i, iid in enumerate(item_ids)}\n\n    model_meta = pd.read_csv(BASE / \"model_metadata.csv\")\n    item_meta = pd.read_csv(BASE / \"item_metadata.csv\")\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    ref_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"model_name\"]\n    foc_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"model_name\"]\n    ref_rows = np.array([name2row[n] for n in ref_names if n in name2row])\n    foc_rows = np.array([name2row[n] for n in foc_names if n in name2row])\n\n    ref_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\n    foc_df = model_meta[model_meta[\"cohort_temporal\"] == \"2024\"]\n    t_min = max(ref_acc.min(), foc_df[\"accuracy\"].min())\n    t_max = min(ref_acc.max(), foc_df[\"accuracy\"].max())\n    foc_inject_mask = (foc_df[\"accuracy\"] >= t_min) & (foc_df[\"accuracy\"] <= t_max)\n    foc_inject_rows = np.array([name2row[n] for n in foc_df.loc[foc_inject_mask, \"model_name\"]\n                                if n in name2row])\n\n    subject_cols = {}\n    subjects = sorted(item_meta[\"subject\"].unique())\n    for subj in subjects:\n        ids = item_meta.loc[item_meta[\"subject\"] == subj, \"item_id\"].values\n        cols = np.array([item2col[iid] for iid in ids if iid in item2col])\n        subject_cols[subj] = cols\n\n    return mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols\n\n\ndef run_experiment(ks=KS, ps=PS, n_seeds=N_SEEDS):\n    t0 = time.time()\n    mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols = load_data()\n    print(f\"Data loaded: {len(ref_rows)} ref, {len(foc_rows)} foc, \"\n          f\"{len(foc_inject_rows)} foc_inject, {len(subjects)} subjects\")\n\n    subj_totals_ref = {}\n    subj_totals_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_totals_ref[subj] = np.asarray(mat[ref_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n        subj_totals_foc[subj] = np.asarray(mat[foc_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n\n    full_total_ref = sum(subj_totals_ref.values())\n    full_total_foc = sum(subj_totals_foc.values())\n\n    subj_X_ref = {}\n    subj_X_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_X_ref[subj] = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n        subj_X_foc[subj] = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n    # Baseline FPR (p=0)\n    print(\"Computing baseline FPR (p=0) for all subjects...\")\n    baseline_fpr = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        cross_ref = full_total_ref - subj_totals_ref[subj]\n        cross_foc = full_total_foc - subj_totals_foc[subj]\n\n        n_strata = 3 if len(s_cols) < 100 else N_STRATA\n        dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,\n                              external_scores_ref=cross_ref,\n                              external_scores_foc=cross_foc,\n                              min_per_stratum=MIN_PER_STRATUM)\n        n_c = int((dif[\"ets_class\"] == \"C\").sum())\n        baseline_fpr[subj] = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n\n    print(f\"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}\")\n\n    # Injection runs\n    target_rows_list = []\n    non_target_rows_list = []\n    total_runs = len(ks) * len(ps) * n_seeds\n    run_i = 0\n\n    for k in ks:\n        for p in ps:\n            for seed in range(1, n_seeds + 1):\n                run_i += 1\n                rng = np.random.RandomState(seed)\n                target_subjects = sorted(rng.choice(subjects, size=k, replace=False))\n                non_target_subjects = [s for s in subjects if s not in target_subjects]\n\n                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])\n\n                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    block = mat_dense_targets[foc_inject_rows]\n                    zeros = (block == 0)\n                    flip_mask = zeros & (rng.random(block.shape) < p)\n                    n_flipped = int(flip_mask.sum())\n                    mat_dense_targets[foc_inject_rows] = block + flip_mask.astype(np.int8)\n\n                non_target_total_ref = full_total_ref - sum(subj_totals_ref[s] for s in target_subjects)\n                non_target_total_foc = full_total_foc - sum(subj_totals_foc[s] for s in target_subjects)\n\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}\n                target_subj_injected = {}\n                for s in target_subjects:\n                    local_idxs = np.array([target_col_to_local[c] for c in subject_cols[s]])\n                    target_subj_injected[s] = mat_dense_targets[:, local_idxs].sum(axis=1).astype(np.float64)\n\n                elapsed = time.time() - t0\n                print(f\"  [{run_i}/{total_runs}] k={k} p={p} seed={seed} \"\n                      f\"flipped={n_flipped} ({elapsed:.0f}s)\")\n\n                # DIF on target subjects\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    other_target_inj = injected_target_total - target_subj_injected[subj]\n                    match_ref = non_target_total_ref + other_target_inj[ref_rows]\n                    match_foc = non_target_total_foc + other_target_inj[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    tpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_tpr = tpr - baseline_fpr[subj]\n\n                    target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, target_subject=subj,\n                        n_items=len(s_cols), tpr=tpr, fpr=np.nan,\n                        delta_tpr=delta_tpr, delta_fpr=np.nan,\n                        n_target_c=n_c, n_clean_c=np.nan\n                    ))\n\n                # DIF on non-target subjects\n                if len(non_target_subjects) <= 20:\n                    test_nontargets = non_target_subjects\n                else:\n                    test_nontargets = sorted(rng.choice(non_target_subjects,\n                                                        size=20, replace=False))\n\n                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n\n                    match_ref = (non_target_total_ref - subj_totals_ref[subj]\n                                 + injected_target_total[ref_rows])\n                    match_foc = (non_target_total_foc - subj_totals_foc[subj]\n                                 + injected_target_total[foc_rows])\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_fpr = fpr - baseline_fpr[subj]\n\n                    non_target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, non_target_subject=subj,\n                        n_items=len(s_cols),\n                        fpr=fpr, baseline_fpr=baseline_fpr[subj],\n                        delta_fpr=delta_fpr\n                    ))\n\n    # Save results\n    target_df = pd.DataFrame(target_rows_list)\n    target_df.to_csv(OUT / \"k30_40_50_results.csv\", index=False)\n\n    nontarget_df = pd.DataFrame(non_target_rows_list)\n    nontarget_df.to_csv(OUT / \"k30_40_50_nontarget.csv\", index=False)\n\n    # Summary by k,p\n    summary_rows = []\n    for k in ks:\n        for p_val in ps:\n            t_sub = target_df[(target_df[\"k\"] == k) & (target_df[\"p\"] == p_val)]\n            nt_sub = nontarget_df[(nontarget_df[\"k\"] == k) & (nontarget_df[\"p\"] == p_val)]\n\n            mean_tpr = t_sub[\"tpr\"].mean() if len(t_sub) > 0 else np.nan\n            mean_delta_tpr = t_sub[\"delta_tpr\"].mean() if len(t_sub) > 0 else np.nan\n            std_delta_tpr = t_sub.groupby(\"seed\")[\"delta_tpr\"].mean().std() if len(t_sub) > 0 else np.nan\n\n            mean_fpr_nt = nt_sub[\"fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            mean_delta_fpr_nt = nt_sub[\"delta_fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            std_delta_fpr_nt = nt_sub.groupby(\"seed\")[\"delta_fpr\"].mean().std() if len(nt_sub) > 0 else np.nan\n\n            summary_rows.append(dict(\n                k=k, p=p_val,\n                mean_tpr_target=round(mean_tpr, 4),\n                mean_delta_tpr=round(mean_delta_tpr, 4),\n                std_delta_tpr=round(std_delta_tpr, 4) if not np.isnan(std_delta_tpr) else np.nan,\n                mean_fpr_non_target=round(mean_fpr_nt, 4),\n                mean_delta_fpr_non_target=round(mean_delta_fpr_nt, 4),\n                std_delta_fpr_non_target=round(std_delta_fpr_nt, 4) if not np.isnan(std_delta_fpr_nt) else np.nan,\n            ))\n\n    summary_df = pd.DataFrame(summary_rows)\n    summary_df.to_csv(OUT / \"k30_40_50_summary.csv\", index=False)\n\n    elapsed = time.time() - t0\n    print(f\"\\nDone in {elapsed:.0f}s. Saved to {OUT}\")\n    print(\"\\nSummary (k=30,40,50):\")\n    print(summary_df.to_string(index=False))\n\n    return target_df, nontarget_df, summary_df\n\n\nif __name__ == \"__main__\":\n    run_experiment()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "e7a8d532-2a1d-4b87-b8be-94045f2112f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VTeagsQXQuji1S7GR9pdKH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1438,
      "cache_read_input_tokens": 34423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1438
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

_source line 18 · 2026-05-23T17:06:43.564Z_

<details><summary>↩ Tool result · `toolu_01LYxmE3MMvYjJuNk7QymNT6`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_k30_40_50.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "16811b80-0741-4f9e-9875-234e64889921",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection/plan_034_k30_40_50.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nplan_034 extension: k=30,40,50 multi-subject simultaneous injection.\nSame logic as plan_034_multi_subject_injection.py but only for KS=[30,40,50].\nOutputs k30_40_50_results.csv, k30_40_50_nontarget.csv, k30_40_50_summary.csv.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\nimport warnings\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_034_multi_subject_injection\"\nOUT.mkdir(exist_ok=True)\n\nKS = [30, 40, 50]\nPS = [0.1, 0.3, 0.5]\nN_SEEDS = 5\nN_STRATA = 5\nMIN_PER_STRATUM = 5\n\n\ndef purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,\n                    external_scores_foc=None, min_per_stratum=5):\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        groups_all = np.concatenate([np.zeros(len(s_ref)), np.ones(len(s_foc))])\n\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n\n        n_bins = len(edges) - 1\n        k_all = np.digitize(s_all, edges[1:-1])\n        strata_labels = _merge_small_strata(k_all, groups_all, n_bins, min_per_stratum)\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        x_all = np.concatenate([X_ref[:, j], X_foc[:, j]])\n\n        for k in np.unique(strata_labels):\n            mask_k = (strata_labels == k)\n            mask_ref = mask_k & (groups_all == 0)\n            mask_foc = mask_k & (groups_all == 1)\n\n            n1 = int(mask_ref.sum())\n            n0 = int(mask_foc.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(x_all[mask_ref].sum())\n            B = float(n1 - A)\n            C = float(x_all[mask_foc].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else np.inf\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets,\n                         n_strata_used=n_ok))\n\n    return pd.DataFrame(rows)\n\n\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\",\n                n_strata_used=0)\n\n\ndef _merge_small_strata(k_all, groups_all, n_bins, min_n):\n    labels = k_all.copy()\n    merged = True\n    while merged:\n        merged = False\n        unique_strata = sorted(np.unique(labels))\n        for i, k in enumerate(unique_strata):\n            mask_k = (labels == k)\n            n_ref = int((mask_k & (groups_all == 0)).sum())\n            n_foc = int((mask_k & (groups_all == 1)).sum())\n            if n_ref < min_n or n_foc < min_n:\n                if i + 1 < len(unique_strata):\n                    next_k = unique_strata[i + 1]\n                    labels[labels == next_k] = k\n                elif i > 0:\n                    prev_k = unique_strata[i - 1]\n                    labels[labels == k] = prev_k\n                merged = True\n                break\n    return labels\n\n\ndef load_data():\n    mat = load_npz(BASE / \"response_matrix.npz\")\n    idx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids = idx[\"item_ids\"]\n    item2col = {iid: i for i, iid in enumerate(item_ids)}\n\n    model_meta = pd.read_csv(BASE / \"model_metadata.csv\")\n    item_meta = pd.read_csv(BASE / \"item_metadata.csv\")\n    name2row = {n: i for i, n in enumerate(model_names)}\n\n    ref_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"model_name\"]\n    foc_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"model_name\"]\n    ref_rows = np.array([name2row[n] for n in ref_names if n in name2row])\n    foc_rows = np.array([name2row[n] for n in foc_names if n in name2row])\n\n    ref_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\n    foc_df = model_meta[model_meta[\"cohort_temporal\"] == \"2024\"]\n    t_min = max(ref_acc.min(), foc_df[\"accuracy\"].min())\n    t_max = min(ref_acc.max(), foc_df[\"accuracy\"].max())\n    foc_inject_mask = (foc_df[\"accuracy\"] >= t_min) & (foc_df[\"accuracy\"] <= t_max)\n    foc_inject_rows = np.array([name2row[n] for n in foc_df.loc[foc_inject_mask, \"model_name\"]\n                                if n in name2row])\n\n    subject_cols = {}\n    subjects = sorted(item_meta[\"subject\"].unique())\n    for subj in subjects:\n        ids = item_meta.loc[item_meta[\"subject\"] == subj, \"item_id\"].values\n        cols = np.array([item2col[iid] for iid in ids if iid in item2col])\n        subject_cols[subj] = cols\n\n    return mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols\n\n\ndef run_experiment(ks=KS, ps=PS, n_seeds=N_SEEDS):\n    t0 = time.time()\n    mat, ref_rows, foc_rows, foc_inject_rows, subjects, subject_cols = load_data()\n    print(f\"Data loaded: {len(ref_rows)} ref, {len(foc_rows)} foc, \"\n          f\"{len(foc_inject_rows)} foc_inject, {len(subjects)} subjects\")\n\n    subj_totals_ref = {}\n    subj_totals_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_totals_ref[subj] = np.asarray(mat[ref_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n        subj_totals_foc[subj] = np.asarray(mat[foc_rows][:, s_cols].sum(axis=1)).ravel().astype(np.float64)\n\n    full_total_ref = sum(subj_totals_ref.values())\n    full_total_foc = sum(subj_totals_foc.values())\n\n    subj_X_ref = {}\n    subj_X_foc = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        subj_X_ref[subj] = mat[ref_rows][:, s_cols].toarray().astype(np.int8)\n        subj_X_foc[subj] = mat[foc_rows][:, s_cols].toarray().astype(np.int8)\n\n    # Baseline FPR (p=0)\n    print(\"Computing baseline FPR (p=0) for all subjects...\")\n    baseline_fpr = {}\n    for subj in subjects:\n        s_cols = subject_cols[subj]\n        cross_ref = full_total_ref - subj_totals_ref[subj]\n        cross_foc = full_total_foc - subj_totals_foc[subj]\n\n        n_strata = 3 if len(s_cols) < 100 else N_STRATA\n        dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,\n                              external_scores_ref=cross_ref,\n                              external_scores_foc=cross_foc,\n                              min_per_stratum=MIN_PER_STRATUM)\n        n_c = int((dif[\"ets_class\"] == \"C\").sum())\n        baseline_fpr[subj] = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n\n    print(f\"Baseline done. Mean FPR = {np.mean(list(baseline_fpr.values())):.4f}\")\n\n    # Injection runs\n    target_rows_list = []\n    non_target_rows_list = []\n    total_runs = len(ks) * len(ps) * n_seeds\n    run_i = 0\n\n    for k in ks:\n        for p in ps:\n            for seed in range(1, n_seeds + 1):\n                run_i += 1\n                rng = np.random.RandomState(seed)\n                target_subjects = sorted(rng.choice(subjects, size=k, replace=False))\n                non_target_subjects = [s for s in subjects if s not in target_subjects]\n\n                target_cols_all = np.concatenate([subject_cols[s] for s in target_subjects])\n\n                mat_dense_targets = mat[:, target_cols_all].toarray().astype(np.int8)\n                n_flipped = 0\n                if p > 0:\n                    block = mat_dense_targets[foc_inject_rows]\n                    zeros = (block == 0)\n                    flip_mask = zeros & (rng.random(block.shape) < p)\n                    n_flipped = int(flip_mask.sum())\n                    mat_dense_targets[foc_inject_rows] = block + flip_mask.astype(np.int8)\n\n                non_target_total_ref = full_total_ref - sum(subj_totals_ref[s] for s in target_subjects)\n                non_target_total_foc = full_total_foc - sum(subj_totals_foc[s] for s in target_subjects)\n\n                injected_target_total = mat_dense_targets.sum(axis=1).astype(np.float64)\n\n                target_col_to_local = {c: i for i, c in enumerate(target_cols_all)}\n                target_subj_injected = {}\n                for s in target_subjects:\n                    local_idxs = np.array([target_col_to_local[c] for c in subject_cols[s]])\n                    target_subj_injected[s] = mat_dense_targets[:, local_idxs].sum(axis=1).astype(np.float64)\n\n                elapsed = time.time() - t0\n                print(f\"  [{run_i}/{total_runs}] k={k} p={p} seed={seed} \"\n                      f\"flipped={n_flipped} ({elapsed:.0f}s)\")\n\n                # DIF on target subjects\n                for subj in target_subjects:\n                    s_cols = subject_cols[subj]\n                    local_idxs = np.array([target_col_to_local[c] for c in s_cols])\n                    X_subj_inj = mat_dense_targets[:, local_idxs]\n\n                    X_ref_s = X_subj_inj[ref_rows]\n                    X_foc_s = X_subj_inj[foc_rows]\n\n                    other_target_inj = injected_target_total - target_subj_injected[subj]\n                    match_ref = non_target_total_ref + other_target_inj[ref_rows]\n                    match_foc = non_target_total_foc + other_target_inj[foc_rows]\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(X_ref_s, X_foc_s, n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    tpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_tpr = tpr - baseline_fpr[subj]\n\n                    target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, target_subject=subj,\n                        n_items=len(s_cols), tpr=tpr, fpr=np.nan,\n                        delta_tpr=delta_tpr, delta_fpr=np.nan,\n                        n_target_c=n_c, n_clean_c=np.nan\n                    ))\n\n                # DIF on non-target subjects\n                if len(non_target_subjects) <= 20:\n                    test_nontargets = non_target_subjects\n                else:\n                    test_nontargets = sorted(rng.choice(non_target_subjects,\n                                                        size=20, replace=False))\n\n                for subj in test_nontargets:\n                    s_cols = subject_cols[subj]\n\n                    match_ref = (non_target_total_ref - subj_totals_ref[subj]\n                                 + injected_target_total[ref_rows])\n                    match_foc = (non_target_total_foc - subj_totals_foc[subj]\n                                 + injected_target_total[foc_rows])\n\n                    n_strata = 3 if len(s_cols) < 100 else N_STRATA\n                    dif = purified_mh_dif(subj_X_ref[subj], subj_X_foc[subj], n_strata=n_strata,\n                                          external_scores_ref=match_ref,\n                                          external_scores_foc=match_foc,\n                                          min_per_stratum=MIN_PER_STRATUM)\n\n                    n_c = int((dif[\"ets_class\"] == \"C\").sum())\n                    fpr = n_c / len(s_cols) if len(s_cols) > 0 else 0.0\n                    delta_fpr = fpr - baseline_fpr[subj]\n\n                    non_target_rows_list.append(dict(\n                        k=k, p=p, seed=seed, non_target_subject=subj,\n                        n_items=len(s_cols),\n                        fpr=fpr, baseline_fpr=baseline_fpr[subj],\n                        delta_fpr=delta_fpr\n                    ))\n\n    # Save results\n    target_df = pd.DataFrame(target_rows_list)\n    target_df.to_csv(OUT / \"k30_40_50_results.csv\", index=False)\n\n    nontarget_df = pd.DataFrame(non_target_rows_list)\n    nontarget_df.to_csv(OUT / \"k30_40_50_nontarget.csv\", index=False)\n\n    # Summary by k,p\n    summary_rows = []\n    for k in ks:\n        for p_val in ps:\n            t_sub = target_df[(target_df[\"k\"] == k) & (target_df[\"p\"] == p_val)]\n            nt_sub = nontarget_df[(nontarget_df[\"k\"] == k) & (nontarget_df[\"p\"] == p_val)]\n\n            mean_tpr = t_sub[\"tpr\"].mean() if len(t_sub) > 0 else np.nan\n            mean_delta_tpr = t_sub[\"delta_tpr\"].mean() if len(t_sub) > 0 else np.nan\n            std_delta_tpr = t_sub.groupby(\"seed\")[\"delta_tpr\"].mean().std() if len(t_sub) > 0 else np.nan\n\n            mean_fpr_nt = nt_sub[\"fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            mean_delta_fpr_nt = nt_sub[\"delta_fpr\"].mean() if len(nt_sub) > 0 else np.nan\n            std_delta_fpr_nt = nt_sub.groupby(\"seed\")[\"delta_fpr\"].mean().std() if len(nt_sub) > 0 else np.nan\n\n            summary_rows.append(dict(\n                k=k, p=p_val,\n                mean_tpr_target=round(mean_tpr, 4),\n                mean_delta_tpr=round(mean_delta_tpr, 4),\n                std_delta_tpr=round(std_delta_tpr, 4) if not np.isnan(std_delta_tpr) else np.nan,\n                mean_fpr_non_target=round(mean_fpr_nt, 4),\n                mean_delta_fpr_non_target=round(mean_delta_fpr_nt, 4),\n                std_delta_fpr_non_target=round(std_delta_fpr_nt, 4) if not np.isnan(std_delta_fpr_nt) else np.nan,\n            ))\n\n    summary_df = pd.DataFrame(summary_rows)\n    summary_df.to_csv(OUT / \"k30_40_50_summary.csv\", index=False)\n\n    elapsed = time.time() - t0\n    print(f\"\\nDone in {elapsed:.0f}s. Saved to {OUT}\")\n    print(\"\\nSummary (k=30,40,50):\")\n    print(summary_df.to_string(index=False))\n\n    return target_df, nontarget_df, summary_df\n\n\nif __name__ == \"__main__\":\n    run_experiment()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 19_

Running the script now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "d48dc041-ee74-41bd-a91e-5ca8f28590e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EsmPwHyQMiNk2aB6ByoRKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6437,
      "cache_read_input_tokens": 35861,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6437
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

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_011TQhZmcRb5eXWgrWhvswQb`</summary>

```json
{
  "command": "python3 artifacts/plan_034_multi_subject_injection/plan_034_k30_40_50.py",
  "description": "Run k=30,40,50 multi-subject injection experiment",
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
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "88e0a3ca-9556-4ceb-98ba-633e5596139f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EsmPwHyQMiNk2aB6ByoRKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6437,
      "cache_read_input_tokens": 35861,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6437
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

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bsntffa33",
  "tool_use_id": "toolu_011TQhZmcRb5eXWgrWhvswQb",
  "description": "Run k=30,40,50 multi-subject injection experiment",
  "task_type": "local_bash",
  "uuid": "ea290974-5345-496c-87b9-69dd99ef3c8e",
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825"
}
```

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bsntffa33",
  "tool_use_id": "toolu_011TQhZmcRb5eXWgrWhvswQb",
  "status": "completed",
  "output_file": "",
  "summary": "Run k=30,40,50 multi-subject injection experiment",
  "uuid": "395dc69e-e029-441d-ab46-c4fdb659b26d",
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825"
}
```

---

### Tool result

_source line 23 · 2026-05-23T17:14:54.313Z_

<details><summary>↩ Tool result · `toolu_011TQhZmcRb5eXWgrWhvswQb`</summary>

```text
Data loaded: 1080 ref, 807 foc, 787 foc_inject, 57 subjects
Computing baseline FPR (p=0) for all subjects...
Baseline done. Mean FPR = 0.3136
  [1/45] k=30 p=0.1 seed=1 flipped=215391 (17s)
  [2/45] k=30 p=0.1 seed=2 flipped=240417 (27s)
  [3/45] k=30 p=0.1 seed=3 flipped=212116 (37s)
  [4/45] k=30 p=0.1 seed=4 flipped=197476 (45s)
  [5/45] k=30 p=0.1 seed=5 flipped=200479 (55s)
  [6/45] k=30 p=0.3 seed=1 flipped=647171 (65s)
  [7/45] k=30 p=0.3 seed=2 flipped=721683 (74s)
  [8/45] k=30 p=0.3 seed=3 flipped=635801 (85s)
  [9/45] k=30 p=0.3 seed=4 flipped=594747 (95s)
  [10/45] k=30 p=0.3 seed=5 flipped=601512 (105s)
  [11/45] k=30 p=0.5 seed=1 flipped=1077958 (114s)
  [12/45] k=30 p=0.5 seed=2 flipped=1203578 (125s)
  [13/45] k=30 p=0.5 seed=3 flipped=1059514 (134s)
  [14/45] k=30 p=0.5 seed=4 flipped=991033 (142s)
  [15/45] k=30 p=0.5 seed=5 flipped=1001087 (152s)
  [16/45] k=40 p=0.1 seed=1 flipped=281444 (161s)
  [17/45] k=40 p=0.1 seed=2 flipped=283315 (172s)
  [18/45] k=40 p=0.1 seed=3 flipped=267290 (182s)
  [19/45] k=40 p=0.1 seed=4 flipped=312297 (192s)
  [20/45] k=40 p=0.1 seed=5 flipped=245720 (204s)
  [21/45] k=40 p=0.3 seed=1 flipped=846045 (215s)
  [22/45] k=40 p=0.3 seed=2 flipped=850119 (226s)
  [23/45] k=40 p=0.3 seed=3 flipped=803161 (236s)
  [24/45] k=40 p=0.3 seed=4 flipped=939154 (246s)
  [25/45] k=40 p=0.3 seed=5 flipped=736603 (257s)
  [26/45] k=40 p=0.5 seed=1 flipped=1409696 (268s)
  [27/45] k=40 p=0.5 seed=2 flipped=1418139 (278s)
  [28/45] k=40 p=0.5 seed=3 flipped=1337829 (289s)
  [29/45] k=40 p=0.5 seed=4 flipped=1565178 (299s)
  [30/45] k=40 p=0.5 seed=5 flipped=1228628 (310s)
  [31/45] k=50 p=0.1 seed=1 flipped=335045 (321s)
  [32/45] k=50 p=0.1 seed=2 flipped=320195 (332s)
  [33/45] k=50 p=0.1 seed=3 flipped=349356 (344s)
  [34/45] k=50 p=0.1 seed=4 flipped=361072 (355s)
  [35/45] k=50 p=0.1 seed=5 flipped=358527 (365s)
  [36/45] k=50 p=0.3 seed=1 flipped=1003652 (376s)
  [37/45] k=50 p=0.3 seed=2 flipped=960740 (388s)
  [38/45] k=50 p=0.3 seed=3 flipped=1047018 (399s)
  [39/45] k=50 p=0.3 seed=4 flipped=1085060 (410s)
  [40/45] k=50 p=0.3 seed=5 flipped=1075108 (420s)
  [41/45] k=50 p=0.5 seed=1 flipped=1671360 (431s)
  [42/45] k=50 p=0.5 seed=2 flipped=1602895 (442s)
  [43/45] k=50 p=0.5 seed=3 flipped=1744755 (453s)
  [44/45] k=50 p=0.5 seed=4 flipped=1808248 (465s)
  [45/45] k=50 p=0.5 seed=5 flipped=1790729 (476s)

Done in 486s. Saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection

Summary (k=30,40,50):
 k   p  mean_tpr_target  mean_delta_tpr  std_delta_tpr  mean_fpr_non_target  mean_delta_fpr_non_target  std_delta_fpr_non_target
30 0.1           0.3355          0.0237         0.0086               0.3374                     0.0259                    0.0060
30 0.3           0.3663          0.0546         0.0226               0.4914                     0.1798                    0.0205
30 0.5           0.4710          0.1593         0.0345               0.6734                     0.3618                    0.0255
40 0.1           0.3348          0.0222         0.0067               0.3566                     0.0407                    0.0234
40 0.3           0.3722          0.0595         0.0226               0.5699                     0.2540                    0.0665
40 0.5           0.5300          0.2174         0.0439               0.7214                     0.4056                    0.0536
50 0.1           0.3440          0.0296         0.0014               0.3636                     0.0559                    0.0272
50 0.3           0.4753          0.1608         0.0291               0.6109                     0.3032                    0.0639
50 0.5           0.7535          0.4390         0.0281               0.7658                     0.4581                    0.0527
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "04b87cee-1341-4e05-a4d1-dc8cb38004cf",
  "tool_use_result": {
    "stdout": "Data loaded: 1080 ref, 807 foc, 787 foc_inject, 57 subjects\nComputing baseline FPR (p=0) for all subjects...\nBaseline done. Mean FPR = 0.3136\n  [1/45] k=30 p=0.1 seed=1 flipped=215391 (17s)\n  [2/45] k=30 p=0.1 seed=2 flipped=240417 (27s)\n  [3/45] k=30 p=0.1 seed=3 flipped=212116 (37s)\n  [4/45] k=30 p=0.1 seed=4 flipped=197476 (45s)\n  [5/45] k=30 p=0.1 seed=5 flipped=200479 (55s)\n  [6/45] k=30 p=0.3 seed=1 flipped=647171 (65s)\n  [7/45] k=30 p=0.3 seed=2 flipped=721683 (74s)\n  [8/45] k=30 p=0.3 seed=3 flipped=635801 (85s)\n  [9/45] k=30 p=0.3 seed=4 flipped=594747 (95s)\n  [10/45] k=30 p=0.3 seed=5 flipped=601512 (105s)\n  [11/45] k=30 p=0.5 seed=1 flipped=1077958 (114s)\n  [12/45] k=30 p=0.5 seed=2 flipped=1203578 (125s)\n  [13/45] k=30 p=0.5 seed=3 flipped=1059514 (134s)\n  [14/45] k=30 p=0.5 seed=4 flipped=991033 (142s)\n  [15/45] k=30 p=0.5 seed=5 flipped=1001087 (152s)\n  [16/45] k=40 p=0.1 seed=1 flipped=281444 (161s)\n  [17/45] k=40 p=0.1 seed=2 flipped=283315 (172s)\n  [18/45] k=40 p=0.1 seed=3 flipped=267290 (182s)\n  [19/45] k=40 p=0.1 seed=4 flipped=312297 (192s)\n  [20/45] k=40 p=0.1 seed=5 flipped=245720 (204s)\n  [21/45] k=40 p=0.3 seed=1 flipped=846045 (215s)\n  [22/45] k=40 p=0.3 seed=2 flipped=850119 (226s)\n  [23/45] k=40 p=0.3 seed=3 flipped=803161 (236s)\n  [24/45] k=40 p=0.3 seed=4 flipped=939154 (246s)\n  [25/45] k=40 p=0.3 seed=5 flipped=736603 (257s)\n  [26/45] k=40 p=0.5 seed=1 flipped=1409696 (268s)\n  [27/45] k=40 p=0.5 seed=2 flipped=1418139 (278s)\n  [28/45] k=40 p=0.5 seed=3 flipped=1337829 (289s)\n  [29/45] k=40 p=0.5 seed=4 flipped=1565178 (299s)\n  [30/45] k=40 p=0.5 seed=5 flipped=1228628 (310s)\n  [31/45] k=50 p=0.1 seed=1 flipped=335045 (321s)\n  [32/45] k=50 p=0.1 seed=2 flipped=320195 (332s)\n  [33/45] k=50 p=0.1 seed=3 flipped=349356 (344s)\n  [34/45] k=50 p=0.1 seed=4 flipped=361072 (355s)\n  [35/45] k=50 p=0.1 seed=5 flipped=358527 (365s)\n  [36/45] k=50 p=0.3 seed=1 flipped=1003652 (376s)\n  [37/45] k=50 p=0.3 seed=2 flipped=960740 (388s)\n  [38/45] k=50 p=0.3 seed=3 flipped=1047018 (399s)\n  [39/45] k=50 p=0.3 seed=4 flipped=1085060 (410s)\n  [40/45] k=50 p=0.3 seed=5 flipped=1075108 (420s)\n  [41/45] k=50 p=0.5 seed=1 flipped=1671360 (431s)\n  [42/45] k=50 p=0.5 seed=2 flipped=1602895 (442s)\n  [43/45] k=50 p=0.5 seed=3 flipped=1744755 (453s)\n  [44/45] k=50 p=0.5 seed=4 flipped=1808248 (465s)\n  [45/45] k=50 p=0.5 seed=5 flipped=1790729 (476s)\n\nDone in 486s. Saved to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_034_multi_subject_injection\n\nSummary (k=30,40,50):\n k   p  mean_tpr_target  mean_delta_tpr  std_delta_tpr  mean_fpr_non_target  mean_delta_fpr_non_target  std_delta_fpr_non_target\n30 0.1           0.3355          0.0237         0.0086               0.3374                     0.0259                    0.0060\n30 0.3           0.3663          0.0546         0.0226               0.4914                     0.1798                    0.0205\n30 0.5           0.4710          0.1593         0.0345               0.6734                     0.3618                    0.0255\n40 0.1           0.3348          0.0222         0.0067               0.3566                     0.0407                    0.0234\n40 0.3           0.3722          0.0595         0.0226               0.5699                     0.2540                    0.0665\n40 0.5           0.5300          0.2174         0.0439               0.7214                     0.4056                    0.0536\n50 0.1           0.3440          0.0296         0.0014               0.3636                     0.0559                    0.0272\n50 0.3           0.4753          0.1608         0.0291               0.6109                     0.3032                    0.0639\n50 0.5           0.7535          0.4390         0.0281               0.7658                     0.4581                    0.0527",
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

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
The experiment completed in ~8 minutes. Now I need to merge the new results with the existing summary_by_k.csv.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "a557b50a-b400-43bd-b7f8-59b02713ffd5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LUfJp5UfaQL6GUDcTQPBV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2181,
      "cache_read_input_tokens": 42298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2181
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

_source line 25_

Experiment completed in ~8 minutes. Now merging with the existing results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "9ab97a38-8f31-40b1-b9ae-a42886d277d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LUfJp5UfaQL6GUDcTQPBV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2181,
      "cache_read_input_tokens": 42298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2181
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

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_018fSNgjzxe3Pcxz6dhdcsXX`</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\nold = pd.read_csv('artifacts/plan_034_multi_subject_injection/summary_by_k.csv')\nnew = pd.read_csv('artifacts/plan_034_multi_subject_injection/k30_40_50_summary.csv')\nmerged = pd.concat([old, new], ignore_index=True).sort_values(['k', 'p']).reset_index(drop=True)\nmerged.to_csv('artifacts/plan_034_multi_subject_injection/summary_by_k_full.csv', index=False)\nprint(merged.to_string(index=False))\n\"",
  "description": "Merge old and new summary CSVs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "286ddf7f-2ff9-4146-82b3-d56b01dcf1c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LUfJp5UfaQL6GUDcTQPBV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2181,
      "cache_read_input_tokens": 42298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2181
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

_source line 27 · 2026-05-23T17:15:01.071Z_

<details><summary>↩ Tool result · `toolu_018fSNgjzxe3Pcxz6dhdcsXX`</summary>

```text
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
30 0.1           0.3355          0.0237         0.0086               0.3374                     0.0259                    0.0060
30 0.3           0.3663          0.0546         0.0226               0.4914                     0.1798                    0.0205
30 0.5           0.4710          0.1593         0.0345               0.6734                     0.3618                    0.0255
40 0.1           0.3348          0.0222         0.0067               0.3566                     0.0407                    0.0234
40 0.3           0.3722          0.0595         0.0226               0.5699                     0.2540                    0.0665
40 0.5           0.5300          0.2174         0.0439               0.7214                     0.4056                    0.0536
50 0.1           0.3440          0.0296         0.0014               0.3636                     0.0559                    0.0272
50 0.3           0.4753          0.1608         0.0291               0.6109                     0.3032                    0.0639
50 0.5           0.7535          0.4390         0.0281               0.7658                     0.4581                    0.0527
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "65eae255-a842-4b59-b824-dacd0545f5d5",
  "tool_use_result": {
    "stdout": " k   p  mean_tpr_target  mean_delta_tpr  std_delta_tpr  mean_fpr_non_target  mean_delta_fpr_non_target  std_delta_fpr_non_target\n 1 0.1           0.3906          0.0743         0.0531               0.3191                     0.0019                    0.0016\n 1 0.3           0.5590          0.2427         0.0456               0.3192                     0.0020                    0.0012\n 1 0.5           0.8340          0.5177         0.0497               0.3188                     0.0016                    0.0015\n 2 0.1           0.3521          0.0383         0.0292               0.3169                     0.0031                    0.0015\n 2 0.3           0.5012          0.1874         0.0493               0.3168                     0.0030                    0.0017\n 2 0.5           0.8071          0.4933         0.0324               0.3152                     0.0015                    0.0019\n 3 0.1           0.3305          0.0225         0.0208               0.3186                     0.0022                    0.0011\n 3 0.3           0.4678          0.1598         0.0662               0.3172                     0.0007                    0.0025\n 3 0.5           0.7779          0.4700         0.0934               0.3153                    -0.0011                    0.0032\n 5 0.1           0.3135          0.0004         0.0230               0.3198                     0.0038                    0.0023\n 5 0.3           0.4345          0.1215         0.0225               0.3157                    -0.0002                    0.0039\n 5 0.5           0.7336          0.4205         0.0410               0.3224                     0.0065                    0.0066\n10 0.1           0.3176          0.0086         0.0123               0.3164                     0.0012                    0.0027\n10 0.3           0.4076          0.0986         0.0152               0.3406                     0.0255                    0.0115\n10 0.5           0.6696          0.3606         0.0269               0.3841                     0.0690                    0.0302\n20 0.1           0.3332          0.0217         0.0101               0.3223                     0.0013                    0.0039\n20 0.3           0.3979          0.0864         0.0182               0.3927                     0.0717                    0.0224\n20 0.5           0.6106          0.2992         0.0299               0.4883                     0.1673                    0.0294\n30 0.1           0.3355          0.0237         0.0086               0.3374                     0.0259                    0.0060\n30 0.3           0.3663          0.0546         0.0226               0.4914                     0.1798                    0.0205\n30 0.5           0.4710          0.1593         0.0345               0.6734                     0.3618                    0.0255\n40 0.1           0.3348          0.0222         0.0067               0.3566                     0.0407                    0.0234\n40 0.3           0.3722          0.0595         0.0226               0.5699                     0.2540                    0.0665\n40 0.5           0.5300          0.2174         0.0439               0.7214                     0.4056                    0.0536\n50 0.1           0.3440          0.0296         0.0014               0.3636                     0.0559                    0.0272\n50 0.3           0.4753          0.1608         0.0291               0.6109                     0.3032                    0.0639\n50 0.5           0.7535          0.4390         0.0281               0.7658                     0.4581                    0.0527",
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

_source line 28_

Merged CSV saved to `summary_by_k_full.csv`.

## 结果汇报

### k=30,40,50 各 contamination_p 下的 ΔFPR（non-target subjects）

| k | p=0.1 | p=0.3 | p=0.5 |
|---|-------|-------|-------|
| 30 | 0.026±0.006 | 0.180±0.021 | 0.362±0.026 |
| 40 | 0.041±0.023 | 0.254±0.067 | 0.406±0.054 |
| 50 | 0.056±0.027 | 0.303±0.064 | 0.458±0.053 |

### 关键发现

**ΔFPR 随 k 单调递增** — 在 p=0.5 下，ΔFPR 从 k=1 的 0.002 → k=10 的 0.069 → k=20 的 0.167 → k=30 的 0.362 → k=50 的 0.458。趋势完全符合预期：matching variable 被越多 contaminated subjects 污染，non-target 的 false positive 率越高。

**k=50, p=0.5 时 ΔFPR = 0.458** — 远超 0.05 阈值。non-target subjects 的 FPR 从 baseline 的 ~0.31 飙升到 0.77，matching variable 已完全失效。

**即使 p=0.1（轻度 contamination），k=50 的 ΔFPR 也达到 0.056** — 刚超过 0.05 threshold，说明 88% subject 覆盖率下即使 10% 的 contamination 也足以让 matching variable 不可靠。

**ΔTPR 在高 k 时反而下降** — k=30/p=0.5 的 ΔTPR 只有 0.159（对比 k=1/p=0.5 的 0.518），因为 matching variable 本身被污染后降低了 target subject 上的检测灵敏度。k=50/p=0.5 回升到 0.439，可能是因为极端注入量使得信号仍然压过噪声。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "uuid": "1f83161b-3b47-4aed-9cbd-f5f5d5f1aaa4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQqYfeL8PAXfXfyFa5iXjD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1400,
      "cache_read_input_tokens": 44479,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1400
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

### Task result

_source line 29_

Merged CSV saved to `summary_by_k_full.csv`.

## 结果汇报

### k=30,40,50 各 contamination_p 下的 ΔFPR（non-target subjects）

| k | p=0.1 | p=0.3 | p=0.5 |
|---|-------|-------|-------|
| 30 | 0.026±0.006 | 0.180±0.021 | 0.362±0.026 |
| 40 | 0.041±0.023 | 0.254±0.067 | 0.406±0.054 |
| 50 | 0.056±0.027 | 0.303±0.064 | 0.458±0.053 |

### 关键发现

**ΔFPR 随 k 单调递增** — 在 p=0.5 下，ΔFPR 从 k=1 的 0.002 → k=10 的 0.069 → k=20 的 0.167 → k=30 的 0.362 → k=50 的 0.458。趋势完全符合预期：matching variable 被越多 contaminated subjects 污染，non-target 的 false positive 率越高。

**k=50, p=0.5 时 ΔFPR = 0.458** — 远超 0.05 阈值。non-target subjects 的 FPR 从 baseline 的 ~0.31 飙升到 0.77，matching variable 已完全失效。

**即使 p=0.1（轻度 contamination），k=50 的 ΔFPR 也达到 0.056** — 刚超过 0.05 threshold，说明 88% subject 覆盖率下即使 10% 的 contamination 也足以让 matching variable 不可靠。

**ΔTPR 在高 k 时反而下降** — k=30/p=0.5 的 ΔTPR 只有 0.159（对比 k=1/p=0.5 的 0.518），因为 matching variable 本身被污染后降低了 target subject 上的检测灵敏度。k=50/p=0.5 回升到 0.439，可能是因为极端注入量使得信号仍然压过噪声。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 614083,
  "duration_api_ms": 126810,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "fc3e8615-7c7d-4c03-a8b1-16d8d77a9825",
  "total_cost_usd": 0.51364,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 34038,
    "cache_read_input_tokens": 194035,
    "output_tokens": 8096,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 34038,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 628,
        "cache_read_input_tokens": 44479,
        "cache_creation_input_tokens": 1400,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1400
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1330,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001445,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 8096,
      "cacheReadInputTokens": 194035,
      "cacheCreationInputTokens": 34038,
      "webSearchRequests": 0,
      "costUSD": 0.5121950000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5557bf57-c0ca-4858-a779-a09f9de991e2"
}
```

</details>

---
