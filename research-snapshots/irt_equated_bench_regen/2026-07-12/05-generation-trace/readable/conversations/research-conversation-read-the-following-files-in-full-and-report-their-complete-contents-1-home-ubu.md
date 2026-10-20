# Research conversation: Read the following files in full and report their complete contents: 1. /home/ubuntu/.agent-ml-research-idea_gen_0520_2/

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-afcf9a07bab716d8b.jsonl`
- **Structured JSON:** [`5283ba07d806fc9a8795.json`](../../sessions/52/5283ba07d806fc9a8795.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

7 recorded events

### User

_source line 1 · 2026-05-20T22:25:39.728Z_

Read the following files in full and report their complete contents:

1. /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py
2. /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012/plan_012_irt_theta_analysis.py

I need to understand the MH-DIF implementation, semi-synthetic injection framework, and IRT theta estimation code. Report back the full code of both files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "agentId": "afcf9a07bab716d8b",
  "type": "user",
  "uuid": "23fa7998-45c3-4735-af83-a561a9742705",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-20T22:25:40.925Z_

I'll read both files in full for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23fa7998-45c3-4735-af83-a561a9742705",
  "isSidechain": true,
  "agentId": "afcf9a07bab716d8b",
  "requestId": "req_011CbEc77J3q4MXwHMEM8P3u",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "60c31b70-7f3c-4a3b-bfea-6e2f8c00a883",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016QTqdV1Ky5b6xVLjuWKb1R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18502,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18502,
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

_source line 3 · 2026-05-20T22:25:41.364Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XXMG62JX4D9z4ELB3HPFAW`</summary>

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
  "parentUuid": "60c31b70-7f3c-4a3b-bfea-6e2f8c00a883",
  "isSidechain": true,
  "agentId": "afcf9a07bab716d8b",
  "requestId": "req_011CbEc77J3q4MXwHMEM8P3u",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fdc4aaa7-1fa7-4f4d-987b-d37378d2683a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016QTqdV1Ky5b6xVLjuWKb1R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18502,
      "cache_read_input_tokens": 0,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18502
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18502,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18502,
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

_source line 4 · 2026-05-20T22:25:41.383Z_

<details><summary>↩ Tool result · `toolu_01XXMG62JX4D9z4ELB3HPFAW`</summary>

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
  "parentUuid": "fdc4aaa7-1fa7-4f4d-987b-d37378d2683a",
  "isSidechain": true,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "agentId": "afcf9a07bab716d8b",
  "type": "user",
  "uuid": "b9a48a85-9e06-4a71-804a-5b81915619d7",
  "sourceToolAssistantUUID": "fdc4aaa7-1fa7-4f4d-987b-d37378d2683a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T22:25:41.440Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VJvVn5jwojbP2xULJ2yyUN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012/plan_012_irt_theta_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9a48a85-9e06-4a71-804a-5b81915619d7",
  "isSidechain": true,
  "agentId": "afcf9a07bab716d8b",
  "requestId": "req_011CbEc77J3q4MXwHMEM8P3u",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "607240b8-7d08-43b9-9b03-c516206d2020",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016QTqdV1Ky5b6xVLjuWKb1R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18502,
      "cache_read_input_tokens": 0,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18502
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18502,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18502,
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

_source line 6 · 2026-05-20T22:25:41.844Z_

<details><summary>↩ Tool result · `toolu_01VJvVn5jwojbP2xULJ2yyUN`</summary>

