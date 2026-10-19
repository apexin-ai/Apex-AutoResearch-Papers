# analysis update statistics with new data

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_analysis_update-statistics-with-new-data_20260520T060316.log`
- **Structured JSON:** [`715af0ea6ecd82ef0764.json`](../../sessions/71/715af0ea6ecd82ef0764.json)

## Before a recorded user message

44 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
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
  "uuid": "d2c9b796-7256-4157-a767-621e1fd39ecf",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779271800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "3d6abfdc-8884-439f-9da7-7ea387026afe",
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49"
}
```

---

### Assistant

_source line 4_

Let me read the existing script first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "7a714304-b4a7-414d-b757-4bb4483c8a38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3AysDcyaRRRAWvCzF57S8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11847,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11847
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

<details open><summary>🔧 Tool call — Read · `toolu_01Vv8cbgrTkr1Aav41KoV1ka`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "337610bc-5f44-4b15-9945-4e497a67812e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3AysDcyaRRRAWvCzF57S8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11847,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11847
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

_source line 6 · 2026-05-20T06:03:27.187Z_

<details><summary>↩ Tool result · `toolu_01Vv8cbgrTkr1Aav41KoV1ka`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Statistical analysis of ACR-VLA Conformal Refinement experiments.
4	Compares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.
5	Also includes Argmin and Adaptive-K baselines.
6	
7	Primary CRM config for Object: norm02 (ε=0.2), K=10.
8	"""
9	
10	import numpy as np
11	from scipy import stats
12	
13	def print_separator(char='=', width=80):
14	    print(char * width)
15	
16	def print_group_stats(name, values):
17	    arr = np.array(values)
18	    print(f"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, "
19	          f"min={arr.min():.4f}, max={arr.max():.4f}")
20	    print(f"    values: {[round(v, 4) for v in values]}")
21	
22	def run_tests(name_a, vals_a, name_b, vals_b):
23	    a = np.array(vals_a)
24	    b = np.array(vals_b)
25	
26	    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)
27	    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')
28	
29	    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /
30	                         (len(a) + len(b) - 2))
31	    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')
32	
33	    diff = a.mean() - b.mean()
34	    diff_pct = diff * 100
35	
36	    print(f"\n  {name_a} vs {name_b}:")
37	    print(f"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)")
38	    print(f"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}")
39	    print(f"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}")
40	    print(f"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})")
41	
42	    return t_pval, u_pval
43	
44	# ============================================================================
45	# DATA (from registry, conclusion=success, 2026-05-20)
46	# Each seed appears once; r2/r3 supersedes earlier runs.
47	# ============================================================================
48	
49	# --- LIBERO-Spatial ---
50	# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback
51	crm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35]  # s42(k5), s43-r2, s44, s45, s47, s48
52	
53	# VLA-only Spatial (seeds 42-50)
54	vla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50
55	
56	# --- LIBERO-Long ---
57	# CRM obs_only Long (seeds 42-47)
58	crm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # s42, s43, s44, s45, s46, s47
59	
60	# VLA-only Long (seeds 42-48)
61	vla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]  # s42, s43, s44, s45, s46, s47, s48
62	
63	# --- LIBERO-Goal ---
64	# CRM obs_only Goal (seeds 42-47)
65	crm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47
66	
67	# VLA-only Goal (seeds 42-46)
68	vla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # s42, s43, s44-r2, s45, s46
69	
70	# --- LIBERO-Object ---
71	# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)
72	crm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2
73	
74	# Supplementary: CRM obs_only norm01 (seeds 42-48)
75	crm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48
76	
77	# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)
78	crm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48
79	
80	# VLA-only Object (seeds 42-50, using r2 for seed45)
81	vla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50
82	
83	# --- Argmin Object ---
84	# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)
85	argmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47
86	argmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45
87	
88	# --- Adaptive-K Object ---
89	adaptive_k_p25 = [0.15, 0.13]  # s42, s43
90	adaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44
91	adaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44
92	adaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44
93	
94	
95	# ============================================================================
96	# ANALYSIS
97	# ============================================================================
98	
99	print_separator()
100	print("STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments")
101	print("All success rates are fractions (0.0 to 1.0)")
102	print("Object benchmark primary CRM config: norm02 (ε=0.2), K=10")
103	print_separator()
104	
105	# ============================================================================
106	# 1. LIBERO-SPATIAL
107	# ============================================================================
108	print("\n1. LIBERO-SPATIAL")
109	print_separator('-')
110	print_group_stats("CRM obs_only (n=6)", crm_spatial)
111	print_group_stats("VLA-only (n=9)", vla_spatial)
112	run_tests("CRM", crm_spatial, "VLA-only", vla_spatial)
113	
114	# ============================================================================
115	# 2. LIBERO-LONG
116	# ============================================================================
117	print("\n\n2. LIBERO-LONG")
118	print_separator('-')
119	print_group_stats("CRM obs_only (n=6)", crm_long)
120	print_group_stats("VLA-only (n=7)", vla_long)
121	run_tests("CRM", crm_long, "VLA-only", vla_long)
122	
123	# ============================================================================
124	# 3. LIBERO-GOAL
125	# ============================================================================
126	print("\n\n3. LIBERO-GOAL")
127	print_separator('-')
128	print_group_stats("CRM obs_only (n=6)", crm_goal)
129	print_group_stats("VLA-only (n=5)", vla_goal)
130	run_tests("CRM", crm_goal, "VLA-only", vla_goal)
131	
132	# ============================================================================
133	# 4. LIBERO-OBJECT (primary: norm02 K=10)
134	# ============================================================================
135	print("\n\n4. LIBERO-OBJECT")
136	print_separator('-')
137	
138	print("\n  [PRIMARY: CRM norm02 K=10]")
139	print_group_stats("CRM obs_only norm02 K=10 (n=6)", crm_object)
140	print_group_stats("VLA-only (n=8)", vla_object)
141	run_tests("CRM norm02 K=10", crm_object, "VLA-only", vla_object)
142	
143	print("\n  [Supplementary: CRM norm01]")
144	print_group_stats("CRM obs_only norm01 (n=6)", crm_object_norm01)
145	run_tests("CRM norm01", crm_object_norm01, "VLA-only", vla_object)
146	
147	print("\n  [Supplementary: CRM norm02 K=5]")
148	print_group_stats("CRM obs_only norm02 K=5 (n=7)", crm_object_k5)
149	run_tests("CRM norm02 K=5", crm_object_k5, "VLA-only", vla_object)
150	
151	# ============================================================================
152	# 5. ARGMIN BASELINES (Object)
153	# ============================================================================
154	print("\n\n5. ARGMIN BASELINES (Object)")
155	print_separator('-')
156	print_group_stats("Argmin K=10 (n=5)", argmin_object_k10)
157	print_group_stats("Argmin K=5 (n=4)", argmin_object_k5)
158	print_group_stats("VLA-only (n=8)", vla_object)
159	print_group_stats("CRM norm02 K=10 (n=6)", crm_object)
160	
161	print("\n  Argmin K=10 vs VLA-only:")
162	run_tests("Argmin K=10", argmin_object_k10, "VLA-only", vla_object)
163	print("\n  Argmin K=10 vs CRM norm02 K=10:")
164	run_tests("Argmin K=10", argmin_object_k10, "CRM norm02", crm_object)
165	
166	# ============================================================================
167	# 6. ADAPTIVE-K BASELINES (Object)
168	# ============================================================================
169	print("\n\n6. ADAPTIVE-K BASELINES (Object)")
170	print_separator('-')
171	print_group_stats("Adaptive-K p25 (n=2)", adaptive_k_p25)
172	print_group_stats("Adaptive-K p50 (n=3)", adaptive_k_p50)
173	print_group_stats("Adaptive-K p75 (n=3)", adaptive_k_p75)
174	print_group_stats("Adaptive-K p90 (n=3)", adaptive_k_p90)
175	all_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90
176	print_group_stats("Adaptive-K all (n=11)", all_adaptive)
177	print_group_stats("VLA-only (n=8)", vla_object)
178	print_group_stats("CRM norm02 K=10 (n=6)", crm_object)
179	
180	print("\n  Adaptive-K (all) vs VLA-only:")
181	run_tests("Adaptive-K all", all_adaptive, "VLA-only", vla_object)
182	print("\n  Adaptive-K (all) vs CRM norm02 K=10:")
183	run_tests("Adaptive-K all", all_adaptive, "CRM norm02", crm_object)
184	
185	# ============================================================================
186	# 7. SUMMARY TABLE
187	# ============================================================================
188	print("\n")
189	print_separator()
190	print("SUMMARY TABLE")
191	print_separator()
192	print(f"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}")
193	print_separator('-')
194	
195	def get_vla_baseline(bench):
196	    if bench == "LIBERO-Spatial": return vla_spatial
197	    if bench == "LIBERO-Long": return vla_long
198	    if bench == "LIBERO-Goal": return vla_goal
199	    if bench == "LIBERO-Object": return vla_object
200	    return None
201	
202	def print_summary_row(bench, method, vals, is_vla=False):
203	    arr = np.array(vals)
204	    n = len(arr)
205	    mean = arr.mean()
206	    std = arr.std(ddof=1)
207	    baseline = get_vla_baseline(bench)
208	    if is_vla or baseline is None:
209	        print(f"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}")
210	    else:
211	        bl_arr = np.array(baseline)
212	        diff = mean - bl_arr.mean()
213	        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)
214	        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'
215	        print(f"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}")
216	
217	print_summary_row("LIBERO-Spatial", "CRM obs_only", crm_spatial)
218	print_summary_row("LIBERO-Spatial", "VLA-only", vla_spatial, is_vla=True)
219	print()
220	print_summary_row("LIBERO-Long", "CRM obs_only", crm_long)
221	print_summary_row("LIBERO-Long", "VLA-only", vla_long, is_vla=True)
222	print()
223	print_summary_row("LIBERO-Goal", "CRM obs_only", crm_goal)
224	print_summary_row("LIBERO-Goal", "VLA-only", vla_goal, is_vla=True)
225	print()
226	print_summary_row("LIBERO-Object", "CRM norm02 K=10", crm_object)
227	print_summary_row("LIBERO-Object", "CRM norm01 (supp)", crm_object_norm01)
228	print_summary_row("LIBERO-Object", "CRM norm02 K=5 (supp)", crm_object_k5)
229	print_summary_row("LIBERO-Object", "VLA-only", vla_object, is_vla=True)
230	print_summary_row("LIBERO-Object", "Argmin K=10", argmin_object_k10)
231	print_summary_row("LIBERO-Object", "Argmin K=5", argmin_object_k5)
232	print_summary_row("LIBERO-Object", "Adaptive-K (all)", all_adaptive)
233	
234	# ============================================================================
235	# 8. KEY SIGNIFICANCE RESULTS
236	# ============================================================================
237	print("\n")
238	print_separator()
239	print("KEY SIGNIFICANCE RESULTS")
240	print_separator()
241	
242	tests = [
243	    ("Spatial: CRM vs VLA", crm_spatial, vla_spatial),
244	    ("Long: CRM vs VLA", crm_long, vla_long),
245	    ("Goal: CRM vs VLA", crm_goal, vla_goal),
246	    ("Object(norm02): CRM vs VLA", crm_object, vla_object),
247	    ("Object(norm01-supp): CRM vs VLA", crm_object_norm01, vla_object),
248	    ("Object: Argmin-K10 vs VLA", argmin_object_k10, vla_object),
249	    ("Object: CRM-norm02 vs Argmin-K10", crm_object, argmin_object_k10),
250	    ("Object: Adaptive-K vs VLA", all_adaptive, vla_object),
251	    ("Object: CRM-norm02 vs Adaptive-K", crm_object, all_adaptive),
252	]
253	
254	print(f"\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}")
255	print('-' * 85)
256	for name, a, b in tests:
257	    arr_a, arr_b = np.array(a), np.array(b)
258	    diff = arr_a.mean() - arr_b.mean()
259	    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)
260	    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')
261	    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /
262	                         (len(a) + len(b) - 2))
263	    d = diff / pooled_std if pooled_std > 0 else float('inf')
264	    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'
265	    print(f"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}")
266	
267	# ============================================================================
268	# 9. VERIFICATION NOTES
269	# ============================================================================
270	print("\n")
271	print_separator()
272	print("VERIFICATION NOTES")
273	print_separator()
274	print("- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).")
275	print("  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).")
276	print("  Registry value retained but unverified.")
277	print("- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).")
278	print("- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).")
279	print("- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.")
280	
281	print("\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant")
282	print()
283	print_separator()
284	print("END OF ANALYSIS")
285	print_separator()
286	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "a87e4a0c-c1f2-43ff-be91-37e65b816eb1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35]  # s42(k5), s43-r2, s44, s45, s47, s48\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # s42, s43, s44, s45, s46, s47\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]  # s42, s43, s44, s45, s46, s47, s48\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # s42, s43, s44-r2, s45, s46\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13]  # s42, s43\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_long)\nprint_group_stats(\"VLA-only (n=7)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=5)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
      "numLines": 286,
      "startLine": 1,
      "totalLines": 286
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I need to update the data arrays with the new values. Let me make the edits:

1. `vla_long`: add [0.16, 0.16, 0.15, 0.17] → line 61
2. `crm_spatial`: add [0.36] → line 51
3. `vla_goal`: add [0.65] → line 68
4. `crm_long`: add [0.14] → line 58
5. `adaptive_k_p25`: add [0.15] → line 89

I also need to update the n= counts in the print_group_stats calls and the comments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "3b49cef1-3a4e-41b0-8b01-ba4faeb1deb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K7ak9yfFr541MrgnyUzT2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5863,
      "cache_read_input_tokens": 23688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5863
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

_source line 8_

Now I'll make the five data array edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "60b44552-ed52-4e9e-816d-0758fee1c5e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K7ak9yfFr541MrgnyUzT2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5863,
      "cache_read_input_tokens": 23688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5863
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

_source line 9_

<details open><summary>🔧 Tool call — Edit · `toolu_01WvfMoKryLgnE1TCpjL5THc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "old_string": "vla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]  # s42, s43, s44, s45, s46, s47, s48",
  "new_string": "vla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "ad4f78a7-697e-4b2f-861b-93bcea4b1487",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K7ak9yfFr541MrgnyUzT2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5863,
      "cache_read_input_tokens": 23688,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5863
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

_source line 10 · 2026-05-20T06:03:37.415Z_

<details><summary>↩ Tool result · `toolu_01WvfMoKryLgnE1TCpjL5THc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "3b879943-f726-4a60-a4b3-084cd62c5eee",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
    "oldString": "vla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]  # s42, s43, s44, s45, s46, s47, s48",
    "newString": "vla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35]  # s42(k5), s43-r2, s44, s45, s47, s48\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # s42, s43, s44, s45, s46, s47\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]  # s42, s43, s44, s45, s46, s47, s48\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # s42, s43, s44-r2, s45, s46\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13]  # s42, s43\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_long)\nprint_group_stats(\"VLA-only (n=7)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=5)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
    "structuredPatch": [
      {
        "oldStart": 58,
        "oldLines": 7,
        "newStart": 58,
        "newLines": 7,
        "lines": [
          " crm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # s42, s43, s44, s45, s46, s47",
          " ",
          " # VLA-only Long (seeds 42-48)",
          "-vla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]  # s42, s43, s44, s45, s46, s47, s48",
          "+vla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52",
          " ",
          " # --- LIBERO-Goal ---",
          " # CRM obs_only Goal (seeds 42-47)"
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

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_01Gp4h3bUxuRb8qGhRa5kzjw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "old_string": "crm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35]  # s42(k5), s43-r2, s44, s45, s47, s48",
  "new_string": "crm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]  # s42(k5), s43-r2, s44, s45, s47, s48, s51"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "3401eaf9-c33c-418d-9fca-e881ae787ff8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QgCM7fPeCn7SfsoU6SMJtD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 544,
      "cache_read_input_tokens": 29551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 544
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

_source line 12 · 2026-05-20T06:03:42.247Z_

<details><summary>↩ Tool result · `toolu_01Gp4h3bUxuRb8qGhRa5kzjw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "79ea782b-6b1e-4095-abaa-a4504fd80376",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
    "oldString": "crm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35]  # s42(k5), s43-r2, s44, s45, s47, s48",
    "newString": "crm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]  # s42(k5), s43-r2, s44, s45, s47, s48, s51",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35]  # s42(k5), s43-r2, s44, s45, s47, s48\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # s42, s43, s44, s45, s46, s47\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # s42, s43, s44-r2, s45, s46\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13]  # s42, s43\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_long)\nprint_group_stats(\"VLA-only (n=7)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=5)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
    "structuredPatch": [
      {
        "oldStart": 48,
        "oldLines": 7,
        "newStart": 48,
        "newLines": 7,
        "lines": [
          " ",
          " # --- LIBERO-Spatial ---",
          " # CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback",
          "-crm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35]  # s42(k5), s43-r2, s44, s45, s47, s48",
          "+crm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]  # s42(k5), s43-r2, s44, s45, s47, s48, s51",
          " ",
          " # VLA-only Spatial (seeds 42-50)",
          " vla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50"
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

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_01UiSekcokwN5gCrwQEDMPPG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "old_string": "vla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # s42, s43, s44-r2, s45, s46",
  "new_string": "vla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "67a691e7-7b81-4943-a249-5df1e9af4e52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019fL9SV5ouaodvZkzxa3qnZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 335,
      "cache_read_input_tokens": 30095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 335
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

_source line 14 · 2026-05-20T06:03:46.397Z_

<details><summary>↩ Tool result · `toolu_01UiSekcokwN5gCrwQEDMPPG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "a147ac86-a4c5-4689-a36b-0822e6dfdb41",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
    "oldString": "vla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # s42, s43, s44-r2, s45, s46",
    "newString": "vla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]  # s42(k5), s43-r2, s44, s45, s47, s48, s51\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # s42, s43, s44, s45, s46, s47\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # s42, s43, s44-r2, s45, s46\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13]  # s42, s43\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_long)\nprint_group_stats(\"VLA-only (n=7)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=5)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
    "structuredPatch": [
      {
        "oldStart": 65,
        "oldLines": 7,
        "newStart": 65,
        "newLines": 7,
        "lines": [
          " crm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47",
          " ",
          " # VLA-only Goal (seeds 42-46)",
          "-vla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # s42, s43, s44-r2, s45, s46",
          "+vla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49",
          " ",
          " # --- LIBERO-Object ---",
          " # PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)"
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

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_013hp7JB2taCbctNM3o9DjLe`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "old_string": "crm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # s42, s43, s44, s45, s46, s47",
  "new_string": "crm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "47c3ad1c-3420-4b83-9b77-4a5633640a51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DZENv7GHnvckTjwRpZUXx4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 313,
      "cache_read_input_tokens": 30430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 313
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

_source line 16 · 2026-05-20T06:03:51.530Z_

<details><summary>↩ Tool result · `toolu_013hp7JB2taCbctNM3o9DjLe`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "96aefca6-d2f5-48dc-8c59-0c93d5db60b5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
    "oldString": "crm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # s42, s43, s44, s45, s46, s47",
    "newString": "crm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]  # s42(k5), s43-r2, s44, s45, s47, s48, s51\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # s42, s43, s44, s45, s46, s47\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13]  # s42, s43\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_long)\nprint_group_stats(\"VLA-only (n=7)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=5)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
    "structuredPatch": [
      {
        "oldStart": 55,
        "oldLines": 7,
        "newStart": 55,
        "newLines": 7,
        "lines": [
          " ",
          " # --- LIBERO-Long ---",
          " # CRM obs_only Long (seeds 42-47)",
          "-crm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # s42, s43, s44, s45, s46, s47",
          "+crm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50",
          " ",
          " # VLA-only Long (seeds 42-48)",
          " vla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52"
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

_source line 17_

<details open><summary>🔧 Tool call — Edit · `toolu_017CFkpoA7eyQjtZoNzQKvzQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "old_string": "adaptive_k_p25 = [0.15, 0.13]  # s42, s43",
  "new_string": "adaptive_k_p25 = [0.15, 0.13, 0.15]  # s42, s43, s44"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "bb56a77a-98e3-408a-87d0-59a36eab6e54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JRiTVK5PifHAuda555KCeV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 323,
      "cache_read_input_tokens": 30743,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 323
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

_source line 18 · 2026-05-20T06:03:54.787Z_

<details><summary>↩ Tool result · `toolu_017CFkpoA7eyQjtZoNzQKvzQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "b5b27fd9-0a32-48e9-9cb3-80c8e19f7a25",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
    "oldString": "adaptive_k_p25 = [0.15, 0.13]  # s42, s43",
    "newString": "adaptive_k_p25 = [0.15, 0.13, 0.15]  # s42, s43, s44",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]  # s42(k5), s43-r2, s44, s45, s47, s48, s51\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13]  # s42, s43\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_long)\nprint_group_stats(\"VLA-only (n=7)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=5)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
    "structuredPatch": [
      {
        "oldStart": 86,
        "oldLines": 7,
        "newStart": 86,
        "newLines": 7,
        "lines": [
          " argmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45",
          " ",
          " # --- Adaptive-K Object ---",
          "-adaptive_k_p25 = [0.15, 0.13]  # s42, s43",
          "+adaptive_k_p25 = [0.15, 0.13, 0.15]  # s42, s43, s44",
          " adaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44",
          " adaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44",
          " adaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44"
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

_source line 19_

Now update the hardcoded n= labels in print_group_stats calls and the comment header.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "a6f79145-5121-4e64-a9d9-5346f8d34917",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UtdwQHJjq8mP8oWDFthevE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 31066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

<details open><summary>🔧 Tool call — Edit · `toolu_01YaKxk5F7PVGmvpFvcs6vs2`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "old_string": "print_group_stats(\"CRM obs_only (n=6)\", crm_spatial)",
  "new_string": "print_group_stats(\"CRM obs_only (n=7)\", crm_spatial)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "41963aaf-4928-44b4-8ff5-e6e5342356c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UtdwQHJjq8mP8oWDFthevE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 31066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 21 · 2026-05-20T06:03:58.619Z_

<details><summary>↩ Tool result · `toolu_01YaKxk5F7PVGmvpFvcs6vs2`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "4304ee48-3b69-41c4-9eed-adb0e0e378db",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
    "oldString": "print_group_stats(\"CRM obs_only (n=6)\", crm_spatial)",
    "newString": "print_group_stats(\"CRM obs_only (n=7)\", crm_spatial)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]  # s42(k5), s43-r2, s44, s45, s47, s48, s51\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13, 0.15]  # s42, s43, s44\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_long)\nprint_group_stats(\"VLA-only (n=7)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=5)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
    "structuredPatch": [
      {
        "oldStart": 107,
        "oldLines": 7,
        "newStart": 107,
        "newLines": 7,
        "lines": [
          " # ============================================================================",
          " print(\"\\n1. LIBERO-SPATIAL\")",
          " print_separator('-')",
          "-print_group_stats(\"CRM obs_only (n=6)\", crm_spatial)",
          "+print_group_stats(\"CRM obs_only (n=7)\", crm_spatial)",
          " print_group_stats(\"VLA-only (n=9)\", vla_spatial)",
          " run_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)",
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

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_01JnifHm9RBuTuKqUWA4KuAy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "old_string": "print_group_stats(\"CRM obs_only (n=6)\", crm_long)\nprint_group_stats(\"VLA-only (n=7)\", vla_long)",
  "new_string": "print_group_stats(\"CRM obs_only (n=7)\", crm_long)\nprint_group_stats(\"VLA-only (n=11)\", vla_long)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "5ea701af-cc6d-4603-818f-1eaa1b748196",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSjKWyeEYowKzjsGh18Yrw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 31331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 373
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

_source line 23 · 2026-05-20T06:04:02.535Z_

<details><summary>↩ Tool result · `toolu_01JnifHm9RBuTuKqUWA4KuAy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "325e849a-abb8-4f2a-be78-d8bff249b946",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
    "oldString": "print_group_stats(\"CRM obs_only (n=6)\", crm_long)\nprint_group_stats(\"VLA-only (n=7)\", vla_long)",
    "newString": "print_group_stats(\"CRM obs_only (n=7)\", crm_long)\nprint_group_stats(\"VLA-only (n=11)\", vla_long)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]  # s42(k5), s43-r2, s44, s45, s47, s48, s51\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13, 0.15]  # s42, s43, s44\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=7)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_long)\nprint_group_stats(\"VLA-only (n=7)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=5)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
    "structuredPatch": [
      {
        "oldStart": 116,
        "oldLines": 8,
        "newStart": 116,
        "newLines": 8,
        "lines": [
          " # ============================================================================",
          " print(\"\\n\\n2. LIBERO-LONG\")",
          " print_separator('-')",
          "-print_group_stats(\"CRM obs_only (n=6)\", crm_long)",
          "-print_group_stats(\"VLA-only (n=7)\", vla_long)",
          "+print_group_stats(\"CRM obs_only (n=7)\", crm_long)",
          "+print_group_stats(\"VLA-only (n=11)\", vla_long)",
          " run_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)",
          " ",
          " # ============================================================================"
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

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_01KL3PUhjybNRZ8F3ma6X22G`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "old_string": "print_group_stats(\"VLA-only (n=5)\", vla_goal)",
  "new_string": "print_group_stats(\"VLA-only (n=6)\", vla_goal)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "e6401f78-7771-4fc5-a5b4-925b7738887a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016V4dhHk7uZ4YAWdT1oyFEJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 289,
      "cache_read_input_tokens": 31704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 289
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

_source line 25 · 2026-05-20T06:04:08.590Z_

<details><summary>↩ Tool result · `toolu_01KL3PUhjybNRZ8F3ma6X22G`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "0c276520-8f08-4c58-b3dd-e438fe1662e2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
    "oldString": "print_group_stats(\"VLA-only (n=5)\", vla_goal)",
    "newString": "print_group_stats(\"VLA-only (n=6)\", vla_goal)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]  # s42(k5), s43-r2, s44, s45, s47, s48, s51\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13, 0.15]  # s42, s43, s44\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=7)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=7)\", crm_long)\nprint_group_stats(\"VLA-only (n=11)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=5)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
    "structuredPatch": [
      {
        "oldStart": 126,
        "oldLines": 7,
        "newStart": 126,
        "newLines": 7,
        "lines": [
          " print(\"\\n\\n3. LIBERO-GOAL\")",
          " print_separator('-')",
          " print_group_stats(\"CRM obs_only (n=6)\", crm_goal)",
          "-print_group_stats(\"VLA-only (n=5)\", vla_goal)",
          "+print_group_stats(\"VLA-only (n=6)\", vla_goal)",
          " run_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)",
          " ",
          " # ============================================================================"
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

_source line 26_

<details open><summary>🔧 Tool call — Edit · `toolu_016dfwrqjtn9MHbVeXXSoHSz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "old_string": "print_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)",
  "new_string": "print_group_stats(\"Adaptive-K p25 (n=3)\", adaptive_k_p25)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "b9737111-3097-4eb5-b17e-312a8b277b91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5JdtvJ6Gd7b3KvAjWB9zm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 245,
      "cache_read_input_tokens": 31993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 245
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

_source line 27 · 2026-05-20T06:04:12.155Z_

<details><summary>↩ Tool result · `toolu_016dfwrqjtn9MHbVeXXSoHSz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "740c5596-6e08-4b49-af43-71d483f1162c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
    "oldString": "print_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)",
    "newString": "print_group_stats(\"Adaptive-K p25 (n=3)\", adaptive_k_p25)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]  # s42(k5), s43-r2, s44, s45, s47, s48, s51\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13, 0.15]  # s42, s43, s44\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=7)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=7)\", crm_long)\nprint_group_stats(\"VLA-only (n=11)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=6)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
    "structuredPatch": [
      {
        "oldStart": 168,
        "oldLines": 7,
        "newStart": 168,
        "newLines": 7,
        "lines": [
          " # ============================================================================",
          " print(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")",
          " print_separator('-')",
          "-print_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)",
          "+print_group_stats(\"Adaptive-K p25 (n=3)\", adaptive_k_p25)",
          " print_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)",
          " print_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)",
          " print_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)"
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

_source line 28_

Now update the `all_adaptive` count label (was n=11, now n=12) and the source comment lines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "ce6712d4-0096-47f7-b40e-6042a4403919",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NV5VCqjoabmY6pv71Uv7Xn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 32238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 255
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

_source line 29_

<details open><summary>🔧 Tool call — Edit · `toolu_01CmRJsbHcgtYnk7zRRme8UT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "old_string": "print_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)",
  "new_string": "print_group_stats(\"Adaptive-K all (n=12)\", all_adaptive)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "e604629f-adf0-403c-81b8-005aa7ca61cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NV5VCqjoabmY6pv71Uv7Xn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 32238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 255
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

_source line 30 · 2026-05-20T06:04:16.085Z_

<details><summary>↩ Tool result · `toolu_01CmRJsbHcgtYnk7zRRme8UT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "ac1336f1-21b3-4f63-8ba4-d3d82e92f989",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
    "oldString": "print_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)",
    "newString": "print_group_stats(\"Adaptive-K all (n=12)\", all_adaptive)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]  # s42(k5), s43-r2, s44, s45, s47, s48, s51\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13, 0.15]  # s42, s43, s44\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=7)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=7)\", crm_long)\nprint_group_stats(\"VLA-only (n=11)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=6)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=3)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
    "structuredPatch": [
      {
        "oldStart": 173,
        "oldLines": 7,
        "newStart": 173,
        "newLines": 7,
        "lines": [
          " print_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)",
          " print_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)",
          " all_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90",
          "-print_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)",
          "+print_group_stats(\"Adaptive-K all (n=12)\", all_adaptive)",
          " print_group_stats(\"VLA-only (n=8)\", vla_object)",
          " print_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)",
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

### Assistant

_source line 31_

Also update the data section header comment and the source comments for Long/Spatial/Goal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "94386c1f-c62a-4999-8903-a34558e1fbf6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNsNnFmoisLzd3mQjJ4Rtk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 32493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 273
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

_source line 32_

<details open><summary>🔧 Tool call — Edit · `toolu_01MXV2dAMFLnJ3LBz7dDYo7b`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "old_string": "# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback",
  "new_string": "# CRM obs_only norm02 K=10 (seeds 43-48,51); seed42 uses K=5 fallback"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "94a86c6e-595d-4fd7-aeff-aed0256f0c91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNsNnFmoisLzd3mQjJ4Rtk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 32493,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 273
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

_source line 33 · 2026-05-20T06:04:21.039Z_

<details><summary>↩ Tool result · `toolu_01MXV2dAMFLnJ3LBz7dDYo7b`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "bba23794-97d6-467b-8ea5-aecd0cfda59b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
    "oldString": "# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback",
    "newString": "# CRM obs_only norm02 K=10 (seeds 43-48,51); seed42 uses K=5 fallback",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]  # s42(k5), s43-r2, s44, s45, s47, s48, s51\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13, 0.15]  # s42, s43, s44\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=7)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=7)\", crm_long)\nprint_group_stats(\"VLA-only (n=11)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=6)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=3)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=12)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
    "structuredPatch": [
      {
        "oldStart": 47,
        "oldLines": 7,
        "newStart": 47,
        "newLines": 7,
        "lines": [
          " # ============================================================================",
          " ",
          " # --- LIBERO-Spatial ---",
          "-# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback",
          "+# CRM obs_only norm02 K=10 (seeds 43-48,51); seed42 uses K=5 fallback",
          " crm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]  # s42(k5), s43-r2, s44, s45, s47, s48, s51",
          " ",
          " # VLA-only Spatial (seeds 42-50)"
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

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_01G4aZQzPT892USupiPiX4e5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "old_string": "# CRM obs_only Long (seeds 42-47)",
  "new_string": "# CRM obs_only Long (seeds 42-47, 50)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "e18a8856-7504-4842-bc84-df7af45adcd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018nZMdeBDXRz1qfxxemai9t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 289,
      "cache_read_input_tokens": 32766,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 289
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

_source line 35 · 2026-05-20T06:04:25.140Z_

<details><summary>↩ Tool result · `toolu_01G4aZQzPT892USupiPiX4e5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "1584d0b6-abd5-44e6-8ae3-39336a9f9a47",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
    "oldString": "# CRM obs_only Long (seeds 42-47)",
    "newString": "# CRM obs_only Long (seeds 42-47, 50)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48,51); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]  # s42(k5), s43-r2, s44, s45, s47, s48, s51\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13, 0.15]  # s42, s43, s44\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=7)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=7)\", crm_long)\nprint_group_stats(\"VLA-only (n=11)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=6)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=3)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=12)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
    "structuredPatch": [
      {
        "oldStart": 54,
        "oldLines": 7,
        "newStart": 54,
        "newLines": 7,
        "lines": [
          " vla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50",
          " ",
          " # --- LIBERO-Long ---",
          "-# CRM obs_only Long (seeds 42-47)",
          "+# CRM obs_only Long (seeds 42-47, 50)",
          " crm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50",
          " ",
          " # VLA-only Long (seeds 42-48)"
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

_source line 36_

<details open><summary>🔧 Tool call — Edit · `toolu_01WYAsEznwH9inCGJPpQFfaR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "old_string": "# VLA-only Long (seeds 42-48)",
  "new_string": "# VLA-only Long (seeds 42-52)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "29486532-e91d-4636-8f23-26c0bdf4688d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012cPbo3aXocJKnooGvRWrLa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 33055,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 236
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

_source line 37 · 2026-05-20T06:04:28.591Z_

<details><summary>↩ Tool result · `toolu_01WYAsEznwH9inCGJPpQFfaR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "b4075013-7703-4f57-873a-e2ac65b3608e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
    "oldString": "# VLA-only Long (seeds 42-48)",
    "newString": "# VLA-only Long (seeds 42-52)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48,51); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]  # s42(k5), s43-r2, s44, s45, s47, s48, s51\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47, 50)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13, 0.15]  # s42, s43, s44\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=7)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=7)\", crm_long)\nprint_group_stats(\"VLA-only (n=11)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=6)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=3)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=12)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
    "structuredPatch": [
      {
        "oldStart": 57,
        "oldLines": 7,
        "newStart": 57,
        "newLines": 7,
        "lines": [
          " # CRM obs_only Long (seeds 42-47, 50)",
          " crm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50",
          " ",
          "-# VLA-only Long (seeds 42-48)",
          "+# VLA-only Long (seeds 42-52)",
          " vla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52",
          " ",
          " # --- LIBERO-Goal ---"
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

_source line 38_

<details open><summary>🔧 Tool call — Edit · `toolu_019TXW6v39Pw8MT3SaEdk3Sk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "old_string": "# VLA-only Goal (seeds 42-46)",
  "new_string": "# VLA-only Goal (seeds 42-46, 49)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "a4a467a5-afcf-44d4-acc7-e7ab7c0292ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EJQYdW5EHXyDz6gMBg2fa2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 231,
      "cache_read_input_tokens": 33291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 231
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

_source line 39 · 2026-05-20T06:04:32.347Z_

<details><summary>↩ Tool result · `toolu_019TXW6v39Pw8MT3SaEdk3Sk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "71f5ef6a-5cdb-4f88-9300-58d666e492c6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
    "oldString": "# VLA-only Goal (seeds 42-46)",
    "newString": "# VLA-only Goal (seeds 42-46, 49)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48,51); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]  # s42(k5), s43-r2, s44, s45, s47, s48, s51\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47, 50)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17, 0.14]  # s42, s43, s44, s45, s46, s47, s50\n\n# VLA-only Long (seeds 42-52)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]  # s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13, 0.15]  # s42, s43, s44\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=7)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=7)\", crm_long)\nprint_group_stats(\"VLA-only (n=11)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=6)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=3)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=12)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
    "structuredPatch": [
      {
        "oldStart": 64,
        "oldLines": 7,
        "newStart": 64,
        "newLines": 7,
        "lines": [
          " # CRM obs_only Goal (seeds 42-47)",
          " crm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47",
          " ",
          "-# VLA-only Goal (seeds 42-46)",
          "+# VLA-only Goal (seeds 42-46, 49)",
          " vla_goal = [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]  # s42, s43, s44-r2, s45, s46, s49",
          " ",
          " # --- LIBERO-Object ---"
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

_source line 40_

Running the script and saving output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "d72c9a83-9272-48d6-9a7a-bdce9686633b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8QwvvytaWxMSd6xaoA3B9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 338,
      "cache_read_input_tokens": 33522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 338
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

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01GbV7YTuvdrCVEWG8cJzVjx`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts && python3 statistical_analysis.py 2>&1 | tee statistical_analysis_output_v2.txt",
  "description": "Run updated statistical analysis script and save output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "81e23eae-2d09-4ebc-a4e9-26cd3de46907",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W8QwvvytaWxMSd6xaoA3B9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 338,
      "cache_read_input_tokens": 33522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 338
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

_source line 42 · 2026-05-20T06:04:37.832Z_

<details><summary>↩ Tool result · `toolu_01GbV7YTuvdrCVEWG8cJzVjx`</summary>

```text
================================================================================
STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments
All success rates are fractions (0.0 to 1.0)
Object benchmark primary CRM config: norm02 (ε=0.2), K=10
================================================================================

1. LIBERO-SPATIAL
--------------------------------------------------------------------------------
  CRM obs_only (n=7): n=7, mean=0.3457, std=0.0140, min=0.3200, max=0.3600
    values: [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]
  VLA-only (n=9): n=9, mean=0.2956, std=0.0113, min=0.2700, max=0.3100
    values: [0.3, 0.29, 0.31, 0.27, 0.3, 0.3, 0.3, 0.29, 0.3]

  CRM vs VLA-only:
    Difference: +0.0502 (+5.02 pp)
    Welch's t-test: t=7.7315, p=0.000007 ***
    Mann-Whitney U: U=63.0, p=0.000835 ***
    Cohen's d: 4.0071 (large)


2. LIBERO-LONG
--------------------------------------------------------------------------------
  CRM obs_only (n=7): n=7, mean=0.1700, std=0.0200, min=0.1400, max=0.2000
    values: [0.17, 0.15, 0.2, 0.18, 0.18, 0.17, 0.14]
  VLA-only (n=11): n=11, mean=0.1482, std=0.0223, min=0.1100, max=0.1800
    values: [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]

  CRM vs VLA-only:
    Difference: +0.0218 (+2.18 pp)
    Welch's t-test: t=2.1575, p=0.048849 *
    Mann-Whitney U: U=59.5, p=0.060644 n.s.
    Cohen's d: 1.0170 (large)


3. LIBERO-GOAL
--------------------------------------------------------------------------------
  CRM obs_only (n=6): n=6, mean=0.6817, std=0.0343, min=0.6400, max=0.7200
    values: [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]
  VLA-only (n=6): n=6, mean=0.6867, std=0.0388, min=0.6300, max=0.7300
    values: [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]

  CRM vs VLA-only:
    Difference: -0.0050 (-0.50 pp)
    Welch's t-test: t=-0.2364, p=0.817940 n.s.
    Mann-Whitney U: U=17.0, p=0.935736 n.s.
    Cohen's d: -0.1365 (negligible)


4. LIBERO-OBJECT
--------------------------------------------------------------------------------

  [PRIMARY: CRM norm02 K=10]
  CRM obs_only norm02 K=10 (n=6): n=6, mean=0.1683, std=0.0183, min=0.1500, max=0.2000
    values: [0.16, 0.16, 0.16, 0.15, 0.2, 0.18]
  VLA-only (n=8): n=8, mean=0.1088, std=0.0136, min=0.0900, max=0.1300
    values: [0.12, 0.12, 0.1, 0.11, 0.13, 0.1, 0.1, 0.09]

  CRM norm02 K=10 vs VLA-only:
    Difference: +0.0596 (+5.96 pp)
    Welch's t-test: t=6.6993, p=0.000095 ***
    Mann-Whitney U: U=48.0, p=0.002182 **
    Cohen's d: 3.7868 (large)

  [Supplementary: CRM norm01]
  CRM obs_only norm01 (n=6): n=6, mean=0.1750, std=0.0105, min=0.1600, max=0.1900
    values: [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]

  CRM norm01 vs VLA-only:
    Difference: +0.0663 (+6.62 pp)
    Welch's t-test: t=10.3058, p=0.000000 ***
    Mann-Whitney U: U=48.0, p=0.002232 **
    Cohen's d: 5.3538 (large)

  [Supplementary: CRM norm02 K=5]
  CRM obs_only norm02 K=5 (n=7): n=7, mean=0.1600, std=0.0216, min=0.1300, max=0.1900
    values: [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]

  CRM norm02 K=5 vs VLA-only:
    Difference: +0.0512 (+5.12 pp)
    Welch's t-test: t=5.4125, p=0.000312 ***
    Mann-Whitney U: U=55.5, p=0.001681 **
    Cohen's d: 2.8903 (large)


5. ARGMIN BASELINES (Object)
--------------------------------------------------------------------------------
  Argmin K=10 (n=5): n=5, mean=0.1240, std=0.0288, min=0.1000, max=0.1700
    values: [0.17, 0.13, 0.12, 0.1, 0.1]
  Argmin K=5 (n=4): n=4, mean=0.1300, std=0.0163, min=0.1100, max=0.1500
    values: [0.15, 0.13, 0.11, 0.13]
  VLA-only (n=8): n=8, mean=0.1088, std=0.0136, min=0.0900, max=0.1300
    values: [0.12, 0.12, 0.1, 0.11, 0.13, 0.1, 0.1, 0.09]
  CRM norm02 K=10 (n=6): n=6, mean=0.1683, std=0.0183, min=0.1500, max=0.2000
    values: [0.16, 0.16, 0.16, 0.15, 0.2, 0.18]

  Argmin K=10 vs VLA-only:

  Argmin K=10 vs VLA-only:
    Difference: +0.0152 (+1.52 pp)
    Welch's t-test: t=1.1093, p=0.316589 n.s.
    Mann-Whitney U: U=26.5, p=0.362759 n.s.
    Cohen's d: 0.7451 (medium)

  Argmin K=10 vs CRM norm02 K=10:

  Argmin K=10 vs CRM norm02:
    Difference: -0.0443 (-4.43 pp)
    Welch's t-test: t=-2.9747, p=0.022297 *
    Mann-Whitney U: U=4.0, p=0.052478 n.s.
    Cohen's d: -1.8803 (large)


6. ADAPTIVE-K BASELINES (Object)
--------------------------------------------------------------------------------
  Adaptive-K p25 (n=3): n=3, mean=0.1433, std=0.0115, min=0.1300, max=0.1500
    values: [0.15, 0.13, 0.15]
  Adaptive-K p50 (n=3): n=3, mean=0.1533, std=0.0115, min=0.1400, max=0.1600
    values: [0.16, 0.16, 0.14]
  Adaptive-K p75 (n=3): n=3, mean=0.1367, std=0.0208, min=0.1200, max=0.1600
    values: [0.12, 0.13, 0.16]
  Adaptive-K p90 (n=3): n=3, mean=0.1333, std=0.0115, min=0.1200, max=0.1400
    values: [0.12, 0.14, 0.14]
  Adaptive-K all (n=12): n=12, mean=0.1417, std=0.0147, min=0.1200, max=0.1600
    values: [0.15, 0.13, 0.15, 0.16, 0.16, 0.14, 0.12, 0.13, 0.16, 0.12, 0.14, 0.14]
  VLA-only (n=8): n=8, mean=0.1088, std=0.0136, min=0.0900, max=0.1300
    values: [0.12, 0.12, 0.1, 0.11, 0.13, 0.1, 0.1, 0.09]
  CRM norm02 K=10 (n=6): n=6, mean=0.1683, std=0.0183, min=0.1500, max=0.2000
    values: [0.16, 0.16, 0.16, 0.15, 0.2, 0.18]

  Adaptive-K (all) vs VLA-only:

  Adaptive-K all vs VLA-only:
    Difference: +0.0329 (+3.29 pp)
    Welch's t-test: t=5.1457, p=0.000098 ***
    Mann-Whitney U: U=91.0, p=0.000924 ***
    Cohen's d: 2.3102 (large)

  Adaptive-K (all) vs CRM norm02 K=10:

  Adaptive-K all vs CRM norm02:
    Difference: -0.0267 (-2.67 pp)
    Welch's t-test: t=-3.0991, p=0.014001 *
    Mann-Whitney U: U=8.5, p=0.009608 **
    Cohen's d: -1.6761 (large)


================================================================================
SUMMARY TABLE
================================================================================
Benchmark          Method                   n    Mean     Std  Δ vs VLA    p-value   Sig
--------------------------------------------------------------------------------
LIBERO-Spatial     CRM obs_only             7  0.3457  0.0140   +0.0502   0.000007   ***
LIBERO-Spatial     VLA-only                 9  0.2956  0.0113         —          —     —

LIBERO-Long        CRM obs_only             7  0.1700  0.0200   +0.0218   0.048849     *
LIBERO-Long        VLA-only                11  0.1482  0.0223         —          —     —

LIBERO-Goal        CRM obs_only             6  0.6817  0.0343   -0.0050   0.817940  n.s.
LIBERO-Goal        VLA-only                 6  0.6867  0.0388         —          —     —

LIBERO-Object      CRM norm02 K=10          6  0.1683  0.0183   +0.0596   0.000095   ***
LIBERO-Object      CRM norm01 (supp)        6  0.1750  0.0105   +0.0663   0.000000   ***
LIBERO-Object      CRM norm02 K=5 (supp)    7  0.1600  0.0216   +0.0512   0.000312   ***
LIBERO-Object      VLA-only                 8  0.1088  0.0136         —          —     —
LIBERO-Object      Argmin K=10              5  0.1240  0.0288   +0.0152   0.316589  n.s.
LIBERO-Object      Argmin K=5               4  0.1300  0.0163   +0.0212   0.073136  n.s.
LIBERO-Object      Adaptive-K (all)        12  0.1417  0.0147   +0.0329   0.000098   ***


================================================================================
KEY SIGNIFICANCE RESULTS
================================================================================

Comparison                                  Diff   t-test p     MW-U p   Sig   Cohen d
-------------------------------------------------------------------------------------
Spatial: CRM vs VLA                      +0.0502   0.000007   0.000835   ***   +4.0071
Long: CRM vs VLA                         +0.0218   0.048849   0.060644     *   +1.0170
Goal: CRM vs VLA                         -0.0050   0.817940   0.935736  n.s.   -0.1365
Object(norm02): CRM vs VLA               +0.0596   0.000095   0.002182   ***   +3.7868
Object(norm01-supp): CRM vs VLA          +0.0663   0.000000   0.002232   ***   +5.3538
Object: Argmin-K10 vs VLA                +0.0152   0.316589   0.362759  n.s.   +0.7451
Object: CRM-norm02 vs Argmin-K10         +0.0443   0.022297   0.052478     *   +1.8803
Object: Adaptive-K vs VLA                +0.0329   0.000098   0.000924   ***   +2.3102
Object: CRM-norm02 vs Adaptive-K         +0.0267   0.014001   0.009608     *   +1.6761


================================================================================
VERIFICATION NOTES
================================================================================
- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).
  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).
  Registry value retained but unverified.
- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).
- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).
- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.

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
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "c00bec55-eeae-483c-b78e-af6f1fe364dd",
  "tool_use_result": {
    "stdout": "================================================================================\nSTATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\nAll success rates are fractions (0.0 to 1.0)\nObject benchmark primary CRM config: norm02 (ε=0.2), K=10\n================================================================================\n\n1. LIBERO-SPATIAL\n--------------------------------------------------------------------------------\n  CRM obs_only (n=7): n=7, mean=0.3457, std=0.0140, min=0.3200, max=0.3600\n    values: [0.35, 0.34, 0.36, 0.34, 0.32, 0.35, 0.36]\n  VLA-only (n=9): n=9, mean=0.2956, std=0.0113, min=0.2700, max=0.3100\n    values: [0.3, 0.29, 0.31, 0.27, 0.3, 0.3, 0.3, 0.29, 0.3]\n\n  CRM vs VLA-only:\n    Difference: +0.0502 (+5.02 pp)\n    Welch's t-test: t=7.7315, p=0.000007 ***\n    Mann-Whitney U: U=63.0, p=0.000835 ***\n    Cohen's d: 4.0071 (large)\n\n\n2. LIBERO-LONG\n--------------------------------------------------------------------------------\n  CRM obs_only (n=7): n=7, mean=0.1700, std=0.0200, min=0.1400, max=0.2000\n    values: [0.17, 0.15, 0.2, 0.18, 0.18, 0.17, 0.14]\n  VLA-only (n=11): n=11, mean=0.1482, std=0.0223, min=0.1100, max=0.1800\n    values: [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14, 0.16, 0.16, 0.15, 0.17]\n\n  CRM vs VLA-only:\n    Difference: +0.0218 (+2.18 pp)\n    Welch's t-test: t=2.1575, p=0.048849 *\n    Mann-Whitney U: U=59.5, p=0.060644 n.s.\n    Cohen's d: 1.0170 (large)\n\n\n3. LIBERO-GOAL\n--------------------------------------------------------------------------------\n  CRM obs_only (n=6): n=6, mean=0.6817, std=0.0343, min=0.6400, max=0.7200\n    values: [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]\n  VLA-only (n=6): n=6, mean=0.6867, std=0.0388, min=0.6300, max=0.7300\n    values: [0.71, 0.69, 0.73, 0.63, 0.71, 0.65]\n\n  CRM vs VLA-only:\n    Difference: -0.0050 (-0.50 pp)\n    Welch's t-test: t=-0.2364, p=0.817940 n.s.\n    Mann-Whitney U: U=17.0, p=0.935736 n.s.\n    Cohen's d: -0.1365 (negligible)\n\n\n4. LIBERO-OBJECT\n--------------------------------------------------------------------------------\n\n  [PRIMARY: CRM norm02 K=10]\n  CRM obs_only norm02 K=10 (n=6): n=6, mean=0.1683, std=0.0183, min=0.1500, max=0.2000\n    values: [0.16, 0.16, 0.16, 0.15, 0.2, 0.18]\n  VLA-only (n=8): n=8, mean=0.1088, std=0.0136, min=0.0900, max=0.1300\n    values: [0.12, 0.12, 0.1, 0.11, 0.13, 0.1, 0.1, 0.09]\n\n  CRM norm02 K=10 vs VLA-only:\n    Difference: +0.0596 (+5.96 pp)\n    Welch's t-test: t=6.6993, p=0.000095 ***\n    Mann-Whitney U: U=48.0, p=0.002182 **\n    Cohen's d: 3.7868 (large)\n\n  [Supplementary: CRM norm01]\n  CRM obs_only norm01 (n=6): n=6, mean=0.1750, std=0.0105, min=0.1600, max=0.1900\n    values: [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]\n\n  CRM norm01 vs VLA-only:\n    Difference: +0.0663 (+6.62 pp)\n    Welch's t-test: t=10.3058, p=0.000000 ***\n    Mann-Whitney U: U=48.0, p=0.002232 **\n    Cohen's d: 5.3538 (large)\n\n  [Supplementary: CRM norm02 K=5]\n  CRM obs_only norm02 K=5 (n=7): n=7, mean=0.1600, std=0.0216, min=0.1300, max=0.1900\n    values: [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]\n\n  CRM norm02 K=5 vs VLA-only:\n    Difference: +0.0512 (+5.12 pp)\n    Welch's t-test: t=5.4125, p=0.000312 ***\n    Mann-Whitney U: U=55.5, p=0.001681 **\n    Cohen's d: 2.8903 (large)\n\n\n5. ARGMIN BASELINES (Object)\n--------------------------------------------------------------------------------\n  Argmin K=10 (n=5): n=5, mean=0.1240, std=0.0288, min=0.1000, max=0.1700\n    values: [0.17, 0.13, 0.12, 0.1, 0.1]\n  Argmin K=5 (n=4): n=4, mean=0.1300, std=0.0163, min=0.1100, max=0.1500\n    values: [0.15, 0.13, 0.11, 0.13]\n  VLA-only (n=8): n=8, mean=0.1088, std=0.0136, min=0.0900, max=0.1300\n    values: [0.12, 0.12, 0.1, 0.11, 0.13, 0.1, 0.1, 0.09]\n  CRM norm02 K=10 (n=6): n=6, mean=0.1683, std=0.0183, min=0.1500, max=0.2000\n    values: [0.16, 0.16, 0.16, 0.15, 0.2, 0.18]\n\n  Argmin K=10 vs VLA-only:\n\n  Argmin K=10 vs VLA-only:\n    Difference: +0.0152 (+1.52 pp)\n    Welch's t-test: t=1.1093, p=0.316589 n.s.\n    Mann-Whitney U: U=26.5, p=0.362759 n.s.\n    Cohen's d: 0.7451 (medium)\n\n  Argmin K=10 vs CRM norm02 K=10:\n\n  Argmin K=10 vs CRM norm02:\n    Difference: -0.0443 (-4.43 pp)\n    Welch's t-test: t=-2.9747, p=0.022297 *\n    Mann-Whitney U: U=4.0, p=0.052478 n.s.\n    Cohen's d: -1.8803 (large)\n\n\n6. ADAPTIVE-K BASELINES (Object)\n--------------------------------------------------------------------------------\n  Adaptive-K p25 (n=3): n=3, mean=0.1433, std=0.0115, min=0.1300, max=0.1500\n    values: [0.15, 0.13, 0.15]\n  Adaptive-K p50 (n=3): n=3, mean=0.1533, std=0.0115, min=0.1400, max=0.1600\n    values: [0.16, 0.16, 0.14]\n  Adaptive-K p75 (n=3): n=3, mean=0.1367, std=0.0208, min=0.1200, max=0.1600\n    values: [0.12, 0.13, 0.16]\n  Adaptive-K p90 (n=3): n=3, mean=0.1333, std=0.0115, min=0.1200, max=0.1400\n    values: [0.12, 0.14, 0.14]\n  Adaptive-K all (n=12): n=12, mean=0.1417, std=0.0147, min=0.1200, max=0.1600\n    values: [0.15, 0.13, 0.15, 0.16, 0.16, 0.14, 0.12, 0.13, 0.16, 0.12, 0.14, 0.14]\n  VLA-only (n=8): n=8, mean=0.1088, std=0.0136, min=0.0900, max=0.1300\n    values: [0.12, 0.12, 0.1, 0.11, 0.13, 0.1, 0.1, 0.09]\n  CRM norm02 K=10 (n=6): n=6, mean=0.1683, std=0.0183, min=0.1500, max=0.2000\n    values: [0.16, 0.16, 0.16, 0.15, 0.2, 0.18]\n\n  Adaptive-K (all) vs VLA-only:\n\n  Adaptive-K all vs VLA-only:\n    Difference: +0.0329 (+3.29 pp)\n    Welch's t-test: t=5.1457, p=0.000098 ***\n    Mann-Whitney U: U=91.0, p=0.000924 ***\n    Cohen's d: 2.3102 (large)\n\n  Adaptive-K (all) vs CRM norm02 K=10:\n\n  Adaptive-K all vs CRM norm02:\n    Difference: -0.0267 (-2.67 pp)\n    Welch's t-test: t=-3.0991, p=0.014001 *\n    Mann-Whitney U: U=8.5, p=0.009608 **\n    Cohen's d: -1.6761 (large)\n\n\n================================================================================\nSUMMARY TABLE\n================================================================================\nBenchmark          Method                   n    Mean     Std  Δ vs VLA    p-value   Sig\n--------------------------------------------------------------------------------\nLIBERO-Spatial     CRM obs_only             7  0.3457  0.0140   +0.0502   0.000007   ***\nLIBERO-Spatial     VLA-only                 9  0.2956  0.0113         —          —     —\n\nLIBERO-Long        CRM obs_only             7  0.1700  0.0200   +0.0218   0.048849     *\nLIBERO-Long        VLA-only                11  0.1482  0.0223         —          —     —\n\nLIBERO-Goal        CRM obs_only             6  0.6817  0.0343   -0.0050   0.817940  n.s.\nLIBERO-Goal        VLA-only                 6  0.6867  0.0388         —          —     —\n\nLIBERO-Object      CRM norm02 K=10          6  0.1683  0.0183   +0.0596   0.000095   ***\nLIBERO-Object      CRM norm01 (supp)        6  0.1750  0.0105   +0.0663   0.000000   ***\nLIBERO-Object      CRM norm02 K=5 (supp)    7  0.1600  0.0216   +0.0512   0.000312   ***\nLIBERO-Object      VLA-only                 8  0.1088  0.0136         —          —     —\nLIBERO-Object      Argmin K=10              5  0.1240  0.0288   +0.0152   0.316589  n.s.\nLIBERO-Object      Argmin K=5               4  0.1300  0.0163   +0.0212   0.073136  n.s.\nLIBERO-Object      Adaptive-K (all)        12  0.1417  0.0147   +0.0329   0.000098   ***\n\n\n================================================================================\nKEY SIGNIFICANCE RESULTS\n================================================================================\n\nComparison                                  Diff   t-test p     MW-U p   Sig   Cohen d\n-------------------------------------------------------------------------------------\nSpatial: CRM vs VLA                      +0.0502   0.000007   0.000835   ***   +4.0071\nLong: CRM vs VLA                         +0.0218   0.048849   0.060644     *   +1.0170\nGoal: CRM vs VLA                         -0.0050   0.817940   0.935736  n.s.   -0.1365\nObject(norm02): CRM vs VLA               +0.0596   0.000095   0.002182   ***   +3.7868\nObject(norm01-supp): CRM vs VLA          +0.0663   0.000000   0.002232   ***   +5.3538\nObject: Argmin-K10 vs VLA                +0.0152   0.316589   0.362759  n.s.   +0.7451\nObject: CRM-norm02 vs Argmin-K10         +0.0443   0.022297   0.052478     *   +1.8803\nObject: Adaptive-K vs VLA                +0.0329   0.000098   0.000924   ***   +2.3102\nObject: CRM-norm02 vs Adaptive-K         +0.0267   0.014001   0.009608     *   +1.6761\n\n\n================================================================================\nVERIFICATION NOTES\n================================================================================\n- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\n  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\n  Registry value retained but unverified.\n- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\n- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\n- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\n\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\n\n================================================================================\nEND OF ANALYSIS\n================================================================================",
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

_source line 43_

脚本运行成功，输出已保存到 `statistical_analysis_output_v2.txt`。

### 关键变化对比（v1 → v2）

| Comparison | 旧 p-value | 新 p-value | 变化 |
|---|---|---|---|
| **Long: CRM vs VLA** | 0.0276 * (n=6v7) | **0.0488 *** (n=7v11) | p 变大，但仍 *（VLA-Long 加入4个偏高的seed拉高了baseline mean：0.1414→0.1482） |
| **Goal: CRM vs VLA** | 0.5819 n.s. (n=6v5) | **0.8179 n.s.** (n=6v6) | 新seed49=0.65拉低VLA-Goal均值（0.694→0.687），差异更小，仍不显著 |
| **Spatial: CRM vs VLA** | p≈7e-6 *** | **p≈7e-6 ***（n=7v9）** | CRM加了0.36，mean微升0.3433→0.3457，显著性不变 |
| **Long CRM mean** | 0.1750 (n=6) | **0.1700 (n=7)** | seed50=0.14 拉低了 CRM-Long 均值 |
| **Adaptive-K all** | n=11 | **n=12** | p25加入0.15，整体mean 0.1409→0.1417 |

**核心影响**：Long 的 p-value 从 0.028 升至 0.049，刚好卡在 0.05 边缘——VLA-Long 新增的4个seed（0.15-0.17）偏高，缩小了 CRM-VLA 差距。MW-U 检验已不显著（p=0.061）。其余结论不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "uuid": "d698afba-03d6-4601-a997-13ccb8c1d6a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QuNCUfjQjmggRdr5vpD1Kx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4150,
      "cache_read_input_tokens": 33860,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4150
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

### Task result

_source line 44_

脚本运行成功，输出已保存到 `statistical_analysis_output_v2.txt`。

### 关键变化对比（v1 → v2）

| Comparison | 旧 p-value | 新 p-value | 变化 |
|---|---|---|---|
| **Long: CRM vs VLA** | 0.0276 * (n=6v7) | **0.0488 *** (n=7v11) | p 变大，但仍 *（VLA-Long 加入4个偏高的seed拉高了baseline mean：0.1414→0.1482） |
| **Goal: CRM vs VLA** | 0.5819 n.s. (n=6v5) | **0.8179 n.s.** (n=6v6) | 新seed49=0.65拉低VLA-Goal均值（0.694→0.687），差异更小，仍不显著 |
| **Spatial: CRM vs VLA** | p≈7e-6 *** | **p≈7e-6 ***（n=7v9）** | CRM加了0.36，mean微升0.3433→0.3457，显著性不变 |
| **Long CRM mean** | 0.1750 (n=6) | **0.1700 (n=7)** | seed50=0.14 拉低了 CRM-Long 均值 |
| **Adaptive-K all** | n=11 | **n=12** | p25加入0.15，整体mean 0.1409→0.1417 |

**核心影响**：Long 的 p-value 从 0.028 升至 0.049，刚好卡在 0.05 边缘——VLA-Long 新增的4个seed（0.15-0.17）偏高，缩小了 CRM-VLA 差距。MW-U 检验已不显著（p=0.061）。其余结论不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 88046,
  "duration_api_ms": 86933,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "fe1021a9-5b13-4647-b97b-ed019f2bbc49",
  "total_cost_usd": 0.52298475,
  "usage": {
    "input_tokens": 18,
    "cache_creation_input_tokens": 26169,
    "cache_read_input_tokens": 513667,
    "output_tokens": 4034,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 26169,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 529,
        "cache_read_input_tokens": 33860,
        "cache_creation_input_tokens": 4150,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4150
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1580,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001655,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 18,
      "outputTokens": 4034,
      "cacheReadInputTokens": 513667,
      "cacheCreationInputTokens": 26169,
      "webSearchRequests": 0,
      "costUSD": 0.52132975,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "071b027d-1f2e-4140-a5a4-8248cbf8c215"
}
```

</details>

---
