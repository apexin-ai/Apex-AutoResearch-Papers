# Research conversation: Read the full contents of /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_co

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ad94fcaf931bacbd0.jsonl`
- **Structured JSON:** [`36dacae5dee2021a59c4.json`](../../sessions/36/36dacae5dee2021a59c4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

5 recorded events

### User

_source line 1 · 2026-05-22T19:00:12.436Z_

Read the full contents of /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_condition_dominance.py and report the entire file content back to me. I need to understand how data is constructed (panels, K_eff, eta_max, ASR, judge IDs, conditions, etc.) so I can replicate the same data pipeline in a new script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "f7e118f8-9665-4cde-97a8-ca7f36b0435c",
  "agentId": "ad94fcaf931bacbd0",
  "type": "user",
  "uuid": "c239c527-28a5-4e07-8a3e-3b5136e18a18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "c3b0d292-dbdb-4721-ada5-ecb6c7ddc3f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T19:00:13.936Z_

I'll read the full contents of that file for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c239c527-28a5-4e07-8a3e-3b5136e18a18",
  "isSidechain": true,
  "agentId": "ad94fcaf931bacbd0",
  "requestId": "req_011CbJ84EzL27Uhvne2wxFgs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f87e8298-41d9-4be0-ae84-2ea145911bd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "c3b0d292-dbdb-4721-ada5-ecb6c7ddc3f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LA2k5zMWWBarHis2TBAVZh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15637,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15637,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 3 · 2026-05-22T19:00:14.078Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R5wh1gRb28Nny2r4Jmd3NM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_condition_dominance.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f87e8298-41d9-4be0-ae84-2ea145911bd8",
  "isSidechain": true,
  "agentId": "ad94fcaf931bacbd0",
  "requestId": "req_011CbJ84EzL27Uhvne2wxFgs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fe01db15-0654-4ae7-81bc-11cd4a48aa6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "c3b0d292-dbdb-4721-ada5-ecb6c7ddc3f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LA2k5zMWWBarHis2TBAVZh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15637,
      "cache_read_input_tokens": 0,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15637
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 106,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15637,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15637,
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

_source line 4 · 2026-05-22T19:00:14.105Z_

<details><summary>↩ Tool result · `toolu_01R5wh1gRb28Nny2r4Jmd3NM`</summary>

```text
1	#!/usr/bin/env python3
2	"""Condition-Dependent Dominance Analysis.
3	
4	For each of 12 conditions (2 datasets x 6 attacks), determines whether
5	K_eff_resid or η_max dominates panel ASR via standardized β comparison
6	and FDR-corrected significance testing.
7	
8	Output:
9	  - artifacts/results/plan001/condition_dominance_15model.json
10	"""
11	
12	import os
13	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
14	
15	import sys
16	sys.path.insert(0, "/root/cert_manip_resist_eval")
17	
18	import json
19	import itertools
20	import numpy as np
21	import statsmodels.api as sm
22	from pathlib import Path
23	from scipy import stats
24	from statsmodels.stats.multitest import multipletests
25	from statsmodels.stats.outliers_influence import variance_inflation_factor
26	
27	from src.utils import setup_logging
28	from src.unified_data_loader import (
29	    ALL_MODELS, DATASETS, ATTACKS,
30	    load_all_scores, load_pairs, load_mi_data,
31	)
32	
33	logger = setup_logging("condition_dominance")
34	
35	EPS = 1e-6
36	FDR_ALPHA = 0.05
37	
38	MODEL_FAMILIES = {
39	    "qwen2.5-72b": "qwen", "qwen2.5-32b": "qwen", "qwen2.5-14b": "qwen",
40	    "llama3.1-70b": "meta", "llama3.1-8b": "meta",
41	    "mistral-large": "mistral",
42	    "claude-opus-4": "anthropic", "claude-sonnet-4": "anthropic",
43	    "claude-3-haiku": "anthropic",
44	    "gpt-5.5": "openai", "gpt-4.1": "openai",
45	    "gpt-4o": "openai", "gpt-4o-mini": "openai",
46	    "gemini-2.5-pro": "google", "gemini-2.5-flash": "google",
47	}
48	
49	
50	def _json_default(obj):
51	    if isinstance(obj, np.floating):
52	        v = float(obj)
53	        return None if (np.isnan(v) or np.isinf(v)) else v
54	    if isinstance(obj, np.integer):
55	        return int(obj)
56	    if isinstance(obj, np.ndarray):
57	        return obj.tolist()
58	    if isinstance(obj, np.bool_):
59	        return bool(obj)
60	    raise TypeError(f"Not JSON serializable: {type(obj)}")
61	
62	
63	def majority_vote(votes):
64	    counts = {"A": 0, "B": 0, "tie": 0}
65	    for v in votes:
66	        counts[v] = counts.get(v, 0) + 1
67	    mc = max(counts.values())
68	    winners = [k for k, c in counts.items() if c == mc]
69	    if len(winners) == 1:
70	        return winners[0]
71	    for w in winners:
72	        if w != "tie":
73	            return w
74	    return "tie"
75	
76	
77	def compute_individual_asr(clean_list, attacked_list, pairs):
78	    n = min(len(clean_list), len(attacked_list), len(pairs))
79	    n_flips = n_correct = 0
80	    for i in range(n):
81	        gt = pairs[i]["ground_truth_winner"]
82	        if clean_list[i].get("winner", "tie") == gt:
83	            n_correct += 1
84	            if attacked_list[i].get("winner", "tie") != gt:
85	                n_flips += 1
86	    return n_flips / max(n_correct, 1)
87	
88	
89	def compute_panel_asr(jids, clean, attacked, pairs):
90	    n = min(len(pairs), *(len(clean[j]) for j in jids),
91	            *(len(attacked[j]) for j in jids))
92	    n_flips = n_correct = 0
93	    for i in range(n):
94	        gt = pairs[i]["ground_truth_winner"]
95	        cv = majority_vote([clean[j][i].get("winner", "tie") for j in jids])
96	        if cv != gt:
97	            continue
98	        n_correct += 1
99	        av = majority_vote([attacked[j][i].get("winner", "tie") for j in jids])
100	        if av != gt:
101	            n_flips += 1
102	    return n_flips / max(n_correct, 1)
103	
104	
105	# ── Main ────────────────────────────────────────────────────────────
106	
107	def main():
108	    logger.info("=" * 60)
109	    logger.info("Condition-Dependent Dominance Analysis (15 models)")
110	    logger.info("=" * 60)
111	
112	    mi_data = load_mi_data()
113	    pairs = load_pairs()
114	    clean, attacked = load_all_scores()
115	
116	    # Precompute individual ASR for all (ds, atk, model) triples
117	    logger.info("\nComputing individual ASR...")
118	    ind_asr = {}
119	    for ds in DATASETS:
120	        for atk in ATTACKS:
121	            for mid in ALL_MODELS:
122	                if mid in clean[ds] and mid in attacked[ds][atk]:
123	                    ind_asr[(ds, atk, mid)] = compute_individual_asr(
124	                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]
125	                    )
126	    logger.info(f"  Computed {len(ind_asr)} individual ASR values")
127	
128	    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))
129	    logger.info(f"  Total panels: {len(all_combos)}")
130	
131	    # ── Per-condition analysis ──────────────────────────────────────
132	    condition_data = {}
133	    raw_eta_ps = []
134	    raw_kresid_ps = []
135	    valid_keys = []
136	
137	    for ds in DATASETS:
138	        keff_data = mi_data["keff_per_panel"].get(ds, {})
139	        for atk in ATTACKS:
140	            cond = f"{ds}x{atk}"
141	            logger.info(f"\n--- {cond} ---")
142	
143	            p_asrs, p_keffs, p_etas = [], [], []
144	            skipped = 0
145	
146	            for combo in all_combos:
147	                jids = [ALL_MODELS[i] for i in combo]
148	                if not all((ds, atk, j) in ind_asr for j in jids):
149	                    skipped += 1
150	                    continue
151	                pk = "|".join(jids)
152	                if pk not in keff_data:
153	                    skipped += 1
154	                    continue
155	
156	                keff = keff_data[pk]["keff"]
157	                etas = [ind_asr[(ds, atk, j)] for j in jids]
158	                eta_max = max(etas)
159	
160	                cs = {j: clean[ds][j] for j in jids}
161	                ats = {j: attacked[ds][atk][j] for j in jids}
162	                p_asr = compute_panel_asr(jids, cs, ats, pairs[ds])
163	
164	                p_asrs.append(p_asr)
165	                p_keffs.append(keff)
166	                p_etas.append(eta_max)
167	
168	            n_panels = len(p_asrs)
169	            logger.info(f"  {n_panels} panels, {skipped} skipped")
170	
171	            if n_panels < 10:
172	                logger.warning(f"  Too few panels, skipping")
173	                continue
174	
175	            p_asrs = np.array(p_asrs)
176	            p_keffs = np.array(p_keffs)
177	            p_etas = np.array(p_etas)
178	
179	            if np.std(p_asrs) < 1e-10:
180	                logger.warning(f"  Constant ASR ({p_asrs[0]:.4f}), skipping")
181	                continue
182	
183	            # ── Part 1: Standardized β comparison ──
184	            # Full OLS in log space (same as step4)
185	            log_keff = np.log(p_keffs)
186	            log_eta = np.log(p_etas + EPS)
187	            y = np.log(p_asrs + EPS)
188	
189	            X = np.column_stack([log_keff, log_eta])
190	            Xc = sm.add_constant(X)
191	            fit_full = sm.OLS(y, Xc).fit()
192	
193	            # Partial p-values from full OLS
194	            keff_p = float(fit_full.pvalues[1])
195	            eta_p = float(fit_full.pvalues[2])
196	
197	            # Standardized β = raw_β × SD(x) / SD(y)
198	            sd_y = np.std(y)
199	            keff_std_beta = float(fit_full.params[1] * np.std(log_keff) / sd_y)
200	            eta_std_beta = float(fit_full.params[2] * np.std(log_eta) / sd_y)
201	
202	            # Also compute residualized K_eff for verification
203	            keff_resid = sm.OLS(log_keff, sm.add_constant(log_eta)).fit().resid
204	            fit_resid = sm.OLS(y, sm.add_constant(keff_resid)).fit()
205	            kresid_p_check = float(fit_resid.pvalues[1])
206	
207	            dominance_ratio = abs(keff_std_beta) / max(abs(eta_std_beta), 1e-12)
208	
209	            # ── Part 2: Condition-level features ──
210	            # Individual ASR stats across all 15 models
211	            indiv_asrs = [
212	                ind_asr[(ds, atk, m)]
213	                for m in ALL_MODELS if (ds, atk, m) in ind_asr
214	            ]
215	            mean_indiv_asr = float(np.mean(indiv_asrs))
216	            indiv_asr_range = float(max(indiv_asrs) - min(indiv_asrs))
217	            indiv_asr_std = float(np.std(indiv_asrs))
218	            n_models_with_data = len(indiv_asrs)
219	
220	            # Per-model breakdown
221	            indiv_detail = {}
222	            for m in ALL_MODELS:
223	                if (ds, atk, m) in ind_asr:
224	                    indiv_detail[m] = {
225	                        "asr": ind_asr[(ds, atk, m)],
226	                        "family": MODEL_FAMILIES.get(m, "unknown"),
227	                    }
228	
229	            cd = {
230	                "n_panels": n_panels,
231	                "n_models": n_models_with_data,
232	                "dataset": ds,
233	                "attack": atk,
234	                # Standardized regression results (from full OLS)
235	                "keff_std_beta": keff_std_beta,
236	                "eta_std_beta": eta_std_beta,
237	                "keff_raw_p": keff_p,
238	                "eta_raw_p": eta_p,
239	                "kresid_p_check": kresid_p_check,
240	                "dominance_ratio": float(dominance_ratio),
241	                "R2": float(fit_full.rsquared),
242	                "vif_keff": float(variance_inflation_factor(Xc, 1)),
243	                "vif_eta": float(variance_inflation_factor(Xc, 2)),
244	                # Panel-level stats
245	                "avg_panel_asr": float(np.mean(p_asrs)),
246	                "panel_asr_std": float(np.std(p_asrs)),
247	                "eta_max_mean": float(np.mean(p_etas)),
248	                "eta_max_sd": float(np.std(p_etas)),
249	                "keff_mean": float(np.mean(p_keffs)),
250	                "keff_sd": float(np.std(p_keffs)),
251	                # Individual ASR stats
252	                "mean_indiv_asr": mean_indiv_asr,
253	                "indiv_asr_range": indiv_asr_range,
254	                "indiv_asr_std": indiv_asr_std,
255	                "indiv_detail": indiv_detail,
256	            }
257	            condition_data[cond] = cd
258	            raw_eta_ps.append(eta_p)
259	            raw_kresid_ps.append(keff_p)
260	            valid_keys.append(cond)
261	
262	            logger.info(
263	                f"  Std β: K_eff={keff_std_beta:+.4f} (p={keff_p:.2e}), "
264	                f"η_max={eta_std_beta:+.4f} (p={eta_p:.2e}), "
265	                f"ratio={dominance_ratio:.2f}, R²={fit_full.rsquared:.4f}, "
266	                f"VIF={variance_inflation_factor(Xc, 1):.2f}"
267	            )
268	
269	    # ── FDR correction (Benjamini-Hochberg) ─────────────────────────
270	    logger.info(f"\nApplying FDR correction across {len(valid_keys)} conditions...")
271	    _, fdr_eta, _, _ = multipletests(raw_eta_ps, method="fdr_bh")
272	    _, fdr_kresid, _, _ = multipletests(raw_kresid_ps, method="fdr_bh")
273	
274	    for i, ck in enumerate(valid_keys):
275	        condition_data[ck]["eta_fdr_p"] = float(fdr_eta[i])
276	        condition_data[ck]["kresid_fdr_p"] = float(fdr_kresid[i])
277	
278	        eta_sig = fdr_eta[i] < FDR_ALPHA
279	        kresid_sig = fdr_kresid[i] < FDR_ALPHA
280	
281	        if eta_sig and not kresid_sig:
282	            cat = "eta_max_dominant"
283	        elif kresid_sig and not eta_sig:
284	            cat = "K_eff_dominant"
285	        elif eta_sig and kresid_sig:
286	            cat = "co-dominant"
287	        else:
288	            cat = "neither"
289	        condition_data[ck]["category"] = cat
290	
291	    # ── TABLE 1: Dominance Classification ───────────────────────────
292	    logger.info("\n" + "=" * 160)
293	    logger.info("TABLE 1: Dominance Classification (Standardized β)")
294	    logger.info("=" * 160)
295	    hdr = (
296	        f"{'Condition':<32} {'η_std_β':>8} {'K_std_β':>8} {'Ratio':>6} "
297	        f"{'η_FDR_p':>10} {'K_FDR_p':>10} {'Category':<18} "
298	        f"{'AvgASR':>7} {'η_SD':>7} {'MeanIndiv':>9} {'ASRRange':>8}"
299	    )
300	    logger.info(hdr)
301	    logger.info("-" * 160)
302	    for ck in valid_keys:
303	        d = condition_data[ck]
304	        sig_e = "***" if d["eta_fdr_p"] < 0.001 else "**" if d["eta_fdr_p"] < 0.01 else "*" if d["eta_fdr_p"] < 0.05 else "ns"
305	        sig_k = "***" if d["kresid_fdr_p"] < 0.001 else "**" if d["kresid_fdr_p"] < 0.01 else "*" if d["kresid_fdr_p"] < 0.05 else "ns"
306	        logger.info(
307	            f"  {ck:<30} {d['eta_std_beta']:>+8.4f} {d['keff_std_beta']:>+8.4f} "
308	            f"{d['dominance_ratio']:>6.2f} "
309	            f"{d['eta_fdr_p']:>9.2e}{sig_e:>3} {d['kresid_fdr_p']:>9.2e}{sig_k:>3} "
310	            f"{d['category']:<18} "
311	            f"{d['avg_panel_asr']:>7.4f} {d['eta_max_sd']:>7.4f} "
312	            f"{d['mean_indiv_asr']:>9.4f} {d['indiv_asr_range']:>8.4f}"
313	        )
314	
315	    # ── TABLE 2: Category Summary ──────────────────────────────────
316	    logger.info("\n" + "=" * 120)
317	    logger.info("TABLE 2: Category Summary")
318	    logger.info("=" * 120)
319	
320	    categories = {}
321	    for ck in valid_keys:
322	        cat = condition_data[ck]["category"]
323	        if cat not in categories:
324	            categories[cat] = {
325	                "conditions": [],
326	                "attacks": set(),
327	                "indiv_ranges": [],
328	                "avg_asrs": [],
329	                "mean_indiv_asrs": [],
330	                "eta_sds": [],
331	                "keff_sds": [],
332	            }
333	        categories[cat]["conditions"].append(ck)
334	        categories[cat]["attacks"].add(condition_data[ck]["attack"])
335	        categories[cat]["indiv_ranges"].append(condition_data[ck]["indiv_asr_range"])
336	        categories[cat]["avg_asrs"].append(condition_data[ck]["avg_panel_asr"])
337	        categories[cat]["mean_indiv_asrs"].append(condition_data[ck]["mean_indiv_asr"])
338	        categories[cat]["eta_sds"].append(condition_data[ck]["eta_max_sd"])
339	        categories[cat]["keff_sds"].append(condition_data[ck]["keff_sd"])
340	
341	    hdr2 = f"{'Category':<18} {'N':>3} {'Conditions':<55} {'Attacks':<40} {'AvgRange':>8}"
342	    logger.info(hdr2)
343	    logger.info("-" * 130)
344	    for cat in ["K_eff_dominant", "eta_max_dominant", "co-dominant", "neither"]:
345	        if cat not in categories:
346	            continue
347	        info = categories[cat]
348	        logger.info(
349	            f"  {cat:<16} {len(info['conditions']):>3} "
350	            f"{', '.join(info['conditions']):<55} "
351	            f"{', '.join(sorted(info['attacks'])):<40} "
352	            f"{np.mean(info['indiv_ranges']):>8.4f}"
353	        )
354	
355	    # ── Systematic Difference Analysis ──────────────────────────────
356	    logger.info("\n" + "=" * 120)
357	    logger.info("SYSTEMATIC DIFFERENCE ANALYSIS")
358	    logger.info("=" * 120)
359	
360	    for cat in ["K_eff_dominant", "eta_max_dominant", "co-dominant", "neither"]:
361	        if cat not in categories:
362	            continue
363	        info = categories[cat]
364	        logger.info(f"\n  {cat} (n={len(info['conditions'])}):")
365	        logger.info(f"    Mean panel ASR:      {np.mean(info['avg_asrs']):.4f}")
366	        logger.info(f"    Mean η_max SD:       {np.mean(info['eta_sds']):.4f}")
367	        logger.info(f"    Mean K_eff SD:       {np.mean(info['keff_sds']):.4f}")
368	        logger.info(f"    Mean indiv ASR:      {np.mean(info['mean_indiv_asrs']):.4f}")
369	        logger.info(f"    Mean indiv ASR range: {np.mean(info['indiv_ranges']):.4f}")
370	
371	    # Cross-category comparison: K_eff dom vs η_max dom
372	    if "K_eff_dominant" in categories and "eta_max_dominant" in categories:
373	        k_info = categories["K_eff_dominant"]
374	        e_info = categories["eta_max_dominant"]
375	        logger.info("\n  --- K_eff_dominant vs η_max_dominant ---")
376	        for metric, k_vals, e_vals in [
377	            ("Avg panel ASR", k_info["avg_asrs"], e_info["avg_asrs"]),
378	            ("Mean indiv ASR", k_info["mean_indiv_asrs"], e_info["mean_indiv_asrs"]),
379	            ("Indiv ASR range", k_info["indiv_ranges"], e_info["indiv_ranges"]),
380	            ("η_max SD", k_info["eta_sds"], e_info["eta_sds"]),
381	            ("K_eff SD", k_info["keff_sds"], e_info["keff_sds"]),
382	        ]:
383	            k_mean = np.mean(k_vals)
384	            e_mean = np.mean(e_vals)
385	            logger.info(f"    {metric:<22}: K_dom={k_mean:.4f}  η_dom={e_mean:.4f}  diff={k_mean - e_mean:+.4f}")
386	
387	    # Attack type → dominance mapping
388	    logger.info("\n  --- Attack Type → Dominance Mapping ---")
389	    atk_map = {}
390	    for ck in valid_keys:
391	        atk = condition_data[ck]["attack"]
392	        cat = condition_data[ck]["category"]
393	        ds = condition_data[ck]["dataset"]
394	        if atk not in atk_map:
395	            atk_map[atk] = []
396	        atk_map[atk].append(f"{ds}→{cat}")
397	    for atk in ATTACKS:
398	        if atk in atk_map:
399	            logger.info(f"    {atk:<22}: {', '.join(atk_map[atk])}")
400	
401	    # ── Save JSON ───────────────────────────────────────────────────
402	    cat_summary = {}
403	    for cat, info in categories.items():
404	        cat_summary[cat] = {
405	            "conditions": info["conditions"],
406	            "attack_types": sorted(info["attacks"]),
407	            "n_conditions": len(info["conditions"]),
408	            "avg_panel_asr": float(np.mean(info["avg_asrs"])),
409	            "avg_indiv_asr_range": float(np.mean(info["indiv_ranges"])),
410	            "avg_mean_indiv_asr": float(np.mean(info["mean_indiv_asrs"])),
411	            "avg_eta_max_sd": float(np.mean(info["eta_sds"])),
412	            "avg_keff_sd": float(np.mean(info["keff_sds"])),
413	        }
414	
415	    # Remove indiv_detail from condition_data for cleaner JSON
416	    conditions_out = {}
417	    for ck, cd in condition_data.items():
418	        cd_copy = {k: v for k, v in cd.items() if k != "indiv_detail"}
419	        conditions_out[ck] = cd_copy
420	
421	    output = {
422	        "analysis": "condition_dominance_15model",
423	        "n_models": len(ALL_MODELS),
424	        "models": ALL_MODELS,
425	        "fdr_alpha": FDR_ALPHA,
426	        "eps": EPS,
427	        "conditions": conditions_out,
428	        "category_summary": cat_summary,
429	    }
430	
431	    out_dir = Path("/root/cert_manip_resist_eval/artifacts/results/plan001")
432	    out_dir.mkdir(parents=True, exist_ok=True)
433	    out_path = out_dir / "condition_dominance_15model.json"
434	    with open(out_path, "w") as f:
435	        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
436	    logger.info(f"\nSaved: {out_path}")
437	
438	
439	if __name__ == "__main__":
440	    main()
441	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe01db15-0654-4ae7-81bc-11cd4a48aa6c",
  "isSidechain": true,
  "promptId": "f7e118f8-9665-4cde-97a8-ca7f36b0435c",
  "agentId": "ad94fcaf931bacbd0",
  "type": "user",
  "uuid": "a5c8d389-a9be-45a3-8637-94d038c30aad",
  "sourceToolAssistantUUID": "fe01db15-0654-4ae7-81bc-11cd4a48aa6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "c3b0d292-dbdb-4721-ada5-ecb6c7ddc3f4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-22T19:00:31.670Z_

