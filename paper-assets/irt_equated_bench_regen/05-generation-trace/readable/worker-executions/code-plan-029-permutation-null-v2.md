# code plan 029 permutation null v2

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 6
- **Recorded user turns:** 0
- **Tool calls:** 1
- **Original source:** `logs/workers/worker_code_plan_029_permutation_null_v2_20260521T102030.log`
- **Structured JSON:** [`675c2dbbd84396daeab6.json`](../../sessions/67/675c2dbbd84396daeab6.json)

## Before a recorded user message

6 recorded events

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
  "session_id": "9f56302d-d4e8-4fe3-a01a-ef0e7bd17f56",
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
    "mcp__agent-ml-research__register_artifact"
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
  "uuid": "f00fccdd-156d-44d8-8a1f-8dd2d20271a0",
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
    "resetsAt": 1779369000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1a28b254-daf1-4130-958f-eff7ef63f5d7",
  "session_id": "9f56302d-d4e8-4fe3-a01a-ef0e7bd17f56"
}
```

---

### Assistant

_source line 4_

Reading the existing script first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9f56302d-d4e8-4fe3-a01a-ef0e7bd17f56",
  "uuid": "7122497b-7e1a-4460-99a4-3492f416c178",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQRAn166Ui31x5ZTN9WWCS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12357,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12357
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

<details open><summary>🔧 Tool call — Read · `toolu_017goqN7HednfRZW5vrnZdXB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/plan_029_permutation_null.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9f56302d-d4e8-4fe3-a01a-ef0e7bd17f56",
  "uuid": "0c96fe23-4da9-4200-a154-a4780a0af926",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQRAn166Ui31x5ZTN9WWCS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12357,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12357
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

_source line 6 · 2026-05-21T10:20:39.311Z_