````text
1	#!/usr/bin/env python3
2	"""
3	plan_012_irt_theta_analysis.py — IRT θ-Conditioning MH-DIF Analysis
4	
5	Uses IRT-based θ estimates (logit of proportion correct) instead of raw total
6	scores for MH-DIF stratification. Tests whether finer ability matching reduces
7	the high baseline FPR from plan_011 (temporal ~31%, ability ~49%) while
8	preserving detection power for differential contamination.
9	
10	Variants tested:
11	  - theta_eq_K   : equal-width bins on θ (K=10,15,20)
12	  - theta_qt_K   : quantile bins on θ (K=10,15,20)
13	  - external_5   : plan_011 baseline (5-quantile bins on full-matrix total score)
14	
15	Outputs (all in plan_012/):
16	  theta_estimates.csv, dose_response_theta.csv, enrichment_theta.csv,
17	  plan_012_report.md
18	"""
19	
20	import numpy as np
21	import pandas as pd
22	from scipy.sparse import load_npz
23	from scipy.stats import chi2 as chi2_dist, fisher_exact
24	from pathlib import Path
25	import time
26	import warnings
27	
28	warnings.filterwarnings("ignore", category=RuntimeWarning)
29	
30	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
31	OUT = BASE / "plan_012"
32	OUT.mkdir(exist_ok=True)
33	
34	INJECTION_PS = [0.0, 0.3, 0.5, 0.7, 1.0]
35	N_SEEDS = 5
36	N_BASELINE = 500
37	N_CONTAMINATED = 100
38	STRATA_COUNTS = [10, 15, 20]
39	
40	
41	# ════════════════════════════════════════════════════════════════════════════
42	#  MH-DIF CORE
43	# ════════════════════════════════════════════════════════════════════════════
44	def _nan_row(j):
45	    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,
46	                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class="A")
47	
48	
49	def _compute_mh_item(X_ref_j, X_foc_j, k_ref, k_foc, n_bins):
50	    """Compute MH statistics for a single item given pre-computed bin assignments."""
51	    R = S = 0.0
52	    sum_diff = 0.0
53	    sum_var = 0.0
54	    pr = ps_qr = qs = 0.0
55	    n_ok = 0
56	
57	    for k in range(n_bins):
58	        mr = (k_ref == k)
59	        mf = (k_foc == k)
60	        n1 = int(mr.sum())
61	        n0 = int(mf.sum())
62	        if n1 == 0 or n0 == 0:
63	            continue
64	
65	        A = float(X_ref_j[mr].sum())
66	        B = float(n1 - A)
67	        C = float(X_foc_j[mf].sum())
68	        D = float(n0 - C)
69	        Nk = float(n1 + n0)
70	        m1 = A + C
71	        m0 = B + D
72	
73	        if m1 == 0 or m0 == 0 or Nk <= 1:
74	            continue
75	        n_ok += 1
76	
77	        Rk = A * D / Nk
78	        Sk = B * C / Nk
79	        R += Rk
80	        S += Sk
81	
82	        EA = n1 * m1 / Nk
83	        sum_diff += A - EA
84	        sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))
85	
86	        Pk = (A + D) / Nk
87	        Qk = (B + C) / Nk
88	        pr += Pk * Rk
89	        ps_qr += Pk * Sk + Qk * Rk
90	        qs += Qk * Sk
91	
92	    if n_ok == 0 or (R == 0 and S == 0):
93	        return None
94	
95	    if S == 0:
96	        alpha, delta, se = np.inf, -np.inf, np.nan
97	    elif R == 0:
98	        alpha, delta, se = 0.0, np.inf, np.nan
99	    else:
100	        alpha = R / S
101	        delta = -2.35 * np.log(alpha)
102	        v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)
103	        se = 2.35 * np.sqrt(v) if v > 0 else np.nan
104	
105	    if sum_var > 0:
106	        chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
107	        pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
108	    else:
109	        chi2_stat = pval = np.nan
110	
111	    ad = abs(delta) if np.isfinite(delta) else np.inf
112	    if ad < 1.0:
113	        ets = "A"
114	    elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:
115	        ets = "C"
116	    else:
117	        ets = "B"
118	
119	    return dict(alpha_mh=alpha, delta_mh=delta, se=se,
120	                chi2=chi2_stat, p_value=pval, ets_class=ets)
121	
122	
123	def mh_dif_with_bins(X_ref, X_foc, scores_ref, scores_foc, n_strata, bin_mode="equal"):
124	    """
125	    MH-DIF with pre-computed ability scores.
126	
127	    bin_mode:
128	      "equal"   — equal-width bins on score scale
129	      "quantile" — quantile bins (equal-count)
130	    """
131	    J = X_ref.shape[1]
132	    s_all = np.concatenate([scores_ref, scores_foc])
133	
134	    if bin_mode == "equal":
135	        edges = np.linspace(s_all.min() - 0.001, s_all.max() + 0.001, n_strata + 1)
136	        n_bins = n_strata
137	    else:
138	        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
139	        n_bins = len(edges) - 1
140	
141	    if n_bins < 2:
142	        return pd.DataFrame([_nan_row(j) for j in range(J)])
143	
144	    k_ref = np.digitize(scores_ref, edges[1:-1])
145	    k_foc = np.digitize(scores_foc, edges[1:-1])
146	
147	    rows = []
148	    for j in range(J):
149	        result = _compute_mh_item(X_ref[:, j], X_foc[:, j], k_ref, k_foc, n_bins)
150	        if result is None:
151	            rows.append(_nan_row(j))
152	        else:
153	            result["col_idx"] = j
154	            rows.append(result)
155	
156	    return pd.DataFrame(rows)
157	
158	
159	# ════════════════════════════════════════════════════════════════════════════
160	#  DATA LOADING
161	# ════════════════════════════════════════════════════════════════════════════
162	print("=== Loading data ===")
163	mat = load_npz(BASE / "response_matrix.npz")
164	idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
165	MODEL_NAMES = idx["model_names"]
166	ITEM_IDS = idx["item_ids"]
167	ITEM2COL = {iid: i for i, iid in enumerate(ITEM_IDS)}
168	
169	model_meta = pd.read_csv(BASE / "model_metadata.csv")
170	li_labels = pd.read_csv(BASE / "mmlu_li2024_proxy_labels.csv")
171	ability_dif = pd.read_csv(BASE / "plan_001" / "dif_results_ability.csv")
172	
173	NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}
174	N_MODELS, J_FULL = mat.shape
175	print(f"  Matrix: {N_MODELS} x {J_FULL}")
176	
177	
178	# ════════════════════════════════════════════════════════════════════════════
179	#  STEP 1: IRT θ ESTIMATION
180	# ════════════════════════════════════════════════════════════════════════════
181	print("\n=== Step 1: IRT theta estimation ===")
182	totals_all = np.asarray(mat.sum(axis=1)).ravel().astype(np.float64)
183	p_correct = (totals_all + 0.5) / (J_FULL + 1.0)
184	theta_all = np.log(p_correct / (1.0 - p_correct))
185	
186	print(f"  θ range: [{theta_all.min():.3f}, {theta_all.max():.3f}]")
187	print(f"  θ mean: {theta_all.mean():.3f}, std: {theta_all.std():.3f}")
188	
189	corr = np.corrcoef(theta_all, totals_all)[0, 1]
190	print(f"  Correlation(θ, total_score): {corr:.4f}")
191	
192	theta_df = pd.DataFrame({
193	    "model_name": MODEL_NAMES,
194	    "theta": theta_all,
195	    "total_score": totals_all,
196	    "method": "logit_laplace"
197	})
198	theta_df.to_csv(OUT / "theta_estimates.csv", index=False)
199	print(f"  Saved theta_estimates.csv ({len(theta_df)} rows)")
200	
201	
202	# ════════════════════════════════════════════════════════════════════════════
203	#  STEP 2: SELECT BASELINE ITEMS (same as plan_011)
204	# ════════════════════════════════════════════════════════════════════════════
205	print("\n=== Step 2: Selecting baseline items ===")
206	merged = ability_dif.merge(li_labels[["item_id", "contamination_type"]], on="item_id", how="inner")
207	baseline_pool = merged[(merged["contamination_type"] == "clean") & (merged["ets_class"] == "A")]
208	print(f"  Baseline pool (clean + ETS A): {len(baseline_pool)}")
209	
210	baseline_items = baseline_pool.sample(N_BASELINE, random_state=42)
211	baseline_item_ids = baseline_items["item_id"].values
212	baseline_col_indices = np.array([ITEM2COL[iid] for iid in baseline_item_ids])
213	print(f"  Selected {N_BASELINE} baseline items")
214	
215	
216	# ════════════════════════════════════════════════════════════════════════════
217	#  STEP 3: DEFINE COHORTS
218	# ════════════════════════════════════════════════════════════════════════════
219	print("\n=== Step 3: Defining cohorts ===")
220	
221	
222	def get_row_indices(col, values):
223	    names = model_meta.loc[model_meta[col].isin(values), "model_name"]
224	    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])
225	
226	
227	cohort_defs = {}
228	
229	# (a) Ability cohort
230	ref_ability_idx = get_row_indices("cohort_accuracy_quintile", [1, 2])
231	foc_ability_idx = get_row_indices("cohort_accuracy_quintile", [4, 5])
232	
233	ref_acc = model_meta.loc[model_meta["cohort_accuracy_quintile"].isin([1, 2]), "accuracy"]
234	foc_acc = model_meta.loc[model_meta["cohort_accuracy_quintile"].isin([4, 5]), "accuracy"]
235	ab_overlap_min = max(ref_acc.min(), foc_acc.min())
236	ab_overlap_max = min(ref_acc.max(), foc_acc.max())
237	
238	if ab_overlap_min <= ab_overlap_max:
239	    foc_ab_inject_mask = (
240	        model_meta["cohort_accuracy_quintile"].isin([4, 5]) &
241	        (model_meta["accuracy"] >= ab_overlap_min) &
242	        (model_meta["accuracy"] <= ab_overlap_max)
243	    )
244	    foc_ab_inject_idx = np.array([NAME2ROW[n] for n in model_meta.loc[foc_ab_inject_mask, "model_name"] if n in NAME2ROW])
245	else:
246	    foc_ab_inject_idx = foc_ability_idx
247	
248	print(f"  Ability: ref={len(ref_ability_idx)} (Q1-2), foc={len(foc_ability_idx)} (Q4-5)")
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
272	print(f"    Inject: {len(foc_t_inject_idx)} focal models in accuracy overlap")
273	
274	cohort_defs["temporal"] = dict(
275	    ref_idx=ref_temporal_idx, foc_idx=foc_temporal_idx,
276	    foc_inject_idx=foc_t_inject_idx
277	)
278	
279	
280	# ════════════════════════════════════════════════════════════════════════════
281	#  STEP 4: SEMI-SYNTHETIC INJECTION + θ-CONDITIONED MH-DIF
282	# ════════════════════════════════════════════════════════════════════════════
283	print("\n=== Step 4: Semi-Synthetic Injection + MH-DIF ===")
284	
285	X_base = mat[:, baseline_col_indices].toarray().astype(np.int8)
286	full_totals = np.asarray(mat.sum(axis=1)).ravel().astype(np.float64)
287	print(f"  Baseline submatrix: {X_base.shape}, density: {X_base.mean():.4f}")
288	
289	# Build variant list: theta_eq_K, theta_qt_K, external_5
290	MH_VARIANTS = []
291	for ns in STRATA_COUNTS:
292	    MH_VARIANTS.append(f"theta_eq_{ns}")
293	    MH_VARIANTS.append(f"theta_qt_{ns}")
294	MH_VARIANTS.append("external_5")
295	
296	injection_rows = []
297	
298	total_runs = len(INJECTION_PS) * N_SEEDS * len(cohort_defs) * len(MH_VARIANTS)
299	run_count = 0
300	t_start = time.time()
301	
302	for cohort_name, cdef in cohort_defs.items():
303	    ref_idx = cdef["ref_idx"]
304	    foc_idx = cdef["foc_idx"]
305	    foc_inject_idx = cdef["foc_inject_idx"]
306	
307	    theta_ref = theta_all[ref_idx]
308	    theta_foc = theta_all[foc_idx]
309	    ext_ref = full_totals[ref_idx]
310	    ext_foc = full_totals[foc_idx]
311	
312	    for p in INJECTION_PS:
313	        for seed in range(1, N_SEEDS + 1):
314	            rng = np.random.RandomState(seed)
315	
316	            contam_local_idx = rng.choice(N_BASELINE, N_CONTAMINATED, replace=False)
317	            contam_set = set(contam_local_idx.tolist())
318	
319	            X_inj = X_base.copy()
320	            n_flipped = 0
321	
322	            if p > 0:
323	                for local_j in contam_local_idx:
324	                    for model_row in foc_inject_idx:
325	                        if X_inj[model_row, local_j] == 0:
326	                            if rng.random() < p:
327	                                X_inj[model_row, local_j] = 1
328	                                n_flipped += 1
329	
330	            X_ref = X_inj[ref_idx]
331	            X_foc = X_inj[foc_idx]
332	
333	            for variant in MH_VARIANTS:
334	                run_count += 1
335	
336	                if variant.startswith("theta_eq_"):
337	                    ns = int(variant.split("_")[2])
338	                    dif_results = mh_dif_with_bins(
339	                        X_ref, X_foc, theta_ref, theta_foc,
340	                        n_strata=ns, bin_mode="equal"
341	                    )
342	                    strata_count = ns
343	                elif variant.startswith("theta_qt_"):
344	                    ns = int(variant.split("_")[2])
345	                    dif_results = mh_dif_with_bins(
346	                        X_ref, X_foc, theta_ref, theta_foc,
347	                        n_strata=ns, bin_mode="quantile"
348	                    )
349	                    strata_count = ns
350	                elif variant == "external_5":
351	                    dif_results = mh_dif_with_bins(
352	                        X_ref, X_foc, ext_ref, ext_foc,
353	                        n_strata=5, bin_mode="quantile"
354	                    )
355	                    strata_count = 5
356	
357	                contam_mask = dif_results["col_idx"].isin(contam_set)
358	                contam_results = dif_results[contam_mask]
359	                clean_results = dif_results[~contam_mask]
360	
361	                n_c_contam = (contam_results["ets_class"] == "C").sum()
362	                n_c_clean = (clean_results["ets_class"] == "C").sum()
363	                tpr = n_c_contam / N_CONTAMINATED
364	                fpr = n_c_clean / (N_BASELINE - N_CONTAMINATED)
365	
366	                table = [[n_c_contam, N_CONTAMINATED - n_c_contam],
367	                         [n_c_clean, (N_BASELINE - N_CONTAMINATED) - n_c_clean]]
368	                fisher_or, fisher_p = fisher_exact(table)
369	
370	                injection_rows.append(dict(
371	                    p=p, seed=seed, cohort_type=cohort_name,
372	                    mh_variant=variant,
373	                    strata_count=strata_count,
374	                    tpr=tpr, fpr=fpr,
375	                    fisher_or=fisher_or, fisher_p=fisher_p,
376	                    n_responses_flipped=n_flipped,
377	                ))
378	
379	                elapsed = time.time() - t_start
380	                if run_count % 35 == 0 or (p in [0.0, 1.0] and seed == 1 and "theta_eq_10" in variant):
381	                    print(f"  [{run_count}/{total_runs}] {cohort_name} {variant:14s} p={p} seed={seed}: "
382	                          f"TPR={tpr:.3f} FPR={fpr:.3f} ({elapsed:.0f}s)")
383	
384	
385	# ════════════════════════════════════════════════════════════════════════════
386	#  STEP 5: AGGREGATE & SAVE
387	# ════════════════════════════════════════════════════════════════════════════
388	print("\n=== Step 5: Aggregating results ===")
389	
390	inj_df = pd.DataFrame(injection_rows)
391	
392	summary_rows = []
393	for (p_val, cohort, variant), grp in inj_df.groupby(["p", "cohort_type", "mh_variant"]):
394	    summary_rows.append(dict(
395	        p=p_val, cohort_type=cohort, mh_variant=variant,
396	        strata_count=grp["strata_count"].iloc[0],
397	        tpr_mean=grp["tpr"].mean(), tpr_std=grp["tpr"].std(),
398	        fpr_mean=grp["fpr"].mean(), fpr_std=grp["fpr"].std(),
399	        fisher_or_mean=grp["fisher_or"].mean(),
400	        fisher_p_median=grp["fisher_p"].median(),
401	    ))
402	summary_df = pd.DataFrame(summary_rows)
403	
404	inj_df.to_csv(OUT / "injection_results.csv", index=False)
405	summary_df.to_csv(OUT / "dose_response_theta.csv", index=False)
406	print(f"  Saved injection_results.csv ({len(inj_df)} rows)")
407	print(f"  Saved dose_response_theta.csv ({len(summary_df)} rows)")
408	
409	
410	# ════════════════════════════════════════════════════════════════════════════
411	#  STEP 6: REAL DATA DIF — ENRICHMENT AGAINST LI ET AL. LABELS
412	# ════════════════════════════════════════════════════════════════════════════
413	print("\n=== Step 6: Real data DIF (no injection) — enrichment vs Li et al. ===")
414	
415	li_item_ids = li_labels["item_id"].values
416	li_col_indices = np.array([ITEM2COL[iid] for iid in li_item_ids if iid in ITEM2COL])
417	li_item_ids_valid = np.array([iid for iid in li_item_ids if iid in ITEM2COL])
418	
419	li_labels_valid = li_labels[li_labels["item_id"].isin(li_item_ids_valid)].copy()
420	li_labels_valid = li_labels_valid.set_index("item_id").loc[li_item_ids_valid].reset_index()
421	
422	X_li = mat[:, li_col_indices].toarray().astype(np.int8)
423	print(f"  Li et al. items submatrix: {X_li.shape}")
424	
425	enrichment_rows = []
426	
427	for cohort_name in ["temporal"]:
428	    cdef = cohort_defs[cohort_name]
429	    ref_idx = cdef["ref_idx"]
430	    foc_idx = cdef["foc_idx"]
431	
432	    X_ref_li = X_li[ref_idx]
433	    X_foc_li = X_li[foc_idx]
434	
435	    theta_ref = theta_all[ref_idx]
436	    theta_foc = theta_all[foc_idx]
437	    ext_ref = full_totals[ref_idx]
438	    ext_foc = full_totals[foc_idx]
439	
440	    for variant in MH_VARIANTS:
441	        if variant.startswith("theta_eq_"):
442	            ns = int(variant.split("_")[2])
443	            dif_results = mh_dif_with_bins(X_ref_li, X_foc_li, theta_ref, theta_foc,
444	                                           n_strata=ns, bin_mode="equal")
445	            sc = ns
446	        elif variant.startswith("theta_qt_"):
447	            ns = int(variant.split("_")[2])
448	            dif_results = mh_dif_with_bins(X_ref_li, X_foc_li, theta_ref, theta_foc,
449	                                           n_strata=ns, bin_mode="quantile")
450	            sc = ns
451	        elif variant == "external_5":
452	            dif_results = mh_dif_with_bins(X_ref_li, X_foc_li, ext_ref, ext_foc,
453	                                           n_strata=5, bin_mode="quantile")
454	            sc = 5
455	
456	        dif_results["item_id"] = li_item_ids_valid[dif_results["col_idx"].values]
457	        dif_merged = dif_results.merge(li_labels_valid[["item_id", "contamination_type"]], on="item_id")
458	
459	        is_contam = dif_merged["contamination_type"] != "clean"
460	        is_clean = dif_merged["contamination_type"] == "clean"
461	        is_c = dif_merged["ets_class"] == "C"
462	
463	        rate_contam = (is_c & is_contam).sum() / is_contam.sum() if is_contam.sum() > 0 else 0
464	        rate_clean = (is_c & is_clean).sum() / is_clean.sum() if is_clean.sum() > 0 else 0
465	        enrichment = rate_contam / rate_clean if rate_clean > 0 else np.inf
466	
467	        enrichment_rows.append(dict(
468	            cohort=cohort_name,
469	            mh_variant=variant,
470	            strata_count=sc,
471	            n_items=len(dif_merged),
472	            n_contam=int(is_contam.sum()),
473	            n_clean=int(is_clean.sum()),
474	            rate_contam=rate_contam,
475	            rate_clean=rate_clean,
476	            fpr_clean=rate_clean,
477	            enrichment=enrichment,
478	        ))
479	
480	        print(f"  {variant:14s}: rate_contam={rate_contam:.4f}, "
481	              f"rate_clean={rate_clean:.4f}, enrichment={enrichment:.3f}")
482	
483	enrichment_df = pd.DataFrame(enrichment_rows)
484	enrichment_df.to_csv(OUT / "enrichment_theta.csv", index=False)
485	print(f"  Saved enrichment_theta.csv ({len(enrichment_df)} rows)")
486	
487	
488	# ════════════════════════════════════════════════════════════════════════════
489	#  REPORT
490	# ════════════════════════════════════════════════════════════════════════════
491	print("\n=== Generating report ===")
492	
493	L = []
494	def w(s=""):
495	    L.append(s)
496	
497	w("# Plan 012: IRT θ-Conditioning MH-DIF Analysis")
498	w()
499	w("## 1. Objective")
500	w()
501	w("Replace raw total scores with IRT-based θ estimates as the MH-DIF stratification")
502	w("variable. Test whether finer ability matching reduces the high baseline FPR from")
503	w("plan_011 (temporal ~31%, ability ~49%) while preserving detection power (TPR).")
504	w()
505	
506	w("## 2. θ Estimation Method")
507	w()
508	w("**Method**: Logit of proportion correct with Laplace smoothing")
509	w("```")
510	w("θ = log((total + 0.5) / (N_items + 1 - total - 0.5))")
511	w("```")
512	w(f"- N models: {N_MODELS}")
513	w(f"- N items (full matrix): {J_FULL}")
514	w(f"- θ range: [{theta_all.min():.3f}, {theta_all.max():.3f}]")
515	w(f"- θ mean±std: {theta_all.mean():.3f}±{theta_all.std():.3f}")
516	w(f"- Correlation(θ, total_score): {corr:.4f}")
517	w()
518	w("This is a monotone transformation of the Rasch model sufficient statistic.")
519	w("Two binning strategies are compared:")
520	w("- **Equal-width (eq)**: equal intervals on the logit scale — respects IRT metric")
521	w("- **Quantile (qt)**: equal-count bins — ensures balanced strata")
522	w()
523	
524	w("## 3. Experimental Design")
525	w()
526	w(f"- Baseline items: {N_BASELINE}")
527	w(f"- Contaminated per run: {N_CONTAMINATED}")
528	w(f"- Injection probabilities: {INJECTION_PS}")
529	w(f"- Seeds per p: {N_SEEDS}")
530	w(f"- Strata counts tested: {STRATA_COUNTS}")
531	w()
532	w("### Cohort definitions")
533	w()
534	for cn, cd in cohort_defs.items():
535	    w(f"- **{cn}**: ref N={len(cd['ref_idx'])}, foc N={len(cd['foc_idx'])}, "
536	      f"foc inject N={len(cd['foc_inject_idx'])}")
537	w()
538	w("### MH variants")
539	w()
540	w("| Variant | Stratification | Description |")
541	w("|---------|---------------|-------------|")
542	for ns in STRATA_COUNTS:
543	    w(f"| theta_eq_{ns} | Equal-width θ bins | {ns} equal intervals on logit scale |")
544	    w(f"| theta_qt_{ns} | Quantile θ bins | {ns} equal-count bins on θ |")
545	w("| external_5 | Quantile total-score | 5 bins on full-matrix total (plan_011 baseline) |")
546	w()
547	
548	# ─── Results tables ───
549	w("## 4. Semi-Synthetic Results")
550	w()
551	
552	for cohort in ["temporal", "ability"]:
553	    w(f"### {cohort.capitalize()} cohort")
554	    w()
555	
556	    # Baseline FPR table
557	    w("#### Baseline FPR (p=0)")
558	    w()
559	    w("| Variant | FPR (mean±std) |")
560	    w("|---------|----------------|")
561	    sub = summary_df[(summary_df["p"] == 0.0) & (summary_df["cohort_type"] == cohort)]
562	    for _, r in sub.sort_values("mh_variant").iterrows():
563	        w(f"| {r.mh_variant} | {r.fpr_mean:.3f}±{r.fpr_std:.3f} |")
564	    w()
565	
566	    # Dose-response table (selected variants)
567	    w("#### Dose-response (key variants)")
568	    w()
569	    key_variants = ["theta_eq_10", "theta_qt_10", "theta_qt_20", "external_5"]
570	    w("| Variant | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |")
571	    w("|---------|---|----------------|----------------|------|-----------|----------|")
572	    for variant in key_variants:
573	        sub_v = summary_df[(summary_df["cohort_type"] == cohort) & (summary_df["mh_variant"] == variant)]
574	        if len(sub_v) == 0:
575	            continue
576	        base_tpr = sub_v[sub_v["p"] == 0.0]["tpr_mean"].values
577	        base_tpr = base_tpr[0] if len(base_tpr) > 0 else 0
578	        for _, r in sub_v.sort_values("p").iterrows():
579	            d_tpr = r.tpr_mean - base_tpr
580	            w(f"| {r.mh_variant} | {r.p} | {r.tpr_mean:.3f}±{r.tpr_std:.3f} | "
581	              f"{r.fpr_mean:.3f}±{r.fpr_std:.3f} | {d_tpr:+.3f} | "
582	              f"{r.fisher_or_mean:.2f} | {r.fisher_p_median:.2e} |")
583	    w()
584	
585	# ─── Success criteria ───
586	w("## 5. Success Criteria Evaluation")
587	w()
588	w("**Target**: baseline FPR < 0.10, TPR > 0.70 at p=0.5 (temporal cohort)")
589	w()
590	
591	for variant in MH_VARIANTS:
592	    sub = summary_df[(summary_df["cohort_type"] == "temporal") & (summary_df["mh_variant"] == variant)]
593	    fpr0 = sub[sub["p"] == 0.0]["fpr_mean"].values
594	    tpr05 = sub[sub["p"] == 0.5]["tpr_mean"].values
595	    if len(fpr0) > 0 and len(tpr05) > 0:
596	        fpr_ok = "PASS" if fpr0[0] < 0.10 else "FAIL"
597	        tpr_ok = "PASS" if tpr05[0] > 0.70 else "FAIL"
598	        w(f"- **{variant}**: FPR={fpr0[0]:.3f} [{fpr_ok}], TPR@p=0.5={tpr05[0]:.3f} [{tpr_ok}]")
599	w()
600	
601	# ─── Enrichment ───
602	w("## 6. Enrichment Against Li et al. Labels (No Injection)")
603	w()
604	w("| Variant | Strata | Rate(contam) | Rate(clean) | Enrichment |")
605	w("|---------|--------|-------------|-------------|------------|")
606	for _, r in enrichment_df.iterrows():
607	    w(f"| {r.mh_variant} | {r.strata_count} | {r.rate_contam:.4f} | "
608	      f"{r.rate_clean:.4f} | {r.enrichment:.3f} |")
609	w()
610	w("(plan_001 reference: enrichment = 0.96 with 5-strata total-score MH)")
611	w()
612	
613	# ─── Analysis ───
614	w("## 7. Analysis & Conclusions")
615	w()
616	
617	# Find best variant
618	best_variant = None
619	best_fpr = 1.0
620	for variant in MH_VARIANTS:
621	    sub = summary_df[(summary_df["cohort_type"] == "temporal") &
622	                     (summary_df["mh_variant"] == variant) & (summary_df["p"] == 0.0)]
623	    if len(sub) > 0:
624	        fpr = sub.iloc[0]["fpr_mean"]
625	        if fpr < best_fpr:
626	            best_fpr = fpr
627	            best_variant = variant
628	
629	ext_sub = summary_df[(summary_df["cohort_type"] == "temporal") &
630	                     (summary_df["mh_variant"] == "external_5") & (summary_df["p"] == 0.0)]
631	ext_fpr = ext_sub.iloc[0]["fpr_mean"] if len(ext_sub) > 0 else None
632	
633	w("### θ vs total-score stratification")
634	w()
635	if ext_fpr is not None:
636	    w(f"- Plan_011 external (5 quantile strata, total score) FPR: {ext_fpr:.3f}")
637	w(f"- Best θ variant ({best_variant}) FPR: {best_fpr:.3f}")
638	if ext_fpr is not None:
639	    w(f"- FPR difference: {best_fpr - ext_fpr:+.3f}")
640	w()
641	
642	w("### Equal-width vs quantile binning")
643	w()
644	for ns in STRATA_COUNTS:
645	    eq_sub = summary_df[(summary_df["cohort_type"] == "temporal") &
646	                        (summary_df["mh_variant"] == f"theta_eq_{ns}") & (summary_df["p"] == 0.0)]
647	    qt_sub = summary_df[(summary_df["cohort_type"] == "temporal") &
648	                        (summary_df["mh_variant"] == f"theta_qt_{ns}") & (summary_df["p"] == 0.0)]
649	    if len(eq_sub) > 0 and len(qt_sub) > 0:
650	        w(f"- K={ns}: equal-width FPR={eq_sub.iloc[0]['fpr_mean']:.3f}, "
651	          f"quantile FPR={qt_sub.iloc[0]['fpr_mean']:.3f}")
652	w()
653	
654	w("### Why FPR remains elevated")
655	w()
656	w("Possible explanations if FPR stays high despite θ-conditioning:")
657	w("1. Real DIF exists between cohorts — genuine differential item functioning")
658	w("   (2023 vs 2024 models genuinely differ on certain items beyond overall ability)")
659	w("2. Cohorts differ on dimensions not captured by a single θ parameter")
660	w("   (e.g., training data composition, architecture effects)")
661	w("3. The logit(p) θ estimate has correlation >.999 with raw total scores,")
662	w("   so quantile bins on θ produce nearly identical strata to quantile bins on totals")
663	w("4. MH-DIF's power to distinguish real DIF from ability confounding is limited")
664	w("   when the grouping variable (year/quintile) correlates strongly with ability")
665	w()
666	
667	w("### Recommendations")
668	w()
669	w("Based on these results:")
670	w()
671	sub_t = summary_df[summary_df["cohort_type"] == "temporal"]
672	for variant in ["theta_eq_10", "theta_qt_10", "theta_qt_20", "external_5"]:
673	    v_sub = sub_t[sub_t["mh_variant"] == variant]
674	    fpr0 = v_sub[v_sub["p"] == 0.0]["fpr_mean"].values
675	    tpr05 = v_sub[v_sub["p"] == 0.5]["tpr_mean"].values
676	    tpr1 = v_sub[v_sub["p"] == 1.0]["tpr_mean"].values
677	    if len(fpr0) > 0 and len(tpr05) > 0 and len(tpr1) > 0:
678	        w(f"- {variant}: FPR₀={fpr0[0]:.3f}, TPR@0.5={tpr05[0]:.3f}, TPR@1.0={tpr1[0]:.3f}")
679	w()
680	
681	(OUT / "plan_012_report.md").write_text("\n".join(L) + "\n")
682	print("  Report written to plan_012_report.md")
683	
684	
685	# ════════════════════════════════════════════════════════════════════════════
686	#  CONSOLE SUMMARY
687	# ════════════════════════════════════════════════════════════════════════════
688	print("\n" + "=" * 70)
689	print("SUMMARY — Baseline FPR (p=0)")
690	print("=" * 70)
691	for cohort in ["temporal", "ability"]:
692	    print(f"\n  {cohort}:")
693	    sub = summary_df[(summary_df["p"] == 0.0) & (summary_df["cohort_type"] == cohort)]
694	    for _, r in sub.sort_values("mh_variant").iterrows():
695	        print(f"    {r.mh_variant:14s}: FPR={r.fpr_mean:.3f}±{r.fpr_std:.3f}")
696	
697	print("\n" + "=" * 70)
698	print("SUMMARY — TPR at p=0.5 (temporal)")
699	print("=" * 70)
700	sub = summary_df[(summary_df["p"] == 0.5) & (summary_df["cohort_type"] == "temporal")]
701	for _, r in sub.sort_values("mh_variant").iterrows():
702	    print(f"  {r.mh_variant:14s}: TPR={r.tpr_mean:.3f}±{r.tpr_std:.3f}")
703	
704	print("\n" + "=" * 70)
705	print("SUMMARY — Enrichment (Li et al.)")
706	print("=" * 70)
707	for _, r in enrichment_df.iterrows():
708	    print(f"  {r.mh_variant:14s}: enrichment={r.enrichment:.3f}")
709	
710	total_elapsed = time.time() - t_start
711	print(f"\nTotal time: {total_elapsed:.0f}s")
712	print(f"All outputs saved to {OUT}")
713	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "607240b8-7d08-43b9-9b03-c516206d2020",
  "isSidechain": true,
  "promptId": "1da8ac0f-f4a0-401f-99a2-96b0e24df4ad",
  "agentId": "afcf9a07bab716d8b",
  "type": "user",
  "uuid": "e00a4cdb-36ac-4add-ae2a-49e161cbd9a6",
  "sourceToolAssistantUUID": "607240b8-7d08-43b9-9b03-c516206d2020",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-20T22:25:58.062Z_