Here's the complete file content with explanation of the data pipeline:

## File: `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_condition_dominance.py`

### Data Pipeline Overview

The script constructs a complex data pipeline with the following key components:

#### **1. Input Data Loading (Lines 112-114)**
```
mi_data = load_mi_data()          # Mutual information / K_eff data
pairs = load_pairs()              # Ground truth judge decisions
clean, attacked = load_all_scores()  # Judge verdicts (clean vs attacked)
```

#### **2. Judge IDs & Model Structure (Lines 38-47, 128)**
- **15 models** defined in `ALL_MODELS` imported from `src.unified_data_loader`
- **Model families** mapped (e.g., "qwen2.5-72b" → "qwen", "claude-opus-4" → "anthropic")
- **Panels**: All 3-judge combinations from 15 models = C(15,3) = 455 panels per condition

#### **3. Individual ASR Calculation (Lines 118-126)**
For each (dataset, attack, judge_model) triple:
```
ind_asr[(ds, atk, mid)] = compute_individual_asr(
    clean[ds][mid],          # Judge's clean decisions
    attacked[ds][atk][mid],  # Judge's attacked decisions  
    pairs[ds]                # Ground truth winners
)
```
- **compute_individual_asr** (Lines 77-86): Among cases where judge agrees with ground truth in clean state, measures fraction that flip when attacked
- Formula: n_flips / max(n_correct, 1)

