# analysis benchmark statistics — Part 2 of 2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../analysis-benchmark-statistics.md) · [Structured JSON](../../../sessions/d9/d9e0cbf0a05cc8771022.json)

## Round 1

### Tool result

_source line 55 · 2026-05-20T04:19:27.271Z_

<details><summary>↩ Tool result · `toolu_014mvk1vXriN4Bx7xYZUFQ3g`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Statistical analysis of ACR-VLA Conformal Refinement experiments.
4	Compares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.
5	Also includes Argmin and Adaptive-K baselines.
6	"""
7	
8	import numpy as np
9	from scipy import stats
10	
11	def print_separator(char='=', width=80):
12	    print(char * width)
13	
14	def print_group_stats(name, values):
15	    """Print mean +/- std for a group."""
16	    arr = np.array(values)
17	    print(f"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, "
18	          f"min={arr.min():.4f}, max={arr.max():.4f}")
19	    print(f"    values: {[round(v, 4) for v in values]}")
20	
21	def run_tests(name_a, vals_a, name_b, vals_b):
22	    """Run t-test and Mann-Whitney U test between two groups."""
23	    a = np.array(vals_a)
24	    b = np.array(vals_b)
25	
26	    # Independent two-sample t-test (Welch's, unequal variance)
27	    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)
28	
29	    # Mann-Whitney U test (non-parametric)
30	    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')
31	
32	    # Effect size: Cohen's d
33	    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /
34	                         (len(a) + len(b) - 2))
35	    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')
36	
37	    # Difference
38	    diff = a.mean() - b.mean()
39	    diff_pct = diff * 100  # percentage points
40	
41	    print(f"\n  {name_a} vs {name_b}:")
42	    print(f"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)")
43	    print(f"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}")
44	    print(f"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}")
45	    print(f"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})")
46	
47	    return t_pval, u_pval
48	
49	# ============================================================================
50	# DATA FROM REGISTRY (verified from all experiments with conclusion=success)
51	# ============================================================================
52	
53	# --- LIBERO-Spatial ---
54	# CRM obs_only (norm02 variants, K=5 and K=10): seeds 42-48
55	# From registry: seed42=0.35, seed43=0.32(k5) or 0.34(norm02-r2), seed44=0.37(k5-r2) or 0.36(norm02),
56	# seed45=0.34(k5-r2) or 0.34(norm02), seed46=0.33(r2), seed47=0.32(norm02), seed48=0.35(norm02 and crm-spatial)
57	# Using the best-matched K=10 norm02 experiments (primary config):
58	crm_spatial = [0.34, 0.36, 0.34, 0.33, 0.32, 0.35]  # seeds 43-r2, 44, 45, 46-r2, 47, 48
59	# K=5 variants:
60	crm_spatial_k5 = [0.35, 0.32, 0.37, 0.34]  # seeds 42, 43, 44-r2, 45-r2
61	# Combined unique seeds (using K=10 when available, K=5 for seed42):
62	crm_spatial_all = [0.35, 0.34, 0.36, 0.34, 0.33, 0.32, 0.35]  # seeds 42(k5), 43-r2, 44, 45, 46-r2, 47, 48
63	# Fallback from user-provided data (n=8):
64	crm_spatial_user = [0.32, 0.34, 0.36, 0.34, 0.34, 0.33, 0.32, 0.35]
65	
66	# VLA-only Spatial: seeds 42-50
67	vla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30]  # seeds 42, 43, 44, 45, 46, 47, 50
68	# Fallback from user-provided data (n=9):
69	vla_spatial_user = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.30, 0.29]
70	
71	# --- LIBERO-Long ---
72	# CRM obs_only Long: seeds 42-47
73	crm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # seeds 42, 43, 44, 45, 46, 47
74	# User-provided (same):
75	crm_long_user = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]
76	
77	# VLA-only Long: seeds 42-48
78	vla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]  # seeds 42, 43, 44, 45, 46, 47, 48
79	# User-provided (n=7):
80	vla_long_user = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.11]
81	
82	# --- LIBERO-Goal ---
83	# CRM obs_only Goal: seeds 42-46
84	crm_goal = [0.67, 0.72, 0.64, 0.65, 0.72]  # seeds 42, 43, 44-r2, 45-r2, 46
85	# User-provided (same):
86	crm_goal_user = [0.67, 0.72, 0.64, 0.65, 0.72]
87	
88	# VLA-only Goal: seeds 42-46
89	vla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # seeds 42, 43, 44-r2, 45, 46
90	# User-provided (same):
91	vla_goal_user = [0.71, 0.69, 0.73, 0.63, 0.71]
92	
93	# --- LIBERO-Object ---
94	# CRM obs_only Object (norm02, K=10): seeds from registry
95	# Using norm02 K=10 results: seed43-r2=0.16, seed44-r2=0.16, seed45=0.16, seed46=0.15, seed47=0.20, seed48-r2=0.18
96	# Using norm01 results: seed42=0.19, seed44=0.16, seed45-r2=0.17, seed46-r3=0.18, seed47=0.17, seed48=0.18
97	# Using norm02 K=5 results: seed42=0.14, seed43=0.19, seed44=0.17, seed45=0.15, seed46=0.16, seed47=0.13, seed48=0.18
98	# We'll use norm01 as the primary CRM config (best performing, consistent config):
99	crm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # seeds 42, 44, 45-r2, 46-r3, 47, 48
100	# norm02 K=10:
101	crm_object_norm02 = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # seeds 43-r2, 44-r2, 45, 46, 47, 48-r2
102	# norm02 K=5:
103	crm_object_norm02_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # seeds 42-48
104	
105	# VLA-only Object: from registry
106	# seed42=0.12 (overall_sr), seed43=0.12 (overall_sr), seed44-r2=0.10, seed45=0.09(overall_sr),
107	# seed45-r2=0.11, seed46=0.13, seed47=0.10, seed48=0.10, seed50=0.09
108	vla_object = [0.12, 0.12, 0.10, 0.09, 0.13, 0.10, 0.10, 0.09]  # seeds 42, 43, 44-r2, 45, 46, 47, 48, 50
109	# Using seed45-r2 instead of seed45 (more recent run):
110	vla_object_alt = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]
111	
112	# --- Argmin Object ---
113	# K=10: seed43=0.17, seed44-r2=0.13, seed45=0.12, seed46=0.10, seed47=0.10
114	argmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]
115	# K=5: seed42=0.15, seed43=0.13, seed44-r2=0.11, seed45=0.13
116	argmin_object_k5 = [0.15, 0.13, 0.11, 0.13]
117	
118	# Argmin Spatial (only 1 data point from registry)
119	argmin_spatial = [0.34]
120	
121	# --- Adaptive-K Object ---
122	# p25: seed42=0.15, seed43=0.13
123	adaptive_k_p25 = [0.15, 0.13]
124	# p50: seed42=0.16, seed43=0.16, seed44=0.14
125	adaptive_k_p50 = [0.16, 0.16, 0.14]
126	# p75: seed42=0.12, seed43=0.13, seed44=0.16
127	adaptive_k_p75 = [0.12, 0.13, 0.16]
128	# p90: seed42=0.12, seed43=0.14, seed44=0.14
129	adaptive_k_p90 = [0.12, 0.14, 0.14]
130	
131	
132	# ============================================================================
133	# ANALYSIS
134	# ============================================================================
135	
136	print_separator()
137	print("STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments")
138	print("All success rates are fractions (0.0 to 1.0)")
139	print_separator()
140	
141	# ============================================================================
142	# 1. LIBERO-SPATIAL: CRM vs VLA-only
143	# ============================================================================
144	print("\n1. LIBERO-SPATIAL")
145	print_separator('-')
146	print("\n  [Registry data]")
147	print_group_stats("CRM obs_only (registry, n=7)", crm_spatial_all)
148	print_group_stats("VLA-only (registry, n=7)", vla_spatial)
149	run_tests("CRM", crm_spatial_all, "VLA-only", vla_spatial)
150	
151	print("\n  [User-provided data]")
152	print_group_stats("CRM obs_only (user, n=8)", crm_spatial_user)
153	print_group_stats("VLA-only (user, n=9)", vla_spatial_user)
154	run_tests("CRM", crm_spatial_user, "VLA-only", vla_spatial_user)
155	
156	# ============================================================================
157	# 2. LIBERO-LONG: CRM vs VLA-only
158	# ============================================================================
159	print("\n\n2. LIBERO-LONG")
160	print_separator('-')
161	print("\n  [Registry data]")
162	print_group_stats("CRM obs_only (registry, n=6)", crm_long)
163	print_group_stats("VLA-only (registry, n=7)", vla_long)
164	run_tests("CRM", crm_long, "VLA-only", vla_long)
165	
166	print("\n  [User-provided data]")
167	print_group_stats("CRM obs_only (user, n=6)", crm_long_user)
168	print_group_stats("VLA-only (user, n=7)", vla_long_user)
169	run_tests("CRM", crm_long_user, "VLA-only", vla_long_user)
170	
171	# ============================================================================
172	# 3. LIBERO-GOAL: CRM vs VLA-only
173	# ============================================================================
174	print("\n\n3. LIBERO-GOAL")
175	print_separator('-')
176	print("\n  [Registry data = User-provided data]")
177	print_group_stats("CRM obs_only (n=5)", crm_goal)
178	print_group_stats("VLA-only (n=5)", vla_goal)
179	run_tests("CRM", crm_goal, "VLA-only", vla_goal)
180	
181	# ============================================================================
182	# 4. LIBERO-OBJECT: CRM vs VLA-only
183	# ============================================================================
184	print("\n\n4. LIBERO-OBJECT")
185	print_separator('-')
186	
187	print("\n  [CRM norm01 config]")
188	print_group_stats("CRM obs_only norm01 (n=6)", crm_object_norm01)
189	print_group_stats("VLA-only (n=8)", vla_object)
190	run_tests("CRM norm01", crm_object_norm01, "VLA-only", vla_object)
191	
192	print("\n  [CRM norm02 K=10 config]")
193	print_group_stats("CRM obs_only norm02 K=10 (n=6)", crm_object_norm02)
194	print_group_stats("VLA-only (n=8)", vla_object)
195	run_tests("CRM norm02", crm_object_norm02, "VLA-only", vla_object)
196	
197	print("\n  [CRM norm02 K=5 config]")
198	print_group_stats("CRM obs_only norm02 K=5 (n=7)", crm_object_norm02_k5)
199	print_group_stats("VLA-only (n=8)", vla_object)
200	run_tests("CRM norm02 K=5", crm_object_norm02_k5, "VLA-only", vla_object)
201	
202	# ============================================================================
203	# 5. ARGMIN BASELINES (Object)
204	# ============================================================================
205	print("\n\n5. ARGMIN BASELINES (Object)")
206	print_separator('-')
207	print_group_stats("Argmin K=10 (n=5)", argmin_object_k10)
208	print_group_stats("Argmin K=5 (n=4)", argmin_object_k5)
209	print_group_stats("VLA-only (n=8)", vla_object)
210	print_group_stats("CRM norm01 (n=6)", crm_object_norm01)
211	
212	print("\n  Argmin K=10 vs VLA-only:")
213	run_tests("Argmin K=10", argmin_object_k10, "VLA-only", vla_object)
214	print("\n  Argmin K=10 vs CRM norm01:")
215	run_tests("Argmin K=10", argmin_object_k10, "CRM norm01", crm_object_norm01)
216	
217	# ============================================================================
218	# 6. ADAPTIVE-K BASELINES (Object)
219	# ============================================================================
220	print("\n\n6. ADAPTIVE-K BASELINES (Object)")
221	print_separator('-')
222	print_group_stats("Adaptive-K p25 (n=2)", adaptive_k_p25)
223	print_group_stats("Adaptive-K p50 (n=3)", adaptive_k_p50)
224	print_group_stats("Adaptive-K p75 (n=3)", adaptive_k_p75)
225	print_group_stats("Adaptive-K p90 (n=3)", adaptive_k_p90)
226	all_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90
227	print_group_stats("Adaptive-K all (n=11)", all_adaptive)
228	print_group_stats("VLA-only (n=8)", vla_object)
229	print_group_stats("CRM norm01 (n=6)", crm_object_norm01)
230	
231	print("\n  Adaptive-K (all) vs VLA-only:")
232	run_tests("Adaptive-K all", all_adaptive, "VLA-only", vla_object)
233	print("\n  Adaptive-K (all) vs CRM norm01:")
234	run_tests("Adaptive-K all", all_adaptive, "CRM norm01", crm_object_norm01)
235	
236	# ============================================================================
237	# 7. SUMMARY TABLE
238	# ============================================================================
239	print("\n")
240	print_separator()
241	print("SUMMARY TABLE")
242	print_separator()
243	print(f"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'95% CI':>15}")
244	print_separator('-')
245	
246	def print_row(bench, method, vals):
247	    arr = np.array(vals)
248	    n = len(arr)
249	    mean = arr.mean()
250	    std = arr.std(ddof=1)
251	    se = std / np.sqrt(n)
252	    ci_lo = mean - 1.96 * se
253	    ci_hi = mean + 1.96 * se
254	    print(f"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} [{ci_lo:.4f}, {ci_hi:.4f}]")
255	
256	print_row("LIBERO-Spatial", "CRM obs_only", crm_spatial_all)
257	print_row("LIBERO-Spatial", "VLA-only", vla_spatial)
258	print()
259	print_row("LIBERO-Long", "CRM obs_only", crm_long)
260	print_row("LIBERO-Long", "VLA-only", vla_long)
261	print()
262	print_row("LIBERO-Goal", "CRM obs_only", crm_goal)
263	print_row("LIBERO-Goal", "VLA-only", vla_goal)
264	print()
265	print_row("LIBERO-Object", "CRM norm01", crm_object_norm01)
266	print_row("LIBERO-Object", "CRM norm02 K=10", crm_object_norm02)
267	print_row("LIBERO-Object", "CRM norm02 K=5", crm_object_norm02_k5)
268	print_row("LIBERO-Object", "VLA-only", vla_object)
269	print_row("LIBERO-Object", "Argmin K=10", argmin_object_k10)
270	print_row("LIBERO-Object", "Argmin K=5", argmin_object_k5)
271	print_row("LIBERO-Object", "Adaptive-K (all)", all_adaptive)
272	
273	# ============================================================================
274	# 8. KEY FINDINGS
275	# ============================================================================
276	print("\n")
277	print_separator()
278	print("KEY SIGNIFICANCE RESULTS")
279	print_separator()
280	
281	tests = [
282	    ("Spatial: CRM vs VLA", crm_spatial_all, vla_spatial),
283	    ("Long: CRM vs VLA", crm_long, vla_long),
284	    ("Goal: CRM vs VLA", crm_goal, vla_goal),
285	    ("Object(norm01): CRM vs VLA", crm_object_norm01, vla_object),
286	    ("Object(norm02): CRM vs VLA", crm_object_norm02, vla_object),
287	    ("Object: Argmin-K10 vs VLA", argmin_object_k10, vla_object),
288	    ("Object: CRM-norm01 vs Argmin-K10", crm_object_norm01, argmin_object_k10),
289	]
290	
291	print(f"\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}")
292	print('-' * 85)
293	for name, a, b in tests:
294	    arr_a, arr_b = np.array(a), np.array(b)
295	    diff = arr_a.mean() - arr_b.mean()
296	    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)
297	    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')
298	    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /
299	                         (len(a) + len(b) - 2))
300	    d = diff / pooled_std if pooled_std > 0 else float('inf')
301	    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'
302	    print(f"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}")
303	
304	print("\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant")
305	print()
306	print_separator()
307	print("END OF ANALYSIS")
308	print_separator()
309	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d070063d-ce5b-49de-a319-f3828e749284",
  "uuid": "d7aef28c-0c45-4e8f-ab95-3ad2945c2155",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    \"\"\"Print mean +/- std for a group.\"\"\"\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    \"\"\"Run t-test and Mann-Whitney U test between two groups.\"\"\"\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    # Independent two-sample t-test (Welch's, unequal variance)\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n\n    # Mann-Whitney U test (non-parametric)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    # Effect size: Cohen's d\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    # Difference\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100  # percentage points\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA FROM REGISTRY (verified from all experiments with conclusion=success)\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only (norm02 variants, K=5 and K=10): seeds 42-48\n# From registry: seed42=0.35, seed43=0.32(k5) or 0.34(norm02-r2), seed44=0.37(k5-r2) or 0.36(norm02),\n# seed45=0.34(k5-r2) or 0.34(norm02), seed46=0.33(r2), seed47=0.32(norm02), seed48=0.35(norm02 and crm-spatial)\n# Using the best-matched K=10 norm02 experiments (primary config):\ncrm_spatial = [0.34, 0.36, 0.34, 0.33, 0.32, 0.35]  # seeds 43-r2, 44, 45, 46-r2, 47, 48\n# K=5 variants:\ncrm_spatial_k5 = [0.35, 0.32, 0.37, 0.34]  # seeds 42, 43, 44-r2, 45-r2\n# Combined unique seeds (using K=10 when available, K=5 for seed42):\ncrm_spatial_all = [0.35, 0.34, 0.36, 0.34, 0.33, 0.32, 0.35]  # seeds 42(k5), 43-r2, 44, 45, 46-r2, 47, 48\n# Fallback from user-provided data (n=8):\ncrm_spatial_user = [0.32, 0.34, 0.36, 0.34, 0.34, 0.33, 0.32, 0.35]\n\n# VLA-only Spatial: seeds 42-50\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30]  # seeds 42, 43, 44, 45, 46, 47, 50\n# Fallback from user-provided data (n=9):\nvla_spatial_user = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.30, 0.29]\n\n# --- LIBERO-Long ---\n# CRM obs_only Long: seeds 42-47\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # seeds 42, 43, 44, 45, 46, 47\n# User-provided (same):\ncrm_long_user = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]\n\n# VLA-only Long: seeds 42-48\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]  # seeds 42, 43, 44, 45, 46, 47, 48\n# User-provided (n=7):\nvla_long_user = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.11]\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal: seeds 42-46\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72]  # seeds 42, 43, 44-r2, 45-r2, 46\n# User-provided (same):\ncrm_goal_user = [0.67, 0.72, 0.64, 0.65, 0.72]\n\n# VLA-only Goal: seeds 42-46\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # seeds 42, 43, 44-r2, 45, 46\n# User-provided (same):\nvla_goal_user = [0.71, 0.69, 0.73, 0.63, 0.71]\n\n# --- LIBERO-Object ---\n# CRM obs_only Object (norm02, K=10): seeds from registry\n# Using norm02 K=10 results: seed43-r2=0.16, seed44-r2=0.16, seed45=0.16, seed46=0.15, seed47=0.20, seed48-r2=0.18\n# Using norm01 results: seed42=0.19, seed44=0.16, seed45-r2=0.17, seed46-r3=0.18, seed47=0.17, seed48=0.18\n# Using norm02 K=5 results: seed42=0.14, seed43=0.19, seed44=0.17, seed45=0.15, seed46=0.16, seed47=0.13, seed48=0.18\n# We'll use norm01 as the primary CRM config (best performing, consistent config):\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # seeds 42, 44, 45-r2, 46-r3, 47, 48\n# norm02 K=10:\ncrm_object_norm02 = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # seeds 43-r2, 44-r2, 45, 46, 47, 48-r2\n# norm02 K=5:\ncrm_object_norm02_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # seeds 42-48\n\n# VLA-only Object: from registry\n# seed42=0.12 (overall_sr), seed43=0.12 (overall_sr), seed44-r2=0.10, seed45=0.09(overall_sr),\n# seed45-r2=0.11, seed46=0.13, seed47=0.10, seed48=0.10, seed50=0.09\nvla_object = [0.12, 0.12, 0.10, 0.09, 0.13, 0.10, 0.10, 0.09]  # seeds 42, 43, 44-r2, 45, 46, 47, 48, 50\n# Using seed45-r2 instead of seed45 (more recent run):\nvla_object_alt = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]\n\n# --- Argmin Object ---\n# K=10: seed43=0.17, seed44-r2=0.13, seed45=0.12, seed46=0.10, seed47=0.10\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]\n# K=5: seed42=0.15, seed43=0.13, seed44-r2=0.11, seed45=0.13\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]\n\n# Argmin Spatial (only 1 data point from registry)\nargmin_spatial = [0.34]\n\n# --- Adaptive-K Object ---\n# p25: seed42=0.15, seed43=0.13\nadaptive_k_p25 = [0.15, 0.13]\n# p50: seed42=0.16, seed43=0.16, seed44=0.14\nadaptive_k_p50 = [0.16, 0.16, 0.14]\n# p75: seed42=0.12, seed43=0.13, seed44=0.16\nadaptive_k_p75 = [0.12, 0.13, 0.16]\n# p90: seed42=0.12, seed43=0.14, seed44=0.14\nadaptive_k_p90 = [0.12, 0.14, 0.14]\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL: CRM vs VLA-only\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint(\"\\n  [Registry data]\")\nprint_group_stats(\"CRM obs_only (registry, n=7)\", crm_spatial_all)\nprint_group_stats(\"VLA-only (registry, n=7)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial_all, \"VLA-only\", vla_spatial)\n\nprint(\"\\n  [User-provided data]\")\nprint_group_stats(\"CRM obs_only (user, n=8)\", crm_spatial_user)\nprint_group_stats(\"VLA-only (user, n=9)\", vla_spatial_user)\nrun_tests(\"CRM\", crm_spatial_user, \"VLA-only\", vla_spatial_user)\n\n# ============================================================================\n# 2. LIBERO-LONG: CRM vs VLA-only\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint(\"\\n  [Registry data]\")\nprint_group_stats(\"CRM obs_only (registry, n=6)\", crm_long)\nprint_group_stats(\"VLA-only (registry, n=7)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\nprint(\"\\n  [User-provided data]\")\nprint_group_stats(\"CRM obs_only (user, n=6)\", crm_long_user)\nprint_group_stats(\"VLA-only (user, n=7)\", vla_long_user)\nrun_tests(\"CRM\", crm_long_user, \"VLA-only\", vla_long_user)\n\n# ============================================================================\n# 3. LIBERO-GOAL: CRM vs VLA-only\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint(\"\\n  [Registry data = User-provided data]\")\nprint_group_stats(\"CRM obs_only (n=5)\", crm_goal)\nprint_group_stats(\"VLA-only (n=5)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT: CRM vs VLA-only\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [CRM norm01 config]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [CRM norm02 K=10 config]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object_norm02)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02\", crm_object_norm02, \"VLA-only\", vla_object)\n\nprint(\"\\n  [CRM norm02 K=5 config]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_norm02_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=5\", crm_object_norm02_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm01 (n=6)\", crm_object_norm01)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm01:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm01\", crm_object_norm01)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm01 (n=6)\", crm_object_norm01)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm01:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm01\", crm_object_norm01)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'95% CI':>15}\")\nprint_separator('-')\n\ndef print_row(bench, method, vals):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    se = std / np.sqrt(n)\n    ci_lo = mean - 1.96 * se\n    ci_hi = mean + 1.96 * se\n    print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} [{ci_lo:.4f}, {ci_hi:.4f}]\")\n\nprint_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial_all)\nprint_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial)\nprint()\nprint_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_row(\"LIBERO-Long\", \"VLA-only\", vla_long)\nprint()\nprint_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal)\nprint()\nprint_row(\"LIBERO-Object\", \"CRM norm01\", crm_object_norm01)\nprint_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object_norm02)\nprint_row(\"LIBERO-Object\", \"CRM norm02 K=5\", crm_object_norm02_k5)\nprint_row(\"LIBERO-Object\", \"VLA-only\", vla_object)\nprint_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY FINDINGS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial_all, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm01): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object(norm02): CRM vs VLA\", crm_object_norm02, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm01 vs Argmin-K10\", crm_object_norm01, argmin_object_k10),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
      "numLines": 309,
      "startLine": 1,
      "totalLines": 309
    }
  }
}
```

</details>

---


### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Bash · `toolu_01Hp9yEmrtogQQms9dKU5nTo`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts && python3 statistical_analysis.py",
  "description": "Run statistical analysis script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d070063d-ce5b-49de-a319-f3828e749284",
  "uuid": "f7d3bedf-1593-4f7d-aea5-b8496b645b71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgMJYPiTZ7fsGCMG4R6FnD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6664,
      "cache_read_input_tokens": 28442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6664
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

_source line 57 · 2026-05-20T04:19:32.411Z_

<details><summary>↩ Tool result · `toolu_01Hp9yEmrtogQQms9dKU5nTo`</summary>

```text
================================================================================
STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments
All success rates are fractions (0.0 to 1.0)
================================================================================

1. LIBERO-SPATIAL
--------------------------------------------------------------------------------

  [Registry data]
  CRM obs_only (registry, n=7): n=7, mean=0.3414, std=0.0135, min=0.3200, max=0.3600
    values: [0.35, 0.34, 0.36, 0.34, 0.33, 0.32, 0.35]
  VLA-only (registry, n=7): n=7, mean=0.2957, std=0.0127, min=0.2700, max=0.3100
    values: [0.3, 0.29, 0.31, 0.27, 0.3, 0.3, 0.3]

  CRM vs VLA-only:
    Difference: +0.0457 (+4.57 pp)
    Welch's t-test: t=6.5320, p=0.000028 ***
    Mann-Whitney U: U=49.0, p=0.001884 **
    Cohen's d: 3.4915 (large)

  [User-provided data]
  CRM obs_only (user, n=8): n=8, mean=0.3375, std=0.0139, min=0.3200, max=0.3600
    values: [0.32, 0.34, 0.36, 0.34, 0.34, 0.33, 0.32, 0.35]
  VLA-only (user, n=9): n=9, mean=0.2956, std=0.0113, min=0.2700, max=0.3100
    values: [0.3, 0.29, 0.31, 0.27, 0.3, 0.3, 0.3, 0.3, 0.29]

  CRM vs VLA-only:
    Difference: +0.0419 (+4.19 pp)
    Welch's t-test: t=6.7772, p=0.000011 ***
    Mann-Whitney U: U=72.0, p=0.000517 ***
    Cohen's d: 3.3354 (large)


2. LIBERO-LONG
--------------------------------------------------------------------------------

  [Registry data]
  CRM obs_only (registry, n=6): n=6, mean=0.1750, std=0.0164, min=0.1500, max=0.2000
    values: [0.17, 0.15, 0.2, 0.18, 0.18, 0.17]
  VLA-only (registry, n=7): n=7, mean=0.1414, std=0.0254, min=0.1100, max=0.1800
    values: [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]

  CRM vs VLA-only:
    Difference: +0.0336 (+3.36 pp)
    Welch's t-test: t=2.8628, p=0.016373 *
    Mann-Whitney U: U=36.0, p=0.035947 *
    Cohen's d: 1.5388 (large)

  [User-provided data]
  CRM obs_only (user, n=6): n=6, mean=0.1750, std=0.0164, min=0.1500, max=0.2000
    values: [0.17, 0.15, 0.2, 0.18, 0.18, 0.17]
  VLA-only (user, n=7): n=7, mean=0.1371, std=0.0281, min=0.1100, max=0.1800
    values: [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.11]

  CRM vs VLA-only:
    Difference: +0.0379 (+3.79 pp)
    Welch's t-test: t=3.0125, p=0.013267 *
    Mann-Whitney U: U=36.0, p=0.035947 *
    Cohen's d: 1.6085 (large)


3. LIBERO-GOAL
--------------------------------------------------------------------------------

  [Registry data = User-provided data]
  CRM obs_only (n=5): n=5, mean=0.6800, std=0.0381, min=0.6400, max=0.7200
    values: [0.67, 0.72, 0.64, 0.65, 0.72]
  VLA-only (n=5): n=5, mean=0.6940, std=0.0385, min=0.6300, max=0.7300
    values: [0.71, 0.69, 0.73, 0.63, 0.71]

  CRM vs VLA-only:
    Difference: -0.0140 (-1.40 pp)
    Welch's t-test: t=-0.5783, p=0.578952 n.s.
    Mann-Whitney U: U=11.0, p=0.833534 n.s.
    Cohen's d: -0.3658 (small)


4. LIBERO-OBJECT
--------------------------------------------------------------------------------

  [CRM norm01 config]
  CRM obs_only norm01 (n=6): n=6, mean=0.1750, std=0.0105, min=0.1600, max=0.1900
    values: [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]
  VLA-only (n=8): n=8, mean=0.1063, std=0.0151, min=0.0900, max=0.1300
    values: [0.12, 0.12, 0.1, 0.09, 0.13, 0.1, 0.1, 0.09]

  CRM norm01 vs VLA-only:
    Difference: +0.0688 (+6.88 pp)
    Welch's t-test: t=10.0624, p=0.000000 ***
    Mann-Whitney U: U=48.0, p=0.002207 **
    Cohen's d: 5.1512 (large)

  [CRM norm02 K=10 config]
  CRM obs_only norm02 K=10 (n=6): n=6, mean=0.1683, std=0.0183, min=0.1500, max=0.2000
    values: [0.16, 0.16, 0.16, 0.15, 0.2, 0.18]
  VLA-only (n=8): n=8, mean=0.1063, std=0.0151, min=0.0900, max=0.1300
    values: [0.12, 0.12, 0.1, 0.09, 0.13, 0.1, 0.1, 0.09]

  CRM norm02 vs VLA-only:
    Difference: +0.0621 (+6.21 pp)
    Welch's t-test: t=6.7554, p=0.000062 ***
    Mann-Whitney U: U=48.0, p=0.002157 **
    Cohen's d: 3.7604 (large)

  [CRM norm02 K=5 config]
  CRM obs_only norm02 K=5 (n=7): n=7, mean=0.1600, std=0.0216, min=0.1300, max=0.1900
    values: [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]
  VLA-only (n=8): n=8, mean=0.1063, std=0.0151, min=0.0900, max=0.1300
    values: [0.12, 0.12, 0.1, 0.09, 0.13, 0.1, 0.1, 0.09]

  CRM norm02 K=5 vs VLA-only:
    Difference: +0.0537 (+5.37 pp)
    Welch's t-test: t=5.5142, p=0.000212 ***
    Mann-Whitney U: U=55.5, p=0.001665 **
    Cohen's d: 2.9258 (large)


5. ARGMIN BASELINES (Object)
--------------------------------------------------------------------------------
  Argmin K=10 (n=5): n=5, mean=0.1240, std=0.0288, min=0.1000, max=0.1700
    values: [0.17, 0.13, 0.12, 0.1, 0.1]
  Argmin K=5 (n=4): n=4, mean=0.1300, std=0.0163, min=0.1100, max=0.1500
    values: [0.15, 0.13, 0.11, 0.13]
  VLA-only (n=8): n=8, mean=0.1063, std=0.0151, min=0.0900, max=0.1300
    values: [0.12, 0.12, 0.1, 0.09, 0.13, 0.1, 0.1, 0.09]
  CRM norm01 (n=6): n=6, mean=0.1750, std=0.0105, min=0.1600, max=0.1900
    values: [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]

  Argmin K=10 vs VLA-only:

  Argmin K=10 vs VLA-only:
    Difference: +0.0177 (+1.77 pp)
    Welch's t-test: t=1.2732, p=0.255058 n.s.
    Mann-Whitney U: U=28.5, p=0.224257 n.s.
    Cohen's d: 0.8404 (large)

  Argmin K=10 vs CRM norm01:

  Argmin K=10 vs CRM norm01:
    Difference: -0.0510 (-5.10 pp)
    Welch's t-test: t=-3.7564, p=0.013785 *
    Mann-Whitney U: U=2.0, p=0.020671 *
    Cohen's d: -2.4594 (large)


6. ADAPTIVE-K BASELINES (Object)
--------------------------------------------------------------------------------
  Adaptive-K p25 (n=2): n=2, mean=0.1400, std=0.0141, min=0.1300, max=0.1500
    values: [0.15, 0.13]
  Adaptive-K p50 (n=3): n=3, mean=0.1533, std=0.0115, min=0.1400, max=0.1600
    values: [0.16, 0.16, 0.14]
  Adaptive-K p75 (n=3): n=3, mean=0.1367, std=0.0208, min=0.1200, max=0.1600
    values: [0.12, 0.13, 0.16]
  Adaptive-K p90 (n=3): n=3, mean=0.1333, std=0.0115, min=0.1200, max=0.1400
    values: [0.12, 0.14, 0.14]
  Adaptive-K all (n=11): n=11, mean=0.1409, std=0.0151, min=0.1200, max=0.1600
    values: [0.15, 0.13, 0.16, 0.16, 0.14, 0.12, 0.13, 0.16, 0.12, 0.14, 0.14]
  VLA-only (n=8): n=8, mean=0.1063, std=0.0151, min=0.0900, max=0.1300
    values: [0.12, 0.12, 0.1, 0.09, 0.13, 0.1, 0.1, 0.09]
  CRM norm01 (n=6): n=6, mean=0.1750, std=0.0105, min=0.1600, max=0.1900
    values: [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]

  Adaptive-K (all) vs VLA-only:

  Adaptive-K all vs VLA-only:
    Difference: +0.0347 (+3.47 pp)
    Welch's t-test: t=4.9425, p=0.000168 ***
    Mann-Whitney U: U=83.0, p=0.001294 **
    Cohen's d: 2.2946 (large)

  Adaptive-K (all) vs CRM norm01:

  Adaptive-K all vs CRM norm01:
    Difference: -0.0341 (-3.41 pp)
    Welch's t-test: t=-5.4478, p=0.000089 ***
    Mann-Whitney U: U=1.5, p=0.001630 **
    Cohen's d: -2.4772 (large)


================================================================================
SUMMARY TABLE
================================================================================
Benchmark          Method                   n    Mean     Std          95% CI
--------------------------------------------------------------------------------
LIBERO-Spatial     CRM obs_only             7  0.3414  0.0135 [0.3315, 0.3514]
LIBERO-Spatial     VLA-only                 7  0.2957  0.0127 [0.2863, 0.3051]

LIBERO-Long        CRM obs_only             6  0.1750  0.0164 [0.1619, 0.1881]
LIBERO-Long        VLA-only                 7  0.1414  0.0254 [0.1226, 0.1603]

LIBERO-Goal        CRM obs_only             5  0.6800  0.0381 [0.6466, 0.7134]
LIBERO-Goal        VLA-only                 5  0.6940  0.0385 [0.6603, 0.7277]

LIBERO-Object      CRM norm01               6  0.1750  0.0105 [0.1666, 0.1834]
LIBERO-Object      CRM norm02 K=10          6  0.1683  0.0183 [0.1537, 0.1830]
LIBERO-Object      CRM norm02 K=5           7  0.1600  0.0216 [0.1440, 0.1760]
LIBERO-Object      VLA-only                 8  0.1063  0.0151 [0.0958, 0.1167]
LIBERO-Object      Argmin K=10              5  0.1240  0.0288 [0.0987, 0.1493]
LIBERO-Object      Argmin K=5               4  0.1300  0.0163 [0.1140, 0.1460]
LIBERO-Object      Adaptive-K (all)        11  0.1409  0.0151 [0.1320, 0.1499]


================================================================================
KEY SIGNIFICANCE RESULTS
================================================================================

Comparison                                  Diff   t-test p     MW-U p   Sig   Cohen d
-------------------------------------------------------------------------------------
Spatial: CRM vs VLA                      +0.0457   0.000028   0.001884   ***   +3.4915
Long: CRM vs VLA                         +0.0336   0.016373   0.035947     *   +1.5388
Goal: CRM vs VLA                         -0.0140   0.578952   0.833534  n.s.   -0.3658
Object(norm01): CRM vs VLA               +0.0688   0.000000   0.002207   ***   +5.1512
Object(norm02): CRM vs VLA               +0.0621   0.000062   0.002157   ***   +3.7604
Object: Argmin-K10 vs VLA                +0.0177   0.255058   0.224257  n.s.   +0.8404
Object: CRM-norm01 vs Argmin-K10         +0.0510   0.013785   0.020671     *   +2.4594

Significance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant

================================================================================
END OF ANALYSIS
================================================================================
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d070063d-ce5b-49de-a319-f3828e749284",
  "uuid": "9dae94c1-d9a9-4da4-a473-2fd6a8cb607c",
  "tool_use_result": {
    "stdout": "================================================================================\nSTATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\nAll success rates are fractions (0.0 to 1.0)\n================================================================================\n\n1. LIBERO-SPATIAL\n--------------------------------------------------------------------------------\n\n  [Registry data]\n  CRM obs_only (registry, n=7): n=7, mean=0.3414, std=0.0135, min=0.3200, max=0.3600\n    values: [0.35, 0.34, 0.36, 0.34, 0.33, 0.32, 0.35]\n  VLA-only (registry, n=7): n=7, mean=0.2957, std=0.0127, min=0.2700, max=0.3100\n    values: [0.3, 0.29, 0.31, 0.27, 0.3, 0.3, 0.3]\n\n  CRM vs VLA-only:\n    Difference: +0.0457 (+4.57 pp)\n    Welch's t-test: t=6.5320, p=0.000028 ***\n    Mann-Whitney U: U=49.0, p=0.001884 **\n    Cohen's d: 3.4915 (large)\n\n  [User-provided data]\n  CRM obs_only (user, n=8): n=8, mean=0.3375, std=0.0139, min=0.3200, max=0.3600\n    values: [0.32, 0.34, 0.36, 0.34, 0.34, 0.33, 0.32, 0.35]\n  VLA-only (user, n=9): n=9, mean=0.2956, std=0.0113, min=0.2700, max=0.3100\n    values: [0.3, 0.29, 0.31, 0.27, 0.3, 0.3, 0.3, 0.3, 0.29]\n\n  CRM vs VLA-only:\n    Difference: +0.0419 (+4.19 pp)\n    Welch's t-test: t=6.7772, p=0.000011 ***\n    Mann-Whitney U: U=72.0, p=0.000517 ***\n    Cohen's d: 3.3354 (large)\n\n\n2. LIBERO-LONG\n--------------------------------------------------------------------------------\n\n  [Registry data]\n  CRM obs_only (registry, n=6): n=6, mean=0.1750, std=0.0164, min=0.1500, max=0.2000\n    values: [0.17, 0.15, 0.2, 0.18, 0.18, 0.17]\n  VLA-only (registry, n=7): n=7, mean=0.1414, std=0.0254, min=0.1100, max=0.1800\n    values: [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]\n\n  CRM vs VLA-only:\n    Difference: +0.0336 (+3.36 pp)\n    Welch's t-test: t=2.8628, p=0.016373 *\n    Mann-Whitney U: U=36.0, p=0.035947 *\n    Cohen's d: 1.5388 (large)\n\n  [User-provided data]\n  CRM obs_only (user, n=6): n=6, mean=0.1750, std=0.0164, min=0.1500, max=0.2000\n    values: [0.17, 0.15, 0.2, 0.18, 0.18, 0.17]\n  VLA-only (user, n=7): n=7, mean=0.1371, std=0.0281, min=0.1100, max=0.1800\n    values: [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.11]\n\n  CRM vs VLA-only:\n    Difference: +0.0379 (+3.79 pp)\n    Welch's t-test: t=3.0125, p=0.013267 *\n    Mann-Whitney U: U=36.0, p=0.035947 *\n    Cohen's d: 1.6085 (large)\n\n\n3. LIBERO-GOAL\n--------------------------------------------------------------------------------\n\n  [Registry data = User-provided data]\n  CRM obs_only (n=5): n=5, mean=0.6800, std=0.0381, min=0.6400, max=0.7200\n    values: [0.67, 0.72, 0.64, 0.65, 0.72]\n  VLA-only (n=5): n=5, mean=0.6940, std=0.0385, min=0.6300, max=0.7300\n    values: [0.71, 0.69, 0.73, 0.63, 0.71]\n\n  CRM vs VLA-only:\n    Difference: -0.0140 (-1.40 pp)\n    Welch's t-test: t=-0.5783, p=0.578952 n.s.\n    Mann-Whitney U: U=11.0, p=0.833534 n.s.\n    Cohen's d: -0.3658 (small)\n\n\n4. LIBERO-OBJECT\n--------------------------------------------------------------------------------\n\n  [CRM norm01 config]\n  CRM obs_only norm01 (n=6): n=6, mean=0.1750, std=0.0105, min=0.1600, max=0.1900\n    values: [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]\n  VLA-only (n=8): n=8, mean=0.1063, std=0.0151, min=0.0900, max=0.1300\n    values: [0.12, 0.12, 0.1, 0.09, 0.13, 0.1, 0.1, 0.09]\n\n  CRM norm01 vs VLA-only:\n    Difference: +0.0688 (+6.88 pp)\n    Welch's t-test: t=10.0624, p=0.000000 ***\n    Mann-Whitney U: U=48.0, p=0.002207 **\n    Cohen's d: 5.1512 (large)\n\n  [CRM norm02 K=10 config]\n  CRM obs_only norm02 K=10 (n=6): n=6, mean=0.1683, std=0.0183, min=0.1500, max=0.2000\n    values: [0.16, 0.16, 0.16, 0.15, 0.2, 0.18]\n  VLA-only (n=8): n=8, mean=0.1063, std=0.0151, min=0.0900, max=0.1300\n    values: [0.12, 0.12, 0.1, 0.09, 0.13, 0.1, 0.1, 0.09]\n\n  CRM norm02 vs VLA-only:\n    Difference: +0.0621 (+6.21 pp)\n    Welch's t-test: t=6.7554, p=0.000062 ***\n    Mann-Whitney U: U=48.0, p=0.002157 **\n    Cohen's d: 3.7604 (large)\n\n  [CRM norm02 K=5 config]\n  CRM obs_only norm02 K=5 (n=7): n=7, mean=0.1600, std=0.0216, min=0.1300, max=0.1900\n    values: [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]\n  VLA-only (n=8): n=8, mean=0.1063, std=0.0151, min=0.0900, max=0.1300\n    values: [0.12, 0.12, 0.1, 0.09, 0.13, 0.1, 0.1, 0.09]\n\n  CRM norm02 K=5 vs VLA-only:\n    Difference: +0.0537 (+5.37 pp)\n    Welch's t-test: t=5.5142, p=0.000212 ***\n    Mann-Whitney U: U=55.5, p=0.001665 **\n    Cohen's d: 2.9258 (large)\n\n\n5. ARGMIN BASELINES (Object)\n--------------------------------------------------------------------------------\n  Argmin K=10 (n=5): n=5, mean=0.1240, std=0.0288, min=0.1000, max=0.1700\n    values: [0.17, 0.13, 0.12, 0.1, 0.1]\n  Argmin K=5 (n=4): n=4, mean=0.1300, std=0.0163, min=0.1100, max=0.1500\n    values: [0.15, 0.13, 0.11, 0.13]\n  VLA-only (n=8): n=8, mean=0.1063, std=0.0151, min=0.0900, max=0.1300\n    values: [0.12, 0.12, 0.1, 0.09, 0.13, 0.1, 0.1, 0.09]\n  CRM norm01 (n=6): n=6, mean=0.1750, std=0.0105, min=0.1600, max=0.1900\n    values: [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]\n\n  Argmin K=10 vs VLA-only:\n\n  Argmin K=10 vs VLA-only:\n    Difference: +0.0177 (+1.77 pp)\n    Welch's t-test: t=1.2732, p=0.255058 n.s.\n    Mann-Whitney U: U=28.5, p=0.224257 n.s.\n    Cohen's d: 0.8404 (large)\n\n  Argmin K=10 vs CRM norm01:\n\n  Argmin K=10 vs CRM norm01:\n    Difference: -0.0510 (-5.10 pp)\n    Welch's t-test: t=-3.7564, p=0.013785 *\n    Mann-Whitney U: U=2.0, p=0.020671 *\n    Cohen's d: -2.4594 (large)\n\n\n6. ADAPTIVE-K BASELINES (Object)\n--------------------------------------------------------------------------------\n  Adaptive-K p25 (n=2): n=2, mean=0.1400, std=0.0141, min=0.1300, max=0.1500\n    values: [0.15, 0.13]\n  Adaptive-K p50 (n=3): n=3, mean=0.1533, std=0.0115, min=0.1400, max=0.1600\n    values: [0.16, 0.16, 0.14]\n  Adaptive-K p75 (n=3): n=3, mean=0.1367, std=0.0208, min=0.1200, max=0.1600\n    values: [0.12, 0.13, 0.16]\n  Adaptive-K p90 (n=3): n=3, mean=0.1333, std=0.0115, min=0.1200, max=0.1400\n    values: [0.12, 0.14, 0.14]\n  Adaptive-K all (n=11): n=11, mean=0.1409, std=0.0151, min=0.1200, max=0.1600\n    values: [0.15, 0.13, 0.16, 0.16, 0.14, 0.12, 0.13, 0.16, 0.12, 0.14, 0.14]\n  VLA-only (n=8): n=8, mean=0.1063, std=0.0151, min=0.0900, max=0.1300\n    values: [0.12, 0.12, 0.1, 0.09, 0.13, 0.1, 0.1, 0.09]\n  CRM norm01 (n=6): n=6, mean=0.1750, std=0.0105, min=0.1600, max=0.1900\n    values: [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]\n\n  Adaptive-K (all) vs VLA-only:\n\n  Adaptive-K all vs VLA-only:\n    Difference: +0.0347 (+3.47 pp)\n    Welch's t-test: t=4.9425, p=0.000168 ***\n    Mann-Whitney U: U=83.0, p=0.001294 **\n    Cohen's d: 2.2946 (large)\n\n  Adaptive-K (all) vs CRM norm01:\n\n  Adaptive-K all vs CRM norm01:\n    Difference: -0.0341 (-3.41 pp)\n    Welch's t-test: t=-5.4478, p=0.000089 ***\n    Mann-Whitney U: U=1.5, p=0.001630 **\n    Cohen's d: -2.4772 (large)\n\n\n================================================================================\nSUMMARY TABLE\n================================================================================\nBenchmark          Method                   n    Mean     Std          95% CI\n--------------------------------------------------------------------------------\nLIBERO-Spatial     CRM obs_only             7  0.3414  0.0135 [0.3315, 0.3514]\nLIBERO-Spatial     VLA-only                 7  0.2957  0.0127 [0.2863, 0.3051]\n\nLIBERO-Long        CRM obs_only             6  0.1750  0.0164 [0.1619, 0.1881]\nLIBERO-Long        VLA-only                 7  0.1414  0.0254 [0.1226, 0.1603]\n\nLIBERO-Goal        CRM obs_only             5  0.6800  0.0381 [0.6466, 0.7134]\nLIBERO-Goal        VLA-only                 5  0.6940  0.0385 [0.6603, 0.7277]\n\nLIBERO-Object      CRM norm01               6  0.1750  0.0105 [0.1666, 0.1834]\nLIBERO-Object      CRM norm02 K=10          6  0.1683  0.0183 [0.1537, 0.1830]\nLIBERO-Object      CRM norm02 K=5           7  0.1600  0.0216 [0.1440, 0.1760]\nLIBERO-Object      VLA-only                 8  0.1063  0.0151 [0.0958, 0.1167]\nLIBERO-Object      Argmin K=10              5  0.1240  0.0288 [0.0987, 0.1493]\nLIBERO-Object      Argmin K=5               4  0.1300  0.0163 [0.1140, 0.1460]\nLIBERO-Object      Adaptive-K (all)        11  0.1409  0.0151 [0.1320, 0.1499]\n\n\n================================================================================\nKEY SIGNIFICANCE RESULTS\n================================================================================\n\nComparison                                  Diff   t-test p     MW-U p   Sig   Cohen d\n-------------------------------------------------------------------------------------\nSpatial: CRM vs VLA                      +0.0457   0.000028   0.001884   ***   +3.4915\nLong: CRM vs VLA                         +0.0336   0.016373   0.035947     *   +1.5388\nGoal: CRM vs VLA                         -0.0140   0.578952   0.833534  n.s.   -0.3658\nObject(norm01): CRM vs VLA               +0.0688   0.000000   0.002207   ***   +5.1512\nObject(norm02): CRM vs VLA               +0.0621   0.000062   0.002157   ***   +3.7604\nObject: Argmin-K10 vs VLA                +0.0177   0.255058   0.224257  n.s.   +0.8404\nObject: CRM-norm01 vs Argmin-K10         +0.0510   0.013785   0.020671     *   +2.4594\n\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\n\n================================================================================\nEND OF ANALYSIS\n================================================================================",
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

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the statistics. Let me compose the memory.md update with the "全 benchmark 统计摘要" section. I need to read the current memory.md content and append/update it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d070063d-ce5b-49de-a319-f3828e749284",
  "uuid": "9fe2529d-3730-44fa-a5df-dbb527129312",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017VEcvYMsLFt4V9rhxnXSED",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4503,
      "cache_read_input_tokens": 35106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4503
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

_source line 59_

统计计算完成。现在更新 memory.md，追加全 benchmark 统计摘要段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d070063d-ce5b-49de-a319-f3828e749284",
  "uuid": "9dea7144-d391-4f3d-8a9d-113d6793b845",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017VEcvYMsLFt4V9rhxnXSED",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4503,
      "cache_read_input_tokens": 35106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4503
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

_source line 60_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01PWYXksQogZ9Gc2cC7KrTFc`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "memory.md",
  "content": "# Project Memory\n\n## 失败模式记录\n\n- [失败模式] Cron false positive：eval 脚本不写 W&B 也不写 sentinel file，进程正常退出后 cron 5 次检测找不到标记 → 自动标记为 failed。受影响：eval-vla-only-long-seed46, eval-vla-only-goal-seed46。修复方案：tail 日志确认实际完成 → 手动修正 conclusion=success + 补录 metrics。预防：eval 实验应检查 output JSON 是否存在作为 sentinel。\n\n- [失败模式] FMVD 信号无效：ODE velocity dispersion 与 K=10 action variance 几乎无相关性 (ρ=0.0825, 远低于 0.3 阈值)。根因：flow matching 的确定性 ODE 轨迹的 velocity norm 变异编码的是 denoising dynamics，而非 action-level uncertainty。per-task 方向不一致 (milk ρ=-0.284)。FMVD 分布极窄 (std=0.040)，无法区分 uncertain vs confident steps。**教训：zero-cost signal 不能假设有效——denoising 空间的统计量不一定映射到 action 空间的 uncertainty。K=2 L2 divergence (直接在 action 空间测量) 是更直觉的替代方案。**\n\n- [失败模式] OpenVLA-7B eval timeout：OpenVLA-7B 每 episode ~77s（SmolVLA ~30s），500 episodes 需 ~10.7h。默认 timeout_hours=6 不够 → EXIT_CODE=124。修复方案：OpenVLA eval 实验 timeout_hours 至少设 12h。\n\n## CRM Coverage 限制\n\nCRM v3 训练数据 = Object(10) + Spatial(10) = 20 tasks。LIBERO-Goal 和 LIBERO-10 (Long) 的 tasks 不在训练覆盖范围内。CRM-Goal 和 CRM-Long 实验是 OOD 泛化测试——Director 已知并批准。\n\n## Adaptive K 信号探索\n\n| 信号 | ρ vs K10_var | 结论 | 备注 |\n|------|-------------|------|------|\n| FMVD (velocity dispersion) | 0.0825 | ❌ NO-GO | zero-cost 但无效 |\n| K=2 L2 divergence | TBD (~1-2h) | ⏳ | 需要 K=2 采样，非 zero-cost |\n\n## 全 Benchmark 统计摘要 (2026-05-20)\n\n### 1. LIBERO-Object — **Strong improvement**\n\n| Method | n | Mean±Std | 95% CI | vs VLA Δ | p (Welch) | Cohen's d |\n|--------|---|----------|--------|----------|-----------|-----------|\n| CRM norm01 (ε=0.2, K=10) | 6 | 17.5%±1.0% | [16.7%, 18.3%] | **+6.9 pp** | <0.001 *** | 5.15 |\n| CRM norm02 K=10 | 6 | 16.8%±1.8% | [15.4%, 18.3%] | +6.2 pp | <0.001 *** | 3.76 |\n| CRM norm02 K=5 | 7 | 16.0%±2.2% | [14.4%, 17.6%] | +5.4 pp | <0.001 *** | 2.93 |\n| Adaptive-K (all percentiles) | 11 | 14.1%±1.5% | [13.2%, 15.0%] | +3.5 pp | <0.001 *** | 2.29 |\n| Argmin K=10 | 5 | 12.4%±2.9% | [9.9%, 14.9%] | +1.8 pp | 0.255 n.s. | 0.84 |\n| Argmin K=5 | 4 | 13.0%±1.6% | [11.4%, 14.6%] | +2.4 pp | — | — |\n| **VLA-only** | **8** | **10.6%±1.5%** | **[9.6%, 11.7%]** | — | — | — |\n\nCRM norm01 > CRM norm02 > Adaptive-K > Argmin ≈ VLA-only。CRM 相对提升 65%，Argmin 无显著提升。\n\n### 2. LIBERO-Spatial — **Moderate improvement**\n\n| Method | n | Mean±Std | 95% CI | vs VLA Δ | p (Welch) | Cohen's d |\n|--------|---|----------|--------|----------|-----------|-----------|\n| CRM obs_only (K=10) | 8 | 33.8%±1.4% | [32.8%, 34.7%] | **+4.2 pp** | <0.001 *** | 3.34 |\n| **VLA-only** | **9** | **29.6%±1.1%** | **[28.8%, 30.3%]** | — | — | — |\n\nCRM 相对提升 14%。3 个 task ≥80%，4 个 task 0%——强二分性，CRM 对 next_to/between 有效，对 on_stove/on_cabinet 无效。\n\n### 3. LIBERO-Goal (OOD) — **Neutral**\n\n| Method | n | Mean±Std | 95% CI | vs VLA Δ | p (Welch) | Cohen's d |\n|--------|---|----------|--------|----------|-----------|-----------|\n| CRM obs_only | 5 | 68.0%±3.8% | [64.7%, 71.3%] | -1.4 pp | 0.579 n.s. | -0.37 |\n| **VLA-only** | **5** | **69.4%±3.8%** | **[66.0%, 72.8%]** | — | — | — |\n\nCRM 在 Goal 上无改善（OOD，tasks 不在 CRM 训练集）。无害但也无益。\n\n### 4. LIBERO-Long (OOD) — **Moderate improvement**\n\n| Method | n | Mean±Std | 95% CI | vs VLA Δ | p (Welch) | Cohen's d |\n|--------|---|----------|--------|----------|-----------|-----------|\n| CRM obs_only | 6 | 17.5%±1.6% | [16.2%, 18.8%] | **+3.4 pp** | 0.016 * | 1.54 |\n| **VLA-only** | **7** | **14.1%±2.5%** | **[12.3%, 16.0%]** | — | — | — |\n\nCRM 相对提升 24%。尽管 Long tasks 不在 CRM 训练集，仍有显著 OOD 泛化增益。\n\n### 效果总结\n\n| Benchmark | 效果 | Δ (pp) | p-value | 解读 |\n|-----------|------|--------|---------|------|\n| **Object** | Strong | +6.9 | <0.001 | 训练域内，CRM 优势最大 |\n| **Spatial** | Moderate | +4.2 | <0.001 | 训练域内，统计高度显著 |\n| **Long** | Moderate | +3.4 | 0.016 | OOD 泛化，显著但 p 较大 |\n| **Goal** | Neutral | -1.4 | 0.579 | OOD 泛化，无效果 |\n\n**排序：CRM norm01 > CRM norm02 K=10 > CRM norm02 K=5 > Adaptive-K > Argmin ≈ VLA-only**\n\nKey insight: CRM 在 in-distribution benchmarks (Object, Spatial) 上一致且显著有效；在 OOD benchmarks 中，Long 受益但 Goal 不受益——可能因为 Long 的 task 结构与训练数据更相似（sequential manipulation），而 Goal 涉及不同的语义推理。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d070063d-ce5b-49de-a319-f3828e749284",
  "uuid": "91470150-e7f5-4314-8478-d2abf6f146bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017VEcvYMsLFt4V9rhxnXSED",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4503,
      "cache_read_input_tokens": 35106,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4503
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

_source line 61 · 2026-05-20T04:20:25.454Z_

<details><summary>↩ Tool result · `toolu_01PWYXksQogZ9Gc2cC7KrTFc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d070063d-ce5b-49de-a319-f3828e749284",
  "uuid": "9be27ec6-571a-4879-9c06-dac880a854f6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 62_

统计分析已写入 memory.md「全 Benchmark 统计摘要」段。核心结论：

| Benchmark | Δ (pp) | p-value | 判定 |
|-----------|--------|---------|------|
| **Object** | +6.9 | <0.001 | Strong |
| **Spatial** | +4.2 | <0.001 | Moderate |
| **Long (OOD)** | +3.4 | 0.016 | Moderate |
| **Goal (OOD)** | -1.4 | 0.579 | Neutral |

方法排序：CRM norm01 > norm02 K=10 > norm02 K=5 > Adaptive-K > Argmin ≈ VLA-only。分析脚本保存在 `artifacts/statistical_analysis.py`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d070063d-ce5b-49de-a319-f3828e749284",
  "uuid": "f0b4eeb7-1b74-427b-b7d1-2d047f8d1446",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FxhVnq6VKeNnHjX5S18XRr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2650,
      "cache_read_input_tokens": 39609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2650
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

_source line 63_

统计分析已写入 memory.md「全 Benchmark 统计摘要」段。核心结论：

| Benchmark | Δ (pp) | p-value | 判定 |
|-----------|--------|---------|------|
| **Object** | +6.9 | <0.001 | Strong |
| **Spatial** | +4.2 | <0.001 | Moderate |
| **Long (OOD)** | +3.4 | 0.016 | Moderate |
| **Goal (OOD)** | -1.4 | 0.579 | Neutral |

方法排序：CRM norm01 > norm02 K=10 > norm02 K=5 > Adaptive-K > Argmin ≈ VLA-only。分析脚本保存在 `artifacts/statistical_analysis.py`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 314714,
  "duration_api_ms": 312765,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "d070063d-ce5b-49de-a319-f3828e749284",
  "total_cost_usd": 1.21589,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 30418,
    "cache_read_input_tokens": 190309,
    "output_tokens": 4290,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 30418,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 222,
        "cache_read_input_tokens": 39609,
        "cache_creation_input_tokens": 2650,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2650
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1490,
      "outputTokens": 13,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001555,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 24,
      "outputTokens": 16578,
      "cacheReadInputTokens": 517630,
      "cacheCreationInputTokens": 86552,
      "webSearchRequests": 0,
      "costUSD": 1.214335,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5407c65c-bdfa-4977-a718-1e99fe4c1a8d"
}
```

</details>

---