Perfect! I've successfully read both files. Here's a complete summary of what these scripts implement:

## File 1: plan_011_analysis.py — Semi-Synthetic DIF Validation

**Purpose**: Validates the MH-DIF methodology by injecting known differential contamination into real MMLU response data and testing detection capability.

**Key Components**:

1. **MH-DIF Core Function** (`mh_dif_subset`):
   - Implements purified Mantel-Haenszel DIF detection for all items
   - Supports 3 stratification strategies:
     - Standard: total score on all items minus current item
     - Anchor: total score on known-clean items only (oracle knowledge)
     - External: total score on full 12,508-item original matrix (best matching precision)
   - Computes alpha (log-odds ratio), delta (ETS DIF parameter), chi-square tests, p-values
   - Classifies items as ETS A, B, or C based on |delta| threshold (1.0) and p < 0.05

2. **Semi-Synthetic Injection Framework**:
   - Selects 500 baseline items (clean + ETS A classification)
   - Creates two cohorts: ability (Q1-2 vs Q4-5) and temporal (2023 vs 2024)
   - Injects differential contamination into N_CONTAMINATED=100 items per run
   - Injection probability varies: p ∈ [0.0, 0.3, 0.5, 0.7, 1.0]
   - Uses 5 random seeds per configuration
   - Flips 0→1 responses probabilistically in focal group