#### **4. Panel-Level Data Construction (Lines 146-166)**
For each condition (dataset × attack) and each 3-judge panel:

```
For each 3-judge combination:
  - Validate all 3 judges have data for (ds, atk)
  - Retrieve K_eff from mi_data["keff_per_panel"][ds]["|".join(jids)]
  - eta_max = max(ind_asr values for the 3 judges)
  - Compute panel_asr via majority vote of judges' decisions
  
Panel data collected:
  p_asrs   = [panel_asr_1, panel_asr_2, ...]
  p_keffs  = [keff_1, keff_2, ...]
  p_etas   = [eta_max_1, eta_max_2, ...]
```

**compute_panel_asr** (Lines 89-102): For each case:
1. Take majority vote of 3 judges' clean verdicts
2. If majority agrees with ground truth, increment n_correct
3. If attacked majority disagrees with ground truth, increment n_flips
4. Return n_flips / n_correct

#### **5. Condition-Level Features (Lines 137-256)**
For each of 12 conditions (2 datasets × 6 attacks):

**Regression analysis** (log-space OLS):
```
y = log(p_asrs + EPS)
X = [log(p_keffs), log(p_etas + EPS)]
Fit: y ~ X (+ constant)

Extract:
  - Standardized β: raw_β × SD(x) / SD(y)
  - Partial p-values from OLS
  - VIF (variance inflation factors)
  - R²
```