<details><summary>↩ Tool result · `toolu_017goqN7HednfRZW5vrnZdXB`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_029_permutation_null.py — Permutation null for temporal DIF C%
4	
5	Tests whether the observed ~31.3% C-category rate in temporal DIF (2023 vs 2024)
6	exceeds chance under random label assignment.  1000 permutations, keeping group
7	sizes fixed (N_ref=1080, N_foc=807).
8	
9	Key optimisation: purified scores (and hence strata) are independent of the
10	ref/foc split, so they are precomputed once.  Per-permutation work reduces to
11	two np.bincount calls per item.
12	"""
13	
14	import numpy as np
15	import pandas as pd
16	from scipy.sparse import load_npz
17	from scipy.stats import chi2 as chi2_dist
18	from pathlib import Path
19	import time
20	
21	import matplotlib
22	matplotlib.use("Agg")
23	import matplotlib.pyplot as plt
24	
25	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/"
26	            "projects/irt_equated_bench_regen/artifacts")
27	OUT = BASE / "plan_029_permutation_null"
28	OUT.mkdir(exist_ok=True)
29	
30	N_PERM = 1000
31	N_STRATA = 5
32	SEED = 42
33	
34	# ═══════════════════════════════════════════════════════════════
35	#  DATA
36	# ═══════════════════════════════════════════════════════════════
37	print("Loading data...")
38	t0 = time.time()
39	
40	mat = load_npz(BASE / "response_matrix.npz")
41	X_full = mat.toarray()          # int8, (5227, 12508)
42	del mat
43	
44	idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
45	MODEL_NAMES = idx["model_names"]
46	ITEM_IDS = idx["item_ids"]
47	J = len(ITEM_IDS)
48	
49	meta = pd.read_csv(BASE / "model_metadata.csv")
50	NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}
51	
52	# Temporal subset (1887 models)
53	temporal_mask = meta["cohort_temporal"].isin(["2023", "2024"])
54	temporal_meta = meta[temporal_mask].copy()
55	temporal_rows = np.array([NAME2ROW[n] for n in temporal_meta["model_name"]
56	                          if n in NAME2ROW])
57	name2cohort = dict(zip(meta["model_name"], meta["cohort_temporal"]))
58	is_ref_true = np.array([name2cohort[MODEL_NAMES[r]] == "2023"
59	                         for r in temporal_rows])
60	
61	N_temp = len(temporal_rows)
62	N_ref = int(is_ref_true.sum())
63	N_foc = N_temp - N_ref
64	
65	X_temp = X_full[temporal_rows]   # (1887, 12508) int8
66	del X_full
67	
68	print(f"  N_temporal={N_temp}, N_ref={N_ref}, N_foc={N_foc}, J={J}")
69	print(f"  Loaded in {time.time() - t0:.1f}s")
70	
71	# ═══════════════════════════════════════════════════════════════
72	#  PRECOMPUTE STRATA  (fixed across permutations)
73	# ═══════════════════════════════════════════════════════════════
74	print("Precomputing strata...")
75	t0 = time.time()
76	
77	tot = X_temp.astype(np.float64).sum(axis=1)       # (1887,)
78	purified_all = tot[:, None] - X_temp.astype(np.float64)  # (1887, J)
79	
80	quantiles = np.linspace(0, 1, N_STRATA + 1)
81	edges = np.quantile(purified_all, quantiles, axis=0)  # (6, J)
82	inner_edges = edges[1:-1]                              # (4, J)
83	
84	strata = np.zeros((N_temp, J), dtype=np.int8)
85	for e_idx in range(inner_edges.shape[0]):
86	    strata += (purified_all >= inner_edges[e_idx][None, :]).astype(np.int8)
87	
88	del purified_all, edges, inner_edges
89	
90	MAX_BINS = int(strata.max()) + 1          # should be 5
91	
92	# Transpose for contiguous row access in the hot loop
93	strata_T = strata.T.copy()                # (J, 1887) int8
94	resp_T = X_temp.T.astype(np.float64)      # (J, 1887) float64 — weights for bincount
95	del X_temp, strata
96	
97	print(f"  Done in {time.time() - t0:.1f}s  (MAX_BINS={MAX_BINS})")
98	
99	# ═══════════════════════════════════════════════════════════════
100	#  FAST C% COMPUTATION
101	# ═══════════════════════════════════════════════════════════════
102	MINLEN = 2 * MAX_BINS
103	
104	def compute_c_pct(is_ref):
105	    """Return C-category percentage given a ref/foc boolean mask."""
106	    foc_offset = (~is_ref).astype(np.intp) * MAX_BINS   # (1887,)
107	    n_c = 0
108	
109	    for j in range(J):
110	        s_j = strata_T[j]          # (1887,) int8, contiguous row
111	        r_j = resp_T[j]            # (1887,) float64, contiguous row
112	
113	        combined = s_j.astype(np.intp) + foc_offset
114	
115	        counts = np.bincount(combined, minlength=MINLEN)
116	        correct = np.bincount(combined, weights=r_j, minlength=MINLEN)
117	
118	        n1 = counts[:MAX_BINS].astype(np.float64)
119	        n0 = counts[MAX_BINS:2*MAX_BINS].astype(np.float64)
120	        A  = correct[:MAX_BINS]
121	        C  = correct[MAX_BINS:2*MAX_BINS]
122	        B  = n1 - A
123	        D  = n0 - C
124	        Nk = n1 + n0
125	        m1 = A + C
126	        m0 = B + D
127	
128	        valid = (n1 > 0) & (n0 > 0) & (m1 > 0) & (m0 > 0) & (Nk > 1)
129	        if not valid.any():
130	            continue
131	
132	        Av, Bv, Cv, Dv = A[valid], B[valid], C[valid], D[valid]
133	        Nkv = Nk[valid]
134	        n1v, n0v, m1v, m0v = n1[valid], n0[valid], m1[valid], m0[valid]
135	
136	        R = (Av * Dv / Nkv).sum()
137	        S = (Bv * Cv / Nkv).sum()
138	        if R == 0 or S == 0:
139	            continue
140	
141	        delta = -2.35 * np.log(R / S)
142	        if abs(delta) < 1.5:
143	            continue
144	
145	        EA = n1v * m1v / Nkv
146	        sum_diff = (Av - EA).sum()
147	        sum_var = (n1v * n0v * m1v * m0v / (Nkv * Nkv * (Nkv - 1))).sum()
148	        if sum_var <= 0:
149	            continue
150	
151	        chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
152	        pval = 1.0 - chi2_dist.cdf(chi2_stat, df=1)
153	        if pval < 0.05:
154	            n_c += 1
155	
156	    return n_c / J * 100
157	
158	
159	# ═══════════════════════════════════════════════════════════════
160	#  VERIFY OBSERVED C%
161	# ═══════════════════════════════════════════════════════════════
162	print("\nVerifying observed C%...")
163	t0 = time.time()
164	observed_c = compute_c_pct(is_ref_true)
165	dt_single = time.time() - t0
166	print(f"  Observed C% = {observed_c:.2f}%  ({dt_single:.1f}s)")
167	
168	# ═══════════════════════════════════════════════════════════════
169	#  PERMUTATION TEST
170	# ═══════════════════════════════════════════════════════════════
171	print(f"\nRunning {N_PERM} permutations (seed={SEED}, "
172	      f"est. {dt_single * N_PERM / 60:.0f} min)...")
173	rng = np.random.RandomState(SEED)
174	perm_results = []
175	t_start = time.time()
176	
177	for i in range(N_PERM):
178	    perm_idx = rng.permutation(N_temp)
179	    is_ref_perm = np.zeros(N_temp, dtype=bool)
180	    is_ref_perm[perm_idx[:N_ref]] = True
181	
182	    c_pct = compute_c_pct(is_ref_perm)
183	    perm_results.append(c_pct)
184	
185	    if (i + 1) % 10 == 0:
186	        elapsed = time.time() - t_start
187	        avg = elapsed / (i + 1)
188	        eta = avg * (N_PERM - i - 1)
189	        n_exceed = sum(1 for x in perm_results if x >= observed_c)
190	        print(f"  [{i+1:4d}/{N_PERM}] C%={c_pct:.2f}%  "
191	              f"max_null={max(perm_results):.2f}%  "
192	              f"n_exceed={n_exceed}  "
193	              f"{avg:.1f}s/perm  ETA {eta/60:.1f}min")
194	
195	    if (i + 1) == 100:
196	        n_exc = sum(1 for x in perm_results if x >= observed_c)
197	        print(f"\n  [checkpoint] 100 permutations done, "
198	              f"n_exceed={n_exc}, max_null={max(perm_results):.2f}%")
199	        if n_exc == 0:
200	            print(f"  Already p < 0.01; continuing to {N_PERM} for precision.\n")
201	
202	total_time = time.time() - t_start
203	print(f"\nCompleted {N_PERM} permutations in {total_time / 60:.1f} min")
204	
205	# ═══════════════════════════════════════════════════════════════
206	#  STATISTICS
207	# ═══════════════════════════════════════════════════════════════
208	null = np.array(perm_results)
209	n_exceed = int((null >= observed_c).sum())
210	p_value = (n_exceed + 1) / (N_PERM + 1)     # conservative
211	
212	null_mean = null.mean()
213	null_std  = null.std()
214	null_ci   = (np.percentile(null, 2.5), np.percentile(null, 97.5))
215	null_max  = null.max()
216	null_min  = null.min()
217	
218	print(f"\n{'=' * 55}")
219	print("RESULTS")
220	print(f"{'=' * 55}")
221	print(f"  Observed C%      {observed_c:.2f}%")
222	print(f"  Null mean ± SD   {null_mean:.2f}% ± {null_std:.2f}%")
223	print(f"  Null 95% CI      [{null_ci[0]:.2f}%, {null_ci[1]:.2f}%]")
224	print(f"  Null range       [{null_min:.2f}%, {null_max:.2f}%]")
225	print(f"  N exceed         {n_exceed} / {N_PERM}")
226	p_str = "< 0.001" if p_value < 0.001 else f"= {p_value:.4f}"
227	print(f"  p-value          {p_str}")
228	
229	# ═══════════════════════════════════════════════════════════════
230	#  OUTPUTS
231	# ═══════════════════════════════════════════════════════════════
232	
233	# 1. CSV
234	pd.DataFrame({"permutation": np.arange(1, N_PERM + 1),
235	              "c_pct": perm_results}).to_csv(
236	    OUT / "permutation_results.csv", index=False)
237	
238	# 2. Figure
239	fig, ax = plt.subplots(figsize=(7, 4))
240	ax.hist(null, bins=40, color="#4A90D9", edgecolor="white", alpha=0.85,
241	        label="Null distribution")
242	ax.axvline(observed_c, color="#D9534F", lw=2, ls="--",
243	           label=f"Observed = {observed_c:.1f}%")
244	ax.set_xlabel("C% (ETS category C items)", fontsize=11)
245	ax.set_ylabel("Count", fontsize=11)
246	ax.set_title(f"Permutation Null for Temporal DIF C%\n"
247	             f"(N={N_PERM}, p {p_str})", fontsize=12)
248	ax.legend(fontsize=10)
249	ax.annotate(f"Null: {null_mean:.1f}% ± {null_std:.1f}%\n"
250	            f"Observed: {observed_c:.1f}%\n"
251	            f"p {p_str}",
252	            xy=(0.97, 0.95), xycoords="axes fraction",
253	            ha="right", va="top", fontsize=9,
254	            bbox=dict(boxstyle="round,pad=0.3",
255	                      facecolor="lightyellow", edgecolor="gray"))
256	fig.tight_layout()
257	fig.savefig(OUT / "fig_permutation_null.png", dpi=200)
258	plt.close()
259	
260	# 3. Report
261	report = f"""# Plan 029: Permutation Null for Temporal DIF C%
262	
263	## Purpose
264	
265	Test whether the observed temporal DIF C% significantly exceeds the rate
266	expected under random label assignment.
267	
268	## Method
269	
270	- **Data**: {N_temp} models with temporal labels ({N_ref} "2023", {N_foc} "2024"), {J} items
271	- **Procedure**: {N_PERM} permutations of temporal labels, group sizes fixed
272	- **MH-DIF**: purified matching, {N_STRATA} quantile strata, ETS classification
273	- **Seed**: {SEED}
274	- **Optimisation**: strata precomputed once (invariant to label permutation)
275	
276	## Results
277	
278	| Metric | Value |
279	|--------|-------|
280	| Observed C% | {observed_c:.2f}% |
281	| Null mean ± SD | {null_mean:.2f}% ± {null_std:.2f}% |
282	| Null 95% CI | [{null_ci[0]:.2f}%, {null_ci[1]:.2f}%] |
283	| Null range | [{null_min:.2f}%, {null_max:.2f}%] |
284	| N exceed observed | {n_exceed} / {N_PERM} |
285	| p-value | {p_str} |
286	
287	## Interpretation
288	
289	The observed temporal DIF C% of {observed_c:.2f}% is \
290	{"**far above**" if p_value < 0.001 else "**above**" if p_value < 0.05 else "not above"} \
291	the permutation null (mean {null_mean:.2f}%, max {null_max:.2f}%, \
292	p {p_str}).  The 31.3% C-category rate cannot be attributed to \
293	chance label assignment.
294	
295	## Runtime
296	
297	- Per permutation: ~{dt_single:.1f}s
298	- Total: {total_time / 60:.1f} min ({N_PERM} permutations)
299	"""
300	
301	(OUT / "permutation_null_report.md").write_text(report)
302	
303	print(f"\nOutputs → {OUT}/")
304	for f in ["permutation_results.csv", "fig_permutation_null.png",
305	          "permutation_null_report.md"]:
306	    p = OUT / f
307	    print(f"  {f}  ({p.stat().st_size / 1024:.0f} KB)" if p.exists() else
308	          f"  {f}  MISSING")
309	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9f56302d-d4e8-4fe3-a01a-ef0e7bd17f56",
  "uuid": "81170e6a-7373-40e1-b293-94cbc17e7cb3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null/plan_029_permutation_null.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nplan_029_permutation_null.py — Permutation null for temporal DIF C%\n\nTests whether the observed ~31.3% C-category rate in temporal DIF (2023 vs 2024)\nexceeds chance under random label assignment.  1000 permutations, keeping group\nsizes fixed (N_ref=1080, N_foc=807).\n\nKey optimisation: purified scores (and hence strata) are independent of the\nref/foc split, so they are precomputed once.  Per-permutation work reduces to\ntwo np.bincount calls per item.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\n\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/\"\n            \"projects/irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_029_permutation_null\"\nOUT.mkdir(exist_ok=True)\n\nN_PERM = 1000\nN_STRATA = 5\nSEED = 42\n\n# ═══════════════════════════════════════════════════════════════\n#  DATA\n# ═══════════════════════════════════════════════════════════════\nprint(\"Loading data...\")\nt0 = time.time()\n\nmat = load_npz(BASE / \"response_matrix.npz\")\nX_full = mat.toarray()          # int8, (5227, 12508)\ndel mat\n\nidx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\nMODEL_NAMES = idx[\"model_names\"]\nITEM_IDS = idx[\"item_ids\"]\nJ = len(ITEM_IDS)\n\nmeta = pd.read_csv(BASE / \"model_metadata.csv\")\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}\n\n# Temporal subset (1887 models)\ntemporal_mask = meta[\"cohort_temporal\"].isin([\"2023\", \"2024\"])\ntemporal_meta = meta[temporal_mask].copy()\ntemporal_rows = np.array([NAME2ROW[n] for n in temporal_meta[\"model_name\"]\n                          if n in NAME2ROW])\nname2cohort = dict(zip(meta[\"model_name\"], meta[\"cohort_temporal\"]))\nis_ref_true = np.array([name2cohort[MODEL_NAMES[r]] == \"2023\"\n                         for r in temporal_rows])\n\nN_temp = len(temporal_rows)\nN_ref = int(is_ref_true.sum())\nN_foc = N_temp - N_ref\n\nX_temp = X_full[temporal_rows]   # (1887, 12508) int8\ndel X_full\n\nprint(f\"  N_temporal={N_temp}, N_ref={N_ref}, N_foc={N_foc}, J={J}\")\nprint(f\"  Loaded in {time.time() - t0:.1f}s\")\n\n# ═══════════════════════════════════════════════════════════════\n#  PRECOMPUTE STRATA  (fixed across permutations)\n# ═══════════════════════════════════════════════════════════════\nprint(\"Precomputing strata...\")\nt0 = time.time()\n\ntot = X_temp.astype(np.float64).sum(axis=1)       # (1887,)\npurified_all = tot[:, None] - X_temp.astype(np.float64)  # (1887, J)\n\nquantiles = np.linspace(0, 1, N_STRATA + 1)\nedges = np.quantile(purified_all, quantiles, axis=0)  # (6, J)\ninner_edges = edges[1:-1]                              # (4, J)\n\nstrata = np.zeros((N_temp, J), dtype=np.int8)\nfor e_idx in range(inner_edges.shape[0]):\n    strata += (purified_all >= inner_edges[e_idx][None, :]).astype(np.int8)\n\ndel purified_all, edges, inner_edges\n\nMAX_BINS = int(strata.max()) + 1          # should be 5\n\n# Transpose for contiguous row access in the hot loop\nstrata_T = strata.T.copy()                # (J, 1887) int8\nresp_T = X_temp.T.astype(np.float64)      # (J, 1887) float64 — weights for bincount\ndel X_temp, strata\n\nprint(f\"  Done in {time.time() - t0:.1f}s  (MAX_BINS={MAX_BINS})\")\n\n# ═══════════════════════════════════════════════════════════════\n#  FAST C% COMPUTATION\n# ═══════════════════════════════════════════════════════════════\nMINLEN = 2 * MAX_BINS\n\ndef compute_c_pct(is_ref):\n    \"\"\"Return C-category percentage given a ref/foc boolean mask.\"\"\"\n    foc_offset = (~is_ref).astype(np.intp) * MAX_BINS   # (1887,)\n    n_c = 0\n\n    for j in range(J):\n        s_j = strata_T[j]          # (1887,) int8, contiguous row\n        r_j = resp_T[j]            # (1887,) float64, contiguous row\n\n        combined = s_j.astype(np.intp) + foc_offset\n\n        counts = np.bincount(combined, minlength=MINLEN)\n        correct = np.bincount(combined, weights=r_j, minlength=MINLEN)\n\n        n1 = counts[:MAX_BINS].astype(np.float64)\n        n0 = counts[MAX_BINS:2*MAX_BINS].astype(np.float64)\n        A  = correct[:MAX_BINS]\n        C  = correct[MAX_BINS:2*MAX_BINS]\n        B  = n1 - A\n        D  = n0 - C\n        Nk = n1 + n0\n        m1 = A + C\n        m0 = B + D\n\n        valid = (n1 > 0) & (n0 > 0) & (m1 > 0) & (m0 > 0) & (Nk > 1)\n        if not valid.any():\n            continue\n\n        Av, Bv, Cv, Dv = A[valid], B[valid], C[valid], D[valid]\n        Nkv = Nk[valid]\n        n1v, n0v, m1v, m0v = n1[valid], n0[valid], m1[valid], m0[valid]\n\n        R = (Av * Dv / Nkv).sum()\n        S = (Bv * Cv / Nkv).sum()\n        if R == 0 or S == 0:\n            continue\n\n        delta = -2.35 * np.log(R / S)\n        if abs(delta) < 1.5:\n            continue\n\n        EA = n1v * m1v / Nkv\n        sum_diff = (Av - EA).sum()\n        sum_var = (n1v * n0v * m1v * m0v / (Nkv * Nkv * (Nkv - 1))).sum()\n        if sum_var <= 0:\n            continue\n\n        chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n        pval = 1.0 - chi2_dist.cdf(chi2_stat, df=1)\n        if pval < 0.05:\n            n_c += 1\n\n    return n_c / J * 100\n\n\n# ═══════════════════════════════════════════════════════════════\n#  VERIFY OBSERVED C%\n# ═══════════════════════════════════════════════════════════════\nprint(\"\\nVerifying observed C%...\")\nt0 = time.time()\nobserved_c = compute_c_pct(is_ref_true)\ndt_single = time.time() - t0\nprint(f\"  Observed C% = {observed_c:.2f}%  ({dt_single:.1f}s)\")\n\n# ═══════════════════════════════════════════════════════════════\n#  PERMUTATION TEST\n# ═══════════════════════════════════════════════════════════════\nprint(f\"\\nRunning {N_PERM} permutations (seed={SEED}, \"\n      f\"est. {dt_single * N_PERM / 60:.0f} min)...\")\nrng = np.random.RandomState(SEED)\nperm_results = []\nt_start = time.time()\n\nfor i in range(N_PERM):\n    perm_idx = rng.permutation(N_temp)\n    is_ref_perm = np.zeros(N_temp, dtype=bool)\n    is_ref_perm[perm_idx[:N_ref]] = True\n\n    c_pct = compute_c_pct(is_ref_perm)\n    perm_results.append(c_pct)\n\n    if (i + 1) % 10 == 0:\n        elapsed = time.time() - t_start\n        avg = elapsed / (i + 1)\n        eta = avg * (N_PERM - i - 1)\n        n_exceed = sum(1 for x in perm_results if x >= observed_c)\n        print(f\"  [{i+1:4d}/{N_PERM}] C%={c_pct:.2f}%  \"\n              f\"max_null={max(perm_results):.2f}%  \"\n              f\"n_exceed={n_exceed}  \"\n              f\"{avg:.1f}s/perm  ETA {eta/60:.1f}min\")\n\n    if (i + 1) == 100:\n        n_exc = sum(1 for x in perm_results if x >= observed_c)\n        print(f\"\\n  [checkpoint] 100 permutations done, \"\n              f\"n_exceed={n_exc}, max_null={max(perm_results):.2f}%\")\n        if n_exc == 0:\n            print(f\"  Already p < 0.01; continuing to {N_PERM} for precision.\\n\")\n\ntotal_time = time.time() - t_start\nprint(f\"\\nCompleted {N_PERM} permutations in {total_time / 60:.1f} min\")\n\n# ═══════════════════════════════════════════════════════════════\n#  STATISTICS\n# ═══════════════════════════════════════════════════════════════\nnull = np.array(perm_results)\nn_exceed = int((null >= observed_c).sum())\np_value = (n_exceed + 1) / (N_PERM + 1)     # conservative\n\nnull_mean = null.mean()\nnull_std  = null.std()\nnull_ci   = (np.percentile(null, 2.5), np.percentile(null, 97.5))\nnull_max  = null.max()\nnull_min  = null.min()\n\nprint(f\"\\n{'=' * 55}\")\nprint(\"RESULTS\")\nprint(f\"{'=' * 55}\")\nprint(f\"  Observed C%      {observed_c:.2f}%\")\nprint(f\"  Null mean ± SD   {null_mean:.2f}% ± {null_std:.2f}%\")\nprint(f\"  Null 95% CI      [{null_ci[0]:.2f}%, {null_ci[1]:.2f}%]\")\nprint(f\"  Null range       [{null_min:.2f}%, {null_max:.2f}%]\")\nprint(f\"  N exceed         {n_exceed} / {N_PERM}\")\np_str = \"< 0.001\" if p_value < 0.001 else f\"= {p_value:.4f}\"\nprint(f\"  p-value          {p_str}\")\n\n# ═══════════════════════════════════════════════════════════════\n#  OUTPUTS\n# ═══════════════════════════════════════════════════════════════\n\n# 1. CSV\npd.DataFrame({\"permutation\": np.arange(1, N_PERM + 1),\n              \"c_pct\": perm_results}).to_csv(\n    OUT / \"permutation_results.csv\", index=False)\n\n# 2. Figure\nfig, ax = plt.subplots(figsize=(7, 4))\nax.hist(null, bins=40, color=\"#4A90D9\", edgecolor=\"white\", alpha=0.85,\n        label=\"Null distribution\")\nax.axvline(observed_c, color=\"#D9534F\", lw=2, ls=\"--\",\n           label=f\"Observed = {observed_c:.1f}%\")\nax.set_xlabel(\"C% (ETS category C items)\", fontsize=11)\nax.set_ylabel(\"Count\", fontsize=11)\nax.set_title(f\"Permutation Null for Temporal DIF C%\\n\"\n             f\"(N={N_PERM}, p {p_str})\", fontsize=12)\nax.legend(fontsize=10)\nax.annotate(f\"Null: {null_mean:.1f}% ± {null_std:.1f}%\\n\"\n            f\"Observed: {observed_c:.1f}%\\n\"\n            f\"p {p_str}\",\n            xy=(0.97, 0.95), xycoords=\"axes fraction\",\n            ha=\"right\", va=\"top\", fontsize=9,\n            bbox=dict(boxstyle=\"round,pad=0.3\",\n                      facecolor=\"lightyellow\", edgecolor=\"gray\"))\nfig.tight_layout()\nfig.savefig(OUT / \"fig_permutation_null.png\", dpi=200)\nplt.close()\n\n# 3. Report\nreport = f\"\"\"# Plan 029: Permutation Null for Temporal DIF C%\n\n## Purpose\n\nTest whether the observed temporal DIF C% significantly exceeds the rate\nexpected under random label assignment.\n\n## Method\n\n- **Data**: {N_temp} models with temporal labels ({N_ref} \"2023\", {N_foc} \"2024\"), {J} items\n- **Procedure**: {N_PERM} permutations of temporal labels, group sizes fixed\n- **MH-DIF**: purified matching, {N_STRATA} quantile strata, ETS classification\n- **Seed**: {SEED}\n- **Optimisation**: strata precomputed once (invariant to label permutation)\n\n## Results\n\n| Metric | Value |\n|--------|-------|\n| Observed C% | {observed_c:.2f}% |\n| Null mean ± SD | {null_mean:.2f}% ± {null_std:.2f}% |\n| Null 95% CI | [{null_ci[0]:.2f}%, {null_ci[1]:.2f}%] |\n| Null range | [{null_min:.2f}%, {null_max:.2f}%] |\n| N exceed observed | {n_exceed} / {N_PERM} |\n| p-value | {p_str} |\n\n## Interpretation\n\nThe observed temporal DIF C% of {observed_c:.2f}% is \\\n{\"**far above**\" if p_value < 0.001 else \"**above**\" if p_value < 0.05 else \"not above\"} \\\nthe permutation null (mean {null_mean:.2f}%, max {null_max:.2f}%, \\\np {p_str}).  The 31.3% C-category rate cannot be attributed to \\\nchance label assignment.\n\n## Runtime\n\n- Per permutation: ~{dt_single:.1f}s\n- Total: {total_time / 60:.1f} min ({N_PERM} permutations)\n\"\"\"\n\n(OUT / \"permutation_null_report.md\").write_text(report)\n\nprint(f\"\\nOutputs → {OUT}/\")\nfor f in [\"permutation_results.csv\", \"fig_permutation_null.png\",\n          \"permutation_null_report.md\"]:\n    p = OUT / f\n    print(f\"  {f}  ({p.stat().st_size / 1024:.0f} KB)\" if p.exists() else\n          f\"  {f}  MISSING\")\n",
      "numLines": 309,
      "startLine": 1,
      "totalLines": 309
    }
  }
}
```

</details>

---