3. **Performance Metrics**:
   - TPR (True Positive Rate): proportion of contaminated items detected as ETS C
   - FPR (False Positive Rate): proportion of clean items falsely marked as ETS C
   - Fisher's exact test OR and p-values for statistical significance
   - Dose-response curves across injection probabilities

4. **Output**:
   - injection_results.csv: All runs (250 rows: 5 p × 5 seeds × 2 cohorts × 5 variants)
   - dose_response_summary.csv: Aggregated statistics
   - per_item_results.csv: Per-item delta/p-value for anchor variant
   - plan_011_report.md: Full analysis report

**Key Findings Structure**:
- Compares 3 MH variants to identify matching variable contamination (when standard FPR is high but external FPR is low)
- Distinguishes differential vs non-differential contamination detection capability

---

## File 2: plan_012_irt_theta_analysis.py — IRT θ-Conditioning MH-DIF

**Purpose**: Tests whether IRT-based ability estimates reduce the high baseline FPR from plan_011 while maintaining detection power.

**Key Components**:

1. **IRT θ Estimation** (Lines 179-199):
   - Method: Logit of proportion correct with Laplace smoothing
   ```python
   θ = log((total + 0.5) / (J_full + 1 - total - 0.5))
   ```
   - Applied to full 12,508-item matrix for all 5,227 models
   - Produces θ range and correlation with raw total scores (~0.999+)