**Individual ASR statistics** (Lines 211-227):
```
indiv_asrs = [ind_asr[(ds, atk, m)] for all m with data]
  - mean_indiv_asr
  - indiv_asr_range (max - min)
  - indiv_asr_std
  - per-model breakdown with family classification
```

**Panel-level statistics**:
```
  - avg_panel_asr, panel_asr_std
  - eta_max_mean, eta_max_sd
  - keff_mean, keff_sd
  - n_panels (valid 3-judge combinations)
```

#### **6. FDR Correction (Lines 269-289)**
- **Benjamini-Hochberg FDR correction** applied across 12 conditions
- Corrects p-values for both η_max and K_eff_resid
- **Dominance classification**:
  - **K_eff_dominant**: K_eff p < 0.05 (FDR), η_max p ≥ 0.05
  - **eta_max_dominant**: η_max p < 0.05 (FDR), K_eff p ≥ 0.05
  - **co-dominant**: Both p < 0.05
  - **neither**: Both p ≥ 0.05

#### **7. Output Structure (Lines 421-436)**
```json
{
  "analysis": "condition_dominance_15model",
  "n_models": 15,
  "models": [list of 15 model names],
  "fdr_alpha": 0.05,
  "eps": 1e-6,
  "conditions": {
    "dataset1xattack1": {
      "n_panels": count,
      "n_models": count with data,
      "keff_std_beta": float,
      "eta_std_beta": float,
      "keff_raw_p": float,
      "eta_raw_p": float,
      "kresid_p_check": float,
      "dominance_ratio": float,
      "R2": float,
      "vif_keff": float,
      "vif_eta": float,
      "avg_panel_asr": float,
      "panel_asr_std": float,
      "eta_max_mean": float,
      "eta_max_sd": float,
      "keff_mean": float,
      "keff_sd": float,
      "mean_indiv_asr": float,
      "indiv_asr_range": float,
      "indiv_asr_std": float,
      "eta_fdr_p": float,
      "kresid_fdr_p": float,
      "category": "K_eff_dominant|eta_max_dominant|co-dominant|neither"
    },
    ...
  },
  "category_summary": {...}
}
```