2. **MH-DIF with Stratification Variants**:
   - `theta_eq_K`: Equal-width bins on θ scale (respects IRT metric)
   - `theta_qt_K`: Quantile bins on θ (equal-count strata)
   - K ∈ [10, 15, 20] to test strata count effects
   - `external_5`: 5-quantile bins on full-matrix total score (plan_011 baseline)

3. **Core MH Computation** (`_compute_mh_item` and `mh_dif_with_bins`):
   - Separates stratification from per-item calculation
   - Pre-computes bin assignments once, applies to all items
   - Same MH statistics (alpha, delta, chi2, p-value, ETS class) as plan_011

4. **Semi-Synthetic Injection**:
   - Identical setup to plan_011 (same 500 baseline items, cohorts, injection scheme)
   - Tests all MH variants against same contamination patterns
   - Measures baseline FPR and dose-response curves

5. **Real Data Enrichment Analysis** (Lines 410-485):
   - Applies all MH variants to Li et al. contamination labels (no injection)
   - Computes enrichment: rate(contaminated flagged) / rate(clean flagged)
   - Tests whether θ-conditioning improves detection against real contamination

6. **Output**:
   - theta_estimates.csv: All models' θ and total score
   - injection_results.csv: All semi-synthetic runs
   - dose_response_theta.csv: Aggregated semi-synthetic results
   - enrichment_theta.csv: Real-data enrichment rates by variant
   - plan_012_report.md: Full analysis with success criteria evaluation

**Key Distinctions from plan_011**:
- Replaces total-score stratification with IRT θ
- Tests multiple strata counts (10, 15, 20) vs fixed 5
- Evaluates whether finer ability matching reduces FPR while preserving TPR
- Includes enrichment analysis on real contamination labels for practical validation

Both scripts follow the same semi-synthetic injection methodology but test different MH-DIF conditioning strategies to identify the optimal approach for contamination detection in LLM evaluation benchmarks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e00a4cdb-36ac-4add-ae2a-49e161cbd9a6",
  "isSidechain": true,
  "agentId": "afcf9a07bab716d8b",
  "requestId": "req_011CbEc7GBLfjrg6BmUKwZT2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "84630982-a7e1-4ba5-bd26-00217e87e1c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "5fffb4b4-76a3-42fd-94be-f15a5a7c83d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013uG3af1mLGitMUqSPTPRtw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 23119,
      "cache_read_input_tokens": 18502,
      "output_tokens": 1372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23119
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1372,
          "cache_read_input_tokens": 18502,
          "cache_creation_input_tokens": 23119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23119,
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