### Key Data Dependencies

1. **load_mi_data()** → dict with structure `{"keff_per_panel": {ds: {panel_key: {"keff": float}}}}`
2. **load_pairs()** → dict with structure `{ds: [{"ground_truth_winner": "A"|"B"|"tie"}, ...]}`
3. **load_all_scores()** → tuple of two dicts:
   - `clean[ds][model_id] = [{"winner": "A"|"B"|"tie"}, ...]`
   - `attacked[ds][atk][model_id] = [{"winner": "A"|"B"|"tie"}, ...]`

The output is saved to `/root/cert_manip_resist_eval/artifacts/results/plan001/condition_dominance_15model.json`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5c8d389-a9be-45a3-8637-94d038c30aad",
  "isSidechain": true,
  "agentId": "ad94fcaf931bacbd0",
  "requestId": "req_011CbJ84N6xjFmj9auRQTwig",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "92bb0937-bbc1-47a9-a0d7-5a1258164e99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "sessionId": "c3b0d292-dbdb-4721-ada5-ecb6c7ddc3f4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013yRRxmfPcZKYUfv8HhfSBU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 7967,
      "cache_read_input_tokens": 15637,
      "output_tokens": 1791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7967
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1791,
          "cache_read_input_tokens": 15637,
          "cache_creation_input_tokens": 7967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7967,
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
